#!/usr/bin/env python3
"""
download_cache.py — Fetch every URL in research/source_urls.md into research/cache/.

Cache files are named by SHA-256 of the URL (deterministic, collision-free).
Already-cached URLs are skipped. Re-run any time to fetch new URLs.

research/cache/manifest.json  maps  url → {file, content_type, status, size, fetched_at}

Usage:
    python scripts/download_cache.py [--workers 50] [--timeout 20] [--force]
"""

import argparse
import asyncio
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import aiohttp
except ImportError:
    sys.exit("pip install aiohttp")

ROOT = Path(__file__).parent.parent
CACHE_DIR = ROOT / "research" / "cache"
MANIFEST_PATH = CACHE_DIR / "manifest.json"
SOURCE_URLS = ROOT / "research" / "source_urls.md"

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; SpeakerResearchBot/1.0)",
           "Accept-Language": "en-GB,en;q=0.9"}

_EXT_MAP = {
    "text/html": ".html",
    "application/pdf": ".pdf",
    "application/json": ".json",
    "application/xhtml+xml": ".html",
    "text/xml": ".xml",
    "application/xml": ".xml",
}


def url_cache_name(url: str, content_type: str) -> str:
    h = hashlib.sha256(url.encode()).hexdigest()
    ct_base = content_type.split(";")[0].strip().lower()
    ext = _EXT_MAP.get(ct_base)
    if not ext:
        # Guess from URL
        lower = url.lower().split("?")[0]
        if lower.endswith(".pdf"):
            ext = ".pdf"
        elif lower.endswith(".json"):
            ext = ".json"
        else:
            ext = ".html"
    return h + ext


def load_manifest() -> dict:
    if MANIFEST_PATH.exists():
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    return {}


def save_manifest(manifest: dict, lock: asyncio.Lock = None) -> None:
    MANIFEST_PATH.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )


def read_url_list(force: bool, manifest: dict) -> list[str]:
    if not SOURCE_URLS.exists():
        sys.exit(f"Not found: {SOURCE_URLS}\nRun scripts/extract_urls.py first.")
    urls = []
    for line in SOURCE_URLS.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if force or line not in manifest:
            urls.append(line)
    return list(dict.fromkeys(urls))  # preserve order, deduplicate


async def fetch_one(url: str, session: aiohttp.ClientSession, timeout: int) -> dict | None:
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=timeout),
                               headers=HEADERS, allow_redirects=True) as r:
            ct = r.headers.get("Content-Type", "text/html")
            body = await r.read()
            return {"status": r.status, "content_type": ct,
                    "body": body, "final_url": str(r.url)}
    except asyncio.TimeoutError:
        return {"status": 0, "error": "timeout"}
    except aiohttp.ClientError as e:
        return {"status": 0, "error": str(e)}
    except Exception as e:
        return {"status": 0, "error": str(e)}


async def worker(queue: asyncio.Queue, session: aiohttp.ClientSession,
                 timeout: int, manifest: dict, manifest_lock: asyncio.Lock,
                 counters: dict) -> None:
    while True:
        url = await queue.get()
        if url is None:
            queue.task_done()
            break

        result = await fetch_one(url, session, timeout)
        counters["total"] += 1

        if result and result["status"] == 200:
            ct = result["content_type"]
            fname = url_cache_name(url, ct)
            fpath = CACHE_DIR / fname
            fpath.write_bytes(result["body"])
            entry = {
                "file": fname,
                "content_type": ct,
                "status": 200,
                "size_bytes": len(result["body"]),
                "fetched_at": datetime.now(timezone.utc).isoformat(),
                "final_url": result.get("final_url", url),
            }
            async with manifest_lock:
                manifest[url] = entry
                save_manifest(manifest)
            counters["ok"] += 1
            print(f"[OK  {len(result['body'])//1024:4d}kB] {url}")
        else:
            err = result.get("error", f"HTTP {result.get('status')}") if result else "no response"
            counters["err"] += 1
            print(f"[ERR]  {url}  → {err}")

        queue.task_done()


async def run(args):
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    manifest = load_manifest()
    urls = read_url_list(args.force, manifest)

    if not urls:
        print("Nothing to fetch — all URLs already cached. Use --force to re-fetch.")
        return

    print(f"Fetching {len(urls)} URLs with {args.workers} workers…")
    counters = {"total": 0, "ok": 0, "err": 0}
    manifest_lock = asyncio.Lock()
    queue: asyncio.Queue = asyncio.Queue()

    connector = aiohttp.TCPConnector(limit=args.workers, ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
        workers = [
            asyncio.create_task(
                worker(queue, session, args.timeout, manifest, manifest_lock, counters)
            )
            for _ in range(args.workers)
        ]
        for url in urls:
            await queue.put(url)
        await queue.join()
        for _ in workers:
            await queue.put(None)
        await asyncio.gather(*workers)

    print(f"\n{counters['ok']} fetched, {counters['err']} errors  -> {MANIFEST_PATH}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=50)
    ap.add_argument("--timeout", type=int, default=20)
    ap.add_argument("--force", action="store_true", help="Re-fetch even if already cached")
    args = ap.parse_args()
    asyncio.run(run(args))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
crawl_cache.py — Durable BFS web crawler. Builds research/cache/.

DURABILITY DESIGN
-----------------
Kill and restart at any time — no data is lost:

  1. Every downloaded file is written as <sha256>.partial first, then
     atomically renamed to its final name (<sha256>.html/.pdf/etc.).
     A killed process leaves .partial files; startup deletes them.

  2. The manifest (manifest.json) is written via atomic rename from
     manifest.json.tmp so it is never half-written.

  3. Newly discovered URLs (PDFs found inside HTML pages) are appended
     to source_urls.md immediately per URL (inside asyncio.Lock).
     On restart, the BFS queue is rebuilt from source_urls.md minus
     manifest — all discovered URLs survive a kill.

RESTART BEHAVIOUR
-----------------
  source_urls.md = all URLs we know about (seeds + discovered)
  manifest.json  = all URLs successfully downloaded (HTTP 200)
  On restart: fetch everything in source_urls.md not in manifest.
  429/404/errors are not recorded in the manifest, so they are
  automatically retried on next run.

PARALLELISM
-----------
No artificial delays. 200 workers by default — pure network I/O,
saturate the pipe. If a server 429s, that URL stays out of the
manifest and is retried next run.

USAGE
-----
  python scripts/crawl_cache.py
  python scripts/crawl_cache.py --workers 200 --timeout 20
  python scripts/crawl_cache.py --force   # re-fetch everything
"""

import argparse
import asyncio
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse

try:
    import aiohttp
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit("pip install aiohttp beautifulsoup4")

ROOT = Path(__file__).parent.parent
CACHE_DIR = ROOT / "research" / "cache"
MANIFEST_PATH = CACHE_DIR / "manifest.json"
SOURCE_URLS = ROOT / "research" / "source_urls.md"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; SpeakerResearchBot/1.0)",
    "Accept-Language": "en-GB,en;q=0.9",
}

_CONTENT_TYPE_EXT: dict[str, str] = {
    "text/html":             ".html",
    "application/pdf":       ".pdf",
    "application/json":      ".json",
    "application/xhtml+xml": ".html",
    "text/xml":              ".xml",
    "application/xml":       ".xml",
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _cache_filename(url: str, content_type: str) -> str:
    h = hashlib.sha256(url.encode()).hexdigest()
    ct = content_type.split(";")[0].strip().lower()
    ext = _CONTENT_TYPE_EXT.get(ct)
    if not ext:
        lower = url.lower().split("?")[0]
        ext = ".pdf" if lower.endswith(".pdf") else ".json" if lower.endswith(".json") else ".html"
    return h + ext


def _is_pdf(url: str) -> bool:
    return url.lower().split("?")[0].endswith(".pdf")


def _discover_from_html(html: str, base_url: str) -> list[str]:
    """Extract PDF links from an HTML page — the only URLs we follow."""
    try:
        soup = BeautifulSoup(html, "html.parser")
    except Exception:
        return []
    results = []
    for tag in soup.find_all("a", href=True):
        href = tag["href"].strip()
        if not href or href.startswith(("#", "javascript:", "mailto:")):
            continue
        abs_url = urljoin(base_url, href).split("#")[0].rstrip(".,;)>")
        if abs_url.startswith("http") and _is_pdf(abs_url):
            results.append(abs_url)
    return list(dict.fromkeys(results))


# ---------------------------------------------------------------------------
# Atomic I/O
# ---------------------------------------------------------------------------

def _atomic_write_bytes(path: Path, data: bytes) -> None:
    partial = path.with_suffix(path.suffix + ".partial")
    partial.write_bytes(data)
    partial.replace(path)


def _atomic_write_manifest(manifest: dict) -> None:
    tmp = MANIFEST_PATH.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    tmp.replace(MANIFEST_PATH)


def _startup_cleanup() -> None:
    partials = list(CACHE_DIR.glob("*.partial"))
    if partials:
        for p in partials:
            p.unlink()
        print(f"Cleaned {len(partials)} incomplete .partial file(s) from previous run.")


def load_manifest() -> dict:
    if MANIFEST_PATH.exists():
        try:
            return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print("Warning: manifest.json corrupt — starting fresh.")
            return {}
    return {}


# ---------------------------------------------------------------------------
# source_urls.md
# ---------------------------------------------------------------------------

def read_pending_urls(manifest: dict, force: bool) -> list[str]:
    if not SOURCE_URLS.exists():
        sys.exit(f"Not found: {SOURCE_URLS}\nRun scripts/extract_urls.py first.")
    urls = []
    for line in SOURCE_URLS.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if force or line not in manifest:
            urls.append(line)
    return list(dict.fromkeys(urls))


async def _append_discovered(url: str, file_lock: asyncio.Lock) -> None:
    async with file_lock:
        existing = set()
        if SOURCE_URLS.exists():
            for line in SOURCE_URLS.read_text(encoding="utf-8").splitlines():
                existing.add(line.strip())
        if url not in existing:
            with SOURCE_URLS.open("a", encoding="utf-8") as f:
                f.write(url + "\n")


# ---------------------------------------------------------------------------
# Async fetch + worker
# ---------------------------------------------------------------------------

async def fetch_one(url: str, session: aiohttp.ClientSession, timeout: int):
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=timeout),
                               headers=HEADERS, allow_redirects=True) as r:
            ct = r.headers.get("Content-Type", "text/html")
            body = await r.read()
            return r.status, ct, body, str(r.url)
    except asyncio.TimeoutError:
        return 0, None, None, "timeout"
    except aiohttp.ClientError as e:
        return 0, None, None, str(e)
    except Exception as e:
        return 0, None, None, str(e)


async def worker(
    queue: asyncio.Queue,
    session: aiohttp.ClientSession,
    timeout: int,
    manifest: dict,
    manifest_lock: asyncio.Lock,
    seen: set,
    seen_lock: asyncio.Lock,
    file_lock: asyncio.Lock,
    counters: dict,
) -> None:
    while True:
        url = await queue.get()
        if url is None:
            queue.task_done()
            break

        status, ct, body, info = await fetch_one(url, session, timeout)
        counters["total"] += 1

        if status == 200 and body:
            fname = _cache_filename(url, ct)
            _atomic_write_bytes(CACHE_DIR / fname, body)

            async with manifest_lock:
                manifest[url] = {
                    "file": fname,
                    "content_type": ct,
                    "status": 200,
                    "size_bytes": len(body),
                    "fetched_at": datetime.now(timezone.utc).isoformat(),
                    "final_url": info,
                }
                _atomic_write_manifest(manifest)

            counters["ok"] += 1
            print(f"[OK  {len(body)//1024:4d}kB] {url}")

            # Follow PDF links discovered in HTML pages
            if "html" in ct.lower() and not _is_pdf(url):
                discovered = _discover_from_html(body.decode("utf-8", errors="replace"), url)
                async with seen_lock:
                    fresh = [u for u in discovered if u not in seen]
                    for u in fresh:
                        seen.add(u)
                for u in fresh:
                    await _append_discovered(u, file_lock)
                    await queue.put(u)
        else:
            err = info if status == 0 else f"HTTP {status}"
            counters["err"] += 1
            print(f"[ERR]  {url}  -> {err}")

        queue.task_done()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

async def run(args):
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    _startup_cleanup()

    manifest = load_manifest()
    pending = read_pending_urls(manifest, args.force)

    if not pending:
        print("All URLs already cached. Use --force to re-fetch.")
        return

    print(f"Pending: {len(pending)}  |  Already cached: {len(manifest)}  |  Workers: {args.workers}")

    seen: set = set(manifest.keys()) | set(pending)
    manifest_lock = asyncio.Lock()
    seen_lock = asyncio.Lock()
    file_lock = asyncio.Lock()
    counters = {"total": 0, "ok": 0, "err": 0}

    queue: asyncio.Queue = asyncio.Queue()
    for url in pending:
        await queue.put(url)

    connector = aiohttp.TCPConnector(limit=args.workers, ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
        workers = [
            asyncio.create_task(worker(
                queue, session, args.timeout,
                manifest, manifest_lock,
                seen, seen_lock,
                file_lock, counters,
            ))
            for _ in range(args.workers)
        ]
        await queue.join()
        for _ in workers:
            await queue.put(None)
        await asyncio.gather(*workers)

    print(f"\n{counters['ok']} fetched  |  {counters['err']} errors  |  {len(manifest)} total cached")


def main():
    ap = argparse.ArgumentParser(
        description="Durable BFS crawler. Kill and restart safely at any time."
    )
    ap.add_argument("--workers", type=int, default=200,
                    help="Parallel connections (default 200)")
    ap.add_argument("--timeout", type=int, default=20,
                    help="Per-request timeout seconds (default 20)")
    ap.add_argument("--force", action="store_true",
                    help="Re-fetch everything, ignoring manifest")
    asyncio.run(run(ap.parse_args()))


if __name__ == "__main__":
    main()

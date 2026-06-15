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
     to source_urls.md immediately and individually (file-append is
     atomic for small writes). On restart, the BFS queue is rebuilt
     from source_urls.md minus manifest — all discovered URLs survive.

RESTART BEHAVIOUR
-----------------
  - source_urls.md  : all URLs we know about (seeds + discovered)
  - manifest.json   : all URLs successfully downloaded
  - On restart: fetch everything in source_urls.md not in manifest.
    The in-memory BFS queue is lost but source_urls.md is the durable
    equivalent, so nothing is skipped.

RATE LIMITING
-------------
Full 50-worker parallelism everywhere except sites that 429 us.
Add entries to _DOMAIN_DELAY to throttle specific domains.

USAGE
-----
  python scripts/crawl_cache.py [--workers 50] [--timeout 20] [--force]
  python scripts/crawl_cache.py --force   # re-fetch everything
"""

import argparse
import asyncio
import hashlib
import json
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse

try:
    import aiohttp
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit("pip install aiohttp beautifulsoup4")

# Per-domain minimum gap in seconds (0 = no limit).
_DOMAIN_DELAY: dict[str, float] = {
    "loudspeakerdatabase.com":     5.0,
    "www.loudspeakerdatabase.com": 5.0,
}

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

# PDF links on product pages are followed automatically.
# HTML links are never followed (we don't want to crawl the whole internet).
_PDF_FOLLOW_DOMAINS = {
    "doc.soundimports.nl",
    "sbacoustics.com", "www.sbacoustics.com",
    "seas.no", "www.seas.no",
    "scan-speak.dk", "www.scan-speak.dk",
    "daytonaudio.com", "www.daytonaudio.com",
    "visaton.de", "www.visaton.de",
    "beyma.com", "www.beyma.com",
    "morel.co.il", "www.morel.co.il",
    "wavecor.com", "www.wavecor.com",
    "fast-images.static-thomann.de",
    "cdn.shopify.com",
    "www.parts-express.com",
    "www.falconacoustics.co.uk",
    "www.hificollective.co.uk",
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


def _should_follow(url: str) -> bool:
    """Return True if this URL should be added to the BFS queue."""
    try:
        p = urlparse(url)
    except Exception:
        return False
    if not p.path.lower().endswith(".pdf"):
        return False
    domain = p.netloc.lower()
    # Allow any PDF from trusted PDF domains, and any PDF from the same
    # product-page domains (many shops host datasheets on their own CDN).
    return True  # follow all PDFs — they'll 404 if they don't exist


def _discover_from_html(html: str, base_url: str) -> list[str]:
    """Extract followable URLs from an HTML page (PDFs only)."""
    try:
        soup = BeautifulSoup(html, "html.parser")
    except Exception:
        return []
    results = []
    for tag in soup.find_all("a", href=True):
        href = tag["href"].strip()
        if not href or href.startswith(("#", "javascript:", "mailto:")):
            continue
        abs_url = urljoin(base_url, href).split("#")[0]
        # Strip trailing ) from malformed markdown-derived URLs
        abs_url = abs_url.rstrip(".,;)>")
        if abs_url.startswith("http") and _should_follow(abs_url):
            results.append(abs_url)
    return list(dict.fromkeys(results))


# ---------------------------------------------------------------------------
# Atomic I/O
# ---------------------------------------------------------------------------

def _atomic_write_bytes(path: Path, data: bytes) -> None:
    """Write bytes atomically: write to .partial then rename."""
    partial = path.with_suffix(path.suffix + ".partial")
    partial.write_bytes(data)
    partial.replace(path)  # os.replace() — atomic on Windows + POSIX


def _atomic_write_manifest(manifest: dict) -> None:
    """Write manifest atomically via temp file."""
    tmp = MANIFEST_PATH.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    tmp.replace(MANIFEST_PATH)


def _startup_cleanup() -> None:
    """Delete any .partial files left by a previous killed run."""
    partials = list(CACHE_DIR.glob("*.partial"))
    if partials:
        for p in partials:
            p.unlink()
        print(f"Cleaned up {len(partials)} incomplete .partial file(s) from previous run.")


def load_manifest() -> dict:
    if MANIFEST_PATH.exists():
        try:
            return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print("Warning: manifest.json is corrupt — starting fresh.")
            return {}
    return {}


# ---------------------------------------------------------------------------
# source_urls.md helpers
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


async def _persist_discovered_url(url: str, file_lock: asyncio.Lock) -> None:
    """Append a single discovered URL to source_urls.md immediately."""
    async with file_lock:
        existing = set()
        if SOURCE_URLS.exists():
            for line in SOURCE_URLS.read_text(encoding="utf-8").splitlines():
                existing.add(line.strip())
        if url not in existing:
            with SOURCE_URLS.open("a", encoding="utf-8") as f:
                f.write(url + "\n")


# ---------------------------------------------------------------------------
# Per-domain rate limiter
# ---------------------------------------------------------------------------

class DomainThrottle:
    def __init__(self):
        self._locks: dict[str, asyncio.Lock] = defaultdict(asyncio.Lock)
        self._last: dict[str, float] = defaultdict(float)

    async def wait(self, url: str) -> None:
        domain = urlparse(url).netloc.lower()
        delay = _DOMAIN_DELAY.get(domain, 0.0)
        if delay <= 0:
            return
        async with self._locks[domain]:
            elapsed = time.monotonic() - self._last[domain]
            if elapsed < delay:
                await asyncio.sleep(delay - elapsed)
            self._last[domain] = time.monotonic()


# ---------------------------------------------------------------------------
# Async worker
# ---------------------------------------------------------------------------

async def fetch_one(url: str, session: aiohttp.ClientSession,
                    timeout: int, throttle: DomainThrottle):
    await throttle.wait(url)
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
    throttle: DomainThrottle,
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

        status, ct, body, info = await fetch_one(url, session, timeout, throttle)
        counters["total"] += 1

        if status == 200 and body:
            fname = _cache_filename(url, ct)
            # Atomic write: .partial → final
            _atomic_write_bytes(CACHE_DIR / fname, body)

            entry = {
                "file": fname,
                "content_type": ct,
                "status": 200,
                "size_bytes": len(body),
                "fetched_at": datetime.now(timezone.utc).isoformat(),
                "final_url": info,
            }
            # Atomic manifest update
            async with manifest_lock:
                manifest[url] = entry
                _atomic_write_manifest(manifest)

            counters["ok"] += 1
            print(f"[OK  {len(body)//1024:4d}kB] {url}")

            # Discover PDF links from HTML pages and add to queue
            if "html" in ct.lower() and not _is_pdf(url):
                discovered = _discover_from_html(body.decode("utf-8", errors="replace"), url)
                async with seen_lock:
                    fresh = [u for u in discovered if u not in seen]
                    for u in fresh:
                        seen.add(u)
                for u in fresh:
                    # Persist to source_urls.md immediately (survives kill)
                    await _persist_discovered_url(u, file_lock)
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
        print("Nothing to fetch — all seed URLs already cached.")
        print("Use --force to re-fetch, or run extract_urls.py to find new URLs.")
        return

    print(f"Pending: {len(pending)} URLs | Workers: {args.workers} | Cache: {len(manifest)} already done")

    seen: set = set(manifest.keys())
    seen.update(pending)

    manifest_lock = asyncio.Lock()
    seen_lock = asyncio.Lock()
    file_lock = asyncio.Lock()
    counters = {"total": 0, "ok": 0, "err": 0}
    throttle = DomainThrottle()

    queue: asyncio.Queue = asyncio.Queue()
    for url in pending:
        await queue.put(url)

    connector = aiohttp.TCPConnector(limit=args.workers, ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
        workers = [
            asyncio.create_task(worker(
                queue, session, args.timeout, throttle,
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

    print(f"\n{counters['ok']} fetched  |  {counters['err']} errors  |  {len(manifest)} total in cache")


def main():
    ap = argparse.ArgumentParser(
        description="Durable BFS crawler. Kill and restart safely at any time."
    )
    ap.add_argument("--workers", type=int, default=50,
                    help="Parallel connections (default 50)")
    ap.add_argument("--timeout", type=int, default=20,
                    help="Per-request timeout seconds (default 20)")
    ap.add_argument("--force", action="store_true",
                    help="Re-fetch everything, ignoring manifest")
    asyncio.run(run(ap.parse_args()))


if __name__ == "__main__":
    main()

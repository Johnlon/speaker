#!/usr/bin/env python3
"""
crawl_cache.py — BFS web crawler that builds research/cache/.

Seed URLs come from research/source_urls.md.
After fetching each HTML page, discovered URLs (PDFs, datasheets, etc.) are
added to the queue and appended to source_urls.md so they persist for next run.
Already-cached URLs are skipped — re-run any time to catch new content.

research/cache/manifest.json  maps  url -> {file, content_type, status, size, fetched_at}

URL discovery rules (conservative — we don't want to crawl the whole web):
  - Any URL ending in .pdf found on a product page
  - doc.soundimports.nl/pdf/ links (SI datasheets)
  - Manufacturer PDF links (sbacoustics.com, seas.no, scan-speak.dk, etc.)
  - Does NOT follow: navigation links, category pages, cart, etc.

Usage:
    python scripts/crawl_cache.py [--workers 50] [--timeout 20] [--force]
"""

import argparse
import asyncio
import hashlib
import json
import re
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

# Per-domain minimum gap in seconds (0 = unlimited).
# Only fill in domains that need throttling; everything else runs flat out.
_DOMAIN_DELAY: dict[str, float] = {
    "loudspeakerdatabase.com": 2.0,
    "www.loudspeakerdatabase.com": 2.0,
}

ROOT = Path(__file__).parent.parent
CACHE_DIR = ROOT / "research" / "cache"
MANIFEST_PATH = CACHE_DIR / "manifest.json"
SOURCE_URLS = ROOT / "research" / "source_urls.md"

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; SpeakerResearchBot/1.0)",
           "Accept-Language": "en-GB,en;q=0.9"}

_EXT_MAP = {
    "text/html":             ".html",
    "application/pdf":       ".pdf",
    "application/json":      ".json",
    "application/xhtml+xml": ".html",
    "text/xml":              ".xml",
    "application/xml":       ".xml",
}

# Domains we trust to follow PDF links from
_TRUSTED_PDF_DOMAINS = {
    "doc.soundimports.nl",
    "sbacoustics.com",
    "www.sbacoustics.com",
    "seas.no",
    "www.seas.no",
    "scan-speak.dk",
    "www.scan-speak.dk",
    "daytonaudio.com",
    "www.daytonaudio.com",
    "visaton.de",
    "www.visaton.de",
    "beyma.com",
    "www.beyma.com",
    "morel.co.il",
    "www.morel.co.il",
    "wavecor.com",
    "www.wavecor.com",
}

# Domains whose product pages we seed from (may discover PDFs here)
_PRODUCT_DOMAINS = {
    "www.soundimports.eu",
    "soundimports.eu",
    "willys-hifi.com",
    "www.willys-hifi.com",
    "www.hificollective.co.uk",
    "www.falconacoustics.co.uk",
    "www.lautsprechershop.de",
    "loudspeakerdatabase.com",
    "www.daytonaudio.com",
    "daytonaudio.com",
    "www.parts-express.com",
    "www.tb-speaker.com",
}


def url_cache_name(url: str, content_type: str) -> str:
    h = hashlib.sha256(url.encode()).hexdigest()
    ct_base = content_type.split(";")[0].strip().lower()
    ext = _EXT_MAP.get(ct_base)
    if not ext:
        lower = url.lower().split("?")[0]
        ext = ".pdf" if lower.endswith(".pdf") else ".json" if lower.endswith(".json") else ".html"
    return h + ext


def is_pdf_url(url: str) -> bool:
    return url.lower().split("?")[0].endswith(".pdf")


def should_follow(url: str) -> bool:
    """True if this discovered URL should be added to the crawl queue."""
    try:
        p = urlparse(url)
    except Exception:
        return False
    domain = p.netloc.lower()
    path = p.path.lower()

    # Always follow PDFs from trusted domains
    if domain in _TRUSTED_PDF_DOMAINS and path.endswith(".pdf"):
        return True
    # SI datasheet subdomain — always follow
    if "doc.soundimports" in domain and path.endswith(".pdf"):
        return True
    # Any PDF linked from any page we're scraping
    if path.endswith(".pdf"):
        return True
    # Don't follow HTML links to new domains
    return False


def discover_urls(html: str, base_url: str) -> list[str]:
    """Extract followable URLs from an HTML page."""
    try:
        soup = BeautifulSoup(html, "html.parser")
    except Exception:
        return []
    found = []
    for tag in soup.find_all("a", href=True):
        href = tag["href"].strip()
        if not href or href.startswith(("#", "javascript:", "mailto:")):
            continue
        abs_url = urljoin(base_url, href).split("#")[0].split("?")[0]
        if abs_url.startswith("http") and should_follow(abs_url):
            found.append(abs_url)
    return list(dict.fromkeys(found))


# ---------------------------------------------------------------------------
# Per-domain rate limiter (only for domains in _DOMAIN_DELAY)
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
# Manifest helpers
# ---------------------------------------------------------------------------

def load_manifest() -> dict:
    if MANIFEST_PATH.exists():
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    return {}


def _save_manifest(manifest: dict) -> None:
    MANIFEST_PATH.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )


def read_seed_urls(manifest: dict, force: bool) -> list[str]:
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


def append_to_source_urls(new_urls: list[str]) -> None:
    """Append newly discovered URLs to source_urls.md."""
    if not new_urls:
        return
    existing = set()
    if SOURCE_URLS.exists():
        for line in SOURCE_URLS.read_text(encoding="utf-8").splitlines():
            existing.add(line.strip())
    to_add = [u for u in new_urls if u not in existing]
    if not to_add:
        return
    with SOURCE_URLS.open("a", encoding="utf-8") as f:
        f.write(f"\n# discovered by crawl_cache.py\n")
        for u in to_add:
            f.write(u + "\n")
    print(f"  [+] Discovered {len(to_add)} new URLs -> source_urls.md")


# ---------------------------------------------------------------------------
# Async fetch + worker
# ---------------------------------------------------------------------------

async def fetch_one(url: str, session: aiohttp.ClientSession, timeout: int,
                    throttle: DomainThrottle):
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


async def worker(queue: asyncio.Queue, session: aiohttp.ClientSession,
                 timeout: int, throttle: DomainThrottle,
                 manifest: dict, manifest_lock: asyncio.Lock,
                 seen: set, seen_lock: asyncio.Lock,
                 discovered_lock: asyncio.Lock, discovered: list,
                 counters: dict) -> None:
    while True:
        url = await queue.get()
        if url is None:
            queue.task_done()
            break

        status, ct, body, info = await fetch_one(url, session, timeout, throttle)
        counters["total"] += 1

        if status == 200 and body:
            fname = url_cache_name(url, ct)
            fpath = CACHE_DIR / fname
            fpath.write_bytes(body)
            entry = {
                "file": fname,
                "content_type": ct,
                "status": 200,
                "size_bytes": len(body),
                "fetched_at": datetime.now(timezone.utc).isoformat(),
                "final_url": info,
            }
            async with manifest_lock:
                manifest[url] = entry
                _save_manifest(manifest)
            counters["ok"] += 1
            kb = len(body) // 1024
            print(f"[OK  {kb:4d}kB] {url}")

            # Discover new URLs from HTML pages
            if "html" in ct.lower() and not is_pdf_url(url):
                new_urls = discover_urls(body.decode("utf-8", errors="replace"), url)
                async with seen_lock:
                    fresh = [u for u in new_urls if u not in seen]
                    for u in fresh:
                        seen.add(u)
                if fresh:
                    async with discovered_lock:
                        discovered.extend(fresh)
                    for u in fresh:
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
    manifest = load_manifest()
    seeds = read_seed_urls(manifest, args.force)

    if not seeds:
        print("Nothing to fetch — all seed URLs already cached.")
        print("Use --force to re-fetch, or run extract_urls.py to find new URLs.")
        return

    print(f"Seeds: {len(seeds)} uncached URLs. Workers: {args.workers}")

    seen: set = set(manifest.keys())
    seen.update(seeds)
    manifest_lock = asyncio.Lock()
    seen_lock = asyncio.Lock()
    discovered_lock = asyncio.Lock()
    discovered: list = []
    counters = {"total": 0, "ok": 0, "err": 0}
    throttle = DomainThrottle()

    queue: asyncio.Queue = asyncio.Queue()
    for url in seeds:
        await queue.put(url)

    connector = aiohttp.TCPConnector(limit=args.workers, ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
        workers = [
            asyncio.create_task(worker(
                queue, session, args.timeout, throttle, manifest,
                manifest_lock, seen, seen_lock,
                discovered_lock, discovered, counters
            ))
            for _ in range(args.workers)
        ]
        await queue.join()
        for _ in workers:
            await queue.put(None)
        await asyncio.gather(*workers)

    print(f"\n{counters['ok']} fetched, {counters['err']} errors")
    print(f"Cache: {len(manifest)} total entries -> {MANIFEST_PATH}")

    # Persist newly discovered URLs
    append_to_source_urls(discovered)


def main():
    ap = argparse.ArgumentParser(description="BFS crawler — fetches seed URLs and follows PDF links")
    ap.add_argument("--workers", type=int, default=50,
                    help="Parallel connections (default 50)")
    ap.add_argument("--timeout", type=int, default=20,
                    help="Per-request timeout in seconds (default 20)")
    ap.add_argument("--force", action="store_true",
                    help="Re-fetch even if already cached")
    args = ap.parse_args()
    asyncio.run(run(args))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
crawl_cache.py — Durable BFS web crawler. Builds research/cache/.

DURABILITY
----------
Kill and restart at any time — no data is lost:
  - Files written as <sha256>.partial, atomically renamed on completion.
    Startup deletes any .partial left by a killed run.
  - manifest.json written via manifest.json.tmp -> rename (never half-written).
  - Discovered URLs appended to source_urls.md immediately per URL.
    Restart rebuilds queue from source_urls.md minus manifest.
  - HTTP 200  -> recorded in manifest (file + metadata). Skipped on restart.
  - HTTP 404  -> recorded in manifest (status only, no file). Skipped on restart.
  - HTTP 429 / timeout / other error -> NOT recorded. Retried on restart.

SI SEARCH FALLBACK
------------------
When a constructed SoundImports product URL 404s, the script automatically
searches SI for the correct URL and adds any matching product pages to the
queue. This handles slug mismatches (e.g. morel-mdt22t -> morel-mdt-22).

THROTTLING
----------
Per-domain semaphore limits concurrency for sites that rate-limit.
_DOMAIN_SEM maps domain -> max concurrent connections.

USAGE
-----
  python scripts/crawl_cache.py
  python scripts/crawl_cache.py --workers 200 --timeout 20
  python scripts/crawl_cache.py --force   # re-fetch everything including 404s
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
from urllib.parse import quote_plus, urljoin, urlparse

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

# Max concurrent connections per domain. Everything else runs flat out.
_DOMAIN_SEM: dict[str, int] = {
    "loudspeakerdatabase.com":     1,
    "www.loudspeakerdatabase.com": 1,
}

_SI_HOST = "www.soundimports.eu"
_SI_PRODUCT_RE = re.compile(r"^/en/[a-z0-9][a-z0-9\-]+\.html$")

_WILLYS_HOST = "willys-hifi.com"
_WILLYS_PRODUCT_RE = re.compile(r"^/products/[a-z0-9][a-z0-9\-]+$")

# ---------------------------------------------------------------------------
# URL helpers
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


def _slug_to_query(slug: str) -> str:
    """Convert a URL slug to a natural-language search query.
    'sb-acoustics-sb12pacr25-4-mid-woofer' -> 'sb acoustics sb12pacr25 4 mid woofer'
    Adds spaces at letter-digit transitions, replaces hyphens with spaces.
    """
    q = re.sub(r"([a-z])(\d)", r"\1 \2", slug)
    q = re.sub(r"(\d)([a-z])", r"\1 \2", q)
    return q.replace("-", " ").strip()


# --- SoundImports (Magento) ---

def _is_si_product_url(url: str) -> bool:
    p = urlparse(url)
    return p.netloc == _SI_HOST and bool(_SI_PRODUCT_RE.match(p.path))


def _si_search_url(failed_url: str) -> str:
    slug = urlparse(failed_url).path.rstrip("/").rsplit("/", 1)[-1].replace(".html", "")
    q = _slug_to_query(slug)
    return f"https://{_SI_HOST}/en/catalogsearch/result/?q={quote_plus(q)}"


def _extract_si_product_urls(html: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    found = []
    for a in soup.find_all("a", href=True):
        href = a["href"].split("#")[0].split("?")[0].rstrip(".,;)>")
        p = urlparse(href)
        if not p.netloc:
            href = f"https://{_SI_HOST}{href}"
            p = urlparse(href)
        if p.netloc == _SI_HOST and _SI_PRODUCT_RE.match(p.path):
            found.append(href)
    return list(dict.fromkeys(found))


# --- Willys-Hifi (Shopify, /a/search HTML endpoint) ---

def _is_willys_product_url(url: str) -> bool:
    p = urlparse(url)
    return p.netloc == _WILLYS_HOST and bool(_WILLYS_PRODUCT_RE.match(p.path))


def _willys_search_url(failed_url: str) -> str:
    """Build a Willys search URL from a failed product slug.
    Uses the full slug as the query — the search engine handles partial matches.
    e.g. sb-acoustics-sb12pacr25-4-mid-woofer -> /a/search?q=sb-acoustics-sb12pacr25-4-mid-woofer
    """
    slug = urlparse(failed_url).path.rstrip("/").rsplit("/", 1)[-1]
    return f"https://{_WILLYS_HOST}/a/search?q={quote_plus(slug)}"


def _extract_willys_product_urls(html: str) -> list[str]:
    """Parse Willys /a/search HTML results page for /products/ links."""
    soup = BeautifulSoup(html, "html.parser")
    found = []
    for a in soup.find_all("a", href=True):
        href = a["href"].split("?")[0].split("#")[0].rstrip(".,;)>")
        p = urlparse(href)
        if not p.netloc:
            href = f"https://{_WILLYS_HOST}{href}"
            p = urlparse(href)
        if p.netloc == _WILLYS_HOST and _WILLYS_PRODUCT_RE.match(p.path):
            found.append(href)
    return list(dict.fromkeys(found))


def _discover_from_html(html: str, base_url: str) -> list[str]:
    """Return PDF links found in an HTML page."""
    soup = BeautifulSoup(html, "html.parser")
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
        print(f"Cleaned {len(partials)} .partial file(s) from previous killed run.")


def load_manifest() -> dict:
    if MANIFEST_PATH.exists():
        try:
            return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print("Warning: manifest.json corrupt — starting fresh.")
            return {}
    return {}


# ---------------------------------------------------------------------------
# source_urls.md helpers
# ---------------------------------------------------------------------------

def read_pending_urls(manifest: dict, force: bool) -> list[str]:
    """Return URLs not yet in manifest (or all if --force)."""
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


async def _append_url(url: str, file_lock: asyncio.Lock) -> None:
    """Append a discovered URL to source_urls.md if not already present."""
    async with file_lock:
        existing = set()
        if SOURCE_URLS.exists():
            for line in SOURCE_URLS.read_text(encoding="utf-8").splitlines():
                existing.add(line.strip())
        if url not in existing:
            with SOURCE_URLS.open("a", encoding="utf-8") as f:
                f.write(url + "\n")


# ---------------------------------------------------------------------------
# Progress reporter
# ---------------------------------------------------------------------------

class Progress:
    def __init__(self, total: int):
        self.total = total
        self.ok = 0
        self.err_404 = 0
        self.err_other = 0
        self.discovered = 0
        self._start = time.monotonic()
        self._last_print = 0.0
        self._lock = asyncio.Lock()

    async def record(self, status: int, url: str = "", new_urls: int = 0) -> None:
        async with self._lock:
            if status == 200:
                self.ok += 1
            elif status == 404:
                self.err_404 += 1
            elif status != 0 or "429" not in url:
                self.err_other += 1
            self.discovered += new_urls
            await self._print_if_due()

    async def _print_if_due(self) -> None:
        now = time.monotonic()
        done = self.ok + self.err_404 + self.err_other
        if done % 5 == 0 or now - self._last_print >= 20:
            self._last_print = now
            elapsed = now - self._start
            rate = done / elapsed if elapsed > 1 else 0
            remaining = self.total - done
            eta = f"{remaining/rate:.0f}s" if rate > 0 else "?"
            print(
                f"  [{elapsed:5.0f}s] {done}/{self.total} done"
                f" | ok={self.ok} 404={self.err_404} other={self.err_other}"
                f" | +{self.discovered} discovered"
                f" | {rate:.1f}/s eta={eta}"
            )


# ---------------------------------------------------------------------------
# Per-domain semaphore pool
# ---------------------------------------------------------------------------

class DomainSemaphores:
    def __init__(self):
        self._sems: dict[str, asyncio.Semaphore] = {}

    def get(self, url: str):
        domain = urlparse(url).netloc.lower()
        limit = _DOMAIN_SEM.get(domain)
        if limit is None:
            return asyncio.nullcontext()
        if domain not in self._sems:
            self._sems[domain] = asyncio.Semaphore(limit)
        return self._sems[domain]


# ---------------------------------------------------------------------------
# Async fetch
# ---------------------------------------------------------------------------

async def _fetch(url: str, session: aiohttp.ClientSession, timeout: int,
                 sems: DomainSemaphores):
    async with sems.get(url):
        try:
            async with session.get(
                url,
                timeout=aiohttp.ClientTimeout(total=timeout),
                headers=HEADERS,
                allow_redirects=True,
            ) as r:
                ct = r.headers.get("Content-Type", "text/html")
                body = await r.read()
                return r.status, ct, body, str(r.url)
        except asyncio.TimeoutError:
            return 0, None, None, "timeout"
        except aiohttp.ClientError as e:
            return 0, None, None, str(e)
        except Exception as e:
            return 0, None, None, str(e)


# ---------------------------------------------------------------------------
# Worker
# ---------------------------------------------------------------------------

async def worker(
    queue: asyncio.Queue,
    session: aiohttp.ClientSession,
    timeout: int,
    sems: DomainSemaphores,
    manifest: dict,
    manifest_lock: asyncio.Lock,
    seen: set,
    seen_lock: asyncio.Lock,
    file_lock: asyncio.Lock,
    progress: Progress,
) -> None:
    while True:
        url = await queue.get()
        if url is None:
            queue.task_done()
            break

        status, ct, body, info = await _fetch(url, session, timeout, sems)
        new_discovered = 0

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
            print(f"[OK  {len(body)//1024:4d}kB] {url}")

            # Follow PDF links from HTML pages
            if "html" in ct.lower() and not _is_pdf(url):
                discovered = _discover_from_html(body.decode("utf-8", errors="replace"), url)
                async with seen_lock:
                    fresh = [u for u in discovered if u not in seen]
                    for u in fresh:
                        seen.add(u)
                for u in fresh:
                    await _append_url(u, file_lock)
                    await queue.put(u)
                new_discovered = len(fresh)

        elif status == 404:
            # Record permanently so we don't retry on next run
            async with manifest_lock:
                manifest[url] = {
                    "status": 404,
                    "fetched_at": datetime.now(timezone.utc).isoformat(),
                }
                _atomic_write_manifest(manifest)
            print(f"[404]  {url}")

            # On 404, try site-specific search to find the canonical URL
            if _is_si_product_url(url):
                search_url = _si_search_url(url)
                print(f"       SI search: {search_url}")
                s2, ct2, body2, _ = await _fetch(search_url, session, timeout, sems)
                if s2 == 200 and body2:
                    candidates = _extract_si_product_urls(body2.decode("utf-8", errors="replace"))
                    async with seen_lock:
                        fresh = [u for u in candidates if u not in seen]
                        for u in fresh:
                            seen.add(u)
                    if fresh:
                        print(f"       -> {len(fresh)} candidate(s): {', '.join(u.split('/')[-1] for u in fresh[:3])}")
                        for u in fresh:
                            await _append_url(u, file_lock)
                            await queue.put(u)
                        new_discovered += len(fresh)
                    else:
                        print(f"       -> no results")

            elif _is_willys_product_url(url):
                search_url = _willys_search_url(url)
                 print(f"       Willys search: {search_url}")
                s2, ct2, body2, _ = await _fetch(search_url, session, timeout, sems)
                if s2 == 200 and body2:
                    candidates = _extract_willys_product_urls(body2.decode("utf-8", errors="replace"))  # HTML
                    async with seen_lock:
                        fresh = [u for u in candidates if u not in seen]
                        for u in fresh:
                            seen.add(u)
                    if fresh:
                        print(f"       -> {len(fresh)} candidate(s): {', '.join(u.split('/')[-1] for u in fresh[:3])}")
                        for u in fresh:
                            await _append_url(u, file_lock)
                            await queue.put(u)
                        new_discovered += len(fresh)
                    else:
                        print(f"       -> no results")

        else:
            # 429 / timeout / other transient error — NOT recorded, retried next run
            err = info if status == 0 else f"HTTP {status}"
            print(f"[ERR]  {url}  -> {err}")

        await progress.record(status, url, new_discovered)
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
        print("All URLs already cached or marked 404. Use --force to retry everything.")
        return

    throttled = " ".join(f"{d.split('.')[0]}={lim}conn" for d, lim in _DOMAIN_SEM.items())
    already_done = sum(1 for v in manifest.values() if v.get("status") == 200)
    already_404 = sum(1 for v in manifest.values() if v.get("status") == 404)
    print(f"Pending: {len(pending)}  |  Already ok: {already_done}  |  Already 404: {already_404}  |  Workers: {args.workers}")
    print(f"Throttled: {throttled}")

    seen: set = set(manifest.keys()) | set(pending)
    manifest_lock = asyncio.Lock()
    seen_lock = asyncio.Lock()
    file_lock = asyncio.Lock()
    sems = DomainSemaphores()
    progress = Progress(len(pending))

    queue: asyncio.Queue = asyncio.Queue()
    for url in pending:
        await queue.put(url)

    connector = aiohttp.TCPConnector(limit=args.workers, ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
        workers = [
            asyncio.create_task(worker(
                queue, session, args.timeout, sems,
                manifest, manifest_lock,
                seen, seen_lock,
                file_lock, progress,
            ))
            for _ in range(args.workers)
        ]
        await queue.join()
        for _ in workers:
            await queue.put(None)
        await asyncio.gather(*workers)

    elapsed = time.monotonic() - progress._start
    print(
        f"\nFinished in {elapsed:.0f}s"
        f"  |  ok={progress.ok}  404={progress.err_404}  other={progress.err_other}"
        f"  |  +{progress.discovered} new URLs discovered"
        f"  |  {sum(1 for v in manifest.values() if v.get('status') == 200)} total cached"
    )


def main():
    ap = argparse.ArgumentParser(
        description="Durable BFS crawler. Kill/restart safely. 404s recorded, 429s retried."
    )
    ap.add_argument("--workers", type=int, default=200)
    ap.add_argument("--timeout", type=int, default=20)
    ap.add_argument("--force", action="store_true",
                    help="Re-fetch everything including recorded 404s")
    asyncio.run(run(ap.parse_args()))


if __name__ == "__main__":
    main()

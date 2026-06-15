#!/usr/bin/env python3
"""
refetch_drivers.py — Re-scrape every product page URL from project files and
extract structured driver specs into drivers_refetched.json.

Does NOT modify any existing file. Compare output with drivers.json.

Usage:
    python scripts/refetch_drivers.py [options]

Options:
    --source si|willys|hfc|lss|ldb|dayton|all   Limit to one source (default: all)
    --model  ND91-4                              Fetch one model only (substring match)
    --workers 10                                 Parallel fetch workers (default: 10)
    --delay  1.5                                 Per-domain rate limit in seconds (default: 1.5)
    --output drivers_refetched.json              Output file (default: drivers_refetched.json)
    --timeout 15                                 Per-request timeout in seconds (default: 15)
"""

import argparse
import asyncio
import json
import re
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

try:
    import aiohttp
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit("Install dependencies: pip install aiohttp beautifulsoup4")

ROOT = Path(__file__).parent.parent
DRIVERS_JSON = ROOT / "drivers.json"
DRIVERS_MD = ROOT / "drivers.md"
RESEARCH = ROOT / "research"

UA = "Mozilla/5.0 (compatible; SpeakerResearchBot/1.0)"
HEADERS = {"User-Agent": UA, "Accept-Language": "en-GB,en;q=0.9"}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def log(msg: str) -> None:
    print(msg, flush=True)


def classify_url(url: str) -> str:
    h = urlparse(url).netloc.lower()
    if "soundimports" in h and "doc." not in h:
        return "soundimports"
    if "willys" in h:
        return "willys"
    if "hificollective" in h:
        return "hfc"
    if "lautsprechershop" in h:
        return "lss"
    if "loudspeakerdatabase" in h:
        return "loudspeakerdatabase"
    if "daytonaudio" in h:
        return "dayton"
    if "falconacoustics" in h:
        return "falcon"
    if "parts-express" in h:
        return "parts_express"
    if "doc.soundimports" in h or url.lower().endswith(".pdf"):
        return "datasheet"
    return "other"


def classify_url_from_filename(name: str) -> str:
    if name.startswith("si_"):
        return "soundimports"
    if name.startswith("willys_"):
        return "willys"
    if name.startswith("hfc_"):
        return "hfc"
    if name.startswith("lautsprechershop_"):
        return "lss"
    return "other"


def is_pdf_url(url: str) -> bool:
    return url.lower().endswith(".pdf") or "doc.soundimports" in url


def parse_float(s: str) -> float | None:
    if not s:
        return None
    s = re.sub(r"\*+", "", s)
    m = re.search(r"[-+]?\d+\.?\d*", s.replace(",", ""))
    if m:
        try:
            return float(m.group())
        except ValueError:
            return None
    return None


def parse_freq_range(s: str) -> tuple[float | None, float | None]:
    nums = re.findall(r"[\d,]+", s)
    nums = [float(n.replace(",", "")) for n in nums]
    if len(nums) >= 2:
        return nums[0], nums[1]
    return None, None


def _ts() -> str:
    return datetime.now(timezone.utc).isoformat()


# ---------------------------------------------------------------------------
# Per-domain rate limiter
# ---------------------------------------------------------------------------

class DomainRateLimiter:
    """Ensures at least `delay` seconds between requests to the same domain."""

    def __init__(self, delay: float):
        self.delay = delay
        self._locks: dict[str, asyncio.Lock] = defaultdict(asyncio.Lock)
        self._last: dict[str, float] = defaultdict(float)

    async def acquire(self, url: str) -> None:
        domain = urlparse(url).netloc.lower()
        lock = self._locks[domain]
        async with lock:
            elapsed = time.monotonic() - self._last[domain]
            if elapsed < self.delay:
                await asyncio.sleep(self.delay - elapsed)
            self._last[domain] = time.monotonic()


# ---------------------------------------------------------------------------
# URL collectors
# ---------------------------------------------------------------------------

def urls_from_drivers_json() -> dict[str, dict]:
    drivers = {}
    if not DRIVERS_JSON.exists():
        return drivers
    data = json.loads(DRIVERS_JSON.read_text(encoding="utf-8"))
    for d in data.get("drivers", []):
        mid = d.get("id", "")
        entry = {
            "model": d.get("model", ""),
            "brand": d.get("brand", ""),
            "role": d.get("role", ""),
            "urls": {},
            "datasheets": [],
        }
        for p in d.get("prices", []):
            u = p.get("url")
            if u:
                src = classify_url(u)
                entry["urls"].setdefault(src, [])
                if u not in entry["urls"][src]:
                    entry["urls"][src].append(u)
        for ds in d.get("datasheets", []):
            u = ds.get("url")
            if u and u not in entry["datasheets"]:
                entry["datasheets"].append(u)
        drivers[mid] = entry
    return drivers


_MD_LINK = re.compile(r"\[([^\]]*)\]\((https?://[^\)]+)\)")
_RAW_URL = re.compile(r"https?://\S+")


def urls_from_markdown(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    urls = [m.group(2) for m in _MD_LINK.finditer(text)]
    for line in text.splitlines():
        if "**Source:**" in line or "Source:" in line:
            urls += _RAW_URL.findall(line)
    return list(dict.fromkeys(urls))


def urls_from_index_files() -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for f in RESEARCH.glob("*_index.md"):
        src = classify_url_from_filename(f.name)
        for u in urls_from_markdown(f):
            result.setdefault(src, [])
            if u not in result[src]:
                result[src].append(u)
    return result


def build_driver_index() -> dict[str, dict]:
    drivers = urls_from_drivers_json()
    index_urls = urls_from_index_files()

    for src, urls in index_urls.items():
        for url in urls:
            if is_pdf_url(url):
                continue
            matched = False
            for did, dentry in drivers.items():
                model_slug = dentry["model"].lower().replace(" ", "-").replace("/", "-")
                brand_slug = dentry["brand"].lower().replace(" ", "-")
                url_lower = url.lower()
                if model_slug in url_lower or (brand_slug in url_lower and model_slug[:4] in url_lower):
                    dentry["urls"].setdefault(src, [])
                    if url not in dentry["urls"][src]:
                        dentry["urls"][src].append(url)
                    matched = True
                    break
            if not matched:
                drivers.setdefault("__unmatched__", {
                    "model": "", "brand": "", "role": "", "urls": {}, "datasheets": []
                })
                drivers["__unmatched__"]["urls"].setdefault(src, [])
                if url not in drivers["__unmatched__"]["urls"][src]:
                    drivers["__unmatched__"]["urls"][src].append(url)

    return drivers


# ---------------------------------------------------------------------------
# Extractors (sync — called after HTML is fetched)
# ---------------------------------------------------------------------------

_SI_FIELD_MAP = {
    "impedance_ohm":     ["impedance (z)", "impedance"],
    "sensitivity_db":    ["sensitivity (spl at 1m / 2.83v)", "sensitivity", "spl"],
    "power_rms_w":       ["power handling (rms)", "rms power handling"],
    "power_max_w":       ["power handling (max)", "power handling (peak)"],
    "freq_low_hz":       ["frequency response"],
    "re_ohm":            ["dc resistance (re)", "re"],
    "le_mh":             ["voice coil inductance (le)", "le"],
    "fs_hz":             ["resonant frequency (fs)", "fs"],
    "qms":               ["mechanical q (qms)", "qms"],
    "qes":               ["electromagnetic q (qes)", "qes"],
    "qts":               ["total q (qts)", "qts"],
    "mms_g":             ["diaphragm mass inc. airload (mms)", "mms"],
    "cms_mm_n":          ["mechanical compliance of suspension (cms)", "cms"],
    "sd_cm2":            ["surface area of cone (sd)", "sd"],
    "vd_cm3":            ["volume of displacement (vd)", "vd"],
    "bl_tm":             ["bl product (bl)", "bl"],
    "vas_l":             ["compliance equivalent volume (vas)", "vas"],
    "xmax_mm":           ["maximum linear excursion (xmax)", "xmax"],
    "vc_mm":             ["voice coil diameter", "vc diameter"],
    "frame_od_mm":       ["overall outside diameter", "outside diameter"],
    "depth_mm":          ["overall depth"],
    "cutout_mm":         ["baffle cutout diameter"],
    "mounting_holes":    ["# mounting holes", "number of mounting holes"],
    "cone_material":     ["cone / diaphragm material", "cone material", "diaphragm material"],
    "surround_material": ["surround material"],
    "vc_wire":           ["voice coil wire material"],
    "vc_former":         ["voice coil former"],
    "frame_material":    ["basket / frame material", "basket material"],
    "magnet_material":   ["magnet material"],
    "driver_type":       ["woofer type", "tweeter type"],
    "series":            ["woofer series", "tweeter series"],
}

_SI_LABEL_TO_FIELD: dict[str, str] = {}
for _field, _labels in _SI_FIELD_MAP.items():
    for _lbl in _labels:
        _SI_LABEL_TO_FIELD[_lbl] = _field

_TEXT_FIELDS = {"cone_material", "surround_material", "vc_wire", "vc_former",
                "frame_material", "driver_type", "series"}


def _normalise_magnet(val: str) -> str:
    v = val.lower()
    if "neo" in v or "neodymium" in v:
        return "neodymium"
    if "ferrite" in v or "ceramic" in v:
        return "ferrite"
    if "alnico" in v:
        return "alnico"
    return val.strip()


def _parse_row(label: str, value: str, specs: dict) -> None:
    label = label.lower().strip().rstrip(":")
    field = _SI_LABEL_TO_FIELD.get(label)
    if not field:
        for k, f in _SI_LABEL_TO_FIELD.items():
            if k in label:
                field = f
                break
    if not field or not value:
        return
    if field == "freq_low_hz":
        lo, hi = parse_freq_range(value)
        if lo:
            specs["freq_low_hz"] = lo
        if hi:
            specs["freq_high_hz"] = hi
    elif field == "magnet_material":
        specs["magnet"] = _normalise_magnet(value)
    elif field in _TEXT_FIELDS:
        specs[field] = value.strip()
    elif field == "mounting_holes":
        v = parse_float(value)
        if v is not None:
            specs[field] = int(v)
    else:
        v = parse_float(value)
        if v is not None:
            specs[field] = v


def _table_specs(soup, selectors: list[str]) -> dict:
    specs: dict = {}
    for sel in selectors:
        for row in soup.select(sel):
            cells = row.find_all(["td", "th"])
            if len(cells) >= 2:
                _parse_row(cells[0].get_text(strip=True),
                           cells[-1].get_text(strip=True), specs)
    return specs


def _price(soup, selectors: list[str]) -> float | None:
    for sel in selectors:
        el = soup.select_one(sel)
        if el:
            p = parse_float(el.get_text())
            if p:
                return p
    return None


def extract_soundimports(html: str, url: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    specs = _table_specs(soup, ["table tr", ".product-specifications tr", ".specs tr"])

    # Also try definition lists
    for dt in soup.find_all("dt"):
        dd = dt.find_next_sibling("dd")
        if dd:
            _parse_row(dt.get_text(strip=True), dd.get_text(strip=True), specs)

    price = _price(soup, [".product-price", ".price", "[data-product-price]", ".product__price"])
    stock_el = soup.select_one(".stock-status, .availability, .product-stock")
    stock = stock_el.get_text(strip=True) if stock_el else None
    name_el = soup.select_one("h1")
    name = name_el.get_text(strip=True) if name_el else None

    datasheet_url = None
    for a in soup.find_all("a", href=True):
        if "doc.soundimports" in a["href"] and a["href"].endswith(".pdf"):
            datasheet_url = a["href"]
            break

    return {"product_name": name, "price_eur": price, "stock": stock,
            "specs": specs, "datasheet_url": datasheet_url}


def extract_loudspeakerdatabase(html: str, url: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    specs = _table_specs(soup, ["table tr"])
    for dt in soup.find_all("dt"):
        dd = dt.find_next_sibling("dd")
        if dd:
            _parse_row(dt.get_text(strip=True), dd.get_text(strip=True), specs)
    return {"specs": specs}


def extract_willys(html: str, url: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    specs: dict = {}
    desc = soup.select_one(".product__description, .product-description, #product-description")
    if desc:
        specs = _table_specs(desc, ["tr"])
    price = _price(soup, [".price", ".product__price", "[data-product-price]"])
    stock_el = soup.select_one(".product__inventory, [class*=stock]")
    return {"price_gbp": price, "stock": stock_el.get_text(strip=True) if stock_el else None,
            "specs": specs}


def extract_hfc(html: str, url: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    specs = _table_specs(soup, ["table tr", ".specifications tr"])
    price = _price(soup, [".price", ".product-price", "#product-price"])
    stock_el = soup.select_one(".stock, .availability")
    return {"price_gbp": price, "stock": stock_el.get_text(strip=True) if stock_el else None,
            "specs": specs}


def extract_falcon(html: str, url: str) -> dict:
    return extract_hfc(html, url)


def extract_lss(html: str, url: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    specs = _table_specs(soup, ["table tr"])
    price_el = soup.select_one(".price, .product-price, #price")
    price_inc = parse_float(price_el.get_text()) if price_el else None
    price_exc = round(price_inc / 1.19, 2) if price_inc else None
    stock_el = soup.select_one(".stock, .availability, .lieferzeit")
    return {"price_eur_inc_vat": price_inc, "price_eur_exc_vat": price_exc,
            "stock": stock_el.get_text(strip=True) if stock_el else None, "specs": specs}


def extract_dayton(html: str, url: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    specs = _table_specs(soup, ["table tr", ".specs tr", ".product-specs tr"])
    price = _price(soup, [".price", ".product-price"])
    return {"price_usd": price, "specs": specs}


EXTRACTORS = {
    "soundimports":      extract_soundimports,
    "loudspeakerdatabase": extract_loudspeakerdatabase,
    "willys":            extract_willys,
    "hfc":               extract_hfc,
    "falcon":            extract_falcon,
    "lss":               extract_lss,
    "dayton":            extract_dayton,
}

_MERGE_PRIORITY = ["soundimports", "loudspeakerdatabase", "dayton", "hfc", "falcon", "willys", "lss", "other"]


def merge_specs(sources_fetched: dict) -> dict:
    merged: dict = {}
    for src in _MERGE_PRIORITY:
        for k, v in sources_fetched.get(src, {}).get("specs", {}).items():
            if k not in merged and v is not None:
                merged[k] = v
    for src, sf in sources_fetched.items():
        for pk in ("price_eur", "price_gbp", "price_usd", "price_eur_inc_vat", "price_eur_exc_vat"):
            if sf.get(pk):
                merged.setdefault(f"{src}_{pk}", sf[pk])
    return merged


# ---------------------------------------------------------------------------
# Async fetch
# ---------------------------------------------------------------------------

async def fetch_one(url: str, session: aiohttp.ClientSession,
                    rate_limiter: DomainRateLimiter, timeout: int) -> tuple[int, str | None, str | None]:
    await rate_limiter.acquire(url)
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=timeout),
                               headers=HEADERS, allow_redirects=True) as r:
            if r.status == 200:
                html = await r.text(errors="replace")
                return r.status, html, None
            return r.status, None, f"HTTP {r.status}"
    except asyncio.TimeoutError:
        return 0, None, "timeout"
    except aiohttp.ClientError as e:
        return 0, None, str(e)
    except Exception as e:
        return 0, None, str(e)


# Work item: (driver_id, source_key, url)
async def worker(queue: asyncio.Queue, session: aiohttp.ClientSession,
                 rate_limiter: DomainRateLimiter, timeout: int,
                 results: dict, counters: dict) -> None:
    while True:
        item = await queue.get()
        if item is None:
            queue.task_done()
            break
        did, src, url = item
        extractor = EXTRACTORS.get(src)
        if not extractor:
            queue.task_done()
            continue

        status, html, err = await fetch_one(url, session, rate_limiter, timeout)
        counters["fetches"] += 1

        if err or not html:
            log(f"[ERR {status:3d}] {url}  → {err}")
            results.setdefault(did, {}).setdefault(src, {
                "url": url, "fetch_status": status, "fetch_timestamp": _ts(),
                "error": err or "no content"
            })
        else:
            result = extractor(html, url)
            n = len(result.get("specs", {}))
            counters["specs"] += n
            log(f"[OK  {status}] {url}  → {n} specs")
            if did not in results or src not in results.get(did, {}):
                results.setdefault(did, {})[src] = {
                    "url": url, "fetch_status": status,
                    "fetch_timestamp": _ts(), **result
                }

        queue.task_done()


# ---------------------------------------------------------------------------
# Async main
# ---------------------------------------------------------------------------

async def run(args, driver_index: dict, active_sources: set) -> list[dict]:
    rate_limiter = DomainRateLimiter(args.delay)
    connector = aiohttp.TCPConnector(limit=args.workers, ssl=False)
    results: dict[str, dict] = {}   # did → {src → fetch_result}
    counters = {"fetches": 0, "specs": 0}

    queue: asyncio.Queue = asyncio.Queue()

    # Enqueue work items
    queued = 0
    for did, dentry in driver_index.items():
        if did == "__unmatched__":
            continue
        if args.model and args.model.lower() not in dentry["model"].lower():
            continue
        for src, urls in dentry["urls"].items():
            if src not in active_sources:
                continue
            for url in urls:
                if is_pdf_url(url):
                    continue
                await queue.put((did, src, url))
                queued += 1
                break  # first URL per source per driver

    log(f"Queued {queued} fetches across {args.workers} workers…")

    async with aiohttp.ClientSession(connector=connector) as session:
        workers = [
            asyncio.create_task(worker(queue, session, rate_limiter, args.timeout, results, counters))
            for _ in range(args.workers)
        ]
        await queue.join()
        for _ in workers:
            await queue.put(None)
        await asyncio.gather(*workers)

    log(f"\n{counters['fetches']} fetches completed, {counters['specs']} spec fields extracted")

    output_drivers = []
    for did, dentry in driver_index.items():
        if did == "__unmatched__":
            continue
        if args.model and args.model.lower() not in dentry["model"].lower():
            continue
        sources_fetched = results.get(did, {})
        output_drivers.append({
            "id": did,
            "brand": dentry["brand"],
            "model": dentry["model"],
            "role": dentry["role"],
            "sources_fetched": sources_fetched,
            "merged": merge_specs(sources_fetched),
        })

    return sorted(output_drivers, key=lambda d: (d.get("role", ""), d.get("model", "")))


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Re-fetch driver specs from all product pages")
    parser.add_argument("--source", default="all",
                        choices=["si", "willys", "hfc", "lss", "ldb", "dayton", "all"])
    parser.add_argument("--model", default="", help="Fetch one model (substring match)")
    parser.add_argument("--workers", type=int, default=10, help="Parallel fetch workers")
    parser.add_argument("--delay", type=float, default=1.5, help="Per-domain rate limit (seconds)")
    parser.add_argument("--timeout", type=int, default=15, help="Per-request timeout (seconds)")
    parser.add_argument("--output", default="drivers_refetched.json")
    args = parser.parse_args()

    source_filter_map = {
        "si": "soundimports", "willys": "willys", "hfc": "hfc",
        "lss": "lss", "ldb": "loudspeakerdatabase", "dayton": "dayton",
    }
    active_sources = (set(EXTRACTORS.keys()) if args.source == "all"
                      else {source_filter_map.get(args.source, args.source)})

    log("Building driver URL index…")
    driver_index = build_driver_index()
    log(f"  {sum(1 for k in driver_index if k != '__unmatched__')} drivers indexed")

    output_drivers = asyncio.run(run(args, driver_index, active_sources))

    out = {
        "generated": _ts(),
        "note": "Fresh fetch — compare with drivers.json; do not delete that file",
        "driver_count": len(output_drivers),
        "drivers": output_drivers,
    }
    out_path = ROOT / args.output
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    log(f"Written → {out_path}")


if __name__ == "__main__":
    main()

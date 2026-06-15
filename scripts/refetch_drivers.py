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
    --delay  1.5                                 Seconds between requests (default: 1.5)
    --output drivers_refetched.json              Output file (default: drivers_refetched.json)
    --timeout 15                                 Per-request timeout in seconds (default: 15)
"""

import argparse
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit("Install dependencies: pip install requests beautifulsoup4")

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
    if "soundimports" in h:
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
    if "doc.soundimports" in h or h.endswith(".pdf"):
        return "datasheet"
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
    """Parse '65 - 17,000 Hz' → (65.0, 17000.0)"""
    nums = re.findall(r"[\d,]+", s)
    nums = [float(n.replace(",", "")) for n in nums]
    if len(nums) >= 2:
        return nums[0], nums[1]
    return None, None


# ---------------------------------------------------------------------------
# URL collectors
# ---------------------------------------------------------------------------

def urls_from_drivers_json() -> dict[str, dict]:
    """Return {model_id: {role, brand, model, urls: {source: [url]}}}"""
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
_RAW_URL  = re.compile(r"https?://\S+")


def urls_from_markdown(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    urls = [m.group(2) for m in _MD_LINK.finditer(text)]
    # also catch bare URLs on Source: lines
    for line in text.splitlines():
        if "**Source:**" in line or "Source:" in line:
            urls += _RAW_URL.findall(line)
    return list(dict.fromkeys(urls))  # dedupe, preserve order


def urls_from_index_files() -> dict[str, list[str]]:
    """Return {source_key: [url, ...]} extracted from all index .md files."""
    result: dict[str, list[str]] = {}
    index_files = list(RESEARCH.glob("*_index.md"))
    for f in index_files:
        src = classify_url_from_filename(f.name)
        urls = urls_from_markdown(f)
        result.setdefault(src, [])
        result[src] += [u for u in urls if u not in result[src]]
    return result


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


def role_from_filename(name: str) -> str:
    if "tweeter" in name:
        return "high"
    if "woofer" in name or "mid" in name:
        return "mid"
    return ""


# ---------------------------------------------------------------------------
# Fetch
# ---------------------------------------------------------------------------

def fetch(url: str, session: requests.Session, timeout: int) -> tuple[int, str | None, str | None]:
    """Return (status_code, html_or_none, error_or_none)"""
    try:
        r = session.get(url, timeout=timeout, headers=HEADERS, allow_redirects=True)
        return r.status_code, r.text if r.ok else None, None
    except requests.exceptions.Timeout:
        return 0, None, "timeout"
    except requests.exceptions.ConnectionError as e:
        return 0, None, f"connection error: {e}"
    except Exception as e:
        return 0, None, str(e)


# ---------------------------------------------------------------------------
# Extractors
# ---------------------------------------------------------------------------

# Canonical field names → human-readable label variants (lowercased, stripped)
_SI_FIELD_MAP = {
    "impedance_ohm":    ["impedance (z)", "impedance"],
    "sensitivity_db":   ["sensitivity (spl at 1m / 2.83v)", "sensitivity", "spl"],
    "power_rms_w":      ["power handling (rms)", "rms power handling"],
    "power_max_w":      ["power handling (max)", "power handling (peak)"],
    "freq_low_hz":      ["frequency response"],   # parsed specially
    "re_ohm":           ["dc resistance (re)", "re"],
    "le_mh":            ["voice coil inductance (le)", "le"],
    "fs_hz":            ["resonant frequency (fs)", "fs"],
    "qms":              ["mechanical q (qms)", "qms"],
    "qes":              ["electromagnetic q (qes)", "qes"],
    "qts":              ["total q (qts)", "qts"],
    "mms_g":            ["diaphragm mass inc. airload (mms)", "mms"],
    "cms_mm_n":         ["mechanical compliance of suspension (cms)", "cms"],
    "sd_cm2":           ["surface area of cone (sd)", "sd"],
    "vd_cm3":           ["volume of displacement (vd)", "vd"],
    "bl_tm":            ["bl product (bl)", "bl"],
    "vas_l":            ["compliance equivalent volume (vas)", "vas"],
    "xmax_mm":          ["maximum linear excursion (xmax)", "xmax"],
    "vc_mm":            ["voice coil diameter", "vc diameter"],
    "frame_od_mm":      ["overall outside diameter", "outside diameter"],
    "depth_mm":         ["overall depth"],
    "cutout_mm":        ["baffle cutout diameter"],
    "mounting_holes":   ["# mounting holes", "number of mounting holes"],
    "cone_material":    ["cone / diaphragm material", "cone material", "diaphragm material"],
    "surround_material":["surround material"],
    "vc_wire":          ["voice coil wire material"],
    "vc_former":        ["voice coil former"],
    "frame_material":   ["basket / frame material", "basket material"],
    "magnet_material":  ["magnet material"],
    "driver_type":      ["woofer type", "tweeter type", "woofer series"],
    "series":           ["woofer series", "tweeter series"],
}

# Build reverse map: label_lower → field
_SI_LABEL_TO_FIELD: dict[str, str] = {}
for _field, _labels in _SI_FIELD_MAP.items():
    for _lbl in _labels:
        _SI_LABEL_TO_FIELD[_lbl] = _field


def _normalise_magnet(val: str) -> str:
    v = val.lower()
    if "neo" in v or "neodymium" in v:
        return "neodymium"
    if "ferrite" in v or "ceramic" in v:
        return "ferrite"
    if "alnico" in v:
        return "alnico"
    return val.strip()


def _normalise_material(val: str) -> str:
    return val.strip().lower()


def extract_soundimports(html: str, url: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    specs: dict = {}

    # Spec table — rows of <td>label</td><td>value</td>
    for row in soup.select("table tr, .product-specifications tr, .specs tr"):
        cells = row.find_all("td")
        if len(cells) < 2:
            continue
        label = cells[0].get_text(strip=True).lower().rstrip(":")
        value = cells[1].get_text(strip=True)
        field = _SI_LABEL_TO_FIELD.get(label)
        if not field:
            # try partial match
            for k, f in _SI_LABEL_TO_FIELD.items():
                if k in label:
                    field = f
                    break
        if not field or not value:
            continue

        if field == "freq_low_hz":
            lo, hi = parse_freq_range(value)
            if lo:
                specs["freq_low_hz"] = lo
            if hi:
                specs["freq_high_hz"] = hi
        elif field in ("cone_material", "surround_material", "vc_wire",
                       "vc_former", "frame_material", "driver_type", "series"):
            specs[field] = value.strip()
        elif field == "magnet_material":
            specs["magnet"] = _normalise_magnet(value)
        elif field == "mounting_holes":
            v = parse_float(value)
            if v is not None:
                specs[field] = int(v)
        else:
            v = parse_float(value)
            if v is not None:
                specs[field] = v

    # Price
    price = None
    for sel in [".product-price", ".price", "[data-product-price]", ".product__price"]:
        el = soup.select_one(sel)
        if el:
            price = parse_float(el.get_text())
            if price:
                break

    # Stock
    stock = None
    for sel in [".stock-status", ".availability", ".product-stock"]:
        el = soup.select_one(sel)
        if el:
            stock = el.get_text(strip=True)
            break

    # Product name
    name_el = soup.select_one("h1")
    name = name_el.get_text(strip=True) if name_el else None

    # EAN / article number (often in a small table or definition list)
    ean = None
    for el in soup.find_all(string=re.compile(r"EAN|Article", re.I)):
        parent = el.parent
        nxt = parent.find_next_sibling()
        if nxt:
            ean = nxt.get_text(strip=True)
            break

    # SI datasheet PDF link
    datasheet_url = None
    for a in soup.find_all("a", href=True):
        if "doc.soundimports" in a["href"] and a["href"].endswith(".pdf"):
            datasheet_url = a["href"]
            break

    return {
        "product_name": name,
        "ean": ean,
        "price_eur": price,
        "stock": stock,
        "specs": specs,
        "datasheet_url": datasheet_url,
    }


def extract_loudspeakerdatabase(html: str, url: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    specs: dict = {}

    # LDB uses a clean definition list / table layout
    for row in soup.select("table tr"):
        cells = row.find_all(["td", "th"])
        if len(cells) < 2:
            continue
        label = cells[0].get_text(strip=True).lower()
        value = cells[1].get_text(strip=True)
        field = _SI_LABEL_TO_FIELD.get(label)
        if not field:
            for k, f in _SI_LABEL_TO_FIELD.items():
                if k in label:
                    field = f
                    break
        if not field:
            continue
        if field == "freq_low_hz":
            lo, hi = parse_freq_range(value)
            if lo:
                specs["freq_low_hz"] = lo
            if hi:
                specs["freq_high_hz"] = hi
        elif field == "magnet_material":
            specs["magnet"] = _normalise_magnet(value)
        elif field in ("cone_material", "surround_material", "frame_material", "driver_type"):
            specs[field] = value.strip()
        else:
            v = parse_float(value)
            if v is not None:
                specs[field] = v

    # Also try definition lists
    for dt in soup.find_all("dt"):
        dd = dt.find_next_sibling("dd")
        if not dd:
            continue
        label = dt.get_text(strip=True).lower()
        value = dd.get_text(strip=True)
        field = _SI_LABEL_TO_FIELD.get(label)
        if field and value:
            v = parse_float(value)
            if v is not None:
                specs.setdefault(field, v)

    return {"specs": specs}


def extract_willys(html: str, url: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    specs: dict = {}

    # Price
    price = None
    for sel in [".price", ".product__price", "[data-product-price]"]:
        el = soup.select_one(sel)
        if el:
            price = parse_float(el.get_text())
            if price:
                break

    # Specs from product description tables or lists
    desc = soup.select_one(".product__description, .product-description, #product-description")
    if desc:
        for row in desc.find_all("tr"):
            cells = row.find_all(["td", "th"])
            if len(cells) >= 2:
                label = cells[0].get_text(strip=True).lower()
                value = cells[1].get_text(strip=True)
                field = _SI_LABEL_TO_FIELD.get(label)
                if not field:
                    for k, f in _SI_LABEL_TO_FIELD.items():
                        if k in label:
                            field = f
                            break
                if field:
                    if field == "magnet_material":
                        specs["magnet"] = _normalise_magnet(value)
                    else:
                        v = parse_float(value)
                        if v is not None:
                            specs[field] = v

    stock_el = soup.select_one(".product__inventory, .stock, [class*=stock]")
    stock = stock_el.get_text(strip=True) if stock_el else None

    return {"price_gbp": price, "stock": stock, "specs": specs}


def extract_hfc(html: str, url: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    specs: dict = {}

    price = None
    for sel in [".price", ".product-price", "#product-price"]:
        el = soup.select_one(sel)
        if el:
            price = parse_float(el.get_text())
            if price:
                break

    for row in soup.select("table tr, .specifications tr"):
        cells = row.find_all(["td", "th"])
        if len(cells) >= 2:
            label = cells[0].get_text(strip=True).lower()
            value = cells[1].get_text(strip=True)
            field = _SI_LABEL_TO_FIELD.get(label)
            if not field:
                for k, f in _SI_LABEL_TO_FIELD.items():
                    if k in label:
                        field = f
                        break
            if field:
                if field == "magnet_material":
                    specs["magnet"] = _normalise_magnet(value)
                elif field == "freq_low_hz":
                    lo, hi = parse_freq_range(value)
                    if lo:
                        specs["freq_low_hz"] = lo
                    if hi:
                        specs["freq_high_hz"] = hi
                else:
                    v = parse_float(value)
                    if v is not None:
                        specs[field] = v

    stock_el = soup.select_one(".stock, .availability")
    stock = stock_el.get_text(strip=True) if stock_el else None

    return {"price_gbp": price, "stock": stock, "specs": specs}


def extract_falcon(html: str, url: str) -> dict:
    return extract_hfc(html, url)  # similar layout


def extract_lss(html: str, url: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    specs: dict = {}
    price_inc = None
    price_exc = None

    # LSS has German/English bilingual tables
    for row in soup.select("table tr"):
        cells = row.find_all(["td", "th"])
        if len(cells) < 2:
            continue
        label = cells[0].get_text(strip=True).lower()
        value = cells[-1].get_text(strip=True)
        # try both column orders
        field = _SI_LABEL_TO_FIELD.get(label)
        if not field:
            for k, f in _SI_LABEL_TO_FIELD.items():
                if k in label:
                    field = f
                    break
        if field:
            if field == "magnet_material":
                specs["magnet"] = _normalise_magnet(value)
            elif field == "freq_low_hz":
                lo, hi = parse_freq_range(value)
                if lo:
                    specs["freq_low_hz"] = lo
                if hi:
                    specs["freq_high_hz"] = hi
            else:
                v = parse_float(value)
                if v is not None:
                    specs[field] = v

    # Price — LSS shows inc and exc VAT
    price_el = soup.select_one(".price, .product-price, #price")
    if price_el:
        price_inc = parse_float(price_el.get_text())
        if price_inc:
            price_exc = round(price_inc / 1.19, 2)

    stock_el = soup.select_one(".stock, .availability, .lieferzeit")
    stock = stock_el.get_text(strip=True) if stock_el else None

    return {
        "price_eur_inc_vat": price_inc,
        "price_eur_exc_vat": price_exc,
        "stock": stock,
        "specs": specs,
    }


def extract_dayton(html: str, url: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    specs: dict = {}

    for row in soup.select("table tr, .specs tr, .product-specs tr"):
        cells = row.find_all(["td", "th"])
        if len(cells) < 2:
            continue
        label = cells[0].get_text(strip=True).lower()
        value = cells[1].get_text(strip=True)
        field = _SI_LABEL_TO_FIELD.get(label)
        if not field:
            for k, f in _SI_LABEL_TO_FIELD.items():
                if k in label:
                    field = f
                    break
        if field:
            if field == "magnet_material":
                specs["magnet"] = _normalise_magnet(value)
            elif field == "freq_low_hz":
                lo, hi = parse_freq_range(value)
                if lo:
                    specs["freq_low_hz"] = lo
                if hi:
                    specs["freq_high_hz"] = hi
            else:
                v = parse_float(value)
                if v is not None:
                    specs[field] = v

    price_el = soup.select_one(".price, .product-price")
    price = parse_float(price_el.get_text()) if price_el else None

    return {"price_usd": price, "specs": specs}


EXTRACTORS = {
    "soundimports":    extract_soundimports,
    "loudspeakerdatabase": extract_loudspeakerdatabase,
    "willys":          extract_willys,
    "hfc":             extract_hfc,
    "falcon":          extract_falcon,
    "lss":             extract_lss,
    "dayton":          extract_dayton,
}


# ---------------------------------------------------------------------------
# Merge: prefer SI > LDB > dayton > others
# ---------------------------------------------------------------------------
_MERGE_PRIORITY = ["soundimports", "loudspeakerdatabase", "dayton", "hfc", "falcon", "willys", "lss", "other"]


def merge_specs(sources_fetched: dict) -> dict:
    merged: dict = {}
    for src in _MERGE_PRIORITY:
        sf = sources_fetched.get(src, {})
        s = sf.get("specs", {})
        for k, v in s.items():
            if k not in merged and v is not None:
                merged[k] = v
    # prices
    for src, sf in sources_fetched.items():
        for price_key in ("price_eur", "price_gbp", "price_usd",
                          "price_eur_inc_vat", "price_eur_exc_vat"):
            if price_key in sf and sf[price_key]:
                merged.setdefault(f"{src}_{price_key}", sf[price_key])
    return merged


# ---------------------------------------------------------------------------
# Build driver URL index from all sources
# ---------------------------------------------------------------------------

def build_driver_index() -> dict[str, dict]:
    """Merge URLs from drivers.json + drivers.md + index files into one dict keyed by driver id."""
    drivers = urls_from_drivers_json()

    # URLs from drivers.md Source: lines — grouped by model id heuristic
    md_urls = urls_from_markdown(DRIVERS_MD)
    # We can't reliably match MD URLs to driver ids without parsing, so store globally
    # and let the fetch loop handle them via the per-source extractor

    # URLs from index files
    index_urls = urls_from_index_files()

    # Add index file URLs into a catch-all bucket per source
    for src, urls in index_urls.items():
        for url in urls:
            if is_pdf_url(url):
                continue
            # Try to match to existing driver by scanning URL slug
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
            # unmatched — add to __unmatched__ bucket
            if not matched:
                drivers.setdefault("__unmatched__", {"model": "", "brand": "", "role": "", "urls": {}, "datasheets": []})
                drivers["__unmatched__"]["urls"].setdefault(src, [])
                if url not in drivers["__unmatched__"]["urls"][src]:
                    drivers["__unmatched__"]["urls"][src].append(url)

    return drivers


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Re-fetch driver specs from all product pages")
    parser.add_argument("--source", default="all",
                        choices=["si", "willys", "hfc", "lss", "ldb", "dayton", "all"],
                        help="Limit fetches to one source")
    parser.add_argument("--model", default="", help="Fetch one model (substring match on model name)")
    parser.add_argument("--delay", type=float, default=1.5, help="Delay between requests (seconds)")
    parser.add_argument("--timeout", type=int, default=15, help="Per-request timeout (seconds)")
    parser.add_argument("--output", default="drivers_refetched.json", help="Output JSON file")
    args = parser.parse_args()

    source_filter_map = {
        "si": "soundimports", "willys": "willys", "hfc": "hfc",
        "lss": "lss", "ldb": "loudspeakerdatabase", "dayton": "dayton",
    }
    active_sources = set(EXTRACTORS.keys()) if args.source == "all" \
        else {source_filter_map.get(args.source, args.source)}

    log("Building driver URL index…")
    driver_index = build_driver_index()
    log(f"  {len(driver_index)} driver entries (inc. __unmatched__)")

    session = requests.Session()
    session.headers.update(HEADERS)

    output_drivers = []
    total_fetches = 0
    total_specs = 0

    for did, dentry in driver_index.items():
        if did == "__unmatched__":
            continue
        if args.model and args.model.lower() not in dentry["model"].lower():
            continue

        sources_fetched: dict = {}

        for src, urls in dentry["urls"].items():
            if src not in active_sources:
                continue
            extractor = EXTRACTORS.get(src)
            if not extractor:
                continue
            for url in urls:
                if is_pdf_url(url):
                    continue
                time.sleep(args.delay)
                status, html, err = fetch(url, session, args.timeout)
                total_fetches += 1

                if err or not html:
                    log(f"[ERR {status}] {url} → {err}")
                    sources_fetched[src] = {"url": url, "fetch_status": status,
                                            "fetch_timestamp": _ts(), "error": err or "no content"}
                    continue

                result = extractor(html, url)
                n_specs = len(result.get("specs", {}))
                total_specs += n_specs
                log(f"[OK {status}] {url} → {n_specs} specs")

                sources_fetched[src] = {
                    "url": url,
                    "fetch_status": status,
                    "fetch_timestamp": _ts(),
                    **result,
                }
                break  # use first successful URL per source

        output_drivers.append({
            "id": did,
            "brand": dentry["brand"],
            "model": dentry["model"],
            "role": dentry["role"],
            "sources_fetched": sources_fetched,
            "merged": merge_specs(sources_fetched),
        })

    output = {
        "generated": datetime.now(timezone.utc).isoformat(),
        "note": "Fresh fetch — compare with drivers.json; do not delete that file",
        "fetch_count": total_fetches,
        "spec_fields_extracted": total_specs,
        "driver_count": len(output_drivers),
        "drivers": sorted(output_drivers, key=lambda d: (d.get("role", ""), d.get("model", ""))),
    }

    out_path = ROOT / args.output
    out_path.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    log(f"\nDone. {total_fetches} fetches, {total_specs} spec fields → {out_path}")


def _ts() -> str:
    return datetime.now(timezone.utc).isoformat()


if __name__ == "__main__":
    main()

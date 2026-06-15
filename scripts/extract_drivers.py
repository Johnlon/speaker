#!/usr/bin/env python3
"""
extract_drivers.py — Parse research/cache/ and produce drivers_extracted.json.

Key design:
- Input:  research/cache/manifest.json  (url → {file, content_type, ...})
- Output: drivers_extracted.json        (keyed by manu:manucode)

Driver type (high/mid/sub/pr/full_range) is determined from page/PDF content.
manu:manucode is extracted from content (JSON-LD → OG → h1/title → URL slug).

Merge: same manu:manucode from multiple sources → merged spec dict, with per-source
raw data preserved under 'sources'.

Usage:
    python scripts/extract_drivers.py [--output drivers_extracted.json]
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

try:
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit("pip install beautifulsoup4")

# Optional PDF support
try:
    import pypdf
    _HAVE_PYPDF = True
except ImportError:
    try:
        import PyPDF2 as pypdf  # older name
        _HAVE_PYPDF = True
    except ImportError:
        _HAVE_PYPDF = False

ROOT = Path(__file__).parent.parent
CACHE_DIR = ROOT / "research" / "cache"
MANIFEST_PATH = CACHE_DIR / "manifest.json"

# ---------------------------------------------------------------------------
# Site classification
# ---------------------------------------------------------------------------

def classify_url(url: str) -> str:
    h = urlparse(url).netloc.lower()
    if "doc.soundimports" in h or (url.lower().endswith(".pdf") and "soundimports" in h):
        return "datasheet_si"
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
    if url.lower().endswith(".pdf"):
        return "datasheet"
    return "other"


# ---------------------------------------------------------------------------
# Brand normalisation
# ---------------------------------------------------------------------------

_BRAND_NORM = {
    "dayton audio": "dayton",
    "dayton": "dayton",
    "sb acoustics": "sbacoustics",
    "sb-acoustics": "sbacoustics",
    "sbacoustics": "sbacoustics",
    "seas": "seas",
    "scan-speak": "scanspeak",
    "scanspeak": "scanspeak",
    "peerless": "peerless",
    "peerless by tymphany": "peerless",
    "tymphany": "peerless",
    "vifa": "peerless",
    "visaton": "visaton",
    "beyma": "beyma",
    "morel": "morel",
    "sica": "sica",
    "markaudio": "markaudio",
    "hivi": "hivi",
    "hivi swans": "hivi",
    "swan": "hivi",
    "tang band": "tangband",
    "tangband": "tangband",
    "tectonic": "tectonic",
    "faital": "faital",
    "faitalpro": "faital",
    "prv audio": "prv",
    "prv": "prv",
    "wavecor": "wavecor",
    "celestion": "celestion",
    "audaphon": "audaphon",
    "monacor": "monacor",
    "fountek": "fountek",
    "eminence": "eminence",
    "pmc": "pmc",
    "focal": "focal",
}

_KNOWN_BRANDS = sorted(_BRAND_NORM.keys(), key=len, reverse=True)


def norm_brand(raw: str) -> str:
    r = raw.lower().strip()
    return _BRAND_NORM.get(r, re.sub(r"[^a-z0-9]", "", r))


def norm_model(raw: str) -> str:
    m = raw.strip()
    m = re.sub(r"\s+", "-", m)
    m = re.sub(r"[^a-zA-Z0-9\-/]", "", m)
    m = m.strip("-")
    return m.lower()


def make_id(brand: str, model: str) -> str:
    return f"{norm_brand(brand)}:{norm_model(model)}"


# ---------------------------------------------------------------------------
# Driver type detection from free text
# ---------------------------------------------------------------------------

_TYPE_PATTERNS = [
    (re.compile(r"\bsubwoofer\b", re.I), "sub"),
    (re.compile(r"\bpassive\s+radiator\b", re.I), "pr"),
    (re.compile(r"\btweeter\b", re.I), "high"),
    (re.compile(r"\bmidrange\b|\bmid[- ]range\b", re.I), "mid"),
    (re.compile(r"\bfull[- ]range\b|\bfull range\b", re.I), "full_range"),
    (re.compile(r"\bmid[- ]?woofer\b|\bbass[- ]?midwoofer\b", re.I), "mid"),
    (re.compile(r"\bwoofer\b", re.I), "mid"),
]


def detect_type(text: str) -> str | None:
    for pat, dtype in _TYPE_PATTERNS:
        if pat.search(text):
            return dtype
    return None


# ---------------------------------------------------------------------------
# manu:manucode extraction from HTML content
# ---------------------------------------------------------------------------

def _json_ld_product(soup) -> dict | None:
    for tag in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(tag.string or "")
            if isinstance(data, list):
                for item in data:
                    if item.get("@type") == "Product":
                        return item
            elif data.get("@type") == "Product":
                return data
        except Exception:
            pass
    return None


def extract_id_from_html(soup, url: str) -> tuple[str | None, str | None, str | None]:
    """Returns (brand, model, driver_type) from HTML content."""
    brand, model, driver_type = None, None, None

    # 1. JSON-LD
    ld = _json_ld_product(soup)
    if ld:
        name = ld.get("name", "")
        brand_node = ld.get("brand", {})
        brand = brand_node.get("name") if isinstance(brand_node, dict) else str(brand_node)
        # If brand not in LD, extract from name
        if not brand or brand == name:
            for b in _KNOWN_BRANDS:
                if name.lower().startswith(b):
                    brand = b
                    model = name[len(b):].strip()
                    break
        elif brand:
            model = name.replace(brand, "").strip(" -")
        desc = ld.get("description", "")
        driver_type = detect_type(name + " " + desc)

    # 2. OG tags
    if not brand:
        og_title = soup.find("meta", property="og:title")
        if og_title:
            t = og_title.get("content", "")
            for b in _KNOWN_BRANDS:
                if t.lower().startswith(b):
                    brand = b
                    model = t[len(b):].strip(" -")
                    break

    # 3. <h1>
    if not brand:
        h1 = soup.find("h1")
        if h1:
            t = h1.get_text(strip=True)
            for b in _KNOWN_BRANDS:
                if t.lower().startswith(b):
                    brand = b
                    model = t[len(b):].strip(" -")
                    break

    # 4. <title>
    if not brand:
        title = soup.find("title")
        if title:
            t = title.get_text(strip=True).split("|")[0].split("-")[0].strip()
            for b in _KNOWN_BRANDS:
                if t.lower().startswith(b):
                    brand = b
                    model = t[len(b):].strip(" -")
                    break

    # 5. URL slug fallback
    if not brand:
        slug = urlparse(url).path.rstrip("/").split("/")[-1]
        slug = slug.replace(".html", "").replace(".php", "")
        for b in _BRAND_NORM:
            slug_b = re.sub(r"[^a-z0-9]", "-", b)
            if slug.startswith(slug_b):
                brand = b
                model = slug[len(slug_b):].strip("-")
                break
        if not brand:
            # generic slug — first segment as brand, rest as model
            parts = slug.split("-")
            brand = parts[0]
            model = "-".join(parts[1:]) if len(parts) > 1 else slug

    # Type from page body if not yet found
    if not driver_type:
        body_text = soup.get_text(" ", strip=True)[:3000]
        driver_type = detect_type(body_text)

    return brand, model, driver_type


def extract_id_from_pdf_text(text: str) -> tuple[str | None, str | None, str | None]:
    """Extract brand, model, driver_type from PDF text (first 2000 chars)."""
    sample = text[:2000]
    brand, model = None, None
    for b in _KNOWN_BRANDS:
        if b in sample.lower():
            brand = b
            # Try to extract model: words after brand name on same line
            pattern = re.compile(re.escape(b) + r"[\s\-]*([\w\-/]+)", re.I)
            m = pattern.search(sample)
            if m:
                model = m.group(1).strip()
            break
    driver_type = detect_type(sample)
    return brand, model, driver_type


# ---------------------------------------------------------------------------
# Spec field parsers (reused from refetch_drivers.py logic)
# ---------------------------------------------------------------------------

def _pf(s: str) -> float | None:
    if not s:
        return None
    s = re.sub(r"\*+", "", s)
    m = re.search(r"[-+]?\d+\.?\d*", s.replace(",", ""))
    return float(m.group()) if m else None


_SI_FIELD_MAP = {
    "impedance_ohm":     ["impedance (z)", "impedance"],
    "sensitivity_db":    ["sensitivity (spl at 1m / 2.83v)", "sensitivity", "spl"],
    "power_rms_w":       ["power handling (rms)", "rms power handling"],
    "power_max_w":       ["power handling (max)", "power handling (peak)"],
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
    "cone_material":     ["cone / diaphragm material", "cone material", "diaphragm material"],
    "surround_material": ["surround material"],
    "vc_wire":           ["voice coil wire material"],
    "frame_material":    ["basket / frame material", "basket material"],
    "magnet_material":   ["magnet material"],
    "driver_type_raw":   ["woofer type", "tweeter type", "driver type"],
    "freq_low_hz":       ["frequency response"],
}

_LABEL_TO_FIELD: dict[str, str] = {}
for _f, _ls in _SI_FIELD_MAP.items():
    for _l in _ls:
        _LABEL_TO_FIELD[_l.lower()] = _f

_TEXT_FIELDS = {"cone_material", "surround_material", "vc_wire", "frame_material",
                "driver_type_raw"}


def _norm_magnet(v: str) -> str:
    lv = v.lower()
    if "neo" in lv or "neodymium" in lv:
        return "neodymium"
    if "ferrite" in lv or "ceramic" in lv:
        return "ferrite"
    if "alnico" in lv:
        return "alnico"
    return v.strip()


def _parse_row(label: str, value: str, specs: dict) -> None:
    label = label.lower().strip().rstrip(":")
    field = _LABEL_TO_FIELD.get(label)
    if not field:
        for k, f in _LABEL_TO_FIELD.items():
            if k in label:
                field = f
                break
    if not field or not value.strip():
        return
    if field == "freq_low_hz":
        nums = re.findall(r"[\d,]+", value)
        nums = [float(n.replace(",", "")) for n in nums]
        if len(nums) >= 1:
            specs["freq_low_hz"] = nums[0]
        if len(nums) >= 2:
            specs["freq_high_hz"] = nums[1]
    elif field == "magnet_material":
        specs["magnet"] = _norm_magnet(value)
    elif field in _TEXT_FIELDS:
        specs[field] = value.strip()
    else:
        v = _pf(value)
        if v is not None:
            specs[field] = v


def parse_html_specs(soup) -> dict:
    specs: dict = {}
    for row in soup.find_all("tr"):
        cells = row.find_all(["td", "th"])
        if len(cells) >= 2:
            _parse_row(cells[0].get_text(strip=True), cells[-1].get_text(strip=True), specs)
    for dt in soup.find_all("dt"):
        dd = dt.find_next_sibling("dd")
        if dd:
            _parse_row(dt.get_text(strip=True), dd.get_text(strip=True), specs)
    return specs


def parse_price(soup) -> float | None:
    for sel in [".product-price", ".price", "[data-product-price]", ".product__price",
                "#price", "#product-price"]:
        el = soup.select_one(sel)
        if el:
            v = _pf(el.get_text())
            if v:
                return v
    return None


# ---------------------------------------------------------------------------
# Per-file extraction
# ---------------------------------------------------------------------------

def extract_html(url: str, raw: bytes) -> dict:
    soup = BeautifulSoup(raw, "html.parser")
    brand, model, driver_type = extract_id_from_html(soup, url)
    specs = parse_html_specs(soup)
    price = parse_price(soup)

    # driver_type_raw from specs overrides content detection
    raw_type = specs.pop("driver_type_raw", None)
    if raw_type and not driver_type:
        driver_type = detect_type(raw_type) or raw_type.lower()

    stock_el = soup.select_one(".stock-status, .availability, .product-stock, "
                               ".product__inventory, [class*=stock], .lieferzeit")
    stock = stock_el.get_text(strip=True) if stock_el else None

    site = classify_url(url)
    price_key = {"soundimports": "price_eur", "willys": "price_gbp",
                 "hfc": "price_gbp", "falcon": "price_gbp",
                 "lss": "price_eur", "dayton": "price_usd"}.get(site, "price")

    return {
        "brand": brand,
        "model": model,
        "driver_type": driver_type,
        "specs": specs,
        price_key: price,
        "stock": stock,
    }


def extract_pdf(url: str, raw: bytes) -> dict:
    if not _HAVE_PYPDF:
        return {"brand": None, "model": None, "driver_type": None, "specs": {}}
    import io
    try:
        reader = pypdf.PdfReader(io.BytesIO(raw))
        text = "\n".join(
            page.extract_text() or "" for page in reader.pages[:3]
        )
    except Exception as e:
        return {"brand": None, "model": None, "driver_type": None, "specs": {},
                "error": str(e)}

    brand, model, driver_type = extract_id_from_pdf_text(text)

    # Parse any spec table rows from the PDF text
    specs: dict = {}
    for line in text.splitlines():
        if ":" in line:
            parts = line.split(":", 1)
            _parse_row(parts[0], parts[1], specs)

    return {
        "brand": brand,
        "model": model,
        "driver_type": driver_type,
        "specs": specs,
    }


# ---------------------------------------------------------------------------
# Merge priority
# ---------------------------------------------------------------------------

_MERGE_ORDER = ["soundimports", "datasheet_si", "datasheet", "loudspeakerdatabase",
                "dayton", "hfc", "falcon", "willys", "lss", "parts_express", "other"]


def merge_driver_data(sources: dict) -> dict:
    merged_specs: dict = {}
    for site in _MERGE_ORDER:
        for k, v in sources.get(site, {}).get("specs", {}).items():
            if k not in merged_specs and v is not None:
                merged_specs[k] = v
    prices = {}
    for site, data in sources.items():
        for pk in ("price_eur", "price_gbp", "price_usd", "price"):
            if data.get(pk):
                prices[f"{site}_{pk}"] = data[pk]
    return {"specs": merged_specs, "prices": prices}


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default="drivers_extracted.json")
    args = ap.parse_args()

    if not MANIFEST_PATH.exists():
        sys.exit(f"Manifest not found: {MANIFEST_PATH}\nRun download_cache.py first.")

    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    print(f"Processing {len(manifest)} cached files…")

    # driver_id → {brand, model, driver_type, sources: {site → raw_data}}
    drivers: dict[str, dict] = {}
    skipped = 0

    for url, entry in manifest.items():
        if entry.get("status") != 200:
            skipped += 1
            continue
        fname = entry.get("file")
        if not fname:
            skipped += 1
            continue
        fpath = CACHE_DIR / fname
        if not fpath.exists():
            skipped += 1
            continue

        raw = fpath.read_bytes()
        ct = entry.get("content_type", "text/html").lower()
        site = classify_url(url)

        if "pdf" in ct or url.lower().endswith(".pdf"):
            data = extract_pdf(url, raw)
        else:
            data = extract_html(url, raw)

        brand = data.get("brand") or ""
        model = data.get("model") or ""
        driver_type = data.get("driver_type")

        if not brand or not model:
            # Can't generate a meaningful ID — store under the URL hash prefix
            import hashlib
            did = f"unknown:{hashlib.sha256(url.encode()).hexdigest()[:12]}"
        else:
            did = make_id(brand, model)

        if did not in drivers:
            drivers[did] = {
                "id": did,
                "brand": norm_brand(brand) if brand else None,
                "model": model or None,
                "driver_type": driver_type,
                "sources": {},
            }
        else:
            # Fill in type if not yet known
            if not drivers[did]["driver_type"] and driver_type:
                drivers[did]["driver_type"] = driver_type

        drivers[did]["sources"][site] = {
            "url": url,
            "cached_file": fname,
            **{k: v for k, v in data.items() if k not in ("brand", "model", "driver_type")},
        }

    # Second pass: merge specs
    output_drivers = []
    for did, d in drivers.items():
        merged = merge_driver_data(d["sources"])
        output_drivers.append({
            "id": did,
            "brand": d["brand"],
            "model": d["model"],
            "driver_type": d["driver_type"],
            "merged": merged,
            "sources": d["sources"],
        })

    output_drivers.sort(key=lambda x: (x.get("driver_type") or "", x.get("model") or ""))

    out_path = ROOT / args.output
    out_path.write_text(
        json.dumps({
            "generated": datetime.now(timezone.utc).isoformat(),
            "driver_count": len(output_drivers),
            "skipped_entries": skipped,
            "drivers": output_drivers,
        }, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )
    print(f"Written {len(output_drivers)} drivers ({skipped} skipped) -> {out_path}")
    if not _HAVE_PYPDF:
        print("Note: pypdf not installed - PDF datasheets not parsed. pip install pypdf")


if __name__ == "__main__":
    main()

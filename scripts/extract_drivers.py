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
import html as _html
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

try:
    import pypdf
    _HAVE_PYPDF = True
except ImportError:
    try:
        import PyPDF2 as pypdf
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
        return "ldb"
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


def _extract_model_code(raw: str) -> str:
    """Strip description text after the model code in a product title suffix.

    "3FE25-16F 3\" Full-range Woofer 16 Ohm" → "3FE25-16F"
    "SIG150-4 5.25\" Woofer 4Ω"              → "SIG150-4"
    "Alpair-5 Grey 3\" Full Range Aluminium"  → "Alpair-5"
    """
    raw = _html.unescape(raw).strip()
    tokens = raw.split()
    for tok in tokens:
        tok_clean = re.sub(r"[^A-Za-z0-9\-/\.]", "", tok)
        if (len(tok_clean) >= 2
                and re.search(r"[A-Za-z]", tok_clean)
                and re.search(r"[0-9]", tok_clean)):
            return tok_clean
    return re.sub(r"[^A-Za-z0-9\-/\.]", "", tokens[0]) if tokens else raw


# ---------------------------------------------------------------------------
# Driver type detection
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


def _title_zone(soup) -> str:
    """Narrow text zone for driver type detection — title/h1/meta only.
    Avoids false 'sub' matches from page footer/nav category links.
    """
    parts = []
    t = soup.find("title")
    if t:
        parts.append(t.get_text(strip=True))
    h1 = soup.find("h1")
    if h1:
        parts.append(h1.get_text(strip=True))
    desc = soup.find("meta", attrs={"name": "description"})
    if desc:
        parts.append(desc.get("content", ""))
    og = soup.find("meta", property="og:title")
    if og:
        parts.append(og.get("content", ""))
    return " ".join(parts)


# ---------------------------------------------------------------------------
# General HTML ID extraction (non-LDB)
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

    # 1. JSON-LD Product
    ld = _json_ld_product(soup)
    if ld:
        name = _html.unescape(ld.get("name", ""))
        brand_node = ld.get("brand", {})
        brand = brand_node.get("name") if isinstance(brand_node, dict) else str(brand_node)
        if not brand or brand == name:
            for b in _KNOWN_BRANDS:
                if name.lower().startswith(b):
                    brand = b
                    model = _extract_model_code(name[len(b):].strip())
                    break
        elif brand:
            model = _extract_model_code(name.replace(brand, "").strip(" -"))
        desc = ld.get("description", "")
        driver_type = detect_type(name + " " + desc)

    # 2. OG tags
    if not brand:
        og_title = soup.find("meta", property="og:title")
        if og_title:
            t = _html.unescape(og_title.get("content", ""))
            for b in _KNOWN_BRANDS:
                if t.lower().startswith(b):
                    brand = b
                    model = _extract_model_code(t[len(b):].strip(" -"))
                    break

    # 3. <h1>
    if not brand:
        h1 = soup.find("h1")
        if h1:
            t = _html.unescape(h1.get_text(strip=True))
            for b in _KNOWN_BRANDS:
                if t.lower().startswith(b):
                    brand = b
                    model = _extract_model_code(t[len(b):].strip(" -"))
                    break

    # 4. <title>
    if not brand:
        title = soup.find("title")
        if title:
            t = _html.unescape(title.get_text(strip=True).split("|")[0].split("-")[0].strip())
            for b in _KNOWN_BRANDS:
                if t.lower().startswith(b):
                    brand = b
                    model = _extract_model_code(t[len(b):].strip(" -"))
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
            parts = slug.split("-")
            brand = parts[0]
            model = "-".join(parts[1:]) if len(parts) > 1 else slug

    # Restrict type detection to title/h1/meta — not full body
    if not driver_type:
        driver_type = detect_type(_title_zone(soup))

    return brand, model, driver_type


# ---------------------------------------------------------------------------
# LDB-specific extraction
# ---------------------------------------------------------------------------

# data-highlight → (output_field, scale_factor_or_None, is_text)
_LDB_HL: dict[str, tuple[str, float | None, bool]] = {
    "spl1w":             ("sensitivity_db",    None,  False),
    "fs":                ("fs_hz",             None,  False),
    "qms":               ("qms",               None,  False),
    "qes":               ("qes",               None,  False),
    "qts":               ("qts",               None,  False),
    "xmax":              ("xmax_mm",           None,  False),
    "vd":                ("vd_cm3",            None,  False),
    "pw":                ("power_rms_w",       None,  False),
    "pmax":              ("power_max_w",       None,  False),
    "z":                 ("impedance_ohm",     None,  False),
    "re":                ("re_ohm",            None,  False),
    "le":                ("le_mh",             None,  False),
    "vc_diam":           ("vc_mm",             None,  False),
    "vc_material":       ("vc_wire",           None,  True),
    "bl":                ("bl_tm",             None,  False),
    "sd":                ("sd_cm2",            None,  False),
    "mms":               ("mms_g",             None,  False),
    "cms":               ("cms_mm_n",          0.001, False),  # µm/N → mm/N
    "vas":               ("vas_l",             None,  False),
    "diaphragm_material":("cone_material",     None,  True),
    "surround_material": ("surround_material", None,  True),
    "magnet":            ("magnet",            None,  True),
    "frame_material":    ("frame_material",    None,  True),
    "diam":              ("frame_od_mm",       None,  False),
    "mounting_diam":     ("cutout_mm",         None,  False),
    "depth":             ("depth_mm",          None,  False),
}

_LDB_MAGNET_NORM = {"ferrite": "ferrite", "ceramic": "ferrite",
                    "neodymium": "neodymium", "neo": "neodymium", "alnico": "alnico"}


def _ldb_brand_model(url: str) -> tuple[str, str]:
    """Extract brand and model directly from LDB URL path: /Brand/Model"""
    parts = urlparse(url).path.strip("/").split("/")
    brand = parts[0] if len(parts) >= 1 else ""
    model = parts[1] if len(parts) >= 2 else ""
    return brand, model


def parse_ldb_specs(soup) -> dict:
    """Extract T/S parameters from LDB page using data-highlight attributes."""
    specs: dict = {}

    # Remove comparison driver tables — they have the same data-highlight attrs
    # but belong to other drivers shown as "similar" in the sidebar.
    for tbl in soup.find_all("table", class_="driver_data"):
        tbl.decompose()

    seen: set = set()
    for li in soup.find_all("li"):
        hl_spans = [s for s in li.find_all("span") if s.get("data-highlight")]
        if not hl_spans:
            continue
        hl = hl_spans[0].get("data-highlight", "").strip()
        if not hl or hl in seen:
            continue
        seen.add(hl)

        mapping = _LDB_HL.get(hl)
        if not mapping:
            continue
        field, scale, is_text = mapping

        # Frequency response — extract low/high Hz pair
        if hl == "fr":
            val_span = li.find("span", class_="value")
            if val_span:
                nums = re.findall(r"\d+", val_span.get_text())
                if len(nums) >= 2:
                    specs["freq_low_hz"] = float(nums[0])
                    specs["freq_high_hz"] = float(nums[1])
            continue

        val_span = li.find("span", class_="value")
        if not val_span:
            continue
        raw_val = val_span.get_text(strip=True).lstrip("±").strip()

        if is_text:
            # Normalise magnet material; store others as-is
            txt = raw_val.strip()
            if field == "magnet":
                txt = _LDB_MAGNET_NORM.get(txt.lower(), txt.lower())
            if txt:
                specs[field] = txt
        else:
            v = _pf(raw_val)
            if v is None:
                continue
            if scale:
                v = round(v * scale, 6)
            specs[field] = v

    return specs


def _ldb_driver_type(soup) -> str | None:
    """Use LDB's own type classification from the type-ribbon link."""
    ribbon = soup.select_one("a.type-ribbon h2, .type-ribbon")
    if ribbon:
        return detect_type(ribbon.get_text(strip=True))
    return detect_type(_title_zone(soup))


# ---------------------------------------------------------------------------
# Spec field parsers — SI / generic HTML
# ---------------------------------------------------------------------------

def _pf(s: str) -> float | None:
    if not s:
        return None
    s = re.sub(r"\*+", "", s)
    m = re.search(r"[-+]?\d+\.?\d*", s.replace(",", ""))
    return float(m.group()) if m else None


def _parse_eur_price(s: str) -> float | None:
    """Parse European price format where comma is the decimal separator.

    "19,95"      → 19.95
    "€ 19,95"    → 19.95
    "1.234,56"   → 1234.56
    """
    s = re.sub(r"[€$£ \s]", "", s)
    # European decimal: digits, optional dot-thousands, comma, 2 decimal digits
    m = re.search(r"(\d{1,3}(?:\.\d{3})*),(\d{2})(?!\d)", s)
    if m:
        integer = m.group(1).replace(".", "")
        return float(integer + "." + m.group(2))
    # Standard decimal
    m = re.search(r"(\d+\.\d+|\d+)", s.replace(",", ""))
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
            v = _parse_eur_price(el.get_text())
            if v and v > 0:
                return v
    return None


# ---------------------------------------------------------------------------
# Per-file extraction
# ---------------------------------------------------------------------------

def extract_html(url: str, raw: bytes) -> dict:
    soup = BeautifulSoup(raw, "html.parser")
    site = classify_url(url)

    # LDB pages have a clean brand/model in the URL and a structured T/S section
    if site == "ldb":
        brand_raw, model_raw = _ldb_brand_model(url)
        driver_type = _ldb_driver_type(soup)
        specs = parse_ldb_specs(soup)
        return {
            "brand": brand_raw,
            "model": model_raw,
            "driver_type": driver_type,
            "specs": specs,
        }

    brand, model, driver_type = extract_id_from_html(soup, url)
    specs = parse_html_specs(soup)
    price = parse_price(soup)

    raw_type = specs.pop("driver_type_raw", None)
    if raw_type and not driver_type:
        driver_type = detect_type(raw_type) or raw_type.lower()

    stock_el = soup.select_one(".stock-status, .availability, .product-stock, "
                               ".product__inventory, [class*=stock], .lieferzeit")
    stock = stock_el.get_text(strip=True) if stock_el else None

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

    brand, model, driver_type = _extract_id_from_pdf(text, url)

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


def _extract_id_from_pdf(text: str, url: str) -> tuple[str | None, str | None, str | None]:
    """Extract brand/model from PDF text, falling back to URL path."""
    sample = text[:2000]

    # Try URL path first for known datasheet patterns
    # e.g. doc.soundimports.nl/pdf/brands/HiVi/B4N/... → brand=HiVi, model=B4N
    path = urlparse(url).path
    parts = [p for p in path.split("/") if p and p.lower() not in
             ("pdf", "brands", "datasheet", "datasheets", "documents", "files")]
    brand, model = None, None
    for p in parts:
        if brand and not model:
            # Skip version-suffix files like "pdf_hiVi_B4N_1.pdf"
            if p.lower().startswith("pdf_") or re.match(r"pdf_", p, re.I):
                break
            model = re.sub(r"[^A-Za-z0-9\-/\.]", "", p)
            break
        for b in _BRAND_NORM:
            if b in p.lower() or p.lower() in b:
                brand = p
                break

    # Fall back to text scan
    if not brand:
        for b in _KNOWN_BRANDS:
            if b in sample.lower():
                brand = b
                pat = re.compile(re.escape(b) + r"[\s\-]*([\w\-/]+)", re.I)
                m = pat.search(sample)
                if m:
                    model = m.group(1).strip()
                break

    driver_type = detect_type(sample)
    return brand, model, driver_type


# ---------------------------------------------------------------------------
# Merge priority
# ---------------------------------------------------------------------------

_MERGE_ORDER = ["soundimports", "ldb", "datasheet_si", "datasheet",
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
            if not drivers[did]["driver_type"] and driver_type:
                drivers[did]["driver_type"] = driver_type

        drivers[did]["sources"][site] = {
            "url": url,
            "cached_file": fname,
            **{k: v for k, v in data.items() if k not in ("brand", "model", "driver_type")},
        }

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
        print("Note: pypdf not installed — PDF datasheets not parsed. pip install pypdf")


if __name__ == "__main__":
    main()

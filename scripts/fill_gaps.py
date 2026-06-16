#!/usr/bin/env python3
"""
fill_gaps.py — Fill missing T/S and spec fields in drivers.json from cached files.

No API calls. Parses cached HTML (SoundImports <dl> structure) and PDFs
(pypdf text + regex) to extract values and write them into any blank field.
Existing values in drivers.json are NEVER overwritten.

Output: drivers_merged.json  (review before promoting to drivers.json)
        fill_gaps_report.txt  (summary of what was filled / what's still missing)

Usage:
    python scripts/fill_gaps.py
    python scripts/fill_gaps.py --dry-run   # report only, no output file
"""

import argparse
import io
import json
import re
import sys
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
    _HAVE_PYPDF = False

ROOT      = Path(__file__).parent.parent
CACHE_DIR = ROOT / "research" / "cache"
MANIFEST  = CACHE_DIR / "manifest.json"
DJ_PATH   = ROOT / "drivers.json"
OUT_PATH  = ROOT / "drivers_merged.json"
RPT_PATH  = ROOT / "fill_gaps_report.txt"

# ---------------------------------------------------------------------------
# SoundImports <dl> label → (field_name, unit_hint)
# ---------------------------------------------------------------------------
_SI_LABEL = {
    # T/S parameters (short form inside "Thiele-Small" section)
    "fs":              ("fs_hz",          "hz"),
    "qts":             ("qts",            None),
    "qes":             ("qes",            None),
    "qms":             ("qms",            None),
    "re":              ("re_ohm",         "ohm"),
    "le":              ("le_mh",          "mh"),
    "mms":             ("mms_g",          "g"),
    "cms":             ("cms_mm_n",       "cms"),   # unit ambiguous — handle separately
    "sd":              ("sd_cm2",         "cm2"),
    "vas":             ("vas_l",          "l"),
    "bl":              ("bl_tm",          None),
    "xmax":            ("xmax_mm",        "mm"),
    "vd":              ("vd_cm3",         "cm3"),
    # Full-label forms (SI product page — main specs section)
    "resonant frequency (fs)":            ("fs_hz",          "hz"),
    "resonant frequency":                 ("fs_hz",          "hz"),
    "dc resistance (re)":                 ("re_ohm",         "ohm"),
    "dc resistance":                      ("re_ohm",         "ohm"),
    "voice coil inductance (le)":         ("le_mh",          "mh"),
    "voice coil inductance":              ("le_mh",          "mh"),
    "impedance (z)":                      ("impedance_ohm",  "ohm"),
    "nominal impedance":                  ("impedance_ohm",  "ohm"),
    "sensitivity (spl at 1m / 2.83v)":   ("sensitivity_db", "db"),
    "sensitivity (spl at 1w/1m)":        ("sensitivity_db", "db"),
    "sensitivity":                        ("sensitivity_db", "db"),
    "power handling (rms)":               ("power_rms_w",    "w"),
    "power handling (max)":               ("power_max_w",    "w"),
    "rms power handling":                 ("power_rms_w",    "w"),
    "rms power handling (aes 426b)":      ("power_rms_w",    "w"),
    "program power":                      ("power_max_w",    "w"),
    "overall outside diameter":           ("frame_od_mm",    "mm"),
    "outside diameter":                   ("frame_od_mm",    "mm"),
    "cutout diameter":                    ("cutout_mm",      "mm"),
    "depth":                              ("depth_mm",       "mm"),
    "voice coil diameter":                ("vc_mm",          "mm"),
    "diaphragm material":                 ("cone_material",  "str"),
    "cone material":                      ("cone_material",  "str"),
    "surround material":                  ("surround_material", "str"),
    "surround":                           ("surround_material", "str"),
    "magnet":                             ("magnet",         "str"),
    "frame material":                     ("frame_material", "str"),
    "voice coil wire":                    ("vc_wire",        "str"),
    # SI Thiele-Small section uses long labels WITHOUT abbreviation in parens
    "total q":                            ("qts",            None),
    "total q (qts)":                      ("qts",            None),
    "electrical q":                       ("qes",            None),
    "electrical q (qes)":                 ("qes",            None),
    "mechanical q":                       ("qms",            None),
    "mechanical q (qms)":                 ("qms",            None),
    "linear excursion":                        ("xmax_mm",  "mm"),
    "linear excursion (xmax)":                 ("xmax_mm",  "mm"),
    "maximum linear excursion":                ("xmax_mm",  "mm"),
    "maximum linear excursion (xmax)":         ("xmax_mm",  "mm"),
    "diaphragm mass inc. airload":             ("mms_g",    "g"),
    "diaphragm mass inc. airload (mms)":       ("mms_g",    "g"),
    "moving mass (incl. air load)":            ("mms_g",    "g"),
    "moving mass incl. air load":              ("mms_g",    "g"),
    "mechanical compliance of suspension":          ("cms_mm_n", "cms"),
    "mechanical compliance of suspension (cms)":    ("cms_mm_n", "cms"),
    "effective piston area":                   ("sd_cm2",   "cm2"),
    "effective piston area (sd)":              ("sd_cm2",   "cm2"),
    "surface area of cone":                    ("sd_cm2",   "cm2"),
    "surface area of cone (sd)":               ("sd_cm2",   "cm2"),
    "equivalent compliance volume":            ("vas_l",    "l"),
    "equivalent compliance volume (vas)":      ("vas_l",    "l"),
    "compliance equivalent volume":            ("vas_l",    "l"),
    "compliance equivalent volume (vas)":      ("vas_l",    "l"),
    "force factor":                            ("bl_tm",    None),
    "force factor (bl)":                       ("bl_tm",    None),
    "bl product":                              ("bl_tm",    None),
    "bl product (bl)":                         ("bl_tm",    None),
    "electromagnetic q":                       ("qes",      None),
    "electromagnetic q (qes)":                 ("qes",      None),
    "volume displacement":                     ("vd_cm3",   "cm3"),
    "volume displacement (vd)":                ("vd_cm3",   "cm3"),
    "overall depth":                           ("depth_mm", "mm"),
    "voice coil wire material":                ("vc_wire",  "str"),
    "basket / frame material":                 ("frame_material", "str"),
    "magnet material":                         ("magnet",   "str"),
}

# Frequency-response label → parse "A-B Hz" into two fields
_FREQ_LABELS = {
    "frequency response", "freq. range", "frequency range",
    "usable frequency range",
}

# ---------------------------------------------------------------------------
# Value parsers
# ---------------------------------------------------------------------------

def _parse_num(s: str) -> float | None:
    """Extract the first number from a string like '550 Hz', '4.8 Ω', '90 dB'."""
    # Handle European decimals like "19,95" — but only when followed by exactly 2 digits
    s2 = re.sub(r"(\d{1,3}(?:\.\d{3})*),(\d{2})(?!\d)", lambda m: m.group(1).replace(".", "") + "." + m.group(2), s)
    m = re.search(r"[-+]?\d+(?:[.,]\d+)?", s2.replace(",", "."))
    return float(m.group().replace(",", ".")) if m else None


def _parse_freq_range(s: str) -> tuple[float | None, float | None]:
    """Parse '1500 - 25000 Hz' → (1500.0, 25000.0)."""
    nums = re.findall(r"\d+(?:[.,]\d+)?", s.replace(",", "."))
    if len(nums) >= 2:
        return float(nums[0]), float(nums[-1])
    return None, None


def _parse_cms(raw: str, label: str) -> float | None:
    """
    Cms is sometimes µm/N (LDB/datasheets) and sometimes mm/N (SI).
    SI states mm/N explicitly; if the unit string contains 'µm' or 'um', divide by 1000.
    """
    val = _parse_num(raw)
    if val is None:
        return None
    low = raw.lower()
    if "µm" in low or "um/n" in low or "micrometer" in low:
        val /= 1000.0
    return val


def _parse_size_inch(raw: str) -> float | None:
    """Extract inch size from strings like '26 mm | 1\"' or '1.0 inch' or '25 mm'."""
    # Explicit inch marker
    m = re.search(r'(\d+(?:[.,]\d+)?)\s*(?:"|\'\'|inch)', raw, re.I)
    if m:
        return float(m.group(1).replace(",", "."))
    # Just mm — convert
    m = re.search(r'(\d+(?:[.,]\d+)?)\s*mm', raw, re.I)
    if m:
        mm = float(m.group(1).replace(",", "."))
        return round(mm / 25.4, 3)
    return None


def _parse_price_eur(s: str) -> float | None:
    s = re.sub(r"[€$£\s]", "", s)
    m = re.search(r"(\d{1,3}(?:\.\d{3})*),(\d{2})(?!\d)", s)
    if m:
        return float(m.group(1).replace(".", "") + "." + m.group(2))
    m = re.search(r"\d+\.\d+|\d+", s.replace(",", ""))
    return float(m.group()) if m else None


# ---------------------------------------------------------------------------
# SI HTML parser
# ---------------------------------------------------------------------------

def _extract_from_si_html(raw: bytes) -> dict:
    """Parse a SoundImports product page — returns flat dict of spec fields."""
    soup = BeautifulSoup(raw, "html.parser")
    result: dict = {}

    # ---- specs <dl> --------------------------------------------------------
    specs_sec = soup.find(id=re.compile(r"^specs?$", re.I))
    dls = specs_sec.find_all("dl") if specs_sec else soup.find_all("dl")

    for dl in dls:
        items = dl.find_all("div")
        if not items:
            # flat dt/dd pairs
            dts = dl.find_all("dt")
            dds = dl.find_all("dd")
            items_pairs = list(zip(dts, dds))
        else:
            items_pairs = []
            for item in items:
                dt = item.find("dt")
                dd = item.find("dd")
                if dt and dd:
                    items_pairs.append((dt, dd))

        for dt, dd in items_pairs:
            label = dt.get_text(strip=True).lower().rstrip(":")
            value = dd.get_text(strip=True)

            if label in _FREQ_LABELS:
                lo, hi = _parse_freq_range(value)
                if lo is not None and "freq_low_hz" not in result:
                    result["freq_low_hz"] = lo
                if hi is not None and "freq_high_hz" not in result:
                    result["freq_high_hz"] = hi
                continue

            if "cone / dome diameter" in label or "cone diameter" in label:
                sz = _parse_size_inch(value)
                if sz and "nominal_size_inch" not in result:
                    result["nominal_size_inch"] = sz
                continue

            mapping = _SI_LABEL.get(label)
            if not mapping:
                continue
            field, unit_hint = mapping

            if unit_hint == "str":
                if field not in result and value:
                    # Normalise magnet type
                    if field == "magnet":
                        v_low = value.lower()
                        if "neo" in v_low:
                            value = "neodymium"
                        elif "ferr" in v_low:
                            value = "ferrite"
                        elif "alnico" in v_low:
                            value = "alnico"
                    result[field] = value
            elif unit_hint == "cms":
                val = _parse_cms(value, label)
                if val is not None and field not in result:
                    result[field] = val
            else:
                val = _parse_num(value)
                if val is not None and field not in result:
                    # Vas in litres — SI sometimes shows "8.40 L" or "8400 cm³"
                    if field == "vas_l" and "cm" in value.lower():
                        val /= 1000.0
                    result[field] = val

    # ---- price -------------------------------------------------------------
    for el in soup.find_all(class_=re.compile(r"price", re.I), limit=8):
        txt = el.get_text(strip=True)
        p = _parse_price_eur(txt)
        if p and 1 < p < 2000 and "price_eur" not in result:
            result["price_eur"] = p
            break

    return result


# ---------------------------------------------------------------------------
# PDF text parser
# ---------------------------------------------------------------------------

# Maps regex label patterns → (field, unit_hint)
_PDF_PATTERNS: list[tuple[re.Pattern, str, str]] = [
    (re.compile(r"\bFs\b.*?(\d+\.?\d*)\s*Hz",        re.I), "fs_hz",          ""),
    (re.compile(r"\bQts\b.*?(\d+\.?\d*)",             re.I), "qts",             ""),
    (re.compile(r"\bQes\b.*?(\d+\.?\d*)",             re.I), "qes",             ""),
    (re.compile(r"\bQms\b.*?(\d+\.?\d*)",             re.I), "qms",             ""),
    (re.compile(r"\bRe\b.*?(\d+\.?\d*)\s*[ΩΩohm]",   re.I), "re_ohm",          ""),
    (re.compile(r"\bLe\b.*?(\d+\.?\d*)\s*mH",         re.I), "le_mh",           ""),
    (re.compile(r"\bMms\b.*?(\d+\.?\d*)\s*g",         re.I), "mms_g",           ""),
    (re.compile(r"\bCms\b.*?(\d+\.?\d*)\s*(mm/N|µm/N|um/N)", re.I), "cms_raw", ""),
    (re.compile(r"\bSd\b.*?(\d+\.?\d*)\s*cm",         re.I), "sd_cm2",          ""),
    (re.compile(r"\bVas\b.*?(\d+\.?\d*)\s*l(?:it)?",  re.I), "vas_l",           ""),
    (re.compile(r"\bBl\b.*?(\d+\.?\d*)\s*T",          re.I), "bl_tm",           ""),
    (re.compile(r"\bXmax\b.*?(\d+\.?\d*)\s*mm",       re.I), "xmax_mm",         ""),
    (re.compile(r"\bVd\b.*?(\d+\.?\d*)\s*cm",         re.I), "vd_cm3",          ""),
    (re.compile(r"(?:Nominal\s+)?[Ii]mpedance.*?(\d+\.?\d*)\s*[ΩΩohm]", re.I), "impedance_ohm", ""),
    (re.compile(r"[Ss]ensitivity.*?(\d{2,3}\.?\d*)\s*dB", re.I), "sensitivity_db", ""),
    (re.compile(r"(?:RMS\s+)?[Pp]ower.*?(\d+\.?\d*)\s*W", re.I), "power_rms_w", ""),
]


def _extract_from_pdf(raw: bytes) -> dict:
    if not _HAVE_PYPDF:
        return {}
    try:
        reader = pypdf.PdfReader(io.BytesIO(raw))
        text = "\n".join(p.extract_text() or "" for p in reader.pages[:6])
    except Exception:
        return {}
    if len(text) < 50:
        return {}

    result: dict = {}
    for pat, field, _ in _PDF_PATTERNS:
        if field in result:
            continue
        if field == "cms_raw":
            m = pat.search(text)
            if m:
                val = float(m.group(1))
                unit = m.group(2).lower()
                if "µm" in unit or "um" in unit:
                    val /= 1000.0
                result["cms_mm_n"] = val
        else:
            m = pat.search(text)
            if m:
                result[field] = float(m.group(1))

    return result


# ---------------------------------------------------------------------------
# Generic HTML fallback (Willys, HFC, SB Acoustics etc.)
# ---------------------------------------------------------------------------

def _extract_from_generic_html(raw: bytes) -> dict:
    """Try DL and TABLE elements on non-SI pages."""
    soup = BeautifulSoup(raw, "html.parser")
    result: dict = {}

    pairs: list[tuple[str, str]] = []

    # All DL elements
    for dl in soup.find_all("dl"):
        dts = dl.find_all("dt")
        dds = dl.find_all("dd")
        for dt, dd in zip(dts, dds):
            pairs.append((dt.get_text(strip=True), dd.get_text(strip=True)))

    # All tables
    for table in soup.find_all("table"):
        for row in table.find_all("tr"):
            cells = row.find_all(["th", "td"])
            if len(cells) >= 2:
                pairs.append((cells[0].get_text(strip=True), cells[1].get_text(strip=True)))

    for label_raw, value in pairs:
        label = label_raw.lower().rstrip(":")

        if any(lbl in label for lbl in _FREQ_LABELS):
            lo, hi = _parse_freq_range(value)
            if lo and "freq_low_hz" not in result:
                result["freq_low_hz"] = lo
            if hi and "freq_high_hz" not in result:
                result["freq_high_hz"] = hi
            continue

        mapping = _SI_LABEL.get(label)
        if not mapping:
            # Try partial match for common short labels
            for key, mp in _SI_LABEL.items():
                if label == key or label.startswith(key + " ") or label.endswith(" " + key):
                    mapping = mp
                    break
        if not mapping:
            continue

        field, unit_hint = mapping
        if field in result:
            continue

        if unit_hint == "str":
            if value:
                result[field] = value
        elif unit_hint == "cms":
            val = _parse_cms(value, label)
            if val is not None:
                result[field] = val
        else:
            val = _parse_num(value)
            if val is not None:
                if field == "vas_l" and "cm" in value.lower():
                    val /= 1000.0
                result[field] = val

    return result


# ---------------------------------------------------------------------------
# Manifest lookup: find cached files for a given driver
# ---------------------------------------------------------------------------

def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", str(s).lower())


def _candidate_slugs(driver: dict) -> list[str]:
    """
    Return a ranked list of slugs to try matching against URL paths.
    Handles malformed entries like brand='SEAS 27TDFC H1189-06' where
    the real model code is embedded in the brand/model string.
    """
    raw_model = str(driver.get("model", ""))
    raw_brand = str(driver.get("brand", ""))
    raw_id    = str(driver.get("id", ""))

    candidates: list[str] = []

    # 1. Full model slug
    ms = _slug(raw_model)
    if ms:
        candidates.append(ms)

    # 2. First space-delimited token from model that looks like a part number
    #    e.g. "SEAS 27TDFC H1189-06" → "27TDFC" → "27tdfc"
    for tok in raw_model.split():
        ts = _slug(tok)
        if len(ts) >= 4 and re.search(r"[a-z]", ts) and re.search(r"\d", ts):
            if ts not in candidates:
                candidates.append(ts)

    # 3. First 6–8 chars of model slug (handles BMR suffix, etc.)
    if ms and len(ms) > 6:
        candidates.append(ms[:6])

    # 4. ID-derived slug without brand prefix
    id_slug = _slug(raw_id)
    brand_slug = _slug(raw_brand)
    if id_slug.startswith(brand_slug) and len(id_slug) > len(brand_slug):
        candidates.append(id_slug[len(brand_slug):])

    return [c for c in candidates if len(c) >= 4]


def _find_cached(driver: dict, manifest: dict) -> list[tuple[str, dict]]:
    """Return list of (url, entry) for all cached 200-OK pages matching this driver."""
    slugs = _candidate_slugs(driver)
    if not slugs:
        return []

    seen: set[str] = set()
    hits: list[tuple[str, dict]] = []
    for url, entry in manifest.items():
        if entry.get("status") != 200:
            continue
        if not entry.get("file"):
            continue
        if not (CACHE_DIR / entry["file"]).exists():
            continue
        path_slug = _slug(urlparse(url).path)
        for s in slugs:
            if s in path_slug and url not in seen:
                seen.add(url)
                hits.append((url, entry))
                break
    return hits


# ---------------------------------------------------------------------------
# Main merge logic
# ---------------------------------------------------------------------------

_FILLABLE = {
    "fs_hz", "qts", "qes", "qms", "re_ohm", "le_mh", "mms_g", "cms_mm_n",
    "sd_cm2", "vas_l", "bl_tm", "xmax_mm", "vd_cm3", "impedance_ohm",
    "sensitivity_db", "power_rms_w", "power_max_w", "freq_low_hz", "freq_high_hz",
    "frame_od_mm", "cutout_mm", "depth_mm", "vc_mm", "magnet",
    "cone_material", "surround_material", "frame_material", "vc_wire",
    "nominal_size_inch",
}

# Only the fields actually used in crossover/solutions analysis, by role.
# Tweeters don't publish Qts/Sd/Xmax — don't flag those as missing.
_CRITICAL_BY_ROLE: dict[str, set] = {
    "mid":  {"fs_hz", "sensitivity_db", "impedance_ohm", "power_rms_w", "qts", "xmax_mm"},
    "high": {"fs_hz", "sensitivity_db", "impedance_ohm", "power_rms_w"},
    "sub":  {"fs_hz", "qts", "xmax_mm", "sensitivity_db", "impedance_ohm"},
    "pr":   {"fs_hz", "qms", "xmax_mm"},
    "excl": {"sensitivity_db", "impedance_ohm"},   # excluded — only care about basic id
}
_CRITICAL = {"fs_hz", "sensitivity_db", "impedance_ohm", "power_rms_w"}  # fallback


def _extract_all(url: str, entry: dict) -> dict:
    """Run the appropriate extractor for a given cached file."""
    raw = (CACHE_DIR / entry["file"]).read_bytes()
    ct  = entry.get("content_type", "text/html").lower()
    if "pdf" in ct or url.lower().endswith(".pdf"):
        return _extract_from_pdf(raw)
    if "soundimports" in url:
        return _extract_from_si_html(raw)
    return _extract_from_generic_html(raw)


def run(args):
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    dj       = json.loads(DJ_PATH.read_text(encoding="utf-8"))
    drivers  = dj["drivers"]

    report_lines: list[str] = []
    total_filled = 0

    for drv in drivers:
        did   = drv.get("id", "?")
        role  = drv.get("role", "?")
        cached = _find_cached(drv, manifest)

        # Merge extracted specs — try all matching files, prefer SI HTML first
        merged: dict = {}
        sources_used: list[str] = []

        si_hits   = [(u, e) for u, e in cached if "soundimports" in u and not u.endswith(".pdf")]
        pdf_hits  = [(u, e) for u, e in cached if u.lower().endswith(".pdf") or "pdf" in e.get("content_type","")]
        other_hits = [(u, e) for u, e in cached if u not in [x for x,_ in si_hits] and u not in [x for x,_ in pdf_hits]]

        for url, entry in si_hits + pdf_hits + other_hits:
            extracted = _extract_all(url, entry)
            if extracted:
                sources_used.append(url.split("/")[-1][:50])
                for k, v in extracted.items():
                    if k in _FILLABLE and k not in merged and v is not None:
                        merged[k] = v

        # Apply to driver — only fill missing / null fields
        filled_here: list[str] = []
        for field, val in merged.items():
            if drv.get(field) is None:
                drv[field] = val
                filled_here.append(field)
                total_filled += 1

        # Also handle prices — append if not already present
        if "price_eur" in merged and not any(
            p.get("currency") == "EUR" for p in drv.get("prices", [])
        ):
            drv.setdefault("prices", []).append({
                "source": "soundimports", "currency": "EUR",
                "price": merged["price_eur"],
            })

        # Report — use role-appropriate critical set
        crit = _CRITICAL_BY_ROLE.get(role, _CRITICAL)
        missing_critical = [f for f in sorted(crit) if drv.get(f) is None]
        status_tag = "OK" if not missing_critical else f"MISSING: {', '.join(missing_critical)}"
        line = (f"[{role:4s}] {did[:55]:<55}  "
                f"filled={len(filled_here):2d}  {status_tag}")
        if filled_here:
            line += f"\n         <- {', '.join(filled_here)}"
            if sources_used:
                line += f"\n         src: {sources_used[0]}"
        report_lines.append(line)

    # Summary
    roles_missing: dict[str, list[tuple[str, list[str]]]] = {}
    fully_covered = 0
    for drv in drivers:
        r = drv.get("role", "?")
        crit = _CRITICAL_BY_ROLE.get(r, _CRITICAL)
        missing = [f for f in sorted(crit) if drv.get(f) is None]
        if missing:
            roles_missing.setdefault(r, []).append((drv.get("id","?"), missing))
        else:
            fully_covered += 1

    summary = [
        f"\n{'='*70}",
        f"Total fields filled: {total_filled}",
        f"Drivers with all role-critical fields: {fully_covered} / {len(drivers)}",
        "",
        "Still missing role-critical fields:",
    ]
    for role, items in sorted(roles_missing.items()):
        summary.append(f"  {role}: {len(items)} drivers")
        for did, missing in items[:8]:
            summary.append(f"    - {did[:50]}  [{', '.join(missing)}]")
        if len(items) > 8:
            summary.append(f"    ... and {len(items)-8} more")

    full_report = "\n".join(report_lines + summary)
    print(full_report)

    RPT_PATH.write_text(full_report, encoding="utf-8")
    print(f"\nReport -> {RPT_PATH}")

    if not args.dry_run:
        dj["generated"] = "2026-06-16"
        dj["driver_count"] = len(drivers)
        OUT_PATH.write_text(
            json.dumps(dj, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        print(f"Merged -> {OUT_PATH}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true",
                    help="Print report but do not write drivers_merged.json")
    run(ap.parse_args())


if __name__ == "__main__":
    main()

"""Build drivers.json from drivers.md and vendor index files.

Usage: python scripts/build_drivers_json.py
Output: drivers.json in the project root.
"""

import json
import re
import os
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ---------------------------------------------------------------------------
# Step 1: build a model→role lookup from the index files
# ---------------------------------------------------------------------------

INDEX_ROLE = {
    "research/si_tweeter_index.md": "high",
    "research/willys_tweeter_index.md": "high",
    "research/hfc_tweeter_index.md": "high",
    "research/lautsprechershop_tweeter_index.md": "high",
    "research/si_woofer_index.md": "mid",
    "research/willys_woofer_index.md": "mid",
    "research/hfc_woofer_index.md": "mid",
    "research/lautsprechershop_woofer_index.md": "mid",
}

# Map normalised model token → role
index_role_map: dict[str, str] = {}

def _norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())

for rel_path, role in INDEX_ROLE.items():
    path = os.path.join(ROOT, rel_path)
    if not os.path.exists(path):
        continue
    with open(path, encoding="utf-8") as f:
        for line in f:
            # Table rows start with |
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.split("|")]
            if len(cells) < 2:
                continue
            model_cell = cells[1].strip("* ").strip()
            if model_cell and model_cell.lower() not in ("model", "---", ""):
                # strip markdown bold/italic
                model_cell = re.sub(r"\*+", "", model_cell).strip()
                index_role_map[_norm(model_cell)] = role


# ---------------------------------------------------------------------------
# Step 2: parse drivers.md
# ---------------------------------------------------------------------------

SECTION_ROLE = {
    "Subwoofer": "sub",
    "Passive Radiator": "pr",
    "Tweeters": "high",
    "Midranges": "mid",
    "June 2026 Mass Index — Tweeters": "high",
    "June 2026 Mass Index — Woofers & Midranges": "mid",
    "Hard-Excluded Drivers": None,
    "Out-of-Stock / Deferred": None,
    "Eliminated on Specification": None,
}

def _flt(s: str) -> float | None:
    try:
        return float(s.replace(",", ""))
    except (ValueError, AttributeError):
        return None

def _int(s: str) -> int | None:
    v = _flt(s)
    return int(v) if v is not None else None


def extract_float(pattern: str, text: str) -> float | None:
    m = re.search(pattern, text, re.IGNORECASE)
    return _flt(m.group(1)) if m else None


def extract_int(pattern: str, text: str) -> int | None:
    v = extract_float(pattern, text)
    return int(v) if v is not None else None


def parse_heading(heading: str) -> tuple[str, str, str]:
    """Return (brand, model, raw_status_tag) from a ### heading line."""
    heading = re.sub(r"^###\s*", "", heading).strip()
    # Remove ★ markers
    heading = re.sub(r"[★✓]", "", heading).strip()
    # Strip everything after ' — ' (the status/description suffix)
    base = re.split(r"\s+[—–-]\s+", heading)[0].strip()

    # Try to split brand from model: model is usually the last token that
    # contains digits or a slash, or is all-uppercase.
    # Heuristic: last word-group that looks like a part number.
    tokens = base.split()
    model_start = len(tokens)
    for i, t in enumerate(tokens):
        if re.search(r"[0-9/]", t) or t.isupper():
            model_start = i
            break
    brand = " ".join(tokens[:model_start]).strip()
    model = " ".join(tokens[model_start:]).strip()
    if not brand:
        brand = model
        model = base

    # Status tag from suffix
    status_tag = heading  # full heading for status detection
    return brand, model, status_tag


def detect_status(heading_full: str, section: str | None) -> str:
    h = heading_full.upper()
    if "LOCKED" in h:
        return "locked"
    if any(x in h for x in ("REJECTED", "HARD EXCLUDED", "HARD-EXCLUDED", "EXCLUDED")):
        return "rejected"
    if "OUT OF STOCK" in h or " OOS" in h:
        return "oos"
    if "CANDIDATE" in h or "★" in h:
        return "candidate"
    if "CATALOGUE" in h:
        return "catalogue"
    if section in ("Hard-Excluded Drivers", "Eliminated on Specification"):
        return "rejected"
    if section == "Out-of-Stock / Deferred":
        return "oos"
    return "catalogue"


def make_id(brand: str, model: str) -> str:
    raw = f"{brand}-{model}".lower()
    raw = re.sub(r"[^a-z0-9]+", "-", raw)
    return raw.strip("-")


def parse_prices(text: str) -> list[dict]:
    prices = []
    source_map = {
        "soundimports": "soundimports",
        "si ": "soundimports",
        "si price": "soundimports",
        "willys": "willys",
        "hfc": "hfc",
        "hifi collective": "hfc",
        "falcon": "falcon",
        "lss": "lss",
        "lautsprechershop": "lss",
        "audiophonics": "audiophonics",
        "parts express": "parts-express",
    }
    # Match lines like: SoundImports price: €44.95
    for m in re.finditer(
        r"(soundimports|willys[- ]hifi|willys|hfc|hifi collective|falcon(?: acoustics)?|lss|lautsprechershop|audiophonics|si)\s*(?:price|:)[:\s]*([€£])([0-9]+(?:\.[0-9]+)?)",
        text, re.IGNORECASE
    ):
        src_raw = m.group(1).lower()
        currency = "EUR" if m.group(2) == "€" else "GBP"
        price = float(m.group(3))
        src = next((v for k, v in source_map.items() if src_raw.startswith(k)), src_raw)
        prices.append({"source": src, "currency": currency, "price": price})

    # Also catch inline like: £29.90 (Falcon)
    for m in re.finditer(
        r"([€£])([0-9]+(?:\.[0-9]+)?)\s*\(([^)]+)\)",
        text, re.IGNORECASE
    ):
        src_raw = m.group(3).lower().split()[0]
        currency = "EUR" if m.group(1) == "€" else "GBP"
        price = float(m.group(2))
        src = next((v for k, v in source_map.items() if src_raw.startswith(k.strip())), src_raw)
        # Don't duplicate
        if not any(p["source"] == src and p["price"] == price for p in prices):
            prices.append({"source": src, "currency": currency, "price": price})

    return prices


def parse_datasheets(text: str) -> list[dict]:
    sheets = []
    # Local paths
    locals_ = re.findall(r"research/[^\s\]\"']+\.pdf", text)
    urls_ = re.findall(r"https?://[^\s\]\"'>]+\.pdf[^\s\]\"']*", text)
    for i, local in enumerate(locals_):
        entry: dict = {"local": local}
        if i < len(urls_):
            entry["url"] = urls_[i]
        sheets.append(entry)
    if not locals_ and urls_:
        for url in urls_:
            sheets.append({"url": url})
    return sheets


def build_driver(heading: str, body_lines: list[str], section: str | None) -> dict | None:
    brand, model, heading_full = parse_heading(heading)
    if not model:
        return None

    text = "\n".join(body_lines)

    d: dict = {}
    d["id"] = make_id(brand, model)
    d["brand"] = brand or "Unknown"
    d["model"] = model

    # --- Role ---
    # 1. From explicit Role: tag in body
    role_m = re.search(r"Role:\s*\**(SUB|PR|MID|HIGH|EXCL)\**", text, re.IGNORECASE)
    if role_m:
        d["role"] = role_m.group(1).lower()
    else:
        # 2. From section
        sec_role = SECTION_ROLE.get(section or "", None)
        if sec_role:
            d["role"] = sec_role
        else:
            # 3. From index files
            idx_role = index_role_map.get(_norm(model))
            if idx_role:
                d["role"] = idx_role
            else:
                d["role"] = "unknown"

    d["status"] = detect_status(heading_full, section)

    # --- Driver type ---
    type_m = re.search(r"Type:\s*\**([^|\n\*]+)", text, re.IGNORECASE)
    if type_m:
        d["driver_type"] = type_m.group(1).strip().strip("*").strip()

    # --- Physical ---
    size_m = re.search(r'(?:Size|Nominal Diameter)[:\s]+\**([0-9.]+)"', text, re.IGNORECASE)
    if size_m:
        d["nominal_size_inch"] = _flt(size_m.group(1))

    # Frame OD — tweeters use "Faceplate OD", mids use "Frame OD"
    fp_m = (re.search(r"(?:Frame OD|Faceplate OD|FP OD)[:\s]+\**([0-9.]+)\s*mm", text, re.IGNORECASE)
            or re.search(r"FP[=:\s]+\**([0-9.]+)\s*mm", text, re.IGNORECASE))
    if fp_m:
        d["frame_od_mm"] = _flt(fp_m.group(1))

    shape_m = re.search(r"Frame[:\s|]+\**([a-z]+)\**\s*(?:steel|alumin|frame|$|\|)", text, re.IGNORECASE)
    if shape_m and shape_m.group(1).lower() in ("round", "square", "oval"):
        d["frame_shape"] = shape_m.group(1).lower()

    imp_m = (re.search(r"Impedance[:\s]+\**([0-9.]+)\s*[ΩΩ]", text)
             or re.search(r"Imp[:\s]+\**([0-9.]+)\s*[ΩΩ]", text))
    if imp_m:
        d["impedance_ohm"] = _flt(imp_m.group(1))

    cutout_m = re.search(r"(?:Cutout|Baffle Cutout)[:\s]+\**([0-9.]+)\s*mm", text, re.IGNORECASE)
    if cutout_m:
        d["cutout_mm"] = _flt(cutout_m.group(1))

    depth_m = re.search(r"Depth[:\s]+\**([0-9.]+)\s*mm", text, re.IGNORECASE)
    if depth_m:
        d["depth_mm"] = _flt(depth_m.group(1))

    holes_m = re.search(r"([0-9]+)\s*mounting holes", text, re.IGNORECASE)
    if holes_m:
        d["mounting_holes"] = _int(holes_m.group(1))

    # --- Acoustic ---
    sens_m = re.search(r"Sensitivity[:\s]+\**([0-9.]+)\s*dB", text, re.IGNORECASE)
    if sens_m:
        d["sensitivity_db"] = _flt(sens_m.group(1))

    pwr_m = re.search(r"Power[:\s]+\**([0-9.]+)\s*W\s*RMS", text, re.IGNORECASE)
    if pwr_m:
        d["power_rms_w"] = _flt(pwr_m.group(1))

    pmax_m = re.search(r"(?:Power[:\s]+[^|\n]*?/\s*\**([0-9.]+)\s*W\s*(?:peak|max))", text, re.IGNORECASE)
    if pmax_m:
        d["power_max_w"] = _flt(pmax_m.group(1))

    freq_m = re.search(r"[Ff]req(?:uency)?[^:\n]*[:\s]+\**([0-9]+)\s*[–\-]\s*([0-9,]+)\s*[Hk]", text)
    if freq_m:
        d["freq_low_hz"] = _int(freq_m.group(1))
        d["freq_high_hz"] = _int(freq_m.group(2).replace(",", ""))

    # --- T/S ---
    for key, pat in [
        ("fs_hz",     r"Fs[:\s]+\**([0-9.]+)\s*Hz"),
        ("qts",       r"Qts[:\s]+\**([0-9.]+)"),
        ("qes",       r"Qes[:\s]+\**([0-9.]+)"),
        ("qms",       r"Qms[:\s]+\**([0-9.]+)"),
        ("xmax_mm",   r"Xmax[:\s]+\**([0-9.]+)\s*mm"),
        ("sd_cm2",    r"Sd[:\s]+\**([0-9.]+)\s*cm"),
        ("vd_cm3",    r"Vd[:\s]+\**([0-9.]+)\s*cm"),
        ("vas_l",     r"Vas[:\s]+\**([0-9.]+)\s*[Ll]"),
        ("bl_tm",     r"BL[:\s]+\**([0-9.]+)\s*Tm"),
        ("re_ohm",    r"Re[:\s]+\**([0-9.]+)\s*[ΩΩ]"),
        ("le_mh",     r"Le[:\s]+\**([0-9.]+)\s*mH"),
        ("mms_g",     r"Mms[:\s]+\**([0-9.]+)\s*g"),
        ("cms_mm_n",  r"Cms[:\s]+\**([0-9.]+)\s*mm"),
        ("vc_mm",     r"\bVC[:\s]+\**([0-9.]+)\s*mm"),
    ]:
        v = extract_float(pat, text)
        if v is not None:
            d[key] = v

    # --- Derived ---
    beam_m = re.search(r"beaming starts[^0-9]*([0-9,]+)\s*Hz", text, re.IGNORECASE)
    if beam_m:
        d["beaming_limit_hz"] = _int(beam_m.group(1).replace(",", ""))

    xover_m = re.search(r"2[×x]\s*=\s*([0-9]+)\s*Hz", text, re.IGNORECASE)
    if xover_m:
        d["min_xover_hz"] = _int(xover_m.group(1))

    # --- Materials ---
    if re.search(r"[Nn]eodymium|Neo-Balanced", text):
        d["magnet"] = "neodymium"
    elif re.search(r"[Ff]errite", text):
        d["magnet"] = "ferrite"

    cone_m = re.search(r"Cone[:\s]+\**([^|\n\*]+)", text, re.IGNORECASE)
    if cone_m:
        cone_text = cone_m.group(1).strip().lower()
        if "alumin" in cone_text:
            d["cone_material"] = "aluminium"
        elif "paper" in cone_text or "fiber" in cone_text or "fibre" in cone_text:
            d["cone_material"] = "paper"
        elif "carbon" in cone_text:
            d["cone_material"] = "carbon"
        elif "ceramic" in cone_text:
            d["cone_material"] = "ceramic"
        elif "polyprop" in cone_text or "pp" in cone_text:
            d["cone_material"] = "polypropylene"

    if re.search(r"[Rr]ubber surround", text):
        d["surround_material"] = "rubber"
    elif re.search(r"[Ss]ilicone surround", text):
        d["surround_material"] = "silicone"

    # --- Prices & datasheets ---
    prices = parse_prices(text)
    if prices:
        d["prices"] = prices

    sheets = parse_datasheets(text)
    if sheets:
        d["datasheets"] = sheets

    return d


def parse_drivers_md() -> list[dict]:
    path = os.path.join(ROOT, "drivers.md")
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()

    drivers = []
    current_section: str | None = None
    current_heading: str | None = None
    current_body: list[str] = []

    def flush():
        if current_heading:
            d = build_driver(current_heading, current_body, current_section)
            if d:
                drivers.append(d)

    for line in lines:
        line_s = line.rstrip("\n")
        if line_s.startswith("## "):
            flush()
            current_heading = None
            current_body = []
            current_section = line_s[3:].strip()
        elif line_s.startswith("### "):
            flush()
            current_heading = line_s
            current_body = []
        elif current_heading is not None:
            current_body.append(line_s)

    flush()
    return drivers


# ---------------------------------------------------------------------------
# Step 3: assemble and write
# ---------------------------------------------------------------------------

ROLE_ORDER = {"sub": 0, "pr": 1, "mid": 2, "high": 3, "unknown": 4}

def main():
    drivers = parse_drivers_md()

    # Sort: role order, then brand, then model
    drivers.sort(key=lambda d: (
        ROLE_ORDER.get(d.get("role", "unknown"), 99),
        d.get("brand", ""),
        d.get("model", ""),
    ))

    out = {
        "generated": str(date.today()),
        "driver_count": len(drivers),
        "drivers": drivers,
    }

    out_path = os.path.join(ROOT, "drivers.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Written {len(drivers)} drivers to {out_path}")

    # Print role summary
    from collections import Counter
    roles = Counter(d.get("role", "unknown") for d in drivers)
    for role, count in sorted(roles.items()):
        print(f"  {role}: {count}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Cross-check every numeric value in drivers.md against drivers.json.
Ensures all data in MD is present and accurate in JSON.
"""
import json, re, sys
from pathlib import Path

ROOT = Path(r"C:\Users\johnl\work\speaker")
JSON_PATH = ROOT / "drivers.json"
MD_PATH   = ROOT / "drivers.md"

# ── helpers ──────────────────────────────────────────────────────────────────

def norm(s):
    return re.sub(r'[\s\-/\._×★()]', '', s.upper())

def strip_md(s):
    return re.sub(r'\*{1,2}', '', s)

def to_float(raw):
    try:
        return float(raw.replace(',', ''))
    except (ValueError, AttributeError):
        return None

def find_val(pattern, text, group=1):
    m = re.search(pattern, text, re.IGNORECASE)
    if m:
        return to_float(strip_md(m.group(group)))
    return None

# ── field extraction from an MD block ────────────────────────────────────────

# (json_key, tolerance, regex)
FIELDS = [
    ("sensitivity_db",  0.15, r'Sensitivity[:\s]+\*{0,2}([\d.,]+)\s*dB'),
    ("power_rms_w",     0.5,  r'Power[:\s]+\*{0,2}([\d.,]+)\s*W\s*RMS'),
    ("power_max_w",     0.5,  r'Power[:\s]+[\d.,\*\s]+W\s*RMS\s*/\s*\*{0,2}([\d.,]+)\s*W'),
    ("fs_hz",           0.6,  r'\bFs[:\s]+\*{0,2}([\d.,]+)\s*Hz'),
    ("impedance_ohm",   0.05, r'Impedance[:\s]+\*{0,2}([\d.]+)\s*[ΩO]'),
    ("frame_od_mm",     0.5,  r'(?:Frame OD|Faceplate OD)[:\s]+\*{0,2}([\d.]+)\s*mm'),
    ("cutout_mm",       0.5,  r'Cutout[:\s]+\*{0,2}([\d.]+)\s*mm'),
    ("depth_mm",        0.5,  r'Depth[:\s]+\*{0,2}([\d.]+)\s*mm'),
    ("sd_cm2",          0.5,  r'\bSd[:\s≈]+\*{0,2}([\d.]+)\s*cm[²2]'),
    ("xmax_mm",         0.06, r'\bXmax[:\s]+±?\*{0,2}([\d.]+)\s*mm'),
    ("qts",             0.005,r'\bQts[:\s]+\*{0,2}([\d.]+)'),
    ("qes",             0.005,r'\bQes[:\s]+\*{0,2}([\d.]+)'),
    ("qms",             0.01, r'\bQms[:\s]+\*{0,2}([\d.]+)'),
    ("re_ohm",          0.05, r'\bRe[:\s]+\*{0,2}([\d.]+)\s*[ΩO]'),
    ("le_mh",           0.005,r'\bLe[:\s1kKhHz\s]+\*{0,2}([\d.]+)\s*mH'),
    ("mms_g",           0.05, r'\bMms[:\s]+\*{0,2}([\d.]+)\s*g'),
    ("cms_mm_n",        0.01, r'\bCms[:\s]+\*{0,2}([\d.]+)\s*mm/N'),
    ("bl_tm",           0.05, r'\b(?:BL?|Bl)[:\s]+\*{0,2}([\d.]+)\s*(?:Tm|N/A)'),
    ("vas_l",           0.01, r'\bVas[:\s]+\*{0,2}([\d.]+)\s*L'),
]

FREQ_RE = re.compile(
    r'Frequency\s+(?:range|response)[:\s]+([\d,]+)\s*[–\-]\s*([\d,]+)\s*Hz',
    re.IGNORECASE
)

def extract_md_fields(block):
    result = {}
    for json_key, _, pat in FIELDS:
        if json_key not in result:
            v = find_val(pat, block)
            if v is not None:
                result[json_key] = v
    m = FREQ_RE.search(block)
    if m:
        lo = to_float(m.group(1))
        hi = to_float(m.group(2))
        if lo: result["freq_low_hz"]  = lo
        if hi: result["freq_high_hz"] = hi
    return result

# ── parse drivers.md ─────────────────────────────────────────────────────────

md_text = MD_PATH.read_text(encoding='utf-8')
HEADING = re.compile(r'^### (.+?)(?:\s+—|\s+\*{2})', re.MULTILINE)

md_drivers = {}   # norm_key → {name, fields}
headings = list(HEADING.finditer(md_text))
for i, m in enumerate(headings):
    name  = m.group(1).strip()
    start = m.end()
    end   = headings[i+1].start() if i+1 < len(headings) else len(md_text)
    block = md_text[start:end]
    key   = norm(name.split('(')[0].strip())
    fields = extract_md_fields(block)
    if key not in md_drivers:
        md_drivers[key] = {'name': name, 'fields': fields, 'block_key': key}

# ── load & merge drivers.json ─────────────────────────────────────────────────

with open(JSON_PATH, encoding='utf-8') as f:
    raw = json.load(f)

# Merge duplicate IDs (union of all fields, last non-None value wins per field)
json_by_id = {}
for d in raw['drivers']:
    did = d['id']
    if did not in json_by_id:
        json_by_id[did] = dict(d)
    else:
        for k, v in d.items():
            if v is not None:
                json_by_id[did][k] = v

# Build lookup: normalised model → entry AND normalised brand+model → entry
json_by_model     = {}   # model-name only
json_by_brandmodel = {}  # brand+model combined

for d in json_by_id.values():
    mk = norm(d.get('model', ''))
    bk = norm(d.get('brand', '') + d.get('model', ''))
    # Avoid polluting with the doubled entries (model contains itself twice)
    brand_norm = norm(d.get('brand', ''))
    if mk.startswith(brand_norm) and mk[len(brand_norm):] == brand_norm:
        # Doubled — skip
        pass
    if mk and mk not in json_by_model:
        json_by_model[mk] = d
    if bk and bk not in json_by_brandmodel:
        json_by_brandmodel[bk] = d

def find_json(md_key, md_name):
    # Exact model-only match
    if md_key in json_by_model:
        return json_by_model[md_key]
    # Exact brand+model match
    if md_key in json_by_brandmodel:
        return json_by_brandmodel[md_key]
    # Substring: md_key contains or is contained in a JSON key
    best = None
    for jk, jd in json_by_model.items():
        if md_key in jk or jk in md_key:
            if best is None or len(jk) > len(best[0]):
                best = (jk, jd)
    for jk, jd in json_by_brandmodel.items():
        if md_key in jk or jk in md_key:
            if best is None or len(jk) > len(best[0]):
                best = (jk, jd)
    return best[1] if best else None

# ── compare ───────────────────────────────────────────────────────────────────

tol_map = {json_key: tol for json_key, tol, _ in FIELDS}
tol_map.update({"freq_low_hz": 1.0, "freq_high_hz": 1.0})

mismatches   = []
missing_fld  = []
not_matched  = []
json_orphans = []   # JSON entries with no MD counterpart

# Build set of JSON IDs that were successfully matched from MD side
matched_json_ids = set()

for md_key, entry in sorted(md_drivers.items()):
    name   = entry['name']
    fields = entry['fields']

    j = find_json(md_key, name)
    if j is None:
        not_matched.append(name)
        continue

    matched_json_ids.add(j['id'])

    if not fields:
        continue   # matched but no numeric specs to compare (excluded/sparse entries)

    for jfield, md_val in fields.items():
        j_val = j.get(jfield)
        tol   = tol_map.get(jfield, 0.5)
        if j_val is None:
            missing_fld.append({'driver': name, 'field': jfield, 'md_val': md_val,
                                 'json_id': j.get('id', '?')})
        elif abs(md_val - j_val) > tol:
            mismatches.append({'driver': name, 'field': jfield,
                                'md': md_val, 'json': j_val,
                                'json_id': j.get('id', '?')})

# ── reverse check: JSON entries with no MD match ─────────────────────────────
for did, d in json_by_id.items():
    if did not in matched_json_ids:
        json_orphans.append((did, d.get('brand',''), d.get('model','')))

# ── report ────────────────────────────────────────────────────────────────────

print("drivers.md parsed:   %d entries" % len(md_drivers))
print("drivers.json merged: %d unique IDs\n" % len(json_by_id))

if not_matched:
    print("=== MD ENTRIES WITH NO JSON MATCH ===")
    for n in not_matched:
        print("  " + n)
    print()

if mismatches:
    print("=== VALUE MISMATCHES (md_val -> json_val) ===")
    for m in sorted(mismatches, key=lambda x: x['driver']):
        print("  [%s]  %s" % (m['json_id'], m['driver']))
        print("    %-18s md=%-10s json=%-10s delta=%+.3f" % (
            m['field'], m['md'], m['json'], m['md'] - m['json']))
    print()

if missing_fld:
    print("=== FIELDS IN MD MISSING FROM JSON ===")
    prev = None
    for m in sorted(missing_fld, key=lambda x: (x['driver'], x['field'])):
        if m['driver'] != prev:
            print("  [%s]  %s" % (m['json_id'], m['driver']))
            prev = m['driver']
        print("    %-18s md=%s" % (m['field'], m['md_val']))
    print()

if json_orphans:
    print("=== JSON ENTRIES WITH NO MD COUNTERPART ===")
    for did, brand, model in sorted(json_orphans):
        print("  [%s]  %s %s" % (did, brand, model))
    print()

if not mismatches and not missing_fld and not not_matched and not json_orphans:
    print("Perfect 1:1 correlation - MD and JSON are fully in sync.")

#!/usr/bin/env python3
"""
Patch drivers.json to match drivers.md: fix mismatches and add missing fields.
All corrections derived from check_drivers.py output; sources are datasheets in
drivers.md (authoritative) vs potentially-stale JSON values.
"""
import json
from pathlib import Path

JSON_PATH = Path(r"C:\Users\johnl\work\speaker\drivers.json")

with open(JSON_PATH, encoding='utf-8') as f:
    data = json.load(f)

# ── Patch table ─────────────────────────────────────────────────────────────
# (id_prefix, field, value, note)
# id_prefix: match any entry whose id starts with or equals this
PATCHES = [
    # === MISMATCHES (json is wrong vs MD/datasheet) ===
    # ND25FW-4: SoundImports states 2500-20000Hz; JSON has corrupt 4/5
    ("dayton-audio-nd25fw-4",       "freq_low_hz",  2500, "SI page / Dayton datasheet"),
    ("dayton-audio-nd25fw-4",       "freq_high_hz", 20000,"SI page / Dayton datasheet"),
    # SB29RDAC: SB Acoustics datasheet (research/sb_acoustics_sb29rdac-c000-4.pdf) says 600Hz
    # JSON had 900Hz from SoundImports product page — datasheet is authoritative
    ("sb-acoustics-sb29rdac",       "fs_hz",        600,  "SB Acoustics datasheet (600Hz); SI page incorrect at 900Hz"),

    # === MISSING FIELDS (add to JSON) ===
    # Celestion TF0510: Sd from geometry (cutout 117mm - 2x8.5mm surround = 100mm dia)
    ("celestion-tf0510",            "sd_cm2",       78.5, "derived from geometry (cutout 117mm, pi*50^2 = 78.54cm2)"),
    # CF18N-4: freq range from SoundImports product page
    ("dayton-audio-cf18n-4",        "freq_low_hz",  2500, "SI product page"),
    ("dayton-audio-cf18n-4",        "freq_high_hz", 20000,"SI product page"),
    # DC25T-8: Fs from drivers.md sourced datasheet
    ("dayton-audio-dc25t-8",        "fs_hz",        1468, "drivers.md / datasheet"),
    # DSA90-8: Xmax from Parts Express spec sheet
    ("dayton-audio-dsa90-8",        "xmax_mm",      2.5,  "Parts Express spec sheet"),
    # ND20FA-6: freq range from SoundImports page (Fs 2005 Hz => usable from ~2000Hz)
    ("dayton-audio-nd20fa-6",       "freq_low_hz",  2000, "drivers.md / SI page"),
    ("dayton-audio-nd20fa-6",       "freq_high_hz", 20000,"drivers.md / SI page"),
    # ND25FN-4: Fs from drivers.md / Dayton datasheet
    ("dayton-audio-nd25fn-4",       "fs_hz",        1350, "drivers.md / Dayton datasheet"),
    # RS100-8: Xmax from SoundImports
    ("dayton-audio-rs100-8",        "xmax_mm",      3.5,  "drivers.md / SI page"),
    # RST28F-4: freq range from SI page
    ("dayton-audio-rst28f-4",       "freq_low_hz",  1400, "drivers.md / SI page"),
    ("dayton-audio-rst28f-4",       "freq_high_hz", 20000,"drivers.md / SI page"),
    # TCP115-8: Xmax from SI / Dayton datasheet
    ("dayton-audio-tcp115-8",       "xmax_mm",      4.0,  "drivers.md / Dayton datasheet"),
    # HiVi B4N: BL from HiVi CLIO lab measurement datasheet (pdf_hiVi_B4N_2)
    ("hivi-swan-b4n",               "bl_tm",        6.22, "HiVi CLIO datasheet (pdf_hiVi_B4N_2.pdf)"),
    # HiVi TN25: freq range from SI product page
    ("hivi-tn25",                   "freq_low_hz",  2500, "SI product page"),
    ("hivi-tn25",                   "freq_high_hz", 22000,"SI product page"),
    # Monacor DT-25N: freq range from SI product page
    ("monacor-dt-25n",              "freq_low_hz",  1600, "SI product page"),
    ("monacor-dt-25n",              "freq_high_hz", 20000,"SI product page"),
    # Morel MDT12: from drivers.md / datasheet
    ("morel-mdt12",                 "fs_hz",        1000, "drivers.md / Morel datasheet"),
    ("morel-mdt12",                 "freq_low_hz",  1800, "drivers.md / SI page"),
    ("morel-mdt12",                 "freq_high_hz", 25000,"drivers.md / Morel datasheet"),
    # SB15SFCR-00 racetrack PR: Sd from SoundImports
    ("sb-acoustics-sb15sfcr",       "sd_cm2",       178,  "drivers.md / SI page"),
    # SEAS 27TFFNC: Fs from SI product page
    ("seas-prestige-27tffnc",       "fs_hz",        1170, "drivers.md / SI product page"),
]

changes = 0
for d in data['drivers']:
    did = d['id']
    for id_prefix, field, value, note in PATCHES:
        if did.startswith(id_prefix):
            old = d.get(field)
            if old != value:
                d[field] = value
                status = "FIXED  " if old is not None else "ADDED  "
                print("%s [%s] %s: %s -> %s  (%s)" % (
                    status, did, field, old, value, note))
                changes += 1

print("\n%d changes applied." % changes)

with open(JSON_PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print("drivers.json written.")

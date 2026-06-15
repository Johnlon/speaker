#!/usr/bin/env python3
"""Scratch pad — reuse for one-off JSON/MD investigations."""
import json, re
from pathlib import Path

ROOT = Path(r"C:\Users\johnl\work\speaker")

with open(ROOT / "drivers.json", encoding="utf-8") as f:
    data = json.load(f)

by_id = {}
for d in data["drivers"]:
    did = d["id"]
    if did not in by_id or len(d) > len(by_id[did]):
        by_id[did] = d

# ── investigation code here ──────────────────────────────────────────────────

for did, d in by_id.items():
    if "nd25" in did:
        print(did, d.get("fs_hz"), d.get("freq_low_hz"), d.get("freq_high_hz"))

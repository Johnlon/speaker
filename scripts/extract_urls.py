#!/usr/bin/env python3
"""
extract_urls.py — Scan all project files and emit a flat, deduplicated URL list.

Sources:
  - drivers.json  (prices[].url, datasheets[].url)
  - drivers.md    (every line containing a URL)
  - research/*_index.md  (all markdown links and bare URLs)
  - CONSTRUCTED: SI product-page and loudspeakerdatabase.com URLs derived from
    every brand+model entry in drivers.json (404s will be silently skipped by
    download_cache.py; they're cheap to attempt at 50-worker parallelism)

Output: research/source_urls.md  (one URL per line; comment lines start with #)

Run before download_cache.py whenever new drivers are added to drivers.json.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
RESEARCH = ROOT / "research"
OUT = RESEARCH / "source_urls.md"

_MD_LINK = re.compile(r"\[(?:[^\]]*)\]\((https?://[^\)\s]+)\)")
_RAW_URL = re.compile(r"https?://[^\s\)\]\"'<>,]+")


def _urls_in_text(text: str) -> list[str]:
    found = []
    for m in _MD_LINK.finditer(text):
        found.append(m.group(1).rstrip("."))
    for m in _RAW_URL.finditer(text):
        u = m.group(0).rstrip(".,;)")
        if u not in found:
            found.append(u)
    return found


# ---------------------------------------------------------------------------
# Brand → SoundImports URL slug mapping
# ---------------------------------------------------------------------------

_SI_BRAND_SLUG = {
    "dayton":        "dayton-audio",
    "sbacoustics":   "sb-acoustics",
    "seas":          "seas",
    "scanspeak":     "scan-speak",
    "peerless":      "peerless-by-tymphany",
    "visaton":       "visaton",
    "beyma":         "beyma",
    "morel":         "morel",
    "sica":          "sica",
    "markaudio":     "markaudio",
    "hivi":          "hivi",
    "tangband":      "tang-band",
    "tectonic":      "tectonic",
    "faital":        "faitalpro",
    "wavecor":       "wavecor",
    "celestion":     "celestion",
    "audaphon":      "audaphon",
    "monacor":       "monacor",
    "fountek":       "fountek",
}

_LDB_BRAND = {
    "dayton":        "Dayton",
    "sbacoustics":   "SB-Acoustics",
    "seas":          "SEAS",
    "scanspeak":     "Scan-Speak",
    "peerless":      "Peerless",
    "visaton":       "Visaton",
    "beyma":         "Beyma",
    "morel":         "Morel",
    "sica":          "SICA",
    "markaudio":     "Markaudio",
    "hivi":          "HiVi",
    "tangband":      "Tang-Band",
    "tectonic":      "Tectonic",
    "faital":        "FaitalPRO",
    "wavecor":       "Wavecor",
    "celestion":     "Celestion",
    "monacor":       "Monacor",
}


def _norm_brand(raw: str) -> str:
    r = raw.lower().strip()
    mapping = {
        "dayton audio": "dayton",
        "sb acoustics": "sbacoustics",
        "scan-speak": "scanspeak",
        "peerless by tymphany": "peerless",
        "hivi swans": "hivi",
        "tang band": "tangband",
        "faitalpro": "faital",
    }
    return mapping.get(r, re.sub(r"[^a-z0-9]", "", r))


def _model_slug(model: str) -> str:
    s = model.lower().replace(" ", "-").replace("/", "-")
    s = re.sub(r"[^a-z0-9\-]", "", s)
    return re.sub(r"-+", "-", s).strip("-")


def construct_si_url(brand_norm: str, model: str) -> str | None:
    bs = _SI_BRAND_SLUG.get(brand_norm)
    if not bs:
        return None
    return f"https://www.soundimports.eu/en/{bs}-{_model_slug(model)}.html"


def construct_ldb_url(brand_norm: str, model: str) -> str | None:
    lb = _LDB_BRAND.get(brand_norm)
    if not lb:
        return None
    # LDB URL: /Brand/Model  (model mostly as-is, spaces to underscores)
    m = model.replace(" ", "_")
    return f"https://loudspeakerdatabase.com/{lb}/{m}"


# ---------------------------------------------------------------------------
# Extractors
# ---------------------------------------------------------------------------

def from_drivers_json() -> list[tuple[str, str]]:
    path = ROOT / "drivers.json"
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    results = []
    for d in data.get("drivers", []):
        did = d.get("id", "?")
        for p in d.get("prices", []):
            u = p.get("url")
            if u:
                results.append((f"drivers.json/{did}/prices", u))
        for ds in d.get("datasheets", []):
            u = ds.get("url")
            if u:
                results.append((f"drivers.json/{did}/datasheets", u))
    return results


def from_drivers_md() -> list[tuple[str, str]]:
    path = ROOT / "drivers.md"
    if not path.exists():
        return []
    results = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        for u in _urls_in_text(line):
            lbl = "drivers.md/Source" if ("Source:" in line or "**Source:**" in line) else "drivers.md"
            results.append((lbl, u))
    return results


def from_index_files() -> list[tuple[str, str]]:
    results = []
    for f in sorted(RESEARCH.glob("*_index.md")):
        text = f.read_text(encoding="utf-8", errors="replace")
        for u in _urls_in_text(text):
            results.append((f"research/{f.name}", u))
    return results


def from_constructed(existing: set[str]) -> list[tuple[str, str]]:
    """Generate SI + LDB URLs for every driver in drivers.json not already known."""
    path = ROOT / "drivers.json"
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    results = []
    for d in data.get("drivers", []):
        brand_raw = d.get("brand", "")
        model = d.get("model", "")
        if not brand_raw or not model:
            continue
        bn = _norm_brand(brand_raw)

        si = construct_si_url(bn, model)
        if si and si not in existing:
            results.append(("constructed/soundimports", si))

        ldb = construct_ldb_url(bn, model)
        if ldb and ldb not in existing:
            results.append(("constructed/loudspeakerdatabase", ldb))

    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    all_pairs: list[tuple[str, str]] = []
    all_pairs += from_drivers_json()
    all_pairs += from_drivers_md()
    all_pairs += from_index_files()

    seen: set[str] = set()
    by_label: dict[str, list[str]] = {}
    for label, url in all_pairs:
        if url in seen:
            continue
        seen.add(url)
        by_label.setdefault(label, []).append(url)

    # Add constructed URLs for any driver not already covered
    for label, url in from_constructed(seen):
        if url in seen:
            continue
        seen.add(url)
        by_label.setdefault(label, []).append(url)

    lines = [
        "# source_urls.md — generated by scripts/extract_urls.py",
        "# Edit this file to add or remove URLs, then re-run download_cache.py",
        "# Lines starting with # are comments. One URL per non-comment line.",
        "",
    ]
    for label, urls in by_label.items():
        lines.append(f"# {label}")
        lines += urls
        lines.append("")

    total = len(seen)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Written {total} URLs -> {OUT}")

    # Summary breakdown
    from urllib.parse import urlparse
    from collections import Counter
    hosts = Counter(urlparse(u).netloc for u in seen)
    for h, n in sorted(hosts.items(), key=lambda x: -x[1]):
        print(f"  {n:4d}  {h}")


if __name__ == "__main__":
    main()

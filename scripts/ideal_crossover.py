#!/usr/bin/env python3
"""
Compute ideal mid/tweeter crossover for every combo in combos.md.

Ideal = geometric mean of:
  - tweeter floor  = 3 × Fs  (below this THD is objectionable; 2×Fs is hard minimum)
  - mid ceiling    = 0.80 × beaming frequency  (above this off-axis coherence collapses)

If 3×Fs > ceiling but 2×Fs < ceiling: marginal window — use 2×Fs as floor, flag THD concern.
If 2×Fs > ceiling: incompatible — no clean handover exists, flag accordingly.

Updates cols in combos.md:
  - Best_cross (parts[5]): replaces the value with computed ideal
  - Notes (last col): replaces generic quality text with computed assessment
"""

import math
import re

# ── Mid beaming frequencies (Hz) ─────────────────────────────────────────────
# f_beam = 34400 / (π × √(Sd/π));  values confirmed from combos.md beaming table
MID_BEAM: dict[str, int] = {
    "DSA90-8":          3260,
    "DS115-8":          2636,
    "HiVi B4N":         2636,
    "SB12PFCR25-4":     2730, "SB12PFCR":     2730,
    "SB12MNRX2-25-4":   2730, "SB12MNRX2":    2730,
    "SB12NRX25-4":      2730, "SB12NRX":       2730,
    "SB12PACR25-4":     2730, "SB12PACR":      2730,
    "DMA105-8":         2900,
    "SPM-116/8":        2600,
    "Beyma 4FR40":      2600,
    "DA115-8":          2600,
    "TCP115-8":         2570,
    "SIG120-4":         2570,
    "RS125-4":          2184,
    "RS125P-4":         2184, "RS125P":        2184,
    "HiVi M5N":         2185,
    "SB13PFCR25-4":     2080, "SB13PFCR":      2080,
    "SDS-P830656":      2080,
    "SIG150-4":         1990,
    "PA130-8":          2000,  # 5" driver ~85cm² Sd; original combos used 2000 — verify Sd from datasheet
    "SLS-85S25CP04-04": 3000, "SLS-85":        3000,  # 3.3" driver; original combos used 3000 — verify Sd from datasheet
    "ND91-4":           3000,  # 4" Faital-type; original combos used 3000 — verify Sd from datasheet
    "PLUVIA-7HD Gold":  2185, "PLUVIA-7HD":    2185,
    "RS100-8":          2900,  # 4" driver; was wrongly set to 2184 (RS125 value); original combos used 2900 — verify Sd from datasheet
}

# ── Tweeter Fs (Hz) ───────────────────────────────────────────────────────────
# Derived from min_xover / 2 (min_xover = 2×Fs, from Tweeter Minimum Crossover table)
TWEET_FS: dict[str, int] = {
    "R2604/833000":     440,  "R2604/833":     440,
    "XT25TG30-04":      440,  "XT25TG":        440,
    "R2604/832000":     500,  "R2604/832":      500,
    "H1189-06":         550,  "H1189":          550,  "SEAS H1189-06": 550,
    "XT25BG60-04":      570,  "XT25BG":         570,
    "DX25TG59-04":      590,  "DX25TG":         590,
    "SB29SDAC-C000-4":  600,  "SB29SDAC":       600,
    "SB29RDNC-C000-4":  580,  "SB29RDNC":       580,
    "RST28F-4":         710,  "RST28F":          710,
    "D2606/920000":    1100,  "D2606":          1100,
    "NE25VTS-04":       730,  "NE25VTS":         730,
    "NE19VTS-04":       770,  "NE19VTS":         770,
    "SB21SDC-C000-4":   720,  "SB21SDC":         720,
    "SB21RDCN-C000-4":  850,  "SB21RDCN":        850,
    "SB26ST-C000-5":    870,  "SB26ST":          870,
    "SEAS H1406-04":   1170,  "H1406-04":       1170,  "H1406":        1170,
    "CF18N-4":         1100,  "CF18N":           1100,
    "TD25F-4":          900,  "TD25F":            900,
    "DA25BG08-06":      710,  "DA25BG":           710,
    "XT25SC90-04":      825,  "XT25SC90":         825,
    "XT19TD00-04":      820,  "XT19TD":           820,
    "SB19ST-C000-4":    980,  "SB19ST":           980,
    "SB26STCN-C000-4":  950,  "SB26STCN":         950,
    "DT-28N":          1200,  "DT28N":            1200,
    "HiVi TN28-B":     1300,  "TN28B":            1300,
    "ND25FA-4":        1350,  "ND25FA":            1350,
    "HiVi TN25":       1500,  "TN25":              1500,
    "XT25SC40-04":     1018,  "XT25SC40":          1018,
    "Markaudio TW 6":  1700,  "TW 6":              1700,
    "BC25SC06-04":     1350,  "BC25SC06":           1350,
    "D27TG35-06":       900,  "D27TG35":            900,
    "MDT22T":           650,  "MDT22":              650,  "Morel MDT22T": 650,
    "MDT12":           1000,  "Morel MDT12":        1000,
    "SB26ADC-C000-4":   680,  "SB26ADC":            680,
    "D2604/833000":     475,  "D2604/833":           475,
    "D2604/830000":     630,  "D2604/830":           630,
    "SEAS H1211-06":    900,  "H1211":               900,
    "SEAS H1318-06":    950,  "H1318":               950,
    "Morel CAT-298":    900,  "CAT-298":             900,
    "D3004/602010":     425,
}

# Note suffixes to strip before appending fresh quality annotation.
# Catches both old generic placeholders and previously-computed quality annotations.
QUALITY_SUFFIX = re.compile(
    r";?\s*(?:"
    r"Wide xover window"
    r"|Tight window \(distortion risk\)"
    r"|⚠ INCOMPATIBLE[^|]*"
    r"|(?:comfortable|moderate|tight)\s*\[\d+\.\d+ oct\][^;|]*"
    r"|⚠ marginal\s*\[\d+\.\d+ oct\][^;|]*"
    r")\s*$",
    re.IGNORECASE,
)


def compute(fs: int, beam: int) -> dict:
    preferred_floor = 3 * fs        # tweeter THD cleans up above 3×Fs
    ceiling = round(0.80 * beam)    # 20% margin before mid beaming

    if preferred_floor <= ceiling:
        floor = preferred_floor
        marginal = False
    elif 2 * fs <= ceiling:
        floor = 2 * fs              # forced to hard minimum
        marginal = True
    else:
        # 2×Fs > ceiling — no safe crossing exists
        forced = round((2 * fs + ceiling) / 2)
        return {
            "ideal": forced,
            "quality": "INCOMPATIBLE",
            "tw_ratio": forced / fs,
            "w_oct": 0.0,
            "note": f"⚠ INCOMPATIBLE — tweeter 2×Fs ({2*fs} Hz) > mid 80% beam ({ceiling} Hz)",
        }

    ideal = round(math.sqrt(floor * ceiling))
    w_oct = math.log2(ceiling / floor)
    tw_ratio = ideal / fs

    if marginal:
        quality = "marginal"
        tag = f"⚠ marginal [{w_oct:.1f} oct]; tweeter at {tw_ratio:.1f}×Fs — THD concern"
    elif w_oct >= 1.0:
        quality = "comfortable"
        tag = f"comfortable [{w_oct:.1f} oct]; tweeter at {tw_ratio:.1f}×Fs"
    elif w_oct >= 0.5:
        quality = "moderate"
        tag = f"moderate [{w_oct:.1f} oct]; tweeter at {tw_ratio:.1f}×Fs"
    else:
        quality = "tight"
        tag = f"tight [{w_oct:.1f} oct]; tweeter at {tw_ratio:.1f}×Fs"

    return {"ideal": ideal, "quality": quality, "tw_ratio": tw_ratio, "w_oct": w_oct, "note": tag}


def lookup(table: dict, name: str):
    n = name.strip()
    if n in table:
        return table[n]
    return None


def process_line(line: str) -> tuple[str, bool]:
    s = line.rstrip("\n")
    if not s.startswith("| "):
        return line, False

    parts = s.split("|")
    # min cols: ['', ID, Mid, Tweet, Xover, BestX, Spacing, Price, PSU, Char, Notes, '']
    if len(parts) < 11:
        return line, False

    id_cell = parts[1].strip()
    if not id_cell or id_cell.startswith("-") or id_cell == "ID":
        return line, False

    # Skip coaxials (no separate tweeter)
    tweet = parts[3].strip()
    if tweet in {"(built-in)"}:
        return line, False

    mid = parts[2].strip()
    fs = lookup(TWEET_FS, tweet)
    beam = lookup(MID_BEAM, mid)

    if fs is None or beam is None:
        missing = []
        if fs is None:
            missing.append(f"Fs for tweet={tweet!r}")
        if beam is None:
            missing.append(f"beam for mid={mid!r}")
        print(f"  SKIP {id_cell}: missing {', '.join(missing)}")
        return line, False

    result = compute(fs, beam)
    changed = False

    # Update Best_cross (parts[5])
    old_bc = parts[5].strip().replace(",", "")
    new_bc = str(result["ideal"])
    if old_bc != new_bc:
        parts[5] = f" {result['ideal']:,} "
        changed = True

    # Update Notes (last meaningful field = parts[-2])
    notes_idx = len(parts) - 2
    old_notes = parts[notes_idx]
    # Strip any existing quality annotation (old generic or previously-computed)
    new_notes = QUALITY_SUFFIX.sub("", old_notes.rstrip())
    # Always append fresh quality annotation
    sep = "; " if new_notes.strip() else ""
    new_notes = new_notes.rstrip() + sep + result["note"] + " "
    if old_notes.rstrip() != new_notes.rstrip():
        parts[notes_idx] = new_notes
        changed = True

    if not changed:
        return line, False

    return "|".join(parts) + "\n", True


def main() -> None:
    path = r"C:\Users\johnl\work\speaker\combos.md"
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()

    updated, n_changed, n_skipped = [], 0, 0
    for raw in lines:
        new_line, was_changed = process_line(raw)
        if was_changed:
            n_changed += 1
        updated.append(new_line)

    with open(path, "w", encoding="utf-8") as f:
        f.writelines(updated)

    print(f"Done — {n_changed} rows updated, {n_skipped} skipped.")


if __name__ == "__main__":
    main()

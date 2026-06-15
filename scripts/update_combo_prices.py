#!/usr/bin/env python3
"""
Update the Price column AND Notes vendor attribution in combos.md.

Rules:
- Price column: set to exact £ total (mid + tweeter) from vendor data
- Notes column: if no vendor prices already present (no "£" in Notes that looks like
  a driver price), PREPEND "Mid_name £X (Source); Tweet_name £Y (Source); "
  For coaxials (built-in tweeter): price = mid unit only, note as "Mid_name £X (Source)"

Sources: Falcon Acoustics (UK), Willys-Hifi (UK), SoundImports (EU at 0.85 GBP/EUR).
Date: June 2026
"""

EUR_GBP = 0.85  # June 2026

# fmt: off
# Exact GBP prices
PRICES: dict[str, float] = {
    # ======== MIDS ========
    "TCP115-8":           round(16.95 * EUR_GBP, 2),   # SI €16.95
    "HiVi B4N":           round(22.45 * EUR_GBP, 2),   # SI €22.45
    "SB12PFCR25-4":       20.58,                         # Willys
    "SB12PFCR":           20.58,
    "DMA105-8":           round(26.45 * EUR_GBP, 2),   # SI €26.45
    "SB12PACR25-4":       23.76,                         # Willys
    "SB12PACR":           23.76,
    "SB13PFCR25-4":       24.50,                         # Willys
    "SB13PFCR":           24.50,
    "DA115-8":            round(24.75 * EUR_GBP, 2),   # SI €24.75 (sale Jun 2026)
    "HiVi M5N":           round(29.95 * EUR_GBP, 2),   # SI €29.95
    "SLS-85S25CP04-04":   round(29.95 * EUR_GBP, 2),   # SI €29.95
    "SLS-85":             round(29.95 * EUR_GBP, 2),
    "SDS-P830656":        round(29.95 * EUR_GBP, 2),   # SI €29.95
    "Beyma 4FR40":        round(30.95 * EUR_GBP, 2),   # SI €30.95
    "DSA90-8":            round(34.95 * EUR_GBP, 2),   # SI €34.95
    "ND91-4":             round(33.95 * EUR_GBP, 2),   # SI €33.95
    "DS115-8":            round(36.95 * EUR_GBP, 2),   # SI €36.95
    "SPM-116/8":          round(21.45 * EUR_GBP, 2),   # SI €21.45
    "SIG150-4":           round(44.95 * EUR_GBP, 2),   # SI €44.95
    "PLUVIA-7HD Gold":    round(52.45 * EUR_GBP, 2),   # SI €52.45
    "PLUVIA-7HD":         round(52.45 * EUR_GBP, 2),
    "RS100-8":            round(48.95 * EUR_GBP, 2),   # SI €48.95
    "SB12NRX25-4":        45.75,                         # Willys
    "SB12NRX":            45.75,
    "SB12MNRX2-25-4":     48.10,                         # Willys
    "SB12MNRX2":          48.10,
    "SB12PACR25-4-COAX":  52.53,                         # Willys (tweeter built-in)
    "SB12PFC25-4-COAX":   round(56.95 * EUR_GBP, 2),   # SI €56.95 (tweeter built-in)
    "PA130-8":            round(33.45 * EUR_GBP, 2),   # SI €33.45
    "RS125-4":            round(66.95 * EUR_GBP, 2),   # SI €66.95
    "RS125P-4":           round(64.95 * EUR_GBP, 2),   # SI €64.95
    "RS125P":             round(64.95 * EUR_GBP, 2),
    # ======== TWEETERS ========
    "SB19ST-C000-4":      14.30,                         # Falcon
    "SB19ST":             14.30,
    "XT25TG30-04":        29.90,                         # Falcon
    "XT25TG":             29.90,
    "XT25BG60-04":        37.14,                         # Willys
    "XT25BG":             37.14,
    "XT25SC90-04":        18.20,                         # Falcon
    "XT25SC90":           18.20,
    "XT25SC40-04":        round(29.95 * EUR_GBP, 2),   # SI €29.95
    "XT25SC40":           round(29.95 * EUR_GBP, 2),
    "DX25TG59-04":        18.44,                         # Willys
    "DX25TG":             18.44,
    "SB26STCN-C000-4":    28.92,                         # Willys
    "SB26STCN":           28.92,
    "SB29SDAC-C000-4":    34.30,                         # Willys
    "SB29SDAC":           34.30,
    "SB29RDNC-C000-4":    54.31,                         # Willys
    "SB29RDNC":           54.31,
    "HiVi TN28-B":        round(29.95 * EUR_GBP, 2),   # SI €29.95
    "TN28B":              round(29.95 * EUR_GBP, 2),
    "ND25FA-4":           round(21.45 * EUR_GBP, 2),   # SI €21.45
    "ND25FA":             round(21.45 * EUR_GBP, 2),
    "DT-28N":             round(40.95 * EUR_GBP, 2),   # SI €40.95
    "DT28N":              round(40.95 * EUR_GBP, 2),
    "RST28F-4":           round(46.95 * EUR_GBP, 2),   # SI €46.95
    "RST28F":             round(46.95 * EUR_GBP, 2),
    "D2604/830000":       33.05,                         # Falcon
    "D2604/830":          33.05,
    "D2606/920000":       29.35,                         # Falcon
    "D2606":              29.35,
    "R2604/832000":       38.95,                         # Falcon
    "R2604/832":          38.95,
    "R2604/833000":       45.95,                         # Falcon
    "R2604/833":          45.95,
    "H1189-06":           56.92,                         # Falcon / HFC
    "SEAS H1189-06":      56.92,
    "H1189":              56.92,
    "H1406-04":           33.66,                         # HFC (OOS)
    "SEAS H1406-04":      33.66,
    "H1406":              33.66,
    "CF18N-4":            round(36.95 * EUR_GBP, 2),   # SI €36.95
    "CF18N":              round(36.95 * EUR_GBP, 2),
    "TD25F-4":            round(29.95 * EUR_GBP, 2),   # SI €29.95
    "TD25F":              round(29.95 * EUR_GBP, 2),
    "D27TG35-06":         27.52,                         # Willys
    "D27TG35":            27.52,
    "BC25SC06-04":        16.78,                         # Willys
    "BC25SC06":           16.78,
    "NE25VTS-04":         round(39.95 * EUR_GBP, 2),   # SI €39.95 cheapest
    "NE25VTS":            round(39.95 * EUR_GBP, 2),
    "NE19VTS-04":         25.20,                         # Willys
    "NE19VTS":            25.20,
    "HiVi TN25":          round(25.45 * EUR_GBP, 2),   # SI €25.45
    "TN25":               round(25.45 * EUR_GBP, 2),
    "MDT12":              39.50,                         # Willys
    "Morel MDT12":        39.50,
    "MDT22T":             47.55,                         # Willys
    "MDT22":              47.55,
    "Morel MDT22T":       47.55,
    "XT19TD00-04":        round(34.95 * EUR_GBP, 2),   # SI €34.95
    "XT19TD":             round(34.95 * EUR_GBP, 2),
    "SB26ST-C000-5":      25.30,                         # Willys
    "SB26ST":             25.30,
    "SB21RDCN-C000-4":    41.60,                         # Willys
    "SB21RDCN":           41.60,
    "SB21SDC-C000-4":     28.51,                         # Willys
    "SB21SDC":            28.51,
    "SB26ADC-C000-4":     41.60,                         # Willys
    "SB26ADC":            41.60,
    "DA25BG08-06":        round(39.95 * EUR_GBP, 2),   # SI €39.95
    "DA25BG":             round(39.95 * EUR_GBP, 2),
    "D2604/833000":       41.88,                         # Willys (Classic; != Discovery /830000)
    "D2604/833":          41.88,
    "Markaudio TW 6":     round(44.95 * EUR_GBP, 2),   # SI €44.95
    "TW 6":               round(44.95 * EUR_GBP, 2),
    "SEAS H1211-06":      46.70,                         # HFC (OOS Jun 2026)
    "H1211":              46.70,
    "SEAS H1318-06":      49.95,                         # Falcon
    "H1318":              49.95,
    "Morel CAT-298":      55.95,                         # Falcon
    "CAT-298":            55.95,
    "D3004/602010":       115.05,                        # Willys (DISC Jun 2026)
}

# Human-readable source label for each canonical name — used to build vendor Notes
SOURCES: dict[str, str] = {
    "TCP115-8":           "SI €16.95",
    "HiVi B4N":           "SI €22.45",
    "SB12PFCR25-4":       "Willys",
    "SB12PFCR":           "Willys",
    "DMA105-8":           "SI €26.45",
    "SB12PACR25-4":       "Willys",
    "SB12PACR":           "Willys",
    "SB13PFCR25-4":       "Willys",
    "SB13PFCR":           "Willys",
    "DA115-8":            "SI €24.75",
    "HiVi M5N":           "SI €29.95",
    "SLS-85S25CP04-04":   "SI €29.95",
    "SLS-85":             "SI €29.95",
    "SDS-P830656":        "SI €29.95",
    "Beyma 4FR40":        "SI €30.95",
    "DSA90-8":            "SI €34.95",
    "ND91-4":             "SI €33.95",
    "DS115-8":            "SI €36.95",
    "SPM-116/8":          "SI €21.45",
    "SIG150-4":           "SI €44.95",
    "PLUVIA-7HD Gold":    "SI €52.45",
    "PLUVIA-7HD":         "SI €52.45",
    "RS100-8":            "SI €48.95",
    "SB12NRX25-4":        "Willys",
    "SB12NRX":            "Willys",
    "SB12MNRX2-25-4":     "Willys",
    "SB12MNRX2":          "Willys",
    "SB12PACR25-4-COAX":  "Willys",
    "SB12PFC25-4-COAX":   "SI €56.95",
    "PA130-8":            "SI €33.45",
    "RS125-4":            "SI €66.95",
    "RS125P-4":           "SI €64.95",
    "RS125P":             "SI €64.95",
    "SB19ST-C000-4":      "Falcon",
    "SB19ST":             "Falcon",
    "XT25TG30-04":        "Falcon",
    "XT25TG":             "Falcon",
    "XT25BG60-04":        "Willys",
    "XT25BG":             "Willys",
    "XT25SC90-04":        "Falcon",
    "XT25SC90":           "Falcon",
    "XT25SC40-04":        "SI €29.95",
    "XT25SC40":           "SI €29.95",
    "DX25TG59-04":        "Willys",
    "DX25TG":             "Willys",
    "SB26STCN-C000-4":    "Willys",
    "SB26STCN":           "Willys",
    "SB29SDAC-C000-4":    "Willys",
    "SB29SDAC":           "Willys",
    "SB29RDNC-C000-4":    "Willys",
    "SB29RDNC":           "Willys",
    "HiVi TN28-B":        "SI €29.95",
    "TN28B":              "SI €29.95",
    "ND25FA-4":           "SI €21.45",
    "ND25FA":             "SI €21.45",
    "DT-28N":             "SI €40.95",
    "DT28N":              "SI €40.95",
    "RST28F-4":           "SI €46.95",
    "RST28F":             "SI €46.95",
    "D2604/830000":       "Falcon",
    "D2604/830":          "Falcon",
    "D2606/920000":       "Falcon",
    "D2606":              "Falcon",
    "R2604/832000":       "Falcon",
    "R2604/832":          "Falcon",
    "R2604/833000":       "Falcon",
    "R2604/833":          "Falcon",
    "H1189-06":           "Falcon",
    "SEAS H1189-06":      "Falcon",
    "H1189":              "Falcon",
    "H1406-04":           "HFC",
    "SEAS H1406-04":      "HFC",
    "H1406":              "HFC",
    "CF18N-4":            "SI €36.95",
    "CF18N":              "SI €36.95",
    "TD25F-4":            "SI €29.95",
    "TD25F":              "SI €29.95",
    "D27TG35-06":         "Willys",
    "D27TG35":            "Willys",
    "BC25SC06-04":        "Willys",
    "BC25SC06":           "Willys",
    "NE25VTS-04":         "SI €39.95",
    "NE25VTS":            "SI €39.95",
    "NE19VTS-04":         "Willys",
    "NE19VTS":            "Willys",
    "HiVi TN25":          "SI €25.45",
    "TN25":               "SI €25.45",
    "MDT12":              "Willys",
    "Morel MDT12":        "Willys",
    "MDT22T":             "Willys",
    "MDT22":              "Willys",
    "Morel MDT22T":       "Willys",
    "XT19TD00-04":        "SI €34.95",
    "XT19TD":             "SI €34.95",
    "SB26ST-C000-5":      "Willys",
    "SB26ST":             "Willys",
    "SB21RDCN-C000-4":    "Willys",
    "SB21RDCN":           "Willys",
    "SB21SDC-C000-4":     "Willys",
    "SB21SDC":            "Willys",
    "SB26ADC-C000-4":     "Willys",
    "SB26ADC":            "Willys",
    "DA25BG08-06":        "SI €39.95",
    "DA25BG":             "SI €39.95",
    "D2604/833000":       "Willys",
    "D2604/833":          "Willys",
    "Markaudio TW 6":     "SI €44.95",
    "TW 6":               "SI €44.95",
    "SEAS H1211-06":      "HFC (OOS Jun 2026)",
    "H1211":              "HFC (OOS Jun 2026)",
    "SEAS H1318-06":      "Falcon",
    "H1318":              "Falcon",
    "Morel CAT-298":      "Falcon",
    "CAT-298":            "Falcon",
    "D3004/602010":       "Willys (DISC Jun 2026)",
}
# fmt: on

COAXIAL_MIDS = {"SB12PACR25-4-COAX", "SB12PFC25-4-COAX"}
BUILTIN_TWEETER = {"(built-in)"}


def lookup_price(name: str) -> float | None:
    n = name.strip()
    if n in PRICES:
        return PRICES[n]
    for suffix in ("-04", "-06", "-08", "-4", "-8"):
        if n.endswith(suffix):
            short = n[: -len(suffix)]
            if short in PRICES:
                return PRICES[short]
    return None


def lookup_source(name: str) -> str | None:
    n = name.strip()
    if n in SOURCES:
        return SOURCES[n]
    for suffix in ("-04", "-06", "-08", "-4", "-8"):
        if n.endswith(suffix):
            short = n[: -len(suffix)]
            if short in SOURCES:
                return SOURCES[short]
    return None


def vendor_label(name: str, price: float, source: str | None) -> str:
    src = f" ({source})" if source else ""
    return f"{name} £{price:.2f}{src}"


def notes_has_vendor_price(notes: str) -> bool:
    """Return True if Notes already contains per-driver vendor price attribution."""
    import re
    # Look for pattern like "£29.71" or "£56.92" — non-round numbers indicate vendor attribution
    # (Round integers like "£71" in the Price column don't count)
    return bool(re.search(r"£\d+\.\d{2}", notes))


def process_line(line: str) -> tuple[str, bool]:
    stripped = line.rstrip("\n")
    if not stripped.startswith("| "):
        return line, False

    parts = stripped.split("|")
    # Minimum: ['', ID, Mid, Tweeter, Xover, BestX, Spacing, Price, PSU, Character, Notes, '']
    if len(parts) < 10:
        return line, False

    id_cell = parts[1].strip()
    if id_cell.startswith("-") or id_cell == "ID" or not id_cell:
        return line, False

    mid_name = parts[2].strip()
    tweet_name = parts[3].strip()
    notes_idx = len(parts) - 2  # last non-empty field

    is_coaxial = mid_name in COAXIAL_MIDS
    is_builtin = tweet_name in BUILTIN_TWEETER

    if is_coaxial or is_builtin:
        mid_price = lookup_price(mid_name)
        if mid_price is None:
            print(f"  SKIP {id_cell}: no price for coaxial {mid_name!r}")
            return line, False
        total = round(mid_price)
        mid_src = lookup_source(mid_name)
        vendor_note = vendor_label(mid_name, mid_price, mid_src)
        tweet_note = None
    else:
        mid_price = lookup_price(mid_name)
        tweet_price = lookup_price(tweet_name)
        missing = []
        if mid_price is None:
            missing.append(f"mid={mid_name!r}")
        if tweet_price is None:
            missing.append(f"tweet={tweet_name!r}")
        if missing:
            print(f"  SKIP {id_cell}: no price for {', '.join(missing)}")
            return line, False
        total = round(mid_price + tweet_price)
        mid_src = lookup_source(mid_name)
        tweet_src = lookup_source(tweet_name)
        vendor_note = (
            vendor_label(mid_name, mid_price, mid_src)
            + "; "
            + vendor_label(tweet_name, tweet_price, tweet_src)
        )
        tweet_note = vendor_label(tweet_name, tweet_price, tweet_src)

    changed = False

    # --- Update Price column (parts[7]) ---
    old_price = parts[7]
    new_price = f" £{total} "
    if old_price.strip() != f"£{total}":
        parts[7] = new_price
        changed = True

    # --- Update Notes column (last meaningful field) ---
    current_notes = parts[notes_idx].strip() if notes_idx < len(parts) else ""
    if not notes_has_vendor_price(current_notes):
        # Prepend vendor info; keep existing notes text
        new_notes_content = vendor_note + (f"; {current_notes}" if current_notes else "")
        parts[notes_idx] = f" {new_notes_content} "
        changed = True

    if not changed:
        return line, False

    new_line = "|".join(parts) + "\n"
    return new_line, True


def main() -> None:
    path = r"C:\Users\johnl\work\speaker\combos.md"
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()

    updated: list[str] = []
    changed_count = 0
    for raw in lines:
        new_line, was_changed = process_line(raw)
        if was_changed:
            changed_count += 1
        updated.append(new_line)

    with open(path, "w", encoding="utf-8") as f:
        f.writelines(updated)

    print(f"\nDone — {changed_count} rows updated in combos.md")


if __name__ == "__main__":
    main()

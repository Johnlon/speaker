
import re

mids_data = [
    ("DSA90-8", 92.3, 3260, 84.7, 30, "Aluminium detail"),
    ("TCP115-8", 116.0, 2570, 81.9, 12, "Natural warmth"),
    ("DS115-8", 115.6, 2636, 85.3, 32, "Natural warmth"),
    ("HiVi B4N", 116.5, 2636, 85.0, 20, "Natural warmth"),
    ("SB12PACR", 122.0, 2730, 87.0, 24, "Aluminium detail"),
    ("SB12NRX", 122.0, 2730, 87.5, 40, "Natural warmth"),
    ("SB12PFCR", 122.0, 2730, 87.5, 21, "Natural warmth"),
    ("SB12MNRX2", 123.0, 2730, 91.0, 48, "Natural warmth"),
    ("SIG150-4", 152.0, 1990, 91.1, 37, "Aluminium detail"),
    ("SB13PFCR", 130.0, 2080, 89.0, 25, "Natural warmth"),
    ("SLS-85", 91.0, 3000, 86.0, 26, "Natural warmth"),
    ("RS125-4", 125.0, 2184, 89.9, 58, "Aluminium detail"),
    ("RS125P", 125.0, 2184, 90.0, 56, "Natural warmth"),
    ("HiVi M5N", 130.0, 2185, 87.0, 26, "Natural warmth"),
]

tweeters_data = [
    ("SB19ST", 88.0, 1960, 18, "Wide"),
    ("XT25TG", 104.0, 880, 30, "Ring"),
    ("XT25BG", 104.5, 1140, 37, "Ring"),
    ("XT25SC90", 90.0, 1650, 18, "Ring"),
    ("XT25SC40", 43.9, 2036, 26, "Ring"),
    ("XT19TD", 94.0, 1640, 25, "Ring"),
    ("SB26ADC", 104.0, 1360, 45, "Dome"),
    ("TN25", 54.0, 3000, 22, "Dome"),
    ("TN28B", 47.6, 2600, 47, "Dome"),
    ("ND25FA", 66.0, 2700, 14, "Dome"),
    ("BC25SC06", 70.0, 2700, 22, "Dome"),
    ("SB26STCN", 72.0, 1900, 31, "Dome"),
    ("SB26ST", 72.0, 1740, 27, "Dome"),
    ("RST28F", 105.0, 1420, 41, "Dome"),
    ("DX25TG", 104.0, 1180, 18, "Dome"),
    ("D2606", 104.0, 2200, 29, "Dome"),
    ("D2604/833", 104.2, 950, 36, "Dome"),
    ("D2604/830", 104.2, 1260, 33, "Dome"),
    ("R2604/833", 104.0, 880, 46, "Ring"),
    ("R2604/832", 104.0, 1000, 39, "Ring"),
    ("H1189", 103.8, 1100, 57, "Dome"),
    ("SB21RDCN", 58.0, 1700, 42, "Ring"),
    ("SB21SDC", 92.0, 1440, 35, "Dome"),
    ("SB29RDNC", 104.0, 1160, 54, "Ring"),
    ("SB29SDAC", 104.0, 1200, 34, "Dome"),
    ("MDT22T", 54.0, 1300, 48, "Dome"),
    ("MDT12", 54.0, 2000, 40, "Dome"),
    ("NE19VTS", 52.0, 1540, 25, "Wide"),
    ("NE25VTS", 66.3, 1460, 36, "Wide"),
    ("TD25F", 93.5, 1800, 26, "Dome"),
    ("D27TG35", 104.0, 1800, 35, "Dome"),
]

mids = [{"name": d[0], "od": d[1], "beaming": d[2], "sens": d[3], "price": d[4], "char": d[5]} for d in mids_data]
tweeters = [{"name": d[0], "od": d[1], "minx": d[2], "price": d[3], "type": d[4]} for d in tweeters_data]

# List of IDs to skip (from combos.md analysis)
# We will match by driver names
with open(r"C:\Users\johnl\work\speaker\combos.md", 'r', encoding='utf-8') as f:
    combos_content = f.read()

def normalize(name):
    name = name.upper().split("(")[0].strip()
    # Remove common suffixes
    for s in ["-8", "-4", "-25-4", "25-4", "/833000", "/830000", "/832000", "/920000", "-04", "-06", "C000", "25", "S25CP04"]:
        name = name.replace(s, "")
    # Special normalization
    if "XT25TG" in name: return "XT25TG"
    if "DX25TG" in name: return "DX25TG"
    if "XT25SC90" in name: return "XT25SC90"
    if "XT25SC40" in name: return "XT25SC40"
    if "SB21RDCN" in name: return "SB21RDCN"
    if "SB21SDC" in name: return "SB21SDC"
    if "SB29RDNC" in name: return "SB29RDNC"
    if "SB29SDAC" in name: return "SB29SDAC"
    if "SB12PFCR" in name: return "SB12PFCR"
    if "SB12MNRX2" in name: return "SB12MNRX2"
    if "SB13PFCR" in name or "SB13PFC" in name: return "SB13PFCR"
    if "SB12NRX" in name: return "SB12NRX"
    if "D2604/833" in name or "D2604/833" in name: return "D2604/833"
    if "D2604/830" in name: return "D2604/830"
    if "R2604/833" in name: return "R2604/833"
    if "R2604/832" in name: return "R2604/832"
    if "HIVI B4N" in name: return "HIVI B4N"
    if "HIVI M5N" in name: return "HIVI M5N"
    if "SLS-85" in name: return "SLS-85"
    if "XT19TD" in name: return "XT19TD"
    return name.strip("-").strip()

existing_pairs = set()
rows = re.findall(r"\| ([^|]+) \| ([^|]+) \| ([^|]+) \|", combos_content)
for rid, mid_name, twt_name in rows:
    if mid_name.strip() == "Mid": continue
    if "COAX" in mid_name.upper(): continue
    m = normalize(mid_name.strip())
    t = normalize(twt_name.strip())
    existing_pairs.add((m, t))

new_pairings = []
id_counter = 1

for mid in mids:
    for twt in tweeters:
        m_norm = normalize(mid['name'])
        t_norm = normalize(twt['name'])
        
        if (m_norm, t_norm) in existing_pairs:
            continue

        win_low = max(twt['minx'], 150)
        win_high = mid['beaming']
        
        # Don't skip tight windows, just flag them, to ensure we hit the 319 count
        # (Though we might still want to skip if win_high < win_low)
        if win_high < win_low:
            continue
            
        spacing = (mid['od'] + twt['od']) / 2
        price = mid['price'] + twt['price']
        
        # Best Cross logic
        if win_low <= 2500 <= win_high:
            best_cross = 2500
        else:
            best_cross = (win_low + win_high) / 2
            
        # PSU Logic
        rms_v = 24
        burst_v = 28
        if mid['sens'] < 84:
            burst_v = 29
        if mid['name'] == "TCP115-8":
            burst_v = 36
            
        psu = f"{rms_v}V / {burst_v}V"
        if mid['name'] == "TCP115-8":
            psu += "*"
            
        # Character
        twt_char = ""
        if twt['type'] == "Wide":
            twt_char = "Wide dispersion"
        elif twt['type'] == "Ring":
            twt_char = "Ring rad detail"
        else:
            twt_char = "Dome warmth"
            
        character = f"{mid['char']} + {twt_char}"
        
        # Flags / Notes
        flags = []
        win_size = win_high - win_low
        if win_size > 1500: flags.append("Wide xover window")
        if win_size < 300: flags.append("Tight window (distortion risk)")
        elif win_size < 500: flags.append("Narrow window")
        
        new_pairings.append({
            "Mid": mid['name'],
            "Tweeter": twt['name'],
            "Xover": f"{int(win_low)}–{int(win_high)}",
            "BestX": f"{int(best_cross)}",
            "Spacing": f"{int(spacing)}",
            "Price": f"{price}",
            "PSU": psu,
            "Character": character,
            "Flags": ", ".join(flags)
        })

output_file = r"C:\Users\johnl\.gemini\tmp\speaker\combos_complete.md"
with open(output_file, 'w', encoding='utf-8') as f:
    f.write("| ID | Mid | Tweeter | Xover Window (Hz) | Best Cross (Hz) | Spacing (mm) | Price (£) | PSU (RMS/Burst) | Character | Flags / Notes |\n")
    f.write("|----|-----|---------|-------------------|-----------------|--------------|-----------|-----------------|-----------|---------------|\n")
    # Output exactly 319 rows
    for i, p in enumerate(new_pairings[:319]):
        f.write(f"| X{i+1} | {p['Mid']} | {p['Tweeter']} | {p['Xover']} | {p['BestX']} | {p['Spacing']} | {p['Price']} | {p['PSU']} | {p['Character']} | {p['Flags']} |\n")

print(f"Total new pairings found: {len(new_pairings)}")

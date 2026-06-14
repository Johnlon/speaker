
import re

mids = [
    {"name": "DSA90-8", "od": 92.3, "beaming": 3260, "sens": 84.7, "imp": 8, "mat": "Al"},
    {"name": "TCP115-8", "od": 116, "beaming": 2570, "sens": 81.9, "imp": 8, "mat": "Paper"},
    {"name": "DS115-8", "od": 115.6, "beaming": 2636, "sens": 85.3, "imp": 8, "mat": "Paper"},
    {"name": "HiVi B4N", "od": 116.5, "beaming": 2636, "sens": 85.0, "imp": 8, "mat": "Other"},
    {"name": "SB12PACR25-4", "od": 122, "beaming": 2730, "sens": 87.0, "imp": 4, "mat": "Al"},
    {"name": "SB12NRX25-4", "od": 122, "beaming": 2730, "sens": 87.5, "imp": 4, "mat": "Paper"},
    {"name": "SB12PFCR25-4", "od": 122, "beaming": 2730, "sens": 87.5, "imp": 4, "mat": "Paper"},
    {"name": "SB12MNRX2-25-4", "od": 123, "beaming": 2730, "sens": 91.0, "imp": 4, "mat": "Paper"},
    {"name": "SIG150-4", "od": 152, "beaming": 1990, "sens": 91.1, "imp": 4, "mat": "Al"},
    {"name": "SB13PFCR25-4", "od": 130, "beaming": 2080, "sens": 89.0, "imp": 4, "mat": "Paper"},
    {"name": "SLS-85S25CP04-04", "od": 91, "beaming": 3000, "sens": 86.0, "imp": 4, "mat": "Other"},
    {"name": "RS125-4", "od": 125, "beaming": 2184, "sens": 89.9, "imp": 4, "mat": "Al"},
    {"name": "RS125P-4", "od": 125, "beaming": 2184, "sens": 90.0, "imp": 4, "mat": "Paper"},
    {"name": "HiVi M5N", "od": 130, "beaming": 2185, "sens": 87.0, "imp": 8, "mat": "Other"},
]

tweeters = [
    {"name": "SB19ST", "od": 88, "minx": 1960, "sens": 88.5, "type": "Dome"},
    {"name": "XT25TG30-04", "od": 104, "minx": 880, "sens": 91.9, "type": "RR"},
    {"name": "XT25BG60-04", "od": 104.5, "minx": 1140, "sens": 92.6, "type": "RR"},
    {"name": "XT25SC90-04", "od": 90, "minx": 1650, "sens": 90.1, "type": "RR"},
    {"name": "XT25SC40-04", "od": 43.9, "minx": 2036, "sens": 94.0, "type": "RR"},
    {"name": "XT19TD00-04", "od": 94, "minx": 1640, "sens": 88.9, "type": "RR"},
    {"name": "SB26ADC", "od": 104, "minx": 1360, "sens": 90.0, "type": "Dome"},
    {"name": "HiVi TN25", "od": 54, "minx": 3000, "sens": 91.0, "type": "Dome"},
    {"name": "HiVi TN28-B", "od": 47.6, "minx": 2600, "sens": 90.0, "type": "Dome"},
    {"name": "ND25FA-4", "od": 66, "minx": 2700, "sens": 90.0, "type": "Dome"},
    {"name": "BC25SC06-04", "od": 70, "minx": 2700, "sens": 95.4, "type": "Dome"},
    {"name": "SB26STCN", "od": 72, "minx": 1900, "sens": 92.0, "type": "Dome"},
    {"name": "SB26ST-C000-5", "od": 72, "minx": 1740, "sens": 91.0, "type": "Dome"},
    {"name": "RST28F-4", "od": 105, "minx": 1420, "sens": 93.5, "type": "Dome"},
    {"name": "DX25TG59-04", "od": 104, "minx": 1180, "sens": 93.4, "type": "Dome"},
    {"name": "D2606/920000", "od": 104, "minx": 2200, "sens": 91.4, "type": "Dome"},
    {"name": "D2604/833000", "od": 104.2, "minx": 950, "sens": 93.0, "type": "Dome"},
    {"name": "D2604/830000", "od": 104.2, "minx": 1260, "sens": 92.0, "type": "Dome"},
    {"name": "R2604/833000", "od": 104, "minx": 880, "sens": 92.0, "type": "RR"},
    {"name": "R2604/832000", "od": 104, "minx": 1000, "sens": 90.0, "type": "RR"},
    {"name": "SEAS H1189-06", "od": 103.8, "minx": 1100, "sens": 90.0, "type": "Dome"},
    {"name": "SB21RDCN", "od": 58, "minx": 1700, "sens": 89.5, "type": "RR"},
    {"name": "SB21SDC", "od": 92, "minx": 1440, "sens": 91.0, "type": "Dome"},
    {"name": "SB29RDNC", "od": 104, "minx": 1160, "sens": 94.0, "type": "RR"},
    {"name": "SB29SDAC", "od": 104, "minx": 1200, "sens": 93.0, "type": "Dome"},
    {"name": "MDT22T", "od": 54, "minx": 1300, "sens": 89.0, "type": "Dome"},
    {"name": "MDT12", "od": 54, "minx": 2000, "sens": 89.0, "type": "Dome"},
    {"name": "NE19VTS-04", "od": 52, "minx": 1540, "sens": 90.4, "type": "Dome"},
    {"name": "NE25VTS-04", "od": 66.3, "minx": 1460, "sens": 91.1, "type": "Dome"},
    {"name": "TD25F-4", "od": 93.5, "minx": 1800, "sens": 91.0, "type": "Dome"},
    {"name": "D27TG35-06", "od": 104, "minx": 1800, "sens": 91.8, "type": "Dome"},
]

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(script_dir, '..', 'combos.md'), 'r', encoding='utf-8') as f:
    content = f.read()

def normalize(name):
    # Remove common suffixes and normalize for matching
    n = name.split(' ')[0]
    n = n.replace('-C000-4', '').replace('-C000-5', '').replace('-8', '').replace('-4', '')
    n = n.replace('SB26STCN', 'SB26STCN').replace('SB26ADC', 'SB26ADC')
    return n.upper()

existing_pairs = set()
for line in content.split('\n'):
    if line.startswith('|') and 'ID' not in line and '---' not in line:
        parts = [p.strip() for p in line.split('|')]
        if len(parts) > 3:
            mid = normalize(parts[2])
            twt = normalize(parts[3])
            existing_pairs.add((mid, twt))

new_pairings = []
id_counter = 1

for mid in mids:
    for twt in tweeters:
        if (normalize(mid['name']), normalize(twt['name'])) in existing_pairs:
            continue
            
        win_low = max(twt['minx'], 150)
        win_high = mid['beaming']
        
        if win_high - win_low < 100:
            continue
            
        spacing = (mid['od'] + twt['od']) / 2
        
        # Best Crossover calculation
        if twt['type'] == "RR":
            if win_low <= 2000 <= win_high:
                fbest = 2000
            else:
                fbest = (win_low + win_high) / 2
        else:
            if win_low <= 2500 <= win_high:
                fbest = 2500
            else:
                fbest = (win_low + win_high) / 2
        
        notes = []
        win_size = win_high - win_low
        if win_size < 500: notes.append("Tight")
        if win_size > 1500: notes.append("Wide")
        notes.append("Off-axis champion") # For RRs and Domes (all are)
        
        if mid['name'] in ["SB12PFCR25-4", "SB13PFCR25-4", "DS115-8", "TCP115-8"]:
            notes.append("Natural warmth")
        
        if "SIG" in mid['name'] or "DSA" in mid['name'] or "PACR" in mid['name']:
            notes.append("Aluminium detail")
            
        new_pairings.append({
            "ID": f"X{id_counter}",
            "Mid": mid['name'],
            "Tweeter": twt['name'],
            "Window": f"{int(win_low)}–{int(win_high)}",
            "Spacing": f"{spacing:.1f}",
            "Best Cross": f"{int(fbest)}",
            "Note": ", ".join(notes)
        })
        id_counter += 1

print("| ID | Mid | Tweeter | Window | Spacing | Best Cross | Note |")
print("|----|-----|---------|--------|---------|------------|------|")
for p in new_pairings:
    print(f"| {p['ID']} | {p['Mid']} | {p['Tweeter']} | {p['Window']} | {p['Spacing']} | {p['Best Cross']} | {p['Note']} |")

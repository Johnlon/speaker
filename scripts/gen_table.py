
mids = [
    {"name": "DSA90-8", "od": 92.3, "beaming": 3260, "sens": 84.7, "price": 30, "mat": "Al"},
    {"name": "TCP115-8", "od": 116, "beaming": 2570, "sens": 81.9, "price": 12, "mat": "Paper"},
    {"name": "DS115-8", "od": 115.6, "beaming": 2636, "sens": 85.3, "price": 32, "mat": "Paper"},
    {"name": "HiVi B4N", "od": 116.5, "beaming": 2636, "sens": 85.0, "price": 20, "mat": "Paper"},
    {"name": "SB12PACR", "od": 122, "beaming": 2730, "sens": 87.0, "price": 24, "mat": "Al"},
    {"name": "SB12NRX", "od": 122, "beaming": 2730, "sens": 87.5, "price": 40, "mat": "Paper"},
    {"name": "SB12PFCR", "od": 122, "beaming": 2730, "sens": 87.5, "price": 21, "mat": "Paper"},
    {"name": "SB12MNRX2", "od": 123, "beaming": 2730, "sens": 91.0, "price": 48, "mat": "Paper"},
    {"name": "SIG150-4", "od": 152, "beaming": 1990, "sens": 91.1, "price": 37, "mat": "Al"},
    {"name": "SB13PFCR", "od": 130, "beaming": 2080, "sens": 89.0, "price": 25, "mat": "Paper"},
    {"name": "SLS-85", "od": 91, "beaming": 3000, "sens": 86.0, "price": 26, "mat": "Paper"},
    {"name": "RS125-4", "od": 125, "beaming": 2184, "sens": 89.9, "price": 58, "mat": "Al"},
    {"name": "RS125P", "od": 125, "beaming": 2184, "sens": 90.0, "price": 56, "mat": "Paper"},
    {"name": "HiVi M5N", "od": 130, "beaming": 2185, "sens": 87.0, "price": 26, "mat": "Paper"},
]

tweeters = [
    {"name": "SB19ST", "od": 88, "minx": 1960, "sens": 88.5, "price": 18, "type": "Wide"},
    {"name": "XT25TG", "od": 104, "minx": 880, "sens": 91.9, "price": 30, "type": "Ring"},
    {"name": "XT25BG", "od": 104.5, "minx": 1140, "sens": 92.6, "price": 37, "type": "Ring"},
    {"name": "XT25SC90", "od": 90, "minx": 1650, "sens": 90.1, "price": 18, "type": "Ring"},
    {"name": "XT25SC40", "od": 43.9, "minx": 2036, "sens": 94.0, "price": 26, "type": "Ring"},
    {"name": "XT19TD", "od": 94, "minx": 1640, "sens": 88.9, "price": 25, "type": "Ring"},
    {"name": "SB26ADC", "od": 104, "minx": 1360, "sens": 90.0, "price": 45, "type": "Dome"},
    {"name": "TN25", "od": 54, "minx": 3000, "sens": 91.0, "price": 22, "type": "Dome"},
    {"name": "TN28B", "od": 47.6, "minx": 2600, "sens": 90.0, "price": 47, "type": "Dome"},
    {"name": "ND25FA", "od": 66, "minx": 2700, "sens": 90.0, "price": 14, "type": "Dome"},
    {"name": "BC25SC06", "od": 70, "minx": 2700, "sens": 95.4, "price": 22, "type": "Dome"},
    {"name": "SB26STCN", "od": 72, "minx": 1900, "sens": 92.0, "price": 31, "type": "Dome"},
    {"name": "SB26ST", "od": 72, "minx": 1740, "sens": 91.0, "price": 27, "type": "Dome"},
    {"name": "RST28F", "od": 105, "minx": 1420, "sens": 93.5, "price": 41, "type": "Dome"},
    {"name": "DX25TG", "od": 104, "minx": 1180, "sens": 93.4, "price": 18, "type": "Dome"},
    {"name": "D2606", "od": 104, "minx": 2200, "sens": 91.4, "price": 29, "type": "Dome"},
    {"name": "D2604/833", "od": 104.2, "minx": 950, "sens": 93.0, "price": 36, "type": "Dome"},
    {"name": "D2604/830", "od": 104.2, "minx": 1260, "sens": 92.0, "price": 33, "type": "Dome"},
    {"name": "R2604/833", "od": 104, "minx": 880, "sens": 92.0, "price": 46, "type": "Ring"},
    {"name": "R2604/832", "od": 104, "minx": 1000, "sens": 90.0, "price": 39, "type": "Ring"},
    {"name": "H1189", "od": 103.8, "minx": 1100, "sens": 90.0, "price": 57, "type": "Dome"},
    {"name": "SB21RDCN", "od": 58, "minx": 1700, "sens": 89.5, "price": 42, "type": "Ring"},
    {"name": "SB21SDC", "od": 92, "minx": 1440, "sens": 91.0, "price": 35, "type": "Dome"},
    {"name": "SB29RDNC", "od": 104, "minx": 1160, "sens": 94.0, "price": 54, "type": "Ring"},
    {"name": "SB29SDAC", "od": 104, "minx": 1200, "sens": 93.0, "price": 34, "type": "Dome"},
    {"name": "MDT22T", "od": 54, "minx": 1300, "sens": 89.0, "price": 48, "type": "Dome"},
    {"name": "MDT12", "od": 54, "minx": 2000, "sens": 89.0, "price": 40, "type": "Dome"},
    {"name": "NE19VTS", "od": 52, "minx": 1540, "sens": 90.4, "price": 25, "type": "Wide"},
    {"name": "NE25VTS", "od": 66.3, "minx": 1460, "sens": 91.1, "price": 36, "type": "Wide"},
    {"name": "TD25F", "od": 93.5, "minx": 1800, "sens": 91.0, "price": 26, "type": "Dome"},
    {"name": "D27TG35", "od": 104, "minx": 1800, "sens": 91.8, "price": 35, "type": "Dome"},
]

new_pairings = []
id_counter = 1

for mid in mids:
    for twt in tweeters:
        win_low = max(twt['minx'], 150)
        win_high = mid['beaming']
        
        if win_high - win_low < 100:
            continue
            
        spacing = (mid['od'] + twt['od']) / 2
        price = mid['price'] + twt['price']
        
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
        mid_char = ""
        if mid['name'] in ["DSA90-8", "SIG150-4", "SB12PACR", "RS125-4"]:
            mid_char = "Aluminium detail"
        else:
            mid_char = "Natural warmth"
            
        twt_char = ""
        if twt['type'] == "Wide":
            twt_char = "Wide dispersion"
        elif twt['type'] == "Ring":
            twt_char = "Ring rad detail"
        else:
            twt_char = "Dome warmth"
            
        character = f"{mid_char} + {twt_char}"
        
        # Flags / Notes
        flags = []
        win_size = win_high - win_low
        if win_size > 1500: flags.append("Wide xover window")
        if win_size < 500: flags.append("Tight window")
        
        new_pairings.append({
            "ID": f"X{id_counter}",
            "Mid": mid['name'],
            "Tweeter": twt['name'],
            "Xover": f"{int(win_low)}–{int(win_high)}",
            "Spacing": f"{int(spacing)}",
            "Price": f"{price}",
            "PSU": psu,
            "Character": character,
            "Flags": ", ".join(flags)
        })
        id_counter += 1

output_file = r"C:\Users\johnl\.gemini\tmp\speaker\combos_final.md"
with open(output_file, 'w', encoding='utf-8') as f:
    f.write("| ID | Mid | Tweeter | Xover Hz | Spacing mm | Price £ | PSU (RMS/Burst) | Character | Flags / Notes |\n")
    f.write("|----|-----|---------|----------|------------|---------|-----------------|-----------|---------------|\n")
    for p in new_pairings[:319]:
        f.write(f"| {p['ID']} | {p['Mid']} | {p['Tweeter']} | {p['Xover']} | {p['Spacing']} | {p['Price']} | {p['PSU']} | {p['Character']} | {p['Flags']} |\n")

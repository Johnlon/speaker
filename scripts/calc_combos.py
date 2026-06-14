
mids = [
    {"name": "DSA90-8", "od": 92.3, "beam": 3260, "sens": 84.7, "imp": 8, "char": "Detailed"},
    {"name": "DS115-8", "od": 115.6, "beam": 2636, "sens": 85.3, "imp": 8, "char": "Warm"},
    {"name": "SB12PFCR25-4", "od": 122, "beam": 2730, "sens": 87.5, "imp": 4, "char": "Warm, natural"},
    {"name": "SIG120-4", "od": 123, "beam": 2570, "sens": 89.7, "imp": 4, "char": "Clear, dynamic"},
    {"name": "HiVi B4N", "od": 116.5, "beam": 2636, "sens": 85, "imp": 8, "char": "Warm gold"},
    {"name": "SIG150-4", "od": 152, "beam": 1990, "sens": 91.1, "imp": 4, "char": "Neutral"},
    {"name": "SB13PFCR25-4", "od": 130, "beam": 2080, "sens": 89, "imp": 4, "char": "Warm, nat. fibre"},
    {"name": "SLS-85S25CP04-04", "od": 91, "beam": 3000, "sens": 86, "imp": 4, "char": "Warm"}
]

tweeters = [
    {"name": "SB19ST", "od": 88, "minx": 1960, "sens": 88.5, "imp": 4, "type": "dome"},
    {"name": "XT25TG30-04", "od": 104, "minx": 880, "sens": 91.9, "imp": 4, "type": "ring"},
    {"name": "R2604/833000", "od": 104, "minx": 880, "sens": 92, "imp": 4, "type": "ring"},
    {"name": "D2604/833000", "od": 104.2, "minx": 950, "sens": 93, "imp": 4, "type": "dome"},
    {"name": "MDT22T", "od": 54, "minx": 1300, "sens": 89, "imp": 8, "type": "dome"},
    {"name": "SB21RDCN", "od": 58, "minx": 1700, "sens": 89.5, "imp": 4, "type": "ring dome"},
    {"name": "XT25SC40-04", "od": 43.9, "minx": 2036, "sens": 94, "imp": 4, "type": "ring"},
    {"name": "SB26ST-C000-5", "od": 72, "minx": 1740, "sens": 91, "imp": 5, "type": "dome"},
    {"name": "RST28F-4", "od": 105, "minx": 1420, "sens": 93.5, "imp": 4, "type": "dome"},
    {"name": "DX25TG59-04", "od": 104, "minx": 1180, "sens": 93.4, "imp": 4, "type": "dome"},
    {"name": "SB29RDNC", "od": 104, "minx": 1160, "sens": 94, "imp": 4, "type": "ring dome"},
    {"name": "NE19VTS-04", "od": 52, "minx": 1540, "sens": 90.4, "imp": 4, "type": "dome"},
    {"name": "MDT12", "od": 54, "minx": 2000, "sens": 89, "imp": 8, "type": "dome"}
]

# Existing pairings to check for duplicates
existing = [
    ("DS115-8", "SB19ST", "S1"),
    ("SB12PFCR25-4", "SB19ST", "S2"),
    ("HiVi B4N", "SB19ST", "A1"),
    ("DSA90-8", "SB19ST", "A3"),
    ("DS115-8", "DX25TG59-04", "A4"),
    ("SB12PFCR25-4", "DX25TG59-04", "A5"),
    ("SIG120-4", "SB19ST", "A8"),
    ("SIG150-4", "DX25TG59-04", "B8"),
    ("DS115-8", "XT25TG30-04", "RR1"),
    ("SB12PFCR25-4", "XT25TG30-04", "RR2"),
    ("SIG150-4", "XT25TG30-04", "RR5"),
    ("DS115-8", "NE25VTS-04", "NR2"),
    ("SB12PFCR25-4", "NE25VTS-04", "NR3"),
    ("DSA90-8", "XT25SC40-04", "XC1"),
    ("DS115-8", "XT25SC40-04", "XC2"),
    ("SB12PFCR25-4", "XT25SC40-04", "XC3"),
    ("DS115-8", "HiVi TN28-B", "TN2"),
    ("SB12PFCR25-4", "DA25BG08-06", "DA2"),
    ("SB13PFCR25-4", "DX25TG59-04", "R3"),
    ("DS115-8", "SB26ST-C000-5", "ST1"),
    ("SB12PFCR25-4", "SB26ST-C000-5", "ST2"),
    ("DSA90-8", "SB26ST-C000-5", "ST3"),
    ("DS115-8", "D2604/830000", "DC1"),
    ("SB12PFCR25-4", "D2604/830000", "DC2"),
    ("DS115-8", "TD25F-4", "TD2"),
    ("SB12PFCR25-4", "D27TG35-06", "DT2"),
    ("DS115-8", "BC25SC06-04", "BC2"),
    ("SB12PFCR25-4", "BC25SC06-04", "BC3"),
    ("DS115-8", "SB26STCN-C000-4", "STC2"),
    ("SB12PFCR25-4", "SB26STCN-C000-4", "STC3"),
    ("SB12PFCR25-4", "XT25BG60-04", "XBG2"),
    ("DSA90-8", "XT25BG60-04", "XBG3"),
    ("DS115-8", "SB29RDNC-C000-4", "RPN1"),
    ("SB12PFCR25-4", "SB29RDNC-C000-4", "RPN2"),
    ("DSA90-8", "SB29RDNC-C000-4", "RPN4"),
    ("DS115-8", "RST28F-4", "RST1"),
    ("SB12PFCR25-4", "RST28F-4", "RST2"),
    ("DSA90-8", "RST28F-4", "RST3"),
    ("DSA90-8", "D2606/920000", "D26_1"),
    ("DS115-8", "D2606/920000", "D26_2"),
    ("SB12PFCR25-4", "D2606/920000", "D26_3"),
    ("SB13PFCR25-4", "XT25TG30-04", "SB13_TG"),
    ("SB13PFCR25-4", "D2604/830000", "SB13_DC"),
    ("SB13PFCR25-4", "SB29RDNC-C000-4", "SB13_RPN"),
    ("HiVi B4N", "XT25TG30-04", "B_TG"),
    ("HiVi B4N", "SB26STCN-C000-4", "B_STC"),
    ("HiVi B4N", "D2604/830000", "B_DC"),
    ("DSA90-8", "R2604/833000", "RP1"),
    ("DS115-8", "R2604/833000", "RP2"),
    ("SB12PFCR25-4", "R2604/833000", "RP3"),
    ("DSA90-8", "SB21RDCN-C000-4", "XCR1"),
    ("DS115-8", "SB21RDCN-C000-4", "XCR2"),
    ("SB12PFCR25-4", "SB21RDCN-C000-4", "XCR3"),
    ("DSA90-8", "D2604/833000", "D6R1"),
    ("DS115-8", "D2604/833000", "D6R2"),
    ("SB12PFCR25-4", "D2604/833000", "D6R3"),
    ("DSA90-8", "MDT22T", "MDT22_1"),
    ("DS115-8", "MDT22T", "MDT22_2"),
    ("SB12PFCR25-4", "MDT22T", "MDT22_3"),
]

def normalize(name):
    return name.split("-")[0].split("/")[0].replace("C000", "").replace("04", "").replace("8", "").strip()

existing_lookup = {(m, t): id for m, t, id in existing}
# Add variants for SB29RDNC
existing_lookup[("DS115-8", "SB29RDNC")] = "RPN1"
existing_lookup[("SB12PFCR25-4", "SB29RDNC")] = "RPN2"
existing_lookup[("DSA90-8", "SB29RDNC")] = "RPN4"
existing_lookup[("SB13PFCR25-4", "SB29RDNC")] = "SB13_RPN"
existing_lookup[("DSA90-8", "SB21RDCN")] = "XCR1"
existing_lookup[("DS115-8", "SB21RDCN")] = "XCR2"
existing_lookup[("SB12PFCR25-4", "SB21RDCN")] = "XCR3"

results = []
new_id_counter = 1

def get_best_xover(minx, beam):
    if minx <= 2500 <= beam:
        return 2500
    return round((minx + beam) / 2)

for mid in mids:
    for twt in tweeters:
        window_width = mid["beam"] - twt["minx"]
        if window_width >= 100:
            spacing = round((mid["od"] + twt["od"]) / 2)
            xover = get_best_xover(twt["minx"], mid["beam"])
            
            pair_key = (mid["name"], twt["name"])
            pair_id = existing_lookup.get(pair_key)

            note = ""
            if window_width > 1000:
                note += "Wide window (good). "
            elif window_width < 300:
                note += "Tight window (distortion risk). "
            
            if twt["type"] == "ring":
                note += "Ring radiator advantage. "
            elif twt["type"] == "ring dome":
                note += "Ring dome advantage. "
            
            if "natural" in mid["char"] or "fibre" in mid["char"]:
                note += "Natural fiber mid warmth. "
            elif "Warm" in mid["char"]:
                note += "Paper mid warmth. "
            
            results.append({
                "ID": pair_id,
                "Mid": mid["name"],
                "Tweeter": twt["name"],
                "Window": f"{twt['minx']}\u2013{mid['beam']}",
                "Spacing": spacing,
                "BestX": xover,
                "Note": note.strip()
            })

print("| ID | Mid | Tweeter | Xover Window (Hz) | Spacing (mm) | Best Crossover (Hz) | Quality / Distortion / Note |")
print("|----|-----|---------|-------------------|--------------|---------------------|----------------------------|")
for r in results:
    pid = r["ID"] if r["ID"] else f"M{new_id_counter}"
    if not r["ID"]: new_id_counter += 1
    print(f"| {pid} | {r['Mid']} | {r['Tweeter']} | {r['Window']} | {r['Spacing']} | {r['BestX']} | {r['Note']} |")

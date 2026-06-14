
mids_data = [
    ("DSA90-8", 3260), ("TCP115-8", 2570), ("DS115-8", 2636), ("HiVi B4N", 2636), ("SB12PACR", 2730),
    ("SB12NRX", 2730), ("SB12PFCR", 2730), ("SB12MNRX2", 2730), ("SIG150-4", 1990), ("SB13PFCR", 2080),
    ("SLS-85", 3000), ("RS125-4", 2184), ("RS125P", 2184), ("HiVi M5N", 2185)
]

tweeters_data = [
    ("SB19ST", 1960), ("XT25TG", 880), ("XT25BG", 1140), ("XT25SC90", 1650), ("XT25SC40", 2036),
    ("XT19TD", 1640), ("SB26ADC", 1360), ("TN25", 3000), ("TN28B", 2600), ("ND25FA", 2700),
    ("BC25SC06", 2700), ("SB26STCN", 1900), ("SB26ST", 1740), ("RST28F", 1420), ("DX25TG", 1180),
    ("D2606", 2200), ("D2604/833", 950), ("D2604/830", 1260), ("R2604/833", 880), ("R2604/832", 1000),
    ("H1189", 1100), ("SB21RDCN", 1700), ("SB21SDC", 1440), ("SB29RDNC", 1160), ("SB29SDAC", 1200),
    ("MDT22T", 1300), ("MDT12", 2000), ("NE19VTS", 1540), ("NE25VTS", 1460), ("TD25F", 1800), ("D27TG35", 1800)
]

total = 0
invalid = 0
for mid_name, beaming in mids_data:
    for twt_name, minx in tweeters_data:
        total += 1
        if beaming - max(minx, 150) < 100:
            invalid += 1

print(f"Total: {total}")
print(f"Invalid (window < 100): {invalid}")
print(f"Total - Invalid: {total - invalid}")

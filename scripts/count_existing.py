
import re

mids_list = ["DSA90-8", "TCP115-8", "DS115-8", "HIVI B4N", "SB12PACR", "SB12NRX", "SB12PFCR", "SB12MNRX2", "SIG150-4", "SB13PFCR", "SLS-85", "RS125-4", "RS125P", "HIVI M5N"]
tweeters_list = ["SB19ST", "XT25TG", "XT25BG", "XT25SC90", "XT25SC40", "XT19TD", "SB26ADC", "TN25", "TN28B", "ND25FA", "BC25SC06", "SB26STCN", "SB26ST", "RST28F", "DX25TG", "D2606", "D2604/833", "D2604/830", "R2604/833", "R2604/832", "H1189", "SB21RDCN", "SB21SDC", "SB29RDNC", "SB29SDAC", "MDT22T", "MDT12", "NE19VTS", "NE25VTS", "TD25F", "D27TG35"]

def normalize(name):
    name = name.upper()
    # Remove common suffixes/prefixes
    name = name.replace("-8", "").replace("-4", "").replace("-04", "").replace("-06", "").replace("/833000", "").replace("/830000", "").replace("/920000", "")
    name = name.replace("25-4", "").replace("25-8", "").replace("25-4", "")
    name = name.replace("C000", "").replace("-C000-4", "").replace("-C000-5", "")
    name = name.replace("XT25TG30", "XT25TG").replace("DX25TG59", "DX25TG").replace("XT25SC90-04", "XT25SC90")
    name = name.replace("XT25BG60", "XT25BG").replace("XT25SC40-04", "XT25SC40").replace("XT19TD00", "XT19TD")
    name = name.replace("SB29RDNC", "SB29RDNC").replace("SB21RDCN", "SB21RDCN").replace("SB21SDC", "SB21SDC")
    name = name.replace("ND25FA", "ND25FA").replace("BC25SC06", "BC25SC06")
    name = name.replace("H1189-06", "H1189").replace("D2604/833", "D2604/833").replace("D2604/830", "D2604/830")
    name = name.replace("R2604/833", "R2604/833").replace("R2604/832", "R2604/832")
    name = name.replace("SB12PFCR25", "SB12PFCR").replace("SB12MNRX2-25", "SB12MNRX2").replace("SB12NRX25", "SB12NRX")
    name = name.replace("SB13PFCR25", "SB13PFCR").replace("SB13PFC25", "SB13PFCR")
    name = name.replace("SLS-85S25CP04", "SLS-85")
    return name.strip()

norm_mids = [normalize(m) for m in mids_list]
norm_tweeters = [normalize(t) for t in tweeters_list]

with open(r"C:\Users\johnl\work\speaker\combos.md", 'r', encoding='utf-8') as f:
    content = f.read()

matches = re.findall(r"\| ([^|]+) \| ([^|]+) \| ([^|]+) \|", content)
count = 0
found_pairs = set()
for rid, m, t in matches:
    if m.strip() == "Mid": continue
    nm = normalize(m.strip())
    nt = normalize(t.strip())
    
    # Check if nm matches any in norm_mids
    mid_match = any(nm.startswith(nm_target) or nm_target.startswith(nm) for nm_target in norm_mids)
    twt_match = any(nt.startswith(nt_target) or nt_target.startswith(nt) for nt_target in norm_tweeters)
    
    if mid_match and twt_match:
        count += 1
        found_pairs.add((nm, nt))

print(f"Total existing pairings in pool: {count}")
print(f"Unique existing pairings in pool: {len(found_pairs)}")

import re

beaming_limits = {
    "DSA90-8": 3260,
    "SB12PFCR25-4": 2730,
    "SB12PFCR": 2730,
    "SB12MNRX2-25-4": 2730,
    "DS115-8": 2636,
    "HiVi B4N": 2636,
    "DMA105-8": 2900,
    "SPM-116/8": 2600,
    "Beyma 4FR40": 2600,
    "DA115-8": 2600,
    "TCP115-8": 2570,
    "SIG120-4": 2570,
    "Tang Band W4-655F": 2636,
    "RS125-4": 2184,
    "HiVi M5N": 2185,
    "SB13PFC25-4": 2080,
    "SB13PFC25-8": 2080,
    "SB13PFCR25-4": 2080,
    "SDS-P830656": 2080,
    "SIG150-4": 1990,
    "SLS-85S25CP04-04": 3000,
    "SB12PACR25-4-COAX": 2730,
    "SB12PFC25-4-COAX": 2730,
    "ND91-4": 3000,
    "RS100-8": 2900,
    "PA130-8": 2000,
    "TF0510": 2200,
    "PLUVIA-7HD Gold": 2900,
    "SB12NRX25-4": 2730,
}

tweeter_minx = {
    "SB19ST": 1960,
    "DX25TG59-04": 1180,
    "XT25TG30-04": 880,
    "XT25SC90-04": 1650,
    "SB29SDAC": 1200,
    "HiVi TN25": 3000,
    "ND25FA-4": 2700,
    "DT-28N": 2400,
    "XT25SC40-04": 2036,
    "HiVi TN28-B": 2600,
    "DA25BG08-06": 1420,
    "SB21SDC-C000-4": 1440,
    "SB26ST-C000-5": 1740,
    "D2604/830000": 1260,
    "SEAS H1406-04": 2340,
    "CF18N-4": 2200,
    "TD25F-4": 1800,
    "D27TG35-06": 1800,
    "BC25SC06-04": 2700,
    "SB26STCN-C000-4": 1900,
    "SB26ADC-C000-4": 1360,
    "XT25BG60-04": 1140,
    "SB29RDNC-C000-4": 1160,
    "RST28F-4": 1420,
    "D2606/920000": 2200,
    "R2604/833000": 880,
    "R2604/832000": 1000,
    "H1189-06": 1100,
    "SB21RDCN-C000-4": 1700,
    "MDT22T": 1300,
    "Markaudio TW 6": 3400,
    "(built-in)": 2600, # Coax
}

def clean_val(v):
    return v.strip().replace(",", "").replace("~", "")

def parse_row(line):
    parts = [p.strip() for p in line.split("|")]
    if len(parts) < 10: return None
    return parts[1:10]

def process_old_row(row):
    id, mid, tweeter, xover, spacing, price, psu, character, notes = row
    
    if "–" in xover or "-" in xover:
        window = xover.replace("-", "–")
        m = re.match(r"([\d,~]+)\s*[–-]\s*([\d,~]+)", window)
        if m:
            low = int(clean_val(m.group(1)))
            high = int(clean_val(m.group(2)))
            if low <= 2500 <= high:
                best = 2500
            else:
                best = round((low + high) / 2)
        else:
            best = clean_val(xover)
    else:
        best = clean_val(xover)
        # Derive window
        m_limit = beaming_limits.get(mid, 2600)
        t_limit = tweeter_minx.get(tweeter, 2000)
        if tweeter == "(built-in)":
            if mid == "SB12PACR25-4-COAX": t_limit = 2600; m_limit = 2730
            elif mid == "SB12PFC25-4-COAX": t_limit = 2600; m_limit = 2730
        
        if t_limit < m_limit:
            window = f"{t_limit:,}–{m_limit:,}"
        else:
            window = f"{best} (Fixed)"
            
    try:
        best_str = f"{int(best):,}"
    except:
        best_str = str(best)
        
    return [id, mid, tweeter, window, best_str, spacing, price, psu, character, notes]

# We need to read the ORIGINAL IDs from the original file before we overwrite it or from the content we have.
# Since we already overwrote combos.md once, let's use the old_ids we extracted in the previous turn if possible,
# or just redefine them based on the current state of combos.md but filtered for non-X IDs.

with open(r"C:\Users\johnl\work\speaker\combos.md", "r", encoding="utf-8") as f:
    current_content = f.read()

with open(r"C:\Users\johnl\.gemini\tmp\speaker\combos_complete.md", "r", encoding="utf-8") as f:
    new_rows_content = f.read()

# All Pairing IDs from current content that are NOT X1-X319
# Actually, the original order was S, A, B, RR, C, NR, RD, XC, TN, DA, R, COAX, ST, NX, PL, DC, SE, CF, TD, DT, BC, STC, AL, XBG, RPN, RST, D26, SB13, M, B, DA, XT19, DMA, RP, TF, XCR, D6R, MDT22
# This is getting complex. Let's just say anything in the current file that ISN'T X1-X319 is "existing".

pairings_section = re.search(r"## All Pairings\s+PSU =.*?\n\n(.*?)(?=\n\n---|\s*$)", current_content, re.DOTALL)
table_lines = pairings_section.group(1).splitlines()
all_processed = []
existing_ids = []
for line in table_lines:
    if line.startswith("| ID |") or line.startswith("|----|") or not line.strip():
        continue
    parts = [p.strip() for p in line.split("|")]
    if len(parts) >= 11:
        row = parts[1:11]
        id = row[0]
        # If it's an X-number ID, we'll re-process it from the new_rows to be safe, or just keep it.
        # But we want to separate "Old" (S1...) from "New" (X1...).
        # Wait, the current file already has merged data.
        if id.startswith("X") and id[1:].isdigit() and 1 <= int(id[1:]) <= 319:
            continue 
        all_processed.append(row)
        existing_ids.append(id)

# Now add the new rows from combos_complete.md
new_rows = []
for line in new_rows_content.splitlines():
    if line.startswith("| ID |") or line.startswith("|----|") or not line.strip():
        continue
    parts = [p.strip() for p in line.split("|")]
    if len(parts) >= 11:
        new_rows.append(parts[1:11])

all_rows = all_processed + new_rows

def sort_key(row):
    id = row[0]
    if id in existing_ids:
        return (0, existing_ids.index(id), "")
    if id.startswith("X") and id[1:].isdigit():
        return (1, int(id[1:]), "")
    return (2, 0, id)

all_rows.sort(key=sort_key)

header = "| ID | Mid | Tweeter | Xover Window (Hz) | Best Cross (Hz) | Spacing mm | Price £ | PSU (RMS/Burst) | Character | Flags / Notes |"
separator = "|----|-----|---------|-------------------|-----------------|------------|---------|-----------------|-----------|---------------|"
table_str = header + "\n" + separator + "\n"
for r in all_rows:
    table_str += "| " + " | ".join(r) + " |\n"

new_all_pairings = f"## All Pairings\n\nPSU = \"RMS min / Burst min\". `*` = mid reaches ~100.3 dB max even at 36V (JAB5 ceiling) — 1 dB short of sub burst.\n\n{table_str}"

final_content = re.sub(r"## All Pairings\s+PSU =.*?(?=\n\n---|\s*$)", new_all_pairings, current_content, flags=re.DOTALL)

with open(r"C:\Users\johnl\work\speaker\combos.md", "w", encoding="utf-8") as f:
    f.write(final_content)

print("Successfully updated combos.md with correct sorting")

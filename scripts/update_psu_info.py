import re
import sys

# Reconfigure stdout to use UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# Fallback specs for known drivers if they are not in drivers.md or are missing specs
known_mids = {
    "DSA90-8": {"imp": 8, "sens": 84.7},
    "TCP115-8": {"imp": 8, "sens": 81.9},
    "DS115-8": {"imp": 8, "sens": 85.3},
    "HiVi B4N": {"imp": 8, "sens": 85.0},
    "SB12PACR": {"imp": 4, "sens": 87.0},
    "SB12NRX": {"imp": 4, "sens": 87.5},
    "SB12PFCR": {"imp": 4, "sens": 87.5},
    "SB12MNRX2": {"imp": 4, "sens": 91.0},
    "SIG150-4": {"imp": 4, "sens": 91.1},
    "SB13PFCR": {"imp": 4, "sens": 89.0},
    "SLS-85": {"imp": 4, "sens": 86.0},
    "RS125-4": {"imp": 4, "sens": 89.9},
    "RS125P": {"imp": 4, "sens": 90.0},
    "HiVi M5N": {"imp": 8, "sens": 87.0},
    "SIG120-4": {"imp": 4, "sens": 89.7},
    "DMA105-8": {"imp": 8, "sens": 84.8},
    "SPM-116/8": {"imp": 8, "sens": 84.0},
    "Beyma 4FR40": {"imp": 8, "sens": 87.0},
    "DA115-8": {"imp": 8, "sens": 84.9},
    "RS100-8": {"imp": 8, "sens": 84.6},
    "PA130-8": {"imp": 8, "sens": 88.2},
    "TF0510": {"imp": 8, "sens": 91.0},
    "PLUVIA-7HD": {"imp": 8, "sens": 85.7},
    "SB12PACR25-4-COAX": {"imp": 4, "sens": 87.5},
    "SB12PFC25-4-COAX": {"imp": 4, "sens": 87.5},
    "SB12NRX25-4": {"imp": 4, "sens": 87.5},
}

known_tweeters = {
    "SB19ST": {"imp": 4, "sens": 88.5},
    "XT25TG": {"imp": 4, "sens": 91.9},
    "XT25BG": {"imp": 4, "sens": 92.6},
    "XT25SC90": {"imp": 4, "sens": 90.1},
    "SB29SDAC": {"imp": 4, "sens": 91.0},
    "HiVi TN25": {"imp": 5, "sens": 91.0},
    "ND25FA": {"imp": 4, "sens": 90.0},
    "DT-28N": {"imp": 8, "sens": 92.0},
    "XT25SC40": {"imp": 4, "sens": 94.0},
    "HiVi TN28-B": {"imp": 6, "sens": 90.0},
    "TN28B": {"imp": 6, "sens": 90.0},
    "DA25BG08-06": {"imp": 6, "sens": 91.6},
    "SB21SDC": {"imp": 4, "sens": 91.0},
    "SB26ST-C000-5": {"imp": 5, "sens": 91.0},
    "SB26ST": {"imp": 5, "sens": 91.0},
    "D2604/830000": {"imp": 4, "sens": 92.0},
    "D2604/830": {"imp": 4, "sens": 92.0},
    "SEAS H1406-04": {"imp": 4, "sens": 91.0},
    "CF18N-4": {"imp": 4, "sens": 90.0},
    "TD25F-4": {"imp": 4, "sens": 91.0},
    "TD25F": {"imp": 4, "sens": 91.0},
    "D27TG35-06": {"imp": 6, "sens": 91.8},
    "D27TG35": {"imp": 6, "sens": 91.8},
    "BC25SC06-04": {"imp": 4, "sens": 95.4},
    "BC25SC06": {"imp": 4, "sens": 95.4},
    "SB26STCN-C000-4": {"imp": 4, "sens": 92.0},
    "SB26STCN": {"imp": 4, "sens": 92.0},
    "SB26ADC-C000-4": {"imp": 4, "sens": 90.0},
    "SB26ADC": {"imp": 4, "sens": 90.0},
    "XT25BG60-04": {"imp": 4, "sens": 92.6},
    "SB29RDNC-C000-4": {"imp": 4, "sens": 94.0},
    "SB29RDNC": {"imp": 4, "sens": 94.0},
    "RST28F-4": {"imp": 4, "sens": 93.5},
    "RST28F": {"imp": 4, "sens": 93.5},
    "D2606/920000": {"imp": 6, "sens": 91.4},
    "D2606": {"imp": 6, "sens": 91.4},
    "R2604/833000": {"imp": 4, "sens": 92.0},
    "R2604/833": {"imp": 4, "sens": 92.0},
    "R2604/832000": {"imp": 4, "sens": 90.0},
    "R2604/832": {"imp": 4, "sens": 90.0},
    "H1189-06": {"imp": 6, "sens": 90.0},
    "H1189": {"imp": 6, "sens": 90.0},
    "SB21RDCN-C000-4": {"imp": 4, "sens": 89.5},
    "SB21RDCN": {"imp": 4, "sens": 89.5},
    "MDT22T": {"imp": 8, "sens": 89.0},
    "Markaudio TW 6": {"imp": 4, "sens": 98.0},
    "NE19VTS": {"imp": 4, "sens": 90.4},
    "NE25VTS": {"imp": 4, "sens": 91.1},
    "MDT12": {"imp": 8, "sens": 89.0},
    "(built-in)": {"imp": 4, "sens": 87.5},
    "built-in": {"imp": 4, "sens": 87.5},
}

def parse_drivers(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    entries = re.split(r'\n### ', content)
    
    drivers = {}
    for entry in entries[1:]:
        lines = entry.split('\n')
        name_line = lines[0]
        name = name_line.split('—')[0].split('(')[0].strip()
        
        imp_match = re.search(r'Impedance:\s*(?:\*\*)?([\d.]+)(?:\*\*)?\s*Ω', entry, re.IGNORECASE)
        sens_match = re.search(r'Sensitivity:\s*(?:\*\*)?([\d.]+)(?:\*\*)?\s*dB', entry, re.IGNORECASE)
        
        if not imp_match:
            imp_match = re.search(r'(\d+)\s*Ω\s*impedance', entry, re.IGNORECASE)
        if not imp_match:
            imp_match = re.search(r'imp:\s*(\d+)\s*Ω', entry, re.IGNORECASE)
            
        if not sens_match:
            sens_match = re.search(r'sens(?:itivity)?:\s*(?:\*\*)?([\d.]+)(?:\*\*)?\s*dB', entry, re.IGNORECASE)
            
        if imp_match or sens_match:
            imp = float(imp_match.group(1)) if imp_match else None
            sens = float(sens_match.group(1)) if sens_match else None
            drivers[name] = {"imp": imp, "sens": sens}
            
    return drivers

def normalize_name(name):
    for prefix in ["SB Acoustics", "Dayton Audio", "Peerless by Tymphany", "HiVi Swan", "Scan-Speak", "Morel", "SEAS", "Visaton", "Monacor", "Celestion", "HiVi"]:
        name = name.replace(prefix, "")
    return re.sub(r'[^a-zA-Z0-9]', '', name).lower()

def find_driver(name, parsed_drivers, is_tweeter=False):
    norm = normalize_name(name)
    for k, v in parsed_drivers.items():
        if normalize_name(k) == norm:
            if v.get("imp") and v.get("sens"):
                return v
    for k, v in parsed_drivers.items():
        nk = normalize_name(k)
        if norm in nk or nk in norm:
            if v.get("imp") and v.get("sens"):
                return v
    lookup = known_tweeters if is_tweeter else known_mids
    for k, v in lookup.items():
        if normalize_name(k) == norm:
            return v
    for k, v in lookup.items():
        nk = normalize_name(k)
        if norm in nk or nk in norm:
            return v
    return None

def calc_psu_current_and_power(mid_specs, twt_specs, v_rms, v_burst):
    p_sub_rms = 40.0
    p_mid_rms = (8.0 / mid_specs["imp"]) * 10**((98.0 - mid_specs["sens"]) / 10.0)
    p_twt_rms = (8.0 / twt_specs["imp"]) * 10**((98.0 - twt_specs["sens"]) / 10.0)
    
    i_idle = 0.5
    
    i_rms = (p_sub_rms + p_mid_rms + p_twt_rms) / v_rms + i_idle
    p_rms = v_rms * i_rms
    
    p_sub_burst = 80.0
    i_burst = (p_sub_burst + p_mid_rms + p_twt_rms) / v_burst + i_idle
    p_burst = v_burst * i_burst
    
    return i_rms, p_rms, i_burst, p_burst

def update_combos(combos_path, parsed_drivers):
    with open(combos_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    new_lines = []
    in_table = False
    
    # Store mappings for solutions.md lookup
    pairings_psu_by_id = {}
    pairings_psu_by_names = {}
    
    for line in lines:
        if line.startswith('|') and 'ID' in line:
            in_table = True
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 9:
                parts[8] = "PSU V/A/W (RMS/Burst)"
                new_lines.append(" | ".join(parts).strip() + "\n")
            else:
                new_lines.append(line)
            continue
            
        if in_table and line.startswith('|---'):
            new_lines.append(line)
            continue
            
        if in_table and line.startswith('|'):
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 11:
                pair_id = parts[1]
                mid_name = parts[2]
                twt_name = parts[3]
                psu_col = parts[8]
                
                # Parse voltages
                volt_matches = re.findall(r'(\d+)\s*V', psu_col, re.IGNORECASE)
                if len(volt_matches) >= 2:
                    v_rms = int(volt_matches[0])
                    v_burst = int(volt_matches[1])
                elif len(volt_matches) == 1:
                    v_rms = int(volt_matches[0])
                    v_burst = 28 # fallback
                else:
                    v_rms = 24
                    v_burst = 28
                
                mid_specs = find_driver(mid_name, parsed_drivers, is_tweeter=False)
                twt_specs = find_driver(twt_name, parsed_drivers, is_tweeter=True)
                
                if mid_specs and twt_specs:
                    i_rms, p_rms, i_burst, p_burst = calc_psu_current_and_power(mid_specs, twt_specs, v_rms, v_burst)
                    
                    has_star = '*' in psu_col
                    star_str = '*' if has_star else ''
                    
                    # V/A/W (RMS/Burst) format
                    psu_str = f"{v_rms}V/{i_rms:.1f}A/{int(round(p_rms))}W / {v_burst}V/{i_burst:.1f}A/{int(round(p_burst))}W{star_str}"
                    parts[8] = psu_str
                    
                    # Store mappings
                    pairings_psu_by_id[pair_id] = psu_str
                    pairings_psu_by_names[(normalize_name(mid_name), normalize_name(twt_name))] = psu_str
                else:
                    print(f"Warning: Could not find specs for pairing {pair_id}: Mid '{mid_name}' ({mid_specs}), Twt '{twt_name}' ({twt_specs})")
                
                new_lines.append(" | ".join(parts).strip() + "\n")
            else:
                new_lines.append(line)
        else:
            if in_table and not line.strip():
                in_table = False
            new_lines.append(line)
            
    with open(combos_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
        
    print(f"Successfully updated combos.md. Parsed {len(pairings_psu_by_id)} pairings.")
    return pairings_psu_by_id, pairings_psu_by_names

def update_solutions(solutions_path, pairings_psu_by_id, pairings_psu_by_names):
    with open(solutions_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    lines = content.split('\n')
    new_lines = []
    
    in_table = False
    psu_idx = -1
    id_idx = -1
    combo_idx = -1
    pairing_idx = -1
    
    for line in lines:
        if line.startswith('|') and 'PSU' in line:
            in_table = True
            parts = [p.strip() for p in line.split('|')]
            psu_idx = -1
            id_idx = -1
            combo_idx = -1
            pairing_idx = -1
            for idx, part in enumerate(parts):
                if part == "PSU":
                    psu_idx = idx
                elif part == "ID":
                    id_idx = idx
                elif part == "Combo":
                    combo_idx = idx
                elif part == "Pairing":
                    pairing_idx = idx
            
            new_lines.append(line)
            continue
            
        if in_table and line.startswith('|---'):
            new_lines.append(line)
            continue
            
        if in_table and line.startswith('|'):
            parts = [p.strip() for p in line.split('|')]
            if len(parts) > psu_idx:
                pair_id = None
                mid_twt_key = None
                
                # Check for explicit ID
                if id_idx != -1 and id_idx < len(parts):
                    pair_id = parts[id_idx].replace('**', '').strip()
                
                # Check for pairing name-based matches in Pairing or Combo column
                search_col = None
                if pairing_idx != -1 and pairing_idx < len(parts):
                    search_col = parts[pairing_idx]
                elif combo_idx != -1 and combo_idx < len(parts):
                    search_col = parts[combo_idx]
                    
                if search_col:
                    search_col_clean = search_col.replace('**', '').strip()
                    # Try to find ID in parentheses first
                    m = re.search(r'\(([^)]+)\)', search_col_clean)
                    if m:
                        pair_id = m.group(1).strip()
                    else:
                        # Split by + and find matched drivers
                        driver_parts = search_col_clean.split('+')
                        if len(driver_parts) >= 2:
                            mid_candidate = driver_parts[0].strip()
                            twt_candidate = driver_parts[1].strip()
                            
                            # Let's see if we can resolve these candidates
                            resolved_mid = find_driver(mid_candidate, {}, is_tweeter=False)
                            resolved_twt = find_driver(twt_candidate, {}, is_tweeter=True)
                            
                            # Find matching keys in the dictionary of known mids/tweeters
                            norm_mid_cand = None
                            for k in known_mids.keys():
                                if normalize_name(k) in normalize_name(mid_candidate) or normalize_name(mid_candidate) in normalize_name(k):
                                    norm_mid_cand = normalize_name(k)
                                    break
                            norm_twt_cand = None
                            for k in known_tweeters.keys():
                                if normalize_name(k) in normalize_name(twt_candidate) or normalize_name(twt_candidate) in normalize_name(k):
                                    norm_twt_cand = normalize_name(k)
                                    break
                                    
                            if norm_mid_cand and norm_twt_cand:
                                mid_twt_key = (norm_mid_cand, norm_twt_cand)
                
                new_psu_str = None
                if pair_id and pair_id in pairings_psu_by_id:
                    new_psu_str = pairings_psu_by_id[pair_id]
                elif mid_twt_key and mid_twt_key in pairings_psu_by_names:
                    new_psu_str = pairings_psu_by_names[mid_twt_key]
                elif search_col:
                    # Fallback search through all combos names
                    norm_col = normalize_name(search_col)
                    for (mn, tn), psu_val in pairings_psu_by_names.items():
                        if mn in norm_col and tn in norm_col:
                            new_psu_str = psu_val
                            break
                            
                if new_psu_str:
                    parts[psu_idx] = new_psu_str
                    new_lines.append(" | ".join(parts).strip())
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)
        else:
            if in_table and not line.strip():
                in_table = False
            new_lines.append(line)
            
    with open(solutions_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))
        
    print("Successfully updated solutions.md with calculated PSU current & power values.")

if __name__ == '__main__':
    parsed = parse_drivers(r'C:\Users\johnl\work\speaker\drivers.md')
    by_id, by_names = update_combos(r'C:\Users\johnl\work\speaker\combos.md', parsed)
    update_solutions(r'C:\Users\johnl\work\speaker\solutions.md', by_id, by_names)

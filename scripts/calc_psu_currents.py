import re

def parse_drivers(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all driver entries starting with ###
    entries = re.split(r'\n### ', content)
    
    drivers = {}
    for entry in entries[1:]:
        lines = entry.split('\n')
        name_line = lines[0]
        # Clean name: remove things after "—" or "candidate" etc.
        name = name_line.split('—')[0].split('(')[0].strip()
        
        # Search for Impedance and Sensitivity in the entry
        imp_match = re.search(r'Impedance:\s*([\d.]+)\s*Ω', entry, re.IGNORECASE)
        sens_match = re.search(r'Sensitivity:\s*([\d.]+)\s*dB', entry, re.IGNORECASE)
        
        # Fallback patterns
        if not imp_match:
            imp_match = re.search(r'(\d+)\s*Ω\s*impedance', entry, re.IGNORECASE)
        if not imp_match:
            imp_match = re.search(r'imp:\s*(\d+)\s*Ω', entry, re.IGNORECASE)
            
        if not sens_match:
            sens_match = re.search(r'sens(?:itivity)?:\s*([\d.]+)\s*dB', entry, re.IGNORECASE)
            
        if imp_match or sens_match:
            imp = float(imp_match.group(1)) if imp_match else None
            sens = float(sens_match.group(1)) if sens_match else None
            drivers[name] = {"imp": imp, "sens": sens}
            
    return drivers

if __name__ == '__main__':
    drivers = parse_drivers(r'C:\Users\johnl\work\speaker\drivers.md')
    print(f"Extracted {len(drivers)} drivers:")
    for name, specs in sorted(drivers.items()):
        print(f"  {name}: {specs}")

"""Fix stale hivi_b4n_1 local paths in drivers.json."""
import json, sys
from pathlib import Path

def p(s=''): sys.stdout.buffer.write((str(s)+'\n').encode('utf-8', errors='replace'))

data = json.loads(Path('drivers.json').read_text(encoding='utf-8'))

for drv in data['drivers']:
    if drv.get('id') != 'hivi-swan-b4n':
        continue
    p(f"Before: {drv.get('datasheets')}")
    # Two datasheets: first page is hivi_b4n.pdf, second is hivi_b4n_2.pdf
    # Both source URLs were for the same driver, just two attached PDFs
    new_sheets = []
    seen = set()
    for sheet in drv.get('datasheets', []):
        if isinstance(sheet, dict):
            local = sheet.get('local', '')
            if 'hivi_b4n_1' in local:
                sheet = dict(sheet, local='research/hivi_b4n.pdf')
            elif 'hivi_b4n_2' in local or 'hivi_b4n_datasheet_2' in local:
                sheet = dict(sheet, local='research/hivi_b4n_2.pdf')
        # Deduplicate sheets by local path
        key = sheet.get('local') if isinstance(sheet, dict) else sheet
        if key not in seen:
            seen.add(key)
            new_sheets.append(sheet)
    drv['datasheets'] = new_sheets
    p(f"After:  {drv.get('datasheets')}")

Path('drivers.json').write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')

# Final check
data2 = json.loads(Path('drivers.json').read_text(encoding='utf-8'))
missing = []
for drv in data2['drivers']:
    for sheet in drv.get('datasheets', []):
        if isinstance(sheet, dict) and 'local' in sheet:
            if not Path(sheet['local']).exists():
                missing.append(f"{drv['id']}: {sheet['local']}")
if missing:
    p("Still MISSING:")
    for m in missing: p(f"  {m}")
else:
    p("All local paths OK.")

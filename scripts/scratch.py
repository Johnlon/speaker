"""Add RST28A-4 datasheet URL and source to entry."""
import json, sys
from pathlib import Path
def p(s): sys.stdout.buffer.write((s+'\n').encode('utf-8', errors='replace'))
path = Path('drivers.json')
src = json.loads(path.read_text(encoding='utf-8'))
d = next(x for x in src['drivers'] if x['id'] == 'dayton-audio-rs28a-4')
d.setdefault('sources', [])
d.setdefault('datasheets', [])
d.setdefault('prices', [])
if not any('daytonaudio' in s for s in d['sources']):
    d['sources'].append('https://www.daytonaudio.com/product/1565/rst28a-4-1-1-8-reference-series-aluminum-dome-tweeter-4-ohm')
if not any('rst28a' in str(s).lower() for s in d['datasheets']):
    d['datasheets'].append('https://www.daytonaudio.com/images/resources/275-131--dayton-audio-rst28a-4-specification-sheet.pdf')
if not any(p.get('currency') == 'USD' for p in d['prices']):
    d['prices'].append({'source': 'daytonaudio', 'currency': 'USD', 'price': 58.99})
path.write_text(json.dumps(src, indent=2, ensure_ascii=False), encoding='utf-8')
p(f"Updated: {d['id']}")
p(f"  sources: {d['sources']}")
p(f"  prices: {d['prices']}")

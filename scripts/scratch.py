"""Sanity check drivers.json after dedup."""
import json, sys
from pathlib import Path
from collections import Counter

def p(s): sys.stdout.buffer.write((s+'\n').encode('utf-8', errors='replace'))

src = json.loads(Path('drivers.json').read_text(encoding='utf-8'))
drivers = src['drivers']
p(f"driver_count field: {src['driver_count']}  actual: {len(drivers)}")

ids = [d.get('id','') for d in drivers]
counts = Counter(ids)
dups = {k: v for k, v in counts.items() if v > 1}
p(f"Remaining duplicate IDs: {len(dups)}")

roles = Counter(d.get('role') for d in drivers)
p(f"Role counts: {dict(roles)}")

statuses = Counter(d.get('status') for d in drivers)
p(f"Status counts: {dict(statuses)}")

# Check critical coverage
CRITICAL_BY_ROLE = {
    'mid':  {'fs_hz', 'sensitivity_db', 'impedance_ohm', 'power_rms_w', 'qts', 'xmax_mm'},
    'high': {'fs_hz', 'sensitivity_db', 'impedance_ohm', 'power_rms_w'},
    'sub':  {'fs_hz', 'qts', 'xmax_mm', 'sensitivity_db', 'impedance_ohm'},
    'pr':   {'fs_hz', 'qms', 'xmax_mm'},
    'excl': {'sensitivity_db', 'impedance_ohm'},
}
covered = sum(
    1 for d in drivers
    if all(d.get(f) is not None for f in CRITICAL_BY_ROLE.get(d.get('role',''), set()))
)
p(f"Role-critically covered: {covered} / {len(drivers)}")

# Verify the 3 excl-merged drivers kept excl role
for did in ['dayton-audio-nd25fn-4', 'peerless-by-tymphany-bc25tg15-04', 'peerless-by-tymphany-oc25sc65-04']:
    d = next((x for x in drivers if x['id'] == did), None)
    if d:
        p(f"  {did}: role={d['role']} status={d['status']}")

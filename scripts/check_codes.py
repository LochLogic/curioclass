"""List module rows whose standards codes are not real codes in a known framework."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from standards import validate

bad = 0
for p in sorted(Path(__file__).resolve().parent.parent.glob('data/modules/*.txt')):
    for line in p.read_text(encoding='utf-8').splitlines():
        if line.startswith('#') or not line.strip():
            continue
        f = line.split('|')
        codes = [c.strip() for c in f[5].split(';') if c.strip()] or ['<none>']
        for c in codes:
            if not validate(c):
                bad += 1
                print(f'{p.name:20} {f[0]:5} {f[3][:40]:40} {c}')
print(f'{bad} invalid codes')

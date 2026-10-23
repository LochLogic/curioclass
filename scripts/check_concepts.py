"""Check Phase 2 tool concepts: every module covered, valid formats, healthy variety.

Run from the repo root:  python scripts/check_concepts.py [--write]
--write also writes data/tools-concepts.csv.
"""
import csv, sys
from collections import Counter, defaultdict
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / 'data'
modules = {r['module_id']: r for r in csv.DictReader(open(DATA / 'modules.csv', encoding='utf-8'))}
formats = {r['format_id'] for r in csv.DictReader(open(DATA / 'formats.csv', encoding='utf-8'))}

errors, concepts = [], []
for path in sorted((DATA / 'concepts').glob('*.txt')):
    for n, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        if not line.strip() or line.startswith('#'):
            continue
        f = [x.strip() for x in line.split('|')]
        where = f'{path.name}:{n}'
        if len(f) != 5:
            errors.append(f'{where}: expected 5 fields, got {len(f)}')
            continue
        mid, title, fmt, family, concept = f
        if mid not in modules:
            errors.append(f'{where}: unknown module {mid}')
        if fmt not in formats:
            errors.append(f'{where}: unknown format {fmt}')
        concepts.append(dict(module_id=mid, title=title, format=fmt, family=family, concept=concept))

covered = {c['module_id'] for c in concepts}
missing = [m for m in modules if m not in covered]
titles = Counter(c['title'] for c in concepts)
errors += [f'duplicate tool title: {t}' for t, k in titles.items() if k > 1]

by_subject = defaultdict(list)
for c in concepts:
    if c['module_id'] in modules:
        m = modules[c['module_id']]
        by_subject[m['subject']].append(c)

print(f'{len(concepts)} concepts, {len(covered)}/{len(modules)} modules covered')
print(f'{"subject":18} n  formats  top format share')
for s, cs in by_subject.items():
    fc = Counter(c['format'] for c in cs)
    top, k = fc.most_common(1)[0]
    flag = '  <-- low variety' if k / len(cs) > 0.25 or len(fc) < min(8, len(cs)) else ''
    print(f'{s:18} {len(cs):3} {len(fc):3}      {top} {k / len(cs):.0%}{flag}')
total = Counter(c['format'] for c in concepts)
print('\nall formats:', ', '.join(f'{f} {k}' for f, k in total.most_common()))
unused = formats - set(total)
if unused:
    print('unused formats:', ', '.join(sorted(unused)))

# Same format back to back within one subject and grade reads cookie-cutter
streaks = []
for s, cs in by_subject.items():
    for a, b, c in zip(cs, cs[1:], cs[2:]):
        ga, gb, gc = (modules[x['module_id']]['grade'] for x in (a, b, c))
        if ga == gb == gc and a['format'] == b['format'] == c['format']:
            streaks.append(f'{s} {ga}: three {a["format"]} in a row at {a["module_id"]}')
for x in streaks:
    print('streak:', x)

if missing:
    print(f'\n{len(missing)} modules without a concept, e.g. {missing[:5]}')
for e in errors:
    print('ERROR', e)

if '--write' in sys.argv and not errors:
    fields = ['tool_id', 'title', 'format', 'family', 'module_id', 'subject', 'grade', 'concept', 'status']
    with open(DATA / 'tools-concepts.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for c in concepts:
            m = modules[c['module_id']]
            tid = ''.join(ch if ch.isalnum() else '-' for ch in c['title'].lower()).strip('-')
            while '--' in tid:
                tid = tid.replace('--', '-')
            w.writerow(dict(tool_id=tid, title=c['title'], format=c['format'], family=c['family'],
                            module_id=c['module_id'], subject=m['subject'], grade=m['grade'],
                            concept=c['concept'], status='Concept'))
    print('wrote data/tools-concepts.csv')
sys.exit(1 if errors else 0)

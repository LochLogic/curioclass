"""Write Cory's accepted overlap fixes into data/concepts/*.txt (the concept source, never the CSV).

Reads docs/agents/overlap/choices.json (the decisions) and review.json (the fixes with the title and family rules
applied). Accepted reshapes and renames change the title and concept line; a fix that says the tool leaves its family
clears the family. Tier C fixes left for the spec are not applied here: the spec agent gets them as notes.
Renamed tools change id (the id is the title slug), so data/waves.csv follows. Run from the repo root, then
`python scripts/check_concepts.py --write`.
"""
import csv, json
from pathlib import Path
from common import ROOT, OUT

ROOT, OUT = Path(ROOT), Path(OUT)
DATA = ROOT / 'data'
EXTRA_STANDARDS = {'science-9-photosynthesis-and-cellular-respiration': ['HS-LS2-5']}  # energy-accountant, open call


def slug(title):
    tid = ''.join(ch if ch.isalnum() else '-' for ch in title.lower()).strip('-')
    while '--' in tid:
        tid = tid.replace('--', '-')
    return tid


def main():
    review = {i['id']: i for i in json.loads((OUT / 'review.json').read_text(encoding='utf-8'))}
    choices = json.loads((OUT / 'choices.json').read_text(encoding='utf-8'))
    todo = {}
    for c in choices:
        it = review[c['id']]
        if c['choice'] not in ('accept', 'now') or c['tier'] == 'C' and c['choice'] != 'now':
            continue
        title = c['new_title'] or it['title']
        concept = it['new_concept'] or ''
        leaves = any(r.startswith('Family: Leaves') for r in it['rules'])
        if title != it['title'] or concept or leaves:
            todo[it['id']] = (title, concept, leaves)

    renamed, done = {}, set()
    for path in sorted((DATA / 'concepts').glob('*.txt')):
        lines = path.read_text(encoding='utf-8').splitlines()
        for n, line in enumerate(lines):
            if not line.strip() or line.startswith('#'):
                continue
            f = line.split('|')
            tid = slug(f[1])
            if tid not in todo:
                continue
            title, concept, leaves = todo[tid]
            f[1] = title
            if concept:
                f[4] = concept
            if leaves:
                f[3] = ''
            lines[n] = '|'.join(f)
            done.add(tid)
            if slug(title) != tid:
                renamed[tid] = slug(title)
        path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    missing = set(todo) - done
    if missing:
        raise SystemExit(f'not found in concepts: {sorted(missing)}')

    waves = DATA / 'waves.csv'
    rows = list(csv.DictReader(open(waves, encoding='utf-8')))
    for r in rows:
        r['tool_id'] = renamed.get(r['tool_id'], r['tool_id'])
    with open(waves, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=['tool_id', 'wave'], lineterminator=chr(10))
        w.writeheader()
        w.writerows(rows)

    mods = DATA / 'modules.csv'  # edit the one field in place so the rest of the file stays byte for byte
    lines = mods.read_text(encoding='utf-8').splitlines(keepends=True)
    for n, line in enumerate(lines):
        mid = line.split(',', 1)[0]
        if mid not in EXTRA_STANDARDS:
            continue
        row = next(csv.reader([line]))
        have = [x for x in row[7].split(';') if x]
        add = [code for code in EXTRA_STANDARDS[mid] if code not in have]
        if add:
            old = row[7]
            assert line.count(old) == 1, line
            lines[n] = line.replace(old, ';'.join(have + add))
    mods.write_text(''.join(lines), encoding='utf-8')

    (OUT / 'renamed.json').write_text(json.dumps(renamed, indent=1) + '\n', encoding='utf-8')
    print(f'{len(done)} concept lines changed, {len(renamed)} renamed')


if __name__ == '__main__':
    main()

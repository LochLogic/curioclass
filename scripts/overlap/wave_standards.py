"""Compare the standards each spec in a wave claims with its module's standards in data/modules.csv.

    python scripts/overlap/wave_standards.py docs/agents/BATCH-W1.md [--apply]

Reads the `- Standards` lines in each tools/<id>/spec.md, pulls out codes it recognises (CSTA 2026, NCAS, NGSS, CCSS,
NHES, SHAPE, AASL, CASEL, CTE, NSPFE), coarsens fine codes to the level modules.csv uses (VA:Cr2.1.3a -> VA:Cr2) and
prints, per tool, codes the spec adds and module codes the spec leaves out. Fine NCAS codes the specs name are listed
too, since modules.csv only carries anchors. --apply appends the codes a spec adds to its module's standards field in
data/modules.csv (one field edited in place; codes a spec leaves out are never removed).
"""
import csv, io, os, re, sys
from common import ROOT

PATTERNS = [
    r'\b(?:E[K1-5]|MS|HS)-[A-Z]{3}-[A-Z]{2}-\d{2}\b',                      # CSTA 2026
    r'\b(?:VA|MU|TH|DA|MA):(?:Cr|Pr|Re|Cn)\d+(?:\.\d\.(?:HS[IVA]{1,3}|\d+|K|PK)[a-e]?)?',  # NCAS
    r'\b(?:K|[1-5]|MS|HS|K-2|3-5)-(?:PS|LS|ESS|ETS)\d-\d\b',               # NGSS
    r'\b(?:NHES|SHAPE)\.S\d\b',
    r'\bAASL\.[A-Z][a-z]+\b',
    r'\bD[1-4]\.(?:[A-Z][a-z]{2}\.)?\d+\.(?:K-2|3-5|6-8|9-12)\b',              # C3
]
CASEL = ['Self-Awareness', 'Self-Management', 'Social Awareness', 'Relationship Skills', 'Responsible Decision-Making']
NSPFE = ['Earning Income', 'Spending', 'Saving', 'Investing', 'Managing Credit', 'Managing Risk']


def coarse(code):
    m = re.match(r'((?:VA|MU|TH|DA|MA):(?:Cr|Pr|Re|Cn)\d+)\.', code)
    return m.group(1) if m else code


def claimed(text):
    lines = [l for l in text.splitlines() if re.match(r'\s*[-*]\s*Standards\b', l)]
    s = ' '.join(lines)
    # cut the CSTA 2017 crosswalk and teacher-only links: they are notes, not claims
    s = re.split(r'2017 crosswalk|crosswalk for teachers|Math link for the teacher|References?:', s)[0]
    out = set()
    for p in PATTERNS:
        out |= set(re.findall(p, s))
    out |= {f'CASEL.{c}' for c in CASEL if c in s}
    out |= {f'NSPFE.{c}' for c in NSPFE if re.search(rf'\b{c}\b', s) and 'NSPFE' in s}
    if 'Career Clusters' in s and 'CTE' in s:
        out.add('CTE.Career Clusters')
    if 'Career Ready Practices' in s:
        out.add('CTE.Career Ready Practices')
    return out


def wave_ids(note):
    ids = []
    for line in io.open(note, encoding='utf-8'):
        m = re.match(r'\|\s*([a-z][a-z0-9-]*)\s*\|', line)
        if m and m.group(1) != 'id':
            ids.append(m.group(1))
    return ids


def main():
    note = sys.argv[1]
    concepts = {r['tool_id']: r for r in csv.DictReader(io.open(os.path.join(ROOT, 'data', 'tools-concepts.csv'), encoding='utf-8'))}
    mods = {m['module_id']: m for m in csv.DictReader(io.open(os.path.join(ROOT, 'data', 'modules.csv'), encoding='utf-8'))}
    fine, n_same, rows, adds = set(), 0, [], {}
    for tid in wave_ids(note):
        p = os.path.join(ROOT, 'tools', tid, 'spec.md')
        if not os.path.exists(p):
            rows.append(f'- {tid}: no spec')
            continue
        c = claimed(io.open(p, encoding='utf-8').read())
        fine |= {x for x in c if coarse(x) != x}
        spec = {coarse(x) for x in c}
        mod = {x.strip() for x in mods[concepts[tid]['module_id']]['standards'].split(';') if x.strip()}
        add, drop = sorted(spec - mod), sorted(mod - spec)
        if add:
            adds[concepts[tid]['module_id']] = add
        if not add and not drop:
            n_same += 1
            continue
        rows.append(f'- {tid} ({concepts[tid]["grade"]}): spec adds {", ".join(add) or "nothing"}; leaves out {", ".join(drop) or "nothing"}')
    print(f'{n_same} specs claim exactly their module codes; {len(rows)} differ:')
    print('\n'.join(rows))
    print(f'\nFine NCAS codes named in specs ({len(fine)}): {", ".join(sorted(fine))}')
    if '--apply' in sys.argv and adds:
        path = os.path.join(ROOT, 'data', 'modules.csv')
        lines = io.open(path, encoding='utf-8', newline='').read().splitlines(keepends=True)
        for n, line in enumerate(lines):
            mid = line.split(',', 1)[0]
            if mid in adds:
                field = next(csv.reader([line]))[7]
                assert line.count(field) == 1, line
                lines[n] = line.replace(field, ';'.join([field] + adds[mid]))
        io.open(path, 'w', encoding='utf-8', newline='').write(''.join(lines))
        print(f'added codes to {len(adds)} modules')


if __name__ == '__main__':
    main()

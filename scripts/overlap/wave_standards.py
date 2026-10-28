"""Compare the standards each spec in a wave claims with its module's standards in data/modules.csv.

    python scripts/overlap/wave_standards.py docs/agents/BATCH-W1.md [--apply]

Reads the `- Standards` lines in each tools/<id>/spec.md (with their wrapped continuation lines, or an inline
"Standards:" sentence up to the end of its paragraph), pulls out codes it recognises (CSTA 2026, NCAS, NGSS, CCSS ELA,
CCSS math, AP units, WIDA, C3, NHES, SHAPE, AASL, CASEL, CTE, NSPFE), coarsens fine codes to the level modules.csv uses (VA:Cr2.1.3a -> VA:Cr2) and
prints, per tool, codes the spec adds and module codes the spec leaves out. Fine NCAS codes the specs name are listed
too, since modules.csv only carries anchors. --apply adds the codes a spec names to its module in data/modules/*.txt (through
scripts/add_codes.py) and rebuilds data/modules.csv; codes a spec leaves out are never removed.
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
    r'\b(?:RL|RI|RF|W|SL|L)\.(?:K|[1-8]|9-10|11-12)\.\d{1,2}\b',               # CCSS ELA
    r'\b[NAFGS]-[A-Z]{1,3}\.[A-D](?:\.\d{1,2}[a-e]?)?\b',                      # CCSS math (cluster or standard)
    r'\bAP-(?:CALC|PRECALC|STAT)\.U\d+\b',                                     # AP course units
    r'\bWIDA\.(?:ELD-\d|Narrate|Inform|Explain|Argue)\b',                      # WIDA ELD standards and key uses
]
CASEL = ['Self-Awareness', 'Self-Management', 'Social Awareness', 'Relationship Skills', 'Responsible Decision-Making']
NSPFE = ['Earning Income', 'Spending', 'Saving', 'Investing', 'Managing Credit', 'Managing Risk']


def coarse(code):
    m = re.match(r'((?:VA|MU|TH|DA|MA):(?:Cr|Pr|Re|Cn)\d+)\.', code)
    return m.group(1) if m else code


def claimed(text):
    lines, take = [], False
    for l in text.splitlines():
        if re.match(r'\s*[-*]\s*Standards\b', l):
            take = True
            lines.append(l)
        elif 'Standards:' in l and not l.lstrip().startswith(('-', '*', '#')):
            take = True
            lines.append(l[l.index('Standards:'):])
        elif take and l.strip() and not re.match(r'\s*([-*#]|\d+\.)\s', l):
            lines.append(l)
        else:
            take = False
    s = ' '.join(lines)
    # cut the CSTA 2017 crosswalk and teacher-only links: they are notes, not claims
    s = re.split(r'2017 crosswalk|crosswalk for teachers|Math link for the teacher|The math content follows|References?:', s)[0]
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
        # CCSS math: a cluster and a standard inside it count as the same claim (A-CED.A covers A-CED.A.1)
        near = lambda a, b: a == b or a.startswith(b + '.') or b.startswith(a + '.')
        add = sorted(x for x in spec if not any(near(x, m) for m in mod))
        drop = sorted(m for m in mod if not any(near(x, m) for x in spec))
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
        # modules.csv is generated: the codes go in data/modules/*.txt through add_codes.py, then build_db.py
        import subprocess, tempfile
        with tempfile.NamedTemporaryFile('w', suffix='.txt', delete=False, encoding='utf-8') as f:
            f.write(''.join(f'{mid}: {";".join(codes)}\n' for mid, codes in adds.items()))
        subprocess.run([sys.executable, os.path.join(ROOT, 'scripts', 'add_codes.py'), f.name], check=True)
        subprocess.run([sys.executable, os.path.join(ROOT, 'scripts', 'build_db.py')], check=True, stdout=subprocess.DEVNULL)
        os.unlink(f.name)

if __name__ == '__main__':
    main()

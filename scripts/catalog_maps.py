r"""The step 2 maps and the spec sort (docs/ROADMAP.md, "The path from here"). No tokens.

    python scripts/catalog_maps.py

Run scripts/coverage_ledger.py first. Reads data/coverage.csv and every extract row (docs/agents/catalog/rows/*.jsonl)
and writes:

  docs/agents/catalog/tables/map-<subject>.md   one map per subject: the measure, every standard by course with its
                                                status and tools, and the subject's specs sorted
  docs/agents/catalog/tables/spec-sort.csv      one row per tool: fine, small addition or rework, and why
  docs/agents/catalog/tables/maps.md            the index: one line per subject

The sort of a spec, from its row:
  fine            every code is taught and nothing core is missing
  small addition  the tool teaches or practises its codes but a check can be guessed, a core part (explain, write,
                  record) is missing, or a code is off the main path
  rework          the tool does the standard's key step for the student, or only shows or claims its codes, on half
                  or more of its codes, or teaches nothing and shows something
`thin` marks a tool whose spec is missing or voice-only, so the row was read from notes: write the spec first.
`trust` is how far the spot-check (ROADMAP resume note, 2026-11-10) says the subject's rows can be relied on.
"""
import csv, glob, io, json, os, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAT = os.path.join(ROOT, 'docs', 'agents', 'catalog')
TAB = os.path.join(CAT, 'tables')

def rd(path):
    with io.open(os.path.join(ROOT, path), encoding='utf-8') as f:
        return list(csv.DictReader(f))

TRUST = {'math': 'high (a floor)', 'social-studies': 'high', 'ela': 'taught counts are a floor', 'science': 'within one step'}
ORDER = ['k', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 'k-2', '3-5', '6-8', '6-12', '9-12', 'k-12']
STAT = ['full', 'nearly', 'part', 'practice', 'shown', 'none', 'not read', 'no module']
WORD = {'full': 'Full', 'nearly': 'Nearly', 'part': 'Part', 'practice': 'Practice only', 'shown': 'Shown', 'none': 'None',
        'not read': 'Not read', 'no module': 'No module'}

modules = {m['module_id']: m for m in rd('data/modules.csv')}
concepts = {c['tool_id']: c for c in rd('data/tools-concepts.csv')}
cover = rd('data/coverage.csv')
rows = {}
for f in sorted(glob.glob(os.path.join(CAT, 'rows', '*.jsonl'))):
    for ln in io.open(f, encoding='utf-8'):
        if ln.strip():
            r = json.loads(ln); rows[r['id']] = r

def clip(s, n=110):
    s = ' '.join(s.split())
    return s if len(s) <= n else s[:n - 3].rstrip() + '...'

# ---- the spec sort --------------------------------------------------------------------------------------------
def sort_of(r):
    cs = r.get('codes', [])
    why = []
    if not cs: return 'rework', ['carries no code']
    n = len(cs)
    ok = [c for c in cs if c.get('depth') == 'taught' and c.get('missing_weight') in ('', 'edge', None)]
    toolstep = [c['code'] for c in cs if c.get('key_step') == 'tool' or c.get('depth') == 'shown']
    claimed = [c['code'] for c in cs if c.get('depth') == 'claimed']
    touched = [c['code'] for c in cs if c.get('depth') == 'touched']
    core = [c['code'] for c in cs if c.get('missing_weight') == 'core' and c.get('depth') in ('taught', 'practiced', 'explored')]
    held = [c['code'] for c in cs if c.get('depth') == 'practiced']
    if len(ok) == n: return 'fine', []
    if toolstep: why.append('tool does the key step: ' + ', '.join(toolstep[:6]))
    if claimed: why.append('claimed, not taught: ' + ', '.join(claimed[:6]))
    if r.get('beatable') and held: why.append('close the guessable check (%d listed)' % len(r['beatable']))
    elif held: why.append('practice with no real check: ' + ', '.join(held[:6]))
    if core: why.append('core part missing: ' + ', '.join(core[:6]))
    if touched: why.append('off the main path: ' + ', '.join(touched[:6]))
    weak = len(set(toolstep) | set(claimed))
    anything = any(c.get('depth') in ('taught', 'explored') for c in cs)
    if weak * 2 >= n or (weak and not anything): return 'rework', why
    return 'small addition', why

sort_rows = []
for t, r in rows.items():
    c = concepts[t]; m = modules[c['module_id']]
    kind, why = sort_of(r)
    sort_rows.append({'tool': t, 'title': c['title'], 'subject': m['subject'], 'grade': m['grade'], 'module': c['module_id'],
                      'stage': r.get('stage', ''), 'sort': kind, 'thin': 'yes' if 'spec-thin' in (r.get('flags') or []) or r.get('stage') == 'idea' else '',
                      'codes': len(r.get('codes', [])), 'why': ' | '.join(why), 'trust': TRUST.get(m['subject'], 'rough: check each taught by hand')})
gkey = lambda g: ORDER.index(g) if g in ORDER else 99
sort_rows.sort(key=lambda x: (x['subject'], gkey(x['grade']), x['module'], x['tool']))
with io.open(os.path.join(TAB, 'spec-sort.csv'), 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, list(sort_rows[0].keys()), lineterminator='\n'); w.writeheader(); w.writerows(sort_rows)

# ---- one map per subject --------------------------------------------------------------------------------------
subjects = sorted({m['subject'] for m in modules.values()})
index = ['# The step 2 maps\n',
         'Built by scripts/catalog_maps.py from the ledger and the extract rows. One map per subject; the spec sort for '
         'every tool is in spec-sort.csv. How far each subject can be trusted is in the ROADMAP resume note.\n',
         '| Subject | Tools | Standards | Full or nearly | Part | Practice only | Shown | None | Specs fine | Small addition | Rework | Thin spec | Trust |',
         '|---|---|---|---|---|---|---|---|---|---|---|---|---|']
total = collections.Counter()
for s in subjects:
    cov = [r for r in cover if r['subject'] == s]
    tools = [x for x in sort_rows if x['subject'] == s]
    sc = collections.Counter(x['sort'] for x in tools)
    thin = sum(1 for x in tools if x['thin'])
    grades = sorted({r['grade'] for r in cov}, key=gkey)
    allc = collections.Counter(r['status'] for r in cov)
    P = ['# Map: %s\n' % s,
         'Built by scripts/catalog_maps.py. %d tools, %d standard rows (a standard counts once per course that lists it). '
         'Trust: %s.\n' % (len(tools), len(cov), TRUST.get(s, 'rough: the codes are broad and have no filed wording in the packets, so check each taught by hand')),
         '## The measure\n',
         '| Course | Standards | ' + ' | '.join(WORD[k] for k in STAT[:6]) + ' |', '|---|---|' + '---|' * 6]
    for g in grades:
        c = collections.Counter(r['status'] for r in cov if r['grade'] == g)
        P.append('| %s %s | %d | %s |' % (s, g, sum(c.values()), ' | '.join(str(c.get(k) or '') for k in STAT[:6])))
    P.append('\n## The specs, sorted\n')
    P.append('%d fine, %d small addition, %d rework; %d have a thin or missing spec.\n' % (sc['fine'], sc['small addition'], sc['rework'], thin))
    for kind in ('rework', 'small addition', 'fine'):
        pick = [x for x in tools if x['sort'] == kind]
        if not pick: continue
        P.append('### %s (%d)\n' % (kind.capitalize(), len(pick)))
        if kind == 'fine':
            P.append(', '.join('%s (%s)' % (x['title'], x['grade']) for x in pick) + '\n'); continue
        P.append('| Tool | Grade | Stage | Why |'); P.append('|---|---|---|---|')
        for x in pick:
            P.append('| %s%s | %s | %s | %s |' % (x['title'], ' (thin spec)' if x['thin'] else '', x['grade'], x['stage'], clip(x['why'].replace('|', ';'), 200)))
        P.append('')
    P.append('## Every standard, by course\n')
    for g in grades:
        P.append('### %s %s\n' % (s, g))
        P.append('| Standard | Status | Teach tools | Practice or see-why | Weak | Missing |'); P.append('|---|---|---|---|---|---|')
        for r in sorted((r for r in cov if r['grade'] == g), key=lambda r: (STAT.index(r['status']), r['standard'])):
            P.append('| %s%s | %s | %s | %s | %s | %s |' % (r['standard'], ' (%s)' % r['focus'] if r['focus'] else '', WORD[r['status']], clip(r['teach'], 90),
                     clip('; '.join(x for x in (r['practice'], r['see_why']) if x), 90), clip(r['weak'], 70), clip(r['parts_missing'].replace('|', ';'), 140)))
        P.append('')
    io.open(os.path.join(TAB, 'map-%s.md' % s), 'w', encoding='utf-8', newline='\n').write('\n'.join(P) + '\n')
    index.append('| [%s](map-%s.md) | %d | %d | %d | %d | %d | %d | %d | %d | %d | %d | %d | %s |' % (
        s, s, len(tools), len(cov), allc['full'] + allc['nearly'], allc['part'], allc['practice'], allc['shown'], allc['none'],
        sc['fine'], sc['small addition'], sc['rework'], thin, TRUST.get(s, 'rough')))
    total.update(sc); total['thin'] += thin
index.append('\nAll tools: %d fine, %d small addition, %d rework; %d with a thin or missing spec.' % (total['fine'], total['small addition'], total['rework'], total['thin']))
io.open(os.path.join(TAB, 'maps.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(index) + '\n')
print('\n'.join(index[2:]))

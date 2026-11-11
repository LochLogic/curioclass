r"""Catalog review, step 2: tables from the extract rows (docs/agents/CATALOG-REVIEW.md). No tokens.

    python scripts/catalog_compute.py <name> <subject> <grade> [<grade> ...]

Reads docs/agents/catalog/rows/*.jsonl, keeps tools whose module is in <subject> and one of the grades (a band such
as 6-8 counts as a grade), and writes docs/agents/catalog/tables/<name>.md: coverage per standard, module codes not
taught, the clash rule, math focus and balance, a value table, and the flags.
"""
import csv, glob, io, json, os, re, sys, itertools, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAT = os.path.join(ROOT, 'docs', 'agents', 'catalog')
name, subject, grades = sys.argv[1], sys.argv[2], sys.argv[3:]

def rd(path):
    with io.open(os.path.join(ROOT, path), encoding='utf-8') as f:
        return list(csv.DictReader(f))

modules = {r['module_id']: r for r in rd('data/modules.csv')}
concepts = {r['tool_id']: r for r in rd('data/tools-concepts.csv')}
tags = {r['tool_id']: r for r in rd('docs/agents/overlap/tags.csv')}

rows = []
for f in sorted(glob.glob(os.path.join(CAT, 'rows', '*.jsonl'))):
    for n, line in enumerate(io.open(f, encoding='utf-8'), 1):
        line = line.strip()
        if not line: continue
        r = json.loads(line)
        c = concepts.get(r['id'])
        if not c: print('unknown tool', r['id'], 'in', os.path.basename(f)); continue
        m = modules[c['module_id']]
        if m['subject'] != subject or m['grade'] not in grades: continue
        r['_m'], r['_c'] = m, c
        r['_band'] = (tags.get(r['id']) or {}).get('band', m['grade'])
        rows.append(r)
ids = {r['id'] for r in rows}
missing = [t for t, c in concepts.items() if c['subject'] == subject and c['grade'] in grades and t not in ids]

# ---- expected codes -------------------------------------------------------------------------------------------
single = [g for g in grades if '-' not in g]            # coverage is judged for the single grades asked for
focus = {}
expected = []
def short(code):
    """One spelling for matching: 4.NBT.B.5 -> 4.NBT.5, A-REI.B.4a -> A-REI.4a (as in scripts/coverage_ledger.py)."""
    p = code.strip().split('.')
    i = 1 if '-' in p[0] else 2
    if len(p) > i + 1 and re.match(r'^[A-Z]$', p[i]) and p[i + 1][:1].isdigit(): del p[i]
    return '.'.join(p)
def base(code):
    """4.NF.B.3a -> 4.NF.3 ; SL.6.1.c -> SL.6.1"""
    code = short(code)
    m = re.match(r'^(.*?\.\d+)[a-z]?(\.[a-z])?$', code)
    return m.group(1) if m else code
def filed(path):
    for line in io.open(os.path.join(ROOT, path), encoding='utf-8'):
        if line.strip() and not line.startswith('#'): yield line.rstrip('\n')

if subject == 'math':
    cf = {r['cluster']: r['focus'] for r in csv.DictReader(filed('data/standards/ccss-math-focus.csv'))}
    for line in filed('data/standards/ccss-math-standards.txt'):
        sid = line.split('\t')[0]
        if sid.split('.')[0].lower() in single and not re.search(r'\d[a-z]$', sid):
            expected.append(base(sid)); focus[base(sid)] = cf.get(sid.rsplit('.', 1)[0], '')
elif subject == 'ela':
    for line in filed('data/standards/ccss-ela-standards.txt'):
        if any(re.search(r'\.%s\.' % g, line, re.I) for g in single):
            expected.append(line.split()[0])

# explored (a see-why tool, format 2) counts with taught for clashes and value; shown ranks with touched
RANK = {'taught': 3, 'explored': 3, 'practiced': 2, 'shown': 1, 'touched': 1, 'claimed': 0}

by_code = collections.defaultdict(list)
for r in rows:
    for c in r.get('codes', []):
        by_code[base(c['code'])].append((r['id'], c.get('depth', '?'), c.get('activity', ''), c['code']))

out = []
P = out.append
P('# Catalog review tables: %s\n' % name)
P('%d tools read (%s, grades %s). Built by scripts/catalog_compute.py from docs/agents/catalog/rows/.\n' % (len(rows), subject, ', '.join(grades)))
if missing: P('**No row yet for:** ' + ', '.join(sorted(missing)) + '\n')

# ---- 1 coverage -----------------------------------------------------------------------------------------------
P('## 1. Coverage, standard by standard\n')
P('A standard is covered when at least one tool teaches it (depth `taught`). `practiced` assumes it was taught '
  'elsewhere; `explored` is a see-why tool; `shown` means the tool does the key step; `touched` can be skipped; '
  '`claimed` has no matching student action. Parts left out and the full, part or shown verdict are in '
  'data/coverage.csv (scripts/coverage_ledger.py).\n')
P('| Standard |%s Taught by | Practiced | Explored, shown, touched or claimed | Status |' % (' Focus |' if focus else ''))
P('|---|%s---|---|---|---|' % ('---|' if focus else ''))
status_count = collections.Counter()
for code in expected:
    hits = by_code.get(code, [])
    t = [h for h in hits if h[1] == 'taught']; p = [h for h in hits if h[1] == 'practiced']
    o = [h for h in hits if h[1] in ('explored', 'shown', 'touched', 'claimed')]
    nt = len({h[0] for h in t})
    st = 'ok' if nt in (1, 2, 3) else 'crowded (%d)' % nt if nt else 'practice only' if p else 'thin' if o else '**no tool**'
    status_count[st.split(' (')[0]] += 1
    def f(hs):
        parts = collections.defaultdict(set)
        for h in hs: parts[h[0]].add(h[3].replace(code, '').strip('.'))
        return ', '.join(t + (' (%s)' % ', '.join(sorted(x for x in v if x)) if any(v) else '') for t, v in sorted(parts.items())) or '-'
    P('| %s |%s %s | %s | %s | %s |' % (code, (' %s |' % focus.get(code, '')) if focus else '', f(t), f(p),
                                       ', '.join(sorted('%s (%s)' % (h[0], h[1]) for h in o)) or '-', st))
P('\nCount: ' + ', '.join('%s %d' % kv for kv in status_count.most_common()) + '.\n')
extra = sorted(c for c in by_code if c not in expected)
if extra:
    P('Codes named by these tools from outside the grade: ' + ', '.join('%s (%d)' % (c, len(by_code[c])) for c in extra) + '.\n')

# ---- 2 module codes not taught --------------------------------------------------------------------------------
P('## 2. Module codes its own tool does not teach\n')
P('| Tool | Module codes | Not taught or practiced (from the row) | Claimed or only touched |')
P('|---|---|---|---|')
for r in rows:
    weak = [c['code'] + ' (' + c['depth'] + ')' for c in r.get('codes', []) if c.get('depth') in ('shown', 'touched', 'claimed')]
    un = [u for u in r.get('module_codes_untaught', []) if u]
    if un or weak:
        P('| %s | %s | %s | %s |' % (r['id'], r['_m']['standards'].replace(';', ', '), ', '.join(un) or '-', ', '.join(weak) or '-'))
P('')

# ---- 3 clash rule ---------------------------------------------------------------------------------------------
P('## 3. Clash rule (two or more of skill key, action, setting group match, same band)\n')
P('| Band | Tool A | Tool B | Matched | Shared standards |')
P('|---|---|---|---|---|')
nclash = 0
for a, b in itertools.combinations(rows, 2):
    if a['_band'] != b['_band']: continue
    m = [k for k in ('skill_key', 'action', 'setting_group') if a.get(k) and a.get(k) == b.get(k) and a.get(k) != 'generic']
    sa = {base(c['code']) for c in a.get('codes', []) if RANK.get(c.get('depth'), 0) >= 2}
    sb = {base(c['code']) for c in b.get('codes', []) if RANK.get(c.get('depth'), 0) >= 2}
    if len(m) >= 2 or (len(m) >= 1 and sa & sb):
        nclash += 1
        P('| %s | %s | %s | %s | %s |' % (a['_band'], a['id'], b['id'], ' + '.join(m), ', '.join(sorted(sa & sb)) or '-'))
if not nclash: P('| - | none | | | |')
P('\nRows with one match are listed only when the two tools also teach or practice the same standard.\n')

# ---- 4 focus and balance --------------------------------------------------------------------------------------
P('## 4. Kinds of work%s\n' % (' and focus' if focus else ''))
P('Each tool splits its time across understanding, fluency and application (0 to 3 each).\n')
P('| Tool |%s Understanding | Fluency | Application | Use | Minutes |' % (' Focus |' if focus else ''))
P('|---|%s---|---|---|---|---|' % ('---|' if focus else ''))
tot = collections.Counter(); ftot = collections.Counter()
for r in rows:
    k = r.get('kinds', {})
    fo = ''
    if focus:
        fs = {focus.get(base(c['code']), focus.get(c['code'], '?')) for c in r.get('codes', []) if RANK.get(c.get('depth'), 0) >= 2}
        fo = 'major' if 'major' in fs else 'supporting' if 'supporting' in fs else 'additional' if 'additional' in fs else '?'
        ftot[fo] += 1; r['_focus'] = fo
    for x in ('understanding', 'fluency', 'application'): tot[x] += k.get(x, 0)
    P('| %s |%s %s | %s | %s | %s | %s |' % (r['id'], (' %s |' % fo) if focus else '', k.get('understanding', ''), k.get('fluency', ''),
                                            k.get('application', ''), r.get('use', ''), r.get('minutes', '')))
s = sum(tot.values()) or 1
P('\nShare of all points: ' + ', '.join('%s %d%%' % (x, round(100 * tot[x] / s)) for x in ('understanding', 'fluency', 'application')) + '.')
if focus:
    n = len(rows) or 1
    P('Tools by focus: ' + ', '.join('%s %d (%d%%)' % (k, v, round(100 * v / n)) for k, v in ftot.most_common()) + '.')
P('')

# ---- 5 value --------------------------------------------------------------------------------------------------
P('## 5. Value table\n')
P('Depth = best depth on any code. Sole = standards only this tool teaches. Sorted so the weakest case for a tool '
  'comes first: little taught, paper could do it, costly to build. A sort order for the judge, not a verdict.\n')
P('| Tool | Stage | Depth | Sole teacher of | What paper could not do | Screen adds | Cost |')
P('|---|---|---|---|---|---|---|')
teachers = {c: {h[0] for h in hs if h[1] == 'taught'} for c, hs in by_code.items()}
def val(r):
    d = max([RANK.get(c.get('depth'), 0) for c in r.get('codes', [])] or [0])
    sole = sorted(c for c, t in teachers.items() if t == {r['id']})
    paper = {'none': 2, 'partial': 1, 'full': 0}.get(r.get('paper_version'), 0 if (r.get('paper_gap') or 'none').strip().lower() == 'none' else 2 if 'paper_gap' in r else 1)
    cost = {'simple': 0, 'sibling': 0, 'new-engine': 1, 'super': 2}.get(r.get('cost_class'), 1)
    return d + paper + min(len(sole), 2) - cost, d, sole
for r in sorted(rows, key=lambda r: val(r)[0]):
    sc, d, sole = val(r)
    P('| %s | %s | %s | %s | %s | %s | %s |' % (r['id'], r.get('stage') or r['_c']['status'], {3: 'taught or explored', 2: 'practiced', 1: 'shown or touched', 0: 'claimed'}[d],
        ', '.join(sole) or '-', (r.get('paper_gap') or r.get('paper_version', '')).replace('|', '/'), (r.get('screen_adds') or '').replace('|', '/'), r.get('cost_class', '')))
P('')

# ---- 6 flags --------------------------------------------------------------------------------------------------
P('## 6. Flags, beatable checks and unsure notes\n')
for r in rows:
    fl = [x for x in r.get('flags', []) if x]; be = [x for x in r.get('beatable', []) if x]; un = [x for x in r.get('unsure', []) if x]
    if fl or be or un:
        P('- **%s**%s' % (r['id'], (' [' + ', '.join(fl) + ']') if fl else ''))
        for x in be: P('  - beatable: ' + x)
        for x in un: P('  - unsure: ' + x)
P('')

os.makedirs(os.path.join(CAT, 'tables'), exist_ok=True)
dest = os.path.join(CAT, 'tables', name + '.md')
io.open(dest, 'w', encoding='utf-8', newline='\n').write('\n'.join(out).replace('—', '-'))
print('wrote', os.path.relpath(dest, ROOT), '|', len(rows), 'rows |', dict(status_count), '| clashes', nclash)

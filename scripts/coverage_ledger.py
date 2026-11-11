r"""The coverage ledger (docs/ECOSYSTEM.md; path step 2 in docs/ROADMAP.md). No tokens.

    python scripts/coverage_ledger.py

Reads every catalog extract row (docs/agents/catalog/rows/*.jsonl), data/modules.csv, data/tools-concepts.csv and the
filed standards in data/standards/, and writes:

  data/coverage.csv                       one row per standard per course: where it is taught in full
  docs/agents/catalog/tables/measure.md   the one measure per course, and the modules that hold two topics

Status of a standard: `full` (a tool teaches it, every part), `part` (taught with parts left out, or explored by a
see-why tool), `practice` (practised only), `shown` (the tool does the key step, or it can be skipped), `none` (every
tool of the modules that list it was read and none reaches it), `not read` (a tool there has no row yet),
`no module` (no module lists it).
"""
import csv, glob, io, json, os, re, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAT = os.path.join(ROOT, 'docs', 'agents', 'catalog')

def rd(path):
    with io.open(os.path.join(ROOT, path), encoding='utf-8') as f:
        return list(csv.DictReader(f))

def lines(path):
    for ln in io.open(os.path.join(ROOT, path), encoding='utf-8'):
        ln = ln.rstrip('\n')
        if ln.strip() and not ln.startswith('#'): yield ln

def short(code):
    """One spelling for matching: 4.NBT.B.5 -> 4.NBT.5, A-REI.B.4a -> A-REI.4a, SL.6.1.c -> SL.6.1c."""
    code = code.strip()
    p = code.split('.')
    i = 1 if '-' in p[0] else 2            # high school ids start with the domain (A-REI); K-8 with the grade
    if len(p) > i + 1 and re.match(r'^[A-Z]$', p[i]) and p[i + 1][:1].isdigit():
        del p[i]
    code = '.'.join(p)
    return re.sub(r'(\d)\.([a-z])$', r'\1\2', code)

def split(code):
    """4.NF.3a -> (4.NF.3, a)"""
    m = re.match(r'^(.*\d)([a-z])$', code)
    return (m.group(1), m.group(2)) if m else (code, '')

# ---- the filed standards --------------------------------------------------------------------------------------
long_of, letters, math_by_cluster, math_by_grade = {}, collections.defaultdict(set), collections.defaultdict(list), collections.defaultdict(list)
for ln in lines('data/standards/ccss-math-standards.txt'):
    sid = ln.split('\t')[0]
    b, let = split(short(sid))
    if let: letters[b].add(let); long_of.setdefault(b, re.sub(r'[a-z]$', '', sid)); continue
    long_of[b] = sid
    math_by_cluster[sid.rsplit('.', 1)[0]].append(b)
    math_by_grade[sid.split('.')[0].lower()].append(b)
ela_by_grade = collections.defaultdict(list)
for ln in lines('data/standards/ccss-ela-standards-full.txt'):
    sid = ln.split('\t')[0]
    b, let = split(short(sid))
    if let: letters[b].add(let); continue
    g = sid.split('.')[1].lower()
    for x in ([g] if '-' not in g else g.split('-') if g in ('9-10', '11-12') else [g]): ela_by_grade[x].append(b)
focus = {}
for r in csv.DictReader(lines('data/standards/ccss-math-focus.csv')):
    for b in math_by_cluster.get(r['cluster'], []): focus[b] = r['focus']

# ---- modules, tools, rows -------------------------------------------------------------------------------------
modules = rd('data/modules.csv')
concepts = rd('data/tools-concepts.csv')
tools_of = collections.defaultdict(list)
for c in concepts: tools_of[c['module_id']].append(c['tool_id'])
mod_of_tool = {c['tool_id']: c['module_id'] for c in concepts}

def mod_codes(m):
    out = []
    for c in m['standards'].split(';'):
        c = c.strip()
        if not c: continue
        out += math_by_cluster[c] if c in math_by_cluster else [split(short(c))[0]]
    return out

rows = {}
for f in sorted(glob.glob(os.path.join(CAT, 'rows', '*.jsonl'))):
    for ln in io.open(f, encoding='utf-8'):
        if ln.strip():
            r = json.loads(ln); rows[r['id']] = r

hits = collections.defaultdict(list)      # base code -> (tool, letter, depth, parts_missing, unit_adds)
for t, r in rows.items():
    for c in r.get('codes', []):
        b, let = split(short(c.get('code', '')))
        hits[b].append((t, let, c.get('depth', ''), [p for p in c.get('parts_missing', []) if p], c.get('unit_adds', '')))

# ---- courses --------------------------------------------------------------------------------------------------
courses = collections.OrderedDict()
for m in sorted(modules, key=lambda m: (m['subject'], m['grade'])):
    courses.setdefault((m['subject'], m['grade']), []).append(m)

ORDER = ['k', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
def in_band(grade, band):
    if '-' not in band: return False
    a, b = band.split('-')
    return ORDER.index(a) <= ORDER.index(grade) <= ORDER.index(b)
def expected_for(subject, grade):
    return list(math_by_grade.get(grade, [])) if subject == 'math' else list(ela_by_grade.get(grade, [])) if subject == 'ela' else []

def status(code):
    hs = hits.get(code, [])
    need = letters.get(code, set())
    clean = {h[1] for h in hs if h[2] == 'taught' and not h[3]}
    if '' in clean or (need and need <= clean): return 'full'
    if any(h[2] in ('taught', 'explored') for h in hs): return 'part'
    if any(h[2] == 'practiced' for h in hs): return 'practice'
    if hs: return 'shown'
    return ''

out, measure = [], []
for (subject, grade), mods in courses.items():
    listed = collections.defaultdict(list)
    for m in mods:
        for c in mod_codes(m): listed[c].append(m['module_id'])
    if grade in ORDER:                      # a band module (ela 6-8) also serves each grade inside its band
        for (s2, g2), ms in courses.items():
            if s2 == subject and in_band(grade, g2):
                for m in ms:
                    for c in mod_codes(m):
                        if c in expected_for(subject, grade): listed[c].append(m['module_id'])
    expected = expected_for(subject, grade)
    expected += [c for c in listed if c not in expected]
    count = collections.Counter()
    for code in expected:
        st = status(code)
        if not st:
            ts = [t for mid in listed.get(code, []) for t in tools_of[mid]]
            st = 'no module' if code not in listed else 'not read' if any(t not in rows for t in ts) or not ts else 'none'
        count[st] += 1
        hs = hits.get(code, [])
        def who(*depths):
            d = collections.defaultdict(set)
            for h in hs:
                if h[2] in depths: d[h[0]].add(h[1])
            return '; '.join(t + ('(%s)' % ''.join(sorted(v)) if any(v) else '') for t, v in sorted(d.items()))
        missing = sorted({p for h in hs if h[2] in ('taught', 'explored') for p in h[3]})
        got = {h[1] for h in hs if h[2] == 'taught' and not h[3]}
        missing += ['part %s' % x for x in sorted(letters.get(code, set()) - got)] if letters.get(code) and '' not in got and st != 'full' else []
        out.append({'subject': subject, 'grade': grade, 'standard': long_of.get(code, code), 'focus': focus.get(code, ''),
                    'status': st, 'lesson': who('taught'), 'see_why': who('explored'), 'practice': who('practiced'),
                    'weak': who('shown', 'touched', 'claimed'), 'parts_missing': ' | '.join(missing),
                    'unit_adds': ' | '.join(sorted({h[4] for h in hs if h[4]})),
                    'modules': '; '.join(listed.get(code, [])), 'worksheets': '', 'generator': '', 'reading_room': '', 'unit': ''})
    read = sum(1 for m in mods for t in tools_of[m['module_id']] if t in rows)
    alltools = sum(len(tools_of[m['module_id']]) for m in mods)
    measure.append((subject, grade, count, len(expected), read, alltools))

cols = ['subject', 'grade', 'standard', 'focus', 'status', 'lesson', 'see_why', 'practice', 'weak', 'parts_missing', 'unit_adds',
        'modules', 'worksheets', 'generator', 'reading_room', 'unit']
with io.open(os.path.join(ROOT, 'data', 'coverage.csv'), 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, cols, lineterminator='\n'); w.writeheader(); w.writerows(out)

# ---- the measure and the two-topic modules --------------------------------------------------------------------
P = []
P.append('# The one measure, course by course\n')
P.append('Built by scripts/coverage_ledger.py from the extract rows; the rows behind it are in data/coverage.csv. '
         'A course whose tools are not all read yet shows how many were. Worksheets, generators, the Reading Room and '
         'units are not counted yet (their columns in the ledger are filled in path step 4).\n')
P.append('| Course | Tools read | Standards | Full | Part | Practice | Shown | None | Not read | No module |')
P.append('|---|---|---|---|---|---|---|---|---|---|')
for subject, grade, c, n, read, alltools in measure:
    P.append('| %s %s | %d of %d | %d | %s |' % (subject, grade, read, alltools, n,
             ' | '.join(str(c.get(k, 0) or '') for k in ('full', 'part', 'practice', 'shown', 'none', 'not read', 'no module'))))
P.append('\n## Modules that may hold two topics (math: standards from more than one domain)\n')
P.append('Candidates only. A module is split when it holds two unrelated topics (BASELINE rule 22); each comes to Cory as an '
         'exception in path step 4.\n')
P.append('| Module | Title | Domains | Tools |')
P.append('|---|---|---|---|')
n = 0
for m in modules:
    if m['subject'] != 'math': continue
    doms = sorted({re.sub(r'\.\d+$', '', c) for c in mod_codes(m) if re.search(r'\.\d+$', c)})
    if len(doms) > 1:
        n += 1; P.append('| %s | %s | %s | %s |' % (m['module_id'], m['title'], ', '.join(doms), ', '.join(tools_of[m['module_id']])))
os.makedirs(os.path.join(CAT, 'tables'), exist_ok=True)
io.open(os.path.join(CAT, 'tables', 'measure.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(P) + '\n')
tot = collections.Counter()
for m in measure: tot.update(m[2])
print('wrote data/coverage.csv (%d rows) and tables/measure.md |' % len(out), len(rows), 'tools read |', dict(tot), '| two-domain math modules', n)

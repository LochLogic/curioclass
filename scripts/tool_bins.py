r"""Sorts every existing tool and spec into three bins by demand, and writes docs/TOOL-BINS.md. No tokens.

    python -X utf8 scripts/tool_bins.py

The rule is BASELINE rule 26 and docs/FOUNDATION.md section 6 item 5 (Cory, 2026-11-11):
  (a) named by a unit or section plan, as key or light: gets course work;
  (b) live and passing the teaching test but not named: stays on the shelf, claims no course coverage;
  (c) everything else: frozen, no further spend.
The list is made here, never by inspection. A tool moves to (a) only when a unit or section plan asks for it.

What is read (nothing is written except docs/TOOL-BINS.md):
  data/tools-concepts.csv                     the catalog: one row per tool (id, title, module)
  data/modules.csv, data/subjects.csv         the subject and grade of each tool's module
  tools/<id>/                                 the stage of a tool, by the files in its folder (see stage())
  data/plans/<course>/days.csv                named by a plan as data: columns tool and mark
  docs/courses/<course>/TOOL-ASKS.md          named by a plan: one "## Title" section per tool with a Mark line,
                                              a Spec line and a day table; "(does not exist)" in a heading; and
                                              the table "Earlier-grade tools named for reteach"
  docs/courses/<course>/[su]NN*.md            cross-check only: a catalog tool named in a sheet or plan that is
                                              not on the asks page is reported, not binned
  docs/agents/catalog/tables/spec-sort.csv    the teaching-test record: the catalog read of every tool
                                              (built by scripts/catalog_maps.py from the extract rows)
  docs/agents/catalog/shape/shape.csv         cross-check only: the stage that docs/COURSES-STATUS.md counts

Definitions, as implemented:
  live      tools/<id>/tool.json exists. This is the definition in scripts/catalog_batch.py, which set the
            `stage` of every extract row; scripts/course_status.py counts that same field for COURSES-STATUS.md.
  passing   the tool's row in spec-sort.csv has sort = "fine": every code it carries was read as taught, with
            no core part of the wording missing. A tool with no row has no teaching-test record and is never
            counted as passing.
  named     the tool is in a days.csv row with a mark, or has a section or a reteach row in a TOOL-ASKS.md.
"""
import csv, datetime, glob, io, os, re, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def P(*p): return os.path.join(ROOT, *p)
def rd(path):
    with io.open(P(path), encoding='utf-8') as f:
        return list(csv.DictReader(f))
def text(path):
    with io.open(path, encoding='utf-8') as f:
        return f.read()

ORDER = ['k', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 'k-2', '3-5', '6-8', '6-12', '9-12', 'k-12']
gkey = lambda g: ORDER.index(g) if g in ORDER else 99

def stage(t):
    """Same test and same order as scripts/catalog_batch.py."""
    for f, s in (('tool.json', 'live'), ('src.html', 'built'), ('spec.md', 'spec'), ('idea.md', 'idea')):
        if os.path.exists(P('tools', t, f)): return s
    return 'none'

# ---- the catalog ------------------------------------------------------------------------------------------------
concepts = {c['tool_id']: c for c in rd('data/tools-concepts.csv')}
modules = {m['module_id']: m for m in rd('data/modules.csv')}
subjects = {s['subject_id']: s['label'] for s in rd('data/subjects.csv')}
sortrow = {r['tool']: r for r in rd('docs/agents/catalog/tables/spec-sort.csv')}
by_title = collections.defaultdict(list)
for c in concepts.values(): by_title[c['title'].strip().lower()].append(c['tool_id'])
folders = sorted(d for d in os.listdir(P('tools')) if os.path.isdir(P('tools', d)))
outside = [d for d in folders if d not in concepts]          # Recess games and Curiosities: not in the catalog
warn = []

def subj(t): return modules[concepts[t]['module_id']]['subject']
def grade(t): return modules[concepts[t]['module_id']]['grade']
def title(t): return concepts[t]['title'] if t in concepts else t

# ---- (a) named by a plan ----------------------------------------------------------------------------------------
# named[key] = dict(id or None, title, mark, course, where[list], kind: 'tool' | 'reteach' | 'missing')
named = collections.OrderedDict()
def name_it(key, **kw):
    d = named.setdefault(key, dict(id=None, title=key, mark='', course='', where=[], kind='tool', note=''))
    for k, v in kw.items():
        if k == 'where': d['where'] += [w for w in v if w not in d['where']]
        elif v: d[k] = v
    return d

# 1. plans as data
for f in sorted(glob.glob(P('data', 'plans', '*', 'days.csv'))):
    course = os.path.basename(os.path.dirname(f))
    per = collections.OrderedDict()
    for r in csv.DictReader(io.open(f, encoding='utf-8')):
        t, m = (r.get('tool') or '').strip(), (r.get('mark') or '').strip().lower()
        if not t: continue
        if m not in ('key', 'light'): warn.append('%s days.csv day %s: tool %s has mark "%s"' % (course, r['day'], t, m))
        per.setdefault(t, dict(mark=m, days=[], units=[]))
        per[t]['days'].append(r['day'])
        if r['unit'] not in per[t]['units']: per[t]['units'].append(r['unit'])
    for t, d in per.items():
        name_it(t, id=t, title=title(t), mark=d['mark'], course=course,
                where=['data/plans/%s/days.csv: section %s, day %s' % (course, ', '.join(d['units']), ', '.join(d['days']))])

# 2. the asks page of each course
def md_rows(lines):
    """Rows of the first pipe table in `lines`, as lists of cells, header and rule dropped."""
    out = []
    for ln in lines:
        if ln.startswith('|'):
            cells = [c.strip() for c in ln.strip().strip('|').split('|')]
            if not all(set(c) <= set('-: ') for c in cells): out.append(cells)
        elif out: break
    return out[1:]

for f in sorted(glob.glob(P('docs', 'courses', '*', 'TOOL-ASKS.md'))):
    course = os.path.basename(os.path.dirname(f))
    rel = 'docs/courses/%s/TOOL-ASKS.md' % course
    parts = re.split(r'(?m)^## +', text(f))[1:]
    for part in parts:
        lines = part.split('\n')
        head = lines[0].strip()
        if head.lower().startswith('earlier-grade tools named for reteach'):
            for cells in md_rows(lines[1:]):
                if len(cells) < 3: continue
                shown = cells[0]
                bare = re.sub(r'\s*\(.*?\)', '', shown).strip()
                ids = by_title.get(bare.lower(), [])
                if len(ids) != 1:
                    warn.append('%s: reteach tool "%s" matches %d catalog titles' % (rel, bare, len(ids)))
                    name_it(bare, title=bare, course=course, kind='missing', note='named for reteach; not found in the catalog',
                            where=['%s, reteach table: %s' % (rel, cells[2])])
                    continue
                d = name_it(ids[0], id=ids[0], title=title(ids[0]), course=course,
                            where=['%s, reteach table: %s' % (rel, cells[2])])
                if not d['mark']: d['kind'] = 'reteach'       # a tool with its own section keeps its mark
            continue
        mm = re.search(r'\*\*Mark\.\*\*\s*([A-Za-z]+)', part)
        mark = mm.group(1).lower() if mm else ''
        if mark not in ('key', 'light'): warn.append('%s: section "%s" has no key or light mark' % (rel, head)); mark = ''
        sm = re.search(r'\*\*Spec\.\*\*\s*tools/([a-z0-9-]+)/', part)
        rows = md_rows(lines[1:])
        dl = []
        for r in rows:
            if r and r[0] and r[0] not in dl: dl.append(r[0])
        days = '; '.join(d if d.lower().startswith('to ') else 'day %s' % d for d in dl)
        days = days.replace('; To day', '; to day')
        plans = sorted(set(re.findall(r'\[([su]\d+(?:-\d+)?)\]', '\n'.join(' '.join(r) for r in rows))))
        where = ['%s: %s%s' % (rel, days or 'no day given', ' (%s)' % ', '.join(plans) if plans else '')]
        if 'does not exist' in head.lower() or not sm:
            bare = re.sub(r'\s*\(does not exist\)', '', head, flags=re.I).strip()
            if 'does not exist' not in head.lower(): warn.append('%s: section "%s" has no Spec line' % (rel, head))
            name_it(bare, title=bare, mark=mark, course=course, kind='missing', where=where)
            continue
        t = sm.group(1)
        if t in named and named[t]['mark'] and mark and named[t]['mark'] != mark:
            warn.append('%s: %s is "%s" here and "%s" in days.csv; days.csv wins' % (rel, t, mark, named[t]['mark']))
            mark = named[t]['mark']
        d = name_it(t, id=t, title=title(t), mark=mark, course=course, where=where)
        d['kind'] = 'tool'
        if not os.path.isdir(P('tools', t)):
            d['kind'] = 'missing'; warn.append('%s: %s has no folder in tools/' % (rel, t))

named_ids = {d['id'] for d in named.values() if d['id']}

# 3. cross-check: catalog tools named in a sheet or plan and missing from the asks page
stray = collections.defaultdict(set)
for f in sorted(glob.glob(P('docs', 'courses', '*', '[su][0-9]*.md'))):
    body = text(f)
    rel = os.path.basename(os.path.dirname(f)) + '/' + os.path.basename(f)
    for t in set(re.findall(r'tools/([a-z0-9-]+)/', body)):
        if t not in named_ids: stray[t].add(rel)
    for t, c in concepts.items():
        if t in named_ids: continue
        if re.search(r'(?<![A-Za-z])' + re.escape(c['title']) + r'(?![A-Za-z])\s*(?:\((?:key|light)\)|:)', body):
            stray[t].add(rel)

# ---- the three bins ---------------------------------------------------------------------------------------------
A, B, C = [], [], []
for d in named.values():
    A.append(d)
for t in sorted(concepts):
    if t in named_ids: continue
    st = stage(t)
    rec = sortrow.get(t)
    if st == 'live' and rec and rec['sort'] == 'fine': B.append(t); continue
    if st != 'live': why = 'not live (%s)' % st
    elif not rec: why = 'no teaching-test record'
    else: why = 'live, read, does not pass (%s)' % rec['sort']
    C.append((t, st, why))

live_all = [t for t in concepts if stage(t) == 'live']
shape_live = {r['tool'] for r in rd('docs/agents/catalog/shape/shape.csv') if r['stage'] == 'live'}
if set(live_all) != shape_live:
    warn.append('live by folder (%d) and live in shape.csv (%d) differ: %s' % (
        len(live_all), len(shape_live), ', '.join(sorted(set(live_all) ^ shape_live))))
no_record = [t for t, st, why in C if why == 'no teaching-test record']
a_tools = [d for d in A if d['kind'] == 'tool']
a_reteach = [d for d in A if d['kind'] == 'reteach']
a_missing = [d for d in A if d['kind'] == 'missing']
a_exist = [d for d in A if d['id'] and d['kind'] != 'missing']
assert len(a_exist) + len(B) + len(C) == len(concepts)

# ---- the page ---------------------------------------------------------------------------------------------------
today = datetime.date.today().isoformat()
out = []
W = out.append
W('# Tool bins: every tool and spec, sorted by demand\n')
W('Generated by scripts/tool_bins.py on %s. Do not edit by hand. Run the script again.\n' % today)
W('**The rule** (BASELINE rule 26; FOUNDATION section 6 item 5; Cory, 2026-11-11). Every tool and spec made before '
  'the rule sits in one of three bins, set by this script and never by inspection.')
W('A tool moves to bin (a) only when a unit or section plan asks for it.\n')
W('| Bin | What it means | Count |')
W('|---|---|---|')
W('| (a) Named by a unit or section plan | Gets course work | %d in the catalog, plus %d asked for and not built |' % (len(a_exist), len(a_missing)))
W('| (b) Live and passing, not named | Stays on the shelf as a free-standing tool. Claims no course coverage | %d |' % len(B))
W('| (c) Everything else | Frozen. No further spend | %d |' % len(C))
W('| All catalog tools | | %d |' % len(concepts))
W('')
W('## How the script decides\n')
W('- **The catalog** is data/tools-concepts.csv: %d tools, each with a folder in tools/.' % len(concepts))
W('- **Named by a plan** means one of two things. The tool is in a day row of data/plans/<course>/days.csv with a '
  'mark. Or it has its own heading, or a row in the reteach table, on a course page docs/courses/<course>/TOOL-ASKS.md. '
  'Where both give a mark, days.csv wins. The scope and sequence does not count: it is not a unit or section plan.')
W('- **Live** means the folder holds tool.json. This is the same test that set the stage counted in '
  'docs/COURSES-STATUS.md. Live tools in the catalog: %d.' % len(live_all))
W('- **Passing the teaching test** (BASELINE rule 21) is read from docs/agents/catalog/tables/spec-sort.csv, the '
  'catalog read of 2026-11-10. A tool passes when its sort is "fine": every code it carries was read as taught, '
  'with no core part of the wording missing. A sort of "small addition" or "rework" does not pass.')
W('- **No record, no pass.** A live tool with no row in that file goes to bin (c) with the reason "no '
  'teaching-test record". That count today: %d.' % len(no_record))
W('- **Limits.** The catalog read is rough and was not made by playing each tool. No built tool has been played '
  'against its spec yet (docs/agents/catalog/verified.txt is empty). A spec fixed after the read does not change '
  'a live tool, because the code still follows the old spec. So bin (b) is what the record says today, no more.\n')

W('## Bin (a): named by a unit or section plan (%d)\n' % (len(a_exist) + len(a_missing)))
W('### Key and light tools (%d)\n' % len(a_tools))
W('| Tool | Folder | Mark | Stage | Course | Where it is named |')
W('|---|---|---|---|---|---|')
for d in sorted(a_tools, key=lambda d: (d['mark'] != 'key', d['title'])):
    W('| %s | %s | %s | %s | %s | %s |' % (d['title'], d['id'], d['mark'] or 'not marked', stage(d['id']), d['course'], '. '.join(d['where'])))
W('')
W('### Earlier tools named only for reteach (%d)\n' % len(a_reteach))
W('A readiness check names each of these as an earlier tool or page. No plan marks them key or light, and no ask '
  'is made of them. They count as named by a plan.\n')
W('| Tool | Folder | Grade | Stage | Course that names it | Where it is named |')
W('|---|---|---|---|---|---|')
for d in sorted(a_reteach, key=lambda d: d['title']):
    W('| %s | %s | %s | %s | %s | %s |' % (d['title'], d['id'], grade(d['id']), stage(d['id']), d['course'], '. '.join(d['where'])))
W('')
W('### Asked for, not built (%d)\n' % len(a_missing))
W('A plan asks for each of these and nothing exists yet: no spec and no folder. They are not counted in the %d '
  'catalog tools.\n' % len(concepts))
W('| Asked for | Mark | Course | Where it is named | Note |')
W('|---|---|---|---|---|')
for d in a_missing:
    W('| %s | %s | %s | %s | %s |' % (d['title'], d['mark'] or 'not marked', d['course'], '. '.join(d['where']), d['note'] or 'asked for, not built'))
W('')
if stray:
    W('### Check: named in a sheet or plan, not on the asks page (%d)\n' % len(stray))
    W('The script found these catalog tools in a unit plan or section plan. They have no heading on the asks page, '
      'so they are not in bin (a). Add a heading if the plan means to use one.\n')
    for t in sorted(stray): W('- %s (%s): %s' % (title(t), t, ', '.join(sorted(stray[t]))))
    W('')

W('## Bin (b): live and passing, not named (%d)\n' % len(B))
W('These stay on the shelf as free-standing tools. They claim no course coverage.\n')
W('| Tool | Folder | Subject | Grade | Codes read |')
W('|---|---|---|---|---|')
for t in sorted(B, key=lambda t: (subj(t), gkey(grade(t)), t)):
    W('| %s | %s | %s | %s | %s |' % (title(t), t, subjects.get(subj(t), subj(t)), grade(t), sortrow[t]['codes']))
W('')

W('## Bin (c): everything else (%d)\n' % len(C))
W('Frozen. No further spend until a unit or section plan asks for one of them.\n')
why_n = collections.Counter(re.sub(r' \(.*', '', why) if why.startswith('not live') else why for _, _, why in C)
st_n = collections.Counter(st for _, st, _ in C)
W('| Why it is here | Count |')
W('|---|---|')
W('| Not live: a spec only | %d |' % st_n['spec'])
W('| Not live: built, not live | %d |' % st_n['built'])
W('| Not live: an idea only | %d |' % st_n['idea'])
if st_n['none']: W('| Not live: empty folder | %d |' % st_n['none'])
for s in ('small addition', 'rework'):
    W('| Live, read, does not pass the teaching test (%s) | %d |' % (s, sum(why == 'live, read, does not pass (%s)' % s for _, _, why in C)))
W('| Live, no teaching-test record | %d |' % len(no_record))
W('| **All of bin (c)** | **%d** |' % len(C))
W('')
W('### By subject\n')
W('| Subject | Spec or idea | Built | Live, does not pass | Live, no record | All |')
W('|---|---|---|---|---|---|')
tab = collections.defaultdict(collections.Counter)
for t, st, why in C:
    k = 'spec' if st in ('spec', 'idea', 'none') else 'built' if st == 'built' else 'norec' if why == 'no teaching-test record' else 'fail'
    tab[subj(t)][k] += 1
for s in sorted(tab, key=lambda s: -sum(tab[s].values())):
    c = tab[s]
    W('| %s | %d | %d | %d | %d | %d |' % (subjects.get(s, s), c['spec'], c['built'], c['fail'], c['norec'], sum(c.values())))
W('')
W('### By subject and grade\n')
W('Each cell is the count in bin (c). The full list is one filter away in docs/spec-fixes/fix-list.csv.\n')
sg = collections.defaultdict(collections.Counter)
for t, st, why in C: sg[subj(t)][grade(t)] += 1
for s in sorted(sg, key=lambda s: -sum(sg[s].values())):
    W('- **%s** (%d): %s' % (subjects.get(s, s), sum(sg[s].values()),
                             ', '.join('%s: %d' % ('K' if g == 'k' else g.replace('k', 'K'), n) for g, n in sorted(sg[s].items(), key=lambda x: gkey(x[0])))))
W('')
lf = sorted((t for t, st, why in C if st == 'live'), key=lambda t: (subj(t), gkey(grade(t)), t))
W('### The live tools in bin (c) (%d)\n' % len(lf))
W('These stay live on the site. Frozen means no further work is spent on them.\n')
W('| Tool | Folder | Subject | Grade | The read says |')
W('|---|---|---|---|---|')
for t in lf:
    W('| %s | %s | %s | %s | %s |' % (title(t), t, subjects.get(subj(t), subj(t)), grade(t), sortrow[t]['sort'] if t in sortrow else 'no teaching-test record'))
W('')

W('## Outside the sort (%d)\n' % len(outside))
W('These folders in tools/ are not in the catalog. They are Recess games and Curiosities. They claim no standard '
  '(FOUNDATION section 6 item 4), so the teaching test does not apply and they are in no bin.\n')
W(', '.join('%s (%s)' % (d, stage(d)) for d in outside) + '\n')

W('## Checks\n')
W('- Bins add up: %d + %d + %d = %d catalog tools.' % (len(a_exist), len(B), len(C), len(concepts)))
W('- Live tools: %d by folder, %d in the stage column that docs/COURSES-STATUS.md counts. %d of them are in bin (a), %d in (b), %d in (c).' % (
    len(live_all), len(shape_live), sum(stage(d['id']) == 'live' for d in a_exist), len(B), len(lf)))
if warn:
    W('- Warnings from this run:')
    for w in warn: W('  - ' + w)
else:
    W('- No warnings from this run.')

page = '\n'.join(out) + '\n'
assert chr(0x2014) not in page and chr(0x2013) not in page
with io.open(P('docs', 'TOOL-BINS.md'), 'w', encoding='utf-8', newline='\n') as f:
    f.write(page)

for w in warn: print('warning:', w)
for t in sorted(stray): print('not on the asks page:', t, sorted(stray[t]))
print('live', len(live_all), '(shape.csv %d)' % len(shape_live), '| outside the sort', len(outside))
print('bin a', len(a_exist), '(key or light %d, reteach %d) plus %d asked for, not built' % (len(a_tools), len(a_reteach), len(a_missing)))
print('bin b', len(B))
print('bin c', len(C), '(no teaching-test record %d)' % len(no_record))

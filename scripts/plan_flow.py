"""Builds the Review Desk's plan flow: every step of docs/PRODUCTION-PATH.md, from pre-work to the last day and
tool, as nodes that light up as the work is done.

Run: python -X utf8 scripts/plan_flow.py out.json   (then ArtifactData set stats/plan from out.json)

Everything the Desk draws comes from here, so the flow adapts: the course list comes from data/courses.csv (via
course_status.py), unit and day counts from data/plans/frames.csv once a frame sets them (estimates until then),
and steps can be added in this file without touching the page.

Where the states come from:
- data/plans/flow-status.csv, one row per node that has moved (node, state, date, note). The lead adds or edits a
  row when a step starts (active) or ends (done). A node with no row is still to do.
- days, unit plans and tools are counted from the repo through scripts/course_status.py.
States: . to do, a active, d done, e on file from before the 2026-11-13 plan (to be re-read in its turn).
"""
import csv, io, json, os, re, subprocess, sys, tempfile, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORDER = ['Social Studies', 'Science', 'English Language Arts', 'Math']   # build order; math last
SHORT = {'English Language Arts': 'ELA', 'Social Studies': 'Social studies'}
GRADES = ['K'] + [str(i) for i in range(1, 13)]
EST_DAYS, EST_UNITS = 150, 16
CODE = {'todo': '.', 'active': 'a', 'done': 'd', 'earlier': 'e'}

def slug(t): return re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')

# course facts from course_status.py
tmp = os.path.join(tempfile.gettempdir(), 'cc-course-status.json')
subprocess.run([sys.executable, '-X', 'utf8', os.path.join(ROOT, 'scripts', 'course_status.py'), tmp],
               check=True, stdout=subprocess.DEVNULL)
CS = json.load(io.open(tmp, encoding='utf-8'))
subj = {s['name']: s for s in CS['subjects']}
summ = {s['name']: s for s in CS['summary']}
strips = {s['title']: s for s in CS.get('strips', [])}

# hand-kept states
led = {}
p = os.path.join(ROOT, 'data', 'plans', 'flow-status.csv')
if os.path.exists(p):
    for r in csv.DictReader(io.open(p, encoding='utf-8')):
        led[r['node']] = CODE.get(r['state'].strip(), '.')
st = lambda nid, default='.': led.get(nid, default)

# real counts, once a course frame sets them: data/plans/frames.csv (course slug, units, days). Until then a
# course shows an estimate, drawn as "about" cells, so the flow grows or shrinks as the frames are written.
frames = {}
p = os.path.join(ROOT, 'data', 'plans', 'frames.csv')
if os.path.exists(p):
    for r in csv.DictReader(io.open(p, encoding='utf-8')):
        frames[r['course'].strip()] = (int(r['units'] or 0) or None, int(r['days'] or 0) or None)
def units_of(c):
    f = frames.get(slug(c['title']), (None, None))[0]
    return (f, False) if f else ((c['units_total'], False) if c.get('units_total') else (EST_UNITS, True))
def days_of(c):
    f = frames.get(slug(c['title']), (None, None))[1]
    return (f, False) if f else ((c['days_total'], False) if c.get('days_total') else (EST_DAYS, True))

def core(name): return [c for c in subj[name]['courses'] if c.get('core')]
def courses(name): return subj[name]['courses']

bands = []
def stage(id_, title, sub, lanes): bands.append(dict(type='stage', id=id_, title=title, sub=sub, lanes=lanes))
def mile(id_, title, sub): bands.append(dict(type='milestone', id=id_, title=title, sub=sub, s=st(id_)))
def N(id_, label, default='.'): return [id_, label, st(id_, default)]

stage('pre', 'Pre-work', 'Make the social studies standard usable, scout a base text, set the measures, make the expert reader good enough', [
    dict(title='Social studies standard', nodes=[N('P1a', 'Load the Massachusetts standards'), N('P1b', 'Redraw the course list'),
         N('P1c', 'Name the check states'), N('P1d', 'Design the replaced state-study year'), N('P1e', 'Psychology and electives')]),
    dict(title='Base text and rules', nodes=[N('P2', 'Scout a social studies base text'), N('P3', 'Replace rule 25'),
         N('P4', 'Set probe and guard measures')]),
    dict(title='The expert reader', nodes=[N('P5a', 'Subject lenses'), N('P5b', 'Science and social studies bars'),
         N('P5c', 'Briefs for the new layers'), N('P5d', 'Calibration test, expert and Codex')]),
])

def prog_default(name, g):
    return 'e' if name == 'Math' and g in ('3', '4', '5') else '.'
stage('prog', 'Progressions', 'What each grade owns, assumes and hands on, per subject, K to 12; then one review across all four', [
    dict(title=SHORT.get(n, n), nodes=[N(f'prog:{slug(n)}:{g}', f'{SHORT.get(n, n)}, grade {g}', prog_default(n, g)) for g in GRADES]
         + [N(f'prog-review:{slug(n)}', f'{SHORT.get(n, n)}: expert read')]) for n in ORDER
] + [dict(title='Across subjects', nodes=[N('prog-review:all', 'One read across all four')])])

def frame_default(c): return 'e' if c.get('days_total') else '.'
stage('frames', 'Course frames', 'Grades, standards and skills owned, day total, unit list, source map: one per core course', [
    dict(title=SHORT.get(n, n), nodes=[N(f'frame:{slug(c["title"])}', c['title'], frame_default(c)) for c in core(n)]) for n in ORDER
] + [dict(title='Checks', nodes=[N('b1:review', 'Whole-structure review'), N('b1:site', 'Website design check'), N('b1:codex', 'Codex read')])])
mile('baseline1', 'Baseline 1', 'Every progression and course frame reviewed; the site checked against the hierarchy')

MILE = {'Social Studies': ('baseline2', 'Baseline 2', 'Social studies reviewed from the progression down, probe read, template fixed once'),
        'Science': ('m-science', 'Science reviewed', 'From the progression down, probe read'),
        'English Language Arts': ('m-ela', 'ELA reviewed', 'From the progression down, probe read'),
        'Math': ('m-math', 'Math reviewed', 'Old work converted, from the progression down, probe read')}
for n in ORDER:
    s, cs = slug(n), core(n)
    unit_lanes = []
    for c in cs:
        k = slug(c['title']); tot, est = units_of(c)
        have = c.get('units') or 0
        cells = ''.join(st(f'unit:{k}:{i + 1}', 'e' if i < have else '.') for i in range(tot))
        unit_lanes.append(dict(title=c['title'], est=est, cells=cells))
    stage(f'cycle:{s}', SHORT.get(n, n), 'Scope and sequence for every course, review, unit plans, review, probe', [
        dict(title='Scope and sequence', nodes=[N(f'ss:{slug(c["title"])}', c['title'], 'e' if c.get('days_total') else '.') for c in cs]
             + [N(f'ss-review:{s}', 'Review')]),
        dict(title='Probe', nodes=[N(f'units-review:{s}', 'Units review'), N(f'probe:{s}', 'Probe: a few days written and read')]),
    ] + [dict(title='Unit plans', group=True, rows=unit_lanes)])
    mile(*MILE[n])
mile('final', 'Final review', 'Every core subject and course, from the progressions down; Codex reads a sample')

stage('guard', 'The guard', 'A few days in each subject written from the unit plans and measured before full writing', [
    dict(title='Guard', nodes=[N(f'guard:{slug(n)}', SHORT.get(n, n)) for n in ORDER])])

rows = []
for n in ORDER:
    for c in core(n):
        strip = strips.get(c['title'])
        if strip:
            cells = ''.join('e' if x in ('written', 'cheap', 'read', 'taught') else '.' for x in strip['days'])
        n_days, est = days_of(c)
        if not strip:
            cells = '.' * n_days
        else:
            cells = (cells + '.' * n_days)[:n_days]
        # a day's state beyond what the repo shows (for example active writing) comes from day:<course>:<n> rows
        cells = ''.join(led.get(f'day:{slug(c["title"])}:{i + 1}', ch) for i, ch in enumerate(cells))
        rows.append(dict(title=c['title'], group=SHORT.get(n, n), est=est, cells=cells))
bands.append(dict(type='rows', id='days', title='Sections, days and lessons',
                  sub='Every teaching day of every core course, each read by the cheap and expert readers; courses finished whole', rows=rows))

tool_rows = []
for n in ORDER:
    r = summ[n]
    total, live = (r.get('spec') or 0) + (r.get('built') or 0) + (r.get('live') or 0), r.get('live') or 0
    tool_rows.append(dict(title=SHORT.get(n, n), group='Tools', cells='e' * live + '.' * (total - live)))
bands.append(dict(type='rows', id='tools', title='Tools', sub='Built or rebuilt for the sections that name them, live and verified. Tools live today stay on the shelf until a section names them', rows=tool_rows, dots=True))

after = [dict(title=s['name'], nodes=[[f'after:{slug(c["title"])}', c['title'], '.'] for c in s['courses']])
         for s in CS['subjects'] if s['name'] not in ORDER]
bands.append(dict(type='stage', id='after', title='After the core', sub='The other 49 courses, once the core subjects are done', lanes=after, faint=True))

def rle(cs):
    out, i = [], 0
    while i < len(cs):
        j = i
        while j < len(cs) and cs[j] == cs[i]: j += 1
        out.append(f'{cs[i]}{j - i}'); i = j
    return ''.join(out)
for b in bands:
    for l in b.get('lanes', []):
        for r in l.get('rows', []): r['rle'] = rle(r['cells'])
    for r in b.get('rows', []): r['rle'] = rle(r['cells'])
def strip_cells(o):
    if isinstance(o, dict): return {k: strip_cells(v) for k, v in o.items() if k != 'cells'}
    if isinstance(o, list): return [strip_cells(v) for v in o]
    return o

# saved for later: data/plans/later.csv (id, state open/done, added, who, title, when, detail). Anything the work
# sets aside until a trigger (a file Cory saves by hand, a reread before a unit cites something) gets a row here.
later = []
p = os.path.join(ROOT, 'data', 'plans', 'later.csv')
if os.path.exists(p):
    later = [dict(r) for r in csv.DictReader(io.open(p, encoding='utf-8'))]

out = dict(at=datetime.datetime.now().isoformat(timespec='minutes'), bands=bands, later=later,
           note='From docs/PRODUCTION-PATH.md (draft 5). Day and unit counts marked "about" are estimates until each course frame sets them.')
io.open(sys.argv[1], 'w', encoding='utf-8').write(json.dumps(strip_cells(out), separators=(',', ':')))
cnt = {}
def tally(cs):
    for ch in cs: cnt[ch] = cnt.get(ch, 0) + 1
for b in bands:
    for l in b.get('lanes', []):
        tally(x[2] for x in l.get('nodes', []))
        for r in l.get('rows', []): tally(r['cells'])
    for r in b.get('rows', []): tally(r['cells'])
print('nodes by state:', cnt, 'bytes:', os.path.getsize(sys.argv[1]))

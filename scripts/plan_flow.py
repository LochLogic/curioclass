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
# the join is the frame slug: a core course's title in course_status.py slugs to its frame folder name
# ("Science, Grade 4" -> science-grade-4); a core course of the four subjects with no frame row is reported, not guessed
for _n in ORDER:
    for _c in [c for c in subj[_n]['courses'] if c.get('core')]:
        if frames and not _c.get('course'):
            print('plan_flow: no frames.csv row for core course "%s" (slug %s)' % (_c['title'], slug(_c['title'])), file=sys.stderr)
def fid(c): return c.get('course') or slug(c['title'])   # the frame slug from course_status.py
def units_of(c):
    f = frames.get(fid(c), (None, None))[0]
    return (f, False) if f else ((c['units_total'], False) if c.get('units_total') else (EST_UNITS, True))
def days_of(c):
    f = frames.get(fid(c), (None, None))[1]
    return (f, False) if f else ((c['days_total'], False) if c.get('days_total') else (EST_DAYS, True))

def core(name): return [c for c in subj[name]['courses'] if c.get('core')]
def courses(name): return subj[name]['courses']

bands = []
names, flinks = {}, {}   # unit labels and the file each finished step opens (repo path)
def stage(id_, title, sub, lanes): bands.append(dict(type='stage', id=id_, title=title, sub=sub, lanes=lanes))
def mile(id_, title, sub): bands.append(dict(type='milestone', id=id_, title=title, sub=sub, s=st(id_)))
def N(id_, label, default='.'): return [id_, label, st(id_, default)]

stage('pre', 'Pre-work', 'Groundwork before any course is planned. Make the social studies standard usable, pick a base text, set the measures, and prove the expert reader is good enough.', [
    dict(title='Social studies standard', nodes=[N('P1a', 'Load the Massachusetts standards'), N('P1b', 'Redraw the course list'),
         N('P1c', 'Name the check states'), N('P1d', 'Design the replaced state-study year'), N('P1e', 'Psychology and electives')]),
    dict(title='Base text and rules', nodes=[N('P2', 'Scout a social studies base text'), N('P3', 'Replace rule 25'),
         N('P4', 'Set probe and guard measures')]),
    dict(title='The expert reader', nodes=[N('P5a', 'Subject lenses'), N('P5b', 'Science and social studies bars'),
         N('P5c', 'Briefs for the new layers'), N('P5d', 'Calibration test, expert and Codex')]),
])

def prog_default(name, g):
    return 'e' if name == 'Math' and g in ('3', '4', '5') else '.'
stage('prog', 'Progressions', 'For each subject, what every grade owns, assumes from the grade before and hands on to the next, K to 12. Each subject is written, read twice and fixed; then one read checks all four together.', [
    dict(title=SHORT.get(n, n), nodes=[N(f'prog:{slug(n)}:{g}', f'{SHORT.get(n, n)}, grade {g}', prog_default(n, g)) for g in GRADES]
         + [N(f'prog-review:{slug(n)}', f'{SHORT.get(n, n)}: expert read')]) for n in ORDER
] + [dict(title='Across subjects', nodes=[N('prog-review:all', 'One read across all four')])])

def frame_default(c): return 'e' if c.get('days_total') else '.'
stage('frames', 'Course frames', 'One page per core course: its grades, the standards and skills it owns, its number of days, its unit list and a map of the base text. Three checks then review the whole structure and the website.', [
    dict(title=SHORT.get(n, n), nodes=[N(f'frame:{slug(c["title"])}', c['title'], frame_default(c)) for c in core(n)]) for n in ORDER
] + [dict(title='Checks', nodes=[N('b1:review', 'Whole-structure review'), N('b1:site', 'Website design check'), N('b1:codex', 'Codex read'), N('b1:pages', 'Course pages from the frames')])])
mile('baseline1', 'Baseline 1', 'Every progression and course frame has been reviewed. The website matches the plan from subject down to course.')

MILE = {'Social Studies': ('baseline2', 'Baseline 2', 'Social studies is reviewed from the progression down and its probe is read. Any fix to the day template is made here once, for every subject.'),
        'Science': ('m-science', 'Science reviewed', 'Science is reviewed from the progression down and its probe is read.'),
        'English Language Arts': ('m-ela', 'ELA reviewed', 'ELA is reviewed from the progression down and its probe is read.'),
        'Math': ('m-math', 'Math reviewed', 'The older math work is converted to the new plan. Then math is reviewed from the progression down and its probe is read.')}
for n in ORDER:
    s, cs = slug(n), core(n)
    unit_lanes = []
    for c in cs:
        k = slug(c['title']); tot, est = units_of(c)
        have = c.get('units') or 0
        cells = ''.join(st(f'unit:{k}:{i + 1}', 'e' if i < have else '.') for i in range(tot))
        unit_lanes.append(dict(title=c['title'], est=est, cells=cells, k=k))
        for i in range(tot):
            f = os.path.join('docs', 'courses', fid(c), 's%02d.md' % (i + 1))
            if os.path.exists(os.path.join(ROOT, f)):
                head = io.open(os.path.join(ROOT, f), encoding='utf-8').readline()
                t_ = re.sub(r'\*+', '', head.split(':', 1)[1]) if ':' in head else ''
                t_ = re.split(r'\s*\(|\.\s|\?|\.$', t_.strip())[0].strip().rstrip('.')
                names[f'unit:{k}:{i + 1}'] = 'Unit %d: %s' % (i + 1, t_) if t_ else 'Unit %d' % (i + 1)
                flinks[f'unit:{k}:{i + 1}'] = ['The unit plan', f]
        for name, node in (('scope-and-sequence.md', f'ss:{k}'), ('frame.md', f'frame:{k}')):
            f = os.path.join('docs', 'courses', fid(c), name)
            if os.path.exists(os.path.join(ROOT, f)):
                flinks[node] = ['The ' + ('scope and sequence' if name.startswith('scope') else 'course frame'), f]
    stage(f'cycle:{s}', SHORT.get(n, n), 'Each course gets its scope and sequence (the units in order), then a plan for every unit, each reviewed. A probe then writes a few real days to test the plans.', [
        dict(title='Scope and sequence', nodes=[N(f'ss:{slug(c["title"])}', c['title'], 'e' if c.get('days_total') else '.') for c in cs]
             + [N(f'ss-review:{s}', 'Review')]),
        dict(title='Unit plans', group=True, rows=unit_lanes),
        dict(title='Review and probe', nodes=[N(f'units-review:{s}', 'Units review'), N(f'probe:{s}', 'Probe: a few days written and read')]),
    ])
    mile(*MILE[n])
mile('final', 'Final review', 'Every core course is reviewed from the progressions down. Codex reads a sample as a second check.')

stage('guard', 'The guard', 'A few days in each subject are written from the unit plans and measured. Full writing starts only once they pass.', [
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
                  sub='Every teaching day of every core course, written and then read by the cheap and expert readers. Courses are finished whole, not a few days at a time.', rows=rows))

tool_rows = []
for n in ORDER:
    r = summ[n]
    total, live = (r.get('spec') or 0) + (r.get('built') or 0) + (r.get('live') or 0), r.get('live') or 0
    tool_rows.append(dict(title=SHORT.get(n, n), group='Tools', cells='e' * live + '.' * (total - live)))
bands.append(dict(type='rows', id='tools', title='Tools', sub='Interactive tools, built or rebuilt only for the sections that call for them, then checked live. Tools live today wait on the shelf until a section names them.', rows=tool_rows, dots=True))

# after the core (Cory 2026-11-14: "build out the after the core subjects into our core framework so i can better
# visualize the massive workload ahead"): the same steps as a core subject, drawn faint, every count an estimate until
# a frame sets it. The core electives come first, then each other subject in the catalog's order.
def after_cycle(id_, title, cs, sub, pre=True):
    lanes = []
    if pre:
        lanes.append(dict(title='Pre-work', nodes=[N(f'pre:{id_}', 'Bar work owed'), N(f'prog:{id_}', 'Progression')]))
    lanes += [dict(title='Course frames', nodes=[N(f'frame:{slug(c["title"])}', c['title']) for c in cs]),
              dict(title='Scope and sequence', nodes=[N(f'ss:{slug(c["title"])}', c['title']) for c in cs] + [N(f'ss-review:{id_}', 'Review')])]
    urows = []
    for c in cs:
        tot, est = units_of(c)
        urows.append(dict(title=c['title'], est=est, cells=''.join(st(f'unit:{slug(c["title"])}:{i + 1}') for i in range(tot)), k=slug(c['title'])))
    lanes.append(dict(title='Unit plans', group=True, rows=urows))
    lanes.append(dict(title='Review and probe', nodes=[N(f'units-review:{id_}', 'Units review'), N(f'probe:{id_}', 'Probe')]))
    bands.append(dict(type='stage', id=f'after:{id_}', title=title, sub=sub, lanes=lanes, faint=True))
    group = title.replace('After the core: ', '').replace(' (shelved)', '')
    return [(group[0].upper() + group[1:], c) for c in cs]   # each course with its subject, for the days groups

after_cs = []
electives = [c for n in ORDER for c in courses(n) if not c.get('core')]
if electives:
    after_cs += after_cycle('electives', 'After the core: core electives', electives,
                            'Precalculus, statistics, calculus, earth and space science, environmental science and psychology: the first courses after the core, built on the progressions of the core subjects.', pre=False)
for s_ in CS['subjects']:
    if s_['name'] in ORDER:
        continue
    shelved = s_['name'] == 'World Languages'
    after_cs += after_cycle(slug(s_['name']), 'After the core: ' + s_['name'] + (' (shelved)' if shelved else ''), s_['courses'],
                            ('Shelved 2026-11-11; counted so the whole is visible. ' if shelved else '')
                            + 'The same steps as a core subject: the bar work this subject owes first, then its progression, frames, scopes and sequences and unit plans. Counts are estimates until each frame is written.')
n_after = len(after_cs)
arows = []
for grp, c in after_cs:     # grouped by subject so each gets its own days bar on the Desk
    n_days, est = days_of(c)
    arows.append(dict(title=c['title'], group=grp, est=est, cells=''.join(st(f'day:{slug(c["title"])}:{i + 1}') for i in range(n_days))))
bands.append(dict(type='rows', id='after-days', title='After the core: days', sub='Every teaching day of the other %d courses, at about %d days a course until each frame sets its count.' % (n_after, EST_DAYS), rows=arows, faint=True))

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
# what each step is, in plain words, for the Desk's click bubbles. Keyed by node id, or by its kind (the part
# before the first colon), or by a row kind. Short: a line or two, or a few bullets ("- " lines).
ABOUT = {
    'P1a': "Load the Massachusetts social studies standards into the repo, in our own words, so every later step can point at them.",
    'P1b': "Redraw the social studies course list to follow the Massachusetts order, moving topics and worksheets without breaking links.",
    'P1c': "Choose the other states and national references every social studies unit is checked against.",
    'P1d': "Design the grade 3 year that replaces a single-state study, so it works for students in any state.",
    'P1e': "Decide where psychology and the social studies electives go: after the core subjects.",
    'P2': "Look for a free, openly licensed social studies textbook to build from. None met the bar, so social studies is written as Curio Class's own.",
    'P3': "Replace the old rule (prove at the bottom first) with the new build order: plan from the top down, test with a probe and a guard.",
    'P4': "Set the lines the probe and the guard are measured against, so a pass or fail is a number, not a feeling.",
    'P5a': "Give the expert reader a lens per subject: what a strong reviewer of that subject looks for, with sources.",
    'P5b': "Write the bar for science and social studies (what adoption reviewers expect), as math and ELA already had.",
    'P5c': "Write the job sheets the readers and writers follow for the new planning layers.",
    'P5d': "Test both readers (the expert agent and Codex) on work with planted faults, to see if they can be trusted.",
    'prog': "This grade's list of skills in this subject: what it owns, what it assumes from the grade before, and what it hands on to the next.",
    'prog-review': "Two independent readers (the expert and Codex) read this subject's whole progression cold; one fix pass applies what they find. Only big items go to the Desk.",
    'prog-review:all': ('Two readers check where the four subjects meet:\n'
                        '- Timing: a lean on another subject only uses what that subject has already taught\n'
                        '- Missing links: the same idea taught twice with neither side knowing\n'
                        '- One name for one tool across subjects\n'
                        '- No year overloaded with hard new ideas at once\n'
                        '- Reading topics line up with science and social studies\n'
                        '- Sensitive topics handled the same way everywhere'),
    'frame': "One page for this course: its grades, the standards and skills it owns, its number of days, its unit list with a reason for each, and a map of the base text.",
    'b1:review': "A read of the whole structure at once: every progression and frame, checking they fit together.",
    'b1:site': "Check the website's pages and links match the plan, from subject down to course.",
    'b1:codex': "Codex reads the progressions and frames as a second, independent reader.",
    'b1:pages': "Build the course and unit pages for all 52 core courses from the frames, hidden from the live site until Cory says.",
    'ss': "The scope and sequence for this course: its units in order, each with what it teaches and roughly how many days.",
    'ss-review': "The expert reads every scope and sequence in this subject together; one fix pass follows.",
    'units-review': "The expert reads this subject's unit plans together before any days are written.",
    'probe': "A few real days are written from the unit plans and read, to test the plans before full writing.",
    'guard': "A few days written from the unit plans and measured against set lines. Full writing in this subject starts only once they pass.",
    'after': "A course outside the four core subjects. It starts once the core is done.",
    'baseline1': "A checkpoint: every progression and course frame reviewed, and the website matches the plan.",
    'baseline2': "A checkpoint: social studies reviewed top to bottom and its probe read. Any fix to the day template is made here, once.",
    'm-science': "A checkpoint: science reviewed from the progression down, probe read.",
    'm-ela': "A checkpoint: ELA reviewed from the progression down, probe read.",
    'm-math': "A checkpoint: older math work converted to the new plan, then reviewed from the progression down, probe read.",
    'final': "A checkpoint: every core course reviewed from the progressions down; Codex reads a sample.",
    'row:units': "The unit plans for this course, one cell a unit. Dashed cells are an estimate until the course frame sets the count.",
    'row:days': "Every teaching day of this course, one cell a day: written, then read by the cheap and the expert readers.",
    'row:tools': "The interactive tools in this subject, one dot a tool. Lit dots are live and verified.",
}
info = {}
p = os.path.join(ROOT, 'data', 'plans', 'flow-status.csv')
if os.path.exists(p):
    for r in csv.DictReader(io.open(p, encoding='utf-8')):
        info[r['node']] = [r.get('date') or '', r.get('note') or '']

# what was found or changed, for the bubbles of finished steps. Reviews: a short hand-written result in
# data/plans/flow-results.csv (node,result), written when the fix pass closes the step. Grade progressions: counted
# from the data, so they never go stale.
found = {}
p = os.path.join(ROOT, 'data', 'plans', 'flow-results.csv')
if os.path.exists(p):
    for r in csv.DictReader(io.open(p, encoding='utf-8')):
        found[r['node']] = ['What was found', r['result']]
PFILE = {'social-studies': 'social-studies', 'science': 'science', 'english-language-arts': 'ela', 'math': 'math'}
for s, f in PFILE.items():
    p = os.path.join(ROOT, 'data', 'progressions', f + '.csv')
    if not os.path.exists(p):
        continue
    by = {}
    for r in csv.DictReader(io.open(p, encoding='utf-8')):
        by.setdefault(r['grade'].strip(), []).append(r)
    for g, rs in by.items():
        codes = [c.strip() for r in rs for c in (r['standard'] or '').split(';') if c.strip()]
        own = len({c for c in codes if not c.startswith('~')})
        part = len({c for c in codes if c.startswith('~')})
        links = sum(len([x for x in (r['cross_subject'] or '').split(';') if x.strip()]) for r in rs)
        std = ', '.join(x for x in [f'{own} standards owned' if own else '',
                                    f'{part} started here and finished in a later grade' if part else ''] if x)
        txt = f'{len(rs)} skills; {std}; {links} links to other subjects.'
        found[f'prog:{s}:{g}'] = ['In this grade', txt]

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

LINKS_EXTRA = {'units-review:social-studies': ['The structure pass report', 'docs/reviews/ss-units-structure-pass-2026-11-14.md']}
for n_, v_ in LINKS_EXTRA.items():
    flinks.setdefault(n_, v_)
REPO = 'https://github.com/LochLogic/curioclass/blob/main/'
flinks = {n_: [v_[0], REPO + v_[1].replace(os.sep, '/')] for n_, v_ in flinks.items()}
out = dict(names=names, links=flinks, at=datetime.datetime.now().isoformat(timespec='minutes'), bands=bands, later=later, about=ABOUT, info=info, found=found,
           note='From docs/PRODUCTION-PATH.md (draft 5). Day and unit counts marked "about" are estimates until each course frame sets them.')
io.open(sys.argv[1], 'w', encoding='utf-8').write(json.dumps(strip_cells(out), separators=(',', ':')))
# A Desk document holds at most 256 KB, so the plan also goes out as parts: <out>.parts/plan-c<i>.json, each
# {"stamp", "i", "n", "s"} with s a slice of the JSON text. The Desk joins the parts that share a stamp once all n
# are in, so the plan has no size cap (each publish sends every part; ArtifactData batch, at most 1 MiB a call).
_txt = json.dumps(strip_cells(out), separators=(',', ':'))
_stamp = out['at'] + ':' + str(len(_txt))
_chunk = 100000
_parts = [_txt[i:i + _chunk] for i in range(0, len(_txt), _chunk)] or ['']
_dir = sys.argv[1] + '.parts'
os.makedirs(_dir, exist_ok=True)
for _f in os.listdir(_dir):
    if _f.startswith('plan-c'):
        os.remove(os.path.join(_dir, _f))
for _i, _s in enumerate(_parts):
    io.open(os.path.join(_dir, 'plan-c%d.json' % _i), 'w', encoding='utf-8').write(
        json.dumps(dict(stamp=_stamp, i=_i, n=len(_parts), s=_s), separators=(',', ':')))
print('parts:', len(_parts), 'in', _dir)
cnt = {}
def tally(cs):
    for ch in cs: cnt[ch] = cnt.get(ch, 0) + 1
for b in bands:
    for l in b.get('lanes', []):
        tally(x[2] for x in l.get('nodes', []))
        for r in l.get('rows', []): tally(r['cells'])
    for r in b.get('rows', []): tally(r['cells'])
print('nodes by state:', cnt, 'bytes:', os.path.getsize(sys.argv[1]))

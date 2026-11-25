"""Builds the Review Desk's plan flow: the seven stages of docs/COURSE-RUN.md (pre-work to course finish), the same
for every subject, as nodes that light up as the work is done. The core four are drawn bright, every other course faint.

Run: python -X utf8 scripts/plan_flow.py out.json   (then ArtifactData set stats/plan from out.json)

Everything the Desk draws comes from here, so the flow adapts: the course list comes from data/courses.csv (via
course_status.py), unit and day counts from data/plans/frames.csv once a frame sets them (estimates until then),
and steps can be added in this file without touching the page.

Where the states come from:
- data/plans/flow-status.csv, one row per node that has moved (node, state, date, note). The lead adds or edits a
  row when a step starts (active) or ends (done). A node with no row is still to do.
- unit plans and tools are counted from the repo through scripts/course_status.py; section plans from the plan
  files, items.csv and the answer-key reads; days from courses/<course>/u*/dNNN.md, done once the grade's sample
  read (docs/reviews/ladder-sample-<course>-a-*.md) is filed.
States: . to do, a active, d done, e on file from before the 2026-11-13 plan (to be re-read in its turn).
"""
import csv, glob, io, json, os, re, subprocess, sys, tempfile, datetime

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
# the join is the course id (data/plans/course-list.csv, the frame slug); a core course of the four subjects with no
# frame row is reported, not guessed
for _n in ORDER:
    for _c in [c for c in subj[_n]['courses'] if c.get('core')]:
        if frames and _c['course'] not in frames:
            print('plan_flow: no frames.csv row for core course "%s" (slug %s)' % (_c['title'], _c['course']), file=sys.stderr)
def fid(c): return c['course']   # the course id from data/plans/course-list.csv
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

# The seven stages of docs/COURSE-RUN.md (draft 3, adopted 2026-11-20), the same for every subject. Each stage is
# one band with a lane per subject: the four core subjects bright, then the core electives and the other subjects
# faint (lane `faint`), every count an estimate until a frame sets it. Node ids are kept from the earlier
# PRODUCTION-PATH flow, so every state in flow-status.csv still lights the same step.
SUBJ_ORDER = ['Social Studies', 'Science', 'English Language Arts', 'Math']   # how the lanes are listed
electives = [c for n in SUBJ_ORDER for c in courses(n) if not c.get('core')]
others = [s_ for s_ in CS['subjects'] if s_['name'] not in SUBJ_ORDER]
AFTER = ([('core-electives', 'Core electives', electives, False)] if electives else []) + \
        [(slug(s_['name']), s_['name'] + (' (shelved)' if s_['name'] == 'World Languages' else ''), s_['courses'], True) for s_ in others]
def sname(n): return SHORT.get(n, n)

def prog_default(name, g):
    return 'e' if name == 'Math' and g in ('3', '4', '5') else '.'
def frame_default(c): return 'e' if c.get('days_total') else '.'

def day_files(c):
    """Day numbers written for a course: courses/<course>/u*/dNNN.md."""
    out = set()
    for f in glob.glob(os.path.join(ROOT, 'courses', fid(c), 'u*', 'd[0-9][0-9][0-9].md')):
        out.add(int(os.path.basename(f)[1:4]))
    return out
def grade_closed(c):
    """A grade closes when its sample read is filed (COURSE-RUN stage 6: two fresh readers, 10 days)."""
    return bool(glob.glob(os.path.join(ROOT, 'docs', 'reviews', 'ladder-sample-%s-a-*.md' % fid(c))))

# 1. Pre-work
stage('pre', '1. Pre-work', 'Once per subject: the standard in our own words, the approach, a base text, the expert reader and its bar, the course list and shape, the dose. The expert must catch planted faults before it is trusted.', [
    dict(title='Social studies standard', nodes=[N('P1a', 'Load the Massachusetts standards'), N('P1b', 'Redraw the course list'),
         N('P1c', 'Name the check states'), N('P1d', 'Design the replaced state-study year'), N('P1e', 'Psychology and electives')]),
    dict(title='Base text and rules', nodes=[N('P2', 'Scout a social studies base text'), N('P3', 'Replace rule 25'),
         N('P4', 'Set probe and guard measures')]),
    dict(title='The expert reader', nodes=[N('P5a', 'Subject lenses'), N('P5b', 'Science and social studies bars'),
         N('P5c', 'Briefs for the new layers'), N('P5d', 'Calibration test, expert and Codex')]),
] + [dict(title=t, faint=True, nodes=[N(f'pre:{i}', 'Pre-work')]) for i, t, cs, pre in AFTER if pre])

# 2. Progression
stage('prog', '2. Progression', 'Once per subject, all grades: what every grade owns, assumes from the grade before and hands on, written blind by band, then stitched and read. The subject ledger is seeded here.', [
    dict(title=sname(n), nodes=[N(f'prog:{slug(n)}:{g}', f'{sname(n)}, grade {g}', prog_default(n, g)) for g in GRADES]
         + [N(f'prog-review:{slug(n)}', f'{sname(n)}: expert read')]) for n in SUBJ_ORDER
] + [dict(title='Across subjects', nodes=[N('prog-review:all', 'One read across all four')])]
  + [dict(title=t, faint=True, nodes=[N(f'prog:{i}', 'Progression')]) for i, t, cs, pre in AFTER if pre])

# 3. Course frames, then scopes and sequences
lanes3 = []
for n in SUBJ_ORDER:
    cs = core(n)
    lanes3.append(dict(title=sname(n) + ' frames', nodes=[N(f'frame:{fid(c)}', c['title'], frame_default(c)) for c in cs]))
    lanes3.append(dict(title=sname(n) + ' scopes and sequences', nodes=[N(f'ss:{fid(c)}', c['title'], 'e' if c.get('days_total') else '.') for c in cs]
                       + [N(f'ss-review:{slug(n)}', 'Review')]))
lanes3.append(dict(title='Checks', nodes=[N('b1:review', 'Whole-structure review'), N('b1:site', 'Website design check'), N('b1:codex', 'Codex read'),
                                          N('b1:pages', 'Course pages from the frames'), N('baseline1', 'Baseline 1: frames reviewed')]))
lanes3.append(dict(title='Gate: owner approves the baseline', nodes=[N(f'gate3:{slug(n)}', sname(n)) for n in SUBJ_ORDER]))
for i, t, cs, pre in AFTER:
    lanes3.append(dict(title=t + ' frames', faint=True, nodes=[N(f'frame:{fid(c)}', c['title']) for c in cs]))
    lanes3.append(dict(title=t + ' scopes and sequences', faint=True, nodes=[N(f'ss:{fid(c)}', c['title']) for c in cs]
                       + [N(f'ss-review:{i}', 'Review')]))
    lanes3.append(dict(title=t + ': gate', faint=True, nodes=[N(f'gate3:{i}', 'Owner approves the baseline')]))
stage('frames', '3. Course frames, then scopes and sequences', 'Per course, grades in order, pilot course first. A frame holds the owned skills, dose, session count, units and source map; the scope and sequence holds every day in order, the checks and the calendar fit.', lanes3)

# 4. Unit plans
# A unit plan is done only while it meets the stage 4 bar of COURSE-RUN: since L87 (2026-11-22) that includes field
# 5's Goal map, checked by scripts/unitplan.py (its exit-kind and practice-shape lines). A plan marked done in
# flow-status.csv that fails those lines shows as on file (e), to be brought up to the bar in its turn.
_up = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(ROOT, 'scripts', 'unitplan.py'), 'check'],
                     capture_output=True, text=True, encoding='utf-8', cwd=ROOT).stdout
below_bar = set(re.findall(r'^FAIL (?:exit-kind|practice-shape): (\S+?\.md):', _up, re.M))

def unit_state(nid, path, default):
    s_ = st(nid, default)
    return 'e' if s_ == 'd' and path in below_bar else s_

lanes4 = []
for n in SUBJ_ORDER:
    unit_lanes = []
    for c in core(n):
        k = fid(c); tot, est = units_of(c)
        have = c.get('units') or 0
        cells = ''.join(unit_state(f'unit:{k}:{i + 1}', 'docs/courses/%s/s%02d.md' % (fid(c), i + 1),
                                   'e' if i < have else '.') for i in range(tot))
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
    lanes4.append(dict(title=sname(n), group=True, rows=unit_lanes))
lanes4.append(dict(title='Reads', nodes=[N(f'units-review:{slug(n)}', sname(n)) for n in SUBJ_ORDER]))
lanes4.append(dict(title='Gate: cold read, then owner approval', nodes=[N(f'gate4:{slug(n)}', sname(n)) for n in SUBJ_ORDER]))
for i, t, cs, pre in AFTER:
    urows = []
    for c in cs:
        tot, est = units_of(c)
        urows.append(dict(title=c['title'], est=est, cells=''.join(st(f'unit:{fid(c)}:{j + 1}') for j in range(tot)), k=fid(c)))
    lanes4.append(dict(title=t, group=True, rows=urows, faint=True))
    lanes4.append(dict(title=t + ': reads', faint=True, nodes=[N(f'units-review:{i}', 'Units review')]))
    lanes4.append(dict(title=t + ': gate', faint=True, nodes=[N(f'gate4:{i}', 'Cold read, then owner approval')]))
stage('units', '4. Unit plans', 'Per course, units in order. Each goal names its exit kind, a practice of a different shape and review entries that point at earlier ledger rows. One cold read from the progression down, then owner approval.', lanes4)

# 5. Section plans, plan data and keys: one cell a section, from days.csv's `unit` column (the section id, 5.2).
# A section is done when its plan (docs/courses/<course>/u<uu>-<s>.md), its plan data (items.csv rows for the
# section) and its unit's answer-key read (docs/reviews/answer-key-<course>-u<uu>-*.md) are all in; under way once
# the plan is written. A unit not yet split holds one placeholder `N.1` section longer than six days, drawn as an
# estimate of one section per five days. A flow-status row section:<course>:<u>.<s> overrides the state.
def section_cells(c):
    k, p = fid(c), os.path.join(ROOT, 'data', 'plans', fid(c), 'days.csv')
    secs, est = {}, False
    if os.path.exists(p):
        for r in csv.DictReader(io.open(p, encoding='utf-8')):
            u = (r.get('unit') or '').strip()
            if re.fullmatch(r'\d+\.\d+', u):
                secs[u] = secs.get(u, 0) + 1
    data = set()
    p = os.path.join(ROOT, 'data', 'plans', fid(c), 'items.csv')
    if os.path.exists(p):
        for r in csv.DictReader(io.open(p, encoding='utf-8')):
            data.add((r.get('unit') or '').strip())
    keys = {int(m.group(1)) for f in glob.glob(os.path.join(ROOT, 'docs', 'reviews', 'answer-key-%s-u*.md' % fid(c)))
            for m in [re.search(r'-u(\d+)-', os.path.basename(f))] if m}
    cells = ''
    for u, n_d in secs.items():
        a, b = u.split('.')
        if b == '1' and n_d > 6 and not any(x.startswith(a + '.') and x != u for x in secs):
            cells += '.' * max(1, round(n_d / 5)); est = True
            continue
        f = os.path.join(ROOT, 'docs', 'courses', fid(c), 'u%02d-%s.md' % (int(a), b))
        s = ('d' if (u in data and int(a) in keys) else 'a') if os.path.exists(f) else '.'
        cells += led.get(f'section:{k}:{u}', s)
    if not secs:
        cells, est = '.' * round(days_of(c)[0] / 5), True
    return cells, est
srows = []
for n in SUBJ_ORDER:
    for c in core(n):
        cells, est = section_cells(c)
        srows.append(dict(title=c['title'], group=sname(n), est=est, cells=cells))
for i, t, cs, pre in AFTER:
    for c in cs:
        srows.append(dict(title=c['title'], group=t, est=True, faint=True, cells='.' * round(days_of(c)[0] / 5)))
bands.append(dict(type='rows', id='sections', title='5. Section plans, plan data and keys', noun='sections', tip='row:sections',
                  sub='Per grade, units in order: section plans, then plan data (items, wrong answers, sources, pieces), then a fresh key read per unit. In a subject\'s first grade, unit 1 goes all the way through days first (the probe). Then the kit is frozen for the grade.',
                  lanes=[dict(title='Unit 1 probes', nodes=[N(f'probe:{slug(n)}', sname(n)) for n in SUBJ_ORDER])], rows=srows))

# 6. Days: one cell a day. A written day (courses/<course>/u*/dNNN.md) is under way until its grade closes with a
# sample read, then done. Days on file from before the 2026-11-13 plan (grade 4 math) stay "on file".
rows = []
close_lanes = []
for n in SUBJ_ORDER:
    cl = []
    for c in core(n):
        n_days, est = days_of(c)
        have, closed = day_files(c), grade_closed(c)
        strip = strips.get(c['title'])
        old = [x in ('written', 'cheap', 'read', 'taught') for x in strip['days']] if strip else []
        cells = ''
        for d_ in range(1, n_days + 1):
            if d_ in have: ch = 'd' if closed else 'a'
            elif d_ <= len(old) and old[d_ - 1]: ch = 'e'
            else: ch = '.'
            cells += led.get(f'day:{fid(c)}:{d_}', ch)
        rows.append(dict(title=c['title'], group=sname(n), est=est, cells=cells))
        cl.append(N(f'close:{fid(c)}', c['title'], 'd' if closed else ('a' if have else '.')))
    close_lanes.append(dict(title=sname(n) + ': grade close', nodes=cl))
for i, t, cs, pre in AFTER:
    for c in cs:
        n_days, est = days_of(c)
        rows.append(dict(title=c['title'], group=t, est=est, faint=True, cells=''.join(st(f'day:{fid(c)}:{j + 1}') for j in range(n_days))))
bands.append(dict(type='rows', id='days', title='6. Days',
                  sub='Per grade, in order, 4 to 6 days a job, each job waiting until its ledger rows are written. A written day is under way until its grade closes: a cleanup job, then a sample read of 10 days by two fresh readers. Faint rows are the other subjects, at about %d days a course until each frame sets its count.' % EST_DAYS,
                  lanes=close_lanes, rows=rows))

# 7. Course finish: per course, the checks read as one assessment plan, a coherence pass, English learner supports,
# art and voice and the tools the sections name; then the cross-grade continuity pass, a whole-course cold read and
# owner sign-off. Tools are drawn here as dots, one a tool, lit when live.
lanes7 = [dict(title=sname(n), nodes=[N(f'finish:{fid(c)}', c['title']) for c in core(n)] + [N(f'continuity:{slug(n)}', 'Continuity pass')])
          for n in SUBJ_ORDER]
lanes7 += [dict(title=t, faint=True, nodes=[N(f'finish:{fid(c)}', c['title']) for c in cs]) for i, t, cs, pre in AFTER]
tool_rows = []
for n in SUBJ_ORDER:
    r = summ[n]
    total, live = (r.get('spec') or 0) + (r.get('built') or 0) + (r.get('live') or 0), r.get('live') or 0
    tool_rows.append(dict(title=sname(n) + ' tools', group='Tools', cells='e' * live + '.' * (total - live)))
bands.append(dict(type='rows', id='finish', title='7. Course finish', dots=True,
                  sub='Per course: the checks read as one assessment plan, a coherence pass over units and seams, English learner supports, art and voice, and the tools the sections name. Then the cross-grade continuity pass, a whole-course cold read and owner sign-off. Dots are tools, lit when live.',
                  lanes=lanes7, rows=tool_rows))

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
    'probe': "Unit 1 of the subject's first grade goes all the way through section plans, plan data, keys and days first, and is read, before the rest of the grade. The kit is retooled once after it.",
    'gate3': "Stage 3 gate: Cory approves this subject's baseline (frames and scopes and sequences), scope changes only.",
    'gate4': "Stage 4 gate: one cold read from the progression down across every course of the subject, then Cory approves the unit plans.",
    'close': "This grade's days close: one cleanup job for faults across days, then a sample read of 10 days by two fresh readers, then a retool before the next grade.",
    'finish': "Course finish: the checks read as one assessment plan, a coherence pass, English learner supports, art and voice, the tools the sections name; then a whole-course cold read, final sensitivity and safety reads, and Cory's sign-off.",
    'continuity': "The cross-grade continuity pass: the ledger check re-run across all grades and every review claim confirmed against the written day, one fix job per grade.",
    'pre': "This subject's pre-work: the standard in our own words, the approach, a base text, the expert's lens and bar, the course list and shape, the dose, cross-subject leans and sensitive ground.",
    'baseline1': "A checkpoint: every progression and course frame reviewed, and the website matches the plan.",
    'row:units': "The unit plans for this course, one cell a unit. A plan is done once it meets the stage 4 bar, Goal map included; one written before that bar shows as on file. Dashed cells are an estimate until the course frame sets the count.",
    'row:days': "Every teaching day of this course, one cell a day. Amber: written, its grade not yet closed. Green: the grade closed with a cleanup and a sample read.",
    'row:sections': "The sections of this course, one cell a section (1 to 6 days). Amber: the section plan is written. Green: its plan data and its unit's answer-key read are in too. Dashed cells are an estimate until the unit is split.",
    'row:tools': "The interactive tools in this subject, one dot a tool. Lit dots are live; a tool is rebuilt or checked when a section names it.",
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
           note='From docs/COURSE-RUN.md (draft 3): seven stages, the same for every subject. Day and unit counts marked "about" are estimates until each course frame sets them.')
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

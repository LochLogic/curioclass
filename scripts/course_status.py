"""Writes docs/COURSES-STATUS.md: one row per course, showing which layers exist.

A course is counted the way a school would schedule it (Cory, 2026-11-11):
- math, English language arts, science, social studies: one per grade through grade 8
  (ELA through 12), then one per named high school course;
- every other subject: one per discipline per grade band; world languages one per language.
The 93 catalog pages (subject by grade or band) are a different count and are not courses.

Run: python -X utf8 scripts/course_status.py [out.json]
With a path, also writes the Review Desk document (then ArtifactData set stats/courses).
"""
import csv, glob, io, json, os, sys, collections, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def rows(p): return list(csv.DictReader(io.open(os.path.join(ROOT, p), encoding='utf-8')))
def has(p): return os.path.exists(os.path.join(ROOT, p))

CORE4 = ['math', 'ela', 'science', 'social-studies']
BY_GRADE = {'math-k8', 'ela-k12', 'science-k5', 'science-ms', 'ss-k5'}
GRADES = ['k'] + [str(i) for i in range(1, 13)]
BAND_OF = {'k': 'k-2', '1': 'k-2', '2': 'k-2', '3': '3-5', '4': '3-5', '5': '3-5'}
BANDS = ['k-2', '3-5', '6-8', '9-12']
ONE_ROW = {'world-languages'}          # keyed by level, not grade: one course per language
SHORT = {'math': 'Math', 'ela': 'English language arts', 'science': 'Science', 'social-studies': 'Social studies'}

courses = {r['course_id']: r for r in rows('data/courses.csv')}
subjects = {r['subject_id']: r['label'] for r in rows('data/subjects.csv')}
modules = rows('data/modules.csv')
modmap = {m['module_id']: m for m in modules}
tools = rows('docs/agents/catalog/shape/shape.csv')

def gname(g): return 'Kindergarten' if g == 'k' else 'Grade ' + g
def bname(b): return b.replace('k', 'K').replace('-', ' to ')

def place(m):
    """Returns (kind, key, title, sortkey). kind is 'course' or 'shared'."""
    s, c, g = m['subject'], m['course_id'], m['grade']
    if s in CORE4:
        if c in BY_GRADE:
            if g in GRADES:
                return 'course', f'{s}-{g}', f'{SHORT[s]}, {gname(g)}', (GRADES.index(g), '')
            return 'shared', f'{s}-{g}', f'{SHORT[s]}, topics shared across grades {bname(g)}', (0, g)
        return 'course', c, courses[c]['title'], (20 + int(courses[c]['typical_grade'] or 9), c)
    title = courses[c]['title']
    if s in ONE_ROW:
        return 'course', c, title.split(' (')[0] + ', all levels', (0, c)
    b = BAND_OF.get(g, g)
    if b in BANDS:
        return 'course', f'{c}-{b}', f'{title}, grades {bname(b)}', (BANDS.index(b), c)
    return 'shared', f'{c}-{b}', f'{title}, topics shared across grades {bname(b)}', (9, c)

info = {}
for m in modules:
    kind, key, title, sk = place(m)
    d = info.setdefault(key, dict(kind=kind, title=title, sort=sk, subject=m['subject'], mods=0,
                                  tools=collections.Counter(), core=courses[m['course_id']]['core'] == 'y'))
    d['mods'] += 1
    m['_key'] = key
for t in tools:
    info[modmap[t['module']]['_key']]['tools'][t['stage']] += 1

import re
# the canonical course id is the frame slug (data/plans/frames.csv, written by scripts/frame.py sync); a course
# title slugs to it ("Science, Grade 4" -> science-grade-4), and a course with no frame gets ''
FRAMES = {r['course']: r for r in rows('data/plans/frames.csv')} if has('data/plans/frames.csv') else {}
FRAME_IDS = set(FRAMES)
def frame_id(title):
    k = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
    return k if k in FRAME_IDS else ''

# progression rows by subject and grade (data/progressions/<subject>.csv)
PROG = {}
for s_ in CORE4:
    if has(f'data/progressions/{s_}.csv'):
        PROG[s_] = {r['grade'].strip().upper() for r in rows(f'data/progressions/{s_}.csv')}

def plan_count(fid, key):
    """Unit and section plans on file: docs/courses/<frame slug>/ and the older docs/courses/<key>/."""
    return sum(len(glob.glob(os.path.join(ROOT, 'docs', 'courses', k, '[us][0-9]*.md'))) for k in {fid, key} - {''})

def layer_cells(key, d):
    s = d['subject']
    fid = frame_id(d['title'])
    grade = FRAMES[fid]['grade'].strip().upper() if fid else None
    num = 0 if grade == 'K' else int(grade) if grade and grade.isdigit() else None
    if s == 'math': rubric = 'yes' if num is not None else 'no'                    # docs/RUBRIC-MATH-K8.md, RUBRIC-MATH-HS.md
    elif s == 'ela': rubric = 'yes' if (num is not None and num >= 3) else 'no'     # docs/RUBRIC-ELA.md, grades 3 to 12
    elif s == 'science': rubric = 'yes' if fid else 'no'                            # docs/RUBRIC-SCIENCE.md, K to 12
    else: rubric = 'no'
    if s == 'math' and has('docs/APPROACH-MATH.md'): approach = 'draft'
    elif s == 'ela' and has('docs/APPROACH-ELA.md'): approach = 'draft'
    elif s in ('science', 'social-studies') and fid: approach = 'lens and rubric'   # stand-in until days (Cory, 2026-11-14)
    else: approach = 'shared page only'
    prog = 'yes' if (fid and grade in PROG.get(s, set())) else 'no'
    if fid and has(f'docs/courses/{fid}/scope-and-sequence.md'): spine = 'yes'
    elif has(f'docs/courses/{key}-spine.md'): spine = 'draft'
    else: spine = 'no'
    plans = plan_count(fid, key)
    return rubric, approach, prog, spine, (str(plans) if plans else 'no')

SPINE_ROW = re.compile(r'^\|\s*(\d*)\s*\|\s*(.+?)\s*\|\s*(\d+)\s*\|\s*(\d+)(?:\s*to\s*(\d+))?\s*\|')

def days_units(fid):
    """Units from data/plans/<frame slug>/days.csv: [(unit number or None for a course-level check, label, first, last)]."""
    p = os.path.join(ROOT, 'data', 'plans', fid, 'days.csv') if fid else ''
    if not p or not os.path.exists(p): return []
    out = []
    for r in csv.DictReader(io.open(p, encoding='utf-8')):
        st, day = (r.get('stretch') or '').strip(), (r.get('day') or '').strip()
        if not day.isdigit(): continue
        n = int(st) if st.isdigit() else None
        if out and out[-1][0] == n and out[-1][3] == int(day) - 1:
            out[-1] = (n, out[-1][1], out[-1][2], int(day))
        else:
            out.append((n, f'Unit {n}' if n is not None else 'Course-level check', int(day), int(day)))
    return out

def spine_units(key, fid=''):
    """The scope and sequence table: [(unit number or None for a check, label, first day, last day)]."""
    got = days_units(fid)
    if got: return got
    p = os.path.join(ROOT, 'docs', 'courses', f'{key}-spine.md')
    if not os.path.exists(p): return []
    out, inside = [], False
    for line in io.open(p, encoding='utf-8'):
        if line.startswith('|') and 'On days' in line: inside = True; continue   # the year's table only
        if inside and not line.startswith('|'):
            if out: break
            continue
        m = SPINE_ROW.match(line) if inside else None
        if m:
            a = int(m.group(4)); b = int(m.group(5) or a)
            out.append((int(m.group(1)) if m.group(1) else None, re.sub(r'\*|\s*\(.*', '', m.group(2)).strip(), a, b))
    return out

# reviews are filed by day number only; they belong to the one course that has written days (grade 4 math today)
REVIEWED = {'cheap': set(), 'expert': set()}
for f in glob.glob(os.path.join(ROOT, 'docs', 'reviews', 'cheap-d[0-9][0-9][0-9]-*.md')):
    REVIEWED['cheap'].add(int(os.path.basename(f)[7:10]))
for f in glob.glob(os.path.join(ROOT, 'docs', 'reviews', 'day-[0-9][0-9][0-9]-*.md')):
    REVIEWED['expert'].add(int(os.path.basename(f)[4:7]))
WRITTEN = {}
for f in glob.glob(os.path.join(ROOT, 'courses', '*', 'u*', 'd[0-9][0-9][0-9].md')):
    WRITTEN.setdefault(os.path.basename(os.path.dirname(os.path.dirname(f))), set()).add(int(os.path.basename(f)[1:4]))
TAUGHT = {}   # no course day has been taught yet; filled from taught-run records when they exist

def ladder(key, fid=''):
    """Counts down the build order: scope and sequence, unit plans, section plans, days written, read, taught."""
    units = spine_units(key, fid)
    dirs = [os.path.join(ROOT, 'docs', 'courses', k) for k in {fid, key} - {''}]
    uplans = {int(re.match(r's(\d+)', os.path.basename(f)).group(1)) for d in dirs for f in glob.glob(os.path.join(d, 's[0-9]*.md'))}
    splans = sum(len(glob.glob(os.path.join(d, 'u[0-9]*-[0-9]*.md'))) for d in dirs)
    written = WRITTEN.get(key, set())
    only = len(WRITTEN) == 1 and key in WRITTEN
    cheap = (REVIEWED['cheap'] & written) if only else set()
    expert = (REVIEWED['expert'] & written) if only else set()
    taught = TAUGHT.get(key, set())
    total = max((u[3] for u in units), default=0)
    r = dict(units_total=sum(1 for u in units if u[0] is not None), units=len(uplans), sections=splans,
             days_total=total, written=len(written), cheap=len(cheap), read=len(expert), taught=len(taught))
    strip = None
    if written or uplans:
        planned = {n for u in units if u[0] in uplans for n in range(u[2], u[3] + 1)}
        def state(n):
            if n in taught: return 'taught'
            if n in expert: return 'read'
            if n in cheap: return 'cheap'
            if n in written: return 'written'
            if n in planned: return 'planned'
            return 'sequence'
        strip = dict(days=[state(n) for n in range(1, total + 1)],
                     segments=[dict(n=u[0], label=u[1], a=u[2], b=u[3]) for u in units])
    return r, strip

out = []
A = out.append
today = datetime.date.today().isoformat()
A('# Course status: which layers exist for every course\n')
A(f'Generated by scripts/course_status.py on {today}. Do not edit by hand; run the script again.\n')
A('**What this is.** A status table, not a plan. It shows the gap between what exists and a finished course. '
  'Every course on it is to be finished to the bar (Cory, 2026-11-11). The build order is docs/PRODUCTION-PATH.md; '
  'the current state is docs/HANDOFF.md.\n')
A('**How courses are counted.** As a school would schedule them: math, English language arts, science and '
  'social studies by grade and then by named high school course; every other subject by discipline and grade '
  'band; world languages by language. The catalog has 93 pages (a subject at a grade or band), which is a '
  'different count: some pages hold several courses and some hold none.\n')
A('**The layers** (docs/ROADMAP.md, "The layers"). Standards are loaded for every subject, the shared approach '
  '(docs/APPROACH.md) is a draft that serves every course, and every catalog page is shaped, so those have no '
  'column. The columns are the layers that differ by course:\n')
A('- **Rubric file**: our own-words file of what a published review rubric asks. Where none is written, the bar '
  'for that course is only the general one in docs/ADOPTION-BAR.md, and for subjects with no published rubric '
  'the bar still has to be stated.')
A('- **Approach**: the subject page that says how the shared approach is carried out. For science and social '
  'studies, the subject lens (docs/agents/lenses/) and the rubric stand in until days are written (Cory, 2026-11-14).')
A('- **Progression**: what the grade inherits and hands on (rows for the grade in data/progressions/<subject>.csv).')
A('- **Scope and sequence**: every day of the year in order (docs/courses/<course>/scope-and-sequence.md). "yes" '
  'means the file is on file; docs/HANDOFF.md says which have been read and fixed. "draft" is an older -spine.md '
  'file only.')
A('- **Plans**: unit plans and section plans on file, as a count.')
A('- **Topics** and **Tools**: what the catalog holds. Tools are counted as spec / built / live. A spec or a '
  'built tool is not yet tied to a section plan anywhere except the trial sections.')
A('\nNo course has lessons, print, checks with keys or teacher pages yet. That is layer 7; it starts after the '
  'unit plans, with the probe and guard (docs/PRODUCTION-PATH.md).\n')

courselist = {k: d for k, d in info.items() if d['kind'] == 'course'}
groups = [(s, subjects[s]) for s in CORE4] + [(s, subjects[s]) for s in subjects if s not in CORE4]

A('## Summary\n')
A('| Subject | Courses | Flagged core | With a scope and sequence | With any plan | Topics | Tools: spec / built / live |')
A('|---|---|---|---|---|---|---|')
tot = collections.Counter()
J = dict(at=datetime.datetime.now(datetime.timezone.utc).isoformat(), summary=[], subjects=[], shared=[], strips=[], core_subjects=[SHORT[c] for c in CORE4])
for s, label in groups:
    ds = [(k, d) for k, d in courselist.items() if d['subject'] == s]
    cells = [layer_cells(k, d) for k, d in ds]
    tc = collections.Counter()
    for _, d in ds: tc.update(d['tools'])
    lad = collections.Counter()
    for k, d_ in ds: lad.update(ladder(k, frame_id(d_['title']))[0])
    r = dict(n=len(ds), core=sum(d['core'] for _, d in ds), spine=sum(c[3] != 'no' for c in cells),
             plans=sum(c[4] != 'no' for c in cells), mods=sum(d['mods'] for _, d in ds),
             spec=tc['spec'] + tc['idea'], built=tc['built'], live=tc['live'],
             units=lad['units'], sections=lad['sections'], written=lad['written'], cheap=lad['cheap'],
             read=lad['read'], taught=lad['taught'])
    tot.update(r)
    J['summary'].append(dict(name=label, **r))
    A(f"| {label} | {r['n']} | {r['core']} | {r['spine']} | {r['plans']} | {r['mods']} | {r['spec']} / {r['built']} / {r['live']} |")
    if s == CORE4[-1]:
        J['core4'] = dict(tot)
        A(f"| **The four core subjects** | **{tot['n']}** | **{tot['core']}** | **{tot['spine']}** | **{tot['plans']}** | "
          f"**{tot['mods']}** | **{tot['spec']} / {tot['built']} / {tot['live']}** |")
A(f"| **All courses** | **{tot['n']}** | **{tot['core']}** | **{tot['spine']}** | **{tot['plans']}** | **{tot['mods']}** | "
  f"**{tot['spec']} / {tot['built']} / {tot['live']}** |")
A('\nTool counts here leave out tools that sit on shared topics (last table). "Spec" includes a few that are '
  'still ideas.\n')


for s, label in groups:
    ds = sorted([(k, d) for k, d in courselist.items() if d['subject'] == s], key=lambda kd: kd[1]['sort'])
    A(f'## {label} ({len(ds)} courses)\n')
    js = dict(name=label, courses=[]); J['subjects'].append(js)
    A('| Course | Core | Rubric file | Approach | Progression | Scope and sequence | Plans | Topics | Tools: spec / built / live |')
    A('|---|---|---|---|---|---|---|---|---|')
    for k, d in ds:
        ru, ap, pr, sp, pl = layer_cells(k, d)
        t = d['tools']
        lad, strip = ladder(k, frame_id(d['title']))
        js['courses'].append(dict(title=d['title'], course=frame_id(d['title']), core=d['core'], rubric=ru, approach=ap, prog=pr, spine=sp, plans=pl,
                                  mods=d['mods'], spec=t['spec'] + t['idea'], built=t['built'], live=t['live'], **lad))
        if strip: J['strips'].append(dict(title=d['title'], **lad, **strip))
        A(f"| {d['title']} | {'yes' if d['core'] else ''} | {ru} | {ap} | {pr} | {sp} | {pl} | {d['mods']} | "
          f"{t['spec'] + t['idea']} / {t['built']} / {t['live']} |")
    A('')

sh = sorted([(k, d) for k, d in info.items() if d['kind'] == 'shared'], key=lambda kd: (kd[1]['subject'], kd[1]['sort']))
A('## Topics that belong to no single course\n')
A('These sit on a band page and are shared by the grades in it. Decided (Cory, 2026-11-11): the topic and its '
  'tools stay shared, and each grade\'s scope and sequence claims the skill on its own days, with that grade\'s standard and '
  'texts, so every standard has an owner in a course. The single topics fold into their nearest course. They '
  'are not counted as courses above.\n')
A('| Shared set | Topics | Tools: spec / built / live |')
A('|---|---|---|')
for k, d in sh:
    t = d['tools']
    J['shared'].append(dict(title=d['title'], mods=d['mods'], spec=t['spec'] + t['idea'], built=t['built'], live=t['live']))
    A(f"| {d['title']} | {d['mods']} | {t['spec'] + t['idea']} / {t['built']} / {t['live']} |")
A('\nAlso not counted: French, which is on the course list with no topics yet (other languages come later, '
  'decided 2026-10-22).\n')

text = '\n'.join(out)
assert '—' not in text
io.open(os.path.join(ROOT, 'docs', 'COURSES-STATUS.md'), 'w', encoding='utf-8', newline='\n').write(text)
J['total'] = dict(tot)
if len(sys.argv) > 1:
    io.open(sys.argv[1], 'w', encoding='utf-8').write(json.dumps(J))
print('courses', tot['n'], 'core4', sum(1 for d in courselist.values() if d['subject'] in CORE4), 'shared sets', len(sh))

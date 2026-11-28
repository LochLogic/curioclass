"""Gate for course frames, docs/courses/<slug>/frame.md (PRODUCTION-PATH step 2, added 2026-11-13).

    python -X utf8 scripts/frame.py check [slug ...]   check the frames (all found, or the ones named)
    python -X utf8 scripts/frame.py sync               rewrite data/plans/frames.csv and the school calendar
                                                       (data/plans/calendar.csv, the table in docs/courses/CALENDAR.md)
    python -X utf8 scripts/frame.py calendar           print each K to 8 grade's course-level check weeks

The frame's format is set by docs/pipeline/briefs/frame-write.md. Which progression rows a course owns, its catalogue id
(data/courses.csv course_id), grade, term, weeks and pins are columns of data/plans/course-list.csv; fill its `rows`
cell when its frame is written. The school calendar (school day, week) is
docs/courses/CALENDAR.md.

FAIL (exit 1):
- a missing section (The course in brief, Seams, Models carried, Units, Course-level checks, Cross-subject), or one
  of Seams, Models carried, Course-level checks or Cross-subject with nothing under its heading;
- the **Units.** or **Days.** bullet with no number first; a Units table whose row count differs from **Units.**;
- unit days that add to more than the course's days;
- a Skills id that is not one of the course's rows, or sits in two units; a course row placed in no unit;
- an Owned standards code that the unit's rows do not own, or a code a unit's rows own (not ~) missing from its
  Owned standards;
- data/plans/frames.csv disagreeing with the frame on units or days (run sync), a frames.csv row with no frame, a
  course-list.csv course with rows and no frame, or a catalogue id not in data/courses.csv;
- a stale note (scripts/stale.py) in the frame.
note (exit 0): the days left for course-level checks and respond days, per course; and the frame-write lessons
that are not failures yet (added 2026-11-14, baseline 1 structure findings 3, 6 and 8, Codex finding 3):
- the time a day: no minutes, or no lessons a week, in the **Days.** bullet (or a bullet labelled Time);
- a Check set adds cell that does not start "Candidate" (or "None");
- a course-level check with no respond day; checks the calendar cannot place (After unit not read); a Course-level
  checks section not in the one table shape (| Check | After unit | Check days | Respond days | What it checks |);
- no **Sensitivity reads.** bullet, or no "paper path", in The course in brief;
- a lettered part of an owned standard (W.7.1c) not named by its code in the row of the unit that owns its parent;
- a unit's rows' ~contribution code named nowhere in the unit row (no tilde codes in frames: the begun part is
  described in the unit's prose, What students learn, with its later owner; lead calls 2026-11-15, math 1);
- an assumes or hands_on id missing from Seams; a model missing from Models carried; a cross_subject lean (code or
  id) missing from Cross-subject;
- a cross-frame citation ("math grade 4 unit 8 (about school days 113 to 127)") more than 3 days outside the cited
  unit's place on the calendar;
- outside-reader wording that FOUNDATION 7.3 (revised 2026-11-14) replaced with agent reads.
A note becomes a FAIL once every frame passes it (the brief's rule: warnings first).
"""
import csv
import glob
import io
import math
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
FRAMES_CSV = os.path.join(ROOT, 'data', 'plans', 'frames.csv')
CAL_CSV = os.path.join(ROOT, 'data', 'plans', 'calendar.csv')
CAL_MD = os.path.join(ROOT, 'docs', 'courses', 'CALENDAR.md')
COLS = ['course', 'catalog_id', 'subject', 'grade', 'title', 'units', 'days', 'minutes_min', 'minutes_max',
        'per_week', 'weeks', 'term', 'legacy_plan_id']
YEAR_DAYS, YEAR_WEEKS = 160, 32


# The course list is data (consolidation step 4.C): data/plans/course-list.csv owns every course's id (the frame slug),
# subject, grade, catalogue id, the progression rows it owns (`rows`: grade:K or prefix:bio-), term, weeks, pins and
# any legacy plan id. The dicts below are views of it, kept under their old names for the readers.
COURSE_LIST = os.path.join(ROOT, 'data', 'plans', 'course-list.csv')


def _grade(g):
    return lambda r: r['grade'].strip() == g
def _prefix(p):
    return lambda r: r['skill_id'].startswith(p)


def course_list():
    with open(COURSE_LIST, encoding='utf-8', newline='') as fh:
        return list(csv.DictReader(fh))


def selector(sel, subject):
    """(progression file, row test) for a course-list `rows` cell: `grade:K` or `prefix:bio-` (the core courses), or
    parts joined by `&` (the later subjects' band courses, 2026-11-25): `file:<data/progressions name>` when the
    course's subject cell is not the file's name, `grade:K|1|2` (any of these grades), `prefix:da-|va-` (any of these
    skill id prefixes) and `strand:mu` (any of these strands). `|` keeps the cell free of commas."""
    preds = []
    for part in sel.split('&'):
        kind, _, val = part.strip().partition(':')
        vals = tuple(v.strip() for v in re.split(r'[|,]', val) if v.strip())
        if kind == 'file':
            subject = val.strip()
        elif kind == 'grade':
            preds.append(lambda r, vs=vals: r['grade'].strip() in vs)
        elif kind == 'prefix':
            preds.append(lambda r, vs=vals: r['skill_id'].startswith(vs))
        elif kind == 'strand':
            preds.append(lambda r, vs=vals: r['strand'].strip() in vs)
        else:
            raise SystemExit('course-list.csv rows cell %r: unknown part %r' % (sel, kind))
    return subject, (lambda r: all(p(r) for p in preds))


COURSE_ROWS, COURSE_META, LEGACY, TERM, WEEKS, PINS = {}, {}, {}, {}, {}, {}
ROWS_GRADE = {}   # a one-year course over a grade range (career exploration 6-8) sits on its `rows` grade's calendar
for _r in course_list():
    _s, _sel = _r['id'], _r['rows']
    if _sel:
        COURSE_ROWS[_s] = selector(_sel, _r['subject'])
        _g = [p.partition(':')[2] for p in _sel.split('&') if p.strip().startswith('grade:')]
        if len(_g) == 1 and len(re.split(r'[|,]', _g[0])) == 1:
            ROWS_GRADE[_s] = _g[0].strip().upper()
        COURSE_META[_s] = (_r['catalog_id'], _r['grade'])
    if _r['legacy_plan_id']:
        LEGACY[_r['legacy_plan_id']] = _s       # a plan folder kept under its old name (the math-4 pilot)
    if _r['term'] and _r['term'] != 'year':
        TERM[_s] = _r['term']                   # half-year courses: which half
    if _r['weeks']:
        WEEKS[_s] = int(_r['weeks'])            # weeks a fewer-than-five-a-week course spreads over (CALENDAR.md stagger rule)
    if _r['pins']:
        PINS[_s] = {int(x): int(y) for x, y in (p.split(':') for p in _r['pins'].split())}   # course day: school day

SECTIONS = ['The course in brief', 'Seams', 'Models carried', 'Units', 'Course-level checks', 'Cross-subject']
SUBJ_WORDS = {'math': 'math', 'science': 'science', 'ela': 'ela', 'english language arts': 'ela',
              'social studies': 'social-studies'}
OUTSIDE_READER = re.compile(r'qualified [\w ]{0,30}(reviewer|reader)|content reviewer|community (sensitivity )?reader'
                            r"|teacher's safety read|outside (human )?reader|specialist reader", re.I)
_rows = {}
_parsed = {}


def rows(subject):
    if subject not in _rows:
        p = os.path.join(ROOT, 'data', 'progressions', subject + '.csv')
        _rows[subject] = list(csv.DictReader(open(p, encoding='utf-8')))
    return _rows[subject]


def split(cell):
    return [x.strip() for x in re.split(r';|,', cell or '') if x.strip()]


def split_codes(cell):
    # standard codes split at semicolons only: career cluster codes hold commas (career pathways read, 2026-11-25)
    return [x.strip() for x in (cell or '').split(';') if x.strip()]


def path_of(slug):
    return os.path.join(ROOT, 'docs', 'courses', slug, 'frame.md')


def section(t, name):
    m = re.search(r'^## %s\s*$(.*?)(?=^## |\Z)' % re.escape(name), t, re.M | re.S)
    return m.group(1) if m else ''


def bullet(t, label):
    """The text of the brief's bullet that starts with **<label>.** (to the next bullet or heading)."""
    m = re.search(r'^\s*[-*]\s*\*\*%s\.?\*\*(.*?)(?=^\s*[-*]\s*\*\*|^#|\Z)' % label, t, re.M | re.S)
    return m.group(1) if m else ''


def table(sec):
    lines = [l for l in sec.splitlines() if l.strip().startswith('|')]
    out = []
    if lines:
        head = [c.strip() for c in lines[0].strip().strip('|').split('|')]
        for l in lines[2:]:
            cells = [c.strip() for c in l.strip().strip('|').split('|')]
            if len(cells) < len(head):
                cells += [''] * (len(head) - len(cells))
            out.append(dict(zip(head, cells)))
        return head, out
    return [], out


WORDNUM = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10}


def _num(s):
    s = s.lower()
    return int(s) if s.isdigit() else WORDNUM.get(s)


def parse_checks(sec):
    """The course-level checks in order: [{label, after (unit number or None: after the one before), check, respond,
    review}]. Reads the one table shape and the older shapes (tables with Falls after / After unit / After, and
    **After unit N (k days** bullets with a following respond-day bullet)."""
    head, tab = table(sec)
    out = []
    if tab:
        after_col = next((h for h in head if 'after' in h.lower()), None)
        for r in tab:
            label = r.get('Check') or r.get(head[0], '')
            after_cell = r.get(after_col, '') if after_col else ''
            m = re.search(r'(?:unit\s*)?(\d+)', after_cell, re.I) if not re.search(r'review', after_cell, re.I) else None
            after = int(m.group(1)) if m else None
            row = ' '.join(r.values())
            c = dict(label=label.strip('* '), after=after, check=0, respond=0, review=0)
            if 'Check days' in r:
                c['check'] = int((re.findall(r'\d+', r['Check days']) or [0])[0])
                c['respond'] = int((re.findall(r'\d+', r.get('Respond days', '')) or [0])[0])
                if re.search(r'review', label, re.I):
                    c['review'], c['check'] = c['check'], 0
            else:
                days = r.get('Days', '')
                nums = re.findall(r'\d+', days)
                total = int(nums[0]) if nums else 0
                if re.search(r'review', label, re.I) and 'respond' not in days:
                    c['review'] = total
                elif 'respond' in days:
                    c['check'] = total
                    rm = re.search(r'(\d+|\w+) respond', days)
                    c['respond'] = _num(rm.group(1)) or 0 if rm else 0
                else:
                    rm = re.search(r'\b(\d+|one|two|three|four)\s+respond days?', row, re.I) or \
                        re.search(r'\b(a|respond)\s+(?:respond\s+)?day\b', row, re.I)
                    resp = (1 if rm.group(1).lower() in ('a', 'respond') else _num(rm.group(1)) or 0) if rm else 0
                    c['respond'] = resp
                    c['check'] = total - resp if total > resp else total
            out.append(c)
        return out
    for b in re.split(r'\n(?=\s*[-*]\s)', sec):
        m = re.search(r'After unit (\d+)\s*\((\d+|one|two|three) days?', b, re.I)
        if m:
            out.append(dict(label='after unit %s' % m.group(1), after=int(m.group(1)), check=_num(m.group(2)) or 0,
                            respond=0, review=0))
            rm = re.search(r'(\d+|one|two) respond days?', b[m.end():], re.I)
            if rm:
                out[-1]['respond'] = _num(rm.group(1)) or 0
            continue
        m = re.search(r'\*\*\s*(\d+|one|two|three) respond days?', b, re.I)
        if m and out:
            out[-1]['respond'] += _num(m.group(1)) or 0
    return out


def parse(slug):
    if slug in _parsed:
        return _parsed[slug]
    t = open(path_of(slug), encoding='utf-8').read()
    out = {'text': t, 'sections': re.findall(r'^## (.+?)\s*$', t, re.M)}
    for k in ('Units', 'Days'):
        m = re.search(r'^\s*[-*]\s*\*\*%s\.\*\*\s*(\d+)' % k, t, re.M)
        out[k.lower()] = int(m.group(1)) if m else None
    out['head'], out['table'] = table(section(t, 'Units'))
    m = re.search(r'^# Course frame:\s*(.+?)\s*$', t, re.M)
    out['title'] = m.group(1) if m else slug
    brief = section(t, 'The course in brief')
    timing = re.sub(r'\s+', ' ', bullet(brief, 'Days') + ' ' + bullet(brief, r'Time[\w ]*'))
    # the lesson length: the first "N minutes" or "N to M minutes" that is not a weekly or yearly total
    out['minutes'] = (None, None)
    for m in re.finditer(r'(?<![\d,])(\d+)(?:\s+to\s+(\d+))?(?:-|\s)minutes?\b(?!\s+(?:a|per|each)\s+week)', timing):
        lo, hi = int(m.group(1)), int(m.group(2) or m.group(1))
        if 20 <= lo <= 240:
            out['minutes'] = (lo, hi)
            break
    pw = re.search(r'\b(five|four|three|two|one|\d)\s+(?:lessons?|days?|sessions?|meetings?|times|periods?)?\s*(?:a|per|each)\s+week', timing, re.I)
    out['per_week'] = _num(pw.group(1)) if pw else (5 if re.search(r'every school day|each school day|\bdaily\b', timing) else None)
    if out['per_week'] is None and re.search(r'\b(?:one|a)\s+(?:\w+\s+)?every (?:two|other) weeks?|every second week',
                                             timing, re.I):
        out['per_week'] = 0.5                      # library 6 to 8 and 9 to 12: about one session every two weeks
    out['half'] = bool(re.search(r'half[- ]year|a half year', timing, re.I))
    out['checks'] = parse_checks(section(t, 'Course-level checks'))
    # band courses (2026-11-25): a Year column in the Units table names the grade year or level each unit is taught in
    # (K, 1, 2 or Level 1 and so on); the course's days then spread over that many school years, one after another
    ycol = next((h for h in out['head'] if h.lower() in ('year', 'level')), None)
    out['years'] = []
    for u in out['table'] if ycol else []:
        y = u.get(ycol, '').strip()
        if y and y not in out['years']:
            out['years'].append(y)
    _parsed[slug] = out
    return out


# ------------------------------------------------------------------ the school calendar (docs/courses/CALENDAR.md)
def meeting(slug, f):
    """(weeks the course meets, the school day its year starts after, lessons a week)."""
    days = f['days'] or YEAR_DAYS
    if slug in TERM:
        return YEAR_WEEKS // 2, (0 if TERM[slug] == 'fall' else YEAR_DAYS // 2), 5
    years = max(1, len(f.get('years') or []))                   # a band course runs its years one after another
    days = math.ceil(days / years)
    weeks = YEAR_WEEKS
    if f['per_week'] and f['per_week'] < 5 and days > f['per_week'] * (YEAR_WEEKS - 4):
        weeks = min(YEAR_WEEKS, math.ceil(days / f['per_week']))   # science 3 to 5: four a week for 30 weeks
    return WEEKS.get(slug, weeks) * years, 0, f['per_week'] or round(days / YEAR_WEEKS)


def school_day(slug, f, n):
    """The school day (1 to 160) on which course day n falls: the course's days spread evenly over its weeks."""
    weeks, start, _ = meeting(slug, f)
    days = f['days'] or YEAR_DAYS
    pts = [(0, start)] + sorted((k, start + v) for k, v in PINS.get(slug, {}).items() if 0 < k < days) +         [(days, start + weeks * 5)]
    for (n0, s0), (n1, s1) in zip(pts, pts[1:]):
        if n <= n1:
            return s0 + max(1, math.ceil((n - n0) * (s1 - s0) / (n1 - n0)))
    return start + max(1, math.ceil(n * weeks * 5 / days))


def week(sd):
    return (sd - 1) // 5 + 1


def calendar(slug):
    """[(kind, n, label, first course day, last course day)] in teaching order: units, checks, respond and review
    days. kind is unit, check, respond or review. None when the checks cannot all be placed."""
    f = parse(slug)
    units = []
    for u in f['table']:
        d = re.match(r'\s*(\d+)', u.get('Days', ''))
        n = re.match(r'\s*(\d+)', u.get('#', ''))
        q = re.sub(r'\*', '', u.get('Unit and compelling question', '')).strip()
        units.append((int(n.group(1)) if n else len(units) + 1, q, int(d.group(1)) if d else 0))
    after = {}
    last = None
    for c in f['checks']:
        key = c['after'] if c['after'] is not None else last
        if key is None:
            return None
        after.setdefault(key, []).append(c)
        last = key
    out, day = [], 0
    def add(kind, n, label, k):
        nonlocal day
        if k:
            out.append((kind, n, label, day + 1, day + k))
            day += k
    placed = 0
    for n, q, k in units:
        add('unit', n, q, k)
        for i, c in enumerate(after.get(n, [])):
            placed += 1
            add('review', n, c['label'], c['review'])
            add('check', n, c['label'], c['check'])
            add('respond', n, c['label'], c['respond'])
    if placed != len(f['checks']):
        return None
    return out


def days_calendar(slug, f):
    """The calendar read from a written scope and sequence (added 2026-11-14): [(kind, n, label, first course day,
    last course day, first school day, last school day)] from data/plans/<slug>/days.csv, each day on its school_day
    where filled (CALENDAR.md: that column wins) and on the even spread otherwise. Days run in school-day order, and a
    unit or check run is cut wherever another day falls between, so a held day (a look-back taught weeks later, an
    on-the-day lesson) shows on its own week. None when the course has no usable days.csv or its check runs do not
    match the frame's Course-level checks table; the caller then falls back to the frame."""
    p = os.path.join(ROOT, 'data', 'plans', slug, 'days.csv')
    base = calendar(slug)
    if not base or not os.path.exists(p):
        return None
    with open(p, encoding='utf-8') as fh:
        rs = list(csv.DictReader(fh))
    if not rs or not {'day', 'stretch', 'kind'} <= set(rs[0]):
        return None
    labels = {n: q for kind, n, q, _, _ in base if kind == 'unit'}
    days = []
    for r in rs:
        d, st = (r.get('day') or '').strip(), (r.get('stretch') or '').strip().upper()
        if not d.isdigit() or not (st.isdigit() or st == 'C'):
            return None
        sd = (r.get('school_day') or '').strip()
        sd = int(sd) if sd.isdigit() else school_day(slug, f, int(d))
        k = (r.get('kind') or '').strip().lower()
        kind = 'unit' if st != 'C' else ('check' if k == 'check' else 'respond' if k == 'respond' else 'review')
        days.append((sd, int(d), kind, st))
    days.sort()
    segs = []
    for sd, d, kind, st in days:
        if segs and segs[-1][0] == kind and segs[-1][1] == st:
            segs[-1][2].append(d)
            segs[-1][3].append(sd)
        else:
            segs.append((kind, st, [d], [sd]))
    out, group, unit, prev = [], -1, None, 'unit'
    for kind, st, ds, sds in segs:
        if kind == 'unit':
            unit = int(st)
            out.append(('unit', unit, labels.get(unit, ''), min(ds), max(ds), min(sds), max(sds)))
        else:
            if prev == 'unit' or (prev == 'respond' and kind != 'respond'):
                group += 1   # a new course-level check: after a unit, or a review or check day after a respond day
            label = f['checks'][group]['label'] if group < len(f['checks']) else ''
            out.append((kind, unit, label, min(ds), max(ds), min(sds), max(sds)))
        prev = kind
    if group + 1 != len(f['checks']):
        return None
    return out


def calendar_rows():
    """Every course's units and checks on the school calendar: from its days.csv once a scope and sequence is written
    (days_calendar), else from its frame's unit days and Course-level checks table, spread evenly."""
    out = []
    for s in found():
        f = parse(s)
        cal = days_calendar(s, f)
        if cal is None:
            cal = [(kind, n, label, a, b, school_day(s, f, a), school_day(s, f, b))
                   for kind, n, label, a, b in (calendar(s) or [])]
        g = COURSE_META.get(s, ('', ''))[1]
        ys = f.get('years') or []
        for kind, n, label, a, b, sa, sb in cal:
            gr = ROWS_GRADE.get(s, g) if '-' in g else g
            if ys:
                # a band course: each year's rows go on that year's own calendar, under its grade (K, 1 to 12) where
                # the Year cell names one, so the stagger rule and CALENDAR.md read them beside the core grades
                span = meeting(s, f)[0] // len(ys) * 5          # school days one year of the band spans
                i = min(len(ys) - 1, (sa - 1) // span)
                y = re.sub(r'(?i)^(grade|year)\s+', '', ys[i]).strip()
                gr = y.upper() if re.fullmatch(r'(?i)k|\d{1,2}', y) else '%s %s' % (g, ys[i])
                sa, sb = sa - i * span, min(sb - i * span, span)
            out.append(dict(course=s, grade=gr, subject=COURSE_ROWS[s][0], kind=kind,
                            unit=n, label=label[:80], first_day=a, last_day=b, first_school_day=sa,
                            last_school_day=sb, first_week=week(sa), last_week=week(sb)))
    return out


def check_weeks(cal_rows):
    """{grade: {subject: [(week, course, label)]}} for course-level check days, K to 8."""
    out = {}
    for r in cal_rows:
        if r['kind'] != 'check' or r['grade'] not in ('K',) + tuple(str(i) for i in range(1, 9)):
            continue
        for w in range(r['first_week'], r['last_week'] + 1):
            out.setdefault(r['grade'], {}).setdefault(r['subject'], []).append((w, r['course'], r['label']))
    return out


SUBJECT_CORE = ('math', 'science', 'ela', 'social-studies')


def classroom_course(r):
    """K to 5: the courses the classroom teacher teaches (the four core subjects, health and SEL). Specials (arts,
    physical education, computer science, library, English language development) have their own teacher and check
    in their own slot, so they do not count toward the classroom week (lead 2026-11-26)."""
    return r['subject'] in SUBJECT_CORE or r['subject'] == 'sel' or r['course'].startswith('health-')


def stagger_key(r):
    """The core subjects count by subject; an after-core course counts on its own, named by its course slug (lead
    2026-11-25), except that in 6 to 8 the arts electives count as one (a student takes one arts elective at a time;
    lead 2026-11-26)."""
    if r['subject'] in SUBJECT_CORE:
        return r['subject']
    if r['subject'] == 'arts' and r['grade'] in ('6', '7', '8'):
        return 'arts elective'
    return r['course']


def clashes(cal_rows):
    """The stagger rule (docs/courses/CALENDAR.md): K to 5 have one classroom teacher, so no school week holds
    course-level check days of two of that teacher's courses (classroom_course); 6 to 8 have a teacher per subject, so no school day does, and week 32 is a finals week.
    Returns (grade, 'week N' or 'day N', [subjects])."""
    out = []
    by = {}
    for r in cal_rows:
        g = r['grade']
        if r['kind'] != 'check' or g not in ('K',) + tuple(str(i) for i in range(1, 9)):
            continue
        if g in ('6', '7', '8'):
            for d in range(r['first_school_day'], r['last_school_day'] + 1):
                if week(d) < YEAR_WEEKS:
                    by.setdefault(g, {}).setdefault('day %d' % d, set()).add(stagger_key(r))
        elif classroom_course(r):
            for w in range(r['first_week'], r['last_week'] + 1):
                by.setdefault(g, {}).setdefault('week %d' % w, set()).add(stagger_key(r))
    for g in sorted(by, key=lambda k: -1 if k == 'K' else int(k)):
        for when, ss in sorted(by[g].items(), key=lambda kv: int(kv[0].split()[1])):
            if len(ss) > 1:
                out.append((g, when, sorted(ss)))
    return out


def cited_unit(cal_rows, subj, grade, unit):
    for r in cal_rows:
        if r['subject'] == subj and r['grade'] == grade and r['kind'] == 'unit' and r['unit'] == unit:
            c = r['course']
            if subj == 'science' and grade in ('9', '10', '11'):
                pass
            return r
    return None


CITE = re.compile(r"\b(math|science|ela|english language arts|social studies)\s+grade\s+(k|\d+)(?:'s)?\s+"
                  r"(?:[a-z ]{0,25}?\b)?unit\s+(\d+)\s*\(([^)]*)\)", re.I)


def citations(slug, cal_rows):
    """Notes for cross-frame citations more than 3 days outside the cited unit's place on the calendar."""
    notes = []
    for m in CITE.finditer(parse(slug)['text']):
        subj = SUBJ_WORDS[m.group(1).lower()]
        g = m.group(2).upper()
        rs = [x for x in cal_rows if x['subject'] == subj and x['grade'] == g and x['kind'] == 'unit'
              and x['unit'] == int(m.group(3)) and COURSE_META.get(x['course'], ('', ''))[1] == g
              and x['course'] != slug and not x['course'] in TERM]
        rs = [x for x in rs if x['course'] == rs[0]['course']]   # one course; a unit may sit in several runs
        rng = re.search(r'(\d+)\s+to\s+(\d+)', m.group(4))
        if not rs or not rng:
            continue
        a, b = int(rng.group(1)), int(rng.group(2))
        school = 'school' in m.group(4)
        lo = min(x['first_school_day'] if school else x['first_day'] for x in rs)
        hi = max(x['last_school_day'] if school else x['last_day'] for x in rs)
        if a < lo - 3 or b > hi + 3:
            notes.append('%s: cites %s grade %s unit %s at %s days %d to %d; the calendar has %d to %d' % (
                slug, m.group(1), g, m.group(3), 'school' if school else 'course', a, b, lo, hi))
    return notes


# ------------------------------------------------------------------ the gate
def lettered(subject):
    """{parent code: [lettered part codes]} from the subject's standards files."""
    import progression
    out = {}
    for fn in progression.STD_FILES.get(subject, []):
        p = os.path.join(ROOT, 'data', 'standards', fn)
        if not os.path.exists(p):
            continue
        for line in open(p, encoding='utf-8'):
            if line.startswith('#') or not line.strip():
                continue
            code = line.split('\t')[0].split()[0].strip()
            m = re.match(r'^(.*\d)([a-z])$', code)
            if m:
                out.setdefault(m.group(1), [])
                if code not in out[m.group(1)]:
                    out[m.group(1)].append(code)
    return out


def named_parts(text, parent):
    """Lettered parts of parent named by code in text: 4.NF.B.3a, 4.NF.B.3a to d, W.8.2a, b and c."""
    got = set()
    for m in re.finditer(re.escape(parent) + r'([a-z](?:\s*(?:,|and|to|-|or)\s*[a-z]\b)*)(?![a-z])', text):
        seq = m.group(1)
        letters = re.findall(r'\b([a-z])\b|^([a-z])', seq)
        ls = [x or y for x, y in letters]
        for r in re.finditer(r'([a-z])\s*(?:to|-)\s*([a-z])\b', seq):
            ls += [chr(c) for c in range(ord(r.group(1)), ord(r.group(2)) + 1)]
        got |= {parent + l for l in ls if l}
    return got


def frames_csv():
    if not os.path.exists(FRAMES_CSV):
        return {}
    return {r['course']: r for r in csv.DictReader(open(FRAMES_CSV, encoding='utf-8'))}


def check(slug, cal_rows=None):
    fails, notes = [], []
    if slug not in COURSE_ROWS:
        return ['%s: no rows cell in data/plans/course-list.csv' % slug], notes
    subject, test = COURSE_ROWS[slug]
    f = parse(slug)
    t = f['text']
    for s in SECTIONS:
        if s not in f['sections']:
            fails.append('%s: no "## %s" section' % (slug, s))
        elif s not in ('The course in brief', 'Units') and not section(t, s).strip():
            fails.append('%s: "## %s" has nothing under it' % (slug, s))
    if f['units'] is None:
        fails.append('%s: the **Units.** bullet has no number first' % slug)
    if f['days'] is None:
        fails.append('%s: the **Days.** bullet has no number first' % slug)
    tab = f['table']
    if f['units'] is not None and len(tab) != f['units']:
        fails.append('%s: **Units.** says %d, the Units table has %d rows' % (slug, f['units'], len(tab)))
    own = {r['skill_id']: r for r in rows(subject) if test(r)}
    parts = lettered(subject)
    seen = {}
    day_sum = 0
    for u in tab:
        n = u.get('#', '?')
        d = re.match(r'\s*(\d+)', u.get('Days', ''))
        if d:
            day_sum += int(d.group(1))
        else:
            fails.append('%s unit %s: Days is not a number' % (slug, n))
        ids = split(u.get('Skills', '').replace('`', ''))
        owned_codes, contrib = set(), set()
        for i in ids:
            if i not in own:
                fails.append('%s unit %s: skill %s is not one of the course rows' % (slug, n, i))
                continue
            if i in seen:
                fails.append('%s: skill %s in units %s and %s' % (slug, i, seen[i], n))
            seen[i] = n
            owned_codes |= {c for c in split_codes(own[i]['standard']) if not c.startswith('~')}
            contrib |= {c[1:] for c in split_codes(own[i]['standard']) if c.startswith('~')}
        cell = u.get('Owned standards', '').replace('`', '')
        listed = {c for c in split_codes(cell) if not c.startswith('~') and c.lower() not in ('none', 'none owned')}
        for c in sorted(listed - owned_codes):
            fails.append('%s unit %s: owned standard %s is not owned by the unit\'s rows' % (slug, n, c))
        for c in sorted(owned_codes - listed):
            fails.append('%s unit %s: its rows own %s, missing from Owned standards' % (slug, n, c))
        missing = sorted(c for c in contrib if c not in ' '.join(u.values()))
        if missing:
            notes.append('%s unit %s: its rows contribute to %s; name each begun code in What students learn, '
                         'with its later owner (no ~CODE in Owned standards)' % (
                slug, n, ', '.join(missing)))
        row_text = ' '.join(u.values())
        unnamed = []
        for c in sorted(owned_codes):
            kids = parts.get(c, [])
            if kids:
                got = named_parts(row_text, c) | (owned_codes & set(kids))
                unnamed += [k for k in kids if k not in got]
        if unnamed:
            notes.append('%s unit %s: lettered parts not named by code in the unit row (standards in full): %s' % (
                slug, n, ', '.join(unnamed)))
        cs = u.get('Check set adds', None)
        if cs is not None and cs.strip() and not re.match(r'\W*(candidate|none)', cs, re.I):
            fails.append('%s unit %s: the Check set adds cell does not start "Candidate" (lesson 2)' % (slug, n))
    for i in own:
        if i not in seen:
            fails.append('%s: course row %s is in no unit' % (slug, i))
    if f['years']:
        ycol = next(h for h in f['head'] if h.lower() in ('year', 'level'))
        per = {}
        for u in tab:
            d = re.match(r'\s*(\d+)', u.get('Days', ''))
            if not u.get(ycol, '').strip():
                fails.append('%s unit %s: the %s cell is empty' % (slug, u.get('#', '?'), ycol))
            per[u.get(ycol, '').strip()] = per.get(u.get(ycol, '').strip(), 0) + (int(d.group(1)) if d else 0)
        notes.append('%s: unit days by %s: %s' % (slug, ycol.lower(), ', '.join('%s %d' % kv for kv in per.items())))
    if f['days'] is not None:
        if day_sum > f['days']:
            fails.append('%s: unit days add to %d, more than the course\'s %d' % (slug, day_sum, f['days']))
        else:
            notes.append('%s: %d units, %d days (%d in units, %d for checks and respond days)' %
                         (slug, len(tab), f['days'], day_sum, f['days'] - day_sum))
    # the frame-write lessons (added 2026-11-14 as notes; those every frame passed became failures the same day)
    brief = section(t, 'The course in brief')
    if f['minutes'][0] is None:
        fails.append('%s: the **Days.** bullet gives no minutes a lesson (lesson 3)' % slug)
    if f['per_week'] is None:
        fails.append('%s: the **Days.** bullet gives no lessons a week (lesson 3)' % slug)
    if not re.search(r'^\s*[-*]\s*\*\*Sensitivity reads\.\*\*', brief, re.M):
        fails.append('%s: The course in brief has no **Sensitivity reads.** bullet (lesson 12)' % slug)
    if 'paper path' not in brief.lower():
        fails.append('%s: The course in brief names no paper path (lesson 14)' % slug)
    ch = f['checks']
    if not ch:
        fails.append('%s: no course-level check could be read from Course-level checks' % slug)
    for c in ch:
        if not c['review'] and not c['respond']:
            fails.append('%s: course-level check "%s" has no respond day (lesson 1)' % (slug, c['label'][:40]))
    head, _ = table(section(t, 'Course-level checks'))
    if head != ['Check', 'After unit', 'Check days', 'Respond days', 'What it checks']:
        notes.append('%s: Course-level checks is not in the one table shape '
                     '(| Check | After unit | Check days | Respond days | What it checks |)' % slug)
    if f['days'] is not None and ch and calendar(slug) is None:
        fails.append('%s: a course-level check names no unit the calendar can place it after' % slug)
    elif f['days'] is not None and ch:
        used = sum(c['check'] + c['respond'] + c['review'] for c in ch)
        if used + day_sum != f['days']:
            fails.append('%s: course-level days read from Course-level checks add to %d; the course has %d left' % (
                slug, used, f['days'] - day_sum))
    seams, models, cross = section(t, 'Seams'), section(t, 'Models carried'), section(t, 'Cross-subject')
    miss_s = sorted({a for r in own.values() for a in split(r['assumes']) + split(r['hands_on'])} - set(re.findall(r'[\w-]+', seams)))
    if miss_s:
        notes.append('%s: Seams does not name %s' % (slug, ', '.join(miss_s)))
    miss_m = sorted({m for r in own.values() for m in split(r['model_in']) + split(r['model_out'])
                     if m.lower() not in models.lower()})
    if miss_m:
        fails.append('%s: Models carried does not name %s' % (slug, ', '.join(miss_m)))
    miss_x = []
    for r in own.values():
        for x in [y.strip() for y in (r['cross_subject'] or '').split(';') if y.strip()]:
            mm = re.match(r'\s*([\w-]+)\s*:\s*~?([\w.\-]*\w)', x)
            ref = mm.group(2) if mm and mm.group(1) != 'lit' else ''   # lit: is an also-met literacy code, no lean
            if ref and ref not in cross:
                miss_x.append('%s (%s)' % (ref, r['skill_id']))
    if miss_x:
        fails.append('%s: Cross-subject does not name the lean %s' % (slug, ', '.join(sorted(miss_x))))
    hits = []
    for m in OUTSIDE_READER.finditer(t):
        if not re.search(r'\b(no|not|never|nor)\b[^.]*$', t[max(0, m.start() - 60):m.start()], re.I):
            hits.append(m.group(0))
    if hits:
        notes.append('%s: outside-reader wording %d time(s) (%s); FOUNDATION 7.3 (2026-11-14) assigns these reads '
                     'to agents' % (slug, len(hits), ', '.join('"%s"' % h for h in sorted(set(hits)))))
    if cal_rows is not None:
        notes += citations(slug, cal_rows)
    import stale
    fails += stale.check_file(path_of(slug))
    r = frames_csv().get(slug)
    if not r or str(f['units']) != r['units'].strip() or str(f['days']) != r['days'].strip():
        fails.append('%s: data/plans/frames.csv disagrees with the frame (run scripts/frame.py sync)' % slug)
    elif any(str(v) != (r.get(k) or '') for k, v in row_of(slug).items()):
        notes.append('%s: data/plans/frames.csv is behind the frame (run scripts/frame.py sync)' % slug)
    # Pending(<what it waits on>) marks a cell that waits on a Desk card, a load or a browser check (later.csv L154):
    # named here as waiting, never a failure
    waits = sorted(set(re.findall(r'Pending\(([^)]*)\)', open(path_of(slug), encoding='utf-8').read())))
    if waits:
        notes.append('%s: waiting on %d Pending marker(s): %s' % (slug, len(waits), '; '.join(waits)))
    return fails, notes


WRITING_FILE = os.path.join(ROOT, 'build', 'frames-writing.txt')


def writing():
    """Courses whose frames are being written now (build/frames-writing.txt, the lead's, git-ignored; added
    2026-11-25 while the after-core frames were written beside the Codex day lanes): the full `frame.py check`, which
    every course's gate runs, skips them with a note so a frame half written cannot show as a new failure in another
    course's gate. `frame.py check <slug>` still checks them in full. The lead empties the file when the frames are
    committed."""
    if not os.path.exists(WRITING_FILE):
        return set()
    return {l.strip() for l in open(WRITING_FILE, encoding='utf-8') if l.strip() and not l.startswith('#')}


def check_global():
    """Failures that belong to no one frame: frames.csv rows with no frame, courses with no frame, catalogue ids."""
    fails = []
    have = set(found()) | writing()
    for c in sorted(set(frames_csv()) - have):
        fails.append('data/plans/frames.csv: row %s has no frame (run scripts/frame.py sync)' % c)
    for c in sorted(set(COURSE_ROWS) - have):
        fails.append('%s: has rows in data/plans/course-list.csv but no docs/courses/%s/frame.md' % (c, c))
    cat = {r['course_id'] for r in csv.DictReader(open(os.path.join(ROOT, 'data', 'courses.csv'), encoding='utf-8'))}
    for c in sorted(COURSE_ROWS):
        if c not in COURSE_META:
            fails.append('%s: no catalog_id in data/plans/course-list.csv' % c)
        elif COURSE_META[c][0] not in cat:
            fails.append('%s: catalogue id %s is not in data/courses.csv' % (c, COURSE_META[c][0]))
    return fails


def found():
    return sorted(os.path.basename(os.path.dirname(p)) for p in glob.glob(os.path.join(ROOT, 'docs', 'courses', '*', 'frame.md')))


def row_of(s):
    f = parse(s)
    cat, g = COURSE_META.get(s, ('', ''))
    weeks, _, pw = meeting(s, f)
    return {'course': s, 'catalog_id': cat, 'subject': COURSE_ROWS.get(s, ('',))[0], 'grade': g, 'title': f['title'],
            'units': f['units'] or '', 'days': f['days'] or '', 'minutes_min': f['minutes'][0] or '',
            'minutes_max': f['minutes'][1] or '', 'per_week': f['per_week'] or '',
            'weeks': weeks if f['days'] else '', 'term': TERM.get(s, 'year'),
            'legacy_plan_id': next((k for k, v in LEGACY.items() if v == s), '')}


def meta(course):
    """A course's row in data/plans/frames.csv, by frame slug or legacy plan id (math-4), or None."""
    rs = frames_csv()
    return rs.get(LEGACY.get(course, course))


def write_calendar(cal):
    cols = ['course', 'grade', 'subject', 'kind', 'unit', 'label', 'first_day', 'last_day', 'first_school_day',
            'last_school_day', 'first_week', 'last_week']
    with open(CAL_CSV, 'w', encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, cols, lineterminator='\n')
        w.writeheader()
        for r in cal:
            w.writerow(r)
    if not os.path.exists(CAL_MD):
        return
    lines = ['| Grade | Course | Course-level check days (weeks) | Units end (week) |', '|---|---|---|---|']
    order = ['K'] + [str(i) for i in range(1, 13)]
    by = {}
    for r in cal:
        by.setdefault((r['grade'], r['subject'], r['course']), []).append(r)
    for (g, s, c), rs in sorted(by.items(), key=lambda kv: (order.index(kv[0][0]) if kv[0][0] in order else 99, kv[0][1], kv[0][2])):
        cw = ', '.join('%s %s' % (x['label'][:24], ('week %d' % x['first_week']) if x['first_week'] == x['last_week']
                                   else 'weeks %d to %d' % (x['first_week'], x['last_week'])) for x in rs if x['kind'] == 'check')
        ue = max((x['last_week'] for x in rs if x['kind'] == 'unit'), default='')
        lines.append('| %s | %s | %s | %s |' % (g, c, cw or 'none read', ue))
    cl = clashes(cal)
    lines.append('')
    lines.append('Stagger rule breaks (K to 5 by week, 6 to 8 by school day before the finals week): %s.' % (
        '; '.join('grade %s %s (%s)' % (g, w, ', '.join(ss)) for g, w, ss in cl) if cl else 'none'))
    gen = '\n'.join(lines)
    md = open(CAL_MD, encoding='utf-8').read()
    new = re.sub(r'(<!-- gen:calendar -->\n).*?(\n<!-- /gen -->)', lambda m: m.group(1) + gen + m.group(2), md, flags=re.S)
    if new != md:
        with open(CAL_MD, 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(new)


def sync():
    have = found()
    out = {s: row_of(s) for s in have}
    with open(FRAMES_CSV, 'w', encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, COLS, lineterminator='\n')
        w.writeheader()
        for k in sorted(out):
            w.writerow(out[k])
    print('frames.csv: %d course(s)' % len(out))
    cal = calendar_rows()
    write_calendar(cal)
    print('calendar.csv: %d row(s), %d course(s)' % (len(cal), len({r['course'] for r in cal})))


def main(a):
    if a[:1] == ['sync']:
        return sync()
    if a[:1] == ['calendar']:
        cal = calendar_rows()
        for g, subs in sorted(check_weeks(cal).items(), key=lambda kv: (kv[0] != 'K', int(kv[0]) if kv[0] != 'K' else 0)):
            print('grade %s: %s' % (g, '; '.join('%s weeks %s' % (s, ', '.join(str(w) for w, _, _ in ws))
                                                  for s, ws in sorted(subs.items()))))
        for g, w, ss in clashes(cal):
            print('  clash: grade %s %s: %s' % (g, w, ', '.join(ss)))
        return
    if a[:1] != ['check']:
        raise SystemExit(__doc__)
    bad = 0
    cal = calendar_rows()
    if not a[1:]:
        for x in check_global():
            print('  FAIL', x)
            bad += 1
    skip = set() if a[1:] else writing()
    if skip:
        print('  note %d frame(s) being written are skipped here (build/frames-writing.txt); check each by name' % len(skip))
    for s in a[1:] or [x for x in found() if x not in skip]:
        fails, notes = check(s, cal)
        print('frame %s: %d failure(s)' % (s, len(fails)))
        for x in fails:
            print('  FAIL', x)
        for x in notes:
            print('  note', x)
        bad += len(fails)
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main(sys.argv[1:])

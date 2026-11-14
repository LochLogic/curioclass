"""Unit plan skeletons for the four core subjects (social studies, math, ELA, science): every mechanical field
filled, every judgement field marked.

    python -X utf8 scripts/unit_skeleton.py <course> [<unit>] [--force] [--out DIR] [--data-dir DIR]
    python -X utf8 scripts/unit_skeleton.py --list [<subject>]   courses and unit counts; subject is social-studies,
                                                                  math, ela or science (default: all, social studies first)

One shared core builds every skeleton; a small adapter per subject (the `if subj ==` blocks in build(), the SUBJECT
table below) adds what that subject's unit plan needs mechanically. Social studies output is frozen: its lines come
from the shared core alone. --data-dir DIR reads DIR/<course>/days.csv, source-map.csv, materials.csv and
DIR/calendar.csv instead of data/plans (for tests, so synthetic data never sits in data/plans); the frame, the
progression and the standards still come from the repository.

Writes docs/courses/<course>/s{uu}.md in the shape of docs/courses/UNIT-PLAN.md (the unit plan, fields 1 to 10; the
section plans follow later, PRODUCTION-PATH step 7). Never overwrites an existing file without --force. --out DIR
writes DIR/<course>/s{uu}.md instead (for tests). Output is deterministic: same data, same bytes.

Filled from: data/plans/<course>/days.csv (days, kinds, goals, codes, assessment days, notes), data/plans/calendar.csv
(school days, weeks), data/progressions/social-studies.csv (skills, what they assume and hand on), the standards files
in data/standards/ (own-word lines and lettered parts), docs/courses/<course>/frame.md (unit title, compelling
question, models carried, check set, sensitive topics) and data/plans/<course>/source-map.csv where it exists.

Math adds: cluster weights (data/standards/ccss-math-focus.csv), the frame's practices, tools and supplies named in
day notes (or in tools/supplies columns and materials.csv where they exist), base-text lesson rows from source-map.csv.
ELA adds: the frame's text set, owned codes grouped by strand with the days they are taught (kind Understanding) and
practised (other kinds), writing types and writing days, base-text rows. Science adds: the anchoring phenomenon, the
frame's practices and crosscutting concepts, a three-dimensions table (one row per performance expectation), safety
and materials notes from day notes and the frame, base-text rows.

Left for the writer: a line that begins `TODO` followed by `(writer):` and what is needed (hook, supporting
questions, sources chosen, limits, teaching moves, items and answers, errors, response groups, tools, family note and
so on). scripts/unitplan.py check fails while any is left.

The day list at the end ("Day list") and fields 4 to 6 are tables and do not count toward the word cap.
"""
import csv
import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLANS = ROOT / 'data' / 'plans'
DOCS = ROOT / 'docs' / 'courses'
STD = ROOT / 'data' / 'standards'
PROGS = ROOT / 'data' / 'progressions'
SUBJECTS = ['social-studies', 'math', 'ela', 'science']
SUBJECT_STD = {   # standards files read for own-word lines and lettered parts, per subject (social studies frozen)
    'social-studies': ('ma-hss-2018.txt', 'c3-indicators.txt', 'ccss-literacy-6-12.txt'),
    'math': ('ccss-math-standards.txt',),
    'ela': ('ccss-ela-standards-full.txt', 'ccss-literacy-6-12.txt'),
    'science': ('ngss-pes.txt', 'ccss-literacy-6-12.txt'),
}
DATA_DIR = None                     # --data-dir: days.csv, source-map.csv, materials.csv, calendar.csv read from here
SUBJ = 'social-studies'             # the subject of the course being built or checked (set_subject)
OPEN = '<!-- skel -->'              # lines between these markers are mechanical copies of data and do not count toward the word cap
CLOSE = '<!-- /skel -->'
MARK = 'TODO' + '(writer)'          # built in two pieces so this file never trips its own check
EMDASH = chr(0x2014)


def read_csv(path):
    if not Path(path).exists():
        return []
    with io.open(path, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def set_data_dir(path):
    global DATA_DIR
    DATA_DIR = Path(path) if path else None


def set_subject(subj):
    global SUBJ
    SUBJ = subj


def plan_file(course, name):
    """data/plans/<course>/<name> (or DIR/<course>/<name> under --data-dir)."""
    return (DATA_DIR or PLANS) / course / name


def courses_of(subject=None):
    """Course ids in data/plans/frames.csv order, for one subject or (None) all four, social studies first."""
    rows = read_csv(PLANS / 'frames.csv')
    if subject:
        return [r['course'] for r in rows if r['subject'] == subject]
    return [r['course'] for s in SUBJECTS for r in rows if r['subject'] == s]


def subject_of(course):
    for r in read_csv(PLANS / 'frames.csv'):
        if r['course'] == course:
            return r['subject']
    return None


def ss_courses():
    """The social studies course ids, in data/plans/frames.csv order."""
    return courses_of('social-studies')


def days_rows(course):
    return read_csv(plan_file(course, 'days.csv'))


def unit_numbers(course):
    return sorted({int(r['stretch']) for r in days_rows(course) if r['stretch'].isdigit()})


def unit_days(course, unit):
    return [r for r in days_rows(course) if r['stretch'] == str(unit)]


def split_list(s):
    return [x.strip() for x in re.split(r'\s*[;,]\s*', s or '') if x.strip()]


_STD = {}


def std_text():
    """code -> own-word line ('' for files that hold ids only: the C3 file, the NGSS file) for the current subject."""
    if SUBJ not in _STD:
        d = {}
        for name in SUBJECT_STD[SUBJ]:
            p = STD / name
            if not p.exists():
                continue
            for line in io.open(p, encoding='utf-8'):
                if line.startswith('#') or not line.strip():
                    continue
                code, _, text = line.rstrip('\n').partition('\t')
                d[code.strip()] = text.strip()
        _STD[SUBJ] = d
    return _STD[SUBJ]


def children(code):
    """Lettered parts of a standard: the codes that are the code plus one lowercase letter. A topic heading
    (last segment not starting with a digit, as MA.6.T3) has none."""
    if not code.split('.')[-1][:1].isdigit():
        return []
    std = std_text()
    return sorted(k for k in std if len(k) == len(code) + 1 and k.startswith(code) and k[-1].islower())


def required_codes(rows):
    """Codes a unit must carry: every code in its days.csv rows, in first-seen order, each followed by its lettered
    parts that days.csv does not itself list."""
    seen, out = set(), []
    for r in rows:
        for c in split_list(r['codes']):
            if c not in seen:
                seen.add(c)
                out.append(c)
    for c in list(out):
        for ch in children(c):
            if ch not in seen:
                seen.add(ch)
                out.append(ch)
    return out


def days_codes_order(rows):
    """days.csv codes in first-seen order, with each code's lettered parts placed right after it."""
    out = []
    for c in required_codes(rows):
        out.append(c)
    # place children after their parent
    ordered = []
    for c in out:
        if c in ordered:
            continue
        if len(c) > 1 and c[-1].islower() and c[:-1] in out:
            continue
        ordered.append(c)
        ordered.extend(ch for ch in children(c) if ch in out)
    for c in out:
        if c not in ordered:
            ordered.append(c)
    return ordered


def clean(s):
    return (s or '').replace(EMDASH, ', ').replace('|', '/').replace('\n', ' ').strip()


def table_rows(lines, header_start):
    """Rows (list of cells) of the first markdown table whose header line starts with header_start."""
    out, on = [], False
    for ln in lines:
        if not on:
            if ln.startswith(header_start):
                on = True
            continue
        if not ln.startswith('|'):
            break
        cells = [c.strip() for c in ln.strip().strip('|').split('|')]
        if set(''.join(cells)) <= set('-: '):
            continue
        out.append(cells)
    return out


def frame_lines(course):
    p = DOCS / course / 'frame.md'
    return p.read_text(encoding='utf-8').splitlines() if p.exists() else []


def frame_unit(course, unit):
    for cells in table_rows(frame_lines(course), '| # | Unit and compelling question'):
        if cells and cells[0] == str(unit) and len(cells) >= 10:
            return cells
    return None


def frame_models(course, unit):
    """(model, how) for each model of the frame's Models carried table that names this unit."""
    rows = table_rows(frame_lines(course), '| Model |')
    out = []
    pat = re.compile(r'unit %d(?!\d)' % unit, re.I)
    for cells in rows:
        if len(cells) < 4:
            continue
        if not is_ss():
            if unit in unit_nums(cells[2]):
                out.append((cells[0], 'introduced or first used here: ' + cells[2]))
            elif unit in unit_nums(cells[3]):
                out.append((cells[0], 'used again here: ' + cells[3] + ' (from: ' + cells[2] + ')'))
        elif pat.search(cells[2]):
            out.append((cells[0], 'introduced or first used here: ' + cells[2]))
        elif pat.search(cells[3]):
            out.append((cells[0], 'used again here: ' + cells[3] + ' (from: ' + cells[2] + ')'))
    return out


def split_title(cell):
    """('Where we live', 'Why is our town where it is?') from the frame's 'Title. "Question?"' cell."""
    cell = cell.strip()
    m = re.match(r'^(.*?)\.\s+"(.+)"\s*$', cell)
    if m:
        return m.group(1).strip(), m.group(2).strip()
    idx = [m.start() for m in re.finditer(r'\.\s', cell)]
    for i in idx:
        rest = cell[i + 1:].strip()
        if rest.endswith('?') and not re.search(r'\.\s', rest):
            return cell[:i].strip(), rest
    return cell, ''


def calendar_rows(course, unit):
    return [r for r in read_csv((DATA_DIR or PLANS) / 'calendar.csv')
            if r['course'] == course and r['kind'] == 'unit' and r['unit'] == str(unit)]


def runs(nums):
    """Consecutive runs of a sorted list of ints: [(26, 38), (55, 55)]."""
    out = []
    for n in sorted(nums):
        if out and n == out[-1][1] + 1:
            out[-1] = (out[-1][0], n)
        else:
            out.append((n, n))
    return out


def runs_text(nums):
    """'26 to 38 and 55' for the header; the checker parses the same shape."""
    return ' and '.join(('%d to %d' % r) if r[0] != r[1] else str(r[0]) for r in runs(nums))


def progression():
    return {r['skill_id']: r for r in read_csv(PROGS / (SUBJ + '.csv'))}


def grade_of(skill, prog):
    r = prog.get(skill)
    return r['grade'] if r else '?'


# ---------------------------------------------------------------------------------------------------------------
# Per-subject layer (math, ELA, science). Social studies uses none of it.

STRANDS = [('RL', 'Reading literature'), ('RI', 'Reading informational text'), ('RF', 'Reading foundational skills'),
           ('W', 'Writing'), ('SL', 'Speaking and listening'), ('L', 'Language')]
WTYPE = {'1': 'argument (opinion in kindergarten to grade 5)', '2': 'informative or explanatory writing',
         '3': 'narrative writing', '4': 'clear and coherent writing for task, purpose and audience',
         '5': 'planning, revising and editing', '6': 'using technology to produce and publish',
         '7': 'a research project', '8': 'gathering and citing sources', '9': 'drawing evidence from texts',
         '10': 'writing over time (routine and extended)'}
WRITEWORDS = re.compile(r'\b(draft\w*|essay\w*|write|writes|writing|paragraph\w*|argument\w*|narrative\w*|article\w*|'
                        r'revis\w*|publish\w*|report\w*|poem\w*|scene\w*|opinion\w*|informative|research\w*)\b', re.I)
SAFEWORDS = re.compile(r'\b(safety|goggles?|eye protection|gloves|hazard\w*|chemical\w*|flame|heat\w*|allerg\w*|sharp|'
                       r'ventilat\w*|demonstration|teacher-only|disposal|food policy)\b', re.I)
TOOLWORDS = re.compile(r'\b(tools?|simulations?|applets?|calculators?|manipulatives?|supplies|materials?|paper|ruler|'
                       r'protractor|compass|string|kit|device|spinners?|cubes|slips|film|audio|recording|print\w*|'
                       r'household|no-kit|number line|tracing|grid|data sheet|drawing tool|construction tool)\b', re.I)
TOOLCOLS = ('tools', 'tool', 'supplies', 'materials', 'safety')
_FOCUS = {}


def is_ss():
    return SUBJ == 'social-studies'


def focus_weights():
    """cluster -> major, supporting, additional (K to 8) or wap (high school), from data/standards/ccss-math-focus.csv."""
    if not _FOCUS:
        p = STD / 'ccss-math-focus.csv'
        if p.exists():
            lines = [ln for ln in io.open(p, encoding='utf-8') if ln.strip() and not ln.startswith('#')]
            for r in csv.DictReader(lines):
                _FOCUS[r['cluster']] = r['focus']
    return _FOCUS


def cluster_of(code):
    """7.RP.A.2a gives 7.RP.A; A-SSE.A.1 gives A-SSE.A."""
    p = code.split('.')
    n = 3 if (p[0].isdigit() or p[0] == 'K') else 2
    return '.'.join(p[:n])


def unit_nums(text):
    """The unit numbers a frame cell names ('Units 2, 3 (x), 4' gives 2, 3 and 4); a unit of another grade or course
    ('grade 8 unit 3', 'Geometry unit 2') is not counted."""
    text = re.sub(r'\([^)]*\)', ' ', text)
    out = set()
    for m in re.finditer(r'\b[Uu]nits?\s+(\d+(?:\s*(?:,|and|to)\s*\d+)*)', text):
        before = text[:m.start()].rstrip()
        if re.search(r'([Gg]rade \d+|[Gg]rades \d+ and \d+|Algebra I+|Geometry|Biology|Chemistry|Physics|course)$', before):
            continue
        toks = re.findall(r'\d+|\bto\b', m.group(1))
        i = 0
        while i < len(toks):
            if i + 2 < len(toks) and toks[i + 1] == 'to':
                out.update(range(int(toks[i]), int(toks[i + 2]) + 1))
                i += 3
            else:
                if toks[i] != 'to':
                    out.add(int(toks[i]))
                i += 1
    return out


def split_unit_cell(cell):
    """(title, question, anchor) from the frame's unit cell; the 'Anchor: ...' tail is science's phenomenon."""
    anchor = ''
    if not is_ss():
        m = re.search(r'\s+Anchor:\s*(.+)$', cell.strip())
        if m:
            anchor = m.group(1).strip()
            cell = cell.strip()[:m.start()]
    t, q = split_title(cell)
    return t, q, anchor


def frame_cross(course, unit):
    """Rows of the frame's Cross-subject table that name this unit (cells as a list)."""
    lines = frame_lines(course)
    for ln in lines:
        if ln.startswith('| Other subject'):
            head = [c.strip().lower() for c in ln.strip().strip('|').split('|')]
            ucol = next((k for k, c in enumerate(head) if 'unit' in c), None)
            if ucol is None:
                return []
            return [cells for cells in table_rows(lines, ln[:20]) if len(cells) > ucol and unit in unit_nums(cells[ucol])]
    return []


def strand_of(code):
    pre = code.split('.')[0]
    for k, name in STRANDS:
        if pre == k:
            return k, name
    return pre, 'Literacy in other subjects'


def day_uses(rows, code):
    """(taught, practised) day numbers where days.csv names the code or one of its lettered parts. Taught: kind
    Understanding; practised: every other kind."""
    names = {code} | set(children(code))
    taught, prac = [], []
    for r in rows:
        if names & set(split_list(r['codes'])):
            (taught if r['kind'] == 'Understanding' else prac).append(int(r['day']))
    return taught, prac


def days_or_none(nums):
    return runs_text(nums) if nums else 'none'


def base_text_of(course):
    """The base text a course adapts (docs/sources/BASE-TEXTS.md), or '' when the course is our own."""
    meta = next((r for r in read_csv(PLANS / 'frames.csv') if r['course'] == course), {})
    g = meta.get('grade', '')
    if SUBJ == 'math':
        return 'Illustrative Mathematics K-12 (CC BY 4.0)'
    if SUBJ == 'science' and g in ('6', '7', '8'):
        return 'OpenSciEd Middle School (CC BY 4.0)'
    if SUBJ == 'ela' and g in ('K', '1', '2', '3', '4', '5'):
        return 'EL Education K-5, 2017 (CC BY 4.0)'
    return ''


def source_rows(course, unit):
    return [r for r in read_csv(plan_file(course, 'source-map.csv')) if r['unit'].split('.')[0] == str(unit)]


def files_with(codes):
    names = []
    for name in SUBJECT_STD[SUBJ]:
        p = STD / name
        if not p.exists():
            continue
        keys = set()
        for line in io.open(p, encoding='utf-8'):
            if line.startswith('#') or not line.strip():
                continue
            keys.add(line.split('\t')[0].strip())
        if any(c in keys for c in codes):
            names.append('data/standards/' + name)
    return names


def day_note_lines(rows, rx, skip=None, goal_too=True):
    out = []
    for r in rows:
        note = clean(r['note'])
        goal = clean(r['goal']) if goal_too else ''
        if rx.search(note) or rx.search(goal):
            if skip is not None and skip.search(note):
                continue
            out.append('  - Day %s (%s): %s' % (r['day'], r['kind'], note or goal))
    return out


def column_lines(rows):
    out = []
    for col in TOOLCOLS:
        if rows and col in rows[0]:
            for r in rows:
                if r[col].strip():
                    out.append('  - Day %s, %s column: %s' % (r['day'], col, clean(r[col])))
    return out


def material_lines(course, rows):
    days = {r['day'] for r in rows}
    out = []
    for m in read_csv(plan_file(course, 'materials.csv')):
        used = set((m.get('used_days') or '').split())
        if m.get('made_day') in days or used & days:
            out.append('  - %s (made day %s, used days %s, per %s, kept in %s)'
                       % (clean(m.get('material', '')), m.get('made_day', ''), m.get('used_days', ''),
                          m.get('per', ''), m.get('kept_in', '')))
    return out


PE_RE = re.compile(r'^(?:K-2|3-5|K|[1-5]|MS|HS)-[A-Z]+\d(?:-\d+)?$')
WEIGHTWORD = {'major': 'major', 'supporting': 'supporting', 'additional': 'additional', 'wap': 'prerequisite'}

# The judgement-line wording that differs by subject. Social studies is frozen: its entries are the original text.
TXT = {
    'social-studies': {
        'hook': 'Hook for day 1 (what students meet first, tied to the question; sources named in field 10).',
        'supq': 'Supporting questions (the ones the class writes together, with the day each is answered).',
        'claim': 'The closing claim: what students claim, from which named sources, on which day it is written.',
        'carried': 'Carried: for each model above, what happens to it over the unit (read and returned to, tied, revised or withdrawn), and the day.',
    },
    'math': {
        'hook': 'Hook for day 1 (the task or question students meet first, tied to the compelling question; its source named in field 10).',
        'supq': 'Supporting questions (the ones the class asks and answers, with the day each is answered).',
        'claim': 'The closing claim: what students can say, show or solve at the end of the unit, from which named tasks, and the day it is checked.',
        'carried': 'Carried: for each model above, the day it is tied to the written form, the day it is withdrawn, and what happens to it in between (UNIT-PLAN.md rule 12).',
    },
    'science': {
        'hook': 'Hook for day 1: the anchoring phenomenon or design problem as students first meet it (what they see, hear or handle), tied to the compelling question; its source named in field 10.',
        'supq': 'Question board: the questions students are expected to raise from the phenomenon, grouped, and the day each is answered.',
        'claim': 'The closing explanation: what students explain about the phenomenon, from which evidence they gathered or read, and the day the class writes it.',
        'carried': 'Carried: for each model above, how it is revised over the unit (the day of the initial model, each revision with the evidence that caused it, and the consensus model).',
    },
    'ela': {
        'hook': 'Hook for day 1: the first text or text moment and how it opens the compelling question; sources named in field 10.',
        'supq': 'Supporting questions (text-dependent questions that move from what the text says, to how it says it, to what it means beside the other texts; the day each is answered).',
        'claim': 'The closing claim: what students claim in the main piece of writing or talk, from which named texts, and the day it is written.',
        'carried': 'Carried: for each model above, what is read and returned to (the day it first appears, each text it returns to, and the day it is last used).',
    },
}


def is_pe(code):
    return bool(PE_RE.match(code))


def math_clusters(codes):
    """[(cluster, weight word or '', [codes])] in first-seen order, from data/standards/ccss-math-focus.csv."""
    fw = focus_weights()
    order, byc = [], {}
    for c in codes:
        k = cluster_of(c)
        if k not in byc:
            byc[k] = []
            order.append(k)
        byc[k].append(c)
    return [(k, fw.get(k, ''), byc[k]) for k in order]


def header_weight(codes):
    """Lines that follow the header paragraph (non-social-studies)."""
    L = []
    if SUBJ == 'math':
        cl = math_clusters(codes)
        groups = []
        for wt in ('major', 'supporting', 'additional', 'wap'):
            ks = [k for k, w_, _ in cl if w_ == wt]
            if ks:
                groups.append('%s (%s)' % (WEIGHTWORD[wt], ', '.join(ks)))
        L.append(OPEN)
        L.append('Weight (Student Achievement Partners, data/standards/ccss-math-focus.csv): %s.' % ('; '.join(groups) or 'none on file'))
        L.append(CLOSE)
        miss = [k for k, w_, _ in cl if not w_]
        if miss:
            L.append('%s: Weight of cluster %s: not in data/standards/ccss-math-focus.csv (missing data); state it and its source.' % (MARK, ', '.join(miss)))
    else:
        L.append(OPEN)
        L.append('Weight: not used in this subject (the weight field is math only, UNIT-PLAN.md field 1).')
        L.append(CLOSE)
    return L


def field2_extras(course, unit, rows, codes, fr, anchor):
    """Subject lines after the standards and progression blocks of field 2."""
    L = []
    c3 = clean(fr[5]) if fr else ''
    if SUBJ == 'math':
        L.append(OPEN)
        if c3:
            L.append('- **Practices (frame, C3 column):** %s' % c3)
        L.append(CLOSE)
        L.append('%s: Practices: for each practice named above, the task where students do it, and its day.' % MARK)
        L.append('%s: Fluency: which owned standards set an expected fluency (the frame\'s fluency note) and how it is built with no timer shown to students, or one line saying the unit sets none.' % MARK)
    elif SUBJ == 'ela':
        L.append(OPEN)
        if c3:
            L.append('- **Text set (frame, C3 column):** %s' % c3)
        L.append('- **Owned codes by strand (days.csv: taught = days of kind Understanding, practised = days of any other kind):**')
        by = {}
        for c in codes:
            if len(c) > 1 and c[-1].islower() and c[:-1] in codes:
                continue
            by.setdefault(strand_of(c), []).append(c)
        names = [k for k, _ in STRANDS]
        for key in sorted(by, key=lambda kn: (names.index(kn[0]) if kn[0] in names else 99, kn[0])):
            parts = []
            for c in by[key]:
                t, p = day_uses(rows, c)
                parts.append('%s (taught: %s; practised: %s)' % (c, days_or_none(t), days_or_none(p)))
            L.append('  - %s (%s): %s' % (key[1], key[0], '; '.join(parts)))
        wnums = []
        for c in codes:
            parts = c.split('.')
            if parts[0] == 'W' and len(parts) >= 3:
                n = re.match(r'\d+', parts[2]).group(0)
                if n not in wnums:
                    wnums.append(n)
        if wnums:
            L.append('- **Writing types (the W codes of this unit):**')
            for n in wnums:
                ds = sorted({int(r['day']) for r in rows
                             if any(x.split('.')[0] == 'W' and len(x.split('.')) >= 3 and re.match(r'\d+', x.split('.')[2]).group(0) == n
                                    for x in split_list(r['codes']))})
                L.append('  - W.x.%s, %s: days %s' % (n, WTYPE.get(n, 'writing'), days_or_none(ds)))
        wl = [r for r in rows if WRITEWORDS.search(r['goal'])]
        if wl:
            L.append('- **Days whose goal names writing (days.csv goals):**')
            for r in wl:
                L.append('  - Day %s (%s): %s' % (r['day'], r['kind'], clean(r['goal'])))
        L.append(CLOSE)
        L.append('%s: Anchor and paired texts: for each text in the text set above, say which is the anchor and which is paired, the day it is read, and its rights line. Missing data: the text records (texts.csv, UNIT-PLAN.md) are not built.' % MARK)
        L.append('%s: Text complexity: for each anchor, the measure where usable, the qualitative demands, the reader and task, and the support, in a line each (missing data: texts.csv).' % MARK)
        L.append('%s: Word list: the words drawn from the texts for the unit, about 8 to 10 a week, met before, during and after reading (missing data: words.csv is not built).' % MARK)
        L.append('%s: Main piece of writing: its type, the process (plan, draft, revise, edit, publish) or on-demand, the day it is assigned and the day it is finished; and the writing tasks above that are short pieces.' % MARK)
        L.append('%s: Taught versus practised: check the split above against the unit\'s goals and say which owned codes the unit teaches and which it only practises.' % MARK)
    elif SUBJ == 'science':
        L.append(OPEN)
        if anchor:
            L.append('- **Anchoring phenomenon or design problem (frame):** %s' % clean(anchor))
        if c3:
            L.append('- **Practices and crosscutting concepts (frame, C3 column, the unit\'s own focal list):** %s' % c3)
        L.append(CLOSE)
        if not anchor:
            L.append('%s: Anchoring phenomenon or design problem: the frame\'s unit cell names none (missing data); name it on a line that begins "Anchor:".' % MARK)
        pes = [c for c in codes if is_pe(c)]
        if pes:
            mp = re.search(r'Practices:\s*(.*?)(?:\.?\s*Crosscutting|$)', c3)
            mc = re.search(r'Crosscutting(?: concepts)?:\s*(.*)$', c3)
            prac = mp.group(1).strip() if mp and mp.group(1).strip() else 'not in the frame'
            ccc = mc.group(1).strip() if mc and mc.group(1).strip() else 'not in the frame'
            L.append('')
            L.append('Three dimensions of each performance expectation (names only; the Next Generation Science Standards are never named in student, teacher or family copy):')
            L.append('')
            L.append('| Performance expectation | Science and engineering practice | Core idea | Crosscutting concept |')
            L.append('|---|---|---|---|')
            for c in pes:
                L.append('| %s | %s: practice this expectation uses (unit list: %s) | %s: core idea (missing data: no core idea text on file) | %s: crosscutting concept (unit list: %s) |'
                         % (c, MARK, prac, MARK, MARK, ccc))
            L.append('')
        L.append('%s: Storyline: the question board (what students notice and wonder), the initial class model and its day, each revision with the evidence that causes it, the consensus model and its day, and the unseen phenomenon the end-of-unit assessment uses.' % MARK)
    return L


def field3_extras(course, unit, skills, prog):
    cross = [(s, clean(prog[s].get('cross_subject', ''))) for s in skills if s in prog and prog[s].get('cross_subject', '').strip()]
    fc = frame_cross(course, unit)
    if not cross and not fc:
        return []
    L = [OPEN]
    if cross:
        L.append('- **Cross-subject (progression, cross_subject column):** ' + '; '.join('%s: %s' % x for x in cross) + '.')
    if fc:
        L.append('- **Cross-subject (frame, rows that name this unit):**')
        for cells in fc:
            L.append('  - ' + clean('; '.join(c for c in cells if c)))
    L.append(CLOSE)
    return L


def field8_lines(course, rows, fr):
    L = [OPEN]
    items = column_lines(rows)
    if SUBJ == 'science':
        safe = day_note_lines(rows, SAFEWORDS, goal_too=False)
        tools = day_note_lines(rows, TOOLWORDS, skip=SAFEWORDS)
        L.append('- **Materials and tools named in days.csv (notes and goals):**')
        L.extend(items + tools or ['  - none named'])
        L.append('- **Safety named in days.csv notes:**')
        L.extend(safe or ['  - none named'])
        if fr and fr[9].strip():
            L.append('- **Safety and teacher notes (frame, last column of the unit row):** %s' % clean(fr[9]))
    else:
        tools = day_note_lines(rows, TOOLWORDS)
        L.append('- **Tools and supplies named in days.csv (notes and goals):**')
        L.extend(items + tools or ['  - none named'])
    mats = material_lines(course, rows)
    if mats:
        L.append('- **Materials (data/plans/%s/materials.csv):**' % course)
        L.extend(mats)
    L.append(CLOSE)
    if SUBJ == 'math':
        L.append('%s: Tools (each with its day, mark key or light, job, verdict and a link to TOOL-ASKS.md; or "None") and the supplies list. Every task has a paper path.' % MARK)
    elif SUBJ == 'science':
        L.append('%s: Tools and materials: for each investigation the three tiers (household stand-ins, a no-kit data path said plainly to be weaker, a Curio Class simulation marked spec only), the cost to a class, each tool with its day, mark, job and verdict (link to TOOL-ASKS.md), and for every hands-on day the hazards, the controls, the eye protection and the teacher-only steps.' % MARK)
    else:
        L.append('%s: Tools and supplies: the print copy of every text, each tool with its day, mark, job and verdict (link to TOOL-ASKS.md; or "None"), and the paper path of any digital step, saying plainly what the paper path does not meet.' % MARK)
    return L


def field10_extras(course, unit):
    """Source-map lines (inside the skel block) and the missing-data lines for a non-social-studies unit."""
    base = base_text_of(course)
    sm = source_rows(course, unit)
    L, miss = [], []
    if sm:
        L.append('- **Base text%s and source map (data/plans/%s/source-map.csv), rows for unit %d:**' % (' ' + base if base else '', course, unit))
        count = {}
        for r in sm:
            count[r['decision']] = count.get(r['decision'], 0) + 1
            extra = ''
            if r.get('order_conflict', '').strip():
                extra = ' Order conflict: %s (harms learning: %s).' % (clean(r['order_conflict']), r.get('harms_learning', '') or 'not stated')
            L.append('  - %s, %s: standards %s; goals %s; our days %s; %s. %s%s'
                     % (r['source'], clean(r['title']), clean(r.get('standards', '')) or 'none listed', clean(r.get('goals', '')) or 'none listed',
                        r['days'] or 'none', r['decision'], clean(r['why']), extra))
        L.append('- **Source-map decisions in this unit:** %s.' % ', '.join('%s %d' % (k, v) for k, v in sorted(count.items())))
    elif base:
        L.append('- **Base text:** %s; data/plans/%s/source-map.csv has no rows for unit %d.' % (base, course, unit))
        miss.append('%s: Base text lessons used: data/plans/%s/source-map.csv has no rows for this unit (missing data; it comes with the scope and sequence, sequence-write.md rule 8); list the lessons, their days and decisions.' % (MARK, course))
    return L, miss


def uniq(seq):
    seen, out = set(), []
    for x in seq:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


def sections_of(rows):
    secs = {}
    for r in rows:
        secs.setdefault(r['unit'], []).append(int(r['day']))
    return sorted(secs.items(), key=lambda kv: min(kv[1]))


def build(course, unit):
    allrows = days_rows(course)
    rows = [r for r in allrows if r['stretch'] == str(unit)]
    if not rows:
        raise SystemExit('%s has no unit %s' % (course, unit))
    byday = {int(r['day']): r for r in allrows}
    first, last = int(rows[0]['day']), int(rows[-1]['day'])
    prog = progression()
    std = std_text()
    subj = SUBJ
    ss = is_ss()
    tx = TXT[subj]
    fr = frame_unit(course, unit)
    title, question, anchor = split_unit_cell(fr[1]) if fr else ('Unit %s' % unit, '', '')
    frame_meta = next((r for r in read_csv(PLANS / 'frames.csv') if r['course'] == course), {})
    cal = calendar_rows(course, unit)
    kinds = {}
    for r in rows:
        kinds[r['kind']] = kinds.get(r['kind'], 0) + 1
    order = ['Understanding', 'Fluency', 'Application', 'Check', 'Respond']
    kind_txt = ', '.join('%s %d' % (k.lower(), kinds[k]) for k in order if k in kinds)
    sections = sections_of(rows)
    W = []
    w = W.append

    # ---- field 1: header
    w('# Unit %d: %s' % (unit, clean(title)))
    w('')
    w('<!-- Skeleton from scripts/unit_skeleton.py. Mechanical fields are filled from data; change one only if it is '
      'wrong, and say so in your last message. Replace every marker line with the content it asks for. -->')
    w('')
    sd = ''
    if cal:
        sdays = [n for r in cal for n in range(int(r['first_school_day']), int(r['last_school_day']) + 1)]
        sd = '; school days %s, weeks %s to %s' % (runs_text(sdays), cal[0]['first_week'], cal[-1]['last_week'])
    sec_txt = '; '.join('%s (days %s)' % (k, runs_text(v)) for k, v in sections)
    w('Course `%s` (%s). **Days %s** (%d course days%s). Sections: %s. Days by kind: %s. '
      'A plan, not a lesson: nothing here is built or tried with children. Fields follow UNIT-PLAN.md.'
      % (course, clean(frame_meta.get('title', course)), runs_text([int(r['day']) for r in rows]), len(rows), sd,
         sec_txt, kind_txt))
    w('')
    if ss:
        w('%s: Weight (major, supporting or additional) if this course uses it, otherwise one line saying it does not.' % MARK)
    else:
        W.extend(header_weight(required_codes(rows)))
    if len(sections) > 1:
        w('%s: Name each section (%s) in one line each; days.csv holds only their numbers and days.'
          % (MARK, ', '.join(k for k, _ in sections)))
    w('')

    # ---- field 2: standards
    w('## 2. Standards, limits, and what is carried')
    w('')
    if question:
        w('- **Compelling question (frame):** "%s"' % clean(question))
    w('%s: %s' % (MARK, tx['hook']))
    w('%s: %s' % (MARK, tx['supq']))
    w('%s: %s' % (MARK, tx['claim']))
    w('%s: Teaching moves across the unit: what the teacher does to keep the inquiry going (where to model, where to step back).' % MARK)
    w('')
    codes = days_codes_order(rows)
    w(OPEN)
    c3_nolines = []
    for c in codes:
        if len(c) > 1 and c[-1].islower() and c[:-1] in codes:
            continue
        txt = std.get(c, '')
        kids = [k for k in children(c) if k in codes]
        if not txt:
            c3_nolines.append(c)
            w('- **%s:** (no own-word line in the standards file%s)' % (c, '' if c in std else '; code not found'))
            continue
        if kids:
            parts = '; '.join('%s (%s) %s' % (k[-1], k, clean(std[k])) for k in kids)
            w('- **%s:** %s Parts, by verb: %s' % (c, clean(txt), parts))
        else:
            w('- **%s:** %s Parts, by verb: whole standard.' % (c, clean(txt)))
    w(CLOSE)
    w('')
    if c3_nolines and ss:
        w('%s: The skill codes above with no own-word line (%s): give each one line, in your own words, and its parts by '
          'verb, from the indicator in data/standards/c3-indicators.txt.' % (MARK, ', '.join(c3_nolines)))
    elif c3_nolines and subj == 'science':
        w('%s: The performance expectations above have no statement on file (%s; missing data: data/standards/ngss-pes.txt holds codes only): '
          'give each one line, in your own words, with its assessment boundary.' % (MARK, ', '.join(c3_nolines)))
    elif c3_nolines:
        w('%s: The codes above that are not in the standards file (%s; missing data): give each one line, in your own words, '
          'and its parts by verb.' % (MARK, ', '.join(c3_nolines)))
    skills = uniq(s for r in rows for s in split_list(r['skills']))
    w(OPEN)
    w('- **Progression skills owned (data/progressions/%s.csv):** %s.' % (subj, '; '.join(skills)))
    models = frame_models(course, unit)
    if models:
        w('- **Carried (frame, models carried):**')
        for m, how in models:
            w('  - %s: %s' % (clean(m), clean(how)))
    else:
        w('- **Carried (frame, models carried):** the frame names no model for this unit.')
    w(CLOSE)
    if not ss:
        W.extend(field2_extras(course, unit, rows, codes, fr, anchor))
    w('%s: Limits (what this unit does not teach or assess, and why).' % MARK)
    w('%s: %s' % (MARK, tx['carried']))
    w('')

    # ---- field 3: where it sits
    w('## 3. Where it sits')
    w('')
    assumes = uniq(a for s in skills if s in prog for a in split_list(prog[s]['assumes']))
    hands = uniq(a for s in skills if s in prog for a in split_list(prog[s]['hands_on']))
    own = set(skills)
    def lab(x):
        return '%s (grade %s)' % (x, grade_of(x, prog))
    w(OPEN)
    w('- **Builds on (progression, assumes):** %s.' % ('; '.join(lab(a) for a in assumes if a not in own) or 'none listed'))
    w('- **Leads to (progression, hands on):** %s.' % ('; '.join(lab(a) for a in hands if a not in own) or 'none listed'))
    if fr:
        w('- **Why this unit, here (frame):** %s' % clean(fr[7]))
    w(CLOSE)
    if not ss:
        W.extend(field3_extras(course, unit, skills, prog))
    w('%s: Builds on: mark each handoff strong or weak, and say what the previous unit leaves (its last day file Tomorrow line and carried list).' % MARK)
    w('%s: Comes back: where this unit\'s ideas return later in the course, by unit and day.' % MARK)
    w('')

    # ---- field 4: readiness
    w('## 4. Readiness check, whole')
    w('')
    prev = byday.get(first - 1)
    retr = []
    for r in rows:
        for m in re.finditer(r'retrieval tasks?\b[^;]*', r['note'], re.I):
            retr.append((int(r['day']), clean(m.group(0))))
    given_prev = prev is not None and (prev['assess'] == 'readiness' or
                                       re.search(r"(unit %d's|next unit's) readiness" % unit, prev['note'], re.I) is not None)
    w_ready = False
    if first == 1:
        w('**Given:** the start-of-year check, before day 1 (served in unit 1, which defines it).')
        w('%s: Define the start-of-year check: what it asks and how the teacher uses it (or say this course has none, and why).' % MARK)
        w_ready = True
    elif given_prev:
        w('**Given:** day %d, the last ten minutes (days.csv day %d: kind %s, assess = %s). Note there: "%s"'
          % (int(prev['day']), int(prev['day']), prev['kind'], prev['assess'] or 'blank', clean(prev['note'])))
        w_ready = True
    elif retr:
        w('**Retrieval only:** days.csv holds no readiness check before this unit; the retrieval tasks below are its before-teaching evidence.')
    else:
        w('**Given:** none (days.csv holds no readiness check before this unit and no retrieval task in its days).')
    if w_ready:
        w('')
        w('| # | Code | The item | Key | Serves section |')
        w('|---|---|---|---|---|')
        w('| 1 | | %s: item, with its key and the earlier row it tests | | |' % MARK)
        w('')
        w('%s: Readiness items (at least one for each earlier-grade row the note above names), a gap-by-gap ten-minute reteach, '
          'when it happens, and the earlier tool or page.' % MARK)
    if retr:
        w('')
        w('Retrieval tasks (rows used the year before or earlier the same year; days.csv notes):')
        w('')
        w('| Day | The row and task (days.csv) | The prompt, and what the teacher does with a miss |')
        w('|---|---|---|')
        for d, t in retr:
            w('| %d | %s | %s: the prompt, and what the teacher does with a miss |' % (d, t, MARK))
    w('')

    # ---- field 5: end-of-unit assessment
    w('## 5. End-of-unit assessment, whole')
    w('')
    ass = [r for r in rows if r['assess'] in ('end', 'mid')]
    for r in ass:
        label = 'End-of-unit assessment' if r['assess'] == 'end' else 'Mid-unit assessment'
        w('Day %s (%s): %s' % (r['day'], label, clean(r['goal'])))
        if r['note']:
            w('Note (days.csv): %s' % clean(r['note']))
        w('')
        w('| Day | Code | Part (own words) | The item, answer and wrong answers (error letter) | Owner |')
        w('|---|---|---|---|---|')
        acodes = split_list(r['codes'])
        full = []
        for c in acodes:
            full.append(c)
            full.extend(k for k in children(c) if k not in acodes)
        for c in full:
            txt = clean(std.get(c, ''))
            if len(c) > 1 and c[-1].islower() and c[:-1] in full:
                part = '%s: %s' % (c[-1], txt)
            else:
                part = txt or ('whole indicator (verb from the C3 file)' if ss else
                               'whole expectation (statement not on file; its three dimensions are in the field 2 table)' if subj == 'science'
                               else 'whole standard')
            w('| %s | %s | %s | %s | section %s |' % (r['day'], c, part, MARK, r['unit']))
        w('')
    if not ass:
        w('days.csv marks no end-of-unit assessment day in this unit.')
        w('')
    w('%s: Teacher-judged items: look-fors, and two sample answers (one that meets them, one that does not). One line on accommodations.' % MARK)
    w('')

    # ---- field 6: error register
    w('## 6. Error register')
    w('')
    w('| | The error or first idea | What it shows | Source |')
    w('|---|---|---|---|')
    w('| A | %s | | |' % MARK)
    w('')
    w('%s: Errors and first ideas (misconceptions), lettered once for the unit, each with what it shows and its source or "from memory".' % MARK)
    w('')

    # ---- field 7: response allocation
    w('## 7. Response allocation')
    w('')
    resp = [r for r in rows if r['kind'] == 'Respond']
    if resp:
        w('- **Respond days (days.csv):** %s.' % '; '.join('day %s' % r['day'] for r in resp))
    else:
        w('- **Respond days (days.csv):** none in this unit.')
    for r in rows:
        if r['assess'] == 'readiness' or re.search(r"(unit %d's|next unit's) readiness" % (unit + 1), r['note'], re.I):
            w("- **Next unit's readiness check:** the last ten minutes of day %s (%s)." % (r['day'], r['kind']))
    if frame_meta.get('minutes_min'):
        lo, hi = frame_meta['minutes_min'], frame_meta['minutes_max']
        w('- **Day length (data/plans/frames.csv):** %s minutes.' % (lo if lo == hi else '%s to %s' % (lo, hi)))
    w('%s: Marking time and response time named separately; whether response sits inside the assessment day or on respond days (count it once); how the assessment is marked; what each error group does; the one-child path.' % MARK)
    w('')

    # ---- field 8
    w('## 8. Tools and supplies across the unit')
    w('')
    if ss:
        w('%s: Tools (each with its day, mark, job, verdict and a link to TOOL-ASKS.md; or "None") and the supplies list. Every map, source and task has a printed version (paper path).' % MARK)
    else:
        W.extend(field8_lines(course, rows, fr))
    w('')

    # ---- field 9
    w('## 9. Family note')
    w('')
    w('%s: One or two sentences for the unit.' % MARK)
    w('')

    # ---- field 10
    w('## 10. Sources and what is still to make')
    w('')
    w(OPEN)
    if ss:
        used = sorted({('data/standards/ma-hss-2018.txt' if c.startswith('MA.') else 'data/standards/c3-indicators.txt'
                        if c.startswith('D') else 'data/standards/ccss-literacy-6-12.txt') for c in codes})
    else:
        used = files_with(codes)
    w('- **Standards files:** %s. **Progression:** data/progressions/%s.csv. **Frame and scope and sequence:** '
      'docs/courses/%s/frame.md, scope-and-sequence.md; days in data/plans/%s/days.csv.' % (', '.join(used), subj, course, course))
    progcodes = uniq(c for s in skills if s in prog for c in split_list(prog[s]['standard']))
    only = [c for c in progcodes if (c if ss else c.lstrip('~')) not in codes]
    if only:
        w('- **Note:** the progression lists %s for these skills, but days.csv does not cite %s.%s'
          % (', '.join(only), 'it' if len(only) == 1 else 'them',
             ' A leading ~ marks a standard the row touches without owning.' if not ss and any(c.startswith('~') for c in only) else ''))
    if fr and fr[8].strip():
        w('- **Check set adds (frame):** %s' % clean(fr[8]))
    sm = [r for r in read_csv(plan_file(course, 'source-map.csv')) if r['unit'].split('.')[0] == str(unit)]
    miss10 = []
    if not ss:
        extra10, miss10 = field10_extras(course, unit)
        W.extend(extra10)
    elif sm:
        w('- **Source map (data/plans/%s/source-map.csv):**' % course)
        for r in sm:
            w('  - %s, %s (our days %s): %s. %s' % (r['source'], clean(r['title']), r['days'], r['decision'], clean(r['why'])))
    sens = [r for r in rows if 'sensitiv' in r['note'].lower()]
    if fr and fr[9].strip():
        w('- **Sensitive topics (frame):** %s' % clean(fr[9]))
    if sens:
        w('- **Days flagged for the sensitivity read (days.csv notes):**')
        for r in sens:
            t = re.sub(r'^sensitivity read \([^)]*\)( with the unit plan)?:?\s*', '', clean(r['note']), flags=re.I)
            w('  - Day %s: %s' % (r['day'], t))
    w(CLOSE)
    if ss:
        w('%s: Sources chosen for the unit (named, with licence and what was read); the primary sources and the community\'s own sources first.' % MARK)
        w('%s: What the sensitivity agent (docs/pipeline/briefs/sensitivity-read.md) must study for this unit, the community\'s own sources first; or one line saying the unit has no cultural, Native, hard-history, faith, health or disability content.' % MARK)
    else:
        for m in miss10:
            w(m)
        src = {'math': 'the base-text lessons used with each credit line, and the Progressions pages read',
               'science': 'the base unit and lessons adapted with each credit line, and public data sets with their rights lines',
               'ela': 'each text with its author, rights line and place in the unit'}[subj]
        w('%s: Sources chosen for the unit (named, with licence and what was read): %s.' % (MARK, src))
        more = {'math': '', 'science': ' Name the hazards and chemicals the safety read checks against published guidance.',
                'ela': ' Name each original text the text agent reads.'}[subj]
        w('%s: What the sensitivity agent (docs/pipeline/briefs/sensitivity-read.md) must study for this unit, the community\'s own sources first; '
          'or one line saying the unit has no cultural, Native, hard-history, faith, health or disability content.%s' % (MARK, more))
    w('%s: What was not seen, and what is still to make. Mark anything written from memory "from memory".' % MARK)
    w('')

    # ---- day list (generated table)
    w('## Day list (from days.csv, do not edit)')
    w('')
    w('| Day | School day | Kind | Goal | Codes | Note |')
    w('|---|---|---|---|---|---|')
    for r in rows:
        d = int(r['day'])
        if r.get('school_day'):
            sdv = r['school_day']
        else:
            sdv = ''
            for cr in cal:
                if int(cr['first_day']) <= d <= int(cr['last_day']):
                    sdv = str(int(cr['first_school_day']) + d - int(cr['first_day']))
        w('| %d | %s | %s | %s | %s | %s |' % (d, sdv, r['kind'], clean(r['goal']), '; '.join(split_list(r['codes'])), clean(r['note'])))
    w('')
    return '\n'.join(W)


def main(a):
    force = '--force' in a
    out = None
    if '--out' in a:
        i = a.index('--out')
        out = Path(a[i + 1])
        a = a[:i] + a[i + 2:]
    if '--data-dir' in a:
        i = a.index('--data-dir')
        set_data_dir(a[i + 1])
        a = a[:i] + a[i + 2:]
    a = [x for x in a if x != '--force']
    if a[:1] == ['--list'] and len(a) <= 2:
        subj = a[1] if len(a) == 2 else None
        if subj and subj not in SUBJECTS:
            raise SystemExit('subject must be one of: %s' % ', '.join(SUBJECTS))
        for c in courses_of(subj):
            set_subject(subject_of(c))
            n = len(unit_numbers(c))
            print('%-48s %d units' % (c, n) + ('' if n else ' (no days.csv yet)'))
        return 0
    if not a:
        raise SystemExit(__doc__)
    course = a[0]
    if subject_of(course) is None:
        raise SystemExit('not a course in data/plans/frames.csv: %s' % course)
    set_subject(subject_of(course))
    if not unit_numbers(course):
        raise SystemExit('%s has no days.csv yet (its scope and sequence comes first, PRODUCTION-PATH step 5)' % course)
    units = unit_numbers(course)
    if len(a) > 1:
        units = [int(a[1])]
    folder = (out / course) if out else (DOCS / course)
    folder.mkdir(parents=True, exist_ok=True)
    rc = 0
    for u in units:
        p = folder / ('s%02d.md' % u)
        if p.exists() and not force:
            print('exists, kept:', p)
            rc = rc or 0
            continue
        text = build(course, u)
        p.write_text(text, encoding='utf-8', newline='\n')
        print('wrote', p, '(%d TODO)' % text.count(MARK))
    return rc


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

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

Writes the skeleton to docs/courses/<course>/unit-skeletons/s{uu}.md (an ignored working file, always rebuilt; it is
the writer's read view of the facts) in the shape of docs/courses/UNIT-PLAN.md (the unit plan, fields 1 to 10; the
section plans follow later, PRODUCTION-PATH step 7). When the plan docs/courses/<course>/s{uu}.md does not exist yet,
it also writes the starter plan: the skeleton with its fact blocks taken out (headings and writer markers only). A
written plan is never touched: its facts render from data (scripts/plan_facts.py, consolidation 4.E2); --force is
accepted and changes nothing. Lettered parts: a choice standard (is_choice:
"one of", "from the list", "research one", parts marked "option:") owes no part, one option in depth and the rest
surveyed; when days.csv cites parts of a code, a unit owes only the parts it cites; a "such as" list gives examples,
never required parts (structure pass 2026-11-14). --out DIR
writes under DIR/<course>/ instead (for tests). Output is deterministic: same data, same bytes.

Filled from: data/plans/<course>/days.csv (days, kinds, goals, codes, assessment days, notes), data/plans/calendar.csv
(school days, weeks), data/progressions/social-studies.csv (skills, what they assume and hand on), the standards files
in data/standards/ (own-word lines and lettered parts), docs/courses/<course>/frame.md (unit title, compelling
question, models carried, check set, sensitive topics) and data/plans/<course>/source-map.csv where it exists.

Math adds: cluster weights (data/standards/ccss-math-focus.csv), the frame's practices, tools and supplies named in
day notes (or in tools/supplies columns and materials.csv where they exist), base-text lesson rows from source-map.csv.
ELA adds: the frame's text set, owned codes grouped by strand with the days they are taught (kind Understanding) and
practiced (other kinds), writing types and writing days, base-text rows. Science adds: the anchoring phenomenon, the
frame's practices and crosscutting concepts, a three-dimensions table (one row per performance expectation, filled from
data/standards/ngss-pe-dimensions.csv with the expectation lines, limits and emphases), safety and materials notes from
the days.csv tools, supplies and safety columns, day notes and the frame, base-text rows. ELA text rows come from
data/plans/ela-texts.csv (the word list is asked of the writer as data/plans/<course>/wordlist.csv). Math weights include
`plus` (advanced (+) standards, outside the weighted set). Unit 1's readiness check is the last ten minutes of day 1
(lead rule 2026-11-14); with no readiness rows the unit says "Start-of-year check: none needed; retrieval only".

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


class DataError(SystemExit):
    """A data file the skeleton cannot use: the message names the file (and line) and what is wrong. A SystemExit, so
    the command line prints the message, never a traceback; scripts/unitplan.py and codex_units.py catch it."""


def shown_path(path):
    try:
        return Path(path).resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return Path(path).as_posix()


def read_csv(path, need=None):
    """Rows of a CSV file ([] when it does not exist). With need (a list of column names), the header must hold every
    one of them and every row must have as many cells as the header, or DataError names the file, the line, the
    columns it has and the columns it needs. Lines that start with # are skipped when need is given."""
    if not Path(path).exists():
        return []
    with io.open(path, encoding='utf-8', newline='') as f:
        if need is None:
            return list(csv.DictReader(f))
        rd = csv.DictReader(l for l in f if not l.startswith('#'))
        head = rd.fieldnames or []
        miss = [c for c in need if c not in head]
        if miss:
            raise DataError('%s: has columns %s; needs %s (missing: %s)'
                            % (shown_path(path), ','.join(head) or '(none)', ','.join(need), ','.join(miss)))
        rows = []
        for r in rd:
            if None in r or any(r[c] is None for c in need):
                n = len([k for k, v in r.items() if k is not None and v is not None]) + len(r.get(None) or [])
                raise DataError('%s: data row %d has %d cells, the header has %d (%s)'
                                % (shown_path(path), len(rows) + 1, n, len(head), ','.join(head)))
            rows.append(r)
        return rows


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
    rows = read_csv(PLANS / 'frames.csv', FRAMES_COLS)
    if subject:
        return [r['course'] for r in rows if r['subject'] == subject]
    return [r['course'] for s in SUBJECTS for r in rows if r['subject'] == s]


def subject_of(course):
    for r in read_csv(PLANS / 'frames.csv', FRAMES_COLS):
        if r['course'] == course:
            return r['subject']
    return None


def ss_courses():
    """The social studies course ids, in data/plans/frames.csv order."""
    return courses_of('social-studies')


FRAMES_COLS = ['course', 'subject', 'grade', 'title', 'minutes_min', 'minutes_max']
DAYS_COLS = ['day', 'stretch', 'unit', 'kind', 'goal', 'skills', 'codes', 'assess', 'note']   # sequence-write.md "The files"
# The one source-map layout (sequence-write.md rule 8; the same list as MAP_COLS in scripts/sequence.py, which gates it).
MAP_COLS = ['source', 'title', 'goals', 'standards', 'unit', 'days', 'decision', 'why', 'order_conflict', 'harms_learning']


def days_rows(course):
    """data/plans/<course>/days.csv; DataError when a column of DAYS_COLS is missing, a row is short, or a day is not a
    whole number."""
    p = plan_file(course, 'days.csv')
    rows = read_csv(p, DAYS_COLS)
    for i, r in enumerate(rows, 1):
        if not r['day'].strip().isdigit():
            raise DataError('%s: data row %d: day "%s" is not a whole number' % (shown_path(p), i, r['day']))
    return rows


def unit_numbers(course):
    return sorted({int(r['stretch']) for r in days_rows(course) if r['stretch'].isdigit()})


def unit_days(course, unit):
    return [r for r in days_rows(course) if r['stretch'] == str(unit)]


def split_list(s):
    # a career cluster code ("CTE.Career Clusters.Arts, Entertainment, & Design...") holds commas: a piece that
    # starts with CTE. stays whole (career pathways read, 2026-11-25)
    out = []
    for piece in (s or '').split(';'):
        if piece.strip().lstrip('~').startswith('CTE.'):
            out.append(piece.strip())
        else:
            out += [x.strip() for x in re.split(r'\s*,\s*', piece) if x.strip()]
    return out


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


# A choice standard: its lettered parts are options, one studied in depth and the rest surveyed, never each a required
# part ("one of", "from the list", "research one ...", or parts that say "option:"). "one another" is not a choice.
CHOICE_PARENT = re.compile(r'\bone of\b|\bfrom the list\b|\bchoosing one\b|\b(?:research|report on|analy[sz]e|in|map)\s+'
                           r'(?:the causes and course of\s+)?one\b(?!\s+another)', re.I)
CHOICE_CHILD = re.compile(r'\boption:|\bas an example agency\b', re.I)


def is_choice(code):
    """True for a standard whose lettered parts are options to choose among (see CHOICE_PARENT)."""
    kids = children(code)
    if not kids:
        return False
    std = std_text()
    return bool(CHOICE_PARENT.search(std.get(code, ''))) or any(CHOICE_CHILD.search(std.get(k, '')) for k in kids)


def parts_of(code, rows=None, allrows=None):
    """Lettered parts a unit owes for a code. When the course's days.csv cites any part of the code itself (the parts
    are assigned to units), a unit owes only the parts its own rows cite. Otherwise a choice standard owes none (one
    option in depth, the rest surveyed) and any other standard owes every part. Without allrows, every part (or none
    for a choice standard)."""
    kids = children(code)
    if not kids:
        return []
    if allrows is not None and rows is not None:
        cited = {c for r in allrows for c in split_list(r['codes'])}
        if any(k in cited for k in kids):
            mine = {c for r in rows for c in split_list(r['codes'])}
            return [k for k in kids if k in mine]
    return [] if is_choice(code) else kids


def required_codes(rows, allrows=None):
    """Codes a unit must carry: every code in its days.csv rows, in first-seen order, each followed by the lettered
    parts it owes (parts_of) that days.csv does not itself list."""
    seen, out = set(), []
    for r in rows:
        for c in split_list(r['codes']):
            if c not in seen:
                seen.add(c)
                out.append(c)
    for c in list(out):
        for ch in parts_of(c, rows, allrows):
            if ch not in seen:
                seen.add(ch)
                out.append(ch)
    return out


def days_codes_order(rows, allrows=None):
    """days.csv codes in first-seen order, with each code's lettered parts placed right after it."""
    out = []
    for c in required_codes(rows, allrows):
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


def frame_skill_units(course):
    """skill -> the first frame unit whose Skills cell lists it (cold reads 2026-11-24: owned comes from the frame)."""
    out = {}
    for cells in table_rows(frame_lines(course), '| # | Unit and compelling question'):
        if cells and cells[0].isdigit() and len(cells) >= 10:
            for s in split_list(cells[3].replace('`', '')):
                out.setdefault(s.lstrip('~'), int(cells[0]))
    return out


def frame_models(course, unit):
    """(model, how) for each model of the frame's Models carried table that names this unit."""
    rows = table_rows(frame_lines(course), '| Model |')
    out = []
    pat = re.compile(r'unit %d(?!\d)' % unit, re.I)
    for cells in rows:
        if len(cells) < 4:
            continue
        if not is_ss():
            nums = unit_nums(cells[2])
            if unit in nums and unit != min(nums):
                # the cell names an earlier unit of this course first (science 7 food-web: unit 3 checks, unit 4 retrieves)
                out.append((cells[0], 'used again here (first used in unit %d): %s' % (min(nums), cells[2])))
            elif unit in nums and re.search(r'reactivat|revisit|retriev', cells[2], re.I):
                out.append((cells[0], 'reactivated here (from an earlier grade: %s): %s' % (cells[1], cells[2])))
            elif unit in nums:
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


CAL_COLS = ['course', 'kind', 'unit', 'first_day', 'last_day', 'first_school_day', 'last_school_day', 'first_week', 'last_week']


def calendar_rows(course, unit):
    p = (DATA_DIR or PLANS) / 'calendar.csv'
    out = [r for r in read_csv(p, CAL_COLS) if r['course'] == course and r['kind'] == 'unit' and r['unit'] == str(unit)]
    for r in out:
        for c in ('first_day', 'last_day', 'first_school_day', 'last_school_day'):
            if not r[c].strip().isdigit():
                raise DataError('%s: the row for %s unit %s: %s "%s" is not a whole number' % (shown_path(p), course, unit, c, r[c]))
    return out


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
    """'26 to 38 and 55' (or '34, 58, 94 and 102 to 120') for the header; the checker parses both shapes."""
    parts = [('%d to %d' % r) if r[0] != r[1] else str(r[0]) for r in runs(nums)]
    if len(parts) < 3:
        return ' and '.join(parts)
    return '%s and %s' % (', '.join(parts[:-1]), parts[-1])


PROG_COLS = ['grade', 'skill_id', 'standard', 'assumes', 'hands_on', 'cross_subject']


def progression():
    return {r['skill_id']: r for r in read_csv(PROGS / (SUBJ + '.csv'), PROG_COLS)}


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
# Safety words in notes (science field 8). "chemical" is left out: "chemical change" and "chemical reaction" name content,
# not a hazard (spot check 2026-11-15).
SAFEWORDS = re.compile(r'\b(safety|goggles?|eye protection|gloves|hazard\w*|flame|heat\w*|allerg\w*|sharp|'
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
    if re.fullmatch(r'\s*\d+(?:\s*(?:,|and|to)\s*\d+)*\s*\.?\s*', text):   # a bare list ('2, 4, 7'): the Units column
        text = 'Units ' + text
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
    if not is_ss():
        # every shape the four subjects' frames use (spot check 2026-11-15: italic, quoted after a "?" title, "Title:
        # Question?", "**Title** (weeks ...)"); social studies keeps split_title, its output is frozen
        return split_science_cell(cell)
    t, q = split_title(cell)
    return t, q, ''


def _sentences(text):
    return [x.strip() for x in re.split(r'(?<=[.?])\s+(?=[A-Z*"])', text.strip()) if x.strip()]


def _plain(x):
    return re.sub(r'\s+', ' ', x.replace('**', '').replace('*', '')).strip().strip('"').strip()


def split_science_cell(cell):
    """(title, question, anchor) from a science frame cell in any of its shapes: K to 2 'Title. *Question?* Anchor: ...',
    grades 3 to 5 'Title. "Question?" Anchor: ...', grades 6 to 8 'Title. Question? Anchor: ...', high school
    '**Title** (weeks 1 to 3). Anchor: ... Question?' (question last) or '... Design problem: ... Question? Anchor: ...'.
    The question and the anchor are kept apart; a 'Design problem:' sentence joins the front of the anchor."""
    cell = cell.strip()
    head = ''
    mh = re.match(r'\*\*(.+?)\*\*\s*(?:\((?:weeks?|about) [^)]*\))?\.?\s*', cell)
    if mh:                      # high school: '**Title** (weeks 1 to 3).' leads the cell
        head, cell = mh.group(1).strip(), cell[mh.end():].strip()
    ms = list(re.finditer(r'(?<![A-Za-z])Anchor:\s*', cell))
    if ms:
        before, tail = cell[:ms[-1].start()].strip(), cell[ms[-1].end():].strip()
    else:
        before, tail = cell, ''
    design, title, question = [], '', ''
    mq = re.search(r'\*([^*]+\?)\*|"([^"]+\?)"', before)
    if mq:
        question = (mq.group(1) or mq.group(2)).strip()
        title = before[:mq.start()].strip()
        mid = before[mq.end():].strip()
        if re.match(r'Design (problem|question):', mid):
            design.append(mid)
    else:
        # a question may close with a bracketed aside: 'What do the sources say? (each student's own question)'
        sents = [re.sub(r'(?<=\?)\s+\(.*$', '', x) for x in _sentences(before)]
        qi = max((i for i, x in enumerate(sents) if x.endswith('?')), default=None)
        if qi is not None:
            question = sents[qi]
            title = sents[0] if qi > 0 else ''
            mc = re.match(r'^([^?:]{2,80}):\s+(.+\?)$', question) if qi == 0 else None
            if mc and not re.match(r'Design (problem|question)', mc.group(1)):   # 'Similarity: How can ...?'
                title, question = mc.group(1), mc.group(2)
            design = [x for x in sents[1:] if sents.index(x) != qi and re.match(r'Design (problem|question):', x)]
        else:
            tsents = _sentences(tail)
            qi = max((i for i, x in enumerate(tsents) if x.endswith('?')), default=None)
            title = before
            if qi is not None:
                question = tsents[qi]
                tail = ' '.join(x for i, x in enumerate(tsents) if i != qi)
    if not question and not tail:
        t, q = split_title(cell)
        return head or t, q, ''
    if head:
        title = head
    title = re.sub(r'\s*\(weeks? [^)]*\)', '', _plain(title)).rstrip('.').strip()
    # a design sentence that runs into "Anchor:" with no full stop still ends as a sentence (science K unit 3)
    design = [x if re.search(r'[.?!]$', x) else x + '.' for x in design]
    anchor = ' '.join(design + ([('Anchor: ' if design else '') + tail] if tail else [])).strip()
    return title or cell, _plain(question), anchor


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
    """(taught, practiced) day numbers where days.csv names the code or one of its lettered parts. Taught: kind
    Understanding; practiced: every other kind."""
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
    meta = next((r for r in read_csv(PLANS / 'frames.csv', FRAMES_COLS) if r['course'] == course), {})
    g = meta.get('grade', '')
    if SUBJ == 'math':
        return 'Illustrative Mathematics K-12 (CC BY 4.0)'
    if SUBJ == 'science' and g in ('6', '7', '8'):
        return 'OpenSciEd Middle School (CC BY 4.0)'
    if SUBJ == 'ela' and g in ('K', '1', '2', '3', '4', '5'):
        return 'EL Education K-5, 2017 (CC BY 4.0)'
    return ''


def source_map(course):
    """All rows of data/plans/<course>/source-map.csv ([] when there is none). A map not in the one layout (MAP_COLS)
    stops the skeleton with DataError naming the file, the columns it has and the columns it needs: a plan written
    against an unconverted map would lose its base-text lines, so it is not written at all."""
    try:
        return read_csv(plan_file(course, 'source-map.csv'), MAP_COLS)
    except DataError as e:
        raise DataError('%s. The source map is not yet in the one layout of sequence-write.md rule 8; convert it first.' % e)


def source_rows(course, unit):
    return [r for r in source_map(course) if r['unit'].strip().split('.')[0] == str(unit)]


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
WEIGHTWORD = {'major': 'major', 'supporting': 'supporting', 'additional': 'additional', 'wap': 'prerequisite', 'plus': 'plus'}
PLUSNOTE = 'plus means advanced (+) standards, outside the weighted set'
WAPNOTE = ('prerequisite means "wap" in the focus file, a widely applicable prerequisite: a high school cluster that later '
           'courses lean on, still this course\'s own content')

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
        'supq': '',     # the question board is asked once, in the Storyline line (spot check 2026-11-15)
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


_DIMS = {}
_ELA = {}


def pe_dims():
    """pe -> dimension -> [rows], from data/standards/ngss-pe-dimensions.csv (own-word lines only, as stored)."""
    if not _DIMS:
        p = STD / 'ngss-pe-dimensions.csv'
        if p.exists():
            lines = [ln for ln in io.open(p, encoding='utf-8') if ln.strip() and not ln.startswith('#')]
            for r in csv.DictReader(lines):
                _DIMS.setdefault(r['pe'], {}).setdefault(r['dimension'], []).append(r)
    return _DIMS


def pe_statement(code):
    """The stored own-word expectation line for a science code ('' when none)."""
    rows = pe_dims().get(code, {}).get('statement', [])
    return clean(rows[0]['element']) if rows else ''


def pe_limit_lines(code):
    """' Emphasis: ... Limit: ...' from the clarification and boundary rows ('' when none)."""
    d = pe_dims().get(code, {})
    out = ''
    if d.get('clarification'):
        txt = ' '.join(clean(r['element']) for r in d['clarification'])
        out += ' ' + (txt if txt.startswith('Emphasis:') else 'Emphasis: ' + txt)
    if d.get('boundary'):
        out += ' Limit: %s' % ' '.join(clean(r['element']) for r in d['boundary'])
    return out


def std_line(code):
    """The own-word line for a code: the stored expectation statement for science, else the standards file line."""
    if SUBJ == 'science' and is_pe(code):
        t = pe_statement(code)
        if t:
            return t
    return std_text().get(code, '')


def pe_row(code):
    """The three-dimensions table row for one expectation, cells filled from the stored rows."""
    d = pe_dims().get(code)
    if not d:
        return '| %s | %s: no rows in data/standards/ngss-pe-dimensions.csv (missing data) | %s | %s |' % (code, MARK, MARK, MARK)

    def join(rows, fmt):
        t = '; '.join(fmt(r).strip().rstrip('.') for r in rows)
        return clean(t + '.') if t else ''
    sep = join(d.get('sep', []), lambda r: '%s: %s' % (r['name'], r['element'])) or MARK + ': no practice on file'
    dci = join(d.get('dci', []), lambda r: '%s %s%s: %s' % (r['code'], r['name'], ' (secondary)' if r.get('role') == 'secondary' else '', r['element'])) \
        or MARK + ': no core idea on file'
    ccc = join(d.get('ccc', []), lambda r: '%s: %s' % (r['name'], r['element']))
    if not ccc:
        names = [r['name'] for r in d.get('eta', []) + d.get('nos', [])]
        ccc = clean('; '.join('%s (connection, no crosscutting concept)' % n for n in names))
        if not ccc and 'ETS' in code:
            # the standards list none for some engineering expectations (K-2-ETS1-1): say so, never invent one
            ccc = 'None listed for this engineering expectation; use the unit\'s focal crosscutting concept (frame, C3 column, above).'
        ccc = ccc or MARK + ': no crosscutting concept on file'
    return '| %s | %s | %s | %s |' % (code, sep, dci, ccc)


def pe_connections(code):
    d = pe_dims().get(code, {})
    rows = d.get('eta', []) + d.get('nos', [])
    return '; '.join('%s: %s' % (clean(r['name']), clean(r['element'])) for r in rows)


ELA_COLS = ['course', 'unit', 'text_id', 'title', 'author', 'year', 'kind', 'use', 'part', 'edition', 'measure', 'demands',
            'status', 'rights_basis']


def ela_rows():
    """All rows of data/plans/ela-texts.csv (under --data-dir, DIR/ela-texts.csv)."""
    key = str(DATA_DIR)
    if _ELA.get('dir') != key:
        p = (DATA_DIR or PLANS) / 'ela-texts.csv'
        if not p.exists():
            p = PLANS / 'ela-texts.csv'     # under --data-dir the real file stands in until the test dir holds its own
        rows = read_csv(p, ELA_COLS)
        _ELA.clear()
        _ELA.update({'dir': key, 'rows': rows})
    return _ELA['rows']


def ela_texts(course, unit):
    """Rows of data/plans/ela-texts.csv for one ELA course and unit."""
    return [r for r in ela_rows() if r['course'] == course and r['unit'] == str(unit)]


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
        for wt in ('major', 'supporting', 'additional', 'wap', 'plus'):
            ks = [k for k, w_, _ in cl if w_ == wt]
            if ks:
                groups.append('%s (%s)' % (WEIGHTWORD[wt], ', '.join(ks)))
        L.append(OPEN)
        L.append('Weight (Student Achievement Partners, data/standards/ccss-math-focus.csv): %s.%s%s'
                 % ('; '.join(groups) or 'none on file', (' In this line ' + PLUSNOTE + '.') if any(w_ == 'plus' for _, w_, _ in cl) else '',
                    (' In this line ' + WAPNOTE + '.') if any(w_ == 'wap' for _, w_, _ in cl) else ''))
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
        L.append('%s: Fluency: which owned standards set an expected fluency (the frame\'s fluency note) and how it is built without time pressure (a timer only with a grounded purpose, BASELINE rule 30), or one line saying the unit sets none.' % MARK)
    elif SUBJ == 'ela':
        L.append(OPEN)
        trows = ela_texts(course, unit)
        if trows:
            L.append('- **Text set (data/plans/ela-texts.csv, %d rows for this course and unit; use is anchor, paired or independent):**' % len(trows))
            for t in trows:
                L.append('  - %s (%s): %s, %s%s; %s, %s; status: %s; edition: %s; rights: %s'
                         % (t['text_id'], t['use'] or 'use not stated', clean(t['title']), clean(t['author']) or 'author not stated',
                            ' (%s)' % t['year'] if t['year'].strip() else '', t['part'] or 'part not stated', t['kind'] or 'kind not stated', t['status'],
                            clean(t['edition']) or 'not stated', clean(t['rights_basis']) or 'not stated'))
        else:
            if c3:
                L.append('- **Text set (frame, C3 column):** %s' % c3)
            L.append('- **Text records:** no rows in data/plans/ela-texts.csv for this course and unit.')
        L.append('- **Owned codes by strand (days.csv: taught = days of kind Understanding, practiced = days of any other kind):**')
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
                parts.append('%s (taught: %s; practiced: %s)' % (c, days_or_none(t), days_or_none(p)))
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
        wl = [int(r['day']) for r in rows if WRITEWORDS.search(r['goal'])]
        if wl:
            L.append('- **Days whose goal names writing (goals in the day list):** %s.' % runs_text(wl))
        anchors = [t for t in trows if t['use'] == 'anchor']
        if anchors:
            L.append('- **Text complexity on file (ela-texts.csv, measure and qualitative demands of each anchor):**')
            for t in anchors:
                L.append('  - %s: measure: %s; demands: %s' % (clean(t['title']), clean(t['measure']) or 'not stated', clean(t['demands']) or 'not stated'))
        L.append(CLOSE)
        if trows:
            L.append('%s: Anchor and paired texts: confirm each anchor and paired row above, the day it is read, and fill the rows whose status is to choose or to confirm (name the text, its edition and its part); say which texts you added or dropped. Rights stay as the file has them; where a row says not stated, give the basis you know (public domain by date, written by Curio Class, or the licence) and list the row under "For the lead".' % MARK)
            L.append('%s: Text complexity: for each anchor, the reader and task and the support (the measure and the qualitative demands are on file above); correct a demand that is wrong.' % MARK)
        else:
            L.append('%s: Anchor and paired texts: no rows in data/plans/ela-texts.csv for this course and unit; name each anchor and paired text, the day it is read, and its rights line.' % MARK)
            L.append('%s: Text complexity: for each anchor, the measure where usable, the qualitative demands, the reader and task, and the support, in a line each.' % MARK)
        L.append('%s: Word list: draw about 8 to 10 words a week from this unit\'s texts, met before, during and after reading, and write them to data/plans/%s/wordlist.csv (unit, word, text_id, week, when).' % (MARK, course))
        L.append('%s: Main piece of writing: its type, the process (plan, draft, revise, edit, publish) or on-demand, the day it is assigned and the day it is finished; and the writing tasks above that are short pieces.' % MARK)
        L.append('%s: Taught versus practiced: check the split above against the unit\'s goals and say which owned codes the unit teaches and which it only practises.' % MARK)
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
            L.append('')
            L.append('Three dimensions of each performance expectation (names and own-word lines from data/standards/ngss-pe-dimensions.csv; the Next Generation Science Standards are never named in student, teacher or family copy):')
            L.append('')
            L.append(OPEN)
            L.append('| Performance expectation | Science and engineering practice | Core idea | Crosscutting concept |')
            L.append('|---|---|---|---|')
            for c in pes:
                L.append(pe_row(c))
            L.append(CLOSE)
            conn = [(c, pe_connections(c)) for c in pes if pe_connections(c)]
            if conn:
                L.append(OPEN)
                L.append('- **Connections (engineering and nature of science, same file):**')
                for c, t in conn:
                    L.append('  - %s: %s' % (c, t))
                L.append(CLOSE)
            L.append('')
        L.append('%s: Storyline: the question board (what students notice and wonder from the phenomenon, grouped, with the day each question is answered) and the unseen phenomenon the end-of-unit assessment uses. The model\'s path (initial, revisions, consensus) goes under Carried, once.' % MARK)
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


def note_days(rows, rx, skip=None, goal_too=True):
    """Day numbers whose note (or goal) matches rx, less those whose note matches skip."""
    out = []
    for r in rows:
        note, goal = clean(r['note']), (clean(r['goal']) if goal_too else '')
        if (rx.search(note) or rx.search(goal)) and not (skip is not None and skip.search(note)):
            out.append(int(r['day']))
    return out


def grouped_lines(rows, only=None, skip=None):
    """The optional tools, supplies and safety columns of days.csv, one line per item with the days it appears (an item
    repeated on many days is printed once)."""
    out = []
    for col in TOOLCOLS:
        if (only and col not in only) or (skip and col in skip):
            continue
        if rows and col in rows[0]:
            for it, ds in group_column(rows, col):
                out.append('  - %s: %s (day%s %s)' % (col, clean(it), 's' if len(ds) > 1 else '', runs_text(ds)))
    return out


def field8_lines(course, rows, fr):
    """Field 8 for math, ELA and science: the days.csv columns grouped by item, and the day numbers whose notes or goals
    name tools or safety (the notes themselves are in the day list, not copied here)."""
    L = [OPEN]
    if SUBJ == 'science':
        nd = note_days(rows, TOOLWORDS, skip=SAFEWORDS)
        L.append('- **Materials and tools named in days.csv (tools and supplies columns, by item):**')
        L.extend(grouped_lines(rows, skip=('safety',)) or ['  - none in the columns'])
        if nd:
            L.append('- **Days whose notes or goals name tools or materials (see the day list):** %s.' % runs_text(nd))
        sd = note_days(rows, SAFEWORDS, goal_too=False)
        L.append('- **Safety named in days.csv (safety column, by hazard):**')
        L.extend(grouped_lines(rows, only=('safety',)) or ['  - none in the column'])
        if sd:
            L.append('- **Days whose notes name safety (see the day list):** %s.' % runs_text(sd))
        if fr and fr[9].strip():
            L.append('- **Safety and teacher notes (frame):** in field 10, under "Sensitive topics and teacher notes (frame)".')
    else:
        items = grouped_lines(rows)
        nd = note_days(rows, TOOLWORDS)
        L.append('- **Tools and supplies named in days.csv (columns, by item; then notes and goals):**')
        L.extend(items)
        if nd:
            L.append('  - Days whose notes or goals name tools or supplies (see the day list): %s.' % runs_text(nd))
        if not items and not nd:
            L.append('  - none named')
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


def has_order_conflict(value):
    """True when a source-map order_conflict cell records a real conflict. Empty cells and the no-conflict prose
    some courses keep there ("None; lesson order retained.", "Source order kept; ...", "No source lesson ...") are
    not conflicts (ELA structure pass 2026-11-24)."""
    v = value.strip().lower()
    return bool(v) and not v.startswith(('none', 'no ', 'no;', 'no,', 'source order kept'))


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
            # one line per row (spot check 2026-11-15, bulk): goals, standards and why stay in source-map.csv
            L.append('  - %s, %s: our days %s; %s%s'
                     % (r['source'], clean(r['title']), r['days'] or 'none', r['decision'],
                        '; order conflict' if has_order_conflict(r.get('order_conflict', '')) else ''))
        L.append('- **Source-map decisions in this unit:** %s. Goals, standards, the reason for each decision and any order '
                 'conflict are in the file.' % ', '.join('%s %d' % (k, v) for k, v in sorted(count.items())))
    elif base:
        L.append('- **Base text:** %s; data/plans/%s/source-map.csv has no rows for unit %d.' % (base, course, unit))
        miss.append('%s: Base text lessons used: data/plans/%s/source-map.csv has no rows for this unit (missing data; it comes with the scope and sequence, sequence-write.md rule 8); list the lessons, their days and decisions.' % (MARK, course))
    return L, miss


def note_clauses(note):
    """Clauses of a days.csv note: split at a full stop or a semicolon that sits outside brackets. A clause that ends a
    sentence keeps its full stop."""
    out, depth, cur = [], 0, ''
    for i, ch in enumerate(note):
        cur += ch
        if ch in '([':
            depth += 1
        elif ch in ')]':
            depth = max(0, depth - 1)
        elif depth == 0 and ch == ';':
            out.append(cur[:-1])
            cur = ''
        elif depth == 0 and ch == '.' and (i + 1 == len(note) or note[i + 1].isspace()):
            out.append(cur)
            cur = ''
    if cur.strip():
        out.append(cur)
    return [c.strip() for c in out if c.strip()]


def retrieval_clauses(note, day, broad=False):
    """The retrieval tasks a day's note sets: the whole sentence or clause, not a forward mention such as "opens as a
    retrieval task on day 27" (a clause that does not begin with the words and names another day). Social studies
    notes say "retrieval task"; with broad (math, ELA, science) any form of the word counts ("Retrieve s2-compare-designs",
    "retrieval of unit 1")."""
    out = []
    for c in note_clauses(note):
        m = re.search(r'\bretriev\w*' if broad else r'retrieval tasks?\b', c, re.I)
        if not m:
            continue
        if m.start() == 0:
            out.append(c)
            continue
        other = [int(x) for x in re.findall(r'retrieval tasks? on day (\d+)', c, re.I) if int(x) != day]
        if not other:
            out.append(c[m.start():])
    return out


# Math, ELA and science retrieval tasks (spot check 2026-11-15, finding 3): the whole clause, never a fragment cut at the
# word; a clause with no row id, unit, grade or day reference is a routine, a rule or a minute budget, not a task; a
# clause that only reviews days of the same unit is review, not retrieval; "for unit N" belongs to unit N.
IDTOK = re.compile(r'\b[a-z0-9]+(?:-[a-z0-9]+)+\b')
REFWORDS = re.compile(r'\b(?:units?|grades?)\s+(?:\d+|K)\b|\bkindergarten\b|\b(?:Biology|Chemistry|Physics|Algebra I+|Geometry)\b')
NOT_TASK = re.compile(r'\b(?:instead of|replacing|replaces)\b[^.;]{0,40}$', re.I)
FOR_UNIT = re.compile(r'\bfor (?:unit (\d+)|the next unit)\b|\bnext unit\'s\b', re.I)


def ids_in(text, prog):
    """Progression row ids named in a text, in order."""
    return uniq(t for t in IDTOK.findall(text) if t in prog)


def day_nums(text):
    """The course days a text names ('days 43, 45 and 48', 'days 53 to 54', 'day 51')."""
    out = set()
    for m in re.finditer(r'\bdays?\s+(\d+(?:\s*(?:,|and|to)\s*\d+)*)', text, re.I):
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


def task_clauses(note, day, prog, first):
    """The retrieval tasks of one math, ELA or science note (see IDTOK above): whole clauses that name a row id, a unit,
    a grade or a day outside the unit; "Refresh <row id>" counts too (science 4 day 18)."""
    out = []
    for c in note_clauses(note):
        ids = ids_in(c, prog)
        m = re.search(r'\bretriev\w*', c, re.I)
        if not m:
            if ids and re.search(r'\brefresh\w*', c, re.I):
                out.append(c)
            continue
        if NOT_TASK.search(c[:m.start()]):
            continue        # 'instead of ordinary mixed retrieval': the task named elsewhere
        if re.search(r'\bnever\b', c, re.I) and not ids:
            continue        # a rule ('Retrieval openings never count as assessment evidence')
        if any(int(x) != day for x in re.findall(r'retriev\w*(?:\s+tasks?)?\s+on\s+day\s+(\d+)', c, re.I)):
            continue        # a mention of a task on another day
        words = REFWORDS.search(c)
        days = day_nums(c)
        if not ids and not words and not days:
            continue        # no reference: a routine or a minute budget
        if not ids and not words and all(first <= d <= day for d in days):
            continue        # review of this unit's own days
        out.append(c)
    return out


def unit_tasks(rows, allrows, unit, prog):
    """[(day, clause)] retrieval tasks of a math, ELA or science unit: its own days' task clauses less those for another
    unit, plus the clauses of the up to three days before it (its readiness window) that are for it. A clause that names
    only row ids of the next unit, on the unit's last days, is the next unit's (ELA 7 day 86)."""
    byday = {int(r['day']): r for r in allrows}
    first, last = int(rows[0]['day']), int(rows[-1]['day'])

    def rel(u):
        sk = {s for r in allrows if r['stretch'] == str(u) for s in split_list(r['skills'])}
        return sk | {a for s in sk if s in prog for a in split_list(prog[s].get('assumes', ''))}
    me, nxt, prv = rel(unit), rel(unit + 1), rel(unit - 1)
    out = []
    for r in rows:
        d = int(r['day'])
        for c in task_clauses(r['note'], d, prog, first):
            m = FOR_UNIT.search(c)
            if m and (int(m.group(1)) if m.group(1) else unit + 1) != unit:
                continue
            ids = set(ids_in(c, prog))
            if not m and d > last - 3 and ids and not ids & me and ids & nxt:
                continue
            out.append((d, c))
    for k in range(1, 4):
        p = byday.get(first - k)
        if p is None or p['stretch'] not in (str(unit - 1), 'C'):
            break
        pd = int(p['day'])
        pfirst = min(int(r['day']) for r in allrows if r['stretch'] == p['stretch'])
        for c in task_clauses(p['note'], pd, prog, pfirst):
            m = FOR_UNIT.search(c)
            ids = set(ids_in(c, prog))
            if (m and (int(m.group(1)) if m.group(1) else unit) == unit) or (not m and ids and not ids & prv and ids & me):
                out.append((pd, c))
    return sorted(out, key=lambda x: x[0])


def grade_num(g):
    g = str(g or '').strip()
    return 0 if g == 'K' else int(g) if g.isdigit() else None


def year_before(skill, prog, frame_meta):
    """True when the progression row is from the grade just before the course's own (a retrieval task, not readiness)."""
    cg, sg = grade_num(frame_meta.get('grade')), grade_num(prog.get(skill, {}).get('grade'))
    return cg is not None and sg is not None and cg - sg < 2


def earlier_unit_skills(allrows, rows, unit):
    """[(earlier unit number, [skills])] for skills this unit's days cite that earlier units of the course also cite."""
    mine = uniq(s for r in rows for s in split_list(r['skills']))
    out = []
    for u in sorted({int(r['stretch']) for r in allrows if r['stretch'].isdigit() and int(r['stretch']) < unit}):
        theirs = {s for r in allrows if r['stretch'] == str(u) for s in split_list(r['skills'])}
        shared = [s for s in mine if s in theirs]
        if shared:
            out.append((u, shared))
    return out


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


# ---------------------------------------------------------------------------------------------------------------
# Computed checks for math, ELA and science (the faults the scope and sequence reads kept finding, 2026-11-14 and 15).

TEACH_KINDS = ('Understanding', 'Fluency', 'Application')
# Evidence gathered child by child (sequence-write.md rule 2, "Collect once").
EVIDENCE = re.compile(r'one-to-one|one to one|one-on-one|one on one|conferenc\w*|running records?|'
                      r'individual\w* (?:reading|read|interview|record)\w*|small[- ]group', re.I)
REUSE = re.compile(r'\breus\w*', re.I)


def subject_courses():
    """[(grade number, course)] of the current subject, in data/plans/frames.csv order."""
    out = []
    for r in read_csv(PLANS / 'frames.csv', FRAMES_COLS):
        g = grade_num(r['grade'])
        if r['subject'] == SUBJ and g is not None:
            out.append((g, r['course']))
    return out


def used_on(r, skill, course_grade, prog, via=True):
    """True when a days.csv row teaches or assesses a progression row (rule 2: "used" is a day that teaches or assesses
    it): the row is in its skills, the day is not a readiness check, and for a row owned before the course's grade the
    day's note sets no retrieval or readiness task (a retrieval opening or a readiness check is not a use).
    With via (lead, 2026-11-15, after the social studies audit flagged reasoned calls such as grade 7's Roman Republic
    using grade 5's constitution row): a day that teaches a row whose progression `assumes` names the skill uses it too,
    since that row builds directly on it. One hop only."""
    if r['assess'] == 'readiness':
        return False
    own = split_list(r['skills'])
    if skill not in own:
        if not via or not any(skill in split_list(prog.get(s, {}).get('assumes', '')) for s in own):
            return False
        if not is_ss() and (r['kind'] in ('Respond', 'Check') or r['stretch'] == 'C'):
            return False    # a respond, check or course-level day is no one-hop use (spot check 2026-11-15, science 4)
        return not re.search(r'retriev|readiness', r['note'], re.I) or r['kind'] in ('Understanding', 'Application')
    og = grade_num(prog.get(skill, {}).get('grade'))
    if og is not None and course_grade is not None and og < course_grade and re.search(r'retriev|readiness', r['note'], re.I):
        return False
    return True


def earlier_rows(course, rows, allrows, prog, frame_meta, ready_day):
    """One entry per row the unit assumes (the progression's assumes of its skills, less its own skills), each a dict:
    row, owned (grade text), last (where it was last used), rule ('retrieval', 'readiness' or a fault sentence),
    named (where days.csv names it for this unit) and off (a sentence when days.csv and the rule disagree, else '').
    Last use (sequence-write.md rule 2, "Count by grade number"): the highest grade whose days.csv teaches or assesses
    the row, counting this course's days before the unit as this year; with no use on file, the owner grade. A row last
    used the year before or earlier this year gets retrieval; two or more grades back, a readiness check."""
    cg = grade_num(frame_meta.get('grade'))
    first, lastday = int(rows[0]['day']), int(rows[-1]['day'])
    skills = uniq(s for r in rows for s in split_list(r['skills']))
    # Only the unit's own-grade rows bring their assumes (lead, 2026-11-15): an earlier-grade row listed for retrieval
    # (math lead call 4 puts its id in the skills column) is itself an earlier row, not a source of further ones.
    def own(s):
        g = grade_num(prog[s]['grade'])
        return g is None or cg is None or g >= cg
    nss = not is_ss()
    tasks = []
    if nss:
        # Math, ELA, science (spot check 2026-11-15): an earlier-grade row in the skills column is itself an earlier
        # row (it was dropped before, losing geometry's readiness rows); assumes come only from own-grade skills first
        # cited in this unit (a skill an earlier unit already cites is in continuous use, its assumes were met there);
        # an earlier-grade row a retrieval task names is an earlier row too (science 4 day 18, "Refresh s1-...").
        unit = int(rows[0]['stretch'])
        tasks = unit_tasks(rows, allrows, unit, prog)
        prior = {s for r in allrows if int(r['day']) < first for s in split_list(r['skills'])}
        mine = [s for s in skills if s in prog and own(s)]
        early = [s for s in skills if s in prog and not own(s)]
        named = [a for _, t in tasks for a in ids_in(t, prog) if not own(a)]
        assumes = [a for a in uniq(early + [a for s in mine if s not in prior for a in split_list(prog[s]['assumes'])] + named)
                   if a not in set(mine)]
    else:
        assumes = [a for a in uniq(a for s in skills if s in prog and own(s) for a in split_list(prog[s]['assumes']))
                   if a not in set(skills)]
    if not assumes:
        return []
    other, unread = [], []
    for g, c in subject_courses():
        if c == course or cg is None or g >= cg:
            continue
        try:
            other.append((g, c, days_rows(c)))
        except DataError as e:
            unread.append((g, c, str(e)))
    retr_days = {}
    for r in rows:
        if nss:
            clauses = ' '.join(t for d, t in tasks if d == int(r['day']))
        else:
            clauses = ' '.join(retrieval_clauses(r['note'], int(r['day']), broad=True))
        # days.csv `retrieves` (review change 7): the skill ids a day retrieves, stated; it is read first, and the
        # note text still counts where a written course has not filled the column yet
        stated = split_list(r.get('retrieves') or '')
        for a in assumes:
            if a in stated or (a in split_list(r['skills']) and re.search(r'retriev', r['note'], re.I)) \
                    or a in ids_in(clauses, prog) or (not nss and a in clauses):
                retr_days.setdefault(a, []).append(int(r['day']))
    if nss:     # a task for this unit on a day before it (its readiness window)
        for d, t in tasks:
            if d < first:
                for a in ids_in(t, prog):
                    if a in assumes:
                        retr_days.setdefault(a, []).append(d)
    out = []
    for a in assumes:
        e = {'row': a, 'owned': '?', 'last': '', 'lastg': '', 'rule': '', 'named': '', 'off': '', 'group': ''}
        out.append(e)
        p = prog.get(a)
        if p is None:
            e['rule'] = 'not in data/progressions/%s.csv' % SUBJ
            e['off'] = '%s is not a row of the progression (missing data)' % a
            continue
        og = grade_num(p['grade'])
        e['owned'] = 'grade %s' % p['grade']
        here = [int(r['day']) for r in allrows if int(r['day']) < first and used_on(r, a, cg, prog)]
        later = [int(r["day"]) for r in allrows if int(r["day"]) > lastday and used_on(r, a, cg, prog, via=False)]
        if og is None or cg is None:
            e['rule'] = 'grade not a number'
            e['off'] = 'the grade of %s or of the course is not a number' % a
            continue
        if og > cg:
            e['rule'] = 'owned in a later grade'
            e['off'] = '%s is owned in grade %s, after this course: the progression or the unit order is wrong' % (a, p['grade'])
            continue
        if here:
            e['last'] = 'this course, last day %d' % max(here)
            e['lastg'] = 'earlier this year'
            e['rule'] = 'retrieval'
        elif og == cg:
            if later:
                e['last'] = 'this course, first day %d' % min(later)
                e['rule'] = 'taught later in this course'
                e['off'] = '%s is assumed here but first taught on day %d, after this unit' % (a, later[0])
            else:
                e['last'] = 'no day of this course'
                e['rule'] = 'not taught in this course'
                e['off'] = '%s is owned in this grade but no day of this course\'s days.csv teaches it' % a
            continue
        else:
            used = [(g, c, [int(r['day']) for r in rws if used_on(r, a, g, prog)]) for g, c, rws in other]
            used = [u for u in used if u[2]]
            if used:
                g, c, ds = max(used, key=lambda u: u[0])
                e['last'] = 'grade %s (%s, last day %d)' % ('K' if g == 0 else g, c, max(ds))
                e['lastg'] = 'grade %s' % ('K' if g == 0 else g)
                lg = g
            else:
                gone = [u for u in unread if u[0] == og]
                have = [c for g, c, _ in other if g == og]
                e['last'] = 'grade %s, the owner (%s)' % (p['grade'], 'its days.csv is unreadable' if gone else
                                                         'no day of %s cites it' % have[0] if have else 'no days.csv yet')
                e['lastg'] = 'grade %s' % p['grade']
                lg = og
            e['rule'] = 'retrieval' if cg - lg < 2 else 'readiness'
        rd = ready_day is not None and (a in split_list(ready_day['skills']) or a in ready_day['note'])
        names = []
        if rd:
            names.append('readiness check, day %s' % ready_day['day'])
        if a in retr_days:
            names.append('retrieval, day%s %s' % ('s' if len(retr_days[a]) > 1 else '', runs_text(retr_days[a])))
        e['named'] = '; '.join(names) or 'not named by id'
        if nss and not names and e['rule'] == 'retrieval' and e['lastg'] == 'earlier this year':
            # in use this year: no task by id is asked (spot check 2026-11-15, finding 2)
            e['named'] = 'in use this year (no task by id needed)'
        if e['rule'] == 'readiness' and not rd:
            e['group'] = ('want a readiness check, and the readiness check before this unit does not name them'
                          if ready_day is not None else 'want a readiness check, and days.csv holds no readiness check for this unit')
            e['off'] = '%s (last used %s)' % (a, e['lastg'])
        elif e['rule'] == 'retrieval' and rd and a not in retr_days:
            e['off'] = '%s wants retrieval (last used %s), not the readiness check that names it' % (a, e['lastg'])
    return out


def taught_before(allrows, code, day, same_day=False):
    """Teaching days (kinds Understanding, Fluency, Application) of the course before a day that cite the code, its
    parent (for a lettered part) or one of its parts; with same_day, the day itself counts too."""
    names = {code} | set(children(code))
    if len(code) > 1 and code[-1].islower():
        names.add(code[:-1])
    return [int(r['day']) for r in allrows if r['kind'] in TEACH_KINDS and names & set(split_list(r['codes']))
            and (int(r['day']) < day or (same_day and int(r['day']) == day))]


def evidence_pairs(allrows, unit, day):
    """[(other day, later day reuses a record?)] for days within ten course days of an assessment day of the unit where
    both gather evidence child by child (EVIDENCE in goal or note, and an assess value or kind Check). Days of one
    assessment spread over the unit (the same assess value in the same unit) are not a pair."""
    byday = {int(r['day']): r for r in allrows}
    me = byday[day]
    if not EVIDENCE.search(me['goal'] + ' ' + me['note']):
        return []
    out = []
    for d in sorted(byday):
        r = byday[d]
        if d == day or abs(d - day) > 10 or not (r['assess'] or r['kind'] == 'Check'):
            continue
        if not EVIDENCE.search(r['goal'] + ' ' + r['note']):
            continue
        if r['stretch'] == me['stretch'] and r['assess'] == me['assess']:
            continue
        # Collect once is about the same evidence twice (lead, 2026-11-15): two checks on different codes are no pair.
        if not set(split_list(r['codes'])) & set(split_list(me['codes'])):
            continue
        later = byday[max(d, day)]
        out.append((d, bool(REUSE.search(later['goal'] + ' ' + later['note']))))
    return out


def group_column(rows, col):
    """[(item, [days])] for a ;-separated days.csv column (tools, supplies, safety), items in first-seen order; a safety
    cell that is the word none is not an item."""
    order, days, label = [], {}, {}
    for r in rows:
        for it in [x.strip() for x in (r.get(col) or '').split(';') if x.strip()]:
            if col == 'safety' and it.lower() == 'none':
                continue
            k = item_key(it)
            if k not in days:
                order.append(k)
                days[k] = []
                label[k] = it
            if int(r['day']) not in days[k]:
                days[k].append(int(r['day']))
    return [(label[k], days[k]) for k in order]


def item_key(it):
    """An item's key for grouping: case, a bracketed aside and plural endings ignored, so 'foil strip switch (household
    stand-in)' and 'foil strip switch', or 'metal spoons' and 'metal spoon', are one item (spot check 2026-11-15)."""
    t = re.sub(r'\s*\([^)]*\)', '', it.lower())
    words = [re.sub(r'(?<=[a-z]{2})(?<!s)s$', '', x) for x in re.findall(r'[a-z0-9]+', t)]
    return ' '.join(words) or it.lower()


MINS = re.compile(r'\b(?:\d+|one|two|three|four|five|six|seven|eight|nine|ten|twelve|fifteen|twenty|thirty|forty|'
                  r'fifty)[- ]minutes?\b', re.I)
KEPT = re.compile(r'\bas (?:the )?(?:end-of-unit |mid-unit |assessment )?(?:evidence|products?|records?)\b|'
                  r'\bassessment (?:products?|evidence)\b|\bend-of-unit evidence\b|\breused on day\b', re.I)
CODETOK = re.compile(r'(?<![\w.])[A-Z0-9][A-Za-z0-9]*(?:[.-][A-Za-z0-9]+)+')


def evidence_days(rows):
    """Days of a unit with no assess value whose note keeps their product as assessment evidence (math 8 day 34,
    math 5 day 51): an assessment day reuses that record (sequence-write.md rule 2, Collect once)."""
    return [r for r in rows if not r['assess'] and kept_in(r['note'])]


def kept_in(note):
    """True when the note keeps a product as evidence; 'not assessment evidence' and 'no end-of-unit evidence' do
    not (math K day 19, 4.E2 judge h0500)."""
    return any(not re.search(r'\b(?:not|no|never|without)\s+(?:\w+\s+)?$', note[:m.start()], re.I)
               for m in KEPT.finditer(note))


def mentions(text, code):
    """True when a note names the code, or (math and ELA) its lettered or numbered tail the way notes shorten it:
    '7c' for 5.NF.B.7c, 'for 6' for 5.NF.B.6."""
    if re.search(r'(?<![\w.])%s(?![\w])' % re.escape(code), text):
        return True
    tail = code.split('.')[-1] if '.' in code else ''
    if re.fullmatch(r'\d+[a-z]', tail):
        return re.search(r'(?<![\w.])%s\b' % tail, text) is not None
    if tail.isdigit():
        return re.search(r'\bfor %s\b' % tail, text) is not None
    return False


def reuse_sources(note, day, codes, byday):
    """code -> [days] an assessment day's note reuses for it ('Reuse day 51 ... for 7c', 'Do not recollect the full
    performance from day 34'). A sentence that names codes maps only those; one that names none maps every code the
    reused day cites."""
    out = {}
    for sent in re.split(r'(?<=\.)\s+|;\s*', note):
        if not (REUSE.search(sent) or re.search(r'\brecollect\w*|\bre-?scor\w*', sent, re.I)):
            continue
        ds = sorted(x for x in day_nums(sent) if x < day and x in byday)
        if not ds:
            continue
        named = [c for c in codes if mentions(sent, c)]
        others = [t for t in CODETOK.findall(sent) if (t in std_text() or is_pe(t)) and t not in codes]
        if not named and others:
            continue        # it reuses evidence for other codes (science 7 day 95)
        for c in named or codes:
            fam = {c} | set(children(c)) | ({c[:-1]} if c[-1:].islower() else set())
            src = [x for x in ds if fam & set(split_list(byday[x]['codes']))]
            if src:
                out[c] = uniq(out.get(c, []) + src)
    return out


SECTION_DAYS = 15      # a section longer than this is flagged for breaks (math, ELA, science)


def long_sections(sections):
    """[(section, days)] of the sections longer than SECTION_DAYS (ELA K unit 4 is one 39-day section)."""
    return [(k, v) for k, v in sections if len(v) > SECTION_DAYS]
COMPLETES = re.compile(r'\bunit (\d+) completes\b|\bcompleted? in unit (\d+)\b|\bowned (?:later )?in unit (\d+)\b|'
                       r'\bownership remains in unit (\d+)\b', re.I)


def coverage_gaps(codes, evrows, fo, bgn):
    """Owned codes (the frame's Owned standards when it lists any, never a begun code) that no assessment day or kept
    teaching day in evrows cites, itself, through a lettered part or through its parent (field 5 coverage line)."""
    sampled = {c for r in evrows for c in split_list(r['codes'])}
    owned = [c for c in codes if (not fo or c in fo or (c[-1:].islower() and c[:-1] in fo)) and c not in bgn]
    return [c for c in owned if not (({c} | set(children(c)) | ({c[:-1]} if c[-1:].islower() else set())) & sampled)]


def frame_owned(fr):
    """The Owned standards cell of a frame unit row, ~ codes left out (they are begun, not owned)."""
    if not fr or len(fr) < 5:
        return set()
    return {c for c in split_list(fr[4].replace('`', '')) if not c.startswith('~')}


def begun_codes(unit, rows, rawrows, own_sk, prog, fr):
    """code -> where it is completed ('' when not said), for the codes a math, ELA or science unit begins and a later
    unit or grade owns (spot check 2026-11-15, finding 5). A code is begun when days.csv marks it ~ wherever the unit
    cites it, when the progression marks it ~ on the unit's own rows and no own row owns it, or when a note sentence
    that names it (or names no code) says "unit N completes" and the frame's unit row does not own it. A lettered part
    of a begun code is begun too, unless a row owns the part."""
    codes = uniq(c for r in rows for c in split_list(r['codes']))
    rawc = [x for r in rawrows for x in split_list(r['codes'])]
    bare = {x for x in rawc if not x.startswith('~')}
    out = {}
    for x in rawc:
        if x.startswith('~') and x[1:] not in bare:
            out[x[1:]] = ''
    pstd = [x for s in own_sk if s in prog for x in split_list(prog[s]['standard'])]
    pbare = {x for x in pstd if not x.startswith('~')}
    for x in pstd:
        if x.startswith('~') and x[1:] not in pbare and x[1:] in codes:
            out.setdefault(x[1:], '')
    owned = frame_owned(fr)
    for r in rows:
        mine = split_list(r['codes'])
        for sent in re.split(r'(?<=\.)\s+', r['note']):
            m = COMPLETES.search(sent)
            if not m:
                continue
            n = int(next(g for g in m.groups() if g))
            if n <= unit or re.search(r'\b(?:not|never)\b[^.]{0,30}$', sent[:m.start()], re.I):
                continue
            named = [c for c in mine if re.search(r'(?<![\w.])%s(?![\w])' % re.escape(c), sent)]
            for c in named or mine:
                if c not in owned and not (c[-1:].islower() and c[:-1] in owned) and (owned or c not in pbare):
                    if not out.get(c):
                        out[c] = 'unit %d completes it (day %s note)' % (n, r['day'])
    for c in codes:
        if c[-1:].islower() and c[:-1] in out and c not in out and c not in pbare:
            out[c] = out[c[:-1]]
    return out


def build(course, unit):
    allrows = days_rows(course)
    raw = {int(r['day']): r for r in allrows}      # days.csv as written: the day list and the field 5 code cells keep its ~
    if not is_ss():
        # math, ELA, science: a ~ in days.csv marks a begun code; the code itself is the same code (spot check 2026-11-15)
        allrows = [dict(r, codes='; '.join(x.lstrip('~') for x in split_list(r['codes']))) for r in allrows]
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
    frame_meta = next((r for r in read_csv(PLANS / 'frames.csv', FRAMES_COLS) if r['course'] == course), {})
    cal = calendar_rows(course, unit)
    kinds = {}
    for r in rows:
        kinds[r['kind']] = kinds.get(r['kind'], 0) + 1
    order = ['Understanding', 'Fluency', 'Application', 'Check', 'Respond']
    kind_txt = ', '.join('%s %d' % (k.lower(), kinds[k]) for k in order + sorted(set(kinds) - set(order)) if k in kinds)
    sections = sections_of(rows)
    skills = uniq(s for r in rows for s in split_list(r['skills']))
    cg = grade_num(frame_meta.get('grade'))
    own_sk, early_sk, bgn = skills, [], {}
    if not ss:
        tx = dict(tx, hook=tx['hook'].replace('day 1', 'day %d' % first))
        # Spot check 2026-11-15, finding 1: an earlier-grade row in the skills column is listed for retrieval or
        # readiness, never as owned, and feeds neither Builds on nor Leads to.
        early_sk = [s for s in skills if s in prog and grade_num(prog[s]['grade']) is not None and cg is not None
                    and grade_num(prog[s]['grade']) < cg]
        own_sk = [s for s in skills if s not in early_sk]
        bgn = begun_codes(unit, rows, [raw[int(r['day'])] for r in rows], own_sk, prog, fr)
    # Cold reads 2026-11-24 (every core subject): owned is the frame's Skills cell for this unit, in this subject's
    # progression; a row an earlier unit of the course owns is listed as used again, and another subject's row as
    # cross-subject. own_sk above still feeds the begun and progression-note checks, unchanged.
    fsu = frame_skill_units(course)
    fown = [s for s, u in fsu.items() if u == unit and s in prog]
    if not fsu:     # a frame with no Skills cells at all: the days.csv rows, as before
        fown = [s for s in own_sk if s in prog]
    prev_sk = early_sk or [s for s in skills if s in prog and s not in fown and grade_num(prog[s]['grade']) is not None
                           and cg is not None and grade_num(prog[s]['grade']) < cg]
    left = [s for s in skills if s in prog and s not in fown and s not in prev_sk]
    reuse_sk = [s for s in left if fsu.get(s, unit) < unit]
    later_sk = [s for s in left if fsu.get(s, unit) > unit]
    loose_sk = [s for s in left if s not in fsu]
    cross_sk = [s for s in skills if s not in prog]
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
        nweeks = int(cal[-1]['last_week']) - int(cal[0]['first_week']) + 1 if (cal[0]['first_week'].isdigit() and cal[-1]['last_week'].isdigit()) else 0
        if not ss and len(sdays) > len(rows) and nweeks:
            # a course that does not meet every school day (science K, 3 a week): the span is not the days it meets
            sd = '; school days %s (the course meets about %d a week, so not every school day in the span), weeks %s to %s' % (
                runs_text(sdays), round(len(rows) / nweeks), cal[0]['first_week'], cal[-1]['last_week'])
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
    long_secs = long_sections(sections) if not ss else []
    if long_secs:
        # spot check 2026-11-15 (ELA K unit 4, one 39-day section): a section this long is a unit, not a section
        w('%s: Section%s %s run%s more than %d days (days.csv gives the unit one section); propose the section breaks '
          '(days and a one-line name each) and list them under "For the lead"; never change days.csv yourself.'
          % (MARK, 's' if len(long_secs) > 1 else '', ', '.join('%s (%d days)' % (k, len(v)) for k, v in long_secs),
             '' if len(long_secs) > 1 else 's', SECTION_DAYS))
    w('')

    # ---- field 2: standards
    w('## 2. Standards, limits, and what is carried')
    w('')
    if question:
        w('- **Compelling question (frame):** "%s"' % clean(question))
    w('%s: %s' % (MARK, tx['hook']))
    if tx['supq']:
        w('%s: %s' % (MARK, tx['supq']))
    w('%s: %s' % (MARK, tx['claim']))
    w('%s: Teaching moves across the unit: what the teacher does to keep the inquiry going (where to model, where to step back).' % MARK)
    w('')
    codes = days_codes_order(rows, allrows)
    w(OPEN)
    c3_nolines = []
    for c in codes:
        if len(c) > 1 and c[-1].islower() and c[:-1] in codes:
            continue
        begun = c.startswith('~') and len(c) > 1   # a code this course begins and a later one owns (lead, 2026-11-15)
        txt = std_line(c[1:] if begun else c)
        if begun and txt:
            txt = '(begun here; the full expectation is owned and assessed later) ' + txt
        lab_ = c
        if c in bgn:       # math, ELA, science: the ~ shown wherever the code is (spot check 2026-11-15, finding 5)
            lab_ = '~' + c
            if txt:
                txt = '(begun here; %s) %s' % (bgn[c] or 'the full expectation is owned and assessed later', txt)
        kids = [k for k in children(c) if k in codes]
        if txt and 'such as' in txt:
            txt = txt.rstrip() + ' (The "such as" list gives examples, not required parts.)'
        if txt and not kids and is_choice(c):
            opts = '; '.join('%s (%s) %s' % (k[-1], k, clean(std[k])) for k in children(c))
            w('- **%s:** %s Parts: a choice standard, one option studied in depth and the rest surveyed (not each a '
              'required part). Options: %s' % (lab_, clean(txt), opts))
            continue
        b = c[1:] if begun else c
        if subj == 'science' and txt and is_pe(b) and pe_statement(b):
            w('- **%s:** %s%s' % (lab_, clean(txt), pe_limit_lines(b)))
            continue
        if not txt:
            c3_nolines.append(c)
            w('- **%s:** (no own-word line in the standards file%s)' % (lab_, '' if c in std else '; code not found'))
            continue
        if kids:
            parts = '; '.join('%s (%s) %s' % (k[-1], k, clean(std[k])) for k in kids)
            w('- **%s:** %s Parts, by verb: %s' % (lab_, clean(txt), parts))
        else:
            w('- **%s:** %s Parts, by verb: whole standard.' % (lab_, clean(txt)))
    if ss and any(c.startswith('MA.') for c in codes):
        w('- **Taught and assessed in general form:** Curio Class serves every state, so each MA code above is taught and assessed '
          'in general form: the class\'s own place, with worked examples from several states. Massachusetts or Boston is at most one '
          'worked example, never the place every student is assumed to live in; items and sources must not assume it.')
    w(CLOSE)
    w('')
    if c3_nolines and ss:
        w('%s: The skill codes above with no own-word line (%s): give each one line, in your own words, and its parts by '
          'verb, from the indicator in data/standards/c3-indicators.txt.' % (MARK, ', '.join(c3_nolines)))
    elif c3_nolines and subj == 'science':
        w('%s: The performance expectations above have no statement on file (%s; missing data: no statement row in data/standards/ngss-pe-dimensions.csv): '
          'give each one line, in your own words, with its assessment boundary.' % (MARK, ', '.join(c3_nolines)))
    elif c3_nolines:
        w('%s: The codes above that are not in the standards file (%s; missing data): give each one line, in your own words, '
          'and its parts by verb.' % (MARK, ', '.join(c3_nolines)))
    w(OPEN)
    w('- **Progression skills owned (data/progressions/%s.csv):** %s.' % (subj, '; '.join(fown) or 'none listed'))
    if reuse_sk:
        w('- **Earlier rows used again (review, not owned):** %s.' % '; '.join('%s (unit %d)' % (x, fsu[x]) for x in reuse_sk))
    if later_sk:
        w('- **Later rows begun here (owned by a later unit):** %s.' % '; '.join('%s (unit %d)' % (x, fsu[x]) for x in later_sk))
    if loose_sk:
        w('- **Rows in the days.csv skills column that no frame unit lists:** %s.' % '; '.join(loose_sk))
    if prev_sk:
        w('- **Earlier-grade rows in the days.csv skills column (retrieval or readiness, not owned; field 4):** %s.'
          % '; '.join('%s (grade %s)' % (x, grade_of(x, prog)) for x in prev_sk))
    if cross_sk:
        w('- **Rows from other subjects in the days.csv skills column (cross-subject, not owned):** %s.' % '; '.join(cross_sk))
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
    if bgn:
        w('%s: Limits (what this unit does not teach or assess, and why), and for each ~ code above the part this unit teaches and samples (%s).'
          % (MARK, ', '.join('~' + c for c in codes if c in bgn)))
    else:
        w('%s: Limits (what this unit does not teach or assess, and why).' % MARK)
    w('%s: %s' % (MARK, tx['carried']))
    w('')

    # ---- field 3: where it sits
    w('## 3. Where it sits')
    w('')
    assumes = uniq(a for s in fown for a in split_list(prog[s]['assumes']))
    hands = uniq(a for s in fown for a in split_list(prog[s]['hands_on']))
    own = set(fown)
    if not ss:
        # Leads to never names a row this course already taught or an earlier grade's row (math 5, math 8, geometry)
        done = {s for r in allrows if int(r['day']) < first for s in split_list(r['skills'])}
        hands = [a for a in hands if a not in done and not (a in prog and cg is not None and grade_num(prog[a]['grade']) is not None
                                                            and grade_num(prog[a]['grade']) < cg)]
    def lab(x):
        return '%s (grade %s)' % (x, grade_of(x, prog))
    w(OPEN)
    w('- **Builds on (progression, assumes):** %s.' % ('; '.join(lab(a) for a in assumes if a not in own) or 'none listed'))
    w('- **Leads to (progression, hands on):** %s.' % ('; '.join(lab(a) for a in hands if a not in own) or 'none listed'))
    earlier = earlier_unit_skills(allrows, rows, unit)
    if earlier:
        w('- **Earlier units in this course whose skills the days of this unit cite (days.csv skills):** %s.'
          % '; '.join('unit %d (%s)' % (u, ', '.join(sk_)) for u, sk_ in earlier))
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
    retr = []
    if ss:
        for r in rows:
            for t in retrieval_clauses(r['note'], int(r['day']), broad=False):
                retr.append((int(r['day']), clean(t)))
    else:
        retr = [(d, clean(t)) for d, t in unit_tasks(rows, allrows, unit, prog)]

    def ready_for_me(p):
        return p is not None and (p['assess'] == 'readiness' or
                                  re.search(r"(unit %d's|next unit's) readiness" % unit, p['note'], re.I) is not None)
    # the check may sit up to three days back (sequence.py READINESS_AHEAD), through respond or course-level (C) days,
    # so long as no other unit opens between
    prev = byday.get(first - 1)
    for k in range(1, 4):
        p = byday.get(first - k)
        if p is None:
            break
        between = [byday.get(first - j) for j in range(1, k)]
        if any(b is None or b['stretch'] not in (p['stretch'], 'C') for b in between):
            break
        if ready_for_me(p):
            prev = p
            break
    given_prev = ready_for_me(prev)
    w_ready = False
    ready1 = []
    erows = []
    if not ss:
        # math, ELA, science: every earlier row the unit assumes, its last use and the treatment rule 2 gives it
        rday = rows[0] if (first == 1 and rows[0]['assess'] == 'readiness') else (prev if given_prev and first != 1 else None)
        erows = earlier_rows(course, rows, allrows, prog, frame_meta, rday)
        if first == 1:
            ready1 = [e['row'] for e in erows if e['rule'] == 'readiness']
    elif first == 1:
        # lead rule 2026-11-14: no sitting before day 1. Readiness rows are the skills this unit assumes that were last
        # used two or more grades back (a row from the year before is a retrieval task, scope and sequence rule 1) and
        # that no retrieval task of the unit already carries; with none, the check is not needed and retrieval stands alone.
        retr_text = ' '.join(t for _, t in retr)
        ready1 = [a for a in uniq(a for s_ in uniq(s for r in rows for s in split_list(r['skills'])) if s_ in prog
                                  for a in split_list(prog[s_]['assumes']))
                  if a not in set(s for r in rows for s in split_list(r['skills'])) and a not in retr_text
                  and not year_before(a, prog, frame_meta)]
    if first == 1 and (ready1 or rows[0]['assess'] == 'readiness'):
        w('**Given:** day %d, the last ten minutes, after the hook (lead rule 2026-11-14: no sitting before day 1; reteach on day 2 or 3). '
          'Readiness rows (%s): %s.'
          % (first, 'progression, assumes, not retrieved in this unit' if ss else 'rule 2, the table below',
             '; '.join('%s (grade %s)' % (a, grade_of(a, prog)) for a in ready1) or 'none found; days.csv day 1 marks the check, see its note'))
        w_ready = True
    elif first == 1:
        w('Start-of-year check: none needed; retrieval only.')
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
        w('%s: Readiness items (at least one for each earlier-grade row the %s), a gap-by-gap ten-minute reteach, '
          'when it happens, and the earlier tool or page.' % (MARK, 'note above names' if ss else 'table below marks readiness'))
    if erows:
        w('')
        w('Earlier rows this unit assumes (progression assumes; last use from the days.csv of this course and earlier grades, '
          'a day that only retrieves or checks readiness not counted; rule 2 of sequence-write.md: last used the year before or '
          'earlier this year, retrieval; two or more grades back, readiness check):')
        w('')
        w(OPEN)
        w('| Row | Owned | Last used | Rule says | days.csv names it |')
        w('|---|---|---|---|---|')
        for e in erows:
            w('| %s | %s | %s | %s | %s |' % (e['row'], e['owned'], clean(e['last']) or '-', e['rule'], e['named'] or '-'))
        w(CLOSE)
        offs = [e['off'] for e in erows if e['off'] and not e['group']]
        for gtext in uniq(e['group'] for e in erows if e['group']):
            items = [e['off'] for e in erows if e['group'] == gtext]
            if len(items) == 1:
                gtext = gtext.replace('want a', 'wants a', 1).replace(' name them', ' name it')
            offs.append('%s %s' % (', '.join(items), gtext))
        if offs:
            w('')
            w('%s: days.csv and rule 2 disagree: %s. Plan what the plan can (a retrieval task inside an existing day; readiness '
              'items where a check is given); never add a day; list each disagreement under "For the lead".' % (MARK, '; '.join(offs)))
    quiet = [e['row'] for e in erows if e['rule'] == 'retrieval' and e['named'] == 'not named by id']
    if retr or quiet:
        w('')
        w('Retrieval tasks (rows used the year before or earlier the same year; days.csv notes):')
        w('')
        w('| Day | The row and task (days.csv) | The prompt, and what the teacher does with a miss |')
        w('|---|---|---|')
        if ss:
            for d, t in retr:
                w('| %d | %s | %s: the prompt, and what the teacher does with a miss |' % (d, t, MARK))
        else:
            # one row per distinct task, its days together (a note repeated across days is one task)
            for t in uniq(t for _, t in retr):
                w('| %s | %s | %s: the prompt, and what the teacher does with a miss |'
                  % (runs_text([d for d, u in retr if u == t]), t, MARK))
        for a in quiet:
            w('| %s: the day it opens, inside existing time | %s (rule 2 retrieval; days.csv names no task for it) | %s: the prompt, '
              'and what the teacher does with a miss |' % (MARK, a, MARK))
    w('')

    # ---- field 5: end-of-unit assessment
    w('## 5. End-of-unit assessment, whole')
    w('')
    ass = [r for r in rows if r['assess'] in ('end', 'mid', 'observe')]
    kept = [] if ss else evidence_days(rows)
    if kept:
        w(OPEN)
        w('- **Evidence kept on teaching days (days.csv notes; an assessment day reuses it, never collects it again):** %s.'
          % '; '.join('day %s (%s)' % (r['day'], ', '.join(split_list(r['codes'])) or 'no codes') for r in kept))
        w(CLOSE)
        w('')
    for r in ass:
        label = {'end': 'End-of-unit assessment', 'mid': 'Mid-unit assessment', 'observe': 'End-of-unit assessment (observation)'}[r['assess']]
        w('Day %s (%s): %s' % (r['day'], label, clean(r['goal'])))
        if r['note'] and ss:
            w('Note (days.csv): %s' % clean(r['note']))
        elif r['note']:
            # printed once, in the day list (spot check 2026-11-15, bulk)
            w('Note (days.csv): in the day list, day %s; read it before writing the items.' % r['day'])
        acodes = split_list(r['codes'])
        full = []
        for c in acodes:
            full.append(c)
            full.extend(k for k in parts_of(c, rows, allrows) if k not in acodes)
        todo5 = []
        reused, contrib = {}, set()
        if not ss:
            d = int(r['day'])
            reused = reuse_sources(r['note'], d, full, byday)
            contrib = {c for c in full if re.search(r'(?<![\w.])%s(?![\w])[^.;]{0,40}contributing evidence' % re.escape(c), r['note'], re.I)}
            w(OPEN)
            lo, hi = frame_meta.get('minutes_min', ''), frame_meta.get('minutes_max', '')
            mins = lo if lo == hi else '%s to %s' % (lo, hi)
            hosts = re.search(r"(unit %d's|next unit's) readiness" % (unit + 1), r['note'], re.I)
            own = [s for s in re.split(r'(?<=\.)\s+|\s*\|\s*', r['note'])
                   if not any(x != d for x in day_nums(s))]
            named_mins = uniq(m.group(0).lower() for s in own for m in MINS.finditer(s))
            w('- **Time:** %s; %d row%s below to sample.%s'
              % (('%s minutes a day (data/plans/frames.csv)%s' % (mins, ", less 10 for the next unit's readiness check on this day" if hosts else ''))
                 if lo else 'day length not in data/plans/frames.csv', len(full), '' if len(full) == 1 else 's',
                 (' The note budgets its own minutes (%s): fit the items to those, not to the whole day.' % ', '.join(named_mins[:8]))
                 if named_mins else ''))
            if reused:
                w('- **Reused, not collected again (days.csv note):** %s.'
                  % '; '.join('%s from day%s %s' % (c, 's' if len(v) > 1 else '', runs_text(v)) for c, v in reused.items()))
            untaught = [c for c in acodes if not taught_before(allrows, c, d, same_day=r['assess'] == 'observe')]
            if untaught:
                w('- **Assessed before any teaching day cites it (days.csv codes):** %s.' % ', '.join(untaught))
                todo5.append('%s: Day %d assesses %s before any teaching day of days.csv cites %s: name the earlier day that teaches %s '
                             '(cited under another code), or list it under "For the lead"; a code is assessed only after a day teaches it.'
                             % (MARK, d, ', '.join(untaught), 'it' if len(untaught) == 1 else 'them', 'it' if len(untaught) == 1 else 'each'))
            pairs = evidence_pairs(allrows, unit, d)
            if pairs:
                w('- **Child-by-child evidence within ten days (days.csv goals and notes):** %s.'
                  % '; '.join('day %d also gathers it, %d days %s%s' % (o, abs(o - d), 'before' if o < d else 'after',
                                                                  ' (the later note reuses the record)' if ok else '')
                              for o, ok in pairs))
                bad5 = [o for o, ok in pairs if not ok]
                if bad5:
                    todo5.append('%s: Collect once (sequence-write.md rule 2): day %d and day%s %s both gather evidence child by child within '
                                 'ten days; plan the later one to reuse the earlier record and say so, or list it under "For the lead".'
                                 % (MARK, d, 's' if len(bad5) > 1 else '', runs_text(bad5)))
            w(CLOSE)
        w('')
        w('| Day | Code | Part (own words) | The item, answer and wrong answers (error letter) | Owner |')
        w('|---|---|---|---|---|')
        rawday = split_list(raw[int(r['day'])]['codes'])
        for c in full:
            txt = clean(std_line(c[1:] if c.startswith('~') and len(c) > 1 else c))
            if txt and c.startswith('~'):
                txt = '(begun here, owned later; sample only what this unit teaches) ' + txt
            elif txt and c in bgn:
                txt = '(~ begun here, owned later; sample only what this unit teaches) ' + txt
            if is_choice(c) and not any(k in full for k in children(c)):
                txt = '%s (a choice standard: one row, on the option each student chose)' % txt
            if len(c) > 1 and c[-1].islower() and c[:-1] in full:
                part = '%s: %s' % (c[-1], txt)
            else:
                part = txt or ('whole indicator (verb from the C3 file)' if ss else
                               'whole expectation (statement not on file; see the field 2 table)' if subj == 'science'
                               else 'whole standard')
            item, owner = MARK, 'section %s' % r['unit']
            if not ss:
                if any(k in full for k in children(c)):
                    # the parts below carry the items; the parent keeps its row for scripts/unitplan.py (spot check, finding 6)
                    part, item = 'the lettered parts below', 'Asked through the part rows below; no separate item.'
                if c in reused:
                    owner = 'reused from day%s %s (no new item; name the record)' % ('s' if len(reused[c]) > 1 else '', runs_text(reused[c]))
                elif c in contrib:
                    owner = 'section %s, contributing evidence only (days.csv note)' % r['unit']
            shown = ('~' + c) if ('~' + c) in rawday else c
            w('| %s | %s | %s | %s | %s |' % (r['day'], shown, part, item, owner))
        w('')
        if todo5:
            W.extend(todo5)
            w('')
    if not ass:
        w('days.csv marks no end-of-unit assessment day in this unit.')
        w('')
    if not ss:
        # an owned code whose evidence has no assessment day (science 7, ELA K; spot check 2026-11-15, finding 6)
        gaps = coverage_gaps(codes, ass + kept, frame_owned(fr), bgn)
        if gaps:
            w(OPEN)
            w('- **Owned codes on no assessment day of this unit (days.csv codes; frame Owned standards):** %s.' % ', '.join(gaps))
            w(CLOSE)
            w('%s: For each code just listed, name the assessment day and item, or the kept product, that gives its evidence; '
              'where none does, list it under "For the lead" (never add a day).' % MARK)
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
        if int(r['day']) == first:
            continue    # a readiness check on the unit's own first day is its own (unit 1, day 1), not the next unit's
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
    progcodes = uniq(c for s in own_sk if s in prog for c in split_list(prog[s]['standard']))
    if ss:
        only = [c for c in progcodes if c not in codes]
    else:
        # a code cited through its lettered parts, or a part cited through its parent, is cited (spot check, ELA K and 7)
        def cited(c):
            c = c.lstrip('~')
            return c in codes or any(k in codes for k in children(c)) or (c[-1:].islower() and c[:-1] in codes)
        only = [c for c in progcodes if not cited(c)]
    if only:
        w('- **Note:** the progression lists %s for these skills, but days.csv does not cite %s.%s'
          % (', '.join(only), 'it' if len(only) == 1 else 'them',
             ' A leading ~ marks a standard the row touches without owning.' if not ss and any(c.startswith('~') for c in only) else ''))
    if fr and fr[8].strip():
        w('- **Check set adds (frame):** %s' % clean(fr[8]))
    sm = source_rows(course, unit) if ss else []
    miss10 = []
    if not ss:
        extra10, miss10 = field10_extras(course, unit)
        W.extend(extra10)
    elif sm:
        w('- **Source map (data/plans/%s/source-map.csv):**' % course)
        for r in sm:
            w('  - %s, %s (our days %s): %s. %s' % (r['source'], clean(r['title']), r['days'], r['decision'], clean(r['why'])))
    if subj == 'ela':
        trows = ela_texts(course, unit)
        if trows:
            w('- **Texts:** author, year, edition and rights of each are in the text set of field 2 (data/plans/ela-texts.csv).')
    sens = [r for r in rows if 'sensitiv' in r['note'].lower()]
    if fr and fr[9].strip():
        w('- **Sensitive topics%s (frame):** %s' % ('' if ss else ' and teacher notes', clean(fr[9])))
    if sens and ss:
        w('- **Days flagged for the sensitivity read (days.csv notes):**')
        for r in sens:
            w('  - Day %s: %s' % (r['day'], clean(r['note'])))   # in full: the bracket often holds what to read
    elif sens:
        w('- **Days flagged for the sensitivity read (their notes, in full, are in the day list):** %s.'
          % runs_text([int(r['day']) for r in sens]))
    w(CLOSE)
    if ss:
        w('%s: Sources chosen for the unit (named, with licence and what was read); the primary sources and the community\'s own sources first.' % MARK)
        w('%s: What the sensitivity agent (docs/pipeline/briefs/sensitivity-read.md) must study for this unit, the community\'s own sources first; or one line saying the unit has no cultural, Native, hard-history, faith, health or disability content.' % MARK)
    else:
        for m in miss10:
            w(m)
        src = {'math': 'the base-text lessons used with each credit line, and the Progressions pages read',
               # only grades 6 to 8 adapt a base text; the others are Curio Class's own (spot check 2026-11-15)
               'science': ('the base unit and lessons adapted with each credit line, and public data sets with their rights lines'
                           if base_text_of(course) else
                           'the references read (no base text: this grade\'s units are Curio Class\'s own, any outside unit is '
                           'reference only and never copied), and public data sets with their rights lines'),
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
        w('| %d | %s | %s | %s | %s | %s |' % (d, sdv, r['kind'], clean(r['goal']), '; '.join(split_list(raw[d]['codes'])), clean(r['note'])))
    w('')
    return '\n'.join(W)


def self_test():
    """Checks of the computed lines on small made-up data in a temporary --data-dir (real course ids, so frames.csv
    gives grades; nothing under data/ or docs/ is written). Prints each check and returns 0 when all pass."""
    import tempfile
    fails = []

    def check(name, ok):
        print('%s  %s' % ('ok  ' if ok else 'FAIL', name))
        if not ok:
            fails.append(name)

    def stops(name, fn, *want):
        try:
            fn()
            check(name, False)
        except DataError as e:
            check(name, all(x in str(e) for x in want))

    head = 'day,stretch,unit,kind,goal,skills,codes,assess,note\n'
    saved = DATA_DIR, SUBJ
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)

        def put(course, name, text):
            (t / course).mkdir(parents=True, exist_ok=True)
            (t / course / name).write_text(text, encoding='utf-8', newline='\n')

        set_data_dir(t)
        set_subject('science')
        # 1. a source map in an older layout stops with a message naming the file and the missing columns
        put('science-grade-3', 'source-map.csv', 'base_unit,day,decision\nU1,1,keep\n')
        stops('old-layout source map stops', lambda: source_map('science-grade-3'),
              'source-map.csv', 'missing: source,title', 'convert it first')
        put('science-grade-3', 'source-map.csv', ','.join(MAP_COLS) + '\nOS,T,g,3-PS2-1,1,1 to 2,keep,w,,no\n')
        check('one-layout source map reads', len(source_map('science-grade-3')) == 1)
        # 2. days.csv: a missing column, a day that is not a whole number, a short row
        put('science-grade-4', 'days.csv', 'day,stretch,unit,kind,goal\n1,1,1.1,Understanding,g\n')
        stops('days.csv missing column stops', lambda: days_rows('science-grade-4'), 'missing: skills,codes,assess,note')
        put('science-grade-4', 'days.csv', head + 'x,1,1.1,Understanding,g,,,,\n')
        stops('non-number day stops', lambda: days_rows('science-grade-4'), 'day "x" is not a whole number')
        put('science-grade-4', 'days.csv', head + '1,1,1.1,Understanding,g,,\n')
        stops('short row stops', lambda: days_rows('science-grade-4'), 'data row 1 has')
        # 3. rule 2 by last use: a K row last used in K is readiness in grade 3, a grade 2 row retrieval
        put('science-kindergarten', 'days.csv', head + '5,1,1.1,Understanding,g,tk-push,,,\n')
        put('science-grade-2', 'days.csv', head + '9,1,1.1,Application,g,t2-design,,,\n')
        put('science-grade-3', 'days.csv', head + '1,1,1.1,Understanding,g,t3-force,3-PS2-1,,Retrieve t2-design after the hook.\n'
                                                  '2,1,1.1,Check,g,t3-force,3-PS2-1,end,\n')
        prog = {'tk-push': {'grade': 'K', 'assumes': ''}, 't2-design': {'grade': '2', 'assumes': ''},
                't3-force': {'grade': '3', 'assumes': 'tk-push;t2-design;t9-none'}}
        rows = days_rows('science-grade-3')
        meta = {'grade': '3'}

        def er(ready=None):
            return {e['row']: e for e in earlier_rows('science-grade-3', rows, rows, prog, meta, ready)}
        e = er()
        check('K row last used in K is readiness in grade 3',
              e['tk-push']['rule'] == 'readiness' and 'no readiness check' in e['tk-push']['group'])
        check('grade 2 row is retrieval, named on day 1', e['t2-design']['rule'] == 'retrieval'
              and e['t2-design']['named'] == 'retrieval, day 1' and not e['t2-design']['off'])
        check('row missing from the progression is flagged', 'not a row of the progression' in e['t9-none']['off'])
        check('readiness check naming the row clears the fault',
              not er({'day': '1', 'skills': 'tk-push', 'note': ''})['tk-push']['off'])
        # a grade 2 day that only retrieves the K row is not a use; a grade 2 teaching day is
        put('science-grade-2', 'days.csv', head + '9,1,1.1,Application,g,t2-design;tk-push,,,Retrieve tk-push.\n')
        check('a retrieval day is not a use', er()['tk-push']['rule'] == 'readiness')
        put('science-grade-2', 'days.csv', head + '9,1,1.1,Application,g,t2-design;tk-push,,,\n')
        e = er()
        check('a grade 2 teaching day makes the K row retrieval', e['tk-push']['rule'] == 'retrieval'
              and e['tk-push']['last'] == 'grade 2 (science-grade-2, last day 9)')
        # an unreadable days.csv in an earlier grade is noted, not a traceback
        put('science-grade-2', 'days.csv', 'day\n1\n')
        check('unreadable earlier days.csv is noted', 'unreadable' in er()['t2-design']['last'])
        # spot check 2026-11-15: an earlier-grade id in the skills column is a retrieval row, not owned; a row in use
        # earlier this year needs no task by id
        put('science-grade-2', 'days.csv', head + '9,1,1.1,Application,g,t2-design,,,\n')
        put('science-grade-3', 'days.csv', head + '1,1,1.1,Understanding,g,t3-force,3-PS2-1,,\n'
                                                  '2,2,2.1,Understanding,g,t3-force;t3-next;t2-old,3-PS2-2,,Retrieve t2-old (grade 2).\n')
        prog.update({'t2-old': {'grade': '2', 'assumes': ''}, 't3-next': {'grade': '3', 'assumes': 't2-design;tk-push'}})
        al3 = days_rows('science-grade-3')
        e = {x['row']: x for x in earlier_rows('science-grade-3', [r for r in al3 if r['stretch'] == '2'], al3, prog, meta, None)}
        check('earlier-grade skills-column id is a retrieval row, named', 't2-old' in e
              and e['t2-old']['rule'] == 'retrieval' and e['t2-old']['named'] == 'retrieval, day 2')
        check('row in use this year needs no task by id', e['t2-design']['named'].startswith('in use this year'))
        check('own-grade skills are never earlier rows', 't3-force' not in e and 't3-next' not in e)
    set_data_dir(saved[0])
    # 8. spot check 2026-11-15 (math, ELA, science paths; social studies output is frozen)
    set_subject('math')
    for cell, want in [('Adding within 20. *What makes a sum easy to find?*', ('Adding within 20', 'What makes a sum easy to find?')),
                       ('Smallpox: who gets the credit? "Who should get the credit?"', ('Smallpox: who gets the credit?', 'Who should get the credit?')),
                       ('Similarity: How can a photo tell us true lengths?', ('Similarity', 'How can a photo tell us true lengths?')),
                       ('**Douglass** (weeks 17 to 19). How did reading change him?', ('Douglass', 'How did reading change him?'))]:
        check('compelling question split: %s' % want[0], split_unit_cell(cell)[:2] == want)
    an = split_unit_cell('Ramps. *Why?* Design problem: miss a block tower Anchor: our ball rolls.')[2]
    check('design sentence ends before the anchor', 'tower. Anchor: our ball' in an)
    tc = task_clauses('Then grammar retrieval. Retrieval openings never count as assessment evidence. '
                      'Retrieve m4-mixed-numbers (grade 4).', 10, {'m4-mixed-numbers': {}}, 5)
    check('retrieval junk dropped, whole task kept', tc == ['Retrieve m4-mixed-numbers (grade 4).'])

    def R(d, st, k, sk, c, a, n):
        return dict(day=str(d), stretch=st, unit=st + '.1', kind=k, goal='g', skills=sk, codes=c, assess=a, note=n)
    pr = {'e6-a': {'grade': '6', 'assumes': ''}, 'e7-b': {'grade': '7', 'assumes': 'e6-a'}, 'e7-c': {'grade': '7', 'assumes': ''}}
    al = [R(84, '3', 'Understanding', 'e7-c', '', '', 'Retrieve e6-a for unit 3.'), R(85, '3', 'Understanding', 'e7-c', '', '', ''),
          R(86, '3', 'Check', 'e7-c', '', 'end', 'Retrieve e6-a for unit 4.'), R(87, '4', 'Understanding', 'e7-b', '', '', '')]
    check('a task for the next unit is credited to it', unit_tasks(al[3:], al, 4, pr) == [(86, 'Retrieve e6-a for unit 4.')]
          and unit_tasks(al[:3], al, 3, pr) == [(84, 'Retrieve e6-a for unit 3.')])
    p2 = {'m7-a': {'grade': '7', 'assumes': ''}, 'm8-b': {'grade': '8', 'assumes': 'm7-a'}}
    check('a respond or check day is no one-hop use', not used_on(R(5, '1', 'Respond', 'm8-b', '', '', ''), 'm7-a', 8, p2)
          and not used_on(R(5, '1', 'Check', 'm8-b', '', '', ''), 'm7-a', 8, p2)
          and used_on(R(5, '1', 'Understanding', 'm8-b', '', '', ''), 'm7-a', 8, p2))
    rows8 = [R(31, '2', 'Understanding', 'm8-x', '8.G.A.4;8.EE.B.6', '', 'Begin slope; unit 3 completes the derivations.'),
             R(32, '2', 'Understanding', 'm8-x', '~8.F.A.1', '', ''), R(35, '2', 'Check', 'm8-x', '8.G.A.4', 'end', '')]
    st8 = [dict(r, codes=r['codes'].replace('~', '')) for r in rows8]
    bg = begun_codes(2, st8, rows8, ['m8-x'], {'m8-x': {'grade': '8', 'standard': '8.G.A.4;~8.EE.B.6', 'assumes': ''}},
                     ['2', 'u', '16', 'm8-x', '8.G.A.4'])
    check('begun: ~ in days.csv, and "unit N completes" outside the frame owned list',
          bg == {'8.F.A.1': '', '8.EE.B.6': 'unit 3 completes it (day 31 note)'})
    check('reuse note maps a code to its source day',
          reuse_sources('Reuse day 31 record for 8.G.A.4; no new collection.', 35, ['8.G.A.4'],
                        {int(r['day']): r for r in st8}) == {'8.G.A.4': [31]})
    check('note shorthand names a part', mentions('Reuse day 51 for 7c and for 6', '5.NF.B.7c')
          and mentions('Reuse day 51 for 7c and for 6', '5.NF.B.6') and not mentions('for 7c', '5.NF.B.7a'))
    check('kept evidence day found', [r['day'] for r in evidence_days(
        [R(34, '2', 'Application', '', '8.G.A.4', '', 'Retain the product as end-of-unit evidence.'),
         R(33, '2', 'Application', '', '8.G.A.4', '', '')])] == ['34'])
    check('coverage: owned code on no assessment day, parts and begun codes handled',
          coverage_gaps(['8.G.A.4', '8.G.A.3', '8.EE.B.6', '5.NF.B.7'], [R(35, '2', 'Check', '', '8.G.A.4;5.NF.B.7a', 'end', '')],
                        {'8.G.A.4', '8.G.A.3', '5.NF.B.7'}, {'8.EE.B.6': ''}) == ['8.G.A.3'])
    check('a section over 15 days is flagged',
          [k for k, _ in long_sections([('4.1', list(range(39))), ('4.2', list(range(10)))])] == ['4.1'])
    check('near-duplicate items merge', group_column([dict(day='1', supplies='foil strip switch (household stand-in)'),
                                                      dict(day='2', supplies='Foil strip switch'), dict(day='3', supplies='metal spoons'),
                                                      dict(day='3', supplies='metal spoon')], 'supplies')
          == [('foil strip switch (household stand-in)', [1, 2]), ('metal spoons', [3])])
    check('wap spelled out on the weight line', any('widely applicable prerequisite' in x for x in header_weight(['G-SRT.B.5'])))
    set_subject('science')
    check('engineering expectation with no crosscutting concept says so', 'None listed for this engineering' in pe_row('K-2-ETS1-1'))
    # the science 7 food-web cell that first showed this changed in 4.E2 (unit 4 is now its first use), so a fixture
    _fl = frame_lines
    globals()['frame_lines'] = lambda course: ['| Model | Where it comes from | Unit that first uses it here | Units that use it again |',
                                               '|---|---|---|---|',
                                               '| food-web | grade 5 | Unit 3 readiness day 41 checks this; unit 4 retrieves it | Unit 5 |']
    try:
        check('a model first used in an earlier unit is not "introduced here"',
              any(m == 'food-web' and 'first used in unit 3' in h for m, h in frame_models('science-grade-7', 4)))
    finally:
        globals()['frame_lines'] = _fl
    # 4. assessed before taught; a lettered part counts its parent
    al = [dict(day=str(d), stretch='1', unit='1.1', kind=k, goal='', skills='', codes=c, assess=a, note='')
          for d, k, c, a in [(1, 'Understanding', '3-PS2-1', ''), (2, 'Check', '3-PS2-1;3-PS2-2', 'end'),
                             (3, 'Understanding', '3-PS2-2', '')]]
    check('code taught day 1 counts before day 2', taught_before(al, '3-PS2-1', 2) == [1])
    check('code first taught day 3 is untaught at day 2', taught_before(al, '3-PS2-2', 2) == [])
    check('same-day teaching counts with same_day', taught_before(al, '3-PS2-2', 3, same_day=True) == [3])
    # 5. child-by-child evidence within ten days, a reuse note, one assessment spread over a unit
    ev = [dict(day=str(d), stretch=s, unit=s + '.1', kind='Check', goal=g, skills='', codes='W.3.1', assess=a, note=n)
          for d, s, g, a, n in [(3, '1', 'one-to-one interview', 'mid', ''),
                                (9, '2', 'conference on drafts', 'end', 'reuse the day 3 record'),
                                (12, '2', 'conference on drafts', 'end', ''),
                                (30, '3', 'one-to-one interview', 'end', '')]]
    check('evidence pair within ten days, reuse read', evidence_pairs(ev, 2, 9) == [(3, True)])
    check('checks on different codes are no pair',
          evidence_pairs([dict(r, codes='W.3.2') if r['day'] == '3' else r for r in ev], 2, 9) == [])
    check('no pair beyond ten days', evidence_pairs(ev, 3, 30) == [])
    # 6. grouped columns, with safety none dropped
    gc = [dict(day='1', safety='goggles; none'), dict(day='2', safety='goggles'), dict(day='4', safety='none')]
    check('grouped safety column', group_column(gc, 'safety') == [('goggles', [1, 2])])
    # 7. the same input writes the same skeleton (the first science course with days and no source map)
    for c in courses_of('science'):
        set_subject('science')
        try:
            us = unit_numbers(c)
            if not us or source_map(c):
                continue
            check('deterministic (%s unit %d)' % (c, us[0]), build(c, us[0]) == build(c, us[0]))
        except DataError:
            continue
        break
    set_subject(saved[1])
    print('%d failed' % len(fails) if fails else 'all passed')
    return 1 if fails else 0


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
    if a[:1] == ['--self-test']:
        return self_test()
    if a[:1] == ['--list'] and len(a) <= 2:
        subj = a[1] if len(a) == 2 else None
        if subj and subj not in SUBJECTS:
            raise SystemExit('subject must be one of: %s' % ', '.join(SUBJECTS))
        for c in courses_of(subj):
            set_subject(subject_of(c))
            try:
                n = len(unit_numbers(c))
            except DataError as e:
                print('%-48s ? units (cannot read: %s)' % (c, e))
                continue
            print('%-48s %d units' % (c, n) + ('' if n else ' (no days.csv yet)'))
        return 0
    if not a or a[0] in ('-h', '--help'):
        print(__doc__)
        return 0 if a else 2
    course = a[0]
    if subject_of(course) is None:
        raise SystemExit('not a course in data/plans/frames.csv: %s' % course)
    set_subject(subject_of(course))
    units = unit_numbers(course)
    if not units:
        raise SystemExit('%s has no days.csv yet (its scope and sequence comes first, PRODUCTION-PATH step 5)' % course)
    if len(a) > 1:
        if not a[1].isdigit() or int(a[1]) not in units:
            raise SystemExit('%s has no unit %s (units: %s)' % (course, a[1], runs_text(units)))
        units = [int(a[1])]
    folder = (out / course) if out else (DOCS / course)
    side = folder / 'unit-skeletons'
    side.mkdir(parents=True, exist_ok=True)
    import plan_facts
    for u in units:
        try:
            text = build(course, u)
        except DataError as e:
            raise DataError('unit_skeleton: %s unit %d not written: %s' % (course, u, e))
        s = side / ('s%02d.md' % u)
        s.write_text(text, encoding='utf-8', newline='\n')
        print('wrote', s, '(%d TODO, %d words, about %d tokens)' % (text.count(MARK), len(text.split()), len(text) // 4))
        p = folder / ('s%02d.md' % u)
        if p.exists():
            print('plan exists, kept:', p)
            continue
        p.write_text(plan_facts.with_link(course, p.name, plan_facts.strip(text)), encoding='utf-8', newline='\n')
        print('wrote', p, '(the starter plan: headings and writer markers; its facts render from data)')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

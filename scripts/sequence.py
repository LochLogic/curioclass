"""Scope and sequence gate (PRODUCTION-PATH step 3): a course's day map before any section plan or item exists.

    python -X utf8 scripts/sequence.py check [course]     exit 1 on any failure

Reads docs/courses/<course>/frame.md (through scripts/frame.py) and data/plans/<course>/days.csv at the scope stage:
one row per course day, with the columns of docs/pipeline/briefs/sequence-write.md
(day, stretch, unit, kind, goal, skills, codes, assess, school_day, note). `stretch` is the unit number, or C for a
course-level check day or its respond day (with a blank `unit`). plan.py runs this gate for a course whose plan
folder has days.csv but no parts.csv and no items.csv; once section plans are written, plan.py's full gate takes over.
Added 2026-11-14 (baseline 1 structure finding 2).

Optional columns after `note`, for math and science only: tools, supplies, safety (semicolon lists, empty when none;
see sequence-write.md). Added 2026-11-14. Social studies and ELA days.csv files are never checked for them.

Source map (added 2026-11-15, one layout for every subject, sequence-write.md rule 8): where
data/plans/<course>/source-map.csv exists its columns start with MAP_COLS in that order (`url` may follow), every
decision is keep, split, merge, cut or ours, `unit` is a unit number or <unit>.<n> of the frame, `days` lists course
days in range ("12", "12-13", "12; 14"), blank only on a cut, and every cut gives its reason in `why`.

Fluency kind (added 2026-11-17, later.csv L64; definitions in docs/GLOSSARY.md, row "teaching day"): a Fluency day
whose goal drafts or edits writing, or introduces or teaches, fails (fluency_checks). What a script cannot judge is a
note: a goal that revises a piece of writing, a note that introduces, teaches, begins or drafts, and a code the day
carries for the first time in the course (map and fact-routine days do this legitimately).

Rule 2 (added 2026-11-15, notes only for now): every unit's readiness and retrieval are counted as the unit skeleton
counts them (rule2_notes); a missed readiness row or a readiness check where retrieval is due prints a note.
"""
import csv, io, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLANS = ROOT / 'data' / 'plans'
DOCS = ROOT / 'docs' / 'courses'
sys.path.insert(0, str(Path(__file__).resolve().parent))
import frame   # noqa: E402

KINDS = {'Understanding', 'Fluency', 'Application', 'Check', 'Respond'}
ASSESS = {'', 'readiness', 'mid', 'end', 'course', 'observe'}
MID_UNIT_DAYS = 25          # a unit longer than this carries a mid-unit assessment
READINESS_AHEAD = 3         # a readiness check sits at most this many days before its unit's first day
NEED = ['day', 'stretch', 'unit', 'kind', 'goal', 'skills', 'codes', 'assess']
LIST_COLS = ('tools', 'supplies', 'safety')   # optional, math and science only (sequence-write.md, days.csv columns)
LIST_SUBJECTS = ('math', 'science')
NO_HAZARD = 'none'                            # the one word a science safety cell holds when the day was weighed and has no hazard
MAP_COLS = ['source', 'title', 'goals', 'standards', 'unit', 'days', 'decision', 'why', 'order_conflict', 'harms_learning']
MAP_DECISIONS = {'keep', 'split', 'merge', 'cut', 'ours'}
HANDS_ON = re.compile(r'\b(lab|investigat\w*|experiment\w*|dissect\w*|build|builds|built|construct(?:s|ion)?|test(?:s|ing)? '
                      r'(?:the|a|each|their)|heat\w*|burn\w*|mix\w*|measure|measures|demonstrat\w*|hands-on|model(?:s)? with)\b', re.I)


def subject_of(slug):
    """The course's subject id (ela, math, science, social-studies), from data/plans/course-list.csv."""
    r = next((c for c in frame.course_list() if c['id'] == slug), {})
    return (r.get('subject') or '').strip()


def list_cell_fails(lab, col, v):
    """A tools, supplies or safety cell is a `; `-separated list with no empty item."""
    v = v.strip()
    if v and any(not x.strip() for x in v.split(';')):
        return ['%s: %s has an empty item or a stray semicolon (write "a; b; c", empty when none)' % (lab, col)]
    return []


def tool_cols(days, subject):
    """Failures and notes for the optional tools, supplies and safety columns. Math and science only: any other
    subject returns nothing, so a social studies days.csv can never fail here.
    What a script can check: the cells are well-formed lists; a science days.csv that has supplies also has safety;
    every science day that names supplies (physical material in the hands of students) fills safety, with the single
    word none when the day was weighed and has no hazard. days.csv has no hands-on marker, so a day whose goal or
    note reads like hands-on work but names no supplies is a note, not a failure."""
    fails, notes = [], []
    if subject not in LIST_SUBJECTS or not days:
        return fails, notes
    have = [c for c in LIST_COLS if c in days[0]]
    if subject == 'science':
        if not have:
            notes.append('no tools, supplies or safety columns (a science days.csv carries them: sequence-write.md)')
        elif 'supplies' in have and 'safety' not in have:
            fails.append('days.csv has a supplies column and no safety column (science needs both)')
        elif 'safety' in have and 'supplies' not in have:
            fails.append('days.csv has a safety column and no supplies column (science needs both)')
    for d in days:
        lab = 'day %s' % d['day']
        for c in have:
            fails += list_cell_fails(lab, c, d.get(c) or '')
        sup, saf = (d.get('supplies') or '').strip(), (d.get('safety') or '').strip()
        if subject == 'science' and 'safety' in have and 'supplies' in have:
            if sup and not saf:
                fails.append('%s: supplies named and safety empty (write the hazard and control, or "%s")' % (lab, NO_HAZARD))
            if saf.lower() == NO_HAZARD and saf != NO_HAZARD:
                fails.append('%s: safety "%s" must be the lower-case word "%s" alone' % (lab, saf, NO_HAZARD))
            if NO_HAZARD in [x.strip().lower() for x in saf.split(';')] and ';' in saf:
                fails.append('%s: "%s" stands alone in a safety cell, not in a list' % (lab, NO_HAZARD))
            if not sup and not saf and HANDS_ON.search(d['goal'] + ' ' + d.get('note', '')):
                notes.append('%s: reads like hands-on work but names no supplies and no safety' % lab)
    if have and not any((d.get(c) or '').strip() for d in days for c in have):
        notes.append('the %s column(s) are empty on every day' % '/'.join(have))
    return fails, notes


# Fluency mislabels (later.csv L64, 2026-11-17). The goal is the day's plain statement of what it does, so a writing
# verb or a teaching verb there is reliable; "before drafting" and the noun "introduction" are not verbs and do not match.
FLU_FAIL = re.compile(r'(?<!before )\b(draft|drafts|drafting|edit|edits|editing|introduce|introduces|introducing|'
                      r'teach|teaches)\b|\bfor the first time\b', re.I)
WRITING = r'(sentence|paragraph|draft|essay|narrative|argument|explanation|analysis|account|summary|report|letter|retelling|writing|claim)s?'
FLU_REVISE = re.compile(r'\brevis(e|es|ing)\b(\s+\S+){0,3}?\s+%s\b' % WRITING, re.I)
FLU_NOTE = re.compile(r'\b(introduce|introduces|introducing|teach|teaches)\b(?! no\b| or\b)', re.I)
# skip "no new content ..." clauses and another subject's teaching ("Math 7 teaches ... before this day")
FLU_NOTE_NOT = re.compile(r'(\b(no|not|never|nothing|without|before)\b[^.;|]{0,40}'
                          r'|\b(math|ela|science|history|social studies)\b[^.;|]{0,20})$', re.I)


def fluency_checks(days):
    """Failures and notes for Fluency days that first teach (Understanding) or work on a piece of writing
    (Application), by the definitions of docs/GLOSSARY.md (row "teaching day")."""
    fails, notes, seen = [], [], set()
    for d in days:
        codes = [c.strip() for c in d['codes'].split(';') if c.strip()]
        if d['kind'] == 'Fluency':
            lab, goal, note = 'day %s' % d['day'], d['goal'], d.get('note', '')
            m = FLU_FAIL.search(goal)
            if m:
                fails.append('%s: a Fluency day whose goal says "%s" (first teaching is Understanding; drafting, revising '
                             'or editing writing is Application; GLOSSARY "teaching day")' % (lab, m.group(0)))
            else:
                if FLU_REVISE.search(goal):
                    notes.append('%s: Fluency, but the goal revises a piece of writing (Application?)' % lab)
                hits = [x for x in FLU_NOTE.finditer(note) if not FLU_NOTE_NOT.search(note[:x.start()])]
                if hits:
                    notes.append('%s: Fluency, but the note says "%s" (Understanding or Application?)' % (lab, hits[0].group(0)))
            new = [c for c in codes if c not in seen]
            if new:
                notes.append('%s: Fluency, first day in the course for %s (practice of a taught skill, or first '
                             'teaching?)' % (lab, ', '.join(new)))
        seen.update(codes)
    return fails, notes


def rows(course, name):
    p = PLANS / course / (name + '.csv')
    if not p.exists():
        return None
    with io.open(p, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def stage(course):
    """'scope' when only days.csv exists, 'plan' once parts or items exist, None with no days.csv."""
    if rows(course, 'days') is None:
        return None
    return 'plan' if (rows(course, 'parts') or rows(course, 'items')) else 'scope'


def map_days(v):
    out = []
    for part in re.split(r'[;,\s]+', re.sub(r'\s*(-|to)\s*', r'\1', v.strip())):
        if not part:
            continue
        m = re.fullmatch(r'(\d+)(?:-|to)(\d+)', part)
        if m:
            out += list(range(int(m.group(1)), int(m.group(2)) + 1))
        elif part.isdigit():
            out.append(int(part))
        else:
            return None
    return out


def map_fails(course, nunits, ndays):
    """One source-map layout for every subject (lead, 2026-11-15, after the reads found 21 layouts in 21 maps)."""
    p = PLANS / course / 'source-map.csv'
    if not p.exists():
        return []
    with io.open(p, encoding='utf-8', newline='') as fh:
        rd = csv.DictReader(fh)
        head, sm = rd.fieldnames or [], list(rd)
    if head[:len(MAP_COLS)] != MAP_COLS or any(c != 'url' for c in head[len(MAP_COLS):]):
        return ['source-map.csv columns are %s; they must be %s (url may follow; sequence-write.md rule 8)'
                % (','.join(head), ','.join(MAP_COLS))]
    out = []
    for i, r in enumerate(sm, 2):
        lab = 'source-map.csv line %d (%s)' % (i, r['source'])
        if None in r or any(v is None for v in r.values()):
            # a stray comma shifts every cell after it (later.csv L65, Algebra I row 60)
            n = len(head) + len(r.get(None) or []) - sum(v is None for k, v in r.items() if k is not None)
            out.append('%s: %d cells under a %d-column header (quote any comma inside a cell)' % (lab, n, len(head)))
            continue
        if r['decision'] not in MAP_DECISIONS:
            out.append('%s: decision "%s" is not keep, split, merge, cut or ours' % (lab, r['decision']))
        if not r['source'].strip():
            out.append('%s: no source lesson id' % lab)
        u = r['unit'].strip()
        if u and not (re.fullmatch(r'\d+(\.\d+)?', u) and 1 <= int(u.split('.')[0]) <= (nunits or 999)):
            out.append('%s: unit "%s" is not a unit 1 to %d (or <unit>.<n>)' % (lab, u, nunits))
        ds = map_days(r['days'])
        if ds is None:
            out.append('%s: days "%s" is not a day list ("12", "12-13", "12; 14")' % (lab, r['days']))
        elif any(not 1 <= d <= ndays for d in ds):
            out.append('%s: days "%s" fall outside 1 to %d' % (lab, r['days'], ndays))
        elif not ds and r['decision'] != 'cut':
            out.append('%s: no days, and the decision is not cut' % lab)
        if r['decision'] == 'cut' and not r['why'].strip():
            out.append('%s: a cut with no reason in why' % lab)
        if r['decision'] != 'cut' and not u:
            out.append('%s: no unit' % lab)
    return out


def md_fails(md, slug, nunits):
    """The scope and sequence page holds its title and a section per unit (added 2026-11-14: three pages were
    committed empty that day and the gate passed them)."""
    t = md.read_text(encoding='utf-8')
    if not t.strip():
        return ['docs/courses/%s/scope-and-sequence.md is empty' % slug]
    out = []
    if not re.search(r'^#\s+Scope and sequence\b', t, re.M | re.I):
        out.append('docs/courses/%s/scope-and-sequence.md has no "# Scope and sequence: <title>" line' % slug)
    have = {int(m.group(1)) for m in re.finditer(r'^#{2,4}\s+Units?\s+(\d+)\b', t, re.M | re.I)}
    if not have:
        out.append('docs/courses/%s/scope-and-sequence.md has no unit sections ("## Unit 1. ...")' % slug)
    elif nunits:
        miss = [str(n) for n in range(1, nunits + 1) if n not in have]
        if miss:
            out.append('docs/courses/%s/scope-and-sequence.md has no section for unit(s) %s' % (slug, ', '.join(miss)))
    return out


SEP_CCC = [r'asking questions|defining problems', r'developing and using models|models?', r'planning and carrying out|investigations?',
           r'analyzing and interpreting|interpreting data', r'mathematics|computational thinking',
           r'constructing explanations|designing solutions', r'argument from evidence|engaging in argument',
           r'obtaining, evaluating|communicating information', r'patterns?', r'cause and effect',
           r'scale, proportion|scale and proportion', r'systems? and system models|system models?',
           r'energy and matter|flows? of energy', r'structure and function', r'stability and change']


def named_sep_ccc(f):
    """How many of the 8 practices and 7 crosscutting concepts the frame's units table names, read from the C3 /
    "Practices and crosscutting concepts" column (falls back to the whole table when that column is absent)."""
    head = f.get('head') or []
    col = next((h for h in head if h == 'C3' or re.search(r'practices', h, re.I)), None)
    text = ' '.join((r.get(col, '') if col else ' '.join(r.values())) for r in (f.get('table') or []))
    return sum(1 for pat in SEP_CCC if re.search(pat, text, re.I))


def science_coverage_fails(slug, md, f):
    """Science only (L106, sequence-write.md "The files"): the scope ends with a "Practice and crosscutting concept
    coverage" table, one column per practice and concept the frame names, none empty in every row. Applied to a
    course whose scope has the heading, or earth-and-space-science and environmental-science (grades 4 to 8 may
    lack it for now). Day numbers are not verified."""
    if subject_of(slug) != 'science':
        return []
    text = md.read_text(encoding='utf-8') if md.exists() else ''
    m = re.search(r'^#+\s*Practice and crosscutting concept coverage\s*$', text, re.M | re.I)
    if not m and slug not in ('earth-and-space-science', 'environmental-science'):
        return []
    if not m:
        return ['scope-and-sequence.md lacks the section "Practice and crosscutting concept coverage" (sequence-write.md, science)']
    lines = [l for l in text[m.end():].split(chr(10) + '## ')[0].splitlines() if l.strip().startswith('|')]
    if len(lines) < 3:
        return ['"Practice and crosscutting concept coverage" has no table']
    cells = lambda l: [c.strip() for c in l.strip().strip('|').split('|')]
    head, body = cells(lines[0]), [cells(l) for l in lines[2:]]
    out = []
    want = named_sep_ccc(f)
    if len(head) - 1 < want:
        out.append('coverage table has %d practice and concept columns, the frame names %d' % (len(head) - 1, want))
    for i, h in enumerate(head[1:], 1):
        if all(i >= len(r) or r[i].strip().lower() in ('', 'none') for r in body):
            out.append('coverage table column "%s" is empty or none in every row (a practice or concept the frame names '
                       'must be on a day)' % h)
    return out


def check(course):
    fails, notes = [], []
    slug = frame.LEGACY.get(course, course)
    days = rows(course, 'days') or []
    if slug not in frame.found():
        return ['no frame docs/courses/%s/frame.md for this scope and sequence' % slug], notes
    f = frame.parse(slug)
    md = DOCS / slug / 'scope-and-sequence.md'
    if not md.exists():
        fails.append('no docs/courses/%s/scope-and-sequence.md' % slug)
    else:
        fails += md_fails(md, slug, f.get('units') or 0)
        fails += science_coverage_fails(slug, md, f)
        if not re.search(r'^#+\s*Shorter path', md.read_text(encoding='utf-8'), re.M | re.I):
            notes.append('scope-and-sequence.md has no "Shorter path" section (sequence-write.md rule 10, '
                         'added 2026-11-14)')
    if not days:
        return fails + ['days.csv has no rows'], notes
    miss = [c for c in NEED if c not in days[0]]
    if miss:
        return fails + ['days.csv lacks column(s) %s' % ', '.join(miss)], notes
    nums = [int(d['day']) for d in days if d['day'].strip().isdigit()]
    if nums != list(range(1, len(days) + 1)):
        fails.append('days are not numbered 1 to %d in order' % len(days))
    if f.get('days') and len(days) != f['days']:
        fails.append('%d days, the frame says %d' % (len(days), f['days']))
    nunits = f.get('units') or 0
    table = [r for r in (f.get('table') or []) if str(r.get('#', '')).strip().isdigit()]
    want = {r['#'].strip(): int(re.findall(r'\d+', r.get('Days', '0'))[0]) for r in table if re.findall(r'\d+', r.get('Days', ''))}
    got, kinds_in = {}, {}
    for d in days:
        lab = 'day %s' % d['day']
        s = d['stretch'].strip()
        if s == 'C':
            if d['unit'].strip():
                fails.append('%s: a course-level day leaves unit blank' % lab)
        elif not (s.isdigit() and 1 <= int(s) <= nunits):
            fails.append('%s: stretch "%s" is not a unit 1 to %d or C' % (lab, s, nunits))
        else:
            got[s] = got.get(s, 0) + 1
            kinds_in.setdefault(s, []).append(d)
        if d['kind'] not in KINDS:
            fails.append('%s: kind "%s" is not one of %s' % (lab, d['kind'], ', '.join(sorted(KINDS))))
        if d['assess'] not in ASSESS:
            fails.append('%s: assess "%s" is not one of %s' % (lab, d['assess'], ', '.join(sorted(a for a in ASSESS if a))))
        if not d['goal'].strip():
            fails.append('%s: no goal' % lab)
        if d.get('school_day', '').strip() and not d['school_day'].strip().isdigit():
            fails.append('%s: school_day "%s" is not a number' % (lab, d['school_day']))
    for u, n in want.items():
        if got.get(u, 0) != n:
            fails.append('unit %s: %d days, the frame says %d' % (u, got.get(u, 0), n))
    for u, ds in sorted(kinds_in.items(), key=lambda kv: int(kv[0])):
        # a course-level check on the day right after a unit's last day may stand for that unit's end-of-unit
        # assessment, as frames on the pilot shape set it (lead, 2026-11-26, computer science run)
        last = max(int(d['day']) for d in ds)
        after = next((x for x in days if x['day'].strip().isdigit() and int(x['day']) == last + 1), None)
        check_after = after is not None and after['stretch'].strip() == 'C' and after['kind'] == 'Check'
        if not check_after and not any(d['assess'] == 'end' or (d['assess'] == 'observe' and frame.COURSE_META.get(slug, ('', ''))[1] in ('K', '1', '2'))
                   for d in ds):
            fails.append('unit %s: no end-of-unit assessment day (assess = end, or a course-level check the day after '
                         'its last day; K to 2 may use observe)' % u)
        if len(ds) > MID_UNIT_DAYS and not any(d['assess'] == 'mid' for d in ds):
            fails.append('unit %s: %d days and no mid-unit assessment (assess = mid)' % (u, len(ds)))
    # each course-level check is followed by a respond day before the next unit day
    for i, d in enumerate(days):
        if d['stretch'] == 'C' and d['kind'] == 'Check':
            nxt = next((x for x in days[i + 1:] if x['kind'] != 'Check' or x['stretch'] != 'C'), None)
            if nxt is None or not (nxt['stretch'] == 'C' and nxt['kind'] == 'Respond'):
                fails.append('day %s: a course-level check with no respond day after it' % d['day'])
    # readiness timing (Cory, 2026-11-14, sequence-write.md rule 2): a readiness check is given before its unit
    # opens, in the last ten minutes of the previous unit's last day or of a respond day between the two units, a few
    # days ahead at most; never on a unit's first day, with one exception (lead rule 2026-11-14): unit 1's check
    # takes the last ten minutes of course day 1, after the hook
    firsts = {}
    for i, d in enumerate(days):
        s = d['stretch'].strip()
        if s.isdigit() and s not in firsts:
            firsts[s] = i
    starts = sorted(firsts.values())
    for i, d in enumerate(days):
        if d['assess'] != 'readiness':
            continue
        s = d['stretch'].strip()
        if i == 0 and s == '1':
            continue  # unit 1's own check, the last ten minutes of day 1
        if i in starts:
            fails.append("day %s: a readiness check on unit %s's first day (give it before the unit opens: the last "
                         "ten minutes of the previous unit's last day or of the respond day between; unit 1: the "
                         "last ten minutes of day 1)" % (d['day'], s))
            continue
        nxt = next((j for j in starts if j > i), None)
        closes = s == 'C' or d['kind'] == 'Respond' or i + 1 >= len(days) or days[i + 1]['stretch'].strip() != s
        if nxt is None or nxt - i > READINESS_AHEAD or not closes:
            fails.append("day %s: a readiness check that is not on the previous unit's last day or a respond day "
                         "within %d days before a unit's first day" % (d['day'], READINESS_AHEAD))
    fails += map_fails(course, nunits, len(days))
    ff, fn = fluency_checks(days)
    fails += ff
    notes += fn
    tf, tn = tool_cols(days, subject_of(slug))
    fails += tf
    notes += tn
    # every owned skill and code of the frame is placed on some day
    placed = ' '.join(d['skills'] + ' ' + d['codes'] for d in days)
    for r in table:
        for sk in [x.strip() for x in re.split(r'[;,]', r.get('Skills', '')) if x.strip()]:
            if re.fullmatch(r'[\w-]+', sk) and sk not in placed:
                fails.append('unit %s: owned skill %s is on no day' % (r['#'], sk))
        for c in [x.strip() for x in r.get('Owned standards', '').split(';') if x.strip()]:
            c = c.split()[0].lstrip('~')
            if not re.search(r'(?<![\w.-])%s(?![\w-])' % re.escape(c), placed):
                notes.append('unit %s: standard %s is on no day' % (r['#'], c))
    notes += rule2_notes(course, subject_of(slug))
    return fails, notes


def rule2_notes(course, subject):
    """Rule 2 readiness and retrieval (sequence-write.md, "Count by grade number"), counted exactly as the unit
    skeleton counts it (scripts/unit_skeleton.py earlier_rows, one-hop "used"): a note for every unit whose readiness
    check misses a row it owes, and every row given readiness where retrieval is due. Notes, not failures, while the
    count settles (lead, 2026-11-15); the skeleton prints the same lines in field 4."""
    skel_subj = subject
    try:
        import unit_skeleton as u
    except Exception as e:   # the gate never fails on the helper itself
        return ['rule 2 check skipped: %s' % e]
    if skel_subj not in u.SUBJECTS:
        return []
    u.set_subject(skel_subj)
    try:
        prog = u.progression()
        allrows = u.days_rows(course)
        meta = next((r for r in u.read_csv(u.PLANS / 'frames.csv', u.FRAMES_COLS) if r['course'] == course), {})
        byday = {int(r['day']): r for r in allrows}
        out = []
        for unit in sorted({int(r['stretch']) for r in allrows if r['stretch'].isdigit()}):
            rows = [r for r in allrows if r['stretch'] == str(unit)]
            first, rday = int(rows[0]['day']), None
            if first == 1 and rows[0]['assess'] == 'readiness':
                rday = rows[0]
            else:
                for k in range(1, READINESS_AHEAD + 1):
                    p = byday.get(first - k)
                    if p and (p['assess'] == 'readiness' or re.search(r"(unit %d's|next unit's) readiness" % unit, p['note'], re.I)):
                        rday = p
                        break
            for e in u.earlier_rows(course, rows, allrows, prog, meta, rday):
                if e['group'] or 'wants retrieval' in e['off']:
                    out.append('unit %d (rule 2): %s' % (unit, e['off']))
        return out
    except SystemExit as e:   # unit_skeleton.DataError: a data file it cannot read
        return ['rule 2 check skipped: %s' % e]


def main(a):
    if a[:1] != ['check']:
        raise SystemExit(__doc__)
    cs = a[1:2] or [p.name for p in sorted(PLANS.iterdir()) if p.is_dir() and stage(p.name) == 'scope']
    bad = 0
    for c in cs:
        fl, nt = check(c)
        print('sequence %s: %d failure(s)' % (c, len(fl)))
        for x in fl: print('  FAIL', x)
        for x in nt: print('  note', x)
        bad += len(fl)
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main(sys.argv[1:])

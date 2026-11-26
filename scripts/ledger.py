"""The subject ledger: what each grade of a subject actually taught, carried up the ladder.

    python -X utf8 scripts/ledger.py add <subject> <course> <where> <day> <kind> "<entry>" ["<note>"] [--student-word]
    python -X utf8 scripts/ledger.py show <subject> [--before <course>] [--kind <kind>] [--term <text>] [--course <course>]
    python -X utf8 scripts/ledger.py note <subject> <course> <day> "<entry>" "<new note>"
    python -X utf8 scripts/ledger.py check <subject> [--all]
    python -X utf8 scripts/ledger.py settle <subject> <course> [--apply]
    python -X utf8 scripts/ledger.py seed <subject> <units.csv>
    python -X utf8 scripts/ledger.py gate <subject> <course> <first_day> <last_day>
    python -X utf8 scripts/ledger.py recheck <subject> [--all]

Serves every course run (docs/COURSE-RUN.md); first built 2026-11-18 for the science K to 3 ladder test (L81).
One file per course, data/plans/<course>/ledger.csv (consolidation step 4.D; env LEDGER_DIR overrides the plans
folder, for tests); the commands still name a subject, which reads its ladder's courses in ladder order. Every
section writer and day writer in a run reads it (`show`, everything below its own course plus its own course so
far) and adds what it teaches (`add`). Writers never edit the CSV by hand.

Columns: course, where (u01-2, a section, or s01 for a unit-level entry), day (the day number, or blank when planned
for the whole section), kind, entry, note, stage (planned when a section plan adds it, written when a day adds it).
student_word (term rows: yes, no or blank; blank on other kinds): yes when the term is a word a student is taught and
given a definition for, set by the writer with --student-word; a writer's row without the flag is no. Blank means not
judged yet: seed writes blank, and so do the older rows migrated in 4.L (Desk q-student-word-1). The word backlog
(vocabulary.py report) counts only yes rows and prints the blank ones as undecided; most term rows record what a later
day may lean on, for teachers and writers (close review 4).

seed (stage 4): units.csv has columns course, where (s03 for a unit-level entry, or u03-2), kind, entry, note; every
row is added at stage planned in one call; all-or-nothing, refuses bad kinds, courses off the ladder and duplicates.

check: besides the structural problems it prints a separate "citation check": a review note whose cited target exists
only at stage planned must say "planned only"; citations matching no row are listed as their own kind. These do not
change the exit code. A citation follows "review of": a course (full id, or grade-N / kindergarten for the same
subject), a where (u04-1) or a whole unit (u04, unit 4), optional days (day 5, days 3 and 4, days 26 to 29) and
optional words (in brackets, or after a bare course). It matches rows of that course with that where, that day (a
planned row with blank day stands in when the day is not written yet) and those words in entry or note.

gate: a day job for <course> days a..b may start only when every lower-grade (or earlier same-course) entry that the
section rows of those days cite is at stage written (decision 2026-11-21, DESK-ANSWERS "Ledger-gated scheduling").
Exit 0 gate open; 1 blocked (one line per blocker); 2 usage. Citations into the gated sections themselves are exempt.

add with a day promotes a planned row of the same course, where, kind and entry (case and spacing ignored) to
written instead of adding a duplicate; settle cleans up finished courses (see settle).

recheck: every review claim with its target's stage and whether the target's day still exists in days.csv.

Kinds:
- term: a word students are taught to use;
- notation: a symbol or written form;
- model: a picture, diagram or explanation students build;
- case: a phenomenon, example or story used to teach (later grades may revisit it, never as an exit);
- investigation: a hands-on test or observation;
- material: equipment or supplies students handle;
- routine: a classroom routine students learn (a notebook page, a talk move);
- text: a read-aloud, passage or sheet text;
- skill: a practice students do (measure with a ruler, sort by one property);
- none: the day introduces nothing new (a review, practice or test day); the entry says why, one row per such day
  (the index's status report fails a day file with no written row, later L133).
"""
import csv
import io
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import safe_write  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DIR = Path(os.environ['LEDGER_DIR']) if os.environ.get('LEDGER_DIR') else ROOT / 'data' / 'plans'
PLANS = ROOT / 'data' / 'plans'
COLS = ['course', 'where', 'day', 'kind', 'entry', 'note', 'stage', 'student_word']
STUDENT = ('yes', 'no', '')   # term rows: is this a word a student is taught and given a definition for? blank = not judged
KINDS = ('term', 'notation', 'model', 'case', 'investigation', 'material', 'routine', 'text', 'skill', 'none')
sys.path.insert(0, str(ROOT / 'scripts'))
import subjects  # noqa: E402  one home for subject ids and ladders (consolidation 4.H)

LEDGER_SUBJECTS = subjects.CORE
LADDER = subjects.ladders(LEDGER_SUBJECTS)   # each subject's courses in teaching order, from course-list.csv


def path(course):
    """A course's ledger file."""
    return DIR / course / 'ledger.csv'


def exists(subject):
    return any(path(c).exists() for c in LADDER.get(subject, ()))


def course_rows(course):
    p = path(course)
    if not p.exists():
        return []
    return list(csv.DictReader(io.StringIO(safe_write.read_text(p), newline='')))


def rows(subject):
    """Every row of a subject's ladder, course by course in ladder order."""
    return [r for c in LADDER.get(subject, ()) for r in course_rows(c)]


def _write(course, rs):
    """Writes one course's ledger through a temp file and os.replace, so a reader never sees half a file. Callers hold
    safe_write.lock(path(course)) around the read, the change and this write (add, renote, settle, seed)."""
    s = io.StringIO()
    w = csv.DictWriter(s, fieldnames=COLS, lineterminator='\n')
    w.writeheader()
    w.writerows(rs)
    safe_write.replace(path(course), s.getvalue())


def _append(course, new_rows):
    _write(course, course_rows(course) + [dict(zip(COLS, r)) for r in new_rows])


def norm(text):
    return ' '.join(text.casefold().split())


def write_all(subject, rs):
    """Rewrites only the courses whose rows changed."""
    for c in LADDER[subject]:
        mine = [r for r in rs if r['course'] == c]
        if mine != course_rows(c):
            _write(c, mine)


def add(subject, course, where, day, kind, entry, note='', student=False):
    """Holds the course's lock (safe_write) for the whole read, change and write."""
    with safe_write.lock(path(course)):
        return _add(subject, course, where, day, kind, entry, note, student)


def _add(subject, course, where, day, kind, entry, note='', student=False):
    if subject not in LADDER or course not in LADDER[subject]:
        sys.exit('ledger: %s is not on the %s ladder' % (course, subject))
    if kind not in KINDS:
        sys.exit('ledger: kind must be one of %s' % ', '.join(KINDS))
    if day and not day.isdigit():
        sys.exit('ledger: day is a number or blank')
    if not entry.strip():
        sys.exit('ledger: entry is empty')
    if student and kind != 'term':
        sys.exit('ledger: --student-word marks term rows only')
    sw = ('yes' if student else 'no') if kind == 'term' else ''
    if day:
        # A planned row of the same section, kind and entry (written at section-plan time) is promoted, not duplicated.
        rs = rows(subject)
        hit = [r for r in rs if r['course'] == course and r['where'] == where and r['kind'] == kind
               and r['stage'] == 'planned' and norm(r['entry']) == norm(entry)]
        if hit:
            r = hit[0]
            r['day'], r['stage'] = day, 'written'
            if student:
                r['student_word'] = 'yes'
            if note.strip() and note.strip() != r['note']:
                r['note'] = (r['note'] + '; ' + note.strip()) if r['note'] else note.strip()
            write_all(subject, rs)
            print('promoted: %s %s day %s %s: %s' % (course, where, day, kind, entry.strip()))
            return
    stage = 'written' if day else 'planned'
    _append(course, [[course, where, day, kind, entry.strip(), note.strip(), stage, sw]])
    print('added: %s %s day %s %s: %s' % (course, where, day or '-', kind, entry.strip()))


def show(subject, before=None, kind=None, term=None, course=None):
    """--term keeps rows whose entry or note holds the text (any case); --course keeps one course. A whole show runs to
    hundreds of KB and is cut off when read in one piece (science ladder report, 2026-11-19): filter it."""
    order = LADDER[subject]
    stop = order.index(before) if before in order else len(order)
    keep = set(order[:stop + 1]) if before else set(order)
    t = (term or '').lower()
    out = [r for r in rows(subject) if r['course'] in keep and (not kind or r['kind'] == kind)
           and (not course or r['course'] == course) and (not t or t in (r['entry'] + ' ' + r['note']).lower())]
    if not out:
        print('(the %s ledger is empty so far)' % subject)
        return
    cur = None
    for r in sorted(out, key=lambda r: (order.index(r['course']), r['where'], int(r['day'] or 0))):
        if r['course'] != cur:
            cur = r['course']
            print('\n## %s' % cur)
        # The course goes on every line: section names (u02-1) repeat across grades, and a writer who greps for one
        # must not mistake kindergarten's u02-1 for grade 1's (found 2026-11-18, grade 1 unit 3).
        print('- %s %s %s %s: %s%s' % (r['course'], r['where'],('day ' + r['day']) if r['day'] else '(planned)', r['kind'],
                                     r['entry'], (' (' + r['note'] + ')') if r['note'] else ''))


def renote(subject, course, day, entry, note):
    """Holds the course's lock (safe_write) for the whole read, change and write."""
    with safe_write.lock(path(course)):
        return _renote(subject, course, day, entry, note)


def _renote(subject, course, day, entry, note):
    """Correct one row's note (a row tagged new that a lower grade taught, or review that is new): the only edit."""
    rs = rows(subject)
    hit = [r for r in rs if r['course'] == course and r['day'] == day and r['entry'] == entry.strip()]
    if len(hit) != 1:
        sys.exit('ledger note: %d rows match %s day %s "%s"; need exactly one' % (len(hit), course, day, entry))
    hit[0]['note'] = note.strip()
    write_all(subject, rs)
    print('note set: %s day %s %s: %s' % (course, day, entry.strip(), note.strip()))


def settle(subject, course, apply=False):
    """Holds the course's lock (safe_write) for the whole read, change and write."""
    with safe_write.lock(path(course)):
        return _settle(subject, course, apply)


def _settle(subject, course, apply=False):
    """Finished course: a planned row whose course, kind and entry also stand as a written row is a leftover (a day
    writer added a new row instead of moving the planned one). --apply DELETES the planned duplicate: marking it written
    would leave two written rows for one entry, and the written row already carries the day and the real note. Planned
    rows with no written match are only listed (planned, never written); nothing else is changed."""
    if subject not in LADDER or course not in LADDER[subject]:
        sys.exit('ledger settle: %s is not on the %s ladder' % (course, subject))
    rs = rows(subject)
    written = {(r['kind'], norm(r['entry'])) for r in rs if r['course'] == course and r['stage'] == 'written'}
    dup = [r for r in rs if r['course'] == course and r['stage'] == 'planned' and (r['kind'], norm(r['entry'])) in written]
    never = [r for r in rs if r['course'] == course and r['stage'] == 'planned' and (r['kind'], norm(r['entry'])) not in written]
    for r in never[:10] if not apply else []:
        print('  planned, never written: %s %s: %s' % (r['where'], r['kind'], r['entry'][:70]))
    print('%s %s: %d rows; settled (planned duplicate of a written row) %d; planned, never written %d%s' % (
        subject, course, sum(1 for r in rs if r['course'] == course), len(dup), len(never),
        ' (first 10 shown above)' if never and not apply else ''))
    if apply and dup:
        ids = {id(r) for r in dup}
        write_all(subject, [r for r in rs if id(r) not in ids])
        print('applied: deleted %d planned duplicates' % len(dup))
    elif dup:
        print('dry run: nothing changed (--apply deletes the %d duplicates)' % len(dup))
    return 0


def seed(subject, file):
    if subject not in LADDER:
        sys.exit('ledger seed: no ladder for %s' % subject)
    with open(file, encoding='utf-8', newline='') as f:
        src = list(csv.DictReader(f))
    need = {'course', 'where', 'kind', 'entry', 'note'}
    if not src or set(src[0]) != need:
        sys.exit('ledger seed: columns must be course, where, kind, entry, note (and at least one row)')
    have = {(r['course'], r['where'], r['kind'], r['entry'].strip()) for r in rows(subject)}
    errs, out = [], []
    for i, r in enumerate(src, 2):
        r = {k: (v or '').strip() for k, v in r.items()}
        key = (r['course'], r['where'], r['kind'], r['entry'])
        if r['course'] not in LADDER[subject]:
            errs.append('line %d: %s is not on the %s ladder' % (i, r['course'], subject))
        elif r['kind'] not in KINDS:
            errs.append('line %d: unknown kind %s' % (i, r['kind']))
        elif not re.fullmatch(r's\d\d|u\d\d-\d+', r['where']):
            errs.append('line %d: where must look like s03 or u03-2' % i)
        elif not r['entry']:
            errs.append('line %d: entry is empty' % i)
        elif key in have:
            errs.append('line %d: duplicate of an existing or earlier row: %s %s %s' % (i, r['course'], r['where'], r['entry']))
        else:
            have.add(key)
            out.append([r['course'], r['where'], '', r['kind'], r['entry'], r['note'], 'planned',
                        ''])                      # a term row from seed is not judged yet (blank)
    if errs:
        print('\n'.join(errs))
        sys.exit('ledger seed: refused, nothing added (%d problems)' % len(errs))
    for c in LADDER[subject]:
        mine = [r for r in out if r[0] == c]
        if mine:
            with safe_write.lock(path(c)):
                _append(c, mine)
    print('seeded %d planned rows into the %s ledger' % (len(out), subject))


# ---- citations ----------------------------------------------------------------------------------------------------

def _days(text):
    out = []
    for p in re.split(r'\s*(?:,|and|;)\s*', text):
        m = re.fullmatch(r'(\d+)\s*(?:to|-)\s*(\d+)', p.strip())
        if m and 0 <= int(m.group(2)) - int(m.group(1)) < 400:
            out += list(range(int(m.group(1)), int(m.group(2)) + 1))
        elif p.strip().isdigit():
            out.append(int(p))
    return out


def _tokens(subject):
    names = sorted(LADDER[subject], key=len, reverse=True)
    return re.compile('|'.join([
        '(?P<course>' + '|'.join(re.escape(n) for n in names) + r')(?![\w-]*\d)',
        r'\b(?P<short>kindergarten|grade[- ]\d+)\b',
        r'\b(?P<where>u(?P<wu>\d\d)(?:-(?P<ws>\d+))?)\b',
        r'\bunits? (?P<unit>\d+)\b',
        r'\b(?:days?|d)\s?(?P<days>\d+(?:\s*(?:,|and|to|-)\s*\d+)*)',
        r'\((?P<paren>[^)]*)\)']), re.I)


_TOK = {}


def _short_course(subject, text):
    t = text.lower().replace(' ', '-')
    for c in LADDER[subject]:
        if t == 'kindergarten' and c.endswith('kindergarten'):
            return c
        if t.startswith('grade-') and c.endswith('-' + t):
            return c
    return None


def _new(course):
    return {'course': course, 'where': None, 'unit': None, 'days': [], 'words': '', 'bare': True}


def citations(subject, course, note):
    """Targets a note cites after 'review of'. Each: dict(course, where, unit, days, words, text). A bare course (no
    where, unit or days) is filled by the next where or unit; anything else starts a new target."""
    tok = _TOK.setdefault(subject, _tokens(subject))
    out = []
    for m in re.finditer(r'review of ', note):
        seg = re.split(r'review of |;|\.\s|\.$', note[m.end():])[0]
        cur_course, cur, last_end, left = course, None, 0, []
        for t in tok.finditer(seg):
            left.append(seg[last_end:t.start()])
            last_end = t.end()
            g = t.groupdict()
            if g['course'] or g['short']:
                c = g['course'].lower() if g['course'] else _short_course(subject, g['short'])
                if c:
                    cur_course = c
                    cur = _new(c)
                    out.append(cur)
            elif g['where'] or g['unit']:
                if g['where']:
                    wu = int(g['wu'])
                    wh, un = ('u%02d-%s' % (wu, g['ws']), None) if g['ws'] else (None, wu)
                else:
                    wh, un = None, int(g['unit'])
                if cur is None or not cur['bare'] or cur['course'] != cur_course:
                    cur = _new(cur_course)
                    out.append(cur)
                cur['where'], cur['unit'], cur['bare'] = wh, un, False
            elif g['days']:
                if cur is None:
                    cur = _new(cur_course)
                    out.append(cur)
                cur['days'] += _days(g['days'])
                cur['bare'] = False
            elif g['paren'] is not None and cur is not None:
                p = g['paren'].strip()
                if p and not re.match(r'(planned|review|new)', p, re.I) and not p.endswith('.md'):
                    cur['words'] = (cur['words'] + ' ' + p).strip()
        left.append(seg[last_end:])
        # words after a bare course ("english-language-arts-kindergarten rhyming")
        if cur is not None and cur['bare'] and not cur['words']:
            rest = re.sub(r'\b(and|the|of|in|on|at|a|an|to|day|days)\b|[^\w\s-]', ' ', left[-1])
            rest = re.sub(r'\s+', ' ', rest).strip()
            if rest:
                cur['words'] = rest
    for t in out:
        t['text'] = describe(t)
    return out


def describe(t):
    s = t['course']
    if t['where']:
        s += ' ' + t['where']
    elif t['unit'] is not None:
        s += ' unit %d' % t['unit']
    if t['days']:
        s += ' day' + ('s ' if len(t['days']) > 1 else ' ') + ','.join(str(d) for d in t['days'][:6])
    if t['words']:
        s += ' (' + t['words'] + ')'
    return s


def index(rs):
    ix = {}
    for r in rs:
        ix.setdefault(r['course'], []).append(r)
    return ix


def resolve(t, ix):
    """-> (stage, rows): 'written' when any matching row is written, 'planned' when all are, None when none match."""
    cand = ix.get(t['course'], [])
    if t['where']:
        cand = [r for r in cand if r['where'] == t['where']]
    elif t['unit'] is not None:
        cand = [r for r in cand if r['where'] == 's%02d' % t['unit'] or r['where'].startswith('u%02d-' % t['unit'])]
    if t['days']:
        ds = {str(d) for d in t['days']}
        hit = [r for r in cand if r['day'] in ds]
        cand = hit or [r for r in cand if not r['day']] or cand
    if t['words'] and cand:
        w = t['words'].lower()
        hit = [r for r in cand if w in (r['entry'] + ' ' + r['note']).lower()]
        if not hit:
            bits = [x for x in re.findall(r'\w+', w) if len(x) > 3]
            hit = [r for r in cand if any(b in (r['entry'] + ' ' + r['note']).lower() for b in bits)] if bits else []
        cand = hit
    if not cand:
        return None, []
    return ('written' if any(r['stage'] == 'written' for r in cand) else 'planned'), cand


def claims(subject, rs):
    for r in rs:
        if 'review of ' in r['note']:
            yield r, citations(subject, r['course'], r['note'])


def rowname(r):
    return '%s %s %s: %s' % (r['course'], r['where'], ('day ' + r['day']) if r['day'] else '(planned)', r['entry'][:60])


def check(subject, show_all=False):
    rs = rows(subject)
    bad = 0
    for i, r in enumerate(rs, 2):
        if None in r or set(r) != set(COLS):
            print('line %d: wrong cell count' % i)
            bad += 1
        elif r['kind'] not in KINDS or r['course'] not in LADDER[subject]:
            print('line %d: unknown kind or course' % i)
            bad += 1
        elif r['student_word'] not in (STUDENT if r['kind'] == 'term' else ('',)):
            print('line %d: student_word is yes, no or blank on a term row and blank on any other kind' % i)
            bad += 1
    print('%s ledger: %d rows, %d problems' % (subject, len(rs), bad))
    ix = index(rs)
    po, un, nclaims, ntargets = [], [], 0, 0
    for r, ts in claims(subject, rs):
        nclaims += 1
        said = 'planned only' in r['note'].lower()
        for t in ts:
            ntargets += 1
            st, _ = resolve(t, ix)
            if st is None:
                un.append((r, t))
            elif st == 'planned' and not said:
                po.append((r, t))
    print('\n== citation check (added 2026-11-21; does not change the exit code) ==')
    print('review notes: %d, cited targets: %d' % (nclaims, ntargets))
    print('planned-only findings: %d (target only at stage planned, note lacks "planned only")' % len(po))
    print('unmatched citations: %d (no ledger row matches the cited target)' % len(un))
    lim = None if show_all else 8
    for title, lst in (('planned-only', po), ('unmatched', un)):
        for r, t in lst[:lim]:
            print('  %s: %s cites %s' % (title, rowname(r), t['text']))
        if lim and len(lst) > lim:
            print('  ... %d more %s (use --all)' % (len(lst) - lim, title))
    return 1 if bad else 0


def section_where(unit):
    """days.csv unit '3.10' -> ledger where 'u03-10'."""
    a, _, b = unit.partition('.')
    return 'u%02d-%s' % (int(a), b) if a.isdigit() and b.isdigit() else None


def days_of(course):
    """{day number: where} from data/plans/<course>/days.csv, or None when there is no file."""
    p = PLANS / course / 'days.csv'
    if not p.exists():
        return None
    with open(p, encoding='utf-8', newline='') as f:
        return {int(r['day']): section_where(r['unit']) for r in csv.DictReader(f) if r['day'].isdigit()}


def gate(subject, course, first, last):
    if subject not in LADDER or course not in LADDER[subject]:
        sys.exit('ledger gate: %s is not on the %s ladder' % (course, subject))
    if not (first.isdigit() and last.isdigit() and int(first) <= int(last)):
        sys.exit('ledger gate: first_day and last_day are numbers, first <= last')
    dm = days_of(course)
    if dm is None:
        sys.exit('ledger gate: no days.csv for %s' % course)
    a, b = int(first), int(last)
    missing = [d for d in range(a, b + 1) if d not in dm]
    if missing:
        sys.exit('ledger gate: days not in days.csv of %s: %s' % (course, ','.join(map(str, missing[:10]))))
    secs = {dm[d] for d in range(a, b + 1)}
    shown = ','.join(sorted(x or 'course-level' for x in secs))  # check days (unit C) carry no section
    rs = rows(subject)
    mine = [r for r in rs if r['course'] == course and
            ((r['day'] and a <= int(r['day']) <= b) or (not r['day'] and r['where'] in secs))]
    if not mine:
        print('gate closed: %s days %d-%d have no ledger rows (sections %s not seeded)' % (course, a, b, shown))
        return 1
    ix = index(rs)
    seen, blockers = set(), []
    for r in mine:
        for t in citations(subject, course, r['note']):
            own = t['course'] == course and (t['where'] in secs or (
                t['where'] is None and t['unit'] is not None and any(s and s.startswith('u%02d-' % t['unit']) for s in secs)))
            if own:
                continue
            st, _ = resolve(t, ix)
            if st == 'written' or t['text'] in seen:
                continue
            seen.add(t['text'])
            blockers.append('blocked: %s is %s (cited by %s)' % (t['text'], 'planned only' if st else 'not in the ledger', rowname(r)))
    if blockers:
        print('\n'.join(blockers))
        print('gate closed: %s days %d-%d, %d blockers' % (course, a, b, len(blockers)))
        return 1
    print('gate open: %s days %d-%d (%d rows, sections %s)' % (course, a, b, len(mine), shown))
    return 0


def recheck(subject, show_all=False):
    tally, lines = recheck_tally(subject, show_all)
    if not show_all and len(lines) > 40:
        lines = lines[:40] + ['... %d more (use --all)' % (len(lines) - 40)]
    print('\n'.join(lines))
    print('%s recheck: %d citations; target written %d, planned only %d, unmatched %d; target day gone %d; flagged %d' % (
        subject, tally['citations'], tally['written'], tally['planned'], tally['unmatched'], tally['gone'],
        tally['flagged']))
    return 1 if tally['flagged'] else 0


def recheck_tally(subject, show_all=False):
    """The recheck counts as data ({citations, written, planned, unmatched, gone, flagged}) and its lines; the
    Dashboard's quality panel reads the counts (plan_flow.py health, review change 4)."""
    rs = rows(subject)
    ix = index(rs)
    dcache, cnt, n, gone, flagged, lines = {}, {'written': 0, 'planned': 0, None: 0}, 0, 0, 0, []
    for r, ts in claims(subject, rs):
        for t in ts:
            n += 1
            st, hit = resolve(t, ix)
            cnt[st] += 1
            ok = st == 'written' or (st == 'planned' and 'planned only' in r['note'].lower())
            extra = ''
            if st:
                days = {int(x['day']) for x in hit if x['day']} | set(t['days'])
                if days:
                    if t['course'] not in dcache:
                        dcache[t['course']] = days_of(t['course'])
                    dm = dcache[t['course']]
                    lost = sorted(d for d in days if dm is not None and d not in dm)
                    if dm is None:
                        extra = ' (no days.csv)'
                    elif lost:
                        gone += 1
                        ok = False
                        extra = ' (day no longer in days.csv: %s)' % ','.join(map(str, lost[:6]))
            flagged += 0 if ok else 1
            if show_all or not ok:
                lines.append('%s | cites %s -> %s%s' % (rowname(r), t['text'], st or 'unmatched', extra))
    return dict(citations=n, written=cnt['written'], planned=cnt['planned'], unmatched=cnt[None], gone=gone,
                flagged=flagged), lines


def self_test():
    """Four processes add ten rows each to one course's ledger at once: all forty must land (4.E2 race test)."""
    import subprocess
    import tempfile
    d = Path(tempfile.mkdtemp())
    c = LADDER['science'][0]
    (d / c).mkdir()
    (d / c / 'ledger.csv').write_text(','.join(COLS) + '\n', encoding='utf-8')
    env = dict(os.environ, LEDGER_DIR=str(d))
    script = ('import sys; sys.argv[0] = %r; sys.path.insert(0, %r); import ledger\n'
              'for i in range(10): ledger.add("science", %r, "u01-1", "", "term", "race-%%s-%%d" %% (sys.argv[1], i))'
              % (__file__, str(Path(__file__).parent), c))
    procs = [subprocess.Popen([sys.executable, '-X', 'utf8', '-c', script, str(k)], env=env, stdout=subprocess.DEVNULL)
             for k in range(4)]
    codes = [x.wait() for x in procs]
    with open(d / c / 'ledger.csv', encoding='utf-8', newline='') as f:
        got = [r for r in csv.DictReader(f) if r['entry'].startswith('race-')]
    left = sorted(x.name for x in (d / c).iterdir() if x.name != 'ledger.csv')
    ok = codes == [0] * 4 and len(got) == 40 and not left
    print('ledger self-test: %s (exit codes %s, %d of 40 rows, leftovers %s)' % (
        'all passed' if ok else 'FAILED', codes, len(got), left or 'none'))
    return 0 if ok else 1


def main(a):
    if a == ['--self-test']:
        return self_test()
    if a == ['files']:
        # every ledger file on disk belongs to a ladder course, so none can sit unchecked (4.E2)
        known = {c for cs in LADDER.values() for c in cs}
        stray = sorted(p.parent.name for p in DIR.glob('*/ledger.csv') if p.parent.name not in known)
        print('\n'.join('stray ledger: data/plans/%s/ledger.csv (course not on a ladder)' % c for c in stray))
        print('ledger files: %d on disk, %d stray' % (len(list(DIR.glob('*/ledger.csv'))), len(stray)))
        return 1 if stray else 0
    if not a or a[0] not in ('add', 'show', 'check', 'note', 'seed', 'gate', 'recheck', 'settle'):
        print(__doc__)
        return 2
    if a[0] == 'add':
        student = '--student-word' in a
        a = [x for x in a if x != '--student-word']
        if len(a) not in (7, 8):
            sys.exit('ledger add: subject course where day kind entry [note] [--student-word]')
        add(*a[1:8], student=student)
        return 0
    if a[0] == 'note':
        if len(a) != 6:
            sys.exit('ledger note: subject course day entry note')
        renote(*a[1:6])
        return 0
    if a[0] == 'settle':
        if len(a) not in (3, 4) or (len(a) == 4 and a[3] != '--apply'):
            sys.exit('ledger settle: subject course [--apply]')
        return settle(a[1], a[2], len(a) == 4)
    if a[0] == 'seed':
        if len(a) != 3:
            sys.exit('ledger seed: subject units.csv')
        seed(a[1], a[2])
        return 0
    if a[0] == 'gate':
        if len(a) != 5:
            sys.exit('ledger gate: subject course first_day last_day')
        return gate(*a[1:5])
    if len(a) < 2 or a[1] not in LADDER:
        sys.exit('ledger %s: subject (%s)' % (a[0], ', '.join(LADDER)))
    if a[0] in ('check', 'recheck'):
        return (check if a[0] == 'check' else recheck)(a[1], '--all' in a)
    flags = dict(zip(a[2::2], a[3::2])) if len(a) > 2 else {}
    show(a[1], flags.get('--before'), flags.get('--kind'), flags.get('--term'), flags.get('--course'))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

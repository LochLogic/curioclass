"""Lesson days: check each day file against docs/courses/LESSON-DAY.md and build its print pages.

    python -X utf8 scripts/lesson.py check            every day file under courses/; exit 1 on any failure
    python -X utf8 scripts/lesson.py build [--pdf]    write the pages to build/lessons/ (--pdf also prints the
                                                      student page with Chrome and counts its sides)

A day file is courses/<course>/u<stretch>-<unit>/d<day>.md: a header block, "## Teacher page" with fixed
headings, then "## Student page". Questions are named by id, [[s11-P90-1]], and live in
data/plans/<course>/items.csv with their computed keys (scripts/plan.py). Nothing here types a key.
"""
import html, re, subprocess, sys, os, time
from fractions import Fraction
from pathlib import Path

import markdown

sys.path.insert(0, str(Path(__file__).resolve().parent))
import plan  # noqa: E402

ROOT = plan.ROOT
COURSES = ROOT / 'courses'
OUT = ROOT / 'build' / 'lessons'
DAY_MIN = plan.DAY_MIN
HEADER = ['day', 'course', 'unit', 'version', 'materials', 'print', 'credit', 'leans_on']
TEACHER = ['Before class', 'The day', 'Other rooms', 'Shorter or longer', 'Words and supports', 'Tomorrow', 'Credit']
CAP_TEACH, CAP_CHECK, CAP_BEFORE, CAP_STUDENT = 900, 500, 80, 350   # student: everything printed, stems included
SENTENCE_MAX = 15            # words in one student sentence, grades 3 to 5 (ours, untested)
BAD_LICENCE = re.compile(r'\bnc\b|noncommercial|non-commercial|sharealike|share-alike|-sa\b|\bnd\b|-nd\b|'
                         r'noderivatives|no derivatives', re.I)
REF = re.compile(r'\[\[([A-Za-z0-9-]+)\]\]')
STEPS = re.compile(r'\[\[steps:([A-Za-z0-9-]+)\]\]')
NOTE = re.compile(r'\[\[note:([A-Za-z0-9-]+)\]\]')   # a short form for a table: who, and the numbers given
FIG = re.compile(r'\[\[fig:([A-Za-z0-9-]+)\]\]')     # the row's figure, drawn where it stands (a fix: their picture)
CHROME = Path(r'C:\Program Files\Google\Chrome\Application\chrome.exe')


# ------------------------------------------------------------------ reading a day file
def parse(path):
    t = path.read_text(encoding='utf-8')
    m = re.match(r'---\n(.*?)\n---\n(.*)', t, re.S)
    if not m:
        return None
    head = {}
    for line in m[1].splitlines():
        k, _, v = line.partition(':')
        head[k.strip()] = v.strip()
    body = m[2]
    teacher, _, student = body.partition('\n## Student page\n')
    teacher = teacher.split('\n## Teacher page\n', 1)[-1]
    title = re.search(r'^# (.+)$', body, re.M)
    secs = dict(re.findall(r'^### (.+?)\n(.*?)(?=^### |\Z)', teacher, re.M | re.S))
    blocks = [(int(a), b.strip(), c) for a, b, c in
              re.findall(r'^#### (\d+) min\. (.+?)\n(.*?)(?=^#### |^### |\Z)', secs.get('The day', ''), re.M | re.S)]
    sides = re.findall(r'^### (Side \d)\n(.*?)(?=^### |\Z)', student, re.M | re.S)
    return dict(path=path, head=head, title=title[1] if title else '', teacher=teacher, student=student,
                order=re.findall(r'^### (.+)$', teacher, re.M), secs=secs, blocks=blocks, sides=sides)


def words(md):
    """Prose words a person reads: no ids, no blanks, no table rules, no markup, no bare numbers or signs."""
    md = FIG.sub(' ', NOTE.sub(' ', STEPS.sub(' ', REF.sub(' ', md))))
    md = re.sub(r'<[^>]+>', ' ', md)   # HTML tags and their attributes are markup, not words
    md = re.sub(r'_{2,}|\{sketch\}|\{work\}|\{small\}|\{tall\}|^\|[-| ]+\|$|[#*|>`]', ' ', md, flags=re.M)
    return sum(1 for w in md.split() if re.search(r'[A-Za-z]', w))   # words, not numerals or signs


def day_files():
    return sorted(COURSES.glob('*/u*/d[0-9][0-9][0-9].md'))


def tool_title(folder):
    p = ROOT / 'tools' / folder / 'spec.md'
    if p.exists():
        m = re.match(r'# (.+)', p.read_text(encoding='utf-8'))
        if m:
            return m[1].strip()
    return folder


def grade(course):
    m = re.search(r'(\d+)$', course)
    return int(m[1]) if m else None


def course_name(course):
    subj, _, g = course.rpartition('-')
    return 'grade %s %s' % (g, {'ela': 'English language arts'}.get(subj, subj))


def defaults_cap(course):
    """The student reading cap a course sets in its DEFAULTS.md ("student page ... 350 words"), else the default."""
    p = ROOT / 'docs' / 'courses' / course / 'DEFAULTS.md'
    m = re.search(r'[Ss]tudent page[^.]*?(\d+) words', p.read_text(encoding='utf-8')) if p.exists() else None
    return int(m[1]) if m else CAP_STUDENT


WHEN = 'when it exists:'


def leans(d):
    """Every outside piece the day needs; "when it exists: path" is a piece the day uses only once it is built."""
    return [x.strip() for x in d['head'].get('leans_on', '').split(';') if x.strip() and x.strip() != 'nothing']


def optional(d):
    return [x[len(WHEN):].strip() for x in leans(d) if x.lower().startswith(WHEN)]


def missing(d):
    """Pieces the day cannot be taught without that do not exist ("when it exists" pieces are not counted)."""
    return [x for x in leans(d) if not x.lower().startswith(WHEN) and not (ROOT / x).exists()]


def stem_words(d, byid):
    """Words a student reads in the questions printed on the student page."""
    return (sum(words(stem(byid[r])) for r in REF.findall(d['student']) if r in byid) +
            sum(words(note(byid[r])) for r in NOTE.findall(d['student']) if r in byid and byid[r].get('figure')))


def sentences(text):
    return [s for s in re.split(r'(?<=[.?!])\s+', text.replace('"', '')) if s.strip()]


# ------------------------------------------------------------------ the gates
def check_day(d, items, days):
    f, h, lab = [], d['head'], d['path'].relative_to(ROOT).as_posix()
    for k in HEADER:
        if not h.get(k):
            f.append('%s: header field "%s" is missing' % (lab, k))
    row = next((x for x in days if x['day'] == h.get('day')), None)
    if row is None:
        return f + ['%s: day %s has no row in days.csv' % (lab, h.get('day'))]
    if row['unit'] != h.get('unit'):
        f.append('%s: unit %s, but days.csv says %s' % (lab, h.get('unit'), row['unit']))
    want = TEACHER
    got = [s for s in d['order'] if s in want]
    if got != want:
        f.append('%s: teacher headings should be %s in that order; found %s' % (lab, ', '.join(want), ', '.join(d['order'])))
    check_day_kind = row['kind'] == 'Check'
    # minutes
    tot = sum(b[0] for b in d['blocks'])
    if tot != DAY_MIN:
        f.append('%s: the parts of the day add to %d minutes, not %d' % (lab, tot, DAY_MIN))
    if not check_day_kind:
        names = [b[1] for b in d['blocks']]
        k = next((i for i, n in enumerate(names) if n.lower().startswith('warm-up')), -1)
        if row['opens_min']:   # the opening may be one part or several in a row (a respond half, then teaching)
            run, want = 0, int(row['opens_min'])
            for b in d['blocks'][k + 1:]:
                run += b[0]
                if run >= want:
                    break
            if run != want:
                f.append('%s: the parts after the warm-up do not add to the opening\'s %s min in days.csv'
                         % (lab, row['opens_min']))
    elif row.get('check_min'):   # a check day's parts follow check_min, in order ("end check 30; respond 20; ...")
        want = [int(re.findall(r'\d+', re.sub(r'\(.*?\)', '', s))[-1]) for s in row['check_min'].split(';')
                if re.findall(r'\d+', re.sub(r'\(.*?\)', '', s))]
        got = [b[0] for b in d['blocks']]
        if got != want:
            f.append('%s: the parts run %s min; days.csv check_min says %s' % (lab, got, want))
    # Tomorrow: the next day by number, in any unit folder of the course, must carry the hand-off ("day N" in it)
    nxt = int(h.get('day', 0) or 0) + 1
    tm = d['secs'].get('Tomorrow', '')
    nf = next(iter(sorted(d['path'].parent.parent.glob('u*/d%03d.md' % nxt))), None)
    if re.search(r'\bday %d\b' % nxt, tm, re.I) and nf and not re.search(
            r'\bday %d\b' % (nxt - 1), nf.read_text(encoding='utf-8'), re.I):
        f.append('%s: "Tomorrow" sends work to day %d, but %s never names day %d'
                 % (lab, nxt, nf.relative_to(ROOT).as_posix(), nxt - 1))
    if nf and re.search(r'\bday %d\b' % nxt, tm, re.I):
        nt = nf.read_text(encoding='utf-8')
        # each error letter "Tomorrow" sends must be picked up by name in the next day (expert, day 81 and 82)
        for L in sorted({a or b for a, b in re.findall(r'\berror ([A-H])\b|\(([A-H])\)', tm)}):
            pat = (r'\berror A\b|\(A\)|\bA\b(?= and| or|,|\)| group| pile| students)|(?:and|or|,) A\b' if L == 'A'
                   else r'\b%s\b' % L)
            if not re.search(pat, nt):
                f.append('%s: "Tomorrow" sends error %s to day %d, which never names it' % (lab, L, nxt))
        # a seating promise ("sit near you") must be kept on the next day (expert, days 84 and 85)
        if re.search(r'near you', tm, re.I) and not re.search(r'near you', nt, re.I):
            f.append('%s: "Tomorrow" seats students near you on day %d, which never says so' % (lab, nxt))
    # a teacher-judged practice row (a written task) goes back the next day, unless it stays with students
    if nf:
        nt = nf.read_text(encoding='utf-8')
        for i in items:
            if (i['day'] == h.get('day') and i['check'] == 'practice' and i['judged'] == 'teacher'
                    and '[[%s]]' % i['item_id'] in d['teacher']
                    and not re.search(r'stay with (?:the )?students|not collected', d['teacher'], re.I)
                    and not re.search(re.escape(i['item_id']) + r'|written task', nt, re.I)):
                f.append('%s: the written task %s is judged but day %d never hands it back' % (lab, i['item_id'], nxt))
    # a part that promises the answers on the display must build that screen (a Check: line or a partner check)
    for _, bname, btxt in d['blocks']:
        if (re.search(r'display shows the answers', btxt, re.I) and not re.search(r'^Check(?: \(sort\))?: ', btxt, re.M)
                and not re.search(r'swap and check|swap and compare|partner check|check their own|partners check', btxt, re.I)
                and not re.search(r'=\s*\?', btxt)):
            f.append('%s: "%s" says the display shows the answers but has no Check: line to build that screen' % (lab, bname))
        # a warm-up asks questions; every question is a row (rule 1), so the warm-up names one
        if (not check_day_kind and bname.lower().startswith('warm-up') and not REF.search(btxt)
                and not re.search(r'facts check|sheet|count aloud', btxt, re.I)):
            f.append('%s: the warm-up names no [[id]]; its questions must be rows (rule 1)' % lab)
    # list numbers on the student page never repeat inside a side (a restart after a line printed 1, 2, 3 twice)
    for side, body in d['sides']:
        ns = [int(n) for n in re.findall(r'^(\d+)\.\s', body, re.M)]
        if len(ns) != len(set(ns)):
            f.append('%s: %s numbers its questions %s; a number repeats' % (lab, side, ns))
    # the student page: one numbered question a line; room for every sketch asked for
    for ln in d['student'].splitlines():
        if not ln.lstrip().startswith('|') and len(re.findall(r'(?:^|\s)\d+\.\s+\[\[', ln)) > 1:
            f.append('%s: two numbered questions on one student line print as a broken list: %s' % (lab, ln.strip()[:50]))
    for side, body in d['sides']:
        for chunk in re.split(r'\n(?=\*\*)', body):
            # the goal line ("**I can ...**") and a bold label are not asks; only the words under them are
            ask = re.sub(r'^\*\*I can .*?\*\*\s*$', ' ', chunk, flags=re.M)
            ask = re.sub(r'\*\*[^*\n]+\*\*', ' ', ask)
            if (re.search(r'\b(sketch|draw)\b', ask, re.I) and not re.search(r'\{sketch\}|\{work\}|\{small\}|\{tall\}|\[\[fig:', chunk)
                    and not re.search(r'grid paper|\bback\b|notebook|strip sheet', chunk, re.I)):
                f.append('%s: %s asks for a sketch or a drawing with no box for it: %s' % (lab, side, chunk.strip()[:40]))
    # a wide student table must leave each writing column at least half an inch
    for tb in re.findall(r'^\|.*\|$', d['student'], re.M):
        n = tb.count('|') - 1
        if n > 3 and 7.3 * 0.8 / (n - 1) < 0.5:
            f.append('%s: a student table of %d columns leaves its columns under half an inch' % (lab, n))
            break
        if row['tool']:
            tt = tool_title(row['tool'])
            tm = sum(b[0] for b in d['blocks'] if tt in b[1])
            if tm != int(row['tool_min'] or 0):
                f.append('%s: parts naming %s add to %d min; days.csv says %s' % (lab, tt, tm, row['tool_min']))
    # caps
    tw = words(d['teacher'])
    cap = CAP_CHECK if check_day_kind else CAP_TEACH
    if tw > cap:
        f.append('%s: teacher page is %d words of prose; the cap is %d' % (lab, tw, cap))
    bw = words(d['secs'].get('Before class', ''))
    if bw > CAP_BEFORE:
        f.append('%s: "Before class" is %d words; the cap is %d' % (lab, bw, CAP_BEFORE))
    byid = {i['item_id']: i for i in items}
    sw = words(d['student']) + stem_words(d, byid)
    scap = defaults_cap(h.get('course', ''))
    if sw > scap:
        f.append('%s: student page is %d words a student reads (frame and questions); the cap is %d' % (lab, sw, scap))
    g = grade(h.get('course', ''))
    if g is not None and 3 <= g <= 5:
        for r in sorted(set(REF.findall(d['student']))):
            for s in sentences(stem(byid[r]) if r in byid else ''):
                if words(s) > SENTENCE_MAX:
                    f.append('%s: a sentence in %s is %d words; grades 3 to 5 keep to %d' % (lab, r, words(s), SENTENCE_MAX))
    for s in TEACHER:
        if s in d['secs'] and words(d['secs'][s]) < 4:
            f.append('%s: "%s" has nothing under it' % (lab, s))
    gone = missing(d)
    if gone and 'not ready' not in h.get('version', '').lower():
        f.append('%s: leans on %s, which does not exist; build it or mark the version "not ready"' % (lab, ', '.join(gone)))
    if optional(d) and 'exists' not in re.sub(r'^---.*?---', '', d['teacher'], flags=re.S):
        f.append('%s: leans_on has a "when it exists" piece, but the teacher page names no fallback for it' % lab)
    if not d['sides'] or len(d['sides']) > 2:
        f.append('%s: the student page needs "### Side 1" (and at most "### Side 2")' % lab)
    # questions
    figs = FIG.findall(d['teacher'] + d['student'])
    refs = (REF.findall(d['teacher'] + d['student']) + STEPS.findall(d['teacher']) + NOTE.findall(d['student'])
            + figs)
    for r in NOTE.findall(d['student']):
        if r in byid and not byid[r].get('figure'):
            f.append('%s: [[note:%s]] needs a figure cell to print from' % (lab, r))
    for r in figs:
        if r in byid and not byid[r].get('figure'):
            f.append('%s: [[fig:%s]] needs a figure cell to draw from' % (lab, r))
    for r in refs:
        if r not in byid:
            f.append('%s: [[%s]] has no row in items.csv' % (lab, r))
        elif byid[r]['day'] != h.get('day'):
            f.append('%s: [[%s]] belongs to day %s' % (lab, r, byid[r]['day']))
    pieces = ''.join(q.read_text(encoding='utf-8') for q in d['path'].parent.glob('*.md') if not re.match(r'd\d{3}$', q.stem))
    for i in items:
        if i['day'] == h.get('day') and i['check'] in plan.LESSON_KINDS | {'exit'} and i['item_id'] not in refs:
            if i.get('path') in ('board', '') and '[[%s]]' % i['item_id'] in pieces:
                continue   # a board row printed by the unit's sheet piece, or a fixed practice sheet's row
            if i.get('path') == 'spare':
                continue   # kept in data (a later day may cite it), printed on no page
            if i['check'] == 'tool' and re.search(r'\bexists\b', d['teacher'], re.I):
                continue   # the tool's own numbers, asked by the tool once it is built
            f.append('%s: %s is a row for this day that no page uses' % (lab, i['item_id']))
    # two worked examples of one day drawn from the same first strip share one scale, so their lengths compare
    # (expert, day 86: 48 and 14 printed the same length)
    exs = [byid[r] for r in dict.fromkeys(refs) if r in byid and byid[r]['check'] == 'example'
           and figures(byid[r]) and figures(byid[r])[0].startswith('strip')]
    for k, a in enumerate(exs):
        for b in exs[k + 1:]:
            try:
                fa, fb = strip_bars(figures(a)[0])[0], strip_bars(figures(b)[0])[0]
            except ValueError:
                continue
            if (fa[0], fa[1][0]) == (fb[0], fb[1][0]) and strip_scale(figures(a)[0]) != strip_scale(figures(b)[0]):
                f.append('%s: %s and %s start from the same strip but are drawn to different scales; give both '
                         'the same scale=' % (lab, a['item_id'], b['item_id']))
    # every number in a figure is in its stem, so the picture and the words agree
    for r in sorted(set(refs)):
        i = byid.get(r)
        if i and i.get('figure'):
            for k, spec in enumerate(figures(i)):
                # the problem's picture keeps to its stem; a fix's right picture may use the right working too; a
                # worked example's picture shows the working, so it may use its answer and steps (day 2: 24 drawn
                # as the 4 by 6 at the turn); the display holds it back until the step that draws it
                ex = i['check'] == 'example'
                sn = set(plan.numbers(i['stem'] + (' ' + i.get('steps', '') if k or ex else '')
                                      + (' ' + i['answer'] if ex else '')))
                if spec.startswith('strip'):
                    try:
                        fv = strip_numbers(spec)
                    except ValueError as e:
                        f.append('%s: %s figure: %s' % (lab, r, e)); continue
                else:
                    fv = [v for kk, v in (x.split('=', 1) for x in spec.split()[1:] if '=' in x) if kk in ('l', 'w', 'A', 'P')]
                for v in fv:
                    if v != '?' and v.replace('_', ' ') not in sn:
                        f.append('%s: %s figure has %s, which its %s does not say'
                                 % (lab, r, v.replace('_', ' '), 'working' if k else 'stem, answer or steps' if ex
                                    else 'stem'))
    for r in set(REF.findall(d['student'])):
        if r in byid and byid[r]['check'] == 'exit':
            f.append('%s: exit question %s is printed on the student page; it belongs on the slip' % (lab, r))
    # credit
    c = h.get('credit', '').lower()
    if c != 'ours' and not ('adapted' in c and 'http' in c and re.search(r'cc by|cc0|public domain', c)):
        f.append('%s: credit must be "ours" or say "adapted from" with the licence (CC BY, CC0 or public domain) '
                 'and a link' % lab)
    adapted = c.split('informed by')[0]
    if BAD_LICENCE.search(adapted):
        f.append('%s: a NonCommercial, ShareAlike or NoDerivatives source cannot be adapted (Curio Class content is '
                 'CC BY 4.0)' % lab)
    for r in sorted(set(refs)):
        s = byid.get(r, {}).get('source', '')
        if s and (BAD_LICENCE.search(s) or 'http' not in s or not re.search(r'cc by|cc0|public domain', s, re.I)):
            f.append('%s: %s has a source that is not CC BY, CC0 or public domain with a licence link' % (lab, r))
    return f


# ------------------------------------------------------------------ building the pages
CSS = """
@page { size: letter; margin: 0.5in; }
body { font-family: Georgia, 'Times New Roman', serif; color: #000; background: #fff; margin: 0 auto; max-width: 7.3in; }
body.student { font-size: 14pt; line-height: 1.45; } body.large { font-size: 18pt; }
body.teacher, body.key { font-size: 11pt; line-height: 1.4; }
h1 { font-size: 1.4em; margin: 0 0 .3em; } h2 { font-size: 1.15em; margin: 1em 0 .3em; } h3, h4 { font-size: 1em; margin: .9em 0 .2em; }
table { border-collapse: collapse; width: 100%; margin: .4em 0; } th, td { border: 1px solid #000; padding: .3em .4em; vertical-align: top; text-align: left; }
.student td { height: 2em; padding: .2em .4em; } .student p { margin: .45em 0; } .sketch { border: 1px dashed #000; height: 0.9in; margin: .3em 0; }
.side { page-break-after: always; } .side:last-child { page-break-after: auto; }
.q { font-style: normal; } .blank { display: inline-block; border-bottom: 1px solid #000; height: 1em; vertical-align: baseline; }
.student table.narrow td:first-child { width: 30%; } .student table.narrow td:nth-child(2) { width: 42%; }
.student table.wide td:first-child { width: 27%; }
.student table.sets td:first-child { width: 40%; } .student table.sets td:nth-child(2) { width: 50%; } .student table.sets td { height: 2em; }
.frac { display: inline-flex; flex-direction: column; vertical-align: middle; text-align: center; font-size: .78em; line-height: 1.05; margin: 0 .08em; }
.frac > span:first-child { border-bottom: 1px solid #000; } .meta td:first-child { width: 22%; font-weight: bold; }
.slip { border: 1px dashed #000; height: 4.6in; width: 48%; display: inline-block; box-sizing: border-box; padding: .2in; margin: 0 1% .2in 0; vertical-align: top; font-size: 12pt; overflow: hidden; } .slip p { margin: .35em 0; } .slip .foot { font-size: 8pt; margin-top: .3em; padding-top: .2em; }
.screen { min-height: 90vh; font-size: 30pt; line-height: 1.35; page-break-after: always; padding: .3in; border-bottom: 2px solid #000; }
.warn { border: 2px solid #000; padding: .4em; font-weight: bold; }
.screen svg { display: block; max-width: 100%; margin: .3em 0; } .screen li { color: #555; } .screen li.now { color: #000; font-weight: bold; }
.pair { display: flex; gap: .4in; } .pair > div { flex: 1; border: 2px solid #000; padding: .2in; }
.sketch.work { height: 0.8in; } .sketch.small { height: 0.5in; } .sketch.tall { height: 1.5in; } .slip .sketch { height: 1.3in; } .slip .sketch.tall { height: 1.5in; }
.foot { font-size: 9pt; margin-top: 1em; border-top: 1px solid #000; padding-top: .3em; }
"""


def nkey(i):
    """A row's n in natural order: '2' before '10', and '9.1a', '9.1b', '9.2a' (stretch 9's end numbers)."""
    return [(0, int(x), '') if x.isdigit() else (1, 0, x) for x in re.findall(r'\d+|[^\d.]+', i.get('n') or '0')]


def put(path, text, encoding='utf-8'):
    """Write a built file only when its text changed, so an unchanged page keeps its date and its PDF is not
    printed again."""
    if not (path.exists() and path.read_text(encoding=encoding) == text):
        path.write_text(text, encoding=encoding)


def page(title, body, cls):
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" '
            'content="width=device-width,initial-scale=1"><title>%s</title><style>%s</style></head>'
            '<body class="%s">%s</body></html>' % (html.escape(title), CSS, cls, body))


def stem(i):
    s = i['stem'].strip()
    return s[1:-1] if s.startswith('"') and s.endswith('"') and s.count('"') == 2 else s


def steps(i):
    return [s.strip() for s in (i.get('steps') or '').split('|') if s.strip()]


def stacked(s):
    """A question for a student: '6 3/4' as a whole number beside a stacked fraction (HTML)."""
    s = html.escape(s, quote=False)
    fr = lambda n, d: '<span class="frac"><span>%s</span><span>%s</span></span>' % (n, d)
    s = re.sub(r'\b(\d+) (\d+)/(\d+)\b', lambda m: '%s%s' % (m[1], fr(m[2], m[3])), s)
    return re.sub(r'(?<![\d/])(\d+)/(\d+)\b', lambda m: fr(m[1], m[2]), s)


def tables(h):
    """Student tables: two or three columns keep the notes-table widths; wider ones share the width evenly, and a
    first row whose cells after the first are empty is a row to write in, not a bold header."""
    def one(m):
        tb = m[0]
        n = len(re.findall(r'<th', tb.split('</tr>', 1)[0]))
        head = tb.split('</tr>', 1)[0]
        kind = 'sets' if '✓' in head or '>Write it' in head else ('narrow' if n <= 3 else 'wide')   # a set table: item, write it, tick
        tb = tb.replace('<table>', '<table class="%s">' % kind, 1)
        hd = re.search(r'<thead>\s*<tr>(.*?)</tr>\s*</thead>', tb, re.S)
        if hd and n > 3 and all(not re.sub(r'<.*?>', '', c).strip() for c in re.findall(r'<th[^>]*>(.*?)</th>', hd[1], re.S)[1:]):
            row = re.sub(r'<th([^>]*)>', r'<td\1>', hd[1]).replace('</th>', '</td>')
            tb = tb.replace(hd[0], '').replace('<tbody>', '<tbody><tr>%s</tr>' % row, 1)
        return tb
    return re.sub(r'<table>.*?</table>', one, h, flags=re.S)


def md(text, items, teacher=False):
    """Day-file markdown to HTML. [[id]] prints the question, upright (and on the teacher page its answer; on a
    student page its fractions stacked); [[steps:id]] prints the worked steps from the row, the same cell the
    display reveals."""
    byid = {i['item_id']: i for i in items}

    def sub(m):
        i = byid.get(m[1])
        if not i:
            return m[0]
        if not teacher:
            return stacked(stem(i))
        return stem(i) + (' **[%s]**' % i['answer'] if i['answer'] else '')

    def sub_steps(m):
        i = byid.get(m[1])
        return '\n\n' + '\n'.join('%d. %s' % (k + 1, s) for k, s in enumerate(steps(i))) + '\n\n' if i else m[0]
    def sub_note(m):
        i = byid.get(m[1])
        return note(i) if i else m[0]

    def sub_fig(m):   # its own paragraph, so markdown leaves the SVG alone
        i = byid.get(m[1])
        if not (i and figures(i)):
            return m[0]
        cap = '' if figures(i)[0].startswith('strip') else ';max-width:3.4in'   # a rectangle at full width runs long
        return '\n\n<div class="fig" style="margin:.2em 0%s">%s</div>\n\n' % (cap, figure(figures(i)[0], 0.6))
    text = FIG.sub(sub_fig, NOTE.sub(sub_note, STEPS.sub(sub_steps, text)))
    text = REF.sub(sub, text).replace('{sketch}', '<div class="sketch"></div>').replace(
        '{work}', '<div class="sketch work"></div>').replace('{small}', '<div class="sketch small"></div>').replace(
        '{tall}', '<div class="sketch tall"></div>')
    text = re.sub(r'_{2,}', lambda m: '<span class="blank" style="width:%.1fem"></span>' % (len(m[0]) * 0.45), text)
    return tables(markdown.markdown(text, extensions=['tables', 'sane_lists']))


UNIT_WORD = {'ft': 'feet', 'in': 'inches', 'cm': 'centimeters', 'm': 'meters', 'yd': 'yards', 'units': 'units'}
ONE_UNIT = {'feet': 'foot', 'inches': 'inch'}   # irregular singulars; any other unit word drops its last s


def unit_for(v, unit):
    """The unit word for a count of v: '1 tile', '1 foot', '12 tiles' (a 1-wide figure printed "1 units")."""
    if fig_num(v) != 1:
        return unit
    return ONE_UNIT.get(unit, unit[:-1] if unit.endswith('s') and not unit.endswith('ss') else unit)


def fig_fields(spec):
    """A figure cell's fields and flags: 'rect l=6_3/4 w=2_3/4 P=? u=in' (a mixed number joins with _), and bare
    flags such as grid (draw the unit squares) and marks (tick and number each unit side along the edge)."""
    parts = spec.split()[1:]
    f = dict(x.split('=', 1) for x in parts if '=' in x)
    return {k: v.replace('_', ' ') for k, v in f.items()}, {x for x in parts if '=' not in x}


def fig_num(v):
    try:
        return float(sum(Fraction(x) for x in v.split()))
    except (ValueError, ZeroDivisionError):
        return None


def note(i):
    """'Lee: 48 square feet, 6 feet wide' from the stem's name and the figure cell's given numbers."""
    f, _ = fig_fields(i['figure'])
    unit = UNIT_WORD.get(f.get('u', 'ft'), f.get('u', ''))
    who = re.search(r'The (\w+) family', i['stem'])
    given = (['%s square %s' % (f['A'], unit_for(f['A'], unit))] if 'A' in f else []) + (
        ['%s %s of fence' % (f['P'], unit_for(f['P'], unit))] if 'P' in f else [])
    given += ['%s %s %s' % (f[k], unit_for(f[k], unit), {'w': 'wide', 'l': 'long'}[k]) for k in ('w', 'l')
              if f.get(k, '?') != '?']
    return (who[1] + ': ' if who else '') + ', '.join(given)


def figures(i):
    """A row's figure cell as a list of figure specs. A fix may hold two, 'their | right': the wrong working's
    picture, then the right one ('| strip ...' gives only the right one). Any other row holds one."""
    cell = (i.get('figure') or '').strip()
    if not cell:
        return []
    return [x.strip() for x in cell.split('|')] if '|' in cell else [cell]


def figure(spec, size=1.0):
    """A figure cell drawn as inline SVG: a strip diagram ('strip ...') or a labelled rectangle ('rect ...')."""
    if not spec:
        return ''
    if spec.split()[0] == 'strip':
        return strip(spec, size)
    if spec.split()[0] == 'rows':
        return rows_fig(spec, size)
    return rect(spec, size)


SCALE = re.compile(r'scale=(\d+)')   # draw as if the longest bar were this long, so two figures of one day share a unit
STRIP_BAR = re.compile(r'^(?P<name>[^:]*):(?P<pieces>[^=/]+)(?:=(?P<total>[^/]+))?(?:/(?P<segs>.+))?$')


def strip_bars(spec):
    """'strip Kitten:7 Dog:7*8=d' as bars: [(name, [(value, count), ...], total, [segment, ...]), ...]. A value or
    count is a number, a letter or '?'; '_' in a name is a space."""
    bars = []
    for tok in spec.split()[1:]:
        if SCALE.fullmatch(tok):
            continue   # scale=48: a drawing option, not a bar
        m = STRIP_BAR.match(tok)
        if not m:
            raise ValueError('strip bar "%s" is not name:pieces[=total][/a,b]' % tok)
        pieces = []
        for p in m['pieces'].split('+'):
            v, _, c = p.partition('*')
            pieces.append((v.strip(), (c or '1').strip()))
        bars.append((m['name'].replace('_', ' '), pieces, (m['total'] or '').strip(),
                     [s.strip() for s in (m['segs'] or '').split(',') if s.strip()]))
    return bars


def strip_numbers(spec):
    """The numbers a strip figure prints (values, counts, totals, segments), for the figure-and-stem gate."""
    out = []
    for _, pieces, total, segs in strip_bars(spec):
        for v, c in pieces:
            out += [v] + ([c] if c != '1' else [])
        out += [total] + segs
    return [x for x in out if re.fullmatch(r'\d+', x)]


def strip_scale(spec):
    m = re.search(r'(?:^|\s)scale=(\d+)\b', spec)
    return int(m[1]) if m else None


def strip(spec, size=1.0, upto=None):
    """A strip (tape) diagram from a figure cell. Each bar is 'Name:pieces[=total][/a,b]':
    pieces are 'value' or 'value*count' joined by '+'; the first piece is one unit, a later piece of the same value
    is drawn as more copies (solid), a piece of another value as an extra piece (dashed), as in '6+2' for 2 more
    than 6. '=total' brackets the whole bar and writes its total under it ('?' or a letter for the unknown). '/a,b'
    brackets parts of the bar, as in '/135,p' for 135 read and p left. A count that is a letter ('9*n=36') draws one
    long piece marked 'n times'. Unknowns are worked out from the other bars, so the picture is to scale; a piece
    too small to label is widened. 'scale=48' draws as if the longest bar were 48, so two figures of one day can
    share one unit. upto=n draws only the first n bars, in the full picture's frame (the display builds a picture
    step by step)."""
    bars = strip_bars(spec)
    known = {}

    def val(x):
        if re.fullmatch(r'\d+', x):
            return Fraction(int(x))
        return known.get(x)

    for _ in range(4):   # solve each bar's one unknown from its total, sharing letters across bars
        for _, pieces, total, _ in bars:
            t = val(total) if total else None
            terms = [(val(v), val(c), v, c) for v, c in pieces]
            unk = [k for k, (a, b, _, _) in enumerate(terms) if a is None or b is None]
            if t is not None and len(unk) == 1:
                a, b, v, c = terms[unk[0]]
                rest = sum(x * y for k, (x, y, _, _) in enumerate(terms) if k != unk[0])
                if a is None and b is not None and b and v != '?':
                    known[v] = (t - rest) / b   # an unknown count stays unknown: it is drawn as one long piece
            elif t is None and total and total != '?' and not unk:
                known[total] = sum(a * b for a, b, _, _ in terms)
    widths = []
    for _, pieces, total, _ in bars:
        whole = val(total) if total else None
        widths.append(whole or sum((val(v) or 0) * (val(c) if val(c) is not None else 4) for v, c in pieces))
    top = max([w for w in widths if w] or [1])
    if strip_scale(spec):
        top = max(top, Fraction(strip_scale(spec)))
    fill = top / 4   # an unknown with nothing to size it from
    # one drawing space for every size (a font of 30 units); size only sets how big it prints
    span, fs, minp, bh, gap = 640, 30, 54, 46, 10
    lw = max([len(n) for n, _, _, _ in bars] + [1]) * fs * 0.52 + 16
    x0 = lw + 10
    t = lambda x, y, s, a='middle': '<text x="%.0f" y="%.0f" text-anchor="%s" font-size="%d">%s</text>' % (
        x, y, a, fs, html.escape(s))
    box = lambda x, y, w, dash='': ('<rect x="%.0f" y="%.0f" width="%.0f" height="%d" fill="none" stroke="#000" '
                                    'stroke-width="3"%s/>' % (x, y, w, bh, dash))

    def bracket(xa, xb, yb, label, up=False):   # a square bracket along a bar, its label off the middle tick
        s, mid = (-1 if up else 1), (xa + xb) / 2
        return ('<path d="M%.0f %.0f L%.0f %.0f L%.0f %.0f L%.0f %.0f M%.0f %.0f L%.0f %.0f" fill="none" '
                'stroke="#000" stroke-width="2"/>' % (xa, yb, xa, yb + s * 10, xb, yb + s * 10, xb, yb,
                                                      mid, yb + s * 10, mid, yb + s * 16)) + t(
            mid, yb + (s * 16 + (fs - 2) if not up else -16 - 6), label)
    out, y, right = [], 4, x0
    for bi, ((name, pieces, total, segs), w) in enumerate(zip(bars, widths)):
        if upto is not None and bi == upto:
            hidden = len(out)
        above = bool(total and segs)
        if above:
            y += fs + 26
        unit, x = pieces[0][0], x0
        for v, c in pieces:
            a, n = val(v), val(c)
            if n is None:   # an unknown number of copies: one long piece, as long as what is left of the total
                rest = sum((val(v2) or 0) * (val(c2) or 0) for v2, c2 in pieces if (v2, c2) != (v, c))
                long_ = (w - rest) if w and val(total) else (a or fill) * 4
                pw = max(float(long_ * span / top), minp * 2)
                out += [box(x, y, pw), t(x + pw / 2, y + bh / 2 + fs / 3, '%s times' % c)]
                x += pw
                continue
            for _ in range(int(n)):   # a piece of the unit's value is a copy; any other value is an extra piece
                pw = max(float((a if a is not None else fill) * span / top), minp)
                out += [box(x, y, pw, '' if v == unit else ' stroke-dasharray="10 6"'),
                        t(x + pw / 2, y + bh / 2 + fs / 3, v)]
                x += pw
        out.append(t(x0 - 12, y + bh / 2 + fs / 3, name, 'end'))
        right = max(right, x)
        if total:
            out.append(bracket(x0, x, y - 4 if above else y + bh + 4, total, up=above))
        y += bh
        if segs:
            tv = val(total) if total else (Fraction(w) if w else None)
            first = val(segs[0])
            cut = [x0]
            if tv and first is not None and len(segs) == 2:
                cut.append(x0 + (x - x0) * float(first / tv))
            else:
                cut += [x0 + (x - x0) * k / len(segs) for k in range(1, len(segs))]
            cut.append(x)
            for k, sg in enumerate(segs):
                out.append(bracket(cut[k] + 3, cut[k + 1] - 3, y + 4, sg))
        y += (fs + 24 if (total and not above) or segs else 0) + gap
    if upto is not None and upto < len(bars):
        out = out[:hidden]   # later bars are laid out (so the frame does not jump) but not drawn yet
    if strip_scale(spec):
        right = max(right, x0 + span)   # a shared scale keeps one frame width, so equal units print equal
    W, H = right + 20, y
    alt = 'A strip diagram: ' + '; '.join('%s %s%s' % (n, ' and '.join(
        v if c == '1' else '%s copies of %s' % (c, v) for v, c in p), (', in all ' + tt) if tt else '')
        for n, p, tt, _ in bars)
    # full size fills the width (the display); a smaller size prints its words at about 11 point on a page
    style = ('width:100%;max-width:9in;height:auto' if size >= 1 else
             'display:block;height:%.2fin;width:auto;max-width:100%%' % (H / fs * 11 / 72 * size / 0.6))
    return ('<svg viewBox="0 0 %.0f %.0f" width="%.0f" style="%s" role="img" '
            'aria-label="%s" xmlns="http://www.w3.org/2000/svg" font-family="Georgia, serif">%s</svg>') % (
        W, H, W, style, html.escape(alt), ''.join(out))


def rect(spec, size=1.0):
    """A labelled rectangle from a figure cell: 'rect w=7 l=? A=63 u=ft' or 'rect l=12 w=? P=38 u=ft'. Small
    whole-number sides are drawn to scale; 'grid' draws the unit squares inside and 'marks' ticks and numbers each
    unit side along the edge. Larger figures keep one plain shape."""
    f, flags = fig_fields(spec)
    u = f.get('u', 'ft')
    unit = UNIT_WORD.get(u, u)
    lab = lambda v: '?' if v == '?' else '%s %s' % (v, unit_for(v, unit))
    L, Wd = fig_num(f.get('l', '?')), fig_num(f.get('w', '?'))
    scaled = L and Wd and L <= 12 and Wd <= 12
    W = 420 * size
    H = W * Wd / L if scaled else 220 * size
    if scaled and H > 300 * size:
        W, H = W * 300 * size / H, 300 * size
    pad = 60 * size if 'marks' in flags else 0
    fs = 36 * size
    tw = lambda s: len(s) * fs * 0.52   # about a Georgia character's width
    # 'rows' labels one long side "4 in each row" and one short side "3 rows", once each (expert, day 1: an array
    # is read in rows, not as a length in tiles); otherwise each side is labelled twice in its unit
    rows_ = 'rows' in flags
    if rows_:
        top = '?' if f.get('l', '?') == '?' else '%s in %s' % (f['l'], 'the row' if Wd == 1 else 'each row')
        side = '?' if f.get('w', '?') == '?' else '%s %s' % (f['w'], 'row' if Wd == 1 else 'rows')
    else:
        top, side = lab(f.get('l', '')), lab(f.get('w', ''))
    x0, y0, w, h = max(170 * size, tw(side) + 30 * size) + pad, 60 * size + pad, W, H
    mid = ''
    if 'A' in f:   # squares and tiles are already square units: "28 squares inside"
        mid = ('%s %s inside' % (f['A'], unit_for(f['A'], unit)) if unit in ('squares', 'tiles') else
               '%s square %s inside' % (f['A'], unit_for(f['A'], unit)))
    elif 'P' in f:
        mid = '%s %s%s all the way around' % (f['P'], unit_for(f['P'], unit), ' of ' + f['around'] if f.get('around') else '')
    # an inside label wider than the shape goes under it, below the bottom label (expert, day 2: Kai's 4 by 9)
    below = bool(mid) and tw(mid) > w - 16 * size
    right = 0 if rows_ else tw(side) + 30 * size
    fw = max(x0 + w + max(right, 170 * size) + pad, x0 + w / 2 + tw(top) / 2 + 20 * size,
             x0 + w / 2 + tw(mid) / 2 + 20 * size if below else 0)
    fh = H + 130 * size + 2 * pad + (50 * size if below else 0)
    t = lambda x, y, s, a='middle', z=fs: '<text x="%.0f" y="%.0f" text-anchor="%s" font-size="%.0f">%s</text>' % (
        x, y, a, z, html.escape(s))
    extra = ''
    if scaled and 'grid' in flags and L == int(L) and Wd == int(Wd):
        cx, cy = w / L, h / Wd
        extra += ''.join('<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f" stroke="#000" stroke-width="1"/>' % (
            x0 + k * cx, y0, x0 + k * cx, y0 + h) for k in range(1, int(L)))
        extra += ''.join('<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f" stroke="#000" stroke-width="1"/>' % (
            x0, y0 + k * cy, x0 + w, y0 + k * cy) for k in range(1, int(Wd)))
    if scaled and 'marks' in flags and L == int(L) and Wd == int(Wd):
        cx, cy, n, tk, off, z = w / L, h / Wd, 0, 9 * size, 30 * size, 24 * size
        segs = ([(x0 + (k + .5) * cx, y0, 0, -1) for k in range(int(L))] + [(x0 + w, y0 + (k + .5) * cy, 1, 0) for k in range(int(Wd))]
                + [(x0 + w - (k + .5) * cx, y0 + h, 0, 1) for k in range(int(L))] + [(x0, y0 + h - (k + .5) * cy, -1, 0) for k in range(int(Wd))])
        for x, y, dx, dy in segs:
            n += 1
            extra += '<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f" stroke="#000" stroke-width="2"/>' % (
                x - dx * tk, y - dy * tk, x + dx * tk, y + dy * tk)
            extra += t(x + dx * off, y + dy * off + 8 * size, str(n), 'middle', z)
    labels = (t(x0 + w / 2, y0 - 14 * size - pad, top) + t(x0 - 10 * size - pad, y0 + h / 2 + 12 * size, side, 'end'))
    if not rows_:
        labels += (t(x0 + w / 2, y0 + h + 46 * size + pad, top)
                   + t(x0 + w + 10 * size + pad, y0 + h / 2 + 12 * size, side, 'start'))
    if mid:
        labels += (t(x0 + w / 2, y0 + h + (96 if not rows_ else 46) * size + pad, mid) if below
                   else t(x0 + w / 2, y0 + h / 2 + 12 * size, mid))
    return ('<svg viewBox="0 0 %.0f %.0f" width="%.0f" style="width:100%%;max-width:9in;height:auto" role="img" aria-label="%s" xmlns="http://www.w3.org/2000/svg" '
            'font-family="Georgia, serif"><rect x="%.0f" y="%.0f" width="%.0f" height="%.0f" fill="none" stroke="#000" '
            'stroke-width="3"/>%s%s</svg>') % (
        fw, fh, fw, html.escape('A rectangle: ' + ', '.join(
            '%s %s' % (k, v) for k, v in f.items()) + (', drawn in rows' if rows_ else '')), x0, y0, w, h, extra, labels)


def rows_fig(spec, size=1.0):
    """Tiles dealt into rows: 'rows 12/5' deals 12 dots one at a time into 5 rows (3, 3, 2, 2, 2) and leaves each
    short row's missing places open, dashed, so the picture shows why 5 is not a factor of 12 (expert, day 1)."""
    n, r = (int(x) for x in spec.split()[1].split('/'))
    per = [n // r + (1 if k < n % r else 0) for k in range(r)]
    cols, d = max(per), 44 * size
    x0, y0 = 40 * size, 30 * size
    out = []
    for k, c in enumerate(per):
        for j in range(cols):
            cx, cy = x0 + j * d + d / 2, y0 + k * d + d / 2
            out.append('<circle cx="%.0f" cy="%.0f" r="%.0f" %s/>' % (cx, cy, d * 0.36, 'fill="#000"' if j < c else
                                                                     'fill="none" stroke="#000" stroke-width="2" stroke-dasharray="5 4"'))
        out.append('<text x="%.0f" y="%.0f" font-size="%.0f">%d</text>' % (x0 + cols * d + 16 * size, y0 + k * d + d * 0.68, 26 * size, c))
    W, H = x0 + cols * d + 70 * size, y0 + r * d + 20 * size
    alt = '%d dots dealt into %d rows: %s in the rows; the short rows are left open' % (n, r, ', '.join(map(str, per)))
    return ('<svg viewBox="0 0 %.0f %.0f" width="%.0f" style="width:100%%;max-width:4in;height:auto" role="img" '
            'aria-label="%s" xmlns="http://www.w3.org/2000/svg" font-family="Georgia, serif">%s</svg>') % (
        W, H, W, html.escape(alt), ''.join(out))


def foot_line(h, course, credits=()):
    s = 'Curio Class, %s, day %s, version %s, CC BY 4.0, curioclass.org' % (
        course_name(course), int(h['day']), h['version'])
    return '<div class="foot">%s%s</div>' % (html.escape(s), ''.join(
        '<br>%s' % html.escape(c) for c in credits))


def branch_only(d, rows):
    """Parts whose rows the day reaches only on an "If ..." branch or under "Longer": not on the default path."""
    day = d['secs'].get('The day', '')
    main = '\n\n'.join(par for par in re.split(r'\n\s*\n', day) if not par.lstrip().startswith('**If'))
    hit = set(REF.findall(main)) | set(STEPS.findall(main))
    return ({(i['code'], p) for i in rows for p in plan.partset(i)}
            - {(i['code'], p) for i in rows if i['item_id'] in hit for p in plan.partset(i)})


def header_table(d, row, parts, tt, side=frozenset()):
    h = d['head']
    ps = '; '.join('%s (%s) %s%s' % (p['code'], p['part'], p['text'],
                                     ' (on a branch or Longer only)' if (p['code'], p['part']) in side else '') for p in parts)
    cells = [('Day', '%s, unit %s, %s day' % (h['day'], h['unit'], row['kind'].lower())),
             ('Goal', row['goal']), ('Standard parts', ps or 'see the unit opener'),
             ('Tool', '%s (%s), %s min' % (tt, row['mark'], row['tool_min']) if row['tool'] else 'None'),
             ('Materials', h['materials']), ('Print', h['print']),
             ('Leans on', '; '.join(x for x in leans(d) if not x.lower().startswith(WHEN)) or 'nothing'),
             ] + ([('Uses when it exists', '; '.join(optional(d)))] if optional(d) else []) + [
             ('Version', h['version']), ('Credit', h['credit'])]
    return '<table class="meta">%s</table>' % ''.join(
        '<tr><td>%s</td><td>%s</td></tr>' % (html.escape(a), html.escape(b)) for a, b in cells)


def student_html(d, course, items):
    h, title = d['head'], d['title']
    byid = {i['item_id']: i for i in items}
    credits = sorted({byid[r]['source'] for r in REF.findall(d['student']) if r in byid and byid[r].get('source')})
    if h['credit'].lower() != 'ours':
        credits = [h['credit']] + credits
    sides = ''.join('<div class="side">%s%s%s</div>' % (
        '<p>Name ______________________ Date __________</p>' if k == 0 else '', md(body, items),
        foot_line(h, course, credits))
        for k, (_, body) in enumerate(d['sides']))
    return '<h1>%s</h1>%s' % (html.escape(title), sides)


def build_day(d, course, items, days, parts_all, errors, wrongs, pdf):
    h = d['head']
    row = next(x for x in days if x['day'] == h['day'])
    tt = tool_title(row['tool']) if row['tool'] else ''
    mine = [i for i in items if i['day'] == h['day'] and i['check'] in plan.LESSON_KINDS | {'exit'}]
    # a check day is measured by its end rows, which carry the stretch, not the day
    # (a stretch with two check days keeps each day's end rows apart: select by the day being built)
    end = sorted((i for i in items if i['stretch'] == row['stretch'] and i['check'] == 'end' and i['day'] == h['day']),
                 key=nkey)
    if row['kind'] != 'Check':
        end = []
    pk = {(i['code'], p) for i in (end or mine) for p in plan.partset(i)}   # a cell may name several: "f, g"
    parts = [p for p in parts_all if (p['code'], p['part']) in pk]
    out = OUT / course / d['path'].parent.name
    out.mkdir(parents=True, exist_ok=True)
    name = d['path'].stem
    title = d['title']
    byid = {i['item_id']: i for i in items}
    refs = sorted({r for r in REF.findall(d['teacher'] + d['student']) + STEPS.findall(d['teacher']) if r in byid},
                  key=lambda r: (ORDER.index(byid[r]['check']) if byid[r]['check'] in ORDER else 9,
                                 byid[r].get('path', ''), nkey(byid[r]), r))   # the id last: ties print in one order
    refs = [i['item_id'] for i in end] + [r for r in refs if r not in {i['item_id'] for i in end}]
    credits = sorted({byid[r]['source'] for r in refs if byid[r].get('source')})
    foot = foot_line(h, course, ([h['credit']] if h['credit'].lower() != 'ours' else []) + credits)
    gone = missing(d)
    warn = ('<p class="warn">Not ready to teach: %s missing.</p>' % html.escape(', '.join(gone))) if gone else ''
    side = branch_only(d, mine) if not end else set()
    tb = '<h1>%s</h1><p>Teacher page</p>%s%s%s%s' % (html.escape(title), warn, header_table(d, row, parts, tt, side),
                                                     md(d['teacher'], items, teacher=True), foot)
    put(out / (name + '-teacher.html'), page(title + ': teacher page', tb, 'teacher'), encoding='utf-8')
    sb = student_html(d, course, items)
    put(out / (name + '-student.html'), page(title + ': student page', sb, 'student'), encoding='utf-8')
    put(out / (name + '-student-large.html'), page(title + ': student page, large print', sb, 'student large'),
                                                     encoding='utf-8')
    # key: in the order the pages use them, both exit paths
    errname = {e['letter']: e['error'] for e in errors if e['stretch'] == row['stretch']}
    kr = []
    for r in refs:
        i = byid[r]
        ws, seen = [], set()
        for w in (w for w in wrongs if w['item_id'] == r):
            e = w['error']
            what = ('error %s' % e) + ('' if e in seen else ', ' + errname.get(e, '').lower()) if e else ''
            seen.add(e)
            tail = (what + (' (%s)' % w['note'] if w['note'] else '')).strip()
            ws.append(w['shown'] + (': ' + tail if tail else ''))
        where = i['check'] + (' %s' % i['n'] if i['check'] == 'end' else '') + (' (%s)' % i['path'] if i.get('path') else '')
        ans = html.escape(i['answer'])
        if i['judged'] == 'teacher' and steps(i):
            ans += '<br><b>Look-fors, each ticked alone:</b><ol>%s</ol>' % ''.join(
                '<li>%s</li>' % html.escape(x) for x in steps(i))
        if i['judged'] == 'teacher' and i.get('samples'):
            ans += '<b>Samples (ours, untested):</b><ul>%s</ul>' % ''.join(
                '<li>%s</li>' % html.escape(x.strip()) for x in i['samples'].split('|') if x.strip())
        # a strip figure prints with its question (a fix: their picture, then the right one)
        pics = ''.join('<div style="margin:.2em 0">%s%s</div>' % (
            ('<i>%s</i>' % ('Their picture' if k == 0 else 'The right picture')) if len(figures(i)) == 2 else '',
            figure(x, 0.6)) for k, x in enumerate(figures(i)) if x.startswith('strip'))
        kr.append('<tr><td>%s</td><td>%s</td><td>%s</td><td class="q">%s%s</td><td>%s</td><td>%s</td></tr>' % (
            html.escape(where), html.escape(i['item_id']), html.escape(part_of(i)), html.escape(stem(i)), pics, ans,
            html.escape('; '.join(ws))))
    kb = ('<h1>%s: key</h1><p>Each answer is worked out in full. The last column names the wrong answers to expect and the error each one shows.</p>'
          '<p>%s</p>'
          '<table><tr><th>Where</th><th>Id</th><th>Part</th><th>Question</th><th>Answer</th><th>Wrong answers and what '
          'they mean</th></tr>%s</table>%s' % (html.escape(title), html.escape(ACCEPT), ''.join(kr), foot))
    put(out / (name + '-key.html'), page(title + ': key', kb, 'key'), encoding='utf-8')
    # exit slip, four to a sheet: the paper path only
    ex = [i for i in mine if i['check'] == 'exit' and i.get('path', '') in ('', 'paper')]
    if ex and row['kind'] != 'Check':
        one = '<div class="slip"><p>Name ______________ Day %s</p>%s%s</div>' % (h['day'], ''.join(
            slip_item(k, i) for k, i in enumerate(ex)), foot)
        put(out / (name + '-exit.html'), page(title + ': exit slips', one * 4, 'student'), encoding='utf-8')
    # display, in the order the teacher page runs: part by part, each [[id]], [[steps:id]] and **Ask.** where it
    # first appears (a worked example with its figure, then its steps one screen at a time; a fix with the wrong
    # working beside the right; a challenge); a plain sum's answers; a part's "check your answers" screen only when
    # that part names a partner or self check (its own "Check: ..." line, if any, is the sentence); the frames last
    scr, done, asked = [], set(), set()
    fig = lambda i: figure(figures(i)[0]) if len(figures(i)) == 1 else ''
    tok = re.compile(r'\[\[(?:steps:)?([A-Za-z0-9-]+)\]\]|\*\*Ask\.\*\* (.+?)(?=\n\s*\n|\Z)', re.S)
    peer = re.compile(r'swap and check|swap and compare|partner check|check their own|partners check', re.I)
    on_page = set(REF.findall(d['student']))
    last_ex = []
    draws = re.compile(r'\b(draw|drawn|build|snap|sketch|lay|put out)\b', re.I)

    def step_fig(i, k, first, n):
        """The example's figure at step k: none before the step that first draws or builds it; a strip grows a bar
        a step from there, in the full picture's frame, whole by the last step; smaller once the list is long."""
        spec = figures(i)[0] if len(figures(i)) == 1 else ''
        if not spec or k < first:
            return ''
        upto = None
        if spec.startswith('strip') and k < n - 1:
            nb = len(strip_bars(spec))
            upto = min(nb, k - first + 1) if k - first + 1 < nb else None
        svg = strip(spec, 1.0, upto) if spec.startswith('strip') else figure(spec)
        return svg if k < 2 else '<div style="max-width:60%%">%s</div>' % svg

    def screens(i):
        if i['check'] == 'example':
            st = steps(i)
            first = next((k for k, s in enumerate(st) if draws.search(s)), 0)
            at = re.search(r'\bat=(\d+)', figures(i)[0]) if len(figures(i)) == 1 else None
            if at:   # 'rows 12/5 at=4': the picture is the answer, held back until the step that shows it
                first = int(at[1]) - 1
            o = ['<div class="screen"><p>%s</p>%s</div>' % (stacked(stem(i)), fig(i) if first == 0 and not
                                                            draws.search(st[0] if st else '') else '')]
            for k in range(len(st)):
                # a step that lays this example beside an earlier one shows that one's picture too
                other = (''.join(figure(figures(e)[0]) for e in last_ex[-1:] if len(figures(e)) == 1)
                         if re.search(r'\bbeside the\b', st[k], re.I) else '')
                o.append('<div class="screen">%s%s<ol>%s</ol></div>' % (other, step_fig(i, k, first, len(st)), ''.join(
                    '<li%s>%s</li>' % (' class="now"' if j == k else '', html.escape(s)) for j, s in enumerate(st[:k + 1]))))
            last_ex.append(i)
            return o
        if i['check'] == 'fix':   # one figure is the problem's, above both; two are their picture and the right one
            st, fs = steps(i) + ['', ''], figures(i)
            two = [figure(x) if x else '' for x in fs] if len(fs) == 2 else ['', '']
            return ['<div class="screen"><p>%s</p>%s<div class="pair"><div><b>Their working</b>%s<p>%s</p></div>'
                    '<div><b>The right working</b>%s<p>%s</p></div></div></div>' % (
                        stacked(stem(i)), fig(i), two[0], html.escape(cap1(re.sub(r'^.*?working: ', '', st[0]))),
                        two[1], html.escape(cap1(re.sub(r'^.*?working: ', '', st[1]))))]
        if i['check'] == 'challenge':
            return ['<div class="screen"><p><b>Challenge.</b> %s</p></div>' % stacked(stem(i))]
        return []

    def answers_screen():
        # the letter sentence only when a key holds a letter for an unknown (expert, day 6: stretch 1 has none)
        letter = any(LETTER.search(i['answer']) for i in end if i['judged'] == 'key')
        return ('<div class="screen"><p><b>Answers.</b> %sAn equation is right in any order if it '
                'says the same thing. Mark your own in pen. Items %s are read by your teacher.</p><ol>%s</ol></div>' % (
                    'Any letter is right. ' if letter else '',
                    ' and '.join(i['n'] for i in end if i['judged'] == 'teacher') or 'none',
                    ''.join('<li style="list-style:none"><b>%s.</b> %s</li>' % (html.escape(i['n']), html.escape(
                        i['answer'] if i['judged'] == 'key' else 'read by your teacher')) for i in end)))

    def walk(text, prac):
        for m in tok.finditer(text):
            if m[2]:
                # every quoted question in the Ask paragraph is a screen (a "Then:" question too); answers
                # ("Expect: ...") are quoted without a question mark and stay off the screen
                qs = [q for q in re.findall(r'"([^"]+)"', m[2]) if q.rstrip().endswith('?')] or \
                    re.findall(r'"([^"]+)"', m[2])[:1]
                for q in qs:
                    q = re.sub(r'[*]', '', q).strip()
                    if q not in asked:   # one screen per planned question, however often the page names it
                        asked.add(q)
                        scr.append('<div class="screen">%s</div>' % html.escape(q))
                for r in REF.findall(m[2]):   # a row named inside the Ask paragraph is still walked
                    if r not in done and r in byid:
                        done.add(r)
                        scr.extend(screens(byid[r]))
                        if byid[r]['check'] in ('practice', 'tool'):
                            prac.append(byid[r])
                continue
            if m[1] in done or m[1] not in byid:
                continue
            done.add(m[1])
            i = byid[m[1]]
            scr.extend(screens(i))
            if i['check'] in ('practice', 'tool'):
                prac.append(i)

    def chunks(btxt):
        """A part's text cut where the display must follow the prose: each "If ..." branch paragraph is its own run
        of screens (expert, day 5: every warm-up branch was shown at once), and a Check: line closes a run, so its
        screen comes before an Ask written after it."""
        out, cur = [], []
        for par in re.split(r'\n\s*\n', btxt):
            if cur and re.match(r'\s*(?:\*\*)?If\b', par):
                out.append('\n\n'.join(cur)); cur = []
            cur.append(par)
            if re.search(r'^Check(?: \(sort\))?: ', par, re.M):
                out.append('\n\n'.join(cur)); cur = []
        return out + (['\n\n'.join(cur)] if cur else [])

    shown = False
    for _, bname, whole in d['blocks']:
        if end and bname.lower().startswith('respond'):
            scr.append(answers_screen())
            shown = True
            gs = [' '.join(b.split()) for b in re.findall(r'^- (.+?)(?=^- |\n\s*\n|\Z)', whole, re.M | re.S)]
            for b in gs:
                scr.append('<div class="screen"><p><b>Group.</b> %s</p></div>' % html.escape(b))
            if len(gs) > 1:   # groups work at once: one screen holds every task (expert, day 6)
                scr.append('<div class="screen" style="font-size:16pt"><p><b>Every group.</b></p><ul>%s</ul></div>'
                           % ''.join('<li>%s</li>' % html.escape(b) for b in gs))
        for btxt in chunks(whole):
          prac = []
          walk(btxt, prac)
          # tool rows (the paper path of a tool part) get a question screen, then their check screens, so the
          # answers never show before students predict (expert, day 4): a long row (a story, a whole table) its own
          # pair of screens; short rows with short answers (a table's lines, day 83) share one of each
          tools, prac = [i for i in prac if i['check'] == 'tool'], [i for i in prac if i['check'] != 'tool']
          ct = re.search(r'^Check(?: \(sort\))?: (.+)$', btxt, re.M)
          say_t = html.escape(ct[1].strip() if ct else 'Does yours match? Fix it in pen.')
          brief = [i for i in tools if words(stem(i)) <= 12 and len(i['answer']) <= 60]
          if len(brief) < len(tools):   # all share one screen, or each has its own: the page's order is kept (day 2)
              brief = []
          for i in tools:
              if i in brief:
                  continue
              scr.append('<div class="screen"><p>%s</p></div>' % stacked(stem(i)))
              scr.append('<div class="screen"><p><b>Check your answers.</b> %s</p><p>%s</p><p><b>%s</b></p></div>' % (
                  say_t, stacked(stem(i)), html.escape(i['answer'])))
          if brief:
              scr.append('<div class="screen"><ol>%s</ol></div>' % ''.join(
                  '<li>%s</li>' % stacked(stem(i)) for i in brief))
              scr.append('<div class="screen"><p><b>Check your answers.</b> %s</p><ol>%s</ol></div>' % (say_t, ''.join(
                  '<li>%s<br><b>%s</b></li>' % (stacked(stem(i)), html.escape(i['answer'])) for i in brief)))
          # a practice row the student page does not print has no other place to be read: a long one (a story) gets
          # its own screen, then its answer; short ones (warm-up facts) share one screen, answered below
          cm0 = re.search(r'^Check(?: \((sort)\))?: (.+)$', btxt, re.M) or peer.search(whole)
          off = [i for i in prac if i['item_id'] not in on_page]
          for i in off:
              if words(stem(i)) > 12:
                  scr.append('<div class="screen"><p>%s</p></div>' % stacked(stem(i)))
                  if not cm0:
                      scr.append('<div class="screen"><p>%s</p><p><b>%s</b></p></div>' % (
                          stacked(stem(i)), html.escape(i['answer'])))
          short = [i for i in off if words(stem(i)) <= 12]
          if short:
              scr.append('<div class="screen"><ol>%s</ol></div>' % ''.join('<li>%s</li>' % stacked(stem(i)) for i in short))
          plain = [i for i in prac if re.search(r'=\s*\?\s*$', stem(i))]
          if plain:
              scr.append('<div class="screen"><p><b>Check your answers.</b></p><ol>%s</ol></div>' % ''.join(
                  '<li>%s = %s</li>' % (html.escape(stem(i).rstrip('? =').strip()), html.escape(i['answer'])) for i in plain))
          rest = [i for i in prac if i not in plain]
          cm = re.search(r'^Check(?: \((sort)\))?: (.+)$', btxt, re.M)
          if rest and (cm or peer.search(whole)):
              say = cm[2].strip() if cm else ('Put each answer back in its equation. Does it give the number in the '
                                             'question? If not, put a question mark.')
              # each row's answer, whatever its form; "Check (sort):" shows only its first part, the kind, so a sort
              # checked now does not give away the solving that comes later
              ans = lambda i: i['answer'].split(';')[0].strip() if cm and cm[1] else i['answer']
              scr.append('<div class="screen"><p><b>Check your answers.</b> %s</p><ol>%s</ol></div>' % (
                  html.escape(say), ''.join('<li>%s<br><b>%s</b></li>' % (stacked(stem(i)), html.escape(ans(i)))
                                            for i in rest)))
          elif short:   # warm-up rows with no check line: their answers, so the teacher need not read them out
              left = [i for i in short if i not in plain]
              if left:
                  scr.append('<div class="screen"><p><b>Answers.</b></p><ol>%s</ol></div>' % ''.join(
                      '<li>%s<br><b>%s</b></li>' % (stacked(stem(i)), html.escape(i['answer'])) for i in left))
    # anything named outside the parts of the day (Longer, Tomorrow); the day's own parts are walked above
    walk('\n'.join(v for k, v in d['secs'].items() if k != 'The day'), [])
    if end and not shown:
        scr.append(answers_screen())
    scr += ['<div class="screen">%s</div>' % html.escape(q) for q in
            re.findall(r'"([^"]*__[^"]*)"', d['secs'].get('Words and supports', ''))]
    put(out / (name + '-display.html'), page(title + ': display', ''.join(scr) + foot, 'display'),
                                                encoding='utf-8')
    note = ''
    if pdf:
        note = print_sides(out / (name + '-student.html'))
    return out, note


ACCEPT = ('Any equal form of an equation is right: the two factors in either order, either side of the equals sign, '
          'any letter, or the matching division (n × 9 = 36, 9 × n = 36, 36 = 9 × n and 36 ÷ 9 = n all say the same).')
ORDER = ['example', 'tool', 'fix', 'practice', 'challenge', 'exit']
LETTER = re.compile(r'(?<![A-Za-z])[a-z](?![A-Za-z])\s*[=×÷+−-]|[=×÷+−-]\s*[a-z](?![A-Za-z])')   # n × 9, = n


def cap1(s):
    """The first letter up: a fix's working with its "Right working:" label stripped starts a sentence."""
    return s[:1].upper() + s[1:]
DRAWS = re.compile(r'\b(draw|sketch|strip picture|strips)\b', re.I)


def slip_item(k, i):
    """One exit question on the slip. A stem that asks for a drawing gets a box before its lines; a teacher-judged
    exit gets a taller work box; a sentence with blanks in the stem ("Finish: __ is __ times as many as __.") prints
    as its own fill line, and when the stem ends in such frames they are the answer lines."""
    sents = re.split(r'(?<=[.?!])\s+', stem(i))
    ask = [s for s in sents if '__' not in s]
    frames = [s for s in sents if '__' in s]
    blank = lambda s: re.sub(r'_{2,}', '<span class="blank" style="width:5em"></span>', stacked(s))
    # a full search ("Find all the factor pairs") is marked on its working, so it gets a work box and one answer
    # line (expert, day 3); asked with "how do you know", the box holds the pairs and the lines the reason (day 2)
    search = re.search(r'\ball the factor pairs\b|\bevery factor\b', stem(i), re.I)
    why = search and re.search(r'how do you know', stem(i), re.I)
    label = '<span style="font-size:10pt">Pairs:</span>' if why else ''
    box = ('<div class="sketch tall">%s</div>' % label if i['judged'] == 'teacher' else
           '<div class="sketch">%s</div>' % label if (DRAWS.search(stem(i)) and not re.search(r'grid paper', stem(i), re.I))
           or search else '')
    lines = ''.join('<p>%s</p>' % blank(s) for s in frames) or (
        '<p>How I know: ____________________</p><p>__________________________</p>' if why else
        '<p>__________________________</p>' if search else
        '<p>__________________________</p><p>__________________________</p>')
    if frames and not re.search(r'\b(?:finish|answer)\b', ' '.join(frames), re.I) and len(frames) < 2:
        lines += '<p>__________________________</p>'
    # "Write prime or composite for 59, 77, 34 and 73": a row for each number, with room for its proof (day 5 read)
    each = re.match(r'Write ([a-z, ]+?) for ((?:\d+, )+\d+ and \d+)\.', stem(i))
    if each and not frames:
        nums = re.findall(r'\d+', each[2])
        lines = ('<table><tr><th style="width:22%%">Number</th><th style="width:33%%">%s?</th><th>Proof</th></tr>%s</table>' % (
            html.escape(each[1][0].upper() + each[1][1:]), ''.join('<tr><td>%s</td><td></td><td></td></tr>' % n for n in nums)))
    return '<p>%d. %s</p>%s%s' % (k + 1, stacked(' '.join(ask)), box, lines)


def part_of(i):
    """'4.MD.A.3 (b), MP.2': the standard's part and the practice a row tests."""
    return '%s%s%s' % (i['code'], ' (%s)' % i['part'] if i.get('part') else '', ', ' + i['practice'] if i.get('practice') else '')


def print_sides(src):
    """Print the student page to PDF with headless Chrome and count its sides. A PDF newer than its page is
    counted as it stands; a fresh print that matches the old PDF but for its dates leaves the old file alone, so an
    unchanged page never shows as a changed PDF."""
    final = src.with_suffix('.pdf')
    if final.exists() and final.stat().st_size and final.stat().st_mtime >= src.stat().st_mtime:
        return count_sides(final)
    if not CHROME.exists():
        return 'page count not checked (no Chrome)'
    pdf = src.with_name(src.stem + '.printing.pdf')
    if pdf.exists():
        pdf.unlink()
    args = ['--headless=new', '--disable-gpu', '--no-pdf-header-footer', '--print-to-pdf=%s' % pdf, src.as_uri()]
    if os.name == 'nt':  # a bare call can return with nothing written under the sandbox; Start-Process -Wait works
        ps = "Start-Process -FilePath '%s' -ArgumentList %s -Wait -PassThru | Out-Null" % (
            CHROME, ','.join("'%s'" % a for a in args))
        subprocess.run(['powershell', '-NoProfile', '-Command', ps], capture_output=True)
    else:
        subprocess.run([str(CHROME)] + args, capture_output=True)
    for _ in range(20):
        if pdf.exists() and pdf.stat().st_size:
            break
        time.sleep(0.5)
    if not pdf.exists():
        return 'page count not checked (Chrome wrote nothing)'
    time.sleep(0.3)   # let Chrome finish the file
    new = undated(pdf.read_bytes())
    if final.exists() and undated(final.read_bytes()) == new:
        pdf.unlink()
        os.utime(final)   # the same PDF: keep its bytes, mark it current
    else:
        pdf.write_bytes(new)
        os.replace(pdf, final)
    return count_sides(final)


def undated(b):
    """A printed PDF with its creation and change dates set to one fixed value of the same length, so two prints of
    one page are the same bytes."""
    def fixed(m):
        digits = iter(b'20260101000000' + b'0' * 20)
        return m[1] + re.sub(rb'[0-9]', lambda _: bytes([next(digits)]), m[2])
    return re.sub(rb'(/(?:CreationDate|ModDate) ?\(D:)([0-9+\-Z\']+)', fixed, b)


def count_sides(pdf):
    from pypdf import PdfReader
    n = len(PdfReader(str(pdf)).pages)
    return '%d side(s)%s' % (n, '' if n <= 2 else ' FAIL: more than two')


# ------------------------------------------------------------------ once-per-unit pieces
# A piece is any other .md in a unit folder (opener.md, record.md, readiness.md, ...), with a header naming its
# kind: opener (written, 1,200 words at most), record (the record sheet, generated), check (a readiness check:
# student page and key generated from the rows), facts (a facts check sheet), family (the family note), sheet (a
# generator preset's page for the teacher), blank (a sheet printed as written, for students to work on: one with
# no preset, such as the strip sheet; two sides at most).
CAP_OPENER = 1200
PIECE_HEAD = ['piece', 'course', 'unit', 'version', 'credit']
PIECE_KINDS = ('opener', 'record', 'check', 'facts', 'family', 'sheet', 'blank')


def preset(h):
    """A sheet piece names a generator preset as 'unit n' (data/closet/worksheets/generated.csv)."""
    import ws_generated
    u, _, n = (h.get('preset') or '').partition(' ')
    return ws_generated.load().get(u, {}).get(int(n)) if n.strip().isdigit() else None


def piece_files():
    return sorted(p for p in COURSES.glob('*/u*/*.md') if not re.match(r'd\d{3}$', p.stem))


def parse_piece(path):
    t = path.read_text(encoding='utf-8')
    m = re.match(r'---\n(.*?)\n---\n(.*)', t, re.S)
    if not m:
        return None
    head = {k.strip(): v.strip() for k, _, v in (ln.partition(':') for ln in m[1].splitlines())}
    title = re.search(r'^# (.+)$', m[2], re.M)
    return dict(path=path, head=head, body=m[2], title=title[1] if title else path.stem)


def piece_rows(p, items):
    """A check piece's rows: those its "## Items" section names by id, in that order (a fixed practice sheet, so
    the day's other rows of the same kind stay out), or else every row of its check kind for its stretch."""
    h = p['head']
    named = REF.findall(section(p['body'], 'Items') or '')
    if named:
        byid = {i['item_id']: i for i in items}
        return [byid[r] for r in named if r in byid]
    return sorted([i for i in items if i['check'] == h.get('check') and i['stretch'] == h.get('stretch')],
                  key=nkey)


def unit_foot(h, course, what):
    return '<div class="foot">%s</div>' % html.escape(
        'Curio Class, %s, unit %s, %s, version %s, CC BY 4.0, curioclass.org'
        % (course_name(course), h['unit'], what, h['version']))


def section(body, name):
    m = re.search(r'^## %s\n(.*?)(?=^## |\Z)' % re.escape(name), body, re.M | re.S)
    return m[1] if m else None


def check_piece(p, items):
    f, h, lab = [], p['head'], p['path'].relative_to(ROOT).as_posix()
    for k in PIECE_HEAD:
        if not h.get(k):
            f.append('%s: header field "%s" is missing' % (lab, k))
    kind = h.get('piece')
    if kind not in PIECE_KINDS:
        f.append('%s: piece "%s" is not one of %s' % (lab, kind, ', '.join(PIECE_KINDS)))
    if kind == 'opener' and words(p['body']) > CAP_OPENER:
        f.append('%s: the unit opener is %d words; the cap is %d' % (lab, words(p['body']), CAP_OPENER))
    if kind == 'check':
        rs = piece_rows(p, items)
        if not rs:
            f.append('%s: no %s rows for stretch %s in items.csv' % (lab, h.get('check'), h.get('stretch')))
        have = {i['item_id'] for i in items}
        for r in REF.findall(section(p['body'], 'Items') or ''):
            if r not in have:
                f.append('%s: [[%s]] has no row in items.csv' % (lab, r))
        g = grade(h.get('course', ''))
        for i in rs:
            for s in sentences(stem(i)):
                if g and 3 <= g <= 5 and words(s) > SENTENCE_MAX:
                    f.append('%s: a sentence in %s is %d words; grades 3 to 5 keep to %d'
                             % (lab, i['item_id'], words(s), SENTENCE_MAX))
    if kind == 'sheet' and not preset(h):
        f.append('%s: preset "%s" is not a row of data/closet/worksheets/generated.csv' % (lab, h.get('preset', '')))
    if kind == 'family':
        for lang in ('English', 'Spanish'):
            sec = section(p['body'], lang)
            if sec is None:
                f.append('%s: no "## %s" section' % (lab, lang))
            elif words(sec) > 150:
                f.append('%s: the %s note is %d words; the cap is 150' % (lab, lang, words(sec)))
    return f


def build_piece(p, items, wrongs, errors):
    h, course = p['head'], p['head']['course']
    out = OUT / course / p['path'].parent.name
    out.mkdir(parents=True, exist_ok=True)
    name, kind, title = p['path'].stem, h['piece'], p['title']
    body = re.sub(r'^# .+\n', '', p['body'], count=1, flags=re.M)
    mdh = lambda t: markdown.markdown(t, extensions=['tables'])
    if kind in ('opener', 'family'):
        put(out / (name + '.html'), page(title, '<h1>%s</h1>%s%s' % (
            html.escape(title), mdh(body), unit_foot(h, course, name)), 'teacher'), encoding='utf-8')
        return out
    if kind == 'blank':   # a student sheet printed as written (its markup may lay out boxes), with the foot line
        put(out / (name + '-student.html'), page(title, '<h1>%s</h1>%s%s' % (
            html.escape(title), mdh(body), unit_foot(h, course, name)), 'student'))
        return out
    if kind == 'sheet':   # a page for the teacher: the preset's link, then the piece's own notes
        g = preset(h)
        url = 'https://curioclass.org' + g['url']
        put(out / (name + '.html'), page(title, '<h1>%s</h1><p><b>Make and print it:</b> <a href="%s">%s</a>. '
            'Each press of New sheet gives a fresh sheet and its key; print one sheet per student and the key for '
            'you.</p>%s%s' % (html.escape(title), html.escape(url), html.escape(url), md(body, items, teacher=True),
                              unit_foot(h, course, name)),
            'teacher'), encoding='utf-8')
        return out
    if kind == 'facts':   # every pair a x b with 2 <= a <= b <= 9, once: products, or the matching quotients
        pairs = [(a, b) for a in range(2, 10) for b in range(a, 10)]
        import random
        rnd = random.Random(h.get('seed', '1'))
        rnd.shuffle(pairs)
        qs = ['%d × %d =' % (a, b) if h.get('facts') == 'products' else '%d ÷ %d =' % (a * b, rnd.choice((a, b)))
              for a, b in pairs]
        cells = ''.join('<td>%s ______</td>%s' % (q, '</tr><tr>' if k % 4 == 3 else '') for k, q in enumerate(qs))
        sb = '<h1>%s</h1><p>Name ______________________ Date __________</p>%s<table class="facts"><tr>%s</tr></table>%s' % (
            html.escape(title), mdh(section(body, 'Student') or ''), cells, unit_foot(h, course, name))
        css = '<style>.facts td { height: auto; padding: .35em .4em; width: 25%; font-size: 14pt; }</style>'
        put(out / (name + '-student.html'), page(title, css + sb, 'student'), encoding='utf-8')
        key = ''.join('<td>%s %s</td>%s' % (q, eval(q[:-1].replace('×', '*').replace('÷', '//')),
                                             '</tr><tr>' if k % 4 == 3 else '') for k, q in enumerate(qs))
        put(out / (name + '-key.html'), page(title + ': key', '<h1>%s: key</h1>%s<table><tr>%s</tr></table>%s' % (
            html.escape(title), mdh(section(body, 'Teacher') or ''), key, unit_foot(h, course, name)), 'key'), encoding='utf-8')
        return out
    if kind == 'record':
        st = h.get('stretch')
        looks = {k.strip(): int(v) for k, _, v in (x.partition('=') for x in h.get('lookfors', '').split(';')) if v}
        ex = lambda d: sorted({i['part'] for i in items if i['stretch'] == st and i['check'] == 'exit' and i['day'] == d and i['part']})
        cols = [('R%s' % i['n'], 1) for i in items if i['stretch'] == st and i['check'] == 'readiness']
        # the exits by day; a written task named in the header ("written: s01-W3; s01-W5") follows its day's exit,
        # one column for each look-for on its row
        byid = {i['item_id']: i for i in items}
        wts = [byid[x.strip()] for x in h.get('written', '').split(';') if x.strip() in byid]
        mid = [((int(d), 0), ('E%s (%s)' % (d, ', '.join(ex(d))) if ex(d) else 'E%s' % d, 1))
               for d in {i['day'] for i in items if i['stretch'] == st and i['check'] == 'exit'}]
        mid += [((int(w['day']), 1), ('W%s (%s)' % (w['day'], w['part']) if w['part'] else 'W%s' % w['day'],
                                      max(1, len(steps(w))))) for w in wts]
        # a facts check part named in the header ("factcols: F1=3; F2=4") follows its day's columns: its count of 36
        # (expert, day 3: the facts check had nowhere to be recorded)
        mid += [((int(v), 2), (k.strip(), 1)) for k, _, v in (x.partition('=') for x in h.get('factcols', '').split(';'))
                if v.strip().isdigit()]
        cols += [c for _, c in sorted(mid)]
        ends = [i for i in items if i['stretch'] == st and i['check'] == 'end']
        cols += [('End %s (%s)' % (i['n'], i['part']) if i['part'] else 'End %s' % i['n'], looks.get(i['n'], 1)) for i in ends]
        lf = ''.join('<p><b>W%s look-fors:</b> %s</p>' % (w['day'], '; '.join('%d. %s' % (k + 1, html.escape(s))
                     for k, s in enumerate(steps(w)))) for w in wts if steps(w))
        lf += ''.join('<p><b>End %s look-fors:</b> %s</p>' % (i['n'], '; '.join('%d. %s' % (k + 1, html.escape(s))
                      for k, s in enumerate(steps(i)))) for i in ends if i['judged'] == 'teacher' and steps(i))
        hd = '<tr><th>Student</th>%s</tr>' % ''.join('<th colspan="%d">%s</th>' % (n, html.escape(c)) for c, n in cols)
        sub = '<tr><th></th>%s</tr>' % ''.join(''.join('<th>%s</th>' % ('' if n == 1 else '%d' % (k + 1))
                                                      for k in range(n)) for _, n in cols)
        row = '<tr><td style="width:1.6in">&nbsp;</td>%s</tr>' % ('<td></td>' * sum(n for _, n in cols))
        css = ('<style>@page { size: letter landscape; margin: .4in; } body.record { max-width: none; font-size: 9pt; }'
               ' .record td { height: .26in; padding: 0 .2em; } .record th { font-size: 8pt; }</style>')
        tb = '<h1>%s</h1>%s<table>%s%s%s</table>%s%s' % (html.escape(title), mdh(body), hd, sub,
                                                       row * int(h.get('rows', 28)), lf, unit_foot(h, course, 'record sheet'))
        put(out / (name + '.html'), page(title, css + tb, 'record'), encoding='utf-8')
        return out
    # a check: the student page, a large-print copy, and the key
    rs = piece_rows(p, items)
    foot = unit_foot(h, course, 'practice sheet' if h.get('check') == 'practice' else '%s check' % h.get('check'))
    def facts_list(i):   # "lead: 6 × 7, 8 × 4, ...; 42 ÷ 6, ...": six or more bare facts, each gets its own blank
        m = re.match(r'(.*?):\s*(.+)$', stem(i), re.S)
        fs = [x.strip().rstrip('.') for x in re.split(r'[,;]', m[2])] if m else []
        return (m[1], fs) if len(fs) >= 6 and all(re.fullmatch(r'\d+ [×÷] \d+', x) for x in fs) else None

    def room(i):   # a drawing goes on grid paper; a list of facts gets a blank for each; otherwise a work box
        if re.search(r'\bgrid\b', stem(i), re.I):
            return '<p>Draw on your grid paper.%s</p>' % ('' if re.search(r'\barea \d', stem(i)) else
                                                          ' Write the area inside each.')
        if facts_list(i):
            fs = facts_list(i)[1]
            return '<table class="facts"><tr>%s</tr></table>' % ''.join(
                '<td style="border:0;width:20%%">%s = ____</td>%s' % (x, '</tr><tr>' if k % 5 == 4 else '')
                for k, x in enumerate(fs))
        if h.get('room') == 'tall':   # a whole search: a tall box and a full-width answer line (day 3 read)
            return '<div class="sketch tall"></div><p>Answer: %s</p>' % ('_' * 62)
        return '<div class="sketch work"></div><p>Answer: ______________________</p>'

    def asked(i):
        return facts_list(i)[0] + '.' if facts_list(i) else stacked(stem(i))
    sb = '<h1>%s</h1><p>Name ______________________ Date __________</p>%s%s%s' % (
        html.escape(title), mdh(section(body, 'Student') or ''), ''.join(
            '<p>%d. %s</p>%s%s' % (k + 1, asked(i), figure(i['figure'], 0.5) if i.get('figure') else '', room(i))
            for k, i in enumerate(rs)), foot)
    put(out / (name + '-student.html'), page(title, sb, 'student'), encoding='utf-8')
    put(out / (name + '-student-large.html'), page(title + ', large print', sb, 'student large'), encoding='utf-8')
    errname = {e['letter']: e['error'] for e in errors if e['stretch'] == h.get('stretch')}
    tail = lambda w: ((('error %s, %s' % (w['error'], errname.get(w['error'], '').lower())) if w['error'] else '')
                      + (' (%s)' % w['note'] if w['note'] else '')).strip()
    wr = lambda i: '; '.join(w['shown'] + (': ' + tail(w) if tail(w) else '')
                             for w in wrongs if w['item_id'] == i['item_id'])
    kr = ''.join('<tr><td>%s</td><td>%s</td><td class="q">%s</td><td>%s</td><td>%s</td></tr>' % tuple(
        html.escape(x) for x in (i['n'], part_of(i), stem(i), i['answer'], wr(i))) for i in rs)
    kb = ('<h1>%s: key</h1>%s<table><tr><th>#</th><th>Part</th><th>Question</th><th>Answer</th><th>Wrong answers and '
          'what they mean</th></tr>%s</table>%s' % (html.escape(title), mdh(section(body, 'Teacher') or ''), kr, foot))
    put(out / (name + '-key.html'), page(title + ': key', kb, 'key'), encoding='utf-8')
    return out


# ------------------------------------------------------------------ main
def load(course):
    return (plan.rows(course, 'items'), plan.rows(course, 'days'), plan.rows(course, 'parts'),
            plan.rows(course, 'errors'), plan.rows(course, 'wrongs'))


def main(a):
    if not a or a[0] not in ('check', 'build'):
        raise SystemExit(__doc__)
    bad = 0
    files = day_files()
    for c in sorted({p.parent.parent.name for p in files}):
        pf, pn, _, _ = plan.check(c)
        for x in pf:
            print('  FAIL', x)
        bad += len(pf)
    for p in files:
        d = parse(p)
        lab = p.relative_to(ROOT).as_posix()
        if d is None:
            print('  FAIL %s: no header block' % lab); bad += 1; continue
        c = d['head'].get('course', p.parent.parent.name)
        items, days, parts, errors, wrongs = load(c)
        fails = check_day(d, items, days)
        byid = {i['item_id']: i for i in items}
        side_note = 'sides not counted (no Chrome)'
        if CHROME.exists() and d['sides']:   # the two-side rule, on the printed page
            import tempfile
            tmp = Path(tempfile.gettempdir()) / ('curio-%s-%s.html' % (c, p.stem))
            put(tmp, page('check', student_html(d, c, items), 'student'))
            side_note = print_sides(tmp)
            if 'FAIL' in side_note:
                fails.append('%s: the student page prints to more than two sides' % lab)
        print('%s: teacher %d words, student %d words (%d frame, %d questions), %d min, %s, %d failure(s)' % (
            lab, words(d['teacher']), words(d['student']) + stem_words(d, byid), words(d['student']),
            stem_words(d, byid), sum(b[0] for b in d['blocks']), side_note, len(fails)))
        for x in fails:
            print('  FAIL', x)
        bad += len(fails)
        if a[0] == 'build' and not fails:
            out, note = build_day(d, c, items, days, parts, errors, wrongs, '--pdf' in a)
            print('  built %s%s' % (out.relative_to(ROOT).as_posix(), ('; student page: ' + note) if note else ''))
            if optional(d):
                print('  Uses when it exists: %s' % '; '.join(optional(d)))
            if 'FAIL' in note:
                bad += 1
    for p in piece_files():
        pc = parse_piece(p)
        lab = p.relative_to(ROOT).as_posix()
        if pc is None:
            print('  FAIL %s: no header block' % lab); bad += 1; continue
        c = pc['head'].get('course', p.parent.parent.name)
        items, days, parts, errors, wrongs = load(c)
        fails = check_piece(pc, items)
        note = ''
        if not fails and pc['head'].get('piece') in ('check', 'facts', 'blank') and CHROME.exists():
            out = build_piece(pc, items, wrongs, errors)
            note = ', student page ' + print_sides(out / (p.stem + '-student.html'))
            if 'FAIL' in note:
                fails.append('%s: the student page prints to more than two sides' % lab)
        print('%s: %s, %d words%s, %d failure(s)' % (lab, pc['head'].get('piece'), words(pc['body']), note, len(fails)))
        for x in fails:
            print('  FAIL', x)
        bad += len(fails)
        if a[0] == 'build' and not fails:
            out = build_piece(pc, items, wrongs, errors)
            print('  built %s/%s' % (out.relative_to(ROOT).as_posix(), p.stem))
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main(sys.argv[1:])

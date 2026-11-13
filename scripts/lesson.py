"""Lesson days: check each day file against docs/courses/LESSON-DAY.md and build its print pages.

    python -X utf8 scripts/lesson.py check            every day file under courses/; exit 1 on any failure
    python -X utf8 scripts/lesson.py build [--pdf]    write the pages to build/lessons/ (--pdf also prints the
                                                      student page with Chrome and counts its sides)

A day file is courses/<course>/u<unit>-<section>/d<day>.md: a header block, "## Teacher page" with fixed
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
KIND_WORD = {'Check': 'assessment'}   # days.csv kind to the word printed on the header (docs/GLOSSARY.md)
HEADER = ['day', 'course', 'unit', 'version', 'materials', 'print', 'credit', 'leans_on']
TEACHER = ['Before class', 'The day', 'Other rooms', 'At home', 'Shorter or longer', 'Words and supports', 'Tomorrow',
           'Credit']
CAP_TEACH, CAP_CHECK, CAP_BEFORE, CAP_STUDENT = 900, 500, 80, 350   # student: everything printed, stems included
CAP_HOME = 170                         # the At home block, counted apart from the teacher prose cap
HOME_TEACH, HOME_CHECK = (30, 40), (40, 50)   # minutes at home: a teaching day; an assessment day (about 45)
# TEMPORARY: sections whose days are still to get their At home block (homeschool option 1, 2026-11-12). Their days
# report "At home block missing" as a note, not a failure. The agent that writes a section's blocks removes it here;
# when the list is empty, delete it.
HOME_TODO = set()
# A part: "- **N min. Name.**", the name on one line; its closing "." may be left off, and "?" or "!" is kept.
HOME_PART = re.compile(r'^- \*\*(\d+) min\.? ([^*\n]+?[?!]?)\.?\*\*(.*?)(?=^- \*\*\d+ min|^\*\*|\Z)', re.M | re.S)
TALK = re.compile(r'\bpairs?\b|turn-and-talk|whole class|\bthe class\b|\*\*Ask\.?\*\*', re.I)
HOME_LACKS = re.compile(r'projector|grid paper|tiles|device|string loop|document camera|large tiles', re.I)
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
    md = re.sub(r'<!--.*?-->|</?[A-Za-z][^<>]*>', ' ', md, flags=re.S)   # HTML tags (a letter after <), not a < b comparisons
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


# ------------------------------------------------------------------ the At home block (homeschool option 1)
def teacher_prose(d):
    """The teacher page without its At home block, which has its own cap and its own view."""
    return re.sub(r'^### At home\n.*?(?=^### |\Z)', '', d['teacher'], flags=re.M | re.S)


def home_parts(d):
    """The At home parts, written "- **N min. Name.** ...": (minutes, name, text)."""
    return [(int(a), b.strip(), c) for a, b, c in HOME_PART.findall(d['secs'].get('At home', ''))]


def numbered_label(cur, n):
    """A numbered question under a label: "On your own 2"; under a label that ends in a number, "Set 1, question 2"
    (unit 3 reads, days 11 and 18: "Set 1 2")."""
    return '%s, question %s' % (cur, n) if cur[-1:].isdigit() else '%s %s' % (cur, n)


def page_labels(d):
    """Each question on the student page by the name a parent finds it under: "side 2, On your own 1".

    A bold label opens a group ("**On your own.**", ending in ".", "?", "!" or ":"); the group carries over to side 2
    until a new label. A label that names its own question ("**Example 2.** [[id]]") names that question only, so the
    numbered questions after it stay in the group above it ("Equation cards 1", not "Example 2 1"). A question in a
    table row with no number is named by its table and row ("Bo's stamps, row 2"): the table is the group, or the
    table's first header cell when there is no group, and a second table in one group is "table 2"."""
    lab = {}
    cur = ''
    for side, body in d['sides']:
        sn = side.lower()
        tab, tabs, row = None, 0, 0
        for ln in body.splitlines():
            m = re.match(r'\s*\*\*(?!I can)([^*]+?)[.?!:]\*\*', ln)
            if m:
                tab, tabs = None, 0
                name = m[1].strip()
                name = 'item %s' % name if name.isdigit() else name
                refs = REF.findall(ln[m.end():])[:1]
                for r in refs:   # "**Example 1.** [[id]]": the label is the question's name
                    lab.setdefault(r, '%s, %s' % (sn, name))
                if not refs:
                    cur = name
                continue
            s = ln.strip()
            if s.startswith('|'):
                if re.fullmatch(r'\|?[\s:|-]+\|?', s):   # the header rule
                    continue
                cells = [c.strip() for c in s.strip('|').split('|')]
                if tab is None:   # a new table: its first line is the header
                    tabs += 1
                    first = re.sub(r'\[\[[^]]*\]\]|\d+\.', '', cells[0]).strip()
                    tab = cur or first or 'the table'
                    if tabs > 1:
                        tab = '%s, table %d' % (tab, tabs)
                    row = 0
                    if not REF.search(s):   # a header with no question in it is not a row
                        continue
                row += 1
                numbered = dict((r, n) for n, r in re.findall(r'(\d+)\.\s*\[\[([A-Za-z0-9-]+)\]\]', s))
                for r in NOTE.findall(s)[:1] + REF.findall(s):
                    if r in numbered:
                        lab.setdefault(r, '%s, %s' % (sn, numbered_label(cur, numbered[r]) if cur else
                                                      'problem %s' % numbered[r]))
                    else:
                        lab.setdefault(r, '%s, %s, row %d' % (sn, tab, row))
                continue
            tab = None
            m = re.match(r'\s*(\d+)\.\s+.*?\[\[([A-Za-z0-9-]+)\]\]', ln)
            if m:
                lab.setdefault(m[2], '%s, %s' % (sn, numbered_label(cur, m[1]) if cur else 'problem %s' % m[1]))
                continue
            for r in REF.findall(ln):
                lab.setdefault(r, '%s, %s' % (sn, cur) if cur else sn)
    return lab


def home_todo(d):
    return d['path'].parent.name in HOME_TODO


def check_home(d, items, row, lab):
    """The At home block (LESSON-DAY.md, "At home"): minutes in the band, every item on the student page, a Say.
    line where the class talks, a Swap. line for what a home lacks, the exit ticket last, the cap."""
    f = []
    if 'At home' not in d['secs']:
        if home_todo(d):
            return ['NOTE %s: At home block missing (section %s is on the backfill list, HOME_TODO in lesson.py)'
                    % (lab, d['path'].parent.name)]
        return ['%s: At home block missing' % lab]
    home, h = d['secs']['At home'], d['head']
    assess = row['kind'] == 'Check'
    for ln in re.findall(r'^- \*\*\d.*$', home, re.M):   # a part line the parser cannot read
        if not HOME_PART.match(ln):
            f.append('%s: At home part "%s" is not written "- **N min. Name.** ..." (minutes, then the name, both '
                     'inside one pair of ** on one line)' % (lab, ln[:50]))
    parts = home_parts(d)
    if not parts:
        return f + ['%s: At home has no parts written "- **N min. Name.** ..."' % lab]
    lo, hi = HOME_CHECK if assess else HOME_TEACH
    tot = sum(p[0] for p in parts)
    if not lo <= tot <= hi:
        f.append('%s: At home parts add to %d minutes; %s %d to %d' % (
            lab, tot, 'an assessment day runs' if assess else 'a teaching day runs', lo, hi))
    hw = words(home)
    if hw > CAP_HOME:
        f.append('%s: At home is %d words; the cap is %d' % (lab, hw, CAP_HOME))
    labels = page_labels(d)
    byid = {i['item_id']: i for i in items}
    exits = [i['item_id'] for i in items if i['day'] == h.get('day') and i['check'] == 'exit'
             and i.get('path', '') in ('', 'paper')]
    for r in REF.findall(home):
        if r not in labels and r not in exits:
            f.append('%s: At home names [[%s]], which is not on the student page%s' % (
                lab, r, '' if r in byid else ' (and has no row)'))
    if STEPS.search(home) or NOTE.search(home) or FIG.search(home):
        f.append('%s: At home names questions as [[id]] only; the view prints each one with its question' % lab)
    if TALK.search(d['secs'].get('The day', '')) and not re.search(r'\*\*Say\.\*\* ', home):
        f.append('%s: the class talks in pairs or as a class, but At home has no **Say.** line for the parent' % lab)
    for m in re.finditer(r'\*\*Say\.\*\* (.*?)(?=\n\s*\n|\Z)', home, re.S):
        if not re.search(r'\bExpect\b', m[1]):
            f.append('%s: an At home **Say.** line gives no answer to expect ("Expect: ...")' % lab)
    if HOME_LACKS.search(h.get('materials', '')) and not re.search(r'^\*\*Swap\.\*\* ', home, re.M):
        f.append('%s: the materials need things a home may lack, but At home has no **Swap.** line' % lab)
    if not re.search(r'^\*\*Skip\.\*\* ', home, re.M):
        f.append('%s: At home has no **Skip.** line (what to leave out)' % lab)
    if assess:
        if not re.search(r'assessment', parts[0][1], re.I):
            f.append('%s: on an assessment day the At home path opens with the assessment' % lab)
        for i in items:   # the view prints every end item (day 24 read); each must be found on the page
            if i['day'] == h.get('day') and i['check'] == 'end' and i['item_id'] not in labels:
                f.append('%s: end item %s is not on the student page, so the At home view cannot say where it is'
                         % (lab, i['item_id']))
    else:
        last = parts[-1]
        if not re.search(r'exit ticket', last[1], re.I):
            f.append('%s: the last At home part is "%s"; on a teaching day it is the exit ticket' % (lab, last[1]))
        elif exits and not set(exits) <= set(REF.findall(last[2])):
            f.append('%s: the At home exit ticket part does not name the paper exit row(s) %s'
                     % (lab, ', '.join(exits)))
    if re.search(r'\btimer\b|\bscores?\b|\bgrades?\b(?! \d)|\bpoints\b|\bpercent', home, re.I):
        f.append('%s: At home shows no timer, grade or score' % lab)
    if re.search(r'one child at home', d['secs'].get('Other rooms', ''), re.I):
        f.append('%s: "One child at home" now lives in At home; take it out of Other rooms' % lab)
    return f


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
        f.append('%s: header unit (section) %s, but days.csv says %s' % (lab, h.get('unit'), row['unit']))
    want = [s for s in TEACHER if s != 'At home' or 'At home' in d['order']]   # a missing block is reported below
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
    elif row.get('check_min'):   # an assessment day's parts follow check_min, in order ("end-of-unit assessment 30; respond 20; ...")
        want = [int(re.findall(r'\d+', re.sub(r'\(.*?\)', '', s))[-1]) for s in row['check_min'].split(';')
                if re.findall(r'\d+', re.sub(r'\(.*?\)', '', s))]
        got = [b[0] for b in d['blocks']]
        if got != want:
            f.append('%s: the parts run %s min; days.csv check_min says %s' % (lab, got, want))
    # Tomorrow: the next day by number, in any section folder of the course, must carry the hand-off ("day N" in it)
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
        if (re.search(r'display shows the answers|answers on the (?:display|screen)', btxt, re.I)
                and not re.search(r'^Check(?: \(sort\))?: ', btxt, re.M)
                and not re.search(r'swap and check|swap and compare|partner check|check their own|partners check', btxt, re.I)
                and not re.search(r'=\s*\?', btxt)
                # a row the student page does not print gets its answers screen anyway (the build's warm-up rule)
                # and a plain sum ("64 ÷ 8 = ?") gets its check screen (day 81)
                and not any(r not in REF.findall(d['student']) or any(
                    re.search(r'=\s*\?\s*$', stem(i)) for i in items if i['item_id'] == r) for r in REF.findall(btxt))):
            f.append('%s: "%s" says the display shows the answers but has no Check: line to build that screen' % (lab, bname))
        # a warm-up asks questions; every question is a row (rule 1), so the warm-up names one
        if (not check_day_kind and bname.lower().startswith('warm-up') and not REF.search(btxt)
                and not re.search(r'facts check|sheet|count aloud', btxt, re.I)):
            f.append('%s: the warm-up names no [[id]]; its questions must be rows (rule 1)' % lab)
    # a planned question is written **Ask.**; "**Ask** (after step 4)." built no screen (unit 2 reads, days 7, 8)
    for m in re.finditer(r'\*\*Ask\*\*', d['teacher']):
        f.append('%s: write the planned question as "**Ask.**" (the period inside the bold), not "%s"'
                 % (lab, d['teacher'][m.start():m.end() + 20].split('\n')[0]))
    # "under the camera" on a day whose materials say there is none (unit 2 reads, day 7; day 1 before it)
    if re.search(r'no document camera', h.get('materials', ''), re.I) and re.search(
            r'under the camera', teacher_prose(d), re.I):
        f.append('NOTE %s: the page says "under the camera", but the materials say no document camera' % lab)
    # an assessment day's teacher-judged items go back the next day: that day names them (unit 2 reads, day 9
    # finding 6: the written-task gate read practice rows only, so day 10 passed without items 3 and 5)
    if check_day_kind and nf:
        nt = nf.read_text(encoding='utf-8')
        dn = int(h.get('day', 0) or 0)
        judged = [i for i in items if i['day'] == h.get('day') and i['check'] == 'end' and i['judged'] == 'teacher']
        if judged and not re.search(r"\bday\s+%d(?:'s)?\s+(?:end-of-unit\s+)?(?:assessments?|items?)\b" % dn, nt, re.I):
            f.append('%s: items %s are judged after class, but day %d never hands back "day %d\'s assessment"'
                     % (lab, ' and '.join(i['n'] for i in judged), dn + 1, dn))
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
    tw = words(teacher_prose(d))   # the At home block has its own cap (check_home)
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
                continue   # a board row printed by the section's sheet piece, or a fixed practice sheet's row
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
                elif spec.startswith('cols'):   # the two numbers, and a wrong answer drawn for a fix
                    cm = re.match(r'(\d+)\s*[+−-]\s*(\d+)$', spec.split()[1])
                    if not cm:
                        f.append('%s: %s figure: cols needs two numbers, as cols 3746+2538' % (lab, r)); continue
                    sn = {x.replace(',', '') for x in sn}
                    ff = fig_fields(spec)[0]
                    fv = [cm[1], cm[2]] + ([ff['ans']] if 'ans' in ff and '/' not in ff['ans'] else [])
                elif kind(spec) in FRACTION_FIGS:
                    try:
                        vs = spec if ex else fig_view(spec, 'student')   # 'then' lines are not printed for it
                        fv = line_numbers(vs) if kind(spec) == 'line' else fstrip_numbers(vs)
                        figure(spec)
                    except (ValueError, ZeroDivisionError) as e:
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
            f.append('%s: exit question %s is printed on the student page; it belongs on the exit ticket' % (lab, r))
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
    f += check_lists(d, items, lab)
    f += check_home(d, items, row, lab)
    f += check_reads3(d, items, row, lab, nf)
    f += check_reads4(d, items, row, days, lab, nf)
    return f


REASON = re.compile(r'\b(?:why|because|how I know|how do you know|what went wrong|explain|I notice|reason)\b', re.I)


def body_of(path):
    """A day file's text without its header block."""
    return re.sub(r'^---.*?---', '', path.read_text(encoding='utf-8'), flags=re.S)


def check_reads4(d, items, row, days, lab, nf):
    """Gates from grouping every cheap and expert finding of units 1, 2, 3, 9, 10 and 11 (2026-11-12): the exit
    tickets go back, the seam between units, room for a challenge and a reason, an assessment day collects, and
    (a note) a respond group for every letter the end items can show."""
    f, h = [], d['head']
    n = int(h.get('day', 0) or 0)
    check_kind = row['kind'] == 'Check'
    # the exit tickets of a teaching day come back the next day (days 8, 13, 14, 20: tickets with no hand-back)
    if nf and not check_kind:
        ex = [i['item_id'] for i in items if i['day'] == str(n) and i['check'] == 'exit'
              and i.get('path', '') in ('', 'paper')]
        nb = body_of(nf)
        if ex and not (re.search(r'\bE%d\b' % n, nb) or any(e in nb for e in ex)
                       or re.search(r"\bday %d'?s? (?:exit )?(?:tickets?|exit)\b" % n, nb, re.I)):
            f.append('%s: day %d never picks up day %d\'s exit tickets (name "E%d", the exit id, or "day %d\'s '
                     'tickets")' % (lab, n + 1, n, n, n))
    # the seam between units (unit 2 reads: day 9 to day 10 broke): the first day of a unit reads the last day of the
    # unit before, names it, and that day's Tomorrow names this one
    prev = next((x for x in days if x['day'] == str(n - 1)), None)
    if prev is None and n > 1:
        f.append('NOTE %s: day %d has no days.csv row (its unit is not in data yet); read its plan for what it hands on'
                 % (lab, n - 1))
    elif prev and prev['stretch'] != row['stretch']:
        pf = next(iter(sorted(d['path'].parent.parent.glob('u*/d%03d.md' % (n - 1)))), None)
        if pf is None:
            f.append('NOTE %s: the first day of unit %s; day %d (%s) is not written, so read its days.csv row and plan '
                     'for what it hands on' % (lab, row['stretch'], n - 1, prev['unit']))
        else:
            if not re.search(r'\bday %d\b' % (n - 1), body_of(d['path']), re.I):
                f.append('%s: the first day of unit %s never names day %d, the last day before it; pick up its '
                         'Tomorrow' % (lab, row['stretch'], n - 1))
            if not re.search(r'\bday %d\b' % n, parse(pf)['secs'].get('Tomorrow', ''), re.I):
                f.append('%s: "Tomorrow" of day %d (%s) never names day %d, the first day of unit %s'
                         % (lab, n - 1, pf.relative_to(ROOT).as_posix(), n, row['stretch']))
    # room on the student page (cheap reads, every unit: one short line for a challenge or a reason)
    byid = {i['item_id']: i for i in items}
    s = d['student']
    refs = [(m.start(), m[1]) for m in REF.finditer(s)]
    for k, (pos, r) in enumerate(refs):
        if byid.get(r, {}).get('check') == 'challenge':
            seg = re.split(r'\n\*\*|\n###', s[pos:refs[k + 1][0] if k + 1 < len(refs) else len(s)])[0]
            if not re.search(r'_{4,}|\{(?:sketch|work|small|tall)\}|^\|', seg, re.M) and not re.search(
                    r'paper|\bback\b|notebook', seg, re.I):
                f.append('%s: challenge %s has no room to answer on the page (a line, a box, or "on the back")' % (lab, r))
    for ln in s.splitlines():
        bl = re.findall(r'_{2,}', ln)
        if (REASON.search(ln) and bl and max(map(len, bl)) < 20 and not ln.lstrip().startswith('|')
                and not re.search(r'[=×]', ln)):
            f.append('%s: a reason line has only a short blank ("%s"); give it a full-width line' % (lab, ln.strip()[:50]))
    if check_kind:
        td = d['secs'].get('The day', '')
        # an assessment day collects the pages (day 24: nothing collected them)
        if not re.search(r'\bcollect', td, re.I):
            f.append('%s: an assessment day that never says when the pages are collected' % lab)
        # every letter an end item's wrong rows can show has a respond group (days 9, 24, 88: groups that did not
        # fit the register); a note, since a teacher-judged item may go back the next day instead
        named = set()
        for a, b in re.findall(r'\b([A-K]) to ([A-K])\b', td):
            named |= {chr(c) for c in range(ord(a), ord(b) + 1)}
        for x in 'ABCDEFGHIJK':
            if re.search(r'\(%s\)|\berrors? %s\b|^- %s\b|\b%s\b(?= and| or|,|\)| group| pile| students|\.| \()|'
                         r'(?:and|or|,|\() ?%s\b' % ((x,) * 5), td, re.M):
                named.add(x)
        ends = {i['item_id'] for i in items if i['day'] == str(n) and i['check'] == 'end'}
        rows_ = _WRONGS.get(h.get('course', '')) or plan.rows(h.get('course', ''), 'wrongs')
        miss = sorted({w['error'] for w in rows_ if w['item_id'] in ends and w['error'] not in ('', 'x')} - named)
        if miss:
            f.append('NOTE %s: end items can show error(s) %s, but the respond part names no group for them'
                     % (lab, ', '.join(miss)))
    return f


NUM_WORD = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6}
PARTNER = re.compile(r'partners? (?:swap|check)|swap (?:pages|and)|partner check|check their own', re.I)
PEER = re.compile(r'swap and check|swap and compare|partner check|check their own|partners check', re.I)


def side_text(body):
    """A student side's words, squeezed for a contains test: lower case, letters and digits only."""
    return re.sub(r'[^a-z0-9]', '', body.lower())


def check_reads3(d, items, row, lab, nf):
    """Gates from the unit 3 reads (2026-11-12): pieces that exist, a check screen for every set and partner check,
    hand-drawn strips, frames that print as mixed numbers or where they are said to, exit room, and the papers the
    day and its opener name (the last three as notes)."""
    f, h = [], d['head']
    byid = {i['item_id']: i for i in items}
    for x in optional(d):   # day 14 read: "when it exists" for course pieces that exist (a tool's file may exist
        if x.startswith('courses/') and (ROOT / x).exists():   # before the tool is done, so tools are left out)
            f.append('%s: leans_on says "when it exists: %s", but it exists; name it plainly and drop the fallback'
                     % (lab, x))
    for bi, (_, bname, btxt) in enumerate(d['blocks']):
        checks = len(re.findall(r'^Check(?: \(sort\))?: ', btxt, re.M))
        later = sum(len(re.findall(r'^Check(?: \(sort\))?: ', b[2], re.M)) for b in d['blocks'][bi:])
        for ln in btxt.splitlines():   # day 21 read: a Check: sentence mid-paragraph builds no screen
            if re.search(r'\S.*?\bCheck(?: \(sort\))?: ', ln) and not re.match(r'\s*Check(?: \(sort\))?: ', ln):
                f.append('%s: "%s" has "Check:" inside a line; it builds a screen only at the start of its own line'
                         % (lab, bname))
                break
        if re.search(r'\bafter each set\b', btxt, re.I):   # day 15 read: one check screen for four sets
            nm = re.search(r'\b(two|three|four|five|six|[2-6])\s+(?:short\s+)?sets\b', btxt, re.I)
            sets = (NUM_WORD.get(nm[1].lower()) or int(nm[1])) if nm else \
                len(set(re.findall(r'\bSet ([A-Z1-9])\b', btxt))) or None
            if later < (sets or 2):   # its sets may run on into the parts after it (day 73)
                f.append('%s: "%s" checks "after each set" but has %d Check: line(s) for %s sets' % (
                    lab, bname, later, sets or 'several'))
        if PARTNER.search(btxt) and not checks and not PEER.search(btxt):
            f.append('%s: "%s" has a partner check with no "Check:" line, so the display has no answers to check '
                     'against' % (lab, bname))
    # day 14 read: a strip typed as a table of shaded cells prints unequal; it is an fstrip figure
    drawn = 0
    for tb in re.findall(r'(?:^[ \t]*\|.*\|[ \t]*\n?)+', d['student'], re.M):
        cells = [c.strip() for ln in tb.splitlines() if not re.fullmatch(r'[\s|:-]+', ln)
                 for c in ln.strip().strip('|').split('|')]
        drawn += bool(any(cells) and all(c == '■' for c in cells if c))
    if drawn:
        f.append('%s: %d student table(s) of only ■ cells are hand-drawn strips; draw each as an fstrip figure '
                 '([[fig:id]], ask= to print the question only)' % (lab, drawn))
    # day 20 read: "__/15   4/5" prints as "15 4/5", a mixed number
    for ln in d['student'].splitlines():
        if re.search(r'/\d+\s+\d+/\d+', ln):
            f.append('%s: a student line runs a fraction into a number ("%s"), which prints as a mixed number; put '
                     'words or a comma between them' % (lab, re.search(r'\S*/\d+\s+\d+/\d+', ln)[0]))
    # day 19 read: a frame the teacher page says is printed on a side must be on that side
    ws = d['secs'].get('Words and supports', '')
    sides = dict(d['sides'])
    for m in re.finditer(r'Frames? on ([^:."]*?):\s*((?:"[^"]*"\s*)+)', ws):
        where = [s for s in sides if s.lower() in m[1].lower()] or (
            list(sides) if 'student page' in m[1].lower() else [])
        if not where:
            continue
        page_t = side_text(re.sub(r'<[^>]+>', '', md(''.join(sides[s] for s in where), items)))
        for q in re.findall(r'"([^"]*)"', m[2]):
            if side_text(q.replace('__', '')) not in page_t:
                f.append('%s: Words and supports puts the frame "%s" on %s, which does not print it'
                         % (lab, q[:40], ' and '.join(where).lower()))
    # day 21 read: an exit with no room to write
    for k, i in enumerate(x for x in items if x['day'] == h.get('day') and x['check'] == 'exit'
                          and x.get('path', '') in ('', 'paper')):
        if row['kind'] != 'Check' and not re.search(r'class="blank"|_{4,}|class="sketch|<table', slip_item(k, i)):
            f.append('%s: exit %s leaves no room to write on the ticket' % (lab, i['item_id']))
    # notes: a fraction Tomorrow sends that the next day never names; the papers the day names
    tm = d['secs'].get('Tomorrow', '')
    if nf:
        nt = nf.read_text(encoding='utf-8')
        sent = ' '.join(re.findall(r'\bday %d\b([^.]*)' % (int(h['day']) + 1), tm))   # what it says day N+1 does
        for fr in sorted(set(re.findall(r'(?<![\d/])\d+/\d+(?![\d/])', sent))):
            if not re.search(r'(?<![\d/])%s(?![\d/])' % re.escape(fr), nt + ''.join(
                    i['stem'] + i['answer'] for i in items if '[[%s]]' % i['item_id'] in nt)):
                f.append('NOTE %s: "Tomorrow" names %s, which day %d never shows' % (lab, fr, int(h['day']) + 1))
    for what, n in re.findall(r'([^;,()]*?) from (?:the )?days? (\d+)', h.get('materials', '')):
        noun = re.findall(r'[a-z]+', what.lower())
        src = next(iter(sorted(d['path'].parent.parent.glob('u*/d%03d.md' % int(n)))), None)
        if noun and src and not re.search(r'\b%s' % noun[-1].rstrip('s'), src.read_text(encoding='utf-8'), re.I):
            f.append('NOTE %s: materials take "%s" from day %s, which never names %s' % (lab, what.strip(), n, noun[-1]))
    head = ' '.join(h.get(k, '') for k in ('materials', 'print', 'leans_on')).lower()
    held = (r'\b(?:fold|folds|cut|cuts|hold|holds|lay|lays|hand out|give out|take out)\s+(?:up\s+)?'
            r'(?:(?:the|their|your|two|a|an|each|one|large|long|paper|sign)\s+)*(?:[a-z]+\s+)?(strips?|cards?|sheets?)\b')
    for noun in sorted({m.lower().rstrip('s') for m in re.findall(held, d['secs'].get('The day', ''), re.I)}):
        if noun not in head:
            f.append('NOTE %s: the day uses %ss, which no materials, print or leans_on line names' % (lab, noun))
    op = d['path'].parent / 'opener.md'
    if op.exists():
        sup = op.read_text(encoding='utf-8').split('## Supplies for the section')[-1].split('\n## ')[0]
        files = dict((n.lower(), fn) for n, fn in re.findall(r'[Tt]he ([a-z ]+? sheet) \(([\w-]+)\.md\)',
                                                              op.read_text(encoding='utf-8')))
        for name, dd in re.findall(r'the ([a-z ]+? sheet) \((days? [^)]*)\)', sup):
            nums = [int(x) for x in re.findall(r'\d+', dd)]
            if re.search(r'\bto\b', dd) and len(nums) == 2:
                nums = list(range(nums[0], nums[1] + 1))
            said = [re.escape(name)] + ([re.escape(files[name])] if name in files else [])
            if int(h.get('day', 0)) in nums and not re.search('|'.join(said), d['path'].read_text(encoding='utf-8'),
                                                                 re.I):
                f.append('NOTE %s: the section opener lists "the %s" for this day, which never names it' % (lab, name))
    return f


_WRONGS = {}


def check_lists(d, items, lab):
    """Gates from the unit 9 reads (2026-11-12): what the opener sends home, the papers the prose uses, the
    branches an exit ticket can trigger, and the student page in the day's order."""
    f, h = [], d['head']
    day, course = h.get('day', ''), h.get('course', '')
    prn = h.get('print', '').lower()
    # the opener names a day for the family note; that day prints it (day 72: no day printed the note)
    op = d['path'].parent / 'opener.md'
    if op.exists():
        m = re.search(r'family note\b(?:\s*\([^)]*\))?[^.]*?goes home on day (\d+)', op.read_text(encoding='utf-8'), re.I)
        if m and m[1] == day and 'family note' not in prn:
            f.append('%s: the opener sends the family note home on day %s, but the print line does not list it' % (lab, day))
    # grid paper or the column sheet used in the day's parts is on the print line (days 73, 76, 77)
    the_day = d['secs'].get('The day', '')
    # (grid paper is a supply: the materials line will do; the column sheet is a page Curio Class prints)
    mat = h.get('materials', '').lower()
    for name, pat, where in (('grid paper', r'grid paper', prn + ' ' + mat), ('the column sheet', r'columns? sheet', prn)):
        if re.search(pat, the_day, re.I) and not re.search(pat, where, re.I):
            f.append('%s: the day uses %s, but the %s line does not list it' % (
                lab, name, 'print' if name != 'grid paper' else 'materials or print'))
    # an "If many X" branch on the exit tickets of day N-1 needs a wrong answer for X on that exit (day 76: a B branch E75
    # could not show)
    if course not in _WRONGS:
        _WRONGS[course] = plan.rows(course, 'wrongs') if (plan.ROOT / 'data' / 'plans' / course / 'wrongs.csv').exists() else []
    for _, bname, btxt in d['blocks']:
        m = re.match(r'E(\d+) back', bname)
        if not m:
            continue
        exits = {i['item_id'] for i in items if i['day'] == m[1] and i['check'] == 'exit'}
        have = {w['error'] for w in _WRONGS[course] if w['item_id'] in exits}
        for par in re.split(r'\n\s*\n', btxt):
            if re.match(r'\s*\*\*If many [A-I]\b', par) or re.search(r"tickets showed many [A-I]\b", par):
                for L in re.findall(r'\bmany ([A-I])\b', par.split('**:')[0] if '**:' in par else par.split(':')[0]):
                    if exits and L not in have:
                        f.append('%s: "%s" has a branch for many %s, but no wrong answer on E%s shows %s' % (lab, bname, L, m[1], L))
    # the student page runs in the order the day teaches it, or the part says to turn back (days 73 and 76)
    taught = [r for r in REF.findall(the_day)]
    first = {}
    for k, r in enumerate(taught):
        first.setdefault(r, k)
    page = [r for r in REF.findall(d['student']) if r in first]
    seen = []
    for r in page:
        if r not in seen:
            seen.append(r)
    for a, b in zip(seen, seen[1:]):
        if first[b] < first[a] and not re.search(r'turn back to side', the_day, re.I):
            # a note, not a failure: units 10 and 11 have pages in this order, read and kept
            f.append('NOTE %s: the student page prints %s before %s, but the day teaches them the other way round'
                     % (lab, a, b))
            break
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
.student table.digits { table-layout: fixed; width: auto; } .student table.digits td { width: .55in; text-align: center; } .student table.digits td:first-child { width: .3in; }
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
    """A row's n in natural order: '2' before '10', and '9.1a', '9.1b', '9.2a' (unit 9's assessment numbers)."""
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
        cells = [re.sub(r'<.*?>', '', c).strip() for c in re.findall(r'<th[^>]*>(.*?)</th>', hd[1], re.S)] if hd else []
        # a first row of numbered questions ("1. 573 + 248") is a row to answer, not a header (s09 expert, day 72)
        asks = any(cells) and all(re.match(r'\d+\.\s', c) for c in cells if c)
        if hd and (asks or n > 3 and all(not c for c in cells[1:])):
            row = re.sub(r'<th([^>]*)>', r'<td\1>', hd[1]).replace('</th>', '</td>')
            tb = tb.replace(hd[0], '').replace('<tbody>', '<tbody><tr>%s</tr>' % row, 1)
        # a digit grid (a sign, then one digit a cell) prints equal columns, the sign cell narrow, so a new place
        # looks like any other place (s09 expert, day 77)
        every = [re.sub(r'<.*?>', '', c).strip() for c in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', tb, re.S)]
        if n >= 4 and every and all(re.fullmatch(r'[0-9+−-]?', c) for c in every) and any(c.isdigit() for c in every):
            tb = tb.replace('<table class="%s">' % kind, '<table class="digits">', 1)
        return tb
    return re.sub(r'<table>.*?</table>', one, h, flags=re.S)


def part_lines(s):
    """A question in parts, (a), (b), (c), prints one part to a line on the student page (unit 3 reads)."""
    if '(a)' not in s or '(b)' not in s:
        return s
    return re.sub(r'(?<=\S)\s+\(([a-h])\)\s', r'<br>(\1) ', s)


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
            return part_lines(stacked(stem(i)))
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
        cap = '' if kind(figures(i)[0]) in ('strip',) + FRACTION_FIGS else ';max-width:3.4in'   # a rectangle at full width runs long
        div = '<div class="fig" style="margin:.2em 0%s">%s</div>' % (cap, student_fig(figures(i)[0]))
        ls = m.string.rfind('\n', 0, m.start()) + 1
        if m.start() > ls and not m.string[ls:m.start()].strip():
            # indented under a numbered item: an inline span, so markdown keeps it and the lines after it in the item
            return div.replace('<div class="fig" style="', '<span class="fig" style="display:block;', 1)[:-6] + '</span>'
        return '\n\n%s\n\n' % div
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
    """A figure cell drawn as inline SVG: a strip diagram ('strip ...'), dots in rows ('rows ...'), place-value
    columns ('cols ...'), number lines ('line ...'), fraction strips ('fstrip ...') or a labelled rectangle
    ('rect ...')."""
    if not spec:
        return ''
    if spec.split()[0] == 'strip':
        return strip(spec, size)
    if spec.split()[0] == 'rows':
        return rows_fig(spec, size)
    if spec.split()[0] == 'cols':
        return cols(spec, size)
    if spec.split()[0] == 'line':
        return numline(spec, size)
    if spec.split()[0] == 'fstrip':
        return fstrip(spec, size)
    if spec.split()[0] == 'tiles':
        return tiles(spec, size)
    return rect(spec, size)


FRACTION_FIGS = ('line', 'fstrip')   # number lines and fraction strips: drawn on exit tickets too
STUDENT_LINE = 38   # FIG_FS (30) prints at 11 point; 38 at 14; a number line's words and fractions on the student page: 14 point (day 12 read)


def student_fig(spec):
    """A figure cell as the student page draws it: what fig_view keeps for the student; a number line's labels at
    the page's 14 point, other kinds at the usual small size."""
    v = fig_view(spec, 'student')
    return numline(v, 0.6, fs=STUDENT_LINE) if kind(v) == 'line' else figure(v, 0.6)


def kind(spec):
    return spec.split()[0] if spec else ''


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


def tiles(spec, size=1.0):
    """The steps of a shape pattern side by side, each labelled under it: 'tiles #/# ##/## ###/###' is columns of
    2; a step's rows run top to bottom, split by /, # a square and . a gap ('tiles # .#./###/.#.' is a plus sign
    growing). The flag 'sticks' draws each square as four sticks, unfilled (unit 2 reads, day 8: a shape-pattern
    day drew no shape anywhere). Options with = (at=2) are the display's, not the picture's."""
    toks = spec.split()[1:]
    sticks = 'sticks' in toks
    st = [t.split('/') for t in toks if t != 'sticks' and '=' not in t]
    d, gap, lab = 30, 50, 34
    hmax = max(len(g) for g in st)
    W = sum(max(len(r) for r in g) * d for g in st) + gap * (len(st) + 1)
    H = hmax * d + lab + 20
    out, x0 = [], gap
    for k, g in enumerate(st):
        w = max(len(r) for r in g)
        top = 10 + (hmax - len(g)) * d   # every step sits on one floor line
        for ri, r in enumerate(g):
            for ci, c in enumerate(r):
                if c == '#':
                    out.append('<rect x="%d" y="%d" width="%d" height="%d" %s/>' % (
                        x0 + ci * d, top + ri * d, d, d, 'fill="none" stroke="#000" stroke-width="5"' if sticks
                        else 'fill="#ddd" stroke="#000" stroke-width="2"'))
        out.append('<text x="%d" y="%d" font-size="22" text-anchor="middle">Step %d</text>' % (
            x0 + w * d / 2, 10 + hmax * d + lab - 6, k + 1))
        x0 += w * d + gap
    n = [sum(r.count('#') for r in g) for g in st]
    alt = 'Steps 1 to %d of the shape pattern: %s %s' % (len(st), ', '.join(map(str, n)), 'squares of sticks'
                                                           if sticks else 'squares')
    wid = 'width:100%%;max-width:%.1fin' % min(9, W / 30 * 0.3 * (1 if size >= 1 else 0.8))
    return ('<svg viewBox="0 0 %d %d" style="%s;height:auto" role="img" aria-label="%s" '
            'xmlns="http://www.w3.org/2000/svg" font-family="Georgia, serif">%s</svg>') % (
        W, H, wid, html.escape(alt), ''.join(out))


PARTS_WORD = {1: 'wholes', 2: 'halves', 3: 'thirds', 4: 'fourths', 5: 'fifths', 6: 'sixths', 7: 'sevenths',
              8: 'eighths', 9: 'ninths', 10: 'tenths', 12: 'twelfths', 15: 'fifteenths', 16: 'sixteenths',
              20: 'twentieths', 24: 'twenty-fourths', 30: 'thirtieths', 100: 'hundredths'}
FIG_FS = 30   # the font of the fraction figures' drawing space: at size 0.6 it prints at about 11 point


def fig_style(W, H, size, fs=FIG_FS):
    """Full size fills the width (the display); a smaller size prints its words at about 11 point on a page and
    shrinks to fit a narrow place (an exit ticket), never past its box."""
    if size >= 1:
        return 'width:100%;max-width:9in;height:auto'
    return 'display:block;width:%.2fin;max-width:100%%;height:auto' % (W / fs * 11 / 72 * size / 0.6)


def sfrac(x, y, v, fs, anchor='middle'):
    """A number as SVG text with its baseline at y: '3/4' stacked (numerator over a bar over denominator), whole
    numbers and '?' on one line. Returns (svg, height above the baseline)."""
    t = lambda yy, s: '<text x="%.0f" y="%.0f" text-anchor="%s" font-size="%d">%s</text>' % (x, yy, anchor, fs, html.escape(s))
    if '/' not in v:
        return t(y, v), fs * 0.75
    n, d = v.split('/', 1)
    w = max(len(n), len(d)) * fs * 0.56 + 6
    x1 = x - w / 2 if anchor == 'middle' else x - w if anchor == 'end' else x
    # Georgia's figures hang below the line (old style), so the bar sits well under the numerator's baseline
    return (t(y - fs * 1.32, n) + '<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f" stroke="#000" stroke-width="2"/>'
            % (x1, y - fs * 1.02, x1 + w, y - fs * 1.02) + t(y, d)), fs * 2.1


def line_rows(spec):
    """'line to=2 d=4 sub=3 pt=7/4 / d=12 blank=21/12' as (options, rows): options hold to= and the names flag;
    each row (split at a lone '/') holds d, sub, lab, pt, blank, seg and name."""
    opts, rows = {'to': '1', 'names': False}, [{}]
    for tok in spec.split()[1:]:
        if tok == '/':
            rows.append({})
        elif tok == 'names':
            opts['names'] = True
        elif tok == 'then':   # a line for the key and the display only (fig_split); drawn here like any other
            rows[-1]['then'] = True
        elif '=' in tok:
            k, v = tok.split('=', 1)
            if k in ('to', 'scale', 'ask', 'by'):
                opts[k] = v
            elif k in ('d', 'sub', 'lab', 'pt', 'blank', 'seg', 'name'):
                rows[-1][k] = v
            else:
                raise ValueError('line figure: "%s" is not to=, d=, sub=, lab=, pt=, blank=, seg=, name=, ask= or by='
                                 % tok)
        else:
            raise ValueError('line figure: "%s" is not a field (to=, d=, ...), the names flag, then or a lone /' % tok)
    if 'ask' in opts and not re.fullmatch(r'\d', opts['ask']):
        raise ValueError('line figure: ask= is the number of lines printed whole on the student page, as ask=1')
    if 'by' in opts and not re.fullmatch(r'(?:[-*]|\d+)(?:,(?:[-*]|\d+))*', opts['by']):
        raise ValueError('line figure: by= lists the lines shown on each screen, as by=-,1,1,2,* ("-" none, "*" all)')
    for r in rows:
        if not re.fullmatch(r'\d+', r.get('d', '')):
            raise ValueError('line figure: each line needs d= (the parts in one whole), as d=4')
    if not re.fullmatch(r'[1-9]', opts['to']):
        raise ValueError('line figure: to= is a whole number, as to=1 or to=2')
    return opts, rows


def line_numbers(spec, then=None):
    """The numbers a line figure prints as given (its points, a strip laid on it, a listed label), for the
    figure-and-stem gate. A blank point is the student's to name, and tick labels come from d=, so neither counts.
    then=False counts only the lines the student page prints, then=True only the 'then' lines."""
    out = []
    for r in line_rows(spec)[1]:
        if then is not None and bool(r.get('then')) != then:
            continue
        for k in ('pt', 'seg'):
            out += [v for v in r.get(k, '').split(',') if v]
        if r.get('lab', '') not in ('', 'all', 'none', 'whole'):
            out += [v for v in r['lab'].split(',') if v and v != '0']
    return out


def numline(spec, size=1.0, upto=None, span=900, ffs=26, fs=FIG_FS):
    """Number lines from a figure cell, stacked to one scale so a point on one sits straight above the same amount
    on the next: 'line to=1 d=4 pt=3/4 / d=8'. to= the range from 0 (1 or 2); per line, split by a lone '/':
    d= the parts in one whole (ticks), sub= cuts each part again with short ticks, lab= the labels under the ticks
    (whole: 0, 1, 2, the default; all: every tick, as fractions between the wholes; none; or a list, 0,1/4,1),
    pt= points marked and named above the line (pt=3/4,5/4), blank= points marked with
    an empty box above for the student to write the name, seg= a shaded strip lying on the line from 0, name= a
    word at the left ('names' writes each line's parts word: fourths). upto=n draws only the first n lines;
    span is the drawn length from 0 to the end (an exit ticket draws it shorter, so its words keep their size);
    ffs is the fractions' size (the student page draws them as big as the words: STUDENT_LINE)."""
    opts, rows = line_rows(spec)
    to = int(opts['to'])
    bw, bh = 92, 116   # a blank box: room for a written fraction at the printed size
    word = lambda r: r.get('name', '').replace('_', ' ') or (PARTS_WORD.get(int(r['d']), '') if opts['names'] else '')
    lw = max([len(word(r)) * fs * 0.52 for r in rows] + [0])
    x0 = (lw + 24 if lw else 0) + 30
    X = lambda v: x0 + float(Fraction(v)) * span / to
    out, y = [], 6
    for ri, r in enumerate(rows):
        if upto is not None and ri == upto:
            hidden = len(out)
        d = int(r['d'])
        sub = int(r.get('sub', '1') or 1)
        pts = [v for v in r.get('pt', '').split(',') if v]
        blanks = [v for v in r.get('blank', '').split(',') if v]
        lab = r.get('lab', 'whole')
        listed = lab.split(',') if lab not in ('whole', 'all', 'none') else []
        fr = (lab == 'all' and d > 1) or any('/' in v for v in listed)
        top = max([bh + 18] * bool(blanks) + [ffs * 2.15 + 22] * any('/' in v for v in pts)
                  + [fs * 0.8 + 22] * bool(pts) + [18] * bool(r.get('seg')) + [22 if ri else 14])   # a tick's top clears the labels above
        ly = y + top
        out.append('<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f" stroke="#000" stroke-width="3"/>' % (
            X(0) - 2, ly, X(to) + 2, ly))
        if r.get('seg'):
            out.append('<rect x="%.0f" y="%.0f" width="%.0f" height="14" fill="#bbb" stroke="#000" stroke-width="2"/>'
                       % (X(0), ly - 16, X(r['seg']) - X(0)))
        for k in range(d * sub * to + 1):
            v = Fraction(k, d * sub)
            h = 18 if v.denominator == 1 else 13 if k % sub == 0 else 7
            out.append('<line x1="%.1f" y1="%.0f" x2="%.1f" y2="%.0f" stroke="#000" stroke-width="%s"/>' % (
                X(v), ly - h, X(v), ly + h, '3' if v.denominator == 1 else '2'))
        # labels under the ticks
        below = []
        if lab == 'whole' or lab == 'all':
            below += [(Fraction(w), str(w)) for w in range(to + 1)]
        if lab == 'all':
            below += [(Fraction(k, d), '%d/%d' % (k, d)) for k in range(1, d * to) if k % d]
        for v in listed:
            below = [b for b in below if b[0] != Fraction(v)] + [(Fraction(v), v)]
        for v, s in below:   # a whole number among fractions sits level with their bars
            sv, _ = sfrac(X(v), ly + 22 + (ffs * 2.1 - (0 if '/' in s else ffs * 0.75) if fr else fs * 0.8), s,
                          ffs if '/' in s else fs)
            out.append(sv)
        for v in pts + blanks:
            out.append('<circle cx="%.1f" cy="%.0f" r="9" fill="#000"/>' % (X(v), ly))
        for v in pts:
            sv, _ = sfrac(X(v), ly - 22, v, ffs)
            out.append(sv)
        for v in blanks:
            out.append('<rect x="%.0f" y="%.0f" width="%d" height="%d" fill="#fff" stroke="#000" stroke-width="2" '
                       'stroke-dasharray="8 5"/>' % (X(v) - bw / 2, ly - 16 - bh, bw, bh))
        if word(r):
            out.append('<text x="%.0f" y="%.0f" text-anchor="end" font-size="%d">%s</text>' % (
                X(0) - 30, ly + fs * 0.35, fs, html.escape(word(r))))
        gap = (4, 0) if fs != FIG_FS else (18, 10)   # the student page's bigger words: closer lines, so the page fits
        y = ly + 22 + (ffs * 2.1 if fr else fs * 0.8) + gap[1] + (gap[0] if ri < len(rows) - 1 else 0)
    if upto is not None and upto < len(rows):
        out = out[:hidden]
    W, H = X(to) + 46, y + 4
    alt = 'Number lines from 0 to %d, one under the other: ' % to if len(rows) > 1 else 'A number line from 0 to %d: ' % to
    alt += '; '.join('in %s%s%s%s' % (
        PARTS_WORD.get(int(r['d']), '%s parts' % r['d']),
        (', each part cut into %s' % r['sub']) if r.get('sub') else '',
        (', a point at %s' % ' and '.join(v for v in r['pt'].split(',') if v != '?')) if r.get('pt') else '',
        (', a point to name at %s' % ' and '.join(r['blank'].split(','))) if r.get('blank') else '') for r in rows)
    return ('<svg viewBox="0 0 %.0f %.0f" width="%.0f" style="%s" role="img" aria-label="%s" '
            'xmlns="http://www.w3.org/2000/svg" font-family="Georgia, serif">%s</svg>') % (
        W, H, W, fig_style(W, H, size), html.escape(alt), ''.join(out))


FSTRIP = re.compile(r'^(?:(?P<name>[^:]+):)?(?P<k>\d+)/(?P<n>\d+)(?P<blank>=\?)?$')


def fstrip_bars(spec):
    """'fstrip 2/3 Lu:4/6=?' as [(name, k, n, blank)]: each a whole cut into n equal parts, k shaded."""
    bars = []
    for tok in spec.split()[1:]:
        if tok in ('unit', 'lab=none', 'then') or re.match(r'(?:ask|by)=', tok):
            continue
        m = FSTRIP.match(tok)
        if not m or int(m['n']) < 1:
            raise ValueError('fraction strip "%s" is not k/n, Name:k/n or k/n=?' % tok)
        bars.append(((m['name'] or '').replace('_', ' '), int(m['k']), int(m['n']), bool(m['blank'])))
    if not bars:
        raise ValueError('a fraction strip needs at least one k/n')
    return bars


def fstrip_numbers(spec):
    """The fractions a strip figure names (not a blank one, not an unshaded 0/n), for the figure-and-stem gate."""
    return ['%d/%d' % (k, n) for _, k, n, b in fstrip_bars(spec) if not b and k]


FIG_OPTS = {'line': ('to', 'scale', 'ask', 'by', 'names'), 'fstrip': ('unit', 'lab', 'ask', 'by')}


def fig_parts(spec):
    """A line or fstrip figure cell as (options, lines or strips, how many the student page prints). 'then' starts
    the lines or strips drawn on the key and the display only ('line d=5 pt=2/5 / then d=5 sub=2 pt=4/10',
    'fstrip 8/12 then 4/6 2/3'); ask=N prints only the first N on the student page, the ticket and the display's
    question screen. Each line is a list of its tokens; each strip is one token."""
    k = kind(spec)
    opts, rows, then_at = [], [[]], None
    for t in spec.split()[1:]:
        if k == 'line' and t == '/':
            rows.append([])
        elif t == 'then':
            if then_at is None:
                then_at = len(rows) - 1 if k == 'line' else len([r for r in rows if r])
        elif t.split('=', 1)[0] in FIG_OPTS[k] and (k == 'line' or t.split('=', 1)[0] != 'lab' or t == 'lab=none'):
            opts.append(t)
        elif k == 'fstrip':
            if rows[-1]:
                rows.append([])
            rows[-1].append(t)
        else:
            rows[-1].append(t)
    rows = [r for r in rows if r] if k == 'fstrip' else rows
    ask = re.search(r'\bask=(\d+)', spec)
    keep = min(len(rows) if then_at is None else then_at, int(ask[1]) if ask else len(rows))
    return opts, rows, keep


def fig_view(spec, view='key'):
    """A figure cell as one page draws it: 'student' (the student page, the ticket, a check piece) keeps the lines or
    strips before 'then' and within ask=; 'key' keeps them all. Both drop then, ask= and by=, which only say who sees
    what. Any other figure kind is returned as it is."""
    if kind(spec) not in FRACTION_FIGS:
        return spec
    opts, rows, keep = fig_parts(spec)
    rows = rows if view == 'key' else rows[:max(keep, 1)]
    opts = [o for o in opts if not re.match(r'(?:ask|by)=', o)]
    if kind(spec) == 'line':
        return ' '.join(['line'] + opts + [' / '.join(' '.join(r) for r in rows)])
    return ' '.join(['fstrip'] + [r[0] for r in rows] + opts)


def fig_counts(spec, st, example):
    """How many lines or strips of a line or fstrip figure each display screen shows: the question screen, then one
    count a step. by= gives them ('by=-,1,1,2,*': - none, * all); otherwise the question screen shows what the
    student page prints, or only the first line of a worked example whose later lines carry points (the points are
    the answers), and the rest come in one a step from the first step that cuts, draws, folds or circles, all by the
    last step. None when the figure needs none of this (it then grows as before)."""
    if kind(spec) not in FRACTION_FIGS:
        return None
    opts, rows, keep = fig_parts(spec)
    n, T = len(st), len(rows)
    by = re.search(r'\bby=(\S+)', spec)
    if by:
        want = by[1].split(',')
        want += [want[-1]] * (n + 1 - len(want))
        return [T if w == '*' else 0 if w == '-' else min(int(w), T) for w in want[:n + 1]]
    pts = kind(spec) == 'line' and example and any(t.startswith('pt=') for r in rows[1:] for t in r)
    if keep == T and not (pts and not re.search(r'\bask=', spec)):
        return None
    q = 1 if keep == T else keep
    start = next((k for k, s in enumerate(st) if re.search(r'\b(cut|draw|drawn|sketch|fold|circle)\b', s, re.I)), 0)
    out = [q]
    for k in range(n):
        out.append(T if k == n - 1 else q if k < start else min(T, q + k - start + 1))
    return out


def fstrip(spec, size=1.0, upto=None, span=780):
    """Fraction strips from a figure cell, stacked to one length so they compare: 'fstrip 1/2 2/4 4/8'. Each
    k/n is a whole cut into n equal parts with the first k shaded; past n (7/4) a second whole follows, its edge
    drawn heavy. 'Lu:1/6' writes the name at the left instead of the fraction; '2/6=?' leaves an empty box there
    for the student; 'lab=none' writes nothing at the left; 'unit' writes 1/n in each part wide enough to hold it.
    upto=n draws only the first n strips (the display, a step at a time)."""
    bars = fstrip_bars(spec)
    flags = set(spec.split()[1:])
    fs, ffs, bh, gap = FIG_FS, 26, 58, 20
    wholes = max(-(-k // n) for _, k, n, _ in bars) or 1
    L = span / wholes
    nolab = 'lab=none' in flags
    lw = 0 if nolab else max([len(nm) * fs * 0.52 if nm else 64 for nm, _, _, b in bars] + [0])
    x0 = lw + (26 if lw else 0) + 6
    out, y = [], 6
    for bi, (nm, k, n, blank) in enumerate(bars):
        if upto is not None and bi == upto:
            hidden = len(out)
        w = L / n
        cnt = max(-(-k // n), 1) * n
        if n > 24:   # hundredths: thin parts, a heavier line every 10, so the shaded count reads (day 15 read)
            out.append('<rect x="%.1f" y="%.0f" width="%.1f" height="%d" fill="#fff"/>' % (x0, y, cnt * w, bh))
            if k:
                out.append('<rect x="%.1f" y="%.0f" width="%.1f" height="%d" fill="#bbb"/>' % (x0, y, k * w, bh))
            for j in range(1, cnt):
                if j % n:
                    out.append('<line x1="%.1f" y1="%.0f" x2="%.1f" y2="%.0f" stroke="#000" stroke-width="%s"/>' % (
                        x0 + j * w, y, x0 + j * w, y + bh, '4' if j % 10 == 0 else '1'))
            out.append('<rect x="%.1f" y="%.0f" width="%.1f" height="%d" fill="none" stroke="#000" stroke-width="2.5"/>'
                       % (x0, y, cnt * w, bh))
        for j in range(cnt if n <= 24 else 0):
            out.append('<rect x="%.1f" y="%.0f" width="%.1f" height="%d" fill="%s" stroke="#000" stroke-width="2.5"/>' % (
                x0 + j * w, y, w, bh, '#bbb' if j < k else '#fff'))
            if 'unit' in flags and w >= 44:
                sv, _ = sfrac(x0 + (j + .5) * w, y + bh / 2 + 22, '1/%d' % n, 22)
                out.append(sv)
        for j in range(n, cnt + 1, n):   # the edge of each whole, heavy
            out.append('<line x1="%.1f" y1="%.0f" x2="%.1f" y2="%.0f" stroke="#000" stroke-width="6"/>' % (
                x0 + j * w, y - 3, x0 + j * w, y + bh + 3))
        out.append('<line x1="%.1f" y1="%.0f" x2="%.1f" y2="%.0f" stroke="#000" stroke-width="6"/>' % (x0, y - 3, x0, y + bh + 3))
        if not nolab:
            if blank:
                out.append('<rect x="%.0f" y="%.0f" width="64" height="%d" fill="#fff" stroke="#000" stroke-width="2" '
                           'stroke-dasharray="8 5"/>' % (x0 - 26 - 64, y - 6, bh + 12))
            elif nm:
                out.append('<text x="%.0f" y="%.0f" text-anchor="end" font-size="%d">%s</text>' % (
                    x0 - 18, y + bh / 2 + fs * 0.35, fs, html.escape(nm)))
            else:
                sv, _ = sfrac(x0 - 18 - 20, y + bh / 2 + ffs, '%d/%d' % (k, n), ffs)
                out.append(sv)
        y += bh + gap
    if upto is not None and upto < len(bars):
        out = out[:hidden]
    W, H = x0 + L * wholes + 10, y - gap + 8
    alt = ('Fraction strips of one length, one under the other: ' if len(bars) > 1 else 'A fraction strip: ') + '; '.join(
        '%s%d of %d equal parts shaded' % ((nm + ', ') if nm else '', k, n) for nm, k, n, _ in bars)
    return ('<svg viewBox="0 0 %.0f %.0f" width="%.0f" style="%s" role="img" aria-label="%s" '
            'xmlns="http://www.w3.org/2000/svg" font-family="Georgia, serif">%s</svg>') % (
        W, H, W, fig_style(W, H, size), html.escape(alt), ''.join(out))


PLACE = ['ones', 'tens', 'hundreds', 'thousands', 'ten thousands', 'hundred thousands', 'millions']


def cols_rename(a, b):
    """Ungroup first, right to left (s09 expert, day 75): the top number's places after each column is looked at.
    A place that must give and holds 0 first takes ten from its left (day 76: 500 is 4, 9, 10). Index 0 is ones."""
    top, states = a[:], []
    def give(j):   # place j gives one to the place on its right
        if top[j] == 0 and j + 1 < len(top):
            give(j + 1)
            top[j] += 10
        top[j] -= 1
    for j in range(len(top)):
        if top[j] < (b[j] if j < len(b) else 0) and j + 1 < len(top):
            give(j + 1)
            top[j] += 10
        states.append(top[:])
    return states


def cols(spec, size=1.0, state='*'):
    """A sum or difference in place-value columns: 'cols 3746+2538' or 'cols 9372-4156'. Place names over the
    columns, then a row for the small 1s (adding) or the rename (subtracting: the old digit crossed out, the new
    one above it), the two numbers, a line and the answer. Their working for a fix: carry=3 (the places, ones 0,
    that get a small 1), rename=-,-,-,14 (the new top digits left to right, '-' for one left as it was; none for
    no rename) and ans=4136, or ans=5/12/7/14 for a column written whole. state is a step of the display:
    '0' the numbers only, 'r2' the rename of the first two places, 'd3' three answer places, '*' everything."""
    f, _ = fig_fields(spec)
    m = re.match(r'(\d+)\s*([+−-])\s*(\d+)$', spec.split()[1])
    x, op, y = int(m[1]), '+' if m[2] == '+' else '−', int(m[3])
    true = x + y if op == '+' else x - y
    ans = f.get('ans', str(true)).split('/') if '/' in f.get('ans', '') else list(f.get('ans', str(true)))
    n = max(len(m[1]), len(m[3]), len(ans))
    a = [int(c) for c in reversed(m[1])] + [0] * (n - len(m[1]))
    b = [int(c) for c in reversed(m[3])]
    ans = list(reversed(ans))
    full = state == '*'
    r = int(re.search(r'r(\d+)', state)[1]) if re.search(r'r(\d+)', state) else (n if full else 0)
    d = int(re.search(r'd(\d+)', state)[1]) if re.search(r'd(\d+)', state) else (n if full else 0)
    small = {}   # place -> the small text over it
    crossed = set()
    if op == '+':
        if 'carry' in f:
            for j in (int(c) for c in f['carry'].split(',') if c.strip()):
                if j <= d:
                    small[j] = '1'
        else:
            c = 0
            for j in range(n):
                s = a[j] + (b[j] if j < len(b) else 0) + c
                c = s // 10
                if c and j + 1 <= d and j + 1 < n:
                    small[j + 1] = str(c)
    else:
        if 'rename' in f:
            new = [] if f['rename'] == 'none' else list(reversed(f['rename'].split(',')))
            now = {j: v for j, v in enumerate(new) if v != '-'} if r else {}
        else:
            st = cols_rename(a[:len(m[1])], b)
            now = {j: str(v) for j, v in enumerate(st[min(r, len(st)) - 1]) if v != a[j]} if r else {}
        small, crossed = now, set(now)
    cw, x0 = 64 * size, 52 * size
    hy, sy, ty, by, ly = 34 * size, 78 * size, 122 * size, 170 * size, 186 * size
    ay = 232 * size
    W, H = x0 + n * cw + 12 * size, 250 * size
    cx = lambda j: x0 + (n - 1 - j) * cw + cw / 2
    out = []
    for j in range(n):   # place names, two lines where they are two words
        w = PLACE[j].split() if j < len(PLACE) else ['']
        for k, part in enumerate(w):
            out.append('<text x="%.0f" y="%.0f" font-size="%.0f" text-anchor="middle">%s</text>' % (
                cx(j), hy - (len(w) - 1 - k) * 15 * size, 13 * size, part))
        if j:   # a light line between places
            out.append('<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f" stroke="#999" stroke-width="1"/>' % (
                cx(j) + cw / 2, 44 * size, cx(j) + cw / 2, ay + 8 * size))
    num = lambda v, j, y, fs=34: out.append('<text x="%.0f" y="%.0f" font-size="%.0f" text-anchor="middle">%s</text>' % (
        cx(j), y, fs * size, v))
    for j, v in small.items():
        num(v, j, sy, 24)
    for j in range(len(m[1])):
        num(a[j], j, ty)
        if j in crossed:
            out.append('<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f" stroke="#000" stroke-width="2.5"/>' % (
                cx(j) - 12 * size, ty - 4 * size, cx(j) + 12 * size, ty - 22 * size))
    for j in range(len(b)):
        num(b[j], j, by)
    out.append('<text x="%.0f" y="%.0f" font-size="%.0f" text-anchor="middle">%s</text>' % (
        x0 - 26 * size + cw * (n - len(b)), by, 34 * size, op))
    out.append('<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f" stroke="#000" stroke-width="3"/>' % (x0 - 40 * size, ly, W - 8 * size, ly))
    for j in range(min(d, len(ans))):
        num(ans[j], j, ay, 34 if len(ans[j]) == 1 else 26)
    alt = '%s %s %s in columns under the place names%s' % (m[1], op, m[3], ', answer %s' % ''.join(reversed(ans)) if d else '')
    return ('<svg viewBox="0 0 %.0f %.0f" width="%.0f" style="width:100%%;max-width:%.1fin;height:auto" role="img" '
            'aria-label="%s" xmlns="http://www.w3.org/2000/svg" font-family="Georgia, serif">%s</svg>') % (
        W, H, W, min(6.5, 0.8 * n + 0.8), html.escape(alt), ''.join(out))


def cols_state(spec, k):
    """The display's state of a column figure at step k (0-based): its by= list, one entry a step ('-' none)."""
    f, _ = fig_fields(spec)
    by = f.get('by', '').split(',') if f.get('by') else []
    return by[k] if k < len(by) else '*'


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
    cells = [('Day', '%s, section %s, %s day' % (h['day'], h['unit'], KIND_WORD.get(row['kind'], row['kind'].lower()))),
             ('Goal', row['goal']), ('Standard parts', ps or 'see the section opener'),
             ('Tool', '%s (%s), %s min' % (tt, row['mark'], row['tool_min']) if row['tool'] else 'None'),
             ('Materials', h['materials']), ('Print', h['print'])] + (
             [('At home', 'the At home view, %s-home.html, %d minutes with one child'
               % (d['path'].stem, sum(p[0] for p in home_parts(d))))] if 'At home' in d['secs'] else []) + [
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


def home_html(d, row, items, warn, foot):
    """The At home view: the goal and minutes, the block as written (each [[id]] named by where it sits on the
    student page), then the questions it names, pulled from data, with their answers for the parent."""
    h, title = d['head'], d['title']
    byid = {i['item_id']: i for i in items}
    exits = [i['item_id'] for i in items if i['day'] == h['day'] and i['check'] == 'exit'
             and i.get('path', '') in ('', 'paper')]
    labels = page_labels(d)

    def where(r):
        if r in exits:
            return 'ticket question %d' % (exits.index(r) + 1) if len(exits) > 1 else 'the ticket question'
        side, _, name = labels.get(r, r).partition(', ')
        return '%s (%s)' % (name, side) if name else side
    home = d['secs']['At home']
    named = list(dict.fromkeys(r for r in REF.findall(home) if r in byid))
    if row['kind'] == 'Check':   # an assessment day: every end item, whatever the block names (day 24 read)
        ends = sorted((i for i in items if i['day'] == h['day'] and i['check'] == 'end'), key=nkey)
        named = [i['item_id'] for i in ends] + [r for r in named if r not in {i['item_id'] for i in ends}]

    def answer(i):   # a worked example's steps, and a judged item's look-fors and samples, for the parent
        a = html.escape(i['answer'])
        if i['check'] == 'example' and steps(i):
            a += '<ol>%s</ol>' % ''.join('<li>%s</li>' % html.escape(x) for x in steps(i))
        if i['judged'] == 'teacher' and steps(i) and i['check'] != 'example':
            a += '<br><b>Look-fors:</b><ol>%s</ol>' % ''.join('<li>%s</li>' % html.escape(x) for x in steps(i))
        if i['judged'] == 'teacher' and i.get('samples'):
            a += '<b>Samples (ours, untested):</b><ul>%s</ul>' % ''.join(
                '<li>%s</li>' % html.escape(x.strip()) for x in i['samples'].split('|') if x.strip())
        return a
    tot = sum(p[0] for p in home_parts(d))
    kind = 'an assessment day' if row['kind'] == 'Check' else 'a teaching day'
    meta = [('Goal', row['goal']), ('Time', '%d minutes, one parent and one child (%s)' % (tot, kind)),
            ('Print', 'the student page' + (', the recording page' if re.search(r'recording page', home, re.I) else '')
             + (' and one exit ticket' if exits and row['kind'] != 'Check' else '')
             + '; this page and its answers are for you')]
    last = {'group': None, 'end': 0}

    def name(m):   # "Fix it 1 (side 1), then 2": a run of questions from one place names the place once
        r = m[1]
        if r not in byid:
            return m[0]
        w = where(r)
        g = re.match(r'(.*?)(?:,? (?:row |question )?\d+)?(?: \((side \d)\))?$', w)
        group = (g[1], g[2])
        gap = home[last['end']:m.start()]
        same = last['group'] and g[1] == last['group'][0] and len(gap) <= 8   # ", ", " and ", ", then ", " to "
        if same:   # the same place: the number alone, and its side only when the run turns the page
            w = w[len(g[1]):].lstrip(', ')
            if group == last['group']:
                w = w.split(' (side')[0]
        elif re.search(r'(?:^|\.\**)\s*$', home[:m.start()]):   # a sentence starts with it
            w = w[0].upper() + w[1:]
        last.update(group=group, end=m.end())
        return '**%s**' % w.strip()
    body = md(REF.sub(name, home), items)
    qs = ''.join('<tr><td>%s</td><td class="q">%s</td><td>%s</td></tr>' % (
        html.escape(where(r)), stacked(stem(byid[r])), answer(byid[r])) for r in named)
    return ('<h1>%s</h1><p>At home</p>%s<table class="meta">%s</table>%s'
            '<h2>The questions</h2><p>The child works on the printed page; the answers are for you.</p>'
            '<table><tr><th>Where</th><th>Question</th><th>Answer</th></tr>%s</table>%s' % (
                html.escape(title), warn, ''.join('<tr><td>%s</td><td>%s</td></tr>' % (html.escape(a), html.escape(b))
                                                  for a, b in meta), body, qs, foot))


def build_day(d, course, items, days, parts_all, errors, wrongs, pdf):
    h = d['head']
    row = next(x for x in days if x['day'] == h['day'])
    tt = tool_title(row['tool']) if row['tool'] else ''
    mine = [i for i in items if i['day'] == h['day'] and i['check'] in plan.LESSON_KINDS | {'exit'}]
    # an assessment day is measured by its end rows, which carry the unit, not the day
    # (a unit with two assessment days keeps each day's end rows apart: select by the day being built)
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
    # the key's order (unit 3 reads, days 10 and 20): an assessment's end rows, then the warm-up, then the rows in
    # the order the student page prints them, then the rest (the exit) in the old order
    warm = [r for _, bn, wh in d['blocks'] if bn.lower().startswith('warm') for r in REF.findall(wh)]
    shown_at = re.findall(r'\[\[(?:fig:|note:)?([A-Za-z0-9-]+)\]\]', d['student'])
    endid = {i['item_id'] for i in end}
    refs = [i['item_id'] for i in end] + [r for r in dict.fromkeys(warm + shown_at + refs)
                                          if r in refs and r not in endid]
    warm = set(warm) - endid
    credits =sorted({byid[r]['source'] for r in refs if byid[r].get('source')})
    foot = foot_line(h, course, ([h['credit']] if h['credit'].lower() != 'ours' else []) + credits)
    gone = missing(d)
    warn = ('<p class="warn">Not ready to teach: %s missing.</p>' % html.escape(', '.join(gone))) if gone else ''
    side = branch_only(d, mine) if not end else set()
    tb = '<h1>%s</h1><p>Teacher page</p>%s%s%s%s' % (html.escape(title), warn, header_table(d, row, parts, tt, side),
                                                     md(teacher_prose(d), items, teacher=True), foot)
    put(out / (name + '-teacher.html'), page(title + ': teacher page', tb, 'teacher'), encoding='utf-8')
    sb = student_html(d, course, items)
    put(out / (name + '-student.html'), page(title + ': student page', sb, 'student'), encoding='utf-8')
    put(out / (name + '-student-large.html'), page(title + ': student page, large print', sb, 'student large'),
                                                     encoding='utf-8')
    # key: in the order the pages use them, both exit paths
    errname = {e['letter']: err_name(e['error']) for e in errors if e['stretch'] == row['stretch']}
    errname['x'] = ERR_X
    kr = []
    for r in refs:
        i = byid[r]
        ws, seen = [], set()
        for w in (w for w in wrongs if w['item_id'] == r):
            e = w['error']
            nm = errname.get(e, '').lower() if e and e not in seen else ''
            what = ('error %s' % e) + (', ' + nm if nm else '') if e else ''
            seen.add(e)
            # a note the register's name beside it already says is dropped; with no letter the note is the meaning,
            # printed after a colon, not in brackets after one (unit 2 reads, day 9 finding 10)
            nt = '' if nm and w['note'].strip().lower() in nm else w['note']
            tail = (what + (' (%s)' % nt if nt and what else nt)).strip()
            ws.append(w['shown'] + (': ' + tail if tail else ''))
        where = ('warm-up' if r in warm else i['check']) + (' %s' % i['n'] if i['check'] == 'end' else '') + (
            ' (%s)' % i['path'] if i.get('path') else '')
        ans = html.escape(i['answer'])
        if i['judged'] == 'teacher' and steps(i):
            ans += '<br><b>Look-fors, each ticked alone:</b><ol>%s</ol>' % ''.join(
                '<li>%s</li>' % html.escape(x) for x in steps(i))
        if i['judged'] == 'teacher' and i.get('samples'):
            ans += '<b>Samples (ours, untested):</b><ul>%s</ul>' % ''.join(
                '<li>%s</li>' % html.escape(x.strip()) for x in i['samples'].split('|') if x.strip())
        # a strip figure prints under its row, the table's full width, all of it ('then' lines too), at the size
        # it was drawn for (day 11 read: in the question cell it shrank to a thumbnail); a fix: their picture, then
        # the right one
        pics = ''.join('<div style="margin:.2em 0">%s%s</div>' % (
            ('<i>%s</i>' % ('Their picture' if k == 0 else 'The right picture')) if len(figures(i)) == 2 else '',
            figure(fig_view(x, 'key'), 0.6)) for k, x in enumerate(figures(i))
            if x and kind(x) in ('strip', 'tiles') + FRACTION_FIGS)
        kr.append('<tr><td>%s</td><td>%s</td><td>%s</td><td class="q">%s</td><td>%s</td><td>%s</td></tr>%s' % (
            html.escape(where), html.escape(i['item_id']), html.escape(part_of(i)), html.escape(stem(i)), ans,
            html.escape('; '.join(ws)), ('<tr><td colspan="6">%s</td></tr>' % pics) if pics else ''))
    kb = ('<h1>%s: key</h1><p>Each answer is worked out in full. The last column names the wrong answers to expect and the error each one shows.</p>'
          '<p>%s</p>'
          '<table><tr><th>Where</th><th>Id</th><th>Part</th><th>Question</th><th>Answer</th><th>Wrong answers and what '
          'they mean</th></tr>%s</table>%s' % (html.escape(title), html.escape(key_rule([byid[r] for r in refs], warm)),
                                               ''.join(kr), foot))
    put(out / (name + '-key.html'), page(title + ': key', kb, 'key'), encoding='utf-8')
    if 'At home' in d['secs']:
        put(out / (name + '-home.html'), page(title + ': at home', home_html(d, row, items, warn, foot), 'teacher'),
            encoding='utf-8')
    # exit ticket, four to a sheet: the paper path only
    ex = [i for i in mine if i['check'] == 'exit' and i.get('path', '') in ('', 'paper')]
    if ex and row['kind'] != 'Check':
        one = '<div class="slip"><p>Name ______________ Day %s</p>%s%s</div>' % (h['day'], ''.join(
            slip_item(k, i) for k, i in enumerate(ex)), foot)
        put(out / (name + '-exit.html'), page(title + ': exit tickets', one * 4, 'student'), encoding='utf-8')
    # display, in the order the teacher page runs: part by part, each [[id]], [[steps:id]] and **Ask.** where it
    # first appears (a worked example with its figure, then its steps one screen at a time; a fix with the wrong
    # working beside the right; a challenge); a plain sum's answers; a part's "check your answers" screen only when
    # that part names a partner or self check (its own "Check: ..." line, if any, is the sentence); the frames last
    scr, done, asked = [], set(), set()
    fig = lambda i: figure(figures(i)[0]) if len(figures(i)) == 1 else ''
    # "**Ask.**", and "**Ask** (after step 4)." too: the build dropped the second form's screen (unit 2 reads,
    # days 7 and 8); the check fails it, so the page keeps one form
    tok = re.compile(r'\[\[(steps:)?([A-Za-z0-9-]+)\]\]|\*\*Ask\.?\*\*\.? ?(.+?)(?=\n\s*\n|\Z)', re.S)
    peer = re.compile(r'swap and check|swap and compare|partner check|check their own|partners check', re.I)
    on_page = set(REF.findall(d['student']))
    last_ex = []
    draws = re.compile(r'\b(draw|drawn|build|snap|sketch|lay|put out)\b', re.I)

    pend, held = [], {}   # a fix's right working, waiting for its Ask; Ask screens waiting for a step (after step N)
    just = {}   # the worked example walked last, while nothing follows it: an "after step N" Ask written under it
    # goes after its own step N, not the next example's (unit 2 reads, days 7 and 8; day 19 had it on example 2)

    def flush():
        scr.extend(h for _, h in pend)
        pend.clear()

    def staged_fig(i, c):
        """A line or fstrip figure showing its first c lines or strips, in the whole picture's frame."""
        spec = fig_view(figures(i)[0], 'key')
        if not c:
            return ''
        T = len(fig_parts(spec)[1])
        return (numline if kind(spec) == 'line' else fstrip)(spec, 1.0, c if c < T else None)

    def step_fig(i, k, first, n):
        """The example's figure at step k: none before the step that first draws or builds it; a strip grows a bar
        a step from there, in the full picture's frame, whole by the last step; smaller once the list is long. A line
        or fstrip figure with then, ask= or by= (or a worked example's line whose later lines carry points) shows
        what fig_counts says."""
        spec = figures(i)[0] if len(figures(i)) == 1 else ''
        if spec.startswith('cols'):   # columns fill in step by step, as the by= list says (s09 expert, days 72 to 76)
            s = cols_state(spec, k)
            return '' if s == '-' else cols(spec, 1.0, s)
        cnt = fig_counts(spec, steps(i), True) if spec else None
        if cnt is not None:
            svg = staged_fig(i, cnt[k + 1])
            return svg if k < 2 or not svg else '<div style="max-width:60%%">%s</div>' % svg
        if not spec or k < first:
            return ''
        upto = None
        grow = {'strip': (strip, lambda s: len(strip_bars(s))), 'line': (numline, lambda s: len(line_rows(s)[1])),
                'fstrip': (fstrip, lambda s: len(fstrip_bars(s)))}.get(kind(spec))
        if grow and k < n - 1:   # a picture of several bars or lines grows one a step, whole by the last step
            nb = grow[1](spec)
            upto = min(nb, k - first + 1) if k - first + 1 < nb else None
        svg = grow[0](spec, 1.0, upto) if grow else figure(spec)
        return svg if k < 2 else '<div style="max-width:60%%">%s</div>' % svg

    def screens(i):
        if i['check'] == 'example':
            st = steps(i)
            first = next((k for k, s in enumerate(st) if draws.search(s)), 0)
            at = re.search(r'\bat=(\d+)', figures(i)[0]) if len(figures(i)) == 1 else None
            if at:   # 'rows 12/5 at=4': the picture is the answer, held back until the step that shows it
                first = int(at[1]) - 1
            col = len(figures(i)) == 1 and figures(i)[0].startswith('cols')
            cnt = fig_counts(figures(i)[0], st, True) if len(figures(i)) == 1 else None
            qf = staged_fig(i, cnt[0]) if cnt is not None else (
                fig(i) if first == 0 and not col and not draws.search(st[0] if st else '') else '')
            o = ['<div class="screen"><p>%s</p>%s</div>' % (stacked(stem(i)), qf)]
            for k in range(len(st)):
                # a step that lays this example beside an earlier one shows that one's picture too
                other = (''.join(figure(figures(e)[0]) for e in last_ex[-1:] if len(figures(e)) == 1)
                         if re.search(r'\bbeside the\b', st[k], re.I) else '')
                o.append('<div class="screen">%s%s<ol>%s</ol></div>' % (other, step_fig(i, k, first, len(st)), ''.join(
                    '<li%s>%s</li>' % (' class="now"' if j == k else '', html.escape(s)) for j, s in enumerate(st[:k + 1]))))
                # an Ask written "after step N" before this example's steps gets its screen there (day 19 read)
                o.extend(held.pop(k + 1, []))
            for k in sorted(held):   # a step number past the last: after the last step
                o.extend(held.pop(k))
            last_ex.append(i)
            return o
        if i['check'] == 'fix':   # one figure is the problem's, above both; two are their picture and the right one
            # two screens (unit 3 reads, days 12, 16, 17, 18): the problem with their working, while the class
            # talks; then both side by side, the right working in full, after the part's Ask
            st, fs = steps(i) + ['', ''], figures(i)
            two = [figure(x) if x else '' for x in fs] if len(fs) == 2 else ['', '']
            theirs = '<div><b>Their working</b>%s<p>%s</p></div>' % (
                two[0], html.escape(cap1(re.sub(r'^.*?working: ', '', st[0]))))
            right = ''.join('<p>%s</p>' % html.escape(cap1(re.sub(r'^.*?working: ', '', x))) for x in st[1:] if x)
            pend.append((i['item_id'], '<div class="screen"><p>%s</p>%s<div class="pair">%s<div><b>The right working'
                         '</b>%s%s</div></div></div>' % (stacked(stem(i)), fig(i), theirs, two[1], right)))
            return ['<div class="screen"><p>%s</p>%s<div class="pair">%s</div></div>' % (stacked(stem(i)), fig(i),
                                                                                          theirs)]
        if i['check'] == 'challenge':
            return ['<div class="screen"><p><b>Challenge.</b> %s</p></div>' % stacked(stem(i))]
        return []

    def answers_screen():
        # labelled by the numbers on the student page, not the part names (s09 expert, day 77); the equal-forms
        # sentence only on a day with equations; a judged sum or difference shows its number, so a student who
        # let a wrong one stand can see it
        num = lambda i: (re.search(r'(?m)^\s*\**(\d+)\.\**\s.*?\[\[%s\]\]' % re.escape(i['item_id']), d['student'])
                         or [None, i['n']])[1]
        eq = accept(end) == ACCEPT
        letter = any(LETTER.search(i['answer']) for i in end if i['judged'] == 'key')

        def say(i):
            if i['judged'] == 'key':
                return i['answer']
            last = i['answer'].split(';')[-1].strip()
            if re.fullmatch(r'[\d,]+', last) and re.search(r'[+−]', stem(i)):
                kind = 'difference' if '−' in stem(i) else 'sum'
                how = 'adding' if re.search(r'(?<!without )\badding\b', stem(i), re.I) else 'reason'
                return 'The %s is %s. Your %s is read by your teacher.' % (kind, last, how)
            return 'Read by your teacher.'
        judged = [num(i) for i in end if i['judged'] == 'teacher']
        # fractions and signs: a right answer in another form is still right (day 24 read, as day 88 had by hand)
        frac = any(re.search(r'\d/\d', i['answer']) for i in end)
        sign = any(re.search(r'[<>]', i['answer']) for i in end)
        return ('<div class="screen"><p><b>Answers.</b> %s%s%s%sMark your own in pen.%s</p><ol>%s</ol></div>' % (
                    'Any letter is right. ' if letter else '',
                    'An equation is right in any order if it says the same thing. ' if eq else '',
                    'Any equal name is right. ' if frac else '',
                    'A sign is right if it reads true as a sentence. ' if sign else '',
                    (' Items %s are judged by your teacher.' % ' and '.join(judged)) if judged else '',
                    ''.join('<li style="list-style:none"><b>%s.</b> %s%s</li>' % (
                        html.escape(num(i)), html.escape(say(i)), ''.join(
                            '<div style="max-width:5in">%s</div>' % tiles(x, 0.6) for x in figures(i)
                            if kind(x) == 'tiles')) for i in end)))

    def walk(text, prac):
        for m in tok.finditer(text):
            if m[3]:
                # every quoted question in the Ask paragraph is a screen (a "Then:" question too); answers
                # ("Expect: ...") are quoted without a question mark and stay off the screen
                qs = [q for q in re.findall(r'"([^"]+)"', m[3]) if q.rstrip().endswith('?')] or \
                    re.findall(r'"([^"]+)"', m[3])[:1]
                after = re.search(r'\bafter step (\d+)\b', m[3], re.I)
                out = []
                for q in qs:
                    q = re.sub(r'[*]', '', q).strip()
                    if q not in asked:   # one screen per planned question, however often the page names it
                        asked.add(q)
                        out.append('<div class="screen">%s</div>' % html.escape(q))
                n = int(after[1]) if after else 0
                if after and just and just['end'] == len(scr) and n <= len(steps(just['row'])):
                    at = just['start'] + 1 + n
                    scr[at:at] = out
                    just['end'] = len(scr)
                elif after:   # "after step 2": its screen waits for the next worked example's step 2 (day 19 read)
                    held.setdefault(n, []).extend(out)
                else:
                    scr.extend(out)
                    flush()   # a fix's right working comes after the class has answered (unit 3 reads)
                for r in REF.findall(m[3]):   # a row named inside the Ask paragraph is still walked
                    if r not in done and r in byid:
                        done.add(r)
                        flush()
                        scr.extend(screens(byid[r]))
                        if byid[r]['check'] in ('practice', 'tool'):
                            prac.append(byid[r])
                continue
            if m[1] and any(p[0] == m[2] for p in pend):   # [[steps:id]] for a fix shown above: its right working
                # waits for an Ask later in the same part, so the class answers before the screen does (unit 2
                # reads, day 7: Lena's reason showed before Lena's question)
                if not re.search(r'\*\*Ask\.?\*\*', text[m.end():]):
                    flush()
            if m[2] in done or m[2] not in byid:
                continue
            done.add(m[2])
            i = byid[m[2]]
            flush()
            start = len(scr)
            scr.extend(screens(i))
            just.clear()
            if i['check'] == 'example':
                just.update(row=i, start=start, end=len(scr))
            if i['check'] in ('practice', 'tool'):
                prac.append(i)
        flush()

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
            if len(gs) == 1:
                scr.append('<div class="screen"><p><b>Group.</b> %s</p></div>' % html.escape(gs[0]))
            if len(gs) > 1:   # groups work at once: one screen holds every task (expert, days 6 and 77)
                # students read it to find their group: the name and what they match, then the first task sentence
                # only; the teacher's notes stay on the teacher page (unit 2 reads, day 9 finding 7)
                def seen_by(b):
                    j, dep = -1, 0
                    for k, c in enumerate(b):   # the first bracket, matched: "(7, 8, or ... (error G))"
                        if c == '(':
                            dep += 1
                        elif c == ')' and dep:
                            dep -= 1
                            if not dep:
                                j = k
                                break
                    head, rest = (b[:j + 1], b[j + 1:].lstrip(' :.')) if j >= 0 else ('', b)
                    first = re.split(r'(?<=[.!?])\s+', rest)[0]
                    return (head + ': ' if head else '') + first
                scr.append('<div class="screen" style="font-size:16pt"><p><b>Find your group.</b></p><ul>%s</ul></div>'
                           % ''.join('<li>%s</li>' % html.escape(seen_by(b)) for b in gs))
        for btxt in chunks(whole):
          prac = []
          walk(btxt, prac)
          # tool rows (the paper path of a tool part) get a question screen, then their check screens, so the
          # answers never show before students predict (expert, day 4): a long row (a story, a whole table) its own
          # pair of screens; short rows with short answers (a table's lines, day 83) share one of each
          tools, prac = [i for i in prac if i['check'] == 'tool'], [i for i in prac if i['check'] != 'tool']
          ct = re.search(r'^Check(?: \(sort\))?: (.+)$', btxt, re.M)
          say_t = html.escape(ct[1].strip() if ct else 'Does yours match? Fix it in pen.')
          # a row that asks for a feature is checked on the feature's terms, not against one written answer
          # (unit 2 reads, day 7 finding 8: right noticing crossed out)
          feat = lambda rs: any(FEAT.search(stem(i)) for i in rs)
          if feat(tools) and not re.search(r'feature', say_t, re.I):
              say_t += ' ' + html.escape(FEAT_SAY)
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
              if any(i not in short for i in plain):   # its questions before its answers (day 15 read)
                  scr.append('<div class="screen"><ol>%s</ol></div>' % ''.join(
                      '<li>%s</li>' % stacked(stem(i)) for i in plain if i not in short))
              scr.append('<div class="screen"><p><b>Check your answers.</b></p><ol>%s</ol></div>' % ''.join(
                  '<li>%s = %s</li>' % (html.escape(stem(i).rstrip('? =').strip()), html.escape(i['answer'])) for i in plain))
          rest = [i for i in prac if i not in plain]
          cm = re.search(r'^Check(?: \((sort)\))?: (.+)$', btxt, re.M)
          if rest and (cm or peer.search(whole)):
              # the equation line only where there is an equation; a yes or no about multiples reads its
              # multiplication (unit 2 reads, day 8 finding 7)
              say = cm[2].strip() if cm else (
                  'Does your multiplication show it? If not, put a question mark.' if all(
                      re.search(r'multiple|factor', stem(i), re.I) for i in rest) else
                  'Put each answer back in its equation. Does it give the number in the question? If not, put a '
                  'question mark.' if any('=' in stem(i) + i['answer'] for i in rest) else
                  'Does your working show it? If not, put a question mark.')
              if feat(rest) and 'feature' not in say.lower():
                  say += ' ' + FEAT_SAY
              # a warm-up's questions get their own screen first, so the display put up before class does not
              # open on the answers (unit 2 reads, day 8 finding 7)
              if bname.lower().startswith('warm-up') and not any(i in short or i in plain for i in rest):
                  scr.append('<div class="screen"><ol>%s</ol></div>' % ''.join(
                      '<li>%s</li>' % stacked(stem(i)) for i in rest))
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
    walk('\n'.join(v for k, v in d['secs'].items() if k not in ('The day', 'At home')), [])
    for k in sorted(held):   # an "after step N" Ask with no worked example after it keeps its screen
        scr.extend(held.pop(k))
    if end and not shown:
        scr.append(answers_screen())
    scr += ['<div class="screen">%s</div>' % html.escape(q) for q in
            re.findall(r'"([^"]*__[^"]*)"', d['secs'].get('Words and supports', ''))]
    if end:   # an assessment day's challenges are for whoever finishes, all at once: one screen (s09 expert, day 77)
        ch = '<div class="screen"><p><b>Challenge.</b> '
        merged = []
        for x in scr:
            if merged and x.startswith(ch) and merged[-1].startswith(ch):
                merged[-1] = merged[-1][:-len('</div>')] + x[len('<div class="screen">'):]
            else:
                merged.append(x)
        scr = merged
    put(out / (name + '-display.html'), page(title + ': display', ''.join(scr) + foot, 'display'),
                                                encoding='utf-8')
    note = ''
    if pdf:
        note = print_sides(out / (name + '-student.html'))
    return out, note


ACCEPT = ('Any equal form of an equation is right: the two factors in either order, either side of the equals sign, '
          'any letter, or the matching division (n × 9 = 36, 9 × n = 36, 36 = 9 × n and 36 ÷ 9 = n all say the same).')
ORDER = ['example', 'tool', 'fix', 'practice', 'challenge', 'exit']


def accept(rows):
    """The key's opening rule: the equal-forms note only on a day with an equation (a letter for an unknown, or a
    division); a day of sums and differences with estimates gets the estimate rule instead (s09 expert, days 72 to
    77: the factors note printed on adding days)."""
    # a fraction rule "(16 ÷ 2)/(10 ÷ 2)" is not a factor equation (day 16 read: the factors note on every unit 3 key)
    rule = lambda s: re.sub(r'\([^()]*[×÷][^()]*\)/\([^()]*[×÷][^()]*\)', 'F', s)
    if any(LETTER.search(stem(i)) or LETTER.search(i['answer']) or '÷' in rule(stem(i) + i['answer'])
           or re.search(r'×.*=', rule(i['answer'])) for i in rows):
        return ACCEPT
    if any(re.search(r'\d+/\d+\s*[=<>]', i['answer']) for i in rows):   # naming and comparing fractions (unit 3)
        return 'Any right grouping or cut is right, and a name with smaller numbers need not be the smallest.'
    if any(re.search(r'\b(?:estimate|about)\b', i['answer'], re.I) for i in rows):
        return 'Any close estimate is right: it only has to catch a big mistake.'
    return ''
FEATURE_RULE = ('A feature is right if it is true of every number and is not the rule. A reason says what one jump '
                'does to the feature; more numbers are not a reason.')


def key_rule(rows, warm=()):
    """The key's opening line. On a number-pattern day (4.OA.C.5 taught) how to mark a feature and a reason, with
    the equal-forms or other rule only if a taught row of another standard calls for it: the warm-up and the
    patterns' own sums do not (unit 2 reads, day 7: the equation note printed from the warm-up's 4 × 18 = 72).
    Any other day keeps accept() on all its rows."""
    if not any(i['code'] == '4.OA.C.5' and i['check'] != 'end' for i in rows):
        return accept(rows)
    rest = [i for i in rows if i['item_id'] not in warm and i['code'] != '4.OA.C.5']
    return ' '.join(x for x in (FEATURE_RULE, accept(rest)) if x)


LETTER = re.compile(r'(?<![A-Za-z])[a-z](?![A-Za-z])\s*[=×÷+−-]|[=×÷+−-]\s*[a-z](?![A-Za-z])')   # n × 9, = n


# error x: any other wrong answer, a slip or miscount that sends a student to no group (unit 2 reads)
ERR_X = 'Any other wrong answer: no group'


def err_name(text):
    """A register error as the key names it: without its worked example (': 2/3 = 2/6', or one in brackets), which
    printed beside wrong answers it did not match (unit 3 reads, days 14 and 20); the row's own note says the rest."""
    ex = lambda s: re.search(r'\d\s*/\s*\d|=', s)
    text = re.sub(r'\s*\(([^()]*)\)', lambda m: '' if ex(m[1]) else m[0], text)
    head, sep, tail = text.partition(': ')
    return head if sep and ex(tail) else text


def cap1(s):
    """The first letter up: a fix's working with its "Right working:" label stripped starts a sentence."""
    return s[:1].upper() + s[1:]
FEAT = re.compile(r'\b(?:did not say|did not tell|notice)\b', re.I)
FEAT_SAY = 'Your feature may be different. Is it true of every number? Is it the rule? Fix only those.'
DRAWS = re.compile(r'\b(draw|sketch|strip picture|strips)\b', re.I)


def slip_item(k, i):
    """One exit question on the exit ticket. A stem that asks for a drawing gets a box before its lines; a teacher-judged
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
    # a column sum or difference: a work box for the columns, then a labelled line for each part asked (s09 expert,
    # days 72 to 76: two bare lines held neither the working nor which answer was which)
    big = r'(\d{1,3}(?:,\d{3})+|\d{3,})'
    sm = re.search(big + r'\s*([+−-])\s*' + big, stem(i))
    if sm and not frames and not each and re.search(r'\b(add|subtract|find)\b', stem(i), re.I):
        sub = sm[2] != '+'
        a, b = (int(x.replace(',', '')) for x in (sm[1], sm[3]))
        ad = [int(c) for c in reversed(str(a))]
        st = cols_rename(ad, [int(c) for c in reversed(str(b))]) if sub else []
        zero = sub and any(ad[j] == 0 and st[-1][j] != 0 for j in range(len(ad)))
        q = stem(i)
        labels = (['Estimate'] if re.search(r'\bestimate\b', q, re.I) else []) + (['Rename'] if zero else []) + \
            ['Difference' if sub else 'Sum'] + (['Which place'] if re.search(r'\bwhich place\b', q, re.I) else []) + \
            (['Became'] if re.search(r'\bbecome\b', q, re.I) else []) + \
            (['Worth'] if re.search(r'\bworth\b', q, re.I) else []) + \
            (['Check'] if re.search(r'\bto check\b|\bcheck(?:s)? it\b|\bcheck your\b', q, re.I) else [])
        box = '<div class="sketch tall"></div>'
        lines = ''.join('<p>%s: <span class="blank" style="width:%sem"></span></p>' % (
            l, '13' if l in ('Rename', 'Became', 'Check') else '9') for l in labels)
    # a number line or fraction strip the question names prints on the ticket, to mark on (unit 3: "on the line
    # marked in twelfths" printed with no line)
    pic = ''.join('<div class="fig" style="margin:.15em 0">%s</div>' % (
        numline(fig_view(x, 'student'), 0.6, span=520) if kind(x) == 'line' else fstrip(fig_view(x, 'student'), 0.6,
                                                                                        span=480))
                  for x in figures(i) if kind(x) in FRACTION_FIGS)
    if search or each or sm:   # the kinds above keep their own layout
        return '<p>%d. %s</p>%s%s%s' % (k + 1, stacked(' '.join(ask)), pic, box, lines)
    # any other question keeps its sentences in order, each with its room where it is asked (unit 3 reads)
    rule = '<p>__________________________</p>'
    out, ps = [], slip_pieces(stem(i))
    for kd, x in ps:   # the picture after the first run of sentences, a drawing box after the last
        out.append('<p>%s</p>' % stacked(x) if kd == 'p' else '<p>%s</p>' % blank(x) if kd == 'f' else rule * x)
    out[0] = out[0].replace('<p>', '<p>%d. ' % (k + 1), 1)
    at = [n for n, (kd, _) in enumerate(ps) if kd == 'p'] or [0]
    out[at[0]] += pic
    # a drawing box goes under the sentence that asks for the drawing (unit 2 reads, day 8: "Draw steps 2 and 3"
    # had its box at the foot of the slip, after the lines for the reason)
    dr = [n for n, (kd, x) in enumerate(ps) if kd == 'p' and DRAWS.search(x)]
    out[(dr or at)[0] if dr else at[-1]] += box
    return ''.join(out)


WHY = re.compile(r'\b(?:why|how do you know|how you know|explain)\b', re.I)
WRITE = re.compile(r'^(?:\([a-h]\)\s*)?(?:then |so |and )?(?:write|name|find|rename)\b', re.I)


def slip_pieces(q):
    """An exit question as pieces in its own order: ('p', text) a run of sentences, ('f', sentence) a sentence with
    blanks printed as its fill line, ('l', n) n write lines. A why or how-do-you-know sentence gets two lines, a
    question or a "Write ..." with no frame after it one; a part, (a) or (b), with no room of its own gets a line
    (and one more when the words before the parts ask to show or rename); a question with no room at all gets two."""
    chunks = re.split(r'\s+(?=\([a-h]\)\s)', q.strip())
    pre = chunks[0] if len(chunks) > 1 and not re.match(r'\([a-h]\)\s', chunks[0]) else None
    work = bool(pre and re.search(r'\b(?:show|rename|explain)\b', pre, re.I))
    out = []
    for c in chunks:
        sents = [x for x in re.split(r'(?<=[.?!])\s+', c) if x.strip()]
        room, para = False, []
        for j, s in enumerate(sents):
            nxt = sents[j + 1] if j + 1 < len(sents) else ''
            if '__' in s:
                if para:
                    out.append(('p', ' '.join(para))); para = []
                out.append(('f', s)); room = True
                continue
            para.append(s)
            if c is pre:
                continue
            n = 2 if WHY.search(s) else 1 if (s.rstrip().endswith('?') and '__' not in nxt and not WHY.search(nxt)) \
                or (WRITE.search(s) and '__' not in nxt) else 0
            if n:
                out.append(('p', ' '.join(para))); para = []
                out.append(('l', n)); room = True
        if para:
            out.append(('p', ' '.join(para)))
        if re.match(r'\([a-h]\)\s', c) and (not room or work):
            out.append(('l', 1))
    if not any(kd in 'lf' for kd, _ in out):
        out.append(('l', 2))
    elif not any(kd == 'f' for kd, _ in out) and sum(x for kd, x in out if kd == 'l') < 2:
        n = max(n for n, (kd, _) in enumerate(out) if kd == 'l')
        out[n] = ('l', out[n][1] + 1)
    return out


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


# ------------------------------------------------------------------ once-per-section pieces
# A piece is any other .md in a section folder (opener.md, record.md, readiness.md, ...), with a header naming its
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
    the day's other rows of the same kind stay out), or else every row of its check kind for its unit."""
    h = p['head']
    named = REF.findall(section(p['body'], 'Items') or '')
    if named:
        byid = {i['item_id']: i for i in items}
        return [byid[r] for r in named if r in byid]
    return sorted([i for i in items if i['check'] == h.get('check') and i['stretch'] == h.get('stretch')],
                  key=nkey)


def unit_foot(h, course, what):
    return '<div class="foot">%s</div>' % html.escape(
        'Curio Class, %s, section %s, %s, version %s, CC BY 4.0, curioclass.org'
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
        f.append('%s: the section opener is %d words; the cap is %d' % (lab, words(p['body']), CAP_OPENER))
    if kind == 'check':
        rs = piece_rows(p, items)
        if not rs:
            f.append('%s: no %s rows for unit %s in items.csv' % (lab, h.get('check'), h.get('stretch')))
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
    # a blank, "__", is a line to write on, never markdown's bold: "It must keep going because __." read as
    # "__ ... __" in bold across a sentence (unit 3 openers), as md() already does for a day page
    mdh = lambda t: markdown.markdown(t, extensions=['tables'])
    blanks = lambda t: re.sub(r'_{2,}', lambda m: '<span class="blank" style="width:%.1fem"></span>'
                              % (len(m[0]) * 0.45 if len(m[0]) > 2 else 2.5), t)
    if kind in ('opener', 'family'):   # prose for the teacher or family: a blank is never bold (sheets keep theirs)
        put(out / (name + '.html'), page(title, '<h1>%s</h1>%s%s' % (
            html.escape(title), mdh(blanks(body)), unit_foot(h, course, name)), 'teacher'), encoding='utf-8')
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
        # a teacher-judged exit on a day the header names ("exitlooks: 7") takes one tick a look-for, like a written
        # task (unit 2 reads, day 7 finding 2); other sheets keep one tick for the ticket
        xl = {x.strip() for x in h.get('exitlooks', '').split(';') if x.strip()}
        xj = lambda d: [i for i in items if i['stretch'] == st and i['check'] == 'exit' and i['day'] == d
                        and i['judged'] == 'teacher' and steps(i) and d in xl]
        mid = [((int(d), 0), ('E%s (%s)' % (d, ', '.join(ex(d))) if ex(d) else 'E%s' % d,
                              max([len(steps(i)) for i in xj(d)] or [1])))
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
        lf = ''.join('<p><b>E%s look-fors:</b> %s</p>' % (i['day'], '; '.join('%d. %s' % (k + 1, html.escape(s))
                     for k, s in enumerate(steps(i)))) for d in sorted({i['day'] for i in items if i['stretch'] == st
                                                                      and i['check'] == 'exit'}, key=int)
                     for i in xj(d)) + lf
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
        return (m[1], fs) if len(fs) >= 6 and all(re.fullmatch(r'\d+ [×÷+−] \d+', x) for x in fs) else None

    def room(i):   # a drawing goes on grid paper; a list of facts gets a blank for each; otherwise a work box
        if re.search(r'\bgrid\b', stem(i), re.I):
            return '<p>Draw on your grid paper.%s</p>' % ('' if re.search(r'\barea \d', stem(i)) else
                                                          ' Write the area inside each.')
        if facts_list(i):
            fs = facts_list(i)[1]
            return '<table class="facts"><tr>%s</tr></table>' % ''.join(
                '<td style="border:0;width:20%%">%s = ____</td>%s' % (x, '</tr><tr>' if k % 5 == 4 else '')
                for k, x in enumerate(fs))
        if i.get('figure') and i['figure'].split()[0] in FRACTION_FIGS:
            # the line or strips under the item are its work space (unit 2 reads, cheap day 9)
            return '<p>Answer: %s</p>' % ('_' * 30)
        if h.get('room') == 'line':   # worked on grid paper: the answer line only (s09 expert, day 77)
            return '<p>Answer: %s</p>' % ('_' * 30)
        if h.get('room') == 'tall':   # a whole search: a tall box and a full-width answer line (day 3 read)
            return '<div class="sketch tall"></div><p>Answer: %s</p>' % ('_' * 62)
        return '<div class="sketch work"></div><p>Answer: ______________________</p>'

    def asked(i):
        return facts_list(i)[0] + '.' if facts_list(i) else stacked(stem(i))
    sb = '<h1>%s</h1><p>Name ______________________ Date __________</p>%s%s%s' % (
        html.escape(title), mdh(section(body, 'Student') or ''), ''.join(
            '<p>%d. %s</p>%s%s' % (k + 1, asked(i), figure(fig_view(i['figure'], 'student'), 0.5) if i.get('figure') else '', room(i))
            for k, i in enumerate(rs)), foot)
    put(out / (name + '-student.html'), page(title, sb, 'student'), encoding='utf-8')
    put(out / (name + '-student-large.html'), page(title + ', large print', sb, 'student large'), encoding='utf-8')
    errname = {e['letter']: err_name(e['error']) for e in errors if e['stretch'] == h.get('stretch')}
    errname['x'] = ERR_X
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
        notes = [x[5:] for x in fails if x.startswith('NOTE ')]
        fails = [x for x in fails if not x.startswith('NOTE ')]
        byid = {i['item_id']: i for i in items}
        side_note = 'sides not counted (no Chrome)'
        if CHROME.exists() and d['sides']:   # the two-side rule, on the printed page
            import tempfile
            tmp = Path(tempfile.gettempdir()) / ('curio-%s-%s.html' % (c, p.stem))
            put(tmp, page('check', student_html(d, c, items), 'student'))
            side_note = print_sides(tmp)
            if 'FAIL' in side_note:
                fails.append('%s: the student page prints to more than two sides' % lab)
        hp = home_parts(d)
        print('%s: teacher %d words, student %d words (%d frame, %d questions), %d min, %s, %s, %d failure(s)' % (
            lab, words(teacher_prose(d)), words(d['student']) + stem_words(d, byid), words(d['student']),
            stem_words(d, byid), sum(b[0] for b in d['blocks']), side_note,
            'at home %d words, %d min' % (words(d['secs']['At home']), sum(x[0] for x in hp))
            if 'At home' in d['secs'] else 'no at home', len(fails)))
        for x in fails:
            print('  FAIL', x)
        for x in notes:
            print('  NOTE', x)
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
        for x in notes:
            print('  NOTE', x)
        bad += len(fails)
        if a[0] == 'build' and not fails:
            out = build_piece(pc, items, wrongs, errors)
            print('  built %s/%s' % (out.relative_to(ROOT).as_posix(), p.stem))
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main(sys.argv[1:])

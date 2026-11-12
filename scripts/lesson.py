"""Lesson days: check each day file against docs/courses/LESSON-DAY.md and build its print pages.

    python -X utf8 scripts/lesson.py check            every day file under courses/; exit 1 on any failure
    python -X utf8 scripts/lesson.py build [--pdf]    write the pages to build/lessons/ (--pdf also prints the
                                                      student page with Chrome and counts its sides)

A day file is courses/<course>/u<stretch>-<unit>/d<day>.md: a header block, "## Teacher page" with fixed
headings, then "## Student page". Questions are named by id, [[s11-P90-1]], and live in
data/plans/<course>/items.csv with their computed keys (scripts/plan.py). Nothing here types a key.
"""
import html, re, subprocess, sys, os, time
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
    md = NOTE.sub(' ', STEPS.sub(' ', REF.sub(' ', md)))
    md = re.sub(r'_{2,}|\{sketch\}|^\|[-| ]+\|$|[#*|>`]', ' ', md, flags=re.M)
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


def leans(d):
    return [x.strip() for x in d['head'].get('leans_on', '').split(';') if x.strip() and x.strip() != 'nothing']


def missing(d):
    return [x for x in leans(d) if not (ROOT / x).exists()]


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
        if row['opens_min'] and k + 1 < len(d['blocks']) and d['blocks'][k + 1][0] != int(row['opens_min']):
            f.append('%s: the opening after the warm-up is %d min; days.csv says %s'
                     % (lab, d['blocks'][k + 1][0], row['opens_min']))
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
    if not d['sides'] or len(d['sides']) > 2:
        f.append('%s: the student page needs "### Side 1" (and at most "### Side 2")' % lab)
    # questions
    refs = REF.findall(d['teacher'] + d['student']) + STEPS.findall(d['teacher']) + NOTE.findall(d['student'])
    for r in NOTE.findall(d['student']):
        if r in byid and not byid[r].get('figure'):
            f.append('%s: [[note:%s]] needs a figure cell to print from' % (lab, r))
    for r in refs:
        if r not in byid:
            f.append('%s: [[%s]] has no row in items.csv' % (lab, r))
        elif byid[r]['day'] != h.get('day'):
            f.append('%s: [[%s]] belongs to day %s' % (lab, r, byid[r]['day']))
    for i in items:
        if i['day'] == h.get('day') and i['check'] in plan.LESSON_KINDS | {'exit'} and i['item_id'] not in refs:
            f.append('%s: %s is a row for this day that no page uses' % (lab, i['item_id']))
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
.q { font-style: italic; } .blank { display: inline-block; border-bottom: 1px solid #000; height: 1em; vertical-align: baseline; }
.student td:first-child { width: 30%; font-size: 12pt; } .student td:nth-child(2) { width: 42%; } .meta td:first-child { width: 22%; font-weight: bold; }
.slip { border: 1px dashed #000; height: 4.6in; width: 48%; display: inline-block; box-sizing: border-box; padding: .25in; margin: 0 1% .2in 0; vertical-align: top; font-size: 13pt; }
.screen { min-height: 90vh; font-size: 30pt; line-height: 1.35; page-break-after: always; padding: .3in; border-bottom: 2px solid #000; }
.warn { border: 2px solid #000; padding: .4em; font-weight: bold; }
.screen svg { display: block; max-width: 100%; margin: .3em 0; } .screen li { color: #555; } .screen li.now { color: #000; font-weight: bold; }
.pair { display: flex; gap: .4in; } .pair > div { flex: 1; border: 2px solid #000; padding: .2in; }
.sketch.work { height: 0.8in; }
.foot { font-size: 9pt; margin-top: 1em; border-top: 1px solid #000; padding-top: .3em; }
"""


def page(title, body, cls):
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" '
            'content="width=device-width,initial-scale=1"><title>%s</title><style>%s</style></head>'
            '<body class="%s">%s</body></html>' % (html.escape(title), CSS, cls, body))


def stem(i):
    s = i['stem'].strip()
    return s[1:-1] if s.startswith('"') and s.endswith('"') and s.count('"') == 2 else s


def steps(i):
    return [s.strip() for s in (i.get('steps') or '').split('|') if s.strip()]


def md(text, items, teacher=False):
    """Day-file markdown to HTML. [[id]] prints the question (and on the teacher page its answer);
    [[steps:id]] prints the worked steps from the row, the same cell the display reveals."""
    byid = {i['item_id']: i for i in items}

    def sub(m):
        i = byid.get(m[1])
        if not i:
            return m[0]
        return '*%s*' % stem(i) + (' **[%s]**' % i['answer'] if teacher and i['answer'] else '')

    def sub_steps(m):
        i = byid.get(m[1])
        return '\n\n' + '\n'.join('%d. %s' % (k + 1, s) for k, s in enumerate(steps(i))) + '\n\n' if i else m[0]
    def sub_note(m):
        i = byid.get(m[1])
        return note(i) if i else m[0]
    text = NOTE.sub(sub_note, STEPS.sub(sub_steps, text))
    text = REF.sub(sub, text).replace('{sketch}', '<div class="sketch"></div>').replace(
        '{work}', '<div class="sketch work"></div>')
    text = re.sub(r'_{2,}', lambda m: '<span class="blank" style="width:%.1fem"></span>' % (len(m[0]) * 0.45), text)
    return markdown.markdown(text, extensions=['tables'])


def note(i):
    """'Lee: 48 square feet, 6 feet wide' from the stem's name and the figure cell's given numbers."""
    f = dict(x.split('=', 1) for x in i['figure'].split()[1:] if '=' in x)
    unit = {'ft': 'feet', 'in': 'inches'}.get(f.get('u', 'ft'), f.get('u', ''))
    who = re.search(r'The (\w+) family', i['stem'])
    given = (['%s square %s' % (f['A'], unit)] if 'A' in f else []) + (['%s %s of fence' % (f['P'], unit)] if 'P' in f else [])
    given += ['%s %s %s' % (f[k], unit, {'w': 'wide', 'l': 'long'}[k]) for k in ('w', 'l') if f.get(k, '?') != '?']
    return (who[1] + ': ' if who else '') + ', '.join(given)


def figure(spec, size=1.0):
    """A labelled rectangle from a figure cell: 'rect w=7 l=? A=63 u=ft' or 'rect l=12 w=? P=38 u=ft'."""
    f = dict(x.split('=', 1) for x in spec.split()[1:] if '=' in x)
    u = f.get('u', 'ft')
    unit = {'ft': 'feet', 'in': 'inches', 'cm': 'centimetres', 'm': 'metres'}.get(u, u)
    lab = lambda v: '?' if v == '?' else '%s %s' % (v, unit)
    W, H = 420 * size, 220 * size
    x0, y0, w, h = 170 * size, 60 * size, W, H
    mid = ''
    if 'A' in f:
        mid = '%s square %s inside' % (f['A'], unit)
    elif 'P' in f:
        mid = '%s %s of fence all the way around' % (f['P'], unit)
    fs = 36 * size
    t = lambda x, y, s, a='middle': '<text x="%.0f" y="%.0f" text-anchor="%s" font-size="%.0f">%s</text>' % (
        x, y, a, fs, html.escape(s))
    return ('<svg viewBox="0 0 %.0f %.0f" width="%.0f" style="width:100%%;max-width:9in;height:auto" role="img" aria-label="%s" xmlns="http://www.w3.org/2000/svg" '
            'font-family="Georgia, serif"><rect x="%.0f" y="%.0f" width="%.0f" height="%.0f" fill="none" stroke="#000" '
            'stroke-width="3"/>%s%s%s%s%s</svg>') % (
        W + 340 * size, H + 130 * size, W + 340 * size, html.escape('A rectangle: ' + ', '.join(
            '%s %s' % (k, v) for k, v in f.items())), x0, y0, w, h,
        t(x0 + w / 2, y0 - 14 * size, lab(f.get('l', ''))), t(x0 + w / 2, y0 + h + 46 * size, lab(f.get('l', ''))),
        t(x0 - 10 * size, y0 + h / 2, lab(f.get('w', '')), 'end'), t(x0 + w + 10 * size, y0 + h / 2, lab(f.get('w', '')), 'start'),
        t(x0 + w / 2, y0 + h / 2 + 8 * size, mid) if mid else '')


def foot_line(h, course, credits=()):
    s = 'Curio Class, %s, day %s, version %s, CC BY 4.0, curioclass.org' % (
        course_name(course), int(h['day']), h['version'])
    return '<div class="foot">%s%s</div>' % (html.escape(s), ''.join(
        '<br>%s' % html.escape(c) for c in credits))


def header_table(d, row, parts, tt):
    h = d['head']
    ps = '; '.join('%s (%s) %s' % (p['code'], p['part'], p['text']) for p in parts)
    cells = [('Day', '%s, unit %s, %s day' % (h['day'], h['unit'], row['kind'].lower())),
             ('Goal', row['goal']), ('Standard parts', ps or 'see the unit opener'),
             ('Tool', '%s (%s), %s min' % (tt, row['mark'], row['tool_min']) if row['tool'] else 'None'),
             ('Materials', h['materials']), ('Print', h['print']), ('Leans on', h.get('leans_on', '')),
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
    end = sorted((i for i in items if i['stretch'] == row['stretch'] and i['check'] == 'end'), key=lambda i: int(i['n']))
    if row['kind'] != 'Check':
        end = []
    pk = {(i['code'], i['part']) for i in (end or mine) if i['part']}
    parts = [p for p in parts_all if (p['code'], p['part']) in pk]
    out = OUT / course / d['path'].parent.name
    out.mkdir(parents=True, exist_ok=True)
    name = d['path'].stem
    title = d['title']
    byid = {i['item_id']: i for i in items}
    refs = sorted({r for r in REF.findall(d['teacher'] + d['student']) + STEPS.findall(d['teacher']) if r in byid},
                  key=lambda r: (ORDER.index(byid[r]['check']) if byid[r]['check'] in ORDER else 9,
                                 byid[r].get('path', ''), int(byid[r]['n'] or 0)))
    refs = [i['item_id'] for i in end] + [r for r in refs if r not in {i['item_id'] for i in end}]
    credits = sorted({byid[r]['source'] for r in refs if byid[r].get('source')})
    foot = foot_line(h, course, ([h['credit']] if h['credit'].lower() != 'ours' else []) + credits)
    gone = missing(d)
    warn = ('<p class="warn">Not ready to teach: %s missing.</p>' % html.escape(', '.join(gone))) if gone else ''
    tb = '<h1>%s</h1><p>Teacher page</p>%s%s%s%s' % (html.escape(title), warn, header_table(d, row, parts, tt),
                                                     md(d['teacher'], items, teacher=True), foot)
    (out / (name + '-teacher.html')).write_text(page(title + ': teacher page', tb, 'teacher'), encoding='utf-8')
    sb = student_html(d, course, items)
    (out / (name + '-student.html')).write_text(page(title + ': student page', sb, 'student'), encoding='utf-8')
    (out / (name + '-student-large.html')).write_text(page(title + ': student page, large print', sb, 'student large'),
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
        kr.append('<tr><td>%s</td><td>%s</td><td class="q">%s</td><td>%s</td><td>%s</td></tr>' % (
            html.escape(where), html.escape(i['item_id']), html.escape(stem(i)), ans, html.escape('; '.join(ws))))
    kb = ('<h1>%s: key</h1><p>Every answer below is recomputed by scripts/plan.py from data/plans/%s/items.csv.</p>'
          '<table><tr><th>Where</th><th>Id</th><th>Question</th><th>Answer</th><th>Wrong answers and what they mean</th>'
          '</tr>%s</table>%s' % (html.escape(title), course, ''.join(kr), foot))
    (out / (name + '-key.html')).write_text(page(title + ': key', kb, 'key'), encoding='utf-8')
    # exit slip, four to a sheet: the paper path only
    ex = [i for i in mine if i['check'] == 'exit' and i.get('path', '') in ('', 'paper')]
    if ex and row['kind'] != 'Check':
        one = '<div class="slip"><p>Name ______________ Day %s</p>%s%s</div>' % (h['day'], ''.join(
            '<p>%d. %s</p><p>__________________________</p><p>__________________________</p>' % (k + 1, html.escape(stem(i)))
            for k, i in enumerate(ex)), foot)
        (out / (name + '-exit.html')).write_text(page(title + ': exit slips', one * 4, 'student'), encoding='utf-8')
    # display: each worked example with its figure, then its steps one screen at a time; each fix with the wrong
    # working beside the right; one screen per planned question; the frames; a check-your-answers screen
    scr = []
    fig = lambda i: figure(i['figure']) if i.get('figure') else ''
    for r in refs:
        i = byid[r]
        if i['check'] == 'example':
            scr.append('<div class="screen"><p>%s</p>%s</div>' % (html.escape(stem(i)), fig(i)))
            st = steps(i)
            for k in range(len(st)):
                scr.append('<div class="screen">%s<ol>%s</ol></div>' % (fig(i) if k < 2 else '', ''.join(
                    '<li%s>%s</li>' % (' class="now"' if j == k else '', html.escape(s)) for j, s in enumerate(st[:k + 1]))))
        elif i['check'] == 'fix':
            st = steps(i) + ['', '']
            scr.append('<div class="screen"><p>%s</p>%s<div class="pair"><div><b>Their working</b><p>%s</p></div>'
                       '<div><b>The right working</b><p>%s</p></div></div></div>' % (
                           html.escape(stem(i)), fig(i), html.escape(re.sub(r'^.*?working: ', '', st[0])),
                           html.escape(re.sub(r'^.*?working: ', '', st[1]))))
    scr += ['<div class="screen">%s</div>' % html.escape(re.sub(r'[*]', '', q).strip())
            for q in re.findall(r'\*\*Ask\.\*\* "(.+?)"', d['teacher'])]
    scr += ['<div class="screen">%s</div>' % html.escape(q) for q in
            re.findall(r'"([^"]*__[^"]*)"', d['secs'].get('Words and supports', ''))]
    prac = [byid[r] for r in refs if byid[r]['check'] == 'practice']
    if prac:
        scr.append('<div class="screen"><p><b>Check your answers.</b> Put each answer back in its equation. Does it '
                   'give the number in the question? If not, put a question mark.</p><ol>%s</ol></div>' % ''.join(
                       '<li>%s</li>' % html.escape(stem(i)) for i in prac))
    if end:
        # the check day's display: the key-marked answers, for students marking their own in another colour
        scr.append('<div class="screen"><p><b>Answers.</b> Mark your own in another colour. Items %s are read by '
                   'your teacher.</p><ol>%s</ol></div>' % (
                       ' and '.join(i['n'] for i in end if i['judged'] == 'teacher') or 'none',
                       ''.join('<li value="%s">%s</li>' % (i['n'], html.escape(i['answer'] if i['judged'] == 'key'
                                                                           else 'read by your teacher'))
                               for i in end)))
    (out / (name + '-display.html')).write_text(page(title + ': display', ''.join(scr) + foot, 'display'),
                                                encoding='utf-8')
    note = ''
    if pdf:
        note = print_sides(out / (name + '-student.html'))
    return out, note


ORDER = ['example', 'tool', 'fix', 'practice', 'challenge', 'exit']


def print_sides(src):
    """Print the student page to PDF with headless Chrome and count its sides."""
    if not CHROME.exists():
        return 'page count not checked (no Chrome)'
    pdf = src.with_suffix('.pdf')
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
    from pypdf import PdfReader
    n = len(PdfReader(str(pdf)).pages)
    return '%d side(s)%s' % (n, '' if n <= 2 else ' FAIL: more than two')


# ------------------------------------------------------------------ once-per-unit pieces
# A piece is any other .md in a unit folder (opener.md, record.md, readiness.md, ...), with a header naming its
# kind: opener (written, 1,200 words at most), record (the record sheet, generated), check (a readiness check:
# student page and key generated from the rows), facts (a facts check sheet), family (the family note).
CAP_OPENER = 1200
PIECE_HEAD = ['piece', 'course', 'unit', 'version', 'credit']
PIECE_KINDS = ('opener', 'record', 'check', 'facts', 'family', 'sheet')


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
    h = p['head']
    return sorted([i for i in items if i['check'] == h.get('check') and i['stretch'] == h.get('stretch')],
                  key=lambda i: int(i['n'] or 0))


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
        (out / (name + '.html')).write_text(page(title, '<h1>%s</h1>%s%s' % (
            html.escape(title), mdh(body), unit_foot(h, course, name)), 'teacher'), encoding='utf-8')
        return out
    if kind == 'sheet':   # a page for the teacher: the preset's link, then the piece's own notes
        g = preset(h)
        url = 'https://curioclass.org' + g['url']
        (out / (name + '.html')).write_text(page(title, '<h1>%s</h1><p><b>Make and print it:</b> <a href="%s">%s</a>. '
            'Each press of New sheet gives a fresh sheet and its key; print one sheet per student and the key for '
            'you.</p>%s%s' % (html.escape(title), html.escape(url), html.escape(url), mdh(body), unit_foot(h, course, name)),
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
        (out / (name + '-student.html')).write_text(page(title, css + sb, 'student'), encoding='utf-8')
        key = ''.join('<td>%s %s</td>%s' % (q, eval(q[:-1].replace('×', '*').replace('÷', '//')),
                                             '</tr><tr>' if k % 4 == 3 else '') for k, q in enumerate(qs))
        (out / (name + '-key.html')).write_text(page(title + ': key', '<h1>%s: key</h1>%s<table><tr>%s</tr></table>%s' % (
            html.escape(title), mdh(section(body, 'Teacher') or ''), key, unit_foot(h, course, name)), 'key'), encoding='utf-8')
        return out
    if kind == 'record':
        st = h.get('stretch')
        looks = {k.strip(): int(v) for k, _, v in (x.partition('=') for x in h.get('lookfors', '').split(';')) if v}
        cols = [('R%s' % i['n'], 1) for i in items if i['stretch'] == st and i['check'] == 'readiness']
        cols += [('E%s' % d, 1) for d in sorted({i['day'] for i in items if i['stretch'] == st and i['check'] == 'exit'})]
        cols += [('End %s' % i['n'], looks.get(i['n'], 1)) for i in items if i['stretch'] == st and i['check'] == 'end']
        hd = '<tr><th>Student</th>%s</tr>' % ''.join('<th colspan="%d">%s</th>' % (n, html.escape(c)) for c, n in cols)
        sub = '<tr><th></th>%s</tr>' % ''.join(''.join('<th>%s</th>' % ('' if n == 1 else '%d' % (k + 1))
                                                      for k in range(n)) for _, n in cols)
        row = '<tr><td style="width:1.6in">&nbsp;</td>%s</tr>' % ('<td></td>' * sum(n for _, n in cols))
        css = ('<style>@page { size: letter landscape; margin: .4in; } body.record { max-width: none; font-size: 9pt; }'
               ' .record td { height: .26in; padding: 0 .2em; } .record th { font-size: 8pt; }</style>')
        tb = '<h1>%s</h1>%s<table>%s%s%s</table>%s' % (html.escape(title), mdh(body), hd, sub,
                                                     row * int(h.get('rows', 28)), unit_foot(h, course, 'record sheet'))
        (out / (name + '.html')).write_text(page(title, css + tb, 'record'), encoding='utf-8')
        return out
    # a check: the student page, a large-print copy, and the key
    rs = piece_rows(p, items)
    foot = unit_foot(h, course, '%s check' % h.get('check'))
    sb = '<h1>%s</h1><p>Name ______________________ Date __________</p>%s%s%s' % (
        html.escape(title), mdh(section(body, 'Student') or ''), ''.join(
            '<p>%d. %s</p><div class="sketch work"></div><p>Answer: ______________________</p>' % (k + 1, html.escape(stem(i)))
            for k, i in enumerate(rs)), foot)
    (out / (name + '-student.html')).write_text(page(title, sb, 'student'), encoding='utf-8')
    (out / (name + '-student-large.html')).write_text(page(title + ', large print', sb, 'student large'), encoding='utf-8')
    errname = {e['letter']: e['error'] for e in errors if e['stretch'] == h.get('stretch')}
    tail = lambda w: ((('error %s, %s' % (w['error'], errname.get(w['error'], '').lower())) if w['error'] else '')
                      + (' (%s)' % w['note'] if w['note'] else '')).strip()
    wr = lambda i: '; '.join(w['shown'] + (': ' + tail(w) if tail(w) else '')
                             for w in wrongs if w['item_id'] == i['item_id'])
    kr = ''.join('<tr><td>%s</td><td class="q">%s</td><td>%s</td><td>%s</td></tr>' % tuple(
        html.escape(x) for x in (i['n'], stem(i), i['answer'], wr(i))) for i in rs)
    kb = ('<h1>%s: key</h1>%s<table><tr><th>#</th><th>Question</th><th>Answer</th><th>Wrong answers and what they '
          'mean</th></tr>%s</table>%s' % (html.escape(title), mdh(section(body, 'Teacher') or ''), kr, foot))
    (out / (name + '-key.html')).write_text(page(title + ': key', kb, 'key'), encoding='utf-8')
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
            tmp.write_text(page('check', student_html(d, c, items), 'student'), encoding='utf-8')
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
        if not fails and pc['head'].get('piece') in ('check', 'facts') and CHROME.exists():
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

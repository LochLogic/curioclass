"""Field 5's Goal map for unit plans (docs/courses/UNIT-PLAN.md), filled in bulk (later.csv L102, 2026-11-22).

    python -X utf8 scripts/goalmap.py brief  <course> [--out FILE]    the reading brief for one course
    python -X utf8 scripts/goalmap.py insert <course> <rows.csv>      write the Goal map tables into the plans

brief: for each unit plan of the course that has no Goal map yet, each teaching day (a day that is not a check,
respond, mid or end day, as scripts/unitplan.py counts it) with its kind, goal and note from days.csv, then what the
course already says about that day: every table row of the plan whose first cell is the day (not the end-of-unit
item table, the readiness table or the generated day list), and any "Day N" paragraph. Where the day is written
(courses/<course>/u*/dNNN.md), the written day's timed parts instead: each part's heading and opening words, and the
exit ticket part in full. The writer reads the written day first, and the plan only where the day is silent.

insert: rows.csv has the columns plan, day, goal_verb, exit_kind, exit_shape, practice_shape (fault is ignored
here). Each plan named gets one table under a "Goal map. One row for each teaching day:" line at the end of field 5,
replacing any Goal map already there. Rows go in day order. Then run `scripts/unitplan.py check <course>`.
"""
import csv
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import unit_skeleton as sk  # noqa: E402

SKIP_HEADS = ('part (own words)', 'school day', 'the row and task', 'goal verb', 'part | item', 'item, minutes')
HEAD = 'Goal map. One row for each teaching day:'
COLS = '| Day | Goal verb | Exit kind | Exit shape | Practice shape |\n|---|---|---|---|---|'


def words(s, n):
    w = s.split()
    return ' '.join(w[:n]) + (' ...' if len(w) > n else '')


def plans(course):
    return sorted(glob.glob(os.path.join(ROOT, 'docs', 'courses', course, 's[0-9][0-9].md')))


def teach_days(course, unit):
    sk.set_subject(sk.subject_of(course))
    return [r for r in sk.unit_days(course, unit)
            if r['kind'].lower() not in ('check', 'respond') and r.get('assess', '') not in ('end', 'mid')]


def plan_notes(text):
    """day -> list of snippets from the plan's own tables and Day paragraphs."""
    out = {}
    skip, head, prev = False, '', ''
    for ln in text.splitlines():
        if ln.startswith('|'):
            c = [x.strip() for x in ln.strip().strip('|').split('|')]
            low = ln.lower()
            first = not prev.startswith('|')
            prev = ln
            if first:     # a table's first line is its heading row; only tables keyed by day are read
                skip = not re.search(r'day|exit', c[0].lower()) or any(h in low for h in SKIP_HEADS)
                head = ' / '.join(c[1:])
                continue
            if skip or set(ln) <= set('|-: '):
                continue
            m = re.match(r'(?:[A-Z]{1,2}|Days?\s*|Exit\s*)?(\d+)\b', c[0]) if c else None
            if m:
                out.setdefault(int(m.group(1)), []).append('[%s] %s' % (words(head, 12), words(' | '.join(c[1:]), 90)))
        else:
            prev = ln
            m = re.match(r'\**Days? (\d+)\b[^*]*\**[:.]', ln)
            if m:
                out.setdefault(int(m.group(1)), []).append('[para] ' + words(re.sub(r'\*', '', ln), 90))
    return out


def written(course, day):
    f = glob.glob(os.path.join(ROOT, 'courses', course, '*', 'd%03d.md' % day))
    if not f:
        return None
    text = open(f[0], encoding='utf-8').read()
    teacher = text.split('\n### Other rooms')[0]
    parts = re.split(r'\n#### ', teacher)[1:]
    out = []
    for p in parts:
        head, _, body = p.partition('\n')
        body = re.sub(r'\s+', ' ', body).strip()
        out.append('  * %s: %s' % (head.strip(), words(body, 110) if 'exit' in head.lower() else words(body, 18)))
    return out


def exit_items(course):
    """day -> exit items of data/plans/<course>/items.csv: the cards a written day's exit names by id."""
    p = os.path.join(ROOT, 'data', 'plans', course, 'items.csv')
    out = {}
    if not os.path.exists(p):
        return out
    for r in csv.DictReader(open(p, encoding='utf-8')):
        if r.get('check') == 'exit' and r.get('day', '').isdigit():
            out.setdefault(int(r['day']), []).append('  - item %s (%s): %s Answer: %s' % (
                r['item_id'], r.get('path') or r.get('judged') or '', words(r['stem'], 70), words(r['answer'], 25)))
    return out


def audit(course):
    """For plans that have a Goal map: each row beside the day's goal, written exit part and exit items."""
    items = exit_items(course)
    out = ['# Goal map audit: %s' % course, '']
    for p in plans(course):
        text = open(p, encoding='utf-8').read()
        unit = int(os.path.basename(p)[1:3])
        rows = {int(m.group(1)): m.group(0) for m in re.finditer(r'^\| (\d+) \| [^|]+ \| (?:produce|recogni[sz]e) \|.*$', text, re.M)}
        out.append('## plan s%02d' % unit)
        for r in teach_days(course, unit):
            d = int(r['day'])
            out.append('### day %d: %s' % (d, r['goal']))
            out.append('MAP: ' + rows.get(d, '(none)'))
            w = [x for x in (written(course, d) or []) if 'exit' in x.lower()[:40]]
            out.extend(w)
            out.extend(items.get(d, []))
        out.append('')
    return '\n'.join(out)


def brief(course):
    out = ['# Goal map brief: %s' % course, '']
    items = exit_items(course)
    for p in plans(course):
        text = open(p, encoding='utf-8').read()
        if HEAD.split('.')[0] in text and '| Exit kind |' in text:
            continue
        unit = int(os.path.basename(p)[1:3])
        days = teach_days(course, unit)
        if not days:
            continue
        notes = plan_notes(text)
        out.append('## plan s%02d' % unit)
        for r in days:
            d = int(r['day'])
            out.append('### day %d (%s): %s' % (d, r['kind'], r['goal']))
            if r.get('note'):
                out.append('note: ' + words(r['note'], 25))
            w = written(course, d)
            if w:
                out.append('WRITTEN DAY:')
                out.extend(w)
                out.extend(items.get(d, []))
            else:
                got = notes.get(d, [])[:4]
                out.extend('- ' + s for s in got)
                if not got:
                    out.append('- (plan names nothing for this day)')
        out.append('')
    return '\n'.join(out)


def cell(s):
    return re.sub(r'\s+', ' ', s.replace('|', '/')).strip()


def insert(course, rows_csv):
    rows = {}
    for r in csv.DictReader(open(rows_csv, encoding='utf-8')):
        rows.setdefault(r['plan'].strip().lower().replace('.md', ''), []).append(r)
    for key, rs in sorted(rows.items()):
        p = os.path.join(ROOT, 'docs', 'courses', course, key + '.md')
        text = open(p, encoding='utf-8').read()
        rs.sort(key=lambda r: int(r['day']))
        table = '\n'.join('| %s | %s | %s | %s | %s |' % (int(r['day']), cell(r['goal_verb']), cell(r['exit_kind']),
                                                         cell(r['exit_shape']), cell(r['practice_shape'])) for r in rs)
        block = '%s\n\n%s\n%s\n' % (HEAD, COLS, table)
        m = re.search(r'^## 6\. ', text, re.M)
        if not m:
            sys.exit('%s: no field 6 heading' % p)
        head, tail = text[:m.start()], text[m.start():]
        i = head.find(HEAD)
        if i >= 0:
            head = head[:i]
        head = head.rstrip('\n') + '\n\n' + block + '\n'
        open(p, 'w', encoding='utf-8', newline='\n').write(head + tail)
        print('wrote %s (%d rows)' % (os.path.relpath(p, ROOT), len(rs)))


if __name__ == '__main__':
    a = sys.argv[1:]
    if len(a) >= 2 and a[0] == 'brief':
        s = brief(a[1])
        if '--out' in a:
            open(a[a.index('--out') + 1], 'w', encoding='utf-8').write(s)
            print('%s: %d lines, %d words' % (a[1], s.count('\n'), len(s.split())))
        else:
            print(s)
    elif len(a) >= 2 and a[0] == 'audit':
        s = audit(a[1])
        open(a[a.index('--out') + 1], 'w', encoding='utf-8').write(s) if '--out' in a else print(s)
        if '--out' in a:
            print('%s: %d lines, %d words' % (a[1], s.count('\n'), len(s.split())))
    elif len(a) == 3 and a[0] == 'insert':
        insert(a[1], a[2])
    else:
        sys.exit(__doc__)

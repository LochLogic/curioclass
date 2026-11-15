"""Gate for written unit plans of the four core subjects (docs/courses/<course>/s{uu}.md).

    python -X utf8 scripts/unitplan.py check [<subject> | <course> ...] [--dir DIR] [--data-dir DIR] [--complete]

Arguments are courses or subjects (social-studies, math, ela, science); none means all courses of all four subjects
(a course with no days.csv yet has no units and is passed over). A course with no s{uu}.md is skipped (--complete makes
a missing unit plan a failure). --dir DIR reads DIR/<course>/s{uu}.md instead of docs/courses; --data-dir DIR reads
days.csv, source-map.csv and calendar.csv from DIR/<course>/ (DIR/calendar.csv) instead of data/plans (both for
tests). Prints `path:line: what` for each failure and `PASS path` or `FAIL path (n)` for each file; exit 1 on any
failure.

Fails on:
  - a marker line left by scripts/unit_skeleton.py (the TODO word with "(writer)");
  - a missing field heading of UNIT-PLAN.md (fields 2 to 10 as `## N. ...`) or the day list;
  - an owned code, or a lettered part it owes, that days.csv gives the unit and the plan never names (parts owed:
    unit_skeleton.parts_of; a choice standard owes no part, and when days.csv cites parts of a code a unit owes only
    the parts it cites);
  - an assessment day (end or mid) whose codes and owed parts are not each a row of field 5 with an item written; an
    observation day (observe) whose codes are not each named in the code cell of a field 5 item row;
  - a "?" standing for a lost apostrophe, quote or accented letter (a "?" inside a word, or opening a word), or the
    replacement character; URLs and code spans are skipped;
  - an em dash anywhere; "Curio" not followed by " Class";
  - a header day range, a day count or a day list that disagrees with days.csv (the day numbers and kinds);
  - a readiness check given on the unit's first day (field 4 `Given:` line), except in the course's first unit, whose
    start-of-year check is the last ten minutes of day 1 (a `Start-of-year check:` line is also a valid field 4 line);
  - math only: a cluster of an owned standard whose weight (major, supporting, additional, or prerequisite for high
    school) the plan does not state as `weight (cluster, cluster)`, or states differently from
    data/standards/ccss-math-focus.csv;
  - science only: an owned performance expectation with no row in the three-dimensions table of field 2, or a row
    with an empty practice, core idea or crosscutting concept cell; no anchoring phenomenon named in field 2;
  - ELA only: a strand of the owned codes (RL, RI, RF, W, SL, L) not named as `(RL)` and so on in field 2, or no text set;
  - ELA only, a note and never a failure: an anchor text of data/plans/ela-texts.csv for the unit that field 2 and field 10
    both leave unnamed;
  - math, ELA and science: a source-map.csv row of the unit whose source id field 10 does not name;
  - over the word cap of UNIT-PLAN.md, "Length" (the one home of the rule): 1,250 words for a unit plan, outside fields
    4, 5 and 6, the day list and skel blocks; 1,800 for a one-section merged document (one with `## U3.` to `## U11.`
    section fields after the day list), outside the same and U3, U4 and U6.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import unit_skeleton as sk  # noqa: E402

MARK = sk.MARK
CAP = 1250          # a unit plan (UNIT-PLAN.md, "Length")
CAP_MERGED = 1800   # a one-section unit, one merged document (U3 to U11 after the day list)
NOTES = []          # notes printed ahead of a file's PASS or FAIL line; they never fail a file
SHOWN = ['']        # the path being checked, for the notes
FIELDS = list(range(2, 11))
UNCOUNTED = {4, 5, 6, 'days', 'U3', 'U4', 'U6'}


def load_sections(lines):
    """{key: (start_line_index, end_line_index)} for fields 2..10 and 'days'; key repeats are collected as lists."""
    heads = []
    for i, ln in enumerate(lines):
        m = re.match(r'^## (\d+)\.\s', ln)
        mu = re.match(r'^## U(\d+)\.\s', ln)
        if m:
            heads.append((int(m.group(1)), i))
        elif mu:
            heads.append(('U' + mu.group(1), i))
        elif re.match(r'^## Day list\b', ln):
            heads.append(('days', i))
    spans = {}
    for n, (key, i) in enumerate(heads):
        end = heads[n + 1][1] if n + 1 < len(heads) else len(lines)
        spans.setdefault(key, []).append((i, end))
    return heads, spans


def cells(ln):
    return [c.strip() for c in ln.strip().strip('|').split('|')]


def check_file(path, course, unit):
    msgs = []

    def bad(line, what):
        msgs.append('%s:%s: %s' % (path, line if line else '-', what))

    text = Path(path).read_text(encoding='utf-8')
    lines = text.splitlines()
    sk.set_subject(sk.subject_of(course))
    rows = sk.unit_days(course, unit)
    if not rows:
        bad(0, 'days.csv has no unit %d' % unit)
        return msgs
    days = [int(r['day']) for r in rows]
    kinds = {int(r['day']): r['kind'] for r in rows}

    # em dash, Curio
    for i, ln in enumerate(lines, 1):
        if sk.EMDASH in ln:
            bad(i, 'em dash')
        if re.search(r'\bCurio\b(?! Class)', ln):
            bad(i, '"Curio" not followed by " Class"')

    # title
    m = re.match(r'^# Unit (\d+):\s*\S', lines[0] if lines else '')
    if not m:
        bad(1, 'title is not "# Unit N: Name"')
    elif int(m.group(1)) != unit:
        bad(1, 'title says unit %s, file is unit %d' % (m.group(1), unit))

    # sections
    heads, spans = load_sections(lines)
    for f in FIELDS:
        if f not in spans:
            bad(0, 'missing field %d heading (## %d. ...)' % (f, f))
        elif len(spans[f]) > 1:
            bad(spans[f][1][0] + 1, 'field %d heading twice' % f)
    if 'days' not in spans:
        bad(0, 'missing "## Day list" section')
    order = [k for k, _ in heads if isinstance(k, int)]
    if order != sorted(order):
        bad(0, 'fields out of order')

    # header: days
    head_txt = ' '.join(lines[:12])
    mh = re.search(r'\*\*Days ([^*]+)\*\*', head_txt)
    if not mh:
        bad(2, 'header has no "**Days A to B**"')
    else:
        got_days = set()
        for tok in re.split(r'\s*,\s*|\s+and\s+', mh.group(1).strip()):
            m3 = re.fullmatch(r'(\d+)(?: to (\d+))?', tok.strip())
            if not m3:
                bad(3, 'header days "%s" not understood' % mh.group(1))
                break
            lo = int(m3.group(1))
            hi = int(m3.group(2) or lo)
            got_days.update(range(lo, hi + 1))
        else:
            if got_days != set(days):
                bad(3, 'days %s, days.csv has %s' % (mh.group(1), sk.runs_text(days)))
    mc = re.search(r'\((\d+) course days', head_txt)
    if mc and int(mc.group(1)) != len(days):
        bad(3, '%s course days, days.csv has %d' % (mc.group(1), len(days)))

    # day list
    if 'days' in spans:
        s, e = spans['days'][0]
        got = {}
        for i in range(s, e):
            if lines[i].startswith('|'):
                c = cells(lines[i])
                if len(c) >= 3 and c[0].isdigit():
                    got[int(c[0])] = (i + 1, c[2])
        for d in days:
            if d not in got:
                bad(s + 1, 'day list lacks day %d' % d)
            elif got[d][1] != kinds[d]:
                bad(got[d][0], 'day %d kind "%s", days.csv has "%s"' % (d, got[d][1], kinds[d]))
        for d in sorted(set(got) - set(days)):
            bad(got[d][0], 'day %d is not in unit %d of days.csv' % (d, unit))

    # TODO markers
    todo = [i for i, ln in enumerate(lines, 1) if MARK in ln]
    for i in todo[:5]:
        bad(i, MARK + ' left')
    if len(todo) > 5:
        bad(todo[5], '... and %d more %s lines' % (len(todo) - 5, MARK))

    # codes
    f2 = chr(10).join(lines[spans[2][0][0]:spans[2][0][1]]) if 2 in spans else ''
    allrows = sk.days_rows(course)
    for c in sk.required_codes(rows, allrows):
        if not re.search(r'(?<![\w.])%s(?![A-Za-z0-9])' % re.escape(c), f2):
            bad(0, 'code %s%s not named in field 2' % (c, ' (lettered part)' if c[-1].islower() and c[:-1] in sk.std_text() else ''))

    # readiness
    if 4 in spans:
        s, e = spans[4][0]
        sec = lines[s:e]
        given = [(s + i + 1, ln) for i, ln in enumerate(sec)
                 if re.match(r'^\**Given:', ln) or re.match(r'^\**Retrieval only:', ln) or re.match(r'^\**Start-of-year check:', ln)]
        if not given:
            bad(s + 1, 'field 4 has no "Given:", "Retrieval only:" or "Start-of-year check:" line')
        for i, ln in given:
            m2 = re.search(r'(?<!before )\bday (\d+)\b', ln.split('Note there')[0], re.I)
            # the course's first unit (day 1) gives its check in the last ten minutes of day 1 (lead rule 2026-11-14)
            if ln.lstrip('*').startswith('Given:') and m2 and int(m2.group(1)) == days[0] and days[0] != 1:
                bad(i, 'readiness check given on the unit\'s first day (day %d)' % days[0])

    # assessment
    if 5 in spans:
        s, e = spans[5][0]
        have = {}
        items = []      # (line, code cell, longest other cell) of every numbered row, for observation days
        for i in range(s, e):
            ln = lines[i]
            if ln.startswith('|'):
                c = cells(ln)
                if len(c) >= 4 and c[0].isdigit():
                    have[(int(c[0]), c[1])] = (i + 1, c[3])
                if len(c) >= 3 and c[0].isdigit():
                    items.append((i + 1, c[1], max(len(x.split()) for x in c[2:])))
        for r in rows:
            if r['assess'] == 'observe':
                # observation tables are numbered by item, not day: each code named in some item's code cell
                d = int(r['day'])
                for c in sk.split_list(r['codes']):
                    rx = r'(?<![\w.])%s(?![A-Za-z0-9])' % re.escape(c)
                    hit = [x for x in items if re.search(rx, x[1])]
                    if not hit:
                        bad(s + 1, 'observation day %d: no item row names %s in its code cell' % (d, c))
                    elif all(x[2] < 3 for x in hit):
                        bad(hit[0][0], 'observation day %d: item for %s is empty' % (d, c))
                continue
            if r['assess'] not in ('end', 'mid'):
                continue
            d = int(r['day'])
            acodes = sk.split_list(r['codes'])
            full = []
            for c in acodes:
                full.append(c)
                full.extend(k for k in sk.parts_of(c, rows, allrows) if k not in acodes)
            if not any(k[0] == d for k in have):
                bad(s + 1, 'no item rows for assessment day %d' % d)
                continue
            for c in full:
                row = have.get((d, c))
                if row is None:
                    bad(s + 1, 'assessment day %d: no item for %s' % (d, c))
                elif MARK not in row[1] and len(row[1].split()) < 3:
                    bad(row[0], 'assessment day %d: item for %s is empty' % (d, c))

    # "?" for a character lost to encoding (an apostrophe, quote or accented letter written as "?")
    for i, ln in enumerate(lines, 1):
        x = re.sub(r'`[^`]*`', ' ', ln)
        x = re.sub(r'\]\([^)]*\)|<https?://[^>]*>|https?://\S+', ' ', x)
        if '\ufffd' in x or re.search(r'\w\?\w', x) or re.search(r'(?:^|[\s(\[|])\?(?=[A-Za-z0-9])', x):
            bad(i, '"?" or the replacement character where a letter, apostrophe or quote was lost (write UTF-8)')

    # subject checks (mechanical only); social studies has none
    if not sk.is_ss():
        subject_checks(course, unit, rows, lines, spans, bad)

    # word cap
    count = 0
    skip = set()
    for key in UNCOUNTED:
        for s, e in spans.get(key, []):
            skip.update(range(s, e))
    body = '\n'.join(ln for i, ln in enumerate(lines) if i not in skip)
    body = re.sub(r'<!-- skel -->.*?<!-- /skel -->', ' ', body, flags=re.S)
    body = re.sub(r'<!--.*?-->', ' ', body, flags=re.S)
    count = len(re.findall(r'\S+', body))
    merged = any(isinstance(k, str) and k.startswith('U') for k, _ in heads)
    cap = CAP_MERGED if merged else CAP
    if count > cap:
        bad(0, '%d words outside fields 4, 5, 6%s and the day list, cap %d%s'
            % (count, ', U3, U4, U6' if merged else '', cap, ' (merged one-section document)' if merged else ''))
    return msgs


def subject_checks(course, unit, rows, lines, spans, bad):
    text = '\n'.join(lines)
    f2 = '\n'.join(lines[spans[2][0][0]:spans[2][0][1]]) if 2 in spans else ''
    f10 = '\n'.join(lines[spans[10][0][0]:spans[10][0][1]]) if 10 in spans else ''
    codes = sk.required_codes(rows)
    if sk.SUBJ == 'math':
        found = {}
        for m in re.finditer(r'\b(major|supporting|additional|plus|prerequisite)\s*\(([^)]*)\)', text):
            for k in sk.split_list(m.group(2)):
                found.setdefault(k, m.group(1))
        for k, wt, cs in sk.math_clusters(codes):
            want = sk.WEIGHTWORD.get(wt)
            if not want:
                continue    # no weight on file for this cluster: the skeleton's TODO names the missing data
            if k not in found:
                bad(0, 'cluster %s (%s) has no stated weight: write "weight word (cluster, cluster)", as in the header' % (k, ', '.join(cs[:3])))
            elif found[k] != want:
                bad(0, 'cluster %s is stated %s, data/standards/ccss-math-focus.csv says %s' % (k, found[k], want))
    elif sk.SUBJ == 'science':
        have = {}
        lo, hi = spans[2][0] if 2 in spans else (0, 0)
        for i in range(lo, hi):
            if lines[i].startswith('|'):
                c = cells(lines[i])
                if c and sk.is_pe(c[0]):
                    have[c[0]] = (i + 1, c)
        for pe in [c for c in codes if sk.is_pe(c)]:
            row = have.get(pe)
            if row is None:
                bad(0, 'performance expectation %s has no row in the three-dimensions table of field 2' % pe)
            elif len(row[1]) < 4 or any(not x.strip() for x in row[1][1:4]):
                bad(row[0], '%s: practice, core idea and crosscutting concept must each be named' % pe)
        if not re.search(r'anchor', f2, re.I):
            bad(0, 'field 2 names no anchoring phenomenon or design problem')
    elif sk.SUBJ == 'ela':
        for key in sorted({sk.strand_of(c)[0] for c in codes}):
            if '(%s)' % key not in f2:
                bad(0, 'field 2 does not name the strand (%s) of the owned codes' % key)
        if not re.search(r'text set', f2, re.I):
            bad(0, 'field 2 names no text set')
        norm = lambda x: re.sub(r'[^a-z0-9]+', ' ', x.lower()).strip()
        have = norm(f2 + ' ' + f10)
        for t in sk.ela_texts(course, unit):
            if t['use'] == 'anchor' and norm(t['title']) not in have:
                NOTES.append('%s:-: note (not a failure): anchor text %s "%s" in data/plans/ela-texts.csv is named in neither field 2 nor field 10'
                             % (SHOWN[0], t['text_id'], t['title']))
    for r in sk.source_rows(course, unit):
        if r['source'] not in f10:
            bad(0, 'source-map.csv row %s is not named in field 10' % r['source'])


def shown(p):
    try:
        return Path(p).resolve().relative_to(sk.ROOT).as_posix()
    except ValueError:
        return Path(p).as_posix()


def main(a):
    if not a or a[0] != 'check':
        raise SystemExit(__doc__)
    a = a[1:]
    base = sk.DOCS
    complete = '--complete' in a
    a = [x for x in a if x != '--complete']
    if '--dir' in a:
        i = a.index('--dir')
        base = Path(a[i + 1])
        a = a[:i] + a[i + 2:]
    if '--data-dir' in a:
        i = a.index('--data-dir')
        sk.set_data_dir(a[i + 1])
        a = a[:i] + a[i + 2:]
    courses = []
    for x in a:
        courses.extend(sk.courses_of(x) if x in sk.SUBJECTS else [x])
    courses = courses or sk.courses_of(None)
    bad_any = False
    seen = 0
    for course in courses:
        if sk.subject_of(course) is None:
            print('not a course in data/plans/frames.csv: %s' % course)
            bad_any = True
            continue
        sk.set_subject(sk.subject_of(course))
        for u in sk.unit_numbers(course):
            p = base / course / ('s%02d.md' % u)
            if not p.exists():
                if complete:
                    print('FAIL %s (missing)' % p)
                    bad_any = True
                continue
            seen += 1
            del NOTES[:]
            SHOWN[0] = shown(p)
            msgs = check_file(shown(p), course, u)
            for m in msgs + NOTES:
                print(m)
            if msgs:
                bad_any = True
                print('FAIL %s (%d)' % (shown(p), len(msgs)))
            else:
                print('PASS %s' % shown(p))
    if not seen:
        print('no unit plans found for: %s' % ', '.join(courses))
    return 1 if bad_any else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

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
  - course data it cannot read (a days.csv or source-map.csv missing a column of its layout, a short row, a day that is
    not a whole number): one `path:-: cannot check:` line naming the file and its columns;
  - over the word cap of UNIT-PLAN.md, "Length" (the one home of the rule): 1,600 words for a unit plan, outside fields
    4, 5 and 6, the day list and skel blocks; 2,300 for a one-section merged document (one with `## U3.` to `## U11.`
    section fields after the day list), outside the same and U3, U4 and U6.
Section plans (docs/courses/<course>/u{uu}-{n}.md, added 2026-11-17 at the kindergarten probe) are checked with their
unit. Each fails on: a TODO(writer) marker; a missing field heading 1 to 11; an em dash or "Curio" without " Class"; a
lost "?"; a header day range that is not the section's days in days.csv; a `## Day N` block for a day outside the
section, or a section day with no block; a day whose `- **N min. Part.**` lines add up outside frames.csv
minutes_min to minutes_max; over 1,600 words outside fields 3, 4 and 6 and skel blocks.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import unit_skeleton as sk  # noqa: E402

MARK = sk.MARK
CAP = 1600          # a unit plan (UNIT-PLAN.md, "Length")
CAP_MERGED = 2300   # a one-section unit, one merged document (U3 to U11 after the day list)
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
    register_check(course, lines, spans, bad)

    # word cap
    count = 0
    skip = set()
    for key in UNCOUNTED:
        for s, e in spans.get(key, []):
            skip.update(range(s, e))
    body = '\n'.join(ln for i, ln in enumerate(lines) if i not in skip)
    body = re.sub(r'<!-- skel -->.*?<!-- /skel -->', ' ', body, flags=re.S)
    body = re.sub(r'<!--.*?-->', ' ', body, flags=re.S)
    body = re.sub(r'Sections: .*?\.(?= Days by kind)', ' ', body)   # generated from days.csv, not writing
    count = len(re.findall(r'\S+', body))
    merged = any(isinstance(k, str) and k.startswith('U') for k, _ in heads)
    cap = CAP_MERGED if merged else CAP
    if count > cap:
        bad(0, '%d words outside fields 4, 5, 6%s and the day list, cap %d%s'
            % (count, ', U3, U4, U6' if merged else '', cap, ' (merged one-section document)' if merged else ''))
    return msgs


SEC_CAP = 1600   # a section plan (UNIT-PLAN.md, "Length"), outside fields 3, 4 and 6
LOST_Q = re.compile(r'\w\?\w|(?<![\w(\[\s])\?\w|�')


def check_section(path, course, unit):
    """Failures for one section plan u{uu}-{n}.md (see the module doc)."""
    text = Path(path).read_text(encoding='utf-8')
    lines = text.split('\n')
    msgs = []

    def bad(i, what):
        msgs.append('%s:%d: %s' % (shown(path), i + 1, what))
    sec = re.search(r'u(\d+)-(\d+)\.md$', str(path))
    sid = '%d.%d' % (int(sec.group(1)), int(sec.group(2)))
    nums = [int(r['day']) for r in sk.days_rows(course) if (r.get('unit') or '').strip() == sid]
    fr = [r for r in sk.read_csv(sk.PLANS / 'frames.csv', sk.FRAMES_COLS) if r['course'] == course]
    lo, hi = (int(fr[0]['minutes_min']), int(fr[0]['minutes_max'])) if fr and fr[0]['minutes_min'] else (0, 999)
    if not nums:
        bad(-1, 'section %s has no days in days.csv' % sid)
    heads = {}
    for i, ln in enumerate(lines):
        m = re.match(r'## (\d+)\. ', ln)
        if m:
            heads[int(m.group(1))] = i
        if MARK in ln:
            bad(i, 'a skeleton marker left for the writer')
        if '—' in ln:
            bad(i, 'an em dash')
        if re.search(r'\bCurio\b(?! Class)', ln):
            bad(i, '"Curio" without " Class"')
        if 'http' not in ln and '`' not in ln and LOST_Q.search(ln):
            bad(i, 'a "?" standing for a lost character')
    for f in range(1, 12):
        if f not in heads:
            bad(-1, 'missing field heading "## %d. ..."' % f)
    m = re.search(r'\*\*Days? (\d+)(?: to (\d+))?\.\*\*', text)
    if nums and m:
        a, b = int(m.group(1)), int(m.group(2) or m.group(1))
        if (a, b) != (min(nums), max(nums)):
            bad(-1, 'header says days %d to %d; days.csv gives section %s days %d to %d'
                % (a, b, sid, min(nums), max(nums)))
    blocks, cur = {}, None
    for i, ln in enumerate(lines):
        d = re.match(r'## Day (\d+)\b', ln)
        if d:
            cur = int(d.group(1))
            blocks[cur] = [i, 0]
            continue
        if ln.startswith('## '):
            cur = None
        if cur is not None:
            mm = re.match(r'\s*- \*\*(\d+) min\. ', ln)
            if mm:
                blocks[cur][1] += int(mm.group(1))
    for n, (i, total) in blocks.items():
        if nums and n not in nums:
            bad(i, 'day %d is not in section %s' % (n, sid))
        elif not total:
            bad(i, 'day %d has no "- **N min. Part.**" lines' % n)
        elif not lo <= total <= hi:
            bad(i, 'day %d parts add up to %d minutes; the day is %d to %d' % (n, total, lo, hi))
    for n in nums:
        if n not in blocks:
            bad(-1, 'section day %d has no "## Day %d" block' % (n, n))
    skip = set()
    order = sorted(heads.items(), key=lambda x: x[1])
    for k, (f, start) in enumerate(order):
        end = order[k + 1][1] if k + 1 < len(order) else len(lines)
        if f in (3, 4, 6):
            skip.update(range(start, end))
    body = '\n'.join(ln for i, ln in enumerate(lines) if i not in skip)
    body = re.sub(r'<!-- skel -->.*?<!-- /skel -->', ' ', body, flags=re.S)
    body = re.sub(r'<!--.*?-->', ' ', body, flags=re.S)
    count = len(re.findall(r'\S+', body))
    if count > SEC_CAP:
        bad(-1, '%d words outside fields 3, 4 and 6, cap %d' % (count, SEC_CAP))
    return msgs


def register_check(course, lines, spans, bad):
    # one mistake per register letter (UNIT-PLAN field 6; social studies probe, 2026-11-15)
    if 6 in spans:
        lo, hi = spans[6][0]
        for i in range(lo, hi):
            c = cells(lines[i]) if lines[i].startswith('|') else []
            if len(c) < 2 or not re.fullmatch(r'[A-Z]{1,2}', c[0]):
                continue
            err = re.split(r'\b(?:right|correct|Right|Correct)\s*:', c[1])[0]
            if ';' in err:
                what = 'error %s joins two claims with a semicolon: one misconception per letter (UNIT-PLAN field 6)' % c[0]
                if course == 'math-4':     # its plans predate the rule; reworked in step 5
                    NOTES.append('%s:%d: note (not a failure): %s' % (SHOWN[0], i + 1, what))
                else:
                    bad(i + 1, what)
    # one wrong answer sorts a student into one group: "error D or I", "(D or I)" (second probe, 2026-11-15)
    two = re.compile(r'\b(?:errors?|letters?)\s+([A-Z])\s+or\s+([A-Z])\b|\(\s*([A-Z])\s+or\s+([A-Z])\s*\)')
    pair = re.compile(r'\(\s*([A-Z])\s*,\s*([A-Z])\s*\)')
    for f in (5, 6, 7):
        for lo, hi in spans.get(f, []):
            for i in range(lo, hi):
                if two.search(lines[i]):
                    what = 'one wrong answer tagged with two letters ("%s"): tag the letter whose text describes it (UNIT-PLAN field 6)' % two.search(lines[i]).group(0)
                    if course == 'math-4':
                        NOTES.append('%s:%d: note (not a failure): %s' % (SHOWN[0], i + 1, what))
                    else:
                        bad(i + 1, what)
                elif f == 5 and pair.search(lines[i]):
                    NOTES.append('%s:%d: note (not a failure): "%s" tags two letters; if it is one wrong answer, keep one'
                                 % (SHOWN[0], i + 1, pair.search(lines[i]).group(0)))


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


# ------------------------------------------------------------------ new gates (L87 step 8, 2026-11-21)
# Two tagged checks on field 5's "Goal map" table (docs/courses/UNIT-PLAN.md): exit-kind and practice-shape. They print
# their own line after a file's old lines ("FAIL exit-kind: path:line: ...") and are not counted in the file's "(n)",
# so the old output stays as it was.
NEW_TAGS = ('exit-kind', 'practice-shape')
PRODUCE = {'explain', 'describe', 'draw', 'write', 'build', 'make', 'solve', 'compose', 'construct', 'create', 'argue',
           'justify', 'tell', 'say', 'compare', 'retell', 'summarize', 'summarise', 'design', 'model', 'predict', 'revise',
           'plan', 'calculate', 'compute', 'show', 'give', 'state', 'report', 'present', 'perform', 'read aloud'}
RECOGNISE = {'identify', 'recognise', 'recognize', 'choose', 'select', 'match', 'circle', 'point', 'notice', 'spot', 'sort',
             'pick', 'tell apart', 'distinguish'}
# 'find' and 'locate' are in neither list: in math "find the sum" or "locate 3/4 on a number line" asks the child to
# produce, in ELA "find the detail" asks them to recognise; the writer chooses by what the goal asks (2026-11-22).
KINDS_OK = {'produce', 'recognise', 'recognize'}


def goal_map(lines, spans):
    """Rows of field 5's goal map: (line number, day, verb, kind, exit shape, practice shape). The table's heading row
    names its columns (Day, Goal verb, Exit kind, Exit shape, Practice shape), in any order."""
    rows = []
    if 5 not in spans:
        return None
    s, e = spans[5][0]
    cols, found = None, False
    for i in range(s, e):
        ln = lines[i]
        if not ln.startswith('|'):
            cols = None      # a table ends at the first line that is not a row; the next table names its own columns
            continue
        c = cells(ln)
        low = [x.lower() for x in c]
        if 'exit kind' in low:
            cols, found = {x: k for k, x in enumerate(low)}, True
            continue
        if cols and c and c[0].isdigit() and not set(ln) <= set('|-: '):
            g = lambda name: c[cols[name]].strip() if name in cols and cols[name] < len(c) else ''
            rows.append((i + 1, int(c[0]), g('goal verb').lower(), g('exit kind').lower(), g('exit shape').lower(),
                         g('practice shape').lower()))
    return rows if found else None


def new_gates(path, course, unit):
    """Lines of the exit-kind and practice-shape checks for one unit plan: every teaching day of the unit (a day that is
    not an assessment or respond day) has a goal-map row; its exit kind is produce or recognise and agrees with its
    goal verb; its practice shape is named and differs from its exit shape."""
    text = Path(path).read_text(encoding='utf-8') if Path(path).exists() else Path(sk.ROOT / path).read_text(encoding='utf-8')
    lines = text.splitlines()
    sk.set_subject(sk.subject_of(course))
    urows = sk.unit_days(course, unit)
    heads, spans = load_sections(lines)
    out = []
    gm = goal_map(lines, spans)
    teach = [int(r['day']) for r in urows
             if r['kind'].lower() not in ('check', 'respond') and r.get('assess', '') not in ('end', 'mid')]
    if gm is None:
        if teach:
            out.append('exit-kind: %s:-: field 5 has no "Goal map" table (Day, Goal verb, Exit kind, Exit shape, Practice shape) '
                       'naming each goal\'s exit kind' % path)
        return out
    have = {d: (ln, v, k, es, ps) for ln, d, v, k, es, ps in gm}
    for d in teach:
        if d not in have:
            out.append('exit-kind: %s:-: day %d has no goal-map row' % (path, d))
            continue
        ln, verb, kind, es, ps = have[d]
        if kind not in KINDS_OK:
            out.append('exit-kind: %s:%d: day %d exit kind "%s" is neither produce nor recognise' % (path, ln, d, kind))
        else:
            # A goal with two verbs ("choose and explain") names both, joined by "and" or a comma; the exit kind
            # agrees with the goal when it agrees with any listed verb (2026-11-22).
            vs = [w.split()[0] for w in re.split(r'\s*(?:,|\band\b)\s*', verb) if w.strip()] if verb else []
            k = 'recognise' if kind.startswith('recogni') else 'produce'
            own = PRODUCE if k == 'produce' else RECOGNISE
            other = RECOGNISE if k == 'produce' else PRODUCE
            v = vs[0] if vs else ''
            if vs and not any(x in own for x in vs) and any(x in other for x in vs):
                out.append('exit-kind: %s:%d: day %d goal verb "%s" asks to %s but the exit kind is %s'
                           % (path, ln, d, verb, 'recognise' if v in RECOGNISE else 'produce', k))
        if not ps:
            out.append('practice-shape: %s:%d: day %d names no practice shape' % (path, ln, d))
        elif not es:
            out.append('practice-shape: %s:%d: day %d names no exit shape' % (path, ln, d))
        elif re.sub(r'\W+', ' ', ps).strip() == re.sub(r'\W+', ' ', es).strip():
            out.append('practice-shape: %s:%d: day %d practice shape "%s" is the exit\'s shape; practice and exit must differ'
                       % (path, ln, d, ps))
    for d in sorted(set(have) - set(days_of(urows))):
        out.append('exit-kind: %s:%d: goal-map day %d is not a day of unit %d' % (path, have[d][0], d, unit))
    return out


def days_of(urows):
    return [int(r['day']) for r in urows]


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
        try:
            units = sk.unit_numbers(course)
        except sk.DataError as e:
            print('FAIL %s (cannot read: %s)' % (course, e))
            bad_any = True
            continue
        for u in units:
            p = base / course / ('s%02d.md' % u)
            if not p.exists():
                if complete:
                    print('FAIL %s (missing)' % p)
                    bad_any = True
                continue
            seen += 1
            del NOTES[:]
            SHOWN[0] = shown(p)
            try:
                msgs = check_file(shown(p), course, u)
            except sk.DataError as e:
                # course data the gate cannot read (a source map not in the one layout, a short days.csv row): a
                # failure naming the file and its columns, never a traceback
                msgs = ['%s:-: cannot check: %s' % (shown(p), e)]
            for m in msgs + NOTES:
                print(m)
            if msgs:
                bad_any = True
                print('FAIL %s (%d)' % (shown(p), len(msgs)))
            else:
                print('PASS %s' % shown(p))
            try:
                ng = new_gates(shown(p), course, u)
            except sk.DataError:
                ng = []
            for m in ng:
                print('FAIL', m)
            bad_any = bad_any or bool(ng)
            for q in sorted(p.parent.glob('u%02d-*.md' % u)):
                seen += 1
                qm = check_section(q, course, u)
                for m in qm:
                    print(m)
                if qm:
                    bad_any = True
                    print('FAIL %s (%d)' % (shown(q), len(qm)))
                else:
                    print('PASS %s' % shown(q))
    if not seen:
        print('no unit plans found for: %s' % ', '.join(courses))
    return 1 if bad_any else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

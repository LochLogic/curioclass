"""Section skeletons: one section plan's mechanical fields filled from data, every judgment field marked.

    python -X utf8 scripts/section_skeleton.py <course> <section>|u<unit>|all [--force] [--out DIR] [--data-dir DIR]
    python -X utf8 scripts/section_skeleton.py --self-test

Built 2026-11-16 for the section plan authoring plan (PRODUCTION-PATH step 7, "How section plans are authored"): a
script, never a model, so the facts are exact, the output is the same every run, and it can be rebuilt after any
days.csv change. It sits ahead of the Codex writer, which fills only the marked fields.

Writes a sidecar, docs/courses/<course>/section-skeletons/u<uu>-<s>.md (or DIR/<course>/u<uu>-<s>.md with --out),
never the section plan itself. Never overwrites without --force. Fields follow the section plan blank copy in
docs/courses/UNIT-PLAN.md; lines between the skel markers are copies of data and do not count toward the cap.

Filled from: days.csv (the section's days, kinds, checks, goals, notes, codes, skills, tools, supplies, safety), the
frame (unit title and question), frames.csv (minutes), the standards files (own-word lines), the progression (each
skill's grade), source-map.csv (each day's credit), sources.csv and items.csv where they exist, and the unit plan
s<uu>.md: its field 2 lines naming the section's days, its field 5 and field 6 rows for those days, its field 7
respond line and field 8. A unit that was one section until the 2026-11-16 cuts keeps its section fields in the unit
plan (U3 to U11): table rows are sliced by day, and the prose is copied into every section, flagged for the writer
to keep only what belongs to this section's days.
"""
import re
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import unit_skeleton as u     # noqa: E402
import day_skeleton as dk    # noqa: E402

SEC_DIR = 'section-skeletons'
DAYNUM = re.compile(r'(?<![\w.\-/])(\d{1,3})(?![\w.\-/%])')


# ---- reading the unit plan

def plan_text(course, unit):
    p = u.DOCS / course / ('s%02d.md' % unit)
    return p.read_text(encoding='utf-8') if p.exists() else None


def field(text, head):
    """Body of the `## <head>` field (head is a regex such as '5\\.' or 'U6\\.'), skel markers dropped, or ''."""
    if not text:
        return ''
    m = re.search(r'^## %s.*?\n(.*?)(?=^## |\Z)' % head, text, re.M | re.S)
    return re.sub(r'<!-- /?skel -->\n?', '', m.group(1)).strip() if m else ''


def mentions(line, days):
    """True when a line names one of the days as a bare number (not inside a code such as D2.Civ.3.3-5)."""
    line = re.sub(r'\b(?:pages?|pp?\.|grades?|lessons?|units?|minutes?)\s+\d+(?:\s*(?:,|to|and)\s*\d+)*', ' ', line, flags=re.I)
    return any(int(x) in days for x in DAYNUM.findall(line))


def split_blocks(body):
    """[(kind, lines)]: kind 'table' for a markdown table, 'text' for a paragraph or list item run."""
    out, cur, kind = [], [], None
    for ln in body.splitlines():
        k = 'table' if ln.lstrip().startswith('|') else ('blank' if not ln.strip() else 'text')
        if k == 'blank':
            if cur:
                out.append((kind, cur))
            cur, kind = [], None
            continue
        if kind and k != kind:
            out.append((kind, cur))
            cur = []
        kind = k
        cur.append(ln)
    if cur:
        out.append((kind, cur))
    return out


def day_cell(row):
    cells = [c.strip() for c in row.strip().strip('|').split('|')]
    return int(cells[0]) if cells and cells[0].isdigit() else None


def slice_table(lines, days):
    """Header, divider and the rows whose first cell is one of the days; None if the table has no Day column."""
    if len(lines) < 3 or not any(day_cell(r) is not None for r in lines[2:]):
        return None
    rows = [r for r in lines[2:] if day_cell(r) in days]
    return lines[:2] + rows if rows else []


def sliced(body, days, prose='lines'):
    """A unit-plan field cut to this section: Day-keyed table rows of the section's days; prose either as the
    lines naming a section day ('lines') or whole ('all', for the merged U fields)."""
    out, whole = [], []
    for kind, lines in split_blocks(body):
        if kind == 'table':
            t = slice_table(lines, days)
            if t:
                out.append('\n'.join(t))
            elif t is None and prose == 'all':
                whole.append('\n'.join(lines))
        elif prose == 'all':
            whole.append('\n'.join(lines))
        else:
            hits = [ln for ln in lines if mentions(ln, days)]
            if hits:
                out.append('\n'.join(hits))
    return out, whole


def quote(lines_or_blocks):
    out = []
    for b in lines_or_blocks:
        if out:
            out.append('>')
        out.extend(('> ' + ln) if ln.strip() else '>' for ln in b.splitlines())
    return out


# ---- the section

def sections_of(allrows, unit):
    """[(section, [rows])] of one unit in day order."""
    out = []
    for r in allrows:
        if r['stretch'] != str(unit):
            continue
        if out and out[-1][0] == r['unit']:
            out[-1][1].append(r)
        else:
            out.append((r['unit'], [r]))
    return out


def kinds_line(rows):
    order = ['Understanding', 'Fluency', 'Application', 'Check', 'Respond']
    parts = []
    for k in order + sorted({r['kind'] for r in rows} - set(order)):
        ds = [r['day'] for r in rows if r['kind'] == k]
        if ds:
            parts.append('%s %d (%s)' % (k.lower(), len(ds), ', '.join(ds)))
    return ', '.join(parts)


def owner_of(allrows, item_day, code, secs):
    """The section that last taught the code before the item's day: the section that owns the item."""
    t = u.taught_before(allrows, code.lstrip('~'), item_day)
    if not t:
        return None
    last = max(t)
    return next((s for s, rs in secs if any(int(r['day']) == last for r in rs)), None)


def build(course, section):
    subj = u.subject_of(course)
    if subj is None:
        raise u.DataError('%s is not a course in data/plans/frames.csv' % course)
    u.set_subject(subj)
    allrows = u.days_rows(course)
    if not re.fullmatch(r'\d+\.\d+', section):
        raise u.DataError('section must look like 3.2, not "%s"' % section)
    unit = int(section.split('.')[0])
    secs = sections_of(allrows, unit)
    names = [s for s, _ in secs]
    if section not in names:
        raise u.DataError('%s unit %d has no section %s in days.csv (it has %s)' % (course, unit, section, ', '.join(names) or 'none'))
    i = names.index(section)
    rows = secs[i][1]
    days = [int(r['day']) for r in rows]
    dayset = set(days)
    meta = dk.frame_meta(course)
    cg = u.grade_num(meta.get('grade'))
    prog = u.progression()
    text = plan_text(course, unit)
    merged = bool(text and re.search(r'^## U3\.', text, re.M))
    title, question = '(no frame row)', ''
    cells = u.frame_unit(course, unit)
    if cells:
        title, question = u.split_title(re.sub(r'\*\*', '', cells[1]))
    unit_days = [int(r['day']) for r in allrows if r['stretch'] == str(unit)]
    lo, hi = meta.get('minutes_min', ''), meta.get('minutes_max', '')
    mins = (lo if lo == hi else '%s to %s' % (lo, hi)) if lo else ''

    # ---- what stops or warns before writing
    stops, warns = [], []
    if text is None:
        stops.append('no unit plan docs/courses/%s/s%02d.md: the section plan is written after its unit plan' % (course, unit))
    else:
        want = re.search(r'Sections: (.*?)\.(?= Days by kind)', text)
        have = '; '.join('%s (days %s to %s)' % (s, rs[0]['day'], rs[-1]['day']) for s, rs in secs)
        if want and want.group(1) != have:
            warns.append('the unit plan header lists sections "%s", but days.csv has "%s": run section_cuts.py headers '
                         '(later.csv L66)' % (want.group(1), have))
    if subj == 'ela':
        for t in u.ela_texts(course, unit):
            if 'to write' in (t.get('status') or '').lower():
                stops.append('core text %s (%s), "%s", is still to write: Curio Class writes it before the unit\'s '
                             'section plans (later.csv L58)' % (t['text_id'], t['use'], t['title']))
    for x in dk.lead_rows(course, unit):
        warns.append('open calendar finding (unit-rejections.csv, %s lens): %s' % (x['lens'], u.clean(x['finding'])))
    if len(rows) > 6:
        warns.append('%d days, over the 6-day section length: section_cuts.py marked it "long:"; confirm it reads as one '
                     'piece of work' % len(rows))

    L = []
    w = L.append
    w('# Section %s skeleton: %s' % (section, u.clean(title)))
    w('')
    w('A sidecar for the section plan writer (scripts/section_skeleton.py). Lines between the markers are copies of '
      'data: change the data, not these lines. Every %s is the writer\'s. The plan itself is '
      'docs/courses/%s/u%02d-%s.md, written in the fields of docs/courses/UNIT-PLAN.md "Blank copy: section plan".'
      % (u.MARK, course, unit, section.split('.')[1]))
    w('')
    if stops or warns:
        w('## Before writing')
        w('')
        w(u.OPEN)
        for s in stops:
            w('- **STOP:** %s.' % s.rstrip('.'))
        for s in warns:
            w('- **Warning:** %s.' % s.rstrip('.'))
        w(u.CLOSE)
        w('')

    # ---- header
    w('## Header')
    w('')
    w(u.OPEN)
    w('%s. Unit %d, %s (days %d to %d): see [s%02d.md](s%02d.md). **Days %d to %d.** Days by kind: %s. A plan, not '
      'a lesson: nothing here is built or tried with %s. Fields follow UNIT-PLAN.md.' % (
          meta.get('title', course), unit, u.clean(title), unit_days[0], unit_days[-1], unit, unit, days[0], days[-1],
          kinds_line(rows), 'children' if (cg is not None and cg <= 5) else 'students'))
    w('')
    if question:
        w('- Compelling question (frame): "%s"' % u.clean(question))
    w('- Section %d of %d in the unit%s.' % (i + 1, len(secs), '; the unit plan holds its section fields as U3 to U11 '
                                             '(a one-section unit until the 2026-11-16 cuts)' if merged else ''))
    if mins:
        w('- Day length (frames.csv): %s minutes.' % mins)
    w(u.CLOSE)
    w('')
    w('%s: the title (a plain name for this piece of learning) if the one above does not fit.' % u.MARK)
    w('')

    # ---- 1. standards
    w('## 1. Standards and practices')
    w('')
    w(u.OPEN)
    codes = []
    for r in rows:
        for c in u.split_list(r['codes']):
            if c not in codes:
                codes.append(c)
    for c in codes:
        on = [r['day'] for r in rows if c in u.split_list(r['codes'])]
        begun = c.startswith('~') and len(c) > 1
        txt = u.std_line(c[1:] if begun else c)
        w('- **%s** (days %s)%s: %s' % (c, ', '.join(on), ', begun here and owned later' if begun else '',
                                       u.clean(txt) if txt else '(no own-word line on file)'))
    skills = []
    for r in rows:
        for s in u.split_list(r['skills']):
            if s not in skills:
                skills.append(s)
    for s in skills:
        p = prog.get(s)
        g = u.grade_num(p['grade']) if p else None
        w('- skill %s%s' % (s, ' (not a progression row)' if p is None else
                            ' (grade %s, earlier grade: review, never taught as new)' % p['grade'] if (g is not None and cg is not None and g < cg)
                            else ' (grade %s)' % p['grade']))
    f2, _ = sliced(field(text, r'2\.'), dayset)
    if f2:
        w('')
        w('Unit plan field 2, the lines naming this section\'s days:')
        w('')
        L.extend(quote(f2))
    w(u.CLOSE)
    w('')
    w('%s: this section\'s share of each code with its verb quoted; the limits that bite here; connections with their '
      'day; what the teacher page must explain.%s' % (u.MARK, ' Strategies or algorithm where the standard sets one; '
                                                      'one or two practices, each with its day and task.' if subj == 'math' else ''))
    w('')

    # ---- 2. where it sits
    w('## 2. Where it sits')
    w('')
    w(u.OPEN)
    if i > 0:
        ps, prs = secs[i - 1]
        w('- Before: section %s (days %s to %s), ending day %s: %s' % (ps, prs[0]['day'], prs[-1]['day'], prs[-1]['day'], u.clean(prs[-1]['goal'])))
    else:
        w('- Before: the start of unit %d.' % unit)
    if i + 1 < len(secs):
        ns, nrs = secs[i + 1]
        w('- After: section %s (days %s to %s), opening day %s: %s' % (ns, nrs[0]['day'], nrs[-1]['day'], nrs[0]['day'], u.clean(nrs[0]['goal'])))
    else:
        nxt = next((r for r in allrows if int(r['day']) > days[-1]), None)
        w('- After: the end of unit %d%s' % (unit, ('; next, day %s (%s): %s' % (nxt['day'], nxt['kind'], u.clean(nxt['goal']))) if nxt else ', the last of the course'))
    rd = [int(r['day']) for r in allrows if r['assess'] == 'readiness' and int(r['day']) <= unit_days[0]]
    if rd:   # given in the last minutes of the day before the unit (or on its first day); a readiness day at the
        w('- The readiness check for this unit: day %d (days.csv).' % max(rd))   # a readiness day at the unit end is the next unit's
    w(u.CLOSE)
    w('')
    w('%s: one or two lines; the readiness items it uses, and where its own results go.' % u.MARK)
    w('')

    # ---- 3. checks
    w('## 3. Checks, written first')
    w('')
    w(u.OPEN)
    for r in rows:
        if r['assess']:
            w('- Day %s: assessment "%s" (%s day).' % (r['day'], r['assess'], r['kind']))
    f5rows, _ = sliced(field(text, r'5\.'), set(unit_days))
    owned = []
    for t in f5rows:
        lines = t.splitlines()
        if not lines[0].lstrip().startswith('|'):
            continue
        head = [c.strip().lower() for c in lines[0].strip().strip('|').split('|')]
        ci = head.index('code') if 'code' in head else None
        for ln in lines[2:]:
            cells = [c.strip() for c in ln.strip().strip('|').split('|')]
            d = day_cell(ln)
            if ci is None or d is None or ci >= len(cells):
                continue
            own = owner_of(allrows, d, cells[ci], secs)
            if own == section:
                if not owned:
                    owned.extend(lines[:2])
                owned.append(ln)
    if owned:
        w('')
        w('End-of-unit assessment rows (unit plan field 5) whose code this section taught last, so this section owns them '
          '(an "Owner" cell may still name the old one-section placeholder):')
        w('')
        L.extend(owned)
    items = [x for x in dk.plan_csv(course, 'items') if x.get('day', '').strip().isdigit() and int(x['day']) in dayset]
    if items:
        w('')
        w('items.csv rows on these days:')
        for x in items:
            w('- [[%s]] day %s (%s): key: %s' % (x['item_id'], x['day'], x.get('check', ''),
                                                 u.clean((x.get('answer') or x.get('compute') or 'NONE').strip())))
    w(u.CLOSE)
    exits = [r['day'] for r in rows if r['kind'] in ('Understanding', 'Fluency', 'Application')]
    w('')
    w('%s: the unit assessment items this section owns, by number; then an exit question for each teaching day (%s), '
      'in full, with its answer and its wrong answers by error letter (rule 4: no taught numbers or cases).' % (
          u.MARK, ', '.join(exits) or 'none'))
    w('')

    # ---- 4. errors
    w('## 4. Expected errors and first ideas')
    w('')
    f6, _ = sliced(field(text, r'6\.'), dayset)
    reg = [b for b in (field(text, r'6\.').split('\n')) if b.lstrip().startswith('|')]
    named = [ln for ln in reg[2:] if mentions(ln, dayset)]
    w(u.OPEN)
    if named:
        w('Error register rows (unit plan field 6) that name one of this section\'s days:')
        w('')
        L.extend(reg[:2] + named)
    elif reg:
        w('No error register row names one of days %d to %d; the register has letters %s.' % (
            days[0], days[-1], ', '.join(c for c in (ln.strip().strip('|').split('|')[0].strip() for ln in reg[2:]) if c)))
    else:
        w('The unit plan has no error register table.')
    w(u.CLOSE)
    w('')
    w('%s: for each letter this section meets, a wrong example beside a right one, the day it is shown, and what to do '
      'if many made it (five to ten minutes).' % u.MARK)
    w('')

    # ---- 5. carried and instruments
    w('## 5. What is carried, and instruments')
    w('')
    mats = []
    for r in rows:
        for col in dk.TOOL_COLS:
            for x in (r.get(col) or '').split(';'):
                if x.strip() and x.strip().lower() != 'none':
                    mats.append('- day %s %s: %s' % (r['day'], col, x.strip()))
    f8 = field(text, r'8\.')
    w(u.OPEN)
    L.extend(mats or ['- days.csv names no tools, supplies or safety lines on these days.'])
    if f8:
        w('')
        w('Unit plan field 8 (tools and supplies across the unit):')
        w('')
        L.extend(quote([f8]))
    w(u.CLOSE)
    w('')
    w('%s: what is carried and what happens to it; each key moment with the ideal instrument and the spec judged against '
      'it; what a room with nothing does.' % u.MARK)
    w('')

    # ---- 6. days
    w('## 6. Days')
    w('')
    for r in rows:
        d = int(r['day'])
        w('## Day %d' % d)
        w('')
        w(u.OPEN)
        w('- kind: %s%s. %s.' % (r['kind'], ('; assessment: %s' % r['assess']) if r['assess'] else '',
                                 dk.KIND_MEANS.get(r['kind'], '').capitalize()))
        w('- goal: %s' % u.clean(r['goal']))
        if r['note'].strip():
            w('- note: %s' % u.clean(r['note']))
        cr = dk.credit_rows(course, d)
        if cr and all(c['decision'].strip() == 'ours' for c in cr):
            w('- credit: ours')
        elif cr:
            w('- credit: adapted from %s' % '; '.join('%s, %s (%s)' % (c['source'], c['title'], c['decision']) for c in cr))
        else:
            w('- credit: ours (no base lesson is mapped to this day)')
        here, reserved = dk.day_sources(course, d)
        for s in here:
            w('- source %s (%s): %s; status: %s' % (s['source_id'], s.get('use', ''), s['title'], s.get('status', '')))
        for s, d0 in reserved:
            w('- reserved for day %d, never named today: %s ("%s")' % (d0, s['source_id'], s['title']))
        w(u.CLOSE)
        w('')
        w('%s: one `- **N min. Part.**` line per block of time, adding up to %s minutes (the day skeleton reads these '
          'lines); who holds what is carried; tool by part with mark, job and minutes, or "None"; work by hand; the '
          'day\'s evidence by its number in field 3.' % (u.MARK, mins or 'the day\'s'))
        w('')

    # ---- 7 to 11
    w('## 7. Talk and writing')
    w('')
    w('%s: two or three planned questions with their days; one written task; the look-fors the teacher judges it by.' % u.MARK)
    w('')
    w('## 8. Practice that returns')
    w('')
    rev = [s for s in skills if prog.get(s) and u.grade_num(prog[s]['grade']) is not None and cg is not None and u.grade_num(prog[s]['grade']) < cg]
    if rev:
        w(u.OPEN)
        w('- Earlier-grade skills on these days (review): %s' % ', '.join(rev))
        w(u.CLOSE)
        w('')
    w('%s: what earlier work is practised on each day.%s' % (u.MARK, ' The warm-up; the fluency target, or "none; the '
                                                              'standard sets none".' if subj == 'math' else ''))
    w('')
    w('## 9. Supports and extension')
    w('')
    w('%s: English learners (words and a sentence frame); access; check accommodations; reading load; extension on the '
      'same standard.' % u.MARK)
    w('')
    w('## 10. Two rooms')
    w('')
    last = days[-1] == unit_days[-1] or any(r['assess'] == 'end' for r in rows)
    w('%s: a parent teaching one child, in a few lines%s; one projector.' % (
        u.MARK, ', with one line on the last day of the unit (this section holds it)' if last else ''))
    w('')
    w('## 11. Not in this section, and still to make')
    w('')
    w('%s: what a reader might expect and will not find, and where it lives; what is still to make; any tool that is '
      'spec only; the "from memory" marks this plan relies on.' % u.MARK)
    w('')

    # ---- merged one-section plans: the U fields, sliced
    if merged:
        w('## From the unit plan\'s section fields (U3 to U11)')
        w('')
        w('The unit was one section when its plan was written, so these fields cover all of days %d to %d. Rows keyed by '
          'day are cut to this section; prose is copied whole into every section of the unit. Keep only what belongs to '
          'days %d to %d, move it into the matching field above, and drop the rest.' % (unit_days[0], unit_days[-1], days[0], days[-1]))
        w('')
        for m in re.finditer(r'^## (U(\d+)\.[^\n]*)\n', text, re.M):
            n = m.group(2)
            body = field(text, r'U%s\.' % n)
            if not body:
                continue
            tabs, prose = sliced(body, dayset, prose='all')
            w('### %s' % m.group(1))
            w('')
            w(u.OPEN)
            if tabs:
                L.extend(quote(tabs))
            if prose:
                if tabs:
                    w('>')
                L.extend(quote(['(shared across the unit) ' + prose[0]] + prose[1:]))
            if not tabs and not prose:
                w('(no rows for these days)')
            w(u.CLOSE)
            w('')
    return '\n'.join(L).rstrip() + '\n'


def write(course, section, out=None, force=False):
    d = (Path(out) / course) if out else (u.DOCS / course / SEC_DIR)
    d.mkdir(parents=True, exist_ok=True)
    a, b = section.split('.')
    p = d / ('u%02d-%s.md' % (int(a), b))
    if p.exists() and not force:
        return p, 'kept (exists; --force to rebuild)'
    text = build(course, section)
    p.write_text(text, encoding='utf-8', newline='\n')
    n = text.count('**STOP:**')
    return p, 'written' + (', %d STOP%s before writing' % (n, '' if n == 1 else 's') if n else '')


def all_sections(course, unit=None):
    rows = u.days_rows(course)
    out = []
    for r in rows:
        if r['stretch'].isdigit() and (unit is None or r['stretch'] == str(unit)) and r['unit'] not in out:
            out.append(r['unit'])
    return out


def self_test():
    bad = 0

    def check(name, ok):
        nonlocal bad
        print('%s  %s' % ('ok   ' if ok else 'FAIL ', name))
        bad += 0 if ok else 1

    c = 'social-studies-grade-3'
    secs = all_sections(c, 2)
    a = build(c, secs[0])
    check('deterministic', a == build(c, secs[0]))
    check('all eleven fields', all(('## %d. ' % k) in a for k in range(1, 12)))
    rows = [r for r in u.days_rows(c) if r['unit'] == secs[0]]
    check('one day block per day', all(('## Day %s\n' % r['day']) in a for r in rows) and a.count('\n## Day ') == len(rows))
    check('no em dash', u.EMDASH not in a)
    tot = sum(len([r for r in u.days_rows(c) if r['unit'] == s]) for s in secs)
    check('sections cover the unit', tot == len([r for r in u.days_rows(c) if r['stretch'] == '2']))
    # a unit that was one section until the cuts
    m = next((x for x in ('algebra-i', 'chemistry', 'economics') if (u.DOCS / x / 's02.md').exists()
              and re.search(r'^## U3\.', (u.DOCS / x / 's02.md').read_text(encoding='utf-8'), re.M)), None)
    if m:
        ss = all_sections(m, 2)
        t1, t2 = build(m, ss[0]), build(m, ss[-1])
        check('merged U fields are carried into each section', '### U3.' in t1 and '### U3.' in t2)
        d1 = {int(r['day']) for r in u.days_rows(m) if r['unit'] == ss[0]}
        d2 = {int(r['day']) for r in u.days_rows(m) if r['unit'] == ss[-1]}
        u3 = t1.split('### U3.')[1].split('### U4.')[0]
        check('U3 day rows are cut to the section', all(day_cell(ln[2:]) in d1 for ln in u3.splitlines()
                                                        if ln.startswith('> |') and day_cell(ln[2:]) is not None)
              and not any(day_cell(ln[2:]) in d2 for ln in u3.splitlines() if ln.startswith('> |')))
    try:
        build(c, '2.99')
        check('an unknown section is a data error', False)
    except u.DataError:
        check('an unknown section is a data error', True)
    with tempfile.TemporaryDirectory() as t:
        p, s1 = write(c, secs[0], out=t)
        p.write_text('kept', encoding='utf-8')
        _, s2 = write(c, secs[0], out=t)
        check('never overwrites without --force', s1.startswith('written') and s2.startswith('kept'))
    print('all passed' if not bad else '%d failed' % bad)
    return bad


def main(a):
    if not a or a[0] in ('-h', '--help'):
        raise SystemExit(__doc__)
    if a[0] == '--self-test':
        raise SystemExit(1 if self_test() else 0)
    force = '--force' in a
    out = a[a.index('--out') + 1] if '--out' in a else None
    if '--data-dir' in a:
        u.set_data_dir(a[a.index('--data-dir') + 1])
    pos = [x for i, x in enumerate(a) if not x.startswith('--') and (i == 0 or a[i - 1] not in ('--out', '--data-dir'))]
    if len(pos) < 2:
        raise SystemExit(__doc__)
    course, which = pos[0], pos[1]
    if which == 'all':
        secs = all_sections(course)
    elif which.startswith('u') and which[1:].isdigit():
        secs = all_sections(course, int(which[1:]))
    else:
        secs = [which]
    stopped = 0
    for s in secs:
        p, how = write(course, s, out, force)
        print('%s: %s' % (u.shown_path(p), how))
        stopped += 'STOP' in how
    if stopped:
        print('%d section%s with a STOP: clear it, then rebuild with --force' % (stopped, '' if stopped == 1 else 's'))
        raise SystemExit(1)


if __name__ == '__main__':
    main(sys.argv[1:])

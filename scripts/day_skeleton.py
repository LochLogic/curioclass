"""Day skeletons: one teaching day's mechanical fields filled from data, every judgment field marked (later.csv L31).

    python -X utf8 scripts/day_skeleton.py <course> <day>|u<unit>|all [--force] [--out DIR] [--data-dir DIR]
    python -X utf8 scripts/day_skeleton.py --self-test

A living draft, built 2026-11-15 (findings built in 2026-11-16) ahead of its first real need (Cory: "having a file there longer will help accumulate
improvements"), from the design note docs/pipeline/DAY-SKELETON.md. It is not yet part of any production step: the day
writers start after section plans exist (PRODUCTION-PATH step 7), and the skeleton is proven on social studies first,
then frozen there as the unit skeleton is. Add what each run teaches to the "Lessons" list in DAY-SKELETON.md.

Writes a sidecar, docs/courses/<course>/day-skeletons/d<nnn>.md (or DIR/<course>/d<nnn>.md with --out), never the
day file itself: the day file (docs/courses/LESSON-DAY.md, "Where it lives") is the writer's prose, so the skeleton
can be regenerated without touching it. Never overwrites without --force. Output is deterministic.

Filled from: data/plans/<course>/days.csv (the day, the days before and after), data/plans/frames.csv (minutes),
data/plans/calendar.csv (the unit's school days and weeks), the frame (unit title and question), the progression
(each skill's grade; earlier-grade rows are review, never the day's own), the standards files (own-word lines),
source-map.csv (the base lesson adapted, for the credit line), the unit plan docs/courses/<course>/s<uu>.md (for
leans_on), and parts.csv / items.csv in data/plans/<course>/ where a section plan has been written. Every count it
makes (taught before, Collect once) is the unit skeleton's own function, imported, so the three tools (scope gate,
unit skeleton, day skeleton) never count differently.
"""
import re
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import unit_skeleton as u   # noqa: E402

DAY_DIR = 'day-skeletons'
TOOL_COLS = ('tools', 'supplies', 'safety')
AT_HOME = ('30 to 40 minutes on a teaching day, 40 to 50 on an assessment day, at most 170 words (LESSON-DAY "At home '
           'view"; lesson.py CAP_HOME and HOME_TEACH, HOME_CHECK)')


def frame_meta(course):
    return next((r for r in u.read_csv(u.PLANS / 'frames.csv', u.FRAMES_COLS) if r['course'] == course), {})


def optional_rows(course, name, need):
    p = u.plan_file(course, name)
    return u.read_csv(p, need) if p.exists() else None


def section_block(course, r, day):
    """The `## Day N` block of the day's section plan, docs/courses/<course>/u<uu>-<s>.md, or None."""
    if '.' not in r['unit']:
        return None
    a, b = r['unit'].split('.', 1)
    f = u.DOCS / course / ('u%02d-%s.md' % (int(a), b))
    if not f.exists():
        return None
    m = re.search(r'^## Day %d\b.*?(?=^## |\Z)' % day, f.read_text(encoding='utf-8'), re.M | re.S)
    return m.group(0) if m else None


def section_parts(course, r, day):
    """The day's timed parts from its section plan: the `- **N min. Name.**` lines under `## Day N` (social studies
    probe, 2026-11-15: parts.csv holds the standards' parts, not the day's)."""
    blk = section_block(course, r, day)
    if blk is None:
        return None
    return [(x.group(1), x.group(2)) for x in re.finditer(r'^- \*\*(\d+) min\. (.+?)\.?\*\*', blk, re.M)]


def section_lines(blk, pattern):
    """(name, text) of the section plan parts whose name matches pattern, the text cut to one short line."""
    out = []
    for m in re.finditer(r'^- \*\*\d+ min\. (.+?)\.?\*\*(.*?)(?=^- \*\*\d+ min|^\S|\Z)', blk or '', re.M | re.S):
        if re.search(pattern, m.group(1), re.I):
            t = ' '.join(m.group(2).split())
            out.append((m.group(1).strip(), t if len(t) <= 220 else t[:217].rsplit(' ', 1)[0] + '...'))
    return out


# ---- findings built in from the reads (DAY-SKELETON.md "Findings to build in"; 2026-11-16)

KIND_MEANS = {   # docs/GLOSSARY.md day kinds, as the sample reads asked them printed (math grade 2 unit 3)
    'Understanding': 'meets new content: the goal is taught here, from a hook and a worked example',
    'Fluency': 'practises what earlier days taught until it comes easily; no new content is taught and no writing is drafted, revised or edited',
    'Application': 'applies taught work to a new task or case (an inquiry, a lab, a draft, a revision or edit); nothing is taught as new',
    'Check': 'an assessment day: its items sample only what earlier days taught',
    'Respond': 'acts on an assessment: reteach and revise what the checks showed, from the work students handed in',
}
SCORING = ('end', 'mid', 'course')
ASSESS_DAYS = ('end', 'mid', 'observe', 'course')
CHECKED = re.compile(r'^(checked|read|written|quoted|caption checked)\b', re.I)


def nums(s):
    return [int(x) for x in re.findall(r'\d+', s or '')]


def plan_csv(course, name):
    """Rows of data/plans/<course>/<name>.csv, or [] when the file is not written yet."""
    rows = optional_rows(course, name + '.csv', None)
    return rows or []


def lead_rows(course, unit):
    """Unapplied `lead` rows of data/plans/unit-rejections.csv for the unit: findings that wait on a calendar fix."""
    p = u.PLANS / 'unit-rejections.csv'
    if unit is None or not p.exists():
        return []
    return [x for x in u.read_csv(p, ['course', 'unit', 'lens', 'finding', 'ruling', 'applied'])
            if x['course'] == course and x['ruling'] == 'lead' and not x['applied'].strip()
            and x['unit'].strip().lstrip('0') == str(unit)]


def scored_day_check(course, allrows, unit):
    """items.csv end and mid items against days.csv (sample read, math grade 7 unit 5): every scored item's day is an
    assessment day, and every days.csv end day of the unit holds end items. A disagreement is a data error."""
    items = [i for i in plan_csv(course, 'items') if i.get('stretch', '').strip() == str(unit)]
    if not items:
        return
    byday = {int(x['day']): x for x in allrows}
    path = u.shown_path(u.plan_file(course, 'items.csv'))
    for i in items:
        if i.get('check') in ('end', 'mid') and i.get('day', '').strip().isdigit():
            d = int(i['day'])
            if d not in byday or byday[d]['assess'] not in ASSESS_DAYS:
                raise u.DataError('%s: item %s is a %s item on day %d, but days.csv gives day %d no assessment (assess "%s"); '
                                  'fix the section plan or days.csv' % (path, i['item_id'], i['check'], d, d,
                                                                        byday.get(d, {}).get('assess', 'no such day')))
    ends = {int(i['day']) for i in items if i.get('check') == 'end' and i.get('day', '').strip().isdigit()}
    if ends:
        for d, x in byday.items():
            if x['stretch'] == str(unit) and x['assess'] == 'end' and d not in ends:
                raise u.DataError('%s: days.csv makes day %d unit %d\'s end-of-unit assessment, but no end item is on it '
                                  '(end items are on day %s)' % (path, d, unit, ', '.join(map(str, sorted(ends)))))


def scored_work(course, allrows, r, day):
    """Lines and stops for work made on earlier days and scored today (both probes; the unit loop's known-fault test):
    the day it was made and the days of its written feedback, from materials.csv and handbacks.csv."""
    lines, stops = [], []
    if r['assess'] not in SCORING:
        return lines, stops
    hand = plan_csv(course, 'handbacks')
    first = {}
    for c in u.split_list(r['codes']):
        t = u.taught_before(allrows, c.lstrip('~'), day)
        if t:
            first[c] = min(t)
    for m in plan_csv(course, 'materials'):
        # materials.csv `per` is copies (one per student or one for the class), not authorship: a sheet made and used
        # today is a handout. Scored work is a student's copy carried in from an earlier day (first real run, 2026-11-16)
        used, made = nums(m.get('used_days')), nums(m.get('made_day'))
        if day not in used or not made or m.get('per', '').strip() == 'class' or made[0] >= day:
            continue
        md = made[0]
        fb = [h for h in hand if nums(h.get('from_day')) and md <= nums(h['from_day'])[0] < day
              and nums(h.get('to_day')) and nums(h['to_day'])[0] <= day]
        back = sorted({nums(h['to_day'])[0] for h in fb})
        lines.append('- Scored work: %s, made on day %d; written feedback handed back on %s (handbacks.csv)' % (
            m['material'], md, ('day ' if len(back) == 1 else 'days ') + ', '.join(map(str, back)) if back
            else 'NO day between the day it was made and today'))
        for c, f in first.items():
            if md == f:
                stops.append('%s is made on day %d, the first day %s is taught; scored work comes after teaching '
                             '(UNIT-PLAN field 5)' % (m['material'], md, c))
        if not fb:
            stops.append('%s has no written feedback day before it is scored on day %d (handbacks.csv)' % (m['material'], day))
    return lines, stops


def day_sources(course, day):
    """sources.csv rows for the day (the `days` cell), and the reserved sources the day must not name yet."""
    here, later = [], []
    for s in plan_csv(course, 'sources'):
        sd = nums(s.get('days'))
        if day in sd:
            here.append(s)
        elif s.get('use') == 'reserved' and sd and day < min(sd):
            later.append((s, min(sd)))
    return here, later


def unit_field(course, unit, n):
    """The text of field n of the unit plan s<uu>.md, without its heading, or ''."""
    p = u.DOCS / course / ('s%02d.md' % unit) if unit else None
    if not p or not p.exists():
        return ''
    m = re.search(r'^## %d\..*?\n(.*?)(?=^## |\Z)' % n, p.read_text(encoding='utf-8'), re.M | re.S)
    return re.sub(r'<!-- /?skel -->', '', m.group(1)).strip() if m else ''


def credit_rows(course, day):
    """Source-map rows whose `days` cell includes this day (sequence.py map_days reads the same cell)."""
    out = []
    for r in u.source_map(course) if u.plan_file(course, 'source-map.csv').exists() else []:
        if r['decision'].strip() == 'cut':
            continue
        nums = set()
        for part in re.split(r'[;,\s]+', re.sub(r'\s*(-|to)\s*', r'\1', r['days'].strip())):
            m = re.fullmatch(r'(\d+)(?:(?:-|to)(\d+))?', part)
            if m:
                a, b = int(m.group(1)), int(m.group(2) or m.group(1))
                nums.update(range(a, b + 1))
        if day in nums:
            out.append(r)
    return out


def skill_lines(r, prog, cg):
    """One line per skill on the day: own (this grade) or earlier-grade review (never treated as the day's own)."""
    out = []
    for s in u.split_list(r['skills']):
        p = prog.get(s)
        if p is None:
            out.append('- %s: not a row of the progression (check the id)' % s)
            continue
        g = u.grade_num(p['grade'])
        if g is not None and cg is not None and g < cg:
            how = 'readiness check' if r['assess'] == 'readiness' else 'review (retrieval)'
            out.append('- %s (grade %s): earlier-grade row, %s here, not taught as new' % (s, p['grade'], how))
        else:
            out.append('- %s (grade %s): taught or practised here' % (s, p['grade']))
    return out


def code_lines(r):
    out = []
    for c in u.split_list(r['codes']):
        begun = c.startswith('~') and len(c) > 1
        txt = u.std_line(c[1:] if begun else c)
        lead = '(begun here, owned later; sample only what this day teaches) ' if begun else ''
        out.append('- **%s:** %s%s' % (c, lead, u.clean(txt) if txt else '(no own-word line on file: write one from the standard)'))
    return out


def build(course, day):
    subj = u.subject_of(course)
    if subj is None:
        raise u.DataError('%s is not a course in data/plans/frames.csv' % course)
    u.set_subject(subj)
    allrows = u.days_rows(course)
    byday = {int(r['day']): r for r in allrows}
    if day not in byday:
        raise u.DataError('%s has no day %d in days.csv' % (course, day))
    r = byday[day]
    meta = frame_meta(course)
    cg = u.grade_num(meta.get('grade'))
    prog = u.progression()
    unit = int(r['stretch']) if r['stretch'].isdigit() else None
    if unit is not None:
        scored_day_check(course, allrows, unit)
    # ---- what stops or warns before a writer starts (findings built in, 2026-11-16)
    stops, warns = [], []
    if subj == 'ela' and unit is not None:
        for t in u.ela_texts(course, unit):
            if 'to write' in (t.get('status') or '').lower():
                stops.append('core text %s (%s), "%s", is still to write: Curio Class writes it before any day of this '
                             'unit is written, never the day writer (later.csv L58)' % (t['text_id'], t['use'], t['title']))
    if re.search(r'\bto write\b', r['note'], re.I):
        warns.append('the days.csv note names something "to write": if it is a text or passage the day reads, it is a '
                     'blocker, not a hole for the day writer')
    for x in lead_rows(course, unit):
        warns.append('open calendar finding (unit-rejections.csv, %s lens, not yet applied): %s' % (x['lens'], u.clean(x['finding'])))
    work_lines, work_stops = scored_work(course, allrows, r, day)
    stops += work_stops
    srcs, reserved = day_sources(course, day)
    for s in srcs:   # one STOP a source: a sheet passage needs a link (unless we make it) and a checked status
        st_ = s.get('status', '').strip()
        made_here = re.match(r'(to make|written)\b', st_, re.I)
        why = []
        if not CHECKED.match(st_):
            why.append('status "%s", not checked' % st_)
        if not s.get('url', '').strip() and not made_here:
            why.append('no link')
        if why:
            stops.append('source %s ("%s"): %s (sources.csv; checked once for the course at plan data, '
                         'plan-data.md step 4, never by the day writer)' % (s['source_id'], s['title'], '; '.join(why)))
    items_all = plan_csv(course, 'items')
    day_items = [i for i in items_all if i.get('day', '').strip() == str(day)]
    for i in day_items:
        if not (i.get('answer') or '').strip() and not (i.get('compute') or '').strip() and not (i.get('samples') or '').strip():
            stops.append('item %s has no key, computed answer or sample answers in items.csv (every rotated form '
                         'needs its own)' % i['item_id'])
    L = []
    w = L.append
    title = '(course-level check)'
    question = ''
    if unit is not None:
        cells = u.frame_unit(course, unit)
        if cells:
            title, question = u.split_title(re.sub(r'\*\*', '', cells[1]))
    w('# Day %d skeleton: %s, %s' % (day, meta.get('title', course), 'unit %d' % unit if unit else 'course-level day'))
    w('')
    w('A sidecar for the day writer (scripts/day_skeleton.py, a living draft). Lines between the markers are copies of '
      'data: change the data, not these lines. Every %s is the writer\'s.' % u.MARK)
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
        if stops:
            w('The day is not written until every STOP is cleared in the data and this skeleton is rebuilt (--force).')
            w('')
    # ---- the header block (LESSON-DAY "Where it lives")
    w('## Header')
    w('')
    w(u.OPEN)
    w('- day: %d' % day)
    w('- course: %s' % course)
    w('- unit: %s%s' % (r['stretch'], (' (section %s): %s' % (r['unit'], title)) if unit else ''))
    if question:
        w('- compelling question (frame): "%s"' % u.clean(question))
    w('- kind: %s%s' % (r['kind'], ('; assessment: %s' % r['assess']) if r['assess'] else ''))
    if r['kind'] in KIND_MEANS:
        w('- what the kind means: %s (%s). Keep it this kind: a teaching day is never quietly made an '
          'assessment, and a Fluency day teaches nothing new' % (r['kind'], KIND_MEANS[r['kind']]))
    w('- version: draft, not yet taught')
    lo, hi = meta.get('minutes_min', ''), meta.get('minutes_max', '')
    w('- minutes: %s' % ((lo if lo == hi else '%s to %s' % (lo, hi)) if lo else '(frames.csv gives none)'))
    if unit is not None:
        for c in u.calendar_rows(course, unit):
            w('- calendar: unit days %s to %s, school days %s to %s, weeks %s to %s' % (
                c['first_day'], c['last_day'], c['first_school_day'], c['last_school_day'], c['first_week'], c['last_week']))
    if r.get('school_day', '').strip():
        w('- school day (days.csv): %s' % r['school_day'])
    # tools, supplies and safety cells are ;-separated (items may hold commas); a safety cell of "none" is no item
    mats = [(col, items) for col in TOOL_COLS
            for items in [[x.strip() for x in (r.get(col) or '').split(';') if x.strip() and x.strip().lower() != 'none']] if items]
    for col, items in mats:
        w('- %s: %s' % (col, '; '.join(items)))
    plan = u.DOCS / course / ('s%02d.md' % unit) if unit else None
    lean = []
    if plan:
        lean.append(('' if plan.exists() else 'when it exists: ') + 'docs/courses/%s/%s' % (course, plan.name))
    if unit and '.' in r['unit']:
        sp = 'docs/courses/%s/u%02d-%s.md' % (course, unit, r['unit'].split('.', 1)[1])
        lean.append(sp if (u.ROOT / sp).exists() else 'when it exists: ' + sp)
        op = 'courses/%s/u%02d-%s/opener.md' % (course, unit, r['unit'].split('.', 1)[1])
        lean.append(op if (u.ROOT / op).exists() else 'when it exists: the section %s opener (%s)' % (r['unit'], op))
    else:
        lean.append('when it exists: the section %s opener' % r['unit'] if unit else 'the course check set (frame)')
    w('- leans_on: %s' % '; '.join(lean))
    cr = credit_rows(course, day)
    if cr and all(c['decision'].strip() == 'ours' for c in cr):
        w('- credit: ours (the header says exactly "ours"; source-map: %s)' % '; '.join(c['title'] for c in cr))
    elif cr:
        w('- credit: adapted from %s' % '; '.join('%s, %s (%s)' % (c['source'], c['title'], c['decision']) for c in cr))
    else:
        w('- credit: ours (no base lesson is adapted on this day; the header says exactly "ours")')
    w(u.CLOSE)
    w('')
    # ---- the day as the scope sets it
    w('## The day as the scope and sequence sets it')
    w('')
    w(u.OPEN)
    w('- **Goal:** %s' % u.clean(r['goal']))
    if r['note'].strip():
        w('- **Note:** %s' % u.clean(r['note']))
    w('')
    w('**Skills:**')
    w('')
    L.extend(skill_lines(r, prog, cg) or ['- (none listed)'])
    w('')
    w('**Codes, in our words where the standards file has them:**')
    w('')
    L.extend(code_lines(r) or ['- (none listed)'])
    w(u.CLOSE)
    w('')
    w('%s: the goal in student words (one sentence a student could repeat at the door).' % u.MARK)
    w('')
    # ---- supply and safety limits (sample read, science grade 7 unit 2)
    f8 = unit_field(course, unit, 8)
    if f8 and (mats or subj == 'science' or re.search(r'\b(lab|investigat\w*|build|experiment|model)\b', r['goal'] + ' ' + r['note'], re.I)):
        w('## Supplies and safety limits (unit plan field 8)')
        w('')
        w(u.OPEN)
        L.extend('> ' + ln if ln.strip() else '>' for ln in f8.splitlines())
        w(u.CLOSE)
        w('')
        w('Every investigation, build or task stays inside these limits and their cost line. A task the limits forbid is a '
          'data error to report, never a writer\'s guess.')
        w('')
    # ---- assessment days
    if r['assess'] in ('end', 'mid', 'observe', 'course', 'readiness'):
        w('## Assessment')
        w('')
        w(u.OPEN)
        for c in u.split_list(r['codes']):
            base = c.lstrip('~')
            t = u.taught_before(allrows, base, day, same_day=r['assess'] == 'observe')
            w('- %s: %s' % (c, ('taught on days %s' % ', '.join(map(str, t[-6:]))) if t else
                             'NOT taught on any earlier day: teach it first or do not sample it'))
        if unit is not None:
            for other, ok in u.evidence_pairs(allrows, unit, day):
                w('- Collect once: day %d also gathers child-by-child evidence on a shared code; %s' % (
                    other, 'the later day reuses the record' if ok else 'the later day must reuse that record or sample a new case'))
        L.extend(work_lines)
        if unit is not None and r['assess'] == 'end':
            ends = [i for i in items_all if i.get('stretch', '').strip() == str(unit) and i.get('check') == 'end']
            if any(i.get('judged') == 'teacher' and '|' in (i.get('steps') or '') for i in ends):
                w('- Record sheet: teacher-judged end items with several look-fors; the header carries `endlooks: 012` '
                  'so each look-for gets its own column, scored 2, 1 or 0')
        w(u.CLOSE)
        if r['assess'] in ('end', 'mid', 'course', 'readiness'):
            w('')
            w('A cold check\'s text or case is new: it may not restate a taught text\'s central idea or reuse its key '
              'teaching words (probe 2; sample read, ELA grade 8 unit 3).')
        w('')
        w('%s: what each item samples (the part of each code), and the record sheet line. Checks claim only what '
          'they sample (sequence-write.md rule 2).' % u.MARK)
        w('')
    # ---- the teacher page, in LESSON-DAY order
    w('## The teacher page (docs/courses/LESSON-DAY.md order)')
    w('')
    w('1. **The header:** generated from the block above.')
    w('2. **Before class:** %s: set-up only, 80 words at most.%s' % (
        u.MARK, (' Lay out: ' + '; '.join(i for c, items in mats if c != 'safety' for i in items) + '.') if mats else ''))
    mine = section_parts(course, r, day)
    if mine:
        tot = sum(int(n) for n, _ in mine)
        ok = not lo or int(lo) <= tot <= int(hi or lo)
        w('3. **The day:** one part per line of the section plan; %d minutes%s:' % (
            tot, '' if ok else ', NOT the frame\'s %s: fix the section plan' % lo))
        for n, name in mine:
            w('   - `#### %s min. %s`' % (n, name.strip()))
        blk = section_block(course, r, day)
        taught = section_lines(blk, r'hook|teaching first|worked example|model')
        if section_lines(blk, r'exit') and taught:
            w('   - Beside the exit: today\'s %s. The exit is a new case, not this one in new numbers (probe 2).' % '; '.join(
                '%s: %s' % (n, t) for n, t in taught))
    else:
        w('3. **The day:** %s: one `#### N min. Part` heading under `### The day` per block of time, adding up to %s minutes. No section '
          'plan is on file yet, so the parts are the writer\'s.' % (u.MARK, lo or 'the day\'s'))
    if any(c == 'tools' for c, _ in mats) or re.search(r'\b(device|projector|tool|simulation|applet)\b', r['note'], re.I):
        w('4. **Other rooms:** %s: the paper path when there are no devices, no printer, one projector; only what differs.' % u.MARK)
    else:
        w('4. **Other rooms:** none needed unless the writer adds a device or a print; then the paper path.')
    w('5. **At home:** %s: the same day for one parent and one child; %s.' % (u.MARK, AT_HOME))
    w('6. **Shorter or longer:** %s: what to cut without making the work easier, and the extension.' % u.MARK)
    w('7. **Words and supports:** %s: key words (with Word Wall card ids only where the topic has cards; never a line '
      'saying none are supplied), sentence frames, access notes.' % u.MARK)
    nxt = byday.get(day + 1)
    w('8. **Tomorrow:** %s: what the exit tells the teacher and what changes next day.%s' % (
        u.MARK, (' Next day (%d, %s): %s' % (day + 1, nxt['kind'], u.clean(nxt['goal']))) if nxt else ' (the last day of the course)'))
    w('9. **Credit:** from the header.')
    if any(c == 'safety' for c, _ in mats):
        w('')
        w('**Safety (days.csv):** %s. %s: the safety lines on the teacher page and the student page.' % (
            '; '.join(dict(mats)['safety']), u.MARK))
    w('')
    w('No timer is shown to students unless it has a grounded purpose (a pace cue, a movement game, classroom '
      'management; LESSON-DAY rule 7).')
    w('')
    # ---- hand-backs (science and math probe, 2026-11-18: day 5 handed day 6 repairs it had no slot for)
    hb_in = [h for h in plan_csv(course, 'handbacks') if nums(h.get('to_day')) == [day]]
    hb_out = [h for h in plan_csv(course, 'handbacks') if nums(h.get('from_day')) == [day]]
    if hb_in or hb_out:
        w('## Hand-backs')
        w('')
        w('Rows of handbacks.csv. Incoming work lands in a named part of today; that part must hold its minutes '
          '(plan.py checks the section plan). Outgoing work is made today and handed back later.')
        w('')
        w(u.OPEN)
        parts = section_parts(course, r, day) or []
        for h in hb_in:
            where = h.get('where', '').strip()
            hit = [(mn, nm) for mn, nm in parts if where and where.lower() in nm.lower()]
            slot = ('the %s-minute part "%s"' % hit[0]) if hit else 'NO PART NAMED "%s" in the section plan' % where
            w('- In from day %s: %s, %s minutes, into %s%s%s' % (
                h.get('from_day', ''), h.get('what', ''), h.get('minutes', '') or '?', slot,
                ('; error ' + h['error']) if h.get('error', '').strip() else '',
                ('; ' + u.clean(h['note'])) if h.get('note', '').strip() else ''))
        for h in hb_out:
            nb = byday.get((nums(h.get('to_day')) or [0])[0])
            w('- Out to day %s: %s, %s minutes into its "%s" part%s' % (
                h.get('to_day', ''), h.get('what', ''), h.get('minutes', '') or '?', h.get('where', ''),
                (' (%s)' % u.clean(nb['goal'])) if nb else ''))
        w(u.CLOSE)
        w('')
    # ---- questions
    w('## Questions')
    w('')
    if day_items:
        w('Rows already in items.csv for this day, each with its key and samples, so the answer-key read and the writer '
          'see the same thing (probe 2; later.csv L56):')
        w('')
        w(u.OPEN)
        for i in day_items:
            key = (i.get('answer') or '').strip() or ('computed: %s' % i['compute'] if (i.get('compute') or '').strip() else 'NONE')
            smp = (i.get('samples') or '').strip()
            w('- [[%s]] (%s%s): key: %s%s' % (i['item_id'], i.get('check', ''), ', judged by ' + i['judged'] if i.get('judged') else '',
                                             u.clean(key), ('; samples: ' + u.clean(smp)) if smp else ''))
        w(u.CLOSE)
    else:
        w('%s: every question the student answers is a row in data/plans/%s/items.csv with a computed key '
          '(LESSON-DAY rule 1); none exists for this day yet.' % (u.MARK, course))
    w('')
    if srcs or reserved:
        w('## Sources')
        w('')
        w(u.OPEN)
        for s in srcs:
            w('- %s (%s): %s; %s; rights: %s; status: %s' % (s['source_id'], s.get('use', ''), s['title'],
                                                             s.get('url', '') or 'no link', s.get('rights', ''), s.get('status', '')))
        for s, d0 in reserved:
            wm = re.search(r'watch:\s*([^.;"]+(?:;[^.;"]+)*)', s.get('note', ''))
            w('- Reserved for day %d, never named today: %s ("%s")%s' % (d0, s['source_id'], s['title'],
                                                                       ('; nor the words ' + wm.group(1).strip()) if wm else ''))
        w(u.CLOSE)
        w('')
    # ---- the checks the written day must pass (probe 2 check lines, fix-u03-4; lesson.py's rules, printed first)
    hi_min = int(hi or lo or 60)
    per = 15 * hi_min
    carries = any(nums(h.get('to_day')) == [day] and h.get('where', '').strip().lower() == 'assessment'
                  for h in plan_csv(course, 'handbacks'))
    cap = per if (r['kind'] != 'Check' or carries) else 500
    w('## Checks the written day must pass')
    w('')
    w('- Teacher prose at most %d words (15 a minute of a %d-minute day%s); At home apart, at most 170.' % (
        cap, hi_min, '' if r['kind'] != 'Check' else (', an assessment day that scores earlier work keeps the teaching cap'
                                                     if carries else ', an assessment day: 500')))
    w('- Glosses only for words the day uses.')
    if reserved:
        w('- No reserved source, nor a word its note watches for, is named before its day (list above).')
    if r['kind'] == 'Respond':
        w('- The student page says "Scored from the work you handed in".')
    if r['assess'] == 'end':
        w('- Each rotated form of an item has its own key.')
    w('')
    w('## The student page')
    w('')
    w('%s: two sides at most (large print may run longer), named by item id, never a typed key.' % u.MARK)
    w('')
    return '\n'.join(L)


def write(course, day, out=None, force=False):
    d = (Path(out) / course) if out else (u.DOCS / course / DAY_DIR)
    d.mkdir(parents=True, exist_ok=True)
    p = d / ('d%03d.md' % day)
    if p.exists() and not force:
        return p, 'kept (exists; --force to rebuild)'
    text = build(course, day)
    p.write_text(text, encoding='utf-8', newline='\n')
    n = text.count('**STOP:**')
    return p, 'written' + (', %d STOP%s before writing' % (n, '' if n == 1 else 's') if n else '')


def self_test():
    bad = 0

    def check(name, ok):
        nonlocal bad
        print('%s  %s' % ('ok   ' if ok else 'FAIL ', name))
        bad += 0 if ok else 1

    c = 'social-studies-grade-3'
    rows = u.days_rows(c)
    a = build(c, 5)
    check('deterministic', a == build(c, 5))
    check('header has the fixed fields', all(k in a for k in ('- day: 5', '- course: ' + c, '- version: draft', '- minutes:', '- leans_on:', '- credit:')))
    check('teacher page lists all nine parts', all(('%d. **' % i) in a for i in range(1, 10)))
    last = max(int(r['day']) for r in rows)
    check('last day names no next day', '(the last day of the course)' in build(c, last))
    ad = next((int(r['day']) for r in rows if r['assess'] in ('end', 'mid')), None)
    check('an assessment day gets the Assessment section', ad is None or '## Assessment' in build(c, ad))
    with tempfile.TemporaryDirectory() as t:
        p, s1 = write(c, 5, out=t)
        p.write_text('kept', encoding='utf-8')
        _, s2 = write(c, 5, out=t)
        check('never overwrites without --force', s1 == 'written' and s2.startswith('kept') and p.read_text(encoding='utf-8') == 'kept')
    sci = 'science-grade-6'
    t6 = build(sci, 1)
    check('a begun (~) code keeps its mark and finds its statement', '**~MS-PS4-2:** (begun here' in t6 and 'no own-word line' not in t6.split('**~MS-PS4-2:**')[1].split('\n')[0])
    m5 = next((int(r['day']) for r in u.days_rows('math-grade-5') if r['stretch'] == '2'), 1)
    t5 = build('math-grade-5', m5)
    check('earlier-grade skills are review, not the day\'s own', all('taught or practised' not in ln for ln in t5.splitlines() if '(grade 4)' in ln))
    check('the day kind is explained', '- what the kind means: ' in a)
    # findings built in 2026-11-16, on a copy of the social studies probe section's data with planted faults
    import csv as _csv
    import shutil
    w1 = 'world-history-i'
    with tempfile.TemporaryDirectory() as t:
        shutil.copytree(u.PLANS / w1, Path(t) / w1)
        u.set_data_dir(t)
        try:
            base = build(w1, 45)
            check('carried scored work prints its made day and feedback days',
                  re.search(r'Scored work: .+, made on day \d+; written feedback handed back on days? \d', base) is not None)
            check('the end items print their keys', '(end, judged by teacher): key: ' in base)

            def rewrite(name, fn):
                p = Path(t) / w1 / name
                with open(p, encoding='utf-8', newline='') as f:
                    rows = list(_csv.DictReader(f))
                head = list(rows[0].keys())
                rows = fn(rows)
                with open(p, 'w', encoding='utf-8', newline='') as f:
                    wr = _csv.DictWriter(f, head, lineterminator='\n')
                    wr.writeheader()
                    wr.writerows(rows)
            rewrite('handbacks.csv', lambda rows: [x for x in rows if not (42 <= int(x['from_day']) < 45)])
            check('scored work with no feedback day is a STOP', '**STOP:**' in build(w1, 45) and 'no written feedback day' in build(w1, 45))
            rewrite('sources.csv', lambda rows: [dict(x, status='to cut and check') if x['days'].strip() == '44' else x for x in rows])
            check('an unchecked source on the day is a STOP', 'not checked' in build(w1, 44))
            rewrite('items.csv', lambda rows: [dict(x, day='43') if x['item_id'] == 's03-A4' else x for x in rows])
            try:
                build(w1, 44)
                check('an end item on a teaching day is a data error', False)
            except u.DataError as e:
                check('an end item on a teaching day is a data error', 's03-A4' in str(e))
        finally:
            u.set_data_dir(None)
    # hand-backs listed with the receiving part (science and math probe, 2026-11-18)
    h6, h5 = build('algebra-ii', 6), build('algebra-ii', 5)
    check('incoming hand-backs name the receiving part and its minutes',
          '## Hand-backs' in h6 and re.search(r'In from day 5: .+ into the \d+-minute part "', h6) is not None)
    check('outgoing hand-backs are listed on the day that makes them', 'Out to day 6:' in h5)
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
        days = [int(r['day']) for r in u.days_rows(course)]
    elif which.startswith('u') and which[1:].isdigit():
        days = [int(r['day']) for r in u.days_rows(course) if r['stretch'] == which[1:]]
    elif which.isdigit():
        days = [int(which)]
    else:
        raise SystemExit('day must be a number, u<unit> or all')
    stopped = 0
    for d in days:
        p, how = write(course, d, out, force)
        print('%s: %s' % (u.shown_path(p), how))
        stopped += 'STOP' in how
    if stopped:
        print('%d day%s with a STOP: clear it in the data, then rebuild with --force' % (stopped, '' if stopped == 1 else 's'))
        raise SystemExit(1)


if __name__ == '__main__':
    main(sys.argv[1:])

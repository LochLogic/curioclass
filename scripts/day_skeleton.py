"""Day skeletons: one teaching day's mechanical fields filled from data, every judgment field marked (later.csv L31).

    python -X utf8 scripts/day_skeleton.py <course> <day>|u<unit>|all [--force] [--out DIR] [--data-dir DIR]
    python -X utf8 scripts/day_skeleton.py --self-test

A living draft, built 2026-11-15 ahead of its first real need (Cory: "having a file there longer will help accumulate
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
    lean.append('when it exists: the section %s opener' % r['unit'] if unit else 'the course check set (frame)')
    w('- leans_on: %s' % '; '.join(lean))
    cr = credit_rows(course, day)
    if cr:
        w('- credit: adapted from %s' % '; '.join('%s, %s (%s)' % (c['source'], c['title'], c['decision']) for c in cr))
    else:
        w('- credit: none (no base lesson is adapted on this day)')
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
        w(u.CLOSE)
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
    parts = optional_rows(course, 'parts.csv', ['day'])
    mine = [p for p in parts or [] if p['day'].strip() == str(day)]
    if mine:
        w('3. **The day:** one part per row of the section plan (parts.csv); the minutes must add up to the day:')
        for p in mine:
            w('   - `#### %s min. %s`' % (p.get('minutes', '?'), p.get('part', p.get('title', '')).strip()))
    else:
        w('3. **The day:** %s: one `#### N min. Part` heading under `### The day` per block of time, adding up to %s minutes. No section '
          'plan (parts.csv) is on file yet, so the parts are the writer\'s.' % (u.MARK, lo or 'the day\'s'))
    if any(c == 'tools' for c, _ in mats) or re.search(r'\b(device|projector|tool|simulation|applet)\b', r['note'], re.I):
        w('4. **Other rooms:** %s: the paper path when there are no devices, no printer, one projector; only what differs.' % u.MARK)
    else:
        w('4. **Other rooms:** none needed unless the writer adds a device or a print; then the paper path.')
    w('5. **At home:** %s: the same day for one parent and one child; %s.' % (u.MARK, AT_HOME))
    w('6. **Shorter or longer:** %s: what to cut without making the work easier, and the extension.' % u.MARK)
    w('7. **Words and supports:** %s: key words with their Word Wall cards, sentence frames, access notes.' % u.MARK)
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
    # ---- questions
    w('## Questions')
    w('')
    items = optional_rows(course, 'items.csv', ['id'])
    ids = [i['id'] for i in items or [] if i.get('day', '').strip() == str(day)]
    if ids:
        w('Rows already in items.csv for this day: %s.' % ', '.join('[[%s]]' % i for i in ids))
    else:
        w('%s: every question the student answers is a row in data/plans/%s/items.csv with a computed key '
          '(LESSON-DAY rule 1); none exists for this day yet.' % (u.MARK, course))
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
    p.write_text(build(course, day), encoding='utf-8', newline='\n')
    return p, 'written'


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
    for d in days:
        p, how = write(course, d, out, force)
        print('%s: %s' % (u.shown_path(p), how))


if __name__ == '__main__':
    main(sys.argv[1:])

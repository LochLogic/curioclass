"""Course-run job generator (docs/COURSE-RUN.md stages 5 and 6; the kit is docs/pipeline/kit/).

    python -X utf8 scripts/coursegen.py <subject> <course> [<course> ...] --out <dir> [--probe] [--texts]
                                        [--read-units N] [--day-min 4] [--day-max 6]
    python -X utf8 scripts/coursegen.py sweep <subject> <course> --out <dir> --made-at <stage> --found-at <stage>
                                        --fault "<text>" --test "<text>" [--found-in <where>] [--tool <text>]
                                        [--scope <text>] [--tag <word>]

<subject> is ela, social-studies, math or science. Courses are given in grade order. Per course the queue is, in
COURSE-RUN order: section plans unit by unit, a fresh plan read, one plan fix, then per unit plan data, the answer-key
read and the days (4 to 6 days a job, each job preceded by its ledger gate line, course-level check days in day
order), then the grade sample (two readers), the cleanup, and a retool stop. With --probe, the first course's unit 1
runs all the way through days before the other units' section plans, then a probe retool stop. After the last grade:
the cross-grade continuity read and one fix job per grade (from the second on). Writes one job file per job, numbered,
plus queue.txt (one line per job; GATE and LEAD lines are for the lead). Every job file starts with the KIT-VERSION
line. Placeholders in the templates are upper-case words in braces ({UNIT}, {COURSE}, {DATE}); a single pass fills
them, so no token can sit inside another word, and an unknown token is an error. {DATE} is today's date at generation.

Day grouping and section lists come from data/plans/<course>/days.csv (columns stretch, unit, day). A course missing a
stage's input is reported by stage and skipped (and every course after it); the queue is written for the courses
before it. Exit code 0 when every course was generated, 2 when one was not."""
import argparse
import csv
import datetime
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KIT = ROOT / 'docs' / 'pipeline' / 'kit'
PLANS = ROOT / 'data' / 'plans'
DOCS = ROOT / 'docs' / 'courses'
TOKEN = re.compile(r'\{([A-Z][A-Z0-9_]*)\}')
SUBJECTS = {  # slug: (course prefix, words)
    'ela': ('english-language-arts', 'English language arts'),
    'social-studies': ('social-studies', 'social studies'),
    'math': ('math', 'math'),
    'science': ('science', 'science'),
}
SECTION_SPLIT = 5  # a unit with more sections than this is cut in two halves for section and data jobs
PLANGATE = ("python -X utf8 scripts/plan.py check 2>&1 | awk '/^COURSE: [0-9]+ items/{on=1;print;next} "
            "on && /^[a-z0-9-]+: [0-9]+ items/{on=0} on || /COURSE/'")
LESSONGATE = 'python -X utf8 scripts/lesson.py check 2>&1 | grep "courses/COURSE/"'
STAGE_GATES = {'unit plan': 'unitplan', 'section plan': 'unitplan', 'data': 'plan', 'days': 'lesson'}


def read(p):
    return Path(p).read_text(encoding='utf-8')


def kit_version():
    m = re.search(r'^KIT-VERSION:\s*(.+?)\s*$', read(KIT / 'README.md'), re.M)
    if not m:
        sys.exit('docs/pipeline/kit/README.md has no KIT-VERSION line')
    return m.group(1)


def fill(text, mp, where):
    """One pass over upper-case brace tokens; an unknown token is an error."""
    def rep(m):
        k = m.group(1)
        if k not in mp:
            raise KeyError('%s: unknown token {%s}' % (where, k))
        return mp[k]
    return TOKEN.sub(rep, text)


def frame_row(course):
    """The course's row of data/plans/frames.csv (subject, grade), or None."""
    with open(ROOT / 'data' / 'plans' / 'frames.csv', encoding='utf-8', newline='') as f:
        for r in csv.DictReader(f):
            if r['course'] == course:
                return r
    return None


def grade_token(course):
    """'k' or the grade number, from frames.csv (so a course named without its grade, such as
    world-geography-and-ancient-civilizations-i or algebra-i, still finds its grade note)."""
    r = frame_row(course)
    if r and r['grade'].strip():
        g = r['grade'].strip().lower()
        return 'k' if g in ('k', 'kindergarten') else g
    if course.endswith('kindergarten'):
        return 'k'
    m = re.search(r'grade-(\d+)$', course)
    return m.group(1) if m else None


def sections(rows):
    """{unit number: [(section id like '1.2', [days])]} from days.csv rows."""
    secs = {}
    for r in rows:
        if r['stretch'].isdigit() and r['unit'] and '.' in r['unit']:
            secs.setdefault(int(r['stretch']), {}).setdefault(r['unit'], []).append(int(r['day']))
    return {u: sorted(v.items(), key=lambda x: [int(y) for y in x[0].split('.')]) for u, v in secs.items()}


def sname(uu, s):
    return 'u%s-%s' % (uu, s.split('.')[1])


def halves(ss):
    return [ss] if len(ss) <= SECTION_SPLIT else [ss[:(len(ss) + 1) // 2], ss[(len(ss) + 1) // 2:]]


def day_batches(ss, lo, hi):
    """Group consecutive sections of one unit into jobs of lo to hi days where the sections allow."""
    groups, cur, n = [], [], 0
    for s, ds in ss:
        if cur and n + len(ds) > hi:
            groups.append(cur)
            cur, n = [], 0
        cur.append((s, ds))
        n += len(ds)
    if cur:
        groups.append(cur)
    cnt = lambda g: sum(len(d) for _, d in g)
    if len(groups) > 1 and cnt(groups[-1]) < lo and cnt(groups[-1]) + cnt(groups[-2]) <= hi + 1:
        last = groups.pop()
        groups[-1] = groups[-1] + last
    return groups


def runs(days, cap=6):
    out, cur = [], []
    for d in sorted(days):
        if cur and (d != cur[-1] + 1 or len(cur) >= cap):
            out.append(cur)
            cur = []
        cur.append(d)
    if cur:
        out.append(cur)
    return out


def safe(s):
    return re.sub(r'[^a-z0-9+-]+', '-', s.lower()).strip('-')


class Queue:
    def __init__(self, out, subj, version, date):
        self.out, self.subj, self.version, self.date = out, subj, version, date
        self.lines, self.n = [], 0
        out.mkdir(parents=True, exist_ok=True)
        self.base = {'DATE': date, 'KITVERSION': version, 'SUBJ': subj, 'SUBJWORD': SUBJECTS[subj][1]}

    def job(self, kind, course, detail, template, extra, gate=None):
        """Write a job file from kit/<template>.txt; gate is (first, last) for a day job's ledger gate queue line."""
        self.n += 1
        num = '%03d' % self.n
        mp = dict(self.base)
        mp.update(extra)
        mp['COURSE'] = course
        mp['JOB'] = safe('%s-%s' % (kind, detail))
        mp['PLANGATE'] = PLANGATE.replace('COURSE', course)
        mp['LESSONGATE'] = LESSONGATE.replace('COURSE', course)
        where = '%s %s %s' % (template, course, detail)
        for k, f in (('COMMON', 'common.txt'), ('GATELINE', 'gate-line.txt')):
            mp[k] = fill(read(KIT / f).strip(), mp, where) if k in ('COMMON',) or gate else ''
        mp['GRADENOTE'] = fill(read(KIT / 'notes' / ('grade-%s.txt' % grade_token(course))).strip(), mp, where)
        mp['SUBJNOTE'] = fill(read(KIT / 'notes' / ('subject-%s.txt' % self.subj)).strip(), mp, where)
        if gate:
            mp['GATELINE'] = fill(read(KIT / 'gate-line.txt').strip(), mp, where)
            self.lines.append('%s | GATE | %s | %s | python -X utf8 scripts/ledger.py gate %s %s %s %s'
                              % (num + 'g', course, detail, self.subj, course, gate[0], gate[1]))
        body = fill(read(KIT / (template + '.txt')), mp, where)
        head = 'KIT-VERSION: %s\nJob %s: %s, %s, %s. Generated %s by scripts/coursegen.py.\n\n' % (
            self.version, num, kind, course, detail, self.date)
        name = '%s-%s-%s.txt' % (num, kind, safe(course + '-' + detail))
        (self.out / name).write_text(head + body, encoding='utf-8', newline='\n')
        self.lines.append('%s | %s | %s | %s | %s' % (num, kind.upper(), course, detail, name))
        return name

    def lead(self, kind, course, detail, template=None, extra=None):
        if template:
            return self.job(kind, course, detail, template, extra or {})
        self.n += 1
        self.lines.append('%03d | LEAD | %s | %s | -' % (self.n, course, detail))

    def write(self, header):
        (self.out / 'queue.txt').write_text('\n'.join(header + self.lines) + '\n', encoding='utf-8', newline='\n')


def missing_inputs(course, subj):
    """Stages whose input is missing for this course, as readable lines."""
    miss = []
    if not (PLANS / course).is_dir():
        return ['no data/plans/%s/ folder (stage 3, course frame and scope and sequence, not started)' % course], None
    dp = PLANS / course / 'days.csv'
    if not dp.exists():
        miss.append('stage 3 (scope and sequence) missing: data/plans/%s/days.csv does not exist' % course)
        return miss, None
    rows = list(csv.DictReader(open(dp, encoding='utf-8')))
    secs = sections(rows)
    if not secs:
        miss.append('stage 3 incomplete: data/plans/%s/days.csv has no section rows (stretch and unit columns empty)' % course)
        return miss, None
    for f, stage in (('DEFAULTS.md', 'stage 3 (course frame)'), ('frame.md', 'stage 3 (course frame)')):
        if not (DOCS / course / f).exists():
            miss.append('%s missing: docs/courses/%s/%s' % (stage, course, f))
    for u in sorted(secs):
        if not (DOCS / course / ('s%02d.md' % u)).exists():
            miss.append('stage 4 (unit plans) missing: docs/courses/%s/s%02d.md' % (course, u))
    return miss, (rows, secs)


def gen_course(q, course, rows, secs, opts, probe):
    subj = q.subj
    ela = subj == 'ela'
    units = sorted(secs)
    checks = sorted(int(r['day']) for r in rows if not r['stretch'].isdigit() or not r['unit'])
    allrows = sorted(int(r['day']) for r in rows)
    units_days = {u: [d for _, ds in secs[u] for d in ds] for u in units}

    def sec_jobs(u):
        uu = '%02d' % u
        for i, g in enumerate(halves(secs[u])):
            q.job('sec', course, 'u%d%s' % (u, 'ab'[i] if len(halves(secs[u])) > 1 else ''), 'section',
                  {'UNIT': str(u), 'UU': uu, 'SECTIONS': ', '.join(sname(uu, s) for s, _ in g)})

    def data_key(u):
        uu = '%02d' % u
        hs = [secs[u]] if not ela else halves(secs[u])
        alld = units_days[u]
        for i, grp in enumerate(hs):
            ds = [d for _, x in grp for d in x]
            names = ', '.join(sname(uu, s) for s, _ in grp)
            if len(hs) == 1:
                ul = 'You also write the unit-level rows (error register, readiness and end-of-unit items, family note).'
                end = 'the end-of-unit items'
            elif i == 0:
                ul = ("This unit is split in two data jobs; you are the first: you also write the unit-level rows (the whole "
                      "unit's error register, readiness items, every end-of-unit item and the family note), so the second "
                      "job (sections %s) only adds its sections' rows." % ', '.join(sname(uu, s) for s, _ in hs[1]))
                end = 'every end-of-unit item of the whole unit'
            else:
                ul = ("This unit is split in two data jobs; you are the second: the first job wrote the unit-level rows "
                      "(error register, readiness, end items, family note); read them, add only your sections' rows, and "
                      "reuse its error letters (add a letter only if your sections need a new one, after the last).")
                end = 'no end items (the first job wrote them)'
            q.job('data', course, 'u%d%s' % (u, 'ab'[i] if len(hs) > 1 else ''), 'data',
                  {'UNIT': str(u), 'UU': uu, 'SECTIONS': names, 'FIRST': str(min(ds)), 'LAST': str(max(ds)),
                   'UNITLEVEL': ul, 'ENDITEMS': end})
        q.job('key', course, 'u%d' % u, 'key', {'UNIT': str(u), 'UU': uu, 'FIRST': str(min(alld)), 'LAST': str(max(alld))})

    def prev_text(first, ds):
        prev = max([d for d in allrows if d < first], default=None)
        if prev is None:
            t = 'Day %d is the first day of this course: there is no day before it.' % first
        else:
            t = ('The day before your first is day %d (find it with courses/%s/*/d%03d.md); read it in full, as write.md '
                 'says. If it is not written yet, read the latest written day before it.' % (prev, course, prev))
        if len(ds) != ds[-1] - ds[0] + 1:
            t += ' Your days are not consecutive (%s): write only these.' % ', '.join(map(str, ds))
        return t

    # day events in day order: ('unit', u, batch) or ('checks', None, run)
    events = []
    for u in units:
        for b in day_batches(secs[u], opts.day_min, opts.day_max):
            events.append((min(d for _, x in b for d in x), 'unit', u, b))
    for r in runs(checks, opts.day_max):
        events.append((r[0], 'checks', None, r))
    events.sort(key=lambda e: e[0])
    prepared = set()

    def emit_event(e):
        _, kind, u, b = e
        if kind == 'unit':
            if u not in prepared:
                data_key(u)
                prepared.add(u)
            uu = '%02d' % u
            ds = [d for _, x in b for d in x]
            st = '; '.join('section %s (folder courses/%s/%s/, days %d to %d)' % (s, course, sname(uu, s), x[0], x[-1])
                           for s, x in b)
            q.job('day', course, '+'.join(s for s, _ in b), 'day',
                  {'UNIT': str(u), 'UU': uu, 'FIRST': str(ds[0]), 'LAST': str(ds[-1]), 'SECTIONTEXT': st,
                   'PREVDAY': prev_text(ds[0], ds)}, gate=(ds[0], ds[-1]))
        else:
            q.job('checks', course, 'days-%d-%d' % (b[0], b[-1]), 'checks',
                  {'CHECKDAYS': ', '.join(map(str, b)), 'FIRST': str(b[0]), 'LAST': str(b[-1])}, gate=(b[0], b[-1]))

    q.lead('lead', course, 'BUILD section skeletons (stage 5 section cuts) for every unit: python -X utf8 '
           'scripts/section_skeleton.py %s all (ignored working files, always rebuilt from data)' % course)
    if opts.texts and ela:
        for u in units:
            q.job('text', course, 'u%d' % u, 'text', {'UNIT': str(u), 'UU': '%02d' % u})
        q.lead('lead', course, 'MERGE texts-out/%s-u*.csv into data/plans/ela-texts.csv and rebuild skeletons' % course)

    rest_units = units
    if probe:
        u1 = units[0]
        lo, hi = min(units_days[u1]), max(units_days[u1])
        sec_jobs(u1)
        if opts.texts and ela:
            q.job('text2', course, 'u%d' % u1, 'text2', {'UNIT': str(u1), 'UU': '%02d' % u1})
        first_ev = [e for e in events if (e[1] == 'unit' and e[2] == u1) or (e[1] == 'checks' and lo <= e[0] <= hi)]
        for e in first_ev:
            emit_event(e)
        events = [e for e in events if e not in first_ev]
        q.lead('lead', course, 'PROBE RETOOL STOP: unit 1 is through days. Re-run the filtered gates yourself, '
               'log findings (found at, made at) in docs/pipeline/kit/RETOOL.md, retool the kit, bump KIT-VERSION, '
               'regenerate this grade\'s remaining queue; the kit is then frozen for the grade (COURSE-RUN stage 5)')
        rest_units = units[1:]
    for u in rest_units:
        sec_jobs(u)
        if opts.texts and ela:
            q.job('text2', course, 'u%d' % u, 'text2', {'UNIT': str(u), 'UU': '%02d' % u})
    if opts.texts and ela:
        q.lead('lead', course, 'MERGE texts-out/%s-u*-new.csv (merge_extra) and rebuild skeletons' % course)
    # fresh plan read (units in chunks), then one fix
    if rest_units:
        chunks = [rest_units[i:i + opts.read_units] for i in range(0, len(rest_units), opts.read_units)]
        for i, c in enumerate(chunks):
            q.job('plan-read', course, 'units-%s' % '-'.join(map(str, (c[0], c[-1]))) if len(c) > 1 else 'unit-%d' % c[0],
                  'plan-read', {'UNITS': ', '.join(map(str, c)), 'PART': 'abcdefgh'[i]})
        q.job('plan-fix', course, 'grade', 'plan-fix', {})
        q.lead('lead', course, 'after plan fix: re-run the filtered unitplan and ledger checks yourself; faults made at '
               'an earlier stage found here go to a sweep (kit/sweep.txt); the kit is frozen from here to the grade end')
    # days, in day order, each unit's data and key just before its first day job
    for e in events:
        emit_event(e)
    q.lead('lead', course, 're-run the filtered plan and lesson gates for the course yourself; save the counts '
           '(agents\' own counts are not trusted)')
    # grade sample: one day per decile, a gets even deciles, b odd
    rng = random.Random(course)
    pool = sorted(allrows)
    pick = []
    for i in range(10):
        part = pool[len(pool) * i // 10: len(pool) * (i + 1) // 10]
        pick.append(rng.choice(part) if part else None)
    for tag, idx in (('a', range(0, 10, 2)), ('b', range(1, 10, 2))):
        days = [pick[i] for i in idx if pick[i]]
        q.job('sample-read', course, tag, 'sample-read', {'PART': tag, 'DAYS': ', '.join(map(str, days))})
    q.job('cleanup', course, 'grade', 'cleanup', {})
    q.lead('retool', course, 'grade close', 'retool-stop', {})


def main_gen(a):
    subj = a.subject
    prefix = SUBJECTS[subj][0]
    version, date = kit_version(), datetime.date.today().isoformat()
    for c in a.courses:
        fr = frame_row(c)
        if (fr['subject'] if fr else None) != subj and not c.startswith(prefix):
            sys.exit('course %s is not a %s course (frames.csv subject, or prefix %s)' % (c, subj, prefix))
        if grade_token(c) is None:
            sys.exit('course %s has no grade: no grade in data/plans/frames.csv and no kindergarten or grade-N ending' % c)
    for f in ['notes/subject-%s.txt' % subj] + ['notes/grade-%s.txt' % grade_token(c) for c in a.courses]:
        if not (KIT / f).exists():
            sys.exit('the kit has no %s: write it first (RETOOL.md entry)' % f)
    if 'STUB' in read(KIT / ('notes/subject-%s.txt' % subj))[:20]:
        print('WARNING: subject note for %s is a stub; write docs/pipeline/kit/notes/subject-%s.txt before running jobs'
              % (subj, subj))
    q = Queue(Path(a.out), subj, version, date)
    done, status = [], 0
    for i, c in enumerate(a.courses):
        miss, data = missing_inputs(c, subj)
        if miss:
            print('NOT GENERATED %s: %d missing input(s); every course after it is skipped too' % (c, len(miss)))
            for m in miss:
                print('  - ' + m)
            status = 2
            break
        rows, secs = data
        gen_course(q, c, rows, secs, a, a.probe and i == 0)
        done.append(c)
    if len(done) >= 2:
        q.job('continuity-read', done[-1], 'all-grades', 'continuity-read', {'COURSES': ', '.join(done)})
        for c in done[1:]:
            q.job('continuity-fix', c, 'grade', 'continuity-fix', {})
    if done:
        q.lead('lead', done[-1], 'subject close: run `python -X utf8 scripts/ledger.py recheck %s` yourself, add the later.csv '
               'row and the token report' % subj)
    q.write(['# queue for %s: %s' % (subj, ' '.join(a.courses)),
             '# KIT-VERSION: %s; generated %s; probe=%s texts=%s; command: coursegen.py %s' % (
                 version, date, a.probe, a.texts, ' '.join(sys.argv[1:])),
             '# columns: number | kind | course | detail | file (GATE lines carry the ledger gate command; LEAD lines are yours)'])
    print('%s: %d lines (%d jobs written) in %s; kit %s' % (', '.join(done) or 'no course', len(q.lines), q.n, a.out, version))
    return status


def main_sweep(a):
    version, date = kit_version(), datetime.date.today().isoformat()
    course = a.courses[0]
    gate_kind = STAGE_GATES.get(a.made_at, 'plan')
    gates = {'unitplan': 'python -X utf8 scripts/unitplan.py check %s' % course,
             'plan': PLANGATE.replace('COURSE', course),
             'lesson': LESSONGATE.replace('COURSE', course)}[gate_kind]
    scope = a.scope or {'unit plan': 'docs/courses/%s/s*.md' % course,
                        'section plan': 'docs/courses/%s/u*-*.md' % course,
                        'data': 'data/plans/%s/ (items, wrongs, handbacks, sources) and courses/%s/u*-*/ shared pieces' % (course, course),
                        'days': 'courses/%s/**/d*.md' % course}.get(a.made_at, 'every file of that stage in ' + course)
    q = Queue(Path(a.out), a.subject, version, date)
    q.job('sweep', course, a.tag or 'fault', 'sweep',
          {'FAULT': a.fault, 'FOUND_AT': a.found_at, 'MADE_AT': a.made_at, 'FOUND_IN': a.found_in or 'the run report',
           'TEST': a.test, 'SCOPE': scope, 'TOOL': a.tool or 'name it', 'GATES': gates, 'TAG': safe(a.tag or 'fault')})
    q.write(['# sweep job; KIT-VERSION: %s; generated %s' % (version, date)])
    print('sweep job written to', a.out)
    return 0


def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'sweep':
        ap = argparse.ArgumentParser(prog='coursegen.py sweep')
        ap.add_argument('sweep')
        ap.add_argument('subject', choices=sorted(SUBJECTS))
        ap.add_argument('courses', nargs=1)
        ap.add_argument('--out', required=True)
        for k in ('made-at', 'found-at', 'fault', 'test'):
            ap.add_argument('--' + k, required=True)
        for k in ('found-in', 'tool', 'scope', 'tag'):
            ap.add_argument('--' + k)
        return main_sweep(ap.parse_args())
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('subject', choices=sorted(SUBJECTS))
    ap.add_argument('courses', nargs='+')
    ap.add_argument('--out', required=True)
    ap.add_argument('--probe', action='store_true', help="run the first course's unit 1 through days first")
    ap.add_argument('--texts', action='store_true', help='ELA only: add text and text2 jobs')
    ap.add_argument('--read-units', type=int, default=4, help='units per plan reader (default 4)')
    ap.add_argument('--day-min', type=int, default=4)
    ap.add_argument('--day-max', type=int, default=6)
    return main_gen(ap.parse_args())


if __name__ == '__main__':
    sys.exit(main())

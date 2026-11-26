"""A read-only spacing report for one course, from its ledger and plan data (pedagogy-architecture review change 8).

    python -X utf8 scripts/spacing.py <course> [--all]

Read at the stage 4 gate (units planned: do owned skills come back?) and at grade close (days written: how far apart
are the returns, and which words were taught once and never used again?). It fails nothing; it is a reading.

Three parts:
1. Gaps: every "review of ..." citation in this course's ledger that resolves (ledger.py, as the recheck does) to a
   row with a day, measured in school days when both ends are in this course, and counted by grade when the cited row
   is an earlier course's. Shown as a distribution, so a course whose returns all sit within a week of first teaching
   shows it.
2. Owned skills that never return after their unit: a skill the frame's Units table gives to unit N, named by no day
   of a later unit or later course-level check day (days.csv `skills`, `retrieves` when that column exists, or the day's note naming the skill id).
3. Terms never cited again: written term rows this course introduces (not reviews) that no later ledger row, in this
   course or a later grade of the subject, reviews (a citation counts when it resolves to at most three rows).
"""
import csv
import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLANS = ROOT / 'data' / 'plans'
sys.path.insert(0, str(ROOT / 'scripts'))

CAP = 25


def rows_of(p):
    if not p.exists():
        return []
    with io.open(p, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(line for line in f if not line.startswith('#')))


def subject_of(course):
    import ledger
    for s, cs in ledger.LADDER.items():
        if course in cs:
            return s, cs
    return None, []


def ids(s):
    return [x.strip() for x in re.split(r'[;,]', s or '') if x.strip()]


def report(course, full=False):
    import ledger
    import frame
    subj, ladder = subject_of(course)
    if not subj:
        sys.exit('%s is not on a ledger ladder (ledger.py LADDER)' % course)
    rs = ledger.rows(subj)
    lix = ledger.index(rs)
    days = {int(r['day']): r for r in rows_of(PLANS / course / 'days.csv') if (r.get('day') or '').isdigit()}
    school = {d: int(r['school_day']) if (r.get('school_day') or '').isdigit() else d for d, r in days.items()}
    unit_of = {d: (r.get('stretch') or '').strip() for d, r in days.items()}
    print('Spacing report: %s (%s ledger, %d days in days.csv)' % (course, subj, len(days)))

    # 1. gaps
    within, earlier, cited = [], {}, set()
    for r, ts in ledger.claims(subj, rs):
        for t in ts:
            st, hit = ledger.resolve(t, lix)
            if len(hit) <= 3:                  # a narrow match; "review of <course> u02-1" alone matches every row
                for h in hit:
                    cited.add(id(h))
            if r['course'] != course or not (r['day'] or '').isdigit():
                continue
            d = int(r['day'])
            # measure from the earliest cited row in this course (a broad "review of <course> u02-1" cites a whole
            # section, and its first day is the first teaching), else from the earlier course's row
            for h in sorted(hit, key=lambda x: (x['course'] != course, int(x['day']) if (x['day'] or '').isdigit() else 999))[:1]:
                if h['course'] == course and (h['day'] or '').isdigit():
                    g = school.get(d, d) - school.get(int(h['day']), int(h['day']))
                    if g > 0:
                        within.append(g)
                elif h['course'] != course:
                    earlier[h['course']] = earlier.get(h['course'], 0) + 1
    print('\n1. Gaps between first teaching and a return, in school days (%d returns within the course)' % len(within))
    bands = [(1, 5, 'within a week'), (6, 20, '1 to 4 weeks'), (21, 60, '1 to 3 months'), (61, 999, 'over 3 months')]
    counts = [sum(1 for g in within if lo <= g <= hi) for lo, hi, _ in bands]
    top = max(counts + [1])
    for (lo, hi, name), n in zip(bands, counts):
        print('   %-14s %4d %s' % (name, n, '#' * (60 * n // top)))
    if within:
        s = sorted(within)
        print('   median %d, longest %d' % (s[len(s) // 2], s[-1]))
    for c, n in sorted(earlier.items(), key=lambda x: ladder.index(x[0]) if x[0] in ladder else 99):
        print('   returns to %s: %d' % (c, n))

    # 2. owned skills that never return after their unit
    try:
        table = frame.parse(course).get('table') or []
    except Exception:
        table = []
    owned = {}
    for r in table:
        if (r.get('#') or '').strip().isdigit():
            for sid in ids(r.get('Skills')):
                owned.setdefault(sid, int(r['#']))
    lost = []
    for sid, u in sorted(owned.items(), key=lambda x: (x[1], x[0])):
        last = max([d for d in days if unit_of[d] == str(u)] or [0])
        back = [d for d, r in days.items() if (unit_of[d].isdigit() and int(unit_of[d]) > u or unit_of[d] == 'C' and d > last)
                and (sid in ids(r.get('skills')) or sid in ids(r.get('retrieves')) or sid in (r.get('note') or ''))]
        if not back:
            lost.append('%s (unit %d)' % (sid, u))
    print('\n2. Owned skills that never return after their unit: %d of %d' % (len(lost), len(owned)))
    for x in lost[:None if full else CAP]:
        print('   ' + x)
    if not full and len(lost) > CAP:
        print('   ... %d more (--all)' % (len(lost) - CAP))

    # 3. terms never cited again
    later = set(ladder[ladder.index(course):])
    mine = [r for r in rs if r['course'] == course and r['kind'] == 'term' and r['stage'] == 'written'
            and 'review of' not in r['note']]
    import vocabulary
    seen = {}                                 # head word -> the (course, day) of every later review row naming it
    for r in rs:
        if r['course'] in later and 'review of' in r['note']:
            for w in vocabulary.heads(r['entry']):
                seen.setdefault(w.lower(), []).append((ladder.index(r['course']), int(r['day']) if r['day'].isdigit() else 999))

    def again(r):
        if id(r) in cited:
            return True
        here, d = ladder.index(course), int(r['day']) if r['day'].isdigit() else 0
        return any((c, x) > (here, d) for w in vocabulary.heads(r['entry']) for c, x in seen.get(w.lower(), []))
    once = [r for r in mine if not again(r)]
    print('\n3. Terms this course introduces that no later row reviews: %d of %d' % (len(once), len(mine)))
    for r in sorted(once, key=lambda x: int(x['day']) if x['day'].isdigit() else 0)[:None if full else CAP]:
        print('   day %s %s: %s' % (r['day'] or '?', r['where'], r['entry'][:70]))
    if not full and len(once) > CAP:
        print('   ... %d more (--all)' % (len(once) - CAP))

    return 0


def main(a):
    full = '--all' in a
    a = [x for x in a if x != '--all']
    if len(a) != 1:
        print(__doc__)
        return 2
    return report(a[0], full)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

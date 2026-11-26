"""The pass marks a grade close measured (pedagogy-architecture review change 3, 2026-11-25).

    python -X utf8 scripts/pass_marks.py add <course> <YYYY-MM-DD> <days sampled> <serious a day> <wrong keys> <tokens a day> "<note>"
    python -X utf8 scripts/pass_marks.py show [course]

One row per course per grade close in data/plans/pass-marks.csv, beside data/plans/debt.csv (the gate's known
failing lines): debt says what the gates still fail, pass marks say what the readers found. The lead adds the row
after the grade-close sample read (COURSE-RUN stage 6), from the readers' reports:
- days sampled: the days the fresh readers read in full;
- serious a day: FIRM faults (the kind a teacher would hit in class) divided by days sampled;
- wrong keys: keys found wrong in the sample (a key that marks a right answer wrong, or the reverse);
- tokens a day: the writer's tokens per day for the grade, from the run's token record.
A measure the run did not record is left blank, never estimated. COURSE-RUN section 5 sets the marks to meet; the
Dashboard's quality panel (plan_flow.py health) shows the rows over time. Adding a row for the same course and date
replaces it.
"""
import csv
import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILE = ROOT / 'data' / 'plans' / 'pass-marks.csv'
COLS = ['course', 'date', 'days_sampled', 'serious_a_day', 'wrong_keys', 'tokens_a_day', 'note']


def rows():
    if not FILE.exists():
        return []
    with io.open(FILE, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def write(rs):
    rs.sort(key=lambda r: (r['course'], r['date']))
    with io.open(FILE, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, COLS, lineterminator='\n')
        w.writeheader()
        w.writerows(rs)


def num(x, kind):
    if x == '':
        return ''
    try:
        kind(x)
    except ValueError:
        sys.exit('not a number: %r (leave a measure blank with "")' % x)
    return x


def main(a):
    if a[:1] == ['add'] and len(a) == 8:
        c, d, n, s, k, t, note = a[1:]
        if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', d):
            sys.exit('date must be YYYY-MM-DD')
        if not (ROOT / 'data' / 'plans' / c).is_dir():
            sys.exit('no course %s' % c)
        new = dict(course=c, date=d, days_sampled=num(n, int), serious_a_day=num(s, float), wrong_keys=num(k, int),
                   tokens_a_day=num(t, int), note=note)
        rs = [r for r in rows() if (r['course'], r['date']) != (c, d)] + [new]
        write(rs)
        print('pass marks: %s %s written' % (c, d))
        return 0
    if a[:1] == ['show']:
        for r in rows():
            if len(a) < 2 or r['course'] == a[1]:
                print('%-32s %s  days %-3s serious/day %-4s wrong keys %-3s tokens/day %s' % (
                    r['course'], r['date'], r['days_sampled'], r['serious_a_day'], r['wrong_keys'],
                    r['tokens_a_day']))
        return 0
    print(__doc__)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

"""Move the `version:` line of a course's day files at a stage gate (pedagogy-architecture review change 2, 2026-11-25).

    python -X utf8 scripts/day_version.py <course> grade-read <YYYY-MM-DD> [--dry-run]
    python -X utf8 scripts/day_version.py <course> signed-off <YYYY-MM-DD> [--dry-run]
    python -X utf8 scripts/day_version.py <course> show
    python -X utf8 scripts/day_version.py <course> stamp <YYYY-MM-DD>      store the upstream marks after another full read
    python -X utf8 scripts/day_version.py <course> changed                 days whose upstream changed since their mark
    python -X utf8 scripts/day_version.py --self-test

A day's own file is its status (index.py status report): the version line says how far the day has come, so no
separate status table is kept. The lead runs this at a grade close (after the sample read and cleanup are
committed: `grade-read`) and after the owner's sign-off (`signed-off`). Only day files (courses/<course>/*/dNNN.md)
change, and only their version line.

The line is built in a fixed order, each clause at most once:

    draft N[, grade read DATE][, signed off DATE][, not ready], not yet taught

- `draft` alone becomes `draft 1`; the writer's draft number is kept.
- `not ready` is left as it is: it means a piece the day leans on is still to make (lesson.py reads it), which a
  sign-off does not change. It is dropped by hand, or by a later run, when the pieces exist.
- `not yet taught` stays until a classroom has taught the day.
- A grade read never moves a signed-off day back; a second grade read updates the date.
"""
import csv
import datetime
import hashlib
import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PIECES = ROOT / 'courses'
PLANS = ROOT / 'data' / 'plans'
MARKS = 'day-marks.csv'
MARK_COLS = ['day', 'hash', 'date', 'stage']


# ---- the upstream-changed mark (review change 6): what a read saw above each day
#
# At every read gate (grade-read, signed-off, or `stamp` after any other full read of a course's days) the script
# stores, per day with a file, one hash of what the day is built from: its days.csv row and its items.csv rows
# (stems, keys, steps, samples, every column). data/plans/<course>/day-marks.csv holds day, hash, date, stage.
# index.py's status report recomputes the hash and lists a day whose upstream changed since that read: the day was
# read against data that is no longer there, so it needs a look (or a fresh stamp once it is read again).

def _rows(p):
    if not p.exists():
        return []
    with io.open(p, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def upstream(days, items):
    """{day number: hash} from days.csv rows and items.csv rows (CSV dicts)."""
    by = {}
    for r in items:
        if (r.get('day') or '').isdigit():
            by.setdefault(int(r['day']), []).append(r)
    out = {}
    for r in days:
        if not (r.get('day') or '').isdigit():
            continue
        d = int(r['day'])
        parts = ['\x1f'.join('%s=%s' % (k, r[k]) for k in sorted(r) if k and r[k])]   # a blank new column: no change
        for it in sorted(by.get(d, []), key=lambda x: x.get('item_id', '')):
            parts.append('\x1f'.join('%s=%s' % (k, it[k]) for k in sorted(it) if k and it[k]))
        out[d] = hashlib.sha1('\x1e'.join(parts).encode('utf-8')).hexdigest()[:16]
    return out


def marks(course):
    return {int(r['day']): r for r in _rows(PLANS / course / MARKS) if (r.get('day') or '').isdigit()}


def stamp(course, stage, date, have):
    """Store the hash of every day in `have` (day numbers with a file); other days' marks are kept."""
    now = upstream(_rows(PLANS / course / 'days.csv'), _rows(PLANS / course / 'items.csv'))
    m = marks(course)
    for d in have:
        if d in now:
            m[d] = dict(day=str(d), hash=now[d], date=date, stage=stage)
    with io.open(PLANS / course / MARKS, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, MARK_COLS, lineterminator='\n')
        w.writeheader()
        w.writerows(m[d] for d in sorted(m))
    print('%s: %d day marks stored in data/plans/%s/%s (%s %s)' % (course, len(have), course, MARKS, stage, date))


def changed(course, days=None, items=None):
    """[(day, mark row)] whose upstream hash differs from the stored mark."""
    m = marks(course)
    if not m:
        return []
    now = upstream(days if days is not None else _rows(PLANS / course / 'days.csv'),
                   items if items is not None else _rows(PLANS / course / 'items.csv'))
    return [(d, m[d]) for d in sorted(m) if now.get(d) != m[d]['hash']]
LINE = re.compile(r'^version:[ \t]*(.*?)[ \t]*$', re.M)
DATE = re.compile(r'\d{4}-\d{2}-\d{2}$')


def parse(v):
    """{'draft': N, 'read': date, 'signed': date, 'not_ready': bool, 'taught': bool, 'other': [clauses]}."""
    out = {'draft': 1, 'read': '', 'signed': '', 'not_ready': False, 'other': []}
    for cl in [x.strip() for x in v.split(',') if x.strip()]:
        lo = cl.lower()
        m = re.fullmatch(r'draft(?: (\d+))?', lo)
        if m:
            out['draft'] = int(m.group(1) or 1)
        elif lo.startswith('grade read '):
            out['read'] = cl[len('grade read '):].strip()
        elif lo.startswith('signed off '):
            out['signed'] = cl[len('signed off '):].strip()
        elif lo == 'not ready':
            out['not_ready'] = True
        elif lo == 'not yet taught':
            pass
        else:
            out['other'].append(cl)
    return out


def render(p):
    parts = ['draft %d' % p['draft']]
    if p['read']:
        parts.append('grade read ' + p['read'])
    if p['signed']:
        parts.append('signed off ' + p['signed'])
    parts += p['other']
    if p['not_ready']:
        parts.append('not ready')
    parts.append('not yet taught')
    return ', '.join(parts)


def move(v, stage, date):
    p = parse(v)
    if stage == 'grade-read':
        if not p['signed']:
            p['read'] = date
    elif stage == 'signed-off':
        p['signed'] = date
    else:
        raise ValueError(stage)
    return render(p)


def day_files(course):
    return sorted(f for f in (PIECES / course).glob('*/d*.md') if re.fullmatch(r'd\d{3}[a-z]?\.md', f.name))


def run(course, stage, date, dry):
    files = day_files(course)
    if not files:
        sys.exit('no day files under courses/%s' % course)
    changed = 0
    seen = {}
    for f in files:
        raw = f.read_bytes()
        text = raw.decode('utf-8')
        m = LINE.search(text[:3000])
        if not m:
            print('%s: no version line (index.py status reports it); left alone' % f.relative_to(ROOT).as_posix())
            continue
        new = move(m.group(1), stage, date)
        seen[new] = seen.get(new, 0) + 1
        if new == m.group(1):
            continue
        changed += 1
        if not dry:
            text = text[:m.start(1)] + new + text[m.end(1):]
            f.write_bytes(text.encode('utf-8'))
    for v, n in sorted(seen.items(), key=lambda x: -x[1]):
        print('%4d  version: %s' % (n, v))
    print('%s: %d of %d day files %s' % (course, changed, len(files), 'would change' if dry else 'changed'))
    if not dry:
        stamp(course, stage, date, day_numbers(files))


def day_numbers(files):
    return sorted({int(re.match(r'd(\d{3})', f.name).group(1)) for f in files})


def show(course):
    seen = {}
    for f in day_files(course):
        m = LINE.search(f.read_text(encoding='utf-8')[:3000])
        v = m.group(1) if m else '(no version line)'
        seen[v] = seen.get(v, 0) + 1
    for v, n in sorted(seen.items(), key=lambda x: -x[1]):
        print('%4d  version: %s' % (n, v))


def self_test():
    ok = True

    def check(name, cond):
        nonlocal ok
        ok = ok and bool(cond)
        print('  %s %s' % ('ok    ' if cond else 'FAILED', name))
    check('grade read keeps not ready',
          move('draft 1, not ready, not yet taught', 'grade-read', '2026-11-22')
          == 'draft 1, grade read 2026-11-22, not ready, not yet taught')
    check('sign-off after a grade read',
          move('draft 1, grade read 2026-11-22, not ready, not yet taught', 'signed-off', '2026-11-23')
          == 'draft 1, grade read 2026-11-22, signed off 2026-11-23, not ready, not yet taught')
    check('bare draft becomes draft 1 and gains not yet taught',
          move('draft', 'grade-read', '2026-11-22') == 'draft 1, grade read 2026-11-22, not yet taught')
    check('a grade read never moves a signed-off day back',
          move('draft 2, signed off 2026-11-23, not yet taught', 'grade-read', '2026-12-01')
          == 'draft 2, signed off 2026-11-23, not yet taught')
    check('idempotent', move(move('draft 1, not ready, not yet taught', 'signed-off', '2026-11-23'), 'signed-off',
                             '2026-11-23') == 'draft 1, signed off 2026-11-23, not ready, not yet taught')
    a = [{'day': '1', 'goal': 'x'}, {'day': '2', 'goal': 'y'}]
    it = [{'item_id': 's01-X1', 'day': '1', 'answer': '4'}]
    h1 = upstream(a, it)
    h2 = upstream(a, [{'item_id': 's01-X1', 'day': '1', 'answer': '5'}])
    check('upstream mark: a changed key changes only its day', h1[1] != h2[1] and h1[2] == h2[2])
    print('day_version self-test: %s' % ('all passed' if ok else 'FAILED'))
    return 0 if ok else 1


def main(a):
    if a == ['--self-test']:
        return self_test()
    if len(a) == 2 and a[1] == 'show':
        return show(a[0]) or 0
    if len(a) == 3 and a[1] == 'stamp' and DATE.match(a[2]):
        return stamp(a[0], 'read', a[2], day_numbers(day_files(a[0]))) or 0
    if len(a) == 2 and a[1] == 'changed':
        for d, r in changed(a[0]):
            print('day %d: upstream changed since its %s mark of %s' % (d, r['stage'], r['date']))
        return 0
    if len(a) >= 3 and a[1] in ('grade-read', 'signed-off') and DATE.match(a[2]):
        return run(a[0], a[1], a[2], '--dry-run' in a) or 0
    print(__doc__)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

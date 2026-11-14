"""Gate for course frames, docs/courses/<slug>/frame.md (PRODUCTION-PATH step 2, added 2026-11-13).

    python -X utf8 scripts/frame.py check [slug ...]   check the frames (all found, or the ones named)
    python -X utf8 scripts/frame.py sync               rewrite data/plans/frames.csv (course,units,days) from them

The frame's format is set by docs/pipeline/briefs/frame-write.md. Which progression rows a course owns is set in
COURSE_ROWS below (subject, and the grades or skill_id prefixes); add a course there when its frame is written.

FAIL (exit 1):
- a missing section (The course in brief, Seams, Models carried, Units, Course-level checks, Cross-subject);
- the **Units.** or **Days.** bullet with no number first; a Units table whose row count differs from **Units.**;
- unit days that add to more than the course's days;
- a Skills id that is not one of the course's rows, or sits in two units; a course row placed in no unit;
- an Owned standards code that the unit's rows do not own, or a code a unit's rows own (not ~) missing from its
  Owned standards;
- data/plans/frames.csv disagreeing with the frame (run sync);
- a stale note (scripts/stale.py) in the frame.
note (exit 0): the days left for course-level checks and respond days, per course.
"""
import csv
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))

# slug -> (subject, test on a progression row)
def _grade(g):
    return lambda r: r['grade'].strip() == g
def _prefix(p):
    return lambda r: r['skill_id'].startswith(p)
COURSE_ROWS = {
    'social-studies-kindergarten': ('social-studies', _grade('K')),
    'world-geography-and-ancient-civilizations-i': ('social-studies', _grade('6')),
    'world-geography-and-ancient-civilizations-ii': ('social-studies', _grade('7')),
    'civics-government-and-civic-life': ('social-studies', _grade('8')),
    'world-history-i': ('social-studies', _grade('9')),
    'world-history-ii': ('social-studies', _grade('10')),
    'us-history-i': ('social-studies', _grade('11')),
    'us-history-ii': ('social-studies', _prefix('us2-')),
    'us-government-and-politics': ('social-studies', _prefix('gov-')),
    'economics': ('social-studies', _prefix('econ-')),
}
for _g in range(1, 6):
    COURSE_ROWS['social-studies-grade-%d' % _g] = ('social-studies', _grade(str(_g)))

SECTIONS = ['The course in brief', 'Seams', 'Models carried', 'Units', 'Course-level checks', 'Cross-subject']
_rows = {}


def rows(subject):
    if subject not in _rows:
        p = os.path.join(ROOT, 'data', 'progressions', subject + '.csv')
        _rows[subject] = list(csv.DictReader(open(p, encoding='utf-8')))
    return _rows[subject]


def split(cell):
    return [x.strip() for x in re.split(r';|,', cell or '') if x.strip()]


def path_of(slug):
    return os.path.join(ROOT, 'docs', 'courses', slug, 'frame.md')


def parse(slug):
    t = open(path_of(slug), encoding='utf-8').read()
    out = {'text': t, 'sections': re.findall(r'^## (.+?)\s*$', t, re.M)}
    for k in ('Units', 'Days'):
        m = re.search(r'^\s*[-*]\s*\*\*%s\.\*\*\s*(\d+)' % k, t, re.M)
        out[k.lower()] = int(m.group(1)) if m else None
    units = []
    sec = re.search(r'^## Units\s*$(.*?)(?=^## |\Z)', t, re.M | re.S)
    if sec:
        lines = [l for l in sec.group(1).splitlines() if l.strip().startswith('|')]
        if lines:
            head = [c.strip() for c in lines[0].strip().strip('|').split('|')]
            for l in lines[2:]:
                cells = [c.strip() for c in l.strip().strip('|').split('|')]
                if len(cells) < len(head):
                    cells += [''] * (len(head) - len(cells))
                units.append(dict(zip(head, cells)))
    out['table'] = units
    return out


def check(slug):
    fails, notes = [], []
    if slug not in COURSE_ROWS:
        return ['%s: not in COURSE_ROWS (scripts/frame.py)' % slug], notes
    subject, test = COURSE_ROWS[slug]
    f = parse(slug)
    for s in SECTIONS:
        if s not in f['sections']:
            fails.append('%s: no "## %s" section' % (slug, s))
    if f['units'] is None:
        fails.append('%s: the **Units.** bullet has no number first' % slug)
    if f['days'] is None:
        fails.append('%s: the **Days.** bullet has no number first' % slug)
    tab = f['table']
    if f['units'] is not None and len(tab) != f['units']:
        fails.append('%s: **Units.** says %d, the Units table has %d rows' % (slug, f['units'], len(tab)))
    own = {r['skill_id']: r for r in rows(subject) if test(r)}
    seen = {}
    day_sum = 0
    for u in tab:
        n = u.get('#', '?')
        d = re.match(r'\s*(\d+)', u.get('Days', ''))
        if d:
            day_sum += int(d.group(1))
        else:
            fails.append('%s unit %s: Days is not a number' % (slug, n))
        ids = split(u.get('Skills', '').replace('`', ''))
        owned_codes = set()
        for i in ids:
            if i not in own:
                fails.append('%s unit %s: skill %s is not one of the course rows' % (slug, n, i))
                continue
            if i in seen:
                fails.append('%s: skill %s in units %s and %s' % (slug, i, seen[i], n))
            seen[i] = n
            owned_codes |= {c for c in split(own[i]['standard']) if not c.startswith('~')}
        listed = {c for c in split(u.get('Owned standards', '').replace('`', '')) if not c.startswith('~')}
        for c in sorted(listed - owned_codes):
            fails.append('%s unit %s: owned standard %s is not owned by the unit\'s rows' % (slug, n, c))
        for c in sorted(owned_codes - listed):
            fails.append('%s unit %s: its rows own %s, missing from Owned standards' % (slug, n, c))
    for i in own:
        if i not in seen:
            fails.append('%s: course row %s is in no unit' % (slug, i))
    if f['days'] is not None:
        if day_sum > f['days']:
            fails.append('%s: unit days add to %d, more than the course\'s %d' % (slug, day_sum, f['days']))
        else:
            notes.append('%s: %d units, %d days (%d in units, %d for checks and respond days)' %
                         (slug, len(tab), f['days'], day_sum, f['days'] - day_sum))
    import stale
    fails += stale.check_file(path_of(slug))
    csv_rows = {r['course']: r for r in csv.DictReader(open(os.path.join(ROOT, 'data', 'plans', 'frames.csv'), encoding='utf-8'))}
    r = csv_rows.get(slug)
    if not r or str(f['units']) != r['units'].strip() or str(f['days']) != r['days'].strip():
        fails.append('%s: data/plans/frames.csv disagrees with the frame (run scripts/frame.py sync)' % slug)
    return fails, notes


def found():
    return sorted(os.path.basename(os.path.dirname(p)) for p in glob.glob(os.path.join(ROOT, 'docs', 'courses', '*', 'frame.md')))


def sync():
    p = os.path.join(ROOT, 'data', 'plans', 'frames.csv')
    old = {r['course']: r for r in csv.DictReader(open(p, encoding='utf-8'))}
    for s in found():
        f = parse(s)
        old[s] = {'course': s, 'units': f['units'] or '', 'days': f['days'] or ''}
    with open(p, 'w', encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, ['course', 'units', 'days'], lineterminator='\n')
        w.writeheader()
        for k in sorted(old):
            w.writerow(old[k])
    print('frames.csv: %d course(s)' % len(old))


def main(a):
    if a[:1] == ['sync']:
        return sync()
    if a[:1] != ['check']:
        raise SystemExit(__doc__)
    bad = 0
    for s in a[1:] or found():
        fails, notes = check(s)
        print('frame %s: %d failure(s)' % (s, len(fails)))
        for x in fails:
            print('  FAIL', x)
        for x in notes:
            print('  note', x)
        bad += len(fails)
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main(sys.argv[1:])

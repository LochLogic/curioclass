"""Scope and sequence gate (PRODUCTION-PATH step 3): a course's day map before any section plan or item exists.

    python -X utf8 scripts/sequence.py check [course]     exit 1 on any failure

Reads docs/courses/<course>/frame.md (through scripts/frame.py) and data/plans/<course>/days.csv at the scope stage:
one row per course day, with the columns of docs/pipeline/briefs/sequence-write.md
(day, stretch, unit, kind, goal, skills, codes, assess, school_day, note). `stretch` is the unit number, or C for a
course-level check day or its respond day (with a blank `unit`). plan.py runs this gate for a course whose plan
folder has days.csv but no parts.csv and no items.csv; once section plans are written, plan.py's full gate takes over.
Added 2026-11-14 (baseline 1 structure finding 2).
"""
import csv, io, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLANS = ROOT / 'data' / 'plans'
DOCS = ROOT / 'docs' / 'courses'
sys.path.insert(0, str(Path(__file__).resolve().parent))
import frame   # noqa: E402

KINDS = {'Understanding', 'Fluency', 'Application', 'Check', 'Respond'}
ASSESS = {'', 'readiness', 'mid', 'end', 'course', 'observe'}
MID_UNIT_DAYS = 25          # a unit longer than this carries a mid-unit assessment
READINESS_AHEAD = 3         # a readiness check sits at most this many days before its unit's first day
NEED = ['day', 'stretch', 'unit', 'kind', 'goal', 'skills', 'codes', 'assess']


def rows(course, name):
    p = PLANS / course / (name + '.csv')
    if not p.exists():
        return None
    with io.open(p, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def stage(course):
    """'scope' when only days.csv exists, 'plan' once parts or items exist, None with no days.csv."""
    if rows(course, 'days') is None:
        return None
    return 'plan' if (rows(course, 'parts') or rows(course, 'items')) else 'scope'


def md_fails(md, slug, nunits):
    """The scope and sequence page holds its title and a section per unit (added 2026-11-14: three pages were
    committed empty that day and the gate passed them)."""
    t = md.read_text(encoding='utf-8')
    if not t.strip():
        return ['docs/courses/%s/scope-and-sequence.md is empty' % slug]
    out = []
    if not re.search(r'^#\s+Scope and sequence\b', t, re.M | re.I):
        out.append('docs/courses/%s/scope-and-sequence.md has no "# Scope and sequence: <title>" line' % slug)
    have = {int(m.group(1)) for m in re.finditer(r'^#{2,4}\s+Units?\s+(\d+)\b', t, re.M | re.I)}
    if not have:
        out.append('docs/courses/%s/scope-and-sequence.md has no unit sections ("## Unit 1. ...")' % slug)
    elif nunits:
        miss = [str(n) for n in range(1, nunits + 1) if n not in have]
        if miss:
            out.append('docs/courses/%s/scope-and-sequence.md has no section for unit(s) %s' % (slug, ', '.join(miss)))
    return out


def check(course):
    fails, notes = [], []
    slug = frame.LEGACY.get(course, course)
    days = rows(course, 'days') or []
    if slug not in frame.found():
        return ['no frame docs/courses/%s/frame.md for this scope and sequence' % slug], notes
    f = frame.parse(slug)
    md = DOCS / slug / 'scope-and-sequence.md'
    if not md.exists():
        fails.append('no docs/courses/%s/scope-and-sequence.md' % slug)
    else:
        fails += md_fails(md, slug, f.get('units') or 0)
        if not re.search(r'^#+\s*Shorter path', md.read_text(encoding='utf-8'), re.M | re.I):
            notes.append('scope-and-sequence.md has no "Shorter path" section (sequence-write.md rule 10, '
                         'added 2026-11-14)')
    if not days:
        return fails + ['days.csv has no rows'], notes
    miss = [c for c in NEED if c not in days[0]]
    if miss:
        return fails + ['days.csv lacks column(s) %s' % ', '.join(miss)], notes
    nums = [int(d['day']) for d in days if d['day'].strip().isdigit()]
    if nums != list(range(1, len(days) + 1)):
        fails.append('days are not numbered 1 to %d in order' % len(days))
    if f.get('days') and len(days) != f['days']:
        fails.append('%d days, the frame says %d' % (len(days), f['days']))
    nunits = f.get('units') or 0
    table = [r for r in (f.get('table') or []) if str(r.get('#', '')).strip().isdigit()]
    want = {r['#'].strip(): int(re.findall(r'\d+', r.get('Days', '0'))[0]) for r in table if re.findall(r'\d+', r.get('Days', ''))}
    got, kinds_in = {}, {}
    for d in days:
        lab = 'day %s' % d['day']
        s = d['stretch'].strip()
        if s == 'C':
            if d['unit'].strip():
                fails.append('%s: a course-level day leaves unit blank' % lab)
        elif not (s.isdigit() and 1 <= int(s) <= nunits):
            fails.append('%s: stretch "%s" is not a unit 1 to %d or C' % (lab, s, nunits))
        else:
            got[s] = got.get(s, 0) + 1
            kinds_in.setdefault(s, []).append(d)
        if d['kind'] not in KINDS:
            fails.append('%s: kind "%s" is not one of %s' % (lab, d['kind'], ', '.join(sorted(KINDS))))
        if d['assess'] not in ASSESS:
            fails.append('%s: assess "%s" is not one of %s' % (lab, d['assess'], ', '.join(sorted(a for a in ASSESS if a))))
        if not d['goal'].strip():
            fails.append('%s: no goal' % lab)
        if d.get('school_day', '').strip() and not d['school_day'].strip().isdigit():
            fails.append('%s: school_day "%s" is not a number' % (lab, d['school_day']))
    for u, n in want.items():
        if got.get(u, 0) != n:
            fails.append('unit %s: %d days, the frame says %d' % (u, got.get(u, 0), n))
    for u, ds in sorted(kinds_in.items(), key=lambda kv: int(kv[0])):
        if not any(d['assess'] == 'end' or (d['assess'] == 'observe' and frame.COURSE_META.get(slug, ('', ''))[1] in ('K', '1', '2'))
                   for d in ds):
            fails.append('unit %s: no end-of-unit assessment day (assess = end; K to 2 may use observe)' % u)
        if len(ds) > MID_UNIT_DAYS and not any(d['assess'] == 'mid' for d in ds):
            fails.append('unit %s: %d days and no mid-unit assessment (assess = mid)' % (u, len(ds)))
    # each course-level check is followed by a respond day before the next unit day
    for i, d in enumerate(days):
        if d['stretch'] == 'C' and d['kind'] == 'Check':
            nxt = next((x for x in days[i + 1:] if x['kind'] != 'Check' or x['stretch'] != 'C'), None)
            if nxt is None or not (nxt['stretch'] == 'C' and nxt['kind'] == 'Respond'):
                fails.append('day %s: a course-level check with no respond day after it' % d['day'])
    # readiness timing (Cory, 2026-11-14, sequence-write.md rule 2): a readiness check is given before its unit
    # opens, in the last ten minutes of the previous unit's last day or of a respond day between the two units, a few
    # days ahead at most; a unit 1 check is served by the start-of-year check; never on a unit's first day
    firsts = {}
    for i, d in enumerate(days):
        s = d['stretch'].strip()
        if s.isdigit() and s not in firsts:
            firsts[s] = i
    starts = sorted(firsts.values())
    for i, d in enumerate(days):
        if d['assess'] != 'readiness':
            continue
        s = d['stretch'].strip()
        if i in starts:
            fails.append("day %s: a readiness check on unit %s's first day (give it before the unit opens: the last "
                         "ten minutes of the previous unit's last day or of the respond day between; unit 1: the "
                         "start-of-year check)" % (d['day'], s))
            continue
        nxt = next((j for j in starts if j > i), None)
        closes = s == 'C' or d['kind'] == 'Respond' or i + 1 >= len(days) or days[i + 1]['stretch'].strip() != s
        if nxt is None or nxt - i > READINESS_AHEAD or not closes:
            fails.append("day %s: a readiness check that is not on the previous unit's last day or a respond day "
                         "within %d days before a unit's first day" % (d['day'], READINESS_AHEAD))
    # every owned skill and code of the frame is placed on some day
    placed = ' '.join(d['skills'] + ' ' + d['codes'] for d in days)
    for r in table:
        for sk in [x.strip() for x in re.split(r'[;,]', r.get('Skills', '')) if x.strip()]:
            if re.fullmatch(r'[\w-]+', sk) and sk not in placed:
                fails.append('unit %s: owned skill %s is on no day' % (r['#'], sk))
        for c in [x.strip() for x in r.get('Owned standards', '').split(';') if x.strip()]:
            c = c.split()[0].lstrip('~')
            if not re.search(r'(?<![\w.-])%s(?![\w-])' % re.escape(c), placed):
                notes.append('unit %s: standard %s is on no day' % (r['#'], c))
    return fails, notes


def main(a):
    if a[:1] != ['check']:
        raise SystemExit(__doc__)
    cs = a[1:2] or [p.name for p in sorted(PLANS.iterdir()) if p.is_dir() and stage(p.name) == 'scope']
    bad = 0
    for c in cs:
        fl, nt = check(c)
        print('sequence %s: %d failure(s)' % (c, len(fl)))
        for x in fl: print('  FAIL', x)
        for x in nt: print('  note', x)
        bad += len(fl)
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main(sys.argv[1:])

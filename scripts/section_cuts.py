"""Section boundaries for units still held as one placeholder section (the days.csv `unit` column; `stretch` is
the unit, `unit` is the section, docs/GLOSSARY.md).

    python -X utf8 scripts/section_cuts.py list [<course>...]           units still one section and longer than 6 days
    python -X utf8 scripts/section_cuts.py brief <course> <out.md>      compact brief for the agent that proposes cuts
    python -X utf8 scripts/section_cuts.py check <proposals.csv>        gates on a proposals file, writes nothing
    python -X utf8 scripts/section_cuts.py apply <proposals.csv> [--dry]   writes the cuts (only rows with status ok)
    python -X utf8 scripts/section_cuts.py headers [<course>...] [--dry]  re-sync every unit plan's "Sections: ..."
                                                                       header part from days.csv (safe to re-run)

Proposals CSV columns: course,unit,section,first,last,title,status,why
  status is `ok` (apply), or `decide` (a judgement call left for the lead; never applied).
Gates (check and apply): every unit in the file is covered day by day with no gap or overlap, sections are numbered
N.1, N.2 ... in day order, each is 1 to 6 days unless `why` starts with "long:" (a run that should not be cut, for
example one investigation), an end check (assess `end`) followed by teaching in a later section is printed as a NOTE (ELA scores end parts across
its closing weeks; it does not block), no Understanding day follows a mid check (assess
`mid`) inside its section, and no section is a lone Respond day.
Apply rewrites the `unit` column of days.csv and items.csv (by day), the "Sections: ..." part of the unit plan's
header line (docs/courses/<course>/sNN.md), and stops on parts.csv rows that name a split placeholder (those need a
section each, by hand). CSVs keep UTF-8 without BOM and their line endings.
"""
import csv, io, re, sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLANS = ROOT / 'data' / 'plans'
DOCS = ROOT / 'docs' / 'courses'
SKIP = {'math-4'}
MAXLEN = 6


def read_csv(p):
    raw = p.read_bytes().decode('utf-8')
    nl = '\r\n' if '\r\n' in raw else '\n'
    r = csv.DictReader(io.StringIO(raw))
    return r.fieldnames, list(r), nl


def write_csv(p, fields, rows, nl):
    b = io.StringIO()
    w = csv.DictWriter(b, fieldnames=fields, lineterminator=nl)
    w.writeheader()
    w.writerows(rows)
    p.write_bytes(b.getvalue().encode('utf-8'))


def days(course):
    return read_csv(PLANS / course / 'days.csv')[1]


def units_of(rows):
    us = defaultdict(list)
    for r in rows:
        if r['stretch'].isdigit():
            us[int(r['stretch'])].append(r)
    return us


def todo(course):
    """[(unit, rows)] for units still one section and longer than MAXLEN days."""
    out = []
    for u, rs in sorted(units_of(days(course)).items()):
        if len({r['unit'] for r in rs}) == 1 and len(rs) > MAXLEN:
            out.append((u, rs))
    return out


def courses():
    return sorted(p.parent.name for p in PLANS.glob('*/days.csv') if p.parent.name not in SKIP)


def cut(s, n):
    s = ' '.join(s.split())
    return s if len(s) <= n else s[:n - 3].rstrip() + '...'


def plan_bits(course, u):
    p = DOCS / course / ('s%02d.md' % u)
    if not p.exists():
        return None, [], []
    t = p.read_text(encoding='utf-8')
    head = next((l for l in t.splitlines() if l.startswith('# ')), '')
    prop = [l.strip() for l in t.splitlines() if re.search(r'[Pp]roposed section|section breaks?', l)][:3]
    # lines that place a mid-unit check or a long run (lab, investigation, project, seminar, essay drafting)
    hits = []
    for l in t.split('## Day list')[0].splitlines():
        if re.search(r'\bmid-unit\b|\bmid check\b|\binvestigation\b|\bproject\b|\bseminar\b|\bdebate\b|\bdraft', l, re.I) \
                and re.search(r'\bdays? \d', l):
            hits.append(cut(l.strip('-* '), 220))
    return head, prop, hits[:8]


def brief(course):
    w = []
    for u, rs in todo(course):
        head, prop, hits = plan_bits(course, u)
        w.append('## %s unit %d (%s), days %s to %s, %d days, now one section %s'
                 % (course, u, cut(head[2:], 90) if head else 'no plan', rs[0]['day'], rs[-1]['day'], len(rs), rs[0]['unit']))
        for l in prop:
            w.append('Plan proposes: ' + cut(l, 400))
        for l in hits:
            w.append('Plan mentions: ' + l)
        w.append('')
        w.append('| day | kind | assess | goal | note |')
        w.append('|---|---|---|---|---|')
        for r in rs:
            extra = ' [lab/tools]' if (r.get('tools') or r.get('supplies') or r.get('safety')) else ''
            w.append('| %s | %s | %s | %s | %s%s |' % (r['day'], r['kind'], r['assess'], cut(r['goal'], 140),
                                                     cut(r['note'], 160), extra))
        w.append('')
    return '\n'.join(w)


def load_props(p):
    return read_csv(Path(p))[1]


def gate(props):
    """Errors as strings; plan is {(course, unit): [(section, first, last, title)]} for status ok units."""
    errs, plan = [], defaultdict(list)
    by = defaultdict(list)
    for r in props:
        by[(r['course'], int(r['unit']))].append(r)
    cache = {}
    for (c, u), rs in sorted(by.items()):
        if any(r['status'] != 'ok' for r in rs):
            continue
        if c not in cache:
            cache[c] = units_of(days(c))
        drs = cache[c].get(u)
        if not drs:
            errs.append('%s unit %d: no such unit' % (c, u)); continue
        if len({r['unit'] for r in drs}) != 1:
            errs.append('%s unit %d: already split in days.csv' % (c, u)); continue
        dn = [int(r['day']) for r in drs]
        kind = {int(r['day']): r['kind'] for r in drs}
        ass = {int(r['day']): r['assess'] for r in drs}
        rs = sorted(rs, key=lambda r: int(r['first']))
        pos = {d: i for i, d in enumerate(dn)}   # a unit's days need not be one block (e.g. a later look-back day)
        at = 0
        for i, r in enumerate(rs, 1):
            f, l = int(r['first']), int(r['last'])
            name = '%s unit %d section %s' % (c, u, r['section'])
            if r['section'] != '%d.%d' % (u, i):
                errs.append('%s: should be numbered %d.%d' % (name, u, i))
            if f not in pos or l not in pos or pos[l] < pos[f]:
                errs.append('%s: days %d to %d are not days of the unit in order' % (name, f, l)); at = None; break
            if pos[f] != at:
                errs.append('%s: starts day %d, expected %d (gap or overlap)' % (name, f, dn[at] if at < len(dn) else -1))
            span = dn[pos[f]:pos[l] + 1]
            n = len(span)
            if n > MAXLEN and not r['why'].lower().startswith('long:'):
                errs.append('%s: %d days (1 to %d, or why "long: ...")' % (name, n, MAXLEN))
            if all(kind.get(d) == 'Respond' for d in span):
                errs.append('%s: a lone Respond section' % name)
            last = (i == len(rs))
            for j, d in enumerate(span):
                if ass.get(d) == 'end' and not last and not all(
                        kind.get(e) in ('Check', 'Respond') or ass.get(e) in ('end', 'observe', 'course')
                        or e != dn[pos[e] - 1] + 1 for e in dn[pos[l] + 1:]):
                    print('NOTE %s: day %d is an end check before teaching days in a later section' % (name, d))
                if ass.get(d) == 'mid' and any(kind.get(e) == 'Understanding' for e in span[j + 1:]):
                    errs.append('%s: new teaching after the day %d mid check in the same section' % (name, d))
            at = pos[l] + 1
        if at is not None and at != len(dn):
            errs.append('%s unit %d: sections stop before the unit ends (day %d)' % (c, u, dn[-1]))
        plan[(c, u)] = [(r['section'], int(r['first']), int(r['last']), r['title']) for r in rs]
    return errs, plan


def apply(plan, dry):
    for c in sorted({c for c, _ in plan}):
        mine = {u: secs for (cc, u), secs in plan.items() if cc == c}
        sec_of = {}
        old = {}
        for u, secs in mine.items():
            dn = [int(r['day']) for r in units_of(days(c))[u]]
            for s, f, l, _ in secs:
                for d in dn[dn.index(f):dn.index(l) + 1]:
                    sec_of[d] = s
        pf = PLANS / c / 'parts.csv'
        if pf.exists():
            fields, rows, _ = read_csv(pf)
            for r in rows:
                if r.get('stretch', '').isdigit() and int(r['stretch']) in mine and r.get('unit', '').endswith('.1'):
                    raise SystemExit('%s parts.csv names placeholder %s for %s: give it a section by hand first'
                                     % (c, r['unit'], r['code']))
        for name in ('days.csv', 'items.csv'):
            p = PLANS / c / name
            if not p.exists():
                continue
            fields, rows, nl = read_csv(p)
            n = 0
            for r in rows:
                d = r.get('day', '')
                if d.isdigit() and int(d) in sec_of and r['unit'] != sec_of[int(d)]:
                    old[r['unit']] = 1
                    r['unit'] = sec_of[int(d)]
                    n += 1
            print('%s %s: %d rows %s' % (c, name, n, 'would change' if dry else 'changed'))
            if not dry and n:
                write_csv(p, fields, rows, nl)
        if not dry:
            headers([c], dry)


def headers(cs, dry):
    """Rewrite the 'Sections: ...' part of each unit plan header from days.csv; reports only changes."""
    for c in cs:
        for u, rs in sorted(units_of(days(c)).items()):
            p = DOCS / c / ('s%02d.md' % u)
            if not p.exists():
                continue
            secs = []
            for r in rs:
                if secs and secs[-1][0] == r['unit']:
                    secs[-1][2] = r['day']
                else:
                    secs.append([r['unit'], r['day'], r['day']])
            new = 'Sections: ' + '; '.join('%s (days %s to %s)' % tuple(s) for s in secs) + '.'
            t = p.read_text(encoding='utf-8')
            t2, k = re.subn(r'Sections: .*?\.(?= Days by kind)', lambda m: new, t, count=1)
            if not k:
                print('%s s%02d.md: no "Sections: ... Days by kind" header, fix by hand' % (c, u))
            elif t2 != t:
                print('%s s%02d.md header %s' % (c, u, 'would change' if dry else 'synced'))
                if not dry:
                    p.write_bytes(t2.encode('utf-8'))


def main(a):
    if not a or a[0] in ('-h', '--help'):
        print(__doc__); return 0
    if a[0] == 'list':
        tot = 0
        for c in (a[1:] or courses()):
            t = todo(c)
            if t:
                tot += len(t)
                print('%-46s %2d units: %s' % (c, len(t), ', '.join('%d (%d days)' % (u, len(rs)) for u, rs in t)))
        print('total', tot)
        return 0
    if a[0] == 'headers':
        headers([x for x in a[1:] if x != '--dry'] or courses(), '--dry' in a)
        return 0
    if a[0] == 'brief':
        Path(a[2]).write_text(brief(a[1]), encoding='utf-8', newline='\n')
        print('wrote', a[2], len(todo(a[1])), 'units')
        return 0
    if a[0] in ('check', 'apply'):
        props = load_props(a[1])
        errs, plan = gate(props)
        dec = sorted({(r['course'], r['unit']) for r in props if r['status'] != 'ok'})
        for e in errs:
            print('FAIL', e)
        print('%d units gated, %d left to decide, %d failures' % (len(plan), len(dec), len(errs)))
        if errs:
            return 1
        if a[0] == 'apply':
            apply(plan, '--dry' in a)
        return 0
    print(__doc__)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

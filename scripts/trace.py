"""Walk the curriculum index up and down from one code, skill or day (pedagogy-architecture review change 5, 2026-11-25).

    python -X utf8 scripts/trace.py <code>                 3.OA.A.1, 4-ESS2-1
    python -X utf8 scripts/trace.py <skill>                sk-push-pull, s4-weathering-erosion (or prog:<subject>:<id>)
    python -X utf8 scripts/trace.py <course> <day>         science-grade-4 57
    python -X utf8 scripts/trace.py ... --all              every line, not the first 12 of each list

Reads data/index.db (rebuilt first when stale, as index.py does). The chain, top to bottom:

    code  <-owns-  skill  <-teaches-  unit (frame)  <-in-unit-  day  <-on-day-  item
                   skill  -assumes->  earlier skill;  skill -leans-cross-> another subject's code or skill
    day's ledger rows <-reviews- later rows that cite them

Up is toward the standard (what this rests on); down is toward the days and items (what rests on this).
"""
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
import index  # noqa: E402

CAP = 12


class G:
    def __init__(self):
        if index.stale():
            index.save(index.build())
        con = sqlite3.connect(index.DB)
        self.nodes = {k: v for k, *v in con.execute('select key, type, course, local, path, line, state from nodes')}
        self.out, self.inn = {}, {}
        for s, d, kind in con.execute('select src, dst, kind from edges'):
            self.out.setdefault(s, []).append((kind, d))
            self.inn.setdefault(d, []).append((kind, s))
        con.close()

    def to(self, k, kind):
        return sorted({d for kd, d in self.out.get(k, []) if kd == kind})

    def frm(self, k, kind):
        return sorted({s for kd, s in self.inn.get(k, []) if kd == kind})


def show(title, keys, full):
    if not keys:
        return
    print('  %s (%d):' % (title, len(keys)))
    for k in keys[:None if full else CAP]:
        print('    ' + k)
    if not full and len(keys) > CAP:
        print('    ... %d more (--all)' % (len(keys) - CAP))


def skills_of(g, k):
    return [k] if k.startswith('prog:') else []


def trace_code(g, code, full):
    k = 'code:' + code
    if k not in g.nodes and k not in g.inn:
        sys.exit('no code %s in the index' % code)
    sk = g.frm(k, 'owns')
    print('code %s' % code)
    print(' up:')
    print('  (a standard code is the top of the chain)')
    print(' down:')
    show('skills that own it', sk, full)
    show('skills of another subject that lean on it', g.frm(k, 'leans-cross'), full)
    units = sorted({u for s in sk for u in g.frm(s, 'teaches')})
    show('units whose frame teaches those skills', units, full)
    show('days that cite the code', [d for d in g.frm(k, 'code') if d.startswith('day:')], full)
    show('items that cite the code', [d for d in g.frm(k, 'code') if d.startswith('item:')], full)


def trace_skill(g, sid, full):
    k = sid if sid.startswith('prog:') else next((x for x in g.nodes if x.startswith('prog:') and x.endswith(':' + sid)), '')
    if not k:
        sys.exit('no skill %s in the index' % sid)
    print('skill %s' % k)
    print(' up:')
    show('codes it owns', g.to(k, 'owns'), full)
    show('skills it assumes', g.to(k, 'assumes'), full)
    show('other subjects it leans on', g.to(k, 'leans-cross'), full)
    print(' down:')
    show('units whose frame teaches it', g.frm(k, 'teaches'), full)
    show('days that name it', g.frm(k, 'skill'), full)
    show('skills that assume it', g.frm(k, 'assumes'), full)
    show('skills of another subject that lean on it', g.frm(k, 'leans-cross'), full)


def trace_day(g, course, n, full):
    k = 'day:%s:d%03d' % (course, n)
    if k not in g.nodes:
        sys.exit('no day %d in %s (days.csv)' % (n, course))
    v = g.nodes[k]
    sec = [x for x in g.nodes if x.startswith('section:%s:' % course)]
    print('day %s %d (data at %s:%s)' % (course, n, v[3], v[4]))
    print(' up:')
    units = g.to(k, 'in-unit')
    show('unit', units, full)
    for u in units:
        show('  skills that unit teaches (frame)', g.to(u, 'teaches'), full)
    show('codes the day cites', g.to(k, 'code'), full)
    sk = g.to(k, 'skill')
    show('skills the day names', sk, full)
    show('  codes those skills own', sorted({c for s in sk for c in g.to(s, 'owns')}), full)
    files = g.frm(k, 'is-day')
    for f in files:
        show('leans_on of ' + f[5:], [d[5:] if d.startswith('path:') else d for d in g.to(f, 'leans_on')], full)
    print(' down:')
    show('day file', [f[5:] for f in files], full)
    show('items on the day', g.frm(k, 'on-day'), full)
    rows = sorted(x for x in g.nodes if x.startswith('row:%s:' % course) and re.match(r'row:[^:]+:[^:]+:%d:' % n, x))
    show('ledger rows of the day', rows, full)
    show('later ledger rows that review them', sorted({s for r in rows for s in g.frm(r, 'reviews')}), full)
    show('words the day introduces', g.to(k, 'introduces'), full)
    show('plans and days that mention it', sorted(s[5:] if s.startswith('file:') else s for s in g.frm(k, 'mentions')), full)
    del sec


def main(a):
    full = '--all' in a
    a = [x for x in a if x != '--all']
    if not a:
        print(__doc__)
        return 2
    g = G()
    if len(a) == 2 and a[1].lstrip('d').isdigit():
        trace_day(g, a[0], int(a[1].lstrip('d')), full)
    elif a[0].startswith('code:') or ('code:' + a[0]) in g.inn or ('code:' + a[0]) in g.nodes:
        trace_code(g, a[0].replace('code:', '', 1), full)
    else:
        trace_skill(g, a[0], full)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

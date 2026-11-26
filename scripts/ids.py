"""Retired ids and the id registry (consolidation 4.H).

    python -X utf8 scripts/ids.py check          fail a retired id that is live again, a bad row in ids-retired.csv, or
                                                 an item, day or source id that left its table since the last commit
                                                 with no retire row
    python -X utf8 scripts/ids.py --self-test
    python -X utf8 scripts/ids.py retire <old_id> [<new_id>] --reason "..."   append one row (the only way to write it)
    python -X utf8 scripts/ids.py registry       write data/ids-registry.csv (ignored): every live id and every alias

Ids use the index's node keys (scripts/index.py): item:<course>:<item_id>, day:<course>:d012, unit:<course>:3,
section:<course>:3.2, piece:<course>:<section>/<name>.md, prog:<subject>:<id>, course:<id>, and so on.
data/ids-retired.csv is committed and append-only: old_id, new_id (blank when the id is gone, not merged), date,
reason. The registry is generated from the index plus that file and never committed.
"""
import csv
import datetime
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
RETIRED = ROOT / 'data' / 'ids-retired.csv'
REGISTRY = ROOT / 'data' / 'ids-registry.csv'
COLS = ['old_id', 'new_id', 'date', 'reason']


def retired():
    with open(RETIRED, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def live():
    import index
    if not index.DB.exists():
        index.save(index.build())
    con = sqlite3.connect(index.DB)
    try:
        return {k: (t, p) for k, t, p in con.execute('select key, type, path from nodes')}
    finally:
        con.close()


def check():
    lines, nodes, seen = [], live(), set()
    for i, r in enumerate(retired(), 2):
        old, new = r['old_id'], r['new_id']
        if not old or ':' not in old:
            lines.append('FAIL data/ids-retired.csv:%d: old_id "%s" is not an index key (kind:course:local)' % (i, old))
        if old in seen:
            lines.append('FAIL data/ids-retired.csv:%d: %s is retired twice' % (i, old))
        seen.add(old)
        if old in nodes:
            lines.append('FAIL %s: retired on %s, but it is live again (%s); a retired id is never reused'
                         % (old, r['date'], nodes[old][1] or nodes[old][0]))
        if new and new not in nodes:
            lines.append('note %s: merged into %s, which is not live' % (old, new))
    return lines


TABLES = (('items.csv', 'item_id', 'item:{c}:{v}'), ('days.csv', 'day', 'day:{c}:d{v:0>3}'),
          ('sources.csv', 'source_id', 'source:{c}:{v}'))


def table_ids(text, c, col, key):
    """Index keys for the ids of one course table's text."""
    if not text:
        return set()
    out = set()
    for r in csv.DictReader(ln for ln in text.splitlines() if not ln.startswith('#')):
        v = (r.get(col) or '').strip()
        if v:
            out.add(key.format(c=c, v=v))
    return out


def dropped(committed, now, retired_ids):
    """Ids a table held at the last commit that it holds no longer, with no ids.py retire row (goal test 11)."""
    return sorted(committed - now - retired_ids)


def left_tables():
    """FAIL lines for each id that left a course table since the last commit without `ids.py retire`. It runs in a
    writer's gate before the commit, which is where a deletion can still be seen (close review, goal test 11)."""
    import subprocess
    gone = {r['old_id'] for r in retired()}
    lines = []
    for p in sorted((ROOT / 'data' / 'plans').glob('*/')):
        c = p.name
        for name, col, key in TABLES:
            rel = 'data/plans/%s/%s' % (c, name)
            old = subprocess.run(['git', 'show', 'HEAD:' + rel], cwd=ROOT, capture_output=True, text=True,
                                 encoding='utf-8').stdout
            if not old:
                continue
            new = (ROOT / rel).read_text(encoding='utf-8') if (ROOT / rel).exists() else ''
            if new == old:
                continue
            for k in dropped(table_ids(old, c, col, key), table_ids(new, c, col, key), gone):
                lines.append('FAIL %s: left %s since the last commit with no data/ids-retired.csv row (ids.py retire)'
                             % (k, rel))
    return lines


def self_test():
    old = table_ids('item_id,stem\na1,x\na2,y\n', 'c', 'item_id', 'item:{c}:{v}')
    new = table_ids('item_id,stem\na1,x\n', 'c', 'item_id', 'item:{c}:{v}')
    ok = dropped(old, new, set()) == ['item:c:a2'] and dropped(old, new, {'item:c:a2'}) == []
    ok = ok and table_ids('day,goal\n7,g\n', 'c', 'day', 'day:{c}:d{v:0>3}') == {'day:c:d007'}
    print('ids self-test: %s' % ('all passed' if ok else 'FAILED'))
    return 0 if ok else 1


def retire(a):
    if not a or '--reason' not in a:
        raise SystemExit(__doc__)
    reason = a[a.index('--reason') + 1]
    pos = [x for x in a[:a.index('--reason')]]
    old, new = pos[0], (pos[1] if len(pos) > 1 else '')
    if any(r['old_id'] == old for r in retired()):
        raise SystemExit('ids: %s is already retired' % old)
    import safe_write
    with safe_write.lock(RETIRED):
        with open(RETIRED, 'a', encoding='utf-8', newline='') as f:
            csv.writer(f, lineterminator='\n').writerow([old, new, datetime.date.today().isoformat(), reason])
    print('retired %s%s' % (old, ' -> ' + new if new else ''))
    return 0


def registry():
    nodes = live()
    with open(REGISTRY, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, lineterminator='\n')
        w.writerow(['id', 'type', 'path', 'alias_of'])
        for k in sorted(nodes):
            w.writerow([k, nodes[k][0], nodes[k][1] or '', ''])
        for r in retired():
            w.writerow([r['old_id'], 'retired', '', r['new_id']])
    print('registry: %d live ids, %d retired -> %s' % (len(nodes), len(retired()), REGISTRY.relative_to(ROOT)))
    return 0


def main(a):
    if a[:1] == ['--self-test']:
        return self_test()
    if a[:1] == ['check']:
        lines = check() + left_tables()
        print('\n'.join(lines))
        print('ids: %d retired id(s) checked, %d line(s)' % (len(retired()), len(lines)))
        return 1 if any(ln.startswith('FAIL') for ln in lines) else 0
    if a[:1] == ['retire']:
        return retire(a[1:])
    if a[:1] == ['registry']:
        return registry()
    raise SystemExit(__doc__)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

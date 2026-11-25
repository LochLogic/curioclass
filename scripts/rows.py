"""The one safe way to write a row of a course's plan CSV (consolidation step 4.D).

    python -X utf8 scripts/rows.py upsert <course> <table> --key <col>[,<col>...] <col>=<value> ... [--dry-run]

<table> is a file of data/plans/<course>/ without .csv (items, wrongs, days, materials, handbacks, sources, ...).
The row whose --key columns equal the given values is updated (only the columns given change); with no such row a new
row is appended (columns not given are blank). Every key column must be given, every column must already be in the
file's header, and a key that matches two rows is refused. The file is read whole, then written through a temp file
and os.replace; only the changed or added record's text changes, so every other line, its quoting and its line ending
stay byte for byte. --dry-run prints the change and writes nothing. The ledger has its own command (scripts/ledger.py).
"""
import csv
import io
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLANS = Path(os.environ['ROWS_PLANS']) if os.environ.get('ROWS_PLANS') else ROOT / 'data' / 'plans'


def records(text):
    """[(raw text of the record including its line ending, parsed fields)], header first."""
    lines = text.splitlines(keepends=True)
    out, buf = [], []
    for ln in lines:
        buf.append(ln)
        joined = ''.join(buf)
        try:
            parsed = next(csv.reader(io.StringIO(joined), strict=True))
        except (csv.Error, StopIteration):
            continue
        if joined.count('"') % 2:        # an open quoted field spans the line break
            continue
        out.append((joined, parsed))
        buf = []
    if buf:
        raise SystemExit('rows: the file ends inside a quoted field')
    return out


def line(fields, nl):
    s = io.StringIO()
    csv.writer(s, lineterminator=nl).writerow(fields)
    return s.getvalue()


def upsert(course, table, key, values, dry=False):
    p = PLANS / course / (table + '.csv')
    if not p.exists():
        raise SystemExit('rows: %s does not exist (rows.py never makes a new table)' % p)
    text = p.read_bytes().decode('utf-8')
    recs = records(text)
    head = recs[0][1]
    nl = '\r\n' if recs[0][0].endswith('\r\n') else '\n'
    bad = sorted({c for c in list(values) + key if c not in head})
    if bad:
        raise SystemExit('rows: not in the header of %s: %s' % (p.name, ', '.join(bad)))
    miss = [k for k in key if k not in values]
    if miss:
        raise SystemExit('rows: give a value for every key column: %s' % ', '.join(miss))
    ix = [head.index(k) for k in key]
    hits = [i for i, (_, f) in enumerate(recs[1:], 1) if [f[j] if j < len(f) else '' for j in ix] == [values[k] for k in key]]
    if len(hits) > 1:
        raise SystemExit('rows: key %s matches %d rows in %s; refused' % (values, len(hits), p.name))
    if hits:
        i = hits[0]
        old = recs[i][1] + [''] * (len(head) - len(recs[i][1]))
        new = list(old)
        for c, v in values.items():
            new[head.index(c)] = v
        if new == old:
            print('unchanged: %s %s %s' % (course, table, ', '.join('%s=%s' % (k, values[k]) for k in key)))
            return 0
        end = nl if recs[i][0].endswith(('\n', '\r')) else ''
        recs[i] = (line(new, nl)[:-len(nl)] + end, new)
        what = 'updated'
        diff = ['  %s: %r -> %r' % (c, o, n) for c, o, n in zip(head, old, new) if o != n]
    else:
        new = [values.get(c, '') for c in head]
        if recs[-1][0] and not recs[-1][0].endswith(('\n', '\r')):
            recs[-1] = (recs[-1][0] + nl, recs[-1][1])
        recs.append((line(new, nl), new))
        what = 'added'
        diff = ['  ' + ', '.join('%s=%s' % (c, v) for c, v in zip(head, new) if v)]
    print('%s%s: %s %s' % ('dry run, would be ' if dry else '', what, course, table))
    print('\n'.join(diff))
    if dry:
        return 0
    tmp = p.with_name(p.name + '.tmp')
    tmp.write_bytes(''.join(r for r, _ in recs).encode('utf-8'))
    os.replace(tmp, p)
    return 0


def self_test():
    import tempfile
    global PLANS
    d = Path(tempfile.mkdtemp())
    (d / 'c').mkdir()
    f = d / 'c' / 't.csv'
    f.write_bytes(b'id,a,b\r\nx1,"one, two",\r\nx2,"multi\r\nline",z\r\n')
    PLANS = d
    upsert('c', 't', ['id'], {'id': 'x1', 'b': 'new'})
    assert f.read_bytes() == b'id,a,b\r\nx1,"one, two",new\r\nx2,"multi\r\nline",z\r\n', f.read_bytes()
    upsert('c', 't', ['id'], {'id': 'x3', 'a': 'q'})
    assert f.read_bytes().endswith(b'x3,q,\r\n')
    upsert('c', 't', ['id'], {'id': 'x2', 'a': 'flat'}, dry=True)
    assert b'flat' not in f.read_bytes()
    for bad in ({'id': 'x1', 'zz': '1'}, {'a': '1'}):
        try:
            upsert('c', 't', ['id'], bad)
            raise AssertionError('accepted %s' % bad)
        except SystemExit:
            pass
    print('rows.py self-test: all passed')
    return 0


def main(a):
    if a == ['--self-test']:
        return self_test()
    if len(a) < 4 or a[0] != 'upsert' or '--key' not in a:
        raise SystemExit(__doc__)
    dry = '--dry-run' in a
    a = [x for x in a if x != '--dry-run']
    course, table = a[1], a[2]
    k = a.index('--key')
    key = a[k + 1].split(',')
    rest = a[3:k] + a[k + 2:]
    values = {}
    for x in rest:
        if '=' not in x:
            raise SystemExit('rows: expected col=value, got %r' % x)
        c, v = x.split('=', 1)
        values[c] = v
    return upsert(course, table, key, values, dry)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

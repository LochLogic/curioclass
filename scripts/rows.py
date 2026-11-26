"""The one safe way to write a row of a course's plan CSV (consolidation steps 4.D and 4.E2).

    python -X utf8 scripts/rows.py upsert <course> <table> --key <col>[,<col>...] <col>=<value> ... [--value-file <col>=<file>] [--dry-run]
    python -X utf8 scripts/rows.py delete <course> <table> --key <col>[,<col>...] <col>=<value> ... [--dry-run]
    python -X utf8 scripts/rows.py check [<course> ...]     every plan CSV splits into the same records as Python's csv reader
    python -X utf8 scripts/rows.py --self-test

<table> is a file of data/plans/<course>/ without .csv (items, wrongs, days, materials, handbacks, sources, ...);
the course 'shared' with the table vocabulary writes data/plans/vocabulary.csv (the word table, 4.I).
upsert: the row whose --key columns equal the given values is updated (only the columns given change); with no such row
a new row is appended (columns not given are blank). delete: the one row with that key is removed. Every key column
must be given, every column must already be in the file's header, and a key that matches two rows is refused.
--value-file reads a value (for example one with line breaks) from a UTF-8 file. The file is read whole and written
through safe_write (a lock per file, a temp name per process); only the changed, added or removed record's text
changes, so every other line, its quoting and its line ending stay byte for byte. --dry-run prints the change and
writes nothing. The ledger is never written here: it has its own command (scripts/ledger.py).
"""
import csv
import io
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import safe_write  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PLANS = Path(os.environ['ROWS_PLANS']) if os.environ.get('ROWS_PLANS') else ROOT / 'data' / 'plans'
NAME = re.compile(r'[a-z0-9][a-z0-9_-]*')
SHARED = ('vocabulary',)   # cross-course tables at data/plans/<table>.csv, written as course 'shared'


def records(text):
    """[(raw text of the record including its line ending, parsed fields)], header first. Splits on line feeds only."""
    lines = re.split(r'(?<=\n)', text)
    if lines and lines[-1] == '':
        lines.pop()
    out, buf = [], []
    for ln in lines:
        buf.append(ln)
        joined = ''.join(buf)
        if joined.count('"') % 2:        # an open quoted field spans the line break
            continue
        try:
            parsed = list(csv.reader(io.StringIO(joined, newline=''), strict=True))
        except csv.Error:
            continue
        if len(parsed) != 1:
            continue
        out.append((joined, parsed[0]))
        buf = []
    if buf:
        raise SystemExit('rows: the file ends inside a quoted field')
    return out


def line(fields, nl):
    s = io.StringIO()
    csv.writer(s, lineterminator=nl).writerow(fields)
    return s.getvalue()


def target(course, table):
    if table == 'ledger':
        raise SystemExit('rows: the ledger is written only through scripts/ledger.py')
    if course == 'shared' and table in SHARED:   # a cross-course table: data/plans/<table>.csv (4.I)
        return PLANS / (table + '.csv')
    if not NAME.fullmatch(course) or not NAME.fullmatch(table):
        raise SystemExit('rows: course and table are plain names (no path separators): %r %r' % (course, table))
    p = PLANS / course / (table + '.csv')
    if not p.exists():
        raise SystemExit('rows: %s does not exist (rows.py never makes a new table)' % p)
    return p


def change(course, table, key, values, dry=False, remove=False):
    p = target(course, table)
    with safe_write.lock(p):
        text = safe_write.read_text(p)
        if text.startswith('﻿'):
            raise SystemExit('rows: %s starts with a byte order mark; remove it first' % p.name)
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
        hits = [i for i, (_, f) in enumerate(recs[1:], 1)
                if [f[j] if j < len(f) else '' for j in ix] == [values[k] for k in key]]
        if len(hits) > 1:
            raise SystemExit('rows: key %s matches %d rows in %s; refused' % (values, len(hits), p.name))
        keytext = ', '.join('%s=%s' % (k, values[k]) for k in key)
        if remove:
            if not hits:
                raise SystemExit('rows: no row with %s in %s' % (keytext, p.name))
            what, diff = 'deleted', ['  ' + recs[hits[0]][0].rstrip('\r\n')]
            del recs[hits[0]]
        elif hits:
            i = hits[0]
            old = recs[i][1] + [''] * (len(head) - len(recs[i][1]))
            new = list(old)
            for c, v in values.items():
                new[head.index(c)] = v
            if new == old:
                print('unchanged: %s %s %s' % (course, table, keytext))
                return 0
            end = nl if recs[i][0].endswith('\n') else ''
            recs[i] = (line(new, nl)[:-len(nl)] + end, new)
            what = 'updated'
            diff = ['  %s: %r -> %r' % (c, o, n) for c, o, n in zip(head, old, new) if o != n]
        else:
            new = [values.get(c, '') for c in head]
            if recs[-1][0] and not recs[-1][0].endswith('\n'):
                recs[-1] = (recs[-1][0] + nl, recs[-1][1])
            recs.append((line(new, nl), new))
            what = 'added'
            diff = ['  ' + ', '.join('%s=%s' % (c, v) for c, v in zip(head, new) if v)]
        print('%s%s: %s %s' % ('dry run, would be ' if dry else '', what, course, table))
        print('\n'.join(diff))
        if not dry:
            safe_write.replace(p, ''.join(r for r, _ in recs))
    return 0


def upsert(course, table, key, values, dry=False):
    return change(course, table, key, values, dry)


def check(courses):
    bad = n = 0
    files = [p for c in courses or sorted(x.name for x in PLANS.iterdir() if x.is_dir())
             for p in sorted((PLANS / c).glob('*.csv'))]
    if not courses:                            # the shared tables too (debt.csv, pass-marks.csv, later.csv, ...)
        files += sorted(PLANS.glob('*.csv'))
    for p in files:
        n += 1
        text = p.read_bytes().decode('utf-8')
        try:
            recs = records(text)
        except SystemExit as e:
            print('FAIL %s: %s' % (p.relative_to(PLANS).as_posix(), e))
            bad += 1
            continue
        ref = list(csv.reader(io.StringIO(text, newline='')))
        if ''.join(r for r, _ in recs) != text or [f for _, f in recs] != ref:
            print('FAIL %s: records differ from the csv reader' % p.relative_to(PLANS).as_posix())
            bad += 1
    print('rows check: %d files, %d problems' % (n, bad))
    return 1 if bad else 0


def _race_worker(d, k):
    global PLANS
    PLANS = Path(d)
    for i in range(20):
        upsert('c', 't', ['id'], {'id': 'w%s-%d' % (k, i), 'a': 'x'})


def self_test():
    import subprocess
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
    change('c', 't', ['id'], {'id': 'x3'}, remove=True)
    assert b'x3' not in f.read_bytes()
    for bad in (('c', 't', {'id': 'x1', 'zz': '1'}), ('c', 't', {'a': '1'}), ('c', 'ledger', {'id': 'x1'}),
                ('../c', 't', {'id': 'x1'}), ('c', 't', {'id': 'nope'})):
        try:
            change(bad[0], bad[1], ['id'], bad[2], remove=(bad[2] == {'id': 'nope'}))
            raise AssertionError('accepted %s' % (bad,))
        except SystemExit:
            pass
    procs = [subprocess.Popen([sys.executable, __file__, '--race-worker', str(d), str(k)],
                              stdout=subprocess.DEVNULL) for k in range(5)]
    assert [p.wait() for p in procs] == [0] * 5
    got = [r for _, r in records(f.read_bytes().decode('utf-8'))[1:] if r[0].startswith('w')]
    assert len(got) == 100, len(got)
    assert sorted(x.name for x in (d / 'c').iterdir()) == ['t.csv']
    print('rows.py self-test: all passed (5 processes x 20 upserts: 100 of 100 rows)')
    return 0


def main(a):
    if a == ['--self-test']:
        return self_test()
    if len(a) == 3 and a[0] == '--race-worker':
        _race_worker(a[1], a[2])
        return 0
    if a and a[0] == 'check':
        return check(a[1:])
    if len(a) < 4 or a[0] not in ('upsert', 'delete') or '--key' not in a:
        raise SystemExit(__doc__)
    dry = '--dry-run' in a
    a = [x for x in a if x != '--dry-run']
    course, table = a[1], a[2]
    k = a.index('--key')
    key = a[k + 1].split(',')
    rest = a[3:k] + a[k + 2:]
    values = {}
    i = 0
    while i < len(rest):
        x = rest[i]
        if x == '--value-file':
            c, _, fn = rest[i + 1].partition('=')
            values[c] = Path(fn).read_text(encoding='utf-8').rstrip('\r\n')
            i += 2
            continue
        if '=' not in x:
            raise SystemExit('rows: expected col=value, got %r' % x)
        c, v = x.split('=', 1)
        values[c] = v
        i += 1
    return change(course, table, key, values, dry, remove=(a[0] == 'delete'))


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

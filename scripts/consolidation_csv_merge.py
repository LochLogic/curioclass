"""Rebuild the CSVs both sides of the Codex draft merge changed, course by course (docs/CONSOLIDATION-PLAN.md step 2).

    python -X utf8 scripts/consolidation_csv_merge.py merge   during `git merge` in S:\\CurioClass-draft: writes the files
    python -X utf8 scripts/consolidation_csv_merge.py keys    duplicate-key check over the plan CSVs the draft touched

merge reads three versions of each shared CSV with git show: the merge base, HEAD (draft/codex) and MERGE_HEAD (main).
Rows are grouped by course. The draft owns only its lane courses (DRAFT_COURSES); every other course takes main's
rows, and any draft difference there is listed, not applied (the 2026-11-24 union merge bd20bc418 had dropped 64
planned rows of ELA kindergarten and grade 3 on the draft). A lane course takes the draft's rows, or main's when only
main changed it. A lane course changed on both sides is refused, except where ALLOW_BOTH names the rule:
math-kindergarten, where main seeded 83 unit-level planned rows (where s01 to s10) after the branch split and the
draft wrote section and day rows (where u..). Unit-level rows are never promoted by `ledger.py add` (it matches the
same where), and the ELA courses keep theirs beside their section rows, so both sets are kept: main's unit rows first,
then the draft's rows, the order the ELA ledger uses. Assertions: one header, no exact duplicate rows, ela-texts
text_id unique, each course's row count equal to its chosen side's.

keys checks one natural key per file type over every data/plans/*/*.csv changed on draft/codex since the merge base,
and reports a duplicate as new only when the base did not already have it.
"""
import collections
import csv
import io
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHARED = ['data/plans/ela-texts.csv', 'data/plans/ledgers/ela.csv', 'data/plans/ledgers/math.csv',
          'data/plans/ledgers/science.csv', 'data/plans/ledgers/social-studies.csv']
DRAFT_COURSES = {'english-language-arts-grade-4', 'math-kindergarten', 'science-grade-4', 'science-grade-5',
                 'social-studies-grade-4', 'social-studies-grade-5'}
ALLOW_BOTH = {('data/plans/ledgers/math.csv', 'math-kindergarten')}
norm = lambda t: re.sub(r'\s+', ' ', t.strip().lower())
FILE_KEYS = {'days': ['day'], 'errors': ['stretch', 'letter'], 'handbacks': ['from_day', 'to_day', 'what'],
             'items': ['item_id'], 'materials': ['material'], 'parts': ['code', 'part'], 'source-map': ['source'],
             'sources': ['source_id'], 'wordlist': ['unit', 'word'], 'words': ['pattern'],
             'wrongs': ['item_id', 'shown'], 'ledger': ['course', 'where', 'day', 'kind', 'entry']}


def git(*a):
    p = subprocess.run(['git', *a], cwd=ROOT, capture_output=True)
    return p.stdout.decode('utf-8') if p.returncode == 0 else None


def table(text):
    if not text:
        return None, []
    rows = list(csv.reader(io.StringIO(text, newline='')))
    return rows[0], rows[1:]


def by_course(header, rows):
    ci = header.index('course')
    d = collections.OrderedDict()
    for r in rows:
        d.setdefault(r[ci], []).append(r)
    return d


def merge():
    base = git('merge-base', 'HEAD', 'MERGE_HEAD').strip()
    for f in SHARED:
        bh, br = table(git('show', f'{base}:{f}'))
        dh, dr = table(git('show', f'HEAD:{f}'))
        mh, mr = table(git('show', f'MERGE_HEAD:{f}'))
        header = mh or dh
        assert all(h in (None, header) for h in (bh, dh, mh)), f'{f}: headers differ'
        B, D, M = (by_course(header, r) for r in (br, dr, mr))
        out, report = [], []
        for c in list(M) + [c for c in D if c not in M]:
            b, d, m = B.get(c, []), D.get(c, []), M.get(c, [])
            dch, mch = d != b, m != b
            if c not in DRAFT_COURSES:
                if dch:
                    gone = collections.Counter(map(tuple, b)) - collections.Counter(map(tuple, d))
                    extra = collections.Counter(map(tuple, d)) - collections.Counter(map(tuple, b))
                    report.append(f'  {c}: main kept; the draft differs from base by -{sum(gone.values())} '
                                  f'+{sum(extra.values())} rows (not a draft lane, not applied)')
                out += m
                continue
            if dch and mch:
                if (f, c) not in ALLOW_BOTH:
                    raise SystemExit(f'{f}: {c} changed on both sides; no rule for it')
                assert not b, f'{f}: {c} has base rows; the ALLOW_BOTH rule assumes none'
                wi = header.index('where')
                assert all(r[wi].startswith('s') for r in m) and not any(r[wi].startswith('s') for r in d), \
                    f'{f}: {c} rows are not split into main unit rows and draft section rows'
                rows, why = m + d, f'both: main {len(m)} unit rows + draft {len(d)} rows'
            elif dch:
                rows, why = d, f'draft ({len(b)} -> {len(d)})'
            elif mch:
                rows, why = m, f'main ({len(b)} -> {len(m)})'
            else:
                rows, why = m, None
            out += rows
            if why:
                report.append(f'  {c}: {why}')
        exact = collections.Counter(tuple(r) for r in out)
        assert not [k for k, v in exact.items() if v > 1], f'{f}: exact duplicate rows'
        assert header not in out, f'{f}: header repeated inside the rows'
        if f.endswith('ela-texts.csv'):
            ti = header.index('text_id')
            ids = collections.Counter(r[ti] for r in out)
            assert not [k for k, v in ids.items() if v > 1], f'{f}: duplicate text_id'
        buf = io.StringIO(newline='')
        csv.writer(buf, lineterminator='\n').writerows([header] + out)
        (ROOT / f).write_bytes(buf.getvalue().encode('utf-8'))
        print(f'{f}: {len(out)} rows (base {len(br)}, main {len(mr)}, draft {len(dr)})')
        print('\n'.join(report))


def dupes(header, rows, kind):
    cols = FILE_KEYS.get(kind)
    if not cols or not all(c in header for c in cols):
        return None
    idx = [header.index(c) for c in cols]
    c = collections.Counter(tuple(norm(r[i]) for i in idx) for r in rows)
    return {k for k, v in c.items() if v > 1}


def keys():
    base = git('merge-base', 'HEAD', 'origin/main').strip()
    files = git('diff', '--name-only', base, 'HEAD', '--', 'data/plans/*/*.csv').split()
    bad = 0
    for f in sorted(files):
        p = ROOT / f
        if not p.exists():
            continue
        kind = 'ledger' if '/ledgers/' in f else p.stem
        h, r = table(p.read_text(encoding='utf-8'))
        now = dupes(h, r, kind)
        if now is None:
            print(f'  no key rule: {f}')
            continue
        bh, br = table(git('show', f'{base}:{f}'))
        before = dupes(bh, br, kind) if bh else set()
        new = now - (before or set())
        print(f'{"NEW " if new else "ok  "} {f}: {len(r)} rows, {len(now)} duplicate keys ({len(new)} new)')
        for k in sorted(new)[:5]:
            print('       ', k)
        bad += bool(new)
    print(f'{len(files)} files checked; {bad} with new duplicate keys')
    return bad


if __name__ == '__main__':
    cmd = sys.argv[1:] or ['']
    if cmd[0] == 'merge':
        merge()
    elif cmd[0] == 'keys':
        sys.exit(1 if keys() else 0)
    else:
        raise SystemExit(__doc__)

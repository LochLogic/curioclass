"""Where every tool is in the pipeline, as data (consolidation step 5 item 1).

    python -X utf8 scripts/tool_stages.py seed [--dry-run]       write data/tool-stages.csv from today's file evidence
    python -X utf8 scripts/tool_stages.py set <tool_id> <stage> --record <path> [--date YYYY-MM-DD] [--dry-run]
    python -X utf8 scripts/tool_stages.py check                  every catalog tool has one row, a known stage and its
                                                                 record on disk; prints where the files disagree

data/tool-stages.csv (tool_id, stage, date, record) is the one home of a tool's stage. board.py (docs/BUILD-BOARD.md)
and desk_stats.py (the Desk's stats panel) read it instead of guessing from file names. `record` is the file that
proves the stage (repository path); `date` is when that record last changed in git. The step that moves a tool runs
`set` (the briefs say so when tool work resumes). Stages and their order are board.ORDER.

`check` also compares each row with board.infer(), the old file guess, and prints a line where they differ: the
CSV wins, and the line says which record to look at. Before seed, board.py fell back to the guess.
data/tools.csv (two rows, an older catalog schema) is not read by any script and is left alone: it is not a stage
record.
"""
import csv
import io
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
OUT = ROOT / 'data' / 'tool-stages.csv'
COLS = ['tool_id', 'stage', 'date', 'record']

# the record that proves each stage, in the order board.infer() reads them (first that exists wins)
PROOF = {'concept': ['data/tools-concepts.csv'], 'spec': ['spec.md'],
         'build': ['codex-report.md', 'tool.draft.json'], 'selfcheck': ['codex-review.md'],
         'refine': ['refine.md'], 'fix': ['polish.md'], 'exit': ['refine.md', 'verify.md'],
         'artvoice': ['refine.md', 'verify.md'], 'finish': ['final.md'], 'live': ['tool.json']}


def catalog():
    import board
    return [r['tool_id'] for r in csv.DictReader(open(ROOT / 'data' / 'tools-concepts.csv', encoding='utf-8'))] + \
        [r['tool_id'] for r in board.recess_rows()]


def proof(tid, stage):
    for name in PROOF[stage]:
        rel = name if '/' in name else 'tools/%s/%s' % (tid, name)
        if (ROOT / rel).exists():
            return rel
    return ''


def git_dates():
    """Last commit date (YYYY-MM-DD) of every file under tools/ and data/tools-concepts.csv, one git call."""
    out = subprocess.run(['git', 'log', '--format=@%ad', '--date=short', '--name-only', '--', 'tools',
                          'data/tools-concepts.csv'], cwd=ROOT, capture_output=True, text=True, encoding='utf-8').stdout
    seen, day = {}, ''
    for ln in out.splitlines():
        if ln.startswith('@'):
            day = ln[1:]
        elif ln and ln not in seen:
            seen[ln] = day
    return seen


def read():
    if not OUT.exists():
        return {}
    with open(OUT, encoding='utf-8', newline='') as f:
        return {r['tool_id']: r for r in csv.DictReader(f)}


def text(rows):
    s = io.StringIO()
    w = csv.DictWriter(s, COLS, lineterminator='\n')
    w.writeheader()
    w.writerows(sorted(rows.values(), key=lambda r: r['tool_id']))
    return s.getvalue()


def write(rows):
    import safe_write
    with safe_write.lock(OUT):
        safe_write.replace(OUT, text(rows))


def seed(dry):
    import board
    dates = git_dates()
    rows = {}
    for tid in catalog():
        st = board.infer(tid)['stage']
        rec = proof(tid, st)
        rows[tid] = {'tool_id': tid, 'stage': st, 'date': dates.get(rec, ''), 'record': rec}
    counts = {}
    for r in rows.values():
        counts[r['stage']] = counts.get(r['stage'], 0) + 1
    print('tool_stages: %s %d rows: %s' % ('would write' if dry else 'wrote', len(rows),
                                         ', '.join('%s %d' % (s, counts.get(s, 0)) for s in board.ORDER)))
    if not dry:
        write(rows)


def set_stage(a):
    import board
    import datetime
    tid, stage = a[1], a[2]
    if stage not in board.ORDER:
        raise SystemExit('tool_stages: unknown stage %r (one of %s)' % (stage, ', '.join(board.ORDER)))
    if tid not in catalog():
        raise SystemExit('tool_stages: %s is not in data/tools-concepts.csv or data/recess.json' % tid)
    rec = a[a.index('--record') + 1] if '--record' in a else ''
    if not rec or not (ROOT / rec).exists():
        raise SystemExit('tool_stages: --record must name a file that exists (the record that proves the stage)')
    day = a[a.index('--date') + 1] if '--date' in a else datetime.date.today().isoformat()
    rows = read()
    old = rows.get(tid)
    rows[tid] = {'tool_id': tid, 'stage': stage, 'date': day, 'record': rec}
    print('tool_stages: %s %s: %s -> %s (%s)' % ('would set' if '--dry-run' in a else 'set', tid,
                                               old['stage'] if old else 'no row', stage, rec))
    if '--dry-run' not in a:
        write(rows)


def check():
    import board
    rows = read()
    out = []
    if not rows:
        return ['FAIL data/tool-stages.csv is missing or empty (run tool_stages.py seed)']
    cat = catalog()
    for tid in cat:
        r = rows.get(tid)
        if r is None:
            out.append('FAIL %s: no row in data/tool-stages.csv' % tid)
            continue
        if r['stage'] not in board.ORDER:
            out.append('FAIL %s: unknown stage %r' % (tid, r['stage']))
        elif not r['record'] or not (ROOT / r['record']).exists():
            out.append('FAIL %s: stage %s, record %r is not on disk' % (tid, r['stage'], r['record']))
        else:
            guess = board.infer(tid)['stage']
            if guess != r['stage']:
                out.append('note %s: data says %s, the files look like %s (see %s)' % (tid, r['stage'], guess,
                                                                                  r['record']))
    for tid in sorted(set(rows) - set(cat)):
        out.append('FAIL %s: row in data/tool-stages.csv but not in the catalog or data/recess.json' % tid)
    return out


def main(a):
    if not a or a[0] not in ('seed', 'set', 'check'):
        print(__doc__)
        return 2
    if a[0] == 'seed':
        seed('--dry-run' in a)
        return 0
    if a[0] == 'set':
        set_stage(a)
        return 0
    lines = check()
    for ln in lines:
        print(ln)
    bad = sum(ln.startswith('FAIL') for ln in lines)
    print('tool_stages check: %d rows, %d problems, %d notes' % (len(read()), bad, len(lines) - bad))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

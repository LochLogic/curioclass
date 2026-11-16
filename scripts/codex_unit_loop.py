"""Write and refine unit plans with Codex: write, three lens reads, one fix, gates (2026-11-15 loop).

Usage: python -X utf8 scripts/codex_unit_loop.py <queue.txt> [logdir=PATH] [results=PATH] [tries=2]

The queue holds one job a line, worked in order: `<course> <units> <mode>`, where <units> is `all`, `N` or `N-M`
(the course's real unit numbers) and <mode> is `write` (write the unit with the subject's writer brief if
scripts/unitplan.py does not pass it, then refine) or `review` (refine only, for units already written). Refine is:
three Codex lens reads in parallel (docs/pipeline/briefs/unit-lens.md, lenses assessment, sources and sequence; they
edit nothing and their findings are their reports, docs/reviews/codex-write-lens-<lens>-<course>-sNN-<date>.md), then
one Codex fix (docs/pipeline/briefs/unit-lens-fix.md), then unitplan.py. A unit that cannot be made to pass stops its
course (later units build on it); the queue moves to its next line. Lines starting # are skipped.

Each step's time and result go to results (CSV: time, course, unit, step, seconds, exit, pass). Codex trouble (three
failed calls in a row) waits 20 minutes and tries once more; a fourth failure in a row ends the run, which is how an
exhausted token allowance shows. Logs go to logdir, never under docs/reviews.
"""
import concurrent.futures as cf
import csv
import datetime
import os
import subprocess
import sys
import tempfile
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = [sys.executable, '-X', 'utf8']
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import codex_units as cu  # noqa: E402

LENSES = ('assessment', 'sources', 'sequence')
LENS = 'docs/pipeline/briefs/unit-lens.md'
FIX = 'docs/pipeline/briefs/unit-lens-fix.md'


class Run:
    def __init__(self, logdir, results, tries):
        self.logdir, self.results, self.tries = logdir, results, tries
        self.fails = 0

    def note(self, course, uu, step, secs, code, ok):
        new = not os.path.exists(self.results)
        with open(self.results, 'a', newline='', encoding='utf-8') as f:
            w = csv.writer(f)
            if new:
                w.writerow(['time', 'course', 'unit', 'step', 'seconds', 'exit', 'pass'])
            w.writerow([datetime.datetime.now().isoformat(timespec='seconds'), course, uu, step, int(secs), code,
                        '' if ok is None else ('yes' if ok else 'no')])

    def codex(self, args, tag, log):
        """Run codex_write.py; returns (exit, seconds, sent_a_message). Tracks failures in a row."""
        t = time.time()
        r = subprocess.run(PY + ['scripts/codex_write.py'] + args + ['tag=' + tag, 'log=' + log], cwd=ROOT,
                           capture_output=True, text=True, encoding='utf-8')
        out = r.stdout + r.stderr
        sent = 'codex exec failed' not in out and 'codex CLI not found' not in out
        return r.returncode, time.time() - t, sent

    def guard(self, sent):
        """Count failed codex calls in a row; wait once after three; stop after four."""
        if sent:
            self.fails = 0
            return
        self.fails += 1
        if self.fails == 3:
            print('three codex failures in a row: waiting 20 minutes', flush=True)
            time.sleep(1200)
        elif self.fails >= 4:
            print('codex keeps failing (tokens spent or service down): stopping', flush=True)
            raise SystemExit(3)

    def refine(self, course, subject, u, uu, brief):
        day = datetime.date.today().isoformat()     # the fix reads the lens reports of this date, even past midnight
        args = lambda b, extra: [b, course, 'unit=%d' % u, 'uu=' + uu, 'writer_brief=' + brief] + extra
        with cf.ThreadPoolExecutor(max_workers=3) as ex:
            futs = {}
            for lens in LENSES:
                tag = 'lens-%s-%s-s%s' % (lens, course, uu)
                log = os.path.join(self.logdir, tag + '.log')
                futs[lens] = ex.submit(self.codex, args(LENS, ['lens=' + lens, 'allow=docs/reviews/' + tag + '-*.md']),
                                       tag, log)
            for lens, fu in futs.items():
                code, secs, sent = fu.result()
                self.note(course, uu, 'lens-' + lens, secs, code, None)
                self.guard(sent)
        tag = 'fix-%s-s%s' % (course, uu)
        code, secs, sent = self.codex(args(FIX, ['allow=docs/courses/{course}/s%s.md' % uu, 'date=' + day]), tag,
                                      os.path.join(self.logdir, tag + '.log'))
        self.guard(sent)
        ok = cu.passes(course, uu)
        self.note(course, uu, 'fix', secs, code, ok)
        return ok

    def job(self, course, spec, mode):
        subject, nums = cu.units(course)
        if spec != 'all':
            lo, _, hi = spec.partition('-')
            lo, hi = int(lo), int(hi or lo)
            nums = [n for n in nums if lo <= n <= hi]
        brief = cu.brief_for(subject)
        print(course, mode, 'units', nums, flush=True)
        for u in nums:
            uu = '%02d' % u
            path = os.path.join(ROOT, 'docs', 'courses', course, 's%s.md' % uu)
            if mode == 'write':
                if not os.path.exists(path):
                    r = subprocess.run(PY + ['scripts/unit_skeleton.py', course, str(u)], cwd=ROOT,
                                       capture_output=True, text=True, encoding='utf-8')
                    if r.returncode != 0 or not os.path.exists(path):
                        print(course, uu, 'STOPPED: no skeleton:', (r.stdout + r.stderr).strip()[:300], flush=True)
                        return
                done = os.path.exists(os.path.join(ROOT, 'docs', 'reviews', 'codex-write-fix-%s-s%s-%s.md'
                                                   % (course, uu, datetime.date.today().isoformat())))
                if done and cu.passes(course, uu):
                    print(course, uu, 'already through the loop today, skipped', flush=True)
                    continue
                if not cu.passes(course, uu):
                    for t in range(1, self.tries + 1):
                        log = os.path.join(self.logdir, 'write-%s-s%s-try%d.log' % (course, uu, t))
                        code, secs, sent = self.codex([brief, course, 'unit=%d' % u, 'uu=' + uu],
                                                      '%s-s%s' % (course, uu), log)
                        self.guard(sent)
                        ok = cu.passes(course, uu)
                        self.note(course, uu, 'write', secs, code, ok)
                        print(course, uu, 'write try', t, 'PASS' if ok else 'FAIL', flush=True)
                        if ok:
                            break
                    else:
                        print(course, uu, 'STOPPED: write still failing', flush=True)
                        return
            ok = self.refine(course, subject, u, uu, brief)
            print(course, uu, 'refined', 'PASS' if ok else 'FAIL', flush=True)
            if not ok:
                print(course, uu, 'STOPPED: fails after the fix', flush=True)
                return


def main(a):
    if not a or a[0] in ('-h', '--help'):
        print(__doc__)
        return 0 if a else 2
    opts = dict(x.split('=', 1) for x in a[1:])
    logdir = opts.get('logdir', tempfile.gettempdir())
    os.makedirs(logdir, exist_ok=True)
    run = Run(logdir, opts.get('results', os.path.join(logdir, 'loop-results.csv')), int(opts.get('tries', '2')))
    for line in open(a[0], encoding='utf-8'):
        p = line.split('#', 1)[0].split()
        if not p:
            continue
        if len(p) != 3 or p[2] not in ('write', 'review'):
            raise SystemExit('bad queue line: %r (want: course units write|review)' % line)
        run.job(*p)
    print('QUEUE DONE', flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

r"""Take turns in one repository: one worker at a time, any model, any machine.

The turn and the job queue live in git (data/pipeline/turn.json, data/pipeline/jobs.csv), so a worker on another
machine sees the same lock after a pull. Workers never commit or push themselves: `start` and `end` do it.
`end` runs the gates and refuses to hand back the turn while the job added a failure that was not there at `start`.

    python -X utf8 scripts/turn.py status                         who holds the turn, and the queue
    python -X utf8 scripts/turn.py next [--role R]                the next ready job and its paste line
    python -X utf8 scripts/turn.py start <worker> [--role R | --job ID]   take the turn and print the job brief
    python -X utf8 scripts/turn.py brief                          print the held job's brief again
    python -X utf8 scripts/turn.py end <worker> [--fail "why"]    run the gates, commit, push, hand back the turn
    python -X utf8 scripts/turn.py add-unit <course> <unit> <first>-<last>   queue a unit: plan, plan read, plan data
    python -X utf8 scripts/turn.py expand <course> <unit>         queue a unit's days (runs itself after plan data)
    python -X utf8 scripts/turn.py release --force                a person clears a stuck turn

Roles: planner, expert, writer, cheap, fixer, lead. Workers name themselves (codex, sara, claude, cory ...).
Briefs: docs/pipeline/briefs/<kind>.md. Guide: docs/pipeline/README.md.
"""
import csv, datetime, json, os, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PIPE = ROOT / 'data' / 'pipeline'
JOBS = PIPE / 'jobs.csv'
TURN = PIPE / 'turn.json'
BRIEFS = ROOT / 'docs' / 'pipeline' / 'briefs'
COLS = ['id', 'course', 'unit', 'kind', 'role', 'target', 'after', 'status', 'worker', 'started', 'ended', 'commit', 'note']
ROLE = {'plan': 'planner', 'plan-read': 'expert', 'plan-data': 'planner', 'write': 'writer', 'cheap': 'cheap',
        'expert': 'expert', 'fix': 'fixer', 'measure': 'lead'}
# never committed by a turn: Cory's own untracked files and agent worktrees
KEEP_OUT = ['docs/Curio-Class-Plan.pdf', 'docs/US Curriculum Design Blueprint.pdf', 'docs/Return',
            'docs/agents/audit/wordwall-movement-cards.jpg', '.claude']
NEVER_TOUCH = ['data/closet/words', 'closet/words', 'data/media-manifest.txt']
GATES = [['scripts/plan.py', 'check'], ['scripts/lesson.py', 'check']]
CO = 'Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>'


def now():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M')


def git(*a, check=True):
    r = subprocess.run(['git', *a], cwd=ROOT, capture_output=True, text=True, encoding='utf-8', errors='replace')
    if check and r.returncode:
        sys.exit('git %s failed:\n%s%s' % (' '.join(a), r.stdout, r.stderr))
    return r


def py(*a):
    return subprocess.run([sys.executable, '-X', 'utf8', *a], cwd=ROOT, capture_output=True, text=True,
                          encoding='utf-8', errors='replace')


def load():
    if not JOBS.exists():
        return []
    with open(JOBS, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def save(jobs):
    PIPE.mkdir(parents=True, exist_ok=True)
    with open(JOBS, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, COLS, lineterminator='\n')
        w.writeheader()
        for j in jobs:
            w.writerow({c: j.get(c, '') for c in COLS})


def ready(jobs):
    done = {j['id'] for j in jobs if j['status'] == 'done'}
    return [j for j in jobs if j['status'] == 'waiting' and all(a in done for a in j['after'].split() if a)]


def held():
    return json.loads(TURN.read_text(encoding='utf-8')) if TURN.exists() else None


def dirty():
    out = []
    for line in git('status', '--porcelain', '--untracked-files=all').stdout.splitlines():
        p = line[3:].strip().strip('"')
        if any(p == k or p.startswith(k + '/') for k in KEEP_OUT):
            continue
        out.append(line)
    return out


def failures():
    lines = []
    for g in GATES:
        r = py(*g)
        lines += [l.strip() for l in (r.stdout + r.stderr).splitlines() if l.strip().startswith('FAIL')]
    return lines


def pull():
    git('pull', '-q', '--rebase', '--autostash', 'origin', 'main')


def push(msg, paths=None):
    """Commit and push; on a rejected push, pull --rebase and try again (twice)."""
    if paths is None:
        git('add', '-A', '--', '.', *[':!' + k for k in KEEP_OUT])
    else:
        git('add', '--', *paths)
    if git('diff', '--cached', '--quiet', check=False).returncode == 0:
        return git('rev-parse', '--short', 'HEAD').stdout.strip()
    git('commit', '-q', '-m', msg + '\n\n' + CO)
    for _ in range(3):
        if git('push', '-q', 'origin', 'HEAD:main', check=False).returncode == 0:
            return git('rev-parse', '--short', 'HEAD').stdout.strip()
        git('pull', '-q', '--rebase', 'origin', 'main')
    sys.exit('push failed three times; the commit is local. Run `git push origin HEAD:main` by hand.')


def fill(job):
    kind = job['kind']
    t = (BRIEFS / (kind + '.md')).read_text(encoding='utf-8')
    unit = int(job['unit'])
    first, last = (job['target'].split('-') + [''])[:2] if '-' in job['target'] else (job['target'], job['target'])
    day = job['target'] if kind == 'write' else ''
    vals = {'course': job['course'], 'unit': str(unit), 'uu': '%02d' % unit, 'first': first, 'last': last,
            'day': day, 'ddd': ('%03d' % int(day)) if day else '', 'date': datetime.date.today().isoformat(),
            'job': job['id'], 'note': job.get('note', '')}
    if day:
        vals['prev'] = str(int(day) - 1)
        vals['next'] = str(int(day) + 1)
    for k, v in vals.items():
        t = t.replace('{' + k + '}', v)
    return t


def paste_line(job):
    return ('Read AGENTS.md, then run `python -X utf8 scripts/turn.py start <your name> --job %s`, do the job it prints, '
            'and finish with `python -X utf8 scripts/turn.py end <your name>`.' % job['id'])


def cmd_status(_):
    h = held()
    print('Turn: held by %s for %s since %s' % (h['worker'], h['job'], h['since']) if h else 'Turn: free')
    jobs = load()
    r = {j['id'] for j in ready(jobs)}
    for j in jobs:
        if j['status'] == 'done' and j['ended'][:10] < datetime.date.today().isoformat():
            continue
        st = 'ready' if j['id'] in r else j['status']
        print('  %-26s %-8s %-8s %s' % (j['id'], j['role'], st, j['worker'] or ''))


def pick(jobs, role=None, job=None):
    rs = ready(jobs)
    if job:
        m = [j for j in rs if j['id'] == job]
        if not m:
            sys.exit('job %s is not ready (see `turn.py status`)' % job)
        return m[0]
    rs = [j for j in rs if not role or j['role'] == role]
    return rs[0] if rs else None


def cmd_next(a):
    pull()
    role = a[a.index('--role') + 1] if '--role' in a else None
    j = pick(load(), role)
    if not j:
        print('No ready job%s.' % (' for ' + role if role else ''))
        return
    print('%s (%s)\n%s' % (j['id'], j['role'], paste_line(j)))


def cmd_start(a):
    if not a:
        sys.exit('start <worker> [--role R | --job ID]')
    worker = a[0]
    role = a[a.index('--role') + 1] if '--role' in a else None
    jid = a[a.index('--job') + 1] if '--job' in a else None
    d = dirty()
    if d:
        sys.exit('The checkout has uncommitted changes; a turn starts clean:\n  ' + '\n  '.join(d))
    pull()
    h = held()
    if h:
        sys.exit('The turn is held by %s (%s since %s). Wait, or a person runs `turn.py release --force`.'
                 % (h['worker'], h['job'], h['since']))
    jobs = load()
    j = pick(jobs, role, jid)
    if not j:
        sys.exit('No ready job%s.' % (' for ' + role if role else ''))
    base = failures()
    TURN.write_text(json.dumps({'worker': worker, 'job': j['id'], 'since': now(), 'base': base}, indent=1),
                    encoding='utf-8')
    j.update(status='taken', worker=worker, started=now())
    save(jobs)
    push('turn: %s takes %s' % (worker, j['id']), [str(TURN.relative_to(ROOT)), str(JOBS.relative_to(ROOT))])
    if held()['worker'] != worker:
        sys.exit('Someone else took the turn first.')
    print('You hold the turn for %s.\n\n%s' % (j['id'], fill(j)))


def cmd_brief(_):
    h = held()
    if not h:
        sys.exit('Nobody holds the turn.')
    print(fill(next(j for j in load() if j['id'] == h['job'])))


def cmd_end(a):
    if not a:
        sys.exit('end <worker> [--fail "why"]')
    worker, fail = a[0], (a[a.index('--fail') + 1] if '--fail' in a else None)
    h = held()
    if not h or h['worker'] != worker:
        sys.exit('%s does not hold the turn (%s).' % (worker, h and h['worker']))
    touched = [l for l in dirty() if any(l[3:].strip('"').startswith(n) for n in NEVER_TOUCH)]
    if touched:
        sys.exit('These files must not be changed by a job; restore them first:\n  ' + '\n  '.join(touched))
    jobs = load()
    j = next(x for x in jobs if x['id'] == h['job'])
    new = []
    if not fail:
        if j['kind'] != 'plan':
            r = py('scripts/plan.py', 'tables', j['course'])
            if r.returncode:
                new.append('plan.py tables %s failed: %s' % (j['course'], (r.stdout + r.stderr).strip()[-300:]))
        base, now_fail = set(h.get('base', [])), failures()
        # the fix pass leaves no failure at all; any other job adds none
        new += now_fail if j['kind'] == 'fix' else [f for f in now_fail if f not in base]
        if new:
            print('The turn stays with %s: the gates show failures this job must clear (or end with --fail "why"):' % worker)
            print('  ' + '\n  '.join(dict.fromkeys(new)))
            sys.exit(1)
        if j['kind'] in ('write', 'fix', 'plan-data'):
            py('scripts/lesson.py', 'build', '--pdf')
    j.update(status='failed' if fail else 'done', ended=now(), note=(fail or j.get('note', '')))
    if j['kind'] == 'plan-data' and not fail:
        jobs = expand(jobs, j['course'], int(j['unit']))
    TURN.unlink()
    save(jobs)
    c = push('%s: %s by %s%s' % (j['id'], 'failed' if fail else 'done', worker, (' (' + fail + ')') if fail else ''))
    jobs = load()
    for x in jobs:
        if x['id'] == j['id']:
            x['commit'] = c
    save(jobs)
    push('turn: %s commit noted' % j['id'], [str(JOBS.relative_to(ROOT))])
    print('%s %s; turn handed back (%s).' % (j['id'], 'failed' if fail else 'done', c))


def add(jobs, **k):
    if any(j['id'] == k['id'] for j in jobs):
        return jobs
    k.setdefault('role', ROLE[k['kind']])
    k.setdefault('status', 'waiting')
    jobs.append(k)
    return jobs


def cmd_add_unit(a):
    course, unit, rng = a[0], int(a[1]), a[2]
    pull()
    jobs = load()
    u = '%s-u%02d' % (course, unit)
    add(jobs, id=u + '-plan', course=course, unit=str(unit), kind='plan', target=rng, after='')
    add(jobs, id=u + '-plan-read', course=course, unit=str(unit), kind='plan-read', target=rng, after=u + '-plan')
    add(jobs, id=u + '-plan-data', course=course, unit=str(unit), kind='plan-data', target=rng, after=u + '-plan-read')
    save(jobs)
    push('turn: queue %s (plan, plan read, plan data)' % u, [str(JOBS.relative_to(ROOT))])
    print('Queued %s. Its days are queued when its plan-data job ends.' % u)


def expand(jobs, course, unit):
    path = ROOT / 'data' / 'plans' / course / 'days.csv'
    with open(path, encoding='utf-8', newline='') as f:
        days = sorted(int(r['day']) for r in csv.DictReader(f) if r['stretch'].strip() == str(unit))
    if not days:
        return jobs
    u = '%s-u%02d' % (course, unit)
    rng = '%d-%d' % (days[0], days[-1])
    # days are written in order; the first day also waits for the day before it, when that day is queued here
    prev = '%s-d%03d-write' % (course, days[0] - 1)
    after = prev if any(j['id'] == prev for j in jobs) else u + '-plan-data'
    for d in days:
        jid = '%s-d%03d-write' % (course, d)
        add(jobs, id=jid, course=course, unit=str(unit), kind='write', target=str(d), after=after)
        after = jid
    add(jobs, id=u + '-cheap', course=course, unit=str(unit), kind='cheap', target=rng, after=after)
    add(jobs, id=u + '-expert', course=course, unit=str(unit), kind='expert', target=rng, after=u + '-cheap')
    add(jobs, id=u + '-fix', course=course, unit=str(unit), kind='fix', target=rng, after=u + '-expert')
    add(jobs, id=u + '-measure', course=course, unit=str(unit), kind='measure', target=rng, after=u + '-fix')
    return jobs


def cmd_expand(a):
    pull()
    jobs = expand(load(), a[0], int(a[1]))
    save(jobs)
    push('turn: queue the days of %s unit %s' % (a[0], a[1]), [str(JOBS.relative_to(ROOT))])
    cmd_status([])


def cmd_release(a):
    if '--force' not in a:
        sys.exit('release --force (a person, for a stuck turn)')
    pull()
    h = held()
    if not h:
        print('Nobody holds the turn.')
        return
    jobs = load()
    for j in jobs:
        if j['id'] == h['job'] and j['status'] == 'taken':
            j.update(status='waiting', worker='', started='')
    TURN.unlink()
    save(jobs)
    push('turn: released by hand (%s held %s)' % (h['worker'], h['job']),
         [str(TURN.relative_to(ROOT)), str(JOBS.relative_to(ROOT))])
    print('Released. Changes the stuck job left in the checkout were not committed; look at `git status`.')


CMDS = {'status': cmd_status, 'next': cmd_next, 'start': cmd_start, 'brief': cmd_brief, 'end': cmd_end,
        'add-unit': cmd_add_unit, 'expand': cmd_expand, 'release': cmd_release}

if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in CMDS:
        print(__doc__)
        sys.exit(0)
    CMDS[sys.argv[1]](sys.argv[2:])

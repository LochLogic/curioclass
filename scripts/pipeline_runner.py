r"""Run the job queue unattended: take the turn, start the right worker with the job brief, end the turn, repeat.

    python -X utf8 scripts/pipeline_runner.py [--once] [--only ROLE[,ROLE]] [--max N] [--dry]

Which worker serves which role, and how it is started, is data/pipeline/workers.json (a worker with
"enabled": false is skipped). One job at a time, never two. When a job's gates fail, the worker gets one more go with
the failures in its prompt; if they still fail, the job is ended --fail and the runner stops for a person. A worker
that ends within two minutes, or says it hit a usage limit, stops the runner and gives the turn back.
Stop gently: create data/pipeline/runner/STOP (the current job finishes first). Logs: data/pipeline/runner/
(not committed); one row per run in data/pipeline/runs.csv (committed with the job).
"""
import csv, datetime, json, os, re, shutil, subprocess, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PIPE = ROOT / 'data' / 'pipeline'
LOGS = PIPE / 'runner'
RUNS = PIPE / 'runs.csv'
RUN_COLS = ['job', 'worker', 'model', 'started', 'minutes', 'tries', 'result', 'tokens']
sys.path.insert(0, str(ROOT / 'scripts'))
import turn  # noqa: E402

LIMIT_WORDS = re.compile(r'usage limit|rate limit|quota|out of credits|limit reached', re.I)


def exe(name):
    hit = shutil.which(name) or shutil.which(name + '.cmd')
    npm = Path(os.environ.get('APPDATA', '')) / 'npm' / (name + '.cmd')
    if not hit and npm.exists():
        hit = str(npm)
    return hit


def tturn(*a):
    r = subprocess.run([sys.executable, '-X', 'utf8', 'scripts/turn.py', *a], cwd=ROOT, capture_output=True,
                       text=True, encoding='utf-8', errors='replace')
    return r.returncode, r.stdout + r.stderr


def tokens(text):
    """Best effort: the largest total-token figure the worker printed (Codex --json, Claude --output-format json)."""
    n = [int(x) for x in re.findall(r'"(?:total_tokens|tokens_used)"\s*:\s*(\d+)', text)]
    u = re.findall(r'"input_tokens"\s*:\s*(\d+).{0,200}?"output_tokens"\s*:\s*(\d+)', text, re.S)
    n += [int(a) + int(b) for a, b in u]
    return max(n) if n else ''


def launch(w, prompt, log):
    args = [exe(w['cmd'][0]) or w['cmd'][0]] + [a.replace('{repo}', str(ROOT)) for a in w['cmd'][1:]]
    env = dict(os.environ, **w.get('env', {}))
    t0 = time.time()
    with open(log, 'w', encoding='utf-8') as out:
        p = subprocess.Popen(args, cwd=ROOT, stdin=subprocess.PIPE, stdout=out, stderr=subprocess.STDOUT,
                             text=True, encoding='utf-8', env=env)
        p.stdin.write(prompt)
        p.stdin.close()
        try:
            p.wait(timeout=w.get('timeout_min', 120) * 60)
        except subprocess.TimeoutExpired:
            p.kill()
    text = Path(log).read_text(encoding='utf-8', errors='replace')
    return p.returncode, time.time() - t0, text


def log_run(row):
    new = not RUNS.exists()
    with open(RUNS, 'a', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, RUN_COLS, lineterminator='\n')
        if new:
            w.writeheader()
        w.writerow(row)


def say(msg):
    line = '%s %s' % (datetime.datetime.now().strftime('%H:%M'), msg)
    print(line, flush=True)
    with open(LOGS / 'summary.txt', 'a', encoding='utf-8') as f:
        f.write(line + '\n')


def main(a):
    LOGS.mkdir(parents=True, exist_ok=True)
    workers = json.loads((PIPE / 'workers.json').read_text(encoding='utf-8'))
    only = set(a[a.index('--only') + 1].split(',')) if '--only' in a else None
    cap = int(a[a.index('--max') + 1]) if '--max' in a else 0
    done = 0
    while True:
        if (LOGS / 'STOP').exists():
            say('STOP file found; stopping.')
            return
        turn.pull()
        if turn.held():
            say('turn held by %s; waiting' % turn.held()['worker'])
            if '--once' in a:
                return
            time.sleep(300)
            continue
        job, wname = None, None
        for j in turn.ready(turn.load()):
            if only and j['role'] not in only:
                continue
            for name, w in workers.items():
                if w.get('enabled', True) and j['role'] in w['roles']:
                    job, wname = j, name
                    break
            if job:
                break
        if not job:
            say('no ready job for an enabled worker; stopping.')
            return
        w = workers[wname]
        if '--dry' in a:
            say('would run %s with %s' % (job['id'], wname))
            return
        rc, out = tturn('start', wname, '--job', job['id'])
        if rc:
            say('start refused: ' + out.strip()[-400:])
            return
        brief = out.split('\n', 2)[-1]
        prompt = ('You are the worker "%s" in the Curio Class repository. Read AGENTS.md first. A runner already holds '
                  'the turn for you and will end it: do not run turn.py, and do not commit or push.\n\n%s'
                  % (wname, brief))
        stamp = datetime.datetime.now().strftime('%Y%m%d-%H%M')
        started, tries, total, result, tok = turn.now(), 0, 0.0, '', 0
        while True:
            tries += 1
            say('%s: %s try %d' % (job['id'], wname, tries))
            rc, secs, text = launch(w, prompt, LOGS / ('%s-%s-%d.log' % (stamp, job['id'], tries)))
            total += secs
            tok += tokens(text) or 0
            if secs < 120 or LIMIT_WORDS.search(text[-3000:]) and rc:
                say('%s: worker ended after %ds (rc %s), maybe a usage limit; giving the turn back and stopping.'
                    % (job['id'], secs, rc))
                tturn('release', '--force')
                return
            log_run({'job': job['id'], 'worker': wname, 'model': w.get('model', ''), 'started': started,
                     'minutes': round(total / 60, 1), 'tries': tries, 'result': 'gates next', 'tokens': tok or ''})
            rc, out = tturn('end', wname)
            if rc == 0:
                result = 'done'
                break
            if tries >= 2:
                tturn('end', wname, '--fail', 'gates still failing after two tries; see the runner log')
                result = 'failed'
                break
            prompt = ('You are the worker "%s". You were doing this job and the gates still fail. Fix these, then '
                      'stop (do not run turn.py, do not commit):\n%s\n\nThe job:\n%s' % (wname, out[-3000:], brief))
        say('%s: %s in %.0f min, %s tokens' % (job['id'], result, total / 60, tok or '?'))
        if result == 'failed':
            say('stopping for a person.')
            return
        done += 1
        if '--once' in a or (cap and done >= cap):
            return


if __name__ == '__main__':
    main(sys.argv[1:])

r"""Pull new messages from the home page message box into docs/Return/messages/ for review (never committed).

    python scripts/messages.py pull      write the unread messages to docs/Return/messages/<date>.md and mark them read
    python scripts/messages.py count     how many are waiting, by kind
    python scripts/messages.py again N   mark the last N messages unread, to pull them again

The messages live in the Cloudflare D1 database curioclass-messages (worker/index.js, worker/sql/messages.sql).
"""
import datetime as dt, json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'docs' / 'Return' / 'messages'
DB = 'curioclass-messages'
KINDS = {'broken': "Something's broken", 'feedback': 'Feedback', 'idea': 'Ideas', 'hello': 'Just saying hi'}


def sql(command):
    r = subprocess.run(f'npx wrangler d1 execute {DB} --remote --json --command "{command}"', cwd=ROOT, shell=True,
                       capture_output=True, text=True, encoding='utf-8', timeout=120)
    if r.returncode:
        sys.exit(r.stderr.strip() or r.stdout.strip())
    return json.loads(r.stdout)[0]['results']


def pull():
    rows = sql('SELECT id, created, kind, role, message, email, page FROM messages WHERE read = 0 ORDER BY created')
    if not rows:
        print('No new messages.')
        return
    OUT.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.now().strftime('%Y-%m-%d-%H%M')
    lines = [f'# Messages pulled {stamp} ({len(rows)})', '']
    for kind, title in KINDS.items():
        group = [r for r in rows if r['kind'] == kind]
        if not group:
            continue
        lines += [f'## {title} ({len(group)})', '']
        for r in group:
            who = ', '.join(x for x in (r['role'], r['email'], r['page']) if x)
            lines += [f"### #{r['id']} · {r['created'][:16].replace('T', ' ')} UTC" + (f' · {who}' if who else ''), '',
                      r['message'].strip(), '']
    path = OUT / f'{stamp}.md'
    path.write_text('\n'.join(lines), encoding='utf-8')
    ids = ','.join(str(r['id']) for r in rows)
    sql(f'UPDATE messages SET read = 1 WHERE id IN ({ids})')
    print(f'{len(rows)} messages -> {path}')


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'pull'
    if cmd == 'pull':
        pull()
    elif cmd == 'count':
        for r in sql('SELECT kind, COUNT(*) AS n FROM messages WHERE read = 0 GROUP BY kind'):
            print(f"{r['kind']}: {r['n']}")
    elif cmd == 'again':
        n = int(sys.argv[2])
        sql(f'UPDATE messages SET read = 0 WHERE id IN (SELECT id FROM messages ORDER BY id DESC LIMIT {n})')
        print(f'last {n} marked unread')
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main()

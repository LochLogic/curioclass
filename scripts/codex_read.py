"""Send a read brief to Codex by script, no clicks (Cory 2026-11-13: "use a script to send it over there automatically").

    python -X utf8 scripts/codex_read.py <brief.md> <out.md> [key=value ...]

Fills {key} slots in the brief (subject=..., date=... is added), tells Codex it reads only and that its last message
is the whole report, runs `codex exec` in a read-only sandbox with web search on, and writes the last message to
<out.md>. The report is Codex's; the caller files its findings as with any expert read.
"""
import datetime
import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FRAME = """You are the second, independent reader of a Curio Class plan file (a free K-12 curriculum). The repository
is the current directory. You may read any file and run read-only commands (python scripts that only check).
You may not edit, create or delete any file: you are in a read-only sandbox, and where the brief says "write
docs/reviews/...", instead give that report, complete, as your final message, in Markdown. Use web search for
outside sources where the brief asks for them, and name each source by link; mark what rests on memory.
No em dashes in the report.

The brief follows.

"""


def main(a):
    if len(a) < 2:
        raise SystemExit(__doc__)
    brief, out = a[0], a[1]
    slots = {'date': datetime.date.today().isoformat()}
    for kv in a[2:]:
        k, v = kv.split('=', 1)
        slots[k] = v
    text = open(brief, encoding='utf-8').read()
    for k, v in slots.items():
        text = text.replace('{' + k + '}', v)
    codex = shutil.which('codex') or shutil.which('codex.cmd')
    if not codex:
        raise SystemExit('codex CLI not found')
    tmp = out + '.part'
    cmd = [codex, 'exec', '-s', 'read-only', '-C', ROOT, '-c', 'tools.web_search=true',
           '--color', 'never', '-o', tmp, '-']
    r = subprocess.run(cmd, input=FRAME + text, text=True, encoding='utf-8',
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    log = out + '.log'
    open(log, 'w', encoding='utf-8').write(r.stdout or '')
    if r.returncode != 0 or not os.path.exists(tmp) or not open(tmp, encoding='utf-8').read().strip():
        raise SystemExit('codex exec failed (exit %s); see %s' % (r.returncode, log))
    os.replace(tmp, out)
    print('wrote', out)


if __name__ == '__main__':
    main(sys.argv[1:])

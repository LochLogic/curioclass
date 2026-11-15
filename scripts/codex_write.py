"""Send a write brief to Codex by script, no clicks, no approvals (the unit plan writer; modeled on codex_read.py).

    python -X utf8 scripts/codex_write.py <brief.md> <course> [key=value ...] [log=PATH]

Fills {course}, {date} and any key=value slot in the brief, runs `codex exec` in a workspace-write sandbox with web
search on, the repository as the working root, the prompt on stdin, and the last message kept. Before and after the
run it snapshots `git status --porcelain` plus each listed file's size and mtime, and afterwards reports every file
that changed outside the allowed set:

    docs/courses/<course>/s*.md, docs/courses/<course>/TOOL-ASKS.md, docs/courses/<course>/DEFAULTS.md

Other courses' docs/courses/*/s{uu}.md may change at the same time from other writers and are ignored. The last
message goes to docs/reviews/codex-write-<course>-<date>.md (the outside-file report is appended to it); the full log
goes to log=PATH (default: a file in the system temp directory, never under docs/reviews). Exit 1 if codex failed or an
outside file changed. Ignored files (.gitignore) are not in `git status`, so a change there is not seen.

Other jobs (added 2026-11-14 for the scope and sequence run, scripts/codex_scopes.py): `allow=a;b` replaces the
allowed set with these repo paths or globs ({course} filled), and `tag=x` names the report codex-write-<x>-<date>.md.
Other courses' scope files (scope-and-sequence.md, days.csv, source-map.csv) and docs/reviews/sequence-* reports may
change at the same time from parallel jobs and are ignored.

Example:  python -X utf8 scripts/codex_write.py docs/pipeline/briefs/plan-codex.md social-studies-grade-3
"""
import datetime
import fnmatch
import os
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FRAME = """You are writing files in a Curio Class repository (a free K-12 curriculum). The repository is the current
directory. You may read any file the brief allows and run local commands (python scripts that check). You may write
only the files the brief names; the sandbox lets you write anywhere in the repository, so the limit is yours to keep:
a script compares the repository before and after and reports every other file you touched. Do not use git. Do not ask
questions: nobody is there to answer, so decide, and put what a person must look at in your last message.
Your last message is the report the brief asks for; it is filed as it stands. No em dashes anywhere.
Gates: run the ones the brief names. If a gate fails on another course's file, or does not run in the sandbox, say so in
one line and carry on with your own files.

The brief follows.

"""


def git_status():
    """{path: (status, size, mtime_ns)} for every path `git status --porcelain` lists (untracked files one by one)."""
    r = subprocess.run(['git', '-C', ROOT, 'status', '--porcelain=v1', '-z', '-uall'],
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if r.returncode != 0:
        raise SystemExit('git status failed: ' + r.stderr.decode('utf-8', 'replace'))
    parts = r.stdout.decode('utf-8', 'replace').split('\0')
    out = {}
    i = 0
    while i < len(parts):
        e = parts[i]
        i += 1
        if len(e) < 4:
            continue
        status, path = e[:2], e[3:]
        if status[0] in 'RC' or status[1] in 'RC':
            i += 1                      # the original name of a rename or copy follows
        full = os.path.join(ROOT, path)
        try:
            st = os.stat(full)
            out[path] = (status, st.st_size, st.st_mtime_ns)
        except OSError:
            out[path] = (status, None, None)
    return out


def changed(before, after):
    """Paths whose status, size or mtime differ, that appeared, or that dropped out of the status list."""
    out = []
    for p in sorted(set(before) | set(after)):
        if before.get(p) != after.get(p):
            out.append(p)
    return out


ALLOW = None   # set from allow=; None means the unit plan set below


def allowed(path, course):
    p = path.replace('\\', '/')
    if ALLOW is not None:
        return any(fnmatch.fnmatch(p, g.replace('{course}', course)) for g in ALLOW)
    d ='docs/courses/%s/' % course
    if p.startswith(d) and '/' not in p[len(d):]:
        name = p[len(d):]
        return fnmatch.fnmatch(name, 's*.md') or name in ('TOOL-ASKS.md', 'DEFAULTS.md')
    return False


def other_course_plan(path):
    p = path.replace('\\', '/').split('/')
    if len(p) == 3 and p[:2] == ['docs', 'reviews'] and p[2].startswith('codex-write-'):
        return True                     # another concurrent run's report
    if len(p) == 3 and p[:2] == ['docs', 'reviews'] and (p[2].startswith('sequence-') or p[2].endswith('.md.log')):
        return True                     # a parallel scope job's read or its log
    if len(p) == 4 and p[0] == 'data' and p[1] == 'plans' and p[3] in ('days.csv', 'source-map.csv'):
        return True                     # a parallel scope job's days
    if len(p) == 4 and p[:2] == ['docs', 'courses'] and p[3] == 'scope-and-sequence.md':
        return True
    return len(p) == 4 and p[0] == 'docs' and p[1] == 'courses' and (
        fnmatch.fnmatch(p[3], 's*.md') or p[3] in ('TOOL-ASKS.md', 'DEFAULTS.md'))


def main(a):
    if len(a) < 2:
        raise SystemExit(__doc__)
    brief, course = a[0], a[1]
    date = datetime.date.today().isoformat()
    slots = {'course': course, 'date': date}
    log = os.path.join(tempfile.gettempdir(), 'codex-write-%s-%s.log' % (course, date))
    for kv in a[2:]:
        k, v = kv.split('=', 1)
        if k == 'log':
            log = v
        elif k == 'allow':
            global ALLOW
            ALLOW = [g.strip() for g in v.split(';') if g.strip()]
        elif k == 'tag':
            slots['_tag'] = v
        else:
            slots[k] = v
    text = open(brief, encoding='utf-8').read()
    for k, v in slots.items():
        text = text.replace('{' + k + '}', v)
    codex = shutil.which('codex') or shutil.which('codex.cmd')
    if not codex:
        raise SystemExit('codex CLI not found')
    tag = slots.pop('_tag', None) or course + ('-s' + slots['uu'] if 'uu' in slots else '')
    out = os.path.join(ROOT, 'docs', 'reviews', 'codex-write-%s-%s.md' % (tag, date))
    tmp = os.path.join(tempfile.gettempdir(), 'codex-write-%s-%s.last.part' % (tag, date))
    if os.path.exists(tmp):
        os.remove(tmp)
    before = git_status()
    cmd = [codex, 'exec', '-s', 'workspace-write', '-C', ROOT, '-c', 'tools.web_search=true',
           '--color', 'never', '-o', tmp, '-']
    r = subprocess.run(cmd, input=FRAME + text, text=True, encoding='utf-8',
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    os.makedirs(os.path.dirname(log) or '.', exist_ok=True)
    open(log, 'w', encoding='utf-8').write(r.stdout or '')
    after = git_status()
    outside = [p for p in changed(before, after)
               if not allowed(p, course) and not other_course_plan(p)
               and p.replace('\\', '/') != os.path.relpath(out, ROOT).replace('\\', '/')]
    inside = [p for p in changed(before, after) if allowed(p, course)]
    last = open(tmp, encoding='utf-8').read() if os.path.exists(tmp) else ''
    failed = r.returncode != 0 or not last.strip()
    report = last.rstrip() + '\n'
    if outside:
        report += '\n## Files changed outside the allowed set\n\n' + ''.join('- %s\n' % p for p in outside)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf-8').write(report)
    print('wrote', out)
    print('log', log)
    print('changed in the allowed set: %d' % len(inside))
    for p in inside:
        print('  ' + p)
    if outside:
        print('OUTSIDE the allowed set:')
        for p in outside:
            print('  ' + p)
    if failed:
        print('codex exec failed (exit %s) or sent no last message; see %s' % (r.returncode, log))
    return 1 if (failed or outside) else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

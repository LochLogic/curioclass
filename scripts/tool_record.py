"""One record per tool past Spec (consolidation step 5 item 5): tools/<id>/tool.md.

    python -X utf8 scripts/tool_record.py flatten <tool_id> [--dry-run]   fold that tool's record files into tool.md
    python -X utf8 scripts/tool_record.py flatten --all [--dry-run]       every tool that has record files
    python -X utf8 scripts/tool_record.py part <tool_id> <file>           print one record part, from either shape
    python -X utf8 scripts/tool_record.py check                           every tool.md parses; no part is in both shapes

What moves: the process record after Spec, the files in PARTS (build brief and report, self-check, refine and its
lens reports, the pre-2026-10-27 verify, fix, handoff, art plan, finish check). Each goes into tool.md under its
stage heading, between `<!-- part: <file> -->` and `<!-- end part -->`, its own headings pushed down two levels;
`part` gives the text back (line feeds, no trailing blank lines). Earlier rounds (polish-1.md, refine-2026-10-28.md and its folder,
codex-report-1.md) move to S:/CurioClass-archive/tool-rounds-<date>/<id>/ (git history keeps them too). A dated log
closes the file. What stays: idea.md and spec.md (the build briefs and queues name spec.md), notes.md, plan.md and
exit.md (teacher pages the site reads), sources.md, nav-plan.md, src.html, art/, voice/, tool.json. A super-check
script, when a tool gets one, goes in tools/<id>/checks/.

Readers use part() and has(), so both shapes work until the last tool is flattened (board.py, refine_pack.py). A new
record part is written into tool.md by the step that makes it (docs/BUILD-PLAN.md, "One record per tool").
"""
import datetime
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / 'tools'
ARCHIVE = Path('S:/CurioClass-archive')
sys.path.insert(0, str(ROOT / 'scripts'))

# (stage heading, files in that stage, in order); a name with * is a glob inside the tool folder
PARTS = [('Build', ['CODEX-BRIEF.md', 'codex-report.md']),
         ('Self-check', ['codex-review.md']),
         ('Refine', ['sensitivity-pre-refine.md', 'refine.md', 'refine/*.md']),
         ('Exit check before 2026-10-27', ['verify.md']),
         ('Fix', ['polish.md', 'review-fix.md']),
         ('Handoff', ['handoff.md']),
         ('Art and voice', ['art-plan.md', 'final-art.md']),
         ('Finish check', ['final.md', 'final-fix.md'])]
EARLIER = [re.compile(r'polish-\d+\.md'), re.compile(r'refine-\d{4}-\d{2}-\d{2}(\.md)?'),
           re.compile(r'codex-report-\d+\.md'), re.compile(r'codex-review-\d+\.md')]
OPEN = re.compile(r'<!-- part: (\S+) -->')
CLOSE = '<!-- end part -->'


def files_of(folder):
    """[(stage, relative name)] of the record files present in a tool folder, in PARTS order."""
    out = []
    for stage, names in PARTS:
        for n in names:
            hits = sorted(folder.glob(n)) if '*' in n else ([folder / n] if (folder / n).is_file() else [])
            out += [(stage, p.relative_to(folder).as_posix()) for p in hits]
    return out


def earlier_of(folder):
    return sorted(p for p in folder.iterdir() if any(rx.fullmatch(p.name) for rx in EARLIER))


def _shift(text, n):
    """Push Markdown headings down n levels (n < 0 pulls them back), outside fenced code."""
    out, fence = [], False
    for ln in text.split('\n'):
        if ln.lstrip().startswith('```'):
            fence = not fence
        elif not fence and re.match(r'#+ ', ln):
            ln = ('#' * n + ln) if n > 0 else ln[-n:]
        out.append(ln)
    return '\n'.join(out)


def parse(text):
    """{part name: original text} from a tool.md."""
    parts, name, buf = {}, None, []
    for ln in text.split('\n'):
        m = OPEN.fullmatch(ln.strip())
        if m and name is None:
            name, buf = m.group(1), []
        elif ln.strip() == CLOSE and name is not None:
            body = '\n'.join(buf)
            parts[name] = _shift(body[1:-1] if body.startswith('\n') and body.endswith('\n') else body, -2)
            name = None
        elif name is not None:
            buf.append(ln)
    if name is not None:
        raise ValueError('part %s has no end marker' % name)
    return parts


def part(tid, name):
    """A record part's text from the old file or from tool.md; '' when the tool has neither."""
    f = TOOLS / tid / name
    if f.is_file():
        return f.read_text(encoding='utf-8')
    t = TOOLS / tid / 'tool.md'
    if t.is_file():
        return parse(t.read_text(encoding='utf-8')).get(name, '')
    return ''


def has(tid, name):
    f = TOOLS / tid / name
    if f.is_file():
        return True
    t = TOOLS / tid / 'tool.md'
    return t.is_file() and name in parse(t.read_text(encoding='utf-8'))


def git_date(path):
    out = subprocess.run(['git', 'log', '-1', '--format=%ad', '--date=short', '--', str(path)], cwd=ROOT,
                         capture_output=True, text=True).stdout.strip()
    return out or 'not committed'


def render(tid, title, found, old, log):
    out = ['# %s: the record' % title, '',
           'Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is',
           '[spec.md](spec.md); the teacher notes are [notes.md](notes.md).', '']
    stage = None
    for st, name, text in found:
        if st != stage:
            out += ['## ' + st, '']
            stage = st
        body = text.replace('\r\n', '\n').rstrip('\n')
        out += ['<!-- part: %s -->' % name, '', _shift(body, 2), '', CLOSE, '']
    out += ['## Log', ''] + log + ['']
    return '\n'.join(out)


def flatten(tid, dry, today, titles):
    folder = TOOLS / tid
    found = files_of(folder)
    old = earlier_of(folder)
    if not found and not old:
        return None
    t = folder / 'tool.md'
    prior = parse(t.read_text(encoding='utf-8')) if t.is_file() else {}
    texts, log = [], []
    for st, name in found:
        if name in prior:
            raise SystemExit('tool_record: %s has %s both as a file and inside tool.md' % (tid, name))
        texts.append((st, name, (folder / name).read_text(encoding='utf-8')))
        log.append('- %s: %s folded in (last changed %s)' % (today, name, git_date(folder / name)))
    if prior:                                  # a tool flattened before keeps its parts and log
        keep = [(st, n, prior[n]) for st, names in PARTS for n in prior if _stage(n) == st]
        texts = sorted(keep + texts, key=lambda x: _order(x[1]))
        log = _old_log(t.read_text(encoding='utf-8')) + log
    dest = ARCHIVE / ('tool-rounds-' + today) / tid
    log += ['- %s: earlier round %s moved to %s' % (today, p.name, dest.as_posix()) for p in old]
    text = render(tid, titles.get(tid, tid), texts, old, log)
    if not dry:
        import safe_write
        safe_write.replace(t, text)
        assert parse(t.read_text(encoding='utf-8')).keys() >= {n for _, n, _ in texts}
        for _, name in found:
            (folder / name).unlink()
        if (folder / 'refine').is_dir() and not any((folder / 'refine').iterdir()):
            (folder / 'refine').rmdir()
        for p in old:
            dest.mkdir(parents=True, exist_ok=True)
            shutil.move(str(p), str(dest / p.name))
        _point_stage(tid)
    return len(found), len(old)


def _stage(name):
    for st, names in PARTS:
        for n in names:
            if n == name or ('*' in n and Path(name).match(n)):
                return st
    return 'Other'


def _order(name):
    i = 0
    for st, names in PARTS:
        for n in names:
            if n == name or ('*' in n and Path(name).match(n)):
                return (i, name)
            i += 1
    return (i, name)


def _old_log(text):
    return text.split('\n## Log\n', 1)[1].strip('\n').split('\n') if '\n## Log\n' in text else []


def _point_stage(tid):
    """A stage record that was folded in now points at tool.md."""
    import tool_stages
    rows = tool_stages.read()
    r = rows.get(tid)
    if r and r['record'].startswith('tools/%s/' % tid) and not (ROOT / r['record']).exists():
        r['record'] = 'tools/%s/tool.md' % tid
        tool_stages.write(rows)


def titles():
    import csv
    import board
    rows = list(csv.DictReader(open(ROOT / 'data' / 'tools-concepts.csv', encoding='utf-8'))) + board.recess_rows()
    return {r['tool_id']: r['title'] for r in rows}


def check():
    out = []
    for t in sorted(TOOLS.glob('*/tool.md')):
        tid = t.parent.name
        try:
            parts = parse(t.read_text(encoding='utf-8'))
        except ValueError as e:
            out.append('FAIL tools/%s/tool.md: %s' % (tid, e))
            continue
        for name in parts:
            if _stage(name) == 'Other':
                out.append('FAIL tools/%s/tool.md: unknown part %s' % (tid, name))
            if (t.parent / name).is_file():
                out.append('FAIL tools/%s: %s is both a file and a part of tool.md' % (tid, name))
    return out


def main(a):
    if not a or a[0] not in ('flatten', 'part', 'check'):
        print(__doc__)
        return 2
    if a[0] == 'part':
        sys.stdout.write(part(a[1], a[2]))
        return 0
    if a[0] == 'check':
        lines = check()
        for ln in lines:
            print(ln)
        n = len(list(TOOLS.glob('*/tool.md')))
        print('tool_record check: %d tool.md files, %d problems' % (n, len(lines)))
        return 1 if lines else 0
    dry = '--dry-run' in a
    today = datetime.date.today().isoformat()
    ids = sorted(p.name for p in TOOLS.iterdir() if p.is_dir()) if '--all' in a else [a[1]]
    names = titles()
    tools = parts = rounds = 0
    for tid in ids:
        r = flatten(tid, dry, today, names)
        if r:
            tools += 1
            parts += r[0]
            rounds += r[1]
            if not '--all' in a or not dry:
                print('%s tools/%s/tool.md: %d parts, %d earlier rounds' % ('would write' if dry else 'wrote', tid, *r))
    print('tool_record: %s %d tools, %d parts folded, %d earlier rounds archived' % (
        'would flatten' if dry else 'flattened', tools, parts, rounds))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

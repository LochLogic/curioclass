r"""The build board: where every tool is in the pipeline. The stage is read from data/tool-stages.csv
(scripts/tool_stages.py, its one home); art, voice, verify, plan and sub come from the tool's files. The file guess
below (infer) seeded that table and is what `tool_stages.py check` compares against.

    python scripts/board.py              write docs/BUILD-BOARD.md and print the totals
    python scripts/board.py --wave 1     print one wave's rows

Stages, in order (docs/BUILD-PLAN.md, "Names for each step"). Each tool counts under the last step it has finished:
  concept    Idea: only the catalog line
  spec       Spec: tools/<id>/spec.md (docs/agents/SPEC.md)
  build      Build: codex-report.md (in Codex's checkout until pulled), or a Claude build with no Self-check
  selfcheck  Self-check: codex-review.md; waiting for Refine
  refine     Refine: refine.md's first line is OPEN or ROUND 2 and there is no polish.md; waiting for Fix
  fix        Fix: polish.md is in; waiting for the Exit check
  exit       Exit check: refine.md (or a pre-2026-10-27 verify.md) says PASS; waiting for art and voice
  artvoice   Art and voice: every asset painted and every line recorded (or none asked for); waiting for the Finish check
  finish     Finish check: final.md says PASS; waiting for Cory's Sign-off on the Desk
  live       tool.json (on the site)
The Plan column says whether tools/<id>/plan.md exists (docs/LESSON-PLANS.md), and Sub whether exit.md does (its Sub Day
packet). Neither holds back the stage.
Waves come from data/waves.csv (tool_id,wave). Sign-off state lives on the Desk, not here.
"""
import csv, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / 'tools'
sys.path.insert(0, str(ROOT / 'scripts'))
from voice import clip_name  # noqa: E402


def art(f):
    p = f / 'art' / 'prompts.json'
    if not p.exists():
        return 0, 0
    names = [a['name'] for a in json.loads(p.read_text(encoding='utf-8'))['assets']]
    return sum((f / 'art' / f'{n}.webp').exists() for n in names), len(names)


def voice(f):
    p = f / 'voice' / 'lines.json'
    if not p.exists():
        return 0, 0
    spec = json.loads(p.read_text(encoding='utf-8'))
    lines = {*spec.get('lines', []), *(t for g in spec.get('groups', []) for t in g)}
    return sum((f / 'voice' / clip_name(t)).exists() for t in lines), len(lines)


def first_line(tid, name):
    """The first line of a record part, from the old file or from tool.md (scripts/tool_record.py)."""
    import tool_record
    return tool_record.part(tid, name).split('\n', 1)[0].upper()


def has(tid, name):
    import tool_record
    return tool_record.has(tid, name)


_STAGES = None


def row(tid):
    """Where a tool is: its stage from data/tool-stages.csv (scripts/tool_stages.py, consolidation step 5 item 1),
    the other columns from its files. A tool with no row there falls back to the file guess."""
    global _STAGES
    if _STAGES is None:
        import tool_stages
        _STAGES = {k: r['stage'] for k, r in tool_stages.read().items()}
    r = infer(tid)
    r['stage'] = _STAGES.get(tid, r['stage'])
    return r


def infer(tid):
    """The file guess (before data/tool-stages.csv): the last step a tool's files show finished (docs/BUILD-PLAN.md,
    "Names for each step"). tool_stages.py seed starts from it and tool_stages.py check compares against it."""
    f = TOOLS / tid
    a, an = art(f); v, vn = voice(f)
    verdict = first_line(tid, 'refine.md' if has(tid, 'refine.md') else 'verify.md')
    if (f / 'tool.json').exists():
        st = 'live'
    elif (f / 'tool.draft.json').exists():
        if 'PASS' in verdict:
            if a == an and v == vn:  # every asset painted and every line recorded (or none asked for)
                st = 'finish' if 'PASS' in first_line(tid, 'final.md') else 'artvoice'
            else:
                st = 'exit'
        elif verdict:  # Refine wrote its fix list (OPEN, or ROUND 2 after an exit check)
            st = 'fix' if has(tid, 'polish.md') else 'refine'
        else:
            st = 'selfcheck' if has(tid, 'codex-review.md') else 'build'
    elif (f / 'spec.md').exists():
        st = 'spec'
    else:
        st = 'concept'
    return {'stage': st, 'art': f'{a}/{an}' if an else '-', 'voice': f'{v}/{vn}' if vn else '-',
            'verify': 'PASS' if 'PASS' in verdict else ('FIX' if verdict else ''), 'plan': 'yes' if (f / 'plan.md').exists() else '',
            'sub': 'yes' if (f / 'exit.md').exists() else ''}


def recess_rows():
    """Recess games (data/recess.json, docs/GAMES.md) sit outside the tool catalog. The board and the Desk count them too,
    as subject 'recess', with the shelf's grade band as their grade."""
    band = {'k2': 'k-2', '35': '3-5', '68': '6-8', '912': '9-12'}
    games = json.loads((ROOT / 'data' / 'recess.json').read_text(encoding='utf-8'))['games']
    return [{'tool_id': g['id'], 'title': g['title'], 'grade': band.get(g['band'], ''), 'subject': 'recess', 'format': 'game',
             'family': 'recess', 'concept': g['blurb']} for g in games]


# Each tool counts under the last step it has finished. Sign-off is counted on the Desk (items marked ready).
ORDER = ['concept', 'spec', 'build', 'selfcheck', 'refine', 'fix', 'exit', 'artvoice', 'finish', 'live']


def main():
    rows = list(csv.DictReader(open(ROOT / 'data' / 'tools-concepts.csv', encoding='utf-8'))) + recess_rows()
    waves = {}
    wf = ROOT / 'data' / 'waves.csv'
    if wf.exists():
        waves = {r['tool_id']: r['wave'] for r in csv.DictReader(open(wf, encoding='utf-8'))}
    for r in rows:
        r.update(row(r['tool_id'])); r['wave'] = waves.get(r['tool_id'], '')
    if '--wave' in sys.argv:
        w = sys.argv[sys.argv.index('--wave') + 1]
        for r in rows:
            if r['wave'] == w:
                print(f"{r['tool_id']:34} {r['stage']:9} verify {r['verify'] or '-':4} plan {r['plan'] or '-':3} sub {r['sub'] or '-':3} art {r['art']:6} voice {r['voice']}")
        return
    tot = {s: sum(r['stage'] == s for r in rows) for s in ORDER}
    out = ['# Build board', '', 'Generated by `python scripts/board.py` from the files in tools/. Do not edit by hand.', '',
           '| ' + ' | '.join(ORDER) + ' |', '|' + '---|' * len(ORDER), '| ' + ' | '.join(str(tot[s]) for s in ORDER) + ' |', '']
    for w in sorted({r['wave'] for r in rows if r['wave']}, key=lambda x: (len(x), x)):
        out += [f'## Wave {w}', '', '| Tool | Grade | Subject | Format | Family | Stage | Verify | Plan | Sub | Art | Voice |', '|---|---|---|---|---|---|---|---|---|---|---|']
        for r in [r for r in rows if r['wave'] == w]:
            out.append(f"| {r['title']} | {r['grade']} | {r['subject']} | {r['format']} | {r['family'] or ''} | {r['stage']} | {r['verify']} | {r['plan']} | {r['sub']} | {r['art']} | {r['voice']} |")
        out.append('')
    rec = [r for r in rows if r['subject'] == 'recess']
    if rec:
        out += ['## Recess', '', '| Game | Band | Stage | Verify | Art |', '|---|---|---|---|---|']
        out += [f"| {r['title']} | {r['grade'] or 'all'} | {r['stage']} | {r['verify']} | {r['art']} |" for r in rec]
        out.append('')
    (ROOT / 'docs' / 'BUILD-BOARD.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('  '.join(f'{s} {tot[s]}' for s in ORDER))


if __name__ == '__main__':
    main()

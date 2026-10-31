r"""Cory's Codex queue: paste blocks for each tool, and the worktrees they run in.

    python scripts/codex_queue.py prompts      rewrite docs/agents/codex-prompts-40.txt
    python scripts/codex_queue.py worktrees    make every missing worktree under S:\CurioClass-codex from origin/main
    python scripts/codex_queue.py sync         fast-forward worktrees whose tool is untouched, so they get brief fixes

Codex's sandbox can't create a worktree, so they are all made ahead of time. Cory opens S:\CurioClass-codex as the
Codex project and pastes one block per new chat. A build and its review use different ports, so they can overlap.
"""
import csv, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = Path('S:/CurioClass-codex')
OUT = ROOT / 'docs' / 'agents' / 'codex-prompts-40.txt'
RULE = '=' * 78
QUEUE = """game-day-fuel art-style-match virtual-gallery biome-atlas workplace-scenarios up-the-watershed reserve-designer
first-aid-responder data-policy-council act-it-out research-quest design-challenge-studio brand-builder speech-coach
design-for-a-friend credit-card-builder captain-s-choices model-mechanic grid-operator work-rate-crew spot-the-ai
shadow-measure rules-referee ph-mystery-liquids packaging-challenge me-vs-the-counter launch-pad keyword-fishing
is-the-historian-right input-or-output fire-lookout-triangles fair-dice-investigation design-the-study
courtroom-statistics code-kitchen zipline-energy water-shapes-earth theory-gym storyboard-studio traffic-light-coder""".split()
HELD = 'image-transformer pocket-universe span-and-spire near-and-far'.split()  # built before this queue, at the old paths
BUILD_PORTS = {'A': (9990, 8795), 'B': (9980, 8785), 'C': (9970, 8775)}
REVIEW_PORTS = {'A': (9960, 8765), 'B': (9950, 8755), 'C': (9940, 8745)}

HEADER = r"""CURIO CLASS: 40 CODEX TOOLS, PASTE AND WATCH

SET UP, ONCE
Open S:\CurioClass-codex as the project in Codex. All 40 worktrees are already made inside it.

EACH TOOL IS TWO PASTES, EACH IN ITS OWN NEW CHAT
1. BUILD. Paste it, watch it work. It makes the art as it goes. It ends with "Build done".
2. REVIEW. Paste it in a NEW chat, never the build chat: a reviewer who did not build it catches more. It fixes what it
   finds and ends with "Review done".

The work holds uncommitted in S:\CurioClass-codex\<tool-id> until Claude's Refine. Mark [x] as each step finishes.

HOW MANY AT ONCE
Up to three builds and three reviews, one of each from each group. Groups A, B and C use different ports, and reviews
use their own, so a build and a review never clash. Never run two builds, or two reviews, from the same group.

IF IT STICKS
If a command hangs for about 20 minutes, press Esc and paste:

That command hung, so I stopped it. Close any Chrome or server you started, note it under Left open in the report, and carry on with the next step.

If it says it is reconnecting, wait. If the model is at capacity, send: carry on
"""

BUILD = """Build the Curio Class tool {t}. Your worktree is {w}: every command runs from there, and you write only inside tools/{t}/. Read docs/agents/CODEX-BUILD.md first and follow it exactly. Scratch is {s}. This is Build only: make no git commits and do not start a polish round. Use Chrome ports {c} and host port {h}.

Graphics and gameplay come first. A tool that passes every check but looks plain or plays flat has failed. Make the images yourself with your image tool as you build, and try hard: use rich art wherever it lifts the tool. The owner can dial it back later. No people in generated images. Stay inside what the spec teaches. If the spec lists open questions, take the option it leans toward and note each one in handoff.md.

Before you build anything, tell me in five lines what the tool is, what the first 10 seconds look like, what the most satisfying moment will be, what makes later rounds different from the first, and which images you will make. Then go ahead without waiting for me. Put a time limit on every command. When tools/{t}/codex-report.md is written, say "Build done" and stop."""

REVIEW = """Review the Curio Class tool {t} cold. You did not build it. Your worktree is {w}: every command runs from there, and you write only inside tools/{t}/. Read {b}/CODEX-REVIEW.md first and follow it exactly, along with the rules in {b}/CODEX-BUILD.md. Scratch is {s}. Make no git commits. Use Chrome ports {c} and host port {h}.

Play it before you read what the builder said. Find what three blind reviewers would find, fix every blocker and should fix, and lift the flattest moment and the weakest art. Keep what is strong, and do not make it plainer. One pass only. Put a time limit on every command. When tools/{t}/codex-review.md is written, say "Review done" and stop."""


def group(i):
    return 'ABC'[i % 3]


def ports(table, g):
    c, h = table[g]
    return f'{c} to {c + 7}', h


def block(kind, title, text):
    return f'--- {kind}: {title} ---\n\n{text}\n\n--- end ---\n'


def prompts():
    with open(ROOT / 'data' / 'tools-concepts.csv', encoding='utf-8', newline='') as f:
        rows = {r['tool_id']: r for r in csv.DictReader(f)}
    parts = [HEADER, RULE, 'REVIEWS FOR THE FOUR TOOLS ALREADY BUILT', RULE, '',
             'These four sit at the old paths. For each one, open its own folder as the project in a new Codex chat, once its',
             'build has said "Build done". They had no images made during the build, so the review makes them.\n']
    for i, t in enumerate(HELD):
        g = group(i)
        c, h = ports(REVIEW_PORTS, g)
        scratch = f'C:/Users/Cory/AppData/Local/Temp/curio-codex/{t}'
        parts += [f'[ ] {rows[t]["title"]}  group {g}   Project folder: S:\\CurioClass-codex-{t}\n',
                  block('REVIEW', t, REVIEW.format(t=t, w=f'S:/CurioClass-codex-{t}', b='S:/CurioClass-media/docs/agents', s=scratch, c=c, h=h))]
    for i, t in enumerate(QUEUE):
        r, g = rows[t], group(i)
        w, s = f'{BASE.as_posix()}/{t}', f'{BASE.as_posix()}/_scratch/{t}'
        parts += [RULE, f'{i + 1} of {len(QUEUE)}: {r["title"]}  ({r["subject"]}, grade {r["grade"]})  group {g}', RULE, '']
        c, h = ports(BUILD_PORTS, g)
        parts += ['[ ] BUILD\n', block('BUILD', t, BUILD.format(t=t, w=w, s=s, c=c, h=h))]
        c, h = ports(REVIEW_PORTS, g)
        parts += ['[ ] REVIEW, in a new chat\n', block('REVIEW', t, REVIEW.format(t=t, w=w, b='docs/agents', s=s, c=c, h=h))]
    text = '\n'.join(parts)
    assert '\u2014' not in text
    OUT.write_text(text, encoding='utf-8', newline='\r\n')
    print(f'wrote {OUT}')


def git(*args, cwd=ROOT):
    return subprocess.run(['git', *args], cwd=cwd, capture_output=True, text=True)


def worktrees():
    git('fetch', '-q', 'origin')
    (BASE / '_scratch').mkdir(parents=True, exist_ok=True)
    for i, t in enumerate(QUEUE):
        (BASE / '_scratch' / t).mkdir(exist_ok=True)
        if (BASE / t).exists():
            continue
        made = git('worktree', 'add', '-q', str(BASE / t), '-b', f'codex/{t}', 'origin/main')
        print(f'{i + 1}/{len(QUEUE)} {t}', 'ok' if made.returncode == 0 else made.stderr.strip(), flush=True)


def sync():
    git('fetch', '-q', 'origin')
    for t in QUEUE:
        if not (BASE / t).exists():
            continue
        if git('status', '--porcelain', '--', f'tools/{t}', cwd=BASE / t).stdout.strip():
            print(f'{t}: started, left alone')
            continue
        done = git('merge', '-q', '--ff-only', 'origin/main', cwd=BASE / t)
        print(f'{t}:', 'up to date' if done.returncode == 0 else done.stderr.strip())


if __name__ == '__main__':
    {'prompts': prompts, 'worktrees': worktrees, 'sync': sync}[sys.argv[1]]()

r"""Cory's Codex queue. Every chat works in one shared checkout, S:\CurioClass-codex, on branch codex/queue.

    python scripts/codex_queue.py prompts    rewrite S:\CurioClass-codex\_queue.txt with only what is left to paste
    python scripts/codex_queue.py sync       bring the shared checkout up to origin/main, so it gets brief fixes
    python scripts/codex_queue.py clean      delete the scratch of every tool that has its review

What is done comes from the disk: codex-report.md means built, codex-review.md means reviewed. So the text file never
needs hand tidying. A build and a review use different ports, so they can overlap.
"""
import csv, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = Path('S:/CurioClass-codex')
OUT = BASE / '_queue.txt'
RULE = '=' * 78
QUEUE = """image-transformer near-and-far game-day-fuel art-style-match virtual-gallery biome-atlas workplace-scenarios
up-the-watershed reserve-designer first-aid-responder data-policy-council act-it-out research-quest
design-challenge-studio brand-builder speech-coach design-for-a-friend credit-card-builder captain-s-choices
traffic-light-coder pocket-universe span-and-spire design-fixer art-through-time gallery-critique
city-skyline-studio world-music-map band-practice theory-gym music-history-radio character-voice-booth
director-s-chair levels-and-pathways dance-pattern-puzzle choreography-board dance-styles-explorer flipbook-studio
storyboard-studio weekend-drawing-share hallway-art-museum traveling-art-show place-mood-makeover school-wall-mural
sketchbook-process-journal parade-and-bedtime-music name-song-practice recorder-concert-rehearsal
cartoon-soundtrack-mixer folk-song-arranger cover-version-review recital-practice-plan puppet-show-feelings
moon-base-drama neighborhood-issue-play audience-talkback three-viewpoints-scene scene-staging-comparison
stage-lighting-plot monologue-rehearsal feeling-scarf-dance family-dance-night poem-to-movement
recital-stage-directions dancers-on-tour dance-hall-decades choreography-for-a-cause museum-courtyard-performance
sound-and-picture-book field-trip-slideshow cereal-ad-questions stop-motion-clay-shoot toy-ad-reality-check
morning-show-crew viral-video-breakdown mini-documentary-crew model-mechanic grid-operator work-rate-crew
spot-the-ai shadow-measure rules-referee ph-mystery-liquids packaging-challenge me-vs-the-counter launch-pad
keyword-fishing is-the-historian-right input-or-output fire-lookout-triangles fair-dice-investigation
design-the-study courtroom-statistics code-kitchen zipline-energy water-shapes-earth""".split()
DANCE = ("Owner's decision: this tool should end up with painted dancers, not the code figure. Use the kit's figure for now, "
         "keep it easy to swap, and add the poses it will need to art/prompts.json with \"people\": true for the next painter.")
NOTES = {  # desk answers the spec does not hold yet (docs/agents/decisions/DESK-ANSWERS.md)
    'music-history-radio': "Owner's decision: add one station from outside the European and American line, with sourced facts.",
    'director-s-chair': "Owner's decision: the 5 masks are objects, not people, so paint them yourself. The masked actors stay figures in code.",
    'neighborhood-issue-play': "Owner's decision: restore the idea card's third problem, a new family who speaks another language, in place "
                               "of the empty lot. Write it as neighbors who can't yet talk to each other, never the family as the problem. "
                               "Its puppets are people, so list them with \"people\": true for the next painter.",
}
for _t in ("levels-and-pathways dance-pattern-puzzle choreography-board dance-styles-explorer feeling-scarf-dance family-dance-night "
           "poem-to-movement recital-stage-directions dancers-on-tour dance-hall-decades choreography-for-a-cause "
           "museum-courtyard-performance").split():
    NOTES[_t] = DANCE
BUILD_PORTS = {'A': (9990, 8795), 'B': (9980, 8785), 'C': (9970, 8775)}
REVIEW_PORTS = {'A': (9960, 8765), 'B': (9950, 8755), 'C': (9940, 8745)}

HEADER = r"""CURIO CLASS: CODEX QUEUE

This file lists only what is left. To refresh it, run: python S:\CurioClass-codex\scripts\codex_queue.py prompts

EVERY CHAT
Start it inside the CurioClass-codex project in Codex, using New chat under that project. A chat started anywhere else
lands in Documents\Codex and can't reach the tool. If that happens it will say so and stop, so just start it again.

EACH TOOL IS TWO PASTES, EACH IN ITS OWN NEW CHAT
BUILD ends with "Build done". REVIEW ends with "Review done". Never paste a review into the build chat: a reviewer who
did not build it catches more.

HOW MANY AT ONCE
Up to three builds and three reviews, one of each from each group (A, B, C). Never two builds, or two reviews, from the
same group. A refresh changes the groups, so let running chats finish first.

IF IT STICKS
If a command hangs for about 20 minutes, press Esc and paste:

That command hung, so I stopped it. Close any Chrome or server you started, note it under Left open in the report, and carry on with the next step.

If it says it is reconnecting, wait. If the model is at capacity, send: carry on
"""

BUILD = """Build the Curio Class tool {t}. Read docs/agents/CODEX-BUILD.md first and follow it exactly. Your folder must be S:\\CurioClass-codex; if it is not, say so and stop. Write only in tools/{t}/ and _scratch/{t}/. This is Build only: make no git commits and do not start a polish round. Use Chrome ports {c} and host port {h}.

Graphics and gameplay come first. A tool that passes every check but looks plain or plays flat has failed. Make the images yourself with your image tool as you build, and try hard: use rich art wherever it lifts the tool. The owner can dial it back later. No people in generated images. Stay inside what the spec teaches. If the spec lists open questions, take the option it leans toward and note each one in handoff.md.

Before you build anything, tell me in five lines what the tool is, what the first 10 seconds look like, what the most satisfying moment will be, what makes later rounds different from the first, and which images you will make. Then go ahead without waiting for me. Put a time limit on every command. When tools/{t}/codex-report.md is written, say "Build done" and stop."""

REVIEW = """Review the Curio Class tool {t} cold. You did not build it. Read docs/agents/CODEX-REVIEW.md first and follow it exactly, along with the rules in docs/agents/CODEX-BUILD.md. Your folder must be S:\\CurioClass-codex; if it is not, say so and stop. Write only in tools/{t}/ and _scratch/{t}/. Make no git commits. Use Chrome ports {c} and host port {h}.

Play it before you read what the builder said. Find what three blind reviewers would find, fix every blocker and should fix, and lift the flattest moment and the weakest art. Keep what is strong, and do not make it plainer. One pass only. Put a time limit on every command. When tools/{t}/codex-review.md is written, say "Review done" and stop."""


def group(i):
    return 'ABC'[i % 3]


def ports(table, g):
    c, h = table[g]
    return f'{c} to {c + 7}', h


def block(kind, t, text):
    note = f'\n\n{NOTES[t]}' if t in NOTES else ''
    return f'--- {kind}: {t} ---\n\n{text}{note}\n\n--- end ---\n'


def state(t):
    folder = BASE / 'tools' / t
    return (folder / 'codex-report.md').exists(), (folder / 'codex-review.md').exists()


def prompts():
    with open(ROOT / 'data' / 'tools-concepts.csv', encoding='utf-8', newline='') as f:
        rows = {r['tool_id']: r for r in csv.DictReader(f)}
    states = {t: state(t) for t in QUEUE}
    reviewed = [t for t, (_, v) in states.items() if v]
    waiting = [t for t, (b, v) in states.items() if b and not v]
    unbuilt = [t for t, (b, _) in states.items() if not b]
    parts = [HEADER, RULE, f'{len(reviewed)} reviewed, {len(waiting)} built and waiting for review, {len(unbuilt)} to build', RULE,
             '', 'Done: ' + (', '.join(reviewed) or 'none'), '']
    if waiting:
        parts += [RULE, 'REVIEWS TO PASTE', RULE, '']
    for i, t in enumerate(waiting):
        g = group(i)
        c, h = ports(REVIEW_PORTS, g)
        parts += [f'{rows[t]["title"]}  group {g}\n', block('REVIEW', t, REVIEW.format(t=t, c=c, h=h))]
    if unbuilt:
        parts += [RULE, 'BUILDS TO PASTE (the review for each one appears here after you refresh)', RULE, '']
    for i, t in enumerate(unbuilt):
        r, g = rows[t], group(i)
        c, h = ports(BUILD_PORTS, g)
        parts += [f'{r["title"]}  ({r["subject"]}, grade {r["grade"]})  group {g}\n', block('BUILD', t, BUILD.format(t=t, c=c, h=h))]
    text = '\n'.join(parts)
    assert '\u2014' not in text
    OUT.write_text(text, encoding='utf-8', newline='\r\n')
    print(f'{OUT}: {len(reviewed)} reviewed, {len(waiting)} to review, {len(unbuilt)} to build')


def git(*args):
    return subprocess.run(['git', *args], cwd=BASE, capture_output=True, text=True)


def sync():
    git('fetch', '-q', 'origin')
    done = git('merge', '-q', '--ff-only', 'origin/main')
    print('up to date' if done.returncode == 0 else done.stderr.strip())


def clean():
    for t in QUEUE:
        scratch = BASE / '_scratch' / t
        if state(t)[1] and scratch.exists():
            shutil.rmtree(scratch, ignore_errors=True)
            print(f'cleaned {t}')


if __name__ == '__main__':
    {'prompts': prompts, 'sync': sync, 'clean': clean}[sys.argv[1]]()

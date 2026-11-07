r"""Cory's Codex queue. Every chat works in one shared checkout, S:\CurioClass-codex, on branch codex/queue.

    python scripts/codex_queue.py prompts    rewrite S:\CurioClass-codex\_queue.txt with only what is left to paste
    python scripts/codex_queue.py sync       bring the shared checkout up to origin/main, so it gets brief fixes
    python scripts/codex_queue.py clean      delete the scratch of every tool that has its review

What is done comes from the disk: codex-report.md means built, codex-review.md means reviewed. So the text file never
needs hand tidying. A build and a review use different ports, so they can overlap.

Fixes (docs/agents/CODEX-FIX.md): a tool in FIX with a refine.md whose first line is OPEN or ROUND 2 and no polish.md
wants a fix. Its own ports, so a fix overlaps builds and reviews too.
"""
import csv, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = Path('S:/CurioClass-codex')
OUT = BASE / '_queue.txt'
RULE = '=' * 78
QUEUE = """nonsense-words image-transformer near-and-far game-day-fuel art-style-match virtual-gallery biome-atlas workplace-scenarios
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
design-the-study courtroom-statistics code-kitchen zipline-energy water-shapes-earth
energy-accountant medical-test-paradox data-table-builder personal-essay-studio usage-panel body-thermostat
algebra-tile-studio
gas-law-lab punnett-predictor misleading-charts phishing-spotter paycheck-decoder fallacy-field-guide mole-bakery
equation-balancer rigid-motion-twins thesis-workshop star-life-story globe-theatre-stage""".split()
# Added 2026-11-05 (Cory: the token budget has room). circuit-builder and sound-studio stay out: they overlap the
# Circuit Bench and Voice Lab instruments.
# Refined tools whose fixes Codex makes (Cory, 2026-11-04). The merged list is tools/<id>/refine.md, brought over from main.
# sight-words left the queue 2026-11-04: it is live on the site, so a Codex review would rework a live tool (Cory).
FIX = """city-skyline-studio levels-and-pathways first-aid-responder music-history-radio span-and-spire pocket-universe
sky-dome living-earth virtual-gallery flipbook-studio puppet-show-feelings moon-base-drama
circuit-bench voice-lab microscope-bench poets-workbench
graph-studio compass-and-straightedge cipher-vault molecule-forge living-pond
safety-sweep-house traffic-light-coder research-quest up-the-watershed
worry-size-sorter bus-stop letter-lanterns line-leader-picker""".split()
# 2026-11-05 evening: Claude Refine (lenses + merge) done in the Codex checkout, then Codex fixes first in the run (Cory).
# span-and-spire and pocket-universe: the instruments pivot (Cory, 2026-11-04); their refine.md is a pivot list.

# Curiosities (Cory, 2026-11-05): first in the queue, with their own build and review prompts (CURIO_BUILD, CURIO_REVIEW
# below) so nothing of the lesson-tool brief bleeds in. Each joins the queue only once its spec is in the Curiosity shape.
CURIO = """voice-lab living-earth sky-dome microscope-bench circuit-bench graph-studio compass-and-straightedge
poets-workbench cipher-vault molecule-forge living-pond
safety-sweep-house traffic-light-coder research-quest up-the-watershed
worry-size-sorter bus-stop letter-lanterns line-leader-picker""".split()


def curio_ready(t):
    spec = BASE / 'tools' / t / 'spec.md'
    return spec.exists() and '(Curiosity No.' in spec.read_text(encoding='utf-8', errors='replace')[:400]


# Spec test (Cory, 2026-11-05): ten specs written under SPEC.md's "Lessons from ten full Refines", built right after
# the Curiosities so their Refine counts can be compared (docs/agents/MEASURE-FIRST.md). The run caps stay as set, so
# the end of the list waits for the next run.
SPEC_TEST = """safety-sweep-house worry-size-sorter bus-stop letter-lanterns line-leader-picker bug-hunt
warming-evidence-desk cocoa-chain roller-coaster-rounding the-buyout""".split()
# Second spec test (2026-11-06): the first specs written in the new format (SPEC.md's "Can it be beaten?" and "Heard in
# order" sections). Their Refines check the 2026-11-06 decision in docs/agents/MEASURE-FIRST.md.
SPEC_TEST_2 = """estimation-station which-way-is-down box-plot-builder story-graphs illusion-lab""".split()
# Third spec batch (2026-11-06), same new format, spec checked like the second.
SPEC_TEST_3 = """vibration-station skate-park-angles cooler-challenge lunch-survey-cleanup trade-island""".split()
# Fourth spec batch (2026-11-06); trade-island's factory card was also revised (no Rana Plaza).
SPEC_TEST_4 = """push-the-pumpkin egg-carton-factory scarf-juggling-ladder interest-rate-dial electromagnet-lab""".split()
# Fifth spec batch (2026-11-07).
SPEC_TEST_5 = """tap-to-start-puppets paper-plane-assembly-line box-packer front-line leaf-factory""".split()
_SPEC = SPEC_TEST + SPEC_TEST_2 + SPEC_TEST_3 + SPEC_TEST_4 + SPEC_TEST_5
QUEUE = ([t for t in CURIO if curio_ready(t)] + _SPEC
         + [t for t in QUEUE if t not in CURIO and t not in _SPEC])
DANCE = ("Owner's decision: this tool gets painted dancers, not the code figure. Paint them yourself, marked \"people\": true, "
         "with a natural range of dancers. Draw the fewest poses that teach the moves well, and keep the figure easy to swap.")
NOTES = {  # desk answers the spec does not hold yet (docs/agents/decisions/DESK-ANSWERS.md)
    'music-history-radio': "Owner's decision: add one station from outside the European and American line, with sourced facts.",
    'director-s-chair': "Owner's decision: the 5 masks are objects, not people, so paint them yourself. The masked actors stay figures in code.",
    'neighborhood-issue-play': "Owner's decision: restore the idea card's third problem, a new family who speaks another language, in place "
                               "of the empty lot. Write it as neighbors who can't yet talk to each other, never the family as the problem. "
                               "Its puppets are people: paint them yourself, marked \"people\": true.",
}
PLAIN = ("Owner's decision: this tool is plain on purpose, for a grade 2 teacher. The spec's Look section wins over the push for rich art "
         "and gameplay above: parchment, a blue border, one quiet word at a time, one small flourish in the top bar. Build it as a sibling "
         "of the other word tool (nonsense-words and sight-words share a layout).")
NOTES['nonsense-words'] = NOTES['sight-words'] = PLAIN
# Rebuilds (Cory, 2026-11-05: "go back to the data starved ones and do them right"). The runner adds these to the build
# prompt only. The first build's report was renamed codex-report-1.md, so the tool counts as unbuilt again.
_REDO = ("Second build (owner's decision, Cory, 2026-11-05). The first build of this Curiosity ran before the sandbox had "
         "network access, so it came out without its real material. Its report is tools/{t}/codex-report-1.md: read it, "
         "above all Left open, before you plan. Keep what works in the existing files and do it right this time: gather the "
         "real material the spec names, as \"Gathering data\" in the brief says (network is on now, and for this build the "
         "gathering cap is 75 minutes, not 45), then build the parts that were left out for lack of it. The instrument "
         "should feel finished, not a frame waiting for data. Write a fresh tools/{t}/codex-report.md covering the whole "
         "tool; under Built, say what changed from the first build. Leave codex-report-1.md where it is.")
REDO = {t: _REDO.format(t=t) + ' ' + more for t, more in {
    'living-earth': "First build's gaps: the earthquake catalogue (M5.0, or the spec's M5.5 fallback), ETOPO relief, Natural "
                    "Earth, NOAA volcanoes and licensed plate material, and the layers, city search, plate and volcano "
                    "readouts and Rewind that depend on them.",
    'sky-dome': "First build's gaps: the full star catalogue fields (including B-V colour), the Natural Earth place list, "
                "checked distances, the full constellation figure set and the deep-sky markers, each confirmed against two "
                "sources.",
    'microscope-bench': "First build's gaps: genuinely scaled real micrographs under PD, CC0 or CC BY with their scale, the "
                        "specimen and prepared-slide tray, stains and mounts, pond motion and focal stacks. This is the heart "
                        "of the instrument: without real images it is not a microscope.",
}.items()}
EXTRA = {}  # tools outside the catalog, as {'id': {'title': ..., 'subject': ..., 'grade': ...}}
for _t in ("levels-and-pathways dance-pattern-puzzle choreography-board dance-styles-explorer feeling-scarf-dance family-dance-night "
           "poem-to-movement recital-stage-directions dancers-on-tour dance-hall-decades choreography-for-a-cause "
           "museum-courtyard-performance").split():
    NOTES[_t] = DANCE
BUILD_PORTS = {'A': (9990, 8795), 'B': (9980, 8785), 'C': (9970, 8775)}
REVIEW_PORTS = {'A': (9960, 8765), 'B': (9950, 8755), 'C': (9940, 8745), 'D': (9930, 8735)}
FIX_PORTS = {'A': (9920, 8725), 'B': (9910, 8715)}

HEADER = r"""CURIO CLASS: CODEX QUEUE

This file lists only what is left. To refresh it, run: python S:\CurioClass-codex\scripts\codex_queue.py prompts

EVERY CHAT
Start it inside the CurioClass-codex project in Codex, using New chat under that project. A chat started anywhere else
lands in Documents\Codex and can't reach the tool. If that happens it will say so and stop, so just start it again.

EACH TOOL IS TWO PASTES, EACH IN ITS OWN NEW CHAT
BUILD ends with "Build done". REVIEW ends with "Review done". Never paste a review into the build chat: a reviewer who
did not build it catches more.

HOW MANY AT ONCE
Up to three builds (groups A, B, C) and four reviews (groups A, B, C, D) at once. Never two builds, or two reviews, from
the same group. A refresh changes the groups, so let running chats finish first.

AWAY FROM THE PC
Start Menu > Codex Queue runs these blocks for you, each in its own fresh session, until the queue is empty or the usage
limit is reached. Log: S:\CurioClass-codex\_runner\summary.txt. Don't paste by hand while it runs.

IF IT STICKS
If a command hangs for about 20 minutes, press Esc and paste:

That command hung, so I stopped it. Close any Chrome or server you started, note it under Left open in the report, and carry on with the next step.

If it says it is reconnecting, wait. If the model is at capacity, send: carry on
"""

BUILD = """Build the Curio Class tool {t}. Read docs/agents/CODEX-BUILD.md first and follow it exactly. Your folder must be S:\\CurioClass-codex; if it is not, say so and stop. Write only in tools/{t}/ and _scratch/{t}/. This is Build only: make no git commits and do not start a polish round. Use Chrome ports {c} and host port {h}.

Graphics and gameplay come first. A tool that passes every check but looks plain or plays flat has failed. Make the images yourself with your image tool as you build, and try hard: use rich art wherever it lifts the tool. The owner can dial it back later. You may draw people where the scene needs them; mark each one \"people\": true. Stay inside what the spec teaches. If the spec lists open questions, take the option it leans toward and note each one in handoff.md. Try to cheat every score and check you build, and fix any cheat that passes.

Before you build anything, tell me in seven lines what the tool is, what the first 10 seconds look like, what the most satisfying moment will be, what makes later rounds different from the first, which images you will make, your size budget (images and voice, in KB, against the 2 MB goal), and any place the spec contradicts itself or the brief. Then go ahead without waiting for me. Put a time limit on every command. When tools/{t}/codex-report.md is written, say "Build done" and stop."""

REVIEW = """Review the Curio Class tool {t} cold. You did not build it. Read docs/agents/CODEX-REVIEW.md first and follow it exactly, along with the rules in docs/agents/CODEX-BUILD.md. Your folder must be S:\\CurioClass-codex; if it is not, say so and stop. Write only in tools/{t}/ and _scratch/{t}/. Make no git commits. Use Chrome ports {c} and host port {h}.

Play it before you read what the builder said. Try to break every score and check the cheap way, walk the main path with the voice on, and hold every fact to a named source. Find what three blind reviewers would find, fix every blocker and should fix, and lift the flattest moment and the weakest art. Keep what is strong, and do not make it plainer. One pass only. Put a time limit on every command. When tools/{t}/codex-review.md is written, say "Review done" and stop."""


FIXP = """Fix the Curio Class tool {t} from its Claude Refine. Read docs/agents/CODEX-FIX.md first and follow it exactly, along with the rules in docs/agents/CODEX-BUILD.md. Your folder must be S:\\CurioClass-codex; if it is not, say so and stop. Write only in tools/{t}/ and _scratch/{t}/. Make no git commits and do not edit refine.md. Use Chrome ports {c} and host port {h}.

The list is tools/{t}/refine.md. Reproduce each blocker and should fix before you fix it, fix the cause, and prove every fix with a frame or a number at the size the item names. For every score, check or meter an item touches, try the cheapest way to pass without the skill after your fix. Mark an item FIXED only when you saw it fixed. Put a time limit on every command. When tools/{t}/polish.md is written, say "Fix done" and stop."""

CURIO_BUILD = """Build the Curio Class Curiosity {t}. This is a Curiosity, not a lesson tool. Read docs/agents/CODEX-CURIOSITY.md first and follow it exactly: it replaces docs/agents/CODEX-BUILD.md, and you read only the sections of CODEX-BUILD.md it names. Your folder must be S:\\CurioClass-codex; if it is not, say so and stop. Write only in tools/{t}/ and _scratch/{t}/. This is Build only: make no git commits and do not start a polish round. Use Chrome ports {c} and host port {h}.

Build the real instrument the spec describes, working on real rules and real material, filling the screen, with the family marks of Span and Spire and Pocket Universe (maker's plate and Manual drawer lower-left, Motion, Sound and Read on its own power panel). No score, goal, level, sticker, quiz, finish screen, mode pills or kit header, even where a habit says to add one. Draw the working surface in code so the material stays exact; paint only real objects or places that add something.

Before you build anything, tell me in seven lines what real instrument this is, what the first two minutes look like with nothing read, what a month of use would still find, which controls and readouts it has, which images (if any) you will make, your size budget against the 2 MB goal, and any place the spec contradicts the brief. Then go ahead without waiting for me. Put a time limit on every command. When tools/{t}/codex-report.md is written, say "Build done" and stop."""

CURIO_REVIEW = """Review the Curio Class Curiosity {t} cold. You did not build it. This is a Curiosity, not a lesson tool: read docs/agents/CODEX-CURIOSITY.md first, including "For the reviewer", then docs/agents/CODEX-REVIEW.md for the process and report file. Judge it against the Curiosity brief and the short test, never against lesson norms. Your folder must be S:\\CurioClass-codex; if it is not, say so and stop. Write only in tools/{t}/ and _scratch/{t}/. Make no git commits. Use Chrome ports {c} and host port {h}.

Play it before you read what the builder said. Try to break the instrument (extreme values, every control at both ends, rapid input, resize while running), walk it with the voice on, and hold every dataset and fact to a named source and licence. Never add a goal, score, level, quiz, finish screen or kit header; remove any that slipped in. If it fails a question of the short test, make the real material more central. Fix every blocker and should fix, lift the flattest moment, keep what is strong. One pass only. Put a time limit on every command. When tools/{t}/codex-review.md is written, say "Review done" and stop."""


class _Pick(str):
    """A prompt template that hands a Curiosity its own prompt. The runner calls template.format(t=..., c=..., h=...)."""
    def __new__(cls, plain, curio):
        s = super().__new__(cls, plain)
        s.curio = curio
        return s

    def format(self, *a, **k):
        return (self.curio if k.get('t') in CURIO else str(self)).format(*a, **k)


BUILD = _Pick(BUILD, CURIO_BUILD)
REVIEW = _Pick(REVIEW, CURIO_REVIEW)
CURIO_FIX = """Fix the Curio Class Curiosity {t} from its Claude Refine. This is a Curiosity, not a lesson tool: read docs/agents/CODEX-CURIOSITY.md first, then docs/agents/CODEX-FIX.md for the process and polish.md report, and the rules in docs/agents/CODEX-BUILD.md that the Curiosity brief names. Where the fix brief or the gate leans on lesson norms (a welcome, a goal, a score, a finish), the Curiosity brief wins: never add a goal, score, level, quiz, finish screen or kit header. Your folder must be S:\\CurioClass-codex; if it is not, say so and stop. Write only in tools/{t}/ and _scratch/{t}/. Make no git commits and do not edit refine.md. Use Chrome ports {c} and host port {h}.

The list is tools/{t}/refine.md. Reproduce each blocker and should fix before you fix it, fix the cause, and prove every fix with a frame or a number at the size the item names. Hold every fact and dataset you touch to a named source and licence; you may go online to gather or re-check material as the Curiosity brief's "Gathering data" says. Mark an item FIXED only when you saw it fixed. Put a time limit on every command. When tools/{t}/polish.md is written, say "Fix done" and stop."""
FIXP = _Pick(FIXP, CURIO_FIX)
EXTRA.update({
    'voice-lab': {'title': 'Voice Lab', 'subject': 'science', 'grade': '8'},
    'living-earth': {'title': 'Living Earth', 'subject': 'science', 'grade': '6'},
    'sky-dome': {'title': 'Sky Dome', 'subject': 'science', 'grade': '1'},
    'microscope-bench': {'title': 'Microscope Bench', 'subject': 'science', 'grade': '6'},
    'circuit-bench': {'title': 'Circuit Bench', 'subject': 'science', 'grade': '8'},
    'graph-studio': {'title': 'Graph Studio', 'subject': 'math', 'grade': '9'},
    'compass-and-straightedge': {'title': 'Compass and Straightedge', 'subject': 'math', 'grade': '10'},
    'poets-workbench': {'title': "Poet's Workbench", 'subject': 'ela', 'grade': '7'},
})


def group(i, groups='ABC'):
    return groups[i % len(groups)]


def ports(table, g):
    c, h = table[g]
    return f'{c} to {c + 7}', h


def block(kind, t, text):
    note = f'\n\n{NOTES[t]}' if t in NOTES else ''
    return f'--- {kind}: {t} ---\n\n{text}{note}\n\n--- end ---\n'


def state(t):
    folder = BASE / 'tools' / t
    return (folder / 'codex-report.md').exists(), (folder / 'codex-review.md').exists()


def fix_wanted(t):
    folder = BASE / 'tools' / t
    if t not in FIX or (folder / 'polish.md').exists() or not (folder / 'refine.md').exists():
        return False
    with open(folder / 'refine.md', encoding='utf-8') as f:
        first = f.readline().strip()
    return first.startswith(('OPEN', 'ROUND 2'))


def prompts():
    with open(ROOT / 'data' / 'tools-concepts.csv', encoding='utf-8', newline='') as f:
        rows = {r['tool_id']: r for r in csv.DictReader(f)}
    rows.update(EXTRA)
    states = {t: state(t) for t in QUEUE}
    reviewed = [t for t, (_, v) in states.items() if v]
    waiting = [t for t, (b, v) in states.items() if b and not v]
    unbuilt = [t for t, (b, _) in states.items() if not b]
    fixes = [t for t in FIX if fix_wanted(t)]
    parts = [HEADER, RULE, f'{len(reviewed)} reviewed, {len(waiting)} built and waiting for review, {len(unbuilt)} to build, '
             f'{len(fixes)} to fix', RULE, '', 'Done: ' + (', '.join(reviewed) or 'none'), '']
    if fixes:
        parts += [RULE, 'FIXES TO PASTE (from a Claude Refine; each ends with "Fix done")', RULE, '']
    for i, t in enumerate(fixes):
        g = group(i, 'AB')
        c, h = ports(FIX_PORTS, g)
        parts += [f'{rows[t]["title"]}  group {g}\n', block('FIX', t, FIXP.format(t=t, c=c, h=h))]
    if waiting:
        parts += [RULE, 'REVIEWS TO PASTE', RULE, '']
    for i, t in enumerate(waiting):
        g = group(i, 'ABCD')  # four reviews at once, three builds (Cory, 2026-11-03)
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
    print(f'{OUT}: {len(reviewed)} reviewed, {len(waiting)} to review, {len(unbuilt)} to build, {len(fixes)} to fix')


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

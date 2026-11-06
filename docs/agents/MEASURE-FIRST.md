# Measure first: does Claude's Refine still find much after a Codex review? (2026-11-04)

Cory's call: full Claude Refine on 5 Codex-built, Codex-reviewed tools, run 2, then 2, then 1, with a go-ahead
between batches. Bar from the desk card (q-measure-first): no blockers and 3 or fewer should fix per tool on average
means Codex's review can replace Refine (one Claude exit check after it). Otherwise the full Refine stays.
The lenses do not read codex-report.md or codex-review.md.

| Tool | Built | Round 1 blockers | Should fix | Polish accepted | Lens tokens | Before Codex (10-28 Refine) |
|---|---|---|---|---|---|---|
| city-skyline-studio | 11-01 | 1 | 10 | 8 | 657k | 0 / 14 / 14 |
| levels-and-pathways | 11-01 | 0 | 6 | 11 | 707k | 2 / 10 / 8 |
| first-aid-responder | 10-31 | 1 | 13 | 10 | 563k | none |
| music-history-radio | 11-01 | 1 | 14 | 18 | 748k (incl. sensitivity 117k) | none |

Batch 1 (look and merge only, plus a 20 minute shared audit per tool): 1.36M lens tokens for two tools, about 20 to
25 minutes of wall time with all six lenses at once. Polish and exit check not yet run.

Batch 2: 1.31M lens tokens for two tools (music-history-radio also needed the sensitivity agent, which FAILED it on
gamelan's date and how Black musicians are credited). Both blockers are teaching errors a student would carry away
(a CPR score that rewards pausing; a living tradition dated by when Europeans heard it).

## Spec test (2026-11-05): do the new SPEC.md rules lower Refine counts?

SPEC.md gained "Lessons from ten full Refines" (commit edb985fa). Ten new specs were written under it:
safety-sweep-house, worry-size-sorter, bus-stop, letter-lanterns, line-leader-picker, bug-hunt,
warming-evidence-desk, cocoa-chain, roller-coaster-rounding, the-buyout (grades K to 12, seven subjects).

Baseline to beat (round 1 Refine on Codex-built tools from older specs, ten tools): 9 blockers (0.9 per tool),
99 should fix (9.9 per tool). About half the blockers traced to the spec (unchecked facts, scores rewarding the
wrong thing, standards half taught).

Measure: build each with Codex (build plus Codex review), run the same Claude Refine (shared audit, three lenses,
merge), and count blockers and should fix, and how many trace to the spec. Spec cost: about 140k to 210k Claude
tokens each, 7 to 15 minutes.

### First five results (2026-11-06)

Round 1 Refine (shared audit, three lenses, merge; a fresh sensitivity agent on worry-size-sorter), merges asked to
trace each item to the spec or the build:

| Tool | Grade | Blockers | Should fix | Traced to spec (B / SF) |
|---|---|---|---|---|
| safety-sweep-house | K-2 | 0 | 15 | not traced (merged 2026-11-05, before tracing was asked) |
| line-leader-picker | K | 0 | 12 | 0 / 6 |
| worry-size-sorter | 3-5 | 1 | 12 | 1 / 8 |
| bus-stop | K-1 | 2 | 9 | 1 / 4 |
| letter-lanterns | K | 3 | 15 | 1 / 7 |
| **Five tools** | | **6 (1.2 a tool)** | **63 (12.6 a tool)** | 3 of 6 blockers; 25 of 48 should fix (four tools) |

Baseline: 0.9 blockers and 9.9 should fix a tool, about half of blockers from the spec. So far the new SPEC.md rules
have not lowered the counts: both are higher, and about half of what is found still traces to the spec. Spec-traced
items that repeat: checks that give the answer away or can be beaten without the skill (bus-stop Express strip and
totals, letter-lanterns elimination and fixed answer spots, line-leader chart, worry goal reason), and voice lines
for pre-readers (letter names for sounds, feedback after the next question, how-to lines never heard). Caveats: five
tools, four of them K-1 with full voice (more voice items than the mostly older baseline set), and the lenses now
use a shared audit plus stricter briefs, so part of the rise may be the instrument. Five more (bug-hunt,
warming-evidence-desk, cocoa-chain, roller-coaster-rounding, the-buyout) are queued for Codex review.

### Decision (Claude integrator, at Cory's "decide now", 2026-11-06)

Keep writing specs: about half of all Refine findings trace to them, so a weaker spec costs more later. Change how the
lessons reach the spec: SPEC.md now requires two filled sections, "Can it be beaten?" (every check against every
no-skill path) and "Heard in order" (K-2 line order and waits), because the same two gaps recurred even with the
rules written down. The five remaining spec-test tools still go through Refine as more data on the old format; the
next specs use the new sections, and their first five Refines are the check on this change.

### Second spec test (new format, 2026-11-06)

The first five specs written with SPEC.md's required "Can it be beaten?" and "Heard in order" sections. They are queued
for Codex as SPEC_TEST_2 in scripts/codex_queue.py, right after SPEC_TEST. Their Refine counts check the decision above:
if the two sections work, fewer blockers and should-fix items trace back to the spec.

| Tool | Grade | Subject | Spec tokens | Minutes | Lines |
|---|---|---|---|---|---|
| estimation-station | 2 | math | 179,490 | 11.7 | 201 |
| which-way-is-down | 5 | science | 166,424 | 9.1 | 324 |
| box-plot-builder | 6 | math | 209,409 | 13.6 | 316 |
| story-graphs | 8 | math | 207,392 | 15.1 | 204 |
| illusion-lab | 12 | psychology | 188,594 | 13.4 | 354 |
| **Average** | | | **190,262** | **12.6** | |

Each spec ran on one Opus agent; all five ran in parallel (about 15 minutes of wall time). The cost sits inside the
old range (about 140k to 210k tokens), so the two new sections did not make specs dearer. The spec check (overlaps,
voices, accents, names, both new sections, and a rerun of story-graphs' number checks) found nothing to fix. Three
specs run over the 300-line guide, mostly because of the two new tables.

### Third spec batch (new format, 2026-11-06)

Five more concept-stage tools specced in the new format, one Opus agent each, mixed bands and four subjects. Queued as
SPEC_TEST_3 in scripts/codex_queue.py.

| Tool | Grade, subject | Tokens | Minutes |
|---|---|---|---|
| vibration-station | 1, science | 190,522 | 11.5 |
| skate-park-angles | 4, math | 157,477 | 7.8 |
| cooler-challenge | 6, science | 236,394 | 16.8 |
| lunch-survey-cleanup | 6-8, computer science | 224,522 | 13.3 |
| trade-island | 12, social studies | 230,418 | 14.1 |
| Average | | 207,867 | 12.7 |

Total about 1.04M, close to the second test's 190k average. Spec check: every section present, "Can it be beaten?" and
"Heard in order" filled, no em dashes, voices and accents all distinct, lengths 198 to 306 lines. Three items for Cory:
lunch-survey-cleanup asks to use a made-up survey (data-desk family rule asks for real data) and moved the blanks from
the English learners' class to grade 6 paper forms; trade-island carries a Rana Plaza 2013 case card, which needs the
fresh sensitivity review before build.

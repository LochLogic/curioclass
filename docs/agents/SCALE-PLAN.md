# Scale plan: the remaining ~505 tools (unlocked 2026-10-27)

Agreed with Cory on 2026-10-26. It waited for the CS batch (robot-dance, computer-builder, score-keeper, game-remix,
code-tracer), which was fully done on 2026-10-27: all five live, voiced, planned and approved. Start when Cory says go.
The live count is now 76, not 74.

## Why

Specs, art and voice batch well, but only once their inputs have settled. The slow, costly part is build, verify, fix,
and most fix rounds catch the same voice bugs again and again: a stale line, lines out of order, the first-tap race, a
missing how-to, nagging. So: fix that class of bug once in the kit, clear overlaps across the whole catalog before
writing specs, and batch each step only after its inputs are final.

## Order

1. **In parallel (they touch different files):**
   - **Overlap pass** over every remaining one-line concept (data/concepts/*.txt):
     - Tag each concept with three things: the skill taught, what the student does (sort, build, trace, predict...),
       and the setting or metaphor.
     - "Too alike" means two of those three match within the same grade band. The same skill in another band is
       usually a spiral, which is fine.
     - The 76 live tools are fixed points: concepts move away from them, never the reverse.
     - Report gaps (thin subjects or bands, skills with no tool) as well as clashes, since a clashing concept may
       best move into a gap.
     - One agent tags and clusters; a second, cold agent checks the clusters.
     - Output: a decision list for Cory, not edits. Each cluster gets a suggested keep, reshape, merge or
       move-to-gap.
   - **Shared narration helper** in kit/curio.js (`Curio.voice`):
     - Covers the queue, valid-at-play-time checks, once keys, how-to lines spoken once then shown in the hint only,
       hush, Read, the first-tap welcome, Sound on and off with pacing, and one standard `log`.
     - Build it from computer-builder's version, the most battle-tested one. Two kinds of line from the start (CS
       batch lesson): how-to and teaching lines spoken once, and event lines (praise, results, failures) spoken every
       time and still dropped when stale. A skipped welcome stays unmarked, and the line must match the state.
     - Escape hatch: "speak now and wait", for timing-bound tools (music, Pause/Step).
     - Ship it with a small test page, then a pilot tool that goes through verify.
     - VERIFY gains a standard voice check: repeats, stale lines, first-tap timing.
     - New tools use it. Live tools move over only when touched, starting with the four early grade 11 tools that
       still have the first-tap race. No mass retrofit.
2. **Cory decides the clusters.** Concept edits then go in data/concepts/*.txt, never the CSV
   (`check_concepts.py --write` reverts edits made only in the CSV).
3. **Spec waves** of about 30 to 50 tools, one subject or band at a time, each with its own overlap check (RUNBOOK
   "Spec check").
4. **Art overnight per wave**, right after the spec check:
   - Cloudflare FLUX (free daily allowance), Codex `gptart.py` (usage cap), or local FLUX (about 17 GB of RAM).
   - Expect about 10 to 20 percent to be redone during builds.
5. **Builds stream** on the new helper in small mixed Build and Refine waves (RUNBOOK, Wave cadence; REFINE.md), then
   big build-only waves per family once its Refine counts fall. At most about 3 to 4 agents.
6. **Voice nights per refined group**, only after Refine passes:
   - Narration lines change during fix rounds (game-remix went from 35 to 49 in one round, then to 42 when Cory cut Share).
   - After each voice night, run `scripts/voice_liveliness.py` and redo only clearly flat takes (`localvoice.py --redo`);
     the check is gentle on purpose, and a flag or two per tool can stay.
   - Local Qwen takes about 1 to 2 s per line, roughly 10 to 15 GPU hours for the whole catalog.
   - Voice and FLUX cannot share the 16 GB card, so art nights and voice nights alternate.
7. **Reviews per wave** on the Review Desk instead of one at a time.

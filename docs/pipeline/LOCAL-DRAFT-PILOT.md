# Local-model drafting: the pilots (days set up 2026-11-26, not run; section plans running 2026-11-26)

Cory 2026-11-26: "could we then use a local, academic LLM to draft all the days? then have you or codex run the fixes
and then a refinement that's done only by you?" Set up, not run, on his word. The question it answers: does a free
local draft plus a fix pass cost less than writing the day fresh, at the same bar?

## The shape being tested

1. **Skeleton** (scripts/day_skeleton.py): every mechanical field from data; every judgment field a TODO(writer).
2. **Local draft** (scripts/local_draft.py): the local model fills only the TODO(writer) holes, from the skeleton,
   LESSON-DAY.md, the section plan's day block and one finished day of the same kind from another course.
3. **Gates**: lesson.py's day checks on the draft (`local_draft.py check`).
4. **Fix**: Codex or Claude, against the gates and the bar.
5. **Refine**: Claude only, as now.

What the local model never does: write a key (keys stay computed in items.csv), choose a standard, supply or link
(those are skeleton facts), or build the pieces a day leans on (cards, records, family notes). The pilot drafts the
day file only.

## The pilot set

science-grade-1, days 1 to 8 (unit 1, sections 1.1 and 1.2: three Understanding, one Application, two Fluency, one
Check, one Respond). Cory signed science K to 3 off on 2026-11-23, so each draft has a known-good twin. The model never
sees the twin. Its shape example comes from science-grade-2.

## How to run it (when Cory says go)

1. Close the chat and image models. Start `S:\AI\Start-Coder.bat` (gpt-oss-20b on port 5003, 32k context).
2. `python -X utf8 scripts/local_draft.py prompts` shows each prompt's size (about 17k tokens, plus 7k out).
3. `python -X utf8 scripts/local_draft.py draft` writes build/local-pilot/drafts/ and a timing log.
4. `python -X utf8 scripts/local_draft.py check` and `compare`.
5. Fix pass: a fresh Claude agent brings each draft to the gates and the bar, and logs its tokens and minutes. A
   second fresh agent writes the same 8 days from the skeleton alone, as the baseline cost.
6. Side-by-side read: the fixed drafts against the signed-off twins, blind to which is which, on the LESSON-DAY bar
   (teaching moves, examples, student-word goal, At home, cuts and extension, sensitivity).

Everything lands in build/local-pilot/ (git-ignored). Nothing touches courses/, data/ or docs/.

## What decides it

- **Go:** fixed drafts read at par with the twins, and the fix pass costs at most half the fresh-write baseline.
- **Narrow:** par on some parts only (say, At home and Shorter or longer): use the local model for those parts.
- **Stop:** fixing is near the cost of writing, or errors slip past the fix pass.

## Known limits

- 16 GB of VRAM caps the prompt: the rules, skeleton, section block and one example fit; the unit plan, frame and
  progression do not (the skeleton already carries what they decide).
- A 20B model makes more factual slips than Codex or Claude; science K to 3 is a fair first test, upper grades and
  sensitive history are harder.
- The day skeleton is itself still a living draft, so the pilot tests it too: record what it lacked in
  DAY-SKELETON.md's lessons.

## The section plan pilot (Cory 2026-11-26: "the pilot for sections only")

Cory's shape for core section plans: a high-quality, low-cost prep, a zero-cost local draft, a cheap fix, then an
Opus refine. Run first on math-grade-1 unit 1 (sections u01-1 to u01-4); grade 1 has no written sections yet, so
there is no signed-off twin and the blind read is against a fresh write instead.

1. **Skeleton:** scripts/section_skeleton.py (script, free), as for every section job.
2. **Prep (Claude Opus):** one note per section, at most 1,100 words, carrying every judgment the local model cannot
   make: exits solved with keys and lettered wrong answers, Shape lines, part minutes, cases, continuity from the
   ledger, fallbacks. build/local-pilot/sec/prep/<course>/.
3. **Local draft:** `python -X utf8 scripts/local_draft.py sec-draft math-grade-1 1`. The model sees only the rules
   (UNIT-PLAN.md rules, fields and Length; the brief's Write and probe rules), DEFAULTS.md, the prep note and the
   skeleton. build/local-pilot/sec/drafts/ (raw output kept beside each draft).
4. **Fix (Sonnet):** the drafts to the gates (`sec-check ... fixed`) and the bar. build/local-pilot/sec/fixed/.
5. **Refine (Opus):** as for any section. build/local-pilot/sec/refined/.
6. **Baseline:** a fresh Sonnet writer does the ordinary section job from the skeleton (no ledger rows).
   build/local-pilot/sec/fresh/.
7. **Blind read:** refined against fresh, labels hidden, on the section plan bar.

Go if the fix costs at most half the fresh write and the blind read is at least even; the whole pipeline's tokens
(prep plus fix plus refine) are reported beside the fresh write plus its usual refine. Nothing lands in docs/ until
Cory picks; the winner then goes through the normal gates. Early note: a smoke test answer put a ten frame as "a row
of ten" (it is two rows of five), the kind of slip the prep and fix passes must catch.

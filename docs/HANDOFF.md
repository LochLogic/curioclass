# Handoff: the current state

Where the work stands and what to do next, as of 2026-11-15. The reasons behind decisions are in the decision log,
[agents/decisions/DESK-ANSWERS.md](agents/decisions/DESK-ANSWERS.md). If another page disagrees with this one, find
which is stale, fix it and say so.

## State now

The plan is [PRODUCTION-PATH.md](PRODUCTION-PATH.md): the four core subjects are planned top down, one layer at a
time, before more days are written.

- **Progressions** (step 1): done for all four core subjects, K to 12, in data/progressions/.
- **Course frames** (step 2): done for all 52 core courses (docs/courses/<course>/frame.md, totals in
  data/plans/frames.csv). Baseline 1 is closed.
- **Scopes and sequences** (steps 3 and 5): all 52 written, read by the expert and by Codex, fixed and through a
  structure pass (docs/courses/<course>/scope-and-sequence.md, data/plans/<course>/days.csv). The scope gate prints
  no rule 2 notes (social studies fixed 2026-11-15, later.csv L28).
- **Unit plans**: social studies has 138, written, read twice, fixed and through a structure pass. Science, ELA and
  math have skeletons for all 259 units (scripts/unit_skeleton.py, spot-checked); their judgement fields are not
  filled yet.
- **Section plans and days**: none under the current path. A day skeleton draft exists early on purpose
  (scripts/day_skeleton.py, docs/pipeline/DAY-SKELETON.md, later.csv L31). Grade 4 math's older plans and 48 days,
  made under the retired pilot plan, are held for math's units in step 5 (PRODUCTION-PATH section 4; rework list in L13).
- **The site**: not launched. scripts/course_pages.py builds hidden course and unit pages for all 52 core courses
  (`SHOWN = False`); the design is [SITE-DESIGN.md](SITE-DESIGN.md). Day pages will be one source file per day,
  published as one page per section with each day as an anchor (settled 2026-11-15, see DESK-ANSWERS).
- **Tools**: paused until step 9, the Codex queue's builds included. Live tools stay live and claim no course
  coverage (BASELINE rule 26).

By course: [COURSES-STATUS.md](COURSES-STATUS.md) (generated; never edit by hand). By step: the Desk Dashboard's
plan flow, data/plans/flow-status.csv. Parked work: data/plans/later.csv.

## Next steps, in order

1. The social studies probe (PRODUCTION-PATH step 4, docs/pipeline/PROBE-GUARD.md), then
   baseline 2, where any unit template change is made once, before three more subjects copy it. The day pipeline
   (plan-data.md, lesson.py, LESSON-DAY.md, courses/<course>/) is math-shaped: adapting it for social studies is
   part of the probe. The blind rule names courses/math-4/ only (narrowed 2026-11-15, see DESK-ANSWERS), so new
   day folders can be written under courses/.
2. Science, ELA and math units together (step 5): Codex fills the skeletons the social studies way
   (scripts/codex_units.py with plan-codex-science.md, plan-codex-ela.md and plan-codex-math.md), then expert and
   Codex reads, a fix pass, a structure pass, each subject's own probe and a review from the progression down. ELA
   text editions and rights go into data/plans/ela-texts.csv after each batch (L32). Math is written blind, then
   reconciled with grade 4's old work (L13); high school math is read against docs/RUBRIC-MATH-HS.md (L49, L50).
3. Then the path's later steps: the final review (step 6), a short approach page per subject before days (L27),
   the guard and days (step 7), and tools (step 9).

## How to start

Read [AGENTS.md](../AGENTS.md), then PRODUCTION-PATH.md, [GLOSSARY.md](GLOSSARY.md), the decision log and
[BASELINE.md](agents/decisions/BASELINE.md). The pipeline guide is [pipeline/README.md](pipeline/README.md).

The folders (the truth is the GitHub repository, branch `main`):

| Folder | Branch | Who works there |
|---|---|---|
| `S:\CurioClass` | `main` | The main session |
| `S:\CurioClass-spec2` | `spec/sara` | Sara's sessions only; they push to `spec/sara` and to `main` |
| `S:\CurioClass-codex` | `codex/queue` | Codex |
| `S:\CurioClass-sources` | none | Base texts and references (AGENTS.md) |
| `S:\CurioClass-archive` | none | Set-aside files; anything needing deletion moves to `<what>-<date>\` here |

The main session pulls first (`git pull -q --rebase origin main`), pushes with `git push -q origin HEAD:main`,
commits only its own files and never edits in another session's folder. A background agent editing files blocks
`pull --rebase`: commit after it finishes. "Bypassed rule violations" on main is normal.

## Standing facts

- 107 courses (105 active, 2 world languages shelved); 52 core courses in the four core subjects plus 6 core
  electives. World languages stay in the course counts as a reminder. Every course is finished to the adoption bar;
  never call that unrealistic.
- The blind rule: writers and first readers never open a subject's earlier planning (each brief lists the paths),
  so old work cannot steer the new layers; a reconcile step then settles each difference by a named source
  (PRODUCTION-PATH step 1).
- There are no outside human readers: the expert, Codex, sensitivity, safety and answer-key agents take those
  places (settled 2026-11-14, see DESK-ANSWERS). Nothing here has been tried with a student or read by a working
  teacher, and the source search, the bar drafts and the standards check rest on agent reports.
- Codex runs by script, with no clicks (scripts/codex_read.py, codex_scopes.py, codex_units.py). Codex Pro ends
  2026-11-30.
- Questions for Cory go on the Review Desk (address in docs/agents/RUNBOOK.md) as question cards with a pick, and
  are said in chat too. A card's status goes from `question` to `answered`; Cory answers in a comment. Sara's
  session cannot open the Desk, so the main session places her cards. Cory wants pushback and welcomes questions
  about earlier decisions.
- After changes, refresh the Desk: `python -X utf8 scripts/course_status.py <out.json>` (doc `stats/courses`) and
  `python -X utf8 scripts/plan_flow.py <out.json>` (doc `stats/plan`; node states in data/plans/flow-status.csv).
  When a review step closes, add its result to data/plans/flow-results.csv (node, then two or three sentences:
  findings per reader, main fixes, what went to Cory).
- Parked work gets a row in data/plans/later.csv; mark a row done rather than deleting it, and act on any row whose
  trigger has passed.
- Stale notes are expected often. A note that waits on other work starts `Pending(<file>, <file>#<text> or <plan
  node>):`; `python -X utf8 scripts/stale.py check [files]` fails a marker whose work has landed. When a layer
  lands, run it and rewrite what it flags.

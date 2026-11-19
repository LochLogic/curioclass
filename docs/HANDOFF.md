# Handoff: the current state

Where the work stands and what to do next, as of 2026-11-18. The reasons behind decisions are in the decision log,
[agents/decisions/DESK-ANSWERS.md](agents/decisions/DESK-ANSWERS.md). If another page disagrees with this one, find
which is stale, fix it and say so.

## State now

- **Under way 2026-11-18: the science ladder test (later.csv L81).** Kindergarten to grade 3, initial dirty pass: ledger (scripts/ledger.py, data/plans/ledgers/science.csv), section plans K to 3, then plan data and days K to 3, then a read-only sample. Runs straight through (Cory dropped the pauses 2026-11-18), in two lanes: section plans a grade ahead, plan data and days behind. Section plans for kindergarten to grade 3 are done (2026-11-19); kindergarten (64 days) and grade 1 (68 days) are all written; grade 2 days are under way (through day 47), and grade 3 plan data has started. Day-stage jobs come from _scratch/ladder/gen.py. Tokens: docs/reviews/ladder-science-tokens-2026-11-18.csv.

- **Done 2026-11-18: the confirm probe (L78), first for ELA and for middle school** (report
  docs/reviews/probe-confirm-2026-11-18.md). After L75 (hand-backs in the day skeleton, the plan.py slot gate, sources
  checked once), L76 with L74 (rules 1 to 10, per-band DEFAULTS.md from scripts/defaults.py, unit edits): ELA grade 11
  days 1 to 5 and science grade 7 days 1 to 6, lean process, Sonnet agents. Result: Off on plan share (46%, 50%;
  line 35%), Watch on units (3 of 13 other units firm), On for template. Skeletons ran with no STOP and no unslotted
  hand-back; the rule kinds mostly did not return; what is left is item keys in unit data that two reads still
  catch, plus content notes and reading pace in ELA. Rules round done (section-write rules 11 to 14 and science lines,
  plan-data Keys paragraph, DEFAULTS regenerated, measure 2 unit fixes). **Next is Cory's pick, Desk card
  q-probe-confirm-1 (later.csv L79):** a second confirm probe (recommended) or scale a first wave. Lead: L80 (two page
  gates). 2.22M tokens, 195k and 174k a finished day.
- **Done 2026-11-18: the fourth probe, first for science and math** (Cory 2026-11-18; report
  docs/reviews/probe-science-math-2026-11-18.md). Science grade 5 and Algebra II: section plans 1.1 and 1.2, plan
  data and pieces for section 1.1, days 1 to 4 and 1 to 5, read (answer key, one expert read per course) and fixed by
  Claude Sonnet agents with the lean process (L69 test). Result: Off on plan share (50%, 42%) and units changed (6 of
  11 other units), On for template; the social studies, science and math probe nodes are closed. **Skeletons:** the
  machinery runs unchanged across three subjects and bands; what it runs on is not ready (the same running faults in
  every probe). Shortest path to ready: L75 (gate and skeleton session), L76 with L74 (rules, per-band DEFAULTS,
  small unit edits), then L78 (confirm probe with ELA and middle school). Cory's items: L71 (units.csv rows, now
  eleven), L77 (soil trial, source A1). Token ledger in docs/reviews/probe-science-math-tokens-2026-11-18.csv.
- **Done 2026-11-18: the third probe, kindergarten social studies** (Cory 2026-11-17; report
  docs/reviews/probe-social-studies-3-2026-11-18.md). Section plans for units 1 to 3 (u01-1 to u03-4, now gated by
  unitplan.py), docs/courses/social-studies-kindergarten/DEFAULTS.md, plan data and shared pieces (our own
  read-alouds as `piece: story`), and days 1 to 19, all read (section lens, answer key, expert per unit, sensitivity)
  and fixed by Claude Sonnet agents (Codex out of tokens). Result: Off on plan share (51%) and units changed (68% of
  19 early-grade units), On for template (new `spoken` path, per-minute prose cap on ranged frames, short-day At
  home). Next: later.csv L74 (K to 2 rules, a correction pass, probe again), L72 (kindergarten page rendering), L73
  (small gates), L71 (Cory: seven units.csv rows; until then plan.py and lesson.py show seven known failures).
  Example section plan u01-1 signed off by Cory 2026-11-18. Token ledger for L69 in the report.
- **Done 2026-11-17: the Claude second lens pass** (Codex had hit its limit). Claude Sonnet agents ran the unit loop
  with docs/pipeline/briefs/unit-lens-claude.md (stage `read`, then stage `fix`) over the 186 jobs in
  docs/pipeline/claude-jobs.txt; reports are docs/reviews/claude-lens-*-2026-11-17.md and claude-fix-*-2026-11-17.md.
  Every course in the list is fixed, gated and pushed; science 8 was held over the cap until the caps were raised to
  1,600 and 2,300 (2026-11-17, DESK-ANSWERS). `stash@{0}` (redundant, from a 5:35pm autostash race) and
  `stash@{1}` (2026-10-27, another session's) are left in place; never `git stash` here.
  **Pausing point for baseline 2 (2026-11-17, Cory).** Since the pass: the caps are 1,600 and 2,300; Desk answers
  q-lens-pass-1 and q-electives-frames-1 are applied (docs/reviews/desk-answers-*-2026-11-17.md, elective base texts
  now in the source store); later.csv L64 (Fluency mislabel: one rule in GLOSSARY "teaching day", a sequence.py gate,
  44 days relabelled, docs/reviews/fluency-sweep-2026-11-17.md), L65 and L66 are done. Everything is committed and
  every gate passes. Carried into baseline 2: docs/reviews/lead-list-lens-pass-2026-11-17.md (934 LEAD items and 489
  findings rejected for the old cap, by unit) and the Fluency sweep's "left for the lead" list.

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
- **Social studies probe** (2026-11-15, docs/reviews/probe-social-studies-2026-11-15.md): Off. US History I days 78
  to 82 written and read the full way; plan share 60%, units changed 88% (mostly error letters holding two
  misconceptions, written by Codex in 119 units). Corrected 2026-11-15: all 138 units by Codex
  (docs/pipeline/briefs/unit-correct.md, reports docs/reviews/codex-write-correct-*), the rules in UNIT-PLAN.md, the
  plan-codex briefs and unitplan.py, sources "verified or none", and days 78 to 82 fixed with a Native nations read
  (docs/reviews/sensitivity-native-u05-2-2026-11-15.md). **Second probe** (World History I 3.4, days 42 to 46,
  docs/reviews/probe-social-studies-2-2026-11-15.md): Off again (plan share 60%, units 42%, one required table
  added to UNIT-PLAN field 7), but only 6 of 147 findings needed a unit plan; most sit in keys, samples and source
  sheets written at plan-data. Next (later.csv L56): gates for the repeated faults, a second correction pass run to
  the gates, an answer-key read after plan-data, a third probe. Whether science, ELA and math units wait is Desk card
  q-probe-ss-2.
- **Section plans and days**: only the two probe sections (US History I 5.2, days 78 to 82; World History I 3.4, days 42 to 46). A day skeleton draft exists early on purpose
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

- 120 courses (118 active, 2 world languages shelved); 52 core courses in the four core subjects plus 6 core
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
  `python -X utf8 scripts/plan_flow.py <out.json>` (docs `stats/plan-c0`, `plan-c1`, ... from <out.json>.parts/, sent together in one ArtifactData batch; the Desk joins them, so the plan has no size cap; node states in data/plans/flow-status.csv).
  Then refresh the signed-out copy: ArtifactData `list` on `items` (limit 1000) and `stats` (limit 100) with out_dir
  `<dir>`, run `python -X utf8 scripts/desk_snap.py <dir> <folder holding desk.html>`, and republish the Desk page
  with `files: {"snap.json": "<that folder>/snap.json"}`. Viewers who are not signed in see only this copy (no
  comments, no live updates), so skipping it leaves the shared link showing old data.
  When a review step closes, add its result to data/plans/flow-results.csv (node, then two or three sentences:
  findings per reader, main fixes, what went to Cory).
- Parked work gets a row in data/plans/later.csv; mark a row done rather than deleting it, and act on any row whose
  trigger has passed.
- Stale notes are expected often. A note that waits on other work starts `Pending(<file>, <file>#<text> or <plan
  node>):`; `python -X utf8 scripts/stale.py check [files]` fails a marker whose work has landed. When a layer
  lands, run it and rewrite what it flags.

# Handoff: the current state

Where the work stands and what to do next, as of 2026-11-21. The reasons behind decisions are in the decision log,
[agents/decisions/DESK-ANSWERS.md](agents/decisions/DESK-ANSWERS.md). If another page disagrees with this one, find
which is stale, fix it and say so.

## State now

- **Done 2026-11-21: L87, the process aligned to COURSE-RUN.** Versioned kit docs/pipeline/kit/ (KIT-VERSION 1, retool log), `scripts/coursegen.py` (queues in COURSE-RUN order with a unit 1 probe and ledger-gate lines), `scripts/ledger.py` gate, seed, recheck and settle (and `add` promotes planned rows), `made_at` in defects.csv, ten new tagged checks across unitplan.py, plan.py and lesson.py, and `scripts/tokens.py`. Docs point at COURSE-RUN. Record docs/reviews/l87-alignment-2026-11-21.md; new-check hits in finished courses and the math Goal maps are later.csv L102. Next: the two-lane run (below).
- **Done 2026-11-22: the social studies and ELA sample fixes (later.csv L99, L100; Cory 2026-11-21, Desk q-ladder-ss-ela-1).** One fresh fix agent per course applied or rejected every sampled FIRM fault, replaced weak sources or cut the facts, moved keys out of 63 child pieces, applied the ELA grade 1 tale sensitivity read and restored the Maathai Nobel line from the Nobel Prize site. Gates are back to each course's before counts. Record docs/reviews/ladder-ss-ela-fixes-2026-11-22.md. Next: L87 alignment.
- **Done 2026-11-21: the social studies and ELA ladder run (later.csv L98).** Kindergarten to grade 3, initial dirty pass, straight through: ledgers (social-studies.csv, ela.csv), section plans, plan data and 1,056 days (social studies K 64, grades 1 and 2 96, grade 3 160; ELA 160 a grade), then run-end fixes from an outside reader, a capstone cross-grade continuity pass (social studies 7 of 257 claims drifted, ELA 29 of 302, all fixed) and an 80-day read-only sample. Report docs/reviews/ladder-ss-ela-report-2026-11-19.md. Pass marks: FIRM 1.19 a day (miss; science 1.4), wrong keys down by a third (met), review not said still common (miss), 79k tokens a day (miss; target 60k). Open: L99 must-fix before live (ELA grade 1 tale sensitivity, 74 key-line pieces, the Maathai line), L100 Desk card on fixing the 95 sample FIRM findings now or at L87, L101 watch items and template points. Next: L87 alignment, now with ledger-gated scheduling (DESK-ANSWERS 2026-11-21).
- **2026-11-20: after-core stage 1 reads done** (side work). Library, ELD, career education and world languages (still shelved, pre-work only) were each read cold and fixed (docs/reviews/prework-*-read-2026-11-20.md); health and PE cite the national dose figures; per-subject calibration added to docs/pipeline/CALIBRATION.md. Cory answered q-prework-open-1 and -2 on 2026-11-21, applied (DESK-ANSWERS.md); catalogue edits held for a step boundary of the main run (later.csv L90). Every after-core subject still owes the second-model read (later.csv L88, from 2026-11-23) and its calibration run; progressions for library, ELD and career wait on those calls and gate support in scripts/progression.py (its codes() splits ids at the first space).
- **2026-11-20: after-core pre-work answers applied** (side work, Desk q-prework-arts-1, q-prework-health-pe-1 and -2, q-prework-cs-1; DESK-ANSWERS.md). Health, PE and computer science pages and progressions carry Cory's calls; arts own-words file is next (later.csv L82 to L85). Open on Desk q-prework-open-1: the health and PE approach yes, our own coding editor, and the SEL reader's calls. SEL pre-work continues (read: docs/reviews/prework-sel-read-2026-11-19.md).

- **Done 2026-11-19: the science ladder test (later.csv L81).** Kindergarten to grade 3, initial dirty pass: ledger (scripts/ledger.py, data/plans/ledgers/science.csv), section plans, plan data and 328 days (K 64, grade 1 68, grade 2 76, grade 3 120), all committed, then a read-only sample of 40 days. Result: 1.4 FIRM faults a day, nearly none gate-visible; fill cost about 72k tokens a day. Report: docs/reviews/ladder-science-report-2026-11-19.md. Cory picked: fix all that can be fixed, then pause. Fixed 2026-11-19 (gates, briefs, every sample FIRM finding, all 328 days at 0 lesson.py failures): docs/reviews/ladder-science-fixes-2026-11-19.md. PAUSED for Cory; Refine 1 and grades past 3 wait. Day-stage jobs come from _scratch/ladder/gen.py. Tokens: docs/reviews/ladder-science-tokens-2026-11-18.csv.

- **Done 2026-11-18: the confirm probe (L78), first for ELA and for middle school** (report
  docs/reviews/probe-confirm-2026-11-18.md). After L75 (hand-backs in the day skeleton, the plan.py slot gate, sources
  checked once), L76 with L74 (rules 1 to 10, per-band DEFAULTS.md from scripts/defaults.py, unit edits): ELA grade 11
  days 1 to 5 and science grade 7 days 1 to 6, lean process, Sonnet agents. Result: Off on plan share (46%, 50%;
  line 35%), Watch on units (3 of 13 other units firm), On for template. Skeletons ran with no STOP and no unslotted
  hand-back; the rule kinds mostly did not return; what is left is item keys in unit data that two reads still
  catch, plus content notes and reading pace in ELA. Rules round done (section-write rules 11 to 14 and science lines,
  plan-data Keys paragraph, DEFAULTS regenerated, measure 2 unit fixes). Desk card q-probe-confirm-1
  (later.csv L79) was answered 2026-11-18: superseded by the science grade ladder (L81). Lead: L80 (two page
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
plan flow, drawn as the seven stages of [COURSE-RUN.md](COURSE-RUN.md) for all 105 active courses (core bright,
core electives and other subjects faint), node states in data/plans/flow-status.csv. Parked work: data/plans/later.csv.

## Next steps, in order

Every course now runs by [COURSE-RUN.md](COURSE-RUN.md) (since 2026-11-20). PRODUCTION-PATH.md keeps the record of
why the core was planned top down; its steps 7 and 8 are superseded by COURSE-RUN stages 5 and 6.

1. **The next course run, two lanes side by side** (DESK-ANSWERS 2026-11-20): math K to 3, and social studies grades 4
   and 5 with World Geography I. Each subject's first grade starts with a unit 1 probe. The queue comes from
   `scripts/coursegen.py` and the kit in docs/pipeline/kit/; day jobs are ledger-gated (`scripts/ledger.py gate`);
   cost tables come from `scripts/tokens.py`. Prep done 2026-11-22 (later.csv L102): math K to 3 Goal maps and
   section skeletons, the math subject note, grade notes 4 to 6; both lanes generate their queues cleanly.
2. **Science K to 3 stays paused for Cory** (later.csv L81), as do Refine 1 and the grades past 3.
3. **Before any course goes live:** the watch items in later.csv L101, and each course's stage 7 finish (COURSE-RUN).
4. **After the core:** the electives and later subjects run from COURSE-RUN stage 1; their second-model reads and
   calibration are later.csv L88.

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

# Handoff: the current state

Where the work stands and what to do next, as of 2026-11-26. The reasons behind decisions are in the decision log,
[agents/decisions/DESK-ANSWERS.md](agents/decisions/DESK-ANSWERS.md). If another page disagrees with this one, find
which is stale, fix it and say so.

Where every kind of file lives and who writes it: [../data/homes.csv](../data/homes.csv) (`scripts/homes.py kind <path>`). How to make a change that reaches past one day: [CHANGES.md](CHANGES.md).

## State now

- **Done 2026-11-26: every after-core course frame (65 frames, 117 of 117 courses framed; 3 world-language courses stay shelved).** Each frame was written to the new architecture, read by Codex and by a subject expert, then fixed in one pass per subject (docs/reviews/frame-*-fixes-2026-11-2*.md; arts in frame-music-theater-media-arts-fixes-2026-11-26.md). The lead calendar pass followed: CALENDAR.md's K to 5 rule now counts only the classroom teacher's courses (core, health, SEL) and 6 to 8 counts the arts electives as one; pins for PE 6 to 8, computer science grade 6 and health 3 to 5 leave `frame.py calendar` with no clash. Open lead items and Cory's questions are in build/frame-writes/NEXT.txt and on the Desk.
- **Done 2026-11-26: Health of the build and Quality.** gate.py refuses to store a baseline when a gate crashed (the pile-up cause); goal tests 13 to 16 added; ELA K to 3 alignment defects (108 fixed, 3 rejected) and social studies K to 3 and 5 (111 fixed, 11 rejected, 49 left open; reasons in build/quality/ss-dispositions-2026-11-26/).
- **Paused 2026-11-26 by Cory: Codex days, one lane per core subject** (ran from 2026-11-25; math-kindergarten, science-grade-4, social-studies-grade-4, english-language-arts-grade-4; scripts/codex_lane.py, logs build/lanes/<lane>/run.log). The lead commits outside the lanes with `codex_lane.py lead-commit`. All four hit the Codex usage limit at 03:23 (resets 2026-11-30 7:08 AM, the day Pro becomes Plus); Cory closed the Codex work out for now, the lead ended the four lane processes and left build/lanes/STOP in place (the usage-pause loop never reads STOP, later.csv L144). Where each stopped (last commit, then the job that reruns first): math 019 DAY ok (73e5c4ae6), next 020 DATA u2; science 015 DAY ok (ebb64eaf8), next 016 DAY 1.4; social studies 016 DATA u1 ok (2f3462bec), next 017 KEY u1; ELA 019 done, next 020 PLAN-READ units 1-4. Uncommitted half-jobs sit in the working tree: math-kindergarten u02 pieces and plan data (job 020, about 125 files) and science-grade-4 u01-4 (job 016, 9 files); the rerun brings them to the kit, so nobody commits or moves them by hand. To restart: delete build/lanes/STOP, then one terminal per lane: `python -X utf8 scripts/codex_lane.py run <math|science|social-studies|ela>`.
- **In progress from 2026-11-24: the consolidation ([CONSOLIDATION-PLAN.md](CONSOLIDATION-PLAN.md)).** Everything comes back into this one folder, then the architecture for scale; curriculum first (the tool catalog is frozen; tools are reshaped after the curriculum is done). Steps run one at a time: 0 freeze, 1 rescue, 2 Codex merge, 3 cleanup, 4 architecture, 5 tool records, 6 close.
  - Done: steps 0 to 3; step 4 sub-steps 4.A to 4.J (report [reviews/consolidation/step4-report.md](reviews/consolidation/step4-report.md)). Curriculum writing may restart (since 4.G).
  - The close Fable review is [reviews/consolidation/step4-close-review.md](reviews/consolidation/step4-close-review.md). Its findings 1, 2 and 7 are fixed and the nine-word US spelling sweep has run (2026-11-25, scripts/us_spelling.py).
  - 4.L done 2026-11-25 (CONSOLIDATION-PLAN 4.L Built list; Fable read docs/reviews/consolidation/step4-L-review.md). At each grade close the lead runs `gate.py --course <course> --record` (data/plans/debt.csv). Row 7, the count-only Word Wall read, waits for L130. Next: step 5's items 2 to 4 and 6, on Cory's go. Step 5's record items ran early on Cory's word (2026-11-25): item 1, the tool stage table data/tool-stages.csv (scripts/tool_stages.py), and item 5, one record per tool, tools/<id>/tool.md, with all 194 tools flattened (scripts/tool_record.py). Its tool-changing items 2 to 4 and 6 wait for tool work.
  - L133 done 2026-11-25: a day file needs a written ledger row (kind `none` for review, practice and test days) and a version line, or the index status report fails it; 34 known days are baselined, later.csv L136 (kit 12).
  - The Desk Dashboard was rebuilt 2026-11-25 to show the whole site (built so far, every course with drill-down to days, health); desk/README.md says what each part reads.
  - The pedagogy-architecture review's changes 1 to 9 are built (2026-11-25; CONSOLIDATION-PLAN 4.L list; kit 13), then code-reviewed and every living doc checked for continuity the same day (kit 14). New lead steps: at grade close `scripts/pass_marks.py add`, `scripts/day_version.py <course> grade-read <date>` and a read of `scripts/spacing.py <course>`; at sign-off `day_version.py <course> signed-off <date>`; `scripts/trace.py` walks a code, skill or day up and down. English learner supports are made in the lesson, not at stage 7. Later L137 to L142.
  - The Word Wall gets no import: a count-only overlap read when L130 opens (Cory, 2026-11-25).
  - Block two and step 5 touch no course data. Scale counts for later marketing: [funding/SCALE.md](funding/SCALE.md).
- **Ended 2026-11-24: the Codex draft run (later.csv L105).** Stopped softly by Cory; main merged into draft/codex and a baseline sheet written (docs/reviews/codex-draft-baseline-2026-11-24.md). Merged into main 2026-11-24 (consolidation step 2, docs/reviews/consolidation/step2-report.md): the six lane courses' days are on main as draft 1, unread, with their known gate failures; course pages stay off the deploy. The review is PAUSED for Cory (L105 lists its classes).
- **Done 2026-11-23: science K to 3 finished to COURSE-RUN stage 7 and signed off by Cory (later.csv L81).** His calls were applied 2026-11-23 (docs/reviews/signoff-fix-science-<course>-2026-11-23.md; DESK-ANSWERS 2026-11-23). Run record from 2026-11-22: The L102 exit faults fixed, a 10-day re-sample per grade (K 0.9, grade 1 1.2, grade 2 0.8, grade 3 0.8 FIRM a day), a full read and cleanup for grade 1, then the stage 7 reads, one fix pass and a safety page per course, and the K to 3 continuity pass. Gates: lesson.py 0 FAIL; plan.py only the known units.csv lines. Records docs/reviews/finish-fix-science-<course>-2026-11-22.md, continuity-science-2026-11-22.md. Cory's calls are on Desk cards q-sci-finish-k, -g1, -g2, -g3. Art, voice and tools deferred.
- **Done 2026-11-22: science K to 3 outside-reader fixes.** The Gemini findings were verified and fixed in all four courses (commits 06044df12, a217321fe, cebb837f9; ledgers docs/reviews/gemini-fixes-science-<course>-2026-11-22.md); gates at each course's baseline. Science K to 3 stays PAUSED for Cory (later.csv L81).
- **Done 2026-11-22: all 65 progression nodes.** SEL, ELD, library, career education and Spanish joined the earlier subjects (data/progressions/, flow-status.csv). World languages is Spanish only; ASL waits on the required review (later.csv L93).
- **Done 2026-11-21 to 22: the Recess games.** Infinite Hike, Farlight and Ripple (the renamed music maker) are live, Go, Chess, Checkers and Untangle went live early (Desk card recess-live-early), Cargo Hold is spec only. Which are live is in [GAMES.md](GAMES.md), "On the shelf now" (the `live` flag in data/recess.json is not used).
- **Done 2026-11-21: L87, the process aligned to COURSE-RUN.** Versioned kit docs/pipeline/kit/ (KIT-VERSION 1; 2 since the 2026-11-22 wording retool, RETOOL.md), `scripts/coursegen.py` (queues in COURSE-RUN order with a unit 1 probe and ledger-gate lines), `scripts/ledger.py` gate, seed, recheck and settle (and `add` promotes planned rows), `made_at` in defects.csv, ten new tagged checks across unitplan.py, plan.py and lesson.py, and `scripts/tokens.py`. Docs point at COURSE-RUN. Record docs/reviews/l87-alignment-2026-11-21.md; new-check hits in finished courses and the math Goal maps are later.csv L102. Next: the two-lane run (below).
- **Done 2026-11-22: the social studies and ELA sample fixes (later.csv L99, L100; Cory 2026-11-21, Desk q-ladder-ss-ela-1).** One fresh fix agent per course applied or rejected every sampled FIRM fault, replaced weak sources or cut the facts, moved keys out of 63 child pieces, applied the ELA grade 1 tale sensitivity read and restored the Maathai Nobel line from the Nobel Prize site. Gates are back to each course's before counts. Record docs/reviews/ladder-ss-ela-fixes-2026-11-22.md. Next: the two-lane run (below).
- **Done 2026-11-21: the social studies and ELA ladder run (later.csv L98).** Kindergarten to grade 3, initial dirty pass, straight through: ledgers (social-studies.csv, ela.csv), section plans, plan data and 1,056 days (social studies K 64, grades 1 and 2 96, grade 3 160; ELA 160 a grade), then run-end fixes from an outside reader, a capstone cross-grade continuity pass (social studies 7 of 257 claims drifted, ELA 29 of 302, all fixed) and an 80-day read-only sample. Report docs/reviews/ladder-ss-ela-report-2026-11-19.md. Pass marks: FIRM 1.19 a day (miss; science 1.4), wrong keys down by a third (met), review not said still common (miss), 79k tokens a day (miss; target 60k). L99 and L100 were done 2026-11-22 (above); L101 (watch items and template points, to settle before any course goes live) is open.
- **After-core subjects (side work, 2026-11-20 to 22):** stage 1 and the progression are done for every after-core subject (health, PE, arts, computer science, SEL, ELD, library, career education, Spanish): each was read cold and by a second model, fixed, and Cory's calls applied (docs/reviews/prework-*, progression-*; DESK-ANSWERS.md). World languages is Spanish only and still shelved; ASL waits on the required review (later.csv L93). Still owed: the catalog retag (later.csv L90 part 2, with L95), a person to read the health kindergarten body names (L89), the library band-file comparison (L103) and the can-do note (L92). Their frames, scopes and later stages wait for their course runs (COURSE-RUN).

- **Done 2026-11-19: the science ladder test (later.csv L81).** Kindergarten to grade 3, initial dirty pass: ledger (scripts/ledger.py, data/plans/ledgers/science.csv), section plans, plan data and 328 days (K 64, grade 1 68, grade 2 76, grade 3 120), all committed, then a read-only sample of 40 days. Result: 1.4 FIRM faults a day, nearly none gate-visible; fill cost about 72k tokens a day. Report: docs/reviews/ladder-science-report-2026-11-19.md. Cory picked: fix all that can be fixed, then pause. Fixed 2026-11-19 (gates, briefs, every sample FIRM finding, all 328 days at 0 lesson.py failures): docs/reviews/ladder-science-fixes-2026-11-19.md. PAUSED for Cory; Refine 1 and grades past 3 wait. Day-stage jobs now come from scripts/coursegen.py (gen.py, the earlier generator, archived 2026-11-24). Tokens: docs/reviews/ladder-science-tokens-2026-11-18.csv.

- **Probes, 2026-11-15 to 18 (history; each is closed).** Social studies US History I and World History I (docs/reviews/probe-social-studies-2026-11-15.md, probe-social-studies-2-2026-11-15.md); kindergarten (probe-social-studies-3-2026-11-18.md); science grade 5 and Algebra II (probe-science-math-2026-11-18.md); ELA grade 11 and science grade 7 (probe-confirm-2026-11-18.md). Their rule and gate work fed the kit (L87). Cory's seven units.csv rows are later.csv L71.
- **Done 2026-11-17: the Claude second lens pass** over the 186 jobs in docs/pipeline/claude-jobs.txt (reports docs/reviews/claude-lens-*-2026-11-17.md and claude-fix-*; carried list docs/reviews/lead-list-lens-pass-2026-11-17.md). Never `git stash` here; two old stashes are left in place.

Courses run by [COURSE-RUN.md](COURSE-RUN.md); [PRODUCTION-PATH.md](PRODUCTION-PATH.md) is the record of why the four core subjects were planned top down, one layer at a
time, before more days are written.

- **Progressions** (step 1): done for all four core subjects, K to 12, in data/progressions/.
- **Course frames** (step 2): done for all 52 core courses (docs/courses/<course>/frame.md, totals in
  data/plans/frames.csv). Baseline 1 is closed. The after-core frames were done 2026-11-26 (117 courses framed).
- **Scopes and sequences** (steps 3 and 5): all 52 written, read by the expert and by Codex, fixed and through a
  structure pass (docs/courses/<course>/scope-and-sequence.md, data/plans/<course>/days.csv). The scope gate prints
  no rule 2 notes (social studies fixed 2026-11-15, later.csv L28).
- **Unit plans**: all 259 science, ELA and math units have skeletons (scripts/unit_skeleton.py); social studies has 138 plans, read twice, fixed and through a structure pass. Judgement fields are filled at each course's run, and the ladder grades (K to 3) are done (math Goal maps: later.csv L102).
- **Section plans and days**: the ladder runs wrote section plans and days for science K to 3 (328 days) and social studies and ELA K to 3 (1,056 days), all fixed and gated (above); the probe sections (US History I 5.2, World History I 3.4, science grade 5, Algebra II, ELA grade 11, science grade 7) have section plans only or a few days. Grade 4 math's older plans and 48 days, made under the retired pilot plan, are held for math's units (PRODUCTION-PATH; rework list in L13). The Codex draft days (math kindergarten, science grades 4 and 5, social studies grades 4 and 5, part of ELA grade 4) are on main and unread (L105, paused).
- **The site**: live but not marketed (marketing starts when all curriculum is written and tools are beyond 75 percent complete, Cory 2026-11-24). scripts/course_pages.py builds hidden course and unit pages for all 52 core courses
  (`SHOWN = False`); the design is [SITE-DESIGN.md](SITE-DESIGN.md). Day pages will be one source file per day,
  published as one page per section with each day as an anchor (settled 2026-11-15, see DESK-ANSWERS).
- **Tools**: the catalog is frozen until consolidation step 5 items 2 to 4 and 6, the Codex queue's builds included. Live tools stay live and claim no course
  coverage (BASELINE rule 26).

By course: [COURSES-STATUS.md](COURSES-STATUS.md) (generated; never edit by hand). By step: the Desk Dashboard's
plan flow, drawn as the seven stages of [COURSE-RUN.md](COURSE-RUN.md) for all 118 active courses (core bright,
core electives and other subjects faint), node states in data/plans/flow-status.csv. Parked work: data/plans/later.csv.

## Next steps, in order

Every course now runs by [COURSE-RUN.md](COURSE-RUN.md) (since 2026-11-20). PRODUCTION-PATH.md keeps the record of
why the core was planned top down; its steps 7 and 8 are superseded by COURSE-RUN stages 5 and 6.

1. **Unit plans back to the stage 4 bar: done 2026-11-22 (later.csv L102).** Every core unit plan now has field 5's
   Goal map (docs/courses/UNIT-PLAN.md): 364 plans in 48 courses, 5,354 rows, filled by one gated agent job per course
   (scripts/goalmap.py brief, insert and audit); `scripts/unitplan.py check` prints no exit-kind or practice-shape
   line. Where days are written (social studies, ELA and science K to 3) each row was read from the written day and
   its exit cards; an exit that does not measure its goal is logged in data/plans/defects.csv (found_by cheap, kind
   alignment, ref "later.csv L102"): 369 open (six more rejected under the K to 2 speech rule), 247 of them day faults in the K to 3 written days, 122 in plan
   exits. They are fixed in each course's refine or day fix, and the row states the goal's target exit to fix toward.
2. **Decide where curriculum writing restarts (Desk q-restart-1).** The architecture work is done (consolidation
   step 4, the pedagogy-architecture review, then kit 14 after the continuity check), so writing may restart. Six courses already hold Codex draft
   days on main, unread: math kindergarten (160), science grades 4 and 5 (120 each), social studies grade 4 (160) and
   grade 5 (51 of 160), and part of ELA grade 4. Their review, later.csv L105, is paused at Cory's call. The queues
   come from `scripts/coursegen.py` and the kit in docs/pipeline/kit/ (all four subjects generate cleanly on kit 13; kit 14 changes only the lead checklist and spelling,
   checked 2026-11-25); day jobs are ledger-gated (`scripts/ledger.py gate`); costs from `scripts/tokens.py`.
3. **Science grades 4 and up can climb** (K to 3 signed off 2026-11-23, later.csv L81), starting from the grade 4
   and 5 Codex drafts once L105 opens. Each new science scope gets the coverage table (L104). Art, voice and tools
   for K to 3 wait for their stages.
4. **Before any course goes live:** the watch items in later.csv L101, and each course's stage 7 finish (COURSE-RUN).
5. **After the core:** the electives and later subjects run from COURSE-RUN stage 1; their second-model reads and
   calibration are later.csv L88.

## How to start

Read [AGENTS.md](../AGENTS.md), then COURSE-RUN.md (PRODUCTION-PATH.md for background), [GLOSSARY.md](GLOSSARY.md), the decision log and
[BASELINE.md](agents/decisions/BASELINE.md). The pipeline guide is [pipeline/README.md](pipeline/README.md).

The folders (the truth is the GitHub repository, branch `main`):

| Folder | Branch | Who works there |
|---|---|---|
| `S:\CurioClass` | `main` | The main session, and every other worker (one checkout since 2026-11-25; old branches are tags `archive/*`) |
| `S:\CurioClass-sources` | none | Base texts and references (AGENTS.md) |
| `S:\CurioClass-archive` | none | Set-aside files; anything needing deletion moves to `<what>-<date>\` here |

The main session pulls first (`git pull -q --rebase origin main`), pushes with `git push -q origin HEAD:main`,
commits only its own files and never edits in another session's folder. A background agent editing files blocks
`pull --rebase`: commit after it finishes. "Bypassed rule violations" on main is normal.

## Doc map: which doc owns what

Each rule lives in one doc. Dated reports go in docs/reviews/; retired docs are in S:\CurioClass-archive (INDEX.csv).

| Doc | Owns |
|---|---|
| AGENTS.md | Rules for every worker: commits, turns, the folders, house style |
| docs/HANDOFF.md | Current state, next steps, standing facts, this map |
| docs/VISION.md | The north star, the pillars, how the site talks, what we will not do |
| docs/FOUNDATION.md | Purpose, who it is for, the promises, the bar, how work is checked |
| docs/ROADMAP.md | The one plan: tracks and their status |
| docs/PRODUCTION-PATH.md | Why the core was planned top down, layer by layer (a record; COURSE-RUN.md is how courses run now) |
| docs/COURSE-RUN.md, docs/pipeline/ | Running a course through the pipeline; the pipeline kit and guide |
| docs/APPROACH.md, APPROACH-MATH/ELA.md | How Curio Class teaches; which standards and why; per-subject approach |
| docs/APPROACH-SOURCES.md | The sources behind the approach and their access notes |
| docs/ADOPTION-BAR.md, ADOPTION-BAR-SUBJECTS.md | The adoption bar and each subject's standing against it |
| docs/RUBRIC-*.md | The rubrics the reads score against |
| docs/GLOSSARY.md | Our words for our things |
| docs/agents/decisions/BASELINE.md, DESK-ANSWERS.md | Cory's standing calls; the append-only decision log |
| docs/COURSES-STATUS.md, docs/BUILD-BOARD.md | Generated status (course_status.py, board.py); never edit by hand |
| docs/SITE.md, docs/SITE-DESIGN.md | How today's site is built; where the site design is going |
| docs/SUPPLY-CLOSET-PLAN.md | The Supply Closet shelves, Break Box included |
| docs/WORKSHEETS-PLAN.md, docs/LIBRARY-PLAN.md, docs/GAMES.md | Worksheets; the Reading Room; Recess |
| docs/ECOSYSTEM.md | How the shelves hang together |
| docs/CURIOSITIES.md, docs/LESSON-PLANS.md | Curiosities (the second shape); tool lesson plans |
| docs/TOOL-CONTRACT.md | What every tool must do, and the Polish checklist |
| docs/KIT.md, docs/families/, docs/ART.md | The shared kit, family engines, the art pipeline |
| docs/BUILD-PLAN.md, docs/TOOL-BINS.md | Tool build waves; the tool bins (generated; the tool catalog is frozen) |
| docs/agents/*.md | Briefs for each agent role (SPEC, BUILD, REFINE, CODEX-*, DAY-WRITER and others) |
| docs/CONSOLIDATION-PLAN.md | The consolidation, steps 0 to 6 (reports in docs/reviews/consolidation/) |
| data/plans/course-list.csv | The 120 courses: id (the frame slug), subject, grade, core, term, status (data/plans/README.md) |
| data/plans/math-4/, docs/courses/math-4/ | The grade 4 math pilot, kept blind, reconciled under later.csv L13; not a course id |

## Standing facts

- 120 courses (118 active, 2 world languages shelved; the list is data/plans/course-list.csv); 58 in the four core subjects (52 flagged core plus 6
  electives), and 8 health and PE courses flagged core, so 60 flagged core in all. World languages stay in the course counts as a reminder. Every course is finished to the adoption bar;
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

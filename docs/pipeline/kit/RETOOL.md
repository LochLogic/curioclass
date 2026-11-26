# Kit retool log

Each retool is dated, names the KIT-VERSION it produced, and logs every change with the finding behind it, the stage
that found it and the stage that made it. The kit changes only here, between grades (README.md, "The retool rule").

## Retool 0: KIT-VERSION 1 (2026-11-22)

Source: the social studies and ELA K to 3 run report (docs/reviews/ladder-ss-ela-report-2026-11-19.md, its findings,
patterns and recommendations), the fix notes (docs/reviews/ladder-ss-ela-fixes-2026-11-22.md), the alignment audit
(docs/reviews/course-run-alignment-2026-11-20.md, steps 1, 5, 6 and the step 8 sweep template) and the lead rules that
lived only in prompts and _scratch/ladder2/STATE.md.

### Report findings and where each went

| Finding (stage that found / made it) | Where it went |
|---|---|
| Review claims drifted when the lower grade changed after it was cited (capstone: 36 drifted claims; found at capstone, made at section and day) | Ledger gating: a day job starts with `ledger.py gate` and stops on non-zero (day, checks, gate-line); the "planned only" rule for review notes (section, day, cleanup, continuity); continuity read and fix use `ledger.py recheck` |
| Cost 79k a day against 60k; the fixed reading cost dominates short days (found at report / made at job shape) | Day jobs of 4 to 6 days from one read of plan and ledger (generator); cost reminder in common.txt (read only what is needed, filter CSVs, never re-read after an edit) |
| Gates caught almost none of the 95 sample FIRM findings; agents' gate counts missed FAIL lines after the course summary (found at sample / made at agent reporting) | common.txt: report all filtered lines, own counts not trusted, lead re-runs (retool-stop step 1, queue LEAD lines) |
| Exit does not measure the goal; rule 4; two asks in one stem; spoken items the child writes (section, data) | Item rules in data.txt, key.txt (splits two-part items), day.txt, plan-read.txt; path honesty in section, data, day, checks |
| Shape sharing: practice, model or card shares an exit's shape (unit plan and section plan set it) | "Shape:" lines required on every exit and check item in section.txt; checked by plan-read; held in data and day; sweep template for the unit-plan cause |
| Parts that cannot run in their minutes, repair slots too small, marking time | Turn-taking time (about 45 s a child per spoken ask, a rotating six with a hand-back, real repair minutes) in section, data, day, checks, plan-read, sample-read |
| Sources: Wikipedia or a search summary as the record; 403 sites; over-cutting of core facts | Sources rule in common.txt (never Wikipedia or a summary; one other solid source; a fact whose page refused a read is kept as "browser check" and listed; cut only a fact no solid page could state) |
| Id-only matching corrupts rows; a CSV truncated by opening for write first | CSV safety rule in common.txt (full id with prefix, read whole file first) |
| Key lines in child pieces (74 piece files) | Key rule in data, day, checks (keys in teacher key pieces); key-line scan in cleanup.txt; "key-on-child-page" kind in sample-read and key |
| "Template point" used as a shield | common.txt: a plan design choice is not a template point |
| Agents ran git status and git --version; stray temp folders | No-git wording in common.txt (the word git is never typed, "re-read the file you edited"); helper folder rule |
| Key readers' cold solve was not blind (shared pieces print keys) | Cold-solve rule at the top of key.txt |
| Stale plan field 3 exit lines after data changes | data.txt may update field 3 and `## Day N` blocks to match items.csv; key.txt lists stale lines; day.txt says items.csv is the truth |
| Held words and cases practiced before their exit (wagon beats) | Held-word rule in day.txt and checks.txt (check practice words against items.csv first; end items never practiced with their own words in the ELA note) |
| Day job reads the previous "Tomorrow" line | day.txt |
| Facts that rest on sites that refuse reads; a hinge with no fallback (local nation page, visitor, photo) | Hinge fallback rule in section, data and the social studies note; sources rule |
| ELA texts: commissioned texts with no rows, on-file rows with no file | text.txt and text2.txt carried over (optional, `--texts`) |
| Mid-course check days written out of order (found at day 44 before day 43) | Generator places course-level check days in day order between unit day jobs |
| Plan stage skipped: no fresh read of a grade's plans, no probe, one sample after all grades, ad hoc retool | plan-read, plan-fix, probe mode, per-grade sample and cleanup, retool-stop, RETOOL.md (alignment audit section 4) |
| Template bug: UNIT replaced inside UNIT-PLAN.md; report date hardcoded | Upper-case brace tokens filled in one pass, `{DATE}` filled at generation (alignment audit section 2) |

### Changes to the kit itself

- Job files and notes copied from _scratch/ladder2/ and cleaned: no "L81, second test" labels, no hardcoded dates, no
  lead-run-note references; blind-list and scratch paths now point at _scratch/l87/.
- Subject and grade notes are data files (notes/subject-<s>.txt, notes/grade-<band>.txt); the math note is a stub.
- Added templates: plan-read, plan-fix, sample-read (from the science sample job), cleanup (from the sample-fix job),
  continuity-read and continuity-fix (from capstone-read and capstone-fix, using `ledger.py recheck`), retool-stop,
  sweep, and the generator `scripts/coursegen.py` replacing gen2.py and daysmode.py.
- 2026-11-22, never-open list: following Cory's decision of 2026-11-20, math files are fully open to future math
  runs. The common rules drop the math-4, math-3-5-progression, `*-spine.md`, NEXT-SPINES.md, im-g4-draft-map.csv and
  data/units.csv blinds and keep `.claude/`, docs/Return/, the spec2 folder, closet/words, the media manifest, the
  `*reconcile*` reviews and ela-6.
- 2026-11-22, run prep (later.csv L102), before any run used kit 1, so the version stays 1: the math subject note is
  written (notes/subject-math.txt: base text and login rule, APPROACH-MATH teaching rules, cold-solved keys with
  error letters, the Goal map exit shape, paper path, invented story problems, sourced real-world numbers); grade
  notes for grades 4, 5 and 6 (notes/grade-4.txt, grade-5.txt, grade-6.txt) for social studies 4 and 5 and World
  Geography and Ancient Civilizations I; `scripts/coursegen.py` takes each course's subject and grade from
  data/plans/frames.csv, so a course named without its grade (World Geography I, Algebra I) finds its grade note.
- 2026-11-22, browser checks (Cory, standing rule): a source page an agent cannot open (403, bot wall) is no longer
  cut on sight; the fact stays as "browser check" with its url and the job lists it, and the lead opens the list in
  Claude in Chrome at the grade's close (retool-stop step 0). Never a scraper or a way around a block. common.txt,
  text2.txt and retool-stop.txt changed; docs/COURSE-RUN.md stage 5 and AGENTS.md say the same.

### Left for a later retool (not in version 1)

- Scripts behind the checks (alignment audit section 5): unit-level ledger seed, plan.py one-ask and cold-word checks,
  lesson.py turn-time and marking-time checks, defects.csv `made_at` column, token report. Other agents own those.
- Gate quirks the writers listed as template points (warm-up id rule on repair days, `assess=observe` versus the
  unitplan check, no-exit day kinds, 300 to 500 word teacher caps on short days). These are gate or DEFAULTS changes,
  settled by the lead and Cory, then logged here.
- Grade notes for grades 7 and up (the generator stops without one: World Geography II, math grades 7 and 8, the
  high school courses).

## Retool 1: KIT-VERSION 2 (2026-11-22)

Source: the lead continuity sweep of 2026-11-22 (no grade running; science K to 3 paused at L81). Wording only, no new rule.

| Finding (stage that found / made it) | Where it went |
|---|---|
| Lines still said a source that cannot be checked is cut, against the browser-check rule (sweep / kit and briefs) | cleanup.txt, key.txt, data.txt, notes/subject-social-studies.txt and the table line above now keep a refused page as "browser check" and point to the Sources rule in common.txt |
| Retired word "exit slip" (sweep / kit) | data.txt, day.txt, checks.txt say exit ticket; the `exit: half` column keeps its name |
| UK spellings in the lines edited (sweep / kit) | US spelling in those files |

## Retool 2: KIT-VERSION 3 (2026-11-23)

Source: the Codex draft run (Cory, 2026-11-23: Codex drafts section plans and days for every lane this week, no reads until later; scripts/codex_draft.py). No grade running in the kit's own runs.

| Finding (stage that found / made it) | Where it went |
|---|---|
| The generator stopped for science: no subject note (generator / kit) | notes/subject-science.txt, written from the science K to 3 run's defaults, safety pages and Cory's sign-off calls (Earth's age rule, spoken comparison counts as produce in K to 2) |

## Retool 3: KIT-VERSION 4 (2026-11-25)

Source: consolidation step 4.D (docs/CONSOLIDATION-PLAN.md). No grade running.

| Finding (stage that found / made it) | Where it went |
|---|---|
| Hand-written CSV writes kept causing truncation and wrong-row overwrites (lead reads / jobs) | scripts/rows.py upsert, named in the CSV safety line of common.txt |
| Ledgers moved from data/plans/ledgers/<subject>.csv to data/plans/<course>/ledger.csv (consolidation / kit) | the CSV safety line of common.txt; scripts/ledger.py commands unchanged |
| Skeletons were tracked and jobs could edit them, so generated files drifted from their source (consolidation / kit) | day.txt: skeletons are ignored working files, never edited; the edit line no longer lists them (step 4.E) |
| day.txt still said "section not in data/units.csv" failures are known, after 4.B removed that check (consolidation / kit) | the line is dropped |

## Retool 4: KIT-VERSION 5 (2026-11-25)

Source: the pause-4e Fable review (docs/reviews/consolidation/pause-4e-review.md), consolidation 4.E2 step 0. No grade running.

| Finding (stage that found / made it) | Where it went |
|---|---|
| Skeleton generators kept an existing file, so a job reran them and read a stale skeleton (review / consolidation 4.E) | day_skeleton.py and section_skeleton.py always rebuild; section.txt rebuilds its skeletons at job start; coursegen always emits the build line |
| Two jobs writing one course's ledger at once could lose rows (review / consolidation 4.D) | scripts/safe_write.py (a lock per file, a temp name per process, retries) under ledger.py and rows.py, with race self-tests; common.txt says jobs in one course may both write through them |
| draft-fix.txt still said "section not in data/units.csv" failures are known (review / consolidation 4.B) | the line is dropped |

## Retool 5: KIT-VERSION 6 (2026-11-25)

Source: consolidation 4.E2 (docs/CONSOLIDATION-PLAN.md), Cory's choice to stop storing fact copies in plans. No grade running.

| Finding (stage that found / made it) | Where it went |
|---|---|
| Written plans stored copies of data inside `<!-- skel -->` blocks, and the copies drifted from data (consolidation 4.E census: 6,250 lines not in a fresh render) | blocks stripped from all 916 plans; facts render from data through scripts/plan_facts.py (skeletons, plan.py packets, Front Office, the writer's read view); `skel-guard` gate and unitplan.py check fail on any marker in a plan |
| Briefs told writers to keep or fill the marked fields in the plan (consolidation 4.E2) | plan-codex.md, plan-codex-ela.md, plan-codex-math.md, plan-codex-science.md, plan-codex-read.md and section-write.md: the facts are read with `plan_facts.py <course> <file>`, never copied into the plan; the plan holds judgment prose only |
| Generators wrote UK spellings into rendered lines (consolidation 4.E2) | unit_skeleton.py and section_skeleton.py write "practiced" |

## Retool 6: KIT-VERSION 7 (2026-11-25)

Source: consolidation 4.G (docs/CONSOLIDATION-PLAN.md), one gate command. No grade running.

| Finding (stage that found / made it) | Where it went |
|---|---|
| Briefs gave two filtered gate commands, `{PLANGATE}` (an awk filter over plan.py check) and `{LESSONGATE}` (a grep over lesson.py check), and workers counted FAIL lines by hand, including lines after the course summary (consolidation review) | one placeholder `{GATE}` = `python -X utf8 scripts/gate.py --course <course>` in checks, cleanup, continuity-fix, data, day, key, retool-stop and sample-read; coursegen.py's sweep gates use it too; common.txt's gate rule says store `--baseline` first, exit 1 means a new failure |
| Briefs carried the known exception "section ... not in data/units.csv" (consolidation 4.B retired the file) | dropped from checks.txt and data.txt |
| AGENTS.md said one worker at a time, while course runs worked side by side (consolidation review) | common.txt and AGENTS.md: side by side in different courses, never the same course or file at once |

## Retool 7: KIT-VERSION 8 (2026-11-25)

Source: consolidation 4.H (docs/CONSOLIDATION-PLAN.md), homes and ids. No grade running.

| Finding (stage that found / made it) | Where it went |
|---|---|
| The never-open lists in 14 briefs and common.txt were typed by hand, drifted, and still named data/units.csv (consolidation plan 4.H) | one line per brief rendered from data/homes.csv by `scripts/homes.py briefs --write`; `homes.py check` fails a line that differs from the render |
| Per-course reports landed at the top of docs/reviews/ (consolidation 4.H home rule) | cleanup, key, plan-fix, plan-read, sample-read and sweep write to `docs/reviews/{COURSE}/`; plan_flow.py reads there first |
| A revised item got a `-v2` id, so ids changed under every link (consolidation 4.H) | data/plans/README.md: a revised item keeps its id, the version goes in `version`; plan.py fails a new suffixed id |

## Retool 8: KIT-VERSION 9 (2026-11-25)

Source: the step 4 close review (docs/reviews/consolidation/step4-close-review.md), findings 1, 2 and 7. No grade running.

| Finding (stage that found / made it) | Where it went |
|---|---|
| A course gate with no stored baseline passed, and a job could store a broken course as its own baseline (step 4 close review, finding 1) | gate.py --course stores the baseline itself on an unchanged course, refuses --baseline on a changed one and exits 2 with no baseline; common.txt, day.txt, cleanup.txt and continuity-fix.txt no longer tell jobs to store one |
| The course gate printed every known line (math K 8,721 lines) and plan.py printed same-stem pairs one by one (finding 2) | the gate prints counts by rule and only new lines (`--verbose` for all); plan.py groups same-stem files per unit (math K plan lines 4,292 to 82) |
| common.txt said both "two jobs never write the same course" and "jobs in one course may both write" (finding 7) | one sentence: never two jobs in the same course at once |

## Retool 9: KIT-VERSION 10 (2026-11-25)

Source: the step 4 close review, finding 4 (consolidation 4.L row 6). No grade running.

| Finding (stage that found / made it) | Where it went |
|---|---|
| The word backlog counted every ledger term row (16,128 heads, mostly phrases a later day leans on, not words a student is taught) (close review, finding 4) | ledger term rows carry student_word yes or no (default no); day.txt and section-write.md tell writers to add `--student-word` only for a word the page teaches students as vocabulary; vocabulary.py report counts only yes rows |

## Retool 10: KIT-VERSION 11 (2026-11-25)

Source: the step 4 close review, "what got worse" (c) (consolidation 4.L row 8). No grade running.

| Finding (stage that found / made it) | Where it went |
|---|---|
| The debt baselines (the `--all` lesson check and lint style lines) had no schedule, so they could sit forever (close review, "what got worse" (c)) | cleanup.txt part D "Known debt": the cleanup job works a course's known debt down and reports "known debt fixed / left by rule"; the lead records the count per grade close with `gate.py --course <course> --record` into data/plans/debt.csv (COURSE-RUN.md stage 6) |

## Retool 11: KIT-VERSION 12 (2026-11-25)

Source: the Fable read of 4.L, finding 1 (later.csv L133). No grade running.

| Finding (stage that found / made it) | Where it went |
|---|---|
| Goal test 10 checked one direction: a written ledger row must name a day with a file, but a day file with no ledger row passed, and the day's `version:` line was never read (Fable read of 4.L, finding 1) | index.py status report fails a day file with no written ledger row and a day file with no version line; ledger kind `none` for a day that introduces nothing new; day.txt tells writers to add one `none` row for such a day. The 34 days found on 2026-11-25 are baselined and worked off under later.csv L136 |

## Retool 12: KIT-VERSION 13 (2026-11-25)

Source: the pedagogy-architecture review (docs/reviews/consolidation/pedagogy-architecture-review.md), changes 2, 3, 6, 7, 8 and 9. No grade running.

| Finding (stage that found / made it) | Where it went |
|---|---|
| A day's retrieval was picked by rule 2 alone; the plan could not say which earlier skill a day brings back (review change 7) | days.csv `retrieves` column; data.txt tells the plan-data writer to fill it; unit_skeleton.py rule 2 uses a stated retrieval first |
| Grade-close pass marks were prose in grade reports (review change 3) | data/plans/pass-marks.csv via scripts/pass_marks.py add at stage 6 Fix; shown on the Dashboard quality panel |
| Day version lines never moved past draft, and a day read against data that later changed looked finished (review changes 2 and 6) | scripts/day_version.py moves version lines at grade read and sign-off and stores upstream marks (day-marks.csv); index.py status lists days whose upstream changed |
| No reading of how far apart returns sit (review change 8) | scripts/spacing.py, read at the stage 4 gate and at grade close (COURSE-RUN.md) |
| English learner supports were named in two places: section plan field 9 (APPROACH principle 9) and stage 7 Make (review change 9) | made in the lesson only (section field 9, day sentence frames); stage 7 checks them across the course and fills a gap it finds |

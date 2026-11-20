# Course run alignment: gaps and plan

2026-11-20. Saved for later as L87. Start only after the ELA and social studies K-3 run closes (its report,
capstone pass and commit done). Nothing here changes the kit while that run is going.

Source: a read-only audit of the repository against docs/COURSE-RUN.md (draft 3), with the main claims checked by
hand. Line numbers are as of 2026-11-20 and may have moved.

## Continuity: where the process does not match COURSE-RUN

### 1. Bookkeeping and docs

| Gap | Where | What to change |
|---|---|---|
| No later.csv row for the ELA and social studies run; jobs call themselves "L81, second test", but L81 is the science ladder (done) | data/plans/later.csv:82; _scratch/ladder2/*.txt line 1 | Add a done row for the run at run end; drop L81 labels from the kit |
| Course shape, dose and lanes settled only in STATE.md | _scratch/ladder2/STATE.md (2026-11-20 draft 2 block) | Log in DESK-ANSWERS (COURSE-RUN says they live there) |
| HANDOFF next steps are the old probe and guard order; science ladder shown as paused; this run not named | docs/HANDOFF.md:11, :89-102 | Point next steps at COURSE-RUN |
| PRODUCTION-PATH step 7 "section plans one section ahead", step 8 per-day writer, cheap, expert and fix cadence; "After the core subjects" never names COURSE-RUN | docs/PRODUCTION-PATH.md:220-273, :282-301 | Point both at COURSE-RUN; keep the history |
| Pipeline README and briefs describe the old flow | docs/pipeline/README.md:17-19, :34-49; briefs/section-write.md:96-117; briefs/write.md:16-20 | Replace "In a ladder run" and "no read follows"; add the planned-only rule to write.md |
| ledger.py says it was built for the science ladder | scripts/ledger.py:9-11 | Reword the docstring |
| Tool-cadence docs (Build and Refine waves) read as the runbook | docs/agents/RUNBOOK.md:9-33, :112-117; BUILD-PLAN.md:3-30 | Mark them as tool-only, link COURSE-RUN for courses |

### 2. Template bugs

| Gap | Where | What to change |
|---|---|---|
| `fill` replaces the token UNIT inside "UNIT-PLAN.md": 53 plan-data jobs point at docs/courses/N-PLAN.md | _scratch/ladder2/gen2.py:11-21 | Use tokens that cannot sit inside other words (for example {UNIT}) |
| Report date hardcoded | _scratch/ladder2/keyjob.txt:12 | Fill the date at generation |

### 3. Rules held only in lead prompts or STATE.md

Shape notes on plan items, the "planned only" rule for review notes, turn-taking time, ledger gating, the
no-git-at-all wording, and the cost reminder. Move each into datajob.txt, dayjob.txt or secjob.txt, and give the kit a
version line so a run can say which version it used.

### 4. Run order against the stage flow

| COURSE-RUN says | The ELA and social studies run did | What to change |
|---|---|---|
| Stages 5 and 6 interleave one grade at a time | All section plans first, then data and days; ELA grades 1, 2 and 3 ran at once | Generator emits per-grade order |
| Kit frozen within a grade | Kit changed mid-grade (lead run notes, shape notes made required) | Changes logged and applied only between grades |
| A fresh read of each grade's plans, then one fix job | No plan read (secjob.txt:1, section-write.md:116) | Add plan-read and fix jobs |
| Unit 1 probe in a subject's first grade | None | Probe mode in the generator |
| Sample read at each grade's close | One sample after all grades (STATE.md:52) | Grade-close sample job |
| Cross-grade continuity pass as a stage 7 job | One-off for ELA | Template plus a ledger.py re-check mode |
| Retool at stage and grade end | Ad hoc mid-run | A retool log per stage and grade |

### 5. Checks named in COURSE-RUN with no script behind them

| Stage | Check | Where it would go |
|---|---|---|
| 2, 4 | Ledger seeded at stage planned (now only at section plans); math not on the ladder | scripts/ledger.py (LADDER, a unit-level seed) |
| 4 | Each goal names its exit kind; practice shape differs from the exit; review entries point at real earlier rows | scripts/unitplan.py, UNIT-PLAN template fields |
| 5 | One ask per item; shape notes present; cold check words | scripts/plan.py |
| 5, 6 | Review claims only on rows at stage written ("planned only" otherwise); a day job waits until its ledger rows are written | scripts/ledger.py check and a gate command; lesson.py check_review_named |
| 6 | Turn-taking time, exit slot and marking time; copied exit text (now number reuse only) | scripts/lesson.py, scripts/plan.py:867-899 |
| Fixes | Every finding logged with the stage that made it; a sweep job | defects.csv `made_at` column (plan.py:1286), a sweep template |
| Cost | Tokens per day and per minute of class; tokens per planning stage | A token report script reading frames.csv minutes |

### 6. Elective pre-work against stage 1

| Gap | Where | What to change |
|---|---|---|
| Dose not cited | health/APPROACH.md:122-124 ("ours and untested"); physical-education/APPROACH.md:92 ("from memory") | Cite the national body's figure |
| Library has one course for grades 6 to 8 (K-8 is one course per grade) | library/APPROACH.md:41 | Desk card: settle the course shape |
| Calibration run once on the core, not per subject | docs/reviews/calibration-2026-11-13.md | Add per-subject calibration to stage 1 |

## Plan, in order

Each step lists its done-check.

1. **Template bugs.** Fix gen2.py tokens and the keyjob date. Done when a regenerated job names UNIT-PLAN.md and
   today's date.
2. **Bookkeeping.** later.csv row for the finished run; DESK-ANSWERS entries for course shape, dose, lanes and the
   COURSE-RUN adoption. Done when DESK-ANSWERS answers "where is the dose rule".
3. **Docs point at COURSE-RUN.** HANDOFF, PRODUCTION-PATH (steps 7, 8 and "After the core subjects"), pipeline README,
   section-write.md, write.md, ledger.py docstring, a tool-only note on RUNBOOK and BUILD-PLAN. Done when no living
   doc describes the old day cadence as current.
4. **Elective pre-work.** Cite health and PE dose; Desk card for library 6 to 8; calibration added to the stage 1
   checklist. Done when every APPROACH dose line has a source.
5. **Kit.** Move every lead-prompt rule into the job templates; add a kit version line and a retool log. Done when a
   job runs correctly with no extra run notes.
6. **Generator.** Per-grade order (section plans, plan read and fix, data and keys, days, grade sample, retool), unit 1
   probe mode, continuity-pass job. Done when the generator writes the math K-3 queue in COURSE-RUN order.
7. **Ledger.** Math on the ladder, a unit-level seed, the planned-only check, a gate command for day jobs. Done when a
   day job whose rows are still planned is refused.
8. **Fix tracing.** `made_at` column in defects.csv and a sweep template. Done when a logged finding carries both
   stages.
9. **New gates.** unitplan.py (exit kind, practice shape), plan.py (one ask, cold words), lesson.py (turn time,
   marking time, copied exit text). Done when each is tried on a planted fault and catches it.
10. **Token report.** Per day, per minute and per planning stage. Done when the run report's cost table comes from the
    script, not by hand.

Steps 1 to 9 come before the next run (math K-3 and social studies 4, 5 and World Geography I). Step 10 can follow.
The ELA and social studies run report's findings join step 5 as retool 0.

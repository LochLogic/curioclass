# Course-production audit: working top-down from the base texts (2026-11-13)

Asked by Cory: "Now that we have large data sets, is it better to work from the widest scope down to the narrowed
day by day? Architecturally, how can we best turn our new, large data sets into something that hits our end goal?"
Run by a fresh, read-only agent on the layer-audit method (stages scored on how measured they are and how sure we
can be the design is right). Saved by the lead session. Evidence: COST.md, REVIEW-CADENCE.md, INTEGRATION-PLAN.md,
u04-1.md, cheap-d025, defects.csv, analysis-math.md, IM lesson-07. Written before the reads of days 26 to 28.

## 1. Summary

**Yes, work top-down, but bring the base text in at the top, not at the day.** Today the writer gets a finished
unit plan that already fixes numbers, minutes and moves, plus the IM lesson, and spends much of its effort
reconciling the two (day 25 +9% writer tokens on unit 2, day 26 +24%). The IM lesson itself is about 4,000 tokens of
a 210,000 to 240,000 day: the rise is reconciliation, not reading.

Recommended hybrid: **our frame stays ours and comes first** (scope and sequence, end-of-unit assessments, error
register, readiness checks, exits; IM gives nothing there, it is behind its login). **Below the frame, section
plans come from a per-course source map**: each day row names the goal, the source parts, the exit and the error
letters, and the writer picks numbers and contexts.

Honest size of the payoff: a base text is mainly a quality lever. At most it removes about a quarter of a writer's
tokens, about 10% of a fully read day. The big cost lever is the expert read (36% of a day), which shrinks only when
expert-only findings fall to about one per day. Base texts cover 21 of 105 courses (about 20% of days), so the
pipeline must not fork: a base text is an optional column, not a second process.

## 2. Stage scoreboard

R = refined (how much measurement has hit it), B = best setup (how sure the design is right now). Out of 10.

| # | Stage | R | B | Basis |
|---|---|---|---|---|
| 1 | Source store, licences, catalog | 5 | 7 | Manifests, catalog, drop lists exist (MEASURED). Source quality against our rubric never checked (ASSUMED). |
| 2 | Course scope and sequence | 2 | 4 | Only grade 4 math has one; drawn blank before any base text; cost and effect unmeasured (DERIVED). |
| 3 | Fit table, source to our units | 1 | 6 | Prose, grade 4 math only, unread. Needed; form untested (DERIVED). |
| 4 | Unit plan (sNN.md) | 2 | 5 | One cold read (s11: 15 findings); tokens never measured; 51 of 864 ledger findings in the plan layer because plans are barely read (MEASURED). |
| 5 | Section plan, day rows | 2 | 3 | Rows fix numbers, minutes, moves, contexts: exactly what the source supplies, so the conflict lives here (MEASURED, n=2). |
| 6 | Plan as data (CSVs, plan.py) | 6 | 7 | 81,000 to 250,000 per unit, heavily gated; exits, keys, wrongs stay ours in any order (DERIVED). |
| 7 | Shared pieces | 5 | 6 | 165,000 to 231,000 per unit; IM family materials, glossary, practice unused (DERIVED). |
| 8 | Source extract per day | 0 | 5 | Not built; IM .md is clean, OpenSciEd and EL are PDFs and zips (MEASURED by file type). |
| 9 | Day writer and gates | 8 | 5 | **Flag.** Most measured stage (132,000 drifting to 194,000 per day); unproven with a base text. |
| 10 | Seams and hand-offs | 6 | 7 | Parallel writing broke seams in unit 3; order plus seam gate fixed it (MEASURED). |
| 11 | Cheap focused read | 7 | 7 | Three units; expert agreed with 80 to 85% of its findings (MEASURED). |
| 12 | Expert read, every day | 8 | 5 | **Flag.** 460 findings; expert-only stuck at 3 to 6 per day; never checked against a human; writer and expert are the same kind of model (FOUNDATION 7.1). |
| 13 | Fix pass and gate promotion | 7 | 6 | **Flag.** 70 to 81% of findings repeat a known kind; fixed days never re-read; the reliability review is the first check. |
| 14 | Rights and credit gate | 3 | 7 | Name gate plus cheap-read check 7; light rigor is Cory's call (ASSUMED sufficient). |
| 15 | Build, print, site | 6 | 7 | Gated, byte-stable PDFs; unaffected. |
| 16 | Teacher read (FOUNDATION 7.3) | 1 | 6 | 11.1 pack sent 2026-11-12; no result yet. |
| 17 | Taught run, timed students | 0 | 5 | None yet. |
| 18 | Cory's Desk | 4 | 8 | 0 to 1 owner minutes per unit (MEASURED). |

Pattern: the middle (9 to 13) is heavily measured; both ends (plans upstream, people downstream) have almost no
data. Omitted: tool builds and the Codex queue, art and voice, Spanish, the standards ledger, progressions, rubric
and approach pages, Sara's specs, deploy.

## 3. Alternatives for stages below 7

- **Scope and sequence (2).** Arms: ours from blank (incumbent); adopt the base order and lesson count with a short
  deviation list; ours with unit edges snapped to the source. Test: count order conflicts per course from the fit
  table (desk work). Expected: grade 4 keeps its approved order (four conflicts, 44 days written, IM's 149 lessons
  near our 150 days); every base-text course without a scope and sequence takes the base order, as Cory chose for
  science 6 to 8.
- **Fit table (3).** Prose (incumbent) or a CSV row per source lesson. All 1,292 IM lesson.prep.md files carry
  "CCSS Standards" and "Learning Goals" (MEASURED), so a script fills most of it.
- **Unit and section plans (4, 5).** Arms: full prescriptive plan (incumbent); a thin row (goal, base parts, exit,
  error letters, minutes, moves only where we deviate); the planner adapts the source at plan time. Test: plan grade 4
  unit 8 (place value, 10 days against IM 4.4.6 to 4.4.17, no order conflict) base-text-first, write three days, same
  reads. Expected: planning tokens down, writer at or below the no-source baseline, expert-only findings flat to lower.
- **Source extract (8).** None needed for IM (lesson plus prep about 3,600 tokens). OpenSciEd and EL need a
  once-per-unit PDF-to-markdown extract.
- **Day writer (9).** Add an "approach transform" card per base text: IM runs launch, explore, synthesize; our grades
  2 to 5 default is teaching first (APPROACH.md). Decide that conversion once, not every day.
- **Expert read (12).** Arms: every day (incumbent); one day in five; one set read per section (3 to 4 days as a
  teacher would). The reliability review is a set read: log its tokens and per-day yield, seams included. Validity:
  have the teacher reader mark which expert findings are real on the 11.1 days.
- **Fix pass (13).** The reliability review's residual is its measurement.

## 4. The top-down comparison

Baseline per fully read day (unit 3, MEASURED parts; planning not measured):

| Part | Tokens per day | Share |
|---|---|---|
| Writer | 181,000 | 33% |
| Cheap read | 118,000 | 22% |
| Expert read | 195,000 | 36% |
| Unit-level pieces per day | about 48,000 | 9% |
| Total | about 540,000 | |

(Unit 2, three days, about 650,000 per day. The agent "tokens" figure is probably end-of-run context size, not billed
tokens; log tool uses beside it.)

What a base text can remove from a writer's day (DERIVED from file sizes): fixed reads (template, brief, examples,
neighbours, plans, CSV rows, gate output) 60,000 to 90,000, not removable; thinking, drafting and churn 90,000 to
120,000, of which only the activity design is removable; the source itself 4,000 to 7,000, a cost. **Upper bound
about 50,000 to 60,000 per day: 25 to 30% of the writer, about 10% of a fully read day.** Always ours: items, wrongs,
keys, the trace, At home, Tomorrow, gates, both reads.

- **(a) Current order (our plan first, source at the day).** Writer 211,000 and 240,000 (n=2), about 575,000 per day
  all in. A reconciliation tax on every day of every base-text course planned blind. Low source dose: the test may
  barely measure the source.
- **(b) Base-text-first.** A source map per course, about 100,000 to 150,000 once, mostly scripted (ASSUMED); thinner
  section plans; writer likely 160,000 to 190,000 (ASSUMED). Risks: explore-first against teach-first, exits drifting
  from an arc we did not design, wording close to the source. Whether expert-only findings fall is unknown and decisive.
- **(c) Hybrid (recommended).** Our frame first (scope and sequence, units with assessments, error register,
  readiness, exits), then the source map shapes section plans and day rows. Day costs as (b), frame costs as today.
  Honours FOUNDATION's "we do not stitch two programs": reordering IM lessons inside a plan designed blind is closer
  to stitching than following one arc.

No-base subjects (84 of 105 courses) use the same frame and course map, filled from references (order, unit size,
anchors), no copying; the day pipeline is identical.

Honest size: about 13,300 days (56 core courses at 150, 49 others at an assumed 100). At 540,000 per day about 7.2
billion context tokens; with step 3 earned (cheap read every day, expert read one day in five) about 390,000 per day,
5.2 billion. Planning, teacher reads and taught runs on top, unmeasured.

## 5. Recommended architecture, smallest first

1. A `base` cell in data/plans/<course>/days.csv (`im:4.3.7:warm-up,a1`), format checked by plan.py.
2. docs/sources/IM-TO-DAY.md, the approach transform card (IM part to LESSON-DAY part, launch-explore to teaching
   first, drops, lean-cuts). Mostly in analysis-math.md section 2. Later one each for OpenSciEd and EL.
3. data/plans/<course>/source-map.csv, one row per base lesson: source id, title, minutes, standards, goals (scripted
   from prep.md), our unit, our days, use (keep, split, merge, cut, ours), leans to cut, note. Built once per course
   at its scope and sequence step; for no-base courses the same file with reference rows.
4. A thin day-row form for base-text days in UNIT-PLAN.md: moves only where we deviate; numbers and contexts left to
   the writer.
5. Once-per-unit extracts for OpenSciEd and EL at S:\CurioClass-sources\_extract\<source>\<unit>\L03.md (scripted
   from the PDFs; a Codex job).
6. Keep deferred: basepack.py, the 8-word index, any whole-store index or embeddings.

Who: the lead writes cards and plans; Codex writes scripts; day writers take turns; a smaller model does the cheap
read; the expert reads; people do the human reads.

## 6. Process and order of work

1. Finish stage 1 of the unit 4 test with the measures in section 7.
2. Base-text-first test on grade 4 unit 8: source map, thin plans, three days, same reads, planning tokens measured
   (about 2 million tokens).
3. Decide; plan the rest of grade 4 (units 5 to 8, 12 to 18) under the winning arm.
4. Frames for the other base-text courses in one batch while days stay depth-first (math K to 3, 5 to 8, Algebra 1,
   Geometry, Algebra 2; ELA K to 5; science 6 to 8 redraw): source map, scope and sequence adopting the base order
   with deviations, expert read. Cheap, and gives the 105-course plan real sizes.
5. No-base courses follow the same frame-first path with references.
6. A qualified teacher on the first adapted section of each base text (IM, then OpenSciEd, then EL), plus the open
   11.1 read; the teacher marks which expert findings are real.
7. Cadence with a base text: cheap read every day; expert every day of the first adapted unit per base text; step 3
   once expert-only findings are at one per day or fewer; then a set read per section if it catches more per token.

## 7. What to measure in the running test

1. Per day: writer tokens and tool uses; the writer's conflict list (plan said X, source said Y, chose Z); the source
   dose (share of parts from the source).
2. Controls: day 28 ("fluency, mostly ours") in stage 1; days 36 to 37 in stage 2. Writer tokens have risen about 10%
   per unit as briefs and gates grew, so a unit 2 comparison mixes two effects.
3. Findings per day by kind, especially "teaching sense" (an example does not teach what the exit asks; a rule false
   in general): the class a base text could reduce. Rights findings zero.
4. Noise: within a unit writer tokens vary about plus or minus 20% and findings 7 to 14 per day, so four days show only
   large effects. Treat the go rule as indicative.
5. Final reliability review: a fresh expert reads days 25 to 28 as a set plus the 24-25 and 28-29 seams; residual
   findings per day by severity (blocker: wrong mathematics or cannot be taught; major: students miss the goal or a
   key is wrong; minor: wording or layout), by layer and by origin (source-adapted part or ours); regressions from
   the fix pass; a yes or no per day on "a teacher could teach this tomorrow with no prep"; its own tokens.
6. The same reliability brief on a control set (unit 2 days 7 to 9 after their fixes, about 250,000 tokens), or the
   residual has nothing to compare against.

## 8. Open questions for Cory

1. For base-text courses without a scope and sequence: is the base text's unit order and lesson count the default
   frame, as chosen for science 6 to 8?
2. Does grade 4 math keep its approved order (adding before multiplying among four conflicts)?
3. Who is the teacher reader for the first adapted section of each base text, and when?
4. Is about 2.3 million tokens acceptable for the control reliability read plus the unit 8 base-text-first test?
5. IM's cool-downs and teacher guides are CC BY behind a free sign-in. Take them? (An account would need Cory.)

## 9. Corrections to its own earlier claims

1. Reading the base text is about 2% of a writer's tokens, not a large share: the rise is reconciliation.
2. Token figures are probably end-of-run context size, not cumulative billed tokens.
3. It first leaned toward re-sequencing grade 4 to IM's order; with an approved order, 44 written days and four
   conflicts, grade 4 keeps its order.
4. No pack script is needed for IM; only the PDF sources need extraction.
5. This test is the worst case for arm (a): the worst fit in grade 4 (14 days against 6 lessons, reversed order), on a
   plan that predates the source.

## 10. Not checked

The reads of days 26 to 28; the writers' own reports (relied on the lead's summary); how the agent token figure is
defined; whether IM's pedagogy meets RUBRIC-MATH-K8; how hard OpenSciEd and EL PDF extraction is; planning cost;
teacher-read results; day counts for the 49 non-core courses (assumed).

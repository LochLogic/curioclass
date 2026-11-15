# Sequence read: Algebra I, 2026-11-15

Expert cold read of the Curio Class Algebra I scope and sequence (grade 9), done under docs/pipeline/briefs/sequence-read.md with the math lens. The named bar, docs/RUBRIC-MATH-K8.md, has no high school notes, so the read applies the lens, the band rules and the earlier reads' settled choices. First of three high school math reads; "Across the band" is in the Algebra II report.

## What I read

- AGENTS.md, docs/agents/EXPERT.md, docs/agents/lenses/math.md, docs/GLOSSARY.md, docs/pipeline/briefs/sequence-read.md and sequence-write.md, docs/RUBRIC-MATH-K8.md.
- docs/courses/algebra-i/frame.md and scope-and-sequence.md in full.
- data/plans/algebra-i/days.csv (160 rows) and source-map.csv (294 rows).
- data/progressions/math.csv, grade 6 to 11 rows; data/plans/math-grade-6/7/8/days.csv for the last use of every assumed row.
- The base: Illustrative Mathematics Algebra 1, 1st edition (S:\CurioClass-sources\illustrative-math\hs-algebra-1), every lesson's title, teacher and student goals and learning targets, the course standards page and the modeling prompts.
- data/plans/calendar.csv; the frame read docs/reviews/frame-algebra-i-2026-11-14.md; the biology, chemistry and physics sequence reads (2026-11-14) for math leans; the math grade 8 sequence read (2026-11-15) and its "Across the band".
- Gate output: plan.py check, sequence.py check, frame.py calendar, stale.py check.

## Verdict

A faithful, well-built sequence: all 132 IM lessons kept in order, readiness placed correctly by grade number, one extended task per end day, modeling prompts moved to unit ends for a reason that holds, and no copied wording. It repeats the band's main fault: the year-end check samples the fluency expectations only inside critique forms, so Geometry and Algebra II receive no direct record of equation solving or hand graphing. Its course-level checks overclaim and re-collect recent records, and the codes Algebra I begins for later owners are taught for many days but never named on any check. Ready after the fixes below, none of which adds a day.

## Findings

### 1. The year-end check does not sample the fluency expectations directly (serious)

- What is wrong: the frame names A-REI.B.3 (linear equations and inequalities in one variable), F-IF.C.7a (graph linear and quadratic functions by hand) and the begun A-SSE.A.2 (seeing structure to rewrite) as the course's fluency. Day 158 is "repair a decision tree" and day 159 an "evidence-ranking" across function families. A-REI.B.3 and A-SSE.A.2 are on neither day; F-IF.C.7a is on day 159 inside a ranking of supplied work. No item asks a student to solve, rewrite or graph from a blank page. The last direct A-REI.B.3 record is check 1 (day 60).
- Why it matters: the band rule says every year-end check samples each fluency expectation directly at a short independent station. Geometry opens unit 6 and Algebra II opens unit 2 on these skills, and day 160's hand-off record says nothing current about them. This is grade 8 finding 1 again, one grade on.
- Fix: on day 158 give the decision tree 35 minutes and add a 10-minute untimed independent station: three linear equations or inequalities (one with distribution and fractions, one with variables on both sides, one inequality whose direction flips), two structural rewrites (a difference of squares and a factor out of a trinomial), and one hand graph of a quadratic in factored form with intercepts and vertex. No supplied steps. Add A-REI.B.3 and A-SSE.A.2 to the day's codes, call it "direct fluency sample" in the note and the check table.
- Evidence: days.csv days 60, 156, 158, 159, 160; frame fluency line; grade 8 finding 1 and "Across the band" call 1. Confidence: firm. LAYER: sequence. REPEAT: yes.

### 2. Begun codes are taught for many days but never named on a check (moderate)

- What is wrong: 26 codes that teaching days carry appear on no end-of-unit, mid-unit or course-level check. Most are begun here and owned later (the progression gives them to Algebra II or Geometry): F-IF.B.4 (21 teaching days), F-BF.A.1a (16), F-LE.A.2 (15), A-CED.A.2 and A-SSE.A.2 (10 each), F-BF.A.1 (9), F-LE.B.5 (8), A-CED.A.1, A-SSE.B.3 and S-ID.B.6a (7 each), A-SSE.A.1 and F-BF.B.3 (6), A-REI.A.1 (5), N-Q.A.1 to A.3 (3 to 4 each), and single-day F-IF.C.7b, C.7e, C.8, C.8b, A-REI.C.7, A-REI.D.11, A-SSE.B.3c. Day 106 says it uses "products from days 98 to 105 for the started codes" without naming them, and day 129's hand graphs cover intercepts and extrema without listing F-IF.B.4.
- Why it matters: the later owners assess these in other contexts only. Algebra II assesses F-IF.B.4 in trigonometry (day 135), F-LE.A.2 with rational inputs (day 94) and F-BF.A.1a with combined functions (day 108). The linear, quadratic and exponential parts that Algebra I teaches for weeks reach no record, so no hand-off can say whether a student can read key features of a quadratic graph or build a linear rule from a context. A day counted for a code that no check names is a day with no evidence.
- Fix: each end-of-unit assessment lists the begun codes whose taught part it samples, with the part named: day 45 "A-CED.A.1, A-CED.A.2, linear cases"; day 82 "F-IF.B.4, linear and piecewise"; day 106 "F-LE.A.2, F-LE.B.5, F-BF.A.1a, linear and exponential"; day 129 "F-IF.B.4, quadratic; F-BF.B.3, vertical and horizontal shifts"; day 156 "A-SSE.A.2, A-SSE.B.3, quadratic". The day 160 hand-off carries these partial records forward. Whether any begun code should change owner is the lead's call, and moving a standard between courses is Cory's.
- Evidence: days.csv codes and assess columns (count over all 160 rows); data/progressions/math.csv owners; Algebra II days.csv days 94, 108, 135. Confidence: likely. LAYER: sequence. REPEAT: new.

### 3. The course-level checks overclaim and re-collect recent records (moderate)

- What is wrong: day 61 lists nine codes, including all unit 3 codes three days after day 58 recorded them. Day 109 re-prompts F-LE.A.1 three days after day 106, and its task, "compare rival model proposals", is the form of day 105's "compare growth models for supplied national debt data", although every check note says "This task form has not appeared in the preceding ten school days". Day 159's evidence-ranking repeats the choose-a-model form of days 153 and 155. Each check note asks "a short prompt for every taught part of each listed code" across six to nine codes in 40 minutes, and respond days list 10 to 14 codes. Day 158 does reuse day 156 records, which is right.
- Why it matters: collect once says a check within ten days reuses the record; the non-repeat rule asks for new forms and contexts. A false boilerplate sentence in every note will be trusted by the unit planner.
- Fix: day 61 drops the unit 3 codes and reuses the day 58 record; day 109 drops F-LE.A.1 parts (reuse day 106) and uses a form not seen in the prior ten school days, for example writing a rule from two points read off an unfamiliar graph; day 159 replaces evidence-ranking with a blank-page task. Strike the boilerplate sentence and write the actual form check for each day. Check days list only the codes they sample.
- Evidence: days.csv days 58, 61, 105, 106, 109, 153, 155, 156, 158 to 160. Confidence: firm. LAYER: sequence. REPEAT: yes (grade 8 finding 2).

### 4. The prerequisite inventory says grade 7 and 8 day evidence is pending (low)

- What is wrong: the inventory marks grade 7 and 8 day maps "absent" and "day evidence pending". Both exist (data/plans/math-grade-7 and math-grade-8/days.csv).
- Why it matters: a stale note invites the next writer to redo the ledger or doubt it.
- Fix: replace the note with "verified against grade 6 to 8 days, 2026-11-15". I checked every row: m7-two-step-inequalities, m7-percent-problems, m7-compare-populations and m7-random-samples have no grade 8 use and get readiness (days 1, 17, 83); m6-data-displays is checked on day 1; every m8 row is retrieved. The placement is correct.
- Evidence: scope-and-sequence.md inventory; grade 7 and 8 days.csv. Confidence: firm. LAYER: sequence. REPEAT: yes (grade 8 finding 5).

### 5. Day 34's mid-unit prose names equations the codes do not carry (low)

- What is wrong: day 34's note says the mid-unit assessment covers "equations"; A-REI.B.3 is not in its codes.
- Fix: add A-REI.B.3 to day 34's codes, or drop "equations" from the note.
- Evidence: days.csv day 34. Confidence: firm. LAYER: sequence. REPEAT: new.

### 6. The source map uses a layout unlike rule 8 and the other math courses (low)

- What is wrong: columns are source, source_unit, source_lesson, source_url, stretch, day, decision, track, note. Rule 8 asks for a reason column; this file has "note". 128 "supports" rows (track optional, no day) sit among the base-lesson rows. Geometry shares this layout; Algebra II and grades 6 to 8 each use another.
- Fix: the lead picks one layout for the band (grade 8 call 4 named grade 6's); rename "note" to "reason" here at the least.
- Evidence: the six source-map headers. Confidence: firm. LAYER: process. REPEAT: yes.

### 7. Frame code lists with a tilde or comma raise false gate notes (low)

- What is wrong: sequence.py check reports "on no day" for A-CED.A.1, N-Q.A.3, A-REI.D.11, A-SSE.A.1b and A-SSE.A.1 in units 2 to 7; each is on a day, but the frame lists it as "~code" or after a comma.
- Fix: semicolons in the frame code lists; the lead decides whether the gate should read the tilde.
- Evidence: gate output; frame.md unit table. Confidence: firm. LAYER: process. REPEAT: yes (grade 8 finding 8).

## Checks the brief asks for

- **Source map against the base:** every IM Algebra 1 lesson has a row, 132 base lessons in order. Decisions: 264 keep (with supports rows), 25 ours, 4 merge, 1 cut. Lessons 1.6 to 1.8 (spreadsheet lessons) merge on day 6 with a reason that holds: one supplied table and paper calculations keep the reasoning without a software dependency. Modeling prompt 1 merges into day 15 as an eight-minute critique. The one cut, the vacation-planning prompt in unit 4, has a reason that holds: the kept comparison prompt already carries the modeling cycle and interval rates. Ours days are assessments, response, readiness and named load days.
- **Base order and departures:** unit and lesson order kept. The one departure is the modeling prompts, which IM places after particular lessons (for example "Planning a Concert" after 7.2); here each sits on the unit's last teaching day (15, 44, 57, 81, 105, 128, 155). The reason, methods are available and the prompt is the unit's full performance, holds.
- **Our words:** all 140 base-linked goal cells compared with their lesson's title, teacher goals, student goals and targets. Highest similarity 0.62 (day 53); none close. **Copy rate: 0 of 140.**
- **Focus:** on teaching days (check and respond excluded), 103 of 135 days carry N-RN, N-Q, A-SSE, A-CED, A-REI or F-IF codes (76 percent; 64 percent weighted by code share); adding F-LE.A.1, F-BF.A.1 and S-ID.C.7, 127 days (94 percent). No high school bar sets a line.
- **Widely applicable prerequisites:** linear equations and inequalities, function notation and interpretation, linear and exponential models, quadratic structure and solving, and rational exponents (N-RN) are each taught and assessed, except the begun parts in finding 2.
- **Coherence from grade 8:** linear functions in all representations (8.F) to function notation and F-IF; 8.EE.C.7 and C.8 to A-REI.B.3 and the systems unit; scatter plots and lines of fit (8.SP) to S-ID.B.6 and residuals; integer exponents (8.EE.A.1) to rational exponents; irrational numbers (8.NS) to N-RN.B.3. Every m8 row is retrieved in its first use, not rebuilt.
- **Modeling across the course:** seven prompt days, one per unit, with supplied data. MP4 is named on each.
- **Rigor:** understanding, fluency and application days in every unit; the 5-minute mixed opening spaces A-REI.B.3 and factoring. Only the year-end direct sample is missing (finding 1).
- **Readiness by grade number:** correct (finding 4). The frame says "idle two or more grades" and "next grade, direct".
- **End days:** each holds one extended task, the retained modeling product, plus short items. Correct.
- **Collect once and non-repeating checks:** finding 3.
- **Science hand-offs:** Biology (same year) uses S-ID.A.1 to A.3 and fitted lines with bridges on both sides; Chemistry (grade 10) leans on A-CED.A.4, S-ID.B.6, S-ID.C.7, S-ID.C.9 and F-LE.A.1c, all taught and assessed here. Physics (grade 11) leans on F-IF.B.6, A-CED.A.4, alg1-quadratic-patterns, alg1-writing-equations-constraints and S-ID.B.6; see the Algebra II "Across the band" for the readiness question.
- **Calendar:** checks on days 60 to 61, 108 to 109 and 158 to 159 match calendar.csv; week 32 is finals.
- **Shorter path:** present, with ten fold-in days, none assessed.

## Lens checklist

| Lens item | Holds | Note |
| --- | --- | --- |
| Major work share | yes | 76 percent of teaching days on core algebra and function clusters |
| Progression coherence | partly | begun codes carry no record (finding 2) |
| Standard taught in part with no finishing day | yes | owners named in the progression |
| Problems that join units | yes | modeling prompts, residuals from linear unit, quadratic versus exponential |
| Fluency spaced and mixed | yes | year-end direct sample missing (finding 1) |
| Practices named | yes | all eight, tied to days |
| Models consistent | yes | tables, graphs and equations side by side; hanger to inequalities |
| Readiness by grade number | yes | verified against grade 6 to 8 days |
| End days not stacked | yes | one extended task per end day |
| Collect once | partly | days 61, 109 (finding 3) |
| Our words | yes | 0 of 140 |
| Source-map layout | no | finding 6 |

## What is right and should not be touched

- Modeling prompts at unit ends, with the reason written.
- The readiness ledger's placements, the hook before the day 1 check, and the m8 rows retrieved rather than rechecked.
- Supplied anonymous data throughout; the individual correlation computation cohorts on days 53 to 55 for a class of 30.
- Day 156's explicit "real cases here; complex cases finish in Algebra II" for A-REI.B.4, and the F-LE.A.3 split between days 106 and 129.
- The Biology and ELA bridges named by day.

## What I could not judge

- Whether the 40-minute check budgets hold with the station added; the unit plans must time it.
- The course id difference (algebra-i against algebra-1) is the lead's, already raised.

## Settled by the expert

| Choice | Reason | File |
| --- | --- | --- |
| Day 158 gains a 10-minute untimed station: three linear equations or inequalities, two rewrites, one quadratic hand graph | Year-end fluency sample (finding 1) | days.csv day 158; check table |
| End-of-unit assessments name the taught part of each begun code | A record goes forward (finding 2) | days.csv days 45, 82, 106, 129, 156 |
| Day 61 reuses day 58; day 109 reuses day 106 and changes form; day 159 gets a blank-page task | Collect once, non-repeat (finding 3) | days.csv days 61, 109, 159 |
| Boilerplate "has not appeared" sentence replaced by the day's actual form check | It is false on day 109 | days.csv check notes |
| Prerequisite inventory marked verified against grade 6 to 8 days | Day maps exist | scope-and-sequence.md |
| A-REI.B.3 added to day 34 | Prose and codes agree | days.csv day 34 |

## For Cory

Nothing.

## Sources

- Illustrative Mathematics Algebra 1, 1st edition (openly licensed pages), S:\CurioClass-sources\illustrative-math\hs-algebra-1: lesson order, goals, modeling prompts.
- Common Core State Standards for Mathematics, high school (data/standards), and the high school Progressions for algebra, functions and modeling (from memory for the limits named; consistent with data/progressions/math.csv).
- docs/RUBRIC-MATH-K8.md: no high school criteria; the lens applied instead.

## For the source list

- A high school bar: EdReports' high school mathematics review criteria (focus on widely applicable prerequisites, coherence, rigor and modeling) would fill the missing bar the frame and this read both note.

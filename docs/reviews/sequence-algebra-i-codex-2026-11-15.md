# Algebra I scope and sequence: independent cold read

**Date:** 2026-11-15  
**Intended report path:** `docs/reviews/sequence-algebra-i-2026-11-15.md`  
**Delivery:** Complete report supplied here. No file created, edited or deleted.

## Verdict

The sequence is coherent overall, but needs five targeted corrections before unit planning. Its biggest risk is that the assessment directions can produce a final record without direct linear fluency evidence or complete evidence of the statistical performances claimed. Preserve the seven-unit order and strengthen those reservations, correct readiness and retrieval timing, and reconcile the stale prerequisite directions.

## What I read

- `docs/agents/EXPERT.md`, the mathematics lens, `docs/RUBRIC-MATH-K8.md`, the foundation, teaching approaches, relevant source-register entries and evidence notes, roadmap sections, BASELINE rules 20 to 24, glossary, and base-text policy.
- The complete Algebra I scope and sequence, all 160 rows of `days.csv`, the complete frame, and all rows of `source-map.csv`.
- All 28 Algebra I progression rows, their earlier-grade prerequisites, and the local standard text for owned and started codes.
- `CALENDAR.md`, the Grade 9 calendar rows, and relevant cross-subject directions in the Biology, ELA Grade 9 and World History I frames.
- Relevant Grade 6, Grade 7 and Grade 8 daily records to verify prerequisite use.
- The stored first-edition base lesson inventory, course narrative, and selected preparation pages concerning standard deviation, formula rearrangement, fitted models and vertex-form graphing.
- Permitted earlier Algebra I frame reviews, their recorded fixes, and relevant mathematics sequence findings to establish REPEAT tags. The blind exclusions were respected.
- Outside sources linked below.

Previous-session memory informed reporting conventions only. No curriculum finding rests on memory.

### Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Algebra I reported zero sequence failures; the repository-wide command then stopped with `ModuleNotFoundError: No module named 'markdown'`. |
| `python -X utf8 scripts/frame.py calendar` | Completed; no stagger-rule break reported. |
| `python -X utf8 scripts/frame.py check algebra-i` | Zero failures; 160 days, comprising 151 unit days and nine check/respond days. |
| `python -X utf8 scripts/stale.py check` | 56 files, zero failures. Manual stale directions remain, as finding 5 explains. |

The sequence checker’s six comma-parsing notes do not establish missing instruction: the referenced codes appear on relevant daily rows.

## Findings, most serious first

### 1. The year-end check does not reserve direct linear fluency evidence

**Severity:** Serious  
**LAYER:** sequence  
**REPEAT:** yes, direct year-end fluency omissions appear in earlier mathematics sequence reviews, including Grade 2, finding 2.  
**Confidence:** Firm

**Location:** Course-level check 3; `days.csv`, days 158 and 159; frame, “Fluency without a timer.”

**What is wrong:** The frame identifies solving linear equations and inequalities as a course fluency. Day 158 reserves a quadratic decision-tree repair, with equations drawn from earlier units, but lists neither `alg1-equation-reasoning` nor `A-REI.B.3`. Day 159 reserves model selection. Neither explicitly asks students to solve a linear equation and a linear inequality independently.

The writing rule requires every year-end check to sample each named fluency directly. Earlier assessment records and daily rotation do not supply that missing year-end reservation.

**Why it matters:** A student could explain a quadratic method-selection tree while remaining unable to solve a linear inequality accurately. The receiving teacher would lack direct evidence of a foundational procedure.

**Exact fix:** Within day 158’s existing individual-work allocation:

- Reserve short independent linear-equation and linear-inequality entries, including rational coefficients and a letter-coefficient case with stated restrictions.
- Add `alg1-equation-reasoning` and `A-REI.B.3` to the row.
- Replace equivalent decision-tree entries rather than adding time.
- Explicitly reserve hand graphing within day 159’s existing `F-IF.C.7a` work, so selecting a function family cannot stand for graphing fluency.

Keep the untimed student experience and day 160 response allocation.

### 2. Statistics assessment reservations leave required student products implicit

**Severity:** Moderate  
**LAYER:** sequence, standard  
**REPEAT:** yes, the same production-versus-recognition problem appears in the Grade 8 sequence review, finding 1.  
**Confidence:** Likely

**Location:** Unit 1 assessment description and days 14 to 16; Unit 3 assessment description and days 50 to 58.

**What is wrong:** The repeated instruction to assess every listed part is broader than the named evidence:

| Expectation | Named evidence | Remaining reservation |
|---|---|---|
| `S-ID.A.1` | A chosen display and display-choice questions | An individual construction record covering dot plot, histogram and box plot |
| `S-ID.B.6` | Fitting, prediction, residuals and model critique | An explicitly retained student-built scatter plot and description of association |
| `S-ID.C.7` | A prediction in units; the narrative mentions slope and intercept units | Separate contextual interpretations of both fitted coefficients |

The [standard text](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf) distinguishes these performances. The kept [base lesson 3.4](https://im.kendallhunt.com/HS/teachers/1/3/4/preparation.html) includes contextual slope and intercept interpretation, but the daily reservation does not carry that instruction clearly.

This is a reservation defect, not proof that the eventual teaching would omit the work.

**Why it matters:** Writers can implement the named comparison and interpretation tasks faithfully while collecting incomplete evidence for the claimed codes.

**Exact fix:**

- On day 14, reserve an independent three-display record from one small supplied data set. Day 16 explicitly scores that record alongside day 15’s comparison.
- On day 56, explicitly retain each student’s scatter plot, association description and fitted line for day 58.
- On day 50, name contextual slope and intercept interpretation in the goal or note. Day 58 reserves a short response for each, including whether the intercept is meaningful in the data setting.
- Carry these evidence references into course check 1 wherever the corresponding codes are listed.

These changes use existing days and replace equivalent practice.

### 3. Unit 1 readiness conflicts with this run’s explicit timing requirement

**Severity:** Moderate  
**LAYER:** sequence, process  
**REPEAT:** yes, the same conflict appears in the Grade 5 and Grade 8 independent sequence reviews.  
**Confidence:** Firm

**Location:** Prerequisite inventory, Unit 1 description, and day 1.

**What is wrong:** Older-grade readiness occurs in the final ten minutes of Unit 1’s first day, after its hook. This run expressly requires Unit 1 readiness in the start-of-year check before the unit opens.

There is an actual instruction conflict: repository `sequence-write.md`, rule 2, permits the after-hook exception. The draft follows that exception, but the supplied review brief takes precedence.

**Why it matters:** Readiness results cannot shape the opening lesson when collected after that lesson’s hook and work.

**Exact fix:** Move the existing display and distribution probes into an explicitly counted start-of-year check before Unit 1 opens. Preserve the hook as the unit’s opening and retain targeted display rebuilding afterward.

Reconcile the opening allocation, frame, calendar and shorter-path references together. The existing unassessed practice folds provide a way to pay for the allocation within 160 meetings, but a fold used in the canonical opening must not also count toward ten further reductions in the shorter year.

### 4. Square-root retrieval is scheduled after earlier work already needs it

**Severity:** Moderate  
**LAYER:** sequence, progression  
**REPEAT:** yes, retrieval after first relevant use appears in the Grade 3 and Grade 5 independent sequence reviews.  
**Confidence:** Firm

**Location:** Prerequisite inventory; days 10, 26, 126 and 131.

**What is wrong:** The inventory first retrieves `m8-roots` on day 131. Earlier work already needs it:

- Day 10 builds standard deviation from squared distances. Completing that calculation requires a square root.
- Day 26 explicitly includes a squared-quantity formula and relevant contextual branches.
- Day 126 sketches intercepts from vertex form.

Grade 8 day 142 explicitly teaches square equations and distinguishes their two solutions from a positive length. This is year-before retrieval, not older-grade readiness.

**Why it matters:** The plan supplies its named prerequisite support much later than the first tasks that require it. The distinction between a principal square root and two equation solutions matters here. The [Algebra Progression, PDF page 13](https://mathematicalmusings.org/wp-content/uploads/2013/07/ccss_progression_algebra_2013_07_03.pdf) specifically cautions about this distinction.

**Exact fix:** Name a brief square-root retrieval in day 10’s existing opening, using a small perfect-square example. On day 26, retrieve the two-solution distinction before rearranging the squared formula and then apply the context’s restrictions.

Update the inventory to identify day 10 as the first relevant use. Retain later retrieval, labelled as another return. Add the prerequisite to the relevant progression assumptions where the squared calculation is required.

### 5. The prerequisite register and frame retain obsolete directions

**Severity:** Minor  
**LAYER:** frame, process  
**REPEAT:** yes, stale prerequisite registers and superseded frame directions appear in earlier mathematics sequence reviews.  
**Confidence:** Firm

**Location:** Scope and sequence, prerequisite introduction and “For the lead”; frame, readiness bullet, Units 2 and 7, source map and shorter-calendar note.

**What is wrong:** Grade 7 and Grade 8 day maps are present, each with 160 rows. The draft still calls them unavailable and leaves their prerequisite treatment provisional.

The frame also continues to prescribe readiness on Grade 8 equations, systems and roots, although the sequence correctly treats them as retrieval. Its source-map wording implies next-unit readiness occupies every respond day, while only days 17 and 83 need those older-grade checks. Its statement that no shorter-calendar proposal exists is superseded by this sequence’s ten named folds.

**Why it matters:** A unit writer can follow either current file and receive different assessment and pacing instructions.

**Exact fix:**

- Replace the unavailable-map statements with verified day references.
- Keep histograms’ older history distinct from the later dot-plot and box-plot use; do not advance every display component merely because a row id appears.
- Replace the frame’s Grade 8 readiness directions with retrieval, preserving readiness on Grade 7 inequalities and percent.
- Make readiness conditional on the next unit’s actual older prerequisites.
- Point the frame to the sequence’s counted shorter path.
- Reconcile the Unit 1 wording with finding 3.

The absent high school rubric, course-id mapping and eventual tools file remain genuine process items. They are not newly discovered curriculum defects.

## Sequence, load and assessment audit

### Order and days by load

“Teaching meetings” includes modeling days and the teaching portion of embedded mid-unit days.

| Unit | Total days | Teaching meetings | Load judgment |
|---|---:|---:|---|
| 1. One-variable statistics | 17 | 15 | Defensible: 14 base meetings after the spreadsheet merge, plus modeling |
| 2. Linear algebra | 29 | 27 | Defensible: six rows, several solution methods, proof and constraints |
| 3. Two-variable statistics | 13 | 11 | Compact but coherent: tables, fitting, residuals, correlation, causation |
| 4. Functions | 21 | 19 | Defensible: notation, rates, domains, piecewise work and linear inverses |
| 5. Exponentials | 24 | 22 | Defensible despite only three rows: 21 base lessons carry substantial started work |
| 6. Quadratic functions | 20 | 18 | Defensible: patterns, expansion, forms, graphing and the growth comparison |
| 7. Quadratic equations | 27 | 25 | Defensible: factoring, square completion, formula, number arguments and interpretation |

No unit is demonstrably far over or under its load. Days 34, 114 and 144 remain tight implementation budgets, already acknowledged in the draft.

The important dependencies hold: linear algebra precedes fitted lines; function language precedes exponentials; quadratics precede the completed higher-power growth comparison; area expansion precedes factoring; square completion precedes the formula derivation.

### Standards and assessments

The 36 owned code entries have identifiable teaching placements. The material evidence corrections are findings 1 and 2.

| Unit | Coverage judgment |
|---|---|
| 1 | All three displays are taught; the closing construction evidence needs finding 2 |
| 2 | Letter coefficients, inequalities, formula rearrangement, solution sets, reversible elimination and viable regions are named |
| 3 | Frequency denominators, residuals, individual coefficient computation and causation are named; productive evidence needs finding 2 |
| 4 | Definition, notation, domains, interval rates and the frame’s linear-inverse boundary are carried |
| 5 | `F-LE.A.1a`, `1b` and `1c` are explicit; `F-LE.A.3` finishes in Unit 6 as previously settled |
| 6 | Hand graphing and the completed growth comparison have named assessment evidence |
| 7 | Derivation, number arguments, zeros, symmetry, extrema and different-representation comparisons are explicit |

The later-course completion of started standards is acknowledged. This read does not reopen the settled nonlinear-inverse, complex-solution or function-family handoffs.

Units 2 and 7 have mid-unit assessments. Response occupies the next two openings once. Each end-of-unit assessment has one respond day, and each two-part course check has one respond day. No duplicated response allocation was found.

### Readiness and retrieval

The present Grade 7 and Grade 8 daily records support the principal classifications:

| Prerequisite group | Last-use evidence | Treatment here |
|---|---|---|
| Older one-variable displays and population comparisons | Grade 6 histogram work; Grade 7 distribution and sampling work | Readiness remains appropriate; Unit 1 placement needs finding 3 |
| `m7-two-step-inequalities` | Grade 7 teaching and assessments | Day 17 readiness is correctly placed |
| `m7-percent-problems` | Grade 7 teaching and assessments | Day 83 readiness is correctly placed |
| Grade 8 equations, slopes, proportional comparisons and systems | Grade 8 linear units | Retrieval is appropriate |
| Grade 8 tables, scatter plots and fitted models | Grade 8 data unit | Retrieval on days 47 and 50 is appropriate |
| Grade 8 function rows and integer exponents | Grade 8 function and exponent units | Retrieval is appropriate |
| Grade 8 transformations, roots and irrational numbers | Grade 8 geometry and number work | Retrieval is appropriate; roots need the earlier placement in finding 4 |

No later unit incorrectly administers readiness on year-before work. No older prerequisite is incorrectly assigned retrieval in the daily plan. The two later readiness checks occur immediately before their units, not weeks ahead.

## Checks, calendar and shorter path

The course-level checks explicitly draw recently closed skills from earlier-unit content. Their planned task forms differ from the preceding assessment forms, and recent individual records are reused explicitly.

The check windows match the calendar:

- Days 60 and 61, weeks 12 and 13; response day 62.
- Days 108 and 109, week 22; response day 110.
- Days 158 and 159, week 32; response day 160.

Same-year timing is sound. Biology’s population unit, days 58 to 75, precedes the exponential callback on day 104. ELA argument evaluation, days 100 to 116, follows mathematics’ causation work, so day 55 correctly carries its own bridge. Early Biology displays are covered by Biology’s own worked example.

All seven Candidate cells are settled, with zero-day planning checks retained and separate extensions dropped with reasons.

The shorter path supplies both a 40-minute budget and ten distinct practice folds. No assessed or response day is removed. Its final viability remains an item-writing question, particularly on embedded mid-unit and technology-rotation days. Finding 3 requires corresponding opening-calendar adjustments.

## Source map

The map accounts for:

- 132 main-course lessons: 129 keep entries and three merge entries.
- Nine modeling prompts: seven kept, one merged introduction and one justified cut.
- 128 optional supports lessons, explicitly outside the core calendar.
- Original assessment and response allocations.

Main-course lesson order is preserved. Moving modeling prompts to the unit closing days has a stated instructional reason. The spreadsheet merge and vacation-prompt cut are explained. No unplaced main lesson or unexplained order reversal was found.

## Lens checklist

| Scope and sequence line | Result |
|---|---|
| No standard taught only in part without a later completion | **Met with qualifications:** later completions are named; finding 2 strengthens the assessment reservations |
| Problems intentionally join units | **Met:** fitted lines use earlier algebra; growth comparisons and course checks connect units |
| Fluency receives spaced, mixed practice | **Met in practice scheduling; missed in year-end reservation:** finding 1 |

All eight practices have named tasks. Their implementation and scoring belong to unit planning.

The high school focus rule is majority time within each course, as stated on printed page 7 of the [High School Publishers’ Criteria](https://achievethecore.org/content/upload/Math_Publishers_Criteria_HS_Spring_2013_FINAL.pdf). The K to 8 percentage threshold should not be imported. Day-code overlap alone does not establish time spent.

## What is right and should remain

Preserve the seven-unit order, anonymous or supplied data, the explicit individual technology computation, reversible elimination reasoning, both real solution signs, the nonzero qualifier in number arguments, and the spread of extended performances across closing days.

The [federal algebra practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/20) supports keeping solved-example analysis, attention to structure and deliberate strategy choice. It does not validate these particular minute budgets.

## Settled by the expert

These are recommendations for the caller to apply.

| Choice | Reason | Files affected |
|---|---|---|
| Add direct linear solving to the year-end check | Supplies the named fluency evidence | Scope and sequence; days 158 and 159 |
| Retain explicit statistical construction records | Makes claimed performances reviewable | Days 14, 16, 50, 56 and 58 |
| Retrieve roots on day 10 and revisit both solutions on day 26 | Support precedes the first relevant uses | Prerequisite inventory; daily notes; relevant progression assumptions |
| Preserve older-row readiness and Grade 8 retrieval classifications | Present day maps support them | Inventory and frame |
| Use the supplied brief’s pre-unit readiness timing | Resolves this run’s instruction conflict | Opening allocation, frame, calendar and shorter-path references |
| Retain the existing unit order and main lesson mapping | Dependencies and load are defensible | Frame and source map |

## For Cory

- No new scope, money, people or audience decision is required by these findings.

## Limits and sources

This read judges planning reservations, not finished assessment items, scoring quality or classroom duration. Those materials remain unwritten.

Sources opened or inspected:

- [CCSS Mathematics](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf): exact content expectations.
- [High School Publishers’ Criteria](https://achievethecore.org/content/upload/Math_Publishers_Criteria_HS_Spring_2013_FINAL.pdf): focus, coherence, rigor and applicable prerequisite content.
- [High School Review Criteria v2.0](https://cdn.edreports.org/media/2025/07/Math-HS-Review-Criteria_2.0.pdf): assessment coverage and high school review expectations.
- [Algebra Progression, 2013 draft](https://mathematicalmusings.org/wp-content/uploads/2013/07/ccss_progression_algebra_2013_07_03.pdf): equation reasoning and square-root distinctions.
- [Functions Progression, 2013 draft](https://mathematicalmusings.org/wp-content/uploads/2013/07/ccss_progression_functions_2013_07_02.pdf): function meaning, representations and interval rates.
- [Statistics Progression, 2012 draft](https://mathematicalmusings.org/wp-content/uploads/2012/06/ccss_progression_sp_hs_2012_04_21_bis.pdf): distribution summaries and fitted-model interpretation.
- [Base-text scope and sequence](https://im.kendallhunt.com/HS/teachers/1/scope_and_sequence.html) and [course narrative](https://im.kendallhunt.com/HS/teachers/1/narrative.html): sequence dependencies and instructional arcs.
- [Fishtank Algebra I pacing](https://www.fishtanklearning.org/curriculum/math/algebra-1/pacing-guide/): comparison of period assumptions and calendar flexibility.
- [Eureka high school overview](https://greatminds.org/hubfs/knowledge/resources/math/EM_Basic_Curriculum_Files/Curriculum_Overview/EM_G912_CurriculumOverview.pdf): reference-only sequence comparison.
- [WWC algebra practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/20): reasoning, structure and strategy choice.

The combined 2023 Progressions file exceeded the web reader’s size limit. Relevant older drafts were successfully opened through the alternate links above; their excerpts were read, not the complete documents.

## For the source list

Record the working alternate Progressions addresses above. The high school Publishers’ Criteria and current review-criteria PDF were reachable in this run.

**Verdict:** Coherent sequence, five targeted corrections required before unit planning.  
**Finding count:** 5.  
**Report path:** `docs/reviews/sequence-algebra-i-2026-11-15.md`, supplied here only.


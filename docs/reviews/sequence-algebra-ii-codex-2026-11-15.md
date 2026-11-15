# Algebra II scope and sequence: independent cold read

**Report path:** `docs/reviews/sequence-algebra-ii-2026-11-15.md`  
**Delivery:** Complete report supplied here. No files changed.

## Verdict

The seven-unit sequence is coherent and its main mathematical dependencies are sound. It needs correction before unit planning because several assessment claims exceed the named student performances, and the prerequisite ledger uses outdated evidence. Preserve the course order while repairing those reservations and reconciling the opening readiness allocation.

## What I read

- `docs/agents/EXPERT.md`, the mathematics lens, `docs/RUBRIC-MATH-K8.md`, the foundation, shared and mathematics approaches, source register, glossary, relevant ROADMAP sections and BASELINE rules 20 to 24.
- The complete Algebra II scope and sequence, frame, 160 daily rows and 161 source-map rows.
- All 26 grade 11 mathematics progression rows, relevant prerequisite rows and their standard text, including parent-code subparts.
- The calendar policy and grade 11 calendar records.
- Relevant Algebra I and Geometry daily records to verify last use.
- The earlier Algebra II frame reviews and independent Algebra I sequence review, for repeat classification.
- The outside sources linked below, including three curriculum sequence comparisons.

The requested K to 8 rubric contains no high school notes. I therefore checked the applicable high school criteria directly. I respected the blind-file exclusions.

## Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Algebra II reported zero failures; the wider run later stopped because `markdown` is missing. |
| `python -X utf8 scripts/frame.py calendar` | Completed without a reported stagger-rule break. |
| `python -X utf8 scripts/frame.py check algebra-ii` | Passed: seven units, 151 unit days and nine course-level check and respond days. |
| `python -X utf8 scripts/stale.py check` | Passed: 56 files, zero failures. |
| `python -X utf8 scripts/plan.py check algebra-ii` | Passed with four coverage notes. |

The four notes do not establish missing content: A-REI.A.2 appears on day 38, A-CED.A.1 on days 88 and 94, F-IF.C.9 on day 130, and S-ID.A.1 on day 141.

## Findings, most serious first

### 1. Several assessment reservations claim more than their named performances demonstrate

**Severity:** Serious  
**LAYER:** sequence, standard  
**REPEAT:** yes, the same evidence-reservation problem appears in the independent Algebra I sequence review, finding 2.  
**Confidence:** firm

**Location:** Days 68, 107, 133, 134 and 155; the corresponding unit assessment descriptions.

The unit-level coverage descriptions are stronger than several individual assessment rows. This matters because the brief requires each assessed day to support every part of each code it lists.

| Day | Claimed evidence | What remains unsupported by the named task |
|---|---|---|
| 68 | F-BF.B.4a through inverse verification | Checking supplied inverses does not necessarily require students to solve for the input and write the inverse themselves. |
| 107 | Parent F-BF.A.1 through selecting and fitting a model | The task does not name arithmetic combination of function types, part b. That performance is appropriately reserved for day 108. |
| 133 and 134 | F-IF.B.4 through daylight and tide models | Neither row reserves the complete graph/table interpretation and verbal-description sketching evidence claimed by that code. Day 135 does. |
| 155 | S-IC.A.1 and S-IC.B.3 through designing a randomized experiment | Random assignment alone does not establish population inference from random sampling or comparison among surveys, experiments and observational studies. |

These distinctions follow the [standards](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf), the [Functions Progression, PDF page 13](https://mathematicalmusings.org/wp-content/uploads/2013/07/ccss_progression_functions_2013_07_02.pdf), and the [Statistics Progression, PDF pages 11 to 12](https://mathematicalmusings.org/wp-content/uploads/2012/06/ccss_progression_sp_hs_2012_04_21_bis.pdf).

**Why it matters:** A writer could deliver the named tasks faithfully and still record evidence for performances students never produced.

**Exact fix:**

- Replace day 68’s verification-only reservation with two short solve-and-write inverse responses, using the scaled-cube and rational cases already taught on day 57.
- Replace parent F-BF.A.1 on day 107 with F-BF.A.1a if students explicitly write the selected contextual rule. Keep the parent and part b on day 108.
- Keep F-TF.B.5 on days 133 and 134. Remove their full F-IF.B.4 assessment claims and explicitly score that complete evidence on day 135.
- Keep the experimental analysis claim on day 155. Move its population-sampling and three-study-type assessment claims to explicitly named short responses on day 156.
- Make the prose distinguish evidence collected on each day from coverage accumulated across the assessment window.

These repairs fit the existing assessment windows.

### 2. The last-use ledger misclassifies recent prerequisites and does not justify integer-exponent retrieval

**Severity:** Moderate  
**LAYER:** sequence, progression  
**REPEAT:** yes, obsolete prerequisite evidence appears in the independent Algebra I sequence review, finding 5.  
**Confidence:** firm for the Geometry corrections; likely for the missing integer-exponent readiness reservation.

**Location:** Scope and sequence lines 9 to 42 and 159; days 1, 45, 46 and 95.

Geometry’s day map exists. It supplies explicit evidence that changes these classifications:

| Prerequisite | Grade 10 evidence | Current Algebra II treatment | Required treatment |
|---|---|---|---|
| `alg1-function-notation` | Geometry days 86 and 106 | Unit 1 readiness | Retrieval |
| `alg1-inverse-functions` | Geometry day 86 | Day 45 readiness | Retrieval before the nonlinear inverse work |
| `alg1-completing-square` | Geometry days 110 and 111 | Day 45 readiness | Retrieval before complex quadratics |
| `alg1-piecewise-absolute-value` | Geometry day 99, with assessment on day 101 | Day 95 readiness | Retrieval before transformations |

The six Geometry-owned handoffs also have actual daily placements: scaling on days 84 to 99, coordinate transformations on days 106 to 123, radians on days 134 to 140, triangle ratios on days 68 to 79, circle equations on days 109 to 123, and sample spaces on days 144 to 155. Their retrieval classification is supported and need not remain provisional.

The integer-exponent exception has the opposite problem. Its ledger cites Algebra I days 86 to 88, which concern exponential rules and representations, rather than explicitly teaching the stated exponent laws. Even a verified grade 9 use would remain two grades before grade 11. No named intervening use establishes the zero, negative and combined-exponent properties before day 46.

**Why it matters:** Readiness time is spent checking recently used work while a foundation for extending exponent laws lacks the required documented check.

**Exact fix:**

- Replace the unavailable-Geometry statements with the verified references above.
- Remove the four recent rows from readiness and place short retrieval tasks immediately before their relevant uses.
- Add a compact integer-exponent probe to day 45, covering zero, negative and combined exponents, unless a qualifying grade 10 or earlier grade 11 use is documented.
- Update the shorter-path instruction that relies on day 45’s readiness record.
- Preserve component-specific caution: Geometry’s area-model return does not establish that every quadratic graph feature was recently used.

### 3. Unit 1 readiness violates this run’s explicit placement requirement

**Severity:** Moderate  
**LAYER:** sequence, process  
**REPEAT:** yes, the independent Algebra I sequence review, finding 3, identifies the same instruction conflict.  
**Confidence:** firm

**Location:** Scope and sequence lines 13 to 15, 44, 50 and 136; day 1; frame readiness directions.

The plan puts older-skill readiness in the final ten minutes of Unit 1’s first day. This run expressly requires Unit 1 readiness in a start-of-year check before the unit opens.

The repository’s `sequence-write.md` rule 2 permits the after-hook exception. The draft follows that repository exception, but the supplied review instruction takes precedence for this run.

**Why it matters:** The results arrive after the opening work they are supposed to inform.

**Exact fix:** Put the remaining older growth-pattern prerequisites into an explicitly counted start-of-year check before Unit 1 opens. Retrieve function notation within the unit, following finding 2. Reconcile the opening allocation, frame, calendar, source map and shorter path together.

An existing unassessed practice fold can pay for that allocation within 160 meetings. A fold used in the canonical route cannot also count toward the shorter route’s ten additional reductions.

### 4. The promised high school focus calculation is still absent

**Severity:** Moderate  
**LAYER:** frame, sequence, process  
**REPEAT:** yes, the earlier independent Algebra II frame review, finding 2, explicitly assigned this calculation to the sequence layer.  
**Confidence:** firm

**Location:** Frame “Focus, coherence and rigor”; scope and sequence “Calendar, leans and teaching load” and “For the lead,” item 2.

The frame says the scope and sequence counts actual Curio Class days. The sequence provides no such count and returns the issue to the frame layer. Its daily codes establish placements, but overlapping code lists do not establish instructional time.

The applicable criterion is a majority of time within each course on widely applicable prerequisites. The published table includes F-BF.1, F-LE.1 and S-IC.1 alongside the other named content. Neither counting all F-BF and F-LE content nor applying the K to 8 percentage is the correct substitute. [High School Publishers’ Criteria, printed pages 7 to 8](https://achievethecore.org/content/upload/Math_Publishers_Criteria_HS_Spring_2013_FINAL.pdf), [High School Review Criteria, indicator 1b.i](https://cdn.edreports.org/media/2025/07/Math-HS-Review-Criteria_2.0.pdf).

**Why it matters:** The present figures cannot establish the course’s actual emphasis or guide justified pacing changes.

**Exact fix:** Add a planned-time calculation using the published prerequisite table. Classify the substantive work within mixed days, include relevant portions of added development days, and state the denominator and treatment of assessment and response time. Keep base-lesson overlap percentages labelled as descriptive counts.

Do not change unit allocations merely to improve an unsupported percentage. The absent local high school rubric does not prevent using the reachable published criterion.

### 5. Current planning files retain conflicting implementation directions

**Severity:** Minor  
**LAYER:** frame, sequence, process  
**REPEAT:** yes, conflicting current-file instructions recur in the independent Algebra I sequence review, finding 5.  
**Confidence:** firm

**Location:** Frame readiness paragraphs, unit rows and source map; days 32 and 33.

Three conflicts remain despite the stale checker passing:

- The frame repeatedly prescribes readiness for rows the sequence correctly treats as same-year retrieval, and it will need the additional corrections in finding 2.
- The frame’s Unit 7 and source map retain opt-in pulse collection. The sequence and day 154 require supplied outcomes without pulse collection.
- Days 32 and 33 name a five-minute response opening and also retain a five-minute retrieval opening. The prose says response replaces retrieval.

**Why it matters:** Writers receive different instructions depending on which current file they follow. The duplicate opening also undermines the stated period budget.

**Exact fix:** Reconcile the frame to the corrected prerequisite ledger and supplied-data decision. In days 32 and 33, replace the appended retrieval sentence with an explicit statement that the five-minute response replaces that day’s usual retrieval. Preserve historical reports as history.

## Sequence, standards and load audit

All 26 owned progression rows and 51 owned code entries have identifiable placements. I found no reason to reorder the seven units.

| Unit | Days | Base lessons | Load judgment |
|---|---:|---:|---|
| 1. Sequences and functions | 14 | 11 | Appropriate introduction; opening readiness needs finding 3 |
| 2. Polynomials and rational functions | 31 | 26 | Its seven rows justify the longest allocation |
| 3. Complex numbers and rational exponents | 24 | 19 | Separate rewriting and inverse work have clear purposes |
| 4. Exponential functions and equations | 23 | 18 | Rational inputs, logarithms and expression interpretation justify the load |
| 5. Transformations of functions | 14 | 11 | Compact, with substantial earlier function knowledge available |
| 6. Trigonometric functions | 24 | 19 | Measured arcs, graph construction and modeling justify the allocation |
| 7. Statistical inferences | 21 | 16 | Sampling reconstruction and visible simulation processes justify the added days |

No run is demonstrably far over or under its teaching load. Assessment density remains an implementation risk: day 44 lists 12 codes, day 94 lists 15 including parents and subparts, and day 158 lists 17. Those counts are not independent item counts, but actual tasks must demonstrate that the combined demands fit.

The important dependencies hold:

- Polynomial arithmetic and division precede rational rewriting.
- Equation reasoning precedes nonlinear inverses.
- Rational exponents precede fractional-interval exponential growth.
- Transformations precede transformed periodic models.
- Sampling reconstruction and hand simulation precede simulated margins and treatment comparisons.

The lettered parts of A-SSE.A.1, A-SSE.B.3 and F-IF.C.8 receive explicit placements. Signed transformations, algebraic symmetry, tangent’s domain and asymptotes, negative radian inputs and simulation-based inference are explicitly carried. Finding 1 concerns the assessment evidence claimed for these placements, rather than a missing unit.

Unit 2’s midpoint assessment follows the Remainder Theorem discussion. Its response occupies the next two openings once. End-of-unit and course-level response days are otherwise counted once.

## Readiness, checks and calendar

Beyond finding 2, the principal classifications are defensible. The older statistical rows and grade 7 random sampling receive readiness before Unit 7; sample spaces are correctly distinguished from sampling inference. Same-year factoring, quadratic reasoning and exponential work receive retrieval.

Later readiness slots fall immediately before their units on days 14, 45, 72, 95 and 136. None is weeks ahead of its unit opening.

The course-level checks explicitly transfer recently assessed skills into earlier-unit content:

| Check | Assessment days | Respond day | Calendar judgment |
|---|---|---|---|
| 1 | 70 and 71 | 72 | Matches weeks 14 to 15 |
| 2 | 110 and 111 | 112 | Matches weeks 22 to 23 |
| 3 | 158 and 159 | 160 | Matches week 32 |

The planned forms distinguish audits and recommendations from the preceding direct-solving, model-building and experimental-design performances. The year-end reservation directly samples all four named fluency standards and includes F-IF.C.9. The settled F-IF.C.7d exception is preserved.

Physics waves occupy days 77 to 92, before the periodic callback on day 129. That day also carries its own frequency bridge. Chemistry half-life and grade 10 ELA evidence evaluation are prior-year returns. The Economics and Government contingency bridges are stated.

## Candidates, shorter path and source map

Every Candidate cell has a disposition. The seven progression comparisons remain planning checks at zero student-day cost. Retained extensions have bounded time inside existing days; dropped extensions have reasons.

The shorter path names both a 40-minute period structure and ten fold-in days: **4, 6, 29, 46, 52, 62, 64, 83, 87 and 145**. None is an assessed or respond day. The stated mathematical work is preserved in named neighbors. Findings 2 and 3 require corresponding readiness and counting updates.

The source map contains:

- 120 individual base lessons, all retained in their original order.
- Eight modeling-prompt entries, including the introductory prompt merged into day 12.
- 33 original development, assessment, response and course-level entries.

No base lesson is unplaced or cut. No unexplained main-lesson order reversal was found.

## Lens checklist

| Scope and sequence checklist line | Result |
|---|---|
| No standard taught only in part without later completion | **Met for teaching placement; missed in several assessment reservations**, finding 1 |
| Problems intentionally join units | **Met:** series, inverses, transformed models and cumulative transfers connect units |
| Fluency receives spaced, mixed practice | **Met:** rotating openings and direct year-end sampling are named |

All eight mathematical practices have identifiable tasks. Their scoring quality cannot be certified before the items and rubrics exist.

## What is right and should remain

Preserve the unit order, finite-series derivation, nonlinear-inverse contribution, original-domain treatment of rational functions, explicit algebraic symmetry, tangent qualifications, sampling reconstruction and supplied-data choices.

The sequence follows the [base-text narrative’s dependency chain](https://im.kendallhunt.com/HS/teachers/3/narrative.html). The [federal algebra practice guide](https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/WWC_Algebra_PG_Revised_02022018.pdf) also supports retaining worked-solution analysis, attention to structure and deliberate strategy choice. It does not validate these particular minute budgets.

## Settled by the expert

These are recommendations for the caller to apply.

| Choice | Reason | Files affected |
|---|---|---|
| Require solve-and-write inverse responses | Matches the contribution being claimed | Scope and sequence; day 68 |
| Narrow assessment codes to named evidence | Preserves complete unit coverage without inflated daily claims | Days 107, 133, 134, 155 and 156 |
| Use verified Geometry last-use evidence | Recent use requires retrieval | Prerequisite ledger; affected daily notes; frame |
| Reserve integer-exponent readiness unless qualifying later use is documented | The present citation does not establish recent use | Days 45 and 46; shorter path |
| Apply this run’s pre-unit opening requirement | Resolves the explicit instruction conflict | Opening allocation, frame, calendar and source map |
| Use the published high school focus table | Supplies the applicable criterion | Frame and scope and sequence |
| Keep supplied outcomes and replace duplicate openings | Makes current directions consistent | Frame; days 32 and 33 |
| Retain the seven-unit mathematical order | Dependencies and teaching loads are defensible | Frame and source map |

## For Cory

- No new scope, money, people or audience decision is required. These repairs preserve the existing content and can be reconciled within the 160-meeting course.

## Limits and outside sources

This review judges planning commitments. Finished items, answer keys, scoring rubrics and classroom timings were unavailable, so assessment duration and support quality remain unverified. No substantive judgment rests on unverified model memory.

Sources inspected:

- [CCSS Mathematics](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf): exact content expectations.
- [High School Publishers’ Criteria](https://achievethecore.org/content/upload/Math_Publishers_Criteria_HS_Spring_2013_FINAL.pdf): per-course focus and prerequisite table.
- [High School Review Criteria v2.0](https://cdn.edreports.org/media/2025/07/Math-HS-Review-Criteria_2.0.pdf): full intent, assessment evidence and high school review expectations.
- [Functions Progression](https://mathematicalmusings.org/wp-content/uploads/2013/07/ccss_progression_functions_2013_07_02.pdf): inverse construction and function representations.
- [Algebra Progression](https://mathematicalmusings.org/wp-content/uploads/2013/07/ccss_progression_algebra_2013_07_03.pdf): equation reasoning and representation structure.
- [Statistics Progression](https://mathematicalmusings.org/wp-content/uploads/2012/06/ccss_progression_sp_hs_2012_04_21_bis.pdf): sampling, assignment and inference distinctions.
- [Base-text narrative](https://im.kendallhunt.com/HS/teachers/3/narrative.html), [scope and sequence](https://im.kendallhunt.com/HS/teachers/3/scope_and_sequence.html), and [model-fitting lesson](https://im.kendallhunt.com/HS/teachers/3/5/11/preparation.html): sequence and task intent.
- [Fishtank Algebra 2](https://www.fishtanklearning.org/curriculum/math/algebra-2/): comparison sequence, with its additional advanced content treated as reference.
- [New York high school curriculum overview](https://www.nysedregents.org/engageny/a-story-of-functions-curriculum-map-and-overview.pdf): another comparison sequence, read as reference only.
- [Federal algebra practice guide](https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/WWC_Algebra_PG_Revised_02022018.pdf): reasoning, structure and strategy selection.

The linked Progressions readings were relevant excerpts from the older drafts, not a complete reread of the compiled 2023 edition.

**Verdict:** Coherent sequence, corrections required before unit planning.  
**Finding count:** 5.  
**Report path:** `docs/reviews/sequence-algebra-ii-2026-11-15.md`, supplied here only.
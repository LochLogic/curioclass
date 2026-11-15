# Geometry scope and sequence: independent first read

**Date:** 2026-11-15  
**Intended report path:** `docs/reviews/sequence-geometry-2026-11-15.md`  
**Delivery:** Report supplied here only. No files created, edited or deleted.

## Verdict

The sequence has a sound mathematical order, but needs targeted revision before unit planning. Its largest risk is that several claims of complete assessment coverage lack a named student performance, while cylinder work is treated as renewing a broader prerequisite row. Repair those reservations and readiness distinctions, preserving the eight-unit order, staged proof development and existing day totals.

## What I read

- `docs/agents/EXPERT.md`, the mathematics lens, `docs/RUBRIC-MATH-K8.md`, and relevant foundation, approach, source-register, glossary, ROADMAP and BASELINE guidance.
- The complete Geometry scope and sequence, all 160 `days.csv` rows, the frame and all source-map entries.
- All 28 grade 10 mathematics progression rows, their prerequisite rows, relevant Algebra II receiving rows, and the applicable standard text.
- `docs/courses/CALENDAR.md` and grade 10 rows in `data/plans/calendar.csv`.
- Relevant prerequisite evidence in the grade 7, grade 8 and Algebra I day maps.
- Earlier Geometry frame reviews and relevant Algebra I and grade 8 sequence findings, within the supplied blind boundary.
- The outside sources linked below.

The named rubric contains no substantive high school supplement. I therefore consulted the high school criteria directly.

**Gate limitation:** `plan.py check` reported zero Geometry failures, then stopped elsewhere because `markdown` is unavailable; `frame.py calendar` passed, `frame.py check geometry` passed with zero failures, and `stale.py check` reported zero failures across 56 files.

The two Geometry code notes concern comma-suffixed codes in the frame. Valid `A-CED.A.2` and `A-CED.A.4` appear on days 99 and 114.

## Findings, most serious first

### 1. Three assessment reservations need explicit evidence for the claimed standard

**Severity:** Serious  
**LAYER:** sequence, standard  
**REPEAT:** yes, productive actions and full assessment coverage recur in the grade 8 sequence review, finding 1  
**Confidence:** firm for the step-function and table-construction reservations; likely for the density reservation

**Locations:** Unit 5 evidence description; days 99 to 101 and 159.

| Reservation | What is missing or ambiguous | Exact fix |
|---|---|---|
| `F-IF.C.7b`, days 99 and 101 | The plan names square-root, cube-root, absolute-value and piecewise graphs, but never explicitly reserves a **step-function graph**. A general piecewise example need not be a step function. | Make the piecewise example on day 99 a step function, including endpoint conventions. Name its graph as retained evidence on day 101, including in the shorter-period route. |
| `S-CP.A.4`, day 159 | Auditing a supplied table and reconstructing one missing count do not establish that the student can **construct a two-way frequency table**. Day 156 reserves construction, but day 159 does not explicitly name that retained product. | Reuse each student's dated day 156 table-construction record for this part of `S-CP.A.4`. State this on day 159 and in the course-check description. Keep the new audit for interpretation, conditional probabilities and independence. |
| `G-MG.A.2`, days 100 and 101 | The container task promises density evidence, but does not explicitly require both **density by area and density by volume**. Mentioning fictional populations in a sensitivity note does not require a population-area calculation. | Retain a short independent population-area density response from day 98 alongside day 100's mass-volume density model. Name both products in day 101's reuse instruction. |

**Why it matters:** A writer can follow the named tasks, omit these performances and still claim complete coverage. A blanket instruction to cover every part does not identify the missing product.

The official [mathematics standards](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf) specify step functions, constructing two-way tables, and density based on area and volume. The fixes use existing work and avoid another recent table-construction task.

### 2. Cylinder work does not renew the whole curved-volume prerequisite

**Severity:** Serious  
**LAYER:** sequence, progression  
**REPEAT:** yes, prerequisite checks before first use were raised in the earlier Geometry frame review, finding 3; this is the remaining partial-row problem  
**Confidence:** likely

**Locations:** Prerequisite table, `m8-volume-curved`; Unit 5 evidence; days 26, 43 and 81.

**What is wrong:** The grade 8 row covers cylinder, cone and sphere formulas. Day 26 checks a cylinder, and day 43 explicitly teaches cylinder volume. The sequence then treats the row as current-year retrieval in Unit 5, although neither named event renews its cone and sphere parts.

The sequence correctly refuses to renew the whole plane-transformation row from one quadratic-graph application. The same distinction is needed here.

**Why it matters:** A student can succeed with cylinders and still enter the cone and sphere work without the promised diagnosis of older learning. The phrase “only cross sections remain an unused older row” on day 81 is consequently too broad, and already conflicts with its added circle check.

**Exact fix:**

- Keep cylinder volume as retrieval from day 43.
- Add brief cone and sphere formula/use prompts to day 81's existing readiness window, alongside cross sections and circle formulas.
- Name the targeted reminders before the cone work on day 94 and sphere application on day 96.
- Rewrite the prerequisite entry to distinguish the renewed cylinder component from the older cone and sphere components.

No standard ownership or unit length changes. The [Geometry Progression](https://mathematicalmusings.org/wp-content/uploads/2016/03/ccss_progression_g_7_hs_2016_03_27.pdf) distinguishes earlier formula use from the later arguments explaining formulas.

### 3. Unit 1 readiness violates this run's explicit opening rule

**Severity:** Moderate  
**LAYER:** sequence, process  
**REPEAT:** yes, grade 8 sequence review, finding 2, and Algebra I sequence review  
**Confidence:** firm

**Locations:** Prerequisite table; paragraph beginning “Day 1's check”; Unit 1 evidence; day 1.

**What is wrong:** The four older-row readiness tasks occupy the last ten minutes of Unit 1's first day. This run explicitly requires Unit 1 readiness in a start-of-year check before the unit opens.

There is a real instruction conflict: the repository glossary and sequence-writing brief permit the last-ten-minutes exception for Unit 1, and the gate accepts it. The sequence follows that exception, but fails the supplied review instruction.

**Why it matters:** The diagnostic cannot shape the opening lesson, and different writers receive incompatible directions.

**Exact fix:** Move the four tasks into a named start-of-year check before Unit 1 opens, preserve the resulting reminders, and remove day 1's readiness designation. Reconcile the repository exception with the governing instruction. Do not silently add a 161st meeting or change the frame's allocation.

### 4. The high school focus question remains unresolved despite accessible criteria

**Severity:** Moderate  
**LAYER:** frame, sequence, process  
**REPEAT:** yes, independent Geometry frame review, finding 4; carried forward as unresolved  
**Confidence:** firm

**Locations:** Frame, “Focus, coherence and rigor”; scope and sequence, “For the lead,” item 1.

**What is wrong:** The plan postpones the applicable prerequisite list and per-course interpretation until a local high school rubric exists. Those source questions can now be settled: the [High School Publishers' Criteria, printed pages 7 to 8](https://achievethecore.org/content/upload/Math_Publishers_Criteria_HS_Spring_2013_FINAL.pdf) apply the majority-of-time expectation to a single course and explicitly include `G-CO.A.1`, `G-CO.C.9` and `G-CO.C.10`.

The remaining uncertainty is the allocation of instructional time. Neither lesson-code overlap nor equal shares among listed codes measures it. A direct-code screen of the current CSV finds a listed prerequisite code on 50 of 135 teaching-kind days, but this excludes qualifying applications and connections, so it cannot establish a focus shortfall.

**Why it matters:** Unit writers lack a common accounting method and can inherit incompatible claims.

**Exact fix:** Record the source's per-course interpretation and complete prerequisite categories now. Add a time allocation by day or coherent block, counting qualifying applications, connections and mixed practice once. Report the resulting share with its method. Keep the verdict on focus open until that evidence exists.

This does not justify importing the K to 8 percentage threshold or resizing Geometry now.

### 5. The frame retains readiness directions that the sequence has superseded

**Severity:** Minor  
**LAYER:** frame, process  
**REPEAT:** yes, grade 8 sequence review, finding 4  
**Confidence:** firm

**Locations:** Frame readiness wording, Seams table, and Units 4, 5 and 7.

**What is wrong:** The frame still instructs readiness on Pythagorean work in Unit 4 and circle work in Unit 7, although the sequence explicitly teaches those prerequisites earlier in the same year. Its Unit 5 wording also calls for a full curved-volume check without distinguishing cylinder retrieval from the remaining older components.

**Why it matters:** A unit writer beginning from the frame can add unnecessary checks or follow a different prerequisite contract. The stale-text gate does not detect these substantive contradictions.

**Exact fix:** Update the operational frame directions:

- Unit 4 retrieves Unit 3's dilation and Pythagorean work.
- Unit 7 retrieves day 90's circumference and circle-area work.
- Unit 5 uses the component distinction in finding 2.
- The Seams table distinguishes the original incoming handoff from its treatment after current-year teaching.

Retain the historical grade-to-grade handoffs.

## Prerequisites checked

| Earlier row or group | Last documented earlier use | Treatment and judgment |
|---|---:|---|
| `m7-triangle-conditions` | Grade 7 | Older readiness is appropriate; opening placement needs finding 3. |
| `m8-rigid-motions`, `m8-transformations-coordinates`, `m8-angle-facts` | Grade 8 | Algebra I's narrower graph work does not renew these complete rows. Older readiness is appropriate. |
| `m8-congruence` | Grade 8 | Day 26 readiness before Unit 2 is appropriate. |
| `m8-volume-curved` | Grade 8 | Day 43 renews cylinders only; finding 2 addresses the remainder. |
| `m8-dilations-similarity` | Grade 8 | Day 48 readiness, then current-year retrieval in later units. |
| `m8-pythagorean-theorem` | Grade 8 | Day 48 readiness; day 62 explicitly teaches it before Unit 4 retrieval. |
| `m7-scale-drawings` | Grade 7 | Older readiness on day 48 is appropriate. |
| `m6-equivalent-ratios` | Grade 7 retrieval | Day 48 readiness remains appropriate after intervening grades. The inventory should say “retrieved,” rather than “explicitly taught again,” for grade 7 days 1, 13 and 34. |
| `m7-cross-sections`, `m7-circles` | Grade 7 | Day 81 readiness is appropriate; circle teaching on day 90 supports Unit 7 retrieval. |
| `m8-coordinate-distance` | Grade 8 | Day 105 readiness before Unit 6 is appropriate. |
| `m7-probability-models`, `m7-compound-events` | Grade 7 | Day 143 readiness and tree-diagram reactivation are appropriate. |
| Listed Algebra I rows and Biology contribution | Grade 9 | Retrieval is appropriate; the sequence does not incorrectly give these a readiness check. |

Apart from Unit 1, readiness is immediately before the receiving unit. The cylinder check precedes its application by 17 days and the Pythagorean check precedes explicit teaching by 14 days, but both meet the stated **pre-unit** placement rule. These gaps alone are not findings.

## Order, load and assessment structure

| Unit | Total days | Teaching-kind days | Judgment |
|---|---:|---:|---|
| 1. Constructions and rigid transformations | 26 | 24 | Construction constraints precede motion definitions and formal angle arguments. |
| 2. Congruence | 19 | 17 | Rigid-motion congruence precedes criteria and quadrilateral proofs. |
| 3. Similarity | 19 | 17 | Dilation properties precede AA, proportionality and the similarity-based Pythagorean proof. |
| 4. Right triangle trigonometry | 14 | 12 | Similarity explains ratios before their calculation and application. |
| 5. Solid geometry | 21 | 19 | Three spatial days, five scaling/root days and seven volume days reflect different loads. |
| 6. Coordinate geometry | 21 | 19 | Point rules precede conic equations, slope criteria, intersections and coordinate proof. |
| 7. Circles | 17 | 15 | Angle relationships and constructions precede radians and sector arguments. |
| 8. Conditional probability | 14 | 12 | Sample spaces and tables precede conditional denominators and independence. |

No run is demonstrably far over or under its teaching load. Units 5 and 6 have the greatest assessment density, but their retained products make the allocation plausible at this layer. Actual item timing remains untested.

Unit 1's day 14 mid-unit assessment is correctly placed, with response in days 15 and 16. Each unit and course-level check has response counted once.

The end-of-unit reservations otherwise carry the named theorem parts, including both perpendicular-bisector directions, the parallelogram converse, all four triangle theorems, both conditional-independence directions and both multiplication factorizations. Finding 1 identifies the remaining explicit evidence gaps.

## Calendar, source map, Candidates and shorter path

- **Calendar:** Checks on days 46 to 47, 103 to 104 and 158 to 159 match weeks 10, 21 and 32. Grade 10 has no additional stagger restriction before finals week.
- **Cross-subject timing:** Chemistry's earlier precision and conversion needs are correctly identified against days 17 to 31, 42 to 53 and 88 to 99. Geometry assumes no unfinished same-year incoming skill. The Chemistry bridges remain necessary.
- **Source map:** All 124 main lessons are placed once in base order. All eleven modeling prompts have decisions: eight keeps, one merge and two cuts with reasons. Later prompt placement is explained.
- **Candidates:** All eight units settle their Candidate cells with an existing day location or a reason for dropping them. No additional required day is hidden in an extension.
- **Shorter path:** Both a 40-minute period and ten named fold-in days are provided. Days 2, 8, 18, 22, 42, 50, 58, 60, 96 and 140 have destinations. None is a designated assessment, response day or retained assessment-window product. No required content is explicitly cut.

The [base course narrative](https://im.kendallhunt.com/HS/teachers/2/narrative.html) supports the retained proof progression. The [comparison pacing guide](https://www.fishtanklearning.org/curriculum/math/geometry/pacing-guide/) uses longer periods and calendar flexibility, so its day counts cannot validate this plan's minutes. A [second comparison sequence, PDF pages 24 to 26](https://greatminds.org/hubfs/knowledge/resources/math/EM_Basic_Curriculum_Files/Curriculum_Overview/EM_G912_CurriculumOverview.pdf#page=24), likewise supports the broad mathematical arc without requiring its calendar.

## Lens checklist

| Scope and sequence requirement | Result |
|---|---|
| Every owned standard completed beyond a partial introduction | Met in teaching reservations; assessment qualifications in finding 1. |
| Problems intentionally join units | Met through modeling, coordinate revisiting and earlier-content course checks. |
| Fluency receives spaced, mixed practice | Met through daily openings, weekly constructions and later congruence, similarity and coordinate rotations. |

All eight practices have named tasks. Understanding, procedural work and application are deliberately connected. The [federal learning guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/1) supports spacing and connecting representations, but does not validate these specific minute budgets.

## What should remain

Preserve the unit order, gradual proof development, explicit cross-unit theorem records, paper routes, fictional or supplied data, complete radian argument, and exclusion of `S-CP.B.8` from the year-end check. Preserve the distinction between new check forms and recently completed assessments.

## Settled by the expert

Recommendations for the caller to apply:

| Choice | Reason | Files affected |
|---|---|---|
| Use a step function as day 99's piecewise example and retain its graph | Makes the required subtype explicit without another graph family | Scope and sequence; days 99 and 101 |
| Name day 156's constructed table as reused evidence on day 159 | Preserves the productive action without repeating its recent task form | Course-check description; day 159 |
| Retain day 98 area-density evidence beside day 100 volume-density evidence | Covers both density bases | Unit 5 evidence; days 98 and 101 |
| Diagnose older cone and sphere work on day 81 | Cylinder work does not renew those components | Prerequisite table; days 81, 94 and 96 |
| Use the published per-course focus interpretation | Resolves the source question; time evidence still needs accounting | Frame and sequence focus notes |
| Replace superseded frame readiness directions with current-year retrieval | Gives unit writers one operational contract | Geometry frame |
| Describe grade 7 ratio entries as retrieval | Matches their actual day notes; readiness classification stays unchanged | Prerequisite inventory |

## For Cory

- Resolve the counted time for a start-of-year check before Unit 1. A separate meeting would change the fixed allocation; this report does not authorize an extra day.

## Limits and source notes

This read evaluates planning reservations, not finished items, keys, scoring or demonstrated classroom duration. The later sensitivity read remains necessary for the fictional screening context.

Additional sources consulted:

- [High school review criteria v2.0](https://cdn.edreports.org/media/2025/07/Math-HS-Review-Criteria_2.0.pdf): full standards intent, coherence, rigor and instructional-time evidence.
- [High School Statistics and Probability Progression](https://mathematicalmusings.org/wp-content/uploads/2012/06/ccss_progression_sp_hs_2012_04_21_bis.pdf): movement from earlier probability to conditional probability and independence.
- [Base-text scope and sequence](https://im.kendallhunt.com/HS/teachers/2/scope_and_sequence.html): dependency rationale, particularly similarity before trigonometry.

For the source list, retain the working Geometry Progression address above. The first attempted Geometry PDF address failed; the linked 2016 draft opened successfully. No curricular finding rests on memory; prior workflow memory informed scope handling only.

**Verdict:** Sound mathematical sequence; five targeted corrections required before unit planning.  
**Finding count:** 5.  
**Report path:** `docs/reviews/sequence-geometry-2026-11-15.md`, supplied here only and not saved.


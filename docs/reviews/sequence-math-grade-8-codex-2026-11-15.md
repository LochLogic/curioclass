# Independent scope and sequence review: Math Grade 8

**Date:** 2026-11-15  
**Intended report path:** `docs/reviews/sequence-math-grade-8-2026-11-15.md`  
**Delivery:** Complete report supplied here. No files created, edited or deleted.

## Verdict

The eight-unit sequence is mathematically sound overall and preserves a defensible progression from transformations through linear relationships to functions and later numerical work. Its main risk is that some assessment descriptions promise complete standards coverage without explicitly reserving the student actions those standards require. Make the four corrections below before unit planning, preserving the mathematical order and addressing the conflicting start-of-year readiness instructions explicitly.

## What I read and checked

- `docs/agents/EXPERT.md`, the mathematics lens, `RUBRIC-MATH-K8.md`, FOUNDATION, the shared and mathematics approaches, relevant APPROACH-SOURCES and ROADMAP sections, BASELINE rules 20 to 24, the glossary and sequence-writing rules.
- The complete Grade 8 scope and sequence, frame, `days.csv` and `source-map.csv`.
- All 24 Grade 8 progression rows, all directly assumed earlier mathematics rows, and relevant Grade 6 and Grade 7 day records.
- All 36 local Grade 8 standard codes, including lettered parts.
- `docs/courses/CALENDAR.md` and all Grade 8 rows in `data/plans/calendar.csv`.
- The stored base-lesson inventory and selected open lessons, including the equation-example and line-fitting tasks.
- Permitted earlier Grade 8 frame reports and the Grade 6 sequence report, for finding history and repeat classifications.
- The outside sources linked below.

The blind-rule exclusions were respected. Prior-run memory informed the review method and report structure only. No curricular conclusion rests on memory.

### Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Stopped before Grade 8 with `ModuleNotFoundError: No module named 'markdown'`; also reported an unrelated missing Algebra I sequence |
| `python -X utf8 scripts/frame.py calendar` | Completed; no stagger-rule breaks reported |
| `python -X utf8 scripts/frame.py check math-grade-8` | Passed: 0 failures, 153 unit days plus 7 course-level days |
| `python -X utf8 scripts/plan.py check math-grade-8` | Passed: 0 failures |
| `python -X utf8 scripts/stale.py check` | Passed: 56 files, 0 failures |

The Grade 8 plan check notes the frame token `8.F.A.3,` with its attached comma. The valid code is present in the day file. The incomplete global gate does not withhold this verdict.

## Findings, most serious first

### 1. Assessment reservations need the standards’ productive actions

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, incomplete standard performances were identified in the earlier Grade 8 frame read and Grade 6 sequence read  
**Confidence:** Likely

**Location:** Unit 4 assessment descriptions and days 62 and 68; unit 5 assessment descriptions and days 81 and 91.

**What is wrong:** Two required actions remain implicit behind the repeated promise that every listed code is checked in full:

- **8.SP.A.2:** Day 60 compares proposed fits; the assessment descriptions emphasize judging fit by closeness. They do not explicitly reserve a student’s own fitted line or name a retained line-fitting product.
- **8.EE.C.7a:** The descriptions reserve classifying solution counts and transforming equations. They do not explicitly ask students to give examples of equations with the three different solution counts.

These actions exist in retained base instruction. Base lesson 8.6.5 asks students to draw their own fitted lines, and base lesson 8.4.7 asks students to complete equations to produce specified solution behavior. The weakness is the assessment reservation, rather than an established absence from instruction. [Line-fitting lesson](https://im.kendallhunt.com/MS/teachers/3/6/5/index.html), [equation-example lesson](https://im.kendallhunt.com/MS/teachers/3/4/7/index.html).

**Why it matters:** A writer could implement the specified comparison and classification prompts, believe the code-level promise has been satisfied, and collect no evidence that students can produce the required objects. The standards explicitly require informal fitting and giving equation examples. [Statistics standard](https://www.thecorestandards.org/Math/Content/8/SP/), [equation standard](https://www.thecorestandards.org/Math/Content/8/EE/).

**Exact fix:**

1. Name an individual product on **day 61**: a student-drawn line fitted to supplied paired data, with a closeness justification. Explicitly retain it for days **62 and 68**.
2. On **day 79**, require students to construct an equation for each solution count and verify each through equivalent forms. Name that product in days **81 and 91**, alongside the existing solving prompts.
3. In course checks **116 and 159**, explicitly reserve a brief example-generation entry when listing 8.EE.C.7a.
4. Replace equivalent practice or classification items, keeping the existing assessment days and response allocations.

This is a reservation-level correction. Finished items and scoring still belong to unit planning.

### 2. Unit 1 readiness conflicts with this run’s explicit timing rule

**Severity:** Moderate  
**LAYER:** process  
**REPEAT:** new  
**Confidence:** Firm

**Location:** Earlier-row register; unit 1 prose; day 1; `source-map.csv` row `ours-1`.

**What is wrong:** The sequence puts symmetry and signed-coordinate readiness in the final ten minutes of **unit 1’s first day**. This run explicitly requires unit 1 readiness in the start-of-year check and says a unit’s first day stays clean for its hook and compelling question.

There is a genuine instruction conflict: the repository’s `sequence-write.md`, rule 2, expressly permits unit 1 readiness in the last ten minutes of day 1. The glossary repeats that exception, and the gate accepts it. The sequence follows that repository exception, but it does not satisfy the supplied review brief.

**Why it matters:** The check cannot shape the first unit’s opening when it occurs after that opening. More broadly, a writer receives incompatible directions from the review brief and repository guidance.

**Exact fix:** Under this run’s instruction, place the existing symmetry and signed-coordinate tasks in a **start-of-year check before unit 1 opens**, preserve the day 2 rebuilding, and remove readiness from unit 1’s opening day. Reconcile the repository exception with the governing decision so later writers receive one rule.

A fully specified placement depends on whether the start-of-year check occurs before the 160 meetings or occupies one of them. That changes the course-day allocation and belongs to Cory; it must not be silently resolved by adding time or reducing unit 1.

The prerequisite classifications themselves are appropriate: symmetry was last explicitly taught in Grade 4, and the complete signed-coordinate row in Grade 6.

### 3. Fold-in day 30 has response time without a destination

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, conflicting shorter-path time reservations appear in the Grade 6 sequence report  
**Confidence:** Firm

**Location:** “Shorter path,” fold-in day 30; `days.csv`, days 28 to 31.

**What is wrong:** Day 30 contains the second **five-minute response** to day 28’s mid-unit assessment. The fold-in table moves its corresponding-side-ratio work into days 28 and 31 but does not move that response.

The general instruction to keep response time does not identify its receiving day or displaced activity.

**Why it matters:** A teacher following the fold-in table can lose half the planned response allocation. Alternatively, the teacher must invent additional time on a receiving day.

**Exact fix:** Add this instruction to the day 30 fold:

> Keep day 29’s five-minute response. On the shortened-year path, move day 30’s five-minute response to the start of canonical day 31, replacing that day’s ordinary mixed-retrieval opening. Then connect the corresponding-side ratio to the slope triangles.

This preserves the full ten-minute response once, retains the mathematics, and adds no meeting. Update the blanket shorter-path statement to acknowledge that day 30 carries embedded response time.

The other nine named fold-ins do not carry assessment flags or explicitly retained assessment products.

### 4. The prerequisite register and frame retain obsolete directions

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, the same stale prerequisite-file status and conflicting frame readiness directions appear in the Grade 6 sequence report  
**Confidence:** Firm

**Location:** Scope and sequence lines 11 to 35 and lead item 1; frame Readiness bullet, units 1, 7 and 8, and source-map allowances.

**What is wrong:** The sequence says the Grade 7 day file does not exist and leaves all Grade 7 last-use entries provisional. That file now exists. All **18 directly assumed Grade 7 mathematics rows** have teaching and assessment placements.

The frame also retains directions that conflict with the sequence:

- Unit 1 calls for readiness on year-before triangle work.
- Unit 7 calls for exponent readiness, although the sequence explicitly teaches and assesses the prerequisite in unit 6.
- Unit 8 calls for coordinate readiness, although the sequence explicitly teaches and assesses that row in unit 1.
- Source-map allowances still describe launch days in units 2 and 4 as readiness days.

**Why it matters:** The next writer inherits unnecessary verification work and contradictory assessment instructions. The automated stale check does not detect these statements.

**Exact fix:**

1. Replace the missing-file statement with dated Grade 7 planning references, using the evidence table below.
2. Remove the provisional qualifications for the 18 verified mathematics rows.
3. Retain the separate qualification on the ELA argument routine, whose upstream day evidence was not verified here.
4. Align frame readiness directions with the sequence’s verified last uses, subject to finding 2’s start-of-year placement decision.
5. Rename the unit 2 and unit 4 source-map allowances as launches with retrieval.
6. Remove the comma attached to `8.F.A.3`.

These checks establish planned teaching and assessment, not classroom delivery.

## Order, standards and load

| Unit | Total days | Retained base lessons | Judgment |
|---|---:|---:|---|
| 1. Rigid transformations and congruence | 20 | 17 | Experimental moves precede congruence and informal angle arguments |
| 2. Dilations, similarity and slope | 16 | 13 | Center and multiplier precede similarity, angle-angle reasoning and slope triangles |
| 3. Linear relationships | 19 | 14 | Proportional comparison precedes initial value, line derivations and solution pairs |
| 4. Associations in data | 14 | 10 | Paired records and plots precede fitted models and categorical tables |
| 5. Equations and systems | 21 | 16 | Equivalent equations and solution counts precede simultaneous equations and substitution |
| 6. Functions and volume | 23 | 19 | One-output reasoning precedes comparisons, models and dimension-dependent volume |
| 7. Exponents and scientific notation | 20 | 16 | Factor reasoning precedes zero and negative exponents, scale and operations |
| 8. Pythagorean theorem and irrational numbers | 20 | 16 | Root bounds precede theorem applications; converse, coordinate distance and decimal classification follow |

No unit is demonstrably far over or under its mathematical load. The heavier work receives meaningful runs: nine equation lessons before seven system lessons, eleven function lessons before eight volume lessons, and eight exponent lessons before eight scientific-notation lessons.

All **24 owned progression rows** and **36 standard codes** have placements. The sequence explicitly carries the easily lost requirements: exterior-angle arguments, all rigid-motion preservation properties, both slope derivations, system inspection, all three solid-volume formulas, technology notation, irrational-expression estimates, repeating-decimal conversion, both square-equation signs, the theorem and converse, and three-dimensional lengths. Finding 1 concerns assessment actions despite code coverage.

No unit exceeds 25 days. The additional mid-unit assessments are sensibly positioned, including embedded assessments in units 1 and 2. Responses are allocated once on the full path; finding 3 addresses the shortened path.

## Readiness and retrieval evidence

The current Grade 7 plan supports retrieval for every directly assumed Grade 7 mathematics row:

| Earlier rows | Grade 7 evidence |
|---|---|
| Scale drawings | Teaching days 1 to 10; assessment 11 |
| Triangle conditions; angle relationships | Teaching 121 to 130; assessment 137 |
| Proportional tables, equations and graphs | Teaching 13 to 31; assessment 32 |
| Fractional unit rates | Teaching 47 to 50; assessments 57 and 67 |
| Population comparisons | Teaching 149 and 153; assessment 155 |
| Chance and probability models | Teaching 139 to 148; assessment 156 |
| Two-step equations; linear expressions | Teaching 92 to 116; assessment 117 |
| Rational-number problems | Teaching 84 to 89; assessment 90 |
| Circles | Teaching 35 to 42; assessment 43 |
| Composite area and prism volume | Teaching 132 to 136; assessment 137 |
| Signed multiplication and division | Teaching 76 to 82; assessment 90 |
| Decimal expansions | Explicit teaching 83; assessment 90 |
| Signed addition and subtraction | Teaching 69 to 75; assessment 90 |

The older rows receive these treatments:

| Row | Last explicit use before Grade 8 | Grade 8 treatment |
|---|---|---|
| `m4-symmetry` | Grade 4 | Readiness on day 1, placement correction required by finding 2 |
| `m6-four-quadrants` | Grade 6 | Readiness on day 1; explicit teaching and assessment on days 6 and 7; later same-year retrieval |
| `m6-exponents` | Grade 6 | Readiness on day 92 immediately before unit 6; explicit teaching and assessment on day 105; later same-year retrieval |

Grade 7’s brief retrieval references to exponents and coordinates do not establish renewed teaching or assessment of those complete older rows. No later unit checks an older row weeks ahead or puts readiness on its first day. The sequence itself does not misclassify a year-before mathematics row as readiness; the stale frame does.

## Course checks and cross-subject calendar

| Check | Placement | Recent-unit treatment |
|---|---|---|
| 1 | Day 70, week 14; response 71 | Uses earlier geometry and line content for recent data reasoning; retains recent data records |
| 2 | Day 116, week 24; response 117 | Uses earlier line and plan contexts for functions; retains volume evidence |
| 3 | Days 158 and 159, week 32; response 160 | Uses earlier figures and containers for recent root and right-triangle reasoning |

The sequence expressly requires earlier-unit content for recent-unit skills and different course-check forms. Actual items must preserve that distinction.

The checks meet the target weeks **14, 24 and 32**. Neither mid-year mathematics check shares another subject’s course-check day. Finals-week overlap is permitted.

The same-year leans are supported:

- Scatter plots precede science units 4 and 5, which start on days **77 and 105**.
- Mathematics days **58 and 59** supply growth-context bridges before science genetics.
- Science units 1 and 2 finish by day **46**, before mathematics graph-shape tasks on **97 and 98**.
- Science scale contexts precede mathematics scientific notation on **128**.
- Civics unit 4 finishes on **63**, before mathematics table tasks on **66 and 67**; a supplied-data fallback is named.

## Source map, candidates and shorter path

The source map accounts for all **131 unique base lessons**, matching the stored preparation-file inventory:

- **121 kept**, each assigned to a course day.
- **10 cut**, each with a reason.
- **39 original days**, completing 160 meetings.
- Retained lesson order preserved within every unit.
- The data-unit move justified by science availability and accompanied by changes to function language and later-unit practice.

All eight Candidate cells are settled. Progression comparisons cost zero student days; retained extensions replace existing examples; dropped investigations have reasons and day costs inside the allocations.

The 45-minute path names a complete period allocation and preserves explanation, an anchor task, synthesis and exit evidence. The ten fold-ins name receiving days and preserve owned content. Finding 3 is the specific response-time repair required.

## Focus, rigor and the mathematics lens

The conservative calculation reproduces exactly: **116 days × 45 minutes = 5,220 minutes**, or **65.25 percent of 8,000 minutes**. It is a planning lower bound. The frame’s approximate 81 percent remains unverified by this calculation.

Five units own only major clusters. Supporting data applies line reasoning; irrational-number work supports roots and lengths; volume connects to functions. The evidence guide permits connected supporting work and asks reviewers to compare several counting perspectives. [Evidence guide, indicator 1e](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf#page=13).

| Scope and sequence lens line | Result |
|---|---|
| Every owned standard reaches completion | **Met in instructional placement; assessment reservations need finding 1** |
| Problems deliberately join units | **Met:** days 53, 90, 113, 152 and the cumulative checks |
| Fluency receives spaced, mixed practice | **Met:** equation work continues through units 6 to 8 |
| Models and dependencies precede use | **Met overall** |
| Grade limits and algorithm expectations | **Met** |
| Supporting work connects to major work | **Met at planning level** |
| All eight practices have named tasks | **Met:** explicit content tasks identify MP1 to MP8 |
| Source decisions and order are complete | **Met** |
| Daily exits, scoring, accommodations and family supports | **Not yet applicable to full verification at this layer** |
| High school and post-Algebra-II provisions | **Not applicable** |

## What is right and should remain

- Similarity before slope, and equations before systems.
- The data-unit move and its prerequisite adaptations.
- Shared-standard completion across units.
- Exponent rebuilding before curved-solid formulas.
- Both theorem directions and the three-dimensional application.
- Original assessments, named retained products, paper paths and nonpersonal supplied data.
- The explicit distinction between planning allocations and demonstrated classroom timing.

The progression documents support these mathematical connections. The second curriculum comparison uses a different opening order but also places similarity before slope and connects functions with geometry; it supplies no reason to reorder this plan. [Expressions and Equations Progression](https://commoncoretools.files.wordpress.com/2011/04/ccss_progression_ee_2011_04_25.pdf), [Geometry Progression](https://mathematicalmusings.org/wp-content/uploads/2016/03/ccss_progression_g_7_hs_2016_03_27.pdf), [comparison curriculum, PDF pages 24 to 25](https://greatminds.org/hubfs/knowledge/resources/math/EM_Basic_Curriculum_Files/Curriculum_Overview/EM_G68_CurriculumOverview.pdf#page=24).

## Settled by the expert

These are recommendations for the caller to apply; no edits were made.

| Choice | Reason | Files affected |
|---|---|---|
| Retain day 61’s individual fitted-line product | Makes the productive part of 8.SP.A.2 explicit | Sequence and day file |
| Require constructed examples for all three equation solution counts on day 79 | Completes the reserved evidence for 8.EE.C.7a | Sequence and day file |
| Move shortened-path day 30 response into day 31’s ordinary opening | Preserves ten minutes of response without adding time | Shorter-path table and day note |
| Replace provisional Grade 7 entries with verified planning references | All 18 incoming mathematics rows now have evidence | Prerequisite register |
| Align frame readiness language with established last uses | Removes competing directions | Frame |
| Preserve unit order and mathematical allocations pending the start-of-year decision | No demonstrated load problem warrants broader changes | Frame and sequence |

## What I could not judge

Finished assessment items, answer keys, scoring criteria, accommodations and classroom completion times do not yet exist here. The packed assessment windows and transferred shorter-year tasks need checking against actual items during unit planning.

The compiled 2023 Progressions PDF exceeded the web tool’s size limit. Accessible earlier Expressions and Equations, Statistics and Probability, and Geometry drafts were used alongside the official standards. No conclusion relies on remembering inaccessible material.

## Outside sources

- [Official Grade 8 standards](https://www.thecorestandards.org/Math/Content/8/EE/), with the linked [Geometry](https://www.thecorestandards.org/Math/Content/8/G/), [Functions](https://www.thecorestandards.org/Math/Content/8/F/), [Number System](https://www.thecorestandards.org/Math/Content/8/NS/) and [Statistics](https://www.thecorestandards.org/Math/Content/8/SP/) pages: exact required performances.
- [Expressions and Equations Progression](https://commoncoretools.files.wordpress.com/2011/04/ccss_progression_ee_2011_04_25.pdf): exponents, roots, slope derivations and equations.
- [Statistics and Probability Progression](https://commoncoretools.files.wordpress.com/2011/12/ccss_progression_sp_68_2011_12_26_bis.pdf): paired data, scatter plots and informal models.
- [Geometry Progression](https://mathematicalmusings.org/wp-content/uploads/2016/03/ccss_progression_g_7_hs_2016_03_27.pdf): transformation and coordinate handoffs.
- [K to 8 Publishers’ Criteria](https://achievethecore.org/content/upload/Math_Publishers_Criteria_K-8_Spring_2013_FINAL.pdf): focus, coherence, rigor and similarity before slope.
- [Mathematics evidence guide](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf): full-intent assessment evidence and focus calculations.
- [Base curriculum sequence](https://im.kendallhunt.com/MS/teachers/3/scope_and_sequence.html): dependencies and the data-unit move.
- [Second curriculum overview](https://greatminds.org/hubfs/knowledge/resources/math/EM_Basic_Curriculum_Files/Curriculum_Overview/EM_G68_CurriculumOverview.pdf): independent sequence and pacing comparison, reference only.
- [Federal Grades 4 to 8 problem-solving guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/16/Published): representations, reflection and strategy comparison. It supports instructional choices, not this course’s exact pacing.

**For the source list:** Record the accessible Geometry draft URL and the Grades 6 to 8 comparison overview if absent. Retain the compiled-PDF size-limit note.

## For Cory

- Settle where the start-of-year readiness check belongs within the course’s time allocation. This run forbids the repository’s explicit day 1 exception; moving it into a separate counted meeting would change the frame’s unit/course-level day split.

**Final verdict:** Sound overall; revise before unit planning. **Finding count:** 4. **Report path:** `docs/reviews/sequence-math-grade-8-2026-11-15.md`, supplied here only.


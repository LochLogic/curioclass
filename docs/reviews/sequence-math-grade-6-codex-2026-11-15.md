# Independent scope and sequence review: Math Grade 6

**Date:** 2026-11-15  
**Intended report path:** `docs/reviews/sequence-math-grade-6-2026-11-15.md`  
**Delivery:** Complete report supplied here. No files were created or changed.

## Verdict

The eight-unit sequence is sound overall, with appropriate mathematical dependencies, substantial applications and a complete source map. Its main risks are an incomplete factoring requirement and conflicting time instructions that undermine the shorter-period promise. Make the four targeted corrections below before unit planning, preserving unit order, ownership and day counts.

## What I read and checked

- `docs/agents/EXPERT.md`, the mathematics lens, mathematics rubric, foundation, shared and mathematics approaches, relevant source notes, applicable ROADMAP sections, BASELINE rules 20 to 24, glossary and sequence-writing rules.
- The complete Grade 6 scope and sequence, frame, `days.csv` and `source-map.csv`.
- All Grade 6 progression rows, their Grade 5 prerequisites and Grade 7 handoffs, and the older factors and scaled-graphs rows.
- All local Grade 6 standard text, including lettered parts.
- `CALENDAR.md` and every Grade 6 calendar row.
- The current Grade 5 day file for prerequisite evidence.
- Earlier permitted Grade 6 frame reports and their fix dispositions, plus the Grade 3 sequence report for repeat classifications.
- The stored base-lesson inventory, selected base lessons and the outside sources linked below.

The blind-rule exclusions were respected. No curricular conclusion rests on memory. Prior review memory informed only the report structure.

### Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Did not complete: `ModuleNotFoundError: No module named 'markdown'` |
| `python -X utf8 scripts/frame.py calendar` | Passed; no stagger-rule breaks |
| `python -X utf8 scripts/frame.py check math-grade-6` | Passed: 0 failures, eight units, 160 days |
| `python -X utf8 scripts/sequence.py check math-grade-6` | Passed: 0 failures |
| `python -X utf8 scripts/stale.py check` | Passed: 56 files, 0 failures |

The sequence check notes a comma attached to `6.EE.A.1` in the frame. The actual code is present on days 14 and 15 and completed in unit 6. The incomplete full gate does not withhold this verdict.

## Findings, most serious first

### 1. Factoring a sum lacks the standard’s required stopping condition

**Severity:** Moderate  
**LAYER:** standard  
**REPEAT:** yes, incomplete standard clauses were identified in the earlier Grade 6 frame reads  
**Confidence:** Firm

**Location:** Scope and sequence, unit 7; `days.csv`, days 138 and 140; progression row `m6-gcf-lcm`; frame unit 7.

**What is wrong:** The plan requires factoring a sum using the distributive property, but never states that the two numbers remaining inside the sum must have no common factor greater than 1. That is an explicit requirement of [6.NS.B.4](https://www.thecorestandards.org/Math/Content/6/NS/).

For example, both `42 + 30 = 2(21 + 15)` and `42 + 30 = 6(7 + 5)` are valid equalities. Only the second reaches the required form. Day 140’s instruction to assess “factoring a sum” does not distinguish them.

**Why it matters:** A writer can build mathematically correct teaching and assessment items that establish only part of the owned standard.

**Exact fix:** Add to day 138:

> Factor a sum of two whole numbers from 1 to 100 by taking out their greatest common factor, and explain why the two numbers inside the parentheses have no common factor greater than 1.

Require that explanation in day 140’s existing factoring prompt. Carry the same stopping condition into the unit summary, frame and progression notes. Use a partially factored equality beside a fully factored one to make the distinction visible. No additional day is needed.

### 2. The time instructions conflict on readiness days and do not establish the 45-minute path

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, incompatible assessment and response allocations appeared in the earlier Grade 6 frame reads  
**Confidence:** Firm on the conflicting instructions; judgment call on the proposed shorter-period allocations

**Location:** `days.csv`, days 119 and 141; scope and sequence, “Shorter path”; the seven merged-day budgets.

**What is wrong:** Days 119 and 141 each prescribe:

- First 40 minutes: response and retry.
- Last 10 minutes: readiness.
- A separate five-minute mixed-practice opening.

The first two reservations already occupy 50 minutes. Neither row says that its ordinary opening is replaced or included, unlike the explicit replacement language used after the mid-unit assessments.

The shorter-period paragraph also promises to keep assessment and response reservations. A 40-minute response plus ten-minute readiness check cannot fit a 45-minute period. Merged days already contain 45-minute cores, so retaining their exact budgets plus spaced practice also exceeds 45 minutes.

**Why it matters:** Teachers receive incompatible schedules. The likely casualty is response, readiness, independent work or the exit ticket, precisely the components the plan promises to protect.

**Exact fix:**

1. On the full path, explicitly replace the ordinary opening on days 119 and 141. State **40 minutes response, including the changed retry, plus ten minutes readiness, total 50**.
2. Give those two days a separate shorter-period allocation: **35 minutes targeted response and retry plus ten minutes readiness, total 45**, without another opening.
3. On 45-minute assessment days, omit the unrelated mixed-practice opening and retain the assessment core.
4. Revise each merged-day budget to **40 minutes of core plus five minutes of spaced practice**, naming the repeated example or reporting turn removed. Retain synthesis and original exit evidence.
5. Give compressed day 4 one budget, since it receives both days 3 and 5. For example: five minutes retrieval, ten rearranging, ten deriving the formula and identifying perpendicular height, ten fractional substitution, five synthesis and five exit evidence.

Replace the blanket promise about unchanged reservations with these explicit shorter-period schedules. Recalculate affected minute classifications after the correction.

### 3. Unit 1’s prerequisite ledger misses its early volume and exponent connections

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, prerequisite retrieval occurring after first use appears in the Grade 3 sequence report, finding 2  
**Confidence:** Likely

**Location:** Scope and sequence, prerequisite table; `days.csv`, days 11, 14 and 15.

**What is wrong:** The ledger places volume-concept and volume-formula retrieval on day 74. Yet day 11 distinguishes surface area from volume, and day 14 uses cubic units and cube-layer drawings while adapting the base squares-and-cubes lesson.

The [base lesson’s preparation page](https://im.kendallhunt.com/MS/teachers/1/1/17/preparation.html) explicitly builds on Grade 5 volume. The exponent connection also begins here, while the named powers-of-ten retrieval is deferred to days 82 and 108. The [Expressions and Equations Progression, PDF page 4](https://commoncoretools.files.wordpress.com/2011/04/ccss_progression_ee_2011_04_25.pdf#page=4) connects Grade 5 powers of ten to Grade 6 numerical exponents.

Unit 1’s generic “grade 5 retrieval” opening does not identify these tasks.

**Why it matters:** The prerequisite record directs support to unit 4 or later even though the early geometry work already needs those connections. It also makes familiar exponent notation easier to present as entirely new.

**Exact fix:**

- On day 11, retrieve the distinction between counting square units on a surface and cubic units filling a solid.
- On day 14, retrieve the cube-layer relationship to `l × w × h`, then connect a familiar power-of-ten expression to repeated multiplication before extending to squares and cubes.
- Name `m5-volume-concepts`, `m5-volume-formulas` and `m5-powers-of-ten` in these notes and in the prerequisite ledger.
- Retain days 74, 82 and 108 as subsequent retrieval.

Use the existing opening or worked example. These are year-before retrieval tasks, with no new readiness check.

### 4. The prerequisite evidence limitation is obsolete, and the frame retains conflicting readiness directions

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, obsolete prerequisite-file status and readiness wording appear in the Grade 3 sequence report, finding 6  
**Confidence:** Firm

**Location:** Scope and sequence, lines 13 and 162 and prerequisite-table qualifications; repeated day notes; frame Readiness bullet, Seams table and affected unit descriptions.

**What is wrong:** The sequence says the Grade 5 day file was absent and leaves all 23 Grade 5 prerequisites provisionally classified. That file now exists, and every one of those rows has teaching or assessment placements.

The frame still directs readiness checks on Grade 5 area, fraction division and decimals, despite the sequence correctly treating these as retrieval and expressly overriding the frame.

**Why it matters:** The next writer inherits an unnecessary investigation and two competing sets of assessment directions.

**Exact fix:** Replace the missing-file claim with a dated statement that all 23 prerequisites were checked against the Grade 5 day plan. Record relevant day references and remove the repeated provisional qualifications. This verifies planned use, not classroom delivery.

Update the frame’s Grade 5 readiness directions to retrieval. Preserve the older-row readiness provisions for factors and scaled graphs. Grade 5 day 119’s passing retrieval of factors does not, by itself, establish teaching or assessment of the complete older row under sequence-writing rule 2.

The automated stale check did not detect these statements.

## Coverage, order and load

### Unit arcs

| Unit | Total days | Source-backed teaching days, including retained performances | Judgment |
|---|---:|---:|---|
| 1. Area and surface area | 18 | 16 | Decomposition precedes formulas; triangle work precedes nets and tent design |
| 2. Introducing ratios | 21 | 17 | Language and equivalence precede number lines, tables, graphs and representation choice |
| 3. Unit rates and percentages | 20 | 17 | Four conversion lessons, five rate lessons and eight percent/application lessons fit the ownership |
| 4. Dividing fractions | 20 | 17 | Both meanings precede the reciprocal algorithm, then lengths and fractional volume |
| 5. Arithmetic in base ten | 14 | 12 | Models explain algorithms; later mixed practice supports fluency |
| 6. Expressions and equations | 22 | 19 | Equation meanings precede equivalence, exponents and relationships |
| 7. Rational numbers | 22 | 19 | Signed positions and order precede inequalities, coordinates and contextual distances |
| 8. Data sets and distributions | 16 | 14 | Questions and displays precede measures, box plots and the final summary |

No unit is demonstrably far over or under its load. The allocations favor the heavier new representation and reasoning work rather than equal time per progression row.

The base dependency order is preserved. A second curriculum places geometry later and rational numbers before expressions, illustrating that another coherent order is possible, not that this course must change. [Base dependency guidance](https://im.kendallhunt.com/MS/teachers/1/scope_and_sequence.html), [second curriculum overview, PDF pages 3 to 4](https://greatminds.org/hubfs/knowledge/resources/math/EM_Basic_Curriculum_Files/Curriculum_Overview/EM_G68_CurriculumOverview.pdf#page=3).

### Standards and assessments

All **26 owned progression rows** and **47 local standard codes** have placements. No lettered code is absent. Finding 1 concerns the completeness of a required performance despite its code being present.

| Unit | Named end-window evidence |
|---|---|
| 1 | Tent design on 16; independent area and net prompts on 17 |
| 2 | Ratio investigation on 37; tables, plots, comparisons and ratio prompts on 38 |
| 3 | Paint plan on 57; rates, conversion and percent prompts on 58; parent ratio record completed with unit 2 evidence |
| 4 | Fractional box model on 77; division meanings, algorithm explanation and volume prompts on 78 |
| 5 | Applied algorithm record on 93; all four decimal algorithms and long division on 94 |
| 6 | Relationship performance on 115; expressions, equations, equivalence and exponents on 116 |
| 7 | Coordinate product on 139; signed-number, inequality and factors/multiples prompts on 140 |
| 8 | Contextual summary on 155; statistical questions, displays and measures on 156 |

The plan explicitly covers equation and inequality substitution, an unknown versus a variable set, fractional cube packing, coordinate side lengths and contextual statistical summaries. These should remain explicit in later items. [Expressions and Equations standards](https://www.thecorestandards.org/Math/Content/6/EE/), [Geometry standards](https://www.thecorestandards.org/Math/Content/6/G/), [Statistics and Probability standards](https://www.thecorestandards.org/Math/Content/6/SP/).

No unit exceeds 25 days. The additional mid-unit assessments on days **28, 49, 71, 103 and 130** are sensibly placed. In particular, day 71 follows instruction in the reciprocal algorithm. Embedded response replaces eight subsequent openings rather than adding eight new reservations.

Actual items remain necessary to verify that the broad independent-prompt sets fit their budgets. Their absence is appropriate at this layer and is not an additional finding.

### Readiness and retrieval

The current Grade 5 day plan supports retrieval for all 23 Grade 5 prerequisites:

| Prerequisites | Last-use grade established |
|---|---:|
| Fraction area; shape hierarchy | 5 |
| Scaling; fraction multiplication and its problems | 5 |
| Multiplication algorithm; two-digit division strategies | 5 |
| Coordinate system; plotted points; two patterns | 5 |
| Measurement conversion | 5 |
| Fraction as division; unit-fraction division; unlike-fraction addition/subtraction | 5 |
| Volume concepts and formulas | 5 |
| Decimal operations, place value, comparison and rounding; powers of ten | 5 |
| Numerical expressions; measurement line plots | 5 |

The two older directly assumed rows receive readiness:

| Row | Last explicit teaching grade | Placement |
|---|---:|---|
| `m4-factors-multiples` | 4 | Last ten minutes of day 119, before unit 7 opens on 120 |
| `m3-scaled-graphs` | 3 | Last ten minutes of day 141, before unit 8 opens on 142 |

Both checks are immediately before their units. Neither occurs on a unit’s first day or excessively far ahead. No misplaced year-before readiness check remains in the sequence itself. Findings 2 to 4 address the time instructions, early retrieval omissions and stale frame wording.

### Course checks and calendar

| Check | Placement | Recent-unit treatment |
|---|---|---|
| 1 | Day 80, week 16; response 81 | Earlier area/rate/sharing contexts; reuses days 77 to 78 evidence |
| 2 | Day 118, week 24; response 119 | Earlier ratio, fraction, decimal and area contexts; reuses recent relationship evidence |
| 3 | Days 158 to 159, week 32; response 160 | Earlier resource and area/rate contexts; reuses day 155’s summary |

The sequence explicitly requires different recent task forms and earlier-unit content for newly checked skills. Named carried records fall within ten school days. Response is assigned once per window, subject to finding 2’s scheduling clarification.

The checks meet the target weeks **16, 24 and 32**. No mid-year check shares another subject’s check day. Finals-week overlap is permitted.

Cross-subject timing is supported by the calendar:

- Earlier social studies timelines and mapping precede signed numbers and coordinates.
- Earlier science temperature-time and trial records precede their mathematical reuse.
- Mathematics ratios and rates precede science’s rate, scale and magnification applications.
- Science’s histogram bridge supplies reading before mathematics teaches construction.
- Earlier ELA research precedes the data project; the mathematics day retains a local fallback.
- Before mathematics histograms, the stated ELA bridge uses other displays.

The day 155 investigation overlaps the late social studies and ELA windows. The sequence discloses this and limits mathematics to one supplied-data period. Whether that exception satisfies the frame’s workload restriction remains Cory’s decision.

### Candidates, source map and shorter year

All eight Candidate cells are settled. Progression comparisons cost no student days; retained extensions fit existing tasks; dropped investigations have reasons.

The source map accounts for **147 unique base lessons**:

- **138 retained lessons** occupy **131 course days** through seven paired merges.
- **Nine lessons are cut**, each with a reason.
- **29 original days** complete the 160-day course.
- Retained source order is preserved.
- Every mapped base lesson has a corresponding stored preparation file.

The ten shorter-year fold-ins are days **3, 5, 20, 22, 32, 42, 53, 85, 123 and 146**. None carries an assessment flag, readiness check or embedded mid-unit response. Their named receiving days preserve the owned content. Finding 2 concerns the shorter-period budgets, especially where two folds converge on day 4.

### Focus, rigor and practices

The minute figures reproduce exactly: **5,154 strict major**, **1,033 connected geometry** and **1,813 other**, totaling 8,000 minutes. The connected total is **77.3 percent**; the strict total is **64.4 percent**.

Connected supporting work may be included, so the strict figure alone does not justify resizing units. These remain planning allocations, particularly where whole geometry cores are classified as connected work. The evidence guide calls for multiple counting perspectives and explicit connections. [Evidence guide, indicator 1e, PDF pages 14 to 15](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf#page=14).

All eight practices have named tasks: perseverance in division problems, quantitative reasoning in ratios and signed quantities, critique of equivalence and summaries, modelling in the tent and data tasks, representation choice, precision, structure and repeated algorithm reasoning.

## Mathematics lens checklist: scope and sequence

| Lens line | Result |
|---|---|
| Every owned standard reaches completion | **Missed in one explicit requirement:** finding 1 |
| Problems deliberately join units | **Met** |
| Fluency receives spaced, mixed practice | **Met**, with opening-time clarification in finding 2 |
| Models and prerequisite work precede dependent use | **Mostly met:** finding 3 |
| Algorithms and numerical limits respect grade expectations | **Met** |
| Supporting work connects to major work | **Met at planning level** |
| Focus is examined from multiple perspectives | **Met provisionally:** minutes, days, lessons and units are reported |
| All eight practices have named tasks and evidence | **Met at planning level** |
| Source-map decisions and order are complete | **Met** |
| Unit-level scoring, supports, daily exits and accommodations | **Not yet applicable to full verification** |
| High school and post-Algebra-2 provisions | **Not applicable** |

## What is right and should remain

- The eight-unit order, ownership and day totals.
- Both meanings of fraction division before the explained algorithm.
- The required tent application and deliberately connected later tasks.
- Models tied to written methods, followed by spaced algorithm practice.
- Original assessment evidence and explicit reuse of recent products.
- Supplied, nonpersonal data and the no-year-zero caution.
- The bounded final statistics investigation.

The emphasis on representations, reflection and strategy choice is consistent with the federal problem-solving guide. That supports these instructional choices, not a claim that this course’s pacing has been validated. [Federal Grades 4 to 8 practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/16/Published).

## Settled by the expert

These are item-level corrections for the caller to apply.

| Choice | Reason | Files affected |
|---|---|---|
| Require complete factoring, with no shared factor greater than 1 remaining inside the sum | Completes 6.NS.B.4 | Sequence, day file, frame, progression |
| Replace the ordinary opening on readiness/response days | Removes incompatible time instructions | Day file and shorter-path prose |
| Specify separate 45-minute schedules | Makes the shorter-period route actionable | Sequence, day file, source map |
| Retrieve volume and familiar exponent notation during unit 1 | Reconnects prerequisites before their early use | Prerequisite ledger and day notes |
| Replace provisional Grade 5 status with verified planning references | The upstream day plan now exists | Sequence and day notes |
| Retain unit order, ownership and allocations | No demonstrated load problem requires changing them | Frame and sequence |

## What I could not judge

Finished assessment items, scoring guidance, accommodations and actual classroom completion times are not yet available. The seven merged lessons and dense final checks need verification with the actual items during unit planning.

The compiled 2023 Progressions PDF exceeded the web retrieval limit. The separate Number System and Geometry progression links could not be retrieved. Accessible earlier ratio, expression and statistics drafts were read alongside the official standards; their older wording was not treated as overriding the standards.

## Outside sources

- [Official Grade 6 standards](https://www.thecorestandards.org/Math/Content/6/NS/): exact expectations, especially complete factoring.
- [Expressions and Equations Progression](https://commoncoretools.files.wordpress.com/2011/04/ccss_progression_ee_2011_04_25.pdf): prior expressions, exponents and variable meanings.
- [Ratios and Proportional Relationships Progression](https://commoncoretools.files.wordpress.com/2012/02/ccss_progression_rp_67_2011_11_12_corrected.pdf): multiplicative equivalence and connected representations.
- [Statistics and Probability Progression](https://commoncoretools.files.wordpress.com/2011/12/ccss_progression_sp_68_2011_12_26_bis.pdf): distributions, measures and box-plot dependencies.
- [Base curriculum sequence](https://im.kendallhunt.com/MS/teachers/1/scope_and_sequence.html): dependency order.
- [Second curriculum overview](https://greatminds.org/hubfs/knowledge/resources/math/EM_Basic_Curriculum_Files/Curriculum_Overview/EM_G68_CurriculumOverview.pdf): independent comparison of sequencing and load, reference only.
- [K to 8 Publishers’ Criteria](https://www.thecorestandards.org/assets/Math_Publishers_Criteria_K-8_Spring%202013_FINAL.pdf): focus, coherence and rigor.
- [Mathematics review criteria](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Review%20Criteria_2.0.pdf) and [evidence guide](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf): full-intent evidence and focus-counting perspectives.
- [Federal problem-solving guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/16/Published): representations, reflection and strategy comparison.

**For the source list:** Add the corrected ratio-progression URL and the Grades 6 to 8 comparison overview if absent. Record the compiled-PDF size limit and failed progression fetches.

## For Cory

- Decide whether the bounded, single-period statistics investigation is an acceptable exception to the frame’s cross-subject project-overlap restriction. Complete calendar separation would require a broader calendar or scope decision.

**Final verdict:** Sound overall; make four targeted corrections before unit planning. **Finding count:** 4. **Report path:** `docs/reviews/sequence-math-grade-6-2026-11-15.md`, supplied here only.


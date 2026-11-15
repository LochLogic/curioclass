# Independent cold read: Grade 2 Math scope and sequence

**Date:** 2026-11-15  
**Role:** Independent first reader, before the expert  
**Intended report path:** `docs/reviews/sequence-math-grade-2-2026-11-15.md`  
**Delivery:** Complete report supplied here. No files changed.

## Verdict

The sequence is coherent overall, but needs four targeted corrections before unit planning. The biggest instructional risk is day 6’s wording, which permits subtraction beyond the range taught so far; the year-end check also leaves direct within-100 fluency evidence unspecified. Preserve the nine-unit order and allocations, tighten those instructions, repair the shorter-year fold-in, and reconcile the stale frame wording.

## What I read

- `docs/agents/EXPERT.md`, the mathematics lens, `docs/RUBRIC-MATH-K8.md`, the foundation, relevant Roadmap requirements, BASELINE rules 20 to 24, glossary, shared and mathematics approaches, and relevant source-register entries and evidence notes.
- The complete Grade 2 mathematics scope and sequence, all 160 daily rows, the frame, its inventory row, and the complete source map.
- All 28 Grade 2 progression rows, their 26 Grade 1 mathematical prerequisites, and relevant Grade 3 handoffs.
- Grade 1 mathematics daily placements for every assumed row, plus Grade 1 social studies’ saving instruction.
- Complete Grade 2 standards, `docs/courses/CALENDAR.md`, and Grade 2 calendar entries across all four subjects.
- Sequence-writing requirements, earlier Grade 2 frame reviews and fixes, neighboring mathematics sequence reviews, and the readiness-timing decision.
- The outside sources linked below.

The prohibited files were not opened. No curriculum conclusion rests on memory.

## Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Did not finish: `ModuleNotFoundError: No module named 'markdown'`. |
| `python -X utf8 scripts/frame.py calendar` | Passed; Grade 2 mathematics checks occupy weeks 18 to 19 and 29. |
| `python -X utf8 scripts/frame.py check math-grade-2` | Passed: nine units, 160 days, including 153 unit days and seven course-level check/respond days. |
| `python -X utf8 scripts/stale.py check` | Passed: 56 files, zero failures. Manual inconsistencies remain below. |

The incomplete global gate does not prevent this substantive verdict.

## Findings, most serious first

### 1. Day 6 permits subtraction that has not been taught

**LAYER:** sequence  
**REPEAT:** yes, the same broad-goal problem identified in the Grade 1 sequence review, finding 2  
**Severity:** moderate  
**Confidence:** firm

**Location:** `data/plans/math-grade-2/days.csv`, day 6.

**What is wrong:** The goal says, “Practice adding and subtracting within 10, 20, or 50.” Its ordinary reading permits general subtraction within 50.

Days 1 to 4 teach facts within 20, and day 5 extends addition to 50. General two-digit subtraction begins in unit 2. Grade 1 provided subtraction within 20 and subtraction of multiples of ten, rather than general subtraction within 50.

The retained base lesson’s detailed learning goals distinguish addition/subtraction within 20 from addition within 50. Its broad purpose sentence lost that distinction when copied into the daily goal. [Base lesson preparation](https://im.kendallhunt.com/k5/teachers/grade-2/unit-1/lesson-6/preparation.html). The [base-ten progression, PDF page 7](https://commoncoretools.files.wordpress.com/2011/04/ccss_progression_nbt_2011_04_073.pdf) explains why general two-digit subtraction is deferred.

**Why it matters:** A writer following the authoritative goal could create practice requiring a strategy students have not yet learned.

**Exact fix:** Replace day 6’s goal with:

> Practise addition and subtraction within 20 and addition within 50.

Add the same operation-specific limits to its note and source-map reason. Preserve both existing skills and codes: the within-100 code represents an early contribution, not completed fluency. Keep the day and its shorter-year fold into day 5.

### 2. The year-end check does not identify direct within-100 fluency evidence

**LAYER:** sequence  
**REPEAT:** yes, incomplete alignment between an assessed code and the named performance, as in earlier Grade 2 frame findings  
**Severity:** moderate  
**Confidence:** likely

**Location:** Scope and sequence, “Course-level checks,” especially line 157; `days.csv`, day 144.

**What is wrong:** Day 144 lists `m2-fluency-within-100` and `2.NBT.B.5`, but names error analysis and connections between drawings and written methods. It does not explicitly require students to calculate mixed within-100 sums and differences independently, or identify a retained record that demonstrates that fluency.

The reused facts record concerns within-20 work. The reused unit 7 explanation record concerns three-digit methods. Neither establishes the listed within-100 fluency target.

Error analysis can reveal understanding while leaving a student’s independent calculation fluency untested. The [standard, PDF page 19](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf) and [Publishers’ Criteria, PDF page 11](https://achievethecore.org/content/upload/Math_Publishers_Criteria_K-8_Spring_2013_FINAL.pdf) distinguish fluent computation from conceptual explanation.

**Why it matters:** The handoff could report year-end fluency using evidence that demonstrates a different demand.

**Exact fix:** Use the already-budgeted written warm-ups on days 138 and 140:

- Day 138: retain each child’s independent within-100 addition, including cases with and without composing a ten.
- Day 140: retain corresponding subtraction, including cases with and without decomposing a ten.
- Record accuracy and the strategy used, without a student-facing timer or blocks as fluency evidence.
- Add the relevant skill/code and evidence note to those rows.
- State explicitly that day 144 reuses these products for `2.NBT.B.5`; its fresh error-analysis task supplies complementary reasoning evidence.

This adds no day or individual interview and preserves the non-repetition rule.

### 3. The shorter-year path removes the line-plot introduction under the wrong description

**LAYER:** sequence  
**REPEAT:** new  
**Severity:** moderate  
**Confidence:** firm

**Location:** Scope and sequence, “Shorter path,” line 175; `days.csv`, days 51 to 53.

**What is wrong:** The fold-in table sends day 52 into day 51 while describing its retained work as “Metric/customary benchmark review and a measured difference.”

Day 52 actually introduces line plots. Day 51 practises measurement and calculation, and day 53 expects students to create line plots. The proposed fold preserves different work from the day being removed.

The source map identifies day 52 as base lesson 3.14, whose purpose is introducing the representation and its features. [Base lesson 3.14](https://im.kendallhunt.com/k5/teachers/grade-2/unit-3/lesson-14/lesson.html).

**Why it matters:** A teacher following the shorter path could reach line-plot construction without the planned introduction to its scale and data representation.

**Exact fix:** Retain day 52. Replace that fold-in row with:

| Fold-in day | Neighbor retaining its work | Retained work |
|---|---|---|
| 115 | 114 | Short no-exchange addition practice within 1000, following the model-to-written connections already taught |

Day 115 is unassessed practice following day 114’s explicit no-exchange work. Keep its essential practice within approximately ten minutes of day 114 by reducing repetition. This retains ten folds and preserves the line-plot teaching order.

### 4. Current frame and daily wording still conflict with the sequence

**LAYER:** process  
**REPEAT:** yes, stale instructions recur in the earlier frame and neighboring sequence reviews  
**Severity:** minor  
**Confidence:** firm

**Location:** Frame, Readiness bullet and units 1, 2, 3 and 5; unit 9 descriptions and totals; `days.csv`, day 42.

**What is wrong:**

- The frame still prescribes readiness checks for Grade 1 prerequisites. The sequence correctly assigns retrieval because those rows were used the year before.
- The frame says unit 9 has no assessment of its own. The sequence now gives it an embedded day 159 observation and day 160 response.
- Day 42 says students use a ruler “for the first time,” after day 41 already explicitly uses one.
- The frame’s budget explanation still uses nine assessment days and six course-level check/respond days, although its implemented allocation is eight separate assessment days and seven course-level days.

The sequence already acknowledges the readiness and unit 9 conflicts. They remain outstanding documentation repairs, rather than newly discovered mathematical defects.

**Why it matters:** A unit writer can follow conflicting instructions about assessment placement and first instruction.

**Exact fix:**

- Replace the frame’s year-before readiness language with retrieval inside lessons. Preserve readiness checks only for genuinely older prerequisites.
- Describe unit 9 as having “no separate assessment day; an embedded closing observation and response remain within its final lessons.”
- Remove “for the first time” from day 42.
- State the implemented budget consistently: 139 retained lessons, six added teaching days, eight separate assessment days, and seven course-level check/respond days.

Keep historical reviews unchanged.

## Order, standards and days by load

| Unit | Days | Owned rows | Judgment |
|---|---:|---:|---|
| 1. Addition, subtraction and data | 19 | 3 | Graphs lead coherently to comparison tapes. Correct day 6’s numerical limits. |
| 2. Within 100 | 19 | 5 | No-exchange subtraction precedes decomposition; stories precede two-step composition. |
| 3. Measurement | 19 | 5 | Equal units, rulers, benchmarks, comparisons and plots form a sound arc. |
| 4. Number line | 16 | 1 | The broad foundational model justifies more time than its single row suggests. |
| 5. Numbers to 1000 | 16 | 5 | Hundreds precede representations, crossings, comparison and mental changes. |
| 6. Geometry, time and money | 18 | 4 | Eight geometry/share days, three clock days, six money days and the closing day fit the load. |
| 7. Within 1000 | 21 | 2 | The heaviest computation receives the largest allocation, including zero and method comparison. |
| 8. Equal groups | 12 | 3 | Pairing precedes arrays; arrays precede partitioned rectangles. |
| 9. Putting it together | 13 | 0 | Justified cumulative review and response, with embedded closure. |

No allocation is demonstrably far over or under its substantive load. Equal days per progression row would misrepresent the work.

All 26 numbered Grade 2 standards and both lettered parts of `2.NBT.A.1` have substantive teaching placements. The plan explicitly carries the easily omitted requirements: both graph forms, generated measurement data, number names and expanded form, all four mental ten/hundred operations, shape drawing, share and whole language, analog/digital time, and money notation.

Assessment windows generally name suitable products and missing-part prompts. Units 1 to 8 have closing assessments; unit 9 has its embedded observation. No unit exceeds 25 days, so no mid-unit assessment is required. Response time is allocated once. Finding 2 repairs the remaining year-end fluency specification.

## Readiness, retrieval and calendar

All **26 directly assumed mathematical rows**, plus `ss1-saving`, were taught or assessed in Grade 1. Their treatment as retrieval is correct.

| Unit | Retrieval placement |
|---|---|
| 1 | Day 1: facts, problem meanings, equality, unknowns and categorical data |
| 2 | Day 20: Grade 1 calculation and grouping, plus unit 1 tapes |
| 3 | Day 39: equal-unit measurement and comparison, plus calculation |
| 4 | Day 58: measurement and unit 3 rulers |
| 5 | Day 74: tens, digits, counting, comparison and ten-more/less |
| 6 | Day 93: shapes, shares, clocks, saving context and skip-counting |
| 7 | Day 111: earlier calculation and place value |
| 8 | Day 132: shape composition and doubles |
| 9 | Day 148: earlier representations and assessment records |

No older prerequisite is incorrectly retrieved, and no readiness check is misplaced on a first day or weeks ahead. The stale frame instructions are finding 4.

The course-level checks match the calendar’s target weeks. ELA’s mid-year check ends on day 76, fourteen school days before mathematics day 90. Its year-end check begins on day 158, thirteen days after mathematics’ record-use day 145.

The same-year leans have suitable bridges:

- ELA talk moves and story-question modelling occupy named time on days 20 and 31.
- Later science plant and habitat work is replaced by classroom-object data.
- Science’s earlier erosion measurement retains its ruler bridge while mathematics teaches centimeters and rulers.

Immediate course-level checks explicitly use earlier-unit contexts and different task forms for the just-ended unit. Recent counting, facts and method records are reused.

## Source map, Candidates and shorter path

The source map accounts for all **146 base lessons: 139 kept and seven optional lessons cut**. Its fourteen original rows represent six added teaching days and eight separate assessments. Retained lessons stay in base order.

All nine Candidate cells are settled. Planning comparisons cost zero student days; retained extensions have named time inside existing days; dropped extensions have reasons. The earlier corrections requiring above-100 four-addend totals and retaining base lesson 3.17 remain intact.

The 45-minute route preserves the main instructional components, but observation and packet timing still require unit-plan demonstration. Of the ten proposed shorter-year folds, nine preserve the stated work; finding 3 replaces the incorrect tenth. None of the proposed fold days carries an assessment marker.

The warning that a 150-meeting calendar requires a fresh cross-subject stagger is appropriate.

## Mathematics lens checklist

| Lens requirement | Result |
|---|---|
| Every owned standard is completed beyond its headline | **Met in teaching allocation.** Year-end fluency evidence needs finding 2. |
| Problems deliberately join units | **Met:** graph-to-tape comparisons, measurement stories, number-line translations and later graph calculations. |
| Fluency receives spaced, mixed practice | **Met:** daily practice, alternate written work, retained games and cumulative review. |
| Models precede dependent work | **Met in the full sequence.** Shorter-path exception is finding 3. |
| Grade limits and strategy order are respected | **Missed in day 6’s wording:** finding 1. |
| Major work receives sufficient emphasis | **Met provisionally:** the recorded total is 7,930/9,600 minutes, or 82.6 percent. |
| Supporting work practises major work | **Met:** explicit arithmetic connections in data, clocks, money and arrays. |
| Every source lesson has a decision | **Met.** |
| All eight practices have content tasks and evidence | **Met at this layer.** |
| Understanding, fluency and application are represented | **Met in the planned sequence.** |
| Finished assessment items, exits and accommodations | **Not applicable yet:** instruments remain to be written. |
| Final manipulative connections and timer behavior | **Not applicable yet:** lesson artifacts remain to be built. |
| High-school and post-Algebra II provisions | **Not applicable.** |

The focus percentage is a planning allocation, not measured classroom time. The [mathematics evidence guide, PDF pages 13 to 15](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf) supports the K to 2 threshold and counting supporting work connected to major work.

## What is right and should not be touched

- The nine-unit order and unequal allocations.
- Rulers before abstract number lines, and hundreds before three-digit computation.
- Nearby treatment of subtraction with and without decomposing.
- Above-100 four-addend totals in required work.
- Whole-year fact development, without treating September recall as an exit requirement.
- Reused individual records and explicitly counted response time.
- Paper alternatives and contexts that avoid personal disclosures.

## Settled by the expert

| Choice | Reason | Files affected by eventual repair |
|---|---|---|
| Bound day 6 subtraction to 20 and addition to 50 | Matches taught content and detailed base goals | `days.csv`, source map |
| Retain within-100 written products on days 138 and 140 | Supplies direct year-end fluency evidence without another interview | `days.csv`, scope and sequence |
| Keep day 52; fold day 115 into 114 instead | Preserves the line-plot introduction and ten-day reduction | Scope and sequence |
| Preserve unit order and all full-year allocations | No finding requires moving ownership or resizing units | Frame and sequence |
| Keep all listed Grade 1 prerequisites as retrieval | Their last-use grade is verified | Frame |
| Describe unit 9’s closure as embedded | Reconciles the frame with the implemented observation | Frame |

## What I could not judge

Assessment items, scoring guidance, full coverage rosters, accommodations and lesson-part timing are not yet available. The broad cumulative packets and practical observation windows therefore remain planning estimates.

The consolidated 2023 Progressions PDF exceeded the web tool’s size limit. I read the authors’ accessible earlier domain drafts for the relevant comparisons; I did not independently verify every 2023 page citation.

## Sources

- [Official mathematics standards](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf), PDF pages 19 to 20: Grade 2 requirements and limits.
- [Operations progression](https://commoncoretools.files.wordpress.com/2011/05/ccss_progression_cc_oa_k5_2011_05_302.pdf), PDF pages 18 to 21: problem subtypes, two-step limits and fluency.
- [Base-ten progression](https://commoncoretools.files.wordpress.com/2011/04/ccss_progression_nbt_2011_04_073.pdf), PDF pages 7 to 9: subtraction handoff, hundreds and computation.
- [Measurement progression](https://commoncoretools.files.wordpress.com/2012/07/ccss_progression_gm_k5_2012_07_21.pdf), Grade 2 section: ruler units and number-line foundations.
- [Base curriculum scope and sequence](https://im.kendallhunt.com/k5/teachers/grade-2/course-guide/scope-and-sequence.html): unit order and mathematical arcs.
- [Eureka Math overview](https://greatminds.org/hubfs/3454910/knowledge/resources/math/EM_Basic_Curriculum_Files/Curriculum_Overview/EM_GPK5_CurriculumOverview.pdf), Grade 2 beginning on PDF page 25, and [Fishtank Grade 2](https://www.fishtanklearning.org/curriculum/math/2nd-grade/): comparison sequences, used as references only.
- [K to 8 Publishers’ Criteria](https://achievethecore.org/content/upload/Math_Publishers_Criteria_K-8_Spring_2013_FINAL.pdf): coherence and distinct rigor demands.
- [Federal elementary mathematics intervention guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/26): systematic instruction, representations and deliberate word-problem teaching. Its intervention setting does not establish whole-course effectiveness.

## For the source list

Record the accessible domain-progression links above as fallbacks when the consolidated PDF exceeds the tool limit.

## For Cory

- No new scope, money, people or audience decision arises from these findings.
- The existing K to 2 device assumption remains an audience decision; this sequence can proceed through its paper path.

**Verdict:** Coherent sequence; revise before unit planning. **Finding count:** 4. **Report path:** `docs/reviews/sequence-math-grade-2-2026-11-15.md`, supplied here, not written.
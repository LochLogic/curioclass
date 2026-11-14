# Independent review: Grade 2 Math course frame

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/frame-math-grade-2-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files changed.

## Verdict

The frame has a sound mathematical sequence and a workable year allocation, but needs targeted revision before unit planning. Its biggest risk is that Unit 2 makes part of an owned standard optional, while several other summaries leave required student performances implicit. Restore those requirements, assign MP2 explicitly, and correct the stale notes while preserving the nine-unit order.

## What I read and checked

- `docs/agents/EXPERT.md`, the mathematics lens, `docs/RUBRIC-MATH-K8.md`, the foundation, the relevant roadmap sections, BASELINE rules 20 to 24, the shared and mathematics approaches, source guidance, and glossary.
- The complete Grade 2 frame, its `frames.csv` row, all 28 Grade 2 progression rows, adjacent-grade handoff rows, and the Grade 1 and Grade 3 mathematics frames.
- Grade 2 standards in `data/standards/ccss-math-standards.txt`.
- The Grade 2 science, ELA and social studies frames for the relevant cross-subject dependencies.
- The base text’s nine unit overviews, lesson inventories and preparation-page standards tags, plus selected lesson text supporting the findings below.
- Earlier Grade 2 reviews, the K to 2 fixes report, relevant progression reconciliation and fixes, and neighboring mathematics reviews for repeated finding types.

`data/plans/math-grade-2/source-map.csv` does not exist. The frame-writing brief explicitly postpones that CSV until the scope and sequence, so I reviewed the complete inline map and do not repeat the previously rejected missing-file finding.

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Could not finish: `ModuleNotFoundError: No module named 'markdown'`. |
| `python -X utf8 scripts/frame.py check math-grade-2` | Passed: 9 units, 160 days, 154 within units and 6 for checks and respond days. |
| `python -X utf8 scripts/stale.py check` | Passed: 56 files, zero failures. Unmarked stale statements remain below. |

The current brief expressly permits this substantive review despite the incomplete gate. It supersedes the earlier Codex report’s decision to withhold judgment.

## Findings, most serious first

### 1. Required four-addend work is labelled an extension

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, narrowing an owned standard, as in the earlier Grade 2 expert review, finding 5  
**Confidence:** firm

**Location:** `docs/courses/math-grade-2/frame.md:144`, Unit 2, especially “Extension: four addends with a total past 100.”

**What is wrong:** The progression’s `m2-add-four-two-digit` row explicitly permits totals above 100. The frame instead puts those totals in an extension, inviting the unit writer to reserve them for selected students. The standard limits the addends’ size and number, without imposing a total of 100. [Official standards, PDF page 19](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf).

**Why it matters:** A student could complete the required path without experiencing the full number range of the standard.

**Exact fix:** In Unit 2’s learning description, write:

> Add up to four two-digit numbers using place value and properties, including totals above 100. For example, group 25 + 35 + 45 + 15 as 60 + 60 = 120.

Replace the extension with:

> Find two different useful groupings of four two-digit addends and explain why both give the same total.

Keep ownership in Unit 2 and retain its 19 days. Include an above-100 example in its required teaching and assessment.

### 2. Several summaries omit required student performances

**Severity:** Moderate  
**LAYER:** standard  
**REPEAT:** yes, the same incomplete-summary problem as the earlier Grade 2 expert review, finding 5  
**Confidence:** firm

**Location:** The Units table, Units 1, 3 and 6.

**What is wrong:** These cells name content without fully stating what students must do:

| Unit and standard | Missing or implicit requirement | Exact replacement or addition |
|---|---|---|
| 1, `2.MD.D.10` | Producing both graph types | “Students draw both picture graphs and bar graphs with a single-unit scale for up to four categories, then solve the stated data problems.” |
| 3, `2.MD.D.9` | Generating the plotted measurements | “Students generate data by measuring several objects to the nearest whole unit, or repeatedly measuring one object, and construct a line plot with a whole-number horizontal scale.” |
| 6, `2.MD.C.7` | Writing time and using both clock forms | “Tell and write time from analog and digital clocks to the nearest five minutes, using a.m. and p.m.” |
| 6, `2.G.A.1` | Drawing shapes from attributes | “Recognize and draw shapes with specified attributes, and identify the listed shapes.” |

These demands appear in the [official standards, PDF page 20](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf) and the progression notes.

**Why it matters:** Reading graphs, naming shapes and answering clock questions can appear to satisfy the current summaries. Those activities alone do not demonstrate the required production tasks.

**Exact fix:** Apply the wording above in the existing cells. The retained base lessons already provide homes for this work, including graph construction, ruler-generated data, drawing shapes and clock work. No lesson, standard or day needs moving. This is a defect in the frame’s instructions to writers, not evidence that the base text omits the teaching.

### 3. MP2 has no explicit unit assignment

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, the same omission identified in the Grade 3 Codex rerun, finding 4  
**Confidence:** firm

**Location:** The Standard bullet and Units table.

**What is wrong:** The frame promises the eight mathematical practices, but its candidates name MP1 and MP3 through MP8 only. MP2 is absent.

The retained [base lesson 2.4.13](https://im.kendallhunt.com/k5/teachers/grade-2/unit-4/lesson-13/lesson.html) explicitly develops MP2 by connecting situations, equations, number lines and tape diagrams. The [Publishers’ Criteria, PDF page 14](https://achievethecore.org/content/upload/Math_Publishers_Criteria_K-8_Spring_2013_FINAL.pdf) calls for each practice to be meaningfully present across the year.

**Why it matters:** Without a named home, the unit writer can overlook the connection between numerical representations and the quantities they describe.

**Exact fix:** Replace Unit 4’s candidates with:

> Candidate: MP.2, interpreting quantities across stories, equations and number-line diagrams, anchored in base lesson 2.4.13; MP.5, choosing and using the number line.

MP7 remains explicitly assigned elsewhere. Add a brief course-wide inventory showing where all eight practices sit. Keep the unit’s 16 days.

### 4. The lens still describes completed progression work as missing

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, kindergarten Codex finding 6 and Grade 1 Codex finding 6; still unapplied  
**Confidence:** firm

**Location:** `docs/agents/lenses/math.md:61`.

**What is wrong:** The lens says progression pages exist only for Grades 3 to 5 and that other bands need the same handoff work. The assembled progression and course frames now record that work.

**Why it matters:** Every new reviewer is directed toward rebuilding an existing layer instead of examining its remaining weaknesses.

**Exact fix:** Replace the two-line gap with:

> Core mathematics ownership, handoffs, models and limits from kindergarten through Grade 11 are recorded in data/progressions/math.csv. The Grades 3 to 5 narrative remains supplementary guidance. Course-frame reviews check these records against actual unit order.

### 5. The lens’s missing untimed-check guidance claim is stale

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, kindergarten Codex finding 5 and Grade 1 Codex finding 7; still unapplied  
**Confidence:** firm

**Location:** `docs/agents/lenses/math.md:65`.

**What is wrong:** The lens says no page explains checking K to 2 counting and fluency without a timer. The frames now describe observation, listening, games and individual checks, including recorded strategy categories.

**Why it matters:** The note hides the actual remaining work: usable tasks, recording procedures and instructional responses.

**Exact fix:** Replace the gap with:

> The K to 2 frames describe untimed counting and arithmetic-fluency checks through observation, games and individual listening. Unit plans must specify the tasks, recording guidance, coverage of every child and response decisions. Counting and arithmetic fluency are checked separately.

This preserves the distinction between a documented approach and completed assessment instruments.

### 6. The rubric’s current-state table understates work already on file

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale planning-status statements recur in the earlier frame reviews  
**Confidence:** firm

**Location:** `docs/RUBRIC-MATH-K8.md:34` and the teacher-supports row immediately below it.

**What is wrong:** The table says mathematical practices are “not in our plan at all” and lists writing the approach with sources as unfinished. Practices now appear in frames and planning fields, and the approach pages and source register exist.

**Why it matters:** The standing bar sends writers back to completed documentation while failing to distinguish planning from implementation.

**Exact fix:** Rewrite the practices status cell:

> Practices appear in course frames and unit and section planning fields. Remaining work: verify that each course places all eight in suitable content tasks and carries them through teaching and assessment.

In the teacher-supports cell, replace the missing-approach claim with:

> The shared and mathematics approaches and their source register are on file. Their stated review status remains as recorded on those pages.

Retain the genuinely unfinished teacher-support work.

### 7. The earlier Grade 2 report retains an obsolete ELA limitation

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, the same historical-review status problem identified in the kindergarten Codex review, finding 7  
**Confidence:** firm

**Location:** `docs/reviews/frame-math-grade-2-2026-11-14.md:17`.

**What is wrong:** The earlier report says no Grade 2 ELA frame exists yet. It now exists, and the mathematics frame uses its first unit for discussion and text-question dependencies.

**Why it matters:** A subsequent reader could treat coordination with ELA as still unexamined.

**Exact fix:** Preserve the original account of that reader’s work, but append:

> Update, 2026-11-14: the Grade 2 ELA frame now exists. Its Unit 1 places e2-discussion and e2-wh-questions in weeks 1 to 7. The mathematics frame names local bridges where their precise teaching dates may follow first use.

## Coverage, order and pacing

**Owned skills:** All 28 Grade 2 progression skills occur exactly once in the Skills column. No foreign skill ownership was found. Later-grade examples are labelled as extensions; Finding 1 corrects a Grade 2 requirement mistakenly placed there.

**Standards:** Every owned code, including the lettered parts of `2.NBT.A.1`, has a unit. Findings 1 and 2 address the remaining scope and wording defects. The contributing and owning rows for `2.OA.A.1`, `2.NBT.B.5` and `2.NBT.B.7` are distinguished.

**Unit reasons and order:** The sequence holds. Measurement precedes the abstract number line, place value precedes three-digit computation, and arrays precede partitioned rectangles. No unresolved use-before-teaching problem was found.

| Unit | Owned skills | Kept base lessons | Added lessons | Assessment days | Total days |
|---|---:|---:|---:|---:|---:|
| 1 | 3 | 17 | 1 | 1 | 19 |
| 2 | 5 | 16 | 2 | 1 | 19 |
| 3 | 5 | 18 | 0 | 1 | 19 |
| 4 | 1 | 15 | 0 | 1 | 16 |
| 5 | 5 | 14 | 1 | 1 | 16 |
| 6 | 4 | 17 | 0 | 1 | 18 |
| 7 | 2 | 18 | 2 | 1 | 21 |
| 8 | 3 | 11 | 0 | 1 | 12 |
| 9 | 0 | 13 | 0 | 1 | 14 |
| **Total** | **28** | **139** | **6** | **9** | **154** |

Four course-check days and two respond days bring the year to **160 days**. Unit 7’s two broad computation skills justify its 21 days; Unit 4’s foundational model justifies 16 despite having one progression row. Unit 9 is justified as cumulative review. No unit is demonstrably far over or under its load at this layer.

**Source map:** All 146 base lessons are accounted for: 139 retained and seven optional lessons cut with reasons. Unit boundaries and base-lesson order are preserved. Six additions are named. No reference-only or non-commercial source is mapped as teaching material.

**Seams:** Grade 1’s adapted tape-diagram introduction is picked up explicitly. Grade 3 receives the expected arithmetic, measurement, graphing, array and partitioning foundations. Longer handoffs and threads ending in Grade 2 are identified.

**Cross-subject:** ELA’s concurrent teaching has explicit mathematics bridges. Science’s later applications are distinguished from prerequisites, and its early ruler use has its own bridge. No unresolved dependency on another subject teaching an unavailable skill was found.

## Mathematics lens checklist

| Course-frame line | Result |
|---|---|
| Major work meets the K to 2 line by multiple perspectives | **Met provisionally at frame level.** The frame gives unit, day and lesson perspectives and requires later verification of minutes. Its provisional allocation is not completed lesson-level evidence. |
| Supporting clusters practise major work | **Met.** Data, money, time and equal-group work have named arithmetic connections. |
| Every source-map row has a decision | **Met.** Retained, cut and added work is identified. |

The focus interpretation correctly includes supporting work connected to major work. The applicable K to 2 threshold and the need to consider multiple perspectives are confirmed in the [evidence guide, PDF pages 13 to 15](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf).

The related progression checks found no unlabelled ownership duplication, premature standard algorithm, or model introduced after first use. Scope-and-sequence, unit-assessment and day-level checklist lines are not applicable to this frame review.

## Earlier findings and what should be preserved

The earlier substantive Grade 2 review’s five findings have been addressed: the cuts now have a day-budget reason, lesson 3.17 is restored, the tape-diagram handoff is clarified, science timing is corrected, and the partition-language requirement is expanded. Those settled findings are not reopened.

Preserve:

- The nine-unit order and ruler-to-number-line progression.
- Early subtraction with and without decomposing, and the explicit across-zero lesson.
- Spaced fluency practice and observation-based untimed checks.
- Paper access and the safeguards around surveys, money and pairing children.

The two comparison curricula support the broad emphasis and progression without requiring identical boundaries: [Fishtank Grade 2](https://www.fishtanklearning.org/curriculum/math/2nd-grade/) and [Eureka’s curriculum overview, Grade 2 beginning on PDF page 25](https://greatminds.org/hubfs/3454910/knowledge/resources/math/EM_Basic_Curriculum_Files/Curriculum_Overview/EM_GPK5_CurriculumOverview.pdf).

## Settled by the expert

| Choice | Reason | File touched by a later fixer |
|---|---|---|
| Include above-100 four-addend totals in required Unit 2 work | Restores the existing owned standard | Grade 2 frame, Unit 2 |
| Use 25 + 35 + 45 + 15 = 120 as an illustrative case | All four addends are two-digit; grouping exposes structure | Grade 2 frame, Unit 2 |
| Assign MP2 and MP5 to Unit 4, anchored in base lesson 2.4.13 | Uses retained content; MP7 remains elsewhere | Grade 2 frame, Unit 4 |
| Make the production requirements in Finding 2 explicit | Prevents interpretation-only teaching from satisfying the summaries | Grade 2 frame, Units 1, 3 and 6 |
| Retain unit order and day allocations | No identified correction requires moving ownership or days | Grade 2 frame and `frames.csv` |

## For Cory

No new scope decision is required by these findings. Existing audience, people and money questions remain:

- Whether the planned 60-minute daily course also needs a shorter-period path.
- Who, and any pay, for the saree-silk context reader.

## Limits and sources

This review cannot establish whether warm-ups absorb every displaced center activity, whether observations reach every child within the available minutes, or whether the finished assessments cover every standard. Those require unit plans, assessment instruments and classroom evidence.

The 2023 consolidated Progressions PDF exceeded the web tool’s size limit. I used the authors’ earlier [K to 5 Base Ten progression, 2015 draft](https://community.ksde.org/Portals/54/Documents/Standards/Standards_Review/Linked_Files/Numbers_and_Operations_Base_10_Progression_K-5.pdf) for the relevant comparison, alongside the current repository records. I did not treat it as a fresh verification of every 2023 page citation.

Additional sources consulted:

- [Grade 2 base-text scope and sequence](https://im.kendallhunt.com/k5/teachers/grade-2/course-guide/scope-and-sequence.html): unit purposes and order.
- [Official mathematics standards](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf): content demands and practices.
- [K to 8 Publishers’ Criteria](https://achievethecore.org/content/upload/Math_Publishers_Criteria_K-8_Spring_2013_FINAL.pdf): coherence and practice-content connections.
- [Federal elementary mathematics intervention guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/26): representations, mathematical language and deliberate word-problem teaching. Its intervention context does not establish the effectiveness of this whole course.

No curriculum finding rests on memory. Prior memory informed only the read-only review workflow.

**For the source list:** Add the reachable 2015 progression address and Grade 2 Fishtank course page if they are useful for later reads.

**Final disposition: revise, 7 findings. Intended report path: `docs/reviews/frame-math-grade-2-2026-11-14.md`, supplied here only.**


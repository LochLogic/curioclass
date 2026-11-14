# Expert cold read: Grade 1 Math course frame

**Date:** 2026-11-14  
**Intended report:** `docs/reviews/frame-math-grade-1-2026-11-14.md`  
**Delivery:** Complete report below. No files changed.

## Verdict

The mathematical sequence is sound, but the frame needs revision before unit planning. Its largest risk is treating a complete-looking summary as sufficient evidence for lesson coverage, assessment capacity and instructional time. Complete the required source map, justify the assessment allocation, and repair the cross-subject and stale-status notes while preserving the unit order.

## What I read and checked

- `docs/agents/EXPERT.md`, the mathematics lens and `docs/RUBRIC-MATH-K8.md`.
- The foundation, shared and mathematics approaches, relevant source-register entries, Roadmap requirements, BASELINE rules 20 to 24, glossary and production-path requirements.
- The complete Grade 1 mathematics frame, its `frames.csv` row, all 26 Grade 1 progression rows and all 24 Grade 1 standard and substandard entries.
- Kindergarten and Grade 2 mathematics frames, including their seams and models.
- Relevant Grade 1 ELA, science and social studies frame passages and progression rows.
- The base-text record, all 146 Grade 1 lesson-preparation records for counts and standard tags, and targeted lesson narratives.
- Earlier mathematics progression reviews and fixes, relevant frame reviews and cross-subject findings.
- Outside sources linked below.

The requested `data/plans/math-grade-1/source-map.csv` does **not exist**.

### Checks

| Check | Result |
|---|---|
| Requested repository-wide `plan.py check` | Initially stopped because the default interpreter lacks `markdown` |
| Repository-wide check using the import workaround below | Exit 0, zero failures |
| `plan.py check math-grade-1` | Zero failures, but zero items checked |
| `frame.py check math-grade-1` | Zero failures |
| `progression.py check math` | 305 rows, zero failures |
| `stale.py check` | 41 files, zero failures |

The workaround supplied an in-memory `markdown` module whose rendering function raises if called. The complete checker ran without calling it. No checking function was changed, no check was skipped, and no dependency or file was installed.

A passing frame gate establishes placement and arithmetic. It does not establish the substantive claims examined below.

## Findings, most serious first

### 1. The required lesson-level source map is missing

**LAYER:** base text  
**REPEAT:** new  
**Severity:** substantial planning gap  
**Confidence:** firm

**What is wrong:** The frame’s source-map table groups lessons into eight ranges, while the required CSV is absent. `docs/PRODUCTION-PATH.md`, step 2, explicitly requires every base lesson to be mapped at the frame layer. Frame lines 183 to 184 defer the day-level map without distinguishing that later work from the lesson-to-unit inventory required now.

The ranges account for all 146 lessons, so I found no missing base lesson in the prose inventory. However, there is no individual record carrying each lesson’s title, goals, standards and decision.

**Why it matters:** A later writer cannot reliably audit individual lessons, distinguish substantive coverage from warm-up tags, or record adaptations against the approved edition.

**Exact fix:** Create `data/plans/math-grade-1/source-map.csv` with one row for each of these lessons:

| Base unit | Lessons | Curio Class unit |
|---|---:|---:|
| 1 | 1 to 15 | 1 |
| 2 | 1 to 22 | 2 |
| 3 | 1 to 28 | 3 |
| 4 | 1 to 23 | 4 |
| 5 | 1 to 14 | 5 |
| 6 | 1 to 17 | 6 |
| 7 | 1 to 17 | 7 |
| 8 | 1 to 10 | 8 |

Use the existing schema, record `keep` for each retained lesson, and identify the first-edition source. Keep exact course-day assignment for the scope and sequence. Rewrite the frame’s deferral sentence:

> The lesson-to-unit inventory is in data/plans/math-grade-1/source-map.csv. The scope and sequence assigns its course days and records the additional assessment, check and respond days.

### 2. Assessment time is reduced from the base allocation without a reason

**LAYER:** base text  
**REPEAT:** yes, assessment-capacity concerns in `math-4-spine-2026-11-11.md`, finding 1  
**Severity:** moderate  
**Confidence:** firm on the difference; judgment call on sufficiency

**What is wrong:** Each unit receives its base lesson count plus **one** assessment day. The base text’s pacing guidance includes **two assessment days per unit**. The frame explains replacing unavailable assessments with original assessments, but does not explain reducing their time. [Base-text pacing guidance](https://im.kendallhunt.com/k5/teachers/grade-1/course-guide/pacing-guide-and-dependency-diagram.html).

Across eight units, that is eight fewer assessment days than the base allocation.

**Why it matters:** First-grade evidence includes oral explanations, manipulation and observed fluency. A written assessment fitting one period does not establish that the teacher can collect the necessary individual evidence.

**Exact fix:** Add an explicit assessment adaptation rationale. Require each unit plan to identify:

- What is collected during the assessment day.
- What individual evidence is collected during preceding lessons.
- Teacher observation minutes and how every child is reached.
- Coverage of every owned standard.

State that these original assessments replace the base assessment allocation. If that evidence cannot fit, return the additional-day requirement to Cory before fixing the scope and sequence. Do not cut standards to preserve the current total.

### 3. Two cross-subject links misdescribe their role

**LAYER:** progression  
**REPEAT:** yes, inaccurate lean descriptions in `progression-math-2026-11-13.md`, finding 6  
**Severity:** moderate  
**Confidence:** firm

**What is wrong:**

1. Frame line 150 and `m1-add-take-problems.cross_subject` describe **SL.1.2** as retelling. That standard concerns asking and answering questions about key details in orally presented information. The ELA progression correctly distinguishes it from story retelling. [Official speaking and listening standards](https://www.thecorestandards.org/ELA-Literacy/SL/1/).

2. Frame line 157 and `m1-data-three-categories.cross_subject` describe **1-ESS1-2** as organizing observations into three groups. Its substantive expectation concerns seasonal daylight comparisons. Science’s frame places the completed comparison in unit 8, around week 31. It is a later application of mathematics taught in unit 1, not preparation supplied to mathematics in week 2. [Official science standard](https://www.nextgenscience.org/pe/1-ess1-2-earths-place-universe).

**Why it matters:** These descriptions can make the availability calendar appear to establish prerequisites that the named standards do not supply.

**Exact fix:**

- Change the literacy link to:

  > ela:e1-key-details (SL.1.2: ask and answer questions about key details of a problem read aloud)

  Preserve teacher-modeled retelling as a mathematics comprehension routine. Do not require the central-message work of ELA’s retelling standard.

- Describe `s1-daylight-seasons` as a **later application** of unit 1’s data work. Remove it from the mathematics prerequisite table and retain it in the reciprocal table showing what science uses from mathematics.
- Make the same corrections in the progression’s cross-subject cells.

No owned standard needs to change grade or unit.

### 4. The major-work calculation lacks an instructional-time perspective

**LAYER:** frame  
**REPEAT:** yes, multiple-perspective focus accounting discussed in `math-4-spine-2026-11-11.md`  
**Severity:** moderate evidence gap  
**Confidence:** firm

**What is wrong:** Lines 15 to 18 report units, days and base lessons carrying a major-cluster tag. Because one lesson equals one day, the latter two do not establish an independent instructional-time calculation.

The evidence guide specifically requests minutes when a lesson equals a day. Standard tags alone also do not show how much time addresses that standard. For example, geometry lessons can carry major-work tags through number warm-ups. [Evidence guide, PDF pages 14 to 15](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf#page=14).

**Why it matters:** The course appears comfortably focused, but the reported three-way calculation overstates what has been demonstrated.

**Exact fix:** Retain the unit and lesson inventories. Add estimated minutes by lesson component, including assessments, and identify supporting work that substantively develops major work. Distinguish standards addressed from standards merely built on or anticipated.

Until that exists, label **133/160 days** as a provisional allocation estimate and **137/146 lessons** as a tag inventory. Do not change the sequence merely to increase either percentage.

### 5. The cross-subject introduction says existing frames will be written later

**LAYER:** process  
**REPEAT:** yes, stale planning-state notes in earlier frame reviews  
**Severity:** minor  
**Confidence:** firm

**What is wrong:** Frame lines 143 to 144 say the other subjects’ frames are written later. Grade 1 ELA, science and social studies frames now exist.

**Why it matters:** The note presents an available comparison as future work and obscures which timings have actually been checked.

**Exact replacement:**

> Grade 1 ELA, science and social studies frames are available. The tables below compare their current unit placements with mathematics. Exact within-unit timing remains for the scope and sequence; a named bridge supplies any skill needed earlier.

Retain the existing length bridges and apply finding 3’s corrections.

### 6. The mathematics lens still describes completed handoff work as missing

**LAYER:** process  
**REPEAT:** yes, stale-status findings in earlier progression and frame reads  
**Severity:** minor  
**Confidence:** firm

**What is wrong:** Lens lines 61 to 62 say progression pages exist only for grades 3 to 5 and that other bands need the same handoff work. `data/progressions/math.csv` now supplies ownership, handoffs, models, limits and notes through grade 11. The earlier mathematics review itself records this gap as addressed.

**Why it matters:** Readers can repeat completed structural work instead of examining the remaining course-level questions.

**Exact replacement:**

> data/progressions/math.csv now records core mathematics ownership, handoffs, models and limits from kindergarten through grade 11. The grades 3 to 5 narrative remains a supplementary explanation. Course frames check these handoffs against actual unit order.

This does not claim that equivalent narrative essays exist for every band.

### 7. The lens still says untimed K to 2 checking has no explanation

**LAYER:** process  
**REPEAT:** yes, already identified in the Kindergarten mathematics frame’s lead item 4  
**Severity:** minor  
**Confidence:** firm

**What is wrong:** Lens lines 65 to 66 say there is no page explaining untimed checking. The three K to 2 mathematics frames now describe observation in games and individual checks, with records distinguishing known facts, quick strategies and counting.

**Why it matters:** The stale gap can trigger duplicate work and hide the actual remaining need: usable assessment instruments.

**Exact replacement:**

> The K to 2 mathematics frames describe untimed fluency checks through games and individual observation. Unit plans must turn these descriptions into tasks, recording guidance and response decisions. Counting checks are separate from arithmetic-fluency checks.

### 8. The earlier mathematics review retains an outstanding-work statement now fulfilled

**LAYER:** process  
**REPEAT:** yes, stale review-status notes in earlier frame reads  
**Severity:** minor  
**Confidence:** firm

**What is wrong:** `docs/reviews/progression-math-2026-11-13.md:205` says the fluency how-to page remains for the course frames. Those frames now contain the promised explanation.

**Why it matters:** A later worker following the review can mistake a completed handoff for unfinished work.

**Exact fix:** Preserve the historical finding and add this dated closure annotation:

> Update, 2026-11-14: The Kindergarten, Grade 1 and Grade 2 mathematics frames now describe untimed fluency observation and recording. The frame-level explanation is complete; unit-level tasks and recording instruments remain to be written.

## Ownership, standards, order and days

All **26 Grade 1 skills** are placed exactly once. The progression owns all **24 standard and substandard entries**, representing 21 numbered standards plus the three lettered parts of 1.NBT.B.2.

Reading the frame together with its progression notes and retained base lessons, I found no established substantive omission from a Grade 1 standard. Full implementation and assessment coverage remain unverified. Preserve explicit requirements that short frame summaries compress: numeral-to-collection matching, explained mental changes of ten, zero differences when subtracting tens, describing a whole as two halves or four fourths, and both telling and writing clock times. [Number and base ten](https://www.thecorestandards.org/Math/Content/1/NBT/), [measurement and data](https://www.thecorestandards.org/Math/Content/1/MD/), [geometry](https://www.thecorestandards.org/Math/Content/1/G/).

| Unit | Days | Owned skills | Judgment |
|---|---:|---:|---|
| 1. Adding, subtracting and data | 16 | 2 | Reasonable opening and connected data work |
| 2. Story problems | 23 | 5 | Substantial language and equation load justifies the allocation |
| 3. Adding and subtracting within 20 | 29 | 5 | Correctly receives the largest allocation |
| 4. Numbers to 99 | 24 | 4 | Appropriate depth before adding within 100 |
| 5. Adding within 100 | 15 | 2 | Reasonable after unit 4’s preparation |
| 6. Length to 120 units | 18 | 4 | Coherent measurement, counting and problem-solving connections |
| 7. Geometry and time | 18 | 4 | Reasonable; halves precede half-hour clocks |
| 8. Putting it together | 11 | 0 | Legitimate cumulative review unit |

No unit is demonstrably far over or under its share. The **154 unit days plus six course-check and respond days total 160**. In a 180-day calendar, that leaves 20 days for interruptions and flexibility. Finding 2 concerns assessment feasibility within that allocation.

The source lesson counts and unit edges follow the first edition. The prose names the permitted edition; no reference-only material is proposed for adaptation. The missing CSV prevents a completed mapping audit.

## Seams and cross-subject availability

The Kindergarten handoffs are picked up, and Grade 2’s receiving frame agrees with this course’s outgoing seam. Preserve the distinction between Kindergarten’s ten ones and Grade 1’s unit called a ten, introduced before broader place-value computation. [Base lesson introducing ten as a unit](https://im.kendallhunt.com/k5/teachers/grade-1/unit-3/lesson-8/preparation.html).

Preserve Grade 1 opportunities to solve and discuss difficult start-unknown and opposite-language comparison problems, with proficiency continuing into Grade 2. Late Grade 1 tape diagrams are appropriate. [Operations progression, PDF pages 12 to 14](https://commoncoretools.files.wordpress.com/2011/05/ccss_progression_cc_oa_k5_2011_05_302.pdf#page=12), [late-year comparison lesson](https://im.kendallhunt.com/k5/teachers/grade-1/unit-6/lesson-12/preparation.html).

| Connection | Availability judgment |
|---|---|
| ELA key-detail questions for mathematics unit 2 | ELA unit 1 teaches the skill; exact early timing is protected by mathematics modeling it |
| ELA questions for mathematics unit 6 | ELA unit 1 precedes the need |
| Mathematics data for science and voting | Mathematics unit 1 precedes the substantive later uses |
| Science leaf ordering around week 11 | Earlier than mathematics unit 6; retain science’s direct-comparison bridge |
| Science length-unit measurement around week 24 | Near mathematics unit 6’s introduction; sequence the lessons explicitly or use science’s local teaching bridge |
| Number comparison and story problems for social studies weeks 27 to 28 | Mathematics teaches them beforehand |

The alternative open curriculum’s sequence also supports the central importance of ten as a unit and continued fluency practice across other topics. Its different placement of measurement is not evidence that this frame’s order is wrong. [Curriculum overview, PDF pages 16 to 17](https://greatminds.org/hubfs/knowledge/resources/math/EM_Basic_Curriculum_Files/Curriculum_Overview/EM_GPK5_CurriculumOverview.pdf#page=16).

## Lens checklist: course-frame layer

| Lens line | Mark | Evidence |
|---|---|---|
| Major work reaches the K to 2 line | **Met provisionally; time evidence incomplete** | Allocation suggests sufficient focus; finding 4 |
| Supporting work practices major work | **Met** | Data develops counting and comparison; number practice continues during geometry |
| Every source-map row has a decision | **Missed** | Required lesson-level file absent; finding 1 |
| Earlier-grade dependencies and model order | **Met** | Counting, ten-frames, ten as a unit and later diagrams form a coherent sequence |
| No premature standard algorithm or unexplained grade ownership | **Met** | Strategies precede algorithms; later-grade examples are labeled extensions |
| Standards completed rather than merely tagged | **Met at frame level** | Checked against progression descriptions and retained lessons |
| Problems join units deliberately | **Met at frame level** | Measurement joins counting, comparison and story problems |
| Fluency receives spaced practice | **Met** | Warm-ups and games continue through the year |
| All eight mathematical practices | **Met at frame level** | All eight have candidates; actual tasks belong in unit plans |
| Unit rigor balance and assessment-item alignment | **Not applicable yet** | Requires unit plans and assessments |
| Day goals, exits, model-to-writing links and timer behavior | **Not applicable yet** | Requires lesson artifacts |
| High-school bar and post-Algebra II source gaps | **Not applicable** | Outside this course |
| K to 2 progression and untimed-checking gaps | **Work present; notes stale** | Findings 6 to 8 |

## Settled by the expert

| Choice | Reason | File touched by the eventual fix |
|---|---|---|
| Preserve the eight-unit order | Dependencies and base sequence agree | Grade 1 frame |
| Preserve unit 8 as cumulative review | Owning no new skill does not invalidate a review unit | Grade 1 frame |
| Use `e1-key-details` for the SL.1.2 link | Matches the actual literacy operation | Mathematics progression and frame |
| Treat seasonal daylight data as a later application | Mathematics supplies the data method first | Mathematics progression and frame |
| Retain the length bridges | Avoids moving standards solely to align subject calendars | Mathematics and science frames |
| Preserve observed, untimed fluency checking | Appropriate course policy; do not claim that research proves timing is universally harmful | Grade 1 frame |

## What is right and should not be touched

- Ten as a unit precedes broader place-value computation.
- Equality and unknowns are treated as mathematical relationships.
- Fluency within 10 is distinguished from strategies within 20.
- Measurement remains major work.
- Paper and physical materials provide a complete route.
- Context notes avoid personal financial and family disclosure.

## What I could not judge

Actual lessons, assessment instruments, individual observation capacity and instructional-minute totals are not available for certification.

The compiled 2023 Progressions PDF exceeded the web tool’s size limit. I read accessible earlier operations and measurement drafts for the relevant qualitative claims. Base-ten and geometry progression downloads were unsuccessful, so I did not independently verify the frame’s page pointers into those documents.

No curriculum finding rests on memory. Prior local memory informed review procedure only.

## Sources

Alongside the sources linked at the relevant findings:

- [Grade 1 operations standards](https://www.thecorestandards.org/Math/Content/1/OA/): complete problem-solving, strategy, fluency and equation expectations.
- [K to 8 Publishers’ Criteria](https://achievethecore.org/content/upload/Math_Publishers_Criteria_K-8_Spring_2013_FINAL.pdf): focus, coherence and rigor.
- [Measurement progression](https://commoncoretools.files.wordpress.com/2012/07/ccss_progression_gm_k5_2012_07_21.pdf): direct and indirect comparison and iterated units.
- [Federal mathematics intervention guide](https://ies.ed.gov/ncee/wwc/practiceguide/26): systematic instruction, mathematical language, representations and deliberate word-problem teaching. Its intervention setting limits generalization to whole-class policy.

## For the source list

The official standards pages were reachable at `www.thecorestandards.org`. The university’s [progressions index](https://archive.math.arizona.edu/ime/progressions/) supplied accessible older operations and measurement drafts when the compiled document could not be opened.

## For Cory

- Confirm the proposed 60-minute daily, 160-day course allocation.
- If the assessment-capacity check requires additional days, decide the timetable allowance before the scope and sequence fixes the year.

**Verdict:** Sound mathematical sequence; revise before unit planning. **Findings:** 8. **Report path:** `docs/reviews/frame-math-grade-1-2026-11-14.md`, supplied above, not written.


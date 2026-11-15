# Independent sequence review: Kindergarten Math

**Date:** 2026-11-15  
**Intended report path:** `docs/reviews/sequence-math-kindergarten-2026-11-15.md`  
**Delivery:** Complete report supplied here. No files written.  
**Role:** Independent first reader for this run, before the expert.

## Verdict

The sequence is mathematically sound overall, with coherent unit arcs, complete planned ownership, and appropriate kindergarten limits. Its main weakness is that unit 2 begins collecting mid-unit evidence before all its assessed performances have received their named instruction. Revise that window and remove the obsolete frame notes before treating the sequence as settled.

**Finding count: 2.**

## What I read

- `docs/agents/EXPERT.md`, the math lens, and `docs/RUBRIC-MATH-K8.md`.
- The foundation, shared and mathematics approaches, relevant source-register entries and evidence notes, roadmap provisions, baseline rules 20 to 24, glossary, and sequence-writing rules.
- The complete kindergarten scope and sequence, all 160 day rows, the frame, and all 161 source-map rows.
- All 20 kindergarten mathematics progression rows and the grade 1 assumptions receiving their handoffs.
- Kindergarten standards, lettered parts, cluster classifications, `CALENDAR.md`, and kindergarten calendar rows across all four subjects.
- The two earlier kindergarten math frame reports, relevant kindergarten sequence findings, and readiness-timing and K to 2 sequence-fix records.
- Outside sources linked below, including two curricula and selected base lessons.

The blind boundary was respected. Memory supplied procedural reminders only; no curriculum finding rests on memory.

## Gates

The repository-wide `plan.py check` stopped because the environment lacks the Python `markdown` package; this does not withhold the verdict.

| Check | Result |
|---|---|
| `python -X utf8 scripts/frame.py calendar` | Passed; kindergarten math checks remain in weeks 17 and 31 |
| `python -X utf8 scripts/frame.py check math-kindergarten` | 0 failures |
| `python -X utf8 scripts/plan.py check math-kindergarten` | 0 failures |
| `python -X utf8 scripts/sequence.py check math-kindergarten` | 0 failures |
| `python -X utf8 scripts/stale.py check` | 56 files, 0 failures |

No turn, build, sync, defect-writing, or Git mutation command was run.

## Findings, most serious first

### 1. Unit 2 starts its mid-unit assessment before the full assessed work is taught

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** new, this specific assessment-before-instruction problem was not identified in the earlier reports examined  
**Confidence:** Firm on the ordering; likely on its classroom consequences

**Location:** Scope and sequence, unit 2 and “Observation windows”; `days.csv`, days 30 to 35.

**What is wrong:** Days 30 and 31 each assess ten assigned children. The closing description on day 32 requires counting out requested sets, cardinality after rearrangement, and writing 0 to 10, including zero. But day 32 is the named count-out lesson, day 33 explicitly introduces the empty-group work, and day 34 is the named full-range writing lesson.

The base text does provide writing practice in lesson K.2.12, mapped to day 30. Therefore, writing is not wholly absent before the assessment. However, that center practises 1 to 10, and it does not establish the complete zero-inclusive assessment target. The base text separately identifies K.2.14 as its count-out lesson and K.2.16 as its quantity-writing lesson. [Early writing center](https://im.kendallhunt.com/k5/teachers/kindergarten/unit-2/lesson-12/lesson.html), [count-out lesson](https://im.kendallhunt.com/k5/teachers/kindergarten/unit-2/lesson-14/preparation.html), [quantity-writing lesson](https://im.kendallhunt.com/k5/teachers/kindergarten/unit-2/lesson-16/preparation.html).

Counting out also requires remembering a stopping quantity, beyond counting an existing collection. The Progressions explicitly distinguish these demands. [Counting and operations Progressions, PDF page 4](https://commoncoretools.files.wordpress.com/2011/05/ccss_progression_cc_oa_k5_2011_05_302.pdf).

**Why it matters:** The first twenty children can be recorded as needing response on performances whose explicit lessons are still ahead. Different children consequently receive different opportunities to learn before the same assessment record is completed.

**Exact fix:**

- Move the mid-unit observation window to **days 34 to 36**, beginning after day 34’s instruction.
- Move `assess = mid` from day 32 to **day 36**.
- Retain independent numeral products, including zero, and use the individual turns for counting out and cardinality.
- Move the two ten-minute response slots to **days 37 and 38**.
- Remove the old observation and response instructions from days 30 to 34. Update day 35’s note so practice uses emerging observations rather than a supposedly completed mid-unit record.
- Update the scope’s window and response references.

This preserves the 26-day unit, the base lesson order, the assessment’s coverage, and the final window on days 40 to 44. The later midpoint is justified by the complete target becoming available.

### 2. The frame still presents completed documentation work as outstanding

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale-status findings recur in both earlier kindergarten math frame reports  
**Confidence:** Firm

**Location:** `frame.md`, “For the lead,” item 4, and the source-map introduction.

**What is wrong:** Item 4 still says the math lens claims there is no page explaining untimed K to 2 checks and no progression work beyond grades 3 to 5. The current lens already contains the replacement descriptions.

The source-map introduction also presents the day-level map as forthcoming, although `data/plans/math-kindergarten/source-map.csv` now exists.

**Why it matters:** A later writer is directed toward completed repairs and can mistake available planning evidence for unfinished work. The stale-note gate does not detect these statements.

**Exact fix:** Replace item 4 with a dated completion note, or remove the resolved action. Replace the source-map’s future wording with a direct pointer to the existing CSV. Preserve the historical reviews unchanged.

## Coverage, order, and load

### Unit arcs

| Unit | Allocated days | Judgment |
|---|---:|---|
| 1 | 18 | Appropriate foundation in tools, routines, matching, tracking, and explaining a count |
| 2 | 26 | Its five owned rows justify the longest allocation; repair the mid-unit window |
| 3 | 19 | Shape recognition precedes construction and composition; direct comparisons form a coherent arc |
| 4 | 20 | Meaning precedes stories and symbolic recording |
| 5 | 17 | Decomposition supports both-addends-unknown stories and partners of ten |
| 6 | 16 | Counting, teen structure, representations, and written numerals build coherently |
| 7 | 15 | Six lessons reconnect number work and composition before nine lessons on solids and assessment |
| 8 | 22 | Seventeen days before the check and five review days consolidate counting and fluency |

No unit is clearly far over or under its load. Unit 1’s single owned row does not make its 18 days excessive: classroom routines and reliable counting underpin the year. Units 3 and 7 together occupy 34 days, but unit 7 includes six deliberate connections to earlier number work.

### Standards and assessments

No additional missing kindergarten standard or lettered part was found at this planning layer.

| Content | Planned completion and evidence |
|---|---|
| Counting and cardinality | One-to-one record in unit 1; cardinality, one more, comparison, and partial numeral/counting ranges in unit 2; full range in unit 6; oral sequence in unit 8 |
| Operations | Representations and initial stories in unit 4; explicit continuation and retained story evidence in unit 5; spaced fluency through unit 8 |
| Teen structure | Unit 6 includes composition, decomposition, language, and recorded representations |
| Measurement and sorting | Several attributes of one object, direct comparisons with descriptions, and all three sorting steps are named |
| Geometry | Environmental naming, six position words, varied sizes and turns, building, drawing, composing, and flat/solid comparison have named evidence |

Unit 4 explicitly postpones both-addends-unknown story completion to unit 5 and names its assessment there. That continuation is visible rather than hidden behind a code.

Unit 2 is the only unit exceeding 25 days and has the required mid-unit slot. Response time is otherwise identified once, including unit 4’s same-day response and unit 8’s course-level response.

### Readiness and retrieval

There are **no assumed earlier-grade progression rows**, so there is no last-use grade requiring a readiness check.

Same-year retrieval is present on the opening days of units 2 to 8: days **19, 45, 64, 87, 104, 120, and 135**. No unit incorrectly checks a year-before row, retrieves an older-grade row, or places a readiness check on its first day.

### Course-level checks and calendar

The mid-year check explicitly draws unit 4 contexts from earlier collections, comparisons, and composed shapes. It reuses recent individual story and equation evidence instead of collecting it again.

The year-end check similarly carries forward unit 8’s counting and fluency record. Its fresh work concerns earlier units and uses a separately reserved task form.

The baseline calendar agrees with the write-up:

- Math checks: days **84 to 85**, week **17**, and **152 to 153**, week **31**.
- Nearest ELA check days: **78** and **158**, giving the stated six-day and five-day gaps.
- ELA sorting and read-aloud work precede their math uses.
- Weather and ramps overlap the relevant math teaching, with the stated bridges.
- Math’s position lesson on day 45 precedes the social studies map unit beginning on day 47.

### Candidates, shorter path, and source map

Every candidate cell is settled. Retained student extensions have explicit costs of five or ten minutes within existing centers; dropped extensions have reasons. Teacher preparation costs zero student days.

The shorter path supplies a 55-minute route and ten named fold-ins. All ten fold-in days have blank assessment markers, and their work remains in named neighboring lessons. The text correctly distinguishes losing ten math meetings from adopting an entirely shorter school calendar.

The source map contains **137 base lessons: 136 retained and one cut**, plus 24 original slots. Every course day has exactly one placed map row. The position, measurement, and ten-frame adaptations have stated reasons; remaining base lesson order is preserved.

## Math lens checklist: scope and sequence

| Lens line | Result |
|---|---|
| Every owned standard is carried through to completion | **Met at planning level**, with the assessment-timing correction in finding 1 |
| Problems deliberately connect units | **Met**, especially shape compositions with operations and the cumulative checks |
| Fluency receives spaced, mixed practice | **Met**, daily addition and subtraction practice from day 71 |
| All eight practices have named tasks and evidence | **Met at planning level** |
| Supporting work practises major work | **Met**, through category counts, counted pieces, equations, and stories |
| Major-work emphasis is demonstrated | **Met as a provisional reservation:** 7,700 of 9,600 minutes, or 80.2 percent |
| K to 2 counting and arithmetic fluency are checked separately | **Met**, distinct performances and strategy records without a student timer |
| Models and limits follow the progression | **Met** |
| High school and past-Algebra-2 provisions | **Not applicable** |

The practice assignments are concrete: tracking-tool choice for MP.5, precise counting and comparison for MP.6, comparison arguments for MP.3, story models for MP.4, quantities and symbols for MP.2, structural reasoning for MP.7, complementary-part and counting patterns for MP.8, and revised story representations for MP.1.

The major-work reservation addresses the earlier frame review’s missing time calculation. Actual lesson-part minutes still need verification during unit planning. The evidence guide supports examining instructional time alongside other perspectives. [Mathematics evidence guide, indicator 1e](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf).

## What is right and should remain

- The unit order and explicit reasons for departures from the base text.
- Daily counting, sustained arithmetic practice, and untimed individual evidence.
- Connected objects, drawings, and symbols, including total-left equations.
- Explicit partial-range completion and later story-problem continuation.
- Reuse of recent assessment records.
- Paper alternatives and protections against compulsory personal disclosure.

## Settled by the expert

These are item-level recommendations for the caller to apply.

| Choice | Reason | Files affected |
|---|---|---|
| Mid-unit 2 window on days 34 to 36; close on day 36 | Full assessed instruction is available before observation | Scope and sequence; `days.csv` |
| Mid-unit response on days 37 and 38 | Preserves two response slots without adding days | Scope and sequence; `days.csv` |
| Retain unit allocations and base lesson order | The problem is assessment placement | Same files |
| Remove obsolete frame action notes and link the existing source map | Makes the handoff current | `frame.md` |

## For Cory

- None required for these corrections. They preserve scope, audience, money, people, ownership, and annual time.

## What I could not judge

This sequence contains no finished assessment items, keys, or child-by-child record sheets. Their quality and actual completion time remain unit-plan checks.

The unit 8 four-minute turns are planning estimates, not classroom timing evidence. They are not demonstrably impossible: other children can practise independently while the teacher observes. Actual throughput still needs verification.

## Outside sources and limits

- [Official mathematics standards](https://learning.ccsso.org/wp-content/uploads/2022/11/Math_Standards1.pdf): kindergarten requirements and grade boundaries.
- [Counting and operations Progressions](https://commoncoretools.files.wordpress.com/2011/05/ccss_progression_cc_oa_k5_2011_05_302.pdf): distinct counting demands and kindergarten story types. The compiled 2023 PDF exceeded the retrieval limit; this accessible earlier draft was used.
- [K to 8 Publishers’ Criteria](https://achievethecore.org/content/upload/Math_Publishers_Criteria_K-8_Spring_2013_FINAL.pdf): focus, coherence, and progression.
- [Mathematics evidence guide](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf): instructional emphasis and full-intent evidence.
- [Base curriculum’s kindergarten sequence](https://im.kendallhunt.com/k5/teachers/kindergarten/course-guide/scope-and-sequence.html): unit purposes and order.
- [Second curriculum’s overview, kindergarten pages 9 to 11](https://greatminds.org/hubfs/knowledge/resources/math/EM_Basic_Curriculum_Files/Curriculum_Overview/EM_GPK5_CurriculumOverview.pdf): independent comparison of number, operations, measurement, and teen-number sequencing.
- [Teaching Math to Young Children](https://ies.ed.gov/ncee/WWC/PracticeGuide/18): developmental progression and progress monitoring. It does not validate this plan’s exact pacing.

**For the source list:** Add the direct K.2.12 writing-center and K.2.14 preparation links used in finding 1 as timing evidence.

**Final verdict:** Revise the unit 2 assessment window, then proceed to unit planning. **Findings:** 2. **Report path:** `docs/reviews/sequence-math-kindergarten-2026-11-15.md`, delivered here only.


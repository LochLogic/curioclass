# Independent cold read: Grade 1 Math scope and sequence

**Date:** 2026-11-15  
**Intended report path:** `docs/reviews/sequence-math-grade-1-2026-11-15.md`  
**Delivery:** Complete report supplied here. No files changed.

## Verdict

The sequence is mathematically coherent, but needs three targeted corrections before unit planning. The largest risk is the claim of complete equal-sharing assessment evidence when the named observation schedule does not establish every part for every child. Preserve the unit order and day allocations, repair that evidence gap, constrain day 114’s subtraction goal, and update the stale notes.

## What I read

- `docs/agents/EXPERT.md`, the mathematics lens, `docs/RUBRIC-MATH-K8.md`, the foundation, shared and mathematics approaches, relevant source-register entries, Roadmap requirements, BASELINE rules 20 to 24, glossary, and sequence-writing rules.
- The complete Grade 1 mathematics scope and sequence, all 160 daily rows, its frame, frames inventory row, and all 160 source-map rows.
- All 26 Grade 1 progression rows and the kindergarten prerequisite rows, alongside the complete Grade 1 standards.
- `docs/courses/CALENDAR.md` and the Grade 1 calendar entries across subjects.
- The kindergarten daily file’s assessment entries for all 20 prerequisite rows. That file is now present.
- Both earlier Grade 1 mathematics frame reviews, the relevant frame-fixes record, and the sequence writer’s handoff.
- The outside sources linked below, including two curriculum sequences and targeted base lessons.

The prohibited files were not opened. Prior local memory informed report procedure only; no curriculum finding rests on memory.

## Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Did not finish: the environment lacks the `markdown` dependency. |
| `python -X utf8 scripts/frame.py calendar` | Passed; Grade 1 mathematics checks remain in weeks 19 and 30. |
| `python -X utf8 scripts/frame.py check math-grade-1` | Passed: eight units, 160 days, including 153 unit days and seven course-level check/respond days. |
| `python -X utf8 scripts/stale.py check` | Passed: 56 files, zero failures. Manual stale findings remain below. |

## Findings, most serious first

### 1. The first half of the class lacks named evidence for the final part of 1.G.A.3

**LAYER:** sequence  
**REPEAT:** yes, incomplete standard coverage, also identified in the earlier Grade 1 frame review, finding 3  
**Severity:** substantial  
**Confidence:** firm

**Location:** `days.csv`, days 138 to 140 and 146 to 148; scope and sequence, unit 7.

**What is wrong:** Day 138 collects the first half of the class’s explanations about partitioning, share names, and describing the whole. Day 139 then teaches why more equal shares produce smaller pieces. Day 140 collects the remaining half’s explanations, explicitly including that final relationship.

No day names a retained comparison product or later observation establishing the final relationship for the children already heard on day 138. Nevertheless, the closing and course-level records claim complete 1.G.A.3 coverage.

This relationship is an explicit standard requirement, and the retained base sequence places its focused teaching after the first observation: [Grade 1 geometry standards](https://www.thecorestandards.org/Math/Content/1/G/), [base lesson 7.11](https://im.kendallhunt.com/k5/teachers/grade-1/unit-7/lesson-11/preparation.html).

**Why it matters:** Half the class can receive a complete record without demonstrating the last part. Putting the requirement in the unit summary does not fill the child-level evidence gap.

**Exact fix:** Add this requirement to day 139’s note:

> After teaching the comparison, retain every child’s short drawn or oral explanation showing why fourths are smaller than halves of the same-sized whole. Use the circle and rectangle products already made. This supplies the final 1.G.A.3 evidence for children heard on day 138.

Use the existing synthesis or exit-ticket time. Update day 146 and the unit 7 paragraph to identify this product explicitly. Preserve both existing explanation rotations and add no assessment day.

### 2. Day 114 permits untaught subtraction and carries an unrelated length code

**LAYER:** sequence  
**REPEAT:** new  
**Severity:** moderate  
**Confidence:** firm

**Location:** `days.csv`, day 114, mapped to base lesson 6.4.

**What is wrong:** Its goal is “Practice adding and subtracting within 100,” but Grade 1 subtraction beyond 20 is restricted here to multiples of ten. General subtraction within 100 has not been taught. The row carries only `m1-order-compare-length` and `1.MD.A.1`, although its stated activity contains no length comparison.

The base lesson has the same broad purpose sentence, but its actual activities distinguish addition within 100 from smaller-number addition/subtraction practice. Copying that sentence without its activity limits creates an ambiguous curriculum instruction. [Base lesson 6.4](https://im.kendallhunt.com/k5/teachers/grade-1/unit-6/lesson-4/lesson.html). The Grade 1 subtraction boundary is explicit in [1.NBT.C.6](https://www.thecorestandards.org/Math/Content/1/NBT/).

**Why it matters:** A writer following the authoritative daily goal could build general two-digit subtraction practice before instruction, while reporting coverage of a length standard the day does not address.

**Exact fix:**

- Replace the goal with: “Practice addition within 100 and addition and subtraction within 20.”
- Replace the skills with `m1-add-within-100; m1-add-sub-within-20`.
- Replace the codes with `1.NBT.C.4; 1.OA.C.6`.
- Add number cards and recording sheets, with handwritten alternatives, to supplies.
- Record the numerical limits in the note and source-map reason.

Keep the day in unit 6 as retrieval and practice. No ownership or day allocation changes.

### 3. Current file status and assessment wording remain inconsistent

**LAYER:** process  
**REPEAT:** yes, stale planning-state notes in both earlier Grade 1 frame reads  
**Severity:** minor  
**Confidence:** firm

**Location:** Scope and sequence, lines 15 and 185 to 187; frame, Readiness bullet, unit 8 row, and “For the lead” item 2.

**What is wrong:**

- The sequence says kindergarten `days.csv` is absent. It now exists, and its assessment entries carry all 20 assumed kindergarten rows.
- The frame still prescribes readiness checks for year-before prerequisites, despite the sequence correctly superseding that wording.
- The frame calls unit 8 an eleven-day unit in one note, while its table and daily plan give ten days.
- The frame says unit 8 has no assessment of its own, while day 160 now closes an embedded observation.

The sequence acknowledges several inconsistencies, so these are documentation repairs rather than newly discovered mathematical defects. The kindergarten availability statement may have been accurate when drafted.

**Why it matters:** A later writer can follow conflicting instructions about prerequisite assessment and unit closure.

**Exact fix:**

- Replace the kindergarten absence statements with a dated verification that its daily record now exists and supports kindergarten as the last-use grade for all 20 prerequisite rows.
- Replace the frame’s readiness bullet with retrieval wording consistent with the sequence.
- Change eleven review days to ten.
- Describe unit 8 as having “no separate assessment day; an embedded closing observation and response remain inside its final lessons.”

Do not alter historical reports.

## Order, coverage and days by load

| Unit | Days | Owned rows | Judgment |
|---|---:|---:|---|
| 1. Adding, subtracting and data | 16 | 2 | Counting precedes data interpretation; both owned standards reach the closing record. |
| 2. Story problems | 23 | 5 | Situation families precede concentrated equation work. Partial contribution to 1.OA.A.1 is correctly distinguished from completed codes. |
| 3. Adding and subtracting within 20 | 29 | 5 | Largest allocation fits the central fluency and strategy load. Day 57’s mid-unit assessment follows initial make-ten instruction; response is counted once. |
| 4. Numbers to 99 | 24 | 4 | Tens, mixed tens/ones, comparisons and flexible representations build in a defensible order. All a/b/c cases reach the closing assessment. |
| 5. Adding within 100 | 15 | 2 | Established place value supports the shorter allocation. New-ten composition follows no-new-ten work. |
| 6. Length to 120 units | 18 | 4 | Direct comparison precedes indirect comparison and equal-unit measurement. Counting and story work connect earlier units. Correct day 114 as finding 2 specifies. |
| 7. Geometry and time | 18 | 4 | Eight shape lessons, four sharing lessons and five clock lessons are proportionate. Halves precede half-hour clocks. Finding 1 repairs assessment evidence. |
| 8. Putting it together | 10 | 0 | Legitimate targeted review following the year-end response. Its embedded closure adds no day. |

No run is demonstrably far over or under its substantive load. Equal days per row would be inappropriate.

The plan carries all 21 numbered Grade 1 standards and the three lettered parts of 1.NBT.B.2. It explicitly includes the easily compressed requirements: numeral/collection matching, mental ten-more/less with reasoning, zero tens differences, composite shapes reused as units, share language, and both telling and writing clock times. The assessment exception is finding 1.

## Readiness, retrieval and calendar

All **20 distinct assumed earlier-grade rows** have kindergarten as their last-use grade. The current kindergarten daily record supports that classification.

| Unit | Treatment |
|---|---|
| 1 | Kindergarten counting, cardinality and small facts on day 1; sorting on day 7. |
| 2 | Kindergarten story meanings and expressions on day 17; group comparison on day 27. |
| 3 | Kindergarten decompositions and small facts on day 40; ten partners and teen structure on day 47. |
| 4 | Earlier Grade 1 ten structure on day 69; kindergarten numeral comparison on day 82. |
| 5 | Teen structure already used this year and unit 4 place value on day 96. |
| 6 | Kindergarten measurable attributes on day 111; counting prerequisites on day 118. |
| 7 | Kindergarten shape naming/analysis on day 129 and composition on day 130. |
| 8 | Explicit earlier Grade 1 work. |

No year-before row is incorrectly assigned readiness in the daily plan. No older prerequisite is incorrectly treated as retrieval, and no readiness check occupies a unit’s first day.

The course-level checks meet the target weeks, **19 and 30**, and preserve the required separation from ELA checks. The day 17 literacy bridge is appropriate because opening the ELA unit does not establish completed instruction. The science length bridges remain necessary because science uses those ideas earlier.

The immediate course-level checks use earlier-unit content for fresh tasks and retain the just-completed unit records. This satisfies the purpose of avoiding repeated collection. Their coverage should remain described as a combined record, without claiming a second independent demonstration of the unique unit 4 or unit 7 skills.

## Source map, Candidates and shorter path

The source map contains **146 retained base lessons and 14 original rows**. Each base lesson is placed once, in order, with lesson counts of **15, 22, 28, 23, 14, 17, 17 and 10** across units 1 to 8. The tape-diagram and context adaptations are identified.

All eight Candidate cells are settled. Planning comparisons cost zero student days; the two retained student extensions occupy named existing time. The dropped extensions have defensible reasons.

The forty-five-minute path preserves core representations, explanations and evidence. Its feasibility remains to be demonstrated in unit plans, especially during rotations.

The ten named fold-in days are **6, 10, 21, 26, 32, 46, 60, 73, 81 and 99**. None contains a scheduled assessment, unique owned part, initial prerequisite retrieval or allocated response slot. The distinction between ten missing mathematics meetings and a compressed school calendar is appropriately explicit.

## Mathematics lens checklist: scope and sequence

| Lens line | Result |
|---|---|
| Every standard is completed beyond its headline | **Met in teaching allocation; assessment evidence missed for part of the class in finding 1.** |
| Problems deliberately join units | **Met:** data/counting, make-ten/place value, and measurement/story diagrams. |
| Fluency receives spaced, mixed practice | **Met:** daily warm-ups, centers and later review; within-10 fluency remains distinct from within-20 strategies. |
| Models are taught before use | **Met:** ten-frames, ten as a unit, base-ten drawings and late labelled tape diagrams. |
| Grade limits are respected | **Missed in day 114’s goal:** finding 2. |
| Major work receives sufficient emphasis | **Met provisionally:** the planned 8,115/9,600 minutes exceed 75 percent; component-minute verification remains for unit plans. |
| Supporting work practices major work | **Met:** data supports operations, and unit 7 explicitly reserves number-work time. |
| All eight practices have named tasks and evidence | **Met at this layer.** |
| Understanding, fluency and application are represented | **Met in the planned tasks; actual lesson balance remains unverified.** |
| Every source lesson has a placement and decision | **Met.** |
| Unit assessment items, exits and accommodations are complete | **Not applicable yet:** instruments have not been written. |
| Student timer behavior and final manipulative-to-writing implementation | **Not applicable yet:** lesson artifacts are unavailable. |
| High-school and post-Algebra II provisions | **Not applicable.** |

## What is right and should not be touched

- The eight-unit order and unequal allocations.
- Equality as a relationship and unknowns in varied positions.
- Supported exposure to difficult story subtypes without imposing Grade 2 proficiency.
- Counting evidence separated from arithmetic-fluency evidence.
- The explicit tape-diagram adaptation.
- Shared response allocations and retained individual records.
- Paper alternatives and contexts that avoid personal disclosures.

## Settled by the expert

| Choice | Reason | File affected by eventual repair |
|---|---|---|
| Collect the smaller-share comparison from every child on day 139 | Completes the standard after instruction without another interview | Grade 1 `days.csv` and scope and sequence |
| Bound day 114 to addition within 100 and addition/subtraction within 20 | Matches taught content and the base activities | Grade 1 `days.csv` and source map |
| Preserve all unit allocations | No demonstrated load imbalance requires resizing | Grade 1 frame and sequence |
| Keep kindergarten prerequisites as retrieval | All 20 were used in the immediately preceding grade | Grade 1 prerequisite narrative and frame |
| Accept combined recent portfolios and earlier-unit fresh tasks for immediate course-level checks | Avoids duplicate individual collection while retaining coverage | Grade 1 check descriptions |
| Keep unit 8’s embedded closure within ten days | Reconciles review-unit status with the closing-assessment requirement | Grade 1 frame |

## What I could not judge

Actual assessment items, scoring guidance, accommodations, lesson-part minutes and classroom observation capacity are not yet available. The 24-child and shorter-period budgets are planning estimates, not demonstrated implementation.

The linked base-ten and geometry progression downloads timed out. Those page references were not independently verified; judgments here use the standards, progression records and accessible base lessons. No finding depends on inaccessible material.

## Sources

- [Grade 1 operations standards](https://www.thecorestandards.org/Math/Content/1/OA/), [base-ten standards](https://www.thecorestandards.org/Math/Content/1/NBT/), [measurement/data standards](https://www.thecorestandards.org/Math/Content/1/MD/) and [geometry standards](https://www.thecorestandards.org/Math/Content/1/G/): complete expectations and numerical limits.
- [Operations progression](https://commoncoretools.files.wordpress.com/2011/05/ccss_progression_cc_oa_k5_2011_05_302.pdf), PDF pages 13 to 17: counting strategies and difficult story subtypes.
- [Measurement progression](https://commoncoretools.files.wordpress.com/2012/07/ccss_progression_gm_k5_2012_07_21.pdf), PDF pages 8 to 10: direct/indirect comparison and iterated units.
- [Base curriculum scope and sequence](https://im.kendallhunt.com/k5/teachers/grade-1/course-guide/scope-and-sequence.html) and [pacing guidance](https://im.kendallhunt.com/k5/teachers/grade-1/course-guide/pacing-guide-and-dependency-diagram.html): order and assessment adaptation.
- [Eureka Math curriculum overview](https://greatminds.org/hubfs/knowledge/resources/math/EM_Basic_Curriculum_Files/Curriculum_Overview/EM_GPK5_CurriculumOverview.pdf#page=16), PDF pages 16 to 17: comparison sequence, ten as a unit, and continued fluency across topics. Used as reference only.
- [K to 8 Publishers’ Criteria](https://achievethecore.org/content/upload/Math_Publishers_Criteria_K-8_Spring_2013_FINAL.pdf): focus, coherence and rigor.
- [Mathematics evidence guide](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf#page=13): K to 2 focus threshold and multiple counting perspectives.
- [Federal elementary mathematics intervention guide](https://ies.ed.gov/ncee/wwc/practiceguide/26): systematic instruction, representations and deliberate word-problem teaching. Its intervention setting limits whole-class generalization.

## For the source list

No new source is required. Record the base-ten and geometry progression access failures if updating reachability notes.

## For Cory

None. These corrections change no scope, money, people, audience or standard ownership.

**Verdict:** Coherent sequence; revise before unit planning. **Finding count:** 3. **Report path:** `docs/reviews/sequence-math-grade-1-2026-11-15.md`, supplied here, not written.


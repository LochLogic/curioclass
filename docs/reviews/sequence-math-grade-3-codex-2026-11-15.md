# Independent sequence review: Math Grade 3

**Date:** 2026-11-15  
**Role:** Independent first reader, before the expert  
**Intended report path:** `docs/reviews/sequence-math-grade-3-2026-11-15.md`  
**Delivery:** Complete report supplied here. No files changed.

## Verdict

The sequence has a sound mathematical arc, appropriate unit allocations, and explicit plans for the owned standards, assessments, and cumulative checks. Its main risks are division practice scheduled before instruction, prerequisite retrieval placed after first use, and a no-kit measurement route that cannot supply all the claimed evidence. Correct these and the data and handoff inconsistencies below before using the sequence to generate unit plans.

**Finding count: 6.**

## What I read

- `docs/agents/EXPERT.md`, the mathematics lens, and `docs/RUBRIC-MATH-K8.md`.
- The foundation, shared and mathematics approaches, relevant source-register entries and evidence notes, roadmap provisions, BASELINE rules 20 to 24, glossary, and sequence-writing rules.
- The complete Grade 3 scope and sequence, all 160 day rows, the frame, and source map.
- All 24 Grade 3 mathematics progression rows, their Grade 2 prerequisites, and relevant adjacent-grade handoffs.
- The current Grade 2 day file to verify the 23 assumed rows.
- Grade 3 standards, including lettered parts and official footnotes.
- `CALENDAR.md`, Grade 3 calendar rows, relevant same-year frame passages, and selected ELA day rows.
- Earlier permitted Grade 3 mathematics frame reviews, Grade 1 and kindergarten sequence findings, and the readiness-timing record.
- Outside sources linked below, including two curriculum sequences and selected base lessons.

The prohibited files were not opened. Session memory supplied procedural scope reminders only; no curriculum finding rests on memory.

## Gates

The repository-wide plan check stopped because Python lacks the `markdown` package; this environment failure does not withhold the verdict.

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Incomplete: `ModuleNotFoundError: No module named 'markdown'` |
| `python -X utf8 scripts/frame.py calendar` | Passed; Grade 3 mathematics checks fall in weeks 12, 23, and 31 |
| `python -X utf8 scripts/frame.py check math-grade-3` | 0 failures |
| `python -X utf8 scripts/plan.py check math-grade-3` | 0 failures |
| `python -X utf8 scripts/sequence.py check math-grade-3` | 0 failures |
| `python -X utf8 scripts/stale.py check` | 56 files, 0 failures |

No turn, synchronization, build, defect-writing, or Git mutation command was run.

## Findings, most serious first

### 1. Division facts enter the warm-up before division is taught

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, practice using untaught content also appears in the earlier Grade 1 sequence review, finding 2  
**Confidence:** Firm on the ordering; likely on its classroom effect

**Location:** `days.csv`, days 62 to 67; scope and sequence, “Load, practice and limits.”

**What is wrong:** Day 62 introduces the first division meaning, but its warm-up already requires mixed multiplication and related division facts. The same generic direction continues while the two division meanings are being established. Division as an unknown factor is not explicitly taught until day 67.

This contradicts the sequence’s own promise that related quotients enter after division has meaning. The retained first division lesson opens with grouping and multiplication reasoning before its division work. [Base division-opening lesson](https://im.kendallhunt.com/k5/teachers/grade-3/unit-4/lesson-1/lesson.html).

**Why it matters:** A writer following the daily record can ask children to practise unfamiliar division notation and procedures before teaching their meaning.

**Exact fix:** Keep days 62 to 67 warm-ups on understood multiplication facts and maintained addition and subtraction. Begin mixed related-quotient retrieval on day 68, after the unknown-factor connection has been taught. Update the course practice paragraph and corresponding source-map notes. This preserves all unit days.

### 2. Several prerequisite retrieval tasks occur after their first relevant use

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** new among the permitted earlier reports examined  
**Confidence:** Firm

**Location:** Scope and sequence, prerequisite ledger; `days.csv`, days 7 to 10, 20, 31, 36, and 41.

**What is wrong:** The ledger calls its entries the first relevant retrieval days, but several skills and models are already required earlier:

| Prerequisite | Listed first retrieval | Earlier named use | Correct placement |
|---|---:|---|---|
| `m2-one-step-problems` | 54 | Day 7, one-step graph comparisons; day 10, retrieved tape diagrams | Retrieve comparison reasoning on day 7 and reconnect the diagram on day 10 |
| `m2-two-step-problems` | 54 | Day 8, two-step graph comparisons | Retrieve on day 8 |
| `m2-explain-strategies` | 40 | Day 20, property reasoning about turning an array | Retrieve on day 20 |
| `m2-measure-with-tools` | 92 | Day 31, measuring rectangle side lengths | Retrieve on day 31 |
| `m2-length-problems` | 139 | Day 36, finding missing lengths | Retrieve on day 36 |
| `m2-number-line` | 50 | Day 41, an open number line for addition | Retrieve on day 41 |

The current Grade 2 day file carries all 23 assumed rows, so these remain retrieval tasks. They do not require older-grade readiness checks. Deliberately reconnecting familiar representations when their use changes is also consistent with the federal intervention guide. [Systematic instruction and representations](https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/WWC2021006-Math-PG.pdf).

**Why it matters:** Teachers receive prerequisite support after the lesson that first needs it. The tape diagram is particularly clear: day 10 says it is retrieved, but the prerequisite ledger postpones the relevant rows until day 54.

**Exact fix:** Make the placements above explicit in the daily notes and prerequisite ledger. Retain later retrieval where the context changes, but label it as another retrieval. Update the frame’s Seams and Models tables to acknowledge these earlier uses. Keep retrieval brief and inside the relevant lesson.

### 3. The no-kit measurement route cannot supply the full measuring performance

**Severity:** Moderate  
**LAYER:** standard  
**REPEAT:** yes, an assessed standard lacking a required performance also appears in the Grade 1 sequence review, finding 1  
**Confidence:** Firm on the requirement; likely on how the fallback would be implemented

**Location:** Scope and sequence, unit 7, especially line 109; `days.csv`, days 122 to 124, 132, and 153.

**What is wrong:** Unit 7 provides scale diagrams as the no-kit route, then says supplied records cannot replace actual measuring “when equipment is available.” That qualification leaves the equipment-free route able to substitute interpretation for measuring.

Yet days 132 and 153 reuse individual measurement records as evidence for full `3.MD.A.2`. Reading supplied scale pictures does not establish that a child measured an object’s mass. The standard requires measuring as well as estimating and solving problems. [Official mathematics standards, printed page 25](https://learning.ccsso.org/wp-content/uploads/2022/11/Math_Standards1.pdf#page=25).

**Why it matters:** A teacher or parent without equipment can complete the written route while an essential performance remains unobserved.

**Exact fix:** State that diagrams support interpretation and problem solving but do not complete the measuring requirement. Reserve an individual estimate-and-measure record within days 122 to 124 using shared suitable equipment, with rotation where necessary. Reuse that record at both assessments. If equipment cannot be accessed, explicitly mark the measuring component pending rather than recording full coverage.

This corrects the evidence claim without adding a day or authorizing a purchase.

### 4. Eight added days put teaching directions in the supplies column

**Severity:** Moderate  
**LAYER:** process  
**REPEAT:** new among the permitted earlier reports examined  
**Confidence:** Firm

**Location:** `days.csv`, days **73, 74, 75, 82, 85, 94, 100, and 110**; corresponding original-day source-map rows.

**What is wrong:** Their `supplies` cells contain instructional paragraphs rather than physical materials. Examples include the complete unknown-position direction on day 82, operation-order boundaries on day 85, and the fact-record collection instructions on day 75.

The source-map reasons for these days largely reproduce the warm-up notes, so they do not preserve the misplaced instructions either. The sequence-writing specification says the supplies fields feed unit-plan and skeleton materials lines.

**Why it matters:** Generating a unit plan can turn essential teaching and assessment directions into a materials list. Writers can miss the instructions precisely where the sequence adds content beyond the base lessons.

**Exact fix:**

- Move each instructional paragraph into `note`.
- Leave only actual physical materials in `supplies`.
- Fill the applicable drawn-model names in `tools`, including the number line on day 100.
- Preserve day 75’s collection and reuse rule in its note.
- Give each added source-map row its substantive reason, including the owned part it supplies.
- Remove the stray repeated fraction-code prefix in day 100’s note.

### 5. Thirty-six source-map entries repeat their destination day

**Severity:** Minor  
**LAYER:** base text  
**REPEAT:** new among the permitted earlier reports examined  
**Confidence:** Firm

**Location:** `source-map.csv`, retained lessons from base units 3.6, 3.7, and 3.8.

**What is wrong:** Thirty-six rows contain duplicate tokens such as `117; 117`, `134; 134`, and `149; 149`. Each maps one retained lesson to one course day.

**Why it matters:** The map overstates placements for a consumer that counts tokens and obscures whether a lesson was deliberately split. The current checks accept these entries.

**Exact fix:** Replace each repeated pair with its single day number. Preserve the genuine merge of base lessons 3.3.8 and 3.3.9 onto day 46. Confirm that all 143 base lessons still have one decision and retained lesson order remains unchanged.

### 6. The prerequisite handoff contains obsolete file-status and readiness statements

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale planning-state notes recur in the earlier Grade 3 frame and kindergarten and Grade 1 sequence reviews  
**Confidence:** Firm

**Location:** Scope and sequence, line 11, prerequisite table, and “For the lead,” item 1; frame Readiness bullet, Seams table, and units 3, 6, 7, and 8.

**What is wrong:** The sequence says `data/plans/math-grade-2/days.csv` does not exist. It now exists and carries all 23 assumed rows. The table’s repeated “planned” qualification therefore describes an obsolete evidence limitation.

The frame also continues to require readiness checks on Grade 2 rows, although its general rule and this sequence correctly classify those rows as retrieval.

**Why it matters:** The next writer receives an unnecessary upstream investigation and conflicting assessment instructions.

**Exact fix:** Replace the missing-file claim with a dated statement that all 23 prerequisites were verified in the Grade 2 day plan. Update the ledger’s evidence status, without claiming classroom delivery was verified. Replace the frame’s Grade 2 readiness directions with retrieval directions and remove the obsolete follow-up action.

The automated stale check passed but did not detect these statements.

## Coverage, order, and load

### Unit arcs

| Unit | Total days | Teaching days | Judgment |
|---|---:|---:|---|
| 1. Multiplication | 22 | 20 | Eight graph days support twelve days developing multiplication meaning |
| 2. Area | 16 | 14 | Coverage precedes products; three decomposition days preserve additive area |
| 3. Addition, subtraction, rounding | 21 | 19 | Six addition, five subtraction, four rounding, and four application days form a defensible allocation |
| 4. Division and facts | 16 | 14 | Meanings precede inverse relationships and strategies, except the premature warm-up |
| 5. Larger-number problems | 14 | 12 | Four initial lessons, two problem-range lessons, and six further application and strategy lessons fit the ownership |
| 6. Fractions | 23 | 21 | Unit fractions lead to lines, equivalence, whole-number fractions, and comparisons |
| 7. Measurement | 17 | 15 | Five ruler/plot days, three mass/volume days, three time days, and four applications |
| 8. Shapes and perimeter | 15 | 13 | Five classification days precede eight perimeter and connected-design days |

No unit is demonstrably far over or under its load. Unit 3’s additional-cluster allocation is substantial, but it includes maintained fluency and four days beginning major two-step work. Neither equal time per standard nor resizing is warranted.

### Standards and assessments

All owned codes and lettered parts have named teaching and assessment placements. The conditional measuring gap is finding 3.

| Content | Planned completion and evidence |
|---|---|
| Multiplication meaning and graphs | Days 1 to 20; assessment 21 |
| Area concepts and `3.MD.C.7a`, `7b`, `7d` | Days 23 to 36; artifact 36 and assessment 37 |
| Addition, subtraction, rounding | Days 39 to 57; assessment 58 |
| Division, properties, patterns, distributive area, developing facts | Days 62 to 75; fact record 75 and assessment 76 |
| Multiples of ten and complete problem range | Days 78 to 89; modelling record 89 and assessment 90 |
| Partitioning and all fraction parts | Days 92 to 112; design 112 and assessment 113 |
| Measurement and time | Days 117 to 131; retained practical records and assessment 132 |
| Classification and perimeter | Days 134 to 146; retained products and assessment 147 |

No unit exceeds 25 days, so no mid-unit assessment is required. Each unit has one response day, and the course has four additional response days. Response time is counted once.

The plan appropriately distinguishes developing facts in unit 4 from the year-end memory target. Actual items must preserve the distinction between recalled products and strategy-supported computation.

### Readiness and retrieval

All 23 assumed earlier-grade rows have last use in Grade 2 according to the current day plan. No older directly assumed row requiring readiness was established.

No actual readiness check is placed on a unit’s first day or excessively early. The sequence correctly overrides the frame’s inappropriate Grade 2 readiness wording. Retrieval timing still needs finding 2’s repairs.

### Checks and calendar

The baseline meets the target calendar:

- Check 1: day **60**, week **12**.
- Check 2: day **115**, week **23**.
- Check 3: days **152 to 153**, week **31**.

The sequence explicitly places recent computation in earlier graph and area contexts, recent fractions in earlier area and problem contexts, and recent perimeter work in earlier representations. It reserves different task forms and reuses named independent products.

Same-year leans have adequate timing or bridges:

- ELA vocabulary work occupies days 40 to 77; mathematics retains its own bridge on day 78.
- ELA discussion precedes fraction comparisons.
- Later science weather work is not assumed by early graph lessons.
- Earlier science motion work does not substitute for the fresh fractional measurements.
- Earlier science and social studies retain their whole-unit, washer-count, and within-100 bridges.

### Candidates, shorter path, and source map

All eight Candidate cells are settled, with retained additions and extensions assigned to existing days.

The shorter path names ten unassessed fold-ins: **7, 18, 25, 33, 41, 48, 53, 69, 81, and 108**. It preserves assessment artifacts, response days, and owned parts. Its shortened check meetings, **53, 105, and 142 to 143**, are correct. The text appropriately requires another cross-subject calendar check.

The 45-minute adaptation is explicitly provisional. Its actual feasibility, especially when combined with 150 meetings, remains a timing question for unit planning.

The source map accounts for **143 base lessons**, including **14 cuts**. The 129 retained lessons occupy 128 course days because of the subtraction merge; 32 original slots bring the course to 160. Cuts and adaptations have reasons, and retained base order is preserved. Finding 5 concerns duplicate destination tokens, not missing lessons.

## Math lens checklist: scope and sequence

| Lens line | Result |
|---|---|
| Every owned standard reaches completion | **Met in the main plan; missed for full measuring evidence in the equipment-free fallback**, finding 3 |
| Problems deliberately connect units | **Met** |
| Fluency receives spaced, mixed practice | **Met**, with premature division practice corrected under finding 1 |
| All eight practices have named tasks and evidence | **Met at planning level** |
| Models are available before their new use | **Mostly met; prerequisite reconnections need finding 2** |
| Grade limits and algorithm expectations hold | **Met** |
| Supporting work practises major work | **Met**, particularly graphs, fractional plots, and partitioning |
| Major-work emphasis is demonstrated | **Provisionally met:** six principal units and an explicit estimate of 108 of 160 day equivalents |
| Source-map decisions are complete | **Met**, with finding 5’s data correction |
| High school and past-Algebra-2 provisions | **Not applicable** |

The major-work estimate is 67.5 percent. It remains a planning estimate rather than verified instructional minutes. The evidence guide calls for multiple counting perspectives. [Mathematics evidence guide, indicator 1e](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf#page=13).

## What is right and should remain

- The base sequence, including graphs before multiplication and fractions before fractional rulers.
- Explicit unknown positions, both division meanings, and both rectangle comparison requirements.
- Delayed standard-algorithm mastery and appropriately bounded fraction work.
- Original assessments and reused independent products.
- Private fact records, spaced practice, and no student countdown.
- The named shorter-year folds and honest timing limitations.

## Settled by the expert

These are item-level recommendations for the caller to apply.

| Choice | Reason | Files affected |
|---|---|---|
| Begin mixed division-fact warm-ups on day 68 | The inverse connection has been taught | Scope, day file, source map |
| Move prerequisite retrieval to the first uses in finding 2 | Support must precede dependent work | Scope, day file, frame |
| Require an actual measuring record for full measurement coverage | Interpretation cannot establish measuring | Scope and day file |
| Restore instructions to notes and materials to supplies | Preserve essential directions in generated plans | Day file and source map |
| Deduplicate 36 map destinations | Each retained lesson has one intended destination | Source map |
| Verify Grade 2 use from its existing day plan | Removes an obsolete prerequisite limitation | Scope and frame |
| Retain all unit allocations and standard ownership | No demonstrated imbalance requires changing them | Frame and sequence |

## What I could not judge

Finished assessment items, scoring guidance, record sheets, and actual lesson minutes are not available at this layer. The broad course checks need timed item blueprints during unit planning.

The compiled 2023 Progressions PDF exceeded the retrieval limit. Accessible earlier OA, NBT, and fraction documents supported the conceptual checks, but the compiled document’s exact page pointers were not independently verified. The federal fractions practice guide timed out.

No judgment depends on an inaccessible source or recalled research claim.

## Outside sources

- [Official mathematics standards](https://learning.ccsso.org/wp-content/uploads/2022/11/Math_Standards1.pdf): complete expectations, footnotes, and grade boundaries.
- [Counting and operations Progressions](https://commoncoretools.files.wordpress.com/2011/05/ccss_progression_cc_oa_k5_2011_05_302.pdf): meanings, strategies, problem types, and fluency.
- [Base-ten Progression](https://mathematicalmusings.org/wp-content/uploads/2015/03/ccss_progression_nbp_k5_2015_03_16.pdf): maintained computation and rounding.
- [Fractions Progression](https://mathematicalmusings.org/wp-content/uploads/2018/08/ccss_progression_nf_35_2018_08_10.pdf): unit fractions, number lines, equivalence, and comparisons.
- [Base curriculum sequence](https://im.kendallhunt.com/k5/teachers/grade-3/course-guide/scope-and-sequence.html): unit order and connections.
- [Second curriculum overview, Grade 3](https://greatminds.org/hubfs/knowledge/resources/math/EM_Basic_Curriculum_Files/Curriculum_Overview/EM_GPK5_CurriculumOverview.pdf#page=34): independent comparison of sequencing and sustained operations work; reference only.
- [K to 8 Publishers’ Criteria](https://achievethecore.org/content/upload/Math_Publishers_Criteria_K-8_Spring_2013_FINAL.pdf): focus, coherence, rigor, and supporting work.
- [Federal elementary mathematics intervention guide](https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/WWC2021006-Math-PG.pdf): systematic review and representation connections. Its intervention setting does not validate this course’s whole-class pacing.

**For the source list:** Record the accessible earlier Progressions links and the two access failures. No new research claim needs adding.

## For Cory

- If complete coverage is promised to a room without measuring equipment, decide how it will access a suitable shared metric scale or balance and calibrated masses. No purchase or outreach was undertaken.

**Final verdict:** Sound overall; make the six targeted corrections before unit planning. **Finding count:** 6. **Report path:** `docs/reviews/sequence-math-grade-3-2026-11-15.md`, supplied here only.


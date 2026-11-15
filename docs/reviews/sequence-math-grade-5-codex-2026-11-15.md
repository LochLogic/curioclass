# Independent read: Math Grade 5 scope and sequence

**Date:** 2026-11-15  
**Delivery:** Complete report supplied here. No files were created or changed.

## Verdict

The mathematical architecture is sound, with targeted revisions needed before unit planning. The main risk is that the shorter-period path and decimal assessment promise more work than their named slots reliably support. Make the evidence windows and receiving practice slots explicit, then correct readiness placement, retrieval timing and stale frame instructions while retaining the unit order and ownership.

## What I read

- The expert instructions, mathematics lens, mathematics rubric, foundation, shared and mathematics approaches, relevant source records and evidence notes, applicable roadmap sections, BASELINE rules 20 to 24, glossary and sequence-writing rules.
- The complete [scope and sequence](/S:/CurioClass/docs/courses/math-grade-5/scope-and-sequence.md), all 160 rows of [days.csv](/S:/CurioClass/data/plans/math-grade-5/days.csv), the [frame](/S:/CurioClass/docs/courses/math-grade-5/frame.md), and the source-map inventory, decisions and shorter-period instructions.
- All 25 Grade 5 progression rows, their earlier-grade prerequisites and relevant Grade 6 handoffs. I checked prerequisite placements in the permitted `data/plans/math-grade-4/days.csv`.
- The Grade 5 standards, [CALENDAR.md](/S:/CurioClass/docs/courses/CALENDAR.md), every Grade 5 calendar row, and the other Grade 5 subjects’ Cross-subject sections.
- Permitted earlier Grade 5 frame reports, the Grade 3 independent sequence report and the Grade 1 expert sequence report, for prior findings and REPEAT tags.
- Targeted public base lessons and locally stored lesson narratives, plus the outside sources linked below.

The blind exclusions were honored. No substantive judgment below rests solely on model memory.

**Gates:** `plan.py check` could not finish because `markdown` is missing; `frame.py check math-grade-5` and the additional scoped `sequence.py check math-grade-5` passed with zero failures; `frame.py calendar` ran without a stagger violation; `stale.py check` passed across 56 files.

## Findings, most serious first

### 1. Unit 1’s readiness check conflicts with this run’s placement requirement

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** new among the permitted reports examined  
**Confidence:** firm

**Location:** Scope and sequence, prerequisite table and Unit 1; `days.csv`, days 1 and 2.

**What is wrong:** The older prerequisite `m3-area-concepts` is checked during day 1’s last ten minutes, after the volume hook. This run explicitly requires Unit 1’s older prerequisites to be checked in the start-of-year check before the unit opens.

There is a real instruction conflict: the repository’s sequence-writing rule currently permits the exact day-1 arrangement used here. The scoped gate therefore passes it. The direct instruction for this review takes precedence.

**Why it matters:** The result cannot shape the opening lesson, and the plan does not meet the readiness placement requested for this run. The classification itself is correct: this is an older prerequisite, not a Grade 4 retrieval.

**Exact fix:** Place the square-unit task in an explicitly identified start-of-year readiness check before Unit 1. Remove `assess=readiness` and the check allocation from day 1; use its results to plan the opening support. Retain the targeted square-unit reminder where needed.

If that check requires another scheduled meeting, its place within the fully allocated 160-day year needs Cory’s decision. Do not silently add a day or shorten a unit.

### 2. The decimal end-of-unit assessment lacks the earlier evidence window its shorter path assumes

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, end-day performance loading appears in the Grade 1 sequence report, finding 3  
**Confidence:** likely

**Location:** Scope and sequence, Unit 7 and Shorter path; `days.csv`, days 92, 95, 100 and 106; source-map assessment row for day 106.

**What is wrong:** Day 106 requires four complete operation blocks. Each includes a model or drawing, reasoning, a written method and an explanation, with estimation and critique also included. Unlike several other units, Unit 7 names no earlier independent products that the end day reuses.

The source map nevertheless tells the shorter-period writer to use saved independent products within the window. Those products and their collection days have not been assigned. The sequence-writing rule also directs writers to spread multiple full performances across the closing work.

**Why it matters:** A writer could compress the explanatory work into answer-only calculations or collect evidence outside the budget. The standard requires the connections between representations, strategies and written methods. The [base-ten Progression, PDF pages 19 to 20](https://mathematicalmusings.org/wp-content/uploads/2015/03/ccss_progression_nbp_k5_2015_03_16.pdf) supports preserving those connections.

**Exact fix:** Identify independent addition evidence on day 92, subtraction evidence on day 95 and multiplication evidence on day 100, replacing parallel practice within those days. Each retained product should contain the operation, representation, written connection and explanation. Day 106 should explicitly reuse them and collect the division performance and remaining critique evidence.

Update the prose, daily notes and shorter-period entries together. Keep the independent evidence on its named day. These collection days do not remove any of the ten proposed fold-in days.

### 3. Nineteen receiving warm-ups have two competing assignments

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** new among the permitted reports examined  
**Confidence:** firm

**Location:** Source-map `short_period` column; corresponding multiplication warm-up notes in `days.csv`.

**What is wrong:** The 45-minute path repeatedly moves five minutes of source practice into a later warm-up, “replacing parallel practice.” Nineteen distinct receiving days already reserve five minutes for spaced, mixed standard multiplication:

**82, 85, 88, 94, 97, 100, 103, 112, 115, 121, 124, 127, 130, 136, 139, 142, 145, 151 and 160.**

For example, day 93’s addition practice moves into day 94’s multiplication slot; day 126’s line-plot practice moves into day 127’s multiplication slot. Those are different learning targets. The two source rows merged into day 150 describe one shared move to day 151 and should be counted once.

**Why it matters:** Following the shorter path either removes much of the promised multiplication maintenance or expands warm-ups beyond their allocation. Both files cannot govern the same five minutes as written. Dedicated fluency practice is consistent with the [K to 8 Publishers’ Criteria](https://achievethecore.org/content/upload/Math_Publishers_Criteria_K-8_Spring_2013_FINAL.pdf).

**Exact fix:** Preserve the explicitly scheduled multiplication slots. For each conflicting source-map entry, either:

- omit the duplicate practice tail after retaining a representative independent case on its original day; or
- place it inside a named later activity, replacing a specified parallel case there.

Do not move first teaching, required representations or independent assessment evidence. Record the receiving activity and minutes instead of assigning the occupied warm-up.

### 4. Two retrieval placements follow the first named use

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, late prerequisite retrieval appears in the Grade 3 independent sequence report, finding 2  
**Confidence:** likely

**Location:** Scope and sequence, prerequisite table and same-year prerequisite paragraph; `days.csv`, days 18, 31, 72 and 73.

**What is wrong:**

| Prerequisite | Listed retrieval | Earlier named use |
|---|---:|---|
| Grade 4 mixed-number representation | Day 31 | Day 18 explicitly solves problems with mixed-number quotients |
| Unit 2 fractional quotient meaning | Day 73 | Day 72 interprets a remainder as a fractional share |

The first case needs recognition and interpretation of mixed numbers, even though rewriting them for multiplication comes later. The second uses the earlier sharing meaning before the sequence’s declared retrieval placement.

**Why it matters:** The prerequisite support arrives after the task that first requires it. These remain retrieval tasks. They do not need additional readiness assessments.

**Exact fix:** Add a brief mixed-number interpretation retrieval at the opening of day 18, or earlier if an adapted task first uses that representation. Keep day 31’s retrieval specifically for rewriting mixed numbers before multiplication. Retrieve Unit 2 sharing meaning at the opening of day 72, then label day 73 as another retrieval in the fractional partial-quotient setting.

Update the prerequisite ledger to distinguish first retrieval from later returns. No days are added.

### 5. The frame retains instructions and dates superseded by the sequence

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, stale readiness and coordination notes recur in the permitted earlier mathematics reports  
**Confidence:** firm

**Location:** Frame, Readiness bullet, Unit 1 and Unit 3 descriptions, Cross-subject table, For the lead item 5, and source-map notes.

**What is wrong:**

- The Readiness bullet calls each first base lesson’s Grade 4 revisit a “readiness check.” The sequence correctly treats these as retrieval.
- Several frame passages still describe braces as added in base lesson 2.13. The sequence now first teaches braces on day 10 and revisits them on day 29.
- The frame places science’s design unit around school days 133 to 156 and sky unit around days 83 to 108. The current calendar gives **125 to 147** and **75 to 100**, respectively. The sequence uses the current dates.

**Why it matters:** A unit writer consulting the frame can restore outdated assessment labels, symbol timing or cross-subject assumptions.

**Exact fix:** Replace the Grade 4 “readiness check” wording with “retrieval task.” Synchronize Unit 1’s older-prerequisite wording with finding 1. State consistently that day 10 introduces brackets and braces separately and day 29 revisits braces. Replace the two science date ranges with the current calendar ranges and retain the existing bridges.

The earlier missing-symbol finding is resolved in the sequence. This finding concerns residual instructions that could undo that correction.

## Coverage, order and load

The unit arcs build coherently toward their questions:

| Unit | Teaching days | Judgment |
|---|---:|---|
| 1 | 12 | Packing, layers, dimensions, formulas, decomposition and expressions form a coherent arc. |
| 2 | 5 | Appropriate compact allocation for quotient meaning and sharing applications. |
| 3 | 18 | Sustained partitioning and fractional-area work justifies the longer allocation. |
| 4 | 11 | Both permitted division types precede operation selection and mixed-number applications. |
| 5 | 20 | Nine multiplication lessons, eight division lessons and three applications justify the load. |
| 6 | 10 | Representations precede comparison, rounding and applications. |
| 7 | 15 | Six addition/subtraction, five multiplication and four division days are defensible; assessment collection needs finding 2. |
| 8 | 7 | Powers precede conversions and multi-step applications; customary conversions use stated factors. |
| 9 | 14 | Six unlike-fraction days, two plot days and six scaling days match the multiple demands. |
| 10 | 13 | Coordinates precede pattern graphs; five hierarchy days cover attributes and inheritance. |

No unit exceeds 25 days, so no mid-unit assessment is required. I found no run substantially over or under its instructional load.

No omitted lettered teaching part was established at this layer. The important completion points are explicit: grouping symbols on day 10, both fraction-multiplication parts through day 40, both unit-fraction division types through day 53, both decimal place relationships through day 89, and fraction equivalence through multiplication by one on day 131.

The end-of-unit records identify the required content and saved products. Unit 7 needs the collection correction above. Actual item wording, keys, scoring and administration time remain unit-plan work.

## Other checks requested by the brief

| Check | Result |
|---|---|
| Earlier-grade last use | All 23 listed Grade 4 prerequisite rows have teaching or assessment placements in the permitted prior-year day file. `m3-area-concepts` has no explicit prior-year placement. |
| Readiness versus retrieval | Classification is sound. No later unit opens with readiness, no Grade 4 row is checked as older learning, and no older row is merely retrieved. Placement corrections are findings 1 and 4. |
| Checks that do not repeat | Checks 1 and 2 explicitly draw the recent unit’s skills from earlier units’ content and change task form. Check 3 specifies decision-table and report-audit forms. |
| Response counted once | Unit and course-level response allocations are distinguished. Later review applies the results without claiming another assessment allocation. |
| Calendar | Check days 55, 108, and 153 to 154 fall in target weeks 11, 22 and 31. |
| Same-year leans | Current dates and bridges work: whole grams, supplied distances and scale models, bar graphs, and the temporary earlier-grade line-plot bridge. Social studies uses latitude and longitude. |
| Candidates | Every unit settles its candidate guidance and extension, with embedded time or a reason for dropping it. |
| Short year | Ten unassessed donor days are named with destinations: 4, 19, 30, 48, 64, 74, 87, 101, 124 and 144. No owned part is explicitly cut. |
| Shorter period | Present, but receiving practice allocations need finding 3 and the assessment window needs finding 2. |
| Source map | All 148 expected base lessons appear exactly once, with no missing or duplicate lesson identifiers. Decisions and cut reasons are supplied. Retained lesson order stands; routine reuse is identified separately. |
| Stale notes | Automated check passed; finding 5 records the manual findings. |

The two merged review days now name retained activities, omissions and minute budgets. This resolves the earlier missing-selection finding. Their practical timing remains untried.

## Lens checklist: scope and sequence layer

| Lens line | Result |
|---|---|
| A standard taught in part with no later completion | Met at the planning layer: no missing lettered teaching part established. |
| Problems deliberately join units | Met: fraction meaning, volume, division, decimal area and scaling are reconnected in named tasks. |
| Fluency receives spaced, mixed practice | Met in the main path; missed in the shorter-period allocation until finding 3 is fixed. |
| Major-work focus | Met as a planning budget: 8 of 10 units and the stated conservative 7,425 of 9,600 minutes, about 77.3 percent. The [evidence guide’s Grade 3 to 8 guideline](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf) is 65 percent. |
| Prerequisites and models precede use | Mostly met; finding 4 corrects two retrieval placements. |
| Grade limits and algorithm progression | Met: general fraction division, long-division fluency and decimal-algorithm fluency remain later work. |
| Practices tied to teaching and evidence | Met: all eight have named tasks; MP5 includes a consequential tool choice. |
| Supporting work practices major work | Met through expressions, conversion and fraction plots. |
| Source-map decisions | Met. |
| Counting observations and high school criteria | Not applicable to this Grade 5 sequence. |

## What is right and should not be touched

- The unit order, especially quotient meaning before fraction multiplication and the multiplication algorithm before decimal operations.
- The mixed-number product bridge and the replacement of premature unlike-denominator sums in fractional partial quotients.
- The explicit `n/n` equivalence connection, positive-quantity qualification for scaling, inclusive trapezoid convention and given pattern rules.
- The named independent evidence windows already used in Units 4, 5, 9 and 10.
- The cross-subject bridges, separate check weeks and cuts of investigations into private household habits.

## Settled by the expert

These are recommendations for the caller to apply, not edits made during this read.

| Choice | Reason | File touched |
|---|---|---|
| Retain the ten-unit order and ownership | No instructional dependency requires a move | Frame and scope and sequence |
| Save decimal evidence on days 92, 95 and 100; reuse it on day 106 | Preserve full explanations without concentrating four performances on the end day | Days, source map and Unit 7 prose |
| Preserve the scheduled multiplication warm-ups in the shorter path | They carry the course’s deliberate fluency maintenance | Source map |
| Omit duplicate source practice or replace a named later activity case | Resolve the nineteen occupied receiving slots without adding time | Source map |
| Retrieve mixed-number interpretation by day 18 and fractional sharing on day 72 | Put prerequisite support before its first named use | Days and prerequisite ledger |
| Synchronize symbol timing, retrieval labels and science dates | Prevent older frame instructions from overriding the current sequence | Frame |
| Keep assessment, response and owned content intact in compression | These are the shorter path’s binding constraints | Scope and sequence and source map |

## What I could not judge

- Actual assessment difficulty, answer-key accuracy or scoring reliability: items do not yet exist at this layer.
- Whether the proposed minutes work with students. Finding 2 is a planning risk, not a measured overrun.
- The compiled Progressions’ exact pagination: the web tool rejected that PDF because of its size. Accessible standalone documents supported the substantive checks; compiled page pointers were not certified.
- Full implementation of access, family supports or model withdrawal, which belongs in later plans.

## Outside sources

- [Common Core mathematics standards](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf): Grade 5 content and required performances.
- [Fractions Progression, 2018 draft](https://mathematicalmusings.org/wp-content/uploads/2018/08/ccss_progression_nf_35_2018_08_10.pdf): quotient meaning, partitioning, unlike denominators, restricted division and scaling.
- [Base-ten Progression, 2015 draft](https://mathematicalmusings.org/wp-content/uploads/2015/03/ccss_progression_nbp_k5_2015_03_16.pdf): multiplication fluency, explained division and decimal methods.
- [K to 8 Publishers’ Criteria](https://achievethecore.org/content/upload/Math_Publishers_Criteria_K-8_Spring_2013_FINAL.pdf): focus, connections and dedicated fluency practice.
- [Mathematics K to 8 evidence guide](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf): major-work calculation perspectives and guideline.
- [Base curriculum’s Grade 5 scope and sequence](https://im.kendallhunt.com/k5/teachers/grade-5/course-guide/scope-and-sequence.html): unit order, dependencies and conceptual arcs.
- [Second curriculum’s Grade 5 overview](https://greatminds.org/hubfs/knowledge/resources/math/EM_Basic_Curriculum_Files/Curriculum_Overview/EM_GPK5_CurriculumOverview.pdf#page=56): independent comparison of sequencing and operation load, used as reference only.
- [Federal fractions practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/15): understanding fractions as numbers and explaining computational procedures.

**For the source list:** Record the accessible standalone Progressions links as fallbacks and the compiled-PDF size failure. No new research claim is proposed.

## For Cory

- Settle the calendar allocation if the pre-unit start-of-year readiness check must occupy a separate meeting within the 160-day course. The active brief requires that placement, while the repository writing rule currently permits the existing day-1 placement.

**Verdict:** Sound architecture; revise before unit planning. **Finding count:** 5. **Report path:** `docs/reviews/sequence-math-grade-5-2026-11-15.md`, supplied here only.
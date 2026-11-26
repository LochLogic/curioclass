# Frame read: computer-science-grade-11

2026-11-26 | Independent second reader | Read-only report

## Verdict

The frame has a sound content structure: all 13 selected progression rows are placed once, its owned standards match the units, and its calendar fits 64 course days. The biggest risk is assuming students took earlier computer science electives, followed by a model-testing sequence that uses test results to choose training-data changes. Five findings need correction before scope and sequence, without changing the six-unit structure or calendar.

## What was read and checked

- The frame-read brief, applicable frame-write rules and after-core changes, EXPERT.md, and the computer science lens.
- The subject adoption bar, STANDARD.md and APPROACH.md, with shared foundation, approach, production and decision rules.
- `docs/courses/computer-science-grade-11/frame.md`, its adjacent grade 10 and grade 12 frames, and relevant earlier frame, progression and pre-work reviews.
- The `grade:11` selector in `data/plans/course-list.csv`; all 13 selected progression rows, their ownership, prerequisites and outgoing links.
- The course’s frames and calendar rows, grade 11 core check weeks, and the mathematics progression for percent and scatter plots.
- All 12 Foundational and four Specialty standards’ boundary statements in the stored 2026 CSTA PDF, checked beside the published source.

No files were changed.

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check computer-science-grade-11` | One stage-related failure: day-level plan data is absent. Course-filtered to honor repository instructions. |
| `python -X utf8 scripts/frame.py check computer-science-grade-11` | 0 failures; 60 unit days plus four course-level check/respond days. |
| `python -X utf8 scripts/stale.py check` | 121 files checked, 0 failures. Unmarked stale statements remain. |
| Independent placement and ownership check | All 13 skills placed exactly once; no owned-standard mismatches; outgoing progression links reciprocal. |
| Calendar comparison | Mid-year check day 35, week 18; year-end check day 63, week 32. Both match the calendar rows and applicable calendar rules. |

The plan-stage failure does not block this frame verdict. This is a single-grade course, so the band-course Year column requirement does not apply.

## Findings

### 1. Serious: the entry path assumes earlier electives were taken

**LAYER:** frame  
**REPEAT:** yes, combined grades 6 to 12 review S1  
**Confidence:** firm

**Location:** Incoming Seams introduction and table, frame lines 161 to 185; unit openings.

The frame says every grade 10 prerequisite opens through retrieval because it was taught the year before. STANDARD.md describes these courses as electives, and frame-write rule 32 prohibits assuming an optional course was taken.

A student who skipped grade 10 encounters functions, lists, documentation, data cleaning and network diagrams without a stated teaching path. The readiness checks on two older rows do not address this.

**Exact fix:** Add a **Course order** bullet:

> Earlier computer science electives are helpful but are not assumed. Each unit checks the prerequisite concepts it uses. Students who demonstrate them begin with retrieval; students who do not receive a worked example and supported practice before independent work.

Add one combined ten-minute prerequisite check at each existing point:

| Unit entering | Placement | Concepts checked |
|---|---|---|
| 1 | Last ten minutes of day 1, after the hook | Confidentiality, integrity, availability, and reading a simple network diagram |
| 2 | Last ten minutes of day 9 | Tracing functions with lists, reading a short documentation entry |
| 3 | Last ten minutes of day 23 | Reading a three-variable chart and cleaning a few data rows |
| 4 | Last ten minutes of day 36 | Matching a model type to a task, checking data values, reading a test-table |
| 5 | Last ten minutes of day 48 | Identifying users, benefits, harms and exposure from data collection |
| 6 | Last ten minutes of day 55 | Reading an infrastructure diagram, a policy timeline and a team-role plan |

Combine these with the existing readiness checks, rather than scheduling two checks in the same ten minutes. Add a fallback column to Seams naming the worked example and supported practice within each unit’s opening Understanding lessons. Retain retrieval for students who demonstrate readiness.

### 2. Serious: unit 4 uses the test results to choose model changes

**LAYER:** frame  
**REPEAT:** new in the computer science reviews consulted  
**Confidence:** likely

**Location:** Unit 4, frame line 237, sessions 4 to 9; model-training tool description.

Session 4 teaches why test examples stay unseen. Sessions 6 and 7 then expose the test results and use them to decide which training-data changes to keep. That table remains useful for comparing revisions, but it has become development evidence rather than an independent final test.

This teaches students to optimize against the evidence later used to support an accuracy claim. The distinction matters even with a small classroom model. The primary technical guidance explicitly separates model choices from final test data. [Common pitfalls and recommended practices](https://scikit-learn.org/stable/common_pitfalls)

**Exact fix:** Keep the same sessions, but use three supplied piles:

- **Session 4:** Separate training examples, examples for comparing revisions, and a sealed final test set.
- **Session 6:** Examine results on the comparison set.
- **Session 7:** Choose training-data changes using that same comparison table.
- **Session 8:** Build the chosen-task model, keeping its final test examples separate.
- **Session 9:** Freeze the model, run the final test once, then write the accuracy claim and limitations.

Update the pseudocode, model report, tool ask and card-model path accordingly. Explain this in plain language; no cross-validation or additional mathematics is needed. Claims based on the comparison table must identify that table as previously used during revision.

### 3. Serious: the Specialty allocation does not substantiate the claimed share below 10 percent

**LAYER:** frame  
**REPEAT:** yes, combined review S2  
**Confidence:** firm on the accounting gap; likely on the eventual share

**Location:** Days bullet and “Days outside the standards,” frame lines 24 to 29 and 50 to 55; units 1 to 4.

The frame counts unit 3 sessions 5 and 6 together as one lesson equivalent, although both are described as Specialty sessions and no partial allocation is stated. Counting those as two, while accepting every other estimate, gives **5.5 of 52 teaching days, or 10.6 percent**.

Unit 1 session 2 also teaches data states and control types used by the Specialty standard but is absent from the allocation. The frame therefore cannot currently support its stated 4.5-day total.

C1 and STANDARD.md require Specialty work to count toward the outside-content limit. Shared lessons need explicit allocations.

**Exact fix:** Replace the estimate with this five-day-equivalent budget, and state the remaining Foundational work in each split session:

| Specialty work | Allocation |
|---|---:|
| Unit 1 sessions 2 and 3: data states, controls and threat classification | 2 |
| Unit 2 session 3 and half of session 4: unit/integration testing and generated test suggestions | 1.5 |
| Unit 3 half of session 5 and half of session 6: convention analysis and correction | 1 |
| Unit 4 half of session 7: training-data modification and comparison | 0.5 |
| **Total** | **5 of 52 teaching days, 9.6 percent** |

Use the remaining halves for the existing Foundational tasks: evaluating program correctness, judging what charts support, and selecting/reviewing the next model dataset. Keep the chart revision in session 7. Require the scope writer to count all outside-content minutes, including shared lessons, against this budget.

This preserves every named Specialty standard and adds no days.

### 4. Moderate: the course-level checks need bounded task forms and a time budget

**LAYER:** frame  
**REPEAT:** yes, assessment-load pattern in combined review S3  
**Confidence:** likely

**Location:** Course-level checks, frame lines 245 and 246; Evidence bullet.

The mid-year sitting combines chart and simulation evaluation, a corrected chart, an individual caption, a security solution and generated-code testing. The year-end sitting combines infrastructure analysis, a policy modification and three earlier-unit samples.

Calling these “short” or “40-minute” does not constrain their reading and writing demands. A later writer could reasonably produce several full performances from either row, leaving students unable to finish.

**Exact fix:** Keep the current check dates, but replace the open task descriptions with a bounded blueprint:

| Check | Required task form | Task minutes |
|---|---|---:|
| Mid-year | One linked chart-and-simulation case, including one small convention correction | 20 |
|  | Individual caption explaining the already revised chart | 5 |
|  | One described flaw with a concise mitigation | 5 |
|  | One short generated function tested against supplied cases | 5 |
| Year-end | One infrastructure chain with a concise explanation | 6 |
|  | One policy modification with its rationale and affected group | 8 |
|  | Individual justification referring to the already revised design document | 4 |
|  | Training-data review sample | 6 |
|  | Model-claim sample | 5 |
|  | Algorithm-impact sample | 6 |

Each blueprint totals 35 task minutes, leaving five minutes within the stated sitting for directions and collection. Score the previously revised products outside the sitting. Give each unseen task a response limit, supplied evidence and stated look-fors.

The unit writer must verify these limits against the actual items. I agree with the earlier review’s workload concern, but the available evidence does not establish that every grade needs a uniform two-lesson check.

### 5. Minor: the lead notes report work as missing or failing when current files show otherwise

**LAYER:** process  
**REPEAT:** yes, combined review M4 and earlier stale-note findings  
**Confidence:** firm

**Location:** For the lead 2, frame lines 272 to 278; header line 3.

The frame says the grade 12 frame does not exist. It does, and its incoming Seams table picks up the grade 11 handoffs. It also says a grade 10 note “now fails stale.py,” although that note has already been replaced and the checker reports zero failures.

These statements send the lead toward completed work.

**Exact fix:** Replace For the lead 2 with:

> **Seams with grades 10 and 12.** Both adjacent frames exist. Grade 10’s outgoing table matches this frame’s incoming rows. Grade 12’s incoming table picks up this frame’s outgoing rows in units 1 to 5. Its introductory statement that grade 11 unit numbers are not cited should be replaced by the corresponding unit numbers from this frame’s outgoing Seams table.

Change `catalogue id` to `catalog id` in the header to follow the US-spelling rule.

## Lens checklist, course-frame layer

| Lens line | Result |
|---|---|
| All five concepts receive taught time | Met. Programming occupies 14 of 60 unit days; data, systems, algorithms and society have substantial units. |
| Read and predict, then modify, then make | Met explicitly in unit 2 and stated as the course rule. Entry prerequisites need finding 1’s fallback. |
| Unplugged work teaches an idea; device work tests it | Met at frame level in every unit. |
| The notional machine is taught | Met through tracing, list diagrams, test-tables and assignment wording. |
| Debugging and testing are explicit methods | Met for programs; model evaluation needs finding 2. |
| Practices sit inside content | Met. Practices have content tasks; pair roles switch. |
| Society uses evidence, dated sources and multiple views | Planned. Actual case packs and their evidence remain to be checked. |
| Non-specialist teacher support | Required by the inherited approach; actual explanations, solutions and bug guidance are later-layer checks. |
| No construct is assumed before teaching | Missed for students without earlier electives, finding 1. |
| Standards reach their boundary depth | Substantial teaching is present for all 16 owned ids. Assessment time remains a risk, finding 4. |
| Specialty claims fit the Foundational course; no S2 claims | Named S1 list is permitted; time accounting needs finding 3. No S2 is claimed. |
| AI is integrated rather than confined to a late isolated unit | Met through generated-code evaluation, model development and impact analysis. |
| No unit lacks an unplugged path | Met. |
| Doing is assessed through code, products and reasoning | Met in the proposed forms; final rubrics and individual evidence remain later checks. |
| Tools have named jobs and require no student accounts or installation | Met in the specification. |
| No unsupported general-thinking claim | Met. |

## Settled by the expert

| Choice | Decision | Reason | Files affected |
|---|---|---|---|
| Unit structure and calendar | Keep six units and 64 days | Ownership, sequence and calendar arithmetic hold | Grade 11 frame |
| Elective entry | Add combined checks and named teaching fallbacks | Existing rule 32 already requires this | Grade 11 frame |
| Model evaluation | Separate revision comparisons from final testing | Preserves an interpretable final accuracy claim | Frame and corresponding progression notes |
| Specialty time | Budget five of 52 teaching-day equivalents | Makes the shared-session allocation explicit | Grade 11 frame |
| Assessment format | Keep dates; bound tasks and response lengths | Resolves the frame-level ambiguity without a new band-wide rule | Grade 11 frame |
| Second-largest function | Specify “second-largest distinct value”; define the insufficient-values result and prohibit input mutation | Makes repeated-value tests unambiguous | Unit 2 specification |

No standard moves between grades or units.

## What is right and should not be touched

- The security-to-testing-to-data-to-model sequence, followed by impact analysis.
- The distinction between owned standards, review and contributions to grade 12.
- The high-level security solution, which does not require implementing an attack or fix.
- The honest “part met without a device” marks for model training and visualization creation.
- Draft, written-feedback and revision placements for the chart, model report and design document.
- The safeguards against personal-data collection and testing real systems.

## What could not be judged

The tools, actual assessment items, rubrics, saved code and case packs do not yet exist at this layer. Their correctness, accessibility, individual evidence and completion time cannot be certified from the frame.

The Washington recycling example is a viable source direction, but the detailed policy proposal and unnamed local data-center case remain unverified teaching materials. The frame’s “from memory” markings must remain until their specific facts are checked. No finding here rests solely on subject-matter memory.

## Sources

- [2026 CSTA PK–12 Computer Science Standards](https://csteachers.org/wp-content/uploads/2026/07/2026-CSTA-PK%E2%80%9312-Computer-Science-Standards.pdf): checked all 16 claimed standards’ boundaries, including device requirements and excluded technical depth.
- [Common pitfalls and recommended practices](https://scikit-learn.org/stable/common_pitfalls): distinguishes model-development choices from final test evidence.
- [Computing pedagogy](https://www.raspberrypi.org/teach/pedagogy): checked the read, investigate, modify and make sequence.
- [NIST SP 1270](https://www.nist.gov/publications/towards-standard-identifying-and-managing-bias-artificial-intelligence): verified the proposed bias-background source.
- [CARE Principles for Indigenous Data Governance](https://www.gida-global.org/careprinciples): verified the Indigenous-authored source and its current address.
- [Washington electronics recycling guidance](https://ecology.wa.gov/regulations-permits/guidance-technical-assistance/electronics-ecycle-guidance-and-reports): confirmed an official starting source for the recycling-policy case.

## For the source list

Replace the frame’s CARE address ending in `/care`, which returned 404, with the working `/careprinciples` address. Add the model-evaluation guidance above if the lead retains that technical evidence in APPROACH-SOURCES.md.

## For Cory

- Existing decision only: whether to authorize the unit 3 weather-data download or use the frame’s invented-data fallback.
- The five corrections introduce no new scope, audience, spending or outside-person decision.


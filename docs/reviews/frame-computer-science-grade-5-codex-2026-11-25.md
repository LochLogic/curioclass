# Independent frame read: computer-science-grade-5

2026-11-25. Read-only report supplied inline. No report file was created.

## Verdict

**Needs fixes before scope and sequence writing.** The five-unit structure, ownership placement, calendar, and grade-to-grade handoffs are sound. The main risk is recording full coverage from assessment tasks or paper versions that omit required actions. Keep the units and 32-session budget, but repair those evidence contracts and the session-level pacing.

**Findings: 7, most serious first.**

## What I read

- The complete grade 5 frame and the adjacent grade 4 and grade 6 frames.
- `frame-read.md`, the after-core requirements in `frame-write.md`, `EXPERT.md`, the computer science lens, STANDARD, APPROACH, and adoption bar.
- FOUNDATION, relevant production-path and BASELINE rules, shared APPROACH, GLOSSARY, calendar rules, subject decisions, and base-text guidance.
- The course’s `grade:5` selector in `course-list.csv`, its `frames.csv` and calendar rows, all 16 selected progression rows, and their incoming and outgoing links.
- All 19 E5 statements and boundary statements in the stored CSTA PDF, checked beside the live publication.
- The cited math and science Units rows and calendar placements.
- Relevant pre-work, progression, kindergarten, combined elementary, and grade 4 reviews.
- The outside sources linked below.

Prior memory informed the review workflow only. No substantive finding rests on model memory.

## Checks and calendar

| Check | Result |
|---|---|
| `python -X utf8 scripts/frame.py check computer-science-grade-5` | Passed: 0 failures; 28 unit days plus 4 course-check and respond days |
| `python -X utf8 scripts/plan.py check computer-science-grade-5` | Failed because the later plan-stage CSVs do not exist; this does not prevent a frame verdict |
| `python -X utf8 scripts/stale.py check` | Passed: 121 files, 0 failures |
| Independent ownership and seam check | 16 skills placed once, 19 owned standards, no missing reciprocal handoffs |

The plan command was course-filtered under AGENTS.md; the consolidated gate was not run because it writes output and baseline files.

The calendar matches the frame: units occupy weeks 1 to 5, 6 to 10, 11 to 17, 20 to 24, and 27 to 32. Course checks occupy weeks 18 and 25, followed by respond weeks 19 and 26. Neither check overlaps a grade 5 core check week. The disclosed after-core clashes belong to the lead’s calendar pass.

This is a single-grade course, so the band-course Year column is not applicable.

## Findings

### 1. Unit 3’s assessment does not establish all the programming outcomes it claims

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, assessment-action gaps recur in the kindergarten read; the combined elementary review also identified the thin remix item  
**Confidence:** Firm

**Location:** [Unit 3](/S:/CurioClass/docs/courses/computer-science-grade-5/frame.md:252), Evidence bullet, and [mid-year check](/S:/CurioClass/docs/courses/computer-science-grade-5/frame.md:260).

Day 18 claims to score unit 3 in full, but:

| Outcome | Gap in the specified evidence |
|---|---|
| E5-PRO-VD-06 | Tracing a supplied score program does not establish the student’s own use of variable storage, comparison, and updating. |
| E5-PRO-PD-05 | Building a missing component individually does not establish collaborative integration and testing. The actual team project receives feedback only. |
| E5-PRO-TR-08 | The check records one chosen strategy, without requiring evidence that each student applied more than one. |
| E5-PRO-PD-04 | Adding a prescribed segment leaves purposeful modification and an individual variation insufficiently specified. |

These distinctions follow the [published boundaries, PDF pages 56, 60, and 66, printed pages 51, 55, and 61](https://csteachers.org/wp-content/uploads/2026/07/2026-CSTA-PK%E2%80%9312-Computer-Science-Standards.pdf).

**Why it matters:** A teacher could award completion while observing only tracing, isolated construction, or prescribed assembly.

**Exact fix:**

- Score the revised session 7 project with an individual record: the student’s own component, its integration with teammates’ components, relevant tests, and documentation.
- Ensure every student’s variable evidence includes setting, updating, and comparing a value. Students whose project role lacks these actions complete a short supplied-shell modification.
- Across sessions 4 and 7, retain individual evidence of applying two debugging strategies, including the correction and retest.
- Replace day 18’s prescribed remix with a choice of two or three supplied segments. Each student selects one, makes a purposeful change, tests the resulting variation, credits the source, and explains the change.
- Revise Evidence and the check row to permit these scored later-session records alongside unseen check items. No score should come from the session that first teaches the row.

### 2. Unit 4’s check omits collection and relationships between variables

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, incomplete data-investigation evidence recurs in the kindergarten second-model read  
**Confidence:** Firm

**Location:** [Unit 4](/S:/CurioClass/docs/courses/computer-science-grade-5/frame.md:253) and [year-end check](/S:/CurioClass/docs/courses/computer-science-grade-5/frame.md:261).

The table task starts with supplied data, so it checks organization but not computational collection. The variability task checks typical values, an outlier, and possible causes, but omits the relationship between columns that the teaching description correctly includes.

See the [published boundaries, PDF pages 69 and 74, printed pages 64 and 69](https://csteachers.org/wp-content/uploads/2026/07/2026-CSTA-PK%E2%80%9312-Computer-Science-Standards.pdf).

**Why it matters:** “Scores unit 4 in full” exceeds the evidence specified for two of its four standards.

**Exact fix:**

- Replace the supplied-table-only task with a small collection-and-organization task. Each student captures numeric and descriptive responses from fictional case cards through the local form, then sorts and groups the resulting table.
- Add a variability prompt asking students to describe one visible relationship between two columns, without calculating a statistic.
- Keep typical values, outliers, and possible sources of variation as separate look-fors.
- Mark the collection-and-organization standard part met on the paper path, as the frame already requires.

### 3. The paper path overstates full coverage of variable programming

**Severity:** Serious  
**LAYER:** frame, progression  
**REPEAT:** yes, incorrect full-coverage claims for paper substitutes recur in the earlier elementary reads  
**Confidence:** Likely

**Location:** [Devices bullet](/S:/CurioClass/docs/courses/computer-science-grade-5/frame.md:108), unit 3, and progression row `g5-variables-use`.

The frame says every E5 ID except the collection and training IDs is met fully on paper. E5-PRO-VD-06’s boundary specifies using variables in a block-based or beginner text-based environment. Printed tracing remains valuable, but the blanket claim does not distinguish simulated execution from use in that environment.

See [PDF page 60, printed page 55](https://csteachers.org/wp-content/uploads/2026/07/2026-CSTA-PK%E2%80%9312-Computer-Science-Standards.pdf#page=60). This also follows the earlier review’s distinction between paper algorithms and a required programming environment.

**Why it matters:** A no-device school could record full variable-programming coverage from paper tracing alone.

**Exact fix:**

- Add E5-PRO-VD-06 to the IDs marked **“part met without a device.”**
- Retain paper construction, tracing, and partner execution as instruction and supporting evidence.
- State that full coverage requires the student to construct or modify variable behavior in the browser environment and test it.
- Mirror this qualification in `g5-variables-use.notes`, Devices, Paper path, and the assessment records.
- For stations or one screen, identify each student’s actual programming contribution rather than treating class observation as equivalent evidence.

### 4. The assessment schedule exceeds its own available time

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, assessment overload was identified in the combined elementary and grade 4 reads  
**Confidence:** Firm on the arithmetic; likely on classroom feasibility

**Location:** Days and Evidence bullets; both course-check rows.

The frame reserves three minutes for retrieval and four for device closure, leaving about 33 minutes. Its stated 25-minute paper plus 10-minute practical already totals 35 minutes, before setup. Day 18 also includes two practical constructions, and day 25 requires both table operations and model retraining. One device per pair requires time for both students’ evidence.

**Why it matters:** The scope writer inherits a schedule that cannot meet its own routine, even before access accommodations.

**Exact fix:**

- Use the session 7 programming records described in finding 1.
- Score the trained and refined model in unit 4 session 4, after its initial teaching in session 3. Retain each student’s training choices, test count, and explanation.
- Make day 18 a provisional 20-minute written component plus 10 minutes of practical rotations.
- Make day 25 an 18-minute written component plus 12 minutes of collection-and-organization rotations.
- State that those practical allowances cover both students in a pair.
- Carry the scored project and model records into the checks; remove the duplicate timer-build and model-retraining tasks from those sittings.
- Replace the universal “25 plus 10” description with these explicit budgets.

These are planning allowances, not established classroom timings.

### 5. The first model-training session lacks the promised worked example

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, make-before-modify was identified in the kindergarten second-model read  
**Confidence:** Likely

**Location:** [Unit 4, sessions 3 and 4](/S:/CurioClass/docs/courses/computer-science-grade-5/frame.md:253).

Session 3 begins with pairs building a labeled set and training their model. The first explicit modification follows in session 4. Grade 4 prepares the concept of training-data effects, but does not teach students this tool’s training workflow.

This conflicts with APPROACH’s requirement to show and trace a worked example before students try a new construct. The [PRIMM summary](https://static.raspberrypi.org/files/curriculum/quickreads/11-Pedagogy_Summary_PRIMM_V4_2023.pdf) supports gradual transfer from supplied examples; applying that structure to elementary model training remains Curio Class’s untested adaptation.

**Why it matters:** A scope writer could open the first training-tool session with independent construction despite the frame’s stated teaching order.

**Exact fix:** Open session 3 with a supplied labeled set and a teacher-modeled training-and-test cycle. Students predict outputs, inspect results, and modify one example before building their own small set. Keep session 4 for varied examples, refinement, and the later scored evidence described in finding 4. Name this sequence in both the unit row and Day kinds.

### 6. Five debugging strategies are crowded into one teaching session

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, finding M5 in the combined elementary review  
**Confidence:** Likely

**Location:** [Unit 3, sessions 3 and 4](/S:/CurioClass/docs/courses/computer-science-grade-5/frame.md:252).

Session 3 asks students to try three strategies in turn, adds error-message reading and temporary output, and records their use. That is a dense introduction within roughly 33 instructional minutes. The boundary’s examples are being treated like a compulsory five-strategy checklist.

**Why it matters:** Students may name strategies without learning when and how to apply them.

**Exact fix:**

- Session 3: model and practice hand tracing and testing one part at a time.
- Session 4: introduce isolation by removing pieces, then let students choose and compare strategies on new bugs.
- Keep message reading and temporary output as optional techniques used when the example warrants them.
- Require individual evidence of two applied strategies, as finding 1 specifies.
- Update the outgoing seam’s summary to match the three taught strategies.

### 7. Stale status wording and small factual inconsistencies remain

**Severity:** Minor  
**LAYER:** process, progression, frame  
**REPEAT:** yes, wording, column-reference, device-share, and network-note issues appear in the combined elementary review  
**Confidence:** Firm

**Location:** Opening; Days, Practices, and Devices bullets; Cross-subject; For the lead item 5; `g5-network-parts.notes`.

| Problem | Exact fix |
|---|---|
| For the lead item 5 says the lead must apply changes already present in the progression. | Replace it with: “The progression already contains the listed grade 5 depth and spelling changes. No application remains from this list.” Change the Standard bullet’s reference accordingly. |
| The Practices column is called the fifth column. | Refer to it by its heading, “Practices and concept areas.” |
| The opening uses “catalogue id.” | Change it to “catalog id.” |
| Cross-subject says science meets every school day. | State that math meets five days a week and grade 5 science four, with course days converted through the calendar. Keep the correctly cited science weeks 25 to 30. |
| Devices infers a share of yearly time from a list of about 12 device-containing sessions, excluding check and respond usage. | Replace the time claim with: “About 12 of the 22 teaching sessions contain device work, several only in part. The scope and sequence will total device minutes, including assessments and response.” |
| `g5-network-parts.notes` omits the switch taught in unit 1. | Add “switch” to its component list. It is already in the row’s vocabulary. |
| “32 sessions for 16 rows” is described as below about two sessions per row. | Change this to “exactly two course sessions per row, including checks and respond days.” |

**Why it matters:** These inconsistencies send unnecessary work back to the lead and leave later writers with conflicting descriptions. The stale-note script does not detect the already-applied row-change list.

The earlier combined review prescribed a particular away-from-device proportion. This read does not adopt that correction: session counts alone do not establish minutes.

## Settled by the expert

| Choice | Reason | Files affected |
|---|---|---|
| Keep five units and 32 sessions | Ownership and relative loads support the structure | Grade 5 frame |
| Keep the current unit order | Systems precede later device work; algorithm plans precede programming; data precedes training | Grade 5 frame |
| Score individual project evidence in session 7 | Preserves collaboration evidence and releases check time | Evidence, unit 3, checks |
| Score model refinement in session 4 | Uses later application rather than first teaching | Evidence, unit 4, checks |
| Teach three debugging strategies over two sessions | Meets the intended breadth without requiring every illustrative technique | Unit 3 and outgoing seam |
| Add collection and a relationship prompt to unit 4 evidence | Repairs omissions within existing ownership | Unit 4 and year-end check |
| Qualify the no-device variable-programming claim | Keeps useful paper instruction without overstating coverage | Frame and progression note |

No standard needs to move between units.

## Lens checklist, course-frame layer

| Lens requirement or error check | Result |
|---|---|
| All five concepts receive teaching | Met |
| AI has data and algorithm foundations | Met: unit 4 builds on earlier data and testing work |
| Read, predict, modify, then make | Mostly met; model-training workflow needs finding 5 |
| Meaningful unplugged work in every unit | Met |
| Explicit notional machine and variable tracing | Met |
| Debugging taught as a repeatable method | Met in intent; pacing and individual evidence need findings 1 and 6 |
| Collaboration and human-centered design inside content | Met in teaching; scored integration needs finding 1 |
| Society work uses dated evidence and perspectives | Required clearly; finished cases remain to be verified |
| Support for a non-specialist teacher | Met as a planning requirement through APPROACH and the named teacher materials |
| Constructs appear before dependent work | Met overall; first training-tool use needs finding 5 |
| Standards taught and checked at their boundary depth | Assessment and paper claims need findings 1 to 3 |
| No unsupported Specialty or X + CS claims | Met |
| Device feedback serves named purposes | Met in design |
| Tools avoid accounts, installation, and off-device storage | Required clearly; implementation not yet judged |
| Projects and code assessed with rubrics | Partly met; the team project currently receives feedback only |
| No claims of general thinking or attainment gains | Met |
| Middle-school text-code transition | Met at the seam: grade 6 explicitly bridges blocks and text |
| Finished code, keys, error messages, and pair-role execution | Not applicable yet; later-layer checks |

## What is right and should not be touched

All 16 selected skills are placed exactly once, and all 19 owned IDs appear. Incoming and outgoing progression links are reciprocal. Grade 6 explicitly picks up the grade 5 models and provides the blocks-to-text bridge.

The calendar arithmetic is correct. Unit 5 has its own assessment and respond day after the course-level check, so its late placement does not leave it unassessed.

The math and science leans have usable bridges. Math’s pattern work arrives in weeks 27 to 30; the earlier computer science work limits itself to familiar counting. Science’s design-testing unit arrives in weeks 25 to 30; computer science supplies its own repeated-trial explanation in week 21.

The source map accounts for all 36 Year 6 base lessons: 13 used wholly or in part, 23 explicitly excluded. Its major reorderings are explained. The public [archive listing](https://www.raspberrypi.org/curriculum/archived/key-stage-2) and four mapped unit pages confirm the unit and lesson identities.

The privacy provisions are specific: invented cases, drawings rather than faces or voices, pretend accounts, local storage, and no questions about students’ homes or families.

## What I could not judge

- Full base-lesson contents, third-party permissions, or the feasibility of compressing their activities. The frame correctly identifies its title-and-overview mapping as provisional.
- Finished editor, table, and training tools, including access behavior and saving.
- Actual assessment timings, finished rubrics, keys, or teacher workload.
- The factual accuracy and perspectives of society cards that have not yet been written.

No additional stale note was established beyond finding 7. Dated review records should remain unchanged.

## Sources checked outside the repository

- [2026 CSTA PK to 12 Computer Science Standards](https://csteachers.org/wp-content/uploads/2026/07/2026-CSTA-PK%E2%80%9312-Computer-Science-Standards.pdf): all E5 boundaries and exclusions.
- [Archived key stage 2 curriculum](https://www.raspberrypi.org/curriculum/archived/key-stage-2): Year 6 unit identities and lesson-order guidance.
- [Communication and collaboration](https://www.raspberrypi.org/curriculum/archived/key-stage-2/computing-systems-and-networks-communication): mapped communication lessons and excluded addressing lessons.
- [Variables in games](https://www.raspberrypi.org/curriculum/archived/key-stage-2/programming-a-variables-in-games): variable development, design, and six-lesson sequence.
- [Introduction to spreadsheets](https://www.raspberrypi.org/curriculum/archived/key-stage-2/data-and-information-spreadsheets): collection, formatting, and excluded later work.
- [Sensing movement](https://www.raspberrypi.org/curriculum/archived/key-stage-2/programming-b-sensing): step-counter lesson identity and prior constructs.
- [PRIMM pedagogy summary](https://static.raspberrypi.org/files/curriculum/quickreads/11-Pedagogy_Summary_PRIMM_V4_2023.pdf): supplied examples and gradual movement toward independent creation. It does not establish this grade 5 course’s effectiveness.

## For Cory

- **Training-tool scope:** Resolve the frame’s existing question about building the local drawing-based training tool. Until a suitable tool exists, retain an explicit partial-coverage qualification for the training ID.
- **Base-material scope:** Confirm the archived edition to load so lesson-level and license checks can replace the provisional public-page mapping.

## For the source list

Add the four specific archived unit links above beside the general archive address. No new research claim is proposed.


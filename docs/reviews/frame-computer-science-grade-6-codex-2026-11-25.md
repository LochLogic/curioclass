# Independent frame read: computer-science-grade-6

2026-11-25. Read-only review. No file was created or changed.

## Verdict

**Needs fixes before scope and sequence writing.** The six-unit structure, ownership placement, prerequisite order and grade-to-grade handoffs are sound. The main risk is that writers would inherit assessment claims that exceed the specified evidence, crowded checks, and incorrect descriptions of adapted lessons; repair those contracts while preserving the course’s breadth and 64-session budget.

**Findings: 6, most serious first.**

## What I read

- The complete grade 6 frame and the adjacent grade 5 and grade 7 frames.
- `frame-read.md`, the after-core provisions of `frame-write.md`, `EXPERT.md`, the computer science lens, STANDARD, APPROACH and adoption bar.
- FOUNDATION, relevant production-path and BASELINE rules, shared APPROACH, GLOSSARY, subject decisions and base-text guidance.
- The `grade:6` selector in `course-list.csv`, all 18 selected progression rows, adjacent-grade rows, `frames.csv` and the calendar rows.
- The grade 6 math and science Units tables.
- Relevant pre-work, progression and earlier frame reviews.
- The published standards and outside sources linked below.

Prior memory informed the review workflow only. No substantive finding rests on model memory.

## Checks and calendar

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check computer-science-grade-6` | Failed: the later plan-stage CSVs are absent; this does not prevent a frame verdict |
| `python -X utf8 scripts/frame.py check computer-science-grade-6` | Passed: 0 failures |
| `python -X utf8 scripts/stale.py check` | Passed: 121 files, 0 failures |
| Independent ownership check | All 18 selected skills placed exactly once; all 17 owned standards placed |
| Independent seam and model check | No missing reciprocal progression links; all 17 input/output models represented |

The plan command was course-filtered under AGENTS.md. The consolidated gate was not run because it writes output and baseline files.

The recorded calendar matches the frame:

| Component | Course days | School days | Weeks |
|---|---:|---:|---:|
| Unit 1 | 1 to 16 | 3 to 40 | 1 to 8 |
| Unit 2 | 17 to 27 | 43 to 68 | 9 to 14 |
| Unit 3 | 28 to 37 | 70 to 93 | 14 to 19 |
| Mid-year check and response | 38 to 39 | 95 to 98 | 19 to 20 |
| Unit 4 | 40 to 46 | 100 to 115 | 20 to 23 |
| Unit 5 | 47 to 53 | 118 to 133 | 24 to 27 |
| Unit 6 | 54 to 62 | 135 to 155 | 27 to 31 |
| Year-end check and response | 63 to 64 | 158 to 160 | 32 |

The mid-year check avoids grade 6 core check weeks. Week 32 permits the year-end overlap. Other after-core clashes remain the lead’s calendar pass.

This is a single-grade course, so the band-course Year column does not apply.

## Findings

### 1. Three assessment descriptions omit actions needed for the claimed coverage

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, incomplete assessment actions recur in the kindergarten, grade 4 and grade 5 reads  
**Confidence:** Firm

**Location:** [Unit 4](/S:/CurioClass/docs/courses/computer-science-grade-6/frame.md:247), [mid-year check](/S:/CurioClass/docs/courses/computer-science-grade-6/frame.md:255), [year-end check](/S:/CurioClass/docs/courses/computer-science-grade-6/frame.md:256), and Evidence.

| Outcome | Gap |
|---|---|
| MS-DAT-DC-22 | Answering from a supplied printed or on-screen properties panel does not demonstrate opening a computational tool to view metadata. |
| MS-ALG-ML-06 | Unit 4’s assessment asks for a hypothesis and a proposed test, but does not require performing the experiment and interpreting its result. |
| MS-SOC-HI-38 | The year-end item compares actors within one era, although the taught comparison extends across eras. |

These distinctions follow the [published boundaries, PDF pages 47, 70 and 95, printed pages 42, 65 and 90](https://csteachers.org/wp-content/uploads/2026/07/2026-CSTA-PK%E2%80%9312-Computer-Science-Standards.pdf).

**Why it matters:** A teacher could record full coverage from explanations that omit the required action or comparison.

**Exact fix:**

- In the mid-year check, have each student open a supplied file’s properties, locate relevant metadata and use it to answer the question. A printed-panel response remains available and is marked **part met without a device**.
- In unit 4’s assessment, have students select new classifier inputs, obtain outputs, record whether these support their hypothesis and revise it if necessary.
- Replace the year-end history item with two short source cards from different eras. Students compare two actor types’ roles, motivations and interactions across those eras.
- Update Evidence and the assessment descriptions together.

### 2. Both course-level checks carry too much work for one sitting

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, the combined grades 6 to 12 review, S3, already identifies this grade 6 risk  
**Confidence:** Likely

**Location:** [Course-level checks](/S:/CurioClass/docs/courses/computer-science-grade-6/frame.md:251).

The mid-year sitting combines four data outcomes, a computational table task, written reasoning and three earlier-unit items. The year-end sitting combines four substantial systems and society tasks, source reading and three earlier-unit items. Each receives about 40 minutes, within a course that also reserves setup and collection time.

**Why it matters:** Students may demonstrate speed and reading endurance instead of the intended computing knowledge. The repair in finding 1 makes the evidence stronger but increases the pressure.

**Exact fix:** Give each course-level check two sessions: one for the immediately preceding unit and one for earlier-unit samples. Retain one respond session after each.

Keep 64 sessions through these specific changes:

- Reduce unit 1 from 16 to 15 sessions by folding its standalone session 7 build into the existing team project. Preserve the draft, written feedback, revision, assessment and response.
- Reduce unit 6 from nine to eight sessions by combining the worked system comparison and its invented-user choice in one Understanding session.
- The resulting unit totals are **15, 11, 10, 7, 7 and 8**, totaling 58. Four course-check sessions and two respond sessions bring the course to 64.

The revised mid-year checks occupy course days 37 and 38, school days 93 and 95, both in week 19; response remains day 39. The year-end checks occupy course days 62 and 63, school days 155 and 158, in weeks 31 and 32; response remains day 64. These placements avoid core checks outside finals week.

Update the Days bullet, check descriptions, session references and generated calendar together. This is a local pacing recommendation, not a new rule for every computer science course.

### 3. Fluency examples include first teaching

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, the kindergarten second-model read also found new work placed under Fluency  
**Confidence:** Firm

**Location:** [Day kinds](/S:/CurioClass/docs/courses/computer-science-grade-6/frame.md:73), unit 1 and unit 3.

The frame labels these as Fluency:

- Unit 1 session 3 introduces string joining, Boolean manipulation and type conversion.
- Unit 1 session 6 introduces further programming patterns, including maximum/minimum tracking.
- Unit 3 session 6 introduces grouping, summaries and the average, including an explicit bridge ahead of math.

Under GLOSSARY, first teaching is Understanding. The subject APPROACH also defines Fluency as practice of earlier teaching.

**Why it matters:** The scope writer could omit worked teaching because the frame presents these methods as already learned.

**Exact fix:**

- Classify unit 1 session 3 and unit 3 session 6 as **Understanding**.
- Classify unit 1 session 6 as Understanding where it first introduces maximum/minimum or another new pattern. Its later repetitions can be Fluency.
- Replace the Day kinds examples with: “Fluency practices previously taught constructs and operations. A session that introduces a new operation, programming pattern or math bridge is Understanding, even when students modify a working example.”

No additional session is required.

### 4. The source map assigns several lessons the wrong content

**Severity:** Serious  
**LAYER:** base text  
**REPEAT:** yes, source-map adaptation gaps appeared in the kindergarten read; these particular mismatches are new  
**Confidence:** Firm

**Location:** [Source map](/S:/CurioClass/docs/courses/computer-science-grade-6/frame.md:311), units 1, 3 and 5, and their Check set adds cells.

The public lesson pages establish several mismatches:

- Programming lesson 7 teaches subroutines, but [lesson 8](https://www.raspberrypi.org/curriculum/archived/key-stage-3/programming-essentials-in-scratch-part-ii/fly-cat-fly) teaches condition-controlled loops. [Lesson 9](https://www.raspberrypi.org/curriculum/archived/key-stage-3/programming-essentials-in-scratch-part-ii/loop-de-loop) evaluates which loop type to use. They are not another subroutine lesson and simple count-controlled-loop review.
- Spreadsheet [lesson 2](https://www.raspberrypi.org/curriculum/archived/key-stage-3/modelling-data-spreadsheets/quick-calculations) teaches formulas, cell references and autofill. [Lesson 4](https://www.raspberrypi.org/curriculum/archived/key-stage-3/modelling-data-spreadsheets/become-a-data-master) supplies the totals, counts, minimum/maximum functions and chart work attributed elsewhere.
- The network [Privacy lesson page](https://www.raspberrypi.org/curriculum/archived/key-stage-3/networks-from-semaphores-to-the-internet/the-world-wide-web) does not establish the claimed triangle-case lesson. Its description and objectives are themselves inconsistent.

**Why it matters:** A writer following the map would retrieve different teaching from what the frame promises.

**Exact fix:**

- Map programming lesson 7 to unit 1’s procedure sessions. List lessons 8 and 9 as excluded because this adaptation retains count-controlled iteration and does not take their condition-controlled-loop and loop-selection sequence.
- Treat spreadsheet lesson 2 as excluded from the adaptation. Map lesson 4’s summary functions to unit 3 session 6 and its chart portion to session 7. Identify sorting, filtering, grouping and the average bridge as Curio Class additions where the mapped source does not supply them.
- Treat unit 5 session 4’s triangle cases as Curio Class work. Remove the claim that network lesson 6 supplies them; list that lesson as excluded unless the eventual file inspection establishes a usable part.
- Correct the corresponding unit descriptions, Check set adds cells and source-map closing paragraph.
- Correct the blanket “resources dated 2023” description: the opened [network unit](https://www.raspberrypi.org/curriculum/archived/key-stage-3/networks-from-semaphores-to-the-internet) lists 2024 resource updates.

Keep the existing pending file-license and third-party checks.

### 5. Unmarked stale notes remain despite the stale checker passing

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, combined grades 6 to 12 review, M4  
**Confidence:** Firm

**Location:** [For the lead, item 3](/S:/CurioClass/docs/courses/computer-science-grade-6/frame.md:289), and the introductory description of approach pages in `docs/ADOPTION-BAR-SUBJECTS.md`.

The grade 6 note says grade 7 leaves grade 6 unit numbers for a later seam read. Grade 7 now cites those units. The adoption-bar introduction also says no subject approach page exists, although the computer science approach page exists and records its approval.

**Why it matters:** These notes send the lead back to completed work and misstate the repository’s current state.

**Exact fix:**

- Replace grade 6’s lead item 3 with: “Grade 7’s Picked up table cites this frame’s units and matches the progression handoffs. Its unit 4 readiness provision covers a school that omitted grade 6 unit 4.”
- Replace the adoption-bar sentence with: “Layer 3 requires a subject approach page before scope and sequence writing; the subject pages and the owed table below record their current status.”

The lead applies the shared-document correction.

### 6. Unit 2’s compelling question promises proof that the unit excludes

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** Likely

**Location:** [Unit 2](/S:/CurioClass/docs/courses/computer-science-grade-6/frame.md:245).

The question asks students to “prove it works,” while the unit explicitly excludes proof and teaches verification for selected inputs. The [published boundary](https://csteachers.org/wp-content/uploads/2026/07/2026-CSTA-PK%E2%80%9312-Computer-Science-Standards.pdf) makes the same distinction.

**Why it matters:** The question overstates what the unit’s evidence can establish.

**Exact fix:** Replace it with:

> How can we show what an algorithm does, test it for given inputs, and see the same thinking in people’s jobs?

## Settled by the expert

| Choice | Decision and reason | File |
|---|---|---|
| Unit order | Keep. Variables precede procedures; procedures precede algorithm models; data precedes classifier investigation. | Grade 6 frame |
| Ownership | Keep all 18 selected rows and 17 owned ids in their present units. | Frame and progression |
| Assessment evidence | Require the missing actions and comparison in finding 1. | Evidence and assessment cells |
| Check allocation | Use the concrete 64-session redistribution in finding 2. | Frame; generated calendar |
| Day kinds | First teaching, including math bridges, is Understanding. | Day kinds and unit descriptions |
| Source adaptation | Correct the lesson identities without adding constructs or moving standards. | Source map and unit descriptions |
| Math and science leans | Keep the bridges. Their cited core unit ranges match the calendar. | Cross-subject |
| Unit 2 question | Say “test it for given inputs.” | Unit 2 |

## Lens checklist, course-frame layer

| Lens line | Result |
|---|---|
| All five concepts, with AI connected to content | Met. Programming, algorithms, data, systems/security and society receive substantive teaching. |
| Read, predict and modify before making | Met in the programming sequence; preserve during pacing edits. |
| Unplugged work followed by purposeful device work | Met in all six units. |
| Explicit notional machine | Met through named boxes, assignment language and tracing. |
| Debugging taught as a method | Met through prediction, comparison, test tables and retesting. |
| Collaboration and human-centered practices inside content | Met. Team roles, feedback and design evaluation have named tasks. |
| Society uses evidence and multiple views | Met as a frame requirement; finished source packs remain to be checked. |
| Support for a non-specialist teacher | Met as a stated obligation for explanations, tested solutions and common bugs. |
| No construct or model required before introduction | Met. |
| Blocks-to-text bridge | Met. Grade 6 reads both views before independent text work. |
| Standards taught to their boundaries | Teaching outline largely met; assessment contract missed in finding 1. |
| No inappropriate Specialty claim | Met. None claimed. |
| AI not a disconnected final unit | Met. Data precedes the mid-course classifier work. |
| Unplugged path in every unit | Met. |
| Performance and code evidence | Present, but check allocation needs finding 2. |
| Tools have named jobs and require no student account | Met as specifications; implementation is not yet verified. |
| Assignment distinguished from equality | Met. |
| No unsupported general-thinking benefit claim | Met. |
| Pair roles switch | Met. |

## What is right and should not be touched

- The balance across concept areas and the progression’s ownership map.
- The explicit limits on lists, parameters, protocols, advanced audits and model internals.
- The blocks-to-text bridge and trace-before-build structure. These are consistent with the [PRIMM pedagogy summary](https://static.raspberrypi.org/files/curriculum/quickreads/11-Pedagogy_Summary_PRIMM_V4_2023.pdf).
- The team project’s separate draft, written feedback and revision.
- Invented personal-data cases, local work storage, paper versions and explicit partial-coverage labels.
- The math bridges, packet-game controls and unit-specific sensitivity preparation.

## What I could not judge

- Actual completion times. The check-load finding is a planning judgment, not a timed classroom result.
- The archived lesson packages’ licenses, third-party exceptions and complete contents. Public lesson pages were readable; lesson-package downloads require login, and the source store remains pending.
- Whether the proposed editor, table tool and classifier meet their offline, access and evidence requirements.
- Finished teacher explanations, assessment keys and society source packs, which belong to later stages.

## Sources checked outside the repository

- [2026 standards publication](https://csteachers.org/wp-content/uploads/2026/07/2026-CSTA-PK%E2%80%9312-Computer-Science-Standards.pdf): owned-standard statements and boundaries.
- [Archived key stage 3 listing](https://www.raspberrypi.org/curriculum/archived/key-stage-3): source-unit inventory and sequencing guidance.
- [Programming part I](https://www.raspberrypi.org/curriculum/archived/key-stage-3/programming-essentials-in-scratch-part-i) and [part II](https://www.raspberrypi.org/curriculum/archived/key-stage-3/programming-essentials-in-scratch-part-ii): lesson inventory.
- [Programming lesson 7](https://www.raspberrypi.org/curriculum/archived/key-stage-3/programming-essentials-in-scratch-part-ii/you-ve-got-the-moves), lessons 8 and 9 linked in finding 4: procedure and iteration distinctions.
- [Spreadsheet unit](https://www.raspberrypi.org/curriculum/archived/key-stage-3/modelling-data-spreadsheets), with lessons 2 and 4 linked in finding 4: calculation and summary-function placement.
- Network unit and Privacy lesson linked in finding 4: source-map claims and edition dates.
- PRIMM summary linked above: support for the existing programming sequence.

## For Cory

None new. The findings preserve the approved course scope, ownership and total sessions.

## For the source list

Add the specific archived lesson URLs linked in finding 4, with their verified topics. Record the inconsistent network Privacy page and keep its package-level confirmation open.


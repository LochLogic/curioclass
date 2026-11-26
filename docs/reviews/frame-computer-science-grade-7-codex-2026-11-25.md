# Second-model frame read: computer-science-grade-7

2026-11-25. Read-only report supplied inline. No files were created or changed.

## Verdict

**Needs fixes before scope and sequence writing.** The six-unit structure, standard ownership, prerequisite order and calendar arithmetic are sound, but the frame assumes completion of the previous elective and specifies insufficient final evidence for the documentation standard. Repair those contracts, the first-teaching label and the source-map descriptions while preserving all six units and the 64-session budget.

**Findings: 8, most serious first.**

## What I read

- The complete [grade 7 frame](/S:/CurioClass/docs/courses/computer-science-grade-7/frame.md), adjacent grade 6 and grade 8 frames, and their relevant handoffs.
- `frame-read.md`, the after-core provisions of `frame-write.md`, `EXPERT.md`, the computer science lens, subject STANDARD and APPROACH, and the shared and computer science adoption bars.
- FOUNDATION, shared APPROACH, relevant production-path and BASELINE rules, GLOSSARY, subject decisions, calendar rules and base-text guidance.
- The `grade:7` selector in `course-list.csv`, all 19 selected progression rows, their reciprocal prerequisites and handoffs, `frames.csv`, and calendar rows.
- The grade 7 mathematics and science Units tables.
- Relevant computer science pre-work, progression and earlier frame reviews, including the combined grades 6 to 12 review and earlier second-model reads.
- All 15 owned standards and their full boundary statements in the published CSTA PDF, plus the outside sources linked below.

Prior memory informed the review workflow only. No substantive finding rests on model memory.

## Checks and calendar

| Check | Result |
|---|---|
| `python -X utf8 scripts/frame.py check computer-science-grade-7` | Passed: 0 failures |
| `python -X utf8 scripts/plan.py check computer-science-grade-7` | Failed because plan-stage CSVs are absent; this does not block a frame verdict |
| `python -X utf8 scripts/stale.py check` | Passed: 121 files, 0 failures |
| Independent placement check | All 19 selected skills placed exactly once; all 15 owned standards placed |
| Independent seam and model check | All progression links reciprocal; all 17 input/output models represented |
| Calendar comparison | All 10 stored course-calendar rows agree with the current frame |

The plan check was course-filtered under AGENTS.md; the consolidated gate was not run because it creates output and baseline files.

| Component | Course days | Weeks |
|---|---:|---:|
| Unit 1 | 1 to 10 | 1 to 5 |
| Unit 2 | 11 to 23 | 6 to 12 |
| Unit 3 | 24 to 31 | 12 to 16 |
| Mid-year check and response | 32 to 33 | 16 to 17 |
| Unit 4 | 34 to 43 | 17 to 22 |
| Unit 5 | 44 to 55 | 22 to 28 |
| Unit 6 | 56 to 62 | 28 to 31 |
| Year-end check and response | 63 to 64 | 32 |

The mid-year check falls on school day 80, avoiding grade 7 core check days. The year-end check falls on school day 158, where overlap is permitted during finals week. Other after-core clashes remain the lead’s calendar pass.

The unit totals are **10 + 13 + 8 + 10 + 12 + 7 = 60**. Two course-check days and two respond days bring the total to 64. The distribution reasonably reflects the team project, systems work and shorter society unit.

This is a single-grade course, so the band-course Year column does not apply.

## Findings

### 1. Previous elective participation is assumed without an entry bridge

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, combined grades 6 to 12 review, S1  
**Confidence:** Firm

**Location:** The course in brief, Days; Seams, opening paragraph and Picked up table.

The frame calls the course an elective but treats every grade 6 prerequisite as year-before retrieval. Its only fallback addresses omission of grade 6 unit 4. A student who did not take grade 6 computer science can therefore encounter variables, procedures, flowcharts, testing and data operations without their assumed instruction.

This conflicts with frame-write rule 32. The progression links themselves are correct; the missing part is the course’s entry treatment.

**Exact fix:** Add a **Course order** bullet distinguishing retrieval for returning students from readiness evidence and worked bridges for students without the preceding elective.

Place ten-minute prerequisite checks at these existing points:

| Upcoming unit | Readiness slot |
|---|---|
| 1 | Last ten minutes of day 1, after the hook |
| 2 | Last ten minutes of day 10 |
| 3 | Last ten minutes of day 23 |
| 4 | Last ten minutes of day 33 |
| 5 | Last ten minutes of day 43 |
| 6 | Last ten minutes of day 55 |

Use the prerequisite rows already listed in Seams. Name the worked example that each flagged gap triggers before its first application. Retain the existing day 33 provision for omitted grade 6 machine-learning work within this broader treatment.

State that grade 7 teaches its owned standards fully even where grade 6 only began them.

### 2. The final documentation task does not demonstrate the required device use

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, incomplete assessment actions recur in earlier computer science second-model reads  
**Confidence:** Firm

**Location:** [Unit 2](/S:/CurioClass/docs/courses/computer-science-grade-7/frame.md:236), Evidence, Devices and the mid-year check.

Session 14 teaches documentation use on a device, but day 22 assesses MS-PRO-PD-13 through a reference entry and a call written by hand. The scored team-product description does not explicitly require documentation use. Meanwhile, Devices correctly says this standard needs a device for full credit.

The [published boundary, PDF page 57, printed page 52](https://csteachers.org/wp-content/uploads/2026/07/2026-CSTA-PK%E2%80%9312-Computer-Science-Standards.pdf#page=57) connects documentation with writing, debugging and refining programs. The subject STANDARD explicitly distinguishes the handwritten stand-in from full device evidence.

**Why it matters:** A teacher could record full attainment from the same evidence the frame elsewhere calls partial.

**Exact fix:** Make documentation use an explicit, individual look-for in the scored unit 2 product:

- After session 14’s teaching, each student uses a supplied reference entry to add or refine a function call in the program.
- Each student uses the error guide to identify and resolve a supplied error.
- Retain the reference used, resulting code and test result as evidence scored with the session 21 product.

Keep day 22’s handwritten task as supplementary evidence. On the no-device path, retain **part met without a device**. Update Evidence and the carried-record description together.

### 3. First teaching of list traversal is labeled Fluency

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, first teaching under Fluency appears in the grade 6 second-model read, finding 3  
**Confidence:** Firm

**Location:** Day kinds; unit 2, session 13.

Session 13 first introduces looping over a list, but the Day kinds bullet names it as Fluency. Sessions 11 and 12 introduce the collection and item operations, without explicitly teaching traversal.

GLOSSARY defines first explicit teaching of a new method or model as Understanding. The base’s [list-iteration lesson](https://www.raspberrypi.org/curriculum/archived/key-stage-3/python-programming-with-sequences-of-data/the-famous-for) also begins with examples that establish syntax and execution before application.

**Exact fix:** Classify session 13 as **Understanding**. Begin with a worked list traversal, trace the current item and output, then let students modify it. Remove session 13 from the Fluency examples; retain unit 1 session 5 and unit 2 session 16 as examples of practice after teaching.

No extra day is needed.

### 4. The course checks need a bounded workload

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, combined grades 6 to 12 review, S3  
**Confidence:** Likely

**Location:** [Course-level checks](/S:/CurioClass/docs/courses/computer-science-grade-7/frame.md:242).

The mid-year check combines two newly created charts, accessibility explanation, a substantial privacy response, grouping and summarizing, code analysis and testing. The year-end check combines three society performances with three earlier-unit tasks. Both receive about 40 minutes without task-level limits.

**Why it matters:** The eventual writer can preserve every listed demand yet produce a check that rewards speed more than computing understanding.

**Exact fix:** Keep the current check days and impose these limits when rewriting their cells:

| Check | Maximum task budget |
|---|---|
| Mid-year | Charts and comparison: 15 minutes; privacy case: 12; short trace: 6; testing item: 7 |
| Year-end | Historical effects: 10 minutes; automation case: 10; technology-suitability judgment: 10; short pseudocode design: 5; network item: 5 |

For mid-year, use a small unseen table with prepared plotting grids. Remove the additional group-and-summarize item and carry session 24’s record unscored.

For year-end, remove the additional model-results item and carry unit 4’s assessment record unscored. Bound the society tasks to short source cards and structured responses.

These are planning limits, not measured completion times. Verify them against the actual items before accepting the checks.

### 5. The source map misdescribes omitted and retained lesson content

**Severity:** Moderate  
**LAYER:** base text  
**REPEAT:** yes, source-map content mismatches recur in the grade 6 second-model read, finding 4  
**Confidence:** Firm

**Location:** [Source map](/S:/CurioClass/docs/courses/computer-science-grade-7/frame.md:291), unit 2 and its base-text description.

The Year 9 source row groups lessons 1, 5 and 6 as a project frame offered to grade 8. However, [lesson 1, Warm up](https://www.raspberrypi.org/curriculum/archived/key-stage-3/python-programming-with-sequences-of-data/warm-up), introduces lists and individual-item access. Grade 7 replaces that introductory work in session 11.

The map also claims lesson 3, [In a while, crocodile](https://www.raspberrypi.org/curriculum/archived/key-stage-3/python-programming-with-sequences-of-data/in-a-while-crocodile), within sessions 11 to 13. That lesson includes while-loop practice and string operations, neither explicitly retained nor excluded by this mapping.

**Exact fix:** Replace the Year 9 mapping with:

- **Session 11:** Curio Class’s own list introduction, replacing lesson 1’s introductory list work.
- **Session 12:** adapted list operations from lesson 2, *Playlist*.
- **Session 13:** adapted list traversal from lesson 4, *The famous for*, taught before modification.
- **Lesson 3:** left out of this grade 7 adaptation because its additional while/string sequence is not needed for the selected list introduction.
- **Lessons 1, 5 and 6:** identify separately as introduction, project and concluding consolidation or assessment, rather than calling all three a project frame.

Update the grade 8 source-map claim that grade 7 adapted lesson 3. Keep three list sessions and their existing outside-standard count.

### 6. Resolved seams remain described as unresolved, with dangling references

**Severity:** Moderate  
**LAYER:** process  
**REPEAT:** yes, combined grades 6 to 12 review, M4  
**Confidence:** Firm

**Location:** [Handed on table](/S:/CurioClass/docs/courses/computer-science-grade-7/frame.md:189), its closing paragraph, For the lead items 2 and 3, and unit 4’s final cell.

The current progression already links `g7-collab-text` to `g8-text-project` reciprocally. The grade 8 frame exists and places the pickup in unit 2, day 24. The grade 7 frame still says no row receives the handoff and that grade 8’s frame was absent.

References to “Row changes 1” and “Row changes 9” also point to no section in this file. The stale checker passed, so these require human correction.

**Exact fix:**

- Replace the code-review destination with **g8-text-project, grade 8 unit 2, day 24**.
- Replace the closing exception with: **“Every handoff above is reciprocal in data/progressions/computer-science.csv.”**
- Remove For the lead items 2 and 3 as completed work.
- Add grade 8 destination units to the handoff table: systems to unit 1; programming to unit 2, with code analysis also used in unit 4; data to unit 3; algorithms to unit 4; society to unit 5.
- Remove the dangling “Row changes” references. The board-game example can simply remain the stated example.

Do not rewrite the dated earlier review.

### 7. The course-size rationale miscounts its progression rows

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** Firm

**Location:** Days bullet, line 24.

The frame says 18 rows. The `grade:7` selector returns **19**, and all 19 are correctly placed across the units: **2, 4, 3, 3, 4 and 3**.

**Exact fix:** Replace the sentence with:

> 64 sessions for 19 progression rows is about 3.4 sessions per row, including checks.

Keep the 15-owned-standard count and all unit allocations.

### 8. The header retains UK spelling

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, the combined grades 6 to 12 review already identifies this wording  
**Confidence:** Firm

**Location:** [Opening course line](/S:/CurioClass/docs/courses/computer-science-grade-7/frame.md:3).

**Exact fix:** Change **“catalogue id”** to **“catalog id”**, following AGENTS.md’s US-spelling rule.

## Lens checklist: course-frame layer

| Lens requirement | Result |
|---|---|
| Owned CSTA standards taught at their boundary depth | Teaching coverage is present; documentation assessment needs finding 2’s repair |
| No unsupported Specialty or S2 claims | Met: none claimed |
| AI connected to data and algorithms rather than isolated without foundations | Met: unit 3 prepares unit 4; unit 6 reuses the learning |
| Unplugged work in every unit | Met: all six units name it |

The wider lens is also visible through explicit notional-machine teaching, systematic debugging, changing pair roles, text with a blocks stand-in, dated society cases and teacher support requirements. First teaching versus practice needs finding 3’s correction.

## What is right and should remain

- All five concept areas receive substantial teaching.
- Owned standards and revisited standards are distinguished correctly.
- Unit order respects variables, procedures, data preparation and machine-learning prerequisites.
- The grade 7 math leans have usable bridges where math teaches the formal content later.
- Safety and privacy use invented data, toy systems and no student accounts.
- The paper path honestly records partial attainment where the subject rules require device evidence.
- The source-store and third-party checks are explicitly pending rather than presented as completed.

## Settled by the expert

| Choice | Reason | File touched by the fixer |
|---|---|---|
| Keep six units and 64 sessions | Counts and broad allocation are defensible | Grade 7 frame |
| Retain the existing math bridges | They avoid premature probability and population inference | Grade 7 frame |
| Score documentation use through individual device evidence in the project | Matches the stated full-credit requirement | Grade 7 frame |
| Label first list traversal Understanding | It introduces a new execution method | Grade 7 frame |
| Use the explicit source mapping in finding 5 | Matches the public lesson descriptions | Grade 7 frame; corresponding grade 8 source-map sentence |
| Preserve the landed code-review handoff | Both progression ends and grade 8’s pickup now exist | Grade 7 frame |

## For Cory

None required for these repairs. No change to standard ownership, course audience, spending or outside people is recommended.

## What I could not judge

Actual assessment duration, item quality, scoring reliability, tool behavior and teacher-page usability cannot be verified before those materials exist. The pending base-resource store and per-file rights checks also prevent approval of particular adapted problems, wording or images.

I did not verify every proposed society case’s eventual factual claims. Those still require the named sources and sensitivity reads before lesson writing.

## Sources

- [2026 CSTA standards PDF](https://csteachers.org/wp-content/uploads/2026/07/2026-CSTA-PK%E2%80%9312-Computer-Science-Standards.pdf): all 15 owned statements and boundaries checked. Stored copy also inspected: :codex-file-citation{path="S:/CurioClass-sources/computer-science/csta-2026-11-21/csta-2026-pk12-cs-standards.pdf" purpose="source"}
- [PRIMM teaching summary](https://static.raspberrypi.org/files/curriculum/quickreads/11-Pedagogy_Summary_PRIMM_V4_2023.pdf): checked the progression from supplied code through modification to creation.
- [Archived Python introduction](https://www.raspberrypi.org/curriculum/archived/key-stage-3/introduction-to-python-programming): checked unit sequence and lesson coverage.
- [Archived sequences unit](https://www.raspberrypi.org/curriculum/archived/key-stage-3/python-programming-with-sequences-of-data): checked the lesson inventory; individual lesson links support finding 5.
- [Thinking machines](https://www.raspberrypi.org/curriculum/archived/key-stage-3/computing-systems/thinking-machines): checked the background lesson used for unit 6.
- [Computer History Museum timeline](https://www.computerhistory.org/timeline/) and [EPA electronics page](https://www.epa.gov/recycle/electronics-donation-and-recycling): inspected the proposed history and environmental source routes; neither inspection validates the future complete case packet.

## For the source list

Add the individual archived lesson URLs used in finding 5 to the computer science source notes. They expose distinctions that the unit overview alone does not establish.


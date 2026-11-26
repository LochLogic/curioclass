# Frame read: Computer Science, Grade 1

2026-11-25. Independent second-model read. No files were changed.

## Verdict

The course structure is sound: all 15 selected progression rows and all 16 E1 standards are placed once, the 32-session calendar adds up, and the neighboring-course handoffs match. The biggest risk is assessment: two tasks omit part of the owned action, and the promised individual oral evidence lacks a convincing time budget. Repair those assessment contracts before writing the scope and sequence; retain the five-unit order and existing standard ownership.

**Findings: 4, ordered most serious first.**

## What I read and checked

- [The course frame](S:/CurioClass/docs/courses/computer-science-grade-1/frame.md), its entries in `course-list.csv`, `frames.csv`, and `calendar.csv`, and the 15 progression rows selected by `rows=grade:1`.
- The frame-read brief, frame-write brief including its after-core changes, EXPERT.md, the computer science lens, subject bar, STANDARD.md and APPROACH.md.
- Relevant foundation, shared-bar, approach, production-path, source-license, and decision rules.
- Kindergarten and grade 2 frame material and progression rows for the seams; the grade 1 mathematics Units table and calendar for both declared leans.
- Earlier computer science pre-work and progression reviews, and the kindergarten frame reads and fix report, to distinguish repeated findings from settled issues.
- All 16 E1 boundary statements in the stored standards PDF, especially PDF pages 40, 68, 76 and 102:

  :codex-file-citation{path="S:/CurioClass-sources/computer-science/csta-2026-11-21/csta-2026-pk12-cs-standards.pdf" purpose="source"}

- Outside sources linked below, checked during this read.

### Check results

| Check | Result |
|---|---|
| `python -X utf8 scripts/frame.py check computer-science-grade-1` | Pass, 0 failures; 5 units, 32 days |
| `python -X utf8 scripts/plan.py check computer-science-grade-1` | Stops because the plan-stage day and item files are absent |
| `python -X utf8 scripts/stale.py check` | One failure in another course, physical education grades 9 to 12 |
| Stale check restricted to this frame | Pass, 0 failures |
| Independent placement count | 15 rows placed once; 16 owned ids |
| Calendar reconciliation | Units total 28 sessions, plus 2 checks and 2 respond sessions |

The plan check was course-filtered to honor the repository’s prohibition on unfiltered checks; neither its stage failure nor the unrelated stale-note failure prevents this verdict.

The calendar places units in weeks 1 to 6, 7 to 12, 15 to 22, 23 to 26, and 29 to 32. Checks in weeks 13 and 27 avoid all grade 1 core course-level check weeks. This is a single-grade course, so no Year column is required.

## Findings

### 1. Two assessment tasks omit part of the standard’s action

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, incomplete performance evidence also appeared in the kindergarten second-model read, finding 3  
**Confidence:** Firm

**Location:** Frame lines 228 and 229, Course-level checks.

The mid-year task supplies the parts of a pictured job and asks children to order the steps within each part. That does not show whether the child can identify the parts themselves. The year-end task collects and records a count and description but never asks the child to use them to answer a question. These omissions narrow E1-ALG-PS-01 and E1-DAT-DC-08 respectively. See the [official standards, PDF pages 40 and 68](https://csteachers.org/wp-content/uploads/2026/07/2026-CSTA-PK%E2%80%9312-Computer-Science-Standards.pdf).

**Why it matters:** Both cells promise to score their unit in full. A child could complete the listed tasks without demonstrating the missing action.

**Exact fix:**

- Replace the mid-year decomposition item with: “Given a new pictured classroom job and ungrouped action cards, each child identifies its parts by grouping the cards, then orders the steps within each part. Accept drawing or dictated steps.” Score identifying parts separately from ordering steps.
- Replace the year-end collection item with: “Given two small block towers, answer ‘How are these towers alike and different?’ Each child collects a count and an observed description, records both, and uses both in a spoken, pointed or drawn answer.” Score collection methods, the two forms of data, and their use in the answer separately.
- Copy these look-fors into the corresponding unit assessment descriptions and respond directions.

Keep both standards in their existing units.

### 2. The single-sitting oral assessment promise is not adequately budgeted

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, assessment feasibility was the central issue in the earlier kindergarten expert read, finding 1  
**Confidence:** Likely

**Location:** Days and Evidence bullets, lines 15 to 27 and 80 to 92; unit assessment descriptions; Course-level checks.

The frame promises individual spoken evidence from 30 children in five groups while children finish an approximately 15-minute paper task. Fifteen minutes gives each group three minutes, or 30 seconds per child before transitions and recording. At mid-year, that includes two separate explanations per child plus earlier-unit sampling. At year-end, children also collect, record and explain data.

**Why it matters:** Group answers can conceal individual gaps. Rushing the speech can also turn language fluency into the deciding factor.

**Exact fix:**

Replace the universal single-sitting rule with:

> End-of-unit evidence may be gathered across named sessions. Individual oral items on previously taught content may be collected during independent work in the final teaching sessions. The designated assessment session completes the remaining unseen items. No evidence is scored in the session that first teaches its content.

Then revise each assessment description to name:

- Which oral items are collected earlier and which remain on the assessment day.
- The children heard in each session.
- Minutes for instructions, individual responses, recording and transitions.
- The independent task for everyone else.

For example, collect unit 2’s changed-order explanation after its session 3 teaching, leaving the later people-or-computer explanation for day 13. Keep the 32-session total and protect the teaching of newly introduced rows. Do not treat partner speech alone as a teacher-scored individual record.

### 3. Factual examples and society teaching lack explicit source directions

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, source grounding and society cases were addressed in the computer science pre-work reads  
**Confidence:** Firm about the missing directions

**Location:** Units 2 and 5, especially their anchors and “What students learn” cells.

Unit 2 introduces book suggestions and generated pictures as actual uses of pattern-finding systems. Unit 5 supplies before-and-after activity comparisons. Neither cell identifies factual sources or distinguishes constructed practice scenes from documented cases. Unit 5 also leaves the subject’s requirement for two sourced views unspecified.

**Why it matters:** A writer could build these days entirely from plausible invented pictures while treating them as evidence of real computing uses and changes.

**Exact fix:**

- Mark the tower, plant dispute, generic screens and town scenes **“invented for practice.”**
- Add to unit 2’s writing requirements: “The teacher source line gives a checked primary source and date for each real AI use represented; the drawing itself is invented.”
- Add to unit 5: “Each activity comparison names its factual source in the teacher source line. The teacher materials supply two brief, sourced perspectives on its use, including an advantage and a limitation, with dates. Student pictures use generic devices and names.”
- For the information-search comparison, the [Computer History Museum’s networking and web timeline](https://www.computerhistory.org/timeline/networking-the-web/) is an available historical starting source. Select a specific entry rather than citing the entire timeline for every comparison.

This supplies evidence for the existing content without adding a unit or changing its standards.

### 4. The calendar note is already stale

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale status wording also appeared in the computer science pre-work fix pass  
**Confidence:** Firm

**Location:** “For the lead,” item 1, lines 253 to 257.

The note says week 13 shares with no other after-core course and names only health at week 27. The current `calendar.csv` also places library in week 13, and media arts and theater in week 27.

**Why it matters:** The lead’s calendar pass would start from an incomplete clash list.

**Exact fix:** Replace those two claims with:

> In the calendar checked on 2026-11-25, week 13 is shared with library and research skills. Week 27 is shared with health, media arts and theater. These overlaps remain for the lead’s after-core calendar pass.

Do not move check weeks during this read.

## Lens checklist

| Frame-level lens requirement | Result |
|---|---|
| All five concept areas | Met |
| Read and trace before modify and make | Met |
| Unplugged work teaches named concepts | Met in every unit |
| Explicit notional machine | Met through ordered execution and waiting for the tap |
| Debugging taught as a method | Met |
| Practices taught within content | Met |
| Society with evidence | Missed in the source directions, finding 3 |
| Non-specialist teacher support | Required by the governing approach; finished teacher pages cannot yet be judged |
| Boundary depth respected | Teaching is sound; assessment contracts need finding 1 |
| Specialty claims appropriate | Not applicable; none claimed |
| AI supported by earlier ideas | Met through kindergarten sorting and unit 2 pattern work |
| Unplugged path in every unit | Met |

## What is right and should be retained

- The five-unit order and unequal day allocations fit the rows’ teaching load.
- Kindergarten retrieval leads into genuine grade 1 additions; the grade 2 frame picks up every outgoing row.
- Mathematics data work finishes by week 4, well before its use here. The measurement overlap in weeks 23 to 26 has an explicit bridge.
- Programming creation and debugging receive performance tasks.
- All 36 partial-base lessons are accounted for, including exclusions. The archive edition and unresolved file-level license checks are stated honestly.
- Checks serving as unit assessments avoid duplicate assessment runs.

## Settled by the expert

| Choice | Reason | File touched by the later fix |
|---|---|---|
| Use ungrouped cards for the decomposition assessment | Reveals whether the child identifies the parts | Grade 1 frame, mid-year check |
| Give the data collection an explicit question and answer | Preserves the purpose of collecting data | Grade 1 frame, year-end check |
| Permit distributed individual oral evidence after teaching | Makes the evidence contract more feasible | Grade 1 frame, Evidence and assessment descriptions |
| Retain ownership, unit order and 32 sessions | No evidence warrants changing them | Grade 1 frame |
| Refresh the clash list without moving checks | Scheduling remains the lead’s calendar task | Grade 1 frame, For the lead 1 |

## For Cory

- No new scope, money, people or audience decision arises from this read.
- The existing K to 2 picture-block editor extension remains a scope decision already identified in the frame.

## What I could not judge

The archived lesson packages are not loaded, so file-level licenses, third-party exclusions and adaptation fidelity remain unverified. The public programming-quizzes page could not be opened in this read. Finished tools, scoring keys, accessibility behavior and classroom timing also remain untested.

No finding rests on model memory. Finding 2 is a feasibility judgment based on the stated tasks and arithmetic, not a measured classroom result.

## Outside sources

- [2026 CSTA standards](https://csteachers.org/wp-content/uploads/2026/07/2026-CSTA-PK%E2%80%9312-Computer-Science-Standards.pdf): checked owned depth and assessment actions.
- [Archived key stage 1 curriculum](https://www.raspberrypi.org/curriculum/archived/key-stage-1): checked unit inventory and source-order guidance.
- [Robot algorithms](https://www.raspberrypi.org/curriculum/archived/key-stage-1/programming-a-robot-algorithms) and [Break it down](https://www.raspberrypi.org/curriculum/archived/key-stage-1/programming-a-robot-algorithms/debugging): checked sequence and decomposition.
- [Pictograms](https://www.raspberrypi.org/curriculum/archived/key-stage-1/data-and-information-pictograms): checked mapped and excluded lessons.
- [PRIMM teaching summary](https://static.raspberrypi.org/files/curriculum/quickreads/11-Pedagogy_Summary_PRIMM_V4_2023.pdf): checked the supplied-program-to-modification-to-creation sequence; it does not validate this grade 1 course.
- [Computer History Museum timeline](https://www.computerhistory.org/timeline/networking-the-web/): identified an accessible factual source for unit 5.

## For the source list

Add the specific archived Year 2 lesson links above if absent. The lesson titled “Break it down” uses the URL ending `/debugging`.
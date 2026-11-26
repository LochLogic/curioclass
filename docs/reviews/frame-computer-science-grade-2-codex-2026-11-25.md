# Frame read: Computer Science, Grade 2

2026-11-25. Independent second-model read. No files changed.

## Verdict

The frame has a sound course structure: all 14 selected progression rows and all 16 E2 standards are placed once, the handoffs match, and the 32-session calendar balances. The biggest risk is the assessment contract, which omits two required actions and promises more individual oral evidence than its timing explains. Repair those contracts and the four implementation issues below before writing the scope and sequence; retain the five-unit order and existing ownership.

**Findings: 6, ordered most serious first.**

## What I read and checked

- The complete [grade 2 frame](/S:/CurioClass/docs/courses/computer-science-grade-2/frame.md), its `course-list.csv` selector (`grade:2`), progression rows, `frames.csv` entry and calendar rows.
- The frame-read brief, after-core frame-write instructions, EXPERT.md, computer science lens, subject bar, STANDARD.md and APPROACH.md.
- Relevant foundation, production-path, shared approach, baseline, source and decision rules.
- Grade 1 and grade 3 frames and progression rows for the seams.
- Grade 2 mathematics and ELA Units tables and calendar placements.
- Relevant computer science pre-work, progression and earlier frame reviews, including the kindergarten fix report.
- The official E2 standards and boundary statements, archived base-unit pages, and outside sources linked below.

### Check results

| Check | Result |
|---|---|
| `python -X utf8 scripts/frame.py check computer-science-grade-2` | Pass: 0 failures; 5 units, 32 days |
| `python -X utf8 scripts/plan.py check computer-science-grade-2` | Fails because later plan-stage `days.csv` and parts/items files are absent |
| `python -X utf8 scripts/stale.py check` | Pass: 121 files, 0 failures |
| Independent placement count | 14 rows placed exactly once; 16 distinct owned standards |
| Independent seam check | No missing reciprocal `assumes` or `hands_on` links |
| Calendar reconciliation | 28 unit sessions + 2 check sessions + 2 respond sessions = 32 |

The plan check was course-filtered to honor the repository rule against unfiltered checks; its stage failure does not prevent this verdict.

| Course component | Course days and weeks |
|---|---|
| Unit 1 | 1 to 6 |
| Unit 2 | 7 to 10 |
| Mid-year check and response | 11 and 12 |
| Unit 3 | 13 to 20 |
| Unit 4 | 21 to 25 |
| Year-end check and response | 26 and 27 |
| Unit 5 | 28 to 32 |

Weeks 11 and 26 avoid the grade 2 core course-level checks. Their acknowledged clashes with health, visual arts and SEL remain for the lead’s after-core calendar pass. This is a single-grade course, so a Year column is not required.

## Findings

### 1. Two scored tasks omit part of their owned standard

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, incomplete assessment evidence appeared in the kindergarten second-model read, finding 3, and grade 1 read, finding 1  
**Confidence:** Firm

**Location:** Unit 3, line 228; year-end Course-level check, line 237.

The year-end data task asks children to sort data types and identify a collection method, but never compare what information the types provide. Unit 3’s assessment asks for the building steps and attribution, but omits explaining the functions of the blocks used. Both omissions matter because the frame promises full assessment of the owned standards. See E2-DAT-DC-08 and E2-PRO-RD-06 in the [official standards, PDF pages 68 and 62](https://csteachers.org/wp-content/uploads/2026/07/2026-CSTA-PK%E2%80%9312-Computer-Science-Standards.pdf).

**Why it matters:** Children could pass the listed tasks without demonstrating the missing actions, although both are present in the teaching descriptions.

**Exact fix:**

- Extend the data item with: “Using the same classroom-object cards, show which information tells how many or how much, which describes or groups the objects, and one comparison the data supports.” Accept pointing, drawing or speech. Score collection method and information provided separately.
- Extend unit 3’s explanation with: “Point to the event, the repeated steps and the repeat count, and explain what each does in the program you built.” Score this separately from building steps and attribution.
- Copy these look-fors into the Evidence bullet and corresponding respond directions. Keep both standards in their current units.

### 2. The oral evidence exceeds the stated single-sitting allowance

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, grade 1 second-model read, finding 2  
**Confidence:** Likely

**Location:** Evidence bullet, lines 83 to 96; unit assessment descriptions; Course-level checks.

The general rule budgets one spoken answer per child while classmates complete about 15 minutes of paper work. The year-end check explicitly requires an explanation of collection bias, a personally refined question, and an explanation of the sorter’s likely mistake. That is at least 90 individual responses for 30 children, approximately ten seconds each within the paper-work window, before transitions and recording.

Unit 1 similarly names several explanations per child. The frame supplies no alternative collection schedule.

**Why it matters:** A writer may rush responses, accept group answers as individual evidence, or omit a required look-for.

**Exact fix:** Replace the universal single-sitting rule with:

> Individual scored evidence may be gathered across named sessions after its content has been taught. Each assessment description identifies the evidence collected earlier, the evidence completed on the assessment day, the children heard in each session, and the minutes for instructions, responses, recording and transitions. No evidence is scored in the session that first teaches its content. Partner speech alone is not an individual teacher-scored record.

For the year-end check, collect the refined-question responses from ten children during each of unit 4’s sessions 3, 4 and 5, using five minutes of independent work per session. Keep one individual collection-bias explanation on day 26; let children explain the sorter’s mistake through a drawn or pointed link between the missing training examples and the mistaken prediction. Apply the same explicit timing requirement to the other assessments, preserving all respond sessions.

### 3. The microphone activity contradicts the subject’s privacy rule

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** Firm

**Location:** Devices bullet, lines 97 to 100; unit 1 session 2 and Tools, line 226.

Unit 1 proposes tracing a spoken word through a microphone to a sound-level display. STANDARD.md, “Privacy and safety,” explicitly prohibits a student’s voice entering a program, dataset or tool. Local processing without storage does not resolve that wording conflict.

**Why it matters:** The scope writer could build an activity forbidden by the governing subject page.

**Exact fix:** Remove the student-spoken-word and sound-level-view options. Replace them with:

> Pairs trace a key press to a displayed letter, or a button press to a short tone. No microphone or voice input is used.

Update the Devices bullet and tool description accordingly. Microphones may remain among pictured hardware examples.

### 4. Society teaching lacks the required sourced perspectives

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, computer science pre-work read, finding 8, and grade 1 second-model read, finding 3  
**Confidence:** Firm

**Location:** Unit 5, line 230; Sensitivity reads and For the lead source-list entries.

Unit 5 names useful cases, but directs writers mainly to organizational homepages and a general timeline. It does not require the two sourced views specified by STANDARD.md, “Real cases in society days,” and APPROACH.md. A sensitivity source pack does not supply that missing teaching contract.

The timeline activity also needs dated instances of use or artifacts, rather than an unsupported order for generic technologies that persisted across centuries.

**Why it matters:** Writers could produce plausible case cards without traceable factual evidence or the perspectives the subject requires.

**Exact fix:** Add to unit 5:

> Each case card has a teacher source line naming the exact page, publisher, historical date or period, and access date. Each society session includes two brief perspectives supported by dated sources, with a question about whom the tool helps and a limitation or different need. Invented scenes are labeled “invented for practice.” Timeline positions refer to documented artifacts or uses, not assumed invention dates or replacement of one culture’s tool by another.

Replace the broad factual pointers with these checked starting pages:

- [The Versatile, Venerable Abacus](https://www.computerhistory.org/revolution/calculators/1/1), for Chinese and Japanese examples.
- [Inka khipu](https://americanindian.si.edu/exhibitions/infinityofnations/andes/143866.html), for a dated object and its record-keeping context.
- [Louis Braille: His Legacy and Influence](https://www.loc.gov/exhibits/louis-braille/overview.html), for Braille’s contribution.

Retain the separate requirement for community-owned sensitivity sources.

### 5. One base lesson is neither mapped nor excluded

**Severity:** Moderate  
**LAYER:** base text  
**REPEAT:** yes, kindergarten second-model read, finding 5  
**Confidence:** Firm

**Location:** Source map, line 302.

The “Events and actions in programs” row places lessons 3, 5 and 6 and excludes lessons 1 and 2. Lesson 4 is absent, leaving only 35 of the base year’s 36 lessons accounted for. The publisher identifies lesson 4 as [Adding features](https://www.raspberrypi.org/curriculum/archived/key-stage-2/programming-b-events-and-actions/adding-features).

**Why it matters:** The next writer cannot distinguish a deliberate exclusion from an overlooked lesson.

**Exact fix:** Append to that row’s exclusions:

> Lesson 4, Adding features: additional drawing features and command sequences are left out; unit 3 already teaches and checks the owned sequence, event and repeat work, and this lesson adds no required E2 coverage.

Keep the existing day allocation. The completed inventory should account for all 36 lessons.

### 6. The calendar fallback offers to delete a required respond day

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, assessment and response allocation was addressed in the kindergarten expert read and fix pass  
**Confidence:** Firm

**Location:** For the lead 1, lines 267 to 269.

The fallback says that moving the check to week 27 could make unit 5 lose its respond day. That contradicts APPROACH.md’s requirement that every K to 5 unit end with one, and the frame’s own Days bullet.

**Why it matters:** A scheduling adjustment could silently remove the planned instructional response to unit 5’s assessment.

**Exact fix:** Replace the fallback sentence with:

> Retain weeks 11 and 26 pending the lead’s after-core calendar pass. Any later move preserves both course-level respond sessions and every unit’s respond session. A revised schedule must name its teaching-session adjustment and pass the frame check; deleting a respond session is not an option.

No check-week move is recommended by this read.

## Lens checklist

| Frame-level lens requirement | Result |
|---|---|
| All five concept areas receive teaching | Met |
| Programming does not dominate the course | Met: 6 of 22 teaching sessions |
| Read and predict before modify and make | Met |
| Constructs and models introduced before use | Met |
| Unplugged work teaches a named concept in every unit | Met |
| Explicit notional machine | Met through ordered execution, events and counted repeats |
| Debugging taught as a method | Met |
| Collaboration, design and ethics inside content | Met |
| Society taught with evidence and multiple views | Missed in the frame directions, finding 4 |
| Non-specialist teacher support | Required by APPROACH.md; finished teacher pages not yet judgeable |
| Boundary depth and owned actions preserved | Teaching largely met; scored evidence needs finding 1 |
| Specialty and S2 claims appropriate | Not applicable: none claimed |
| AI connected to prior data and algorithm ideas | Met |
| No blank-editor opening | Met |
| Assessment includes doing and code | Met in form; completeness and timing need findings 1 and 2 |
| Tools have named jobs and no account/install requirement | Met; voice-input conflict needs finding 3 |
| Pair roles switch | Met |
| No unsupported general-thinking claim | Met |
| Day-level keys, misconceptions and accessibility behavior | Not applicable at this layer; later verification required |

## What is right and should be retained

- The five-unit order and unequal allocations follow the actual teaching load.
- All incoming and outgoing progression links match.
- Repeat counts are stepped through without assuming multiplication or repeated addition before mathematics teaches them.
- Mathematics graphs precede unit 4, and the ELA explanation work has an explicit bridge.
- Checks serving as unit assessments avoid duplicate assessment runs.
- The source-store and file-license limits are acknowledged honestly.
- No additional stale status claim was found in this frame.

## Settled by the expert

| Choice | Reason | Later edit |
|---|---|---|
| Retain ownership, unit order and 32 sessions | Placement, dependencies and arithmetic hold | Grade 2 frame |
| Add separate data-information and block-function look-fors | Makes the assessment evidence complete | Evidence and assessment descriptions |
| Allow distributed individual evidence after teaching | Resolves the single-sitting bottleneck | Evidence and timing descriptions |
| Use key/button input instead of student voice | Meets the existing privacy rule | Devices and unit 1 |
| Explicitly exclude base lesson 4 | Completes the inventory without adding days | Source map |
| Protect every respond session | Preserves the governing pacing rule | For the lead 1 |

## For Cory

- No new scope, money, people or audience decision is required by these findings.
- The existing request to extend the editor to kindergarten through grade 2 remains a scope decision already identified in the frame.

## What I could not judge

The archived lesson packages are not loaded, so file-level licenses, third-party exclusions and adaptation fidelity remain unverified. Finished tools, scoring keys, accessibility behavior and classroom timings are also untested.

The National Federation of the Blind museum page returned **403 Forbidden**, status **browser check**. I did not fetch it another way; the Library of Congress supplied an accessible alternative for the factual Braille check.

No finding rests on model memory. Assessment timing is a feasibility judgment from the frame’s tasks and arithmetic, not an observed classroom result.

## Other outside sources

- [2026 CSTA standards](https://csteachers.org/wp-content/uploads/2026/07/2026-CSTA-PK%E2%80%9312-Computer-Science-Standards.pdf): checked E2 scope, boundaries and assessment actions.
- [Archived Events and actions unit](https://www.raspberrypi.org/curriculum/archived/key-stage-2/programming-b-events-and-actions): checked lesson inventory.
- [Archived Branching databases unit](https://www.raspberrypi.org/curriculum/archived/key-stage-2/data-and-information-branching-databases): checked mapped and excluded lesson ranges.
- [PRIMM teaching summary](https://static.raspberrypi.org/files/curriculum/quickreads/11-Pedagogy_Summary_PRIMM_V4_2023.pdf): checked the supplied-program, modification and creation sequence; it does not validate this grade 2 implementation.

## For the source list

Add the exact abacus, khipu, Braille and archived lesson links above where absent. Record the blocked National Federation of the Blind page for a browser check.
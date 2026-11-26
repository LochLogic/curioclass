# Frame read: Computer Science, Grade 3

2026-11-25. Independent second-model read. No files changed.

## Verdict

The frame is sound in structure: all 16 selected progression skills and 19 owned standards are placed once, the dependencies work, and the calendar balances at 32 sessions. The biggest risk is individual assessment evidence: the pair’s program does not establish what each child implemented. Add that evidence, complete the society-source contract, and fix the response and variable-lesson inconsistencies before writing the scope and sequence.

**Findings: 5, most serious first.**

## What I read and checked

- The complete [grade 3 frame](/S:/CurioClass/docs/courses/computer-science-grade-3/frame.md), its `grade:3` selector in `course-list.csv`, selected progression rows, `frames.csv` entry and calendar rows.
- `frame-read.md`, the after-core provisions of `frame-write.md`, EXPERT.md, the computer science lens, subject bar, STANDARD.md and APPROACH.md.
- Relevant foundation, production-path, glossary, baseline, source and recorded decision rules.
- Adjacent computer science frames and progression rows for grades 2 and 4.
- Relevant grade 3 mathematics, science and ELA Units tables and calendar placements.
- Computer science pre-work, progression and earlier frame reviews, consulted after the initial frame read.
- Official standards and selected boundary statements, archived base-unit pages and the outside sources linked below.

### Check results

| Check | Result |
|---|---|
| `python -X utf8 scripts/frame.py check computer-science-grade-3` | Pass: 0 failures |
| `python -X utf8 scripts/plan.py check computer-science-grade-3` | Fails because later plan-stage day and parts/items files are absent |
| `python -X utf8 scripts/stale.py check` | Pass: 121 files, 0 failures |
| Independent placement count | 16 skills, each placed exactly once; 19 distinct owned standards; no missing or extra codes |
| Reciprocal progression links | No missing incoming or outgoing links |
| Calendar arithmetic | 28 unit sessions + 2 check sessions + 2 respond sessions = 32 |
| Base inventory | All 36 Year 4 lessons accounted for: 13 used, 23 excluded; inherited Year 3 ranges addressed |

The plan check was course-filtered to honor the repository prohibition on unfiltered checks; its stage failure does not prevent this verdict. Commands used `-B` to prevent bytecode-file creation.

| Component | Course days and weeks |
|---|---|
| Unit 1 | 1 to 6 |
| Unit 2 | 7 to 10 |
| Mid-year check and response | 11 and 12 |
| Unit 3 | 13 to 21 |
| Unit 4 | 22 to 25 |
| Year-end check and response | 26 and 27 |
| Unit 5 | 28 to 32 |

Weeks 11 and 26 avoid grade 3 core course-level checks. After-core clashes remain for the lead’s calendar pass. This is a single-grade course, so no Year column is required.

## Findings

### 1. The pair product does not establish each child’s implementation

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, combined grades 1 to 5 expert read, M3  
**Confidence:** Firm

**Location:** Evidence bullet, lines 89 to 103; unit 3 assessment, line 250.

The Evidence bullet requires the child’s own program for a develop standard, but day 20 scores the pair’s saved program. The individual feedback sentence establishes a reported suggestion and change, not independent implementation. A child could receive the implementation score while their partner did the coding.

The [official standard, PDF page 55, printed page 50](https://csteachers.org/wp-content/uploads/2026/07/2026-CSTA-PK%E2%80%9312-Computer-Science-Standards.pdf) permits implementing a classmate’s algorithm with credit. That does not establish which member implemented the shared product.

**Exact fix:** Keep the pair build and feedback sessions. Add this requirement to the Evidence bullet and unit 3:

> Session 5 reserves two five-minute turns at each pair’s device. Each child independently implements a short version of their own or a classmate’s credited step-card algorithm, using already-taught structures. The partner completes a paper task without helping. Each child saves or prints their own result. Day 20 scores this individual implementation with the pair program as supporting evidence.

Count those ten minutes inside session 5 by shortening its second partner-reading exercise. Preserve the worked reading example, feedback and revision sessions, and respond day. On the paper path, retain the existing partial-coverage mark.

### 2. Society teaching lacks the required sourced perspectives

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, grade 2 second-model read, finding 4, and computer science pre-work read, finding 8  
**Confidence:** Firm

**Location:** Evidence bullet; unit 1 session 4, line 248; unit 5, line 252.

The frame reduces society evidence to a short claim with a reason. STANDARD.md requires two views with a dated source for each, and APPROACH.md repeats that requirement. Unit 5 supplies broad organizational pointers, but neither unit specifies the required perspective pair. The sensitivity pack serves a different purpose.

**Why it matters:** Writers could produce plausible benefit-risk charts and history cards without the evidence or range of perspectives the subject requires.

**Exact fix:** Replace the society-evidence sentence and add to the affected unit rows:

> Each society session uses two brief perspectives supported by dated sources. These may be different users’ documented needs or experiences. Teacher source lines name the exact page, publisher, historical date or period, and access date. Students make a short claim with a reason tied to the supplied evidence. Invented scenes are labeled “invented for practice.”

For unit 5, timeline positions must refer to documented uses or artifacts, rather than implying that letters, telephone calls or written bills disappeared when later tools arrived. The [National Weather Service’s About Models page](https://www.weather.gov/about/models) is a checked starting source for the computing-and-forecasting example.

### 3. The calendar fallback removes a required respond session

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, grade 2 second-model read, finding 6  
**Confidence:** Firm

**Location:** For the lead 1, lines 295 to 297.

The fallback moves unit 5 into four weeks and folds its respond day into its assessment day. APPROACH.md requires every K to 5 unit to end with a respond day, and this frame explicitly adopts that rule.

**Why it matters:** A later scheduling adjustment could silently remove the planned response to unit 5’s assessment.

**Exact fix:** Replace the fallback with:

> Retain weeks 11 and 26 pending the lead’s after-core calendar pass. Any revised schedule preserves both course-level respond sessions and every unit’s respond session. A check-week move must identify its teaching-session adjustment and pass the frame check; it must not absorb unit 5’s respond session into its assessment.

No check-week move is recommended by this read.

### 4. The variable lesson contradicts its progression limit and overstates editor behavior

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes for the variable-name claim, combined grades 1 to 5 expert read, m8; new for the one-variable contradiction  
**Confidence:** Firm for the contradiction; likely for the editor-behavior risk

**Location:** Unit 3 session 6 and assessment, line 250; mathematics bridge, line 272.

The progression note and mathematics bridge limit the demand to **one variable with a known starting value**. Session 6 instead specifies a score **and** a counter.

It also says a misspelled name makes a second box. The editor specification does not establish that behavior. The [official boundary, PDF page 60, printed page 55](https://csteachers.org/wp-content/uploads/2026/07/2026-CSTA-PK%E2%80%9312-Computer-Science-Standards.pdf) requires consistent variable naming, but does not prescribe automatic variable creation after a spelling error.

**Why it matters:** The writer receives conflicting depth instructions and may teach a misleading account of the editor.

**Exact fix:** Use this wording for session 6:

> A completed short program has one score variable with a known starting value. Children identify its name, what it stores and what changes it, then fill a trace-table. A variable keeps one consistent name; deliberately creating a second variable creates a separate named box.

Use one variable in the unit assessment and retain the existing small-number mathematics bridge.

### 5. Several frame statements disagree with the current data or table

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes for stale notes and column references; new for the specific calendar and sampling discrepancies  
**Confidence:** Firm

These are small corrections, but they leave contradictory instructions for the next writer.

| Location | Problem | Exact fix |
|---|---|---|
| Year-end check, line 259 | Claims to sample units 1 to 3. Its new items sample units 1 and 3 only. | Change both sampling phrases to “units 1 and 3.” Keep unit 2’s mid-year result in the course record; do not add another task to this sitting merely to preserve the sentence. |
| Cross-subject opening, lines 263 to 264 | Says science meets every school day and equates its course days with school days. | Replace with: “Math and ELA meet every school day. Science meets four days a week; its course days map to school days through calendar.csv. This course’s day n falls in week n.” Preserve the existing science-unit week ranges, which are correct. |
| For the lead 7, lines 323 to 326 | Lists progression changes as awaiting application, although the current CSV contains them. | Replace the item with: “No progression-row change is requested by this frame.” |
| For the lead 1, lines 293 to 294 | Its week 26 clash list omits dance, now present in the calendar. | Add dance to the list. Keep resolution with the lead’s calendar pass. |
| Practices bullet, line 53 | Calls the Practices column the fifth column; it is sixth. | Say “the Practices and concept areas column,” without a number. |
| Opening, line 3 | Uses UK spelling “catalogue.” | Change to “catalog.” |

The stale-note script passes because it does not catch all of these unmarked prose discrepancies.

## Lens checklist

| Frame-level requirement | Result |
|---|---|
| All five concept areas receive teaching | Met |
| Programming does not dominate | Met: 7 of 22 teaching sessions |
| Read and predict before modify and make | Met |
| Models and constructs introduced before use | Met |
| Unplugged work teaches named concepts | Met in the planned paths |
| Explicit notional machine | Met through ordered execution, named boxes and tracing |
| Debugging taught as a method | Met |
| Collaboration, design and ethics inside content | Met in outline |
| Society uses evidence and multiple views | Missed in the frame contract, finding 2 |
| Non-specialist teacher support | Required by APPROACH.md; finished pages remain unverified |
| Boundary depth and progression limits | Mostly met; variable contradiction needs finding 4 |
| Specialty or S2 claims | Not applicable: none claimed |
| AI connected to data and algorithms | Met |
| Assessment includes programs and doing | Met in form; individual implementation needs finding 1 |
| Tools have named jobs and account-free paths | Met in the specification |
| Pair-role switching | Required by APPROACH.md; exact timing belongs in later plans |
| No unsupported general-thinking claim | Met |
| Day-level keys, errors and accessibility behavior | Not yet judgeable |

## What is right and should be retained

- The five-unit order and unequal allocations follow the teaching load.
- All progression links are reciprocal. Grade 3 supplies what grade 4 expects.
- Mathematics graphs precede unit 4. The weather-table fallback avoids assuming science’s later weather instruction.
- The course-level checks replace the corresponding unit assessments, avoiding duplicate assessment days.
- The partial base excludes media-production work that does not serve the owned standards.
- The source-package and license checks are honestly identified as incomplete.
- The supplied-program, modification and creation order is consistent with the [PRIMM teaching summary](https://static.raspberrypi.org/files/curriculum/quickreads/11-Pedagogy_Summary_PRIMM_V4_2023.pdf). That source does not validate this particular grade 3 implementation.

## Settled by the expert

| Choice | Reason | Later edit |
|---|---|---|
| Retain ownership, five units and 32 sessions | Placement, dependencies and arithmetic hold | Grade 3 frame |
| Add individual implementation evidence within unit 3 | Makes the implementation score attributable to each child | Evidence and unit 3 |
| Keep one variable with a known starting value | Follows the selected progression row and existing bridge | Unit 3 |
| Preserve every respond session | Follows the governing pacing rule | Calendar fallback |
| Correct the sampling description instead of adding another item | Existing coverage remains recorded; the check description becomes accurate | Year-end check |
| Retain the no-device partial mark for E3-PRO-PD-04 | The boundary specifies a block-based environment | Devices and corresponding course record |

The previously identified device-share difference remains for the lead to reconcile with APPROACH.md. The frame states its share and reason; this read supplies no evidence that increasing screen time would improve learning.

## For Cory

None arising from these findings. They can be resolved within the existing standards and 32-session course.

## What I could not judge

- The archived lesson packages are not loaded. File-level licenses, third-party exclusions and adaptation fidelity remain unverified.
- Finished editor behavior, scoring keys and accessibility cannot be judged from the frame.
- The proposed 25-minute assessment sittings remain untested. The year-end sitting, with four unit tasks and three earlier-unit items, particularly needs a timed draft.
- Unit 5’s detailed factual cards still need exact source checks when written.

No content finding rests on model memory. Prior-run memory supplied only a review checklist; the course evidence above was checked against current files and outside sources.

## Outside sources

- [2026 CSTA standards](https://csteachers.org/wp-content/uploads/2026/07/2026-CSTA-PK%E2%80%9312-Computer-Science-Standards.pdf): checked selected grade 3 boundaries and assessment actions.
- [PRIMM teaching summary](https://static.raspberrypi.org/files/curriculum/quickreads/11-Pedagogy_Summary_PRIMM_V4_2023.pdf): checked the programming teaching sequence.
- [Archived Year 4 Internet unit](https://www.raspberrypi.org/curriculum/archived/key-stage-2/computing-systems-and-networks-the-internet), [Repetition in games](https://www.raspberrypi.org/curriculum/archived/key-stage-2/programming-b-repetition-in-games), and [Data logging](https://www.raspberrypi.org/curriculum/archived/key-stage-2/data-and-information-data-logging): checked lesson inventories and overview-level mapping.
- [National Weather Service: About Models](https://www.weather.gov/about/models): checked the forecasting example’s factual starting point.
- [Federal Trade Commission: Protecting Your Child’s Privacy Online](https://consumer.ftc.gov/articles/protecting-your-childs-privacy-online): checked the proposed online-information source pack.

## For the source list

Add the exact weather-service and privacy-page links above where absent, replacing homepage-only pointers.


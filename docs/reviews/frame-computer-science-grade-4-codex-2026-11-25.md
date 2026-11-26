# Independent frame read: computer-science-grade-4
2026-11-25

## Verdict

The five-unit, 32-session structure is sound, but the frame needs substantive corrections before scope writing. The largest risk is claiming full coverage from tasks or paper versions that omit part of a published boundary. Keep the unit order and day totals, restore the missing depth, and repair the assessment contracts.

**Findings: 7.** This read disagrees with the earlier combined review’s “minor fixes” verdict for grade 4 because findings 1 to 4 affect what the scope writer would teach or assess.

## What I read and checked

- The complete grade 4 frame, the adjacent grade 3 and grade 5 frames, and their progression handoffs.
- `frame-read.md`, the relevant frame-writing requirements, the computer science lens, STANDARD and APPROACH, and the subject’s adoption bar.
- `course-list.csv`, `frames.csv`, `calendar.csv`, the 16 selected progression rows, and the 19 E4 standard statements.
- All 19 E4 boundary statements in the stored standards PDF, checked beside the live [published standards](https://csteachers.org/2026-csta-pk-12-computer-science-standards/).
- The cited core-course Units rows and calendar placements.
- Relevant earlier progression, pre-work, kindergarten, and combined elementary frame reviews.

Prior review memory supplied a checking checklist only. No finding rests on unverified subject knowledge from memory.

### Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/frame.py check computer-science-grade-4` | Passed: 0 failures; 5 units, 32 days, including 4 course-check and respond days |
| `python -X utf8 scripts/plan.py check computer-science-grade-4` | Failed because the day-level plan files do not yet exist; this does not prevent a frame verdict |
| `python -X utf8 scripts/stale.py check` | Passed: 121 files, 0 failures |

The unfiltered plan command was replaced by the course-filtered check under AGENTS.md; the consolidated gate was not run because it creates or replaces output files.

No files were edited, created, or deleted.

## Findings

### 1. The paper path incorrectly claims the data-report standard in full

**Severity:** Serious  
**LAYER:** frame, progression  
**REPEAT:** yes, incomplete boundary coverage recurs in the earlier pre-work and kindergarten reads  
**Confidence:** Firm

**Location:** [frame.md, Devices](/S:/CurioClass/docs/courses/computer-science-grade-4/frame.md:99), unit 3, For the lead item 4; progression row `g4-data-explain`.

The frame permits a handwritten report and chart, then says every standard except E4-DAT-DC-09 is met fully on paper. E4-DAT-DI-10’s boundary also requires a computational tool and a digital explanation containing the visualization. See PDF page 74, printed page 69 of the [published standards](https://csteachers.org/2026-csta-pk-12-computer-science-standards/).

**Why it matters:** A school could record full coverage while omitting the required digital reporting work.

**Exact fix:**

- Unit 3 session 3: students produce a short digital report containing their chart, collection process, result, and limitation, then revise it after the partner comment.
- Day 17: retain an individual digital report task using a new small dataset.
- Specify how the chart and narrative are saved together locally.
- Mark **both** E4-DAT-DC-09 and E4-DAT-DI-10 “part met without a device” on the no-device path.
- Update `g4-data-explain.notes`, Devices, Paper path, and For the lead item 4 consistently. Add session 3 to the device-session count.

Keep the handwritten version as useful instruction and supporting evidence.

### 2. The quiz project requires variable design without identifying it as grade 5 work

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, teaching beyond the owner boundary is an established pre-work review finding type  
**Confidence:** Likely

**Location:** [unit 4](/S:/CurioClass/docs/courses/computer-science-grade-4/frame.md:243), sessions 3 to 5 and the “Out” statement.

Teams plan and build a scored quiz, including its score and ending. The exclusion reserves only comparing a variable with a number for grade 5, leaving students apparently responsible for constructing the score updates themselves. E4-PRO-VD-06 stops at tracing supplied variable behavior; designing variable-driven programs belongs beyond that boundary. See PDF page 60, printed page 55 of the [published standards](https://csteachers.org/2026-csta-pk-12-computer-science-standards/).

**Why it matters:** The scope writer could turn grade 4’s tracing requirement into first teaching of grade 5 variable programming.

**Exact fix:** Supply a working quiz shell with its score initialization, updates, and final display already written. Students trace that logic, then contribute question prompts, answer branches, messages, tests, and comments. Replace the exclusion with:

> Students trace supplied score logic but do not design or write variable initialization, updates, or comparisons. Grade 5 teaches students to construct those behaviors.

Retain meaningful individual contributions and the team program.

### 3. Two owner notes narrow the published boundary

**Severity:** Serious  
**LAYER:** progression, frame  
**REPEAT:** yes, omitted boundary details recur in the earlier pre-work reads  
**Confidence:** Firm

**Location:** Unit 1 session 2 and `g4-wired-wireless`; unit 5 session 1 and `g4-ml-learning`.

The network task covers speed, steadiness, and movement but leaves distance and network safety unspecified. The machine-learning task varies quantity or representation but never specifies inaccurate labels. Both omissions originate in the owner notes that the frame treats as its complete depth contract.

The relevant boundaries are on PDF pages 87 and 46, printed pages 82 and 41 of the [published standards](https://csteachers.org/2026-csta-pk-12-computer-science-standards/).

**Why it matters:** Later writers can follow both the progression and frame faithfully while preserving these gaps.

**Exact fix:**

| Row | Required addition within its existing session |
|---|---|
| `g4-wired-wireless` | Compare invented situations using distance, speed, convenience, and whether the available network is trusted. Include a case where declining an unknown network is the sensible choice. Avoid presenting either connection method as universally faster or safer. |
| `g4-ml-learning` | Add a small training set with deliberately incorrect labels. Students predict the effect, observe the supplied sorter’s results, and explain what changed when labels were corrected. Keep this qualitative and teacher-run. |

Mirror these additions in the unit descriptions and assessment look-fors. No standards need to move between units.

### 4. Two assessment descriptions stop before the required action

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, the kindergarten second-model read identified the same assessment-verb problem  
**Confidence:** Firm

**Location:** Unit 1 day 5; year-end check day 24.

The troubleshooting assessment orders steps and names a first check. The debugging assessment names the piece that broke. Neither description requires completing a repair and verifying that it worked.

These are application and debugging outcomes, reinforced by the adoption bar’s requirement for doing evidence. See the [published standards](https://csteachers.org/2026-csta-pk-12-computer-science-standards/), PDF pages 81 and 65, printed pages 76 and 60.

**Why it matters:** A student could receive credit for describing a process without demonstrating its successful use.

**Exact fix:**

- **Day 5:** replace step-ordering alone with a new staged or pictured fault. The student follows the process, selects and applies a safe fix, and verifies the result. A paper version can reveal the next system response after each chosen action.
- **Day 24:** require the student to locate the faulty addition, correct it, and rerun the relevant tests. Record expected result, observed result, change, and retest.
- Across unit 4’s small debugging examples, explicitly cover sequence, events, repetition, and selection. They need not occur in one program.
- Add these actions to the scored look-fors and respond-day records.

### 5. Day 24 carries too much assessment work

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, finding M4 in the earlier combined elementary frame review  
**Confidence:** Likely

**Location:** [Course-level checks, year-end row](/S:/CurioClass/docs/courses/computer-science-grade-4/frame.md:251); Evidence bullet; unit 4 session 5.

Day 24 combines four substantial programming tasks, three cumulative samples, and scoring a team product with evidence for every member. Finding 4 also requires the debugging task to include repair and retesting.

**Why it matters:** The stated 30-minute sitting is vulnerable to becoming rushed, especially with paired devices and access accommodations. This is a workload judgment, not a measured classroom timing.

**Exact fix:**

- Gather and score the revised team product from session 5, after feedback and revision, with an individual contribution record.
- Let that record carry E4-PRO-PD-05 and the student’s own documentation evidence for E4-PRO-RD-07.
- On day 24, retain trace, comparison, and repair-and-retest tasks, followed by the three brief cumulative samples.
- Remove the separate comment-writing item from that sitting. State a provisional budget of 5 minutes for tracing, 5 for comparison, 10 for debugging, and 6 for cumulative samples.
- Revise the Evidence bullet so product evidence is an explicit assessment form.

Keep day 25 for response. No additional course day is needed.

### 6. The incoming seam table omits a real prerequisite

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, finding m3 in the earlier combined elementary frame review  
**Confidence:** Firm

**Location:** [Picked up from Grade 3](/S:/CurioClass/docs/courses/computer-science-grade-4/frame.md:164).

`g4-history-limits.assumes` includes `g3-benefits-risks`, and grade 3 explicitly hands that relationship forward. Grade 4’s incoming table lists that earlier row only against `g4-resources`.

**Why it matters:** The progression is reciprocal, but the frame hides one retrieval obligation from the scope writer.

**Exact fix:** Add:

> `g3-benefits-risks` | Grade 3 unit 1, course days 1 to 6 | Benefit-risk-chart for a widely used system | `g4-history-limits` | Unit 5 session 4 | Retrieval: name one benefit and one limitation of a pictured system before explaining the improvement.

Add a “Grade 3 unit and course days” column to the existing table using the verified calendar ranges: unit 1, days 1 to 6; unit 2, 7 to 10; unit 3, 13 to 21; unit 4, 22 to 25; unit 5, 28 to 32.

### 7. Small wording errors remain in the frame and selected rows

**Severity:** Minor  
**LAYER:** frame, progression  
**REPEAT:** yes, findings m1, m2, and m6 in the earlier combined elementary frame review  
**Confidence:** Firm

**Location:** Frame opening and Practices bullet; notes for `g4-ml-learning` and `g4-debug-increment`.

The opening uses “catalogue”; the Practices bullet calls its column the fifth, although it is sixth; two selected progression notes retain UK spelling.

**Exact fix:**

- Change “catalogue id” to “catalog id.”
- Replace “the Units table’s fifth column” with “the Units table’s Practices and concept areas column.”
- Change “labelled” to “labeled” in `g4-ml-learning.notes`.
- Change “practise” to “practice” in `g4-debug-increment.notes`.

## Settled by the expert

| Choice | Reason | Files affected |
|---|---|---|
| Keep five units and 32 sessions | The ownership and relative loads support this structure | Grade 4 frame |
| Keep the current unit order | Systems precede device work; algorithms precede programming; data precedes training-data analysis | Grade 4 frame |
| Preserve the no-device course with honest partial marks | Useful instruction remains possible without overstating coverage | Frame; `g4-data-explain` |
| Supply the score mechanism in grade 4 | Preserves tracing depth and grade 5’s construction work | Unit 4 |
| Score the revised team product from session 5 | Releases assessment time without removing collaboration evidence | Evidence; unit 4; check table |
| Restore the missing boundary details inside existing sessions | No change in standard ownership or unit count is required | Two progression notes and their units |

## Lens checklist, course-frame layer

| Lens requirement or error check | Result |
|---|---|
| All five concepts receive substantial teaching | Met |
| AI has algorithm and data foundations | Met: unit 5 builds on units 2 and 3 |
| Read and predict, then modify, then make | Met in the stated sequence |
| Meaningful unplugged work in every unit | Met |
| Device feedback serves a named learning purpose | Met in design |
| Explicit notional machine and variable-value tracing | Met |
| Debugging taught as a method | Teaching met; scored evidence needs finding 4 |
| Collaboration and user considerations inside content | Met |
| Society work grounded in dated evidence and perspectives | Required by APPROACH; finished cases remain unverified |
| Support for a non-specialist teacher | Required clearly through APPROACH and the named teacher materials |
| Owned standards taught at their boundary depth | Missed: findings 1 to 3 |
| Performance evidence rather than recall alone | Partly met: findings 4 and 5 |
| No Specialty or X + CS ownership | Met |
| Middle-school text-code bridge | Not applicable to this frame |
| Unsupported claims about general thinking gains | None found |

## What is right and should not be touched

All 16 selected skills are placed exactly once, and all 19 owned IDs appear. The progression’s incoming and outgoing links are reciprocal; finding 6 concerns their presentation.

The calendar matches the frame: units occupy weeks 1 to 6, 7 to 10, 13 to 18, 19 to 23, and 26 to 32. Checks occupy weeks 11 and 24, with response in weeks 12 and 25. Neither check overlaps a core check week. The music clash in week 24 is already disclosed for the lead’s after-core calendar pass.

The math, ELA, and science citations match their calendar rows. Where same-year content arrives later, the frame supplies workable bridges.

The source map accounts for all 36 Year 5 base lessons through placement or explicit exclusion. It explains its main reordering and distinguishes Curio Class work from adapted material. Unit 5’s separate assessment and respond day make its placement after the course-level check defensible.

## What I could not judge

- Full base-lesson contents, third-party permissions, or compressed lesson feasibility. The frame correctly identifies its public-page mapping as provisional.
- Finished tools, keys, rubrics, access behavior, or actual assessment timing.
- The biography and workforce cards’ eventual factual accuracy and perspectives. Their sources still need checking when the cards are written.
- The archived Systems and searching page, which returned an inaccessible-tool result. **Browser check** remains needed for that page; no finding depends on its unseen content.

No additional stale status note was established.

## Sources checked outside the repository

- [2026 CSTA PK–12 Computer Science Standards](https://csteachers.org/2026-csta-pk-12-computer-science-standards/): controlling statements and boundary depth.
- [Archived Year 5 curriculum listing](https://www.raspberrypi.org/curriculum/archived/key-stage-2): base-unit identity.
- [Selection in quizzes](https://www.raspberrypi.org/curriculum/archived/key-stage-2/programming-b-selection-in-quizzes): six-lesson sequence and public overview.
- [Flat-file databases](https://www.raspberrypi.org/curriculum/archived/key-stage-2/data-and-information-flat-file-databases): lesson sequence and investigation purpose.
- [PRIMM pedagogy summary](https://static.raspberrypi.org/files/curriculum/quickreads/11-Pedagogy_Summary_PRIMM_V4_2023.pdf): supplied programs, tracing, gradual modification, and creation. Its cited study does not establish this grade 4 course’s effectiveness.

## For Cory

- **Tool build scope:** Decide whether the planned table tool should also save a narrative-and-chart report, or another offline browser tool should provide that function. Recommendation: one small report view in the table tool. Finding 1’s coverage correction is required whichever implementation is chosen.

## For the source list

Retain the two specific archived unit links above beside the archive listing. Record the inaccessible Systems and searching page for browser checking. No new research claim is proposed.


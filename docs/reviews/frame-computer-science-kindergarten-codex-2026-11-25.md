# Second-model frame read: computer-science-kindergarten

2026-11-25. Read-only report supplied inline. No files were changed.

## What I read

- The complete kindergarten frame, its `frames.csv` row, and its rows in `calendar.csv`.
- The `grade:K` selection in `course-list.csv`: 14 progression rows owning 16 EK standards.
- Grade 1 progression rows and both ends of every kindergarten handoff. The grade 1 frame does not yet exist.
- `frame-read.md`, the after-core changes in `frame-write.md`, `EXPERT.md`, the computer science lens, subject STANDARD and APPROACH, and the computer science adoption bar.
- FOUNDATION, shared APPROACH, relevant production-path steps, BASELINE rules, GLOSSARY, calendar rules, subject decisions, base-text guidance, and relevant earlier computer science reviews.
- Published standards boundary statements, public base-unit pages, and the outside sources linked below.

No finding rests on model memory.

## Verdict

**Needs fixes before the scope and sequence is written.** The five-unit structure, ownership placement, calendar arithmetic, and paper provision are sound, but two units inherit incorrect interpretations of their standards, and several unit assessments omit the work their owned standards require. Correct those teaching and assessment contracts first, while keeping the existing unit count and 32-session budget.

**Findings: 6, ordered most serious first.**

## Checks and calendar

| Check | Result |
|---|---|
| `python -X utf8 scripts/frame.py check computer-science-kindergarten` | Passed: 0 failures; 28 unit days plus 4 course-check and respond days |
| `python -X utf8 scripts/plan.py check computer-science-kindergarten` | Reported missing plan-stage CSVs; this is a frame-stage course |
| `python -X utf8 scripts/stale.py check` | Passed: 70 files, 0 failures |
| Independent ownership and seam check | 14 rows, 16 standards, no missing reciprocal kindergarten handoffs |

The writing gate wrapper was not run because it writes output and baseline files; the filtered plan check and structural frame check were run instead.

The calendar agrees with the frame: units occupy weeks 1–5, 6–11, 14–21, 22–26, and 29–32; course checks occupy weeks 12 and 27, followed by respond weeks 13 and 28. Those checks avoid the kindergarten core check weeks. Other after-core subjects currently overlap these weeks, but the supplied after-core brief specifically requires avoidance of core checks.

The math citations also agree with the calendar: unit 2 occupies days 19–44 and unit 3 days 45–63. Each lean has a usable fallback.

## Findings

### 1. Unit 5 teaches the next grade’s history comparison instead of its owned kindergarten comparison

**Severity:** Serious  
**LAYER:** progression  
**REPEAT:** yes, partial-standard coverage was identified in `prework-computer-science-gemini-2026-11-20.md`, finding 4  
**Confidence:** Firm

**Location:** `frame.md`, Units table, unit 5; Models carried; kindergarten handoff; progression row `k-then-now`.

The unit compares activities before and after computing arrived: letters and phone messages, paper and screen maps, printed and electronic books. The kindergarten boundary instead asks children to recognize visible changes between older and newer computing devices. The activity comparison belongs to grade 1. See the [published standards, PDF page 93, printed page 88](https://csteachers.org/wp-content/uploads/2026/07/2026-CSTA-PK%E2%80%9312-Computer-Science-Standards.pdf#page=93).

**Why it matters:** A writer can follow the frame faithfully and leave EK-SOC-HI-14 untaught at its stated depth. The seam also becomes repetition rather than development.

**Exact fix:**

- Replace unit 5 session 2 with an older/newer computing-device comparison. Use an older portable computer and a current classroom laptop; children identify visible differences in the screen, keyboard, and case.
- Use the [Computer History Museum’s 1981 collection timeline](https://www.computerhistory.org/timeline/1981/) as the teacher’s factual source for the older example. Use direct observation of the classroom device for the current example. Curio Class supplies its own generic drawings.
- Replace the history assessment with an unfamiliar older/newer device pair and a spoken or pointed identification of a visible change.
- Change `k-then-now` notes, the model description, and the kindergarten handoff to this device comparison. Keep grade 1’s activity comparison as its next step.
- Keep the two-card timeline, four unit days, and existing standard ownership.

The progression correction belongs to the lead; the reader edits nothing.

### 2. Unit 2’s exclusion removes part of its owned algorithm standard

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, boundary-depth coverage is the same kind as the earlier second-model pre-work finding 4  
**Confidence:** Firm

**Location:** `frame.md`, unit 2, “What students learn,” especially “no breaking a task into parts”; progression row `k-people-steps`.

EK-ALG-IM-03 includes a simple description of how people develop an algorithm: identify a task, recognize smaller parts, and order steps. The blanket exclusion removes that description. The separate requirement to teach the word *algorithm* in context is also absent from the frame and `k-follow-steps` vocabulary. See [PDF pages 40 and 49, printed pages 35 and 44](https://csteachers.org/wp-content/uploads/2026/07/2026-CSTA-PK%E2%80%9312-Computer-Science-Standards.pdf).

**Why it matters:** “People made the rules” is narrower than describing how people devise steps to solve a problem. The current exclusion directs the writer away from required teaching.

**Exact fix:** Replace the exclusion and add this teaching direction:

> Session 1 names an ordered set of steps an algorithm, spoken beside the picture cards. In session 2, children describe how a person chooses a task, notices its smaller parts, and orders steps to reach the goal. Connect this to instructions people give computers. Out: no independent decomposition method, conditional instructions, repetition, or translation into code.

The lead should add `algorithm` to `k-follow-steps.words` and the simple human planning process to `k-people-steps.notes`. This describes people’s planning without importing grade 1’s independent decomposition task.

### 3. Units 2, 3, and 4 have incomplete end-of-unit evidence

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** Firm

**Location:** `frame.md`, Evidence bullet; unit 2–4 assessment descriptions; Course-level checks.

Three assessment contracts are incomplete:

- **Unit 2:** “Say who could change a rule” does not check the human planning process or explain that people create computing technologies. The mid-year check then carries this inadequate record forward.
- **Unit 3:** The assessment predicts, identifies a wrong command, and interprets signs, but does not create a command sequence. Creation appears in the later course check, after the unit’s respond opportunity.
- **Unit 4:** Reading a supplied graph and suggesting a choice omits posing a question and participating in collecting its data. The year-end check carries that record forward too.

These are doing and explaining requirements, confirmed by the [published standards](https://csteachers.org/wp-content/uploads/2026/07/2026-CSTA-PK%E2%80%9312-Computer-Science-Standards.pdf), not interchangeable recognition tasks.

**Why it matters:** The teacher can record completion while lacking evidence for owned outcomes. The scheduled respond day cannot address work the assessment never observes.

**Exact fix:**

| Unit | Replacement or addition within its existing assessment session |
|---|---|
| 2 | Add a short picture-supported explanation: how a person planned steps for a goal, and who made the pictured computer game or computing tool. Record the two look-fors separately. |
| 3 | Add an unseen short route for which each child arranges a command sequence. Ask the child to describe its movement. Keep wrong-command identification and sign interpretation; score repair separately only if treated as extension. |
| 4 | Replace the supplied-graph-only task with a brief investigation: each child proposes a concrete question with support, contributes to gathering a small group’s answers, and uses the resulting display to answer it and support a choice. Use individual observation marks within the group task. |

Update the course-check cells so carried records name this evidence. Retain the five unit assessment sessions and five unit respond sessions.

### 4. Unit 2 asks children to make before they modify

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** Firm

**Location:** `frame.md`, unit 2 sessions 2 and 4; Day kinds bullet.

Session 2 asks children to make their own game step-card set. The first explicit modification of a working set comes in session 4. This reverses both the subject APPROACH and the frame’s own promised order.

The [PRIMM teaching summary](https://static.raspberrypi.org/files/curriculum/quickreads/11-Pedagogy_Summary_PRIMM_V4_2023.pdf) supports beginning with supplied programs before modification and creation. Its use with kindergarten remains the repository’s stated, untested adaptation.

**Why it matters:** The session descriptions give the scope writer a conflicting sequence, despite the general rule being correct.

**Exact fix:**

- In session 2, supply a working game step-card set. Children follow it, change one step, predict, and check the result while discussing who designed it.
- Move creating their own set and having a classmate follow it to session 4.
- Label session 4 **Application**. Keep its sorting task as retrieval or brief practice.
- Update the Day kinds example so it does not describe session 4 as a Fluency session containing new creation.

No days or standards move between units.

### 5. The source map needs an explicit adaptation sequence and complete exclusions

**Severity:** Moderate  
**LAYER:** base text  
**REPEAT:** new  
**Confidence:** Likely for the adaptation risk; firm for the incomplete public-page entries

**Location:** `frame.md`, Source map; unit 3 base description.

The map splits “Grouping data” into source lessons 1, 3, 4 followed later by 2, 5, 6, without explicitly acknowledging the changed source order. It also describes the last robot lessons mainly as prediction and repair, while the public lesson 5 includes planning and creating. Three excluded units retain “lesson count not opened,” and the animation page is now reachable.

The publisher says lessons follow numerical order, so a deliberate adaptation needs its own reason and sequence. See the [source ordering guidance](https://teachcomputing.org/curriculum/key-stage-1), [Grouping data](https://teachcomputing.org/curriculum/key-stage-1/data-and-information-grouping-data), and [Getting there](https://teachcomputing.org/curriculum/key-stage-1/programming-a-moving-a-robot/getting-there).

**Why it matters:** A scope writer cannot tell whether the reordered and compressed material preserves the intended learning or merely preserves lesson titles.

**Exact fix:**

- State that sorting moves ahead of counting to establish attribute groups in unit 2, with counting and question answering resumed in unit 4 after the math lean.
- Map robot lessons 1–3 to session 2, lesson 4 to session 3, and the planning, creation, and testing from lessons 5–6 to session 6. Identify sessions 4–5 as Curio Class trace and wrong-command work.
- Replace each excluded unit’s unknown count with “Lessons 1–6, all left out,” retaining its exclusion reason. The public pages list six lessons each: [Digital painting](https://teachcomputing.org/curriculum/key-stage-1/creating-media-digital-painting), [Digital writing](https://teachcomputing.org/curriculum/key-stage-1/creating-media-digital-writing), and [Programming animations](https://teachcomputing.org/curriculum/key-stage-1/programming-b-introduction-to-animation).
- Keep the pending source-store and third-party checks explicit. Public summaries do not establish the contents or rights of downloaded lesson packages.

### 6. The disability sensitivity read has no named community source

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, the earlier pre-work reads identified incomplete sensitivity preparation  
**Confidence:** Firm

**Location:** `frame.md`, Sensitivity reads bullet and unit 1 teacher notes.

“Disability-led guidance” and “the federal Section 508 program’s plain-language pages” describe source categories, not sources the agent must study. Frame-write lessons 12 and 30 require named sources for flagged content.

**Why it matters:** The next reader must invent the preparation pack, and a government accessibility page cannot supply disabled people’s own perspectives.

**Exact fix:** Name and link a starting pack in unit 1’s note:

- [ASAN, Identity-First Language](https://autisticadvocacy.org/about-asan/identity-first-language/), for one community’s account of language and identity, without treating it as universal.
- [Section508.gov, Hardware ICT Overview](https://www.section508.gov/test/ict-hardware-overview/), for accessible hardware and assistive-technology distinctions.

Also retain the sensitivity brief’s requirement to expand this to at least five sources, including two community-owned sources matched to the disabilities actually represented in the finished materials.

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| Keep five units and 32 sessions | The allocation fits the relative loads and includes response time | Kindergarten frame |
| Keep course checks in weeks 12 and 27 | They satisfy the supplied core-week avoidance rule | Kindergarten frame and calendar |
| Use visible device changes for kindergarten history | Restores the owned depth and a distinct grade 1 handoff | Frame; `k-then-now` notes |
| Describe human planning without teaching independent decomposition | Covers the kindergarten requirement while preserving grade 1 development | Frame; `k-people-steps` notes |
| Repair assessments inside existing sessions | The missing evidence does not require another unit or a longer year | Frame |
| Modify supplied game steps before creating new ones | Makes the concrete session order follow the subject approach | Frame |

## Lens checklist, course-frame layer

| Lens line | Result |
|---|---|
| Five concepts, with AI foundations inside content | Met |
| Read and predict, then modify, then make | Missed in unit 2; finding 4 |
| Unplugged teaching and meaningful device use | Met in the frame |
| Explicit model of commands running in order | Met |
| Debugging taught through predictable steps | Met in outline; distinguish kindergarten identification from scored repair |
| Collaboration and human-centered practices inside content | Met |
| Society grounded in evidence | Partly met; correct and source unit 5 |
| Non-specialist teacher support | Required through APPROACH; execution belongs to later plans |
| Standards within their boundary depth | Missed; findings 1–2 |
| Specialty claims restricted | Not applicable; none claimed |
| No unit without unplugged work | Met |
| Middle-school text-code bridge | Not applicable |

## What is right and should not be touched

- All owned rows appear exactly once, and every kindergarten handoff has its reciprocal grade 1 assumption.
- Step-cards precede programming, sorting precedes data grouping, and math timing has explicit bridges.
- Programming receives eight sessions, compared with four for the lighter society unit. Equal allocation would be weaker.
- Paper provision, pre-reader responses, privacy controls, movement access, cleanup time, and respond days are concrete.
- Unit 5 can follow the course-level check because its own assessment remains counted.

## What I could not judge

- The grade 1 frame’s actual pickup of these seams, because that frame is absent.
- Full base-lesson contents, third-party permissions, or whether their detailed activities fit the compressed sessions. Only public pages were checked.
- Finished assessment timing, rubrics, keys, and teacher explanations. These do not exist at frame level.

## For Cory

- **Editor scope:** The frame proposes extending the approved grade 3–5 editor into kindergarten–grade 2 picture-block mode. That changes build scope. Recommendation: consider it separately; keep this course runnable through its complete paper provision.
- **Source acquisition:** The frame proposes an adult sign-in to obtain the partial base. Account creation remains Cory’s decision; public-page mapping does not settle acquisition or reuse checks.

## For the source list

Add the linked museum device-history source and the named sensitivity sources if absent. The published standards, PRIMM summary, and public base-unit pages were checked live for this report; no finding relies on an unopened research claim.
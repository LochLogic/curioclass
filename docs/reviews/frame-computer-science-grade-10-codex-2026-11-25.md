# Frame read: computer-science-grade-10
2026-11-25 | Independent second reader | Read-only report

## Verdict

The frame has a sound content structure: all 15 selected progression rows are placed once, its 12 owned standards have substantial teaching, and its calendar fits 64 course days. The biggest risk is its assumption that students took the previous computer science elective, followed by an overloaded year-end assessment session. Five findings need correction before scope and sequence: two serious, two moderate and one minor.

## What was read and checked

- `docs/pipeline/briefs/frame-read.md`, the applicable frame-write rules and after-core changes, `docs/agents/EXPERT.md`, and the computer science lens.
- The computer science adoption bar, `STANDARD.md` and `APPROACH.md`, with the shared foundation, approach and relevant production and decision rules.
- `docs/courses/computer-science-grade-10/frame.md` in full; its course-list selector, frames row and calendar rows.
- All 15 rows selected by `grade:10` in `data/progressions/computer-science.csv`, including their incoming and outgoing links.
- The adjacent grade 9 and grade 11 frames; grade 8 mathematics’ Units table for the scatter-plot prerequisite.
- The earlier combined grades 6 to 12 frame review and relevant pre-work and progression reviews, after reading the frame.
- All 12 owned standards’ boundary statements in the stored 2026 CSTA PDF, PDF pages 44, 48, 52, 58, 63, 72, 86, 88, 89, 98 and 101: :codex-file-citation{path="S:/CurioClass-sources/computer-science/csta-2026-11-21/csta-2026-pk12-cs-standards.pdf" purpose="source"}

No files were changed.

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check computer-science-grade-10` | One stage-related failure: lesson-plan data files are absent. The command was course-filtered as repository instructions require. |
| `python -X utf8 scripts/frame.py check computer-science-grade-10` | 0 failures; 58 unit days and six check/respond days. |
| `python -X utf8 scripts/stale.py check` | 121 files checked, 0 failures. Unmarked stale statements remain, identified below. |

The plan-stage failure does not block this frame verdict.

## Findings

### 1. Serious: the entry path assumes students took grade 9 computer science

**LAYER:** frame  
**REPEAT:** yes, earlier combined frame review S1  
**Confidence:** firm

**Location:** Seams, “Picked up from Grade 9 computer science,” frame lines 139 to 166; unit openings in lines 217 to 222.

The frame treats grade 9 procedures, lists, algorithm design, network reading, data dictionaries and other skills as available through short retrieval tasks. The subject standard describes grades 6 to 12 as electives, and frame-write rule 32 explicitly prohibits assuming an optional course was taken. The readiness checks for two grade 8 rows do not address a student who skipped grade 9.

Such a student encounters the first unit’s procedure and list work without a stated teaching path. Later units repeat the same problem with their assumed prerequisites.

**Exact fix:** Add a **Course order** bullet and a fallback column to the incoming Seams table:

> Earlier computer science electives are helpful but are not assumed. Each unit checks the prerequisite concepts before using them. Students who show those concepts begin with retrieval; students who do not receive a worked example and supported practice before the unit’s independent task.

Place one combined ten-minute prerequisite check at each of these existing points:

| Unit entering | Check placement | Concepts checked |
|---|---|---|
| 1 | Last ten minutes of course day 1 | Procedures, parameters, lists, tracing, saved-code evaluation and attribution |
| 2 | Last ten minutes of day 12 | Reading pseudocode, comparing equivalent procedures and recognizing previously introduced AI types |
| 3 | Last ten minutes of day 21 | Reading a network, security measures and packet paths |
| 4 | Last ten minutes of day 32 | Data dictionaries, allowed values and ranges |
| 5 | Last ten minutes of day 42 | Identifying a design’s users, benefits and harms |
| 6 | Last ten minutes of day 53 | Reading a technology timeline and distinguishing technical differences from societal effects |

Combine these with existing readiness items rather than adding a second check to the same ten minutes. For every checked prerequisite, name the worked example, practice and minutes provided when it is missing. Keep later-owned standards as contributions, but teach their introductory tasks without requiring the earlier elective.

### 2. Serious: day 62 contains two full unseen performances

**LAYER:** frame  
**REPEAT:** yes, the assessment-load pattern in the earlier combined review S3  
**Confidence:** likely, based on the specified work and available minutes

**Location:** Unit 6, frame line 222; year-end Course-level checks row, line 229.

Day 62 requires both an evidence-based evaluation of an emerging technology across society, environment and access, and a different unseen case analyzed at four decision points. The second task alone asks for twelve risk/benefit/long-term-effect entries plus a defended judgment.

These are two substantial performances in a period the frame estimates provides about 35 teaching minutes. Moving earlier-unit sampling to day 63 does not resolve this load. Frame-write rule 19 limits an end day to one full performance.

**Exact fix:** Keep all unit lengths and calendar dates. Replace unit 6 lesson 8’s general review, course day 61, with the unseen human-choices assessment for **HS-SOC-HU-43**. Day 62 then assesses **HS-SOC-ET-41** alone; day 63 retains the earlier-unit samples and carries day 61’s result unscored. Day 64 responds to both assessments.

Update the Days and Evidence bullets, unit 6’s assessment description and the year-end check row to state that unit 6’s assessment spans day 61 and the following check. No standard moves between units, and the total remains 64 days.

### 3. Moderate: the progression still permits acting the disability personas

**LAYER:** progression  
**REPEAT:** yes, earlier combined review M5  
**Confidence:** firm

**Location:** `data/progressions/computer-science.csv`, line 167, `g10-design-hcd` notes; compare frame unit 5, line 221.

The frame carefully requires written persona cards that are never acted. The progression still says, “User stand-ins are classmates playing roles.” Because the progression rows are the planning contract, a later writer could follow that wording and introduce the activity the frame expressly excludes.

**Exact fix:** Replace that sentence in the progression note with:

> User stand-ins are written persona cards read aloud, never acted; no student imitates a disability or supplies personal information.

Keep the frame’s existing safeguards. This is a wording correction within the existing task and scope.

### 4. Moderate: unit 3 leaves its real case unselected

**LAYER:** frame  
**REPEAT:** yes, the unresolved-case/source pattern identified in progression review finding 8  
**Confidence:** firm

**Location:** Unit 3, frame line 219, lesson 8 and teacher-source column.

The invented hospital case is usable and clearly labeled. The second case, however, is only “a second case” from government pages. The HHS reporting portal, a general social-engineering page and a phishing page are source categories rather than a selected case. Frame-write rules 11 and 23 require the pick and its usable source before the next writer begins.

This leaves the scope writer to choose the incident, establish its facts and determine which consequences the evidence supports.

**Exact fix:** Specify the second card as:

> An observed employee-impersonation scheme documented in the FBI/IC3 advisory of April 11, 2024: criminals obtain credentials, impersonate employees and seek account changes through support staff. Students classify its cause and the documented risks to accounts and data. Claims about further consequences are labeled possible, not established.

Use the [FBI/IC3 advisory](https://www.ic3.gov/PSA/2024/PSA240411) as the exact teacher source. Select only the conceptual description and consequences for the card, excluding procedural attack details. Keep the invented hospital case for practicing the complete stakeholder grid.

The frame’s named CISA page returned **403, browser check**. It was not fetched another way; the FBI source was the alternative.

### 5. Minor: several status statements and pointers contradict current files

**LAYER:** process  
**REPEAT:** yes, earlier combined review S3 and M4, plus its wording findings  
**Confidence:** firm

**Location:** frame lines 3, 50, 203 and 251 to 258.

Several statements can now misdirect the next writer:

- **For the lead 3** calls progression changes “needed,” although the packet link, cleaning depth, case notes, industry wording and US spelling have landed.
- **For the lead 2** says grades 6 to 9, 11 and 12 copy the two-lesson checks. The adjacent grade 9 and grade 11 frames still allocate one lesson per check.
- The **test-table** model says it was last used in grade 8. Grade 9 unit 2 lesson 3 explicitly uses it.
- The practices bullet calls its Units column the fifth; it is the sixth.
- The header uses “catalogue,” contrary to the US-spelling rule.

**Exact fixes:**

1. Replace For the lead 3 with:

   > The packet-strip prerequisite, cleaning structure, case descriptions, industry wording and human-centered spelling are present in the progression. The remaining g10-design-hcd correction is to specify persona cards read aloud, never acted. Case-fact verification remains separate from these row edits.

2. Replace For the lead 2 with:

   > This frame allocates two lessons per course-level check. Other grades retain their own current allocations; any band-wide change belongs to the lead’s reconciliation pass.

3. Change the test-table origin cell to:

   > Grade 4 (g4-debug-increment); used again in grade 9 unit 2 lesson 3 and its later program tests.

   Preserve the grade 8 generated-code readiness item, which checks a distinct application.

4. Change “fifth column” to “sixth column.”
5. Change “catalogue id” to “catalog id.”

## Coverage, days and seams

All 15 selected skill rows appear once. The frame owns 12 standards, with concept counts ALG 3, DAT 2, PRO 2, SOC 2 and SYS 3. Five later-owned codes are identified as contributions with their owner grades. No Specialty or X + CS code is claimed.

The unit allocations are **12 + 9 + 8 + 10 + 11 + 8 = 58 days**. Four check days and two respond days bring the course to 64. No unit is conspicuously over- or underallocated relative to its programming, design, data or case-analysis load; finding 2 concerns assessment placement within that allocation.

The calendar rows match the frame:

| Event | Course days | School days | Weeks |
|---|---:|---:|---:|
| Mid-year check | 30 to 31 | 75 and 78 | 15 to 16 |
| Respond | 32 | 80 | 16 |
| Year-end check | 62 to 63 | 155 and 158 | 31 to 32 |
| Respond | 64 | 160 | 32 |

The mid-year check avoids the stated core check weeks. Week 32 is permitted for high school finals. After-core overlaps remain the lead’s calendar pass; the current rows also show SEL sharing the mid-year check’s school day 75.

Incoming and outgoing progression links are reciprocal. Grade 9’s intended handoffs and grade 11’s pickups match in content. Grade 8 mathematics unit 4 teaches the scatter plots used here, and the frame provides a worked-chart reminder. No same-year core prerequisite was found to be scheduled after its use.

There is no base text for this grade, so a source map is not applicable.

## Lens checklist

| Frame-level lens test | Result |
|---|---|
| All five concept areas receive substantial teaching | Met |
| AI has algorithm/data foundations rather than one isolated late unit | Met |
| Read, trace and modify precede independent code work | Met |
| The notional machine and systematic debugging are explicit | Met |
| Practices occur inside content, including switching pair roles | Met |
| Every unit includes unplugged work | Met |
| Owned standards respect their boundary depth | Met in planned teaching; assessment-load repair required |
| Specialty claims stay within the Foundational course’s limits | Not applicable: none claimed |
| Society work uses evidence and more than one view | Partly met: selected cases exist, but unit 3’s second case needs finding 4 |
| A non-specialist teacher receives content and debugging support | Met as a frame commitment; finished materials remain to be reviewed |

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Retain six units and their current lengths | Content order and allocation are defensible | Grade 10 frame |
| Assess human choices on day 61 and emerging impacts on day 62 | Gives each full performance its own session without adding days | Grade 10 frame |
| Use read-aloud persona cards | Resolves the progression/frame conflict | Computer science progression |
| Use the dated FBI advisory for unit 3’s second card | Provides a concrete, accessible primary source | Grade 10 frame |
| Retain the no-device “part met” labels for HS-DAT-DC-23 and HS-PRO-PD-13 | The frame correctly distinguishes learning the idea from completing the device requirement | Grade 10 frame |

## What is right and should not be touched

Keep the code-reading emphasis, explicit boundary exclusions, independent explanations within the team design project, invented personal data, offline tool requirements and honest device exceptions.

I do **not** repeat the earlier combined review’s M8 as an established fault. The written rules do not require separate draft and feedback days, and the approach’s explicit requirement to end every unit with a respond day applies to K to 5. Grade 10’s portfolio after its respond lesson is not, by itself, a demonstrated violation.

Different check lengths across grades also do not require changing this frame’s allocation. The false statement that other grades already copy it does require correction.

## What could not be judged

Completed tools, source packets, keys, rubrics and timed assessment items do not yet exist at this layer. Their usability, accessibility and actual completion times remain later checks.

No finding rests on unaided memory. The broad Michigan case was corroborated, but its complete court record and every proposed unit 6 factual claim were not independently reread. The proposed HHS settlement page could not be opened because its archive redirect was inaccessible; no finding relies on its contents.

## Outside sources

- [2026 CSTA standards PDF](https://csteachers.org/wp-content/uploads/2026/07/2026-CSTA-PK%E2%80%9312-Computer-Science-Standards.pdf): checked the owned standards’ boundary depth.
- [Computing pedagogy](https://www.raspberrypi.org/teach/pedagogy): supports retaining code comprehension, modeling and gradual movement toward independent work.
- [FBI/IC3 social-engineering advisory, April 11, 2024](https://www.ic3.gov/PSA/2024/PSA240411): the concrete replacement source in finding 4.
- [Michigan’s October 2022 settlement announcement](https://www.michigan.gov/ag/news/press-releases/2022/10/20/som-settlement-of-civil-rights-class-action-alleging-false-accusations-of-unemployment-fraud): corroborates the automated unemployment-fraud case and consequences.
- [FTC COPPA FAQ](https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions): checked the distinction between privacy requirements and an operator’s decision to block younger users.
- [CISA’s named social-engineering page](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks): **browser check, 403**.

## For the source list

Add the FBI/IC3 advisory above to `docs/APPROACH-SOURCES.md`, recording its date and use for the conceptual social-engineering case.

## For Cory

None of the proposed repairs changes the course’s scope, audience, money or outside people. The entry fallback implements the existing optional-course rule.
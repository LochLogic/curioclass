# Independent frame read: Library and Research Skills, grade 1

**Date:** November 25, 2026  
**Course:** `library-and-research-skills-grade-1`  
**Findings:** 3  
**Delivery:** Complete report here. No files changed.

## Verdict

The frame is sound in its sequence, placement of all eight progression skills, ownership of AASL.I.A.2, and handoffs between kindergarten and grade 2. Its largest concrete risk is a final reflection that requires individual sheets the teacher has already sent home. Fix that materials conflict, identify the remaining host tasks by progression row, and update the stale work-status notes before writing the scope and sequence.

## What I read and checked

- `docs/pipeline/briefs/frame-read.md`, the applicable frame-writing instructions, EXPERT, FOUNDATION, relevant production-path and BASELINE provisions, and the shared approach and source guidance.
- The library lens, library STANDARD and APPROACH, the shared adoption criteria, the library subject bar, and relevant library decisions.
- The complete grade 1 frame, its `grade:1` selector in `course-list.csv`, its `frames.csv` row, and its calendar rows.
- All eight grade 1 library progression rows, their preceding and receiving rows, the named standard phrases, and the kindergarten and grade 2 frames.
- The relevant grade 1 ELA and science Units tables, their calendar placements, and selected scope and lesson-data entries to check availability and stale notes.
- Earlier library pre-work, progression, kindergarten frame reviews and fixes, and the applicable frame-review lessons.
- The stored continuum document named in the frame, reading its grade 1 column and priority-skill boxes directly from its tables.
- The outside sources linked below.

There is no base text or source map to review. This is a single-grade course, so the band-course Year column requirement is not applicable.

| Required check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check library-and-research-skills-grade-1` | One failure: the plan stage expects lesson-plan CSVs that do not exist at this frame stage. Course filtering follows the repository instruction. |
| `python -X utf8 scripts/frame.py check library-and-research-skills-grade-1` | **0 failures:** four units, 30 sessions, 25 in units and five for course checks and response. |
| `python -X utf8 scripts/stale.py check` | Three failures, all in the physical education grades 3 to 5 frame. None concerns this course. |

These results do not withhold the frame verdict. The aggregate gate was not run because it can write a baseline.

Independent checks confirmed:

- Each of the eight selected skills appears in exactly one unit.
- Both directions of every grade 1 progression handoff match.
- The frame identifies its one owned standard and ten carried standards correctly.
- Unit sessions total `6 + 6 + 6 + 7 = 25`.
- Library checks in weeks 13 and 28 avoid the grade 1 core check weeks: 14, 15, 16, 19, and 29 through 32.
- The stated after-core clashes match the calendar.

## Findings, most serious first

### 1. The final reflection requires sheets that have already gone home

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** firm, an internal materials conflict

**Location:** [Evidence, line 71](S:/CurioClass/docs/courses/library-and-research-skills-grade-1/frame.md:71) and [year-end response, line 185](S:/CurioClass/docs/courses/library-and-research-skills-grade-1/frame.md:185).

**What is wrong:** The Evidence bullet sends sheets home after marking and says no individual record outlives its unit. Week 30 nevertheless requires each child to compare a “know” from a unit 1 sheet with current knowledge. No retained copy, classroom display, or reliable return route is specified.

**Why it matters:** The teacher cannot run the promised comparison from the materials available. Requiring families to preserve and return the sheets would add an unstated dependency.

**Exact fix:** Preserve a class-level starting point:

1. Add to unit 1’s inquiry description: “Keep an anonymous class know-and-wonder display, with no names or individual scores, for the year-end reflection.”
2. In the year-end response description, replace the individual-sheet comparison with: “Each child compares one ‘know’ from the anonymous class display made in unit 1 with what they know now.”
3. Add the display to the materials list.

This preserves the existing handling of individual sheets and the purpose of the final reflection.

### 2. Units 1 and 3 do not identify their host tasks by progression row

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, the host-task traceability requirement appears in `prework-library-read-2026-11-20.md`, finding 9  
**Confidence:** firm

**Location:** [Host tasks](S:/CurioClass/docs/courses/library-and-research-skills-grade-1/frame.md:48), [unit 1](S:/CurioClass/docs/courses/library-and-research-skills-grade-1/frame.md:175), [unit 3](S:/CurioClass/docs/courses/library-and-research-skills-grade-1/frame.md:177), and the closing Cross-subject paragraph.

**What is wrong:** The frame promises a host task identified by row ID in every unit, following library APPROACH. Unit 1 names science topics and unit numbers; unit 3 names ELA’s bird topic and unit number. Neither supplies the host-task row ID. Units 2 and 4 already provide an indexed science host.

**Why it matters:** The topics are suitable, but the scope writer must infer which core task the library work supports.

**Exact fix:** Replace the two host descriptions with:

- **Unit 1:** “Host: the class’s sky observations and questions, `science:s1-sky-patterns`, science grade 1 unit 1 (days 1 to 8), or its plant-part investigation, `science:s1-parts-mimic`, unit 2 (days 10 to 21).”
- **Unit 3:** “Host: the provided-source research on bird body parts, reviewing `ela:e1-shared-research`, and its informative writing, reviewing `ela:e1-informative`, ELA grade 1 unit 3 (days 79 to 119).”

Repeat those IDs in the closing Cross-subject paragraph. Keep the existing stand-alone questions and availability fallbacks.

### 3. The frame describes completed work as pending

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale status notes were finding 7 of the kindergarten expert frame read and finding 3 of its independent read  
**Confidence:** firm

**Location:** [Check set read, line 117](S:/CurioClass/docs/courses/library-and-research-skills-grade-1/frame.md:117), [Cross-subject, lines 198 onward](S:/CurioClass/docs/courses/library-and-research-skills-grade-1/frame.md:198), and [For the lead, item 1](S:/CurioClass/docs/courses/library-and-research-skills-grade-1/frame.md:225).

**What is wrong:**

- The Check set read says two differences still need progression notes, and For the lead asks that both notes be added. Both are already present in `data/progressions/library.csv`: `g1-story-or-fact-book` at line 10 and `g1-device-stop-rule` at line 16.
- Cross-subject says exact lesson availability waits on the core scopes and sequences. The grade 1 ELA and science scopes and lesson-data files already exist. For example, ELA explicitly teaches the story/information distinction on course day 35 and contents/headings on day 81.

**Why it matters:** These notes invite duplicate progression edits and leave the next writer treating available scheduling evidence as missing.

**Exact fix:**

1. Replace “Differences, each needing a row note” with “Differences, each recorded in its progression row note.”
2. Replace For the lead item 1 with: “**L103 row notes applied.** The bin-label and username substitutions are recorded in `g1-story-or-fact-book` and `g1-device-stop-rule` in `data/progressions/library.csv`.”
3. Replace the Cross-subject waiting clause with: “The ELA and science scopes and lesson-data files already exist. The library scope and sequence should use those day placements when scheduling host tasks; each lean retains its ‘if later’ route for local scheduling differences.”

## Lens checklist at the frame layer

| Lens requirement | Result |
|---|---|
| A year of spaced units and a growing inquiry cycle | Met: four units, with judge and use explicitly located within the four-picture cycle. |
| Named priority skills, without duplicate ownership | Met: eight rows placed once; AASL.I.A.2 owned here. |
| Grade placement checked against the continuum | Met: substitutions and deferrals are explained; the two requested difference notes already exist. |
| Skills taught on real work | Partly met: suitable tasks and stand-alone routes exist; finding 2 completes their row references. |
| Source judgment avoids a website-appearance checklist | Met at this grade’s boundary. Source-kind selection is taught here; formal lateral reading is owned later. |
| Questions, finding, and navigation grow in a sensible order | Met: prior knowledge and source choice precede navigation, teamwork, and the final product. |
| Honest use in the band | Met: title and author accompany found information, with help and without shaming. |
| Product, audience, feedback, and reflection | Met in design; finding 1 repairs the final reflection’s materials dependency. |
| No paid-library or device dependency | Met: the closed paper route is complete. |

## What is right and should be retained

The six-session units and seven-session final unit have intelligible reasons. Navigation comes before team finding, and the final book brings earlier skills back into use. The frame supplies concrete assessments for all eight rows, protects response sessions, supports early readers, and names realistic paper substitutes.

The narrower course-level samples also preserve the kindergarten fix: they revisit earlier units on new cases and reuse the just-ended unit’s result without scoring it again.

## Settled by the expert

These are recommendations for the caller to apply. No files were edited.

| Choice | Reason | File touched |
|---|---|---|
| Use an anonymous class display for the final comparison | Makes the reflection runnable with the stated materials policy | Grade 1 library frame |
| Supply the existing science and ELA row IDs for units 1 and 3 | Makes the host tasks traceable without changing their content | Grade 1 library frame |
| Mark the two progression notes applied and acknowledge existing core scopes | Removes stale instructions | Grade 1 library frame |
| Retain four units and the 30-session allocation | Placement, totals, sequence, and calendar checks support them | No allocation change |

## What I could not judge

The student texts, assessment sheets, rubrics, and library lesson plans do not yet exist. Their reading load, scoring quality, and actual administration time remain for the later reads. The stated assessment totals fit arithmetically within 19 working minutes, but the unit plans still need to account for dictation, group changes, and teacher recording.

## Sources and evidence limits

- [AASL learner framework, second edition](https://standards.aasl.org/wp-content/uploads/2026/07/250918-AASL-framework-for-learners.pdf): opened directly to check the owned competency and the boundaries of carried competencies.
- [AASL second-edition explanation](https://standards.aasl.org/2edition/): checked the edition and continuity of the framework.
- [NYC School Library System’s continuum overview](https://nycdoe.libguides.com/c.php?g=895467&p=7009946): confirms the grade-priority and cross-curricular purpose of the continuum. Detailed grade 1 checks used the stored PK to 2 document named in the frame.
- [National Center for Missing and Exploited Children resources](https://www.missingkids.org/netsmartz/resources): verified the listed K to 2 presentation. The presentation itself was not read, so its detailed content is not evidence for this verdict.
- [Monroe continuum guide](https://libguides.monroe.edu/ESIFC/Intro) and [SLSA continuum guide](https://slsa-nys.libguides.com/ifc/intro): **browser check**, unavailable through the web tool. Neither was fetched another way.

No finding rests on recalled outside research. Prior workspace memory informed only the review workflow; findings rest on files and sources checked during this read.

## For the source list

Record the accessible NYC continuum overview and the current access status of the two continuum guides.

## For Cory

None. These findings require no scope, money, people, or audience decision.


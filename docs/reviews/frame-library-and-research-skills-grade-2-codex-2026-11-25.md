# Independent frame read: Library and Research Skills, grade 2

**Date:** November 25, 2026  
**Course:** `library-and-research-skills-grade-2`  
**Findings:** 5  
**Delivery:** Complete report here. No files changed.

## Verdict

The frame has a sound sequence, complete placement of its nine progression skills, and coherent handoffs from grade 1 to grade 3. Its largest risk is that the specified final assessment checks reading another pair’s poster without explicitly assessing the product and reflection promised by its own research-sharing row. Keep the four units and 29 sessions, but repair that evidence gap, the missing guided practice, the reflection’s materials dependency, and the traceability and status notes before writing the scope and sequence.

## What I read and checked

- The frame-reading brief, applicable after-core frame-writing instructions, EXPERT, FOUNDATION, relevant BASELINE and production-path provisions, and shared approach and source guidance.
- The library lens, STANDARD and APPROACH, shared adoption criteria, library subject bar, and relevant recorded decisions.
- The complete grade 2 frame, its `grade:2` course-list selector, `frames.csv` entry, and calendar rows.
- All nine selected library progression rows, their preceding and receiving rows, and the complete neighboring grade 1 and grade 3 frames.
- The relevant grade 2 ELA, science and social studies Units tables and calendar placements.
- The stored continuum document named by the frame, including every grade 2 indicator cell and its priority-skill boxes, extracted directly from its tables.
- Earlier library progression, pre-work and frame reviews relevant to repeated findings.
- The outside sources linked below.

There is no base text or source map. This single-grade course does not need the band-course Year column.

| Required check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check library-and-research-skills-grade-2` | One failure: missing lesson-plan CSVs at this frame stage. The command was course-filtered under repository instructions. |
| `python -X utf8 scripts/frame.py check library-and-research-skills-grade-2` | **0 failures:** four units, 29 sessions, 24 in units and five for course checks and response. |
| `python -X utf8 scripts/stale.py check` | Eight failures, all in other courses. |

The aggregate gate was not run because it writes output and baseline files; these limitations do not withhold the frame verdict.

Independent checks confirmed:

- All nine selected skills appear in exactly one unit.
- Both directions of the grade 1 and grade 3 handoffs match.
- The two owned IDs are `AASL.IV.A.2` and `AASL.VI.B.2`. Their treatment is defensible at the stated grade 2 depth.
- Twelve later-owned competencies are introduced with help, with `AASL.I.A.2` additionally returning as review.
- Sessions total `6 + 6 + 6 + 6 + 2 + 3 = 29`.
- Checks in weeks 13 and 27 avoid core check weeks 14 to 16, 18 to 20, 28, 29, 31 and 32.
- The stated week 27 after-core clashes match the calendar.

## Findings, most serious first

### 1. Unit 4’s named assessment does not establish its research-sharing skill

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, incomplete priority-skill checks were finding 3 of the kindergarten expert frame read  
**Confidence:** likely

**Location:** [Unit 4, line 200](S:/CurioClass/docs/courses/library-and-research-skills-grade-2/frame.md:200).

**What is wrong:** `g2-research-share` includes making a pair poster from found facts, sharing it, responding to another poster, and looking back on the process. Its specified end-of-unit evidence is a sentence about what a pretend class’s poster taught the child. That checks responding to another product, but the frame does not explicitly score the pair’s own product or each child’s look-back. The general daily-observation promise does not identify these as assessment evidence.

**Why it matters:** A writer can follow the listed assessment exactly and report success for this row without establishing its central product-making and reflection components.

**Exact fix:** Add this to Unit 4’s end-of-unit evidence:

> The assessment also uses the pair’s completed poster and each child’s explanation and look-back from inquiry day 4. The checklist records whether the poster answers the class question with two source-supported facts and credits, whether each child explains a contribution, and whether each child identifies one successful step and one next improvement. Mark the poster after class and collect the spoken evidence during the scheduled sharing. The new-poster sheet item is the transfer sample for responding to another product.

Name these observation windows in the unit plan’s time budget. Keep the existing assessment sitting and respond day.

### 2. Two new skills pass directly from demonstration to inquiry without guided practice

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** firm, against the subject’s stated teaching sequence

**Location:** [Day kinds, line 29](S:/CurioClass/docs/courses/library-and-research-skills-grade-2/frame.md:29), [Unit 1, line 197](S:/CurioClass/docs/courses/library-and-research-skills-grade-2/frame.md:197), and [Unit 2, line 198](S:/CurioClass/docs/courses/library-and-research-skills-grade-2/frame.md:198).

**What is wrong:** Unit 1 introduces matching questions to source kinds on day 3, after its practice day. Unit 2 introduces writing credit lines on day 3, also after its practice day. Both then move to inquiry on day 4. Library APPROACH, section field 5, specifies teacher modeling, pair practice with the card, and withdrawal on the first inquiry day.

**Why it matters:** The frame omits the supported student tries between watching these new moves and using them in research. This particularly affects credit writing, which grade 2 checks independently.

**Exact fix:** Retain six sessions in each unit:

- Change Unit 1 day 3 to **show-me with practice**: after the model, pairs match three new questions to source kinds using the pictured card, explain their choices, and receive feedback.
- Change Unit 2 day 3 to **show-me with practice**: after the model, pairs write credit lines for two new covers using the card and correct them from feedback.
- State that the card is withdrawn on day 4 in both units.
- Update the Day kinds bullet to acknowledge these practice portions.

### 3. The year-end reflection needs individual sheets that have already gone home

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, finding 1 of the independent grade 1 frame read  
**Confidence:** firm

**Location:** [Evidence, line 76](S:/CurioClass/docs/courses/library-and-research-skills-grade-2/frame.md:76) and [year-end response, line 207](S:/CurioClass/docs/courses/library-and-research-skills-grade-2/frame.md:207).

**What is wrong:** Sheets go home after marking, and no individual record outlives its unit. Week 29 nevertheless requires each child to compare current knowledge with the know-and-wonder sheet from Unit 1. No retained classroom version or return route is specified.

**Why it matters:** The promised comparison cannot reliably run with the available materials.

**Exact fix:**

1. Add to Unit 1: “Keep an anonymous class know-and-wonder display, without names or individual scores, for the year-end reflection.”
2. Replace the year-end individual-sheet comparison with: “Each child compares one starting idea from the anonymous class display with what they know now.”
3. Add the display to the materials list.

This preserves the existing handling of individual sheets.

### 4. Several host tasks lack the promised progression-row references

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, finding 2 of the independent grade 1 read and the host-task traceability issue in library pre-work finding 9  
**Confidence:** firm

**Location:** [Host tasks, line 55](S:/CurioClass/docs/courses/library-and-research-skills-grade-2/frame.md:55), the Units table, and [the closing Cross-subject paragraph, line 251](S:/CurioClass/docs/courses/library-and-research-skills-grade-2/frame.md:251).

**What is wrong:** The frame promises host tasks named by progression row. Unit 1 gives topics and unit numbers without IDs. Unit 2 names ELA’s fossil unit without identifying its supported task. Unit 4’s alternative science host also lacks an ID.

**Why it matters:** The scope writer must infer which core work the library inquiry serves.

**Exact fix:** Retain the existing topics and add:

| Location | Host reference to insert |
|---|---|
| Unit 1, maps | `social-studies:ss2-map-parts`, using questions about what a map shows |
| Unit 1, water | `science:s2-water-where`, using the provided-source question about where water is found |
| Unit 2, fossils | `ela:e2-text-features`, finding a fossil book and locating facts within it |
| Unit 4, alternative science host | `science:s2-seed-pollinator-model`, using its question about animals spreading seeds or carrying pollen |

Repeat these references in the closing Cross-subject paragraph. Keep the stand-alone routes and scheduling fallbacks.

### 5. Completed progression work and available scheduling evidence are described as pending

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, finding 3 of the independent grade 1 read and earlier kindergarten stale-note findings  
**Confidence:** firm

**Location:** [Check set read, line 125](S:/CurioClass/docs/courses/library-and-research-skills-grade-2/frame.md:125), [calendar explanation, line 216](S:/CurioClass/docs/courses/library-and-research-skills-grade-2/frame.md:216), [Cross-subject, line 223](S:/CurioClass/docs/courses/library-and-research-skills-grade-2/frame.md:223), and [For the lead, line 258](S:/CurioClass/docs/courses/library-and-research-skills-grade-2/frame.md:258).

**What is wrong:**

- All four progression-note changes requested in For the lead item 1 already appear in `library.csv`, at lines 17, 18, 19 and 22.
- Cross-subject says lesson availability waits on the core scopes and sequences. Grade 2 ELA, science and social studies scopes and `days.csv` files already exist.
- The calendar explanation says every week from 28 onward has a core check. Week 30 does not.

**Why it matters:** These statements invite duplicate edits and unnecessarily restrict the later scheduling pass.

**Exact fix:**

1. Replace “Differences, each needing a row note” with “Differences, each recorded in its progression row note.”
2. Replace For the lead item 1 with: “**L103 row notes applied.** The four differences are recorded in `g2-question-to-research`, `g2-kinds-of-sources`, `g2-catalog-lookup` and `g2-fact-sort`.”
3. Replace the waiting clause with: “The core scopes and lesson-data files exist. Use their day placements when scheduling host tasks, retaining the ‘if later’ routes for local scheduling differences.”
4. Replace the blanket calendar claim with: “Weeks 28, 29, 31 and 32 hold core checks. Week 30 is free of core checks; using it would require revising this course’s contiguous weekly schedule.”

The fourth correction does not require changing the current 29-session allocation.

## Lens checklist at the frame layer

| Lens requirement | Result |
|---|---|
| A year of spaced inquiry, rather than orientation alone | Met: four complete inquiry units |
| Named grade priorities, each checked | Partly met: finding 1 completes the specified evidence |
| No duplicate ownership at the same depth | Met |
| Continuum placement and reasons for differences | Met in substance; finding 5 corrects their status |
| Library and social studies lateral-reading ownership distinguished | Met: formal lateral reading remains later library work |
| Skills attached to host tasks | Partly met: finding 4 supplies missing references |
| Source judgment avoids a page-appearance checklist | Met at this grade’s boundary |
| Questions guide source choice and finding | Met |
| Honest use accompanies research | Met: credits return across products, without shaming |
| Making, sharing and self-reflection | Present; findings 1 and 3 repair evidence and materials |
| AASL text copying or approval claims | None found |
| Live-page dependence | Not applicable: the course has a complete closed paper route |
| Paid database, library or device dependence | None |
| Product names in proposed instructional copy | None found |
| Unsupported claims of learning effects | None found |

## What is right and should be retained

Question and source-kind selection precede catalog finding and crediting; these precede comparison and sorting; the final poster gathers the year’s work. The progression handoffs are explicit and consistent.

The paper route is complete, same-year leans have workable fallbacks, and interview topics and substitutions respect the subject’s boundaries. The course-level checks revisit earlier learning without immediately scoring the just-ended unit again. Unit 3’s three carried skills share a case set, making six sessions defensible pending the unit-level time check.

## Settled by the expert

Recommendations for the caller to apply. No files were edited.

| Choice | Reason | File |
|---|---|---|
| Name the actual poster and spoken reflection as assessment evidence | Completes the existing research-sharing row | Grade 2 library frame |
| Add guided practice within Units 1 and 2 day 3 | Preserves fading support without adding sessions | Grade 2 library frame |
| Use an anonymous class display for the final comparison | Makes the reflection runnable | Grade 2 library frame |
| Insert the existing host-row IDs | Makes tasks traceable | Grade 2 library frame |
| Correct completed-work and calendar statements | Removes stale instructions and a factual overstatement | Grade 2 library frame |
| Retain four units and 29 sessions | Coverage, totals and current check placement support them | No allocation change |

## What I could not judge

The library student texts, assessment pages, rubrics and lesson plans do not yet exist. Their actual reading load, accessibility and administration time remain for later reads. The listed assessment totals fit arithmetically within 19 working minutes, but that is not evidence that their transitions, dictation and observation demands will fit in practice.

## Sources and evidence limits

- [AASL learner framework, second edition](https://standards.aasl.org/wp-content/uploads/2026/07/250918-AASL-framework-for-learners.pdf): checked the two owned competencies and boundaries of carried work.
- [AASL second-edition explanation](https://standards.aasl.org/2edition/): checked edition continuity.
- [NYC School Library System continuum overview](https://nycdoe.libguides.com/c.php?g=895467&p=7009946): checked the continuum’s grade-priority and cross-curricular purpose. Detailed grade 2 comparison used the stored band document named in the frame.
- [National Center for Missing and Exploited Children resources](https://www.missingkids.org/netsmartz/resources): confirmed the listed K to 2 presentation. The presentation itself was not read.
- [Monroe continuum guide](https://libguides.monroe.edu/ESIFC/Intro): **browser check**, unavailable through the web tool. It was not fetched another way; the NYC overview supplied an accessible institutional source.

No substantive finding rests on recalled outside research. The memory lookup supplied only prior frame-review context.

## For the source list

Record the accessible NYC continuum overview and the Monroe guide’s current browser-check status.

## For Cory

None. The proposed fixes preserve scope, audience, staffing and session allocations.


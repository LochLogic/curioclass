# Independent cold read: English Language Arts Grade 11

**Date:** 2026-11-15  
**Report destination:** `docs/reviews/sequence-english-language-arts-grade-11-2026-11-15.md`  
**Delivery:** Complete report inline. No files were changed.

## Verdict

The sequence has a coherent instructional arc and preserves the frame’s unit ownership, whole-work reading commitments, writing calendar, and grade 12 handoffs. It needs revision before unit planning because required book components are missing from the local copies, several assessment claims exceed their named evidence, and the shared research submission conflicts with history’s scoring day. Restore the required texts and close those task and calendar gaps while retaining the existing unit allocations.

**Finding count: 7.**

## What I read and checked

- `docs/agents/EXPERT.md`, the ELA lens, `docs/RUBRIC-ELA.md`, the foundation, relevant baseline rules, roadmap planning requirements, shared approach, ELA approach, and source-access and evidence notes.
- The complete Grade 11 scope and sequence, all 160 day rows, the course frame, and all 30 Grade 11 progression rows.
- The 26 declared Grade 10 ELA prerequisites against the current Grade 10 day map; the relevant mathematics progression rows.
- `docs/courses/CALENDAR.md` and Grade 11 calendar rows, with relevant US History I and Physics day records.
- All 42 Grade 11 entries in `data/plans/ela-texts.csv`; the local Douglass and Scarlet Letter copies and their metadata.
- The full local grades 11 to 12 standards, including lettered parts.
- Earlier Grade 11 frame reviews and relevant Grade 8, Grade 9, and US History I sequence findings for repeat classification.
- Outside standards, complexity guidance, review criteria, writing guidance, curriculum comparisons, and complete-edition contents, linked below.

The blind-rule exclusions were respected. Saved memory informed report structure only; no substantive finding rests solely on memory.

### Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Grade 11 reported zero sequence failures; the full run subsequently stopped because Python’s `markdown` module is missing. |
| `python -X utf8 scripts/frame.py calendar` | Passed; reported no stagger violation within its checked scope. |
| `python -X utf8 scripts/frame.py check english-language-arts-grade-11` | Passed: zero failures, 148 unit days plus 12 course-level days. |
| `python -X utf8 scripts/stale.py check` | Passed: 56 files, zero failures. |

The incomplete full gate does not withhold this verdict. No turn, defect-ledger, synchronization, or editing command was run.

## Findings, most serious first

### 1. Required portions of both long works are absent from the local copies

**Severity:** Serious  
**LAYER:** sequence  
**REPEAT:** yes, text availability and completeness extend Grade 11 independent frame finding 7  
**Confidence:** firm

**Location:** “Reading, writing and talk through the year”; days 82, 89, and 96 to 100; the corresponding text records.

**What is wrong:** The sequence assigns Douglass’s complete prefatory material and Appendix, and Hawthorne’s complete Custom-House introduction. However:

- `library/douglass-narrative/text.md` begins with Chapter I and ends with Chapter XI. It contains neither the prefatory documents nor the Appendix.
- `library/scarlet-letter/text.md` begins with Chapter I and contains the 24 novel chapters without The Custom-House.
- Both accompanying `story.json` files label the source part as `whole`.

The complete-edition contents confirm those missing components. [Douglass edition](https://www.gutenberg.org/files/23/23-h/23-h.htm), [Hawthorne edition](https://www.gutenberg.org/files/33/33-h/33-h.htm).

**Why it matters:** Day 89’s distinction between religious claims depends directly on the absent Appendix. The novel’s framing work and assigned reading also depend on unavailable material. A writer could follow the sequence and the “on file” labels while producing incomplete reading.

**Exact fix:** Supply checked, omission-disclosed copies of the missing components; correct the completeness metadata; and record their editions and locations. Retain their scheduled reading. Recalculate the affected reading assignments after restoration rather than substituting summaries.

### 2. Several assessment rows do not secure every demand they list

**Severity:** Serious  
**LAYER:** standard  
**REPEAT:** yes, Grade 8 sequence finding 2 and earlier Grade 11 partial-standard findings  
**Confidence:** firm on the missing specifications

**Location:** Days 33, 117, and 137.

**What is wrong:**

| Day | Listed demand | Evidence missing from the named task |
|---|---|---|
| 33 | `L.11-12.5a` | Interpreting hyperbole or paradox in context is named; explaining its role in the text is not. |
| 117 | `RL.11-12.5` | No structural analysis connecting a choice to overall structure, meaning, and aesthetic impact is named. |
| 117 | `RL.11-12.9` | A same-period excerpt is supplied, but no explicit comparison of how the pair treats a similar theme is specified. |
| 117 | `RI.11-12.2` | Literary theme diagrams and summary correction do not explicitly establish interacting nonfiction central ideas. |
| 137 | `SL.11-12.2` | Credibility and discrepancies are named, but source accuracy is not explicitly judged. |

These distinctions come from the standards’ actual performances, not additional expectations imposed by this review. [Official standards, reading, speaking/listening, and language sections](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf).

**Why it matters:** The sequence’s own assessment convention requires named evidence for every listed part. A busy writer could build the specified tasks and still record unsupported coverage.

**Exact fix:**

- Day 33: require a brief explanation of what the figure contributes to the author’s meaning or purpose.
- Day 117: remove `RL.11-12.5`, `RI.11-12.2`, and their corresponding skill claims from this sampled check. Their unit assessments remain intact.
- Day 117: retain `RL.11-12.9`, but explicitly require one evidence-supported comparison linking the two same-period texts’ treatment of a shared theme.
- Day 137: require an accuracy judgment for each source, identifying corroboration, a contradiction, or a limit on verification.

This narrows an overloaded cumulative check without cutting owned instruction or its unit assessment.

### 3. The single shared research paper is scored before ELA collects its final version

**Severity:** Serious  
**LAYER:** sequence  
**REPEAT:** yes, both earlier Grade 11 frame reviews identified the shared-calendar seam  
**Confidence:** firm

**Location:** Unit 4 milestone calendar, days 60, 65, 70, and 75; US History I day 71.

**What is wrong:** ELA’s final shared essay is due on day 75. History day 71 already says the reform paper is scored for historical reasoning. Earlier history milestones occur on days 56, 61, and 66, while ELA schedules completion on days 60, 65, and 70.

The weekly labels broadly agree, but the final-product instruction does not. The scope acknowledges the seam without supplying a runnable handoff.

**Why it matters:** Students could face two submissions or history could score an unfinished paper, defeating the promised single product.

**Exact fix:** Retain the authorized day 75 final submission. Specify one shared artifact and distinguish history’s earlier progress checkpoints from ELA’s completion deadlines. Replace history day 71’s final-paper scoring instruction with draft feedback and its existing assessment response; historical scoring of the final artifact follows day 75 without requiring another student product or another history teaching day.

The caller should reconcile the two records together. No unit resizing is needed.

### 4. Reading loads and text demand remain insufficiently documented to validate the allocations

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, Grade 11 frame finding 7 and Grade 9 sequence finding 1  
**Confidence:** firm on missing evidence; judgment call on eventual classroom fit

**Location:** Reading rationale, units 2, 5, 6, and 8; `data/plans/ela-texts.csv`.

**What is wrong:** Of 42 Grade 11 text records, 31 say the measure is not on file, and all 42 have blank rights-check fields. Numerous excerpt limits and lengths remain unspecified. The retained Dunbar poem has no Grade 11 record.

The scope says selections are specified in the record, but entries such as Riis’s chapters and the tenement testimony do not identify exact boundaries. It also defers actual load checking to unit planning after fixing the day allocations.

A concrete discrepancy is the novel: its local 24 chapters contain approximately **68,100 whitespace-separated words**, before restoring The Custom-House, while the planning estimate is about 63,000 words.

**Why it matters:** The rationale for rising demand is sensible, but it cannot substitute for selection-specific evidence. Complexity requires quantitative, qualitative, and reader/task considerations together. [Common Core Appendix A](https://www.oregon.gov/ode/educator-resources/standards/ELA/Documents/ela-appendix-a.pdf).

**Exact fix:** Complete a provisional load and complexity table before accepting the allocations:

- Exact edition, excerpt boundaries, word count or media duration, and source location.
- Appropriate measure with provenance, or a reason it is unsuitable.
- Qualitative demands, matching supports, task, and placement reason.
- Reading divided between class and the authorized home allowance.
- Concurrent writing, discussion, vocabulary, and feedback time.

Prioritize the restored book components, unit 2’s three complete texts, unit 8’s selections, and the retained Dunbar addition. Do not require computed measures for poems or drama.

### 5. Unit 4 does not place the seminar and teacher-led discussion it promises

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** new  
**Confidence:** firm on the day-map omission

**Location:** Year-long discussion promise; days 56 to 78.

**What is wrong:** The scope says every unit has an explicit seminar and a shorter teacher-led text discussion in its notes. Unit 4 names rehearsals, presentations, peer feedback, and a shorter evidence discussion on day 74, but no explicit full seminar or teacher-led hard-passage discussion.

**Why it matters:** Presenting findings and rehearsing a talk do not automatically provide the collaborative reasoning routine promised by the frame. The research unit is the year’s longest unit and should preserve that routine. Frequent evidence-based discussion is also part of the review criteria. [ELA criteria, indicators 2i and 2j](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_6_12_Review_Criteria_2_0_a3fc2b49ab.pdf).

**Exact fix:** Make day 62’s source comparison include a 15-minute student-led seminar on which sources can support a contested reform claim, with prepared evidence and written synthesis. Name a short teacher-led discussion of the model’s source integration on day 64. Keep both inside the existing source-evaluation and synthesis work, preserving the presentation rotations.

### 6. The shorter path lacks a defined period budget and drops a named discussion setting

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, Grade 8 sequence finding 6 and Grade 9 sequence finding 5  
**Confidence:** firm

**Location:** “Shorter path”; day 15; fold-in day 8.

**What is wrong:** The shorter-period route gives general priorities without naming a period length or reconciling explicit allocations. Day 15 alone specifies 45 minutes of reading, discussion, and synthesis before transitions.

All ten proposed fold-in days are unassessed, which is correct. However, folding day 8 preserves its alternate-ending task, vocabulary, and paragraph without explicitly preserving its teacher-led discussion. Unit 1 later relies on that discussion setting as evidence.

**Why it matters:** The shorter route could exceed the available period or lose an owned discussion dimension while claiming complete preservation.

**Exact fix:**

- Define a provisional **40-minute path** and budget its heaviest assessment windows.
- For day 15, use ten minutes reading, 18 minutes discussion, nine minutes synthesis, and three minutes transitions. Confirm the selected passage and task fit.
- Explicitly preserve day 8’s teacher-led exchange within day 7’s ending analysis.
- For each fold destination, identify the work it replaces and its retained minutes, especially days 62, 101, and 136.
- Retain every assessment, response slot, and required reading.

Keep the existing distinction between scattered lost meetings and a school year that actually ends earlier.

### 7. Current-status notes still direct unnecessary reconciliation

**Severity:** Low  
**LAYER:** process  
**REPEAT:** yes, Grade 8 sequence finding 8 and Grade 9 sequence finding 7  
**Confidence:** firm

**Location:** Prerequisite introduction and inventory; “For the lead” items 1 and 4; frame readiness wording.

**What is wrong:**

- Grade 10 ELA’s day map now exists. All 26 declared ELA prerequisites have mapped Grade 10 placements.
- Physics day 119 explicitly places its element-formation communication in week 24 as short in-class work, with no competing take-home process piece. The supposed unknown week 23 explanation deadline has been resolved in that record.
- The frame still directs first-day readiness on Grade 10 pickups, contradicting the sequence’s correctly placed retrieval.

**Why it matters:** Later writers could reopen settled work or restore prohibited first-day readiness checks.

**Exact fix:** Replace the blanket missing-Grade-10 caveat with verified planned placements. Retain the narrower mathematics uncertainty because Algebra I and Geometry day maps remain absent. Mark the Physics seam resolved from day 119, and update the frame’s readiness wording to match the governing retrieval rule.

Do not describe mapped planned teaching as evidence that students have actually received instruction.

## Required checks beyond the findings

### Order, assessments, and days by load

The general order is sound: evidence precedes sustained analysis; source evaluation precedes research drafting; complete reading precedes final literary conclusions; and interpretation teaching precedes its assessment.

| Unit | Total days | Teaching days, excluding Check and Respond | Load judgment |
|---|---:|---:|---|
| 1 | 16 | 13 | Reasonable for four texts and eight annual routines. |
| 2 | 18 | 15 | Plausible, subject to measured reading and publication budgets. |
| 3 | 21 | 16 | Substantial document set and argument; four assessment days are explicit. |
| 4 | 23 | 20 | Two inquiries, essay, and talk justify the allocation; fix the handoff. |
| 5 | 14 | 11 | Tightest whole-book run; restored components need counting. |
| 6 | 21 | 18 | Whole novel, framing text, comparisons, and literary argument justify substantial time. |
| 7 | 10 | 8 | Appropriate concentrated work on one owned reading row. |
| 8 | 8 | 6 | Plausible for one bounded set; exact selections remain necessary. |
| 9 | 17 | 13 | Plausible for complete short works, narrative production, and interpretation work. |

No clearly excessive allocation is established. Underallocation remains a risk requiring measurement in units 5 and 6, rather than a proved impossibility.

Every unit has an end-of-unit assessment and one response allocation. No unit exceeds 25 days, so none requires a mid-unit assessment under the brief. Five process pieces and three cold one-sitting pieces are placed. Recent products and conferences are generally reused appropriately.

### Readiness and retrieval

- **ELA:** All 26 declared prerequisites belong to Grade 10 and have current mapped placements there. Retrieval is appropriate; no unit incorrectly gives these rows an older-skill readiness check.
- **Mathematics:** Grade 10’s `geo-two-way-probability` explicitly applies the earlier two-way-table standard, but its day evidence remains unavailable. Unit 8’s conservative day 130 readiness reservation is candidly provisional.
- **Timing:** Day 130 immediately precedes unit 8’s day 131 hook. No readiness check is placed on a unit’s first day or weeks ahead.
- **Dramatic irony:** Grade 8 knowledge is expressly not assumed. Day 139 teaches it afresh before use.

### Course checks and calendar

Checks occupy weeks **16, 24, and 32**, matching the Grade 11 calendar. Shared week 32 finals are permitted.

Earlier-content transfer is explicit after units 6 and 9. Check 1 avoids repeating the just-ended research audit and formal presentation. Founding documents, reform context, slavery-resistance context, immigration, and Physics writing dependencies arrive first or have named bridges. The shared research artifact remains the exception in finding 3.

### Candidate cells

All ten check-set candidates are settled:

| Decision | Candidates |
|---|---|
| Kept with internal cost | Gothic and reliability, 15 minutes on day 12; annotated source list, 45 minutes across days 62 and 65; Dunbar, 15 minutes on day 128. |
| Dropped with reasons | Second Salem record, additional Emerson essay, Henry speech, Jacobs chapters, additional Hawthorne tale, Hine photographs, and Crane story. |

Both optional recent quotations are also explicitly dropped. The retained Dunbar addition still needs its record.

**Source map:** Not applicable. This course has no adaptable base curriculum.

### Lens checklist: scope and sequence

| Lens line | Result |
|---|---|
| Text demand climbs, or its ordering has a stated reason | **Met in rationale; verification incomplete.** Independence and integration increase, but text records remain insufficient. |
| Research and full-process writing recur | **Met.** Two inquiry cycles and five process pieces are scheduled. |
| Formal discussion occurs often | **Missed in unit 4’s explicit placement.** The remaining units provide frequent discussion. |
| K to 2 phonics and decodables align | **Not applicable.** |

This is not a completed rubric score.

## What should be preserved

Keep the unit order, full-work commitments, distinct writing purposes, source-based tasks, and explicit grade 12 limits. Preserve the historical bridges, omission disclosures, safe alternatives, scaffolded Grade 11 proficiency standard, individual digital-component records, and reuse of recent evidence.

The short research cycle followed by sustained inquiry is particularly useful. Models, practice, revision, and feedback should remain protected, consistent with the [secondary-writing practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/22).

## Settled by the expert

| Choice | Reason | Files affected when applied |
|---|---|---|
| Retain current unit allocations provisionally | No demonstrated need yet to transfer days | Scope; day map |
| Restore missing book components | Required reading must actually be available | Library copies, metadata, text records |
| Narrow day 117’s assessment claims | Preserve valid sampling and reduce unsupported coverage | Day map; check description |
| Retain day 75 as the shared final submission | Matches the authorized ELA milestone | ELA and history handoff records |
| Place unit 4 discussion on days 62 and 64 | Preserve annual routines within existing work | Day map |
| Define and budget a 40-minute path | Makes the shorter-period promise reviewable | Shorter-path section |
| Preserve day 8’s teacher-led exchange in day 7 | Prevents loss of a discussion setting | Fold table |
| Close Grade 10 and Physics availability notes | Current records resolve those uncertainties | Scope; frame |

## For Cory

- **Scope, only if measured loads require it:** Decide any transfer of days between units or change to a required reading commitment. No such transfer or cut is recommended without the completed load budget.

## Outside sources and limits

- [Official Common Core standards](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf): checked the applicable reading, writing, discussion, presentation, and language requirements.
- [Common Core Appendix A](https://www.oregon.gov/ode/educator-resources/standards/ELA/Documents/ela-appendix-a.pdf): checked the complexity model and progression toward independence.
- [ELA review criteria](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_6_12_Review_Criteria_2_0_a3fc2b49ab.pdf) and [evidence guide](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_6_12_Evidence_Guide_2_0_2068cea08f.pdf): consulted selected complexity, pacing, and discussion provisions.
- [Secondary-writing practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/22): consulted its recommendations on explicit strategy instruction and integrated reading and writing.
- [Fishtank Grade 11 pacing guide](https://www.fishtanklearning.org/curriculum/ela/11th-grade/pacing-guide/): comparison only. Its 60-minute lessons and additional reading allowance prevent direct day-count equivalence.
- [Louisiana unit progression](https://doe.louisiana.gov/docs/default-source/teacher-toolbox-resources/ela-guidebooks-unit-progressions.pdf): checked the published Grade 11 course comparison. Its detailed Scarlet Letter unit returned HTTP 403 and was not used as evidence.
- [Douglass complete-edition contents](https://www.gutenberg.org/files/23/23-h/23-h.htm) and [Hawthorne complete-edition contents](https://www.gutenberg.org/files/33/33-h/33-h.htm): verified the missing components.

Actual classroom timing, finished assessment quality, scoring reliability, complete rights clearance, and sensitivity-read completion remain unverified.

**For the source list:** Add the two complete-edition links, Grade 11 pacing guide, and Louisiana progression; these addresses were absent from `APPROACH-SOURCES.md`.

**Verdict:** Revise before unit planning.  
**Finding count:** 7.  
**Report path:** `docs/reviews/sequence-english-language-arts-grade-11-2026-11-15.md`, delivered inline, not written.


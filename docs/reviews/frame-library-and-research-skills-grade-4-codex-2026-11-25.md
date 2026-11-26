# Independent frame read: Library and Research Skills, grade 4

**Date:** November 25, 2026  
**Course:** `library-and-research-skills-grade-4`  
**Findings:** 6  
**Delivery:** Complete report here. No files changed.

## Verdict

The sequence, calendar and grade-to-grade handoffs are sound, but the frame needs targeted fixes before the scope and sequence is written. Its largest risk is that following the detailed unit instructions would leave part of an inquiry unfinished or collect insufficient evidence of an owned skill. Retain four units and 30 sessions, while repairing inquiry completion, assessment evidence, check-set coverage, the home alternative and contradictory or stale instructions.

## What I read and checked

- The frame-reading brief, applicable after-core frame-writing provisions, EXPERT, FOUNDATION, shared approach, production-path guidance and relevant recorded decisions.
- The library lens, STANDARD, APPROACH, subject adoption bar, and relevant pre-work, progression and frame reviews.
- The complete grade 4 frame, its `grade:4` selector in `course-list.csv`, its `frames.csv` entry and calendar rows.
- All nine selected progression rows, their preceding and receiving rows, and the neighboring grade 3 and grade 5 frames.
- The cited grade 4 core-course Units tables, calendar placements and existence of their lesson-data files; the grade 3 math graphing prerequisite.
- The stored 2019 continuum document named by the frame, including its grade 4 cells and bold priority skills.
- The outside sources linked below.

There is no base text or source-map requirement. This single-grade course does not require a Year column.

| Required check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check library-and-research-skills-grade-4` | One failure: plan-stage lesson CSVs do not exist. Course-filtered under repository instructions. |
| `python -X utf8 scripts/frame.py check library-and-research-skills-grade-4` | **0 failures:** four units, 30 sessions, 26 in units and four for course checks and response. |
| `python -X utf8 scripts/stale.py check` | Six failures, all in other courses. |

The aggregate gate wrapper was not run because it writes output and baselines; these limitations do not withhold the verdict.

Independent checks confirmed:

- All nine selected progression skills appear in exactly one unit.
- The nine owned IDs match the progression, across **eight** owner rows.
- All incoming and outgoing progression links are reciprocal.
- Sessions total `6 + 7 + 6 + 7 + 2 + 2 = 30`.
- Checks in weeks 14 and 29 avoid current grade 4 core check weeks.
- The health-check overlaps are accurately disclosed for the lead’s calendar pass.
- Same-year fallbacks prevent later core instruction from becoming an unmet prerequisite.

## Findings, most serious first

### 1. Unit 1 does not complete its promised inquiry cycle

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, grade 3 independent frame read, finding 2; kindergarten pilot’s inquiry repair  
**Confidence:** firm

**Location:** Frame, Inquiry arc bullet, lines 55 to 61; Unit 1, line 174.

**What is wrong:** Library APPROACH requires a complete inquiry cycle and a shared product in every unit. Unit 1’s inquiry day specifies a plan, searches, a partner reading the plan and a self-check. It never explicitly requires students to read a located source, judge its usefulness, use information to answer their question or share that answer. Its assessment likewise requests plans without explicitly requiring a record of carrying them out.

**Why it matters:** A writer can follow these instructions and produce a planning exercise without the research outcome that makes the planning useful. The [AASL learner framework](https://standards.aasl.org/wp-content/uploads/2026/07/250918-AASL-framework-for-learners.pdf) includes implementation within I.B.2.

**Exact fix:**

- Replace the inquiry-day description with:

  > Plan and search for one narrowed host question. Locate short answering passages through two printed source kinds, retrieve the earlier maker-and-purpose check, and record what each search actually found. Write a brief answer with its source credit, share it with a partner, then complete the self-check.

- Add the answering passages and an answer-and-credit box to the materials.
- In the assessment, require the student to execute the search plan on the supplied materials and record a located result from each kind. Score both the fit of the plan and evidence of its implementation.
- Update the Inquiry phases cell to include construct and express.

Use earlier-grade answering and credit routines as review. Keep independent category-making and formal lateral reading in their existing places.

### 2. Unit 3’s assessment substitutes written questions and dictation for interaction

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, the incomplete individual-performance evidence pattern in the library progression review and grade 3 independent read  
**Confidence:** firm

**Location:** Unit 3, line 176, end-of-unit evidence.

**What is wrong:** Students write open questions and record an answer the teacher reads aloud. This checks question construction and recording, but does not show each student asking someone a question, attending to that person’s perspective or responding thoughtfully. Those actions are part of the taught row and the intended II.D.2 outcome. The [AASL framework](https://standards.aasl.org/wp-content/uploads/2026/07/250918-AASL-framework-for-learners.pdf) distinguishes interest in others’ perspectives from merely recording information.

**Why it matters:** A student could meet the written rubric without demonstrating the interpersonal skill this unit owns.

**Exact fix:** Replace the dictated-answer component with a brief assessed exchange on a new, teacher-approved neutral topic:

> Each student asks an open question, accurately restates the partner’s answer and asks one relevant follow-up. The teacher records these three outcomes separately for each student. The written record supports the observation.

Retain the written explanation of the group’s investigation plan and the three planned questions. Budget approximately eight minutes for written work and eighteen minutes for observed exchanges, about seventy seconds per pair for fifteen pairs. Partners complete the written work while awaiting their observed exchange. Validate that allocation when the assessment materials are built.

### 3. Two grade 4 continuum priorities are only partly represented

**Severity:** Moderate  
**LAYER:** frame, progression  
**REPEAT:** yes, incomplete check-set substitutions in the grade 3 independent read, finding 4  
**Confidence:** likely

**Location:** Check set read, lines 103 to 116; Units 2 and 4, lines 175 and 177; corresponding progression notes.

**What is wrong:**

- The stored continuum’s grade 4 media-literacy priority asks students to evaluate **accuracy and purpose**. The frame records purpose sorting and finding an advertisement, but does not commit to checking accuracy.
- Its grade 4 revision priority includes assessing one’s own work against teacher-provided criteria. The frame commits to using others’ advice, while identifying product criteria remains a “Candidate” in Check set adds. The process self-check after sharing does not clearly supply product assessment before revision.

These are table 0, grade 4 cells, rows 49 and 32 of the stored band document.

**Why it matters:** Correctly identifying an informative purpose does not establish that a statement is accurate. Acting on advice also does not establish that a student can identify a needed change independently.

**Exact fix:**

- In Unit 2’s existing source practice, have students check one factual statement from an invented media page against a second supplied source and mark it supported, contradicted or unresolved. Include one fresh example in its assessment.
- In Unit 4, make the product rubric available before drafting. Before peer feedback, each student checks the draft against it and identifies one needed change.
- Record these treatments in the corresponding progression notes and Check set read account.

These are supported additions inside existing work. Formal lateral-reading ownership remains in grade 5.

### 4. Unit 3’s stand-alone question does not provide the promised home alternative

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** firm

**Location:** Host tasks bullet, lines 50 to 54; Unit 3, line 176.

**What is wrong:** The frame promises a stand-alone question with a closed source set that works at home. Unit 3 instead offers a class book-preference survey, schoolyard observation and questions to a classmate or school adult. Its listed materials are recording sheets, rather than an alternative source set. A single child and teaching adult cannot run the stated class survey.

**Why it matters:** The home teacher must invent participants, data or an alternative investigation.

**Exact fix:** Add this explicit branch:

> At home, the student and teaching adult co-design an observation using a supplied sequence of invented schoolyard pictures after rain: which pictured places remain wet longest? They decide what to record, collect observations from the sequence and tally the results. The student asks the adult three open questions about possible observation methods, records the answers and shares the finding.

Add the picture sequence and adult-response guidance to the materials. Apply the same plan, contribution, listening and recording criteria. Keep the classroom survey as an equal option.

### 5. Unit 4’s regrouped reteach has two conflicting locations

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, grades 1 to 12 library frame read, minor finding m1  
**Confidence:** firm

**Location:** Days bullet, lines 21 to 23; Unit 4, line 177; year-end respond description, line 184.

**What is wrong:** The Days bullet places Unit 4’s regrouped reteach in the year-end respond day. The unit table places it after the gallery on Unit 4 day 7. The year-end respond description provides no allocation for that additional job.

**Why it matters:** A writer cannot tell which session must preserve time for responding to Unit 4’s assessment results.

**Exact fix:** Keep the reteach where the unit table already places it:

> Unit 4 day 7: fifteen minutes for the gallery, ten minutes of regrouped reteach from the product and revision-assessment results, and four minutes for the self-check.

Rewrite the Days bullet to match. State that the year-end respond session addresses the cumulative check’s gaps and the year’s reflection.

This refines the earlier review: the current unit table already names a reteach, so the remaining defect is contradictory placement.

### 6. Completed work remains pending, and the owner-row count is wrong

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, grades 1 to 12 library frame read, M1; grade 3 independent read, finding 5  
**Confidence:** firm

**Location:** Days bullet, line 18; Cross-subject introduction, lines 194 to 196; For the lead, lines 229 to 248.

**What is wrong:**

- All five progression-note edits requested in For the lead item 1 already appear in `library.csv`.
- The named grade 4 core courses already have lesson-data files. Their availability does not still await the creation of scopes and sequences.
- All eight library frames now contain Check set read records, although the L103 instruction still identifies other grades as awaiting that work.
- There are eight owner rows containing nine owned IDs, not seven owner rows.

**Why it matters:** These instructions invite duplicate edits and obscure the reconciliation still needed.

**Exact fix:**

1. Change the count to “nine grade 4 rows, eight owner rows containing nine owned IDs.”
2. Replace item 1’s pending instructions with:

   > The five L103 progression-note changes are applied: g4-narrow-and-plan, g4-search-more-kinds, g4-evidence-notes, g4-honest-use and g4-own-question.

3. Replace the Cross-subject waiting clause with:

   > The cited core lesson-data files exist. Use their day placements when scheduling host tasks, retaining the “if later” routes for local scheduling differences.

4. Replace item 4 with:

   > Grade 4’s comparison and five row-note changes are recorded. Reconcile L103 against the comparison records now present in all eight library frames and identify only genuinely unfinished work.

Do not close L103 merely because comparison records exist, and do not rewrite dated review records.

## Lens checklist at the frame layer

| Lens requirement | Result |
|---|---|
| Spaced units across the year | Met |
| Complete inquiry cycle in every unit | Partly met, finding 1 |
| Named grade priorities, each checked | Partly met, findings 2 and 3 |
| Single ownership at the stated depth | Met |
| Earlier or later grade placements explained | Met |
| Library and social studies lateral-reading ownership distinguished | Met |
| Host tasks named | Met |
| Stand-alone alternatives | Partly met, finding 4 |
| Questions guide searching | Met |
| Source judgment avoids a page-appearance checklist | Met at the stated grade boundary; finding 3 repairs accuracy checking |
| Honest use accompanies research | Met |
| Making, sharing and reflection | Present; findings 1 and 3 repair omissions |
| Assessment requires doing the skill | Partly met, finding 2 |
| Competency copying or approval claims | None found |
| Live-page dependence without capture or substitution | None in the complete paper route |
| Paid database, library or device dependence | None |
| Product names in proposed instructional copy | None found |
| Unsupported claims of learning effects | None found |

## What is right and should be retained

The progression from planning to evidence, human investigation and independent inquiry is coherent. The heavier note-making unit receives seven sessions, and the final product has separate drafting, feedback and revision time.

Keep the reciprocal seams, neutral cases, printed materials, private correction of copying and explicit cross-subject fallbacks. Keep checks in weeks 14 and 29 pending the lead’s coordinated after-core calendar pass.

## Settled by the expert

Recommendations for the caller to apply. No files were edited.

| Choice | Reason | File |
|---|---|---|
| Complete Unit 1 with a sourced answer and partner share | Fulfills the existing full-cycle requirement | Grade 4 frame |
| Collect an observed question-and-response exchange | Demonstrates the existing interpersonal outcome | Grade 4 frame |
| Add supported accuracy checking and product self-assessment | Addresses the grade 4 check-set priorities | Grade 4 frame; progression notes |
| Supply an adult-and-child observation branch | Makes the existing home alternative runnable | Grade 4 frame |
| Put Unit 4’s regrouped reteach on its day 7 | Resolves conflicting instructions within existing time | Grade 4 frame |
| Correct pending-work notes and the owner-row count | Prevents duplicate work | Grade 4 frame |
| Retain four units and 30 sessions | Counts, load and calendar support them | No allocation change |

## What I could not judge

The actual library passages, assessment pages, scoring examples and lesson plans do not yet exist. Their reading load, accessibility, scoring consistency and administration time require later reads. The declared 29 working minutes are a planning limit, not demonstrated feasibility.

## Sources and evidence limits

- [AASL learner framework, second edition](https://standards.aasl.org/wp-content/uploads/2026/07/250918-AASL-framework-for-learners.pdf): checked the owned competencies and distinctions between planning, implementation and interpersonal evidence.
- [NYC School Library System continuum overview](https://nycdoe.libguides.com/c.php?g=895467&p=7009946): confirms the continuum’s grade-priority and cross-curricular purposes. Detailed comparison used the preexisting [stored 2019 band document](S:/CurioClass-sources/library/aasl-2026-11-21/esifc-3-5/esifc-priority-3-5.docx), read directly.
- [Digital Inquiry Group lateral-reading collection](https://cor.inquirygroup.org/curriculum/collections/teaching-lateral-reading/): checked the distinction between external source checking and trusting a page’s own presentation.
- [Online-safety resource listing](https://www.missingkids.org/netsmartz/resources): confirmed the named grades 3 to 5 presentation remains listed. Its complete kit was not reviewed.
- [Monroe continuum guide](https://libguides.monroe.edu/ESIFC): **browser check**, unavailable through the web tool. It was not fetched another way.

No substantive finding rests on recalled outside research. The memory lookup supplied only review-method context.

## For the source list

Record the Monroe guide’s browser-check status and distinguish its inaccessible live page from the stored band document actually inspected.

## For Cory

None. These fixes preserve course scope, audience, staffing, ownership and session allocations.


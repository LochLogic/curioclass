# Independent frame read: Library and Research Skills, grade 3

**Date:** November 25, 2026  
**Course:** `library-and-research-skills-grade-3`  
**Findings:** 5  
**Delivery:** Complete report here. No files changed.

## Verdict

The frame has a sound sequence, places all nine progression skills exactly once, and gives coherent handoffs between grades 2, 3 and 4. Its largest risk is that a writer could follow its detailed instructions while leaving an inquiry cycle incomplete or collecting insufficient evidence for an owned standard. Keep the four units and 30 sessions, but repair the gallery workload, inquiry steps, individual team evidence, check-set gaps and stale instructions before writing the scope and sequence.

## What I read and checked

- The frame-reading brief, applicable after-core frame-writing provisions, EXPERT, FOUNDATION, shared approach, production-path and relevant BASELINE rules.
- The library lens, STANDARD, APPROACH, subject adoption bar and relevant recorded decisions.
- The complete grade 3 frame, its `grade:3` selector in `course-list.csv`, its `frames.csv` entry and calendar rows.
- The selected progression rows, preceding and receiving rows, and neighboring grade 2 and grade 4 frames.
- Relevant grade 3 ELA, science and social studies Units tables, calendar placements and selected lesson-data entries.
- The stored continuum document named by the frame, including the grade 3 indicator cells and their bold priority skills.
- Relevant earlier library progression, pre-work and frame reviews.
- The outside sources linked below.

There is no base text or source-map requirement. This single-grade course does not need the band-course Year column.

| Required check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check library-and-research-skills-grade-3` | One failure: the plan-stage lesson CSVs do not exist. Course-filtered under repository instructions. |
| `python -X utf8 scripts/frame.py check library-and-research-skills-grade-3` | **0 failures:** four units, 30 sessions, 26 in units and four for course checks and response. |
| `python -X utf8 scripts/stale.py check` | Seven failures, all in other courses. |

The aggregate gate wrapper was not run because it writes files; these limitations do not withhold the frame verdict.

Independent checks confirmed:

- All nine selected skills appear in exactly one unit.
- The seven owned IDs match the progression.
- The grade 2 and grade 4 handoffs match the selected rows.
- Sessions total `5 + 7 + 6 + 8 + 2 + 2 = 30`.
- Checks in weeks 13 and 29 avoid grade 3 core check weeks.
- The week 29 health-check overlap is accurately disclosed for the lead’s calendar pass.
- Earlier-grade retrieval and same-year fallbacks prevent the named core-course leans from becoming unmet prerequisites.

## Findings, most serious first

### 1. The gallery workload is unbounded, and its new feedback move lacks guided practice

**Severity:** High  
**LAYER:** frame, progression  
**REPEAT:** yes for the missing guided practice, grade 2 independent frame read, finding 2; the workload problem is new  
**Confidence:** firm

**Location:** Grade 3 frame, Unit 4, line 171; `library.csv`, `g3-gallery-feedback`, line 32.

**What is wrong:** Both files say students leave two notes on each classmate’s product. With 30 individual products, that means 58 notes per child and 1,740 notes across the class. The gallery session has about 24 working minutes after its five-minute model. The same session moves directly from that model into independent feedback, without the supported pair practice specified by library APPROACH, section field 5.

**Why it matters:** Following the instructions literally makes the session impossible. Quietly reducing the assignment leaves the writer to invent its workload and teaching sequence.

**Exact fix:**

1. Replace “leave two notes on each” in both files with:

   > Each student reads one assigned classmate’s product and writes two notes: one thing learned, in their own words, and one specific, kind suggestion tied to the skill card. Assign partners so every product receives feedback.

2. Specify Unit 4 day 6 as:

   > Five-minute teacher model; six-minute pair practice on a sample product with the card and corrective feedback; twelve-minute independent response to the assigned product without the card; six minutes for collection and self-check.

3. Have the teacher screen the slips before day 7’s revision.

This produces 60 independent notes across the class and preserves both existing feedback targets. Those targets are consistent with the separate response and constructive-feedback competencies in the [AASL learner framework](https://standards.aasl.org/wp-content/uploads/2026/07/250918-AASL-framework-for-learners.pdf).

### 2. Unit 2’s detailed inquiry stops at finding a source

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** firm against the subject’s explicit requirement

**Location:** The course’s Units and Inquiry arc bullets; Unit 2, line 169; Models carried.

**What is wrong:** The frame and library APPROACH promise a complete inquiry cycle in every unit, with a shared product. Unit 2’s inquiry day specifies a search plan, catalog search, library-area lookup and self-check. It does not specify reading the found source, judging it, using information to answer the question or sharing that answer. Unit 1 also leaves its judge step implicit. The generic promise that every unit completes the cycle does not supply these missing actions.

**Why it matters:** A writer could build a search exercise without the research task that gives searching its purpose.

**Exact fix:**

- Add to Unit 2’s inquiry-day description:

  > Start with the student’s research question. Use the catalog to find a short source in the closed set, retrieve the grade 2 maker-and-purpose check, select one fact that answers the question, and record a brief answer with its credit line. Share the answer with a partner before the self-check.

- Add the answering passage and answer-and-credit box to Unit 2’s materials.
- In Unit 1, name the supported grade 2 maker-and-purpose check before using the supplied source.
- Make the other units’ returning steps explicit: Unit 3’s pair share communicates a brief answer from its notes; Unit 4’s fact-finding includes the promised short search-plan review.

Budget these short steps within the existing inquiry sessions. Retain the present ownership boundaries, with formal lateral reading remaining later library work.

### 3. The team assessment does not explicitly collect every student’s recognition of another learner’s contribution

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, the incomplete two-ID assessment pattern in the library progression review, finding 4  
**Confidence:** firm

**Location:** Unit 4, line 171; `library.csv`, `g3-research-team`, line 33.

**What is wrong:** The progression’s independent check requires each student to report a finding **and name what a teammate added**. The frame requires each member to report, but assigns recording contributions to one team recorder. Its assessment description never explicitly elicits the second action from every student.

**Why it matters:** The recorder’s sheet can establish whose contributions were recorded without establishing that every student recognizes another learner’s contribution. The [AASL framework](https://standards.aasl.org/wp-content/uploads/2026/07/250918-AASL-framework-for-learners.pdf) distinguishes contributing to discussion from articulating awareness of others’ contributions.

**Exact fix:** Replace the team-meeting assessment description with:

> During the observed meeting, each student reports one source-supported finding and names one useful contribution made by a teammate. The teacher records two separate results per student: reported a finding, and accurately named another learner’s contribution. The recorder’s sheet supports the observation but does not substitute for either individual response.

Use brief turns within the existing four-minute team window.

The earlier progression review found this row’s two-part check adequate. This finding concerns the frame’s incomplete transfer of that already adequate requirement.

### 4. Two check-set substitutions do not fully address the priority skills they claim to cover

**Severity:** Moderate  
**LAYER:** frame, progression  
**REPEAT:** new  
**Confidence:** likely

**Location:** Check set read, lines 98 onward; Units 2 and 3, lines 169 and 170; corresponding progression notes.

**What is wrong:**

- The continuum’s grade 3 cybersafety priority includes password strength. The frame substitutes keeping a password private. Its reference to computer science grade 4 does not close the gap: `g4-authn-authz` teaches the distinction between identity checks and permissions.
- The continuum also asks students to begin recognizing perspective and opinion within nonfiction. Checking a factual statement in another source does not by itself teach that distinction.

These differences are visible in the stored grade 3 continuum cells, table 0, rows 65 and 19.

**Why it matters:** Students can complete the proposed activities without learning that a private password may still be easy to guess, or that nonfiction can contain opinion and selective emphasis.

**Exact fix:**

- In Unit 2’s existing scenario practice and assessment, include a paper case in which students distinguish an easily guessed invented password from a harder-to-guess invented option and explain why an adult should help protect it. Use no real credentials or personal details.
- In Unit 3’s existing source practice, use two short, neutral nonfiction accounts of the same weather event. With help, students distinguish a checkable statement from an opinion and notice that accounts can emphasize different facts. Then check one factual statement against another source.
- Record both treatments in the corresponding progression notes and revise the Check set read account.

These are supported introductions inside the existing safety and source-judgment work. They do not transfer later-grade ownership.

### 5. Completed work remains described as pending, and Unit 4’s ownership count is wrong

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, grade 2 independent frame read, finding 5  
**Confidence:** firm

**Location:** Days bullet, lines 16 to 18; Check set read; Cross-subject, lines 188 to 190; For the lead, lines 222 to 244.

**What is wrong:**

- All five progression-note changes requested in For the lead item 1 already appear in `library.csv`, lines 26, 27, 28, 31 and 34.
- Grade 3 ELA, science and social studies already have scopes and lesson-data files. Their availability does not still wait on those files.
- The L103 note lists other grades as awaiting comparison although their frames now contain comparison records.
- Unit 4 has three owner rows containing **five** owned IDs, not four.

**Why it matters:** These instructions invite duplicate work and obscure which reconciliation remains necessary.

**Exact fix:**

1. Replace the pending row-change language with:

   > The five L103 progression-note changes are applied in the selected grade 3 rows.

2. Replace For the lead item 1’s edit instructions with that status and the five affected row IDs.
3. Replace the Cross-subject waiting clause with:

   > The core scopes and lesson-data files exist. Use their day placements when scheduling host tasks, retaining the “if later” routes for local scheduling differences.

4. Replace item 4 with:

   > Grade 3’s comparison and five row-note changes are recorded. Reconcile L103 against the comparison records now present in the other library frames and identify only genuinely unfinished work.

5. Change Unit 4’s load description to “four rows, three owner rows containing five owned IDs.”

Do not rewrite the dated review records.

## Lens checklist at the frame layer

| Lens requirement | Result |
|---|---|
| Spaced units across the year | Met |
| A complete inquiry cycle in every unit | Partly met, finding 2 |
| Named grade priorities, each checked | Partly met, findings 3 and 4 |
| No duplicate ownership at the same depth | Met |
| Earlier or later grade placements explained | Met |
| Library and social studies lateral-reading ownership distinguished | Met |
| Host tasks named, with independent alternatives | Met |
| Questions guide searching and revision | Met |
| Source judgment avoids a page-appearance checklist | Met at the stated grade boundary; finding 4 repairs a check-set gap |
| Honest use accompanies research | Met |
| Making, sharing, feedback and reflection | Present; finding 1 repairs implementation |
| Assessment requires doing the skill | Met in form; finding 3 repairs individual evidence |
| Competency copying or approval claims | None found |
| Live-page dependence without capture or substitution | Not applicable to the complete closed paper route |
| Paid database, library or device dependence | None |
| Product names in proposed instructional copy | None found |
| Unsupported claims of learning effects | None found |

## What is right and should be retained

The question-to-search-to-notes-to-product sequence is coherent. The progression’s previously settled boundary between supported grade 3 note boxes and independent grade 4 categories is preserved.

The paper materials, neutral cases, stand-alone hosts, privacy rules and private correction of copying are useful commitments. Check placement is sound against the current calendar. No unit-to-unit transfer of standards or increase in course sessions is needed.

## Settled by the expert

Recommendations for the caller to apply. No files were edited.

| Choice | Reason | File |
|---|---|---|
| Assign one product per student for two feedback notes | Makes the gallery bounded and reciprocal | Grade 3 frame; `library.csv` |
| Add supported feedback practice within day 6 | Completes the stated fading sequence | Grade 3 frame |
| Name the missing inquiry actions | Makes the full-cycle promise buildable | Grade 3 frame |
| Record both team outcomes individually | Completes the existing owned row | Grade 3 frame |
| Use invented safety cases and supported nonfiction comparisons | Addresses the check-set differences within existing work | Grade 3 frame; progression notes |
| Correct completed-work notes and the five-ID count | Prevents duplicate edits and misleading status | Grade 3 frame |
| Retain four units and 30 sessions | Totals and core-check placement support them | No allocation change |

## What I could not judge

The actual library passages, assessment pages, rubrics and lesson plans do not yet exist. Their reading load, accessibility, scoring consistency and administration time require later reads. The declared 29 working minutes provide a planning limit, not evidence that the eventual materials fit it.

## Sources and evidence limits

- [AASL learner framework, second edition](https://standards.aasl.org/wp-content/uploads/2026/07/250918-AASL-framework-for-learners.pdf): checked the owned competencies and assessment distinctions.
- [AASL second-edition explanation](https://standards.aasl.org/2edition/): checked continuity of the framework.
- [NYC School Library System continuum overview](https://nycdoe.libguides.com/c.php?g=895467&p=7009946): confirms the continuum’s grade-priority and cross-curricular purpose. Detailed comparison used the stored 2019 band document named by the frame.
- [Online-safety resources](https://www.missingkids.org/netsmartz/resources) and [2016 grades 3 to 5 presenter guide](https://cdn.netsmartz.org/presentersguides/Grades_3_5_Presenters_Guide_2016.pdf): checked the listing, overview and adult-reporting instructions. The complete presentation kit was not reviewed.
- [Monroe continuum guide](https://libguides.monroe.edu/ESIFC): **browser check**, unavailable through the web tool. It was not fetched another way.

No substantive finding rests on recalled outside research. The memory lookup supplied only review-method context.

## For the source list

Record the accessible presenter-guide PDF and the Monroe guide’s current browser-check status.

## For Cory

None. These fixes preserve course scope, audience, staffing and session allocations.


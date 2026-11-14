# English Language Arts Grade 6: independent frame review

**Intended report path:** `docs/reviews/frame-english-language-arts-grade-6-2026-11-14.md`  
**Delivery:** Complete report supplied here. No report file was created.

## Verdict

The six-unit structure is coherent, but the frame needs revision before baselining, and the repository-wide prerequisite check remains incomplete. The biggest curricular risk is that proposed texts and broad complexity targets are carrying decisions that require actual anchor texts and individual text records. Secure those anchors first, then restore recurring research and make the remaining standards requirements explicit within their existing units.

## What I read and checked

Read:

- `docs/agents/EXPERT.md`, the ELA lens and `docs/RUBRIC-ELA.md`.
- `docs/FOUNDATION.md`, the relevant roadmap sections, shared and ELA approaches, glossary, source register, and relevant baseline decisions.
- The complete Grade 6 frame and its `frames.csv` row.
- All 29 Grade 6 progression rows, with adjacent-grade ownership and handoffs.
- The complete Grade 5 and Grade 7 frames.
- Relevant unit and calendar information in the Grade 6 mathematics, science and social studies frames.
- Earlier ELA scope and sequence, rubric, progression and correction reports, plus relevant frame reviews for repeat classification.
- Outside standards, review criteria, research guidance and curriculum maps linked below.

Grade 6 has no base curriculum. `data/plans/english-language-arts-grade-6/source-map.csv` is absent, but a source map is **not applicable** under the source register.

### Check results

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Could not complete: `ModuleNotFoundError: No module named 'markdown'` |
| Existing alternative Python launcher | Could not launch its Python child process: permission denied |
| `python -B -X utf8 scripts/plan.py check english-language-arts-grade-6` | Passed: 0 failures; no item or wrong-answer records |
| `python -B -X utf8 scripts/frame.py check english-language-arts-grade-6` | Passed: 0 failures; 148 unit days and 12 course-level days |
| `python -X utf8 scripts/stale.py check` | Passed: 56 files, 0 failures |

The targeted checks do not replace the required repository-wide result. The curricular observations below are provisional pending that result.

## Findings, most serious first

### 1. The prerequisite repository-wide check remains incomplete

**Severity:** Blocking verification issue  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

**Location:** `scripts/lesson.py:15`, reached through `scripts/plan.py check`.

The available default Python lacks `markdown`, so the required command terminates before completing. The alternative launcher also cannot run. This is an environment failure, not evidence of a defect in the Grade 6 curriculum.

**Why it matters:** EXPERT.md requires the plan check before curricular clearance. Passing the narrower course and frame checks establishes useful facts but does not establish that prerequisite.

**Exact fix:** Configure the review runner to use an existing, permitted Python environment with the required dependencies, rerun the exact repository-wide command, and attach its completed result before this review is cleared. If it reports plan failures, return those to the writer before further clearance.

The same unresolved environment problem appears in `docs/reviews/frame-science-grade-6-codex-2026-11-14.md`, finding 1.

### 2. The anchor-text requirement is deferred beyond the frame

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes  
**Confidence:** firm

**Location:** Grade 6 frame, “Reading level,” all six text-set cells, and “For the lead,” item 3.

The original novella, poems, play, stories and articles are commissions described in the frame, rather than linked texts available for inspection. Agency materials are mostly identified by organization and subject rather than exact title, edition, passage and location. No course text-record file exists.

Consequently, the band target, proposed word counts and general support rule cannot establish the difficulty or placement of individual anchors. The ELA lens explicitly requires anchors on file with their measures, qualitative analyses and placement reasons. The [grades 6 to 12 criteria, indicator 2b](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_6_12_Review_Criteria_2_0_a3fc2b49ab.pdf), also requires documented complexity evidence.

**Why it matters:** A writer cannot reliably plan reading time, questions or supports from a plot description. The frame's largest instructional commitments remain untested.

**Exact fix:** Before baselining the frame:

1. Give each anchor a stable identifier and an exact text or passage location.
2. Put the original anchor drafts on file.
3. Record the quantitative measure where applicable, qualitative demands, reader and task considerations, and reason for placement.
4. Identify the associated supports and rights status.
5. Count the informational and literary balance from those designated anchors.

Until then, describe these as proposed text commissions and complexity targets.

This repeats the unresolved text-readiness problem in `ela-6-spine-2026-11-11.md`, findings 1 and 6. The contemporary-text direction is an improvement; the missing evidence remains.

### 3. One research project does not fulfill the progression's recurring research commitment

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** firm

**Location:** “Days,” unit 3, unit 6, and `e6-short-research.notes`.

The frame explicitly promises **one research project**. The owning progression row requires **two or three short projects** across the year.

Unit 6 reuses sources for an argument, but it does not explicitly require another inquiry, source gathering, credibility judgments, notes or bibliography. A supplied-source writing task does not automatically establish a second research cycle. The [evidence guide, indicator 2t](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_6_12_Evidence_Guide_2_0_2068cea08f.pdf), separately examines repeated opportunities to apply research skills.

**Why it matters:** Students can complete the frame as written after encountering the research routine only once. Grade 7 then receives less practice than the progression promises.

**Exact fix:** Keep ownership in unit 3 and explicitly add a second application in unit 6. Develop the existing flood-wall task into a short inquiry with:

- A focused question and an opportunity to refocus it.
- Several print and digital sources.
- Credibility judgments.
- Quoted or paraphrased notes and basic bibliographic information.
- Findings used in the existing argument and talk.

Budget this within unit 6's 20 days and update the course summary to two projects. Do not add Grade 7 search-term or citation-format requirements.

### 4. Two older texts are ambiguously treated as anchors despite the stated policy

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes  
**Confidence:** firm

**Location:** “Base text,” “Reading level,” and units 2 and 6.

The frame says older public-domain texts appear only as paired or optional readings. Its reading-level paragraph nevertheless names the Hammurabi translation and Cline's 1900 report among the year's harder anchors. Their unit cells do not clearly distinguish them from the principal anchors.

**Why it matters:** A busy writer could build these units around older texts, contradicting both the frame's own rule and BASELINE rule 29.

**Exact fix:** Explicitly designate:

- Unit 2's original feature articles and editorials as anchors; King's translation as a paired primary-source selection.
- Unit 6's recent warning explainers and original profile as anchors; Cline's report as a paired historical account.

Remove the translation and report from the sentence describing anchor complexity. Record their separate demands and supports as paired readings.

This repeats the older-anchor concern in `ela-6-spine-2026-11-11.md`, finding 1. It does not require removing either historical source.

### 5. Digital publishing is not assigned a concrete performance

**Severity:** Serious  
**LAYER:** standard  
**REPEAT:** yes  
**Confidence:** likely

**Location:** Unit 1, subsequent typing commitments, and “Paper path and no accounts.”

The frame specifies typing, increasing page counts and peer comments. It does not explicitly assign students to publish a completed piece using technology, including the Internet. That is a distinct component of [W.6.6, printed page 43](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf).

**Why it matters:** A class could complete every named digital task while leaving part of the claimed standard unfinished.

**Exact fix:** Add to the existing process-writing sequence:

> Students produce and publish a completed piece through a school-managed digital route and exchange comments that lead to a revision. Curio Class requires no student account and hosts no student work. If the class cannot complete a digital component, record that component of W.6.6 as unfinished.

Name the publication step in a unit, rather than leaving it implicit in `e6-produce-publish`.

The paper-path caveat is already honest and should remain. The repeat is incomplete performance inside a claimed standard, also identified in the earlier ELA scope-and-sequence review, finding 5.

### 6. L.6.1e is narrowed to register choice

**Severity:** Serious  
**LAYER:** standard  
**REPEAT:** yes  
**Confidence:** likely

**Location:** Unit 1, the L.6.1e description.

The frame describes choosing the standard form for the setting and respecting home languages and dialects. It does not explicitly require students to recognize variations in their own and others' writing and speech, then identify and use strategies to improve conventional expression. Those actions belong to [L.6.1e, printed page 52](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf).

**Why it matters:** Respectful comparison can be taught without students learning the required revision strategies.

**Exact fix:** Expand the existing unit 1 commitment:

> Students identify variations in examples of their own and others' writing and speech, explain which forms fit a named context, and use a model, reference or revision checklist to revise selected examples into conventional English. Home languages and dialects remain respected.

Include written and spoken examples in the unit's checks. Keep this work inside `e6-pronouns`; no standard moves.

This is the same kind of incomplete-standard finding as the earlier ELA review's finding 5.

### 7. The progression still calls the dash decision open

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

**Location:** `data/progressions/ela.csv:207`, `e6-punctuation-spelling.notes`.

The note says that showing dashes beside the house style is “an open question with the lead.” Cory settled it in `docs/agents/decisions/DESK-ANSWERS.md:930`, and Grade 6 unit 4 already follows the decision.

**Why it matters:** The note can reopen a completed decision or cause a writer to omit required punctuation instruction.

**Exact replacement:**

> Teacher note: Cory settled this on 2026-11-13. Teach dashes as required by L.6.2a. Dashes may appear inside exercise sentences and texts students read; Curio Class's surrounding prose remains free of em dashes.

The marked-note checker passes because this is an unmarked stale statement. Similar stale-decision findings occur in the earlier social studies frame reviews.

## Ownership, standards, order and days

### Skill placement and workload

All 29 owned skills occur exactly once in the Skills column. No foreign-grade skill is assigned ownership.

| Unit | Days | Owned rows | Workload judgment |
|---|---:|---:|---|
| 1. River town | 32 | 10 | Plausible for the whole novella, first process piece and year-long routines; actual texts must confirm it |
| 2. Written laws | 26 | 5 | Plausible for source comparison, argument analysis and process writing |
| 3. Forecasting | 24 | 3 | Substantial load despite few rows: research, report and presentations |
| 4. Writing systems | 22 | 4 | Plausible for extended nonfiction, structure, vocabulary and conventions |
| 5. Storm voices | 24 | 5 | Plausible for poetry, drama, performance and comparison |
| 6. Warnings | 20 | 2 | Includes substantial returning work: two pieces, a talk and media integration; explicitly budget the second research application |
| Course-level checks and response | 12 | — | Three two-day checks, each followed by two respond days |
| **Total** | **160** | **29** | Fits the repository's teaching-year allowance |

No unit is demonstrably far over or under its share. Row counts alone would misrepresent the writing and presentation loads.

### Standards in full

The mapping covers all **41 parent standards** across RL, RI, W, SL and L. `L.6.5b` is additionally identified as a separately placed part, not a forty-second parent standard.

The explicit instructional descriptions broadly preserve the standards' grade-level demands. Findings 5 and 6 identify the remaining performance gaps. Finding 2 prevents verification of actual reading complexity, and finding 3 identifies reduced research recurrence.

### Unit reasons and prerequisite order

The order holds:

- Shared reading establishes evidence, summary, discussion and revision.
- Argument analysis precedes the full argument.
- Citing and summary precede research.
- Informative writing precedes its later applications.
- Weather knowledge precedes the storm literature.
- Media integration and historical accounts close the hazards thread.

The named models have plausible incoming sources and later uses. I found no clear case of a model required before its stated introduction.

### Seams

Grade 5's quotation, narrative, discussion, research, word-reading and water-topic handoffs are picked up. Grade 7's frame explicitly receives the Grade 6 evidence, point-of-view, research, argument and language work.

The principal weakness is the amount of research practice handed forward, covered by finding 3. The shorter Grade 6 novella is not itself a progression defect: length alone does not establish complexity.

### Cross-subject availability

| Connection | Current-frame comparison |
|---|---|
| Babylon and law codes | Social studies unit 4 overlaps ELA unit 2. ELA supplies its own background, so prior completion is not assumed |
| Writing systems | Social studies unit 6 finishes before ELA unit 4 |
| Research | ELA unit 3 precedes social studies unit 8 |
| Weather | Science unit 3 overlaps ELA unit 3. ELA explicitly supplies the needed explanations |
| Hazards | Science unit 5 precedes ELA unit 6 under the stated calendars |
| Histograms | Mathematics unit 8 begins after ELA unit 6 starts. The ELA fallback to familiar displays is necessary and explicitly provided |
| Comparing accounts | ELA's late introduction overlaps the approach to social studies unit 11; social studies already teaches its own comparison routine in unit 2 |

These are workable bridges. Later plans must preserve them rather than assume simultaneous unit numbers mean simultaneous instruction.

## ELA lens checklist: course frame

| Checklist line | Disposition | Evidence |
|---|---|---|
| Units use specific topics and texts rather than isolated skills or broad themes | **Met** | Six identifiable topic sets |
| Anchors are on file with measures, qualitative reasons and placement reasons | **Missed** | Finding 2 |
| Texts avoid leaning to one era, tradition or kind | **Missed as verifiable evidence** | The proposed mix is broader, but actual selections and authorship cannot yet be inspected; findings 2 and 4 |
| A long text is read whole | **Met as a frame commitment** | Unit 1 specifies a complete 12-chapter novella; its execution remains subject to finding 2 |

The scope-and-sequence, unit and day checklists are not applicable to scoring this frame. Question percentages, actual scaffolds and lesson execution require those later artifacts.

## Settled by the expert

These are recommendations for the caller to apply. No edits were made.

| Choice | Reason | File affected |
|---|---|---|
| Retain the six-unit order and 160-day total | No demonstrated sequencing or allocation defect requires restructuring | Grade 6 frame |
| Keep research ownership in unit 3; make unit 6 an explicit second application | Restores the existing progression commitment without moving ownership | Grade 6 frame |
| Label the translation and Cline report as paired historical sources | Resolves the anchor-policy contradiction within the existing text sets | Grade 6 frame |
| Make publishing and L.6.1e performances explicit in their current units | Completes existing claims without moving standards | Grade 6 frame |
| Replace the open dash question with the settled wording | The decision already exists | `data/progressions/ela.csv` |
| Withhold final clearance pending the global check | Targeted passes do not establish the prerequisite result | Review status |

## What is right and should remain

- The whole shared novella and evidence-writing routine.
- Argument analysis before extended argument writing.
- Specific knowledge threads connecting the units and adjacent grades.
- Formal discussion at least every two weeks.
- Sentence work inside reading and revision.
- Explicit paper-path limits for digital standards.
- Cross-subject bridges and concrete sensitivity notes.

## What I could not judge

Actual anchor quality, complexity, representation, rights clearance, reading load, question dependence, scoring reliability and classroom timing remain unverified. The original texts and course text records are needed for those judgments.

The repository-wide check also remains incomplete. Nothing here establishes readiness to teach or publish the course.

## Outside sources and memory

- [Common Core ELA standards](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf): checked Grade 6 requirements and adjacent-grade distinctions.
- [Appendix A](https://www.oregon.gov/ode/educator-resources/standards/ELA/Documents/ela-appendix-a.pdf): checked the three-part complexity model.
- [Grades 6 to 12 review criteria](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_6_12_Review_Criteria_2_0_a3fc2b49ab.pdf): checked text records and frame-relevant expectations.
- [Grades 6 to 12 evidence guide](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_6_12_Evidence_Guide_2_0_2068cea08f.pdf): checked recurring research and digital writing opportunities.
- [WWC secondary writing guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/22): checked support for explicit writing instruction and integration with reading.
- [EL Education Grade 6 curriculum map](https://eleducation.org/documents/1375/CurriculumTools_CurriculumMap-Grade6_0220.pdf): reference comparison for named texts, connected topics and recurring research.
- [Core Knowledge Grade 6 scope and sequence](https://www.coreknowledge.org/wp-content/uploads/2026/01/CKLA_G6_ScopeAndSequence.pdf): reference comparison for annual text and skill organization.

No curricular finding rests on personal or saved memory. Prior findings were checked in current repository files.

**For the source list:** The current publisher-hosted curriculum-map addresses above were reachable during this read.

## For Cory

- Confirm the audience assumption of a daily 50-minute lesson plus independent reading at home on four nights.
- Assign the qualified readers and any budget for original texts, Korean language and culture, and applicable hard-history content.

**Verdict:** Revise before baselining; clearance remains provisional.  
**Finding count:** 7, comprising 1 verification blocker and 6 curricular or documentation findings.  
**Report path:** `docs/reviews/frame-english-language-arts-grade-6-2026-11-14.md`, delivered above, not written.
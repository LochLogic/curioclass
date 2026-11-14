# Independent cold read: English Language Arts Grade 11

**Date:** 2026-11-14  
**Requested report path:** `docs/reviews/frame-english-language-arts-grade-11-2026-11-14.md`  
**Delivery:** Complete report below. No file was written.

## Verdict

The frame has a defensible course structure, places all 30 grade 11 progression skills once, and reserves adequate course-level assessment and respond time. It needs revision before the scope and sequence is built because several instructions would produce incomplete standards work, inappropriate assessment demands, or material that conflicts with repository rules. Correct those instructions and reconcile the shared research calendar first, while preserving the whole-book reading and the explicit grade 10 to grade 12 progression.

**Finding count: 11.**

## What I read and checked

- `docs/agents/EXPERT.md`, the ELA lens, `docs/RUBRIC-ELA.md`, `docs/FOUNDATION.md`, the relevant baseline rules, glossary, roadmap planning requirements, shared approach, ELA approach, and ELA source-access and evidence notes.
- The complete grade 11 frame, its `frames.csv` row, and all 30 grade 11 ELA progression rows, including prerequisites, handoffs, models, vocabulary, cross-subject references and notes.
- The grade 10 and grade 12 ELA frames and the progression records needed to check their seams.
- The complete 11 to 12 ELA standards, including lettered parts.
- The relevant US History I frame and progression records, Algebra I’s two-way-table placement, and Physics’ receiving writing dependencies. I also checked the Chemistry frame when investigating the grade 10 frame’s outstanding note.
- Earlier ELA progression reviews, their reconciliation and fix records, the earlier grade 6 ELA course review, and the US History I reviews and subsequent frame-fix record.
- `docs/sources/BASE-TEXTS.md` and the presence of relevant Reading Room texts.

Outside reading included the official standards, text-complexity supplement, current review criteria and selected evidence-guide sections, two published grade 11 curriculum references, the secondary-writing practice guide, and the text of *Trifles*. Links and reading limits appear below.

No substantive finding rests solely on memory. Saved memory informed report-format conventions only.

### Checks

| Command | Observed result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Stopped before completing: `ModuleNotFoundError: No module named 'markdown'` |
| `python -X utf8 scripts/frame.py check english-language-arts-grade-11` | 0 failures; 9 units, 160 days, including 12 course-level check and respond days |
| `python -X utf8 scripts/progression.py check ela` | 374 rows, 0 failures |
| `python -X utf8 scripts/stale.py check` | 56 files, 0 failures |

The full plan gate remains **unverified**. Its interruption was an environment dependency error, not a reported curriculum failure. The direct checks establish structural placement and totals, not instructional completeness.

No defect-ledger entries were written because this review is read-only.

## Findings, most serious first

### 1. Three units give print instructions that conflict with the no-slurs rule

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, US History I independent review, finding 3  
**Confidence:** firm

**Location:** Grade 11 frame, unit 3’s sensitive-topic instruction, unit 5’s Douglass print-copy instruction, and unit 8’s Riis print-copy instruction.

**What is wrong:** Unit 3 directs the Declaration’s phrase about Native peoples to be “read in full.” Units 5 and 8 say slurs are marked in the print copy and not read aloud. Marking a printed slur does not satisfy BASELINE rule 6, which prohibits slurs. The current US History I frame already uses a different instruction: analyze the grievance without printing or requiring students to speak the slur.

**Why it matters:** A writer following this frame could produce prohibited student material. The claimed shared wording with history is also inaccurate.

**Exact fix:**

- Replace unit 3’s instruction with: “Explain that the Declaration includes a dehumanizing description of Native peoples. Analyze the grievance and its political purpose without printing the slur or requiring students to speak it. Pair the analysis with Native-authored accounts of the conflict.”
- In units 5 and 8, replace “marked in the print copy” with an explicit omission marker and a short editorial explanation.
- Describe the resulting editions as complete readings with identified language omissions. Preserve the surrounding argument and disclose every omission.

This changes presentation within the existing scope.

### 2. Paper alternatives lack an honest boundary around digital requirements

**Severity:** Major  
**LAYER:** standard  
**REPEAT:** yes, ELA progression independent review, F3  
**Confidence:** firm

**Location:** “Paper path and accounts”; units 2 and 3, publishing; unit 4, presentation; corresponding `e11-process` and `e11-presentation` notes.

**What is wrong:** A posted paper copy substitutes for publishing and updating with technology. The presentation permits “slides or a handout” without distinguishing what each demonstrates. W.11-12.6 and SL.11-12.5 contain digital performances that paper alone cannot demonstrate. The adjacent grade 10 frame already makes this distinction explicitly. [Official ELA standards, printed pages 46 and 50](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf).

**Why it matters:** A teacher could complete the offered route and record the digital component as taught or demonstrated when it remains unfinished.

**Exact fix:** Add this completion boundary to the frame and relevant progression notes:

> Paper alternatives preserve the reading, writing and presentation work. They do not demonstrate W.11-12.6’s technology requirement or SL.11-12.5’s digital-media requirement. Provide a school-day shared-device route without student accounts, and record each digital component separately until completed.

Name the digital publishing/update opportunity in unit 2 and the strategic digital-media opportunity in unit 4. Retain the paper routes.

### 3. The final reading check applies the grade 12 endpoint to grade 11

**Severity:** Major  
**LAYER:** standard  
**REPEAT:** yes, related support-withdrawal problem in ELA progression independent review, F9  
**Confidence:** firm

**Location:** Course-level check after unit 9.

**What is wrong:** The final check requires an independent cold read at the high end of the band with no routine supports. Grade 11 expressly permits scaffolding there; independent proficiency at the high end is the grade 12 endpoint. This also contradicts the frame’s own support statement and its handoff to grade 12. [Official ELA standards, printed pages 38 and 40](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf).

**Why it matters:** Students could meet the grade 11 expectation and nevertheless fail the course’s stated proficiency check.

**Exact fix:** Replace the final-check description with:

> A cold read in the 11-CCR band, with documented scaffolding as needed at the high end. Supports preserve the reading being assessed and do not supply answers. Record supported proficiency separately from an optional independent extension.

Keep independence as a readiness observation and extension, not the universal grade 11 passing condition.

### 4. The shared research calendar does not match history, and the final writing deadline also collides

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, US History I independent review, finding 5  
**Confidence:** firm on the calendar; likely on daily capacity

**Location:** Process-writing calendar; unit 4; cross-subject research rows; US History I’s shared-project and writing-load instructions.

**What is wrong:**

- US History I reserves **weeks 12 to 15** for the shared research project.
- This frame places the shared brief in **weeks 13 to 15**, while its research product is due about **week 16**.
- The actual ELA sequence puts unit 4 on **days 59 to 78**. Its separate three-day opening project leaves days **62 to 78**, spanning weeks 13 to 16, for the sustained project.
- ELA’s final narrative is due about **week 31**. History explicitly asks ELA to keep its process-writing deadline out of that week because history’s empire report is due then.

A project spanning four calendar weeks is not necessarily 20 uninterrupted project lessons. The demonstrable fault is the incompatible calendars, rather than a proved minimum number of lessons.

**Why it matters:** Teachers cannot run the promised single project on both calendars. The final deadline also defeats the frame’s stated effort to coordinate writing load.

**Exact fix:**

1. Use one shared milestone calendar in both frames. Retain history’s previously settled **weeks 12 to 15** unless the two frames explicitly replace it together.
2. Rework ELA’s preceding days and check placement so the sustained project starts in week 12 and its shared paper and talk finish by week 15. Show the three-day short project separately and budget assessment/respond time.
3. Replace every conflicting research-window and due-date statement.
4. Move the narrative deadline out of week 31 and name its replacement week in both writing calendars.
5. Recompute downstream week ranges while preserving 160 days. Any proposed change to course duration or standard placement goes to Cory.

I agree with the earlier history review’s calendar correction. The ELA draft has reintroduced the discrepancy.

### 5. The *Trifles* author-choice example is factually wrong

**Severity:** Major  
**LAYER:** progression  
**REPEAT:** new  
**Confidence:** firm

**Location:** Unit 9; `e11-lit-author-choices.notes`.

**What is wrong:** Both use “the men offstage” as an example of Glaspell’s authorial choice. The male investigators enter the kitchen at the opening, speak there, leave and return. Minnie Wright, whose actions are reconstructed, remains absent. [Glaspell’s *Trifles*, opening scene and subsequent stage directions](https://www.gutenberg.org/cache/epub/59432/pg59432-images.html).

**Why it matters:** The example would generate an incorrect model analysis for RL.11-12.3 and misrepresent how the audience learns what the investigators overlook.

**Exact fix:** Replace the example in both locations with:

> Glaspell keeps Minnie Wright offstage and confines the visible action to the kitchen. The male investigators repeatedly leave and return while the women examine domestic evidence. Explain how those choices distribute knowledge and sympathy, and what a different staging would lose.

Keep the kitchen setting and the comparison of interpretations.

### 6. Unit 3 names two reading standards without securing their promised outcomes

**Severity:** Moderate  
**LAYER:** standard  
**REPEAT:** yes, partial-standard specification in the US History I reviews  
**Confidence:** likely

**Location:** Unit 3; `e11-info-founding-reasoning` and `e11-info-founding-documents`.

**What is wrong:** The advocacy task maps premises, reasons and conclusions but does not explicitly require a judgment of that reasoning. The document task specifies purpose, audience and a rhetorical feature, but omits analysis of themes. These are already inside the grade 11 progression’s stated contribution, not merely parts deferred to grade 12.

The unit’s compelling question gestures toward evaluation, but it does not tell a busy writer what students must produce. [Official ELA standards, RI.11-12.8 and RI.11-12.9, printed page 40](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf).

**Why it matters:** A unit could complete every listed task while only delineating advocacy and identifying document features.

**Exact fix:** Add two explicit performances:

- After mapping Paine and the Declaration, students judge a premise and the reasoning connecting it to a conclusion, supporting the judgment with textual evidence.
- For each core document, students state and trace a theme alongside purpose and rhetorical feature. End with a short synthesis showing a theme developed differently across two documents.

Name both performances in the unit assessment brief. Keep legal reasoning in grade 12.

### 7. The anchor inventory and complexity record are promised rather than available

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, earlier grade 6 ELA course review, findings 1 and 6  
**Confidence:** firm on the missing record

**Location:** “Anchor text records”; units 1, 4, 7, 8 and 9.

**What is wrong:** There is no `data/plans/english-language-arts-grade-11/` directory or course text inventory. Some selections remain unspecified, including the six to eight Dickinson poems, the Mather excerpt, reform-project sources, census table, testimony passages and performance versions. Approximate measures for two books do not establish the whole year’s complexity.

The frame also says the standards fix the year’s long texts to older works. They require historical American literature and specified founding documents, but do not mandate these particular long books. The books can remain sound choices without that rationale.

**Why it matters:** Anchor suitability, reading load, supports and availability cannot yet be checked consistently. The lens expressly asks for the year’s anchors and their placement evidence at this layer. The review criteria likewise require documented complexity analysis tied to tasks. [ELA 6 to 12 criteria, indicators 2b and 2c](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_6_12_Review_Criteria_2_0_a3fc2b49ab.pdf).

**Exact fix:** Before fixing the frame, provide a provisional inventory, independent of whether the final CSV schema is settled. Each required selection needs:

- Exact work, edition, excerpt limits and accessible source.
- Rights status and repository location, or an explicit acquisition task.
- Quantitative measure and provenance where appropriate.
- Qualitative analysis, task and placement reason.
- Reading load and text-specific support needs.
- For performances, two identified interpretations or a specified live-performance route.

Replace the mandate claim with: “These long works are course selections that support the historical-literature requirements.”

Report the narrow era and tradition range candidly. Preserve the already selected long books while Cory considers any scope change.

### 8. Unit 9 is organized around transferable skills more than one knowledge-building topic

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, related knowledge-coherence concern in ELA progression independent review, F5  
**Confidence:** judgment call

**Location:** Unit 9’s title, compelling question and anchor set.

**What is wrong:** Franklin’s imperial satire, Twain’s antiwar prayer and three works about marriage, domestic confinement and women’s knowledge are connected by irony and authorial technique. The frame does not explain what specific topic knowledge accumulates across all five texts.

**Why it matters:** The unit risks becoming an anthology of examples for standards. The local approach requires one topic and a connected text set. The external evidence guide allows tightly connected topics or themes, but still asks how the texts build knowledge together. [ELA evidence guide, indicator 2d, PDF pages 17 to 20](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_6_12_Evidence_Guide_2_0_2068cea08f.pdf).

**Exact fix:** Propose the core topic **“Marriage, domestic evidence and women’s authority in American fiction, 1892 to 1916”**, using Chopin, Gilman and Glaspell. Specify what each text adds to that topic and connect the narrative task to it.

Then explicitly decide the status of Franklin and Twain. Retaining them as brief satire comparisons rather than equal anchors is one possible route. The anchor-status or scope change goes to Cory; the writer should not silently remove them.

### 9. The preceding ELA frame still says Chemistry’s frame is unwritten

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale completion notes in earlier frame reviews  
**Confidence:** firm

**Location:** Grade 10 ELA frame, Cross-subject introduction, line 154.

**What is wrong:** It says the Chemistry frame “is written later, so its units are not guessed.” The frame now exists. It places `chem-climate-forecast` in unit 9, weeks 23 to 26, and identifies its receiving ELA dependencies.

**Why it matters:** The note leaves an available seam check presented as future work.

**Exact fix:** Replace the sentence with:

> Chemistry’s frame is on file. Its climate-forecast work is in unit 9, weeks 23 to 26, available by week 26 for ELA’s later explanatory work. Earlier technical writing uses the grade 9 skills and Chemistry’s model explanation.

Add the actual Chemistry unit references to the adjacent cross-subject rows.

### 10. Earlier ELA reviews still present resolved mathematics ownership as pending

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale completion notes  
**Confidence:** firm

**Location:** `progression-ela-codex-2026-11-13.md`, F7; `progression-ela-2026-11-13.md`, finding 6, its settled table and “What I could not judge.”

**What is wrong:** These passages still instruct future checking when the mathematics progression exists. It now exists, and the ELA fix report records the resolution. In particular, `alg1-two-way-tables` owns S-ID.B.5 in grade 9, supporting this course’s unit 8.

**Why it matters:** A later reader may reopen settled ownership or restore obsolete pending language.

**Exact fix:** Preserve the dated findings and append a resolution note:

> Resolved in `progression-ela-fixes-2026-11-13.md`. Mathematics ownership is now recorded: S-ID.C.9 and S-ID.B.5 in Algebra I, grade 9; S-IC.B.6 in Algebra II, grade 11. The grade 10 ELA lean was changed to 8.SP.A.1. Same-year timing is checked in course frames.

Mark the old pending recommendations as superseded.

### 11. The earlier history review still says this ELA frame does not exist

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale completion notes  
**Confidence:** firm

**Location:** `frame-us-history-i-codex-2026-11-13.md`, cross-subject availability, line 308, and its closing limitations.

**What is wrong:** The report attributes unverified ordering to the absence of an ELA 11 frame. That frame is now available. The remaining uncertainty is a calendar disagreement, not a missing document.

**Why it matters:** The note conceals the actionable discrepancy behind an obsolete reason to wait.

**Exact fix:** Append this dated resolution:

> Update, 2026-11-14: The ELA 11 frame is now on file. Founding-document and Douglass ordering can be compared directly. The research calendars disagree: history reserves weeks 12 to 15, while ELA’s current sequence reaches week 16. Resolve that discrepancy before describing the shared calendar as agreed.

Retain the original review as historical evidence.

## Coverage, order, days and seams

### Skills and standards

All **30 grade 11 skill rows** have exactly one home in the Skills column. Their references cover **41 distinct parent standards**: 9 literature, 10 informational reading, 10 writing, 6 speaking/listening and 6 language standards.

Every code is marked as a contribution to the two-year band. Grade 12 retains completion ownership. I therefore did not demand that grade 11 independently finish Shakespeare, legal reasoning or early twentieth-century literature. Those deferrals are explicit and have receiving units in grade 12.

Findings 2, 3 and 6 concern actual performance requirements or the stated grade 11 contribution. They are not objections to the band split.

Later returns to a skill are ordinary practice, not duplicate ownership. Earlier skills and models generally have retrieval or review instructions. The final check’s unlabelled acceleration to the grade 12 endpoint is the exception.

### Days and load

| Unit | Skill homes | Days | Current day range | Load judgment |
|---|---:|---:|---|---|
| 1 | 8 | 17 | 1 to 17 | Defensible for short texts plus year-long routines |
| 2 | 5 | 18 | 18 to 35 | Substantial but plausible, pending exact reading load |
| 3 | 5 | 20 | 36 to 55 | Substantial document set and process argument |
| First check/respond | | 3 | 56 to 58 | Explicitly reserved |
| 4 | 2 | 20 | 59 to 78 | Calendar must be reconciled, finding 4 |
| 5 | 2 | 15 | 79 to 93 | Plausible with stated home reading and support |
| Midyear check/respond | | 4 | 94 to 97 | Explicitly reserved |
| 6 | 2 | 20 | 98 to 117 | Defensible for the whole novel and literary argument |
| 7 | 1 | 13 | 118 to 130 | Not excessive merely because it owns one row |
| 8 | 1 | 8 | 131 to 138 | Defensible for a bounded source set |
| 9 | 4 | 17 | 139 to 155 | Exact selections, performances and writing schedule need budgeting |
| Final check/respond | | 5 | 156 to 160 | Adequate reservation; demand needs correction |

The arithmetic is **148 unit days + 12 course-level days = 160**. Against a 180-day school year, that leaves 20 days for school events and other interruptions.

No other unit is demonstrably far over or under its share at frame depth. Skill-row counts are not measures of instructional minutes. Final daily feasibility requires the anchor inventory and scope and sequence.

### Sequence and seams

The main sequence holds: evidence and routines precede extended analysis; Thoreau is read before the argument about his case; process writing precedes sustained research; earlier Puritan and Transcendental texts return beside Hawthorne; poetry precedes the later interpretation task.

Grade 10’s evidence, research, whole-text reading and discussion demands are picked up. Grade 12 receives the corresponding threads and generally makes a clear increase in independence.

The frame correctly identifies the remaining `e12-seminar` wording that describes grade 11 roles as teacher-set. Apply its proposed correction while retaining student leadership inherited from grade 10. That is an already identified repair, not a new finding here.

### Cross-subject availability

- Founding context in US History I units 1 and 2 precedes ELA unit 3.
- History’s slavery and reform work precedes the whole Douglass reading and later Hawthorne work.
- History’s immigration unit precedes the Riis source set.
- Algebra I teaches two-way tables in grade 9, before ELA unit 8.
- ELA’s informative writing and argument precede Physics’ stated receiving units.
- The frame supplies local background where courses run separately or out of step.

The shared research calendar and writing deadlines remain the material exceptions, finding 4.

### Source map

**Not applicable.** The course has no base curriculum under `BASE-TEXTS.md`. Absence of `source-map.csv` is not a defect. Its primary-text inventory and rights records are separate requirements.

## Lens checklist: course frame layer

| Lens line | Result |
|---|---|
| Units use specific topics and texts rather than skills or broad themes | **Missed in part.** Most units hold together; unit 9 needs a tighter knowledge-building account, finding 8. |
| Year’s anchors are on file, with measures, qualitative analysis and placement reasons | **Missed.** Some texts exist, but the complete selection and analysis record does not, finding 7. |
| Year’s texts avoid leaning to one era, tradition or kind | **Missed in part.** Genres are varied and both literary and informational work are substantial. The required anchors remain overwhelmingly older US Anglophone works. This is a disclosed scope issue, not grounds to discard the selected long books. |
| At least one long text is read whole | **Met.** *The Scarlet Letter*, Douglass’s *Narrative* and *Trifles* are planned whole. Apply the disclosed language omissions in finding 1. |

Foundational decoding requirements are **not applicable** to this grade’s course-frame checklist. Question percentages, lesson-level scaffolds, scoring materials and daily teaching quality belong to later layers and cannot be certified from this frame.

## What is right and should not be changed

- Preserve the single home for every progression skill and the explicit two-year ownership arrangement.
- Preserve the two whole books, whole American play and independent-reading log/conference.
- Keep recurring vocabulary, sentence work, writing and discussion.
- Keep the separation between historical context and ELA analysis.
- Retain paper access, no student accounts, sensitive-content notes and community-reader requirements.
- Keep supports beside the original text and fade them according to readiness.

The planned models, process pieces and feedback steps are consistent with the secondary-writing guide’s instructional direction. Their quality still depends on the actual lessons. [Teaching Secondary Students to Write Effectively](https://ies.ed.gov/ncee/wwc/PracticeGuide/22).

## Settled by the expert

These are proposed applications. Nothing was edited.

| Choice | Reason | File or record touched |
|---|---|---|
| Omit prohibited language with visible editorial markers and explanations | Preserves analysis while following rule 6 | Frame, units 3, 5 and 8 |
| Record digital requirements separately from paper completion | Keeps coverage claims accurate | Frame; `e11-process`, `e11-presentation` |
| Assess grade 11 band reading with needed high-end scaffolding | Matches this year’s endpoint | Final course-level check |
| Replace the incorrect *Trifles* staging example | Corrects the model analysis | Frame, unit 9; `e11-lit-author-choices` |
| Add explicit reasoning judgments and document-theme analysis | Completes already promised grade 11 work | Frame, unit 3 |
| Require a provisional anchor inventory before fixing the frame | Makes selection and pacing reviewable | Course text record |
| Keep the proposed seminar-note correction | Preserves leadership already established in grade 10 | `e12-seminar.notes` |
| Add dated resolutions to obsolete review notes | Preserves history while showing current work | Findings 10 and 11 locations |

## For Cory

- **Scope:** Decide any change to unit 9’s anchor status or the year’s range of required perspectives. Keep the existing long-book choices unless explicitly reconsidered.
- **Scope:** If calendar reconciliation requires changing course duration or moving a standard’s teaching home, decide that proposal.
- **People and money:** Assign the required community and qualified readers. Decide whether any new recordings need outside readers or funding.
- **Scope:** Confirm the proposed high-school ELA check set before additions become required content.

## Limits and outside sources

The full plan gate did not complete. This review does not certify daily pacing, every text’s rights, numerical complexity measures, performance availability, assessment quality or classroom effectiveness.

Sources opened for this read:

- [Official Common Core ELA standards](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf): grade-band design and the relevant reading, writing, speaking/listening and language requirements.
- [2012 text-complexity supplement](https://achievethecore.org/content/upload/Appendix-A-New-Research-on-Text-Complexity-revised%20%281%29.pdf): complexity framework and placement guidance. No new measure was computed.
- [ELA 6 to 12 review criteria](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_6_12_Review_Criteria_2_0_a3fc2b49ab.pdf) and [evidence guide](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_6_12_Evidence_Guide_2_0_2068cea08f.pdf): selected text-analysis, knowledge-building, range and research sections. The 141-page guide was not read in full.
- [New York grade 11 curriculum map](https://unbounded-uploads.s3.amazonaws.com/attachments/15621/ela-grade-11-curriculum-map.pdf): overview and research/writing sequence, used as a structural comparison only. Its noncommercial/share-alike material was not adapted.
- [Published grade 11 pacing guide](https://www.fishtanklearning.org/curriculum/ela/11th-grade/pacing-guide/): comparison of period assumptions, reading outside lessons and reserved calendar room. Its schedule is not a required template for Curio Class.
- [Secondary-writing practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/22): explicit strategy instruction and the model, practice and reflection cycle.
- [Glaspell’s *Trifles*](https://www.gutenberg.org/cache/epub/59432/pg59432-images.html): direct verification of staging and character presence.

**For the source list:** Add the specific grade 11 pacing-guide route, New York curriculum-map route and *Trifles* text route to `APPROACH-SOURCES.md` if retained for later reviews. The curriculum landing page returned an incomplete shell, but the linked map PDF was readable.

**Final disposition:** Revise before fixing the frame. **11 findings.** Requested report path: `docs/reviews/frame-english-language-arts-grade-11-2026-11-14.md`, delivered here only.


# Independent frame review: US History I

**Date:** 2026-11-13  
**Intended report path:** `docs/reviews/frame-us-history-i-2026-11-13.md`  
**Delivery:** Complete report below. No file was created or changed.

## Verdict

The nine-unit structure is defensible, all 27 owned progression rows are placed once, and the 160-day year includes adequate course-level check and respond time. The frame needs revision before approval because two owned standards remain partly specified, the Declaration instruction conflicts with the language rule, and the partial-base selections and shared research calendar are unresolved. Preserve the course structure and correct those writing instructions before the scope and sequence is built.

## What I read and checked

- `docs/agents/EXPERT.md`, the social studies lens, `docs/FOUNDATION.md`, the relevant ROADMAP sections, and BASELINE rules.
- The shared core and social studies section of `docs/ADOPTION-BAR-SUBJECTS.md`; `docs/courses/social-studies/STANDARD.md`.
- `docs/APPROACH.md`, relevant source-catalogue and evidence notes in `docs/APPROACH-SOURCES.md`, and `docs/sources/BASE-TEXTS.md`. No social studies approach page currently exists.
- The complete US History I frame, its `frames.csv` row, all 27 grade 11 social studies progression rows, and relevant incoming and outgoing progression records.
- The World History II and US History II frames.
- Relevant ELA 11 progression rows, including research, argument, founding documents and the Douglass reading. No ELA 11 course frame exists.
- Earlier social studies progression reviews and their fix report, cross-subject reviews and fixes, and the kindergarten and grade 1 frame reviews.
- Relevant decisions in `DESK-ANSWERS.md`, the frame-writing and frame-reading briefs, and current production-path status.
- Official Massachusetts and C3 framework passages, the historical legal sources linked below, the stored partial-base licence page, and the six teaching guides for the first two high school US history units of Since Time Immemorial.

### Gate results

| Command | Observed result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Stopped before completing: `ModuleNotFoundError: No module named 'markdown'` |
| Existing alternate Python | Could not launch its child process; no dependency was installed |
| `python -B -X utf8 scripts/frame.py check us-history-i world-history-ii us-history-ii` | All three frames: 0 failures |
| `python -B -X utf8 scripts/progression.py check social-studies` | 384 rows, 0 failures, advisory notes |
| `python -B -X utf8 scripts/stale.py check` | 19 files, 0 failures |

The full plan gate is **unverified**, rather than passed. The direct frame check establishes placement, code-list consistency and totals, not full instructional coverage. No defect-ledger entries were written because this review is read-only.

## Findings, most serious first

### 1. The Fourteenth Amendment standard is narrowed to citizenship cases

**Severity:** Major  
**LAYER:** standard, progression and frame  
**REPEAT:** yes, partial coverage inside a claimed standard, as in the earlier social studies progression reviews  
**Confidence:** firm

**Location:** Frame unit 6; progression rows `us1-native-west` and `us1-women-work-suffrage`.

**What is wrong.** `MA.USI.T6.5` includes the Amendment’s impact on Native Peoples and Asian and European immigrant men and women. Unit 6 names Elk and Wong Kim Ark, but does not secure the European immigrant comparison or distinguish citizenship from protections belonging to persons. The progression’s shorthand, “not to Native people” and “citizenship came in 1924,” also overgeneralizes.

**Why it matters.** A writer could teach constitutional protection as dependent on citizenship and present all Native people as lacking US citizenship before 1924. *Yick Wo* distinguishes protection of persons from citizenship; the 1924 statute expressly addresses people who were not already citizens. [Yick Wo opinion](https://www.govinfo.gov/content/pkg/USREPORTS-118/pdf/USREPORTS-118-356.pdf), [1924 Citizenship Act](https://www.archives.gov/files/historical-docs/doc-content/images/indian-citizenship-act-1924.pdf).

**Exact fix.**

- In `us1-native-west` and unit 6, require a comparison of citizenship, due process and equal protection for Native Peoples and Asian and European immigrant men and women, using the Amendment and selected legal sources.
- Retain Elk and Wong Kim Ark, and add Yick Wo to distinguish rights of persons from citizenship.
- Replace the universal 1924 shorthand with: “Native people acquired US citizenship through several earlier routes; the 1924 Act extended it to remaining noncitizen Native people born within the United States. Citizenship and access to voting are separate questions.”
- Correct the corresponding “Native women before 1924” shorthand in `us1-women-work-suffrage`.

Keep this work in unit 6 under its existing standard and days. The coverage requirement is explicit in the [Massachusetts framework, PDF page 126, printed page 126](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf).

### 2. The explanation standard lacks its full task

**Severity:** Major  
**LAYER:** standard, progression and frame  
**REPEAT:** yes, C3 code presence without its complete required work, as in progression review finding 1  
**Confidence:** firm

**Location:** Unit 5’s C3 column; `us1-argument-writing`.

**What is wrong.** Unit 5 owns `D4.2.9-12`, but its specified products are arguments. The progression mentions a sequenced explanation without explicitly requiring students to evaluate that explanation’s strengths and weaknesses for its purpose.

**Why it matters.** Explaining a causal process and defending a position are related but distinct products. The current instructions allow the argument essays to stand in for the explanation requirement. [C3 Framework, printed page 59](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf).

**Exact fix.** Add to the progression row and unit 5:

> Students also construct a sourced causal explanation of how sectional conflict developed into secession. It uses an explicit sequence, relevant examples and data, and explains the strengths and weaknesses of that causal account for its stated purpose.

Make this a companion section of the existing writing work, with separate scoring criteria, rather than another several-page essay. Require an independent explanation component in the unit assessment.

### 3. “Read in full” contradicts the no-slurs rule

**Severity:** Major  
**LAYER:** frame and progression  
**REPEAT:** new  
**Confidence:** firm

**Location:** Unit 1’s sensitive-topic instruction; `us1-declaration`.

**What is wrong.** Both direct the Declaration’s dehumanizing phrase about Native peoples to be read in full. BASELINE rule 6 prohibits slurs, and the frame otherwise requires excerpts around them.

**Why it matters.** The contradiction leaves the day writer to choose between binding instructions. It could produce prohibited student text or a compulsory oral reading.

**Exact fix.** Replace the instruction in both places with:

> Explain that the Declaration includes a dehumanizing description of Native peoples. Identify the grievance and its political purpose without printing or requiring students to speak the slur. Pair that analysis with Native-authored accounts of the conflict.

Keep the contradiction between equality claims and exclusion central to the lesson. This changes presentation within the existing standard, not its scope.

### 4. The partial base has no source map or selected depth

**Severity:** Moderate  
**LAYER:** base text  
**REPEAT:** new  
**Confidence:** firm on the missing record; likely on the pacing consequence

**Location:** Base-text bullet, units 2 and 6, and absent `data/plans/us-history-i/source-map.csv`.

**What is wrong.** The frame calls Since Time Immemorial a partial base and assigns its first two units broadly, but does not select their levels or account for lessons retained and omitted. Calling the whole course baseless does not resolve the partial-base mapping requirement.

**Why it matters.** These are materially different commitments. The stored foundational-documents Level 1 guide specifies one class period; the allotment Level 2 guide specifies two. Higher levels add substantial work. The choice affects the 15-day and 13-day receiving units.

The two guides supporting those counts are:

:codex-file-citation{path="S:/CurioClass-sources/since-time-immemorial/high-school-unit-1-us-history/4-us-hs-unit-1-level-1kt_.pdf" purpose="source"}

:codex-file-citation{path="S:/CurioClass-sources/since-time-immemorial/high-school-unit-2-us-history/us-hs-unit2-level2.pdf" purpose="source"}

**Exact fix.** Create the source map before frame approval. Record each guide from source units 1 and 2 as retained or omitted, with destination, periods, reason and rights exceptions. Explicitly exclude source units 3 to 6 from this course because their main periods belong in US History II.

My item-level selection is:

- Unit 2: the one-period Level 1 constitutional case, after constitutional principles.
- Unit 6: the two-period Level 2 allotment source analysis, with prerequisite retrieval.
- Other levels: omitted from the required path, with reasons recorded.

Name the Boldt example as a later Washington application, so its chronological jump is explicit. Check linked third-party readings individually; a guide’s umbrella licence does not establish every linked item’s reuse rights. The [publisher’s unit 1 page](https://ospi.k12.wa.us/student-success/resources-subject-area/john-mccoy-lulilas-time-immemorial-tribal-sovereignty-washington-state/high-school-curriculum/high-school-unit-1-us-history) and [unit 2 page](https://ospi.k12.wa.us/student-success/resources-subject-area/john-mccoy-lulilas-time-immemorial-tribal-sovereignty-washington-state/high-school-curriculum/high-school-unit-2-us-history) were discoverable, but live opening returned 403.

### 5. A four-week shared research project has a three-week window

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, shared research coordination from cross-subject review finding 8  
**Confidence:** firm

**Location:** Cross-subject research entry, reciprocal ELA research entry and writing-load paragraph.

**What is wrong.** `e11-research` specifies four weeks, at least five sources, approximately 1,500 words and a talk. The frame calls it a four-week project but places the shared brief in weeks 13 to 15.

**Why it matters.** The apparent coordination compresses the existing ELA commitment and crowds the transition into unit 5’s two full arguments.

**Exact fix.** Change every shared-project window to **weeks 12 to 15**. Use week 11 for reform context and preparation, then the four-week research window. State that the product is one paper and talk, scored separately for historical reasoning and ELA research/writing.

Record this as the availability requirement for the future ELA 11 frame. Its agreement cannot yet be verified. Preserve each course’s independent teaching path.

### 6. The qualified-reader list covers only part of the hard history

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** firm

**Location:** “For the lead,” item 4.

**What is wrong.** The staffing note names units 3, 4 and 6 only. Other units also contain Native or hard-history material: the Sullivan campaign, constitutional slavery protections, racial terror, anti-Chinese violence, lynching and imperial violence.

**Why it matters.** The abbreviated list can become the actual review assignment, leaving required course content outside the qualified person’s read.

**Exact fix.** Replace item 4 with:

> Arrange qualified community review covering Native and hard-history content across units 1 to 9, with the passages and communities identified in each unit’s source list. Every unit also receives the required fresh-agent sensitivity read before publication.

Cory assigns people and any budget. This finding expands the review inventory to match existing content, without adding teaching scope.

### 7. The model table contradicts earlier uses and omits the final argument

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, model continuity and metadata mismatches from earlier progression and cross-subject reads  
**Confidence:** firm

**Location:** “Models carried,” corroboration and claim-evidence-reasoning rows.

**What is wrong.** Corroboration is first scheduled in unit 4, although unit 2 explicitly reviews it and unit 1’s full research cycle includes corroborative value. Claim-evidence-reasoning omits unit 9, where the third full argument is written.

**Why it matters.** A writer following the model calendar can delay retrieval of a research routine already needed and omit its planned return in the final argument.

**Exact fix.**

- Corroboration: first use in unit 1, with retrieval before the first source-selection task; subsequent uses in units 2, 4, 5 and 9.
- Claim-evidence-reasoning: retain first use in unit 1 and add unit 9 to its returns.

Keep these as retrieval and continued use, not new ownership claims.

### 8. An earlier review still says the partial bases are not loaded

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale completion notes, as in the earlier frame reviews  
**Confidence:** firm

**Location:** `docs/reviews/progression-social-studies-codex-2026-11-13.md:73`.

**What is wrong.** The review says the candidate partial bases are not yet loaded. The source register and stored Since Time Immemorial files show otherwise.

**Why it matters.** The note can prompt redundant collection work and obscure the actual outstanding selection task.

**Exact fix.** Replace the current-status sentence, retaining a dated correction:

> Updated 2026-11-13: partial bases are loaded as recorded in BASE-TEXTS.md. US History I must still select and map the pieces it will adapt.

Preserve the original review’s historical context.

### 9. The Government and Economics decision is still marked reserved

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale completion notes  
**Confidence:** firm

**Location:** `docs/reviews/progression-social-studies-fixes-2026-11-13.md:38`.

**What is wrong.** The fix report says grade placement remains reserved for Cory. `DESK-ANSWERS.md`, card `q-ss-progression-1`, records his decision.

**Why it matters.** The stale note reopens a settled question affecting this course’s seams.

**Exact fix.** Replace it with:

> Closed by q-ss-progression-1, 2026-11-13: Government and Economics are open to grades 11 or 12. Their data rows remain grade 12, and their entry requirements do not depend on completing US History I.

### 10. C3 edition confirmation is still listed as unfinished

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale completion notes  
**Confidence:** firm

**Location:** `docs/ADOPTION-BAR-SUBJECTS.md:195` and its social studies status row at line 507.

**What is wrong.** Both retain the edition-confirmation task. The standards file names the official 2013 framework and June 2017 revised PDF, and earlier reviews checked its indicator tables. The official PDF was reopened for this review.

**Why it matters.** A settled source-identification task remains on the prerequisite list.

**Exact fix.** Replace both unfinished-task statements with:

> Edition confirmed: C3 Framework, 2013, June 2017 revised PDF, matching data/standards/c3-indicators.txt.

Link the [official PDF](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf).

### 11. Cross-subject ownership checking still supposedly waits for the progressions

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale completion notes  
**Confidence:** firm

**Location:** `docs/reviews/progression-social-studies-fixes-2026-11-13.md:43`.

**What is wrong.** The note says ownership checking waits on the other progressions. Those files exist; the cross-subject fix report describes the completed resolution and grade-checking work.

**Why it matters.** It confuses completed ownership checks with the still-open question of within-year availability.

**Exact fix.** Replace it with:

> Superseded by the cross-subject read and fix pass, 2026-11-13: references and owning grades were checked against all four progressions. Within-year availability remains a course-frame check; ELA 11’s frame is still needed.

### 12. The production path schedules a cross-subject read already recorded as complete

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale completion notes  
**Confidence:** firm

**Location:** `docs/PRODUCTION-PATH.md:249`.

**What is wrong.** The paragraph ends by scheduling the read across all four progressions. The next paragraph records that read and its fixes as complete.

**Why it matters.** A resume instruction points backward to completed work.

**Exact fix.** Replace the final sentence with:

> The cross-subject read and fix pass are complete, as recorded below. Step 2 develops and reviews the course frames.

## Coverage, order, days and seams

### Owned skills and standards

All 27 grade 11 skills are placed exactly once. Earlier-grade content is identified as revisited content, maintained skill or a skill transfer, with retrieval or reteaching specified.

All Massachusetts topic ranges have receiving units. Parent standards correctly carry optional case-study lists, including the reform and empire research choices. Their alternatives should not be converted into a requirement for a separate full investigation of every listed example.

The substantive full-coverage exceptions are findings 1 and 2.

### Units and days

| Unit | Owned rows | Days | Load judgment |
|---|---:|---:|---|
| 1. Revolution | 4 | 19 | Plausible for content, research teaching and a short argument |
| 2. Founding and early republic | 3 | 15 | Plausible with a bounded constitutional case |
| 3. Expansion and removal | 2 | 13 | Appropriate for maps, policies and source comparison |
| 4. Mills, cotton and reform | 4 | 21 | Longer allocation justified by linked economies and research |
| 5. Civil War and Reconstruction | 4 | 21 | Tightest writing allocation: two full arguments plus content |
| 6. Jim Crow and the West | 2 | 13 | Plausible only with a selected partial-base depth |
| 7. Industry and immigration | 2 | 13 | Plausible, building on earlier industrial history |
| 8. Progressivism and rights | 3 | 17 | Additional time justified by research and informed action |
| 9. Empire and war | 3 | 16 | Tight but plausible with survey, one case and reused argument routines |
| **Units** | **27** | **148** | |
| **Course checks and respond days** | | **12** | |
| **Total** | | **160** | |

No unit is demonstrably far over or under its share at frame depth. That judgment depends on bounding the partial bases and correcting the shared project window. Daily feasibility still needs period lengths and a scope and sequence.

The order holds: independence precedes constitutional construction; expansion and the linked Northern and Southern economies precede sectional crisis; Reconstruction precedes its dismantling; industrialization precedes Progressive responses. The thematic overlaps are explained.

Incoming handoffs from World History II are picked up. Outgoing handoffs match the US History II frame’s receiving units, including the research capstone, civil rights, immigration and reform threads. Its economic opening is a stated toolkit rather than a chronological gap.

### Cross-subject availability

All seven recorded outgoing ELA leans have matching grade 11 contributing rows. History explicitly teaches its disciplinary research, argument and news-reading routines, so it does not require grade 12 ownership first.

The proposed founding-document and Douglass sequence is sensible. Actual same-year ordering remains **unverified** because the ELA 11 frame does not exist. Finding 5 corrects the project duration without treating the proposed calendar as an agreed one.

## Lens checklist: course frame layer

| Lens line | Result |
|---|---|
| Every anchor standard in the course’s topic range has a unit | **Met for placement.** Full treatment still needs finding 1 |
| Replaced grade 3 or grade 8 own-state content retains Massachusetts-only content | **Not applicable.** Historical Massachusetts cases here are part of the national record |
| Units list check-set additions with recorded sources | **Met at frame depth.** All nine units identify candidates and sources; exact comparisons remain unit-plan work |

## What is right and should not be changed

- Preserve the nine-unit structure and 160-day total.
- Keep Northern industry and Southern slavery connected.
- Retain enslaved people’s agency, Native nations as present-day governments, and source criticism of retrospective accounts.
- Preserve the survey-plus-one-case design and complete materials for a student working alone.
- Keep the three full arguments: two in unit 5 and one in unit 9, with unit 1’s shorter rehearsal.
- Preserve student choice in informed action and each course’s independent teaching path.

Previously corrected research source-selection checks, long-gap retrieval arrangements and independent Government/Economics entry requirements are present. I do not reopen those settled findings.

## Settled by the expert

These are proposed applications, not edits made during this review.

| Choice | Reason | Files affected |
|---|---|---|
| Distinguish persons’ protections, citizenship and voting in unit 6 | Completes the existing standard and removes misleading shorthand | Frame; `us1-native-west`; `us1-women-work-suffrage` |
| Add a separately scored explanation within unit 5’s existing writing | Completes D4.2 without another long paper | Frame; `us1-argument-writing` |
| Analyze the Declaration’s dehumanizing wording without reproducing or requiring it aloud | Honors both historical accuracy and rule 6 | Frame; `us1-declaration` |
| Shared reform research runs in weeks 12 to 15 | Restores the specified four weeks | Frame; future ELA 11 frame |
| Select one-period constitutional and two-period allotment guides as the bounded partial-base starting points | Makes the receiving units’ commitments reviewable | Frame; source map |
| Retrieve corroboration in unit 1 and restore its later returns | Aligns the model calendar with actual tasks | Frame |

## For Cory

- Assign qualified community readers whose coverage includes the course’s Native and hard-history material across all nine units, with any necessary budget.
- Settle the frame’s proposed school-facing recommendation about taking Government in grade 12. The existing permission to take it in either grade remains settled.

No standard needs to move between units or grades.

## Limits, sources and source-list additions

The full plan gate could not complete. This review also cannot certify an unwritten ELA calendar, daily teaching time, final excerpts, assessment quality or all third-party rights.

No substantive finding rests solely on memory. Pacing judgments and the proposed bounded lesson selections are professional judgments. Prior memory informed report-format conventions only.

Sources used:

- [Massachusetts History and Social Science Framework, 2018](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf): USI coverage, optional research choices and the immigrant comparison.
- [C3 Framework, revised PDF](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf): owned inquiry, evidence, argument and explanation requirements.
- [Yick Wo opinion](https://www.govinfo.gov/content/pkg/USREPORTS-118/pdf/USREPORTS-118-356.pdf): protection of persons independent of citizenship.
- [Indian Citizenship Act, 1924](https://www.archives.gov/files/historical-docs/doc-content/images/indian-citizenship-act-1924.pdf): the statute’s application to remaining noncitizens.
- [Since Time Immemorial](https://ospi.k12.wa.us/student-success/resources-subject-area/john-mccoy-lulilas-time-immemorial-tribal-sovereignty-washington-state): publisher identification and licence context. Live pages were blocked; stored publisher materials supplied the lesson details.

**For the source list:** add the two legal primary-source links with the uses above, and record the current OSPI access limitation. Keep component-level rights checks separate from the umbrella licence.

**Verdict:** Revise before approval.  
**Finding count:** 12.  
**Report path:** `docs/reviews/frame-us-history-i-2026-11-13.md`, supplied here only.


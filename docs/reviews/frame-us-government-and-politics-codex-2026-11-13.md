# Independent frame review: US Government and Politics

**Date:** 2026-11-13  
**Intended report path:** `docs/reviews/frame-us-government-and-politics-2026-11-13.md`  
**Delivery:** Complete report provided here. No report file was created.

## Verdict

The frame has a sound overall sequence, places all 19 owned progression skills exactly once, and reserves course-level check and respond days within its 80-day half year. It needs revision before scope and sequence writing because some claimed standards remain incomplete or optional, particularly the digital capstone requirements. The most important change is to specify one feasible unit 9 route that completes the required digital work, collaboration and civic action for both classroom and home learners.

## What I read and checked

- `docs/agents/EXPERT.md`, the social studies lens, `docs/FOUNDATION.md`, the required Roadmap sections, `docs/APPROACH.md`, `docs/APPROACH-SOURCES.md`, BASELINE rules 20 to 24, and the locked glossary.
- Section 1 of `docs/ADOPTION-BAR-SUBJECTS.md` and `docs/courses/social-studies/STANDARD.md`.
- The complete Government frame, its `frames.csv` row, all 19 `gov-*` progression rows, and the incoming progression rows named in its seams.
- The grade 8 Civics frame, the World History I and II frames, US History I and II, and Economics. Government has no subsequent civics course; Economics is its suggested following half year.
- Relevant ELA and mathematics progression rows. ELA 11, ELA 12 and Algebra II course frames were absent when checked.
- The Massachusetts Government and News/Media Literacy standard records, official framework passages, and the official C3 indicator wording.
- Earlier social studies progression reviews and fix reports, cross-subject reviews, the kindergarten and grade 1 frame reviews, and the social studies source audit.
- `docs/sources/BASE-TEXTS.md`. There is no Government `source-map.csv`; the course has partial source material rather than a whole-course base text.

### Gate results

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Could not complete: `ModuleNotFoundError: No module named 'markdown'`. This is an environment failure, not a completed gate result. |
| `python -B -X utf8 scripts/frame.py check us-government-and-politics` | 0 failures; nine units, 80 days, 76 unit days and four course-level days. |
| `python -B -X utf8 scripts/progression.py check social-studies` | 384 rows, 0 failures, with advisory notes. |
| `python -X utf8 scripts/stale.py check` | 16 files checked, 0 failures. Unmarked stale notes remain below. |

No packages were installed. No turn-start, turn-end, mutation or defect-logging command was run under this read-only brief.

## Findings, most serious first

### 1. Unit 9 makes required digital work optional

**LAYER:** standard, frame and progression  
**REPEAT:** yes, incomplete requirements inside claimed standards, as in the earlier progression reviews  
**Severity:** serious  
**Confidence:** firm

**What is wrong.** Unit 9 permits “position papers or a digital product.” The `gov-local-action` notes also say students “may work online with outside experts.” Those alternatives leave `MA.NML.T5.4` and `MA.NML.T5.5` unsecured. The first requires producing a substantial digital artifact; the second requires online collaboration with outside experts and others. See the [Massachusetts framework, PDF page 179](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf#page=179).

**Why it matters.** A writer can follow the current instructions faithfully, assign a paper completed entirely within the class, and still claim both codes.

**Exact fix.** Replace the alternative in the frame and progression notes with:

> Every student contributes to a substantial digital portfolio, multipage site or podcast that carries the project’s evidence and position. Position papers may supply its content. Students collaborate through digital tools with an outside expert and other contributors, with an adult mediating contact.

Add a separate evidence requirement for each code. A recorded expert talk alone is a source, not collaboration. If outside collaboration cannot be supported, refer the placement of `NML.T5.5` to Cory rather than describing it as optional while claiming full coverage.

### 2. The shortened founding-document standard drops named ideas

**LAYER:** standard, progression and frame  
**REPEAT:** yes, omitted parts of bundled Massachusetts standards, as in the earlier social studies Codex review  
**Severity:** moderate  
**Confidence:** firm

**What is wrong.** The official `GOV.T1.6` includes constitutionalism and republicanism among the ideas students interpret through founding documents. The local standard paraphrase, `gov-founding-documents` notes and unit 2 list omit both. Republicanism appears as a theory in unit 1, but the frame does not explicitly carry it into the document analysis. Constitutionalism is not named in the frame. Compare the [official framework, PDF page 163](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf#page=163).

**Why it matters.** The local standard record can reproduce the omission in every later plan, while the gate continues to find the correct code.

**Exact fix.** Restore both ideas in the own-word description of `MA.GOV.T1.6`, the progression notes and unit 2:

> Interpret constitutionalism, government bound by constitutional powers and limits, and republicanism, government exercised through representatives, alongside the other named ideas. Support each interpretation with a provision from a founding document.

Use the Constitution’s allocation and limitation of powers and its representative institutions. This completes the standard already assigned to unit 2; it does not move a standard.

### 3. The nonpublic option does not specify a completed action

**LAYER:** frame and standard  
**REPEAT:** yes, the completed-action requirement identified for `gov-local-action` in the earlier Codex progression review  
**Severity:** moderate  
**Confidence:** likely

**What is wrong.** The course brief and unit description require completed action, but unit 9’s teacher note says a team may decline public action and still complete a reflection. It does not identify what action that team completes. A busy writer can reasonably read this as a reflection-only alternative.

**Why it matters.** The course’s one informed-action opportunity can become preparation followed by reflection without action. The [C3 framework, PDF page 62](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf#page=62) distinguishes taking action from discussing possible action.

**Exact fix.** Replace the final sentence of unit 9’s teacher note with:

> Students may decline public identification, public speaking or advocacy for a position. They still complete a chosen, safe civic action, such as submitting an evidence-based information request through an adult or delivering a nonpartisan information product to a consenting audience, then reflect on the response or lack of response.

Protect students’ choice of position. Do not require a visible policy change as evidence of successful completion.

### 4. The procedure comparison still stops short of evaluating civic purposes

**LAYER:** frame and progression  
**REPEAT:** yes, the `D2.Civ.11.9-12` issue identified in the earlier Codex progression review  
**Severity:** moderate  
**Confidence:** likely

**What is wrong.** Unit 4 compares procedures from a town council to the UN Security Council. The progression adds a state legislature and says students examine how each checks power. Neither clearly requires judging how successfully procedures achieve civic purposes, which is the indicator’s distinctive demand. See [C3, PDF page 34](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf#page=34).

**Why it matters.** Describing voting rules or vetoes can replace the intended evaluation of representation, accountability, minority protection or effective decision-making.

**Exact fix.** Add to unit 4 and `gov-checks-balances`:

> Compare a decision procedure at local, state, national and international levels. Judge how well each achieves a named civic purpose, using evidence about whose voice counts, who can block a decision and who can be held accountable.

The earlier repair correctly added the governmental levels. This finding concerns the remaining evaluation requirement.

### 5. The seven-day capstone needs earlier preparation and a home route

**LAYER:** frame  
**REPEAT:** yes, pacing and overlapping research demands were raised in the earlier progression and cross-subject reads  
**Severity:** moderate  
**Confidence:** judgment call

**What is wrong.** Unit 9 has seven days for issue selection, research, competing views, compromise, institutional evaluation, a substantial digital product, outside collaboration, action and reflection. Its assessment and respond day also sit inside those seven days. The preceding course-check respond day currently *launches* team choices, leaving outside participation dependent on a very short response window. Contact is routed only through a school, although a parent teaching one child is an established audience.

**Why it matters.** The likely compression falls on revision, collaboration or action, precisely the work that makes this a capstone.

**Exact fix.**

- Let students select the local issue during unit 8 and use it for that unit’s current-policy reporting.
- Have the course-check respond day confirm readiness and revise the plan.
- Carry the factual report, editorial and visuals into unit 9’s digital product.
- Arrange the outside collaborator before unit 9 begins.
- State: “School staff or the teaching parent mediate contact; public posting and student accounts are unnecessary.”
- In the scope and sequence, demonstrate a seven-day completion path that includes assessment and response. If it does not fit, return a specific day-transfer proposal rather than silently dropping requirements.

This retains the existing unit ownership. Its feasibility still needs a timed trial.

### 6. One check-set attribution is wrong, and the comparison edition needs naming

**LAYER:** frame  
**REPEAT:** new  
**Severity:** minor  
**Confidence:** firm for the California attribution

**What is wrong.** Unit 1 attributes political ideologies and political socialization partly to California 12.3. That standard concerns civil society and its values, rather than political socialization. The college-level framework is the appropriate cited source for that addition. Compare [California’s standards, PDF pages 62 to 63](https://www.cde.ca.gov/be/st/SS/documents/histsocscistnd.pdf#page=62).

The frame also leaves its college-level comparison edition unnamed. The current framework is effective fall 2026 and includes four additional foundational documents. See the [official corrections document](https://apcentral.collegeboard.org/media/pdf/ap-us-government-and-politics-course-and-exam-description-clarifications.pdf).

**Why it matters.** Later writers cannot reliably reproduce the comparison, and an outdated document list can become an apparent completed check.

**Exact fix.** Attribute unit 1’s socialization addition to the college-level framework’s topics 4.1 to 4.4. Retain California 12.3 as support for civil society. Name the fall 2026 comparison edition and require the unit-plan comparison to record decisions on its newly added documents. Their inclusion in the comparison source does not automatically require adding all four to this course.

### 7. The frame claims reciprocal ELA planning that does not yet exist

**LAYER:** process  
**REPEAT:** yes, unverified cross-subject availability was identified in the earlier cross-subject reads  
**Severity:** minor  
**Confidence:** firm

**What is wrong.** The Cross-subject introduction says the ELA frames “record the need for both” grade 11 and grade 12 routes. Neither frame was present when checked. ELA progression rows exist, but they do not establish unit timing. Algebra II’s progression confirms ownership of the statistics skill, but its course frame is also absent.

**Why it matters.** A proposed coordination request reads as an already agreed calendar.

**Exact fix.** Replace the introduction with:

> The ELA progression identifies the matching grade 11 and grade 12 rows. Their course frames have not yet confirmed timing. The table below states Government’s proposed coordination requests and the teaching it supplies when it comes first.

Retain the explicit mathematics bridge in unit 6. Mark reciprocal frame confirmation as pending rather than completed.

### 8. Grade-placement notes still contradict Cory’s settled decision

**LAYER:** process  
**REPEAT:** yes, stale and boilerplate notes were findings in the earlier social studies review  
**Severity:** minor  
**Confidence:** firm

**What is wrong.** Thirteen Government progression rows still contain grade-12-only wording:

`gov-foundations`, `gov-federalism`, `gov-courts`, `gov-executive`, `gov-checks-balances`, `gov-rights-cases`, `gov-parties-elections`, `gov-interest-groups`, `gov-media-democracy`, `gov-policy-news`, `gov-local-action`, `gov-world-affairs`, and `gov-international-orgs`.

The progression fix report’s “Skipped, needs Cory” section still presents placement as unresolved. The grade 8 frame also describes the next separate civics course as grade 12 Government. Cory’s `q-ss-progression-1` decision already permits grades 11 or 12.

**Why it matters.** Writers can restore prerequisites or calendar assumptions that the later decision deliberately removed.

**Exact fix.** Replace grade-12-only statements with:

> Government may be taken in grade 11 or 12. Its rows remain at grade 12 for data ownership. Grade 8 civics prerequisites return after a gap, with the readiness support named here.

Remove fixed skipped-grade counts where they vary by enrollment year. Change the grade 8 seam to “Government in grade 11 or 12.” Add a dated resolution note to the earlier fix report, preserving its original historical account.

### 9. The source audit still presents settled permissions and completed loading as pending

**LAYER:** process  
**REPEAT:** yes, stale completion notes also occur in the earlier frame reads  
**Severity:** minor  
**Confidence:** firm

**What is wrong.** `social-studies-open-material-2026-11-13.md` still describes the retired Government text as gated on Cory’s decision, treats acceptance of OGL v3.0 as outstanding, labels some loaded material “ready to load,” and says science goes second. Later decisions and `BASE-TEXTS.md` record the permissions and loading; the current production order places social studies first.

**Why it matters.** This is a source-selection document future writers are instructed to consult. Its unresolved-status wording can halt authorized work or redirect the production order.

**Exact fix.** Add a dated resolution section and label the superseded recommendations as historical:

> Resolved 2026-11-13: Cory accepted the retired CC BY texts as partial bases and added OGL v3.0 to the permitted base licences. Current permissions, loading status and item-level restrictions are recorded in BASE-TEXTS.md. The production order is governed by PRODUCTION-PATH.md, with social studies first.

Replace the affected Government table verdict and loaded-source status cells with their current status. Preserve remaining item-level rights checks.

## Coverage, order and days

### Owned skills and standards

The ownership boundary is the 19 `gov-*` rows. The other grade 12 rows belong to US History II and Economics, not to Government.

| Unit | Days | Owned progression skills |
|---|---:|---|
| 1 | 6 | `gov-foundations`; `gov-civic-associations` |
| 2 | 9 | `gov-founding-documents`; `gov-ideals-gap` |
| 3 | 7 | `gov-federalism` |
| 4 | 14 | `gov-executive`; `gov-courts`; `gov-checks-balances`; `gov-limited-government` |
| 5 | 9 | `gov-rights-cases`; `gov-free-press` |
| 6 | 9 | `gov-parties-elections`; `gov-interest-groups`; `gov-media-democracy` |
| 7 | 7 | `gov-world-affairs`; `gov-international-orgs` |
| 8 | 8 | `gov-policy-debates`; `gov-policy-news` |
| 9 | 7 | `gov-local-action` |
| **Total** | **76** | **19 skills, each placed once** |

The frame names 40 numbered Government standards, 14 News/Media Literacy standards and ten distinct owned C3 indicators. Code placement is complete; findings 1 to 4 identify requirements that placement alone does not secure.

`D2.Civ.1.9-12` legitimately spans units 3 and 7: domestic and tribal institutions first, international institutions later. These are complementary parts, not duplicate skill placement. Earlier-grade knowledge is identified as retrieval, readiness work or practice. The agency and policy lists contain examples, so they should not become equal-depth studies of every listed option.

### Reasons and sequence

The sequence holds: purposes and participation, founding ideas, allocation of power, branch operations, rights, political influence, foreign affairs, policy analysis and action. Judicial review precedes rights cases; parties and public opinion precede foreign-policy influence; policy research precedes the capstone.

Unit 6’s reason says unit 8 uses media “at once,” although unit 7 intervenes. This is a wording correction: change it to “prepares the media work used again in unit 8.”

### Time

The 76 unit days plus four course-level days total 80. On a 90-day semester calendar, that leaves ten calendar days outside the frame. The scope and sequence must state period length and the shorter-calendar route.

Unit 4’s 14 days reasonably recognize its substantial institutional load. Units 3 and 7 each have seven days, respectively carrying five and eight numbered Government standards plus additional work. They deserve detailed scheduling, but code counts alone do not establish an overload. Unit 9 is the clearest feasibility risk, for the reasons in finding 5.

### Sources and seams

A complete base-lesson inventory is not applicable to this own-course frame. The partial chapter references do not map an NC or reference-only curriculum as adaptable material. Every selected piece still needs its own rights and credit check.

The grade 8 handoff is picked up with explicit readiness support. World History II supplies argument, human-rights and international-context work. Government correctly avoids assuming completion of US History I. Its proposed unit 8 news-literacy bridge should be copied into `gov-policy-news` notes because US History I places its corresponding news-reading work late in the year.

Economics does not depend on Government completion. The suggested Government-then-Economics order therefore remains advice, not a prerequisite.

## Lens checklist: course frame layer

| Lens line | Result | Evidence |
|---|---|---|
| Every anchor standard in the course’s Massachusetts topic range has a unit | **Met for placement; missed for full coverage** | All codes are placed. Findings 1 and 2 identify incomplete requirements. |
| The replaced grade 3 year or grade 8 own-state work avoids Massachusetts-only content | **Not applicable to those grades; met here** | Government uses the student’s state, Massachusetts and another state as worked examples. |
| Units list check-set additions with recorded sources | **Missed in part** | Every unit has an additions cell, but unit 1’s California attribution needs correction. Full comparison tables properly belong to unit planning. |

## What is right and should not be undone

- Keep the distinction between grade 8 founding events and this course’s analysis of governing ideas.
- Keep the explicit grade 11 entry route without US History I prerequisites.
- Keep Congress before the executive within unit 4.
- Keep tribal nations as present-day governments, with community and sensitivity reads required.
- Keep unseen-source assessments, structured deliberation, student choice of position and protection of family information.
- Keep the unit 6 statistics bridge rather than assuming Algebra II has already taught inference.

## Settled by the expert

| Choice | Reason | File touched by the caller |
|---|---|---|
| Retain nine units and 80 days at this layer | No demonstrated need to change the course length | Government frame |
| Use about three days for Congress at the start of unit 4 | Lawmaking supports later institutional and policy analysis | Government frame and future unit 4 plan |
| Complete constitutionalism and republicanism within unit 2 | They belong to the standard already assigned there | Standard record, progression and frame |
| Use an adult-mediated, nonpublic submission as an action option | Preserves student choice while completing action | Government frame and progression |
| Reuse unit 8 reporting in unit 9’s digital product | Reduces repeated research and preserves time for revision | Government frame |
| Record the one-day news-literacy bridge in `gov-policy-news` | Grade 11 Government cannot assume US History I’s late-year news unit | Social studies progression |
| Compare against the fall 2026 college-level framework | Makes the check reproducible and current | Government frame and unit comparison records |
| Change “uses it at once” to “uses it again in unit 8” | Matches the actual sequence | Government frame, unit 6 reason |

## For Cory

- **People:** Confirm a supportable outside-collaboration arrangement for classroom and home learners. If that cannot be provided, decide where `NML.T5.5` will be taught in full.
- **People:** Identify the qualified community reader required for the tribal-sovereignty and hard-history material. No contact or spending is authorized by this report.

## What I could not judge

- A successful full `plan.py check`, because the available Python environment lacks `markdown`.
- Reciprocal timing in the absent ELA 11, ELA 12 and Algebra II frames.
- Actual classroom minutes, source difficulty, assessment quality and capstone completion time before the scope and sequence, source sets and timed trials exist.
- Complete New York and Tennessee comparisons. The New York PDF fetch failed and the Tennessee PDF returned 403. No finding depends on assumed wording from those inaccessible documents.
- Final legal accuracy of selected cases or final rights clearance of adapted pieces.

No finding relies on unverified subject memory. Pacing judgments are professional estimates, not measured classroom results.

## Outside sources and source-list additions

- [Massachusetts History and Social Science Framework, 2018](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf): Government requirements, example lists and News/Media Literacy requirements.
- [C3 Framework, revised 2017](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf): indicator verbs, institutional levels, deliberation and action.
- [California History-Social Science Content Standards](https://www.cde.ca.gov/be/st/SS/documents/histsocscistnd.pdf): civil society, Congress and the unit 1 attribution.
- [College-level Government framework, effective fall 2026](https://apcentral.collegeboard.org/media/pdf/ap-us-government-and-politics-course-and-exam-description.pdf) and [official corrections](https://apcentral.collegeboard.org/media/pdf/ap-us-government-and-politics-course-and-exam-description-clarifications.pdf): comparison edition, topic placement and updated document list.
- [Educating for American Democracy Roadmap](https://www.educatingforamericandemocracy.org/the-roadmap/): inquiry, civic participation and the relationship between historical and civic questions.
- [Civic Online Reasoning](https://cor.inquirygroup.org/): comparison of explicit source-evaluation routines. The curriculum overview was read, not the complete lesson collection.

For the source list, add these verified routes where absent, including the edition and the limited extent of this read. None is permission to adapt restricted material.

**Verdict: revise before scope and sequence writing. Finding count: 9. Intended report path: `docs/reviews/frame-us-government-and-politics-2026-11-13.md`, delivered here only.**
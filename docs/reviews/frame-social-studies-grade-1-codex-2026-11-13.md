# Expert cold read: social studies, grade 1

**Date:** 2026-11-13  
**Intended report:** `docs/reviews/frame-social-studies-grade-1-2026-11-13.md`  
**Delivery:** Markdown here only. No file was created or edited.

The frame has a sound structure, but needs revision before unit planning. Its biggest curriculum risk is that unit 6 can produce identification of national symbols and songs without the explanations their standard requires. Make that explanatory work explicit, preserve kindergarten’s sourcing routine, and close the assessment and handoff gaps below.

## What I read

- `docs/agents/EXPERT.md`, the social studies lens, the shared adoption criteria and social studies section of `docs/ADOPTION-BAR-SUBJECTS.md`, and `docs/courses/social-studies/STANDARD.md`.
- `docs/FOUNDATION.md`, the required Roadmap sections, BASELINE rules 20 to 24, `docs/GLOSSARY.md`, the shared approach and relevant source-register entries.
- The complete kindergarten, grade 1 and grade 2 social studies frames.
- All 21 grade 1 progression rows, their kindergarten prerequisites and receiving grade 2 and grade 3 rows.
- The grade 1 Massachusetts standards, their lettered parts, C3 indicators, economics exclusions and relevant cross-subject progression rows.
- `data/plans/frames.csv`, the base-text record, frame-writing requirements, relevant earlier social studies and cross-subject findings, and their fix reports.
- Official outside sources listed below.

There is no grade 1 base text or source map. That agrees with the repository’s source decision.

### Gates

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Could not complete: the default interpreter lacks `markdown`. No curriculum failure was established by this attempt. |
| Frame checks for kindergarten, grade 1 and grade 2 | All passed, zero failures. |
| `python -B -X utf8 scripts/stale.py check` | Final run: 19 files, zero failures. The unmarked stale notes below escape this check. |

The full plan gate remains unverified. I continued the substantive read because its interruption was an environment dependency error, while the relevant frame gate ran successfully.

## Findings, most serious first

### 1. Unit 6 does not secure explanation of national symbols and songs

**LAYER:** standard  
**REPEAT:** yes, bundled-code incompleteness in `progression-social-studies-codex-2026-11-13.md`, finding 2  
**Confidence:** firm

**What is wrong:** The frame promises every lettered part of `MA.1.T3.2`, but unit 6 supplies a list of buildings, a statue, phrases and songs. The progression similarly emphasizes recognition of tunes and words. The anchor requires recognition **and explanation of meaning**, including the songs. [Massachusetts framework, PDF page 41](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf#page=41).

**Why it matters:** A writer could build naming, matching and singing activities that leave the standard’s explanatory work untaught.

**Exact fix:** In unit 6 and `ss1-national-symbols.notes`, require students to explain what each selected symbol, phrase and song communicates about belonging to the United States, using a supplied image, text or lyric excerpt as evidence. Explicitly revisit the flag and eagle as kindergarten review. Clarify `MA.1.T3.2c` in the local standards file so recognizing words and tunes does not replace the parent standard’s meaning requirement. Preserve the choice not to sing or recite.

### 2. Grade 1 weakens the sourcing routine kindergarten hands on

**LAYER:** frame  
**REPEAT:** yes, the prerequisite and handoff mismatch kind identified in earlier progression reads  
**Confidence:** likely

**What is wrong:** Kindergarten’s frame requires asking who made a photograph and whether it is old or new. Grade 1 replaces this with source kind and age only. Grade 2 then resumes maker, date and place. These adjacent frames do not describe a continuous routine.

**Why it matters:** Students can spend a year treating a photograph as an anonymous illustration instead of evidence somebody created.

**Exact fix:** Replace the grade 1 reading-level bullet’s last sentence with:

> Every source gets a short sourcing talk: what kind it is, who made it when known, whether it is old or new, and what it can help the class find out. The teacher supplies available maker information from the source credit. This maintains kindergarten’s routine; grade 2 teaches the fuller maker, date and place investigation.

This preserves earlier learning without moving grade 2’s owned indicator.

### 3. The final course-level check has no respond day

**LAYER:** frame  
**REPEAT:** yes, the assessment-to-response continuity kind discussed in earlier assessment reviews  
**Confidence:** firm on the requirement; judgment call on the allocation

**What is wrong:** Both respond days follow the mid-year check. The final check ends with a record sent to grade 2. The Roadmap’s finished-course requirements say cumulative checks are followed by response.

**Why it matters:** The final evidence records misconceptions without giving this course time to address them.

**Exact fix:** Keep the 96-day total and all unit allocations. Allocate the two respond days as **one after the mid-year check and one after the final check**. State that each includes targeted teaching and a brief fresh task to check the response. The split remains 91 unit days, three assessment days and two respond days.

### 4. The group-roles handoff remains unresolved

**LAYER:** progression  
**REPEAT:** yes, orphan skills in `progression-social-studies-2026-11-13.md`, finding 3  
**Confidence:** firm

**What is wrong:** `ss1-group-roles.hands_on` is empty. Grade 3’s `ss3-taking-part` develops community participation and roles but assumes only `ss1-voting`. The grade 1 writer correctly identifies this defect under “For the lead”; it remains present in the data.

**Why it matters:** The receiving writer gets an election prerequisite but no explicit instruction to reactivate the contribution of ordinary group members.

**Exact fix:** Add `ss3-taking-part` to `ss1-group-roles.hands_on`, and `ss1-group-roles` to `ss3-taking-part.assumes`. Extend the receiving row’s existing dormant-handoff note to include a readiness task about roles contributing to a shared goal, with a short reteach when needed. Update the frame’s seam row after that repair.

No standard changes grade or unit.

### 5. Unit 3 attributes a kindergarten comparison standard to grade 1

**LAYER:** frame  
**REPEAT:** yes, inaccurate source attribution in earlier social studies reads  
**Confidence:** firm

**What is wrong:** Unit 3 attributes stories of honesty and courage in American and world history to “California grade 1.” That language corresponds to **California K.1.2**, rather than a grade 1 addition. [California standards, PDF page 10, printed page 3](https://www.cde.ca.gov/BE/ST/SS/documents/histsocscistnd.pdf#page=10).

**Why it matters:** The comparison column presents earlier-grade review as evidence of an additional grade 1 expectation.

**Exact fix:** Replace that entry with:

> Honesty and courage in historical stories revisit California K.1.2 as review. The grade 1 analysis of leaders is anchored in MA.1.T1.4. Record any additional grade 1 check-set requirement, with its code, in the unit plan’s comparison table.

Keep the leader study and its present placement.

### Stale-note findings

Each numbered row below is a separate finding. **LAYER: process. REPEAT: yes**, the stale-note kind already identified in the social studies progression expert read, finding 9. **Confidence: firm.**

| # | What is wrong and where | Why it matters | Exact replacement or closure text |
|---|---|---|---|
| **6** | Grade 1 frame, “For the lead” item 3, says the gate reports `frames.csv` as disagreeing. Its row is now `8,96` and the frame gate passes. | Sends the next worker toward a nonexistent discrepancy. | “The grade 1 row in `data/plans/frames.csv` matches this frame: 8 units, 96 days. Frame gate passed on 2026-11-13.” |
| **7** | Kindergarten frame, final lead item, makes the same obsolete disagreement claim. Its row is `6,64`. | Misstates the incoming frame’s readiness. | “The kindergarten row in `data/plans/frames.csv` matches this frame: 6 units, 64 days. Frame gate passed on 2026-11-13.” |
| **8** | Grade 2 frame, lead item 4, makes the same obsolete disagreement claim. Its row is `7,96`. | Misstates the receiving frame’s readiness. | “The grade 2 row in `data/plans/frames.csv` matches this frame: 7 units, 96 days. Frame gate passed on 2026-11-13.” |
| **9** | `docs/GLOSSARY.md:52` labels the progression CSV location “planned.” All four core-subject progression files exist. | Makes established planning data appear prospective. | Remove “(planned)” and retain `data/progressions/<subject>.csv` as the current location. |
| **10** | `docs/GLOSSARY.md:53` says course frames are “Not built.” Frames now exist. | Gives readers the wrong location and state of this layer. | Replace with “`docs/courses/<slug>/frame.md`; PRODUCTION-PATH step 2. Frames are being written and reviewed.” |
| **11** | `docs/ROADMAP.md:95` says social studies waits on an open content-standard decision. `STANDARD.md` records the decision and completed loading. | Can wrongly block authorized planning. | “The social studies content-standard decision is settled and loaded; see `docs/courses/social-studies/STANDARD.md`. Work follows `docs/PRODUCTION-PATH.md`.” |
| **12** | Roadmap lines 118 and 528 still describe the lesson-day template as awaiting writing. The template and its checking/building script exist. | Preserves a completed prerequisite as unfinished work. | In both places, replace the future-writing parenthesis with “the existing lesson-day template, `docs/courses/LESSON-DAY.md`.” |
| **13** | `progression-social-studies-fixes-2026-11-13.md:43` says cross-subject ownership checking waits on the other progressions. The subsequent cross-subject read and fix pass exist. | Leaves a completed grade-level audit in the unresolved list. | “Subsequently addressed by the cross-subject progression reads and `progression-cross-fixes-2026-11-13.md`. Within-year availability remains for paired course-frame review.” |
| **14** | The open-material report’s “Open items” still asks Cory to decide the OGL licence and retired-text AI-clause questions. `BASE-TEXTS.md` records both decisions. | Can reopen settled scope and reuse decisions. | “Closed 2026-11-13: Cory accepted OGL v3.0 and the recorded use of the retired CC BY editions. Follow `docs/sources/BASE-TEXTS.md`; item-level rights checks remain required.” |

For dated reports, the replacement status should be recorded as a dated closure annotation, preserving what was true during the original read.

## Ownership, standards, order and days

The frame gate settles placement: **21 skills, each in exactly one unit; 24 owned Massachusetts codes and 24 owned C3 indicators**. The three excluded grade 1 economics standards have explicit grade 2 destinations. The anchor itself identifies economics as shared with grade 2, so this split is defensible. [Massachusetts framework, PDF page 42](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf#page=42).

| Unit | Days | Owned skills | Judgment on load and placement |
|---|---:|---:|---|
| 1. Our groups | 10 | 3 | Appropriate opening routines and group concepts. |
| 2. Clues from the past | 9 | 2 | Appropriate early placement for the continuing calendar and later historical sources. |
| 3. Leaders | 12 | 2 | More time is justified by biographies, historical context and written explanations. |
| 4. Choosing together | 10 | 2 | Builds on leaders and supplies the later action cycle’s election procedure. |
| 5. Maps and places | 12 | 3 | Reasonable allowance for directions, capitals, physical features and making a map. |
| 6. One country, many people | 13 | 3 | A substantial load. Keep its time and repair finding 1. |
| 7. Helping our community | 12 | 2 | Four weeks at the stated frequency is reasonable for investigation, action and reflection. |
| 8. Earning, buying and saving | 13 | 4 | Connected extensions of kindergarten economics justify fewer days per row. |

No unit is demonstrably far over or under its share. The 96 sessions occupy 32 weeks at three sessions per week, leaving four weeks in a 36-week calendar for interruptions and flexibility.

The owned standards are adequately represented at frame level except for finding 1’s insufficiently specified explanatory demand. Actual teaching, practice and assessment coverage cannot be certified before those artifacts exist.

Earlier-grade models are generally identified as review. The introduction of continents and oceans is distinguished from grade 2’s fuller placement work. I found no unit-order reversal requiring a standard to move.

## Seams and cross-subject availability

Kindergarten’s 19 outgoing skill links are picked up here. Grade 2’s receiving seam agrees with grade 1’s outgoing seam. The named direct returns in grade 3 have progression reasons and retrieval provisions; finding 4 is the remaining unconnected role skill.

The matching mathematics, ELA and science course frames were unavailable during this read. Therefore **same-year teaching-first order is unverified**, rather than passed.

| Dependency | Owning progression row | First need here | Current protection |
|---|---|---|---|
| Picture and word information | `e1-pictures-and-words` | Unit 2 | Photographs, objects and teacher reading. |
| Connections within informational text | `e1-connections` | Unit 3 | Teacher comparison chart. |
| Opinion with reason and closure | `e1-opinion` | Unit 3 | Social studies explicitly teaches shared writing first. |
| Data in up to three categories | `m1-data-three-categories` | Unit 4 | Small teacher-led tally and comparison. |
| Addition and subtraction within 20 | `m1-all-problem-types`, with contributing rows | Unit 8 | Smaller amounts if needed. |
| Seasonal daylight observations | `s1-daylight-seasons` | Unit 2 onward | Calendar begins independently; daylight interpretation joins science later. |

These are sensible provisional bridges. The paired-frame review must identify actual availability and ensure any bridge includes teaching, student practice and readiness evidence. Reciprocal ELA and social studies references do not establish which subject teaches writing first.

## Lens checklist: course-frame layer

| Lens line | Mark | Evidence |
|---|---|---|
| Every anchor standard in the course range has a unit | **Met for placement; missed in full specification** | Codes are placed. Finding 1 concerns the work required by one placed standard. |
| Replaced grade 3 year or grade 8 own-state work retains Massachusetts-only content | **Not applicable** | This is grade 1. Its own-state governor and capital method is appropriate. |
| Units name check-set additions and record their source | **Missed in part** | Every unit has an entry, but unit 3 misattributes its California source, finding 5. Full three-state comparison tables belong to unit planning. |

The broader design also preserves compelling questions, direct content teaching, growing written conclusions and one student-chosen action cycle. Historical material is organized by its stated civic purpose, with timelines carrying chronology. Source quality, competing accounts and unseen-source end-of-unit assessments require later artifact review.

## Settled by the expert

These are recommendations for the caller to apply. Nothing was edited.

| Choice | Decision and reason | File touched |
|---|---|---|
| Symbol work | Require explanations supported by supplied evidence, alongside recognition. | Grade 1 frame; progression notes; local standard clarification |
| Sourcing routine | Preserve kindergarten’s teacher-supported maker question. | Grade 1 frame |
| Respond days | Split the existing two days between mid-year and final checks. Keep 96 days. | Grade 1 frame |
| Group roles | Mirror the grade 1 to grade 3 handoff and extend the receiving readiness provision. | Social studies progression; frame seam |
| California attribution | Label K.1.2 as review, retaining the leader unit and its grade 1 anchor. | Grade 1 frame |
| Unit order and allocations | Retain all eight units and their current day allocations. | Grade 1 frame |

## What is right and should remain

- Supporting questions precede the inquiries that use them.
- Sources precede historical leader study; government precedes capitals; voting precedes the action cycle.
- The economics split is documented rather than silently omitted.
- Read-alouds and visual sources protect access for early readers.
- Family and citizenship examples avoid compelled personal disclosure.
- Native nations appear in the present, and hard-history content is named plainly.
- The action cycle includes investigation, student choice, enactment and reflection.

## What I could not judge

- A successful full plan gate, because of the missing dependency.
- Cross-subject teaching order without the matching frames.
- Actual lesson duration, source difficulty, assessment coverage or independent student performance.
- Final sensitive-content accuracy and rights clearance before the source sets exist.
- The complete New York grade 1 framework: its official PDF timed out. Search-index material was available, but I did not treat that as a full comparison.

No finding rests on unaided memory. Pacing and the proposed response-day split are professional judgments, not claims of demonstrated classroom effectiveness.

## For Cory

- Confirm the proposed scope of **96 sessions at three approximately 30-minute sessions per week**.
- Identify the qualified community reader required for the Native and hard-history material before those units go live.

No new expenditure or audience change is proposed.

## Outside sources and source-list additions

- [Massachusetts 2018 History and Social Science Framework](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf): grade 1 content, lettered requirements and the shared economics topic.
- [Official C3 Framework PDF, revised June 2017](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf): indicator wording and age-banded inquiry expectations. The PDF loaded despite a blocked landing-page request.
- [California History-Social Science Content Standards](https://www.cde.ca.gov/BE/ST/SS/documents/histsocscistnd.pdf): checked the proposed comparison additions and established finding 5.
- [Tennessee 2024 official standards crosswalk](https://www.tn.gov/content/dam/tn/stateboardofeducation/documents/standards/social-studies-2022-2023/TN%20Social%20Studies%20Standards%20Crosswalk%206.24.pdf): inspected the new grade 1 column as a secondary content check.
- [New York K-8 framework](https://www.nysed.gov/sites/default/files/programs/curriculum-instruction/ss-framework-k-8a2.pdf): attempted twice; full retrieval failed.
- [Official K-ESS3-1 expectation](https://www.nextgenscience.org/search-standards?keys=animals): checked the earlier science connection and its modelling demand.

For `docs/APPROACH-SOURCES.md`, record the working direct C3 PDF address, the official comparator links and the New York retrieval limitation. Do not describe an entire comparator as read when only selected grade-level material was inspected.

**Verdict:** revise before unit planning. **Finding count:** 14, comprising five curriculum or attribution findings and nine stale-note findings. **Report path:** `docs/reviews/frame-social-studies-grade-1-2026-11-13.md`, delivered here only.
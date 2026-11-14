# Independent expert review: Grade 4 social studies scope and sequence

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/sequence-social-studies-grade-4-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files changed.

## Verdict

Revise before unit-plan writing. The seven-unit structure, calendar, prerequisite bridges and inquiry arcs are sound, but the assessment outlines and several daily goals do not secure the full performances claimed by their standards. The most important change is to connect each required performance to an explicit teaching day and a named component of its end-of-unit assessment.

## What I read and checked

- `docs/agents/EXPERT.md`, the social studies lens, the shared and social studies adoption bar, and `docs/courses/social-studies/STANDARD.md`.
- The scope and sequence, all 160 rows of `days.csv`, and the Grade 4 frame.
- All 17 Grade 4 progression rows, with the relevant Grade 3 and Grade 5 prerequisite, model and handoff information.
- All 39 owned Massachusetts content standards and the 19 distinct owned C3 indicators. The Grade 4 content codes have no separate lettered child parts; the regional suffixes identify subtopics.
- `CALENDAR.md`, every Grade 4 subject’s rows in `calendar.csv`, and the other subjects’ frame placements for the named leans.
- `FOUNDATION.md`, relevant ROADMAP sections, BASELINE rules 20 to 24, `APPROACH.md`, relevant source-register entries, and the sequence-writing rules.
- Both earlier Grade 4 frame reviews and relevant social studies progression findings and fix records.
- Outside standards and limited curriculum comparisons listed below.

Memory supplied review prompts only. No substantive finding rests solely on memory. Final source difficulty, historical accuracy and sensitivity remain later reads of the selected materials.

### Gate results

| Command | Observed result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Reported an unrelated missing civics sequence, then stopped because Python package `markdown` is unavailable |
| `python -X utf8 scripts/frame.py calendar` | Passed; Grade 4 social studies check weeks are 8, 21 and 27 |
| `python -X utf8 scripts/frame.py check social-studies-grade-4` | Passed, 0 failures |
| `python -X utf8 scripts/plan.py check social-studies-grade-4` | Passed, 0 sequence failures |
| `python -X utf8 scripts/stale.py check` | Stopped with `KeyError: 'node'` while reading its completion ledger |

The full plan and stale-note checks are incomplete; neither prevents this course-specific verdict.

## Findings, most serious first

### 1. The end-of-unit outlines leave substantial taught work unassessed

**Severity:** High  
**LAYER:** sequence  
**REPEAT:** yes, the code-to-performance completeness problem identified in earlier Grade 4 frame and progression reads  
**Confidence:** firm

**Location:** Assessment days 15, 37, 58, 78, 102, 131 and 159, and their prose descriptions.

The outlines reserve useful unfamiliar-source tasks, but those tasks do not establish coverage of every owned standard. Adding a skill or code to an assessment row does not make its stated task assess that skill.

| Unit and end day | Coverage not secured by the stated assessment |
|---|---|
| 1, day 15 | Physical-feature identification, political locations and geographic vocabulary |
| 2, day 37 | Research and presentation, explanation critique, and why nations trade |
| 3, day 58 | Archaeologists’ methods, `MA.4.T2.3` |
| 4, day 78 | Norse evidence, voyage routes and motives, source-kind uses, and simultaneous-event comparison |
| 5, day 102 | Transport, contrasting migration motives, voluntary versus forced arrival, and an explicit slavery-expansion explanation |
| 6, day 131 | State and territory locations, admission timeline, statehood explanation, map construction and civic resources beyond buildings |
| 7, day 159 | Contributions across all five regions, regional disaster responses, catastrophe-driven settlement change and the international comparison |

Unit 6 is the clearest performance mismatch: days 114 to 118 construct maps, but both assessment descriptions ask students to **read** maps. Day 120 also names statehood’s code while asking only for an admission span.

**Why it matters:** Writers could produce engaging units whose final evidence cannot distinguish mastery from partial learning. The external assessment criteria similarly call for demonstrations of content, concepts and skills, rather than a narrow sample alone. [AIR and EdReports criteria, criterion 6](https://air.org/sites/default/files/2024-01/23-23505_HQIM_for_SS_Final.pdf)

**Exact fix:** Expand each unit’s assessment description into a performance-to-component table before writing its items. Name independently completed products already budgeted in the unit as summative components where appropriate, retain an unfamiliar-source transfer task on the named end day, and add targeted components for the omissions above. For Unit 6, require actual map construction and an explanation of statehood; preserve the existing assessment and response allocations.

A synthesis task plus targeted content evidence is a workable design pattern. The reference guide distinguishes these purposes explicitly, although Curio Class’s requirement to assess every owned part is its own. [Investigating History guidebook, assessment section](https://www.doe.mass.edu/investigatinghistory/curriculum/curriculum-guidebook.pdf)

### 2. Several daily goals narrow the required performance

**Severity:** High  
**LAYER:** sequence, progression  
**REPEAT:** yes, earlier Grade 4 frame findings on partially specified standards and progression finding 1 on C3 depth  
**Confidence:** firm on the omissions; likely on how writers would interpret the broad wording

The following are requirements that need explicit placement, not additional standards.

| Location | Problem | Exact fix within the existing days |
|---|---|---|
| Unit 4, days 65 to 74 | Voyages are described and timelined, but no goal requires tracing their routes on a map | Add route tracing to days 66, 69, 71 and 72, using one accumulating map |
| Unit 5, day 85 | “Why people moved west” does not explicitly require comparison; settlement life is also unclear | Compare two documented motives, including men’s and women’s experiences, and retain both journey and settlement evidence |
| Unit 6, days 121 to 123 | The Northeast case can be delivered entirely as explanation | Make day 122 a short question-led investigation using two supplied sources, followed by the existing comparison |
| Unit 7, days 138 to 142 | Broad references to “its peoples” do not secure each region’s required contributions | Put the region-specific group categories and a contribution task in each day’s goal or note |
| Unit 4, days 62, 63 and 78 | Asking audience and purpose can become reading supplied labels | Require an inference supported by a clue within the source, with prompts during teaching |
| Unit 7, day 144 | Movement concerns people only | Include goods and ideas, and explain how cultural and environmental characteristics affected their movement |

These distinctions follow the adopted content and skill standards. [Massachusetts framework, Grade 4, printed pages 62 to 66](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf); [C3 Framework, geography and historical-source indicators](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf)

The regional problem is especially consequential in the Southwest and West descriptions. Naming African Americans somewhere in the year does not secure their contributions in those regions. Likewise, teaching exclusion and incarceration does not by itself teach what Chinese and Japanese American communities contributed.

**Why it matters:** A busy writer can follow the current goals faithfully and still omit the required action or people. The progression already specifies prompted source inference, so that omission would also weaken the Grade 5 handoff.

### 3. Local workloads are uneven despite defensible unit totals

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, the earlier progression and frame reviews’ days-by-load concern  
**Confidence:** judgment call on timing; firm on the concentration of tasks

| Unit | Total days | Understanding | Fluency | Application | Assessment | Respond |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 16 | 9 | 2 | 3 | 1 | 1 |
| 2 | 22 | 8 | 2 | 10 | 1 | 1 |
| 3 | 18 | 11 | 1 | 4 | 1 | 1 |
| 4 | 20 | 12 | 2 | 4 | 1 | 1 |
| 5 | 24 | 17 | 2 | 3 | 1 | 1 |
| 6 | 26 | 11 | 2 | 10 | 2 | 1 |
| 7 | 24 | 13 | 1 | 8 | 1 | 1 |

No whole unit is demonstrably far over or under its load. Two local runs need revision:

- **Unit 6:** Day 108 combines the Northeast with locating and naming all 50 states and capitals. Days 114 to 118 then allocate exactly five lessons, 200 minutes, to five substantial maps. The Southwest lesson additionally introduces the Long Walk and several historical layers.
- **Unit 7:** Day 142 combines the Gold Rush, two communities, exclusion and incarceration in one 40-minute lesson. Its content spans substantially different contexts.

**Why it matters:** These goals invite rapid labeling or compressed hard-history summaries where students need source work and explanation.

**Exact fix:**

- Distribute the state-capital addition across days 108 to 110 by region, with explicitly scheduled retrieval on days 119 and 130.
- Specify supplied base maps and bounded source sets for days 114 to 118. Teach the Long Walk briefly before students map its movement.
- Rebalance days 142 to 144 as a three-day regional investigation: migration and contributions, exclusion and incarceration, then the cross-region and own-place comparison. Preserve the local thread and the movement explanation.
- Keep the seven unit totals unchanged.

The reference course’s 116 lessons of 30 minutes provide context, not proof of feasibility for these individual tasks or a reason to cut this course mechanically. [Massachusetts Grade 4 overview, printed page 8](https://www.doe.mass.edu/investigatinghistory/curriculum/g4-course-overview.pdf)

### 4. Writing recurs, but its intended growth is not stated

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** new  
**Confidence:** likely

**Location:** Days 14, 35, 56, 76, 100, 129 and 157.

These days repeatedly ask students to write and share a claim from sources. Unit 2 adds a short report and Unit 7 adds a proposal, but the sequence does not state how the recurring historical and geographic argument becomes more sustained or less scaffolded.

Grade 3 already hands on a short written claim with named evidence and a linking reason. Repetition is useful, but it does not establish the scope-layer lens requirement for growth from shorter to longer source-based writing.

**Why it matters:** Different unit writers could repeat the same heavily framed paragraph throughout the year.

**Exact fix:** State this progression beside the recurring writing days:

- Day 14: one modeled paragraph with a full frame.
- Day 35: a short report and a focused claim using organized notes.
- Days 56 and 76: two linked paragraphs, with reasons connecting evidence to the claim and a reduced frame.
- Days 100, 129 and 157: an independently organized response using a checklist.
- Days 155 to 156: draft and revise the proposal for its chosen audience.

These are item-level expectations, not additional days. Retain oral rehearsal and access supports. A reference inquiry illustrates how varied source-based intermediate products can feed a sustained final argument, without supplying wording or tasks for adaptation. [New York Complex Societies inquiry, printed page 2](https://c3teachers.org/wp-content/uploads/2024/04/NewYork_5_Complex_Societies.pdf)

### 5. The required shorter route is absent

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, the earlier independent Grade 4 frame review identified this need for the sequence stage  
**Confidence:** firm

**Location:** “The year at a glance” and the course as a whole.

The course specifies 160 daily lessons of about 40 minutes, approximately 107 hours. It offers no shorter route, although FOUNDATION section 5 and adoption-bar criterion C2 require one where schools have less time.

**Why it matters:** Teachers cannot tell what to consolidate while preserving prerequisite teaching, assessment and response time.

**Exact fix:** Add a shorter-route table identifying retained, merged and optional activities, its minutes, and its assessment coverage. Protect required content and response time. Any proposal to drop standards or change the supported audience belongs to Cory.

The target timetable is the audience decision listed below. This finding does not authorize changing the full route’s seven units or 160 days.

### 6. Review flags and “first” claims do not consistently match the plan

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, earlier Grade 4 frame findings on uneven sensitivity flags and stale notes  
**Confidence:** firm

**Locations:** The introductory sensitivity statement, Unit 3’s prose, and several `note` cells.

The introduction says every relevant day names the sensitivity read, but days 49 to 51, 54 and 71 lack that flag despite their Native content. Disaster days also do not consistently carry the promised routing note.

Unit 3 calls day 48 the “first weighed claim of the year,” although days 14 and 35 already require evidence-based claims.

**Why it matters:** Review routing becomes unreliable, and a writer may treat an established routine as new.

**Exact fix:**

- Add the sensitivity-read note to every applicable day, including the Native-content examples above and the disaster sequence. Keep the specific community/source instructions in the frame.
- Replace “first weighed claim of the year” with “first claim weighing archaeological migration theories.”
- Describe Unit 4 sourcing as a deepening of earlier source work, avoiding a misleading implication that earlier evidence requires no sourcing.

The sequence already discloses three frame corrections: the readiness sentence and the Unit 3 and Unit 7 cross-subject day ranges. Apply those replacements as written. They are acknowledged reconciliation work, not additional findings here.

## Calendar, prerequisites and assessment placement

The checks on days 39 to 40, 104 to 105 and 133 to 134 fall in weeks **8, 21 and 27**, matching the explicit Grade 4 target table. No Grade 4 week contains another subject’s course-level check days.

| Lean | Availability and disposition |
|---|---|
| Map measurement, days 5 to 6 | Math Unit 6 is days 77 to 95; the local bridge is present |
| Research and reporting, Unit 2 | ELA research follows in days 39 to 77; local note-taking and report frames are present |
| Archaeological layers, day 43 | Science Unit 4 is school days 72 to 92; the local explanation is present |
| Firsthand and secondhand accounts, day 62 | ELA Unit 4 is days 120 to 156; the local bridge is present |
| Admission spans, day 111 | Math Unit 5 ends on day 76 |
| Resource reasoning, Unit 6 | Science Unit 2 ends on school day 48 |
| Hazard response, Unit 7 | Science Unit 5 ends on school day 117 |
| Erie Canal, day 83 | ELA’s canal unit runs on days 81 to 119; reuse the source set without assuming its full analysis is already taught |

No readiness day is required under the current idle-time rule: the assumed rows were used in Grade 3. Retrieval tasks are the appropriate opening treatment.

Unit 6’s mid-unit assessment is correctly placed on day 120. Its response opens day 121 and is not counted again. Other unit and course-level response allocations are also counted once.

The early “year-end” check intentionally excludes Unit 7, as the frame explains. Keep that limitation explicit rather than presenting it as evidence about the entire year.

## Candidate cells and source map

All nine candidate additions are settled with a placement inside the existing unit totals:

| Unit | Kept addition and placement |
|---|---|
| 1 | Western Hemisphere context, day 4 |
| 2 | Government comparison, day 24 |
| 3 | Settlements and farming, day 51 |
| 4 | Navigation tools, day 65; hemispheric exchange, day 68 |
| 5 | Erie Canal, day 83; overland trails, day 85 |
| 6 | States and capitals, beginning day 108, with redistribution required by finding 3 |
| 7 | Gold Rush, day 142, within the rebalanced run in finding 3 |

No unresolved candidate cell remains. Full check-state comparison tables remain unit-plan work.

**Base-text source map: not applicable.** This course has no base text. Reference curricula remain references.

## Scope and sequence lens checklist

| Lens line | Mark | Evidence |
|---|---|---|
| Questions require the unit’s evidence and allow defensible answers | Met at sequence depth | Maps, trade, archaeological evidence, conquest, expansion and regional relationships supply the substance |
| History follows time order or explains departures | Met | Thematic overview, present-day continuity and closing returns are identifiable; retain timeline signposting |
| Contested events carry more than one telling | Met at sequence depth | Migration theories, landing accounts and the war with Mexico explicitly require comparison |
| Source-based writing recurs and grows from short to long | Missed in part | Recurrence is strong; growth needs finding 4 |

## What is right and should remain

- Map knowledge precedes its later uses, and research routines precede sustained investigations.
- Earlier frame repairs are visible: the Northeast region map, preserved-site explanations, paired timeline, worker/business specialization, human-made catastrophe and policy history.
- Native nations appear in the present as well as the past.
- Conquest, slavery, forced movement, exclusion and incarceration are named plainly.
- Multiple perspectives inform the war with Mexico.
- The action cycle follows research and policy analysis, with sending left to student and teacher choice.
- Paper access and protections against compelled family disclosures are explicit.

## Settled by the expert

Recommendations for the caller to apply. No edits were made.

| Choice | Reason | Files affected |
|---|---|---|
| Keep seven units and their current totals | No demonstrated whole-unit imbalance requires restructuring | Scope and sequence; `days.csv` |
| Use explicit assessment components plus an unfamiliar-source transfer task | Secures breadth without requiring one oversized final task | Same files, assessment descriptions |
| Distribute capitals across the regional location days | Removes the day 108 bottleneck | `days.csv`, days 108 to 110, 119 and 130 |
| Use supplied base maps and bounded source sets | Makes the five-map run more plausible | `days.csv`, days 114 to 118 |
| Rebalance days 142 to 144 | Gives hard-history contexts space while retaining local and comparative work | Scope and sequence; `days.csv` |
| Require source clues for audience and purpose | Preserves the existing Grade 4 inference step | `days.csv`, days 62, 63 and 78 |
| State writing length and scaffold progression | Makes growth visible to subsequent writers | Scope and sequence; recurring writing days |
| Retain retrieval rather than add readiness days | Follows the current idle-time rule | Existing frame correction |

## For Cory

- **Audience:** Set the minimum timetable the shorter route should support. No reduction in standards or change to the full route is assumed.

## Limits and sources

This is a sequence review, not a finished-course adoption review. Actual items, scoring, source accessibility, reading demand and lesson timing remain unverified. No finding requires an outside person or reverses the current agent-read policy.

Outside sources opened during this read:

- [Massachusetts 2018 framework](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf): Grade 4 content requirements and clarifications.
- [C3 Framework](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf): owned indicators and their performance demands.
- [AIR and EdReports criteria](https://air.org/sites/default/files/2024-01/23-23505_HQIM_for_SS_Final.pdf): sequence, inquiry, usability and assessment criteria.
- [Massachusetts Grade 4 overview](https://www.doe.mass.edu/investigatinghistory/curriculum/g4-course-overview.pdf): limited pacing and skill-progression comparison.
- [Investigating History guidebook](https://www.doe.mass.edu/investigatinghistory/curriculum/curriculum-guidebook.pdf): assessment architecture and inquiry structure.
- [New York Complex Societies inquiry](https://c3teachers.org/wp-content/uploads/2024/04/NewYork_5_Complex_Societies.pdf): opening inquiry map and progression of source-based products.
- [Oak National Academy comparison lesson](https://www.thenational.academy/teachers/lessons/comparing-the-earliest-civilisations): limited inspection only; no finding depends on it.

**For the source list:** Add the guidebook’s assessment-section access note and the New York inquiry’s opening-plan inspection to `APPROACH-SOURCES.md`. Neither was read as a whole curriculum.

**Verdict:** Revise before unit-plan writing. **Finding count:** 6. **Report path:** `docs/reviews/sequence-social-studies-grade-4-2026-11-14.md`, supplied here only.


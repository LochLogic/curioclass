# Baseline 1: independent sampled structure review

**Date:** 2026-11-14  
**Part:** B structure, sampled  
**Report destination:** `docs/reviews/baseline-1-codex-2026-11-14.md`  
**Delivery:** Complete report below. No file was created, edited or deleted. No git commands were run.

## Verdict

The sampled curriculum structure is coherent enough to retain its units, progression placements and disciplinary choices. It is not yet ready for an unqualified handoff into scope and sequence production: the downstream gates and planning instructions still assume the older math course structure, and the four subjects lack one executable calendar. Close the five structural findings below before treating baseline 1 as the production reference.

## What I read and checked

Read in full:

| Frame | Units | Course days | Stated classroom block |
|---|---:|---:|---|
| `math-grade-4` | 9 | 160 | 60 minutes |
| `science-grade-4` | 6 | 120 | 45 minutes, four times a week |
| `english-language-arts-grade-4` | 4 | 160 | 90 minutes |
| `social-studies-grade-4` | 7 | 160 | 40 minutes |
| `algebra-i` | 7 | 160 | 45 to 50 minutes |
| `biology` | 10 | 160 | 50 minutes |
| `english-language-arts-grade-9` | 8 | 160 | 50 minutes |
| `world-history-i` | 10 | 160 | Not stated |

Also read:

- The Seams sections and course-level checks of the four subjects’ grade 3 and grade 5 neighbours.
- The corresponding sections of grade 8 math, science and ELA, Geometry, Chemistry, grade 10 ELA, grade 8 civics and World History II.
- The sampled courses’ 201 progression rows for standard references, models and cross-subject links, with targeted handoff and notes checks.
- `AGENTS.md`, `EXPERT.md`, the four subject lenses, the glossary, production steps 2 to 4, frame-writing and frame-reading briefs, foundation, approach and relevant subject-bar provisions.
- The cross-subject reconciliation report and relevant entries in the band fix reports. Settled curricular findings are not reopened here.
- `frames.csv`, `courses.csv`, the catalogue-to-course enumeration, plan-flow code, and the frame, progression, stale, plan and relevant lesson-check code.
- The unit-planning instructions and plan-data formats needed by the next production stages.

**Required gate:** `plan.py check` could not complete because Python lacks `markdown`; the review continued under the brief’s fallback rule.

Independent structural checks found:

| Check | Result |
|---|---|
| `frame.py check`, eight sampled frames | 0 failures |
| `frame.py check`, all 52 frames | 0 failures |
| Four progression checks | 1,261 rows, 0 failures |
| `stale.py check` | 56 files, 0 failures |
| Current core plan-flow roster against frame slugs | Exact 52-course match |

The plan-flow generator was inspected without executing it, because it writes files.

## Findings

### 1. The next planning stages do not yet have compatible identities, validation or entry instructions

**Severity:** Serious  
**Confidence:** Firm, directly reproduced  
**LAYER:** gate, process  
**REPEAT:** yes for the known identifier problem; the downstream failures and stage mismatch are additional structural evidence.

**Locations:** `scripts/plan.py:21`, `:615`, `:620`, `:898`; `scripts/lesson.py:23`, `:126`, `:333`; `scripts/course_status.py:200`; `scripts/plan_flow.py:51`; `docs/pipeline/briefs/plan.md`; `docs/courses/UNIT-PLAN.md:49`; `data/plans/frames.csv`.

The frame slugs are suitable identifiers for individual courses. The downstream plan gate still splits a folder name into subject and grade, recognizes the math standards inventory only for the old subject name, and assumes a 60-minute day.

Read-only calls reproduced:

| Call | Observed result |
|---|---|
| `plan.check("biology")` | `ValueError`, because the identifier has no hyphen to split |
| `plan.check("algebra-i")` | 0 failures, 0 items |
| `plan.check("math-grade-4")` | 0 failures, 0 items |
| `plan.check("social-studies-grade-4")` | 0 failures, 0 items |

The empty results are not validation of a new course. Its plan files do not exist, and the gate does not require them.

There is also no stage-appropriate handoff contract. Step 3 sets every day before step 4 writes unit assessments, but the current detailed day gate expects section records and exit items. The unit-writing brief simultaneously asks for section plans and the preceding unit’s written last day. The unit template still says the previous unit must be built first. Those requirements conflict with planning all units before the probe and with section planning in step 7.

**Why it matters:** The first new course can crash, appear to pass without data, or be planned against the old course’s timing. Writers may also create premature section plans or manufacture assessment items simply to satisfy a gate intended for a later stage.

**Exact fix:**

1. Keep existing catalogue identifiers and use frame slugs as canonical individual-course identifiers. Extend `frames.csv` with authoritative metadata:

   ```text
   course,catalog_id,subject,grade,units,days,lesson_minutes_min,lesson_minutes_max,lessons_per_week,legacy_plan_id
   ```

   Required mappings include:

   | Canonical course | Catalogue id |
   |---|---|
   | `math-grade-4` | `math-k8` |
   | `science-grade-4` | `science-k5` |
   | `english-language-arts-grade-4` | `ela-k12` |
   | `social-studies-grade-4` | `ss-k5` |
   | `algebra-i` | `algebra-1` |
   | `biology` | `biology` |
   | `english-language-arts-grade-9` | `ela-k12` |
   | `world-history-i` | `world-hist-hs` |

   Make every frame’s identification line begin:

   > Course `<canonical course>` (catalogue id `<catalog_id>`).

   Preserve `math-4` as an explicit legacy alias during its scheduled reconciliation.

2. Replace folder-name inference in `plan.py` and `lesson.py` with metadata lookup. Select standards by subject, and check each day against its declared minutes within the course’s permitted block. Unknown courses and missing required stage files must fail explicitly.

3. Have `course_status.py` expose the canonical identifier. Have `plan_flow.py` join on that identifier instead of deriving identity from a display title. The current title-derived joins happen to match all 52 frames.

4. Add a scope-and-sequence writing brief with this governing text:

   > Read the canonical frame, its progression rows and the grade calendar. Write every course day in order, including readiness, assessment, response and review allocations. At this stage, reserve assessment slots and purposes; do not require finished items, answer keys or section plans. Unit plans supply those details in step 4. Section plans follow in step 7, except the section selected for the probe.

   Provide a separate scope-stage check for this output. Keep the detailed item and lesson checks for their proper stages.

5. Replace `UNIT-PLAN.md` rule 5 with:

   > Unit plans follow the subject-wide order in PRODUCTION-PATH steps 3 and 4. A preceding unit need not have written lessons. Section plans follow step 7, except the probe section.

   Update `plan.md` accordingly, including its requirement to read a preceding written day.

6. Before each subject’s scope writing starts, fix its required schemas. In particular, do not leave ELA text-record columns awaiting a retired pilot. Preserve the settled timing: text records and day-level source maps belong with the scope and sequence, not retrospectively before frame closure. Allow source maps to identify a course unit before section identifiers exist.

**Verification:** A registered course with missing scope data fails clearly; `biology` does not crash; a valid 40-, 45-, 50-, 60- or 90-minute course is checked against its own allocation. No course is called checked on zero required records.

### 2. Pairwise availability tables do not yet form a shared grade calendar

**Severity:** Serious for timing certainty; moderate for assessment concentration  
**Confidence:** Firm on arithmetic and overlap; judgment call on acceptable workload  
**LAYER:** process, frame  
**REPEAT:** yes for timing and workload conflicts; this finding concerns the missing shared calendar rather than reopening corrected pairwise citations.

**Locations:** Grade 4 science frame, lines 9 to 12 and Cross-subject; all eight Course-level checks sections; grade 9 ELA Writing load; Biology Writing load; World History I Days bullet.

Grade 4 science combines three different statements:

- 120 sessions;
- four sessions weekly across 30 weeks;
- science session `n` near school day `4n/3`.

Four weekly sessions in an uninterrupted five-day school week imply approximately `5n/4`. The stated `4n/3` instead spreads 120 sessions over 160 school-day positions, averaging 3.75 sessions weekly. Either arrangement can work, but they are different calendars. The unspecified science-free weeks determine which cross-subject dates are true.

The whole-grade time calculation is:

| Grade | Core classroom time |
|---|---|
| 4 | 190 minutes without science; 235 with science |
| 4, a week containing four science sessions | 1,130 minutes, averaging 226 daily |
| 4, annual total | 35,800 minutes; 223.75 per position across a 160-day course calendar |
| 9 | 145 to 150 minutes plus the unstated World History I block |
| 9, if history uses 50 minutes | 195 to 200 minutes daily |

These are core-subject totals, not complete school-day budgets.

Assessment concentration also survives the writing-product staggering:

- Grade 4 math, ELA and social studies place their final cumulative assessments on course days 157 and 158. Science’s existing conversion places its final assessment sessions in approximately the same window.
- Grade 9 Biology, ELA and World History I each place three assessment periods in the final five-day block. Algebra I adds two, producing **11 cumulative assessment periods in week 32**.
- The grade 9 process-piece calendar usefully separates weeks 24, 26, 27 or 28, and 30. It does not resolve the final assessment concentration.

**Why it matters:** A dependency can be described correctly in two frames yet fail under the actual timetable. The same teacher or student experiences all four subjects’ assessments, not each frame separately. The [science standards’ mathematics connections](https://www.nationalacademies.org/read/18290/chapter/18) support keeping quantitative demands in step; they do not establish an acceptable number of assessments weekly.

**Exact fix:**

Add this requirement to production step 3:

> Before individual day sequences are finalized, write one numbered grade calendar showing all four core subjects, their minutes, subject-free days, cumulative assessments and major product deadlines. Map subject sessions to calendar positions explicitly. Check prerequisite availability against this calendar, retaining a local bridge wherever completion is not guaranteed. Identify assessment concentrations for review rather than treating separate subject totals as proof of a workable grade.

Replace grade 4 science’s conversion sentence with:

> Science has 120 sessions in 30 weeks containing four sessions each. Their school-day positions are set by the shared grade calendar, including weeks without science. Cross-subject dates are generated from that calendar.

Apply the same correction to the neighbouring science frames that use the same conversion.

Add a minutes-and-frequency sentence to World History I’s Days bullet. **Proposed audience assumption for Cory:** 50 minutes, five times weekly.

The calendar must explicitly resolve the final assessment window. Retain response time and ensure each assessed skill has been taught. Do not silently shorten assessments, combine independent products or add days.

**Verification:** Recalculate every sampled same-year dependency and display all four subjects’ assessment periods together. The grade 4 conversion must reproduce the chosen weekly schedule.

### 3. The frame gate verifies a smaller contract than the review brief implies

**Severity:** Serious  
**Confidence:** Firm, directly reproduced  
**LAYER:** gate  
**REPEAT:** yes, this is the requested prevention analysis of recurring band-read defects.

**Locations:** `scripts/frame.py:100` to `:155`; `scripts/progression.py:121` onward; `scripts/stale.py:69` onward; baseline brief’s statement about what the gates prove.

Three deliberate changes made only in memory still returned zero frame failures:

| In-memory change | Result |
|---|---|
| Remove every contribution code from grade 9 ELA’s standards column | Pass |
| Empty grade 4 math’s Seams, Models carried and Cross-subject bodies, retaining headings | Pass |
| Remove Biology’s course-level assessment table, retaining its heading | Pass |

The frame gate deliberately removes `~` codes before comparing standards. Consequently, its standards comparison does not protect the grade 9 ELA standard lists. It checks the existence of the other headings, not their contents. Its day calculation verifies that unit totals do not exceed the year, then labels the remainder as available time; it does not establish that the stated assessment and response allocations consume that remainder.

The existing gates have useful, narrower responsibilities:

| Gate | What it establishes | Important boundary |
|---|---|---|
| Frame | Skill placement, fully owned code lists, unit counts, upper day bound, summary agreement | Does not establish complete teaching, contribution coverage or populated seams |
| Progression | Known codes, ownership by grade, reciprocal handoff references, model availability by grade, cross-subject grade timing | Does not establish increasing depth or within-year availability |
| Stale | Recognized pending markers and a limited phrase list | Does not detect general factual or policy drift |
| Plan | Detailed declared parts, items, arithmetic, timing and cross-day records | Does not independently establish that the declared parts exhaust the original standard |

**Why it matters:** Readers can reasonably interpret “the gates already prove” as stronger assurance than the code supplies.

**Exact fix:**

Replace that sentence in `baseline-1.md` with:

> The gates establish the coded placement and reference checks they implement. They do not establish full standard meaning, within-year availability, assessment completeness or the accuracy of unmarked status prose.

Then add the following inexpensive checks:

| Repeated defect | Evidence from earlier fixes | Cheapest useful rule |
|---|---|---|
| Lost contribution codes | Grade 9 and 10 ELA depend on explicit partial contributions | Compare signed contribution codes as well as owned codes against each unit’s placed rows |
| Missing assessment or response allocation | Frame-writing lesson 1 requires counted response time | Require populated assessment rows with separate numeric assessment, response and review allocations; reconcile these with the course remainder |
| Missing model or handoff account | Frame-writing lessons 5 to 7; social studies and science readiness fixes | Require every relevant progression model and handoff identifier in the appropriate frame section; check declared unit order |
| Missing cross-subject lean | Cross-subject fixes repeatedly repaired availability records | Require every progression lean’s reference in the receiving frame’s Cross-subject section |
| Source lessons silently omitted | Source maps carry keep, merge, split and cut decisions | At scope stage, compare mapped source identifiers with the named source inventory, including explicit cuts and reasons |
| Incomplete standard meaning | Math money and angle fixes; science clarification and dimension fixes | Require a sourced element checklist and teaching/assessment locations at the appropriate planning stage; a reader still judges whether those locations fulfill the element |
| Reused texts or cases | ELA fixes moved repeated authors, texts and topics | Compare stable text or case identifiers; flag repeats unless a different purpose is recorded |

One current sampled example demonstrates the cross-subject omission: `s4-energy-resources` names `math:4.NBT.A.2`, but the science frame’s Cross-subject section does not contain that reference.

Add this row there:

| Other subject | Need | Receiving unit | Availability | Bridge |
|---|---|---|---|---|
| Math grade 4 | 4.NBT.A.2, reading state energy data | Science unit 2 | Math unit 5, days 58 to 76, later under the current draft | Student graphs use shares out of 10 and whole-number labels within 1,000 until math teaches larger numbers |

**Verification:** The three in-memory omissions above must produce specific failures after the gate changes. Presence checks must remain explicitly distinct from evidence that teaching is complete.

### 4. Current review-role policy has not reached the active course contracts

**Severity:** Serious  
**Confidence:** Firm  
**LAYER:** process  
**REPEAT:** yes for stale dependencies; the controlling policy change is dated 2026-11-14.

**Locations:** `docs/FOUNDATION.md:123` to `:140`; sampled frames’ Sensitivity reads and For the lead sections; particularly grade 4 math, grade 4 science, Biology and World History I.

The foundation now assigns answer-key, safety and community-informed content reads to fresh specialist agents that study sources first. It explicitly records the 2026-11-14 change from the former outside-reader requirements.

The active frames still impose the former completion conditions:

- Grade 4 math requires a qualified math content reviewer.
- Grade 4 science requires a science teacher’s safety read.
- Biology requires outside specialist and community readers.
- World History I requires qualified community readers before several units ship.

The stale gate passes these statements because they do not use its recognized pending syntax.

**Why it matters:** Writers inherit conflicting requirements about who must read a unit and what blocks completion. This also creates obsolete questions about finding people and paying them.

**Exact fix:**

Replace each frame’s general review-role rule with:

> Review roles and completion requirements follow FOUNDATION section 7.3, revised 2026-11-14. The answer-key, safety and sensitivity agents perform the content reads assigned there, each cold and after studying the required sources. The course-specific cases and source requirements below remain binding.

Then change the affected assignments individually:

- Math content reviewer → answer-key agent.
- Science teacher’s safety/materials read → safety agent.
- Community content reader → sensitivity agent studying that community’s own published materials.
- Preserve the named pilot teaching and student trials, rights read and Spanish-language requirements that the foundation retains.

For example, Biology unit 9’s requirement becomes:

> Before this unit ships, the sensitivity agent studies the Lower Elwha Klallam Tribe’s own published account and checks the description of the Tribe and its role against it.

Remove the corresponding obsolete reader-recruitment questions from active frames. Preserve dated review reports as history.

**Verification:** Scan active course contracts after a foundation policy change. A clean pending-marker check alone must not be reported as policy alignment.

### 5. The glossary describes a different unit ending from the frames

**Severity:** Moderate  
**Confidence:** Firm  
**LAYER:** process, frame  
**REPEAT:** new for the shared unit-boundary contradiction.

**Locations:** `docs/GLOSSARY.md:38`, `:40`, `:43`; `docs/courses/UNIT-PLAN.md:14`, `:149`; sampled frames’ Days bullets and assessment allocations.

The glossary says the end-of-unit assessment occurs on the unit’s last day and defines a teaching day separately from assessment and response days. The frames call their complete allocations “teaching days,” including assessments and response.

Grade 4 math explicitly includes a full assessment day and a subsequent respond day within each unit. The older unit template instead assumes a respond half within the assessment day. Its marking-and-response fields therefore describe a different boundary and timing model.

The glossary also retains a grade 4 unit-length example of 3 to 15 days, while the current frame contains a 22-day unit.

**Why it matters:** A writer can count response twice, omit it, or put the assessment after the day reserved to act on its results.

**Exact fix:**

Replace the glossary’s unit definition with:

> A run of course days on one block of standards. Readiness is checked before the new work; an end-of-unit assessment checks what was taught; planned response follows. The frame and scope and sequence set its length.

Replace the assessment definition with:

> The assessment near the end of a unit, on every part of every standard it teaches. It is followed by the response time named in the plan, within the same day or on later respond days.

Add these definitions:

| Word | Definition |
|---|---|
| **course day** | One numbered allocation in the course, including teaching, assessment, response or review |
| **course-level check** | A cumulative assessment across units; distinct from an end-of-unit assessment |
| **check set** | The external standards or frameworks used to compare planned coverage; not a student assessment |
| **lean** | A cross-subject connection, identified as a prerequisite or a context connection |
| **bridge** | Local teaching or support that permits the receiving task before the other subject supplies the needed skill; its time is included |

Change the frames’ opening allocation wording from “160 teaching days” to “160 course days,” and likewise for other totals.

Rename the unit template’s “respond half” field to **Response allocation**, with this instruction:

> Name the marking time and the response time separately. State whether response occurs within the assessment day or on later respond days, and count it once.

**Verification:** Each unit’s teaching, assessment and response allocations must reconcile with its days. Neither assessment placement nor response duration is inferred from the word “end.”

## Sampled subject-column conclusions

These conclusions concern the sampled seams, not an exhaustive K to 12 content audit.

| Subject | Climb and checks | Shape, selections and base use |
|---|---|---|
| Math | Grade 3 facts and fraction representations support grade 4 algorithms and fraction operations; grade 5 extends denominators, decimal operations and multiplication fluency. Algebra I hands coordinate and quadratic work to Geometry and explicitly reactivates skipped threads later. | The sampled source maps explain splits, merges and cuts. Different unit counts have reasons. Preserve those decisions. |
| Science | Grade 3 defines design problems, grade 4 compares solutions, and grade 5 plans fair prototype tests. Biology extends middle school models and hands quantitative energy and carbon work to Chemistry. Checks generally require unfamiliar cases. | Grade 4’s six-unit, 120-session form matches its neighbours. Its calendar conversion, rather than its unit count, needs correction. |
| ELA | Referring and inferring in grade 4 rises to accurate quotation and several accounts in grade 5. Grade 9’s supported evidence work rises to longer works and greater independence in grade 10, including an explicit independent reading endpoint. | Grade 4’s replacement texts preserve the base sequence’s instructional purposes. Grade 9’s selections and the proposed recent-long-text alternative remain the previously recorded scope question. |
| Social studies | Grade 4 adds purpose, audience and source independence; grade 5 requires less prompted sourcing. World History I develops interpretation and argument before World History II’s contested inquiry and sustained research. | The broad regional and chronological spread is visible in the sampled frames. Recurring historical content is generally given a stated deeper purpose. No additional relocation of standards is recommended. |

The existing same-year bridges are valuable. ELA’s animal texts supply their own background before science’s structures unit; Biology supplies its population rule before Algebra I’s exponential unit; history teaches its own sourcing and early claim routines. Shared literacy responsibility supports this disciplinary teaching rather than requiring every skill to originate in ELA. See the [ELA standards’ design considerations](https://www.thecorestandards.org/ELA-Literacy/introduction/key-design-consideration/) and [science literacy connections](https://www.nationalacademies.org/read/18290/chapter/19).

## Settled by the expert

| Choice | Reason | Files affected |
|---|---|---|
| Canonical course identity is the frame slug; catalogue identity remains separate | A band identifier cannot identify one year’s plan | `frames.csv`, frame headers, planning and status scripts |
| Preserve existing catalogue identifiers and an explicit `math-4` legacy alias | Avoid unrelated catalogue migration | Same files |
| Correct production counts without changing scope | Current enumeration has 58 courses in the four subjects, of which 52 are flagged core; 49 courses outside those subjects make 107 total, with 55 outside the flagged core set | `PRODUCTION-PATH.md`, plan-flow explanatory text |
| Use “course days” for complete allocations | Distinguishes the total from the teaching-day kind | Glossary, frames, briefs |
| Allow same-day or later response, explicitly counted | Accommodates the current frames without forcing the old half-day pattern | Unit template and checks |
| Add the missing energy-data availability row and earlier-number bridge | Closes the sampled coded-lean omission without moving a standard | Grade 4 science frame |
| Apply the current foundation’s review roles | Cory has already settled the policy | Active frames and planning briefs |
| Preserve the sampled unit orders and progression ownership | This read found structural handoff problems, not grounds for a curricular redraw | No unit or ownership changes |

For production step 2, replace the course-count sentence with:

> The 52 courses currently flagged core in the four subjects receive frames in this stage. Six additional courses in those subjects remain non-core and follow the core work.

Replace references to “the 49 non-core courses” with:

> The 55 courses outside the flagged core set follow the core work: 49 outside the four subjects and six non-core courses within them.

## What should remain

Keep the reciprocal seam records, explicit dormant-skill reactivation, unfamiliar assessment cases, discipline-specific bridges, source-map reasons and separate writing deadlines. These are substantive improvements from the band reads.

Keep source inventories and manuscripts at their settled production stages. This review does not reinstate the rejected demand to finish original texts before a frame closes.

## For Cory

1. **Audience and timetable:** Confirm the classroom block assumptions together. Grade 4 currently requires 190 core minutes without science and 235 with it. Grade 9 needs a stated history block; 50 minutes would bring its core total to 195 to 200 minutes.
2. **Audience and calendar:** Confirm the science scheduling profile and whether concentrated final assessment windows are acceptable. The shared calendar should show a concrete proposed arrangement before this decision.
3. **Existing scope question:** Grade 9’s recent long-text alternative remains the question already recorded in its frame. This review adds no recommendation to change its scope.

No new expenditure, outside-reader recruitment or site change is proposed.

## Sources and limits

- [Science standards, mathematics connections](https://www.nationalacademies.org/read/18290/chapter/18): checked the rationale for keeping mathematical demands aligned and distinguishing disciplinary argument.
- [Science standards, literacy connections](https://www.nationalacademies.org/read/18290/chapter/19): checked disciplinary reading, writing and evidence demands.
- [ELA standards, design considerations](https://www.thecorestandards.org/ELA-Literacy/introduction/key-design-consideration/): checked shared responsibility, integrated tasks and high school grade bands.
- [New York social studies framework introduction](https://www.nysed.gov/common/nysed/files/programs/curriculum-instruction/ss-framework-k-12-intro.pdf): consulted the inquiry and disciplinary-literacy explanation. The direct national inquiry-framework PDF returned 403; no finding depends on having read that PDF in full.

No curricular finding rests on memory. Source-map structure and arithmetic were examined, but this was not another lesson-by-lesson base-text audit. Instructional timing remains untested with students. The already recorded disciplinary-literacy inventory gap is not counted again here.

**Final verdict: coherent curriculum structure, with production handoff corrections required. Findings: 5. Report destination: `docs/reviews/baseline-1-codex-2026-11-14.md`, supplied here only and not written.**
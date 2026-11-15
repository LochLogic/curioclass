# Independent scope and sequence review: English Language Arts, Grade 2

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/sequence-english-language-arts-grade-2-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files were created, edited or deleted.

## Verdict

Revise before treating this sequence as settled: the four-unit structure, instructional arcs and allocations are defensible, but several assessment descriptions do not establish the complete performances their codes claim. The largest unresolved dependency is the replacement texts, whose actual difficulty, length and suitability remain unverified. Preserve the unit order and totals while repairing assessment evidence, placing dictionary instruction explicitly, completing text records and specifying the shorter-period route.

## What I read

- `docs/agents/EXPERT.md`, the ELA lens, `docs/RUBRIC-ELA.md`, the foundation, shared and ELA approaches, relevant source-register notes, glossary, BASELINE rules and roadmap sections.
- The complete grade 2 scope and sequence, all 160 day records and the course frame.
- All 30 grade 2 progression rows, their 31 distinct grade 1 prerequisites and those prerequisites’ placements in grade 1 day records.
- The full grade 2 standards, including lettered parts, in `data/standards/ccss-ela-standards-full.txt`.
- `docs/courses/CALENDAR.md` and every grade 2 subject’s calendar rows.
- All 15 grade 2 entries in `data/plans/ela-texts.csv`.
- The 349-row source map, its lesson placements, decisions and referenced archive members.
- The K to 2 frame-fix disposition, earlier kindergarten and grade 1 ELA sequence reports, relevant sequence-writing rules and the base-text register.
- Outside sources linked below.

The prohibited files were not opened. Prior-session memory informed review format and scope discipline only. No course-specific finding rests on memory.

## Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | This course reported **0 failures**; the repository-wide run subsequently stopped elsewhere because the `markdown` module is missing. |
| `python -X utf8 scripts/frame.py calendar` | Completed; grade 2 ELA checks occupy weeks 15 to 16 and 32, with no reported stagger-rule break. |
| `python -X utf8 scripts/frame.py check english-language-arts-grade-2` | Passed: four units, 160 days, including 154 unit days and six course-level days. |
| `python -X utf8 scripts/stale.py check` | Passed: 56 files checked, 0 failures. |

The interrupted repository-wide gate does not withhold or determine this verdict.

## Findings, most serious first

### 1. Several assessment claims exceed their named evidence

**Severity:** High  
**LAYER:** sequence  
**REPEAT:** yes, assessment-to-standard mismatches recur in the earlier kindergarten and grade 1 ELA sequence reports  
**Confidence:** firm on the performance mismatches; likely on the cumulative-record clarification

**Locations:** `days.csv`, days 11, 18 to 19, 30 to 31, 75 to 76, 113 to 115, 118 and 158; corresponding assessment paragraphs.

The assessment contract says that codes identify evidence reserved for the task. These placements need correction:

| Location | What is wrong | Exact fix |
|---|---|---|
| **Text-question assessments, especially days 11, 18 to 19 and 76** | The named work emphasizes answering questions. Covering six question words does not explicitly collect the **asking** component of `RL.2.1` and `RI.2.1`. The recurring speaker-clarification protocol addresses a related speaking standard but does not clearly reserve student-generated reading questions. | Add a brief student-generated, text-dependent question and a supported answer for each text kind. Model and practise this during the school-story and school-article work before assessment. Keep the six-question-word coverage across the assessment. |
| **Unit 1 closing window, days 26, 30 and 31** | The prose promises literary and informational question evidence. Day 30 lists `RI.2.1`; day 31 lists character response and illustrations but omits `RL.2.1`. No closing note explicitly retains the earlier literary-question evidence. | Add `RL.2.1` to day 31 and name its asking-and-answering performance, or explicitly incorporate the completed day 11 evidence into the closing record and confirm any missing component. |
| **Poster observations, days 113 to 115** | These rows list `SL.2.4`, but the named performance is an informational research presentation. That does not necessarily constitute telling a story or recounting an experience. The later recorded stories do provide the required performance. | Remove `SL.2.4` from these poster rows. Retain their research and complete-sentence evidence, and complete `SL.2.4` through the stories on days 117 and 118. |
| **Course checks, days 75 and 158** | Full fluency codes are listed, but the directions describe reading fresh text without explicitly reserving successive oral readings for `RF.2.4b`. A single cold reading cannot demonstrate that component. | Name an initial oral reading and a short successive reading within each child’s conference rotation. Record accuracy, appropriate rate and expression, with understanding and monitoring evidence alongside them. |
| **Unit 3 foundations completion** | The prose says `RF.2.3b` finishes here, but the closing decoding row names only `RF.2.3c`. The additional vowel-team evidence is distributed among cycle checks without an explicit completion reference. | On day 118, explicitly retain the relevant cycle-check evidence, including days 42, 62 and 112, to close `RF.2.3b`. Use the existing response slot for any missing or insecure pattern rather than adding another assessment day. |

The [Common Core standards](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf) distinguish asking from answering, storytelling from informational reporting, and successive oral reading from a single reading.

**Why it matters:** A writer could follow the current descriptions faithfully and produce incomplete evidence while recording complete codes.

Keep the existing assessment windows and response allocations. These repairs clarify performances and records without changing ownership or adding days.

### 2. Replacement-text records remain provisional beyond their agreed completion point

**Severity:** High  
**LAYER:** frame  
**REPEAT:** yes, the grade 2 frame disposition accepted text records with the scope and sequence; the same unresolved dependency appears in the earlier kindergarten and grade 1 sequence reports  
**Confidence:** firm

**Locations:** Scope and sequence, text-record table and “For the lead” item 2; frame, “For the lead” item 3; `data/plans/ela-texts.csv`.

The sequence provides useful intended demands and supports, but expressly identifies the texts as unwritten. The catalogue contains **12 entries marked `to write` and three marked `to choose`**, with blank rights-basis and rights-check fields throughout.

Several entries represent collections rather than inspectable individual texts. Both source tellings for the fable comparison need identification, and the cultural tales still require documented provenance. Consequently, the review cannot establish that the actual texts supply the planned paragraph structure, contrasting versions, reasons, illustrations, sound effects or reading load.

The accepted frame disposition put text records **with the scope and sequence**. The sequence instead defers essential completion to unit planning. The [K to 2 review criteria, indicators 2b and 2c](https://cdn.edreports.org/reviewtools/ela/2.1/ELA-Grades-K-2-v2.1-Tools_Review-Criteria.pdf) call for documented complexity and supports matched to the actual text.

**Why it matters:** Replacing the base books changes the material that makes its instructional sequence work. Intended features cannot establish that the replacement supports the assigned teaching and assessments.

**Exact fix:**

1. Give each constituent selection a stable identifier and manuscript or source location.
2. Complete records covering actual length, reading role, qualitative demands, reader/task fit, placement reason, matched supports and rights status.
3. Complete the replacement manuscripts needed to substantiate those records. Measure prose where meaningful; retain an explicit explanation where a measure is unsuitable.
4. Identify both public-domain fable tellings and document the cultural tales’ sources and attribution limits.
5. Put the settled original-poem and song choices into the catalogue.
6. Retain the required text and sensitivity reads before use.

Do not invent measures for unwritten texts or reopen the rejected demand for a finished inventory before the frame. This finding concerns the agreed scope and sequence completion point.

### 3. Beginning-dictionary instruction lacks a teaching-day placement before its first assessment

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** new  
**Confidence:** likely

**Locations:** Unit 1 foundations paragraph; `days.csv`, days 26 to 30.

The prose reserves dictionary use during days 26 to 32. The day records, however, first explicitly name dictionary use on **day 30’s assessment**. Earlier flexible foundations notes name mapping, blending, matched reading, spelling and rereading, without placing the dictionary model or guided practice.

The grade 1 spelling prerequisite does not itself establish this new reference-material routine. `L.2.2e` requires checking and correcting spelling, not merely opening a dictionary. See the [grade 2 language standards](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf#page=27).

**Why it matters:** A writer working from the daily map could introduce the procedure during the observation intended to assess it.

**Exact fix:** Use ten minutes of day 27’s flexible foundations block to model locating an entry, comparing spellings and correcting a draft word. Give guided practice on day 28 and a brief independent application on day 29. Make day 30 explicitly observe both checking and correction.

This uses existing flexible time and adds no day.

### 4. The shorter-period paragraph does not specify a shorter instructional route

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, the same specification gap appears in the grade 1 ELA sequence report, finding 4  
**Confidence:** firm on the missing specification; judgment call on the eventual minimum allocation

**Location:** “Shorter path,” first paragraph.

The paragraph offers sensible priorities but supplies neither a shorter daily duration nor component minutes. Retaining both blocks somewhere within the same school day can preserve the full 120 minutes without establishing a shorter-period option.

Its warning that a substantially shorter period needs a time-allocation decision is honest. It also leaves the brief’s shorter-period requirement unresolved.

**Why it matters:** A teacher cannot determine whether the course fits an available timetable or where displaced instruction goes.

**Exact fix:** Supply a proposed shorter allocation with ordinary-day and assessment-day budgets. Name the retained explicit teaching, matched reading, topic reading, discussion, writing, grouping and response time, and identify how any displaced work fits elsewhere.

Cory must settle the supported recurring allocation because that changes the course’s time assumptions. Until then, label the paragraph as an occasional-short-day contingency and mark the recurring shorter-period route unresolved.

Preserve the much more concrete ten-day-shorter-year plan.

### 5. Week 32 falls below the promised discussion frequency

**Severity:** Minor  
**LAYER:** sequence  
**REPEAT:** new  
**Confidence:** firm

**Locations:** Named discussion commitment; `days.csv`, days 156 to 160.

The sequence promises the named protocol at least twice each week, including assessment weeks. Week 32 contains only one explicit protocol placement, on day 157. The course checks and day 160 do not name a second discussion.

**Why it matters:** The daily map drops a stated instructional commitment precisely where assessment work can crowd it out.

**Exact fix:** Reserve eight minutes on day 160, **after the unaided retry**, for “turn, pair, link, clarify” about the earlier school text. Students link a comment and ask or answer a clarifying question. Keep assessment evidence separate from this supported discussion.

## Order, coverage and days by load

The main arcs build appropriately:

- Unit 1 completes the school story before its first assessment and supplies article reading and a paragraph model before the informational book.
- Unit 2 teaches story structure, word strategies, grammar and sentence work before the assessed narrative. Practice writing precedes the new narrative, with revision and editing separated.
- Unit 3 moves from process reading to shared research, independent gathering, paragraph writing, posters and recorded stories.
- Unit 4 establishes recounting before version comparison, and author reasons before opinion writing.

| Unit | Days | Owned rows | Base topic lessons | Base foundations lessons | Assessment-bearing days |
|---|---:|---:|---:|---:|---:|
| Schools and community | 32 | 8 | 30 | 25 | 6 |
| Fossils | 42 | 11 | 39 | 35 | 8 |
| Pollination | 41 | 5 | 38 | 35 | 9 |
| Providing for pollinators | 39 | 6 | 36 | 35 | 9 |

No allocation is demonstrably far over or under its load. Unit 2 carries the heaviest new language and narrative load; units 3 and 4 also carry substantial continued foundations, research, performance and writing work. Assessment-bearing days retain other instruction and should not be counted as that many full-day tests.

All lettered parts have identifiable intended coverage. Findings 1 and 3 concern whether the day map actually reserves the complete performance or teaching placement.

## Other required checks

| Requirement | Judgment |
|---|---|
| **Readiness versus retrieval** | All **31 distinct assumed rows** were used in grade 1, confirmed against progression and grade 1 day placements. Retrieval is correct. No older prerequisite requiring readiness was found. |
| **Misclassified units** | None. No unit checks a year-before row as readiness, retrieves an older unrefreshed row, or places a readiness check on its first day. |
| **Retrieval timing** | Unit 1 retrieves on days 1 and 16; unit 2 on day 33; unit 3 during days 77 to 78, 84, 88 and 104; unit 4 on days 119 and 132. Earlier same-year learning also returns appropriately. |
| **Mid-unit assessments** | Present in all four units, each longer than 25 days. |
| **Response counted once** | Topic responses and foundations cycle responses occupy separately identified blocks. No duplicate day charge found. |
| **Checks avoid immediate repetition** | Explicitly met. Both course checks use earlier school content for recently taught skills rather than repeating fossil or pollinator assessments. |
| **Calendar** | Checks on days 75 to 76 and 158 to 159 match the current target weeks. Nearest ELA/math check separations are 14 and 13 school days. No stagger-rule break. |
| **Same-year leans** | Science bridges are placed on days 78 and 88. Cultural introductions occur on days 119, 123 and 124. Earlier social studies comparison and sourced-claim work precede their ELA uses. |
| **Candidate cells** | All four are settled as kept, with assessment and response costs inside their allocations. |
| **Shorter year** | Ten named fold-in days produce 150 meetings. Every folded row has blank `assess`, and none contains an embedded cycle check. The notes preserve first teaching and the assessed work. |
| **Source map** | All 143 topic lessons and 130 foundations lessons are represented in source order. The revision/editing split is explained. All 315 source references resolve; the other 34 rows are Curio Class additions. |
| **Other source decisions** | All 26 decodable entries and 16 omitted Labs stage guides are accounted for. The Labs cut has a stated time rationale. |
| **Stale notes beyond the gate** | The frame still contains superseded readiness wording and approximate cross-subject timing. The sequence correctly flags these for separate correction. Its own retrieval and bridge decisions should stand. |

The source-map check establishes inventory and placement, not the fidelity of every adapted lesson body.

## ELA lens checklist: scope and sequence

| Checklist line | Status | Evidence |
|---|---|---|
| Text demand climbs, or its order is justified | **Planned, not demonstrated** | Increasing independence and harder student-read texts are specified; actual selections and completed records remain unavailable. |
| Research and full-process writing recur | **Met at planning level** | Sustained shared research in unit 3, provided-source gathering returning in unit 4, and multiple process-writing products. |
| Discussion occurs frequently | **Mostly met** | Named routine throughout the year; finding 5 repairs week 32. |
| K to 2 phonics sequence connects to decodable reading | **Met at planning level** | Cycle order, pattern teaching before matched reading, spelling, rereading and checks are explicit. Actual adapted word eligibility remains to be verified. |

Finished question percentages, scoring guidance and classroom execution cannot be judged at this layer.

## Settled by the expert

These are item-level recommendations for the caller to apply.

| Choice | Reason | File affected |
|---|---|---|
| Keep the four units, order and current allocations | Instructional arcs and unequal loads support them. | Frame and sequence |
| Keep retrieval for all 31 grade 1 prerequisites | Their last-use grade is 1. | Frame wording and sequence |
| Add student-generated text questions to the named reading assessments | Completes asking as well as answering. | Days and assessment prose |
| Complete `SL.2.4` through recorded stories; remove it from informational poster observations | Preserves the required performance without another task. | Days 113 to 118 |
| Name successive oral readings in course-check conferences | Makes the fluency evidence explicit. | Days 75 and 158 |
| Close additional vowel-team evidence through named retained cycle records | Avoids an unnecessary additional test. | Day 118 |
| Model dictionary checking on day 27, practise on days 28 and 29, assess correction on day 30 | Places instruction before scored use. | Unit 1 day notes |
| Add the second week 32 discussion after day 160’s unaided retry | Meets the stated frequency without contaminating assessment evidence. | Day 160 |
| Preserve the ten named fold-ins and existing bridges | They protect assessment, foundations order and access to needed content. | Sequence and days |

The accepted foundations ownership convention remains unchanged: opening ownership with explicit continued teaching and appropriately bounded checks.

## What should remain

Preserve the whole school story, explicit foundations beside rich topic reading, sound-based word mapping, matched decodables, the prohibition on guessing, separate revision and editing, independent versus supported reading records, and individual digital-contribution records.

The foundations design broadly accords with the [federal foundational-reading guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/21), including explicit decoding and daily connected reading. That support does not validate the unwritten texts or the proposed classroom timing.

## Sources and limits

Outside sources consulted during this read:

- [Common Core ELA standards](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf): grade 2 requirements and distinctions between performances.
- [K to 2 review criteria](https://cdn.edreports.org/reviewtools/ela/2.1/ELA-Grades-K-2-v2.1-Tools_Review-Criteria.pdf): relevant foundations, text-complexity, discussion, writing, research and assessment indicators. No numerical rubric score was assigned.
- [Federal foundational-reading guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/21): recommendation summary, consulted in part.
- [K to 2 publishers’ criteria](https://tools.achievethecore.org/content/upload/Publishers_Criteria_for_Literacy_for_Grades_K-2.pdf): relevant foundational-reading and text guidance, consulted in part.
- [Core Knowledge skills scope and sequence](https://www.coreknowledge.org/wp-content/uploads/2017/03/CKLA_K2_Skills_ScopeSequence.pdf#page=43): limited grade 2 comparison of review, spelling, reading and writing placements. Its full program was not reviewed.

The live base-curriculum grade page and attempted year-at-a-glance PDF did not open successfully. Local archive inventories were checked, but source lesson bodies were not reread comprehensively; local PDF extraction was unavailable.

I could not judge finished text quality, cultural representation, actual decodable word inventories, completed assessment items, scoring consistency or classroom throughput. No substantive conclusion rests solely on memory.

**For the source list:** The linked K to 2 criteria and alternate publishers’ criteria address opened successfully. The linked Core Knowledge document provides an additional limited comparison source.

## For Cory

- **Scope and instructional time:** Set the recurring shorter daily allocation the course should support, or retain 120 minutes as its minimum and explicitly leave that shorter-period requirement unresolved. The existing 120-minute decision does not need reopening for the full path.

**Verdict: Revise before treating the sequence as settled. Findings: 5. Intended report path: `docs/reviews/sequence-english-language-arts-grade-2-2026-11-14.md`, delivered here, not written.**


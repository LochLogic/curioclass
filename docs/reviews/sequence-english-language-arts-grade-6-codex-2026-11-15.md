# Independent scope and sequence review: English Language Arts Grade 6

**Date:** 2026-11-15  
**Role:** First independent reader, before the expert, following the supplied blind rule.  
**Intended report path:** `docs/reviews/sequence-english-language-arts-grade-6-2026-11-15.md`  
**Delivery:** Complete report supplied here. No report file was written.

## Verdict

Revise before unit planning. The six unit arcs, prerequisite retrieval and cumulative-check placement are coherent, but several assessment claims and standard components remain insufficiently specified. Align the named evidence with the claimed standards first, then correct the text accounting and stale instructions.

**Finding count: 6.**

## What I read and checked

- The complete [scope and sequence](/S:/CurioClass/docs/courses/english-language-arts-grade-6/scope-and-sequence.md), all 160 rows of [days.csv](/S:/CurioClass/data/plans/english-language-arts-grade-6/days.csv), and the complete course frame.
- Grade 5, 6 and 7 rows in `data/progressions/ela.csv`, with grade 5 day placements checked for incoming prerequisites.
- `docs/courses/CALENDAR.md` and every grade 6 row in `data/plans/calendar.csv`.
- All grade 6 records in `data/plans/ela-texts.csv` and the complete grade 6 standard text.
- `EXPERT.md`, the ELA lens, `RUBRIC-ELA.md`, foundation, shared and ELA approaches, relevant roadmap sections, glossary, BASELINE rules 20 to 24, and relevant source-register entries.
- Permitted earlier grade 3 and grade 5 sequence-review passages for repeat classification.
- Outside standards, review guidance, research guidance and comparison curriculum maps linked below.

No prohibited course or review file was opened. Memory supplied general review-method reminders only; no course finding rests on unverified memory.

### Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Reported zero sequence failures for this course, then stopped later because Python lacks `markdown`. |
| `python -X utf8 scripts/frame.py calendar` | Passed; grade 6 ELA checks occupy weeks 12, 22 and 32. |
| `python -X utf8 scripts/frame.py check english-language-arts-grade-6` | Passed, zero failures: 148 unit days and 12 course-level days. |
| `python -X utf8 scripts/stale.py check` | Passed, 56 files and zero failures. |
| `python -B -X utf8 scripts/sequence.py check english-language-arts-grade-6` | Passed, zero failures. |

The incomplete repository-wide gate does not prevent the curricular verdict.

## Findings, most serious first

### 1. Two assessment rows list standards their named evidence cannot demonstrate

**Severity:** Major  
**LAYER:** sequence  
**REPEAT:** yes, assessment-to-code mismatches occur in the earlier grade 5 independent sequence review, finding 1.  
**Confidence:** firm

**Location:** `days.csv`, days 110 and 132.

| Day | What is wrong | Exact fix |
|---|---|---|
| 110 | The course-level check lists W.6.6, but specifies sentence editing and an informative paragraph with a chart. It names no publishing, collaboration or three-page keyboarding evidence. | Remove W.6.6 from this check row. Retain the explicitly collected evidence from days 78 to 79 and 81, with later application on day 149. |
| 132 | This is explicitly “End part 1,” using a play and its performance, but it lists W.6.9b alongside the literary response. No informational text or informational-response product is named. | Remove W.6.9b from this assessment row. Retain W.6.9a for the written reading-to-performance comparison. |

The [writing standards](https://www.thecorestandards.org/ELA-Literacy/W/6/) distinguish technology-based production and collaboration from ordinary composition, and literary evidence from informational evidence.

**Why it matters:** A writer could faithfully build these tasks and still record evidence that students never supplied. The general warning that ordinary teaching codes indicate practice does not resolve an assessment row’s unsupported claims.

These corrections require no new assessment or day.

### 2. The unit 2 mid-unit assessment precedes explicit teaching of part of RI.6.4

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, claiming a standard before its new demands are taught is also identified in the earlier grade 5 independent review, finding 2.  
**Confidence:** likely

**Location:** Days 35, 38, 45 and 47.

Day 35 names technical vocabulary and context or word parts. The first explicit task distinguishing figurative and connotative meanings in informational text is day 47. Day 45 already assesses RI.6.4 and says each listed reading demand is sampled.

The [informational reading standard](https://www.thecorestandards.org/ELA-Literacy/RI/6/) includes figurative, connotative and technical meanings. As written, day 45 either assesses the first two before their planned instruction or samples less than its complete code claim.

**Why it matters:** Mid-unit results could label an untaught demand as a learning failure.

**Exact fix:** Use the existing editorial reading on day 38 to model one figurative expression and one connotative choice in context. Apply both briefly during day 39’s rereading. Retain all three meaning demands on day 45, and make day 47 their application to the code. No day or ownership changes.

### 3. Unit 4 schedules roots but no explicit affix application

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** new  
**Confidence:** likely

**Location:** Unit 4 description; days 89 to 93, 99 and 106.

The sequence names roots such as `graph`, `gram`, `script` and `scrib`. “Affix” appears in the weekly vocabulary plan, but no day names students using a prefix or suffix to infer an unfamiliar word’s meaning. Day 106 reserves L.6.4a to d by code without resolving this missing branch.

[L.6.4b](https://www.thecorestandards.org/ELA-Literacy/L/6/) includes both affixes and roots as meaning clues. Grade 5 instruction supplies a useful inventory, but the grade 6 unit still needs an identifiable application at its own text demand.

**Why it matters:** A unit writer could deliver every named root activity while omitting affix-based inference.

**Exact fix:** Add an affix-and-root inference to day 90, using actual booklet words. Retrieve a familiar prefix and derivational suffix, combine their clues with a root, and verify the inferred meaning in context. Repeat with an unfamiliar example on day 99 and explicitly reserve an affix application within day 106’s L.6.4b prompt. This replaces part of existing word work.

### 4. The unit 5 end task leaves word choice’s effect on meaning implicit

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, incomplete assessment coverage is the same finding type as the earlier grade 5 independent review, finding 1.  
**Confidence:** likely

**Location:** Frame unit 5; scope and sequence unit 5; days 114, 118 and 134.

Day 114 models a word choice’s effect on tone. Day 118 tests an interpretation against word choices, but day 134’s explicit assessment specification again names only “word impact on tone.”

[RL.6.4](https://www.thecorestandards.org/ELA-Literacy/RL/6/) requires analysis of the effect on meaning as well as tone. Determining a figurative meaning and identifying a tone do not necessarily show how a particular choice changes what the reader understands.

**Why it matters:** The end task could omit a required part even though the parent code appears.

**Exact fix:** On day 114, model how replacing a selected word changes both the understood action or idea and the tone. Apply that distinction on day 118. On day 134, require one combined explanation of the selected word’s contribution to meaning and tone, supported by the cold passage. Correct the frame’s unit 5 wording accordingly.

### 5. The anchor count excludes texts that carry required instruction

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, the earlier grade 5 independent sequence review identifies the same catalog-label denominator problem in finding 6.  
**Confidence:** firm

**Location:** Scope and sequence, line 162; text records and days 94, 121 to 122, 140 to 142.

The 23-text count excludes every record labelled `paired`. Yet the Sejong feature teaches idea development, the ice-storm story carries point-of-view and cross-form comparison, and the warning pages carry media integration. These are required instructional texts.

The [6 to 12 evidence guide, indicator 2a](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_6_12_Evidence_Guide_2_0_2068cea08f.pdf) defines core status through instructional use. Pairing alone does not establish exclusion.

**Why it matters:** The stated 52.2 percent informational share and whole-text/excerpt counts do not describe the complete instructional core.

**Exact fix:** Classify scheduled selections by instructional use, independently of `paired`. Include required core selections, unpack bundles consistently, and explain exclusions. Recount genre and length categories. Do not add texts merely to reach 55 percent, which is reported rather than separately scored.

### 6. Active frame and rubric notes still describe the superseded course

**Severity:** Minor  
**LAYER:** frame and process  
**REPEAT:** yes, stale readiness and evidence-status instructions occur in the earlier grade 5 independent review, finding 8.  
**Confidence:** firm

**Location:** Frame readiness paragraphs, writing-calendar typing line, paragraph following its course-check table and unit 6 Candidate cell; `RUBRIC-ELA.md` evidence-status column.

The frame still:

- Calls grade 5 pickups readiness tasks, including the two-page typing task.
- Says units 2, 4 and 6 use the following course-level check as their end-of-unit assessment.
- Places unit 6’s candidate cold end task in course-level check 3.

The sequence correctly uses retrieval, internal end assessments and transfer checks, and already identifies these frame corrections as outstanding.

The rubric’s evidence-status column still describes a 150-day plan, 13 writing pieces, six process pieces, three research projects and much less frequent formal discussion. The current sequence has 160 days, nine named pieces, three process pieces, two research projects and discussion gaps no greater than ten days.

**Why it matters:** Writers consulting these active references receive incompatible directions. The stale script does not detect these semantic contradictions.

**Exact fix:** Apply the frame corrections already named in the sequence. Replace the rubric’s historical evidence-status entries with current sequence references and retained limitations. Preserve its criteria and numerical bar.

## Other required judgments

### Order, load and assessment architecture

The counts below are newly owned progression rows, rather than every previously taught row reused in a unit.

| Unit | Days | New owners | Judgment |
|---|---:|---:|---|
| 1 | 32 | 10 | Whole novella and evidence work precede narrative production. Mid-unit assessment on 15, response on 16; portfolio and cold end evidence on 30 to 31, response on 32. |
| 2 | 26 | 5 | Argument tracing precedes argument writing. Mid-unit assessment on 45, response on 46; end evidence on 56 to 57, response on 58. Correct finding 2. |
| 3 | 24 | 3 | Research is modelled before the report, publication and talks. Products and observations are collected across 81, 83 and 84; response on 85. |
| 4 | 22 | 4 | Whole booklet reading precedes structural analysis; punctuation precedes short applications. End assessment on 106, response on 107. Correct finding 3. |
| 5 | 24 | 5 | Meaning and structure precede viewpoint, comparison and performance. End evidence on 132 and 134, response on 135. Correct finding 4. |
| 6 | 20 | 2 | Account comparison precedes media integration and the reused research/argument routine. End evidence on 149, 151 and 152, response on 153. |

The unequal allocations are defensible. Unit 6’s two new owners sit alongside substantial reused research, writing and speaking; its 20 days are not evidence of underloading. No additional run of days is demonstrably excessive or insufficient from these planning records.

Response time is counted once for each combined assessment. Unit 1’s pilot response is separately identified within day 7.

### Standards and lettered parts

| Standard group | Named instruction and evidence |
|---|---|
| W.6.1a to e | Model on 42; applications through 48 to 56; argument portfolio collected on 56. |
| W.6.2a to f | Model on 72; report development through 79; collection on 81 and cold application on 84. |
| W.6.3a to e | Explicit components on 17, 19, 21 and 22; narrative portfolio on 30. |
| W.6.9a and b | Literary and informational applications recur across the year. Correct the literary-only assessment claim on 132. |
| SL.6.1a to d | Routine taught on 5 and observed in discussion, including 30. |
| L.6.1a to e | Case and intensive pronouns on 24; shifts and antecedents on 25; language variation and revision strategies on 26; portfolio on 30. |
| L.6.2a and b | Teaching on 97 to 98, application on 99 and 103, assessment on 106. |
| L.6.3a and b | Sentence variation and consistent style taught on 23, then applied during revision. |
| L.6.4a to d | Context, roots, references and verification have days; affix application needs finding 3’s correction. |
| L.6.5a to c | Relationships on 93; figures and connotation on 114 to 115; assessment reservations on 106 and 134. |

The remaining owned reading, research, listening and presentation codes have identifiable planned work. This establishes planned coverage, subject to the findings, rather than finished item quality.

### Readiness and retrieval

All 30 unique directly assumed ELA rows have grade 5 use. Retrieval is therefore the correct treatment.

| Receiving unit | Placement |
|---|---|
| 1 | Staged retrieval on days 1, 5, 7 and 11, with vocabulary and typing returns later. |
| 2 | Final ten minutes of 32. |
| 3 | Final ten minutes of 62. |
| 4 | Final ten minutes of 86. |
| 5 | Final ten minutes of 112. |
| 6 | Final ten minutes of 136. |

No unit checks a year-before row as readiness, retrieves an identified older idle row, or places a readiness check on its first day. The oral-reading screen is a separately described follow-up screen.

Two prerequisite-table examples should be made clearer when applying the report: grade 5 day 23 is a two-voice poem, while days 29 to 39 provide clearer narrative evidence; day 118 plans a presentation, while days 121 to 123 provide actual speaking evidence. These better pointers do not change last-use grade or retrieval treatment.

### Course checks and cross-subject timing

The check descriptions explicitly prevent repetition:

- Days 59 to 60 transfer unit 2 skills to flood-town content.
- Days 109 to 110 transfer unit 4 skills to weather content.
- Day 158 transfers unit 6 account/media skills to writing-system content.

The checks meet target weeks 12, 22 and 32.

The same-year leans have adequate timing or named bridges: Babylon background on 33; weather concepts on 63; a percent contingency on 65; alphabet history on 92; familiar displays on 140 and 148; and the sea-floor contingency on 141. Histogram use remains conditional on actual mathematics instruction. Account comparison is taught by 138, before social studies unit 11 begins on 143.

### Candidates, shorter path and source map

All six units settle their Candidate cells and identify existing day costs or zero additional cost. The unit 6 placement is sound in the sequence but needs the frame correction in finding 6.

The ten fold-in days are **13, 28, 54, 82, 102, 108, 129, 147, 155 and 156**. None is an assessment day; their specified work is consolidation rather than unique first teaching. Retrieval and continuing routines are explicitly preserved.

The 40-minute route identifies reductions and honestly preserves W.6.6’s single-sitting demand as a time-provision issue. It is a provisional adaptation, not a demonstrated classroom fit, particularly when combined with 150 meetings.

A base-lesson source map is **not applicable**: this course has no base curriculum.

## ELA lens checklist: scope and sequence layer

| Lens line | Status | Evidence |
|---|---|---|
| Text demand climbs, or departures have a reason | Met at planning level | Supported novella, technical explainers, chapter nonfiction and increasingly implicit literary texts have placement reasons. Actual demand awaits texts. |
| Research recurs | Met | R1 in unit 3; independent reuse in R2, unit 6. |
| Full-process writing recurs | Met | Narrative, argument and informative process pieces, with later shorter applications. |
| Formal discussion occurs often | Met | Twenty named discussions; no gap over ten course days. |
| K to 2 phonics aligns with decodable texts | Not applicable | Grade 6 owns no RF standards. |

## What is right and should not be undone

- Keep the whole novella and complete first-trial arc before the pilot theme assessment.
- Keep explicit models, feedback and visible revision across the three process pieces. This is consistent with the [secondary writing practice guide’s instructional cycle](https://ies.ed.gov/ncee/wwc/PracticeGuide/22).
- Keep the separation of portfolio evidence, observed performance and cold reading tasks.
- Keep hearing before transcript access where listening evidence is intended.
- Keep transfer to earlier content on course checks.
- Keep complete anchors available through print, shared reading and audio beside print, with supported reading recorded distinctly.
- Keep the explicit limitations on unwritten texts, unselected sources and untested timing.

## Settled by the expert

These are item-level dispositions for the caller to apply.

| Choice | Reason | File or location |
|---|---|---|
| Remove W.6.6 from day 110’s check claim | Existing publication and typing evidence already has an appropriate home | `days.csv`, day 110 |
| Remove W.6.9b from day 132 | Its assessment uses literature and performance | `days.csv`, day 132 |
| Teach informational figurative and connotative meaning during editorial reading | Places instruction before the mid-unit assessment | Days 38 to 39; unit 2 description |
| Add affix-based inference within existing word work | Carries the complete L.6.4b demand | Days 90, 99 and 106 |
| Require word-choice analysis of meaning and tone together | Makes the complete RL.6.4 demand observable | Days 114, 118 and 134; frame unit 5 |
| Determine core status by instructional use | Required paired selections can be core | Text-accounting paragraph and text records |
| Retain retrieval and internal end assessments | These follow the current brief | Frame readiness and assessment notes |

## What I could not judge

The originals remain unwritten, federal selections remain unchosen, and cold tasks and scoring resources remain unwritten. Consequently, this review cannot certify actual text complexity, literary quality, cultural suitability, vocabulary recurrence, image rights, the 80 percent text-dependent-task count, scoring reliability or classroom minutes.

The provisional independent-reading options also require complete suitability reads. Their cautions do not establish a screened shelf.

## For Cory

- **Audience and time provision:** A combined 40-minute, 150-meeting implementation remains unverified. A full-course offer for that audience needs a demonstrated time provision, including the protected typing sittings.
- **Independent-reading provision:** The course acknowledges that a suitable modern free shelf is not established. Any change to the audience promise or resource provision belongs to Cory.

The six corrections require no movement of standards between units and no new spending or outside contact.

## Sources and reading limits

- Common Core grade 6 [literature](https://www.thecorestandards.org/ELA-Literacy/RL/6/), [informational reading](https://www.thecorestandards.org/ELA-Literacy/RI/6/), [writing](https://www.thecorestandards.org/ELA-Literacy/W/6/), [speaking and listening](https://www.thecorestandards.org/ELA-Literacy/SL/6/) and [language](https://www.thecorestandards.org/ELA-Literacy/L/6/): standard wording checked against the local file.
- [ELA grades 6 to 12 evidence guide, v2.0](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_6_12_Evidence_Guide_2_0_2068cea08f.pdf): relevant core-text, complexity and writing-accounting provisions, not a complete scored review.
- [Common Core Appendix A](https://www.oregon.gov/ode/educator-resources/standards/ELA/Documents/ela-appendix-a.pdf): three-part text-complexity model, read in part.
- [Publishers’ Criteria, grades 3 to 12](https://achievethecore.org/content/upload/Publishers_Criteria_for_Literacy_for_Grades_3-12.pdf): text-centered instruction and extended reading, read in part.
- [Teaching Secondary Students to Write Effectively](https://ies.ed.gov/ncee/wwc/PracticeGuide/22): recommendations and relevant modelling guidance; underlying studies were not independently read.
- [EL Education grade 6 curriculum map](https://el-education-production.s3.amazonaws.com/media/documents/CurriculumTools_CurriculumMap-Grade6_0220.pdf): comparison of text-based arcs and recurring research.
- [CommonLit grade 6 scope and sequence](https://cdn.commonlit.org/website_assets/193/1716217021/360_Scope_and_Sequence_-_May_2024.pdf) and [middle-school pacing guidance](https://cdn.commonlit.org/website_assets/509/1745587479/CommonLit_360_Pacing_Guidance_SY24-25_%28Grades_6-8%29.pdf): comparison of reading/writing order and stated period assumptions. These are reference comparisons, not adopted material.

**For the source list:** The current 141-page evidence guide opened through the [review-tools page](https://edreports.org/process/review-tools/ela), although its initial direct fetch failed. The linked comparison maps and pacing guide are reusable source leads.

**Verdict:** Revise before unit planning. **Findings:** 6. **Report path:** `docs/reviews/sequence-english-language-arts-grade-6-2026-11-15.md`, supplied above, not written.


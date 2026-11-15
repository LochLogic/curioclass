# Independent scope and sequence review: English Language Arts, Grade 3

**Requested report path:** `docs/reviews/sequence-english-language-arts-grade-3-2026-11-14.md`  
**Delivery:** Complete report below. No file was created or changed.  
**Role:** First independent reader, before the expert, following the supplied blind rule.  
**Finding count:** 7.

## Verdict

The sequence has coherent unit arcs, sensible returns to earlier learning and correctly placed course-level checks, but it needs revision before unit planning. Its largest risk is assessment validity: some named tasks cannot demonstrate their listed standards, while unit 3 omits end assessment of its newly introduced multisyllable decoding. Repair the task-to-standard assignments and the concentrated grammar instruction first, then complete the writing and shorter-period accounting.

## What I read

- `docs/agents/EXPERT.md`, the ELA lens, `docs/RUBRIC-ELA.md`, the foundation, relevant Roadmap sections, shared and ELA approaches, relevant approach-source entries, glossary, and BASELINE rules 20 to 24 and 29.
- The complete grade 3 scope and sequence, frame, all 160 day rows and all 155 source-map rows.
- All 28 grade 3 ELA progression rows, their incoming prerequisite rows, and grade 2 day placements.
- The three earlier-grade cross-subject prerequisite rows and their grade 2 day placements.
- `docs/courses/CALENDAR.md` and every subject’s grade 3 rows in `data/plans/calendar.csv`.
- Grade 3 records in `data/plans/ela-texts.csv`.
- Earlier permitted grade 3 frame reviews, their fix dispositions, and relevant ELA baseline findings, after forming the cold-read findings.
- The outside sources linked below. Source-map archive paths were checked against the local lesson archives.

No prohibited course or review file was opened.

| Required check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Reported zero sequence failures for this course, then stopped elsewhere because Python package `markdown` is missing. |
| `python -X utf8 scripts/frame.py calendar` | Passed; no stagger-rule break. |
| `python -X utf8 scripts/frame.py check english-language-arts-grade-3` | Passed, zero failures; 153 unit days plus seven course-level days. |
| `python -X utf8 scripts/stale.py check` | Passed, 56 files, zero failures. |

The incomplete repository-wide gate does not withhold the curricular verdict.

## Findings, most serious first

### 1. Several assessment tasks do not establish their listed standards

**Severity:** Major  
**LAYER:** sequence  
**REPEAT:** yes, incomplete standard coverage appeared in the earlier independent grade 3 frame review, findings 4 to 6. These are new day-level instances.  
**Confidence:** firm on the mismatched tasks; likely on evidence left unspecified.

**Location:** `days.csv`, especially days 19, 51, 135 and 153.

The repeated instruction to sample every listed part does not identify the required performance. Some assignments are directly incompatible with their codes.

| Day | Problem | Exact correction |
|---|---|---|
| 19 | The article assessment names main idea, details, images and answers, but also lists all four L.3.4 strategies without identifying vocabulary evidence. | Reserve four brief applications: infer meaning from a sentence, explain an affix’s effect, connect an unfamiliar word to a familiar root, and consult a glossary or dictionary for precise meaning. |
| 51 | A poem recording and explanation of word effect do not necessarily show verb formation, three tenses, or adjective and adverb comparison, although L.3.1d, e and g are listed. | Name a separate short sentence-production task covering those demands. A learner’s recording cannot stand for the grammar task. |
| 135 | Both listed readings are informational, but the assessment claims RL.3.4. | Replace RL.3.4 with RI.3.4 for this informational task. Retain L.3.5a only with a phrase whose literal and nonliteral readings students must distinguish. |
| 153 | The water announcement is an informational recording, but SL.3.5 specifically concerns recorded stories or poems. | Remove SL.3.5 from this day. Keep the announcement under its valid speaking and digital-writing codes; retain SL.3.5 evidence from days 35 and 76. |

The distinctions follow the [grade 3 Language standards](https://www.thecorestandards.org/ELA-Literacy/L/3/), [literature standards](https://www.thecorestandards.org/ELA-Literacy/RL/3/) and [speaking and listening standards](https://www.thecorestandards.org/ELA-Literacy/SL/3/).

**Why it matters:** A unit writer can follow these goals faithfully and still produce assessments that cannot support the recorded coverage.

**Exact fix:** Apply the corrections above, then audit every assessment row against the same rule: name the short task or existing individual product that supplies each listed demand. Full item wording can remain with unit planning.

### 2. Unit 3 does not close its newly taught decoding part

**Severity:** Major  
**LAYER:** sequence  
**REPEAT:** yes, the earlier frame reads identified incomplete coverage; this omission occurs in the new sequence.  
**Confidence:** firm.

**Location:** The skills thread; days 81 to 119, especially end-assessment days 114, 115, 117, 118 and 119.

RF.3.3c first enters instruction in unit 3. None of that unit’s end-assessment rows lists it or identifies individual multisyllable decoding evidence. The recurring word checks on days 90 and 105 provide useful interim information, but neither is part of the unit’s closing assessment. Day 158 eventually checks the part, after unit 4.

[RF.3.3c](https://www.thecorestandards.org/ELA-Literacy/RF/3/) requires decoding multisyllable words. Fluent passage reading alone does not guarantee a sample of the newly taught word structures.

**Why it matters:** Students can leave the unit without closing evidence on its new foundational demand.

**Exact fix:** Add RF.3.3c and a brief individual decoding sample to the existing oral rotations on days 117 and 118. Each learner reads unfamiliar words using the syllable and affix structures already taught, followed by a short connected-text application. Return the result during day 119’s existing response time. Add no day.

### 3. Day 50 concentrates too much first grammar instruction immediately before assessment

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, pacing and allocation were raised in the earlier grade 3 frame reviews; the present problem is a specific instructional bottleneck.  
**Confidence:** likely.

**Location:** Days 43 to 51, particularly day 50.

Day 50 is the first explicit instruction for three substantial parts:

- L.3.1d: regular and irregular verb forms.
- L.3.1e: past, present and future simple tense.
- L.3.1g: adjective and adverb comparisons, including selection according to the modified word.

The same day also carries narrative word-choice revision, peer critique, teacher feedback and the ordinary skills block. Day 51 assesses all three grammar parts. Later practice exists, but it comes after this first assessment.

This creates a one-day introduction for several distinct demands, despite available narrative-writing days before it. The [elementary writing practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/17) supports explicit sentence instruction and supported application. It does not establish a required number of lessons; the placement judgment here rests on the documented load.

**Why it matters:** The first assessment may chiefly measure how quickly students absorb a crowded introduction.

**Exact fix:** Within unit 2:

- Teach verb-form choices while drafting actions on day 43.
- Teach tense consistency on day 45.
- Teach adjective and adverb comparisons during descriptive revision on day 48.
- Use day 50 to retrieve and apply these choices during feedback.

Keep their ownership unchanged. Preserve the instruction when day 48 folds into day 47 on the shorter-year path.

### 4. The writing ledger omits substantial pieces already required by the days

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, writing-accounting consistency was raised in the ELA baseline review, finding 5.  
**Confidence:** firm on the omissions.

**Location:** “The reading and skills thread,” its 20-piece ledger, and days 28, 56 and 148.

The ledger reserves six opinion, seven informative and seven narrative pieces. It excludes at least three distinct informative products already required:

| Day | Required product |
|---|---|
| 28 | Explanatory paragraph about Washington’s effort |
| 56 | Paragraph explaining tadpole changes |
| 148 | Source-based announcement script, subsequently revised and recorded |

Adding only these gives six opinion, ten informative and seven narrative pieces: approximately **26/43/30**, before other substantive writing is counted. This is an incomplete accounting, not proof that the finished course will have those shares.

The [grades 3 to 5 evidence guide](https://cdn.edreports.org/reviewtools/ela/2.1/ELA-Grades-3-5-v2.1-Tools_Evidence-Guide.pdf), PDF pages 109 to 111, also distinguishes process writing from on-demand work. Its writing-share discussion is narrative reporting, not a separate scored threshold.

**Why it matters:** Later writers could add artificial pieces to preserve the reservation while overlooking writing the sequence already requires.

**Exact fix:** Replace the selected-piece reservation with a complete planned-product ledger. Give each product a stable identifier, type, source texts, days, and process or one-sitting status. Count the announcement once across drafting, revision and recording. Report process and total-writing distributions separately, then adjust existing short-response purposes where needed.

### 5. The shorter-period section supplies no reduced-time schedule

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, time feasibility appeared in the earlier independent frame review, finding 3; this is the unresolved shorter-period requirement.  
**Confidence:** firm on the missing schedule.

**Location:** “Shorter path,” first paragraph.

The normal timetable already alternates independent reading and partner fluency. Recommending that alternation again does not show how a shorter total literacy allocation works. Splitting 90 minutes into separate periods changes scheduling, but supplies no reduced-time route.

The text candidly acknowledges that its minimum workable block is unknown. That is an appropriate limitation, but the shorter-period requirement remains unmet.

**Why it matters:** A teacher cannot tell what fits, what becomes less frequent, or how much time the alternative requires.

**Exact fix:** Add one explicitly budgeted shorter-total-time option, identifying minutes for the main lesson, word work, reading practice, grammar retrieval and assessment rotations. Name the repeated practice or publication work reduced on particular days. Keep all owned instruction and independent assessment evidence. Mark feasibility provisional until the timed probe; if the budget cannot preserve the course, state that outcome plainly instead of presenting alternation as the completed route.

The ten-day shorter-year list is a separate, substantially stronger provision.

### 6. Anchor accounting treats inventory labels as instructional status

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, anchor identification and balance were unresolved in the earlier independent frame review, finding 2.  
**Confidence:** firm on the classification problem.

**Location:** “For the lead,” item 2; “Text placements and limits”; grade 3 rows in `ela-texts.csv`.

The stated 75/25 split counts only records labelled `anchor`. Several records labelled `paired`, however, supply compulsory core instruction: the book-carrier and packhorse articles, Washington biography, second series book, script and water comparison texts.

The [evidence guide’s anchor definition](https://cdn.edreports.org/reviewtools/ela/2.1/ELA-Grades-3-5-v2.1-Tools_Evidence-Guide.pdf), PDF page 55, turns on instructional use. A “paired” label does not automatically exclude a required core text.

Counting all 24 scheduled, nonoptional inventory records gives **13 literary and 11 informational records**, approximately **54/46**. That is a provisional record count: poem and tale collections still need unpacking into actual selections.

**Why it matters:** The current note could trigger unnecessary text changes while leaving the real core-text inventory unresolved.

**Exact fix:** Identify core status by actual instructional use, retaining a separate field for the relationship “paired.” Reconcile the local text table and central inventory, publish the provisional record count, and recount actual selections when collections are chosen. Complete the frame-required course text records before unit planning. This does not require commissioning extra texts merely to repair the present label count.

### 7. Active guidance retains superseded readiness and completion statements

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale dependency statements appeared in the earlier independent grade 3 frame review, findings 10 and 11.  
**Confidence:** firm.

**Location:**

- Grade 3 frame, “Which row sits where,” Seams and unit 1.
- `docs/RUBRIC-ELA.md`, Gateway 1 evidence-status cells.

The sequence correctly applies retrieval to grade 2 prerequisites. The frame still directs a readiness check on first use of a grade 2 skill and calls the fall oral sample “readiness.” The rubric still says no grade 3 to 5 scope and sequence exists and describes foundational provision as absent.

The stale checker passes because these semantic contradictions are outside its detected failures.

**Why it matters:** A later writer can reintroduce unnecessary readiness assessments or mistake completed planning for absent work.

**Exact fix:** Preserve the distinction between placement screens and prerequisite readiness. Replace the frame’s year-before readiness directions with retrieval, and describe the fall samples as placement or current-performance screens. Update the rubric’s evidence-status cells to point to the new sequences while retaining the limits on unwritten materials and untested timing.

## Other required judgments

| Requirement | Judgment |
|---|---|
| Order within units | Sound overall: short reading routines precede explanatory writing; research precedes the frog page; whole-book reading precedes comparison and opinion; water synthesizes prior research and speaking. Finding 3 identifies the concentrated exception. |
| Prerequisite last use | All 30 directly assumed ELA rows occur in grade 2 day rows. The three earlier-grade cross-subject rows also occur in grade 2. Retrieval is the correct treatment. |
| Misclassified or mistimed readiness | No older prerequisite was found wrongly retrieved. No year-before prerequisite is labelled readiness in the current day rows. No readiness check occupies a unit’s first day. |
| Mid-unit assessments | Present in all four units, each longer than 25 days. |
| Response counted once | Unit 1: day 39; unit 2: day 77; unit 3: final 15 minutes of day 119; unit 4: final 15 minutes of day 156. Interim feedback is separately identified. |
| Checks do not repeat | Met. Days 78 to 79 use book-access content for frog-unit skills. Days 157 to 158 use earlier book-access or frog content for water-unit skills. Both prose and day notes say so. |
| Calendar | Met. ELA checks occupy weeks 16 and 32. |
| Same-year leans | Met as planned. Map, historical-context, frog-life-cycle and habitat bridges are placed where prior completion cannot be assumed. Opinion instruction does not depend on an unprovided social studies lesson. |
| Candidate cells | All have explicit keep decisions and locations inside existing days. Timing remains provisional; the decision to keep each addition is settled. |
| Shorter year | Ten named fold-ins, all with blank assessment cells. Chapters and owned parts are explicitly retained. Combined-day timing remains unverified. |
| Base source map | Complete placement accounting: 153 base lessons, 151 kept and two cuts with reasons, plus two original screen days. Every mapped archive path exists; no lesson PDF was left unmapped. Source order is preserved. |

### Days by load

| Unit | Days | Newly owned rows | Assessment days | Judgment |
|---|---:|---:|---:|---|
| 1 | 39 | 15 | 8 | Launch routines, foundational instruction and several writing/reading products justify the allocation. |
| 2 | 38 | 7 | 8 | Research, narrative, informative writing and continued language parts create substantial load. Day 50 needs redistribution. |
| 3 | 39 | 5 | 10 | Twelve whole-book reading days, five second-book chapters, comparison and performances justify sustained time. Some assessment days also advance reading. |
| 4 | 37 | 1 | 9 | Its load includes synthesis, continued language parts, research, essay, letter and announcement. The small new-row count alone does not justify cutting it. |

No demonstrated unit-wide excess or shortage warrants changing the frame’s day counts.

### Lettered-part coverage

Instructional placements exist across RF.3.3a to d, RF.3.4a to c, W.3.1a to d, W.3.2a to d, W.3.3a to d, SL.3.1a to d, L.3.1a to i, L.3.2a to g, L.3.3a to b, L.3.4a to d and L.3.5a to c.

This placement result does not establish valid assessment evidence. Findings 1 and 2 identify the necessary corrections. The delayed parts are generally distinguished appropriately from their parent codes.

## Lens checklist: scope and sequence layer

| Checklist line | Result |
|---|---|
| Text demand climbs, or departures have a reason | **Met as a commission plan.** Short texts lead to a whole chapter book and independent upper-band information reading. Actual demand remains unverified. |
| Research and full-process writing recur | **Met.** Research in units 2 and 4; a process cycle in every unit. Writing accounting needs finding 4’s correction. |
| Formal discussion occurs often | **Met.** Four named formal discussions per unit, alongside daily partner talk. |
| K to 2 phonics order aligns with decodable texts | **Not applicable.** This is grade 3. Its long-word and fluency thread is present. |

## What is right and should remain

Keep the four unit arcs, whole-book requirement, five connected second-book chapters, repeated research, school-day device route, text-dependent daily responses and decoding-before-context rule. Keep the explicit earlier-topic content for cumulative checks and the bridges that prevent dependence on unfinished science or social studies instruction.

Earlier ownership corrections, the weekly skills timetable, the visual listening task, and the scene/stanza work are visible in this sequence. This report does not reopen those settled choices.

## Settled by the expert

Item-level recommendations for the caller to apply. No edits were made.

| Choice | Reason | File or location |
|---|---|---|
| Correct days 19, 51, 135 and 153 as specified in finding 1 | Align claimed codes with observable work | `days.csv`; assessment descriptions |
| Add multisyllable decoding to days 117 and 118 | Close unit 3’s newly taught foundational part | `days.csv`; unit 3 |
| Distribute grammar introductions across days 43, 45 and 48 | Provide practice before day 51 | `days.csv`; unit 2 |
| Count every planned substantive writing product once | Make the writing distribution auditable | Writing ledger and day notes |
| Classify core texts by instructional use | Avoid misleading anchor-only label counts | Text tables and inventory |
| Retain all four unit lengths and the ten named fold-ins | No demonstrated reason to change their allocation | Scope and sequence |
| Use retrieval for the verified grade 2 prerequisites | Their last use is the preceding grade | Frame readiness wording |

## For Cory

- None arising from the corrections above. They preserve existing content, ownership, unit order and day totals.
- Any eventual change to the required literacy-time assumption remains Cory’s scope decision. This read does not reopen the settled provisional 90-minute block.

## Limits and sources

Actual text quality, final complexity, cultural provenance, rights, complete reading volume and classroom timing remain unverified. I did not inspect every base lesson’s full instructional content; the source-map check establishes complete archive placement and ordering. No curricular finding rests solely on memory. Prior-run memory was used only for review procedure.

Outside sources opened or searched in this run:

- [Common Core grade 3 standards: Language](https://www.thecorestandards.org/ELA-Literacy/L/3/), [foundational reading](https://www.thecorestandards.org/ELA-Literacy/RF/3/), [literature](https://www.thecorestandards.org/ELA-Literacy/RL/3/), [information](https://www.thecorestandards.org/ELA-Literacy/RI/3/), [writing](https://www.thecorestandards.org/ELA-Literacy/W/3/) and [speaking/listening](https://www.thecorestandards.org/ELA-Literacy/SL/3/): checked against the repository’s full standard text.
- [Grades 3 to 5 review criteria](https://cdn.edreports.org/reviewtools/ela/2.1/ELA-Grades-3-5-v2.1-Tools_Review-Criteria.pdf) and [evidence guide](https://cdn.edreports.org/reviewtools/ela/2.1/ELA-Grades-3-5-v2.1-Tools_Evidence-Guide.pdf): relevant foundational, core-text and writing provisions.
- [Federal foundational-reading practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/21): explicit word analysis and daily connected-text reading.
- [Federal elementary-writing practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/17): explicit instruction, writing processes and varied purposes.
- [Core Knowledge grade 3 skills sequence](https://www.coreknowledge.org/wp-content/uploads/2017/06/CKLA_G3_Scope-and-Sequence_Skills-.pdf): comparison of staged instruction, practice and assessment, read as reference only.
- [Base curriculum’s grade 3 map](https://curriculum.eleducation.org/sites/default/files/curriculumtools_curriculummap-grade3_072017.pdf): search-indexed material was available, but direct retrieval returned 404. Its complete content was not treated as newly verified.

**For the source list:** The two linked review-tool CDN addresses worked. The hashed addresses recorded in the local rubric were inaccessible through the web tool during this run.


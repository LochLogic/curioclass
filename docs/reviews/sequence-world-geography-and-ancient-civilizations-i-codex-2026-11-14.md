# Independent scope and sequence review: World Geography and Ancient Civilizations I

**Date:** 2026-11-14  
**Intended report:** `docs/reviews/sequence-world-geography-and-ancient-civilizations-i-2026-11-14.md`  
**Delivery:** Complete report supplied here. No file was created or edited.

## Verdict

The sequence has a sound instructional structure, but it needs revision before unit plans are built from it. Its biggest risk is that complete code lists conceal incomplete teaching and assessment demands. Keep the units, day allocations and writing progression, while making the missing work explicit and resolving the remaining planning contradictions.

## What I read and checked

- The complete target scope and sequence, `days.csv` and course frame.
- All 29 grade 6 social studies progression rows, their stated prerequisites and handoffs, and the relevant grade 6 cross-subject arrangements.
- EXPERT, the social studies lens, the shared and social studies adoption criteria, STANDARD, FOUNDATION, relevant ROADMAP guidance, BASELINE rules 20 to 24, GLOSSARY, APPROACH, APPROACH-SOURCES and BASE-TEXTS.
- CALENDAR and all grade 6 rows of `data/plans/calendar.csv`; relevant ELA, math and science frame sections.
- Both earlier reviews of this course frame, the social studies progression reviews and correction report, and relevant baseline structure findings.
- The external standards and curriculum references linked below.

The earlier frame repairs are substantially present. In particular, the revised questions, longer units 7 and 8, sourcing from the beginning of the year, law-revision task, religious conduct task and explanation self-critique should remain. FOUNDATION’s current agent-review policy supersedes the earlier reports’ requests for outside content readers.

### Checks

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Stopped with `ModuleNotFoundError: No module named 'markdown'`; full gate unverified |
| `python -X utf8 scripts/frame.py calendar` | Completed; grade 6 check weeks 15, 23 and 32, with no reported stagger break |
| `python -X utf8 scripts/frame.py check world-geography-and-ancient-civilizations-i` | 0 failures; 11 units, 160 days |
| `python -X utf8 scripts/sequence.py check world-geography-and-ancient-civilizations-i` | 0 failures |
| `python -X utf8 scripts/stale.py check` | 56 files, 0 failures |

The interrupted full gate does not prevent this verdict.

## Findings, most serious first

### 1. End-of-unit assessment descriptions do not secure the full work their code lists claim

**LAYER:** sequence  
**REPEAT:** yes, incomplete standards-to-task matches recur in the progression and frame reviews  
**Severity:** serious  
**Confidence:** firm on the specification gaps; final item quality remains unjudged

Every assessment row lists its unit’s codes. Several task descriptions, however, permit an assessment that leaves taught requirements unchecked. A writer following the task description could complete it without assessing everything in the code column.

| Unit and assessment day | Work not explicitly secured | Exact repair |
|---|---|---|
| 1, day 9 | Climate explanations and cooperation among disciplines | Add a climate-to-human-life explanation and an example requiring students to combine disciplinary evidence. Sorting questions alone does not demonstrate cooperation. |
| 2, day 24 | Three farming ways of life and mechanisms through which societies spread | Add a brief comparison and a spread explanation, alongside the existing interpretation, change and traits tasks. |
| 3, day 37 | Environmental change and changing settlement patterns | Supply dated representations, rather than only one city map, and require an explanation connecting the changes. |
| 4, day 53 | Gilgamesh and the proposed law revision taught on day 49 | Name both in the assessment specification. Include the revision’s effectiveness against the same public problem. |
| 5, day 69 | Pharaohs, dynasties, a ruler’s actions, and religion with expected conduct | Add an art or text task addressing these demands; the current list names social order and achievements but omits this work. |
| 8, day 112 | Research decisions that may not appear in the finished report | Count a compact research record with the report: questions, source choices, source checks and revision. |
| 9, day 130 | Knowledge of Axum, Swahili connections and West African societies | Require a comparison using the taught historical cases. An unspecified unseen trade source does not ensure all three are assessed. |
| 10, day 141 | Constructing a geographic representation | Explicitly count the student’s days 135 to 136 map and explanation. Reading a supplied keyed map does not establish construction. |
| 11, day 155 | Research-generated questions and the explanation’s strengths and weaknesses | Explicitly count the report and inquiry record with the assessment, as unit 8 already does for its report. |

Unit 6 also needs assessment language matching finding 2. I found no equally specific omission in unit 7’s broad assessment description, although its items must preserve the individual historical requirements.

**Why it matters:** these omissions could produce a course that teaches more than it checks, while its records report complete coverage.

**Exact fix:** revise the assessment goals and corresponding prose to identify the required evidence. Where a map, report or inquiry record counts, say so explicitly and identify the relevant days. Keep the existing assessment and respond slots; the unit plan can combine compact content tasks with separately scored products.

This follows Curio Class’s own assessment rule. As a useful comparison, the [Investigating History guidebook, page 13](https://www.doe.mass.edu/investigatinghistory/curriculum/g6-course-guidebook.pdf#page=14) distinguishes performance assessment from broader content assessment. That comparison supports checking both dimensions; it does not establish that the present descriptions cover them.

### 2. Several C3 demands remain thinner in the day goals than in the claimed indicators

**LAYER:** sequence, progression  
**REPEAT:** yes, progression review finding 1 and the earlier independent frame review identify this problem type  
**Severity:** serious  
**Confidence:** firm on indicator wording; likely on the resulting teaching omissions

The remaining gaps are specific, rather than a reason to reopen every previously repaired C3 mapping.

| Location | Remaining gap | Exact repair inside existing days |
|---|---|---|
| Unit 2, days 13 to 14, `D1.2.6-8` | Expert disagreement is explicit; agreement is not | Require students to identify a shared conclusion as well as a disputed one, and explain the difference in certainty. |
| Unit 4, day 42, `D2.Eco.13.6-8` | Surplus and specialization are explicit; improved living standards are not | Extend the chain to explain how greater output per worker can improve material living conditions, while examining unequal gains. |
| Unit 6, day 79, `D2.Eco.7.6-8` | Entrepreneurship is present; innovation’s economic role is not | Add analysis of a documented innovation already available in the unit and explain how it changed production or exchange. |
| Unit 9, days 120 to 121, `D2.Geo.3.6-8` | The plan offers an electronic map **or** paper, and specifies no graphing task | On the device route, produce and analyze a paper and electronic representation, including a small linked graph. Preserve the paper fallback and state accurately which medium-specific work it cannot demonstrate. |

The requirements were checked against the [C3 Framework’s question, economics and geography tables](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf).

**Why it matters:** a related activity can look complete while stopping short of the indicator’s actual reasoning demand.

**Exact fix:** amend those goals and owning progression notes where needed, then carry the same demands into the assessment specifications. Do not add days or change ownership.

### 3. Three anchor requirements are not fully carried into explicit day work

**LAYER:** sequence, standard  
**REPEAT:** yes, incomplete components within claimed anchor codes recur in both earlier frame reads  
**Severity:** serious  
**Confidence:** firm

| Location | Missing component | Exact repair |
|---|---|---|
| Unit 2, day 16, `MA.6.T2.4` | Farming is explicit, but animal domestication and metallurgy are not | Name and teach all three developments, with their different regional timing. |
| Unit 7, day 87, `MA.6.T3e.3b` | The kingdom and temples appear, but David’s establishment of Jerusalem as capital is absent | Add this event to the historical account and timeline. |
| Unit 9, days 124 to 125, `MA.6.T4b.1` | Axum’s Christianity appears, but East African societies’ role in Islam’s connections to South Asia does not | Add sourced Indian Ocean religious connections on day 125 and carry this code there. |

These components are present in the [official Massachusetts framework, printed pages 86 to 87, 90 and 92](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf). The local paraphrase of `MA.6.T4b.1` also loses the South Asia destination, so that record needs correction alongside the day.

**Why it matters:** later writers can faithfully follow the CSV and still leave required content untaught.

**Exact fix:** amend the named day goals, echo them in the sequence prose, and include their evidence in the unit assessment specifications. All repairs fit the existing units.

### 4. The sequence supplies no shorter path

**LAYER:** sequence  
**REPEAT:** new for this course’s sequence  
**Severity:** moderate  
**Confidence:** firm on the requirement; feasibility of the shorter route needs later timing checks

The sequence specifies 160 daily periods of 50 minutes, but gives no shorter route. FOUNDATION section 5 and adoption criterion C2 explicitly require one.

**Why it matters:** a teacher with shorter periods receives no guidance about what can be shortened while preserving the course’s standards and assessment system.

**Exact fix:** add a “Shorter path” section for 45-minute periods, retaining the 160-day calendar. Give a unit-by-unit table identifying repeated examples, additional comparisons or sharing routines that can be shortened, while preserving essential source work, required products, assessment demands and response time. Check that route against the actual minutes when unit plans are written; do not claim its feasibility has already been demonstrated.

### 5. Unit 6 retains a dormant-prerequisite instruction that contradicts its own history

**LAYER:** progression, frame, sequence  
**REPEAT:** yes, skipped-grade handoffs and readiness terminology were addressed in the progression and baseline reviews  
**Severity:** moderate  
**Confidence:** firm

Day 75 is marked `readiness`, and day 76 promises a one-lesson reteach of grade 3 money and saving. The same progression note and frame say the knowledge was used in grade 5.

The sequence recognizes the contradiction in “For the lead” but leaves it unresolved. Sequence-write rule 2 distinguishes knowledge used the previous year from knowledge idle for two or more grades.

**Why it matters:** the unit reserves an intervention of uncertain size while giving day 76 a full new-content goal.

**Exact fix:** make day 75’s `assess` cell blank and describe its opening as a retrieval task. Replace the automatic one-lesson reteach with a brief, needs-based worked example inside days 75 to 76. Correct the conflicting dormant-knowledge sentence in `ss6-phoenician-trade` and the frame’s readiness references. Keep the money and saving content.

### 6. Two planning notes remain unresolved after their evidence is available

**LAYER:** process  
**REPEAT:** yes, calendar drift and stale status notes recur in the baseline and frame reviews  
**Severity:** minor  
**Confidence:** firm

| Location | What is wrong | Exact fix |
|---|---|---|
| “For the lead,” item 1 | The generated calendar places unit 3 on days 26 to 39 and unit 4 on 40 to 55. The sequence places unit 3 on 26 to 38 plus 55, and unit 4 on 39 to 54. The note says no fix is needed for checks. | Retain the held reflection day, but record the actual unit runs in the generated calendar. Have the calendar process use the established day rows and represent the noncontiguous unit explicitly. Do not hand-edit generated tables. |
| “For the lead,” item 3, and day 110’s note | The ELA product-load check is left undone | Close it using the current ELA frame: its three process pieces are in units 1 to 3, finishing by about day 86. Unit 4 specifies two one-sitting pieces, so the alleged two-week overlap of large writing products is not established. |

**Why it matters:** these notes make a later worker repeat completed investigation or choose between conflicting schedules.

## Order, load and assessment placement

The major dependencies are sound: timeline before dated study, traits before repeated comparisons, regional reasoning before later applications, and the first report before the longer report.

| Unit | Teaching days | Allocation visible in the sequence | Judgment |
|---|---:|---|---|
| 1 | 8 | 3 fields, 3 timeline, 2 climate | Compressed but defensible |
| 2 | 13 | 4 interpretation, 4 early life, 4 complex societies, 1 synthesis | Reasonable |
| 3 | 12 | 4 maps, 4 settlement, 4 action including delayed reflection | Reasonable |
| 4 | 14 | 2 place/time, 2 economics, 2 society, 6 writing/law, 2 synthesis/review | Law emphasis is justified by its source and civic work |
| 5 | 13 | 2 Nile, 4 society/religion, 2 achievements, 4 Kush, 1 synthesis | Reasonable |
| 6 | 8 | 5 trade/economy/work, 3 writing | Reasonable after the specified repairs |
| 7 | 13 | 1 framing, 4 Judaism, 3 Christianity, 4 Islam, 1 comparison | Tight; no demonstrated need to resize |
| 8 | 12 | 5 connections, 7 research | Assessment and response bring the research allocation to the frame’s 9 days |
| 9 | 12 | 6 geography, 2 East Africa, 3 West Africa, 1 synthesis | Tight historical allocation; retain its full content |
| 10 | 9 | 1 living-peoples opening, 4 geography/map, 3 peoples, 1 synthesis | Reasonable |
| 11 | 12 | 4 geography, 1 society introduction, 7 report work | Requires strong source packs, but no demonstrated excess or shortage |

No unit is demonstrably far over or under its load. Unit 11’s report must teach and explain the selected society’s content, rather than become seven days of writing procedures.

Each unit has one assessment and one respond day. None exceeds 25 days, so no mid-unit assessment is required. Response time is counted once. The delayed action reflection is correctly counted as teaching, not as another assessment-response day.

### Lettered parts

| Standard family | Placement | Result |
|---|---|---|
| `MA.6.T2.6a` to `g` | Days 19 to 20, applied on 21 | All seven have explicit content |
| `MA.6.T3b.4a` to `e` | Days 43 to 48 | All five have explicit content; assessment repair remains |
| `MA.6.T3e.3a` to `d` | Days 87 to 92 | All four have day placements; finding 3 completes part b |

## Calendar and same-year leans

Course-level checks fall on days 71 to 72, 114 to 115 and 157 to 158, matching target weeks 15, 23 and 32.

| Lean | Availability or bridge | Judgment |
|---|---|---|
| Social studies timeline to math negative numbers | Days 4 to 6 precede math unit 7, days 120 to 141 | Met |
| Social studies coordinates to math quadrants | Day 28 precedes math unit 7 | Met |
| Latitude to science climate | Day 28 precedes science unit 3, days 52 to 89 | Met |
| Science dating/deep time to early human interpretation | Science comes later; day 12 supplies a local evidence bridge | Met |
| Math graphing to climate graphs | Day 31 explains axes and reads the quantities separately | Met |
| ELA comparing accounts to unit 2 | ELA comes later; day 13 teaches comparison locally | Met |
| ELA purpose to Hammurabi | ELA teaches it by about day 45; day 47 also carries a bridge | Met |
| Writing systems to ELA | Social studies days 80 to 82 precede ELA unit 4, days 87 to 108 | Met |
| ELA research to unit 8 | ELA unit 3, days 63 to 86, precedes day 105 | Met |
| ELA comparing accounts to final report | ELA’s early unit 6 work precedes report work beginning day 148 | Met |

Math’s final data project and the social studies final report occupy overlapping unit windows. Their exact product dates remain a unit-planning coordination issue; the available evidence does not establish a two-week collision.

## Candidate cells and source map

- **Catalhoyuk:** settled as the worked town on day 16, with no additional day. Keep it.
- **Judaism after 70 CE:** settled at approximately half of day 89. Keep it. [California 6.3.5](https://www.cde.ca.gov/BE/ST/SS/documents/histsocscistnd.pdf#page=31) supports this continuation.
- **Other candidate cells:** none require a decision.
- **Whole-course source map:** not applicable because no whole-course base text is adopted. References to possible partial bases do not establish lesson placement. Any later adoption of base lessons needs its placement, exclusions and order changes recorded.

## Scope and sequence lens checklist

| Checklist line | Status | Evidence |
|---|---|---|
| Compelling questions require the unit’s sources and allow defensible answers | Met in design | Questions lead to evidence-based comparisons or explanations; actual source sufficiency remains unjudged |
| History follows time order or gives a reason | Met | Regional organization is stated; the faith grouping and later connection synthesis explain departures |
| Contested history includes more than one telling | Met in design | Changing human-origin interpretations, Kush records and Indigenous accounts provide explicit comparisons |
| Writing from sources recurs and grows | Met | Early claims, the law argument, unit 8 report and longer unit 11 report |

The broader lens requirements for geography, economics, living peoples, religious study and student-chosen action are visible. Findings 1 to 3 address remaining specification gaps. Source difficulty, rights lines, daily sourcing prompts and final sensitivity accuracy require the later materials.

## What is right and should remain

- The timeline, regional reasoning and writing progression.
- Explicit local bridges instead of waiting for later subjects.
- Living Indigenous communities introduced through their own materials.
- Religions taught historically, without devotional practice.
- Unseen-source assessment tasks and protected respond days.
- The delayed action reflection.
- The present 11-unit, 160-day structure.

## Settled by the expert

These are directions for the caller to apply. No changes were made.

| Choice | Reason | Files affected |
|---|---|---|
| Keep unit order, ownership and day totals | No demonstrated structural defect | Target frame, sequence and day CSV |
| Make assessment evidence explicit, including named products where appropriate | Secures coverage without adding assessment days | Sequence and assessment-day rows |
| Add the specific C3 and anchor tasks in findings 2 and 3 | Completes existing claims | Named day rows, sequence prose, relevant progression notes and anchor paraphrase |
| Treat day 75 as retrieval | The prerequisite was used in grade 5 | Progression, frame, sequence, days 75 to 76 |
| Keep reflection on day 55 | Preserves delayed reflection and unit totals | Sequence and generated-calendar process |
| Provide a 45-minute route for the same calendar | Meets the required shorter-path provision | Sequence, later verified through unit-plan timings |
| Close the ELA large-product note | Current ELA frame resolves the stated uncertainty | Sequence “For the lead” item 3 and day 110 note |

## For Cory

- None required from this read. The repairs retain the course’s scope, unit ownership and approved audiences, and require no spending or outside contact.

## Limits, sources and source-list additions

This is a sequence review, not a finished-course adoption review. I could not judge actual assessment items, translations, reading difficulty, source balance, rights clearance or classroom timing. No substantive finding rests solely on memory; pacing judgments are professional judgments.

- [Massachusetts 2018 History and Social Science Framework](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf): checked grade 6 requirements against the local records and day descriptions.
- [C3 Framework, revised June 2017 PDF](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf): checked claimed indicator demands.
- [California History–Social Science Standards](https://www.cde.ca.gov/BE/ST/SS/documents/histsocscistnd.pdf): confirmed the Judaism-after-70 candidate.
- [Investigating History grade 6 guidebook](https://www.doe.mass.edu/investigatinghistory/curriculum/g6-course-guidebook.pdf): compared regional organization and the distinction between performance and content assessment.
- [Oak history curriculum explanation](https://support.thenational.academy/our-history-curriculum): limited comparison of chronology, prerequisites and inquiry sequences.
- [Oak early-civilizations comparison lesson](https://www.thenational.academy/teachers/lessons/comparing-the-earliest-civilisations): inspected its stated purpose and placement, without treating younger-grade material as evidence of grade 6 sufficiency.

**For the source list:** add the Oak curriculum-explanation route, recording that only its sequencing and inquiry guidance was inspected. The other principal routes are already recorded in APPROACH-SOURCES.

**Verdict:** revise before unit planning. **Finding count:** 6. **Report path:** `docs/reviews/sequence-world-geography-and-ancient-civilizations-i-2026-11-14.md`, delivered here only.


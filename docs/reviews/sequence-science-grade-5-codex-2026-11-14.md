# Independent cold read: Science Grade 5 scope and sequence

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/sequence-science-grade-5-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files changed.

## Verdict

Revise before unit planning: the six-unit order and allocations are coherent, but the water-distribution model contains an incorrect category and several prerequisite returns use retrieval where this brief requires readiness. The largest risk is building apparently complete standards coverage from graphs or assessment records that omit a required performance. Correct those reservations within the existing units, retaining their ownership, order and day totals.

## What I read

- `docs/agents/EXPERT.md`, the science lens and `docs/RUBRIC-SCIENCE.md`.
- FOUNDATION, APPROACH, relevant APPROACH-SOURCES entries, GLOSSARY, the required ROADMAP sections and BASELINE rules 20 to 24.
- The complete Grade 5 science scope and sequence, all 120 day rows, the complete frame and its `frames.csv` record.
- All Grade 5 science progression rows, their assumed earlier rows and intervening uses relevant to readiness.
- The owned performance expectations and their local dimension records.
- CALENDAR.md and the Grade 5 calendar rows for all four subjects.
- Both earlier Grade 5 science frame reviews, their fix dispositions and relevant earlier science sequence findings.
- The base-text record and outside sources linked below.

The blind-file boundary was preserved. Prior-run memory informed the review method only; findings rest on current files and sources checked during this read.

## Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Did not complete: importing `lesson.py` raised `ModuleNotFoundError: No module named 'markdown'`. |
| `python -X utf8 scripts/frame.py calendar` | Completed; no stagger-rule break reported. |
| `python -X utf8 scripts/frame.py check science-grade-5` | Passed, zero failures. |
| `python -X utf8 scripts/sequence.py check science-grade-5` | Passed, zero failures. |
| `python -X utf8 scripts/stale.py check` | Passed: 56 files, zero failures. |

The interrupted global gate does not prevent the substantive verdict.

## Findings, most serious first

### 1. The water graphs mislabel the freshwater remainder and conceal separately available reservoir quantities

**Severity:** Major  
**LAYER:** sequence, frame, progression  
**REPEAT:** yes, reservoir graphing was finding 4 in the earlier Grade 5 frame cold read  
**Confidence:** firm

**Location:** Scope and sequence, unit 5, lines 69 and 112; `days.csv`, days 93 to 98 and 118; frame unit 5; `s5-water-distribution.notes`.

**What is wrong:** The proposed freshwater graph assigns about 69 parts to ice, 30 to groundwater and **1 to lakes, rivers and swamps**. In the cited water-source table, freshwater lakes hold 0.26%, rivers 0.006% and swamps 0.03% of freshwater. Their combined share is approximately **0.296%, not 1%**. Ground ice and permafrost account for much of the omitted remainder.

The all-water graph also treats “ocean” and “fresh” as exhaustive categories, omitting saline groundwater and saline lakes. These are category errors, beyond ordinary rounding. [USGS, Where is Earth’s Water?](https://www.usgs.gov/water-science-school/science/where-earths-water?items_per_page=6&page=1&qt-science_center_objects=)

Naming lakes and rivers inside one combined bar does not demonstrate graphing their different quantities, although the source supplies them separately. The official evidence statement calls for quantitative reservoir comparisons. [5-ESS2-2 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/5-ESS2-2%20Evidence%20Statements%20June%202015%20asterisks.pdf)

**Why it matters:** Students would explain water availability using a falsely enlarged surface-water store. A writer could also implement the current graph instructions faithfully without securing the claimed reservoir comparison.

**Exact fix:**

- Use **salt water versus fresh water** for the rounded overview. Identify oceans as the dominant saltwater reservoir, rather than equating all salt water with oceans.
- Preserve the freshwater change of whole, but use source-faithful categories and quantities. Do not assign the entire remainder to lakes, rivers and swamps.
- Add a small-reservoir inset distinguishing lakes and rivers. Supply quantities and appropriately labelled axes; require graphing and comparison, not percentage calculation.
- Keep combined ice categories explicitly labelled where the source combines them.
- Carry these requirements into days 98 and 118 and the coverage table.

Math unit 6, school days 79 to 90, precedes this water work on school days 114 onward. Supplied decimal shares therefore need not be restricted to Grade 4 whole-number hundred-square displays.

This finding **disagrees with the earlier settled 69/30/1 category assignment**. That earlier recommendation explicitly rested on memory. The live source table establishes the correction; it does not require changing the standard or unit allocation.

### 2. Five older prerequisite returns need readiness, and unit 1’s check conflicts with this run’s timing instruction

**Severity:** Major  
**LAYER:** sequence, progression, frame  
**REPEAT:** yes, conflicting prerequisite and readiness instructions recur in the earlier Grade 2 science sequence review, finding 5  
**Confidence:** firm

**Location:** Scope and sequence, lines 17, 29, 53, 65 and 152; corresponding day notes; frame readiness policy and seams.

**What is wrong:** The sequence applies a “content revisited” exemption to several rows last used in Grade 3. This run’s explicit rule requires readiness for assumed rows last used two or more grades back.

| Receiving unit | Assumed row | Last recorded use | Current treatment | Required placement |
|---|---|---|---|---|
| 2 | `s3-environment-traits` | Grade 3 | Retrieval on day 18 | Readiness in day 17’s final ten minutes |
| 2 | `s3-habitat-survival` | Grade 3 | Retrieval on day 23 | Readiness in day 17’s final ten minutes |
| 4 | `s3-magnet-static` | Grade 3 | Retrieval on day 62 | Add to day 61 readiness |
| 4 | `s1-sky-patterns` | Grade 3 for the patterns-practice link | Retrieval on day 63 | Add to day 61 readiness |
| 5 | `s3-climates` | Grade 3 | Retrieval on day 85 | Readiness in day 84’s final ten minutes |

The Grade 3 use of `s1-sky-patterns` explicitly concerns predicting motion, rather than reteaching sky content. Even accepting Grade 3 as its last use, it remains two grades back.

Unit 1 places `s2-pieces-new-object` readiness after its first-day hook. GLOSSARY and sequence-write currently permit that exception, but **this run explicitly requires the start-of-year check and keeps every unit’s first day clean**. The supplied brief controls this review.

**Why it matters:** The plan can begin dependent work before identifying missing older knowledge. Conflicting instructions also make faithful implementation depend on which file a writer follows.

**Exact fix:** Apply the placements above and specify the short targeted support or extension each result selects inside the receiving unit. Move unit 1’s readiness to the start-of-year check before its hook. Identify its calendar slot explicitly rather than silently adding a numbered science meeting.

Retain the correctly placed readiness on day 44 for Grade 2 properties, material choice and thermal changes, and day 61 for daylight and seasons. Retain retrieval for Grade 4 rows, earlier same-year learning, `s2-water-where` maintained through Grade 4 maps, and the force-arrow thread maintained through Grade 4 collisions.

### 3. Course-level check day 42 claims the complete measurement standard using supplied measurements alone

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, incomplete practical assessment evidence recurs in the Grade 1 science sequence review, finding 1  
**Confidence:** firm on the requirement; likely on the omission allowed by the wording

**Location:** Scope and sequence, check 1 and coverage table; `days.csv`, day 42.

**What is wrong:** Day 42 lists full `5-PS1-2`, but its materials are raw measurement sheets and graph paper. It names neither student measurement nor an assessed earlier measurement performance.

Reading supplied weights and graphing them assesses analysis. It does not, by itself, assess measuring weights. The official performance description retains both measurement and graphing. [Grade 5 evidence statements, PDF page 2](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/5th_Grade%20Evidence%20Statements%20June%202015%20asterisks.pdf#page=2)

**Why it matters:** A student could receive a complete-code result without evidence of performing the measurement component. The sequence’s honest warning that record-based substitutes are weaker does not complete this particular assessment reservation.

**Exact fix:** State in day 42 that the assessed evidence includes each student’s identifiable observed weighing record from day 16, alongside the new heating, cooling and mixing analysis. Alternatively, reserve a brief observed measurement station within day 42.

For a route with no measurement opportunity, record that component as **not yet observed**, rather than treating the supplied-data task as complete practical evidence. Keep the check and response allocations.

### 4. The materials allowance is stated, but unit cost estimates are still deferred

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, the same omission appears in the kindergarten science sequence review, finding 4, and Grade 2 review, finding 4  
**Confidence:** likely

**Location:** Scope and sequence, Materials, lines 122 and 126; all six unit descriptions.

**What is wrong:** “Under about 30 dollars per unit” is the approved allowance. It is not an estimate showing that each proposed materials route fits it. Actual costing is deferred to unit plans, although the science rubric explicitly assigns **S6, costs**, to this layer.

**Why it matters:** One shared scale or tester, classroom eye protection, reusable containers and consumables have different quantity and reuse assumptions. Those assumptions affect both affordability and the practical assessment route.

**Exact fix:** Add a six-row provisional cost table for the stated class of 30. Separate assumed classroom stock, new reusable equipment and consumables; show quantities, reuse and estimated additional cost. Count shared purchases once and identify the minimum equipment retained on the reduced-materials route.

Use dated estimates and preserve the approved ceiling. A proposed increase belongs to Cory.

### 5. Active authoring inputs still contain contradictory calendar, coverage and review instructions

**Severity:** Minor  
**LAYER:** frame, process  
**REPEAT:** yes, stale control statements recur in the kindergarten science sequence review, finding 5, and Grade 2 review, finding 5  
**Confidence:** firm

**Location:** Frame Days and Cross-subject sections; science rubric Gateway 2 coverage row, S5 and Questions for Cory.

**What is wrong:** The stale gate passes, but these contradictions remain:

| Input | Conflict | Exact fix |
|---|---|---|
| Frame Days bullet | Says five meetings occur in three of weeks 8 to 10, then four weekly meetings resume. | State the stored pattern: five meetings in weeks **4, 7 and 10**, three in **11, 17 and 24**, four in the other weeks. |
| Frame ELA availability | Uses older ranges, including unit 3 at 83 to 121 and unit 4 at 122 to 156. | Align with the current calendar: unit 2 **42 to 80**, unit 3 **84 to 123**, unit 4 **124 to 156**. |
| Rubric coverage status | Says dimension statements exist in no data file. | Acknowledge `ngss-pe-dimensions.csv`; retain the requirement to verify its instructional and assessment use. |
| Rubric S5 and Questions for Cory | Still require the superseded science-teacher safety read. | Align with current FOUNDATION 7.3’s safety-agent requirement. Preserve separate human pilot requirements. |

**Why it matters:** Later writers can receive incompatible requirements from current control files. The sequence already flags several discrepancies, but disclosure leaves both instructions active.

The frame and progression readiness wording also need the alignment specified in finding 2.

## Order, standards and load

All 14 owned expectations have teaching and end-of-unit assessment reservations. They have no lettered subcodes; completeness depends on their substantive performances and dimension elements.

| Unit | Owned expectations | Teaching days | Assessment + response | Judgment |
|---|---|---:|---:|---|
| 1 | `5-PS1-1`, `5-PS1-2` | 15 | 2 | Particle evidence precedes conservation applications; heating, cooling and mixing are reserved. |
| 2 | `5-LS1-1`, `5-LS2-1`, `5-PS3-1` | 22 | 2 | Plant-source arguments precede matter cycling; the food web precedes energy tracing. |
| 3 | `5-PS1-3`, `5-PS1-4` | 15 | 2 | Properties become evidence before controlled mixing claims. |
| 4 | `5-PS2-1`, `5-ESS1-2`, `5-ESS1-1` | 18 | 2 | Center-directed gravity, three sky datasets and relative-distance arguments have distinct runs. |
| 5 | `5-ESS2-1`, `5-ESS2-2` | 13 | 2 | Interaction modeling precedes distribution; the water work needs finding 1. |
| 6 | `5-ESS3-1`, `3-5-ETS1-3` | 16 | 2 | Source synthesis precedes design; testing, graphing, failure analysis and revision are protected. |
| **Total** | **14 expectations** | **99** | **12** | **111 unit days, plus nine course-level days.** |

No whole unit is demonstrably far over or under its load. Unit 2’s 24 days support three linked expectations and continuing observations. Unit 4’s eight-day sky run carries three datasets, and unit 6’s design allocation permits repeated testing rather than a single demonstration.

No unit exceeds 25 days, so no mid-unit assessment is required. Response time is counted once.

Apart from the findings above, the reservations explicitly include the previously vulnerable ecosystem exchanges, newcomer effects, food uses, property comparisons, controlled trials and unfamiliar engineering performance. These are planning commitments, not verification of unwritten items or scoring guidance.

## Calendar, checks, candidates and shorter path

- **Check weeks:** 10, 21 and 30 match CALENDAR.md. The Grade 5 calendar shows no course-check collision.
- **Same-year leans:** Whole-gram weighing, bar graphs, supplied distance scales, source organizers, modeled synthesis and Grade 4 line plots provide explicit bridges. Science’s water-distribution work precedes ELA’s water unit.
- **Non-repetition:** The scope and sequence explicitly assigns earlier air-and-weight contexts to check 1, earlier apparatus/material contexts to check 2 and earlier air/material contexts to check 3. This meets the purpose reservation at this layer. The eventual items must make those connections substantive.
- **Candidates:** All six are settled. Leaf litter, minerals and watershed mapping each cost one existing day. Scent demonstration, home night observation and younger-class talk are dropped with reasons.
- **Shorter period:** The 30-minute guidance preserves evidence, model revision, safety, assessments and response.
- **Shorter year:** Ten named fold-ins are supplied: days **26, 37, 51, 58, 66, 74, 78, 91, 96 and 114**. None is an assessment or response day; continuing observations are retained.
- **Further shortening:** The separate 90-meeting route remains explicitly unestablished and assigned to unit planning. The ten-day option does not prove that larger reduction.
- **Source map:** Not applicable. This course has no base text.

## Science lens checklist: scope and sequence

| Lens line | Result | Evidence |
|---|---|---|
| Unit anchors are phenomena or problems, rather than topic headings | **Met** | Pumped ball, historical tree growth, unknown powders, falling objects and sky patterns, water scarcity and runoff. |
| Models are built before later work uses them | **Met** | Particles precede plant matter and material changes; food webs precede energy tracing; water systems precede protection design. |
| Engineering expectations appear through design work | **Met** | Unit 6 includes alternatives, controlled repeated tests, failure points and revision. |
| Equipment has substitutes or a no-kit path | **Met at reservation level** | Alternatives are named throughout. Findings 3 and 4 address assessment evidence and cost. |

At the rubric’s scope layer, phenomena, ordering, source choice and band boundaries are substantially secured. Full coverage remains incomplete where findings 1 and 3 apply. Prerequisite treatment needs finding 2, and S6 costs need finding 4.

## What is right and should remain

Keep the six-unit order, first-week plant preparation, qualified interpretation of historical evidence, separate matter and energy arrows, controlled-comparison sequence, three sky datasets and unfamiliar engineering assessment.

Also preserve the distinction between clearer water and safe drinking water, the absence of household water-access questions, and the explicit limits of supplied-data substitutes.

## Settled by the expert

| Choice | Reason | Files touched by the caller |
|---|---|---|
| Correct the water categories and add a small-reservoir inset | Preserves source accuracy and quantitative comparison without percentage procedures | Sequence, day notes, frame and progression water row |
| Readiness on days 17, 61 and 84 for the five older returns | Applies this brief’s last-use rule immediately before receiving units | Sequence, day notes and prerequisite wording |
| Put unit 1 readiness in the start-of-year check | This run explicitly keeps its first day clean | Sequence and start-of-year assessment reservation |
| Include day 16’s identifiable weighing evidence in day 42’s assessed record | Completes measurement evidence without another check day | Day 42 and check description |
| Retain the existing unit order, allocations, candidates and ten fold-ins | Their instructional purposes are defensible | No structural change |
| Add six provisional cost estimates within the existing allowance | Tests the proposed route without authorizing spending | Sequence materials table |
| Align control-file wording with the existing calendar and FOUNDATION | Removes contradictory instructions | Frame and science rubric |

## What I could not judge

Finished assessment items, scoring quality, actual station timing, apparatus reliability, selected plant datasets, purchase costs and completed safety implementation remain unverified.

`docs/APPROACH-SCIENCE.md` is absent. The subject-specific explanation of how the general approach operates in science therefore could not be read.

The earlier small-volume balloon decision was already adjudicated. I do not reopen it here or treat the apparatus as validated; the sequence appropriately retains measurement uncertainty and requires later resolution checks.

## Sources and source-list notes

- [Official Grade 5 evidence statements](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/5th_Grade%20Evidence%20Statements%20June%202015%20asterisks.pdf): performance requirements, dimension integration and assessment boundaries.
- [Official 5-ESS2-2 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/5-ESS2-2%20Evidence%20Statements%20June%202015%20asterisks.pdf): reservoir graphing requirements.
- [USGS water-distribution table](https://www.usgs.gov/water-science-school/science/where-earths-water?items_per_page=6&page=1&qt-science_center_objects=): checked categories and quantities. This reachable address is useful for the source register.
- [NGSS Appendix E](https://www.nextgenscience.org/sites/default/files/resource/files/AppendixE-ProgressionswithinNGSS-061617.pdf) and [Appendix F](https://www.nextgenscience.org/sites/default/files/resource/files/Appendix%20F%20%20Science%20and%20Engineering%20Practices%20in%20the%20NGSS%20-%20FINAL%20060513.pdf): progression and integrated practice principles.
- [EQuIP Science rubric](https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf): coherent lesson development and observable assessment evidence.
- [Current K–5 review criteria](https://cozy-dream-721ab6aab0.media.strapiapp.com/Science_20_K_5_20_Review_20_Criteria_2_0_ddd732f02c.pdf) and [evidence guide](https://cozy-dream-721ab6aab0.media.strapiapp.com/Science_20_K_5_20_Evidence_20_Guide_2_0_796df92bd4.pdf): targeted coverage, phenomena, assessment and pacing passages. These current links worked when the rubric’s older criteria link did not.
- [OpenSciEd elementary alignment overview](https://openscied.org/curriculum/elementary-school/standards-alignment/): sequence dependencies and flexible ordering. The full linked PDF returned 403 and the embed timed out; no pacing conclusion rests on the inaccessible document.
- [TERC Grade 5 overview](https://inquiryproject.terc.edu/curriculum/curriculum5/index.html) and [sequence chart](https://inquiryproject.terc.edu/curriculum/curriculum5/glance/5C_Overview.pdf): comparison of sustained measurement, models and evidence. Its additional content is not imported into this course.

The water correction rests on live verification, not memory. No finding depends on an inaccessible or paywalled source.

## For Cory

- **Audience and scope:** The existing question about whole-band state-test preparation remains open. This review adds no test-review content.
- **Time allocation, only if needed:** If no start-of-year assessment slot exists before course day 1, resolve the ten-minute allocation explicitly. Do not silently add a science meeting or take another subject’s time.

**Verdict:** Revise before unit planning. **Finding count:** 5. **Report path:** `docs/reviews/sequence-science-grade-5-2026-11-14.md`, supplied above, not written.


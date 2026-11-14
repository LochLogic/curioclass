# Chemistry course frame review, 2026-11-14

**Intended report path:** `docs/reviews/frame-chemistry-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files changed.

## Verdict

The frame is coherent in ownership, sequence, and overall time, but needs revision before the scope and sequence is built. Its biggest risk is that the supplied-data alternatives omit required investigation and construction performances while the course claims full coverage. Preserve the unit order and day allocations, and first make each route explicit about the performances students complete.

## What I read and checked

- `docs/agents/EXPERT.md`, the science lens, science rubric, foundation, shared approach, relevant roadmap sections, BASELINE rules 20 to 24, glossary, source record, source-list entries, and frame-writing guidance.
- The chemistry frame in full, its `frames.csv` row, all 20 grade 10 science progression rows, and the relevant incoming and outgoing progression links.
- The Biology and Physics frames, with their chemistry handoffs.
- Relevant Geometry, Algebra I, ELA 10, and World History II frame material, plus earlier-grade mathematics and writing progression entries.
- The earlier chemistry reviews, high school science fix report, and relevant earlier science findings for recurrence.
- Official standards, clarifications, boundaries, and selected evidence statements through the outside sources linked below.

Chemistry has no base text. The absent `data/plans/chemistry/source-map.csv` is therefore appropriate. `docs/APPROACH-SCIENCE.md` remains absent; I used the shared approach, science lens, and science rubric.

**Checks:** `plan.py check` could not finish because Python lacks `markdown`; `frame.py check chemistry` passed with 0 failures; `stale.py check` passed across 56 files.

The failed general gate does not withhold this verdict, following the explicit instruction for this read.

## Findings, most serious first

### 1. Supplied-data routes omit required practical performances

**Severity:** High  
**LAYER:** frame  
**REPEAT:** yes, the Grade 6 rerun, finding 5, also found a fallback that did not secure its investigation practice  
**Confidence:** firm

**Location:** Chemistry frame, “Labs and materials”; units 2, 3, 5, and 7.

**What is wrong:** The alternatives promise provided property data, cave-growth and freeze-thaw data, temperature logs, and solar-oven test results. Those support explanation and analysis, but do not establish how students plan and conduct investigations or build and refine a device.

The official evidence statements require students to make investigation decisions and collect evidence for HS-PS1-3, and to construct, test, evaluate, and improve their device for HS-PS3-3. The local science rubric, S6, also expressly rejects a fallback that drops its intended practice. [Investigation evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/HS-PS1-3%20Evidence%20Statements%20June%202015%20asterisks.pdf), [device-design evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/HS-PS3-3%20Evidence%20Statements%20June%202015%20asterisks.pdf).

**Why it matters:** A teacher or parent could complete the advertised alternative and record an expectation as complete without the student performing its required verb. This affects HS-PS1-3, HS-ESS2-5, HS-PS3-4, and HS-PS3-3.

**Exact fix:** Add this course rule:

> Each alternative identifies the student decisions, evidence collection, construction, testing, and revision it preserves. Reading supplied results alone is identified as partial coverage where an expectation requires investigation or physical construction. The unit plan names the practical opportunity still needed for completion.

Then revise the four unit notes:

- **Unit 2:** Students choose comparison conditions, controls, measurements, and repetitions, collect observations, and evaluate their investigation’s limitations.
- **Unit 3:** Preserve student planning and evidence collection in accessible mechanical and chemical investigations. Supplied rock-melting data may supplement these.
- **Unit 5:** Preserve a student-planned thermal investigation with recorded measurements and quantitative and conceptual interpretation.
- **Unit 7:** Preserve building, testing, and improving a device. Existing oven data can inform a design, but cannot replace its construction and testing.

Keep the supplied-data routes for access, with their limits stated.

### 2. Unit 2 promises that cooking oil disappears in the evaporation comparison

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, inaccurate anchor descriptions were also found in the earlier chemistry review, finding 5  
**Confidence:** firm

**Location:** Chemistry frame, unit 2 anchor and evaporation substitute.

**What is wrong:** The anchor says water, rubbing alcohol, and cooking oil on a paper towel “disappear at different rates.” Cooking oil leaves a persistent translucent mark on the classroom timescale. Spreading into paper also needs to be distinguished from evaporation.

The chemistry society’s comparison uses water and alcohol. The college laboratory manual explicitly distinguishes disappearing water marks from persistent lipid marks. [Water and alcohol investigation](https://www.acs.org/middleschoolchemistry/lessonplans/chapter5/lesson1.html), [college laboratory manual, grease-spot investigation](https://bio.libretexts.org/Courses/Harrisburg_Area_Community_College/BIOL_101%3A_General_Biology_l_-_Laboratory_Manual/01%3A_Labs/1.03%3A_Organic_Molecules).

**Why it matters:** The anchor supplies an inaccurate expected observation. A writer could interpret absorption as evaporation or ask students to explain a disappearance they do not observe.

**Exact fix:** Replace the opening observation with:

> Matched drops of water and rubbing alcohol dry at different rates, while cooking oil leaves a persistent mark. Water and alcohol also bead differently on the same clean surface.

Change the substitute note to:

> Compare water and rubbing alcohol under controlled conditions. Distinguish spreading from drying, and use evaporation as qualitative evidence alongside supplied property data, rather than as a direct measurement of vapour pressure.

Keep the unit’s question about particle attractions and designed materials.

### 3. Unit 1’s transition-metal investigations need an explicit extension label

**Severity:** Moderate  
**LAYER:** standard  
**REPEAT:** yes, the earlier chemistry review, finding 1, also concerned selecting proficiency cases inside assessment boundaries  
**Confidence:** firm

**Location:** Chemistry frame, unit 1, hands-on examples.

**What is wrong:** The unit restricts its assessed periodic predictions to main-group elements, but its named hands-on reactions use steel wool and copper without identifying them as enrichment. Iron and copper are d-block elements. Their reactions should not silently become proficiency evidence for the main-group predictions promised here. [Official boundaries](https://www.nextgenscience.org/topic-arrangement/hschemical-reactions), [structure and properties boundaries](https://www.nextgenscience.org/topic-arrangement/hsstructure-and-properties-matter), [iron](https://periodic-table.rsc.org/element/26/iron), [copper](https://periodic-table.rsc.org/element/29/copper).

**Why it matters:** Students could be asked to apply a simplified outer-electron model beyond the cases for which it was introduced, or teachers could assess the wrong evidence.

**Exact fix:** Add:

> Steel-wool and copper observations are optional enrichment about chemical change. They are not assessed periodic-prediction cases for HS-PS1-1 or HS-PS1-2. Required prediction and explanation tasks use the named main-group cases, with supplied observations or recordings where classroom reactions are unsuitable.

No new experiment or standard movement is needed.

### 4. The ELA forecast handoff overlaps by three days

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, same-year availability was an earlier chemistry finding; the current resolution still overstates this handoff  
**Confidence:** firm

**Location:** Chemistry frame, “Leans from the other subjects,” ELA row; high school science fix report, cross-subject ELA 10 note.

**What is wrong:** Chemistry says ELA 10 unit 7 comes after its forecast. Counting the unit days and intervening course checks gives:

| Work | Course days |
|---|---:|
| Chemistry unit 9 | 113 to 130 |
| ELA 10 unit 7 | 128 to 155 |
| Overlap | 128 to 130 |

The fix report consequently goes too far when it recommends removing ELA’s existing “if later” line.

**Why it matters:** The week labels conceal an opening dependency on a forecast that may still be unfinished. ELA already supplies a suitable fallback, so removing it would create an avoidable gap.

**Exact fix:** Replace the chemistry availability cell with:

> ELA 10 unit 7 begins on day 128; Chemistry unit 9 ends on day 130. ELA uses its supplied forecast reading until the chemistry forecast is complete, then may draw on that work.

Rewrite the corresponding fix-report recommendation to retain ELA’s existing fallback. No unit or day movement is necessary.

### 5. ELA 10 still says the chemistry frame is unwritten

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, earlier chemistry review finding 3 and the high school science fix report  
**Confidence:** firm

**Location:** `docs/courses/english-language-arts-grade-10/frame.md:154`.

**What is wrong:** The cross-subject introduction says “the chemistry frame is written later, so its units are not guessed.” The chemistry frame exists and supplies the required timing.

**Why it matters:** This leaves completed coordination looking unresolved and encourages unnecessary future checking.

**Exact fix:** Replace that clause with:

> Chemistry timing is recorded in docs/courses/chemistry/frame.md. Its forecast unit ends on day 130, while this course’s research unit starts on day 128; the forecast-reading fallback covers that overlap.

Keep the historical earlier review as a record of its original observation.

### 6. The science rubric’s nature-of-science gap note is stale

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale cross-file status notes recur in the earlier chemistry review  
**Confidence:** firm

**Location:** `docs/RUBRIC-SCIENCE.md:64`, Gateway 2 connections.

**What is wrong:** The note says no plan names where nature of science is taught. Chemistry explicitly names units 1, 8, and 9. Biology and Physics also name locations.

**Why it matters:** The note misidentifies the remaining work. Locations are planned; their instructional tasks and evidence still need development.

**Exact fix:** Replace the gap note with:

> Nature-of-science locations are named in the current high school frames: Biology units 5, 7 and 8; Chemistry units 1, 8 and 9; Physics units 3, 7 and 8. Unit plans must specify the tasks and evidence that develop these ideas.

The passing stale checker did not catch findings 5 and 6.

## Ownership, standards, and days

All **20 owned progression skills appear exactly once**, with no extra skill in the ownership column. All **21 chemistry expectations have one unit placement**. Across Biology, Chemistry, and Physics, all **71 high school expectations have exactly one owner**.

The following judgments concern frame commitments, not completed lessons or assessments. The comparison used the official [physical science](https://www.nextgenscience.org/sites/default/files/AllDCI.pdf), [Earth systems](https://www.nextgenscience.org/topic-arrangement/hsearths-systems), and [human sustainability](https://www.nextgenscience.org/topic-arrangement/hshuman-sustainability) descriptions.

| Unit | Days | Owned expectations | Judgment |
|---|---:|---|---|
| 1 | 16 | HS-PS1-1, HS-PS1-2 | Required content placed; distinguish enrichment, finding 3 |
| 2 | 15 | HS-PS1-3, HS-PS2-6 | Correct aims; findings 1 and 2 |
| 3 | 10 | HS-ESS2-5 | Mechanical and chemical work placed; practical fallback incomplete |
| 4 | 12 | HS-PS1-7 | Conservation, proportions, and mole placed |
| 5 | 18 | HS-PS1-4, HS-PS3-4, HS-PS3-1 | Earlier energy-case repair retained; practical fallback incomplete |
| 6 | 13 | HS-PS1-5, HS-PS1-6 | Rate and equilibrium-design commitments placed |
| 7 | 12 | HS-PS3-3, HS-ETS1-2 | Design and decomposition placed; construction fallback incomplete |
| 8 | 10 | HS-PS1-8 | Nuclear models, energy scale, and half-life placed |
| 9 | 18 | HS-ESS2-4, HS-ESS2-2, HS-ESS3-5 | Climate mechanisms, feedbacks, and forecast placed |
| 10 | 13 | HS-ESS2-6, HS-ESS3-6 | Quantitative carbon model and published-model interpretation distinguished |
| 11 | 12 | HS-ESS3-1, HS-ESS3-2 | Human activity and resource evaluation placed |

**Time:** 149 unit days plus 11 course-check and respond days equals 160 lessons, or 8,000 minutes. This fits the stated 32 instructional weeks and leaves approximately 20 days within a 180-day school calendar for other school demands.

No unit is demonstrably far over or under its load. Unit 5 and unit 9 each have 18 days for three expectations. The longer allocations per expectation in units 3, 4, and 8 reasonably accommodate reactivation, quantitative reasoning, investigations, or several nuclear models. Actual lesson timing remains to be established.

## Order, seams, and cross-subject readiness

- **Order:** Periodic patterns precede bulk properties; those precede water’s effects on materials. Conservation precedes energy accounting, energy precedes rate and equilibrium work, and these precede the device design. Climate precedes quantitative carbon and resource decisions.
- **Incoming seams:** Biology’s bond-energy, computational-model, carbon-cycle, feedback, and engineering handoffs are picked up. Older science knowledge has retrieval or readiness provisions.
- **Outgoing seams:** All 12 progression handoffs to Physics match its receiving frame.
- **Mathematics:** Earlier algebra, statistics, scientific notation, and integer exponents support the course. Geometry teaches some quantity work later, but chemistry supplies explicit bridges. Avoiding logarithms for pH is appropriate.
- **ELA and history:** Earlier writing supports early chemistry explanations. World History II bridges the science it encounters before chemistry. The forecast handoff needs finding 4.
- **Sources:** Chemistry correctly remains an original course with references, rather than mapping restricted reference lessons as a base text.

Two outside curriculum comparisons support treating the chosen sequence as defensible rather than mandatory: [OpenSciEd’s chemistry explanation](https://openscied.org/on-demand-hub/how-are-traditional-chemistry-topics-organized-in-openscied-high-school-chemistry/) integrates chemistry and Earth science through phenomena; [NJCTL’s chemistry sequence](https://njctl.org/materials/courses/chemistry-1/) places atomic structure, bonding, mole work, thermochemistry, and kinetics in a broadly comparable dependency order. Neither comparison justifies copying its tasks.

## Science lens checklist, course frame layer

| Checklist line | Result |
|---|---|
| Every owned expectation has a unit that sufficiently provides for it | **Missed in the fallback routes:** finding 1; boundary clarification in finding 3 |
| Grades 6 to 8 preserve the base-text order or explain departures | **Not applicable** |
| High school band expectations have named course owners | **Met:** 71 expectations owned once |
| Every unit names an anchor phenomenon or design problem | **Met in placement; scientific correction needed:** finding 2 |

Question boards, model revision, evidence-based explanation, transfer tasks, engineering, materials alternatives, and safety review are planned. Their implementation belongs to the unit and day reads. The [EQuIP rubric](https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf) supports examining actual integrated student performances; a frame cannot establish a numerical course score.

## What is right and should not be touched

Preserve the unit order, 160-day total, named ownership, reciprocal Biology and Physics seams, main-group limits, and the distinction between qualitative reaction energy and the thermal computational model.

Preserve the repaired Earth science coverage, the published-results boundary for HS-ESS3-6, explicit mathematics bridges, unseen transfer tasks, no-account and paper provisions, and the existing safety controls and qualified-reader requirement.

The earlier chemistry review’s principal repairs are present. I do not reopen them. This substantive verdict supersedes the earlier gate-blocked review’s decision to leave chemistry unjudged.

## Settled by the expert

| Choice | Reason | File affected when applied |
|---|---|---|
| Keep all unit allocations and the 160-day total | No demonstrated allocation defect | Chemistry frame |
| Use controlled water/alcohol drying observations; describe oil’s persistent mark accurately | Makes the anchor observable and scientifically sound | Chemistry frame, unit 2 |
| Identify transition-metal observations as enrichment | Keeps assessed periodic predictions inside their boundary | Chemistry frame, unit 1 |
| Retain ELA’s forecast-reading bridge through chemistry’s completion | The courses overlap on days 128 to 130 | Chemistry and ELA 10 frames; fix-report note |
| Replace both stale status notes with the wording above | Names the work that actually remains | ELA 10 frame; science rubric |

## What I could not judge

The frame does not establish final investigation protocols, actual materials costs, classroom timing, simulation quality, assessment items, or complete practice and crosscutting-concept element coverage. These require the subsequent unit plans and lessons.

No scientific finding rests on memory. Prior memory informed only the review method; findings use current repository evidence and the linked outside sources.

## For the source list

Add the linked HS-PS1-3 and HS-PS3-3 evidence statements, chemistry society water/alcohol investigation, college grease-spot investigation, and element fact pages to `docs/APPROACH-SOURCES.md`. They supplied direct evidence for findings 1 to 3.

The university-hosted laboratory PDF returned 404; its cached extract was not needed because the accessible college laboratory page supplied the relevant evidence.

## For Cory

- **People and money:** Name the qualified science teacher for investigation safety and materials, and the experienced reader for units 8 to 11; decide any pay.
- **Audience and scope:** If the no-kit route is intended to count as full course completion, decide how learners obtain the practical opportunities required by finding 1.

**Verdict:** Revise before scope-and-sequence development. **Finding count:** 6. **Report path:** `docs/reviews/frame-chemistry-2026-11-14.md`, supplied here only.


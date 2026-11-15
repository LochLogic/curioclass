# Independent cold read: Science, Grade 8 scope and sequence

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/sequence-science-grade-8-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files created, edited or deleted.

## Verdict

The six-unit order and overall allocations are defensible, but the sequence needs revision before unit planning. Its biggest risk is treating coverage-table promises as sufficient evidence of complete teaching and assessment, particularly for waves, galactic motion and conducting field investigations. Preserve the storyline and source order while correcting those reservations, prerequisite treatment, band-level accounting and materials costs.

**Finding count: 6 consolidated findings.**

## What I read and checked

Read in full:

- `docs/agents/EXPERT.md`, the science lens and `docs/RUBRIC-SCIENCE.md`.
- `docs/courses/science-grade-8/scope-and-sequence.md`.
- All 160 rows of `data/plans/science-grade-8/days.csv`.
- All rows of `data/plans/science-grade-8/source-map.csv`.
- The Grade 8 frame and `docs/courses/CALENDAR.md`.

Supporting reading included the Grade 8 progression rows, Grades 6 and 7 rows, relevant earlier prerequisite rows, Grade 8 calendar entries across subjects, the standards dimension file, foundation, approach, glossary, source policy, relevant roadmap and BASELINE guidance, and permitted earlier science reviews.

Outside verification used official standards, evidence statements, practice and crosscutting appendices, the science evidence guide, the unit rubric and all six published base-unit descriptions. No scientific finding rests on memory.

The prohibited files were not opened. No turn-taking, synchronization, defect-writing or other mutation command was run.

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Could not finish: sandbox Python lacks `markdown`. |
| `python -X utf8 scripts/frame.py calendar` | Passed; no stagger-rule breaks reported. |
| `python -X utf8 scripts/frame.py check science-grade-8` | Passed: 6 units, 160 days, including 4 course-level days. |
| `python -X utf8 scripts/sequence.py check science-grade-8` | Passed: 0 failures. |
| `python -X utf8 scripts/stale.py check` | Passed: 56 files, 0 marked failures. |

The unavailable repository-wide gate does not withhold this curriculum verdict.

## Findings

### 1. Three required components lack explicit teaching or complete assessment reservations

**Severity:** Major  
**LAYER:** sequence, standard  
**REPEAT:** yes, incomplete performance reservations recur in the earlier Grade 8 frame read, findings 1 and 4.  
**Confidence:** firm on the reservation gaps.

**Locations:** Coverage table, rows `s8-wave-amplitude-energy`, `s8-earth-sun-moon` and `s8-gravity-solar-system`; days 32 to 35, 93 to 96 and 99 to 103.

**What is wrong:** The coverage table is stronger than the daily contract in three places.

| Component | Current reservation | Exact fix |
|---|---|---|
| Wavelength within MS-PS4-1 | Day 45’s coverage-table entry names wavelength, but no teaching day explicitly develops or retrieves it. Days 33 and 34 name amplitude and frequency. | Add a spatial wave representation to day 34 alongside the time-based vibration representation. Distinguish wavelength, frequency and amplitude, then retain all three in days 45 and 75. Do not infer wavelength from an unlabeled time axis. |
| Complete MS-PS4-2 model | Brightness and light crossing empty space appear in the coverage table without an explicit daily task. The assessment descriptions emphasize light-material cases; contrasting the media needed by sound and light does not also demonstrate reflection, absorption and transmission of mechanical waves. | In days 94 and 95, explicitly revise the qualitative light-wave model for brightness, color and light crossing empty space. Reserve a paired sound-and-light material comparison on days 96 and 103, including reflection, absorption and transmission. |
| Galactic motion within MS-ESS1-2 | Days 99 to 102 develop solar-system orbits, formation and location within the Milky Way. Locating the solar system within a galaxy does not explicitly model gravity governing motion within that galaxy. | Extend day 102’s model to show stars, including the solar system, orbiting within the Milky Way under gravity. Require that relationship in day 103’s assessed model, alongside solar-system motion and disk formation. |

These requirements are explicit in the official [wave expectation](https://www.nextgenscience.org/pe/ms-ps4-1-waves-and-their-applications-technologies-information-transfer), [light and mechanical-wave expectation](https://www.nextgenscience.org/pe/ms-ps4-2-waves-and-their-applications-technologies-information-transfer), and [galactic-motion evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/MS-ESS1-2%20Evidence%20Statements%20June%202015%20asterisks.pdf).

**Why it matters:** A busy unit writer could follow every daily goal and still omit a component that the final coverage table promises to assess.

Keep the existing units and allocations. Replace repeated representations or reporting within the named days, and record the revised allocations in the source map.

### 2. Field-investigation assessments do not secure evidence that students conducted the investigation

**Severity:** Major  
**LAYER:** sequence, standard  
**REPEAT:** yes, incomplete practical assessment evidence recurs in the Grade 5 sequence read, finding 3.  
**Confidence:** firm.

**Locations:** Days 54, 55, 64, 65, 66, 73 and 75; coverage row `s8-fields`; materials paragraph at line 142.

**What is wrong:** The physical route includes students conducting magnetic and electric investigations. The assessed reservations, however, name investigation evaluations, explanations and improvements without explicitly retaining the students’ conducted-investigation evidence as an assessed performance.

The no-kit route substitutes supplied observations and measurements. The sequence correctly acknowledges that this is weaker and must not be described as students carrying out the investigation. That honesty leaves the full MS-PS2-5 claim unresolved for that route.

The standard requires conducting an investigation as well as evaluating its design. Its clarification permits investigations using simulations, which provides a possible solution. [Official expectation](https://www.nextgenscience.org/pe/ms-ps2-5-motion-and-stability-forces-and-interactions), [evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/MS-PS2-5%20Evidence%20Statements%20June%202015%20asterisks.pdf).

**Why it matters:** Evaluating someone else’s supplied investigation cannot establish that the student can conduct one.

**Exact fix:**

1. Name the magnetic records from days 54 and 55 and electric records from days 64 and 65 as assessed products: procedure followed, student-generated observations, design evaluation and improvement.
2. Explicitly attach those products or observed performances to days 66 and 73. Day 75 can reuse this practical evidence while requiring a new interpretation.
3. Give the reduced-materials route either a simple actual investigation or a learner-controlled simulation in which students select conditions and generate records.
4. Keep supplied-data analysis available, but identify the conducting component as incomplete until the student performs it.

This does not require repeating a complete practical investigation during each written assessment.

### 3. Readiness treatment follows the older idle-grade rule instead of this run’s last-use rule

**Severity:** Major  
**LAYER:** sequence, frame, progression  
**REPEAT:** yes, the same rule conflict appears in the Grade 5 sequence read, finding 2.  
**Confidence:** firm on the explicit placements and policy conflict.

**Locations:** Unit assessment paragraphs; days 1, 26, 28, 32, 76, 79, 82, 131 and 134; frame Days, Seams and Models carried sections.

**What is wrong:** This run requires readiness when an assumed row was last used two or more grades back. The sequence instead permits retrieval after a Grade 6 last use because only Grade 7 intervenes.

| Receiving unit | Row or model | Last recorded use | Current treatment | Exact correction |
|---|---|---|---|---|
| 1 | `s4-collisions`, `s3-balanced-forces`, `s4-speed-energy`, force diagram | Grades 4, 5, 4 and 5 | Readiness after day 1’s hook | Put these in the start-of-year check before the unit opens, as this run requires. Name its delivery slot without silently adding a numbered meeting. |
| 2 | `s4-wave-model` and wave model | Grade 6, through `s6-digital-signals` | Retrieval on days 28 and 32 | Add readiness to day 26’s final ten minutes. |
| 2 | `s6-light-paths` and light-ray model | Grade 6 | Retrieval on days 28 and 32 | Include in day 26 readiness. |
| 4 | `s5-shadows-sky` and Earth-sun-moon model | Grade 6, through `s6-climate-circulation` | Retrieval on days 79 and 82 | Include in day 76’s existing readiness allocation. |
| 6 | `s6-geologic-time` | Grade 6 | Retrieval on day 134 | Include a rock-layer ordering and time-scale prompt in day 131 readiness. |

Day 26 currently reserves 50 response minutes. Change that to 40 response minutes plus ten readiness minutes, with the corresponding source-map consolidation stated explicitly. Unit 2 must also name the support selected by those results within its existing days, rather than continuing to say that no readiness or reteaching is needed.

The unit 1 placement follows the current repository glossary and writing brief, which permit a first-day exception. **The supplied instructions for this run explicitly require the start-of-year check and a clean first-day hook, so they control this review.**

Two preceding-year prerequisites also lack explicit retrieval tasks:

- Add `s7-body-systems-food` retrieval before the ear-and-brain source synthesis on day 42.
- Add `s7-interaction-patterns` retrieval before the reproduction argument on day 136.

The launcher-energy work on days 14 and 15 also precedes the day 46 check of `s4-energy-device`’s stored-energy contribution. Make that contribution explicit in the start-of-year readiness and day 2 response, then treat its unit 3 return as retrieval.

**Why it matters:** The present treatment can discover an old prerequisite gap after dependent work has begun. Missing retrieval tasks also leave year-before handoffs as assumptions rather than planned student work.

Preserve the correctly placed readiness on days 46, 104 and 131 for the other older rows. Preserve retrieval for maintained particle energy, Grade 7 design and cell work, populations, and concepts taught earlier this year. I found no clearly established case of an unnecessary readiness check on a preceding-year row.

### 4. Full middle-school practice and crosscutting-element accounting is deferred past the required layer

**Severity:** Moderate  
**LAYER:** sequence, progression  
**REPEAT:** new in the permitted reports read.  
**Confidence:** firm on the missing accounting; substantive omissions remain unestablished.

**Location:** Standards and three-dimensional coverage, particularly line 123; frame Standard paragraph.

**What is wrong:** The table traces the elements attached to the course’s listed expectations. It then says unit plans must still count the full band obligations against Grades 6 and 7.

That is useful preparation, but it does not settle S11. Naming all eight practices and the crosscutting concepts does not show that their required elements are developed across the band. The official appendices distinguish those individual capabilities, and the evidence guide calls for locating their development across learning opportunities. [Practice appendix](https://www.nextgenscience.org/sites/default/files/Appendix%20F%20%20Science%20and%20Engineering%20Practices%20in%20the%20NGSS%20-%20FINAL%20060513.pdf), [crosscutting appendix](https://www.nextgenscience.org/sites/default/files/Appendix%20G%20-%20Crosscutting%20Concepts%20FINAL%20edited%204.10.13.pdf), [science evidence guide, indicators 2b and 2c](https://cdn.edreports.org/media/2025/07/Science-6-8-Evidence-Guide_2.0.pdf).

**Why it matters:** Grade 8 closes the band. Discovering an unplaced element during unit writing could require changing an already fixed sequence.

**Exact fix:** Add a band-completion matrix containing:

- Each required practice and crosscutting element.
- Its earlier Grade 6 or 7 teaching location, where present.
- Its Grade 8 development or application days.
- The observable evidence demonstrating it.

Use existing reservations where they suffice. Return any genuine allocation or ownership change to the lead rather than declaring the band complete by category names alone.

### 5. No unit has a provisional materials cost

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, the same deferral appears in the Grade 6 sequence read, finding 3.  
**Confidence:** firm.

**Location:** Source time, tools and materials, especially line 144; For the lead, item 3.

**What is wrong:** The sequence explicitly defers costs to unit planning. The science rubric assigns **S6 costs** to the scope-and-sequence layer.

Household alternatives and supplied-data routes are useful, but they do not establish the cost of classroom quantities, eye protection, force measurement, magnets, switched holders, printing or replacements.

**Why it matters:** The teacher cannot judge whether the proposed physical route is feasible, and the no-kit route has the practice limitation identified in finding 2.

**Exact fix:** Add six provisional unit estimates for the shared approach’s class of thirty, with a one-child equivalent where materially different. State quantities, assumed stock, new reusable equipment, consumables, printing, reuse between units, dated price sources and the minimum equipment retained on the reduced-materials route.

Count shared equipment once. Producing estimates does not authorize purchases or establish a spending ceiling.

### 6. Active supporting documents retain conflicting instructions and obsolete status notes

**Severity:** Minor  
**LAYER:** frame, progression, process  
**REPEAT:** yes, stale authoring instructions recur in the Grade 6 sequence read, finding 4.  
**Confidence:** firm.

The stale gate passes, but these unmarked contradictions remain:

| Location | Conflict | Exact fix |
|---|---|---|
| Frame opening | Says the scope and sequence sets days later, although the day-level sequence now exists. | Link the sequence and day record as the current draft. |
| Frame Days, Seams and Models carried; relevant progression notes | Permit Grade 6 last-use retrieval under the older idle-grade rule. | Align with finding 3’s last-use rule and readiness placements. |
| Frame Cross-subject | Gives qualitative functions as days 93 to 116 and scientific notation as 119 to 138. | Use the current calendar: **93 to 115** and **118 to 137**. |
| Frame unit 5 safety | Retains teacher-dispensed rubbing alcohol. The sequence replaces extraction with supplied observations. | Identify the supplied-observation route as the current adaptation and remove the obsolete handling instruction from this route. |
| Science rubric, Gateway 2 full-scope gap | Says dimension statements exist in no data file. | Acknowledge `ngss-pe-dimensions.csv`; retain the requirement to trace elements to teaching and evidence. |
| Science rubric S5 and Questions for Cory | Still require finding a science teacher for the safety read. | Align with current FOUNDATION 7.3’s safety-agent requirement, preserving the separate human pilot requirements. |

**Why it matters:** A later writer receives incompatible calendar, prerequisite, materials or review instructions depending on which input is opened.

These are consistency repairs to current decisions, not new staffing or scope decisions.

## Order, assessments and days by load

The sequence places all **26 progression rows**, representing **26 owned codes plus the applied MS-PS3-5 contribution**. These expectations have no lettered subcodes; completeness depends on their performances and constituent elements.

| Unit | Days | Expectations | Order and load judgment |
|---|---:|---:|---|
| 1. Contact forces | 26 | 5 owned | Collision evidence precedes force and energy explanations, then engineering. The first 17 days develop the science; nine days complete design work and assessment response. Defensible. |
| 2. Sound waves | 20 | 2 owned, plus wave contribution | Source motion precedes wave representation, transmission and receiver synthesis. Most time belongs to the wave development row. Defensible, subject to findings 1 and 3. |
| 3. Forces at a distance | 28 | 3 owned, 1 applied | Magnetic evidence precedes fields and stored energy. The 100 electric minutes and 50 gravitational minutes have explicit locations. Defensible. |
| 4. Earth in space | 28 | 5 owned | Seasons precede phases and eclipses; the red moon motivates optical revision. Scale and gravity close the unit. The final six days are dense, but no demonstrable whole-unit underallocation is established. |
| 5. Genetics | 27 | 5 owned | Environmental explanations precede inheritance and causal gene models. Whole-cell synthesis precedes protein reasoning; sexual-asexual comparison precedes final assessment. Defensible. |
| 6. Selection and ancestry | 27 | 6 owned | Fossil and anatomical patterns precede selection mechanisms, numerical models and embryo evidence. Short completion rows share evidence with the longer development rows. Defensible. |

No whole unit is demonstrably far over or under its load. Row counts alone would give a misleading comparison.

All five units exceeding 25 days have mid-unit assessments: days **17, 66, 96, 116 and 143**. Their reservations generally avoid assessing untaught later components. End-of-unit assessments fall on days **25, 45, 73, 103, 130 and 157**, with response allocations explicitly counted.

The named design, technology, cell, numerical-selection, embryo and reproduction products make the short final assessments more credible. Actual completion time and scoring quality remain unverified.

## Calendar, cumulative checks, candidates and shorter path

**Calendar:** Days 75 and 159 fall in target weeks **15 and 32**. Day 75 conflicts with no other subject’s mid-year course-level check. Shared finals week is permitted.

**Same-year leans:**

- Graph-shape bridges precede the later math functions unit.
- Scatter plots are available before the gravity and growth tasks.
- Written-out distances and earlier powers of ten avoid premature scientific notation.
- The earlier claim-evidence-reasoning frame supports the overlap with ELA argument writing.
- Unit 2 supplies its own source-synthesis support before ELA research.
- Science technology synthesis finishes on day 120, before ELA’s gene-claims unit begins on day 129.

**Checks that do not repeat:** Both cumulative-check descriptions explicitly draw the immediately preceding unit’s skills from earlier-unit contexts with new records. Preserve those instructions.

**Candidates:** All six cells are settled with zero additional days and explicit exclusions. No unresolved Candidate cell remains.

**Shorter path:** Both required forms are present. The ten unassessed folds are:

`4 into 3; 16 into 15; 29 into 28; 36 into 35; 56 into 55; 67 into 68; 81 into 80; 110 into 111; 135 into 134; 142 into 141.`

None of the folded rows carries an assessment marker. No owned component is explicitly deleted. The receiving-day timings, especially the investigation-adjacent folds at days 55 and 68, still need verification during unit planning.

The statement that a 150-meeting, 45-minute route is not established as equivalent is appropriate. Keep it.

## Source map

The map accounts for **91 base lessons**:

| Base unit | Lesson rows |
|---|---:|
| 8.1 | 16 |
| 8.2 | 14 |
| 8.3 | 12 |
| 8.4 | 17 |
| 8.5 | 17 |
| 8.6 | 15 |

Optional 8.1 lesson 16 is the only cut, with a reason. The remaining lessons retain numerical order. Additions and condensations are labeled.

Every referenced local source file exists. Each allocation sums to its row’s stated minutes, and every numbered course day totals 50 allocated minutes. This verifies the written budget, not classroom feasibility.

The published unit descriptions support the broad arcs: [contact forces](https://openscied.org/instructional-materials/8-1-contact-forces/), [sound](https://openscied.org/instructional-materials/8-2-sound-waves/), [forces at a distance](https://openscied.org/instructional-materials/8-3-forces-at-a-distance/), [Earth in space](https://openscied.org/instructional-materials/8-4-earth-in-space/), [genetics](https://openscied.org/instructional-materials/8-5-genetics/), and [selection and ancestry](https://openscied.org/instructional-materials/8-6-natural-selection-common-ancestry/).

Detailed retention of every archived lesson’s evidence was not independently verified. The sandbox lacks the PDF extraction packages and executable checked for that purpose.

## Science lens checklist: scope and sequence

| Lens line | Result |
|---|---|
| Anchors are phenomena rather than topics | **Met.** All six units begin with a specific explanatory puzzle. |
| Models are built before dependent use | **Missed locally.** The main arcs work; prerequisite treatment and several component reservations need findings 1 and 3. |
| Engineering expectations appear in units | **Met.** Unit 1 requires systematic comparison, testing and combining features. |
| Equipment has substitutes or a no-kit path | **Met for availability; missed for full practice equivalence.** Alternatives are named, but finding 2 applies to conducting investigations. |

For the rubric’s sequence-layer responsibilities, phenomenon-driven planning, base choice, broad coherence and band boundaries are supported. Full coverage needs findings 1, 2 and 4; costs need finding 5. This is a plan-level judgment, not a score for unwritten lessons.

## Settled by the expert

These are item-level choices for the caller to apply. None was applied during this read.

| Choice | Reason | Files affected |
|---|---|---|
| Keep all six units, their order and allocations | The prerequisite arcs and base sequence are defensible | Frame and sequence |
| Explicitly teach wavelength on day 34 | Prevents assessing an unassigned component | Sequence; days.csv |
| Complete the light model on days 94 and 95 | Places the coverage-table promises in daily work | Sequence; days.csv |
| Add galactic motion to day 102 and its assessed model | Location within a galaxy does not explain motion within it | Sequence; days.csv |
| Assess conducted field-investigation records | Preserves the standard’s practical performance | Sequence; days 54 to 75 |
| Place readiness on days 26, 76 and 131 as specified | Applies this run’s last-use rule near the receiving unit | Sequence; source map; supporting notes |
| Put unit 1 readiness in the start-of-year check | This run keeps the first-day hook clean | Sequence and start-of-year reservation |
| Retain the optional selling-designs omission | No owned expectation depends on it | Source map |
| Add band-element accounting and provisional costs | Both belong at this layer | Sequence and supporting coverage record |

## What is right and should remain

Preserve the evidence-driven model revisions, force and energy work before sound, explicit electric and gravitational additions, whole-cell synthesis before gene-protein reasoning, and inheritance before selection.

Also preserve the unfamiliar transfer cases, individual explanations attached to products, respectful genetics and hearing provisions, supplied extraction observations, clear evolution teaching, and the distinction between model feeding success and inherited population change.

Earlier frame concerns about missing additions, separate energy graphs, sensory synthesis, causal mutation models, embryo comparisons and reproductive argument now have substantive reservations. They should not be reopened as wholly absent.

## What I could not judge

- Actual assessment duration, scoring, accommodations and item completeness.
- Classroom feasibility of the minute allocations and shortened routes.
- Final apparatus procedures, setup, cleanup and completed safety implementation.
- Current school inventory and purchase costs.
- Complete band-element coverage, pending finding 4’s matrix.
- Detailed retained evidence in every archived base lesson.
- The unwritten `APPROACH-SCIENCE.md`.

The [unit-review rubric](https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf) was used for coherence and observable-performance principles, not to assign a finished-unit rating.

## For the source list

The accessible [Grade 6 to 8 science evidence guide](https://cdn.edreports.org/media/2025/07/Science-6-8-Evidence-Guide_2.0.pdf) supports element-level coverage and assessment review. Relevant passages were read; the full 91-page guide was not read.

Retain the specific MS-PS2-5 and MS-ESS1-2 evidence-statement links above if they are absent from the source register.

## For Cory

- **Money:** Decide any materials allowance or purchase only after the six provisional estimates are supplied.
- No new scope, audience or outside-person decision is recommended by this read.

**Verdict:** Revise before unit planning. **Finding count:** 6. **Report path:** `docs/reviews/sequence-science-grade-8-2026-11-14.md`, supplied here only.
# Independent cold read: Science Grade 6 scope and sequence

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/sequence-science-grade-6-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files changed.

## Verdict

Revise before unit planning, while retaining the six-unit order and current day allocations. The largest risk is declaring complete standards coverage where the regional-climate work omits two interactions, alongside a cumulative assessment that requires an explicitly untaught cooling mechanism. Correct those reservations, add provisional materials costs, and align the stale authoring instructions.

**Finding count: 4.**

## What I read

- `docs/agents/EXPERT.md`, the science lens, `docs/RUBRIC-SCIENCE.md`, FOUNDATION, GLOSSARY, the shared APPROACH, relevant APPROACH-SOURCES entries, the required ROADMAP sections and BASELINE rules 20 to 24.
- The complete Science Grade 6 scope and sequence, all 160 day rows, the frame and all 86 source-map rows.
- All Grade 6 and Grade 5 science progression rows, the assumed Grade 3 and Grade 4 rows, and intervening uses relevant to readiness.
- The local performance-expectation and dimension records for all 14 owned expectations and the light contribution.
- CALENDAR.md and every Grade 6 calendar row.
- Earlier Grade 6 frame reviews, the science baseline review and fixes, science data-gap documentation, and relevant permitted science sequence reviews.
- Stored base-program unit-page text and the outside sources linked below.

The blind-file boundary was preserved. Prior-run memory informed report structure and review method only. No subject finding rests on unverified memory.

## Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Did not complete: `ModuleNotFoundError: No module named 'markdown'`. |
| `python -X utf8 scripts/frame.py calendar` | Passed; no stagger-rule break reported. |
| `python -X utf8 scripts/frame.py check science-grade-6` | Passed, zero failures; six units, 160 days. |
| `python -X utf8 scripts/stale.py check` | Passed: 56 files, zero failures. |

The interrupted general gate does not withhold this verdict.

## Findings, most serious first

### 1. The regional-climate reservation omits ice and living-things interactions

**Severity:** Major  
**LAYER:** sequence, standard  
**REPEAT:** yes, incomplete substantive standard coverage is the same kind as finding 3 in the earlier Grade 6 frame cold read  
**Confidence:** firm

**Location:** Scope and sequence, unit 3 and the MS-ESS2-6 coverage row; `days.csv`, days 85 to 89.

**What is wrong:** The climate arc explicitly reserves latitude, sunlight angle, rotation, temperature, salinity, continents, altitude and distance inland. It does not reserve how **ice and living things interact with the climate system**, although those are included in the claimed ESS2.D element.

Day 64 places ice and living things on water-cycle paths. That supplies useful prior knowledge, but it does not yet make their effects on weather and climate part of the regional model. The official foundation element includes these interactions, and the local dimensions file preserves them. [MS-ESS2-6 and its foundation elements](https://www.nextgenscience.org/pe/ms-ess2-6-earths-systems)

**Why it matters:** A writer could implement every stated climate task faithfully and still omit these relationships. Day 89’s promise to cover every part would then exceed the teaching reservation.

**Exact fix:**

- On day 64, explicitly retain plant transpiration as a contribution to atmospheric moisture.
- On day 85, include supplied evidence comparing sunlight reflected and absorbed by ice-covered and darker surfaces, using the light and energy models already taught.
- On day 88, require the regional model to connect those two relationships with the atmosphere and water pathways, alongside the existing geographic comparisons.
- On day 89, name ice-cover and vegetation evidence in the unfamiliar region and require students to use it in their model.
- Add these teaching and assessment locations to the MS-ESS2-6 coverage row.

Use one integrated model rather than adding a separate report. No new expectation, numerical radiation calculation or unit allocation is needed.

### 2. The mid-year dew case requires an unreserved cooling mechanism

**Severity:** Major  
**LAYER:** sequence  
**REPEAT:** new in the permitted course and layer reports read  
**Confidence:** likely on the instructional omission; firm on the physical mechanism

**Location:** Scope and sequence, Course-level checks, line 137; `days.csv`, day 90; frame Course-level check 1.

**What is wrong:** Explaining why dew forms on exposed grass but not beneath a tree requires more than condensation and the absorption of visible light. The contrast depends on nighttime radiative energy exchange between surfaces, the sky and overhead cover. The day record explicitly teaches light absorption, particle collisions, fluid circulation and condensation, but never explicitly builds thermal emission and the effect of overhead cover on net cooling. [National Weather Service, dew and frost development](https://www.weather.gov/source/zhu/ZHU_Training_Page/fog_stuff/Dew_Frost/Dew_Frost.htm), [National Weather Service, heat transfer](https://www.weather.gov/crp/weather_education)

The same reservation says four panels assess the full ray contribution, but names no transparent-boundary bending performance. “Light/energy paths” does not itself reserve refraction.

**Why it matters:** A correct student model based on the stated teaching may be insufficient to explain the tree contrast. Conversely, a general condensation answer could receive credit without demonstrating the ray contribution the check lists.

**Exact fix:** Replace the grass/tree comparison with an unfamiliar cold-container display case assembled from earlier units’ content. Specify four evidence panels:

1. A ray model accounting for reflection, transmission, absorption and bending at a transparent boundary.
2. A thermal investigation plan comparing mass and kind of matter, with controlled conditions and temperature records.
3. A before-and-after particle kinetic-energy argument identifying energy transferred into or out of the sample.
4. Pure-substance particle predictions for state changes when energy is added or removed, including condensation on the cold container.

Keep the case unfamiliar, retain day 90 and its four listed codes, and retain day 91’s response allocation. State explicitly that the unit 3 state-change sampling uses earlier cup and cold-surface content.

This fixes the assessment reservation without requiring a new teaching topic.

### 3. Materials alternatives are named, but unit costs remain deferred

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, Grade 5 science sequence review, finding 4  
**Confidence:** firm on the missing estimates

**Location:** Scope and sequence, Materials, tools and source decisions; For the lead, item 2; all six unit descriptions.

**What is wrong:** The sequence identifies shared devices, household substitutes and weaker record-based paths, but supplies no provisional unit cost estimates. It expressly defers pricing to unit plans. The science rubric assigns **S6, costs**, to the scope-and-sequence layer.

**Why it matters:** A teacher cannot tell whether the proposed physical investigation route is feasible. One shared thermometer, classroom eye protection, microscopy equipment and consumables have different quantity and reuse assumptions. These choices also determine which practical performances students can actually carry out.

**Exact fix:** Add a six-row provisional materials-cost table stating:

- The classroom quantity assumption.
- Equipment assumed already available.
- New reusable equipment and consumables.
- Sharing and reuse across units.
- Estimated additional cost, with dated sources.
- Minimum physical equipment retained on the reduced-materials route.

Count shared purchases once. Identify separately the cost and instructional limitation of the microscopy route. Estimates can remain provisional; a purchasing decision is not required to produce them.

### 4. Current frame, progression and rubric instructions still contradict the sequence

**Severity:** Minor  
**LAYER:** frame, progression, process  
**REPEAT:** yes, Grade 5 science sequence review, finding 5, and earlier Grade 6 stale-note findings  
**Confidence:** firm

**What is wrong:** The stale gate passes, but these authoring contradictions remain active.

| Location | Conflict | Exact fix |
|---|---|---|
| Frame Days policy | Counts intervening idle grades, allowing retrieval after a Grade 4 last use. This run requires readiness for an assumed row last used two or more grades back. | Replace the policy with this run’s last-use rule and distinguish readiness before the unit from retrieval inside a day. |
| Frame unit 4, Seams and Models carried | Still prescribe retrieval for rock layers and stability-change. | Name readiness in day 91’s final ten minutes and targeted response on day 93. Keep erosion and feature-map retrieval because Grade 5 maintains them. |
| Frame unit 5 and wave-model entry | Still prescribe wave retrieval. | Name readiness in day 115’s final ten minutes and response on day 117. Keep information-code retrieval through Grade 5’s recorded use. |
| Grade 6 progression notes | Rock-layer, stability-change and wave returns retain the older retrieval instructions. | Align the relevant notes with the placements above. Do not change ownership. |
| Frame mathematics availability | Statistics remains at days 143 to 158 and rational numbers at 121 to 142. | Use the current calendar: statistics **142 to 157**, rational numbers **120 to 141**. The sequence already uses these ranges. |
| Science rubric, Gateway 2 gap | Says dimension statements exist in no data file. | Acknowledge `ngss-pe-dimensions.csv`; retain the requirement to trace its elements into teaching and assessment evidence. |
| Science rubric S5 and Questions for Cory | Still require finding a science teacher for the safety read. | Align with current FOUNDATION 7.3’s safety-agent requirement, preserving the required safety review and separate human pilot requirements. |

**Why it matters:** A later writer can receive incompatible readiness, coverage or review requirements depending on which current input is opened. The sequence’s explanation of the discrepancy is helpful, but leaves the competing instructions available.

These are consistency repairs to existing decisions, not new scope or staffing decisions.

## Order, standards, assessments and load

The course places 14 progression rows. Thirteen rows own 14 expectations, while the remaining row contributes the ray portion of MS-PS4-2. These expectations have no lettered subcodes; completeness depends on their substantive performances and dimension elements.

| Unit | Days | Owned expectations | Order and load judgment |
|---|---:|---:|---|
| 1. Light and matter | 17 | 0, plus one contribution | Observation and competing models precede controlled light comparisons. The allocation includes year routines, safety and the ray contribution. |
| 2. Thermal energy | 34 | 3 | Matter paths precede particle-transfer mechanisms; mechanisms precede prototype construction and revision. The long allocation supports investigations and an actual design performance. |
| 3. Weather, climate and water cycling | 38 | 4 | Particle and energy ideas support water paths before fronts and global circulation. The four-day climate close needs finding 1, but the overall allocation is defensible. |
| 4. Rock cycling and plate tectonics | 24 | 4 | Plate and rock-process models develop together before historical reconstruction and the final cycle. The late scale and timeline work is concentrated but supported by earlier evidence. |
| 5. Natural hazards | 20 | 2 | Plate and weather mechanisms precede forecasting and mitigation; information integration precedes the reliability argument. |
| 6. Cells and systems | 23 | 1 | Structural observations create the need for microscopy. The allocation also carries three later-owned starts and the three-day accessibility close. |

No whole unit is demonstrably far over or under its load. Unit 6’s single owned expectation does not make its 23 days excessive: comparative investigation, supported later-owned mechanisms and the accessibility close account for the additional work.

Assessment reservations are generally substantive:

- Day 17 names all four ray components.
- Days 44 and 51 reserve mass, kind, temperature relationships and an energy argument.
- Days 48 and 49 provide identifiable construction and testing evidence.
- Days 76 and 89 reserve particle-state and water-cycle performances; day 89 also uses the weather collection portfolio.
- Day 115 reserves rock cycling, all named plate-evidence classes, spatial and temporal scales, and strata-based historical organization.
- Day 135 includes both digital storage and transmission.
- Day 155 uses the carried-out investigation portfolio, unfamiliar samples and only the named parts of later-owned expectations.
- Day 159 identifies the earlier investigation portfolio supporting its cell station.

The practical evidence reservations are consistent with treating investigation and construction as performances. [MS-LS1-1 evidence statements](https://www.nextgenscience.org/sites/default/files/MS%20LS%20Evidence%20Statements%20June%202015.pdf), [MS-PS3-4 evidence statements](https://www.nextgenscience.org/evidence-statement/ms-ps3-4-evidence-statements)

Both units exceeding 25 days have mid-unit assessments. Response time is counted once. Actual item coverage, scoring and completion time remain unverified.

## Readiness and retrieval

| Assumed row or model | Last relevant use | Current sequence treatment |
|---|---|---|
| `s4-light-eye` | Grade 5, `s5-star-brightness` | Retrieval on day 2. Correct. |
| `s4-energy-transfer` | Grade 5, `s5-food-energy-sun` | Retrieval on day 18. Correct under the recorded row-use rule. |
| Grade 5 particles and design testing | Grade 5 | Retrieval on day 18. Correct. |
| Grade 5 conservation, sphere interactions and water distribution | Grade 5 | Retrieval in unit 3. Correct. |
| `s3-weather-data` | Maintained through Grade 5, explicitly recorded in the handoff | Retrieval in unit 3. Correct. |
| `s3-climates` | Grade 5, `s5-sphere-interactions` | Retrieval on day 85. Correct. |
| `s5-shadows-sky` | Grade 5 | Retrieval on day 85. Correct. |
| `s4-rock-layers`, stability-change | Grade 4 | Readiness on day 91; response on day 93. Correct. |
| `s4-weathering-erosion`, `s4-earth-feature-maps` | Grade 5 sphere interactions and water distribution | Retrieval on day 94. Correct. |
| `s4-wave-model` | Grade 4 | Readiness on day 115; response on day 117. Correct. |
| `s4-hazard-solutions`, `s4-information-codes` | Grade 5, `s5-design-test` | Retrieval on days 116 and 128. Correct. |
| `s4-structures-function` | Grade 5, `s5-plant-matter` | Retrieval in unit 6. Correct. |
| Sensory signaling | Taught with support on day 13 this year | Retrieval in unit 6. Correct. |

I found no receiving unit that incorrectly checks a preceding-year row or retrieves an unmaintained older row. The actual readiness checks immediately precede their units and do not occupy first-day hooks. Finding 4 concerns the conflicting underlying instructions.

## Calendar, cumulative checks, candidates and shorter path

**Calendar:** Days 90 and 159 fall in target weeks 18 and 32. Day 91’s response falls in week 19, correctly distinguished from the assessment week. The mid-year check does not collide with another subject’s course-level check.

**Same-year leans:** The calendar supports ratios, rates, timeline work and informative writing before their dependent science tasks. Statistics, histograms, media integration and overlapping argument writing receive named local bridges. Below-zero temperatures are read without assuming signed arithmetic. The two design windows avoid social studies’ days 100 to 113 research allocation.

**Checks that do not repeat:** The sequence explicitly draws unit 3 state-change sampling from earlier cup and cold-surface content. The year-end cell station uses earlier rock-grain evidence and an unfamiliar living sample, rather than repeating the healing assessment. Preserve these directions when applying finding 2.

**Candidates:** All six cells are settled with zero added days and explicit exclusions. The accessibility close is retained as part of the frame.

**Shorter path:** Both required forms exist. The ten named folds are:

`4 into 3; 7 into 6; 31 into 32; 39 into 38; 54 into 53; 62 into 61; 71 into 70; 100 into 99; 122 into 121; 145 into 144.`

All ten folded days have blank assessment cells. No assessment, response allocation, readiness check or owned part is explicitly cut. The warning against combining both shortened options without a separate time check is appropriate.

**Source map:** All 86 base lessons are placed consecutively: 8, 18, 22, 14, 10 and 14 lessons across the six units. Every referenced source file exists; no lesson is marked cut. Condensations, substitutions and additions have reasons.

The published base descriptions support the broad order, including coupled plate and rock-process development and the cells unit’s investigation-to-transfer arc. [Plate tectonics and rock cycling](https://openscied.org/instructional-materials/6-4-rock-cycling-plate-tectonics/), [Cells and systems](https://openscied.org/instructional-materials/6-6-cells-systems/)

## Science lens checklist: scope and sequence

| Lens line | Result |
|---|---|
| A unit’s anchor is a phenomenon rather than a topic | **Met.** Each unit opens with an observable puzzle. |
| Models are built before dependent use | **Missed locally.** Teaching arcs are coherent, but day 90’s tree comparison requires finding 2. |
| Engineering expectations appear in units | **Met.** Unit 2 carries design, construction, testing and improvement; unit 5 carries the declared engineering starts. |
| Equipment has substitutes or a no-kit path | **Met at plan level for alternatives.** Shared equipment, supplied evidence and paper paths are named. S6’s separate cost requirement is missed, finding 3. |

For the rubric’s sequence-layer responsibilities, phenomenon-driven planning and base order are supported. Full element coverage needs finding 1. This is a planning judgment, not a score for unwritten lessons or assessments. [Science 6 to 8 evidence guide, indicators 1e, 1k and 2a to 2c](https://cdn.edreports.org/media/2025/07/Science-6-8-Evidence-Guide_2.0.pdf), [EQuIP Science version 3.0](https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf)

## Settled by the expert

These are item-level choices for the caller to apply.

| Choice | Reason | File touched |
|---|---|---|
| Add ice-cover and plant-moisture relationships to existing unit 3 evidence and model tasks | Completes the claimed climate element without adding an expectation | Sequence; days 64, 85, 88 and 89 |
| Replace the grass/tree cumulative case with the four-panel cold-container display case | Uses taught mechanisms and explicitly reserves the listed performances | Sequence; day 90; frame check description |
| Retain readiness on days 91 and 115, with response on days 93 and 117 | Placements satisfy this run’s last-use and timing rules | Align frame and progression notes |
| Add provisional costs with sharing and reuse assumptions | Cost belongs at this layer | Sequence |
| Retain unit order, allocations, practical portfolios and ten folds | No established defect requires changing them | No allocation change |

## What is right and should remain

Preserve the evidence-driven model revisions, particle reasoning before design, water-cycle work before frontal-weather explanation, and coupled plate and rock-process development. Preserve actual prototype evidence, comparative microscopy, digital storage as well as transmission, the explicit limits on later-owned expectations, and the disability-led accessibility close.

The earlier frame concerns about membrane versus wall function, microscopic-to-landform scale, storm mechanisms and the no-microscope comparison have substantive homes in this sequence. They should not be reopened as missing.

## What I could not judge

- Actual assessment duration, scoring quality and whether the shorter-period tasks fit.
- Final investigation procedures, equipment suitability and safety implementation.
- Purchase costs and existing school inventory.
- Every source lesson’s detailed retained evidence: the large storyline PDFs exceeded the web tool’s size limit, and the available command environment lacked a PDF text extractor. Source-map completeness and order were checked, with published unit descriptions used for substantive comparisons.
- The unwritten science approach page. Shared guidance, the lens and the rubric were used instead.

## For the source list

The [Science 6 to 8 evidence guide, version 2.0](https://cdn.edreports.org/media/2025/07/Science-6-8-Evidence-Guide_2.0.pdf) was accessible. Relevant passages on phenomena, assessment, dimension coverage and safety were read; the entire 91-page guide was not read.

## For Cory

- **Money:** Equipment inventory and the Grade 6 materials allowance remain unknown. Any spending decision should follow the concrete six-unit cost table.
- No new scope, audience or outside-person decision is needed for these fixes.

**Verdict:** Revise before unit planning. **Findings:** 4. **Intended report path:** `docs/reviews/sequence-science-grade-6-2026-11-14.md`, supplied above, not written.


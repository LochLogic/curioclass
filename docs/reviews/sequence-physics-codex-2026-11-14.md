# Independent cold read: Physics scope and sequence

**Date:** 2026-11-14  
**Intended report:** `docs/reviews/sequence-physics-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files were created, edited or deleted.

## Verdict

Revise before unit planning, while retaining the broad scientific sequence and its substantive coverage. The largest risk is inconsistent prerequisite treatment: some older work receives retrieval, while light interactions are checked after their first use. Correct those placements, complete unit 6’s assessment reservation, and supply provisional materials costs.

**Finding count: 4.**

## What I read

- `docs/agents/EXPERT.md`, the science lens and `docs/RUBRIC-SCIENCE.md`.
- The complete Physics scope and sequence, all 160 `days.csv` rows, and the Physics frame.
- All 20 Physics progression rows, the preceding Chemistry rows, and relevant earlier prerequisites and intervening uses.
- `docs/courses/CALENDAR.md` and every grade 11 calendar row.
- Relevant mathematics progression rows for graph interpretation, equations, rearranging formulas, roots and periodic modelling.
- FOUNDATION, GLOSSARY, the shared APPROACH, relevant APPROACH-SOURCES entries, the required ROADMAP sections, BASELINE rules 20 to 24, and the base-text policy.
- The local science dimension records for all 20 owned expectations.
- Permitted earlier Physics frame reviews, science progression reports, relevant science sequence reviews, readiness-timing documentation and science data-gap documentation.
- Outside primary sources linked below.

The blind-file boundary was preserved. Prior-run memory informed review method and report structure only. No scientific finding rests on unverified memory.

`docs/APPROACH-SCIENCE.md` is not present. The shared approach, science lens and science rubric supplied the available instructional guidance.

## Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Did not complete: `ModuleNotFoundError: No module named 'markdown'`. |
| `python -X utf8 scripts/frame.py calendar` | Completed; no stagger-rule break reported. |
| `python -X utf8 scripts/frame.py check physics` | Passed: zero failures; 10 units, 160 days, including 149 unit days and 11 course-level days. |
| `python -X utf8 scripts/plan.py check physics` | Passed: zero failures. |
| `python -X utf8 scripts/stale.py check` | Passed: 56 files, zero failures. |

The interrupted global gate does not withhold this verdict.

## Findings, most serious first

### 1. Readiness treatment does not consistently follow this run’s last-use and timing rules

**Severity:** Major  
**LAYER:** sequence, frame, progression  
**REPEAT:** yes, the same rule conflict appears in the Grade 8 science sequence review, finding 3  
**Confidence:** firm on the recorded last uses and placements

**Locations:** Scope and sequence lines 7, 17, 55, 63, 69 and 85; `days.csv` days 1, 76, 86, 92, 94, 127 and 129; corresponding frame and progression handoffs.

**What is wrong:**

| Receiving unit | Evidence | Current treatment | Required correction |
|---|---|---|---|
| 1 | Force and collision rows and force-diagram were last used in grade 8. | Readiness follows the hook on day 1. | Give readiness in the start-of-year check before the unit opens, as this run explicitly requires. Resolve its delivery slot rather than adding an uncounted meeting. |
| 7 | `bio-sources-of-variation` was last used in grade 9. | Retrieval on day 94. | Add a brief ultraviolet-and-DNA readiness task to day 92’s final ten minutes; use its result on day 94. |
| 9 | The progression explicitly records `s6-plate-evidence` as last used in grade 9. Chemistry maintains the plate model for melting, rather than the full past-motion evidence row. | Retrieval on day 129. | Include past-motion evidence in day 127’s existing readiness allocation; use the result on day 129. |
| 6, then 7 | Unit 6 uses absorption and detection on day 86 and guided-light transmission on day 89. | The light-paths readiness check waits until day 92, before unit 7. | Put the necessary earlier light-path components in day 76 readiness and day 78 support. Explicitly carry reflection, absorption and transmission into day 86’s model. Unit 7 then retrieves that work. |

The final case checks old light knowledge after the course has already needed it. Moving its first readiness reservation also prevents unit 7 from checking components taught earlier that same year.

The current repository writing brief, glossary and gate permit the unit 1 exception. **The supplied instructions for this run explicitly require a start-of-year check and a clean first-day hook, so they control this review.** The passing gate therefore does not settle this discrepancy.

**Why it matters:** A prerequisite gap can be discovered after dependent instruction has begun. The older “intervening idle grade” convention also classifies grade 9 to grade 11 returns differently from the rule supplied for this run.

**Exact fix:** Apply the placements above and align the affected Physics frame and progression notes. Retain preceding-year Chemistry retrieval, unit 2’s return to unit 1, unit 5’s return to unit 3, and the other correctly placed readiness checks. The unit 1 allocation issue belongs to Cory because the frame reserves no separate start-of-year day; a concrete option appears below.

### 2. Unit 6’s explicit assessment reservation omits mathematical technical communication

**Severity:** Moderate  
**LAYER:** sequence, standard  
**REPEAT:** yes, incomplete performance reservations recur in the earlier Physics frame read, finding 2  
**Confidence:** firm

**Locations:** Scope and sequence lines 63 and 125; `days.csv` days 89 to 91.

**What is wrong:** The plan explicitly requires visual, spoken and written technical communication for HS-PS4-5, but omits mathematical communication. The official practice element includes that fourth form. Mathematics assessed separately under HS-PS4-1 does not automatically demonstrate mathematical communication about a device. [Official HS-PS4-5 foundation elements](https://www.nextgenscience.org/pe/hs-ps4-5-waves-and-their-applications-technologies-information-transfer)

The generic requirement to assess “all parts” is weaker than the specific three-format list a writer will follow. The local dimension file also includes mathematical communication.

**Why it matters:** A student could complete the stated technical explanation in every named format while leaving one claimed practice component unrepresented.

**Exact fix:**

- On days 89 and 90, require a numerical pixel or sampled-signal representation connected to its pulse representation and explained as part of the device’s operation.
- On day 91, reserve mathematical communication within the unfamiliar technical system, alongside visual, spoken and written evidence.
- Explicitly reserve the remaining HS-PS4-5 evidence: solar electrical capture, digitization with storage and transmission, photoelectric response, and the intended signal or energy pathway.
- An unfamiliar solar-powered imaging and communication system can join these components in one annotated product. Keep the information qualitative and exclude band theory.

Carry this reservation into the shorter-year combination of days 90 and 89. No additional day or ownership change is required.

This extends the earlier repair rather than reopening it: absorption, detection and device mechanisms now precede the explanation, which is correct.

### 3. All ten unit costs are deferred beyond the layer that requires them

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, Grade 6 science sequence review, finding 3, and Grade 8 review, finding 5  
**Confidence:** firm

**Location:** Scope and sequence lines 144 to 148 and 171; all unit materials provisions.

**What is wrong:** The sequence names equipment, substitutes and no-kit routes, but supplies no provisional unit costs. It expressly leaves school cost to unit planning. The science rubric assigns **S6, costs**, to the scope-and-sequence layer.

**Why it matters:** Feasibility depends on classroom quantities, existing stock and reuse. A sensitive induction meter, current limiting, collision-force measurement and eye protection have different implications from printed data sheets. These choices also affect whether students can complete the physical investigation performance.

**Exact fix:** Add a ten-row provisional materials-cost table for the shared approach’s class of thirty, stating:

- Quantities and equipment assumed already available.
- New reusable equipment, consumables and printing.
- Reuse across units, with shared purchases counted once.
- Dated price sources and estimated additional cost.
- Minimum physical equipment and the remaining performance limitation on the reduced-materials route.
- A one-child equivalent where materially different.

An estimate does not authorize purchasing or establish a spending ceiling.

### 4. The science rubric retains obsolete data and safety-review instructions

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, Grade 6 science sequence review, finding 4  
**Confidence:** firm

**Locations:** `docs/RUBRIC-SCIENCE.md`, line 66, S5 at line 104, and Questions for Cory at lines 184 onward.

**What is wrong:**

| Current statement | Contrary current evidence | Exact fix |
|---|---|---|
| Practice, core idea and crosscutting statements exist in no data file. | `data/standards/ngss-pe-dimensions.csv` now contains those records, and Physics uses them. | Acknowledge the file. Describe the remaining task as tracing elements into teaching and assessment evidence. |
| A science teacher must read safety and materials, and completion waits until that person is found. | Current FOUNDATION 7.3 assigns this content review to a fresh safety agent. The Physics frame follows that decision. | Update S5 and Questions for Cory to match FOUNDATION, retaining the safety review and the separate human pilot requirements. |

**Why it matters:** A later writer or reviewer receives incompatible requirements from active governing files. The passing stale-note gate does not detect these unmarked contradictions.

These are consistency repairs to existing decisions, not new staffing decisions.

## Order, standards, assessments and load

All 20 owned expectations have teaching and end-of-unit assessment locations. They have no lettered subcodes; completeness depends on their substantive components and dimension elements.

| Unit | Days | Owned expectations | Order and load judgment |
|---|---:|---:|---|
| 1. Push, pull, bounce | 18 | 2 | Motion records precede the force law; force comparisons precede momentum synthesis. Quantitative representations justify the longer allocation. Finding 1 affects readiness. |
| 2. Softer landings | 12 | 1 | Criteria and planning precede construction, testing, evaluation, refinement and retesting. Twelve days support an actual design cycle. |
| 3. Where will the spacecraft be? | 16 | 2 | Force laws precede orbital predictions. Ellipses and equal-area reasoning precede period calculations and supplied computation. |
| 4. The first hill | 16 | 2 | Track evidence, particle explanations and arrangement energy precede the joined field-energy account. |
| 5. Spin a wheel, light a lamp | 11 | 1 | Planning precedes both investigation directions, improvement and explanation. Four investigation days are justified. |
| 6. Messages made of waves | 16 | 3 | Wave relationships precede digital questions and device explanations. Findings 1 and 2 need correction. |
| 7. Light, two ways | 14 | 2 | Evidence for both models precedes their comparison; exposure mechanisms precede published-claim evaluation. |
| 8. Where your atoms came from | 18 | 3 | Spectral evidence precedes solar and stellar explanations, then convergent cosmic evidence. |
| 9. The restless Earth | 18 | 3 | Seismic and other interior evidence precede convection, feedback and crust-age synthesis. Waves and half-life are already available. |
| 10. Older than Earth | 10 | 1 | Preservation and dating precede body-composition and crater evidence, then the formation account. |

No whole unit is demonstrably far over or under its load. The allocations follow investigation, representation and evidence demands rather than equal days per code.

The assessment reservations retain several easily lost components:

- Momentum uses reference frames, boundaries and external exchange.
- Both force laws and all three orbit laws are placed.
- Energy models connect macroscopic changes to particles, arrangement, fields and radiation.
- Investigation records supplement the unit 5 transfer task.
- Digital work includes transmission and storage.
- Stellar work includes mass, stage, solar variability and nuclear accounting.
- Earth work includes feedback, multiple interior evidence types, continental and oceanic ages, and dating evidence.
- Formation work includes sample ages, body composition and crater histories.

Unit 6 needs finding 2. Actual prompts, scoring and timed completion cannot yet be judged.

No unit exceeds 25 days, so none requires a separate mid-unit assessment. Each unit names its response day once; the four course-level response days are separate.

## Readiness trace

The 25 distinct science prerequisites group as follows.

| Prerequisites | Last relevant earlier use | Judgment |
|---|---|---|
| Eight Chemistry rows: atomic structure, bulk forces, Earth energy, energy accounting, device design, nuclear processes, thermal equilibrium and water/Earth materials | Grade 10 | Retrieval is appropriate. |
| `bio-sources-of-variation` | Grade 9 | Unit 7 needs readiness under this run’s rule. |
| Force and collision rows | Grade 8 | Readiness is appropriate; unit 1 timing needs correction. |
| Fields, electromagnetic forces, gravity-mass and gravity-solar-system | Grade 8, then relevant earlier Physics units | Day 30 readiness and later retrieval are appropriate. |
| Kinetic and potential energy | Grade 8 | Day 46 readiness is appropriate. |
| Wave quantities and digital signals | Grades 8 and 6 respectively | Day 76 readiness is appropriate. |
| Light paths | Grade 8 in the recorded progression, then Physics unit 6 | First-use timing needs correction, finding 1. |
| Solar-system scale | Grade 8, then unit 8 | Day 109 readiness and unit 10 retrieval are appropriate. |
| Plate evidence | Grade 9 for the evidence row | Unit 9 needs readiness; distinguish this from the maintained plate model. |
| Rock cycle | Grade 10 | Retrieval is appropriate. |
| Surface-change scales | Grade 6 | Day 127 readiness is appropriate. |
| Geologic time | Grade 8 through fossil-record work | Day 145 readiness is appropriate. |

Apart from unit 1, the existing readiness slots sit immediately before their receiving units. I found no readiness check placed weeks ahead.

## Calendar, repetition, candidates and shorter path

**Calendar:** Physics checks occupy weeks **13, 22 and 32**, matching its calendar rows. The grade 11 rule permits the shared finals week.

**Same-year leans:** ELA informative writing ends on day 34 and argument on day 55, before the Physics uses. The model explainer and reasoning frame remain sensible supports. Physics avoids the later rational-exponent dependency, and its wave work precedes Algebra II’s periodic modelling.

**Checks that do not repeat:** Days 64, 108 and 158 explicitly draw the immediately preceding unit’s skills into earlier-unit contexts. Those reservations satisfy the non-repetition rule at sequence depth.

**Candidates:** All ten units settle their candidate cells with named existing days and no added days. Unit 1 gives a reason for dropping its additional designed-system candidate. Required elements remain required.

**Shorter year:** The ten fold-ins are explicitly paired with receiving days:

`15→14`, `28→27`, `44→43`, `60→59`, `74→73`, `90→89`, `104→103`, `125→124`, `143→142`, `153→152`.

None carries an assessment marker. The receiving descriptions retain the named work. The shorter-period route preserves reasoning and assessment commitments, but its actual timing remains to be demonstrated in unit plans.

**Source map:** Not applicable. Physics has no base text; the source policy identifies high school science as original work with reference-only curricula.

## Science lens checklist: scope and sequence

| Checklist line | Result |
|---|---|
| A unit anchor is a topic rather than a phenomenon | **Met:** all ten units name an observable phenomenon or design problem. |
| A model is used before the unit that builds it | **Missed in prerequisite handling:** light interactions need the correction in finding 1. The broad model order otherwise holds. |
| Engineering design expectations appear in no unit | **Not applicable to ownership:** Physics owns none; unit 2 applies the earlier-owned engineering practices through a complete cycle. |
| Equipment is assumed without a substitute or no-kit path | **Met for named alternatives; costs missed:** finding 3. Unit 5’s conduct limitation remains explicit. |

At planning depth, question boards, initial models, evidence-based revisions, argument and unfamiliar transfer are reserved. Safety hazards and controls accompany the listed physical investigations. These commitments do not certify unwritten lessons.

## What is right and should not be changed

- Preserve the motion-to-design, fields-to-energy and waves-to-Earth-evidence dependencies.
- Preserve calculator roots and central-body restrictions on orbital equations.
- Preserve particle explanations, field-system boundaries and both objects’ energy changes.
- Preserve radiation distinctions among photon energy, absorption and total exposure.
- Preserve the solid-mantle limitation on the water analogue.
- Preserve the selected age-table comparison rather than a universal claim about lunar or meteorite ages.
- Preserve the explicit distinction between recorded-run analysis and physical investigation conduct.

The earlier Physics mechanism and anchor repairs are present. This review does not reopen them.

## Settled by the expert

| Choice | Reason | File affected when applied |
|---|---|---|
| Put Biology ultraviolet/DNA readiness on day 92 and targeted support on day 94 | Grade 9 is two grades back under this run’s rule | Physics sequence and days; corresponding handoff notes |
| Add plate-evidence readiness to day 127 and support to day 129 | The evidence row’s recorded last use is grade 9 | Physics sequence and days; corresponding handoff notes |
| Move necessary light-path readiness to day 76 and support to day 78 | It must precede unit 6’s device work | Physics sequence and days |
| Use a numerical encoding and pulse representation within technical communication | Supplies the missing mathematical format without advanced mathematics | Days 89 to 91 and HS-PS4-5 coverage row |
| Retain the present broad order and other unit allocations | No demonstrated load defect warrants redistribution | Physics frame and sequence |
| Count shared equipment once in provisional estimates | Prevents misleading unit and course totals | Physics materials-cost table |

## For Cory

- **Allocation:** This run’s clean unit 1 hook requires a start-of-year slot absent from the frame. One concrete option keeps 160 days: make day 1 a course-level start check, use day 2 for the hook, day 3 for targeted reteaching, and combine the original day 3 motion-record introduction with day 4’s graph work. Unit 1 becomes 17 days, with 148 unit days and 12 course-level days overall. This changes the frame allocation, so it is not an expert-settled day swap.
- **Money and access:** Decide whether any shared physical-kit provision is possible for the current-and-field investigation. The recorded-run route can remain available, but its acknowledged conduct limitation must remain visible in completion claims.

## What I could not judge

- Actual assessment prompts, scoring guidance, accommodations and completion time.
- Exact data sets, source extracts and tool implementations, which remain unselected.
- Physical performance evidence on the no-kit unit 5 route. Its limitation is already acknowledged.
- Completed lesson safety, setup, cleanup and the required fresh safety and sensitivity reads.
- Whole-band element completion across finished Biology, Chemistry and Physics materials. Code ownership alone does not demonstrate that completion.

## Outside sources

- [Official DCI arrangements](https://www.nextgenscience.org/sites/default/files/AllDCI.pdf): checked alongside the local element inventory for scope and assessment boundaries.
- [HS-PS4-5 foundation elements](https://www.nextgenscience.org/pe/hs-ps4-5-waves-and-their-applications-technologies-information-transfer): mathematical communication and device components, finding 2.
- [HS-ESS1-3 foundation elements](https://www.nextgenscience.org/pe/hs-ess1-3-earths-place-universe): stellar evidence, communication and nuclear accounting.
- [HS-PS2-5 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/HS-PS2-5%20Evidence%20Statements%20June%202015%20asterisks.pdf): planning, measurement, conduct and investigation refinement.
- [Science high school evidence guide, version 2.0](https://cdn.edreports.org/media/2026/06/Science%20High%20School%20Evidence%20Guide_2.0.pdf): targeted reading of element-level coverage, assessment and safety indicators.
- [EQuIP science rubric, version 3.0](https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf): phenomena, coherence, prior learning and observable assessment evidence.
- [Federal instruction and study practice guide](https://ies.ed.gov/ncee/WWC/PracticeGuide/1/Published): retrieval and spaced return. It does not establish the repository’s particular readiness-placement rule.
- [Published high school scope and sequence](https://www.openscied.org/wp-content/uploads/2023/09/OpenSciEd-High-School-Scope-Sequence-September-2021.pdf) and [New Visions Physics overview](https://www.newvisions.org/curriculum/science/physics): reference comparisons for integrated Physics and Earth science. The latter adapts the former, so these are related comparisons, not independent evidence of effectiveness.

**For the source list:** The accessible high school evidence-guide address above can be added to APPROACH-SOURCES. The general high school materials landing page attempted during this read was inaccessible; the published sequence PDF was reachable.

**Verdict: revise before unit planning. Findings: 4. Report path: `docs/reviews/sequence-physics-2026-11-14.md`, supplied above and not written to disk.**


# Biology course frame: independent review, 2026-11-14

**Intended report path:** `docs/reviews/frame-biology-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files changed.

## Verdict

The biology frame has a coherent sequence, complete skill placement, and a workable provisional calendar, but it needs targeted corrections before the scope and sequence is built. The largest risk is inaccurate or insufficiently supported modeling of matter and energy, especially unit 4’s account of energy not transferred to the next trophic level. Correct that model, complete unit 1’s feedback coverage, and replace unit 3’s proposed revision evidence while preserving the current unit order and day total.

## What I read

- `docs/agents/EXPERT.md`, the science lens, `docs/RUBRIC-SCIENCE.md`, the foundation, glossary, shared approach, relevant roadmap sections, BASELINE rules 20 to 24, and the shared adoption-bar rows.
- The complete biology frame, its `frames.csv` row, all 24 grade 9 science progression rows, their earlier-grade prerequisites, and receiving Chemistry and Physics rows.
- The complete grade 8 science and Chemistry frames; relevant Algebra I and ELA 9 unit, calendar, and cross-subject sections.
- The source policy and science source register. Biology has no base text or source-map file, consistent with that policy.
- Earlier biology reports, the high school science fixes report, and relevant science progression reviews and reconciliation records.
- Live official standards and evidence statements, Appendix K, EQuIP, and two curriculum developers’ public course descriptions, linked below.

Earlier personal memory informed review technique only. No curricular finding rests on unverified personal memory.

## Checks

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Could not complete: `ModuleNotFoundError: No module named 'markdown'`. |
| `python -X utf8 scripts/frame.py check biology` | Passed: 0 failures; 10 units, 160 days. |
| `python -X utf8 scripts/stale.py check` | Passed: 56 files, 0 failures. |

The incomplete repository gate does not withhold this verdict. Its result establishes neither a biology defect nor a complete repository pass.

## Findings, most serious first

### 1. Unit 4 sends all remaining energy directly to respiration heat

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, scientific accuracy, as in the earlier biology report’s finding 5  
**Confidence:** firm

**Location:** `docs/courses/biology/frame.md:113`; `data/progressions/science.csv:145`, `bio-energy-pyramids`.

**What is wrong:** Both texts say roughly a tenth passes upward and “the rest” is released as heat through respiration. This omits energy remaining in uneaten material, dead organisms, and waste that enters detrital pathways. It turns an approximate transfer efficiency into an incorrect account of every remaining energy flow.

**Why it matters:** Students could build an energy budget that erases decomposers and organic material. The official HS-LS2-4 foundation and evidence statements distinguish material stored, respired, and discarded, and require accounting for energy not transferred upward. See [HS-LS2 evidence statements, PDF pages 7 to 8](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/HS%20LS2%20Evidence%20Statements%20June%202015%20asterisks.pdf).

**Exact fix:** Replace the account in both locations with:

> Use a proportional energy budget to distinguish energy incorporated into biomass at the next trophic level, energy transferred as respiration heat, and chemical energy remaining in uneaten material and waste that can enter detrital and decomposer pathways. Transfer efficiency varies; roughly ten percent is an illustrative approximation. Track conserved atoms separately from energy.

Keep the existing 11 days.

### 2. Unit 1 narrows feedback to restoring a set point

**Severity:** Moderate  
**LAYER:** standard  
**REPEAT:** yes, incomplete standard coverage, as in the earlier biology report’s finding 2  
**Confidence:** firm

**Location:** `docs/courses/biology/frame.md:110`; `bio-homeostasis-feedback`.

**What is wrong:** The unit specifies feedback toward a set point, and the progression likewise requires return toward a set point. Neither secures the positive-feedback part of the claimed core idea. The unit’s candidate crosscutting statement mentions destabilization, but candidates may subsequently be dropped.

**Why it matters:** HS-LS1-3’s foundation includes both amplifying and counteracting feedback. Students need to distinguish feedback direction from whether an outcome is desirable. The [official HS-LS1 foundation](https://www.nextgenscience.org/dci-arrangement/hs-ls1-molecules-organisms-structures-and-processes) explicitly includes both types.

**Exact fix:** Retain the homeostasis investigation. Add a required comparison with a provided organism-level positive-feedback case, such as a simplified blood-clotting sequence, without molecular mechanisms. Students identify what response counteracts a disturbance, what response amplifies change, and what limits or stops amplification. Put this requirement in “What students learn” and the progression notes, rather than leaving it solely among candidates.

This revises the earlier report’s blanket conclusion that the remaining expectations were fully represented.

### 3. Unit 3’s new revision evidence does not establish its intended explanation

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, evidence must support the claimed performance, as in the science progression review’s finding F4  
**Confidence:** likely

**Location:** `docs/courses/biology/frame.md:112`, HS-LS1-6 sentence.

**What is wrong:** The proposed new evidence is that seedlings’ dry mass exceeds the sugar they “could store.” The frame gives no basis for that storage limit. Dry mass alone cannot distinguish stored sugars from other compounds or establish that sugar atoms entered newly formed amino acids.

**Why it matters:** A writer could manufacture a storage ceiling or present a conclusion as evidence. HS-LS1-6 requires a justified explanation and revision concerning the relationships between atoms in sugars and other molecules. See [HS-LS1 evidence statements, PDF pages 8 to 9](https://www.nextgenscience.org/sites/ngss/files/HSLS1EvidenceStatements060215.pdf).

**Exact fix:** Keep the seedling mass investigation for photosynthesis and respiration. Replace the HS-LS1-6 revision trigger with:

> Students use atom-tracking models and a supplied simulation to explain biosynthesis, then revise their explanation when supplied evidence traces carbon from sugar into newly formed amino acids. They account for other required elements entering the organism from its surroundings.

Provide a printed atom-tracking path. No reaction pathways or macromolecule-identification exercise is required.

The earlier biology finding correctly restored explanation revision. Its prescribed dry-mass trigger, now applied, needs this further correction.

### 4. The one-lesson investigation promise contradicts the planned observations

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, timing and feasibility, as in the earlier biology report’s finding 1  
**Confidence:** firm

**Location:** `docs/courses/biology/frame.md:8`, compared with units 1 and 3.

**What is wrong:** “Every investigation fits one lesson” conflicts with seedling changes observed over a week and root-growth observations. A measurement session can fit one period; the complete investigation cannot.

**Why it matters:** A teacher or writer could omit advance preparation, repeated observations, or drying time when converting this frame into lessons.

**Exact fix:** Replace the sentence with:

> Each investigation’s active classroom sessions fit 50-minute lessons. Longitudinal investigations name advance preparation, elapsed observation time, repeated measurements, and any teacher processing between sessions. Units 1 and 3 reserve these sessions within their existing day allocations.

No increase to the course total is justified by this finding.

### 5. The progression’s load explanation counts four engineering expectations

**Severity:** Minor  
**LAYER:** progression  
**REPEAT:** yes, incorrect explanatory counts, as in the earlier biology report’s finding 9  
**Confidence:** firm

**Location:** `data/progressions/science.csv:136`, `bio-population-carrying-capacity`.

**What is wrong:** The note describes Biology’s 30 expectations as all life science, **four** engineering, and three Earth and space expectations. The actual allocation is 24 life science, **three** engineering, and three Earth and space expectations. HS-ETS1-2 belongs to Chemistry.

**Why it matters:** The explanatory note contradicts the ownership data used to justify Biology’s load.

**Exact fix:** Replace that parenthesis with:

> 24 life science expectations, three engineering expectations (HS-ETS1-1, HS-ETS1-3 and HS-ETS1-4), and three Earth and space expectations

Keep the total of 30 and all existing ownership.

### 6. ELA 9 still says the Biology and Algebra I frames will be written later

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, explicitly identified in the high school science fixes report  
**Confidence:** firm

**Location:** `docs/courses/english-language-arts-grade-9/frame.md:156`.

**What is wrong:** The cross-subject introduction says both frames are written later. Both exist, and Biology already gives its availability calendar. The marked stale-note check does not catch this sentence.

**Why it matters:** It discourages reconciliation with available evidence and leaves the reciprocal handoff described as unknown.

**Exact fix:** Replace the sentence’s second half with:

> The world history, Biology and Algebra I frames are on file. Biology unit 7 runs in weeks 19 to 23, before this course’s unit 7 in weeks 24 to 26; Biology unit 9 runs in weeks 25 to 28, so this course retains its supplied-source bridge for human impacts.

Retain the existing independent ELA source path.

### 7. The science rubric’s material inventory is stale

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale planning status, as in the earlier biology report’s finding 3  
**Confidence:** firm

**Location:** `docs/RUBRIC-SCIENCE.md:54`.

**What is wrong:** The paragraph identifies the grade 4 draft and middle school base text as the only material. Multiple science course frames and a science progression now exist.

**Why it matters:** The rubric is an entry point for reviewers. Its inventory sends them past available planning evidence.

**Exact fix:** Replace the paragraph with:

> Science course frames and the science progression are now on file, alongside the grade 4 scope and sequence draft and the middle school base text. These are planning evidence, not completed courses; claims about lessons, assessments and classroom use require the corresponding materials.

Do not infer that a finished course exists.

### 8. The science rubric says no plan places the nature of science

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale planning status, as in the earlier biology report’s finding 3  
**Confidence:** firm

**Location:** `docs/RUBRIC-SCIENCE.md:64`, Gateway 2 connections row.

**What is wrong:** “No plan names where the nature of science is taught” is contradicted by Biology’s explicit placements in units 5, 7 and 8, and by the neighboring frames.

**Why it matters:** It reports a completed planning step as absent and obscures the actual remaining task: tracing those placements into instruction and assessment.

**Exact fix:** Replace the gap statement with:

> Course frames now name nature-of-science placements, including Biology units 5, 7 and 8. The scope and sequence and unit plans must turn these placements into explicit student work and assessment evidence.

## Coverage, order and days

All **24 owned skills appear exactly once**, with no foreign-grade skill presented as newly owned. The core high school allocation contains **71 distinct expectations**, each owned once: Biology 30, Chemistry 21, Physics 20.

| Unit | Days | Owned expectations | Frame judgment |
|---|---:|---:|---|
| 1. Steady inside | 13 | 2 | Purpose and opening position hold; complete feedback coverage |
| 2. One cell, many kinds | 12 | 2 | Appropriate pickup from systems to specialized cells |
| 3. Where the mass goes | 18 | 4 | Appropriate load; replace revision evidence and clarify elapsed time |
| 4. Energy and carbon | 11 | 2 | Correct prerequisite position; correct energy accounting |
| 5. Populations | 18 | 4 | Quantitative work, multiple scales and revision are placed |
| 6. Inheritance | 16 | 3 | DNA prerequisite precedes inheritance; anchor mechanism is named |
| 7. Evolution | 18 | 4 | Variation and population prerequisites precede selection |
| 8. Life and Earth | 11 | 2 | Appropriate synthesis before human-impact design |
| 9. River design | 17 | 4 | Revised allocation supports the design and refinement cycle |
| 10. Simulations | 15 | 3 | Appropriate capstone after computational and design models |
| Course checks and response | 11 | Cumulative | Six assessment days and five respond days |
| **Total** | **160** | **30** | **149 unit days plus 11 course-level days** |

No further day redistribution is supported by this read. The earlier four-day redistribution is present and should remain.

All 30 expectations have a unit. Beyond findings 1 to 3, I found no additional frame-level omission of a whole required performance. That is a planning judgment, not verification of unwritten lessons or assessment items. Published clarification examples were used to interpret depth, rather than treated as a requirement to teach every possible example.

## Seams and cross-subject readiness

The grade 8 handoffs into genetics, selection, senses and design are picked up. Grade 7 ecosystem and cellular-energy work has explicit retrieval after the intervening year. Chemistry receives the promised qualitative bond model, carbon cycle, computational practice, Earth-life feedback and engineering work; the radiation-DNA handoff to Physics is consistent.

Algebra I teaches the required statistics and linear-model work before Biology’s later uses. Unit 1’s concurrent graphing demand has a worked-example bridge. Biology unit 5 explicitly teaches its update rule before Algebra I’s exponential unit.

ELA 9 teaches argument and explanatory writing after several Biology demands. Biology supplies its own disciplinary writing supports. Those bridges are appropriate; ELA 9’s stale introduction is finding 6.

**Source map:** Not applicable. Biology is original work, and the absence of `source-map.csv` is consistent with the source policy. No reference-only or non-commercial source is mapped as a Biology base text.

## Science lens checklist: course frame layer

| Lens line | Result |
|---|---|
| Every owned performance expectation has a unit and sufficient intended coverage | **Missed in part:** placement complete; findings 1 to 3 concern accuracy, elements and evidence |
| Grades 6 to 8 retain base order or record departures and losses | **Not applicable** |
| High school band expectations have explicit course ownership | **Met:** all 71 owned once across the three core courses |
| Every unit names an anchor phenomenon or design problem | **Met:** all ten do |

The frame also explicitly places engineering, nature of science, retrieval, transfer assessment, material alternatives and sensitivity reads. Actual storyline continuity, model revisions, safety sheets and assessment quality remain later-layer checks.

## What is right and should remain

- The body-to-cell, matter-and-energy, ecosystem, inheritance, evolution and design sequence.
- Separate tracking of matter and energy in unit 3.
- Revision on contrasting evidence in units 3 and 5.
- The explicit explanation of the Labrador anchor.
- The strengthened design allocation and three-day group-behavior section.
- Privacy protections, accessible participation choices, food-grade beans, and reference-only source boundaries.

The different orders in the public [OpenSciEd Biology description](https://openscied.org/on-demand-hub/how-are-traditional-biology-topics-organized-in-openscied-high-school-biology/) and [BSCS course description](https://bscs.org/educator_resource/bscs-biology-understanding-for-life/) do not establish a reason to reorder this frame. They provide useful comparisons for coherent phenomenon-based organization, not a compulsory sequence.

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Keep all ten units and 160 days | No demonstrated need for further redistribution | Biology frame; `frames.csv` |
| Separate respiration heat from detrital energy pathways | Correct proportional accounting within HS-LS2-4 | Biology frame; `bio-energy-pyramids` |
| Require a positive-feedback comparison within unit 1 | Completes the claimed feedback elements | Biology frame; `bio-homeostasis-feedback` |
| Replace the dry-mass storage ceiling with atom-tracking evidence | Revision must address biosynthesis | Biology frame, unit 3 |
| Distinguish elapsed investigation time from lesson time | Makes the existing calendar implementable | Biology frame, Days bullet |
| Correct three engineering expectations and the stale status sentences | Repository evidence settles these item-level corrections | Files named in findings 5 to 8 |

These are recommendations for the caller to apply. No standard moves between units or courses.

## For Cory

- **People and any pay:** The existing requirement remains for a qualified science teacher’s safety and materials read, the sensitive-content readers for units 6 and 7, and the community-informed review of unit 9. This review does not arrange those readers.

No new scope, audience or spending decision is needed.

## Limits and sources

This is a frame review. It does not certify classroom timing, completed investigations, item-level assessment coverage, finished simulations, or source permissions for assets not yet selected. The science approach page remains absent. The high school criteria PDF linked by the repository was inaccessible through the web tool; I consulted the current [official review-tools page](https://edreports.org/process/review-tools/science) and used the repository rubric without assigning finished-course scores.

Sources opened live:

- [Official high school standards](https://www.nextgenscience.org/sites/default/files/HSDCI.pdf): performance wording, foundation elements, clarifications and boundaries.
- [HS-LS1 evidence statements](https://www.nextgenscience.org/sites/ngss/files/HSLS1EvidenceStatements060215.pdf): investigation, molecular explanation and revision requirements.
- [HS-LS2 evidence statements](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/HS%20LS2%20Evidence%20Statements%20June%202015%20asterisks.pdf): ecosystem accounting and student performances.
- [HS-ESS2-7](https://www.nextgenscience.org/pe/hs-ess2-7-earths-systems): Earth-life feedback.
- [Appendix K](https://www.nextgenscience.org/sites/default/files/Appendix%20K_Revised%208.30.13.pdf): course allocation as a model for local development.
- [EQuIP version 3](https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf): coherence, evidence and three-dimensional design.

**For the source list:** Add the direct HS-LS1 and HS-LS2 evidence-statement links above and the two developer course-description links. Record the failed criteria-PDF address and the accessible review-tools entry page.

**Verdict:** Targeted corrections needed before building the scope and sequence. **Finding count:** 8. **Report path:** `docs/reviews/frame-biology-2026-11-14.md`, supplied here, not written.


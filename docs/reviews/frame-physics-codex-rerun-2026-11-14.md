# Physics course frame: independent review

**Date:** 2026-11-14  
**Requested report path:** `docs/reviews/frame-physics-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files were changed.

## Verdict

Revise the frame before using it as the basis for the scope and sequence. Its ownership, broad sequence, prerequisites and year length are sound, but several commitments are too narrow to secure full standards coverage, and three anchors make claims that need qualification. The most important change is to specify the missing scientific mechanisms and student performances within the existing units.

**Finding count: 8.**

## What I read and checked

- `docs/agents/EXPERT.md`, the science lens, `docs/RUBRIC-SCIENCE.md`, `docs/FOUNDATION.md`, the relevant roadmap sections, BASELINE rules 20 to 24, the glossary, approach, science source-list entries and base-text rules.
- The complete Physics frame, its `frames.csv` row and all 20 grade 11 science progression rows.
- The Chemistry frame, relevant Biology handoffs, and the earlier progression rows Physics retrieves.
- Relevant portions of the Algebra I, Algebra II, grade 8 mathematics, ELA 11 and World History I frames.
- The earlier Physics reviews, high school science fixes, and relevant earlier science findings.
- Outside primary sources linked below, including full standards statements and foundation elements, rather than relying on the local code-only standards inventory.

Physics is the last core science course. There is no succeeding core frame; the two science electives have no frames on disk. Physics has no base text and no source map, consistent with `BASE-TEXTS.md`.

| Required check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Could not complete: `ModuleNotFoundError: No module named 'markdown'`. |
| `python -X utf8 scripts/frame.py check physics` | Passed: 0 failures; 10 units, 149 unit days, 11 course check and respond days. |
| `python -X utf8 scripts/stale.py check` | One failure in the unrelated ELA 7 frame, line 32. |

The unavailable full gate and unrelated stale-note failure do not prevent this curricular verdict, as the current brief explicitly directs.

## Findings, most serious first

### 1. Three anchors make scientific claims too absolute to teach safely

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, inaccurate or overgeneralized anchors also occur in the earlier Biology and grade 3 science reads  
**Confidence:** firm

**Location:** `docs/courses/physics/frame.md`, units 4, 7 and 10, lines 121, 124 and 127.

**What is wrong:**

- Unit 4 says a roller coaster’s first hill is “always” tallest. Conservation constrains the height reachable from a specified initial energy without additional energy input. It does not establish that rule for every ride.
- Unit 7 says radio waves do nothing measurable and pass through harmlessly. Absorbed radiofrequency energy can heat matter; sufficiently intense exposure can damage tissue. Frequency matters, but intensity, duration and absorption also matter. [ARPANSA’s radiofrequency explanation](https://www.arpansa.gov.au/understanding-radiation/what-is-radiation/non-ionising-radiation/radiofrequency-radiation)
- Unit 10 treats meteorites and lunar rocks as uniformly older than terrestrial rocks. Lunar samples include rocks about two billion years old. The useful comparison concerns selected ancient samples and the preservation or resetting of their records. [Brown University’s account by a participating researcher](https://www.brown.edu/news/2021-10-07/moon)

**Why it matters:** These sentences become the premises students are asked to explain. A writer following them literally could teach false rules about conservation, radiation or radiometric ages.

**Exact fix:**

- Unit 4: use a specified cart or gravity-driven ride with no added power after release. Ask why it cannot regain its release height when energy transfers to the surroundings.
- Unit 7: replace the harmlessness contrast with: “Sunlight can damage skin, while a radio receiver detects broadcasts inside a room. How do different frequencies interact with matter, and what controls their effects?” Explicitly include thermal absorption and distinguish photon energy from total exposure.
- Unit 10: use a selected, sourced age table containing ancient meteorites, ancient lunar samples, terrestrial rocks and younger lunar rocks. Ask why their ages differ and how the oldest records constrain Earth’s early history.

These are wording and example choices within existing ownership.

### 2. Three claimed standards need explicit mechanisms beyond their current headlines

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, the earlier Physics review’s finding 1 concerns narrowed standards  
**Confidence:** firm on the omissions; likely on the proposed teaching examples

**Location:** Physics units 4, 6 and 9; corresponding progression notes.

**What is wrong and the exact fix:**

| Standard | Gap | Required addition |
|---|---|---|
| **HS-PS3-2**, unit 4 | The frame names macroscopic motion, height, springs, charged plates and thermal energy, but never requires the model to explain these through particle motion and configuration. Listing `particle-model` does not secure that performance. | Require students to connect a macroscopic energy change to particle motion and relative positions, including what changes microscopically when motion becomes thermal energy. Retain the charged-plate case. [Official evidence statement](https://www.nextgenscience.org/sites/ngss/files/HS-PS3-2_Evidence%20Statements%20Jan%202015.pdf) |
| **HS-PS4-5**, unit 6 | The frame says devices use wave behaviour, but omits the progression row’s explicit interaction with matter. Photoelectric behaviour appears only in unit 7, after unit 6’s technical explanation. | Before the explainer, teach the necessary absorption, detection and light-to-electric response qualitatively, including provided evidence about photoelectric materials. Require a device explanation tracing the signal or energy through matter. Unit 7 can then evaluate the competing light models. No band theory is needed. [Official foundation elements](https://www.nextgenscience.org/pe/hs-ps4-5-waves-and-their-applications-technologies-information-transfer) |
| **HS-ESS2-1**, unit 9 | Constructive and destructive processes are listed, but the model need not show interacting processes or feedback. | Add a model of changing relief and rates: uplift increases relief and erosion; erosion reduces relief and changes subsequent erosion. Students use the model across spatial and temporal scales. [Earth systems foundation elements](https://www.nextgenscience.org/dci-arrangement/hs-ess2-earths-systems) |

**Why it matters:** A busy writer could satisfy the present descriptions with energy categories, device descriptions and separate landform processes, while omitting the explanatory mechanisms the standards develop.

The earlier review’s charged-plate and Earth evidence fixes are present and should remain. These are additional gaps found by checking the primary sources.

### 3. Required crosscutting concepts disappear from units 6 and 9

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, the grade 2 frame review’s finding 1 identifies the same type  
**Confidence:** firm

**Location:** Units 6 and 9, the C3 and “Check set adds” columns.

**What is wrong:** Unit 6 lists patterns, stability and change, and societal influence, but omits cause and effect for its wave and device work. Unit 9 omits patterns from crust-age reasoning. The candidate additions do not repair these omissions.

**Why it matters:** The frame promises all three dimensions together. Other useful concepts cannot silently substitute for the elements attached to the claimed work.

**Exact fix:**

- Unit 6: add required cause-and-effect work. Students distinguish an observed association from evidence supporting a wave relationship, then explain how a designed device produces its intended effect. [Wave standards’ foundation elements](https://www.nextgenscience.org/dci-arrangement/hs-ps4-waves-and-their-applications-technologies-information-transfer)
- Unit 9: add required pattern reasoning from empirical crust-age evidence, alongside the existing energy and change work. [Earth’s place in the universe foundation elements](https://www.nextgenscience.org/dci-arrangement/hs-ess1-earths-place-universe)
- Distinguish required elements from optional “Check set adds.” A later unit plan may drop an optional addition, but must retain coverage of required elements.

### 4. Unit 5’s no-kit route drops the investigation performance

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, the science 4 review’s finding 7 requires honest limits for data-only alternatives  
**Confidence:** firm

**Location:** Unit 5, line 122, “No-kit path: provided meter readings.”

**What is wrong:** Reading supplied measurements supports analysis. It does not, by itself, preserve students’ responsibility for planning and conducting the investigation, including choosing measurements, trials and precision. Those decisions are part of HS-PS2-5’s practice. [Official investigation elements](https://www.nextgenscience.org/pe/hs-ps2-5-motion-and-stability-forces-and-interactions)

**Why it matters:** Students using the alternative could be recorded as completing the expectation while missing its central performance. This also conflicts with rubric S6.

**Exact fix:** Specify both directions of investigation, current producing a field and a changing field producing current. Require student decisions about controls, measurements, repetitions and limitations. For the no-kit route, provide selectable recorded runs or an interactive investigation with those decisions retained, and state plainly that recorded or simulated work is weaker than investigating the physical system. Supplied meter readings alone must not count as evidence of having conducted it.

### 5. The simplified orbital equation needs a central-body restriction

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** firm

**Location:** Math readiness, unit 3 teacher note, cross-subject mathematics table, and `phys-orbits` notes.

**What is wrong:** The frame uses \(T^2=a^3\), with years and astronomical units, while claiming predictions for planets, moons and launched satellites. That normalization is appropriate for a small object orbiting the Sun. It cannot be applied unchanged to a moon or satellite orbiting another body.

**Why it matters:** The earlier fractional-exponent fix is useful, but its unqualified equation could now generate incorrect orbital predictions.

**Exact fix:** Keep squares, cubes and calculator roots. State that \(a\) is the semimajor axis and restrict \(T^2=a^3\) to Sun-centred cases. For other central bodies, supply the appropriate coefficient in \(T^2=k a^3\), or compare two orbits around the same body using a supplied reference orbit. Do not require students to derive the coefficient. [NASA’s explanation of Kepler’s laws and the mass-dependent generalization](https://science.nasa.gov/solar-system/orbits-and-keplers-laws/)

### 6. Unit 8 opens by giving students the explanation

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, science 4 review finding 2 identifies an anchor that gives away its answer  
**Confidence:** likely

**Location:** Unit 8, line 125.

**What is wrong:** The anchor announces that the elements in students’ bodies were made inside earlier stars. That is a major conclusion of the unit, rather than an observation students need its models to explain.

**Why it matters:** The likely implementation becomes an illustrated account of a supplied explanation. Rubric S1 explicitly rejects an anchor that gives its answer away. The external rubric likewise calls for student sense-making driven by phenomena. [EQuIP science rubric, category I.A](https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf)

**Exact fix:** Open with a sourced set of laboratory element spectra and contrasting stellar spectra. Students identify similarities and differences, record initial explanations, and ask what light can reveal about stellar composition and history. Introduce stellar element formation and the early universe as explanations developed from evidence. Keep all three expectations and the 18 days.

### 7. The science rubric’s planning inventory is stale

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, grade 3 independent rerun finding 10  
**Confidence:** firm

**Location:** `docs/RUBRIC-SCIENCE.md`, lines 54 to 55.

**What is wrong:** The rubric says the grade 4 draft and middle school base text are the only material. The repository now contains the science progression and course frames, including Physics.

**Why it matters:** Reviewers receive an obsolete account of the evidence available for judging planning.

**Exact fix:** Replace that inventory with:

> Science planning includes `data/progressions/science.csv`, the course frames, the grade 4 scope and sequence draft, and the middle school base text. These documents describe intended teaching and do not establish completed courses.

Retain the distinction between plans and built materials.

### 8. The rubric incorrectly says no plan locates nature-of-science teaching

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, grade 3 independent rerun finding 11  
**Confidence:** firm

**Location:** `docs/RUBRIC-SCIENCE.md`, line 64, Gateway 2 connections row.

**What is wrong:** “No plan names where the nature of science is taught” is contradicted by Physics’ explicit locations in units 3, 7 and 8.

**Why it matters:** It presents placed work as unplaced, obscuring the actual next task of checking its implementation.

**Exact fix:** Replace the gap sentence with:

> Course frames name intended nature-of-science locations, including Physics units 3, 7 and 8. Unit plans and assessments must demonstrate the intended elements through student work.

## Ownership, standards, order and days

An independent comparison found **20 owned skills, 20 placements, no omissions, no duplicates and no extra skills from another grade**. Earlier-grade content is explicitly identified as retrieval, reactivation or reteaching. Across Biology, Chemistry and Physics, all **71 high school expectation codes** are owned exactly once, including all 19 Earth and space codes.

| Unit | Days | Owned expectations | Coverage judgment at frame level |
|---|---:|---|---|
| 1 | 18 | HS-PS2-1, HS-PS2-2 | Adequate commitment to quantitative motion and momentum |
| 2 | 12 | HS-PS2-3 | Design, evaluation and refinement secured |
| 3 | 16 | HS-PS2-4, HS-ESS1-4 | Both force laws and orbital representations placed; finding 5 |
| 4 | 16 | HS-PS3-2, HS-PS3-5 | Particle explanation needs strengthening; findings 1 and 2 |
| 5 | 11 | HS-PS2-5 | Both induction directions placed; alternative-route gap, finding 4 |
| 6 | 16 | HS-PS4-1, HS-PS4-2, HS-PS4-5 | Findings 2 and 3 |
| 7 | 14 | HS-PS4-3, HS-PS4-4 | Required evaluation practices placed; radiation framing needs correction |
| 8 | 18 | HS-ESS1-1, HS-ESS1-2, HS-ESS1-3 | Evidence and performances placed; anchor needs revision |
| 9 | 18 | HS-ESS2-3, HS-ESS2-1, HS-ESS1-5 | Findings 2 and 3; earlier evidence-restoration fixes present |
| 10 | 10 | HS-ESS1-6 | Evidence categories placed; age comparison needs qualification |

The broad order holds: momentum precedes collision design; forces precede orbital predictions; fields precede field-energy work; waves precede seismic interpretation; light precedes stellar evidence; Chemistry supplies fusion, half-life and thermal transfer first. The standards comparison used the [official DCI arrangements](https://www.nextgenscience.org/sites/default/files/AllDCI.pdf), particularly PDF pages 79 to 84 and 96 to 99.

**149 + 11 = 160 days.** The stated week ranges fit those allocations and the intervening checks. Each course check has response time, and unit assessments are explicitly inside unit allocations. Eleven days for unit 5’s practical investigation and twelve for unit 2’s iterative design are defensible despite each owning one expectation. No day transfer is justified by this read.

## Seams and cross-subject checks

- All twelve Chemistry handoffs are picked up in Physics. Biology’s ultraviolet and DNA handoff returns in unit 7.
- Dormant grade 6 content has named readiness and reteaching provision; grade 8 content has retrieval or model reactivation.
- The final-core-course position is accurately stated. Elective extensions are optional, and their unwritten frames are not a gap in core ownership.
- Algebra I and grade 8 mathematics teach the required algebra, graph interpretation and roots earlier. Avoiding rational exponents remains appropriate.
- ELA 11 teaches informative writing before Physics units 6 and 8, and argument before unit 8. Its current argument unit spans **weeks 7 to 11**, rather than the Physics table’s 8 to 11. This does not change availability.
- Physics waves precede Algebra II’s periodic modelling. The latter supplies independent contexts if courses are reordered.

The course arrangement is a defensible local use of the [modified-domain model in Appendix K](https://www.nextgenscience.org/sites/default/files/Appendix%20K_Revised%208.30.13.pdf). The [OpenSciEd high school sequence](https://www.openscied.org/wp-content/uploads/2023/09/OpenSciEd-High-School-Scope-Sequence-September-2021.pdf) provides a reference comparison for integrating Physics and Earth science, not a required order or an adaptation source.

## Science lens checklist

| Course-frame checklist line | Result |
|---|---|
| Every owned expectation has a unit and is taught sufficiently | **Placement met; fullness missed in the specified findings** |
| Grades 6 to 8 preserve base-text order or justify departures | **Not applicable** |
| High school expectations have named owning courses | **Met** |
| Every unit names an anchor phenomenon or design problem | **Met as placement; quality missed in findings 1 and 6** |

| General lens requirement, at frame depth | Result |
|---|---|
| Three dimensions used together | **Missed in specific commitments**, findings 2 and 3 |
| Phenomena drive units | **Partly met**, findings 1 and 6 |
| Coherent storyline and prerequisites | **Met in broad order**; lesson navigation remains later work |
| Models built and revised | **Met as a planning requirement**; revision points need unit plans |
| Argument from evidence | **Met as a planning requirement** |
| Planned investigations and fair tests | **Partly met**, finding 4 |
| Transfer at the end | **Met as a requirement**, including unseen course-check cases |
| Safety | **Met as frame-level provision**; physical procedures and qualified review remain outstanding |
| Plain facts | **Deep-time commitments met**; inaccurate simplifications require finding 1 |

The three-dimensional interpretation is consistent with the [National Research Council framework summary](https://www.nationalacademies.org/read/13165/chapter/2). This is a frame judgment, not a score for unwritten lessons or assessments.

## Settled by the expert

| Choice | Reason | File affected when applied |
|---|---|---|
| Retain 10 units and 160 days | No demonstrated allocation defect | Physics frame; `frames.csv` |
| Qualify the three absolute anchor claims | Preserve accurate, explainable phenomena | Physics units 4, 7 and 10 |
| Make particle, device-interaction and landform-feedback mechanisms explicit | Complete work within current ownership | Physics frame and corresponding progression notes |
| Restore required crosscutting elements in units 6 and 9 | Optional additions cannot replace required coverage | Physics frame |
| Retain experimental decisions in the no-kit route and state its limits | Preserve the practice and honest evidence claims | Physics unit 5 |
| Restrict the normalized orbital equation to its applicable system | Keep predictions correct without advanced mathematics | Physics frame; `phys-orbits` |
| Open unit 8 with spectral evidence | Leave the explanation for students to develop | Physics unit 8 |
| Correct ELA argument timing to weeks 7 to 11 | Match the current neighbouring frame | Physics cross-subject table |
| Rewrite both stale rubric notes | Distinguish placed plans from demonstrated implementation | Science rubric |

No standard moves between units or courses.

## What is right and should not be touched

Keep the explicit high school ownership, Chemistry handoffs, retrieval provisions, calculator-root approach, revised Earth evidence lists, unseen transfer tasks, response time and paper-path requirement. Keep the restrictions on mains electricity, battery types, lasers, ultraviolet lamps and viewing the Sun. Keep the clear statement that deep time is taught from evidence.

The earlier Physics review’s applied corrections remain useful. I disagree with its broader “checked and found right” conclusion where primary-source comparison exposes the additional mechanisms and crosscutting gaps above. The earlier independent review’s withheld verdict is superseded by this substantive read under the amended brief.

## What could not be judged

Actual 50-minute feasibility, model revisions, assessment quality, equipment costs and investigation safety require the unit plans and day materials. Qualified safety and materials review remains necessary. The full plan gate did not complete in this sandbox.

## Sources and memory

Primary standards, evidence statements, review criteria and scientific sources are linked beside their uses above. No curricular finding rests solely on memory. Prior memory informed reporting conventions only.

For `APPROACH-SOURCES.md`, add the newly consulted [energy evidence statement](https://www.nextgenscience.org/sites/ngss/files/HS-PS3-2_Evidence%20Statements%20Jan%202015.pdf), [orbital explanation](https://science.nasa.gov/solar-system/orbits-and-keplers-laws/), [radiofrequency explanation](https://www.arpansa.gov.au/understanding-radiation/what-is-radiation/non-ionising-radiation/radiofrequency-radiation) and [lunar sample account](https://www.brown.edu/news/2021-10-07/moon). The attempted Library of Congress page returned 403; it does not support a finding.

## For Cory

- **People and money:** Identify the qualified science teacher for investigation safety and materials, plus the sensitive-topic readers already requested by the frame. Any compensation remains Cory’s decision.
- No new scope or audience decision is required.

**Verdict: revise before scope and sequence. Finding count: 8. Report path: `docs/reviews/frame-physics-2026-11-14.md`, supplied here without writing a file.**


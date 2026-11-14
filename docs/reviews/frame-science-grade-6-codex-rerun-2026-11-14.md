# Independent frame review: Science Grade 6

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/frame-science-grade-6-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files changed.

## Verdict

Revise before using this frame as the fixed basis for the scope and sequence. Its ownership, year length and broad sequence are sound, but unit 4 gives conflicting instructions about the base lesson order, and several statements could produce incomplete or inaccurate teaching. Resolve those content issues first, then correct the pacing explanation and stale notes.

**Finding count: 10.**

## What I read and checked

- `docs/agents/EXPERT.md`, the science lens, `docs/RUBRIC-SCIENCE.md`, `docs/FOUNDATION.md`, `docs/GLOSSARY.md`, BASELINE rules 20 to 24, and the relevant approach and roadmap guidance.
- The complete Grade 6 frame, its `frames.csv` row, all 14 Grade 6 science progression rows, and the incoming and outgoing rows named by their handoffs.
- The Grade 5 and Grade 7 science frames, with Grade 8 ownership checked where Grade 6 contributes to later expectations.
- The Grade 6 mathematics and ELA frames and the relevant Grade 6 social studies frame passages.
- The source-map requirements in `frame-write.md`, `BASE-TEXTS.md`, the six stored standard-unit storylines, and relevant unit-page passages.
- Earlier Grade 6 frame reports, science progression reports and fixes, and related Grade 7 and Grade 8 findings.
- Official standards, evidence statements and source-program pages linked below.

`data/plans/science-grade-6/source-map.csv` is absent. This is **not a frame defect**: `frame-write.md` expressly assigns that lesson-and-day CSV to the scope-and-sequence stage. The embedded map is the applicable frame artifact.

`docs/APPROACH-SCIENCE.md` is also absent. I used the shared approach, science lens and science rubric; I did not infer an unwritten subject approach.

### Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Could not complete: `ModuleNotFoundError: No module named 'markdown'`. |
| `python -X utf8 scripts/frame.py check science-grade-6` | Passed, 0 failures; six units, 160 days, including four course-level days. |
| `python -X utf8 scripts/stale.py check` | Passed, 56 files, 0 failures. |

The unavailable general gate does not withhold this verdict. Its failure is an environment limitation, not evidence of a curriculum defect.

## Findings, most serious first

### 1. Unit 4 gives conflicting instructions about the base lesson order

**Severity:** Serious  
**LAYER:** base text  
**REPEAT:** yes, source-order conflicts recur in the science progression Codex read, finding F2  
**Confidence:** firm on the conflicting instructions

**Location:** Grade 6 frame, “Models carried,” unit 4, and the source-map loss check.

The frame promises the base lesson order, but twice requires the rock-cycle model first. The stored 6.4 storyline develops underground structure and plate motion through lessons 3 to 9, followed by past continental positions, strata evidence and erosion in lessons 10 to 14. Its [published unit description](https://openscied.org/instructional-materials/6-4-rock-cycling-plate-tectonics/) confirms that sequence.

A writer could reasonably follow “rock-cycle model comes first” by front-loading a complete cycle, breaking the promised storyline and teaching explanations before the evidence creates a need for them.

**Exact fix:** Replace the “rock-cycle first” instructions with:

> Plate and rock-process models develop together in the base lesson order. Lessons 3 and 7 to 9 build underground structure, plate motion, melting and new rock formation; lessons 10 to 14 add past positions, strata, weathering and erosion. Students synthesize the linked models as this evidence accumulates. A complete rock-cycle model is not an opening prerequisite.

Make the matching correction in “Models carried” and the loss check. Retain all four owned expectations in unit 4.

### 2. The cell wall is given the membrane’s regulatory job

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, cell-function coverage is also at issue in the Grade 8 frame read, finding 3  
**Confidence:** firm

**Location:** Unit 6; `data/progressions/science.csv`, `s6-cells-body-systems`.

Both say the membrane and wall control what enters and leaves a cell. This conflates their roles. The [MS-LS1-2 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/MS-LS1-2%20Evidence%20Statements%20June%202015%20asterisks.pdf) distinguishes membrane regulation from the structural role of plant cell walls.

Although Grade 6 only starts this expectation, an inaccurate initial model creates a later misconception.

**Exact fix:** Replace the phrase in both places with:

> The cell membrane controls what enters and leaves the cell; plant cells also have a cell wall that provides structural support.

Keep MS-LS1-2 as a contribution completed later.

### 3. MS-ESS2-2 is narrowed chiefly to different rates

**Severity:** Moderate  
**LAYER:** standard  
**REPEAT:** yes, earlier Grade 6 frame read, finding 4  
**Confidence:** firm

**Location:** Unit 4; `s6-surface-change-scales`.

The frame names different rates and broadly mentions different sizes, but supplies no microscopic process or explicit explanation connecting spatial scales. The [standard and evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/MS-ESS2-2%20Evidence%20Statements%20June%202015%20asterisks.pdf) require more than comparing slow uplift with a rapid landslide.

Without a concrete small-scale case, a writer can complete the stated examples while omitting that part of the expectation.

**Exact fix:** Add to unit 4 and the progression note:

> Students explain surface change across spatial as well as time scales, from water dissolving microscopic amounts of rock to erosion, deposition and mountain building. Include water, ice and wind, and compare gradual change with sudden events. A limestone-weathering case links small-scale dissolution with larger landforms, including underground formations.

Require an evidence-based explanation using the contrasting scales.

### 4. Unit 5’s wording makes the plate model explain storms

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** likely wording risk; firm on the scientific distinction

**Location:** Unit 5; `s6-hazard-forecast`.

The list of earthquakes, eruptions, tsunamis and storms is followed by “mapped and explained with the plate model.” The natural reading applies that explanation to every listed hazard. Storm patterns require the atmospheric and oceanic reasoning developed in unit 3. The official [weather expectation](https://www.nextgenscience.org/pe/ms-ess2-5-earths-systems) makes that mechanism explicit.

This could carry a false causal explanation into lessons and assessments.

**Exact fix:** Replace the opening with:

> Students map the locations, magnitudes and frequencies of natural hazards. They explain earthquake, eruption and earthquake-generated tsunami patterns with the plate model, and storm patterns with unit 3’s atmosphere and ocean models.

Use the same distinction in the progression note.

### 5. The no-microscope route does not define the investigation it preserves

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, earlier Grade 6 frame read, finding 1  
**Confidence:** likely

**Location:** Unit 6 materials note.

“Hand lenses and a public-domain micrograph set” does not establish what students investigate, record or compare. Hand lenses should not be presented as a general replacement for cellular microscopy. The course-wide admission that supplied data are weaker is helpful, but the local route still needs an instructional job.

The [MS-LS1-1 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/MS-LS1-1%20Evidence%20Statements%20June%202015%20asterisks.pdf) calls for recorded evidence across organisms and cell types, including comparisons relevant to living and nonliving material.

**Exact fix:** Replace the note with:

> Hand lenses support observations of visible structures, not a general substitute for cellular microscopy. No-microscope path: a guided investigation using scaled micrographs and a virtual microscope, with a paper equivalent. Students record and compare evidence from unicellular organisms, varied cells in multicellular organisms and nonliving samples. This path is weaker because students examine images collected by others rather than prepare and image their own samples.

No particular microscope purchase or magnification threshold is settled by this read.

### 6. The annual minute surplus is incorrectly described as a surplus in every unit

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, earlier Grade 6 frame read, finding 2  
**Confidence:** firm on arithmetic; judgment call on teaching feasibility

**Location:** “Days,” lines 11 to 13.

The year has 240 minutes beyond the base allocation, but unit 6 receives 1,100 minutes against the base’s 1,125. Thus “each unit gets its base time” is false. This matters because unit writers need to see where condensation is required.

**Exact fix:** Replace that claim with:

> Across the year, the unit allocation provides 240 minutes beyond the base total. This is distributed unevenly: units 1 to 5 gain 40, 35, 60, 75 and 55 minutes respectively; unit 6 is 25 minutes below base time before its added retrieval work. The scope and sequence must identify the condensation within unit 6 and account for those retrieval tasks explicitly.

The 25-minute difference alone does not establish that a whole additional day is necessary. I do not endorse an automatic day transfer from unit 3 without a lesson-level pacing map.

### 7. The light row still says its ownership correction is waiting

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale-note findings recur in the science progression expert read, finding 8  
**Confidence:** firm

**Location:** `data/progressions/science.csv:78`, `s6-light-paths`.

The note says moving ownership to Grade 8 waits on a way to mark contributing rows. The current data already use `~MS-PS4-2`, and `s8-earth-sun-moon` owns the expectation.

This invites reopening completed work.

**Exact fix:** Replace the obsolete sentence with:

> This row contributes to MS-PS4-2, marked ~; s8-earth-sun-moon owns and completes the expectation.

The frame already identifies this correction correctly.

### 8. The particle-temperature row still names the former owner

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, the same stale-status type as finding 7  
**Confidence:** firm

**Location:** `data/progressions/science.csv:79`, `s6-particle-temperature`.

The note says MS-PS3-5 sits on `s8-energy-transfer-argument`, although the current standard cell places ownership here and marks the Grade 8 application with `~`.

The contradictory directions obscure which course must establish proficiency.

**Exact fix:** Replace that sentence with:

> This row owns MS-PS3-5; s8-energy-transfer-argument applies it later to whole objects and is marked ~.

Preserve the current ownership cells.

### 9. The earlier Grade 6 review’s ELA status is stale

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale review results are already identified in the earlier Grade 6 report, finding 6  
**Confidence:** firm

**Location:** `docs/reviews/frame-science-grade-6-2026-11-14.md:118`.

It says the ELA 6 frame is not yet written. That frame exists and supplies a usable calendar. Leaving the statement current hides completed coordination.

**Exact fix:** Replace the status sentence, or append a dated update:

> ELA 6 now has a frame. Its weather research runs on days 63 to 86 and its hazards unit on days 137 to 156. Science supplies its own argument support in unit 2 and media-integration support in unit 5 where ELA instruction comes later.

Retain historical gate observations as observations of their respective environments.

### 10. The owned-standard count is wrong

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, earlier Grade 6 frame read, finding 5  
**Confidence:** firm

**Location:** “Standard,” line 16.

The frame says 13 owned codes. There are **14 owned expectations on 14 progression rows**, plus one contributing expectation. One row contributes without owning, while `s6-particle-temperature` owns two codes.

**Exact fix:**

> The course owns 14 performance expectations on 14 progression rows and contributes the ray part of MS-PS4-2.

## Coverage, sequence and seams

### Owned skills and standards

All 14 Grade 6 skills appear exactly once in the unit Skills column. No other grade’s skill is placed there as a new owner. Earlier learning is identified as retrieval or review, and contributions to later expectations are named.

The following is a frame-level coverage judgment, not certification of unwritten lessons or assessment items.

| Unit | Owned expectations | Result |
|---|---|---|
| 1 | None; contributes to MS-PS4-2 | Contribution and later owner correctly identified |
| 2 | MS-PS3-3, MS-PS3-4, MS-PS3-5 | Design, investigation and evidence-supported energy argument provided for |
| 3 | MS-PS1-4, MS-ESS2-4, MS-ESS2-5, MS-ESS2-6 | State-change, water-cycle, weather and circulation work provided for |
| 4 | MS-ESS2-1, MS-ESS2-2, MS-ESS2-3, MS-ESS1-4 | Placement complete; sequence conflict and spatial-scale omission require findings 1 and 3 |
| 5 | MS-ESS3-2, MS-PS4-3 | Coverage provided for; causal wording needs finding 4 |
| 6 | MS-LS1-1 | Main route provided for; fallback needs finding 5 |

I checked these claims against the [official DCI arrangement](https://www.nextgenscience.org/sites/default/files/AllDCI.pdf) and the individual standards and evidence statements linked in the findings.

The broad order has sound reasons: light supports thermal design; particles and energy support weather; plate reasoning supports geologic hazards; cells support Grade 7 metabolism. The unit 4 wording conflict is the material internal-order exception.

### Days and source map

| Unit | Skills | Base days at 45 minutes | Planned days at 50 minutes | Minute difference |
|---|---:|---:|---:|---:|
| 1 | 1 | 18 | 17 | +40 |
| 2 | 2 | 37 | 34 | +35 |
| 3 | 4 | 42 | 39 | +60 |
| 4 | 4 | 25 | 24 | +75 |
| 5 | 2 | 21 | 20 | +55 |
| 6 | 1 | 25 | 22 | -25 |
| **Total** | **14** | **168** | **156** | **+240** |

The four additional course-level days give a 160-day year. Both course-level assessments have a respond day.

The map places all **86 Grade 6 base lessons** in the corresponding six units, with no omitted lesson ranges. The mapped folders are the standard units, not the excluded computer-science variants. The six-unit order is preserved; finding 1 concerns the contradictory instruction *within* unit 4.

The shared loss check also makes claims about Grades 7 and 8. Their existing reports identify unresolved additions. This Grade 6 review does not independently certify that entire 59-expectation claim.

### Seams and cross-subject timing

- **Grade 5 into Grade 6:** particles, conservation, Earth-system interactions and fair design tests are picked up. Older light, weather, rock and sensory learning has explicit retrieval.
- **Grade 6 into Grade 7:** particles and state change feed reactions; thermal design feeds optimization; cells feed body systems; climate, water and geology feed the final Earth-systems unit.
- **Longer handoffs:** the later owners of light, sensory processing and cell functions are identified. Correcting the cell-wall statement preserves that handoff.
- **Mathematics:** ratio language, unit rates and scaling arrive before science units 4 and 6. Statistics arrive later, so the supplied bridges remain necessary. The conditional fallback table is appropriate; it should not be read as evidence that every listed mathematical skill comes later.
- **ELA:** informative writing precedes science unit 4. Argument instruction overlaps science unit 2, and media integration follows science unit 5; science appropriately supplies local support.
- **Social studies:** its timeline and latitude work precede science’s corresponding uses.

## Science lens checklist

Each line in the lens’s **course frame** checklist is addressed below.

| Lens line | Result |
|---|---|
| Every owned performance expectation has a unit and is sufficiently covered | **Missed in part:** MS-ESS2-2 needs finding 3; the microscopy fallback needs finding 5 |
| Grades 6 to 8 preserve base order or explain departures and losses | **Missed in part:** six-unit order retained, but unit 4’s internal instruction conflicts with it |
| High school expectations have explicit course ownership | **Not applicable** |
| Every unit names an anchor phenomenon or design problem | **Met** |

At this layer, the frame also provides for question boards, model revision, evidence-based argument, design, unseen end-of-unit tasks, materials alternatives and safety review. Their actual quality must be judged in the later unit and day artifacts. This distinction follows the [EQuIP rubric’s treatment of coherent, three-dimensional performances](https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf).

## What is right and should be preserved

- Complete, unique skill placement and the current contributing-standard notation.
- The six-unit sequence and the substantial particle-to-weather and geology-to-hazards connections.
- Explicit engineering starts and later completion owners.
- Course-level respond days, paper alternatives and no-account requirements.
- Plain treatment of Earth’s age, careful disaster and disability framing, and named needs for qualified readers.
- The strengthened linked atmosphere-ocean model. The earlier omission of salinity and continental constraints has been addressed; it is not reopened here.

This read disagrees with the earlier report’s unqualified source-order approval because of finding 1. It also does not adopt its automatic whole-day redistribution or a prescribed microscope purchase.

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Keep unit 4 in the base lesson order and develop its models progressively | Removes conflicting writer instructions | Grade 6 frame |
| Distinguish membrane regulation from wall support | Correct initial cell model | Frame and science progression |
| Use a limestone-weathering case for the small spatial scale | Makes the missing scale concrete within the existing expectation | Frame and science progression |
| Explain storms with unit 3’s models | Preserves correct causal reasoning | Frame and science progression |
| Specify a recorded-data microscopy fallback and its limitation | Makes the fallback teachable without deciding a purchase | Grade 6 frame |
| Retain the 160-day proposal while exposing the actual minute margins | Arithmetic alone does not establish a whole-day shortfall | Grade 6 frame |
| Keep current standard ownership and replace obsolete notes | The ownership changes are already implemented | Science progression |
| Correct the count to 14 owned expectations | Recomputed from current rows | Grade 6 frame |

## What I could not judge

- Whether every investigation, discussion and assessment fits the proposed periods. That requires the lesson-level allocation and classroom timing.
- Detailed practice and crosscutting-concept element coverage, assessment quality and safety implementation in unwritten unit and day materials.
- Final rights clearance for replacement images, readings and simulations.
- The full shared Grade 7 and Grade 8 loss check beyond the relevant seams and existing reports.

No curricular finding rests solely on memory. Prior session memory informed report formatting only.

## For Cory

- **Audience and timetable:** the existing assumption of five 50-minute lessons weekly.
- **Scope and catalog structure:** the existing proposal for three year courses under the middle-school band label.
- **People and money:** the science safety/materials reader, disability-community reader and counselor review already requested by the frame.

## Sources and source-list additions

Official sources were opened during this read:

- [NGSS DCI arrangement](https://www.nextgenscience.org/sites/default/files/AllDCI.pdf): expectation wording, clarification statements and boundaries.
- [MS-ESS2-2 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/MS-ESS2-2%20Evidence%20Statements%20June%202015%20asterisks.pdf): spatial scales and geoscience evidence.
- [MS-LS1-1 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/MS-LS1-1%20Evidence%20Statements%20June%202015%20asterisks.pdf): investigation and observation requirements.
- [MS-LS1-2 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/MS-LS1-2%20Evidence%20Statements%20June%202015%20asterisks.pdf): membrane, wall and whole-cell functions.
- [Weather standard](https://www.nextgenscience.org/pe/ms-ess2-5-earths-systems): air-mass mechanisms and permitted data sources.
- [Base unit 6.4](https://openscied.org/instructional-materials/6-4-rock-cycling-plate-tectonics/) and [base unit 6.6](https://openscied.org/instructional-materials/6-6-cells-systems/): sequence and investigation context.
- [EQuIP science rubric](https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf): coherence and integrated student performances.

**For the source list:** add the three directly linked evidence statements if they are not already indexed. They give more useful completion criteria than the local code-only inventory.

**Verdict:** Revise before freezing the frame.  
**Finding count:** 10.  
**Report path:** `docs/reviews/frame-science-grade-6-2026-11-14.md`, supplied above, not written.


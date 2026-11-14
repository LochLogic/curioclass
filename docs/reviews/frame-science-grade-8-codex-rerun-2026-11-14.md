# Independent review: Science, Grade 8 course frame

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/frame-science-grade-8-2026-11-14.md`  
**Delivery:** Complete report below. No files changed.

## Verdict

Revise before detailed unit planning. The six-unit order, skill ownership and main course seams are sound, but the frame understates several required performances and does not demonstrate enough time for its promised additions and reteaching. The most consequential change is to identify those additions explicitly and budget them alongside the full standards, while preserving the base sequence.

## What I read and checked

- `docs/agents/EXPERT.md`, the science lens, science rubric, foundation, glossary, teaching approach, source register, relevant roadmap guidance and BASELINE rules 20 to 24.
- The complete grade 8 frame, its `frames.csv` entry and all 26 grade 8 science progression rows.
- The grade 7 and Biology frames, the grade 6 shared source map and loss check, and relevant Chemistry and Physics handoffs.
- Grade 8 math and ELA frames, with earlier math prerequisites checked against their progression and frames.
- Relevant earlier science progression, reconciliation, fixes and frame reviews.
- All six locally stored grade 8 base storylines and relevant unit pages.
- Official standards, evidence statements, base-unit descriptions and science review guidance linked below.

`data/plans/science-grade-8/source-map.csv` does not exist. This is **not a finding**: `frame-write.md` explicitly requires the summary source map now and defers the day-level CSV until the scope and sequence.

| Gate | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Could not finish: `ModuleNotFoundError: No module named 'markdown'`. |
| `python -X utf8 scripts/frame.py check science-grade-8` | Passed: zero failures; six units; 160 days, comprising 156 unit days and four course-level days. |
| `python -X utf8 scripts/stale.py check` | Passed: 56 files checked, zero marked failures. |

The unavailable repository-wide gate does not withhold this curriculum verdict.

## Findings

### 1. Unit 4 does not describe the light-wave work that completes MS-PS4-2

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, earlier grade 8 review, finding 4  
**Confidence:** firm

**Location:** `frame.md`, unit 4, unit 2 and the incoming light seam.

Unit 4 claims completion through reflected moonlight and the words “reflected, absorbed or transmitted.” That leaves out the qualitative wave model explaining brightness, color, frequency-dependent bending and light crossing empty space. Those elements are explicit in both the progression row and the [official standard](https://www.nextgenscience.org/pe/ms-ps4-2-waves-and-their-applications-technologies-information-transfer).

Unit 2 also calls sound’s material interactions a review of grade 6. Grade 6 supplied the light-ray contribution; applying these interactions to sound is new work here.

**Why it matters:** A writer following this summary could omit the very work for which ownership moved to grade 8.

**Exact fix:** Replace the unit 4 completion description with:

> Students develop, revise and use a qualitative wave model of light to explain brightness, color, reflection, absorption, transmission and color-dependent bending between materials. They distinguish light crossing empty space from sound requiring matter.

In unit 2, write:

> New contribution to MS-PS4-2: students model sound reflected, absorbed or transmitted by materials, building on grade 6’s light-ray work.

Update the seam to name both contributions.

### 2. The source map does not distinguish important additions from base adaptations

**Severity:** Serious  
**LAYER:** base text  
**REPEAT:** yes, earlier grade 8 review, findings 1 and 3  
**Confidence:** firm on the mismatch; judgment call on added time

**Location:** Units 3 and 5, Source map and loss check.

Unit 3 promises electric-charge investigations and magnetic, electric and gravitational potential-energy models. The [base unit’s own description](https://openscied.org/instructional-materials/8-3-forces-at-a-distance/) identifies electricity as an extension and gravity as subsequent work in 8.4. Its core storyline chiefly develops magnetic interactions.

Unit 5 promises completion of the whole-cell standard, but the [base description](https://openscied.org/instructional-materials/8-5-genetics/) describes contributions building on earlier cell work and marks MS-LS1-2 partial. The frame lists cell parts without locating a synthesis that demonstrates their combined function. The [official evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/MS-LS1-2%20Evidence%20Statements%20June%202015%20asterisks.pdf) requires that integrated model.

**Why it matters:** “Adapt one base unit whole” and “nothing lost” conceal work that the unit writer must deliberately add or consolidate.

**Exact fix:** Add these entries to the source-map commentary and unit descriptions:

- Unit 3: a required electrical-charge investigation, including questions about charge, separation and force, plus evaluation of the experimental design.
- Unit 3: explicitly located transfer of the stored-energy model to electrical and gravitational systems, as the frame already promises.
- Unit 5: a whole-cell synthesis near the chromosome and nucleus work, integrating earlier membrane, wall, chloroplast and mitochondrion learning.

Label these **Curio Class additions or consolidations**, locate them relative to base lessons and include their time in finding 3.

I agree with the earlier review’s need to expose these additions. I do **not** treat every illustrative example in a clarification statement as a compulsory separate investigation. In particular, a magnetic-system model alone does not establish failure of MS-PS3-2; the additional issue here is the frame’s explicit promise to address all three interaction types.

### 3. The 160-day fit leaves virtually no allowance for the work added by this frame

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, earlier grade 8 review, finding 2  
**Confidence:** firm on arithmetic and conflicting promises; judgment call on the eventual total

**Location:** Days bullet, unit allocations and For the lead item 2.

| Unit | Base days at 45 minutes | Allocated days at 50 minutes | Difference from base minutes |
|---|---:|---:|---:|
| 1 | 29 | 26 | -5 minutes |
| 2 | 24 | 22 | +20 minutes |
| 3 | 30 | 27 | 0 minutes |
| 4 | 31 | 28 | +5 minutes |
| 5 | 28 | 25 | -10 minutes |
| 6 | 31 | 28 | +5 minutes |
| **Total** | **173** | **156** | **+15 minutes** |

The rounding explanation says units receive added allowance for readiness and reactivation. The allocations instead reproduce almost exactly the base minutes.

The frame adds twelve distinct dormant prerequisite checks, retrieval and reactivation work, and the adaptations in finding 2. Its small-group reteaching proposal also conflicts with the progression’s promise of a one-lesson reteach when dormant prerequisites are missed.

**Why it matters:** Students needing support are most likely to lose either that support or access to the continuing storyline.

**Exact fix:** Replace the rounding claim with:

> These allocations currently reproduce the base time with 15 minutes remaining across the year. The 160-day fit is provisional until the scope and sequence budgets readiness work, reteaching and additions, and identifies corresponding time savings.

Produce a lesson-level minute allocation showing the retained base work, additions, support time and named savings. Preserve the four course-level assessment and respond days. If it exceeds 160 days, bring the resulting calendar or scope choice to Cory.

The earlier review’s approximately 170-day proposal is a planning estimate, not an established minimum. Nor is there sufficient evidence to prohibit all small-group support. The binding problem is the unbudgeted promise and inconsistency with the progression.

### 4. Several unit summaries replace required student performances with content statements

**Severity:** Serious  
**LAYER:** standard  
**REPEAT:** yes, earlier standards-in-full findings  
**Confidence:** firm

**Location:** Units 1 to 6.

The general promise of models and evidence does not reliably preserve each standard’s particular performance.

| Location | Missing or narrowed requirement | Exact addition |
|---|---|---|
| Unit 1, MS-PS3-1 | Students read graphs, but constructing them is not named. | “Students construct and interpret graphs comparing energy with mass at fixed speed, and energy with speed at fixed mass.” |
| Unit 2, MS-LS1-8 | Hearing is described, without an explicit synthesis across receptor inputs. | Add a source-based synthesis comparing mechanical, chemical and light inputs, signals, immediate responses and memories. |
| Unit 3, MS-PS2-5 | Investigation is named; evaluation of its design is missing. | Require students to judge whether their investigation establishes a non-contact interaction, identify a limitation and propose an improvement. |
| Unit 4, MS-ESS1-2 | Gravity holding objects together is named, but the required model and disk-origin idea are not explicit. | Require a student-developed model linking solar-system and galactic motions, placing the solar system within the Milky Way, and explaining the gravitational gathering of the original dust-and-gas disk. |
| Unit 5, MS-LS3-1 | Gene, protein and trait facts are present; a student-developed causal model is not specified. | Require students to develop and use the changed-gene, possible protein-change, organism-effect model, within the stated molecular boundary. |
| Unit 6, MS-LS4-3 | Similar embryos are named without the comparison to adult anatomy. | Require analysis of matched developmental images to infer relationships not evident from adult anatomy. |
| Unit 6, MS-LS1-4 | Helpful reproductive structures and behaviors are named without the empirical argument. | Require an evidence-based argument connecting animal behaviors and specialized plant structures to the probability of successful reproduction, drawing on unit 5’s plant evidence. |

**Why it matters:** These omissions could produce accurate explanations delivered by the teacher while students never perform the claimed standards.

The requirements are supported by the official [energy](https://www.nextgenscience.org/pe/ms-ps3-1-energy), [sensory information](https://www.nextgenscience.org/pe/ms-ls1-8-molecules-organisms-structures-and-processes), [fields](https://www.nextgenscience.org/pe/ms-ps2-5-motion-and-stability-forces-and-interactions), [space-model](https://www.nextgenscience.org/pe/ms-ess1-2-earths-place-universe), [mutation-model](https://www.nextgenscience.org/pe/ms-ls3-1-heredity-inheritance-and-variation-traits), [embryology](https://www.nextgenscience.org/pe/ms-ls4-3-biological-evolution-unity-and-diversity) and [reproduction](https://www.nextgenscience.org/pe/ms-ls1-4-molecules-organisms-structures-and-processes) pages.

These changes preserve existing ownership and unit placement.

### 5. Retained base activities introduce hazards and sensitive content absent from the frame

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, earlier grade 8 review, findings 5 and 6  
**Confidence:** firm

**Location:** Units 1 to 3.

Both contact-forces and sound storylines use a laser and mirror to reveal small movements. The frame names neither that arrangement nor its replacement. Speaker dissection also needs a preparation rule. Contact-forces assessments include concussion examples, missing from the sensitive-topic notes.

**Why it matters:** Whole-unit adaptation can carry these activities forward without the necessary planning controls.

**Exact fix:**

- Units 1 and 2: explicitly replace the laser demonstrations with supplied displacement observations or cleared images/data unless a qualified safety review specifies a controlled apparatus and procedure.
- Unit 3: require the teacher to open speakers in advance and control sharp edges and strong magnets.
- Unit 1: name concussion as sensitive content, use impersonal sporting examples and request no student health stories.

Do not combine a mirror-based activity with the earlier recommendation to prohibit all shiny surfaces. [NSTA’s guidance](https://www.nsta.org/science-and-children/science-and-children-novemberdecember-2021/immerse-elementary-students-light) specifically identifies reflected laser light as a hazard.

### 6. Cross-subject rows identify the wrong progression skills

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, earlier cross-subject synchronization findings  
**Confidence:** firm

**Location:** Cross-subject table.

The placements generally work with the existing bridges, but several row labels do not match `science.csv`:

- The scatter-plot dependency belongs to `s8-gravity-mass`, not `s8-solar-system-scale`.
- The written-argument dependencies belong to `s8-energy-transfer-argument` and `s8-reproduction-behaviors`, rather than the listed fields and natural-selection rows.

**Why it matters:** A later planner following row IDs could scaffold or assess the wrong task.

**Exact fix:** Correct those IDs and replace provisional availability language with the current calendars:

| Dependency | Current availability and response |
|---|---|
| Qualitative functions | Math unit 6, days 93 to 116. Science units 1 and 2 retain their explicit graph-reading bridge. |
| Scatter plots | Math unit 4, introduced about days 56 to 60, before science units 4 and 5. Retain the fallback. |
| Grade 8 argument writing | ELA unit 2, days 31 to 58. Science unit 3 begins day 49, so retain its argument frame during the overlap. |
| Research and source evaluation | ELA unit 3, days 59 to 84. Science unit 2 supplies its own guided source work; unit 5 can reuse the taught routine. |
| ELA genetics thread | ELA unit 5, days 125 to 156, overlapping the end of science genetics. Give ELA its stated background reading until science completion. |

Write the scientific-notation restriction plainly: science unit 4 uses written-out distances or earlier-grade powers of ten and does not require operations in scientific notation before math unit 7.

### 7. The model-history table misstates the last use of two models

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, earlier grade 8 review, finding 8  
**Confidence:** firm

**Location:** Models carried, force-diagram and wave-model rows.

The wave model does not rest throughout grades 5 to 7: `s6-digital-signals` uses it in grade 6. The force-diagram ancestry omits its grade 5 use in `s5-gravity-down`.

**Why it matters:** Readiness tasks should reactivate the actual earlier representation and distinguish what is retained from what is new.

**Exact fix:**

- Wave model: “From grade 4; used for information patterns in grade 6 unit 5; rests in grade 7; amplitude-energy work developed in unit 2.”
- Force diagram: add `s5-gravity-down` as the most recent earlier use, while retaining the contact-force reactivation.

### 8. The grade 6 light note still says the ownership move is pending

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

**Location:** `data/progressions/science.csv`, `s6-light-paths`, line 78.

The note says moving ownership to grade 8 waits on a contributing-row mechanism. The standard column already uses `~MS-PS4-2`, and grade 8 owns the code.

**Why it matters:** A resolved allocation appears open.

**Exact fix:** Replace the obsolete sentence with:

> Grade 6 contributes the ray-model work, marked ~MS-PS4-2. Grade 8 owns and completes the expectation through s8-earth-sun-moon.

### 9. The sound progression note names the former light-standard owner

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

**Location:** `science.csv`, `s8-wave-amplitude-energy`, line 113.

Its note says MS-PS4-2 is owned by `s6-light-paths`, contrary to the current ownership columns.

**Why it matters:** It directs writers to an incomplete contribution as the owner.

**Exact fix:** Replace that clause with:

> This supplies the mechanical-wave contribution to MS-PS4-2; s6-light-paths contributes the earlier ray model, and s8-earth-sun-moon owns and completes the expectation.

### 10. The Earth-sun-moon note also retains the former owner

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

**Location:** `science.csv`, `s8-earth-sun-moon`, line 121.

“The code sits on s6-light-paths” contradicts this row’s own standard column and its later correct ownership sentence.

**Why it matters:** One row gives two incompatible instructions.

**Exact fix:** Replace the obsolete parenthesis with:

> Owns and completes MS-PS4-2, following contributions from s6-light-paths and s8-wave-amplitude-energy.

### 11. The rubric’s inventory of existing science plans is stale

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

**Location:** `docs/RUBRIC-SCIENCE.md`, lines 54 to 55.

The rubric says the grade 4 draft and middle-school base are the only material. Course frames now exist.

**Why it matters:** Reviewers receive an inaccurate starting inventory.

**Exact fix:**

> No finished science course is claimed here. Science progression data and course frames are also on file; these are plans, distinct from built lessons and classroom evidence.

### 12. The rubric’s nature-of-science gap is stale

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

**Location:** `RUBRIC-SCIENCE.md`, Gateway 2 connections row, line 64.

“No plan names where the nature of science is taught” is contradicted by the grade 8 frame’s explicit placements and by adjacent frames.

**Why it matters:** It requests completed placement work while obscuring the remaining implementation work.

**Exact fix:**

> Course frames now name nature-of-science placements. Unit plans and assessments must specify the student performances and evidence at those placements.

### 13. The earlier grade 8 review says the ELA frame is unwritten

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

**Location:** Existing `frame-science-grade-8-2026-11-14.md`, Cross-subject, line 204.

The current ELA frame exists and supplies the calendar checked in finding 6.

**Why it matters:** The earlier conclusion leaves a dependency unresolved after evidence became available.

**Exact fix:**

> Updated by the second read: the ELA 8 frame is on file. Its argument, research and genetics-thread timing has been compared with science; retain the bridges and correct row references described in the second report.

### 14. The progression fixes report still presents high school math placement as absent

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

**Location:** `progression-science-fixes-2026-11-13.md`, Skipped, line 41.

“There is no high school math progression yet” is no longer current: `math.csv` includes grades 9 to 11 and the corresponding frames exist.

**Why it matters:** Subsequent science reviews may rely on generic scaffolds without checking actual availability.

**Exact fix:** Preserve the historical record with this replacement:

> At this fixes pass, high school math placement was unavailable. It is now on file in math.csv and the high school math frames; subsequent science planning checks that calendar and retains scaffolds wherever math comes later.

### 15. The earlier independent report’s blocked status needs a supersession note

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

**Location:** `frame-science-grade-8-codex-2026-11-14.md`, Verdict and Settled by the expert.

That report withheld all curriculum judgment because of the repository-wide gate. The present instruction explicitly removes that restriction, and this read has now completed the substantive review.

**Why it matters:** Leaving it as the current independent result conceals the completed review.

**Exact fix:** Add:

> Superseded by the completed second read delivered on 2026-11-14. The ordinary plan gate remains unavailable in that sandbox because markdown is missing; the course structural check passes, and the curriculum verdict is revise before detailed unit planning.

## Coverage, sequence and seams

All **26 grade 8 progression rows appear exactly once** in the Skills column. They own **26 distinct codes**; the additional MS-PS3-5 contribution is correctly marked as application of grade 6 ownership.

| Unit | Owned standards checked | Result at frame level |
|---|---|---|
| 1 | MS-PS2-1, MS-PS2-2, MS-PS3-1, MS-ETS1-2, MS-ETS1-3 | Ownership and order sound; preserve graph construction under finding 4. |
| 2 | MS-PS4-1, MS-LS1-8 | Appropriate placement; correct the wave contribution and require sensory synthesis. |
| 3 | MS-PS2-3, MS-PS2-5, MS-PS3-2 | Explicit additions, experimental-design evaluation and time accounting needed. |
| 4 | MS-ESS1-1, MS-PS4-2, MS-PS2-4, MS-ESS1-2, MS-ESS1-3 | Main sky sequence sound; complete the light-wave and gravity-model descriptions. |
| 5 | MS-LS3-1, MS-LS3-2, MS-LS1-2, MS-LS1-5, MS-LS4-5 | Appropriate completion point; whole-cell synthesis and causal mutation model need explicit tasks. |
| 6 | MS-LS4-1 through MS-LS4-4, MS-LS4-6, MS-LS1-4 | Appropriate placement; preserve embryological comparison and reproductive argument. |

The six unit reasons hold: contact forces precede sound and fields; fields precede orbital models; inheritance precedes selection. No unit needs moving.

The grade 7 handoffs into design, cells, growth, sensory processing and populations are picked up. Biology’s immediate uses of cell function, inheritance, selection and design match the grade 8 handoffs. Later Chemistry and Physics connections are also represented.

The summary source map places every grade 8 base lesson in order, except optional 8.1 lesson 16, explicitly omitted with a reason. No noncommercial variant is mapped. The weakness is the unrecorded adaptation work, not lesson-range coverage.

## Science lens checklist

| Course-frame checklist line | Result |
|---|---|
| Every owned expectation has a unit that teaches it fully | **Missed:** findings 1, 2 and 4. |
| Grades 6 to 8 preserve base order and document departures or losses | **Order met; adaptation accounting missed:** findings 2 and 3. |
| High school band expectations have explicit course ownership | **Not applicable** to this middle-school frame. |
| Every unit names an anchor phenomenon or design problem | **Met.** |

| Supporting lens principle | Frame-level result |
|---|---|
| Three dimensions used together | Planned, but several required performances need finding 4’s corrections. |
| Phenomenon-driven storyline | Met as a planning commitment. |
| Models built and revised | Met as a commitment; completion tasks and history need correction. |
| Argument from evidence | Present; reproductive argument needs explicit placement. |
| Planned investigations and interpretable data | Present; design evaluation needs explicit wording. |
| Transfer assessment | Met as a commitment to unseen cases. |
| Safety | Incomplete for retained activities, finding 5. |
| Plain scientific facts | Met: evolution and deep time are stated without softening. |

These are frame judgments, not scores for unwritten lessons or assessments. The [EQuIP rubric](https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf) supports checking the coherence and actual student performances at those later layers.

## What is right and should remain

- The six-unit base order and its prerequisite logic.
- Exactly-once skill placement and contributing-standard notation.
- Engineering through designing, evaluating and combining solutions.
- Course assessments followed by respond days.
- Unseen transfer cases, model revision and question-board commitments.
- Paper paths, no student accounts and low-cost materials alternatives.
- Respectful genetics and hearing provisions, including the named community-reader need.
- Evidence-based treatment of evolution.

## Settled by the expert

These choices preserve existing scope and ownership. They have not been applied.

| Choice | Reason | File affected |
|---|---|---|
| Keep all six units in their present order | Dependencies and base sequence agree. | Grade 8 frame |
| Retain the omission of optional 8.1 lesson 16 | It is outside the required base sequence. | Grade 8 source-map section |
| Require light-wave completion in unit 4 | This course owns the completed standard. | Grade 8 frame |
| Identify electrical work and whole-cell synthesis as explicit adaptations | Writers need their location and time. | Grade 8 frame and future source map |
| Preserve each standard’s required student performance | Content statements alone can narrow the teaching. | Unit descriptions |
| Correct dependency IDs and model histories | Current progression and adjacent frames settle them. | Cross-subject and Models carried |
| Treat 160-day fit as provisional pending a minute budget | Only 15 minutes remain above base time. | Days and For the lead |
| Mark obsolete status notes as superseded | Preserve history while making current status clear. | Findings 8 to 15 locations |

## What I could not judge

- Actual classroom timing or whether 160 days can be achieved through sound adaptations.
- Assessment quality, practice-element coverage, materials costs and complete safety procedures at unwritten layers.
- The full archived Teacher Editions inside ZIP files. They were not extracted because this task prohibits file creation. The storylines, unit pages and relevant official standards were accessible.
- Whether a newer sample DNA-extraction handout in the source store exactly matches the locked base edition. Its alcohol procedure needs a version and safety check if retained.

Memory informed the review method only. No curriculum finding rests on remembered standard wording or an unverified prior-session fact.

## Sources and source-list additions

- [Official standards compilation](https://www.nextgenscience.org/sites/default/files/AllDCI.pdf): checked performance expectations, foundation elements and boundaries.
- [MS-PS2-3 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/MS-PS2-3%20Evidence%20Statements%20June%202015%20asterisks.pdf): confirmed electrical-force questioning alongside magnetic-force work.
- [MS-LS1-2 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/MS-LS1-2%20Evidence%20Statements%20June%202015%20asterisks.pdf): confirmed whole-cell modeling and plant-animal comparison.
- [MS-ESS1-2 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/MS-ESS1-2%20Evidence%20Statements%20June%202015%20asterisks.pdf): confirmed solar-system and galaxy model requirements.
- Base-unit pages: [contact forces](https://openscied.org/instructional-materials/8-1-contact-forces/), [sound](https://openscied.org/instructional-materials/8-2-sound-waves/), [forces at a distance](https://openscied.org/instructional-materials/8-3-forces-at-a-distance/), [Earth in space](https://openscied.org/instructional-materials/8-4-earth-in-space/), [genetics](https://openscied.org/instructional-materials/8-5-genetics/) and [selection and ancestry](https://openscied.org/instructional-materials/8-6-natural-selection-common-ancestry/): checked unit contributions and sequence.
- [EQuIP science rubric](https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf): coherence and student-performance review principles.
- [NSTA light-investigation guidance](https://www.nsta.org/science-and-children/science-and-children-novemberdecember-2021/immerse-elementary-students-light): reflected-beam hazard.

For the source register, add the specific evidence-statement links if absent. The base unit pages’ explanation of partial development and extension content is particularly useful alongside their standard-code lists.

## For Cory

- **Calendar and audience:** If a lesson-level budget exceeds 160 days at 50 minutes, decide the longer calendar or a named scope/pacing accommodation. Neither 160 nor approximately 170 days is yet classroom-validated.
- **People and money:** Identify the science safety/materials reader and the Deaf and hard of hearing community reader, with any compensation.

**Verdict:** Revise before detailed unit planning. **Finding count:** 15, comprising seven curriculum/planning findings and eight stale-status findings. **Report path:** `docs/reviews/frame-science-grade-8-2026-11-14.md`, supplied here only.


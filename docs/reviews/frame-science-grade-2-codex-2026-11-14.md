# Independent expert read: Science, Grade 2 course frame

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/frame-science-grade-2-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files were created, edited or deleted.

## Verdict

The frame has a coherent sequence, complete skill placement and a defensible 76-lesson budget, but needs revision before detailed planning. Its biggest risk is that complete standard-code coverage masks incomplete performance requirements in materials classification, habitat comparison and source evaluation. Complete those requirements within their existing units and explicitly require an unfamiliar end-of-unit task, while retaining the unit order and day totals.

**Finding count: 7, comprising four curriculum findings and three stale-note findings.**

## What I read and checked

- `docs/agents/EXPERT.md`, the science lens and `docs/RUBRIC-SCIENCE.md`.
- `docs/FOUNDATION.md`, the requested ROADMAP sections, BASELINE rules 20 to 24, `docs/GLOSSARY.md`, `docs/APPROACH.md`, and relevant entries and evidence notes in `docs/APPROACH-SOURCES.md`.
- The complete [grade 2 science frame](/S:/CurioClass/docs/courses/science-grade-2/frame.md), its `frames.csv` row, all 12 grade 2 science progression rows, their incoming and outgoing connections, and the grade 1 and grade 3 science frames.
- The grade 2 mathematics frame and relevant mathematics and ELA progression rows.
- The grade 2 social studies frame and the grade 1 landform and map-key handoff.
- `docs/sources/BASE-TEXTS.md`, the local science standards inventory, relevant science progression reviews and fixes, the science reconciliation, the earlier grade 4 science review, and relevant cross-subject and course-frame reviews.

Grade 2 science has no base text and no source map. That is consistent with the recorded source policy. The grade 2 ELA frame does not yet exist.

### Checks

| Check | Observed result |
|---|---|
| `python -X utf8 scripts/plan.py check`, run first | Could not complete: `ModuleNotFoundError: No module named 'markdown'` |
| Direct frame checks: science grades 1, 2 and 3, and mathematics grade 2 | All returned **0 failures** |
| Science progression check | **198 rows, 0 failures**, with advisory notes |
| Independent grade 2 placement check | **12 owned skills, each placed exactly once; no foreign owned skills** |
| `python -X utf8 scripts/stale.py check` | **0 failures**, initially across 30 files and across 46 files on the final run |

The dependency error is an environment limitation, not a demonstrated plan defect. The complete plan gate remains unverified. No packages were installed.

No finding rests solely on model memory. Workload judgments are identified as professional judgments rather than classroom-tested results.

## Findings, most serious first

### F1. Habitat comparison is reduced to counting kinds

**Location:** Grade 2 frame, unit 7 and end-of-year check; `science.csv`, `s2-habitat-diversity`  
**LAYER:** standard  
**REPEAT:** yes, incomplete required performances recur in `progression-science-codex-2026-11-13.md`, F4  
**Severity:** serious  
**Confidence:** firm

**What is wrong.** The teaching and check emphasize how many kinds occur in each habitat. They do not require students to record and compare **which recognizable kinds** occur. Two habitats can have equal counts while supporting different plants and animals. The question also assumes the first survey will find more kinds in the garden.

The [2-LS4-1 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/2-LS4-1%20Evidence%20Statements%20June%202015%20asterisks.pdf) requires descriptions, records and comparisons of different types across habitats. The [elementary habitat reference](https://openscied.org/instructional-materials/2-3-habitats/) likewise compares the kinds present.

**Why it matters.** A writer can deliver the promised graphs without teaching the full comparison. Students may also learn an expected result instead of following their observations.

**Exact fix.**

Replace the unit question with:

> What kinds of plants and animals do we find in each place, and how are the places alike and different?

In the frame and progression note, require a picture inventory using sketches, photographs or agreed descriptive labels. Compare both the number of kinds and the kinds shared or different. Keep scientific names outside assessment.

Replace the final check’s count-only comparison with an unfamiliar pair of habitat inventories, including a case with equal counts but different kinds. Ask students to identify a similarity and a difference from the observations. Retain eight days.

### F2. Temperature-dependent classification is not secured

**Location:** Grade 2 frame, units 3 and 4; `science.csv`, `s2-material-properties`  
**LAYER:** standard  
**REPEAT:** yes, omitted core idea elements recur in `science-4-spine-2026-11-11.md`, finding 9  
**Severity:** serious  
**Confidence:** likely

**What is wrong.** Unit 3 sorts predominantly solid samples by properties at one condition. Unit 4 observes heating and cooling for reversibility, but does not explicitly return those observations to classification.

The [2-PS1-1 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/2-PS1-1%20Evidence%20Statements%20June%202015%20asterisks.pdf) includes observing a material under different temperature conditions and using its properties to classify it. The present frame does not assign that complete performance.

**Why it matters.** Students could treat a property as permanently attached to a material, despite later seeing that material melt.

**Exact fix.**

Add to unit 3 and `s2-material-properties`:

> Compare the same material under cooler and warmer conditions. Record its observable properties and classify each sample, including whether it is solid or liquid. Explain that a material’s observable properties can depend on temperature.

Use water and ice as the initial comparison. Unit 4 retrieves that record before investigating reversibility. Use qualitative temperature descriptions and adult-controlled preparation. Include a classification item using two conditions of one material. Retain the existing days and ownership.

### F3. Obtaining water information omits evaluating its sources

**Location:** Grade 2 frame, unit 1; `science.csv`, `s2-water-where`  
**LAYER:** standard  
**REPEAT:** yes, incomplete required performances recur in the earlier science progression reads  
**Severity:** moderate  
**Confidence:** likely

**What is wrong.** Recording facts from two supplied sources does not establish that students can identify a source likely to provide scientific information. That evaluation is explicitly included in the [2-ESS2-3 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/2-ESS2-3%20Evidence%20Statements%20June%202015%20asterisks.pdf).

**Why it matters.** Students can complete the chart by accepting everything supplied, leaving the evaluating part of the practice untaught.

**Exact fix.**

Add to unit 1 and the progression note:

> With teacher support, distinguish a source that can answer the scientific question from one that gives an opinion or invented account. Explain the choice using what the source shows and how its information was obtained.

Use a brief supplied-source comparison before the existing chart. Include one independently answered source-choice item in the unit assessment. No internet searching by students is required.

### F4. The unit-closing instruction does not secure transfer

**Location:** Grade 2 frame, “The storyline in every unit”  
**LAYER:** frame  
**REPEAT:** new  
**Severity:** moderate  
**Confidence:** likely

**What is wrong.** The frame directs every unit to close by explaining its anchor or presenting its tested design. It explicitly reserves unfamiliar situations for the two course-level checks, but gives no equivalent requirement for end-of-unit assessments.

The local science lens requires transfer at the end of a unit. The external [science evidence guide, indicator 1k](https://cdn.edreports.org/media/2025/07/Science-K-5-Evidence-Guide_2.0.pdf) also distinguishes uncertain assessment situations from repeated explanations.

**Why it matters.** A writer following this paragraph could assess a rehearsed class explanation and leave several months before discovering that students cannot apply it.

**Exact fix.**

Append:

> Students return to explain the anchor using their revised model or evidence. Each unit also includes an individual end-of-unit assessment on a phenomenon or design problem students have not studied. It requires a practice used with a core idea and a relevant crosscutting concept.

Count this within each unit’s existing allocation. Keep the unfamiliar course-level checks and both respond days.

### F5. The science frame still treats the mathematics frame as future work

**Location:** Grade 2 science frame, Cross-subject introduction, lines 151 to 152  
**LAYER:** process  
**REPEAT:** yes, stale planning-status notes recur in the earlier course-frame reviews  
**Severity:** minor  
**Confidence:** firm

**What is wrong.** “The math frame is written later” is obsolete. `docs/courses/math-grade-2/frame.md` exists and supplies the relevant sequence.

**Why it matters.** It leaves a completed prerequisite check looking deferred and conceals useful information already available.

**Exact rewritten note:**

> The grade 2 mathematics frame places picture and bar graphs in unit 1, approximately weeks 2 to 3, and ruler measurement in unit 3, approximately weeks 8 to 12. These precede the later science uses. Unit 2 retains its direct-comparison and teacher-supported ruler bridge wherever measurement begins earlier.

Replace “Taught by then in most orders” in the plant row with the verified mathematics unit reference.

### F6. The incoming science frame has the same obsolete deferral

**Location:** Grade 1 science frame, Cross-subject introduction, lines 145 to 146  
**LAYER:** process  
**REPEAT:** yes, the same stale-status pattern as F5 and the earlier frame reviews  
**Severity:** minor  
**Confidence:** firm

**What is wrong.** It says the other subjects’ frames will be written later, although grade 1 mathematics and social studies frames exist.

**Why it matters.** The incoming handoff sends a later worker back to a prerequisite review that can already be performed.

**Exact rewritten note:**

> Grade 1 mathematics and social studies frames exist. Use their unit sequences to verify these connections; retain the local bridges where science comes first. The grade 1 English language arts frame remains pending.

### F7. The mathematics frame has not reconciled its status and season claims with science

**Location:** Grade 2 mathematics frame, Cross-subject introduction and unit 3 reason  
**LAYER:** process  
**REPEAT:** yes, stale and inconsistent planning notes recur in the earlier frame reviews  
**Severity:** minor  
**Confidence:** firm

**What is wrong.** The cross-subject introduction treats the other frames as future work despite the existing science and social studies frames. Unit 3 also says science measures plants and seeds in fall, while science places those investigations in late winter and spring.

Its actual fallback table is sound: mathematics can measure classroom objects without waiting for science.

**Why it matters.** The contradictory reason can lead a writer to expect plant data before the science investigations occur.

**Exact rewritten notes:**

> Grade 2 science and social studies frames exist. Their sequences have been checked here. The grade 2 English language arts frame remains pending.

Replace the unit 3 fall claim with:

> This unit establishes ruler measurement before science’s later plant and seed investigations. Mathematics uses classroom objects and its own measurement data.

## Ownership, standards, reasons and days

The frame places all **12 owned skills exactly once**, covering **11 grade-specific expectations and K-2-ETS1-3**. Reviews of earlier-grade skills are identified as such. No unjustified claim of another grade’s owned skill was found.

| Unit | Days | Owned skills | Owned standards | Judgment |
|---|---:|---:|---|---|
| 1. Land and water | 10 | 2 | 2-ESS2-2; 2-ESS2-3 | Coherent opening; complete source evaluation through F3 |
| 2. Land changes | 16 | 3 | 2-ESS1-1; 2-ESS2-1; K-2-ETS1-3 | Largest allocation justified by evidence gathering, design tests and comparison |
| 3. Materials and uses | 12 | 2 | 2-PS1-1; 2-PS1-2 | Appropriate allocation; complete temperature-dependent classification through F2 |
| 4. Changes | 9 | 2 | 2-PS1-3; 2-PS1-4 | Parts-and-whole account followed by reversible and irreversible changes is defensible |
| 5. Plant needs | 9 | 1 | 2-LS2-1 | Sustained investigation justifies more time than the other single-skill units |
| 6. Seeds and pollinators | 6 | 1 | 2-LS2-2 | Shortest allocation is plausible for the model-building focus |
| 7. Habitats | 8 | 1 | 2-LS4-1 | Appropriate with F1’s fuller comparison |
| **Units** | **70** | **12** | | |
| Course-level checks and response | **6** | | Four check days and two respond days | Explicitly reserved |
| **Course total** | **76** | | | Agrees with `frames.csv` |

The year fits: 34 weeks with two lessons each provide 68 lessons; eight additional lessons provide 76. The stated duration gives approximately 44 to 51 hours annually. No unit is demonstrably far over or under its share at frame depth.

The ordering reasons hold: land representation precedes erosion design; material properties precede changes; plant investigation precedes dispersal models and habitat comparison. Stability and change is introduced before its erosion use. No necessary science model is used before it is available.

The [grade 2 standards](https://www.nextgenscience.org/sites/default/files/K-2Topic.pdf), PDF pages 11 to 14, support the claimed content boundaries. The frame avoids particles, quantitative map scaling, measured geological timescales and later-grade graph conventions.

## Seams and cross-subject timing

**Incoming science seam:** Grade 1 supplies source comparison, observable properties, design sketches, evidence-based accounts, parts and needs, and data records. The frame correctly distinguishes practice links from content prerequisites and retrieves kindergarten plant needs.

**Outgoing science seam:** Grade 3 explicitly picks up the design comparison, plant investigation, dispersal model, habitat comparison, land-and-water model and fast/slow changes. Later-grade matter handoffs agree with the progression. F1 strengthens the habitat handoff without changing its destination.

**Mathematics:** Graphs are taught in mathematics unit 1 before science needs them. Ruler measurement is taught in mathematics unit 3, with a viable bridge for earlier erosion measurements. Plant and seed measurement comes later.

**ELA:** The progression names the relevant reading, writing and research work, but the absent grade 2 frame prevents verification of exact timing. Science supplies read-alouds, shared charts, oral rehearsal and sentence frames, so these are workable local bridges.

**Social studies:** Grade 1 supplies landform words and map keys. Grade 2 social studies begins its world-features unit after its 16-lesson maps unit. Science’s opening unit can precede that use. Allocate two of science’s eight additional lessons within the first four weeks to make its stated completion date concrete.

## Lens checklist: course frame layer

| Lens line | Result |
|---|---|
| Every grade-owned performance expectation has a unit and is taught fully | **Missed in part:** placement is complete; F1 to F3 identify incomplete performance requirements |
| Grades 6 to 8 retain the base-text order or record a reason | **Not applicable:** grade 2 has no base text |
| High school expectations have explicit course ownership | **Not applicable** |
| Every unit names an anchor phenomenon or design problem | **Met:** all seven do |

At this layer, the frame also establishes three-dimensional work, model revision, engineering through tested designs, materials alternatives, safety planning and course-level response. Full element coverage, assessment quality, investigation safety and the preservation of practices in no-kit paths still require the later plans and materials. Those are not certified by this frame read.

## Settled by the expert

These choices retain the existing scope, standard ownership, unit order and total days.

| Choice | Reason | File it touches |
|---|---|---|
| Habitat records include picture inventories and comparisons of kinds, not counts alone | Completes the comparison without requiring scientific names | Grade 2 science frame; `science.csv`, `s2-habitat-diversity` |
| Use cooler and warmer conditions of one material, with qualitative temperature language | Secures temperature-dependent classification within grade limits | Grade 2 science frame; `science.csv`, `s2-material-properties` |
| Add a brief supported source-choice task before the water chart | Makes source evaluation observable | Grade 2 science frame; `science.csv`, `s2-water-where` |
| Include unfamiliar individual end-of-unit tasks within existing unit days | Separates rehearsed anchor explanation from transfer | Grade 2 science frame |
| Place two additional science lessons in the first four weeks | Makes the promised early social studies handoff feasible | Grade 2 science frame and later calendar |
| Explicitly identify relative comparisons and standard length measurement as scale, proportion and quantity | The activities already exist; this makes the band element traceable | Grade 2 science frame, practices and crosscutting concepts record |

The final choice follows [Appendix G’s K-2 elements](https://www.nextgenscience.org/sites/default/files/resource/files/Appendix%20G%20-%20Crosscutting%20Concepts%20FINAL%20edited%204.10.13.pdf). It adds no later-grade content.

## What is right and should be retained

- The seven-unit sequence and its prerequisite logic.
- Engineering within the erosion problem, followed by explicit review in materials.
- The plant investigation’s dated table and single-day comparison graph.
- Spoken and visual vocabulary, read-aloud access and supported writing.
- Materials alternatives with an honest statement that the no-kit path is weaker.
- Reserved checks and respond days, and the required science teacher’s safety read.

Earlier repairs to practice-link wording, the plant graph and long-range handoffs are present. They should not be reopened as unresolved findings.

## What I could not judge

- The full plan gate, because its dependency was unavailable.
- Exact ELA availability without the grade 2 ELA frame.
- Real classroom pacing, supply costs, safety implementation or assessment scoring reliability.
- Complete K-2 practice and crosscutting-concept element coverage without an explicit band coverage trace.
- Reference-curriculum minutes: public unit descriptions were accessible, but they do not establish equivalent 35 to 40 minute session counts.

## For Cory

- **Money:** Confirm or revise the proposed $50 annual classroom-material ceiling.
- **People:** Arrange the science teacher’s investigation safety read and the proposed disaster-sensitive review before release.
- **Audience:** Set the K-2 device assumption before presentation and tool requirements are fixed.

## Sources and source-list notes

The official evidence statements linked in F1 to F3 were read directly. Additional performance checks used the official statements for [material choice](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/2-PS1-2%20Evidence%20Statements%20June%202015%20asterisks.pdf), [reassembly](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/2-PS1-3%20Evidence%20Statements%20June%202015%20asterisks.pdf), [heating and cooling](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/2-PS1-4%20Evidence%20Statements%20June%202015%20asterisks.pdf), [plant investigations](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/2-LS2-1%20Evidence%20Statements%20June%202015%20asterisks.pdf), [dispersal models](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/2-LS2-2%20Evidence%20Statements%20June%202015%20asterisks.pdf), [fast and slow events](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/2-ESS1-1%20Evidence%20Statements%20June%202015%20asterisks.pdf), [erosion solutions](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/2-ESS2-1%20Evidence%20Statements%20June%202015%20asterisks.pdf), [land-and-water models](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/2-ESS2-2%20Evidence%20Statements%20June%202015%20asterisks.pdf), and [engineering design](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/K-5%20ETS%20Evidence%20Statements%20June%202015%20asterisks.pdf).

- [Appendix F](https://www.nextgenscience.org/sites/default/files/resource/files/Appendix%20F%20%20Science%20and%20Engineering%20Practices%20in%20the%20NGSS%20-%20FINAL%20060513.pdf): practice progression and quantitative comparison.
- [EQuIP science rubric](https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf): coherent three-dimensional learning and assessment.
- [Elementary land-change reference](https://openscied.org/instructional-materials/2-1-earth-land-change/), [materials reference](https://openscied.org/instructional-materials/2-2-matter/), and [plants reference](https://openscied.org/instructional-materials/2-4-puzzling-plants/): sequence and performance comparisons only, with no copied tasks or wording.

For the source list, the four elementary reference unit addresses above were reachable. Their public descriptions supported this read; no claim about their lesson-level materials or equivalent teaching minutes is made.

**Verdict: revise before detailed planning. Findings: 7. Intended report path: `docs/reviews/frame-science-grade-2-2026-11-14.md`, supplied here without creating the file.**
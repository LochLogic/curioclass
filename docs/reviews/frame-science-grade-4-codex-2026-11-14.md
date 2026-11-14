# Independent review: Science Grade 4 course frame

**Intended report path:** `docs/reviews/frame-science-grade-4-2026-11-14.md`  
**Delivery:** Complete report supplied here. No file was created, edited or deleted.

## Verdict

The frame has a defensible unit order, complete skill placement and a workable provisional year, but it needs revision before it becomes the writing contract. Its biggest risk is treating complete standard-code coverage as complete performance coverage: internal plant structures, parts of engineering design and the relationship between wave properties and object motion are insufficiently specified. Close those gaps within the existing units, reconcile the cross-subject calendar and correct the stale status notes.

**Finding count: 11, comprising five curriculum findings and six process findings.**

## What I read and checked

Read in full:

- `docs/agents/EXPERT.md`, `docs/agents/lenses/science.md` and `docs/RUBRIC-SCIENCE.md`.
- `docs/courses/science-grade-4/frame.md` and the corresponding `frames.csv` row.
- The grade 3 and grade 5 science frames.
- All 14 grade 4 science progression rows, with the adjacent-grade rows used to check their handoffs.
- The grade 4 mathematics and English language arts frames.

Also consulted:

- `FOUNDATION.md`, the required planning portion of `ROADMAP.md`, BASELINE rules 20 to 24, `APPROACH.md`, `GLOSSARY.md`, the science source entries in `APPROACH-SOURCES.md` and `BASE-TEXTS.md`.
- The relevant grade 4 social studies units and cross-subject calendar.
- Earlier science scope and sequence, progression, reconciliation and fix reports; the cross-progression reports; relevant earlier frame findings.
- The official grade 4 standards, selected evidence statements, progression appendices and review criteria linked below.

Science Grade 4 has **no base text**. Its absent `source-map.csv` is therefore not a defect. `APPROACH-SCIENCE.md` is also absent, as the rubric correctly records.

### Gates

| Command | Observed result |
|---|---|
| Required `python -X utf8 scripts/plan.py check`, attempted first | Could not complete: `ModuleNotFoundError: No module named 'markdown'` |
| Same gate using the existing bundled Python | Same missing dependency |
| `python -B -X utf8 scripts/frame.py check science-grade-4` | 0 failures |
| `python -B -X utf8 scripts/progression.py check science` | 198 rows, 0 failures; advisory notes |
| `python -B -X utf8 scripts/stale.py check`, final run | 56 files, 0 failures |

The full plan gate remains **unverified**, rather than passed. The direct frame and progression checks establish their implemented structural checks; they do not establish substantive completeness.

## Findings, most serious first

### 1. The plant argument still lacks a specified internal structure

**Severity:** Serious  
**LAYER:** standard  
**REPEAT:** yes, the earlier science scope and sequence review, finding 2, identified incomplete plant coverage  
**Confidence:** firm

**Location:** Grade 4 frame, unit 6; `s4-structures-function`; Course-level check 3.

**What is wrong:** The plant evidence names a cactus’s stem, spines and shallow roots, but specifies no internal plant structure or evidence of its function. The flower investigation remains a candidate. Check 3 asks about an unseen animal **or** plant, so its stated task can omit plants altogether.

**Why it matters:** A writer could implement every named example while leaving the plant side incomplete. The evidence statement requires internal and external plant and animal structures, their functions and their interaction within systems. [4-LS1-1 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/4-LS1-1%20Evidence%20Statements%20June%202015%20asterisks.pdf)

**Exact fix:** Keep the cactus anchor. Add a required macroscopic plant case showing internal water-carrying structures, using supplied photographs or an adult-prepared cut stem. Connect roots, internal transport and leaves as interacting parts. Make a flower or fruit case required for reproduction, and require separate plant and animal arguments in the unit assessment. Change Check 3’s wording to “one unseen animal and one unseen plant,” using short supplied evidence cards.

### 2. “3-5-ETS1-2 in full” omits research and peer exchange

**Severity:** Serious  
**LAYER:** standard  
**REPEAT:** yes, the earlier science review identified missing research before design and communication about proposals  
**Confidence:** firm

**Location:** Unit 3 and `s4-information-codes`.

**What is wrong:** Building two codes and comparing them against criteria is specified. Research before designing, sharing findings to develop possible solutions and testing under a range of likely conditions are not. The digital-information reading is presented after the design description rather than as knowledge students use to generate solutions.

**Why it matters:** The unit could become two code-making activities followed by preference judgments. The engineering evidence statement explicitly includes research, communication, testing and comparison using collected data. [3-5-ETS1-2 evidence statement, PDF page 5](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/K-5%20ETS%20Evidence%20Statements%20June%202015%20asterisks.pdf)

**Exact fix:** Add this requirement to the unit and progression row:

> Before designing, students investigate the communication problem and read how information is encoded and decoded. They generate at least two solutions, share proposals, test the same message under two relevant conditions, record accuracy and another agreed measure, and compare solutions using those data and the stated constraints.

Retain grade 5’s ownership of planning the full controlled-variable prototype test. This addition does not move that ownership.

### 3. Wave properties are named without requiring their relationship to object motion

**Severity:** Serious  
**LAYER:** standard  
**REPEAT:** yes, the earlier science review identified assessments that did not elicit the standard’s performance  
**Confidence:** firm

**Location:** Unit 3, `s4-wave-model`, and Course-level check 2.

**What is wrong:** Students describe amplitude and wavelength and observe a cork bobbing. The frame does not require them to compare waves and use their model to explain differences in the object’s motion. Check 2 merely reads amplitude and wavelength from a drawing.

**Why it matters:** Labelling a wave and knowing that it moves a cork can remain disconnected facts. The evidence statement requires relationships among wave properties and object motion, including a qualitative comparison when amplitude changes. [4-PS4-1 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/4-PS4-1%20Evidence%20Statements%20June%202015%20asterisks.pdf)

**Exact fix:** Require comparison of gentle repeating waves with different amplitudes, observation of the floating object and revision of a model explaining its motion. Compare wavelength qualitatively without equations. Replace Check 2’s wave clause with:

> Develop or revise a model of two unseen wave cases, showing amplitude, wavelength and the motion caused in a floating object; use supplied observations to explain a difference.

### 4. The mathematics calendar mistakes an early encounter for completed teaching

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, the cross-progression review identified same-year mathematics taught after science needs it  
**Confidence:** firm

**Location:** Cross-subject mathematics rows, especially line 146; For the lead, item 4.

**What is wrong:** Science says 4.OA.C.5 is taught in mathematics unit 1 and therefore needs no bridge. The current mathematics frame places its full teaching in **unit 7, school days 97 to 111**, after science’s codes unit at approximately **school days 60 to 79**. The mathematics frame itself supplies a bridge for science.

Other rows cite base-text unit numbers instead of the current Curio Class placements. The two proposed progression edits also remain unapplied.

**Why it matters:** Writers receive conflicting prerequisite instructions. The “not needed” statement can suppress the support the actual calendar requires.

**Exact fix:**

- Replace the pattern row’s availability entry with “Mathematics unit 7, approximately school days 97 to 111.”
- Make its bridge unconditional: science teaches and follows the code rule; explaining additional mathematical pattern features waits for mathematics.
- Record current mathematics placements for the other dependencies: 4.OA.A.3 in unit 8, 4.MD.A.1 in unit 6 and 4.G.A.1 in unit 9.
- Apply the frame’s existing proposed budget and ruler-measurement progression edits. Add the supported code-rule interpretation to `s4-information-codes`.

No science or mathematics standard needs to move.

### 5. The ice-map handoff is promised but not placed

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, earlier progression reads identified handoffs unsupported by the receiving or sending content  
**Confidence:** likely

**Location:** Grade 4’s handed-on seam for `s4-earth-feature-maps`; unit 5; grade 5’s picked-up seam and `s5-water-distribution`.

**What is wrong:** Grade 4 promises reading maps of oceans **and ice**, and grade 5 assumes that preparation. Unit 5 names topography, mountains, continental edges, volcanoes, earthquakes, ridges and trenches, but no ice-map work.

**Why it matters:** Grade 5’s stated readiness is stronger than the instruction actually specified.

**Exact fix:** Add a short, explicitly labelled review of `s2-water-where` in unit 5: read a map locating major ice-covered areas alongside oceans and land. Keep water quantities and distribution comparisons in grade 5. Add the review to the progression note so the handoff has a named instructional home.

### Stale-note findings

Each numbered row below is a separate finding.

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale status notes recur in earlier progression and frame reads  
**Confidence:** firm

| # | Location and what is wrong | Why it matters | Exact fix or replacement |
|---|---|---|---|
| **6** | Grade 4 science frame, lines 162 to 163 and For the lead item 2: ELA is still asked to plan the animal-structures bridge. The current ELA frame already does so in unit 2. | Presents a resolved dependency as unfinished coordination. | “ELA grade 4 unit 2, approximately school days 39 to 77, teaches the animal structures and functions needed by its texts. Science unit 6 remains later and develops the scientific argument in full. ELA uses an animal-threat text for its early problem-and-solution example.” Replace the suggestion to reconsider the order with this confirmed arrangement. |
| **7** | `RUBRIC-SCIENCE.md`, lines 54 to 55: the old grade 4 draft and middle school base text are called the only material. | Hides the progression and frame evidence now available. | “Science planning material includes the science progression, course frames, the grade 4 scope and sequence draft and the middle school base text. These are planning commitments, not evidence of a finished course.” |
| **8** | `RUBRIC-SCIENCE.md`, Gateway 2 connections row: “no plan names where the nature of science is taught.” | Keeps a closed placement gap open. Grade 4 explicitly places this work in units 4 and 6; adjacent frames also name placements. | “Course frames now name nature-of-science placements. Grade 4 places them in units 4 and 6. Unit plans must specify the tasks and evidence that enact those commitments.” |
| **9** | `progression-science-fixes-2026-11-13.md`, table rows Codex 1 and 2, still say the two owner moves are not done. Its own later note and the current CSV show both completed. | Leaves contradictory completion records in one report. | Replace both pending sentences with dated closure notes: “Completed afterwards by the caller: MS-PS4-2 is owned by s8-earth-sun-moon, with s6-light-paths contributing; MS-PS3-5 is owned by s6-particle-temperature, with s8-energy-transfer-argument contributing.” |
| **10** | The same fix report, Codex 8 table row and Skipped item, still says high school mathematics has no progression and science rows carry the old absence wording. | Sends reviewers back to a resolved prerequisite problem. The current mathematics progression has 82 high school rows, and the cross-fix report records the replacements. | “High school mathematics is now placed in math.csv. The cross-progression fix pass replaced the absence wording with owning skill ids and grades. Same-year availability still requires comparison of course frames.” |
| **11** | `progression-science-2026-11-13.md`, For Cory, still asks to confirm no grade 12 core course and says the rubric treats Physics as non-core. The current rubric records the settled three-course core allocation. | Leaves a settled scope decision looking open. | Add a dated closure: “Settled on q-hs-science-core: Biology, Chemistry and Physics are core, together carrying the high school Earth and space expectations. There is no grade 12 core science course. RUBRIC-SCIENCE.md reflects this decision.” Keep the original recommendation as historical context. |

## Ownership, standards, units and days

All **14 grade 4 progression skills are placed in exactly one owning unit**. Their **15 owned performance expectations** are present. Earlier-grade retrieval is named, and the contribution to grade 5’s engineering expectation is distinguished from ownership.

| Unit | Days | Owned skills | Owned standards | Substantive result |
|---|---:|---|---|---|
| 1 | 15 | speed-energy; collisions | 4-PS3-1, 4-PS3-3 | Adequate frame commitment |
| 2 | 26 | energy-transfer; energy-device; energy-resources | 4-PS3-2, 4-PS3-4, 4-ESS3-1 | Adequate frame commitment |
| 3 | 15 | wave-model; information-codes | 4-PS4-1, 4-PS4-3, 3-5-ETS1-2 | Findings 2 and 3 |
| 4 | 17 | weathering-erosion; rock-layers | 4-ESS2-1, 4-ESS1-1 | Adequate frame commitment |
| 5 | 17 | earth-feature-maps; hazard-solutions | 4-ESS2-2, 4-ESS3-2 | Standards placed; handoff correction in finding 5 |
| 6 | 21 | light-eye; senses-brain; structures-function | 4-PS4-2, 4-LS1-2, 4-LS1-1 | Finding 1 |

Skill names above retain their `s4-` prefix in the CSV. “Adequate frame commitment” does not certify unwritten lessons or assessments. The standard comparison used the [official grade 4 standards](https://www.nextgenscience.org/sites/default/files/4%20combined%20DCI%20standardsf.pdf), including their practices, core ideas and boundaries.

The unit reasons hold:

- Collisions establish energy-transfer arrows before circuits, devices and waves use them.
- Resources follow the device’s power-source question.
- Comparing codes prepares the later comparison of hazard solutions.
- Erosion prepares the canyon interpretation and flood tray.
- Light precedes sensory processing, which precedes the wider structure argument.

The **111 unit days plus nine course-level days equal 120 lessons**, or **90 hours at 45 minutes**. Four lessons a week for 30 active weeks accounts for them, with two additional weeks reserved for school events. No unit is clearly far above or below a defensible share at this layer. Keep the counts provisional while making the required performances explicit.

A shorter path still belongs in the scope and sequence. It must name actual cuts and trade-offs, as the [pacing guidance](https://cdn.edreports.org/media/2025/07/Science-K-5-Evidence-Guide_2.0.pdf) requests.

## Seams and cross-subject availability

The grade 3 handoffs are picked up: motion and force arrows, criteria and constraints, fossil evidence, weather-data representations and environmental effects. Dormant sunlight knowledge has a readiness check; older light, sound and mapping knowledge has retrieval.

Grade 5 receives the energy arrows, design comparison, erosion reasoning, ray model and resource-impact reasoning it names. Findings 1 and 5 strengthen its plant and water-map preparation.

The current partner frames establish these dispositions:

| Dependency | Disposition |
|---|---|
| Early informative writing and source notes | Science’s supplied writing and note frames remain necessary |
| Mathematical patterns | Bridge required, finding 4 |
| Geometry terminology | Ruler and informal-distance bridge remains necessary |
| Measurement conversions | Single-unit measurement avoids relying on unfinished conversion instruction |
| Maps and integrating two texts | ELA unit 2 precedes science unit 5 |
| Opinion writing and presentations | ELA placements precede science unit 6 |
| ELA animal defenses | Its own content bridge is already specified |
| Social studies resources and hazards | Science’s proposed completion points precede social studies units 6 and 7 |

The school-day equivalents are approximate planning windows. The scope and sequence must verify them against its actual calendar.

## Lens checklist: course frame layer

| Lens requirement | Result |
|---|---|
| Every performance expectation has a unit, and no unit claims one it only touches | **Missed:** codes are complete, but findings 1 to 3 prevent a full substantive finding |
| Grades 6 to 8 preserve the base order or record justified departures and losses | **Not applicable** |
| High school courses explicitly allocate band expectations | **Not applicable** |
| Every unit names an anchor phenomenon or design problem | **Met:** all six do |

The frame also commits to question boards, evidence-driven model revision, unseen transfer cases, low-cost alternatives, investigation safety and plain scientific facts. Those commitments require enactment at later layers. Their existence should not be confused with completed lesson evidence.

## What is right and should not be touched

Keep energy resources beside energy transfer and devices. Keep engineering inside science content, with distinct ownership across grades 3 to 5. Keep erosion before layers and hazards, the distinction between weathering and erosion, and the reuse of the erosion tray.

Keep the 21-day life-and-light unit, the learned-signal memory activity, unseen assessment situations and respond days. The corrections above do not require moving a standard or adding a unit.

The collision-first sequence has a directly relevant comparison in [the reference curriculum’s collision unit](https://openscied.org/instructional-materials/4-1-energy-transfer-collisions/). Another publisher groups resources, circuits, information transfer and waves within its [grade 4 energy module](https://www.foss-science.com/wp-content/uploads/2024/06/FOSS_Path_Energy_Gr4_Sampler_PreviewPages.pdf). These are comparisons, not instructions to copy either program.

## Settled by the expert

These are proposed item-level corrections for the caller to apply.

| Choice | Reason | File touched |
|---|---|---|
| Retain six units and 120 total days | No demonstrated need for a different course size or order | Grade 4 frame; `frames.csv` unchanged |
| Require an internal plant-structure case and separate plant and animal assessment evidence | Completes the already-owned standard | Grade 4 frame; science progression note |
| Make research, peer exchange and evidence-based code comparison explicit | Completes existing engineering ownership | Grade 4 frame; `s4-information-codes` |
| Compare wave amplitude and object motion qualitatively | Elicits modelling without quantitative wave equations | Grade 4 frame; `s4-wave-model` |
| Use the mathematics frame’s actual placements and make the code-rule bridge unconditional | Resolves the calendar contradiction | Grade 4 frame; relevant science progression cells |
| Add an ice-map retrieval task labelled grade 2 review | Makes the promised grade 5 handoff honest | Grade 4 frame; `s4-earth-feature-maps` |
| Keep the existing ELA animal-content bridge | It resolves the early ELA need without moving science ownership | Grade 4 science frame |

## For Cory

- **Audience and time:** Confirm the assumed four 45-minute science lessons a week, with a separately specified shorter route.
- **Money:** Confirm or replace the proposed materials target of about $30 per unit. This review did not price the supplies.
- **People:** Identify the science teacher required to read investigation safety and materials before the course is called finished.

No standard move is proposed.

## Sources and limits

Sources opened during this review:

- [Grade 4 standards](https://www.nextgenscience.org/sites/default/files/4%20combined%20DCI%20standardsf.pdf): complete expectation wording, dimensions and boundaries.
- [4-LS1-1 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/4-LS1-1%20Evidence%20Statements%20June%202015%20asterisks.pdf): plant and animal structures, systems and argument.
- [Engineering evidence statements](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/K-5%20ETS%20Evidence%20Statements%20June%202015%20asterisks.pdf): research, communication and comparison.
- [4-PS4-1 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/4-PS4-1%20Evidence%20Statements%20June%202015%20asterisks.pdf) and [4-PS4-3 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/4-PS4-3%20Evidence%20Statements%20June%202015%20asterisks.pdf): wave models and information-transfer performance.
- [Appendix E](https://www.nextgenscience.org/sites/default/files/resource/files/AppendixE-ProgressionswithinNGSS-061617.pdf), [Appendix F](https://www.nextgenscience.org/sites/default/files/resource/files/Appendix%20F%20%20Science%20and%20Engineering%20Practices%20in%20the%20NGSS%20-%20FINAL%20060513.pdf) and [Appendix G](https://www.nextgenscience.org/sites/default/files/resource/files/Appendix%20G%20-%20Crosscutting%20Concepts%20FINAL%20edited%204.10.13.pdf): selected progression and grade-band passages.
- [EQuIP science rubric](https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf): selected design, progression and assessment criteria.
- [Science K-5 evidence guide](https://cdn.edreports.org/media/2025/07/Science-K-5-Evidence-Guide_2.0.pdf): selected scope, practice and pacing criteria.
- [Framework report brief](https://nap.nationalacademies.org/resource/13165/reportbrief.html): integration and coherent development.
- The two curriculum comparisons linked above: unit summaries and the energy-module sampler, not complete teacher editions.

The previously cited [2019 planning guide](https://cloud.mysteryscience.com/image/upload/v1564615287/Mystery_Science_-_K-5_-_NGSS_Planning_Guide_kpdxol.pdf) could not be reached. No finding relies on it.

I could not judge actual teaching time, materials cost, final safety, model-revision quality or assessment scoring from a frame. The full plan gate also remains blocked. No substantive finding rests solely on remembered science; proposed examples and pacing judgments are professional judgments. Earlier-run memory was used only to orient the report format.

### For the source list

Add the grade 4 standards, individual evidence statements, science evidence guide and curriculum-comparison links above to `APPROACH-SOURCES.md`, with the limited reading scope recorded here. Its current entries already include the appendices and EQuIP rubric.

**Verdict: revise before use as the writing contract. Finding count: 11. Report supplied inline for `docs/reviews/frame-science-grade-4-2026-11-14.md`; the file was not written.**


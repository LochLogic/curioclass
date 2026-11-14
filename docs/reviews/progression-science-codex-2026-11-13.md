# Science progression: independent expert cold read

**Date:** 2026-11-13  
**Reviewer:** Codex, second independent reader  
**Intended report path:** `docs/reviews/progression-science-codex-2026-11-13.md`  
**Delivery:** Complete report below. No file was created or edited.

## Verdict

The progression has complete PE code coverage and a defensible three-course high school allocation, but it is not ready to become the fixed basis for course frames. Its greatest risk is confusing a contribution to a performance expectation with completion, which produces premature ownership, inaccurate source-order claims and missing demonstrations of proficiency. Correct the ownership representation and middle school completion points first, then close the model, prerequisite and cross-subject findings.

**Finding count: 9 consolidated findings.**

## What I read and checked

I read all **198 rows and every column** of `data/progressions/science.csv`, including their embedded notes. `science-excluded.csv` contains its header and **zero exclusions**. There was no separate science notes file beside these two files.

Supporting repository reading:

- `docs/agents/EXPERT.md`
- `docs/agents/lenses/science.md`
- `docs/RUBRIC-SCIENCE.md`
- `docs/FOUNDATION.md`
- `docs/ROADMAP.md`, the planning path through the gaps section
- `docs/agents/decisions/BASELINE.md`, including rules 20 to 24
- `docs/APPROACH.md`
- The science sources and access guidance in `docs/APPROACH-SOURCES.md`
- `docs/GLOSSARY.md`
- `docs/sources/BASE-TEXTS.md`
- The progression write/read briefs and relevant checker implementation
- `data/standards/ngss-pes.txt`, the mathematics standards text and ELA code inventory
- The nine social studies skills named by science cross-subject references

I compared the rows with all **208 PE statements**, their clarification statements and assessment boundaries in the [NGSS DCI arrangement](https://www.nextgenscience.org/sites/default/files/AllDCI.pdf). I also consulted Appendices E, F, G and K, the published middle school scope and sequence, and the cited ELA standards.

For all **18 middle school units**, I inspected the local teacher editions’ placement and prerequisite guidance. I inspected additional standards, mathematics and lesson-set passages where the CSV’s allocation needed checking. The PDFs were read directly from the local ZIP archives in memory, without extracting files. These are the actual stored editions, including updates dated 2025 and 2026.

I did **not** read `parts/`, earlier science course pages or earlier science course reviews. After forming the independent findings, I read `docs/reviews/progression-science-reconcile-2026-11-13.md`.

### Gate result

`python -X utf8 scripts/plan.py check` could not finish:

```text
ModuleNotFoundError: No module named 'markdown'
```

The authorized fallback, `python -X utf8 scripts/progression.py check science`, reported:

```text
progression science: 198 rows, 0 failure(s)
```

The fallback settles code coverage, valid references, ownership uniqueness by grade and the structural checks it implements. It also reported grade-skipping handoffs and model gaps. It does not establish substantive completion, correct prerequisite content or suitable mathematics timing.

### Coverage and distribution

| Grade | Skills | Distinct owning PEs | Physical | Life | Earth and space | Engineering |
|---|---:|---:|---:|---:|---:|---:|
| K | 11 | 11 | 4 | 1 | 5 | 1 |
| 1 | 10 | 10 | 3 | 3 | 2 | 2 |
| 2 | 12 | 12 | 4 | 3 | 4 | 1 |
| 3 | 15 | 16 | 3 | 8 | 3 | 1 |
| 4 | 14 | 15 | 5 | 2 | 5 | 2 |
| 5 | 14 | 14 | 6 | 2 | 5 | 1 |
| 6 | 14 | 14 | 4 | 1 | 8 | 1 |
| 7 | 18 | 19 | 4 | 8 | 4 | 2 |
| 8 | 26 | 26 | 9 | 12 | 3 | 2 |
| 9 | 24 | 30 | 0 | 20 | 1 | 3 |
| 10 | 20 | 21 | 11 | 0 | 8 | 1 |
| 11 | 20 | 20 | 10 | 0 | 8 | 2 |
| 12 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** | **198** | **208** | **62** | **60** | **56** | **20** |

The strand counts use the CSV’s classifications. An engineering-classified row can also own a science PE.

- **Standards not named:** none.
- **Skills with no standard:** none.
- **Standards assigned to multiple owning grades:** none.
- **Structurally premature prerequisite references:** none.
- **Grade 12:** intentionally absent under Cory’s stated decision, not a coverage defect.

## Findings

`REPEAT` compares finding types with the permitted reconcile report. It does not claim an exhaustive search of earlier reviews, which the blind-read instruction prohibited.

### F1. MS-PS4-2 is owned before it is completed, and its final light model is underspecified

**Severity:** High  
**LAYER:** progression  
**REPEAT:** yes, ownership before full completion is the same kind of issue discussed in reconcile difference 4  
**Confidence:** firm

**Skills:** `s6-light-paths`, `s8-wave-amplitude-energy`, `s8-earth-sun-moon`, `chem-earth-energy-climate`, `phys-wave-particle-light`.

`s6-light-paths` explicitly owns MS-PS4-2 “by exception” while acknowledging that substantial parts are completed in grade 8. The exception exists because the schema requires every row to name an owning standard. That requirement is forcing an inaccurate ownership claim.

There is also a substantive omission. The grade 8 notes add sound interactions, light crossing empty space and different bending of colors, but do not clearly require students to develop and use the **wave model of light** that explains brightness and color. `s8-earth-sun-moon` does not record `wave-model` in either model column.

The local 6.1 teacher edition, PDF pages 18 and 21, printed pages 10 and 13, explicitly defers that light model to 8.4. The 8.4 edition, PDF page 24, printed page 16, develops it through the light investigations. The [PE’s foundation elements](https://www.nextgenscience.org/pe/ms-ps4-2-waves-and-their-applications-technologies-information-transfer) distinguish these requirements.

**Why it matters:** A course writer can declare the expectation complete in grade 6, then build grade 8 without the model needed by later climate and physics work.

**Exact fix:**

1. Give MS-PS4-2 its completion owner in grade 8.
2. Preserve `s6-light-paths` as a contributing skill.
3. Add a grade 8 light skill, or expand the existing grade 8 row, to require students to develop, revise and use a qualitative light-wave model for brightness, color, material interactions and frequency-dependent bending.
4. Record `wave-model` in that grade 8 row’s `model_in` and `model_out`.
5. Change the schema/checker so a justified contributing row can identify its PE without falsely becoming its completion owner. For example, distinguish `standard` ownership from `contributes_to`.

A false grade 6 owner should not be retained merely to satisfy the current nonblank-standard rule. The ownership change goes to Cory.

### F2. Several middle school completion points conflict with the teacher editions

**Severity:** High  
**LAYER:** base text  
**REPEAT:** new  
**Confidence:** firm

**Skills:** `s7-reactions-atoms`, `s7-food-molecules`, `s6-particle-temperature`, `s8-energy-transfer-argument`, `s8-collision-forces`, `s8-forces-motion-mass`, `s8-kinetic-energy-graphs`.

The six-unit order is recognizable in each middle school grade. However, several notes delay foundational completion beyond the source unit that develops it.

| Current CSV claim | Teacher-edition evidence | Exact correction |
|---|---|---|
| `s7-food-molecules`, unit 7.3, completes MS-PS1-1 and MS-PS1-2 | The 7.3 edition, PDF page 22, printed page 14, says these are applied in a new context and should already have been developed in 7.1. PDF page 29 explains the required prior chemistry. | In `s7-reactions-atoms`, explicitly develop the molecular models and before/after property evidence needed before 7.2. Change `s7-food-molecules` from “completes” to “applies and extends.” |
| `s8-forces-motion-mass` completes MS-PS2-2 in 8.3 | The 8.1 edition, PDF page 23, printed page 15, locates the force, mass and motion investigations in 8.1. | Set its primary placement to 8.1 and describe 8.3 as reuse with non-contact forces. |
| `s8-kinetic-energy-graphs` completes MS-PS3-1 across 8.1 and 8.3 | The same 8.1 passage develops the quantitative mass and speed relationships before 8.2. | Require completion in 8.1, with subsequent application in 8.3. |
| MS-PS3-5 is only started in 6.2 and owned in grade 8 | The 6.2 edition, PDF page 23, printed page 15, identifies MS-PS3-5 without a partial-development asterisk. | Complete the particle-energy argument in grade 6. Keep the grade 8 argument as a later application. |

The published [middle school scope and sequence](https://www.openscied.org/wp-content/uploads/2024/02/OpenSciEd-Middle-School-Scope-Sequence.pdf) corroborates the main placements.

**Why it matters:** A writer following these notes can postpone force and energy relationships until after the sound work that uses them, or teach chemical-energy design before students can substantiate that a reaction occurred.

**Exact additional row edit:** Add MS-PS3-5 to `s6-particle-temperature.standard` and require an evidence-supported before/after energy argument there. Retain `s8-energy-transfer-argument` as a contributing revisit under the representation corrected in F1.

Moving a completion owner between grades goes to Cory. Correcting placements within the existing source-unit order is a source-fidelity correction.

### F3. Boundary statements do not consistently control the proposed work

**Severity:** High  
**LAYER:** standard  
**REPEAT:** yes, boundary precision recurs in reconcile differences 2 and 16  
**Confidence:** firm for the first two cases; likely for the third

**Skills:** `s4-information-codes`, `s4-wave-model`, `s7-food-molecules`, `chem-energy-accounting`.

Assessment boundaries constrain what is claimed as proficiency for a PE. They do not prohibit every discussion or extension beyond it. The problem here is that the rows do not consistently distinguish those roles.

| Skill | Problem | Exact row correction |
|---|---|---|
| `s4-information-codes` | It says sound **and light** signals are known as waves after `s4-wave-model`, despite that row’s explicit exclusion of electromagnetic waves. | Replace that sentence with: “Students use patterns in sound or flashes of light to send information. They do not need a wave model of light.” Retain the mechanical-wave model where useful. |
| `s7-food-molecules` | It proposes starch and sugar indicator tests as the evidence completing MS-PS1-2, although its own boundary lists a different, restricted set of properties. | Locate the required before/after comparison of permitted properties in 7.1. Label indicator evidence in 7.3 as application or extension, rather than the sole completion evidence for MS-PS1-2. |
| `chem-energy-accounting` | It describes “thermal and chemical” computational systems without distinguishing which calculations remain inside HS-PS3-1’s enumerated energy categories. | Specify a two- or three-component thermal system as the required proficiency case. Keep chemical-reaction accounting as an explicitly identified extension unless its representation is justified within an allowed category. |

Sources: [4-PS4-1](https://www.nextgenscience.org/pe/4-ps4-1-waves-and-their-applications-technologies-information-transfer), [MS-PS1-2](https://www.nextgenscience.org/pe/ms-ps1-2-matter-and-its-interactions), and [HS-PS3-1](https://www.nextgenscience.org/pe/hs-ps3-1-energy).

**Why it matters:** A teacher can follow the proposed activity faithfully and still collect evidence that does not establish the claimed PE.

I am **not** reopening the grade 4 passive-solar-heater choice solely because of the boundary wording. The clarification statement expressly includes that example, and reconcile difference 25 already recognizes the choice.

### F4. Some rows name the content without securing the whole required performance

**Severity:** High  
**LAYER:** progression  
**REPEAT:** yes, missing elements recur in reconcile differences 10, 13, 17 and 19  
**Confidence:** firm on the requirements; likely on the implementation risk

**Skills:** `s6-climate-circulation`, `s8-genes-proteins-traits`, `bio-respiration-energy`, `bio-biodiversity-math`, `bio-define-human-impact-problem`.

| Skill | What remains unsecured | Exact addition to `notes` |
|---|---|---|
| `s6-climate-circulation` | The row explains circulation but does not clearly require student model construction and use. It also omits salinity-driven density differences and the constraint imposed by continental outlines on ocean circulation. | “Students develop, revise and use a linked atmosphere-ocean model to explain a regional climate. Include density differences caused by temperature and salinity, heat redistribution, rotation and continental boundaries. Do not derive Coriolis dynamics.” |
| `s8-genes-proteins-traits` | Its notes can be implemented as explanation by the teacher. The student’s required development and use of a model is absent. | “Students develop and use a model connecting a changed gene on a chromosome to a possible protein change and then to harmful, beneficial or neutral effects on organism structure and function. Keep the model above specific molecular changes.” |
| `bio-respiration-energy` | HS-LS2-3 requires constructing **and revising** an evidence-based explanation. The row requires explanation but no revision. | “After an initial explanation, provide contrasting aerobic and anaerobic evidence. Students revise their explanation of matter cycling and energy flow and identify the evidence responsible.” |
| `bio-biodiversity-math` | The row does not explicitly secure ecosystems at different scales. | “Compare provided data at two clearly different ecosystem scales, then revise the explanation when a second data set changes or limits the first conclusion.” |
| `bio-define-human-impact-problem` | A “large human impact” illustrated by one dam or urban development does not necessarily establish the major global challenge required by HS-ETS1-1. | “Frame the work as a major global biodiversity challenge. Use a local dam, urban expansion or invasive species case to investigate it, and connect the qualitative and quantitative criteria to societal needs and wants.” |

Sources: [MS-ESS2-6](https://www.nextgenscience.org/pe/ms-ess2-6-earths-systems), [MS-LS3-1](https://www.nextgenscience.org/pe/ms-ls3-1-heredity-inheritance-and-variation-traits), [HS-LS2-3](https://www.nextgenscience.org/pe/hs-ls2-3-ecosystems-interactions-energy-and-dynamics), [HS-LS2-2](https://www.nextgenscience.org/pe/hs-ls2-2-ecosystems-interactions-energy-and-dynamics), and the engineering expectations in the [DCI arrangement](https://www.nextgenscience.org/sites/default/files/AllDCI.pdf).

**Why it matters:** These omissions can become days that teach the right facts while omitting the student action, scale or comparison that makes the expectation complete.

These are corrections inside the already claimed expectations, not proposals for new standards.

### F5. The model record contains real gaps and an incorrect reason for one of them

**Severity:** Medium to high  
**LAYER:** progression  
**REPEAT:** yes, model introduction and carry were addressed in reconcile difference 1  
**Confidence:** firm

**Skills:** all rows carrying the models below; specifically `s8-forces-motion-mass`, `s8-collision-forces`, `bio-ecosystem-stability-change`, `s5-plant-matter`, `s6-cells-body-systems`, `s8-earth-sun-moon`.

The gate correctly reports these **24 missing model-grade entries across 12 model names**:

| Model | Missing intervening grades |
|---|---|
| `earth-sun-moon` | 7, 9 |
| `field-model` | 9, 10 |
| `food-web` | 6, 8 |
| `force-diagram` | 6, 7, 9, 10 |
| `light-ray` | 7 |
| `matter-cycle` | 6, 8 |
| `plate-model` | 8 |
| `rock-cycle` | 8, 9 |
| `stability-change` | 5, 8 |
| `structure-function` | 5 |
| `water-cycle` | 8, 9 |
| `wave-model` | 5, 7, 9 |

The note in `bio-ecosystem-stability-change` says grade 8 has no standard whose crosscutting concept is stability and change. That is incorrect: MS-PS2-2 explicitly uses it. The local 8.1 teacher edition, PDF page 23, printed page 15, also develops it deliberately.

There is a second representation problem. `patterns`, `cause-effect`, `structure-function` and `stability-change` are crosscutting concepts, while a ray diagram or food web is a model representation. Treating them all as one kind of “model” obscures whether students are developing a reasoning lens or carrying a particular explanatory representation. [Appendix G](https://www.nextgenscience.org/sites/default/files/resource/files/Appendix%20G%20-%20Crosscutting%20Concepts%20FINAL%20edited%204.10.13.pdf) makes that distinction useful.

**Why it matters:** Some apparent gaps are missing metadata for work already present; others are genuine periods without retrieval. The current file treats both as justified simply because a grade lacks a matching topic expectation.

**Exact fix:**

- Add `stability-change` to `model_in` and `model_out` for `s8-forces-motion-mass`, with a note requiring explanation of unchanged versus changing motion.
- Remove the false grade 8 assertion from `bio-ecosystem-stability-change`.
- Record the actual structure-function reasoning in `s5-plant-matter`, linking roots and leaves to material uptake, rather than saying the reasoning disappears in grade 5.
- Make the grade 8 light-wave carry explicit as specified in F1.
- For every remaining gap in the table, identify a scheduled retrieval and reactivation task. Do not merely add a model label to an unrelated row.
- Distinguish crosscutting-concept development from representation continuity in the progression documentation or data structure.

Science does not require every topic to become new content every year. This read’s continuity requirement does require an explicit maintenance plan, which the file does not yet provide.

### F6. Long-range prerequisites are recorded, but next-grade pickup is incomplete

**Severity:** Medium  
**LAYER:** progression  
**REPEAT:** yes, prerequisite handoffs recur in reconcile differences 11, 14 and 22  
**Confidence:** firm on the gaps; judgment call on the best maintenance schedule

**Skills:** the endpoints of all `hands_on` edges whose target grade exceeds the source grade by more than one.

I checked all **264 reciprocal prerequisite edges**. Of these, **138 skip at least one grade**. None points backward from an assumed skill to a later teaching grade.

The following matrix identifies all 138 skipping edges by source and destination grade:

| Source grade | Destination grades and edge counts | Total |
|---|---|---:|
| K | 2: 3; 3: 5; 4: 1 | 9 |
| 1 | 3: 4; 4: 6; 5: 2 | 12 |
| 2 | 4: 6; 5: 5 | 11 |
| 3 | 5: 5; 6: 2; 8: 7 | 14 |
| 4 | 6: 11; 7: 1; 8: 3 | 15 |
| 5 | 7: 6; 8: 4 | 10 |
| 6 | 8: 4; 9: 1; 10: 8; 11: 9 | 22 |
| 7 | 9: 15; 10: 10 | 25 |
| 8 | 10: 2; 11: 17 | 19 |
| 9 | 11: 1 | 1 |
| **Total** | | **138** |

Examples with substantial student cost include:

- `s3-inherited-traits` to `s8-inheritance`
- `s3-magnet-static` to `s8-fields`
- `s6-geologic-time` to `phys-early-earth-history`
- `s6-digital-signals` to `phys-digital-information`
- `s7-ecosystem-matter-energy` to `bio-energy-pyramids`

Many are legitimate conceptual ancestors. A note explaining the standards’ spacing does not establish that students retained the prerequisite or that the next grade picked it up.

**Exact fix:**

1. Separate long-range ancestry from immediate maintenance handoffs.
2. Where an intervening row already carries the prerequisite, connect through it. For example, `s1-parts-mimic` can explicitly retrieve plant needs and hand that understanding to `s2-plant-needs-test`.
3. At each resumption after a gap, specify the prerequisite students must demonstrate, the readiness task and the short reactivation if it is missing.
4. Where the brief requires annual pickup but no existing row genuinely does it, schedule a maintenance entry. Do not manufacture a prerequisite by linking unrelated topics.
5. Recompute this matrix after F1 and F2, since those corrections change some endpoints.

[Appendix K](https://www.nextgenscience.org/sites/ngss/files/Appendix%20K_Revised%208.30.13.pdf) permits different course organizations and recognizes repeated development. It does not make a long gap evidence of retained proficiency.

### F7. Two physics rows point to the wrong ELA skill

**Severity:** Medium  
**LAYER:** standard  
**REPEAT:** new  
**Confidence:** firm

**Skills:** `phys-wave-particle-light`, `phys-em-radiation-effects`.

Both cite `ela:RI.11-12.8` for evaluating scientific claims. That standard concerns reasoning in seminal United States texts, including constitutional and legal reasoning. It is not the scientific-text evaluation skill described in these rows. See the [grade 11 to 12 informational-reading standard](https://www.thecorestandards.org/ELA-Literacy/RI/11-12/).

The matching scientific-literacy skill is RST.11-12.8. It is also identified in the [NGSS high school waves connections](https://www.nextgenscience.org/dci-arrangement/hs-ps4-waves-and-their-applications-technologies-information-transfer).

**Why it matters:** The references appear valid to the checker while pointing to a different kind of reading. This hides an unrecorded literacy prerequisite.

**Exact fix:**

- Replace the two references with `ela:RST.11-12.8`.
- First add the verified scientific-literacy code and text to the standards inventory, which currently excludes RST and WHST.
- Identify where that literacy skill is taught by or before grade 11.

Do not substitute another valid-looking ELA code solely because the appropriate code is absent.

### F8. Cross-subject references do not yet establish readiness for all required mathematics

**Severity:** Medium  
**LAYER:** progression  
**REPEAT:** new  
**Confidence:** firm on missing references and ownership evidence

**Skills:** particularly `s6-light-paths`, `s6-geologic-time`, `s7-food-molecules`, `s8-gravity-mass`, `s8-kinetic-energy-graphs`, `bio-population-carrying-capacity`, `bio-biodiversity-simulation`, and the other high school rows citing high school mathematics.

There are **170 cross-subject entries in 155 rows**. The nine social studies references exist and are owned at or before the science grade. I found no explicitly grade-numbered mathematics or ELA reference pointing to a later grade.

However:

- **43 rows have blank `cross_subject` cells.** Some blanks are reasonable for qualitative work, but others accompany data interpretation, quantitative models or technical reading.
- `s6-light-paths` has no mathematics reference. Its source’s measurement path uses powers of ten and reasoning about ranges and center.
- `s7-food-molecules` has no mathematics reference despite its data work. The 7.3 edition identifies graphing, rates and statistical summaries.
- `s6-geologic-time` names a social studies timeline skill but leaves the numerical scaling of a 4.6-billion-year timeline unsupported.
- The repository has no mathematics progression establishing owning grades for the high school mathematics codes cited by science. A high school code alone cannot demonstrate availability in Biology 9.

**Exact row corrections:**

| Skill | Required correction |
|---|---|
| `s6-light-paths` | If retaining light-sensor measurements, name `math:5.NBT.A.1` and the supported use of `math:6.SP.A.2`. State which work is guided before same-year statistics instruction. |
| `s7-food-molecules` | Name the graphing and rate skills actually retained from the source, such as `math:6.NS.C.8` and `math:6.RP.A.2`. Add statistical-summary references only if those tasks remain. |
| `s6-geologic-time` | Add the ratio/scale skill used to construct the timeline, with a provided-scale path until the mathematics is taught. |
| `s8-gravity-mass` | Name the table, graph and proportional-comparison skills required by the selected evidence task. |
| `s8-kinetic-energy-graphs` | Add proportional reasoning alongside graph interpretation; do not leave the mass relationship supported only by `8.F.B.5`. |
| High school mathematics-dependent rows | Record the mathematics course and availability point, or provide the necessary scaffold within science. This is especially important for function fitting and computational rules in grade 9. |

These are substantive readiness checks, not a request to fill every blank with a generic writing code. The source teacher editions repeatedly distinguish mathematics assumed beforehand from mathematics introduced with support.

### F9. Grade 8 and Biology carry substantially more completion work, without a load explanation

**Severity:** Medium, planning risk  
**LAYER:** progression  
**REPEAT:** new  
**Confidence:** judgment call

**Skills:** all grade 8 and grade 9 rows, particularly the clusters in units 8.5 and 8.6 and the combined-PE Biology rows.

Grade 8 owns **26 skills**, compared with **18** in grade 7 and **14** in grade 6. That is approximately 44 percent more than grade 7 and 86 percent more than grade 6. Biology has **24 skills owning 30 PEs**, compared with Chemistry’s **20 skills and 21 PEs**, and Physics’s **20 skills and 20 PEs**.

These counts do not prove an overloaded year. Some rows are short applications and others are substantial investigations. They do show that equal-looking rows conceal unequal work, especially where one Biology row combines several performances.

**Why it matters:** Course-frame writers can interpret every owning row as a comparable unit of new instruction and discover the imbalance only after planning the year.

**Exact fix:**

- Identify each middle school row as foundational development, completion or application, with its source-unit location.
- Explain the grade 8 concentration and distinguish already-developed components from new work.
- Expand the notes of combined-PE Biology rows to show the distinct student performances that must receive time.
- Require the course-frame pacing proof to preserve that distinction.

Do not move standards or add a grade 12 course merely to equalize row counts.

## High school allocation against Appendix K

The stated Biology 9, Chemistry 10 and Physics 11 path is a defensible use of Appendix K’s Modified Science Domains model. Appendix K presents models for local development, not a compulsory grade sequence.

All **19 high school Earth and space PEs** have owners:

| Course | Earth and space ownership | Count |
|---|---|---:|
| Biology 9 | HS-ESS2-7; HS-ESS3-3, HS-ESS3-4 | 3 |
| Chemistry 10 | HS-ESS2-2, HS-ESS2-4, HS-ESS2-5, HS-ESS2-6; HS-ESS3-1, HS-ESS3-2, HS-ESS3-5, HS-ESS3-6 | 8 |
| Physics 11 | HS-ESS1-1 through HS-ESS1-6; HS-ESS2-1, HS-ESS2-3 | 8 |

The notes identify and explain five departures from Appendix K’s main course placements:

- HS-PS2-6 in Chemistry
- HS-ESS2-2 in Chemistry
- HS-ESS3-1 in Chemistry
- HS-ESS1-5 in Physics
- HS-ESS1-6 in Physics

Their stated connections are coherent. I found no reason to reverse them. The unresolved concerns are readiness and workload, not the absence of a separate Earth and space course. Source: [Appendix K, Model 3 and Table 6](https://www.nextgenscience.org/sites/ngss/files/Appendix%20K_Revised%208.30.13.pdf).

## Progression lens checklist

| Lens check | Result | Evidence or limitation |
|---|---|---|
| A core idea is not owned by two grades at the same depth | **Met structurally; missed substantively** | Unique owning grades, but F1 and F2 confuse partial development and completion. |
| K to 2, grades 3 to 5 and middle school handoffs do not skip a band | **Met for coverage; missed for continuous pickup** | No entire band is omitted. F6 identifies long gaps within and across bands. |
| No grade assumes an unintroduced model | **Met structurally** | The checker finds introductions. F1 identifies an inadequately specified transition from rays to light waves. |
| Practices grow through the grades | **Met in broad outline; missed in specified rows** | Observation, fair testing, argument, revision and computation increase in sophistication. F4 identifies required performances that remain unsecured. |
| Crosscutting concepts are developed rather than merely named | **Missed** | F5 identifies missing carries, a false grade 8 assertion and conflation with model representations. |
| Middle school follows the base-text order without losing content | **Missed** | The 18-unit sequence is retained, but F2 identifies inaccurate completion placements. |
| High school band expectations have named course owners | **Met** | All 71 high school PEs have owners; all 19 Earth and space PEs are allocated. |
| Words precede dependent use at a suitable level | **Met provisionally at this layer** | No additional definite vocabulary prerequisite failure found. Grade 8 force vocabulary timing is addressed by F2. Actual reading demand needs student texts. |
| Mathematics and literacy are available when required | **Missed** | F7 and F8. |
| Anchors, lesson storylines, model-revision moments and transfer assessments work | **Not applicable to a full judgment here** | These require course frames, unit plans and assessments. Row descriptions alone cannot establish them. |
| Investigation safety, materials substitutions and costs are adequate | **Not applicable to final sign-off here** | Progression notes provide useful cautions. Full materials lists and investigation sheets are not under review. |

The practice and crosscutting-concept judgments use [Appendix F](https://www.nextgenscience.org/sites/default/files/resource/files/Appendix%20F%20%20Science%20and%20Engineering%20Practices%20in%20the%20NGSS%20-%20FINAL%20060513.pdf) and [Appendix G](https://www.nextgenscience.org/sites/default/files/resource/files/Appendix%20G%20-%20Crosscutting%20Concepts%20FINAL%20edited%204.10.13.pdf).

## Settled by the expert

These are recommendations for the caller to apply. Nothing was edited.

| Choice | Reason | File or rows touched |
|---|---|---|
| Keep the three-course high school allocation and its five explained departures | Complete allocation with coherent conceptual connections | Existing high school rows in `science.csv` |
| Keep the K to 2 and grades 3 to 5 engineering ownership ladder | It develops the band expectations without requiring duplicate completion ownership | Existing elementary engineering rows |
| Retain the grade 4 distinctions between weathering and erosion, qualitative speed and energy, and memory versus memory mechanism | These are accurate protections already strengthened by reconciliation | Existing grade 4 notes |
| Describe grade 4 light signals without requiring a light-wave model | Preserves information transfer at the intended level | `s4-information-codes.notes` |
| Require supplied seasonal averages in grade 3 unless calculation is separately taught | Reading typical-weather data need not become premature arithmetic-mean instruction | `s3-weather-data.notes` |
| Introduce grade 5 water shares as “out of 100,” with the grid and graph | Supports the science without silently requiring formal percentage procedures | `s5-water-distribution.notes` |
| Treat early technical vocabulary as explicitly taught oral and visual language | A scientific word need not be independently decodable when first introduced | K to 2 vocabulary guidance |
| Add the missing model, revision, scale and global-challenge requirements in F4 | These complete already claimed performances | The five F4 rows |
| Preserve long-range conceptual ancestry, but distinguish it from demonstrated readiness | Both are useful and answer different planning questions | Prerequisite documentation and schema |

## What is right and should not be undone

- Every PE is represented, with no unexplained exclusion.
- Elementary ownership generally follows the grade-specific expectations.
- The file regularly distinguishes matter cycling from energy flow.
- Most boundary notes are specific and useful.
- Evolution, climate change and Earth’s age are stated plainly.
- Models and practices generally become more demanding across bands.
- Sensitive family-trait activities and disaster examples receive thoughtful protections.
- The middle school source sequence remains recognizable, and the high school Earth and space allocation is complete.

## For Cory

- **Ownership and representation:** Approve the grade 8 completion owner for MS-PS4-2 and the grade 6 completion of MS-PS3-5, together with a representation that permits contributing skills without false ownership.
- **Continuity and time:** Decide where the maintenance work needed for the 138 long-range handoffs and remaining model gaps belongs in the course time budgets.
- **Cross-subject scope:** Assign ownership of scientific-literacy standards and establish when high school mathematics prerequisites become available.

There is no recommendation here for a new grade 12 core course, spending or outside contact.

## Limits of this read

This was a progression review. It did not establish the quality of unwritten student texts, investigation sheets, assessments, materials substitutions or actual teaching time.

The full plan gate remains unverified because its dependency was unavailable. The science progression fallback passed.

No finding rests solely on remembered source content. Proposed scheduling and instructional choices are identified as judgments. `REPEAT` classifications are limited to the permitted reconcile comparison.

## For the source list

Add two access notes for future read-only reviews:

- The actual local teacher editions contain revisions through 2026. Cite each inspected edition’s date rather than assuming every stored file is the original 2022 edition.
- When extraction is prohibited, the installed PDF library can read teacher-edition bytes directly from the ZIP archives in memory. The checked `pdftotext` executable does not accept PDF input from standard input.

**Verdict:** Revise before course-frame development. **Findings:** 9 consolidated findings. **Intended report path:** `docs/reviews/progression-science-codex-2026-11-13.md`, delivered here and not written to disk.
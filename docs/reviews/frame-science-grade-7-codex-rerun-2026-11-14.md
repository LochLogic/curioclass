# Independent expert read: science-grade-7 course frame

**Date:** 2026-11-14  
**Report path:** `docs/reviews/frame-science-grade-7-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files written or changed.

## Verdict

Revise before using this frame to write the scope and sequence. Its six-unit order, skill placement, anchors, and science handoffs are sound, but the base mapping does not secure the full resource standard, retained investigations need clearer safety commitments, and the added teaching does not have a credible unit-by-unit time budget. Keep the order and make those commitments explicit, correct the molecular descriptions, and update the stale notes.

## What I read and checked

- `docs/agents/EXPERT.md`, the science lens, `docs/RUBRIC-SCIENCE.md`, the foundation, shared approach, relevant roadmap sections, BASELINE rules 20 to 24, and science source decisions.
- The complete Grade 7 frame, its `frames.csv` row, all 18 Grade 7 science progression rows, and the Grade 6 and Grade 8 frames and relevant progression handoffs.
- Grade 7 math and ELA frames, relevant math progression entries, and earlier science progression and frame reviews, including the two existing Grade 7 reports.
- `docs/sources/BASE-TEXTS.md`, science entries in `docs/APPROACH-SOURCES.md`, all six locally stored Grade 7 base storylines, relevant stored unit-page text, and live primary sources linked below.
- `data/standards/ngss-pes.txt`, supplemented by official online standard text because the local inventory contains codes only.

`data/plans/science-grade-7/source-map.csv` does not exist. This is appropriate at the frame layer: `docs/pipeline/briefs/frame-write.md` explicitly places that day-level file at the scope-and-sequence stage. The frame’s prose source map is the applicable map here.

| Required check | Observed result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Initial invocation stopped because default Python lacks `markdown` |
| Same unchanged checker with existing dependencies available | Passed, exit 0, using `S:\AI\tts\.venv\Lib\site-packages`; bytecode writing disabled |
| `python -X utf8 scripts/frame.py check science-grade-7` | Zero failures; six units, 156 unit days, four course-level days |
| `python -X utf8 scripts/stale.py check` | 56 files, zero failures |

No packages were installed. No turn-management, synchronization, defect-ledger, or other writing commands were run.

## Findings, most serious first

### 1. Full resource coverage is declared without securing the necessary base extension

**Severity:** Serious  
**LAYER:** base text  
**REPEAT:** yes, unresolved finding 1 in the earlier Grade 7 expert report  
**Confidence:** firm

**Location:** Grade 7 frame, unit 6 and Source map.

**Problem and evidence:** Unit 6 owns MS-ESS3-1 and promises mineral, fossil-fuel, and groundwater distributions explained through geology. The base’s required storyline emphasizes changing water resources; its unit page separately identifies the lesson 10 fossil-fuel-distribution extension. Merely retaining lessons 1 to 18 does not explicitly retain that extension or identify the evidence used for the other resource categories. The official expectation requires mineral, energy, and groundwater resources. [Base unit 7.6](https://openscied.org/instructional-materials/7-6-earths-resources-human-impact/), [MS-ESS3-1](https://www.nextgenscience.org/pe/ms-ess3-1-earth-and-human-activity).

**Why it matters:** A writer can follow the stated base map and produce a strong climate unit while leaving the geological explanation of resource distribution incomplete.

**Exact fix:** Add to unit 6:

> Required coverage for MS-ESS3-1 includes the base lesson 10 fossil-fuel-distribution extension, followed by mineral-ore and groundwater cases using maps, geological evidence, and the Grade 6 plate and rock-cycle models. Students explain an unfamiliar resource distribution from that evidence.

Name these commitments in the source map and account for their minutes under finding 3. Replace the blanket no-loss conclusion with a statement that full coverage depends on these required adaptations.

### 2. Unit 1’s materials restriction conflicts with retained investigations and omits their specific controls

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, unresolved laboratory-safety finding in the earlier Grade 7 report  
**Confidence:** firm

**Location:** Grade 7 frame, unit 1 teacher notes.

**Problem and evidence:** The frame retains the entire base unit but says mixing uses citric acid and baking soda only. The retained storyline includes gas tests with flames, a hydrogen-peroxide reaction, heating water, and electrolysis. The frame names electrolysis as a demonstration, but does not explain whether the other investigations are retained, replaced, or teacher-only. General course-level mention of flame and heating does not settle those choices.

The local 7.1 storyline places flame testing in lessons 5, 6, and 9 and heating in lesson 9. Safety guidance requires protection appropriate to chemical, heat, and pressure hazards, including during demonstrations. [Base unit 7.1](https://openscied.org/instructional-materials/7-1-chemical-reactions-matter/), [NSTA eye-protection guidance](https://www.nsta.org/eye-protection-and-safer-practices-faq).

**Why it matters:** A writer cannot consistently follow both “whole unit retained” and the stated chemical restriction. Essential evidence could disappear, or hazardous work could be carried forward without its intended controls.

**Exact fix:** Replace the restriction with:

> Student mixing is limited to the named bath-bomb ingredients. Retained flame tests, heating, peroxide work, and electrolysis are teacher-only demonstrations under investigation-specific safety protocols. Each protocol names chemicals and concentrations, quantities, apparatus, gas and pressure controls, protective equipment, and observation arrangements. Where the setting cannot support a demonstration, use supplied observation and property data that preserve the comparison the lesson needs.

Record replacements in the source map. Keep the existing qualified science-teacher safety read as a finishing requirement.

### 3. The three-day allowance does not fund the additions where they occur

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, unresolved days-by-load finding  
**Confidence:** firm on the discrepancy; judgment call on the eventual additional days

**Location:** Course-in-brief Days paragraph and unit allocations.

The source totals match the local storylines. The available time beyond those totals is:

| Unit | Base days at 45 minutes | Frame days at 50 minutes | Difference in minutes |
|---|---:|---:|---:|
| 1 | 25 | 23 | +25 |
| 2 | 21 | 19 | +5 |
| 3 | 29 | 27 | +45 |
| 4 | 29 | 26 | −5 |
| 5 | 33 | 31 | +65 |
| 6 | 33 | 30 | +15 |
| **Total** | **170** | **156** | **+150** |

**Problem:** The 150-minute surplus equals one safety day and two full reteach lessons, before readiness checks, retrieval openings, reactivation tasks, or finding 1’s resource work. It is also distributed incorrectly: unit 1 has 25 spare minutes against its approximately 50-minute safety commitment, unit 4 already falls below base time, and unit 5 has 65 spare minutes against two possible 50-minute reteaches plus their checks.

**Why it matters:** Whole-year minute conversion hides local shortages. A writer will have to shorten investigations, omit promised support, or exceed the frame without a recorded decision.

**Exact fix:** Replace the assertion that the base time plus additions fits with a unit-by-unit budget naming:

1. Base activities merged or shortened, with the evidence preserved.
2. Minutes for safety, readiness checks, conditional reteaches, retrieval, and reactivation.
3. Required resource additions and assessment adaptations.
4. The resulting unit totals.

Preserve the four course-level check and respond days. If the complete budget exceeds 160 days, present the resulting calendar and named alternatives to Cory. The earlier report’s 164-day proposal is an estimate, not demonstrated sufficiency.

### 4. Molecular descriptions blur molecules, extended structures, and food-molecule organization

**Severity:** Moderate  
**LAYER:** progression  
**REPEAT:** yes, scientific-accuracy and representation precision; these particular instances are new  
**Confidence:** firm

**Location:** Grade 7 frame, units 1 and 3; `s7-reactions-atoms` and `s7-food-molecules` notes.

**Problem:** Unit 1 says substances are atoms joined into molecules while also introducing a salt crystal. The progression treats starch as an extended structure beside a salt crystal, and unit 3 groups starch, proteins, and fats together as large molecules with repeating subunits. These descriptions invite a writer to teach one structural model for materially different cases.

The standard distinguishes molecular solids from extended structures such as crystals. Dietary fats have a glycerol component joined to three fatty-acid components, rather than the chain organization used to explain starch and proteins. [Official physical-science standards, PDF page 3](https://www.nextgenscience.org/sites/default/files/MS%20PS%20DCI%20Combinedf.pdf), [Biology 2e, Lipids](https://openstax.org/books/biology-2e/pages/3-3-lipids).

**Why it matters:** These models support digestion, conservation, and later chemistry. Incorrect structural categories can propagate into diagrams and assessment keys.

**Exact fix:** Use these distinctions consistently:

> Substances consist of atoms. Some consist of discrete molecules; others form extended structures, such as a salt crystal.

> Food contains molecules of different sizes and arrangements. Starch and proteins have linked building units; fats have a different arrangement of components. These large molecules are contrasted with simple molecules and with extended crystal structures.

Keep salt as the extended-structure example. Remove starch from the list that equates extended structures with crystals. No standard ownership needs to move.

### 5. The earlier independent report still presents an active gate blocker

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

**Location:** `docs/reviews/frame-science-grade-7-codex-2026-11-14.md`, verdict and closing status.

**Problem:** It withholds the curriculum verdict because of a repository-wide gate failure. The unchanged checker now passes with existing dependencies available, and the current brief explicitly permits substantive review despite unrelated or unavailable gates.

**Why it matters:** A reader may treat the course as still awaiting its first independent substantive read.

**Exact fix:** Preserve the historical result and add:

> Superseded by the substantive independent read of 2026-11-14 supplied for `docs/reviews/frame-science-grade-7-2026-11-14.md`. The repository-wide checker passed in that read using the existing dependency directory; the earlier gate result remains a historical snapshot.

### 6. The earlier expert report says the Grade 7 ELA frame is unwritten

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

**Location:** `docs/reviews/frame-science-grade-7-2026-11-14.md:105`.

**Problem:** The ELA frame exists and supplies a calendar. Its research unit overlaps science unit 4, and its argument-writing and argument-evaluation instruction comes after some science uses.

**Why it matters:** The old status prevents the documented science bridges from being checked against actual availability.

**Exact fix:** Replace the sentence with:

> Grade 7 ELA is framed. Research is taught on days 61 to 86, argument writing on days 91 to 112, and argument evaluation on days 135 to 156. Science retains its local bridges wherever it uses these skills earlier.

### 7. The science rubric’s inventory omits the course frames now on file

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

**Location:** `docs/RUBRIC-SCIENCE.md:54-55`.

**Problem:** It identifies the Grade 4 draft and middle-school base text as the only material. The Grade 6, 7, and 8 course frames are present.

**Why it matters:** The inventory understates the planning evidence available to later reviewers.

**Exact fix:**

> Science planning includes the Grade 4 scope and sequence draft, course frames in `docs/courses/`, and the middle-school base text. These are planning materials, not evidence of a finished or classroom-tested course.

### 8. The science rubric says no plan locates nature-of-science teaching

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

**Location:** `docs/RUBRIC-SCIENCE.md:64`.

**Problem:** Grade 7 explicitly locates this work in units 1 and 6; neighboring frames also locate it.

**Why it matters:** A completed frame-level decision remains listed as absent.

**Exact fix:**

> Course frames locate nature-of-science teaching. Unit and section plans must identify the evidence, student task, and assessment that develop each claimed element.

### 9. Notes still say the MS-PS4-2 ownership move is unfinished

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, already identified by the Grade 6 and Grade 8 frame reads  
**Confidence:** firm

**Location:** `s6-light-paths` and `s8-wave-amplitude-energy` notes; `docs/reviews/progression-science-fixes-2026-11-13.md:25`.

**Problem:** Current standard cells make `s6-light-paths` a contributor and `s8-earth-sun-moon` the owner. Notes still describe the old owner or say the move awaits a contributing-row mechanism.

**Why it matters:** The prose contradicts the ownership data that the three frames use.

**Exact fix:** Replace the obsolete ownership wording with:

> MS-PS4-2 is owned by `s8-earth-sun-moon`. `s6-light-paths` contributes the earlier ray-model work; other named units apply or develop parts of the expectation.

In the fixes report, state that the move was subsequently completed, as its own Skipped section already records.

### 10. Notes still say the MS-PS3-5 ownership move is unfinished

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, already identified by the Grade 6 frame read  
**Confidence:** firm

**Location:** `s6-particle-temperature` notes; `docs/reviews/progression-science-fixes-2026-11-13.md:26`.

**Problem:** The notes say the code sits on the Grade 8 application or that its move to Grade 6 is not done. Current standard cells and appended notes already record Grade 6 ownership.

**Why it matters:** This obscures the distinction between prior proficiency, Grade 7 reuse, and Grade 8 application.

**Exact fix:**

> `s6-particle-temperature` owns MS-PS3-5. `s8-energy-transfer-argument` applies it to whole objects and is marked as a contributor.

Replace the fixes report’s unfinished-status sentence with a dated completion statement.

### 11. The progression fixes report still says no high-school math progression exists

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

**Location:** `docs/reviews/progression-science-fixes-2026-11-13.md`, Skipped, Codex 8.

**Problem:** `data/progressions/math.csv` now contains 28 Grade 9, 28 Grade 10, and 26 Grade 11 rows.

**Why it matters:** An obsolete prerequisite-status claim can perpetuate unnecessary scaffolds or postpone real sequencing checks.

**Exact fix:**

> High-school math progression rows now exist in `data/progressions/math.csv`. Check each science dependency against its actual course and unit availability; retain local scaffolds where science still comes first.

This correction does not establish that every high-school science dependency is already timed correctly.

## Coverage, order, source map, and seams

All **18 owned skills** appear exactly once in the Skills column. Their distribution is 1, 2, 3, 3, 5, and 4 rows across the six units. Their **19 owned codes** match the declared ownership.

| Unit | Owned standards checked | Frame-level conclusion |
|---|---|---|
| 1 | MS-PS1-2, MS-PS1-5 | Appropriate before/after-property and conservation work; resolve findings 2 and 4 |
| 2 | MS-PS1-6, MS-ETS1-4 | Design, testing, modification, and model-generated evidence are planned |
| 3 | MS-PS1-1, MS-LS1-3, MS-LS1-7 | Molecular modeling, interacting systems, and matter rearrangement are planned; correct finding 4 |
| 4 | MS-LS1-6, MS-PS1-3, MS-LS2-3 | Photosynthesis, synthetic-material information, system boundaries, matter cycling, and energy flow are planned |
| 5 | MS-LS2-1, MS-LS2-2, MS-LS2-4, MS-LS2-5, MS-ETS1-1 | Resource effects, interactions, evidence-based arguments, competing solutions, and precise design problems are planned |
| 6 | MS-ESS3-1, MS-ESS3-3, MS-ESS3-4, MS-ESS3-5 | Full resource coverage requires finding 1; monitoring and minimization must remain explicit in the local design task |

The life-science checks used the official [LS1](https://www.nextgenscience.org/dci-arrangement/ms-ls1-molecules-organisms-structures-and-processes) and [LS2](https://www.nextgenscience.org/dci-arrangement/ms-ls2-ecosystems-interactions-energy-and-dynamics) descriptions; engineering was checked against [ETS1](https://www.nextgenscience.org/dci-arrangement/ms-ets1-engineering-design). These are frame-level commitments, not certification of unwritten lesson and assessment items.

The unit order has defensible dependencies: reactions support the heater and metabolism; metabolism supports photosynthesis and matter cycling; ecosystems support the final human-impact work. Earlier-grade content is identified as review, reactivation, or a contribution to later ownership.

The source map assigns all **90 required Grade 7 base lessons** once, in order. Lessons 19 and 20 of 7.5 are explicitly excluded from required days as optional extensions, consistent with the local storyline. No NC or reference-only source is mapped. The unresolved issue is required extensions and adaptations inside mapped lessons, not missing base-unit ranges.

The incoming Grade 6 particle, energy, cell, water-cycle, and geological models are picked up. Grade 8 receives the named design, cell, growth, population, and body-system work. The Grade 7 frame’s proposed MS-LS1-5 start-note correction remains genuinely outstanding in the progression, so it is not a stale note.

### Cross-subject availability

| Dependency | Current comparison | Conclusion |
|---|---|---|
| Proportional tables | Math days 13 to 33; science unit 2 days 24 to 42 | Overlap exists. Retain the Grade 6 ratio-table bridge until math instruction is available |
| Percent change | Math days 47 to 68; science unit 6 days 129 to 158 | Available first |
| Argument writing | ELA days 91 to 112; science unit 3 days 43 to 69 | Science’s own modeled argument frame is necessary |
| Informative writing | ELA days 31 to 56; science unit 4 days 72 to 97 | Available first |
| Research | ELA days 61 to 86; science unit 4 days 72 to 97 | Retain the guided source-set bridge during overlap |
| Argument evaluation | ELA days 135 to 156; science unit 5 days 98 to 128 | Science must teach its local evaluation routine |
| ELA’s early ecosystem and climate contexts | Some precede completed science instruction | ELA supplies background and treats supplied climate facts as given where needed |

The earlier report overstates proportional reasoning as already taught before science unit 2. The current bridge prevents that overlap from becoming a new curricular finding.

## Science lens checklist

| Course-frame checklist line | Result |
|---|---|
| Every owned performance expectation has a unit, with full teaching secured | **Missed:** finding 1; other commitments are placed |
| Grades 6 to 8 preserve base order, record departures, and check losses | **Missed in part:** order and lesson ranges are preserved, but required adaptations and their time are not secured |
| High-school band expectations have explicit course ownership | **Not applicable** |
| Every unit names an anchor phenomenon or design problem | **Met** |

Supporting frame-level checks:

| Check | Result |
|---|---|
| Unit reasons and prerequisite order | Met |
| Initial, revised, and consensus models planned | Met |
| Evidence-based explanation and engineering planned | Met |
| Transfer assessment commitment | Met as a commitment; tasks remain to be written |
| Days fit promised work | Missed, finding 3 |
| Retained hazards and controls reconciled | Missed, finding 2 |
| Scientific representations accurate | Missed, finding 4 |
| Materials alternatives and no-kit paths named | Met at frame level |
| Cross-subject prerequisites | Met with the documented local bridges |
| Incoming and outgoing seams | Met, subject to the acknowledged MS-LS1-5 note repair |

## What is right and should not be touched

Keep the six anchors and base order, the single placement of each owned skill, explicit partial-standard handoffs, course checks followed by respond days, paper paths, no-account requirement, and sensitivity provisions.

Do not reopen the settled MS-PS1-1 and MS-PS1-2 ownership placements. Also, do not retain the earlier report’s boiling-point omission as proof of incomplete coverage: the official [MS-PS1-2 boundary](https://www.nextgenscience.org/pe/ms-ps1-2-matter-and-its-interactions) identifies permitted properties, not a requirement to assess every listed property.

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Keep the six-unit order | Dependencies and neighboring science seams support it | Grade 7 frame |
| Require the resource extension explicitly | A base lesson range does not reliably include an optional extension | Grade 7 frame, Source map |
| Distinguish molecules from extended crystal structures | Prevents incorrect molecular models | Grade 7 frame; science progression notes |
| Retain local literacy and ratio bridges | Current calendars show actual overlaps and later instruction | Grade 7 frame, Cross-subject |
| Preserve individual-organism growth alongside population numbers when expanding unit 5 | The progression and official clarification include both | Future unit 5 plan |
| Do not require `source-map.csv` at this layer | The frame-writing brief explicitly defers it | No file needed now |
| Reject boiling-point omission as a standalone coverage finding | An assessment boundary limits acceptable properties | Earlier Grade 7 report |
| Keep the proposed MS-LS1-5 start-note repair | The receiving Grade 8 row already expects that contribution | Science progression notes |

## Limits, sources, and memory

Actual 50-minute lesson timing, investigation protocols, assessment quality, and complete practice and crosscutting-concept element coverage cannot be certified from a frame. The [EQuIP rubric](https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf) was consulted for coherence, integrated performance, and assessment expectations, not used to assign an unwritten course a numerical score.

The full-unit teacher-edition PDFs inside ZIP files were not successfully extracted in this read. Findings rely on directly read storylines, unit-page material, official standards, and current repository evidence. No finding depends solely on the earlier report’s teacher-edition claims.

Prior memory informed review organization and prompts to inspect timing and representations. No curricular conclusion rests on unverified memory.

**For the source list:** Add the directly checked unit 7.6 extension entry, the NSTA eye-protection page, and the molecular-structure clarification sources above where absent. They identify practical checks for later unit writers.

## For Cory

- **Time and audience:** Decide any calendar change only after the complete 50-minute unit budgets are presented.
- **People and money:** Assign the already-required science safety, health, and Indonesia-context readers before the relevant finishing stages.
- **Scope:** Retain the existing decision request about year-course identifiers under the middle-school band label. This read proposes no movement of standard ownership.

**Verdict:** revise before scope-and-sequence writing. **Finding count:** 11, comprising four curricular findings and seven process findings. **Report path:** `docs/reviews/frame-science-grade-7-2026-11-14.md`, supplied here only.


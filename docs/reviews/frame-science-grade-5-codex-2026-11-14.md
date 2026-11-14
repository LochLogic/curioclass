# Expert cold read: science-grade-5 course frame

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/frame-science-grade-5-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files changed.

## Verdict

The six-unit structure, ownership and overall time budget are sound, but the frame needs revision before it guides unit writing. Its biggest risk is that apparently convincing investigations and summaries leave several claimed standards only partly supported, including a conservation experiment whose scale reading can contradict the intended conclusion. Correct the evidence and performance requirements inside the existing units, keeping their ownership and day totals.

## What I read and checked

- [Expert instructions](/S:/CurioClass/docs/agents/EXPERT.md), [science lens](/S:/CurioClass/docs/agents/lenses/science.md), [science rubric](/S:/CurioClass/docs/RUBRIC-SCIENCE.md), foundation, general approach, glossary, relevant roadmap and baseline passages, source register and base-text record.
- [Grade 5 frame](/S:/CurioClass/docs/courses/science-grade-5/frame.md) in full, its `frames.csv` row, and all 14 grade 5 science progression rows, including their prerequisite and destination references.
- Science grade 4 and grade 6 frames in full.
- Grade 5 math and ELA frames, including their availability calendars, and the relevant social studies grade 5 connections.
- Earlier science progression reviews and fixes, cross-subject review dispositions, the science grade 4 review, science source research, and earlier frame findings relevant to repeat classifications.
- Outside standards, evidence statements, review criteria and curriculum references linked below.

`docs/APPROACH-SCIENCE.md` does not exist. Grade 5 science has no base text, and no grade 5 science source-map file exists. That absence is appropriate under the base-text record.

### Gate results

| Check | Result |
|---|---|
| Requested `python -X utf8 scripts/plan.py check` | Initially stopped because the default Python lacks `markdown` |
| Full check using the dependency guard described below | Exit 0; 57 checking summaries; zero failures |
| Science progression | 198 rows; zero failures |
| Grade 5 science frame | Six units; 120 days; zero failures |
| `python -B -X utf8 scripts/stale.py check` | Final run: 56 files; zero failures |

The full check ran with an in-memory substitute for the unavailable rendering dependency. Any attempt to use that dependency would have raised an exception. No checking function changed, no rendering was requested, and no files were installed or written.

The zero from `stale.py` does not settle the unmarked status notes identified below.

## Findings, most serious first

### 1. The balloon experiment can produce the weight loss the frame incorrectly attributes to escaping gas

**Location:** Frame unit 1, line 124; `science.csv`, `s5-conserve-weight.notes`  
**Severity:** High  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** firm

**What is wrong:** The frame uses baking soda and vinegar beneath an expanding balloon as evidence that total measured weight stays unchanged, then attributes a loss to escaping gas. Expansion increases displaced air and can lower the scale reading even when the gas remains contained. A loose cap, the alternative mentioned in the safety instructions, also does not retain the whole system.

The [University of Maryland demonstration](https://lecdem.physics.umd.edu/f/f2/1704-f2-13.html) documents this exact apparatus falling from 261.7 to 258.4 grams as the balloon expands. The [grade 5 conservation evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/5th_Grade%20Evidence%20Statements%20June%202015%20asterisks.pdf), PDF page 2, requires measurements that support the conservation account.

**Why it matters:** A teacher could follow the frame correctly, obtain contrary data and teach students to explain away a real measurement with an incorrect cause.

**Exact fix:** Remove the expanding balloon from the quantitative conservation sequence. Retain closed-system melting, freezing and dissolving measurements; use a documented, tested constant-volume reaction data set for the chemical-change comparison. Keep balloon inflation as qualitative evidence of gas production. Replace the blanket explanation with:

> Compare the complete system before and after. Investigate apparent differences through escaping matter, spills, measurement uncertainty or changes in the apparatus; do not assume every lower reading means gas escaped.

Keep the prohibition on rigidly sealing a gas-producing reaction.

### 2. Unit 2 establishes that soil is not the chief source, but does not establish air’s contribution

**Location:** Frame unit 2, line 125; `s5-plant-matter.notes`; “How science works” bullet  
**Severity:** High  
**LAYER:** standard  
**REPEAT:** yes, incomplete claimed performances recur in the earlier science progression review  
**Confidence:** firm

**What is wrong:** Historical soil weights, hydroponic growth and the class’s weighed pots support the rejection of soil as the chief source. Together with “air is matter,” they still do not distinguish growth from water alone from growth using air and water.

The [5-LS1-1 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/5-LS1-1%20Evidence%20Statements%20June%202015%20asterisks.pdf) explicitly includes evidence concerning growth without air. The historical experiment itself concluded that the added material came from water alone, as shown in the reproduced account in [Analyzing van Helmont’s Willow Experiment](https://faculty.csbsju.edu/ssaupe/biol106/lectures/science_van_Helmont.pdf).

**Why it matters:** Students can repeat the correct conclusion without having evidence for its crucial air component. The history also risks becoming a story in which one measurement established more than it actually did.

**Exact fix:** Add a supplied, sourced comparison showing how otherwise comparable plants respond when carbon dioxide availability differs. Students must connect that evidence, water dependence, soil measurements and air’s material nature in their argument. Describe the historical result as evidence against soil supplying most of the added material, followed by a water-only interpretation that later evidence corrected.

Retain the classroom pots as supporting observations. Require comparable soil moisture conditions before interpreting their weight differences.

### 3. The ecosystem model omits required relationships and applications

**Location:** Frame unit 2, line 125; `s5-matter-movement.notes`  
**Severity:** Moderate  
**LAYER:** standard  
**REPEAT:** yes, incomplete standard elements were identified in the earlier science progression review  
**Confidence:** firm

**What is wrong:** Food webs, decomposition and matter cycling are present. The required account of organisms exchanging gases, water and waste with their environment is not explicit. Neither is using the model to explain how multiple species meet their needs or how an introduced species changes interactions.

These requirements appear in the [5-LS2-1 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/5-LS2-1%20Evidence%20Statements%20June%202015%20asterisks.pdf), particularly “Relationships” and “Connections,” and its [foundation elements](https://www.nextgenscience.org/topic-arrangement/5matter-and-energy-organisms-and-ecosystems).

**Why it matters:** A food-web drawing with decomposers can satisfy the present frame while leaving important parts of the claimed performance untaught.

**Exact fix:** Add these requirements to the unit and progression note:

> The model includes matter entering and leaving living organisms through air, water, food and waste. Students use it to explain how several species meet their needs, then revise an explanation when a new consumer without a predator is introduced in a supplied case.

Keep this qualitative and within the existing 24 days. No molecular explanation or live introduction of organisms is needed.

### 4. The water plan does not secure quantitative graphing of individual reservoirs

**Location:** Frame unit 5, line 128; `s5-water-distribution.notes`  
**Severity:** Moderate  
**LAYER:** standard  
**REPEAT:** yes, full-standard coverage gaps recur in earlier progression and frame reviews  
**Confidence:** firm

**What is wrong:** The frame specifies approximately 97 parts in the ocean and qualitative descriptions of the remaining reservoirs. It does not explicitly require students to graph supplied quantities for those reservoirs. A hundred-square overview cannot adequately distinguish the smallest stores.

The [5-ESS2-2 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/5-ESS2-2%20Evidence%20Statements%20June%202015%20asterisks.pdf) requires graphing given amounts across the named reservoirs. The [published performance expectation](https://www.nextgenscience.org/grade/5?page=2) also includes amounts and percentages.

**Why it matters:** Students could complete only a salt-water versus fresh-water display and never perform the reservoir comparison the standard claims.

**Exact fix:** Require a supplied data table and student-created graphs covering oceans, lakes, rivers, groundwater, glaciers and polar ice, with combined categories clearly identified where the source combines them. Supply quantities in common units and percentage shares already calculated. Use a separate freshwater display with an appropriate scale.

Preserve the previously settled “parts out of 100” explanation. Formal percentage calculation is unnecessary.

### 5. Unit 3 leaves the investigation practice partly unspecified

**Location:** Frame unit 3, line 126; `s5-new-substances.notes`  
**Severity:** Moderate  
**LAYER:** standard  
**REPEAT:** yes, naming a practice without securing its required performance recurs in earlier science reviews  
**Confidence:** firm

**What is wrong:** Students choose mixtures and evidence, but the frame does not require controlled comparisons, consideration of trial numbers or a recorded before-and-after property comparison. Those requirements are explicit in the [5-PS1-4 foundation elements](https://www.nextgenscience.org/topic-arrangement/5structure-and-properties-matter) and [evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/5-PS1-4%20Evidence%20Statements%20June%202015%20asterisks.pdf).

**Why it matters:** A writer could build a sequence of demonstrations that reaches the correct conclusions while missing the investigation performance. Unit 6’s later fair-test work cannot substitute for this unit’s claimed practice.

**Exact fix:** Add:

> Before testing, students record the starting materials’ relevant properties, the comparison being made, what stays constant, what will be measured and how many trials will be used. They record resulting properties and use the controlled comparisons to justify whether a new substance formed.

Retrieve the earlier-grade fair-test routine here. Use three trials for the selected comparison, within the existing 17 days.

### 6. The receiving course overstates the grade 5 sun-angle handoff

**Location:** Grade 6 frame, incoming seam and unit 3 justification; `s6-climate-circulation.notes`  
**Severity:** Minor  
**LAYER:** progression  
**REPEAT:** yes, prerequisite and handoff mismatches recur in the earlier science progression reviews  
**Confidence:** likely

**What is wrong:** Grade 6 describes sun angle as grade 5 knowledge. Grade 5 explicitly teaches shadow and daylight patterns, rotation and orbit, but does not develop the latitude-dependent sunlight model that grade 6 uses.

The grade 5 [space-system boundaries](https://www.nextgenscience.org/topic-arrangement/5space-systems-stars-and-solar-system) and the middle school [climate expectation](https://www.nextgenscience.org/pe/ms-ess2-6-earths-systems) support keeping these depths distinct.

**Why it matters:** The receiving writer may treat an important new explanatory model as retrieval.

**Exact fix:** Replace the receiving prerequisite with:

> Grade 5 supplies daily and seasonal shadow and daylight patterns, with rotation and orbit. Grade 6 develops the relationship between latitude, sunlight angle and uneven heating.

Apply this wording to the grade 6 seam, its retrieval description and `s6-climate-circulation.notes`. Grade 5 needs no added climate content.

### 7 to 12. Unmarked stale status notes remain

Each numbered row is a separate finding. All are **minor**, **LAYER process**, **REPEAT yes**, and **confidence firm**. Earlier progression and frame reviews already identified this kind of stale status wording.

| # | Location and problem | Why it matters | Exact replacement or disposition |
|---|---|---|---|
| **7** | [Science progression fix report, line 32](/S:/CurioClass/docs/reviews/progression-science-fixes-2026-11-13.md:32) says high school math is not placed in a Curio Class course. Current science rows contain named math owners and grades. | Misstates what the completed cross-subject repair achieved. | Replace that status sentence with: “Subsequently resolved by the cross-subject pass: science rows name their mathematics owners and grades in `Math readiness (math.csv)` notes; same-year ordering still requires the course calendars.” |
| **8** | [Same report, line 41](/S:/CurioClass/docs/reviews/progression-science-fixes-2026-11-13.md:41) says no high school math progression exists. `math.csv` now includes 82 rows in grades 9 to 11. | Sends later reviewers back to a completed placement task. | “Resolved: `data/progressions/math.csv` now places high school mathematics. Verify same-year availability against the course frames and retain necessary local scaffolds.” |
| **9** | [Science rubric, lines 54 to 55](/S:/CurioClass/docs/RUBRIC-SCIENCE.md:54) describes the grade 4 draft and middle school base as the only material. Science course frames and the progression now exist. | Hides the current planning layer from reviewers. | “No complete science course is built. Science progressions and course frames are now on file; the grade 4 scope and sequence remains a draft, and middle school has its recorded base text. These are planning materials, not completed courses.” |
| **10** | [Science source review](/S:/CurioClass/docs/reviews/science-open-material-2026-11-12.md:121) still leaves opening a middle school teacher guide as an open task; its package-format uncertainty also remains unqualified. | Repeats completed acquisition and inspection work. | Preserve the dated account and add: “Resolved 2026-11-13: all 18 standard unit packages were obtained and teacher editions inspected. The source catalog records package contents, licence evidence and third-party exclusions.” Mark that open item resolved. |
| **11** | [Source catalog analysis, line 13](/S:/CurioClass-sources/_catalog/analysis-science-ela-ss.md:13) says `docs/sources/BASE-TEXTS.md` does not exist. It exists and records the operative decisions. | Makes the source record appear absent. | “Resolved: `docs/sources/BASE-TEXTS.md` exists and records the base-text and reference decisions.” |
| **12** | [Source catalog analysis, lines 9 to 12](/S:/CurioClass-sources/_catalog/analysis-science-ela-ss.md:9) presents redrawing middle school around the 18-unit base order as a future scope decision. The three middle school frames now implement that order. | Leaves an answered structural question looking open. | “Resolved: the grade 6, 7 and 8 frames adopt the 18-unit base order. `data/sequence.csv` describes the legacy arrangement; use the current frames for course planning.” |

The appended completion section in the middle school source folder’s `NOTES.md` already records the full downloads. I do not count its earlier acquisition account as another unresolved finding.

## Coverage, units and days

The structural gate correctly settles placement: **14 owned skills, each in exactly one unit**, with no unexplained ownership imported from another grade.

| Unit | Owned skills | Days | Substantive result |
|---|---|---:|---|
| 1 | `s5-particles`; `s5-conserve-weight` | 17 | Particle-model scope is appropriate. Conservation needs finding 1. |
| 2 | `s5-plant-matter`; `s5-matter-movement`; `s5-food-energy-sun` | 24 | Plant argument and ecosystem performance need findings 2 and 3. Sun-to-food energy account is appropriately planned. |
| 3 | `s5-identify-materials`; `s5-new-substances` | 17 | Material identification is appropriately planned. Mixing investigation needs finding 5. |
| 4 | `s5-gravity-down`; `s5-shadows-sky`; `s5-star-brightness` | 20 | All three performances are represented at frame level. |
| 5 | `s5-sphere-interactions`; `s5-water-distribution` | 15 | Two-system modeling is appropriately planned. Reservoir graphing needs finding 4. |
| 6 | `s5-protect-resources`; `s5-design-test` | 18 | Resource-information work and controlled prototype testing are appropriately planned. |

The allocation is defensible: unit 2 carries three linked expectations and sustained observations; unit 4 carries three expectations and dormant-knowledge recovery; unit 6 needs repeated testing and revision. No unit is demonstrably far over or under its share.

The total is **111 unit days plus six course-check days and three respond days**, or **120 lessons and 5,400 minutes**. Four 45-minute lessons weekly require 30 science weeks, leaving the stated two weeks for interruptions. The scope and sequence should distinguish elapsed investigation time from lesson time and explicitly include unit assessments within unit allocations.

The unit reasons generally hold. Particles precede their applications; properties precede mixing investigations; ecosystem matter precedes food-energy tracing; Earth-system and water work precedes the design problem. The particular placement of living matter before mystery materials is a defensible choice, not a necessary prerequisite.

## Seams and cross-subject checks

The grade 4 handoffs in energy transfer, light, plant structures, maps, resources and design are picked up. Earlier-grade gaps have named retrieval or readiness responses. Finding 6 is the specific outgoing mismatch.

The same-year bridges are credible when checked beside the current frames:

| Dependency | Availability and judgment |
|---|---|
| Measurement conversion | Math unit 8, approximately school days 110 to 118, follows early science weighing. Keeping measurements in one unit resolves the dependency. |
| Powers of ten | Also math unit 8, after science unit 4’s approximate school days 83 to 108. Supplied numerals and relative-distance comparisons suffice. |
| Coordinate graphing | Math unit 10, approximately days 135 to 149, follows the shadow unit. Tables and bar graphs are valid here. |
| Fractional line plots | Math unit 9, approximately days 119 to 134, overlaps the approach to science unit 6. Retrieve grade 4 line plots explicitly if needed. |
| Source location and research | ELA unit 2, approximately days 42 to 79, follows some early science uses. Science’s supplied sources and organizers must include teacher modeling before independent work. |
| Integrated sources, opinion and presentations | ELA unit 3, approximately days 83 to 121, follows science unit 2. The science frame’s class-built charts and argument supports remain necessary. |
| Rainforest and water connections | Science ecosystems overlap ELA unit 2; science water and protection overlap ELA unit 4, approximately days 122 to 156. Both ELA units provide their own needed background. |

The `4n/3` conversion is an approximate calendar across the stated interruptions, not a precise weekly schedule. Actual science weekdays and interruption dates belong in the scope and sequence.

## Science lens checklist: course-frame layer

| Checklist line | Mark | Evidence |
|---|---|---|
| Every owned performance expectation has a unit and is represented in full | **Missed substantively** | Placement passes; findings 1 to 5 identify evidence or performance gaps. |
| Grades 6 to 8 preserve base order and record losses | **Not applicable** | This is an original grade 5 course. |
| High school band expectations have named course owners | **Not applicable** | Elementary course. |
| Every unit names an anchor phenomenon or design problem | **Met** | All six units do. Sustained storyline quality requires the unit plans. |

Three-dimensional work, model revision, transfer assessments, materials alternatives and safety are promised at an appropriate planning level. This frame cannot establish their execution.

## Settled by the expert

These choices fit existing ownership and day totals. The caller can apply them without moving a standard.

| Choice | Reason | File or rows affected |
|---|---|---|
| Keep six units and 120 lessons | The overall load and order are defensible | Grade 5 frame; `frames.csv` |
| Use the balloon qualitatively, with reliable separate conservation evidence | Avoids misleading scale data | Unit 1; `s5-conserve-weight` |
| Distinguish “not chiefly soil” evidence from evidence for air’s contribution | Makes the plant argument valid | Unit 2; `s5-plant-matter` |
| Add the supplied introduced-consumer case and environmental exchanges | Completes the ecosystem performance | Unit 2; `s5-matter-movement` |
| Graph supplied reservoir quantities and supplied shares | Completes the standard without premature percentage calculation | Unit 5; `s5-water-distribution` |
| Use three trials for unit 3’s selected controlled comparison | Makes the investigation requirement concrete | Unit 3; `s5-new-substances` |
| Retrieve grade 4 fractional line plots when needed | Preserves useful prior learning before grade 5 math completes it | Unit 6 cross-subject bridge |
| Correct the receiving sun-angle description | Keeps new middle school learning distinct from retrieval | Grade 6 frame; `s6-climate-circulation` |

## What is right and should remain

- Unique ownership and the elementary engineering progression.
- Matter cycling distinguished from energy flow.
- The early particle-model introduction and later applications.
- Background shadow observations begun before the sky unit.
- Explicit grade boundaries, especially no molecular chemistry, gravity calculations or explanation of seasonal causes.
- Original elementary investigations, reference-only source restrictions, materials alternatives and unseen assessment contexts.

## Sources and limits

The findings link the standards and evidence statements used for their specific judgments. Additional references consulted were:

- [Science K-5 review criteria v2.0](https://cozy-dream-721ab6aab0.media.strapiapp.com/Science_20_K_5_20_Review_20_Criteria_2_0_ddd732f02c.pdf): selected criteria on full scope, accuracy, coherence and year feasibility.
- [EQuIP science rubric 3.0](https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf): three-dimensional performance, evidence, coherence and assessment.
- [OpenSciEd elementary scope and sequence](https://embed-rech-01.dialog.cm/openscied/docs/elementary_scope_sequence_final_2026): overview and progression guidance as reference, without importing its tasks or wording.
- [The Inquiry Project grade 5 overview](https://inquiryproject.terc.edu/curriculum/curriculum5/index.html): comparison of observable matter investigations and particle representations. Its additional content was not treated as a requirement for this course.

I could not judge unwritten assessments, actual classroom minutes, final investigation reliability, full practice and crosscutting-element coverage, or completed safety controls. The water-agency page timed out, so no new numerical reservoir table is supplied. A historical article was available through search excerpts, but the historical judgment above also uses the accessible university reproduction.

No educational finding rests solely on memory. Prior memory informed report organization and scope discipline only.

**For the source list:** Add the University of Maryland balloon demonstration, the accessible van Helmont reproduction and The Inquiry Project overview if absent. Record the current linked K-5 review-criteria address.

## For Cory

- **Audience and scope:** Confirm the assumed weekly science time and whether a separate spring review of the whole grades 3 to 5 band is wanted.
- **Money:** Set the materials-cost target already raised by the frame.
- **People:** Assign the required science teacher’s safety and materials read before calling the course finished.

**Verdict:** Revise before unit writing. **Finding count:** 12, comprising six content or handoff findings and six process findings. **Report path:** `docs/reviews/frame-science-grade-5-2026-11-14.md`, delivered here, not written.


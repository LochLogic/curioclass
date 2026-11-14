# Independent review: Science Grade 3 course frame

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/frame-science-grade-3-2026-11-14.md`  
**Delivery:** Complete report supplied here. No file was created or edited.

## Verdict

The frame has coherent unit ordering, complete structural skill placement and a plausible 120-lesson main path, but needs revision before the scope and sequence is written. Its greatest risk is that writers will turn inaccurate examples and incomplete planning commitments into lessons while trusting the claim that every standard is covered fully. Correct the habitat example, make the remaining standards commitments explicit, and reconcile investigation timing and cross-subject calendars while preserving the six-unit order.

## What I read and checked

- `docs/agents/EXPERT.md`, the science lens, `docs/RUBRIC-SCIENCE.md`, `docs/FOUNDATION.md`, the relevant ROADMAP planning sections, BASELINE rules 20 to 24, and `docs/GLOSSARY.md`.
- `docs/APPROACH.md`, the science sources and evidence notes in `docs/APPROACH-SOURCES.md`, and `docs/sources/BASE-TEXTS.md`. `docs/APPROACH-SCIENCE.md` is absent.
- The complete target frame, its `frames.csv` entry, all 15 grade 3 science progression rows, their prerequisite and handoff references, and the neighboring grade 2 and grade 4 frames.
- The grade 3 mathematics, ELA and social studies frame provisions relevant to science prerequisites.
- Earlier grade 3 science reports, neighboring science reviews, progression findings and the K to 2 fixes report, to distinguish unresolved findings from completed repairs.
- Official grade 3 standards, engineering evidence statements, relevant external review criteria, and the outside sources linked below.

The local science standards file contains codes, rather than the full expectations and foundation boxes. Outside standards wording was checked directly. No substantive finding below rests solely on memory. Pacing estimates and proposed classroom arrangements are professional judgments.

### Gates

`plan.py check` stopped with `ModuleNotFoundError: No module named 'markdown'`; the review continued using the required structural fallback.

| Command | Result |
|---|---|
| `python -X utf8 scripts/frame.py check science-grade-3` | Passed: 0 failures, 6 units, 120 days, including 111 unit days and 9 course-level days |
| `python -X utf8 scripts/stale.py check` | Passed: 56 files, 0 failures |

No turn-management, build, defect-ledger or other writing command was run.

## Coverage, order and days

An independent read-only comparison found **15 owned skills placed exactly once**, no missing skills, no duplicate placements and no foreign-grade skill IDs in the ownership column.

| Unit | Days | Skills | Claimed expectations | Judgment |
|---|---:|---:|---|---|
| 1. Forces and motion | 16 | 2 | 3-PS2-1, 3-PS2-2 | Adequate frame commitments |
| 2. Non-contact forces and design | 17 | 2 | 3-PS2-3, 3-PS2-4, 3-5-ETS1-1 | Coverage qualifications in finding 2 |
| 3. Life cycles and traits | 22 | 3 | 3-LS1-1, 3-LS3-1, 3-LS3-2 | Adequate scope; observation schedule unresolved |
| 4. Survival | 20 | 3 | 3-LS2-1, 3-LS4-2, 3-LS4-3 | Accuracy and evidence qualifications in findings 1 and 2 |
| 5. Environmental change | 16 | 2 | 3-LS4-1, 3-LS4-4 | Coverage qualification in finding 2 |
| 6. Weather, climate and hazards | 20 | 3 | 3-ESS2-1, 3-ESS2-2, 3-ESS3-1 | Adequate scope; access and anchor qualifications |
| Course checks and respond days | 9 | | | Six check days and three respond days |

These judgments concern teaching commitments in a frame, not demonstrated completion in lessons. The [official grade 3 standards](https://www.nextgenscience.org/sites/default/files/3%20combined%20DCI%20standards%206.13.13.pdf) were used to check the expectations and boundaries.

The unit allocations range from about 6.7 to 8 days per skill. That is a reasonable first allocation: unit 3 needs longitudinal observations, unit 4 needs several evidence-based explanations, and unit 2 combines investigations with problem definition. No unit is demonstrably far over or under its share.

The ordering has defensible dependencies: force arrows precede non-contact forces, traits precede variation, habitat systems precede environmental change, and design criteria precede judgments about solutions. All prerequisite and handoff identifiers in the grade 3 progression rows appear in the frame’s seam tables.

**Source map:** Not applicable. The source record confirms that elementary science has no base text, and no grade 3 source-map file exists. Its absence is appropriate.

## Findings, most serious first

### 1. The Arctic anchor teaches a false exclusion

**Severity:** High  
**LAYER:** frame  
**REPEAT:** yes, earlier grade 3 review, finding 1  
**Confidence:** firm

**Location:** Target frame, unit 4, line 118; progression row `s3-habitat-survival`.

**Problem and consequence:** The anchor says no frog could live in Arctic tundra, while the teaching examples contrast a polar bear with an unspecified frog in the Arctic. Wood frogs occur above the Arctic Circle, and the museum account specifically describes their Alaskan tundra range. The generic contrast teaches that membership in a broad animal group determines survival, instead of examining particular organisms, conditions and characteristics. [Alaska species account](https://www.adfg.alaska.gov/static/species/speciesinfo/_aknhp/Wood_Frog.pdf), [museum account](https://www.amnh.org/exhibitions/frogs-a-chorus-of-colors/frogs-and-the-ecosystem/frog-antifreeze).

**Exact fix:** Replace the anchor’s final clause with:

> Different organisms survive the tundra’s conditions in different ways; which characteristics and needs explain the differences?

Replace the generic frog comparison in both files with named organisms and documented habitat conditions. Include the wood frog as a counterexample to the original claim. Provide evidence for all three outcomes required by 3-LS4-3: surviving well, surviving less well and not surviving.

Do not automatically classify the wood frog as surviving less well merely because it has a specialized adaptation.

### 2. “Taught in full” exceeds several explicit commitments

**Severity:** High  
**LAYER:** frame  
**REPEAT:** yes, earlier grade 3 review, finding 5; neighboring reviews of omitted elements  
**Confidence:** likely overall; firm on the identified omissions

**Location:** Standard bullet, lines 17 to 19; units 2, 4 and 5; “For the lead,” item 4.

**Problem and consequence:** The frame promises every clarification example and complete expectations, but leaves several components to inference:

- Unit 2 omits the electromagnet example despite the frame’s unusually comprehensive examples promise.
- Its 3-5-ETS1-1 work specifies needs, criteria and constraints, but does not place the associated element concerning changing human needs and wants.
- Unit 4 names finding mates, but its planned evidence concerns avoiding predators. No evidence case develops the mating advantage.
- Unit 5 asserts coverage of temperature and other organisms as environmental changes without identifying which case makes either explicit.

A writer can follow the named cases faithfully and still omit these commitments. The engineering evidence statement explicitly includes changing needs and wants. The variation expectation includes mating advantages. [Engineering evidence statements, PDF page 4](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/K-5%20ETS%20Evidence%20Statements%20June%202015%20asterisks.pdf#page=4), [3-LS4-2 foundation elements](https://www.nextgenscience.org/pe/3-ls4-2-biological-evolution-unity-and-diversity).

**Exact fix:** Add these commitments within their existing units:

1. **Unit 2:** An adult-operated, low-voltage electromagnet illustration, with apparatus and heat controls specified in the later investigation sheet. Students observe magnetic interaction; circuit construction is not taught. Add a brief comparison showing how a changed user need changes the latch’s criteria.
2. **Unit 4:** A sourced, nonhuman, within-species mating-success case with evidence students must explain. Avoid a universal claim that brighter animals always attract more mates.
3. **Unit 5:** Name the temperature change, such as a stream warming after its shading trees are removed, and the organism change, such as an introduced plant altering available food. Keep each case to one environmental change.

Add a compact element-to-unit record before calling coverage complete. This implements the repository’s stricter promise. The official standards’ suggested examples are not, by themselves, a requirement to teach every listed example. [Official magnetic-interaction clarification](https://www.nextgenscience.org/pe/3-ps2-3-motion-and-stability-forces-and-interactions).

### 3. Unit 3 needs an observation calendar and a dependable fallback

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, earlier grade 3 review, finding 3  
**Confidence:** likely

**Location:** Weather-log bullet, lines 40 to 43; unit 3, line 117.

**Problem and consequence:** Unit 3 opens with established seedlings and proposes firsthand life-cycle observations, but no planting or animal setup date is assigned. Its 22 lessons occupy about 5.5 instructional weeks at the stated frequency. Even specially selected rapid-cycling plants take approximately 40 calendar days to produce harvestable seed under specified lighting and growing conditions. That timing cannot safely be generalized to ordinary beans or radishes. [Growing-program guidance](https://fastplants.org/frequently-asked-questions/).

**Exact fix:** Add:

> Start the unit 3 seedling comparison during unit 2, on science day 18, with brief observations included in existing lessons. Before unit planning, select the organisms and record setup dates, expected observable stages, care requirements and the source for those timings. Use a supplied dated photograph sequence for stages that will not occur during the observation window or if growth fails. Distinguish directly observed stages from stages learned through that record.

Do not promise that ordinary radishes complete seed-to-seed development within this window.

### 4. Polar temperatures have no mathematics bridge

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, earlier grade 3 review, finding 4  
**Confidence:** firm

**Location:** Weather-log bullet and unit 6, line 120.

**Problem and consequence:** The named polar comparison includes Utqiagvik, whose winter monthly means are below zero even in Fahrenheit. Negative numbers are owned by grade 6 mathematics. The frame supplies averages appropriately, but gives no bridge for reading or graphing negative values. The problem can also arise in the class’s own winter log. [Official station normals](https://www.ncei.noaa.gov/access/services/data/v1?dataset=normals-monthly-1991-2020&endDate=9996-12-31&format=pdf&startDate=0001-01-01&stations=USW00027502).

**Exact fix:** Add:

> Preserve actual temperature observations in the teacher’s record. Below-zero conditions are described verbally and with a supported thermometer illustration; students do not calculate with negative numbers or construct negative-axis graphs. Polar climate comparisons use maps, descriptions and whole-number counts of months in stated temperature categories. Student weather graphs use suitable nonnegative quantities or categorical counts.

Also require unit 4 hunting-success data to use counts with equal trial totals, rather than assuming students can interpret percentages. This is a preventive representation choice, not evidence that the present frame already requires percent.

### 5. The proposed shorter path does not fit its stated schedule

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** firm

**Location:** “For the lead,” item 1, lines 161 to 165.

**Problem and consequence:** Removing about 15 days from 120 leaves 105 lessons. Three lessons weekly across the stated 30 science weeks provide only 90 lessons. The suggested alternative remains 15 lessons too long.

**Exact fix:** Replace the compression claim with:

> The full course requires 120 lessons, equivalent to four lessons weekly across 30 instructional weeks. A three-lesson schedule across those weeks provides 90 lessons. A complete 90-lesson alternative has not been established; identifying 15 compressible lessons would leave 105.

Retain the current allocations pending Cory’s audience and time decision. Do not cut standards or checks to make the arithmetic fit.

### 6. The prerequisite contract differs between science, mathematics and the progression

**Severity:** Moderate  
**LAYER:** progression  
**REPEAT:** yes, earlier grade 3 review, finding 7  
**Confidence:** firm

**Location:** Science Cross-subject table, lines 139 to 147; science progression measurement rows; mathematics frame’s outgoing science table.

**Problem and consequence:** Science correctly provides whole-unit and washer-count bridges, but:

- It locates formal measurement in the base text’s sixth unit, while the current mathematics frame places it in unit 7, approximately days 117 to 133.
- The mathematics frame promises early half-inch measurement and gram-scale reading, contrary to science’s chosen bridges.
- The progression still names the later mathematics without recording those bridges.

Writers following different files will make different prerequisite assumptions. ELA timing also needs actual unit references: W.3.1 belongs to ELA unit 3, which begins around science unit 4’s opening, rather than being securely completed beforehand.

**Exact fix:**

- Name mathematics unit 7 and its approximate day range in science.
- Replace mathematics’ early science bridges with whole-inch or whole-centimeter measurements and equal-object counts.
- Apply science’s existing proposed progression edits for `s3-motion-patterns`, `s3-environment-traits` and `s3-design-problem`.
- Name the actual ELA owning units. Explicitly retain science’s spoken argument and sentence-frame bridge while ELA opinion writing is beginning, and its supported two-source comparison where RI.3.9 timing overlaps.

No unit or standard needs to move.

### 7. The weather anchor assumes events the course cannot guarantee

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, earlier grade 3 review, finding 9  
**Confidence:** firm

**Location:** Unit 6 anchor, line 120.

**Problem and consequence:** “Twice this year the town had a warning” may be false for the teaching year or locality. Writers cannot depend on a local warning, much less exactly two.

**Exact fix:** Replace it with:

> The class log shows changing weather. A documented local or nearby weather warning, from this year or an earlier year, raises the question of how people can reduce harm.

Supply an archived warning and accompanying conditions for classes without a suitable current example.

### 8. The electronic fallback does not explicitly guarantee a paper route

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, earlier grade 3 review, finding 6  
**Confidence:** firm

**Location:** Materials and simulation provisions, lines 30 to 36 and the unit notes.

**Problem and consequence:** A class data set is permitted, but several units specifically propose simulations without explicitly requiring equivalent paper materials. The frame-writing instructions require a paper path beside electronic tools and no student account.

**Exact fix:** Add:

> Every electronic activity requires no student account and has a complete paper route using supplied images, observations or data. The paper route preserves the scientific question and evidence-based reasoning. Tool days also identify the single-projector arrangement.

### 9. Grade 2 promises grade 3 engineering work that grade 3 deliberately defers

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, earlier grade 3 review, finding 8  
**Confidence:** firm

**Location:** Grade 2 frame, outgoing seam for `s2-compare-designs`.

**Problem and consequence:** Grade 2 says grade 3 develops “criteria, constraints and fair tests of many solutions.” Grade 3 owns problem definition; the progression assigns generating and comparing several solutions to grade 4 and the planned prototype-testing expectation to grade 5. The handoff wording remains inconsistent despite the later K to 2 repairs.

**Exact fix:** Replace the receiving-work description with:

> Grade 3 specifies the need, success criteria and constraints precisely enough to judge proposed solutions. Earlier comparison work is retrieved as review; the later grades develop the assigned comparison and prototype-testing expectations.

### 10. The science rubric’s inventory omits the progression and course frames

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, grade 1 review and K to 2 fixes report  
**Confidence:** firm

**Location:** `docs/RUBRIC-SCIENCE.md`, lines 54 to 55.

**Problem and consequence:** It calls the old grade 4 draft and middle school base text the only science material. Current progression and course frames exist. The obsolete inventory directs readers away from relevant planning evidence.

**Exact rewritten note:**

> Science planning material now includes the science progression, course frames, the grade 4 scope and sequence draft, and the middle school base text. These establish planning commitments; they do not establish that a finished science course exists.

### 11. The rubric incorrectly says no plan locates the nature of science

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, recurring stale-note finding type  
**Confidence:** firm

**Location:** `docs/RUBRIC-SCIENCE.md`, Gateway 2 connections row, line 64.

**Problem and consequence:** Grade 3 explicitly assigns fair testing to unit 1 and evidence-based explanations of the past to unit 5. The blanket gap statement can trigger duplicate planning work.

**Exact rewritten note:**

> Course frames now identify planned nature-of-science opportunities. Science Grade 3 names fair testing in unit 1 and evidence-based explanations of the past in unit 5. Unit plans must turn these commitments into explicit student work and checks.

### 12. Mathematics still treats the other grade 3 frames as unwritten

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, analogous mathematics notes identified in neighboring science reviews  
**Confidence:** firm

**Location:** `docs/courses/math-grade-3/frame.md`, outgoing Cross-subject introduction, lines 155 to 156.

**Problem and consequence:** Science, ELA and social studies frames now exist, but the introduction describes them as future work. This discourages reconciliation of the conflicting measurement bridges in finding 6.

**Exact rewritten note:**

> The grade 3 science, English language arts and social studies frames are available. The following table records mathematics availability for those courses; their unit timing and local bridges must agree with the corresponding frame.

## What is right and should remain

- Preserve the six-unit order and current main-path allocations.
- Keep the weather log from week 1, supplied averages and later comparison with longer records.
- Preserve unseen transfer tasks, course checks and respond days.
- Keep nonhuman inheritance examples and the restrictions on comparing students’ bodies and families.
- Preserve explicit review of dormant prerequisites and the distinction between force arrows and later energy models.
- Keep environmental change, deep time and other scientific facts stated plainly.

The published [elementary curriculum framework](https://ssec.si.edu/sites/default/files/images/SSftC%20Frame%20work-.pdf) provides a useful comparison for bundling grade 3 expectations, without establishing a required unit count or sequence. The [other elementary program’s sequence guidance](https://openscied.org/curriculum/elementary-school/standards-alignment/) likewise distinguishes flexible ordering from genuine dependencies.

## Reconciliation with earlier reads

The earlier grade 3 report’s accuracy, planting, mathematics, paper-access and warning-anchor concerns remain substantially applicable.

I qualify three earlier recommendations:

- Reusing grade 2 plant evidence is defensible when explicitly retrieved as review and used to distinguish inherited variation from environmental influence. A new hydrangea anchor is not necessary. The [unit-review rubric](https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf) asks for building on prior learning.
- A specialized survival adaptation does not establish that an organism survives less well.
- Suggested clarification examples are not universally mandatory under the external standards. Finding 2 distinguishes the frame’s stricter examples promise from substantive expectation coverage.

The earlier blocked second-reader report is superseded by this substantive review under the user’s amended gate instruction. Its missing-dependency observation remains accurate; its conclusion that the frame must remain unread no longer governs this task.

## Settled by the expert

| Choice | Reason | Files affected |
|---|---|---|
| Preserve six units and 111 unit days | Ownership and dependencies support them | Grade 3 science frame |
| Replace the blanket frog exclusion | Named organisms and conditions support accurate reasoning | Frame; `s3-habitat-survival` |
| Begin seedling setup on science day 18; provide dated stage records | Makes the opening observable without guaranteeing an unsupported full life cycle | Frame, units 2 and 3 |
| Preserve actual temperature records; use supported categories for polar comparisons | Avoids premature negative-number graphing | Frame, unit 6 |
| Use equal-trial counts for hunting-success data | Keeps comparisons within available mathematics | Frame, unit 4 |
| Use whole length units and washer counts until formal measurement | Aligns existing science bridges | Science progression and both frames |
| Keep grade 2 plant evidence as explicitly labeled review | The deeper explanatory purpose can justify reuse | Frame, unit 3 |
| Require equivalent paper evidence for simulations | Preserves the question and reasoning across access routes | Frame and later unit plans |

## Science lens checklist: course frame layer

| Checklist line | Result | Evidence |
|---|---|---|
| Every grade expectation has a unit that teaches it fully | **Missed in part** | Placement complete; finding 2 identifies unresolved full-coverage commitments |
| Grades 6 to 8 preserve base-text order or explain departures | **Not applicable** | Grade 3 has no base text |
| High school expectations have explicit course ownership | **Not applicable** | Elementary course |
| Every unit names an anchor phenomenon or design problem | **Met for naming** | All six do; findings 1, 3 and 7 address accuracy and feasibility |

The broader lens commitments are present at frame level: integrated practices and ideas, question boards, model revision, arguments, fair investigations and unseen transfer. Actual lesson navigation, element-level assessment coverage, investigation safety and humane-care procedures require later unit and day evidence.

The [course criteria](https://cozy-dream-721ab6aab0.media.strapiapp.com/Science_20_K_5_20_Review_20_Criteria_2_0_ddd732f02c.pdf) and [evidence guide](https://cozy-dream-721ab6aab0.media.strapiapp.com/Science_20_K_5_20_Evidence_20_Guide_2_0_796df92bd4.pdf) support checking elements, scientific accuracy and feasible pacing. No numerical course rating is warranted from a frame alone.

## What I could not judge

No grade 3 unit plans, assessment items or lesson sequence exist in the target directory. Consequently, this read cannot establish instructional completion, actual lesson duration, transfer-task quality, scoring quality or investigation safety.

The detailed external elementary scope document could not be fetched. Its public sequence guidance was readable. The older criteria URL failed, but the current criteria and evidence guide were reached through the publisher’s official index.

The [science assessment research chapter](https://www.nationalacademies.org/read/23548/chapter/2) supports gathering evidence of integrated learning over time; it does not validate this course’s proposed duration.

## For Cory

- **Audience and time:** Confirm the 180-minute weekly science allocation alongside the other grade 3 subjects. A 90-lesson alternative has not been established.
- **Money:** Confirm or revise the proposed materials ceiling of about $25 per unit for a class of 30.
- **People:** Identify the science teacher who will review investigation safety and materials before the course is called finished.

## For the source list

Add the current criteria and evidence-guide addresses linked above, replacing the inaccessible older criteria address. Add the linked Arctic frog evidence, station normals and organism-timing guidance as factual checks, with their specific uses and limits. No source’s wording, tasks or images were copied into curriculum material.

**Verdict:** Revise before scope-and-sequence writing. **Finding count:** 12. **Report path:** `docs/reviews/frame-science-grade-3-2026-11-14.md`, supplied here only.


# Independent cold read: science-grade-2 scope and sequence

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/sequence-science-grade-2-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files were changed.

## Verdict

Revise before unit planning: the seven-unit order and most teaching and assessment reservations are sound. The largest risk is the unresolved timetable, which requires substantially more weekly science time than the frame authorizes. Reconcile that timetable, complete the year-end assessment evidence and make the pollination model’s causal relationships explicit while preserving the existing units and ownership.

**Finding count: 5.**

## What I read

- `docs/agents/EXPERT.md`, the science lens and `docs/RUBRIC-SCIENCE.md`.
- `docs/FOUNDATION.md`; relevant ROADMAP, BASELINE, GLOSSARY, APPROACH and APPROACH-SOURCES sections; the sequence-writing rules and plan-data guidance.
- The complete science-grade-2 scope and sequence, all 76 day rows and the course frame.
- All grade 2 science progression rows and their connected kindergarten and grade 1 prerequisites, including the recorded maintenance chains.
- `docs/courses/CALENDAR.md`, all grade 2 subject rows in `data/plans/calendar.csv` and the course’s `frames.csv` record.
- The local expectation-dimensions records, checked against official standards and evidence statements.
- Earlier grade 2 science frame reviews and fixes, relevant science progression and baseline records, and earlier sequence findings used to determine REPEAT tags.
- The base-text register. Elementary science has no base text.

Outside sources were opened during this read and are linked below. No curricular finding rests solely on memory. Prior-run memory was used only for review-scope discipline.

## Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Stopped with `ModuleNotFoundError: No module named 'markdown'` before completing the repository-wide check. |
| `python -X utf8 scripts/frame.py calendar` | Completed; no stagger-rule breaks reported. |
| `python -X utf8 scripts/frame.py check science-grade-2` | **0 failures:** seven units, 76 days, including 70 unit days. |
| `python -X utf8 scripts/plan.py check science-grade-2` | **0 sequence failures.** |
| `python -X utf8 scripts/stale.py check` | **56 files, 0 failures.** Manual discrepancies remain in finding 5. |

The incomplete global gate does not withhold this verdict.

## Findings, most serious first

### 1. The timetable exceeds the approved weekly allocation

**LAYER:** frame  
**REPEAT:** yes, conflicting teaching-week and time assumptions appeared in the earlier science frame and baseline reads  
**Severity:** serious  
**Confidence:** firm, from current records and independently checked arithmetic

**What is wrong.** The frame authorizes two 35 to 40 minute meetings a week, with a third meeting in approximately eight weeks, across approximately 34 teaching weeks. The shared calendar requires this course to finish in week 28.

The proposed day file contains:

- Ten weeks with two meetings.
- Sixteen weeks with three meetings.
- Two weeks with four meetings, weeks 26 and 27.

Two meetings for 28 weeks plus eight additional meetings provide **64 meetings**, twelve short of 76. After the week-17 respond day, the remaining 35 meetings must fit eleven weeks, exceeding three meetings every week.

The sequence correctly discloses this conflict. Disclosure does not make the course runnable under the approved allocation.

**Why it matters.** Schools following the frame would run out of time. Weeks 26 and 27 require 140 to 160 minutes of science each, against the frame’s approximately 80-minute weekly description.

**Exact fix.** Retain the current units, ownership and day counts pending Cory’s time decision. The concrete recommendation is to retain the proposed dates and replace the frame’s weekly description with the actual meeting pattern, averaging approximately **95 to 109 minutes a week over 28 weeks**. Cory must authorize that change; otherwise the calendar and course budget need a coordinated revision.

The external pacing criterion asks whether the suggested work is feasible within the stated time and whether alternatives are usable. It supplies no prescribed number of science minutes. [Science evidence guide, indicator 3i](https://cdn.edreports.org/media/2025/07/Science-K-5-Evidence-Guide_2.0.pdf).

### 2. Two year-end code claims lack explicit performance evidence

**LAYER:** sequence  
**REPEAT:** yes, incomplete standard-to-assessment alignment recurs in earlier frame and sequence reads  
**Severity:** serious  
**Confidence:** likely overall, with the omissions directly observable

**What is wrong.** Days 74 and 75 promise every part of their listed expectations, but the named tasks leave these gaps:

| Location | Missing evidence | Exact fix |
|---|---|---|
| Day 74, `2-PS1-4` | Wax melting and hardening demonstrates a reversible change; toast demonstrates lasting change caused by heating. No named case tests lasting change caused by cooling. | Add an unfamiliar frozen-and-thawed fruit image sequence. Ask what changed, what happened when warming reversed the cooling, and which evidence supports the reversibility claim. Retain wax and toast. |
| Day 75, `2-LS2-1` | Planning and interpreting supplied plant observations do not themselves demonstrate conducting the investigation. Unlike day 58, this check does not explicitly incorporate the student’s recorded investigation performance. | Name the student’s unit 5 planning and data-collection record as an assessed product considered alongside the fresh transfer task. Require an identifiable record of the student’s contribution, rather than crediting participation in the class investigation generally. |

The official evidence descriptions distinguish changes after heating and cooling and their attempted reversals. They also distinguish planning a plant investigation from collecting its data. [Elementary evidence statements, PDF pages 28 to 30](https://www.nextgenscience.org/sites/default/files/Elem%20%2B%20Exec%20Summary%20June%202015.pdf).

A frozen-and-thawed fruit is a defensible new cooling case: fruit can remain softer after thawing. Students need the observable evidence, without a cellular explanation. [National Center for Home Food Preservation, freezing-fruit FAQ](https://nchfp.uga.edu/faqs/fruits/category/faq-freezing).

**Why it matters.** A writer can implement the current summaries faithfully and still collect narrower evidence than the code claims. Six-minute stations on the shorter-period route make those omissions easier to overlook.

**Exact overall fix.** Revise the two CSV notes and the course-check description to name these components. Keep the existing check and respond days. Before retaining the three-six-minute-station claim, time a complete version that includes the model explanation, both plant comparisons and habitat observations; preparation alone does not establish feasibility.

### 3. Unit 6 does not explicitly explain the flower visits or the plant side of pollination

**LAYER:** sequence  
**REPEAT:** yes, this is the same kind of incomplete element reservation found in earlier science frame coverage findings  
**Severity:** moderate  
**Confidence:** likely

**What is wrong.** The frame asks why bees visit successive flowers. Days 60 to 65 describe visits and pollen movement, but never explicitly teach the food-seeking reason for the visits.

Day 63 moves pollen markers between model flowers, without specifying the plant structures represented by the pollen source and receiving location. Day 64 likewise reserves structure-function reasoning generally, without naming those plant components.

The modelling evidence includes relevant animal structures, plant structures and pollen or seeds, together with their relationships. [Official `2-LS2-2` evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/2-LS2-2%20Evidence%20Statements%20June%202015%20asterisks.pdf). Bees seek floral food, and their visits can transfer pollen between flowers. [USDA, Insects and Pollinators](https://www.nrcs.usda.gov/conservation-basics/animals/insects-pollinators).

**Why it matters.** Children could learn that bees move pollen “to help plants” without explaining the observed visits. A successful marker-transfer demonstration could also omit what the flower components represent.

**Exact fix.**

- On day 60, use the visit photographs to establish that bees seek nectar or pollen for food.
- On day 63, give each model flower a visible pollen source and receiving patch. Students identify what these and the animal model represent.
- On day 64, require the explanation to connect the relevant plant and animal components to the demonstrated movement.
- On day 65, return explicitly to both anchor questions.

Keep this within the six days. Detailed reproductive anatomy and terminology are unnecessary.

### 4. Unit-level cost estimates are deferred beyond the layer that owns them

**LAYER:** sequence  
**REPEAT:** new at this layer  
**Severity:** moderate  
**Confidence:** likely

**What is wrong.** “Calendar and access” retains the approved approximately $50 annual additional-materials allowance, then assigns all unit-level costing to later unit plans. The science rubric explicitly includes **S6, costs**, in the scope and sequence review.

The supplies column is useful, but it does not establish what the room is assumed to own or whether the proposed route fits the allowance.

**Why it matters.** Missing fans, rulers, trays, eye protection or model materials could change the practical route after unit planning has begun.

**Exact fix.** Add a provisional seven-row materials estimate separating:

1. Existing classroom equipment assumed.
2. New reusable equipment.
3. Consumables.
4. The minimum physical materials still needed for the no-kit route.

Count reused purchases once. State the classroom-size assumption and reconcile the total with the existing allowance. These are planning estimates; any requested budget increase belongs to Cory.

### 5. Current authoring inputs still give conflicting instructions

**LAYER:** frame, process  
**REPEAT:** yes, stale prerequisite, status and calendar wording recur in earlier reviews  
**Severity:** minor  
**Confidence:** firm

**What is wrong.** The stale gate passes, but the following discrepancies remain:

| Current input | Conflict | Exact fix |
|---|---|---|
| Frame opening and closing chronology | They still describe the sequence and exact dates as future work. | Link the existing sequence and day record; distinguish proposed dates from an approved timetable. |
| Frame Seams table, units 1 and 5 | “Readiness look” remains for preceding-year or maintained skills. | Replace it with the corresponding retrieval-task wording. |
| Frame mid-year check | It retains the dog-bed material-choice context that the sequence replaces with earlier erosion content. | Carry the erosion-purpose replacement into the frame check table. |
| Generated science calendar rows | They still show older dates, including unit 1 ending on school day 21 and the mid-year respond day on school day 86. The day file gives 20 and 85. | After the timetable decision, regenerate through `frame.py sync` and rerun the calendar check. Do not hand-edit generated rows. |

**Why it matters.** Later writers and other subjects can receive different instructions depending on which authoritative input they open. The sequence’s explanatory notes identify several conflicts but leave both instructions active.

## Order, load and standards

All **12 owned skills and 12 owned codes** have teaching and assessment reservations. These expectations have no lettered subcodes; completeness depends on their substantive requirements and dimension elements.

| Unit | Teaching days | Assessment + response | Judgment |
|---|---:|---:|---|
| 1. Land and water | 8 | 2 | Model construction precedes comparison; source choice precedes combined information. |
| 2. Land changes | 14 | 2 | Largest allocation justified by sources, two erosion agents and tested design comparisons. |
| 3. Materials | 10 | 2 | Sorting precedes purpose-based selection; multiple property tests justify the allocation. |
| 4. Changes | 7 | 2 | Reassembly provides an accessible start before thermal-change arguments. |
| 5. Plant needs | 7 | 2 | The sustained investigation justifies more time than the other single-skill units. |
| 6. Seeds and pollinators | 4 | 2 | Tight but plausible using established routines, with finding 3 repaired. |
| 7. Habitats | 6 | 2 | Inventories precede comparisons; repeated observation informs revision. |
| **Total** | **56** | **14** | **70 unit days, plus six course-level check and respond days.** |

No entire unit is demonstrably far over or under its load. No unit exceeds 25 days, so no mid-unit assessment is required. Response time is counted once: seven unit respond days and two course-level respond days.

The reservations preserve the important boundaries: observable properties, length-only numerical measurements, qualitative geological durations, models without numerical scale, no particle explanation and habitat comparisons without scientific-name recall. These agree with the [official K-2 standards](https://www.nextgenscience.org/sites/default/files/K-2Topic.pdf).

## Readiness and retrieval

On the recorded progression, the sequence’s decision to use retrieval is justified.

| Incoming thread | Last recorded use before grade 2 | Placement |
|---|---|---|
| All directly assumed `s1-` rows | Grade 1 | Retrieval within the relevant teaching days. |
| `sk-living-needs` | Maintained through grade 1 `s1-parts-mimic` | Day 51. |
| `sk-needs-places` | Maintained through grade 1 `s1-parts-mimic` | Day 66. |
| `sk-forecast-severe` | Recorded as maintained through grade 1 `s1-parent-offspring` | Day 11. |
| Earlier same-year science models and routines | Earlier units | Retrieved near their next use. |

No sequence row incorrectly checks a preceding-year skill or retrieves a row classified as unmaintained older learning. There is no misplaced first-day readiness check or readiness check scheduled weeks ahead. The frame terminology still needs finding 5.

## Calendar, checks, candidates and shorter path

- **Check weeks:** days 39 and 40 fall in week 17; days 74 and 75 fall in week 28. These match the target weeks and avoid other subjects’ course-check weeks.
- **Cross-subject leans:** early erosion measurement has a ruler bridge. Graph work follows mathematics unit 1. Early ELA leans retain read-alouds, shared records and spoken-first writing support. Science’s land-and-water work finishes before social studies needs it.
- **Non-repetition:** the mid-year check uses earlier landscape and erosion content for unit 3 skills. The year-end habitat comparison uses earlier plant and seed settings. Both decisions are explicit in prose and day notes.
- **Candidates:** all seven are settled. The map, protected-hillside photographs and repeated survey each cost one existing day. Pencil dismantling, melted crayons, the cooler plant treatment and an additional group animal model are dropped with reasons.
- **Shorter year:** the ten named fold-ins remove no assessment or respond day and preserve the plant and survey intervals.
- **Shorter periods:** the proposed methods are appropriate planning directions. The specific final-check timing remains unverified, as finding 2 explains.
- **Source map:** not applicable because this course has no base text.

## Science lens checklist: scope and sequence layer

| Lens line | Result | Evidence |
|---|---|---|
| A unit anchor is a phenomenon or problem rather than a topic | **Met** | Runoff, erosion, failed hat, contrasting changes, pale grass, animal visits and schoolyard surveys. Unit 6’s explanation needs finding 3. |
| A model is built before later work uses it | **Met** | Land representation precedes erosion; property tests precede selection; plant work precedes later ecological comparisons. |
| Engineering expectations appear through design work | **Met** | Unit 2 tests and compares solutions, including each design’s strengths and weaknesses. |
| Equipment has substitutes or a no-kit path | **Met at reservation level** | Alternatives are named throughout. Cost evidence needs finding 4; later materials must preserve the practices. |

At the rubric’s scope layer, phenomena, ownership, band boundaries and interdisciplinary timing are substantially secured. Complete assessment evidence and cost planning remain open. This is not a rating of finished lessons or materials.

## Settled by the expert

| Choice | Reason | Files affected when applied |
|---|---|---|
| Keep seven units and their existing day counts | No whole-unit load fault warrants resizing. | Frame, sequence and day record |
| Retain the recorded retrieval placements | The progression identifies preceding-year use or maintenance. | Frame wording only |
| Add a frozen-and-thawed fruit evidence sequence to day 74 | Supplies the missing lasting cooling-change comparison. | Sequence and day 74 |
| Incorporate identifiable unit 5 investigation records into the year-end evidence | Preserves the conducting requirement without pretending a new growth study fits a station. | Course-check description and day 75 |
| Make the pollination model’s food-seeking context and plant components explicit | Completes the anchor explanation and model relationships. | Unit 6 description and days 60, 63 to 65 |
| Retain all seven candidate decisions and ten named fold-ins | Their purposes and costs are accounted for. | No change |

## What is right and should remain

Preserve the source-choice task, temperature-dependent classification, individual unfamiliar-case unit performances, strengths-and-weaknesses design comparisons and equal-count/different-kinds habitat comparisons. The plant study’s elapsed time, caution about height alone, stored-seed fallback and explicit safety controls are also valuable.

## What I could not judge

Actual task timing, scoring quality, prepared observation sets, purchase costs and completed safety implementation do not yet exist at this layer. The elementary reference overviews were reachable, but they do not establish equivalent lesson minutes; the full elementary scope-and-sequence embed timed out. The required science approach page is absent.

## Sources and source-list notes

- [Official K-2 standards](https://www.nextgenscience.org/sites/default/files/K-2Topic.pdf): ownership, dimensions and assessment boundaries.
- [Elementary evidence statements](https://www.nextgenscience.org/sites/default/files/Elem%20%2B%20Exec%20Summary%20June%202015.pdf): required observable performances, especially thermal changes and plant investigation.
- [EQuIP science rubric](https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf): coherence and direct evidence of integrated performance.
- [K-5 science evidence guide](https://cdn.edreports.org/media/2025/07/Science-K-5-Evidence-Guide_2.0.pdf): unfamiliar assessment situations and pacing feasibility.
- [OpenSciEd matter](https://openscied.org/instructional-materials/2-2-matter/), [habitats](https://openscied.org/instructional-materials/2-3-habitats/) and [plants](https://openscied.org/instructional-materials/2-4-puzzling-plants/): public reference descriptions and expectation groupings only.
- [Core Knowledge science sequence](https://www.coreknowledge.org/wp-content/uploads/2020/07/CoreKnowledge_Science_Sequence_Rev.pdf): a second public sequence comparison. Its broader content is not treated as this course’s required scope.

**For the source list:** add the reachable USDA pollinator explanation and freezing-fruit FAQ linked in findings 2 and 3 if absent. Record the timed-out elementary sequence embed as unread, rather than relying on its search excerpt.

## For Cory

- **Teaching time:** authorize the concrete 76-meeting, 28-week pattern, including four meetings in weeks 26 and 27, or commission a coordinated calendar and time-budget revision. This changes the approved classroom time assumption.

**Verdict: revise before unit planning. Findings: 5. Report path: `docs/reviews/sequence-science-grade-2-2026-11-14.md` (supplied here, not written).**


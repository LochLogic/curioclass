# Independent first read: Science Grade 3 scope and sequence

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/sequence-science-grade-3-2026-11-14.md`  
**Delivery:** Complete report supplied here. No file was created or edited.

## Verdict

The sequence is coherent and substantially complete at this layer, but needs a readiness-timing correction and reconciliation of active authoring instructions before unit planning. The greatest risk is that later writers follow conflicting prerequisite and safety rules despite the sequence’s generally clear decisions. Move unit 1 readiness to the start-of-year check required by this review brief, then align the upstream instructions while preserving the six-unit, 120-meeting structure.

## What I read and checked

- `docs/agents/EXPERT.md`, the science lens, `docs/RUBRIC-SCIENCE.md`, FOUNDATION, the relevant ROADMAP sections, BASELINE rules 20 to 24, and the glossary.
- The complete target scope and sequence, all 120 rows of its `days.csv`, and its frame.
- Grade 3 science progression rows and the earlier rows recording their prerequisite histories.
- CALENDAR.md, the grade 3 calendar records, and relevant mathematics, ELA and social studies frame provisions.
- APPROACH.md, relevant APPROACH-SOURCES entries and evidence notes, and the base-text record. `docs/APPROACH-SCIENCE.md` is absent.
- Earlier grade 3 science frame reads and relevant science sequence and process reviews, within the blind boundary.
- Outside standards, evidence statements, review guidance and reference curriculum material linked below.

Prior-run memory prompted dependency and calendar checks only. No substantive finding rests on unverified memory.

### Gates

`plan.py check` stopped with `ModuleNotFoundError: No module named 'markdown'`; the review continued with the required structural fallback.

| Command | Result |
|---|---|
| `python -X utf8 scripts/frame.py calendar` | Passed; grade 3 science checks occupy weeks 9, 20 and 30 |
| `python -X utf8 scripts/frame.py check science-grade-3` | Passed: 0 failures; 111 unit days and 9 course-level days |
| `python -X utf8 scripts/sequence.py check science-grade-3` | Passed: 0 failures |
| `python -X utf8 scripts/stale.py check` | Passed: 56 files, 0 failures |

The sequence gate accepts the local unit 1 exception discussed in finding 1. That does not establish compliance with this run’s different instruction.

## Findings, most serious first

### 1. Unit 1 readiness is correctly classified but incorrectly placed under this brief

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, prerequisite timing and conflicting readiness instructions recur in earlier sequence reviews  
**Confidence:** Firm

**Location:** Scope and sequence, unit 1, paragraph beginning “Readiness occupies”; “For the lead,” item 1; CSV days 1, 2 and 8.

**What is wrong:** The final ten minutes of day 1 assess `sk-push-pull` and the prediction practice from `s1-sky-patterns`. This run explicitly requires unit 1 readiness in the start-of-year check and keeps the unit’s first day clear for its hook and compelling question.

The readiness classification is justified. Pushes and pulls were last explicitly used in grade 1, and the sky-pattern prediction row has no recorded grade 2 use. Neither qualifies automatically for retrieval under the controlling last-use rule.

There is a real instruction conflict: local `sequence-write.md`, rule 2, explicitly permits unit 1 readiness after day 1’s hook. The writer followed that exception, but this review brief supersedes it.

**Why it matters:** The diagnostic cannot shape the opening lesson when its results arrive at that lesson’s end. Conflicting instructions also let a gate pass a placement this review was expressly asked to reject.

**Exact fix:**

- Move these two diagnostic tasks to the start-of-year check administered before science day 1.
- Remove `assess=readiness` and the ten-minute diagnostic reservation from day 1.
- Retain day 2’s differentiated support, explicitly naming both push/pull reasoning and prediction from observed patterns.
- Update day 8 and the sequence’s lead note to reference the start-of-year evidence.
- Identify where the diagnostic’s ten minutes fit in the start-of-year arrangements without silently adding a 121st science meeting.
- Align the local writing instruction with the controlling timing rule.

Keep unit 5 readiness on day 81. It is immediately before unit 5 and already uses the correct respond-day location.

### 2. Active upstream documents retain instructions the sequence has superseded

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, the same rubric contradictions appear in the earlier kindergarten science sequence review, finding 5; obsolete readiness wording appears in the grade 1 review, finding 5  
**Confidence:** Firm

**Location:** Grade 3 frame, Days and Seams; relevant progression handoff notes; frame “For the lead,” item 3; science rubric Gateway 2 coverage row, S5 and “Questions for Cory.”

**What is wrong:** The stale checker passes, but these discrepancies remain:

| Active instruction | Conflict | Exact fix |
|---|---|---|
| The frame treats rows from grade 1 or 2 as retrieval; the two unit 1 progression notes invoke a content-revisited exception | This run requires classification by recorded last use | State the last-use rule and identify the two unit 1 readiness rows explicitly |
| The frame still says the dimension-data gap awaits the sequence; the rubric says dimension statements exist in no data file | `ngss-pe-dimensions.csv` exists and the sequence uses it | Link the existing file and retain the requirement to verify its instructional and assessment use |
| Rubric S5 and its closing question require a science teacher’s safety read | Current FOUNDATION 7.3 and this frame require the safety agent’s read against published guidance | Update the rubric while preserving FOUNDATION’s separate human pilot requirements |
| The frame and progression retain “freezing solid” for the wood frog | The sequence correctly warns against implying complete cellular freezing | Replace it with “survives partial freezing in winter” and retain the needs-and-conditions argument |

The wood-frog correction is supported by the state wildlife account, which distinguishes ice between cells from lethal freezing within cells. [Colorado Parks and Wildlife, Wood Frog](https://cpw.state.co.us/species/wood-frog).

**Why it matters:** A later writer can reintroduce a corrected scientific statement, use the wrong diagnostic type, or impose an obsolete completion requirement by following another active input.

**Exact overall fix:** Reconcile these specific passages with the current sequence and FOUNDATION. Mark the existing dimension file as available, without describing its existence as proof of completed coverage. These are corrections to authoring inputs, not reasons to reopen settled unit ownership or day allocations.

## Order, load and assessments

All 15 owned progression rows and 16 owned expectations have identifiable teaching and end-of-unit assessment reservations. I found no missing owned expectation at this layer.

| Unit | Teaching days | Assessment days | Respond days | Judgment |
|---|---:|---:|---:|---|
| 1. Pushes, pulls and swings | 14 | 1 | 1 | Class testing precedes group testing; motion records precede predictions |
| 2. Non-contact forces and design | 14 | 2 | 1 | Interaction evidence precedes criteria, constraints and changed-user needs |
| 3. Life cycles and traits | 19 | 2 | 1 | Reproduction precedes offspring comparisons; inheritance precedes environmental influence |
| 4. Survival | 17 | 2 | 1 | Group arguments, individual variation and habitat fit receive distinct development |
| 5. Environmental change | 13 | 2 | 1 | Fossil inference precedes present-day solution judgments |
| 6. Weather, climate and hazards | 17 | 2 | 1 | Seasonal representation precedes climate synthesis and hazard-design judgments |
| **Total within units** | **94** | **11** | **6** | **111 days** |

Six course-level check days and three course-level respond days complete the 120 meetings.

No whole unit is demonstrably far over or under its load. Unit 2’s 17 days support two progression rows but three expectations, including investigation and full problem definition. Unit 3’s 22 days reasonably accommodate three substantial performances and longitudinal records. Units 4 and 6 each allocate roughly five principal days to each of three strands before integration and assessment.

No unit exceeds 25 days, so no mid-unit assessment is required. Response time is counted once per unit and once per course-level check.

The formal assessment reservations are appropriately specific:

- Days 15 and 34 retain planning and conducting, alongside observation-based prediction.
- Days 31, 32 and 35 retain questioning and complete magnetic problem definition.
- Days 56, 57 and 79 retain animal and flowering-plant models, plant and animal trait evidence, and environmental explanations.
- Days 76, 77 and 80 retain group arguments, variation advantages and habitat reasoning.
- Days 95, 96 and 118 retain fossil inference and solution-merit arguments.
- Days 115, 116 and 119 retain representation, climate-source synthesis and hazard-design judgment.

These are reservations, not verified items or scoring instruments. The official investigation evidence distinguishes planning from collecting and recording data under the plan. The draft’s requirement to preserve assessed performances on alternative routes should remain binding during unit planning. [3-PS2-1 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/3-PS2-1%20Evidence%20Statements%20June%202015%20asterisks.pdf).

The expectations have no lettered subcodes. Their substantive requirements and dimension elements, rather than code presence alone, determine completeness. [Official standards and foundation boxes](https://www.nextgenscience.org/sites/default/files/AllDCI.pdf).

## Readiness and retrieval

| Assumed row or group | Last recorded use | Sequence decision |
|---|---|---|
| `sk-push-pull` | Grade 1 | Readiness justified; placement needs finding 1 |
| `s1-sky-patterns` | Grade 1 | Readiness justified; placement needs finding 1 |
| `s2-compare-designs` | Grade 2 | Day 25 retrieval is appropriate |
| `s2-seed-pollinator-model`, `s2-plant-needs-test` | Grade 2 | Days 37 and 47 retrieval are appropriate |
| `s1-like-parents` | Grade 2 practice link in `s2-heat-cool-change` | Day 43 follows the brief’s recorded-use rule |
| `s1-parent-offspring` | Grade 2 source work | Day 59 retrieval follows recorded use |
| `s1-parts-mimic` | Grade 2 plant and habitat work | Day 64 retrieval is appropriate |
| `s2-habitat-diversity` | Grade 2 | Day 59 retrieval is appropriate |
| `s2-fast-slow-events` | Grade 2 | Day 82 retrieval is appropriate |
| `sk-reduce-impact` | Kindergarten | Day 81 readiness is correctly placed |
| `sk-weather-watch` | Same-year log before unit 6 | Day 98 retrieves an established routine |
| `s2-land-water-model` | Grade 2 | Day 103 retrieval is appropriate |
| `sk-forecast-severe` | Grade 2 `s2-fast-slow-events` | Day 108 retrieval is appropriate |
| `s2-erosion-solutions` | Grade 2 | Day 109 retrieval is appropriate |

No preceding-year row is unnecessarily assigned readiness. Apart from unit 1’s placement, no readiness check is scheduled on a unit’s first day or weeks before use.

## Calendar, non-repetition, candidates and shorter path

**Calendar:** Checks occupy weeks 9, 20 and 30, matching the targets. The second response falls in week 21 and does not create an assessment-week collision.

**Cross-subject leans:** The recorded bridges resolve the timing dependencies. Early lengths use whole units, magnetic holding criteria use washer counts, and scaled graphs follow mathematics unit 1. Concurrent discussion, argument writing and two-source comparison receive local instruction. Globe work precedes climate work. ELA supplies its own frog facts rather than requiring science mastery prematurely.

**Non-repetition:** Each course-level check explicitly returns to earlier-unit content for recently assessed skills: swing contexts after unit 2, unit 3 organisms after unit 4, and the earlier weather-log context after unit 6. These are defensible transfer reservations. Actual tasks must preserve the stated separation.

**Candidates:** All six are settled with costs:

| Unit | Decision |
|---|---|
| 1 | Come-back can dropped; zero days |
| 2 | Compass extension dropped; zero days |
| 3 | Seed-packet comparison retained; 15 minutes on day 42 |
| 4 | Local habitat retained; day 73 plus ten minutes on day 72 |
| 5 | State or regional fossil retained; 20 minutes on day 86 |
| 6 | Forecast and warning retained; 15 minutes on day 108 |

**Shorter path:** The ten named folds are 13→14, 22→21, 29→30, 42→41, 51→50, 63→62, 74→75, 86→85, 93→94 and 113→114. None removes a formal assessment or respond day. The instructions retain the reasoning, section exit tickets and longitudinal data, while keeping checks in their target weeks.

The shorter-period guidance identifies sensible reductions in copying and duplicate reporting. Feasibility remains a later timing question. The external pacing guidance asks for usable scheduling alternatives and reasons for adjustments, rather than prescribing lesson counts. [K-5 science evidence guide, indicator 3i](https://cozy-dream-721ab6aab0.media.strapiapp.com/Science_20_K_5_20_Evidence_20_Guide_2_0_796df92bd4.pdf#page=70).

**Source map:** Not applicable. Elementary science has no base text.

## Science lens checklist: scope and sequence

| Lens line | Result | Evidence |
|---|---|---|
| Anchor is a phenomenon or design problem, rather than a topic | Met | Observable motion, non-contact attraction, living records, habitat contrasts, fossils and weather records |
| Models are built before later work uses them | Met | Force arrows precede magnetic applications; traits precede variation; habitat systems precede environmental change |
| Engineering expectations appear through design work | Met | Unit 2 explicitly defines needs, criteria and constraints; later units judge solutions |
| Equipment has substitutes or a no-kit path | Met at reservation level | Shared apparatus, household stand-ins, labelled records and paper routes are named; assessed practices are expressly protected |

The named initial, revised and consensus models are a strength. The outside coherence criteria support tracing questions and evidence between lessons, rather than treating the opening phenomenon as decoration. [EQuIP science rubric, unit coherence](https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf#page=3).

## Settled by the expert

| Choice | Reason | Files affected when applied |
|---|---|---|
| Keep six units and existing allocations | No demonstrated whole-unit load fault | No allocation changes |
| Use start-of-year readiness for the two dormant unit 1 prerequisites | Required by this review brief and supported by recorded last use | Sequence, days 1, 2 and 8, upstream readiness wording |
| Keep day 81 readiness and day 83 support | Correct timing and explicit response | No change |
| Retain the candidate decisions and ten folds | Costs and retained work are named | No change |
| Retain performance requirements on alternative routes | Supplied records alone cannot demonstrate conducting an investigation | Later unit and assessment plans |
| Use partial-freezing wording for the wood frog | Avoids the false implication that its cells freeze | Frame and progression |
| Reconcile rubric status and safety requirements with current inputs | Prevents duplicated work and obsolete completion conditions | Rubric and frame notes |

## What is right and should remain

Preserve the early planting date, labelled photograph fallbacks, refusal to presume experimental results, explicit mating-advantage evidence, all three habitat outcomes, five environmental-change cases, many-year climate evidence and unfamiliar assessment situations.

Earlier frame concerns about missing examples, calendar bridges, planting timing and paper access have substantially been addressed. They should not be reopened as unchanged defects.

## Limits and outside sources

I could not judge actual assessment timing, scoring, accommodations, source-specific datasets, retail costs or completed safety implementation. Those materials are not supplied at this layer.

Reference comparisons were limited:

- [OpenSciEd grade 3 forces overview](https://openscied.org/instructional-materials/3-1-forces-interactions/): investigation-to-design dependencies, not a required pacing template. Its full elementary scope-and-sequence embed timed out.
- [Core Knowledge science sequence](https://www.coreknowledge.org/wp-content/uploads/2020/07/CoreKnowledge_Science_Sequence_Rev.pdf): a second ordering comparison. Its additional content is not treated as required scope.
- [3-LS2-1 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/3-LS2-1%20Evidence%20Statements%20June%202015%20asterisks.pdf): group-survival argument requirements.
- [3-ESS2-1 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/3-ESS2-1%20Evidence%20Statements%20June%202015%20asterisks.pdf): seasonal representation requirements.

**For the source list:** Record the working criteria and evidence-guide links reached through the [current science review-tools page](https://edreport.org/process/review-tools/science). The older criteria address in the rubric was inaccessible during this read.

## For Cory

- **Time and audience:** The frame promises a 90-meeting route for schools with less weekly science time. This sequence demonstrates 110 meetings and candidly leaves another 20 folds unresolved. Before presenting the 90-meeting route as available, require its complete coverage and calendar demonstration or revise that adoption promise.

**Verdict: revise before unit planning. Findings: 2. Report path: `docs/reviews/sequence-science-grade-3-2026-11-14.md`, supplied here, not written.**


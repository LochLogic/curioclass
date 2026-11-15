# Independent read: science-grade-4 scope and sequence

**Intended report path:** `docs/reviews/sequence-science-grade-4-2026-11-14.md`  
**Delivery:** Complete report supplied here. No file was created, edited or deleted.  
**Finding count:** 3.

## Verdict

The overall order and day allocation are sound, with explicit model development, substantial investigation and design work, and sensible cross-subject bridges. The biggest content risk is the resource assessment reservation, which omits the role of technology in extracting resources and reducing environmental effects. Revise that reservation, add provisional unit costs, and align the conflicting frame and rubric instructions before using the sequence as the unit-writing contract.

## What I read

- `docs/agents/EXPERT.md`, the science lens and `docs/RUBRIC-SCIENCE.md`.
- The complete science-grade-4 scope and sequence, frame and 120-row day record.
- All 14 grade 4 science progression rows, their incoming prerequisites, and the earlier rows used to substantiate maintenance.
- `docs/courses/CALENDAR.md`, the grade 4 rows of `data/plans/calendar.csv`, and the science-grade-4 frame register entry.
- Relevant foundation, approach, glossary, roadmap, BASELINE and source-policy guidance; science entries in `APPROACH-SOURCES.md`; and the grade 4 elements in `ngss-pe-dimensions.csv`.
- Earlier grade 4 science frame reviews, their fix record, and permitted earlier science sequence findings for repeat classification.

I respected the blind-file exclusions. Science Grade 4 has no base text, so a base-lesson source map is not applicable.

Outside reading included official standards and selected evidence statements, EQuIP, and the curriculum comparisons linked below. No substantive finding rests solely on memory. Prior-session memory informed the review format only.

## Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Could not complete: `ModuleNotFoundError: No module named 'markdown'`. |
| `python -X utf8 scripts/frame.py calendar` | Completed; grade 4 science checks fall in weeks 10, 19 and 30. |
| `python -X utf8 scripts/frame.py check science-grade-4` | 0 failures; six units, 120 days, comprising 111 unit days and nine course-level days. |
| `python -X utf8 scripts/stale.py check` | 56 files checked, 0 failures. |

The incomplete full plan gate does not prevent this content verdict.

## Findings, most serious first

### 1. Resource teaching and assessment do not explicitly carry the technology component

**Severity:** Moderate  
**LAYER:** standard, sequence  
**REPEAT:** yes, incomplete performance reservations recur in the earlier science frame and sequence reads; this particular omission is new.  
**Confidence:** likely

**Location:** Unit 2, especially days 33, 37 and 40; the standards-coverage row for `4-ESS3-1`.

**What is wrong:** Day 33 connects changing needs and science knowledge with technology choices. Days 37 and 40 reserve combined-source explanations of natural origins, renewability and environmental effects. None explicitly requires students to explain how technology extracts or uses a resource, or how an improved technology changes an environmental effect.

Those are observable components in the official evidence statement, beyond identifying renewable resources and listing harms. [4-ESS3-1 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/4-ESS3-1%20Evidence%20Statements%20June%202015%20asterisks.pdf)

**Why it matters:** A writer could satisfy every named reservation with a renewable/nonrenewable classification and a list of pollution or habitat effects, leaving the technological cause-and-effect reasoning untaught and unchecked.

**Exact fix:**

- Use part of day 33 for a sourced comparison of one resource-use technology before and after an improvement, such as an electricity-generating facility with and without a specified pollution control.
- Require students to explain how the resource supplies a human energy need, what the technology does, which environmental effect changes, and which effects remain.
- Add that causal explanation explicitly to day 37.
- Add a fresh, brief technology comparison to day 40, retaining its earlier-unit transport context.
- Update the standards-coverage row accordingly.

Keep the work within the existing six resource days. Detailed engineering mechanisms and numerical efficiency calculations are unnecessary.

### 2. The materials ceiling has no unit-level cost evidence

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, the same deferral appears in `sequence-science-grade-2-codex-2026-11-14.md`, finding 4.  
**Confidence:** firm

**Location:** “Materials, tools and access,” particularly the statement that detailed quantities and actual cost checks belong to unit plans.

**What is wrong:** The sequence retains the approved approximately $30 additional-materials ceiling per unit, but supplies no provisional cost for any unit. The science rubric explicitly assigns **S6 costs** to the scope and sequence layer.

The day record identifies materials well, but does not distinguish existing classroom stock from purchases. In particular, a hand-crank flashlight, compatible electrical components, a large water tub, a coil, acrylic mirrors, eye protection and specimens cannot all be assumed available without saying so.

**Why it matters:** Later writers may discover that the selected investigation route or rotation arrangement does not fit the approved ceiling.

**Exact fix:** Add a six-row provisional materials table showing:

- Assumed classroom stock.
- New reusable equipment and consumables.
- Quantities for 30 students under the shared-apparatus route.
- The unit’s additional cost and the source/date of the estimate.
- Minimum physical equipment retained in the fallback route.

Count purchases reused across units once. Include the sunlight-observation contingency in unit 2’s equipment assumptions. Retain the existing ceiling; any proposed increase belongs to Cory.

### 3. Current authoring inputs retain conflicting instructions

**Severity:** Moderate  
**LAYER:** frame, process  
**REPEAT:** yes, stale prerequisite, assessment and status instructions recur in the earlier science frame and sequence reads.  
**Confidence:** firm

**What is wrong:** The stale gate passes, but the following current instructions still disagree.

| Location | Conflict | Exact fix |
|---|---|---|
| Frame opening, Days bullet and Seams table | The frame still places readiness checks at unit openings, broadly treats grade 2 rows as retrieval, and calls sunlight warming last used in kindergarten. The sequence correctly places checks before units and identifies grade 1 use. | Link the existing sequence and day record. Replace the general rule with the current last-use rule. Name readiness on days 15, 41 and 76, with response inside the following opener. |
| Frame unit 5 and water-location seam | `s2-water-where` remains retrieval, although the sequence correctly identifies no grade 3 maintenance and checks it on day 76. | Separate water-location readiness from land-water-map retrieval. |
| Frame unit 3 and mathematics bridge | Ruler measurements of wavelength remain required, while the sequence uses qualitative comparisons and an unnumbered strip. | Remove numerical wavelength measurement from the frame and retain the sequence’s qualitative comparison. |
| Frame Course-level checks table | Check 3 still describes survival-only structure arguments and omits the sense-brain-response performance reserved in the sequence. Other check descriptions also omit parts now explicitly reserved. | Align each frame check description with its corresponding sequence reservation, including all four structure functions and the sense-system model in Check 3. |
| Science rubric, Gateway 2 full-scope gap | It says dimension statements exist in no data file. `ngss-pe-dimensions.csv` now exists and is used by this sequence. | Replace the absence claim with a requirement to trace its elements into teaching and assessment evidence. |
| Science rubric S5 and “Questions for Cory” | These still require finding a science teacher before completion, while current FOUNDATION 7.3 assigns the safety-and-materials read to the safety agent. | Align both statements with the current foundation decision, preserving the required safety read. |

**Why it matters:** A writer can receive different readiness, assessment, boundary or approval instructions depending on which current document is opened.

These corrections align existing decisions. They do not require a new decision about scope or outside people.

## Order, standards, assessments and load

All 14 owned progression rows and 15 owned expectations have teaching and assessment reservations. These codes have no lettered subcodes; completeness depends on their substantive performances and dimension elements.

| Unit | Allocation by load | Assessment reservation and judgment |
|---|---|---|
| 1: Faster and harder | 15 days: six speed-energy, six collision, three shared closing days | Day 14 names an evidence explanation, testable question and collision-energy prediction for `4-PS3-1` and `4-PS3-3`. The same-object comparison is established before conclusions. |
| 2: Energy on the move | 23 days: eight transfer, six device, six resources, three closing days | Day 37 names four transfer modes, actual design-test-refine evidence and a new conversion case. The resource reservation needs finding 1. |
| 3: Waves and messages | 15 days: six wave, six communication-design, three closing days | Day 55 reserves wave-model revision, comparison of unfamiliar codes, research, proposals, peer exchange, two-condition tests and digital encoding/decoding. The telephone extension is appropriately dropped. |
| 4: The changing land | 17 days: ten weathering/erosion, five landscape history, two assessment/response days | Day 72 reserves fresh observations and evidence-based landscape explanation, including matching, fossil-bearing and deformed layers. Investigation precedes historical inference. |
| 5: Earth’s patterns and hazards | 17 days: six mapping, eight design comparison, three closing days | Day 92 reserves organized land/seafloor data and comparison of several solutions against goals, limits and likely conditions. Maps precede hazard decisions. |
| 6: Senses and structures | 24 days: five light, five sensing, nine structures, five shared closing days | Day 116 names unfamiliar light and response cases plus separate plant and animal arguments, including internal/external structures, all four functions and interacting systems. |

The heavier investigation and design components receive more time than simple code counts would suggest. I found no run clearly far over or under its stated load.

The sequence introduces energy arrows before extending them, teaches circuits before device construction, researches communication before generating codes, distinguishes erosion from weathering before interpreting canyon history, and builds the light model before the broader sensing model.

No unit exceeds 25 days, so the brief’s mid-unit assessment trigger does not apply. Unit and course-level response time is counted once. Actual items, scoring guidance and assessment timing remain later-layer evidence.

The official evidence statements support judging these as performances rather than vocabulary coverage. [Grade 4 evidence statements](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/4th_Grade%20Evidence%20Statements%20June%202015%20asterisks.pdf), [engineering evidence statements, page 5](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/K-5%20ETS%20Evidence%20Statements%20June%202015%20asterisks.pdf)

## Readiness and retrieval

| Assumed row or group | Last relevant use established by the record | Sequence treatment |
|---|---|---|
| `s3-motion-patterns`, `s3-balanced-forces` | Grade 3 | Retrieval on days 1 and 7. |
| `sk-sun-warms` | Grade 1 | Readiness in day 15’s final ten minutes; response on day 16. Correct. |
| `s3-design-problem`, `s3-environment-change-solution` | Grade 3 | Retrieval on days 24 and 30. |
| `s1-sound-vibrates` | Grade 1 for the causal vibration idea | Readiness on day 41; response on day 42. Day 17’s observation does not claim to establish that causal model. |
| `s1-signal-device` | Revisited through this year’s lid alarm, including detection at a distant observation point | Retrieval in unit 3 is justified by current-year work. The grade 3 maintenance claim is unnecessary. |
| `s3-weather-data`, `s3-fossils` | Grade 3 | Retrieval on day 57, with fossils revisited on day 67. |
| `s2-fast-slow-events` | Maintained through grade 3 fossils | Retrieval on day 57. |
| `s2-erosion-solutions` | Maintained through grade 3 weather-hazard work | Retrieval in units 4 and 5. |
| `s2-land-water-model` | Maintained through grade 3 climates | Retrieval on day 77. |
| `s2-water-where` | Grade 2; no explicit grade 3 maintenance | Readiness on day 76; response on day 77. Correct. |
| `s3-weather-hazard` | Grade 3 | Retrieval on day 83. |
| `s1-see-with-light`, `s1-light-materials` | Explicitly refreshed on day 18 this year | Retrieval on day 94. |
| `s1-parts-mimic` | Maintained through grade 3 variation work | Retrieval on days 99 and 104. |
| `s3-life-cycles`, `s3-variation-advantage` | Grade 3 | Retrieval on day 104. |

I found no sequence unit that incorrectly checks a preceding-year row or retrieves an unmaintained older row. The actual readiness checks occur immediately before their units, rather than on opening days or weeks in advance. The conflicting frame wording needs finding 3.

## Calendar, cumulative checks, candidates and shorter path

**Calendar:** The sequence and shared calendar agree. Course-level checks occur in weeks 10, 19 and 30. The first check’s response in week 11 is explicitly distinguished from its assessment week.

The named mathematics bridges cover budgets, large numbers, code rules, measurement and geometry. ELA overlap receives writing and source-note supports. Resources finish before social studies begins its regional-resource work on school day 107; hazards finish before its hazard unit begins on school day 137.

**Checks that do not repeat:** The latest unit’s skills explicitly transfer into earlier content:

- Check 1 uses unit 1 moving-toy and transport contexts.
- Check 2 uses unit 3’s water-basin setting.
- Check 3 uses unit 2’s illuminated device and unit 5’s town organisms.

Fresh evidence is named, and actual-performance portfolios are retained where paper alone would be insufficient.

**Candidates:** All six are settled. Collision sounds, the state energy profile, local landform photographs and a dated recent event each receive one day. The telephone and cut-fruit extensions are dropped with reasons and zero additional days.

**Shorter path:** Both required forms are present. The shorter-period route protects evidence, revision and cleanup. The ten unassessed fold-in days are explicitly paired:

`6→5`, `12→11`, `23→22`, `35→34`, `47→46`, `63→62`, `70→69`, `82→81`, `106→105`, `114→113`.

All ten have blank assessment cells. No required setup, assessment, response or owned part is explicitly removed. The separate 90-session route remains unresolved and is honestly distinguished from this 110-session fallback.

## Science lens checklist: scope and sequence

| Lens line | Result |
|---|---|
| Anchors are phenomena rather than topic headings | **Met.** Each unit names an observable puzzle or design problem. |
| Models are built before later use | **Met.** Introduction and revision points are named; major dependencies precede use. |
| Engineering expectations appear in units | **Met.** Unit 3 owns the full comparison expectation; units 2 and 5 develop and reuse design work. |
| Equipment has substitutes or a no-kit path | **Met at plan level for alternatives.** Household stand-ins, shared apparatus, printed evidence and limitations are stated. The separate S6 cost requirement is **missed**, finding 2. |

The sequence is consistent with EQuIP’s emphasis on connected questions, evidence-driven model development and observable student performances. This is a planning judgment, not a score for unwritten lessons. [EQuIP version 3.0, pages 2 to 3](https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf)

## Settled by the expert

These are item-level decisions for the caller to apply.

| Choice | Reason | File touched |
|---|---|---|
| Put a sourced technology-and-environment comparison inside day 33 | Completes the resource evidence reservation without adding time | Sequence and `days.csv` |
| Require the corresponding explanation on days 37 and 40 | Makes the assessed performance explicit | Sequence and `days.csv` |
| Justify unit 3’s signal retrieval through the earlier lid alarm | Current-year use is directly visible | Sequence wording; frame seam |
| Retain qualitative wave comparisons and the unnumbered strip | Keeps the task within the stated boundary | Frame |
| Add provisional six-unit costs within the existing ceiling | Cost belongs at this layer | Sequence |
| Preserve unit order, day totals and the ten named folds | No identified defect requires changing them | No allocation change |

## What is right and should remain

Preserve the collision-first energy story, circuits before construction, research before code design, two-condition solution comparisons, and observations before landscape inference. Preserve the required internal plant case, flower dissection, balanced plant and animal arguments, learned-signal memory example and unfamiliar assessment cases.

The earlier frame findings about plant coverage, engineering research and peer exchange, and wave properties affecting object motion have substantive homes in this sequence. They should not be reopened as missing.

## What I could not judge

Actual lesson navigation, assessment duration, scoring quality, classroom rotation times, purchase costs and final investigation safety cannot be established from these reservations. The sunlight and freeze-thaw fallbacks still require practical verification. `APPROACH-SCIENCE.md` remains absent, as the repository guidance acknowledges.

## Sources and source-list notes

- [Official grade 4 standards and foundation elements](https://www.nextgenscience.org/sites/default/files/AllDCI.pdf): standards architecture and assessment boundaries.
- [Grade 4 evidence statements](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/4th_Grade%20Evidence%20Statements%20June%202015%20asterisks.pdf): selected observable performances.
- [4-ESS3-1 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/4-ESS3-1%20Evidence%20Statements%20June%202015%20asterisks.pdf): finding 1.
- [Engineering evidence statements](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/K-5%20ETS%20Evidence%20Statements%20June%202015%20asterisks.pdf): research, proposals, testing and comparison.
- [EQuIP version 3.0](https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf): coherence and assessment evidence.
- [OpenSciEd collision unit](https://openscied.org/instructional-materials/4-1-energy-transfer-collisions/): comparison for developing energy ideas through observable collisions.
- [Smithsonian grade 4 engineering trainer guide, pages 18 to 19](https://ssec.si.edu/sites/default/files/Intro_Grade4Eng.pdf): comparison for connecting transfer, resources, circuits and design. Reference only; its stated licence is CC BY-NC-SA 4.0.

**For the source list:** The Smithsonian trainer guide is a useful accessible comparison. The direct EdReports K–5 criteria PDF could not be fetched, and its review-tools page timed out; this review therefore used the repository’s filed rubric rather than claiming fresh verification of those criteria.

## For Cory

- No new scope, money, people or audience decision is requested. The recommended fixes fit the existing course and materials ceiling.


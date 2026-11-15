# Independent read: science-kindergarten scope and sequence

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/sequence-science-kindergarten-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files created or changed.

## Verdict

The six-unit sequence is coherent and preserves the frame’s ownership, allocations and intended progression. Revise before unit planning: the largest risk is that some advertised assessment and materials paths omit part of the performance attached to their codes. Make those performances explicit, complete the forecasting content and unit cost estimates, and preserve the existing order.

## What I read

- The complete `docs/courses/science-kindergarten/scope-and-sequence.md`, its 64-row `days.csv`, and the course frame.
- All 11 kindergarten science progression rows, including their prerequisites, models and cross-subject leans.
- `docs/courses/CALENDAR.md` and the kindergarten calendar entries for all four subjects.
- `EXPERT.md`, the science lens, `RUBRIC-SCIENCE.md`, FOUNDATION, the shared approach, relevant ROADMAP sections, BASELINE rules 20 to 24, the glossary and sequence-writing rules.
- The standards code list and all dimension records for the owned expectations.
- Relevant source-register entries, the base-text record, earlier kindergarten science frame reads and fixes, and selected earlier sequence findings to establish recurrence.
- Live outside sources identified below.

The blind-rule exclusions were respected. Memory informed review method only; no curriculum finding rests on remembered standard wording.

## Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Did not complete: missing Python dependency `markdown`. |
| `python -X utf8 scripts/frame.py calendar` | Passed; science checks occupy weeks 14 and 29, with no reported stagger break. |
| `python -X utf8 scripts/frame.py check science-kindergarten` | Passed, zero failures: six units, 64 days. |
| `python -X utf8 scripts/plan.py check science-kindergarten` | Passed, zero sequence failures. |
| `python -X utf8 scripts/stale.py check` | Passed: 56 files, zero failures. |

The unavailable general gate does not withhold this verdict.

## Findings, most serious first

### 1. Two paths do not explicitly preserve the K-PS2-1 investigation performance

**Severity:** Major  
**LAYER:** sequence  
**REPEAT:** yes, the distinction between naming a code and eliciting its performance appeared in the earlier kindergarten social studies sequence read, finding 1.  
**Confidence:** Firm on the required performance; likely on how the current wording would be implemented.

**Location:** Scope and sequence, lines 17 and 105; `days.csv`, days 29 and 30.

**What is wrong:** Unit 1’s closing observations explicitly require children to plan and carry out investigations. The mid-year check instead promises a complete “talk-and-point battery.” Its rows mention fair comparisons but never explicitly require the child to help plan, conduct and record them.

The general no-kit path similarly substitutes picture sequences and recorded observations. It protects children’s construction performances, but does not give the same protection to the unit 1 investigation.

K-PS2-1 requires children’s participation in planning and conducting the investigation. Interpreting someone else’s test supplies different evidence. [Official K-PS2-1 evidence statement, pages 1 to 2](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/K-PS2-1%20Evidence%20Statements%20June%202015%20asterisks.pdf).

**Why it matters:** A writer could implement both descriptions faithfully, obtain correct explanations, and still lack evidence of the claimed investigation practice.

**Exact fix:**

- Amend days 29 and 30 and the mid-year description: each child helps choose the comparison and what stays the same, participates in conducting separate strength and direction trials, records an outcome with marks or pictures, and explains the result. Group investigation is appropriate, with individual evidence recorded.
- Extend line 17’s exception to investigations: retain simple physical objects for children’s own push-and-pull tests. A large paper ball, light cardboard box and tape marks can provide a minimal route.
- State that media can support interpretation and explanation but cannot replace the child’s investigation participation for this code.

Keep the existing days and the unit 1 assessment wording.

### 2. Forecasting omits the weather-pattern knowledge behind prediction

**Severity:** Moderate  
**LAYER:** sequence and standard  
**REPEAT:** yes, an omitted supporting core-idea element was the central issue in the earlier kindergarten science rerun, finding 1.  
**Confidence:** Firm.

**Location:** Unit 2 narrative and coverage table; `days.csv`, days 15 to 19 and 29 to 30.

**What is wrong:** The sequence teaches obtaining a forecast, recognizing a locally relevant warning, and preparing and responding. It does not reserve teaching or assessment of two connected ideas: some severe-weather types are more likely in particular regions, and observable weather patterns help forecasters predict events.

Choosing a local thunderstorm example does not itself teach those relationships. They appear in the official supporting core idea and evidence statement, and the regional-likelihood idea is already present in the repository’s dimension record. [Official K-ESS3-2 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/K-ESS3-2%20Evidence%20Statements%20June%202015%20asterisks.pdf).

**Why it matters:** Forecasting can become a safety-message lesson without the science explaining how useful predictions become possible.

**Exact fix:** Within day 17, add a brief, sourced picture-record comparison showing a locally relevant severe-weather pattern. Explain that forecasters use observed patterns and current information to warn communities before an event. Children ask a question and obtain the answer from the supplied media.

Add a short corresponding look-for to days 18 and 19 and the mid-year battery: the child uses the information to connect a weather pattern, a prediction and a preparation or response. No probability calculations or atmospheric mechanism is needed, and no day is added.

### 3. Course-level weather checks leave required evidence implicit

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, incomplete assessment scope recurs in the earlier kindergarten sequence review, finding 1.  
**Confidence:** Likely.

**Location:** Scope and sequence, lines 105 and 107; `days.csv`, days 29 to 30 and 62 to 63.

**What is wrong:**

| Check | Evidence not explicitly secured |
|---|---|
| Mid-year | A supported quantitative weather observation. “No counting beyond supported groups to ten” sets a limit but does not actually ask for a count. |
| Year-end | A relative-temperature pattern within the weather record. The surface-warming comparison assesses a different expectation and does not establish this weather evidence. |

The unit 2 assessment description explicitly reserves both requirements. The course-level descriptions should be equally clear because they also list K-ESS2-1. The official evidence statement includes both weather quantities and relative temperature over the day. [K-ESS2-1 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/K-ESS2-1%20Evidence%20Statements%20June%202015%20asterisks.pdf).

**Why it matters:** The course-level records could report complete coverage while overlooking a child’s difficulty with one of the taught forms of weather evidence.

**Exact fix:**

- In days 29 and 30, explicitly ask each child to count a selected weather group of at most ten with support and use the picture rows to compare monthly frequencies.
- In days 62 and 63, explicitly ask each child to describe and share a morning/afternoon warmer-or-cooler pattern from actual weather records.
- Add both reservations to the corresponding prose descriptions.

Retain teacher-labelled larger totals and accept what the records show rather than imposing a cooler-morning rule.

### 4. Unit cost estimates are deferred beyond the layer that requires them

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** new among the relevant earlier reports consulted.  
**Confidence:** Firm.

**Location:** Scope and sequence, line 17; all six unit descriptions.

**What is wrong:** The sequence names materials and refers to the settled annual allowance, but gives no unit cost estimates. It explicitly postpones itemization to unit plans. The science rubric assigns costs to this layer through S6 and requires each unit to state its cost.

**Why it matters:** The annual allowance cannot yet be checked against quantities, reuse or the minimal physical materials needed to preserve required performances.

**Exact fix:** Add a six-row estimated materials-cost table stating:

- Assumed class size and quantities.
- Existing classroom stock assumed.
- New purchases and consumables.
- Reuse across units.
- Estimated additional cost per unit and annual total.

Use sourced estimates and count reusable purchases once. Keep the already settled annual allowance; this finding does not request new spending.

### 5. The active science rubric retains two superseded status statements

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale rubric status statements appeared in the earlier kindergarten science rerun, findings 4 and 5.  
**Confidence:** Firm.

**Location:** `docs/RUBRIC-SCIENCE.md`, Gateway 2 coverage row, S5 and “Questions for Cory.”

**What is wrong:**

- The coverage row says practice, core-idea and crosscutting-concept statements exist in no data file. `data/standards/ngss-pe-dimensions.csv` now exists and is used by this sequence.
- The safety provisions still require a science teacher and describe the absence of people as a completion barrier. Current FOUNDATION section 7.3 and the kindergarten frame specify a safety-agent read against published guidance.

The stale checker passes because these contradictions are outside the notes it recognizes.

**Why it matters:** Later reviewers could duplicate completed data work or impose a superseded review requirement.

**Exact fix:** Update the rubric to acknowledge the dimension file while retaining the need to verify its use in instruction and assessment. Replace the superseded science-teacher requirement with FOUNDATION’s current safety-agent requirement. Preserve the separate human pilot requirements that FOUNDATION still retains.

## Order, standards and load

The teaching order is sound apart from the forecasting omission above.

| Unit | Days | Teaching days before the two closing observation days | Owned expectations | Judgment |
|---|---:|---:|---|---|
| 1. Pushes and pulls | 9 | 7 | K-PS2-1 | Habits, strength comparisons, direction and contact evidence build coherently. Finding 1 concerns alternative paths. |
| 2. Weather watch | 10 | 8 | K-ESS2-1; K-ESS3-2 | Record interpretation precedes forecasting. Complete the forecasting content in finding 2. |
| 3. Ramps and targets | 9 | 7 | K-2-ETS1-1; K-PS2-2 | Problem definition precedes construction and results-based revision. |
| 4. Living things | 12 | 10 | K-LS1-1; K-ESS3-1; K-ESS2-2 | Needs patterns precede place relationships and environmental arguments. |
| 5. Sunlight warms | 11 | 9 | K-PS3-1; K-PS3-2 | Surface observations precede shade design, testing and improvement. |
| 6. Caring for our place | 7 | 5 | K-ESS3-3 | Baseline, implementation and follow-up precede communication on a new case. |

All 11 owned expectations have teaching and assessment placements. The four needs patterns, humans and resource relationships, plant/animal/human environmental changes, four surface materials, and child-built shade are explicitly reserved. There are no letter-suffixed owned expectation codes to locate separately. These judgments were checked against the [kindergarten evidence statements](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/Kindergarten%20Evidence%20Statements%20June%202015%20asterisks.pdf) and [engineering evidence statements](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/K-5%20ETS%20Evidence%20Statements%20June%202015%20asterisks.pdf).

No allocation is demonstrably far over or under its load. Unit 1 also establishes investigation habits; units 4 and 5 appropriately receive more time for connected explanations and construction. The daily weather routine adds disclosed time outside the numbered meetings.

## Other required checks

| Requirement | Result |
|---|---|
| Readiness versus retrieval | Met. Every kindergarten `assumes` cell is empty. No earlier-grade readiness row exists, and no readiness assessment is scheduled. |
| Same-year retrieval | Met. Units 2 to 6 retrieve previously introduced habits, ideas or models inside days. No older prerequisite is incorrectly treated as retrieval. |
| Model order | Met. Cause-effect precedes later uses; patterns precede living-needs work; design precedes shade work; the evidence sentence precedes units 5 and 6. |
| Mid-unit assessments | Not applicable. No unit exceeds 25 days. |
| Response counted once | Met. Each unit reserves its final ten minutes once; each course-level check has one separate respond day. |
| Checks avoid immediate repetition | Met at reservation level. Mid-year applies unit 3 skills to earlier motion/chart contexts; year-end applies unit 6 communication to earlier resource contexts. |
| Calendar | Met. Checks occupy weeks 14 and 29. The 29-week frequency difference is disclosed and referred to Cory. |
| Cross-subject leans | Met. Early comparison, counting and questioning have explicit bridges. Later drawing and communication uses follow the calendar’s relevant ELA units. |
| Shorter period | Present. The 20-minute route protects essential evidence and response, but its assessment timing remains unverified. |
| Shorter year | Met. Named fold-ins preserve owned content; all ten listed fold-in days have blank `assess` cells. |
| Source map | Not applicable. Kindergarten science has no base text. |

All candidate cells are settled:

| Unit | Decision and day cost |
|---|---|
| 1 | Keep before-and-after descriptions, embedded with zero added days. |
| 2 | Keep the relative-temperature investigation, one existing day. |
| 3 | Keep the second classroom problem, one existing day. |
| 4 | Drop the animal/feeder commitment; plants and animal media retain the content. |
| 5 | Drop the extra ice-melting comparison; matched-surface evidence retains the content. |
| 6 | Keep the follow-up count, one existing day, with baseline embedded in day 55. |

## Science lens checklist: scope and sequence

| Checklist line | Result |
|---|---|
| Anchors are phenomena or design problems rather than topics | **Met.** All six identify an observable event, record or problem. |
| No model is used before its introduction | **Met.** The stated order preserves the necessary introductions. |
| Engineering expectations appear in a unit | **Met.** Problem definition is owned in unit 3 and reused later. |
| Equipment has substitutes or a no-kit path | **Missed in part.** Alternatives exist, but finding 1 identifies an investigation performance the generic media path does not preserve. |

At this layer, S6 also remains incomplete because unit costs are absent. Element coverage remains incomplete where findings 1 to 3 apply.

## What is right and should remain

Preserve the six units, 64 meetings, unfamiliar closing cases, revised class representations, accessible spoken and drawn evidence, and explicit response allocations.

Keep the earlier corrections: weather records begin on school day 1; archived months address the early comparison; fall photographs protect the winter anchor; humans, air and land resources appear in the place model; and larger counts remain teacher-supported. Young children’s capacity for scientific reasoning supports retaining this substantive work with appropriate guidance. [Taking Science to School, chapter 3, read in part](https://www.nationalacademies.org/read/11625/chapter/5).

## Settled by the expert

These are recommendations for the caller to apply.

| Choice | Reason | File affected |
|---|---|---|
| Retain current unit order and allocations | No demonstrated prerequisite or load fault requires moving days | Sequence and days.csv |
| Require children’s investigation participation in the mid-year and minimal-materials paths | Preserves K-PS2-1’s practice | Sequence; days 29 and 30 |
| Add the forecasting-pattern connection within day 17 | Completes existing ownership without adding a day | Sequence; days 17 to 19, 29 and 30 |
| Make weather count and temperature evidence explicit in course checks | Removes ambiguity without increasing scope | Sequence; course-level check rows |
| Add unit estimates within the existing annual allowance | Makes materials feasibility reviewable | Sequence |
| Preserve all named fold-ins | They remove repetition without cutting assessed content | Sequence |
| Update active rubric status statements | Aligns the review guide with current data and FOUNDATION | Science rubric |

## What I could not judge

Finished assessment items, scoring guidance, local weather records, media rights, actual costs and final investigation safety remain unwritten or unverified.

Assessment timing also needs a concrete rotation plan. For the shared approach’s class of 30, two 30-minute unit observation meetings leave 50 minutes before the reserved response, about 100 seconds per child if handled serially. Course-level checks provide two minutes per child, or 80 seconds with 20-minute periods. Parallel work may make this feasible, but the eventual tasks must demonstrate it.

The science approach page remains absent. No finished-course score or classroom-effectiveness claim is warranted.

## Outside sources and access limits

- [K-PS2-1 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/K-PS2-1%20Evidence%20Statements%20June%202015%20asterisks.pdf): investigation performance.
- [K-ESS2-1 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/K-ESS2-1%20Evidence%20Statements%20June%202015%20asterisks.pdf): quantitative and temperature-pattern evidence.
- [K-ESS3-2 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/K-ESS3-2%20Evidence%20Statements%20June%202015%20asterisks.pdf): regional weather patterns and forecasting.
- [EQuIP science rubric](https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf): coherence and observable assessment evidence.
- [Appendix F](https://www.nextgenscience.org/sites/default/files/resource/files/Appendix%20F%20%20Science%20and%20Engineering%20Practices%20in%20the%20NGSS%20-%20FINAL%20060513.pdf) and [Appendix G](https://www.nextgenscience.org/sites/default/files/resource/files/Appendix%20G%20-%20Crosscutting%20Concepts%20FINAL%20edited%204.10.13.pdf): selected kindergarten practice and concept passages.
- [OpenSciEd kindergarten forces overview](https://openscied.org/instructional-materials/k-3-forces-motion/): reference comparison of investigation before design, not copied material.
- [South Carolina kindergarten weather resource](https://ed.sc.gov/sites/scdoe/assets/File/instruction/standards/Science/Units/K-Earth-Science--Exploring-Weather-Patterns.pdf): comparison of weather-data and picture-record organization, not an alternative standards anchor.

The linked external K-5 review-criteria PDFs were inaccessible; their requirements here rest on the repository rubric. Additional Smithsonian and Rhode Island comparisons were blocked, and the Utah textbook exceeded the browser’s size limit. No finding depends on those unread materials.

**For the source list:** Record the accessible South Carolina comparison and the access limitations above.

## For Cory

- **Schedule:** Confirm whether the calendar’s occasional three-meeting weeks replace the settled two-meeting weekly description, or have the frame and calendar reconciled. The sequence already discloses the difference.

**Verdict:** Revise locally before unit planning. **Finding count:** 5. **Report path:** `docs/reviews/sequence-science-kindergarten-2026-11-14.md`, supplied here, not created.


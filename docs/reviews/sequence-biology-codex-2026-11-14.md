# Independent first read: Biology scope and sequence

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/sequence-biology-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files changed.

## Verdict

The sequence has a coherent unit order, sensible allocations and a calendar that fits, but it needs targeted revision before unit planning. The largest risk is its blanket exemption from readiness checks, followed by several complete-code claims whose named performances omit required evidence. Keep the ten units and 160 days while correcting prerequisite treatment, completing the performance reservations and adding provisional materials costs.

## What I read

- `docs/agents/EXPERT.md`, the science lens and `docs/RUBRIC-SCIENCE.md`.
- The complete biology scope and sequence, frame and all 160 day records.
- All 24 biology progression rows, their earlier science prerequisites, and relevant intervening uses in grades 7 and 8.
- Relevant earlier mathematics rows and selected Grade 8 science day records to check whether prerequisites actually remained in use.
- `docs/courses/CALENDAR.md` and the Grade 9 calendar records across subjects.
- The standards dimension file, relevant literacy standards, foundation, glossary, shared approach, source register, base-text policy, relevant roadmap passages and BASELINE rules 20 to 24.
- Earlier biology frame reports, the biology writing handoff, relevant Grade 7 and Grade 8 sequence findings, and the high school sequence fixes report for repeat classification.
- The primary outside sources linked below.

The prohibited files were not opened. Personal memory informed review technique only; no curriculum finding rests on unverified memory. `docs/APPROACH-SCIENCE.md` is absent.

## Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Biology reported zero failures; the global run subsequently encountered a missing chemistry sequence and stopped because Python lacks `markdown`. |
| `python -X utf8 scripts/frame.py calendar` | Passed. |
| `python -X utf8 scripts/frame.py check biology` | Passed: zero failures, 10 units, 149 unit days and 11 course-level days. |
| `python -X utf8 scripts/stale.py check` | Passed: 56 files, zero marked failures. |

The incomplete global gate does not withhold this biology verdict.

## Findings, most serious first

### 1. Five units retrieve older prerequisites that require readiness before opening

**Severity:** Major  
**LAYER:** sequence, frame, progression  
**REPEAT:** yes, prerequisite classification and timing recur in the Grade 7 science sequence review, finding 1  
**Confidence:** firm

**Location:** Scope and sequence, units 3, 4, 8, 9 and 10; corresponding opening day notes; biology frame, Seams and Models carried; relevant progression handoff notes.

**What is wrong:** The frame counts intervening idle grades rather than applying this run's rule based on the grade of last use. Work last used in grade 7 is two grades back for Biology, so it needs readiness unless grade 8 or earlier Biology work actually used it.

The following older returns remain under retrieval:

| Receiving unit | Prerequisite requiring readiness | Last evidenced use | Exact placement |
|---|---|---|---|
| 3 | `s7-reactions-atoms`, `s7-food-molecules`, and matter-cycle | Grade 7 | Final ten minutes of day 25 |
| 4 | `s7-ecosystem-matter-energy` and food-web | Grade 7 | Final ten minutes of course-level respond day 46 |
| 8 | Plate-motion knowledge from `s6-plate-evidence`, maintained by `s7-resource-distribution` | Grade 7 | Final ten minutes of day 112 |
| 9 | `s7-biodiversity-solutions` and `s7-human-impact-design` | Grade 7 | Final ten minutes of day 123 |
| 10 | `s7-population-consumption` | Grade 7 | Final ten minutes of day 140 |

Unit 3's organism-level processes do not establish that ecosystem feeding relationships have already been retrieved or checked. Conversely, matter-cycle becomes legitimate same-year retrieval after unit 3.

Several grade 7 rows **do** remain appropriate retrieval:

- Body systems through grade 8 senses.
- Cellular growth and photosynthesis through grade 8 cell and growth work.
- Reaction-energy through the grade 8 energy argument.
- Resources and ecosystem disruption through grade 8 natural selection.

Unit 10 also correctly retrieves human-impact design after unit 9. Grade 8 inheritance uses Punnett squares and probability, so the grade 7 identifier alone does not establish that day 85's probability retrieval is misplaced.

**Why it matters:** The current blanket “no readiness check” instruction lets a writer discover older gaps only after dependent modeling begins. Separating prior learning in the dimensions is consistent with [EQuIP Science, instructional supports](https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf); the exact timing requirement comes from this run's brief.

**Exact fix:** Make the five reservations above, keeping each receiving unit's first-day hook clean. Rebalance the preceding response session so readiness occupies its final ten minutes rather than extending the session or counting response twice. Name the support selected by each result and place it before dependent work. Replace the frame and progression's conflicting last-use language.

This disagrees with the earlier biology frame reviews' acceptance of retrieval for all grade 7 returns. Their blanket conclusion does not satisfy the current brief.

### 2. Complete-code claims exceed three named performance reservations

**Severity:** Major  
**LAYER:** sequence, frame, standard  
**REPEAT:** yes, incomplete performance reservations recur in the Grade 8 science sequence review, finding 1  
**Confidence:** firm on the explicit exclusion and reservation gaps

**Locations:** Scope and sequence lines 9 and 65; frame line 173; days 84, 89, 93, 137 and 156; standards coverage entries for inheritance and river-design research.

**What is wrong:** The plan's general instruction to cover every part does not resolve these specific omissions:

| Claimed work | Gap | Exact fix |
|---|---|---|
| Defending a variation claim, `HS-LS3-2`; accompanying `WHST.9-10.1` | Day 84 and the frame explicitly say counterclaims are not required. Making a supported claim does not alone demonstrate defending it against critique. | Replace that exclusion with a short, modeled comparison against a supplied alternative interpretation. Students weigh the evidence and defend the stronger claim. Reserve independent evidence of this on days 93 and 156. |
| Complete `HS-LS3-3`, including the connections the sequence explicitly claims | Day 89 teaches reciprocal relationships among technology, science and society, but neither day 93 nor day 156 names a prompt or retained product assessing them. | Identify day 89's written analysis as an assessed portfolio component on day 93. Add a brief new-case application to day 156's reservation. |
| `WHST.9-10.8` on day 137 | Supplied-source research, notes and citations do not establish effective advanced searching or assessment of each source's usefulness. | Reserve a search-and-selection task before report drafting: students refine a query, compare authoritative sources for usefulness, then integrate and cite selected evidence. An account-free, searchable supplied collection can preserve the offline route. |

For the first row, the official observable performance explicitly includes responding to counterclaims and critique: [HS-LS evidence statements, PDF page 28](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/HS%20LS%20Evidence%20Statements%20June%202015%20asterisks.pdf). The accompanying writing standard also includes counterclaims, while its research standard requires advanced searching and source-usefulness judgments: [official grades 9 to 10 technical writing standards](https://www.thecorestandards.org/ELA-Literacy/WHST/9-10/).

The technology and society connections appear in both the repository dimension file and the [official HS-LS3-3 foundation](https://www.nextgenscience.org/pe/hs-ls3-3-heredity-inheritance-and-variation-traits). Assessing these on every claimed full-code check follows this sequence's own stated rule.

**Why it matters:** A unit writer can follow the specific daily directions while omitting work that the general coverage promise claims. That produces incomplete evidence without an obvious missing code.

**Exact fix:** Apply the reservations above within the existing days, update the coverage descriptions, and retain the disciplinary writing bridges. A short scientific defense is sufficient; there is no need to wait for ELA's later argument unit or add a separate essay.

### 3. All ten unit costs are deferred beyond the layer that requires them

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, the same omission appears in the Grade 7 science sequence review, finding 4  
**Confidence:** firm

**Location:** Materials, tools and sources, especially scope and sequence line 164; all ten units.

**What is wrong:** Supplies and alternatives are named, but quantities and actual costs are deferred to unit planning. No provisional unit costs are supplied. The science rubric explicitly assigns **S6 costs** to the scope-and-sequence layer.

**Why it matters:** The reader cannot evaluate the proposed low-cost route without knowing whether balances, eye protection, alcohol, printing and other supplies are assumed stock or new purchases. This also affects the minimum practical route needed for unit 1's investigation.

**Exact fix:** Add a provisional ten-unit cost table for a stated classroom size, with a one-child note. Separate consumables, reusable equipment counted once, printing, assumed stock and incremental unit costs. Give the basis and uncertainty of estimates; do not call data-only units cost-free when they require printing or device access.

Refine those estimates during unit planning. This recommendation authorizes no purchase.

### 4. Unmarked rubric statements contradict the current evidence and review policy

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale rubric status was identified in the earlier biology frame rerun  
**Confidence:** firm

**Location:** `docs/RUBRIC-SCIENCE.md`, Gateway 2 inventory, S5 and Questions for Cory.

**What is wrong:**

- The rubric says dimension statements exist in no data file. `data/standards/ngss-pe-dimensions.csv` now exists and is explicitly used by this sequence.
- S5 and Questions for Cory still require a science teacher's safety read and describe the absence of people as a completion barrier. The current foundation section 7.3 and biology frame specify a source-studying safety agent.

**Why it matters:** Reviewers can miss the available element-level evidence or revive an outside-person requirement already changed by Cory. The marked stale-note gate does not detect either statement.

**Exact fix:** Point the inventory to the dimension file and distinguish its existence from completed course-level tracing. Replace the superseded safety-reader wording with the current foundation requirement, retaining the actual safety and materials review.

Do not reopen the people decision through this report.

## Order and days by load

No further redistribution is justified by this read.

| Unit | Days | Owned expectations | Order and load judgment |
|---|---:|---:|---|
| 1 | 13 | 2 | Hierarchy precedes feedback interpretation; repeated investigation sessions justify the allocation. |
| 2 | 12 | 2 | Protein function precedes differentiation and organism repair. |
| 3 | 18 | 4 | Separates photosynthesis, respiration, oxygen contrasts and biosynthesis revision before integration. |
| 4 | 11 | 2 | Uses unit 3's processes before ecosystem budgets and reservoir transfers. |
| 5 | 18 | 4 | Gives five opening sessions to the new computational model and three focused sessions to group behavior. |
| 6 | 16 | 3 | Questions and variation sources precede probability, distributions and environmental comparisons. |
| 7 | 18 | 4 | Evidence and selection precede adaptation and protected communication work. |
| 8 | 11 | 2 | Uses photosynthesis and selection before reciprocal Earth-life arguments. |
| 9 | 17 | 4 | Protects testing and two refinement opportunities before the report. |
| 10 | 15 | 3 | Separates resource-model construction, species-model revision and cross-system testing. |

The 24 skill rows are not treated as equal loads. Unit 9's two rows contain four expectations; unit 10's single row contains three substantial performances. Those distinctions are reflected in the days.

## Other required checks

| Requirement | Result |
|---|---|
| End-of-unit coverage | All 30 owned expectations have teaching and assessment locations. Finding 2 identifies incomplete performance reservations. |
| Lettered owned parts | The owned science expectations are unlettered. The accompanying literacy standard has lettered requirements relevant to finding 2. |
| Mid-unit assessments | None required: no unit exceeds 25 days. |
| Response counted once | Met in the day records. Readiness fixes must preserve that accounting. |
| Course-level checks do not repeat | Met in the written reservations. Check 1 applies unit 3 skills to earlier transport/repair content; check 2 applies unit 5 skills to earlier river content; the final check claims no unit 10 codes. |
| Calendar | Checks occupy weeks 9, 16 and 32, matching the shared calendar. Grade 9 has no additional stagger restriction. |
| Same-year leans | Calendar availability supports the later math demands. Day 5 supplies concurrent graphing instruction; day 60 teaches the update rule before exponentials; ELA bridges are named. Finding 2 corrects one bridge's excessive exclusion. |
| Writing load | Biology products finish in weeks 22 and 28, apart from the named ELA pieces and history argument. |
| Candidate cells | All ten cells are settled: 20 elements retained with named sessions and zero additional days. |
| Shorter period | A usable adaptation strategy is stated, including preparation, paired reporting and protected evidence. Actual procedure timing remains untested. |
| Year ten days short | Ten named fold-ins reduce 160 meetings to 150 without deleting assessment days or the named sole performance evidence. |
| Source map | Not applicable: Biology has no base text under the source policy. |
| Stale notes | Marked check passed; finding 4 records additional unmarked contradictions. |

## Science lens checklist: scope-and-sequence layer

| Lens line | Result |
|---|---|
| Anchor is a phenomenon rather than a topic | **Met:** all ten units have observable puzzles or design problems. |
| A model is used before the unit builds it | **Missed in prerequisite preparation:** finding 1. Within-year model development otherwise precedes dependent use. |
| Engineering expectations appear in no unit | **Met:** units 9 and 10 reserve definition, comparison, testing and refinement. |
| Equipment is assumed without a substitute or no-kit path | **Met for named alternatives; costs missed:** finding 3. The plan correctly distinguishes practical and computational execution from supplied-data or paper evidence. |

## What is right and should remain

- The body-to-cell, matter-and-energy, ecosystem, inheritance, evolution and design order.
- Separate matter and energy accounting, including detrital pathways.
- The tracer-driven biosynthesis revision and oxygen-controlled comparison.
- Positive and negative feedback, with limits on amplification.
- Protected communication, design refinement and simulation-construction time.
- Nonhuman genetics examples, privacy protections, food-grade seeds and explicit hazard controls.
- Honest statements that supplied data cannot demonstrate investigation execution and paper reasoning cannot alone demonstrate computer-model construction.

The public course descriptions from [OpenSciEd](https://openscied.org/on-demand-hub/how-are-traditional-biology-topics-organized-in-openscied-high-school-biology/) and [BSCS](https://bscs.org/educator_resource/bscs-biology-understanding-for-life/) provide contrasting coherent organizations. Neither establishes a reason to replace this plan's order.

## Settled by the expert

These are item-level recommendations for the caller to apply.

| Choice | Reason | Files affected |
|---|---|---|
| Keep ten units, 149 unit days and 11 course-level days | No demonstrated need for a scope or allocation change | Biology frame, sequence and days |
| Place readiness at the ends of days 25, 46, 112, 123 and 140 | Checks older prerequisites immediately before use and preserves opening hooks | Sequence and days; matching handoff notes |
| Keep retrieval for prerequisites demonstrably used in grade 8 or earlier Biology | Last use matters more than the identifier's grade | Frame and sequence |
| Require a brief defense against an alternative interpretation in unit 6 | Completes the claimed science and writing performances | Frame, days 84 and 93, final check |
| Explicitly retain the technology/science/society analysis as assessment evidence | Makes the existing teaching reservation observable | Coverage table and days 89, 93 and 156 |
| Complete the river research reservation with searching and usefulness judgments | Notes and citations alone do not carry the claimed research code | Unit 9 day reservations |
| Add provisional costs now | S6 assigns costs to this layer | Sequence materials section |
| Update dimension-file and safety-reader status | Current evidence and foundation settle these corrections | Science rubric |

## For Cory

- No new scope, audience, spending or outside-person decision is required by these corrections.

## Limits and sources

This review judges the planning contract. It cannot establish actual lesson timing, final item coverage, scoring quality, simulation behavior or permissions for data packs not yet selected. Those require the later materials. No finished-course rubric score is assigned.

Sources opened live:

- [Official high school standards](https://www.nextgenscience.org/sites/default/files/HSDCI.pdf): foundation elements and assessment boundaries.
- [Life science evidence statements](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/HS%20LS%20Evidence%20Statements%20June%202015%20asterisks.pdf): observable student performances, particularly defending variation claims.
- [Official technical writing standards](https://www.thecorestandards.org/ELA-Literacy/WHST/9-10/): counterclaims, research and searching.
- [EQuIP Science version 3](https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf): prior learning, coherence and observable evidence.
- [High school science evidence guide](https://cozy-dream-721ab6aab0.media.strapiapp.com/Science_20_High_20_School_20_Evidence_20_Guide_2_0_9d2058e4c2.pdf): selected assessment, practice-element and safety passages.
- The two developer course descriptions linked above: comparison of organization only, not evidence that this sequence works.

**For the source list:** The high school evidence guide was accessible through the current official review-tools page. Add its direct link and record the selected passages read.

**Verdict:** Revise before unit planning. **Finding count:** 4 consolidated findings. **Report path:** `docs/reviews/sequence-biology-2026-11-14.md`, supplied here, not written.


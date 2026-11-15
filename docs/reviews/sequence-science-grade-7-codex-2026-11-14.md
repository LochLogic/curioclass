# Independent first read: Science, Grade 7 scope and sequence

**Date:** 2026-11-14  
**Report path:** `docs/reviews/sequence-science-grade-7-2026-11-14.md`  
**Delivery:** Complete report supplied below. No files created or changed.

## Verdict

Revise before unit planning. The six-unit storyline, ownership, base order and calendar are sound, but several readiness decisions and assessment reservations can produce claims of complete performance without the necessary preparation or practical evidence. Keep the order and 160-day structure while correcting those reservations and supplying provisional materials costs.

## What I read and checked

- `docs/agents/EXPERT.md`, the science lens and `docs/RUBRIC-SCIENCE.md`.
- The complete Grade 7 scope and sequence, all 160 day records, the frame and all 101 source-map records.
- All 18 owned science progression rows, their earlier prerequisites, relevant intervening uses and model handoffs.
- `docs/courses/CALENDAR.md`, the Grade 7 calendar records and relevant Grade 7 ELA frame passages.
- The foundation, shared approach, relevant roadmap passages, BASELINE rules 20 to 24, glossary, planning instructions, science source register and base-text record.
- Earlier Grade 7 frame reports and fixes, relevant science progression findings, and earlier science sequence findings for repeat classification.
- The primary sources linked below.

The prohibited files were not opened. Memory informed the review method only; no finding relies on an unverified memory-derived curriculum fact.

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Initially stopped because default Python lacks `markdown`; the unchanged checker subsequently passed using the existing dependency directory, with bytecode writing disabled |
| `python -X utf8 scripts/plan.py check science-grade-7` | Zero failures |
| `python -X utf8 scripts/frame.py calendar` | Passed; science checks in weeks 14 and 32 |
| `python -X utf8 scripts/frame.py check science-grade-7` | Zero failures; 156 unit days and four course-level days |
| `python -X utf8 scripts/stale.py check` | 56 files, zero failures |

## Findings, most serious first

### 1. Earlier-year use is sometimes claimed before the first older return has received readiness

**Severity:** Major  
**LAYER:** sequence, frame, progression  
**REPEAT:** yes, prerequisite classification and timing recur in the Grade 5 science sequence review, finding 2  
**Confidence:** firm

**Location:** Scope and sequence, units 1, 3 and 4 and “For the lead”; day records 7, 10, 58, 68, 69 and 88.

**What is wrong:** The sequence correctly applies readiness to several older returns, but leaves others under retrieval or treats continued use of a crosscutting concept as continued use of the whole content row.

| First receiving unit | Earlier row or content | Last evidenced use before this year | Current treatment | Required correction |
|---|---|---|---|---|
| 1 | `s5-identify-materials` | Grade 5 | Revisited on day 7, then used to justify later retrieval | Include in the start-of-year readiness check |
| 1 | `s5-new-substances` | Grade 5 | Revisited on day 10, then used to justify later retrieval | Include in the start-of-year readiness check |
| 3 | Matter-cycle knowledge from `s5-matter-movement` | Grade 5 | Retrieval on day 58, described as a model reminder | Check before unit 3 opens |
| 4 | `s5-plant-matter` | Grade 5 for the air-and-water matter argument | Retrieval, because grade 6 carries structure and function | Add the content prerequisite to day 68 readiness |
| 4 | `s4-energy-resources` | Grade 5 through `s5-protect-resources` | Revisited on day 88 to establish later same-year use | Add to day 68 readiness |

The Grade 6 cells row carries structure and function. It does not establish continued use of the specific argument that air and water supply plant matter. Likewise, first using an older row during this year makes later retrieval legitimate, but does not retrospectively satisfy readiness at that first return.

The requirement to identify prior learning separately in the three dimensions supports this distinction. [EQuIP Science rubric, II.C](https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf)

**Why it matters:** A writer can assume older content is secure because a related model label survived. Missing knowledge is then discovered after dependent work has begun.

**Exact fix:**

- Put material identification and new-substance readiness in the start-of-year check, keeping day 1’s hook clean under this run’s instruction.
- Reserve day 41’s final ten minutes for the matter-cycle readiness needed by unit 3. Rebalance unit 2’s assessment evidence across its existing portfolio and final task, preserving response and every assessed part. Do not simply append ten minutes.
- Expand day 68 readiness to include plant matter and energy-resource content alongside food energy from sunlight.
- Name the targeted support selected by each result within the receiving unit.
- Replace the conflicting frame and progression exemption language with this run’s last-use rule.

Keep day 96’s correctly classified readiness for animal behavior, environmental disruption and resource protection. Their recorded earlier uses remain too old for retrieval alone.

### 2. Two checks claim complete codes before required explanatory work is scheduled

**Severity:** Major  
**LAYER:** sequence  
**REPEAT:** new, this timing defect was not identified in the earlier reports read  
**Confidence:** firm

**Location:** Day 13, days 18 to 20, day 113 and days 118 to 119; scope and sequence assessment descriptions.

**What is wrong:**

| Check | Claimed coverage | Required work scheduled later |
|---|---|---|
| Day 13 | `MS-PS1-2` | The explanation connecting changed properties to rearranged atoms is developed on days 18 to 20 |
| Day 113 | Every part of `MS-LS2-4` | Explicit reasoning about a small system change producing a large population change appears on day 119 |

For `MS-PS1-2`, the official observable performance includes explaining the property change through atomic rearrangement. Comparing all six permitted properties does not supply that explanation. [MS-PS1-2 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/MS-PS1-2%20Evidence%20Statements%20June%202015%20asterisks.pdf)

For `MS-LS2-4`, the evidence statement includes the magnitudes of component and population changes and reasoning about disproportionate effects. [MS-LS2-4 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/MS-LS2-4%20Evidence%20Statements%20June%202015%20asterisks.pdf)

**Why it matters:** A writer must either assess untaught reasoning or quietly reduce “every part” to the components already taught.

**Exact fix:**

- Retain day 13’s base property-evidence checkpoint as explicitly partial formative evidence. Remove its full-code assessment claim, including the full-code assessment reservation in the day record. Unit 1 is under 25 days, so it does not require a separate complete-code mid-unit assessment. Day 22 retains full coverage after atomic modeling.
- Before day 113, add an explicit comparison of a small environmental change and a larger population response to the existing local before-and-after work on days 105 to 106. Include evidence magnitude and an alternative interpretation. Day 119 then extends that reasoning through the later ecosystem model.
- State those components in day 113’s task reservation rather than relying on “every part” alone.

These changes preserve the base lesson order and add no day.

### 3. The no-kit route cannot supply the complete practical evidence claimed for the thermal device

**Severity:** Major  
**LAYER:** sequence  
**REPEAT:** yes, supplied-data substitutes being credited as practical performance recur in the Grade 5 science sequence review, finding 3  
**Confidence:** firm

**Location:** Unit 2; day records 35, 39 to 41 and 67; Tools, supplies and access.

**What is wrong:** The sequence honestly calls the no-kit route weaker, but days 41 and 67 still claim every part of `MS-PS1-6` through a prior tested-device portfolio. On the no-kit route, students can reach those days having interpreted supplied trials without constructing and physically testing their own solution.

The official observable performance requires construction, testing and modification. A supplied trial table does not establish that a student performed those actions. [MS-PS1-6 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/MS-PS1-6%20Evidence%20Statements%20June%202015%20asterisks.pdf)

**Why it matters:** The record can show complete achievement for a performance that was never observed. Calling the substitute weaker does not resolve the missing evidence.

**Exact fix:**

- Define the minimum supervised materials route that retains construction, an initial test, modification and retest within days 35 and 39 to 40.
- Require identifiable evidence of each student’s participation and reasoning in that practical cycle.
- On the supplied-data-only route, record construction and physical testing as **not yet observed**. Do not award a complete-code result from that portfolio.
- Carry this distinction into both day 41 and day 67 assessment descriptions and the materials-cost table.

The calcium chloride and ammonium chloride choice itself is not a standards defect: the official clarification names those examples. [MS-PS1-6](https://www.nextgenscience.org/pe/ms-ps1-6-matter-and-its-interactions)

### 4. All six unit costs are deferred beyond the layer that requires them

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, the same omission appears in the Grade 5 science sequence review, finding 4  
**Confidence:** firm on the omission

**Location:** Tools, supplies and access, especially scope and sequence line 132; all six units.

**What is wrong:** The plan names equipment and alternatives but explicitly leaves local costs to unit planning. The science rubric assigns S6 costs to the scope-and-sequence layer.

**Why it matters:** Thermometers, eye protection, gloves, indicators and reusable containers have different quantity and reuse assumptions. Without those assumptions, the proposed low-cost route and minimum practical route cannot be judged.

**Exact fix:** Add six provisional unit estimates for a stated classroom size, with a one-child note. Separate:

- Assumed classroom stock.
- New reusable equipment, counted once.
- Consumables and quantities.
- Additional cost for the minimum practical route.
- The supplied-data alternative and its performance limitations.

Use dated estimates and identify uncertainty. Estimating costs does not authorize purchases.

### 5. Active control documents still contradict current data and review requirements

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, these rubric contradictions recur in the Grade 5 science sequence review, finding 5  
**Confidence:** firm

**Location:** `docs/RUBRIC-SCIENCE.md`, Gateway 2 coverage status, S5 and Questions for Cory.

**What is wrong:** The stale gate passes, but the rubric still says dimension statements exist in no data file, despite `data/standards/ngss-pe-dimensions.csv`. It also requires a science teacher’s safety read and says no course can finish until people are found, while current FOUNDATION 7.3 assigns that content review to the safety agent.

**Why it matters:** Later writers receive conflicting instructions about available coverage evidence and the required review route.

**Exact fix:** Acknowledge the dimension file while retaining the requirement to trace its elements into teaching and assessment. Align the safety-review wording with current FOUNDATION 7.3, preserving the separately required human pilot activities.

The frame and progression readiness wording should be corrected through finding 1, rather than left as an unresolved exception.

## Order, coverage and load

The overall progression is coherent: property evidence precedes atomic explanations; reactions support digestion and respiration; respiration supports photosynthesis; ecosystem cycling supports population dynamics; those models support resource and impact design.

| Unit | Days | Owned rows / expectations | Assessment reservations | Load judgment |
|---|---:|---:|---|---|
| 1 | 23 | 1 / 2 | 13; end 22; response 23 | Sustained development is justified; distinguish the early partial checkpoint |
| 2 | 18 | 2 / 2 | End 41, response inside day | Tightest practical and assessment budget; findings 1 and 3 apply |
| 3 | 25 | 3 / 3 | Mid 54; end 65; response 66 | Molecular completion, interacting systems and cellular reactions have distinct runs |
| 4 | 28 | 3 / 3 | Mid 82; end 95; response 96 | Photosynthesis receives the longest development; synthetic-material work has four named periods |
| 5 | 32 | 5 / 5 | Mid 113; response 114; end 127; response 128 | Five expectations and two support periods justify the allocation |
| 6 | 30 | 4 / 4 | Mid 148; end 157; response 158 | Resource geology has three named days; climate and impact design receive the remaining sustained work |

All 19 owned expectations have teaching and end-of-unit assessment reservations. They have no lettered subcodes; completeness depends on their substantive actions and dimension elements. Apart from the findings above, the sequence explicitly reserves the vulnerable components: extended structures, six interacting body systems, growth and repair, ecosystem boundaries, individual and population effects, resource geology, and both monitoring and impact reduction.

Units 4, 5 and 6 exceed 25 days and contain mid-unit assessments. Response time is counted once. No whole-unit allocation is demonstrably far over its load, although practical timing remains untested.

## Calendar, checks, candidates and shorter path

- **Calendar:** Days 67 and 159 fall in target weeks 14 and 32. The mid-year science check shares no school day with another subject’s course-level check.
- **Same-year leans:** The ratio-table bridge on days 31 to 32, argument bridges on days 58 and 63, evidence-evaluation bridge on day 122 and independent science causal reasoning address skills taught later elsewhere. Informative writing, research and percentage instruction are available at their cited uses.
- **Product load:** The day 94 material record precedes the social studies research unit. The final science and ELA product-window overlap remains unresolved, as the sequence acknowledges. Coordinate deadlines during unit planning; the available ELA frame does not establish an exact deadline.
- **Non-repetition:** Both course checks explicitly draw the immediately preceding unit’s skills through earlier-unit contexts. This meets the planning requirement; eventual items must preserve those substantive connections.
- **Candidates:** All six cells are settled at zero candidate days. Required synthetic-material and geology additions remain inside the unit totals.
- **Shorter period:** The guidance preserves evidence, individual reasoning, safety, assessments and response, and does not claim that shorter meetings preserve the original minutes automatically.
- **Shorter year:** The ten fold-ins are days 3, 6, 12, 28, 37, 46, 56, 71, 116 and 137. None is an assessment, readiness or dedicated response day. Named receiving days retain the work. The warning to recalculate check placement is appropriate.

## Source map

The map contains all 92 base-lesson identifiers: 90 retained lessons and the two optional zero-day cuts, plus nine additions or course-level records. The retained lesson identifiers stay in base order. The optional cuts have reasons, and the required resource extension and geology addition are explicit.

This verifies map completeness and declared order. It does not certify that every condensed activity fits its eventual lesson period.

## Science lens checklist: scope and sequence

| Lens line | Result | Evidence |
|---|---|---|
| Anchors are phenomena or design problems | Met | Fizzing bath bomb, meal heater, health case, food origins, land-use problem and changing water systems |
| Models are built before dependent use | Missed in part | Overall order holds; finding 2 identifies premature full-code checks |
| Engineering expectations appear through design | Met on practical route | Heater iteration, constrained land-use design and monitoring-and-reduction method |
| Equipment has substitutes or no-kit paths | Met as access reservations, incomplete as full performance evidence | Alternatives are named; findings 3 and 4 address their limits and costs |

The relevant scope-layer rubric commitments are substantially present. Full assessment claims, prerequisite treatment and S6 costs need correction. Finished lessons, safety implementation and scoring quality are not judged here.

## What is right and should remain

Keep the six-unit order, provisional early gas explanations, explicit distinction between matter and energy, molecular/crystal distinctions, six-system integration, required resource-geology extension, sensitivity protections and unfamiliar transfer cases.

Earlier frame findings about boiling point, molecular descriptions, demonstration boundaries and the missing resource extension have been addressed. They should not be reopened as unresolved defects.

## Settled by the expert

These are recommendations for the caller to apply; this run changes no files.

| Choice | Reason | Files affected |
|---|---|---|
| Check older returns at their first receiving unit | Later same-year retrieval cannot excuse an unchecked first return | Sequence, day notes, frame and progression |
| Keep day 13 as partial property evidence, with complete assessment after atomic modeling | Preserves the evidence-first storyline | Sequence and day 13 reservation |
| Add explicit small-change/large-response reasoning before day 113 | Makes the complete midpoint claim teachable | Days 105 to 106 and 113 |
| Distinguish practical performance from supplied-data analysis in the record | Prevents unsupported complete-code results | Unit 2 and checks 41 and 67 |
| Add six provisional cost estimates | Makes the proposed materials route reviewable | Sequence materials section |
| Retain unit order, allocations, candidate decisions and ten fold-ins | Their purposes are defensible | No structural change |
| Align rubric status with current data and FOUNDATION | Removes contradictory authoring instructions | Science rubric |

## Limits and sources

Assessment items, scoring guidance, actual timing, consumable quantities and live safety protocols are unwritten or unverified. `docs/APPROACH-SCIENCE.md` is absent.

The large linked base storyline PDFs exceeded the web tool’s size limit, and local PDF extraction libraries were unavailable. I used the source-map inventory and primary unit pages; I do not claim a fresh full-PDF audit.

Sources opened:

- [EQuIP Science rubric](https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf): prior learning, coherence and observable assessment evidence.
- [NGSS Appendix E](https://www.nextgenscience.org/sites/default/files/resource/files/AppendixE-ProgressionswithinNGSS-061617.pdf): distinctions between content progressions.
- [MS-PS1-1 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/MS-PS1-1%20Evidence%20Statements%20June%202015%20asterisks.pdf): molecular and extended-structure modeling boundaries.
- The linked MS-PS1-2, MS-PS1-6 and MS-LS2-4 evidence statements: complete performances and assessment timing.
- [MS-LS1-6](https://www.nextgenscience.org/pe/ms-ls1-6-molecules-organisms-structures-and-processes) and [MS-ESS3-1](https://www.nextgenscience.org/pe/ms-ess3-1-earth-and-human-activity): photosynthesis and resource boundaries.
- [Science 6 to 8 criteria](https://cozy-dream-721ab6aab0.media.strapiapp.com/Science_206_8_20_Review_20_Criteria_2_0_98785530fb.pdf) and [evidence guide](https://cozy-dream-721ab6aab0.media.strapiapp.com/Science_206_8_20_Evidence_20_Guide_2_0_257b169972.pdf): targeted passages on phenomena, assessment, dimension elements and safety.
- OpenSciEd unit pages: [reactions and matter](https://openscied.org/instructional-materials/7-1-chemical-reactions-matter/), [reactions and energy](https://openscied.org/instructional-materials/7-2-chemical-reactions-energy/), [metabolic reactions](https://openscied.org/instructional-materials/7-3-metabolic-reactions/), [photosynthesis](https://openscied.org/instructional-materials/7-4-matter-cycling-photosynthesis/), [ecosystems](https://openscied.org/instructional-materials/7-5-ecosystem-dynamics/) and [resources and human impact](https://openscied.org/instructional-materials/7-6-earths-resources-human-impact/): source storyline and adaptation checks.

**For the source list:** The current evidence-guide link above worked through the [review-tools index](https://edreport.org/process/review-tools/science). Record that access route.

## For Cory

- **Scope:** If no start-of-year readiness slot exists within the course contract, resolve its allocation explicitly before freezing the 160-day calendar.
- **Money and audience:** After costing the minimum practical route, decide any necessary equipment support for classrooms and one-child settings. The data-only route cannot promise complete physical-device performance.

**Verdict:** Revise before unit planning. **Finding count:** 5. **Report path:** `docs/reviews/sequence-science-grade-7-2026-11-14.md`, supplied here, not written.


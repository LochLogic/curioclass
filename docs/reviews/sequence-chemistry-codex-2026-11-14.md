# Chemistry scope and sequence review

**Report path:** `docs/reviews/sequence-chemistry-2026-11-14.md`  
**Delivery:** Complete report supplied here only. No files changed.

## Verdict

The unit order and overall allocations are defensible, but the sequence needs revision before unit planning. The largest substantive gap is unit 3’s incomplete reservation for teaching and assessing the full water-properties core idea. Preserve the existing storyline and practical performances while completing that coverage, correcting one prerequisite classification, supplying provisional costs and reconciling stale instructions.

## What I read and checked

- The chemistry scope and sequence and all 160 rows of `data/plans/chemistry/days.csv`.
- The chemistry frame, its frame-register entry, grade 10 science progression rows, incoming prerequisites and outgoing Physics links.
- `CALENDAR.md` and all grade 10 calendar rows, with relevant Geometry and ELA frame provisions.
- `EXPERT.md`, the science lens, science rubric, foundation, shared approach, relevant roadmap and BASELINE provisions, glossary, source register and sequence-writing brief.
- Permitted earlier chemistry frame reviews and the Grade 8 sequence review, used to identify repeated findings.
- Outside sources linked below. No substantive finding rests on memory; prior memory informed review method only.

The prohibited files were not opened. `APPROACH-SCIENCE.md` is absent.

**Gates:** `plan.py check` reported zero chemistry sequence failures, then stopped because Python lacks `markdown`; `frame.py calendar` passed; `frame.py check chemistry` passed with zero failures; `stale.py check` passed across 56 files.

## Findings, most serious first

### 1. Unit 3’s full water-properties claim exceeds its explicit teaching and assessment reservations

**Severity:** High  
**LAYER:** sequence  
**REPEAT:** yes, incomplete Earth-science coverage was finding 2 in the earlier chemistry frame review.  
**Confidence:** firm on the assessment gap; likely on the ambiguous viscosity reservation.

**Location:** Scope and sequence, unit 3 and standards table; days 38 to 40.

**What is wrong:** Day 38 mentions supplied evidence for “heat storage, light transmission and flow.” Day 40 explicitly reserves expansion, dissolution, transport and melting prompts, but does not reserve evidence for heat storage or light transmission. “Flow” also does not identify water lowering the viscosity of molten rock.

These properties belong to the attached core idea, rather than being additional experiments a reviewer happens to prefer. The official evidence statement also connects water’s thermal properties to surface temperature and air and water movement. [HS-ESS2-5 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/HS-ESS2-5%20Evidence%20Statements%20June%202015%20asterisks.pdf).

**Why it matters:** A writer following the assessment row could produce the promised landscape task while leaving these owned components unassessed. Later thermal work in unit 5 would not repair unit 3’s end-of-unit assessment.

**Exact fix:**

- Make day 38’s supplied-data work explicitly address heat absorption, storage and release; sunlight transmission; and water’s effect on molten-rock viscosity.
- Have day 39’s synthesis produce a brief annotated explanation connecting those properties to Earth processes.
- Explicitly carry that product into day 40’s assessment evidence, with a short unfamiliar-data application.
- Update unit 3’s assessment paragraph and coverage-table entry accordingly.

Keep the existing practical investigations. This fix does not require heating rock or adding a separate experiment for every property.

### 2. Unit 10 checks an exponent prerequisite maintained in the preceding year

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, readiness classification errors recur in the Grade 8 sequence review, finding 3.  
**Confidence:** firm.

**Location:** Readiness section; unit 10; days 130 and 136.

**What is wrong:** Day 130 gives readiness on grade 8 powers of ten for pH. However, `m8-integer-exponents` is explicitly assumed and used by grade 9 `alg1-linear-vs-exponential` and `alg1-exponential-functions`. The latter extends zero and negative integer exponents.

The prerequisite’s last planned use is therefore grade 9. Under this run’s rule, it receives retrieval inside a day.

**Why it matters:** The classification unnecessarily removes ten minutes from climate-assessment response and misstates the progression handoff.

**Exact fix:** Remove the readiness marker and exponent check from day 130, restoring its full response allocation. Open day 136 with a short powers-of-ten retrieval task, then teach the supplied pH representation. Retain the existing whole-unit comparisons, supplied fractional comparisons and exclusion of logarithms.

No other clearly unnecessary preceding-year readiness check was established.

### 3. Provisional materials costs are deferred beyond the layer that requires them

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, the Grade 8 sequence review, finding 5, identifies the same deferral.  
**Confidence:** firm.

**Location:** Materials section, especially its cost paragraph; For the lead, item 3.

**What is wrong:** The sequence assigns costs to future unit plans. The science rubric explicitly assigns **S6 costs** to the scope-and-sequence layer.

Named household materials do not establish the cost of protective equipment, balances, thermometers, freezer access, consumables or printing. The practical-performance commitments make those requirements consequential.

**Why it matters:** A teacher or parent cannot yet judge whether the proposed route is feasible.

**Exact fix:** Add provisional estimates for all 11 units, using the shared approach’s class of thirty and a one-child equivalent where materially different. State assumed inventory, quantities, reusable equipment, consumables, printing, dated price sources and the minimum equipment needed to complete the practical performances.

Count shared equipment once and show later reuse. Estimates do not authorize purchases.

### 4. Supporting instructions retain obsolete prerequisites and an already-resolved staffing conflict

**Severity:** Minor  
**LAYER:** frame, progression, process  
**REPEAT:** yes, stale supporting instructions recur in the Grade 8 sequence review, finding 6.  
**Confidence:** firm.

**What is wrong:** The stale checker passes, but the following conflicts remain.

| Location | Conflict | Exact fix |
|---|---|---|
| Chemistry frame, opening | Says the scope and sequence sets days “later.” | Link the current sequence and daily record as drafts now available. |
| Frame Seams and Models carried; corresponding science progression notes | Permit grade 8 last-use retrieval under the older intervening-grade rule. | Align with this run’s last-use rule and the sequence’s readiness before units 5 and 9. Preserve retrieval for skills maintained in Biology. |
| Sequence, For the lead item 4; science rubric S5 and closing people question | Present finding a science teacher as an unresolved safety-review requirement. | Apply current FOUNDATION 7.3, which assigns this content review to the safety agent. Preserve its separate human pilot requirements. Remove the obsolete staffing question. |
| Science rubric, Gateway 2 full-scope gap | Says dimension statements exist in no data file. | Acknowledge `ngss-pe-dimensions.csv`; retain the requirement to trace elements to teaching and assessment evidence. |

**Why it matters:** Later writers receive conflicting prerequisites and review requirements depending on which supporting document they open.

These are consistency repairs to existing decisions. They do not require a new people-policy decision from Cory.

## Order, standards, assessments and load

All 20 owned progression rows and 21 expectations have daily placements. These expectations have no lettered subcodes; completeness depends on their constituent performances and dimensions.

| Unit | Days | Owned expectations | Order and load judgment |
|---|---:|---:|---|
| 1. The table that predicts | 16 | 2 | Charge and atomic structure precede periodic prediction and revised reaction explanations. Defensible. |
| 2. Strong pulls, weak pulls | 15 | 2 | Investigation planning precedes collection, inference and designed-material communication. Defensible. |
| 3. Water shapes the land | 10 | 1 | Rebuilding precedes the practical comparisons; elapsed freezing time is protected. Coverage needs finding 1. |
| 4. Counting atoms by weighing | 12 | 1 | Atom conservation precedes coefficients, mole reasoning and mass proportions. Defensible. |
| 5. Hot packs and cold packs | 18 | 3 | Bond models, collected thermal evidence and computational creation receive distinct runs. Defensible. |
| 6. Faster, and more | 13 | 2 | Temperature and concentration evidence precede dynamic equilibrium and design refinement. Defensible. |
| 7. Design an energy device | 12 | 2 | Decomposition and criteria precede construction, testing, refinement and retesting. Defensible. |
| 8. Inside the nucleus | 10 | 1 | Nuclear mechanisms precede dating and qualitative energy comparisons. Defensible. |
| 9. Earth’s energy budget | 18 | 3 | Energy mechanisms precede feedback analysis and forecasting. Defensible. |
| 10. Following the carbon | 13 | 2 | Stock and flow quantities precede model revision and published-output interpretation. Defensible. |
| 11. Where people live, and why | 12 | 2 | Causal explanations precede comparable quantities and competing-design evaluation. Defensible. |

No whole unit is demonstrably far over or under its load. Units 5 and 9 reasonably receive the longest allocations. Unit 3’s single expectation includes several practical and conceptual demands, so its ten days are justified.

End-of-unit assessments occupy days **15, 30, 40, 52, 73, 86, 98, 111, 129, 142 and 154**. Response is counted once. No unit exceeds 25 days, so no mid-unit assessment is required.

The practical and computational portfolios substantially improve assessment feasibility. Preserve them. Day 156’s five-code assessment is particularly dense; actual duration remains unverified until its items are written.

Apart from finding 1, the reservations provide plausible coverage at this planning layer. They do not establish that unwritten items, scoring guidance or timings are complete.

## Readiness and retrieval audit

| Receiving unit | Prerequisite and last planned use | Treatment |
|---|---|---|
| 1 | Atom, molecule and reaction rows maintained in Biology, grade 9 | Retrieval on day 1, appropriate. |
| 2 | State-change row last used in grade 7; synthetic materials, grade 7 | Readiness day 16, repair day 18, appropriate. |
| 3 | Water and rock cycles last used in grade 7 | Readiness day 31, repair day 33, appropriate. |
| 4 | Scientific notation, grade 8; conservation maintained in Biology and this course | Readiness day 41 for notation; conservation retrieval, appropriate. |
| 5 | Particle-temperature and specified transfer contribution last used in grade 8; Biology energy and computation, grade 9 | Readiness day 56 and repair day 58; Biology retrieval, appropriate. |
| 6 | Temperature and conservation used earlier this year | Retrieval, appropriate. |
| 7 | Design practice maintained through Biology; energy accounting earlier this year | Retrieval, appropriate. |
| 9 | Weather, grade 6; circulation and climate evidence, grade 7; orbit and light models, grade 8 | Readiness day 112, repair days 114 and 115, appropriate. |
| 10 | Biology carbon and computation; current-year models; integer exponents maintained in grade 9 | Science retrieval appropriate; exponent readiness needs finding 2. |
| 11 | Hazard forecasting last used in grade 7; resource distribution, grade 7; Biology evaluation and grade 9 geography | Readiness day 143 for older rows; retrieval for the maintained work, appropriate. |

All readiness slots are immediately before their receiving units. None occupies a receiving unit’s first day or sits weeks ahead. Unit 1 has no established older prerequisite requiring a start-of-year readiness slot.

## Calendar and cumulative checks

Chemistry’s course-level checks match its calendar:

- Days **54 to 55**, week **11**, with response on day 56.
- Days **100 to 101**, weeks **20 to 21**, with response on day 102.
- Days **156 to 158**, week **32**, with response on days 159 to 160.

Grade 10 has no additional stagger restriction.

The immediately preceding unit’s skills explicitly use earlier content: unit 1 reactions after unit 4, units 5 and 6 after unit 7, and device and fuel-carbon evidence after unit 11. Preserve those non-repetition instructions.

Same-year leans are supported:

- Precision and conversion bridges appear on days 19, 46 and 91 before Geometry completes the relevant work.
- Geometry’s quantity work finishes before carbon modeling and resource comparisons.
- Early chemistry writing has explicit support before the corresponding ELA units.
- ELA’s supplied forecast reading covers its day 128 opening before chemistry’s day 129 forecast.
- History’s earlier industrial and nuclear work has bridges and later chemistry callbacks.

The exact ELA issue-argument due day remains unverified, as the sequence acknowledges.

## Candidates, shorter path and source map

All 11 Candidate cells are settled as kept, with their costs assigned to existing days. None remains an unresolved proposal.

Both shorter-path forms are present. The ten folds are:

`8 into 7; 14 into 13; 29 into 28; 51 into 50; 72 into 71; 85 into 84; 97 into 94 with later updates; 110 into 109; 128 into 127; 141 into 140.`

None removes a marked assessment day. Practical collection, construction, testing, readiness and response remain protected. The design report’s updates after retesting are explicitly retained. Actual receiving-day feasibility still requires unit-level timing.

No base text is assigned. A base-lesson source map is therefore not applicable.

## Science lens checklist: scope and sequence

| Lens line | Result |
|---|---|
| Anchors are phenomena rather than topics | **Met.** Each unit opens with a specific explanatory puzzle or design need. |
| Models are built before dependent use | **Met at plan level**, subject to the prerequisite correction in finding 2 and supporting-document reconciliation. |
| Engineering expectations appear in units | **Met.** Unit 7 reserves decomposition and a physical build-test-refine cycle. |
| Equipment has substitutes or a no-kit path | **Met for stated routes and honest performance limits.** Cost feasibility remains missed under finding 3. |

The sequence supports phenomenon-driven planning, model revision, original high school authorship and broad coherence. Full water-properties coverage and materials costs require correction. This is not a numerical rating of unwritten units.

## Settled by the expert

These are recommendations for the caller to apply. None was applied during this read.

| Choice | Reason | Files affected |
|---|---|---|
| Keep all unit allocations and their order | No demonstrated order or whole-unit load defect | Chemistry sequence and frame |
| Complete water-property teaching and assessment within days 38 to 40 | Closes the identified coverage gap without moving ownership | Chemistry sequence and days.csv |
| Retrieve powers of ten on day 136 | The prerequisite is maintained in grade 9 | Chemistry sequence and days.csv |
| Restore day 130’s full response time | Its readiness allocation is unnecessary | Chemistry days.csv |
| Retain practical portfolios and explicit incomplete-performance records | Supplied results cannot establish every required performance | Chemistry assessment reservations |
| Add provisional unit costs | Required at this layer; purchasing remains separate | Chemistry sequence |
| Reconcile supporting instructions with current decisions | Prevents contradictory downstream authoring | Frame, progression notes and science rubric |

## What is right and should remain

Preserve the main-group boundaries, distinction between physical pack changes and chemical reaction energy, thermal computational proficiency case, and published-results boundary for Earth-system model interpretation.

Also preserve the elapsed freezing interval, repeated thermal measurements, actual device construction and retesting, unseen transfer tasks, sensitivity provisions and explicit limits on supplied-data routes. Earlier frame problems concerning disappearing oil, transition-metal proficiency cases and the ELA forecast overlap have substantive repairs here and should not be reopened as absent.

## Sources and limits

- [Official standards arranged by core idea](https://www.nextgenscience.org/sites/default/files/AllDCI.pdf): performance expectations, dimensions and boundaries.
- [HS-ESS2-5 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/HS-ESS2-5%20Evidence%20Statements%20June%202015%20asterisks.pdf): water-property and investigation coverage.
- [HS-PS3-1 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/HS-PS3-1%20Evidence%20Statements%20June%202015%20asterisks.pdf): computational creation and thermal-case limits.
- [HS-PS1-5 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/HS-PS1-5%20Evidence%20Statements%20June%202015%20asterisks.pdf): temperature, concentration and collision reasoning.
- [High school science evidence guide](https://cdn.edreports.org/media/2025/07/Science-High-School-Evidence-Guide_2.0.pdf): selected passages on phenomena, assessment, element-level coverage and safety. The full 89-page guide was not read.
- [Science unit-review rubric](https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf): coherence and observable-performance principles.
- [OpenSciEd chemistry organization](https://openscied.org/on-demand-hub/how-are-traditional-chemistry-topics-organized-in-openscied-high-school-chemistry/) and [NJCTL chemistry sequence](https://njctl.org/materials/courses/chemistry-1/): contrasting published organizations. Their differences support treating this order as a defensible choice, rather than a prescribed order.

The standalone HS-PS2-6 evidence PDF was inaccessible. Its communication requirements were checked in the official [conceptual-course bundle, PDF page 7](https://www.nextgenscience.org/sites/default/files/HS%20Conceptual%20Course%201%20Bundle%206_0.pdf).

Actual assessment duration, scoring, final laboratory protocols, local inventory, current costs and classroom feasibility remain unverified. Final safety implementation belongs to the subsequent safety read.

**For the source list:** Add the accessible high school evidence-guide URL and specific evidence-statement links above if absent.

## For Cory

- **Money:** Decide any materials allowance or purchases after the provisional estimates are supplied.
- No new scope, audience or outside-person decision is recommended.

**Verdict:** Revise before unit planning. **Finding count:** 4. **Report path:** `docs/reviews/sequence-chemistry-2026-11-14.md`, supplied here only.


# Economics scope and sequence: independent expert read

**Date:** 2026-11-14  
**Intended report:** `docs/reviews/sequence-economics-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files were created, edited or deleted.

## Verdict

Revise before acceptance. The nine-unit order is coherent and the 80-day structure works, but several day goals and assessment descriptions do not secure the full requirements of their attached standards. The most important change is to specify the missing student performances, then resolve the concentrated finance workload within the existing units.

**Finding count: 8.**

## What I read and checked

Read in full:

- `docs/agents/EXPERT.md` and the social studies lens.
- The shared adoption bar, its social studies and personal finance sections, and `docs/courses/social-studies/STANDARD.md`.
- The economics scope and sequence, all 80 rows of `data/plans/economics/days.csv`, and the economics frame.
- All 25 economics progression rows and the earlier rows supplying their prerequisites.
- The loaded ECON and PFL standards, checked against the original Massachusetts framework, printed pages 170 to 175.
- `docs/courses/CALENDAR.md` and the relevant economics, mathematics and ELA calendar entries.

Also consulted FOUNDATION, APPROACH, relevant APPROACH-SOURCES entries, ROADMAP, BASELINE rules 20 to 24, GLOSSARY, BASE-TEXTS, the sequence briefs, both earlier economics frame reviews, their fix report, and relevant progression, baseline and earlier sequence findings.

Outside sources were opened as linked below. No substantive finding rests on unaided memory. Personal memory notes informed only the review method.

### Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Printed economics sequence: 0 failures, then stopped with missing dependency `markdown`. |
| `python -X utf8 scripts/frame.py calendar` | Completed; no reported stagger-rule breaks. |
| `python -X utf8 scripts/frame.py check economics` | 0 failures; 9 units, 80 days. |
| `python -X utf8 scripts/sequence.py check economics` | 0 failures. |
| `python -X utf8 scripts/stale.py check` | One failure in `docs/courses/us-history-ii/frame.md:78`, outside this course. |

The incomplete global gate and unrelated stale failure do not prevent this verdict.

Structural tracing found all **83 Massachusetts codes**, comprising 59 ECON and 24 PFL codes, on teaching days, alongside 16 C3 indicators. The owned ECON and PFL codes have no separately lettered subparts. Placement is complete; semantic coverage needs the repairs below.

## Findings, most serious first

### 1. Some requirements disappear between the standards and the day goals

**LAYER:** sequence, progression, standard  
**REPEAT:** yes, incomplete coverage behind complete code placement appeared in the earlier economics frame and social studies progression reads.  
**Severity:** substantial  
**Confidence:** firm on the requirements; likely on the resulting instructional omissions.

These are specific omissions a writer could carry into lessons:

| Location | Missing requirement | Exact fix |
|---|---|---|
| Day 21, ECON.T3.5 | Increased output disappears from the explanation of competition. | Add explaining the output response alongside costs and prices. |
| Day 56, ECON.T7.6 | Comparing productivity levels does not secure comparison of trends. | Require a dated time series and a comparison of changes across countries. |
| Day 69, PFL.T2.4 | Policies and effectiveness are named, but research and reporting are unsecured. | Require a short sourced investigation and conclusion. |
| Day 70, PFL.T3.3 | Credit denial and uses of reports beyond lending are absent. | Add a supplied credit-history case and explanation of those uses. |
| Day 71, PFL.T3.4 | Consequences are listed without research and reporting. | Require students to investigate a supplied source pack and report the consequences. |

These requirements are explicit in the [Massachusetts framework, printed pages 171, 172, 174 and 175](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf).

Day 56 also needs the resource-distribution component of D2.Eco.15 and an evaluation of scarce-resource pressures producing conflict or cooperation for D2.Geo.11. Globalization’s general effects do not secure those components. Add a focused resource case with evidence for a judgment, as required by the [C3 Framework](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf).

**Why it matters:** Students could complete every stated activity while missing required reasoning. Restore these performances in the day goals and assessment blueprint. Correct the progression paraphrases where they narrow the original research-and-report requirements.

### 2. Assessment descriptions promise more coverage than their tasks secure

**LAYER:** sequence, frame  
**REPEAT:** yes, the earlier economics frame review and civics sequence review identified the same distinction between listed codes and demonstrated performance.  
**Severity:** substantial  
**Confidence:** likely.

“Covers every part” is an assurance, not a component-level specification. Several assessment descriptions omit substantial work taught earlier.

| Assessment | Unsecured coverage | Exact fix |
|---|---|---|
| Day 17 | Product, resource and financial markets; both elasticities; both kinds of price control. | Reserve short components covering those distinctions alongside the unseen market task. |
| Day 33 | Budgets at three government levels and the historical income-profile comparison. | Name the required budget comparison and tax-history analysis explicitly. |
| Day 43 | A forward inference from indicators and current-data reasoning about money-supply changes. | Require both, alongside the historical cycle explanation. |
| Day 50 | Evaluating policy across differing economic conditions. | Use paired recession and inflation cases rather than one unspecified scenario. |
| Day 57 | Trade versus payments balances, productivity trends, globalization’s wider effects, and resource-related conflict or cooperation. | Add named components or identify independently completed work assessed with the unseen task. |
| Day 66 | Advertising evidence, state and federal consumer-protection roles, and income changes caused by labor-market conditions. | Include those requirements explicitly; a job offer, budget and scam-identification task does not secure them. |
| Day 77 | Saving-policy research, consequences research, real versus nominal returns, and asset-price and diversification reasoning. | Identify the evidence supplied by the research records, portfolio and unseen task, with each requirement assigned to a scored component. |

The scope already includes the portfolio record in unit 9’s assessment. Keep that arrangement and make its coverage explicit.

**Why it matters:** Teachers need to know which work establishes each requirement, particularly where a single 50-minute assessment cannot reasonably contain every performance.

**Exact fix across the course:** Add a compact assessment blueprint identifying each standard component, the evidence that assesses it, and its assessment day. Questions, keys and rubrics remain unit-plan work. This implements the repository’s full-coverage rule and the emphasis on aligned assessment in the [social studies materials criteria](https://air.org/sites/default/files/2024-01/23-23505_HQIM_for_SS_Final.pdf).

### 3. The trade task does not specify data sufficient to compute comparative advantage

**LAYER:** sequence, frame, progression  
**REPEAT:** new among the relevant earlier reads.  
**Severity:** substantial  
**Confidence:** firm.

Day 53 proposes working comparative advantage from public trade data. Day 57 asks students to compute it from trade and income data.

Observed exports and income do not, by themselves, provide the opportunity costs needed for that calculation. The partial economics text develops comparative advantage through alternative production possibilities and resource requirements. [Principles of Economics 2e, section 33.1](https://openstax.org/books/principles-economics-2e/pages/33-1-absolute-and-comparative-advantage).

**Why it matters:** A writer could produce an invalid calculation or teach students to treat export volume as proof of lower opportunity cost.

**Exact fix:**

- Keep day 52’s two-country, two-good worked example.
- On day 53, distinguish observed trade patterns from evidence about production opportunity costs.
- Supply an explicitly simplified production-cost table where calculation is required. Label assumptions and any illustrative figures.
- On day 57, provide an unseen production-possibilities or resource-requirements table for calculation. Use trade data separately for interpretation.

This refines the earlier expert’s settled real-country example. I disagree with treating unspecified public trade data as sufficient for the computation; I agree with retaining a real-country application.

### 4. Finance days remain overloaded, and the services comparison comes too early

**LAYER:** sequence, frame  
**REPEAT:** yes, both earlier economics frame reads questioned the finance budget.  
**Severity:** substantial  
**Confidence:** likely on concentration; exact timings are a judgment call.

The earlier frame repair supplied a task budget. The daily sequence now reveals where that budget remains strained:

| Run | Available time | Required work |
|---|---:|---|
| Days 59 to 65 | 7 periods, including 2 action periods | Readiness and possible reteaching, job choice, labor-market reasoning, budget and pay stub, advertising research, payment comparisons, consumer protection, tax return, insurance comparison and identity protection. |
| Days 68 to 76 | 9 periods, including the college addition | Interest, saving-policy research, institution comparison, credit terms and reports, consequences research, borrowing plan, aid offers, asset research, portfolio, regulators and final plan. |
| Day 69 alone | 1 period | Real and nominal rates, saving-policy effectiveness, three kinds of institutional services, a justified comparison, and a possible reteach station. |

Day 69 asks students to compare credit and investment services before days 70 and 73 teach the relevant content in detail.

Day 65 similarly combines insurance investigation and choice with identity protection. A comparable introductory insurance activity allocates 45 to 60 minutes to insurance alone. That is a useful warning, not a measured minimum for this course. [Exploring types of insurance](https://www.consumerfinance.gov/documents/7247/cfpb_building_block_activities_exploring-types-of-insurance_guide.pdf).

**Exact fix within the existing units:**

- Move the institution-services comparison from day 69 to day 76. Make it the evidence for selecting the institution used in the final savings or investment plan.
- Use day 69 for real and nominal rates and the saving-policy investigation.
- Begin the borrowing comparison on day 71 and carry its cost-comparison method into day 72’s aid offers.
- Introduce identity protection through the tax-return documents on day 64, leaving day 65 principally for insurance investigation and comparison.
- Record minutes for teaching, guided work and independent evidence on these revised days. Preserve both action periods, assessments and response days.

**Why it matters:** Without this redistribution, research and independent practice are likely to become brief teacher explanations.

### 5. Several first uses lack an explicit instructional step, and writing does not show a planned increase in demand

**LAYER:** sequence  
**REPEAT:** yes, the earlier progression and baseline reads required models before application and a coherent argument thread.  
**Severity:** moderate  
**Confidence:** likely.

Day 14 is the first explicit elasticity lesson but is classified as Fluency. Day 22 introduces costs and immediately uses marginal revenue without explicitly establishing how revenue changes when output and price change.

The writing sequence likewise jumps to an argument on day 16, while claim-evidence-reasoning is explicitly named only on day 75. Earlier grades provide that model, so it should be retrieved and extended here. The course does not identify how its source-based writing grows.

**Exact fix:**

- Make day 14 Understanding or Application, with a worked elasticity example before independent calculation.
- Add a price-output-revenue table and an explicit marginal-revenue introduction before day 22’s decision task. Require students to distinguish the chosen output from the price read from demand. The [partial text’s monopoly lesson](https://openstax.org/books/principles-economics-2e/pages/9-2-how-a-profit-maximizing-monopoly-chooses-output-and-price) makes these steps explicit.
- Retrieve and model a sourced explanation on day 5.
- Require a two-source argument with a counterclaim on day 16, an extended policy explanation on day 30, and synthesis of multiple sources in the consumer information piece on days 62 to 63.
- State that progression in the scope and sequence. Incorporate it into existing products.

**Why it matters:** A downstream writer needs to know where teaching, supported practice and independent performance occur. Sustained inquiry and evidence-based communication are also central to the [social studies materials criteria](https://air.org/sites/default/files/2024-01/23-23505_HQIM_for_SS_Final.pdf).

### 6. Later readiness checks repeat knowledge already checked and used in this course

**LAYER:** sequence, frame, progression  
**REPEAT:** yes, the earlier civics sequence read found the same readiness-versus-retrieval problem.  
**Severity:** moderate  
**Confidence:** firm.

Day 1 checks grade 8’s opportunity cost, budgets and interest. The course then uses that knowledge, yet days 28, 59 and 68 classify returns to the same row as dormant-knowledge readiness checks and promise another one-lesson reteach.

Those later returns are now within-course retrieval. They are not the first encounter with an earlier-grade row.

**Exact fix:**

- Retain day 1’s readiness check and day 2’s planned response.
- Make days 28, 59 and 68 begin with retrieval tasks; clear their `assess=readiness` cells.
- Replace repeated whole-row reteach promises with brief, targeted support for the particular gap shown.
- Reconcile the frame and progression wording with that classification.
- Retain day 45’s short money check. Its lesson explicitly teaches the functions of money afterward.

**Why it matters:** The current labels reserve repeated remedial work in already crowded units and misdescribe the learning history.

### 7. The required shorter path is absent

**LAYER:** sequence  
**REPEAT:** yes, the earlier civics sequence read identified the same omission.  
**Severity:** moderate  
**Confidence:** firm.

The plan specifies 80 meetings of 50 minutes but gives no shorter path. FOUNDATION section 5 and adoption-bar C2 require one.

**Why it matters:** A teacher with shorter periods or fewer meetings has no defensible cut order and may remove research, practice or response time.

**Exact fix:** Add a shorter-path table identifying retained core performances, reduced repetition or optional examples, supported timetable, and unchanged assessment coverage. Begin by examining repeated readiness work and duplicated case setup. Protect the new research requirements and the finance work identified above.

Do not promise that the same load fits a shorter timetable without testing representative plans. If no shorter route preserves the approved scope, bring Cory a concrete duration or scope proposal.

### 8. The sequence identifies frame contradictions but leaves them as unresolved instructions

**LAYER:** process, frame  
**REPEAT:** yes, stale and contradictory receiving instructions recur in the earlier frame reviews.  
**Severity:** minor  
**Confidence:** firm.

The sequence’s two “For the lead” items are useful and substantially correct, but the receiving frame still says “None open.”

Additional mismatches remain:

| Location | Exact correction |
|---|---|
| Frame’s Roman-money seam | Name day 45’s short check and the same-day teaching response. |
| Frame’s ELA workload note | Replace avoiding the research *weeks* with avoiding the named major milestone days. Preserve the short, in-class economics product. |
| Unit 5 prose | Say circular flow begins on day 37 and aggregate supply and demand on day 39. “Both new models open on the first two days” is inaccurate. |
| Frame’s grade 11 timetable | Explain that the CSV gives the spring placement. For a fall offering, use school day = course day and recheck cross-subject timing. |
| Day 74 portfolio note | State that observations occur on days 74 to 77, including the fourth observation during assessment. |

**Why it matters:** Writers should receive one current instruction for timing, workload and prerequisites.

The shared literacy-loading statements in STANDARD.md and the adoption bar are also stale: the literacy file exists. That issue was already reported in the earlier grade 7 sequence read. Correct the current-status statements without rewriting historical reports.

## Order, coverage and days by load

The principal dependencies are sound: scarcity precedes markets; markets precede competition and intervention; measures precede stabilization policy; trade retrieves opportunity cost; personal finance retrieves wages, inflation and banking.

| Unit | Total days | Teaching days before assessment and response | Massachusetts codes | C3 indicators | Load judgment |
|---|---:|---:|---:|---:|---|
| 1 | 8 | 6 | 9 | 3 | Dense but coherent. |
| 2 | 10 | 8 | 9 | 2 | Appropriate graph allocation; repair first elasticity instruction. |
| 3 | 9 | 7 | 10 | 3 | Tight; secure the marginal-revenue bridge. |
| 4 | 7 | 5 | 8 | 2 | Dense; assessment must preserve the historical tax comparison. |
| 5 | 8 | 6 | 6 | 2 | Reasonable; retain the money-supply bridge. |
| 6 | 7 | 5 | 7 | 1 | Tight but coherent; use contrasting policy conditions. |
| 7 | 7 | 5 | 8 | 3 | Very dense, especially day 56; use a focused shared case. |
| 8 | 9 | 7 | 7 | 0 owned | Two action days leave five other teaching periods; redistribute as finding 4 specifies. |
| 9 | 11 | 9 | 19 | 0 owned | Heaviest concentration of distinct decisions and products; needs the revised task budget. |

These counts indicate concentration, not a rule that standards deserve equal time. No unit exceeds 25 days, so no mid-unit assessment is required. Assessment response time is counted once.

## Calendar, candidates and source map

The midpoint assessment is school day **115, week 23**, followed by response on day 116. The final is school day **159, week 32**, followed by response on day 160. The shared calendar matches the economics sequence.

The Algebra II geometric-series unit precedes spring economics day 71. The supplied-payment-table bridge also makes the borrowing plan independent of that formula. Earlier mathematics leans appropriately use retrieval.

Economics action days 142 and 143 avoid the listed ELA 12 milestones, although they remain inside the larger research window. The frame needs the wording correction in finding 8.

All candidate cells are settled:

- Marginal thinking, production costs, externalities, unemployment types, money creation, and pay-stub work remain inside owned standards.
- Tax filing and paying for college each receive one day, using two of the four allowed addition days.
- Consumer and producer surplus and renting a first home are dropped from taught days with reasons and retained as extensions.

**Source map: not applicable at this layer.** The course has no full base text. Partial-source chapters are identified; unit plans must identify the particular material adapted and its credit.

## Lens checklist: scope and sequence

| Lens line | Result |
|---|---|
| A unit question requires the unit’s sources and permits defensible alternatives | **Met in design.** Frame questions require economic judgment; assessment links need finding 2’s repairs. |
| History runs in time order unless a reason is given | **Not applicable as a governing course order.** Historical examples serve an explicitly conceptual economics sequence. |
| A contested event receives more than one telling | **Met in planning intent.** Competing economic evidence is reserved for controls, policy and trade; actual source selection remains unit-plan work. |
| Writing from sources recurs and grows | **Missed.** Repeated tasks exist, but increasing demand is unspecified. Finding 5 supplies the progression. |

## What is right and should remain

- Keep the nine-unit order and distinct market and aggregate graphs.
- Preserve the earlier repairs: financial-market introduction, money-supply bridge, tax-income profiles, institution comparison, asset research and portfolio tracking.
- Keep student-chosen informed action, paper access, fictional offers and protection against family financial disclosure.
- Keep grade 11 access through locally taught historical examples.
- Preserve assessment and response allocations.

## Settled by the expert

These are choices for the caller to apply; no edits were made.

| Choice | Reason | Files affected |
|---|---|---|
| Supply production-cost information for comparative-advantage calculations | Makes the required calculation valid. | Sequence, days CSV, frame and trade progression note |
| Move the services matrix to day 76 and use it within the final plan | Comparison follows the necessary instruction and serves an existing product. | Sequence and days CSV |
| Carry borrowing comparisons into the college-aid day | Reuses the method rather than restarting it. | Sequence and days CSV |
| Introduce identity protection with tax documents; protect the insurance period | Reduces competing work on day 65. | Sequence and days CSV |
| Add the marginal-revenue bridge before independent output and price decisions | Makes the reasoning explicit. | Sequence and days CSV |
| Reclassify later grade 8 checks as retrieval | Knowledge has already been checked and used here. | Sequence, days CSV, frame and progression notes |
| Retain all nine units, both action days and all response days | The identified repairs do not justify removing them. | Economics planning files |
| Align frame wording and model/portfolio dates | Gives subsequent writers one current instruction. | Frame, sequence and days CSV |

## What I could not judge

Actual assessment items, rubrics, source difficulty, classroom timings and adaptation rights cannot be certified from this layer. The state and college-framework comparison tables belong to the unit plans and were not treated as completed evidence here. No finding claims measured effects on students.

## Sources

- [Massachusetts History and Social Science Framework, 2018](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf): original ECON and PFL requirements, printed pages 170 to 175.
- [C3 Framework](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf): owned economic reasoning and globalization indicators.
- [Social studies materials criteria](https://air.org/sites/default/files/2024-01/23-23505_HQIM_for_SS_Final.pdf): coherent sequence, sustained inquiry, communication and assessment.
- [Principles of Economics 2e, comparative advantage](https://openstax.org/books/principles-economics-2e/pages/33-1-absolute-and-comparative-advantage): data needed for opportunity-cost reasoning.
- [Principles of Economics 2e, monopoly decisions](https://openstax.org/books/principles-economics-2e/pages/9-2-how-a-profit-maximizing-monopoly-chooses-output-and-price): marginal revenue, output choice and price.
- [CEE economics standards, 2010](https://www.councilforeconed.org/wp-content/uploads/2012/03/voluntary-national-content-standards-2010.pdf): marginal decision-making reference.
- [National Standards for Personal Financial Education, 2021](https://files.consumerfinance.gov/f/documents/2021_Natl_Standards_Downloadable_final.pdf): six-domain organization and financial decisions.
- [Exploring types of insurance](https://www.consumerfinance.gov/documents/7247/cfpb_building_block_activities_exploring-types-of-insurance_guide.pdf): a concrete pacing comparison, used with explicit limits.

### For the source list

Add the two section-specific economics links above if absent.

A [2025 third edition of the CEE economics standards](https://www.councilforeconed.org/wp-content/uploads/National-Content-Standards-in-K%E2%80%9312-Economics-3rd-Edition.pdf) is available. Its publication details, introduction and crosswalk were inspected, not all benchmarks. Record it for a reference-currency comparison; this review continues to use the explicitly selected 2010 edition.

## For Cory

- **Scope or duration, only if necessary:** If the revised task budget and shorter-path work cannot preserve full coverage, decide a concrete duration or scope alternative. The approved 80-day main route stands meanwhile.

**Verdict:** revise before acceptance. **Findings:** 8. **Intended report path:** `docs/reviews/sequence-economics-2026-11-14.md`, delivered here only.


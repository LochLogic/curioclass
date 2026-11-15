# Economics unit plans: independent second read

## What I read

I read `docs/courses/economics/s01.md` through `s09.md`, the economics frame, scope and sequence, all 80 rows of `days.csv`, and the relevant economics and prerequisite rows in `data/progressions/social-studies.csv`.

I also read the required guidance, the social studies lens, the applicable adoption-bar criteria, the local standards, source records and relevant checking code. I did not open the prior economics review or the prohibited course files. No files were changed or created.

Checks:

- `unitplan.py check economics`: all nine plans passed.
- `frame.py check economics`: passed, confirming 76 unit days and four course-level assessment and response days.
- `plan.py check economics`: passed.
- The repository-wide plan check stopped on the missing `markdown` dependency after reporting no economics sequence failures.
- Forty-eight targeted numerical checks passed.
- The text scan found no corrupted apostrophes, quotation marks or accented letters represented by question marks.

**Finding tags:** “REPEAT: unassessed” preserves the blind read. Firm findings rest on explicit text or checked sources. Timing findings are judgments about the specified work, not observed classroom timings.

## Course verdict

The course has a coherent sequence, generally accurate economics, careful distinctions between observations and models, and strong protections for students’ financial privacy. It needs revision before the plans can support lesson writing reliably: units 1, 8 and 9 leave important daily evidence unwritten, and unit 8’s advertising assessment measures a different construct from the standard. Several assessment and teaching allocations also need more concrete response formats, while a generator defect produces false statements about carried models.

## Unit 1: Scarcity, choice and economic systems

### 1. Serious: Daily evidence is deferred for every teaching day

**Location:** `s01.md`, fields 5 and 10, especially “Still to make.”

**LAYER:** plan. **REPEAT:** unassessed. **Confidence:** firm.

The plan supplies readiness and end-of-unit assessments but explicitly leaves all independent exit tickets unwritten. Consequently, the reader cannot check whether days 1 to 6 produce evidence of their goals, distinguish the registered errors or provide timely grounds for reteaching. The instruction that future evidence must cover every verb does not supply that evidence.

**Exact fix:** Add a daily-evidence table containing six fully written, independent items, each with its answer, error letters and standard parts:

| Day | Evidence required |
|---|---|
| 1 | Define and distinguish natural, human and capital resources, including inputs to a service. |
| 2 | Identify consumer and producer opportunity costs and compare one additional benefit with its additional cost. |
| 3 | Interpret a fresh frontier, calculate an opportunity cost, and distinguish unused capacity from expanded capacity. |
| 4 | Predict reward, penalty and interest-rate incentives, and explain expected mutual gains from exchange. |
| 5 | Explain a policy-goal conflict and trace incentives, costs and benefits across groups using a source. |
| 6 | Compare the four decision systems and distinguish property rights from their enforcement. |

Reserve these cases from worked examples and the day 7 assessment. Replace “independent exit tickets for every teaching day” in “Still to make” with the remaining production work only.

### 2. Moderate: The assessment needs a specified compact response form

**Location:** `s01.md`, field 5, administration and items 1 to 12.

**LAYER:** plan. **REPEAT:** unassessed. **Confidence:** judgment call.

Forty minutes must accommodate three sources, a frontier, definitions and examples, a twelve-cell systems comparison, several explanations and a sourced counterargument. The plan gives no internal allocation or response format. A lesson writer could reasonably turn each numbered row into a separate written response, producing an assessment substantially larger than its allocation.

**Exact fix:** Specify grids for resources, systems and incentives. Make items 8 and 11 one shared policy paragraph with separate scoring, and items 10 and 12 one shared institutional explanation. State that reading the sources is included in the forty minutes. Preserve every assessed component, but remove repeated requests to explain the same mechanism.

## Unit 2: Markets and prices

### 3. Moderate: The day 11 exit supplies equilibrium answers instead of the schedules needed to determine them

**Location:** `s02.md`, field 5, daily evidence for day 11.

**LAYER:** plan. **REPEAT:** unassessed. **Confidence:** firm.

The prompt announces where quantities match, then asks students to mark those points. It can reveal whether students label axes and identify market participants, but it cannot reveal whether they determine equilibrium from supply and demand. The “printed schedules” and accompanying text are not actually supplied.

**Exact fix:** Replace “quantities match at…” with three complete schedules and ask students to locate the matches. These preserve the intended answers:

| Market | Price or rate | Quantity demanded | Quantity supplied |
|---|---:|---:|---:|
| Bread | 2 | 90 | 30 |
| Bread | 5 | 60 | 60 |
| Bread | 8 | 30 | 90 |
| Gardening labor | 12 | 44 | 12 |
| Gardening labor | 16 | 28 | 28 |
| Gardening labor | 20 | 12 | 44 |
| Loans | 5% | 100 | 60 |
| Loans | 7% | 80 | 80 |
| Loans | 9% | 60 | 100 |

Label quantities as loaves, weekly labor hours and thousands of money units respectively. Keep the existing participant and consumer-choice questions.

### 4. Minor: The next-unit handoff retains a superseded diagnostic draft

**Location:** `s02.md`, field 4, “Next unit handoff”; compare `s03.md`, field 4.

**LAYER:** plan. **REPEAT:** unassessed. **Confidence:** firm.

Unit 2 retains proposed postwar-readiness questions and provisional answers, although unit 3 supplies the final questions and a more precise geographical distinction about reconstruction aid. Two versions leave the administering teacher uncertain which is authoritative.

**Exact fix:** Replace the proposed questions and answers with:

> Administer the two items in `s03.md`, field 4, verbatim, once on day 18. Use that field’s final answer key and pass the item-level results to day 24.

## Unit 3: Business, competition and work

### 5. Moderate: Eight minutes is an inadequate planning allowance for items 11 to 13 as written

**Location:** `s03.md`, field 5, administration and items 11 to 13.

**LAYER:** plan. **REPEAT:** unassessed. **Confidence:** judgment call.

Those eight minutes include four investment mechanisms, a frontier drawing, two added-revenue calculations, an explanation of earnings, three growth mechanisms and interpretation of productivity and compensation evidence. Items 11 and 13 also request overlapping explanations. The allocation risks measuring writing speed and completion more than economic reasoning.

**Exact fix:** Make items 11 and 13 share one four-row causal diagram and one short interpretation of source D, scored separately for the two standards. Use a two-cell calculation for item 12. Change the forty-minute allocation to:

- Items 1 to 4: ten minutes, using comparison grids.
- Items 5 to 8: ten minutes, using the supplied calculation table.
- Items 9 and 10: eight minutes.
- Items 11 to 13: twelve minutes.

These remain untested estimates.

### 6. Minor: The retail concentration item does not name its market precisely enough

**Location:** `s03.md`, field 5, day 23 exit; field 10, retail-concentration description.

**LAYER:** plan. **REPEAT:** unassessed. **Confidence:** firm.

The 65.2% figure concerns food sales through specified outlet types. “The 20 largest retailers” and “sales in the covered US outlets” can be read as all retail sales, weakening the very market-boundary distinction the item teaches. The [source specifies food retailers and the covered food-sales denominator](https://www.ers.usda.gov/topics/food-markets-prices/retailing-wholesaling/retail-trends).

**Exact fix:** Replace that sentence with:

> In 2022, the 20 largest food retailers accounted for 65.2% of US food sales at supermarkets, other grocery stores, warehouse clubs and supercenters.

Use the same denominator in the source card and answer key.

## Unit 4: Government in the economy

### 7. Moderate: The day 30 exit asks students to mark quantities on an unspecified graph

**Location:** `s04.md`, field 5, day 30 daily evidence.

**LAYER:** plan. **REPEAT:** unassessed. **Confidence:** firm.

The prompt describes the relative positions of private and social costs but supplies neither a graph nor numerical schedules. “Mark private and socially preferred quantities” therefore depends on an unwritten representation.

**Exact fix:** Replace that instruction with:

> Sketch and label demand, marginal private cost and marginal social cost, placing marginal social cost above marginal private cost. Label the private and socially preferred intersections. Which quantity is greater, and why?

Keep the policy evaluation and its negative-nine answer. The revised key should require private quantity greater than socially preferred quantity, with uncompensated smoke damage explaining the difference. No numerical quantity is required.

The historical tax rates and federal funding-chart figures checked against their cited sources were consistent with the plan.

## Unit 5: Measuring the whole economy

No additional unit-specific finding.

The separation of market and aggregate graphs, nominal and real growth, price levels and inflation, and accounting relationships and causal claims is sound. The current assessment observations match the dated [GDP release](https://www.bea.gov/news/2026/gdp-advance-estimate-3rd-quarter-2026), [employment release](https://www.bls.gov/news.release/archives/empsit_11062026.htm) and [consumer-price release](https://www.bls.gov/news.release/archives/cpi_11102026.htm), including the unavailable October 2025 comparison.

The handoff that completes D2.Eco.10’s money-supply work in unit 6 is explicit and instructionally sensible.

## Unit 6: Money, banks and policy

### 8. Moderate: The principal writing task has uneven documentary support for its two institutional choices

**Location:** `s06.md`, field 2, closing claim; field 5, day 49 argument; field 10, source pack.

**LAYER:** plan. **REPEAT:** unassessed. **Confidence:** likely.

Students judge Congress against the central bank using several central-bank records, including an internal monetary-policy disagreement. Fiscal policy receives conceptual teaching, but the named documentary comparison supplies no equivalent fiscal-policy record. A student arguing for congressional action has less source evidence available.

**Exact fix:** Replace the repeated December 2008 extract in day 49’s comparison pack with an original, approximately eighty-word summary of the [Congressional Budget Office’s retrospective assessment of the recovery legislation](https://www.cbo.gov/publication/49958). Include its spending and tax channels, implementation delays and model-based estimation limits. Keep the December 2008 material for the day 45 hook.

Revise the writing look-fors to require evidence about both institutional options before the student defends either option or coordination. Fit this substitution inside the existing source-comparison allocation.

The checked money-stock figures, current money definitions and [zero reserve-requirement statement](https://www.federalreserve.gov/monetarypolicy/reservereq.htm) were consistent with the official sources.

## Unit 7: Trade and the global economy

No additional substantive plan finding.

The comparative-advantage calculations, beneficial exchange ratio, reciprocal currency calculations and productivity comparisons checked correctly. The distinction between observed exports and evidence of opportunity costs is particularly important and should remain.

The mechanical “frame names no model” statement is false. Its correction belongs to the generator finding under “For the structure pass.”

The two steelworker accounts should retain their distinct contexts: [Stone describes import competition and impending job loss](https://usw.org/news/bad-trade-deals-changes-my/), while [Wolfe describes recall following tariff protection](https://www.americanmanufacturing.org/blog/why-a-phone-call-was-a-lifesaver-for-this-steelworker-and-others-in-his-tight-knit-community/). The latter should not be presented during production as evidence of a worker gaining from increased imports.

## Unit 8: Earning, spending and protecting

### 9. Serious: Several daily goals have no written independent evidence

**Location:** `s08.md`, fields 5 and 10.

**LAYER:** plan. **REPEAT:** unassessed. **Confidence:** firm.

The assessment is complete, and the informed-action product supplies evidence on days 62 and 63. However, the plan leaves exit tickets unwritten for job choice, the pay-stub budget, payment comparisons, the practice tax return and insurance. The tax case itself also remains unwritten. The reserved day 66 pack cannot serve as teaching or exit material.

**Exact fix:** Add fully specified daily-evidence items for days 59, 60, 61, 64 and 65, each with fresh inputs, answers and error letters. Map the existing individual research record and information piece to days 62 and 63 instead of adding redundant exit tasks.

For day 64, specify the fictional filer’s tax year, filing and dependency status, wages, withholding, supplied deduction, tax-table entry and keyed refund or amount owed. Include a separate identity-protection response. Keep the existing practice-only restriction.

### 10. Serious: The advertising assessment measures fraud-report composition rather than effects on purchasing

**Location:** `s08.md`, field 5, source B, item 3 and its sample response.

**LAYER:** plan. **REPEAT:** unassessed. **Confidence:** firm.

The percentages describe the composition of reported social-media fraud losses. They do not estimate how advertising changes purchasing decisions. The additional question about targeting permits a general explanation disconnected from the numerical evidence. This leaves the data-based part of MA.PFL.T1.4 inadequately assessed. Compare the [anchor standard, printed page 174](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf), with the [fraud source’s reporting population](https://www.ftc.gov/news-events/data-visualizations/data-spotlight/2023/10/social-media-golden-goose-scammers).

**Exact fix:** Keep the fraud chart for consumer-protection teaching. Reserve the [Lewis and Reiley purchasing experiment](https://davidreiley.com/papers/OnlineAdsOfflineSales.pdf) for the assessment instead, using an original summary of its randomized design, approximately 1.6 million customers and estimated 5% purchase increase.

Replace item 3 with:

> What does the estimated 5% increase describe? Explain how the experiment connects advertising with purchases. Does it establish that every customer bought more, or that every advertising campaign would have the same effect? Explain one limit.

The key should distinguish an average estimated effect in that experiment from an individual guarantee or universal prediction. Update the contrasting samples accordingly.

To preserve an unseen source and fresh case, replace the teaching example with an original summary of the different [Blake, Nosko and Tadelis experiment](https://faculty.haas.berkeley.edu/stadelis/BNT_ECMA_rev.pdf). Preserve authorship and industry involvement in production records, with unbranded student copy.

### 11. Moderate: Day 65 has no allocated time for its closing claim

**Location:** `s08.md`, field 2, closing claim and teaching moves.

**LAYER:** plan. **REPEAT:** unassessed. **Confidence:** firm.

The closing claim requires students to combine advertising evidence, protection advice and insurance quotes, including a counterclaim. The stated allocation already consumes all fifty minutes with insurance purposes, quote comparisons, identity protection and an exit ticket.

**Exact fix:** State this allocation explicitly:

> Insurance purposes 10 minutes; quote comparison 15; identity protection 10; closing claim 10; independent exit ticket 5.

Make the closing claim and exit ticket distinct tasks. These remain untested estimates.

## Unit 9: Saving, credit and investing

### 12. Serious: Daily evidence remains incomplete despite the retained-product system

**Location:** `s09.md`, field 5, retained products; field 10, “Still to make.”

**LAYER:** plan. **REPEAT:** unassessed. **Confidence:** firm.

The retained products provide substantial evidence on research and planning days. They do not replace written checks of day 68’s interest concepts, day 70’s credit terms and reporting rights, day 72’s car-and-college comparison, or day 73’s asset-price reasoning. The running teaching offer and college aid offers are also unspecified, while assessment cases are reserved.

**Exact fix:** Add a daily-evidence map for days 68 to 76. Point to existing individual products where they already measure the goal. Write fresh, fully keyed items for days 68, 70, 72 and 73.

Supply the teaching offer and payment table used on days 70 to 72. Supply two fictional college aid offers showing cost of attendance, grants, work earnings, loan amounts and repayment totals. Require students to distinguish net price from borrowing and work earnings. Keep the assessment’s Ari cases withheld.

### 13. Moderate: Saving-policy descriptions alone cannot support the intended effectiveness judgment

**Location:** `s09.md`, field 5, retained item 4; field 10, day 69 sources.

**LAYER:** plan. **REPEAT:** unassessed. **Confidence:** likely.

The two tax-agency cards explain policy mechanisms and restrictions. They contain no participation or outcome evidence. Students can compare hypothetical usefulness and correctly identify insufficient evidence, but the supplied pack does not support a substantive judgment about how well the incentives work.

**Exact fix:** Add a third short evidence card using the [federal audit report on education-saving participation](https://www.gao.gov/products/gao-13-64). Label its 2010 observations and 2012 publication prominently. Use its participation and income-distribution findings as historical evidence about reach, not as current prevalence or proof of a causal saving effect.

Change item 4’s look-fors to require a policy mechanism, evidence about reach, an access limitation and a distinction between participation and additional saving caused by the policy. Three short cards remain within the plan’s stated reading limit.

The checked compound-interest, loan-cost and portfolio answers were correct. The [credit-rate protections](https://www.consumerfinance.gov/ask-cfpb/when-can-my-credit-card-company-increase-my-interest-rate-what-can-i-do-to-get-the-rate-back-down-en-69/), [free-report access](https://www.consumerfinance.gov/ask-cfpb/how-do-i-get-a-free-copy-of-my-credit-reports-en-5/) and [medical-debt rule vacatur](https://www.consumerfinance.gov/rules-policy/final-rules/consumer-reporting-regulation-v/) were consistent with the cited official guidance.

## What should remain

Keep the fictional financial offers, privacy rules, paper paths, conditional economic predictions and component-level scoring. Keep the distinctions between concentration and proven market power, money creation and free wealth, nominal returns and purchasing power, and diversification and guaranteed safety.

The main sequence of models and the explicit response-day handoffs are coherent. I found no invented source established as real among the sources I could trace. Clearly labelled invented assessment material should retain those labels.

## For the fixer

Apply these edits in order:

1. Complete daily-evidence maps and missing keyed items in units 1, 8 and 9. Reuse existing individual products where appropriate.
2. Repair unit 8’s advertising assessment and reserve its replacement source from teaching.
3. Complete unit 8’s tax case and unit 9’s running credit and college-aid cases.
4. Add the missing unit 2 schedules and repair unit 4’s graph instruction.
5. Add the fiscal-policy evidence in unit 6 and the saving-policy evidence in unit 9.
6. Correct the food-sales denominator in unit 3.
7. Replace unit 2’s provisional handoff with the reference to unit 3’s final diagnostic.
8. Specify compact response forms for unit 1 and combine duplicated productivity explanations in unit 3.
9. Apply the revised unit 3 and unit 8 minute allocations.
10. After the generator repair below, correct the affected mechanical model fields and rerun the economics checks.

### Settled by the expert

| Choice | Reason |
|---|---|
| Use the supplied day 11 market schedules. | They preserve the intended equilibria while requiring students to determine them. |
| Combine unit 3 items 11 and 13 through one causal diagram. | It removes duplicate writing while preserving separate standard judgments. |
| Substitute fiscal evidence for a repeated monetary extract. | It supports both institutional choices within existing time. |
| Reserve the purchasing experiment for unit 8’s assessment. | It directly measures the claimed data-based purchasing standard. |
| Map retained products before adding exit tickets. | It closes evidence gaps without unnecessary extra assessment. |

No scope, money, audience or outside-person decision is required for these edits.

## For the structure pass

### 1. Repair plural-unit parsing in the skeleton generator

**Severity:** minor. **LAYER:** process. **REPEAT:** unassessed. **Confidence:** firm.

`scripts/unit_skeleton.py`, `frame_models()`, uses a singular `unit N` match for social studies. It misses references such as “Units 3, 4 and 9” and “Units 8 and 9.”

I reproduced empty model results for units 7, 8 and 9 despite the frame’s explicit references. The existing `unit_nums()` helper correctly parsed the same plural strings.

Use `unit_nums()` for the social studies branch as well. Correct the generated model lists, particularly opportunity cost in unit 7, budgets in units 8 and 9, and supply-demand in unit 9. Preserve the valid carried-model prose already written.

### 2. Resolve the one-section document contract

**Severity:** moderate. **LAYER:** process. **REPEAT:** unassessed. **Confidence:** firm.

`UNIT-PLAN.md` requires a merged document for a one-section unit. All nine plans identify one section, but defer a separate section plan. Meanwhile, `unitplan.py` explicitly assumes separate section plans and applies that document model.

Make the template, writer brief and checker agree about what must be complete at this layer. Explicitly state where daily evidence belongs. A passing unit-plan check should not obscure missing evidence required by `plan-read.md`.

### 3. Extend checking beyond code presence

The current gate verifies that an assessment row names a code and contains item text. It does not establish that the item measures the code, that referenced inputs exist, or that daily goals have evidence.

Add structural checks for daily evidence and referenced input tables. Preserve a human-readable distinction between structural passage, checked arithmetic and content review. The unit 8 advertising mismatch illustrates why code presence cannot certify alignment.

### 4. Preserve dated sources and record access limits

Retain edition, date and table identifiers for assessed figures, especially sources reached through changing URLs.

This review could verify the principal current releases and several historical sources directly. The Chilean water report’s indexed executive summary supported its quoted figures, but direct retrieval timed out. The New York online framework and Neumark and Shirley PDF were not fully accessible in this environment; local PDF extraction libraries were also unavailable. Tennessee’s detailed comparison remains unverified as the plans disclose.

The new fiscal-policy, advertising and saving-participation sources linked above should enter the source list with their reading extent and reuse restrictions. Timing judgments in this report are professional judgments, not classroom measurements. Anticipated error frequencies remain “from memory,” as the drafts correctly state.
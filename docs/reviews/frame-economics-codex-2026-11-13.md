# Independent expert cold read: Economics course frame

**Date:** 2026-11-13  
**Intended report path:** `docs/reviews/frame-economics-2026-11-13.md`  
**Delivery:** Complete report below. No file was created or edited.

## Verdict

The frame has a coherent sequence and complete structural placement, but it needs revision before its allocations become fixed. Its largest risk is shallow coverage inside a compressed half year, especially where personal finance combines substantial decisions, research, informed action and assessment. Secure the missing standard requirements and demonstrate a task-based time budget before advancing the course.

**Finding count: 9 consolidated findings, including 6 process findings.**

## What I read and checked

I read:

- `docs/agents/EXPERT.md`, the social studies lens, the shared adoption bar and its social studies section.
- `docs/courses/social-studies/STANDARD.md`, `docs/FOUNDATION.md`, the relevant ROADMAP sections, BASELINE rules 20 to 24 and the glossary.
- `docs/APPROACH.md`, the source-access guidance and relevant evidence notes in `docs/APPROACH-SOURCES.md`. No social studies approach page was present.
- The complete Economics frame, its `frames.csv` entry and all 25 `econ-` progression rows.
- The grade 11 and 12 social studies progression rows and the earlier rows supplying Economics prerequisites.
- The Government and US History II frames, and the Economics handoff material in the Civics, World History II and US History I frames.
- The loaded economics, personal finance and C3 standard records; the relevant mathematics and earlier ELA progression rows.
- The social studies progression reviews, their fix report, the cross-subject reviews and fixes, the open-material review, `BASE-TEXTS.md` and the relevant decision entries.

Outside checking used the primary sources linked below. **No substantive finding rests on memory.** Pacing recommendations are identified as judgments.

### Gate results

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Could not complete: `ModuleNotFoundError: No module named 'markdown'` |
| `python -B -X utf8 scripts/frame.py check economics` | 0 failures |
| `python -B -X utf8 scripts/progression.py check social-studies` | 384 rows, 0 failures |
| `python -B -X utf8 scripts/stale.py check` | Final run: 19 files, 0 failures |

The global command crashed during dependency import, rather than returning a completed validation result. This is therefore a **conditional content review**, supported by the separate checks, not evidence of a successful full plan gate. Nothing was installed or altered.

### Structural coverage

| Item | Result |
|---|---:|
| Economics progression skills | 25, each placed once |
| Units | 9 |
| Owned Massachusetts codes | 83: 59 Economics and 24 Personal Financial Literacy |
| Distinct C3 indicators assigned to Economics rows | 16 |
| Unit days | 76 |
| Course-level assessment and respond days | 4 |
| Total | 80 |

Other grades’ skills are generally distinguished appropriately: earlier knowledge returns through retrieval or reteaching, and the globalization indicators carry an explicit increase in depth.

## Findings, most serious first

### 1. Several standard requirements remain unsecured despite complete code placement

**LAYER:** frame, progression and standard  
**REPEAT:** yes, the semantic coverage problems in the earlier social studies progression reviews  
**Confidence:** firm on the requirements; likely on the instructional omissions

The frame sometimes names a topic without preserving the required comparison, analysis or investigation.

| Location | What is wrong | Exact fix |
|---|---|---|
| Unit 4, `MA.PFL.T1.3` | Reading historical rate tables does not secure analysis of their effects across income levels. The progression has the same narrowing. | Require a comparison of tax effects on supplied low-, middle- and high-income profiles at selected dates from 1950 onward. Supply suitable tax estimates and explain the limits of comparisons across years. |
| Unit 9, `MA.ECON.T6.5` | Credit, saving and investing appear, but comparing financial institutions’ services is not explicit. | Require a comparison matrix covering fictional institutions’ credit, savings and investment services, including costs, access, liquidity and risk, followed by a justified choice for a supplied person. |
| Unit 9, `MA.ECON.T6.6` | Tracking a supplied fictional portfolio secures monitoring more clearly than research. | Before tracking, require students to investigate asset types through a curated source pack, justify selections and record sources. Then track the fictional holdings across several dated observations. |
| Unit 9, C3 column | `D2.Eco.12.9-12` is claimed as practice, but evaluating financial regulators does not by itself practise selecting fiscal and monetary policies for different conditions. | Remove this practice claim unless Unit 9 includes an actual policy-selection transfer task. Keep ownership in Unit 6. |

The first three requirements were checked against the official [Massachusetts framework, pages 172 and 174](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf). The distinction in the last row comes from [C3 indicator D2.Eco.12.9-12](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf).

**Why it matters:** a writer following the present summaries could produce accurate lessons that still omit the work the listed codes require.

### 2. The time justification still relies too heavily on rows

**LAYER:** frame  
**REPEAT:** yes, the earlier progression reviews and cross-subject review explicitly requested a days-based Economics budget  
**Confidence:** likely; exact allocations remain a judgment call

The total fits the repository’s half-year yardstick. That does not establish that the work fits.

Allowing one end-of-unit assessment day and one respond day per unit leaves:

| Unit | Total days | Skills | Owned codes | Days remaining before readiness and reteaching |
|---|---:|---:|---:|---:|
| 1 | 8 | 3 | 12 | 6 |
| 2 | 10 | 3 | 11 | 8 |
| 3 | 9 | 3 | 13 | 7 |
| 4 | 7 | 2 | 10 | 5 |
| 5 | 9 | 2 | 8 | 7 |
| 6 | 7 | 2 | 8 | 5 |
| 7 | 6 | 2 | 11 | 4 |
| 8 | 7 | 3 | 7 | 5 |
| 9 | 13 | 5 | 19 | 11 |

These are planning allowances, not a claim that readiness checks each consume a whole day.

**Unit 8 is the clearest pressure point.** Its five remaining days must include readiness, potentially a full lesson of budget reteaching, income and job choices, a first-year budget, advertising evidence, payment comparisons, consumer protection, insurance comparisons, identity protection and the public information piece. Pay-stub reading, withholding, tax filing and renting are added as well.

**Unit 7 is also tight:** four remaining days cover comparative advantage, barriers, trade balances, exchange rates, productivity trends and globalization’s economic, social and environmental consequences.

Unit 9 has the largest allocation, but it also carries 19 codes and several substantial products. It is not an obvious donor merely because its number is larger.

The anchor originally describes Economics as a full-year elective and personal finance as a quarter- to half-year body of work. That does not override Cory’s half-year decision, but it strengthens the need to demonstrate this compression. [Massachusetts framework, pages 19 and 173](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf). As a concrete pacing comparison, the federal agency’s introductory high school insurance activity alone allocates 45 to 60 minutes. [Exploring types of insurance](https://www.consumerfinance.gov/documents/7247/cfpb_building_block_activities_exploring-types-of-insurance_guide.pdf).

**Exact fix:** replace the “2 to 5 days a row” assurance with a provisional, task-based allocation. For Units 7, 8 and 9, identify the teaching, guided practice, independent work, research or product work, assessment, response and readiness allowance. Keep additions explicitly conditional on that budget. Merging `econ-credit` and `econ-borrowing-plan` must not be represented as saving time unless actual repeated work is identified.

**Why it matters:** otherwise the likely adjustment occurs during writing, when inquiry, practice or response time is easiest to squeeze out.

### 3. Unit 5 needs an explicit bridge before explaining money-supply effects

**LAYER:** frame and progression  
**REPEAT:** yes, the prerequisite-timing problems identified in the cross-subject reviews  
**Confidence:** likely

`econ-business-cycles`, owned in Unit 5, requires students to explain money-supply effects using current data. The course’s explicit treatment of what constitutes the money supply and how banking works sits in Unit 6. Earlier history supplies banking crises and tight-money examples, but the receiving frame does not state the conceptual bridge.

**Exact fix:** add to Unit 5’s learning and order statements:

> Before the money-supply explanation, retrieve the earlier banking-crisis example and explicitly distinguish money available for payments, including deposits, from income and real output. Use a supplied data case. Unit 6 later develops the banking mechanisms and policy tools.

Record this as prerequisite teaching within Unit 5’s existing days. No ownership move is needed.

**Why it matters:** students can otherwise confuse a change in money with a change in production or income. [C3 D2.Eco.10.9-12](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf) requires the money-supply component.

### 4. Five Economics notes still contradict the settled entry grades

**LAYER:** process  
**REPEAT:** yes, the earlier social studies placement and stale-note findings  
**Confidence:** firm

The following rows still state that Government and Economics are grade 12 courses:

`econ-scarcity-choice`, `econ-taxes-budgets`, `econ-trade`, `econ-global-economy`, `econ-earning-income`.

The tax row also says it builds on the 16th Amendment from grade 11 before later explaining that the example is retaught. The frame accurately flags these defects, but the contradictory instructions remain in the progression.

**Exact fix:**

- Replace the grade restriction with: “Economics is available in grade 11 or 12; grade 12 is its storage label in this data.”
- Describe the grade 8 return as two or three intervening grades, depending on entry.
- Describe the grade 10 return as immediate in grade 11, or after one intervening grade in grade 12.
- Replace the tax prerequisite sentence with: “The 16th Amendment is retaught briefly here; prior completion of US History I is not required.”

**Why it matters:** a downstream writer may follow the earlier prerequisite sentence and assume knowledge that a grade 11 student has not reached. The controlling record is `DESK-ANSWERS.md`, card `q-ss-progression-1`.

### 5. Earlier review results still describe course placement as undecided

**LAYER:** process  
**REPEAT:** yes, stale decision-status notes  
**Confidence:** firm

Two current-looking results are obsolete:

- `progression-social-studies-fixes-2026-11-13.md`, the Codex 3 table entry and “Skipped, needs Cory” entry.
- `progression-cross-codex-2026-11-13.md`, “For Cory,” where the placement question remains open.

**Exact replacement status note:**

> Resolved by q-ss-progression-1 on 2026-11-13: Government and Economics may be taken in grade 11 or 12. Rows remain stored at grade 12. US History I completion is not required; historical examples are retaught locally.

Retain the original review observations as dated history, with this update immediately beside them.

**Why it matters:** leaving the decision open invites another unnecessary scope discussion.

### 6. The progression fix report still says cross-subject checking awaits the progressions

**LAYER:** process  
**REPEAT:** yes, stale prerequisite and completion notes  
**Confidence:** firm

`progression-social-studies-fixes-2026-11-13.md`, “Skipped, needs Cory,” Codex 6, says the ownership check waits on the other progressions. The later cross-subject reviews and `progression-cross-fixes-2026-11-13.md` now record that work and its resulting repairs.

**Exact replacement:**

> Subsequently addressed by the cross-subject reviews and progression-cross-fixes-2026-11-13.md. Use that report and the current progression rows for the repaired references and readiness conditions.

**Why it matters:** the obsolete note directs another reader to repeat completed work instead of checking the remaining within-year timing.

### 7. The earlier social studies review still says partial bases are unloaded

**LAYER:** process  
**REPEAT:** yes, stale completion notes  
**Confidence:** firm about the repository records

`progression-social-studies-codex-2026-11-13.md`, coverage inventory, says the candidate partial bases are not yet loaded. `BASE-TEXTS.md` now records the relevant loaded collections, including the retired economics text and financial education activities.

**Exact replacement status note:**

> Update, 2026-11-13: BASE-TEXTS.md records the relevant partial bases as loaded. Economics still has no whole-course base text, so a complete base-course lesson map is not required at the progression layer.

**Why it matters:** “not loaded” could cause unnecessary acquisition work or prevent use of available material.

### 8. The open-material review retains approval holds Cory has settled

**LAYER:** process  
**REPEAT:** yes, stale decision-status notes  
**Confidence:** firm

`social-studies-open-material-2026-11-13.md` still asks Cory to decide the retired texts’ use and acceptance of the Open Government Licence. Its government recommendation, “Traps,” proposed partial bases and open-items list retain those holds.

**Exact replacement status note at those locations:**

> Resolved by q-ss-partial-bases on 2026-11-13: the Open Government Licence v3.0 is accepted subject to item-level rights checks, and the named retired CC BY editions may serve as partial bases. Current restrictive editions remain reference only. Follow BASE-TEXTS.md.

This records Cory’s decision without making a new legal determination.

**Why it matters:** the stale holds conflict directly with the Economics frame’s permitted source plan.

### 9. ROADMAP still says the social studies content standard is undecided

**LAYER:** process  
**REPEAT:** yes, stale planning-state notes  
**Confidence:** firm

The “Subjects outside the core” paragraph says social studies waits on an open content-standard decision. `STANDARD.md`, the loaded anchor and the decision record show that the choice has been made.

The ROADMAP header acknowledges superseded build-order instructions, but that does not accurately restate this separate decision.

**Exact replacement:**

> Social studies’ content standard was settled on 2026-11-13: C3 skills, Massachusetts 2018 content in the adopted course order, the named check set and the own-state method. Planning follows PRODUCTION-PATH.md.

**Why it matters:** a required orientation document still identifies a resolved decision as a blocker.

## Seams, sources and cross-subject checks

| Check | Judgment |
|---|---|
| Earlier economic reasoning | Picked up appropriately from Civics and World History II, with retrieval and named reteaching. |
| US History I dependency | Removed as an entry requirement. Residual wording remains in Finding 4. |
| US History II overlap | Properly treated as an independent review toolkit. Neither course requires the other. |
| Successor economics course | None. The terminal applications to personal decisions and civic reasoning are reasonable. |
| Graphs and percentages | Supported by earlier mathematics progression rows. |
| Compound growth | Supported by Algebra I’s constant-percent growth work. |
| Loan formulas | The supplied-payment-table bridge appropriately protects grade 11 entry. |
| Same-grade mathematics frame | No Algebra II frame was available to verify its calendar. The local bridge avoids dependence on that calendar. |
| Writing and research | Earlier ELA and history provide a foundation. Economics must still model its own economic evidence tasks. |
| Whole-course source map | Not applicable: Economics has no adopted whole-course base text. No `source-map.csv` was present. |
| Partial bases | Appropriate in principle under the repository’s source record. Individual adaptations and credits remain unit- and day-level checks. |

No unnecessary standard move between units is recommended.

## Lens checklist: course frame layer

| Lens line | Mark | Evidence |
|---|---|---|
| Every anchor standard in the course range has a unit | **Met for placement; missed in part for full treatment** | All codes are placed. Finding 1 identifies unsecured requirements. |
| Replaced grade 3 year or grade 8 “your state” retains Massachusetts-only content | **Not applicable** | This is a national high school economics course. |
| Units record check-set additions and their sources | **Met at frame level** | Candidate additions and source families are named. Exact comparisons belong to the unit plans. |

The frame also preserves compelling questions, direct teaching of economic models, unseen assessment tasks, student-chosen informed action and protections against personal financial disclosure. Actual source difficulty, corroboration routines, counterclaims and daily assessment quality cannot yet be verified.

## Settled by the expert

| Choice | Reason | File affected when applied |
|---|---|---|
| Keep the nine-unit sequence | Its main conceptual dependencies hold. | `docs/courses/economics/frame.md` |
| Keep loan-formula derivation optional | Supplied payment tables allow the required borrowing comparison for either entry grade. | Economics frame and borrowing-plan notes |
| Add the brief money-supply bridge inside Unit 5 | Repairs first use without moving ownership. | Economics frame |
| Use supplied income profiles and tax estimates | Secures the analytical comparison without requiring family disclosure or advanced tax calculation. | Economics frame and tax-row notes |
| Research asset types before tracking fictional holdings | Preserves investigation while retaining the course’s fictional examples. | Economics frame and investing-row notes |
| Do not count a row merger as an automatic time saving | The required learning and assessment remain. | Economics frame, “For the lead” |

These are recommendations for the caller to apply. No edits were made.

## What is right and should not be undone

- Scarcity precedes markets, which precede competition and government intervention.
- Market and aggregate supply-demand models have distinct names and axes.
- Personal finance uses economic ideas already developed earlier in the course.
- Grade 11 access is protected by local historical explanations and the payment-table bridge.
- Fictional offers, no family financial disclosure and student-chosen action are sound design choices.
- Course-level assessments retain respond days.

## For Cory

- **Scope only if the detailed budget fails:** the existing 80-day decision stands. If full coverage cannot fit after planning, bring a concrete duration or content-placement alternative rather than silently cutting standards, practice or response time.
- **School-facing timetable advice:** the suggested Government-first, Economics-second arrangement remains an audience and scheduling recommendation to settle, not a prerequisite.

## Limits and sources

The full plan gate remains unverified. This read does not establish classroom timings, completed unit assessments, individual adaptation rights or a finished course’s adoption-bar result. New York’s PDF returned a fetch error and Tennessee’s page returned an access denial, so neither supports a new substantive finding here.

Sources checked:

- [Massachusetts History and Social Science Framework, 2018](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf): original Economics and personal finance requirements and intended course sizes.
- [C3 Framework](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf): economic reasoning indicators and the distinction between policy selection and regulatory evaluation.
- [CEE economics standards, 2010](https://www.councilforeconed.org/wp-content/uploads/2012/03/voluntary-national-content-standards-2010.pdf): marginal reasoning and economic decision-making reference.
- [National Standards for Personal Financial Education, 2021](https://files.consumerfinance.gov/f/documents/2021_Natl_Standards_Downloadable_final.pdf): comparison of the finance domains and decision demands.
- [California economics standards](https://www2.cde.ca.gov/cacs/history?c0=13,0,4&dl=0&maxgrade=12&mingrade=0&order=0&perpage=100): check-set content, including international trade.
- [Microeconomics course overview](https://apcentral.collegeboard.org/courses/ap-microeconomics): comparison reference for models, marginal analysis and market failure.
- [Exploring types of insurance](https://www.consumerfinance.gov/documents/7247/cfpb_building_block_activities_exploring-types-of-insurance_guide.pdf): a concrete high school activity and its stated duration.

### For the source list

Add the economics, financial education and insurance links above to `APPROACH-SOURCES.md` if absent. Record the insurance activity’s stated grade band and duration; do not treat that duration as a measured minimum for every Curio Class lesson.

**Verdict:** revise before locking. **Findings:** 9. **Intended report path:** `docs/reviews/frame-economics-2026-11-13.md`, supplied here only.
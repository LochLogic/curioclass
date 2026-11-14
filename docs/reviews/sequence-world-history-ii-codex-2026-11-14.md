# Independent review: World History II scope and sequence

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/sequence-world-history-ii-2026-11-14.md`  
**Delivery:** Report supplied here only. No files were changed.

## Verdict

**Revise before unit writing.** The historical arc, unit allocations and course-level calendar are broadly sound, but several day goals and assessment descriptions leave required learning unsecured. The most important repair is to map each standard’s components to explicit student work and assessment evidence, while making the capstone’s independent research route concrete.

## What I read

- `docs/agents/EXPERT.md`, the social studies lens, the shared core and social studies adoption bar, and `docs/courses/social-studies/STANDARD.md`.
- FOUNDATION, the relevant ROADMAP sections, BASELINE rules 20 to 24, APPROACH, relevant APPROACH-SOURCES entries, GLOSSARY, and the sequence briefs.
- The complete World History II scope and sequence, all 160 day rows, its frame, and its source map.
- All 43 grade 10 social studies progression rows, with relevant prerequisite and receiving rows.
- CALENDAR.md, grade 10 calendar records, and relevant ELA 10 and chemistry frame sections.
- The local Massachusetts standards, C3 inventory and literacy-standard loading record.
- Both earlier World History II frame reviews, the earlier independent sequence review, and relevant repair reports.
- Outside sources linked below. The local partial textbook’s copyright page, contents, section headings and selected revolution passages were also inspected.

The earlier sequence review encountered an empty Markdown file. The current file contains the required prose, so that finding is closed. Previously repaired regional coverage, Cold War case selection and review-role decisions are not reopened here.

## Checks

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Could not complete because the sandbox lacks the `markdown` dependency. |
| `python -X utf8 scripts/frame.py calendar` | Passed, with no reported stagger-rule breaks. |
| `python -X utf8 scripts/frame.py check world-history-ii` | Passed: 11 units, 160 days, including 150 unit days and 10 course-level check/respond days. |
| `python -X utf8 scripts/plan.py check world-history-ii` | Passed: 0 failures. |
| `python -X utf8 scripts/stale.py check` | Passed: 56 files, 0 failures. |

The incomplete global gate does not withhold this curriculum verdict.

## Findings, most serious first

### 1. Required content is lost between the progression and the day goals

**Severity:** serious  
**LAYER:** sequence  
**REPEAT:** yes, the earlier independent World History II sequence review identified this kind of loss.  
**Confidence:** firm about the written omissions.

The codes are present, but several goals omit a required comparison, consequence or performance. These requirements appear in the local standards or progression notes; selected requirements were checked against the [official Massachusetts framework](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf), printed pages 149 to 156.

| Location | Exact repair |
|---|---|
| Days 10 to 11, `T1.7` | Compare Latin American political, social and economic developments with contemporary Europe. |
| Day 27, `T1.6` | Analyze causes, Cavour’s and Bismarck’s methods, and the changed balance of power alongside the maps. |
| Day 46, `T4.2b` | Explain what United States involvement changed for the war and affected peoples. |
| Day 60, `T4.6` | Include cultural experimentation, Lenin’s death and the succession struggle. |
| Day 63, `T4.7` | Evaluate an actual government response using the preceding evidence. |
| Days 68 to 70, `T4.10` | Include League failures, changing British and United States responses, Austria and Czechoslovakia. |
| Day 76, `T4.12` | Connect postwar plans and diplomacy to the war’s outcome and emerging Cold War. |
| Day 77, `T4.13` | Explicitly include Christian antisemitism among the Holocaust’s roots. |
| Days 81 to 82, `T4.14` | Analyze effects on Soviet relations. |
| Day 114, `T5.7d` | Explicitly explain military action’s role in Palestinian dispossession and displacement, using dated evidence. |

**Why it matters:** a writer can follow the current goals faithfully while omitting part of what the course claims to teach.

**Exact fix:** incorporate these performances into the existing days and their assessment descriptions. Retain ownership and unit totals. The progression already supplies much of the missing detail, so this is chiefly a repair to the sequence’s instructions.

### 2. Assessment descriptions do not secure all owned learning

**Severity:** serious  
**LAYER:** sequence  
**REPEAT:** yes, assessment coverage gaps recur in the earlier sequence review.  
**Confidence:** firm about the planning gaps; actual items remain unwritten.

Every unit has an assessment slot and unseen-source work. However, those features do not establish complete coverage.

| Location | Problem and exact fix |
|---|---|
| Unit 1, day 14 | `T1.2` and `D1.3` are absent from the assessment code list. Include the English contrast and supporting-question interpretation task. |
| Unit 2, day 25 | Reserve evidence for political decisions and urban, suburban and rural relationships, rather than relying on a generic data task. |
| Unit 3, day 38 | Specify how students demonstrate historical context and the perspectives of history’s writers alongside the map task. |
| Unit 4, day 57 | Its code list includes only two of the unit’s seven owned C3 indicators. Add explicit evidence for treaty/order reasoning, geographical consequences, source credibility and interpretation across media. |
| Units 5 and 6, days 71 and 87 | Carry the repaired performances from finding 1 into the assessment specifications. |
| Unit 8, day 120 | Map the eight Israel/Palestine components to evidence. Two accounts of one event cannot establish coverage of the entire sequence. |
| Unit 11, days 149 to 156 | The research argument is the only owned skill absent from every `assess=end` row. Day 155 checks global problems, while critique, research and audience adaptation sit outside its stated evidence. |

**Why it matters:** completing the named assessment could leave important learning unexamined. Attempting to repair everything through a single 50-minute examination would create a different problem.

**Exact fix:** add a compact component-to-evidence blueprint for each unit. Identify independently completed work that contributes to the end-of-unit assessment. For unit 11, define a composite assessment comprising the report, critique and revision, presentations, action reasoning and day 155’s unseen-source task. Complete its evidence on day 156 and respond once on day 157.

Unit 10 does not need an examination of every survey case in depth. Its definition, anchor-case analysis and terrorism response are appropriately bounded.

### 3. The capstone promises independent research without locating its teaching

**Severity:** serious  
**LAYER:** sequence  
**REPEAT:** yes, this remains unresolved from the earlier independent sequence review.  
**Confidence:** firm.

Grade 10’s stated advance is finding sources independently. Day 145 instead says to take a question and judge a source list. Subsequent days proceed through content, drafting and presentation without explicitly locating the independent search.

The paired course provides substantial preparation, but the history-only route merely says it runs the whole cycle. Day 150 also invokes ELA’s presentation teaching in the same week without naming a local model.

**Why it matters:** receiving and evaluating a supplied list can satisfy the written goal while missing the promised progression. A history-only teacher must invent the omitted research instruction.

**Exact fix:**

- On day 145, model locating and selecting evidence, then require an independent search through a bounded printed archive or index, with an equivalent device route.
- Require at least five useful sources, including primary evidence and historical interpretations, with selection and rejection reasons.
- Make the history-only question and archive available at that launch; distinguish its preparation from ELA’s earlier work.
- Add a local presentation model on day 150.
- Specify a workable panel format for day 152 and its history-only equivalent. The paired ELA plan allocates two days to its longer talks, while history currently names one.

Keep the 13-day unit. These are specifications of the existing research work, not an additional project.

Do not adopt the prose’s suggestion to fold the atrocity survey into a terrorism lesson to gain a research day. It would compress unrelated, sensitive material without solving the missing instruction.

### 4. The prose reintroduces a false common cause for dictatorship

**Severity:** serious  
**LAYER:** sequence  
**REPEAT:** yes, the earlier independent frame review identified and the frame corrected this error.  
**Confidence:** firm.

The scope and sequence’s unit 5 arc, line 77, says:

> The Depression comes before the dictators because it is their opening.

That wording contradicts the repaired frame and the dated day goals. Mussolini took power before the Depression, as the [Holocaust Museum’s account](https://encyclopedia.ushmm.org/content/en/article/benito-mussolini-1) confirms.

**Why it matters:** a writer following the prose can give all three regimes the same inaccurate causal explanation, despite the unit’s purpose of teaching historical causation.

**Exact fix:** replace that sentence with:

> The dated timeline distinguishes the routes to dictatorship. Mussolini’s rule and Stalin’s consolidation began before the Depression; the Depression intensified instability and helped the Nazi rise. Britain supplies the comparison with a surviving democracy.

Retain the day order and the dated comparison on day 67.

### 5. Several C3 performances remain narrower than their codes

**Severity:** serious  
**LAYER:** sequence, with a frame correction for climate geography  
**REPEAT:** yes, incomplete C3 endpoints recur in the earlier frame and sequence reads.  
**Confidence:** firm on the requirements; likely on implementation risk.

| Location | Exact repair |
|---|---|
| Days 1 and 12, `D1.3` | Explain expert agreement and disagreement about concepts in supporting questions, not only the compelling question. |
| Days 85 to 86, `D2.Civ.10` | Analyze how interests and perspectives affect the application of rights through a specific postwar case. |
| Day 127, `D2.Geo.11` | Connect globalization and resource competition to conflict and cooperation within countries as well as between them. |
| Day 146, `D2.Geo.9` | Include climate effects on migration and settlement alongside land and resource use. Restore these in the frame too. |
| Days 147 and 153, `D4.6` | Compare contexts across time and place, including causes, obstacles and opportunities. |
| Days 153 to 154, `D4.7` | Require self-reflection and a causal explanation of the strategy’s likely effects. |

These distinctions were checked against the [C3 Framework](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf), printed pages 24, 32, 42 to 43 and 61.

**Why it matters:** a relevant topic does not ensure that students perform the claimed reasoning.

**Exact fix:** add these performances to the existing tasks and scoring evidence. Also place `D3.2` on day 55, where expert valuation of sources is actually taught, rather than locating it only on day 54.

### 6. Unit 9 gives two substantial power standards one teaching day

**Severity:** moderate  
**LAYER:** sequence  
**REPEAT:** yes, the earlier independent sequence review identified this compression.  
**Confidence:** likely; the allocation is a professional judgment.

Unit 9 has ten teaching/application days. Its allocations include two days for science, three for globalization and resources, two for the Middle East, but only day 130 for European populism and China’s political and economic power together. Day 131 then repeats globalization synthesis.

**Why it matters:** two distinct contemporary standards receive a shared descriptive survey while another strand receives both evidence weighing and a separate concluding claim.

**Exact fix:** use day 130 for European populism, with platforms and election evidence, and day 131 for China, with economic and geopolitical evidence. Complete globalization’s concluding claim within day 126’s existing evidence-weighing task. Keep day 132’s assessment and the 12-day unit total.

This is a day swap within the unit, settled here.

### 7. The source map does not record its departures from textbook order

**Severity:** moderate  
**LAYER:** base text  
**REPEAT:** yes, source traceability remains unresolved from the earlier independent sequence review.  
**Confidence:** firm.

Every `order_conflict` cell is blank, although chapter 8’s Russia material precedes chapter 6 and the French Revolution precedes the American comparison. The prose explains some choices, but the mapping record does not preserve them.

There is also a concrete placement conflict: `etsu-06-french` describes material through Napoleon but assigns only days 4 and 5. Day 6 teaches Napoleon, yet its map row says no base passage fits. The local textbook contains substantial Napoleon material, including printed pages 69 to 72.

**Why it matters:** an adapter cannot reliably distinguish reordered, deliberately replaced and accidentally unmapped material.

**Exact fix:** assign the selected Napoleon passage to day 6, or explicitly cut it with a reason. Record the reorderings and their reasons, including the prior-year American Revolution recall that permits its later comparison placement. Give heading or page boundaries where passages split.

The [publisher record](https://dc.etsu.edu/etsu-oer/13/) confirms the partial base and licence. Preserve the separate checks for third-party images.

### 8. Active guidance contains contradictions and an unfinished pacing requirement

**Severity:** minor  
**LAYER:** process  
**REPEAT:** yes, stale guidance recurs in the earlier sequence review.  
**Confidence:** firm.

| Location | Exact fix |
|---|---|
| Frame, Days bullet | Replace blanket readiness wording with the sequence-writing rule: readiness for dormant prerequisites; retrieval for work maintained in the preceding year. |
| Frame, final “For the lead” item 2 | State that the sequence has settled candidates; unit plans verify comparisons and implement those decisions. |
| STANDARD.md and the adoption bar | Update the claim that literacy standards are unloaded. The file now exists; distinguish loading from ownership decisions. |
| Social studies lens, sensitive-history paragraph | Reconcile its qualified-person requirement with current FOUNDATION section 7.3 and the course’s agent-review policy. |
| Sequence, course-level calendar paragraph | Say that the checks match the frame/calendar records. CALENDAR.md’s named target-week table is for K to 8; grade 10 has the finals-week rule. |
| Sequence, pacing | Supply FOUNDATION’s shorter-period route. Identify shorter excerpts and reduced repetition while preserving contrasting accounts, required performances and assessment evidence. |

**Why it matters:** writers consulting required documents receive different instructions, and the course offers no concrete pacing guidance for shorter periods.

The stale checker’s zero does not settle these semantic contradictions.

## Order, standards placement and load

The main arc holds: revolutions, industry, empire, world wars, Cold War, independence, globalization, mass violence and global problems. The frame explains the thematic returns. Finding 4 is the material fault in the written ordering rationale.

| Unit | Total days | Teaching/application days | Load judgment |
|---|---:|---:|---|
| 1 | 15 | 13 | Reasonable with prior-year recall kept short. |
| 2 | 11 | 9 | Tight but coherent across causes, effects and reform. |
| 3 | 13 | 11 | Day 27 needs its full performance; day 31 needs tightly bounded Asian cases. |
| 4 | 16 | 14 | Heavy but coherent when Versailles evidence serves content and interpretation. |
| 5 | 14 | 12 | Workable after the causal rationale and response evaluation are repaired. |
| 6 | 16 | 14 | Proportionate allocation across war, Holocaust, bombs and consequences. |
| 7 | 15 | 13 | Defensible with one development in depth across both case rows. |
| 8 | 14 | 12 | Tight but proportionate, including four Israel/Palestine days. |
| 9 | 12 | 10 | Uneven allocation, repaired by finding 6. |
| 10 | 11 | 9 | Matches its explicit budget; preserve the survey day. |
| 11 | 13 | 11 | Plausible with a bounded search and concrete presentation arrangements. |

Each unit also contains one assessment day and one respond day. No unit exceeds 25 days, so no mid-unit assessment is required. No unit is demonstrably far overallocated.

All recorded lettered groups have destinations:

| Group | Days |
|---|---|
| `T1.1a` to `c` | 2 to 3 |
| `T3.2a` to `d` | 29 to 30 |
| `T3.4a` to `f` | 34 to 35 |
| `T4.2a` to `c` | 45 to 47 |
| `T4.3a` to `i` | 48 to 53 |
| `T4.7a` to `d` | 61 to 63 |
| `T4.10a` to `d` | 68 to 70 |
| `T4.15a` to `f` | 83 to 85 |
| `T5.3a` to `h` | 95 to 100 |
| `T5.7a` to `h` | 113 to 116 |
| `T5.11a` to `k` | 123, with selected depth on 124 |
| `T6.5a` to `b` | 146 to 147 |
| `T7.1a` to `j` | 135 to 140 |

Placement is established; complete teaching and checking require findings 1, 2 and 5. Legitimate example lists do not require equal-depth treatment of every example.

The absence of separate readiness days is defensible under the current writing rule. Relevant skills were maintained through grade 9, including the action cycle linking grade 8 to grade 10.

## Calendar and same-year leans

Course-level checks match the frame and calendar:

- Days 40 to 41, weeks 8 to 9; respond on 42.
- Days 89 to 91, weeks 18 to 19; respond on 92.
- Days 158 to 159, week 32; respond on 160.

| Lean | Result |
|---|---|
| Colonial literature | History precedes ELA’s days 46 to 60; grade 9 literature supplies prior preparation. |
| Interpretation critique | History days 54 to 55 precede ELA’s argument unit, days 61 to 85. |
| Written argument | Available before the capstone. |
| Research and presentation | Broad milestones align; finding 3 supplies the missing independent route and local presentation model. |
| Steam engine | Day 16 supplies the needed explanation locally. |
| Atomic fission | Day 81 carries its bridge before chemistry days 103 to 112. |
| Science case | Day 123 follows chemistry’s nuclear unit. |
| Climate forecast | Day 146 follows chemistry days 113 to 130. |

## Candidate cells

Every frame candidate has a written decision and an existing day allocation or drop reason.

| Unit | Settlement |
|---|---|
| 1 | Vienna on 6; Jamaica Letter on 10. |
| 2 | Meiji on 18. |
| 3 | Taiping/self-strengthening on 31; Tanzimat and indentured migration dropped for budget. |
| 4 | Balfour/Sykes-Picot on 51. |
| 5 | Three roads to war on 68 to 70; Salt March dropped. |
| 6 | Forced labour and the “comfort women” system on 75. |
| 7 | Space race on 96; Chile/military rule on 98. |
| 8 | Congo/Lumumba on 108; Indigenous rights declaration on 117. |
| 9 | Green Revolution on 125; other additions dropped or incorporated elsewhere. |
| 10 | No additional candidate. |
| 11 | Sustainable Development Goals within 146 to 147. |

Keep these decisions. Clarify that an optional India case does not guarantee the Salt March and Ottoman collapse does not teach Tanzimat. Their exclusion rests on the stated budget.

## Lens checklist: scope and sequence

| Checklist line | Result |
|---|---|
| Questions require unit evidence and allow defensible alternatives | **Met at planning depth.** Final source sets remain unjudged. |
| Chronology is maintained or departures explained | **Missed in one material rationale:** finding 4. Other thematic returns are explained. |
| Contested events receive more than one telling | **Met as a planning requirement.** Actual selections await unit plans. |
| Writing from sources recurs and grows | **Partly met:** recurring claims lead to the capstone, but independent source acquisition needs finding 3. |

## What should be preserved

- The 160-day budget, unit order and protected response time.
- One Cold War development in depth across both case rows.
- Rwanda as anchor and Srebrenica as comparison.
- Unseen-source tasks, repeated argument writing and interpretation across media.
- Present-day communities, resistance and agency alongside hard history.
- Prohibitions on harmful simulations and personal disclosure.
- Printed source routes and explicit science bridges.

## Settled by the expert

These are recommendations for the caller to apply.

| Choice | Reason | Files affected |
|---|---|---|
| Retain current unit totals | No demonstrated need to lengthen the year | Frame and sequence |
| Use days 130 and 131 for separate power studies | Gives both standards adequate explicit work | Days CSV and sequence |
| Finish globalization synthesis on day 126 | Removes repetition without losing the claim | Same |
| Use identified composite assessment evidence | Secures coverage within existing assessment time | Sequence, then unit plans |
| Teach a bounded independent search on day 145 | Delivers the promised grade 10 advance | Days CSV and sequence |
| Add local presentation modelling and panel arrangements | Makes the history-only route concrete | Same |
| Preserve unit 10’s survey day | Avoids further compression of sensitive cases | Sequence |
| Retain retrieval for maintained prerequisites | Matches the current writing rule | Frame wording and sequence |
| Correct the Napoleon placement and record reorderings | Makes adaptation traceable | Source map |

## For Cory

- No new scope, money, people or audience decision is required for these repairs.

## Limits and sources

Classroom minutes, final source difficulty, individual asset rights, assessment quality and sensitivity-read outcomes remain unverified. Those require the actual materials. Workload judgments here are professional judgments, not measured classroom results.

Outside sources opened:

- [Massachusetts 2018 framework](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf): targeted requirements and example-list checks.
- [C3 Framework](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf): targeted performance checks.
- [Partial textbook publisher record](https://dc.etsu.edu/etsu-oer/13/): publication and licence; local PDF supplied passage and order checks.
- [Mussolini account](https://encyclopedia.ushmm.org/content/en/article/benito-mussolini-1): chronology for finding 4.
- [California HSS-10.2.5](https://www2.cde.ca.gov/cacs/id/web/4490): Vienna candidate confirmation.
- [College-level world history framework, effective fall 2026](https://apcentral.collegeboard.org/media/pdf/ap-world-history-modern-course-and-exam-description.pdf): edition and broad sequence inspected, not a complete crosswalk.

The [New York framework](https://www.nysed.gov/sites/default/files/programs/standards-instruction/framework-9-12-with-2017-updates.pdf) returned 502, and the [Tennessee standards PDF](https://www.tn.gov/content/dam/tn/stateboardofeducation/documents/standards/social-studies-2022-2023/TN%20Academic%20Standards%20for%20Social%20Studies%206.24.pdf) returned 403. Their candidate attributions remain repository claims awaiting the unit-level comparisons.

Memory informed the review method only. No substantive finding rests solely on memory.

**For the source list:** record the limited uses and access failures above; no new substantive source is proposed.

**Verdict:** revise before unit writing. **Finding count:** 8. **Report path:** `docs/reviews/sequence-world-history-ii-2026-11-14.md`, delivered here only.


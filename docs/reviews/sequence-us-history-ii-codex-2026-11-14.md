# Independent scope and sequence review: US History II

**Intended report path:** `docs/reviews/sequence-us-history-ii-2026-11-14.md`  
**Delivery:** Complete report below; no files changed.  
**Finding count:** 6.

## Verdict

Revise before unit planning: the course has a coherent historical arc, complete recorded standards placement, and useful recurring source work. Its greatest risk is treating assessment code lists as proof that the described tasks assess every required component. Complete the assessment blueprints, restore the missing geography demands, and reconcile the remaining source and pacing instructions within the existing unit allocations.

## What I read

- `docs/agents/EXPERT.md`, the social studies lens, FOUNDATION, relevant ROADMAP sections, BASELINE rules 20 to 24, GLOSSARY, APPROACH, and relevant APPROACH-SOURCES entries.
- The shared adoption criteria and social studies portion of `docs/ADOPTION-BAR-SUBJECTS.md`, plus `docs/courses/social-studies/STANDARD.md`.
- The complete US History II scope and sequence, days CSV, frame, and all 25 `us2-` progression rows.
- The loaded Massachusetts USII standards, including their lettered parts, and the official framework’s relevant requirements.
- CALENDAR, the grade 12 calendar records, and ELA 12’s research, presentation, coordination, and shortened-year instructions.
- The earlier US History II frame reviews and their fix report, relevant progression findings, and earlier sequence findings for repetition.
- BASE-TEXTS, relevant deferred-work entries, the stored economics book’s contents and relevant text search, and the introductory guides for the four selected Native-history units.

Outside sources were opened for standards, source identification, and instructional comparisons. No substantive finding rests solely on memory. Prior memory informed the review method only.

## Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Stopped during another course’s processing because `markdown` is unavailable. |
| `python -X utf8 scripts/frame.py calendar` | Completed successfully; no stagger-rule breaks reported. |
| `python -X utf8 scripts/plan.py check us-history-ii` | **0 failures.** |
| `python -X utf8 scripts/frame.py check us-history-ii` | One failure: stale `Pending(ss:us-history-ii)` statement at frame line 78; recognized 12 units and 160 days. |
| `python -X utf8 scripts/stale.py check` | One failure, the same frame statement. |

The incomplete global gate does not prevent a substantive verdict.

## Findings, most serious first

### 1. Assessment descriptions do not secure the coverage their code lists claim

**LAYER:** sequence  
**REPEAT:** yes, the same mismatch appears in earlier social studies progression and sequence reviews.  
**Severity:** substantial  
**Confidence:** firm

Every unit has an assessment slot and an unseen-source task. However, several tasks can be completed successfully without demonstrating substantial portions of the attached standards. Statements such as “Covers every part” do not resolve that mismatch.

| Unit, assessment day | What the description leaves unsecured | Exact fix |
|---|---|---|
| 1, day 11 | An event-to-jobs chain does not necessarily assess investment returns, market mechanisms, Federal Reserve organization, or the required historical examples. | Add a component-by-component blueprint. Include independent investment evidence from day 5, compact economics explanations, and the unseen application. |
| 2, day 24 | Two contrasting sources cannot themselves establish knowledge of all ten lettered parts. | Specify the coverage of the short knowledge section across those parts, beside the sourced argument. |
| 3, day 38 | Judging one program using one economic account omits the comparison of accounts, the primary-source report, and the geographic performance. | Include independently completed report and case-study evidence from days 31 and 34; explicitly assess comparison of the two accounts and the geography work. |
| 4, day 55 | Documents restricted to 1938 to 1944 cannot assess the postwar response or a chosen 1945 conference. Map work and the chosen source study are also unsecured. | Include the map and source-study evidence; extend the unseen set through 1946 and reserve questions on origins, entry, and responses before, during, and after the war. |
| 5, day 65 | One home-front source does not establish all six home-front components. A later account of the bomb does not necessarily assess the original reasons or the early nuclear debate. | Specify evidence for each home-front component and both nuclear-history demands, alongside the interpretation task. |
| 6, day 82 | A document and metropolitan map can omit Sputnik, economic-system comparison, flashpoint reasoning, domestic-policy research, and McCarthyism. | Incorporate identified independent work from days 70 to 74 and 79 to 80; retain the geographic application. |
| 7, day 101 | Protest and court excerpts do not necessarily assess the demographic trends, later race relations, legislation, or both Massachusetts components. | Add the relevant data and research evidence, with explicit coverage of the lettered parts. |
| 8, day 112 | One presidential document cannot establish the four-presidency Vietnam comparison or consequences for both Vietnamese and Americans. | Require a concise comparative timeline and consequences explanation, plus the unseen document judgment. |
| 9, day 122 | Transfer to an unfamiliar movement does not assess the movement each student studied in depth. | Score the chosen movement’s research against its option’s requirements; retain the unseen task as additional transfer evidence. |
| 10, day 133 | Explaining two political traditions and judging one policy does not require explaining the Cold War’s end. | Add an explicit causal judgment using internal and external evidence. |
| 11, day 144 | A policy-response judgment can omit technological and immigration trends. | Include the independent trend and immigration comparisons beside the government-response evaluation. |
| 12, day 159 | Scoring the final argument and an unseen explanation critique does not automatically assess the student’s argument critique. | Explicitly include the distinct critique records from days 151 and 152, plus evidence of the two forms and audiences. |

**Why it matters:** Writers could follow these assessment descriptions faithfully while leaving teachers without evidence for claimed learning.

**Course-wide fix:** Make each assessment composite where necessary: identified independent work plus the unseen task. Name every required component and where its evidence comes from. Keep the existing assessment and respond days; do not attempt to fit every research performance into one sitting.

This is a planning-contract finding, not a claim about unwritten assessment items. The distinction between knowledge and disciplinary performance is supported by the [Massachusetts framework](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf) and [C3 Framework](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf).

### 2. The geography repair loses required breadth between the frame and the days

**LAYER:** sequence  
**REPEAT:** yes, US History II’s earlier independent frame review, finding 2.  
**Severity:** substantial  
**Confidence:** firm

The frame and progression now require migration, settlement, **resource use**, and land use at **local, regional, and global scales**. Day 29 retains migration, settlement, and land use but omits resource use and the scales. Day 31 merely finishes the report.

Neither day explicitly establishes the long-term climate evidence required by `D2.Geo.9.9-12`. A dated drought record alone does not establish that dimension. See the [C3 geography indicator, printed page 42](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf#page=42).

**Why it matters:** The previous repair can disappear when the day writer works from the CSV.

**Exact fix:**

- Day 29: require a supplied long-term climate series, the Dust Bowl evidence, and linked local, regional, and world-scale comparisons addressing migration, settlement, resource use, and land use.
- Day 31: require an independently written geographic evaluation in the report, distinguishing climate evidence from farming and policy decisions.
- Include that component explicitly in unit 3’s assessment blueprint.

Keep the existing days. The urban, suburban, and rural breadth of `D2.Geo.8` is carried more successfully into days 76 and 77 and should remain.

### 3. Economics references point writers to the wrong material

**LAYER:** base text  
**REPEAT:** new for the chapter-reference error; the monetarist issue corrects an earlier expert settlement.  
**Severity:** substantial  
**Confidence:** firm

Three references need correction:

- Day 6 cites chapter 27 for measuring output. That chapter concerns money and banking.
- Day 10 cites chapter 27 for fiscal and monetary policy.
- Day 27 and the frame treat chapters 25 and 26 as the source for the Keynesian and monetarist comparison. Chapter 26 concerns the neoclassical perspective. A text search of the stored edition found no occurrence of “monetaris”.

The book’s [contents and preface](https://openstax.org/books/principles-economics-2e/pages/preface) confirm the chapter identities. Its [GDP section](https://openstax.org/books/principles-economics-2e/pages/19-1-measuring-the-size-of-the-economy-gross-domestic-product) supplies the output material. The [Federal Reserve’s Depression history](https://www.federalreservehistory.org/essays/great-depression) provides a suitable reference for monetary contraction and banking-policy failures.

**Why it matters:** A writer following the references could omit the intended content or substitute neoclassical analysis for the specified monetarist explanation.

**Exact fix:**

- Day 6: cite selected material from sections 19.1, 21.1, and 22.1 for output, unemployment, and inflation.
- Days 7 and 8: use selected chapters 27 and 28 material for banking and monetary tools.
- Day 10: cite selected chapter 28 material and section 30.4.
- Day 27: use chapter 25 for the Keynesian explanation and a separately sourced monetary explanation. Keep chapter 26 only if explicitly identified as additional neoclassical context.

Correct the corresponding frame references. Adapt only the authorized stored edition. I disagree with the earlier expert’s assertion that chapters 25 and 26 supply both named accounts.

### 4. Several survey days carry more work than their stated purpose allows

**LAYER:** sequence  
**REPEAT:** yes, load compression was raised in the earlier US History II frame read.  
**Severity:** moderate  
**Confidence:** likely on the risk; judgment call on the redistribution

The problem is concentrated within days:

- Day 9 combines five historical examples with four government roles.
- Day 32 combines eleven options, six named people, deposit insurance, and the court plan.
- Days 114 and 115 survey six movement families plus two additions. The first also holds readiness; the second holds reteaching.

The sequence’s introductory claim that its listed topics are taught “in full” obscures the distinction between orientation and the selected case studied deeply.

**Why it matters:** Writers may produce rapid name lists or squeeze out source analysis.

**Exact fix:**

- Introduce the government-role categories within day 2’s policy comparison. Keep day 9 focused on historical economic effects.
- Make day 32 an explicit orientation menu. Put substantive source analysis of relevant people inside the selected case on days 33 and 34. Retain the court-plan reference as brief context.
- Give unit 9 three survey days: women’s and LGBTQ movements on day 114; disability and environmental movements on day 115; workers’ and Native movements, with the Chicano and Asian American connections, on day 116.
- Move the three in-depth days to 117 to 119. Combine presentation and comparison on day 120; retain the argument on day 121.

Preserve every requirement of the chosen option. Do not turn optional case menus into a requirement for full-depth study of every option. That choice structure is supported by the [Massachusetts framework’s USII case-study provisions](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf#page=132).

The [National Archives New Deal lesson](https://www.archives.gov/legislative/resources/education/new-deal) provides a useful comparison: substantive document activities each receive approximately 45 minutes. That is a warning against compression, not a mandatory timing rule.

### 5. The paired capstone route still gives conflicting instructions

**LAYER:** sequence  
**REPEAT:** yes, the shared-calendar issue appeared in both earlier US History II frame reads.  
**Severity:** moderate  
**Confidence:** firm

The main milestones now align: question around day 123, source list day 135, draft day 145, rehearsal by day 147, talks during days 150 to 156, and final paper day 158.

Two conflicts remain:

1. History day 150 still directs drafting, although the paired project already has a full draft.
2. ELA’s shortened-year instructions allow cutting the second talk, while history preserves two forms for contrasting audiences. Both frames claim a shared cut order.

**Why it matters:** Teachers can duplicate work or remove evidence history still requires.

**Exact fix:**

- Give day 150 explicit variants: standalone students draft; paired students use the existing draft for historical evidence, corroboration, and counterclaim review.
- Give days 154 to 156 variants that distinguish first instruction from adaptation and presentation of an already rehearsed talk.
- Write one paired shortened-year schedule. Preserve history’s two forms and contrasting audiences, its distinct critique tasks, assessment, response, and chosen action. ELA-specific reductions must not remove those components.

Retain the separate standalone requirements. The mismatch is in the operating instructions, not the existence of the pairing.

### 6. Current frame statements still misdescribe status and the semester boundary

**LAYER:** frame  
**REPEAT:** yes, stale operational statements recur in the earlier frame and progression reads.  
**Severity:** minor  
**Confidence:** firm

Two statements remain misleading:

- Frame line 78 says `Pending(ss:us-history-ii)` although the sequence has landed and named the missing topics. The stale gate identifies this.
- The frame and day 85 call that day the close of the fall half. CALENDAR defines the fall half as days 1 to 80. Unit 6 actually crosses that boundary.

**Why it matters:** Writers receive obsolete instructions, and schools receive an inaccurate semester description.

**Exact fix:**

- Replace the pending statement with: “The scope and sequence names the three missing topics; topic and worksheet implementation remains tracked under L8.”
- Keep the day 84 check and day 85 response, but call them a **week 17 mid-year checkpoint after unit 6**.
- Correct the timetable: fall ends during unit 6; spring begins with its remaining days and the checkpoint.
- Remove the “semester line” and “closes the fall half” labels.

This corrects wording without moving units or assessments.

## Order, coverage, and days by load

All 25 progression rows are placed. Teaching rows contain 43 numbered Massachusetts standards, 50 lettered parts, and six owned C3 indicators.

| Lettered group | Recorded teaching days |
|---|---|
| T1.3a to c; T1.9a to b | 3 to 4; 9 |
| T2.1a to j | 13 to 21 |
| T2.4a to k | 32, with selected depth on 33 to 34 |
| T3.5a to f | 47 to 48, with selected depth on 49 |
| T3.8a to f | 57 to 60 |
| T4.5a to d | 89 to 92 |
| T4.7a to b | 97 to 98 |
| T4.8a to f | 114 to 115, with selected depth on 116 to 118 |

Placement is complete. Findings 1 to 4 distinguish placement from sufficient teaching and assessment.

| Unit | Total days | Teaching days | Load judgment |
|---|---:|---:|---|
| 1 | 12 | 10 | Dense toolkit; redistribute day 9’s load. |
| 2 | 13 | 11 | Reasonable, including two argument days. |
| 3 | 14 | 12 | Reasonable overall; survey and geography need clearer contracts. |
| 4 | 15 | 13 | Reasonable for war context, source study, and Allied response. |
| 5 | 10 | 8 | Tight but defensible with supplied, selected sources. |
| 6 | 17 | 15 | Defensible across foreign policy, domestic change, research, and geography. |
| 7 | 17 | 15 | Defensible across movement history, law, data, and regional comparisons. |
| 8 | 11 | 9 | Reasonable if the presidential comparison remains central. |
| 9 | 10 | 8 | Survey time is compressed; finding 4 redistributes it. |
| 10 | 11 | 9 | Reasonable, with capstone time explicitly reserved. |
| 11 | 11 | 9 | Tight: three full addition days leave six other teaching days. |
| 12 | 13 | 11 | Plausible with advance question and source work; paired variants need correction. |

No whole unit is demonstrably far overallocated. Counts of standards alone are not a suitable pacing measure.

The major dependencies work: economics precedes its historical applications; containment precedes Vietnam; civil rights legislation precedes the Great Society discussion; movement surveys precede selection; and capstone preparation precedes the final unit. Thematic returns explain much of the chronological overlap. Unit 4 should signpost its return from US entry to the earlier roads to war.

No unit exceeds 25 days, so no additional mid-unit assessment is required. Twelve unit respond days and three course-level respond days are counted once.

## Calendar and same-year leans

Course-level checks match the grade 12 calendar at days 40, 84, and 146, in weeks 8, 17, and 30. CALENDAR sets no additional high-school stagger rule; unit 12’s assessment and response occupy finals week 32.

Readiness checks correctly address the three grade 8 returns on days 1, 86, and 114, with subsequent reteaching. The sequence-writing rule distinguishes these long returns from recent-grade retrieval.

Mathematics leans are from earlier grades and carry reminders. ELA 12’s calendar places its research unit on days 125 to 160, allowing the shared question and later milestones. Findings 5 and 6 concern the remaining implementation and labeling conflicts.

## Candidate cells and source map

Every candidate is settled with an identifiable cost:

| Unit | Settlement |
|---|---|
| 1 | None. |
| 2 | Voting and citizenship additions embedded; consumer economy and presidential politics on day 17. |
| 3 | Indian Reorganization Act on day 35; court plan embedded on day 32. |
| 4 | Soldiers and special units on day 50. |
| 5 | Bracero program and Zoot Suit riots embedded on day 60. |
| 6 | Termination and relocation on day 78. |
| 7 | Mendez on day 88; Warren Court reference embedded on day 95. |
| 8 | Draft, voting-age amendment, and Kent State embedded on day 107. |
| 9 | Chicano and Asian American movements embedded in the survey. |
| 10 | The 1970s on day 126. |
| 11 | Recent survey, financial crisis, and Native self-government on days 137 to 139; Gulf War embedded on day 140. |
| 12 | None. |

Nine teaching days have no home code, approximately 6.9 percent of the 130 teaching days. Embedded additions still need realistic task budgets.

A complete base-lesson source map is **not applicable** because this is an original course with partial bases. The Native-history units retain their source order, 3 through 6. Unit plans must identify selected pieces rather than imply that entire multi-period guides fit one day.

The stored [termination guide](https://ospi.k12.wa.us/sites/default/files/2023-10/us-hs-unit4-level1.pdf) includes role play. Preserve the historical evidence and tribal framing while replacing that activity with document analysis, consistent with the lens. This is an adaptation instruction, not a finding that the present sequence requires role play.

## Lens checklist for the scope and sequence layer

| Lens line | Result |
|---|---|
| A compelling question requires the unit’s sources and permits defensible answers | **Met in design.** Tasks require evidence; final source selections remain unverified. |
| Chronological departures have reasons | **Met with signposting needed.** Thematic returns are explained; make unit 4’s rewind explicit. |
| Contested events carry more than one telling | **Met as a planning commitment.** Actual source balance awaits section plans. |
| Writing from sources recurs and develops | **Met.** Argument begins early, counterclaims recur, and the capstone adds research and audience demands. |

## What should be preserved

- The recurring economic toolkit and running Cold War map.
- Frequent sourced arguments and unseen-source assessment tasks.
- The civil rights sequence linking organizing, law, demographic evidence, and regional cases.
- Plain hard-history language, privacy protections, and present-day Native sovereignty.
- The paper route and student choice in informed action.
- The current sensitivity-agent arrangement. Do not restore superseded outside-reader requirements.

## Settled by the expert

| Choice | Reason | Files affected when applied |
|---|---|---|
| Make assessments explicit composites where needed | Research and performance evidence cannot all be recreated in one sitting | Scope and sequence; days CSV; later assessment plans |
| Restore the complete geographic evaluation on days 29 and 31 | Carries the existing owned indicator into actual work | Scope and sequence; days CSV |
| Correct economics references and separately source monetarism | Prevents content substitution | Frame; days CSV |
| Redistribute crowded survey work within existing units | Protects selected-case depth | Scope and sequence; days CSV |
| Add paired and standalone capstone variants | Uses completed ELA work coherently | History planning files; ELA coordination statements |
| Retain the week 17 checkpoint and correct its label | Preserves unit order while describing the calendar accurately | Frame; days CSV; calendar label when regenerated |
| Replace the stale topic-status statement | Distinguishes named topics from completed implementation | Frame |

## What I could not judge

Actual assessment items, scoring reliability, final source difficulty, classroom timing, and complete sensitivity handling cannot be judged from this layer. Exact comparison-state references were not independently rechecked; their detailed comparison tables belong to unit planning.

The live Native-curriculum index returned 403, so stored guides were read. The [source-analysis lesson overview](https://www.inquirygroup.org/history-lessons/new-deal-sac) was accessible, but its downloadable materials required registration and were not read.

The [Inquiry History overview](https://inquiryhistory.com/about/) supplied a broad sequence comparison only. Its lesson counts were not treated as measured pacing evidence.

## For the source list

Add or update:

- The corrected economics section references and the Federal Reserve Depression-history reference.
- The National Archives New Deal lesson, including its stated activity durations.
- The direct Native-guide PDF routes, the index access failure, and the need to replace the termination role play.

## For Cory

None arising from these repairs. They retain the approved scope, audience, unit ownership, and day allocations and require no expenditure or outside contact.

**Verdict:** Revise before unit planning. **Findings:** 6. **Intended report path:** `docs/reviews/sequence-us-history-ii-2026-11-14.md`.


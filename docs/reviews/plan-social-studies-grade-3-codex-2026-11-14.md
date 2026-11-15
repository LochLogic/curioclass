# Independent second read: social-studies-grade-3

**Review date:** 2026-11-14  
**Delivery:** This report is supplied here only. No files were changed.

## What I read

I read all seven unit plans, `s01.md` through `s07.md`, including their assessment items, answer examples, daily evidence, error registers, response allocations and sources.

I checked them against:

- `AGENTS.md`, `docs/agents/EXPERT.md`, the social studies lens, `docs/GLOSSARY.md`, `docs/courses/UNIT-PLAN.md` and `docs/pipeline/briefs/plan-read.md`.
- The complete course frame, scope and sequence, and all 160 rows of `data/plans/social-studies-grade-3/days.csv`.
- All grade 3 social studies progression rows, relevant incoming and outgoing rows, and the recorded exclusions.
- The shared criteria and social studies section of `docs/ADOPTION-BAR-SUBJECTS.md`, the foundation, teaching approach, relevant source notes, production guidance and BASELINE rules.
- The loaded grade 3 Massachusetts standards and relevant indicators in the official C3 publication.

After forming the findings, I read the earlier Codex frame and sequence reports solely to identify repeated kinds of defects. I did **not** open the prohibited Claude unit-plan report or any file prohibited by the blind rule.

| Read-only check | Result |
|---|---|
| `python -B -X utf8 scripts/unitplan.py check social-studies-grade-3` | All seven plans passed. |
| `python -B -X utf8 scripts/frame.py check social-studies-grade-3` | Passed, 0 failures. |
| `python -B -X utf8 scripts/plan.py check social-studies-grade-3` | Passed, 0 failures. |
| Comparison of each plan’s day-list goals, kinds, codes and notes with `days.csv` | No differences found. |

Memory informed the review method only. Historical findings below rest on current files and linked sources. Pacing judgments are estimates from the specified tasks, not observations of children.

## Course verdict

The course has a coherent seven-unit arc, useful recurring models, and substantial care in its treatment of evidence, sovereignty and hard history. It needs revision before lesson writing because several assessments do not establish a credible workload within their minutes, unit 5 misses part of its claimed leadership comparison, and unit 7 does not explicitly score the required own-community research. Preserve the course structure and day totals while repairing the assessment blueprints and recurring inquiry work.

## Unit 1: Where we live

### 1. Serious: the assessment’s workload is not secured by its thirty-minute allocation

**Location:** `s01.md`, field 5, Administration and Q1 to Q14.  
**LAYER:** plan. **REPEAT:** yes, assessment feasibility raised in the earlier sequence read.  
**Confidence:** likely.

Moving Q9 to Q12 into the portfolio helps, but the remaining sitting still requires two constructed maps, two cities located through several reference systems, regional state locations, six physical-feature identifications, comparisons across representations, cultural and environmental explanations, and a two-source argument.

Calling the extended answers “about six short sentences” understates the drawing, locating, reading and reasoning. Pointing or oral answers can reduce writing, but the plan supplies no classroom collection procedure for hearing those responses within the same sitting.

**Why it matters:** the assessment could measure completion speed and access to adult recording more strongly than the intended geography and evidence skills.

**Exact fix:**

- In field 5, collect Q2 through a fresh independent task replacing E10, with eight minutes reserved.
- Collect Q4 through a fresh physical-map task replacing E14, with five minutes reserved.
- Collect Q5 through a fresh political-map task replacing E13, with five minutes reserved. On the shorter route, place that component in day 12.
- Keep those components within the end-of-unit assessment record and score them individually on day 23.
- Replace the Administration statement with an explicit list of the remaining day 23 tasks and their allocation. Preserve the unseen-source argument.
- Update the affected `days.csv` notes and regenerate the day list. Do not add days or repeat these components on day 23.

These allocations are a concrete revision to test against the completed packet, not a claim that pacing has been demonstrated.

### 2. Minor: the handoff note describes receiving plans as unwritten

**Location:** `s01.md`, field 3, Returns. The same defect occurs in `s02.md` and `s06.md`.  
**LAYER:** plan. **REPEAT:** yes, stale operational notes.  
**Confidence:** firm.

The receiving plans now exist. The statement obscures the distinction between an available unit-plan handoff and an unavailable lesson-level handoff.

**Exact fix:**

- In `s01.md`, delete “Later plans remain unwritten.”
- In `s02.md`, delete “Later plans are unwritten.”
- In `s06.md`, delete “Its plan is unwritten.”
- Retain the accurate qualification that last-day lesson files and Tomorrow lines have not been verified.

The actual plan-level handoffs are coherent: maps support government and trade, sourcing supports colonial inquiry, and the final project retrieves the year’s models.

## Unit 2: Who decides here

### 3. Serious: five task blocks conceal a much larger assessment

**Location:** `s02.md`, field 5, Administration and Q1 to Q15.  
**LAYER:** plan. **REPEAT:** yes, assessment feasibility.  
**Confidence:** likely.

The five blocks still contain numerous separate demands. Q7 alone requires ten benefit-and-difficulty statements across five settings. Q8 compares three procedures. Q11 requires views, experiences and values for two people plus the pupil’s own foundation. Q12 and Q13 add constitutional origins, rights and structures across several governments.

Sharing labels across codes is sensible, but it does not remove the distinct explanations. The stated six-minute cooperation-and-procedure block is particularly weak.

**Why it matters:** a writer could produce every listed item faithfully and still create an assessment that ordinary classrooms cannot administer as described.

**Exact fix:**

- Collect Q7 as a fresh independent six-minute component replacing the day 36 exit.
- Collect Q8 as a fresh independent six-minute component replacing the day 37 exit.
- Score Q11 from an individual day 39 record that identifies the pupil’s foundation and another participant’s stated foundation.
- Reserve twelve minutes of day 46 for fresh Q12 and Q13 constitutional cards.
- Keep Q9 and Q10’s actual-conduct observations. Written advice must continue to supplement them.
- Rewrite day 47’s administration around the remaining tasks, retaining separate scores for every part and the unseen two-source argument.
- Record the distributed components in field 5 and the affected CSV notes.

### 4. Moderate: supporting-question interpretation disappears after unit 1

**Location:** `s02.md` through `s07.md`, fields 2 and 5.  
**LAYER:** plan. **REPEAT:** yes, semantic inquiry coverage, now at additional locations.  
**Confidence:** firm.

The progression’s `ss3-inquiry-questions` row requires the supporting-question work in every unit. Unit 1 explicitly identifies facts needed, an interpretable idea and alternative readings. Later units co-write questions, but generally omit that task. Identifying two meanings in the compelling question does not replace interpreting an idea within a supporting question.

This concerns missing work, not an omitted code line. The distinction is supported by [C3 D1.3 and D1.4](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf).

**Why it matters:** the course teaches the inquiry routine once but does not reliably maintain it through the harder content.

**Exact fix:** add a supporting-question record during the existing co-writing block in each affected unit. It must contain the question, needed facts, one disciplinary idea with two defensible readings, and the connection to the compelling question.

| Unit | Existing day | Suitable idea |
|---|---:|---|
| 2 | 26 | Fair decision-making through direct participation or representation. |
| 3 | 50 | Meeting immediate needs or preparing for later needs. |
| 4 | 72 | Contributions understood through land care, language or governing. |
| 5 | 90 | Sharing land understood through different arrangements for authority and use. |
| 6 | 125 | Having a voice through voting, representation or petitioning. |
| 7 | 141 | Contributions understood through prominent projects or less visible continuing work. |

Model one distinction, record the class’s reasoning, and retain one short individual response. Do not turn established historical facts into matters of preference or add six further assessment-day essays.

## Unit 3: Making a living here

**Finding 4 applies.** I found no additional unit-specific substantive defect requiring a separate finding.

The economics is generally careful. The plan distinguishes revenue from profit, deposits from interest, money from physical capital, and modern Ghana from ancient Ghana. Its hypothetical cases are labelled as invented.

The named traders and facilities are traceable in the assembly’s [2023 market report](https://tecma.gov.gh/techiman-market-trading-post-for-west-africa/) and [2024 commissioning report](https://tecma.gov.gh/local-government-minister-commissions-ultra-modern-market-in-techiman/). Keep those dates and the distinction between reported experience and present conditions.

## Unit 4: The first peoples of our land

**Finding 4 applies.**

### 5. Minor: question marks have replaced quotation marks

**Location:** `s04.md`, field 5, the Q1 to Q9 scoring-example table, lines 93 to 101 in the reviewed copy.  
**LAYER:** plan. **REPEAT:** new.  
**Confidence:** firm.

Both answer-example columns have damaged quotation delimiters. For example:

- **Old:** `?Penobscot, Narragansett and Wampanoag.?`
- **New:** `"Penobscot, Narragansett and Wampanoag."`

There are eighteen affected answer cells, each with an opening and closing damaged delimiter.

**Why it matters:** the examples look uncertain and will carry damaged text into teacher materials.

**Exact fix:** replace the two delimiter question marks in each affected answer cell with ordinary quotation marks. Preserve genuine question marks inside questions, especially Q6. Do not run a global replacement of every question mark.

The checked factual anchors hold: the [Makah history](https://makah.com/makah-tribal-info/about-history/) supports the permanent-village and seasonal-camp distinction; the [Menominee treaty record](https://menominee-nsn.gov/CulturePages/Treaty1854) supports the date and location; and [Aquinnah’s history](https://wampanoagtribe-nsn.gov/wampanoag-history) supports the emergency-services agreement and place-name account. The [2026 university account of Carol Dana](https://umaine.edu/news/2026/04/university-of-maine-to-award-honorary-degree-to-carol-a-dana/) supports the stated language-teaching work.

## Unit 5: First meetings and early colonies

### 6. Serious: the final assessment is oversized

**Location:** `s05.md`, field 5, day 120 assessment and Administration.  
**LAYER:** plan. **REPEAT:** yes, assessment feasibility.  
**Confidence:** likely.

After excluding the two saved inquiry responses, day 120 still contains twenty separately listed assessment rows. Several contain multiple explanations. The sitting includes chronology, locations, a voyage, two account comparisons, map comparison, Plymouth’s founding and government, hardships, relationships, leaders, expansion, daily life, schooling, slavery, several aspects of trade, and an argument.

Thirty minutes provides an average of ninety seconds per listed row before accounting for their unequal demands. Grouping them onto one sheet does not solve that workload. Oral alternatives also need a collection method.

**Why it matters:** the assessment can appear complete on paper while producing incomplete or unreliable evidence in practice.

**Exact fix:** retain the complete end-of-unit assessment, but collect defined independent components during existing days:

| Component | Placement |
|---|---|
| Q1 to Q4d, the first-half transfer tasks | Day 119, replacing part of review. |
| Revised Q5a leadership comparison | Day 107, replacing its exit. |
| Q8a to Q8e, the integrated maritime task | Day 116, replacing its exit. |
| Q5b, Q6a and Q6b, Q7, and Q9a and Q9b | Day 120. |
| Q10 and Q11 | Existing saved inquiry records. |

Field 5 must state the minutes, individual evidence and scoring date for each component. Use separately reserved passages and maps so each component is unseen when first administered. Update the CSV notes and preserve the day 121 response allocation.

Check the resulting packet against its actual reading and response load before treating this allocation as feasible.

### 7. Serious: the leadership assessment omits the Puritan side of the claimed comparison

**Location:** `s05.md`, field 5, Q5a under `MA.3.T5.1`.  
**LAYER:** plan. **REPEAT:** yes, incomplete coverage of a bundled standard.  
**Confidence:** firm.

Q5a compares Bradford and Ousamequin. It does not assess the Puritan leadership that the plan’s standard statement includes. Teaching mentions Winthrop on day 107, but there is no corresponding assessed comparison.

The [Massachusetts framework, grade 3 Topic 5](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf) includes both Massachusetts Bay Puritan and Plymouth Pilgrim leadership alongside Native leadership.

**Why it matters:** the assessment claims the whole standard while eliciting only part of it.

**Exact fix:**

- **Old:** “Compare Bradford’s and Ousamequin’s roles and decisions using A and B.”
- **New:** “Using the supplied records, compare one governing role and one decision of Bradford, Winthrop and Ousamequin. Explain one difference in whose interests or authority each represented.”

Add a short, sourced Winthrop record and scoring anchors for all three. Do not imply that Winthrop and Metacom negotiated with one another. Collect this component within the revised day 107 allocation in finding 6.

### 8. Moderate: the English account of the 1622 conflict is unnamed

**Location:** `s05.md`, day 99 evidence and field 10.  
**LAYER:** plan. **REPEAT:** new.  
**Confidence:** firm.

The plan promises comparison with “the English account,” but names no author, title, date or passage. The Pamunkey history is linked. The counterpart is left for later verification.

**Why it matters:** the writer cannot yet construct the promised comparison, distinguish testimony from promotion, or verify its answer.

**Exact fix:** name Edward Waterhouse’s 1622 colonial report, *A Declaration of the State of the Colony and Affaires in Virginia*, using the [Virginia Commonwealth University record and facsimile](https://scholarscompass.vcu.edu/britva/3/) as the reference route.

Specify the selected passage before lesson writing. Pair it with the Pamunkey account, explain the report’s colonial purpose and limits, and write an original factual summary suitable for grade 3. Keep hostile language and graphic material out of student copy. The source is a particular colonial report, not the voice of every English person.

This is an incomplete source specification, not evidence that a source was fabricated.

### 9. Moderate: the French and Dutch addition has an unsupported grade attribution

**Location:** `s05.md`, field 10 and inherited “Check set adds” wording; corresponding frame and CSV notes.  
**LAYER:** plan and process. **REPEAT:** new.  
**Confidence:** firm that the recorded attribution is unsupported.

The plan attributes New France and New Netherland map labels to Tennessee’s 2024 grade 3 standards while also stating that the direct comparison was not completed.

The available [official 2024 crosswalk](https://www.tn.gov/content/dam/tn/stateboardofeducation/documents/standards/social-studies-2022-2023/TN%20Social%20Studies%20Standards%20Crosswalk%206.24.pdf) places explicit French and Dutch colonial-map comparison in later grades, including 7.62 and 8.01. It does not substantiate the stated grade 3 attribution.

**Why it matters:** the addition is defensible context, but its recorded provenance is unreliable.

**Exact fix:** retain the settled labels on day 94. Replace the grade 3 attribution with:

> French and Dutch colony labels are retained as a settled Curio Class context addition. Tennessee’s 2024 later-grade colonial comparisons are a reference; no Tennessee grade 3 requirement is claimed.

Correct the frame, sequence and CSV note before regenerating mechanical text.

**Finding 4 also applies.**

## Unit 6: Founding ideas

### 10. Moderate: day 132’s evidence does not measure its stated content

**Location:** `s06.md`, day 132 goal, daily evidence and field 5.  
**LAYER:** plan. **REPEAT:** yes, goal-to-item coverage.  
**Confidence:** firm.

Day 132 promises the origins and meanings of symbols, a song and a holiday through five cards. Its exit asks only about the Statue of Liberty’s broken chain and the difference between an ideal and actual equality. The end-of-unit assessment uses the petition for civic virtues and principles, so it does not supply the missing evidence.

**Why it matters:** the course cannot tell whether pupils understood why the other objects and observances were created or how their meanings developed.

**Exact fix:** replace E132 with a compact five-row response using fresh source captions. For each named card, pupils identify its documented original purpose and one meaning it represents. Include one distinction between original purpose and a later meaning.

Allocate day 132 explicitly: retrieval five minutes, teaching twenty, supported discussion eight, independent evidence seven. Preserve pointing, dictation and the freedom to decline patriotic performance.

**Finding 4 applies.** The stale receiving-plan sentence is covered by finding 2.

The historical distinction among freedom, citizenship, voting and equal rights is sound. Keep the New Jersey exception, supported by the [state historical account](https://www.nj.gov/state/historical/assets/pdf/it-happened-here/ihhnj-er-petticoat-politicians.pdf), and the guidance grounded in [Barnette](https://tile.loc.gov/storage-services/service/ll/usrep/usrep319/usrep319624/usrep319624.pdf).

## Unit 7: How our community changed

### 11. Serious: Boston transfer tasks do not explicitly assess the own-community research

**Location:** `s07.md`, field 5, Q1, Q2 and the withheld-packet statement.  
**LAYER:** plan. **REPEAT:** yes, preserving the own-place demand while generalizing the anchor.  
**Confidence:** firm.

Q1 assesses Boston’s people and population. Q2 assesses Massachusetts’s historical extent and Boston’s growth. The plan says this packet tests transfer regardless of the class’s location.

Transfer is useful, but these tasks do not establish that a child researched their own community or interpreted their own state’s historical extent. P1 assesses a biography, P2 external communication, and P3 and P4 action. None explicitly carries the complete local-history and own-state requirements.

**Why it matters:** a pupil could receive complete marks for the two anchor codes without demonstrating the central own-place work.

**Exact fix:** add two individually scored portfolio components to field 5:

- **P0a, `MA.3.T1.2`:** the pupil’s own-community research from days 142 and 145 to 147. Require attributed evidence about earlier and continuing peoples, workers and newcomers, a dated population comparison, an interview contribution, and a supported change and continuity. Record unresolved gaps rather than inventing local history.
- **P0b, `MA.3.T6.1`:** the pupil’s annotated own-state historical map and growth explanation from days 143 to 144. Require the date, territorial extent, a comparison with today, and a sourced explanation connecting place and economic activity.

Give each component look-fors and two answer examples tied to its factual overlay. Score these alongside the Boston transfer tasks on day 159, without repeating them during its thirty minutes.

Replace:

> The new Boston packet tests transfer regardless of the class’s location.

With:

> The Boston packet tests transfer. P0a and P0b separately assess each pupil’s own-community research and own-state historical-map explanation.

**Finding 4 also applies.**

The dated population figures match the [2026 city publication](https://www.boston.gov/sites/default/files/file/2026/04/7%20-Volume%201%20-%20Boston%E2%80%99s%20People%20and%20Economy.pdf). Keep their reference years. The [Bisceglia interview](https://maryellenwelchgreenway.org/oral-history/eva-bisceglia/) is traceable, but its machine transcript still requires the audio verification already listed in the plan.

## What should remain

Preserve the seven units and their totals, the recurring two-source reasoning, source classification by relationship to the question, and the distinction between observation and inference. Keep Native nations present as distinct living governments, the plain treatment of coercion and slavery, the privacy protections, and the student-selected informed action.

No named historical source was established as invented. Original models and fictional cases are generally labelled honestly.

I could not certify unselected local packets, uninspected image crops, final passage difficulty, reproduction rights or classroom pacing. Several endpoints were blocked, including the original 1777 petition and some image records. Those limits do not prevent the verdict above.

## For the fixer

Apply the edits in this order:

1. Repair unit 5’s missing Puritan leadership comparison and specify its 1622 English source.
2. Add unit 7’s P0a and P0b local assessment components.
3. Redistribute the assessments in units 1, 2 and 5. Preserve every assessed part, individual scoring, fresh material and existing response days.
4. Add the supporting-question record to units 2 through 7.
5. Replace unit 6’s day 132 evidence with the five-card origin-and-meaning task.
6. Correct the French and Dutch addition’s provenance.
7. Repair unit 4’s eighteen damaged quotation cells.
8. Remove the three stale “unwritten” handoff statements.
9. Update factual CSV notes first, regenerate mechanical tables, then rerun the course checks.

These are item-level choices within the existing course. No change to audience, money, outside people, unit ownership or year totals is proposed. **For Cory: none.**

## For the structure pass

### P1. Moderate process finding: the Tennessee comparison remains incomplete across all seven units

**LAYER:** process. **REPEAT:** new. **Confidence:** firm.

Each comparison table substitutes the local decision summary or an access failure for an actual Tennessee comparison. The access limitation is reported honestly, but the subject bar’s comparison requirement remains unfinished.

Use the [official 2024 crosswalk](https://www.tn.gov/content/dam/tn/stateboardofeducation/documents/standards/social-studies-2022-2023/TN%20Social%20Studies%20Standards%20Crosswalk%206.24.pdf) as an available starting point. Record exact relevant codes, what was compared, and whether the course already covers the demand, retains a context addition, or needs a scope decision. Preserve Curio Class’s selected course order rather than importing another state’s whole year.

The official [Tennessee implementation page](https://www.tn.gov/sbe/committees-and-initiatives/standards-review/social-studies.html) distinguishes the 2024 adoption from its 2027 to 2028 implementation. Retain that distinction.

Additional structural repairs should support the findings:

- Add a part-to-evidence blueprint containing the item, collection day, scoring day, source, response mode and minutes. A code appearing in a row is insufficient.
- Distinguish assessment components collected earlier from tasks administered on the assessment day.
- Add a review check for damaged punctuation, including paired question-mark delimiters, while preserving genuine questions.
- Require source comparisons to identify a document edition and exact code or page.
- Check both shorter routes against the revised assessment placements. A removed review day cannot silently remove retained assessment evidence or add work to an already full assessment opening.
- Align the template, skeleton and checker descriptions about where daily evidence belongs. The current plans place it in field 5, while the merged-document template describes U3.
- Keep the structural gate explicitly limited to structural completeness. These plans demonstrate that a passing gate does not establish semantic coverage or feasible assessment size.

**Finding count:** 12, including the course-wide process finding.


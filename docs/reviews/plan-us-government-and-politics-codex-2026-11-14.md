# Independent second read: US Government and Politics

**Review date:** November 14, 2026.  
**Verdict:** Revise before lesson writing.  
**Findings:** Nine: one serious, seven moderate and one minor.

## What I read

I read `s01.md` through `s09.md` in `docs/courses/us-government-and-politics/`, the course frame and scope and sequence, all 80 day records, the government progression rows and their prerequisite rows, and the relevant Massachusetts and C3 standards.

I also read the required guidance, the social studies lens, the subject adoption bar and supporting foundation, approach and standards guidance. I did not open the prohibited files or the other reader’s report. No files were changed.

Checks:

- `python -X utf8 scripts/unitplan.py check us-government-and-politics`: all nine plans passed.
- `python -X utf8 scripts/frame.py check us-government-and-politics`: zero failures.
- `python -X utf8 scripts/plan.py check us-government-and-politics`: zero failures, reported at the sequence stage.

The text scan found no question marks replacing apostrophes, quotation marks or accented letters.

## Course verdict

The course has a coherent progression from authority and constitutional design to rights, political influence, policy research and local action. Its strongest features are individual evidence within group work, explicit limits on inference, clearly labeled fictional assessment sources and a substantial handoff from unit 8 into unit 9. The main corrections concern the own-state method, two misleading assessment statements and several allocations that leave reading, writing or exit evidence insufficiently budgeted.

Preserve the composite assessments, distinctions between historical holdings and current eligibility, protections against compelled advocacy, and honest statements about partial digital coverage.

All findings below are **LAYER: plan**. **REPEAT: unassessed**, because this independent read did not consult earlier review findings. Pacing concerns are desk judgments from the specified tasks and allocations, not observed classroom results.

## Unit 1: Why government, and what kind?

### 1. Minor: One assigned scholarly source is not identifiable enough

**Location:** `s01.md`, field 10, “Sensitivity study.”  
**Confidence:** Firm.

“Derrick Spires’s scholarship on Black citizenship” identifies a scholar and subject, but no particular work. A later reader cannot reproduce the assigned study or distinguish an identified publication from a source still to choose.

**Exact fix:** Replace that phrase with:

> Derrick R. Spires, *The Practice of Citizenship: Black Politics and Print Culture in the Early United States* (2019), identified through the university publication record. Not read here; select and record an accessible article, talk or passage before the sensitivity read.

The [university record](https://www.einaudi.cornell.edu/discover/people/derrick-spires) establishes the publication’s identity. It does not establish that its contents have been read.

No substantive factual correction emerged. The turnout figures match the [Census release](https://www.census.gov/newsroom/press-releases/2025/2024-presidential-election-voting-registration-tables.html). The membership figures are also traceable in the [December 2024 civic-life report](https://americorps.gov/sites/default/files/document/2025-01/CEV2023_HeadlineReport_12192024_508.pdf), which provides a useful replacement address for the blocked report link.

## Unit 2: Founding ideals and the gap

### 2. Moderate: Day 12 leaves the Letter’s reading outside its allocation

**Location:** `s02.md`, field 5, “Day 12 seminar.”  
**Confidence:** Likely.

The specified blocks already consume 50 minutes: ten for reteaching, ten for Douglass and related comparison, twenty for the seminar and ten for the exit ticket. Between those directions, students must also read King’s argument and establish its Birmingham context. That essential preparation has no explicit slot.

Without it, a writer must either compress the seminar or treat a difficult argument as already understood.

**Exact fix:** Replace the allocation with:

> Ten minutes for prerequisite support, five for the Douglass comparison, ten for Birmingham context and a supported reading of the bounded Letter selection, twenty for the seminar and five for the exit ticket.

Select the Letter passage to fit that supported reading. Preserve the distinction between interpreting King’s reasoning and debating whether segregation was acceptable. The [King Institute’s account](https://kinginstitute.stanford.edu/letter-birmingham-jail) supplies the historical setting.

The national and state documents, two deliberation settings and presentation evidence otherwise form a sound sequence.

## Unit 3: Federalism and sovereignty

### 3. Serious: Concrete tasks do not secure the promised own-state learning

**Location:** `s03.md`, fields 4 and 5, especially assessment items 2 to 5 and the day 19 exit ticket.  
**Confidence:** Firm.

The frame requires the student’s state to be the case, with Massachusetts serving as a worked example. The actual assessment requires Massachusetts court powers, Massachusetts municipal forms and Massachusetts state-local relationships. The day 19 exit adds Colorado, but does not require the student’s state.

A writer following those concrete tasks could produce a Massachusetts-and-Colorado unit for a student elsewhere, despite the general own-state instructions.

**Exact fix:**

- In assessment items 2 and 3, require an official provision from the student’s constitution identifying an institution’s express power, a defensible implementing means and a limit. Retain Massachusetts as the worked comparison.
- In item 5, replace the Massachusetts-only drainage case with a verified home-state case tracing legal authority, funding and service delivery.
- Keep item 4’s Massachusetts town-meeting comparison, then require one distinction from the student’s actual local governmental form.
- Rewrite the day 19 exit so the principal case uses the student’s state. Use Massachusetts or Colorado as the comparison.
- Require the home-state packet to contain the governing text and service or funding record, alongside its standards link.

These changes implement the existing frame. They do not add a standard or a day.

### 4. Moderate: Abolishing a water board does not establish a unitary system

**Location:** `s03.md`, field 5, assessment item 1.  
**Confidence:** Likely.

“West permits parliament to abolish regional water boards” supports the keyed answer “unitary” only if those boards represent regional governing authority. They could instead be administrative bodies inside a federal system.

The item therefore risks rewarding an inference that its evidence does not establish.

**Exact fix:**

**Old:**

> West permits parliament to abolish regional water boards.

**New:**

> West’s constitution gives the central parliament ultimate governing authority. Parliament may create, change or abolish regional governments, which have no constitutionally protected sphere of lawmaking.

Keep “unitary” as the answer and require the explanation to identify that distribution of authority.

### 5. Moderate: The mechanical tribal-government statement contradicts the accurate prose

**Location:** `s03.md`, day 20 list; corresponding frame and progression wording.  
**Confidence:** Firm.

The day goal describes more than 570 nations “with their own constitutions and courts.” The instructional prose correctly explains that a separate court or written constitution is not a condition of sovereignty.

The broad statement can become the lesson’s headline and undo that distinction. The [Bureau of Indian Affairs’ explanation](https://www.bia.gov/faqs/how-are-tribal-governments-organized) describes varied governing arrangements and court development.

**Exact replacement:**

> More than 570 federally recognized tribal nations exercise inherent powers of self-government. Their governing documents, institutions and justice systems vary.

Apply this upstream in `days.csv`, the frame’s unit 3 description and the `ss8-federal-state-powers` progression note, then regenerate affected mechanical text.

## Unit 4: The branches and their balance

### 6. Moderate: Day 34’s short-response allocation remains too crowded

**Location:** `s04.md`, fields 5 and 7.  
**Confidence:** Likely.

The composite arrangement appropriately removes several products from the sitting. Nevertheless, seventeen minutes still appear to hold the presidential scenario, court-system explanation, constitutional change, institutional relationships, four historical challenges and the Congress supplement.

These contain numerous separate explanations and evaluations. Calling them short responses does not give the writer a sufficiently bounded assessment.

**Exact fix:** Make the evidence allocation explicit:

- Score item 6 entirely from day 29’s individual record.
- Score the four historical challenges from independently completed, reserved source responses on days 30 and 31.
- Score Congress’s representation distinctions from day 23’s independent evidence and its lawmaking distinctions from day 24’s evidence.
- Incorporate item 7’s institutional map into item 1.
- Leave day 34 with item 1’s unseen argument and items 2 and 4’s bounded responses.

Retain the existing 8-minute reading, 17-minute response, 20-minute argument and 5-minute marking allocation. Update the assessment table so no removed component is silently asked again.

### 7. Moderate: Day 26 has no allocated exit-ticket time

**Location:** `s04.md`, field 5, “Product directions,” day 26.  
**Confidence:** Firm.

Eight minutes surveying agencies, seven modeling, twenty-five researching and ten writing consume all 50 minutes. The plan separately requires a fresh exit response after the research note.

**Exact fix:** Change day 26 to:

> Survey eight minutes; model seven; research twenty; write the individual research note ten; complete and collect the exit ticket five.

Keep the exit’s distinction between evidence of origins, evidence of current activity and evidence of impact.

### 8. Moderate: The answer assigns Senate consent to nomination

**Location:** `s04.md`, field 5, MA.GOV.T2.7 assessment row, item 2.  
**Confidence:** Firm.

The answer says “nomination requires Senate consent.” The President nominates; Senate advice and consent concerns appointment. Other parts of the plan make the distinction more accurately, but the answer column could generate an incorrect answer key.

**Exact fix:**

**Old:**

> Nomination requires Senate consent.

**New:**

> The President nominates. Under the ordinary appointment process, Senate confirmation precedes presidential appointment; nomination alone does not authorize the judge to begin serving.

This follows the [Appointments Clause](https://www.archives.gov/founding-docs/constitution-transcript) and the [Senate’s explanation](https://www.senate.gov/about/powers-procedures/nominations.htm).

## Unit 5: Rights and a free press

No additional finding.

The researched pair supplies the sustained historical comparison, while Mapp and Lovell provide unseen transfer. The plan correctly distinguishes constitutional text, changed precedent and implementation. Its assessment has fewer new components than the table initially suggests because the presentation is scored separately.

Preserve the historical framing and bounded claims in the [Gideon](https://www.govinfo.gov/content/pkg/USREPORTS-372/pdf/USREPORTS-372-335.pdf), [Mapp](https://www.govinfo.gov/content/pkg/USREPORTS-367/pdf/USREPORTS-367-643.pdf) and [Lovell](https://www.govinfo.gov/content/pkg/USREPORTS-303/pdf/USREPORTS-303-444.pdf) tasks.

## Unit 6: Parties, interest groups and media

No definite additional defect established.

The assessment is dense, but its expressly permitted brief responses and previously collected research make it plausible within the stated sitting. Keep its response format bounded when the student sheet is written.

The invented election records, poll and experiment are clearly labeled fiction. The actual media-effects study is identifiable as [King, Schneer and White’s research](https://gking.harvard.edu/files/776.full_.pdf). The plan appropriately separates measured public discussion or checking from demonstrated voting effects.

The readiness items match unit 5’s outgoing items, and sourcing and corroboration hand on explicitly to unit 8.

## Unit 7: The United States in the world

No additional finding.

The 2022 Pakistan material is expressly treated as dated evidence for a historical recommendation, rather than current disaster figures. The plan distinguishes the [appeal](https://mofa.gov.pk/curtain-raiser-launch-of-revised-un-flash-appeal-revised-2022-pakistan-floods-response-plan-frp), [needs assessment](https://www.undp.org/pakistan/publications/pakistan-floods-2022-post-disaster-needs-assessment-pdna) and response plan, including their dates and shared authorship.

The assessment is demanding but permits labeled classifications and uses earlier research for its sustained argument. Preserve that format, the ordinary nongovernmental organization example and the distinction between Senate consent and presidential treaty ratification.

## Unit 8: Policy in the news

### 9. Moderate: Day 69 needs an earlier writing allocation

**Location:** `s08.md`, field 5, “Product conditions and pacing,” days 68 and 69.  
**Confidence:** Judgment call.

Day 69 gives thirty-five minutes to finish a roughly page-long report, write a roughly page-long editorial and produce two visuals. Day 68 explicitly allocates only five minutes to synthesis. That is a thin drafting foundation for four products, especially when the digital fallback gives each student only a short device turn.

The likely cost is unfinished writing or superficial visuals, rather than evidence of both genres and deliberate visual communication.

**Exact fix:**

- On day 68, use five minutes to frame questions, five to model searching, twenty to gather and organize, fifteen to draft the factual report and five for the exit.
- On day 69, use five minutes for the genre model, twenty for the editorial, ten for the two simple visuals, ten for checking and revision, and five for the exit.
- State that saved records from days 66 and 67 support the shortened search block.
- Require visual plans and captions before each shared-device turn. Continue recording actual digital contributions and partial coverage where appropriate.

The current-law cautions should remain. The [food-traceability page](https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-requirements-additional-traceability-records-certain-foods) distinguishes the proposed compliance extension from the congressional enforcement restriction. The [accessibility fact sheet](https://www.ada.gov/resources/2024-03-08-web-rule/) records the 2026 deadline extensions.

## Unit 9: Local action

No additional finding.

This unit receives a concrete dossier, source record, writing and visuals from unit 8. Its assessment correctly separates the unseen individual task from collaboration, authorship and action evidence collected during the project.

Preserve the distinction between delivery, acknowledgement and policy success. The warning about Boston’s closed collection phase is supported by the [city’s current page](https://www.boston.gov/departments/participatory-budgeting/idea-collection). The optional outside exchange and partial-coverage statements are explicit.

## Source verification and limits

I attempted all **136 distinct linked addresses** in the nine plans. Successful retrieval establishes traceability, not a complete reading of every document. I found no invented source presented as real; invented assessment records are clearly labeled.

Some addresses remained blocked, timed out or exceeded retrieval limits. These included the [Tennessee standards](https://www.tn.gov/content/dam/tn/stateboardofeducation/documents/standards/social-studies-2022-2023/TN%20Academic%20Standards%20for%20Social%20Studies%206.24.pdf), [Philippine account](https://ncca.gov.ph/about-ncca-3/subcommissions/subcommission-on-cultural-heritagesch/historical-research/the-philippine-american-war-1899-1902/), [UN Charter](https://www.un.org/en/about-us/un-charter/full-text) and [Kuwait museum page](https://nccal-prod.nccal.gov.kw/en/museums), plus several faith, disability and state pages. I read the stored New York government standards after live retrieval failed. These access limits do not establish fabrication.

No factual finding rests solely on memory. Predicted student errors remain hypotheses marked “from memory” in the plans. Final classroom feasibility, full rights clearance and source packets still to be selected were not established by this read.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Use the revised day 12 allocation. | It explicitly includes the Letter’s supported reading. | `s02.md` |
| Replace the water-board cue. | The new wording supports a unique system classification. | `s03.md` |
| Reserve five minutes for day 26’s exit. | The existing blocks already total 50 minutes. | `s04.md` |
| Begin the factual report on day 68. | It distributes writing across the existing days. | `s08.md` |

## For the fixer

Apply these edits in order:

1. Correct the tribal-government statement in its upstream data and frame homes, then regenerate affected text.
2. Rewrite unit 3’s home-state tasks and assessment evidence as specified in finding 3.
3. Replace unit 3’s water-board cue.
4. Correct unit 4’s nomination answer.
5. Make unit 4’s assessment evidence allocation explicit, then reserve day 26’s exit minutes.
6. Replace unit 2’s day 12 allocation.
7. Redistribute unit 8’s drafting and production time.
8. Identify unit 1’s assigned scholarly work and use the reachable civic-life report address.
9. Run the course-scoped checks again after editing.

**For Cory:** No new question of scope, money, people or audience is required by these fixes.

## For the structure pass

1. **Make assessment coverage inspectable as data.** This course has fully written unit assessments, but `plan.py check` still reports the sequence stage. Add or complete social studies records for standard parts, items, error mappings, product evidence and response minutes so the gate can inspect more than day and code placement.

2. **Check complete time allocations.** Require every explicitly scheduled teaching day to include its reading, product and exit evidence. Flag both totals over 50 and separately required tasks with no slot.

3. **Make composite evidence explicit.** Store each component’s collection day, individual evidence, assessed parts and sitting status. A table row should distinguish work already collected from work newly required on assessment day.

4. **Give sources reproducible identifiers.** Require title, author or issuing body, date, URL or exact local path, selected passage and read status. Distinguish a publication from a general homepage and an assigned future source from one already read.

5. **Reconcile the skeleton with the template.** Several headers label runs longer than six days as one section. Clarify whether these are provisional unit-level placeholders or actual sections, and make the generator and checker follow that decision.

6. **Preserve read-only review instructions.** The supplied brief correctly permits a verdict despite an unrelated gate failure. Carry that rule into the standing reader guidance so it does not continue directing readers to return plans unread.


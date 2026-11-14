# Independent review: US History I scope and sequence

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/sequence-us-history-i-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files were changed.

## Verdict

Revise before acceptance. The nine-unit sequence is coherent, its calendar works, and the new narrative resolves several earlier concerns, but full assessment coverage, high school inquiry depth and some anchor content remain unsecured. The most important change is to specify what students must demonstrate for each owned standard, then rebalance the reform introduction within the existing days.

## What I read

- `docs/agents/EXPERT.md`, the social studies lens, the shared and social studies adoption bar, and `docs/courses/social-studies/STANDARD.md`.
- The complete course scope and sequence, all 160 `days.csv` rows, the course frame and partial-base source map.
- All 27 grade 11 `us1-*` progression rows and relevant incoming and outgoing handoffs.
- `CALENDAR.md` and grade 11 calendar records across subjects; the relevant ELA 11 frame provisions.
- The foundation, relevant roadmap and baseline requirements, glossary, shared approach, source catalogue, base-text register and sequence-writing brief. A separate social studies approach page remains unwritten.
- Earlier US History I frame reviews, the earlier independent sequence review, and relevant progression findings and fixes.
- Official Massachusetts and C3 passages; the selected constitutional and allotment guides; outside references linked below.

### Checks

| Command | Result |
|---|---|
| `python -B -X utf8 scripts/plan.py check` | Could not complete: the Python `markdown` dependency is missing. |
| `python -B -X utf8 scripts/frame.py calendar` | Passed; no stagger-rule break reported. |
| `python -B -X utf8 scripts/frame.py check us-history-i` | Passed: zero failures, nine units, 160 days. |
| `python -B -X utf8 scripts/plan.py check us-history-i` | Passed: zero sequence failures. |
| `python -B -X utf8 scripts/stale.py check` | Passed: 56 files, zero failures. |

The incomplete repository-wide gate does not withhold this verdict.

## Findings, most serious first

### 1. Unit assessments do not yet secure every owned performance

**Severity:** Major  
**LAYER:** sequence  
**REPEAT:** yes, earlier independent sequence review, finding 2  
**Confidence:** firm

**Location:** Assessment days 18, 70, 91 and 154.

**Problem:** The assessment descriptions reserve broad topics and unseen sources, but do not establish coverage of every taught requirement. Some omissions are substantive, beyond missing codes.

| Assessment | Unsecured coverage | Exact fix |
|---|---|---|
| Day 18 | Question construction, inquiry planning and expert-informed source evaluation are taught in unit 1 but have no identified assessment component. `MA.USI.T1.1` is absent from the assessment codes. | Add an independently completed inquiry proposal and source-selection rationale to the unit assessment record. Explicitly assess weighing economic, intellectual and cultural causes. |
| Day 70 | A paper on one reform cannot establish common understanding of every reform strand the plan promises to teach. | Identify common survey questions covering the taught strands, alongside the selected research product and unseen-source task. |
| Day 91 | The causal explanation and historian critique are explicit; evidence selection, source disagreement, claim revision and sustained argument are not assigned assessment evidence. | Identify the independently scored essays and evidence records as assessment components for `D2.His.16`, `D3.3`, `D3.4` and `D4.1`. |
| Day 154 | The description and codes do not secure website sponsorship/authorship or assertion versus verification and evidence versus inference. | Require those distinctions explicitly and include `MA.NML.T4.1` and `MA.NML.T4.3`. |

**Why it matters:** A unit writer could produce a valid-looking assessment that tests only part of the unit’s standards.

**Exact fix:** Add a compact blueprint for each unit identifying the requirement, assessment component, evidence date and response opportunity. Existing independent products may supply components; the single assessment period need not reproduce every extended performance. Course-level checks remain cumulative returns, not substitutes for missing unit coverage.

The earlier concern about the reform paper finishing after the assessment is resolved by the present days 69 to 71. Do not restore that older arrangement.

### 2. Unit 1 retrieves inquiry routines without explicitly carrying their full owned depth

**Severity:** Major  
**LAYER:** sequence  
**REPEAT:** yes, earlier sequence review, finding 3; progression review, finding 1  
**Confidence:** firm

**Location:** Days 2 to 4 and 13.

**Problem:** “Contested questions,” supporting questions and checking a website’s sponsor do not explicitly require expert agreement and disagreement, questions emerging from source work, or evaluation using expert appraisal. These are distinct requirements in the [C3 indicator tables, printed pages 23 to 24 and 54](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf).

**Why it matters:** Students could complete generic research planning while missing the disciplinary work the course owns.

**Exact fix:**

- Day 2: compare two short scholarly interpretations and explain their agreement and disagreement about the enduring issue.
- Day 3: connect supporting questions to that comparison and justify the source types selected.
- Day 4: evaluate at least one source using an accessible expert appraisal.
- Day 13: explain how source analysis generates or changes a question; explicitly include date, place and audience in the source judgment.

Supply printed commentary and appraisal evidence for the paper path. Preserve the eight-source portfolio requirement, including two sources the class has not studied.

### 3. The local standard paraphrase loses part of the required slavery comparison

**Severity:** Major  
**LAYER:** standard, progression, frame, sequence  
**REPEAT:** yes, the same kind of incomplete standard carrying identified in the progression review; this particular omission is newly identified  
**Confidence:** firm

**Location:** `MA.USI.T3.3` in `data/standards/ma-hss-2018.txt:485`; `us1-slavery-economy`; unit 4; day 58.

**Problem:** The official anchor asks students to explain slavery’s growth after 1800 in the Southern states, Caribbean islands and South America. The local paraphrase removes the latter two regions, and the receiving plan consequently concentrates on United States cotton expansion and the domestic slave trade. See [Massachusetts 2018, PDF page 123, printed page 123](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf).

**Why it matters:** Following the local standard faithfully would still leave an owned requirement untaught.

**Exact fix:** Restore the regional requirement in the own-word standard record and receiving instructions. On day 58, use a short comparative map and evidence table connecting United States cotton expansion with plantation expansion in the Caribbean and Brazil. Retain the domestic slave trade, distinguish regional trajectories, and include the comparison in day 70’s blueprint.

This completes an existing standard without moving it or adding a separate unit.

### 4. The reform survey is overloaded and leaves lettered content unsecured

**Severity:** Major  
**LAYER:** sequence, standard  
**REPEAT:** yes, earlier sequence review, finding 4  
**Confidence:** firm on missing specifications; likely on pacing

**Location:** Days 54 to 56 and 61; `MA.USI.T4.2b`, `.2c` and `.2e`.

**Problem:** Day 55 gives one 50-minute period to five reform strands, temperance, prison reform and the research question set. Abolition returns on day 65, but the other four strands have no clearly allocated common teaching beyond that survey.

The carrying instructions omit or blur women’s educational opportunities and ties to abolition, compulsory schooling and literacy growth, and the Transcendentalists’ ideas. The local `.2e` paraphrase also omits materialism and abolitionism from the official list. See [Massachusetts 2018, PDF page 124, printed page 124](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf).

**Why it matters:** Students choose their research subject before receiving a workable common foundation. A teacher could satisfy the day’s wording by naming movements rather than teaching their substance.

**Exact fix, within existing days:**

- Day 55: abolition, women’s rights and education, and public schooling, literacy and publishing.
- Day 56: disability and asylum reform, Transcendentalism, then research-question selection.
- Day 61: complete the source plan while judging and filling the source list.

Use temperance and prison reform as brief connected examples. Specify each strand’s content and require the selected investigation to address its complete option. This provides two periods of common orientation while retaining the week 12 question milestone.

Five separate research projects are not required.

### 5. The early-republic block loses foreign-policy evaluation and misstates the transfer of power

**Severity:** Moderate  
**LAYER:** sequence, frame  
**REPEAT:** yes, earlier sequence review, finding 5  
**Confidence:** firm

**Location:** Days 29 to 31; frame unit 2.

**Problem:** Washington’s day lists domestic policies but omits neutrality and the Jay Treaty, which the progression carries. Day 30 and the frame call 1800 the first peaceful handover without qualification.

**Why it matters:** Students lack a balanced basis for evaluating federal power and foreign policy, and could learn an incorrect chronological distinction. Washington peacefully transferred office to Adams in 1797, as the [National Park Service account](https://www.nps.gov/places/john-adams-inauguration.htm) documents.

**Exact fix:** Add neutrality and the Jay Treaty to day 29’s comparison. Connect Adams’s domestic measures to the foreign crisis and opposition. Replace the transition wording with:

> Explain how the election of 1800 led to the first peaceful transfer of the presidency between rival political parties in 1801.

Carry the correction into the frame and assess both federal power and foreign policy on day 33.

### 6. The action sequence stops at deciding, and its Government substitution leaves two days undefined

**Severity:** Moderate  
**LAYER:** sequence, frame  
**REPEAT:** yes, earlier sequence review, finding 6  
**Confidence:** likely

**Location:** Days 136 and 137.

**Problem:** Students investigate options and decide whether and how to act, but no scheduled task explicitly carries out a chosen step or reflects on its consequences. The progression calls for sharing through a safe route. The Government substitution names a replacement project without explaining what students do during these two history periods.

**Why it matters:** The yearly action can become a planning exercise, or the substitution can leave unplanned time. The [Educating for American Democracy explanation of inquiry](https://www.educatingforamericandemocracy.org/the-roadmap/) connects inquiry with applying conclusions through action.

**Exact fix:** Keep both periods. Day 136 investigates and compares options. Day 137 supports a feasible chosen step, or an evidence-based decision against action, followed by reflection.

When Government supplies the shared action, use these history periods to revisit its evidence, compare it with Progressive-era responses and evaluate the outcome. Government’s action occurs earlier in the year, so this is a return, not simultaneous work. Preserve student choice and adult mediation of outside communication.

### 7. The required shorter path is absent

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, requested within finding 1 of the earlier sequence review  
**Confidence:** firm

**Location:** Course introduction and pacing provisions.

**Problem:** The plan specifies 160 periods of 50 minutes but gives no shorter path. The shared adoption bar’s C2 explicitly requires one.

**Why it matters:** A teacher with shorter periods must decide independently which reading, practice or products to sacrifice.

**Exact fix:** Add a shorter-period route that identifies reductions by section. Preserve owned content, readiness work, all three argument cycles, the research requirements, assessments and response time. Identify which reading lengths, repeated examples and sharing routines are reduced, and explain how the independent history path still works without ELA.

Do not present an unexplained instruction to “shorten activities” as the route.

### 8. One candidate cell remains only partly settled

**Severity:** Minor  
**LAYER:** sequence  
**REPEAT:** yes, earlier sequence review, finding 1  
**Confidence:** firm

**Location:** Frame unit 7’s candidate cell and the sequence’s candidate table.

**Problem:** The frame proposes the Gilded Age party system **and** political machines. The sequence settles machines on day 113 but does not explicitly retain or drop the broader party-system expansion.

**Why it matters:** A later writer cannot tell whether that additional content has been dropped or merely overlooked.

**Exact fix:** Record: “Political machines retained within day 113; a separate Gilded Age party-system treatment dropped to protect the existing industry and immigration allocation.” No added day or standard movement is needed.

The other listed candidates have explicit destinations or recorded reasons for dropping them.

### 9. Current-status notes still contradict the completed plan

**Severity:** Minor  
**LAYER:** process, base text  
**REPEAT:** yes, stale completion notes in earlier frame and sequence reviews  
**Confidence:** firm

**Location:** Sequence “For the lead” item 3 and “For Cory”; `STANDARD.md:25-27`; adoption bar literacy paragraph.

**Problem:**

- The sequence says teaching the Boldt decision itself would need another day, although day 25 already names it and the retained Level 1 guide centers it.
- The sequence proposes putting Red Summer in another course but ends “For Cory: None.”
- The standard policy and adoption bar still describe RH/WHST loading as open, although the separate literacy standards file exists and this frame already uses it.

**Why it matters:** These statements can prompt redundant work or conceal an unresolved scope decision.

**Exact fix:** State that day 25 retains the bounded Level 1 Boldt case; additional levels are excluded. Put the Red Summer disposition under “For Cory,” without treating a transfer as authorized. Add dated literacy-status corrections distinguishing the loaded separate standards file from the remaining placement work.

The [retained Level 1 guide](https://ospi.k12.wa.us/sites/default/files/2023-10/us-hs-unit1-level1.pdf) confirms the one-period allocation and the centrality of the decision.

## Coverage, order and load

All five `T3.2` lettered parts have explicit placements: **a/d on day 52, b on 57, c on 54, e on 53**. All five `T4.2` options are named, with substantive exceptions in finding 4. All eleven `T7.5` parts are placed: **a/b on 140, c/d on 141, e to i on 142, j on 148, k on 151**.

Placement does not settle full treatment. Findings 1 to 4 identify the important remaining differences.

| Unit | Total days | Teaching days excluding assessment and response | Load judgment |
|---|---:|---:|---|
| 1 | 19 | 17 | Proportionate for content and inquiry; complete the inquiry specifications. |
| 2 | 15 | 13 | Plausible with the bounded constitutional case. |
| 3 | 13 | 11 | Plausible; the reason for teaching removal before the expansion maps is explicit. |
| 4 | 21 | 19 | Overall allocation justified; one survey day carries too much breadth. |
| 5 | 21 | 19 | Tight: six drafting days leave 13 other teaching days. Protect feedback and content instruction. |
| 6 | 13 | 11 | Tight, particularly day 107’s three-case legal comparison. Preserve citizenship, voting and protections for persons as distinct questions. |
| 7 | 13 | 11 | Proportionate, drawing on earlier industrial history. |
| 8 | 17 | 15 | Plausible once action and substitution tasks are explicit. |
| 9 | 16 | 14 | Tight but defensible with one empire report, three drafts and one debate. |
| **Units** | **148** | **130** | Plus 12 course-level check and response days. |

No whole unit is demonstrably far overallocated. The clearest underallocation is the common reform orientation: five strands plus two additions and project orientation in one period.

No unit exceeds 25 days, so none requires a mid-unit assessment under the stated rule. Readiness checks occupy the first receiving units for the named long-gap content. Response time is counted once.

## Calendar and same-year leans

The checks match the frame and calendar:

| Check | Assessment days | Response | Weeks |
|---|---|---|---|
| First | 48 to 49 | 50 | 10 |
| Mid-year | 93 to 95 | 96 | 19 to 20 |
| Year-end | 156 to 158 | 159 to 160 | 32 |

Grade 11 has no pre-finals stagger restriction. The simultaneous year-end checks are permitted.

The ELA calendar supports the shared research project: ELA unit 4 occupies days 56 to 78, while history’s question, source-list, draft and scoring milestones fall on days 56, 61, 66 and 71. ELA’s argument unit precedes history unit 5; Douglass follows history’s slavery context; the tenement unit follows history’s immigration unit.

History teaches its early research cycle and later lateral-reading routine itself, so those leans do not require ELA instruction first. Exact ELA daily assignments remain a later coordination check.

## Partial-base source map

The map now records the selected guides, omitted alternatives and later-period exclusions. Source unit 1 precedes source unit 2, and each retained guide follows its prerequisite instruction.

- Unit 1, Level 1: day 25, one period.
- Unit 2, Level 2: days 104 and 105, two periods.
- Other levels in those units: excluded with reasons.
- Source units 3 to 6: excluded from this course because their main periods fall later.

The stored allotment guide confirms two periods and the progression from reading the Act to examining its results. At unit planning, supply a printed alternative to its internet quotation search. The constitutional guide’s cartoon and follow-up sharing also need an explicit within-day adaptation.

The earlier finding that the narrative and map were absent is resolved. Component-level rights and final adapted materials remain unverified.

## Lens checklist: scope and sequence

| Lens line | Result |
|---|---|
| Compelling questions need sources and permit defensible answers | **Met at planning level.** Claims, research products and the League debate address the questions. |
| History follows chronology or explains departures | **Met.** The narrative explains the important thematic returns and removal-first ordering. |
| Contested events carry more than one account | **Met at planning level.** Multiple positions are assigned for taxation, removal, reform, Reconstruction and empire. Final source balance awaits unit plans. |
| Source-based writing recurs and builds from short to long | **Met.** Short claims lead to research and sustained arguments. Findings 1 and 2 strengthen the evidence and assessment specifications. |

## What is right and should remain

Preserve the nine-unit structure, linked Northern and Southern economies, one empire report serving as the third argument, separately scored causal explanation, and shared ELA research product. Keep Native nations in the present tense, enslaved people’s agency, source testing of Lost Cause claims, slur-free presentation and student choice in action.

## Settled by the expert

These are recommendations for the caller, not edits made here.

| Choice | Reason | Files affected |
|---|---|---|
| Use identified independent products within composite unit assessments | Extended performances need explicit evidence without another assessment day | Sequence; assessment-day notes |
| Add scholarly comparison, expert appraisal and question revision to existing unit 1 days | Completes owned inquiry depth | Days 2 to 4 and 13 |
| Restore the regional slavery comparison on day 58 | Completes the existing anchor | Standard record; progression; frame; sequence |
| Spread common reform orientation over days 55 and 56 | Makes informed selection feasible | Days 55, 56 and 61 |
| Correct the transfer-of-power wording and restore Washington’s foreign-policy strand | Removes a factual error and a carrying gap | Frame; days 29 to 31 |
| Use history’s action days to evaluate the shared Government action when applicable | Gives the substitution a defined instructional purpose | Frame; days 136 and 137 |
| Retain machines and drop a separate party-system expansion | Settles the remaining candidate without adding days | Candidate table |
| Keep the selected one-period and two-period partial-base allocations | Publisher guides support those bounds | Source map; unit-planning instructions |

## For Cory

- **Scope:** Settle the Red Summer disposition. The sequence proposes adding it to US History II; this review does not authorize changing that course.

No money, staffing or audience decision is requested.

## Sources and limits

- [Massachusetts History and Social Science Framework, 2018](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf): checked relevant content requirements and lettered reform parts.
- [C3 Framework, revised PDF](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf): checked owned inquiry, source-evaluation and argument requirements.
- [Since Time Immemorial constitutional guide](https://ospi.k12.wa.us/sites/default/files/2023-10/us-hs-unit1-level1.pdf): checked content and stated allocation.
- [Since Time Immemorial allotment unit](https://ospi.k12.wa.us/student-success/resources-subject-area/john-mccoy-lulilas-time-immemorial-tribal-sovereignty-washington-state/high-school-curriculum/high-school-unit-2-us-history): live access was blocked; the stored Level 2 publisher guide was read through read-only text extraction.
- [Reading Like a Historian overview](https://www.inquirygroup.org/history-lessons): compared question-led documentary inquiry and source-reading routines; individual lessons were not inspected.
- [Educating for American Democracy Roadmap](https://www.educatingforamericandemocracy.org/the-roadmap/): checked the relationship between inquiry, conclusions and civic application.
- [National Park Service inauguration account](https://www.nps.gov/places/john-adams-inauguration.htm): verified the 1797 peaceful transfer.

Actual assessment items, excerpt difficulty, complete historical accuracy, sensitivity treatment and third-party rights require later unit-level review. Pacing recommendations are professional judgments, not measured classroom results. Prior memory informed review conventions only; no substantive finding rests solely on memory.

**For the source list:** Record the working direct constitutional-guide address and the continued live-access limitation for the allotment unit.

**Verdict: Revise before acceptance. Finding count: 9. Report path: `docs/reviews/sequence-us-history-i-2026-11-14.md`, supplied here only.**


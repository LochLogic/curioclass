# Independent sequence review: US Government and Politics

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/sequence-us-government-and-politics-2026-11-14.md`  
**Delivery:** Complete report below. No file was created or changed.

## Verdict

Revise before acceptance. The course has a coherent overall order, complete code placement and a sound calendar, but several assessment descriptions do not secure the performances they claim, and the paper route leaves additional digital requirements incomplete without saying so. The most important change is to identify the actual evidence assessed for each standard, then resolve the concentrated workload within the existing unit totals.

## What I read

- `docs/agents/EXPERT.md`, the social studies lens, the social studies adoption bar and `docs/courses/social-studies/STANDARD.md`.
- The complete Government scope and sequence, all 80 `days.csv` rows and the course frame.
- All 19 `gov-*` progression rows and the incoming rows relevant to their prerequisites.
- Government and News/Media Literacy standards in `data/standards/ma-hss-2018.txt`, alongside the official framework; the owned C3 indicators.
- `docs/courses/CALENDAR.md` and the Government, ELA 11, ELA 12 and Algebra II calendar rows, with relevant ELA frame provisions.
- Foundation, required Roadmap sections, approach guidance, source-access notes, BASELINE rules 20 to 24, glossary and base-text policy. The approach page says its social studies companion is still unwritten.
- Both earlier Government frame reviews, their fix report, the social studies baseline fix report, and relevant findings in the earlier civics and grade 5 sequence reviews.
- Outside sources linked below.

### Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Could not complete: Python package `markdown` is missing. |
| `python -X utf8 scripts/frame.py calendar` | Completed; no stagger-rule failure reported. |
| `python -X utf8 scripts/frame.py check us-government-and-politics` | Passed: 9 units, 80 days, including 76 unit days and 4 course-level days. |
| `python -X utf8 scripts/stale.py check` | One failure in another course: `docs/courses/us-history-ii/frame.md:78`, a landed pending reference. |

The unavailable full gate and unrelated stale failure do not withhold this verdict. No mutation, turn-management or defect-logging command was run.

## Findings, most serious first

### 1. Assessment descriptions claim more than their tasks establish

**LAYER:** sequence  
**REPEAT:** yes, the same code-to-task mismatch appears in the earlier civics and grade 5 sequence reviews.  
**Severity:** serious  
**Confidence:** firm

**What is wrong.** Several assessment rows finish with “covers every part,” but their described tasks omit substantial required work. Listing a code does not establish that the assessment elicits its performance.

The clearest example is day 70: judging one unseen past policy does not establish the past/current comparison, information gathering, factual reporting, editorial writing and visual communication claimed in its code list. Day 14 likewise cannot establish actual deliberation in multiple settings through a written document interpretation alone.

**Why it matters.** A writer could administer the described assessments faithfully and still have no scored evidence for important standards. The [Massachusetts framework](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf) distinguishes research, presentation, comparison and production; the [C3 Framework](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf) also requires performed deliberation and participation.

**Exact fix.** Make each end-of-unit assessment composite where needed: retain the unseen task, identify independently completed work collected earlier, and state its scoring criteria. At minimum:

| Assessment day | Evidence to reserve explicitly |
|---|---|
| 5 | Comparison of old and modern association arguments, and a critique of relationships among government, civil society and markets. Day 4 can supply an individual response. |
| 14 | Federalist/Anti-Federalist comparison; the research presentation from days 10 to 11; observed deliberation in both settings on days 12 to 13. |
| 21 | Comparison of governmental systems and domestic institutional powers, beyond whichever single dispute is selected. Include the town/city and open/representative town-meeting distinctions taught on day 19. |
| 34 | Agency research from day 26; majority/dissent argument; historical checks-and-balances cases; four-level procedure evaluation; the limited-government argument. Identify the existing day products that carry these. |
| 45 | The contextualized two-decision presentation from day 42 and comparison of rights documents, alongside the unseen application. |
| 54 | Party development and organization; interest-group/PAC development and evaluation; news-industry structure and media-effects research. The election package alone does not reserve these. |
| 62 | Governmental/nongovernmental organization comparison, evaluation of US participation, and the researched regional argument with a counterclaim from days 60 to 61. |
| 70 | Past/current comparison from day 65, information-gathering evidence from day 68, and both written genres and visual work from day 69. |
| 79 | Each student’s contribution, observed collaboration and deliberation, and evidence of completed action. A hypothetical compromise and a team portfolio score alone are insufficient specifications. |

These are assessment components, not additional assessment days. Preserve the existing respond days and give teachers a criterion-level record showing which evidence needs a response.

For T2.8 and T4.6, retain legitimate example choices. Do not turn the agency and policy example lists into six agency projects or five full policy investigations per student.

### 2. Additional digital requirements disappear on the paper route

**LAYER:** sequence, standard  
**REPEAT:** yes, incomplete digital coverage was identified in the earlier Government frame review; this finding identifies further affected codes.  
**Severity:** serious  
**Confidence:** firm

**What is wrong.**

- Day 68 substitutes printed clippings for digital information work while claiming `MA.NML.T5.1`. Its goal also stops at gathering, without explicitly carrying organization, analysis and synthesis.
- Day 69 requires student-made visuals but never specifies digital production for `MA.NML.T5.3`.
- On the expert-supported route, day 76 says students work through an adult, but does not require the digital collaboration needed for full `MA.NML.T5.5`.

The [official framework, News/Media Literacy topic 5](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf#page=179), makes these digital elements explicit.

**Why it matters.** A wholly paper-based student can complete the stated tasks while the record claims full coverage of T5.1 and T5.3. An arranged expert conversation could also be entirely offline.

**Exact fix.**

1. Specify digital-route evidence on day 68: a student-directed search or data collection, an organized source/data record, and a synthesis.
2. Specify a student-designed digital visual on day 69, using a shared or adult-mediated device where appropriate.
3. For full T5.5 coverage, require an actual digital exchange that contributes to the project, with an adult mediating contact.
4. State route-specific partial coverage wherever those performances are absent. Printed clippings, handmade visuals and offline correspondence remain useful work, but do not establish the omitted digital elements.

Cory’s 2026-11-14 decision already permits optional outside collaboration and partial T5.4/T5.5 coverage. I do not reopen that decision. The additional T5.1/T5.3 limitation needs an explicit scope disposition rather than an unqualified coverage claim.

### 3. Three teaching blocks concentrate too much work into single lessons

**LAYER:** sequence  
**REPEAT:** yes, research and pacing compression were raised in both Government frame reads.  
**Severity:** moderate  
**Confidence:** judgment call

**What is wrong.** The concern is the number of distinct intellectual tasks assigned together, not simply the number of codes.

| Block | Available teaching days | Concentrated demand |
|---|---:|---|
| Unit 2, days 7 to 13 | 7 | Day 12 combines efforts from abolition to the present, the whole Letter from Birmingham Jail, and a seminar. |
| Unit 4, days 23 to 33 | 11 | Day 31 combines reconciliation, war powers and evaluation of procedures at four governmental levels. International institutions are otherwise introduced on day 59. |
| Unit 8, days 64 to 69 | 6 | Day 69 produces two genres, two visuals and an explanation of their differences, following only one information-gathering day. |

The [King Institute’s account](https://kinginstitute.stanford.edu/letter-birmingham-jail) establishes the Letter’s historical setting and multiple argumentative concerns. It does not establish a classroom reading time; this pacing judgment is not a measured result.

**Why it matters.** The likely losses are contextual explanation, source analysis, revision and the chance to answer the unit question thoughtfully.

**Exact fix within the existing totals.**

- **Day 12:** use a bounded, contextualized excerpt set from the Letter for the required seminar. Keep the complete Letter as further reading. Replace the unit 2 readiness explanation’s claim that the documents are reread “in full” with “retaught through the provisions and passages needed for this unit.”
- **Day 31:** retain reconciliation and war powers. Move the four-level procedure evaluation into day 33’s hearing and constitutional-design argument, using four short source cards. Supply a brief introduction to the Security Council procedure before students evaluate it.
- **Days 67 to 69:** use day 67’s contrasting news and opinion pieces as writing models. On day 68, organize and synthesize the bounded source set and begin the factual report. On day 69, complete the editorial, visual communication, genre comparison and revision. Set manageable product lengths explicitly. One digital graphic may serve both pieces with suitable captions.

Preserve all four historical checks-and-balances cases and the substantive policy comparison. No standard moves between units.

### 4. The required shorter path is absent

**LAYER:** sequence  
**REPEAT:** yes, the same omission appears in the earlier civics and grade 5 sequence reviews.  
**Severity:** moderate  
**Confidence:** firm

**What is wrong.** The plan specifies 80 meetings of 50 minutes, or 4,000 minutes, but gives no shorter path. Foundation section 5 requires one when ordinary schools have less time.

**Why it matters.** Teachers with shorter periods have no defensible guide to compression. The busiest lessons are already vulnerable.

**Exact fix.** Add a shorter-path table after the calendar explanation. State its meeting count and minutes, then name the changes by unit: shared source sets, abbreviated presentation formats, bounded writing lengths and reduced repetition. Preserve required teaching, readiness support, independently assessable evidence and response.

Do not silently remove the five retained addition days or treat required work as uncounted homework. The shorter path’s intended time and audience belong to Cory; a concrete option is 80 meetings of 40 minutes, totaling 3,200 minutes.

### 5. Unmarked stale instructions still conflict with the sequence

**LAYER:** process, frame, progression  
**REPEAT:** yes, contradictory readiness and planning instructions recur in earlier sequence reviews.  
**Severity:** moderate  
**Confidence:** firm

**What is wrong.** The stale checker does not identify several live contradictions:

- The frame still says the scope and sequence will set the days later.
- The frame’s unit 9 row and `gov-local-action` progression notes still require every student to complete digital production and outside digital collaboration unconditionally. The later frame decision and sequence allow partial routes.
- The frame’s inquiry summary still says teams arrange their outside collaborator before unit 9.
- The sequence’s two “For the lead” corrections remain unapplied in the frame.
- Frame cross-subject estimates still place unit 8 around weeks 12 to 14 and unit 6 around weeks 9 to 10. Their actual spans are weeks 13 to 15 and 10 to 11.

**Why it matters.** Later writers can follow different files and build incompatible requirements.

**Exact fix.** Reconcile those statements in one cleanup:

- Apply both corrections already written under the sequence’s “For the lead.”
- Make collaboration conditional consistently in the inquiry summary, unit table, seams and progression notes.
- Record full and partial coverage conditions consistently, including finding 2.
- Replace provisional timing with the actual calendar spans.
- Replace the frame’s future-tense status sentence with a pointer to the written sequence.

Leave historical reviews intact. Their earlier recommendations are evidence of prior decisions, not current instructions.

## Coverage, order and days by load

All 19 owned skills are placed. All 54 numbered Government/NML codes and ten owned C3 indicators appear on both teaching and end-assessment days. That establishes placement; findings 1 and 2 qualify full performance coverage.

| Unit | Total days | Teaching days | Load judgment |
|---|---:|---:|---|
| 1 | 6 | 4 | Tight but coherent: foundations, theories, ideologies and associations. Protect the combined readiness support. |
| 2 | 9 | 7 | Sound document-to-argument arc; day 12 needs the bounded reading in finding 3. |
| 3 | 7 | 5 | Clear systems-to-powers-to-sovereignty progression. Keep present-day tribal government substantive. |
| 4 | 13 | 11 | Largest institutional load appropriately gets the most days; redistribute day 31’s comparison. |
| 5 | 9 | 7 | Sensible progression from rights documents to decisions and press freedom. |
| 6 | 9 | 7 | Coherent parties-to-groups-to-media arc; assessment evidence needs expansion. |
| 7 | 8 | 6 | The earlier extra day usefully protects research and argument. |
| 8 | 8 | 6 | Two policy-comparison days and four current-issue days; production needs a clearer division. |
| 9 | 7 | 5 | Earlier issue selection and reused reporting make this plausible, conditional on bounded products and optional-contact rules. |
| **Total** | **76** | **58** | Four additional days hold the two course-level checks and their responses. |

The remaining 22 days comprise 11 assessment days and 11 respond days, each counted once. No unit exceeds 25 days, so no additional mid-unit assessment is required.

No whole unit is demonstrably far overallocated. The demonstrated risk is concentration within particular days.

## Calendar and cross-subject leans

- Government’s checks fall on days 36 and 72, weeks 8 and 15, matching `calendar.csv`. Unit 9 closes in week 16. CALENDAR.md imposes no additional high school stagger rule.
- Government’s founding unit, days 7 to 15, precedes ELA 11’s founding unit, days 35 to 55. The separate reading lenses are stated.
- For a grade 11 student, ELA informative and argument work is scheduled before Government’s day 69.
- For a grade 12 student, ELA 12’s argument is completed around day 38; informative writing is carried from ELA 11.
- The Betts/Gideon default avoids repeating ELA 12’s later Plessy/Brown pair.
- Algebra II’s statistics unit falls on days 137 to 157, after Government’s days 49 and 53. The local sample/source/margin bridge correctly avoids assuming later inference instruction.
- Discussion norms come from earlier grades; the ELA seminar routines also begin early.

The principal dormant-knowledge checks sit before the new work they support. Unit 2’s readiness placement is sensible, but its frame wording needs reconciliation as identified above.

## Candidate cells and source map

Every candidate named in this frame is settled as retained, with a placement and stated cost:

| Placement | Retained additions | Added days |
|---|---|---:|
| Unit 1 | Ideologies and socialization | 1 |
| Unit 3 | Commerce Clause cases | 1 |
| Unit 4 | Congress | 2 |
| Unit 6 | Electoral College and state election rules | 1 |
| Within owned work | Founding readings, rights documents and case-pair extensions, fiscal federalism, polls, treaty practice, policy stages and contacting officials | 0 separately counted |
| **Total** | | **5** |

Those five days are about 8.6 percent of the 58 teaching days. Zero separately counted days still require actual minutes, especially for the Letter.

A complete base-lesson source map is **not applicable**: this is an own-course sequence using partial sources. Chapter notes identify possible material rather than promise whole-book adaptation. Selected passages, rights and credits still need unit-level verification.

## Lens checklist: scope and sequence

| Lens line | Result |
|---|---|
| A unit question requires its sources and permits defensible answers | **Met in design.** The frame supplies substantive questions; tasks must preserve that demand when written. |
| History follows chronology, or gives a reason otherwise | **Met.** This is a reasoned topical civics sequence, with historical development inside topics. |
| Contested events receive more than one telling | **Met as a planning commitment.** Federalist/Anti-Federalist texts, majority/dissent work, competing positions and community sources are specified. Actual selections remain to be judged. |
| Writing from sources recurs and develops | **Met for recurrence; partly secured for execution.** Research presentations, arguments, reporting, editorials and the capstone recur. Findings 1 and 3 protect their evidence and workload. |

## What is right and should remain

- Keep the order from government’s purposes through institutions, rights, influence, world affairs, policy and action.
- Keep the grade 11 entry route without assuming completion of US History I.
- Keep constitutionalism and republicanism explicitly attached to document provisions.
- Keep present-day tribal sovereignty, own-state comparisons and community-authored sources.
- Keep the two deliberation settings, majority/dissent work and student choice of position.
- Keep unit 8’s early issue selection and reuse of its reporting in unit 9.
- Keep a completed, safe action for students declining public advocacy, followed by reflection.
- Keep the default rights pair and the local statistics bridge.

The earlier demand for mandatory outside collaboration has been superseded by Cory’s explicit decision. The earlier request for a qualified outside sensitivity reader has also been superseded by the revised Foundation. Neither is repeated as an unresolved requirement here.

## Settled by the expert

| Choice | Reason | Files affected when applied |
|---|---|---|
| Retain nine units and 80 days | No demonstrated need to change course length or ownership | Frame; scope and sequence |
| Use composite assessment evidence | Actual research, deliberation and production cannot all be established by the unseen written tasks | Scope and sequence; `days.csv`; later assessment plans |
| Use bounded Letter excerpts for day 12 | Preserves its role while protecting context and seminar time | Scope and sequence; `days.csv` |
| Put four-level procedure evaluation into day 33 | Relieves day 31 and connects procedures to constitutional effectiveness | `days.csv`; unit 4 sequence explanation |
| Begin reporting on day 68; permit one graphic with two uses | Protects synthesis and revision without adding days | `days.csv`; unit 8 sequence explanation |
| Preserve example choices in T2.8 and T4.6 | Example lists do not require equal-depth research on every option | Assessment blueprints |
| Retain conditional collaboration and disclose partial coverage accurately | Follows Cory’s current decision | Frame; progression notes; sequence |

## For Cory

- **Scope and audience:** decide whether paper-only partial coverage may also include NML.T5.1 and T5.3, or whether full coverage requires a brief shared-device component.
- **Audience and time:** set the intended shorter-path budget. The concrete option above is 80 meetings of 40 minutes.

No new spending, outreach or outside reviewer is proposed.

## Limits and outside sources

Actual assessment items, selected source difficulty, scoring reliability and classroom minutes cannot yet be judged. Pacing recommendations are professional judgments, not pilot results.

No substantive curricular finding rests on unverified subject memory. Prior memory notes informed review method only.

- [Massachusetts History and Social Science Framework](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf): Government and News/Media Literacy requirements; example-list distinctions.
- [C3 Framework, revised June 2017](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf): owned civics indicators and performed deliberation/action.
- [California History-Social Science Standards](https://www.cde.ca.gov/be/st/ss/documents/histsocscistnd.pdf): targeted checks of civil society, Congress and elections additions, not a complete comparison.
- [Government framework corrections effective fall 2026](https://apcentral.collegeboard.org/media/pdf/ap-us-government-and-politics-course-and-exam-description-clarifications.pdf): verified the comparison edition’s added documents. Their unit-level decisions remain a later planning requirement.
- [Educating for American Democracy Roadmap](https://www.educatingforamericandemocracy.org/the-roadmap/): inquiry, civic knowledge and participation framing.
- [King Institute: Letter from Birmingham Jail](https://kinginstitute.stanford.edu/letter-birmingham-jail): historical setting and argumentative context. The linked full-text PDF could not be opened.
- [Washington high school tribal-sovereignty curriculum](https://ospi.k12.wa.us/index.php/student-success/resources-subject-area/john-mccoy-lulilas-time-immemorial-tribal-sovereignty-washington-state/high-school-curriculum): live fetch returned 403. This review does not certify the selected adaptation’s accuracy or rights.

**For the source list:** add the King Institute context page if absent, recording that its context article, rather than the full Letter, was read.

**Verdict: revise before acceptance. Finding count: 5. Report path: `docs/reviews/sequence-us-government-and-politics-2026-11-14.md`, delivered here only.**


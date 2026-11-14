# Independent sequence review: social studies, grade 1

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/sequence-social-studies-grade-1-2026-11-14.md`  
**Delivery:** Complete report below. No file was created or edited.

## Verdict

Revise before unit planning: the broad teaching order and unit allocations are defensible, but the assessment descriptions do not secure full coverage of the standards they list. The largest risk is apparent completeness, especially where one selected response stands for several distinct requirements; the leader selection also needs updating against current primary evidence. The most important change is to specify the missing assessment evidence within the existing unit days.

## What I read

- `docs/agents/EXPERT.md`, the social studies lens, the shared adoption criteria and social studies bar, and `docs/courses/social-studies/STANDARD.md`.
- FOUNDATION, the required Roadmap sections, BASELINE rules 20 to 24, GLOSSARY, APPROACH, relevant APPROACH-SOURCES entries, and the sequence-writing and frame-writing rules.
- The complete grade 1 scope and sequence, all 96 rows of its `days.csv`, and its frame.
- The kindergarten, grade 1 and grade 2 social studies progression rows, relevant grade 3 receiving rows, and the recorded economics exclusions.
- The grade 1 Massachusetts standards, including lettered parts, and the relevant official C3 indicator wording.
- CALENDAR.md and the grade 1 calendar rows for all four core subjects; the corresponding ELA, math and science frame passages.
- Both earlier grade 1 frame reviews, relevant progression findings, and the social studies baseline review and fix record.
- The base-text record and the outside sources linked below.

Earlier notes helped identify review checks. All findings below rest on files or outside sources checked during this read, not on unaided memory.

## Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Did not complete: reported another course’s missing sequence, then stopped because Python lacks `markdown`. |
| `python -X utf8 scripts/frame.py calendar` | Completed; no grade 1 stagger break reported. |
| `python -X utf8 scripts/frame.py check social-studies-grade-1` | Passed, zero failures. |
| `python -X utf8 scripts/sequence.py check social-studies-grade-1` | Passed, zero failures. |
| `python -X utf8 scripts/stale.py check` | Did not complete: `KeyError: 'node'`. |

The interrupted repository-wide checks do not prevent the substantive verdict.

## Findings, most serious first

### 1. Assessment tasks omit work required by their listed standards

**Severity:** Major  
**LAYER:** sequence  
**REPEAT:** yes, the semantic coverage and assessment-depth problems identified in the progression review and baseline social studies finding 6  
**Confidence:** firm

**What is wrong:** The assessment rows often attach the complete code list to a narrower task. The clearest examples are day 67, which permits one symbol, phrase **or** song, and day 92, which lists values-based purchasing and banks without asking about either. These gaps survive the structural gate because placing a code does not establish that the task assesses it.

The governing requirements are the repository’s definition of an end-of-unit assessment and BASELINE rule 23. The official [Massachusetts framework, pages 39 to 42](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf#page=39) and [C3 Framework, relevant K-2 indicators](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf) establish the distinctions being checked.

**Why it matters:** A unit writer following these summaries can produce a passing record without evidence for important parts of the unit. Enlarging the final assessment day alone would also overload a 30-minute lesson.

**Exact fix:** Amend each assessment description and its corresponding prose paragraph as follows. Use the permitted observation window across the final teaching lessons, retaining the unseen-source task and the existing respond day.

| Unit and assessment | Missing or unsecured evidence | Required repair inside existing days |
|---|---|---|
| **1, day 9** | Breaking a question into smaller questions does not assess the disciplinary ideas and needed facts taught on day 2. Naming roles does not establish their contribution to the shared goal. | Add a brief question-to-idea/fact match. Explicitly score day 8 observations for participation, following the agreed rule and explaining how each role helps. Include what membership gives the group’s members. |
| **2, day 18** | Identifying a photograph does not assess selecting useful sources for a question. Placing dates alone does not secure the calendar-pattern and time-language work. | Present two possible source kinds and a school-history question; ask which would help and why. Add one short calendar-pattern explanation using past, present or future language. |
| **3, day 30** | The task asks about actions and qualities, but does not explicitly check the leader’s responsibility as a group member, student-generated historical questions, or answering a peer’s question. | Add the responsibility prompt and a question about the new leader. Record both asking and answering during the explanation exchange. Explicitly retain the written or dictated claim, reason and closing. |
| **4, day 40** | The listed codes include election meaning and fixed terms with judgments about re-election, but the task asks for a tally, ballot fairness, an office and a service. | Add an election-versus-issue-vote distinction and a short fictional term record requiring a reasoned re-election judgment. Day 38 can supply the latter observation evidence. |
| **5, day 54** | Finding a capital does not explain what makes it a capital. The task does not explicitly check rivers, lakes and mountains or what mapped features represent. | Add a capital explanation and a short feature-identification/explanation task. Specify which criteria the day 52 map contributes, rather than referring generally to its existence. |
| **6, day 67** | One choice among symbol, phrase or song cannot establish all three lettered parts. “United or diverse” permits half of the paired explanation to disappear. | Require evidence across **a, b and c**, and an explanation addressing **both** unity and diversity. Record meaning explanations during days 62 to 66; retain a new-source transfer task on day 67. |
| **7, day 79** | A helper story does not establish the citizenship distinction or the regional/global reach of the problem-and-action indicators. | Add fictional citizenship/community-membership examples without personal disclosure. Use the day 77 comparisons and a brief new picture case to assess problems and possible responses beyond the local setting. |
| **8, day 92** | The task omits employment vocabulary distinctions, explicit price reading, values-based buying, banks, and comparison of saving reasons. | Record selected observations during days 87 to 90 and expand the final task’s coverage statement. Make day 87 include analysis of supplied purchasing choices and day 88 include comparison, rather than listing reasons only. |

For unit 6, the earlier flag/eagle and meaning repairs are present in teaching. This finding concerns the narrower assessment, not a repetition of the repaired teaching omission.

### 2. The “good leader” case selection needs updating against current evidence

**Severity:** Major  
**LAYER:** sequence, frame, progression  
**REPEAT:** new in the earlier course and progression reports reviewed  
**Confidence:** firm on the source update; judgment call on the replacement

**Location:** Unit 3 prose, days 24 and 25, the frame’s leader examples and sensitivity directions, and `ss1-leaders.notes`.

**What is wrong:** Cesar Chavez appears as an uncomplicated example for answering “What makes a good leader?” The sensitivity note addresses working conditions but does not account for March 2026 statements concerning sexual abuse. [Dolores Huerta’s first-person statement](https://medium.com/@dolores_huerta/march-18-2026-e74c20430555?postPublishedType=initial) describes her experiences; the [UFW Foundation’s statement](https://ufwfoundation.org/statement-from-the-ufw-foundation/) acknowledges allegations involving women and minors and explains its cancellation of commemorative activities.

**Why it matters:** This particular six-year-old lesson is designed to establish admirable leadership qualities. An unqualified exemplar now requires contextual work that the planned lesson does not provide.

**Exact fix:** Replace the farmworker-organizing exemplar with **Dolores Huerta**, whose organizing contribution is documented by the [National Park Service](https://www.nps.gov/articles/000/new-era-of-farm-worker-organizing.htm). Preserve the farmworker history, four historical cases and the existing day allocation.

Place Huerta’s organizing case on day 24 and Mankiller’s later community leadership on day 25. Update the frame, progression example list and sensitivity directions together. This also repairs the present claim that Mankiller followed by Chavez is “in time order.” Select and date the specific leadership episodes, rather than treating entire overlapping lives as successive periods.

This is an item-level exemplar choice within the existing standards, not a change to the course’s scope.

### 3. Unit 4 blurs an election with an issue vote and undersupports its comparative question

**Severity:** Moderate  
**LAYER:** sequence, frame  
**REPEAT:** yes, the code-to-task mismatch kind identified in the social studies progression review  
**Confidence:** firm on terminology; likely on the inquiry repair

**Location:** Days 32 to 34, day 39, day 75, and the matching frame descriptions.

**What is wrong:** Day 33 correctly defines an election as choosing a leader. Day 34 then calls an unspecified vote “on a class matter” an election, while day 75 uses the same term for choosing an action. The sequence also asks for the “fairest way” to decide while developing only voting in enough detail to support the answer.

The [Massachusetts framework, page 39](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf#page=39) distinguishes selecting leaders from other decisions. The [C3 inquiry discussion, pages 23 to 25](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf#page=23) supports questions requiring defensible reasoning.

**Why it matters:** Students can learn that every ballot is an election and that the compelling question has a predetermined procedural answer.

**Exact fix:**

- On day 32, retrieve kindergarten’s discussion-and-agreement procedure and compare it with voting through two short classroom cases.
- On day 34, explicitly elect a willing class member to a temporary classroom responsibility, connecting the choice to unit 3’s leadership qualities.
- On day 39, require a reasoned choice of a fair procedure for a supplied situation, using the cases and ballot experience.
- Rename day 75’s choice of an action a **secret-ballot vote**, and make the same correction in the frame.

Keep the unit question and day count.

### 4. The actual calendar requires four meetings in three weeks

**Severity:** Moderate  
**LAYER:** sequence, frame  
**REPEAT:** yes, the calendar-feasibility mismatch kind raised in the baseline structure review  
**Confidence:** firm

**Location:** Scope and sequence introduction, frame Days bullet, and `days.csv.school_day`.

**What is wrong:** The sequence promises three lessons weekly across 31 weeks, but that supplies 93 meetings. The actual 96-row schedule contains these exceptions:

| Week | Course days | Meetings | Time at 30 minutes each |
|---|---|---:|---:|
| 11 | 31 to 34 | 4 | 120 minutes |
| 21 | 62 to 65 | 4 | 120 minutes |
| 31 | 93 to 96 | 4 | 120 minutes |

The frame instead describes 32 teaching weeks. Agreement between the two calendar files does not resolve this mismatch with the stated teaching schedule.

**Why it matters:** A teacher reserving three weekly slots cannot run the published schedule through its week 31 endpoint.

**Exact fix:** Put the actual schedule to Cory as an audience/time decision. The concrete proposed wording is:

> Ninety-six meetings across 31 weeks: three 30-minute meetings in 28 weeks and four in weeks 11, 21 and 31.

If accepted, replace both conflicting introductions with that wording. If three meetings is a firm weekly ceiling, the course total or calendar targets need an explicit revised decision. Do not silently compress two course days into one meeting.

## Order, standards, load and candidates

The main dependencies hold: supporting questions precede later inquiries; source kinds precede biographies; leader study precedes elections; government precedes capitals; maps precede world-place comparisons; and deliberation precedes the action.

No unit exceeds 25 days, so no mid-unit assessment is required. All incoming grade 1 prerequisites were used in kindergarten, so retrieval, rather than a separate dormant-skill readiness day, follows the current rule.

| Unit | Total days | Teaching days | Load judgment | Candidate disposition |
|---|---:|---:|---|---|
| 1 | 10 | 8 | Reasonable for questions, rules and roles. | Families retained within day 3. |
| 2 | 9 | 7 | Reasonable introduction, provided the calendar continues afterward. | Everyday life then and now retained within day 16. |
| 3 | 12 | 10 | Seven content days plus three writing days are justified. | Honesty/courage retained as review within days 22 and 23. |
| 4 | 10 | 8 | Four days on voting and four on government/application are plausible. | Shared services and payment retained within day 36. |
| 5 | 12 | 10 | Appropriate allowance for representations, directions, locations and map construction. | Community/state/country locations retained within day 50. |
| 6 | 13 | 11 | Dense, especially the four symbol/phrase/song teaching days; preserve its allocation. | Community diversity retained within day 60. |
| 7 | 12 | 10 | Three citizenship days and seven problem/action days form a coherent arc. | Local helper case retained within day 71. |
| 8 | 13 | 11 | Two earning, two buying, three choosing, three saving and one synthesis day are defensible. | Specialization retained within day 82. |

Every candidate has a disposition and an existing day location. “No added day” means integration within that lesson, not that the addition takes no minutes. I found no defensible basis for declaring a unit substantially overallocated.

The three lettered parts are explicitly carried:

| Code | Teaching placement |
|---|---|
| `MA.1.T3.2a` | Days 62 and 63 |
| `MA.1.T3.2b` | Day 64 |
| `MA.1.T3.2c` | Day 65 |

The remaining owned content and skill codes have teaching placements. Finding 1 distinguishes those placements from complete assessment coverage. The recorded economics exclusions have grade 2 destinations and should remain.

**Source map:** Not applicable. This course adopts no base text, consistent with `BASE-TEXTS.md`.

## Calendar and same-year leans

The course-level check dates match the specific grade 1 targets: day 42 on school day 68, week 14; days 94 and 95 on school days 152 and 154, week 31. Their response days follow, and the unit and course response allocations are counted separately once.

| Lean | Other subject’s calendar placement | Social studies use | Judgment |
|---|---|---|---|
| `RI.1.6` | ELA unit 1, weeks 1 to 7 | Day 14, week 5 | Overlapping unit; retain photographs, objects and teacher reading rather than assuming completion. |
| `RI.1.3` | ELA unit 2, weeks 7 to 15 | Leader comparison, day 26, week 9 | Overlapping unit; day 26’s teacher comparison chart supplies the bridge. |
| `W.1.1` | ELA unit 4, weeks 24 to 32 | Days 27 to 29, weeks 9 and 10 | Later in ELA; explicit shared writing, frames and dictation carry the bridge. |
| `1.MD.C.4` | Math unit 1, weeks 1 to 4 | Day 34, week 11 | Available first. |
| `1.NBT.B.3` | Math unit 4, weeks 14 to 19 | Day 84, week 28 | Available first. |
| `1.OA.A.1` | Begun in math unit 2; completed in unit 6, weeks 23 to 26 | Day 90, week 30 | Available first. |
| `1-ESS1-2` | Science unit 8, weeks 27 and 28, with earlier observations | Calendar begins in unit 2 | The stated bridge avoids requiring daylight analysis early. |

A subject’s unit interval establishes an availability window, not the precise day a skill is mastered. The two overlapping ELA leans remain protected by their bridges.

## Lens checklist: scope and sequence

| Lens line | Result |
|---|---|
| A compelling question requires the unit’s sources and permits defensible answers | **Missed in part:** unit 4 needs the comparison in finding 3. Other questions have plausible evidence paths. |
| History follows time order or explains its departure | **Missed locally:** unit 3’s claimed order needs the dated-episode repair in finding 2. The thematic course order is explained. |
| A contested event carries more than one telling | **Not yet judgeable at source-set level:** the sequence carries multiple community views, but complete historical source selections do not exist here. Finding 2 addresses a known current evidence conflict. |
| Writing from sources recurs and grows | **Met:** spoken conclusions in units 1 and 2, taught writing in unit 3, repeated closings afterward, explicit evidence work in unit 6 and the final check. |

## Stale notes and earlier findings

The current frame still calls the kindergarten retrieval a readiness check. The sequence already identifies the exact replacement; apply that recorded correction and close its lead item. This is an acknowledged carry-forward, not an additional numbered finding.

The older grade 1 sourcing, flag/eagle, group-role handoff, flyer-price and final-response findings are repaired in the present files. Do not reopen them. The current FOUNDATION replaces the earlier outside-human sensitivity-reader requirement with the recorded agent-read arrangement.

## What is right and should remain

- Eight coherent units with explicit reasons for their order.
- Direct teaching before sustained application.
- Repeated spoken and written conclusions with a clear writing bridge.
- Printed sources and tasks, teacher read-alouds, and dictation.
- Present-day Native governments alongside historical content.
- No compelled disclosure of family background, finances or citizenship.
- A student-chosen action that includes investigation, multiple views, enactment and reflection.
- Explicit assessment response time.

## Settled by the expert

These are recommendations for the caller to apply; no files were changed.

| Choice | Reason | Files affected |
|---|---|---|
| Preserve all eight unit allocations. | No demonstrated load imbalance warrants resizing. | Scope and sequence; days CSV |
| Use observations across final teaching lessons to complete assessment coverage. | Fits the existing K-2 assessment model without adding days. | Scope and sequence; days CSV; subsequent unit plans |
| Use Dolores Huerta for the farmworker leadership case, before Mankiller’s later case. | Preserves the content while responding to current evidence and clarifying chronology. | Sequence, frame, progression example notes |
| Distinguish an election from an issue vote; compare voting with agreement. | Repairs terminology and supports the existing compelling question. | Sequence; frame |
| Retain the W.1.1 bridge. | Social studies teaches the needed writing before ELA’s later unit. | Existing sequence and days CSV |
| Apply the writer’s retrieval-wording correction. | Matches the current readiness rule. | Frame |

## For Cory

- **Audience/time:** Decide whether the course may require four 30-minute meetings in weeks 11, 21 and 31. The current calendar requires them; the stated three-meeting ceiling does not accommodate 96 meetings before week 32.

## What I could not judge

- Finished assessment items, scoring criteria and samples.
- Actual lesson duration or the feasibility of all added observation prompts.
- Final source difficulty, reproduction rights and completeness of competing historical accounts.
- The later unit-level comparison against all three check states.
- A successful repository-wide plan or stale-note check.

## Outside sources and source-list additions

- [Massachusetts 2018 History and Social Science Framework](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf): grade 1 content, clarifications and shared economics topic.
- [NCSS C3 Framework, revised 2017 PDF](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf): inquiry and owned K-2 indicators.
- [California History-Social Science Content Standards](https://www.cde.ca.gov/BE/ST/SS/documents/histsocscistnd.pdf): checked the retained California candidates and the corrected K.1.2 attribution.
- [Dolores Huerta’s March 18, 2026 statement](https://medium.com/@dolores_huerta/march-18-2026-e74c20430555?postPublishedType=initial): primary testimony relevant to the exemplar choice.
- [UFW Foundation’s March 17, 2026 statement](https://ufwfoundation.org/statement-from-the-ufw-foundation/): the organization’s response to the allegations.
- [National Park Service, “A New Era of Farmworker Organizing”](https://www.nps.gov/articles/000/new-era-of-farm-worker-organizing.htm): Huerta’s organizing contribution and the historical setting.

**For the source list:** Add the last three sources as reviewer references. Their use here establishes no permission to reproduce their text or images.

**Verdict:** Revise before unit planning. **Finding count:** 4. **Report path:** `docs/reviews/sequence-social-studies-grade-1-2026-11-14.md`, supplied here only.


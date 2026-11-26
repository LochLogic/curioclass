# Second-model frame read: Theater, grades 3 to 5

**Course:** `theater-grades-3-to-5`  
**Date:** 2026-11-25  
**Mode:** Read only. No files changed.

## Verdict

**Requires changes before scope and sequence writing.** The frame has a sound annual structure: all 24 selected progression skills and 72 owned standards are placed once, in their correct years, and the full-path calendar works. The main risk is that writers could follow its assessment instructions exactly while collecting incomplete evidence or using response time for first-time assessment.

**Findings: 6**, most serious first.

This differs from the “sound and buildable” verdict in `docs/reviews/frame-theater-grades-k-to-12-2026-11-25.md`. Placement and day arithmetic hold, but the assessment contracts below need substantive repair.

## What was read and checked

- The complete [target frame](/S:/CurioClass/docs/courses/theater-grades-3-to-5/frame.md), its course selector, `frames.csv` entry and calendar rows.
- All 24 selected progression rows, their standards, words-file actions, prerequisites and outgoing links.
- The neighboring theater frames’ seams, models and relevant grade 2 and grade 6 teaching.
- The relevant grade 3, 4 and 5 ELA Units tables.
- `frame-read.md`, the after-core provisions of `frame-write.md`, `EXPERT.md`, the arts lens, arts adoption bar, arts `STANDARD.md` and `APPROACH.md`.
- Relevant foundation, shared approach, production-path, calendar, decision, source and earlier arts review material.
- The outside sources linked below.

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check theater-grades-3-to-5` | One failure: the frame-stage course lacks the lesson-plan data this command requires; review continued |
| `python -X utf8 scripts/frame.py check theater-grades-3-to-5` | Passed: 0 failures |
| `python -X utf8 scripts/stale.py check` | Passed: 121 files, 0 failures |
| Independent skill count | 24 selected skills, each placed exactly once |
| Independent standards count | 72 ids, each placed exactly once; 24 per year |
| Independent day count | Each year: 60 unit days, 2 course check days and 2 respond days, totaling 64 |

The gate wrapper was not run because it writes output and baselines, which this read-only assignment prohibits.

## Findings

### 1. Several evidence lines permit incomplete standards coverage

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, incomplete evidence contracts also appear in the earlier theater K to 2 second-model read  
**Confidence:** Firm

**Location:** Units 3, 10, 11 and 12, “What students learn” and “End-of-unit evidence.”

The frame promises an assessment for every owned action, but these instructions leave parts optional or substitute a different action. The distinctions were checked against the [official theater standards](https://www.nationalartsstandards.org/sites/default/files/2021-11/Theatre%20at%20a%20Glance.pdf), particularly PDF pages 4, 7 to 10.

| Unit and id | Problem | Exact fix |
|---|---|---|
| 3, `TH:Cn11.1.3a` | The two-ties card permits omission of either a social issue or another subject. | Require three labeled connections: community, social issue and another subject. Keep them on one card. |
| 3, `TH:Re9.1.3b` | The comparison can use Denslow’s book illustrations and only one theatrical work. | Require comparison of Holder’s theatrical design and a class production. Keep Denslow as background. |
| 10, `TH:Re8.1.5c` | The scored card accepts stance, movement, breath **or** pitch. | Give the card four brief fields covering posture, gesture, breathing and vocal intonation. |
| 11, `TH:Cn10.1.5a` | Explaining how a theater linked other people does not establish the learner’s connection. | Score the existing two-ties card: explain the connection for the learner or an explicitly offered invented participant. |
| 11, `TH:Cn11.1.5a` | The evidence accepts a scene about any one issue category, without requiring investigation of the studied work. | Add historical, global and social context fields to the existing fact-card investigation. Score that kept sheet. |
| 12, `TH:Pr4.1.5a` | Acting a hidden thought does not require the student to describe it or its accompanying emotion. | Score the existing script annotation explaining the thought, emotion and resulting line or action. |
| 12, `TH:Cn11.2.5b` | The script evidence checks two terms but no theatrical convention. | Require one term and one convention, each explained through its identified historical source. |

**Why it matters:** A teacher could mark these ids met without collecting their complete evidence.

Unit 11 also assigns **three written items**, contradicting the course’s maximum of two. Moving `TH:Cn10.1.5a` to the kept two-ties card, as specified above, resolves that contradiction without adding an assessment day.

These are evidence repairs within existing ownership, not proposals to move standards.

### 2. The once-a-week path collects new assessment evidence during response

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, the same timing problem appears in the theater K to 2 read and was addressed in `prework-arts-fixes-2026-11-20.md`  
**Confidence:** Firm on the contradiction; judgment call on the replacement allocation

**Location:** “The once-a-week path,” especially the respond session’s first 15 minutes; four-session units 4 and 12.

**Problem:** Written assessment happens at the beginning of the respond session. The arts approach requires marks to be available before that session, because those marks determine the response. Four sessions also cannot retain separate demonstration, rehearsal with critique and revision, showing check, written check and subsequent response.

**Why it matters:** Checking consumes the promised response time, and the teacher cannot prepare response groups from evidence not yet collected.

**Exact fix:**

1. Remove first-time written assessment from respond sessions.
2. Retain separate showing and written check sessions, followed by response.
3. Use this 32-session allocation:

| Year | Unit session counts, in order | Mid-year check week | Year-end check week |
|---|---|---:|---:|
| 3 | 8, 8, 7, 5 | 17 | 26 |
| 4 | 8, 8, 7, 5 | 17 | 26 |
| 5 | 8, 9, 6, 5 | 18 | 26 |

Each year contains 28 unit sessions and four course check/respond sessions. These proposed check weeks avoid current core check weeks.

For each five-session story unit, specify:

- Session 1: study the works and demonstrate the technique.
- Session 2: rehearse, critique and revise.
- Session 3: showing check.
- Session 4: written check.
- Session 5: response based on completed marks.

On this path, use the showing check as the consented family showing, with an in-class equivalent. Remove the promise of an additional separate family performance after response. Preserve the existing full-path schedule.

### 3. Course check timetables omit preparation for their fresh scenes

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, missing preparation time also appears in the media arts grades 3 to 5 second-model read  
**Confidence:** Firm on the omission; likely on the proposed timing

**Location:** Course-level checks, lines 298 to 307.

**Problem:** The checks require new scenarios, group questions, assigned jobs, rehearsal, hot-seat questions or self-review. Their common timetable budgets setup, warm-up, performances and closing, leaving only four minutes unspecified. It assigns no preparation window for those required tasks.

**Why it matters:** A writer following the timetable must rush or omit the work being assessed, or introduce the supposedly fresh task beforehand.

**Exact fix:** Replace the common timetable with:

| Activity | Minutes |
|---|---:|
| Setup | 3 |
| Warm-up | 3 |
| Read the new card, plan and rehearse in groups | 8 |
| Complete the required jobs, question or reflection record | 4 |
| Six group slots, including transitions | 18 |
| Close | 4 |
| **Total** | **40** |

Limit each performance to two minutes within its three-minute slot. Audience cards are completed while watching an assigned group. State where each check’s particular preparation artifact is produced, rather than relying on an unspecified rehearsal.

The neighboring grades 6 to 8 frame already demonstrates the useful distinction between fresh-task preparation and performance time.

### 4. Unit 12’s performance choice conflicts with its Zuni study restriction

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** Firm

**Location:** Unit 12, works, showing and sensitive-topic cells.

**Problem:** The showing allows each group to make a play from “one of the three tellings,” including *The Poor Turkey Girl*. The sensitive-topic instruction restricts that telling to reading and comparison and prohibits acting as a Zuni character.

**Why it matters:** The main task gives a busy writer permission that the teacher note withdraws.

**Exact fix:** Replace the showing instruction with:

> Each group makes its short play from the Curio Class retelling of Perrault or Ye Xian. The Poor Turkey Girl, if the required community-source check permits its use, is studied for comparison only and is not a performance source.

Keep the existing source-check condition and replacement requirement. Apply the same restriction to script choices and family-showing instructions.

This resolves the frame’s internal contradiction without deciding whether the Zuni telling is suitable.

### 5. Living guidance still describes completed work as owed

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, these stale arts guidance problems were identified in earlier prework and theater reads  
**Confidence:** Firm

**Locations and exact fixes:**

| Location | Problem | Exact replacement or action |
|---|---|---|
| Target frame, Days and For the lead item 3 | Requests a source read that this review has now completed. | State: “The 2016 theater opportunity-to-learn document was checked on 2026-11-25. It addresses grades 6 to 12 and supplies no elementary weekly-time recommendation. This course provides 80 minutes weekly, or 40 on the short path.” Remove the completed request. |
| Arts `STANDARD.md` 3.4, theater row | Broadly says the association has no figure. | Replace with: “No K to 5 weekly-time recommendation verified in the 2016 opportunity-to-learn document, which addresses grades 6 to 12.” |
| `ADOPTION-BAR-SUBJECTS.md`, introductory approach statement | Says no subject approach exists. | Replace with: “Layer 3 requires a subject approach before its scope and sequence; current states are recorded below.” |
| Same file, arts owed row | Still owes L83 and the high school music id load. | Record L83 completed 2026-11-21 and the 63 music strand ids loaded; remove both owed clauses. |

The [association’s document](https://schooltheatre.org/wp-content/uploads/2022/02/Opportunity-to-Learn-Standards-EdTA_2022.pdf), PDF page 5, explicitly identifies its grade range. The repository marks L83 done and contains the loaded music ids and progression rows.

**Why it matters:** These notes send later workers back through completed work and obscure what remains unresolved. The stale-note script does not catch all such statements.

Do not rewrite the dated review reports.

### 6. Two count statements disagree with the frame’s contents

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes for the film count, identified in the combined theater read; new for the incoming-row count  
**Confidence:** Firm

**Locations and exact fixes:**

| Location | Problem | Exact fix |
|---|---|---|
| Base text bullet, around line 63 | Says “two silent films” but names only *The Gold Rush*. | Change to “one silent film.” |
| Seams introduction, line 210 | Says grade 2 hands on eight rows. There are seven distinct rows, with `th-g2-notice` feeding two successors. | Replace with: “Theater, grades K to 2 hands on seven grade 2 rows through eight handoffs.” |

**Why it matters:** These are avoidable inconsistencies in the source list and prerequisite inventory.

## Lens checklist at frame level

| Lens check | Result |
|---|---|
| Grade ids in the correct band year | Met |
| All four artistic processes each year | Met |
| Technique grows across units and years | Met |
| Discipline words support making and response | Met as a planning provision |
| Student choice and a showing in every unit | Met |
| Critique followed by revision | Met on the full path; shorter-path timing needs finding 2 |
| Works span cultures, periods and living makers | Met in the planned selections; individual source checks remain |
| Assessment, self-assessment and kept growth evidence | Partly met, findings 1 to 3 |
| Ordinary-room time, equipment and safe use | Planned explicitly; check timing needs finding 3 |
| Performing happens with people in the room | Met |
| Participation without performing alone | Met as a provision |
| Software does not judge creative work | Met |
| Theater retains its own techniques and purposes | Met |
| Dance/PE and music/fractions boundaries | Not applicable |
| Detailed unit/day execution | Not applicable until those layers exist |

## Calendar, load and seams

The full-path calendar agrees with the frame:

| Year | Unit days | Course check weeks | Total days |
|---|---|---|---:|
| 3 | 16, 16, 18, 10 | 17 and 27 | 64 |
| 4 | 16, 16, 16, 12 | 17 and 26 | 64 |
| 5 | 16, 18, 16, 10 | 18 and 27 | 64 |

No course check falls in a current core check week. Other after-core checks share five of these six check slots; the frame correctly assigns that coordination to the lead’s calendar pass.

The longer design units and shorter concluding story units have defensible reasons. The 14 carried models and grade 6 handoffs are accounted for. The ELA placements support the three named progression leans; earlier opinion-writing uses have explicit sentence-frame support.

One incoming seam needs to follow the existing K to 2 finding: replace unit 2’s retrieval of a generic “decision moment” with recognition of a **performer’s artistic choice**, such as voice or movement. Character decisions within the plot are a different action.

There is no base text, so base-lesson mapping is not applicable.

## Settled by the expert

| Choice | Reason | Files affected |
|---|---|---|
| Preserve the 12-unit sequence and full 64-session years | Ownership, order and annual load hold | Target frame |
| Expand the specified existing cards and guides | Collects complete evidence without moving ownership | Target frame |
| Move unit 11’s personal-connection evidence to its kept card | Restores the connection and retains the two-written-item limit | Target frame |
| Use the revised 32-session allocation | Separates assessment from response while retaining every unit | Target frame |
| Budget fresh-task preparation explicitly | Makes course checks runnable within 40 minutes | Target frame |
| Restrict the Zuni telling to conditional comparison study | Makes the main task agree with its teacher note | Target frame |
| Treat respond sessions separately from course check days under the stagger rule | The written rule names course-level check days | Target frame’s For the lead item 2 |
| Retain the factual statement that Ngũgĩ was imprisoned during 1978 | That statement is true; the detention began in late 1977 | No required correction |

The detention chronology was checked against [James Currey’s account published by the University of Leeds](https://lucas.leeds.ac.uk/article/publishing-ngugi-james-currey/). The earlier review’s suggested clarification is useful, but the current “held … in 1978” wording is not itself a factual error.

## What is right and should not be touched

Preserve the clear annual ownership, recurring four-unit structure, explicit technique progression, substantial practical theater work, paper path, setup and cleanup allowances, portfolios, invented personal-tie options and specific cultural sensitivity instructions.

## What could not be judged

The future lesson materials, complete item-level rights checks, community permission for the Zuni telling and actual classroom execution cannot be certified from this frame. Its movement and voice safety rules remain explicitly **from memory**, pending the designated safety read.

No curriculum finding here relies on unverified model memory. Prior-session memory was used only for review workflow and reporting conventions.

The Indiana University archive returned 403 and was not retried by another route; the accessible Leeds account supplied the chronology check.

## For Cory

- **Money:** Decide the proposed optional ceiling of **$40 per class per year**. The instructional repairs above require no additional purchase or outside person.

## Sources and source-list follow-up

- [National Core Arts Standards: Theatre at a Glance](https://www.nationalartsstandards.org/sites/default/files/2021-11/Theatre%20at%20a%20Glance.pdf): checked the disputed standard actions against the original.
- [2016 Opportunity-to-Learn Standards for Theatre Education](https://schooltheatre.org/wp-content/uploads/2022/02/Opportunity-to-Learn-Standards-EdTA_2022.pdf): verified its grades 6 to 12 scope and the absence of an elementary weekly-time figure in this document.
- [Publishing Ngũgĩ, University of Leeds](https://lucas.leeds.ac.uk/article/publishing-ngugi-james-currey/): checked the detention chronology.

Record these exact links and the theater time document’s limited grade range in the source list. Keep the standards wording paraphrased.


# Second-model cold read: Career Exploration, grades 6 to 8

Date: 2026-11-25  
Course: `career-exploration-grades-6-to-8`  
Subject: `cte`  
Read-only review. No files changed.

## Verdict

The frame has a sound course structure: all 85 owned rows are placed exactly once, all 106 distinct standard codes match their units, and the handoffs are reciprocal. It needs a fix pass before the scope and sequence copies its assessment and pacing rules: choosing one portfolio piece can bypass required practice evidence, the 64-session path does not preserve its promised days, and practice 5 is claimed beyond what paper sorting teaches. Preserve the seven-unit structure, private plan and varied routes while fixing those three points first.

## What was read

- `docs/pipeline/briefs/frame-read.md`, the relevant requirements in `frame-write.md`, `docs/agents/EXPERT.md`, FOUNDATION, the shared APPROACH, production-path guidance and applicable BASELINE rules.
- ADOPTION-BAR-SUBJECTS, shared criteria and part 7.
- The career-education STANDARD, APPROACH and lens. The requested `docs/courses/cte/` and `docs/agents/lenses/cte.md` paths do not exist; `career-education` contains the subject guidance referenced by the frame.
- The [course frame](/S:/CurioClass/docs/courses/career-exploration-grades-6-to-8/frame.md), its `frames.csv` row, its `course-list.csv` selector (`grade:8`) and its calendar rows.
- The selected grade 8 progression rows, their standards and notes, `cte-edges.md`, and grade 10 handoff targets.
- Career-education decisions, the prework fix report, progression review and earlier frame review dated 2026-11-25. The frame was read before that earlier frame review.
- Relevant ELA grade 8 and Civics Units tables and calendar placements. Career Pathways and the cited computer science, library and SEL frames are not yet present.
- Outside sources linked below.

This is one year offered within a catalogue range, not three successive grade years. STANDARD section 3 explicitly settles one-year courses. A Year column and three annual assessment cycles are therefore not required.

## Checks

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check career-exploration-grades-6-to-8` | One failure: lesson-plan CSVs are absent. Continued the frame read as instructed. |
| `python -X utf8 scripts/frame.py check career-exploration-grades-6-to-8` | Passed, zero failures. |
| `python -X utf8 scripts/stale.py check` | Passed, 70 files, zero failures. |
| Independent row and code comparison | All 85 rows placed once; no missing or extra unit standard codes. |
| Independent seam comparison | Every named outgoing target exists, appears in Seams and names its grade 8 prerequisite. |
| Calendar arithmetic | Matches the frame: 92 unit days plus four course-level check and respond days. |

## Findings, most serious first

### 1. The chosen portfolio piece can omit required practice evidence

**Severity:** Serious. **Confidence:** Firm.  
**LAYER:** frame. **REPEAT:** new.

**Location:** “The plan and the portfolio,” “Scored evidence,” Units 2 to 7, and “For the lead,” item 6.

The course promises that every practice is judged through its task. But students submit one chosen field task piece per unit, while different tasks carry different practices. Choosing Unit 2’s data task can omit the stand’s teamwork evidence. Choosing Unit 3’s construction estimate can omit the production line’s persistence and time-management evidence. Choosing Unit 5’s accounting report can omit creativity. Unit 7’s chosen field task does not establish the required email and spoken-answer evidence.

Written feedback on every draft does not resolve the missing assessment evidence. This conflicts with APPROACH’s practice assessment rule and shared bar C8.

**Exact fix:** Retain one chosen full portfolio piece, but replace the scoring rule with:

> Each student submits one revised portfolio piece and the revised plan lines. A short required evidence attachment covers every newly taught practice not demonstrated by that chosen piece. Each attachment names its task, individual evidence and two or three look-fors. It receives feedback and revision before scoring. Portfolio choice never waives a required practice.

Name the attachments in each affected unit: team-role evidence, production-line timeline and second try, resilience response, design development, and the employer email and interview response. These can be excerpts and teacher records, without requiring another full performance.

### 2. The 64-session path cannot keep the days it promises

**Severity:** Serious. **Confidence:** Firm, arithmetic.  
**LAYER:** frame. **REPEAT:** yes, earlier frame review finding 2 and the progression pacing finding.

**Location:** “Days,” Shorter path, Units 2, 6 and 7, and “For the lead,” item 1.

The short allocations total 60 unit sessions, but violate the stated folding rule:

| Unit | Allocated | Minimum under its stated retained activities |
|---|---:|---:|
| 2 | 9 | 10: three explore days, four field task days, three closing days |
| 6 | 10 | 11: four explore days, four field task days, three closing days |
| 7 | 6 | 8: two packet days, two skill days, field task, plan, assessment and respond days |

These minima already assume substantial integration of the other learner-goal work. The short path therefore cannot be copied as a demonstrated schedule.

**Exact fix:** Replace the unsupported fold claim with a seven-row table naming each retained session and each folded activity’s receiving session. Give Units 2, 6 and 7 at least 10, 11 and 8 sessions respectively, then demonstrate how the remaining four units fit the remaining 31 sessions while preserving their owned learning and protected days. State that the 64-session schedule remains unresolved until that table works.

Do not use the earlier review’s proposed eight-session Unit 3 as the repair: three explore days, four field task days and three closing days already require ten.

### 3. Practice 5 is narrowed to paper data handling

**Severity:** Serious. **Confidence:** Firm.  
**LAYER:** progression and frame. **REPEAT:** new.

**Location:** Devices, paper-path claim, Unit 1 and `g8-prac-5-digital-data`.

The frame says no owned code needs technology and paper sorting meets every part. Practice 5 includes using digital tools, not merely understanding a sorted table. The state reproduction of the current practices explicitly includes digital operation, productivity, data use and privacy. The progression row also narrows this to a table that may be entirely on paper. [North Dakota’s current practices, practice 5](https://www.cte.nd.gov/sites/www/files/documents/CareerReady/New12ALL.pdf).

**Exact fix:** Replace “no owned code needs technology” and the full-equivalence claim with an explicit distinction between paper rehearsal and digital evidence. Recommended implementation: each student enters and sorts a small public or invented job table on an offline spreadsheet at a shared device, records a supported decision, and identifies one privacy precaution. Add that requirement to Unit 1 and the progression row.

If the course must remain runnable without any student device operation, identify this part as begun rather than fully taught and name where it is completed. That ownership or access decision belongs to Cory.

### 4. The study-habit task starts too late to run for two weeks

**Severity:** Moderate. **Confidence:** Firm, calendar arithmetic.  
**LAYER:** frame. **REPEAT:** yes, earlier frame review finding 6.

**Location:** Unit 5, “What students learn” and “Why this unit, here.”

The how-I-learn day follows Financial Services’ three days. That places it around course day 62, school day 104. Its report is due on the plan day, course day 66, school day 110. Six school days do not provide the progression row’s two-week practice.

**Exact fix:** Put the how-I-learn day second in Unit 5, course day 60, school day 100. Keep Financial Services’ two explore days on unit days 1 and 3, followed by its field task. Keep the plan day on course day 66. Replace “fits the unit’s three weeks” with “runs from unit day 2 to the plan day, ten school days later.”

### 5. Practice 2 “returns” before its first teaching

**Severity:** Moderate. **Confidence:** Firm.  
**LAYER:** frame. **REPEAT:** yes, earlier frame review finding 1.

**Location:** Units 5 and 6, Practices cells; Unit 7 ownership.

Practice 2 is first taught through the employer email and interview response in Unit 7. Units 5 and 6 nevertheless describe it as returning. A writer can reasonably infer that its criteria were already taught.

**Exact fix:** Keep its ownership in Unit 7. Change:

- Unit 5 to “8 introduced; 12 returns; communication practiced with task-specific support, practice 2’s criteria first taught in Unit 7.”
- Unit 6 to “4, 9 and 11 return; communication practiced with task-specific support, practice 2’s criteria first taught in Unit 7.”

Earlier writing and speaking can remain.

### 6. Unit 7’s unrestricted packet choice escapes the sensitive-topic safeguards

**Severity:** Moderate. **Confidence:** Firm.  
**LAYER:** frame. **REPEAT:** new.

**Location:** Packet days, Sensitive ground and Unit 7’s teacher notes.

Students may choose any of the other 58 sub-clusters and complete a field task from it. Those choices include the six sensitive sub-clusters. Yet the frame describes those fields as named only, and explicitly routes additional disclosure safeguards to Units 4 and 6. Unit 7 does not explain how the school’s leave-out choice, same-cluster swap and disclosure provisions apply to individual packets.

**Exact fix:** Add to Unit 7:

> Packet choices follow the school’s sensitive-sub-cluster choices. Offer a same-cluster alternative. Any packet touching a sensitive sub-cluster receives its required teacher note and sensitivity read before use; the disclosure steps accompany packets on the topics STANDARD section 6 names. Every packet task is an age-appropriate paper simulation, with no clinical, emergency-response, weapons or hazardous equipment activity.

Amend Sensitive ground to include these packets wherever they occur. Label their sub-cluster content as exploration, with no claim to completing Pathways’ owned standards.

### 7. A computer science prerequisite has no fallback

**Severity:** Moderate. **Confidence:** Firm.  
**LAYER:** frame. **REPEAT:** yes, earlier frame review finding 9 and frame-write lesson 32.

**Location:** Cross-subject, `g7-viz-choices`; Readiness and retrieval.

The frame treats this optional course’s chart work as assured prior learning and says a fallback is unnecessary. Students who did not take grade 7 computer science still need it.

**Exact fix:** Replace “Not needed” with:

> The field task sheet teaches the needed chart choice using one fair and one misleading chart of the same table, names the difference, and asks the student to repair the misleading version. No prior computer science course is required.

Use retrieval where students have the prior learning and this bridge where they do not. Add the bridge to the readiness bullet.

### 8. The “unseen” check examples are not reliably unfamiliar

**Severity:** Moderate. **Confidence:** Firm.  
**LAYER:** frame. **REPEAT:** yes, earlier frame review finding 8.

**Location:** Both Course-level checks, “What it checks.”

Check 1 selects Web and Cloud as a sub-cluster not studied at depth, although Unit 2 explicitly includes a web developer card. Check 2 can select a field a student just studied in their chosen packet. A fresh card can still work, but the stated unfamiliar-field rationale does not reliably hold.

**Exact fix:** For Check 1, use a new Network Systems and Cybersecurity job card with new figures. For Check 2, prepare Health Data and Administration and Early Childhood Development alternatives; assign the one outside the student’s packet study. State that all versions use new cards, figures and questions, and assess the same criteria.

### 9. Calendar checks skip the course’s range-grade rows

**Severity:** Moderate. **Confidence:** Firm.  
**LAYER:** process. **REPEAT:** yes, earlier frame review finding 5.

**Location:** `calendar.csv` grade cell; `scripts/frame.py`, `calendar_rows`, `check_weeks` and `clashes`.

The calendar records this course under `6-8`. The stagger checks accept individual grades K through 8, so they skip this course. Its current mid-year placement is clear by manual comparison, but a future clash could pass silently.

**Exact fix:** For a single-year course whose catalogue grade is a range, use its settled instructional placement for calendar checking. Here that is grade 8, matching `grade:8` and the frame. Preserve the catalogue range separately. Regenerate the calendar through its script, then check the course beside grade 8.

Do not repair this by pretending the course has three grade years.

### 10. The soil-and-seed safety citation does not support its stated purpose

**Severity:** Minor. **Confidence:** Firm.  
**LAYER:** frame. **REPEAT:** yes, earlier frame review finding 7.

**Location:** Safety read and Unit 4’s safety sentence.

The cited NSTA statement gives general school science safety guidance, not soil-and-seed handling instructions. A relevant school gardening source supplies more specific material-handling and dust controls. [NSTA statement](https://www.nsta.org/nstas-official-positions/safety-and-school-science-instruction), [University of Maryland Extension, FS-1077](https://dev.extension.umd.edu/resource/food-safety-your-school-gardens-classrooms-and-greenhouses-fs-1077).

**Exact fix:** Describe NSTA as general guidance and add FS-1077 for the optional seed tray. Extend Unit 4’s sentence to specify suitable commercial growing medium, adult preparation and moistening to limit dust, gloves, handwashing, no eating, and the paper alternative.

The writer’s statement that links were not opened “in this pass” is historical, not stale merely because a later reviewer opened them.

### 11. Week 32 remains an unresolved rule conflict

**Severity:** Minor. **Confidence:** Firm.  
**LAYER:** process. **REPEAT:** yes, earlier frame review finding 12.

**Location:** Course-level checks opening paragraph; “For the lead,” item 3; frame-write’s after-core check rule.

CALENDAR explicitly permits grade 6 to 8 year-end checks in finals week 32. The after-core brief broadly prohibits core target weeks. The frame discloses the conflict, but its opening claim that checks occupy weeks without core checks contradicts its own year-end placement.

**Exact fix:** Keep the proposed week 32 placement pending the lead’s rule reconciliation. Replace the opening sentence with:

> The mid-year check avoids grade 8 core check weeks. The year-end check uses week 32 under CALENDAR’s grade 6 to 8 finals-week rule.

The lead should amend frame-write in place to state that exception and record the decision. Do not remove three Unit 6 sessions to solve a wording conflict.

### 12. Several planning notes remain stale or contradictory

**Severity:** Minor. **Confidence:** Firm.  
**LAYER:** process. **REPEAT:** yes, earlier frame review findings 11 and 13.

**Locations and exact fixes:**

- **ADOPTION-BAR-SUBJECTS, career-education owed row:** Replace “five calls” still owed with “The five calls were answered 2026-11-21, Desk q-fix-career-1. Owed: the second state materials rubric.” Correct the career-education approval reference to `q-prework-open-2`.
- **Career-education APPROACH, day-kind table:** Replace the blanket Fluency classification for skill days with “Understanding on first teaching; Fluency on subsequent practice.” The frame already applies the shared rule correctly.
- **Progression `g8-cd2-2-decision-steps`:** Replace “which cluster to study next” with “which job the field task compares first, or which sub-cluster to choose for the self-directed study.” The frame fixes the cluster order and already proposes this repair.
- **Both course-level check cells:** Replace “assessed the day before” with “assessed two course days earlier, with a respond day between.”

These are living-document repairs. Earlier dated review reports remain unchanged.

## Lens checklist

“Met” means adequately specified at frame level, not verified in unwritten lessons.

| Frame-layer lens requirement | Result |
|---|---|
| Personal plan made and revised through the course | Met |
| Broad cluster coverage with meaningful depth | Met on the full path; shorter path unresolved |
| Applied field task in every unit, with data sources | Met |
| Each claimed practice has a task | Tasks named; assessment coverage missed, finding 1 |
| Employability taught directly in context | Partly met; findings 1, 3 and 5 |
| Real, dated figures and geographic limits | Met as a build requirement |
| Multiple routes without ranking students | Met |
| School additions and paper alternatives stated | Met, subject to the digital coverage correction |
| Bar part 7: demonstrations and portfolio | Present; compulsory evidence needs repair |
| Safety for the selected hands-on activities | Controls present; source specificity needs repair |

## What is right and should remain

- The opening unit establishes the plan and models before cluster work.
- The five cluster groups provide breadth without fourteen separate sets of closing days.
- Serving people sits late for defensible reasons, including the Civics budget prerequisite.
- Plans and inventories are private; family-work questions have invented, public-profile and trusted-adult alternatives.
- Feedback and revision precede scoring.
- Routes are compared without making one the default.
- Pathways does not require students to retain their earlier portfolio.
- No base text is claimed, so a base-text source map is not applicable.

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Keep the single-year shape without a Year column | Subject decisions explicitly settle one-year courses | Course frame |
| Keep portfolio choice and require missing-practice attachments | Preserves student judgment while securing evidence | Frame assessment rules |
| Start Unit 5’s habit practice on unit day 2 | Gives ten school days before the plan day | Unit 5 |
| Keep practice 2 ownership in Unit 7; correct earlier “returns” labels | Repairs sequence without moving ownership | Units 5 and 6 |
| Use paired unfamiliar check versions | Avoids overlap with packet choices | Course-level checks |
| Teach the chart bridge when prior computer science is absent | Optional courses cannot be assumed | Cross-subject |

## For Cory

- **Access and scope:** Approve brief student operation of a shared offline device for practice 5, or require honest partial coverage with a named later completion point. The present claim of full coverage without digital operation should not stand.
- **Short-path scope, only if necessary:** If an explicit 64-session schedule cannot preserve the owned learning and protected days, a change in breadth, task structure or dose needs your decision. The current numbers do not demonstrate that it fits.

## Relationship to the earlier read

Several findings repeat unresolved issues in the earlier frame report. I disagree with its conclusion that no issue is serious: missing required assessment evidence and a short path that drops protected work would lead a scope writer to build the wrong course.

I also disagree that all standards are substantively covered merely because their codes match. Practice 5 is a clear counterexample. Conversely, the general lawful-question prohibition already constrains the interview task; a more explicit disability reminder would be useful clarification, rather than a separate coverage failure.

## Sources and limits

- [Current career-ready practices, North Dakota reproduction](https://www.cte.nd.gov/sites/www/files/documents/CareerReady/New12ALL.pdf): checked practice 5’s digital requirement.
- [North Dakota career-ready rubric](https://www.cte.nd.gov/sites/www/files/documents/CareerReady/Entire_Career_Ready_Rubric_Document.pdf): consulted for performance evidence. This does not close the owed second-state instructional-materials rubric.
- [Advance CTE resource page](https://careertech.org/resource/career-ready-practices/): checked the current resource and publisher link. The linked final PDF was image-only in the available extraction; substantive wording was checked in the state reproduction.
- [BLS Handbook disclaimer](https://www.bls.gov/ooh/about/disclaimer.htm): checked national scope, typical entry requirements and limits on interpreting training information.
- [Occupational database content license](https://www.onetcenter.org/license_db.html): confirmed attribution, license-link and modification-notice requirements.
- [Talking Safety](https://www.cdc.gov/niosh/young-workers/talking-safety/): confirmed the free curriculum and its 45-minute lesson format.
- [Young workers’ safety page](https://www.osha.gov/young-workers): checked the frame’s named source.
- [NSTA safety statement](https://www.nsta.org/nstas-official-positions/safety-and-school-science-instruction) and [school gardening guidance](https://dev.extension.umd.edu/resource/food-safety-your-school-gardens-classrooms-and-greenhouses-fs-1077): checked finding 10.

The [2024 guidelines PDF](https://ncda.org/aws/NCDA/asset_manager/get_file/896607?ver=0) returned **403, browser check**. A separate publisher HTML source also returned 403. No alternate retrieval was attempted. Indicator-level conclusions therefore rely on the repository’s recorded standard interpretation and progression, not a fresh full reading of the publisher’s text.

The absent adjacent frames limit seam verification to progression contracts. Actual job cards, packet tasks, assessments and classroom timing cannot yet be judged. No substantive curriculum finding rests on unaided memory; prior memory was used only for review method.

## For the source list

Add the school gardening guidance as a source actually opened, with the relevant container-medium, material-handling, dust and handwashing sections. Record the guidelines URLs as “browser check, 403” rather than freshly read.


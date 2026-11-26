# Scope and sequence

social-and-emotional-learning-grades-6-to-8, Social and Emotional Learning, Grades 6 to 8. Draft, scope stage (2026-11-26; fix pass after the expert read the same day). Built from frame.md, data/progressions/sel.csv, docs/courses/sel/STANDARD.md and APPROACH.md, the lens docs/agents/lenses/sel.md and bar section 9. The day plan is data/plans/social-and-emotional-learning-grades-6-to-8/days.csv (192 rows).

## The band, the years and school days

- 64 sessions a year, 2 a week over 32 weeks, 30 minutes each; 192 sessions in all.
- Year 1 (course days 1 to 64, units 1 to 6) teaches the grade 6 rows; year 2 (days 65 to 128, units 7 to 12) the grade 7 rows; year 3 (days 129 to 192, units 13 to 18) the grade 8 rows, which own the CASEL codes and AASL.V.D.1, AASL.V.D.2 and AASL.III.D.2. Grade 6 and 7 rows begin their codes (~) at that grade's depth, so days 1 to 128 write every code `~ID`; AASL is named in notes only there.
- **school_day formula.** For year index i (0, 1, 2) and session s within the year (1 to 64): school_day = 160·i + ceil(2.5·s). The value is cumulative through the band, so frame.py sorts the three years in order (it splits years by 160-day spans); it equals frame.py's own default spread. Read within its year: day in year = school_day - 160·i, week = (day in year - 1) // 5 + 1.
- Each grade's year shape: four 11s, two 10s or 9s and two 8s, by the frame's Units table; the course-level checks are the end-of-unit Check of units 3, 6, 9, 12, 15 and 18.
- Each three-group unit runs 3 × (Understanding, Fluency, Application), then Check and Respond; each two-group unit 2 × (Understanding, Fluency, Fluency, Application), then Check and Respond. Units 3, 6, 9, 12, 15 and 18 end on their last Application day; the course-level Check on the next day is their end-of-unit assessment.
- Readiness: only course day 1 (the start-of-band check in the last ten minutes of session 1, rule 2). Every later row assumes the row one grade back, so each group's Understanding day opens with that row as retrieval, one item with a part per row; Fluency and Application openings retrieve earlier rows of the same year for spacing. The retrieves column names them.
- Every evidence point is a character's choice on an invented case. SA7 and SA9 pages are private and seen only for their steps; in grade 8 a skill is judged on its steps, never on willingness.

## Year 1: grade 6 (days 1 to 64)

### Unit 1. Finding my way

Days 1 to 10, weeks 1 to 5; Check day 9 (school day 23), Respond day 10. Groups: 1.1 SM5, SM3, SA7 (days 1 to 4); 1.2 SO7, RS8 (days 5 to 8).
- Arc: getting organized for a new school, then reading new settings and choosing the helper.
- Order: organizing first because the first weeks need it; the meter and helper choice come before health unit 2 (week 4) retrieves them.
- Readiness: day 1, assess readiness, on g5-rds-careful-thinking, g5-rel-ask-offer-help and g5-sm-set-goal, watched in the last ten minutes of session 1, after the hook and the modeling, and marked on the class sheet. Day 1 models its three sub-skills on one invented first week, one case in three parts, and quotes the goal steps card word for word (goal, steps, block and plan, check). A class without SEL 3 to 5 gets the grade 5 forms modeled in the first ten minutes of the group that first uses them (goal steps day 2, stop-think-choose and the meter day 5).
- Retrieval: g5-sm-plan-and-tidy (day 2), g5-sm-stay-on-task (day 3), g5-sa-i-can-try (day 4), g5-soc-read-situation and g5-rel-ask-offer-help (day 5).
- Evidence: SM3 and SA7 on day 4's class sheet; SM5 (the planner and the materials system, with the reason), SO7 and RS8 on the Check page and the watched ask rehearsal. SM3 carries AASL.V.D.1 at grade 6 depth (day 1).
- Candidate cells settled: the six-class planner page is a print check at the unit plan, no day cost.

### Unit 2. Who I am in a new place

Days 11 to 21, weeks 6 to 11; Check day 20 (school day 50), Respond day 21. Groups: 2.1 SA3, SA5; 2.2 SA1, SA2; 2.3 SA4, SA9.
- Arc: exact feeling words and the think-feel-do chain, then roles and strengths, then honesty and interests.
- Order: the feelings words come before unit 3's calm-down steps use them.
- Retrieval: grade 5 rows on each Understanding day (days 11, 14, 17).
- Evidence: SA1 and SA2 on day 16; SA9 private, steps only, day 19; SA3, SA5 and SA4 on the Check page and the honest-option rehearsal.
- Candidate cells settled: the close-word reading-level check and the home-language roles map stay as unit-plan checks inside days 11 and 14.

### Unit 3. Calm and careful

Days 22 to 29, weeks 11 to 15; no unit Check: the grade 6 mid-year check on day 30 is its end-of-unit assessment. Groups: 3.1 SM2, SM1; 3.2 RD5, RD6, SA8.
- Arc: the calm-down steps grow to five and a response is chosen, then five-step stop-think-choose, well-being and a practice change.
- Order: after health unit 3 (weeks 7 to 10), which used the four-step card; day 22 names that health unit.
- Leave-out bridge (if unit 2 left out): the feelings scale's one-step form on day 22.
- Evidence: RD6 on day 29; SM2, SM1, RD5 and SA8 on the mid-year check. SA8 carries AASL.V.D.2 at grade 6 depth (day 26).
- Candidate cells settled: the four-tool menu fit and "no student plays a mocker" kept inside days 23 and 24.

### Grade 6 mid-year check (days 30 and 31)

Day 30, school day 75, week 15; Respond day 31, school day 78, week 16. Unit 3's own items plus two written samples (RS8 from unit 1, SA5 from unit 2) and the watched calm-down rehearsal. Off every other grade 6 subject's mid-year check day.

### Unit 4. Friends and talk

Days 32 to 42, weeks 16 to 21; Check day 41 (school day 103), Respond day 42. Groups: 4.1 RS1, RS2, RS5; 4.2 SO1, SO4, SO3; 4.3 RS6, SO5.
- Arc: the talk turn card, friendship paths and the I-statement, then another's view and care, then refusal and thanks.
- Order: refusal follows health unit 4 (weeks 11 to 14); day 38 names that health unit.
- Leave-out bridges: day 32 models the five-step cards' one-step forms (if unit 3 left out) and the feelings scale's one-step form (if unit 2 left out), inside the same ten minutes.
- Evidence: RS2 and RS5 day 34; SO4 and SO3 day 37; SO5 day 40; RS1, SO1 and RS6 on the Check.
- Candidate cells settled: plain-text paper threads and the refusal-card wording check stay inside days 32 and 38.

### Unit 5. Rules, feeds and facts

Days 43 to 53, weeks 22 to 27; Check day 52 (school day 130), Respond day 53. Groups: 5.1 SO6, SO8, SO2; 5.2 RD1, RD2, SA6; 5.3 RD4, RD7.
- Arc: fair norms and app features, then questions and fact checks, then results and who a post reaches.
- Order: comes before math 6's data unit, so counts and fractions only.
- Leave-out bridges: the talk turn card (if unit 4 left out) and the five-step stop-think-choose (if unit 3 left out) on day 43.
- Evidence: SO6, SO8 and SO2 day 45; SA6 day 48; RD4 in the rehearsal; RD1, RD2 and RD7 on the Check.
- Candidate cells settled: an invented app with no real look, and a data page in counts only, inside days 43 and 46.

### Unit 6. Our class proposal

Days 54 to 62, weeks 27 to 31; the year-end check on day 63 is its end-of-unit assessment. Groups: 6.1 SM4, SM6, SM7; 6.2 RS4, RS7, RS3; 6.3 RD3, RS9.
- Arc: a goal, stepping forward and a class proposal; then teamwork and differences; then problems and upstanding.
- Order: after health units 7 and 8 (weeks 22 to 28).
- Leave-out bridges: day 54, the first Understanding day, for unit 3 and unit 4 inside the same ten minutes.
- Evidence: SM6 and SM7 day 56 (each student's own first step and written presentation choice with the reason); RS7 and RS3 day 59; the rest on the year-end check.
- Safety and supplies: inside the school day, the teacher present, about $5 of poster paper.
- Candidate cells settled: the proposal is scoped to three Application sessions, inside day 56.

### Grade 6 year-end check (days 63 and 64)

Day 63, school day 158, week 32 (finals); Respond day 64, school day 160. Unit 6's items plus RS6 (unit 4) and RD7 (unit 5) and the watched upstander rehearsal.

## Year 2: grade 7 (days 65 to 128)

Grade 7 runs each case from a second person's side.

### Unit 7. Seen from both sides

Days 65 to 75, weeks 1 to 6; Check day 74 (school day 25), Respond day 75. Groups: 7.1 SA1, SA2, SA9; 7.2 RS4, SO2; 7.3 RS2, RS3. Retrieval: grade 6 rows on days 65, 68, 71. Evidence: SA9 private (day 67); RS4 day 70; RS3 day 73; SA1, SA2, SO2 and RS2 on the Check. Candidate settled: feedback-custom source picked at the unit plan, inside day 71.

### Unit 8. Pressure and invitations

Days 76 to 85, weeks 6 to 11; Check day 84 (school day 50), Respond day 85. Groups: 8.1 RS6, SO7; 8.2 SO8, RD4, SM3. Day 76 names health unit 12. Leave-out bridge (unit 3 or 4) on day 76. Evidence: SM3 day 83 (AASL.V.D.1 at grade 7 depth); RS6, SO7, SO8 and RD4 on the Check. Candidates settled: a described meme with no image, and the code-word family activity checked against health's notes, inside days 76 and 80.

### Unit 9. Fair and checked

Days 86 to 93, weeks 11 to 15; the mid-year check on day 94 is its end-of-unit assessment. Groups: 9.1 SA6, SO1; 9.2 SO6, RD1, RD2. Leave-out bridge (unit 5) on day 86. Settled case on day 90: the Nineteenth Amendment. Evidence: SO1 day 89; the rest on the check. Candidates settled: a neutral-trait snap judgment and the settled-history read against its source, inside days 86 and 93.

### Grade 7 mid-year check (days 94 and 95)

Day 94, school day 75 of grade 7, week 15; Respond day 95, school day 78, week 16. Unit 9's items plus SA1 (unit 7) and RS6 (unit 8) and the watched say-back rehearsal.

### Unit 10. Inside and shown

Days 96 to 106, weeks 16 to 21; Check day 105 (school day 103), Respond day 106. Groups: 10.1 SA3, SA5; 10.2 SM1, SM2; 10.3 SA4, SA7, SA8. Leave-out bridge (unit 2 or 3) on day 96. Evidence: SM1 day 101; SA7 (private) and SA8 day 104; the rest on the Check. Candidates settled: SA8 as a practice change, and the cover-for-a-friend case written to differ from unit 14, inside day 102.

### Unit 11. Repair and support

Days 107 to 117, weeks 22 to 27; Check day 116 (school day 130), Respond day 117. Groups: 11.1 RS1, RS5, RS7; 11.2 SO4, SO3, RS8; 11.3 SO5, RS9. Leave-out bridge (unit 4 or 6) on day 107. The check-in question on day 110 (school day 115, week 23) comes before health unit 18 (weeks 25 to 27) retrieves it. Evidence: RS7 day 109 (guides rotate by card, each student guides once); SO4 and RS8 day 112; SO5 day 115. Candidates settled: the adult line checked against health, and the turned-down offer rehearsed with the teacher, inside days 110 and 111.

### Unit 12. A shared plan

Days 118 to 126, weeks 27 to 31; the year-end check on day 127 is its end-of-unit assessment. Groups: 12.1 SM4, SM5, SM6; 12.2 RD5, RD6, RD7; 12.3 SM7, RD3. Leave-out bridge (unit 5) on day 118. Evidence: SM5 and SM6 day 120; RD5 and RD6 day 123; RD3 day 126 (each student writes one view of the cause and the solution they would test before the class chooses). Safety: inside the school day and grounds, the teacher present, about $5. Candidates settled: the teacher arranges the one asking session and the scope, inside day 126.

### Grade 7 year-end check (days 127 and 128)

Day 127, school day 158 of grade 7, week 32 (finals); Respond day 128, school day 160. Unit 12's items plus SA4 (unit 10) and RS5 (unit 11) and the watched ask-and-change rehearsal.

## Year 3: grade 8 (days 129 to 192), the owner year

Every option costs something, and a choice is judged afterward.

### Unit 13. Deciding under pressure

Days 129 to 138, weeks 1 to 5; Check day 137 (school day 23), Respond day 138. Groups: 13.1 RD5, SA5, RD4; 13.2 RD1, RD2, RD7. Leave-out bridge (unit 2 or 5) on day 129. Supplies: six two-minute sand timers, about $4 once. Evidence: RD1 and RD7 day 136; RD5 (the timed run and its one-line written look-back), SA5, RD4 (costs weighed, the choice, the choice judged, one prompt each) and RD2 on the Check. Candidates settled: a rumor about an invented school event, and teacher-alone pairs, inside days 130 and 133.

### Unit 14. Values that cost

Days 139 to 149, weeks 6 to 11; Check day 148 (school day 50), Respond day 149. Groups: 14.1 SA1, SA2, SA9; 14.2 SA4, SA6, SO7; 14.3 RS6, SA7. Day 145 names health unit 25. Leave-out bridge (unit 4) on day 139. Evidence: SA1 day 141; SO7 day 144; SA9 and SA7 private (days 141, 147); SA4, SA2, SA6 and RS6 on the Check. Candidates settled: neutral values cards, a dare with no body risk, inside days 139 and 142.

### Unit 15. Heavy weeks

Days 150 to 158, weeks 11 to 15; the mid-year check on day 159 is its end-of-unit assessment. Groups: 15.1 SA3, SM2; 15.2 SM1, SA8; 15.3 SM3, SM5. Leave-out bridge (unit 2 or 3) on day 150. SM3 carries AASL.V.D.1, SA8 AASL.V.D.2. Evidence (owner split): SM1's written cost and recovery on day 155's class sheet; SM5 on day 158's (the cut week, the cost of each move and the folder or checklist system); SA3, SM2, SM3 and SA8 on the mid-year check, where SM1's watched high-stakes rehearsal finishes. Candidate settled: sleep and screen time stay a character's, inside day 150.

### Grade 8 mid-year check (days 159 and 160)

Day 159, school day 78 of grade 8, week 16; Respond day 160, school day 80, week 16, off the grade 8 science check on day 75. Unit 15's items plus RD4 (unit 13) and SA4 (unit 14) and the watched high-stakes calm-down rehearsal. Six items, no two-part merge: SA3, SM2, SM3 (AASL.V.D.1 look-for), SA8 (AASL.V.D.2 look-for) and the two samples; SM5 and SM1's written part are judged on days 158 and 155.

### Unit 16. Other views, fair norms

Days 161 to 171, weeks 17 to 22; Check day 170 (school day 105), Respond day 171. Groups: 16.1 SO1, SO4, SO3; 16.2 SO6, SO8; 16.3 RS3, SO2. Leave-out bridge (unit 2 or 5) on day 161. Settled case on day 164: the ADA (signed July 26, 1990), from ADA.gov and the National Archives' ADA research page; Section 504 only if the unit plan first opens a federal page for it. Day 167 uses the Deaf-Hearing Communication Centre's communication tips; no student simulates hearing loss. Evidence: SO4 and SO3 day 163; SO8 day 166; SO1, SO6, RS3 and SO2 on the Check. Candidates settled: a school-issue view only, and the settled-history read against its source, inside days 161 and 164.

### Unit 17. Hard talks and fair deals

Days 172 to 181, weeks 22 to 27; Check day 180 (school day 130), Respond day 181. Groups: 17.1 RS1, RS2, SO5; 17.2 RS5, RS8. Leave-out bridge (unit 4) on day 172. Evidence: RS2 and SO5 day 175; RS1, RS5 and RS8 on the Check, whose RS8 item asks both halves (the right helper for a costly ask, and an offer of help that takes real time, sized on the meter, with its cost); day 179 plans the offer. Candidate settled: a worrying secret sized big and routed to an adult, inside day 176.

### Unit 18. Improving our school

Days 182 to 190, weeks 27 to 31; the year-end check on day 191 is its end-of-unit assessment. Groups: 18.1 SM4, SM6, SM7; 18.2 RS4, RS7, RD3; 18.3 RS9, RD6. Leave-out bridge (unit 6) on day 182. RS4 carries AASL.III.D.2. Evidence: SM4, SM6 and SM7 day 184 (each student writes a first step with its cost and answers one objection card before the class picks); RS7 and RD3 day 187 (day 186's trio rotation carried onto the real decisions, every student leading once, and each student's written judgment of the solution). Safety: inside the school day and grounds, an adult present; about $10 across the unit. Candidates settled: the improvement scoped to its sessions, and a described video, inside days 184 and 188.

### Grade 8 year-end check (days 191 and 192)

Day 191, school day 158 of grade 8, week 32 (finals); Respond day 192, school day 160. Unit 18's items plus SO6 (unit 16) and RS5 (unit 17) and the watched upstander rehearsal.

## Course-level checks

| Check | Day | School day in year | Week | Respond |
|---|---|---|---|---|
| Grade 6 mid-year | 30 | 75 | 15 | day 31, school day 78, week 16 |
| Grade 6 year-end | 63 | 158 | 32 | day 64, 160, week 32 |
| Grade 7 mid-year | 94 | 75 | 15 | day 95, 78, week 16 |
| Grade 7 year-end | 127 | 158 | 32 | day 128, 160, week 32 |
| Grade 8 mid-year | 159 | 78 | 16 | day 160, 80, week 16 |
| Grade 8 year-end | 191 | 158 | 32 | day 192, 160, week 32 |

Each check is its unit's own end-of-unit assessment on new cases, with at most two written samples from earlier units. Its sheet is kept only until the respond session.

### Owned (grade 8) codes not sampled on a course-level check

A course-level check samples at most two earlier skills, so most owned codes are assessed at their unit's end instead.

| Codes | Where they are assessed | Why not on a course-level check |
|---|---|---|
| RD1, RD7 | day 136 class sheet | the sample cap |
| RD2, RD5, SA5 | unit 13 Check, day 137 | the sample cap |
| SA1, SO7 | days 141, 144 | the sample cap |
| SA2, SA6, RS6 | unit 14 Check, day 148 | the sample cap |
| SA7, SA9 | private pages, steps only (days 147, 141) | private, never collected |
| SM1 (written cost and recovery), SM5 | days 155, 158 class sheets | owner split inside the six-item cap; SM1's watched rehearsal is on the mid-year check |
| SO1, SO2, SO3, SO4, SO8, RS3 | days 163, 166, unit 16 Check day 170 | the sample cap |
| RS1, RS2, RS8, SO5 | days 175, unit 17 Check day 180 | the sample cap |
| SM4, SM6, SM7, RS7, RD3 | days 184, 187 | unit 18 class-sheet points (frame) |

Grade 8 checks sample SA3, SM2, SM3 (with AASL.V.D.1), SA8 (with AASL.V.D.2), SM1 (the watched rehearsal), RD4, SA4, RS9, RS4 (with AASL.III.D.2), RD6, SO6 and RS5.

## Shorter path

- **Once a week** (frame): a three-group unit runs in 5 sessions (Understanding and Fluency together per group, the Applications together, Check and Respond together); a two-group unit in 6 sessions (U+F and the second Fluency per group, the Application, Check and Respond). The shared Check and Respond session runs 5 minutes opening, 12 minutes page and rehearsals, 8 minutes reteach, 5 minutes close. No assessed step is cut. Once a week, the Application session marks the unit's watched rehearsal; the codes judged on Application days in the full path move to the shared Check page as one written part each (the page then holds the unit's own items, up to six). In units 6, 12 and 18, once a week, the class carries out one part of its proposal or improvement, chosen at the unit plan.
- **A year 10 school days short:** merge each two-group unit's two Fluency days per group into one session, each skill rehearsed in its own block (about 10 minutes of paired rehearsal on fewer cards), the retrieval opening kept; the merged day carries the second day's number (days 2 and 3, 6 and 7, 23 and 24, 27 and 28, 77 and 78, 81 and 82, 87 and 88, 91 and 92, 130 and 131, 134 and 135, 173 and 174, 177 and 178); 4 a year, 12 in all, 180 of 192 sessions. Every assessed skill keeps a rehearsal before its evidence point; no assessed or owned part is cut.
- **A shorter 20 to 25 minute period:** 3-minute opening and close, one fewer rehearsal card; nothing assessed is cut.
- **A left-out unit:** a later unit that uses its card models the card's one-step form in the first ten minutes of its first Understanding day (the leave-out bridges named per unit above).

## Sources not loaded

- Federal pages, opened 2026-11-26: for day 90, the National Archives' 19th Amendment milestone page (https://www.archives.gov/milestone-documents/19th-amendment) and the National Park Service's "Who was excluded?" (https://www.nps.gov/articles/who-was-excluded-women-s-suffrage.htm, who was still kept from the polls after 1920); for day 164, ADA.gov's introduction to the ADA (https://www.ada.gov/topics/intro-to-ada/) and the National Archives' ADA research page (https://www.archives.gov/research/americans-with-disabilities, the July 26, 1990 signing). The National Archives milestone list ends in 1965 and has no 504 or ADA page; a 504 page is opened at the unit plan only if the unit plan picks 504 (browser check if it blocks).
- The women's history account (day 90) and the disability-led organization's account (day 164) are named at the unit plan and opened first by the sensitivity agent (browser check if one blocks).
- The Deaf-Hearing Communication Centre's communication tips (day 167) are read by the sensitivity agent.
- The cultural or education sources for the teammate's way (days 57, 71) are picked at the unit plan.

## For the lead

1. **school_day is cumulative.** The brief says "within its year"; cumulative values (160·i + ceil(2.5·s)) keep frame.py's year sort correct and equal its default spread. The weeks given here are within-year.
2. **The frame's open items:** "judgement" in STANDARD.md and the lens (US spelling "judgment"); PE 6 to 8's cue lines ("pick a tool" against the settled "choose"); career 6 to 8's obsolete Pending paragraph; the eighteen Spanish family notes waiting on a translation read.

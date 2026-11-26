# Expert read: scope and sequence, Social and Emotional Learning, Grades 6 to 8 (2026-11-26)

Course `social-and-emotional-learning-grades-6-to-8`. Brief: docs/pipeline/briefs/sequence-read.md, with
build/scope-writes/AFTERCORE-READ.md and AFTERCORE-BRIEF.md. Read cold; I did not write the scope.

## What I read

- docs/agents/EXPERT.md, the lens docs/agents/lenses/sel.md, bar part 9 of docs/ADOPTION-BAR-SUBJECTS.md, docs/courses/sel/STANDARD.md
  (section 7, the shared steps, read against every card the days quote), data/standards/casel-5.txt (our words for the 40 codes).
- docs/courses/social-and-emotional-learning-grades-6-to-8/scope-and-sequence.md and data/plans/social-and-emotional-learning-grades-6-to-8/days.csv
  (all 192 rows, goal and note).
- The frame (the brief, seams, models, every Units row in full, Course-level checks), the g6 to g8 rows of
  data/progressions/sel.csv for every owned code, docs/courses/CALENDAR.md and data/plans/calendar.csv (grades 6 to 8).
- Cross-checks: health 6 to 8 and physical education 6 to 8 days.csv (unit weeks), the ELA 6 to 8, math 6 and 7,
  world geography II and civics days.csv (first day of each core link the notes time), scripts/frame.py (how band
  school days are read), the after-core DESK-ANSWERS entries of 2026-11-26, and the SEL 3 to 5 sequence read of today.
- Gates: `plan.py check` (this course 0 failures), `frame.py calendar` (no break for this course), `sequence.py check`
  and `frame.py check` (0 failures; 18 units, 192 days, 60 unit days a year), `stale.py check` (0 failures).
- Opened: the National Archives 19th Amendment page and its milestone list, ADA.gov's introduction to the ADA, the
  Deaf-Hearing Communication Centre's communication tips page.

## Verdict

The scope is sound in its bones: three years taught three different ways, every session rehearsed, the shared cards
quoted in the band's words, every owned code placed with a named evidence point, the calendar clean, and the
sensitive guards (no student plays the pusher or the mocked, private SA7 and SA9 pages, invented cases, no clinical
words) carried on the days they apply. The biggest risk is in the owner year's evidence: several grade 8 owned codes
are judged on a part only (RS8's offer half, SM5's materials, SM1's recovery plan, RD5's written look-back), and
units 18 and 6 judge each student on acts the whole class or one leader does. The one change that matters most is a
unit 15 owner split plus one added page part in units 13 and 17, which closes those gaps and also settles the writer's
own For the lead item 3.

## Findings, most serious first

### 1. Four grade 8 owned codes are assessed on part of their row only

LAYER sequence. REPEAT new. Confidence: firm (row text against the day text).

- **What is wrong.** Each grade 8 owner row teaches the whole sub-skill (frame, Standard bullet), and each evidence
  point must ask every part of the id it claims.
  - **RS8** (g8-rel-ask-offer-help: "asking for help when it costs ... and offering help that takes real time"). The
    unit 17 Check (day 180) asks only "the right helper for a costly ask"; the rehearsal is the negotiation (RS5). No
    Application day is named for RS8. The offering half has no evidence point in the band's owner year.
  - **SM5** (g8-sm-plan-and-tidy: cut or move, the cost of each, "and keeps the project's papers and materials in a
    chosen system"; the code itself is "plan steps, manage time and keep materials in order"). Day 159 folds SM3 and
    SM5 into "one heavy-week case in two parts": the try-again plan and the cut week. The materials system is taught
    on day 158 but asked nowhere.
  - **SM1** (g8-sm-big-feelings: the response rehearsed "and writes what reacting would cost and how to recover").
    SM1 sits on day 159 only as the watched rehearsal; the written cost and recovery is on no page and no class sheet.
  - **RD5** (g8-rds-careful-thinking: the timed run "then reflects in writing on where the clock bent the thinking").
    Day 137 holds RD5 only as the rehearsal run aloud; the written look-back is not asked.
  - Lighter: **RD4** on day 137 is "a choice judged afterward"; the row also weighs short- and long-term costs before
    choosing. A busy item writer will write only the judgment.
  - The same gap at grade 6 depth: day 9's "the planner choice and its reason" leaves out g6-sm-plan-and-tidy's
    materials comparison (one binder or a folder per class).
- **Why it matters.** These are the band's last word on each code; grade 9 assumes the whole row (the hand-on table).
  A half asked is a half the course cannot say it taught.
- **Fix** (settled by the expert, see the table).
  - Unit 15 gets the owner split units 13, 14, 16, 17 and 18 already use: SM5 judged on day 158's class sheet (the cut
    week, the cost of each move and the folder or checklist system, which day 158's goal already holds); SM1 judged on
    day 155's class sheet (the written cost and recovery, which day 155's goal already holds), the watched high-stakes
    rehearsal still finishing on day 159. Day 159's page becomes SA3, SM2, SM3 with the AASL.V.D.1 look-for, SA8 with
    the AASL.V.D.2 look-for, and the two samples: six items, no two-part merge. Scope For the lead 3 is then settled
    and can be dropped. Day 159's codes keep SM1 (the rehearsal) and drop SM5.
  - Day 180's page item becomes two prompts: "the right helper for a costly ask" and "an offer of help that takes real
    time, sized on the meter, with its cost". Day 179's goal adds the offer to the case it already runs.
  - Day 137: the timed rehearsal ends with a one-line written prompt on the page, "where the clock bent the thinking
    and what a longer pause would change"; the RD4 item reads "short- and long-term costs of each option, the choice,
    then the choice judged against the ending", one prompt per part.
  - Day 9: "the planner and the materials system chosen, with the reason".

### 2. Owner skills judged on acts the class or one leader does

LAYER sequence (and frame, since unit 18 is the frame's model). REPEAT new. Confidence: likely.

- **What is wrong.** The class sheet marks a step seen for each student. Several Application days judge a step only
  some students take:
  - Day 184 judges SM6 and SM7 on "the class chooses and starts a first step, answers objections and carries out a
    part". One first step is chosen for the class; not every student answers an objection.
  - Day 187 judges RS7 on "the improvement team ... leads and follows a decision". One student leads; RD3 is "judges
    its chosen solution", a team act.
  - The same shape at grades 6 and 7: day 56 (SM7, "a first part of the proposal is carried out"), day 109 (RS7, "one
    student guides ... as a neutral leader"), day 126 (RD3, chosen by the class in one session).
- **Why it matters.** A teacher cannot mark 30 students "seen" from one leader or one class vote, so the sheet either
  fills with guesses or most cells stay blank and the Respond session reteaches students who never had a turn.
- **Fix** (settled by the expert). Each such day names the individual record inside the shared act:
  - Day 184: before the class picks, each student writes the first step they would take with its cost (SM6) and
    answers one objection card in writing (SM7).
  - Day 186 rehearses in trios with three small decision cards so each student leads one and follows two; day 187
    keeps that rotation on the real decisions, every student leading once, and each student writes the judgment of
    the solution against the class criteria (RD3).
  - Day 56: each student writes the presentation choice and the reason (SM7). Day 109: guides rotate by card so each
    student guides once (RS7). Day 126: each student writes one view of the cause and the solution they would test
    (RD3) before the class chooses.

### 3. The 10-days-short year folds away the only rehearsal of eight assessed skills

LAYER sequence. REPEAT yes (SEL 3 to 5 read of 2026-11-26, finding 2). Confidence: firm.

- **What is wrong.** The short year folds "the second Fluency day of each group into its Application day's opening,
  saving 25 minutes each" (days 3, 7, 24, 28, 78, 82, 88, 92, 131, 135, 174, 178). The opening is 5 minutes and is the
  session's one retrieval slot (frame, "never two openings"), so the fold cuts the day. Only day 3 repeats day 2's
  content ("the same three choices on harder week cards"). The others are the only Fluency for one skill, the session
  right before that skill's evidence point: day 7 (the RS8 ask, watched from day 8), 24 (SM1's response), 28 (RD6,
  judged day 29), 82 (SM3, judged day 83), 88 (SO1, judged day 89), 92 (RD2's sample), 131 (SA5's slowing thought,
  owned), 135 (RD7, owned, judged day 136), 174 (SO5, owned, judged day 175), 178 (RS8, owned).
- **Why it matters.** The scope promises that no assessed or owned part is cut. On paper that holds, but the
  owned skills go from Understanding straight to the judged Application with no rehearsal, which the lens names as
  SEL's common failure.
- **Fix** (settled by the expert). The same 12 sessions are saved, but each group's two Fluency days merge into one
  session split by skill: each skill keeps about 10 minutes of paired rehearsal on fewer cards, the retrieval opening
  is kept, and the merged day carries the second day's number. The Shorter path bullet reads: "merge each two-group
  unit's two Fluency days per group into one session, each skill rehearsed in its own block on fewer cards (days 2
  and 3, 6 and 7, ...); 4 a year, 12 in all."

### 4. Leave-out bridges missing or late where the frame names them

LAYER sequence. REPEAT yes (SEL 3 to 5 read, finding 3). Confidence: firm (the frame's Leave-out bullet against each first Understanding day).

- **What is wrong.**
  - Unit 4 uses the feelings scale (frame: unit 2's card, "first needed by unit 3, then 4, 10, 15"). Day 32 bridges
    only unit 3, and day 36 retrieves g6-sa-name-feelings.
  - Unit 5 uses the five-step stop-think-choose (frame: unit 3's cards, needed by "units 4, 5, 6"). Day 43 bridges
    only unit 4.
  - Unit 14 uses the refusal options and the I-statement (frame: unit 4's cards, needed by "units 6, 8, 11, 14, 17").
    Day 139 has no bridge.
  - Unit 6's unit-4 bridge is on day 60, the unit's third Understanding day. Day 56 already retrieves the talk turn
    card (g6-rel-talk-listen) and day 54 models the proposal's two ways to present it. The frame puts every bridge in
    the first Understanding session.
- **Why it matters.** A school that leaves out unit 2, 3 or 4 meets a card nobody taught. That is the exact case
  the bridge rule exists for.
- **Fix** (settled by the expert). Day 32 adds "or unit 2: the feelings scale's one-step form"; day 43 adds "or unit 3:
  the five-step stop-think-choose in its one-step form"; day 139 adds "Leave-out bridge if unit 4 was left out: the
  refusal options and the I-statement in their one-step forms (unit 8's bridge may already have taught them; then
  retrieval)"; unit 6's unit-4 bridge moves from day 60 to day 54, beside unit 3's, inside the same ten minutes. The
  scope's per-unit lines change to match (units 4, 5, 6, 14).

### 5. Grade 6 and 7 days claim the CASEL codes outright

LAYER sequence (process). REPEAT new. Confidence: firm.

- **What is wrong.** The frame and the progression mark grade 6 and 7 rows as begun (`~CASEL...`), with grade 8
  owning every code. The `codes` column on days 1 to 128 lists `CASEL.Self-Management.5` and the rest without the `~`,
  so each grade 6 and grade 7 day reads as owning the code. SEL 3 to 5's days.csv keeps the `~` on its begun years.
  `sequence.py` strips the mark, so the gate cannot see this.
- **Why it matters.** Coverage reports, the unit skeleton and the course page would credit each code three times in
  the band, and the "none claimed outside the owned rows" check fails on a read of the file.
- **Fix** (settled by the expert). Prefix `~` to every CASEL code on days 1 to 128 (a csv-module rewrite, codes column
  only). The scope's band bullet reads "Grade 6 and 7 rows begin their codes (~) at that grade's depth".

### 6. Day 1 is over its 30 minutes, and its readiness check sits at the start

LAYER sequence (and frame wording). REPEAT new. Confidence: likely.

- **What is wrong.** Day 1 holds the hook and compelling question, an 8-minute readiness card "after the hook, the
  session's first task", and the modeling of three sub-skills (planner and materials, three focus options, two first
  steps), "every student works one case on each", with the 5-minute close. That leaves about 12 minutes for three
  models and three student cases. Rule 2 (DESK 2026-11-14) puts unit 1's readiness check in the last ten minutes of
  day 1, after the hook. The frame says "inside session 1's first task", and the writer flagged the clash (For the
  lead 1). Two smaller points: the check marks three grade 5 rows, which is a check on year-before rows. That is
  justified at a band's entry, because a class may not have taken SEL 3 to 5, so no change is needed. The goal
  steps bridge is on day 2, after day 1 has already used the card for SA7.
- **Fix** (settled by the expert). Run the three day 1 models on one invented first week, so each student works one
  case in three parts. Model the goal steps card for SA7 with its four steps word for word ("goal, steps, block and
  plan, check", STANDARD section 7), which also serves a class new to the card. Move the readiness card to the last
  ten minutes. The frame's Days bullet should say "the last ten minutes of session 1" (For the lead).
- Related, LAYER sequence, REPEAT new: the goal steps card's four steps are quoted nowhere in days.csv or the
  scope, though the brief asks for every shared card word for word. The day 1 fix covers it; day 54's note may
  repeat it for health unit 8's rungs.

### 7. The once-a-week path does not say where Application evidence goes

LAYER frame and sequence. REPEAT new. Confidence: likely.

- **What is wrong.** On the once-a-week path a three-group unit's three Application sessions become one. Those
  sessions carry the class-sheet evidence of several codes (unit 4: days 34, 37 and 40; grade 8 unit 16: days 163 and
  166; unit 18: days 184 and 187), and in units 6, 12 and 18 they also carry the project. The scope says "no assessed
  step is cut" but does not say where those evidence points sit when 20 minutes hold all of them, or how much of the
  project a once-a-week class does.
- **Why it matters.** A once-a-week teacher cannot mark eight steps for 30 students and run a project part in one
  20-minute block. Unnamed evidence points become skipped ones.
- **Fix.** The Shorter path gains one line per unit kind: "once a week, the Application session marks the unit's
  watched rehearsal; the codes judged on Application days in the full path move to the shared Check page as one
  written part each (the page then holds the unit's own items, up to six)". For units 6, 12 and 18 add: "once a week,
  the class carries out one part of its proposal or improvement, chosen at the unit plan". If that page size breaks
  the frame's five-or-six cap, the frame's short-path text needs the same line (For the lead).

### 8. A source named for day 164 does not exist

LAYER frame (sources). REPEAT yes (SEL 3 to 5 read, finding 5: a named source that does not carry what the day needs). Confidence: firm (opened).

- **What is wrong.** The frame and day 164 teach Section 504 or the ADA from "the National Archives' milestone
  document page". The National Archives milestone list ends in 1965 (the Voting Rights Act and the Medicare and
  Medicaid Act). The page says later documents may be added, but today it has no page for the Rehabilitation Act of
  1973 or the ADA of 1990. The 19th Amendment page does exist and supports day 90's wording (ratified August 18, 1920;
  the vote "shall not be denied or abridged ... on account of sex").
- **Fix.** Day 164's note and the scope's "Sources not loaded" name a federal page that exists: ADA.gov's
  introduction to the ADA (Department of Justice, opened 2026-11-26; it describes the law's reach but not its 1990
  signing, so the date needs a second federal source) if the unit plan picks the ADA, or a federal page on Section 504
  if it picks 504. Either way the disability-led account is still picked at the unit plan, and the sensitivity agent
  opens both. The 504 case fits the frame's "law told apart from carrying it out" line especially well: the
  regulations followed only in 1977, after the 504 protests (from memory; the unit plan confirms it from the chosen
  account). The frame's Base text bullet needs the same correction (For the lead).

### 9. Small accuracy and wording faults

LAYER sequence. REPEAT yes (the same kind as SEL 3 to 5 finding 6). Confidence: firm unless marked.

- Day 1's note says the ELA discussion norms (ela:e6-collab-discussion) run "same weeks". ELA 6 first teaches them on
  its day 5 (school day 5), and SEL day 1 is school day 3. Fix: "from day 2 on, where ELA has set them; day 1 uses
  the teacher's own two talk rules".
- Day 54 says health unit 8 (goals, weeks 25 to 28) "came first". Health 8 runs to school day 137 and SEL day 54 is
  school day 135, so it is alongside. Fix: "runs alongside and is nearly done".
- PE weeks in the notes, copied from the frame, are a week or two off PE 6 to 8's days.csv: unit 4 runs weeks 12 to
  15 (day 57 says 13 to 16), unit 12 weeks 17 to 21 (day 99: 18 to 22), unit 18 weeks 12 to 14 (day 185 in the
  frame: 14 to 16). Each order claim still holds. Fix the numbers, or drop them and keep "came first" or "same weeks".
- Day 22's goal says "the teacher's own model falling apart". The frame has an invented character's model, and a
  reader may take it for the teacher's own story. Fix: "an invented character's model falling apart".
- AASL is named at grade 6 and 7 depth on days 57, 68, 80 and 102, but not on grade 6's SM3 (days 1 to 4) or SA8 (day
  26). Fix: add "SM3 here also carries AASL.V.D.1 at grade 6 depth" to day 1 and "SA8 ... AASL.V.D.2" to day 26, as
  the scope's own band bullet implies.
- Day 90, likely (from memory, standard history): the "law told apart from carrying it out" line should name who was
  still kept from voting after 1920 (Black women under Southern voting laws, Native American women before the 1924
  citizenship act and later state bars, immigrant women barred from citizenship). That is the settled fact the page
  needs. The unit plan confirms it from the women's history account it picks.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Unit 15 owner split: SM5 on day 158's class sheet, SM1's written cost and recovery on day 155's; day 159's page = SA3, SM2, SM3 (V.D.1), SA8 (V.D.2) + two samples; drop SM5 from day 159's codes | asks each owned row whole, inside the frame's six-item cap; removes For the lead 3 | days.csv days 155, 158, 159; scope unit 15 and checks table |
| Day 180 page item gains the offer prompt; day 179's goal adds the offer | RS8's offering half had no evidence point | days.csv 179, 180; scope unit 17 |
| Day 137 adds the written "where the clock bent it" prompt and splits the RD4 item into weigh, choose, judge | RD5 and RD4 rows asked in full | days.csv 137 |
| Day 9 item: "the planner and the materials system chosen, with the reason" | g6 SM5's materials half | days.csv 9 |
| Individual records inside shared acts on days 56, 109, 126, 184, 186 and 187 (written step, objection, rotating leaders, written judgment) | each student's step can be marked | days.csv those days; scope units 6, 11, 12, 18 |
| Short year: merge each group's two Fluency days into one skill-split session (same 12 sessions) instead of folding into the opening | keeps a rehearsal for every assessed skill | scope Shorter path |
| Leave-out bridges added on days 32 (unit 2), 43 (unit 3), 139 (unit 4); unit 6's unit-4 bridge moved from day 60 to day 54 | the frame's bridge list in full, in the first Understanding session | days.csv 32, 43, 54, 60, 139; scope units 4, 5, 6, 14 |
| `~` on every CASEL code on days 1 to 128 | grade 6 and 7 rows are begun, not owned | days.csv codes column |
| Day 1: three models on one first-week case, the goal steps card quoted word for word, readiness in the last ten minutes | the 30 minutes hold; rule 2; the shared card quoted | days.csv 1; scope unit 1 readiness line |
| Notes on days 1, 22, 26, 54, 57, 90, 99 per finding 9 | accuracy and consistency | days.csv |

## The lens checklist (scope and sequence layer)

| Line | Met? |
|---|---|
| Self-management and relationship skills rehearsed, not only discussed | Met: every Fluency and Application rehearses; calm-down done with the body (days 23, 100), refusals against a card. |
| A skill's name or steps unchanged between units of one year | Met: each card grows only in its named unit (stop-think-choose in unit 3, talk turn and refusal in unit 4, upstander in unit 6), the wording matching STANDARD section 7. |
| Health topics pointed to, not taught | Met: each health unit is named on the day it applies; sleep stays a character's and part of a plan (days 26, 150); substances, rides and dares with body risk are kept out. |
| No sub-skill above the age | Met: unfair norms only from settled history (grade 7, grade 8) and invented school norms. |
| A year that repeats another year | Met: grade 6 options, grade 7 the second person's side, grade 8 a cost on every option, visible in every goal. |
| A sub-skill missing from a grade | Met: all 40 in each year (gate and frame table). |
| Short path drops sessions, not units | Met in shape; see findings 3 and 7 for what the shorter sessions must keep. |
| Carry it out and family activity per unit | Met in the frame; the scope leaves them to the frame, which is fine. |
| Sensitive guards (no pusher or mocked part for a student, invented cases, private pages, no clinical words, disclosure route) | Met on the days they apply (8, 18, 24, 38, 60, 76, 113, 145, 188 and others). |

## What is right and should not be touched

- The cumulative school_day (160 x year + ceil(2.5 x session)) is right. frame.py splits band years by 160-day spans
  and DESK 2026-11-26 says school_day counts across a K to 8 band. Scope For the lead 2 needs no change.
- The calendar: every check falls on its CALENDAR.md target week (15, 15, 16; 32 each year), and no grade 6 to 8 check
  shares a school day with another subject's mid-year check (grade 8 day 78 sits between career's day 77 and its
  respond day 79, clear of science's 75).
- The owner splits in units 13, 14, 16, 17 and 18, and the "steps seen, never willingness" line.
- Every health cross-reference checked against health 6 to 8's days.csv (units 2, 3, 4, 7, 11, 12, 17, 18, 23 to 27)
  is in the order the note claims. Every core link timed against its course's days.csv (ELA 6 to 8, math 6 and 7,
  Athenian democracy, civics units 5, 6, 9, 10) is too, except day 1 (finding 9).
- The Deaf and hearing team on case cards, with no simulation of hearing loss. The cited Deaf-Hearing Communication
  Centre page exists and stresses asking each person's preference, which is what day 167 teaches.
- The settled cases: one a year, no repeat in the band, Brown v. Board left to 3 to 5 and 9 to 12.

## What I could not judge

- Whether a 30-minute Check session holds six items, one prompt per part, plus the unfinished pairs' rehearsals. That
  needs the unit plan's timed probe.
- The disability-led account and the women's history account, which are not yet picked (unit plan, sensitivity agent).
- The cited cultural or education sources for units 6 and 7, not yet picked.

## For Cory

- None. Every finding is inside the frame's scope, audience and money.

## For the lead (frame fixes, not the scope's)

- The frame's Days bullet: unit 1's readiness check goes in "the last ten minutes of session 1" (rule 2), not "inside
  session 1's first task".
- The frame's Base text bullet and unit 16 cell: no National Archives milestone page exists for Section 504 or the
  ADA. Name a federal page that exists (ADA.gov for the ADA) or leave the federal source to the unit plan.
- The frame's once-a-week text: where Application-day evidence and the project parts go (finding 7).
- The frame's PE week numbers (finding 9).

## Sources

- National Archives, 19th Amendment milestone page, https://www.archives.gov/milestone-documents/19th-amendment: day
  90's date and wording confirmed.
- National Archives, milestone documents list, https://www.archives.gov/milestone-documents/list: confirmed the list
  ends in 1965, with no 504 or ADA page.
- ADA.gov, Introduction to the ADA, https://www.ada.gov/topics/intro-to-ada/: a federal page that exists for the ADA
  case (it does not give the 1990 date).
- Deaf-Hearing Communication Centre, communication tips, https://www.dhcc.org/resources/communication-tips: confirmed
  it exists and fits day 167.
- From memory, marked where used: the 1977 Section 504 regulations after the protests; who was still kept from voting
  after 1920.

## For the source list

- The National Archives milestone list (above) stops at 1965. Any frame that names a "milestone page" for a later law
  needs another federal source.
- ADA.gov's introduction page (Department of Justice, public domain) as a federal page for the ADA.

# Expert read: scope and sequence, Social and Emotional Learning, Grades 3 to 5 (2026-11-26)

Course `social-and-emotional-learning-grades-3-to-5`. Read cold as a grades 3 to 5 classroom teacher who teaches SEL,
a district adoption reader and a researcher, per docs/pipeline/briefs/sequence-read.md and
build/scope-writes/AFTERCORE-READ.md. A fresh Claude agent wrote the scope. This read changes no file except this
report.

## What I read

- docs/courses/social-and-emotional-learning-grades-3-to-5/scope-and-sequence.md in full, and all 192 rows of
  data/plans/social-and-emotional-learning-grades-3-to-5/days.csv (goal, note, skills, codes, retrieves, school_day).
- The frame docs/courses/social-and-emotional-learning-grades-3-to-5/frame.md: The course in brief, the seam from K
  to 2, Models carried, the Units table, Course-level checks and the Cross-subject headings.
- data/progressions/sel.csv: every grade 3, 4 and 5 row (standard, assumes, notes).
- docs/agents/EXPERT.md, docs/agents/lenses/sel.md, docs/ADOPTION-BAR-SUBJECTS.md part 9, docs/courses/sel/STANDARD.md
  section 7 (shared steps), build/scope-writes/AFTERCORE-BRIEF.md.
- docs/courses/CALENDAR.md (rule 1, the grade 3, 4 and 5 SEL rows) and data/plans/calendar.csv for grades 3 to 5
  (health 3 to 5, PE 3 to 5, math 3, ELA 3 to 5, social studies 3 to 5, computer science 5), and the core days.csv
  files for the 17 core links the scope names, to test each "same weeks", "came before" and "comes later" claim.
- For the REPEAT tag: docs/reviews/sequence-computer-science-grade-10-2026-11-26.md and
  sequence-library-and-research-skills-grade-5-2026-11-26.md.
- Outside, opened 2026-11-26: the National Archives Brown v. Board page, the Brown Foundation page, the National Park
  Service Brown v. Board pages (history index, Briggs v. Elliott), and the CPSC Public Playground Safety Handbook PDF
  (text pulled with pypdf).

Gates run first. `scripts/plan.py check`: this course has no plan-stage failures. `scripts/sequence.py check`: 0
failures. `scripts/frame.py check`: 0 failures (unit days 60 a year; 18 units, 192 days). `scripts/frame.py calendar`:
SEL grade 3 weeks 10 and 26, grades 4 and 5 weeks 15 and 26, matching CALENDAR.md's table. `scripts/stale.py check`:
nothing for this course. I recomputed every check and respond week from the scope's school_day formula: all six
checks and their respond days sit in the frame's and CALENDAR.md's weeks, clear of each grade's core check weeks and
of health 3 to 5's (15/29, 14/29, 14/28). Every owned and begun id sits on a day inside its frame unit, and none is
claimed outside the frame's rows. All 17 core-link and 14 health/PE/CS timing claims hold against the other courses'
days, with one stale wording (finding 6).

## Verdict

The scope is sound in its shape: the years differ in depth as the frame asks, every self-management and relationship
skill is rehearsed by doing, the calendar holds, safety and care guards are on the right days, and the Brown v. Board
case is right in its facts. The biggest risk is the end-of-unit evidence: in 16 places a Check note says a code is
"seen on day N" when day N does not hold that skill, or holds it only as a Fluency day with the card in hand, so the
third skill of many groups (repair, leading, care steps, systems) is taught and rehearsed once and never seen on an
unseen case. The one change that matters most is to put each of those skills into its group's Application goal, the
day the Check note already names; four short-year fold-ins then need moving off the only rehearsal of those same
skills.

## Findings, most serious first

### 1. Sixteen evidence pointers name a day that does not hold the skill, or a Fluency day

LAYER sequence. REPEAT new.

- **What is wrong.** The `skills` column lists every group skill on every day of the group, but the goals carry only
  some of them. For the third skill of a group the arc is often Understanding, one Fluency, and then nothing: the
  Application goal leaves it out, and the Check note points at that Application day anyway (or at the Fluency day).
  The cases, with what the named day actually does:

  | Check | Code (row) | Note says | What that day holds |
  |---|---|---|---|
  | 41 | RS2 (g3-rel-friendships) | repair seen on day 36 | day 36: talk turn, I-statements, fair solution; repair only on F35 |
  | 41 | RS7 (g3-rel-lead-follow) | leading steps seen on day 40 | day 40: sizing, situation questions, I-statement; leading only on F39 |
  | 52 | RD1 (g3-rds-ask-questions) | changed idea seen on days 46 and 48 | 46 is the day it is first taught; 48 is graph and rule only |
  | 63 | SM3 (g3-sm-stay-on-task) | focus plan seen on day 58 | 58 is a Fluency day, card held; A59 has no focus plan |
  | 63 | SM6 (g3-sm-step-forward) | welcome-kit first step, days 60 to 62 | started on F61 only; A62 has no welcome kit |
  | 104 | SO3 (g4-soc-care-when-struggle) | adapted care steps seen on day 99 | 99 is Fluency; A100 is check-in and coaching only |
  | 115 | RS7 (g4-rel-lead-follow) | leading steps seen on day 108 | 108: election and first step; leading only on F107 |
  | 115 | RS2 (g4-rel-friendships) | repair seen on day 111 | 111: team disagreement to a solution; repair only on F110 |
  | 127 | RD6 (g4-rds-good-for-us) | weighed choice seen on day 123 | 123: solution and map; the well-being choice only on F121 |
  | 157 | SO8 (g5-soc-why-rules, owned) | system traced on day 152 | 152: claim against a count and the hurry cost; system only on F151 |
  | 168 | SO3 (g5-soc-care-when-struggle, owned) | care steps and follow-up seen on day 161 | 161: moving friend's view and check-in; care steps only on F160 |
  | 168 | RS8 (g5-rel-ask-offer-help, owned) | asking seen on day 167 | 167: sizing and naming the helper; asking with friends watching only on F166 |
  | 180 | RS7 (g5-rel-lead-follow, owned) | split decision seen on day 171 | 171 is Fluency; no Application leads a split group |
  | 147 | SA9 (g5-sa-what-interests-me, owned) | the log, steps followed only | unit 14 keeps no log; SA9 is on U143 alone |
  | 127 | RD3 (g4-rds-solve-problems) | item 2, two groups' views | the row's "testing a solution" is never run (finding 4) |
  | 20 | SA4 (g3-sa-tell-truth) | page item, honest action and its value | the row's "what honesty cost the character and what it kept" is not asked |

  RS2, RS7 and SO3 miss in all three years, so this is a writing pattern, not a slip.
- **Why it matters.** The frame says each code's end-of-unit evidence is a page item, the watched rehearsal, or a
  product or performance seen in Application with the card withdrawn, and never on a day the skill is first taught.
  As written, five grade 5 owned codes (SO8, SO3, RS8, RS7, SA9) have no valid end-of-unit evidence, and a teacher
  marking the class sheet on day 36 or 108 will look for a step the day never runs. A unit plan writer will build the
  Application days as the goals say and the gap will carry into the lessons.
- **Fix.** Add the missing skill to the named Application goal, card withdrawn, on an unseen case, so each pointer
  becomes true (settled by the expert, table below): day 36 adds "and repair an unseen broken-trust moment, the
  teacher supplying the hurt friend's words"; day 40 adds "and one student leads a short group choice with the three
  leading steps"; day 48 adds "and asks what, why, what if of an unseen class-choice case, saying what changed their
  idea" (day 52's pointer becomes "day 48"); day 59 adds "and uses the focus plan in the planned work time against a
  planned distraction" (pointer "day 59"); day 62 adds "and the welcome kit's first step is checked against its plan"; day 100 adds "and adapts the care steps for an unseen teammate who wants something different"; day 108 adds "the
  elected team's first meeting led with the three leading steps, leader and follower saying how each saw the
  decision"; day 111 adds "and a repair talk for two friends in different groups, the friend's side heard first, the
  teacher supplying the friend's words"; day 123 adds "and each student weighs an unseen well-being choice for self
  and a friend"; day 152 adds "and traces an unseen town system and the pressure on it"; day 161 adds "and acts the
  care steps with a follow-up for an unseen friend whose best friend moved away, a partner playing only the friend";
  day 167 adds "and rehearses asking the teacher for help with friends watching, a partner playing the teacher"; day
  172 adds "the class's split choice of a first step led to a decision, and each student says how they follow when
  their idea lost" (day 180's pointer becomes "day 172"); day 146 adds "and each student marks, privately, the
  purpose-and-cost decision begun on day 143, checked only that the steps were followed" (day 147's pointer becomes
  "the private decision sheet, day 146, steps followed only"); day 20's page item 1 becomes "the honest action, its
  value, and what honesty cost and kept". Application days are 20 minutes of work and these add one short task each;
  where a day is full, the unit plan trims the second task, never the added skill.

### 2. Four short-year fold-ins remove the only rehearsal of an assessed skill

LAYER sequence. REPEAT yes (the computer science grade 10 read of the same day flagged fold-ins that thin an assessed
skill).

- **What is wrong.** The short year folds day 35 (the only repair rehearsal, RS2), day 39 (the only leading
  rehearsal, RS7), day 61 (the only roles rehearsal and the welcome kit's start, RS4 and SM6) and day 160 (the only
  care-steps rehearsal, owned SO3). Day 186 is the only place grade 5 weighs solution costs before acting (RD3, owned)
  and goes too. On the short year those skills go from Understanding straight to the Check.
- **Why it matters.** The scope promises "no owned part cut"; on paper nothing is cut, but the assessed step loses all
  rehearsal, which the frame's kinds of day forbid and the bar's "practised by doing" item scores.
- **Fix.** Fold days whose content the next Application repeats: grade 3 days 14, 18, 34 and 38 (A15, A19, A36 and
  A40 hold those tasks); grade 4 unchanged (67, 77, 102, 125, each covered by its Application); grade 5 days 131, 135,
  141 and 155 (A132, A136, A142, A156 hold them). Update the three day notes that say "Fold-in day" and the Shorter
  path list. Still 12 sessions, 360 minutes.

### 3. Leave-out bridges are missing where the frame names them

LAYER sequence. REPEAT new.

- **What is wrong.** The frame says unit 1's strength scale and four-step stop-think-choose are first needed by units
  2, 3 and 5, and unit 6's goal steps card and focus plan by unit 8. The scope bridges unit 1 only on day 33 (calm-down
  steps) and unit 6 nowhere. Days 16, 25 and 43 use stop-think-choose, day 22 rates on the strength scale, and days 75
  and 79 use the goal card and the focus plan with no bridge line.
- **Why it matters.** A school that leaves out unit 1 or unit 6 gets lessons that lean on a card nobody taught, which
  is the case STANDARD section 5.6 and the frame's Leave-out bullet exist for.
- **Fix.** Add to the notes (settled by the expert): day 12 "Leave-out bridge: where unit 1 was left out, the first
  ten minutes teach four-step stop-think-choose"; day 22 "where unit 1 was left out, the first ten minutes teach the
  strength scale and four-step stop-think-choose"; day 43 adds stop-think-choose to its existing bridge; day 75 adds
  "where grade 3 unit 6 was left out, the goal steps card"; day 79 "where grade 3 unit 6 was left out, the first ten
  minutes teach the focus plan and its try-again step" (day 79, not 75, because day 75 already carries the agreement
  bridge and the focus plan is first used on 79). Add the five to the scope's Leave-out list.

### 4. Grade 4 RD3 never tests its solution

LAYER sequence. REPEAT new.

- **What is wrong.** g4-rds-solve-problems is "gathering two groups' views before choosing and testing a solution".
  Day 123 chooses the solution and plans its test; no later day runs or checks it, and the Check (day 127) asks only
  about the views.
- **Why it matters.** The testing step is the part grade 3 added and grade 4 keeps; dropping it leaves the grade 4
  row a step below grade 3's coat-hook test.
- **Fix.** Day 123 starts the test (one week, school days 307 to 312); day 126's goal adds "the class checks the
  solution test from day 123 and decides what to keep" (as day 51 does in grade 3); day 127's pointer for RD3 becomes
  "item 2 and the test checked on day 126".

### 5. The Brown v. Board sources do not carry the families' cost the day teaches

LAYER sequence (and frame). REPEAT new.

- **What is wrong.** Day 153 teaches "what changing it cost the families and students who did". The frame and scope
  cite the Brown Foundation page "for the families who brought the case"; opened today, that page is the foundation's
  own story and names Oliver Brown only in passing. Nothing listed backs the cost claim. The National Archives page is
  right on everything else: decided May 17, 1954, unanimous, segregation of public schools unconstitutional, and the
  1955 order to desegregate "with all deliberate speed" supports the day's "slower work of carrying it out".
- **Why it matters.** The cost line is the part of the page a child will remember, and it must rest on a source the
  sensitivity agent can read.
- **Fix.** Add the National Park Service's Brown v. Board pages to day 153's note, the scope's "Sources not loaded"
  and the frame's For the lead: https://www.nps.gov/brvb/learn/historyculture/fivecases.htm (five cases) and
  https://www.nps.gov/brvb/learn/historyculture/socarolina.htm (Briggs v. Elliott: parents fired from jobs, refused
  service and loans). The grade 5 page names job loss and refused loans only; the threats and the attack on Rev.
  DeLaine that the page also describes stay off a grade 5 SEL page (settled by the expert). Keep the Brown Foundation
  page as a secondary link, not the families source.

### 6. Small accuracy and wording faults

LAYER sequence. REPEAT new.

- Day 12's note says social studies' ss3-biography "comes later (course days 141 to 160)"; social studies grade 3
  meets it on days 1, 35 and 54 too. Fix: "social studies grade 3 meets ss3-biography across the year; the strengths
  hunt needs nothing from it".
- Days 21, 53, 94, 116, 158 and 181: "sheets are is thrown away". Fix: "sheets are thrown away".
- The scope's shared-cards heading says the cards are "quoted as the frame quotes STANDARD section 7 for grades 3 to
  5". Section 7 gives a grades 3 to 5 form only for the I-statement; the four-step calm-down, talk turn, goal and
  refusal forms are the frame's growth of the section 7 cards. Fix: "as the frame grows STANDARD section 7's cards for
  grades 3 to 5".
- The CPSC handbook (opened: the December 29, 2015 edition) is about playground equipment, not a litter pick-up. Keep
  it for the grounds check, and name the school's grounds policy as the pick-up guide on days 185 and 187.
- Grade 3 unit 6's welcome kit for new students and grade 4 unit 8's class guide for new students are the same
  product a year apart (lens: a year repeating another year's case). Settled below: grade 4's project becomes a class
  guide to our routines for a substitute teacher day, which also reuses unit 7's substitute-day situation (SO7).

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Add the missing skill to Application days 36, 40, 48, 59, 62, 100, 108, 111, 123, 146, 152, 161, 167, 172, with the wording in finding 1, and repoint Check notes on days 52, 63, 147, 180 | each code then has unseen, card-withdrawn evidence on the day its Check note names | days.csv |
| Day 20 page item 1 asks the honest action, its value, and what honesty cost and kept | asks the whole of g3-sa-tell-truth | days.csv |
| Short-year fold-ins: grade 3 days 14, 18, 34, 38; grade 5 days 131, 135, 141, 155; grade 4 unchanged | each folded task is repeated on the next Application | days.csv notes, scope Shorter path |
| Leave-out bridges on days 12, 22, 43 (stop-think-choose, strength scale), 75 (goal steps card), 79 (focus plan) | the frame names these cards and receiving units | days.csv notes, scope Leave-out list |
| Unit 12 solution test runs from day 123 and is checked on day 126 | completes g4-rds-solve-problems | days.csv |
| Brown v. Board: NPS five-cases and Briggs v. Elliott pages back the cost line; job loss and refused loans only, no violence on the grade 5 page | sourced, age-fit cost | days.csv day 153 note, scope Sources |
| Grade 4 unit 8 project: a class guide to our routines for a substitute teacher day | no repeat of grade 3's welcome kit; reuses SO7's case | days.csv day 75 (frame wording for the lead) |
| Fix the stale ss3-biography note, the "are is" typo and the shared-cards heading; name the school's grounds policy for the pick-up | accuracy | days.csv, scope |

## The lens checklist (scope and sequence layer)

- Self-management and relationship skills rehearsed, not only discussed: met on every Understanding and Fluency day;
  missed on Application for the cases in finding 1.
- A skill's name or steps unchanged between units of one year: met (cards and the try-again step worded once; grade
  4 and 5 retrieve the grade 3 card forms).
- Health topics pointed to, not taught: met (snack claim checks a source, not nutrition; tobacco, body safety,
  relationship health and substances named as health's).
- Nothing above the grade's age: met (unfair norms of the past only in grade 5, Brown v. Board, settled fact; grade 3
  systems are school routines).
- Settled cases do not repeat in the band: met for the three cultural cases and the history case; one repeated
  product (finding 6).
- Partners never play the unkind part: met on every refusal, upstander, repair and exclusion day.
- Private pages, invented cases, no clinical words, disclosure route: met on the days they apply.
- Carry-out cue and family note per unit: met (all 18 units; every Respond day sends the note).

## What is right and should not be touched

The three-year depth ladder; the Check design (page and rehearsal side by side, one sheet thrown away after Respond);
the retrieval opening on every group's Understanding day with the prior-grade id in `retrieves`; the school_day
formula and the check weeks; the health seam days (each "where the school runs health" line matches health 3 to 5's
weeks); the coat-hook and three-week trackers that end before their Checks; counts-not-percents in unit 15.

## What I could not judge

The cited cultural sources for days 25, 89 and 173 and the families-and-cultures guidance are not chosen yet. Whether
the 5-minute opening can hold the calm-down routine plus three retrieval items on Understanding days is a pacing
question the probe day will answer.

## For Cory

None. Every finding is item-level or a day placement inside its unit.

## For the source list

- National Park Service, Brown v. Board pages: https://www.nps.gov/brvb/learn/historyculture/fivecases.htm and
  https://www.nps.gov/brvb/learn/historyculture/socarolina.htm (opened 2026-11-26; plaintiffs' reprisals in Briggs v.
  Elliott).
- The Brown Foundation page (https://www.brownvboard.org/brown-foundation-story) is the foundation's history, not an
  account of the families; note that beside it.
- CPSC Public Playground Safety Handbook, https://www.cpsc.gov/s3fs-public/325.pdf: December 29, 2015 edition, 61
  pages, text readable with pypdf.

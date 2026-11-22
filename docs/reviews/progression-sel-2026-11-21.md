# SEL progression: expert cold read, 2026-11-21

Reader: the curriculum expert (docs/agents/EXPERT.md), run cold on data/progressions/sel.csv. Nothing was edited except
this report. Brief: docs/pipeline/briefs/progression-read.md, with {subject} = sel.

## What I read

- docs/agents/EXPERT.md; the lens docs/agents/lenses/sel.md; the pass rule, the shared core and part 9 (Social and
  emotional learning) of docs/ADOPTION-BAR-SUBJECTS.md; docs/courses/sel/STANDARD.md and APPROACH.md in full.
- data/progressions/sel.csv: 520 rows, 40 per grade K to 12, 160 owner rows (grades 2, 5, 8, 12) and 360 `~` rows.
  data/progressions/sel-edges.md (130 cross_subject edges; they match the csv one for one).
- data/standards/casel-5.txt (40 sub-skills, our words).
- For leans only: the target rows in data/progressions/health.csv, ela.csv, math.csv, social-studies.csv,
  physical-education.csv and computer-science.csv (ids, grades, standards, and the notes of the health rows named).
  data/progressions/library-excluded.csv and docs/courses/library/STANDARD.md section 4 for the three AASL ids placed in SEL.
- Gate: `python -X utf8 scripts/progression.py check sel`: 520 rows, 0 failures. `stale.py check` on the four SEL
  pages: 0 failures. plan.py not run, as told. No reconcile report exists for SEL.
- My own checks, run in the scratchpad over the csv: each row's unit against STANDARD section 3's grade table (all 520
  match); model first use by grade and by unit; every cross_subject id and every health id named in a note against its
  file and grade; a marker search for each `~` row's year line; rehearsal words in the self-management and
  relationship rows; text similarity between rows of one sub-skill; K to 2 step counts; multi-week tasks; a word search
  for sensitive ground.
- For REPEAT I compared finding kinds with the headings of the health, physical education and computer science
  progression reads of 2026-11-19 and the core reads of 2026-11-13.

## Verdict

The progression is sound in its frame: every grade teaches all 40 sub-skills in the units STANDARD section 3 places
them in, the seven models start in K or grade 1 and run to grade 12 with no gap and no early use, all 130 leans and all
13 health rows named in teacher notes exist at or before their grade, and the within-band step (school day, second
person, cost, past school) is real in almost every row of grades 1, 3, 6, 7, 9, 10, 11 and 12. The biggest risk is bar
item 5: from grade 3 on, 24 of the 30 rows for friendships, asking and offering help, and standing up for others ask
students to choose, plan or write, and name no rehearsal, so a writer building days from the rows would build the
"discussion with no practice" sessions the bar fails. The one change that matters most is a rehearsal clause on those
rows; after it, the year lines missing from kindergarten and grade 4 and the grade 11 rows that reuse grade 8's cases.
Twelve findings; none needs a gate change, and only one goes to Cory.

## Findings, most serious first

### 1. Relationship rows stop rehearsing after grade 2 (serious; firm. LAYER progression. REPEAT new)

Bar part 9 item 5 and its "Fails if" (posters and discussion with no practice), the lens ("Self-management or
relationship skills met only by discussion, with no rehearsal") and STANDARD section 3 ("Role play of refusal and
standing up... the teacher or a card plays the pressure") all expect relationship skills to be rehearsed. Refusal
(RS6) and settling disagreements (RS5) are rehearsed in every grade. Three relationship sub-skills are not:

- RS9 stand up for someone: K to 2 rehearse; **g3, g4, g5, g6, g7, g8, g9, g10, g11, g12** all pick, choose or plan an
  option and none says the words are rehearsed.
- RS2 friendships: g3, g9 and g10 rehearse; **g4, g5, g6, g7, g8, g11, g12** weigh, write or plan only.
- RS8 ask and offer help: g3, g5 and g10 rehearse; **g4, g6, g7, g8, g9, g11, g12** size, plan or map only.
- Also SM1 strong feelings: **g5-sm-big-feelings** and **g6-sm-big-feelings** list and pick a response with no body
  routine or rehearsed response.

Cost: the section plan writer fills "practice by doing" from the row (bar, "Section plan fills: the practice by
doing"). A row that says "chooses the safest option, writing why" becomes a worksheet day. A reviewer marks the bar's
fail condition on every sampled unit that holds RS9.

Fix (row edits; the wording is item-level, I settle it): append one clause to each listed row, before its year line.
- RS9 rows: "The student then rehearses the chosen words with a partner while the teacher or a card plays the unkind
  act; no student plays the one who is unkind or the one treated unfairly."
- RS2 rows: "The student rehearses the opening of the talk with a partner, using the I-statement frame."
- RS8 rows: "The student rehearses the ask (or the offer) aloud with a partner playing the helper (or the friend)."
- g5 and g6 sm-big-feelings: "then rehearses the calm-down steps and the chosen response in a short scene."
In grades 9 to 12 the rehearsal sits between the plan and the judgement: plan, rehearse, judge.

### 2. Kindergarten and grade 4 `~` rows lack their year line (moderate; firm. LAYER progression. REPEAT new)

STANDARD section 3 (Ownership): a `~` row "has... a one-line note on how that year differs". The line is present and
varied, not stock, in grades 1, 3, 6, 7, 9, 10 and 11 (for example "Grade 7 makes the other person the judge of
whether they were heard", "New in grade 11: the price of changing a norm"). It is missing from:

- **K: 37 of 40 rows** (all but k-rel-talk-listen, k-rel-ask-offer-help and k-sm-have-a-say, which say "First year: ...").
- **Grade 4: 33 of 40 rows**: g4-sa-tell-truth, g4-soc-read-situation, g4-rds-careful-thinking, g4-sa-i-can-try,
  g4-sm-stay-on-task, g4-sm-plan-and-tidy, g4-sm-step-forward, g4-sa-my-strengths, g4-soc-notice-good,
  g4-sa-snap-judgments, g4-rel-different-ways, g4-sa-name-feelings, g4-sa-feel-think-link, g4-sm-big-feelings,
  g4-sm-calm-down, g4-soc-care-when-struggle, g4-soc-read-feelings, g4-soc-thankful, g4-soc-why-rules,
  g4-rel-friendships, g4-rel-settle-disagreements, g4-rel-ask-offer-help, g4-rel-lead-follow, g4-rel-say-no,
  g4-rel-stand-up, g4-sm-have-a-say, g4-rds-good-for-us, g4-rds-ask-questions, g4-rds-check-facts,
  g4-rds-solve-problems, g4-rds-think-ahead, g4-rds-who-is-affected, g4-sa-skills-grow.
- Grade 1: g1-rel-different-ways and g1-rds-careful-thinking.

The grade 4 cases do carry the second person (the step is real); the line naming it is what is missing. Cost: the
frame writer for grade 4 cannot tell from the row alone what makes the grade 4 day differ from grade 3's and 5's, which
is the lens's first error ("a grade year that repeats another year of its band").

Fix: append one line per row. Kindergarten: "First year: <what the child does first>", for example k-sm-calm-down
"First year: two body steps, done with the teacher." Grade 4: "Grade 4 adds <the second person>", for example
g4-sm-calm-down "Grade 4 adds a partner: the student coaches someone else's plan." g4-rel-say-no "Grade 4 adds the
group: the no is held while the friendship is kept."

### 3. Grade 11 reuses grade 8's cases (moderate; firm. LAYER progression. REPEAT new)

In 6 to 8 and 9 to 12 the third year adds a cost, so grade 8 (owner) and grade 11 both carry "cost". The depth differs
(grade 11 plans and judges), but nine grade 11 rows take grade 8's case almost word for word:

| Sub-skill | Grade 8 case | Grade 11 case | Fix: a new grade 11 case |
|---|---|---|---|
| g11-soc-read-feelings | cues behind jokes, "may cost a laugh" | the same, in a group chat | a teammate's short replies after being cut from a starting line-up, read over a week of messages |
| g11-soc-notice-good | rival team, "costs a little pride" | rival team at a shared event, "a little pride" | credit to a junior teammate whose idea replaced the student's own |
| g11-rds-who-is-affected | popular choice that costs another group | the same | a prom or trip date that suits most seniors but clashes with a large group's work shifts |
| g11-sm-have-a-say | school improvement, costs for groups, objections | the same, plus judging | a proposal to change one school routine that staff time limits (a later library hour), with a staffing cost |
| g11-rel-lead-follow | lead an unpopular decision, follow a leader you disagree with | the same | lead a group that must cut a member's part to meet a deadline |
| g11-soc-fair-rules | settled case plus a school norm someone pays to change | the same | keep the settled case; set beside it an invented school norm whose change would cost the student's own group a privilege |
| g11-sm-step-forward | school improvement that "may cost time and draw teasing" | the same phrase | start a peer tutoring slot that costs the student a free period |
| g11-rel-stand-up | speaking up "costs standing with friends" | the same | speaking up when the unkind act comes from a teammate the student depends on for a shared grade |
| g11-rel-friendships | staying close costs other friends or values | costs "grades, other friends" | a friend who asks for daily help with work the student has no time for |

Cost: a student who had the same school in grades 8 and 11 meets the same case twice; a reviewer reading the 9 to 12
band against 6 to 8 marks the lens error. Fix: the case swaps in the table (item-level, settled below).

### 4. Owner rows in grades 5 and 8 are thin, and several grade 8 rows sit at grade 5's depth (moderate; firm. LAYER progression. REPEAT new)

33 of 40 grade 5 rows and 16 of 40 grade 8 rows end with the bare "Owner year for 3 to 5." or "Owner year for 6 to 8."
as their only depth statement. The owner row is the band's full depth and the row other subjects lean on, so it
should be the clearest row of the band. Two problems follow.

- **No case, or a case that reads as the student's own life:** g5-rds-good-for-us ("weighs a choice for their own and
  others' well-being when friends push the other way"), g5-soc-their-view ("a friend going through a change"),
  g5-rds-ask-questions, g5-rds-think-ahead ("results of a choice for many people"), g5-rel-friendships, g5-sm-step-forward.
  A writer cannot tell whether the friend is invented.
- **Grade 8 at grade 5's depth.** The 6 to 8 depth is "the strategy chosen among options and weighed against real
  pressures, with the reason written down". Text similarity between the grade 5 and grade 8 owner rows of one
  sub-skill is highest for g5/g8-sm-step-forward (0.77), g5/g8-rel-teamwork (0.75), g5/g8-rel-ask-offer-help (0.69),
  g5/g8-sm-set-goal and g5/g8-rel-lead-follow. g8-sm-step-forward and g8-rel-teamwork name no options and no written
  reason; they are grade 5's rows with "teasing" or "absence" added.

Fix (row edits): give each listed grade 5 row an invented case and replace the bare tag with what the owner year asks,
for example g5-rds-good-for-us: "On an invented case (a friend asks the student to skip the class job to play), the
student weighs both people's well-being with stop-think-choose and picks with a reason. Owner year for 3 to 5: the
choice holds when friends push the other way." For g8-sm-step-forward: "chooses between two first steps (ask the
student council, or start a sign-up sheet) and writes why the chosen one fits the cost". For g8-rel-teamwork: "chooses
among three ways to cover the absent member's part and writes the reason".

### 5. Kindergarten to grade 2 rows with three steps (moderate; firm. LAYER progression. REPEAT new)

STANDARD section 3 (depth ladder) and APPROACH ("two to four steps (one or two in K to 2)") set one or two pictured
steps for K to 2. Five rows set three: **g1-sm-plan-and-tidy** (three-step picture plan), **g1-rel-stand-up** (stand
with them, say "That's not kind", tell a grown-up), **g2-rel-talk-listen** (listen, ask, build on), **g2-rel-say-no**
(say no, give a reason, offer something else), **g2-sm-set-goal** (three-step goal). g3-rel-talk-listen then says
"Grade 2 used three steps". Cost: the frame and the step card for grade 2 contradict the approved approach page, and
a reviewer reading C4 sees two answers.

Fix (settled below): the rows follow the page. g1-sm-plan-and-tidy: "two pictured steps (desk clear, tools out)";
g1-rel-stand-up: "stand with them and say 'That's not kind', then tell a grown-up" as two steps; g2-rel-talk-listen:
"ask a question, then add to the idea" (listening is the K card); g2-rel-say-no: "say no with a reason, then offer
something else"; g2-sm-set-goal: "a two-step goal". g3-rel-talk-listen: "Grade 2 used two steps; saying back is new"
becomes "Grade 2 asked and added; saying back and listening as a named step are new".

### 6. The AASL id placed with SM3 is not taught in grades 3 to 8 (moderate; firm. LAYER progression. REPEAT new)

Library places AASL V.D.1 (trying again when a task gets hard) in SEL "with SM3 in every band"
(docs/courses/library/STANDARD.md section 4; library-excluded.csv). The SM3 rows teach staying on task against
distraction. Trying again when the task itself is hard appears in g2-sm-stay-on-task ("one more try") and
g11-sm-stay-on-task (a restart after a setback) only; no row in 3 to 5 or 6 to 8 has it. Cost: library units in
grades 3 to 8 lean on a skill no SEL row of those bands teaches, and C1 tracing for library fails on V.D.1.

Fix: add to the owner rows. g5-sm-stay-on-task: "...when friends offer something more fun and when the next step gets
hard, using the focus plan and a try-again step (try another way, then ask)". g8-sm-stay-on-task: "...and a try-again
plan for the hardest part of the project, chosen from options with the reason written". g3 and g6 may carry the same
step in practice.

### 7. Disclosure line missing where a case touches a friend's distress (moderate; firm. LAYER progression. REPEAT yes, the kind of health 2026-11-19 finding 10)

STANDARD section 5 item 4 puts health's disclosure steps in every unit's teacher notes, and the progression carries
them row by row on RS8 and SM2 (all grades) and SO3 from grade 8. These rows set a case a child may answer from life
but carry no line: **g3, g4, g5, g6, g7 soc-care-when-struggle** (a friend "having a hard week", "a hard change");
**g2-soc-read-feelings** and **g5-soc-read-feelings** (a friend who says "I'm fine" but is pulling away, a classic
warning sign); **g5-rel-friendships** ("step back from one that is unhealthy, with a trusted adult", with no invented
case). Fix: append the row's usual line ("Teacher note: if a student tells of harm or risk, follow health's steps
(docs/courses/health/APPROACH.md, "If a student tells you something"): the school's reporting route and the
counselor.") to those eight rows, and give g5-rel-friendships an invented case: "an invented friend who will only play
if the student leaves another child out".

### 8. Apartheid filed under "settled facts the courts have ruled on" (minor; firm. LAYER progression. REPEAT new)

**g10-soc-fair-rules** offers apartheid as a case beside school segregation, under the teacher note "settled facts
the courts have ruled on". Apartheid was ended by repeal and a negotiated election, not by a court ruling, so the note
is wrong for that case (C3 a). Fix: "Teacher note: settled history: school segregation was struck down by the
Supreme Court in 1954; apartheid's laws were repealed from 1990 to 1991 and it ended with the 1994 election; current
political disputes are not SEL content." (From memory; the world history row wh2-apartheid holds the sources.)

### 9. Sensitivity read: wording a family, teacher or district could object to (minor to moderate; judgment call. LAYER progression. REPEAT yes, the kind of health 2026-11-19 finding 10)

Read as a fresh sensitivity reader for students, teachers and families. No therapy claim, clinical label, survey,
ranking game, religious framing of calm-down, or group blame was found; every SA1, SA2, SA6, SO6 and RS9 row carries
its rule. These cases could still draw a complaint:

| Row | What could be objected to | Safer replacement |
|---|---|---|
| g12-sm-have-a-say | "a public comment at a school board meeting", not marked invented, and "carries out a part where allowed": real political action steered by the course into a contested venue | an invented graduate's case; examples "a suggestion to a library or recreation center", "a workplace suggestion"; the real action stays a choice (For Cory 1) |
| g7-rel-say-no | "forward a mean edited picture of a student" can read as image abuse | "forward a mean meme that mocks a student's drawing" |
| g7-soc-read-situation | "a weekend invitation from older students" reads as an unsupervised party | "an invitation from older students to sit with them at a game" |
| g1-soc-read-situation | "a friend's birthday party": some families do not keep birthdays | "a visit to the library" |
| g6-rel-ask-offer-help | "a message to a parent" assumes one kind of family | "a message to a family adult" |
| g1-rds-ask-questions | a real classmate asked "how they do something differently" can lead to a child explaining home or culture, which g1-rel-different-ways rules out | "asks a partner how they would build the class tower differently" |
| sa-feel-think-link, g3 to g12 | "catch the thought, test it, try another" is the core move of a talk therapy; a family may read it as therapy in class | keep the skill; add "Teacher note: a thinking skill used on characters, not a treatment; no student is asked to test their own thoughts aloud." |

### 10. Pace: multi-week tasks that outrun the unit, and kindergarten's short path (minor; judgment call. LAYER progression. REPEAT yes, pace was a heading in health and PE 2026-11-19)

Per grade the load is even: 40 rows a grade, 64 sessions (32 on the short path), units of 5 to 8 sub-skills exactly as
STANDARD section 3 places them. Two things the gate cannot see:
- **Tasks longer than their unit.** A unit is 10 or 11 sessions at two a week, about five and a half weeks.
  g5-sm-set-goal sets a six-week goal; g8-sm-set-goal and g9-sm-set-goal set a term goal; so the end-of-unit
  assessment comes before the goal ends. Grade 3 carries seven multi-week trackers (calm-down daily for a week,
  interest log two weeks, gratitude wall two weeks, coat-hook test a week, practice record three weeks, three-week
  goal, two-week routine change) with nothing saying they run outside the two sessions a week. Fix: g5 "a four-week
  goal"; g8 and g9 "a goal checked at the unit's end and carried on as the unit's carry-out cue"; and each grade 3
  tracker row ends "kept between sessions as the unit's carry-out cue".
- **Kindergarten on the short path.** K units 2, 5 and 6 teach eight sub-skills each in three groups; on the short path
  a group's Understanding and Fluency share one 20-minute session, so about three new sub-skills are named and rehearsed
  in 20 minutes by five-year-olds. Fix: none in the progression; the K frame should use the move-a-session option
  STANDARD section 2 gives it and say so.

### 11. Stale note: STANDARD says progression.py still needs four changes (minor; firm. LAYER process. REPEAT yes)

docs/courses/sel/STANDARD.md section 3, end of "Ownership, for the progression": "Before the first SEL check,
scripts/progression.py needs four changes: sel in STD_FILES and ANCHOR ...". All four are done (progression.py
lines 70, 83, 86 and 128 to 130: casel-5.txt in both maps, MULTI_OWNER for grades 2, 5, 8 and 12) and the check passes.
Fix: replace the sentence with "scripts/progression.py checks this form (MULTI_OWNER: one owner per id in each of
grades 2, 5, 8 and 12)."

### 12. Grade 2 carries three leans (minor; likely. LAYER progression. REPEAT new)

Leans per grade: K 6, 1 7, **2 3**, 3 9, 4 13, 5 14, 6 11, 7 11, 8 14, 9 14, 10 8, 11 8, 12 12. Bar item 9 asks each
unit to name one link to that grade's core courses; grade 2's six units have three candidates (ELA discussion, a
health refusal row, a math graph). Fix: before the grade 2 frame, add leans for g2-soc-why-rules and g2-rds-solve-problems
to grade 2 social studies civics rows, and for g2-soc-their-view to the grade 2 ELA point-of-view row, after the frame
writer checks which ids those grades own (I did not choose ids I had not read).

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| Rehearsal clauses on the RS2, RS8, RS9 and g5/g6 SM1 rows, as worded in finding 1 | bar item 5; wording only, no new content | data/progressions/sel.csv |
| Year lines for K, grade 4 and two grade 1 rows, in the forms in finding 2 | STANDARD's own rule for `~` rows | data/progressions/sel.csv |
| The nine grade 11 case swaps in finding 3 | same skill and depth, new invented cases | data/progressions/sel.csv |
| K to 2 rows cut to two steps (finding 5), not the page raised to three | the approved page wins; the third step is said by the teacher as a prompt | data/progressions/sel.csv |
| Try-again step on g5 and g8 sm-stay-on-task (finding 6) | the library placement already decided it | data/progressions/sel.csv |
| Disclosure line on eight rows and a new case for g5-rel-friendships (finding 7) | STANDARD section 5 item 4 | data/progressions/sel.csv |
| The apartheid note text (finding 8) | accuracy | data/progressions/sel.csv |
| Replacements for g7-rel-say-no, g7-soc-read-situation, g1-soc-read-situation, g6-rel-ask-offer-help, g1-rds-ask-questions and the sa-feel-think-link teacher note (finding 9) | wording inside the rules | data/progressions/sel.csv |
| A four-week goal in g5-sm-set-goal; carry-out lines on grade 3 trackers and the g8/g9 term goals (finding 10) | the check must see the goal | data/progressions/sel.csv |
| The stale sentence replaced (finding 11) | process | docs/courses/sel/STANDARD.md |

## For Cory

1. {"q": "SEL grade 12, sub-skill SM7 (having a say in your own life and your group's), row g12-sm-have-a-say: the row asks the student to plan having a say in a community or workplace process, gives 'a public comment at a school board meeting' as an example, and has the student carry out a part where allowed. Everywhere else SEL keeps student voice inside class and school life (bar part 9 item 12; STANDARD section 4 D), and taking part in public bodies is the government course's (social-studies gov-local-action). School board meetings are a contested venue in many districts, and a course that sends students to one can read as steering them. Should grade 12 SEL keep real community or workplace action, or plan it on an invented graduate's case and leave real public action to the government course?", "options": ["Plan it on an invented case; real public action stays in the government course", "Keep real action where allowed, but drop the school board example", "Keep the row as it is"], "pick": "Plan it on an invented case; real public action stays in the government course"}

## Lens checklist, progression layer

| Line (docs/agents/lenses/sel.md) | Mark |
|---|---|
| A grade year that repeats another year of its band with the same cases and depth | Missed in part: grade 4 year lines missing (finding 2); grade 11 reuses grade 8 cases across bands (finding 3); grade 8 rows at grade 5 depth (finding 4) |
| A sub-skill missing from a grade, or met once with no return | Met: 40 in every grade, each assumes the year before |
| Minutes a week not stated; short path drops units | Not applicable (frame); STANDARD section 2 states both |
| No carry-out cue or family activity | Not applicable (unit plan); the grade 3 trackers should be named as carry-out cues (finding 10) |
| A unit a school could not leave out | Met by STANDARD section 5 item 6; rows assume only the same sub-skill a year back |
| Self-management or relationship skills met only by discussion | Missed: RS2, RS8, RS9 from grade 3 (finding 1) |
| A skill's name or steps changed between units of one year | Met: each model grows once a band (K or 1, then 3, 6, 9), in the unit that first uses it |
| A health topic taught as SEL content | Met: substances, sexual health, dating and crisis are pointed to health rows by id in every 6 to 12 SM2, RS6, RS2 and SO3 row |
| A sub-skill above the grade's age (unfair norms before grade 5) | Met: SO6 is playground and club fairness in K to 4; settled history starts in grade 5 |
| No end-of-unit assessment; one that scores a feeling | Not applicable (unit); rows check skills on invented cases, and SA3, SA4, SA7, SA9 follow STANDARD section 5 item 1 |
| Sensitive topic with no teacher note or reporting line | Missed on eight rows (finding 7) |
| Growth mindset as belief alone | Met: every SA8 row says "never belief alone" |
| Calming routines with religious or spiritual framing | Met: every SM2 row says plain body skills |
| A prompt that needs a disclosure | Met in rule; six grade 5 rows are unclear whether the case is invented (finding 4) |
| Role play casting a victim, perpetrator or real classmate | Met: RS5, RS6, RS9 rows keep the teacher or a card in the pressure part |
| An activity that sorts students by identity | Met: none found |
| Clinical labels | Met: none found |
| Product or rating names | Met: invented apps only, no product names |
| Exit ticket asks how a student feels | Met: K notes say a child is never asked how they feel in a check |

## What is right and should not be touched

- The unit placement: all 520 rows sit in the unit STANDARD section 3 gives them.
- The within-band step pattern where it is written: grades 7 and 10 (second person) and 11 (cost) state a real, varied
  change in nearly every row; grade 12 moves every one of its 40 rows past school.
- The seven models: each grows once a band, in the unit that first needs it, and nothing uses a model before it is made.
- The settled-history line: SO6 grows from "only kids with red shirts" (K) to Brown in grade 5 and back to it at more
  depth, always with the court-ruled case first and no current dispute.
- The health hand-off: every SM2 and RS6 row from grade 6 names its health row by id, and every id exists at or
  before the grade.
- The refusal rehearsal (RS6) and the disagreement rehearsal (RS5): the model for finding 1's fix.

## What I could not judge

- Whether the leans' target rows fall before the SEL unit inside the same year (unit order of the other subjects is
  not in their progression rows). All leans are at or before the grade.
- The reading level of words beyond a scan: the K to 3 word lists are oral and fit, but no list is checked against a
  word frequency source.
- Social studies grade 2 ids for finding 12 (not read).

## Sources

No outside source was fetched in this run. The findings rest on the settled pages read in full (ADOPTION-BAR-SUBJECTS
part 9, STANDARD.md, APPROACH.md, the lens) and on the csv itself. From memory: the apartheid dates in finding 8 (repeal
of the main laws 1990 to 1991, first all-race election April 1994) and Brown v. Board of Education (1954); and that
"catch the thought, test it" is the core move of cognitive behavioral therapy (finding 9).

## Confidence

Findings 1, 2, 3, 4, 5, 6, 7, 8, 11: firm (the settled pages and the rows agree on the fault). Finding 12: likely.
Findings 9 and 10: judgment calls.

## Fix pass (2026-11-21)

Applied by a fix agent to data/progressions/sel.csv (190 rows), data/progressions/sel-edges.md and
docs/courses/sel/STANDARD.md section 3. `progression.py check sel`: 520 rows, 0 failures; `stale.py check` passes on
each changed file.

1. Fixed: a rehearsal clause (who plays what, with the I-statement frame, the problem size meter or the support map)
   on all 30 RS2, RS8 and RS9 rows of grades 3 to 12 and on g5 and g6 sm-big-feelings (32 rows); the written choice
   or plan is kept, and grades 9 to 12 run plan, rehearse, judge. RS9 rehearsals keep the teacher or a card in the
   unkind part; g12-rel-stand-up stays a school case with its written carry to a first job.
2. Fixed: year lines on 37 kindergarten rows (what the band starts with), 33 grade 4 rows and g1-rel-different-ways
   and g1-rds-careful-thinking, in varied wording (72 rows).
3. Fixed: the nine grade 11 rows take the replacement cases in the table; g11-soc-read-feelings also gained the
   disclosure line, since its new case is a teammate pulling away.
4. Fixed: every bare owner tag in grades 5 (33) and 8 (16) now says what the owner year adds; the six grade 5 rows
   named have an invented case; g8-sm-step-forward and g8-rel-teamwork choose among options with the reason written.
5. Fixed: g1-sm-plan-and-tidy, g1-rel-stand-up, g2-rel-talk-listen, g2-rel-say-no and g2-sm-set-goal cut to two
   steps; g3-rel-talk-listen's line reworded as given.
6. Fixed: a try-again step (try another way, then ask, or a chosen try-again plan in 6 to 8) in the SM3 rows of
   grades 3 to 8 (6 rows).
7. Fixed: the disclosure line, in the wording the other rows use, on the eight rows named (the child form on
   g2-soc-read-feelings); g5-rel-friendships has the invented case given.
8. Fixed: g10-soc-fair-rules carries the corrected settled-history note.
9. Fixed: g7-rel-say-no, g7-soc-read-situation, g1-soc-read-situation, g6-rel-ask-offer-help and
   g1-rds-ask-questions reworded as given; the thinking-skill teacher note on sa-feel-think-link, grades 3 to 12
   (10 rows). g12-sm-have-a-say left as it is for Cory (For Cory 1); no plain error found in it.
10. Fixed: g5-sm-set-goal is a four-week goal inside its unit; g8 and g9 sm-set-goal are checked at the unit's end and
    carried on as the unit's carry-out cue; the seven grade 3 trackers are kept between sessions as the unit's
    carry-out cue (a short running thread). Kindergarten short path: no row change, as the report says; a note for
    the K frame (move a session to units 2, 5 and 6) added at the end of sel-edges.md.
11. Fixed: the stale STANDARD section 3 sentence now says progression.py checks this form (MULTI_OWNER) and has
    supported SEL since 2026-11-21, and the progression passes it.
12. Fixed in part: two real leans added and listed in sel-edges.md (g2-soc-their-view to ela:e2-points-of-view,
    g2-sm-big-feelings to ela:e2-character-response); grade 2 now has five. Grade 2 social studies has no civics rows
    (its rows are maps, migration, sources and economics), so no lean was added for g2-soc-why-rules or
    g2-rds-solve-problems.

Left for Cory, unchanged: the 18-and-over rule and g12-sm-have-a-say.

## Cory's answers applied (2026-11-22, Desk q-prog-sel-1)

1. A student 18 or over gets the family note and makes their own leave-out or consent choice, one rule for every subject, written once in AGENTS.md ("Rules that bind every job"); the school's own rules still apply.
2. g12-sm-have-a-say now plans voice for an invented recent graduate; nothing is carried out in a real public body, and the school board example is gone. Real civic action stays in the government course (gov-local-action).
3. The grade 12 RS9 row stays a school case with the written carry to a first job. No change.

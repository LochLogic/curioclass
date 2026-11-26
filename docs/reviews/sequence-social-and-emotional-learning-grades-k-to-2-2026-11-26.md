# Scope and sequence read: Social and Emotional Learning, Grades K to 2 (2026-11-26)

Expert cold read (PRODUCTION-PATH step 3, docs/pipeline/briefs/sequence-read.md, with build/scope-writes/AFTERCORE-READ.md).
I did not write this scope and sequence.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/sel.md, ADOPTION-BAR-SUBJECTS.md part 9 (items 1 to 13 and "Fails if"),
  docs/courses/sel/STANDARD.md (section 7, "Shared steps", read in full), data/standards/casel-5.txt (our words for the
  40 codes, which set the parts of each code).
- build/scope-writes/AFTERCORE-BRIEF.md and docs/pipeline/briefs/sequence-write.md (the rules the writer worked to).
- docs/courses/social-and-emotional-learning-grades-k-to-2/scope-and-sequence.md and
  data/plans/social-and-emotional-learning-grades-k-to-2/days.csv (all 192 rows: goals, notes, skills, codes,
  retrieves, assess, school_day), cold.
- The frame (Course in brief, Seams, Models carried, Units table, Course-level checks), the K, 1 and 2 rows of
  data/progressions/sel.csv (assumes and notes for the rows the findings rest on), docs/courses/CALENDAR.md (rule 1 and
  the SEL table rows) and data/plans/calendar.csv for K to 2 (ELA, math, social studies, health, PE units by week).
- For the leans: data/plans/health-grades-k-to-2/days.csv (units 3, 7, 14, 15), and the social studies K, 1 and 2
  days.csv rows for ssk-rules-why, ssk-traditions, ss1-group-rules, ss1-ways-of-living, ss1-community-problems and
  ss2-people-resource.
- The frame read docs/reviews/frame-social-and-emotional-learning-grades-k-to-2-2026-11-25.md and its fixes file (for
  REPEAT tags and settled points).
- Gates: `scripts/sequence.py check` 0 failures for this course; `scripts/frame.py check` 0 failures (unit days by
  year K 60, 1 60, 2 60; 18 units, 192 days); `scripts/frame.py calendar` SEL weeks K 11 and 26, grade 1 9 and 26,
  grade 2 10 and 26, no stagger break; `scripts/stale.py check` prints nothing for this course.
- Sources opened: the Japan Foundation lesson page and the two Ghanaian Ampe pages the frame names (Sources, below).

## Verdict

The scope is sound in its bones: every K, 1 and 2 row sits on a day, every owned code and the three library ids are
carried in grade 2, every first use of a row retrieves its earlier-year row (checked by script against `assumes`),
the checks sit on the frame's and CALENDAR.md's weeks, and the shorter paths keep every unit and assessed part. The
biggest risk is the subject's own guard: in a dozen pair rehearsals the "teacher or card plays the pressure" line
cannot hold for fifteen pairs at once, so in practice a partner voices the dare, the push or the upset part. The one
change that matters most after that is the grade 2 end-of-unit pages, which say "one prompt per code part" but leave
parts of six owned codes unasked (RS8, RS7, SM5, SO6, SA2, RD5), and the RS1 owner-year step (talk when the other
person disagrees) is on no day.

Finding count: 12 (2 high, 4 medium, 6 low).

## Findings, most serious first

### 1. High. Pair rehearsals put a child in the pushing, unkind or upset part

LAYER sequence. REPEAT new.

- **What is wrong.** The guard (AFTERCORE-BRIEF SEL note, frame unit 5, 9, 10, 16 cells, the lens) is that a partner
  never plays an unkind, pushing or abusive part; the teacher or a card does. Many days are pair Fluency or
  Application with that part in the scene, and the note says "the teacher or a card plays the pressure" or "the
  teacher playing the other part": days 43, 44, 45 (two-puppet ball and the fence pressure), 87 and 88 (I-statement,
  "the teacher playing the other part" in pairs), 90 (refusal "against the card's pressure"), 101 (stand-with "with
  the card playing the unkind part"), 154 and 155, 162 and 163 (dare and second push), 165 (unkind part). One teacher
  cannot voice the pressure for fifteen pairs at once, and a card a five- to seven-year-old holds is read aloud by the
  partner, so the likely reading by a busy writer is that the partner says the dare.
- **Why it matters.** It breaks a named guard on the exact days it exists for, and the unit plans will be written from
  these notes.
- **Fix.** One line, written once in the .md ("Every unit") and in each listed day's note: in pair rehearsal the
  teacher (or a teacher-held puppet) voices the pressure, dare, push or unkind line to the whole class, and pairs answer
  it in turn; the partner is the coach, holding the step card and pointing to each step as it is done. Where a scene
  has two children who simply want different things (one seat, one glue stick, the slide), the partner may play that
  side from a scripted, calm line, never upset, unkind or pushing (as day 77 already does for the friendly chatter).
  The observed rehearsals (days 48, 91, 101, 158, 166 and their Check days) keep the teacher voicing the part.
  Confidence: firm (the arithmetic of one adult and fifteen pairs; the guard's own words).

### 2. High. Grade 2 end-of-unit pages claim "one prompt per code part" but leave parts of six owned codes unasked

LAYER sequence. REPEAT yes (each part of each code, a recurring sequence-read finding).

- **What is wrong.** Against casel-5.txt's wording, the listed prompts (and the observed rehearsal) miss these parts in
  the owner year:
  - Day 159: RS8 is "ask for help when you need it, and offer help when others do"; the prompt is "too big for kids"
    only, though day 156 teaches the offer. RS7 is "lead a group well, and know when to follow"; the prompt is
    "leading by giving turns" only, though days 156 to 158 teach following another leader's plan (the row's owner
    step, "following has a cost").
  - Day 178: SM5 is "plan steps, manage time and keep materials in order"; the prompt is "the plan with times", with
    no materials part (day 175 teaches the labeled folder). SA2 includes strengths "from your culture and the
    languages you speak", the part the frame fix settled to teach on the invented bilingual teammate (frame read
    finding 6); the prompt is "a strength and a teammate's", which a writer will meet without it.
  - Day 135: SO6 has two parts, places and groups having different unwritten rules, and some being unfair; the prompt
    asks only who an unfair rule leaves out and its cost.
  - Day 191: RD5 is careful thinking "in school and out of it"; the prompt is "where thinking helped and rushing would
    have cost", with no out-of-school part (day 190 teaches "at school and at home").
- **Why it matters.** Grade 2 is the band's owner year for all 40 codes; the end-of-unit page is the only check for most
  of them (the .md says so in "Owned codes a course-level check does not sample"), so a missing part is a part never
  assessed in the band.
- **Fix.** Add the prompts in "Settled by the expert". To keep the Check session inside about 13 minutes, let the
  observed performance stand for whole codes where the day already names it, and say so in the goal: day 191's
  watched team problem stands for RS4 and AASL.III.D.2; day 146's calm plan for SM2; day 159's I-statement for RS5; day
  167's refusal for RS6; day 135's thank-you card made on day 134 stands as the product for SO5 (so SO5's page prompt
  can go). That keeps each grade 2 page at about eight prompts. Confidence: firm (the code text against the goals).

### 3. Medium. The mid-year checks "reuse" a unit record that the plan has already thrown away

LAYER sequence (the frame's Course-level checks cells are the root; the .md's For the lead 1 already names it). REPEAT
new.

- **What is wrong.** Days 21, 81 and 148 say the frame's calm-down item is not collected again because the unit's record
  (days 18 and 19; 78 and 79; 145 and 146) "stands for it" under collect once. But the Evidence rule, in the .md, the
  frame and day 7's note, throws each unit's class sheet away at the end of its unit, which is days 20, 80 and 147, the
  session before each check.
- **Why it matters.** As written, the check claims evidence that does not exist on the day it is used; a writer will
  either collect it again (the repeat the scope meant to avoid) or claim nothing and leave the frame's item silently
  dropped.
- **Fix.** On days 20, 80 and 147 add to the note: "Keep the calm-down column of the unit sheet until the mid-year
  check's respond day (day 22, 82, 149), then throw it away with the check sheet." Add the same exception once to the
  .md's Evidence bullet, and to For the lead 1 so the frame's Evidence bullet gains it. Confidence: firm.

### 4. Medium. The openings carry three or four retrieval rows plus the calm-down routine in four minutes

LAYER sequence. REPEAT yes (frame read finding 2, the session budget).

- **What is wrong.** The frame's budget, which the .md repeats, is one 4-minute opening: the calm-down routine "together
  with one retrieval item, never two openings". Yet 17 Understanding days list three or four earlier-year rows in
  `retrieves`, all for that opening: days 73, 83, 94, 108, 111, 118, 124, 129, 132, 137, 164, 169, 175, 182 and 188
  (three each) and days 76 and 100 (four each), many with the leave-out bridge's ten minutes on top where it applies.
- **Why it matters.** Rule 2 is met in the data, but a writer cannot fit three retrieval tasks and a calm-down routine
  in four minutes for six-year-olds; the likely result is retrieval in name only, or the teaching block cut, which is
  the bar's practice-by-doing risk.
- **Fix.** Keep one row (the one the day's first new step builds on) in the opening; retrieve each other row at the
  start of its own modeled step in the 13-minute teaching block, as "the kindergarten (grade 1) step, then one more",
  which is how a grade-up step is taught anyway. Say this once in the .md's Readiness and retrieval bullet and in each
  listed day's note ("Opening: X; Y and Z retrieved as their steps are modeled"). The `retrieves` column stays as it is.
  Confidence: likely (arithmetic against the frame's own budget).

### 5. Medium. RS1's owner-year step, talk when the other person disagrees, is on no day

LAYER sequence. REPEAT yes (an owner code met in part at the owner year, frame read finding 6 and lesson 4).

- **What is wrong.** The frame's Seams row and g2-rel-talk-listen's notes both set grade 2 as "talk when the other person
  disagrees". Days 129 to 131, 134 and 135 teach and check ask and add in a planned talk about class rules; none has a
  partner idea the child disagrees with. RS5 (unit 15) handles a disagreement with the I-statement, which is a
  different code.
- **Why it matters.** RS1 is owned here; the step that marks grade 2 off from grade 1 is the one missing, so grade 2's
  RS1 is grade 1's at a new topic.
- **Fix.** Day 131's planned talk includes one partner idea the child does not agree with, met with the talk turn card
  ("I hear ___; I think ___ because ___"); day 134's observed talk and day 135's rehearsal look-for include it.
  No day added. Confidence: firm.

### 6. Medium. The disclosure route is missing from nine units' days

LAYER sequence. REPEAT new.

- **What is wrong.** The lens says the school's reporting route and the counselor are named in every unit's teacher
  notes, and the frame's Disclosure bullet says every unit follows health's steps. The days name them in units 1, 2, 5,
  8, 9, 10, 14, 15 and 16 only. Units 3 (the true action, the private page), 4 (a hurt and a caring action), 6, 7, 11
  (families, friends, sorry), 12, 13 (a friend's broken rule hidden), 17 (the private page) and 18 have none. The .md's
  "where the frame names one" reads the frame narrower than it is.
- **Why it matters.** The unit plan builds its teacher notes from the day notes; units 4, 11 and 13 are the likely places
  a young child tells something.
- **Fix.** Add the standard line ("Disclosure: health's steps (docs/courses/health/APPROACH.md, 'If a student tells you
  something'): the school's reporting route and the counselor.") to the first Understanding day of units 3, 4, 6, 7, 11,
  12, 13, 17 and 18 (days 23, 31, 53, 65, 105, 118, 129, 169, 182), and change the .md to "in every unit". Confidence:
  firm.

### 7. Low. Three K and grade 1 end pages ask part of a sub-skill or bundle four in one prompt

LAYER sequence. REPEAT yes (each part of each id).

- **What is wrong.** Day 19 asks "pick the ready, tidy, keep-going and 'I choose' pictures" as one prompt for SM6, SM5,
  SM3 and SM7, against the goal's "one prompt per sub-skill". Day 49 asks RS3 as "one way a game from another place is
  the same", but the row and days 46 and 47 teach one way different and one way the same. Day 92 asks RS7 as "what a
  good leader asks", leaving out the follower who shares an idea (days 89 to 91).
- **Fix.** In "Settled by the expert". Confidence: firm.

### 8. Low. The once-a-week path for kindergarten unit 2 does not add up as written

LAYER sequence. REPEAT new.

- **What is wrong.** The .md says the twelfth sessions fold into their group's shared session, "keeping each
  Understanding at three phrases or fewer by moving SM3 and SM7 into day 17's shared session". On the short path, group
  3 has one shared session (unit 2 runs 3 shared, 2 Application, 1 Check and Respond); there is no separate "day 17"
  session, so either group 3's shared session holds four new phrases (over the cap) or the unit runs seven sessions.
- **Fix.** Spell out unit 2's six short-path sessions: (1) group 1 shared; (2) group 2 shared; (3) group 3 shared with
  SM6 and SM5; (4) Application for groups 1 and 2, with SM3 and SM7 named and modeled in its first minutes on the
  center-time task (they are one-step pictured phrases); (5) Application for group 3, observed calm-down steps;
  (6) Check and Respond. Say that SM3 and SM7 are first scored only in session 6. Confidence: likely.

### 9. Low. Day 176 is typed Fluency but does the real project, and the "two-day" project has one day

LAYER sequence. REPEAT new.

- **What is wrong.** Day 176's goal is "the class works its two-day project plan with times and folders, and starts the
  book swap shelf": a real class task, which GLOSSARY and the frame's Kinds of day call Application. No second project
  day is named, though SM5's row and day 175 say "a two-day class project". (Day 125 is the same in a smaller way: it
  "sets up the help it chose".)
- **Fix.** Day 176 rehearses: pairs make a picture-and-word plan with times for a practice project card and file its
  pieces in a labeled folder, then start the class plan. Day 177's note names the class project's second day as
  the carry-out time between days 176 and 177 (the book swap shelf started then). Confidence: likely.

### 10. Low. Grade 1's refusal words drop "say it again"

LAYER progression and sequence. REPEAT new.

- **What is wrong.** Day 89's note (and the g1-rel-say-no row) quotes health grade 1 as "say stop, move away, tell".
  Health grade 1 unit 7 (health days.csv day 35) teaches "say stop, say it again, move away, tell", and STANDARD section
  7's second-push words are "say it again, move away, tell".
- **Fix.** Day 89's note quotes the shared words, "say it again, move away, tell", for the second push; For the lead:
  g1-rel-say-no's note gets the same words. Confidence: firm.

### 11. Low. Two .md statements are stale against the days

LAYER sequence. REPEAT new.

- **What is wrong.** (a) "Every unit names its carry-out cue and family activity (on its Respond day)": the cue is on an
  earlier day in units 2, 4, 8, 11 and 17 (days 14, 33, 75, 110, 177). (b) The grade 2 mid-year check now holds three
  items (RS1, SO6, one grade 1 row) after the calm plan item was reused, while the .md justifies the unsampled list by
  "the frame's check form ... holds five or six items".
- **Fix.** (a) "names its carry-out cue (on the day it starts) and its family activity (on its Respond day)". (b) Use one
  freed slot for SA4 (Settled by the expert) and move SA4 out of the unsampled list. Confidence: firm.

### 12. Low. Cases repeat across the band

LAYER progression and sequence. REPEAT new.

- **What is wrong.** The SEL note says settled cases do not repeat within a band. The class rewrites an unfair club rule
  in grade 1 (day 113) and again in grade 2 (day 134); the snap-judgment case is a newcomer in all three years (days 34,
  100, 164); a class thank-you to a school helper is made in kindergarten (day 36) and grade 2 (day 134). Depth grows
  (grade 2 adds a cost), so this is not a repeated year, but the task and case are the same.
- **Fix.** Grade 2's rewrite (day 134) is of a recess game rule, not a club rule; grade 2's snap judgment (day 164) rests
  on a different neutral trait (a child who is quiet at lunch), not a newcomer; the grade 2 thank-you goes to a town
  helper outside the school, as the row's owner step says. For the lead: the g2-soc-fair-rules note says "a club and a
  recess game". Confidence: judgment call.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Pair rehearsals: the teacher (or a teacher-held puppet) voices every pressure, dare, push or unkind line to the class; the partner coaches with the step card; a calm, scripted "other side" in a plain disagreement is allowed | Keeps the guard with one adult and fifteen pairs (finding 1) | days.csv days 43 to 45, 87, 88, 90, 101, 154, 155, 162, 163, 165; .md "Every unit" |
| Day 159 page: add "who offers help on a small problem" (RS8) and "following a plan that was not your idea" (RS7) | Both parts are owned and taught on days 156 to 158 | days.csv day 159 |
| Day 178 page: add "where the plan's materials go" (SM5) and "a strength the invented teammate's two languages give her" (SA2) | Owned parts taught on days 175 and 169 | days.csv day 178 |
| Day 135 page: add "two groups with different rules" (SO6); SO5's prompt replaced by the day 134 thank-you card as product | SO6's first part; time freed for it | days.csv days 134, 135 |
| Day 191 page: RD5 prompt reads "at school and at home" | RD5's second part, taught on day 190 | days.csv day 191 |
| Observed performances stand for RS4 and AASL.III.D.2 (day 191), SM2 (146), RS5 (159), RS6 (167), said in each goal | Keeps grade 2 pages near eight prompts | days.csv days 146, 159, 167, 191 |
| Day 131 and days 134 and 135: one partner idea the child disagrees with, met with the talk turn card | RS1's owner-year step | days.csv days 131, 134, 135 |
| Days 20, 80, 147: keep the unit sheet's calm-down column until the mid-year check's respond day | Makes collect once true | days.csv days 20, 80, 147; .md Evidence |
| Openings hold one retrieval row; the others are retrieved at the start of their own modeled step | Fits the 4-minute opening | days.csv the 17 days in finding 4; .md Readiness and retrieval |
| Disclosure line on days 23, 31, 53, 65, 105, 118, 129, 169, 182 | Every unit | days.csv; .md "Every unit" |
| Day 19 page: four prompts for SM6, SM5, SM3, SM7; day 49: RS3 asks one way different and one way the same; day 92: RS7 adds the follower's idea | One prompt per sub-skill | days.csv days 19, 49, 92 |
| Grade 2 mid-year check (day 148) adds SA4, the honest action and its cost, on a new case | Uses the slot freed by the reused calm plan; moves SA4 into the sampled list | days.csv days 148, 149; .md Course-level checks |
| Kindergarten unit 2's six short-path sessions as in finding 8 | Keeps the three-phrase cap | .md Shorter path |
| Day 176 rehearses the timed plan and folder on a practice card; the class project's second day is the carry-out time before day 177 | Fluency by GLOSSARY; the "two-day" project gets its two days | days.csv days 176, 177 |
| Day 89 quotes "say it again, move away, tell" | The shared card's words | days.csv day 89 |
| Grade 2 day 134 rewrites a recess game rule; day 164's snap judgment rests on a quiet-at-lunch child | No repeated case in the band | days.csv days 132 to 135, 164 |

## For Cory

- None. Nothing here changes scope, money, people or audience.

## For the lead

- Frame, Evidence bullet: the calm-down column exception (finding 3), beside the scope's own For the lead 1.
- Progression: g1-rel-say-no's quoted words (finding 10); g2-soc-fair-rules "a club and a recess game" (finding 12).
- The scope's For the lead 2 (unit 18 group 2 typed Application) and 3 (codes empty in K and grade 1) are right as
  written; I agree with both.

## The lens checklist (scope and sequence layer)

| Line | Verdict |
|---|---|
| Self-management or relationship skills met only by discussion, with no rehearsal | Met: every group rehearses; at risk only from finding 4's crowded openings |
| A skill's name or steps changed between units of one year | Met, but grade 1's refusal words differ from the shared card (finding 10) |
| A health topic taught as SEL content rather than pointed to | Met: RS6 points to health for body safety and substances on days 42, 89, 161; RD6 uses everyday class choices |
| A sub-skill taught above the grade's age | Met: SO6 is playground and club fairness, SO8 class, school and town rules, no past or current dispute |
| Unit lines checked early (no end-of-unit assessment, a feeling scored, a sensitive topic with no route) | End assessments met and score steps, never feelings; disclosure route missed in nine units (finding 6) |

## Checked and right (do not touch)

- Every K, 1 and 2 row (120) sits on a day; every grade 2 code and the three library ids are on days and on an end
  page. Every first use of a grade 1 or grade 2 row has its earlier row in `retrieves` on that day (script check, no
  misses), and no row is retrieved before it is taught. No readiness check is needed past day 1 (every assumed row was
  used the year before), and none sits on a later unit's first day.
- Course-level checks: K 21 and 22 (week 11), 51 and 52 (26); grade 1 81 and 82 (9), 116 and 117 (26, 27); grade 2 148 and
  149 (10, 11), 180 and 181 (26, 27), matching the frame and CALENDAR.md, with no stagger break. Each check right after a
  unit's end draws on earlier units and says so in its goal and note. The list of owned codes no check samples is
  complete (43 of 43 accounted for).
- school_day: ceiling(5n/2) per year, offsets 160 and 320, sessions on the third and fifth day of each week; every unit
  falls in the frame's weeks.
- Leans, checked against calendar.csv and the other subjects' days: social studies K units 1 and 5, grade 1 units 1 and
  6, grade 2 unit 3 and math K unit 2, grade 1 unit 1, grade 2 unit 1 come before the SEL day; health grade 1 unit 7's
  help and stop steps (health weeks 5 and 7) come before days 83 and 89; health grade 2 unit 14's boundary steps come
  before day 161; ELA's later units carry the frame's bridge (days 9, 73, 150).
- Shared cards word for word in their band form (talk turn, calm-down by year, I-statement with grade 2's "What do you
  need?", goal steps by year), except finding 10.
- Every Candidate cell is settled at 0 days with its reason; the leave-out bridges are placed on the right first
  Understanding days.
- The 10-days-short path: 12 named Fluency fold-ins (4 a year, 80 minutes a year), none assessed, every owned part kept.
- Equity and sensitivity: families of every kind on the model pages, no child asked about a family or culture,
  invented cases for SA4, SA6 on neutral traits, private pages never recorded, no clinical words, no spiritual framing
  of the breath, timers as a pace cue only.

## What I could not judge

- Whether ELA K unit 2, grade 1 unit 2 and grade 2 units 1 and 4 hold the exact rows the frame names (I read their unit
  weeks in calendar.csv, not their days).
- Health K to 2's own school_day numbering: its days.csv appears to count each year from a different offset than this
  course's 160 a year; the weeks I compared come from calendar.csv, which agrees with the leans above. The lead may want
  to confirm health's offsets at the calendar regeneration.

## Sources

- The Japan Foundation, Erin's Challenge, lesson 7 "Let's try", https://www.erin.jpf.go.jp/en/lesson/07/let-us-try
  (opened 2026-11-26): describes the game (spelled "atchi muite hoi") played after a rock, paper, scissors round, with
  pointing and turning the face, no touching. Supports days 111 and 112.
- Tema International School, Ghana,
  https://www.tis.edu.gh/2017/05/19/service-in-action-myp-grade-7-8-engagement-with-calvary-presby-school/ (opened
  2026-11-26): describes Ampe as a Ghanaian game of jumping together, clapping and putting one foot forward on landing,
  mostly played by girls. Supports days 46 and 47.
- myjoyonline, Ghana Month Ampe article,
  https://www.myjoyonline.com/ghana-month-the-game-that-requires-you-to-make-quick-decisions-with-your-legs/ (opened
  2026-11-26): names Ampe as a quick-decision leg game mainly played by girls, but does not describe how it is played.
- Web Japan traditional games page, https://web-japan.org/nipponia/nipponia26/en/topic/: browser check (not opened).
- CPSC Public Playground Safety Handbook: not reopened; the frame read opened its title page.

Confidence overall: findings 1 to 3, 5 to 7 and 10 firm; 4, 8 and 9 likely; 12 a judgment call.

## For the source list

- The myjoyonline Ampe page names the game but does not describe the play; the Tema International School page is the
  one that does. The sensitivity read should lean on the second, and note that Ampe is mostly played by girls in Ghana
  so the class page can say so without making it a girls-only game in class.

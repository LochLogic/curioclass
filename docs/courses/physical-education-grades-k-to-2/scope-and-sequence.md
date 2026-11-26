# Scope and sequence: Physical Education, grades K to 2

Course `physical-education-grades-k-to-2`, a band course for kindergarten, grade 1 and grade 2. Draft, written
2026-11-26 from the frame (docs/courses/physical-education-grades-k-to-2/frame.md) and fixed the same day after the
expert read (docs/reviews/sequence-physical-education-grades-k-to-2-fixes-2026-11-26.md). The days are in
data/plans/physical-education-grades-k-to-2/days.csv (written by
build/scope-writes/scratch/physical-education-grades-k-to-2/make_days.py, then fix_2026-11-26.py in the same folder); this page holds the judgment.

## The band, the standards and the calendar

- **Three years, one file.** Year K is course days 1 to 80, year 1 days 81 to 160, year 2 days 161 to 240. Each
  year has 74 unit days and 6 course-level days (two check days and one respond day at mid-year, the same at
  year-end). `stretch` is the unit number in the frame's Units table (1 to 7 in K, 8 to 14 in grade 1, 15 to 22 in
  grade 2); course-level days have stretch `C` and no unit.
- **Which grade's standards fall in which year.** SHAPE America 2024 has one span-2 set of 49 indicators
  (SHAPE.S1.2.1 to S4.2.10). Each is owned by one progression row of one grade, so it is claimed in that row's year:
  year K claims the indicators named in the kindergarten outcome below, year 1 the grade 1 ones, year 2 the grade 2
  ones. A `~` code on a day is begun there or used in a new setting; the owning unit is named in the day's note.
  S1.2.1 (begun in K unit 1, owned in grade 1 unit 8), S1.2.6 and S1.2.9 and S1.2.16 (begun in K unit 5, owned in
  grade 1 unit 11, grade 2 units 16 and 18) are the indicators that climb across years.
- **Grade outcomes** are the frame's, copied: kindergarten S1 (S1.2.2, S1.2.4, S1.2.5, S1.2.7, S1.2.8, S1.2.10,
  S1.2.11, S1.2.13), S2 (S2.2.1, S2.2.6, S2.2.10), S3 (S3.2.3, S3.2.4, S3.2.7), S4 (S4.2.1, S4.2.3, S4.2.8);
  grade 1 S1 (S1.2.1, S1.2.3, S1.2.6, S1.2.12, S1.2.15), S2 (S2.2.3, S2.2.5, S2.2.8, S2.2.9), S3 (S3.2.1, S3.2.2,
  S3.2.5, S3.2.10), S4 (S4.2.2, S4.2.4, S4.2.7, S4.2.9); grade 2 S1 (S1.2.9, S1.2.14, S1.2.16, S1.2.17), S2
  (S2.2.2, S2.2.4, S2.2.7, S2.2.11, S2.2.12), S3 (S3.2.6, S3.2.8, S3.2.9), S4 (S4.2.5, S4.2.6, S4.2.10).
- **Meeting days and `school_day`.** One 30-minute session, 2.5 a week on average, over 32 weeks a year.
  `school_day` is counted across the band as 160 school days a year: course day n of year y (y = 0 for K, 1 for
  grade 1, 2 for grade 2; n = 1 to 80) is school day **160 x y + 2n**, so the week is
  (school_day - 160 x y - 1) // 5 + 1 and course day n falls in week ceil(2n / 5). This is the frame's even spread
  ("course day d falls on about school day 2d"); no pins. Every unit sits in the frame's weeks and every course check
  in the frame's check weeks (checked by script on all 240 days): K mid-year week 18, K year-end week 28, grade 1
  weeks 18 and 28, grade 2 weeks 17 and 27, with grade 2's respond days in weeks 18 and 28.
- **Calendar rule.** PE is a special in K to 5, so CALENDAR.md rule 1's stagger does not count it (DESK-ANSWERS
  2026-11-26). Even so, no PE check day sits in a core check week of its grade (K 14 to 17, 29 to 32; grade 1 14
  to 16, 19, 29 to 32; grade 2 14 to 16, 18 to 20, 28, 29, 31, 32). Unit end checks are not course-level checks;
  some fall in core weeks (for example K unit 4's check, week 17), which the rule allows.
- **The session.** Every day's 30 minutes hold the instant activity, warm-up, focus, cool-down and closure, with
  about 3 minutes of set-up and put-away done by station groups. No lines, no elimination, no human targets, no
  public picks, no split by gender, no exercise as punishment.
- **Safe space and equipment in every note.** Every movement day's note names its space, its equipment and the
  no-equipment path (the frame's low-equipment version: rolled socks, paper-plate paddles, tape and chalk, string
  ropes), the water break and shade on warm outdoor days where the unit runs outside, and the Required access items
  (a soft surface in units 2, 9 and 15; real child life jackets in unit 22). The wet-weather version of every unit is
  the cleared room with the same stations; units 14 and 20, which want the most space, shrink the play area and keep
  the no-one-out rule.

## Assessment pattern

- **Baseline.** Each unit's first skill day carries a baseline watch of the unit's main cue in six rotating groups
  (met, partly, not yet), never scored. Where the unit's first day is its hook and teaches the skill too, the watch
  of the first try is the baseline and the day still holds no scored task.
- **End of unit.** Units over 10 days (1, 3, 5, 9, 10, 13, 22) have two check days, groups 1 to 3 then 4 to 6, so
  each child is watched once; units of 10 days or fewer have one check day holding one skill task and a knowledge
  prompt, and where the frame names a second skill task it is the closure watch of the unit's last Fluency day,
  carried as a mark (units 2, 4, 11). Conduct is marked once against the S3 behavior the unit names, from practice.
- **Parts of a code.** The checks ask every part of a code the unit claims: S2.2.3 (grade 1 unit 8) and S2.2.4
  (grade 2 unit 21) are asked in traveling, in place and with an object; S1.2.1 (unit 8) asks a change of pathway,
  direction and speed. The "several in-place practice tasks" indicators of span 2 (S1.2.6 to S1.2.14) each rest on
  at least two tasks of the same indicator: the end task, and a second in-place task recorded at the owning unit's
  last Fluency day as its closure watch, carried as a mark and named on the check day (day 31: a roll to a seated
  partner and a bounced-ball catch; day 40: taps a few steps forward and a kick to a partner; day 56: a self-dropped
  ball struck with the paddle; day 120: a bounce to a wall and back and a balloon hit with a partner; day 178: a
  throw to a partner; day 210: a self-dropped ball struck with the long tool). No day is added.
- **Respond days** follow every unit check except unit 20's (the frame gives it none): unit 21's day 1 instant
  activity takes unit 20's "not yet" tactic.
- **Course-level checks** sample earlier units at new stations; see the section below.

## Readiness and retrieval

No row assumes one two or more grades back, so the course has no readiness checks. Every assumed row is retrieved
in the instant activity of the first skill day that needs it, as the frame says. The `retrieves` column lists only
PE skill ids; retrieval of another course (health, SEL, dance, math, social studies) is named in the note. Day 1 of
every unit stays clean for the hook and the question: the retrieval there is a short instant activity on an earlier
cue, not a check, and nothing on day 1 is scored. A child who joins in grade 1 or 2 meets the same retrieval tasks
and the teacher re-teaches the cue on the spot.

## Shared cards

Quoted in the band's form from SEL STANDARD section 7, "Shared steps":

- **Calm-down card.** Kindergarten: "stop, breathe" (the balloon breath). Grade 1 adds: count to five. Grade 2 adds:
  a stretch or asking for a break, chosen by the moment. PE uses it in unit 11 (grade 1 form) and unit 22 (grade 2
  form), and reviews it in unit 14.
- **Goal steps card.** Kindergarten: "my goal and one step". Grade 1 adds: "a helper and a check". Grade 2 adds: "a
  changed step". PE uses it in unit 5 (K form), unit 14 (grade 1 form) and units 16 and 22 (grade 2 form). PE's own
  words "pick, practice, check" are the actions done on those rungs, never a second card (For the lead 2).
- **Team talk** uses health's conflict steps word for word (health K to 2 unit 14, grade 2 weeks 13 to 18, which
  comes later in the year and teaches the same steps): "stop, say what happened, listen, find a fair way, an adult
  helps when words do not work". Trying the fair way is what the group then does, never a printed step. Unit 17
  teaches it (days 183, 185, 189); unit 19 reviews it (day 207).

## Year K (kindergarten ids)

### Unit 1. My space, my moves

Days 1 to 13 (weeks 1 to 6). The safe-space bubble and the signals come first because every later unit needs them;
the cue-words idea is taught on jump and land (day 2), the simplest fixed-spot skill, before traveling uses it (days
4 to 7). Sharing phrases (day 6) come before the turn-taking stations (day 8). Candidate settled: the freeze-and-go
game with no one out is kept as the Application (day 9). Checks days 11 and 12 (two days, 13 days in the unit),
with the conduct mark asking all of S3.2.4: stops on the signal and acts on one cue the teacher gives; respond day 13. Safety: no racing, soft landing surface, one direction of travel at first.

### Unit 2. Still and in place

Days 14 to 23 (weeks 6 to 10). Still balances before in-place moves, because a held balance is the freeze the
in-place sequence ends on. Knee and hands-down balances only on a soft surface (Required access). Candidate settled:
the statue game is kept (day 16). One check day (22) with the four in-place moves carried from day 21's closure
watch; respond day 23.

### Unit 3. Roll and catch

Days 24 to 34 (weeks 10 to 14). The equipment rules open the unit with the roll because this is the first unit
with a ball a pair; catching follows (day 26), then the partner toss (day 29) once both are in hand. Candidate
settled: roll-to-the-pins is kept as a station (day 28; on the shorter path it folds into day 31's stations).
Checks days 32 and 33; respond 34. Balloon allergy check before any balloon.

### Unit 4. Feet on the ball

Days 35 to 42 (weeks 14 to 17). Kick before taps: the still-ball kick reuses unit 3's "look at the target", taps
need a count to ten, which math K unit 1 has given by week 14. Candidate settled: kick to a named colored cone is
kept (day 39). One check day (41) with the ten-taps mark carried from day 40; respond day 42. The check falls in a
core check week (17), which is allowed for a unit check of a special.

**Kindergarten mid-year check:** days 43 and 44 (week 18), respond day 45.

### Unit 5. Strike, bounce, toss, choose

Days 46 to 59 (weeks 19 to 24). Paddle striking first (balloon, then tee), then three first meetings of skills
owned later (bounce, toss, rope), then choice stations with the goal steps card's first rung: the child needs
stations to choose from before choosing. The early tries are marked as growth only. Candidate settled: the balloon
keep-up count against the child's own first try is kept (day 55), the count private. Checks days 57 and 58; respond
59. Safety read (striking tools).

### Unit 6. Moving makes me strong

Days 60 to 67 (weeks 24 to 27). Opens with health's heart fact as retrieval (health K to 2 unit 2, weeks 6 to 11),
then the effort faces and the picture sort. Candidate settled: the home-activity picture card is kept with no day
cost, sent home with the family note (day 64). One check day (66) holding the travel-and-freeze skill task and the
knowledge prompts; respond 67. Sensitive: bodies (no weighing, no body talk).

**Kindergarten year-end check:** days 68 and 69 (week 28), respond day 70. Travel and freeze is reused from day 66
(four school days before) rather than watched again.

### Unit 7. Moving and feeling

Days 71 to 80 (weeks 29 to 32), after the year-end check, as the frame places it. Animal walks first (a feeling in
the whole body), then the scarf dance and how moving helps us feel well; review stations of units 1 to 5 thread
through so the year closes with every cue practiced. Candidate settled: the picture wall with no names is kept (day
77). One check day (79); respond 80 closes the year. Sensitive: emotions.

## Year 1 (grade 1 ids)

### Unit 8. Ways to travel

Days 81 to 90 (weeks 1 to 4). Kindergarten's traveling cues are retrieved first; pathway, then direction and
speed, then the movement words in the three parts S2.2.3 names (traveling, in place, with an object) on days 84 and
85. Candidate settled: the class floor map is kept (day 87). One check day (89); respond 90.

### Unit 9. Jump, balance, shift

Days 91 to 101 (weeks 5 to 9). Weight shifts on mats before jumping a still rope and holding the landing, then a
first self-turned swing. Candidate settled: the three-shape balance story is kept (day 97). Checks 99 and 100;
respond 101. Required access: mats or carpet. Safety read (mats).

### Unit 10. Send and receive

Days 102 to 112 (weeks 9 to 13). The underhand toss builds on kindergarten's roll and catch; feelings faces and
cheering (day 103) come before the partner work leans on them, and kindness after a miss (day 106) before the
pair target game. Candidate settled: the pair target game, where the pair counts, is kept (day 107). Checks 110
and 111; respond 112.

### Unit 11. Bounce, hit, stay calm

Days 113 to 122 (weeks 14 to 17). Bouncing first, then the calm-down card in its grade 1 form (SEL K to 2 unit 8
has taught it, weeks 5 to 8), then the hand strike, so a missed balloon is the first real use of the calm step.
Candidate settled: the calm-step card in a pocket of the child's own sheet is kept (day 119). One check day (121)
with the balloon mark carried from day 120; respond 122. Sensitive: emotions.

**Grade 1 mid-year check:** days 123 and 124 (week 18), respond day 125.

### Unit 12. Feet, tools and a strong heart

Days 126 to 135 (weeks 19 to 22). The pulse-check opens the unit (health K to 2 unit 9 runs the same weeks; neither
waits); kick, tap and tee are kindergarten skills in new settings; "active often" comes after a week of pulse
counts. Candidate settled: the private before-and-after heartbeat drawing is kept (day 131). One check day (134);
respond 135. Sensitive: bodies. Safety read (striking tools).

### Unit 13. Dance to the beat

Days 136 to 147 (weeks 23 to 27). The dance course's grade 1 elements (dance K to 2 unit 5, weeks 1 to 9) are
retrieved; PE takes only the motor skill. Beat and shapes first, then Seven Jumps (Denmark and the Netherlands),
then La Raspa (Mexico), each named by its place with its source line, teacher-set partners, no gender roles.
Candidate settled with a condition (day 143): a family's dance may replace one of the three only when its own source
says it is open to be taught. Checks 145 and 146: the pattern takes its moves from two of the unit's dances,
named on the check card, so S1.2.15's range of styles is asked; respond 147. Sensitivity read before the unit names a dance.

**Grade 1 year-end check:** days 148 and 149 (week 28), respond day 150.

### Unit 14. Games from many places

Days 151 to 160 (weeks 29 to 32). Mugunghwa (Korea) and Doña Blanca (Mexico), both no-one-out; social studies
grade 1 unit 5 has shown the world map. One activity to do with others (S4.2.2) and a favorite, alone or with others (S4.2.4), each with its own
prompt on day 159, then the star and wish on the goal steps
card's grade 1 rungs. Candidate settled: the family games book is kept as an optional page sent home, only with
family consent, no day cost (day 157). One check day (159); respond 160 closes the year. Sensitivity read before
the unit names a game; Mugunghwa is never tied to any television show. Mugunghwa's source is unconfirmed: the
ministry page the frame cites does not name the game in its text (expert read 2026-11-26), so the sensitivity agent
finds a Korean folk-culture source first (browser check: the National Folk Museum of Korea's Encyclopedia of Korean
Folk Culture).

## Year 2 (grade 2 ids)

### Unit 15. Circuit sequences

Days 161 to 170 (weeks 1 to 4). Grade 1's traveling, jump and weight-shift cues are retrieved into one three-part
sequence; why we stretch comes after the warm-up habit is in place. Candidate settled: the partner circuit card is
kept (day 166). One check day (169); respond 170. Required access: mats. Safety read (mats).

### Unit 16. The overhand throw

Days 171 to 180 (weeks 5 to 8). The throw first, then the goal steps card in its grade 2 form on the throw.
Candidate settled: the private goal card is kept (day 176), never posted. One check day (179); respond 180.

### Unit 17. Ball skill stations

Days 181 to 190 (weeks 9 to 12). Six earlier codes in new stations, each child on their own cue; team talk in
health's five steps, word for word (taught here first in the year; health K to 2 unit 14 and SEL K to 2 unit 15 come
later and teach the same steps). The check asks all five steps, the adult-help step included.
The puppet plays the problem, never a child against another. Candidate settled: the picture rotation card is kept
(day 185). One check day (189); respond 190. Safety read (striking tools).

### Unit 18. Jump the rope

Days 191 to 200 (weeks 13 to 16). Self-turned rope, then food and drink for play (health K to 2 unit 12 retrieved;
no good or bad foods, no body talk), then the long rope. Candidate settled: the counting chant is kept (day 195).
One check day (199); respond 200.

**Grade 2 mid-year check:** days 201 and 202 (week 17), respond day 203 (week 18, a math check week: practice only).

### Unit 19. Long-handled striking

Days 204 to 212 (weeks 18 to 21). The level swing, then why striking rules keep people safe and fair (SEL K to 2
unit 13 retrieved), then fair choices with team talk. Candidate settled: the class's own picture rules are kept (day
209). One check day (211); respond 212. Safety read (striking tools).

### Unit 20. Chase and flee

Days 213 to 218 (weeks 22 to 24). The tactics question is the model; tag with no elimination. Candidate settled:
freeze tag with a jump task and rejoin is kept (day 215). One check day (218); no respond day (frame): unit 21's
day 1 instant activity takes the "not yet" tactic.

### Unit 21. Dance sequences

Days 219 to 225 (weeks 24 to 26). Kinderpolka (Germany) and Paw Paw Patch (US play-party game); the dance course's
grade 2 elements are retrieved and PE takes only the motor skill. Day 220 teaches S2.2.4 in all three parts.
Candidate settled: partners teach each other their sequence (day 223, also the closure watch). One check day (224);
respond 225. Sensitivity read before the unit names a dance.

**Grade 2 year-end check:** days 226 and 227 (week 27), respond day 228 (week 28, a science check week: practice
only).

### Unit 22. Safe near water, and looking back

Days 229 to 240 (weeks 28 to 32). Dry land only: life jacket, reach and throw, floating and kicking shown on the
floor, after health K to 2 unit 13's water rules are retrieved. Then a personal difficulty with the calm-down card's
grade 2 form, and a look back across K to 2. Candidate settled: the family water-safety card is kept with no day
cost (day 236). Checks 238 and 239; respond 240 hands the band's records on to grades 3 to 5. Required access: real
child life jackets. Safety read (water). Sensitive: water and emotions.

## Course-level checks

| Check | Course days | Week | After unit | Samples | Respond |
|---|---|---|---|---|---|
| K mid-year | 43, 44 | 18 | 4 | Units 1 to 3: land soft, a balance and in-place moves, a roll and a catch; knowledge: show your space; conduct: stops on the signal, takes turns | 45 (week 18) |
| K year-end | 68, 69 | 28 | 6 | Units 1 to 5: kick, foot taps, tee striking, one early try; travel and freeze reused from day 66; knowledge: the non-kicking foot, the safe swing space; conduct: keeps trying at a chosen station, handles equipment safely | 70 (week 28) |
| Grade 1 mid-year | 123, 124 | 18 | 11 | Units 8 to 10: three traveling ways, three weight-bearing shapes, an underhand toss; knowledge: a movement idea and a partner's feeling from a face card; conduct: an encouraging word | 125 (week 18) |
| Grade 1 year-end | 148, 149 | 28 | 13 | Units 8 to 12: a bounce, a balloon keep-up, a kick, a tee hit; knowledge: the heart is a muscle, one way being active often helps; a calm step for a pictured moment; conduct: acts kindly | 150 (week 28) |
| Grade 2 mid-year | 201, 202 | 17 | 18 | Units 15 to 17: a three-part sequence, three overhand throws per cue, one station; knowledge: a reason to stretch, the team-talk steps; conduct: shares the station and its equipment with words | 203 (week 18) |
| Grade 2 year-end | 226, 227 | 27 | 21 | Units 15 to 20: a self-turned rope, a long-tool tee hit, an overhand throw; knowledge: a chase and a flee move, a snack and a drink, why a rule helps, a goal and its check; conduct: a fair choice | 228 (week 28) |

Each window splits the six groups over its two days, so a child is watched once. Every standard S1 to S4 is
sampled in each year. Every course-level day's note names its stations' space, equipment, no-equipment path and the
water break; a window with a striking station carries the swing-space rule. The frame's check table carries this
table's additions (K year-end S3.2.7 conduct and the reuse of the day 66 record; grade 1 mid-year S3.2.1; grade 1
year-end S2.2.9 and S3.2.5; grade 2 mid-year S3.2.3; grade 2 year-end S3.2.9), fixed 2026-11-26.

**Codes not sampled at any course-level check** (lead call 10, settled): S1.2.15, S1.2.17, S2.2.4, S2.2.5, S2.2.6,
S2.2.10, S2.2.12, S3.2.10, S4.2.1, S4.2.2, S4.2.3, S4.2.4, S4.2.5, S4.2.7 and S4.2.10 are checked only at their unit's
end, because their units come just before a check (records carried unscored, as the frame says) or after the
year-end check (units 7, 14, 22). Every standard is still sampled each year.

## Logic model

One page a year, the same shape for each.

| | Kindergarten | Grade 1 | Grade 2 |
|---|---|---|---|
| Inputs | 80 sessions of 30 minutes; cue cards, picture task cards, record sheet; soft balls, balloons, paddles, cones, ropes, scarves (or the no-equipment path); a soft surface | The same, plus mats (unit 9), beanbags and playground balls, a music track or drum | The same, plus long-handled bats or noodles, ropes matched to height, a long rope, real child life jackets |
| Activities | Units 1 to 7: own space and signals, balances and in-place moves, roll and catch, kick and tap, striking and early tries with choice stations, body changes, moving and feeling | Units 8 to 14: traveling ways and movement words, weight shifts and rope, send and receive with kind partners, bounce and hand strike with calm steps, heart and feet and tools, dances, games from many places | Units 15 to 22: sequences and stretching, overhand throw with goals, ball stations with team talk, rope with food and drink, long-handled striking with rules and fairness, chase and flee, dance sequences, water safety and looking back |
| Outcomes | Kindergarten outcome per standard (band section above), checked by unit checks and two course-level checks | Grade 1 outcome per standard, checked the same way | Grade 2 outcome per standard, checked the same way, records handed to grades 3 to 5 |

The course page says the course has not been tried with children and claims no effect on fitness or health.

## Shorter path

**The 64-session path** (APPROACH.md "Pacing") drops 16 Fluency days a year. None is a check, respond, baseline or
first-teaching day, none is a unit's last Fluency day before its check, at most 3 come from one unit, and every
unit keeps at least one Fluency day. Each dropped day's practice folds into the next Fluency day of its unit. The
day's note says "Shorter path" on each one.

| Year | Days dropped (by unit) |
|---|---|
| K | unit 1: 5, 7, 8; unit 2: 18, 19; unit 3: 25, 28, 29 (the pins station moves into day 31); unit 4: 38; unit 5: 47, 49, 54; unit 6: 63; unit 7: 72, 74, 76 |
| Grade 1 | unit 8: 83, 86; unit 9: 93, 95; unit 10: 104, 105, 108; unit 11: 114, 117, 118; unit 12: 129, 131, 132 (the heartbeat drawing moves into day 133); unit 13: 138, 142; unit 14: 155 |
| Grade 2 | unit 15: 163, 167; unit 16: 172, 174, 177; unit 17: 182, 186, 187; unit 18: 192, 194, 197; unit 19: 206, 208; unit 20: 215 (freeze tag moves into day 216's game); unit 21: none (one Fluency day); unit 22: 231, 233 |

Every owned code keeps its teaching day and its check: the dropped days carry only codes taught on an earlier
Understanding day of the same unit, or S3 conduct codes reviewed from an earlier unit (days 19, 38, 74, 118,
142, 167), which stay practiced on the unit's other days. Both course-level checks and every respond day stay.

**A year 10 school days short** loses about 5 sessions. Drop these first (they are inside the 64-session list):
K 7, 19, 29, 54, 74; grade 1 83, 95, 105, 118, 132; grade 2 167, 177, 187, 197, 208.

**A shorter period** (20 to 25 minutes instead of 30) keeps every day: the warm-up and cool-down shorten to 2
minutes each, and the closure watch keeps its place.

**A leave-out unit** (a school or family that leaves a unit out takes its owned codes off the course page's claim).
Bridges where a later unit uses a left-out unit's card: leave out unit 6 and units 11, 12 and 15 teach the effort
faces in one minute where they use them; leave out unit 11 and units 14 and 22 show the calm-down card's grade 1
rung before using it; leave out unit 12 and unit 15 shows the pulse-check before the stretching day; leave out unit
16 and unit 22 shows the goal steps card's grade 2 rung; leave out unit 17 and unit 19 teaches the team-talk steps
on day 207; leave out unit 5 and unit 14 shows the goal steps card's first rung on day 156. The cultural units (13,
14, 21) are swapped, not left out (frame "Swaps and leave-outs").

## Sources

No day leans on an unloaded source. The safety guides (Nova Scotia 2021, SPHEReS, CDC's drowning page) are read by
the safety agent for units 5, 9, 12, 15, 17, 19 and 22 before they go live, as the frame says; each cultural game
and dance waits on the sensitivity agent's read of its community's own source. The Seven Jumps entry's live address
(2026-11-26) is folkdancefootnotes.org/dance/a-real-folk-dance-what-is-it/1st-generation-dances/childrens-dances-1st-generation-or-living/seven-jumps-l-syvspring-denmark-de-zevensprong-netherlands/. Appropriate practice points and
PECAT were read for placement only.

## For the lead

1. **"Pick, practice, check" and the goal steps card.** PE's own goal words are the actions done on SEL's goal steps
   rungs; the days quote SEL's card and never print a second card. If PE's APPROACH prints "pick, practice, check"
   as a card, it should say this.
2. **Unit 20 without a respond day** (frame). Unit 21's day 1 carries the response; if the lead prefers a respond
   day, it would come from unit 21's single Fluency day, which the shorter path already protects.

## What I am unsure of

- Whether two tasks are enough for the "several in-place practice tasks" indicators; the days record two (the end
  task and the last Fluency day's closure watch), and a unit plan may add a third at no day cost.
- Mugunghwa's source is unconfirmed: the cited ministry page names Korea's alleyway games but not Mugunghwa in its
  text. The sensitivity agent finds a Korean folk-culture source before unit 14 names the game (browser check:
  the National Folk Museum of Korea's Encyclopedia of Korean Folk Culture); the swap rule covers it if none says
  the game is open to be taught.
- Whether the sensitivity read will confirm the other named dances and games as open to be taught; the swap rule
  covers any that fail.

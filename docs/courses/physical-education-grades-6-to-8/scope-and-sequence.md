# Scope and sequence: Physical Education, grades 6 to 8

Course `physical-education-grades-6-to-8`, a band course for grades 6, 7 and 8. Draft, 2026-11-26, from the frame
(docs/courses/physical-education-grades-6-to-8/frame.md); the days are in
data/plans/physical-education-grades-6-to-8/days.csv (288 rows, written by
build/scope-writes/scratch/physical-education-grades-6-to-8/build_days.py). Units, owned rows, codes and day counts
are the frame's, unchanged. The course has not been tried with children and claims no effect on fitness or health.
Fix pass 2026-11-26 after the expert read (docs/reviews/sequence-physical-education-grades-6-to-8-fixes-2026-11-26.md,
script build/scope-writes/scratch/physical-education-grades-6-to-8/fix_2026-11-26.py).

## How the band runs

- **Three years, one after another.** Year 6 is course days 1 to 96, year 7 days 97 to 192, year 8 days 193 to 288.
  Each year is 90 unit days, two mid-year check days and a respond day, and two year-end check days and a respond day.
- **Which standards fall in which year.** SHAPE America's 2024 standards give one set of 61 learning indicators for
  the whole span to grade 8 (SHAPE.S1.8.1 to S4.8.9). Each indicator is owned by one progression row of one grade
  (data/progressions/physical-education.csv), so it is claimed in that row's year only: year 6 claims the grade 6
  rows' codes, year 7 the grade 7 rows', year 8 the grade 8 rows'. A code written with `~` in days.csv is begun
  toward a later owner, or used in a new setting after an earlier one, and is never a claim. The grade outcomes
  below are the frame's.
- **Meeting days and school_day.** Three sessions of 45 minutes a week, 32 weeks a year (APPROACH.md "Pacing", 96
  sessions a year). `school_day` counts school days across the band, 1 to 480: year 6 is band school days 1 to 160,
  year 7 is 161 to 320, year 8 is 321 to 480. Course day d of a year falls on about school day 5d/3 of that year,
  with the lead's pins from data/plans/course-list.csv (course days 49 and 50 of each year on school days 76 and 77
  in grades 6 and 7, 73 and 74 in grade 8; day 96 on school day 160), filled by `frame.school_day`. Take away 160
  (year 7) or 320 (year 8) for the grade's own school day; the week is (school day - 1) // 5 + 1. A filled
  school_day wins over frame.py's spread; the lead regenerates calendar.csv from it.
- **The 45 minutes.** Class time after changing (changing follows the school's own policy, outside the period; no
  one changes in front of others). Instant activity 5 to 8, warm-up 5, focus 20 to 25, cool-down 3, closure 3,
  equipment out and back about 4 (about 6 on outdoor days in units 14 and 20, done by station groups). At least half
  of every lesson is moderate to vigorous activity. Check days: six groups of five, about 4 minutes a group, watched
  in rotation while the others work at stations; a knowledge task on a half sheet takes about 5 minutes.
- **The day pattern of a unit.** Day 1 is the hook and compelling question, then the first cue shown and tried
  (Understanding). Day 2 is the first skill day: its instant activity holds the retrieval task (about 8 minutes) and
  the baseline watch of the unit's main cue, in rotating groups, marked met, partly or not yet. Every cue is taught on
  an Understanding day before any Fluency or Application day uses it. Fluency days are many tries with feedback on
  one cue (stations, partners, no lines); Application days put the skill in a small-sided game, a dance, a circuit or
  a tactic. The last Fluency day of a unit holds the closure watch of any second skill (carried to the check); the
  last Application day records conduct. Check days repeat the baseline cue, so each student has two marks and growth
  is the change. The respond day groups students by the teacher's met, partly and not yet marks and practices the "not
  yet" cue in a new task; where the next unit has a readiness check, it is the respond day's last 10 minutes.
- **Space and equipment.** Every movement day's note in days.csv names its safe space and equipment, with the
  low-equipment path (rolled socks, paper balls, pool noodles, milk-jug scoops, a rope net between two chairs). The
  safe-space rules are the frame's: arm's length all round, one throwing direction, swing space with one swinger per
  space, a water break in warm weather, equipment checked before the lesson. Units with striking tools, resistance
  exercise, power jumps, fitness testing, floor hockey, outdoor work and water are read by the safety agent before
  they go live (named on their first day).
- **Shared cards, word for word (SEL STANDARD section 7, 6 to 8 form).** Calm-down: "stop, breathe, name it, choose,
  go on" (units 6, 11, 12, 22). Goal steps: "goal, steps, block and plan, check" (units 6, 15, 22). PE uses no
  I-statement, refusal or talk turn card in this band.
- **Competition.** Every small-sided game in the band offers a more and a less competitive court or field the student
  chooses (frame, Supports), whether or not the day's note names it.
- **Teacher page, every unit.** Health's disclosure steps word for word (docs/courses/health/APPROACH.md, "If a
  student tells you something"). Puberty: a student who needs a private moment (a period, a growth spurt that makes a
  skill feel new, sweat or smell worries) gets a quiet role change or a restroom break with no reason asked aloud.
- **Readiness and retrieval.** Last use counts by grade with one hop (sequence-write.md rule 2). The readiness checks
  are on day 1 (g4-object-ideas, g3-stay-safe-own) and on the respond days before units 14 (g5-food-drink), 21
  (g5-water-skills) and 22 (g4-world-activities). Four rows the frame first gave readiness checks were used the year
  before through a later row, so they are retrieval: g4-pulse-body (day 25), g4-reasons-strengths (day 81),
  g5-conflict-solve (day 135) and g5-review-experiences (day 151).

## Logic model (one page)

| Inputs | Activities | Outputs | Short-term outcomes | Longer-term outcomes (not claimed) |
|---|---|---|---|---|
| A gym, field or cleared room; about $745 of equipment across the band from nothing (the band's ceiling); printed cue, task and case cards; a teacher with no special training | 96 sessions of 45 minutes a year; skill, fitness, game, dance and outdoor units with a baseline watch, a check and a respond day each | Two marks per student per unit on the main cue; knowledge tasks; conduct marks; a private fitness record and a participation goal kept by the student | Students perform the grade's skills with the named cues, explain fitness and tactics, act safely and fairly, and name ways to stay active | More lifelong activity. The course is untested and claims no effect on fitness or health |

## Year 6 (grade 6 rows, course days 1 to 96)

Grade outcomes (the frame's). S1: throws, rolls and catches with good form, passes, receives and dribbles on the
move, takes a ready defensive stance, performs four-phrase dance sequences, and uses sound technique in
health-related and skill-related fitness exercises (S1.8.2, S1.8.3, S1.8.4, S1.8.6, S1.8.8, S1.8.14, S1.8.15,
S1.8.19), and makes first tries at serves, strokes and tossed-ball striking. S2: breaks a skill into its parts, sorts
the fitness parts, builds a warm-up and cool-down, counts and explains heart rate, names movement ideas, and lists
ways to stay active (S2.8.1, S2.8.9, S2.8.14, S2.8.15, S2.8.16, S2.8.18). S3: welcomes differences and contributes
to a team, follows rules and safe behavior (S3.8.1, S3.8.2, S3.8.6, S3.8.7). S4: explains how self-expression
affects involvement and takes part in many kinds of activity (S4.8.1, S4.8.3).

Picked up from grades 3 to 5: readiness on day 1 (g4-object-ideas, g3-stay-safe-own); grade 5's striking and
fielding, invasion, net and wall skills, fair decisions, FITT, goals and conflict steps are retrieved on the day 2s,
and g4-pulse-body and g4-reasons-strengths (used by grade 5 rows) on days 25 and 81.

### Unit 1. Break down the throw

Course days 1 to 13, school days 2 to 21, weeks 1 to 5. Codes S2.8.18, S1.8.6, S3.8.6, S3.8.7. Day 1 sets the class
rules, the one throwing direction and the fetch signal, and holds the readiness check. Order: roll and underhand
(day 2), sidearm and overhand (day 3), stations and analysis pairs (4, 5, 7), target and roll games (6, 8), closure
watch of the roll and underhand (9), conduct (10). Check: day 11 the overhand throw (3 of 5) and the knowledge task,
day 12 the sidearm throw and the conduct mark; each of the four forms is marked apart. Respond day 13.

### Unit 2. Fitness parts and the warm-up

Course days 14 to 24, school days 22 to 37, weeks 5 to 8. Codes S2.8.9, S2.8.14, S1.8.4. Fitness parts (14),
dynamic warm-up and static cool-down with retrieval of grade 5 FITT (15), skill-related technique and the power
jump's baseline (16), stations, warm-up cards and circuits (17 to 22). One check day (an 11-day unit), day 23: one
skill-related drill and the soft landing, the activity sort, a warm-up, a cool-down and a stretch for the end of a
training block (dynamic or static, and why), the knowledge task taking about 8 minutes from the instant activity.
Respond day 24 is response time only (g4-pulse-body is retrieved on day 25). Health's outcome 3 (warm-up and
cool-down) is taught here.

### Unit 3. Heart rate and strong muscles

Course days 25 to 36, school days 39 to 56, weeks 8 to 12. Codes S2.8.15, S1.8.3. Heart count with the pulse
retrieval (25), strength technique with the squat baseline and retrieval of unit 2's parts and grade 5 FITT (26), the
jog and held stretch with water (27, health's outcome 4), stations, private counts and circuits (28 to 33). Check days
34 (one exercise per health-related part) and 35 (count, convert, explain). Respond day 36. Counts are private, never
posted or compared. Leans on math grade 6 unit 2 (school days 19 to 39), which ends on the school day unit 3 opens:
day 25 says "beats in a minute", and ratio words start on day 26.

### Unit 4. Catch, pass and play together

Course days 37 to 48, school days 57 to 74, weeks 12 to 15. Codes S1.8.8, S1.8.14, S3.8.1, S3.8.2. Catch (37), pass
and receive with the tactics question and the "give" baseline (38), welcoming differences and the class rule (39),
stations, keep-away and scoop-ball games (40 to 45), closure watch of five passes on day 43, conduct on day 45. Check
days 46 (catch at three heights) and 47 (knowledge and conduct). Respond day 48.

### Year 6 mid-year check

Course days 49 and 50 (school days 76 and 77, week 16), respond day 51 (school day 79). Draws from units 1 to 3 at new
stations: two throwing forms, a skill-related drill, a health-related exercise (S1.8.6, S1.8.4, S1.8.3); knowledge on
skill analysis, fitness parts and beats per minute (S2.8.18, S2.8.9, S2.8.15); conduct on rules and equipment
(S3.8.6, S3.8.7). Unit 4's end-of-unit record, taken days before, is carried unscored and none of its items is asked
again (lead arts call).

### Unit 5. Dribble, defend and find the space

Course days 52 to 65, school days 81 to 105, weeks 17 to 21. Codes S1.8.15, S1.8.19, S2.8.1. Dribble (52), past a
passive defender with the "head up" baseline and retrieval of grade 5's dribble, defending and problem solving (53), stance (54), movement ideas in an obstacle course (55), stations,
mirror drills, tag with no one out and small games (56 to 62), closure watch of the stance (61), conduct (62). Check
days 63 (dribble) and 64 (movement idea in two settings, the obstacle course being the third). Respond day 65.

### Unit 6. Dances in many styles

Course days 66 to 79, school days 106 to 130, weeks 22 to 26. Codes S1.8.2, S4.8.1, S4.8.3. A line dance of our own
with no cultural claim (66), cumbia's basic step with teacher-set partners and no gender roles (67), self-expression
with the goal steps card and the calm-down card before a small-group showing (68), the group routine and the
activity record (69), practice, partner changes and showings (70 to 76), conduct (76). Check days 77 (four-phrase
sequence) and 78 (knowledge). Respond day 79 is response time only (g4-reasons-strengths is retrieved on day 81).
Cumbia stays a candidate until its sensitivity confirm (For the lead).

### Unit 7. Strike, serve and stay active

Course days 80 to 93, school days 132 to 155, weeks 27 to 31. Owned code S2.8.16; first tries toward S1.8.5, S1.8.7,
S1.8.10, S1.8.11, S1.8.12 (owned in grade 7). Handheld forehand (80), ways to stay active with retrieval of grade 5 goals, reasons to move
(g4-reasons-strengths) and health's supports and barriers (81), tossed-ball swing with the "eyes on contact" baseline (82), hand and short-tool
underhand serves (83), stations, rallies and the lifetime-activity sampler (84 to 90), conduct (90). Check days 91
(tossed-ball swing, growth marked toward grade 7) and 92 (the personal list of five ways). Respond day 93.

### Year 6 year-end check

Course days 94 and 95 (school days 157 and 159, week 32), respond day 96 (school day 160). Draws from units 4 to 6:
catch and pass, dribble, four-phrase sequence (S1.8.8, S1.8.14, S1.8.15, S1.8.2); knowledge on movement ideas,
self-expression and kinds of activity (S2.8.1, S4.8.1, S4.8.3); conduct on helping and including (S3.8.1, S3.8.2).
Unit 7's record carried unscored.

## Year 7 (grade 7 rows, course days 97 to 192)

Grade outcomes (the frame's). S1: throws for accuracy, distance and power, swings a long tool with a mature pattern,
strikes a tossed ball into space, serves with hand and tool, hits forehand and backhand strokes, and keeps form in
circuits, routines and an outdoor walk (S1.8.5, S1.8.7, S1.8.9, S1.8.10, S1.8.11, S1.8.12). S2: explains attack and
defense in invasion games, changes dances with movement ideas, uses FITT and the training principles, uses
skill-related fitness, links aerobic fitness and effort, plans rest, and links eating, exercise and well-being
(S2.8.2, S2.8.3, S2.8.8, S2.8.11, S2.8.12, S2.8.13, S2.8.17, S2.8.20). S3: talks over game plans, gives and takes
feedback, settles disagreements and keeps the norms of good conduct (S3.8.3, S3.8.4, S3.8.8, S3.8.9). S4: explains
how others and choice affect involvement, examines challenges, and uses strategies to manage feelings (S4.8.2,
S4.8.4, S4.8.5, S4.8.8).

Year-day numbers below are of the year (day 1 is course day 97).

### Unit 8. Throw for power, coach a partner

Course days 97 to 108, school days 2 to 19, weeks 1 to 4. Codes S1.8.9, S3.8.3, S3.8.4. Power cue (day 1), three
throws with the baseline and retrieval of grade 6 throwing, analysis and welcoming (2), feedback cards and game plans
(3), stations and a throwing game (4 to 9; day 6 keeps g6-catch-form in use), conduct (9). Check days 10 and 11,
respond day 12.

### Unit 9. Attack and defend the space

Course days 109 to 120, school days 21 to 37, weeks 5 to 8. Codes S2.8.2, S2.8.3; first tries toward S1.8.13,
S1.8.16, S1.8.17, S1.8.18 (owned in grade 8) on year day 17 (course day 113), whose instant activity retrieves
unit 7's forehand and serve for the volley station; its stick station is on the safety read. Attack (13), cut and pass with the "move without the
ball" baseline (14), defend (15), drills and three-on-three with a drawn play (16 to 21), conduct (21). Check days 22
and 23, respond day 24.

### Unit 10. Train smart

Course days 121 to 132, school days 39 to 56, weeks 8 to 12. Codes S2.8.11, S2.8.12, S2.8.13. FITT and the training
principles (25), effort scale and talk test with the "steady breath" baseline (26), skill-related fitness in sports
(27), circuits, pace keeping and plans (28 to 33), closure watch of the changed station and conduct (33). Check days
34 and 35; day 35's plan change asks each part of S2.8.11 with its own prompt (which FITT part, overload or
progression, fit to the goal, a second activity). Respond day 36 is response time only (g5-conflict-solve is
retrieved on year day 39).

### Unit 11. Swing, place and play fair

Course days 133 to 144, school days 57 to 74, weeks 12 to 15. Codes S1.8.5, S1.8.7, S3.8.8, S3.8.9. Long-tool swing
(37), tossed ball placed into space with the "rotate" baseline (38), settling disagreements with retrieval of the
grade 5 conflict steps, the calm-down card and team talk, and the class's three norms (39), stations and a self-officiated game with no elimination (40 to 45;
day 42 keeps g6-catch-form in use), closure watch of placement (43), conduct (45). Check days 46 and 47, respond day
48.

### Year 7 mid-year check

Course days 145 and 146 (school days 76 and 77 of grade 7, week 16), respond day 147 (school day 79), response time
only (g5-review-experiences is retrieved on course day 151). Draws from units 8 to 10: throws, a cut and pass,
a pace at talk-test effort (S1.8.9, S2.8.2, S2.8.13); knowledge on a defense and a changed plan (S2.8.3, S2.8.11);
conduct on feedback (S3.8.4). Unit 11's record carried unscored.

### Unit 12. Serve, stroke and keep your cool

Course days 148 to 161, school days 81 to 105, weeks 17 to 21. Codes S1.8.10, S1.8.11, S1.8.12, S4.8.8. Hand serves
(52), tool serves with the "toss, step" baseline (53), strokes with both tool lengths (54), managing feelings with
retrieval of a hard moment and what helped (g5-review-experiences) and the calm-down card in full (55), stations and net games (56 to 62), closure watches of short-tool strokes (59) and
long-tool strokes (61), conduct (62). Check days 63 (hand serves, each type marked apart) and 64 (tool serves,
knowledge), respond day 65. Beside SEL 6 to 8 unit 10 (grade 7 weeks 16 to 21).

### Unit 13. Change the dance

Course days 162 to 174, school days 106 to 128, weeks 22 to 26. Codes S2.8.8, S4.8.2, S4.8.4, S4.8.5. Unison and
canon (66), kolo with the "canon" baseline (67), joining in and challenges (68), phrases, rhythm forms, group roles
and the challenge's fix (69 to 75), conduct (75). Check days 76 and 77. Respond day 78 holds the readiness check
g5-food-drink for unit 14, with no weight, calorie or diet talk.

### Unit 14. Out on the trail: form, fuel and rest

Course days 175 to 189, school days 130 to 155, weeks 26 to 31. Codes S2.8.17, S2.8.20; used in new settings
S1.8.2, S1.8.3, S1.8.4; begun toward S1.8.1. Circuit form (79), rest with the "posture" baseline (80), fuel (81,
leaning on science grade 7 unit 3, weeks 9 to 14), the first walk on the grounds (82), circuits, the routine
and the recovery plan (83 to 89), the second walk with conduct (90, keeping g6-rules-safe in use). Check days 91 and
92, respond day 93.

### Year 7 year-end check

Course days 190 and 191 (school days 157 and 159 of grade 7, week 32), respond day 192 (school day 160). Draws from
units 11 to 13: a mature swing, serves to a zone, a changed sequence (S1.8.5, S1.8.10, S1.8.11, S2.8.8); knowledge on
settling a disagreement, managing feelings and a challenge with a fix (S3.8.8, S4.8.8, S4.8.5); conduct on the norms
(S3.8.9). Unit 14's record carried unscored.

## Year 8 (grade 8 rows, course days 193 to 288)

Grade outcomes (the frame's). S1: volleys, dribbles with a tool, shoots, gets open, keeps good form outdoors, and
shows dry-land water safety skills (S1.8.1, S1.8.13, S1.8.16, S1.8.17, S1.8.18, S1.8.20), and uses the band's skills
in modified games and a planned routine. S2: picks shots in net games, explains striking and fielding tactics, uses
problem-solving methods, tracks a chosen fitness test toward a goal, judges technology, and shows outdoor and water
safety knowledge (S2.8.4, S2.8.5, S2.8.6, S2.8.7, S2.8.10, S2.8.19, S2.8.21, S2.8.22). S3: explains why an activity
matters in a culture and links communication and courtesy to leading (S3.8.5, S3.8.10). S4: sets participation
goals, weighs chances and obstacles outside class, and reflects on what PE means to them (S4.8.6, S4.8.7, S4.8.9).

Year-day numbers below are of the year (day 1 is course day 193).

### Unit 15. My test, my goal, my tools

Course days 193 to 202 (year days 1 to 10, school days 2 to 16, weeks 1 to 4), then its held check on course day 239
(year day 47, school day 70, week 14) and its respond day on 240 (year day 48, school day 72). Codes S2.8.10, S2.8.19,
S4.8.6, S4.8.7. Choosing a test (1), the private baseline (2), goals and obstacles on the goal steps card (3), tool
cards (5), plan practice and the private plot (4 to 10). From day 11 to day 46 each warm-up holds about 3 minutes of
the student's own plan. The held check (day 47) is the retest under the same time, route and recording; the process
is marked, never the result. Results are never posted, graded or compared; no BMI, weight or body measures.

### Unit 16. Invasion play

Course days 203 to 217, school days 17 to 37, weeks 4 to 8. Codes S1.8.16, S1.8.17, S1.8.18; used in new settings
S1.8.14, S1.8.15, S1.8.19. Stick dribble (11), shooting with and without a stick and the "stick low" baseline (12),
getting open and the four-on-four (13), courses, shots and games (14 to 22), closure watch of shooting (21), two
get-open moves watched and conduct (22). Check days 23 and 24, respond day 25.

### Unit 17. Net and wall play

Course days 218 to 230, school days 39 to 57, weeks 8 to 12. Codes S1.8.13, S2.8.4, S2.8.7; used in new settings
S1.8.10, S1.8.11, S1.8.12. Short-tool volley (26), long-tool volley and placement with the "contact in front"
baseline (27), the problem-solving method (28), stations and singles and doubles (29 to 35), closure watch of the
rally with a serve (33), the method used again on an invasion game (34), the placed shot and conduct (35). Check days
36 and 37; day 37 collects both method records (net game, day 32; invasion game, day 34) and asks which change worked
in each. Respond day 38.

### Unit 18. My planned week, and leading a warm-up

Course days 231 to 238, school days 58 to 69, weeks 12 to 14. Code S3.8.10; used in new settings S1.8.2, S1.8.3,
S1.8.4. Planning the week (39), leading with the "posture" baseline (40), the week and small-group warm-ups led in
turn (41 to 44), conduct (44). One check day (an 8-day unit), day 45, respond day 46.

### Year 8 mid-year check

Course days 241 and 242 (school days 73 and 74 of grade 8, week 15), respond day 243 (school day 76). Draws a stick
dribble and a volley rally (S1.8.16, S1.8.13), a shot choice (S2.8.4) and courtesy calls (~S3.8.9, grade 7's
conduct in review). Unit 15's test with form, tool-card rating and participation goal were taken on its held check two
days before and are carried by the collect-once rule, not taken again (the frame's check row now says so). Unit 18's
record carried unscored.

### Unit 19. Striking and fielding

Course days 244 to 255, school days 78 to 99, weeks 16 to 20. Codes S2.8.5, S2.8.6; used in new settings S1.8.5 to
S1.8.9. Attacking tactics in a game with no elimination (52), defending tactics and fielding with the "rotate"
baseline and retrieval of grade 6 catching (kept live in units 8 and 11) (53), stations, the fielders' map and games
(54 to 60), closure watch of the field-and-throw (58), conduct (60). Check days 61 and 62, respond day 63.

### Unit 20. Outdoors with good form

Course days 256 to 267, school days 101 to 121, weeks 21 to 25. Codes S1.8.1, S2.8.21. Hiking form and safety steps
(64, health's outcome 6), orienteering with the "map to the ground" baseline (65), paddling on land or a low traverse
on the school's own wall (66), legs, hikes and courses (67 to 72), closure watch of the third activity (71), the
full course with a hike leg and conduct (72). Check days 73 and 74. Respond day 75 holds the readiness check
g5-water-skills for unit 21.

### Unit 21. Safe near water

Course days 268 to 274, school days 123 to 134, weeks 25 to 27. Codes S1.8.20, S2.8.22. Dry land only; no student
enters water. Reach and throw (76), the life jacket with the "reach or throw" baseline (77), stations and scenarios
(78 to 80), closure watch of the reach rescue (80). One check day (a 7-day unit), day 81. CDC's "Preventing
Drowning" page (opened 2026-11-26) covers life jackets, swimming skills, the buddy rule and natural-water risks but not
reach or throw rescues; those steps come from the Palm Beach County Drowning Prevention Coalition's "Reach, Throw, Don't Go" page (https://discover.pbc.gov/drowningprevention/Pages/Reach-Throw-DontGo.aspx, opened 2026-11-26): call for help first, reach with something long while lying flat, throw something that floats, never go in. Respond day 82 holds the
readiness check g4-world-activities for unit 22.

### Unit 22. Why it matters, and what PE means to me

Course days 275 to 285, school days 136 to 155, weeks 28 to 31. Codes S3.8.5, S4.8.9. The ginga (83), the capoeira
circle on its case card, retrieving dance 6 to 8 unit 8 (84), the reflection with both cards in review (85), the
ginga in pairs and in the circle, Naadam read only (confirmed at its UNESCO entry, 2010; the case card names its
rituals and imitates none), the portfolio (86 to 91), conduct (91). One check day (an 11-day
unit), day 92, respond day 93. Leans on social studies grade 4 unit 7, years before.

### Year 8 year-end check

Course days 286 and 287 (school days 157 and 159 of grade 8, week 32), respond day 288 (school day 160), which hands
the band's records to grade 9. Draws a get-open move, a placed hit, orienteering form and a life jacket (S1.8.18,
S2.8.5, S1.8.1, S1.8.20); knowledge on fielders, an outdoor checklist and a cold-water rule (S2.8.6, S2.8.21,
S2.8.22); courtesy linked to leading (S3.8.10); the participation goal looked at again (S4.8.6, S4.8.7). Unit 22's
record carried unscored.

## Course-level checks

Every check sits where the frame and CALENDAR.md put it: mid-year in week 16 (grades 6 and 7) and week 15 (grade 8),
year-end in week 32, the finals week. Each samples earlier units at new stations; the unit just ended is carried by
its own end-of-unit record. A student is watched once in each window. A check and an end-of-unit day in a later year
that watch an earlier year's conduct code write it with `~` (a review, never a claim): days 131, 173, 188, 216, 229,
239, 242, 254, 266, 273 and 284.

Owned codes no course-level check samples, and why (each is checked on its own end-of-unit day):

- Grade 6: S1.8.19 (unit 5's stance is a second skill; the year-end check samples the dribble from that unit),
  S2.8.14 (warm-up and cool-down return in every later warm-up instead), S2.8.16 (unit 7 ends the year; carried).
- Grade 7: S1.8.7 and S2.8.12 (the checks sample the unit's main cue only), S3.8.3 (game plans, sampled through
  feedback S3.8.4), S1.8.12 (strokes are carried on closure watches; the check samples serves), S2.8.17 and S2.8.20
  (unit 14 ends the year; carried), S4.8.2 and S4.8.4 (the check samples unit 13's challenge row, S4.8.5).
- Grade 8: S1.8.17 (shooting, a second skill of unit 16), S2.8.7 (the method record stays in unit 17), S2.8.10 and
  S2.8.19 (carried from unit 15's held check by collect once), S3.8.5 and S4.8.9 (unit 22 ends the year; carried).

## Cross-subject leans on the calendar

- Math grade 6 unit 2 (6.RP.A.3, school days 19 to 39) ends on school day 39, the day unit 3 opens, so day 25 says
  "beats in a minute" and ratio words start on day 26; it is a year before unit 10. Math grade 6 unit 6 (6.EE.C.9) is two years before unit 15; the record sheet supplies the grid.
- Science grade 7 unit 3 (MS-LS1-3, MS-LS1-7, weeks 9 to 14) comes before unit 14 (weeks 26 to 31).
- Social studies grade 4 unit 7 is years before unit 22.
- After-core, named both ways, no lean: health 6 to 8 units 8, 11, 15 and 16 run before or beside units 7, 11 and
  14, which open with a retrieval task on them and say what to do if health runs later; SEL 6 to 8's calm-down card
  (grade 6 unit 3, grade 7 unit 10) and teamwork (grade 7 unit 7) come first or beside; dance 6 to 8 teaches first in
  each year, and unit 22 retrieves its unit 8 capoeira study.

## Sensitivity and leave-out

- **Fitness, bodies and food.** Counts, effort ratings and test results are the student's own, never posted, graded
  or compared; no weighing, BMI or body measures; no calorie or diet talk (units 3, 10, 13's readiness, 14, 15).
- **Emotions.** Calm steps are offered, never a punishment; the teacher page names the school counselor (units 6,
  11, 12).
- **Cultural content.** Cumbia (unit 6), kolo (unit 13), capoeira and Naadam (unit 22) keep the frame's guards: no
  costume, no sacred use, the students' own choreography is not the tradition. Capoeira's sensitivity read comes
  before its case card is written. Naadam is confirmed at its UNESCO entry (2010: horse racing, wrestling and
  archery, with ritual songs and costumes); its read-only case card names the rituals and imitates none.
- **Puberty and disclosure.** A quiet role change or a restroom break with no reason asked aloud; health's disclosure
  steps on every teacher page (How the band runs).
- **Water.** Dry land only; in-water work is the school's own program with a lifeguard.
- **Gender and groups.** No gender split or roles; teams made by the teacher, privately; no elimination, no human
  targets, no exercise as punishment.
- **Leave-out.** The frame names no leave-out unit, so no bridge is needed.

## Shorter path

Three reduced paths, with no check, respond or baseline day cut, no owned code left unplaced, and the last Fluency,
last Application, closure-watch and conduct days kept. The only Understanding days cut are the begun-toward days the
frame says to drop first (83, 113, 178), whose owner unit teaches the skill in full a year later; no first teaching
of a row the year owns is cut. Every unit keeps practice on its main checked cue on at least one kept day, and every
owned part a kept check asks keeps a kept practice; where a dropped day held either, its note names the kept day it
folds into (about 10 minutes). Each dropped day is marked "64-session path: dropped" in its note.

**The 64-session path** (APPROACH.md "Pacing"): 32 days dropped each year, about two thirds of the practice days, as
the frame says openly. Folds on this path (each in the kept day's note): 40 into 43 (catching on "give"), 58 into 62
(the no-one-out tag round), 59 into 61 (dribbling past an active defender), 75 into 76 (the activity record), 19 into
21 (static holds in a training block), 102 into 105 and 138 into 141 (the g6-catch-form cue check, kept live for grade
8), 136 into 139 (swings on "rotate"), 152 into 155 (serves on "toss, step"), 166 into 170 (the rhythm form), 178 and
182 into 186 (the outdoor rules with g6-rules-safe, and the week with rest days), 211 into 213 (stick dribble past an
active defender), 224 into 225 (the net-game method record) and 226 into 227.

| Year 6 unit | Days | Dropped | Kept | Days dropped |
|---|---|---|---|---|
| 1 | 13 | 5 | 8 | 4, 5, 6, 7, 8 |
| 2 | 11 | 4 | 7 | 17, 18, 19, 20 |
| 3 | 12 | 4 | 8 | 28, 29, 30, 32 |
| 4 | 12 | 4 | 8 | 40, 41, 42, 44 |
| 5 | 14 | 5 | 9 | 56, 57, 58, 59, 60 |
| 6 | 14 | 4 | 10 | 70, 71, 72, 75 (day 73, groups teach a phrase, is kept) |
| 7 | 14 | 6 | 8 | 83, 84, 85, 86, 87, 88 |
| Checks | 6 | 0 | 6 | |
| **Total** | **96** | **32** | **64** | |

| Year 7 unit | Days | Dropped | Kept | Course days dropped |
|---|---|---|---|---|
| 8 | 12 | 4 | 8 | 100, 101, 102, 104 |
| 9 | 12 | 4 | 8 | 112, 113, 114, 115 |
| 10 | 12 | 4 | 8 | 124, 125, 126, 128 |
| 11 | 12 | 4 | 8 | 136, 137, 138, 140 |
| 12 | 14 | 4 | 10 | 152, 153, 154, 156 (day 155 opens with 10 minutes of serves on "toss, step") |
| 13 | 13 | 5 | 8 | 165, 166, 167, 168, 169 (the challenge fix moves to day 171; the rhythm form to day 170) |
| 14 | 15 | 7 | 8 | 178 to 184 (day 186 takes the walk's map-and-pace briefing, the outdoor rules and the week with rest days) |
| Checks | 6 | 0 | 6 | |
| **Total** | **96** | **32** | **64** | |

| Year 8 unit | Days | Dropped | Kept | Course days dropped |
|---|---|---|---|---|
| 15 | 12 | 4 | 8 | 196, 198, 199, 201 |
| 16 | 15 | 7 | 8 | 206 to 212 |
| 17 | 13 | 5 | 8 | 221, 222, 223, 224, 226 (day 226's invasion reprise folds into day 227, about 20 minutes, keeping S2.8.7 in two settings) |
| 18 | 8 | 2 | 6 | 233, 234 |
| 19 | 12 | 5 | 7 | 246, 247, 248, 249, 251 |
| 20 | 12 | 4 | 8 | 259, 260, 261, 262 |
| 21 | 7 | 1 | 6 | 270 |
| 22 | 11 | 4 | 7 | 278, 279, 280, 281 |
| Checks | 6 | 0 | 6 | |
| **Total** | **96** | **32** | **64** | |

**A year about 10 school days short** (about 6 sessions at three a week, lead arts call): six Fluency days a year fold
into the named later day of the same unit, each saving one 45-minute session, 270 minutes a year and 810 minutes (18
sessions) across the band against 288. Grade 6: course days 5, 19, 41, 59, 72, 87. Grade 7: 101, 114, 125, 137, 167,
181. Grade 8: 198, 209, 223, 248, 261, 280. Each note says which day it folds into (209 into 211, 280 into 282).

**A shorter period** (35 to 40 minutes, as many middle schools run): instant activity 4, warm-up 4, focus 15,
cool-down 2, closure 3, equipment 4, so at least half stays moving. Two-day checks are unchanged: six groups at about
3.5 minutes each, 21 minutes of rotation. Units with one check day (2, 15, 18, 21, 22) drop the focus block on the check
day and hold a 3-minute warm-up, the 21-minute rotation and the knowledge task.

## Candidate cells settled

| Unit | Candidate | Settled |
|---|---|---|
| 1 | Partner analysis card | Kept, day 5 (about 10 minutes) |
| 2 | Student's own warm-up card | Kept, day 18, used in every later warm-up |
| 3 | Private two-week resting-rate log | Kept, about 3 minutes from day 29, never collected |
| 4 | Class writes the "every player touches it" rule | Kept, day 39 |
| 5 | Group-designed obstacle course | Kept, day 60 |
| 6 | Groups teach each other a phrase | Kept, day 73 |
| 7 | Family "active in our area" card | Kept, sent home, no class time |
| 8 | Feedback card each student keeps | Kept, day 99 |
| 9 | A play the team draws, then runs | Kept, day 115 |
| 10 | Two-week plan change in warm-ups | Kept, day 126 |
| 11 | The class's three norms | Kept, day 135 |
| 12 | Pocket reset card | Kept, day 154 |
| 13 | Canon in two halves | Kept, day 171 |
| 14 | Private "how I recovered" log | Kept, day 182, never collected |
| 15 | Private plot of the student's own test | Kept, day 201 |
| 16 | "Three passes before a shot" | Kept, day 210 |
| 17 | Doubles "rally then point" | Kept, day 224 |
| 18 | Leading another class's warm-up | Dropped: it needs another class's time; students lead a small group in their own class |
| 19 | Fielders' map | Kept, day 247 |
| 20 | Groups set a control for another group | Kept, day 262 |
| 21 | Family water-safety card | Kept, sent home, no class time |
| 22 | Family-shared activity story | Optional, at home, only with family consent |

## Sources not loaded

The days lean on the safety guides the safety agent reads before each hazard unit goes live (striking tools,
resistance exercise, power jumps, fitness testing, floor hockey, outdoor, water), on SHAPE America's guidelines page
and the federal activity guidelines, and on the cultural sources for cumbia, kolo, capoeira and Naadam; none is
loaded in this repository yet. Safety facts in the notes are from the frame and from memory until those reads.

## For the lead

1. **Short path at 64.** Every year reaches 32 drops with no assessed or owned part cut (the expert read agreed once
   day 169 was marked), with the folds named under Shorter path. If the lead prefers the frame's 72-session option,
   drop only the first 24 listed per year.
2. **Open confirmations:** cumbia at a Colombian cultural institution's page and capoeira's sensitivity read before
   its case card (the sensitivity agent's steps). The reach and throw rescue source is the Palm Beach County
   "Reach, Throw, Don't Go" page, opened 2026-11-26; the safety read still checks unit 21. The UNESCO kolo, capoeira and Naadam entries were opened on 2026-11-26, so those browser checks are closed.

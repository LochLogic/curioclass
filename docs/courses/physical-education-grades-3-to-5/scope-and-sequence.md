# Scope and sequence: Physical Education, grades 3 to 5

Course `physical-education-grades-3-to-5`, grades 3 to 5 as three years in one file, draft, written 2026-11-26 from
the frame (docs/courses/physical-education-grades-3-to-5/frame.md, with its 2026-11-25 reviews' fixes applied). The
days live in data/plans/physical-education-grades-3-to-5/days.csv.

## The band on one page

- **Which grade's standards fall in which year.** Year 3 (course days 1 to 80) owns the 18 grade 3 progression rows
  of data/progressions/physical-education.csv, year 4 (days 81 to 160) the 17 grade 4 rows, year 5 (days 161 to
  240) the 14 grade 5 rows: 49 rows owning all 57 span-5 SHAPE America 2024 indicators (SHAPE.S1.5.1 to S1.5.22,
  S2.5.1 to S2.5.18, S3.5.1 to S3.5.7, S4.5.1 to S4.5.10), each claimed only in its owner's unit. Ids and our own
  words only; no indicator sentence is quoted. A begun id (owned in a later grade, begun here) is written `~ID` in
  the codes column and named in the note as "begun toward" (days 18, 73 to 79, 193, 195); a code used in new settings
  (owner earlier) is named in the note only, with no new claim.
- **Grade outcomes**, copied from the frame, with the indicators each year works on:
  - Grade 3. S1: throws, rolls and catches in several tasks, jumps and lands and balances in place, does body rolls
    on a mat, kicks and dribbles with the feet, bounces a ball on the move, strikes with long and short tools, and
    jumps rope in several tasks (S1.5.3, S1.5.6 to S1.5.12, S1.5.16, S1.5.18 to S1.5.20), with four-count dance
    phrases begun. S2: uses movement ideas and tactics to stay safe, says when a warm-up and cool-down are needed,
    names a skill's key parts, matches activities to the health-related fitness parts and describes the benefits of
    activity (S2.5.1, S2.5.7, S2.5.11, S2.5.13, S2.5.15). S3: acts kindly in a group and stays safe with few
    reminders (S3.5.3, S3.5.4). S4: describes how a favorite activity lets them express themselves and explains the
    health benefits of moving, names the calming method that works best during activity and finds a way to be
    active outside class (S4.5.1, S4.5.3, S4.5.8, S4.5.9).
  - Grade 4. S1: links traveling chains, shifts weight from feet to hands, performs an in-place sequence and a dance
    sequence, volleys and bumps, serves, passes and gathers, and combines moving with sending to a target (S1.5.1,
    S1.5.2, S1.5.4, S1.5.5, S1.5.13 to S1.5.15, S1.5.17, S1.5.21). S2: explains how to attack, says why a cue helps
    an object skill, describes skill-related fitness, finds a pulse and describes body changes, and uses movement
    ideas in dance, gymnastics, rhythms and individual activities (S2.5.2, S2.5.4, S2.5.6, S2.5.10, S2.5.12,
    S2.5.14). S3: explains how others see a situation, decides roles with a group and describes activities from
    cultures around the world (S3.5.1, S3.5.2, S3.5.7). S4: describes how favorite activities connect them with
    others, spots a group difficulty, gives reasons for the activities they pick and names a strength and where to
    practice (S4.5.2, S4.5.4, S4.5.5, S4.5.7).
  - Grade 5. S1: shows water safety skills on dry land (simple swimming only in a school's own aquatics program),
    and uses the band's skills in invasion, net and wall, and striking and fielding games and in an eight-part
    routine (S1.5.22). S2: explains how to defend, solves a game problem by testing a change, describes FITT, sets a
    fitness goal, names technology that helps and its limits, explains how food and drink affect activity, and
    shows understanding of water safety and basic swimming (S2.5.3, S2.5.5, S2.5.8, S2.5.9, S2.5.16 to S2.5.18).
    S3: works through a disagreement and makes fair decisions that fit the activity's customs (S3.5.5, S3.5.6). S4:
    sets a goal for four to six weeks and reviews what PE has meant to them (S4.5.6, S4.5.10).
  - Every year is checked by skill tasks, knowledge tasks (shown, said or a one-line written answer) and conduct
    marks.
- **Units and days.** 24 units, 240 course days, 80 a year: 74 in eight units and 6 course-level days (two check days
  and a respond day at mid-year, the same at year-end). `stretch` is the unit number of the frame's Units table (C on
  a course-level day); `unit` is `<unit>.1`.
- **How school_day is counted.** One 35-minute session, 2.5 a week on average, 32 weeks a year, 160 school days a
  year. school_day counts on across the whole band, as frame.py reads it: course day n sits on school day 2n, so
  course day k of a year sits on that year's school day 2k (year 3: school days 2 to 160, year 4: 162 to 320, year
  5: 322 to 480). The week of the year is ((school_day - 1) mod 160) // 5 + 1, which is ceil(k / 2.5). This formula
  is the scope's own and is not re-counted to match calendar.csv; every unit and check sits in the frame's weeks by
  it. A school picks its own two or three days a week.
- **The day.** Every 35-minute day holds the instant activity, warm-up, focus, cool-down and closure, with about 3
  minutes of set-up and clean-up done by station groups (about 4 on mat and net days). Kinds follow docs/GLOSSARY.md
  and APPROACH.md: Understanding (shown in two or three cues, tried at once), Fluency (many tries with feedback on
  one cue), Application (a changing setting: a circuit, a small-sided game, a dance, a chain), Check, Respond. No
  game is played before its skill has been taught and practiced.
- **Assessment pattern.** No unit is over 25 days, so none holds a mid-unit assessment. Units of 10 days or fewer end
  with one check day, longer units (1, 2, 10, 11, 17, 18) with two, and every unit ends with one respond day. Each
  unit's baseline watch (rotating groups, met, partly, not yet) falls on its first skill day and is named in the
  note; marks "carried" come from a closure watch on the unit's last Fluency day. Each check has one skill task, one
  knowledge task and one S3 conduct mark (the conduct mark reviews S3.5.3 or S3.5.4 outside the units that own them,
  with no claim; the day that marks it writes the reviewed id with `~` in the codes column, as K to 2 does). Day 2
  picks up the K to 2 record where the school kept it. Marks go on each child's private skill sheet, which travels with them from grade 3 to grade 6.
  Fitness data stays with the child: no comparing, ranking, posting or grade, no weighing.
- **Readiness and retrieval.** The frame's readiness checks sit in the last ten minutes of a respond day, never on a
  unit's first day: g1-world-games for unit 16 on day
  153 (unit 15's respond day); g2-foods-energy for unit 20 on day 196 (unit 19's respond day); g3-strike-tools
  (long tools, which grade 4 did not use) for unit 21 on day 205 (grade 5's mid-year respond day); g2-water-skills
  for unit 23 on day 225 (grade 5's year-end respond day). The g3-strike-tools check is part-level: the row's
  short-tool part was retrieved on day 116 (grade 4), so only the long-tool part, unused since grade 3, is checked.
  Every other earlier-grade row is retrieved in an instant activity (about 5 minutes) on the first day that needs it
  and named in the `retrieves` column. g1-heart-muscle is one of them: PE K to 2 day 164 (grade 2) retrieved it, so it
  is retrieved on day 33, not checked for readiness. g3-rope gets retrieval in unit 15 (day 149) and unit 22 (day
  215), not readiness.
- **Shared cards**, quoted word for word in the grades 3 to 5 form from the SEL 3 to 5 frame's "Shared steps with
  health and PE" bullet (SEL STANDARD section 7 gives the K to 2, 6 to 8 and 9 to 12 forms): the calm-down card
  "stop, breathe, name it, choose" (units 6, 11, 18, 24); the talk turn card "listen, say back, ask a question, add
  your idea" (a listening card, unit 5, day 49; it is not team talk); the goal steps card "goal, steps, block and plan, check" from grade 4
  on (units 14, 17). SEL 3 to 5 grows the goal card to four steps on its day 54 (grade 3 week 27), so units 4 and 7
  (days 36 and 67) use the K to 2 grade 2 form the class knows, "my goal and one step; a helper and a check; a changed
  step", retrieved from g2-goals. The I-statement card ("I feel ___ when ___ because ___. I need ___.") is SEL's and health's; PE uses it only
  where SEL has taught it and claims no part of it. Team talk is health's conflict steps, the PE K to 2 unit 17
  model: the grade 2 form "stop, say what happened, listen, find a fair way, and an adult helps when words do not work" (health K to 2 day 72) on days 49, 103 and 181 and their uses, then from the grade
  5 mid-year check (day 203, week 18) the grade 5 form "stop, calm down, each says their side, find a fair way, or walk away and get help" (health 3 to 5 day 77, unit 18, week 17).
- **Equipment and safe use.** The supplies columns are math and science only, so every movement day's note ends
  with its unit's space line: the safe space, the equipment, the no-equipment path and the wet-day path (every day
  names one), plus water and shade on warm outdoor days. Mats come from the school's stock, inspected and
  placed as the school's policy says; where there are no mats, no roll or hands-down task is done and the standing
  version is recorded as an adaptation. No inverted balances. Money: the band's ceiling is about $480 of new buys
  (decided by Cory 2026-11-26), grade 3 about $220, grade 4 about $115, grade 5 about $145.
- **Supports and values.** Every task has an adaptation (equipment size, distance, speed, rules, roles); a child
  with an injury or a medical condition follows the nurse's and family's guidance with a moving or seated helping
  role. Groups and teams are made by the teacher, quickly and privately. No exercise as punishment, no elimination,
  no human targets, no public team picks, no activity split by gender; every small-sided game offers a more and a
  less competitive court the child chooses.
- **Sensitivity.** Cultural dances and games (Virginia Reel and Alunelul in unit 8, La Bastringue in unit 15, jianzi
  and Pilolo in unit 16) are candidates until the sensitivity agent confirms each at the community's own
  institution or a public folklife archive; the days say so, and any school or family may swap one. Emotions (units
  6 and 24), food (unit 20) and water (unit 23) carry the frame's flags on the day. Every teacher page carries
  health's "If a student tells you something" steps.

## Year 3 (grade 3 rows, course days 1 to 80)

### Unit 1. Warm up, move safe

Days 1 to 11, weeks 1 to 5. *How do I get my body ready, stay safe when the game keeps changing, and stay safe
without being reminded?* Owns g3-warm-cool (SHAPE.S2.5.11), g3-safe-movement (S2.5.1), g3-stay-safe-own (S3.5.4).

Arc: a freeze-tag hook at walking pace in a fixed area and the warm-up routine (day 1), the safe-movement cues with the baseline watch (day 2), the
cool-down (day 3), the stay-safe signals with one water line, a life jacket on a boat or when playing in natural water (day 5), tag games with no one out (Fluency days 4, 6,
8), a changing-setting tag day with the warm-up card (day 7). Check days 9 and 10 (skill in groups, then the
warm-up and cool-down knowledge task), respond day 11. Retrieval: g2-stretch-why (day 1), g2-chase-flee and
g2-show-ideas (day 2), g2-rules-fair (day 5). Health grade 3 unit 1 runs the same weeks; PE teaches its own warm-up.
Candidate kept: the partner-led warm-up card (day 7, 15 minutes).

### Unit 2. Throw, roll, catch

Days 12 to 22, weeks 5 to 9. *What are the key parts of a good throw, and how do I use them to hit a target and catch
what comes back?* Owns g3-throw-roll-catch (S1.5.9, S1.5.10, S1.5.12), g3-key-parts (S2.5.15).

Arc: the overhand throw with the baseline (day 12), catching at three levels (13), the roll and the underhand throw
(14), the key-parts card (16), Fluency stations (15, 17, 19), target challenges with a stepping partner (18; begun
toward S1.5.17, written `~SHAPE.S1.5.17`). Check days 20 and 21 (overhand throw and catch at a middle and a high level marked apart; the roll and an underhand throw to a hoop, each marked apart, then the key parts), respond day 22.
Retrieval: g2-overhand-throw, g2-ball-skills-combine (day 12), g2-show-ideas (16). Candidate kept: the partner
key-parts checklist (day 18).

### Unit 3. Jump, land, balance, roll

Days 23 to 32, weeks 10 to 13. *How do I land softly, hold a balance on different body parts, and roll safely on a
mat?* Owns g3-jump-land-balance (S1.5.7, S1.5.8), g3-body-roll (S1.5.3).

Arc: landings with the baseline (23), balances and the base of support (24), body rolls on mats (25), a low partner
balance (27), Fluency stations (26, 28, 30), a balance course (29). Check day 31 (landings and balances watched, the
roll mark carried from day 30; base-of-support knowledge; mat-carrying conduct), respond day 32. Retrieval: g2-travel-jump-balance (23). Medical rule on every roll
day; no mats means no roll and an adaptation is recorded. Candidate kept: the drawn balance card (day 29).

### Unit 4. Why we move

Days 33 to 42, weeks 14 to 17. *Which activities build my heart, muscles and flexibility, and how does moving help
my health and let me show who I am?* Owns g3-health-fitness (S2.5.7), g3-benefits (S2.5.13), g3-express-benefits
(S4.5.1, S4.5.3).

Arc: the fitness-parts chart with a mystery circuit (33; baseline on unit 3's landing cue), the benefits by moving
(34, a heart-is-a-muscle reteach where day 33's retrieval shows a gap), favorite activities and the goal steps card in its K to 2 form (36),
health benefits explained (37), circuits (35, 38, 40), a class-planned circuit (39). Check day 41 (circuit with soft
landings; the chart match, two benefits, the two S4 sentences; encouragement), respond day 42. Retrieval:
g3-warm-cool, g3-jump-land-balance and g1-heart-muscle (33), g2-difficulty-lookback and g2-goals (36), health's hour a day in one line. Body
composition is not taught as a body measure. Candidate kept: the private "how I like to move" card (day 39).

### Grade 3 mid-year check (days 43 to 45, week 18)

See Course-level checks.

### Unit 5. Feet and hands on the move

Days 46 to 54, weeks 19 to 22. *How do I keep a ball close while I move it with my feet or my hand, and how do I make
sure everyone in my group gets a turn?* Owns g3-foot-skills (S1.5.18, S1.5.20), g3-hand-dribble (S1.5.19),
g3-kind-groups (S3.5.3).

Arc: the laces kick with the baseline (46), the foot dribble (47), the hand bounce with its baseline (48), kindness
in groups with SEL's talk turn card and team talk (49), stations (50, 52), group dribble-and-pass tasks in a changing maze, no
defenders (51). Check day 53 (kick and foot dribble marked apart, the hand bounce carried from day 52; plant foot and
eyes-up knowledge; passes to everyone), respond day 54. Retrieval: g2-ball-skills-combine (46), g3-safe-movement
(47), g2-talk-problems (49). SEL grade 3 unit 4 runs beside this unit. Candidate kept: the "everyone touched it"
group check (day 50).

### Unit 6. Strike with tools

Days 55 to 62, weeks 22 to 25. *How do I hit a ball with a bat or a paddle, and which calming method works best for
me when I miss?* Owns g3-strike-tools (S1.5.11, S1.5.16), g3-calm (S4.5.9).

Arc: the paddle with the baseline (55), the long tool off a tee (56), choosing a calming method from SEL's card
(57), stations (58, 60), a target-zone day (59). Check day 61 (long-tool contacts, paddle marks carried; the calming
method named and shown; swing space), respond day 62. Retrieval: g3-throw-roll-catch (55), g2-long-strike (56); SEL
unit 1 taught the card first. Emotions flag on day 57. Candidate kept: the private calm card (day 59).

### Grade 3 year-end check (days 63 to 65, week 26)

See Course-level checks.

### Unit 7. Rope and moving outside class

Days 66 to 72, weeks 27 to 29. *How many ways can I jump a rope, and how can I be active outside PE this week?* Owns
g3-rope (S1.5.6), g3-active-outside (S4.5.8).

Arc: forward and backward jumps, each child's first count as the baseline (66), the step-and-jump, the long rope and
the week's try outside class on the goal steps card in its K to 2 form (67), the partner rope and adapted ropes (68), rope stations
(69, 70). Check day 71 (ten in a row against the child's own first count in two tasks, self-turned forward and one of the child's choice, each marked apart; the activity outside class and how it
went; rope space), respond day 72. Retrieval: g2-rope-fixed (66), g2-goals (67), health's hour a day and goal
sentence. Counting to 100 only, never compared. Candidate kept: the recess rope rhyme (day 69, 5 minutes).

### Unit 8. Dance steps

Days 73 to 80, weeks 30 to 32. *How do steps become a phrase, and how do two dances from different places use the
beat?* Owns g3-dance-steps (no owned code; begun toward S1.5.1 and S1.5.5, owned in grade 4, written `~` on days 73 to 79).

Arc: four-count phrases with the baseline (73), the Virginia Reel (74, 75), Alunelul (76), both dances (77), the two
compared (78). Check day 79 (a four-count pattern in each; one difference; kindness in the line), respond day 80,
where the grade 3 skill sheet goes on to grade 4. Retrieval: g2-dance-sequence (73) and dance 3 to 5 unit 1's
elements (weeks 1 to 8); PE teaches only the motor skill. Cultural flag on days 74 and 76: candidates until the
sensitivity agent confirms them; no gender roles, no costume, swap allowed. Candidate kept: partner coaching of one
phrase (day 77).

## Year 4 (grade 4 rows, course days 81 to 160)

### Unit 9. Pulse, agility and the fitness chart

Days 81 to 90, weeks 1 to 4. *What does my pulse tell me about how hard I am working, and which activities build
speed, balance and quick reactions?* Owns g4-pulse-body (S2.5.12, S2.5.14), g4-skill-fitness (S2.5.10).

Arc: finding the pulse (81), the pulse after activity and body changes (82), skill-related fitness on the chart with
the baseline (83), stations (84, 86, 88), labeled stations (85), a changing circuit (87). Check day 89 (an activity
for a named part, the led warm-up carried; pulse and body change, two activities that raise the heart rate, a part
matched; station conduct), respond day 90.
Pulse at the neck: gently, two fingers, one side only (from memory; the safety agent checks).
Retrieval: g3-warm-cool, g3-benefits (81), g3-health-fitness (83), g3-warm-cool again (86). Science lean (later):
one line, "the heart pumps blood to the working muscles"; science grade 4 unit 6 (weeks 24 to 30) comes later and no
structure model is asked. Counting only, no beats per minute; counts private. Health grade 4 unit 8 runs the same
weeks. Candidate kept: the private before-and-after pulse card (day 85).

### Unit 10. Pass, gather, move and send

Days 91 to 101, weeks 5 to 9. *How do I pass to a partner who is moving, and why does each cue make my throw or kick
work?* Owns g4-pass-gather (S1.5.17), g4-move-and-send (S1.5.21), g4-object-ideas (S2.5.4).

Arc: the hand pass to a standing partner with the baseline (91), to a moving partner with hands and feet (92), why
each cue works (93), moving then sending (95), stations (94, 96, 98), invented pass-and-move patterns (97). Check
days 99 (five passes in a pair to a partner moving a few steps, with the hands, then three with the feet) and 100 (dribble-and-send; why a cue helps), respond day 101. Retrieval:
g3-throw-roll-catch (91), g3-foot-skills (92), g3-key-parts (93), g3-hand-dribble (95). Candidate kept: pair-invented
patterns (day 97).

### Unit 11. Attack together

Days 102 to 112, weeks 9 to 13. *How does my team move the ball into the other team's area, and how do we decide who
does what so everyone is part of it?* Owns g4-attack-ideas (S2.5.2), g4-team-roles (S3.5.1, S3.5.2), g4-with-others
(S4.5.2, S4.5.5).

Arc: attacking cues in three-on-three keep-away, baseline on unit 10's pass in play (102), team talk to decide roles
and how others see it (103), connections and group difficulties (105), keep-away and end-zone games (104, 106, 109),
games with a built-in problem (107), rotating roles (108). Check days 110 (moving to open space; roles by team talk)
and 111 (attacking moves, the left-out player's view, a connection and a difficulty with its fix), respond day 112.
Retrieval: g3-safe-movement, g4-pass-gather (102), g3-kind-groups and SEL grade 4 unit 7's working agreement (103),
g3-express-benefits (105), g3-calm (107; SEL grade 4 unit 10 comes later, so the grade 3 card is used). Candidate
kept: the group plan card (day 107).

### Unit 12. Volley, bump and serve

Days 113 to 122, weeks 14 to 17. *How do I keep a light ball in the air with my hands, and how do I serve it into
open space?* Owns g4-hands-strike-levels (S1.5.13, S1.5.14), g4-serve (S1.5.15).

Arc: the volley with the baseline (113), the bump (114), stations (115, 117, 120), the underhand serve (116), a
changing-height day and a cooperative volley, no scoring (118), a hit-choice challenge (119). Check day 121 (volleys
and bumps marked apart, serve carried from day 120; which hit for which height; court conduct), respond day 122.
Retrieval: g3-throw-roll-catch (113), g3-strike-tools (116). Candidate kept: beating one's own first wall-volley
count (day 117).

### Grade 4 mid-year check (days 123 to 125, week 18)

See Course-level checks.

### Unit 13. Chains and weight on the hands

Days 126 to 134, weeks 19 to 22. *How do I link runs, leaps, rolls and balances into one smooth chain, and move my
weight onto my hands and back?* Owns g4-travel-chain (S1.5.1), g4-feet-hands-weight (S1.5.2).

Arc: two-part chains with the baseline (126), the bunny hop and donkey kick (127), chain stations (128), the bear
walk to frog jump inside a chain (129), feet-to-hands stations (130), a four-part chain with a chain map (131), last
practice (132). Check day 133 (four-part chain, the shift carried; the idea changed between links; mat conduct),
respond day 134. Retrieval: g3-jump-land-balance, g3-body-roll, g3-dance-steps (126). Candidate kept: the chain map
(day 131).

### Unit 14. Sequences and strengths

Days 135 to 142, weeks 22 to 25. *How do I build a sequence with a clear start and end, and what are my strengths and
where should I practice next?* Owns g4-in-place-sequence (S1.5.4), g4-reasons-strengths (S4.5.4, S4.5.7).

Arc: start shape, five parts, end shape, first full try as the baseline (135), practice (136, 138, 140), strengths
and reasons from the skill sheet on the goal steps card (137), the sequence changed by its maker (139). Check day
141 (the sequence against its baseline; a strength, a practice place, a reason; a kind comment), respond day 142.
Retrieval: g4-travel-chain, g4-feet-hands-weight (135), g3-active-outside, g3-express-benefits (137). Candidate kept:
the sequence card (day 136).

### Grade 4 year-end check (days 143 to 145, week 26)

See Course-level checks.

### Unit 15. Dance sequences and movement ideas

Days 146 to 153, weeks 27 to 30. *How do I link moves into a dance with a beginning, a middle and an end, and how do
level, pathway, effort and shape change it?* Owns g4-dance-sequence (S1.5.5), g4-dance-ideas (S2.5.6).

Arc: a Curio Class line dance with the baseline (146), the four movement ideas, unit 14's sequence redone (147), La
Bastringue (148), both dances and a rope rhythm station (149), a ribbon solo (150), last practice (151). Check day 152
(a sequence with beginning, middle and end in two of the unit's styles, each marked apart, the second carried from
day 151's closure watch; the idea changed in four routines the teacher shows: dance, gymnastics,
rope rhythm, ribbon solo, one prompt for each setting S2.5.6 names), respond day 153, which also holds the
readiness check for unit 16 on g1-world-games. Retrieval: g3-dance-steps and dance 3 to 5 unit 5's elements (146),
g3-key-parts, g4-in-place-sequence (147), g3-rope (149). Cultural flag on day 148 (tune only, no lyrics). Candidate
kept: groups change one idea in the line dance (day 150).

### Unit 16. Activities from around the world

Days 154 to 160, weeks 30 to 32. *What do children play and dance in other places, and what can we learn about each
activity from where it comes from?* Owns g4-world-activities (S3.5.7).

Arc: jianzi in small circles with the baseline (154; the readiness results set how long the games-from-other-places
recap runs), Pilolo in marked lanes (155), jianzi practice (156), both
games with the map (157), last practice (158). Check day 159 (five kicks; both games described, how each is played and where each comes from;
the group counts every member), respond day 160, where the grade 4 skill sheet goes on. Retrieval: g3-foot-skills
(154), g3-safe-movement (155). Social studies: the grade 3 world map the year before; grade 4 unit 7 runs the same
weeks and neither waits. Cultural flag on days 154 and 155; the unit plan names Pilolo only in the version confirmed
at a Ghanaian institution. Candidate dropped: the family-shared game (day 157 note says why: family consent and a
source check per game do not fit a day); the family note invites families to play one at home instead.

## Year 5 (grade 5 rows, course days 161 to 240)

### Unit 17. My fitness plan

Days 161 to 174, weeks 1 to 6. *How can how often, how hard, how long and what kind help me reach a fitness goal, and
what can technology tell me about it?* Owns g5-fitt (S2.5.9), g5-goal (S2.5.8, S4.5.6), g5-tech (S2.5.16).

Arc: FITT on the plan card (161), setting a goal at a goal station (162), the baseline day and the four- to six-week
plan on the goal steps card (163), changing one FITT part (164), technology and its limits (166), goal practice and
circuits (165, 167, 169, 171), a plan changed (168), a group-planned circuit (170). The weekly goal check runs in
the warm-up of every day from 164 to 171, so a dropped day never takes the week's check. Check days 172 and 173 (unit
days 12 and 13 as the frame sets: the goal station marked for the cue, never the count; FITT change, goal steps, a
tool and a limit), respond day 174. Retrieval: g4-pulse-body, g4-skill-fitness (161), g4-reasons-strengths (162).
Math lean (later): a scaled bar graph of the child's own counts from math grade 3 unit 1 (day 167); 5.G.A.2 comes in
weeks 27 to 30, so no line graph on coordinates. Health grade 5 unit 15 runs the same weeks: one log, not two.
Candidate kept: the family-shared home activity on the FITT card (day 168).

### Unit 18. Invasion games

Days 175 to 187, weeks 6 to 11. *How does my team attack and defend in a small game, and how do we settle it when we
disagree about a call?* Owns g5-defend-ideas (S2.5.3), g5-conflict-solve (S3.5.5); g5-invasion-skills uses SHAPE.S1.5.17
to S1.5.21 in new settings (no claim).

Arc: defending cues with the baseline (175), passing stations with a passive defender (176), the three settings of
S3.5.5 taught and watched in turn, alone (177), with a partner (179) and in a small team (181, with the calm-down card and
team talk and a scripted scene of invented players), soccer-style and basketball-style three-on-three games
(178, 182, 183), defend-and-attack stations (180, 184). Check days 185 (skill in a game; a call settled in a game or
scene, the alone and partner marks carried, so S3.5.5 is checked in all three settings) and 186 (defending moves),
respond day 187. Retrieval: g4-attack-ideas, g4-pass-gather, g4-move-and-send (175), g4-team-roles and SEL grade 4
unit 11 (181). Health unit 18 and SEL unit 16 come later in grade 5, so team talk keeps the grade 2 form here. Candidate kept: each team's disagreement rule
(day 181).

### Unit 19. Net and wall games

Days 188 to 196, weeks 12 to 15. *How do we keep a rally going over a net, and how can we change a game's rules to make
it work better?* Owns g5-problem-solve (S2.5.5); g5-net-wall-skills uses S1.5.13 to S1.5.16 in new settings.

Arc: a cooperative rally with the baseline (188), net stations (189, 194), solving a game problem (190), net games
(191, 193), the rule-change test (192). Check day 195 (a three-hit rally, the serve carried; a problem, the change
and what happened; honest calls, begun toward S3.5.6, written `~` on days 193 and 195), respond day 196, which holds the readiness check for unit 20
on g2-foods-energy. Retrieval: g4-hands-strike-levels, g4-serve (188), g4-team-roles (190). Candidate kept: the class
rule-change log (day 192).

### Unit 20. Fuel for moving

Days 197 to 202, weeks 15 to 17. *How does what I eat and drink change how I feel and play?* Owns g5-food-drink
(S2.5.17).

Arc: water before, during and after inside a circuit, baseline on unit 1's warm-up and cool-down (197; the readiness
results set how long the food-gives-energy recap runs), energy foods
and a recovery snack (198), circuit rounds with the sort (199), a long-game day (200). Check day 201, respond day 202.
Retrieval: g4-pulse-body, g3-warm-cool (197), health grade 3 unit 2 and health grade 5 unit 15. Food flag on every
day: never good or bad, never about body size, no calorie or diet talk, allergies respected. Candidate kept: the
private "what helps me play" card (day 200).

### Grade 5 mid-year check (days 203 to 205, week 18)

See Course-level checks. Day 205 holds the readiness check for unit 21 on g3-strike-tools.

### Unit 21. Striking and fielding

Days 206 to 214, weeks 19 to 22. *How do we hit, run and field in a fair game, and how do we make fair calls with no
referee?* Owns g5-fair-decisions (S3.5.6); g5-strike-field-skills uses S1.5.10 to S1.5.12 and S1.5.16 in new
settings.

Arc: hit, run, field, throw with the baseline (206, the readiness results set the swing reteach), fair decisions and
customs (207), stations (208, 212), self-officiated tee games (209), gentle-pitch games (210), fielding problems
(211). Check day 213, respond day 214. Retrieval: g4-pass-gather (206), g5-conflict-solve and g4-team-roles (207).
Candidate kept: the team fair-call card (day 209).

### Unit 22. Routines

Days 215 to 222, weeks 22 to 25. *How do I build a routine of eight parts that joins rope, gymnastics and dance, and
perform it twice the same?* g5-gym-dance-sequence owns no code; it uses S1.5.1, S1.5.2, S1.5.4, S1.5.5 and S1.5.6 in
new settings, and S2.5.6 in review.

Arc: the routine card (215), parts practice with the first full try as the baseline (216), links and one idea
changed (217), run-throughs (218, 220), performed twice and fixed (219). Check day 221, respond day 222. Retrieval:
g3-rope, g4-travel-chain, g4-feet-hands-weight, g4-in-place-sequence, g4-dance-sequence (215), g4-dance-ideas (217),
and dance 3 to 5 unit 9's elements. Candidate kept: the symbol routine card a partner reads (day 218).

### Grade 5 year-end check (days 223 to 225, week 26)

See Course-level checks. Day 225 holds the readiness check for unit 23 on g2-water-skills.

### Unit 23. Safe near water

Days 226 to 232, weeks 27 to 29. *What would I do if someone were in trouble in the water, and what do floating and
swimming strokes look like?* Owns g5-water-skills (S1.5.22, S2.5.18).

Arc: the reach rescue with the water rules taught here (226; health's safe-places unit was two grades back), the
throw rescue and the buddy rule (227), the life jacket fit and the strokes on the floor (228), stations (229, 230).
Check day 231 (dry-land part of S1.5.22 for every school; simple swimming only in a school's own aquatics program),
respond day 232. Water flag on every day: no child enters water. Rescue steps (call for help first, reach lying on
the stomach, throw something that floats, never go in) are sourced on days 226, 227 and 231 to the Drowning Prevention
Coalition of Palm Beach County's "Reach, Throw, Don't Go" page (opened 2026-11-26); CDC's page supports life jackets
and supervision only. The readiness results from day 225 shape day 226.
New in this band: the buddy rule and floating and strokes shown on the floor, with the fit check added to K to 2's
fastening. Candidate kept: the family water-safety card (day 230), which names those steps.

### Unit 24. Looking back on PE

Days 233 to 240, weeks 30 to 32. *What has PE meant to me, and what will I take with me?* Owns g5-review-experiences
(S4.5.10).

Arc: the scrapbook page and grade 3 review stations (233, 234), grade 4 stations and the calm steps (235), grade 5
stations (236); days 234 to 236 are the band's spaced review of S1 before grade 6, so a unit plan does not pad them, the three-year skill sheet read and a growth station chosen (237), last practice (238). Check day
239, respond day 240, where the three-year records go on to grades 6 to 8. Retrieval: g5-goal, g3-calm (233); SEL
grade 5 unit 13 taught the calm-down card this year. Emotions flag: no right answers, a hard moment is the child's
to keep. Candidate kept: the "what we can do now" picture wall with no names (day 237).

## Course-level checks

Each check uses new stations and settings (no task form from the two weeks before), collects once (the unit just
checked is carried, not collected again), watches a child once in the window, and gives a prompt for each part of
each code it lists.

| Check | Days | Week | Samples (codes on the day rows) |
|---|---|---|---|
| Grade 3 mid-year | 43, 44; respond 45 | 18 | S2.5.1, S1.5.10, S1.5.12, S1.5.9, S3.5.4 (day 43); S1.5.7, S1.5.8, S2.5.11, S2.5.15 (day 44). Unit 4 carried |
| Grade 3 year-end | 63, 64; respond 65 | 26 | S1.5.18, S1.5.20, S1.5.19, S1.5.10, S3.5.3 (63); S1.5.3, S2.5.7, S2.5.13, S4.5.3, S4.5.1 (64). Unit 6 carried |
| Grade 4 mid-year | 123, 124; respond 125 | 18 | S2.5.10, S1.5.17, S1.5.21, S2.5.2, S3.5.2 (123); S2.5.12, S2.5.14, S2.5.4, S2.5.2, S4.5.5 (124). Unit 12 carried |
| Grade 4 year-end | 143, 144; respond 145 | 26 | S1.5.13, S1.5.14, S1.5.15, S1.5.1, S1.5.2, S1.5.17 (143); S2.5.10, S1.5.1, S4.5.2, S3.5.1 (144). Unit 14 carried |
| Grade 5 mid-year | 203, 204; respond 205 | 18 | S4.5.6, S2.5.8, S1.5.17, S1.5.21, S1.5.13, S1.5.14, S3.5.5 (203); S2.5.9, S2.5.16, S2.5.3, S2.5.5, S4.5.6 (204). Unit 20 carried |
| Grade 5 year-end | 223, 224; respond 225 | 26 | S1.5.10, S1.5.12, S1.5.11, S1.5.16, S1.5.17, S3.5.6 (223); S2.5.17, S3.5.6, S2.5.9, S4.5.6, S2.5.8 (224). Unit 22 carried |

Every standard (S1 to S4) is sampled in each year's two checks. Added to the frame's table, all cheap and inside the
same stations: the roll to a target (S1.5.9) at grade 3 mid-year, the laces kick (S1.5.18) and a health benefit
explained (S4.5.3) at grade 3 year-end, the bump (S1.5.14) at grade 4 year-end, the tee hit (S1.5.11) and the paddle
rally (S1.5.16) at grade 5 year-end.

**Codes no course-level check samples (12 of 57), with the reason.** Each is checked in its own unit's end-of-unit
check. Carried by collect-once (the unit's check was days before the year-end check): S4.5.9 (unit 6), S1.5.4,
S4.5.4, S4.5.7 (unit 14). In units that come after the year-end check, the last units of each year: S1.5.6, S4.5.8
(unit 7), S1.5.5, S2.5.6 (unit 15), S3.5.7 (unit 16), S1.5.22, S2.5.18 (unit 23), S4.5.10 (unit 24). The frame puts
those units after week 26 on purpose (K to 5 weeks 28 to 32 are mostly core check weeks).

## Shorter path

**The 64-session year** (the frame's path, 16 of 80 days dropped a year). Only Fluency days, at most 3 a unit, never
a unit's last Fluency day, a check, respond, baseline, readiness or first-teaching day. Each dropped day's work folds
into the next practice day of its unit as its opener. Every unit keeps at least one Fluency day, and every owned
code keeps its teaching day and its check.

| Year | Dropped days |
|---|---|
| 3 | Fluency: 4, 6 (unit 1); 15, 17 (2); 26, 28 (3); 35, 38 (4); 50 (5); 58 (6); 69 (7, the rope rhyme moves to day 70); 75 (8). Application, as the frame allows: 7 (1), 18 (2), 51 (5), 59 (6) |
| 4 | Fluency: 84, 86 (9); 94, 96 (10); 104, 106 (11); 115, 117 (12); 128, 130 (13); 136, 138 (14); 149 (15, the rope station moves to day 150); 156 (16). Application, as the frame allows: 87 (9), 119 (12) |
| 5 | Fluency: 167 (17, the bar graph moves to day 171); 176, 180 (18); 189 (19); 208 (21); 218 (22); 229 (23); 234, 236 (24). Application game days in units of 9 or more days, as the frame allows: 183 (18), 191, 193 (19), 210, 211 (21). Application in units of 6 or more days, as the frame allows: 200 (20, its card folds into day 201's opener), 219 (22) |

Units at three drops: 18, 19, 21 (the frame's ceiling). Units 7, 8, 15, 16, 17, 20 and 23 lose at most one day. Unit 17
keeps seven sessions between the baseline (day 163) and the check (day 172), about four weeks at 2 a week, with the
weekly goal check in every warm-up, so S4.5.6's longer goal holds on the short path.

**A year about 10 days short, by named fold-in days.** Ten school days short is about 5 sessions at 2.5 a week (school
day 2n). Each year names 5 fold-in days from the list above: those 5 sessions (175 minutes) are not met, and each
day's cue survives as a 10-minute segment of the day named; none is assessed, a baseline or a first-teaching day.

| Year | Fold-in day | Folds into | Saves |
|---|---|---|---|
| 3 | 6, 17, 28, 38, 58 | 8, 19, 30, 40, 60 | one 35-minute session each, 5 sessions (175 minutes) in all |
| 4 | 86, 96, 106, 117, 130 | 88, 98, 109, 120, 132 | 5 sessions (175 minutes) |
| 5 | 167, 180, 189, 218, 236 | 169, 184, 194, 220, 238 | 5 sessions (175 minutes) |

A school that loses more uses the rest of the 64-session list in order.

**A shorter period** (25 to 30 minutes instead of 35) keeps every day: the warm-up and cool-down shorten to 2
minutes each and the closure watch keeps its place. Units with one check day hold the rotation and the knowledge task
on the check day and drop that day's focus block.

**Leave-out units and swaps.** A school or family may swap a cultural game or dance (units 8, 15, 16). A unit left
out takes its owned codes off the course page's claim; no other unit claims them. Where a later unit uses a card a
left-out unit made, that unit teaches the card's one-step form in its first ten minutes and claims none of the
left-out sub-skills: the fitness-parts chart (unit 4, used by units 9 and 17), the goal steps card (unit 4 or 7, used
by 14 and 17), team talk in health's conflict-step words (unit 5, used by 11 and 18), the calming card (unit 6, used by 11 and
24), chains and sequences (units 13 and 14, used by 22), the volley, bump and serve cues (unit 12, used by 19), and
long-tool striking (unit 6, used by 21, whose readiness check then becomes a 10-minute swing teach).

## Logic model (one page)

| Year | Inputs | Activities | Outputs | Outcome claimed |
|---|---|---|---|---|
| 3 | 80 sessions of 35 minutes; cue, task and game cards; the K to 2 closet and about $220 of new buys | Units 1 to 8 | Eight unit checks, two course-level checks, a private skill sheet per child | The grade 3 outcomes above, standards S1 to S4 |
| 4 | The same, about $115 of new buys | Units 9 to 16 | The same | The grade 4 outcomes |
| 5 | The same, about $145 of new buys (four youth life jackets among them) | Units 17 to 24 | The same, plus each child's four- to six-week goal record and three-year records passed to grades 6 to 8 | The grade 5 outcomes |

Nothing here has been tried with children, and Curio Class makes no claim of any effect on fitness or health.

## Sources not loaded

- CDC's PECAT 2019 grade 3 to 5 tables and the appropriate practice guidelines (2009): read by the frame for
  placement, not loaded in data/standards; no day quotes them.
- The cultural sources for Virginia Reel, Alunelul (unit 8), La Bastringue (unit 15), jianzi and Pilolo (unit 16): no
  community institution's page is loaded or confirmed; the Library of Congress dance-manual record is a browser
  check (403 to the frame's read).
- SHAPE America's elementary time guideline page (cited by the frame for the 150-minute line) and CDC's "Preventing
  Drowning" page (opened 2026-11-25; life jackets and supervision, no rescue steps) are cited, not loaded.
- Water rescue steps (unit 23): the Drowning Prevention Coalition of Palm Beach County, "Reach, Throw, Don't Go"
  (https://discover.pbc.gov/drowningprevention/Pages/Reach-Throw-DontGo.aspx, opened 2026-11-26: call for help, reach
  lying down with a long object, throw something that floats, never jump in). The Red Cross WHALE Tales lesson 8,
  "Reach or Throw, Don't Go", returned 403: browser check. The neck-pulse caution (day 81) is from memory.

## For the lead

1. **The 64-session path cannot be all Fluency in grades 3 and 4, nor in grade 5 with S4.5.6 kept whole.** The frame says about 30 Fluency days a year, but
   with its own rules (at most 3 a unit, never the last Fluency day, never a first-teaching day) grade 3 has only 12
   droppable Fluency days and grade 4 only 14. This scope drops 4 Application days in grade 3 (7, 18, 51, 59) and 2
   in grade 4 (87, 119), each folding into the next practice day. The frame's fix: allow one Application day in any
   unit of 8 or more days on the short path in grades 3 and 4, as grade 5 already does, or give the frame's Fluency
   count as "about 20 in grade 3, 23 in grade 4". Grade 5 now also drops Application days 200 (unit 20) and 219 (unit
   22) so unit 17 loses only day 167 (sequence read 2026-11-26, finding 2); the read's fix is to allow an Application
   drop in any unit of 6 or more days where Fluency runs out. Raised for the structure pass.
2. **Codes added to course-level checks.** S1.5.9 (grade 3 mid-year), S1.5.18 and S4.5.3 (grade 3 year-end), S1.5.14
   (grade 4 year-end), S1.5.11 and S1.5.16 (grade 5 year-end), so more of the earlier units' codes are sampled. The
   frame's table may add them, or the lead may strike them.
3. **school_day** is the even 2n spread over the band (2 to 480), which reads as the frame's weeks.
4. **Frame items 4, 6 and 7 stand:** the bar-graph fallback is on day 167; health unit 15's one-log note is on days
   162 and 167 and health's frame still needs it; every cultural pick waits on the sensitivity agent.

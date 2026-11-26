# Scope and sequence: Health, grades K to 2

Course `health-grades-k-to-2` (catalog id `health-k-2`), a band course for kindergarten, grade 1 and grade 2, draft written 2026-11-26.

The day record is [days.csv](../../../data/plans/health-grades-k-to-2/days.csv): 84 course days, 28 a year for three years, in the frame's 17 units (24 unit days a year) and 12 course-level days (a mid-year check, a year-end check and a respond day after each, every year). `stretch` is the unit number in the frame's Units table and `unit` is `<unit>.1`, since no unit is split into sections. This file sets purposes and evidence slots, not items, keys or lessons. Health has no base text, so there is no source map.

## How the band runs

**Which grade's standards fall in which year.** National Health Education Standards, 2024, SHAPE America, PreK-2 span, by id only (our words in data/standards/nhes-2024.txt, never the indicator text). The span is written for K to 2 as a whole; each indicator has one owner grade (STANDARD.md section 4), and a year claims only its own owned ids:

| Year of the band | Course days | Units | Owned NHES ids claimed | Count |
|---|---|---|---|---|
| Kindergarten | 1 to 28 | 1 to 5 | S1.2.2, S1.2.4, S7.2.1, S2.2.1, S6.2.1, S4.2.1, S4.2.2, S4.2.5, S3.2.1, S5.2.1 | 10 |
| Grade 1 | 29 to 56 | 6 to 11 | S1.2.1, S1.2.3, S7.2.2, S3.2.2, S8.2.1, S4.2.3, S5.2.2, S1.2.6, S2.2.2, S5.2.3, S8.2.2, S6.2.2, S6.2.3, S6.2.4 | 14 |
| Grade 2 | 57 to 84 | 12 to 17 | S1.2.5, S1.2.7, S5.2.4, S3.2.3, S2.2.3, S4.2.4, S8.2.3, S6.2.5, S6.2.6 | 9 |

That is all 33 PreK-2 indicators. A day's `codes` cell lists the owned ids it works on and any id owned earlier in the course that it practices; an id owned by a later year that a day begins is written `~ID` in `codes` (the progression's form: begun here, counted as standard content, never claimed; days 19, 20, 22, 23 and 25). The sensitive units own no id; their days leave `codes` empty except day 25's begun `~NHES.S4.2.3`, and their notes name what they practice.

**How school_day is counted.** One 30-minute lesson a week, weeks 1 to 28 of each school year (the frame). `school_day` counts across the band the way scripts/frame.py spans it (28 meeting weeks a year, 140 school days a year): kindergarten is school days 1 to 140, grade 1 is 141 to 280, grade 2 is 281 to 420, and a year's own school day is the number less 140 or 280. Course day n of a year (n = 1 to 28) sits on that year's school day 5(n - 1) + 3, the Wednesday of week n, so its week is (school_day - 1) // 5 + 1 within the year, and the n-th day of a year is in week n. Checked with frame.py's calendar rows: every unit and check lands on the frame's weeks (table under Course-level checks).

**The day.** Each 30-minute lesson opens with a short scenario or the unit's compelling question (five minutes at most), then the work, then clean-up and collecting sheets; hand-washing days keep five minutes for washing and drying. A retrieval task takes five minutes of the opening. Most days hold a five-minute pair rehearsal of the step card in use. Children read nothing alone beyond a pictured word card; every scenario is read aloud or pictured, and every rehearsal and item can be done by pointing, drawing, a card or with an adult.

**Day kinds and the step card.** Kinds follow docs/GLOSSARY.md ("teaching day"). The first day a step card is shown, with the teacher saying each step aloud on a scenario (the model), is an Understanding day, because the card is new. Pairs then hold the card in the five-minute rehearsal of the next days, and the card is withdrawn in the last rehearsal before the check at the latest: on the day before each check the pairs rehearse with the card turned over (days 4, 10, 17, 23, 31, 37, 44, 49, 60, 65, 73 and 77), so no child meets the task without the card for the first time on a scored day. The end-of-unit assessment is always taken without it, and every said-aloud hearing (days 17 and 18, 37 and 38, 73 and 74) is taken with the card turned over, one condition for the whole record sheet. Three units have a whole Fluency day (4, 7 and 14), each practice only. One day is Application (day 43, the influence check without the card on new cases); most units first-teach a new row on nearly every day, so the skill on an unseen scenario without the card comes on the check day, and the leave-out paths add an Application day where a sensitive unit's days extend a unit. A card that returns in a later year gets one day with the card back, then goes without (APPROACH.md, "What is carried").

**Shared cards, word for word (SEL STANDARD section 7, K to 2 form).** Calm-down card: "stop, breathe" (the slow balloon breath) in kindergarten, count to five added in grade 1, then a stretch or asking for a break chosen by the moment in grade 2. I-statement: "I feel ___ when ___. I need ___." (grade 2 adds asking "What do you need?" and agreeing a fair end, day 70). Refusal second push: say it again, move away, tell (inside health's boundary steps, "say it, say stop again, move away, tell"). Goal steps card: "my goal and one step" (kindergarten), then a helper and a check (grade 1; day 49's plan ends "and when we will check"), then a changed step (grade 2); health's goal plan uses these rungs. Talk turn card: its two steps, "eyes look, wait my turn", open health's listening card (look, quiet body, wait, say back).

**End-of-unit assessments and response time (stated once).** Every unit's last day is its check day (`kind` Check, `assess` end): unseen pictured scenario cards read aloud, each child answering alone, scored met, partly or not yet on the skill steps with a guide, plus one facts-in-use item per fact the unit lists and one valuing item scored on whether the reason uses a unit fact, never on which choice. Never a fact-recall test, and never a score on a day a topic is first taught. In units 3, 7 and 14 the said-aloud step is heard from every child on a class record sheet, card turned over: ten children on the second-to-last day (`assess` observe; the observation records only the codes heard, and the note says so) and the rest on the check day at a side table while the others draw; any child not heard in the period is heard that week in the classroom routine, since health is the classroom teacher's course. Budget for 30 children: about a minute each. Response time: the last five minutes of each check day re-rehearse the step most often marked not yet, and each child's other not-yet steps return on the year's next course-level respond day, in groups from the record sheets. Doing indicators (NHES.S7.2.2 in unit 6, NHES.S6.2.5 in unit 15) are judged from the teacher's record of each child doing the routine or goal at school, never from a character's chart, never on health or whether a goal worked. Twice a unit each child rates their own use of the steps on a face card (the self-check days are named in each unit's notes). No unit runs over 25 days, so none has a mid-unit assessment.

**Readiness and retrieval.** No readiness check anywhere in the band: kindergarten assumes no earlier health course, and every row grades 1 and 2 assume was taught the year before (counted by grade number, sequence-write.md rule 2), so each opens as a five-minute retrieval task inside the day that needs it, listed in the `retrieves` column. Earlier-grade rows, their last use and treatment:

| Unit | Earlier row (last used) | Treatment, day |
|---|---|---|
| 6 | k-phw-wellness-parts (K) | retrieval, day 29 |
| 6 | k-phw-hand-washing; k-phw-sleep-rest (K) | retrieval, day 30 |
| 6 | k-phw-body-names (K), outside names only | retrieval, day 31 |
| 7 | k-s-trusted-helpers (K) | retrieval, day 33 |
| 7 | k-meh-feeling-words; k-meh-good-listening (K) | retrieval, day 34 |
| 7 | k-s-notice-a-choice; k-aod-medicine-safety; k-t-smoke-and-vapor (K) | retrieval, day 36 |
| 8 | k-phw-things-that-help (K); k-phw-sleep-rest (K) | retrieval, days 41 and 42 |
| 8 | k-fn-foods-for-growing; k-fn-water-first (K) | retrieval, day 43 |
| 8 | k-s-notice-a-choice (K); g1-s-choose-and-ask (grade 1, unit 7) | retrieval, day 44 |
| 9 | k-pa-move-every-day; k-s-safety-gear-and-cars; k-v-kind-words-and-hands (K) | retrieval, day 46 |
| 9 | k-s-trusted-helpers (K); k-phw-pick-a-habit (K) | retrieval, days 47 and 48 |
| 10 (sensitive) | k-v-body-safety (K, sensitive) | retrieval where unit 5 was taught, else the bridge, day 51 |
| 11 (sensitive) | k-v-kind-words-and-hands (K) | retrieval, day 53 |
| 12 | g1-phw-my-strengths; g1-phw-daily-habits (1) | retrieval, day 57 |
| 12 | g1-phw-stop-germs (1); g1-fn-snack-options (1) | retrieval, days 58 and 60 |
| 13 | g1-s-ask-for-help (1) | retrieval, day 62 |
| 13 | g1-pa-play-safe; g1-aod-medicine-helpers (1) | retrieval, day 64 |
| 13 | g1-s-unsafe-feels-wrong (1) | retrieval, day 65 |
| 14 | g1-meh-tell-a-helper; g1-phw-how-things-touch-me (1) | retrieval, days 69 and 70 |
| 14 | g1-s-unsafe-feels-wrong; g1-v-settle-without-hurting (1) | retrieval, days 71 and 72 |
| 15 | g1-pa-play-safe; g1-phw-name-a-goal; g1-phw-goal-helpers-and-steps (1) | retrieval, days 75 and 76 |
| 16 (sensitive) | g1-v-body-safety (1, sensitive) | retrieval where unit 10 was taught, else the bridge, day 79 |
| 17 (sensitive) | g1-sh-families-and-respect (1, sensitive) | retrieval where unit 11 was taught, else the bridge, day 81 |

Inside kindergarten, rows taught earlier the same year are retrieved where a later unit uses them (days 7, 9 and 20). The SEL feeling faces and calm-down card (SEL kindergarten unit 2, weeks 5 to 10) open unit 3 as retrieval; they are another course's rows, so they sit in the note, not in `retrieves`.

**Family notes and sensitive units.** Every unit sends its home task (a talk with a trusted adult the child chooses; a school adult counts) on its first day, English and Spanish, written when the unit is finished; no task asks about a child's home, food, body, feelings or family. Each sensitive unit (5, 10, 11, 16, 17) has its leave-out note on its first page and the longer family note sent home two weeks before, on the day named: unit 5 on day 23 (kindergarten week 23), unit 10 on day 49 (grade 1 week 21), unit 11 on day 51 (week 23), unit 16 on day 77 (grade 2 week 21), unit 17 on day 79 (week 23). A family note that falls on a left-out unit's day still goes home that week. Where one family opts out and the school keeps the unit, the child does a help-steps picture sort with another adult (a kind-words sort on day 53); day 3's opt-out is the washing rehearsal. Every sensitive teaching day carries the disclosure steps of unit 5. In those units rehearsal uses written scripts of the telling line only; the teacher or a card plays any pressure. Each year's sensitive units sit right before the year-end check, which never samples them.

## Kindergarten

### Unit 1: Healthy me (days 1 to 5, kindergarten weeks 1 to 5)

The year opens with healthy having parts (body, mind, friends), the sort the whole band uses. Hand washing is taught on day 2 at the sink in five pictured steps, so the school habit starts in week 2; the washing card is held by pairs on day 3 and withdrawn on day 4. Body names sit on day 3, week 3, so the family note sent on day 1 gives two weeks for preview and the quiet opt-out; day 3 and its family note are marked "person read before publishing" (later.csv L89). Sleep and a calm bedtime routine close the teaching on day 4. Self-checks on days 2 and 4. End-of-unit check on day 5 (order the steps, a washing moment and who it protects, the body, mind or friends sort, a sleep fact, a valuing item); no item on body names. No readiness check (no earlier course). Supplies: school soap and towels, $3 printing.

Candidate settled: the HECAT PHW PreK-2 read's possible dental expectation is kept as one "brush teeth" picture in day 4's bedtime list, 0 days added.

### Unit 2: Food, water and play (days 6 to 11, kindergarten weeks 6 to 11)

Three concrete, positive days first (foods that help us grow, water first, playing hard makes the heart beat faster), so the influence check on day 9 has things to sort, with unit 1's washing and sleep as its first "helps" (retrieval). Day 6's plate is "by color" in the rainbow sense (fruit and vegetable colors), never red, yellow or green food labels. The influence card is modeled on day 9, held by pairs on day 10 and turned over in day 10's last rehearsal, before the check. Day 10 teaches goal step 1, pick one habit from the safe list, the first rung of the shared goal card. Self-checks on days 9 and 10. End-of-unit check on day 11. The PE lean is a bridge here: PE kindergarten unit 6 (weeks 24 to 27) comes later, so day 8 states the heart fact itself with short bursts in a cleared classroom.

Candidate settled: hunger and fullness kept as one sentence inside day 6 (0 days); breakfast moved to unit 8's own Candidate, where a snack-and-meal scene already sits.

### Unit 3: Feelings and friends (days 14 to 18, kindergarten weeks 14 to 18)

Opens after the mid-year check, when routines are set. SEL kindergarten unit 2 (weeks 5 to 10) has taught the faces and the "stop, breathe" card, so day 14 opens with the faces as retrieval and spends its time on the I-statement, the frame this band keeps through grade 2. Day 15 uses SEL's calm-down card, not a health one; day 16 teaches the listening card, opened by SEL's talk turn steps, in the circle and a lunch or playground scene; day 17 teaches kind words and gentle hands. Where a school does not run SEL, days 14 and 15 teach the faces and the card in their first ten minutes. Self-checks on days 15 and 17. Said-aloud I-statement heard across days 17 (observe, ten children; it records NHES.S4.2.1 only) and 18 (the rest), card turned over; end-of-unit check on day 18, where each part is asked: the listening step in two pictured places with "says back" heard at the side table (NHES.S4.2.2), and one kind thing shown or said, pointed or acted with a puppet (NHES.S4.2.5).

Candidate settled: "show care for others' feelings" kept as one scene inside day 17, 0 days.

### Unit 4: Helpers and choices (days 19 to 24, kindergarten weeks 19 to 24)

The kindergarten getting-help unit, in a non-sensitive place so unit 5 can go. Day 19 teaches the two signs of a trusted adult and help step 1 with the model ask; day 20 is the unit's Fluency day (pairs rehearse "Can you help me?" with the I-statement words, retrieved from unit 3). Day 21 teaches "I have a choice"; days 22 and 23 apply it to gear, medicine and smoke under one action, "leave it and tell", with the year's plain-word norm on day 23, "most grown-ups do not smoke or vape". The help card is withdrawn on day 23's sort. Self-checks on days 20 and 23. End-of-unit check on day 24. SEL kindergarten unit 5 (weeks 20 to 25) runs alongside.

Candidate settled: street crossing kept as one scene on day 21 (0 days); "know my address" dropped, because it asks for a child's home address, which no health task asks, and the school keeps that record.

### Unit 5: My body is mine (sensitive, removable; days 25 to 26, kindergarten weeks 25 to 26)

Day 25 teaches body safety in simple words; day 26 rehearses the telling line from a script, then the end-of-unit check (point to "tell" and a helper). It owns no id; it practices NHES.S3.2.1 and previews NHES.S4.2.3. Family note on day 23.

Candidate settled: "surprises are okay, secrets about touch are not" is already in day 25, 0 days.

## Grade 1

### Unit 6: Habits that keep germs away (days 29 to 32, grade 1 weeks 1 to 4)

Germ habits build straight on kindergarten unit 1 and are used every school day, so they open grade 1. Day 29 retrieves the wellness parts and turns them into strengths, and starts the habits chart and the teacher's routine record for NHES.S7.2.2, kept through the unit. Day 30 teaches germs (too small to see; some spread from person to person and make people sick) with the teacher's washable-paint handshake and models the cough-and-wash card; pairs hold it on day 31, which also teaches protecting eyes, ears and skin (outside body names retrieved) and states the year's norm from the class's own routine tally; the card is turned over in day 31's last rehearsal. Self-checks on days 30 and 31. End-of-unit check on day 32, with the routine record carried into the judgment: it judges the routines every child does daily (washing before snack, own cup), with cough covering marked when seen, not required. The check asks for one strength card that is the child's own (the cards are safe actions only) beside a character's.

Candidate settled: hearing and vision checks kept as one sentence on day 31, 0 days.

### Unit 7: Asking for help (days 33 to 38, grade 1 weeks 5 to 10)

The grade 1 getting-help unit. Day 33 teaches the help steps; day 34 asks a helper about a worry with the I-statement (need: help) and the listening card, both back for one day, so standard 3 is met in mental health as well as safety; day 35 teaches what to do when something feels wrong (say stop, then the shared second push); day 36 teaches decision step 2 and the medicine helpers, with the found vape or pills scene moved here from day 35 so its kindergarten retrieval comes first. Day 36 opens with one retrieval picture ("I have a choice: leave it and tell") in place of three tasks, to keep its load. Day 37 is the unit's Fluency day, with the card turned over. Self-checks on days 34 and 36. Said-aloud help request heard across days 37 (observe; codes NHES.S3.2.2 and NHES.S8.2.1, what is heard) and 38, card turned over; end-of-unit check on day 38. It sits before the mid-year check because units 9 and 10 use its steps. SEL grade 1 unit 9 (weeks 10 to 15) follows with the same help words.

Candidate settled: "tell an adult if someone online asks for something" kept as one scene on day 35, 0 days.

### Unit 8: What shapes my health (days 41 to 45, grade 1 weeks 13 to 17)

Day 41 teaches how places affect health, with the shared-place idea for NHES.S1.2.6, and the kindergarten influence card back for one day; day 42 teaches "say how it touches me" with the model; day 43 is Application, the card withdrawn, on a plate, a water cup and an invented snack ad (the year's pressure case); day 44 teaches decision step 3, after unit 7's step 2. Self-checks on days 42 and 44. End-of-unit check on day 45, which asks each part: how an influence touches a character and "How could this touch you if it happened?" (NHES.S2.2.2, a hypothetical that asks for no history), and the shared-place prompt on a pictured home, school and street, none the child's own (NHES.S1.2.6).

Candidate settled: breakfast kept as one character's scene on day 44, 0 days, never asking a child about breakfast.

### Unit 9: Playing safe together, and a goal to try (days 46 to 50, grade 1 weeks 18 to 22)

Play-safe and settling share day 46 (a game gets rough), a week ahead of PE unit 12 (weeks 19 to 22), which teaches the heart and counting beats; health says the heart fact in one line. Day 47 teaches helping a friend choose safely; days 48 and 49 teach the goal frame, then helpers and steps on the shared goal card's grade 1 rung (the plan's last line, "and when we will check"; the card turned over in day 49's last rehearsal), so the plan goes home with ten weeks of the school year left. Self-checks on days 47 and 49. End-of-unit check on day 50 (the goal plan scored on its steps, one helping-a-friend scene). SEL grade 1 unit 12 (weeks 27 to 32) reuses the goal frame later.

Candidate settled: "warm up before play" kept as one line on day 46, 0 days.

### Unit 10: Keep telling (sensitive, removable; days 51 to 52, grade 1 weeks 23 to 24)

Day 51 teaches keep telling when the first adult does not help; day 52 rehearses from a script, then the check (point to the next helper). Owns no id; practices NHES.S4.2.3 and NHES.S3.2.2. If unit 5 was left out, day 51's first ten minutes give its one idea. Family note on day 49.

Candidate settled: a friend telling a worry kept as one scene on day 52, answered with the telling line, 0 days.

### Unit 11: Many kinds of families (sensitive, removable; days 53 to 54, grade 1 weeks 25 to 26)

Day 53 reads aloud a family story with families of many structures; day 54 is the check (pick the respectful words and say why). Owns no id; practices NHES.S4.2.5 and NHES.S2.2.2. Family note on day 51.

Candidate settled: one friendship scene kept on day 54, 0 days.

## Grade 2

### Unit 12: Staying well (days 57 to 61, grade 2 weeks 1 to 5)

Grade 1's habits gather into a reason (day 57), germ habits go deeper with the plain vaccine fact (day 58), day 59 teaches when a doctor or nurse visit is a good idea, and day 60 finishes the decision steps begun in kindergarten with step 4. Health comes before PE unit 18's foods-for-energy row (weeks 13 to 16), so day 60 names foods that give energy for play. Self-checks on days 58 and 60. End-of-unit check on day 61.

Candidate settled: dental checkups kept as one sentence on day 59, 0 days.

### Unit 13: Helpers and emergencies (days 62 to 66, grade 2 weeks 6 to 10)

The grade 2 getting-help unit. Day 62 builds the helper map (help card back for one day); day 63 teaches the emergency rule in full (adult first; if no adult can help, call 911 on a toy or paper phone); day 64 teaches the rules for water, bikes, fire and kitchens with their reasons, ahead of PE unit 22's dry-land water skills (weeks 28 to 32); day 65 rehearses "No thanks" from a script with a card playing the offer, with the year's norm. Self-checks on days 63 and 65. End-of-unit check on day 66. Unit 16 uses the helper map.

Candidate settled: fire escape ("get out, stay out") and "stop, drop and roll" kept as one scene on day 64, 0 days.

### Unit 14: Feelings, limits and fair settling (days 69 to 74, grade 2 weeks 13 to 18)

The heaviest grade 2 unit, with two new cards. Day 69 teaches listening before judging with the influence and listening cards back for one day; day 70 teaches calm first, talk second on SEL's calm-down card (SEL grade 2 unit 14, weeks 5 to 10, has the tools by now); day 71 models the boundary steps, with the I-statement opening the "say it" step; day 72 models the short conflict steps (PE grade 2 unit 17, weeks 9 to 12, teaches them first as team talk, so where the school runs PE they open as a retrieval and the day goes to the adult-help step and practice; with no PE they are taught as new); day 73 is the Fluency day on the boundary card, card turned over. Self-checks on days 70 and 73. Said-aloud boundary steps heard across days 73 (observe) and 74, card turned over; end-of-unit check on day 74, which asks both halves of NHES.S4.2.4 ("A friend says stop. What do you do?" as its own prompt) and NHES.S2.2.3 as how the same thing touches another character. Before unit 16, which uses the boundary steps; SEL grade 2 unit 16 (weeks 17 to 20) follows with dares and rule breaks.

Candidate settled: "accept a no from others" is already in day 71, 0 days.

### Unit 15: Moving together and my goal (days 75 to 78, grade 2 weeks 19 to 22)

Day 75 teaches the invite line, side by side with PE unit 19 (weeks 18 to 21), each naming the other. Day 76 sets every child's movement-break goal at school with the goal card back for one day; the goal runs the weeks between lessons, with the teacher's doing record for NHES.S6.2.5. Day 77 teaches looking back on a character's week and has each child look at their own chart halfway. End-of-unit check on day 78 on the child's own chart and look-back, scored on the steps and the telling. Self-checks on days 76 and 77. It closes the goal thread begun in kindergarten unit 2.

Candidate settled: active things a character does at home kept as one line on day 75, 0 days, never asking about a child's home.

### Unit 16: Who to tell (sensitive, removable; days 79 to 80, grade 2 weeks 23 to 24)

Day 79 uses unit 13's helper map for who to tell at home, school and nearby; day 80 rehearses from a script, then the check. Owns no id; practices NHES.S4.2.4 and NHES.S3.2.3. If unit 10 was left out, day 79 opens with its one idea. Family note on day 77.

Candidate settled: trusted adults outside school kept as one scene on day 79, 0 days.

### Unit 17: Growing bodies, respectful friends (sensitive, removable; days 81 to 82, grade 2 weeks 25 to 26)

Day 81 teaches that bodies grow and change in many ways, and privacy and respect for limits, with no reproduction detail and no pictures of bodies; day 82 is the check. Owns no id; practices NHES.S4.2.4 and NHES.S1.2.2. If unit 11 was left out, day 81 opens with one scene on respect for every family. Family note on day 79.

Candidate settled: "all living things grow" kept as one plain line on day 81, 0 days.

## Course-level checks

| Check | Course day | Week (school day) | Respond day (week) | Codes sampled |
|---|---|---|---|---|
| Kindergarten mid-year | 12 | K week 12 (58) | 13 (week 13) | S7.2.1, S1.2.4, S1.2.2, S2.2.1, S6.2.1 |
| Kindergarten year-end | 27 | K week 27 (133) | 28 (week 28) | S4.2.1, S4.2.2, S4.2.5, S3.2.1, S5.2.1; carried items S7.2.1, S2.2.1 |
| Grade 1 mid-year | 39 | grade 1 week 11 (193) | 40 (week 12) | S1.2.3, S1.2.1, S4.2.3, S3.2.2, S8.2.1, S5.2.2; S7.2.2 from unit 6's record |
| Grade 1 year-end | 55 | grade 1 week 27 (273) | 56 (week 28) | S2.2.2, S1.2.6, S5.2.3, S6.2.2, S6.2.3, S6.2.4, S8.2.2; carried items S1.2.3, S3.2.2 |
| Grade 2 mid-year | 67 | grade 2 week 11 (333) | 68 (week 12) | S5.2.4, S1.2.5, S1.2.7, S3.2.3 |
| Grade 2 year-end | 83 | grade 2 week 27 (413) | 84 (week 28) | S2.2.3, S4.2.4, S8.2.3, S6.2.6; S6.2.5 from unit 15's record; carried items S5.2.4, S3.2.3 |

Every one of the 33 owned codes is sampled on a course-level check day; S7.2.2 and S6.2.5, the two doing indicators, are sampled through the teacher's doing record carried in, not by a new item. The three mid-year checks each come one week after a unit's end-of-unit check, so their items for that unit's skills are built from the earlier unit's content in a different form (kindergarten: unit 1's habits in a pick-one form; grade 1: unit 6's sick-classmate and shared-cup scenes; grade 2: unit 12's very-hot scene for the helper item), and that unit's end record is carried, not re-scored. The year-end checks come after a sensitive unit they never sample. Collect once: unit 7's said-aloud record (days 37 and 38) is carried into the grade 1 mid-year check a week later, and units 3 and 14's records are carried into their year-end checks. No check repeats a task form given in the two weeks before it. Each part of each code has its own prompt (expert read 2026-11-26): kindergarten year-end, the listening step in two pictured places and one kind thing shown or said; grade 1 mid-year, a "hurt" prompt (helmet or sun) beside the germ item for NHES.S1.2.3 and a strength card that is the child's own for NHES.S1.2.1; grade 1 year-end, "How could this touch you if it happened?" beside the character item for NHES.S2.2.2 and the "hurt" prompt on the carried NHES.S1.2.3 item; grade 2 year-end, "A friend says stop. What do you do?" for the honor-others half of NHES.S4.2.4 and how the same thing touches another character for NHES.S2.2.3.

Weeks: all six checks fall on the frame's weeks and the table in docs/courses/CALENDAR.md (12 and 27; 11 and 27; 11 and 27), off every core check week of their grade, and off SEL's (K 11 and 26, grade 1 9 and 26, grade 2 10 and 26). Kindergarten week 12 and week 27 share a week with computer science and library, and grade 2 week 27 with ELD and PE; those are specials, which do not count in the K to 5 stagger rule since the lead calendar pass (CALENDAR.md rule 1), and `frame.py calendar` reports no break.

## Leans on the calendar

| Lean | Other course's days (calendar.csv) | Here | Treatment |
|---|---|---|---|
| k-pa-move-every-day and PE k-fitness-activities | PE unit 6, K weeks 24 to 27 | day 8, week 8 | PE later: day 8 states the heart fact itself (the frame's "if later" bridge), inside the unit's days |
| g1-pa-play-safe and PE g1-heart-muscle | PE unit 12, grade 1 weeks 19 to 22 | day 46, week 18 | Side by side, health a week ahead; heart fact in one line |
| g2-fn-pick-best-snack and PE g2-foods-energy | PE unit 18, grade 2 weeks 13 to 16 | day 60, week 4 | Health first; names energy foods once |
| g2-s-outdoor-and-home-safety and PE g2-water-skills | PE unit 22, grade 2 weeks 28 to 32 | day 64, week 8 | Health first; gives the reason behind water rules |
| g2-pa-invite-friends-to-move and PE g2-rules-fair | PE unit 19, grade 2 weeks 18 to 21 | day 75, week 19 | Side by side; neither teaches the other's part |
| SEL k-sa-name-feelings, k-sm-calm-down | SEL unit 2, K weeks 5 to 10 | days 14 and 15, weeks 14 and 15 | SEL first: retrieval of SEL's faces and card; taught in the first ten minutes where SEL is not run |
| SEL k-rel-say-no on k-s-trusted-helpers | SEL units 1 and 5, K weeks 1 to 4 and 20 to 25 | day 19, week 19 | SEL named school helpers; health adds home and nearby helpers and the two signs |
| SEL g1-rel-say-no, g1-rel-ask-offer-help | SEL unit 9, grade 1 weeks 10 to 15 | days 33 to 36, weeks 5 to 8 | Health first |
| SEL g1-sm-set-goal | SEL unit 12, grade 1 weeks 27 to 32 | day 48, week 20 | Health first |
| SEL g2-rel-say-no | SEL unit 16, grade 2 weeks 17 to 20 | day 71, week 15 | Health first |
| SEL calm-down card, grade 2 form | SEL unit 14, grade 2 weeks 5 to 10 | day 70, week 14 | SEL first: the card is used, not taught again |
| SEL k-rel-talk-listen (talk turn card) | SEL unit 1, K weeks 1 to 4 | day 16, week 16 | SEL first: "eyes look, wait my turn" opens the listening card |
| SEL k-sm-set-goal (goal steps card) | SEL unit 6, K weeks 27 to 32 | day 10, week 10 | Health first: "my goal and one step"; SEL opens with the pick as retrieval |
| SEL g1-rds-solve-problems (the I-statement) | SEL unit 9, grade 1 weeks 10 to 15 | day 34, week 6 (taught K day 14) | Health first, a year ahead; SEL uses the same words |
| SEL g2-sm-set-goal (a changed step) | SEL unit 17, grade 2 weeks 21 to 26 | day 76, week 20 | Health first; the same goal card's grade 2 rung |
| PE g2-talk-problems (team talk) and g2-v-settle-it-with-words | PE unit 17, grade 2 weeks 9 to 12 | day 72, week 16 | PE first: where the school runs PE, health opens the conflict steps as retrieval; taught as new where there is no PE |

No row leans on a core course (science, mathematics, ELA).

## Coverage map (bar criterion 10)

HECAT 2021 healthy behavior outcomes (`HECAT.<topic>.HBO<n>`, data/standards/hecat-topics.txt) by year, with units. "(s)" marks a sensitive unit. Every number in STANDARD.md section 4's K to 2 column is placed.

| Topic | Kindergarten | Grade 1 | Grade 2 | Band |
|---|---|---|---|---|
| Personal health and wellness (PHW) | unit 1 (1, 2, 5); unit 2 (1, 5) | unit 6 (1 to 5); unit 8 (1, 5); unit 9 (1, 2) | unit 12 (1, 2, 5, 11); unit 15 (1, 2) | 1 to 5, 11 |
| Food and nutrition (FN) | unit 2 (1, 2, 3, 6, 7) | unit 8 (1, 2, 3, 6, 7) | unit 12 (1, 3) | 1, 2, 3, 6, 7 |
| Mental and emotional health (MEH) | unit 3 (1, 2, 4, 5, 7) | unit 7 (4) | unit 14 (1, 3, 4, 5, 7) | 1 to 5, 7 |
| Physical activity (PA), with PE | unit 2 (1, 4) | unit 9 (1, 4, 6) | unit 15 (1) | 1, 4, 6 |
| Safety (S) | unit 4 (1, 3, 4, 5, 7) | unit 7 (4 to 7); unit 9 (8) | unit 13 (1, 3 to 7) | 1, 3 to 8 |
| Violence prevention (V) | unit 3 (1, 3); unit 5 (8, s) | unit 7 (7); unit 9 (1, 3, 7); unit 10 (8, s) | unit 14 (1, 3, 7); unit 16 (8, s) | 1, 3, 7; 8 (s) |
| Tobacco (T) | unit 4 (1, 2) | (the found-vape scene, unit 7, practice) | unit 13 (1, 2) | 1, 2 |
| Alcohol and other drugs (AOD) | unit 4 (1, medicine safety) | unit 7 (1) | (medicines stay with adults, unit 13, practice) | 1 |
| Sexual health (SH) | (body names in unit 1, non-sensitive) | unit 11 (2, 3, s) | unit 17 (1, 2, s) | 1, 2, 3 (s) |

Each topic is claimed at least in alternate years (STANDARD.md section 4).

NHES standards by unit (O owns an indicator, p practices one owned elsewhere):

| Standard | K units | Grade 1 units | Grade 2 units |
|---|---|---|---|
| 1 Use health information | 1 O; 2 p; 4 p | 6 O; 7 p; 8 O | 12 O; 13 p; 17 p (s) |
| 2 Analyze influences | 2 O | 8 O; 11 p (s) | 14 O |
| 3 Find help and resources | 4 O; 5 p (s) | 7 O; 10 p (s) | 13 O; 16 p (s) |
| 4 Communicate | 3 O; 4 p | 7 O; 9 p; 10 p (s); 11 p (s) | 13 p; 14 O; 16 p (s); 17 p (s) |
| 5 Decide | 4 O | 7 O; 8 O | 12 O |
| 6 Set goals | 2 O | 9 O | 15 O |
| 7 Practice healthy behaviors | 1 O; 2 p | 6 O; 9 p | 12 p |
| 8 Advocate | 4 p (the scripted ask) | 7 O; 9 O | 15 O |

Every year touches all eight standards with the sensitive units taken out. Every skill standard (2 to 8) is practiced in at least two topics in the band with sensitive rows out, as the frame counts it.

## The old topic stubs (STANDARD.md section 9)

| Stub in data/modules.csv | Decision | Why |
|---|---|---|
| health-pe-k-2-healthy-habits | Kept, as units 1, 6 and 12 | Hand washing, sleep and germ habits are the band's personal health thread |
| health-pe-k-2-food-groups | Renamed: food, water and snack choices, units 2, 8 and 12 | Food groups by name and labels wait for grade 3 (g3-fn-food-groups); K to 2 names foods that help us grow, never good or bad |
| health-pe-k-2-feelings-and-friends | Kept, as unit 3, with units 7 and 14 | Same scope; asking for help lives in unit 7 |
| health-pe-k-2-safety | Kept, as units 4, 7 and 13 | Fire and water in unit 13, traffic gear in unit 4, stranger scenes kept calm in unit 7 |
| health-pe-k-2-health-goals-at-home | Renamed: goals at school, units 2, 9 and 15 | No task asks about a child's home; goals come from the safe list and run at school |

## Sources a day leans on that are not loaded

- HECAT 2021 topic modules (PHW, FN, PA, MEH, S, V, T, AOD; SH read only in part): every unit's planner reads its module's PreK-2 expectations before planning. Every Candidate kept above is conditional on that read; where the read does not list it, the slot returns to practice.
- CDC "Clean Hands" pages (day 2), CDC vaccine and germ pages (day 58), CDC adult tobacco use pages for the norm (days 23 and 65; the expert read of 2026-11-26 opened https://www.cdc.gov/tobacco/php/data-statistics/adult-data-cigarettes/index.html, 19.8% of US adults used any tobacco product in 2022, so "most grown-ups do not smoke or vape" holds; the unit plan dates it to that figure), vaccine fact checked on CDC's vaccines for children page (the unit plan's read adds a national pediatrics association page), the national highway traffic safety agency's car seat and booster pages (day 22), the federal Poison Help pages (day 23), USDA's food guide pages (units 2, 8, 12): named from memory, opened at the expert and safety reads. The car seat and Poison Help pages returned 403 to the frame reader's fetcher: browser check (standing rule 2026-11-22).
- The sensitivity sources for units 1, 5, 10, 11, 16 and 17 named in the frame (the body-names sensitivity review, the federal Child Welfare Information Gateway prevention pages, CDC's child abuse prevention pages, a national child traumatic stress network's guidance): read at each unit's sensitivity read.

## Shorter path

No path cuts an assessed day, an owned row or an owned code; each moves work into a neighbor.

**A year about 10 days short.** Ten school days is two weeks, two lessons at one a week. Each year names two fold-in days, each saving its 30-minute lesson:

| Year | Fold-in day | Where its work goes |
|---|---|---|
| Kindergarten | 7 (water first) | One sentence and a filled water cup inside day 6; the water card joins day 9's sort |
| Kindergarten | 20 (Fluency, the ask) | Its rehearsal becomes the five-minute pair rehearsal of days 21 and 23 |
| Grade 1 | 31 (eyes, ears, sun) | The protection match and the outside-names retrieval move into day 29; the class norm is said at day 30's close from the washing tally the routine record has kept since day 29 ("most of our class washed before snack this week"), so it stays on an Understanding day; the cough-and-wash card keeps its pair practice on day 30, turned over at its end |
| Grade 1 | 43 (Application, plate and ad) | The invented ad becomes day 44's opening scenario; the plate and water cup join day 42's practice; the card is withdrawn on day 44 |
| Grade 2 | 58 (germs deeper) | Vaccines join day 59 (given at checkups); where germs hide becomes day 57's opening; the cough-and-wash retrieval moves with it |
| Grade 2 | 73 (Fluency, boundary card, practice only) | Its rehearsal becomes the five-minute pair rehearsal of days 72 and 74; the ten-child hearing moves to day 72's last ten minutes, card turned over (day 72 then carries `assess` observe in that school's plan). Day 64 is not folded: with day 63 it would put the emergency rule, every child's phone practice, four rule areas and two retrievals in one lesson |

That is 60 minutes a year, 180 minutes over the band: 84 course days become 78 (26 a year). No fold-in day holds an end or course-level check (day 73's observe hearing moves whole to day 72), and the check days keep their weeks. A school that loses more can fold the second-to-last teaching day of unit 2, 8 or 12 into its neighbors on the same pattern.

**Twice a week for half the year.** The frame allows it with the same order and checks. Two lessons a week over 14 weeks puts course day n of a year in week (start - 1) + ceil(n / 2). To keep every check off its grade's core and SEL check weeks, use these halves: kindergarten weeks 15 to 28 (mid-year check week 20, year-end week 28), grade 1 weeks 15 to 28 (weeks 20 and 28), grade 2 weeks 17 to 30 (weeks 22 and 30; weeks 20 and 28 hold grade 2 science checks). Family notes still go home two weeks before each sensitive unit (four lessons ahead). The body-names family note goes home two weeks before day 3: kindergarten week 14, before the course starts, with the day 1 home task. The unit 15 goal runs a full week between lessons this way: days 77 and 78 are each moved one week later, and the week's other lesson is a respond-style re-rehearsal, so the goal runs a week before the look-back and a week before the check. The grade 2 checks keep weeks 22 and 30 (day 83 does not move).

**A leave-out unit.** Each sensitive unit's two days extend the unit the frame names, as two days before that unit's check (an Application day on new scenarios with the card withdrawn and a Fluency rehearsal), so its end-of-unit check moves to its new last day; checks keep their weeks.
- Unit 5 out: unit 4 runs weeks 19 to 26 (check week 26). The kindergarten year-end check then comes right after unit 4's end, so its unit 4 items use unit 3's scenes in a pointing form.
- Unit 10 out: unit 9 runs weeks 18 to 24 (the frame names unit 9 in unit 10's row). Unit 16's day 79 opens with the keep-telling bridge.
- Unit 11 out: unit 8 runs weeks 13 to 19, unit 9 moves to weeks 20 to 24 and unit 10 to 25 to 26 (its family note on week 23). Unit 9 then runs a week behind PE unit 12, so day 46 retrieves PE's heart lesson rather than leading it. Unit 17's day 81 opens with the respect-for-every-family bridge.
- Unit 16 out: unit 14 runs weeks 13 to 20, unit 15 moves to weeks 21 to 24 (PE unit 19 then comes first, and day 75 names its fair rules), unit 17 stays at weeks 25 to 26.
- Both units 10 and 11 out: unit 8 runs weeks 13 to 19 and unit 9 weeks 20 to 26 (two days each). The grade 1 year-end check then comes right after unit 9's end, so its unit 9 items are drawn from unit 8's scenes in a different form, and unit 9's end record is carried. Day 46 retrieves PE unit 12's heart lesson rather than leading it. The unit 10 and unit 11 family notes are dropped.
- Unit 17 out: unit 14 gains its two days the same way and runs weeks 13 to 20 (its check in week 20); unit 15 moves to weeks 21 to 24 (PE unit 19 then comes first, and day 75 names its fair rules) and unit 16 to weeks 25 to 26, with its family note in week 23, on unit 15's third day. With unit 16 also out, unit 14 runs weeks 13 to 22 and unit 15 weeks 23 to 26.
- A family note that falls on a left-out unit's day (unit 11's on day 51, unit 17's on day 79) still goes home that week.
- The sensitive units make no card a later unit needs (help steps come from units 4, 7 and 13; the boundary steps from unit 14), so the leave-out bridge rule applies only to the one-idea openings named above.

**A shorter period.** A 20-minute slot keeps each day's order, its opening scenario (three minutes) and the five minutes of washing on hand-washing days. The pair rehearsal moves into the classroom routine the same week (health is the classroom teacher's course), and each check day splits: the pictured scenes in the slot, the said-aloud hearing and any scribing in the classroom routine that week.

## For the lead

1. **The band's school-day span.** `school_day` follows scripts/frame.py's span for this course (28 meeting weeks a year, so grade 1 starts at school day 141 and grade 2 at 281). If the lead changes the band span to the 32-week year (160), add 20 to every grade 1 school_day and 40 to every grade 2 one; the weeks do not change.
2. **Unit 11's leave-out target.** Extending unit 8 shifts units 9 and 10 two weeks and puts unit 9 behind PE unit 12. Pick: unit 11's days extend unit 9 instead (adjacent to the sensitive block, no unit moves), or keep unit 8 with the shift written above.
3. **SEL grade 1 unit 11 and health unit 11** meet families in the same weeks (SEL weeks 21 to 26, health weeks 25 to 26). Confirm SEL keeps to groups and friendships (no family-structure content) so health's opt-out holds, and each names the other.
4. **Browser check** (from the frame): the national highway traffic safety agency car seat page and the federal Poison Help page.
5. **Body names (L89):** day 3 and its family note are marked for the person's read before publishing.

The frame wording items this file used to list (the step card's first day, unit 7's I-statement, the said-aloud hearing time) were fixed in frame.md in the 2026-11-26 fix pass.

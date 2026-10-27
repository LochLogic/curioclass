# Fitness Program Designer

## One idea
Build a 6-week training plan for a client on a coach's week-by-week grid while a live check panel and a weekly load chart (minutes times effort) catch the classic mistakes as you make them: too much too soon, the same muscles two days running, a missing fitness component, and no progression.

## Not like
- meal-and-move-planner (9-12 health, builder; may become "Game Day Fuel"): plans meals around training days and energy balance. Fitness Program Designer owns FITT programming and has no food in it.
- goal-tracker (6-8 PE, creature): one SMART goal, a log and a creature. This tool designs the training itself, session by session, and checks it against guidelines.
- first-aid-responder (9-12 health, race): emergency steps against the clock. Nothing timed here; it is an untimed design bench.
- captain-s-choices (9-12 PE, story): team culture choices. This tool is solo planning with numbers.

## Who and how
- Grade 9-12, Physical Education, module Lifetime Fitness (design and evaluate a personal fitness program).
- Driver: students on laptops (alone or in pairs).
- Minutes: 20-40 (one period for a full plan; Fix it alone fits 15).
- Standards: SHAPE.S2 (applies fitness concepts: FITT, overload, progression, specificity, recovery), SHAPE.S4 (personal skills: plans for lifelong activity).
- Topic line: "FITT, overload and progression".
- Modes (tool.json): ["Design", "Fix it"].

## Screens and modes
Header (theme-912): title "Fitness Program Designer" with small line "FITT, overload and progression", mode buttons **Design**, **Fix it** (keys 1, 2), **Motion**, **Sound**, **Read**.

### Design (opens first)
- Top of stage: **Client** selector (four persona cards, Content), showing name, age, goal and current week.
- Stage, main: the program grid, 6 rows (Week 1 to 6) by 7 columns (Mon to Sun). Each cell shows up to two session chips: a type letter and icon (**C** Cardio, **S** Strength, **F** Flexibility, **K** Sport or skill), minutes, and RPE; an empty cell reads "Rest". Cell background tint deepens with that day's load (and the load number is printed, so tint is never the only signal).
- Stage, below the grid: the weekly load chart (Content), one bar per week split by type, with the week's load number and its change from the week before ("+8%").
- Panel, top: the session editor for the selected cell: **Type** (five buttons including **Rest**), **Minutes** slider 5 to 120 in 5s, **Effort (RPE)** slider 0 to 10 with its word label, and for Cardio and Sport the client's estimated heart rate range for that effort band. For Strength: **Muscle groups** toggles **Legs**, **Push**, **Pull**, **Core**; **Sets** 1 to 4; **Reps** 6 to 15. Buttons **Add second session**, **Delete session**.
- Panel, middle: grid tools: **Copy week to next**, **Copy week to next +10%** (minutes times 1.1, rounded to the nearest 5), **Clear week**, **Clear plan**.
- Panel, bottom: the **Checks** list (Content), each line with a glyph and words: ✓ pass, ! caution, ✗ fail. Tap a line to highlight the cells or weeks it is about.
- **Save** to one of three slots on this device, **Load**, **Clear saved** (confirm).

### Fix it
- Three broken plans (Content). Pick one: it loads into the same grid with its client. The Checks list shows what is wrong; the panel shows "Fixed: 2 of 5 problems". Fix it is done when every ✗ is gone and at most one ! remains; then a small "Coach approved" stamp appears (no confetti). **Reset this plan** reloads it.

## Content

### Clients (fictional)
| Client | Age | Goal type | Goal | Current week (load) |
|---|---|---|---|---|
| Maya | 15 | 5K | Run a 5K without stopping in 6 weeks | walks 20 min on 3 days, RPE 3 (180) |
| Dev | 16 | Strength | Get stronger for wrestling preseason | lifts 30 min on 2 days, RPE 6, legs, push, pull; jogs 20 min on 1 day, RPE 6 (480) |
| Sam | 17 | Flexibility | More flexible, stronger core for dance | dances 60 min on 3 days, RPE 5 (900) |
| Riley | 14 | General | More energy, try new activities | plays basketball 30 min on 2 days, RPE 4 (240) |

### Effort scale (session RPE, 0 to 10) and bands
0 Rest, 1 Very, very easy, 2 Easy, 3 Moderate, 4 Somewhat hard, 5 Hard, 6 (between), 7 Very hard, 8 (between), 9 (between), 10 Maximal (labels from the session-RPE scale). Bands used by the checks: light 1 to 4; moderate 5 to 6; vigorous 7 to 8; near max 9 to 10 (relative intensity bands from the Physical Activity Guidelines).
Heart rate (estimated max = 220 minus age; moderate 64 to 76 percent, vigorous 77 to 93 percent):
| Age | Est. max | Moderate | Vigorous |
|---|---|---|---|
| 14 | 206 | 132 to 157 | 159 to 192 |
| 15 | 205 | 131 to 156 | 158 to 191 |
| 16 | 204 | 131 to 155 | 157 to 190 |
| 17 | 203 | 130 to 154 | 156 to 189 |
A note under the range: "An estimate. Real maximum heart rates vary a lot from person to person; effort (RPE) is the main guide here."

### Load
Session load = minutes times RPE (session RPE method). Week load = sum of its sessions. Change = (this week minus last week) divided by last week, as a whole percent. Week 1 is compared with the client's current week. When the week before has a load of 0, the change shows "new" and checks 7 and 8 do not flag it.

### Checks (recomputed on every edit; each shows which week fails)
1. **Vigorous cardio**: at least 3 days a week with a Cardio or Sport session at RPE 7 or more (teen guideline). ✗ if fewer in any week.
2. **Muscle strength**: at least 3 days a week with a Strength session (teen guideline). ✗ if fewer.
3. **All muscle groups**: Legs, Push, Pull and Core each at least once a week. ✗ if one is missing.
4. **Recovery**: no muscle group trained on two days in a row (about 48 hours of rest for a group). ✗, highlighting both days.
5. **Flexibility**: at least 2 days a week with a Flexibility session. ✗ if fewer.
6. **Days off**: at least 1 Rest day a week. ✗ if none.
7. **Start where you are**: week 1 load against the current week. ! over +10 percent; ✗ over +50 percent.
8. **Gradual progression**: each week against the one before. ! over +10 percent; ✗ over +50 percent. The ! text: "Big jump. Many coaches keep weekly increases near 10 percent; studies disagree on how strict that must be." The ✗ text: "Too much at once. This tool flags jumps over 50 percent."
9. **Overload**: week 6 load above week 1 load (for a Strength goal: also sets or reps go up at least once over the six weeks). ! if not.
10. **Fits the goal (specificity)**: 5K: at least 3 Cardio days a week, and a Cardio session of 30 minutes or more in week 6. Strength: check 2 passes and overload for sets or reps passes. Flexibility: at least 3 Flexibility days a week. General: checks 1, 2 and 5 all pass. ! if not.
A summary line above the list: "7 of 10 checks pass" (a ! counts as not passing).

### Fix it plans (same every load)
1. **Too much too soon** (Maya): every week Mon to Sat Cardio at RPE 7, Sun Rest; minutes 30, 35, 40, 45, 50, 55 in weeks 1 to 6. Loads 1260, 1470, 1680, 1890, 2100, 2310 (changes +17, +14, +13, +11, +10 percent). Problems: start ✗ (+600 percent), progression ! (weeks 2 to 5), strength ✗, muscle groups ✗, flexibility ✗.
2. **Leg day every day** (Dev): every week Mon to Fri Strength, legs only, 45 min, RPE 7, 3 sets of 10; Sat Sport (wrestling practice) 90 min, RPE 7; Sun Rest. Load 2205 every week. Problems: recovery ✗, muscle groups ✗, vigorous cardio ✗ (1 day), flexibility ✗, start ✗ (+359 percent), overload !, fits the goal ! (sets and reps never go up).
3. **Flat line** (Sam): every week Mon, Wed, Fri Sport (dance) 60 min RPE 5; Tue, Thu Flexibility 20 min RPE 3; Sat Strength, core only, 20 min RPE 5; Sun Rest. Load 1120 every week. Problems: vigorous cardio ✗, strength ✗ (1 day), muscle groups ✗, overload !, fits the goal ! (2 flexibility days), start ! (+24 percent).
The "problems" count in the panel is the number of checks not passing at load.

### Coach notes (Read panel cards, four)
1. FITT / Frequency (how often), Intensity (how hard), Time (how long), Type (what kind). Change one at a time.
2. Overload and progression / Fitness improves when the body does a bit more than it is used to, raised gradually.
3. Recovery / Muscles adapt during rest. Give a muscle group about 48 hours before training it hard again; take at least a day off a week.
4. Specificity / You get better at what you train. A 5K plan is mostly running; a flexibility plan stretches most days.

## Interactions in detail
- Click or tap a cell to select it (Enter on a focused cell); arrow keys move the selection; Delete clears it. A selected cell has a 3 px accent outline.
- Editing a slider updates the cell, the chart and the checks live (under 50 ms). The chart bars animate their height over 200 ms (instant with Motion off).
- Rest is a type: choosing it clears the cell's sessions. A cell with no session counts as a Rest day.
- Copy week to next overwrites the next week after a confirm if it has sessions. On week 6 it is disabled.
- Changing the client keeps the plan and re-runs the checks against the new client (heart rates, goal, current week).
- Tapping a check highlights its cells (outline) or weeks (bracket) until another check or cell is tapped.
- Save slots store the plan and client in localStorage `fpd-plans` (try/catch); nothing about the student is stored.
- Sizes: at 1366x768 the grid, the selected cell's editor and the top of the checks list are visible together; the chart can sit below the fold of the stage but scrolls with it. Under 900 px tall the editor collapses to Type, Minutes and RPE with "More" for strength details. At 760 wide the grid scrolls horizontally inside its box with the week labels pinned.

## Look
- `kit/theme-912.css` (dark instrument), with its own accent `--brand` #a3e05a (lime, "go" green on a training app), `--brand-ink` #13200a.
- Contrast: accent on panel #141b25 11.02:1, on sec-bg #18202b 10.44:1, brand-ink on accent 10.79:1; theme ink and muted ratios as in the theme file. Group siblings use purple, green, raspberry, amber, indigo and coral; the 9-12 health neighbors are not built yet.
- Type colors in chips and chart (each with letter and icon): Cardio #ff8a8a, Strength #5aa9ff, Flexibility #c9a0ff, Sport #5fd39a (the theme's graph colors, 7.4:1 or more on the graph background).
- Numbers in the readout font; ✓ uses the theme's --ok, ! and ✗ use --warn, always with the glyph and words.

## Art
none: drawn in code (grid, chips, chart, persona cards with initials, no portraits).

## Voice
`calm-professor` (Schedar): "Say evenly and clearly, like a calm, friendly college professor." Minimal narration; most text is read on screen.

| Key | Kind | Line | Stale when |
|---|---|---|---|
| wDesign | how | Pick a client, then click a day to add a session. The checks update as you go. | mode left |
| wFix | how | Pick a broken plan. Use the checks to find each problem, then fix it in the grid. | mode left |
| howCheck | how | Click a check to see which days it is about. | a check clicked |
| allPass | event | All ten checks pass. | any edit |
| fixed | event | Coach approved. | any edit |
Check texts and coach notes are read on screen; Read speaks the selected check, or the hint.

## Family engine
none

## Sources
- SHAPE America, National Physical Education Standards (2024), Standards 2 and 4: https://www.shapeamerica.org/standards/pe/
- Teen guidelines (60 minutes daily; vigorous, muscle- and bone-strengthening at least 3 days a week) and relative intensity bands (moderate 5 to 6, vigorous 7 to 8 on a 0 to 10 scale): U.S. HHS, Physical Activity Guidelines for Americans, 2nd ed. (2018), chapters 2 and 3: https://health.gov/our-work/nutrition-physical-activity/physical-activity-guidelines
- Estimated max heart rate 220 minus age; moderate 64 to 76 percent, vigorous 77 to 93 percent: CDC, "Target Heart Rate and Estimated Maximum Heart Rate": https://www.cdc.gov/physical-activity-basics/measuring/heart-rate.html
- Session RPE load (minutes times RPE) and the 0 to 10 labels: Foster et al., "A new approach to monitoring exercise training," J Strength Cond Res 15(1), 2001.
- Gradual progression, all major muscle groups, about 48 hours between sessions for a muscle group, flexibility at least 2 to 3 days a week: Garber et al., ACSM Position Stand, Med Sci Sports Exerc 43(7), 2011; ACSM's Guidelines for Exercise Testing and Prescription, 11th ed. (2021).
- Youth resistance training, 1 to 3 sets of 6 to 15 reps, progression: Faigenbaum et al., NSCA position statement, J Strength Cond Res 23(5 Suppl), 2009.
- Progressive overload in resistance training: ACSM Position Stand, "Progression models in resistance training for healthy adults," Med Sci Sports Exerc 41(3), 2009.
- At least one day off a week for young athletes: Brenner, AAP Council on Sports Medicine and Fitness, "Overuse injuries, overtraining, and burnout in child and adolescent athletes," Pediatrics 119(6), 2007.
- 10 percent rule is a rule of thumb with mixed evidence: Buist et al., "No effect of a graded training program on the number of running-related injuries in novice runners," Am J Sports Med 36(1), 2008.
- The 50 percent "too much at once" line is this tool's own threshold, labelled as such on screen.

## Done when
1. Design opens with Maya and an empty grid; the empty plan shows vigorous cardio, muscle strength, all muscle groups and flexibility ✗, days off ✓, and no divide-by-zero anywhere.
2. Adding sessions updates cell, chart and checks live; the load and percent change on each bar match a hand recomputation (minutes times RPE).
3. Recovery flags legs on Mon and Tue and highlights both cells; moving one to Wed clears it.
4. Copy week to next +10% raises the next week's load by about 10 percent (rounding to 5 minutes may shift it by a few percent; the check uses the true load).
5. Each Fix it plan loads with exactly the problems listed; fixing them yields "Coach approved".
6. Heart rate ranges match the table for each client's age.
7. Save, reload, Load restores a plan; Clear saved empties the slots; nothing else is stored.
8. At 1366x768 grid, editor and the checks summary are visible together; at 760 wide the grid scrolls inside its box; keyboard alone can build a full week.
9. allPass and fixed lines speak each time they happen; how-to lines once per load.

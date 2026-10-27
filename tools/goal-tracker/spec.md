# Goal Tracker

## One idea
Fern, a little plant creature, grows from how often you showed up over the last two weeks, not from a streak, so a missed day costs nothing; right beside it a streak counter drops to zero on every miss, and the gap between the two is the lesson.

## Not like
- habit-hero (K-2 health, creature, same family): Pip's meters drop after a less healthy choice in one day. Fern never shrinks or loses a leaf; it reads weeks of activity against a goal you wrote.
- comeback-club (3-5 SEL, creature): Bix levels up from comebacks after puzzle mistakes. Fern grows from logged physical activity, and the goal itself (how big, how often) is what you tune.
- screen-time-detective (6-8 health, data): a week of pretend screen time analyzed for patterns. Goal Tracker is about writing a realistic activity goal and seeing consistency over a month.
- fitness-program-designer (9-12 PE, builder): a 6-week FITT training plan with load checks. Goal Tracker is one SMART goal and a log, no program design.

## Who and how
- Grade 6-8, Physical Education, module Personal Fitness Plans (set goals and track activity).
- Driver: students on laptops (one each, or pairs).
- Minutes: 15-25.
- Standards: SHAPE.S2 (applies fitness concepts: activity guidelines, intensity), SHAPE.S4 (personal skills: goal setting, self-monitoring).
- Topic line: "setting fitness goals and tracking activity".
- Modes (tool.json): ["Jordan's month", "My goal", "Why it works"].

## Screens and modes
Header: title "Goal Tracker" with small line "Setting fitness goals and tracking activity", mode buttons **Jordan's month**, **My goal**, **Why it works** (keys 1 to 3), **Motion**, **Sound**, **Read**. Stage left, panel right (below under 760 px wide).

### Jordan's month (opens first)
- Stage, top: Fern standing in a clay pot on a windowsill, large. Around the pot, four small variety badges for this week's types: **❤ Cardio**, **💪 Strength**, **🧘 Flexibility**, **⚽ Sport and play** (lit or outline).
- Stage, bottom: a 4-week calendar (Mon to Sun rows), each day a tile with minutes and a type icon; days that met the goal get a check, a day with nothing is blank (never red). A day scrubber (1 to 28) with **▶ Play month** (one day per 0.4 s) moves "today"; Fern and the meters show that day.
- Panel: the goal sentence (editable, see Goal builder), the meters (Family engine) and the **Streak vs Fern** card: "A streak app says: 0 days" beside "Fern says: 7 of 8 goal days in the last two weeks."
- Changing Jordan's goal recomputes everything on the same data: a goal that is too big makes Fern rest; a realistic one makes Fern stand tall. That is the main thing to explore.

### My goal
- Step 1, **Write your goal** (Goal builder, below). Starts at 30 minutes, 3 days a week, 4 weeks, any type.
- Step 2, **Log your last 7 days**: a 7-day strip ending yesterday; tap a day, then tap chips: minutes **0**, **10**, **15**, **20**, **30**, **45**, **60**, **90**, a type, and an effort chip (talk test: **Easy**, **Moderate: can talk, not sing**, **Vigorous: only a few words**). Fern and the meters respond.
- Step 3, **Check your goal**: the tool compares the goal with the week just logged (Interactions) and suggests a step up or a step down, with **Use this goal**.
- A banner on this mode: "This log is not saved. It clears when you close the page." **🧽 Clear log**.

### Why it works
- Six fact cards that flip (Content), and a small side-by-side animation: the same 28 days of Jordan's data drawn as a streak counter (jumping up, falling to 0) and as Fern's 14-day window (a smooth line).

## Content

### Goal builder (SMART, shown as one sentence with tappable blanks)
"I will do [any activity / cardio / strength / flexibility / sport and play] for at least [10 / 15 / 20 / 30 / 45 / 60] minutes on [2 / 3 / 4 / 5 / 6 / 7] days a week for [2 / 4 / 6] weeks, so I can [have more energy / get better at a sport / feel less stressed / keep up with friends / feel stronger]."
Under it, the five SMART letters light as each part is filled: Specific (type), Measurable (minutes and days), Achievable (the check below), Relevant (the reason), Time-bound (weeks).

### Measures (all computed for "today")
- Goal day hit: a day with logged minutes of the goal's type (any type for "any activity") at or above the goal's minutes. At most "days a week" hits count per calendar week.
- Consistency: goal days hit in the last 14 days (today included) divided by goal days planned in that window (days a week times 2), shown as "7 of 8" and a meter.
- This week: goal days hit this calendar week out of days a week.
- Variety: how many of the four types appear this week (0 to 4).
- Leaves: one leaf for every logged day with 10 or more minutes, ever. Leaves are never removed.
- Good week: a finished week with goal days hit at least 70 percent of days a week (rounded up). Each good week adds one flower.
- Streak (for the comparison card only): goal days hit in a row ending today; any day without a hit resets it to 0.

### Fern's stages (by leaves, never goes down)
| Leaves | Stage | Look |
|---|---|---|
| 0 to 2 | Seed | a seed with two tiny leaves |
| 3 to 7 | Sprout | small stem, round eyes, two leaf arms |
| 8 to 14 | Sapling | taller, four leaves, stands on root feet |
| 15 to 24 | Young fern | full fronds |
| 25 or more | Big fern | tall, fronds arching, flowers show |
Pose by consistency: 70 percent or more: standing tall, bright, a little sway. 40 to 69: normal. Under 40: resting (sitting on the pot rim, fronds folded, a small "Ready when you are" bubble). Fern never wilts, browns or cries.

### Jordan's month (fictional grade 7 student; minutes, type)
| Week | Mon | Tue | Wed | Thu | Fri | Sat | Sun |
|---|---|---|---|---|---|---|---|
| 1 | 30 soccer practice | 20 bike | 45 soccer practice | 0 | 25 walk the dog | 60 soccer game | 0 |
| 2 | 30 soccer practice | 15 push-ups and squats | 45 soccer practice | 20 stretching | 0 | 0 (rain) | 40 bike |
| 3 | 0 (sick) | 0 (sick) | 0 (sick) | 10 walk | 30 soccer practice | 60 soccer game | 20 walk |
| 4 | 35 soccer practice | 20 push-ups and squats | 45 soccer practice | 25 bike | 15 stretching | 50 soccer game | 0 |
Types: soccer is sport and play; bike and walk are cardio; push-ups and squats are strength; stretching is flexibility. Weekly totals 180, 150, 120, 190 minutes; 20 days with 10 or more minutes; day 28 is a 0, so every streak ends at 0.
Worked checks for day 28 (verify agent recomputes): 30 min, 4 days: weeks hit 3, 3, 2, 3; consistency 5 of 8 (62 percent); 3 good weeks. 20 min, 4 days: 4, 4, 3, 4; 7 of 8 (88 percent); 4 good weeks. 45 min, 5 days: 2, 1, 1, 2; 3 of 10 (30 percent, Fern rests); 0 good weeks. 60 min, 7 days: 1, 0, 1, 0; 1 of 14 (7 percent).
Default goal on open: 30 minutes, 4 days a week, 4 weeks, any activity, "get better at a sport".

### Achievable check (My goal step 3, and a line under the sentence in Jordan's month)
Compare the goal (minutes times days) with the logged week's minutes of the goal's type on days of 10 or more (for Jordan with any activity, week 1: 180). First match:
- No logged minutes of that type: "This type is new for you. Start small: 2 days a week." Suggest the same minutes on 2 days.
- Goal more than 1.5 times the logged week: "That's a big jump from what you do now. Try a step up, not a leap." Suggest: same days, minutes one step lower, or one fewer day, until within 1.5 times.
- Goal at or under the logged week: "You already do this. Try one more day or 10 more minutes."
- Otherwise: "This is a stretch you can reach."
Always also: "Guideline: kids and teens need 60 minutes of moving every day. Any goal that moves you toward that counts."

### Fact cards (Why it works; front / back)
1. 60 a day / Kids and teens 6 to 17 need at least 60 minutes of moderate to vigorous activity every day.
2. Three kinds / On at least 3 days a week, include vigorous activity, muscle-strengthening and bone-strengthening.
3. Every bit counts / Short bouts add up; there is no minimum length for activity to count.
4. SMART goals / Specific, Measurable, Achievable, Relevant, Time-bound goals make it clear when you've reached them.
5. Habits take time / In one study, new daily habits took a median of 66 days to feel automatic, with a wide range, and missing one day did not reset progress.
6. Talk test / Talk but not sing: moderate. Only a few words: vigorous.

## Interactions in detail
- Any change (goal blank, day chip, scrubber) recomputes and redraws in under 100 ms. A new leaf grows in with a small pop (no pop with Motion off); a new flower opens on the Sunday that finishes a good week.
- The meters' bars ease to their new values over 400 ms. Consistency under 40 percent shows the bar at its value with the words "Resting", never a red or empty warning.
- Changing the goal type to strength in Jordan's month: only Tue of weeks 2 and 4 have strength (15 and 20 minutes), so consistency drops; the Achievable check then uses only that type's minutes in week 1 (0), and says "This type is new for you. Start small: 2 days a week."
- Scrubbing to day 1 to 13: the 14-day window only counts days so far and planned days in the same span (days a week times days so far divided by 7, rounded up), so early days are not judged harshly.
- My goal: logging a day replaces that day's entry; a 0 clears it. Clear log asks to confirm. Nothing is written to localStorage; a reload starts fresh.
- Sound: a soft leaf rustle for a new leaf, a two-note chime for a new flower. No sound for misses.
- Sizes: at 1366x768 Fern, the meters and the calendar are visible together; under 900 px tall the calendar compresses to a 2-row-per-week strip. The day scrubber has 44 px targets.

## Look
- Accent `--brand` #3949ab (indigo), on a light theme on its own `:root`: paper #f6f7fc, ink #1e2238, muted #575d78, line #dde0ef, focus #e0662a (the accent differs from group siblings: purple, green, raspberry, amber, lime and coral; habit-hero is red #d6492f, comeback-club's look is its own).
- Contrast: accent on paper 7.23:1, white on accent 7.73:1, ink on paper 14.64:1, muted on paper 6.05:1. Leaf green #2e8b57 is used for shapes only (3.97:1, above the 3:1 non-text minimum).
- Scene: a soft morning windowsill (pale sky blue, a terracotta pot), Fern in greens with a cream face and dark round eyes; flowers in coral and yellow.

## Art
none: drawn in code (Fern in layered SVG with five stages and three poses, pot, windowsill, calendar, meters).

## Voice
`easy-coach` (Umbriel): "Say in an easy-going, encouraging way, like a relaxed sports coach." No group sibling or 6-8 neighbor uses it.

| Key | Kind | Line | Stale when |
|---|---|---|---|
| wJordan | how | This is Jordan's month. Change the goal and watch what happens to Fern. | mode left |
| wMine | how | Write your own goal, then log your last seven days. | mode left |
| wWhy | how | Tap a card to see why consistency beats a perfect streak. | mode left |
| howScrub | how | Drag the day slider, or press Play month. | scrub started |
| howLog | how | Tap a day, then tap how many minutes and what you did. | a day logged |
| leaf | event | New leaf. | another change before it plays |
| flower | event | A good week. Fern got a flower. | another change before it plays |
| rest | event | Fern is resting. A smaller goal might fit better. | consistency rises to 40 percent or more |
| tall | event | Fern is standing tall. That's consistency. | consistency falls below 70 percent |
| streak0 | event | The streak went back to zero. Fern didn't lose a thing. | scrubber moved again |
| new, big, already, stretch | event | the four Achievable lines | goal changed again |
Fact cards are read on screen.

## Family engine
**habit-hero** (siblings: habit-hero, built; goal-tracker is the first spec in the family and holds the full description). The builder extracts these parts into `kit/habit-hero.js`; habit-hero keeps its own copy until it is next touched.
- `Hero.create(svg, {stages, poses, draw})`: a character drawn in code in layers; `setStage(i)`, `setPose(name)`, `hop()` (a happy bounce) and `settle()` (a calm sit, never sad). Motion off: instant pose changes, no bounce.
- `Hero.meters(el, defs)`: labelled bars with icon and word, `role="meter"` with aria values, eased updates; each def has a floor (habit-hero 5; goal-tracker 0 with a word label instead of an empty bar).
- `Hero.fx(svg, kind)`: an effects layer (sparkles, zzz, germs for habit-hero; leaf pop, flower open, sway for goal-tracker).
- `Hero.timeline(el, {days, render})`: a strip or calendar of moments or days with a "now" marker and a scrubber (habit-hero: seven moments of one day; goal-tracker: 28 days).
Goal Tracker feeds it: Fern (five stages, three poses), meters Consistency, This week and Variety, fx leaf and flower, a 28-day calendar timeline.

## Sources
- SHAPE America, National Physical Education Standards (2024), Standards 2 and 4: https://www.shapeamerica.org/standards/pe/
- 60 minutes daily for ages 6 to 17; vigorous, muscle- and bone-strengthening on at least 3 days; any length of activity counts: U.S. HHS, Physical Activity Guidelines for Americans, 2nd ed. (2018), chapters 2 and 3: https://health.gov/our-work/nutrition-physical-activity/physical-activity-guidelines
- Talk test: CDC, "Measuring Physical Activity Intensity": https://www.cdc.gov/physical-activity-basics/measuring/index.html
- SMART goals: G. T. Doran, "There's a S.M.A.R.T. way to write management's goals and objectives," Management Review 70(11), 1981.
- Habit formation median 66 days, range 18 to 254, a missed day did not derail it: Lally, van Jaarsveld, Potts and Wardle, "How are habits formed," European Journal of Social Psychology 40(6), 2010.
- Jordan's month is invented sample data.

## Done when
1. On open, Jordan's month shows day 28 with the default goal: consistency 5 of 8, streak 0, 20 leaves (Young fern), 3 flowers.
2. Changing the goal to 20 minutes, 4 days gives 7 of 8 and Fern standing tall; 60 minutes, 7 days gives 1 of 14 and Fern resting; leaves stay at 20 in both.
3. Play month moves one day per 0.4 s; leaves only ever increase; streak drops to 0 on day 4.
4. The Achievable line for Jordan (week 1 is 180 minutes, so the limit is 270) says "big jump" for 60 minutes, 5 days (300), "stretch" for 45 minutes, 5 days (225) and "already" for 20 minutes, 3 days (60).
5. My goal: logging seven days updates Fern and the meters; reload clears everything; nothing is in localStorage.
6. No red, no shrinking, no sad face anywhere; low consistency always shows "Resting" in words.
7. Every number on screen matches a hand recomputation from the table.
8. At 1366x768 Fern, meters and calendar fit without scrolling; at 375 wide in the host the calendar scrolls inside its own box and the scrubber stays visible.
9. How-to lines are spoken once per load; leaf, flower and streak lines every time they happen.

## Open questions
- Saving a real log: the wave rules forbid keeping health data beyond the page session, so My goal is a one-sitting "last 7 days" log. A month-long personal tracker would need Save on this device (localStorage with Clear). Keep it session-only, or allow device saving for this tool?

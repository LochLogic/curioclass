# Game Day Fuel
Renamed from: Meal and Move Planner

## One idea
Plan a teen athlete's week of meals around a training schedule the coach already set, watch energy in against energy needed day by day, then play game day hour by hour on a fuel gauge to see whether your plan runs out in the second half.

## Not like
- fitness-program-designer (9-12 PE, builder): designs the training itself with FITT and load checks. Game Day Fuel never changes the training; the schedule is fixed and you plan the food. This settles overlap note M21: FITT programming stays there.
- lunch-tray-builder (K-2 health, builder, food family): one tray from five food groups. Here a whole week, energy and timing around training, for a sport.
- label-detective (3-5 health, mystery, food family): reads one label. Here the label's numbers are added up across a day and a week.
- first-aid-responder (9-12 health, race, same group): timed emergency steps. Nothing timed here except the game-day replay.
- captain-s-choices (9-12 PE, story): team culture choices. This is one athlete's food plan.
- goal-tracker (6-8 PE, creature): logs your own activity. Game Day Fuel uses only fictional athletes; nothing about the student is entered.

## Who and how
- Grade 9-12, Health, module Nutrition and Fitness Planning (energy balance and personal plans).
- Driver: students on laptops (alone or in pairs).
- Minutes: 20-40.
- Standards: NHES.S6 (goal setting for health), NHES.S7 (health-enhancing behaviors).
- Topic line: "nutrition and fitness planning".
- Modes (tool.json): ["Plan the week", "Game day"].

## Screens and modes
Header (theme-912): title "Game Day Fuel" with small line "Nutrition and fitness planning", mode buttons **Plan the week**, **Game day** (keys 1, 2), **Motion**, **Sound**, **Read**.

Athlete bar (both modes, top of stage): four athlete cards (Content), each with its painted sport gear (Art), never a portrait; the chosen one shows name, age, sport, game time, and the week's schedule strip (Mon to Sun chips: **Rest**, **Practice**, **Game**). No body weights or sizes anywhere.

### Plan the week (opens first, with Ana and her "Typical week" loaded)
- Focus: the week grid with its day bars, center stage and the biggest thing; the shelf is in the panel right beside it.
- Stage, main: the week grid: 7 columns (Mon to Sun, each headed by its day type chip) by meal-slot rows (Content, "Slots"). Each cell holds up to 4 food chips (picture, short name); an empty cell reads "Skipped".
- Under each column: a day bar: **Energy in** against **Energy needed** (the day's target), with both numbers ("1,770 of 2,400") and a percent; the bar is shaded by the flag state, always with a word ("Low", "OK", "Very high").
- Panel, top: the **Food shelf** (Content, 30 foods) in a scroll box, filterable by chips **All**, **Breakfast**, **Meals**, **Snacks**, **Drinks**, and by food group. Tap a food to add it to the selected cell; tap a chip in a cell to remove it.
- Panel, middle: **Selected day** totals as a small label in the label-detective style: calories, carbohydrate, protein, fat, fiber, added sugars, sodium, and food group amounts against targets.
- Panel, bottom: **Flags** list (Content), each with glyph and words: ✓ OK, ! check, ✗ gap or extreme. Tap a flag to outline its days or cells.
- Buttons: **Typical week** (reload the starter), **Clear week**, **Copy day to...** (pick target days), **Save**, **Load**, **Clear saved**, and **Fuel notes** (opens six cards, Content).

### Game day
- Focus: the Fuel tank line riding over the timeline, center stage and the biggest thing, with the live clock and tank percent beside it in the panel.
- Stage: a timeline of the game day from wake to bedtime, with each meal slot as a flag at its time (food chips shown on it), the game as a shaded block, and two gauges over the timeline: the **Fuel tank** (percent, a line) and **Drinks** (a check at each drink).
- Panel: **▶ Play game day** (the clock runs at 1 hour per 2 s from wake to the final whistle, where the result card shows: Ana 22 s, Priya 26 s, Marcus 12 s, Kai 7 s at 1x; becomes **⏸ Pause**), **Restart**, a speed toggle **1x / 4x**, the live clock, the tank percent, and the result card at the final whistle (Content, "Result").
- Edits: tap a meal flag to change its foods with the same shelf (it edits the game day in the week plan too). **Move meal** lets the student drag a meal flag along the timeline within its window (Content), to test timing.
- Above the tank, always: "Fuel tank is a teaching model, not a measurement of a real body."

## Content

### Athletes (fictional) and targets
Energy needed: Rest day = the Dietary Guidelines "moderately active" level for age and sex; Practice and Game days = the "active" level (this mapping is the tool's own simplification, said in Fuel notes). Food group targets per day use the "active" level.
| Athlete | Age, sex | Sport | Mon Tue Wed Thu Fri Sat Sun | Game | Wake | Rest / training kcal | Play drain |
|---|---|---|---|---|---|---|---|
| Ana | 16, F | Soccer | P P P P G R R | Fri 4:00 to 5:20 pm | 6:30 | 2,000 / 2,400 | 80 min at 0.65 per min |
| Priya | 14, F | Basketball | P G P P P R R | Tue 6:00 to 7:30 pm | 6:30 | 2,000 / 2,400 | 90 min at 0.55 |
| Marcus | 17, M | Swimming | P P P P P G R | Sat meet 9:00 am to 12:00 pm | 6:00 | 2,800 / 3,200 | 180 min at 0.28 |
| Kai | 15, M | Cross-country | P P P P P G R | Sat race 8:30 to 9:30 am (with warm-up) | 6:00 | 2,600 / 3,000 | 60 min at 0.85 |
Daily food group targets (MyPlate, Healthy US-Style pattern): 2,400 kcal: fruit 2 cups, vegetables 3 cups, grains 8 oz, protein 6.5 oz, dairy 3 cups. 3,000 and 3,200 kcal: fruit 2.5, vegetables 4, grains 10, protein 7, dairy 3.

### Slots (default times)
- Rest and Practice days: Breakfast 7:00, Lunch 12:00, Snack 3:30, Dinner 6:30, Evening snack 8:30.
- Afternoon game (Ana, Priya): Breakfast 7:00, Lunch 12:00, Pre-game (Ana 2:30, Priya 4:30; window 1 to 4 hours before), During (drinks and sports drink only), Recovery (Ana 6:00, Priya 8:00 "Recovery dinner"; window within 2 hours after), Dinner (Ana 7:30; Priya none).
- Morning game (Marcus, Kai): Pre-game breakfast (Marcus 6:30, Kai 6:15; window 1 to 4 hours before, or as early as wake), During, Recovery (Marcus 12:30 "Recovery lunch", Kai 10:00), Lunch (Kai 12:30), Snack 3:30, Dinner 6:30.

### Food shelf (per serving: kcal, carbohydrate g, protein g, fat g, fiber g, added sugars g, sodium mg; MyPlate groups)
Items marked LD reuse label-detective's record and art exactly.
| Food | Serving | kcal | Carb | Prot | Fat | Fib | Add | Na | Groups |
|---|---|---|---|---|---|---|---|---|---|
| Apple (LD) | 1 medium | 100 | 25 | 0 | 0 | 4 | 0 | 0 | fruit 1 |
| Banana (LD) | 1 medium | 110 | 27 | 1 | 0 | 3 | 0 | 0 | fruit 1 |
| Strawberries | 1 cup | 50 | 12 | 1 | 0.5 | 3 | 0 | 0 | fruit 1 |
| Plain oatmeal (LD) | 1 packet | 100 | 19 | 4 | 2 | 3 | 0 | 75 | grains 1 |
| Whole-wheat toast | 2 slices | 160 | 28 | 8 | 2 | 4 | 4 | 280 | grains 2 |
| Scrambled eggs | 2 eggs | 180 | 2 | 12 | 13 | 0 | 0 | 200 | protein 2 |
| Bagel with peanut butter | 1 bagel, 2 Tbsp | 460 | 60 | 17 | 18 | 4 | 7 | 570 | grains 3, protein 2 |
| Plain Greek yogurt (LD) | 1 cup | 80 | 6 | 15 | 0 | 0 | 0 | 55 | dairy 1 |
| White milk (LD) | 1 carton | 100 | 12 | 8 | 2.5 | 0 | 0 | 130 | dairy 1 |
| Chocolate milk (LD) | 1 carton | 150 | 24 | 8 | 2.5 | 1 | 11 | 200 | dairy 1 |
| String cheese (LD) | 1 stick | 80 | 1 | 7 | 6 | 0 | 0 | 200 | dairy 0.67 |
| Turkey sandwich | whole wheat, 2 oz turkey | 280 | 30 | 20 | 5 | 4 | 4 | 900 | grains 2, protein 2, veg 0.25 |
| PB and J | whole wheat | 400 | 48 | 15 | 18 | 6 | 16 | 425 | grains 2, protein 2 |
| Pasta with meat sauce | 1.5 cups | 520 | 70 | 26 | 14 | 6 | 6 | 600 | grains 3, protein 2, veg 0.5 |
| Chicken and rice bowl | 1 bowl | 450 | 50 | 32 | 10 | 2 | 0 | 500 | grains 2, protein 3, veg 0.5 |
| Bean and cheese burrito | 1 | 450 | 60 | 18 | 14 | 9 | 1 | 900 | grains 2, protein 2, dairy 0.5 |
| Cheese pizza | 1 large slice | 285 | 36 | 12 | 10 | 2.5 | 3 | 640 | grains 2, dairy 0.75 |
| Baked salmon | 3 oz | 175 | 0 | 22 | 9 | 0 | 0 | 60 | protein 3 |
| Baked potato | 1 medium | 160 | 37 | 4 | 0 | 4 | 0 | 15 | veg 1 |
| Green salad | 2 cups, dressing | 120 | 8 | 2 | 9 | 2 | 2 | 250 | veg 1 |
| Steamed broccoli | 1 cup | 55 | 11 | 4 | 0.5 | 5 | 0 | 60 | veg 1 |
| Carrots and hummus (LD) | 1 pack | 110 | 12 | 3 | 6 | 4 | 0 | 210 | veg 0.5, protein 0.5 |
| Fried chicken sandwich | fast-food style | 600 | 50 | 28 | 30 | 2 | 6 | 1300 | grains 2, protein 3 |
| French fries | medium | 365 | 48 | 4 | 17 | 4 | 0 | 250 | veg 1 |
| Pretzels (LD) | 1 bag | 110 | 23 | 3 | 1 | 1 | 1 | 400 | grains 1 |
| Granola bar (LD) | 1 bar | 100 | 17 | 1 | 3.5 | 1 | 7 | 70 | grains 0.5 |
| Trail mix (LD) | 1 bag | 170 | 15 | 5 | 11 | 2 | 7 | 50 | protein 1 |
| Fruit smoothie | 16 oz | 300 | 60 | 8 | 3 | 5 | 10 | 100 | fruit 1.5, dairy 0.5 |
| Sports drink (LD) | 1 bottle | 140 | 36 | 0 | 0 | 0 | 34 | 270 | none |
| Water (LD) | 1 bottle | 0 | 0 | 0 | 0 | 0 | 0 | 0 | none |
Drinks for the Drinks check: water, milk, chocolate milk, sports drink, smoothie. Values are typical, not brands; the build agent checks each new row against USDA FoodData Central and MyPlate equivalents, fixes any off by more than 10 percent, and records the FDC id in a comment.

### Typical week (the starter, every athlete)
Every non-game day: Breakfast oatmeal, banana, white milk; Lunch turkey sandwich, apple, white milk; Snack pretzels, water; Dinner pasta with meat sauce, green salad, white milk; Evening snack Greek yogurt, strawberries. Day total 1,770 kcal, 256 g carbohydrate, 2,670 mg sodium, 13 g added sugars.
- Afternoon game day (Ana, Priya): Breakfast as above; Lunch PB and J, apple, white milk; Pre-game banana, pretzels, water; During water, sports drink; Recovery (Ana) chocolate milk, banana, or Recovery dinner (Priya) pasta, salad, chocolate milk; Dinner (Ana) pasta, salad, white milk. Ana's game day: 2,270 kcal, 2,610 mg sodium, 70 g added sugars (12 percent of calories).
- Morning game day (Marcus, Kai): Pre-game breakfast oatmeal, banana, white milk (58 g carbohydrate); During water, sports drink; Recovery (Kai) chocolate milk, banana, then Lunch PB and J, apple, white milk; Recovery lunch (Marcus) PB and J, apple, chocolate milk; Snack pretzels, water; Dinner pasta, salad, white milk.
- What the student finds in Ana's typical week (5 of 10 flags clear): Energy low ✗ Mon to Thu (73.75 percent); Food groups ✗ vegetables 12 of 21 cups and protein 28 of 45.5 oz; Added sugars ! Friday; Sodium ! every day; Recovery ! (51 g carbohydrate but 9 g protein). Marcus and Kai also get Pre-game meal ✗ (58 g); Priya gets Pre-game meal ✗ (only the 50 g snack is inside 1 to 4 hours of a 6:00 game).

### Flags (recomputed on every edit)
1. **Energy, low**: a day under 80 percent of its target ✗ ("Under-fueled: not eating enough for training can leave you tired and slow recovery.").
2. **Energy, very high**: a day over 130 percent ! .
3. **Food groups**: each group's week total against 7 times the daily target; under 80 percent ✗ per group.
4. **Added sugars**: over 10 percent of the day's calories (added sugar g times 4) ! per day.
5. **Sodium**: over 2,300 mg in a day ! per day.
6. **Breakfast**: skipped on a morning practice or game day ✗.
7. **Pre-game meal**: under 60 g carbohydrate eaten 1 to 4 hours before the start ✗ (both ends count: Ana's 12:00 lunch, exactly 4 hours before her 4:00 game, is inside).
8. **Heavy stomach**: 20 g fat or more, or 10 g fiber or more, eaten within 2 hours before the start ! .
9. **Recovery**: no slot within 2 hours after the game with at least 40 g carbohydrate and 15 g protein ! .
10. **Drinks**: no drink in the pre-game slot or in During ! .
The 80, 130, 60 g, 20 g, 10 g, 40 g and 15 g lines are the tool's own thresholds and say so in each flag's detail. A summary line: "7 of 10 flags clear".

### Fuel tank model (Game day; the tool's own teaching model)
- At wake: 30 + the smaller of 50 and (the day before's carbohydrate grams divided by 8). Monday's day before is the plan's Sunday.
- Each meal adds its carbohydrate grams times 0.25, spread evenly over the 60 minutes after its time; During items spread over the game. The tank never goes over 100.
- Awake and not playing: minus 0.05 a minute. Playing: minus the athlete's play drain a minute (table).
- Result at the end of play: 30 or more **Strong finish**; 15 to 29 **Running low late**; under 15 **Out of gas** with the clock time it crossed 15.
- Worked check, Ana's typical week: Thursday 256 g gives 62 at 6:30; meals add 14.5, 21.25 and 12.5; awake drain to 4:00 is 28.5; start 81.75; game minus 52 plus 9 from the sports drink gives 38.75, Strong finish. Without the pre-game snack: 26.25, Running low late. Marcus's typical week: start 67.5, end 26.1, Running low late.

### Result card texts
- Strong finish: "Fuel lasted the whole game. Carbohydrate the day before and the meals today kept the tank up."
- Running low late: "The tank ran low near the end. Look at the pre-game meal and the day before."
- Out of gas: "Out of fuel at {time}. Skipped or small meals before the game left too little."

### Fuel notes (six cards)
1. Energy in, energy out: athletes need more energy on training days than on rest days. Not eating enough for your training can leave you tired, slow recovery and hurt performance. (This tool uses the Dietary Guidelines "active" level for training days; a sports dietitian personalizes it.)
2. Carbohydrate is the main fuel for hard exercise. Eating carbohydrate foods the day before and the day of a game fills your stores.
3. Before: a meal 1 to 4 hours before, mostly carbohydrate with some protein and less fat and fiber, so it sits well.
4. After: carbohydrate and protein after hard exercise help refuel and repair muscles.
5. Fluids: drink before, during and after, more in the heat. Water is the main drink; sports drinks can help in long, hard sessions.
6. Supplements: most teens can get what they need from food. Supplements aren't checked by the FDA for safety or effectiveness before they're sold.

## Interactions in detail
- Selecting a cell (click, or arrows plus Enter) makes it the shelf's target; the selected cell has a 3 px accent outline. A fifth food is refused with "4 foods per meal here".
- Totals, bars and flags update in under 50 ms. Bars grow over 200 ms (instant with Motion off).
- Changing athlete swaps schedule, targets and slots and loads that athlete's saved plan if there is one, else the Typical week. Food in a slot that no longer exists is kept in a "Moved" note on that day for the student to place.
- Move meal clamps to its window (pre-game 1 to 4 hours before start; recovery 0 to 2 hours after end; others 1 hour either side).
- Game day replay: tank and clock move together; Pause holds both. Every control stays live while it runs: a meal edit or a Move meal drag during the replay redraws the tank line for the new plan at once and keeps playing from the same clock time; Restart starts from wake at once. With Motion off the replay still runs on time, the line simply draws without easing. 4x speed is 1 hour per 0.5 s.
- Save keeps one plan per athlete in localStorage `gdf-plans` (try/catch); Clear saved confirms. Nothing about the student is ever entered or stored.
- Language rules: no "good" or "bad" foods, no weight, no "burn off", no dieting. Flags talk about fuel, timing and balance.
- Sizes: at 1366x768 the week grid, the shelf and the top of the flags list fit; the selected-day label may scroll inside the panel. Under 900 px tall the shelf shows two rows with a filter row above. At 760 wide the grid scrolls sideways inside its box with slot names pinned.

## Look
- `kit/theme-912.css` with its own accent `--brand` #7fb2ff (jersey sky blue), `--brand-ink` #0c1a33.
- Contrast: accent on panel #141b25 8.01:1, on sec-bg #18202b 7.59:1; brand-ink on accent 8.02:1. Flag words use theme --ok and --warn with glyphs.
- MyPlate group colors on chips and amounts (always with the group name): fruit #ff8a8a, vegetables #5fd39a, grains #f2c46b, protein #c9a0ff, dairy #8fd0ff, each over 7:1 on #141b25. Fuel tank line in the accent; game block in a 20 percent accent tint.
- Group siblings: body-systems-tour orange, growing-up-q-a mauve, first-aid-responder mint, health-claim-checker yellow. 9-12 neighbors: fitness-program-designer lime, captain-s-choices coral. Food family: lunch-tray-builder orange #c4572f and label-detective teal #1d5c63 (both light themes).

## Art
Local FLUX (`scripts/localart.py`), no people. LD foods reuse label-detective's art. New food art, one shared prompt so they match label-detective's style: "{food}, top three-quarter view, soft flat illustration, blank packaging with no lettering, plain white background"; 1:1; cutout yes; people no; used as shelf and chip pictures and on the Game day meal flags:
- gdf-strawberries: a small bowl of fresh strawberries
- gdf-toast: two slices of whole-wheat toast on a white plate
- gdf-eggs: scrambled eggs on a white plate
- gdf-bagel-pb: a sliced bagel spread with peanut butter on a white plate
- gdf-turkey: a turkey sandwich on whole-wheat bread with lettuce and tomato
- gdf-pbj: a peanut butter and jelly sandwich cut in half
- gdf-pasta: a bowl of pasta with meat sauce
- gdf-ricebowl: a bowl of rice topped with sliced chicken and vegetables
- gdf-burrito: a bean and cheese burrito cut in half
- gdf-pizza: one slice of cheese pizza
- gdf-salmon: a baked salmon fillet with a lemon slice on a white plate
- gdf-potato: a baked potato split open
- gdf-salad: a green salad in a bowl
- gdf-broccoli: steamed broccoli in a bowl
- gdf-chicken-sandwich: a fried chicken sandwich in a plain paper wrapper
- gdf-fries: french fries in a plain red paper carton
- gdf-smoothie: a fruit smoothie in a tall clear cup
Athlete gear (same style, 1:1, cutout yes, people no, one per athlete card; different objects from fitness-program-designer's client cards):
- gdf-gear-ana: a black and white soccer ball beside a pair of soccer cleats
- gdf-gear-priya: an orange basketball beside a pair of high-top basketball shoes
- gdf-gear-marcus: swim goggles and a plain swim cap on a folded striped towel
- gdf-gear-kai: a pair of lightweight running spikes on a patch of grass beside a water bottle
21 images, none with people. The grid, day bars, flags, selected-day label, timeline, Fuel tank line and Drinks gauge are drawn in code (charts and controls).

## Voice
`easy-coach` (Umbriel): "Say in an easy-going, encouraging way, like a relaxed sports coach." Different from fitness-program-designer (calm-professor), captain-s-choices (wise-mentor), first-aid-responder (firm-captain), health-claim-checker (casual-peer) and playbook (lively-host); the food siblings have no voice. `Curio.voice`, `scope: () => state.mode`; Read speaks the selected flag, the result card or the hint.
| Key | Kind | When it plays | Line | Stale when |
|---|---|---|---|---|
| wPlan | how | Plan the week entered | This is a typical week. Tap a meal on the grid, then tap foods on the shelf to add them. | a food added, or mode left |
| howFlag | how | first edit that changes a flag | Tap a flag in the panel to see which days it is about. | a flag tapped |
| wGame | how | Game day entered, replay not running | Tap Play game day and watch the fuel tank. | Play tapped, or mode left |
| again | how | first result card | Tap a meal flag on the timeline to change it. Then tap Play game day again. | a meal edited |
| allClear | event | all ten flags clear | All ten flags clear. | any edit |
| strong | event | result Strong finish, every replay | Strong finish. The fuel lasted the whole game. | Restart or any edit |
| low | event | result Running low late, every replay | Running low near the end. Check the pre-game meal. | Restart or any edit |
| out | event | result Out of gas, every replay | Out of fuel in the second half. | Restart or any edit |
Flags, food values and Fuel notes are read on screen.

## Family engine
food (no family doc; the built siblings are the reference). Uses label-detective's food record (`RAW` rows: name, art, serving, servings per container, kind, then the 15 `KEYS` nutrients), its FDA Daily Values `DV` and rounding `R` for the selected-day label, and its art for the 13 LD foods. Uses lunch-tray-builder's five group keys (`fruit`, `veg`, `grain`, `protein`, `dairy`) and their names. Adds to each record a `groups` object of MyPlate amounts (cups or ounce-equivalents) and a `slotKind` (breakfast, meal, snack, drink). It feeds the engine 17 new food records, four athletes, slot templates and the flag rules above.

## Sources
- NHES 2024 (SHAPE America), Standards 6 and 7: https://www.shapeamerica.org/standards/health/
- Calorie levels by age, sex and activity (moderately active and active), food group amounts by calorie level, added sugars under 10 percent of calories, sodium under 2,300 mg for ages 14 and up: Dietary Guidelines for Americans 2020-2025, Appendix 2 and Appendix 3: https://www.dietaryguidelines.gov/ ; MyPlate: https://www.myplate.gov/
- Athletes' energy and carbohydrate needs, pre-exercise meal 1 to 4 hours before, protein and carbohydrate after, low energy intake harms performance, supplements not reviewed by FDA before sale: NIH Office of Dietary Supplements, "Dietary Supplements for Exercise and Athletic Performance": https://ods.od.nih.gov/factsheets/ExerciseAndAthleticPerformance-HealthProfessional/ and "Dietary Supplements: What You Need to Know": https://ods.od.nih.gov/factsheets/WYNTK-Consumer/
- Same points in detail: Thomas, Erdman and Burke, "Nutrition and Athletic Performance," ACSM, Academy of Nutrition and Dietetics and Dietitians of Canada joint position, Med Sci Sports Exerc 48(3), 2016.
- Fluids before, during and after; water first: CDC, "Heat and Athletes": https://www.cdc.gov/heat-health/hcp/clinical-guidance/heat-and-athletes.html
- Food values: USDA FoodData Central: https://fdc.nal.usda.gov/ ; label-detective's records (FDA 21 CFR 101.9 Daily Values).
- Tool's own, labeled on screen: the rest and training mapping to activity levels, flag thresholds, the fuel tank model and play drains.
- Checks run (Python, `gdf.py` in the R25 scratch folder): training day sums to 1,770 kcal, 256 g carbohydrate, 2,670 mg sodium, 13 g added sugars; Ana's game day 2,270 kcal, 2,610 mg sodium, 70 g added sugars (12.3 percent). Energy: 73.75 percent Mon to Thu (✗), 94.6 Fri, 88.5 Sat and Sun. Week groups: vegetables 12 of 21 cups (57 percent ✗), protein 28 of 45.5 oz (62 percent ✗), grains 49 of 56 (88), fruit and dairy over. Ana's recovery 51 g carbohydrate, 9 g protein (!). Pre-game: Ana's lunch (85 g, at exactly 4 hours) plus the 50 g snack pass; Priya has only the 50 g snack inside 2:00 to 5:00 (✗); Marcus and Kai's breakfast is 58 g (✗). So 5 of 10 flags clear, as listed. Fuel tank, minute by minute: Ana starts the game at 81.75 and ends at 38.75 (Strong finish); without the pre-game snack 26.25 (Running low late); Marcus starts 67.5, ends 26.1; Kai 69.0 to 27.0; Priya 75.75 to 35.25; none crosses 15. Atwater check (4, 4, 9 per gram) within 15 percent for every food but broccoli (55 listed, 64 by Atwater: fiber lowers it; USDA lists about 55, kept). Replay lengths at 1 hour per 2 s from wake to the final whistle: 21.7, 26.0, 12.0 and 7.0 s, all under 30 s (it used to run to bedtime, over 30 s). Contrast ratios recomputed: all as listed.

## Done when
1. Ana's Typical week shows exactly the flags listed under "Typical week" (5 of 10 clear); each day's kcal, carbohydrate and sodium match a hand sum of the table (1,770 kcal, 256 g, 2,670 mg on a training day; 2,270 kcal on game day).
2. Adding and removing foods updates bars, the selected-day label and flags at once; a fifth food is refused.
3. Game day replay for Ana's typical week ends at 38.75 (shown 39 percent), Strong finish; removing the pre-game snack ends at 26 percent, Running low late; Marcus's typical week ends at 26 percent.
4. Moving the pre-game meal outside 1 to 4 hours is blocked; moving it within 2 hours of the start with the fried chicken sandwich raises Heavy stomach.
5. Changing athlete swaps schedule, slots, targets and game time; Kai's and Marcus's game days start with a pre-game breakfast.
6. Save, reload, Load restores each athlete's plan; Clear saved empties `gdf-plans`; nothing else is stored.
7. No body weight, size or "diet" word appears anywhere in the tool (search the DOM text).
8. Focus: the week grid is the biggest, central thing in Plan the week, and the tank line in Game day; at 1366x768 grid, shelf and flag summary are visible; at 760 wide the grid scrolls inside its box; keyboard alone can fill a day.
9. A tap while the replay runs acts at once: Pause stops the clock within one frame, and a meal edit redraws the tank line at once; the replay ends at the final whistle in under 30 s for every athlete.
10. Result lines speak every replay; how lines once per load.
11. All 21 new paintings show beside the 13 LD pictures in one matching style; no person appears.

## Open questions
1. Rename to "Game Day Fuel" (the overlap pass's suggestion) as written? The topic line keeps "nutrition and fitness planning".
2. The 2025-2030 Dietary Guidelines came out in January 2026 and changed some advice. This spec uses the 2020-2025 calorie and food group tables; should the build switch to the new edition's numbers where they differ (the build agent would recheck every target)?
3. Athletes are all fictional; there is no "my own week" with the student's age and sex, to keep nothing about the student entered. OK?

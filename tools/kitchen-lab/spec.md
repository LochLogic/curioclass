# Kitchen Lab

## One idea
In a warm family kitchen at 4:15 in the afternoon, Grandpa Leo (made up, labeled "illustration") hands the child a recipe card for a dinner that must be on the table at 6:00 (soup that takes 45 minutes, a roast chicken that takes 1 hour 20 minutes, and rolls that take 25 minutes), and the child plans each start time by dragging jumps backward on an elapsed-time number line (6:00 back 45 minutes is 5:15) and sets each start on a clock to the minute; then the ingredients: the child estimates first ("Is a pumpkin about 3 grams or 3 kilograms?") and then weighs on a kitchen scale in grams and kilograms, pours water to 2 liters in a measuring jug, and solves one-step kitchen problems with all four operations (4 bags of 250 grams of rice, 9 liters of soup shared among 3 pots, 2 kilograms of flour minus the 1 kilogram used); at 6:00 a good plan has every dish ready together, while a late plan shows the soup still bubbling, so a third grader learns to tell and write time to the minute, to solve elapsed-time problems on a number line, and to estimate and measure liquid volume and mass in liters, grams and kilograms with one-step problems.

## Not like
- clock-shop (1, spec): hour and half hour, same clock engine. Here minutes and elapsed time.
- smoothie-lab (6-7, live): ratios in recipes. Here measuring and timing.
- estimation-station (2, spec): estimating length. Here mass and liquid volume.
- recipe-scaler (4, concept): fractions of a cup. Here grams, liters and minutes.

## Who and how
- Grade 3, Math, module "Time, Volume and Mass". Standards: 3.MD.1 (tell and write time to the nearest minute and measure time intervals in minutes; solve word problems involving addition and subtraction of time intervals in minutes, e.g., by representing the problem on a number line diagram), 3.MD.2 (measure and estimate liquid volumes and masses of objects using standard units of grams, kilograms, and liters; add, subtract, multiply, or divide to solve one-step word problems involving masses or volumes that are given in the same units).
- Format: lab. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Three dishes to time, the time line, the clock, the kitchen scale, the measuring jug, six estimate-then-weigh items, six one-step problems, the 6:00 dinner. Extra: My family meal (the child sets a dinner time and three dishes of their own). tool.json `modes: ["Kitchen", "My family meal"]`, `minutes: "20-30"`, `grades_label: "Grade 3"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 3.MD.1 | Jump back from 6:00 on the time line; set the start on the clock to the minute | jumps labeled in minutes; the clock hands | 2 |
| 3.MD.2 (measure, estimate) | Estimate, then weigh and pour | the scale in g or kg; the jug to 2 L | 3 |
| 3.MD.2 (problems) | Solve six one-step problems in the same units | the bags, pots and flour on the counter | 4 |

## Screens and modes
Header (kit): title "Kitchen Lab"; `Kitchen`, `My family meal`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A home kitchen, a wall clock at 4:15, a recipe card on the counter and Grandpa Leo in an apron. The welcome is queued (`welcomeAfter: true`): "Dinner is at 6:00! The soup takes 45 minutes. When should it start? Drag a jump onto the time line." First hint: "Drag a jump onto the time line."

**Timing (focus: the time line).** At 1366x768 the kitchen fills the left with the time line along the bottom and the recipe card right; at 680x425 the card folds into a tab. The time line runs 4:00 to 6:30 with ticks every 5 minutes. The child drags jump arrows backward from 6:00 (a 30, then a 15) and the line labels the landing: 5:15. Then the child sets the wall clock to 5:15 by dragging the minute hand; the hour hand follows. Chicken: 1 hour 20 minutes back is 4:40, 25 minutes after the 4:15 start of the day. Rolls: 5:35.

**Estimate, then weigh.** Six items: a pumpkin, a bag of rice, an apple, a paper clip, a pot of water, a bag of flour. Two choices first ("about 3 grams or 3 kilograms?"), then the item goes on the scale and the reading appears in grams or kilograms. A note: 1 kilogram is 1,000 grams; a liter of water has a mass of about 1 kilogram.

**Pour.** The jug is marked in liters; the child pours to 2 L for the soup.

**Kitchen problems.** One step each, same units: 4 bags of 250 grams of rice is how many grams? 9 liters of soup shared among 3 pots? 2 kilograms of flour minus 1 kilogram used? Three more like them. Each answer pours or stacks on screen.

**Six o'clock (the aha).** The clock runs forward. With a right plan every dish is ready at 6:00; a late start shows the soup still bubbling and the time line marks how many minutes short. Grandpa Leo: "Work backward from when you want to eat. That's the cook's secret."

**The end.** The plan card with three start times and the measured amounts. `Print` prints it.

**My family meal (extra).** The child picks a dinner time and three dishes with cooking times and plans starts.

## Content
- Three dishes with times, six weigh items with true typical masses (labeled "about"), six one-step problems in grams, kilograms and liters, all readable with `Read`.
- Whole numbers only, as the standard asks.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Jumps snap to 5-minute and 1-minute steps; the clock's minute hand snaps to each minute.
- Keyboard: Tab to jumps, the clock hands, the items, the scale, the jug and the answer box; arrows move a jump or hand by one minute; Enter places.
- With Motion off the clock jumps to 6:00 and the jug fills at once.

## Look
- Accent `--brand` #a33a1f tomato red (header, the time line, buttons); gold #f4c542 (the jump in hand, a dish that is ready); paper #fbf1ee; ink #2b0d06; muted #5f514c.
- Contrast (WCAG 2.1, computed): white on brand 6.60:1; brand on paper 5.94:1; ink on paper 16.27:1; muted on paper 6.83:1; ink on gold 11.10:1.
- Never color alone: ready dishes carry a check and the word "ready"; jumps carry minute labels.
- Different from this batch (dungeon violet, kitchen-tile blue, highway green, soil brown).

## Art
- People (illustrated): Grandpa Leo, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the kitchen (1, 16:9), six weigh items (6, 1:1), the dinner table (1, 16:9).
- Drawn in code: the time line, the clock, the scale dial, the jug marks.
About 9 images.

## Voice
Two bank voices, each unique in this batch: `friendly-dad` as Grandpa Leo; `clear-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.dish + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `jump`: "Drag a jump onto the time line."
- how `clock`: "Drag the minute hand to the start time."
- how `estimate`: "Pick grams or kilograms, then tap Weigh."
- how `pour`: "Drag the jug handle to pour to 2 liters."
- how `solve`: "Type the answer."
- event, whole, six o'clock.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Reuses the clock from the marked block `/* CLOCK ENGINE: begin */ ... /* end */` as described in clock-shop's spec (geared hands, minute snapping) and the number line from `kit/number-line.js` as described in roller-coaster-rounding's spec (`NumberLine` with a time `format`, `nl.span` for jumps). Tool-only code: the scale, the jug, the dishes and the six o'clock run.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Start times | Set the clock by trying | The clock needs a time line plan first, and six o'clock shows minutes short. |
| Estimates | Always pick kilograms | Light items like the apple and paper clip are in grams. |
| Problems | Guess | Each answer is shown as bags, pots or flour that must match. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `jump`; `clock`.
2. `estimate`; `pour`.
3. `solve`.
4. Six o'clock (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 3.MD.1, 3.MD.2 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| 1 kilogram is 1,000 grams; a liter is 1,000 cubic centimeters | NIST, Special Publication 330, "The International System of Units" | BIPM, "The International System of Units (SI Brochure)", 9th edition | yes |
| A liter of water has a mass of about 1 kilogram | NIST, "SI Units: Mass" | BIPM, SI Brochure, history of the kilogram | yes |
| Elapsed time on a number line for grade 3 | Common Core Standards Writing Team (2011), "Progressions for the CCSS, K-5 Measurement and Data" | Common Core Standards Writing Team (2012), "Progressions for the CCSS, Geometric Measurement" | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad s12, 2026-11-10): 6:00 back 45 minutes is 5:15, back 1 hour 20 minutes is 4:40 and back 25 minutes is 5:35; 4:40 is 25 minutes after 4:15; 4 times 250 grams is 1,000 grams, 9 liters shared by 3 is 3 liters, 2 kilograms minus 1 kilogram is 1 kilogram; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 kitchen, time line and card; at 680x425 card as a tab.
2. Three start times are found on the time line and set on the clock to the minute. (3.MD.1)
3. Six items are estimated and then weighed or poured in grams, kilograms or liters. (3.MD.2)
4. Six one-step problems are solved in the same units. (3.MD.2)
5. `Read` reads every card; every control is 48 px or more.
6. Grandpa Leo is labeled illustration; masses say "about".
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: the clock jumps and the jug fills at once; no network requests.

## Open questions
None.

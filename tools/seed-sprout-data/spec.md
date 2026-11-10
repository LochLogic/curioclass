# Seed Sprout Data

## One idea
On a classroom windowsill twelve pots of bean seedlings wait for day 10, and the child's teacher, Mr. Tran (made up, labeled "illustration"), asks for a measurement of every bean; the child drags a ruler to each seedling and reads its height to the nearest 1/8 inch, and each reading drops a dot on a line plot marked in eighths (the plants are simulated, and the tool says so); line plot questions follow: the tallest minus the shortest is 1 1/2 inches, and each 2 3/4 inch bean is 1 1/4 inches taller than the 1 1/2 inch one; a second line plot shows the uneven water each pot got (three pots 1/4 cup, six pots 1/2 cup, three pots 3/4 cup), and the child pours it all into one jug and shares it out equally, so each pot gets 1/2 cup; planning rounds convert units for a month of care (12 pots x 3/4 cup a day is 9 cups, so a week is 63 cups or 15 3/4 quarts; an 18-inch vine is 1 1/2 feet; seeds 5 cm apart are 0.05 m apart); at the end the child sees that a line plot of fractions can be added, compared and shared out like any numbers, so a fifth grader learns to make line plots of measurements in fractions of a unit and solve problems with them, and to convert among units within one system in multi-step problems.

## Not like
- unit-ladder (4, spec): conversion tables between units. Here conversions inside a plan.
- skate-park-angles (4, spec): a line plot of jump heights in whole and half units. Here eighths and fair sharing.
- box-plot-builder (6, spec): summary statistics. Here measuring and fraction operations on a plot.
- fraction-kitchen (5, spec): adding unlike fractions in recipes. Here fractions read from a plot.

## Who and how
- Grade 5, Math, module "Units and Line Plots". Standards: 5.MD.1 (convert among different-sized standard measurement units within a given measurement system (e.g., convert 5 cm to 0.05 m), and use these conversions in solving multi-step, real world problems), 5.MD.2 (make a line plot to display a data set of measurements in fractions of a unit (1/2, 1/4, 1/8); use operations on fractions for this grade to solve problems involving information presented in line plots; for example, given different measurements of liquid in identical beakers, find the amount of liquid each beaker would contain if the total amount in all the beakers were redistributed equally).
- Format: lab (changed from data). Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Twelve simulated seedlings, the height line plot, the water line plot and jug, six plot questions, six planning problems. Extra: Our beans (the class enters real heights from beans they grew; they stay on the device). tool.json `modes: ["Windowsill", "Our beans"]`, `minutes: "25-35"`, `grades_label: "Grade 5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 5.MD.2 | Measure to the nearest 1/8 inch; drop dots | the line plot in eighths | 2 |
| 5.MD.2 | Answer plot questions; share the water equally | the jug split into 12; 1/2 cup each | 3 |
| 5.MD.1 | Convert cups to quarts, inches to feet, cm to m in plans | the plan card filling in | 4 |

## Screens and modes
Header (kit): title "Seed Sprout Data"; `Windowsill`, `Our beans`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A bright windowsill with twelve numbered pots, a ruler, a watering can, a notebook, and Mr. Tran with a clipboard. A small note reads "These plants are simulated." The welcome is queued (`welcomeAfter: true`): "Day 10. Let's measure every bean. Drag the ruler to pot 1." First hint: "Drag the ruler to pot 1."

**Measure (focus: the pot).** At 1366x768 the windowsill runs across the top with the ruler zoom left and the line plot right; at 680x425 the plot is a tab. The ruler zoom shows eighth-inch marks; the child taps the mark at the tip and the reading appears (2 3/8 in). A dot drops on the plot. Twelve readings from 1 1/2 to 3 inches.

**Plot questions.** Six questions on cards: tallest minus shortest; how much taller each 2 3/4 inch bean is than the 1 1/2 inch one; how many beans are taller than 2 1/4; the total height of the two 2 1/4 inch beans. Each answer is typed as a fraction or mixed number.

**Fair water.** A second line plot shows the cups each pot got. The child drags every pot's water into one jug (6 cups in all), then splits the jug into 12 equal shares and types 1/2 cup each. The plot redraws with every dot at 1/2.

**Plan the month.** Six multi-step problems on a plan card: 12 pots x 3/4 cup a day for a week in cups, then quarts (63 cups, 15 3/4 quarts); a vine at 18 inches in feet; seed spacing 5 cm in meters; and three more.

**Same numbers (the aha).** Mr. Tran: "A line plot of fractions is still numbers. You can add them, compare them, and share them out."

**The end.** The notebook with both plots and the plan card. `Print` prints it.

**Our beans (extra).** The class types real heights; they drop on the plot the same way.

## Content
- Twelve simulated heights in eighths, labeled "simulated", the water plot, twelve problems, all readable with `Read`.
- Units: cups, quarts, inches, feet, centimeters, meters; conversions stay inside one system.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A reading can be retaken until the dot is placed; dots can be moved until `Check`.
- Keyboard: Tab to pots, the ruler, the zoom marks (arrows move one eighth), the plot, the jug and answer boxes; Enter measures or checks.
- With Motion off dots appear on the plot and water appears in the jug.

## Look
- Accent `--brand` #2e6b3a sprout green (header, the plot axis, buttons); gold #f4c542 (the ruler mark in hand, the shared jug); paper #eef6ef; ink #0c2412; muted #4f5a51.
- Contrast (WCAG 2.1, computed): white on brand 6.40:1; brand on paper 5.81:1; ink on paper 14.93:1; muted on paper 6.54:1; ink on gold 10.11:1.
- Never color alone: dots stack with counts; heights carry numbers.
- Different from this batch (magnifier indigo, chart sea blue, sign red, cardboard umber).

## Art
- People (illustrated): Mr. Tran, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the windowsill (1, 16:9), seedlings at four heights (4, 1:1), the watering can and jug (1, 1:1).
- Drawn in code: the ruler and eighth marks, both line plots, the plan card.
About 7 images.

## Voice
Two bank voices, each unique in this batch: `friendly-dad` as Mr. Tran; `warm-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.pot + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `measure`: "Tap the ruler mark at the tip."
- how `question`: "Type the answer as a fraction."
- how `pour`: "Drag each pot's water to the jug."
- how `share`: "Type how much each pot gets."
- how `plan`: "Fill in the next box on the plan."
- event, whole, same numbers.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: exact fractions with `Frac` as described in equation-golf's spec, the eighth-inch ruler, two line plots, the jug, the plan card.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Measuring | Tap the nearest whole inch | Readings are checked to the eighth. |
| Fair share | Type the middle value | The total must be poured and split first; the typed share is checked against it. |
| Plans | Convert once | Each problem needs two steps, and both boxes are checked. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `measure`.
2. `question`.
3. `pour`; `share`.
4. `plan`.
5. Same numbers (whole), waits. Then `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 5.MD.1, 5.MD.2 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| 1 quart = 4 cups; 1 foot = 12 inches; 1 m = 100 cm | NIST, Handbook 44, Appendix C, "General Tables of Units of Measurement" | NIST, Special Publication 811, "Guide for the Use of the International System of Units" | yes |
| Bean seeds are planted a few centimeters apart | University of Minnesota Extension, "Growing beans in home gardens" | University of Illinois Extension, "Watch Your Garden Grow: Beans" | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s16, 2026-11-10): twelve heights from 1 1/2 to 3 give a range of 1 1/2; 2 3/4 - 1 1/2 = 1 1/4; 3 x 1/4 + 6 x 1/2 + 3 x 3/4 = 6 cups and 6 / 12 = 1/2; 12 x 3/4 = 9 cups a day, 63 a week, 63 / 4 = 15 3/4 quarts; 18 in = 1 1/2 ft; 5 cm = 0.05 m; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 windowsill, ruler and plot; at 680x425 plot as a tab.
2. Twelve seedlings are measured to the nearest 1/8 inch and plotted. (5.MD.2)
3. Plot questions and the fair water share are solved with fraction operations. (5.MD.2)
4. Six planning problems convert units within one system in more than one step. (5.MD.1)
5. The plants are labeled simulated; Our beans data stays on the device.
6. `Read` reads every card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: dots and water appear at once; no network requests.

## Open questions
- The idea card changes the format from data to lab (default used: lab, since the child measures and concludes from a windowsill experiment rather than browsing a public data set).

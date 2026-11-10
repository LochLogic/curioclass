# Snow Globe Maker

## One idea
At a winter craft-fair booth the child's partner, Rafa (made up, labeled "illustration"), sets out a cylinder, a cone and a sphere with the same radius (5 cm) and height (10 cm) and a jug of water, and asks how much each holds; pour tests answer it: three cones of water fill the cylinder, and one sphere fills two thirds of it, so from the cylinder's pi r squared h (250 pi, about 785.4 cubic centimeters) come the cone at a third (about 261.8) and the sphere at four thirds pi r cubed (about 523.6); booth days bring orders for snow globes (spheres), candle molds (cones) and wooden bases (cylinders), and the child computes volumes, buys water, wax and glitter by the liter, and sets prices, discovering that doubling a globe's radius takes eight times the water; missing-dimension orders run the formulas backward: a globe that holds exactly 1 liter needs a radius of about 6.2 cm, and a candle cone 12 cm tall holding 500 milliliters of wax needs a radius of about 6.3 cm, so a mold about 12.6 cm wide; at the end the child sees three shapes in one family of formulas and how small changes in radius make big changes in volume, so an eighth grader learns the formulas for the volumes of cones, cylinders and spheres and uses them to solve real problems.

## Not like
- box-packer (5, spec): volume of prisms by cubes. Here curved solids.
- big-wheel-small-wheel (7, spec): circle area and circumference. Here volume built on circles.
- packaging-challenge (10, spec): least material. Here volume and cost.
- aquarium-builder (7, spec): composite prisms. Here cones, cylinders and spheres.

## Who and how
- Grade 8, Math, module "Volume of Cylinders, Cones and Spheres". Standards: 8.G.9 (know the formulas for the volumes of cones, cylinders, and spheres and use them to solve real-world and mathematical problems).
- Format: tycoon. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Three pour tests, four booth days of orders, six missing-dimension orders, the supply shop and price board. Extra: Booth fair (the class compares booth profits on the projector). tool.json `modes: ["Booth", "Booth fair"]`, `minutes: "25-35"`, `grades_label: "Grade 8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 8.G.9 (formulas) | Pour cone and sphere into the cylinder | three cones fill it; a sphere fills two thirds | 2 |
| 8.G.9 (use) | Fill orders; buy supplies; set prices | the booth ledger | 3 |
| 8.G.9 (backward) | Find radius or height from a volume | 6.2 cm for a liter globe | 4 |

## Screens and modes
Header (kit): title "Snow Globe Maker"; `Booth`, `Booth fair`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A cozy craft-fair booth with string lights, a workbench holding a cylinder, a cone and a sphere, a water jug, and Rafa in a knit hat. The welcome is queued (`welcomeAfter: true`): "How much does each hold? Drag the cone under the jug to fill it." First hint: "Drag the cone under the jug."

**Pour (focus: the bench).** At 1366x768 the bench fills the left with the formula card right; at 680x425 the card is a sheet. The child fills the cone and pours it into the cylinder; a level line rises a third. Three pours fill it. Then the sphere: one pour reaches two thirds. The card builds each formula from the pours; the child types each volume for r = 5, h = 10, to a tenth.

**Booth day.** Orders arrive on tickets (12 small globes, 6 candle molds, 4 bases). The child computes each volume, totals the water, wax and glitter, and buys them by the liter at sample prices. A price board sets what each item sells for; the ledger shows cost and profit.

**Double it.** A customer asks for a globe twice as wide. The child predicts the water; the pour shows 8 times.

**Backward.** Six orders give a volume and ask for a radius or height. The child solves and the tool builds the shape to check.

**One family (the aha).** Rafa: "Three shapes, one family. And a little more radius makes a lot more volume."

**The end.** The booth's best day. `Print` prints the ledger.

**Booth fair (extra).** Profits compared.

## Content
- Volumes in cubic centimeters and milliliters (1 to 1), pi from the calculator key, answers to a tenth, sample prices labeled "sample prices", all readable with `Read`.
- Candles and globes are winter crafts, not tied to one holiday.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Pours can be repeated; ledger lines can be retyped until `Close the day`.
- Keyboard: Tab to the shapes (Enter picks up and pours), the jug, answer boxes, tickets, the shop and the price board; Enter checks.
- With Motion off pours show the final level at once.

## Look
- Accent `--brand` #9b2340 cranberry (header, the ledger, buttons); gold #f4c542 (the shape in hand, the water line); paper #fbeff2; ink #2b0811; muted #5d4f53.
- Contrast (WCAG 2.1, computed): white on brand 7.75:1; brand on paper 6.92:1; ink on paper 16.35:1; muted on paper 6.91:1; ink on gold 11.27:1.
- Never color alone: levels carry fraction marks; profit and loss carry plus and minus signs.
- Different from this batch (puzzle plum, glacier blue, timber olive, harbor teal).

## Art
- People (illustrated): Rafa and four customers of varied looks, labeled "illustration" (Gemini, `people: true`, 5; cutout yes).
- Local FLUX (`scripts/localart.py`): the craft-fair booth (1, 16:9), finished globes and candles (2, 1:1).
- Drawn in code: the solids, pours and levels, so levels match the math.
About 8 images.

## Voice
Two bank voices, each unique in this batch: `big-sister` as Rafa; `warm-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.day + ':' + state.order + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `pour`: "Drag the shape under the jug, then onto the cylinder."
- how `volume`: "Type the volume to a tenth."
- how `order`: "Type the volume for this order."
- how `buy`: "Tap the supplies you need."
- how `backward`: "Type the radius."
- event, whole, one family.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the solids and pour levels, volume checks to a tenth, the supply shop and ledger; cents use `money` and `r2` as described in paycheck-decoder's spec.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Volumes | Use the cylinder formula for all | Cone and sphere orders are checked against their own formulas. |
| Doubling | Double the water | The pour shows 8 times, and the prediction is logged. |
| Backward | Guess and check by typing | Each guess must come with the solved equation. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `pour`; `volume`.
2. `order`; `buy`.
3. `backward`.
4. One family (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 8.G.9 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| A cone is one third and a sphere two thirds of the matching cylinder | Archimedes, "On the Sphere and Cylinder" (Heath translation, 1897) | Common Core Standards Writing Team (2016), "Progressions for the CCSS, Geometry, 7-8" | yes |
| One milliliter equals one cubic centimeter | NIST, Special Publication 811 | BIPM, "The International System of Units (SI Brochure)" | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s21, 2026-11-10): with r = 5 and h = 10 the cylinder is about 785.4, the cone about 261.8 and the sphere about 523.6, two thirds of the cylinder; a 1 liter sphere has r about 6.2; a 500 mL cone 12 tall has r about 6.3 and width about 12.6; doubling r gives 8 times the volume; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 bench and card; at 680x425 card as a sheet.
2. Pour tests build the cone and sphere formulas from the cylinder. (8.G.9)
3. Four booth days of orders are filled with volumes, supplies and prices. (8.G.9)
4. Six missing-dimension orders are solved backward. (8.G.9)
5. Prices are labeled sample prices.
6. `Read` reads every card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: pours show final levels; no network requests.

## Open questions
None.

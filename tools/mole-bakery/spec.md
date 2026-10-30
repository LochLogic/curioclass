# Mole Bakery

## One idea
A baker can only weigh leaveners, but the reaction counts particles: every order goes grams to moles, through the
balanced equation's mole ratio, and back to grams, and the ingredient that runs out first decides how much gas the
batter gets, while whatever is left over shows up in the taste (extra baking soda bakes into soapy washing soda,
extra acid stays sour).

## Not like
- unit-detective / Unit Sense (gr 9, math): chains conversion cards to check claims. Here every chain runs through a balanced equation, and the deciding step is the mole ratio and the limiting ingredient, not the units.
- reaction-kitchen (gr 7, molecules, not specced): counts atoms in baking soda and vinegar to show mass is kept. Here the same kind of reaction is scaled in grams and moles, with five leavening reactions and a limiting ingredient.
- equation-balancer (gr 10, same group): finds the coefficients. Here the coefficients are given and turned into amounts.
- startup-tycoon / Startup Booth (gr 9-12, CTE): prices, costs and profit. Here coins are game tokens; every decision is a chemical amount.
- energy-accountant (gr 9, biology): fermentation as an energy ledger. Here fermentation is a gas recipe with a percent yield.

## Who and how
- Grade 10, Chemistry, Stoichiometry and the Mole. Students drive. 20 to 40 minutes (the week takes about 25).
- Topic line: "moles, mole ratios and limiting reactants".
- Standards (module): HS-PS1-7 (mass is conserved, shown with math: the mass check on every bake, and every mole calculation).
- tool.json: driver "students", minutes "20-40", modes ["Test kitchen", "Bakery"], grades_label "Grade 10".

## Screens and modes
Header: title, subtitle "Weigh in grams. React in moles." Modes `Test kitchen` (opens first), `Bakery`. Kit buttons.
Stage: the painted bakery counter (`mb-counter`, dimmed) with the painted digital scale (`mb-scale`, grams in code
over its blank display), the painted clear glass mixing bowl seen from the side (`mb-bowl`), and the painted oven
(`mb-oven`) whose window shows the order's bake (Art). The bowl shows its particles as dots drawn in code behind the
bowl image, whose glass is clear enough to show them (molecules engine colors), 1 dot = 0.001 mol (or 1 dot =
0.01 mol past 120 dots of one kind, said in the key). Pantry jars are painted cutouts with code labels.
Focus: in Test kitchen, the bowl of dots with the ingredient rows beside it (the `runs out first` row next to the
bowl); during `Bake`, the oven window. In Bakery, the order board and the bowl, side by side, central. Panel: reaction picker (equation with names), ingredient rows, results, hint.
Ingredient row: name and formula, grams box and slider (0 to 100 g, step 0.01; vinegar 0 to 300 g), molar mass,
moles, and "makes" (the gas this ingredient alone could make by the ratio). The limiting ingredient's row gets the
words `runs out first`.

### Test kitchen (explore)
Opens on R1 with 4.20 g baking soda and 9.41 g cream of tartar, so `Bake` works at once. Pick a reaction (R1 to
R5), set grams, and the bowl and rows update live. `Bake` plays the oven for about 3 s: dots pair up in
the equation's ratio and gas bubbles rise into the dough, leftovers stay in the bowl (instant with Motion off).
During the bake every control stays live: new grams, a new reaction, a mode button or `Bake` again act in the same
frame (the bake in progress is dropped and the bowl shows the new state).
Results card: gas made (mol, g, and mL at 25 °C and 1 atm), leftovers (g of each), taste (`clean`, `soapy`,
`sour`), and the mass check: "before 13.61 g = after 13.61 g (2.20 g left as gas)". `Mix exact` fills the other
ingredient to match the first one's moles (and says so in the log, so it is a check, not a shortcut in Bakery).

### Bakery (tycoon)
A week of six days. Each day shows an order board (one to four orders, each a card with its painted bake: biscuits,
vinegar cake, bread or crisp cookies), the pantry (grams on hand of each
leavener) and the till (coins). For each order: pick its reaction (fixed by the product), set grams, `Bake`.
`Buy` adds 100 g of an ingredient for its price (Content), except on days the supplier is closed. Each bake
result: rise (gas in the dough against the order's target), taste, coins earned, ingredients used. An order paid in
full needs rise within 5 percent of the target and a clean taste; otherwise "The customer took it at half price."
`End day` moves on. Week ledger at the end: coins, grams wasted as leftovers, and each day's limiting ingredient.
Progress saved on this device (localStorage `curio-mole-bakery`, try/catch), `New week` restarts.

## Content
Constants: Avogadro constant 6.02214076 × 10²³ /mol (shown in the dot key: "0.001 mol is 6.02 × 10²⁰
particles"); molar gas volume at 25 °C and 1 atm 24.47 L/mol (from PV = nRT; 24.465 in the math).
Reactions (molar masses from the molecules engine, shown to 2 decimals):
- R1 Biscuit powder: NaHCO3 + KHC4H4O6 → KNaC4H4O6 + H2O + CO2. Baking soda 84.01 g/mol, cream of tartar 188.18.
- R2 Vinegar cake: NaHCO3 + HC2H3O2 → NaC2H3O2 + H2O + CO2. White vinegar entered as grams of vinegar; 5.0 g of
  acetic acid (60.05 g/mol) in every 100 g (labels say "5% acidity", grams per 100 mL; vinegar is close to
  1.0 g/mL, so the tool treats it as per 100 g and says so in the help).
- R3 Bread: C6H12O6 → 2 C2H5OH + 2 CO2 (yeast does it; the ethanol bakes off). Glucose 180.16, ethanol 46.07.
- R4 Crisp cookies: NH4HCO3 → NH3 + CO2 + H2O, baker's ammonia 79.06 (the sum is 79.055; show 79.06 as PubChem
  does, rounding half up on the exact sum, since floating point gives 79.05499); all three come off as gas in a hot oven, so
  each mole gives 3 mol of gas (the label says thin cookies let the ammonia smell bake out).
- R5 Leftover soda in the oven: 2 NaHCO3 → Na2CO3 + H2O + CO2, applied automatically to any leftover baking soda
  after R1 or R2: half a mole of CO2 per mole of leftover soda, and the sodium carbonate (washing soda) tastes soapy.
Taste rule: an ingredient is "left over" when more than 2 percent of its starting moles remain. Leftover soda:
soapy; leftover cream of tartar or acetic acid: sour. Glucose leftovers taste sweet and count as clean.
Prices (game coins per 100 g, made up): baking soda 2, cream of tartar 10, vinegar 1, glucose 3, baker's ammonia 6.
Week (target gas in the dough; pay; the worked answer):
- Day 1 Biscuits: 0.050 mol CO2; pays 20. 4.20 g soda + 9.41 g cream of tartar; 1,223 mL of gas.
- Day 2 Vinegar cake: 0.060 mol CO2; pays 18. 5.04 g soda + 72.06 g vinegar (3.60 g acetic acid).
- Day 3 Supplier closed, 6.00 g cream of tartar in the pantry. Orders: four biscuit batches, 0.010 mol CO2 each,
  5 coins each, and you may decline any. 6.00 g is 0.0319 mol: each batch takes 1.88 g cream of tartar and 0.84 g
  soda, so three batches use 5.64 g (5.65 g by moles, 0.030 mol) with 2.52 g soda; a fourth would need 1.88 g with
  only 0.36 g left. Declining one costs nothing.
- Day 4 Bread: the proof box log says yesterday's dough kept 3.96 g of CO2 from 9.01 g glucose (this bakery's
  yeast, a made-up figure). Percent yield 3.96 / 4.40 = 90.0 percent. Order: 0.090 mol of gas kept in the dough;
  pays 16. Needs 0.100 mol made: 9.01 g glucose.
- Day 5 Crisp cookies: 0.090 mol of gas; pays 14. 0.030 mol baker's ammonia: 2.37 g (not 7.11 g: three gases per
  formula unit).
- Day 6 Rush: pantry has 8.00 g soda and the supplier is closed. Biscuits 0.040 mol (3.36 g soda + 7.53 g cream of
  tartar), vinegar cake 0.030 mol (2.52 g soda + 36.03 g vinegar), cookies 0.060 mol gas (1.58 g baker's ammonia).
  Soda used 5.88 g; 2.12 g left in the pantry.
Mass check example (Day 1): 4.20 + 9.41 = 13.61 g in; out: 10.51 g sodium potassium tartrate + 0.90 g water +
2.20 g CO2 = 13.61 g.
Starting till: 30 coins. Starting pantry: 100 g of each except as the day says.

## Interactions in detail
- Moles = grams ÷ molar mass, exactly (floating point, shown to 4 significant figures); for vinegar, moles of acid
  = 0.050 × grams ÷ 60.05. Extent of reaction = the smallest of (moles of each reactant ÷ its coefficient).
  Gas = extent × gas coefficient (R4 counts all three gases), plus R5 on leftover soda; for R3 the gas kept is
  extent × 2 × the day's yield (90 percent on Days 4 and later in Bakery; 100 percent in Test kitchen, said on
  the card).
- Rise check: |gas kept − target| ≤ 5 percent of target. Taste check as in Content.
- Grams entered beyond the pantry are refused ("Only 6.00 g on the shelf"). Zero grams of a needed ingredient:
  the bake makes no gas from that reaction and says which ingredient was missing.
- Mass check always balances: grams in = grams of products + leftovers + gas; the card lists each.
- `Mix exact` is available in both modes; in Bakery it shows the computed grams and the chain
  ("4.20 g ÷ 84.01 g/mol = 0.0500 mol soda → 0.0500 mol cream of tartar × 188.18 g/mol = 9.41 g").
- Keyboard: grams boxes accept typing and Enter; sliders have arrows (0.01 g) and Page keys (1 g).
- `window.__tool = {state, setMode, set(reaction, grams), bake(), day(n), buy(item), seed()}`.

## Look
Accent `--brand #c270bc` (berry jam), `--brand-ink #10141a`. The painted counter sets the warm scene (honey wood,
flour-white marble, morning window light) under a `#1d1714` wash at 60 percent so the bowl and order cards lead. Code
colors: scale numbers in the readout font `#c9f2c0` on the painted display's dark; bubbles outlined `#cfe3f1`. Dots:
soda `#f0c8a0` squares, cream of tartar `#ab5cf2` circles, acetic acid `#ff8a8a` triangles, glucose `#ffd36b`
hexagons, baker's ammonia `#3050f8` diamonds, CO2 `#909090` rings (shape and color both). Text sits on `--panel`
cards, never on the paintings. Contrast (computed): brand on panel 5.22:1, on --sec-bg 4.95:1, brand-ink on brand
5.57:1.

## Art
Local FLUX (`scripts/localart.py`; replaces the old Cloudflare plan), no people anywhere. 14 images. Dots, rows,
readouts, bars, the till count and every label stay in code.
- mb-counter: a cozy small bakery counter in early morning, a honey wood counter top and flour-dusted marble, a
  plain dark green chalkboard on the back wall, an empty glass display case, warm window light, painterly; 16:9;
  cutout no; people no; stage backdrop under a dark wash.
- mb-scale: a small flat digital kitchen scale in brushed steel with a plain blank dark display, on plain white; 4:3;
  cutout yes; people no; on the counter, grams drawn in code over the display.
- mb-bowl: a wide clear glass mixing bowl seen from the side, empty, on plain white; 4:3; cutout yes; people no; the
  bowl; the code dots are drawn behind it and show through the glass.
- mb-oven: a small bakery oven front with a big glass window and a warm orange glow inside, an empty rack; 4:3;
  cutout yes; people no; the bake picture is drawn on the rack inside the window, rising in code during Bake.
- Bakes, one shared line, four cutouts (1:1, cutout yes, people no; each order card's picture and the bake in the
  oven window, scaled from 85 to 100 percent of its height by the rise in code, so a short rise looks flat):
  mb-biscuits: a tray of tall golden buttermilk biscuits. mb-cake: a round golden cake with a domed top on a plate.
  mb-bread: a high round loaf of crusty bread. mb-cookies: a stack of thin crisp golden cookies.
- Pantry, one shared line, five cutouts (3:4, cutout yes, people no; on the pantry shelf, each with its name and
  grams in a code label over a blank painted label): mb-soda: a small plain white cardboard box with a blank front.
  mb-tartar: a small glass spice jar of fine white powder with a steel lid. mb-vinegar: a clear glass bottle of
  vinegar with a blank paper label. mb-glucose: a small paper sack of fine white sugar, folded shut. mb-ammonia: a
  squat glass jar of coarse white crystals with a cork lid.
- mb-coin: a plain round gold coin with a smooth blank face and a ridged edge, on plain white; 1:1; cutout yes;
  people no; the till icon beside the coin count (no celebration animation, 9-12).

## Voice
Bank voice `playful-friend` (Laomedeia), style "Say playfully and cheerfully, like a head baker who loves a good
recipe." No 9-12 science tool and no other spec in this batch uses it. `Curio.voice`, scope = mode.
- wKitchen (how; Test kitchen welcome, R1 ready; stale once Bake is pressed or grams change): "Press Bake to see
  what this batter makes. Then change the grams and bake again."
- wBakery (how; Bakery welcome; stale once grams change or Bake is pressed): "Read the order, set the grams, then
  press Bake. Rise and taste both count."
- limitTip (how; the first time one ingredient runs out first with more than 2 percent of another left; stale on
  the next change): "That one runs out first. It decides how much gas you get."
- day3 (how; Day 3 opens; stale once any order is baked or declined): "No delivery today. Count how many batches six
  grams can make, then bake or decline each order."
- day5 (how; Day 5 opens; stale once the first bake that day): "Careful: baker's ammonia gives three gases for every
  one you weigh."
- paid (event; an order is paid in full; stale on the next bake): "Right rise, clean taste. Paid in full."
- half (event; an order goes at half price; stale on the next bake): "Close. Check the rise and the leftovers, then
  try the next one."

## Family engine
molecules (`kit/molecules.js`), described in full in bond-battle's spec. This tool is family none but calls the
engine: `molarMass`, `parse`, `tally` (for the mass check), the atom colors. It adds SUBSTANCES entries:
KHC4H4O6, KNaC4H4O6, NaC2H3O2, C6H12O6, C2H5OH, NH4HCO3, NH3, Na2CO3. It reuses reaction-kitchen's NaHCO3 and
CH3COOH entries (acetic acid shown here as HC2H3O2, the acid-first form many chemistry texts use).

## Sources
- HS-PS1-7: NGSS Lead States (2013), Next Generation Science Standards, HS-PS1 Matter and Its Interactions, https://www.nextgenscience.org/
- Mole, molar mass, reaction stoichiometry, limiting reactant, percent yield: OpenStax, Chemistry 2e, 3.1 "Formula Mass and the Mole Concept", 4.3 "Reaction Stoichiometry", 4.4 "Reaction Yields", https://openstax.org/books/chemistry-2e/pages/4-4-reaction-yields
- Avogadro constant (exact) and gas constant for the molar volume: NIST CODATA 2018, https://physics.nist.gov/cuu/Constants/
- Molar masses: PubChem compound summaries (sodium bicarbonate CID 516892, potassium bitartrate CID 23681127, acetic acid CID 176, glucose CID 5793, ammonium bicarbonate CID 14013), https://pubchem.ncbi.nlm.nih.gov/ (checked 2026-10-27), matching the molecules engine's sums.
- Sodium bicarbonate decomposes on heating to sodium carbonate, water and carbon dioxide; ammonium bicarbonate decomposes to ammonia, carbon dioxide and water and is used as a leavening agent: PubChem, sodium bicarbonate and ammonium bicarbonate summaries, same URLs.
- Vinegar acidity (labeled as grams of acetic acid per 100 mL, at least 4 percent): U.S. FDA, Compliance Policy Guide Sec. 525.825 "Vinegar, Definitions", https://www.fda.gov/regulatory-information/search-fda-guidance-documents/cpg-sec-525825-vinegar-definitions-adulteration-dilution
- Yeast fermentation of glucose to ethanol and carbon dioxide: OpenStax, Biology 2e, 7.5 "Metabolism without Oxygen", https://openstax.org/books/biology-2e/pages/7-5-metabolism-without-oxygen
- Day answers and the mass check recomputed in Python (2026-10-27).
- Number checks (Python, 2026-10-29, engine masses): all molar masses recomputed (baker's ammonia sums to 79.055, see
  Content); molar gas volume 24.465 L; every Day answer recomputed and matches (Day 1 4.20 g and 9.41 g give 0.0500
  mol, 1,223 mL; Day 2 72.06 g vinegar; Day 4 yield 89.96 percent, shown 90.0; Day 5 2.37 g, and 7.11 g makes 0.270
  mol, three times the target; Day 6 leaves 2.12 g soda). Found and fixed: the Test kitchen mass check said "4.40 g
  left as gas" for the Day 1 batter, which makes 2.20 g of CO2 (4.40 g is the bread's CO2); Day 3 baked one batch at a
  time takes 1.88 g of cream of tartar each (5.64 g for three), not one 5.65 g bake; Day 3 shows four orders, so the
  board holds up to four. Done when 2: 6.00 g soda with 9.41 g cream of tartar leaves 30 percent of the soda, which R5
  turns into 0.0107 mol more CO2 (0.0607 mol in all). Dot count: 100 g of soda is 1,190 dots at 0.001 mol, so the
  0.01 mol dot past 120 is needed.

## Done when
1. Test kitchen opens on R1 at 4.20 g soda and 9.41 g cream of tartar: 0.0500 mol each, gas 0.0500 mol = 2.20 g =
   1,223 mL, taste clean, mass 13.61 g = 13.61 g (2.20 g left as gas).
2. R1 with 6.00 g soda and 9.41 g cream of tartar: cream of tartar runs out first; leftover soda makes 0.0107 mol more
   CO2 by R5 (0.0607 in all) and the taste reads soapy.
3. R2 with 5.04 g soda and 72.06 g vinegar gives 0.0600 mol CO2, clean.
4. Bakery Day 3: entering more than 6.00 g cream of tartar is refused; three batches at 1.88 g and 0.84 g each are
   paid in full; a fourth is refused with 0.36 g left.
5. Day 4 shows 90.0 percent yield; 9.01 g glucose meets 0.090 mol kept.
6. Day 5: 2.37 g baker's ammonia passes; 7.11 g fails the rise (three times the gas).
7. Day 6 leaves 2.12 g soda; the week ledger lists each day's limiting ingredient; progress survives a reload; `New
   week` resets.
8. Focus: in Test kitchen the bowl and the ingredient rows are the largest block at 1366x768 and in the 680x425
   preview; during Bake the oven window is; in Bakery the order board and bowl are.
9. A tap while Bake plays: changing the grams mid-bake drops the bake and updates the bowl in the same frame.
10. How-to lines once each per page load; paid and half each time; no line names a control that is not live.
11. Every size in STANDARDS.md keeps the scale, the ingredient rows and Bake visible; keyboard-only play works; all 14
    images load and none shows a person; console clean, no network, no em dashes.

## Open questions
- The Day 4 yeast yield (90 percent) is a made-up bakery figure, labeled as such on screen. OK, or drop percent yield to keep every number sourced?

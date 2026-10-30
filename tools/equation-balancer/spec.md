# Equation Balancer

## One idea
You may change how many molecules there are, never what they are: tap a subscript and water turns into hydrogen
peroxide, a different substance, so balancing means adding whole molecules until every kind of atom, and with it
every gram, is the same on both sides of the arrow.

## Not like
- equation-golf (gr 9, math): solves algebra equations on a balance beam, scored in strokes against par. Here there is no beam and no unknown x: the "equation" is a chemical change, the only move is a whole-number count of a real substance, and the check is an atom ledger and a mass ledger.
- reaction-kitchen (gr 7, molecules, not specced): runs kitchen reactions and counts atoms before and after. Here the reactions are not run; you find the counts that make them possible, including combustion, precipitation and predicted products.
- mole-bakery (gr 10, same group): uses balanced equations to scale real amounts in grams. Here the equations themselves are the puzzle; grams appear only as proof that mass is conserved.
- half-life-dice (gr 10, same group): balances nuclear equations by mass number and charge. Here atoms never change identity.
- bond-battle (gr 10, same group): builds substances from atoms to compare their properties. Here the substances are given.

## Who and how
- Grade 10, Chemistry, Chemical Reactions and Equations. Students drive. 15 to 35 minutes.
- Topic line: "balancing chemical equations, conservation of mass".
- Standards (module): HS-PS1-2 (predict the outcome of simple reactions from periodic patterns: Predict), HS-PS1-7 (atoms and so mass are conserved, shown with math: the atom and mass ledgers in every mode).
- tool.json: driver "students", minutes "15-35", modes ["Workbench", "Levels", "Predict"], grades_label "Grade 10".

## Screens and modes
Header: title, subtitle "Count molecules, not guesses." Modes `Workbench` (opens first), `Levels`, `Predict`. Kit
buttons.
Stage: the painted slate lab bench (`eb-bench`) under a reactant tray on the left and a product tray on the right,
an arrow between (trays and arrow in code). Each substance is a card: formula in
large type, name under it, and its molecule drawn (molecules engine, ball-and-stick; ionic compounds as a small ion
cluster) once per copy, up to 8 copies, then a badge "× 16". Under each card a coefficient stepper `−` `+` with the
number between them (typing works too, 1 to 30). Below the trays, two ledgers:
- Atom ledger: one row per element: left count as dots in the atom's color with the number, right the same, and a
  word: `matches`, `2 more on the left`, `3 more on the right`.
- Mass ledger: grams on each side for these counts taken as moles (Σ coefficient × molar mass) and the difference
  in grams; `equal` when balanced.
Panel: equation in text with the current coefficients, `Hint`, `Reset`, `Count groups` toggle (counts NO3, SO4, OH
as units in the ledger when they stay whole on both sides), hint line.
Subscripts in every formula are underlined with dots and tappable. Tapping one opens the Formula card (see
Interactions): it shows what that changed formula would be, then puts the real formula back.

Focus (Workbench and Levels): the two trays and the atom ledger under them, together the central and largest block;
the panel and the menu sit to the side. Predict: the product tray and its three choices, with the periodic strip
right above.

### Workbench (explore)
A menu of every equation in Content (all open, grouped by level) plus their names, each with its small story picture
(Art). Change counts freely; the ledgers respond live. No goal shown beyond the ledgers.

### Levels
Five levels of five equations, any order, all open from the start. An equation is done when it is balanced in
lowest whole numbers; then a short card: the balanced equation, "Atoms: 6 = 6. Mass: 36.03 g = 36.03 g", and the
reaction's one-line story from Content beside its painted story picture (`eb-story-*`; Ca(OH)2 + 2 HCl has no story
line, so its card shows the equation only). Done marks saved on this device (localStorage `curio-equation-balancer`,
try/catch), `Clear progress` in the panel.

### Predict
A card list P1 to P10 sits at the side, like the Workbench menu. Reactants are given; products are unknown. A periodic strip above the trays shows groups 1, 2, 13, 16 and 17 with
each group's usual ion charge (+1, +2, +3, −2, −1). Step 1: pick each product formula from three choices made from
those charges (Content). A wrong pick explains with the charges ("Ca forms 2+ ions and Cl forms 1− ions, so it
takes two Cl to cancel"). Step 2: balance as usual. Worked examples (shown solved, marked "example") come first in
each pattern pair, so the class sees a pattern repeat down a group.

## Content
Levels (balanced coefficients in order; story line). All checked by exact null-space solving and mass totals.
- L1 First counts: 2 H2 + O2 → 2 H2O (water from hydrogen fuel); N2 + 3 H2 → 2 NH3 (making ammonia for fertilizer);
  2 Na + Cl2 → 2 NaCl (table salt from a metal and a toxic gas); 2 Mg + O2 → 2 MgO (a magnesium strip burns
  white); 2 H2O2 → 2 H2O + O2 (peroxide fizzing in a cut).
- L2 Odd meets even: 4 Fe + 3 O2 → 2 Fe2O3 (rust, and the heat in a hand warmer); 4 Al + 3 O2 → 2 Al2O3 (the
  thin skin on aluminum); 2 KClO3 → 2 KCl + 3 O2 (oxygen for emergency oxygen generators); CaCO3 → CaO + CO2
  (balanced as written: making lime from limestone); C6H12O6 → 2 C2H5OH + 2 CO2 (yeast making bread rise).
- L3 Groups travel together: AgNO3 + NaCl → AgCl + NaNO3 (a white solid appears); Pb(NO3)2 + 2 KI → PbI2 + 2 KNO3
  (a yellow solid appears); H2SO4 + 2 NaOH → Na2SO4 + 2 H2O (an acid neutralized); Ca(OH)2 + 2 HCl → CaCl2 + 2 H2O;
  2 Al + 3 CuSO4 → Al2(SO4)3 + 3 Cu (copper plates out of the blue solution).
- L4 Burning fuels: CH4 + 2 O2 → CO2 + 2 H2O (natural gas); C3H8 + 5 O2 → 3 CO2 + 4 H2O (a grill tank);
  C2H5OH + 3 O2 → 2 CO2 + 3 H2O (ethanol fuel); C6H12O6 + 6 O2 → 6 CO2 + 6 H2O (respiration in your cells);
  2 C2H6 + 7 O2 → 4 CO2 + 6 H2O (ethane: the first one that needs a doubled start).
- L5 Big ones: 2 C8H18 + 25 O2 → 16 CO2 + 18 H2O (octane in gasoline); 4 NH3 + 5 O2 → 4 NO + 6 H2O (first step
  to nitric acid); Fe2O3 + 3 CO → 2 Fe + 3 CO2 (a blast furnace makes iron); NaHCO3 + HC2H3O2 → NaC2H3O2 + H2O +
  CO2 (baking soda and vinegar, already balanced); Ca3(PO4)2 + 3 H2SO4 → 3 CaSO4 + 2 H3PO4 (phosphate rock made
  into fertilizer acid).
Mass check values (grams per side for the balanced counts, in the order above): 36.03; 34.06; 116.88; 80.61;
68.03; 319.37; 203.92; 245.09; 100.09; 180.16; 228.31; 663.21; 178.07; 147.01; 532.77; 80.04; 204.09; 142.06;
372.14; 284.13; 1,028.41; 228.11; 243.72; 144.06; 604.39. Predict totals: P2 149.10 g, P4 112.15, P5 59.76,
P6 110.98, P7 533.39, P8 82.01, P9 114.23, P10 97.22.

Predict (reactants; choices; product; balanced):
- P1 example: Na + Cl2; NaCl. 2 Na + Cl2 → 2 NaCl. P2: K + Cl2; choices KCl, KCl2, K2Cl; KCl; 2, 1, 2.
- P3 example: Mg + O2; MgO; 2, 1, 2. P4: Ca + O2; CaO, CaO2, Ca2O; CaO; 2, 1, 2.
- P5: Li + O2; LiO, Li2O, LiO2; Li2O; 4, 1, 2. P6: Ca + Cl2; CaCl, CaCl2, Ca2Cl; CaCl2; 1, 1, 1.
- P7: Al + Br2; AlBr, AlBr3, Al3Br; AlBr3; 2, 3, 2.
- P8 example: Na + H2O; NaOH + H2; 2, 2, 2, 1 (sodium in water: a teacher demo behind a shield, said on the card). P9: K + H2O; choices KOH + H2, KH + O2, K2O + H2; KOH + H2; 2, 2, 2, 1.
- P10: Mg + HCl; MgCl2 + H2, MgCl + H2, MgH2 + Cl2; MgCl2 + H2; 1, 2, 1, 1.
Formula card lookups (tap a subscript): H2O → H2O2 "hydrogen peroxide: a different substance, used to bleach and
disinfect"; O2 → O3 "ozone: a different gas"; CO2 → CO "carbon monoxide: a different, poisonous gas"; Fe2O3 → FeO
"iron(II) oxide: a different compound"; H2 → H3, NaCl → NaCl2, MgO → MgO2 "not a stable substance (the charges or
bonds don't work)"; any other change: "That's a different formula, so a different substance (or none). Change the
number in front instead." The card ends `Put it back` (the only button; the formula never stays changed).

## Interactions in detail
- Model: molecules engine `parse`, `tally`, `compare`, `molarMass` (atomic masses from elements-inspector's table).
  Balanced when every element's left count equals its right count. Lowest terms when the gcd of all coefficients
  is 1. Balanced but not lowest: "Balanced. Every number shares a factor of 2: divide them all." (Level not marked
  done.) Many solutions exist only as multiples of one; every Content equation has a one-dimensional solution set
  (checked).
- Coefficients: integers 1 to 30. `−` at 1 and `+` at 30 are disabled with a tip. Zero is refused ("Every substance
  in the equation has to be there at least once").
- Mass ledger: grams for coefficient × molar mass, shown to 2 decimals; difference reported per element in grams
  ("2.02 g of hydrogen more on the left").
- Hint, in order of use on one equation: (1) "Start with the element that is in only one substance on each side."
  (2) "Leave elements that appear alone, like O2, for last." (3) names the next element to fix and which side is
  short. Hints never change counts. `Reset` sets all counts to 1.
- Count groups: allowed only when a group (NO3, SO4, PO4, OH, C2H3O2) appears whole on both sides; otherwise the toggle
  says "This group breaks apart here."
- Drawn copies animate in and out (about 0.3 s, instant with Motion off); the ledger's dots change with a short
  pulse. A tap during an animation acts at once: the counts and ledger already show the new value; the animation
  only catches up.
- Keyboard: steppers are buttons; number boxes accept typing; Tab order: reactant cards, product cards, ledgers.
- `window.__tool = {state, setMode, load(id), set(coefs), ledger(), predict(n, choice)}`.

## Look
Accent `--brand #59c0ab` (bench teal), `--brand-ink #10141a`. The painted slate bench (`eb-bench`, about `#0f171c`)
under code trays `#18232a` at 90 percent; arrow `#c9d3df`; atoms in Jmol CPK colors with symbols printed (same as
bond-battle); ledger dots use the atom colors and each row is labeled with the symbol, so color is never the only
cue. `matches` in `--ok` with a check glyph, mismatches in `--warn` with the number. Story pictures sit in a framed
card with the text on `--panel` below, never on the picture. Contrast (computed): brand on panel 7.87:1, on --sec-bg
7.46:1, brand-ink on brand 8.40:1.

## Art
Local FLUX (`scripts/localart.py`), no people anywhere. 25 images: one bench and 24 story pictures, one per equation
that has a story line in Content. Story pictures: 4:3, cutout no, people no, shown on the done card (Levels) and as
a small thumbnail in the Workbench menu; plain unlabeled surfaces wherever a label would normally be. Molecules,
trays, ledgers and the periodic strip stay in code.
- eb-bench: a dark slate chemistry lab bench top seen from straight above, faint scratches and a soft lamp glow,
  filling the frame; 16:9; cutout no; people no; stage background under both trays.
- L1: eb-story-water: a car tailpipe with clear water droplets falling from it on a cool morning. eb-story-ammonia:
  rows of young green corn plants in dark soil at sunrise. eb-story-salt: a small heap of white table salt crystals
  on dark slate. eb-story-magnesium: a strip of magnesium burning with a blinding white flame, held in steel tongs
  over a lab bench. eb-story-peroxide: white foam fizzing on a cotton pad beside a plain brown bottle.
- L2: eb-story-rust: a rusty iron chain coiled on weathered wood. eb-story-aluminum: crumpled aluminum foil with a
  dull silver sheen. eb-story-oxygen: an emergency oxygen mask with a clear tube dangling from an open airplane
  ceiling panel. eb-story-lime: an old stone lime kiln with piles of white lime powder at its base.
  eb-story-yeast: a glass of warm water topped with a thick tan foam of bubbling yeast.
- L3: eb-story-silver: a test tube of clear liquid with a cloudy white solid settling to the bottom.
  eb-story-lead: a test tube with a bright yellow solid swirling in clear liquid. eb-story-neutral: a glass burette
  dripping into a flask of liquid turning pale pink. eb-story-copper: a strip of aluminum coated in red-brown copper
  standing in a beaker of blue solution.
- L4: eb-story-gas-stove: a ring of blue flame on a gas stove burner in a dark kitchen. eb-story-propane: a white
  propane tank beside a backyard grill on a patio. eb-story-ethanol: a fuel pump nozzle with a yellow handle resting
  in a car's open fuel door. eb-story-respiration: a ripe banana, a granola bar and a water bottle on a gym bench.
  eb-story-ethane: a tall gas flare burning at a refinery at night.
- L5: eb-story-octane: a red metal gasoline can beside a lawn mower on cut grass. eb-story-nitric: a glowing orange
  fine platinum wire mesh, hot, in a dark steel housing. eb-story-blast-furnace: molten iron pouring from a ladle in
  a steel mill, a bright orange stream and sparks. eb-story-soda-vinegar: a glass flask overflowing with white foam
  on a lab bench. eb-story-phosphate: a heap of rough grey phosphate rock at an open mine under a blue sky.

## Voice
Bank voice `casual-peer` (Zubenelgenubi), style "Say casually and naturally, like a friendly teenager explaining a
puzzle." No 9-12 science neighbor uses it, and no other spec in this batch. `Curio.voice`, scope = mode.
- wBench (how; Workbench welcome; stale once an equation is picked or a stepper is used): "Pick an equation from the
  menu. Then tap plus or minus under a substance and watch the atom ledger."
- wLevels (how; Levels welcome; stale once a stepper is used): "Balance each equation in the smallest whole numbers.
  Tap plus or minus under a substance to add molecules."
- wPredict (how; Predict welcome; stale once a card is picked or a choice is tapped): "Pick a card from the list.
  Examples come solved; on the others, tap the product you think forms."
- subTip (how; the first Formula card opens; stale when it closes): "Change the subscript and you change the
  substance. Tap Put it back."
- doubleTip (how; the first time oxygen is short by an odd count with O2 on one side; stale on any count change):
  "Odd oxygen? Tap plus under the fuel to double it first."
- balanced (event; an equation becomes balanced in lowest terms; stale on any count change or equation change):
  "Balanced. Same atoms, same mass, both sides."
- notLowest (event; balanced with a shared factor; stale on any count change): "That balances, but you can divide
  every number down."

## Family engine
molecules (`kit/molecules.js`), described in full in bond-battle's spec. This tool is family none but calls the
engine: `parse` (with parentheses), `tally`, `compare` (atoms and grams), `molarMass`, `draw` (ball-and-stick, and a
small ion cluster for ionic compounds), `ATOMS` colors. It adds SUBSTANCES entries for every formula in Content.

## Sources
- HS-PS1-2, HS-PS1-7: NGSS Lead States (2013), Next Generation Science Standards, HS-PS1 Matter and Its Interactions, https://www.nextgenscience.org/
- Balancing equations, coefficients versus subscripts: OpenStax, Chemistry 2e, 4.1 "Writing and Balancing Chemical Equations", https://openstax.org/books/chemistry-2e/pages/4-1-writing-and-balancing-chemical-equations
- Reaction types (precipitation, acid-base, combustion, single replacement): OpenStax, Chemistry 2e, 4.2 "Classifying Chemical Reactions", https://openstax.org/books/chemistry-2e/pages/4-2-classifying-chemical-reactions
- Group ion charges and periodic patterns: OpenStax, Chemistry 2e, 2.6 "Ionic and Molecular Compounds", https://openstax.org/books/chemistry-2e/pages/2-6-ionic-and-molecular-compounds
- Atomic masses: elements-inspector's ELEMENTS table (Royal Society of Chemistry periodic table, https://periodic-table.rsc.org/), the same values as IUPAC abridged standard atomic weights.
- Hydrogen peroxide, ozone, carbon monoxide identities and uses: PubChem compound summaries for hydrogen peroxide (CID 784), ozone (CID 24823), carbon monoxide (CID 281), https://pubchem.ncbi.nlm.nih.gov/
- Alkali metals with water as a shielded teacher demonstration: American Chemical Society, Guidelines for Chemical Laboratory Safety in Secondary Schools (2016), https://www.acs.org/education/policies/safety.html
- Every coefficient set and mass total recomputed in Python with sympy null-space solving (2026-10-27).
- Number checks (Python with sympy, 2026-10-29, atomic masses from elements-inspector's table): all 25 Level
  equations and all 10 Predict equations solved by exact null space; each has a one-dimensional solution set and
  its lowest whole numbers match Content; the largest coefficient is 25 (octane), under the 30 cap. Mass totals
  recomputed: every one matches except Pb(NO3)2 + 2 KI, 663.212 g, so 663.20 is corrected to 663.21. Predict totals
  added from the same run. Ethane at 4, 14, 8, 12 has gcd 2.

## Done when
1. Workbench, H2 + O2 → H2O at all 1s: ledger says O "1 more on the left"; setting 2, 1, 2 shows `matches` for H and
   O and mass 36.03 g = 36.03 g.
2. Tapping the 2 in H2O shows the hydrogen peroxide card; `Put it back` restores H2O and the counts are unchanged.
3. Ethane at 4, 14, 8, 12 says balanced but divisible by 2 and is not marked done; 2, 7, 4, 6 is marked done and its
   flare picture shows.
4. Octane reaches 2, 25, 16, 18 with 1,028.41 g each side; `+` stops at 30. Pb(NO3)2 + 2 KI shows 663.21 g.
5. Level 3 with Count groups on shows NO3 as a unit for Pb(NO3)2 + KI; for Al + CuSO4 it counts SO4 whole.
6. Predict P6: picking CaCl gives the charge explanation; CaCl2 then balances at 1, 1, 1.
7. Done marks survive a reload; `Clear progress` clears them; `Reset` sets all counts to 1.
8. Focus: in Workbench and Levels the trays and the atom ledger are the largest block on screen at 1366x768 and in
   the 680x425 preview; in Predict the product choices are.
9. A tap while copies animate: five fast taps on `+` give five counts and the ledger matches after each, with no
   tap lost.
10. How-to lines once each per page load; balanced and notLowest each time; no line names a disabled stepper.
11. Every size in STANDARDS.md keeps both trays, all steppers and the atom ledger visible (cards shrink their
    drawings before anything scrolls); keyboard-only play works; all 25 images load and none shows a person;
    console clean, no network, no em dashes.

## Open questions
- HS-PS1-2 is met through ion charges by group (Predict). Fine for this module, or should predicted products also include simple combustion of a new fuel?

# Hand Warmer Lab

## One idea
A reaction gives off heat or soaks it up depending on its bond budget: breaking bonds always costs energy, forming
bonds always pays energy back, and the net decides. Students run that ledger bond by bond, then use the same idea to
design hot packs and cold packs for a winter trail crew.

## Not like
- energy-accountant (gr 10, biology): energy stored, captured as ATP and lost as heat inside living things. Here the energy comes from bonds and attractions in a pack, counted in kJ per mole.
- hot-meets-cold (gr 11, physics): two objects drift to the same temperature. Here the temperature change starts inside the pack, from breaking and forming.
- bond-battle (gr 10, same group): forces between particles decide melting and boiling points. Here bonds inside particles break and form, and the question is how much energy moves.
- gas-law-lab (gr 10, same group): energy pushes a piston. Here energy warms or cools water.

## Who and how
- Grade 10, Chemistry, Thermochemistry. Students drive. 20 to 35 minutes.
- Topic line: "bond energy, exothermic and endothermic change".
- Standards (module): HS-PS1-4 (a model of energy released or absorbed as total bond energy changes: the ledger, the
  energy staircase and the dissolving card).
- tool.json: driver "students", minutes "20-35", modes ["Bond ledger", "Pack bench"], grades_label "Grade 10".

## Screens and modes
Header: title, subtitle "Break costs. Form pays." Modes `Bond ledger` (opens first), `Pack bench`. Kit buttons.

### Bond ledger
Left: the reactants drawn ball-and-stick with every bond clickable. Middle: the energy staircase, a vertical bar
chart that starts at the reactants' level. Right: the ledger table (bond, count, kJ/mol each, total).
1. Pick a reaction (L1 to L6, Content). The products show faded on the right.
2. Click a bond to break it: it snaps apart, its energy is added to "Energy in" and the staircase climbs one step.
   `Break all` does the rest at once.
3. When every reactant bond is broken (loose atoms float in the middle), `Form` becomes active. Click product bonds
   to form them: each adds to "Energy out" and the staircase steps down. `Form all` finishes.
4. The result card: "Energy in 2,656, energy out 3,338, net −682 kJ. More paid back than spent: exothermic." Below it,
   the measured value for comparison and one line on why they differ (Content).
5. `Run it backward` flips the reaction: the same bonds, in and out swapped, net sign flipped ("Splitting water
   costs what making it paid").
The staircase is the HS-PS1-4 model: reactants level, the climb to loose atoms, the drop to products, and the gap
between start and end labeled "net".

### Pack bench
A pouch with an inner bag of 100 g water (20.0 °C) and a cup of salt. A thermometer and a 60-second temperature
graph sit beside it. Panel: salt picker, grams box and slider (0 to 40 g, step 0.01), `Pop` (squeezes the pouch,
breaks the inner bag), `Fresh pack` (resets to 20.0 °C).
- After `Pop` the temperature moves toward its final value over 10 seconds (instant with Motion off); the card shows
  ΔT, final temperature, kJ released or absorbed, and moles of salt.
- `Why` card: dissolving is a small bond budget too. Pulling the ions apart costs energy; water molecules gripping
  the ions pays energy back. For NaCl the two are almost equal (Content), so the change is tiny. The card shows the
  two bars for NaCl and only the net arrow for the other salts (their two halves are not in our sources).
- Trail orders (a list on the right, any order): each card has a target and a pass band of ±1.0 °C. Passing
  checks the card; progress saved on this device (localStorage `curio-hand-warmer-lab`, try/catch), `Clear` resets.
- Iron card: the air-activated warmer, 4 Fe + 3 O2 → 2 Fe2O3, shown on a separate meter in kJ (not a 100 g water
  pouch: it heats slowly as air seeps in). The card compares kJ per gram with the salt packs.

## Content
Bond energies (kJ/mol, average values, OpenStax Table 7.2): H–H 436, Cl–Cl 243, H–Cl 432, O=O 498, H–O 464,
C–H 415, C=O 741, N≡N 946, N–H 390, F–F 160, H–F 569, C≡O 1080, C–O 350.
Ledger reactions (in, out, net; measured from enthalpies of formation, OpenStax Appendix G):
- L1 H2 + Cl2 → 2 HCl: 679, 864, −185. Measured −184.6.
- L2 2 H2 + O2 → 2 H2O (gas): 1,370, 1,856, −486. Measured −483.6.
- L3 CH4 + 2 O2 → CO2 + 2 H2O (gas): 2,656, 3,338, −682. Measured −802.5. Why: table values are averages over
  many molecules; the C=O bonds in carbon dioxide are stronger than the average C=O.
- L4 N2 + 3 H2 → 2 NH3: 2,254, 2,340, −86. Measured −91.8. (The Haber process; equilibrium-seesaw picks it up.)
- L5 H2 + F2 → 2 HF: 596, 1,138, −542. Measured −546.6.
- L6 CO + 2 H2 → CH3OH (gas): 1,952, 2,059, −107. Measured −90.5. (OpenStax Example 7.9 works this one.)
Run backward gives +185, +486, +682, +86, +542, +107.
Formation values used (kJ/mol): HCl −92.3, H2O(g) −241.8, CH4 −74.6, CO2 −393.5, NH3 −45.9, HF −273.3,
CO −110.5, CH3OH(g) −201.0, Fe2O3 −824.2.
Salts (enthalpy of solution, kJ/mol, 25 °C; molar mass g/mol):
CaCl2 −81.3 (110.98); MgSO4 −91.2 (120.36); LiCl −37.0 (42.39); Na2CO3 −26.7 (105.99); NaC2H3O2 −17.3 (82.03);
NH4NO3 +25.7 (80.04); KNO3 +34.9 (101.10); NH4Cl +14.8 (53.49); KCl +17.2 (74.55); NaCl +3.9 (58.44).
Pack model: q = −ΔH × moles; the heat warms (or cools) the whole solution, water plus salt, at 4.18 J/g °C, with no
loss to the air (said in the help: real pouches leak heat, so real packs fall short).
ΔT for 10 / 20 / 30 g (computed): CaCl2 +15.93 / +29.21 / +40.44; MgSO4 +16.48 / +30.21 / +41.83; LiCl +18.98 /
+34.80 / +48.19; Na2CO3 +5.48 / +10.04 / +13.91; NaC2H3O2 +4.59 / +8.41 / +11.64; NH4NO3 −6.98 / −12.80 / −17.73;
KNO3 −7.51 / −13.76 / −19.06; NH4Cl −6.02 / −11.03 / −15.28; KCl −5.02 / −9.20 / −12.74; NaCl −1.45 / −2.66 / −3.68.
NaCl why card: about 769 kJ to pull a mole of NaCl apart (lattice energy, OpenStax 7.5), about 765 back when water
grips the ions, net +3.9.
Trail orders:
- T1 Mitten pack: +22 °C. CaCl2 14.35 g, or MgSO4 13.81 g.
- T2 Ankle ice pack: −15 °C. NH4NO3 24.27 g, KNO3 22.20 g, or NH4Cl 29.30 g.
- T3 "Table salt cold pack?": reach −5 °C with NaCl. It cannot (−3.68 °C at 30 g, −4.56 °C at the 40 g limit); the
  card passes when the student marks it `Can't be done` after trying at least two amounts.
- T4 Pocket heater: 0.50 kJ per gram of pack is the bar. CaCl2 gives about 0.73 kJ per gram of salt, but the pouch
  must carry its water too: 14.35 g in 114.35 g of pack is 0.092 kJ/g. Iron: 7.38 kJ per gram of iron. The card
  passes when the student picks iron and says why (choice of three reasons, one right: "more energy per gram").
Iron warmer: 4 Fe + 3 O2 → 2 Fe2O3, −1,648.4 kJ for 223.38 g of iron: 7.38 kJ/g. 10 g iron 73.8 kJ; 10 g CaCl2
7.33 kJ. Real air-activated warmers hold iron powder, salt, activated carbon and vermiculite; the salt and carbon
help the iron rust faster, and the vermiculite holds water.
Safety line (help, and Pack bench footer): "This is a virtual lab. Real hand-warmer experiments follow your school's
lab safety rules: goggles, no tasting, and your teacher's say-so for every chemical." Sodium hydroxide is left out on
purpose (caustic).

## Interactions in detail
- The ledger accepts breaks in any order; `Form` is locked until every reactant bond is broken (the help says why:
  the model goes through loose atoms). Undo steps back one click.
- Net = in − out, exactly from the table. Positive net: endothermic; negative: exothermic; the words appear only
  after the last bond forms.
- Pack math: n = g ÷ M; q = −ΔH × n (kJ); ΔT = q × 1000 ÷ ((100 + g) × 4.18). Shown to 2 decimals.
- Pass check: |ΔT − target| ≤ 1.0 °C. A wrong pack is not a fail: the card says "Off by 3.4 °C. Fresh pack and
  try again."
- Keyboard: bonds are buttons in reading order (Tab, Enter); sliders arrows 0.01 g and Page 1 g.
- `window.__tool = {state, setMode, reaction(id), breakAll(), formAll(), backward(), pack(salt, g), pop(), order(id)}`.

## Look
Accent `--brand #d28279` (ember clay), `--brand-ink #10141a`. Scene: dusk snow trail drawn in code (`#1a2230` sky,
`#d8e2ee` snow at 30 percent). Warming uses the accent; cooling uses `#8fd3ff`; the graph line changes color as it
crosses 20 °C. Staircase: climb bars `#8fd3ff` (energy in), drop bars accent (energy out), net bracket in `--ink`.
Atoms in molecules-engine colors. Contrast (computed): brand on panel 5.94:1, on --sec-bg 5.63:1, brand-ink on
brand 6.34:1.

## Art
None. Pouch, thermometer, trail and molecules are drawn in code.

## Voice
Bank voice `news-reader` (the trail crew's steady radio bulletin). No 9-12 science tool uses it. `Curio.voice`,
scope = mode.
- wLedger (how, Bond ledger welcome): "Click each bond on the left to break it. When they're all loose, press Form."
- formTip (how, first time all bonds are broken): "Everything's loose. Now click the product bonds to form them."
- wBench (how, Pack bench welcome): "Pick a salt, set the grams, then press Pop to break the inner bag."
- coldTip (how, first endothermic result): "It got colder. Pulling apart cost more than the water paid back."
- hit (event, an order passes; stale on the next Pop): "That pack will do the job on the trail."
- t3Tip (how, second NaCl try on T3): "If no amount gets there, press Can't be done."

## Family engine
molecules (`kit/molecules.js`), described in full in bond-battle's spec. Family none here; it calls `draw` with
clickable bonds (asks for an `onBond(i, j)` option and a `broken` set so a bond can be drawn apart), `SUBSTANCES`
for H2, Cl2, O2, N2, F2, H2O, HCl, NH3, HF, CH4, CO2, and adds CO and CH3OH entries. Bond energies live in this tool
(a `BOND_ENERGY` table keyed "C=O" and so on), not in the engine.

## Sources
- HS-PS1-4: NGSS Lead States (2013), Next Generation Science Standards, https://www.nextgenscience.org/
- Bond energies (Table 7.2), lattice energy of NaCl, Example 7.9: OpenStax, Chemistry 2e, 7.5 "Strengths of Ionic and Covalent Bonds", https://openstax.org/books/chemistry-2e/pages/7-5-strengths-of-ionic-and-covalent-bonds
- Enthalpies of formation: OpenStax, Chemistry 2e, Appendix G "Standard Thermodynamic Properties for Selected Substances", https://openstax.org/books/chemistry-2e/pages/g-standard-thermodynamic-properties-for-selected-substances (builder re-checks each value).
- Enthalpies of solution, and CaCl2 hot packs, NH4NO3 cold packs: LibreTexts, "General Chemistry: An Atoms First Approach" (Howard University), 9.5 "Enthalpies of Solution", Table 9.5.1 (checked 2026-10-27), https://chem.libretexts.org/
- Air-activated warmer contents: LibreTexts (Duke University), "Thermochemistry of Hand Warmers in Everyday Life" (checked 2026-10-27), https://chem.libretexts.org/
- Specific heat of water 4.18 J/g °C: OpenStax, Chemistry 2e, 5.1 "Energy Basics", Table 5.1.
- Molar masses: the molecules engine (RSC masses), checked against PubChem.
- School lab safety: American Chemical Society, Guidelines for Chemical Laboratory Safety in Secondary Schools (2016), https://www.acs.org/
- Every ΔT, gram target and ledger total recomputed in Python (2026-10-27).

## Done when
1. L3 with every bond broken and formed shows in 2,656, out 3,338, net −682 and measured −802.5 with the why line.
2. `Form` stays locked until the last reactant bond breaks; Undo steps back one bond.
3. `Run it backward` on L2 shows +486 and the word endothermic.
4. Pack bench: 10 g CaCl2 reads +15.93 °C and 7.33 kJ; 30 g NH4NO3 reads −17.73 °C.
5. T1 passes with 14.35 g CaCl2; T2 passes with 24.27 g NH4NO3; T3 passes only through `Can't be done` after two tries; T4 passes on iron.
6. The NaCl why card shows 769 in, 765 back, +3.9 net; other salts show only a net arrow.
7. Progress survives a reload; `Clear` resets; Motion off makes the thermometer jump to its final value.
8. Every size in STANDARDS.md keeps the staircase or the pouch, the ledger or the panel, and the action button visible; keyboard-only works; console clean, no network.

## Open questions
- HS-PS1-4 asks about reactions; dissolving salts is a physical change. Is the Pack bench's "dissolving is a small bond budget too" framing OK, with the iron warmer as the true reaction?
- T4's 0.50 kJ per gram bar is a made-up design target (labeled as such). Keep, or ask only "which gives more energy per gram"?

# Bond Battle

## One idea
Every substance you build from atom cards carries its own boiling point, and the battle is a rising thermometer:
both players reveal a substance, the heat climbs, and the first one to boil away loses, so you learn to read the
forces between particles (a salt's ion lattice beats water's hydrogen bonds, which beat methane's weak pull, and
heavy carbon tetrachloride with no polarity at all still outlasts methanol).

## Not like
- molecule-builder (gr 7, molecules, not specced): snaps atoms into stable molecules. Same engine; here the point is what holds separate particles together, not the molecule itself.
- reaction-kitchen (gr 7, molecules, not specced): counts atoms before and after a reaction. Same engine; no reactions here.
- elements-inspector (gr 10, live): explores one element's atom. Here two or more elements bond, and the bond type comes from their electronegativity gap.
- equation-balancer (gr 10, same group): balances reactions with molecule counts. Here no reactions; structure decides properties.
- hot-meets-cold (gr 11): heat flowing between objects. Here heat is only the referee that tests the forces.
- correlation-guessing-game (gr 9, math) and other card or guessing games: the cards here are real atoms and real data; the winner is decided by measured boiling points, not chance.

## Who and how
- Grade 10, Chemistry, Bonding and Intermolecular Forces. Students drive; Battle is one laptop for two players or one player against the Rival. 15 to 35 minutes.
- Topic line: "ionic and covalent bonds, intermolecular forces".
- Standards (module): HS-PS1-3 (bulk properties such as boiling point infer the strength of forces between particles: Bench and Battle), HS-PS2-6 (molecular structure matters for designed materials: Jobs).
- tool.json: driver "students", minutes "15-35", modes ["Bench", "Battle", "Jobs"], grades_label "Grade 10".

## Screens and modes
Header: title, subtitle "The last one still liquid wins." Modes `Bench` (opens first), `Battle`, `Jobs`. Kit buttons
`Motion`, `Sound`, `Read`.
Stage (all modes): left, the workbench where atom cards and built substances sit; right, the heat column: a tall
thermometer from −273 °C to 4,000 °C on a piecewise scale (−273 to 0, 0 to 200, 200 to 4,000 each get a third of
the height, scale breaks marked with a zigzag). Panel: substance card, bond meter, forces ladder, hint.

### Bench (explore)
Atom palette (10 cards, Content). Tap a card to add an atom to the workbench (drag also works). The molecules
engine joins atoms by their usual bonds and ion charges. When the atoms on the bench match a substance in the
recipe book, it snaps together: ball-and-stick drawing (or an ion lattice tile for ionic, a network tile for
SiO2), its name and formula. Panel shows:
- Bond meter: each kind of bond in it as a mark on a 0 to 3.2 electronegativity-gap bar with the 0.4 and 1.8 lines,
  labeled `nonpolar covalent`, `polar covalent`, `ionic`, and the gap value ("O–H: 3.44 − 2.20 = 1.24").
- Shape and polarity: bond dipole arrows on the drawing; a word `polar molecule` or `nonpolar molecule` (CO2 and
  CCl4 have polar bonds but cancel; the tip says so the first time).
- Forces ladder: London, dipole-dipole, hydrogen bonding, ion lattice, covalent network; the ones present light
  up, the strongest is boxed.
- Melting and boiling point marked on the heat column.
`Pin` puts the substance on the compare shelf (up to 4). The heat slider (`Heat`, −273 to 4,000 °C, keyboard
step 1 °C, Page keys 50) sets one temperature for the whole shelf; each pinned card shows a small particle window
(solid lattice, liquid cluster, gas spread, from the particles engine's look) for its state at that temperature.
`Clear bench`, `Unpin`. An atom that cannot join (a fifth atom on a full molecule) waits beside it with "no free
bond".

### Battle
Two seats: `You` and `Rival` (computer), or `Player 2` (toggle `Two players`, hands hidden by a `Pass the laptop`
screen between turns). Each seat holds 7 atom cards from the 36-card deck. Round:
1. Build: tap cards from your hand into the build tray until they make a recipe-book substance; `Lock in` places
   it face down. `Swap 2` instead discards two cards and draws two (you sit the round out, the other side wins it
   if they built).
2. Heat: both cards flip; the heat column climbs (about 3 s, instant with Motion off). Each substance's marker
   rises with it; at its boiling point (or sublimation point) its particle window turns to gas and the card
   greys with `boiled at −161.5 °C`. The other wins the round.
3. Why card: one sentence from Content naming the force that decided it, with both boiling points.
Hands refill to 7. First to 5 rounds wins the match; `New match`. Same substance on both sides is a tie, no point.
Ionic substances need their charges to add to zero (Mg with two Cl). Rival: builds the highest boiling substance
it can 70 percent of the time, otherwise a random valid one (seeded per match).

### Jobs
Five job cards (Content). Open one, read the spec, pick any recipe-book substance from the book (all unlocked
here), `Try it`. The card answers with the property check against the spec (pass or fail in words, with the
number) and, when it passes, the structure reason and the real use with its source. Some jobs accept two.
Finished jobs get a stamp, saved on this device (localStorage `curio-bond-battle`, try/catch) with `Clear jobs`.

## Content
Atom cards (symbol, name, usual bonds or ion charge, Pauling electronegativity): H hydrogen 1, 2.20; C carbon 4,
2.55; N nitrogen 3, 3.04; O oxygen 2, 3.44; F fluorine 1, 3.98; Cl chlorine 1, 3.16; Si silicon 4, 1.90;
Na sodium ion +1, 0.93; K potassium ion +1, 0.82; Mg magnesium ion +2, 1.31. Battle deck (36): H 10, C 4, N 3,
O 5, F 2, Cl 4, Na 3, K 2, Mg 2, Si 1.

Recipe book (formula, name, kind, strongest force, melting point, boiling point in °C at 1 atm):
- H2 hydrogen, nonpolar molecule, London, −259.2, −252.9
- N2 nitrogen, nonpolar, London, −210.0, −195.8
- O2 oxygen, nonpolar, London, −218.8, −183.0
- F2 fluorine, nonpolar, London, −219.6, −188.1
- Cl2 chlorine, nonpolar, London, −101.5, −34.0
- CH4 methane, nonpolar (C–H gap 0.35), London, −182.5, −161.5
- HCl hydrogen chloride, polar, dipole-dipole, −114.2, −85.1
- CO2 carbon dioxide, polar bonds, nonpolar linear molecule, London, sublimes at −78.5 (no liquid at 1 atm)
- NH3 ammonia, polar, hydrogen bonding, −77.7, −33.3
- HF hydrogen fluoride, polar (gap 1.78, just under the ionic line), hydrogen bonding, −83.4, 19.5
- CH3OH methanol, polar, hydrogen bonding, −97.6, 64.7
- CCl4 carbon tetrachloride, polar bonds, nonpolar tetrahedral, London (large electron cloud), −22.9, 76.7
- H2O water, polar bent, hydrogen bonding, 0.0, 100.0
- MgCl2 magnesium chloride, ionic (gap 1.85), ion lattice, 714, 1,412
- KCl potassium chloride, ionic (2.34), ion lattice, 771, 1,420
- NaCl sodium chloride, ionic (2.23), ion lattice, 801, 1,465
- NaF sodium fluoride, ionic (3.05), ion lattice, 996, 1,704
- SiO2 silicon dioxide (quartz), polar covalent network (1.54), covalent network, 1,713, 2,950
- MgO magnesium oxide, ionic (2.13), ion lattice (2+ and 2− ions), 2,825, 3,600
The builder checks every melting and boiling point against PubChem (Experimental Properties) or the CRC Handbook
and keeps the source value where they differ by more than 1 °C, noting it in the tool's notes (KCl, MgCl2 and SiO2
boiling points vary most between sources).

Why cards (Battle, chosen by the pair's strongest forces; the tool fills in names and numbers):
- ion lattice vs molecule: "{A} is a lattice of ions held by charge on every side; {B}'s molecules only cling to their neighbors."
- H-bond vs London or dipole: "{A}'s molecules hydrogen bond (H on N, O or F), so they hold on until {bpA}."
- both London: "Both have only London forces. {A}'s electron cloud is easier to pull out of shape, so its molecules cling harder." (Not "more electrons": CH4 with 10 outlasts N2 with 14, and O2 outlasts F2.)
- London beats H-bond (CCl4 vs CH3OH): "No polarity at all, but 74 electrons per molecule against 18. Size can beat a hydrogen bond."
- both hydrogen bond: "Both hydrogen bond. {A} makes more of them per molecule, or stronger ones, so it holds on until {bpA}." (Water has two H and two lone pairs to bond with; that is why it beats HF.)
- both ionic: "Both are ion lattices. Ion size and charge set how tight the lattice is, and {A}'s is tighter."
- MgO vs another ionic or SiO2: "Mg2+ and O2− carry double charges, so the lattice holds far tighter."
The card is chosen by the winner's strongest force against the loser's, with the specific cards (CCl4 vs CH3OH,
MgO, SiO2 winning, CO2 losing) taking priority.
- SiO2: "Quartz is one giant molecule: boiling it means breaking covalent bonds, not just pulling molecules apart."
- CO2: "Carbon dioxide skips the liquid at normal pressure: its weak forces let go at −78.5 °C."

Jobs (spec; accepted; answer):
1. Road de-icer: a solid that dissolves into ions in meltwater. Accept NaCl, MgCl2. "Ions spread through the water
   and get in the way of freezing. Highway deicing is the largest single use of salt in the United States (USGS)."
2. Furnace brick: stays solid at 1,500 °C. Accept MgO, SiO2. "Strong lattice or network bonds. Magnesia and silica
   are both made into refractory bricks (USGS)."
3. Ice rink chiller: a liquid that boils between −40 and 0 °C so it soaks up heat as it evaporates. Accept NH3.
   Cl2 fits the number and gets: "It boils at −34.0 °C, but chlorine is toxic and attacks metal. Numbers aren't the
   only spec." "Ammonia is used as an industrial refrigerant (OSHA)."
4. Rocket fuel tank at −253 °C: a fuel that is liquid there. Accept H2. "Only tiny London forces, so hydrogen is a
   liquid only near −253 °C. NASA's large rockets have used liquid hydrogen fuel."
5. Window glass: clear, hard, melts only far above an oven. Accept SiO2. "Glass is mostly silica: a covalent
   network, so no small molecules to pull apart."

## Interactions in detail
- Bond type: gap = |EN a − EN b|, below 0.4 nonpolar covalent, 0.4 to 1.8 polar covalent, above 1.8 ionic
  (shown as a general guide with exceptions, per the source). HF (1.78) sits just left of the ionic line.
- Valid builds come only from the recipe book; the engine matches atom counts (Hill formula), and an ionic build
  must have charge sum zero. Building an unlisted but valid molecule (H2O2, C2H6) in Bench says "That's a real
  molecule, but it isn't in this book yet" and does not snap.
- Heat column: the substance boils when the dial passes bp (sublimes for CO2); with Motion off the dial jumps to
  the loser's bp, then to the winner's.
- Rival seeded with `Math.random` once per match; `__tool.seed(n)` fixes it for tests.
- Battle keeps no score between page loads. Reset: `New match`.
- Keyboard: atom cards and hand cards are buttons; Enter adds; the heat slider has arrow and Page keys.
- `window.__tool = {state, setMode, build(syms), pin(id), heat(t), battle({you, rival}), job(n, formula), seed(n)}`.

## Look
Accent `--brand #ecf994` (pale lime), `--brand-ink #10141a`. Card table `#13241c` felt with cards `#f4f1e6` and dark
ink `#14110a` (16.9:1). Atom spheres in Jmol CPK colors with the symbol printed on each (H `#ffffff`, C `#909090`,
N `#3050f8`, O `#ff0d0d`, F `#90e050`, Cl `#1ff01f`, Si `#f0c8a0`, Na `#ab5cf2`, K `#8f40d4`, Mg `#8aff00`), dark
outline so white H shows on the light card. Heat column gradient blue to red with tick labels in `--ink`.
Contrast (computed): brand on panel 15.29:1, on --sec-bg 14.48:1, brand-ink on brand 16.31:1. Kind of force is
shown by name and icon, not color alone.

## Art
none: drawn in code (cards, atoms, lattices, heat column, card back pattern, preview.svg).

## Voice
Bank voice `hero-coach` (bright, encouraging coach). No 9-12 science neighbor uses it. `Curio.voice`, scope = mode.
- wBench (how, Bench welcome): "Tap atom cards to build a substance. Then pin it and slide the heat."
- wBattle (how, Battle welcome): "Tap cards from your hand to build a substance. Then press Lock in."
- pinTip (how, first substance built): "Press Pin to keep it on the shelf. Pin a few, then slide Heat."
- cancelTip (how, first CO2 or CCl4 built): "Polar bonds, but they point opposite ways and cancel. The molecule is nonpolar."
- wJobs (how, Jobs welcome): "Open a job card. Pick a substance from the book, then press Try it."
- roundWin (event, you win a round; stale when the next round starts): "Yours held on longer. Read why on the card."
- roundLose (event, you lose a round; stale when the next round starts): "Boiled first. Check which force the winner had."
- jobDone (event, a job passes; stale on job change): "That fits the job. Structure did the work."

## Family engine
molecules (`kit/molecules.js`, inlined after `kit:curio`). No family doc exists; this spec holds the full engine
description and the build writes `docs/families/molecules.md` from it. Siblings: molecule-builder (gr 7, sandbox),
reaction-kitchen (gr 7, lab). equation-balancer and mole-bakery (gr 10, family none) also call it (see their specs).
- `ATOMS`: per element `{sym, name, z, mass, en, bonds | charge, cpk, r}`. `mass` comes from elements-inspector's
  ELEMENTS table (same source, RSC); `en` Pauling (PubChem); `cpk` Jmol colors; `r` drawing radius.
- `parse(formula)` → `{El: count}`, handles parentheses and hydrates written with a dot ("Pb(NO3)2",
  "CuSO4·5H2O"); `hill(counts)` → formula text; `molarMass(formula)` → g/mol from ATOMS masses (sum of
  counts × mass, shown to 2 decimals).
- `tally(side)` where side is `[{formula, coef}]` → `{El: atoms}`; `compare(left, right)` →
  `{balanced, perElement: [{el, left, right}], massLeft, massRight}`.
- `bondType(a, b)` → `{gap, type: 'nonpolar' | 'polar' | 'ionic'}` with the 0.4 and 1.8 lines.
- `SUBSTANCES`: the shared recipe book `{id, formula, name, kind: 'molecule' | 'ionic' | 'network' | 'element',
  atoms: [{sym, x, y}], bonds: [[i, j, order]], polar, imf: [...], mp, bp, sublimes, src}`. Each tool may add
  entries (molecule-builder: O3, H2O2; reaction-kitchen: NaHCO3, CH3COOH, Fe2O3).
- `match(atomList)` → a substance or `{open: true, freeBonds}` (used for the snap and "no free bond").
- `draw(group, substance, {x, y, scale, style: 'ball-stick' | 'space-fill', labels: true, dipoles})` (SVG);
  `lattice(group, ionicSubstance, {cols, rows})`; `network(group, 'SiO2')`.
- `stateAt(substance, tC)` → 'solid' | 'liquid' | 'gas'.
- What each sibling feeds it: molecule-builder: free building with a stability check (every atom's bonds full),
  no ions. reaction-kitchen: `tally` before and after with masses for kitchen reactions. This tool: bond types,
  polarity, forces and states.

## Sources
- HS-PS1-3, HS-PS2-6: NGSS Lead States (2013), Next Generation Science Standards, HS-PS1 Matter and Its Interactions and HS-PS2 Motion and Stability, https://www.nextgenscience.org/
- Electronegativity difference bands (below 0.4, 0.4 to 1.8, above 1.8, "a general guide"): OpenStax, Chemistry 2e, 7.2 "Covalent Bonding", Figure 7.8, https://openstax.org/books/chemistry-2e/pages/7-2-covalent-bonding
- Pauling electronegativities: PubChem Periodic Table of Elements, property "Electronegativity", https://pubchem.ncbi.nlm.nih.gov/periodic-table/ (checked 2026-10-27)
- Intermolecular forces (London, dipole-dipole, hydrogen bonding; size and boiling point): OpenStax, Chemistry 2e, 10.1 "Intermolecular Forces", https://openstax.org/books/chemistry-2e/pages/10-1-intermolecular-forces
- Melting and boiling points: PubChem compound pages (Experimental Properties), https://pubchem.ncbi.nlm.nih.gov/, and CRC Handbook of Chemistry and Physics, 97th ed. (2016), Physical Constants of Inorganic and Organic Compounds. Values as listed in Content, to be rechecked at build.
- Salt for highway deicing and magnesia and silica refractories: USGS, Mineral Commodity Summaries 2025, "Salt", "Magnesium Compounds" and "Silica", https://www.usgs.gov/centers/national-minerals-information-center/mineral-commodity-summaries
- Ammonia refrigeration: OSHA, "Ammonia Refrigeration" eTool, https://www.osha.gov/etools/ammonia-refrigeration
- Liquid hydrogen as rocket fuel: NASA, "Liquid Hydrogen: the Fuel of Choice for Space Exploration", https://www.nasa.gov/ (search title)
- Glass is mostly silica (industrial sand is the main raw material of glassmaking): USGS, Mineral Commodity Summaries 2025, "Sand and Gravel (Industrial)", same URL as above
- Electron counts in the why card: CCl4 6 + 4 × 17 = 74; CH3OH 6 + 8 + 4 × 1 = 18 (atomic numbers).
- Jmol CPK colors: Jmol, "Jmol Colors", https://jmol.sourceforge.net/jscolors/
- Gaps recomputed (2026-10-27): HF 1.78, NaCl 2.23, KCl 2.34, NaF 3.05, MgO 2.13, MgCl2 1.85, Si–O 1.54, C=O 0.89, C–Cl 0.61, N–H 0.84, O–H 1.24, H–Cl 0.96, C–H 0.35.

## Done when
1. Bench: H, H, O snaps into water; the bond meter shows O–H at 1.24 (polar covalent); hydrogen bonding is boxed; bp 100.0 on the column.
2. Na and Cl make NaCl (ionic, 2.23); Mg with one Cl waits with "no free bond" style message until a second Cl joins (MgCl2).
3. CO2 and CCl4 show polar bonds but the word "nonpolar molecule", and the cancel tip plays once.
4. Pin CH4, NH3, H2O, NaCl; Heat at 20 °C shows gas, gas, liquid, solid.
5. Battle: CCl4 vs CH3OH: methanol boils at 64.7 °C first and the size why card appears. HF vs HCl: HCl boils at −85.1 °C.
6. An ionic build with unbalanced charge (Mg + Cl) cannot Lock in; `Swap 2` hands the round to a side that built.
7. Jobs: Cl2 on the chiller gets the "numbers aren't the only spec" answer; NH3 passes; stamps survive a reload; `Clear jobs` clears.
8. Every size in STANDARDS.md keeps the hand, the build tray, `Lock in` and the heat column visible; keyboard-only play works; console clean, no network.

## Open questions
- Boiling points of KCl, MgCl2 and SiO2 differ between sources (some list decomposition or sublimation). OK to use PubChem's value at build and note it?
- molecules engine: equation-balancer and mole-bakery (family none) use kit/molecules.js too. Add them to the molecules family, or keep them as outside users of the engine?

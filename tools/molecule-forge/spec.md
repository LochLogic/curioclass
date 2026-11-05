# Molecule Forge (Curiosity No. 12)

Tool id stays `molecule-forge`. Plate: `Curio Class Curiosities · No. 12 · Molecule Forge`. Build brief:
docs/agents/CODEX-CURIOSITY.md. In `tool.draft.json`: `"curiosity": true`, `"plate": 12`.

## The real thing
A chemist's model kit and molecular viewer in one. Each atom is a ball with its real number of bonding spots, drilled
at its real angles, and one rule does everything: a bond fills one spot on each atom. Fill every spot and a molecule
closes and settles into its measured shape (water bends to 104.5 degrees). Repeat a pattern instead and it never closes:
diamond, salt, copper and sand grow, and a push or a battery shows how the way their atoms are held decides whether
they crack, bend or carry current. A field guide names what you built; it is a reference, never a checklist.

## Map
- Anchor: science-7-atoms-and-molecules (MS-PS1-1, models of simple molecules and extended structures).
- Also reaches: science-10-bonding-and-intermolecular-forces (HS-PS2-6: structure decides how a material behaves),
  science-10-atomic-structure-and-the-periodic-table (HS-PS1-1: outer electrons set the bonding spots).
- Grade band 6 to 10. It takes over the Molecule Builder card (tools/molecule-builder/idea.md). A teacher plan would
  teach MS-PS1-1 fully (simple molecules in three representations, extended structures from a repeated pattern), so
  with a plan.md it takes the anchor's lesson card.

## The first two minutes
- 0 s: a dark viewing well; one red oxygen ball turns slowly with two glowing pegs that wobble and hum. The kit tray
  of nine atoms runs down the left. Hint on the rim: "Tap an atom to snap it on."
- 3 to 6 s: two taps on hydrogen. Click, click: the pegs vanish, the molecule bends to its real angle, a thin cyan ring
  pulses out, and the strip prints `H2O · water · 3 atoms · H-O-H about 104°`. The guide tab lights with "Water".
- 10 to 30 s: another hydrogen lands alone (water has no spots left); one more and they snap into H2. Spots fill, then
  it stops, and nobody said so.
- 30 to 120 s: carbon and four hydrogens close methane; drag to turn it; flip to `Spheres`; slide the bench switch to
  `Crystal`, drop one carbon on the seed plate, press `Grow`, and a diamond builds itself shell by shell.

## Things to do
1. Build water, ammonia and methane and read the angle shrink as lone pairs crowd in: about 109, 106, 104 degrees.
2. Tap a bond to make it double or triple: O2, N2, and CO2 dead straight at 180 degrees.
3. Build ethanol and dimethyl ether from the same nine atoms and read two different pages (78 °C against -24.8 °C).
4. Close a ring: benzene, with its double bonds placed either of the two ways; the guide names both.
5. Open caffeine in the field guide, turn its model, and build it atom by atom (24 atoms).
6. Invent: close a structure the guide does not know (H2N-NH-NH2) and keep it on the shelf.
7. Try O=Si=O and read why silicon refuses it in nature; then grow silica in Crystal.
8. Grow diamond from carbon and graphite from a carbon double bond: same atom, two materials.
9. Push salt and it cracks along a flat face; push copper and it bends; push diamond and count the bonds that hold.
10. Clip the battery to all seven crystals: a sea of electrons, a little current, or none.
11. Cut a crystal open and tap an atom inside to count its neighbours: 4, 3, 6, 12 or 8.
12. Compare `Sticks` and `Spheres`, then `Show` a model on the turntable; or just read the guide like a book.

## Controls
- Bench switch `Forge` / `Crystal` (T). Kit tray: H C N O S Cl Si Na Cu (keys 1 to 9; tap adds, drag drops on a peg
  or on empty well for a new structure). Bond tap steps single, double, triple, single as spots allow; H, Cl never step.
- Tab cycles atoms, Enter selects; the selected atom's bond buttons step orders (keyboard path); Delete melts it.
- View: drag or arrow keys rotate (15° per press); wheel, pinch or + / - zoom 50 to 300 percent; `Center` (0);
  `Sticks` / `Spheres` toggle (V); `Show` turntable, 12°/s, Motion off: still with 30° step buttons (H).
- `Undo` (Ctrl+Z, 30 steps), `Clear` (the well), `Save` (to the shelf, up to 12; Ctrl+S).
- Crystal: seed plate (at most 2 atoms; tap the bond between them to step it), `Grow` (G), `Clear seed`, `Push` (P),
  `Current` (E), `Cut open` toggle (X). Any tap or key during growth, Push or Current completes it the same frame.
- Field guide (B): index by name and formula, `Turn`, `Load` into the well. Manual (M). Power panel: Motion, Sound, Read.

## Readouts
A monospace strip along the bottom of the well, live. Formula in Hill order with subscripts (`C8H10N4O2`); atoms
`24 / 40`; `2 SPOTS OPEN` or `ALL SPOTS FULL`; the name when the guide knows it, else `NOT IN THIS GUIDE`. Selected atom:
`O · 2 spots · 2 filled · 2 lone pairs`, the angle at it in whole degrees with "about", each bond's order and drawn
length in pm (sum of covalent radii, x 0.87 double, x 0.78 triple). Crystal: `525 ATOMS · 87 INSIDE`, the pattern,
neighbour count on tap, a test's result line. Budgets: "The well holds 40 atoms."; "A salt grain 1 mm across holds
about 4.5 x 10^19 ions."

## The Manual
A drawer, lower-left. Contents: the spots rule; shapes from groups and lone pairs; how matching works; Sticks and
Spheres; the growth rules; what Push and Current show; honesty notes; sources. Things people have found:
1. Lone pairs squeeze the bond angle: methane 109.5, ammonia about 107, water 104.5 degrees (OpenStax Chem 2e 7.6).
2. Ethanol and dimethyl ether share their atoms: one boils at 78 °C, the other at -24.8 °C (PubChem 702, 8254).
3. Benzene's double bonds can sit two ways and it is still one molecule; vanillin and aspirin too (checks).
4. Of the 92 legal structures made from 1 to 3 of C, N and O filled with hydrogen, 56 have no name in this guide (checks).
5. Diamond and graphite are both carbon; graphite's sheets have no bonds between them, so a pencil writes (OpenStax 10.6).
6. Salt cracks when a push brings like charges face to face; copper's atoms roll to new neighbours and it bends (checks).
7. CO2 is a small molecule and SiO2 a giant one, though carbon and silicon share a column (OpenStax 18.3).
8. Silicon carries a little current, more when warm: a semiconductor (OpenStax 18.3).
9. In 1828 Friedrich Wöhler made urea from non-living chemicals (Wöhler 1828).

## Look
The grammar of a molecular modelling bench: a dark viewing well `#0f1218` with a faint radial glow, the kit tray as a
wooden model-kit box whose balls show their drilled holes (the pegs), Jmol CPK colours for atoms (shaded sprites; white
H outlined dark), a protractor arc drawn at a selected atom, a monospace readout strip, the field guide on warm paper
`#f3ead8` with ink `#2a2118` (13.22:1). Rim `#171b23`, ink `#eef1f6` (15.24:1), muted `#a3abbb` (7.47:1), arc cyan
`#5fd4ff` (10.14:1; 42+ delta E from every atom colour). Open spots: pegs plus a 2 px 3 Hz wobble, never colour alone.
The seed plate is a small specimen stand, lower-centre.
- 1366x768: the well fills the screen; kit tray down the left; readout strip along the bottom; bench switch and power
  panel top-right; the guide slides in from the right over a third; plate and `Manual` lower-left. 375x812: well on top
  (at least 420 px), readout strip, tray as one row, action row; guide as a full sheet; plate and `Manual` lower-left.
- Sound: snap click (H 1,200 Hz, C 800, O 700, Cl 500, Si 450), bond step two rising tones, closing arpeggio, pop, melt
  sizzle, growth ticks a semitone per shell, crack, bend ring, hold clink, slide swish, current hum or one spark.
- 60 fps on a school Chromebook: 40 atoms in Forge with relaxation, 600 sprite atoms in Crystal with depth sort.

## Real material and sources
Atoms (symbol, spots, valence electrons, lone pairs when full, CPK colour, covalent radius pm, sphere radius pm):
H 1 1 0 `#ffffff` 31 120; C 4 4 0 `#909090` 76 170; N 3 5 1 `#3050f8` 71 155; O 2 6 2 `#ff0d0d` 66 152; S 2 6 2
`#ffff30` 105 180; Cl 1 7 3 `#1ff01f` 102 175; Si 4 4 0 `#f0c8a0` 111 210; Na: no covalent spots, one give bead, pairs
only with Cl as ions (102 and 181 pm), `#ab5cf2`, sphere 227; Cu: no spots, Cu with Cu clumps as metal, `#c88033`, 140.
Guide pages, molecules (page, name, formula, PubChem CID, fact): 1 Hydrogen H2 783 "The lightest gas there is. Stars
like the Sun are mostly hydrogen." 2 Oxygen O2 977 "About 21 percent of the air. Its atoms share a double bond."
3 Nitrogen N2 947 "78 percent of the air, held by a triple bond." 4 Chlorine Cl2 24526 "Water plants add it to drinking
water to kill germs." 5 Hydrogen chloride HCl 313 "In water it is hydrochloric acid, the acid your stomach makes."
6 Water H2O 962 "About 71 percent of Earth's surface is water. Its bend measures 104.5°." 7 Hydrogen sulfide H2S 402
"The smell of rotten eggs. Sulfur sits under oxygen, so it is water's cousin." 8 Ammonia NH3 222 "About 88 percent of
US ammonia goes into farm fertilizer." 9 Carbon dioxide CO2 280 "Air holds about 420 parts per million. Frozen, it is
dry ice, which turns straight to gas at about -78 °C." 10 Methane CH4 297 "The main gas in natural gas." 11 Hydrogen
peroxide H2O2 784 "One more oxygen than water, and a different substance: a bleach." 12 Acetylene C2H2 6326 "Burned
with pure oxygen in welding torches, its flame passes 3,000 °C." 13 Formic acid CH2O2 284 "Some ants spray it; formica
is Latin for ant." 14 Silane SiH4 23953 "It catches fire by itself in air; chip factories use it to lay down silicon."
15 Hydrazine N2H4 9321 "Fuel for the small thrusters that steer many spacecraft." 16 Methanol CH4O 887 "Wood alcohol:
first made by heating wood. It is poisonous." 17 Ethylene C2H4 6325 "Ripening fruit gives it off, and it ripens fruit
nearby." 18 Urea CH4N2O 1176 "In 1828 Wöhler made it from non-living chemicals." 19 Ethane C2H6 6324 "Mostly turned into
ethylene to make plastics." 20 Acetic acid C2H4O2 176 "Vinegar is water with at least 4 percent acetic acid."
21 Ethanol C2H6O 702 "Most US gasoline is about 10 percent ethanol. It boils at 78 °C." 22 Dimethyl ether C2H6O 8254
"Ethanol's atoms, joined differently: it boils at -24 °C." 23 Acetone C3H6O 180 "In nail polish remover; your body
makes a little." 24 Propane C3H8 6334 "Squeezed into a tank it turns liquid. It fuels gas grills." 25 Butane C4H10
7843 "The fuel in a pocket lighter." 26 Isobutane C4H10 6360 "Butane with a branch; many home fridges use it as their
cooling gas." 27 Isopropyl alcohol C3H8O 3776 "Rubbing alcohol." 28 Glycine C2H5NO2 750 "The smallest amino acid. Rosetta
found it at a comet in 2016." 29 Benzene C6H6 241 "Faraday found it in 1825 in lamp-gas residue." 30 Vanillin C8H8O3
1183 "Vanilla's main flavour; almost all of it is made in factories." 31 Aspirin C9H8O4 2244 "First sold in 1899, made
from a cousin of a chemical in willow bark." 32 Caffeine C8H10N4O2 2519 "A 12-ounce cup of brewed coffee holds about
113 to 247 mg." Each stores its bond graph (PubChem SMILES, explicit H) and PubChem 3D conformer (H2: 74 pm), about 12 KB.
Guide pages, crystals: 33 Salt (seed Na, Cl; each ion touches 6 of the other); 34 Diamond (C, or C-C; 10 on the Mohs
scale); 35 Graphite (C=C; pencil lead is graphite and clay; graphene Nobel 2010); 36 Silicon (Si or Si-Si; diamond's
pattern; chips); 37 Silica (Si, O; quartz and sand); 38 Copper (Cu; 12 neighbours, bends, most wire); 39 Sodium metal
(Na; soft enough to cut with a knife). Growth rules, budgets (diamond and silicon 525 atoms in 9 shells; graphite 600 in
4 AB sheets 335 pm apart; salt 392 ions, an 8 by 7 by 7 box; copper 561; sodium 559; silica 147 Si and 220 O, straight
cristobalite form), the no-grow seed messages, the 40 also-known names, the special cards (O=Si=O, O3 ring, Na+ Cl- in
Forge, Cu-Cu), tap-to-add, focus, bond stepping, shape (tetrahedral 109.5, flat 120, straight 180; 2.5 degrees off per
lone pair), relaxation (40 atoms), glide to the conformer on a match, skeleton matching (element-labelled graph
isomorphism, bond orders ignored once every spot is full), and Push and Current outcomes: copy exactly from the super
tool spec (git 0f8b5f6d, "Content" and "Interactions in detail"). They are unchanged and checked there in Python.
Sources (all in the super tool spec's Sources, unchanged): NGSS MS-PS1-1; OpenStax Chemistry 2e 7.6, 10.6, 18.3 (CC BY
4.0); PubChem PUG REST (public domain); CRC Handbook lattice parameters; Jmol colours; Cordero 2008, Bondi 1964, Shannon
1976 radii; NASA, USGS, EIA, EPA, FDA, ESA, OSHA, ATSDR, Royal Institution, ACS and the other fact sources per page.
Art: one painted picture per page (39, 4:3, no people) and one backdrop, subjects as in the super spec's Art, about
1.2 MB WebP; atoms, bonds, crystals and the battery in code. Budget about 1.4 MB (goal 2 MB, ceiling 6 MB).

## Honesty notes
- Spots model valence; real bonding has more (charges, resonance). Special cards say where the rule allows what nature
  does not (O=Si=O, a ring of three O). Stereo is not checked; no guide entry has any.
- Shapes follow the groups rule while building, then glide to PubChem's measured conformer on a match; angles say "about".
- Crystals stop at a budget; silica is drawn straight (real quartz bends Si-O-Si to about 144 degrees, said on screen).
  Push and Current are qualitative (crack, bend, hold, slide; flow, a little, none), with no made-up strengths.

## Voice
`knowing-guide` (a curator). First-run hint on the rim, spoken once after the first tap: "Tap an atom to snap it on."
Then only a molecule's name when it first closes this visit ("Water.") and a Crystal test's result line. Read speaks
the readout strip: formula, name or "not in this guide", open spots, the selected atom's angle.

## Done when
1. First two minutes, no reading: two taps on H make water, which bends and names itself; two more make H2.
2. All 32 molecules build by hand and are named, benzene, vanillin and aspirin with either double-bond pattern; ethanol
   and dimethyl ether name differently; formaldehyde shows its also-known card; H2N-NH-NH2 reads NOT IN THIS GUIDE.
3. Bond stepping, angles (about 109, 106, 104 after the glide) and Hill formulas match the super spec's rules.
4. All 7 seeds grow to the stated counts; no-grow seeds give their messages; inside neighbours 4, 3, 6, 12, 8, Si 4.
5. Push and Current give the stated outcomes for every crystal; a tap mid-test shows the end state the same frame.
6. The field guide is browsable in any order with no counts, no locked or dark pages, and no "found" marks.
7. The well is the largest thing at 1366x768, 680x425 and 375x812; tray and readouts visible without scrolling.
8. 40 atoms and 600 crystal atoms hold 60 fps at 4x CPU slowdown; keyboard alone builds water and grows salt.
9. Shelf survives a reload; storage blocked still plays with one line saying so.
10. No score, goal, level, sticker or finish screen anywhere; no "1 of 39".
11. Short test passed and reported with one frame beside Elements Inspector; console clean, no network, no em dashes.

## Open questions
- Should guide pages built on this device carry a pencil "built here" note? Lean: no; it drifts back to a checklist.
- Caffeine's coffee range (FDA) for grades 6 to 10: keep? Lean: keep, it is a measured fact, not advice.
- Sodium metal page: keep? Lean: keep, salt's counterpart that bends and conducts.

## What changed from the super tool spec
- The sticker Book became a field guide: every page readable, no silhouettes, counts or "found" marks.
- The 25 goals went; their lessons moved to the Manual. Inventions became shelf entries marked "not in this guide".
- Kit header, mode pills and right panel became a viewing well, a kit tray, a readout strip and a bench switch; voice
  cut to one hint, names on first close and test results.
- Kept unchanged: atoms, the 39 pages and facts, growth rules, matching, geometry, Push and Current, budgets, art, sources.

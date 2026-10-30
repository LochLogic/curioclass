# Molecule Forge

## One idea
Every atom comes with a set number of bonding spots, and the one rule "a bond fills a spot on each atom" does
everything: fill every spot and the structure closes into a finished molecule (water, then caffeine); leave the pattern
open and the same rule never stops, growing diamond, salt or copper, and how those atoms are held decides whether the
crystal cracks, bends or carries a current.

## First minute
No reading needed. Nothing speaks before the first tap (kit rule).
- 0 s: a dark forge stage. One red oxygen atom floats in the middle, slowly turning, with two glowing pegs (its open
  bonding spots) that wobble and hum softly. Down the left, the atom tray: nine fat atom buttons, each showing its
  pegs. The tray's white hydrogen button pulses once.
- 3 s: the student taps hydrogen. It flies from the tray, snaps onto a peg with a bright click, and the pair bobs. One
  peg is left, still wobbling. The welcome line starts (Voice wForge).
- 6 s: a second tap on hydrogen. Click, and the molecule settles: the pegs vanish, it bends to its real angle, a cyan
  ring of light pulses out, a three-note chime plays, and a sticker slides into the Book button: "Water, 1 of 39", and
  the curator says "Water. It's in your book now."
- 10 s: tapping hydrogen again drops a lone hydrogen beside the water (water has no spots left). Tap once more and the
  two hydrogens snap into H2: a second sticker. The student has learned "spots fill, then it stops" without a word.
- 20 to 60 s: they try carbon (four pegs, a pyramid of them), stack hydrogens until methane closes, drag-rotate it, tap
  Book and see two or three filled pages with painted pictures and one empty silhouette per unfound page. A carbon
  chain that keeps growing sideways never closes until they cap it, which is the first hint of Crystal mode.

## Not like
- bond-battle (gr 10, molecules): cards and boiling points between particles. Here no battle, no heat: the structure
  itself, molecule versus extended structure.
- reaction-kitchen (gr 7, molecules): atoms rearrange in reactions. Here atoms only join; nothing reacts.
- equation-balancer, mole-bakery (gr 10): formulas are given and counted. Here building makes the formula, and one
  formula can make two molecules.
- elements-inspector (built): inside one atom. Here atoms are balls with spots; how they join is the point.
- made-from (gr 7, same module, MS-PS1-3) and particle-party (gr 7, states): no materials history, no heat here.
- field-lines, circuit-builder (sandboxes, gr 11): field board and circuit grid. Here a 3D atom turntable and a
  painted book.
- Takes over the Molecule Builder card (tools/molecule-builder/idea.md): its spots rule, recipe drawer (now the Book),
  repeat-a-pattern crystals and the formula, ball-and-stick and space-filling compare.

## Who and how
- Grades 6 to 10 (catalog: grade 7, Science, Atoms and Molecules, Physical Science). Students drive, solo or pairs on
  one laptop. 15 to 45 minutes, and it is built to be reopened.
- Topic line: "atoms, molecules and extended structures".
- Standard: MS-PS1-1 (develop models to describe the atomic composition of simple molecules and extended structures):
  Forge builds simple molecules in three representations; Crystal grows extended structures from a repeated pattern.
- tool.json: driver "students", minutes "15-45", modes ["Forge", "Crystal"], grades_label "Grades 6-10".

## Screens and modes
Header: title "Molecule Forge", subtitle "Fill every spot." Mode buttons `Forge` (opens first) and `Crystal`; `Book`
(opens the book drawer, with a found counter "7 / 39"); kit buttons `Motion`, `Sound`, `Read`. Layout: atom tray as a
column on the left (a row along the bottom under 760 px wide), the stage in the middle as the largest thing, the panel
on the right (info card, view switch, actions, hint `#hint`). Main controls (tray, `Undo`, `Clear`, `Grow`, `Push`,
`Current`) stay visible without scrolling at every size in STANDARDS.md. Under 900 px tall, the panel compacts to
buttons first, info card below.

### Forge (explore, opens first)
Focus: the structure being built, drawn at least half the stage height, turning slowly when idle.
- Atom tray (9 buttons, Content "Atoms"): H, C, N, O, S, Cl, Si, Na, Cu. Each shows its color, symbol and pegs.
- Tap an atom button: it joins the focus structure (Interactions "Tap to add"). Drag it instead to drop it on a chosen
  peg, or on empty stage to start a new structure.
- Tap a bond: it steps single, double, triple, back to single, as far as both atoms have spots (Interactions).
- Drag one stage atom onto another stage atom: if both have an open spot and are not bonded, a new bond forms (this
  closes rings). Drag a stage atom far away (over 2.5 bond lengths) to pull it off with a pop; drag it onto the tray to
  melt it away.
- Drag empty stage to rotate; wheel or pinch to zoom; `Center` re-frames.
- View switch: `Sticks` (ball-and-stick, default) and `Spheres` (space-filling at van der Waals size). The formula
  (Hill order, subscripts) is always shown in the info card.
- Info card (panel): the focus structure's formula; atom count "9 / 40 atoms"; open spots "2 spots open" or "All spots
  full"; when a book entry is found, its name, page number and `Open page`; when complete but unknown, "Every spot is
  full. Not in the book" and `Add to inventions`. Tap an atom on stage to select it: the card then shows "Oxygen: 2
  spots, 2 filled, 2 lone pairs" and its bonds as buttons ("O to H, single"), each stepping the bond order like a tap
  on the bond (the keyboard path), plus the angle at that atom ("about 104°").
- Actions: `Undo` (last 30 steps), `Clear` (empties the stage, keeps the Book), `Save` (puts the focus structure on the
  shelf), `Show` (turntable view, below).

### Crystal
Focus: the growing crystal, center stage, auto-zooming out as it grows; the seed plate is a small round plate in the
lower left of the stage.
- Same atom tray. Tap or drag atoms onto the seed plate (at most 2 atoms; the plate shows their pegs and bonds, and a
  tap on the bond between them steps its order). `Grow` starts growth from the seed by its rule (Content "Growth
  rules"); `Clear seed` empties the plate.
- Growth adds one shell of atoms every 300 ms (one frame per shell with Motion off), each new atom clicking into place
  with a soft tick that rises in pitch, until the atom budget stops it (Interactions). The info card names the crystal,
  counts atoms ("525 atoms, 87 deep inside"), and reads the pattern: "Every carbon inside touches 4 carbons."
- Tap any crystal atom: it and its touching neighbors light up, with the count ("This chloride touches 6 sodium ions").
- Tests (enabled once a crystal has grown): `Push` slides the top half of the crystal along a layer; `Current` clips a
  battery across it. Results in Interactions; each takes about 1.5 s and a tap anywhere, a key, or a mode change
  finishes it at once.
- `Cut open` toggle: hides the front half so the inside pattern shows. View switch `Sticks` / `Spheres` as in Forge.
- `Save` puts the crystal (its seed and rule, not every atom) on the shelf.

### Book (drawer over either mode)
Focus: the open page. Three tabs: `Pages`, `Goals`, `Shelf`.
- Pages: 39 pages (32 molecules, 7 crystals) in Content order, two per spread on wide screens. Found page: painted
  picture, name, formula, a small turning model in code, the fact, and the kind ("molecule" or "extended structure").
  Unfound: a dark silhouette of the model and the atom count only ("9 atoms: C, H, O"), so it is a target without being
  a recipe. Below the pages, the "Also known" strip (40 names, Content), shown as found names and "?" chips, and
  "Inventions" (the student's own legal unknowns, up to 12).
- Goals: the ladder (Goals section), each with a check mark when met. Never blocks anything.
- Shelf: up to 12 saved builds as thumbnails (rendered in code). Tap one: `Load` (into Forge or Crystal), `Show`,
  `Delete`.
- `Show` (also in the panel): full-stage turntable of one build, slow rotation, name and formula in large type, and a
  `Back` button. This is the "turn the screen around" view.
- Saved on this device: localStorage `curio-molecule-forge` (found pages, also-known found, inventions, goals, shelf),
  try/catch, works with storage blocked. `Reset book` in the Book (asks "Clear every page and goal? Yes / No").

## Goals
Optional; 25 goals in order. Check = the exact test the code runs. Each met goal: chime, the goal flashes in the Book
button, the line `goalDone`. "Complete" means connected and every atom's spots full.
1. First bond. Any two atoms bonded. Teaches: a bond uses one spot on each atom.
2. Close one. Any complete structure. Teaches: a molecule stops when the spots are full.
3. Water. Book match H2O. Teaches: a formula is a count of atoms in one molecule.
4. The air. Find both N2 and O2. Teaches: double and triple bonds (tap the bond).
5. Same eight, bent three ways. Find CH4, NH3 and H2O. Teaches: lone pairs push bonds closer (angles 109.5, about 107,
   about 104.5 degrees, read in the info card).
6. Dead straight. Any complete structure with an atom whose angle reads 180 degrees (CO2, C2H2, HCN). Teaches: two
   groups around an atom go opposite.
7. One more oxygen. Find H2O and H2O2. Teaches: adding one atom makes a different substance.
8. Carbon ladder. Find C2H6, C2H4 and C2H2. Teaches: bond order sets how many hydrogens fit and the shape.
9. Same atoms, two drinks. Find ethanol and dimethyl ether (both C2H6O). Teaches: arrangement, not just atoms, decides
   the substance (one boils at 78 °C, one at minus 24 °C).
10. Branch out. Find butane and isobutane. Teaches: isomers again, with a branch.
11. Ring maker. Any complete structure containing a ring (a cycle in the bond graph). Teaches: chains can close.
12. Benzene, either way. Find benzene; the card notes which of its 2 double-bond patterns you used. Teaches: some
    molecules have more than one valid way to place double bonds and are still one molecule.
13. Sour pair. Find formic acid and acetic acid. Teaches: a repeated group (C=O with O-H) shows up in different
    molecules.
14. First from scratch. Find urea or glycine. Teaches: molecules from living things are atoms like any other.
15. Inventor. Add one complete structure that is not in the book or the also-known list to Inventions. Teaches: the
    rule allows more molecules than any list.
16. Big build. Any complete structure with 20 or more atoms. Teaches: big molecules obey the same rule.
17. Vanillin (19 atoms). 18. Aspirin (21 atoms). 19. Caffeine (24 atoms). Teach: reading a model as a plan.
20. Grain of salt. Grow salt. Teaches: an extended structure is a repeating pattern with no set size.
21. Two carbons, two crystals. Grow diamond and graphite. Teaches: the same atom in a different pattern gives a
    different material.
22. Crack it. Push salt and see it split. Teaches: ions in a pattern; shift it and like charges meet.
23. Bend it. Push copper or sodium and see it stay whole. Teaches: metal atoms share electrons in every direction.
24. Spark test. Run Current through at least 5 different crystals. Teaches: free electrons carry current.
25. Sand from a rule. Grow silica, after finding CO2. Teaches: carbon and silicon sit in the same column but CO2 is a
    small molecule and SiO2 a giant one.

## Content
### Atoms (symbol, name, spots, valence electrons, lone pairs when full, color, covalent radius pm, sphere radius pm)
- H hydrogen, 1, 1, 0, `#ffffff` (dark outline), 31, 120
- C carbon, 4, 4, 0, `#909090`, 76, 170
- N nitrogen, 3, 5, 1, `#3050f8`, 71, 155
- O oxygen, 2, 6, 2, `#ff0d0d`, 66, 152
- S sulfur, 2, 6, 2, `#ffff30`, 105, 180
- Cl chlorine, 1, 7, 3, `#1ff01f`, 102, 175
- Si silicon, 4, 4, 0, `#f0c8a0`, 111, 210
- Na sodium: no covalent spots; one "give" spot (a small + bead). Pairs only with Cl as ions (Na+ and Cl-, drawn at
  ionic radii 102 and 181 pm). `#ab5cf2`, sphere 227.
- Cu copper: no spots; a soft halo. Cu touching Cu clumps as metal. `#c88033`, sphere 140.
Lone pairs = (valence electrons minus bonding electrons used) / 2, shown as faint lobes in `Sticks` view. Bond drawing
length = sum of covalent radii, times 0.87 for double and 0.78 for triple.

### Book: molecules (page, name, formula, atoms, PubChem CID, fact)
1. Hydrogen, H2, 2, 783: "The lightest gas there is. Stars like the Sun are made mostly of hydrogen."
2. Oxygen, O2, 2, 977: "About 21 percent of the air you breathe. Its two atoms share a double bond."
3. Nitrogen, N2, 2, 947: "78 percent of the air is nitrogen, held together by a triple bond."
4. Chlorine, Cl2, 2, 24526: "Water plants add chlorine to drinking water to kill germs."
5. Hydrogen chloride, HCl, 2, 313: "Dissolved in water it is hydrochloric acid, the acid your stomach makes."
6. Water, H2O, 3, 962: "About 71 percent of Earth's surface is covered by water. Its bend measures 104.5°."
7. Hydrogen sulfide, H2S, 3, 402: "The smell of rotten eggs. Sulfur sits under oxygen, so it is water's cousin."
8. Ammonia, NH3, 4, 222: "About 88 percent of the ammonia made in the US goes into farm fertilizer."
9. Carbon dioxide, CO2, 3, 280: "Air holds about 420 parts per million. Frozen, it is dry ice, which turns straight to
   gas at about minus 78 °C."
10. Methane, CH4, 5, 297: "The main gas in natural gas, burned in many stoves and furnaces."
11. Hydrogen peroxide, H2O2, 4, 784: "One more oxygen than water, and a different substance: a bleach."
12. Acetylene, C2H2, 4, 6326: "Burned with pure oxygen in welding torches, its flame passes 3,000 °C."
13. Formic acid, CH2O2, 5, 284: "Some ants spray it. Its name comes from formica, Latin for ant."
14. Silane, SiH4, 5, 23953: "Silicon's version of methane. It catches fire by itself in air, and chip factories use it
    to lay down silicon."
15. Hydrazine, N2H4, 6, 9321: "Fuel for the small thrusters that steer many spacecraft."
16. Methanol, CH4O, 6, 887: "Also called wood alcohol: it was first made by heating wood. It is poisonous."
17. Ethylene, C2H4, 6, 6325: "Ripening fruit gives off this gas, and it makes nearby fruit ripen too."
18. Urea, CH4N2O, 8, 1176: "In 1828 Friedrich Wöhler made it from non-living chemicals, a first for a substance found
    in living things."
19. Ethane, C2H6, 8, 6324: "Taken from natural gas and mostly turned into ethylene to make plastics."
20. Acetic acid, C2H4O2, 8, 176: "Vinegar is water with at least 4 percent acetic acid."
21. Ethanol, C2H6O, 9, 702: "Most US gasoline is about 10 percent ethanol. It boils at 78 °C."
22. Dimethyl ether, C2H6O, 9, 8254: "The same atoms as ethanol, but it boils at minus 24 °C, so it is a gas in the
    room."
23. Acetone, C3H6O, 10, 180: "It is in nail polish remover, and your own body makes a little."
24. Propane, C3H8, 11, 6334: "Squeezed into a tank it turns liquid. It fuels gas grills."
25. Butane, C4H10, 14, 7843: "The fuel inside a pocket lighter."
26. Isobutane, C4H10, 14, 6360: "The same atoms as butane with a branch. Many home refrigerators use it as their
    cooling gas."
27. Isopropyl alcohol, C3H8O, 12, 3776: "Rubbing alcohol from the drugstore."
28. Glycine, C2H5NO2, 10, 750: "The smallest amino acid, a building block of proteins. The Rosetta probe found it at a
    comet in 2016."
29. Benzene, C6H6, 12, 241: "Michael Faraday found it in 1825 in the oily leftovers of lamp gas. Its double bonds can
    sit two ways."
30. Vanillin, C8H8O3, 19, 1183: "The main flavor of vanilla. Almost all vanillin sold is made in factories, not taken
    from beans."
31. Aspirin, C9H8O4, 21, 2244: "A pain medicine first sold in 1899, made from a cousin of a chemical in willow bark."
32. Caffeine, C8H10N4O2, 24, 2519: "A 12-ounce cup of brewed coffee holds about 113 to 247 milligrams of it."
Each entry stores its bond graph (from the PubChem SMILES in Sources, hydrogens explicit) and its PubChem 3D conformer
coordinates (record_type=3d; H2 has none, use 74 pm straight). The builder fetches the SDFs once and inlines them
(about 12 KB).

### Book: crystals (page, name, seed, rule, fact)
33. Salt (sodium chloride): seed Na and Cl. "Each sodium ion touches 6 chloride ions and each chloride touches 6 sodium
    ions, which is why salt grains are little boxes."
34. Diamond: seed C alone, or two C with a single bond. "Every carbon is held by 4 bonds pointing every way. Diamond is
    the hardest natural mineral, 10 on the Mohs scale."
35. Graphite: seed two C with a double bond. "Flat carbon sheets that slide apart: pencil lead is graphite and clay.
    One sheet alone is graphene (Nobel Prize in Physics, 2010)."
36. Silicon: seed Si, or two Si. "The same pattern as diamond. Computer chips are made from very pure silicon."
37. Silica: seed Si and O. "Every silicon holds 4 oxygens and every oxygen joins 2 silicons. Quartz and sand are
    silica."
38. Copper: seed Cu. "Each atom touches 12 others in a sea of shared electrons, so copper bends without breaking and
    carries current. Most electrical wire is copper."
39. Sodium metal: seed Na alone. "Sodium metal is soft enough to cut with a knife."

### Growth rules (Crystal), each checked in Python (Sources)
- Diamond and silicon: every open spot gets a new atom along it at bond length (C-C 154 pm, Si-Si 235 pm); spots point
  to the 4 corners of a tetrahedron, flipped on alternate atoms. Where a new atom would land within 0.25 bond lengths
  of one already there, the two spots bond instead (rings close by themselves). Budget stop: 525 atoms, 9 shells (1, 5,
  17, 41, 83, 147, 239, 363, 525).
- Graphite: as diamond but 3 spots at 120 degrees in a plane (142 pm), one double bond per atom placed by a perfect
  matching; sheets of 150 atoms, then 4 sheets stacked 335 pm apart, offset (AB). 600 atoms.
- Salt: ions add on the empty sites (282 pm apart, 6 directions) that touch the most ions already there; ties fill
  together. Opposite charges only touch. Stops at 392 ions (196 Na, 196 Cl), a solid 8 by 7 by 7 box.
- Copper: atoms nestle into the 12 close-packed directions (255.6 pm). 561 atoms, 6 shells.
- Sodium metal: 8 directions (body-centered, 371.6 pm). 559 atoms, 7 shells.
- Silica: silicon on the diamond pattern 322 pm apart with an oxygen between every bonded pair (Si-O 161 pm), drawn
  straight (the idealized cristobalite form; real quartz bends Si-O-Si to about 144 degrees, said in the info card).
  147 Si and 220 O (367 atoms; O to Si 1.5 overall because edge oxygens are missing, 2.0 inside).
- Seeds that do not grow (message, no growth): H, O, N, Cl or S alone or paired ("Two of these close up into a small
  molecule. Nothing left to grow."); C with O ("Carbon and oxygen close into CO2, a molecule. Try silicon with
  oxygen."); C with H, N or S ("This closes into a molecule. Grow carbon alone, or two carbons."); Na with anything but
  Cl, or Cu with anything but Cu ("These don't build a crystal in this forge. Try one atom of each alone.").

### Also known (40 names, recognized but no page; checked against PubChem)
formaldehyde, acetaldehyde, formamide, propene, propyne, cyclopropane, cyclohexane, 1-propanol, methoxyethane,
chloromethane, dichloromethane, chloroform, carbon tetrachloride, methylamine, methanethiol, hydrogen cyanide,
hypochlorous acid, carbonic acid, carbon disulfide, carbonyl sulfide, sulfur dichloride, dichlorine monoxide, ethylene
glycol, disilane, hydroxylamine, chloramine, dimethylamine, ethylamine, acetonitrile, cyclohexene, toluene,
cyclopentane, ethylene oxide, allene, ketene, diazene, methanimine, aziridine, cyclopropene, methylhydrazine. Card:
"{name}, {formula}. Known to chemists; no page in this book."

### Special cards (complete but worth a word)
- O=Si=O: "Legal by the spots rule, but silicon won't hold double bonds to oxygen in nature. It grabs four oxygens and
  grows into sand: try Si and O in Crystal." Counts as an invention only if the student adds it.
- Three O in a ring: "Legal by the rule. Real ozone, O3, is bent, not a ring, and needs a rule this forge doesn't use."
- Na with Cl in Forge: an ion pair "Na+ Cl-" snaps with a crackle: "Sodium hands an electron to chlorine. Salt doesn't
  stop at two: grow it in Crystal." Not a molecule page.
- Cu with Cu: "Metal atoms share electrons with every neighbor, no spots needed. Grow copper in Crystal."

## Interactions in detail
- Tap to add: the new atom bonds (single) to the open spot on the focus structure's atom with the most open spots, ties
  to the most recently placed atom. If the focus structure is complete or the stage is empty, the atom appears alone
  near the focus structure (not overlapping) and becomes the new focus. An atom added to a structure that has Na or Cu
  follows the Special cards.
- Focus structure: the one last touched (tap, drag or add). Shown by a faint ring under it.
- Bond order tap: from order k, go to k+1 if both atoms have at least one open spot, else back to 1 (freeing spots). A
  triple is the cap. H and Cl bonds never step (one spot). The change animates: atoms pull closer, spots on each atom
  re-aim to the new shape (4 groups tetrahedral, 3 flat at 120, 2 straight).
- Shape while building: each atom's groups = bonded neighbors + open spots + lone pairs. 4 groups point to tetrahedron
  corners (109.5 degrees between bonds), 3 to a flat triangle (120), 2 straight (180). Lone pairs squeeze: with 4
  groups, each lone pair takes 2.5 degrees off bond angles (1 lone pair 107.0, 2 lone pairs 104.5). A light 3D
  relaxation (bond springs, angle springs, a soft push between atoms 3 or more bonds apart) runs each frame, up to 40
  atoms.
- On a book match: the atoms glide (600 ms) to the PubChem 3D conformer, aligned to the current view (best-fit
  rotation), and relaxation pauses until the next edit. Angle readouts come from the drawn geometry, rounded to whole
  degrees with "about" (water then reads about 104, ammonia about 106, H2S about 93; the page fact gives water's
  measured 104.5).
- Matching: a structure is checked when it is complete. It matches an entry when the element-labeled bond graph
  (hydrogens included, bond orders ignored) is isomorphic to the entry's. Because every spot is full, any bond orders
  on that skeleton are a valid way to place double bonds for the same molecule (benzene, vanillin and aspirin have 2,
  every other entry 1). Stereo (mirror forms, cis and trans) is not checked; no book or also-known entry has any.
- Open spots: pegs glow and wobble (amplitude 2 px, 3 Hz) with a faint hum while the structure is incomplete; Motion
  off: steady pegs, no wobble.
- Atom budget, Forge: 40 atoms on stage. At 40 the tray dims and the hint says "The forge holds 40 atoms. Clear or melt
  some to add more." Caffeine (24) fits with room to spare.
- Atom budget, Crystal: growth stops at the last full shell under 600 atoms (salt: last full step). The info card says
  "Budget reached. A real grain 1 mm across holds billions of billions of atoms." (Salt: 1 mm / 0.282 nm = 3.5 million
  ions per edge, about 4.5 x 10^19 ions in the grain.)
- Push (Crystal): slip plane through the middle, top half moved over 1.5 s, outcome computed on the grown crystal.
  - Ionic (salt): top half slides one ion spacing; the code sums q1 q2 / r between the halves; when it turns positive
    (like charges face), they flash red and spring apart along a flat plane with a glassy crack. Card: "Like charges
    met and pushed apart. Salt splits along flat faces."
  - Metal (copper, sodium): slides one atom spacing and settles; it stays whole with a step on its side (bent).
    Card: "The atoms rolled to new neighbors and kept their shared electrons. It bends instead of breaking."
  - Covalent network (diamond, silicon, silica): bonds crossing the plane are counted; they stretch, glow orange and
    pull it back. Card: "{n} bonds cross this cut and none let go. Every atom is held in 3D."
  - Graphite: bonds crossing a layer gap are 0, so the top sheets slide off. Card: "No bonds between sheets, only a
    weak pull. That's how a pencil writes."
- Current: a battery and two clips appear on opposite sides. Free carriers per atom decide it: copper and sodium 1 (a
  sea of electrons, bright sparks flow, hum), graphite 1 along the sheets (sparks run along sheets only), silicon "a
  little" (a few slow sparks; card: "Silicon carries a little current, more when warm: a semiconductor"), salt, diamond
  and silica none (clips spark once, nothing flows; salt's card adds "Melt it or dissolve it and the ions can carry
  current").
- Any tap, key or mode button during growth, Push or Current completes it at once (same frame) and shows the result;
  `Clear seed` or `Grow` during growth stops it and acts.
- Show: rotation 12 degrees per second; Motion off: still, with left and right arrow buttons to turn by 30.
- Keyboard: tray buttons (Enter = tap to add); Tab cycles stage atoms (focus ring, name read by the screen reader);
  Enter selects; the info card's bond buttons step orders; arrow keys rotate the view, + and - zoom; Delete melts the
  selected atom; Ctrl+Z is Undo.
- Reset: `Clear` (stage), `Clear seed` (plate), `Reset book` (with confirm). Nothing else erases progress.
- `window.__tool = {state, setMode, add(sym, atIndex?), bond(i, j, order), clear(), match(), seed([syms], order),
  grow(), push(), current(), book(), goals(), seedRand(n)}` for tests.

### Sound (Web Audio, in code; silent when Sound is off)
Snap: a click whose pitch rises for lighter atoms (H 1,200 Hz, C 800, O 700, Cl 500, Si 450). Bond step: two rising
tones. Complete: three-note arpeggio. New book page: the arpeggio plus a bright sparkle and a page flip noise. Pull
off: a pop. Melt: a falling sizzle. Growth: soft ticks rising a semitone per shell. Crack: filtered noise burst. Bend:
metallic ring. Hold: dull clink. Slide: papery swish. Current: low hum (conductors), single spark (insulators).

## Look
Grades 6 to 8 band: own `:root`. Stage `#0f1218` with a faint radial glow and the painted forge backdrop at 35 percent
under it; panel `#171b23`; ink `#eef1f6`; muted `#a3abbb`. Accent `--brand #5fd4ff` (arc cyan, the glow of a completed
structure), `--brand-ink #0f1218`. Book pages are warm paper `#f3ead8` with ink `#2a2118`. Atoms use the Jmol CPK
colors in Content, shaded spheres drawn once per element as canvas sprites; white H gets a dark outline. Contrast
(computed): ink on panel 15.24:1; muted on panel 7.47:1, on stage 8.12:1; brand on panel 10.14:1, on stage 11.02:1;
brand-ink on brand 11.1:1; paper ink on paper 13.22:1. Accent differs from neighbors (CIE76 delta E): equation-balancer
teal 37, bond-battle lime, mole-bakery berry and circuit-builder blue all larger; at least 42 from every atom color, so
the completion glow never reads as an atom. Open spots are pegs plus wobble, never color alone; crystal tests use words
and motion as well as color. 60 fps budget on a school Chromebook: 40 atoms in Forge with relaxation, 600 sprite atoms
in Crystal with depth sort and no relaxation; `Cut open` and `Spheres` stay inside it.

## Art
Local FLUX (`scripts/localart.py`), no people anywhere, blank surfaces where text would go. 40 images. Atoms, bonds,
crystals, pegs, the battery and the book frame are drawn in code (they are diagrams that rotate and change). Page
pictures: 4:3, cutout no, people no, used at the top of the book page and behind the found card.
- mf-forge: a dark workshop forge at night seen from the front, a glowing anvil bench, soft blue-white light and
  floating sparks, deep shadow in the middle; 16:9; backdrop of Forge at 35 percent.
- mf-crystal: a dim geology workbench with a magnifying lamp, rough mineral specimens at the edges and an empty dark
  velvet cloth in the center; 16:9; backdrop of Crystal.
Pages (number in brackets): mf-sun (1): the Sun's glowing orange surface; mf-air (2, 3): a wide blue sky over a green
meadow; mf-tap (4): a clear glass of drinking water under a running kitchen faucet; mf-stomach (5): an
anatomical-style painting of a stomach glowing on dark; mf-ocean (6): ocean waves meeting a rocky shore; mf-egg (7): a
cracked brown egg on a rustic wooden table, yellowish vapor; mf-field (8): rows of young corn in a farm field, a
fertilizer tank at the edge; mf-dryice (9): a block of dry ice in a bowl spilling white fog; mf-stove (10): a gas
stove burner with a ring of blue flames; mf-bleach (11): a brown plastic bottle with a blank label; mf-torch (12): a
welding torch tip with a fierce blue-white flame, sparks; mf-ants (13): red wood ants swarming over a forest ant
mound; mf-wafer (14): a shiny silicon wafer with a rainbow sheen; mf-thruster (15): a small spacecraft thruster firing
a thin plume above Earth; mf-wood (16): split firewood logs stacked by a glowing stove; mf-bananas (17): green and
yellow bananas and a ripe red apple in a paper bag; mf-lab1828 (18): an old 1820s chemistry bench with glass flasks, a
small burner; mf-pellets (19): a pile of small clear plastic pellets in a scoop; mf-vinegar (20): a glass cruet of
vinegar and pickles; mf-pump (21): a gasoline pump nozzle resting in a car's fuel opening, plain pump; mf-spray (22):
an aerosol spray can releasing a fine mist; mf-polish (23): a small plain glass bottle beside cotton pads stained red
and polish bottles with blank caps; mf-grill (24): a backyard gas grill with a white propane tank underneath;
mf-lighter (25): a clear pocket lighter with a small flame; mf-fridge (26): the open door of a home refrigerator full
of fruit and vegetables; mf-firstaid (27): a first aid kit with a plain bottle, cotton balls and bandages; mf-comet
(28): a comet nucleus with jets of gas and dust, a small probe nearby; mf-gaslamp (29): an old street gas lamp glowing
at dusk; mf-vanilla (30): dark cured vanilla pods and a white vanilla flower; mf-willow (31): a willow tree's long
branches hanging over a quiet river; mf-coffee (32): a steaming cup of black coffee with roasted coffee beans; mf-salt
(33): a heap of coarse sea salt crystals showing tiny cubes; mf-diamond (34): a rough uncut diamond crystal on dark
stone, catching light; mf-pencil (35): a sharpened wooden pencil with a gray graphite tip on shaded paper; mf-chip
(36): a close-up of a computer chip's gold contacts and silicon die; mf-quartz (37): a cluster of clear quartz
crystals on sand; mf-wire (38): coils of shiny copper wire; mf-sodium (39): a lump of silvery metal under clear oil in
a glass dish, freshly cut.

## Voice
Bank voice `knowing-guide` (Sadaltager), style "Say in a knowledgeable, friendly way, like a museum curator showing off
a new find." No molecules-family tool, grade 6 to 8 science spec or this tool's neighbors use it (bond-battle
hero-coach, equation-balancer casual-peer, mole-bakery playful-friend). `Curio.voice`, `scope: () => state.mode`,
`welcomeAfter: true` (the first tap's own line plays first). Most text is read on screen; Read speaks the hint.
- wForge (how; Forge welcome, queued after the first tap; stale once a structure completes or 3 atoms are added): "Tap
  atoms to snap them on. Fill every glowing spot and it holds together."
- closed (how; the first complete structure; stale when it is edited): "Every spot is full, so it stops growing. That's
  a molecule."
- found (event; every new book page; stale when the stage changes): one line per page, "{Name}. It's in your book now."
  (32 recorded lines, Content names).
- again (event; a book entry already found is built again; stale on edit): "You've found this one. Open the book to see
  it."
- bondTip (how; a structure has two neighboring atoms with open spots for 5 s; stale when any bond steps or the
  structure completes): "Tap the bond between them to make it double."
- lonePairs (how; the first time NH3 or H2O completes; stale on edit): "Same eight electrons as methane. The lone pairs
  push the bonds closer."
- twins (event; the second molecule of an isomer pair is found; stale on edit): "Same atoms as one you found, joined
  differently. That's a different substance."
- invention (event; a complete unknown structure; stale on edit): "Every spot is full, and it's not in this book. Add
  it to your inventions."
- full (event; the 40-atom budget is hit; stale when an atom is removed): "The forge holds 40 atoms. Clear some to add
  more."
- wCrystal (how; Crystal welcome; stale once Grow is pressed): "Put one or two atoms on the seed plate. Then press
  Grow."
- noGrow (event; a seed that closes): "Those close into a small molecule. Nothing is left to grow."
- grown (event; growth ends; stale on Clear seed): "{Crystal}. It could keep going. Try Push or Current." (7 lines)
- crack, bend, hold, slide (event; Push results; stale on the next action): the four card texts in Interactions.
- flows, little, none (event; Current results): "Electrons flow through it." / "Only a little current gets through." /
  "No current. Nothing here is free to move."
- goalDone (event; a goal is met): "Goal done. It's checked off in the book."
No line names a disabled control: bondTip needs a steppable bond; wCrystal's hint names Grow only once the plate has an
atom (before that the hint reads "Put one or two atoms on the seed plate.").

## Family engine
molecules (`kit/molecules.js`, as described in tools/bond-battle/spec.md "Family engine"; the first builder of any
sibling writes `docs/families/molecules.md`). This tool uses `ATOMS` (adds `spots`, `ve`, `rcov`, `rvdw`; Na and Cu
flagged `ion` and `metal`), `SUBSTANCES` (adds its 32 molecule entries with `atoms`, `bonds` and `xyz`, and 7 crystal
entries with `kind: 'network' | 'ionic' | 'metal'`), `parse`, `hill`. It adds to the engine, for siblings to reuse:
`complete(graph)` (every spot full), `matchGraph(graph)` (skeleton isomorphism as in Interactions, refining by element
and degree, then backtracking; 24 atoms is instant), `geometry(graph)` (groups and target angles), `grow(seed, budget)`
(the growth rules) and `resonance(graph)` (count of bond-order placements).

## Sources
Standards and model
- MS-PS1-1: NGSS Lead States (2013), Next Generation Science Standards, MS-PS1 Matter and Its Interactions,
  https://www.nextgenscience.org/
- Shapes, 109.5, 120, 180 degrees, water 104.5, ammonia 106.8, lone pairs take more room: OpenStax Chemistry 2e, 7.6
  "Molecular Structure and Polarity",
  https://openstax.org/books/chemistry-2e/pages/7-6-molecular-structure-and-polarity (fetched 2026-10-29).
- Formulas, SMILES, CIDs, 3D conformers, stereo counts: PubChem PUG REST, https://pubchem.ncbi.nlm.nih.gov/ (fetched
  2026-10-29 for all 32 book and 40 also-known names). Dry ice sublimes at minus 109 °F (about minus 78 °C) and
  dimethyl ether boils at minus 24.8 °C: PubChem CIDs 280 and 8254, Experimental Properties (fetched). "Wood alcohol"
  and "rubbing alcohol": PubChem synonyms for CIDs 887 and 3776 (fetched). Ethanol boils at 78 °C: PubChem CID 702.
- Crystal structures (NaCl 6 and 6, fcc 12 neighbors, body-centered 8): OpenStax Chemistry 2e, 10.6 "Lattice Structures
  in Crystalline Solids", https://openstax.org/books/chemistry-2e/pages/10-6-lattice-structures-in-crystalline-solids
- Lattice spacings (diamond a 356.7, silicon 543.1, copper 361.5, sodium 429.1, NaCl 564.0 pm; graphite C-C 142, layers
  335 pm; Si-O 161 pm, quartz Si-O-Si about 144 degrees): CRC Handbook of Chemistry and Physics, 97th ed., "Crystal
  Structures and Lattice Parameters"; recheck at build.
- CPK colors: Jmol, https://jmol.sourceforge.net/jscolors/. Covalent radii: Cordero et al. (2008) Dalton Trans. 2832.
  Van der Waals radii: Bondi (1964) J. Phys. Chem. 68, 441. Ionic radii: Shannon (1976) Acta Cryst. A32, 751.
Facts (fetched or confirmed 2026-10-29)
- Air 78.08 percent N2, 20.95 O2, CO2 420 ppm: NASA Earth Fact Sheet, https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
- Ammonia, 88 percent for fertilizer: USGS MCS 2025 Nitrogen, https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-nitrogen.pdf
- Ethanol about 10 percent of US gasoline: EIA FAQ 27, https://www.eia.gov/tools/faqs/faq.php?id=27&t=10
- Ethane to ethylene for plastics; propane fuel; butane, isobutane in gas liquids: EIA, Hydrocarbon gas liquids
  explained, https://www.eia.gov/energyexplained/hydrocarbon-gas-liquids/
- Isobutane (R-600a) in household refrigerators: EPA SNAP, 2011 and 2018 rules, https://www.epa.gov/snap
- Rotten egg smell: OSHA, Hydrogen Sulfide Hazards, https://www.osha.gov/hydrogen-sulfide/hazards
- Acetone in nail polish remover, made by the body: ATSDR ToxFAQs Acetone, https://www.atsdr.cdc.gov/toxfaqs/tfacts21.pdf
- Vinegar at least 4 percent: FDA CPG Sec. 525.825, https://www.fda.gov/regulatory-information/search-fda-guidance-documents/cpg-sec-525825-vinegar-definitions-adulteration-vinegar-eels
- Coffee 113 to 247 mg per 12 fl oz: FDA, "Spilling the Beans", https://www.fda.gov/consumers/consumer-updates/spilling-beans-how-much-caffeine-too-much
- Glycine at comet 67P: ESA, 27 May 2016, https://www.esa.int/Science_Exploration/Space_Science/Rosetta/Rosetta_s_comet_contains_ingredients_for_life
- Benzene, Faraday 1825, oily residue of lamp gas: Royal Institution, "Benzene at 200", https://www.rigb.org/node/6115
- Urea 1828: Wöhler, "On the artificial production of urea", https://web.chemteam.info/Chem-History/Wohler-article.html
- Formic acid and formica: Britannica, "formic acid", https://www.britannica.com/science/formic-acid
- Ethylene and ripening: UF IFAS, "Ethylene Treatments", https://irrec.ifas.ufl.edu/postharvest/pdfs/past_events/2003_presentations/Ethylene_Treatments.pdf
- Vanillin main flavor, almost all synthetic: ACS Molecule of the Week, https://www.acs.org/molecule-of-the-week/archive/v/vanillin.html
- Aspirin, willow bark, 1899: Pharmaceutical Journal, https://www.pharmaceutical-journal.com/news-and-analysis/infographics/a-history-of-aspirin
- Silane catches fire in air, used to deposit silicon: Air Liquide, https://encyclopedia.airliquide.com/silane
- Hydrazine, spacecraft thruster fuel: NASA GPIM, https://ntrs.nasa.gov/citations/20140009383
- Oxyacetylene flame over 3,000 °C: TWI, https://www.twi-global.com/technical-knowledge/job-knowledge/oxy-fuel-welding-003
- Sodium cuts with a knife: ChemEd X, Element of the Month: Sodium, https://chemedx.org/node/4128
- Recheck at build (standard references, not fetched this session): methane is most of natural gas (EIA, Natural
  gas explained); butane in pocket lighters (PubChem CID 7843, Uses); Sun mostly hydrogen (NASA, Sun facts); 71 percent
  of Earth's surface is water (USGS Water Science School); chlorine disinfects drinking water (CDC, Water Disinfection
  with Chlorine); stomach acid is hydrochloric acid (NCBI Bookshelf, Physiology, Gastric Acid); hydrogen peroxide as a
  bleach (PubChem CID 784, Uses); methanol from heating wood (Britannica, methanol); diamond 10 on Mohs (USGS, Mohs
  Hardness Scale); pencil lead is graphite and clay (USGS Graphite statistics); graphene Nobel 2010 (nobelprize.org);
  chips from pure silicon and quartz is silica (USGS Silicon and Silica MCS 2025); copper in wire (USGS Fact Sheet
  2009-3031, Copper); silicon won't hold Si=O double bonds (OpenStax Chemistry 2e, 18.3).
Checks run (Python 3.13, networkx 3.6, numpy, scipy; scripts in the spec agent's scratchpad, 2026-10-29)
- Bonding rules on every book molecule: parsed each PubChem SMILES, filled hydrogens by the spots table (H1 C4 N3 O2 S2
  Cl1 Si4), confirmed every atom's bond orders sum to its spots and the atom counts equal PubChem's formula: 32 of 32
  book and 40 of 40 also-known pass. Atom counts as listed (caffeine 24 is the largest, under the 40 budget).
- No two of the 72 entries share a skeleton (pairwise isomorphism, element-labeled): the match never confuses two
  pages. Isomer pairs verified distinct: C2H6O (ethanol, dimethyl ether), C4H10 (butane, isobutane), C3H8O (isopropyl
  alcohol, 1-propanol, methoxyethane), C3H6, C2H7N, C2H4O, C3H4.
- Double-bond placements per skeleton (all valid bond-order assignments): benzene 2, vanillin 2, aspirin 2, toluene 2,
  every other entry 1, so skeleton matching plus "every spot full" is exactly the right test.
- PubChem AtomStereoCount and BondStereoCount are 0 for all 72 entries (no stereo to check).
- Geometry: groups-and-lone-pairs rule gives CH4 tetrahedral, NH3 pyramid, H2O and H2S bent, CO2 and C2H2 straight,
  C2H4 and benzene flat. PubChem conformers measure water 104.0, H2S 93.4, NH3 106.0, CH4 109.5, CO2 180.0, benzene
  120.0, H2O2 95.8; urea and caffeine nitrogens are flat (angle sum 360), which the rule alone would draw as pyramids,
  hence the glide to the conformer on a match.
- Strange but legal: all connected structures from 1 to 3 of C, N, O filled with H: 92 legal; 36 have names here, 56 do
  not (Inventions are easy to find; the card never claims nobody has made one).
- Growth: diamond and silicon 525 atoms, every interior atom 4 neighbors at 154.4 or 235.2 pm, all angles 109.47, every
  smallest ring 6 atoms. Graphite sheet: interior atoms 3 neighbors at 142 pm, rings all 6, a matching covers 580 of
  600 atoms (only edge atoms lack a double bond); 0 bonds between layers. Salt: 392 ions, 196 each, every interior ion
  6 opposite neighbors, 0 like-charge contacts, a full 8 by 7 by 7 box (every third step the box is solid). Copper 561,
  every interior atom 12 neighbors at 255.6 pm. Sodium 559, 8 neighbors at 371.6 pm. Silica (straight model) O-O inside
  one SiO4 262.9 pm, each interior Si has 4 O.
- Push: salt 8x8x8, energy between the halves (charge products over distance, units e squared per 282 pm) minus 5.0 at
  rest, minus 0.7 at half a spacing, plus 3.9 after one spacing (halves repel: it cracks). Copper slip on a
  close-packed layer: closest approach 256 pm at rest, 221 pm halfway, 256 pm after one spacing (it settles whole).
  Diamond 1,728 atoms: 133 bonds cross a flat cut. Graphite: 0.
- Budgets: Forge 40 (largest page 24), Crystal 600 (largest grown 600, graphite). Salt grain: 1e-3 m / 0.282e-9 m =
  3.55 million ions per edge, cubed 4.5 x 10^19 ions.
- Contrast and accent distance: computed (Look).

## Done when
1. First minute with no reading: the stage opens with O and two wobbling pegs; two taps on H make water with the glow,
   chime and "Water, 1 of 39" sticker; two more taps on H make H2.
2. Every book molecule can be built by hand and is recognized, including benzene, vanillin and aspirin with either
   double-bond pattern; ethanol and dimethyl ether land on different pages; an also-known molecule (formaldehyde) shows
   its name card; a complete structure outside both lists (H2N-NH-NH2) offers `Add to inventions`.
3. Bond tap: C=C steps to C triple C and back to single; a bond whose atom has no spot left goes back to single; H
   bonds never step. Angles read about 109, 106, 104 for CH4, NH3, H2O after the glide.
4. Crystal: each of the 7 seeds grows its crystal to the counts in Content; C with O, and H alone, give the no-grow
   messages. Tapping an interior atom lights the right neighbor count (diamond 4, graphite 3,
   salt 6, copper 12, sodium 8, silica Si 4).
5. Push gives crack (salt), bend (copper, sodium), hold with a bond count (diamond, silicon, silica), slide (graphite);
   Current gives flow, a little, or none as in Interactions.
6. Focus: in Forge the structure is the largest thing on stage; in Crystal the crystal is central and the seed plate
   small; at 1366x768 and in the 680x425 preview.
7. A tap or key during growth, Push or Current shows the end state in the same frame; a mode button mid-growth switches
   at once.
8. 40 atoms in Forge and 600 in Crystal hold 60 fps in Chrome's performance panel with 4x CPU slowdown; the budget
   messages show at the limit.
9. Book, goals, inventions and shelf survive a reload; `Reset book` clears them; storage blocked still plays.
10. Voice: how lines once per load, found and result lines every time; no line names a disabled control; all 40 images
    load, none shows a person; keyboard-only can build water and grow salt; console clean, no network, no em dashes.
11. Ten-minute check: a fresh player with no instructions is still choosing to play after 10 minutes, and can name one
    thing they figured out.

## Teacher note
Three ways to use it in a period: free play (find 10 pages, then share one surprise with a partner); a goal set (goals
5, 9 and 21: "what decides a substance, the atoms or the arrangement?"); a room challenge (who can find a legal
invention, and can the class check its spots on the board). Reaches MS-PS1-1: models of simple molecules and extended
structures in formula, ball-and-stick and space-filling form. No worksheets.

## Open questions
- Caffeine's fact uses FDA's 12-ounce coffee range (113 to 247 mg). Keep a coffee number for grade 6 to 10, or swap for
  a non-dose fact (tea, cola and chocolate all contain it; source needed)?
- Sodium metal page and its seed: keep (a soft metal that bends and conducts, the counterpart to salt), or drop to six
  crystals and 39 images?
- Book silhouettes show atom counts ("9 atoms: C, H, O"). Is that enough of a hint, or should unfound pages stay fully
  dark?

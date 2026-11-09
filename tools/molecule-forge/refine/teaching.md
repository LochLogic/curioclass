# Teaching lens: molecule-forge (Curiosity No. 12), round 1

Judged against docs/agents/CODEX-CURIOSITY.md and VISION.md "Curiosities: the second shape", not lesson norms.
Scratch: `S:/CurioClass-codex-scratch/molecule-forge/teaching/` (frames in `frames/`, rule checks in `checks.js` and
`checks.json`, run headless on the built bundle, port 9441).

Counts: 1 blocker, 5 should fix, 4 polish, 3 nits.

## Findings

### 1. Bond labels state lengths the model on screen contradicts (blocker, family:curiosity)
- Where: src.html:726 (bond button text), length() at src.html:376; Forge, any matched molecule.
- What: the visible label is the radius-sum estimate ("H single · ~62 pm") even after the molecule has glided to its
  stored conformer. The estimate's assumption fails exactly where students look: H2 reads ~62 pm while the model is
  drawn at 74 pm (the Manual itself says 74). Benzene, vanillin and aspirin ring bonds read "single ~152" and "double
  ~132" while every ring bond in the model is 139 pm, so the readout teaches the alternating-length misconception the
  real structure disproves. Others more than 5 percent off: O2 115 vs 123, H2O2 O-O 132 vs 145, formic acid C-O 142 vs
  135, urea and caffeine C-N 147 vs 137-139. Only the aria-label and a Manual paragraph say "radius estimate"; the
  visible text just says "~".
- How seen: frames/h2-label.png (label "H single · ~62 pm" beside the drawn H2); `dev` shot in shots2.json measured
  every guide bond against its label (14 bond types over 5 percent).
- Better: once a structure matches, label the stored model's length ("139 pm, model"); keep the radius estimate only
  while building and say "estimate" on screen.

### 2. Most field guide facts are gone; 22 of 32 molecule pages and all 7 crystal pages restate the model (should fix, family:curiosity)
- Where: material.json `fact`; crystal pages built at src.html:1076 (`fact:c.pattern`).
- What: 22 molecule pages read "In this model: 2 O. 1 double bond." (Oxygen, Nitrogen, Ammonia, Methane, CO2, Acetone,
  Propane, Butane, Vanillin, Aspirin and 12 more). The crystal pages say only "Every inside atom touches 4 neighbours."
  The spec lists a real fact for each (21 percent of the air, 78 percent nitrogen, dry ice at -78 °C, fertilizer,
  Mohs 10, pencil lead, chips, quartz and sand, most wire, sodium cut with a knife) and says they are kept unchanged.
  The guide is meant to be read "like a book"; with these it answers nothing the strip did not already say, and the
  crystal pages lose the structure-to-use link that HS-PS2-6 rides on. The Manual's "Field guide facts" list repeats the
  same 22 placeholders as facts.
- How seen: frames/guide-oxygen.png, frames/guide-diamond.png; a count over material.json (22 of 32 start "In this model").
- Better: restore the spec facts, each with its named source (most are NASA, USGS, EIA, EPA, NIST-level facts that are
  easy to double-source); drop only the ones that truly fail a second source.

### 3. The outer-electron link (HS-PS1-1) is claimed but never shown (should fix, general)
- Where: spec Map "outer electrons set the bonding spots"; notes.md "Good to know"; atom table src.html:287 (`ve` is
  defined but never displayed).
- What: the student sees spots, filled and lone pairs, never the valence electron count, so nothing they can do or
  see connects spots to outer electrons or the periodic table. Rule 2 binds only the anchor (MS-PS1-1, taught well),
  but the "also reaches" claim is not true as built.
- How seen: grep of src.html (`.ve` unused); selection readout in frames/water and h2-label.
- Better: one more line in the selected-atom readout ("6 outer electrons · needs 2 more · 2 spots"), and on the tray
  ball's label; or drop HS-PS1-1 from the spec and notes.

### 4. A lone atom and its molecule carry the same name (should fix, family:curiosity)
- Where: src.html:709.
- What: the opening oxygen atom reads "Oxygen", identical to the O2 page "Oxygen · O2"; a lone H reads "Hydrogen",
  and so does H2 one tap later. Atom versus molecule is the core idea of the anchor (MS-PS1-1), and the strip blurs it
  at the very first screen.
- How seen: frames/guide-oxygen.png (strip "O / Oxygen" beside page "Oxygen · O2 · 2 atoms"); checks.json `loneH`
  and `h2` both name "Hydrogen".
- Better: "oxygen atom" / "hydrogen atom" for a single atom; the guide name only for a matched molecule.

### 5. O=Si=O settles bent, at about 165 degrees, against the groups rule it teaches (should fix, family:curiosity)
- Where: relax() at src.html:748; Forge, Things to do 7.
- What: CO2 glides to 180 (matched), but O=Si=O, which has the same two groups at the centre and no match to glide to,
  stops at 165 degrees with Motion on (153 with Motion off). Things to do 2 and 7 invite exactly this comparison, and
  the readout then says "about 165°" for a shape the Manual says is straight. Any unmatched two-group centre will do
  the same.
- How seen: `osio-motion` shot (3 s settle, angle 165.4); checks.json `osio` (calm, 153 degrees).
- Better: let relaxation reach its 180 target for two-group centres (or snap to the ideal angle when settled).

### 6. The Manual is written for an engineer, not a grade 6 to 10 reader (should fix, general)
- Where: src.html:238-276 (Manual).
- What: "element-labelled connections", "computed PubChem conformer", "Two records had no supplied 3D model", "The extra
  recognized allene record also supplied only a 2D diagram ... two perpendicular pi bonds", "cristobalite-like
  network", "appreciable current", "not an atomic slip solver". These are build notes. The honesty content is right;
  the reading level is about grade 14.
- How seen: read in the Manual drawer and in src.
- Better: plain sentences ("Hydrogen and silane use a textbook shape instead of a PubChem one"), with build detail moved
  to notes.md.

### 7. "Things people have found" has 4 of the spec's 9 entries (polish, family:curiosity)
- Where: src.html:272.
- What: missing: lone pairs squeeze the angle (109.5, 107, 104.5), the two boiling points, 56 of 92 small structures
  unnamed, salt cracks while copper bends, CO2 small but SiO2 giant, silicon a semiconductor, Wöhler 1828. These are the
  month-of-use depth the Manual is meant to hold, read after finding them.
- How seen: Manual drawer text against spec "The Manual".
- Better: add them back, each with its source.

### 8. Hill formulas on the strip differ from the guide headings for familiar molecules (polish, general)
- Where: strip formula, hill() at src.html:368.
- What: ammonia reads H3N, hydrogen chloride ClH, the ion pair ClNa, while the guide page says NH3 and HCl and the
  crystal says NaCl. Correct Hill order and the Manual explains it, but a 7th grader comparing strip and page sees two
  formulas for one substance.
- How seen: checks.json `nh3` ("H₃N" / "Ammonia"), `nacl` ("ClNa").
- Better: show the conventional formula on the strip when the guide knows the molecule, Hill order otherwise.

### 9. Crystal test results are never spoken (polish, family:curiosity)
- Where: voice/lines.json has only the hint; src.html:328.
- What: the spec's Voice says a molecule's name is spoken on first close and each Crystal test's result line too. The
  Push and Current lines ("Like charges met and pushed apart. Salt splits along flat faces.") are the HS-PS2-6 moment;
  they are only heard via Read. (Craft will judge the voice list itself.)
- How seen: grep of V.say / lines.json.

### 10. On-screen words above grade in the test lines (polish, general)
- Where: src.html:630.
- What: "No current. No mobile carriers in this model." for diamond and silica. "Nothing can move to carry charge" says
  the same thing to a 7th grader.

### 11. Plural slips (nit, general)
- src.html:670 and 706: "1 lone pairs", "1 SPOTS OPEN", tray labels "1 spots". checks.json `nh3`, `loneH`.

### 12. Salt and silica counts use "ATOMS" and a partial "INSIDE" (nit, family:curiosity)
- Salt reads "392 ATOMS" (they are ions, as the spec says); silica reads "83 INSIDE", counting only Si, while inside O
  atoms also sit fully inside. checks.json `crys`.

### 13. "Na · sodium" is lower case where every other atom is capitalised (nit, general)
- src.html selectedInfo; checks.json `nacl`.

## What passed (tested)
- Done when 1: two H on the waiting O make water, "ALL SPOTS FULL", named, "about 104°"; two more H make H2, named.
- Done when 2: every one of the 32 guide molecules matches its own page (no cross-match, butane and isobutane apart,
  ethanol and dimethyl ether apart); formaldehyde shows the also-known card; H2N-NH-NH2 reads NOT IN THIS GUIDE;
  bond orders ignored once spots fill (benzene's two drawings).
- Done when 3: angles after the glide 109 (CH4), 106 (NH3), 104 (H2O), CO2 180; Hill order as specified.
- Done when 4: all 7 seeds grow to the stated counts (525, 525, 600, 392, 561, 559, 147 Si + 220 O); inside neighbour
  counts 4, 4, 3, 6, 12, 8, Si 4, all inside atoms; no-grow messages for C#C, C-O, O, Cl, H.
- Done when 5 (outcomes): salt splits, metals bend, graphite slides, diamond, silicon and silica hold (bond counts
  from the sample); current: metals and graphite flow, silicon a little, salt and the networks none.
- Done when 6 and 10: guide index lists all 39, no counts, locks or found marks; no score, goal, level or finish anywhere.
- Special cards: O=Si=O, O3 ring, Na+ Cl- ion pair, Cu-Cu all show their honesty lines.
- No giveaway risk: there is no predict or quiz mode. No cultural, Native or hard-history content; no sensitive topic
  needing a rule 8 note. Support at home ideas (pencil, salt and copper wire, a tiled floor) are doable tonight.

## Facts spot-checked (second source: recomputation and standard reference values)
1. Salt grain 1 mm across about 4.5 x 10^19 ions: 2.165 g/cm3 x 1 mm3 / 58.44 g/mol x 6.022e23 x 2 = 4.46e19. OK.
2. Water bend 104.5 degrees. OK. 3. Quartz Si-O-Si about 144 degrees. OK.
4. Cu-Cu 255.6 pm (fcc a = 361.5 pm / sqrt 2). OK. 5. Graphite sheets 335 pm apart. OK.
6. Neighbours: diamond 4, graphite 3, rock salt 6, fcc copper 12, bcc sodium 8. OK.
7. Ethanol boils about 78 °C; dimethyl ether about -24.8 °C. OK.
8. Wöhler urea 1828; Faraday benzene 1825; Rosetta glycine at 67P, published 2016. OK.
9. Water covers about 71 percent of Earth's surface (USGS). OK.
10. Cordero covalent radii H 31, C 76, N 71, O 66, S 105, Cl 102, Si 111; Bondi vdW radii and Jmol colours as listed. OK.
11. Salt 8 x 7 x 7 = 392; silica 147 + 220 = 367. OK.
No fact on screen was wrong; the problems are the missing facts (finding 2) and the bond labels (finding 1).

## Frames looked at
Mine: frames/h2-label.png, guide-oxygen.png, guide-diamond.png, plus the scripted readouts in checks.json and the
shots2.json results (bond deviations, O=Si=O settle, silica readout). Audit: audit.md rows only; its clean rows
(Motion off, resize mid-action, held clicks) are cited, not re-shot.

## Audit pilot
- Leads confirmed: none that bear on teaching.
- Leads wrong (noise): all "overlap: #stage / ..." rows (the canvas is full screen by design); "keep region hidden" for
  #readout, #controls and #tray in the guide and manual states (modal drawers, expected); "hint out of view" in every
  state (the hint correctly goes after the first action); "choices cut short" in the guide (two source links below the
  fold of a scrolling page, fine).
- Missed (outside its reach): bond labels contradicting the drawn model, the placeholder guide facts, atom and molecule
  sharing one name, O=Si=O settling bent, the unshown valence electrons, Manual reading level.

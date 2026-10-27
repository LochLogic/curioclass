# Wave 3 spec log

Rules: `docs/agents/BATCH-W3.md`. 32 specs in four groups (9-12 science), one agent per group. The joint review
with wave 2 follows.

## Agent reports

### sci-bio (9, done)

- No renames. Numbers recomputed in Python (models, chi-square, sequences, NOAA swings, reserve plans, contrast).
- Accents: body-thermostat #e25a7e, energy-accountant #d3b069, tree-of-life #b8ead3, reserve-designer #ff4a2e
  (double outline and flag on map tiles), membrane-gatekeeper #f01aff, mitosis-mixer #f1b1ed, carrying-capacity
  #e2a19c, protein-factory #e0ff1a, punnett-predictor #a3ffaf.
- Family engines, each in full: cells (kit/cells.js: Parts, CellView, Phases, Zoom, Membrane, Field) in
  membrane-gatekeeper, naming cell-city (6) and mitosis-mixer; ecosystem (kit/ecosystem.js: Species, Web, Model,
  PopChart, Pyramid, Landscape) in carrying-capacity, naming food-web-wobble, predator-prey-island (Isle Royale
  reserved for it) and energy-pyramid; genetics (kit/genetics.js: Code, Strand, Chain, Gene, Genotype, gametes and
  cross with linkage, chiSquare, Punnett, Meiosis, Skins) in punnett-predictor, naming gene-pool (8) and
  protein-factory. All three use wave 2's kit/probability.js.
- For the joint review: five voices also used by chemistry and earth (friendly-dad with mole-bakery, gravel-ranger
  with hand-warmer-lab, science-narrator with equilibrium-seesaw, lively-host with half-life-dice, upbeat-guide with
  orbit-lab). 23 kept voices for 32 science tools, so some reuse is unavoidable.

Open questions:
- [body-thermostat] Safety pauses say "get help" with no phone number. Fine?
- [energy-accountant] climate-dashboard may also use NOAA CO2. Can both (this one uses only the 2023 seasonal swing)?
- [energy-accountant] The amino acid entry is an atom-only summary, labeled on screen. Keep, or a real two-step path?
- [tree-of-life] HS-LS4-2 and LS4-3 rest on the one-trait finch model. Enough, or add a second trait?
- [tree-of-life] UniProt has no hippo cytochrome c, so its bar reads "not sequenced". Keep as a real-data lesson, or
  swap the species?
- [reserve-designer] Budget $4,000k, since at $3,000k no plan survives a single loss. Keep, or a teacher setting?
- [reserve-designer] The SH 9 crossing figure (about 90 percent) is unverified. If it can't be confirmed, a vague tip?
- [membrane-gatekeeper] The airway level names cystic fibrosis and F508del. Keep, drop the disease name, or drop the
  level?
- [mitosis-mixer] Add real micrographs later as an optional view?
- [carrying-capacity] Wolves slider capped at 6 (7 or more collapses the herd). OK?
- [protein-factory] Keep the names sickle cell disease, hemoglobin C and cystic fibrosis on the calm cards?
- [punnett-predictor] Mutations (HS-LS3-2) covered only by pointing to protein-factory. Enough, or add
  nondisjunction?
- [punnett-predictor] If the Campbell fly counts can't be checked, use Morgan's original counts?

### sci-chem (8, done)

- No renames. Numbers recomputed in Python; each accent's contrast stated.
- Accents and voices: bond-battle hero-coach #ecf994, gas-law-lab wise-mentor #9ec9e8, equation-balancer
  casual-peer #59c0ab, mole-bakery playful-friend #c270bc, hand-warmer-lab news-reader #d28279, equilibrium-seesaw
  gentle-storyteller #c0b959, ph-mystery-liquids firm-captain #d590b0, half-life-dice curious-librarian #97c059.
- Moved after reading the biology specs: four voices (off friendly-dad, gravel-ranger, science-narrator,
  lively-host) and mole-bakery's accent (off #e0aeae). Still a little close: hand-warmer-lab vs carrying-capacity
  (dE 13), equilibrium-seesaw vs energy-accountant (dE 16). Earth and environmental voices were unchecked.
- Family engines: molecules (kit/molecules.js) in full in bond-battle; equation-balancer, mole-bakery and
  hand-warmer-lab call it but stay in family none (hand-warmer-lab asks for draw options `onBond` and `broken`;
  mole-bakery reuses reaction-kitchen's NaHCO3 and CH3COOH). particles (kit/particles.js) in full in gas-law-lab;
  equilibrium-seesaw asks for `react` (pair and split) and `steer`.

Open questions:
- [bond-battle] Boiling points of KCl, MgCl2 and SiO2 vary by source. Use PubChem's at build and note it?
- [bond-battle] Should equation-balancer, mole-bakery and hand-warmer-lab join the molecules family?
- [gas-law-lab] Its only code is HS-PS3-2; gas laws have no NGSS performance expectation. Fine?
- [equation-balancer] HS-PS1-2 met only through ion charges by group. Enough, or add combustion products?
- [mole-bakery] Day 4's 90 percent yeast yield is made up (labeled). OK, or drop percent yield?
- [hand-warmer-lab] Dissolving is physical, HS-PS1-4 is about reactions. "Dissolving is a small bond budget too",
  with the iron warmer as the true reaction: OK?
- [hand-warmer-lab] The T4 target of 0.50 kJ per gram is made up. Keep, or only compare packs?
- [equilibrium-seesaw] Pairing rate held constant, splitting carries the temperature change. OK, or both rise?
- [equilibrium-seesaw] Ammonia card is qualitative (OpenStax). Enough for HS-PS1-6?
- [ph-mystery-liquids] HS-PS1-2 fits weakly. Keep or move?
- [ph-mystery-liquids] Conductivity bulb thresholds are a model choice. OK?
- [half-life-dice] C-14 half-life: OpenStax 5,730 years or NNDC 5,700 ± 30?

### sci-env (5, done)

- Rename proposed: watershed-detective to "Up the Watershed" (the overlap note's "Upstream" dropped the topic word).
- Accents and voices: biome-atlas curious-librarian #5cbf2a, population-dashboard news-reader #f261ce, grid-operator
  firm-captain #ffbf66, watershed-detective casual-peer #5aa6c8, design-challenge-studio easy-coach #00f28d. Closest
  accent anywhere dE 15.9 (population-dashboard vs #ff7ac8). Earth group specs did not exist yet, so climate-dashboard,
  island-economy and feedback-loop-builder were avoided by concept line only. Note: curious-librarian,
  news-reader and firm-captain are also chemistry voices (half-life-dice, hand-warmer-lab, ph-mystery-liquids).
- Family engines: none. population-dashboard may reuse data-desk's Chart for one line chart. biome-atlas runs 270
  lines, a little over the guideline.

Open questions:
- [biome-atlas] Dodge City is the only miss (12 of 13 match), kept as the lesson about averages. OK, or a second miss?
- [biome-atlas] Only HS-LS2-6 is taught. Enough, or add a climate standard?
- [biome-atlas] Succession times rounded from several papers, labeled approximate. Precise enough?
- [population-dashboard] HS-ESS3-1 covered only by the "people, yields and land" panel. Keep the code?
- [population-dashboard] Feed is a world-scale formula, not a simulation. Enough for HS-LS2-1, given
  carrying-capacity simulates it?
- [population-dashboard] Energy per person stands in for "footprint". Add water or land, or keep one resource?
- [grid-operator] AEO2023 build costs (2022 dollars) mixed with 2024 fuel prices, capital at a flat 7% over 30 years
  (battery 15). OK, or newer tables?
- [grid-operator] Existing coal is paid off, so the base fleet is the cheapest plan that keeps the lights on. Keep as
  the lesson, or add a carbon price slider (policy)?
- [grid-operator] Unserved energy is never priced; reliability stays its own score. Agree?
- [watershed-detective] Take "Up the Watershed"?
- [watershed-detective] A $5,000 rain advisory meets the beach goal without cleaning the water. Honest option, or a
  miss?
- [watershed-detective] Costs, flows and loads made up, scaled to EPA guidance. OK?
- [design-challenge-studio] Challenge 3 saves typed text in localStorage. OK, or unsaved?
- [design-challenge-studio] Option costs and the room are made up. Fine?
- [design-challenge-studio] Real water-treatment steps framed as a simulation with a "follow local guidance" note.
  Enough?

### sci-earth-phys (10, done)

- Rename proposed: island-economy to "Lake Commons" (Renamed from: Island Economy).
- Accents and voices: curling-stones easy-coach #ff7a8f, orbit-lab upbeat-guide #a9c4ff, star-life-story
  smooth-narrator #b894d0, hot-meets-cold clear-teacher #ff8f5e, zipline-energy big-sister #d0c440,
  spectrum-explorer knowing-guide #ece8ff, climate-dashboard hs-narrator #94c4c4, feedback-loop-builder wise-mentor
  #ffb0d9, water-shapes-earth gravel-ranger #58acac, island-economy gentle-storyteller #7cac64. Four accents were
  moved off near-clashes with the other wave 3 groups.
- Family engines: forces (curling-stones adds G, netForce, pushRun, glide and stopFor to collision-lab's block, for
  tug-of-war-arena and crash-test-lab); astronomy in full in orbit-lab (Astro constants, orbitFromState, positionAt,
  sweptArea, deepTime, SpaceView, starColor, fmt), used by star-life-story.
- Voices shared with one distant science tool each: wise-mentor, gravel-ranger, gentle-storyteller, upbeat-guide,
  big-sister, knowing-guide.

Open questions:
- [feedback-loop-builder] ESS2-1 and ESS2-3 covered only by Deep Earth cards. OK? Show the 3.42 C lap model beside
  the IPCC 3 C?
- [water-shapes-earth] Made-up (illustrative) rates on the benches OK?
- [climate-dashboard] How deep should Futures and the carbon budget go for grade 9? Refresh data yearly, or freeze?
- [island-economy] Take "Lake Commons"? Add a sourced Indigenous fishery-management card, reviewed by a Native
  educator?
- [star-life-story] Only the Sun and 20 solar masses have sourced later stages. Find a track set (MIST)?
- [orbit-lab] Is Rock Clock an honest home for ESS1-5 and ESS1-6?
- [zipline-energy] Lab rules, or a real standard (ASTM F2959)?
- [spectrum-explorer] How to frame real health claims, and a teacher note for K1 and K6? Keep Signal Lab here?
- [hot-meets-cold] Keep the 12-particle mode where heat briefly flows backward (with an honesty note), or lock to
  60/300 particles?
- [curling-stones] Sweeping modeled only as lower friction, no curl. OK?

## Joint review of waves 2 and 3 (2026-10-27)

90 specs (58 + 32), checked together.

- **Spec sheet:** no flags on either wave.
- **Accents:** every 9-12 accent, specced and live, compared in CIELAB. Two real clashes, both fixed in the spec
  with contrast recomputed on `kit/theme-912.css`:
  - paycheck-decoder #ffe14d was identical to intersection-quest. Now apricot #ffb48c (panel 10.02:1, sec-bg 9.5:1,
    brand-ink #2a1404 on it 10.13:1); nearest other accent dE 20.4.
  - scam-shield cyan #45d0e6 was dE 4.9 from dice-in-the-chatbot #36d6e7. Now jade #36d998 (9.51:1, 9.01:1,
    brand-ink 8.75:1); nearest dE 19.9.
  - The other close pairs the scan found are light-theme paper colors or dark scene colors, not accents. The two
    near pairs the chemistry agent flagged (dE 13 and 16) were left: different subjects and grades.
- **Voices:** 23 kept voices for 90 tools, so each is reused 2 to 6 times across waves 2 and 3, never twice in one
  group. Accepted; the voice bank has no more 9-12 voices.
- **Standards:** `wave_standards.py` now reads CCSS math clusters, AP units and wrapped Standards lines (before, it
  read neither, so wave 2 could not be checked). All 58 wave 2 and 32 wave 3 specs claim exactly their module codes.
  Two codes the specs teach were added to their modules: G-GPE.A.2 on cone-slicer (the parabola, which
  coordinate-proof-lab leaves to it) and F-IF.B.6 on zoom-to-the-limit (answers the math-pre question, reversible).
- **Catalog checks:** check_codes 0 invalid, check_words 0 problems across 762 modules, check_concepts clean,
  coverage unchanged.
- **Renames waiting:** eight proposed titles (wave 2: Unit Sense, Covered: Insurance Claims, Startup Booth, Conic
  Focus Finder, Proof Tower, Slice and Stack; wave 3: Up the Watershed, Lake Commons). Each is also an open question
  for Cory. They get applied with `scripts/rename_tools.py` in one pass after the wave 2 art agent finishes, since it
  works in the old folders.
- **Shared sources, by design:** energy-accountant (NOAA 2023 seasonal swing) and climate-dashboard (long-term
  Mauna Loa); carrying-capacity simulates what population-dashboard's Feed panel computes at world scale. Both are
  in the open questions.

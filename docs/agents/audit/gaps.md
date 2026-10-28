# Curio Class overlap and gap audit: gaps (phase 1, gap agent)

Sources: docs/agents/IDEA-PASS-LOG.md, every `MOVE` line in tools/*/idea.md (renamed ids mapped through
docs/agents/overlap/renamed.json), `scripts/overlap/coverage.py --missing` and `scripts/overlap/standards.py`, run
2026-10-27 on the unedited data/. Nothing in data/ was changed. Every source and target tool below is at the idea stage
(no spec.md, no tool.json) except mind-map (live) and coordinate-proof-lab (specced), so no live tool moves.

Coverage today (all planned tools): every framework is full in the "all" column except CCSS-ELA, 414 of 455. The 41
uncovered ELA codes are the range codes (RL.10, RI.10, W.10) and the technology code (W.6). CSTA is 196 of 196.

Notes on reading the tables:
- **Whole** means the code leaves the source module. **Part** means the source keeps the rest of the code, so the code
  sits on both modules and each tool teaches its part. Modules carry codes at standard level (L.3.2, not L.3.2b), and
  math modules at cluster level (4.NBT.B), so a part move adds the code to the target and leaves it on the source.
- Option for the orchestrator: for split ELA codes, write the part letter on each module (L.6.2a on pause-and-break,
  L.6.2b on the spelling lab). coverage.py already strips the letter (`at_level`), so totals do not change.

## Code moves

55 moves (one row each): 23 to an existing tool, 3 dropped because another tool already teaches the code, and 29 to a
new tool (rows 24 and 28 to 55), which merge into 27 new tools. "Teaches?" is checked against the target's idea.md.

### To an existing tool

| # | Source tool (module) | Code | Target tool (module) | Teaches? | Source keeps |
|---|---|---|---|---|---|
| 1 | agora-assembly (social-studies-6-ancient-greece) | D2.Civ.8.6-8, whole | constitutional-convention (social-studies-8-creating-the-constitution) | Yes: "still here today" cards trace founding principles into today's system; card updated | D2.His.3, D2.Civ.9 |
| 2 | backpack-pack (social-studies-k-needs-and-wants) | D2.Eco.6.K-2, whole | community-helpers-village (social-studies-1-families-and-communities) | Yes: "Jobs and pay" step (work, how pay is earned, what pay buys) | D2.Eco.1 |
| 3 | bowling-lab (science-4-energy-and-motion) | 4-PS3-2, whole | contraption-workshop (science-4-energy-conversion-devices) | Yes: energy view shows transfer by current, light, sound and heat; card updated | 4-PS3-1, 4-PS3-3 |
| 4 | colonial-trade-routes (social-studies-5-colonial-economies) | D2.Geo.9.3-5, whole | settle-the-valley (social-studies-4-human-environment-interaction) | Yes: flood year forces families to move or rebuild. Card needs a D2.Geo.9 standards line | D2.Eco.3, D2.His.2, D2.Geo.11 |
| 5 | state-economy-map (social-studies-4-state-economy-and-resources) | D2.Geo.9.3-5, whole | settle-the-valley (same as row 4) | Yes, as row 4 | D2.Eco.4, plus **add D2.Geo.11.3-5** (then/now toggle on industry layers, per its card) |
| 6 | comma-chameleon (ela-5-conjunctions-tense-and-commas) | L.5.2 part e (spelling) | draft-car-wash (ela-3-5-revising-and-editing) | Yes: grade 5 Polish station; card updated | L.5.2 a-d (commas, titles) |
| 7 | dialogue-director (ela-3-narrative-writing) | L.3.2 parts b, e, f, g (address commas, spelling, dictionary) | draft-car-wash (same) | Yes: grade 3 Polish station; card updated | W.3.3, L.3.2 a, c, d (dialogue punctuation, title capitals, possessives) |
| 8 | draft-car-wash (ela-3-5-revising-and-editing) | L.5.3 part b (varieties of English) | script-read-through (ela-3-5-readers-theater-and-fluency) | **Partly.** The register cast sits under "Class mode or extras (optional)". Rule 4: make it a core solo round before the code goes on the module | L.5.3 a (Sentence Buff) |
| 9 | cooler-challenge (science-6-thermal-energy) | MS-PS3-5, whole | half-pipe-energy (science-8-kinetic-and-potential-energy) | Yes: brake test and friction runs; card updated | MS-PS3-3, MS-PS3-4 |
| 10 | glossary-makers (ela-3-5-academic-and-subject-words) | L.4.5 parts a, b (similes, metaphors, idioms, adages, proverbs) | idiom-illustrator (ela-3-literal-and-figurative-language) | Yes: grade 4 deck. Module grade becomes 3-4 (see Catalog fixes) | L.4.5 c (synonym and opposite per entry) and 7 other codes |
| 11 | idiom-illustrator (ela-3-literal-and-figurative-language) | L.3.4 parts b, c (affixes, roots) | syllable-surgeon (ela-3-multisyllable-decoding) | **Partly.** Its meaning check covers prefixes and suffixes (b). Root words (c: company, companion) have no step yet; the card was not updated. Add a root-family step at spec | L.3.4 a, d (context, glossary), L.3.5, RL.3.4 |
| 12 | meet-the-book-makers (ela-k-all-about-books) | RI.K.4, whole | vocabulary-jar (ela-k-2-new-words-from-read-alouds) | Yes: fact books in the jar; card has the line | RI.K.2, 3, 5, 6, 7 |
| 13 | sentence-train (ela-k-words-and-sentences) | L.K.6, whole | vocabulary-jar (same) | Yes: "Describe it" round reuses jar words | L.K.1, L.K.2 |
| 14 | sentence-train (same) | L.K.1 part a (print letters) | letter-lanterns (ela-k-letter-sounds-and-sight-words) | **Partly.** Tracing is under "Class mode or extras (optional)". Make tracing a core solo step (rule 4). No module change: L.K.1 stays on sentence-train | L.K.1 b-f, L.K.2 |
| 15 | piggy-bank-planner (social-studies-2-money-saving-and-trade) | D2.Eco.14.K-2, whole | pen-pal-parcels (social-studies-2-pen-pal-parcels) | Yes: each letter says why the country sells and buys. Card needs a D2.Eco.14 standards line | D2.Eco.5, 9, 10 |
| 16 | rights-match (social-studies-5-the-constitution-and-bill-of-rights) | D2.Civ.5.3-5, whole | bill-to-law-board-game (social-studies-4-state-government) | **Partly.** Code is already on the target module. The state constitution card is there; the federal-vs-state contrast card the move relies on (D2.Civ.5 names the U.S. Constitution) is not. Add it at spec | D2.Civ.3, 4, 8 |
| 17 | shape-family-tree (math-3-quadrilaterals) | 3.G.A part 3.G.2 (equal areas) | tile-the-floor (math-3-area) | Yes: painters job splits a floor into equal-area parts named 1/4 | 3.G.A (3.G.1) |
| 18 | town-council (social-studies-2-community-helpers-and-government) | D2.Civ.11.K-2, whole | playground-rules (social-studies-k-rules-and-responsibilities) | Yes: "Deciding together" step. Card needs a standards line | D2.Civ.1, 5, 9, 10 |
| 19 | town-council (same) | D4.8.K-2, whole | playground-rules (same) | Yes: listen, build agreement, vote on a swing rule. Card needs a standards line | as row 18 |
| 20 | turn-and-talk-wheel (ela-k-talk-it-over) | SL.K.5, whole | show-and-tell-spotlight (ela-k-2-show-and-tell) | Yes: drawing added to the description; card has the line | SL.K.1, SL.K.2, SL.K.6 |
| 21 | who-said-that (ela-1-who-is-telling-the-story) | RL.1.9, whole | alike-and-different-books (ela-k-2-comparing-two-books) | Yes: grade 1 two characters' adventures; card has the line | RL.1.6 |
| 22 | windblown-pages (ela-k-2-pictures-and-words-together) | RI.2.5, whole | text-feature-makeover (ela-1-text-features) | Yes: grade 2 level (bold words, subheadings, index, menu). Module grade becomes 1-2 | 7 codes |
| 23 | word-thermometer (ela-6-connotation-and-context) | L.6.4, whole | context-roots-dictionary (ela-6-8-academic-vocabulary-strategies) | Yes: grade 6 level; card has the line | L.6.5, RL.6.4, RI.6.4 |
| 24 | go-along (social-studies-12-social-psychology-and-mental-health) | APA.Mental and Physical Health, whole | mind-map (live) was the first choice | **No.** mind-map is a health tool on the continuum, stigma and helping a friend (NHES.S1, S4, S8). It does not teach psychology's perspectives on disorders, their classification or a comparison of treatment approaches. Adding the code would claim more than the live tool teaches, so the card's fallback applies: new tool P4 | APA.Sociocultural |

Row 24 goes to a new tool (P4) and is counted with the new-tool moves below.

### Dropped (another tool already teaches the code)

| # | Source tool | Code | Already taught by |
|---|---|---|---|
| 25 | meet-the-book-makers | RI.K.1 | question-cube (K picture-proof questions) |
| 26 | turn-and-talk-wheel | SL.K.3 | class-phone-call (K asks a caller to repeat or explain) |
| 27 | turn-and-talk-wheel | SL.K.4 | show-and-tell-spotlight (describing with detail stars) |

### To a new tool

| # | Source tool (module) | Code | New tool (see New tools) | Source keeps |
|---|---|---|---|---|
| 28 | sentence-train | L.K.4, whole | E1 Word Meaning Yard | L.K.1, L.K.2 |
| 29 | sentence-train | L.K.5, whole | E1 (merged with row 28) | |
| 30 | word-zoo (ela-1-grammar-basics) | L.1.2, whole | E2 Postcard Writer | L.1.1 |
| 31 | comma-chameleon | L.5.1, whole | E3 Tense Time-Line | L.5.2 a-d |
| 32 | pause-and-break (ela-6-8-commas-dashes-and-ellipses) | spelling parts L.6.2b, L.7.2b, L.8.2c | E4 Tricky Word Lab | L.6.2a, L.7.2a, L.8.2 a-b (punctuation) |
| 33 | pizza-party (math-1-halves-and-fourths) | 1.G.A parts 1.G.1, 1.G.2 | M1 Picky Robot Shapes | 1.G.3 |
| 34 | area-model-builder (math-4-multi-digit-multiplication-and-division) | 4.NBT.B part 4.NBT.4 | M2 Road Trip Logbook | 4.NBT.5, 4.NBT.6 |
| 35 | unit-ladder (math-4-measurement-conversions) | 4.MD.A part 4.MD.3 | M3 Community Plot Planner | 4.MD.1, 4.MD.2 |
| 36 | shrink-ray (math-5-multiplying-and-dividing-fractions) | 5.NF.B parts 5.NF.3, 5.NF.7 | M4 Camp Cook Share-Out | 5.NF.4 to 5.NF.6 |
| 37 | net-folder (math-6-area-surface-area-and-volume) | 6.G.A, rest of 6.G.1 | M5 Sign Shop | 6.G.2 to 6.G.4 |
| 38 | hot-air-and-sandbags (math-7-operations-with-rational-numbers) | 7.NS.A part 7.NS.2d | M6 Remainder Loop | 7.NS.1, 7.NS.2 a-c, 7.NS.3 |
| 39 | blueprint-studio (math-7-scale-drawings-and-constructions) | 7.G.A part 7.G.3 | M7 Clay Cutting Bench | 7.G.1, 7.G.2 |
| 40 | big-wheel-small-wheel (math-7-circles-angles-area-and-volume) | 7.G.B part 7.G.5 | M8 Intersection Angles | 7.G.4 |
| 41 | big-wheel-small-wheel (same) | 7.G.B part 7.G.6 | M9 Aquarium Builder | 7.G.4 |
| 42 | erosion-table (science-4-weathering-and-erosion) | 4-ESS2-2, whole | S1 World Layers Map | 4-ESS2-1 |
| 43 | shadow-clock (science-5-sun-stars-and-shadows) | 5-ESS1-1, whole | S2 Star Lanterns | 5-ESS1-2 |
| 44 | plate-puzzle (science-6-plate-tectonics) | MS-ESS2-1, whole | S3 Rock Recycler | MS-ESS2-3 |
| 45 | plate-puzzle (same) | MS-ESS2-2, whole | S3 (merged with row 44) | |
| 46 | raindrop-s-journey (science-6-water-cycle-and-weather) | MS-ESS2-5, whole | S4 Front Line | MS-ESS2-4 |
| 47 | molecule-builder (science-7-atoms-and-molecules) | MS-PS1-3, whole | S5 Made From | MS-PS1-1 |
| 48 | wave-tank (science-8-waves) | MS-PS4-3, whole | S6 Copy of a Copy | MS-PS4-1, MS-PS4-2 |
| 49 | gene-pool (science-8-reproduction-and-heredity) | MS-LS1-4, whole | S7 Flower Lure | MS-LS1-5, MS-LS3-1, MS-LS3-2, MS-LS4-5 |
| 50 | bug-hunt (science-8-evolution-and-natural-selection) | MS-LS4-1, MS-LS4-2, MS-LS4-3, whole | S8 Fossil and Bone Bench | MS-LS4-4, MS-LS4-6 |
| 51 | hazard-forecaster (science-8-natural-hazards-and-human-impact) | MS-ESS3-3, MS-ESS3-4, whole | S9 Town Footprint | MS-ESS3-2 |
| 52 | hazard-forecaster (same) | MS-ESS3-5, whole | S10 Warming Evidence Desk | MS-ESS3-2 |
| 53 | fed-chair (social-studies-12-money-and-the-federal-reserve) | D2.Eco.9.9-12, whole | P1 Two Villages | D2.Eco.12 |
| 54 | train-your-dog (social-studies-12-learning-and-development) | APA.Development and Learning, lifespan half | P2 One Life, Many Stages | learning half (code stays) |
| 55 | go-along | APA.Individual Variations, whole | P3 Trait Lab | APA.Sociocultural |
| (24) | go-along | APA.Mental and Physical Health, whole | P4 Case Conference | as above |

Rows 24 and 28 to 55 are 29 moves; rows 28 and 29 become one tool (E1) and rows 44 and 45 one tool (S3), giving 27.

### Does each source keep enough to teach?

Yes for all 43 source tools. None is left with nothing. The thinnest after the moves keep one full code and a whole
loop: who-said-that (RL.1.6), plate-puzzle (MS-ESS2-3), hazard-forecaster (MS-ESS3-2), raindrop-s-journey
(MS-ESS2-4), shadow-clock (5-ESS1-2), molecule-builder (MS-PS1-1), erosion-table (4-ESS2-1), fed-chair (D2.Eco.12),
go-along (APA.Sociocultural). Their module titles need trimming (Catalog fixes, item 4).

## New tools

27 new tools from the moves after merging duplicates (L.K.4 and L.K.5 are one tool; MS-ESS2-1 and MS-ESS2-2 are one;
MS-ESS3-3 and MS-ESS3-4 are one; MS-LS4-1 to 3 are one). 7.G.5 and 7.G.6 stay two tools: they are different skills,
not duplicates, and rule 1 never merges only to save work. No existing module carries any of these codes besides the
source (checked code by code), so none can go to an existing tool instead.

Each entry gives the concept line (`module_id|title|format|family|concept`), then the module line
(`grade|course|strand|title|description|standards`). Overlap risks are named for the phase 2 judges.

### ELA

**E1.** `ela-k-word-meanings-and-word-play|Word Meaning Yard|sort||Sort farmyard pictures by meaning (a duck and a boy who ducks), add -ed, -s, re- and un- to change a word, pair opposites, find words at home, and act out walk, march and strut to feel shades of meaning.`
`k|ela-k12|Language|Word Meanings and Word Play|Multiple-meaning words, endings and prefixes, sorting, opposites and shades of verbs|L.K.4;L.K.5`

**E2.** `ela-1-capitals-punctuation-and-spelling|Postcard Writer|builder||Write postcards from a class trip: capitalize names and dates, add end marks, put commas in dates and lists, and spell words by common patterns; the mail carrier delivers a card only when it is right, and the friend's reply shows what was read.`
`1|ela-k12|Language|Capitals, Punctuation and Spelling|Capital dates and names, end marks, commas in dates and lists, spelling patterns|L.1.2`

**E3.** `ela-5-verb-tense-and-conjunctions|Tense Time-Line|puzzle||Events slide on a story track; pick the verb that fits each spot (had finished, will have finished, was running), fix tense shifts that scramble the order, see what conjunctions, prepositions and interjections do, and join ideas with either/or and neither/nor.`
`5|ela-k12|Language|Verb Tense and Conjunctions|Perfect tenses, tense shifts, correlative conjunctions, prepositions and interjections|L.5.1`
Note: L.5.1a (function of conjunctions, prepositions, interjections) is in the line so the whole code is taught.

**E4.** `ela-6-8-spelling-through-word-families|Tricky Word Lab|lab||Solve commonly misspelled words through roots and word families (definite from finite, separate from par), test a spelling rule against a word list, and keep a personal tricky-words list that comes back for review.`
`6-8|ela-k12|Language|Spelling Through Word Families|Spell correctly using roots, word families and patterns|L.6.2;L.7.2;L.8.2`
Privacy line for the saved list (rule 7). Overlap risk: context-roots-dictionary (roots for meaning, not spelling).

### Math

**M1.** `math-1-shapes-and-their-attributes|Picky Robot Shapes|builder||Compose pictures from flat shapes and from solids (cubes, cones, cylinders), then help a picky robot that accepts only true triangles and squares whatever their color, size or turn, and reuse a shape you built to make a bigger one.`
`1|math-k8|Geometry|Shapes and Their Attributes|Defining and non-defining attributes; composing flat and solid shapes|1.G.A`
Overlap risk: pattern-block-pond (K.G.B, composing at K).

**M2.** `math-4-adding-and-subtracting-multi-digit-numbers|Road Trip Logbook|simulator||Log a family road trip's mileage in columns: add each day's miles and subtract to find what is left, regroup like an odometer rolling over, and check each answer with an estimate.`
`4|math-k8|Number and Operations in Base Ten|Adding and Subtracting Multi-Digit Numbers|Fluently add and subtract with the standard algorithm|4.NBT.B`

**M3.** `math-4-area-and-perimeter-formulas|Community Plot Planner|builder||Lay out a community garden where each family's plot has a set area or fence length, find the missing side (a 48 square foot plot that is 6 feet wide), and see why the formulas work.`
`4|math-k8|Measurement and Data|Area and Perimeter Formulas|Apply area and perimeter formulas for rectangles in real problems|4.MD.A`
Overlap risk: garden-grid (grade 2) by look only; title avoids "garden".

**M4.** `math-5-fractions-as-division|Camp Cook Share-Out|simulator||Share pans and scoops at camp: 3 pans for 4 tables gives each 3/4 of a pan, half a pan splits among 3 tables, and the cook counts quarter-cup scoops in 2 cups, so fractions are division and dividing by a unit fraction makes sense.`
`5|math-k8|Number and Operations - Fractions|Fractions as Division|A fraction as division; dividing unit fractions and whole numbers|5.NF.B`
Overlap risk: how-many-fit (grade 6 fraction division; may share fraction-wall bars).

**M5.** `math-6-area-of-polygons|Sign Shop|puzzle||Price the paint for odd-shaped signs by cutting and sliding pieces: a parallelogram becomes a rectangle, a trapezoid becomes two triangles and a rectangle, and composite signs split into shapes you know.`
`6|math-k8|Geometry|Area of Polygons|Area of triangles, parallelograms, trapezoids and composite polygons by composing and decomposing|6.G.A`
Uses the inclusive trapezoid (Catalog fixes, item 3).

**M6.** `math-7-terminating-and-repeating-decimals|Remainder Loop|lab||Divide 1 by 7 the long way and watch the remainders cycle, then try other fractions and find out why every fraction's decimal must end or repeat.`
`7|math-k8|The Number System|Terminating and Repeating Decimals|Long division shows a rational number's decimal ends or repeats|7.NS.A`
Engine could later serve square-root-hunt's repeating-decimal part (overlap risk, light).

**M7.** `math-7-cross-sections-of-solids|Clay Cutting Bench|lab||Slice clay prisms and pyramids with a wire at different angles and predict each cut face before it opens.`
`7|math-k8|Geometry|Cross Sections of Solids|Plane sections of right rectangular prisms and pyramids|7.G.A`
Overlap risk: slice-and-stack (grade 10, specced, G-GMD cross sections). Keep this one to prediction of plane sections.

**M8.** `math-7-angle-relationships|Intersection Angles|puzzle||Find missing angles at a busy intersection where crossing streets, rail crossings and scissor gates make vertical, adjacent, supplementary and complementary angles, writing and solving an equation for each.`
`7|math-k8|Geometry|Angle Relationships|Supplementary, complementary, vertical and adjacent angles in equations|7.G.B`

**M9.** `math-7-surface-area-and-volume-of-prisms|Aquarium Builder|builder||Plan composite prism tanks and planter boxes: buy the glass (surface area) and fill the water (volume) for shapes built from cubes and right prisms.`
`7|math-k8|Geometry|Surface Area and Volume of Prisms|Area, volume and surface area of composite figures of polygons, cubes and right prisms|7.G.B`

### Science

**S1.** `science-4-earth-features-on-maps|World Layers Map|map||Turn on world map layers (mountains, ocean trenches, volcanoes, earthquakes, ocean depth) and find that they line up in patterns, like the ring around the Pacific; the plate explanation waits for grade 6.`
`4|science-k5|Earth and Space Science|Earth's Features on Maps|Patterns of mountains, trenches, volcanoes and earthquakes from maps|4-ESS2-2`

**S2.** `science-5-star-brightness|Star Lanterns|lab||Carry identical lanterns farther and farther across a dark field and measure how dim they look, then find that the sun looks brightest only because it is the closest star.`
`5|science-k5|Earth and Space Science|Star Brightness|The sun's apparent brightness compared with other stars depends on distance|5-ESS1-1`

**S3.** `science-6-rock-cycle-and-changing-surface|Rock Recycler|simulator||Follow one mineral grain through melting, cooling, weathering, burial and uplift, powered by the sun and Earth's inner heat, with each step on its real clock, from a landslide in seconds to uplift over millions of years.`
`6|science-ms|Earth and Space Science|Rock Cycle and Earth's Changing Surface|Cycling of Earth's materials; geoscience processes at many time and space scales|MS-ESS2-1;MS-ESS2-2`

**S4.** `science-6-air-masses-and-weather|Front Line|data|weather|Collect readings from a row of weather stations as a cold air mass meets a warm one, then use the data to forecast tomorrow's weather.`
`6|science-ms|Earth and Space Science|Air Masses and Weather|How moving and interacting air masses change the weather|MS-ESS2-5`
Family weather only if it shares the engine with weather-wardrobe and climate-postcards; otherwise blank.

**S5.** `science-7-synthetic-materials|Made From|explorer||Trace an everyday synthetic material (a nylon jacket, a plastic bottle, a medicine) back to the natural resource it came from and forward to its effects on society.`
`7|science-ms|Physical Science|Synthetic Materials|Synthetic materials come from natural resources and affect society|MS-PS1-3`

**S6.** `science-8-analog-and-digital-signals|Copy of a Copy|lab||Send the same message as a smooth analog wave and as digital pulses through a chain of noisy relays, and see which arrives intact.`
`8|science-ms|Physical Science|Analog and Digital Signals|Digitized signals are a more reliable way to send information|MS-PS4-3`
Overlap risk: secret-code-signals (grade 4, 4-PS4-3 patterns that carry information).

**S7.** `science-8-behaviors-and-structures-for-reproduction|Flower Lure|builder||Design a flower's color, scent, shape and nectar to win visits from a chosen pollinator, then compare animal behaviors (songs, nest building, guarding young) that raise the odds of reproducing.`
`8|science-ms|Life Science|Behaviors and Structures for Reproduction|Animal behaviors and plant structures that raise the odds of reproducing|MS-LS1-4`

**S8.** `science-8-evidence-of-common-ancestry|Fossil and Bone Bench|lab||Order fossils through rock layers to find patterns of change, compare limb bones (a whale flipper, a bat wing, a human arm), and compare early embryos across species.`
`8|science-ms|Life Science|Evidence of Common Ancestry|Fossil record, anatomical similarities and embryo development|MS-LS4-1;MS-LS4-2;MS-LS4-3`
Overlap risk: fossil-clues (grade 3, 3-LS4-1). Different depth; keep with a note likely.

**S9.** `science-8-human-impact-on-earth|Town Footprint|simulator||Watch a town's water, land and energy use grow with its population and spending, then design a way to monitor and shrink one impact.`
`8|science-ms|Earth and Space Science|Human Impact on Earth|Growth in population and consumption raises impacts; designing ways to monitor and reduce them|MS-ESS3-3;MS-ESS3-4`
Overlap risk: up-the-watershed and lake-commons (both 9-12).

**S10.** `science-8-evidence-of-rising-temperatures|Warming Evidence Desk|data||Ask questions of real records (temperature, carbon dioxide, the sun's output, volcanoes) to sort out which factors explain the rise in global temperature over the past century.`
`8|science-ms|Earth and Space Science|Evidence of Rising Temperatures|Factors behind the rise in global temperature over the past century|MS-ESS3-5`
Overlap risk: climate-dashboard (grade 9, HS-ESS3-5). Data source needed (NOAA, NASA records).

### Social studies and psychology

**P1.** `social-studies-12-property-rights-and-the-rule-of-law|Two Villages|simulator||Farm in one of two villages, one with registered land titles and fair courts and one without, decide whether to plant an orchard, lend or start a shop, and see why secure rights and contracts change what people dare to build.`
`12|economics|Economics|Property Rights and the Rule of Law|How institutions such as property rights and the rule of law shape a market economy|D2.Eco.9.9-12`

**P2.** `social-studies-12-lifespan-development|One Life, Many Stages|timeline||Follow one person from infancy to old age through real developmental research (attachment, Piaget's stages, adolescence, aging), predicting each stage before the research shows it.`
`12|psychology|Psychology|Lifespan Development|Physical, cognitive and social development from infancy to old age|APA.Development and Learning`

**P3.** `social-studies-12-personality-intelligence-and-motivation|Trait Lab|lab||Compare trait theories of personality, ideas of intelligence and theories of motivation with the real measures behind them, take sample items, and find what each measure can and cannot tell you.`
`12|psychology|Psychology|Personality, Intelligence and Motivation|Theories and measures of personality, intelligence and motivation, and their limits|APA.Individual Variations`
Rule 7 line if any answers are stored.

**P4.** `social-studies-12-psychological-disorders-and-treatment|Case Conference|roleplay||Sit on a clinic team with fictional case summaries: look at each through the biological, psychological and social lenses, see how disorders are classified, compare treatments by their research evidence, and trace how stress affects health; support resources stay on every screen.`
`12|psychology|Psychology|Psychological Disorders and Treatment|Perspectives on disorders, classification, treatment approaches, stress and health|APA.Mental and Physical Health`
Sensitive (fresh review, rule 5; teacher note, rule 8). Overlap risk: mind-map (live). Keep mind-map on stigma and helping a friend; this one on the science of disorders and treatment.

All 27 are concept-pipeline entries for a later spec wave (rule 10). Grade 7 math gains 4 tools and grade 8 science 5;
the scale plan may want to spread them across waves.

## Uncovered codes

### The 41 CCSS-ELA codes

The gap fill (docs/agents/gapfill/REPORT.md) left all 41 out by design: RL.10 and RI.10 as "a program, not a tool
skill", W.10 as routine writing, W.6 because "every writing tool on the site is digital". This audit's brief asks for a
home for each, and BASELINE rules 2 and 10 lean toward teaching them. The reason given for W.6 is also weak on its own
terms: W.6 asks for keyboarding stamina (grade 3), typing one, two and three pages in a sitting (grades 4 to 6),
linking and citing sources (grades 7 and 8) and updating shared writing in response to feedback (9-12), and no writing
tool in the catalog teaches any of those. No existing tool can take these codes without a thin add-on (rule 2), so each
band gets its own new tool. Eight tools in all; each needs the K-2 or band span check (gf-04).

**W.6 and W.10, four tools (19 codes):**

**R1.** `ela-k-2-publishing-with-digital-tools|Little Book Press|studio||Make a picture book on screen: draw or stamp each page, record or type the words, then publish it as a printable book and a screen book; a partner mode passes pages between two kids at one device.`
`k-2|ela-k12|Writing|Publishing with Digital Tools|Explore digital tools to produce and publish writing, alone and with a partner|W.K.6;W.1.6;W.2.6`

**R2.** `ela-3-5-typing-publishing-and-writing-routines|Deadline Desk|studio||Run the class paper: keyboarding warm-ups grow into typing a whole piece in one sitting (a page at grade 4, two at grade 5), each issue mixes quick single-sitting pieces with a long feature built over several sessions, and the finished issue is published.`
`3-5|ela-k12|Writing|Typing, Publishing and Writing Routines|Keyboarding, producing and publishing with technology; writing over short and extended time frames|W.3.6;W.4.6;W.5.6;W.3.10;W.4.10;W.5.10`

**R3.** `ela-6-8-writing-and-publishing-online|Linked Feature|studio||Build a web feature: type at least three pages in a sitting, link to and cite each source, show how ideas connect in a linked diagram, answer an editor's comments, and keep a routine of daily quick-writes and one long piece over weeks.`
`6-8|ela-k12|Writing|Writing and Publishing Online|Produce and publish with links and citations; collaborate; write routinely|W.6.6;W.7.6;W.8.6;W.6.10;W.7.10;W.8.10`

**R4.** `ela-9-12-publishing-and-updating-writing|Living Explainer|studio||Publish an explainer on a changing question, then new findings and reader comments arrive over the following weeks; update the piece, link and display the evidence flexibly, keep a change log, and write timed single-sitting responses along the way.`
`9-12|ela-k12|Writing|Publishing and Updating Writing|Produce, publish and update writing in response to feedback and new information; write routinely|W.9-10.6;W.11-12.6;W.9-10.10;W.11-12.10`

All four save drafts on the device and say so (rule 7). Collaboration is with illustrated co-writers by default and a
real partner as the extra (rule 4).

**RL.10 and RI.10, four tools (22 codes).** Each pairs literature and informational texts at the band's complexity, a
stretch text at the top of the band with supports the student switches off one at a time, and a range map of what was
read (on the device). Texts can come from data/library/stories-pd.csv and other checked public-domain sources.

**R5.** `ela-k-2-reading-range|Read-Along Shelf|explorer||A shelf of stories, poems and fact books: kindergarten joins read-alouds with a purpose question for each, grades 1 and 2 read along with help that fades page by page, and a range map shows the kinds of texts read.`
`k-2|ela-k12|Reading Literature|Reading Range and Text Complexity|Read stories, poems and fact books at grade level with fading support|RL.K.10;RL.1.10;RL.2.10;RI.K.10;RI.1.10;RI.2.10`

**R6.** `ela-3-5-reading-range|Stretch Shelf|explorer||Choose stories, poems, plays and fact texts at your grade, read a stretch text with supports (word taps, chunk recaps, audio) you switch off one at a time, check understanding at each chunk, and fill a range map across genres and subjects.`
`3-5|ela-k12|Reading Literature|Reading Range and Text Complexity|Read literature and informational texts at the top of the grade band, with fading scaffolds|RL.3.10;RL.4.10;RL.5.10;RI.3.10;RI.4.10;RI.5.10`

**R7.** `ela-6-8-reading-range|Climbing Reads|explorer||Climb from grade-level to top-of-band texts in fiction, poetry, drama, history, science and technical writing, using supports you remove one by one, with a check after each section and a range map of what you read.`
`6-8|ela-k12|Reading Literature|Reading Range and Text Complexity|Read literature and literary nonfiction at the grade band, independently at the top|RL.6.10;RL.7.10;RL.8.10;RI.6.10;RI.7.10;RI.8.10`

**R8.** `ela-9-12-reading-range|Tough Text Club|explorer||Take on a ladder of complex texts (a founding document, a scientific article, a nineteenth-century novel chapter, a poem), plan how to read each, drop the supports one at a time, and track the range you have read.`
`9-12|ela-k12|Reading Literature|Reading Range and Text Complexity|Read complex literature and informational texts independently and proficiently|RL.9-10.10;RL.11-12.10;RI.9-10.10;RI.11-12.10`

If the orchestrator prefers to keep the gap fill's "by design" exclusion for any of these, record the reason here and
in gapfill/REPORT.md so the two documents agree.

### Other codes below full

coverage.py measures every listed framework full except CCSS-ELA. Two lists in data/standards are not measured by it:

- **WRS.Connections** (World-Readiness 3.1, 3.2) is on no module; the other four goal areas are. Add it to
  debate-en-español (world-languages-9-12-current-events-and-debate): its dossier of Spanish news texts and residents'
  voices already has the student acquire information and diverse perspectives through the language (3.2), and the
  city-planning question carries another discipline (3.1). Below grade 9 it stays uncovered; mundo-hispano could take
  3.2 at spec if it is split (it is flagged too big).
- The ACTFL, APA, CTE and AP codes print as "outside every list" because coverage.py has no grid for them. A grid would
  make the next audit catch holes like WRS.Connections automatically.

## Band holes

Cells (code x band) whose only carrier spans several bands. All are world languages or PE; no core-subject code is
held only by a span tool.

| Code | Bands held only by span tools | Tools |
|---|---|---|
| ACTFL.Novice Low | K-2, 3-5, 6-8, 9-12 | fingerspell-flash (live), asl-hello-booth, hola-hallway, calendario-vivo (all K-12) |
| ACTFL.Novice Mid | all four | asl-bingo-night, sign-parameters-lab, mi-casa, mi-día (K-12) |
| ACTFL.Novice High | all four | asl-family-tree, el-restaurante (K-12) |
| WRS.Communication | K-2, 3-5, 6-8 | fingerspell-flash, asl-hello-booth, hola-hallway (K-12) |
| WRS.Comparisons | K-2, 3-5 | sign-parameters-lab (K-12) |
| WRS.Comparisons | 6-8, 9-12 | face-the-grammar (6-12), sign-parameters-lab |
| ACTFL.Intermediate Low | 6-8, 9-12 | face-the-grammar, por-dónde, verb-conjugation-race (6-12) |
| ACTFL.Intermediate Mid | 6-8, 9-12 | classifier-scenes (live), detective-del-pasado, mundo-hispano (6-12) |
| WRS.Cultures | 6-8, 9-12 | deaf-culture-explorer, mundo-hispano (6-12) |
| WRS.Communities | 6-8 | deaf-culture-explorer (6-12) |
| SHAPE.S3 | 6-8 | partner-skill-coach (6-12) |
| SHAPE.S1 | 9-12 | partner-skill-coach (6-12) |
| WIDA.Narrate | 6-8, 9-12 | then-what-happened (6-12, specced) |

How each is handled (rule 1, gf-04):

- **K-12 Novice tools (9 idea cards plus live fingerspell-flash).** ACTFL levels are proficiency, not grade, so one
  module per level is right. But a K child is a pre-reader and a teen beginner is not. Each spec must give a young path
  (audio and picture led, no reading needed, kid characters) and a teen path, and show both at full depth. Where a spec
  cannot, split into a K-5 tool and a 6-12 tool with the same codes. Likely splits, judged from the cards:
  - **el-restaurante** and **asl-family-tree** (the only Novice High carriers) lean on reading a menu and on a teen's
    school project; a K-2 path is doubtful. If either splits, its young half needs a new concept line.
  - **sign-parameters-lab** (written conclusions, minimal pairs) is the only WRS.Comparisons carrier below grade 6. A
    young picture version, or a re-band to 3-12, needs another K-2 carrier for WRS.Comparisons.
  - fingerspell-flash is live and does not move; review its young path at its next revision.
- **6-12 tools.** Intermediate levels at 6-12 are fine if each spec sets middle-school and high-school content (the
  idea cards already use teen settings). then-what-happened's spec already states the reason (proficiency, not grade,
  with three help levels); no change.
- **partner-skill-coach.** The only carrier of SHAPE.S1 at 9-12 and SHAPE.S3 at 6-8. Its clips are throwing, kicking
  and shooting, which fit 6-8 motor skills. For 9-12 depth the spec should add lifetime-activity skills (a tennis
  serve, a golf swing), or SHAPE.S1 at 9-12 needs another tool.
- **K-2 and 3-5 spans inside one band** are not band holes, but the idea pass flagged bedtime-retell and
  i-choose-because for the K-2 check, and the 8 new range tools above span a band; each builder confirms every grade.

## Catalog fixes

1. **Module titles that no longer match their tool** (modules named after the tool; none of these tools is live or
   specced, so ids can change, with data/redirects.csv if needed):
   - social-studies-4-bike-fund-chances, "Bike Fund Chances" -> "Skateboard Fund Chances" (tool skateboard-fund-chances).
   - social-studies-11-behind-the-documentary, "Behind the Documentary" -> "Behind the Podcast" (tool behind-the-podcast).
   - social-studies-8-voices-on-the-vote, "Voices on the Vote" -> "Who Gets to Vote?" (tool who-gets-to-vote, renamed
     from voices-on-the-vote). Found by this audit; not in the idea pass log.
2. **One-tool families.** silk-road (silk-road-traders) has one tool: drop the tag. The same holds for 14 more:
   arrays, big-book, choose-path, clock, elements, folktales, graphs, history-overlay, letter-pals, library,
   lit-timeline, pattern-blocks, state-quest, ten-frame. Drop each unless a sibling is planned. market-day already
   left the market family (ss-1).
3. **Trapezoid: one definition, inclusive** (at least one pair of parallel sides, so a parallelogram is a trapezoid),
   with a teacher note naming the exclusive one:
   - shape-courtroom: rulebook inclusive (its card already recommends this).
   - shape-family-tree: leaves trapezoids out on purpose. If they come back, inclusive; either way its teacher note
     states the site's definition.
   - **coordinate-proof-lab (specced) disagrees today**: its spec defaults to exclusive with an `inclusive` switch and
     an open question. Set the default to inclusive, keep the switch, and update P3 and the name board (a
     parallelogram also lights Trapezoid).
   - Sign Shop (M5) and net-folder: inclusive. pattern-block-pond, definition-duel and live shape-talk show only shapes
     that are trapezoids under both definitions; no change.
4. **Module titles and descriptions after the moves:**
   - ela-5-conjunctions-tense-and-commas: "Conjunctions, Tense and Commas" -> "Commas and Titles"; description
     "Commas in series, after introductions, with yes, no and direct address; marking titles".
   - math-5-multiplying-and-dividing-fractions -> "Multiplying Fractions"; description "Fraction multiplication as scaling".
   - math-6-area-surface-area-and-volume -> "Nets, Surface Area and Volume"; drop "Area of polygons" from the description.
   - math-7-circles-angles-area-and-volume -> "Circles"; description "Circumference and area of circles".
   - science-5-sun-stars-and-shadows -> "Sun and Shadows"; description "Daily and seasonal patterns of shadows, day and night, and the sky".
   - science-6-water-cycle-and-weather -> "Water Cycle"; description "Water cycling through Earth's systems".
   - science-8-natural-hazards-and-human-impact -> "Natural Hazards"; description "Forecasting hazards and reducing their effects".
   - social-studies-12-social-psychology-and-mental-health -> "Social Psychology"; description "Conformity, obedience, bystanders and research ethics".
   - social-studies-12-learning-and-development -> "Learning"; description "Classical, operant and observational learning". (The code stays: it is shared with P2.)
   - social-studies-k-needs-and-wants: description "Basic needs; jobs people do" -> "Needs and wants; choosing what to keep".
5. **Module grade changes:** ela-1-text-features 1 -> 1-2 (takes RI.2.5); ela-3-literal-and-figurative-language
   3 -> 3-4 (takes L.4.5). Both ids carry the old grade; rename or keep by the catalog's id rule.
6. **Module code adds and removals** that the moves imply are in the Code moves tables; one add is not a move:
   D2.Geo.11.3-5 onto social-studies-4-state-economy-and-resources.
7. **Idea cards to update before spec** (target cards that do not yet show the incoming code in full): syllable-surgeon
   (L.3.4 roots step), script-read-through (register round in the solo path), letter-lanterns (tracing as a core step),
   bill-to-law-board-game (federal-vs-state card for D2.Civ.5), settle-the-valley, pen-pal-parcels and
   playground-rules (standards lines for D2.Geo.9, D2.Eco.14, D2.Civ.11 and D4.8).

# Energy Pyramid

## One idea
On a grassland with the sun overhead, grass, grasshoppers, mice, snakes and hawks, the student builds an energy pyramid one level at a time, starting with 10,000 energy units in the grass; for each level the student decides how many animals the level below can feed, and wavy heat arrows leave every level (moving, keeping warm, waste) so the counter drops, with the share passed up varying between levels (roughly 5 to 20 percent, about a tenth on average); trying a fifth level leaves only about 1 unit, not enough to feed even one animal; then a matter view switches to atoms, and droppings and dead bodies go to decomposers (worms, fungi, bacteria), into soil and air, and back into grass, with an atom counter that never drops, while energy must keep arriving from the sun; at the end the two views sit side by side, so a seventh grader learns to develop a model that describes the cycling of matter and the flow of energy among the living and nonliving parts of an ecosystem.

## Not like
- predator-prey-island (7, spec): two populations over time, same family. Here energy and matter per level.
- food-web-wobble (5, concept): who eats whom, no numbers, same family. Here how much moves up.
- leaf-factory (7, spec): one plant's matter and energy. Here a whole grassland.
- wolf-pack-survival (3, spec): one pack's needs. Here why top predators are few.

## Who and how
- Grade 7, Science, module "Matter and Energy in Ecosystems". Standard: MS-LS2-3 (develop a model to describe the cycling of matter and flow of energy among living and nonliving parts of an ecosystem).
- Format: builder. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Five levels with one species each, the energy counter, heat arrows, the share for each step (stated per level), the matter view with four decomposer paths and an atom counter, the side-by-side card. Extra: Ocean pyramid (the same build with plankton, krill, fish, seals, orcas). tool.json `modes: ["Grassland", "Ocean pyramid"]`, `minutes: "20-30"`, `grades_label: "Grade 7"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-LS2-3 (energy flow) | Stack levels, feed each from the one below and try a fifth | the counter; heat arrows; the shrinking pyramid | 2 |
| MS-LS2-3 (matter cycling) | Route droppings and bodies through decomposers to grass | the atom view; the atom counter | 3 |
| MS-LS2-3 (living and nonliving) | Compare both views and label soil, air and sun | the side-by-side card | 4 |

## Screens and modes
Header (kit): title "Energy Pyramid"; `Grassland`, `Ocean pyramid`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A wide grassland at midday, the sun in the corner, grass rippling. A wooden pyramid frame stands empty with only the bottom level filled with grass and a counter reading 10,000. The welcome is queued (`welcomeAfter: true`): "The grass caught the sun's energy. How much of it can reach a hawk? Drag the grasshoppers onto the next level." First hint: "Drag the grasshoppers onto level 2."

**Energy view (focus: the pyramid).** At 1366x768 the grassland sits left with the pyramid and counter right; at 680x425 the pyramid fills the screen and the grassland is a backdrop strip. Each new level shows the energy passed up and the heat arrows leaving the level below with labels (moving, keeping warm, waste). The student sets how many animals the level can feed with a stepper; too many and some go hungry. Level 2 gets about 1,000, level 3 about 100, level 4 about 10. The fifth level shows about 1 and the card says "Not enough to feed even one animal."

**Matter view (the switch).** The scene turns to atoms: carbon and nitrogen dots. Droppings, fallen grass and dead bodies (shown as leaves and a feather, nothing graphic) go to worms, fungi and bacteria; carbon goes to the air, nitrogen into the soil; grass takes them back up. The student drags each path to complete the loop. The atom counter stays the same the whole time.

**Side by side (the aha).** Two pictures: energy as one-way arrows from the sun out as heat; matter as a circle. The student labels the nonliving parts (sun, air, soil, water). Narrator: "Energy flows through and leaves as heat, so the sun has to keep shining. Matter goes around and around."

**The end.** Both views with labels and counts. `Print` prints them.

**Ocean pyramid (extra).** The same build in the sea.

## Content
- Five grassland species and five ocean species, stated shares per step that average about a tenth, heat labels, four decomposer paths, the atom counter, the side-by-side card.
- A note: "Real shares vary from about 5 to 20 percent. This one uses stated numbers."

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A level can be removed and rebuilt; the counter updates at once.
- Keyboard: Tab to species, levels, steppers, paths and labels; Enter places; arrows step.
- With Motion off heat arrows and atom dots are still.

## Look
- Accent `--brand` #8a5300 prairie amber (header, the pyramid frame, energy arrows); gold #f4c542 (the level in focus, the species in hand); paper #fbf7ee; ink #241a05; muted #5d5546.
- Contrast (WCAG 2.1, computed): white on brand 6.33:1; brand on paper 5.92:1; ink on paper 16.03:1; muted on paper 6.88:1; ink on gold 10.54:1.
- Never color alone: energy and matter arrows differ in shape (wavy one-way, circle) and carry words.
- Different from this batch (spruce, signal magenta, indigo, factory teal).

## Art
- Local FLUX (`scripts/localart.py`): the grassland (1, 16:9), the ocean scene (1, 16:9), five grassland species (5, 1:1), five ocean species (5, 1:1), decomposers in soil (1, 4:3).
- Drawn in code: the pyramid, counters, arrows, atom dots.
About 13 images.

## Voice
Two bank voices, each unique in this batch: `bright-teacher` as the guide; `playful-friend` as a grasshopper on level 2 and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.view + ':' + state.level + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `level`: "Drag the next animal onto the next level."
- how `feed`: "Tap plus or minus to set how many it can feed."
- event, whole, the fifth-level card.
- how `matter`: "Tap Matter, then drag each path to finish the loop."
- how `label`: "Drag a label onto each nonliving part."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
ecosystem. Copies predator-prey-island's `/* ECOSYSTEM ENGINE: begin */ ... /* end */` block unchanged (species records) and adds energy per level and an atom loop, so the block can move to `kit/ecosystem.js` for the whole family.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Feeding | Set every level to the maximum | Hungry animals show and the level won't lock. |
| Loop | Drag paths at random | Each path snaps only to its right partner. |
| Labels | Label everything "sun" | Each label checks its spot. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `level`; `feed`.
2. Fifth-level card (whole), waits.
3. `matter`; `label`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for MS-LS2-3 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| About 10 percent of energy passes between levels, ranging roughly 5 to 20 percent | OpenStax, "Biology 2e", chapter 46 | Lindeman (1942), Ecology, "The trophic-dynamic aspect of ecology" | yes |
| Most energy leaves each level as heat from life processes | OpenStax, "Biology 2e", chapter 46 | National Geographic Education, "Energy pyramid" | yes |
| Decomposers return carbon and nitrogen to air and soil | U.S. Environmental Protection Agency, "Nutrient cycles" (education) | OpenStax, "Biology 2e", chapter 46 biogeochemical cycles | yes |
| Matter cycles while energy flows through ecosystems | OpenStax, "Biology 2e", chapter 46 | National Geographic Education, "Food web" | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad r3, 2026-11-10): 10,000 units at a tenth per step gives 1,000, 100, 10 and 1; everything above the grass adds to less than the grass; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 grassland and pyramid; at 680x425 pyramid with strip.
2. Four levels are built and fed and a fifth shows too little energy. (MS-LS2-3)
3. The matter loop is finished and the atom counter holds steady. (MS-LS2-3)
4. Both views are compared and nonliving parts labeled. (MS-LS2-3)
5. Stated shares average about a tenth and the variation note shows.
6. No graphic death; bodies show as leaves and a feather.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: still arrows and dots; no network requests.

## Open questions
None.

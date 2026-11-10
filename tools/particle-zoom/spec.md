# Particle Zoom

## One idea
On a kitchen counter sit a cup of tea, a sugar cube, a balloon and a pump, a glass of ice, a puddle on a plate and a digital scale, and the student picks one change, watches it at normal size, then drags a zoom slider through a magnifier, a microscope and finally a particle view where each kind of particle is a colored ball: the sugar cube breaks into particles that spread between the water particles until they can't be seen, pumping pushes more air particles into the balloon so they hit its walls harder and more often, the puddle's particles leave one by one into the air, and the ice's packed particles loosen into a liquid; the student explains each change in their own words before a caption appears; at the scale bench they weigh before and after: tea and sugar, ice melting in a sealed bag, and baking soda and vinegar in a capped bottle and then in an open cup, graph the readings, and spot that only the open cup lost weight, because gas escaped into the air; at the end a claim card says matter is made of particles too small to see, and when heating, cooling or mixing, the total weight stays the same, so a fifth grader learns to model matter as particles too small to see, and to measure and graph evidence that weight is conserved.

## Not like
- particle-party (7, concept): phase changes and heating curves, same engine. Here particles and weight at the kitchen counter.
- mystery-powders (5, spec): telling substances apart. Here what all matter is made of.
- melt-or-not (2, live): changes that can be undone. Here what's happening inside the change.
- gas-law-lab (10, spec): pressure and volume math, same engine. Here seeing gas particles push.

## Who and how
- Grade 5, Science, module "Matter Is Made of Particles". Standards: 5-PS1-1 (develop a model to describe that matter is made of particles too small to be seen), 5-PS1-2 (measure and graph quantities to provide evidence that regardless of the type of change that occurs when heating, cooling, or mixing substances, the total weight of matter is conserved).
- Format: explorer. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Four zoom changes with four zoom levels, the scale bench with four weigh-ins, the before-and-after graph, the claim card. Extra: Class zoom (the class predicts what the particle view will show before each zoom). tool.json `modes: ["Counter", "Class zoom"]`, `minutes: "20-30"`, `grades_label: "Grade 5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 5-PS1-1 | Zoom into four changes and explain each in their own words | the particle view | 2 |
| 5-PS1-2 (measure) | Weigh four setups before and after a change | the scale; the readings table | 3 |
| 5-PS1-2 (graph) | Graph before and after and explain the one that changed | the graph; the claim card | 4 |

## Screens and modes
Header (kit): title "Particle Zoom"; `Counter`, `Class zoom`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A kitchen counter with the tea, sugar cube, balloon and pump, a glass of ice, a puddle on a plate and a scale. The welcome is queued (`welcomeAfter: true`): "Where does the sugar go when it disappears? Drop it in the tea, then zoom in. Drag the sugar cube to the cup." First hint: "Drag the sugar cube into the tea."

**Zoom (focus: the zoom window).** At 1366x768 the counter is on the left and the zoom window on the right; at 680x425 the zoom window is full and the counter is a strip. The zoom slider has four stops: normal, magnifier, microscope, particle view. Four changes:
1. Sugar dissolving: the cube breaks into particles that spread among water particles.
2. Pumping a balloon: more air particles inside hit the walls more often, so the balloon swells.
3. A puddle drying: particles at the top leave into the air one at a time.
4. Ice melting: packed particles loosen and slide past each other.
Before each caption, the student picks or writes what they think is happening. A note says real particles are far smaller and more numerous than the balls shown.

**Scale bench (5-PS1-2).** The scale reads to a tenth of a gram. Four weigh-ins:
1. Tea plus a 4-gram sugar cube, before and after dissolving.
2. 100 grams of ice in a sealed bag, before and after melting.
3. 1 gram of baking soda and some vinegar in a capped bottle, before and after fizzing.
4. The same in an open cup.
The table logs each reading; the graph shows before and after bars. Only the open cup drops, by about half a gram.

**The claim card (the aha).** "Matter is made of ___ too small to see. In the open cup, weight was lost because ___." Narrator: "The sugar didn't vanish. It's still there, in pieces too small to see. And nothing disappears: if the weight drops, something got out."

**The end.** The zoom notes, the table, the graph and the claim. `Print` prints them.

**Class zoom (extra).** The class predicts before each zoom.

## Content
- Four changes with stated particle rules, four zoom stops, four weigh-ins with stated amounts, the graph, the claim card.
- A safety card for real-life tries: baking soda and vinegar in a capped bottle only with a grown-up and small amounts.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The zoom slider can be dragged or stepped; the particle view keeps running.
- Keyboard: Tab to counter items, the slider, the explanation box, the scale and the graph; arrow keys move the slider; Enter weighs.
- With Motion off the particle view shows still frames with arrows for motion.

## Look
- Accent `--brand` #8a4b08 tea amber (header, the slider, the table); gold #f4c542 (the item in hand, the reading that changed); paper #fcf5ec; ink #2a1703; muted #5f554a.
- Contrast (WCAG 2.1, computed): white on brand 6.79:1; brand on paper 6.28:1; ink on paper 15.88:1; muted on paper 6.73:1; ink on gold 10.56:1.
- Never color alone: particles carry a key with names (water, sugar, air); graph bars carry numbers.
- Different from this batch (globe blue, bakery rose, river green, night indigo).

## Art
- Local FLUX (`scripts/localart.py`): the counter (1, 16:9), magnifier and microscope views for four changes (8, 1:1).
- Drawn in code: the particle view, the scale, the table and graph.
About 9 images.

## Voice
Two bank voices, each unique in this batch: `curious-librarian` as the narrator; `bright-teacher` as the guide and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.change + ':' + state.zoom + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `zoom`: "Drag the zoom slider to the next stop."
- how `explain`: "Say what you think is happening, then tap Show."
- event, whole, each caption.
- how `weigh`: "Tap the scale before and after."
- how `graph`: "Look at the graph. Which one changed?"
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
particles (`kit/particles.js`, inlined after `kit:curio`), as described in gas-law-lab's spec. Uses `Box` with `zones` and `dissolve(id)` for the sugar, wall `hits(side)` for the balloon, `attract` for ice, and `still()` for Motion off. All weights come from this tool's own stated amounts, not from particle counts, and the picture is labeled "in the picture".

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Zoom | Skip to the caption | `Show` stays off until the student picks or writes an idea. |
| Weigh-ins | Weigh only after | The table needs before and after for each. |
| Claim | Say the gas vanished | The claim card asks where it went and checks for "into the air". |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `zoom`; `explain`.
2. Caption (whole), waits.
3. `weigh`; `graph`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for 5-PS1-1, 5-PS1-2 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Matter is made of particles; dissolving, evaporating and melting at the particle level | American Chemical Society, "Middle School Chemistry", chapters 1 and 5 | Royal Society of Chemistry, "The particle model" | yes |
| Mass is conserved in physical and chemical changes in a closed system | American Chemical Society, "Middle School Chemistry", conservation of mass | OpenStax, "Chemistry 2e", law of conservation of matter | yes |
| Baking soda and vinegar make carbon dioxide gas | American Chemical Society, "Inquiry in Action", baking soda and vinegar | Royal Society of Chemistry, "Reactions of carbonates" | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad r30, 2026-11-09): 1 gram of baking soda makes about 0.52 grams of carbon dioxide (44.01 over 84.01), so the open cup drops by about half a gram; four changes at four zoom stops; four weigh-ins; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 counter and zoom; at 680x425 strip.
2. Four changes are zoomed to the particle view and explained before captions. (5-PS1-1)
3. Four setups are weighed before and after. (5-PS1-2)
4. The graph shows only the open cup losing weight, and the claim explains why. (5-PS1-2)
5. The particle picture is labeled as a model, not true size or number.
6. The safety card is shown before the bottle weigh-in.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: still frames with arrows; no network requests.

## Open questions
None.

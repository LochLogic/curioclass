# Reaction Kitchen

## One idea
A kitchen counter holds three benches, each with one question; at bench 1 ("Did something new form?") the student mixes four pairs (baking soda and vinegar, sugar and water, milk and lemon juice, sugar heated in a pan) and compares property cards before and after (density, melting point, solubility, smell, color), sorting each into reaction or not with the data as the reason, and finds that dissolved sugar is still sugar while the other three made new substances; at bench 2 ("Where did the mass go?") baking soda and vinegar fizz in an open cup on a scale and the mass drops, then in a sealed bag the mass holds, and a molecule view counts every atom before and after so the student sees the gas carried the missing mass away; at bench 3 ("Can you make heat on purpose?") the student mixes iron powder, salt, water and sawdust in a pouch, aiming to stay between 40 and 50 degrees Celsius for an hour, tests, reads the temperature graph, changes one amount and tests again, with a cold pack option using baking soda and citric acid; at the end a recipe card holds the best design, so a seventh grader learns to use properties to tell whether a reaction happened, that atoms are rearranged and mass is conserved, and to design and improve a device that releases or absorbs heat by a chemical process.

## Not like
- hand-warmer-lab (10, spec): bond energies and enthalpy. Here kitchen materials and simple design trials only.
- mystery-powders (5, spec): identifying powders by tests. Here whether a new substance formed.
- molecule-builder (7, concept): building molecules, same family. Here rearranging them.
- particle-party (7, concept): particle motion and temperature. Here new substances.

## Who and how
- Grade 7, Science, module "Chemical Reactions". Standards: MS-PS1-2 (analyze and interpret data on the properties of substances before and after the substances interact to determine if a chemical reaction has occurred), MS-PS1-5 (develop and use a model to describe how the total number of atoms does not change in a chemical reaction and thus mass is conserved), MS-PS1-6 (undertake a design project to construct, test, and modify a device that either releases or absorbs thermal energy by chemical processes).
- Format: lab. Driver: one student alone, or pairs (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Bench 1 with four pairs and five properties, bench 2 with the open and sealed tests and an atom count, bench 3 with four amounts, a one-hour graph and up to six trials. Extra: Cold pack (bench 3 run in reverse, aiming at 5 to 10 degrees). tool.json `modes: ["Kitchen", "Cold pack"]`, `minutes: "30-40"`, `grades_label: "Grade 7"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-PS1-2 | Compare property cards before and after four mixes and sort | the property cards; the sort with reasons | 2 |
| MS-PS1-5 | Weigh open and sealed, then count atoms each side | the scale; the atom tally | 3 |
| MS-PS1-6 | Build, test and change a hand warmer | the pouch; the temperature graph; the trial log | 4 |

## Screens and modes
Header (kit): title "Reaction Kitchen"; `Kitchen`, `Cold pack`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A bright kitchen counter with three benches, a question card above each. Safety goggles on a hook. The welcome is queued (`welcomeAfter: true`): "Cooking is chemistry. Let's find out when something new is made. Tap the first bench." First hint: "Tap bench 1."

**Bench 1 (focus: the property cards).** At 1366x768 the mix fills the left with before and after cards right; at 680x425 the cards are a sheet. The student drags two ingredients into a bowl; the mix plays (fizz, curdle, browning, dissolving) and the after card fills. The student sorts: New substance or Same substance, and taps the property that proves it. Sugar in water: the sugar is still there (dry it and you get sugar back). The other three: new properties.

**Bench 2 (focus: the scale).** Open cup: 1 g of baking soda and vinegar on a scale; the reading drops as bubbles leave. Sealed bag: the reading holds. The molecule view shows baking soda and acetic acid on the left, sodium acetate, water and carbon dioxide on the right; the student drags atoms into a tally (Na 1, C 3, H 5, O 5 on each side). Narrator: "The atoms didn't disappear. Some of them left as a gas."

**Bench 3 (the design).** The pouch has four sliders: iron, salt, water, sawdust. `Test` runs one hour in a few seconds; the graph shows temperature against time with the goal band (40 to 50 degrees) shaded. Too hot and short, too cool, or just right. The log keeps each trial and asks what was changed. Only one slider may change between trials for a trial to count as fair. A note: "Rusting is slow outside a pouch. Salt and fine powder speed it up."

**The recipe card (the aha).** The best design and its graph. Narrator: "Atoms rearranged, nothing lost, and the heat came from the change. That's something you can design with."

**The end.** The sort, the tally and the recipe card. `Print` prints them.

**Cold pack (extra).** Baking soda and citric acid take in heat; aim for 5 to 10 degrees.

## Content
- Four pairs with before and after property values, the balanced equation with atom counts, a simple hand-warmer model (heat rate from iron surface, salt and water; cooling to air), a cold pack model, the recipe card.
- Safety note on screen: "Only do these mixes at home with a grown-up. Never taste lab mixes."

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Benches can be done in any order; the recipe card needs all three.
- Keyboard: Tab to ingredients, the sort, the atom tally, sliders and `Test`; arrows move sliders; Enter acts.
- With Motion off mixes show before and after stills and the graph draws at once.

## Look
- Accent `--brand` #a3361f tomato red (header, bench frames, the graph line); gold #f4c542 (the goal band edge, the ingredient in hand); paper #fcf4ef; ink #2a0f08; muted #625048.
- Contrast (WCAG 2.1, computed): white on brand 6.76:1; brand on paper 6.22:1; ink on paper 16.51:1; muted on paper 7.00:1; ink on gold 11.03:1.
- Never color alone: atoms carry letters; the goal band carries numbers.
- Different from this batch (granite brown, raindrop blue, olive, lake teal).

## Art
- Local FLUX (`scripts/localart.py`): the kitchen counter (1, 16:9), four mix close-ups after (4, 1:1).
- Drawn in code: property cards, the scale, molecules, the pouch, the graph.
About 5 images.

## Voice
Two bank voices, each unique in this batch: `lively-host` as the kitchen show host; `warm-teacher` as the lab coach and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.bench + ':' + state.trial + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `mix`: "Drag two ingredients into the bowl."
- how `sort`: "Tap New or Same, then the property that shows it."
- how `weigh`: "Tap Seal the bag, then pour."
- how `tally`: "Drag each atom to the tally."
- how `design`: "Move one slider, then tap Test."
- event, whole, each trial's result.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
molecules (family "molecules"; no engine file yet). This tool builds the molecules family's shared pieces first, in a marked block `/* MOLECULES DATA: begin */ ... /* end */`: atom records (symbol, color, label), small molecule shapes, and an atom tally that checks two sides balance; molecule-builder reuses them.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Sort | Call everything a reaction | Sugar in water fails, and the reason must be a property that changed. |
| Tally | Type numbers | Atoms are dragged from the picture; counts must match the drawing. |
| Design | Max every slider | Too hot fails the band; the log needs one change per fair trial. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `mix`; `sort`.
2. `weigh`; `tally`.
3. `design`; trial result (whole), waits.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for MS-PS1-2, MS-PS1-5, MS-PS1-6 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Signs of a chemical change versus dissolving | American Chemical Society, "Middle School Chemistry", chapter 6 | OpenStax, "Chemistry 2e", physical and chemical properties | yes |
| Baking soda and vinegar make sodium acetate, water and carbon dioxide | American Chemical Society, "Middle School Chemistry", lesson 6.2 | PubChem, sodium bicarbonate reactions | yes |
| Mass is conserved in a closed system | American Chemical Society, "Middle School Chemistry", conservation of mass | OpenStax, "Chemistry 2e", chapter 4 | yes |
| Iron hand warmers use rusting sped up by salt, water and a carbon or wood filler | American Chemical Society, "ChemMatters", hand warmers | Science History Institute, "Hand warmers" | yes |
| Baking soda and citric acid absorb heat | American Chemical Society, "Middle School Chemistry", lesson 6.7 | Royal Society of Chemistry, "Endothermic reactions" | yes |
Backed twice: 6. Cut: 0.

Checks run (Python, scratchpad r2, 2026-11-10): both sides of the baking soda and vinegar equation hold Na 1, C 3, H 5, O 5; 1 g of baking soda can release 0.52 g of carbon dioxide; the goal band is 10 degrees wide; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 mix and cards; at 680x425 sheet.
2. Four mixes are sorted with a property as the reason. (MS-PS1-2)
3. Open and sealed weighings are compared and atoms tallied both sides. (MS-PS1-5)
4. A hand warmer is built, tested and changed one thing at a time. (MS-PS1-6)
5. No bond energies or enthalpy appear; kitchen materials only.
6. The safety note shows on every bench.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: stills and instant graphs; no network requests.

## Open questions
- Overlap risk with hand-warmer-lab (default used: this tool stays with kitchen materials and simple design trials, no bond energies; hand-warmer-lab keeps the energy math).

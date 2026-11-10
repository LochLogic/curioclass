# Sphere Connections

## One idea
Four card decks (rock and land, water, air, living things) sit beside a water bank of 100 tokens, and the student plays a card game against a computer player where each card names what can cause it and what it sets off (a volcano erupts, ash blocks sunlight, the air cools, rain falls, a forest regrows), so playing a card that the last card could cause builds a chain, and a chain scores more for each of the four spheres it crosses; the water bank is the rule that bites: life and town cards cost fresh water, but of the 100 tokens about 97 are salty ocean, about 2 are frozen in ice and only about 1 is liquid fresh water in the ground, lakes, rivers and air, and glacier-melt and well cards unlock a little more at a price; after the game the student sorts the bank into a bar graph and a percent table, zooms into the fresh water to see that most of it is ice or underground, and replays their longest chain as a labeled cause-and-effect diagram with one link explained in a sentence, so a fifth grader learns to model how Earth's rock, water, air and living things interact, and to graph the amounts and percentages of Earth's water to show how little is fresh and reachable.

## Not like
- raindrop-s-journey (6, concept): one water drop's path. Here all four spheres and the whole water supply.
- bond-battle (10, spec): a card game about bonds. Here a card game about Earth systems.
- erosion-table (4, spec): one process at a time. Here chains across systems.
- fossil-clues (3, spec): one place changing over time. Here the whole planet working at once.

## Who and how
- Grade 5, Science, module "Earth's Spheres". Standards: 5-ESS2-1 (develop a model using an example to describe ways the geosphere, biosphere, hydrosphere, and/or atmosphere interact), 5-ESS2-2 (describe and graph the amounts and percentages of water and fresh water in various reservoirs to provide evidence about the distribution of water on Earth).
- Format: cards. Driver: one student against a computer player (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Four decks of ten cards, a guided first hand, the water bank of 100 tokens, the computer player, the graph and percent table, the fresh water zoom, the chain diagram. Extra: Pass and play (two players on one device). tool.json `modes: ["Play", "Pass and play"]`, `minutes: "25-35"`, `grades_label: "Grade 5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 5-ESS2-1 (model) | Build chains where each card is caused by the last | the chain on the table; sphere icons | 2 |
| 5-ESS2-2 (amounts) | Spend fresh water from a bank with real proportions | the water bank | 3 |
| 5-ESS2-2 (graph) | Sort the bank into a bar graph and a percent table; zoom into fresh water | the graph; the table | 3 |
| 5-ESS2-1 (explain) | Replay the longest chain as a diagram and explain one link | the labeled diagram; the sentence | 4 |

## Screens and modes
Header (kit): title "Sphere Connections"; `Play`, `Pass and play`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** Four decks with icons (a mountain, a wave, a cloud, a leaf), a water bank of 100 blue and white tokens, and a hand of five cards. The welcome is queued (`welcomeAfter: true`): "Earth's rock, water, air and life are always pushing on each other. Play a card that the last card could cause. Tap a card in your hand." First hint: "Tap the glowing card in your hand."

**The guided hand.** The first three turns show which cards could follow and why ("Ash in the air can block sunlight").

**Play (focus: the chain).** At 1366x768 the chain runs across the table with the bank and hand below; at 680x425 the hand is a bottom bar. Each card shows its sphere, what can cause it and what it can set off. A legal play links on; a chain that crosses all four spheres scores a bonus. Life and town cards (a farm, a city, a salmon run) cost fresh water tokens. The computer player builds its own chains and can break the student's with a drought card.

**The water bank (5-ESS2-2).** 100 tokens: about 97 salty ocean, about 2 frozen in ice and snow, about 1 liquid fresh water. Only the 1 can be spent. Glacier-melt and well cards move a little more into reach, at a cost in other cards (a shrinking glacier, a sinking water table).

**After the game.** The student drags tokens into a bar graph by place and fills a percent table. A zoom shows fresh water alone: about 69 percent ice, about 30 percent underground, about 1 percent in lakes, rivers, soil, air and living things.

**The chain diagram (the aha).** The longest chain replays as a cause-and-effect diagram with sphere labels. The student picks one link and writes a sentence: "___ affected ___ because ___." Narrator: "Every part of Earth touches every other part. And almost all of Earth's water is salty or frozen, so the fresh water we can reach is precious."

**The end.** The graph, table and diagram. `Print` prints them.

**Pass and play (extra).** Two players on one device.

## Content
- Forty cards (ten per sphere) with stated causes and effects, including real examples (an eruption cooling the air, a forest making rain, a river carving a canyon, beavers making a wetland), the water bank, the computer player, the graph and diagram.
- Water figures are rounded from USGS data so the 100 tokens add up exactly, with the rounding stated.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Illegal plays shake and show what the last card can set off.
- Keyboard: Tab to hand cards, the chain, the bank and the graph; Enter plays; arrow keys move between cards.
- With Motion off cards jump into place and tokens move without sliding.

## Look
- Accent `--brand` #1f5f7a globe blue (header, the water bank, the diagram); gold #f4c542 (the playable card, a four-sphere bonus); paper #eef5f8; ink #0a1f28; muted #4e5a60.
- Contrast (WCAG 2.1, computed): white on brand 7.06:1; brand on paper 6.40:1; ink on paper 15.37:1; muted on paper 6.45:1; ink on gold 10.42:1.
- Never color alone: spheres carry icons and names; tokens carry the words salt, ice, fresh.
- Different from this batch (tea amber, bakery rose, river green, night indigo).

## Art
- Local FLUX (`scripts/localart.py`): forty card pictures (40, 3:4).
- Drawn in code: the table, tokens, graph, table, diagram, sphere icons.
About 40 images.

## Voice
Two bank voices, each unique in this batch: `lively-host` as the game host; `calm-professor` as the Earth scientist and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.turn + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `play`: "Tap a card that the last card could cause."
- event, whole, each card's cause line ("Ash in the air can block sunlight").
- how `spend`: "Drag fresh water tokens to pay for this card."
- how `graph`: "Drag the tokens into the graph."
- how `explain`: "Pick a link and finish the sentence."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the deck and cause rules, the computer player, the bank, the graph and diagram. Card and water data sit in a marked block `/* SPHERES DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Chains | Play any card | Only cards the last card can cause are legal. |
| Bank | Spend ocean tokens | Ocean and ice tokens can't pay for fresh water cards. |
| Explanation | Write any sentence | The sentence must name two linked cards from the chain. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `play`; cause line (whole), waits.
2. `spend`.
3. `graph`.
4. `explain`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for 5-ESS2-1, 5-ESS2-2 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Ocean about 96.5 percent, ice and snow about 1.7 percent, fresh water about 2.5 percent of all water; of fresh water about 69 percent ice and 30 percent groundwater | U.S. Geological Survey, Water Science School, "Where is Earth's water?" | Shiklomanov, "World fresh water resources" in Gleick, "Water in Crisis" (Oxford, 1993) | yes |
| The 1991 Pinatubo eruption cooled Earth by about half a degree Celsius | U.S. Geological Survey, "Mount Pinatubo" fact sheet | NASA Earth Observatory, "Global effects of Mount Pinatubo" | yes |
| Forests return water to the air and help make rain | NASA Earth Observatory, "The water cycle" | U.S. Forest Service, "Forests and water" | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad r30, 2026-11-09): ocean plus salty groundwater and lakes is about 97.4 percent and rounds to 97 tokens; ice, snow and ground ice is about 1.76 and rounds to 2; the rest is about 0.8 and rounds to 1; 97 plus 2 plus 1 is 100; fresh water shares 68.7 plus 30.1 plus 1.2 is 100; four decks of ten is forty cards; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 chain and bank; at 680x425 bottom bar.
2. Chains link cards by cause and cross spheres for a bonus. (5-ESS2-1)
3. The bank uses real water proportions and is graphed with percents, with a fresh water zoom. (5-ESS2-2)
4. The longest chain becomes a diagram with one link explained. (5-ESS2-1)
5. Token rounding is stated and adds to 100.
6. The computer player follows the same rules.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no sliding; no network requests.

## Open questions
- The idea card flags a data source (default used: USGS "Where is Earth's water?" table, rounded to 97 ocean and salty, 2 ice, 1 liquid fresh, with the rounding shown on the graph).

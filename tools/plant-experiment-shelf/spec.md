# Plant Experiment Shelf

## One idea
A shelf holds four pots of bean seeds, a lamp, a dark closet and a watering can, and a notebook page asks "Which thing will you change? Keep everything else the same."; the student sets each pot's light and water (light and water, no light, no water, neither), and the notebook flags any pair of pots that differ in more than one thing as an unfair test; two sped-up weeks play, and each day the student measures height with an on-screen ruler and colors the leaves on a chart; the pot in the dark grows pale and tall and then flops, the dry one wilts, the one with both grows green and strong; at a second bench, flowers with pollen and a field of burrs wait, and the student builds a model animal from parts (a pipe cleaner, a cotton ball, felt, a smooth plastic bead), runs it flower to flower or through the field, and counts pollen grains or seeds carried, comparing fuzzy and smooth models; at the end the notebook holds the claim that plants need light and water to grow, and a model card shows that fuzzy or hooked bodies carry pollen and seeds the way bees and furry animals do, so a second grader learns to plan and conduct an investigation of what plants need to grow, and builds a model that mimics an animal spreading seeds or pollinating flowers.

## Not like
- terrarium-pal (K, spec): a care log, same engine. Here a fair test with measurements.
- three-pigs-lab (2, live): testing building materials. Here testing living things.
- nature-inventor (1, spec): copying animal parts for people. Here modeling what animals do for plants.
- life-cycle-wheel (3, spec): a plant's whole life. Here what helps it grow and spread.

## Who and how
- Grade 2, Science, module "Plants Need Water and Light". Standards: 2-LS2-1 (plan and conduct an investigation to determine if plants need sunlight and water to grow), 2-LS2-2 (develop a simple model that mimics the function of an animal in dispersing seeds or pollinating plants).
- Format: lab. Driver: one child alone or with a grown-up nearby (tool.json `driver: "student"`). Every card is spoken. Controls 56 px or more.
- Four pots, a fair test check, 14 sped-up days with measuring, the model bench with four materials and two tasks, the notebook. Extra: Class shelf (the class predicts each pot together, then runs it). tool.json `modes: ["Shelf", "Class shelf"]`, `minutes: "20-30"`, `grades_label: "Grade 2"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 2-LS2-1 (plan) | Set light and water for four pots and fix any unfair pair | the notebook's fair test check | 2 |
| 2-LS2-1 (conduct) | Run two weeks, measure height and color leaves each day | the growth chart; the four plants | 3 |
| 2-LS2-2 | Build a fuzzy and a smooth model and count pollen or seeds carried | the model bench; the count | 4 |

## Screens and modes
Header (kit): title "Plant Experiment Shelf"; `Shelf`, `Class shelf`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more.

**On load and first tap.** A shelf with four empty pots labeled A to D, a lamp, a closet door and a watering can; a notebook page. The welcome is queued (`welcomeAfter: true`): "Do plants really need light and water? Let's test it fairly. Tap pot A to choose its light and water." First hint: "Tap pot A."

**Plan (focus: the pots).** At 1366x768 the shelf fills the left with the notebook right; at 680x425 the notebook is a sheet. Each pot gets a light choice (lamp or closet) and a water choice (watering can or none). The notebook lists pairs to compare; a pair that differs in two things gets a flag: "Unfair: two things changed. Which one made the difference?" Same soil, same seeds and same pot size are shown as kept the same.

**Two weeks (2-LS2-1).** Tap `Next day` or `Play`. Each day the student drags a ruler to each plant and taps its height; a leaf swatch picks the leaf color. The chart draws four lines and colors. By day 14: the lamp-and-water plant is green and sturdy; the closet plant is pale, tall and thin, and flops; the dry plant wilts; the plant with neither barely sprouts and stays pale.

**Model bench (2-LS2-2).** Flowers with pollen and a field of burrs and seeds. Four parts: pipe cleaner, cotton ball, felt, smooth plastic bead. The student builds two models (a fuzzy bee, a smooth bead bee; a felt sock dog, a smooth dog), runs each, and counts pollen grains moved between flowers or seeds carried through the field. A card shows a real bee's hairy body and a dog's fur with burrs.

**The notebook (the aha).** "Plants need ___ and ___ to grow. My evidence: pot ___ and pot ___." "The fuzzy model carried more ___, like a ___." Narrator: "You changed one thing at a time, so you know what made the difference."

**The end.** The notebook, chart and model counts. `Print` prints them.

**Class shelf (extra).** The class predicts each pot together, then runs it.

## Content
- Four pots, a fair test checker, a 14-day growth model with stated rules, the ruler and leaf swatch, four model parts, two tasks, the notebook.
- Plants recover if light and water are restored in a second run; nothing rots on screen.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Measuring snaps to the nearest half centimeter; any day can be measured again.
- Keyboard: Tab to pots, choices, the ruler, the chart and the bench; Enter sets and measures.
- With Motion off plants change between days without growing smoothly.

## Look
- Accent `--brand` #9c4221 clay pot (header, pots, the notebook); gold #f4c542 (the pot in focus, the ruler mark); paper #fcf3ef; ink #2b0f06; muted #61544e.
- Contrast (WCAG 2.1, computed): white on brand 6.53:1; brand on paper 5.97:1; ink on paper 16.36:1; muted on paper 6.65:1; ink on gold 11.00:1.
- Never color alone: pots carry letters and icons (lamp, closet, drop, no drop); chart lines carry letters; leaf color carries a word.
- Different from this batch (team blue, sandstone, wheel violet, winter teal).

## Art
- Local FLUX (`scripts/localart.py`): the four plants at five stages each (20, 3:4), the shelf (1, 16:9), the flower and burr bench (1, 16:9), a bee close-up and a dog with burrs (2, 4:3).
- Drawn in code: the ruler, the chart, the notebook, model parts and counts.
About 24 images.

## Voice
Two bank voices, each unique in this batch: `clear-teacher` as the notebook and hints; `playful-friend` as the model bench helper. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.day + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `plan`: "Tap a pot and choose its light and water."
- event, whole, an unfair pair flag.
- how `measure`: "Drag the ruler to each plant."
- event, whole, day 14's plants.
- how `build`: "Drag parts to build a model."
- how `run`: "Tap Run and count what it carried."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
terrarium (family "terrarium"). Reuses terrarium-pal's `/* TERRARIUM DATA: begin */ ... /* end */` block (living-thing states, need rules, the picture log) and adds a growth model and the fair test checker inside it.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Plan | Give every pot the same | The notebook says nothing was changed and asks for one change. |
| Measure | Skip measuring | The chart needs at least four measured days per pot. |
| Model | Build only one | The model card needs a fuzzy and a smooth count. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `plan`; flag (whole), waits.
2. `measure`; day 14 (whole).
3. `build`; `run`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for 2-LS2-1, 2-LS2-2 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Plants grown in the dark become pale, tall and weak (etiolation) | Encyclopaedia Britannica, "Etiolation" | Royal Society of Biology, plant growth teaching notes | yes |
| Plants need water; dry plants wilt | U.S. Department of Agriculture, "How plants grow" | University of Minnesota Extension, "Watering plants" | yes |
| Bee body hairs carry pollen | U.S. Forest Service, "Bee pollination" | Xerces Society, "Bees and pollination" | yes |
| Burrs hitch on animal fur to spread seeds | U.S. Forest Service, "Seed dispersal" | Missouri Botanical Garden, "Seed dispersal" | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad r27, 2026-11-09): with pots A (light, water), B (no light), C (no water), D (neither), four pairs differ in one thing and two pairs differ in two; 14 days; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 shelf and notebook; at 680x425 sheet.
2. Four pots are set and unfair pairs are flagged. (2-LS2-1)
3. Two weeks are measured and charted for all four pots. (2-LS2-1)
4. Fuzzy and smooth models are built and their carries counted. (2-LS2-2)
5. The notebook claim cites two pots as evidence.
6. Every card is spoken; nothing rots on screen.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: daily steps; no network requests.

## Open questions
None.

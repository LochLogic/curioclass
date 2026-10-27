# Carrying Capacity

## One idea
A habitat's carrying capacity is set by how fast its food grows back, not by a number painted on the land: run a
deer herd on a forest edge where browse regrows each year and watch it level off at the herd the regrowth can feed,
push it with wolves, a fire, a hard winter or a smaller forest, then replay the real St. Matthew Island reindeer,
29 animals that grew to about 6,000 on slow-growing lichen and crashed, and see why a slow food supply makes a
herd overshoot.

## Not like
- outbreak-model (live, grade 11 math) and slope-field-garden (math): a logistic curve with K as a parameter. Here
  K is an outcome of food regrowth and eating, which students can change and watch; the logistic curve is only an
  optional overlay to compare.
- predator-prey-island (grade 7, ecosystem family): wolves and moose cycling together on Isle Royale. Here the
  wolves are a fixed pack set by a slider and the story is the food limit.
- energy-pyramid (grade 7, ecosystem family): the 10 percent rule by itself. Here the pyramid is one view of the
  same herd.
- population-dashboard (sci 12): human population data. Here one wild herd, simulated.
- reserve-designer (same group): which species can live in a valley at all. Here how many of one species.
- island-economy (sci 9, maybe Lake Commons): people harvesting a shared resource. No harvest decisions here.

## Who and how
Grade 9, science (Life Science module Ecology and Populations: "Carrying capacity, food webs and energy flow").
Driver: students on laptops, or the teacher on a projector for the island story. 20 to 35 minutes. Standards:
HS-LS2-1 (mathematical representations of factors that affect carrying capacity), HS-LS2-2 (mathematical
representations of factors affecting biodiversity and populations at different scales), HS-LS2-4 (energy flow
among trophic levels), HS-LS2-6 (stable conditions keep numbers fairly steady; disturbances can change the
ecosystem).
Topic line: population limits and energy flow.
9-12 dark theme. Header: title, `.seg` modes **Herd**, **Island**, kit buttons `motion`, `sound`, `read`.

## Screens and modes
Shared stage: a backdrop image (forest edge or tundra island) with deer drawn in code as small silhouettes (one
icon per deer up to 60, then each icon is worth more and a "1 icon = N deer" key shows), a food bar under the
backdrop (browse or lichen left), and the population chart below (graphing.js): deer per year (accent), food left
(dashed), and a K line when known. Panel: controls, readouts (`dl.readouts`), `hint`, `tip`. Under 900 px tall:
backdrop shrinks to a 90 px strip.

**Herd** (opens first). Forest edge. Controls:
- **Start herd** slider 2 to 100 (step 1, default 10). **Forest size** slider 0.25 to 2.0 times (step 0.25, default
  1.0).
- **Wolves** slider 0 to 6 (a fixed pack; takes effect from the next year).
- Events: **Fire** (burns 70 percent of the browse above the bare minimum, this year), **Hard winter** (30 percent
  of the herd dies this year).
- **Step 1 year**, **Play** / **Pause** (2 years per second), **Reset** (year 0). The chart shows 60 years.
- **View** `.seg` **Herd** / **Energy flow**. Energy flow replaces the backdrop with a three-level pyramid:
  browse eaten this year, deer and wolves, using the 10 percent rule (bar widths and kJ numbers; see Content).
- **Compare with logistic** switch: draws the logistic curve with handles for K and r (drag, or number fields);
  starts at K = the model's K, r = ln 1.35 = 0.300 per year.
Readouts: Year, Deer, Food left, Food per deer (percent of a full ration), Births, Deaths from hunger, Other deaths,
Wolf kills, K for this forest (shown after the run levels off: "levels off at 300").

**Island** (the case study). Tundra island backdrop. The real counts as points on the chart: 29 (1944), 1,350
(1957), about 6,000 (1963), 42 (1966). **Play the model** runs the same rules with slow-growing lichen, year 0 =
1944. Prompts (cards, no scoring): "Why did the forest herd level off but the island herd crash?" / "How fast does
lichen grow back compared with browse?" **Lichen regrowth** slider (0.002 to 0.05 per year, default 0.005) lets
students test a claim: the peak barely moves (it is set by the lichen stored up over centuries), but faster regrowth
raises the herd the island can keep, so the crash is far smaller. A last card tells the end of the real story: by
the 1980s no reindeer were left (the 42 survivors in 1966 included one male).

## Content
Model (labeled "model" on screen; one source of truth, yearly step, food in deer-years: 1 unit feeds one deer for
one year):
- Lands: Forest edge Bmax 300, regrowth g 0.8 per year, bare minimum 10 percent (30 units deer cannot reach).
  Lichen island Bmax 20,000, g 0.005, bare minimum 2 percent (400). The island starts with Bmax (lichen stored up
  over centuries). Forest size multiplies Bmax.
- Each year: food regrows B = B + g x (Bmax - B); available = max(0, B - minimum); eaten E = min(D, available);
  food per deer f = E / D; births 0.45 x D x f; other deaths 0.10 x D; hunger deaths 0.8 x D x (1 - f); wolf kills
  min(D, W x 15 x D / (D + 50)); hard winter adds 0.3 x D deaths; fire sets B = minimum + 0.3 x (B - minimum) before
  eating. New D under 2 becomes 0. Then B = B - E.
- Why it levels off: the herd is steady when births match deaths, at f = 0.9 / 1.25 = 0.72 (72 percent of a full
  ration). The forest's regrowth when eaten down is 0.8 x (300 - 30) = 216 units, so K = 216 / 0.72 = 300.
  Forest size 0.5 gives K = 150. Island: 0.005 x (20,000 - 400) / 0.72 = 136.
Worked runs (Python, Curio Class 2026-10-27; deer rounded to 0.1):
- Forest, 10 deer: 10, 13.5, 18.2, 24.6, 33.2, 44.8, 60.5, 81.7, 110.3, 148.9, 201.1, 271.4, 305.6, 300.6, 300.1,
  300.0 (years 0 to 15). Passes 150 in year 10, overshoots to 305.6 in year 12.
- Wolves from year 20 (steady herd after): 1 wolf 285.8, 2: 271.8, 3: 258.1, 4: 244.6, 5: 231.5, 6: 218.6.
- Fire in year 25: herd 111 that year, 150, 202, 273, 305, then 300 (back by year 30).
- Hard winter in year 25: 210, then 283, then 300.
- Forest size 0.5: levels at 150 (year 10 onward).
- Island from 29: year 13 (1957) 1,435 (real 1,350); year 17 4,765; year 18 (1962) 6,433; year 19 2,698; year 20
  392; year 21 162; then 136 to the end. Lichen falls from 20,000 to the 400 minimum by year 20.
Logistic overlay: N(t) = K / (1 + ((K - N0)/N0) x e^(-r t)); with K 300, r 0.300, N0 10: year 10 about 122.8 (model
148.9), year 15 about 227.0 (model 300.0). Card: "The logistic curve rounds the corner. The food model turns
sharply, because deer eat well until the food runs short."
Energy flow (10 percent rule, model): browse eaten E units, each unit shown as 1,000 kJ of plant energy (a model
unit); deer level 10 percent of that; wolves 10 percent of the energy in the deer they kill. At the steady forest
herd: plants eaten 216 units = 216,000 kJ, deer level 21,600 kJ, wolves (with 4 wolves, 49.8 deer killed) shown as
1 percent of plant energy. Bars scale by log so wolves stay visible; the numbers are printed.
Hints: Herd "<b>Herd.</b> Press Play and watch where the herd levels off. Then change one thing: wolves, fire, winter
or forest size." / Island "<b>Island.</b> Press Play the model, then compare it with the real counts."
Tips: "Carrying capacity is the largest population the habitat can support over time." / "A herd can overshoot when
food runs out slowly." / "Wolves lower the steady herd, and the forest gets more browse left over." / "Only about 10
percent of the energy at one level reaches the next."
Model limits line: "This model leaves out ages, males and females, disease, snow depth and migration, and wolves
here never starve. Real food regrowth changes year to year."

## Interactions in detail
- Changing a slider while paused changes the next year only; Reset applies Start herd and Forest size from year 0.
- Fire and Hard winter apply to the next stepped year; each can be pressed once per year; they appear as marks on
  the chart's time axis with a word label.
- Logistic handles are draggable points on the chart and number inputs in the panel (keyboard). The overlay never
  changes the model.
- Island: the real points show from the start; Play the model draws the model line year by year. The regrowth slider
  resets the island run.
- Herd icons: deer appear and disappear with a quick fade (none with Motion off); starving years tint the food bar.
- Readouts live in an `aria-live="polite"` region, updated once per year.
- Mode change: `V.hush()`; each mode keeps its run.

## Look
Accent `--brand #e2a19c` (summer coat of a deer, lightened), `--brand-ink #10161f`. Stage under the backdrop
`#11171c`. Food line `#9fd38a` dashed (10.45:1 on the stage; the legend names it, so color is never the only cue). Real data
points: hollow white circles with year labels.
Contrast (computed): brand on --panel 8.09:1, on --sec-bg 7.66:1; brand-ink on brand 8.48:1. Nearest 9-12
accents #f39cbc and #ff8f9e (dE about 20); in this group energy-accountant #d3b069 and mitosis-mixer #f1b1ed (dE 35).

## Art
Cloudflare FLUX.2 (`scripts/cfart.py`), wide landscape backdrops, no animals (deer are drawn in code on top), no
people, no lettering, soft natural light, webp, 16:9, long side 1600 px, cutout no.
- cc-forest-edge: a northern forest edge meeting a grassy clearing with shrubs and young trees, late summer, open
  ground in the foreground for animals to stand on.
- cc-tundra-island: a treeless subarctic island tundra with low hills, pale lichen mats and grass, gray sea at the
  horizon, open ground in the foreground.

## Voice
Bank `science-narrator` (a wildlife documentary narrator, calm, not dramatic). Uses `Curio.voice`, scope = mode.
- welcomeHerd (how): "Welcome to Carrying Capacity. Press Play and watch where the herd levels off."
- welcomeIsland (how): "Island. Press Play the model, then compare it with the real reindeer counts."
- leveled (event, the first time a run holds within 1 percent for 3 years; stale on Reset): "The herd has leveled
  off. The forest's regrowth feeds about this many deer."
- wolvesIn (how, first wolves above 0): "Wolves join next year. Watch what happens to the herd and to the browse."
- fire (event, each fire; stale on Reset): "Fire. Most of the browse is gone this year."
- winter (event, each hard winter; stale on Reset): "A hard winter. Many deer die, and the food that's left goes
  further."
- overshoot (event, island model passes the real 1963 count; stale on Reset): "The herd has outgrown its lichen.
  Lichen grows back very slowly."
- energyView (how, first Energy flow view): "Each level keeps only about a tenth of the energy from the level below."

## Family engine
**ecosystem** family. This spec describes the shared engine in full for the unspecced siblings food-web-wobble
(grade 5), predator-prey-island (grade 7) and energy-pyramid (grade 7).
`kit/ecosystem.js` (depends on `kit/probability.js` for `Rand(seed)` and on `kit/graphing.js` for charts):
- `Species({id, name, role, icon, params})`: role is producer, consumer or predator; params hold the rates below.
- `Web(species, links)`: who eats whom (`links` as [eater, eaten, share]); `web.remove(id)` and
  `web.effects(id)` list the species that lose or gain food (for food-web-wobble's "pull a species" play).
- `Model({resource, consumers, predator, events, seed, noise})`: a yearly step exactly as in Content: resource
  regrowth toward Bmax with a minimum, consumers eat with ration f, births b x f, base deaths m, hunger deaths
  s x (1 - f), type II predation k x D / (D + h), events (fire, hard winter, custom functions). `predator` is either
  fixed (a count, as here) or dynamic (predator births e x kills, predator deaths, for predator-prey cycles).
  `noise` (default 0) multiplies births by a seeded lognormal for year-to-year luck. `run(years)` returns rows;
  `step()` returns one row; every row lists births, deaths by cause, kills, food.
- `PopChart(el, opts)`: population lines over years, K line, event marks, real-data points, optional logistic
  overlay with draggable K and r handles.
- `Pyramid(el, levels, {rule: 0.1, scale: 'log' | 'linear'})`: energy bars with printed kJ.
- `Landscape(el, {backdrop, species, counts})`: draws code-drawn animal icons over an image backdrop, with
  "1 icon = N" scaling past a cap.
What each sibling feeds: food-web-wobble feeds `Species` and `Web` for a five or six species food web, a simple
multi-species `Model` run and `Landscape`. predator-prey-island feeds `Model` with a dynamic predator (wolves and
moose on Isle Royale; the Isle Royale dataset is reserved for it) and `PopChart` with real counts. energy-pyramid
feeds `Pyramid` with the 10 percent rule and its own food chains. carrying-capacity feeds `Model` with a fixed
pack, fire and winter events and land size, `PopChart` with the logistic overlay and the St. Matthew points,
`Pyramid` and `Landscape`.

## Sources
- St. Matthew Island reindeer, 29 introduced in 1944, about 1,350 in 1957, about 6,000 in 1963, 42 in 1966:
  Klein, D. R. (1968), "The introduction, increase, and crash of reindeer on St. Matthew Island", Journal of
  Wildlife Management 32(2):350-367 (checked 2026-10-27).
- None left by the 1980s: U.S. Fish and Wildlife Service, Alaska Maritime National Wildlife Refuge, St. Matthew
  Island pages (verify confirms; otherwise the card says "the herd later died out" citing Klein 1968).
- Carrying capacity, logistic growth, density-dependent limits: OpenStax Biology 2e, section 45.3 "Environmental
  Limits to Population Growth" (CC BY 4.0), https://openstax.org/books/biology-2e/pages/45-3-environmental-limits-to-population-growth
- Energy transfer between trophic levels about 10 percent: OpenStax Biology 2e, section 46.2 "Energy Flow through
  Ecosystems", https://openstax.org/books/biology-2e/pages/46-2-energy-flow-through-ecosystems
- Lichen recovers over decades after grazing: Klein (1968) and OpenStax Biology 2e 46.2 (lichen as slow producer)
  (verify checks the wording).
- Wolf predation lowering deer or elk numbers and leaving more browse (qualitative): National Park Service,
  Yellowstone, "Wolf Restoration" (https://www.nps.gov/yell/learn/nature/wolf-restoration.htm).
- All rates (births, deaths, regrowth, kill rate) are model values; runs computed in Python (Curio Class,
  2026-10-27).

## Done when
1. Herd, defaults: the herd passes 150 in year 10, peaks at about 305.6 in year 12, and holds 300 from year 15; the K
   readout says 300.
2. Forest size 0.5 levels at 150; 4 wolves from year 20 settle at about 244.6.
3. Fire in year 25 drops the herd to about 111 and it is back to 300 by year 30; a hard winter drops it to about 210.
4. Island model: 1,435 in 1957, peak 6,433 in 1962, crash to 392 by 1964, then 136; real points sit beside it.
5. Lichen regrowth 0.05 still peaks at 6,433 but settles at about 1,361 (0.002 settles at about 54).
6. Logistic overlay with K 300 and r 0.300 reads about 122.8 at year 10; dragging K moves the curve, not the model.
7. Energy flow view prints three levels with the 10 percent rule.
8. All controls work by keyboard; main controls visible at 1366x768 and 680x425; chart readable at 375 wide.
9. Each how-to line speaks once in five repeated actions; event lines speak each event.
10. No network, no em dashes.

## Open questions
- [carrying-capacity] The Wolves slider stops at 6 because the pack never starves here; at 7 or more the herd
  collapses, which would mislead. OK to cap it, or show the collapse with a "real wolves would starve first" note?

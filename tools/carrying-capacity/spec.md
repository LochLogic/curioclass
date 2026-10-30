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
Shared stage: a painted backdrop (forest edge or tundra island, Art) as a band across the top with the herd
standing on its open foreground as painted deer or reindeer cutouts (one cutout per animal up to 60, then each is
worth more and a "1 deer = N deer" key shows; the three poses mix by seeded draw), wolves as painted wolf cutouts at
the forest margin (one per wolf), a food bar under the backdrop (browse or lichen left), and the population chart
below (graphing.js): deer per year (accent), food left (dashed), and a K line when known. The chart is the focus and
the largest thing on the stage (about 55 percent of its height); the herd band above it shows the same year. Panel:
controls, readouts (`dl.readouts`), `hint`, `tip`. Under 900 px tall: the herd band shrinks to a 90 px strip.
The backdrop changes with events: a Fire year crossfades to the burned forest edge for that year and fades back as
the browse regrows over the next two years; a Hard winter year shows the winter forest edge for that year; on the
island the grazed-out tundra crossfades in as lichen falls (its opacity = 1 minus lichen left over 20,000). Crossfades
take 0.4 s (instant with Motion off).

**Herd** (opens first). Focus: the population chart, where the herd line levels off. Forest edge. Controls:
- **Start herd** slider 2 to 100 (step 1, default 10). **Forest size** slider 0.25 to 2.0 times (step 0.25, default
  1.0).
- **Wolves** slider 0 to 6 (a fixed pack; takes effect from the next year).
- Events: **Fire** (burns 70 percent of the browse above the bare minimum, this year), **Hard winter** (30 percent
  of the herd dies this year).
- **Step 1 year**, **Play** / **Pause** (2 years per second, so 60 years take 30 s), **Reset** (year 0). The chart
  shows 60 years. Every control stays live during Play: a slider move or event press shows on the chart and readouts
  at once (an event mark appears on the time axis the moment it is pressed) and takes effect in the next year, at
  most 0.5 s later.
- **View** `.seg` **Herd** / **Energy flow**. Energy flow replaces the backdrop with a three-level pyramid:
  browse eaten this year, deer and wolves, using the 10 percent rule (bar widths and kJ numbers; see Content).
- **Compare with logistic** switch: draws the logistic curve with handles for K and r (drag, or number fields);
  starts at K = the model's K, r = ln 1.35 = 0.300 per year.
Readouts: Year, Deer, Food left, Food per deer (percent of a full ration), Births, Deaths from hunger, Other deaths,
Wolf kills, K for this forest (shown after the run levels off: "levels off at 300").

**Island** (the case study). Focus: the chart, with the real counts beside the model line. Tundra island backdrop,
reindeer cutouts. The real counts as points on the chart: 29 (1944), 1,350
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
herd (no wolves): plants eaten 216 units = 216,000 kJ, deer level 21,600 kJ. With 4 wolves from year 20 the herd
settles at 244.6 and still eats 216 units a year (each deer eats 88 percent of a full ration instead of 72): plants
216,000 kJ, deer 21,600 kJ, wolves 10 percent of the 49.8 killed deer's share (49.8 of 244.6) = 440 kJ, about 0.2
percent of plant energy. Bars scale by log so wolves stay visible; the numbers are printed.
Hints: Herd "<b>Herd.</b> Press Play and watch where the herd levels off. Then change one thing: wolves, fire, winter
or forest size." / Island "<b>Island.</b> Press Play the model, then compare it with the real counts."
Tips: "Carrying capacity is the largest population the habitat can support over time." / "A herd can overshoot when
food runs out slowly." / "Wolves lower the steady herd, and each deer that is left gets more to eat." / "Only about 10
percent of the energy at one level reaches the next."
Die-out note (shown in the readouts when the herd reaches 0 while Wolves is above 0): "The herd is gone. In this model
the pack never starves or leaves, so a small herd can be eaten out. Real wolves would move on first." With the
default start herd of 10, 2 or more wolves set from year 0 eat the herd out (see the checks in Sources).
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
- Herd cutouts: deer appear and disappear with a quick fade (none with Motion off); starving years tint the food bar.
  Animals never move on their own, so nothing animates between years except these fades and the crossfades.
- Readouts live in an `aria-live="polite"` region, updated once per year.
- Mode change: `V.hush()`; each mode keeps its run. Sound starts on (kit); the tool's only sound is the voice.

## Look
Accent `--brand #e2a19c` (summer coat of a deer, lightened), `--brand-ink #10161f`. Stage under the backdrop
`#11171c`. Food line `#9fd38a` dashed (10.45:1 on the stage; the legend names it, so color is never the only cue). Real data
points: hollow white circles with year labels.
Contrast (computed): brand on --panel 8.09:1, on --sec-bg 7.66:1; brand-ink on brand 8.48:1. Nearest 9-12
accents #f39cbc and #ff8f9e (dE about 20); in this group energy-accountant #d3b069 and mitosis-mixer #f1b1ed (dE 35).

## Art
Local FLUX (`scripts/localart.py`), no people. 11 images. The two backdrops already drawn (review pending) keep
their prompts in `art/prompts.json`; the rest share that house style (naturalistic, soft natural light, muted calm
colors, no lettering).
- cc-forest-edge (drawn): a northern forest edge meeting a grassy clearing in late summer, spruce, fir and birch
  behind, shrubs and saplings at the margin, open short grass across the foreground; 16:9; cutout no; people no;
  Herd backdrop.
- cc-forest-edge-burned: the same kind of northern forest edge after a ground fire, blackened trunks and scorched
  shrubs, gray ash over the clearing, a few green shoots, open ground across the foreground; 16:9; cutout no; people
  no; crossfades in for a Fire year.
- cc-forest-edge-winter: a northern forest edge in deep winter, snow-loaded spruce, bare birch, a wide snowy clearing
  across the foreground under a pale low sky; 16:9; cutout no; people no; shown for a Hard winter year.
- cc-tundra-island (drawn): a treeless subarctic island tundra, low rolling hills, pale lichen mats and sedge, gray sea
  at the horizon, open flat tundra across the foreground; 16:9; cutout no; people no; Island backdrop.
- cc-tundra-grazed: the same kind of treeless island tundra grazed bare, brown trampled sedge and bare gravel where
  the lichen was, gray sea at the horizon, open ground across the foreground; 16:9; cutout no; people no; crossfades in
  as the lichen falls.
- Animal kit (one shared prompt: "a single animal in full side view, whole body with all four legs, natural colors,
  soft daylight", one cutout per piece): cc-deer-stand (a white-tailed deer standing alert), cc-deer-graze (a
  white-tailed deer with its head down browsing), cc-deer-walk (a white-tailed deer walking), cc-reindeer-stand (a
  wild reindeer with antlers standing), cc-reindeer-graze (a wild reindeer with its head down grazing), cc-wolf (a gray
  wolf standing); 4:3; cutout yes; people no. Sizing: every animal's height is 7 percent of the herd band's height at
  the front of the foreground, shrinking to 4 percent at the back (placed in seeded rows), the wolf at 6 percent; with
  Motion on they fade in and out, never walk.
The food bar, chart, pyramid and logistic handles stay in code (charts and controls).

## Voice
Bank `science-narrator` (a wildlife documentary narrator, calm, not dramatic). Uses `Curio.voice`, scope = mode. How
lines speak once per page load, then only update the hint; event lines speak each time.
- welcomeHerd (how; on entering Herd; stale once Play or Step 1 year is pressed): "Welcome to Carrying Capacity. Press
  Play and watch where the herd levels off."
- welcomeIsland (how; on entering Island; stale once Play the model is pressed): "Island. Press Play the model, then
  compare it with the real reindeer counts."
- leveled (event; the first time a run holds within 1 percent for 3 years; stale on Reset or any slider change):
  "The herd has leveled off. The forest's regrowth feeds about this many deer. Now change one thing: wolves, fire,
  winter or forest size."
- wolvesIn (how; first Wolves above 0; stale if Wolves returns to 0): "Wolves join next year. Watch what happens to
  the herd and to each deer's share of food."
- fire (event; each fire; stale on Reset): "Fire. Most of the browse is gone this year."
- winter (event; each hard winter; stale on Reset): "A hard winter. Many deer die, and the food that's left goes
  further."
- dieOut (event; the herd reaches 0 with Wolves above 0; stale on Reset): "The herd is gone. This pack never starves,
  so a small herd can be eaten out. Press Reset, or lower Wolves."
- overshoot (event; island model passes the real 1963 count; stale on Reset): "The herd has outgrown its lichen.
  Lichen grows back very slowly."
- energyView (how; first Energy flow view; stale on switching back to Herd view): "Each level keeps only about a tenth
  of the energy from the level below."

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
- `Landscape(el, {backdrop, species, counts})`: places each species' painted cutouts (poses mixed by seeded draw,
  sized by row depth) over a painted backdrop, with "1 animal = N" scaling past a cap and crossfades between
  backdrops.
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
- Number checks (Python, 2026-10-29, the yearly step above): every worked run reproduces (forest 10 deer passes 150 in
  year 10, peak 305.6 in year 12; wolves 1 to 6 settle at 285.8 to 218.6; fire 111 then 300 by year 30; winter 210;
  size 0.5 holds 150, 0.25 holds 75, 2.0 holds 600; island 1,435 in 1957, peak 6,432.9 in 1962, 392 in 1964, 136;
  lichen 0.05 settles at 1,361.1 and 0.002 at 54.4, both peaking at 6,433; logistic 122.8 at year 10, 227.0 at 15).
  Worst cases: Wolves set from year 0 eat out the default herd of 10 at 2 wolves or more, a herd of 50 at 3 or more,
  100 at 4 or more (any herd under about 207 at 6 wolves); fire and hard winter in the same year drop 300 to 21, which
  recovers. Fixed: the tip "the forest gets more browse left over" was wrong in this model (browse left stays at the
  30 unit minimum; each deer eats more instead); the wolves' energy level is 0.2 percent of plant energy, not 1
  percent; added the die-out note and line.

## Done when
1. Herd, defaults: the herd passes 150 in year 10, peaks at about 305.6 in year 12, and holds 300 from year 15; the K
   readout says 300.
2. Forest size 0.5 levels at 150; 4 wolves from year 20 settle at about 244.6, with wolf cutouts at the margin.
3. Fire in year 25 drops the herd to about 111, crossfades to the burned forest edge and is back to 300 by year 30; a
   hard winter shows the winter backdrop and drops the herd to about 210.
4. Island model: 1,435 in 1957, peak 6,433 in 1962, crash to 392 by 1964, then 136; real points sit beside it and the
   grazed tundra fades in as lichen falls.
5. Lichen regrowth 0.05 still peaks at 6,433 but settles at about 1,361 (0.002 settles at about 54).
6. Logistic overlay with K 300 and r 0.300 reads about 122.8 at year 10; dragging K moves the curve, not the model.
7. Energy flow view prints three levels with the 10 percent rule (4 wolves: 216,000, 21,600 and about 440 kJ).
8. Focus: the population chart is the largest thing on the stage in both modes, at 1366x768 and in the 680x425
   preview.
9. A tap while Play runs: pressing Fire puts its mark on the chart at once and the next year shows the burn; moving
   Wolves changes the readout at once.
10. 2 wolves from year 0 with a start herd of 10 shows the die-out note and line.
11. All controls work by keyboard; main controls visible at 1366x768 and 680x425; chart readable at 375 wide.
12. Each how-to line speaks once in five repeated actions; event lines speak each event; no network, no em dashes.

## Open questions
- [carrying-capacity] The Wolves slider stops at 6 because the pack never starves here; at 7 or more the herd
  collapses, which would mislead. OK to cap it, or show the collapse with a "real wolves would starve first" note?
- [carrying-capacity] The checks found the same problem below 7: 2 or more wolves set before the herd grows eat out
  the default herd of 10. The revision adds a die-out note and line rather than changing the model. Enough, or should
  the pack shrink when deer are few (a model change)?

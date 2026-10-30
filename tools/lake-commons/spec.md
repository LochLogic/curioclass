# Lake Commons

Renamed from: Island Economy

## One idea
Run a lake town for 100 years in five-year turns: set how many boats fish, how much forest is cut, where new homes go
and how the town gets its energy, then live through good years, floods and droughts; fish, forest and water are
linked, so a town that takes about what grows back keeps going for its great-grandchildren and one that takes more
watches the lake empty.

## Not like
- trade-island (gr 12 social studies, built): two islands trading goods. Here no trade and no island: one town
  sharing one lake, and the lesson is regrowth and limits, not prices.
- predator-prey-island, imaginary-island, idiom-island: other island tools. The lake setting and the renamed title end
  the clash (the overlap note's reshape, taken).
- town-planner-disaster-ready (gr 4 tycoon): energy and flood readiness for a town in one sitting. Here a century of
  turns where today's choices set the next generation's lake.
- carrying-capacity (gr 9 biology, ecosystem family): a population growing to its limit. Here people harvest the
  growth, and the forest changes the lake's limit.
- grid-operator (gr 12 environmental, this wave): a city's power mix. Here energy is one choice among four, scored by
  what it does to fish and forest.
- reserve-designer (gr 9 biology): protecting habitat. Here using a resource without using it up.

## Who and how
Grade 9, Earth and space science (Resources and Sustainability). Students drive, alone or in pairs, 30 to 45
minutes (one century). Explore first: the town opens at year 0 with sensible settings already in place; pressing `Next
5 years` is enough to start.
Topic line: "resources and sustainability".
Standards: HS-ESS3-1, HS-ESS3-2, HS-ESS3-3, HS-ESS3-4.
tool.json: driver "students", minutes "30-45", modes ["Town", "Field Guide", "Century Report"].

## Screens and modes
Header (kit, 9-12 theme): "Lake Commons", small line "Take what grows back." Modes `Town`, `Field Guide`, `Century
Report`; kit `Motion`, `Sound`, `Read`.

### Town (default)
Focus: the painted lake town, the biggest thing on the stage, with the year banner "Year 35 of 100" and the year card
over its top edge; the readouts run as a sparkline strip under it. Stage: the painted lake town (Art, lake-town) seen
from a low hill at a slant, with painted cutouts placed on it and code effects over it. The scene changes with the
numbers:
- Forest: stump patch cutouts cover the forested hills in proportion to forest lost (one patch per 400 ha below
  8,000, up to 20, placed in a fixed seeded order across the slopes); above 8,000 ha nothing is added.
- Fish: shimmer density on the water (code), clipped to the lake outline the builder traces once over the picked
  image.
- Mud: a brown code tint clipped to the same outline after a flood, fading over the next two years.
- Boats: one boat cutout on the water per 5 fishing boats (up to 12); after a collapse they sit tied at the docks.
- Homes: hillside and floodplain house cutouts added as homes are built (one per 10 homes), on fixed spots on the
  slopes and on the meadow by the river mouth.
- Builds: dam, solar array, fish ladder, buffer strips and water treatment plant cutouts appear on fixed spots when
  bought.
- Indicator species: their cutouts sit in a row along the readout strip, full color when seen and a dim outline when
  not.
Panel, Choices (set once per turn): Fishing boats (0 to 60, default 25), Logging (0 to 300 hectares a year, default
64, what the forest regrows each year at 8,000 ha), New homes this turn (20 homes): `Floodplain` (default) / `Hillside`,
Energy: `Firewood` (default) / `Small dam` / `Solar` (switch any
turn, paying the build cost once), Builds (one time each): `Fish ladder` (needs the dam), `Buffer strips`, `Water
treatment`.
Panel, Readouts with small 100-year sparklines: fish in the lake (t), catch per year (t), forest (ha), homes (on
floodplain / hillside), treasury ($), boil-water days, species seen (of 6).
- `Next 5 years` (Space) plays five years at about 1 s each (5 s in all): a year card flips for each (Normal, Good year, Flood
  year, Drought year) with what it did ("Flood: 40 floodplain homes damaged, the lake muddied, fish down 4 percent").
- Every 25 years a generation marker pauses play: "Your children take over the town" (year 25), "grandchildren" (50),
  "great-grandchildren" (75), with a one-line look at the lake then and now and "Press Next 5 years to go on".
- `Calm years` toggle (set before year 0): every year Normal, for clean experiments.
- `Replay same years` (after a century): restarts with the same year sequence so two strategies meet the same weather.
- `New town` starts over with a new seed.

### Field Guide
Focus: the open card's live diagram, centered and large; the other cards sit as a list beside it. Cards that explain
the model in plain words, each with a small live diagram: how fish regrow (fastest at half full),
how forest regrows, how forest protects the lake (less mud), floods and the floodplain, droughts and stored water,
energy choices (cost and benefit table), the three builds, and the six indicator species with what each needs (each with its painted cutout).

### Century Report
Focus: the four century charts with the generation markers, filling the stage. After year 100 (or open any time for the run so far): charts of fish, catch, forest and treasury over the century with
the generation markers; totals; a strip "Town still going at year 100: yes / no" with the reasons; and a side by side of
the last two runs if `Replay same years` was used. `Copy report` (plain text to paste into class work; nothing is ever loaded back from it).

## Content
Model, one step per year (all values made up for the lab, in realistic proportions):
- Forest W (ha): W_next = W + 0.04 W (1 − W / 10,000) − cut. Start 8,000 ha. Cut = logging + 30 ha a year if energy is
  firewood + 2 ha per hillside home when built. Regrows fastest at 5,000 ha (100 ha a year).
- Lake limit K (t of fish) = 1,000 × (0.6 + 0.4 × W / 10,000): a forested shore keeps mud out. At 8,000 ha, K = 920.
- Fish F (t): F_next = F + r F (1 − F / K) − catch, catch = 0.01 × boats × F. r = 0.5; with the dam 0.35; dam with fish
  ladder 0.45. Start 800 t. With the forest full (K 1,000), the most the lake can give year after year is 125 t at 25
  boats.
- Collapse: fish under 50 t ("the fishery has collapsed"; boats earn almost nothing).
Year types (seeded; Calm years makes all Normal): Normal 60 percent, Good 20 (r × 1.4, forest growth × 1.25), Flood 10,
Drought 10 (r × 0.5, forest growth × 0.5).
- Flood: each floodplain home is damaged ($20,000; half with the dam); mud cuts fish by 20 percent × (1 − W / 10,000),
  half that with buffer strips; if forest is under 6,000 ha and there is no water treatment, 30 boil-water days.
- Drought: without the dam, 60 days of water rationing; with the dam, none.
Money (made up): start $500,000. Income: fish $1,000 a tonne, timber $500 a hectare. Build costs: small dam $400,000,
solar $600,000, fish ladder $150,000, buffer strips $100,000, water treatment $300,000; firewood free. Homes: hillside
$10,000 more per home than floodplain. The treasury may go negative ("in debt"); the report counts it.
Energy choices (Field Guide table): firewood (free, 30 ha a year of forest); small dam (one cost, stores water against
droughts, halves flood damage, slows fish regrowth unless a fish ladder is built); solar (highest one cost, no effect on
fish or forest).
Indicator species (seen while the rule holds): trout (fish over 300 t and no dam, or dam with ladder), otter (fish over
200 t), osprey (fish over 150 t and forest over 2,000 ha), heron (forest over 4,000 ha), salamander (forest over 6,000
ha), mayflies (no boil-water days in the last 5 years).
Town still going at year 100: fish at least 50 t, forest at least 1,000 ha, treasury at least $0.

Check values, Calm years, start fish 800 t and forest 8,000 ha, new homes on the floodplain:
| Boats | Logging (ha/yr) | Energy | Year 100 fish (t) | Catch per year at 100 | Forest at 100 | Notes |
|---|---|---|---|---|---|---|
| 25 | 64 | solar | 460.0 | 115.0 | 8,000 | steady from about year 25; income $147,000 a year |
| 25 | 64 | small dam | 262.9 | 65.7 | 8,000 | trout gone |
| 25 | 64 | dam and ladder | 408.9 | 102.2 | 8,000 | |
| 25 | 64 | firewood (94 cut) | 433.9 | 108.5 | 6,679 | forest still falling |
| 35 | 64 | solar | 276.0 | 96.6 | 8,000 | more boats, smaller catch than 25 boats |
| 50 | 64 | solar | 17.3 | 8.7 | 8,000 | collapse (under 50 t) in year 32 |
| 25 | 200 | solar | 300.0 | 75.0 | 0 | forest under 1,000 ha in year 61 |
| 20 | 0 | solar | 598.9 | 119.8 | 9,958 | |
Flood rule check: forest 8,000 ha, fish 460 t: no buffer strips, fish to 441.6 t; with buffer strips, 450.8 t.
Steady state with 25 boats and 64 ha: 0.04 × 8,000 × 0.2 = 64 ha regrows each year; F = 920 × (1 − 0.25 / 0.5) = 460,
catch 0.25 × 460 = 115.

## Interactions in detail
- Choices stay live while years play: a change applies from the next year that plays (the choice shows "from year
  N" beside it at once), and a build bought mid-turn appears on the scene at once. Builds are permanent once bought.
- Switching energy away from the dam keeps the dam (and its fish effect) unless `Remove dam` ($100,000) is chosen; the
  Field Guide says why removing it helps the fish.
- Year results apply in order: forest, then lake limit, then fish growth and catch, then the year type's events.
- Numbers shown rounded (fish to 1 t, forest to 10 ha, money to $1,000); the model keeps full precision.
- Collapse is recoverable: with few boats the fish slowly return (the report shows how long).
- Sound starts on (kit): lake water and birds whose number follows the species count; a rumble on flood years; off
  with Sound.
- Keyboard: Space = Next 5 years, Tab through choices, arrows on sliders; C toggles Calm years before year 0.
- Layout by real stage pixels: wide (scene with panel at side), compact, stack (375 wide: readouts as a strip of
  chips over the scene, choices in a drawer).
- Mode change: `Curio.stop()`, `V.hush()`. The current game and the last two reports per device (localStorage
  `curio-island-economy`, try/catch; the key keeps the old id), `New town` and `Clear reports`.

## Look
Accent (`--brand`) #7cac64, lake reed green: 6.55:1 on --panel #141b25, 6.20:1 on --sec-bg #18202b; --brand-ink #10161f
on it 6.87:1. Moved off brighter greens near virtual-gallery (#b8e07a) and half-life-dice (#97c059); nearest now
half-life-dice (ΔE 17); trade-island and the other island tools use sea blues and sands.
Scene: the painted lake town carries its own colors (lake blues, forest greens, warm roofs); the code layers add
muddy water #7a6a4a as a tint after floods and the fish shimmer in #e8edf3. The year banner and year card sit on a
#10161f panel at 85 percent so their text holds 15:1 or more over any part of the picture.
Sparklines: fish `--gr-1`, forest `--gr-3`, treasury `--gr-2`, damage `--gr-4`.

## Art
Local FLUX (`scripts/localart.py`), no people. 17 images. The house style in `art/prompts.json` (soft painterly,
early morning light, calm, deserted, no lettering) covers every piece.
- lake-town (drawn, review pending): a calm lake town seen from a low hill at a slant, forested hills around a blue
  lake, small wooden docks, a cluster of small houses, a river mouth with a green floodplain meadow; 16:9; cutout no;
  people no; the Town scene under every cutout and code layer.
- Town kit (one shared prompt: "a single small object for a painted lake town, seen from a low hill at a slant, soft
  morning light", one cutout per piece): lc-stumps-a and lc-stumps-b (a patch of cut tree stumps and bare brown
  ground, two shapes), lc-boat (a small wooden fishing boat with an outboard motor), lc-house-meadow (a small wooden
  cottage with a brown roof), lc-house-hill (a small two-story house with a gray roof on a stone footing), lc-dam (a
  small concrete dam with a spillway), lc-solar (a short row of solar panels on a frame), lc-ladder (a concrete fish
  ladder of stepped pools beside a dam), lc-buffer (a strip of shrubs and young willows along a stream bank),
  lc-treatment (a small water treatment building with two round open tanks, plain walls); 4:3; cutout yes; people no.
  Sizing: one scale for the whole kit, set so a cottage is 4 percent of the scene's height on the near meadow; pieces
  on the far slopes shrink to 70 percent; stump patches are 9 percent of the scene's width.
- Species kit (one shared prompt: "a single animal in natural colors, side view, whole body, soft daylight", one
  cutout per piece): lc-trout (a brook trout), lc-otter (a river otter standing on all fours), lc-osprey (an osprey
  with wings spread), lc-heron (a great blue heron standing), lc-salamander (a spotted salamander), lc-mayfly (a mayfly
  with upright wings and long tails); 1:1; cutout yes; people no. Sizing: all six the same height, 40 px in the
  readout strip and 96 px on the Field Guide cards.
Fish shimmer, mud tint, rain and sun effects, year cards, charts and sparklines stay in code.

## Voice
`easy-coach` (Umbriel), style "Say in an easy-going, warm way, like an old fishing guide on the dock telling the
town's story." Changed from gentle-storyteller, which equilibrium-seesaw (a listed neighbor) uses; no tool that
`neighbors.py` lists for this one uses easy-coach. `Curio.voice`, `scope: () => state.mode`. How lines speak once per
page load, then only update the hint; event lines speak each time.
- town (how; Town welcome; stale once Next 5 years is pressed): "Set your boats and your logging, then press Next
  five years."
- flood (event; each flood year card; stale after the turn): "A flood year. Homes by the river took the water first."
- collapse (event; the fishery collapses; stale when fish recover above 100 t): "The nets come up empty now. The lake
  needs time. Try fewer boats."
- generation (event; each generation marker; stale on the next): "A new generation takes over the town. Press Next
  five years to go on."
- guide (how; Field Guide welcome; stale once a card opens): "Tap a card to open it. Each one shows one link between
  fish, forest and water."
- report (how; Century Report welcome after year 100; stale on a mode change): "Here is your century. Press Replay
  same years to try another way with the same weather."
- reportEarly (how; Century Report welcome before year 100, when Replay same years is still disabled; stale on a mode
  change): "Here is your century so far. Go back to Town and press Next five years to finish it."

## Family engine
none. Charts use `kit/graphing.js` `Plane` if present; otherwise the tool's own SVG.

## Sources
- Logistic growth and maximum sustainable yield (half of the limit, r K / 4): OpenStax, Biology 2e (2021), 45.3
  "Environmental Limits to Population Growth"; NOAA Fisheries, "Glossary: maximum sustainable yield",
  https://www.fisheries.noaa.gov/
- Forest cover reduces erosion and sediment reaching lakes and streams: USGS, "Sediment and Suspended Sediment",
  https://www.usgs.gov/special-topics/water-science-school/science/sediment-and-suspended-sediment
- Dams block fish migration; fish ladders: NOAA Fisheries, "Fish Passage", https://www.fisheries.noaa.gov/topic/
  habitat-conservation (fish passage)
- Floodplains and flood risk: FEMA, "Flood Zones", https://www.fema.gov/glossary/flood-zones
- Riparian buffer strips filter sediment: US EPA, "Riparian Buffers", https://www.epa.gov/nps
- Commons and overharvest: Ostrom, "Governing the Commons" (1990); NOAA Fisheries, "Status of Stocks" (overfishing
  terms).
- The town, rates, prices and year odds are made up; every check value computed in Python (2026-10-27).
- Number checks (Python, 2026-10-29, the yearly step in the stated order: forest, then lake limit, then fish growth
  and catch): every table row reproduces except two, now fixed: firewood gives 433.9 t (was 434.0) and 20 boats with
  no logging 598.9 t (was 598.8); the old values came from computing the lake limit with last year's forest. Steady
  state 460 t, 115 t a year. Worst cases: 60 boats collapse in year 11; logging 300 ha a year takes the forest under
  1,000 ha in year 33; a collapsed lake (50 boats to year 40, then 5 boats) is back above 100 t in year 43. Catch by
  boats at steady state peaks at 25 boats (115 t; 20 and 30 boats both 110.4). Flood rule 441.6 and 450.8 t.

## Done when
1. Calm years, default settings with solar energy (25 boats, 64 ha): year 100 fish 460 t, catch 115 t a year, forest 8,000 ha.
2. Calm years, 50 boats: the collapse line plays in year 32 and fish read 17 t at year 100.
3. Calm years, 35 boats catch 96.6 t a year at year 100, less than 25 boats' 115.
4. Small dam without a ladder: fish settle at 263 t and trout leave the species list; adding the ladder brings fish to
   409 t and trout back.
5. Logging 200 ha a year: forest under 1,000 ha in year 61; the report says "Town still going: no (forest)".
6. A flood year with forest 8,000 ha and fish 460 t takes fish to 441.6 t (450.8 with buffer strips) and damages every
   floodplain home.
7. `Replay same years` gives an identical year card sequence; the report shows both runs side by side.
8. Generation markers pause at years 25, 50 and 75 with the line spoken each time.
9. How-to lines once each; event lines as listed; the report line never names Replay same years before year 100.
10. Focus: the painted town is the largest thing in Town at 1366x768 and 680x425; stump patches appear as the forest
    falls and the boats tie up after a collapse.
11. A tap while years play: moving Fishing boats mid-turn shows "from year N" at once and the next year uses it.
12. Scene, choices and readouts usable at 1366x768; drawer at 375 wide; labels at least 10 px in the 680x425 preview;
    no network, the 17 images load, no em dashes.

## Open questions
- [island-economy] Take "Lake Commons" (the overlap note's reshape) as the new title? The spec is written for it.
- [island-economy] Indigenous lake communities have long managed shared fisheries; should the Field Guide add a sourced
  card on that history (with a Native educator's review), or keep the town fictional and generic?

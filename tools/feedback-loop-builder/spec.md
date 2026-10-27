# Feedback Loop Builder

## One idea
Draw arrows between parts of the Earth system and mark each one + or −; close a loop and the tool counts its minus
signs (even amplifies, odd stabilizes), then sends a nudge around it lap after lap so you watch the change grow and
settle, or die away, and finally add living things to the loops and see life and air change each other over billions
of years.

## Not like
- body-thermostat (gr 9 biology, this wave): one body's balancing loop holding a set point. Here many Earth loops,
  amplifying and stabilizing, with no set point.
- climate-dashboard (this group): the measured records. Here the causes, drawn as a system.
- carrying-capacity (gr 9 biology, ecosystem family): population limits. Here loops that join ice, air, rock and life.
- slope-field-garden (gr 12 math, wave 2): growth laws as differential equations. Here no equations beyond a ratio
  per lap; the system's structure is the lesson.
- reserve-designer (gr 9 biology): designing habitat. Here life changing the planet's air and climate.

## Who and how
Grade 9, Earth and space science (Earth's Systems and Feedback). Students drive, 30 to 45 minutes. Explore first:
Build opens with four nodes already linked into the ice and albedo loop, the arrow from Reflectivity to
Sunlight absorbed still waiting for its sign.
Standards: HS-ESS2-1, HS-ESS2-2, HS-ESS2-3, HS-ESS2-7.
tool.json: driver "students", minutes "30-45", modes ["Build", "Earth's Loops", "Life Joins In"].

## Screens and modes
Header (kit, 9-12 theme): "Feedback Loop Builder", small line "Count the minus signs." Modes `Build`, `Earth's
Loops`, `Life Joins In`; kit `Motion`, `Sound`, `Read`.

### Build (explore, default)
Stage: a canvas of round nodes. A palette on the side holds the node set (Content), grouped `Ice and sun`, `Air and
ocean`, `Rock and deep Earth`, `Life`. Drag a node onto the canvas; drag from one node's edge to another to draw an
arrow; tap the arrow's badge to cycle its sign `+` (more causes more) / `−` (more causes less) / `?`.
- When arrows close a loop, the loop glows and a label appears in its middle: "R: amplifying (0 minus signs)" or "B:
  stabilizing (1 minus sign)". Several loops can share nodes; each gets its own label, listed in a side table.
- `Nudge`: pick a node in the loop and press `Nudge` (Space). A pulse travels the loop; each lap the change is
  multiplied by the loop strength (slider 0.1 to 1.2, default 0.5). A lap counter and a small bar chart show each lap's
  change and the running total ("after 6 laps: +1.97 of a possible +2.00").
- Strength 1.0 or more on an amplifying loop: the bars keep growing and the note says "Runaway: this never settles.
  Earth's main climate feedbacks today add up to about 0.64, strong but below 1."
- `Clear canvas`, `Undo` (Ctrl+Z), `Tidy` (auto-lays out the nodes in a circle per loop).

### Earth's Loops
Evidence cards, one per real loop (Content). Each card has a mini loop already drawn, its sign count, how fast it
works, how strong it is (with the IPCC numbers for the four climate feedbacks) and a source line. `Open in Build`
places the loop on the canvas to nudge.
A `Stack the feedbacks` panel: start with doubled CO2 and only the outgoing heat (Planck) response, 1.22 °C; add water
vapor, then ice and albedo, then clouds with toggles; the lap chart shows the total climbing to 3.42 °C with all four,
beside the IPCC's assessed best estimate of 3 °C (likely 2.5 to 4) from all lines of evidence.
A `Deep Earth` card set (HS-ESS2-1, HS-ESS2-3): the plate engine (heat from the mantle drives convection, plates move,
subduction feeds volcanoes, volcanoes build mountains and release CO2, erosion wears mountains down and carries
sediment to the sea) and the rock thermostat (weathering), each with its time scale.

### Life Joins In
For HS-ESS2-7. A deep time strip (4 billion years ago to now) with event cards (Content); click a card to read its
evidence and build its loop or chain on a small canvas. A claim panel: "Life changed the air, and the air changed what
could live." Drag evidence cards into `Supports` or `Does not fit`; `Check` explains each.
Loops to build here: Plants and CO2 (B), Forests and rain (R), Roots and weathering (B), and the oxygen chain
(cyanobacteria → oxygen → ozone → UV shield → life on land), shown as a one-way chain, not a loop.

## Content
Node set: Temperature, Sea ice and snow, Reflectivity (albedo), Sunlight absorbed, Outgoing heat, Water vapor, CO2 in
air, Ocean CO2 uptake, Permafrost thaw, Rock weathering, Rain, Mantle heat, Plate motion, Volcanoes, Mountains,
Erosion, Plants and plankton, Forests, Oxygen, Ozone, Life on land.
Loop rule: count the − links around the loop; an even count (including zero) is reinforcing, an odd count is
balancing. Lap model: each lap multiplies the change by the strength g; a reinforcing loop's total settles at 1 /
(1 − g) times the first nudge when g < 1 (g 0.5: 1, 0.5, 0.25, 0.125, ...; total 2.00); a balancing loop's laps
alternate sign (g −0.5: 1, −0.5, 0.25, −0.125, ...; total 0.67).

Earth's loops (signs, type, speed, strength):
- Ice and albedo: Temperature − Sea ice; Sea ice + Reflectivity; Reflectivity − Sunlight absorbed; Sunlight absorbed
  + Temperature. Two minus: reinforcing. Years to decades. Open ocean reflects about 6 percent of sunlight, bare sea
  ice 50 to 70 percent, snow-covered ice up to 90 percent (NSIDC). Strength +0.35 W/m² per °C (very likely 0.10 to
  0.60). The Arctic warmed nearly four times faster than the globe from 1979 to 2021, largely from sea ice loss.
- Water vapor: Temperature + Water vapor + Temperature. Zero minus: reinforcing. Days to weeks. With lapse rate,
  +1.30 W/m² per °C (1.1 to 1.5).
- Outgoing heat (Planck): Temperature + Outgoing heat − Temperature. One minus: balancing. Immediate. −3.22 W/m² per °C
  (−3.4 to −3.0). The strongest loop; it is why Earth's climate settles.
- Clouds: drawn with a `?` sign that the card fills as +0.42 W/m² per °C (−0.10 to 0.94): likely amplifying, least
  certain.
- Ocean CO2: Temperature − Ocean CO2 uptake − CO2 in air + Temperature. Two minus: reinforcing. Decades to centuries;
  warmer water holds less dissolved gas.
- Permafrost: Temperature + Permafrost thaw + CO2 in air + Temperature. Reinforcing. Decades to centuries.
- Plants and CO2: CO2 in air + Plants and plankton − CO2 in air. One minus: balancing. Years.
- Rock thermostat (weathering): Temperature + Rain + Rock weathering − CO2 in air + Temperature. One minus:
  balancing. Hundreds of thousands of years; holds Earth's climate in a livable range over geologic time.
Stack the feedbacks (doubled CO2, forcing 3.93 W/m²): Planck only 3.93 / 3.22 = 1.22 °C. Each feedback as a share of
Planck: water vapor 0.404, albedo 0.109, clouds 0.130; sum 0.643. Total = 1.22 / (1 − 0.643) = 3.42 °C. Laps with
all four: 1.22, 0.785, 0.504, 0.324, 0.208, 0.134 (running 1.22, 2.01, 2.51, 2.83, 3.04, 3.18). Albedo alone 1.37;
water vapor alone 2.05. IPCC assessed: best 3 °C, likely 2.5 to 4, very likely 2 to 5 (more lines of evidence than
this model).
Deep Earth cards: Earth's interior heat (from formation and radioactive decay) drives mantle convection at a few
centimeters a year; seafloor forms at ridges and sinks at trenches; mountains rise at collisions and erode over
millions of years; volcanoes return carbon to the air, weathering and burial take it back.

Life Joins In cards (age, evidence):
- About 3.4 billion years ago: stromatolites, layered mats built by microbes (Strelley Pool, Australia).
- About 2.4 billion years ago: the Great Oxidation Event. Oxygen from cyanobacteria builds up in the air; dissolved
  iron in the oceans rusts out as banded iron formations.
- Oxygen in the air lets an ozone layer form, which blocks much of the Sun's UV.
- About 470 to 360 million years ago: plants spread across land; roots break rock faster, weathering draws down CO2 and
  the climate cools.
- 359 to 299 million years ago (Carboniferous): swamp forests bury carbon as coal; oxygen climbs.
- Today: ocean plankton do close to half of Earth's photosynthesis; forests like the Amazon recycle their own rain.
Claim evidence sort (Supports / Does not fit): the six cards above support; two decoys do not fit ("The Moon's craters
are 4 billion years old", "Earth's orbit changes over 100,000 years"), each with a reason.

## Interactions in detail
- Arrows: one per ordered pair; a second drag between the same nodes flips direction. Self-loops are refused.
- Loop finding: all simple cycles up to 8 nodes (Johnson's algorithm); an arrow with `?` makes its loops grey with
  "set every sign to classify".
- Nudge: strength is per loop (each loop's row in the side table has its own slider); with shared nodes the nudge runs
  one loop at a time, chosen in the table. Laps animate 0.8 s each, up to 12 laps; Motion off shows the bar chart only.
- Card loops opened in Build keep their real signs and use strengths that match the card (ice and albedo 0.11, water
  vapor 0.40, combined 0.64; balancing loops −0.5 as a teaching value, labeled).
- Extremes: g ≥ 1 on a reinforcing loop stops at 12 laps with the runaway note; a balancing loop at −1 or below shows
  "swings that never settle" and stops at 12.
- Sound: a soft chime per lap, pitch rising for reinforcing and falling for balancing; off with Sound.
- Keyboard: Tab through nodes and arrows, Enter to select, arrow keys to move a node, S to cycle a sign, Space =
  Nudge, Delete removes the selection; focus({preventScroll: true}).
- Layout by real stage pixels: wide (palette left, canvas, table right), compact (table under), stack (375 wide:
  palette as a bottom drawer).
- Mode change: `Curio.stop()`, `V.hush()`. The canvas and claim sort per device (localStorage
  `curio-feedback-loop-builder`, try/catch), `Clear canvas`.

## Look
Accent (`--brand`) #ffb0d9, aurora pink: 10.27:1 on --panel #141b25, 9.74:1 on --sec-bg #18202b; --brand-ink #10161f
on it 10.78:1. Far from body-thermostat's #e25a7e and every group sibling (nearest star-life-story #b894d0 at ΔE 24); mitosis-mixer #f1b1ed
sits at ΔE 12.
Nodes colored by sphere: ice #c8e4ff, air #9fb4d9, ocean #4f8fd0, rock #b08a6a, life #6fc78a, all with #10161f labels
(over 7:1). Reinforcing loops glow `--gr-4`, balancing loops `--gr-1`; arrows #e8edf3 with + badges in `--gr-3` and −
badges in `--gr-2`. Canvas #121821 with a faint dot grid.

## Art
none: drawn in code (nodes with small sphere icons, arrows, loops, bar chart, deep time strip, cards, preview.svg).

## Voice
`wise-mentor` (Gacrux), style "Say thoughtfully and warmly, like a wise high school mentor who loves big systems."
No group sibling uses it; shared in 9-12 science only with gas-law-lab (gr 10 chemistry), far in topic (23 kept voices
for 31 science tools). carrying-capacity's science-narrator stays clear of this loop tool. `Curio.voice`, `scope: () => state.mode`.
- build (how, Build welcome): "One arrow is missing its sign. Tap it, then press Nudge."
- loop (event, a loop closes; stale when it opens again): "A loop. Count the minus signs."
- runaway (event, runaway note shown; stale on a strength change): "That loop never settles. Earth's real loops are weaker."
- earth (how, Earth's Loops welcome): "Open a card, then stack the feedbacks to see where three degrees comes from."
- life (how, Life Joins In welcome): "Walk the time line. Each card shows life changing the air, or the air changing life."
- sorted (event, claim sort all right; stale on Clear): "Every card is in the right pile."

## Family engine
none. Bar charts use `kit/graphing.js` `Plane` if present; otherwise the tool's own SVG.

## Sources
- Feedback strengths, forcing for doubled CO2 (3.93 W/m²), climate sensitivity: IPCC AR6 WG1 (2021), chapter 7,
  Table 7.10 and section 7.5, https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-7/
- Albedo of ocean, sea ice and snow: NSIDC, "Thermodynamics: Albedo", https://nsidc.org/learn/parts-cryosphere/sea-ice/
  science-sea-ice
- Arctic warming nearly four times the global rate 1979 to 2021: Rantanen et al. 2022, Communications Earth and
  Environment 3:168.
- Loop polarity by counting negative links: Sterman, "Business Dynamics" (2000), chapter 5; Meadows, "Thinking in
  Systems" (2008).
- Weathering thermostat: Walker, Hays and Kasting 1981, Journal of Geophysical Research 86:9776.
- Land plants and CO2 drawdown: Berner 1997, Science 276:544. Great Oxidation Event and banded iron: Lyons, Reinhard and
  Planavsky 2014, Nature 506:307. Stromatolites about 3.4 billion years: Allwood et al. 2006, Nature 441:714. Ocean
  share of photosynthesis: Field et al. 1998, Science 281:237. Carboniferous dates: International Commission on
  Stratigraphy, Chart 2023/09.
- Mantle convection, plates, seafloor and mountains: USGS, "This Dynamic Earth", https://pubs.usgs.gov/gip/dynamic/
- Lap totals computed in Python (2026-10-27).

## Done when
1. Build's starting loop gets its last sign: with − it reads "R: amplifying (2 minus signs)"; with + it reads "B:
   stabilizing (1 minus sign)".
2. Nudge at strength 0.5 on a reinforcing loop shows laps 1, 0.5, 0.25, ... and "after 6 laps: +1.97 of a possible
   +2.00"; on a balancing loop the total heads to 0.67.
3. Strength 1.1 on a reinforcing loop stops at 12 laps with the runaway note.
4. Stack the feedbacks: Planck 1.22, all four 3.42, albedo alone 1.37, water vapor alone 2.05, beside "IPCC best 3 °C".
5. Each Earth's Loops card opens in Build with the right sign count (Planck 1, ice and albedo 2, weathering 1).
6. Life Joins In: the six evidence cards support and the two decoys do not fit; "Every card is in the right pile."
7. A canvas with two loops sharing Temperature lists both in the table with separate sliders.
8. How-to lines once each; event lines as listed.
9. Canvas, palette and table usable at 1366x768; drawer at 375 wide; labels at least 10 px in the 680x425 preview; no
   network, no images, no em dashes.

## Open questions
- [feedback-loop-builder] HS-ESS2-1 and HS-ESS2-3 (landforms, Earth's interior) are covered only by the Deep Earth
  cards in Earth's Loops. Enough, or should the module's interior standards get their own tool later?
- [feedback-loop-builder] The lap model with fixed strengths is a teaching model; the 3.42 °C it reaches is shown
  beside the IPCC's 3 °C. OK to show both, or show only the IPCC value?

# Living Pond (Curiosity No. 13)

Tool id stays `living-pond`. Plate: `Curio Class Curiosities · No. 13 · Living Pond`. Build brief:
docs/agents/CODEX-CURIOSITY.md. In `tool.draft.json`: `"curiosity": true`, `"plate": 13`.

## The real thing
An ecologist's study tank: a cut-away pond with a strip-chart recorder, an oxygen meter and a thermometer bolted to
it. Stock it, net it, feed it, shade it, change its bottom, then let it run through spring blooms, summer hunts, fall
die-back and winter ice. It runs on one honest rule: each kind eats, grows, breathes and dies, and every unit of matter
is passed on, never made or lost. A single change ripples through the web seasons later, a ghost line shows what would
have happened without it, and a slow drift in minnow colour shows a heron shaping a population over generations. There
are no goals. The winters and the heron are the drama.

## Map
- Anchor: science-5-food-webs-and-matter-cycles (5-LS2-1 matter among plants, animals, decomposers and environment;
  5-PS3-1 energy in food was once sunlight; 5-LS1-1 algae build from water and air).
- Also reaches: science-3-traits-and-variation (3-LS4-2), science-3-fossils-and-changing-environments (3-LS4-3),
  science-7-ecosystems-and-interactions (MS-LS2-1, MS-LS2-2), science-7-matter-and-energy-in-ecosystems (MS-LS2-3),
  science-8-evolution-and-natural-selection (MS-LS4-4, MS-LS4-6).
- Grade band 3 to 8, anchor grade 5. It takes over the Food Web Wobble card. A teacher plan would teach 5-LS2-1 and
  5-PS3-1 fully (the Matter and Energy lenses are those standards), so with a plan.md it takes the anchor's card.

## The first two minutes
- 0 to 3 s: the Starter pond is alive and running (2 weeks a second). Spring: minnows school, snails crawl on stems, a
  dragonfly nymph creeps on the mud, a painted turtle paddles, a great blue heron stands in the shallows, bubbles rise
  from the algae. The chart pen scratches a line per kind. Hint on the tank rim: "Tap a creature to drop it in."
- 3 to 20 s: the student taps the minnow on the specimen tray; one drops in with a splash and joins the school. A tap on
  the shaker sprinkles flakes and every minnow rushes up. The heron strikes: a plunk, one minnow fewer, a tick on the
  chart.
- 20 to 60 s: the water greens as algae bloom; summer on the far shore; fall leaves sink; ice creeps in from the edges
  with a crackle, the turtle tucks into the mud, the heron flies off, the oxygen needle starts to fall.
- 60 to 120 s: the ice cracks, the heron is back. The net hangs on the rim. "What if I take all the minnows out?"

## Things to do
1. Drop in creatures and shake fish food; tap any creature to see its food arrows for 3 s.
2. Net all the minnows and watch the snails starve under green water, against the dashed ghost of the untouched pond.
3. Switch to the Matter lens, tap one dot, and follow its trip: muck, water and air, algae, minnow, muck again.
4. Leave the Energy lens on for a whole year: sunlight in, about 1 percent caught, about a tenth passed up, heat out.
5. Switch the decomposers off and watch the muck pile up and the web choke; switch them back on and watch it return.
6. Run the feeder on Some for years, then Lots for two summers, and watch the oxygen needle under the ice.
7. Put down a sand bottom and watch the minnow shade strip drift paler over winters; mud drifts it darker; gravel holds.
8. Net all the dragonfly nymphs and watch the snails boom to several times their usual peak.
9. Add 30 minnows at once and ride the boom and the bust.
10. Start from an Empty pond and build a web from the algae up; see what it takes to last ten winters.
11. Shade the pond with the canopy, or turn the year Cold or Mild, and read what changes on the chart.
12. Add a second heron, or take the heron away after ten winters and watch the shade drift back.
13. Run ten winters at Fast, save the pond, and Replay it: read the chart as a history of every winter and every action.

## Controls
- Time (on the chart recorder): `Run` / `Hold` (Space), chart speed `Slow` 1 week/s, `Normal` 2, `Fast` 8 (keys < >),
  `Step` one week (period). The chart keeps scrolling only while running.
- Specimen tray (rim, 8 slots; keys 1 to 7, arrows move the drop point): Algae (5 units), Snail (0.5), Minnow (2,
  shades 2 to 5), Nymph (0.5), Turtle (30), Heron, Decomposers (5 units, 20 specks); Net (N) toggles the net: swipe
  scoops up to 6 per swipe, each slot shows `Net 1` and `all`; Escape puts it down. Decomposers cannot be netted.
- Shaker: 2 units a tap. Feeder `Off` / `Some` 3 a week / `Lots` 12 a week, weeks 6 to 38. Bottom `Sand` / `Gravel` /
  `Mud` (shade 1, 3.5, 6). Decomposers `On` / `Off`.
- New (super spec additions, defaults keep the checked model): Canopy dial `0` / `25` / `50` percent shade (sunlight
  x (1 - shade)); Year dial `Cold` / `Normal` / `Mild` (T offset -2, 0, +2 °C; Mild means no ice).
- Lens selector `Life` / `Matter` / `Energy` (L). Chart: per-line chips (show or hide), `Whole run` toggle (W).
- `New pond` (Starter or Empty; offers to save), `Save` (up to 8; `Open`, `Replay`, `Rename`, `Delete` with confirm),
  Manual (M), power panel (Motion, Sound, Read). Every control is live while running, effective the same frame.

## Readouts
- Calendar dial, tank top-left: `YEAR 3 · WEEK 22 · SUMMER`. On the chart's right end: oxygen needle 0 to 20 mg/L, one
  decimal, marks at 3 "fish gasp" and 2 "winterkill"; thermometer, whole °C; light meter, whole percent of full sun.
- Counts under the chart, monospace: algae clumps, snails, minnows, nymphs, turtle state (swimming, basking, asleep in
  the mud, walked off), heron state (fishing, flew off, back in spring).
- Shade strip: the 8 minnow shades as swatches with a marker at the school's average, `AVG SHADE 3.50`.
- Matter lens ledger: `IN POND 742.0 · ADDED 0 · TAKEN OUT 0 · WALKED OFF 0` (one decimal); the followed dot's trip.
- Energy lens ledger (this year): sunlight in, caught by algae (percent, one decimal), kept in algae, kept in plant
  eaters (percent of algae kept), left as heat, heat out against caught (percent).
- Pond log (Manual): automatic dated lines for ice, ice-out, heron and turtle comings and goings, a kind gone, oxygen
  under 2 under ice. A record, not a list of things to find.

## The Manual
A drawer, lower-left. Contents: the kinds and who eats whom; the model in plain words; the lenses; reading the chart
and the ghost; the pond log; honesty notes; sources. Things people have found (in this pond, with real-world sources):
1. Netting the minnows starved the snails: floating algae grew to 477 to 509 and shaded the algae on stems to 3.3. In
   real lakes this chain is a trophic cascade (Carpenter, Kitchell and Hodgson 1985).
2. A little fish food every summer (3 a week) was harmless for years; then rotting muck under the ice used up the
   oxygen, and 98 to 99 percent of the minnows died each winter. Real ponds winterkill this way (Minnesota DNR).
3. Producers catch only about 1 percent of the sunlight that falls on them (Lindeman 1942); here, 1.2 percent.
4. Plant eaters keep about a tenth of what the algae kept; the rest leaves as heat (OpenStax Biology 2e 46.2); here,
   9.5 to 12.8 percent.
5. With no dragonfly nymphs, the snails' yearly peaks reached 65 to 119 instead of 18 to 77: predators hold prey down.
6. On sand, with the heron fishing by sight, the minnows drifted from shade 3.5 to 1.2 in ten winters; on mud, to 5.8;
   on gravel they stayed at 3.50. Guppies under predators did the same (Endler 1980).
7. Green water hid the minnows from the heron and slowed their drift: shade 1.20, 1.53, 1.97 at 0, 2 and 4 food a week.
8. With the decomposers off, muck held 95 percent of the matter after a year, and the turtle walked off before any kind
   died out. Switched back on, the algae passed 100 units in 35 weeks.
9. Cold water holds more oxygen than warm water: about 14.6 mg/L at 0 °C, about 9 at 20 °C (USGS).
10. Great blue herons hunt fish by sight in shallows (Cornell Lab); this one leaves when it cannot see enough.

## Look
The grammar of an ecologist's study tank and field station: a glass-sided tank in cut-away, a strip-chart recorder
(cream gridded paper, inked lines, season bands, a moving pen), a needle oxygen meter, a glass thermometer, a light
meter, a calendar dial, a specimen tray along the rim. Palette from the pond: water `#9fd0d6` to `#2b6f7a`, green
tint `#6f9a3a` (alpha Af / (Af + 300), max 0.6), muck `#5a4632`, ice `#e8f4f8` at 85 percent; chart paper `#f4faf8`
with ink `#16302e` (13.28:1) and muted `#4c605e` (6.33:1); dragonfly teal `#0e6a73` with white (6.31:1), pressed
`#0b4f56` with white (9.26:1). Chart lines on paper, each with its own dash and an end label: algae `#5b6b2a`, snails
`#8a5a00`, minnows `#1f7a8c`, nymphs `#6b4fa0`, oxygen `#b0306a` (4.98 to 6.46:1). Ghost lines faint and dashed.
- 1366x768: tank full width, about 60 percent of the height (shore above the waterline, heron left, log right); chart
  recorder below with the instruments on its right end; tray on the tank's rim; calendar top-left; power panel
  top-right; plate and `Manual` lower-left. 375x812: tank on top (300 px or more) with a Run, speed and lens strip on
  its edge, chart 160 px, one instrument row, the tray as a scrolling row, other controls below; no sideways scroll.
- Sound (quiet, Web Audio): splash, net swish, flake ticks, heron plunk, heron leaving (two soft falling notes),
  turtle knock on the log, ice crackle and crack, season tick, a kind gone (low two-note fall), winterkill hum. One
  event sound per 150 ms; Fast plays only gone and ice.
- 60 fps on a school Chromebook: about 195 cutouts, 120 specks, 150 dots on a 2D canvas; Motion off: no swimming,
  crossfades or trails, counts still update.

## Real material and sources
The model (weekly step, 7 daily substeps), carried exactly from the super tool spec (git 018ace9b, "The model",
"Starting ponds", "Limits", "Saving", "Interactions in detail"): temperature T = 13 - 11 cos(2 pi (w - 46) / 52) °C,
rates x 2^((T - 20) / 10), ice when T < 4 (weeks 41 to 51), sun = 0.6 + 0.4 cos(2 pi (w - 14) / 52), light under ice
0.3 x sun, osat = 14.6 - 0.39 T + 0.007 T^2; algae logistic with nutrient limit (1.4, Amax 900 and 500, stems shaded by
floating algae); type II eaters, refuges algae 15, snails 4, minnows 6, nymphs 1 (cmax, H, eff, maint, mort: snail
1.0, 100, 0.30, 0.07, 0.02; minnow 1.0, 100, 0.30, 0.07, 0.015, floating algae 1, fish food 3; nymph 0.7, 35, 0.30,
0.07, 0.02, snails 1, minnows 0.5; decomposers 1.5, 100, 0.20, 0.08, 0.10, rest below 2 units); turtle 1.2 x tf a week
at 10 °C and up; heron 1.6 a week, sight visibility 0.15 + 0.85 x |k - bottom| / 7 x clarity, clarity
1 / (1 + (Af / 400)^2); minnow young 88 / 6 / 6 percent shade inheritance; oxygen budget and low-oxygen deaths; exact
matter conservation; gone rules; heron leaves after 3 poor weeks, turtle after 8; energy 10 units per unit matter,
sunlight 70,000 x sun; no randomness in the model. Starter, in units: water and air 300, floating algae 80, stems 70, snails 40,
minnows 40 (shades 2 to 5, 10 each), nymphs 12, decomposers 20, muck 150, turtle, heron, sand, oxygen 10: total 742.
Copy every number, formula and rule from that commit; where this summary and the commit differ, the commit wins.
New controls apply only as stated: canopy multiplies sun before every use; Year adds its offset to T everywhere.
Ghost: on any change, a copy runs 104 weeks ahead unchanged (under 5 ms) and draws dashed.
Model sources: OpenStax Biology 2e 46.1 to 46.3 and 45.6 (CC BY 4.0); Lindeman (1942) Ecology 23(4); Holling (1959)
Canadian Entomologist 91; Gillooly et al. (2001) Science 293; USGS Water Science School, "Dissolved Oxygen and Water";
Minnesota DNR, "Winterkill"; US EPA, "Nutrient Pollution: The Effects"; Cornell Lab, All About Birds, Great Blue Heron;
Ernst and Lovich (2009), Turtles of the United States and Canada; Britannica, "Dragonfly"; Endler (1980) Evolution
34(1); Carpenter, Kitchell and Hodgson (1985), "Cascading trophic interactions and lake productivity", BioScience 35.
Checks: every number in Things people have found comes from the super spec's Python runs (git 018ace9b, Sources).
Art: the super spec's 36 painted images (seasonal shores, strips, plants, creatures in each pose, shaker, net), no
people, about 1.3 MB WebP; chart, needles, dots and text in code. Budget about 1.6 MB (goal 2 MB, ceiling 6 MB).

## Honesty notes
- One small made-up pond: matter in units, one water-and-air pool (no nitrogen or phosphorus split), one oxygen number,
  turtle and heron as fixed adults. Rates are model values chosen so the Starter pond keeps every kind ten winters.
- Minnow generations are about a year, so a drift that takes real fish many generations shows in a few winters; the
  shade strip says "sped up". The oxygen fit runs about 0.5 mg/L high at 20 to 25 °C (USGS).
- Canopy and Year are new: the Manual claims only what the build's own runs show for them.

## Voice
`gravel-ranger` (an old ranger who has watched this pond for years). First-run hint on the rim, spoken once after the
first touch: "Tap a creature to drop it in." Then only event lines, each at most once in 20 s (maxAge 4 s): "Ice. No
new air gets in until spring.", "Oxygen's low. The minnows are gasping at the top.", winterkill, heron or turtle left,
"The snails are gone." Read speaks the calendar, oxygen, temperature, counts and the latest log line.

## Done when
1. First two minutes, no reading: the pond is running, a tap drops a minnow the same frame, ice comes inside a minute.
2. Starter pond keeps all six kinds ten winters at Fast; the Matter ledger stays 742.0; year 10 snails stay about 19 to 34.
3. Net all minnows at year 1 week 13: algae past 400, snails under half the ghost within 52 weeks, heron and turtle leave.
4. Decomposers off from week 0: muck over 90 percent in year 1, turtle leaves first; back on, algae over 100.
5. Feeder Lots for two summers gives a winterkill in year 2; Some keeps minnows ten winters. Sand moves the shade a full
   shade by year 3; gravel holds 3.50.
6. A followed dot writes its trip and reaches an animal; the Energy ledger shows heat out within 5 percent of caught.
7. Canopy and Year work, keep matter exact, and their ten-winter outcomes are reported in codex-report.md.
8. The tank is the largest thing at 1366x768, 680x425 and 375x812; Run, speed and the tray visible without scrolling.
9. Save, reload, Open: same pond, same week; Replay reproduces every mark; storage blocked still plays.
10. 60 fps at the add limits with the "1 = N" keys; keyboard reaches every control and each announces its value.
11. No score, goal, level, sticker or finish screen anywhere; no Journal of stickers, no toasts.
12. Short test passed and reported with one frame beside Beat Lab; console clean, no network, no em dashes.

## Open questions
- Canopy and Year are new controls for the concept's "seasons and light". Keep both? Lean: keep, defaults unchanged.
- Winterkill from overfeeding, said plainly for grades 3 to 8? Lean: yes; it is true and it is the pond's best lesson.
- If the art runs over, drop to two shore backdrops (summer, winter) first? Lean: yes.
- Food Web Wobble's idea card retires? Lean: yes, its content lives here.

## What changed from the super tool spec
- The 25-goal sticker Journal, toasts and chime were removed; their findings became Things people have found. Saved
  ponds stay; the pond log records events instead of awarding them.
- The kit header, `.seg` modes and right panel became a study tank, a chart recorder with instruments and a tray.
- Canopy and Year controls were added for light and seasons; defaults keep every checked number.
- The Teacher note's challenges and the voice's how lines were cut to one first-run hint and event lines.
- Kept unchanged: the model, starting ponds, limits, saving, ghost lines, lenses, art and sources.

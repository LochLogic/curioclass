# Living Pond

## One idea
A cut-away pond you stock with painted creatures and then leave alone: it runs itself through spring blooms, summer
hunts, fall die-back and winter ice on one honest rule (each kind eats, grows, breathes and dies, and every bit of
matter is passed on, never made or lost), so a single change, like netting the minnows or shaking in fish food, ripples
through the whole web seasons later, and a slow drift in minnow color shows a heron shaping a population over
generations.

## First minute
No reading needed. The Starter pond is already alive and Play is already on (Normal, 2 weeks a second).
- 0 to 3 s: a sunny spring pond fills the screen in cut-away: minnows school in the open water, snails crawl on stems,
  a dragonfly nymph creeps on the mud, a turtle paddles, a heron stands in the shallows. Bubbles rise from the algae.
- 3 to 10 s: the creature tray glows softly. The student taps or drags the minnow: a minnow drops in with a splash
  sound and joins the school. Tapping the fish food shaker sprinkles flakes and every minnow rushes to them.
- 10 to 25 s: the heron strikes (a plunk, a minnow gone). The water turns faintly green as algae bloom, the graph under
  the pond climbs, the far shore turns from spring to summer.
- 25 to 45 s: fall colors, then ice spreads across the top with a crackle; the turtle tucks into the mud, the heron
  flies away, minnows slow down. Some minnows fade and sink: the graph dips.
- 45 to 60 s: the ice cracks, spring and the heron return. Now: "what if I take all the minnows out?" The net is there.

## Not like
- food-web-wobble (taken over, grade 5): its content lives here (matter loops through decomposers, sunlight energy
  flows one way and leaves as heat, pulling a species makes the web wobble), in a pond that runs through seasons.
- predator-prey-island (grade 7, same family): real Isle Royale counts, the data. This is the toy: a pond you stock.
- carrying-capacity (grade 9, same family): one herd leveling off yearly. Here many kinds weekly, with seasons.
- energy-pyramid (grade 7, same family): builds the 10 percent pyramid. Here a tenth shows up in a running ledger.
- bug-hunt (grade 8): you are the bird. Here the heron hunts; you change the bottom and the water and watch the drift.
- habitat-hunt (grade 2), beaver-builders (K): find or make a pond. Here the pond is a system to run and break.
- lake-commons (grade 9), invasive-species-alert, leaf-factory (grade 7): a fishery with people, one invader, one leaf.
  Here no people, and all the pieces in one pond.

## Who and how
Grades 3 to 8, anchor grade 5, science (module science-5-food-webs-and-matter-cycles). Driver: students on laptops or
Chromebooks, alone or in pairs; the teacher can run it on a projector. 15 to 45 minutes, and students come back.
Standards: 5-LS2-1 (model the movement of matter among plants, animals, decomposers and the environment), 5-PS3-1
(energy in animals' food was once energy from the sun), 5-LS1-1 (plants get the materials they need for growth chiefly
from air and water: here algae build from the water and air pool). Reaches also: 3-LS4-2 and 3-LS4-3 (differences in
traits give survival advantages; some survive well in a habitat and some do not), MS-LS2-1, MS-LS2-2, MS-LS2-3
(resources, interactions, cycling of matter and flow of energy), MS-LS4-4 and MS-LS4-6 (natural selection changes
trait shares in a population over generations).
Topic line: food webs, the matter loop and energy flow in a pond.
Light theme (grades 3-5 set their own `:root`). Header: title, `.seg` modes **Pond** and **Journal**, kit buttons
`motion`, `sound`, `read`. Panel hint paragraph id `hint`.

**Teacher note** (bottom of Journal, collapsed; lists the standards above). No worksheets. Three ways in a period:
1. Free play (15 min): "Keep the Starter pond alive for five winters while changing one thing. What did your change do
   two seasons later?" Pairs tell the room one surprise.
2. A goal set (20 min): Spring bloom, Wobble, Green water, Choke the pond and Comeback; students show the sticker and
   say which arrow in the web caused it.
3. A challenge for the room (25 min): everyone starts from Empty pond; whose pond still has all six kinds after ten
   winters? Compare the stocking lists on the Journal's saved ponds.

## Screens and modes

### Shared layout
Stage (left, about 70 percent of the width at 1366x768) holds two stacked parts:
- **The pond** (top, about 62 percent of the stage height): a side cut-away of a small pond. Layers top to bottom: the
  painted far-shore backdrop for the season (sky and shore above the waterline), the surface (lily pads, the floating
  algae mat as it grows, ice in winter), open water (minnows, flakes, falling dead bits), stems and stones on both
  sides (cattails, pondweed, algae on stones, snails), the bottom strip (sand, gravel or mud, chosen by the Bottom
  control) with the muck layer on top of it (its thickness follows muck units), and the basking log at the right
  shore. The heron stands in the left shallows. **The pond is the focus** and the largest thing on screen in every
  size.
- **The graph** (below, about 38 percent): `PopChart` with weeks on x (the last 2 years, scrolling; a "whole run"
  toggle shows everything), how many on y. Lines: algae clumps, snails, minnows, nymphs (counts as cutouts, see
  Content), with legend chips that hide or show each line. Season bands shade the x axis (spring, summer, fall,
  winter) and the ice weeks get a pale blue band. A small oxygen gauge sits at the graph's right edge ("Oxygen in the
  water", a vertical bar with the 3 mark labeled "fish gasp" and the 2 mark labeled "winterkill"). **Ghost lines**: on
  any change the player makes, the tool snapshots the pond just before it and runs a copy 104 weeks ahead with no
  change; that copy's lines draw faint and dashed beside the real ones, so the player sees "what would have happened".
  The newest change replaces the ghost. Event marks (add, net, feeder, bottom, decomposers) sit on the time axis.
Panel (right, about 30 percent): the creature tray, the tools, the readouts, the hint and tip.

### Pond (opens first)
Focus: the pond. Controls, top to bottom:
- **Play / Pause** (big button) and **Speed** `.seg`: **Slow** (1 week a second), **Normal** (2 weeks a second, a year
  in 26 s), **Fast** (8 weeks a second, ten winters in 65 s). **Step 1 week** button (works while paused).
- **Lens** `.seg`: **Life**, **Matter**, **Energy** (below).
- **Creature tray** (a 2 x 4 grid of painted icon buttons, each with its name under it): **Algae**, **Snail**,
  **Minnow**, **Nymph** (dragonfly nymph), **Turtle**, **Heron**, **Decomposers** (a worm and fungus icon), **Net**.
  Tap a creature to add one (it drops in at a random spot with a splash), or drag it to a spot in the pond.
- **Net**: toggles the net tool (the button stays pressed). With the net on, a swipe through the pond scoops every
  cutout the net touches (up to 6 per swipe), and each tray button shows **Net 1** under its icon and a small **all**
  button beside it (**Net all minnows** read aloud and in its label). Tap Net again or press Escape to put it down.
- **Fish food** shaker button: each tap shakes a pinch (2 units) into the top of the water; flakes drift down and the
  minnows rush to them. **Feeder** `.seg`: **Off** (default), **Some** (3 units a week), **Lots** (12 units a week),
  feeding weeks 6 to 38 of each year (open-water weeks) and resting in ice weeks.
- **Bottom** `.seg`: **Sand** (Starter), **Gravel**, **Mud**: the bottom art and how well each minnow shade hides.
- **Decomposers working** switch (on by default). Off is a "what if": specks gray out and the muck stops breaking down.
- **New pond** (a card: **Starter pond**, **Empty pond**, Cancel) and **Save pond** (Journal opens and replays).
Readouts (`dl.readouts`): Week and season ("Year 3, week 22, summer"), Water temperature, Light, Oxygen, the six
kinds with counts, Shade of the minnows (a color swatch strip of the 8 shades with a marker at the school's average,
plus "average shade 3.5"), Heron (here, fishing / flew off / back in spring), Turtle (swimming / basking / asleep in
the mud / walked off).

**Lenses** (same pond, same running model):
- **Life** (default): the painted pond only.
- **Matter**: every 5 units of matter become one small dot drawn where that matter is (water and air dots float as
  pale blue in the water and above it, algae dots green in the algae, animal dots inside the cutouts' outlines, muck
  dots brown in the muck). Up to 150 dots; past 750 units of matter a dot is 10 units and the key says so ("1 dot =
  10 units"). Each week dots move between places in the same proportions as the model's flows that week. **Tap any dot
  to follow it**: it gets a yellow ring and a short trail, and a strip under the readouts writes its trip ("muck,
  water and air, floating algae, minnow, water and air..."). Total matter shows as one number with its ledger: "In the
  pond 742. Added 0. Taken out 0. Walked off 0." The total never changes except by those three.
- **Energy**: thin arrows of light pour in from the sun at the surface (width by this week's sunlight); green ribbons
  from algae to the eaters (width by this week's energy eaten); orange wavy heat lines rise out of every living kind and
  the decomposers into the air. A ledger card shows this year so far: Sunlight in, Caught by algae (percent of
  sunlight), Kept in algae, Kept in plant eaters (percent of algae kept), Left as heat, plus "Heat out vs caught"
  as a percent.

### Journal
Focus: the sticker book. A page of 25 sticker slots in rows easy to hard (see Goals). A found sticker shows its
painted icon, its name, the week it was found and one sentence of what happened. An unfound one shows its name and
target line only (goals are always visible; there is nothing to unlock). Under the stickers: **Saved ponds** (up to 8
on this device): each card shows the name, its age in winters, which kinds are alive, and buttons **Open**,
**Replay** (plays it from week 0 at Fast with its own actions), **Rename**, **Delete** (asks once). The Teacher note
sits at the bottom, collapsed. Pond keeps running in the background only if it was playing; Journal does not pause it.

## Goals
Optional. The pond never stops for a goal: a found one plays the sticker chime, shows a 3 s toast ("Sticker: Spring
bloom") and fills its slot. Checks run weekly on model units (snail 0.5, minnow 2, nymph 0.5, clump 5) and the pond's
own log. Easy to hard; each line is target, check, what it teaches.
1. **First splash.** Add any creature. Check: any add. Teaches: what you add brings its matter into the pond.
2. **A whole year.** Run one year. Check: 52 weeks since New pond. Teaches: light and warmth set a yearly rhythm.
3. **Spring bloom.** Check: Af > 150 (Starter peaks 184 to 273 every year). Teaches: algae grow when light returns.
4. **Ice over.** Check: an ice week. Teaches: cold slows all life; ice shuts out new air.
5. **Whose lunch?** Tap a minnow, a snail and a nymph in Life lens. Check: all three tapped. Teaches: who eats whom.
6. **Dot's journey.** Follow a dot from muck to water and air to algae to an animal. Check: the dot visits Det, then
   N, then Af or As, then S, M or Dn (other stops between are fine). Teaches: decomposers close the matter loop.
7. **Heat check.** Watch the Energy lens a whole year. Check: lens open weeks 0 to 51 of one year, and Left as heat
   within 5 percent of Caught by algae. Teaches: energy flows one way and leaves as heat.
8. **About a tenth.** Check: a year where plant eaters keep 5 to 20 percent of what algae kept, Energy lens open at
   year end. Teaches: only a small share of energy passes up each link.
9. **Hunters follow.** Check: in one year the nymph peak week is 4 to 12 weeks after the minnow peak week. Teaches:
   predators rise after their prey.
10. **Boom.** Add 30+ minnows in one week, then see them fall below the count before the add. Check: M under the
    pre-add value within 52 weeks. Teaches: a boom eats its food and feeds its hunters, then busts.
11. **Wobble.** Net all the minnows. Check: S under half the ghost's S within 52 weeks. Teaches: removing one kind
    hits kinds it never ate (minnows grazed the floating algae that shaded the snails' food).
12. **Green water.** Check: Af > 400. Teaches: without grazers, producers run wild and shade everything below.
13. **Snail boom.** Check: S > 30 units (60 snails) within 104 weeks of Net all nymphs, or in a pond with no nymphs.
    Teaches: predators hold prey in check.
14. **Hungry hunters.** Check: Dn reaches 0 while S > 0 and M > 0. Teaches: stock the prey before the hunters.
15. **Heron gives up.** Check: the heron flies off in weeks 0 to 30. Teaches: predators leave when prey is scarce or
    hard to see.
16. **Choke the pond.** Check: Det / total >= 0.90. Teaches: without decomposers matter piles up dead.
17. **Comeback.** Check: after Choke, Af + As > 100 with decomposers on. Teaches: decomposers restart the loop.
18. **Winterkill.** Check: O < 2 in an ice week and M at week 51 under half of M at week 40. Teaches: extra food rots,
    and rotting uses up the fish's oxygen.
19. **Camouflage.** Check: average shade 1.0 or more from its value at New pond within 260 weeks. Teaches: the heron
    takes the minnows it sees, so hidden shades leave more young.
20. **Turn the school back.** Check: after Camouflage and a Bottom change, shade moves 1.0 toward the new bottom
    within 208 weeks. Teaches: selection follows the habitat.
21. **Standoff.** Check: Starter on Gravel since New pond, heron present, 260 weeks with shade always 3.25 to 3.75.
    Teaches: if no shade hides better, nothing is selected.
22. **Rescue.** Check: after Comeback, algae, snails, minnows, nymphs, turtle and decomposers all alive 156 weeks
    later. Teaches: rebuild a web from the bottom up.
23. **Ten winters from nothing.** Check: Empty pond, 520 weeks, all six kinds alive. Teaches: a lasting web needs
    producers, enough prey for hunters, and decomposers.
24. **Careful keeper.** Check: Feeder Some all 520 weeks and M > 0 at the end. Teaches: how much food matters.
25. **Full house.** Check: S >= 20, M >= 80 and Dn >= 5 (40 snails, 40 minnows, 10 nymphs) in one week. Teaches: a
    balanced web carries many kinds at once.

### Depth from combining
Parts that combine: **the creatures** (what you add or net), **the seasons** (light, temperature, ice), **the
decomposers and muck**, **the fish food**, **the bottom** and **the heron's eyes** (water clarity). Surprising
combinations a student can find (each run on the model; numbers in Sources):
1. Netting the minnows starves the snails and sends the turtle away: green water shades the algae on stems.
2. A little fish food every summer, harmless for years, ends in a winterkill: muck builds up and rots under the ice.
3. Green water hides the minnows from the heron and slows their camouflage.
4. A gravel bottom stops the color drift dead.
5. Taking out the dragonfly nymphs makes snails boom to several times their usual peak.
6. Adding minnows grows the dragonflies and the algae on stems (the minnows graze down the shade).
7. Decomposers off makes the turtle walk off long before any kind dies out.
8. Stocking hunters with too little prey starves them, even with the turtle there to "help".

## Content

### Kinds (units of matter per cutout)
| Kind | Cutout = | Eats | Eaten by | Notes |
|---|---|---|---|---|
| Algae (floating mat, and on stems and stones) | 5 units (a clump) | water and air, with sunlight | minnows (floating), snails and turtle (on stems) | an add splits 2.5 floating, 2.5 on stems |
| Snail | 0.5 | algae on stems and stones | nymphs, turtle | |
| Minnow | 2 | floating algae, fish food | nymphs, turtle, heron | 8 shades, 0 pale silver to 7 dark olive |
| Dragonfly nymph | 0.5 | snails, minnows | turtle | |
| Turtle (painted turtle) | 30 (fixed adult) | snails, nymphs, minnows, algae on stems | none | awake at 10 C or warmer |
| Heron (great blue heron) | visitor, not counted | minnows it can see | none | away in ice weeks |
| Decomposers (bacteria, fungi, worms) | 1 speck = 0.25 | muck | none | |
| Muck (dead stuff and droppings) | layer | | decomposers | |
| Water and air (carbon dioxide, water, minerals) | dots only | | algae | |

Food arrows on a tap point from food to eater, plus one to muck (e.g. minnow: floating algae and fish food in; out to
nymph, turtle, heron and, when it dies, muck).

### The model (weekly step, 7 daily substeps; build exactly this)
Week 0 is ice-out in mid March. Temperature T = 13 - 11 cos(2 pi (w - 46) / 52) C (2 to 24 C, warmest week 20); every
rate is scaled by tf = 2^((T - 20) / 10). Ice when T < 4 C (weeks 41 to 51). Sunlight at the surface
sun = 0.6 + 0.4 cos(2 pi (w - 14) / 52); under ice the light in the water is 0.3 x sun. Oxygen saturation
osat = 14.6 - 0.39 T + 0.007 T^2.
- **Algae**: growth = 1.4 x light x tf x A x N / (N + 40) x (1 - A / Amax), Amax 900 floating, 500 on stems; algae on
  stems see light / (1 + Af / 250). Each loses 0.08 x tf x A to water and air and 0.05 x A to muck a week (x 1.6 when
  light < 0.35). Growth is taken from N (scaled down if N is short).
- **Eaters** (type II): intake = cmax x tf x B x P / (H + P) where P is the prey's weighted amount above its refuge
  (algae 15, snails 4, minnows 6, nymphs 1). Of intake, eff becomes body, (0.7 - eff) is breathed to water and air,
  the rest is droppings to muck. Each also breathes maint x tf x B and dies mort x B to muck a week.
  Snail cmax 1.0, H 100, eff 0.30, maint 0.07, mort 0.02. Minnow 1.0, 100, 0.30, 0.07, 0.015; food weights floating
  algae 1, fish food 3. Nymph 0.7, 35, 0.30, 0.07, 0.02; weights snails 1, minnows 0.5. Decomposers 1.5, 100, eff
  0.20, maint 0.08, mort 0.10, eat muck; all intake not built into body is breathed out; below 2 units they rest (no
  breathing or deaths) unless switched off.
- **Turtle**: needs 1.2 x tf units a week each, eats only when T >= 10 C, intake = need x P / (40 + P) with weights
  snails 1, nymphs 0.5, minnows 0.5, algae on stems 0.3. 70 percent breathed out, 30 percent to muck.
- **Heron**: needs 1.6 units a week each, fishes only with no ice and while here. It sees minnow shade k with
  visibility 0.15 + 0.85 x |k - bottom| / 7 x clarity, clarity = 1 / (1 + (Af / 400)^2), bottom shade Sand 1, Gravel
  3.5, Mud 6. Catch = need x V / (10 + V), V = sum of visibility x minnows (above refuge), taken from each shade in
  proportion to its visibility x count. 70 percent breathed out, 30 percent to muck.
- **Minnow young** carry the parents' shade: of each shade's share of new growth, 88 percent stays, 6 percent goes one
  shade paler and 6 percent one darker (clamped at 0 and 7).
- **Fish food**: sinks to muck at 0.4 of what is left a week. Minnows eat it first (weight 3).
- **Oxygen** (mg per liter, 0 to 20): + 0.05 per unit algae build, - 0.05 per unit anything breathes, + 0.6 x (osat -
  O) a week from the air only when there is no ice. Low oxygen deaths a week, to muck: minnows 1.2 x (3 - O) / 3 below
  3; nymphs 0.6 x (1.5 - O) / 1.5 below 1.5; snails 0.15 x (1 - O) below 1.
- **Exact matter**: when a pool's outflows in a substep exceed it, all of them scale down together; the total equals
  start + added - taken out - walked off at every step.
- **Gone rules** (checked each week): snails or nymphs under 0.25 units, minnows under 1 unit, algae or decomposers
  under 0.5 go to muck and the kind is gone. The heron flies off after 3 fishing weeks in a row catching under 30
  percent of its need and comes back at week 0 next spring. The turtle walks off (its 30 units leave the pond,
  "Walked off") after 8 awake weeks in a row eating under 25 percent of its need.
- **Energy**: 10 energy units per unit of matter algae build (caught) and per unit breathed (heat). Sunlight in is
  70,000 x sun a week.
- The model has no randomness. Cutout positions and movement use `Rand(seed)` (kit/probability.js) per pond.

### Starting ponds
- **Starter pond**: water and air 300, floating algae 80, algae on stems 70, snails 40 (80), minnows 40 (20, shades 2,
  3, 4, 5 with 10 units each, average 3.5), nymphs 12 (24), decomposers 20, muck 150, 1 turtle, 1 heron, Sand, oxygen
  10. Total matter 742.
- **Empty pond**: water and air 300, muck 150, decomposers 20, oxygen 10, Sand, nothing else. Hint: "An empty pond.
  Add algae first, then the animals that eat them."
- Tray adds: algae 5 units (2.5 floating, 2.5 on stems), snail 0.5, minnow 2 (shades 2 to 5, a quarter each), nymph
  0.5, turtle 30, decomposers 5 (a scoop of mud with worms, 20 specks), heron (no units). All go to the ledger.

### Limits (the creature budget)
Drawn caps: algae clumps 40, snails 60, minnows 60, nymphs 30, turtles 3, herons 2, decomposer specks 120, matter dots
150. Past a cap the kind is drawn at the cap and a key shows "1 snail = N snails" (N rounded up so the count fits).
Adds stop at twice the cap in units (120 snails, 120 minnows, 60 nymphs, 80 clumps), 3 turtles, 2 herons, with
"The pond is full of snails." Fish food: at most 30 units in one week ("The water is cloudy with food already.").
Worst case run (all at the add limits plus 60 food every week for ten years) stays finite and never negative.

### Saving
Save pond stores on this device (localStorage, in try/catch; up to 8 ponds): name, the starting choice, the action
log (week, action, amount, for every add, net, feeder, bottom, decomposers and fish food), stickers found in it, and
the current week. Open replays the log silently to the saved week (the model is exact, so it is the same pond).
Replay plays it from week 0 at Fast with each action shown as a mark. Stickers found are also kept on this device
across ponds. If storage is blocked, Save says "This browser can't save here" and play goes on.

## Interactions in detail
- **Every control is live while Play runs.** An add or net changes the pond and readouts at once (the model is
  updated immediately, the cutout splashes in or is scooped out the same frame) and the ghost restarts; the feeder,
  bottom and decomposers switch take effect at once in the readouts and from the next substep in the model; the
  event mark lands on the graph at the current week the moment it is pressed.
- **Animation is driven by the model.** Each displayed week, counts become cutouts: new cutouts fade in near their kind
  (young minnows at half size growing to full over 2 s), lost cutouts fade, turn gray and sink into the muck. Heron
  strikes play in proportion to its catch that week (at most one every 1.5 s); nymph lunges in proportion to what
  they ate (at most 2 a second). Minnows school around a wandering leader and rush to flakes; snails crawl along stems
  and stones; nymphs creep on the mud; the turtle swims, basks on the log on warm bright weeks (T >= 18 and sun > 0.8),
  and sleeps tucked in the mud below 10 C. The water's green tint follows Af (alpha = Af / (Af + 300), max 0.6). Oxygen
  bubbles rise from the algae by how much they built. Below oxygen 3 the minnows swim at the top (or under the ice)
  with slow, gasping motion.
- **Seasons**: the backdrop crossfades spring (weeks 0 to 12), summer (13 to 25), fall (26 to 38), winter (39 to 51)
  over 1 s; the light wash over the water follows the light value. Ice grows in from the edges on week 41 and cracks
  apart on week 0.
- **Tapping a cutout** (Life lens, net off): its name, state ("Fishing", "Asleep in the mud") and food arrows for 3 s.
- **Dot moves**: each week a followed dot takes each flow out of its place with chance (that flow / the amount there at
  the week's start); eaten, it becomes body with chance eff, water and air with 0.7 - eff (decomposers 0.8), else muck.
- **Net all** removes every unit of that kind (heron: it leaves for good until added again). Netting the heron or
  turtle removes its cutout; netting decomposers is not allowed ("Decomposers are too small to net. Use the switch.").
- **New pond** keeps nothing from the old pond (stickers stay); asks "Start over? Save this pond first?" with **Save**,
  **Start over**, **Cancel** when the pond has unsaved actions.
- **Extremes**: with every animal gone the seasons still turn; hint "Only algae left. Add snails or minnows." (or
  "Nothing lives here now. Add algae."). A gone kind plays a low two-note fall and puts a gray mark on the graph.
- **Ghost**: computed on change (104 weeks, under 5 ms); the ghost never changes the real pond.
- **Keyboard**: Space plays or pauses, period steps a week, 1 to 7 add the tray kinds, N toggles the net, L cycles
  lenses; every control is a focusable button; arrow keys move the drop point for tray adds.
- **Sizes**: 1366x768 and 1920x1080: stage left, panel right. 1000x625 and 800x500: same split, tray icons 44 px, graph
  34 percent. 680x425 (the preview): panel 260 px wide with the tray as 4 x 2 small icons; Play, Speed and the tray are
  visible without scrolling; readouts collapse to Week, Oxygen and counts. 760 wide and 375 wide: stage on top (pond
  at least 220 px tall at 375, graph 130 px), a Play, Speed and Lens strip pinned over the pond's top edge, panel below;
  no sideways scroll.
- **Performance**: at most about 195 cutouts, 120 specks and 150 dots on a 2D canvas at 60 frames a second on a school
  Chromebook; cutouts are pre-scaled bitmaps cached per size; the model runs one substep batch per displayed week
  (under 1 ms). With Motion off: no swimming, crossfades or trails; cutouts sit in seeded spots and counts update.

### Sounds (Web Audio, quiet, with the kit's Sound)
Splash on add (filtered noise burst, 0.15 s), net swish, flake sprinkle (three high ticks), heron strike (a low plunk),
heron flying off (two falling soft notes), turtle onto log (wood knock), ice forming (crackle ticks), ice breaking
(a brighter crack), season change (a soft wood-block tick), bloom (a soft rising three-note chime the first time Af
passes 150 each year), a kind gone (low two-note fall), winterkill (a low hum fading), sticker (`Curio.yes()`). At most
one event sound each 150 ms; Fast plays only gone, sticker and ice.

## Look
Accent: dragonfly teal `--brand #0e6a73`, `--brand-ink #ffffff`, paper `#f4faf8`, ink `#16302e`, muted `#4c605e`,
pressed tray button `#0b4f56` with white. Water: clear `#9fd0d6` at the top to `#2b6f7a` at the bottom, green tint
`#6f9a3a`; muck `#5a4632`; ice `#e8f4f8` at 85 percent. Graph lines on white: algae `#5b6b2a`, snails `#8a5a00`,
minnows `#1f7a8c`, nymphs `#6b4fa0`, oxygen gauge `#b0306a` (each line also has a distinct dash pattern and an end
label, so color is never the only cue).
Contrast (computed): white on brand 6.31:1; brand on paper 5.97:1; ink on paper 13.28:1; muted on paper 6.33:1; white
on pressed `#0b4f56` 9.26:1; kit pressed seg `#3a2c00` on `#ffd34d` 9.53:1; graph lines on white 4.98 to 6.46:1 (the
pale `#2f8f3a` at 4.11 was rejected). Different from neighbors: lake-commons `#7cac64`, how-animals-see `#2f6b3a`,
carrying-capacity `#e2a19c`.

## Art
Local FLUX (`scripts/localart.py`), no people, 36 images, total under about 1.3 MB as WebP (backdrops 1280 wide,
strips 1600 x 200, cutouts 256 to 384 px). House style: painted naturalistic picture-book look, soft natural light,
clear shapes, gentle colors, blank surfaces wherever lettering could appear. Every cutout is a single subject in side
view on a plain flat pale background (cutout yes, people no).
- Shore backdrops (16:5, cutout no; above the waterline, crossfade by season): lp-shore-spring (a small pond's far
  shore in spring, pale new grass, budding willows, soft blue sky), lp-shore-summer (the same shore in high summer, deep
  green grass, full willows, bright sky), lp-shore-fall (gold and red leaves, tan grass), lp-shore-winter (snow on the
  bank, bare willows, pale sky).
- Strips (8:1, cutout no, tiled): lp-bottom-sand (pale sandy pond bottom with fine ripples), lp-bottom-gravel (mixed
  gray and brown gravel), lp-bottom-mud (dark olive brown mud), lp-muck (soft brown muck with bits of dead leaves and
  twigs; height by muck units), lp-ice (clear pale blue pond ice, frosted top, a few trapped bubbles).
- Plants (cutouts; sway with Motion on): lp-cattails (cattails with brown seed heads and long green leaves, 1:2),
  lp-cattails-winter (dry tan cattails with ragged seed heads, fall and winter, 1:2), lp-lilypads (round green lily
  pads with one white water lily, 3:1), lp-pondweed (a tall stem of green pondweed with narrow leaves, where snails
  crawl, 1:3), lp-algae-stone (a rounded stone covered in soft green algae, 4:3), lp-algae-stone-thin (a rounded stone
  with a thin patchy green film, used when algae on stems is low, 4:3), lp-algae-mat (a loose floating mat of bright
  green filamentous algae, scaled by floating algae, 3:1).
- Grazers and hunters: lp-snail-crawl (a pond snail with a spiral brown shell crawling, body out, 4:3), lp-snail-tucked
  (the same snail pulled into its shell, 1:1), lp-minnow-pale (a small slender minnow with a pale silver body, 3:1,
  shade 0), lp-minnow-dark (the same minnow with a dark olive body and darker back, 3:1, shade 7; shades 1 to 6 draw
  the dark one at alpha k / 7 over the pale one), lp-nymph (a brown green dragonfly nymph with six legs and a wide head,
  4:3), lp-nymph-lunge (the same nymph with its hinged jaw shot forward, 4:3), lp-dragonfly (an adult blue green
  dragonfly body without wings, 3:1; flies over the water weeks 13 to 30, one per 4 nymphs, at most 6),
  lp-dragonfly-wing (one clear veined dragonfly wing, 4:1; two per dragonfly, flicker).
- Turtle and heron: lp-turtle-swim (a painted turtle swimming with legs out, 4:3), lp-turtle-bask (a painted turtle
  resting with its neck stretched, 4:3), lp-turtle-tucked (a painted turtle with head and legs pulled in, 4:3),
  lp-log (a weathered fallen log lying partly in water, 4:1, basking spot), lp-heron-stand (a great blue heron standing
  in shallow water, 1:2), lp-heron-strike (a great blue heron with its neck shot forward and beak in the water, 1:1),
  lp-heron-fly (a great blue heron in flight with wings spread, 2:1).
- Decomposers and props: lp-worm (one pink brown earthworm, curved, 2:1), lp-fungus-leaf (a brown dead leaf with
  white fungus threads, 4:3), lp-leaves (three dead leaves, oak, maple and willow, brown and gold, 3:1; fall and sink
  in fall), lp-shaker (a small round fish food shaker with a blank paper label, 1:1; the Fish food button and the
  shake), lp-net (a small dip net with a wooden handle and green mesh, 1:2; the Net button and cursor).
Tray icons and sticker icons reuse the cutouts (stickers on a colored disc). The graph, gauge, arrows, dots, ribbons
and all text stay in code.

## Voice
Bank `gravel-ranger` (an old park ranger who has watched this pond for years: slow, dry, warm, short sentences). No
close neighbor uses it. Uses `Curio.voice`, scope = mode. How lines speak once, then only set the hint; event lines
speak each time but each event line waits at least 20 s before it repeats (maxAge 4 s so stale lines drop at Fast).
Never two lines in a row about the same thing; nothing nags.
- welcomePond (how; on load; stale once anything is added or netted): "Morning. This pond runs itself. Tap a creature
  to add one, or tap Net to take some out."
- welcomeEmpty (how; Empty pond; stale when algae are added): "Empty pond. Tap Algae first. Everything else eats what
  algae build."
- netOn (how; first Net; stale when the net is put down): "Swipe through the water to scoop, or tap all for every one."
- matterLens (how; first Matter lens; stale on leaving it): "Every dot is a bit of matter. Tap one to follow it."
- energyLens (how; first Energy lens; stale on leaving it): "Sunlight comes in, heat goes out. Watch a whole year."
- decompOff (how; decomposers off; stale when on): "Decomposers stopped. Watch the muck pile up."
- feederLots (how; first Feeder Lots; stale when Feeder is Off): "Lots of food. Uneaten food sinks and rots."
- bottomChange (how; first Bottom change; stale after 52 weeks): "New bottom. Watch the shade strip. It takes winters."
- journal (how; first Journal; stale on returning to Pond): "Here's what you've found. Each sticker is something the
  pond did."
- firstIce (event; first ice week of a year; stale at ice-out): "Ice. No new air gets in until spring."
- lowOxygen (event; oxygen under 3; stale once back over 4): "Oxygen's low. The minnows are gasping at the top."
- winterkill (event; Winterkill fires; stale at ice-out): "Winterkill. Rotting muck under the ice used up the air."
- heronLeft (event; heron flies off; stale when it returns): "The heron gave up. Not enough fish it could see."
- turtleLeft (event; turtle walks off; stale when a turtle is added): "The turtle walked off to find a better pond."
- gone (event; a kind is gone; stale on adding that kind): "The snails are gone. Tap Snail to bring some back." (kind
  name and button match)
Hint (not spoken) while waiting with nothing pressed: "Tap a creature to add it, or press Play." (Play is named only
while paused.)

## Family engine
**ecosystem** (`kit/ecosystem.js`, described in carrying-capacity's spec; not built yet). Living Pond feeds or extends:
- `Species`: the eight kinds above with role, icon (the cutouts) and params.
- `Web`: the links in Content, with `web.effects(id)` used by the tap-a-creature arrows.
- `PopChart`: extended with weekly x, season and ice bands, ghost lines and a side gauge (useful to food-web-wobble's
  idea and predator-prey-island).
- `Landscape`: extended with a `pond` layout (cut-away depth zones: surface, open water, stems, bottom; per-kind zones
  and the "1 = N" key past a cap).
It owns its own weekly matter-conserving pond model in the tool, because the engine's `Model` is a yearly
single-resource step. If a second tool needs a multi-kind weekly model, move it into the engine then.

## Sources
- Food webs, producers, consumers, decomposers, matter cycling: OpenStax Biology 2e, 46.1 "Ecology of Ecosystems" and
  46.3 "Biogeochemical Cycles" (CC BY 4.0), https://openstax.org/books/biology-2e/pages/46-1-ecology-of-ecosystems
- Energy flows one way, about 10 percent passes each level, the rest leaves as heat: OpenStax Biology 2e 46.2
  "Energy Flow through Ecosystems", https://openstax.org/books/biology-2e/pages/46-2-energy-flow-through-ecosystems
- Producers catch only about 1 percent of sunlight: Lindeman, R. L. (1942), "The trophic-dynamic aspect of ecology",
  Ecology 23(4):399-417 (pond and lake energy budgets) and OpenStax 46.2 (verify checks the wording).
- Type II feeding: Holling, C. S. (1959), "Some characteristics of simple types of predation and parasitism", The
  Canadian Entomologist 91:385-398. Predator-prey with seasons: Lotka-Volterra form, OpenStax Biology 2e 45.6.
- Rates double about every 10 C: Gillooly, J. F. et al. (2001), "Effects of size and temperature on metabolic rate",
  Science 293:2248-2251 (Q10 2 is a round model value).
- Cold water holds more oxygen (about 14.6 mg/L at 0 C, about 9 at 20 C): USGS Water Science School, "Dissolved
  Oxygen and Water", https://www.usgs.gov/special-topics/water-science-school/science/dissolved-oxygen-and-water (the
  model's fit runs about 0.5 mg/L high at 20 to 25 C).
- Winterkill under ice from decay using oxygen: Minnesota DNR, "Winterkill",
  https://www.dnr.state.mn.us/fish/winterkill.html (verify confirms the page). Nutrients and algal blooms, green
  water: US EPA, "Nutrient Pollution: The Effects", https://www.epa.gov/nutrientpollution/effects-environment
- Great blue herons hunt fish by sight in shallow water: Cornell Lab, All About Birds, "Great Blue Heron Life History",
  https://www.allaboutbirds.org/guide/Great_Blue_Heron/lifehistory
- Painted turtles eat snails, insects, small fish and plants, and spend winter in the mud: Ernst, C. H. and Lovich,
  J. E. (2009), Turtles of the United States and Canada, 2nd ed., Johns Hopkins (verify checks the 10 C activity line).
- Dragonfly nymphs hunt snails, insect larvae, tadpoles and small fish with a hinged jaw: Encyclopaedia Britannica,
  "Dragonfly" (verify).
- Predators select for color that matches the background, over generations: Endler, J. A. (1980), "Natural selection
  on color patterns in Poecilia reticulata", Evolution 34(1):76-91.
- **Honest model.** Simplified on purpose: one small made-up pond, matter in units not grams, weeks as the step, no
  nitrogen or phosphorus split (one water and air pool), one oxygen number for the whole pond, turtles and herons as
  fixed adults (no breeding; the heron's body is outside the pond), color as a single inherited trait with no cost,
  and minnow generations about a year long, so drift that takes real fish many generations shows in a few winters.
  All rates are model values chosen so the Starter pond keeps every kind for ten winters; they are not measured for
  any one pond.
- **Number checks** (Python, 2026-10-29, the model exactly as in Content, weekly step of 7 substeps):
  - Starter, ten winters: all kinds alive; matter 742.0000 start and end (drift about 1e-12). Year 10 ranges: floating
    algae 8 to 214, algae on stems 27 to 211, snails 19 to 34, minnows 12 to 57, nymphs 10 to 17, oxygen 6.4 to 16.9.
    Lowest snails 3.0 units (year 2). Most cutouts ever: 77 snails, 64 minnows, 32 nymphs, 44 clumps (caps hold).
    Peaks year 10: algae weeks 9 to 22, snails 32, minnows 31, nymphs 38 to 39; nymph peak 4 to 12 weeks after the
    minnow peak in 8 of 10 years. Floating algae yearly peaks 184 to 273. Ice weeks 41 to 51. The heron flew off once
    (year 6 week 9).
  - Energy: algae catch 1.19 to 1.26 percent of sunlight a year; plant eaters keep 9.5 to 12.8 percent of what algae
    keep (year 10: 10.3); heat out within 4 percent of caught in year 1, about 1.7 percent after.
  - Matter tracer: 1,986 of 2,000 followed dots complete muck, water and air, algae, animal within the run; median 64
    weeks, 90 percent within 190. Time share: muck 29, water and air 29, floating algae 17, algae on stems 9, minnows
    11, decomposers 4, snails 1, nymphs 1 percent.
  - Combination 1 (net all minnows, year 1 week 13): floating algae up to 477 to 509 (ghost 256), algae on stems down
    to 3.3 (ghost 64 to 163), snails under half the ghost after 17 weeks, gone year 2 week 17; heron flew off week 15,
    turtle walked off week 25. Netting at other times: under half the ghost after 27, 17, 32, 38, 24 and 15 weeks.
    Netting half: Af max 358, snails down to 1.2 units, no kind lost.
  - Combination 2 (feeder): Some (3 a week) first oxygen under 2 in year 6 week 49, minnows survive ten winters (winter
    losses 98 to 99 percent in years 9 and 10); 4 a week minnows gone year 8 week 51; Lots (12) gone year 2 week 51
    with a 100 percent winter loss; 15 gone year 2 week 51. No feeder: winter minnow loss 38 to 47 percent.
  - Combination 3 (sand, heron, summer feeding): clarity 0.90, 0.75, 0.66, 0.52 at 0, 2, 4, 6 a week; average shade at
    year 10: 1.20, 1.53, 1.97, minnows gone at 6.
  - Combination 4 and drift: sand 3.21, 2.35, 1.70, 1.20 (years 1, 3, 5, 10); mud 3.79, 4.65, 5.30, 5.80; gravel and
    no heron 3.50 exactly all ten years; 2 herons on sand 2.88, 1.62, 1.32, 1.25. One full shade at year 3 week 23 on
    sand and mud. Sand 5 years then mud: 1.70, 2.12, 2.60, 3.25, 4.12 (years 5 to 10), one shade back in 2.08 years.
    Heron removed after 10 years: 0.42 back toward the middle in 5 years. Gravel spread does not shrink (sd 1.12 to
    1.36), so no spread goal.
  - Combination 5 (no nymphs): snails' yearly peaks 65 to 119 against 18 to 77 with nymphs; netting all nymphs gives
    over 60 snails in 23, 49 or 54 weeks (netted year 1 week 13, year 1 week 26, year 2 week 13).
  - Combination 6 (add 30 minnows, year 1 week 13): 41.2 to 107.6 units, peak 124.1 at week 17, low 10.6 at year 2
    week 5; nymphs 12.4 to 23.1; algae on stems up to 333.
  - Combination 7 (decomposers off at week 0): muck 95 percent of matter at year 1 end, 99 at year 2; turtle walked
    off year 1 week 33; snails gone year 2 week 19, minnows week 20, nymphs week 24, algae year 2 week 51 and year 3
    week 5. Back on at year 2 week 26 (+5 units): algae over 100 after 35 weeks. Rescue restock at year 3 week 30 (20
    snails, 10 minnows, 6 nymphs, 1 turtle): all six alive at year 8; restocking 10 snails and 6 minnows only lost the
    turtle again.
  - Combination 8 and building: from Empty, 99 of 108 stockings keep all kinds ten winters (all 9 failures are nymphs
    short of algae and prey); 10 clumps, 20 snails, 10 minnows, 6 nymphs, 1 turtle, 1 heron passes, also stocked at
    week 45; 4, 6, 3, 2: nymphs gone by week 18 to 19. No algae: all die in year 1. Turtle removed: little change. 3
    herons: first flies off year 2 week 10. 100 snails added: crash to 5 in 13 weeks. Full house in Starter at year 3
    week 33 (48 snails, 48 minnows, 13 nymphs).
  - Worst cases: all kinds at the add limits plus 60 food every week for ten years: total 32,290, no negative or
    non-number values, minnows and nymphs eventually gone, nymphs up to 196 (cap and key needed). Starter plus 20 snails
    every 4 weeks: minnows gone year 8 week 51.

## Done when
1. Starter pond on Play keeps all six kinds for ten winters at Fast (65 s), the matter total stays 742 in the Matter
   lens, and year 10 snails stay between about 19 and 34.
2. Net all minnows at year 1 week 13: green water deepens past 400, the snail line drops under half its dashed ghost
   within 52 weeks, the heron flies off and the turtle walks off, each with its line and sound.
3. Decomposers off from week 0: muck passes 90 percent of matter within year 1, the turtle leaves before any kind is
   gone; switching back on brings algae over 100.
4. Feeder Lots for two summers ends in a winterkill sticker in year 2; Some keeps minnows alive for ten winters.
5. Sand with the heron moves the shade marker a full shade by year 3; Gravel holds it at 3.5.
6. Following a dot in Matter lens writes its trip and reaches an animal; the Energy ledger shows heat out within 5
   percent of caught for a full year and plant eaters near a tenth.
7. Focus: the pond is the largest thing on the stage at 1366x768, 1920x1080, 1000x625, 800x500 and the 680x425 preview,
   and at 760 and 375 wide; main controls (Play, Speed, tray) visible without scrolling at 1366x768 and 680x425.
8. A tap while Play runs: adding a minnow at Fast drops it in the same frame, moves the count readout at once and
   marks the graph; switching Feeder or Bottom shows in the readouts at once.
9. At the add limits the "1 = N" keys show, "The pond is full" lines appear, and the pond holds 60 frames a second on a
   school Chromebook; Motion off stops all swimming.
10. Save pond, reload the page, Open: the same pond at the same week; Replay reproduces every action mark.
11. Every how line speaks once in five repeats; event lines speak each event but not more than once in 20 s; keyboard
    reaches every control; no network, no em dashes; the bundled file is under 2 MB.
12. A fresh player with no instructions is still choosing to play after 10 minutes, and can name one thing they
    figured out.

## Open questions
- [living-pond] Food Web Wobble's card is fully taken over here (its arrows show on tapping a creature). OK to retire
  that idea card, or keep a tiny grade-3 version?
- [living-pond] Color drift is fast on purpose (a full shade in about 2.4 winters). Say "sped up" on the shade strip,
  or leave it to the Teacher note?
- [living-pond] Fish food teaches that feeding fish can kill them (winterkill). Fine for grades 3 to 8, or soften the
  winterkill line?
- [living-pond] 36 images at about 1.3 MB keeps the file under 2 MB. If the art runs over, drop to two shore
  backdrops (summer, winter) first, or fewer creature poses?

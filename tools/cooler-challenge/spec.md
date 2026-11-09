# Cooler Challenge

## One idea
Build a lunchbox wall layer by layer, pick the cold packs, and leave it in a car on a sunny morning: three live heat
arrows (through the walls, air at the lid, sunlight) always point from hot to cold, the graph shows the ice line sitting
flat at 0 °C while it melts, and the student learns by testing that walls only slow heat; the ice is what buys time.

## Not like
- hot-meets-cold (gr 11 physics, spec): two objects mixed in a cup, final temperature from heat capacity, particles at
  a wall. Here nothing is mixed and nothing is calculated: a device is designed against a job card, and the bench
  compares temperature change for equal heat, by graph only (MS-PS3-4's boundary: no energy totals).
- hand-warmer-lab (gr 10 chemistry, spec): heat from bond energies. Here no reactions; heat moves in from outside.
- reaction-kitchen (gr 7, concept): its bench 3 designs a rusting-iron hand warmer (a chemical heat source). Here no
  chemistry: insulation, three heat paths and cold packs, a lunchbox not a pouch.
- particle-party (gr 7, concept): heating curves with particle views and plateaus as the main idea. Here the plateau is
  one moment in a design test; no particle animation (a caption names temperature as average particle motion).
- half-pipe-energy (gr 8, concept): owns MS-PS3-5 (moved from this tool, docs/agents/audit/gaps.md row 9: friction and
  brake heat). Nothing here about kinetic energy turning into heat.
- span-and-spire (gr 8 builder, draft): budget plus test for structures. Here the test is a clock and a temperature
  graph, not loads, and parts go in a wall stack, not a truss.
- design-challenge-studio (gr 12, draft): open design process for any problem. Here one device, one job card, a model.

## Who and how
- Grade 6, science, module Thermal Energy (science-6-thermal-energy). Standards: MS-PS3-3, MS-PS3-4 (MS-PS3-5 left this
  module for half-pipe-energy; nothing here claims it). Driver: students (solo by default); a teacher can project Build
  for a class prediction. 30 to 45 minutes (Build 20 to 30, Bench 10 to 15).
- tool.json: driver "students or teacher", minutes "30-45", modes ["Build", "Bench"], grades_label "Grade 6".
- No personal prompts. The engineer's note is stored on this device only and says so on screen (BASELINE rule 7).
- Teacher notes: the hot car is only a test chamber; a line says a parked car heats fast even on a mild day, so never
  leave a person or pet inside (Sources). No person or animal is ever drawn in or near the car.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-PS3-3 (design, construct, test a device that minimizes thermal energy transfer) | Build: add wall layers, a cover, the lid seal and packs within the job card's limits; Run; change one thing; Run again until lunch stays cold to noon on $8; answer the engineer's check; write which change mattered most | the cutaway box changing, three heat arrows shrinking as each path is slowed, the lunch line staying in the cold zone, the test log of every run | Done 1, 2, 3, 4 |
| MS-PS3-4 (plan an investigation: energy transferred, type of matter, mass, temperature change) | Bench: pick a question, set samples A and B so only that variable differs, predict, run with equal heat, pick the sentence the graph supports; all three questions | two cups on identical plates, equal "heat added" bars, two temperature lines and each sample's change in °C, the caption "Temperature tells how fast the particles move, on average" | Done 5, 6 |

## Screens and modes
Kit frame, light theme with the tool's own `:root` (Look). Header: "Cooler Challenge", small line "Keep lunch cold till
noon." Mode buttons `Build` (lunchbox icon) and `Bench` (beaker icon); kit Motion, Sound, Read.
On load: Build, an empty plastic shell (no layers, no cover, no seal, no packs) with the lunch inside, clock 8:00,
graph empty, arrows showing the 9:00 preview. Nothing plays before the first tap. Hint: "Lunch rides in a hot car from
8:00 to noon. Tap a material to add a wall layer, or tap Run to test the bare box." First tap on a material tile adds a
layer (main path); first tap on Run starts the test (main path); any other first tap does its own job at once.

### Build (opens first)
Focus: the cutaway box (designing) and the graph (running). At 1366x768, stage left (64 percent): the painted car
interior (cc-car) fills the stage top (about 440 px tall); the box cutaway sits on the sunlit seat, left half, drawn in
code at about 400 x 300 px; the graph takes the right half, same height. Under both, the test log (4 rows visible,
`Older` and `Newer` page buttons when there are more). Panel right (36 percent), top to bottom: hint; job card (3
lines); `Walls` row of four material tiles (Foam, Cotton batting, Cardboard, Sealed air gap), each 64 px with its
painted swatch, name, price and a "slows heat" bar; `Cover` row (None, Foil, Black cloth); `Lid seal` toggle; `Packs`
row (Frozen bottle, Steel cubes, Fridge bottle); meters "Cost $0.00 of $8", "Wall 0 of 30 mm", "Packs 0 of 4"; `Run`
(big, brand) and `Skip to noon`. All above the fold at 1366x768, 1280x720 and 1000x625. At 680x425 and 800x500 stage
and panel stay side by side: the car backdrop crops to the seat, tiles become 44 px swatches with a 10 px name under
them, the "slows heat" bars hide, and the log folds into a `Log` button that opens over the graph.
- Job card: "Lunch: turkey sandwich and an apple, from the fridge at 3 °C. Keep it at 4 °C (40 °F) or colder from 8:00
  to noon. Budget $8. Walls at most 30 mm. USDA tip: pack at least two cold sources."
- Cutaway: the shell outline, then one band per layer outward (10 mm each, textured with the layer's swatch, labeled in
  code), the cover as the outer skin (foil glints, black cloth matte), a rubber strip at the lid seam when sealed, the
  lunch cutout in the middle, packs above and below it in slots. A tap on a layer band or a pack removes it.
- Heat arrows, from outside to the box, drawn in code: Conduction (orange, through the side wall, label "through the
  walls"), Convection (curling, at the lid seam, "air at the lid"), Radiation (wavy yellow from the windshield,
  "sunlight"). Width shows how fast heat flows right now (Interactions). Legend: "Arrow width: how fast heat flows in."
- Graph: x 8:00 to 12:00 (ticks each 30 min), y -20 to 60 °C (ticks each 10, labels each 20). Blue band from -20 to 4 °C
  "Cold zone: 4 °C (40 °F) or colder". Lines: Lunch (thick, brand red, solid), one line per pack kind present (Frozen
  bottle blue solid, Steel cubes gray long dash, Fridge bottle blue dotted), Car air (brown short dash). The last run's
  lunch line stays as a faded ghost. Clock "9:40" above the graph; car air readout "Car air 48 °C (118 °F)".
- Verdict over the graph's top after a run (Content). A log row is added: run number, walls, cover, seal, packs, cost,
  "cold until" time, job met or not.
- Engineer's check: after the first run that keeps lunch cold to noon within $8, a card opens over the log: two
  questions (Content), one pick each, then a note box "Which change mattered most? Use your log as evidence." (up to
  280 characters, `Save note`), with "Your note stays on this device. Nothing is sent anywhere."

What the picture shows for each outcome: lunch line leaves the cold zone at once (bare box: red line climbs past the
band within a minute, ends at 55 °C, above the car air because the sun heats it); ice too small (blue pack line flat at
0, then climbs; the red line follows it out of the band; ice cutout goes from frozen to half to melted); steel (gray
line climbs from -18 with no flat part; steel cutout loses its frost); fridge bottle (dotted line starts at 3 and
climbs); passing design (red line stays in the band to 12:00, blue line still flat, ice cutout still half frozen).

### Bench
Focus: the two sample lines on the graph. At 1366x768, stage left: the painted lab bench (cc-bench) top strip (about
260 px) with two painted test cups on warming plates, A left and B right, each sample cutout inside (ice block, water,
steel block), each cup with a code thermometer and its temperature; under it the graph (about 400 px). Panel: hint;
three question cards; two setting blocks, `Sample A` and `Sample B`, each four segmented rows: Material (Water,
Steel), Mass (100 g, 200 g, 400 g), Start (Freezer -18 °C, Fridge 3 °C), Heat (Low, High); `Check plan`; then
`Predict` row (A, B, Same) and `Run`; after the run the setting blocks fold to one summary line and four claim buttons
show. At 680x425 the bench strip folds to two small thermometers over the graph; the panel keeps all rows (36 px tall,
44 px targets).
- Graph: x 0 to 30 minutes on the plate, a second axis under it "Heat added: 0 to 3 kJ" (Low) or "0 to 6 kJ" (High)
  when both match; y set before each run from both samples' start and end, padded 5 °C, rounded to 5, at least 20 °C
  tall, fixed during the run. Lines A (brand red) and B (blue), with letters at their ends. Under the cups, two equal
  "Heat added" bars that fill as the run goes. After the run each cup shows "Change: +7.3 °C".
- Caption under the cups: "Temperature tells how fast the particles move, on average."
- Question cards carry a mark: blank, "tested" (right claim first try), or "tested, fixed" (claim fixed).

## Content
Model (Build), all in code, step dt = 10 s explicit Euler, 8:00 to 12:00 (1,441 steps), in this order each step:
car air, the three flows, pack exchange, lunch update, cold check.
- Car air: outside 27 °C (80 °F), sunny. Rise over outside, °F, at minutes 0, 10, 20, 30, 40, 50, 60: 0, 20, 28, 33,
  37, 39.5, 41; linear between; 41 from 60 to 240 minutes (max 121 °F, 49.4 °C). Shown on screen as °C with °F.
- Box: area A = 0.18 m². Resistance R (m²·K/W) = 0.12 inside film + 0.08 outside film + 0.01 shell + layers. Per 10 mm
  layer: Foam 0.286, Cotton batting 0.250, Cardboard (two 5 mm sheets) 0.154, Sealed air gap 0.150. UA = A / R.
- Conduction flow = UA × (car − lunch). Convection flow = leak × (car − lunch), leak 0.08 W/K, 0.008 with Lid seal.
  Radiation flow = absorptance × 500 W/m² × 0.05 m² × 0.08 / R; absorptance: None (blue plastic) 0.6, Foil 0.1, Black
  cloth 0.9.
- Lunch: 300 g, heat capacity 1,050 J/K, starts 3.0 °C. Packs: 200 g each; Frozen bottle (ice, -18 °C), Steel cubes
  (-18 °C), Fridge bottle (liquid water, 3 °C). Each pack trades 2.5 W/K × (lunch − pack) with the lunch. Pack state by
  energy: ice 2.05 J/g·°C below 0, melts at 0 °C taking 334 J/g, water 4.18 J/g·°C; steel 0.47 J/g·°C.
- "Cold until" = the first step the lunch is above 4.0 °C, shown rounded down to the minute ("Cold until 10:45"); never above it =
  "Cold until noon".
- Pack slots: 0 or 1 layer, 4 packs; 2 layers, 3 packs; 3 layers, 2 packs. At most 3 layers (30 mm).
- Prices: Foam $2, Cotton batting $1.50, Cardboard $0.50, Sealed air gap $1, Foil $1, Black cloth $0.50, Lid seal $1,
  Frozen bottle $1, Steel cubes $3, Fridge bottle $1. Budget $8.
- "Slows heat" bar on wall tiles, length in proportion to R per 10 mm (Foam longest, Cardboard and Air gap about half).
- Anchor runs (Python, Sources): bare box 8:00, ends 55.5 °C (car 49.4); 1 frozen bottle bare 8:04; 4 bottles bare
  8:18; 4 bottles bare with Foil and seal 8:57; Foam x2 + seal, no packs 8:02; Foam x3 + Foil + seal, no packs 8:03 (ends
  45.9 °C); Foam x2 + seal + 2 bottles 11:26; Foam x2 + Foil + seal + 2 bottles 11:48; Foam x2 + 2 bottles, no seal
  10:45; Foam x2 + seal + 3 bottles noon ($8); Foam x2 + Foil + seal + 3 steel 8:14; same with 3 fridge bottles 8:05;
  Cotton + Cardboard + seal + 3 bottles noon ($6, cheapest pass).
- Verdicts: noon within $8 "Cold until noon. Job done for $7.00."; noon over budget "Cold until noon, but $9.50 is over
  the $8 budget."; short "Cold until 10:45. Lunch left the cold zone 1 h 15 min early."
- Engineer's check (shuffled, lengths within about 25 percent, one try each):
  1. "Why did the ice in your box melt?" Right: "Heat from the hot car moved into the box and the ice." Others: "Cold
     from the ice leaked out through the walls."; "The ice made its own heat as it sat there."; "The foam and cloth
     warmed up the ice on purpose." Reasons after a wrong pick: "The arrows all point in: heat moves from warmer to
     cooler, and cold is not something that flows."; "Ice does not make heat; it takes heat in as it melts.";
     "Insulation makes no heat; it only slows heat coming in."
  2. "Could thick walls keep lunch cold till noon with no packs?" Right: "No. Walls only slow heat, so lunch still warms
     up." Others: "Yes. Thick enough foam stops heat completely."; "Yes. Foam keeps cold in as well as heat out."; "No.
     Foam makes heat that warms the lunch." Reason: "Try it: three foam layers, foil and the seal, no packs, and lunch
     leaves the cold zone at 8:03."
- Bench: heat Low = 3 kJ, High = 6 kJ, added evenly over 30 minutes to each sample in a sealed test cup (no other heat
  in or out). Same physical values as Build. Final temperatures (start -18 or 3 °C), change in °C:
  water freezer 100 g Low -3.4 (14.6), High 0.0 (18.0, ice reaches 0 °C at 18.4 min, then melts flat); 200 g -10.7
  (7.3), -3.4 (14.6); 400 g -14.3 (3.7), -10.7 (7.3). Water fridge 100 g 10.2 (7.2), 17.4 (14.4); 200 g 6.6 (3.6), 10.2
  (7.2); 400 g 4.8 (1.8), 6.6 (3.6). Steel (either start) 100 g change 63.8, 127.7; 200 g 31.9, 63.8; 400 g 16.0, 31.9
  (highest end 130.7 °C, steel 100 g fridge High).
- Questions and claims (one right; shuffled; one try):
  - Mass: "Does a bigger sample change temperature less?" Right: "With the same heat, the bigger mass changed
    temperature less." Others: "With the same heat, the bigger mass changed temperature more."; "Mass made no
    difference to how much the temperature changed."; "The bigger mass had more heat added to it."
  - Matter: "Do water and steel warm up the same?" Right: "With the same mass and heat, steel changed temperature much
    more." Others: "With the same mass and heat, water changed temperature much more."; "They changed the same,
    because they got the same heat."; "Steel had more heat added to it than water."
  - Energy: "Does more heat make a bigger temperature change?" Right: "More heat added made a bigger temperature
    change." Others: "More heat added made a smaller temperature change."; "The amount of heat made no difference to the
    change."; "More heat added changed the mass of the sample."
- Plan notes: identical "A and B are the same. Change the one thing your question is about."; wrong only "You changed
  [Heat], but your question is about [Mass]."; extra first miss "A and B differ in [n] ways. A fair test changes only the
  thing your question asks about."; second miss names them "They differ in [Mass] and [Heat]."

## Interactions in detail
- Adding a layer fills the next of 3 slots (inside first). If the new pack limit is below the packs in the box, the
  layer is not added and the hint says "Take out a pack first: with 2 layers, 3 packs fit." Adding a 4th layer: "Three
  layers is the limit. Tap a layer in the box to take it out." Pack tiles past the limit: "No room for another pack."
  Covers are a one-pick row; the seal toggles. Meters update at once; cost over $8 turns warn color but Run still works.
- Arrows before a run preview 9:00 (car 49.4 °C, lunch 3 °C); during a run they follow the clock. Width 2 px + 22 px ×
  min(|flow|, 40 W) / 40. A flow below zero flips the arrow outward (the bare box from about 8:52, hotter than the car
  air from the sun) with label "heat out: the box is hotter than the air".
- Run: 4 hours in 24 s (10 minutes a second), clock and lines draw in step; `Skip to noon` finishes at once. With Motion
  off the run still takes 24 s (timing kept) but lines draw without easing and the ice cutout swaps states without fade.
- Any change to the box during a run stops it at once: the partial lunch line becomes the ghost, the clock goes to 8:00,
  and the new box is ready (hint: "You changed the box, so the test starts over at 8:00. Tap Run."). Mode switch during
  a run stops it the same way. Taps never wait for the run.
- Ice cutout state: frozen while the pack is below 0 °C, half from 0 °C with under half melted, mostly melted past half,
  water bottle once fully melted. Steel: frosty below 0 °C, plain above.
- Log keeps every run this session (paged 4 at a time). `Clear log` sits under it. Reset is the kit's: back to load.
- Engineer's check opens once; after it, a "Job done" badge on the job card with "Engineer's check: 2 of 2" or "1 of 2,
  fixed". The note saves to localStorage `curio-cooler-note` (try/catch); a later pass reopens the note only.
- Bench: defaults A and B both Water, 200 g, Fridge, Low. `Check plan` needs a question picked (until then the hint
  says "Tap a question first."). A fair plan locks the settings (`Change plan` unlocks and clears the prediction).
  Predict is one pick, changeable until Run; Run needs a prediction. Run 30 minutes in 10 s; claim buttons show after.
  A claim pick marks the question card; `Next question` resets the settings to defaults. A sample at 0 °C with ice left
  shows "melting" on its thermometer.
- `window.__tool = {state, setMode, build: {add(id), remove(slot), cover(id), seal(on), pack(id), run(), skip(),
  result()}, bench: {question(id), set(side, row, value), check(), predict(v), run(), claim(k)}, allLines, vlog}`.

## Look
Light lunch-counter palette: paper `#f3f6f8`, panel `#ffffff`, ink `#18222e`, muted `#566270`, button line `#7a8592`,
focus `#1f5fd1`, ok `#1d7a3c`, warn `#a3261b`. Accent `--brand #b32630` (lunchbox red: lunch line, Run, sample A).
Cold zone `#dcedf9` with edge and pack line `#1f6aa8`; steel `#4f5966`; car air `#8a5300`. Neighbors use copper
`#b4400f`, ember orange, clay, pink and gold; none is this red. Contrast (computed): ink on paper 14.80:1, panel 16.07:1;
muted 5.73:1 / 6.22:1; brand 5.98:1 / 6.49:1, on the cold zone 5.41:1; white on brand 6.49:1; pack blue 5.25:1 / 5.70:1,
on the zone 4.76:1; car brown 5.83:1; steel 6.55:1; ok 4.96:1; warn 6.79:1; focus 5.35:1; button line 3.46:1
(non-text). Lines also differ by dash and labels, never color alone.

## Art
Local FLUX, one style: warm painted realism, soft morning light. No people or animals anywhere (`people: false`).
- cc-car: "Inside a parked car on a sunny morning, view from the back seat toward the windshield, bright sun streaming
  onto an empty gray back seat, warm dusty light"; 16:9; cutout no; Build backdrop (the box sits on the seat).
- cc-lunch: "A wrapped turkey sandwich beside a red apple"; 1:1; cutout yes; inside the cutaway.
- cc-ice-frozen, cc-ice-half, cc-ice-melted, cc-water-bottle: "A plain clear plastic water bottle frozen solid and
  frosty" / "half melted, ice floating in water" / "almost all water with a sliver of ice" / "full of cold water with
  beads of condensation" (the last is also the Fridge bottle); 3:4; cutout yes; pack slots and the Frozen bottle tile.
- cc-steel-frost, cc-steel: "A small pile of stainless steel cubes covered in white frost" / "the same steel cubes,
  shiny and dry"; 1:1; cutout yes; packs and tile.
- cc-sw-foam, cc-sw-cotton, cc-sw-card, cc-sw-air, cc-sw-foil, cc-sw-cloth: full-frame textures: "white polystyrene
  foam sheet", "fluffy white cotton batting", "corrugated cardboard edge showing its flutes", "two clear plastic sheets
  with a thin gap", "crinkled shiny aluminum foil", "black cotton fabric"; 1:1; cutout no; tiles and clipped into wall
  bands.
- cc-bench: "A tidy school science bench with two small warming plates, blank surfaces, a window behind"; 16:9; cutout
  no; Bench backdrop.
- cc-cup: "An empty clear insulated test cup with a lid"; 3:4; cutout yes; used twice.
- cc-ice-block, cc-water-sample, cc-steel-block: "A clear block of ice" / "cold water in a clear cup insert" / "a
  smooth steel block"; 1:1; cutout yes; inside the cups, scaled by mass (100 g 60 percent, 200 g 80, 400 g 100).
All lettering (labels, prices, readouts) is code over blank surfaces. Box cutaway, arrows, graphs and meters are code.

## Voice
Bank voice `friendly-dad` (Achird), style "Say in a relaxed, friendly way, like a parent who packs lunches and loves a
kitchen experiment." Not used by a neighbor (hot-meets-cold clear-teacher, hand-warmer-lab news-reader,
which-way-is-down upbeat-guide, living-pond gravel-ranger, molecule-forge knowing-guide, span-and-spire firm-captain).
`Curio.voice`, `scope: () => state.mode`. Grade 6: times, prices and numbers are read on screen; no line reads data.
| Key | Kind | When | Stale when | Whole | Text |
|---|---|---|---|---|---|
| wBuild | how | Build welcome | a run started | no | Lunch rides in a hot car from eight until noon. Tap a material to add a wall layer, then tap Run. |
| wallFull | how | 4th layer tapped | a layer removed | no | Three layers is the limit. Tap a layer in the box to take it out. |
| packFirst | how | layer blocked by packs | a pack removed | no | Take out a pack first. Thicker walls leave less room inside. |
| noRoom | how | pack past the limit | a pack removed | no | No room for another pack. Thicker walls leave less room inside. |
| run1 | how | first Run | run ended | no | Watch the red lunch line. Lunch is safe while it stays in the blue cold zone. |
| flat | how | first ice line flat at 0 for 10 sim minutes | run ended | no | See the flat blue line at zero? The ice is melting. Melting takes in heat without getting warmer. |
| restart | how | first edit during a run | Run tapped | no | You changed the box, so the test starts over at eight. Tap Run when you're ready. |
| pass | event | noon within budget | box changed | yes | Cold until noon. Job done. |
| passOver | event | noon over budget | box changed | yes | Cold until noon, but it's over budget. Can you do it for eight dollars? |
| short | event | run ends short | box changed | yes | Lunch left the cold zone early. Change one thing and run it again. |
| check | how | engineer's check opens | check closed | no | Two quick questions from the engineer. Tap one answer for each. |
| right | event | right pick | next pick | yes | Right. |
| wrong | event | wrong pick | next pick | yes | Not quite. Read why under your answer. |
| note | how | after question 2 | note saved | no | Last step: in the note box, say which change helped most. Your log is the evidence. |
| wBench | how | Bench welcome | plan checked | no | Welcome to the test bench. Tap a question, then set A and B so only one thing is different. |
| fair | event | fair plan | Change plan | yes | Fair test. Only one thing is different. |
| unfair | event | any unfair plan | settings changed | yes | Not a fair test yet. Read the note, fix it, and tap Check plan. |
| predict | how | after fair (first time) | Run tapped | no | Which sample will change temperature more? Tap A, B or Same, then tap Run. |
| runB | how | first bench Run | run ended | no | Both samples get the same heat. Watch how far each line moves. |
| claim | how | first claim buttons | claim picked | no | Tap the sentence your graph supports. You get one try. |
| benchDone | event | third question marked | mode left | yes | All three questions tested. That's a full investigation. |
How lines once per page load, then hint only. Event lines every time, at most once per action; unfair at most once per
`Check plan` press. Read speaks the hint (with the job card on Build before the first run).

## Family engine
none: the tool draws its own cutaway, arrows and two small line graphs in SVG (live sweep, ghost line, cold band and
flipping arrows need no shared engine; no family covers thermal models yet).

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Build job "cold until noon on $8" | guessing or mashing tiles; buying the most of everything; only packs; only walls; steel because metal feels cold; fridge bottles; doing nothing; reading the answer off the screen | of 3,450 possible boxes 31 pass within $8 (0.9 percent; about 77 random runs at 24 s each for even odds); with no budget only 46 pass, and over budget is flagged in the verdict and log; 4 bottles and no walls: 8:18 (8:57 with foil and seal); 3 foam layers, no packs: 8:03; no box with any steel or fridge bottle passes; the bare box fails at 8:00; nothing on screen names a passing box (arrows show paths, which is the principle the student must apply) |
| Budget and wall limits | ignore them | the walls cap at 3 layers and pack slots shrink in code; cost shows live and over $8 is never "Job done" |
| Engineer's question 1 (why the ice melted) | guess; longest option; position; the common wrong "cold leaked out" | one try, shuffled each opening, lengths within 25 percent; "cold leaked out" is marked wrong with its reason; guess odds 1 in 4; no line or hint says "cold doesn't flow" before it (arrows only show direction) |
| Engineer's question 2 (walls alone) | guess; pick "Yes" because foam was what helped | one try; both "Yes" options are wrong; guess 1 in 4; the reason sends them to the 8:03 run |
| Engineer's note | type anything | not a check: nothing scores it; the teacher reads it; Done when never relies on its text |
| Bench plan (fair test) | leave A and B the same; change everything; change the wrong row; mash rows until it says fair | identical gets "the same" note; extra changes get a count, then names on the second miss; the wrong row gets "your question is about Mass"; mashing does reach fair, so the plan is never the score: the card marks first-try fairness in the bench log, and only the claim marks a question tested |
| Prediction | any pick | not scored; shown beside the result only |
| Bench claim (each question) | guess; position; longest; same slot every time; elimination across questions; read A or B off the graph; the common wrong ("bigger mass changed more", "same heat so same change") | one try, shuffled; each question has its own four claims, so nothing repeats; claims are about mass, matter or heat, never "A" or "B", so the graph must be tied to the settings; the common wrongs fail; "more heat was added" options fail because the equal bars show it; every fair setup (all 24 settings, Python) agrees with the right claim |

## Heard in order
Grade 6: not every line is voiced, but results land before the next prompt.
- Build run: Run, then run1 (first run only), flat (when the ice holds 10 minutes), then at the end pass, passOver or
  short, whole; check plays only after pass finishes. A tap during the run drops queued how lines, never a verdict.
- Engineer's check: check; pick 1, right or wrong whole; pick 2, right or wrong whole; then note.
- Bench: Check plan, then fair or unfair whole; then predict (first time); Run, runB; at the end claim; the pick, right
  or wrong whole; benchDone after the third card's result. Changing a setting drops a queued fair or unfair line.
- The welcome may be cut by the first tap (BASELINE rule 16); its content stays in the hint, the job card and Read.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| A closed car in sun warms about 20 °F in its first 10 minutes | NY Governor's Traffic Safety Committee release (NHTSA figure), dmv.ny.gov | McLaren, Null, Quinn, Pediatrics 2005;116:e109, Fig 3 | yes |
| About 40 °F warmer within an hour, most of it in the first 30 minutes, near its peak at about 60 minutes | McLaren et al. 2005 (mean 41 °F, range 28 to 49; 80 percent in 30 min) | Consumer Reports test (61 °F outside, over 105 °F in one hour) | yes |
| Never leave a person or pet in a parked car (teacher notes) | weather.gov/safety/heat-children-pets | McLaren et al. 2005 | yes |
| Keep cold food at 40 °F (4 °C) or colder; 40 to 140 °F is the danger zone | USDA back-to-school food safety release, 2025 | FSIS "Keeping Bag Lunches Safe" | yes |
| Pack at least two cold sources in an insulated lunch box | same USDA release | same FSIS handout | yes |
| Freezer 0 °F (-18 °C); fridge 40 °F or colder | FDA "Are You Storing Food Safely?" | FSIS "Freezing and Food Safety" | yes |
| Heat flows from warmer to cooler; insulation slows it; by conduction, convection and radiation | DOE Energy Saver "Insulation" | OpenStax College Physics 2e, ch 14 | yes |
| Melting ice stays at 0 °C while taking in heat, about 334 J/g | OpenStax 2e 14.3, Table 14.2 | Engineering ToolBox "Water: heat of fusion" | yes |
| Specific heats: water 4.18, ice about 2.05, steel 0.45 to 0.50 J/g·°C (model 0.47) | OpenStax 2e Table 14.1 | Engineering ToolBox specific heats | yes |
| Per thickness, foam slows heat best, then cotton batting, then cardboard and a thin sealed air gap | Engineering ToolBox thermal conductivity tables | ASHRAE Handbook Fundamentals, ch 26 (materials, air spaces) | yes |
| Shiny foil reflects most sunlight; black cloth absorbs most | Engineering ToolBox solar absorptance | Incropera, Fundamentals of Heat and Mass Transfer, Table A.12 | yes |
| Temperature measures the particles' average motion (kinetic energy) | NGSS MS-PS3-4 wording | OpenStax 2e 13.4 | yes |
| MS-PS3-3 and MS-PS3-4 wording and boundaries (no energy totals) | nextgenscience.org | NSTA NGSS hub | yes |
Backed twice: 13. Cut: gel packs (their melting heat varies by brand, no two sources agree), frozen grapes (freezing
point needs a food table), the 2-hour discard rule (not needed on screen). Model values not shown as facts (films, leak,
sun, pack contact, lunch heat capacity) are labeled "model" in teacher notes.
Number checks (Python 3, 2026-11-06): every anchor run in Content; all 3,450 boxes enumerated: 31 pass within $8, 46 at
any cost, none with steel or fridge bottles, 5 of the 31 without the seal, 4 with black cloth; dt 10 s against 2 s
flips no verdict; 82 boxes end between 200 and 239 minutes (near misses to improve from); bare box ends hotter than the
car air (55.5 against 49.4 °C), so its arrows flip; bench: all 24 settings and every one-variable pair agree with the
right claims; bench range -14.3 to 130.7 °C; the only bench plateau is water 100 g freezer High at 18.4 min.

## Done when
1. Focus and one idea: Foam x2 + seal + 2 bottles gives "Cold until 11:26"; adding a third bottle gives "Cold until
   noon. Job done for $8.00." with the blue line flat at 0 °C and the ice cutout half melted at noon.
2. Arrows: adding Foil shrinks Radiation, the seal shrinks Convection, each foam layer shrinks Conduction; the bare
   box's Conduction arrow flips outward late in its run.
3. The anchor runs in Content match to the minute; 3 steel or 3 fridge bottles fail; over $8 is never "Job done".
4. Engineer's check opens after the first in-budget pass, one try each, shuffled; the note says it stays on the device.
5. Bench: identical, extra and wrong-row plans get their notes; a fair plan locks; the equal heat bars fill together.
6. Bench claims: Mass, Matter and Energy each mark right only for the listed sentence; benchDone after the third.
7. A tap during a Build run restarts at 8:00 with a ghost line; a tap during a bench run acts at once.
8. At 1366x768 the cutaway, graph, all tiles, meters and Run sit above the fold; at 680x425 stage and panel stay side
   by side with the log in a `Log` button.
9. Voice: how lines once each, verdicts and results whole and before the next prompt, no line names a disabled control.
10. No person or animal in any art; no network requests, no console errors.

## Open questions
None. MS-PS3-5 stays with half-pipe-energy (gaps.md row 9); the module lists only MS-PS3-3 and MS-PS3-4.

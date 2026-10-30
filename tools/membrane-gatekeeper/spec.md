# Membrane Gatekeeper

## One idea
You are the cell membrane: molecules stream at a living cell from both sides and you open and close protein gates
(water channel, glucose carrier, sodium channel, potassium channel, the sodium-potassium pump, and a chloride
channel in the last level)
to keep the inside in balance, learning by playing that channels and carriers only let things flow downhill, that
oxygen slips straight through the lipid, and that only the pump, paying ATP, pushes uphill; each level is a
different specialized cell (red blood cell, gut lining, nerve, kidney, airway) reached by zooming in from the body.

## Not like
- cell-city (grade 6, cells family): a tour of organelles as parts of a city. Here only the membrane, live, as a
  game of gates and gradients.
- mitosis-mixer (same group, cells family): sorting dividing cells in a microscope field. Here one cell's boundary,
  in real time.
- body-thermostat (same group): a whole-body feedback loop with sliders. Here you are the control, at the scale of
  molecules, with keys.
- gas-law-lab and hot-meets-cold (sci 10 and 11): particles spreading out with no gatekeeper. Here diffusion is
  only half the story: proteins choose what crosses.
- bug-hunt (sci 8, arcade): a predator reflex game. Here the arcade timing serves a rule set (downhill only, pump
  costs ATP) that the score depends on.

## Who and how
Grade 9, science (Life Science module Cell Structure and Function: "Organelles and transport"). Driver: students on
laptops, one each, keyboard or touch. 15 to 30 minutes. Standards: HS-LS1-2 (a model of the hierarchical organization
of interacting systems: body, organ, tissue, cell, membrane, shown by each level's zoom-in), HS-LS1-1 (DNA codes for
proteins that do the work of cells: every gate is a protein; the airway level shows a protein made from a changed
gene that never reaches the membrane).
Topic line: cell membranes and transport.
9-12 dark theme. Header: title, `.seg` modes **Levels**, **Lab**, kit buttons `motion`, `sound`, `read`.

## Screens and modes
Stage: the membrane as a wide horizontal band across the middle (two rows of phospholipid heads with tails),
OUTSIDE above (a darker blue-gray field), INSIDE below (a warmer field with the cell's meters). Gate proteins sit in
fixed slots in the band, each with its key number and name; an open gate draws as a parted shape with a glow, a
closed one as a shut barrel. Tokens drift toward the band from both sides, each a shape with its label (H2O
drop, glucose hexagon "Glc", Na+ circle, K+ circle, O2 and CO2 pairs, Cl- square, ATP small star inside only).
Panel right: meters, gate list with keys, `hint`, `tip`. Under 900 px tall: meters move into one row under the
stage; gate list becomes a row of key buttons under the band (also the touch controls).

**Levels** (opens first). Focus: the membrane band with tokens crossing it, across the middle of the stage, with the
meters right beside it; nothing else on the stage is larger. Five levels, each opened by a 3 s zoom ladder (body,
organ, tissue, cell, membrane; skippable with Esc or a **Skip** button, instant with Motion off) with one caption per
step: the body step is a code body-map outline (no face) with the organ highlighted, the organ, tissue and cell steps
are painted (Art), and the membrane step is the live band. A level lasts 90 s; the token rate ramps from 1 to 4 tokens
per second. It runs longer than 30 s because the student plays it, pressing a gate every few seconds; every key and
button acts on the very next frame, and the clock never takes control away. The cell's meters each have a green band; **balance time** counts the seconds with
every meter in its band. End card: balance time out of 90, one line on what that cell does, **Replay**, **Next
level** (all levels open from the start; no locks). Pause with P or the Pause button.

**Lab** (no clock, no score). Focus: the band with its net flow arrows, center stage. Pick any level's cell (five
buttons, each with its painted cell picture); sliders set the outside amount of each substance (Low, Normal,
High) and each gate is a switch. Arrows on the band show net flow per gate (thickness = rate). **Step** and **Run**.
This is where students test a claim ("does the glucose carrier ever pump uphill?"). During **Run** every switch and
slider stays live and the arrows redraw on the next step.

## Content
Transport rules (enforced by the game, explained on screen when a token is refused):
- O2 and CO2 cross the lipid itself, no gate, always down their gradient. Nothing the player does stops them.
- Water crosses through aquaporins toward the side with more dissolved particles (osmosis); a little crosses the
  lipid slowly without them.
- Glucose carrier, Na+ channel, K+ channel, Cl- channel: each moves only its own substance, only from more to less
  (downhill). A token arriving at an open gate on the low side is refused with "Channels only let things flow
  downhill."
- Na+/K+ pump: each cycle spends 1 ATP and moves 3 Na+ out and 2 K+ in, against their gradients. With ATP at 0 it
  stops.
- Big molecules (shown as a large "protein" blob outside) never cross: no gate fits.
Meters (game units 0 to 100; real values shown in the info card): Water (cell volume, green 90 to 110), Glucose
(green 40 to 80; the cell burns 1 per second and makes ATP from it, 1 ATP per 2 glucose units, game scale), Na+
inside (green 5 to 20), K+ inside (green 120 to 150 on its own 0 to 160 scale), ATP (green 20 and up).
Real resting values in the info card (mammalian cell, mM): Na+ inside 5 to 15, outside 145; K+ inside 140, outside 5;
Cl- inside 5 to 15, outside 110 (Alberts Table 11-1). Blood glucose about 5 mM.
Levels:
1. Red blood cell (blood): gates 1 aquaporin, 2 glucose carrier. Waves of saltier plasma and more watery plasma
   push water out and in; the skill is to close the water channels while a wave passes and open them when the plasma
   is normal again, so the cell swells or shrinks back to size. Info: red blood cells shrink in salty water and swell
   in pure water.
   Water rule (game values): outside particle level o is 100 in normal plasma, 135 in a salty wave, 65 in a watery
   wave; inside level c = 100 x 100 / volume; volume changes by k x (c minus o) per second, k = 0.04 through the lipid
   alone plus 0.08 with the aquaporins open. Wave plan (90 s): normal 10 s, salty 8 s, normal 10, salty 8, normal 10,
   watery 8, normal 10, salty 8, normal 10, salty 8 (the seed may shuffle the order of the waves only).
2. Gut lining cell (small intestine): adds 5 the pump. After-meal pulses bring lots of glucose; glucose carriers
   bring it in; the pump keeps Na+ low.
   Glucose rule (game values): outside glucose is 30, rising to 90 for 15 s every 30 s from second 5 (a meal); the
   cell burns 1 unit a second; an open carrier moves 0.03 x the higher side's amount per second from the higher side
   to the lower (one token drawn per 2 units). So the skill is to open the carrier during a meal, close it before the
   meter passes the top of its band, and keep it closed between meals, or glucose leaks back out.
3. Nerve cell: gates 3 Na+ channel, 4 K+ channel, 5 pump. A "Signal" prompt appears every 8 to 12 s: open Na+ (Na+
   rushes in), then within 2 s open K+ (K+ flows out) to complete a signal (a spark runs along a small axon
   drawing); then the pump restores both. Each completed signal counts.
4. Kidney cell (collecting duct): starts with no aquaporins in the outside-facing membrane. When the body is
   short of water an ADH hormone token arrives and two aquaporin slots appear (key 1). Keep them open while
   "Body: thirsty" shows, closed while "Body: well watered" shows.
5. Airway cell (lungs): gate 6 the CFTR Cl- channel. Letting Cl- out pulls water after it, keeping the mucus layer
   above the cell thin (a mucus-thickness meter). **Gene** toggle: Typical CFTR / F508del CFTR. With F508del the
   CFTR protein misfolds and never reaches the membrane: its slot shows an empty, grayed outline, key 6 does
   nothing, and the mucus slowly thickens. Card (calm, factual): "This change in the CFTR gene is the most common
   cause of cystic fibrosis. The protein is made but folds wrong, so the cell destroys it. Medicines called CFTR
   modulators help some of it fold and reach the membrane." No score on this level with F508del (balance time hides).
Hints: Levels "<b>Levels.</b> Keys 1 to 6 open and close gates. Keep every meter in its green band." / Lab
"<b>Lab.</b> Set the outside amounts, switch gates on, press Run. Which way does each one flow?"
Tips: "A channel is a door, not a pump: it can't push uphill." / "Water channels speed water both ways; they can't
choose a direction." / "The pump spends about a third of a resting cell's ATP in many cells." (verify; drop if
unconfirmed) / "Every gate is a protein, built from a gene." / "Oxygen doesn't
need a door: it dissolves straight through the lipid."
Model limits line: "Game numbers are scaled. Real membranes have thousands of each protein, and many more kinds."

## Interactions in detail
- Keys 1 to 6 toggle gates (and on-screen buttons with `aria-pressed`, also the touch controls). Holding is not
  needed. A gate that is not part of the level is hidden, not disabled.
- Tokens move at fixed speed; a token at a closed gate or the bare lipid bounces (except O2 and CO2). Refusals show a
  short label near the gate once per level per reason.
- Scoring: balance time only; no lives, no game over. Meters out of band blink their band edge (no blink with Motion
  off) and say "low" or "high".
- Seeded token stream (cells engine Membrane uses probability.js `Rand(seed)`, seed fixed per level) so every
  student gets the same level.
- Pause on blur (window loses focus). Mode change: `V.hush()`, level stops.
- Sound starts on (kit): soft click on gate open, low thud on refusal; silent with Sound off.

## Look
Accent `--brand #f01aff` (neon magenta, arcade), `--brand-ink #10161f`. The painted zoom ladder pictures show only
during the zoom and on the end card and Lab buttons; the play stage itself stays the flat fields below so token
contrast holds. Stage outside `#121a26`, inside `#1a1520`,
membrane heads `#c9d6e2` with tails `#6e7d8c`. Token colors (each also has its label and shape): water `#6cc8ff`,
glucose `#ffd25e`, Na+ `#ff8a5c`, K+ `#9be564`, Cl- `#7fe0e0`, O2 and CO2 `#c9c9d6`, ATP `#f01aff`.
Contrast (computed): brand on --panel 5.19:1, on --sec-bg 4.92:1; brand-ink on brand 5.44:1. Nearest 9-12 accent
#ff5cf0 (dE 27); every accent in this group is 78 or more away. Tokens on the outside field `#121a26` and inside
`#1a1520` (computed): water 9.44 and 9.68, glucose 12.18 and 12.48, Na+ 7.53 and 7.71, K+ 11.47 and 11.76, Cl-
11.35 and 11.64, gases 10.66 and 10.93, ATP 5.24 and 5.37.

## Art
Local FLUX (`scripts/localart.py`), no people. 15 images, all for the zoom ladder (16:9, cutout no, people no), the
cell pictures also on the level end card and the Lab cell buttons. House style: clear scientific illustration, soft
light, rich but calm colors on a dark background, no lettering. The body step stays a code body-map outline (a
diagram: a plain outline with the organ lit), so no person is painted.
- Organ step: mg-organ-blood (a branching blood vessel cut open, full of red blood cells flowing), mg-organ-gut (a
  section of small intestine, pink and folded), mg-organ-nerve (a white nerve bundle branching along a limb's muscle),
  mg-organ-kidney (a kidney cut in half showing its pale outer layer and dark inner pyramids), mg-organ-lungs (a pair
  of pink lungs with branching airways).
- Tissue step: mg-tissue-blood (a crowd of red blood cells drifting in pale yellow plasma), mg-tissue-gut (finger-like
  intestinal villi covered in a single layer of cells), mg-tissue-nerve (a web of nerve cells with long threads),
  mg-tissue-kidney (a cross-section of small tubes lined with cube-shaped cells), mg-tissue-airway (an airway lining
  of tall cells topped with fine hair-like cilia under a thin mucus layer).
- Cell step: mg-cell-rbc (one red blood cell, a smooth red disc dimpled in the middle), mg-cell-gut (one tall gut
  lining cell with a brush border of tiny fingers on top), mg-cell-nerve (one nerve cell with a round body, branching
  short arms and one long fiber), mg-cell-kidney (one cube-shaped kidney duct cell with a round nucleus), mg-cell-airway
  (one tall airway cell with cilia on top).
The band, gates, tokens, meters, mucus meter and axon spark stay in code: they move, open and count every frame.

## Voice
Bank `lively-host` (an arcade host): quick, bright, short lines. Uses `Curio.voice`, scope = mode. How lines speak
once per page load, then only update the hint; event lines speak each time.
- welcomeLevels (how; on entering Levels; stale once a level starts): "Welcome to Membrane Gatekeeper. Keys one to six
  open and close the gates. Keep every meter in the green."
- welcomeLab (how; on entering Lab; stale once Run or Step is pressed): "Lab. Set the outside amounts, switch gates
  on, and press Run."
- levelRbc (how; first start of level 1; stale when the level ends): "Red blood cell. Press one to close the water
  channels during a wave, and open them when it passes."
- levelGut (how; first start of level 2; stale when the level ends): "Gut lining. Press two to open the glucose
  carrier during a meal, press it again before the meter tops out, and press five to run the pump."
- levelNerve (how; first start of level 3; stale when the level ends): "Nerve cell. When you see Signal, press three
  for sodium, then four for potassium."
- levelKidney (how; first start of level 4; stale when the level ends): "Kidney cell. When the hormone arrives, press
  one to open the new water channels while the body is thirsty."
- levelAirway (how; first start of level 5; stale when the level ends): "Airway cell. Press six to let chloride out,
  and water follows it."
- uphill (how; first refusal in a level; stale after 3 s): "That gate can only let things flow downhill."
- signal (event; each completed signal; stale after 2 s): "Signal sent."
- f508 (event; each switch to F508del; stale on switching back to Typical): "This version of the protein folds wrong
  and never reaches the membrane."
- levelEnd (event; each level end; stale once a button is pressed): "Time. Here's your balance time. Press Next level
  or Replay."
On level 5 with F508del, key 6 does nothing, so no line names it while F508del is on.

## Family engine
**cells** family. This spec describes the shared engine in full for the unspecced siblings cell-city (grade 6,
explorer) and mitosis-mixer (this group).
`kit/cells.js` (depends on `kit/probability.js` for seeded randomness):
- `Parts`: the organelle catalog. Each part: `id`, `name`, `job` (one plain sentence), `in` (animal, plant, both),
  `draw(ctx, x, y, size, style)`. Parts: membrane, cell wall, nucleus, nucleolus, chromosomes, mitochondrion,
  chloroplast, ribosome, rough ER, smooth ER, Golgi, lysosome, vacuole, vesicle, cytoskeleton. A tool may attach its
  own text per part (cell-city adds city analogies: nucleus as city hall).
- `CellView(el, {kind, style, phase, labels, seed})`: draws one cell. `kind`: animal, plant, red blood cell, nerve,
  gut lining, kidney, airway, onion root. `style`: `diagram` (flat colors, labels with leader lines, every part
  clickable, focusable and named) or `stain` (a microscope look: pale pink field, purple-stained chromatin, soft
  edges). `phase` (for dividing cells): interphase, prophase, metaphase, anaphase, telophase, cytokinesis.
- `Phases`: the drawing parameters and one-line descriptions for each phase (used by CellView and Field).
- `Zoom(el, steps)`: a zoom ladder; each step has `name`, `caption`, `draw`; animated zoom between steps (Motion
  off: instant), keyboard step buttons, Esc to skip.
- `Membrane(el, {gates, outside, inside, seed, rate})`: the bilayer band, gate slots (`addGate(type, key)`,
  `open(type, bool)`), a token system with `step(dt)`, events `crossed(type, dir)` and `refused(type, reason)`,
  and transport rules (bilayer-permeable list, downhill-only channels and carriers, pump stoichiometry 3:2:1).
- `Field(el, {n, seed, mix, style})`: a microscope field of `n` cells laid out in files like a root tip, each cell
  given a phase from `mix` (fractions per phase) by seeded draw; returns the cell list with true phases; pan, zoom
  and a focus knob (blur) for the microscope feel; each cell focusable.
What each tool feeds it: cell-city feeds `CellView` diagram style (animal and plant), `Parts` with city analogies
and `Zoom` from organ systems down to organelles. mitosis-mixer feeds `Field`, `Phases` and `CellView` stain style
(onion root). membrane-gatekeeper feeds `Membrane` and `Zoom` (body down to the membrane of five cell kinds).

## Sources
- Ion concentrations inside and outside a typical mammalian cell: Alberts et al., Molecular Biology of the Cell,
  6th ed. (2015), Table 11-1 (checked 2026-10-27).
- Passive transport, osmosis and tonicity, facilitated diffusion, channel and carrier proteins, the Na+/K+ pump
  (3 Na+ out, 2 K+ in, 1 ATP): OpenStax Biology 2e, sections 5.2 and 5.3 (CC BY 4.0),
  https://openstax.org/books/biology-2e/pages/5-3-active-transport
- Aquaporins (Nobel Prize in Chemistry 2003, Peter Agre): https://www.nobelprize.org/prizes/chemistry/2003/summary/
- ADH inserts aquaporin-2 in the collecting duct: OpenStax Anatomy and Physiology 2e, section 25.6 (CC BY 4.0).
- Nerve signal from Na+ inflow then K+ outflow: OpenStax Biology 2e, section 35.2.
- CFTR, F508del as the most common cystic fibrosis variant, misfolding, CFTR modulators: NIH MedlinePlus Genetics,
  "CFTR gene" (https://medlineplus.gov/genetics/gene/cftr/) and NIH NHLBI, "Cystic Fibrosis: Treatment"
  (https://www.nhlbi.nih.gov/health/cystic-fibrosis/treatment) (checked as titles 2026-10-27).
- Pump share of resting ATP: Alberts et al. (2015), ch. 11 (verify confirms "about a third" or the tip is dropped).
- All meter scales, rates and level timings: game values, labeled as such.
- Number checks (Python, 2026-10-29, the water and glucose rules above stepped every 0.1 s over 90 s; balance time is
  seconds in the green band): level 1, gates always closed 75.2 s, always open 42.9 s, open only in normal plasma
  86.4 s, the same play 1 s late 76.3 s, 2 s late 62.0 s; level 2, carrier always closed 19.9 s, always open 66.8 s,
  open during meals until the meter reaches 75 then closed 90.0 s, open for whole meals 50.7 s (it overshoots the
  band). Fixed: the old level 1 told students to
  open water channels to stay in band, but in the model (and in real cells) an open channel during a wave moves the
  cell further out of band; the skill is now to close them during a wave and open them after. The water and glucose
  rules were missing and are now set. The ion levels (Alberts) are unchanged; the pump, nerve, kidney and airway
  timings stay builder-tuned with the scripted checks in Done when.

## Done when
1. In Lab, with every gate closed, only O2 and CO2 cross; opening the glucose carrier with less glucose outside
   moves glucose out, never in.
2. The pump stops when ATP is 0 and each cycle moves 3 Na+ out and 2 K+ in.
3. Level 1: a scripted player that opens the aquaporins only in normal plasma scores about 86 of 90; one that never
   opens them about 75; one that leaves them open about 43. Level 2: carrier open during meals until the meter reaches 75
   scores 90; open for whole meals about 51; always closed about 20.
4. Level 3 counts a signal only when Na+ opens first and K+ within 2 s.
5. Level 4 shows no aquaporins until the ADH token arrives.
6. Level 5 with F508del shows the empty CFTR slot, key 6 does nothing, mucus thickens, balance time is hidden, and
   the card is calm and factual.
7. Every gate works by keys 1 to 6 and by on-screen buttons; pause on blur; the zoom ladder skips with Esc.
8. Playable at 1366x768, 1000x625 and 680x425 without scrolling; touch buttons usable at 375 wide.
9. Each how-to line speaks once in five repeated actions; signal speaks each completed signal; no line names a key
   that does nothing at that moment.
10. Focus: the membrane band and meters are the largest thing on the stage in Levels and Lab, at 1366x768 and 680x425.
11. A tap while a level plays: a gate key pressed at any moment opens or closes the gate on the next frame, during the
    ramp to 4 tokens a second too; levels 3 to 5 each have a scripted player who scores at least 70 of 90 and an
    idle player who scores under 50 (Typical CFTR on level 5).
12. The 15 zoom pictures load in order; no network, no em dashes.

## Open questions
- [membrane-gatekeeper] The airway level names cystic fibrosis and the F508del variant (for HS-LS1-1: a gene change
  makes a protein that cannot do its job). Keep it, keep it but without the disease name, or drop the level?

# Curiosities: concepts for Cory's review

Started 2026-11-04. What a curiosity is, the qualities and the short test: docs/VISION.md, "Curiosities: the
second shape". This file holds the concepts, the look, the super tool pivots and the open choices.

**Status (2026-11-04).** Cory approved the overall concept and the look ("The look" below): both are locked. All
eight concepts go ahead. Span and Spire and Pocket Universe are pivoting first, through a Codex fix round
(tools/<id>/refine.md); Cipher Vault is held out of the Codex queue until its spec is revised. None of the new
concepts has a spec yet.

Each concept names the real thing it is, the first two minutes, where the depth comes from, the real material (with
its licence status), and where it sits on the map: the anchor module it fills and the other modules it reaches.

## Cory's first read (2026-11-04)

| Concept | Verdict | Next |
|---|---|---|
| Voice Lab | Fun | Ahead |
| Living Earth | Good foundation; needs more for the user to do | Boosted below ("Things to do") |
| Sky Dome | A bit simple, still fits | Ahead as is |
| Microscope Bench | Worried it feels like a regular tool; potential if done right | Reshaped below ("Things to do") |
| Circuit Bench | Caught Cory's eye: super cool to just play with | Ahead |
| Graph Studio | Graphing calculator days: fun | Ahead |
| Compass and Straightedge | Can't picture it yet; trust it and let it build out | Ahead, judged once built |
| Poet's Workbench | Hits for literary folks | Ahead |

## The concepts

### 1. Voice Lab (a live spectrogram)

- **The real thing:** the sound spectrogram that phoneticians, birders and audio engineers use.
- **First two minutes:** say "ahhh" and a glowing ribbon of your voice scrolls across the screen. Whistle and it
  becomes one thin line. Say "eee" then "ooo" and watch the bright bands jump.
- **Depth:** pitch versus loudness, harmonics, why vowels differ (formants), why a flute and a violin on the same
  note look different, freezing and measuring a moment, a tone generator to compare against.
- **Real material:** the student's own microphone, analysed live with Web Audio. Nothing is recorded or kept, and
  the mic prompt says so. No outside data.
- **Map:** anchor science-8-waves. Also reaches science-1-sound-and-vibration, science-4-waves-and-information,
  science-11-waves-and-sound, ela-k-rhymes-and-sounds (hearing and seeing the sounds in words), arts-k-2-instrument-families.
- **Watch:** a mic-free mode with built-in clips, for rooms where the mic is blocked.

### 2. Living Earth (a globe of real quakes and volcanoes)

- **The real thing:** a seismologist's map: every large earthquake since 1970 and the world's volcanoes on a globe
  that shows the sea floor.
- **First two minutes:** spin the globe and press play. Fifty years of quakes flash on in a few seconds, and the
  plate edges draw themselves out of the dots.
- **Depth:** depth slices (quakes dipping under Japan and the Andes), magnitude filters, the ocean floor's ridges
  and trenches, a cross-section drawn by dragging a line, one quake's story when tapped.
- **Real material:** USGS earthquake catalog (public domain), NOAA ETOPO relief (public domain), Natural Earth
  (public domain). Plate boundaries (Bird 2003) and the Smithsonian volcano list need their terms checked.
- **Map:** anchor science-6-plate-tectonics. Also reaches science-4-earth-s-features-on-maps,
  science-8-natural-hazards-and-human-impact, science-9-orbits-and-earth-s-history.
- **Things to do** (Cory asked for more, 2026-11-04). Each is something a seismologist really does:
  - **Find the quake.** Drop three seismometer stations anywhere; a real past quake strikes; each station's
    squiggle shows the P wave, then the S wave. Read the gap, draw a circle from each station, and the circles
    meet at the epicentre. Then reveal where it really was.
  - **Send a wave through the Earth.** Tap anywhere to start a quake and watch the P and S waves travel through
    the crust, mantle and core in a cut-away globe. S waves stop at the liquid core, leaving a shadow zone on the
    far side, which is how we learned the core is liquid.
  - **Slice the Earth.** Drag a line across a trench and the cross-section drops open: the quakes trace the
    sinking plate down hundreds of kilometres.
  - **Rewind the continents.** Drag time back 200 million years and the continents slide back into Pangaea, with
    the matching fossils and rock belts lighting up on both shores.
  - **Pin your town.** Drop a pin on any place and see its quake and volcano history around it, the nearest plate
    edge, and how fast that plate moves (a few centimetres a year, about how fast fingernails grow).
- **Watch:** the 2 MB budget (thin the catalog to magnitude 5 and up, about 600 KB packed); real disasters
  shown as data, without gore or casualty counts as spectacle. Plate reconstructions for Rewind need a licensed
  source (GPlates models are openly licensed; check which).

### 3. Sky Dome (a planetarium)

- **The real thing:** a planetarium: the real sky from any place on Earth at any time.
- **First two minutes:** the sky over the student's town tonight. Drag time forward and the stars wheel around the
  pole; the Moon changes shape as days pass.
- **Depth:** why the stars you see change by season, the Moon's phases and rise times, planets wandering against the
  stars, the sky from the South Pole or the equator, star colour and brightness, sky stories from several cultures.
- **Real material:** the Yale Bright Star Catalogue (about 9,000 naked-eye stars), planet positions from JPL's
  published orbital elements. Constellation lines and other cultures' sky stories need a licence check (many are
  share-alike).
- **Map:** anchor science-1-sun-moon-and-stars. Also reaches science-5-sun-stars-and-shadows,
  science-5-star-brightness, science-6-earth-sun-moon-system, science-9-stars-and-the-big-bang.
- **Watch:** Pocket Universe (gravity sandbox) is the neighbour. That one makes orbits; this one watches the sky.

### 4. Microscope Bench

- **The real thing:** a lab microscope with real slides.
- **First two minutes:** a drop of pond water, blurry. Turn the focus knob and it snaps sharp, and something swims.
- **Depth:** magnification steps (10x, 40x, 100x) that show different detail, stains that reveal parts, plant
  versus animal cells, cells dividing caught at each stage, a measuring scale on the eyepiece.
- **Real material:** real micrographs from public-domain collections (CDC Public Health Image Library, NIH, US
  government sources), checked image by image. Focus and depth are layered images, so the blur is honest.
- **Map:** anchor science-6-cells-and-body-systems. Also reaches science-9-cell-structure-and-function,
  science-9-cell-division-and-differentiation.
- **What keeps it from feeling like a regular tool** (Cory's worry, 2026-11-04). A regular tool shows picture 1,
  then picture 2, then asks a question. This one is a bench and a box of things to look at, and the student hunts:
  - **Make your own slide.** Pick from a tray: a drop of pond water, onion skin, a cheek swab, a hair, salt, sugar,
    sand, a leaf, a feather, a fly's wing. Add a stain or not, drop the cover slip. Every choice changes what you see.
  - **Scan the whole slide.** Each slide is a huge stitched image, far bigger than the eyepiece. Pan around it like
    a real stage, with the light and focus knobs working, and hunt: a rotifer hiding in the debris, one cell caught
    mid-division among hundreds.
  - **A sketchbook beside the eyepiece.** Sketch what you found, label it, note the magnification. The sketchbook
    keeps on this device and prints. That is what scientists actually did with microscopes for 300 years.
  - **No questions from the tool.** It never asks "What is this?". Tapping something you found names it only after
    you've zoomed in on it, like a field guide.
- **Watch:** finding enough public-domain images at matching magnifications, and big enough to stitch into a slide
  to scan; motion (swimming) may need short clips.

### 5. Circuit Bench

- **The real thing:** a breadboard bench with a meter: batteries, wires, bulbs, LEDs, switches, resistors, motors and
  a buzzer.
- **First two minutes:** drag a battery and a bulb onto the board, connect two wires, and the bulb glows. Add a
  second bulb and both dim.
- **Depth:** series versus parallel, the multimeter (probe any two points), a short circuit that heats the wire red,
  current shown as moving dots, magnets and a coil that make a motor turn.
- **Real material:** a real circuit solver (nodal analysis on Ohm's and Kirchhoff's laws), no outside data.
- **Map:** anchor science-8-electric-and-magnetic-forces. Also reaches science-3-magnets-and-static-electricity,
  science-11-electricity-and-magnetism, and grade 4 energy.
- **Watch:** our own look; it must not copy an existing circuit simulator.

### 6. Graph Studio

- **The real thing:** a graphing plotter: type any equation and see it.
- **First two minutes:** type y = x² and a curve appears. Change 2 to 3, then add a slider for a, and drag it.
- **Depth:** sliders on any letter, tables from any graph, points you can drag, families of curves, intersections,
  regressions on pasted data, polar and parametric for older students.
- **Real material:** the maths itself; nothing to source.
- **Map:** anchor math-9-function-notation-and-graphs. Also reaches math-8-defining-functions,
  math-8-modeling-with-functions, math-9-linear-quadratic-and-exponential-models, math-11-polynomial-functions,
  math-11-exponential-and-logarithmic-functions, math-11-trigonometric-functions, math-12-functions-and-their-graphs.
  About a dozen graphing lesson tools are planned in those modules; they stay, and each can open this one.
- **Watch:** must not copy any branded graphing calculator in name, look or layout (BASELINE rule 15).

### 7. Compass and Straightedge

- **The real thing:** the two tools Euclid allowed himself, on an endless sheet of paper.
- **First two minutes:** two clicks make a circle, two more make a second, and where they cross is the corner of a
  perfect equilateral triangle. That is Euclid's first proposition.
- **Depth:** bisect an angle, drop a perpendicular, copy a length, build a hexagon, a square, and try (and fail) to
  trisect an angle, with a note on why mathematicians proved it impossible.
- **Real material:** Euclid's Elements (Heath's 1908 translation, public domain) for the constructions and their
  wording.
- **Map:** anchor math-10-proofs-and-constructions. Also reaches math-7-scale-drawings-and-constructions,
  math-10-rigid-motions-and-congruence.
- **Watch:** close to the short test's edge: Euclid's propositions could turn into goals. Keep them as a book to
  browse, never a ladder.

### 8. Poet's Workbench

- **The real thing:** what a poet works with: syllables, stress and rhyme, shown as you write.
- **First two minutes:** type a line and each word lights up its beats: strong, weak, strong. Tap a word and its
  rhymes appear, close rhymes and slant rhymes apart.
- **Depth:** meter checking against iambic and other feet, syllable counts for haiku, a read-aloud of the line with
  the stress, famous public-domain lines to scan, rhyme schemes coloured down the page.
- **Real material:** the CMU Pronouncing Dictionary (134,000 words with stress; BSD-style licence).
- **Map:** anchor ela-7-sound-and-form-in-poetry. Also reaches ela-4-poetry-drama-and-prose,
  ela-k-rhymes-and-sounds.
- **Watch:** Poetry Soundboard (planned studio in the same module) is the neighbour; this may take its card or sit
  beside it.

## The look (approved by Cory, 2026-11-04)

**What makes the regular tools look familiar.** They share one frame (kit/curio.css): a slate header with the title on
the left and a row of pills on the right (modes, Motion, Sound, Read), the picture in the middle, a right-hand panel of
uppercase section labels and rounded pill buttons, and a hint bar along the bottom. City Skyline Studio, Span and Spire
and Pocket Universe all wear it. It is a good frame for lessons: a teacher who has used one tool can run any of them.

**What Beat Lab and Elements Inspector do instead.** Neither wears the frame. Beat Lab looks like a real production
studio: a transport bar, knobs, lit step pads and channel strips, dense and dark. Elements Inspector looks like a lab
instrument: a glowing atom in the middle, monospace readouts, data panels with thin rules, the whole periodic table
as a working surface. Each one borrows the visual language of the real tool it stands for. That is the rule.

**The rule: each curiosity looks like the real thing it is.** Not a photo of one, but its visual grammar:

| Curiosity | Its real grammar |
|---|---|
| Voice Lab | An audio analyser: black glass, a scrolling heat-map ribbon, a level meter, a frequency ruler down the side |
| Living Earth | A seismograph station: a slowly turning globe, drum traces scratching ink, a time dial, survey labels |
| Sky Dome | An observatory: a dark dome, a brass horizon ring, a date wheel and a lat-long setting circle |
| Microscope Bench | A lab bench: the round eyepiece view, coarse and fine focus knobs, a stage with a slide, a lamp dimmer |
| Circuit Bench | An electronics bench: a breadboard, components that look like parts, a multimeter with a needle or LCD |
| Graph Studio | A plotter: graph paper, a pen that draws the curve, an equation tape, sliders like a slide rule |
| Compass and Straightedge | A drafting table: cream paper, pencil lines that stay, a real compass that swings |
| Poet's Workbench | A writer's desk: a typewriter page, stress marks above the line like a printer's proof, a rhyme drawer |
| Span and Spire (pivot) | An engineer's test yard: blueprint paper, members glowing in stress colours, load gauges with needles |
| Pocket Universe (pivot) | Mission control: dark telemetry, orbit plots, a time dial in place of the speed pills |

**What makes them one family, not eight one-offs.** The family is in the grammar, never in one colour:

1. **The object is the stage.** It fills the screen. There is no right-hand pill panel; controls sit where the real
   ones would (knobs on the body, a tray of parts, a toolbelt).
2. **Real controls.** A small shared set, drawn for curiosities: knob, fader, toggle switch, lit pad, dial, needle
   gauge, readout. They turn and click with a small sound (with Sound on), move with a little weight, and each still
   works by keyboard.
3. **Readouts, not prose.** Live numbers with units in a monospace face, the way curiosities speak. Explanations live
   in a fold-out **Manual**, a drawer every curiosity has in the same place, written like a good field guide.
4. **A maker's plate.** Every curiosity carries the same small engraved nameplate in a corner: "Curio Class
   Curiosities · No. 07 · Circuit Bench". It is the family mark, and the numbers make them collectable.
5. **Each picks its own material.** Studio black, lab-glass cyan, blueprint blue, observatory brass, breadboard green,
   cream drafting paper. The palette comes from the real thing, so no two look alike.

**What does not change.** Everything in BASELINE still holds: keyboard play, contrast, reduced motion, the Read voice,
one offline file, school Chromebook speed. Motion, Sound and Read stay, gathered on the curiosity's own power panel
(styled like the curiosity) instead of the header pills.

**On the site.** The Curiosities shelf gets its own presentation: dark, like a cabinet of curiosities, each one shown
by its nameplate and a short live preview (the atom turning, the ribbon scrolling), not the regular tool card. In a
module the curiosity still sits in the normal list, with its nameplate as the badge.

**How it gets built.** The shared controls (knob, fader, dial, gauge, readout, nameplate, Manual drawer) become a small
curiosities kit, grown the usual way: from the first three curiosities that need it (rule 13). Span and Spire and
Pocket Universe, pivoted first, are where it starts.

## Pivoting the super tools (Cory, 2026-11-04)

Cory asked whether the five super tools (docs/agents/SUPER.md) could pivot into curiosities. Most can, because they
already share three of the qualities (the toy comes first, the concept is the mechanic, the model is honest). What
makes each one a game is its goal ladder, its sticker book, or a fixed order of rooms. The pivot is the same move
each time: **free play becomes the front door, the goals leave the frame, and the real material moves to the
centre.** Goals that teach something can stay as an optional book to browse, never a ladder to climb.

| Super tool | Where it stands | The curiosity it becomes | Size of the pivot |
|---|---|---|---|
| Span and Spire | Built and reviewed by Codex (12 Tags with budgets) | **Span and Spire, the engineer's yard.** Build any bridge or tower; choose your own truck, wind and shake; every member glows with its real force and the weakest buckles in slow motion. Budget becomes a dial you can turn on, not a gate. Tags become an optional logbook of tested designs. | Small: a Codex fix round with a pivot brief |
| Pocket Universe | Built and reviewed by Codex (goals and Wonders) | **Pocket Universe, a gravity sandbox.** Fling, rewind, scrub time; the real Solar System as a load. Goals leave the screen; Wonders stay as a book of famous setups to load and break. | Small: a Codex fix round |
| Cipher Vault | Spec only; held out of the Codex queue 2026-11-04 | **Cipher Workbench.** A codebreaker's bench: a frequency counter, a cipher wheel, a Vigenère square, a small rotor machine, all working on any message. Crack real historical messages or stump a partner. The six rooms become an optional case file to open in any order. | Medium: a spec revision before building |
| Molecule Forge | Spec only | **Molecule Forge.** Atoms snap only where real bonding allows; the discovery book stays, but as a field guide that names what you built, not a checklist to fill. | Small: a spec revision |
| Living Pond | Spec only | **Living Pond, an ecosystem tank.** Add and remove species, change the seasons and the light, and watch the populations and the graph respond over years. No goals; the winters and the heron are the drama. | Small: a spec revision |

Each passes the short test once pivoted. Span and Spire is the strongest: a real engineer's structural analysis
you can just play with, exactly like Circuit Bench. Cory approved pivoting both built ones (2026-11-04); their fix rounds are queued. If a fix round cannot carry the
whole pivot, the next step is a rebuild of the frame with a revised spec, keeping the engine.

**Pivot results (2026-11-05).** Both fix rounds finished overnight with every pivot item marked fixed (polish.md in
each tool). Span and Spire now has gauges, a blueprint grid, a truck tray and a material rack; Pocket Universe opens
on space with a mission-control console and a time dial. Two follow-ups are saved, not queued:

- **Plate wording.** Both plates read "Curio Class Instruments · No. 01/02". They change to "Curio Class Curiosities"
  in the next fix round for these two (a one-line change each).
- **A polish boost.** Cory wants these two to get more polish and is thinking it over (2026-11-05). Fold the plate
  wording into that round when Cory decides; do not queue either before then.

## The name (Cory, 2026-11-05)

These tools are **Curiosities** (one is a curiosity), and the shelf is the Curiosities shelf. "Instruments" was the
working name until 2026-11-05 and was dropped because it sounds musical. Older notes, refine lists and the two pivoted
tools' plates still say Instruments; read them as Curiosities.

## Idea: the home page picture becomes the way in (Cory, 2026-11-05; once there are more)

The picture at the top right of the home page (the subject logos) could be re-imagined as the door to the
Curiosities: a cabinet whose pieces are the curiosities themselves, each one opening its tool. Wait until the shelf
has enough pieces to fill it (Beat Lab, Elements Inspector, Span and Spire, Pocket Universe and a few of the new
concepts), then design it with Cory.

## Ideas for later (Cory, 2026-11-06; not on the roadmap yet)

Cory's vibe: a Curiosity somewhere between an old trail-journey game and a modern terraforming game. What the two
share is the material: time (months and years, small choices piling up), a ledger you can feel (supplies, miles,
oxygen, heat), and a place that changes because of you, with no finish line. Two directions go ahead, to flesh out
later; both may keep a little game essence (BASELINE rule 19).

### Second Growth (a field station)

A real damaged place recovers over decades and the student stewards it. Candidate sites: the Mount St. Helens
blast zone from 1980 on (40+ years of published plot surveys), a Dust Bowl farm, a burned forest, a reclaimed mine.
A time dial in years; plant, leave alone, pull invasives, bring back beavers, change the grazing; soil depth,
ground cover, species counts and water move on survey plots and a transect. The look: a field station bench with
quadrat frames, a transect tape, a soil core and a logbook, the landscape painting greening in stages behind it.
Reaches ecosystems, succession, human impact and data over time. Not like Living Pond (populations in a closed
tank): this is landscape succession and stewardship over decades.

### Atmosphere Console (a planetary model)

Pick Mars, Venus or early Earth and change greenhouse gases, albedo, water and pressure; temperature and pressure
respond over centuries with real physics, and the honest answer ("this takes ten thousand years") is part of the
wonder. Watch the overlap with Pocket Universe's mission-control look, and keep the model honest (a named source for
every constant, a readout that says what it leaves out).

### The Wrecking Yard (destruction Curiosities, Cory 2026-11-07)

Destruction is how engineers learn: every failure shows where the forces were going. These are curious and
satisfying, never crass: no people in them, crash test dummies stay abstract, slow-motion replay and force readouts
on every collapse, and the payoff is seeing why it failed. Each needs more polish and size than a first idea, and most
end in the same challenge: now build something that survives.

- **Load Path:** pull bricks or beams out of a building or bridge one at a time; stress colors shift through what is
  left until it gives. Could be a "demolition day" mode inside Span and Spire (No. 01) rather than a new tool.
- **Controlled Demolition:** plan the charge order so a tower falls into its own footprint; the wrong order tips it.
  Center of mass, sequencing, timing.
- **Earthquake Table:** build, then shake with real recorded quakes; compare a rigid frame, cross bracing, a tuned
  mass damper and base isolation. Then build one that stands.
- **Wrecking Ball:** pendulum energy into a wall; mass, height and swing angle against what breaks. Energy and
  momentum.
- **Catapult Range:** trebuchet and catapult against walls of different materials. Projectile motion, energy
  storage, the angle that reaches farthest.
- **Water Works (instead of erosion):** the power of moving water against buildings and shapes. A flume or wave tank
  where a flood or wave hits a flat wall, a wedge, a rounded pier, a house on stilts; force readouts follow the real
  drag relation (force grows with the square of speed), and a wedge splits the flow the way a bridge pier's cutwater
  or a ship's bow does. Then the challenge: design a building or barrier that withstands it.

Open: which is first, and whether Load Path lives inside Span and Spire.

### Open questions for the fleshing out

1. One real place done deeply, or a few sites (Second Growth) and planets (Atmosphere Console) to choose from?
2. Can a choice fail (a replanting that dies in drought) with no game-over?
3. Which light game touches earn their place under rule 19?

## Open choices for Cory

1. **Which concepts go ahead**, and in what order.
2. **Where the shelf lives on the site:** its own page under Browse, a band on the home page, or both.
3. **Where the label lives in the data:** a new column in data/tools-concepts.csv, or a short list
   (data/curiosities.csv: tool_id, anchor, also reaches).
4. **Which live tools already pass the short test** and join the shelf now: Beat Lab and Elements Inspector for
   sure, and the rest checked against the test.
5. **How they are built:** like super tools (one at a time, never in a wave, a third Refine round, a fresh-agent
   ten-minute check), or by the normal path.

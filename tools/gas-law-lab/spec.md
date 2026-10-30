# Gas Law Lab

## One idea
You find absolute zero yourself: warm and cool a gas under a piston, record its volume at a few temperatures, and
every straight line you fit, whatever the gas, the amount or the weight on the piston, crosses zero volume at the
same place, about −273 °C, where the particles you can watch bouncing inside would stop moving altogether.

## Not like
- particle-zoom (gr 5, particles, not specced): zooms into a balloon to show air is particles. Same engine; here the particles are measured (pressure, volume, temperature, energy) and the laws come out of the data.
- particle-party (gr 7, particles, not specced): heats particles through solid, liquid and gas. Same engine; here the gas never condenses (no attractions) and the point is P, V, T and n.
- equilibrium-seesaw (gr 10, same group): squeezes a syringe to shift a reaction. Here nothing reacts; the gas only changes its pressure, volume and temperature, and the apparatus is a weighted piston, a steel can and a balloon.
- hot-meets-cold (gr 11): energy flows between a hot and a cold object. Here the energy goes into one gas, and some of it lifts the piston's weights.
- which-model-wins (gr 9, math): picks the best model by hidden rows. Here the model (a line) is given by theory and the extrapolation past the data is the discovery.
- collision-lab (gr 11): momentum in glider collisions. Here the same wall bounces, counted by the thousand, are what a pressure gauge reads.

## Who and how
- Grade 10, Chemistry, Gases and Kinetic Theory. Students drive; pairs work well. 20 to 40 minutes.
- Topic line: "gas laws and particle motion".
- Standards (module): HS-PS3-2 (energy at the large scale is particle motion plus position: the energy bar, and the lifted weights on the piston).
- tool.json: driver "students", minutes "20-40", modes ["Bench", "Absolute zero"], grades_label "Grade 10".

## Screens and modes
Header: title, subtitle "Measure the gas. Find the law." Modes `Bench` (opens first), `Absolute zero`. Kit buttons.
Stage, left to right: the apparatus standing in the painted water bath (`gl-bath`, its water tinted in code from
cold to hot) with a code thermometer, over a dimmed painted lab (`gl-lab`); beside it a round particle window (a
magnifier circle drawn over the gas) where the particles engine runs. In Balloon the backdrop is the painted place
for the chosen altitude (Art) instead of the lab, and the balloon floats in the open air with a small code thermometer
beside it (the bath controls set the air temperature around it). Panel: apparatus picker, controls, readouts,
`Record`, hint. Below the stage (or beside it at 1366 wide): the Notebook (table plus graph). Under 900 px tall the
controls and readouts sit beside the apparatus and the Notebook becomes a tab `Notebook` next to `Readouts`.
Focus: in Bench and in Absolute zero steps 1 and 3, the apparatus and the particle window, central and largest; in
Absolute zero steps 2 and 4 the Notebook graph moves to the center of the stage (the apparatus shrinks to the side)
so the fitted line and its dashed run to zero volume are the biggest thing.

### Bench (explore)
Apparatus picker: `Piston`, `Can`, `Balloon`. Gas picker: `Helium`, `Nitrogen`, `Argon`.
- Piston: the painted glass cylinder (`gl-cylinder`, inside area 20.0 cm²) with the painted piston (`gl-piston`,
  frictionless and weightless in the model) that slides in code; painted weight blocks (`gl-weight`, "5 kg" printed
  in code) stack on top. `Add weight`, `Remove weight` (0 to 4 blocks of 5.00 kg). The piston settles where the gas pressure equals
  the atmosphere plus the weights, so volume changes.
- Can: the painted rigid 250 mL steel can with a pressure gauge (`gl-can`; the dial face is blank paint, the needle
  and numbers are code). Volume fixed; pressure changes. Amount 0.00100 to 0.0200 mol.
- Balloon: the painted rubber balloon tied shut (`gl-balloon`, scaled in code so its area follows V^(2/3)), holding
  a fixed 0.100 mol (inside pressure taken equal to the outside air; `Pump` and `Valve` are hidden). `Altitude`
  picker: `Sea level`, `1,600 m`, `3,000 m`, `5,000 m`, each with its painted backdrop.
Shared controls: bath slider `Bath` 0 to 100 °C (step 1) and buttons `Ice water 0 °C`, `Room 25 °C`,
`Hot water 80 °C`, `Boiling 100 °C`; `Pump` (+0.00100 mol) and `Valve` (−0.00100 mol) for Piston and Can, amount
0.00100 to 0.0100 mol on the Piston (Can as above). The gas temperature follows the bath over about 2 s (an exponential approach shown on the
thermometer; instant with Motion off). While it follows, every control stays live: a new bath, weight or `Record`
acts in the same frame (Record logs the values on screen at that moment).
Readouts: P (kPa), V (mL), T (°C and K), n (mol) and molecules (n × 6.022 × 10²³), average kinetic energy per
molecule (J), typical speed (rms, m/s), the live check "PV ÷ nT = 8.314" in the readout font, and in the particle
window "wall hits in the picture per second". Energy bar: "energy in particle motion" in joules and,
on the Piston, a second bar "weights lifted" (m g Δh since the last Record).
`Record` adds a Notebook row: apparatus, gas, n, T (°C), T (K), P, V. `Delete row`, `Clear notebook`. The Notebook
graph has axis pickers: x `T (°C)`, `T (K)`, `P`, `1/V`, `n`; y `V`, `P`, `P × V`. `Fit line` draws the least
squares line through the plotted rows and reports slope, intercept and where it crosses y = 0 ("crosses zero
at T = −273.2 °C"). The axis is extended left to −300 °C when x is T (°C) so the crossing is visible (dashed past
the data). Rows saved on this device (localStorage `curio-gas-law-lab`, try/catch).

### Absolute zero (guided)
Steps in the panel, each with its own hint:
1. Piston, no weights, 0.00400 mol. Record the volume at four or more bath temperatures (any, at least 60 °C apart
   end to end; the step's check names the gap if it is narrower).
2. Graph V against T (°C) and press `Fit line`. Read where your line meets zero volume.
3. Change one thing (gas, amount, or weights) and record a second set. Fit it. The second line has a different
   slope but meets zero at the same temperature.
4. Result card: both crossings, their mean, and the accepted value −273.15 °C, with "Kelvin starts here: 0 K".
`Real lab` toggle (on by default in this mode): each recorded volume has a seeded random reading error of up to
±0.1 percent of the reading and temperature ±0.2 °C, so crossings land within a few degrees of −273 °C (always
within 8 °C with four rows 60 °C apart, checked), as in a careful school lab. Off: exact readings.

## Content
Model: ideal gas, PV = nRT, R = 8.314462618 J/(mol·K), T(K) = T(°C) + 273.15, Avogadro constant
6.02214076 × 10²³ /mol, Boltzmann constant 1.380649 × 10⁻²³ J/K, g = 9.80665 m/s².
Gases (molar mass): helium 4.0026 g/mol, nitrogen 28.014 g/mol, argon 39.95 g/mol. rms speed = √(3RT/M):
helium 1,305 / 1,363 / 1,525 m/s at 0 / 25 / 100 °C; nitrogen 493 / 515 / 576; argon 413 / 431 / 483.
Average kinetic energy per molecule (3/2)kT, the same for every gas: 5.66 × 10⁻²¹ J at 0 °C, 6.17 × 10⁻²¹ J at
25 °C, 7.73 × 10⁻²¹ J at 100 °C. Energy in particle motion (moving from place to place): (3/2)nRT for every gas;
nitrogen molecules also tumble, so its bar adds a lighter segment to (5/2)nRT with the label "nitrogen also spins".
Piston: each weight adds 5.00 × 9.80665 / 0.00200 m² = 24.52 kPa. Atmosphere 101.325 kPa.
Check values (0.00400 mol): 0 weights: 89.66 mL at 0 °C, 97.86 at 25, 122.48 at 100. 1 weight (125.84 kPa): 72.19,
78.80, 98.62. 2 weights (150.36 kPa): 60.42, 65.95, 82.54. 4 weights (199.39 kPa): 45.56, 49.73, 62.24.
V against T (°C) at 1 atm: 0.00200 mol slope 0.16411 mL/°C; 0.00400 mol 0.32823; 0.00800 mol 0.65646; every line
crosses zero at −273.15 °C.
Can, 250 mL, 0.0100 mol: 90.84 kPa at 0 °C, 99.16 at 25 °C, 124.10 at 100 °C. The 200 kPa limit: 0.0160 mol at
100 °C reads 198.56 kPa (allowed); pumping to 0.0170 mol at 100 °C would read 210.97 (refused); 0.0170 mol at 25 °C
reads 168.57 and the bath then stops at 80 °C (199.67; 81 °C would read 200.23).
Balloon outside pressure (US Standard Atmosphere): sea level 101.33 kPa, 1,600 m 83.52, 3,000 m 70.11, 5,000 m
54.02. A balloon holding 0.100 mol at 25 °C: 2.45 L, 2.97 L, 3.54 L, 4.59 L.
Energy example (Piston, helium 0.00400 mol, 1 weight, 25 → 80 °C): volume 78.80 → 93.33 mL, piston rises 7.27 mm,
weights gain 0.356 J, total work pushing back the air and weights PΔV = 1.83 J, particle motion energy up 2.74 J,
so the bath supplied 4.57 J.

## Interactions in detail
- All numbers come from PV = nRT exactly; the particle window is a picture (2D, scaled) and never feeds a readout
  except its own "wall hits in the picture" count, which rises with T and n and falls with V as the real pressure
  does (the readout says "in the picture").
- Piston: P = 101.325 + 24.52 × weights kPa; V = nRT/P. Can: V = 250 mL; P = nRT/V. Balloon: P = outside; V = nRT/P.
- Limits: the piston cylinder is 300 mL tall; a state that needs more volume stops the piston at the top stop
  and the readout says "piston at the stop: pressure now rises instead" (then P = nRT/V with V = 300 mL). The can
  gauge is red-lined above 200 kPa ("past safe range"), and nothing may take it there: `Pump` refuses a step that
  would pass 200 kPa at the current temperature ("A real can could burst. The pump stops here."), and the bath
  slider and buttons stop at the last whole degree under 200 kPa with the same line. Valve below 0.00100 mol is refused.
- Fit line: ordinary least squares on the plotted rows (at least 2); x-intercept = −intercept / slope; with fewer
  than 2 rows `Fit line` is disabled with the hint "Record at least two rows". A vertical or flat set says "These
  rows don't make a sloped line."
- Real lab noise: seeded per page load (`__tool.seed(n)`), uniform in the ranges given (volume ±0.1 percent of the
  true value, temperature ±0.2 °C); shown values round to 0.01 mL, 0.1 °C, 0.01 kPa.
- Motion off: particle window shows a still frame with short speed arrows, refreshed every second; numbers update
  at once.
- Keyboard: every control is a button or slider; Notebook rows are a table with a delete button per row.
- `window.__tool = {state, setMode, set({apparatus, gas, n, T, weights, altitude, realLab}), record(), fit(xKey, yKey), seed(n)}`.

## Look
Accent `--brand #9ec9e8` (steel sky), `--brand-ink #10141a`. Bath water tint drawn in code over the painted tank,
`#1d4f6e` at 0 °C blending to `#6e2f2a` at 100 °C at 40 percent, with the temperature also printed; particles
helium `#ffd36b`, nitrogen `#7fb3ff`, argon `#d59cff`, each also drawn at its own size (helium smallest) so color
is not the only cue. Altitude backdrops sit under a `#0b0f17` wash at 35 percent so the balloon and readouts lead.
Labels and readouts sit on `--panel` chips, never straight on a painting. Contrast (computed): brand on panel
9.87:1, on --sec-bg 9.35:1, brand-ink on brand 10.53:1.

## Art
Local FLUX (`scripts/localart.py`), no people anywhere. 11 images. Particles, thermometer, gauge needle and numbers,
the bath tint, readouts, energy bars and the Notebook stay in code.
- gl-lab: a warm wooden physics lab bench before a pegboard wall hung with clamps, ring stands and coiled tubing; 16:9; cutout no; people no;
  Bench and Absolute zero backdrop for Piston and Can, dimmed.
- gl-bath: a tall rectangular glass water bath tank with a coiled steel heating element on the bottom, filled with
  clear water, on plain white; 4:3; cutout yes; people no; under the piston or can, tinted in code.
- gl-cylinder: a tall clear glass cylinder, open at the top, plain unmarked glass, on a round steel foot, on plain
  white; 9:16; cutout yes; people no; the piston's cylinder (graduation marks in code).
- gl-piston: a thick round grey piston disk with a dark rubber seal ring, seen from the side, on plain white; 4:1;
  cutout yes; people no; slides inside the cylinder in code.
- gl-weight: a single brass weight block with a plain flat face and a small handle on top, on plain white; 4:3;
  cutout yes; people no; drawn up to four times, stacked on the piston, "5 kg" in code.
- gl-can: a sturdy steel gas can with a round pressure gauge on top whose dial face is plain white and blank, on
  plain white; 3:4; cutout yes; people no; the Can apparatus, needle and numbers drawn in code.
- gl-balloon: a single round red rubber balloon tied shut with a short curl of string, on plain white; 3:4; cutout
  yes; people no; the Balloon, scaled in code with its volume.
- Altitude backdrops, one shared line, four images (16:9, cutout no, people no, Balloon mode backdrop for the picked
  altitude): gl-alt-sea: a sunny sandy beach at sea level with calm blue water. gl-alt-1600: a wide high plain with
  dry golden grass and a line of mountains on the horizon. gl-alt-3000: an alpine meadow with wildflowers below rocky
  peaks. gl-alt-5000: a bare snowy mountain ridge under a deep blue sky.

## Voice
Bank voice `bright-teacher` (Autonoe), restyled: "Say brightly and clearly, like an upbeat lab instructor who loves a
good measurement." Changed from `wise-mentor`, which orbit-lab (gr 9, a listed neighbor) uses; bright-teacher is the
only kept voice no tool `neighbors.py` lists for this one uses, and no other spec in this batch uses it.
`Curio.voice`, scope = mode.
- wBench (how; Bench welcome; stale once any control is used): "Pick an apparatus. Change the bath or the weights,
  then press Record to log a row."
- weightTip (how; the first weight added; stale once the piston settles): "More weight, more pressure. Watch the gas
  shrink until it pushes back equally."
- fitTip (how; the Notebook first holds two rows, so Fit line turns on; stale once Fit line is pressed): "Press Fit
  line to draw the best straight line through your rows."
- wZero (how; Absolute zero welcome; stale once the first row is recorded): "Record the volume at four bath
  temperatures, at least 60 degrees apart. Then fit a line and see where it meets zero."
- second (how; step 3 opens; stale once a second-set row is recorded): "Now change one thing: the gas, the amount or
  the weights. Record a second set and fit it."
- zero (event; a fit's crossing lands within 10 degrees of −273; stale when the rows change): "Your line meets zero
  near minus 273 degrees Celsius."
- stop (event; the piston reaches the stop; stale when it leaves): "The piston hit the stop. Now the pressure climbs
  instead."
- canStop (event; Pump or the bath is refused at the can's 200 kPa limit; stale on the next change): "A real can
  could burst. The gauge stops here."

## Family engine
particles (`kit/particles.js`, inlined after `kit:curio`). No family doc exists; this spec holds the full engine
description and the build writes `docs/families/particles.md` from it. Siblings: particle-zoom (gr 5, explorer),
particle-party (gr 7, simulator).
- `Box(canvas, {shape: 'rect' | 'circle', width, height, seed})`: a 2D hard-disk simulation drawn on a canvas.
- Species: `addSpecies({id, mass, radius, color, label})`; `add(id, count)`, `remove(id, count)`.
- Temperature: `setT(T)` sets the target; walls act as a heat bath (a particle hitting a wall leaves with a speed
  drawn from the 2D Maxwell distribution for the wall's temperature, blended by `bathCoupling` 0 to 1), so the
  gas warms or cools over a visible time. Speeds scale as √(T/m) in picture units.
- Walls: `setWall(side, {kind: 'rigid' | 'piston' | 'elastic', pos})`; a piston wall moves to `pos` smoothly;
  `hits(side)` returns impacts per second and summed momentum per second over the last second (the picture's
  pressure).
- Attractions: `attract` 0 to 1 (a short-range square well with depth scaled to it) so particle-party gets
  clumping, liquid and solid; 0 here.
- Mixing: `zones` let particle-zoom start a sugar cluster in water particles and watch it spread; `dissolve(id)`
  frees clustered particles at a rate.
- Readouts: `meanKE()`, `speedHist(bins)`, `count(id)`, `frame()` for tests.
- Motion off: `still()` draws the frame with speed arrows and advances one simulated second per redraw.
- Fixed real-world numbers never come from the picture: each tool computes its readouts from its own model (here
  PV = nRT) and labels picture counts "in the picture".
- What each sibling feeds it: particle-zoom: zones, dissolving, a balloon wall (elastic). particle-party: attractions,
  heating at a steady rate, a temperature graph with plateaus. This tool: three walls (piston, rigid, elastic), three
  gases by mass, hit counting.

## Sources
- HS-PS3-2: NGSS Lead States (2013), Next Generation Science Standards, HS-PS3 Energy, https://www.nextgenscience.org/
- Gas laws, ideal gas law, extrapolation to absolute zero: OpenStax, Chemistry 2e, 9.2 "Relating Pressure, Volume, Amount, and Temperature: The Ideal Gas Law", https://openstax.org/books/chemistry-2e/pages/9-2-relating-pressure-volume-amount-and-temperature-the-ideal-gas-law
- Kinetic-molecular theory, average kinetic energy (3/2)kT, rms speed √(3RT/M): OpenStax, Chemistry 2e, 9.5 "The Kinetic-Molecular Theory", https://openstax.org/books/chemistry-2e/pages/9-5-the-kinetic-molecular-theory
- Gas constant, Avogadro constant, Boltzmann constant, standard gravity: NIST CODATA 2018 values, https://physics.nist.gov/cuu/Constants/ (R = 8.314462618 J/(mol·K), exact; NA and k exact; g = 9.80665 m/s², conventional)
- Molar masses He, N2, Ar: PubChem compound pages, https://pubchem.ncbi.nlm.nih.gov/ (He 4.0026, N2 28.014, Ar 39.95; checked 2026-10-27)
- Diatomic gases store energy in rotation too ((5/2)nRT at room temperature): OpenStax, University Physics Volume 2, 2.4 "Distribution of Molecular Speeds" and 3.5 "Heat Capacities of an Ideal Gas", https://openstax.org/books/university-physics-volume-2/pages/3-5-heat-capacities-of-an-ideal-gas
- Pressure with altitude: U.S. Standard Atmosphere, 1976 (NOAA, NASA, USAF), troposphere formula P = 101.325(1 − 2.25577 × 10⁻⁵ h)^5.25588 kPa, https://ntrs.nasa.gov/citations/19770009539
- Every check value recomputed in Python (2026-10-27) from the constants above.
- Number checks (Python, 2026-10-29, CODATA constants): rms speeds, (3/2)kT, the piston table (24.52 kPa a weight),
  the three V against T slopes, can pressures, altitude pressures and balloon volumes, and the energy example (78.80
  to 93.33 mL, 7.27 mm, 0.356 J, PΔV 1.83 J, 2.74 J, 4.57 J) all recomputed and match. The piston reaches its 300 mL
  stop only above 92.4 °C at 0.0100 mol with no weights. Found and fixed: with the old 0.0100 mol top amount the can
  could never pass 200 kPa (at most 124.1), so its safe-range stop could not fire; the can now holds up to 0.0200
  mol and both Pump and the bath stop at 200 kPa (numbers in Content). The old Real lab noise (±0.3 mL, rows 40 °C
  apart) put crossings as far as 77 °C off at small amounts or heavy weights (median 15 °C at 0.00100 mol), so "within
  a few degrees" and the 10 °C zero line failed; noise is now ±0.1 percent of the volume with rows 60 °C apart, and
  pushing every row's error to its limit in every sign pattern, over a dozen row layouts 60 °C apart (evenly spaced,
  bunched at the ends, 0 to 60 and 40 to 100), keeps the crossing within 7.6 °C of −273.15 (95 percent of random runs
  within 2.7 °C), whatever the gas, amount or weights.

## Done when
1. Piston, helium, 0.00400 mol, no weights: 97.86 mL at 25 °C, 122.48 mL at 100 °C; PV ÷ nT reads 8.314 in both.
2. Adding one weight at 25 °C gives 125.84 kPa and 78.80 mL; nitrogen in place of helium changes the speed readout
   (515 vs 1,363 m/s) but not P or V.
3. Can, 0.0100 mol: 90.84 kPa at 0 °C and 124.10 at 100 °C; at 0.0170 mol the bath stops at 80 °C and Pump at
   100 °C is refused, each with the canStop line.
4. Balloon with 0.100 mol at 25 °C: 2.45 L at sea level and 4.59 L at 5,000 m, each over its own painted backdrop.
5. Absolute zero with Real lab off: four rows from 0 to 100 °C fit to a crossing of −273.15 °C (shown −273.2); a
   second set at 0.00800 mol has twice the slope and the same crossing.
6. With Real lab on (any seed), four rows 60 °C apart cross within 8 °C of −273 and the zero line plays; Fit line is
   disabled with one row.
7. Piston heated 25 → 80 °C with one weight shows the weights bar at 0.356 J and the piston up 7.27 mm.
8. Focus: in Bench the apparatus and particle window are the largest thing at 1366x768 and in the 680x425 preview;
   in Absolute zero step 2 the graph is.
9. A tap while the gas warms: pressing `Record` mid-approach logs the on-screen values at once; a new bath button
   restarts the approach from the current temperature in the same frame.
10. How-to lines once each per page load; zero, stop and canStop each time; no line names Fit line while it is
    disabled.
11. Every size in STANDARDS.md keeps the bath controls, weights, Record and readouts visible; keyboard-only play
    works; Motion off freezes the particles but not the numbers; all 11 images load and none shows a person; console
    clean, no network, no em dashes.

## Open questions
- The module's only code is HS-PS3-2; the gas laws themselves have no NGSS performance expectation. This tool teaches them anyway as the route to HS-PS3-2. Fine, or should a state standard (many states keep gas laws) be named?

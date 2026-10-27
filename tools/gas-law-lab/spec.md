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
Stage, left to right: the apparatus in a water bath with a thermometer; beside it a round particle window (a
magnifier circle drawn over the gas) where the particles engine runs. Panel: apparatus picker, controls, readouts,
`Record`, hint. Below the stage (or beside it at 1366 wide): the Notebook (table plus graph). Under 900 px tall the
controls and readouts sit beside the apparatus and the Notebook becomes a tab `Notebook` next to `Readouts`.

### Bench (explore)
Apparatus picker: `Piston`, `Can`, `Balloon`. Gas picker: `Helium`, `Nitrogen`, `Argon`.
- Piston: a glass cylinder (inside area 20.0 cm²) with a frictionless, weightless piston; weight blocks stack on
  top. `Add weight`, `Remove weight` (0 to 4 blocks of 5.00 kg). The piston settles where the gas pressure equals
  the atmosphere plus the weights, so volume changes.
- Can: a rigid 250 mL steel can with a pressure gauge. Volume fixed; pressure changes.
- Balloon: a rubber balloon tied shut (inside pressure taken equal to the outside air). `Altitude` picker:
  `Sea level`, `1,600 m`, `3,000 m`, `5,000 m`.
Shared controls: bath slider `Bath` 0 to 100 °C (step 1) and buttons `Ice water 0 °C`, `Room 25 °C`,
`Hot water 80 °C`, `Boiling 100 °C`; `Pump` (+0.00100 mol) and `Valve` (−0.00100 mol) for Piston and Can, amount
0.00100 to 0.0100 mol. The gas temperature follows the bath over about 2 s (an exponential approach shown on the
thermometer; instant with Motion off).
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
1. Piston, no weights, 0.00400 mol. Record the volume at four or more bath temperatures (any, at least 40 °C apart
   end to end).
2. Graph V against T (°C) and press `Fit line`. Read where your line meets zero volume.
3. Change one thing (gas, amount, or weights) and record a second set. Fit it. The second line has a different
   slope but meets zero at the same temperature.
4. Result card: both crossings, their mean, and the accepted value −273.15 °C, with "Kelvin starts here: 0 K".
`Real lab` toggle (on by default in this mode): each recorded volume has a seeded random reading error of up to
±0.3 mL and temperature ±0.2 °C, so crossings land within a few degrees, as in a school lab. Off: exact readings.

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
Can, 250 mL, 0.0100 mol: 90.84 kPa at 0 °C, 99.16 at 25 °C, 124.10 at 100 °C.
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
  shows a red-lined gauge above 200 kPa with the word "past safe range" and the pump refuses beyond it ("A real can
  could burst. The pump stops here."). Valve below 0.00100 mol is refused.
- Fit line: ordinary least squares on the plotted rows (at least 2); x-intercept = −intercept / slope; with fewer
  than 2 rows `Fit line` is disabled with the hint "Record at least two rows". A vertical or flat set says "These
  rows don't make a sloped line."
- Real lab noise: seeded per page load (`__tool.seed(n)`), uniform in the ranges given; shown values round to
  0.1 mL, 0.1 °C, 0.01 kPa.
- Motion off: particle window shows a still frame with short speed arrows, refreshed every second; numbers update
  at once.
- Keyboard: every control is a button or slider; Notebook rows are a table with a delete button per row.
- `window.__tool = {state, setMode, set({apparatus, gas, n, T, weights, altitude, realLab}), record(), fit(xKey, yKey), seed(n)}`.

## Look
Accent `--brand #9ec9e8` (steel sky), `--brand-ink #10141a`. Bath water `#1d4f6e` at 0 °C blending to `#6e2f2a` at
100 °C with the temperature also printed; glass `#cfe3f1` at 25 percent opacity; brass weights `#b8913f` with "5 kg"
printed; steel can `#8a96a3`; particles helium `#ffd36b`, nitrogen `#7fb3ff`, argon `#d59cff`, each also drawn at
its own size (helium smallest) so color is not the only cue. Contrast (computed): brand on panel 9.87:1, on --sec-bg
9.35:1, brand-ink on brand 10.53:1.

## Art
none: drawn in code (apparatus, bath, particles, preview.svg).

## Voice
Bank voice `wise-mentor` (thoughtful high school mentor). No 9-12 science neighbor uses it. `Curio.voice`, scope = mode.
- wBench (how, Bench welcome): "Pick an apparatus. Change the bath or the weights, then press Record to log a row."
- weightTip (how, first weight added): "More weight, more pressure. Watch the gas shrink until it pushes back equally."
- fitTip (how, first time the graph has two rows): "Press Fit line to draw the best straight line through your rows."
- wZero (how, Absolute zero welcome): "Record the volume at four bath temperatures. Then fit a line and see where it meets zero."
- second (how, step 3 opens): "Now change one thing: the gas, the amount or the weights. Record a second set and fit it."
- zero (event, a fit's crossing lands within 10 degrees of −273; stale when the rows change): "Your line meets zero near minus 273 degrees Celsius."
- stop (event, piston reaches the stop; stale when it leaves): "The piston hit the stop. Now the pressure climbs instead."

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

## Done when
1. Piston, helium, 0.00400 mol, no weights: 97.86 mL at 25 °C, 122.48 mL at 100 °C; PV ÷ nT reads 8.314 in both.
2. Adding one weight at 25 °C gives 125.84 kPa and 78.80 mL; nitrogen in place of helium changes the speed readout (515 vs 1,363 m/s) but not P or V.
3. Can, 0.0100 mol: 90.84 kPa at 0 °C and 124.10 at 100 °C; the pump refuses above 200 kPa with the "past safe range" line.
4. Balloon with 0.100 mol at 25 °C: 2.45 L at sea level and 4.59 L at 5,000 m.
5. Absolute zero with Real lab off: four rows from 0 to 100 °C fit to a crossing of −273.15 °C (shown −273.2); a second set at 0.00800 mol has twice the slope and the same crossing.
6. With Real lab on, the crossing lands within 10 °C of −273 and the zero line plays; Fit line is disabled with one row.
7. Piston heated 25 → 80 °C with one weight shows the weights bar at 0.356 J and the piston up 7.27 mm.
8. Every size in STANDARDS.md keeps the bath controls, weights, Record and readouts visible; keyboard-only play works; Motion off freezes the particles but not the numbers; console clean, no network.

## Open questions
- The module's only code is HS-PS3-2; the gas laws themselves have no NGSS performance expectation. This tool teaches them anyway as the route to HS-PS3-2. Fine, or should a state standard (many states keep gas laws) be named?

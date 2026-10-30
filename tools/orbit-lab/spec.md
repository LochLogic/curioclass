# Orbit Lab

## One idea
Launch a planet sideways from 1 AU at any speed around a star of any mass and watch gravity draw the ellipse: the
star sits at one focus, equal times sweep equal areas, and every launch drops a point on a P² against a³ plot that
lands on the same line as the eight real planets.

## Not like
- cone-slicer, now Conic Focus Finder (gr 12 math, wave 2): ellipses drawn with strings and pins, the geometry of foci.
  Here nothing draws the ellipse but gravity; the empty second focus and the speed changes are the physics.
- launch-pad (gr 9 math, wave 1) and flight-planner (wave 2): parabolas and vectors near the ground. Here orbits
  around a star, energy decides the size, and some launches never come back.
- field-lines (gr 11): the inverse square field drawn as lines. Here the field's consequence: orbit shapes and periods.
- moon-phase-model (gr 6, built, astronomy): Sun, Earth and Moon geometry and phases. Here Kepler's laws with numbers.
- star-life-story (this group, astronomy family): stars over their whole lives. Here one star's grip on its planets;
  the two tools share the astronomy engine.
- size-of-everything (built): scale from atoms to galaxies. Here one solar system at a working scale.

## Who and how
Grade 9, Earth and space science (Orbits and Earth's History). Students drive, 25 to 40 minutes. Explore first:
Launch opens with Earth's launch ready.
Standards: HS-ESS1-4, HS-ESS1-5, HS-ESS1-6.
tool.json: driver "students", minutes "25-40", modes ["Launch", "Planets", "Rock Clock"].

## Screens and modes
Header (kit, 9-12 theme): "Orbit Lab", small line "Gravity draws the ellipse." Modes `Launch`, `Planets`,
`Rock Clock`; kit `Motion`, `Sound`, `Read`.

### Launch (explore, default)
Focus: the orbit in the space view. The space view is the biggest, central thing (about two thirds of the stage
width wide, full width stacked); the Kepler plot sits small under the panel's readouts, not under the stage.
Stage: the space view (engine `SpaceView`) over the painted starfield, the painted star glow at the centre (tinted by
`starColor` for the star mass), a scale bar in AU, and the planet at 1 AU to the right as a painted planet cutout
(picked by planet mass, see Content) with a launch arrow in code. Panel: Launch speed (5 to 50 km/s, step 0.01,
default 29.78), Launch angle from the radius (30 to 150 degrees, default 90, sideways), Star mass (0.5 to 2.0 solar
masses, step 0.1, default 1.0), Planet mass (0.1 to 300 Earth masses, default 1.0). Buttons `Launch` (Space),
`Pause`, `Reset` (R), speed `x1`, `x10`, `x100`.
- Before a launch and while sliders move, a dashed preview of the orbit the current settings will give is drawn at
  once (analytic), so a slider change shows its effect immediately even mid-run.
- The orbit trail draws as the planet moves; when the trail closes, the ellipse is outlined, its two foci marked
  (star at one, a small empty ring at the other), and readouts fill: a (AU), e, perihelion, aphelion (AU), period
  (days or years), speed now (km/s).
- `Equal areas` toggle: shades the area swept in each twelfth of the period, alternating two tints; each wedge shows
  its area in square AU (all equal to 3 decimals). It shows at once, mid-run too, on the current orbit.
- Escape: a launch at or above escape speed draws an open path and the readout says "Escaped: not bound to the star.
  Speed far away: 15.83 km/s".
- Presets row: `Earth` (29.78), `Slow` (20), `Fast` (35), `Very fast` (40), `Escape` (45).
- Every bound launch adds a point to the Kepler plot: P² (yr²) against a³ (AU³), one line per star mass (slope 1/M),
  the eight planets as fixed grey dots.

### Planets
Focus: the log-log plot of P against a, large in the stage, with the line P = a^1.5 and each planet shown on it as
its small painted portrait (28 px, a ring in the accent on hover and focus). Click a planet (on the plot or in the
table): the panel shows its larger portrait (96 px) and a stage inset draws its real orbit to scale (Pluto included
as a dwarf planet, marked). Panel: the table from NASA (Content) with columns planet, distance a (million km and AU),
period (days and years), e, P² / a³. `Show ellipse shape` toggles the inset orbit drawn true to its e (most look like
circles; Mercury and Pluto show their offsets). Question strip: "Which planet's P² / a³ is furthest from 1? Why
might that be?" with `Show me` (rounding in published values; Neptune 0.975).

### Rock Clock
For the Earth half of the module. Two benches, picked with `Seafloor` and `First rocks`.
- Seafloor. Focus: the ocean cross-section. A code diagram (it is a data map: distances, symmetric magnetic stripes
  as a drawn pattern, a ridge in the middle) fills the stage, with code water above and the painted drill ship
  cutout on the surface. Click the seafloor to drill: the ship slides to that point (400 ms; Motion off instant) and
  a core comes up as the painted core cutout in a core tray card, labeled in code with its distance from the ridge
  and its age from the lab's rate. A plot of age against distance fills in the panel; `Fit` draws the line and
  reports the spreading rate. Strip: "Oldest seafloor about 180 million years. Why is the seafloor so young when
  continents hold rocks over 4 billion years old?" with `Show me` (subduction recycles old seafloor; continents float
  and stay).
- First rocks. Focus: the time line with the cards. Five evidence cards (Content), each with a painted picture and its
  text in code, sit in a tray; students drag each card to its age on an engine `deepTime` line from 4.6 billion years
  ago to now (linear). `Check` passes a card when the cards are in the right order and the card's pin is within 0.25
  billion years of its age, and explains the rest. A side panel compares a painted Moon surface and a painted Earth
  surface: the Moon keeps craters because it has no plates, wind or rain to wipe them (the Moon craters card).

## Content
Units: AU, years and solar masses, with GM = 4π² for one solar mass. Escape speed at 1 AU is √2 times the circular
speed. Circular speed at 1 AU around 1 solar mass: 29.785 km/s; escape 42.122 km/s.

Launch check values (launch at 1 AU, 1 solar mass, 90 degrees unless stated):
| Speed (km/s) | a (AU) | e | perihelion / aphelion (AU) | Period |
|---|---|---|---|---|
| 20 | 0.6455 | 0.5491 | 0.2911 / 1 | 189.4 days |
| 25 | 0.7719 | 0.2955 | 0.5438 / 1 | 247.7 days |
| 29.78 | 0.9997 | 0.0003 | 0.9994 / 1 | 365.1 days |
| 35 | 1.6151 | 0.3809 | 1 / 2.2303 | 2.053 years |
| 40 | 5.091 | 0.8036 | 1 / 9.18 | 11.49 years |
| 45 | escapes | | | speed far away 15.83 km/s |
Star mass 2.0 at 29.785 km/s: a 0.6667, e 0.5, period 140.6 days. Circular speed for 2.0 solar masses 42.122 km/s,
period 0.7071 years; for 0.5 solar masses 21.061 km/s, period 1.4142 years. 60 degree launch at 29.78 km/s: a 0.9997,
e 0.5, period 365.1 days (same energy, same period, different shape). At 20 km/s the planet speeds up to 68.71 km/s
at perihelion (angular momentum: 20 × 1 / 0.29107). Planet mass changes nothing (the planet is far lighter than the
star; the model leaves out the star's own wobble).

Planet picture by planet mass (looks only; the orbit ignores it): under 0.5 Earth masses Mars, 0.5 to under 5 Earth,
5 to under 50 Neptune, 50 and over Jupiter.

Screen time: `x1` plays one year in 5 seconds, `x10` in 0.5 s, `x100` in 0.05 s. If the first orbit would take more
than 15 s at the chosen speed, the run steps up to the next speed that closes it in 15 s or less and says so ("Sped
up to x10 to close the orbit"). Periods over 300 years cannot close in 15 s even at x100: their ellipse and
readouts show at once, and the planet keeps moving at x100.

Planets (NASA Planetary Fact Sheet, updated 18 March 2025): distance from Sun (million km), orbital period (days), e:
Mercury 57.9, 88.0, 0.206; Venus 108.2, 224.7, 0.007; Earth 149.6, 365.2, 0.017; Mars 228.0, 687.0, 0.094; Jupiter
778.5, 4331, 0.049; Saturn 1432.0, 10747, 0.052; Uranus 2867.0, 30589, 0.047; Neptune 4515.0, 59800, 0.010; Pluto
(dwarf planet) 5906.4, 90560, 0.244. P² / a³ with 1 AU = 149.5978707 million km: 1.0012, 1.0003, 0.9997, 0.9993,
0.9977, 0.9871, 0.9964, 0.9750, 0.9988. Earth: perihelion 147.1, aphelion 152.1 million km, speeds 30.29 and 29.29
km/s by the vis-viva equation.

Seafloor bench: full spreading rate 2.5 cm per year (about the Mid-Atlantic Ridge), so each side moves 1.25 cm per
year. Age = distance from the ridge / 1.25 cm per year: 250 km, 20 million years; 500 km, 40; 1000 km, 80; 1500 km,
120; 2250 km, 180 (the basin edge). Oldest seafloor about 180 million years. Stripes drawn as a symmetric pattern
(not a real map). Model note: one steady rate; real rates vary by ridge and through time.

First rocks cards (age, what it tells us); the first five go on the time line, the sixth is the Moon and Earth panel:
- Meteorite calcium-aluminum inclusions, 4.567 billion years: the Solar System's first solids.
- Oldest Moon zircons, at least 4.51 billion years: the Moon formed early, likely from a giant impact.
- Jack Hills zircon (Western Australia), 4.404 billion years: crust, and likely liquid water, very early.
- Acasta Gneiss (Canada), about 4.03 billion years: oldest known intact rock.
- Oldest seafloor, about 180 million years: plates recycle oceans.
- Moon craters: the Moon's surface keeps a record Earth's surface erased.

## Interactions in detail
- Orbits use the engine's analytic Kepler solver (elements from the launch state, Kepler's equation by Newton's method,
  hyperbolic branch for escape), so orbits close exactly and periods are exact; frames sample the solution.
- Launch speed under 5 km/s is refused ("falls into the star"); a path whose perihelion is under 0.01 AU shows "grazes
  the star: the model ignores collisions" and still draws (5 km/s at 30 degrees around 2.0 solar masses reaches
  0.0018 AU).
- Edges near escape speed: for star mass 0.5 the escape speed at 1 AU is 29.785 km/s (21.061 × √2), so 29.78 km/s
  stays bound (aphelion 3,173 AU, period 89,425 years) and 29.79 escapes ("0.56 km/s far away"); 42.12 km/s around
  1.0 solar mass stays bound with aphelion 10,996 AU and period 407,751 years. Any orbit with a period over 1,000
  years reads "bound, but the trip takes ... years" and the view stops following after 60 AU.
- Every control stays live during a run: a slider change redraws the dashed preview at once; `Launch` relaunches
  from the start point with the new settings and the old trail fades; speed buttons, `Pause`, `Equal areas` and
  `Reset` act on the next frame.
- Wedge areas: computed from the solved positions with the exact ellipse sector formula (area swept from the focus
  between eccentric anomalies E1 and E2 = ab/2 × ((E2 − E1) − e (sin E2 − sin E1))) and printed to 3 decimals. A
  200-sample shoelace sum was tried and disagreed in the third decimal for 606 of 5,885 test orbits, so do not use it.
- Very large orbits (aphelion over 40 AU) zoom the view out with the scale bar updating; mouse wheel and pinch zoom,
  drag pans, `Fit` recentres. The starfield stays fixed behind the view.
- Rock Clock drill: clicks snap to 50 km; the core at the ridge (0 km) reads "0 to 2 million years: brand new".
- First rocks: cards drag by pointer or keyboard; each card shows a pin at its bottom edge that marks its age; a card
  checked right locks with its age printed. Clear returns all cards to the tray.
- Sound: a soft tone whose pitch follows the planet's speed (higher near the star), a click per wedge; off with Sound.
- Keyboard: Space = Launch, R = Reset, arrows on focused sliders; Tab reaches cards in Rock Clock with Enter to pick
  up and arrow keys to move along the time line.
- Layout by real stage pixels: wide, compact, stack (at 375 wide the Kepler plot moves under the readouts).
- Mode change: `Curio.stop()`, `V.hush()`. Kepler plot points and placed cards per device (localStorage
  `curio-orbit-lab`, try/catch), `Clear`.

## Look
Accent (`--brand`) #a9c4ff, periwinkle starlight: 9.91:1 on --panel #141b25, 9.39:1 on --sec-bg #18202b; --brand-ink
#10161f on it 10.40:1. Clear of field-lines #e8b54a and Conic Focus Finder #8ff0ff; star-life-story uses violet
#b894d0.
Scene: the painted starfield dimmed under a #0b0f17 wash at 40 percent so orbits read; the painted star glow tinted
by `starColor` (1.0 solar mass about #fff4ea), orbit trail in the accent, dashed preview in #c8d2e0, empty focus ring
#c8d2e0, equal-area wedges `--gr-1` and `--gr-2` at 35 percent. Rock Clock: seafloor #2e3b4c, magnetic stripes
#5a6f8a and #8aa1bf, new crust #c9714a at the ridge, water #12263a; painted cards in a 1 px #c8d2e0 frame.

## Art
Local FLUX (`scripts/localart.py`), no people anywhere. 20 images.
- ol-sky: a deep black night sky full of faint scattered stars of many sizes, a few soft blue and amber ones, a thin
  pale wisp of the Milky Way across one corner; 16:9; cutout no; people no; fixed background of the space view.
- ol-star-glow: a single small blazing white star with a soft round glow and four thin faint light rays, centered on
  pure black; 1:1; cutout no (drawn with screen blend so the black drops out); people no; the star at the centre,
  tinted by `starColor`, size by star mass.
- ol-mercury: the planet Mercury, a gray cratered sphere lit from the left, full disk centered on pure black; 1:1;
  cutout yes; people no; Planets marker and portrait.
- ol-venus: the planet Venus, a pale yellow sphere wrapped in smooth cream clouds, lit from the left, full disk on
  pure black; 1:1; cutout yes; people no; Planets.
- ol-earth: the planet Earth from space, blue oceans, white cloud swirls and brown and green land, lit from the left,
  full disk on pure black; 1:1; cutout yes; people no; Planets and the Launch planet.
- ol-mars: the planet Mars, a rusty red sphere with dark patches and a white polar cap, lit from the left, full disk
  on pure black; 1:1; cutout yes; people no; Planets and the Launch planet.
- ol-jupiter: the planet Jupiter, a banded tan and cream sphere with a red oval storm, lit from the left, full disk on
  pure black; 1:1; cutout yes; people no; Planets and the Launch planet.
- ol-saturn: the planet Saturn, a pale gold banded sphere with wide flat tilted rings, lit from the left, on pure
  black; 16:9; cutout yes; people no; Planets.
- ol-uranus: the planet Uranus, a smooth pale cyan sphere with a faint thin upright ring, lit from the left, full disk
  on pure black; 1:1; cutout yes; people no; Planets.
- ol-neptune: the planet Neptune, a deep blue sphere with a dark oval spot and thin white cloud streaks, lit from the
  left, full disk on pure black; 1:1; cutout yes; people no; Planets and the Launch planet.
- ol-pluto: the dwarf planet Pluto, a tan and cream sphere with a pale heart-shaped plain, lit from the left, full
  disk on pure black; 1:1; cutout yes; people no; Planets.
- ol-drill-ship: an ocean drilling ship with a tall steel derrick in the middle of its long deck, side view from a
  distance, on calm open sea; 16:9; cutout yes; people no; Seafloor, moves along the surface to the drill point.
- ol-core: a long split cylinder of dark gray basalt rock core lying in a shallow core tray, top view, studio light;
  4:1; cutout yes; people no; the core card in Seafloor.
- ol-cai: a polished slice of a dark gray meteorite speckled with bright white irregular grains, macro photo; 4:3;
  cutout no; people no; first card.
- ol-moon-zircon: a tiny clear honey-colored crystal grain on a fragment of pale gray Moon rock, macro photo; 4:3;
  cutout no; people no; second card.
- ol-jack-hills: a tiny pink-brown zircon crystal seen through a microscope, sharp faces, dark background; 4:3;
  cutout no; people no; third card.
- ol-acasta: a weathered outcrop of banded gray and white gneiss rock beside a cold northern lake; 4:3; cutout no;
  people no; fourth card.
- ol-pillow-basalt: rounded black pillow-shaped lava rocks on the deep seafloor lit by a single lamp; 4:3; cutout no;
  people no; fifth card.
- ol-moon-surface: the gray surface of the Moon seen from above, crowded with overlapping round craters of every
  size; 4:3; cutout no; people no; the Moon side of the comparison panel and the Moon craters card.
- ol-earth-surface: green rolling hills, forest and winding rivers seen from high above, a wide shallow ring-shaped
  lake left by an ancient crater; 4:3; cutout no; people no; the Earth side of the comparison panel.
Drawn in code: orbits, foci, wedges, launch arrow, preview, plots, table, the seafloor cross-section and stripes, the
time line, card text, preview.svg.

## Voice
Bank `wise-mentor` (an old astronomer at the telescope on a viewing night): thoughtful, warm, unhurried. Changed from
`upbeat-guide`, which protein-factory in this group also uses; the math neighbors launch-pad and flight-planner use
firm-captain and star-life-story uses smooth-narrator. `Curio.voice`, `scope: () => state.mode`.
- launch (how; Launch welcome; stale once Launch is pressed): "Drag Launch speed, then press Launch. Gravity does the
  drawing."
- areas (how; the first orbit that closes; stale when Equal areas is turned on): "Turn on Equal areas. Each slice
  takes the same time and holds the same area."
- escape (event; each escape launch; stale on Reset or the next Launch): "That one is free. It never comes back."
- longTrip (event; each launch with a period over 300 years; stale on the next Launch): "Bound, but this trip takes
  too long to watch. The ellipse is drawn for you."
- planets (how; Planets welcome; stale once a planet is clicked): "These are the real planets. Click one on the plot
  and check how close it sits to the line."
- rocks (how; Rock Clock welcome on the Seafloor bench; stale after the first core): "Click the seafloor to drill a
  core. Then press First rocks to build the timeline."
- cards (how; First rocks opened; stale once a card is placed): "Drag each card to its age on the line, then press
  Check."
- placed (event; every First rocks card placed right on Check; stale on Clear): "Every card is in place."

## Family engine
Family astronomy (this tool and star-life-story). No engine doc yet; keep it in one marked block,
`/* ASTRONOMY ENGINE: begin */ ... /* ASTRONOMY ENGINE: end */`, as `const Astro = (() => { ... })()` with no DOM
access except inside the two view helpers, so it can move to `kit/astronomy.js`. Full description:
- Constants: `GM_SUN` 1.32712440018e20 m³/s², `AU` 1.495978707e11 m, `YR` 365.25 days, `C` 299792458 m/s, `L_SUN`
  3.828e26 W, `M_SUN` 1.989e30 kg, `T_SUN` 5772 K. Units helper `fmt(value, kind)` for km/s, AU, light years and
  years ("4.6 billion years").
- `orbitFromState(r, v, angleDeg, mSun)` → `{bound, a, e, peri, aph, P, h, energy, vInf}` in AU, years, km/s.
- `positionAt(orbit, t)` → `{x, y, speed, E}` (elliptic: Kepler's equation M = E − e sin E by Newton, tolerance
  1e-12; hyperbolic: M = e sinh H − H).
- `sweptArea(orbit, t1, t2)` → area in AU² by the exact sector formula from the two solved positions.
- `deepTime(svgEl, {from, to, log})`: a scrubber and card line over deep time, linear or log, with labeled ticks (used
  by Rock Clock here and by star-life-story's life lines, which run from days to 200 billion years).
- `SpaceView(el, opts)`: pan and zoom canvas with a scale bar in km, AU or light years, an optional fixed background
  image, and image sprites (with optional tint and screen blend); methods `draw(items)`, `fit()`.
- `starColor(T)` → hex from a blackbody approximation (2000 to 50000 K), used for stars in both tools.
- star-life-story feeds it star tracks (mass, phases, durations) and uses `deepTime`, `SpaceView` and `starColor`;
  this tool feeds it launch states and planets.

## Sources
- Planet distances, periods and eccentricities; Earth perihelion and aphelion: NASA Goddard, Planetary Fact Sheet
  (updated 18 March 2025), https://nssdc.gsfc.nasa.gov/planetary/factsheet/ (read 2026-10-27).
- GM of the Sun, astronomical unit: IAU 2012 Resolution B2 (AU) and IAU 2015 nominal values; JPL, "Astrodynamic
  Parameters", https://ssd.jpl.nasa.gov/astro_par.html
- Kepler's laws and the vis-viva equation: OpenStax, University Physics Volume 1, 13.5 "Kepler's Laws of Planetary
  Motion", https://openstax.org/books/university-physics-volume-1/pages/13-5-keplers-laws-of-planetary-motion
- Seafloor spreading (about 2.5 cm per year at the Mid-Atlantic Ridge), oldest seafloor about 180 million years: USGS,
  "This Dynamic Earth", https://pubs.usgs.gov/gip/dynamic/
- Meteorite inclusions 4.567 billion years: Connelly et al. 2012, Science 338:651. Moon zircons at least 4.51 billion
  years: Barboni et al. 2017, Science Advances 3:e1602365. Jack Hills zircon 4.404 billion years: Wilde et al. 2001,
  Nature 409:175. Acasta Gneiss about 4.03 billion years: Bowring and Williams 1999, Contributions to Mineralogy and
  Petrology 134:3.
- Solar luminosity 3.828e26 W and temperature 5772 K: IAU 2015 Resolution B3.
- Number checks (Python, 2026-10-29, vis-viva with the constants above): every row of the launch table matched;
  perihelion speed at 20 km/s is 68.71 km/s (was printed 68.70, fixed); 45 km/s gives 15.835 km/s far away; 0.5 solar
  masses at 29.78 gives aphelion 3,173.4 AU and 89,425 years, at 29.79 escapes at 0.562 km/s; 42.12 around 1.0 gives
  10,996 AU and 407,751 years; 60 degrees gives e 0.5000; worst corner 5 km/s, 30 degrees, 2.0 solar masses gives
  perihelion 0.0018 AU. Screen times at x1: 20 km/s 2.6 s, Earth 5.0 s, 35 km/s 10.3 s, 40 km/s 57 s (auto x10, 5.7
  s); 42 km/s period 805 years (shown at once). Equal areas: 200-sample shoelace disagreed at 3 decimals for 606 of
  5,885 orbits (speeds 5 to 44.5, five angles, masses 0.5 to 2.0), so the exact sector formula is used; on the 20
  km/s orbit every wedge is 0.0912 AU² (prints 0.091). Planet P²/a³ values and Earth's 30.29 and 29.29 km/s
  recomputed and matched. First rocks: on a 600 px line 0.25 billion years is 33 px; Moon zircons and Jack Hills sit
  0.106 billion years (14 px) apart, which is why Check also needs the right order.

## Done when
1. Default launch (29.78 km/s) closes in 365.1 days with e 0.0003 and a 0.9997 AU, in about 5 s at x1.
2. 20 km/s gives a 0.6455, e 0.5491, perihelion 0.2911 AU, 189.4 days, speed 68.71 km/s at perihelion.
3. 35 km/s gives aphelion 2.2303 AU and 2.053 years; 40 km/s steps up to x10 and closes in under 15 s; 45 km/s
   escapes with "15.83 km/s".
4. Star mass 2.0 at 29.785 km/s gives a 0.6667, e 0.5, 140.6 days; planet mass 300 gives the same orbit as 1 (only
   the picture changes to Jupiter).
5. Equal areas on the 20 km/s orbit shows twelve wedges each reading 0.091.
6. Every bound launch lands on its star mass's line in the Kepler plot; the planets table shows Neptune 0.9750; the
   nine planet portraits sit on the Planets plot.
7. Rock Clock: a core at 1000 km reads 80 million years; `Fit` reports 1.25 cm per year per side.
8. First rocks: the five cards placed in order within 0.25 billion years pass and "Every card is in place." plays;
   swapping Moon zircons and Jack Hills fails even when both are within 0.25.
9. Focus: the space view is the largest thing in Launch at 1366x768 and 680x425; the plot is the largest thing in
   Planets.
10. A tap while the planet moves: dragging Launch speed redraws the dashed preview in the same frame; Equal areas
    shows at once; Pause stops the next frame.
11. How-to lines once each; "That one is free." on each escape; no line names a control that is not on screen.
12. Space view, plot and panel visible at 1366x768; stacked at 760 and 375 wide; labels at least 10 px in the
    680x425 preview; all 20 images load, none shows a person; no network, no em dashes.

## Open questions
- [orbit-lab] HS-ESS1-5 and HS-ESS1-6 (plate ages, Earth's early history) live in the Rock Clock mode of an orbit
  tool, because the module joins them. Is that an honest home, or should they move to their own tool later?
- [orbit-lab] Voice moved from upbeat-guide to wise-mentor because protein-factory (same group) uses upbeat-guide.
  OK?

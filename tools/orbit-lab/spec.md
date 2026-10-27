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
Stage: a dark sky view (engine `SpaceView`) with the star at the centre, a scale bar in AU, and a planet at 1 AU to
the right with a launch arrow. Panel: Launch speed (5 to 50 km/s, step 0.01, default 29.78), Launch angle from the
radius (30 to 150 degrees, default 90, sideways), Star mass (0.5 to 2.0 solar masses, step 0.1, default 1.0), Planet
mass (0.1 to 300 Earth masses, default 1.0). Buttons `Launch` (Space), `Pause`, `Reset` (R), speed `x1`, `x10`, `x100`.
- The orbit trail draws as the planet moves; after one full orbit the ellipse is outlined, its two foci marked (star
  at one, a small empty ring at the other), and readouts fill: a (AU), e, perihelion, aphelion (AU), period (days or
  years), speed now (km/s).
- `Equal areas` toggle: shades the area swept in each twelfth of the period, alternating two tints; each wedge shows
  its area in square AU (all equal to 3 decimals).
- Escape: a launch at or above escape speed draws an open path and the readout says "Escaped: not bound to the star.
  Speed far away: 15.83 km/s".
- Presets row: `Earth` (29.78), `Slow` (20), `Fast` (35), `Very fast` (40), `Escape` (45).
- Every bound launch adds a point to the Kepler plot under the stage: P² (yr²) against a³ (AU³), one line per star
  mass (slope 1/M), the eight planets as fixed grey dots.

### Planets
Table from NASA (Content) with columns: planet, distance a (million km and AU), period (days and years), e, P² / a³.
Below, the log-log plot of P against a with the line P = a^1.5 and each planet a labeled dot. Click a planet to draw
its real orbit to scale in the stage (Pluto included as a dwarf planet, marked). `Show ellipse shape` toggles each
orbit drawn true to its e (most look like circles; Mercury and Pluto show their offsets). Question strip: "Which
planet's P² / a³ is furthest from 1? Why might that be?" with `Show me` (rounding in published values; Neptune
0.975).

### Rock Clock
For the Earth half of the module. Two benches, picked with `Seafloor` and `First rocks`.
- Seafloor: a cross-section of an ocean basin with a ridge in the middle, symmetric magnetic stripes (drawn pattern),
  and a drill. Click the seafloor to drill a core: the core reports its distance from the ridge and its age from the
  lab's rate. A plot of age against distance fills; `Fit` draws the line and reports the spreading rate. Strip:
  "Oldest seafloor about 180 million years. Why is the seafloor so young when continents hold rocks over 4 billion
  years old?" with `Show me` (subduction recycles old seafloor; continents float and stay).
- First rocks: evidence cards (Content) on an engine `deepTime` line from 4.6 billion years ago to now. Students drag
  each card to its age; `Check` snaps cards within 2 percent and explains the rest. A panel compares a Moon surface
  and an Earth surface: the Moon keeps craters because it has no plates, wind or rain to wipe them.

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
e 0.5, period 365.1 days (same energy, same period, different shape). At 20 km/s the planet speeds up to 68.70 km/s
at perihelion (angular momentum: 20 × 1 / 0.2911). Planet mass changes nothing (the planet is far lighter than the
star; the model leaves out the star's own wobble).

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

First rocks cards (age, what it tells us):
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
  the star: the model ignores collisions" and still draws.
- Edges near escape speed: for star mass 0.5 the escape speed at 1 AU is 29.785 km/s (21.061 × √2), so 29.78 km/s
  stays bound (aphelion 3,173 AU, period 89,425 years) and 29.79 escapes ("0.56 km/s far away"); 42.12 km/s around
  1.0 solar mass stays bound with aphelion 10,996 AU and period 407,751 years. Any orbit with a period over 1,000
  years reads "bound, but the trip takes ... years" and the view stops following after 60 AU.
- Changing a slider mid-orbit relaunches from the start point on `Launch`; the old trail fades.
- Wedge areas: computed from the solved positions (shoelace over 200 samples per wedge) and printed to 3 decimals.
- Very large orbits (aphelion over 40 AU) zoom the view out with the scale bar updating; mouse wheel and pinch zoom,
  drag pans, `Fit` recentres.
- Rock Clock drill: clicks snap to 50 km; a core within 20 km of the ridge reads "0 to 2 million years: brand new".
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
Scene: deep space #0b0f17 with faint stars #3a4458, the star drawn in its blackbody color (engine `starColor`; 1.0
solar mass about #fff4ea), orbit trail in the accent, empty focus ring #c8d2e0, equal-area wedges `--gr-1` and `--gr-2`
at 35 percent. Rock Clock: seafloor #2e3b4c, magnetic stripes #5a6f8a and #8aa1bf, new crust #c9714a at the ridge.

## Art
none: drawn in code (space view, star, orbits, plots, seafloor, cards, preview.svg).

## Voice
`upbeat-guide` (Zephyr), style "Say brightly and clearly, like a planetarium show host." No group sibling uses it; shared in 9-12
science only with protein-factory (gr 9 biology).
`Curio.voice`, `scope: () => state.mode`.
- launch (how, Launch welcome): "Pick a speed and press Launch. Gravity does the drawing."
- areas (how, first full orbit): "Turn on Equal areas. Each slice takes the same time and holds the same area."
- escape (event, an escape launch; stale on Reset): "That one is free. It never comes back."
- planets (how, Planets welcome): "These are the real planets. Check how close each one sits to the line."
- rocks (how, Rock Clock welcome): "Drill the seafloor, then build the timeline of Earth's first rocks."
- placed (event, all First rocks cards placed right; stale on Clear): "Every card is in place."

## Family engine
Family astronomy (this tool and star-life-story). No engine doc yet; keep it in one marked block,
`/* ASTRONOMY ENGINE: begin */ ... /* ASTRONOMY ENGINE: end */`, as `const Astro = (() => { ... })()` with no DOM
access except inside the two view helpers, so it can move to `kit/astronomy.js`. Full description:
- Constants: `GM_SUN` 1.32712440018e20 m³/s², `AU` 1.495978707e11 m, `YR` 365.25 days, `C` 299792458 m/s, `L_SUN`
  3.828e26 W, `M_SUN` 1.989e30 kg, `T_SUN` 5772 K. Units helper `fmt(value, kind)` for km/s, AU, light years and
  years ("4.6 billion years").
- `orbitFromState(r, v, angleDeg, mSun)` → `{bound, a, e, peri, aph, P, h, energy, vInf}` in AU, years, km/s.
- `positionAt(orbit, t)` → `{x, y, speed}` (elliptic: Kepler's equation M = E − e sin E by Newton, tolerance 1e-12;
  hyperbolic: M = e sinh H − H).
- `sweptArea(orbit, t1, t2)` → area in AU².
- `deepTime(svgEl, {from, to, log})`: a scrubber and card line over deep time, linear or log, with labeled ticks (used
  by Rock Clock here and by star-life-story's life lines, which run from days to 200 billion years).
- `SpaceView(el, opts)`: pan and zoom canvas with a scale bar in km, AU or light years; methods `draw(items)`, `fit()`.
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
- Every launch value computed in Python (2026-10-27).

## Done when
1. Default launch (29.78 km/s) closes in 365.1 days with e 0.0003 and a 0.9997 AU.
2. 20 km/s gives a 0.6455, e 0.5491, perihelion 0.2911 AU, 189.4 days, speed 68.70 km/s at perihelion.
3. 35 km/s gives aphelion 2.2303 AU and 2.053 years; 45 km/s escapes with "15.83 km/s".
4. Star mass 2.0 at 29.785 km/s gives a 0.6667, e 0.5, 140.6 days; planet mass 300 gives the same orbit as 1.
5. Equal areas on the 20 km/s orbit shows twelve wedges with equal areas to 3 decimals.
6. Every bound launch lands on its star mass's line in the Kepler plot; the planets table shows Neptune 0.9750.
7. Rock Clock: a core at 1000 km reads 80 million years; `Fit` reports 1.25 cm per year per side.
8. First rocks: all six cards placed snap and "Every card is in place." plays once.
9. How-to lines once each per mode welcome; "That one is free." on each escape.
10. Space view, plot and panel visible at 1366x768; stacked at 760 and 375 wide; labels at least 10 px in the 680x425
    preview; no network, no images, no em dashes.

## Open questions
- [orbit-lab] HS-ESS1-5 and HS-ESS1-6 (plate ages, Earth's early history) live in the Rock Clock mode of an orbit
  tool, because the module joins them. Is that an honest home, or should they move to their own tool later?

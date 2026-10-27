# Star Life Story

## One idea
Pick a star's mass and scrub its whole life on one time line from millions to hundreds of billions of years; a cutaway
core shows which elements are being forged right now, and when the star dies its new elements fly out as chips that
land on a periodic table of where everything in your body came from.

## Not like
- orbit-lab (this group, astronomy family): one star's gravity on its planets. Here the star itself, birth to death;
  the two share the astronomy engine.
- elements-inspector (built, elements family): each element's facts and its emission spectrum. Here where elements
  are made, not what they look like.
- spectrum-explorer (this group): the electromagnetic spectrum in technology and the body. Here starlight is only the
  star's color and brightness.
- half-life-dice (gr 10 chemistry): radioactive decay of nuclei. Here fusion builds nuclei up.
- size-of-everything (built) and moon-phase-model (gr 6, built): scale and Moon geometry. Here time, mass and fate.

## Who and how
Grade 9, Earth and space science (Stars and the Big Bang). Students drive, 25 to 40 minutes. Explore first: Life
Line opens with the Sun's life ready to scrub.
Standards: HS-ESS1-1, HS-ESS1-2, HS-ESS1-3.
tool.json: driver "students", minutes "25-40", modes ["Life Line", "Sun", "Origins"].

## Screens and modes
Header (kit, 9-12 theme): "Star Life Story", small line "Mass decides everything." Modes `Life Line`, `Sun`,
`Origins`; kit `Motion`, `Sound`, `Read`.

### Life Line (explore, default)
Stage, top: the star drawn at its current color (engine `starColor`) and relative size, beside a cutaway of its core
as an onion of shells, each shell labeled with what it fuses ("hydrogen to helium"). Stage, bottom: the engine
`deepTime` line on a log scale from 1 day to 1 trillion years with the star's phases as colored bands; a scrubber and
`Play` (Space) run through the life with the log scale so short phases get room. A marker "age of the universe 13.8
billion years" sits on the line.
- Mass picker: seven star cards (Content) from 0.4 to 40 solar masses plus a 20 solar mass card with full detail. The
  current card's numbers fill the side panel: mass, surface temperature, main sequence life, fate.
- Phase readout under the scrubber: phase name, how long it lasts, what the core fuses, what the star looks like.
- At the end of a life, `Death` plays: a planetary nebula drifting off a white dwarf, or a supernova flash leaving a
  neutron star or black hole. New element chips (Content) fly to a mini periodic table in the corner.
- `Compare` pins the current life line and draws the next one under it, so two masses share the scale.
- `Arrange` (optional): shuffled phase cards for the Sun or for the 20 solar mass star; drag them into order, `Check`.

### Sun
For HS-ESS1-1, a cross-section of the Sun with three labeled zones (core, radiative zone, convective zone) and a
counter that runs while the mode is open: "Since you opened this, the Sun has turned ... tonnes of mass into energy."
Panel cards: fusion in the core (four hydrogen nuclei become one helium nucleus; 0.7 percent of the mass becomes
energy); the power (3.828 × 10^26 watts, so 4.26 million tonnes a second); the trip (light leaves the surface and
reaches Earth in 499 seconds, about 8.3 minutes); the long view (lost so far in 4.57 billion years: about 0.03 percent
of the Sun's mass). `Sun's future` jumps to Life Line with the Sun card at "now".

### Origins
For HS-ESS1-2 and the element half of HS-ESS1-3. Two panels picked with `Big Bang evidence` and `Periodic table of
origins`.
- Big Bang evidence: three cards, each with a small plot drawn in code. Redshift: farther galaxies move away faster
  (a line through drawn points with "about 70 km/s for every megaparsec"). Cosmic microwave background: a blackbody
  curve at 2.7255 K peaking near 1.06 mm. Light elements: a bar showing about 75 percent hydrogen and 25 percent helium
  by mass. A slider runs the universe's expansion backward to show why all three point to a hot, dense start 13.787
  billion years ago.
- Periodic table of origins: the full table, each element tinted by its main sources (Content); click an element for
  a line ("Most of your calcium came from exploding massive stars"). `My body` filter highlights the eleven elements
  that make up most of the human body.

## Content
Main sequence stars (OpenStax Astronomy 2e, Table 22.1; spectral type, mass, surface temperature, life on the main
sequence):
| Card | Type | Mass (solar) | Surface temp (K) | Main sequence life | Fate |
|---|---|---|---|---|---|
| Blue giant | O5 | 40 | 54,000 | 1 million years | black hole likely (models differ) |
| Blue-white | B0 | 16 | 29,200 | 10 million years | neutron star |
| White | A0 | 3.3 | 9,600 | 500 million years | white dwarf |
| Yellow-white | F0 | 1.7 | 7,350 | 2.7 billion years | white dwarf |
| Sun-like | G0 | 1.1 | 6,050 | 9 billion years | white dwarf |
| Orange | K0 | 0.8 | 5,240 | 14 billion years | white dwarf (none yet) |
| Red dwarf | M0 | 0.4 | 3,750 | 200 billion years | white dwarf (none yet) |
Cards K0 and M0 note: "Its life is longer than the universe's age so far: no star this light has died yet."
Fates: stars that start under about 8 solar masses end as white dwarfs; up to about 20 to 25 solar masses usually as
neutron stars; above that often black holes (Heger et al. 2003, for stars like the Sun's makeup; limits uncertain).

The Sun (Sackmann, Boothroyd and Kraemer 1993): main sequence about 11 billion years, then 0.7 billion years swelling
toward a red giant, 0.6 billion years climbing the red giant branch (up to about 2,300 times today's brightness and 170
times today's radius), 0.1 billion years fusing helium in the core, then a short giant phase, a planetary nebula and a
white dwarf. Age now 4.57 billion years (oldest meteorite solids), so about 6.4 billion years of main sequence left.
The textbook table rounds a 1 solar mass life to 10 billion years; the panel says both.

The 20 solar mass star (Heger et al. 2003, Table 1), core stage, products, duration:
hydrogen to helium, 8.1 million years; helium to carbon and oxygen, 1.2 million years; carbon to neon and magnesium,
980 years; neon to oxygen and magnesium, 0.60 years (219 days); oxygen to silicon and sulfur, 1.3 years; silicon to
iron, 0.031 years (11 days). Then the iron core collapses in under a second and the star explodes as a supernova,
leaving a neutron star. Iron is the end because fusing iron takes energy instead of giving it.

Element chips at death: low mass stars (planetary nebula) carbon, nitrogen and slow-capture elements (barium, lead);
massive stars (supernova) oxygen, neon, magnesium, silicon, sulfur, calcium, iron.

Periodic table of origins (main sources, Johnson 2019; shares not shown as numbers): Big Bang (hydrogen, helium, some
lithium); cosmic ray splitting (lithium, beryllium, boron); dying low mass stars (carbon, nitrogen, many heavy elements
by slow neutron capture such as barium, lead); exploding massive stars (oxygen, neon, magnesium, silicon, sulfur,
calcium, and part of the iron); exploding white dwarfs (much of the iron and nickel); merging neutron stars (gold,
platinum, europium, uranium by fast neutron capture); made by people (technetium and the heaviest elements).
`My body` elements: oxygen, carbon, hydrogen, nitrogen, calcium, phosphorus, potassium, sulfur, sodium, chlorine,
magnesium.

Sun numbers: luminosity 3.828 × 10^26 W; mass to energy L / c² = 4.26 × 10^9 kg per second; over 4.57 billion years
about 6.1 × 10^26 kg, 0.03 percent of 1.989 × 10^30 kg. Light from 1 AU: 1.496 × 10^11 m / 299,792,458 m/s = 499 s.

Big Bang numbers: age 13.787 ± 0.020 billion years; background temperature 2.7255 K, peak wavelength 2.898 mm·K /
2.7255 K = 1.06 mm; Hubble constant shown as "about 70" (measurements range from 67 to 73 km/s per megaparsec).

## Interactions in detail
- Life lines come from the Content tables only; stages not in a source (for the five plain cards after the main
  sequence) show one band labeled "later stages, short" with no invented durations.
- Scrubbing is continuous; the onion and star redraw at each phase boundary; `Play` spends equal screen time per
  decade of the log scale (about 1.2 s per factor of 10; Motion off jumps phase to phase).
- `Compare`: at most two lines; a third replaces the older pinned one.
- Arrange: Sun cards (main sequence, swelling, red giant, helium core, giant again, planetary nebula, white dwarf);
  20 solar mass cards (hydrogen, helium, carbon, neon, oxygen, silicon, collapse, supernova, neutron star). Wrong
  places shake once and stay; `Show order` after two checks.
- Sun counter: tonnes = 4.26 × 10^6 × seconds open, with thousands separators; pauses when the tab is hidden.
- Sound: a low hum whose pitch drops as stars swell; a soft boom at a supernova; off with Sound.
- Keyboard: Space = Play, arrows move the scrubber one phase, Tab reaches cards and table cells (Enter opens a cell).
- Layout by real stage pixels: wide (star and onion side by side), compact, stack (375 wide: onion under the star,
  the time line full width).
- Mode change: `Curio.stop()`, `V.hush()`. Arrange results per device (localStorage `curio-star-life-story`,
  try/catch), `Clear`.

## Look
Accent (`--brand`) #b894d0, nebula violet: 6.75:1 on --panel #141b25, 6.39:1 on --sec-bg #18202b; --brand-ink
#10161f on it 7.08:1. Moved off a pale orchid that sat close to mitosis-mixer's #f1b1ed; clear of orbit-lab's
periwinkle #a9c4ff (ΔE 25); nearest 9-12 accents dance-styles #c9b3ff (ΔE 14) and mitosis-mixer (16).
Scene: space #0b0f17, stars by `starColor`, onion shells hydrogen #6f8fd8, helium #e0c060, carbon #8a8a8a, oxygen and
neon #6fc7b0, silicon #c08a5a, iron #b04a3a, nebula gas #f5b3ff at 30 percent and #6fd0d8 at 20 percent. Time bands
use `--gr-1` to `--gr-4`. Element source tints use six colors from the kit's chart set with a text label in each cell.

## Art
none: drawn in code (stars, onion, nebulas, supernova, time line, periodic table, plots, preview.svg).

## Voice
`smooth-narrator` (Algieba), style "Say smoothly and warmly, like an audiobook narrator telling a long story." No
9-12 science tool uses it. `Curio.voice`, `scope: () => state.mode`.
- life (how, Life Line welcome): "Pick a star and drag along its life. The core shows what it is building now."
- death (event, a death plays; stale on a new card): "The new elements are free. Watch where they land."
- iron (event, the 20 solar mass core reaches iron; stale on a new card): "Iron. Fusing it takes energy, so the core collapses."
- sun (how, Sun welcome): "Every second, the Sun turns millions of tonnes of mass into light."
- origins (how, Origins welcome): "Three clues point back to one hot start. Then click any element to see who made it."

## Family engine
Family astronomy, engine described in full in orbit-lab's spec (`/* ASTRONOMY ENGINE: begin */ ... end */`, `const
Astro`). This tool uses `deepTime` (log, 1 day to 10^12 years) for life lines, `SpaceView` for the star and nebula
scenes, `starColor(T)` for star colors, `fmt` for durations, and the constants `L_SUN`, `M_SUN`, `C`, `AU`. It feeds the
engine star tracks: `{mass, type, tempK, phases: [{name, years, core, look}], fate}` from Content.

## Sources
- Main sequence masses, temperatures and lifetimes: OpenStax, Astronomy 2e (2022), Table 22.1,
  https://openstax.org/books/astronomy-2e/pages/22-1-evolution-from-the-main-sequence-to-red-giants
- The Sun's future stages: Sackmann, Boothroyd and Kraemer 1993, "Our Sun. III. Present and Future", ApJ 418:457,
  https://www.cita.utoronto.ca/~boothroy/sun3.html
- 20 solar mass burning stages and the fate limits: Heger, Woosley, Fryer and Langer 2003, "How Massive Single Stars
  End Their Life", ApJ 591:288, https://arxiv.org/abs/astro-ph/0211062 (Table 1).
- Why fusion stops at iron (binding energy per nucleon): OpenStax, Astronomy 2e, 23.2 "Evolution of Massive Stars".
- Element origins: Johnson 2019, "Populating the periodic table: Nucleosynthesis of the elements", Science 363:474.
- Age of the universe 13.787 ± 0.020 billion years: Planck Collaboration 2020, A&A 641:A6. Background temperature
  2.7255 K: Fixsen 2009, ApJ 707:916. Hubble constant range: Planck 2020 (67.4) and Riess et al. 2022, ApJL 934:L7 (73).
  Redshift and distance: Hubble 1929, PNAS 15:168. About 75 percent hydrogen and 25 percent helium by mass: OpenStax
  Astronomy 2e, 29.5 "The Beginning of the Universe".
- Solar luminosity 3.828e26 W: IAU 2015 Resolution B3. Speed of light: NIST, https://physics.nist.gov/cuu/Constants/
- Sun age 4.57 billion years (oldest meteorite solids 4.567): Connelly et al. 2012, Science 338:651.
- Human body elements: OpenStax, Anatomy and Physiology 2e, 2.1 "Elements and Atoms", Table 2.1.
- Every derived number computed in Python (2026-10-27).

## Done when
1. The Sun card shows 11 billion years of main sequence, "now" at 4.57 billion, and its death leaves a white dwarf.
2. The 20 solar mass card shows six core stages with silicon burning "11 days" and ends in a supernova and neutron star
   with the iron line spoken once.
3. The 0.4 card's life line runs past the 13.8 billion year marker with "no star this light has died yet".
4. `Compare` Sun and 40 solar masses: the 40 line ends before the Sun's main sequence is 1 percent done.
5. Sun mode counter after 10 s reads about 42,600,000 tonnes.
6. Origins: CMB card shows 2.7255 K and peak 1.06 mm; clicking gold says merging neutron stars; `My body` lights 11.
7. Arrange: the Sun's seven cards and the 20 solar mass nine cards check right in the Content order.
8. How-to lines once each; "The new elements are free." on each death.
9. Star, onion and time line visible at 1366x768; stacked at 760 and 375 wide; labels at least 10 px in the 680x425
   preview; no network, no images, no em dashes.

## Open questions
- [star-life-story] Only the Sun and the 20 solar mass star have sourced later stages; the other five cards show the
  main sequence and fate only. OK, or find a sourced track set (for example MIST models) before build?

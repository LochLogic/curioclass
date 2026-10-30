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
Focus: the star and its core, side by side in the middle of the stage, together the biggest thing on screen; the
time lines run full width under them and the card picker sits in the panel.
- Stage, top: the star as a painted portrait for its current phase (Art; main sequence portraits tinted by
  `starColor` for the card's temperature), over the painted nursery backdrop, with a small "not to scale" tag; beside
  it a code cutaway of its core as an onion of shells, each shell labeled with what it fuses ("hydrogen to helium").
- Stage, bottom, two lines driven by one scrubber:
  - Life line (true scale): the engine `deepTime` line on a log scale from 1 day to 1 trillion years since the star
    formed, the star's phases as colored bands, and a marker "age of the universe 13.8 billion years". This is the
    line that compares masses.
  - Phase strip: the same phases as equal-width bands in order, each labeled with its duration ("8.1 million years",
    "11 days"). On a log of age the late phases of a star are squeezed to a pixel or less, so the strip gives each
    one room while the life line keeps the true scale; a bracket on the life line shows where the strip's current
    band sits.
  Dragging either moves both. `Play` (Space) walks the phase strip, 2 s per band.
- Mass picker: seven star cards (Content) from 0.4 to 40 solar masses plus a 20 solar mass card with full detail. The
  current card's numbers fill the side panel: mass, surface temperature, main sequence life, fate.
- Phase readout under the scrubber: phase name, how long it lasts, what the core fuses.
- At the end of a life, `Death` plays (about 3 s): for low mass stars the painted planetary nebula grows and fades
  out from the star while the painted white dwarf fades in at its centre; for massive stars the painted supernova
  flash, then the painted remnant with a neutron star (or, for the 40 card, the painted black hole) at its centre.
  New element chips (Content, code) fly to a mini periodic table in the corner.
- `Compare` pins the current life line and draws the next one under it, so two masses share the scale.
- `Arrange` (optional): shuffled phase cards for the Sun or for the 20 solar mass star, each with its painted
  portrait where one fits; drag them into order, `Check`.

### Sun
For HS-ESS1-1. Focus: the Sun cutaway, central and large, with the running counter right under it. The Sun is the
painted star disk tinted at the Sun's color with a code wedge cut out showing three labeled zones (core, radiative
zone, convective zone, drawn at about 0.25 and 0.7 of the radius). Counter, running while the mode is open: "Since
you opened this, the Sun has turned ... tonnes of mass into energy." Panel cards: fusion in the core (four hydrogen
nuclei become one helium nucleus; 0.7 percent of the mass becomes energy); the power (3.828 × 10^26 watts, so 4.26
million tonnes a second); the trip (light leaves the surface and reaches Earth in 499 seconds, about 8.3 minutes);
the long view (lost so far in 4.57 billion years: about 0.03 percent of the Sun's mass). `Sun's future` jumps to
Life Line with the Sun card at "now".

### Origins
For HS-ESS1-2 and the element half of HS-ESS1-3. Two panels picked with `Big Bang evidence` and `Periodic table of
origins`.
- Big Bang evidence. Focus: the three plots in a row (stacked when narrow). Three cards, each with a small plot drawn
  in code. Redshift (with the painted deep field as the card header): farther galaxies move away faster (a line
  through drawn points with "about 70 km/s for every megaparsec"). Cosmic microwave background: a blackbody curve at
  2.7255 K peaking near 1.06 mm. Light elements: a bar showing about 75 percent hydrogen and 25 percent helium by
  mass. A slider runs the universe's expansion backward to show why all three point to a hot, dense start 13.787
  billion years ago.
- Periodic table of origins. Focus: the table, full stage. The full table, each element tinted by its main sources
  (Content); click an element for a line ("Most of your calcium came from exploding massive stars"). `My body`
  filter highlights the eleven elements that make up most of the human body.

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

Portrait per phase (looks only, not to scale): main sequence, the star disk tinted by `starColor` of the card's
temperature; Sun swelling, red giant branch, helium core and giant again, the giant portrait; 20 solar mass stages
after hydrogen, the giant portrait (see open question); white dwarf, neutron star, black hole, planetary nebula,
supernova and remnant as their own portraits; the five plain cards' "later stages, short" band, the giant portrait
for the white dwarf cards and the star disk for the 16 and 40 cards.

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
Sun zones for the drawing: core to about 0.25 of the radius, radiative zone to about 0.7, convective zone to the
surface.

Big Bang numbers: age 13.787 ± 0.020 billion years; background temperature 2.7255 K, peak wavelength 2.898 mm·K /
2.7255 K = 1.06 mm; Hubble constant shown as "about 70" (measurements range from 67 to 73 km/s per megaparsec).

## Interactions in detail
- Life lines come from the Content tables only; stages not in a source (for the five plain cards after the main
  sequence) show one band labeled "later stages, short" with no invented durations (no length on the life line, one
  band on the phase strip).
- Scrubbing is continuous; the portrait and onion change at each phase boundary (a 300 ms cross-fade; Motion off:
  instant). `Play` moves 2 s per phase band (Sun 7 bands, 14 s; 20 solar mass star 9 bands, 18 s; plain cards 3
  bands, 6 s), then plays Death. Motion off: Play jumps band to band each 2 s with no motion.
- Every control stays live while Play or Death runs: a drag on either line takes over at once and stops Play; a new
  card loads at once and cancels Death; `Compare` pins at once; Space pauses.
- `Compare`: at most two lines; a third replaces the older pinned one.
- Arrange: Sun cards (main sequence, swelling, red giant, helium core, giant again, planetary nebula, white dwarf);
  20 solar mass cards (hydrogen, helium, carbon, neon, oxygen, silicon, collapse, supernova, neutron star). Wrong
  places shake once and stay; `Show order` after two checks.
- Sun counter: tonnes = 4.26 × 10^6 × seconds open, with thousands separators; pauses when the tab is hidden.
- Sound: a low hum whose pitch drops as stars swell; a soft boom at a supernova; off with Sound.
- Keyboard: Space = Play or pause, arrows move the scrubber one phase, Tab reaches cards and table cells (Enter opens
  a cell).
- Layout by real stage pixels: wide (star and onion side by side), compact, stack (375 wide: onion under the star,
  both time lines full width).
- Mode change: `Curio.stop()`, `V.hush()`. Arrange results per device (localStorage `curio-star-life-story`,
  try/catch), `Clear`.

## Look
Accent (`--brand`) #b894d0, nebula violet: 6.75:1 on --panel #141b25, 6.39:1 on --sec-bg #18202b; --brand-ink
#10161f on it 7.08:1. Moved off a pale orchid that sat close to mitosis-mixer's #f1b1ed; clear of orbit-lab's
periwinkle #a9c4ff (ΔE 25); nearest 9-12 accents dance-styles #c9b3ff (ΔE 14) and mitosis-mixer (16).
Scene: the painted nursery backdrop under a #0b0f17 wash at 55 percent so the star portrait leads; star portraits
drawn with screen blend on that dark; onion shells hydrogen #6f8fd8, helium #e0c060, carbon #8a8a8a, oxygen and neon
#6fc7b0, silicon #c08a5a, iron #b04a3a. Time bands use `--gr-1` to `--gr-4`. Element source tints use six colors from
the kit's chart set with a text label in each cell. Orbit-lab uses a plain starfield; this tool uses a glowing
nebula, so the two stages look different side by side.

## Art
Local FLUX (`scripts/localart.py`), no people anywhere. All star portraits are painted on pure black and drawn with
screen blend so the black drops out (cutout no). 10 images.
- sl-star-disk: a glowing star filling the frame, a bright white sphere with fine rice-grain granulation, slightly
  darker edges and a thin soft corona, on pure black; 1:1; cutout no; people no; main sequence portrait for every
  card, tinted by `starColor`; also the Sun in Sun mode under the code cutaway wedge.
- sl-giant: an enormous swollen star, deep orange and red, with a few huge mottled convection cells and a soft hazy
  edge, on pure black; 1:1; cutout no; people no; giant phases.
- sl-white-dwarf: a tiny brilliant blue-white star with a soft round halo in the middle of pure black; 1:1; cutout
  no; people no; the white dwarf end state.
- sl-neutron-star: a tiny blazing blue-white sphere with two thin straight beams of pale light from its poles, on
  pure black; 1:1; cutout no; people no; the neutron star end state, at the remnant's centre.
- sl-black-hole: a perfectly round black shadow in a field of stars, the starlight around it bent into a thin
  glowing ring at its edge; 1:1; cutout no (drawn normally, it must cover); people no; the 40 card's end state.
- sl-planetary-nebula: a glowing ring of teal and rose gas shells around a small bright white star, on pure black;
  1:1; cutout no; people no; low mass Death (scaled 1.0 to 1.6 and faded in code) and the Arrange card.
- sl-supernova: a brilliant white and blue explosion flash with glowing streaks bursting outward, on pure black; 1:1;
  cutout no; people no; massive star Death and the Arrange card.
- sl-remnant: a wispy shell of glowing red and blue gas filaments with a tiny bright point at the centre, on pure
  black; 1:1; cutout no; people no; after the supernova, under the neutron star or black hole.
- sl-nursery: a dark dusty nebula with glowing pink hydrogen clouds and a sprinkle of young blue stars; 16:9; cutout
  no; people no; Life Line backdrop, dimmed.
- sl-deep-field: many small distant galaxies of different shapes and colors, spirals, ellipses and smudges, scattered
  on black; 16:9; cutout no; people no; header of the Redshift card.
Drawn in code: the onion core, the Sun cutaway wedge and zone labels, both time lines, element chips, the periodic
table, plots, preview.svg.

## Voice
`smooth-narrator` (Algieba), style "Say smoothly and warmly, like an audiobook narrator telling a long story." No
9-12 science tool uses it. `Curio.voice`, `scope: () => state.mode`.
- life (how; Life Line welcome; stale once the scrubber moves or Play starts): "Pick a star card, then drag the
  scrubber along its life. The core shows what it is building now."
- death (event; each Death that starts; stale on a new card or a scrub back): "The new elements are free. Watch where
  they land."
- iron (event; the 20 solar mass star enters the silicon to iron band, once per card load; stale on a new card):
  "Iron. Fusing it takes energy, so the core collapses."
- sun (how; Sun welcome; stale when the mode is left): "Every second, the Sun turns millions of tonnes of mass into
  light. Watch the counter."
- origins (how; Origins welcome; stale once a panel button or element is clicked): "Three clues point back to one hot
  start. Drag the slider to run time backward, or press Periodic table of origins."
- element (how; Periodic table of origins opened; stale once an element is clicked): "Click any element to see where
  it was made."

## Family engine
Family astronomy, engine described in full in orbit-lab's spec (`/* ASTRONOMY ENGINE: begin */ ... end */`, `const
Astro`). This tool uses `deepTime` (log, 1 day to 10^12 years) for life lines, `SpaceView` for the star and nebula
scenes (backdrop image and screen-blend sprites), `starColor(T)` for star tints, `fmt` for durations, and the
constants `L_SUN`, `M_SUN`, `C`, `AU`. It feeds the engine star tracks: `{mass, type, tempK, phases: [{name, years,
core, portrait}], fate}` from Content. The phase strip is tool-local.

## Sources
- Main sequence masses, temperatures and lifetimes: OpenStax, Astronomy 2e (2022), Table 22.1,
  https://openstax.org/books/astronomy-2e/pages/22-1-evolution-from-the-main-sequence-to-red-giants
- The Sun's future stages: Sackmann, Boothroyd and Kraemer 1993, "Our Sun. III. Present and Future", ApJ 418:457,
  https://www.cita.utoronto.ca/~boothroy/sun3.html
- 20 solar mass burning stages and the fate limits: Heger, Woosley, Fryer and Langer 2003, "How Massive Single Stars
  End Their Life", ApJ 591:288, https://arxiv.org/abs/astro-ph/0211062 (Table 1).
- Why fusion stops at iron (binding energy per nucleon): OpenStax, Astronomy 2e, 23.2 "Evolution of Massive Stars".
- Sun interior zones (core to about 0.25 of the radius, radiative zone to about 0.7): OpenStax, Astronomy 2e, 16.3
  "Solar Interior: Theory" (verify confirms the fractions).
- Element origins: Johnson 2019, "Populating the periodic table: Nucleosynthesis of the elements", Science 363:474.
- Age of the universe 13.787 ± 0.020 billion years: Planck Collaboration 2020, A&A 641:A6. Background temperature
  2.7255 K: Fixsen 2009, ApJ 707:916. Hubble constant range: Planck 2020 (67.4) and Riess et al. 2022, ApJL 934:L7 (73).
  Redshift and distance: Hubble 1929, PNAS 15:168. About 75 percent hydrogen and 25 percent helium by mass: OpenStax
  Astronomy 2e, 29.5 "The Beginning of the Universe".
- Solar luminosity 3.828e26 W: IAU 2015 Resolution B3. Speed of light: NIST, https://physics.nist.gov/cuu/Constants/
- Sun age 4.57 billion years (oldest meteorite solids 4.567): Connelly et al. 2012, Science 338:651.
- Human body elements: OpenStax, Anatomy and Physiology 2e, 2.1 "Elements and Atoms", Table 2.1.
- Number checks (Python, 2026-10-29): L/c² = 4.259 × 10^9 kg/s (4.26 million tonnes a second; 42.6 million tonnes in
  10 s); 4.57 billion years of it = 6.14 × 10^26 kg = 0.031 percent of the Sun; light 499.0 s = 8.32 minutes; CMB
  peak 1.063 mm; 4 H to He loses 0.71 percent of the mass; neon 0.60 years = 219 days, silicon 0.031 years = 11.3
  days; Sun main sequence left 6.43 billion years. Time line: on a log of age the 20 solar mass star's last four core
  stages (neon, oxygen, silicon, about 2 years in all after 9.3 million) are much less than one pixel wide, and the
  Sun's three later stages (1.4 billion years after 11 billion) take 0.05 of a decade; that failed the old "log
  scale gives short phases room" claim, hence the phase strip. Play: the old 1.2 s per decade would have run 15 s
  for the Sun and 17 s for the 0.4 card; the strip at 2 s per band runs 6 to 18 s. Compare: the 40 card's line ends
  near 1 million years, under 1 percent (110 million years) of the Sun's main sequence.

## Done when
1. The Sun card shows 11 billion years of main sequence, "now" at 4.57 billion, and its death leaves a white dwarf
   (the planetary nebula fades out, the white dwarf portrait stays).
2. The 20 solar mass card's phase strip shows six core stages with silicon burning "11 days", each band wide enough
   to read, and ends in a supernova and neutron star with the iron line spoken once per card load.
3. The 0.4 card's life line runs past the 13.8 billion year marker with "no star this light has died yet".
4. `Compare` Sun and 40 solar masses: the 40 line ends before the Sun's main sequence is 1 percent done.
5. Sun mode counter after 10 s reads about 42,600,000 tonnes.
6. Origins: CMB card shows 2.7255 K and peak 1.06 mm; clicking gold says merging neutron stars; `My body` lights 11.
7. Arrange: the Sun's seven cards and the 20 solar mass nine cards check right in the Content order.
8. Focus: in Life Line the star portrait and onion are the largest thing at 1366x768 and 680x425; in Sun the
   cutaway is.
9. A tap while Play or Death runs: dragging the scrubber stops Play in the same frame; picking a card cancels Death
   at once.
10. How-to lines once each; "The new elements are free." on each death; no line names a control not on screen.
11. Star, onion and both time lines visible at 1366x768; stacked at 760 and 375 wide; labels at least 10 px in the
    680x425 preview; all 10 images load, none shows a person; no network, no em dashes.

## Open questions
- [star-life-story] Only the Sun and the 20 solar mass star have sourced later stages; the other five cards show the
  main sequence and fate only. OK, or find a sourced track set (for example MIST models) before build?
- [star-life-story] The 20 solar mass star after hydrogen is shown with the same giant portrait as the Sun's red
  giant; no source in the spec says what it looks like then (a red supergiant is the usual picture). Add a source and
  a supergiant portrait, or keep the shared one with "not to scale"?

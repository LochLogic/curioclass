# Spectrum Explorer

## One idea
One slider runs the whole electromagnetic spectrum from radio to gamma: the wave on screen shrinks, the photon energy
climbs by a factor of ten trillion, each band lights up the devices that use it and what it does in the body, and a
line near 10 electron volts marks where light starts knocking electrons off atoms.

## Not like
- elements-inspector (built, elements family): each element's emission lines. Here the whole spectrum and what it
  does, not fingerprints of elements.
- star-life-story (this group): starlight as a star's color. Here every band of light and its uses.
- sound-studio (gr 11 physics): sound waves in air. Here electromagnetic waves, and light as
  particles too.
- size-of-everything (built): a zoom across sizes. Here the scale is wavelength and energy, with technology and health
  on every stop.
- field-lines (gr 11): static fields. Here fields that wave and carry energy and information.

## Who and how
Grade 11, physics (Light and the Electromagnetic Spectrum). Students drive, 30 to 45 minutes. Explore first: Spectrum
opens on green light with the slider ready.
Standards: HS-PS4-2, HS-PS4-3, HS-PS4-4, HS-PS4-5.
tool.json: driver "students", minutes "30-45", modes ["Spectrum", "Photon Bench", "Signal Lab", "Claim Check"].

## Screens and modes
Header (kit, 9-12 theme): "Spectrum Explorer", small line "One kind of light, many jobs." Modes `Spectrum`, `Photon
Bench`, `Signal Lab`, `Claim Check`; kit `Motion`, `Sound`, `Read`.

### Spectrum (explore, default)
Stage: a long log-scale band strip (wavelength 10 km to 1 pm, frequency and photon energy scales above and below)
with a draggable marker; above it a wave drawn at the marker's wavelength, scaled with a size comparison ("about the
size of a football field", "a bacterium", "an atom"); the visible band drawn in its real colors, the others in
labeled tints. A dashed line at 124 nm labeled "ionizing from about here". Readouts: wavelength, frequency, photon
energy (eV, with the joules value under it).
- Drag the marker or use `◀` `▶` to jump between the stops in Content. Each stop opens a band card: what it is, a
  device that uses it (with a small diagram: how the device sends or catches the wave), what it does in the body.
- `Compare` pins the current stop so two stops show their ratio: "this photon carries 10,000 times the energy".

### Photon Bench
Two benches, `Photoelectric` and `Two slits`.
- Photoelectric: a metal plate in a vacuum tube, a lamp with Wavelength (150 to 700 nm) and Brightness (0 to 100
  percent) sliders, a metal picker (Content), and a meter for electrons per second and their top energy. Below the
  wavelength threshold no electrons come out at any brightness; above it, brightness changes how many, wavelength
  changes how fast. A `Wave model says` and `Particle model says` pair of cards update with each setting, and the
  measured result marks which model predicted it. `Solar cell` swaps the plate for silicon (gap about 1.1 eV: light
  longer than about 1,100 nm makes no current).
- Two slits: a light source, two slits and a screen with Wavelength (400 to 700 nm), Slit spacing (0.10 to 1.00 mm),
  Screen distance (0.5 to 3.0 m). `Bright` shows the full fringe pattern with spacing readout; `One at a time` fires
  single photons that land as dots and build the same fringes. Strip: "Each photon lands in one spot, but the pattern
  is a wave pattern. Both models are useful."

### Signal Lab
For HS-PS4-2 and HS-PS4-5. A 16 by 16 black and white picture is sent across a chain of relay towers. Controls:
Relays (1 to 8, default 4), Noise per relay (0 to 0.30, default 0.10, as a share of the signal range), `Analog` /
`Digital` / `Both`. `Send` runs the picture tower by tower.
- Analog: each tower amplifies what it got, noise and all, so noise piles up (spread grows as noise × √relays). The
  received picture turns grainy grey.
- Digital: each tower decides 0 or 1 at the halfway mark and sends a clean copy; errors only happen when one hop's
  noise crosses the halfway mark. Flipped pixels flash red; a counter shows "pixels flipped".
- Readout table per run: relays, noise, analog spread at the end, digital flips. Strip: "Digital signals can be copied
  again and again without getting worse, until the noise is big enough to flip bits."

### Claim Check
For HS-PS4-4. Six claim cards (Content). For each: read the claim, open up to three evidence cards (who said it, when,
what kind of source), then rate it `Well supported`, `Mixed or uncertain` or `Not supported`. `Check` shows the
sourced verdict with a calm two-line reason. No score beyond a quiet count "4 of 6 match the evidence".

## Content
Photon energy E = hc / λ with hc = 1239.84 eV·nm; frequency f = c / λ, c = 299,792,458 m/s. Band edges are
conventions (sources differ): radio longer than 30 cm, microwave 1 mm to 30 cm, infrared 750 nm to 1 mm, visible 380
to 750 nm, ultraviolet 10 to 380 nm, X-ray 0.01 to 10 nm, gamma shorter than 0.01 nm.

Stops (wavelength, energy, device, body):
| Stop | λ | E (eV) | Device | Body |
|---|---|---|---|---|
| FM radio 100 MHz | 3.00 m | 4.1 × 10^-7 | radio: a carrier wave whose frequency is nudged to carry sound | passes through; no effect at normal levels |
| Microwave oven and Wi-Fi 2.45 GHz | 12.2 cm | 1.0 × 10^-5 | oven: water molecules absorb and heat; Wi-Fi: digital data | heating only at high power; exposure limits keep phones far below that |
| 5G millimeter wave 28 GHz | 1.07 cm | 1.2 × 10^-4 | phones: short range, lots of data | absorbed in the outer skin layer as slight warmth at high power |
| Body heat | 9.35 µm | 0.133 | thermal camera | your body glows here at 37 °C |
| Fiber optic 1550 nm | 1550 nm | 0.800 | internet cables: light trapped by total internal reflection | none (inside glass) |
| TV remote 940 nm | 940 nm | 1.32 | remote: blinks a digital code | none |
| Red laser 650 nm | 650 nm | 1.91 | laser pointer, barcode scanner | vision; eye hazard if a beam goes straight in |
| Green 532 nm | 532 nm | 2.33 | green laser | vision; plants use red and blue more than green |
| Violet 405 nm | 405 nm | 3.06 | Blu-ray laser | vision |
| UV-A 365 nm | 365 nm | 3.40 | black light, nail lamps | tanning, skin aging |
| UV-B 300 nm | 300 nm | 4.13 | sunlight's sunburn band | sunburn, vitamin D, skin cancer risk |
| UV-C 254 nm | 254 nm | 4.88 | germicidal lamps | damages DNA; kept away from skin and eyes |
| Ionizing line | 124 nm | 10.0 | | from about here up, photons can ionize atoms and molecules |
| Medical X-ray 50 keV | 0.0248 nm | 50,000 | X-ray imaging: soft tissue lets it pass, bone absorbs it | ionizing; small doses used with care |
| Gamma 140 keV | 0.00886 nm | 140,000 | medical tracer (technetium-99m) and gamma camera | ionizing |
Body heat wavelength from Wien's law: 2,898 µm·K / 310 K = 9.35 µm.

Photoelectric (work functions, eV, and threshold wavelengths 1239.84 / φ): sodium 2.46 (504.0 nm), aluminum 4.08
(303.9), zinc 4.31 (287.7), iron 4.50 (275.5), copper 4.70 (263.8), silver 4.73 (262.1), platinum 6.35 (195.3). Top
electron energy = E − φ: 400 nm on sodium 0.64 eV; 254 nm on zinc 0.57 eV; 600 nm (2.07 eV) on sodium: none at any
brightness. Silicon solar cell gap about 1.1 eV, cutoff about 1,127 nm.

Two slits: fringe spacing λL / d. 650 nm, d 0.25 mm, L 1.0 m: 2.60 mm; 532 nm: 2.13 mm; 405 nm: 1.62 mm.

Signal Lab (256 pixels, levels 0 and 1, Gaussian noise σ per hop): digital flip chance per bit per hop Q(0.5 / σ);
expected flips after 8 relays: σ 0.10, 0.0006 (almost never); 0.15, 0.88; 0.20, 12.4; 0.25, 43.0; 0.30, 83.0.
Analog spread after 8 relays: 0.28 at σ 0.10, 0.57 at σ 0.20.

Claims:
- K1 "Radio waves from cell phones are listed by the World Health Organization's cancer agency as possibly
  carcinogenic." Verdict: the listing is real (IARC Group 2B, 2011), and 2B means limited evidence; the US FDA's review
  found the weight of evidence does not link phone use to health problems. Mixed or uncertain.
- K2 "Microwave ovens make food radioactive." Not supported: microwaves heat water molecules; they are not ionizing
  and do not make food radioactive (FDA).
- K3 "You can get sunburned on a cloudy day." Well supported: UV passes through clouds (CDC).
- K4 "A chest X-ray gives about the same dose as 10 days of natural background radiation." Well supported: about 0.1
  mSv (RadiologyInfo, ACR and RSNA).
- K5 "Blue light from phone screens damages your eyes." Not supported by current evidence (American Academy of
  Ophthalmology); screens can cause eye strain and affect sleep timing.
- K6 "Tanning beds are safe because they use mostly UV-A." Not supported: UV-emitting tanning devices are Group 1
  carcinogens (IARC 2009); the FDA warns against their use by people under 18.
Evidence cards per claim name the source type (agency review, single study, advertisement, social post) so students
weigh reliability as well as content; the ad and post cards are written for the tool and say so.

## Interactions in detail
- The band strip is log scale; dragging snaps to stops within 3 percent; the wave drawing keeps 3 to 6 cycles on
  screen and the size comparison changes with each power of ten.
- Photoelectric: electrons per second ∝ brightness when E > φ, zero otherwise; top energy shown to 2 decimals; at E
  within 0.02 eV of φ the meter reads "barely". Brightness 0 shows no electrons whatever the wavelength.
- Two slits, One at a time: photons drawn from the two-slit intensity pattern (cos² fringes under a single-slit
  envelope for 0.05 mm slits), 20 a second, up to 2,000, `Clear screen`.
- Signal Lab: seeded random per `Send` (shown as "run 3"); `Same noise again` repeats a run for a fair analog and
  digital comparison.
- Claim Check: ratings can be changed until `Check`; after `Check` the card stays open with its sources linked as
  text (no network calls).
- Sound: a tone whose pitch follows the marker (log mapped, audible range only), a click per photon; off with Sound.
- Keyboard: arrows move the marker one stop, Home and End jump to the ends; Space = Send or Fire; Tab reaches cards.
- Layout by real stage pixels: wide, compact, stack (375 wide: the band strip turns vertical with the card under it).
- Mode change: `Curio.stop()`, `V.hush()`. Signal runs and claim ratings per device (localStorage
  `curio-spectrum-explorer`, try/catch), `Clear`.

## Look
Accent (`--brand`) #ece8ff, pale light lavender (white light): 14.47:1 on --panel #141b25, 13.71:1 on --sec-bg
#18202b; --brand-ink #10161f on it 15.18:1. Nearest 9-12 accents: speedometer #c7d2de (math, ΔE 12), gas-law-lab
#9ec9e8 (ΔE 21).
Scene: dark lab #0e131b; the visible band in true hues (380 to 750 nm, sRGB approximation); radio #6c7a8f,
microwave #7f8fa8, infrared #a35a4a, ultraviolet #8a6fd8, X-ray #9aa8b8, gamma #c8d0dc, each band label in #e8edf3
(over 9:1 on the tints at 40 percent). Ionizing line `--gr-4`. Analog signal `--gr-1`, digital `--gr-3`, flipped
pixels `--gr-4`.

## Art
none: drawn in code (spectrum strip, waves, device diagrams, tube, slits, relay towers, cards, preview.svg).

## Voice
`knowing-guide` (Sadaltager), style "Say in a knowledgeable, friendly way, like a curator in a science museum's
gallery of light." No group sibling uses it; shared in 9-12 science only with tree-of-life (gr 9 biology).
curious-librarian was left to half-life-dice, the closer radiation neighbor. `Curio.voice`, `scope: () => state.mode`.
- spectrum (how, Spectrum welcome): "Drag the marker from radio to gamma. Watch the energy number climb."
- ionizing (event, first time the marker crosses 124 nm; stale on leaving the ultraviolet band): "Past this line, light can knock electrons off atoms."
- photon (how, Photon Bench welcome): "Try red light on sodium, then turn the brightness all the way up."
- none (event, bright light below threshold; stale on a wavelength change): "Brighter, but still nothing. Each photon is too weak on its own."
- signal (how, Signal Lab welcome): "Send the picture both ways and compare what arrives."
- claims (how, Claim Check welcome): "Read the claim, check who is saying it, then rate it."

## Family engine
none. Plots use `kit/graphing.js` `Plane` if present; otherwise the tool's own SVG.

## Sources
- Band edges, tour of the spectrum and uses: NASA Science, "Tour of the Electromagnetic Spectrum",
  https://science.nasa.gov/ems/ (read 2026-10-27).
- hc = 1239.84 eV·nm and c: NIST CODATA 2018, https://physics.nist.gov/cuu/Constants/
- Work functions: OpenStax, University Physics Volume 3, Table 6.1,
  https://openstax.org/books/university-physics-volume-3/pages/6-2-photoelectric-effect
- Two-slit interference and single photons: OpenStax, University Physics Volume 3, 3.1 and 7.1.
- Silicon band gap about 1.1 eV: OpenStax, University Physics Volume 3, 9.6 "Semiconductors and Doping".
- Wien's law 2,898 µm·K: OpenStax, University Physics Volume 3, 6.1 "Blackbody Radiation".
- Ionizing radiation: US EPA, "Radiation Basics", https://www.epa.gov/radiation/radiation-basics
- Fiber optics and total internal reflection: OpenStax, College Physics 2e, 25.4.
- K1: IARC press release 208 (31 May 2011); US FDA, "Review of Published Literature between 2008 and 2018 of Relevance
  to Radiofrequency Radiation and Cancer" (2020). K2: US FDA, "Microwave Oven Radiation". K3: CDC, "Sun Safety". K4:
  RadiologyInfo.org (ACR and RSNA), "Radiation Dose" (chest X-ray 0.1 mSv, about 10 days). K5: American Academy of
  Ophthalmology, "Should You Be Worried About Blue Light?" (2021). K6: IARC Monographs volume 100D (2012, classification
  2009); US FDA, "Indoor Tanning: The Risks of Ultraviolet Rays".
- Signal Lab noise model and pictures are made up; every value computed in Python (2026-10-27).

## Done when
1. Marker at 532 nm reads 2.33 eV and 5.64 × 10^14 Hz; at 12.2 cm it reads 1.0 × 10^-5 eV and the oven card.
2. Crossing 124 nm shows the ionizing line and speaks it once.
3. Sodium: 600 nm at 100 percent brightness gives no electrons; 400 nm gives top energy 0.64 eV; doubling brightness
   doubles electrons per second and leaves 0.64 unchanged.
4. Platinum needs light under 195.3 nm; the solar cell gives no current at 1,200 nm.
5. Two slits at 650 nm, 0.25 mm, 1.0 m shows 2.60 mm spacing; One at a time builds the same fringes.
6. Signal Lab with 8 relays at noise 0.20: digital flips land near 12 (the readout), analog spread 0.57.
7. Claim Check: all six verdicts show with their sources; ratings saved per device.
8. How-to lines once each; event lines as listed.
9. Strip, cards and controls visible at 1366x768; stacked at 760 and 375 wide; labels at least 10 px in the 680x425
   preview; no network, no images, no em dashes.

## Open questions
- [spectrum-explorer] Claim Check uses real health claims (cell phones, tanning beds, blue light). Is the calm,
  sourced framing right for school, or should K1 and K6 get a teacher note?
- [spectrum-explorer] Four modes in one tool. Keep Signal Lab here for HS-PS4-2, or split it into its own tool later?

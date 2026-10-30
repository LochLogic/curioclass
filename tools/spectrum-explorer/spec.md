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
Bench`, `Signal Lab`, `Claim Check`; kit `Motion`, `Sound`, `Read` (Sound starts on as the kit sets it).

### Spectrum (explore, default)
Focus: the band strip with its marker and the wave above it, full stage width; the band card sits under them (beside
them when the window is wider than tall enough), never covering the strip.
Stage: a long log-scale band strip (wavelength 10 km to 1 pm, frequency and photon energy scales above and below)
with a draggable marker; above it a wave drawn at the marker's wavelength, scaled with a size comparison ("about the
size of a football field", "a bacterium", "an atom"); the visible band drawn in its real colors, the others in
labeled tints. A dashed line at 124 nm labeled "ionizing from about here". Readouts: wavelength, frequency, photon
energy (eV, with the joules value under it).
- Drag the marker or use `◀` `▶` to jump between the stops in Content. Each stop opens a band card: its painted device
  picture (Art), what it is, the device that uses it (with a small code diagram: how the device sends or catches the
  wave), what it does in the body.
- `Compare` pins the current stop so two stops show their ratio: "this photon carries 10,000 times the energy".

### Photon Bench
Two benches, `Photoelectric` and `Two slits`. Focus: the tube and its electron meter (Photoelectric) or the screen
where the fringes build (Two slits), the largest thing on the stage; sliders in the panel.
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
Tube, plate, lamp, slits and screen are diagrams, drawn in code.

### Signal Lab
For HS-PS4-2 and HS-PS4-5. Focus: the two received pictures, side by side and larger than the sent one; the tower
chain runs across the top of the stage over the painted hills (se-hills), one painted tower (se-tower) per relay.
A 16 by 16 black and white picture is sent across the chain. Controls: Relays (1 to 8, default 4), Noise per relay (0
to 0.30, default 0.10, as a share of the signal range), `Analog` / `Digital` / `Both`. `Send` runs the picture tower by
tower (0.4 s a hop, at most 3.2 s).
- Analog: each tower amplifies what it got, noise and all, so noise piles up (spread grows as noise × √relays). The
  received picture turns grainy grey.
- Digital: each tower decides 0 or 1 at the halfway mark and sends a clean copy; errors only happen when one hop's
  noise crosses the halfway mark. Flipped pixels flash red; a counter shows "pixels flipped".
- Readout table per run: relays, noise, analog spread at the end, digital flips. Strip: "Digital signals can be copied
  again and again without getting worse, until the noise is big enough to flip bits."

### Claim Check
For HS-PS4-4. Focus: the open claim card, centred, with its evidence cards beside it.
Six claim cards (Content). For each: read the claim, open up to three evidence cards (who said it, when, what kind of
source), then rate it `Well supported`, `Mixed or uncertain` or `Not supported`. `Check` shows the sourced verdict
with a calm two-line reason. No score beyond a quiet count "4 of 6 match the evidence".

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

Signal Lab (256 pixels, levels 0 and 1, Gaussian noise σ per hop): digital flip chance per bit per hop p = Q(0.5 / σ);
a pixel arrives wrong when it flipped an odd number of times, (1 − (1 − 2p)^8) / 2 after 8 relays. Expected wrong
pixels after 8 relays: σ 0.10, 0.0006 (almost never); 0.15, 0.88; 0.20, 12.2; 0.25, 39.8; 0.30, 70.7. Analog spread
after 8 relays: 0.28 at σ 0.10, 0.57 at σ 0.20.

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
  screen and the size comparison changes with each power of ten. The band card and its picture change the moment the
  marker snaps to a new stop.
- Photoelectric: electrons per second ∝ brightness when E > φ, zero otherwise; top energy shown to 2 decimals; at E
  within 0.02 eV of φ the meter reads "barely". Brightness 0 shows no electrons whatever the wavelength. Electrons
  stream continuously; a slider or metal change shows in the same frame.
- Two slits, One at a time: photons drawn from the two-slit intensity pattern (cos² fringes under a single-slit
  envelope for 0.05 mm slits), 20 a second for the first 200, then 100 a second up to 2,000 (about 28 s in all, so
  the first dots can be watched one by one and the pattern still fills in under 30 s); `Clear screen`. A slider change
  clears the screen and restarts at once with the new pattern.
- Signal Lab: seeded random per `Send` (shown as "run 3"); `Same noise again` repeats a run for a fair analog and
  digital comparison. A control change during a run ends it at once and shows the new settings, ready to Send.
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
#9ec9e8 (ΔE 21); in this batch circuit-builder's spark blue #8fa0ff is ΔE 47 away.
Scene: dark lab #0e131b; the visible band in true hues (380 to 750 nm, sRGB approximation); radio #6c7a8f,
microwave #7f8fa8, infrared #a35a4a, ultraviolet #8a6fd8, X-ray #9aa8b8, gamma #c8d0dc, each band label in #e8edf3
(over 9:1 on the tints at 40 percent). Ionizing line `--gr-4`. Analog signal `--gr-1`, digital `--gr-3`, flipped
pixels `--gr-4`. The device pictures sit on the cards in a 4:3 frame with a 1 px #2b3440 border.

## Art
Local FLUX (`scripts/localart.py`). No people anywhere: the body column is words only, and every band is shown by
its device or source. 16 images.
- Device kit for the band cards (one shared prompt line, 4:3, cutout no, people no): "a single everyday device or
  light source on a plain soft gray background, studio light, blank screens and blank labels", pieces: se-radio (a
  small portable FM radio with its antenna pulled out), se-oven (a white microwave oven with its door closed and a
  plain control panel), se-phone (a smartphone lying face up with a dark blank screen), se-thermal (a handheld
  thermal camera with a pistol grip and a round lens), se-fiber (a bundle of thin glass optical fibers fanning out,
  their tips glowing), se-remote (a black TV remote with plain round buttons, its small front window facing the
  viewer), se-laser-red (a slim silver laser pointer sending a thin red beam), se-laser-green (a slim black laser
  pointer sending a thin green beam), se-disc (a silver optical disc with a rainbow sheen), se-blacklight (a black
  light tube glowing deep violet in a plain holder), se-uvc (a straight germicidal lamp tube glowing pale blue in a
  steel fixture), se-xray (a medical X-ray tube head on a jointed arm above an empty padded table), se-gamma (a
  medical gamma camera: two large flat detector heads on a ring gantry above an empty bed).
- se-sun: the bright sun high in a hazy summer sky above a layer of white clouds; 4:3; cutout no; people no; the UV-B
  card (the source, sunlight, is the point), and the K3 claim card.
- se-tower: a lattice steel radio relay tower with two round dish antennas near the top, side view on a plain white
  background; 9:16; cutout yes; people no; one per relay in Signal Lab.
- se-hills: a wide landscape of low rolling hills at dusk, soft purple and blue sky, dark grass; 4:1; cutout no;
  people no; behind the tower chain in Signal Lab.
Drawn in code: band strip, scales, waves, size comparisons, device diagrams, tube, plate, lamp, slits, screen,
photons, pictures and pixels, evidence cards and their source-type icons, preview.svg.

## Voice
`knowing-guide` (Sadaltager), style "Say in a knowledgeable, friendly way, like a curator in a science museum's
gallery of light." No grade 10 or 11 neighbor or batch sibling uses it; shared in 9-12 science only with
tree-of-life (gr 9 biology). curious-librarian was left to half-life-dice, the closer radiation neighbor.
`Curio.voice`, `scope: () => state.mode`. Hints change at once on every mode or state change; lines queue with a
`valid` check.
- spectrum (how; Spectrum welcome; stale once the marker moves): "Drag the marker from radio to gamma. Watch the
  energy number climb."
- ionizing (how; first time the marker crosses 124 nm; stale on leaving the ultraviolet band): "Past this line, light
  can knock electrons off atoms."
- photon (how; Photoelectric welcome; stale once the metal or wavelength changes): "Pick Sodium, drag Wavelength to
  red, then drag Brightness all the way up."
- none (event; brightness raised with light below threshold; stale on a wavelength or metal change): "Brighter, but
  still nothing. Each photon is too weak on its own."
- slits (how; Two slits opens; stale once One at a time is pressed): "Press One at a time and watch single photons
  build the stripes."
- signal (how; Signal Lab welcome; stale once Send is pressed): "Pick Both, then press Send. Compare the two pictures
  that arrive."
- claims (how; Claim Check welcome; stale once a rating is pressed): "Read the claim and open the evidence cards. Then
  press a rating and Check."

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
- Signal Lab noise model and pictures are made up.
- Number checks (Python, 2026-10-29): every stop's energy and frequency recomputed and matched (532 nm 2.33 eV and
  5.635 × 10^14 Hz; 2.45 GHz 12.24 cm and 1.01 × 10^-5 eV; Wien 9.35 µm); every threshold wavelength matched; 400 nm
  on sodium 0.640 eV, 254 nm on zinc 0.571 eV, silicon cutoff 1,127 nm; fringes 2.60, 2.13, 1.62 mm; analog spread
  0.283 and 0.566. Digital flips: the old table counted every flip (12.4, 43.0, 83.0 at σ 0.20, 0.25, 0.30), but a
  pixel flipped twice arrives right, so the readout's expected wrong pixels are 12.2, 39.8 and 70.7 (fixed; 0.10 and
  0.15 unchanged). Photon energy ratio across the strip (10 km to 1 pm) is 10^16 and between the FM and gamma stops
  3.4 × 10^11; neither is ten trillion (see Open questions). One at a time now fills 2,000 photons in 28 s (was 100 s
  at 20 a second).

## Done when
1. Marker at 532 nm reads 2.33 eV and 5.64 × 10^14 Hz; at 12.2 cm it reads 1.0 × 10^-5 eV and the oven card with its
   picture.
2. Crossing 124 nm shows the ionizing line and speaks it once.
3. Sodium: 600 nm at 100 percent brightness gives no electrons; 400 nm gives top energy 0.64 eV; doubling brightness
   doubles electrons per second and leaves 0.64 unchanged.
4. Platinum needs light under 195.3 nm; the solar cell gives no current at 1,200 nm.
5. Two slits at 650 nm, 0.25 mm, 1.0 m shows 2.60 mm spacing; One at a time builds the same fringes and reaches 2,000
   photons in about 28 s.
6. Signal Lab with 8 relays at noise 0.20: digital wrong pixels land near 12 over several runs, analog spread 0.57.
7. Claim Check: all six verdicts show with their sources; ratings saved per device.
8. Focus: the band strip and wave span the stage in Spectrum, the tube or fringe screen is the largest thing in
   Photon Bench, and the two received pictures in Signal Lab, at 1366x768 and in the 680x425 preview.
9. A tap while anything runs: moving Wavelength during One at a time clears and restarts the pattern in the same
   frame; changing Noise during Send ends the run at once.
10. How-to lines once each per load, then hint only; the none line each time it fits; all 16 images load, none shows
    a person or lettering.
11. Strip, cards and controls visible at 1366x768; stacked at 760 and 375 wide; labels at least 10 px in the 680x425
    preview; no network, no em dashes.

## Open questions
- [spectrum-explorer] Claim Check uses real health claims (cell phones, tanning beds, blue light). Is the calm,
  sourced framing right for school, or should K1 and K6 get a teacher note?
- [spectrum-explorer] Four modes in one tool. Keep Signal Lab here for HS-PS4-2, or split it into its own tool later?
- [spectrum-explorer] The One idea says photon energy "climbs by a factor of ten trillion", but the strip spans
  10^16 (10 km to 1 pm) and the stops span 3.4 × 10^11 (FM to gamma). The One idea is not ours to change: say "ten
  million billion" for the strip, or "a third of a trillion" for the stops?

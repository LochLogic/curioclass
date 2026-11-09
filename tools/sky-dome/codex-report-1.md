# Codex report: sky-dome (Curiosity No. 05)

## Built

A full-screen brass observatory with a catalogue-driven canvas dome, time and date rings, year odometer, projector transport, setting circle, rim levers, object measurements, lower-left maker's plate, power panel and Manual drawer. The deliverable is `sky-dome.html`; edit `src.html` and rebundle.

Core astronomy includes sidereal rotation, catalogue proper motion, precession, JPL Keplerian planets with light-time correction, the Sun, a truncated periodic Moon with topocentric parallax, lunar illumination and conjunction age, average refraction, and numerical rise/set crossings. Stars are never randomly scattered. Milky Way brightness is an explicitly illustrative galactic band.

Build only. No commits, deployment, shared-engine edits, sub-agents or polish round. Authored files are confined to the two authorized folders. The report is deliberately written last because the Curiosity brief and user say to stop immediately when it exists; this overrides the general machinery's early-report advice.

## The real material

All retrieval dates: 2026-11-05. Raw web exports and the failed direct-download manifest are in `_scratch/sky-dome/data/`; `gather.py` records bounded direct routes, and `pack.py` reproducibly rebuilds the catalogue JSON from the saved exports.

- **Stars:** Hoffleit & Warren, Yale Bright Star Catalogue, fifth revised edition. [HEASARC documentation](https://heasarc.gsfc.nasa.gov/W3Browse/star-catalog/bsc5p.html), [NASA licence record](https://data.nasa.gov/dataset/bright-star-catalog), [NOIRLab institutional export](https://www-kpno.kpno.noirlab.edu/Info/Caches/Catalogs/BSC5/catalog5.html). NASA specifies US Government Works / public domain. Direct HEASARC/CDS downloads were denied or unavailable; the same named Yale material was recovered from its institutional HTML transcription through bounded web reads. All 9,096 stellar rows were retained. Fourteen blank or non-stellar HR entries are excluded and listed in `pack-summary.json`. RA, DEC, magnitude, proper motion and spectral class are bundled.
- **Names:** [IAU WGSN catalogue snapshot](https://github.com/mirandadam/iau-starnames/blob/master/catalog_data/IAU-CSN.txt), dated 2022-04-04. Its own header grants Creative Commons Attribution terms without specifying a version. 333 HR-matched names are used, credited to IAU WGSN. No etymologies or cultural stories are bundled.
- **Colours and temperatures:** spectral-class colour ramp for the full star field. Only the two BSC colour-index values explicitly supplied by the spec, Betelgeuse +1.85 and Rigel -0.03, receive numerical B-V and approximate temperature. [NASA's Orion account](https://science.nasa.gov/universe/stories/quick-reads/discovering-the-universe-through-the-constellation-orion/) independently confirms their red/blue distinction. Temperature uses the mathematical formula of [Ballesteros 2012](https://arxiv.org/abs/1201.1809); no paper text, figures or code is reproduced. This is a rough colour estimate, especially for supergiants.
- **Distances:** Sirius 8.6 ly, [NASA Hubble](https://science.nasa.gov/asset/hubble/the-dog-star-sirius-and-its-tiny-companion/); Vega 25 ly, [NASA DART](https://www.nasa.gov/missions/dart/nasas-dart-captures-one-of-night-skys-brightest-stars/) and [NASA Spitzer](https://science.nasa.gov/photojournal/tiny-particles-so-far-away/). Public-domain factual values. Hipparcos is not redistributed. All other stellar distances explicitly say “not bundled”.
- **Planets:** [JPL Standish/Williams element tables](https://ssd.jpl.nasa.gov/planets/approx_pos.html), Tables 1, 2a and 2b. Numerical facts and mathematical methods are independently implemented; no article prose or source code is reproduced. Table 1 covers 1800–2050; Table 2 covers the rest of the specified 3000 BC–AD 3000 interval. The five bright planets are included. Their unbundled apparent magnitudes are shown as unknown.
- **Sun, Moon, events and precession:** independently implemented mathematical methods described by Jean Meeus, *Astronomical Algorithms*. No book prose or code is reproduced. Lunar longitude/distance uses 30 leading terms, latitude 20, plus additive corrections. The Manual explicitly limits accuracy, especially for ancient dates, and makes no eclipse prediction claim.
- **Lines:** 15 simplified conventional figures, implemented as original HR connections. Reference and attribution: [IAU / Sky & Telescope charts](https://www.iau.org/IAU/Astronomy-FAQs/Constellations.aspx), whose page states CC BY 4.0. The full 88-figure line set is not bundled; these are figures, not constellation boundaries.
- **Places:** 48 approximate city-centre or geographic entries, including pole and equator settings. [Natural Earth terms](https://www.naturalearthdata.com/about/terms-of-use/) state public domain. The bulk download was blocked; this is a small manually selected list, not a claimed 1,200-city extraction. Unmatched device zones explicitly say zone estimate and use an equatorial longitude estimate. Latitude and longitude can always be entered directly.
- **Manual facts:** [USNO sidereal time](https://aa.usno.navy.mil/data/siderealtime), [NASA Polaris](https://science.nasa.gov/solar-system/what-is-the-north-star-and-how-do-you-find-it/), NASA stellar and planetary references, and the catalogue/algorithms above. There are no quoted stories. Facts beyond the retained numerical material are plain explanatory summaries.

Optional Messier markers were removed because their individual coordinate checks could not be finished to the brief's source standard. Cultural stories were omitted as the spec leans. There are no painted images or outside libraries.

## Break the instrument

- Six years (-2999, -2799, 0, 1, 2026, 3000) crossed with three latitudes (-90, 0, 90): 18 combinations, no non-finite positions or exceptions. Polar events return above/below-all-day states rather than fabricated rise/set times.
- A real jittered pointer drag exposed an inverted horizon basis; corrected and re-shot. Ground is now below the horizon. Ground masking caches by camera settings, so running time does not rebuild it every frame.
- Held lever clicks, rate changes, reversed time, both grids, trails, zoom and selected objects were exercised. Empty/invalid place input retains the old location and announces the missing place. Numeric fields clamp their stated bounds.
- Real arrow keys on the time ring advanced 21:00 to 22:10 with Right and Shift Right. Calendar stepping preserves 12:00 across the autumn DST transition and clamps January 31 plus one month to February 28.
- Motion off: two Play presses stepped to 04:20; after an additional second time was unchanged and playing was false. Resizing audit states produced no exceptions or stuck disabled controls.
- Final file resource timing contained no resource requests. The only focused-host error was its missing favicon; the test host and tool now use an inline empty favicon, followed by a focused phone retry.

## Voice walk

Bank: `calm-professor`, voice `Schedar`, presenter style in `voice/lines.json`. No recording was made, as required; the shared kit uses browser speech fallback.

Held clicks at two-second gaps produced one “Drag the time dial.” hint, then Read describing the current date, clock, Denver and lunar phase. Read also worked with Sound off. Later instrument actions produce no narration. A first drag hides the hint immediately and drops stale speech; no late instruction interrupts the instrument. The speech log is saved in `voice-result.json`. Acoustic character was not judged in this muted unattended session.

## Short test

The unattended proxy walk uses six 100-second observation windows plus real held inputs and keyboard changes. The grade-1 perspective assumes the spec's teacher operating the large rings; the adult perspective examines seasons, poles, colour and distance. This is agent judgement, not a child usability study.

- Would a kid open it unassigned? **Yes, provisionally:** one turn immediately changes the sky, and there is no front-door reading or completion demand. A daytime opening initially shows fewer objects; turning time is the reveal.
- Would an adult play for fun? **Yes:** date and place changes, orbital trails and the ancient pole have sustained depth. Missing colour/distance measurements limit the current star-inspection depth.
- Is the real thing the interface? **Yes:** catalogue points, computed sky coordinates, lunar illumination and real time/place settings form the working surface.
- Does it work without a score or finish line? **Yes:** the entire instrument remains available continuously.

Frame comparison with Elements Inspector:

![Sky Dome beside Elements Inspector](../../_scratch/sky-dome/comparison.png)

The comparison shows comparable whole-screen instrument confidence and numerical density, with an observatory's own material and layout. It is a build comparison, not a polish round.

## Lesson creep check

Searched `src.html` and voice lines for score, points, level, goal, sticker, badge, correct, wrong, try again, complete and well done. Remaining “points” hits are geometric variable names; none is game language. No score, goal list, level, reward, quiz, finish screen, mode pills or kit header exists. No em dash in authored tool copy or code.

## Done when

1. **FAIL, partial:** Denver's device-zone opening and no-permission/no-welcome behaviour pass. The small place table does not locate every device zone correctly; unknown zones use an explicitly labelled estimate.
2. **FAIL, verification incomplete:** ten Yale coordinates independently cross-check to IAU J2000 values within 0.000210°. Precession and proper motion are implemented. The five required live JPL Horizons spot checks could not be retrieved. Computed 2026-11-05 00:00 UTC RA/DEC (degrees): Mercury 219.1557/-15.5562; Venus 201.2480/-13.1041; Mars 143.5585/16.2182; Jupiter 147.3454/13.9119; Saturn 9.4293/1.1541. These are outputs, not claimed independent validation.
3. **FAIL, reference check incomplete:** Denver June 21 computes rise 11:32:12 UTC, set 02:31:30 UTC next day, daylight 14h 59m 18s; December 21 computes 14:17:32, 23:38:49, daylight 9h 21m 17s. The official USNO reference query/download was unavailable, so the two-minute requirement is not asserted as verified.
4. **FAIL, partial:** against [USNO November phase dates](https://aa.usno.navy.mil/calculated/moon/phases?date=2026-11-01&format=p&nump=8), new/quarter/full elongations were 359.9877°, 89.9955° and 179.9677°. Quarter/full ages were 8.1975 and 15.3260 d. The computed new Moon is 93 seconds later than USNO, so the age still reports the previous cycle at that exact boundary. Away from conjunction the discrepancy is about 0.0011 d. Same-clock nightly stepping and DST preservation pass.
5. **PASS:** 2800 BC gives Thuban DEC +89.908° with proper motion, about 0.092° from the pole. Astronomical year -2799 means 2800 BC; the Manual explains year zero.
6. **PASS for tested controls:** main rings, year, transport, levers and view controls have keyboard operation and accessible names/values. Main time/date/Play targets are at least 60 px; secondary targets at least 44 px. Phone Place traps focus and returns it on close. No physical touchscreen test was available.
7. **FAIL, hardware verification unavailable:** desktop headless rendering, including all stars/lines/trails, measured 9.1 ms median and 9.9 ms at the 95th percentile (120 samples). No school Chromebook or defensible hardware-equivalent profile was available; 60 fps on that hardware is not claimed.
8. **PASS:** required widths and heights captured in the single audit, including 1366x768 and the real 375x812 iframe host. Plate and Manual remain lower-left. Actual collisions at 1000 px and in short previews were fixed and checked with focused shots.
9. **PASS:** Motion off never advances on its own; Play steps. Text contrast examples: cream on control 11.17:1; muted on night 9.39:1; plate 7.08:1; control labels 6.64:1.
10. **PASS for bundled material:** single offline file, zero resource requests in standalone measurements; named sources and terms in the Manual and draft metadata. Approximate/missing material is explicitly identified. IAU name-source terms do not specify a CC version, and that remains stated rather than guessed.
11. **PASS, provisional agent judgement:** four short-test answers and comparison frame above; timed unattended walk and frames retained. No claim of human participant testing.
12. **PASS:** no game or lesson gate, reward, progress display, mode pills or finish screen.

## Audit leads

One mechanical audit, `--no-walk`, on Chrome 9996 and host 8795; held-input and voice walks were separately performed. It finished with **283 leads**, primarily intentional canvas/readout overlays and modal coverage. It reports no Motion-off loop, resize exception or stuck disabled state.

- Canvas underneath telemetry, rim controls and object readout: intentional instrument composition; canvas contains no prose hidden by those elements.
- Short-preview zoom/readout collision and 1000 px transport/settings collisions: fixed; focused frames retained.
- Object card over view buttons: buttons are now hidden while the card is open. Canvas wheel and keyboard zoom remain available.
- Source links under 44 px: made inline blocks with at least 44 px height. Manual prose and references intentionally scroll, with a sticky Close button and native modal focus handling.
- Place sheet over dome and wheels: intentional modal sheet; background is now inert, focus wraps within the sheet, Escape closes, and desktop resize clears its modal state.
- Date/time labels overlapping their wheel hit boxes: intentional engraved labels on those controls. They do not block input.
- Hint out of view after an action: required one-shot hint removal, not missing instructions. Read supplies the current sky.
- No blanket “audit clean” claim. The original audit is preserved; fixes received targeted checks rather than a second full audit.

## Frames looked at

All captured frames inspected individually or on contact sheets: four model tools; initial/default/preview/phone frames; numerical check; night, trails/grid, panned horizon, Thuban, lunar quarter, voice/keyboard, extrema, Motion off and Manual; corrected horizon/Moon/keyboard/calendar; all 20 audit frames; focused 680/1000/phone corrections; and the six timed-walk scenes. Contact sheets and original PNGs stay in `_scratch/sky-dome/`.

## Art made

Zero raster images and zero placeholder art. Canvas draws the exact working sky; CSS/SVG draws the instrument. The bundle is 577,392 bytes and meets both the 600 KB spec goal and the 2 MB general goal. The empty art manifest explains the choice.

## Engine changes wanted

None. Shared kit, docs, scripts and other tool sources were not edited.

## Left open

- Independent Horizons and official USNO solstice comparisons, and actual school-hardware performance verification.
- Full Natural Earth place catalogue and broader timezone mapping, complete BSC B-V fields, more independently sourced distances and full constellation figure set.
- Lunar conjunction boundary age discrepancy and growing ancient-time/rotation uncertainty. The Moon is approximate, not telescope-exact.
- Optional deep-sky markers were omitted rather than retaining unchecked coordinates. Cultural sky stories remain omitted as advised.
- Recorded calm-professor speech and listening verification; no paid recording or upload was attempted.
- Teacher `plan.md` is not part of this build. Do not replace the anchor lesson card without an appropriate teacher plan.

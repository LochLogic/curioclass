# Codex review: sky-dome

## Played

Cold play preceded builder report, handoff, notes and source. Grade 1 teacher-projector, grade 5 solo and adult perspectives, using held clicks, a jittered ring drag, keyboard navigation, sky selection and long observation windows. This is an unattended reviewer proxy, not a child usability study.
Instrument time exceeded ten minutes: six 90-second windows plus at least 73.42 seconds of held-input/voice observation, excluding loading and Chrome startup. There are 108 recorded sky states; `review-summary.json` gives a conservative total of 613.5 seconds.
The night wheel, dense catalogue and brass deck invite exploration. Kept their confidence, colour and density.

## Findings fixed

- **Blocker, family: place data.** Natural Earth mislabeled Maradi as Niamey, also choosing the wrong Africa/Niamey home city. Corrected against NAMEASCII and Wikidata Q664550; regenerated packed cities and zone indexes using `review_pack.py`. Correct Niamey remains Q3674.
- **Should fix, general: main-path voice.** Hint spoke only on Manual pointerdown. First instrument pointer/key now speaks it once through Curio.voice; no continuing narration. Read pauses transport and reads an intelligible date/time with units.
- **Should fix, general: small layouts.** Dial captions wrapped/clipped in 680x425 and collided on the phone. Captions stay on one line; phone captions reserve space above the rings. Main targets remain at least 60 px.
- **Should fix, family: phone reverse.** The reverse switch was hidden without another phone path. It now remains available beside Play, Now, rate and Place; the transport uses the phone's full usable width.
- **Should fix, family: wheel endpoints.** Date Home/End incorrectly changed time of day. They now reach January 1/December 31, preserving clock time, with the correct leap-year range and announcements.
- **Should fix, family: input truth.** Committed out-of-range or blank year/coordinate fields could contradict the model while focused. Reconcile immediately; year changes preserve civil time and clamp February 29 safely.
- **Should fix, family: civil-day bounds.** Horizon-event scans assumed 24 hours, potentially dropping/adding Moon events on daylight-saving dates. Scan from this local midnight to the next, including 23/25-hour home dates.
- **Should fix, family: local year limits.** UTC limits could leave the local-year odometer beyond its own range near the date line. Clamp the displayed local calendar to 3000 BC through AD 3000, including after place changes; stop transport at the boundary.
- **Should fix, family: equatorial grid.** The grid was precessed a second time despite being labelled in current-date RA/DEC. Draw it directly in the date frame used by the readouts.
- **Should fix, family: rendering cost.** Cache the observer basis, date precession, star unit vectors and daily Milky Way geometry, avoiding repeated transforms and per-star allocations. All catalogue rows, original drawn stars/glows, colours and object access remain. Pixel/angle parity was checked at both FOV ends and five latitudes; measured performance and remaining qualification limits are below. A sprite-atlas experiment was slower and was removed.
- **Should fix, family: city ambiguity.** Same-country Suzhou/Yulin entries were indistinguishable. Sourced coordinates disambiguate the retained choices. No city locations invented.
- **Should fix, family: Moon appearance.** Fixed halo and dark disk made a thin daytime crescent look like an occulting black object. Shadow blends into local sky; glow follows illuminated fraction. Preserved computed phase and Sun-facing orientation.
- **Should fix, family: pinch handoff.** Rebase the remaining pointer after the second finger lifts, avoiding a pan jump.
- **Polish, family: weak ancient-pole moment.** Rim now names the closest named star to the hemisphere's pole. At 2800 BC it shows Thuban and 0.1 degrees; the Manual explains that a close pole star need not exist.
- **Should fix, general: sky-label contrast.** Twilight colours could reduce contrast. Opaque dark glyph outlines now preserve the label contrast across the sky ramp.
- **Polish, family: label crowding.** Deep-sky labels share star/telemetry collision reservations; all markers and keyboard access remain.
- **Should fix, general: audit-frame clipping.** Names such as Arcturus/Shaula were cut by the oval canvas clip despite passing rectangular bounds. Require every label corner inside the oval, with a left-side alternative for star labels. Reshoot affected layouts after the audit; retain every star/marker.

## Findings left

- **Verification limit, spec 7 still unqualified:** actual school-Chromebook 60 fps and physical touch-device qualification remain unavailable. Desktop draw median/p95 is 4.2/4.9 ms and frame intervals 16.7/16.7 ms. Fourfold CPU stress draw median improved from 28.0 to 19.95 ms, but cadence remains about 15 fps. That synthetic stress result is not a 60 fps pass or a Chromebook certification; further hardware-specific rendering work remains open.
- **Disclosed material limits:** incomplete device-zone inference, 2022 name snapshot, 14 sourced stellar distances, no planet magnitude model and approximate ancient Moon/Earth rotation. Manual states these limits; no invented measurements added.

## Break it

No score, check, quiz, progression or finish exists. Sun/Moon/object readouts were tested as measurements, with external numerical references rather than a passing strategy.
Year -2999/-2799/0/1/2026/3000 crossed with latitudes -90/0/90 stayed finite. Longitude endpoints, empty and excessive numeric input, 20/180 degree FOV, both directions, all rate detents, all levers both ways, rapid clicks, city rejection and duplicate-city selection were exercised. Endpoint/field contradictions were repaired and retested.
Motion off: repeated held Play steps once per press and remains stopped. Date endpoint tests preserve 12:30 and yield day 1/day 366 in 2024. Real pointer-ring and keyboard paths work. Running-resize and final audit results are recorded below.
Lesson-creep search: remaining hits are geometric `points`, `minute-level` precision and an honesty note saying the snapshot is not the `complete` current list. No lesson or reward mechanic remains.

## Voice walk

Held Play -> Lines -> Names off/on -> Read, two-second gaps: `Drag the time dial.` once, followed only by the explicit Read's date, time, place and Moon illumination. Real dial drag separately speaks the same hint once. Read freezes the reported sky.

| Line | Kind | Expected | Observed |
| --- | --- | --- | --- |
| Drag the time dial | first instrument hint | 1 | 1 on Play and drag fresh pages |
| Read sky, Sound off | explicit reading | 5 | 5 |
| Lever/date/transport actions | unsolicited commentary | 0 after hint | 0 |

No recorded voice was supplied. Chrome was muted as required; logs establish dispatch and timing, not acoustic quality. Fixed line matches voice/lines.json and allLines; variable readings use live values.

## Facts checked

All review fetches: **2026-11-05 local date**. Raw review responses and exact URLs are in `../../_scratch/sky-dome/data/review/manifest.json`; preserved build raw sources remain in `data/second/`. Independent scripts/results are `review_verify.py`, `review-static.json`, `review_numbers.py` and `review-numbers.json`.

- **Stars:** [Yale BSC5 / NASA HEASARC](https://heasarc.gsfc.nasa.gov/W3Browse/star-catalog/bsc5p.html), [NASA licence](https://data.nasa.gov/dataset/bright-star-catalog): US Government Works/public domain. Rechecked all 9,096 packed stellar rows, magnitude, proper motions and 8,786 B-V values against primary raw data; 14 nonstellar entries excluded. Maximum coordinate quantisation/source difference 0.000065 degrees. CDS/CfA is a separate distribution of the same observations, not independent observations.
- **Star positions:** ten stars independently rotated/precessed in Python, including proper motion, agree far inside 0.1 degrees. This verifies implementation, not the physical accuracy of a repeated precession formula.
- **Names:** [IAU WGSN snapshot](https://github.com/mirandadam/iau-starnames/blob/master/catalog_data/IAU-CSN.txt), 333 HR matches, 2022-04-04. Header says Creative Commons Attribution without version; [current IAU policy](https://www.iau.org/IAU/Iau/Copyright.aspx) specifies CC BY 4.0 for web texts. Credited, selection and snapshot disclosed; no etymologies copied.
- **Places:** [Natural Earth](https://www.naturalearthdata.com/about/terms-of-use/), public domain; [Wikidata](https://www.wikidata.org/wiki/Wikidata:Licensing), CC0 verification. Rechecked all 1,238 retained coordinates against raw source. Thirteen source entries remain omitted. Corrected [Maradi Q664550](https://www.wikidata.org/wiki/Q664550), preserving [Niamey Q3674](https://www.wikidata.org/wiki/Q3674). City-centre and time-zone inference are explicitly estimates.
- **Figures:** [Olaf Frohn d3-celestial](https://github.com/ofrohn/d3-celestial/blob/master/data/constellations.lines.json), BSD-3-Clause, the explicit spec fallback. All 88 figures retained, 893 endpoints mapped to Yale; full licence preserved. [IAU](https://www.iau.org/IAU/Astronomy-FAQs/Constellations.aspx) defines areas, not unique stick figures. No share-alike Stellarium data used.
- **Deep sky:** [HEASARC Messier](https://heasarc.gsfc.nasa.gov/W3Browse/general-catalog/messier.html), [US Government Works licence](https://data.nasa.gov/dataset/messier-nebulae). Twenty lowest catalogue magnitudes; every packed centre and magnitude rechecked. Secondary [SEDS](http://messier.seds.org/data.html) values are factual numbers only, no protected prose/images. Differences remain ranges; M41's 14-arcminute centre discrepancy is disclosed.
- **Distances and colour:** 14 NASA fact-page numbers checked against retained primary/secondary evidence, with trigonometric Yale checks where applicable. [Sirius](https://science.nasa.gov/asset/hubble/the-dog-star-sirius-and-its-tiny-companion/) is about 8.6 ly; Yale magnitude -1.46. Betelgeuse B-V +1.85/Rigel -0.03 match Yale. NASA factual material is public domain; no APOD art copied. Hipparcos CC BY-NC catalogue is excluded. [Ballesteros 2012](https://arxiv.org/abs/1201.1809) is independently implemented mathematics, not reproduced paper text/art; estimates and colour limits are labelled. [NASA Chandra](https://wwwastro.msfc.nasa.gov/solar/chandra101/variable_stars/mag.html) and [NASA Space Math](https://spacemath.gsfc.nasa.gov/news/6Page135.pdf) confirm five magnitudes = 100 in received light. [NASA's Sun sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html) confirms -26.74; the readout now labels it nominal.
- **Planets:** [JPL Standish/Williams](https://ssd.jpl.nasa.gov/planets/approx_pos.html), factual numerical elements and independently implemented mathematical methods, no source prose/code copied. Five preserved DE441 Horizons references at 2026-11-05 00:00 UTC independently compared: Mercury 0.00282, Venus 0.00370, Mars 0.00348, Jupiter 0.02645, Saturn 0.08127 degrees.
- **Solar events:** fresh [USNO](https://aa.usno.navy.mil/data/RS_OneDay) government/public-domain numerical responses. June 21 Denver 05:32/20:31 MDT; December 21 07:17/16:39 MST. Model maximum rise/set error 0.525 min; daylight 899.304/561.281 min, errors +0.304/-0.719 min. The formerly open named-source check now passes.
- **Moon:** fresh [USNO primary phases](https://aa.usno.navy.mil/api/moon/phases/date?date=2026-11-01&nump=4), government/public-domain facts. November 9 07:02, 17 11:48 and 24 14:53 UTC: new/quarter/full, 0/50/100 percent, ages approximately 0.0/8.2/15.3 days. Independent Meeus-style code uses mathematical methods without copied book prose/code. Ancient accuracy is explicitly approximate.
- **Discovery notes:** [USNO sidereal time](https://aa.usno.navy.mil/faq/GAST) gives about 86164.09 s/day and 235.91 s earlier daily; [NASA Polaris](https://science.nasa.gov/solar-system/what-is-the-north-star-and-how-do-you-find-it/), [NASA Thuban](https://svs.gsfc.nasa.gov/13512), [NASA lunar motion](https://www.nasa.gov/solar-system/why-can-you-see-the-moon-during-the-day-we-asked-a-nasa-scientist-episode-19/), [NASA Venus geometry](https://pwg.gsfc.nasa.gov/stargaze/Skepler3(op).htm) and [NASA Mars retrograde](https://science.nasa.gov/image-article/apod-2018-november-8-mars-in-the-loop/) support the factual paraphrases. US Government factual material, no copied prose/images. Thuban's computed 2800 BC offset is 0.0916 degrees. Milky Way and horizon remain explicitly illustrative drawings, not measured images.

## Sensitivity

No cultural narratives, etymologies or people imagery are included. IAU names are credited identifiers and constellation figures explicitly modern conventions. Cultural sky stories stay omitted, as the spec leans; any future stories need their own fresh sensitivity review. The geographic name error is fixed rather than disguised.

## Short test

- **Kid opens it unassigned:** yes, provisionally. One turn changes the real sky; selection reveals measurements without a required reading path. Grade 1 remains teacher-operated as specified.
- **Adult plays for fun:** yes. Seasons, Moon geometry, planetary trails and the changing pole sustain comparisons beyond the opening wheel.
- **Real material is the interface:** yes. The catalogue, computed positions, illuminated Moon and changing horizon are the working surface; they remain dominant after fixes.
- **Works without score/finish:** yes. No goals, levels, quiz, finish, kit header or game layer was added.

| Sky Dome, fresh review frame | Elements Inspector, fresh cold model frame |
| --- | --- |
| ![Sky Dome](../../_scratch/sky-dome/review-rim-fixed/post-audit-voice.png) | ![Elements Inspector](../../_scratch/sky-dome/review-cold/model-elements.png) |

Both have dense real material and instrument controls. Sky Dome keeps its own observatory palette and full-screen scene.

## Flattest moment left

Daylight can leave a nearly empty blue dome. That is an honest consequence of time and place; a turn of the time ring reveals the stars. The repaired thin crescent and dynamic pole readout make the quieter observations more rewarding without adding a game.

## Graphics

Zero painted/people images or placeholders. Inspected cold desktop, night, day, both poles, selected-object, Manual, keyboard, phone Place, grayscale and Motion-off frames, plus all 25 final audit PNGs. Original sky density, brass controls and palette retained. All eight post-audit rim-label viewport checks have zero glyph-corner violations, with their frames inspected; real South Pole and voice frames also inspected. Final bundle: **532,025 bytes, about 520 KiB**, below the spec's 600 KB target. Contrast: control 11.17:1, plate 7.08:1, captions 6.99:1; outlined sky text 10.50:1 or better against its dark outline.

## Audit

One complete audit, exit 0, Chrome 9951/host 8755, under the 40-minute limit: `../../_scratch/sky-dome/review-audit/audit.md`. All eight sizes clean; no perpetual motion, resize exceptions, stuck disabled controls or held-control/keyboard errors. Nineteen fresh-page control walks and the five-held/two-rapid checks are clean.
All five leads flag the first hint being hidden after instrument action, required by CODEX-CURIOSITY. No lesson welcome is expected; `Drag the time dial.` is the only automatic hint. The apparent stale city field in the synthetic southern fixture came from bypassing the real city control; the fixture now uses the city change path, checked separately.
The audit frames confirmed canvas-name clipping; corrected only that placement and the observed singular Read wording afterward, then re-shot affected sizes and re-walked voice. No second audit or full review was run.

## Brief/spec checks

- **1, 2, 3:** tested Denver home opening PASS with no permission request; ten stellar and five planetary comparisons PASS; fresh USNO solstice comparisons PASS. Universal home-zone coverage is not claimed.
- **4, 5:** three USNO lunar phases/ages and same-time seasonal stepping PASS; 2800 BC Thuban offset 0.0916 degrees PASS.
- **6, 8, 9:** tested keyboard/control paths and 60 px primary targets PASS; eight layouts and plate/Manual placement PASS; Motion-off steps and contrast PASS. Physical pinch qualification remains unverified.
- **7:** desktop cadence PASS in the measured window; school-Chromebook qualification **NOT PASSED**, with the below-target fourfold stress result explicitly retained above.
- **10, 11, 12:** offline/no runtime requests and credited material PASS; the short test passes as a reviewer proxy, with the model comparison; no score, goal, level, quiz, finish or kit header PASS.

## Left open

Hardware/acoustic/physical-touch validation and disclosed catalogue/model limits above. No plan.md was requested or added; this review does not authorize replacing the anchor lesson card. No questions were asked in this unattended session; spec lean retained omission of cultural stories and NASA distance fallback.
Initial 100-second async-JS observation attempts exceeded the shared driver's 60-second reply limit and do not count. Replacements use bounded observation waits and recorded intervals. Early read-only file inspection lacked a separate kill timeout; substantive browser, bundle, download and audit processes were explicitly bounded. All authored edits stay in the two permitted folders; shared scripts/kit are unchanged and no git commits were made. All started browsers/servers are closed: ports 9950, 9951 and 8755 verified not listening, with no tool-folder host.html. The corrected packer is deterministic. Final hashes and checks are in `review-final-manifest.json` in Scratch.

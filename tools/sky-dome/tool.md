# sky-dome: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: sky-dome (Curiosity No. 05)

#### Built

Second Build, Cory's decision of 2026-11-05. The full-screen observatory, brass rings, projector transport, sky camera, setting circle, rim levers, astronomical engine, lower-left plate, Manual and separate Motion / Sound / Read power panel are retained. `sky-dome.html` is the single offline deliverable; `src.html` and `sky-data.json` are its editable sources.

Changed from the first build:

- Replaced the incomplete institutional star export with the full required Yale fields: all 9,096 stellar rows, 8,786 measured B-V values, position, magnitude, proper motion, spectra and uncertainty / variable flags. Star colours now use a continuous B-V ramp; colour temperature is available throughout its valid range.
- Replaced 48 approximate places with 1,238 checked Natural Earth places, country-qualified search choices and 302 source-derived home-zone names / aliases. Accent-insensitive short names work when unique. Four mathematical reference settings remain available.
- Replaced 15 figure sketches with all 88 conventional constellation figures. The listed d3-celestial fallback is used, including its full BSD notice in the Manual. Serpens' two parts share one figure identity.
- Added 20 real Messier markers, selectable by pointer and by J / Shift J. Their readouts show source magnitude ranges where the two catalogues differ.
- Expanded two distances to 14 checked NASA fact-page distances. ESA's stated noncommercial catalogue licence triggers the specification's fact-page fallback.
- Retrieved and passed the five missing JPL Horizons checks; independently checked Denver solstice events against JPL altitude crossings.
- Re-solved the previous lunar conjunction when a root crosses the cycle boundary. The displayed 0.1-day age explicitly reads approximately zero near conjunction, rather than presenting a precision-dependent cycle wrap as an exact answer.
- Reused projected star records and coordinate slots to reduce per-frame allocations. Live rendering was measured separately from the artificial tight-loop stress test.
- Kept the long sky-object list out of ordinary Tab order, with deliberate entry through Dome. Reserved card clearance below the top telemetry and above the bottom rim. Catalogue flags now say “variability listed”, including suspected entries, rather than asserting confirmed variability.

Build only: no commits, deployment, shared-file edits, sub-agents or polish round. Writes are confined to `tools/sky-dome/` and `_scratch/sky-dome/`. `codex-report-1.md` is preserved. The final report is deliberately written last because its creation is the user's stop trigger. The initial read-only inspection completed immediately without an explicit timeout wrapper; subsequent shell commands and downloads have explicit bounds.

#### The real material

All fetches are dated **2026-11-05**. Gathering ran from 22:39 to 23:05 UTC, inside the authorized 75-minute cap. Raw files, source URLs, hashes, failed routes, per-record comparisons and sampling decisions are in `_scratch/sky-dome/data/second/`. The reproducible offline packer is `pack2.py`; `verify_static2.py` confirms that rerunning it leaves the packed hash unchanged. B-V missing values remain missing, rather than becoming zero.

- **Stars:** Hoffleit & Warren, Yale Bright Star Catalogue, fifth revised edition. [Full HEASARC distribution](https://heasarc.gsfc.nasa.gov/FTP/heasarc/dbase/tdat_files/heasarc_bsc5p.tdat.gz), [NASA licence record](https://data.nasa.gov/dataset/bright-star-catalog): US Government Works / public domain. Checked every required field against the [independently maintained CDS distribution at Harvard CfA](https://vizier.cfa.harvard.edu/viz-bin/asu-tsv?-source=V/50/catalog&-out=HR,RAJ2000,DEJ2000,Vmag,B-V,pmRA,pmDE&-out.max=unlimited). All 9,096 stellar rows are kept; 14 blank or non-stellar HR entries are excluded. All 8,786 measured colours agree exactly, as do magnitude and proper motion. Coordinate rounding differs by at most 0.000067 degrees. These are two catalogue distributions of the same underlying observations, not independent observations. Evidence: `star-crosscheck.json`.
- **Names:** [IAU WGSN Catalog of Star Names](https://github.com/mirandadam/iau-starnames/blob/master/catalog_data/IAU-CSN.txt), 2022-04-04 snapshot. Its own header states Creative Commons Attribution, without a version. All 333 HR-matched names are rebuilt from the raw fixed-width file. No cultural narratives or etymologies are bundled.
- **Places:** [Natural Earth 1:50m populated places](https://www.naturalearthdata.com/downloads/50m-cultural-vectors/50m-populated-places/), [official raw archive](https://naciscdn.org/naturalearth/50m/cultural/ne_50m_populated_places_simple.zip) and [maintained full GeoJSON](https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_50m_populated_places.geojson). [Terms](https://www.naturalearthdata.com/about/terms-of-use/): public domain. Each retained centre is checked against its separate [Wikidata P625 record](https://www.wikidata.org/wiki/Wikidata:Licensing), CC0. Retain 1,238 of 1,251 entries, with agreement within 0.25 degrees; 1,226 agree within 0.1 degrees. Seven missing and six conflicting centres are dropped. The source's own TIMEZONE fields supply the zone associations. IANA was investigated but is not bundled. Evidence: `place-crosscheck.json`, `place-omissions.json` and raw Wikidata batches.
- **Figures:** [Olaf Frohn, d3-celestial constellation lines](https://github.com/ofrohn/d3-celestial/blob/master/data/constellations.lines.json), [BSD 3-Clause licence](https://github.com/ofrohn/d3-celestial/blob/master/LICENSE), explicitly listed as the spec fallback. All 88 identities are checked against the [IAU list](https://www.iau.org/IAU/Astronomy-FAQs/Constellations.aspx), whose chart terms state CC BY 4.0. All 893 endpoint occurrences match Yale positions within 0.002530 degrees and are converted to HR paths. The IAU archive failed; several mirrored chart SVGs were recovered for reference, but there is no claim of a new tracing or independent verification of an official connectivity. The IAU does not prescribe stick figures. The two-source check covers every astronomical endpoint and every figure identity. Full attribution and BSD conditions are in the Manual. Evidence: `figure-crosscheck.json`.
- **Deep sky:** [NASA HEASARC Messier Nebulae](https://heasarc.gsfc.nasa.gov/W3Browse/general-catalog/messier.html), from Hirshfeld & Sinnott (1985); [NASA licence record](https://data.nasa.gov/dataset/messier-nebulae): US Government Works / public domain. The 20 lowest-magnitude rows are kept. Each position and identification is checked against [SEDS Messier Objects with Data](http://messier.seds.org/data.html), Hartmut Frommert and Christine Kronberg. Only factual numbers and plain identifications are reproduced, with no SEDS prose or images. Nineteen centres agree within 0.000172 degrees; M41 differs by 0.234 degrees, or 14 arcminutes, within the cluster's 38-arcminute extent. Its marker uses the HEASARC centre and the discrepancy is explained. Magnitude disagreements are displayed as the two source estimates, not silently averaged. Evidence: `deep-crosscheck.json`.
- **Distances:** The specified NASA fact-page fallback covers Achird, Altair, Arcturus, Betelgeuse, Capella, Castor, Fomalhaut, Pollux, Procyon, Ran, Rigil Kentaurus, Sirius, Toliman and Vega. NASA / public-domain factual numbers; no article prose or pictures are bundled. Primary routes: [nearby stars](https://imagine.gsfc.nasa.gov/features/cosmic/solar_neighborhood_info.html), [Vega](https://www.nasa.gov/missions/dart/nasas-dart-captures-one-of-night-skys-brightest-stars/), [Altair](https://science.nasa.gov/image-article/apod-2015-june-27-stars-of-a-summer-triangle/), [Arcturus](https://science.nasa.gov/resource/whats-up-june-2023-skywatching-tips-from-nasa/), [Gemini](https://science.nasa.gov/solar-system/skywatching/night-sky-network/gemini-constellation/), [Capella](https://science.nasa.gov/image-article/apod-2021-february-6-a-northern-winter-night/), [Alpha Centauri](https://science.nasa.gov/missions/hubble/hubbles-best-image-of-alpha-centauri-a-and-b/), [Fomalhaut](https://science.nasa.gov/missions/hubble/hubble-directly-observes-a-planet-orbiting-another-star/), [Betelgeuse](https://science.nasa.gov/missions/hubble/nasa-hubble-helps-detect-wake-of-betelgeuses-elusive-companion-star/) and [Sirius](https://science.nasa.gov/asset/hubble/the-dog-star-sirius-and-its-tiny-companion/). Each has a second publication or an older Yale trigonometric parallax check; the latter must agree within 8 percent. These are approximate distances, not new precision measurements. Exact source pairs and numerical comparisons are in `distance-checks.json`. [ESA's catalogue page](https://www.cosmos.esa.int/web/hipparcos/catalogues) states CC BY-NC 3.0 IGO; its catalogue is not redistributed.
- **Planets, Sun, Moon and coordinate rules:** [JPL Standish / Williams element tables](https://ssd.jpl.nasa.gov/planets/approx_pos.html), numerical facts and independently implemented formulas; Jean Meeus, *Astronomical Algorithms*, independently written mathematical methods, with no copied book prose or code. Five DE441 Horizons responses and the two solar altitude series are retained as independent numerical references. [USNO](https://aa.usno.navy.mil/data/RS_OneDay) and NASA are credited for the Manual's sidereal, pole, lunar-motion and planetary explanations. The original build's USNO phase reference dates are retained as historical reference, not presented as a fresh download.
- **Colour temperature and display colour:** [Ballesteros (2012)](https://arxiv.org/abs/1201.1809), mathematical formula independently implemented; no paper text or artwork copied. The Manual states its rough nature, reddening / supergiant / multiple-system limitations and the supported B-V interval of -0.4 to +2.0. The continuous screen-colour ramp is an illustrative representation of measured B-V, with spectral fallback only for the 310 missing values. The Milky Way remains an explicitly drawn galactic band, not photographic data.

#### Break the instrument

- All 18 combinations of six years (-2999, -2799, 0, 1, 2026, 3000) and three latitudes (-90, 0, 90) stayed finite. Field-of-view endpoints, polar horizons, rapid pointer movement and the retained instrument controls were exercised. No blank sky caused by a numerical exception. All 9,096 star colours are valid RGB values.
- A real jittered time-ring drag changed the sky; real Left and Shift Right stepping produced 22:10 from 21:00. Real J, J, Shift J returned to M45. The original shared drive has no letter-key mapping; the successful retry uses a Scratch adapter, with shared files unchanged.
- Empty place input preserves the previous site and announces an invalid entry. Country-qualified São Paulo selects its source coordinates. The phone Place sheet opens with focus on the city input and 1,242 available choices, including the four reference settings.
- Motion off: two held Play presses step time; an additional 1.2 seconds leaves it unchanged and `playing` false. The Manual and phone Place open through real Enter presses. All focused completed tool tests report zero browser console errors / warnings / exceptions.
- Live desktop headless rendering, with all stars, lines and trails, has 120 measured draws: median 6.0 ms, 95th percentile 7.0 ms, maximum 7.9 ms. Across 239 animation intervals, median 16.7 ms, 95th percentile 16.8 ms, maximum 33.3 ms. This supports ordinary desktop use; it is not a school-Chromebook result. An artificial synchronous redraw loop produces batching stalls around 50 ms and is preserved as a stress result rather than an FPS claim.
- The standalone file and the 375-pixel inner document each report zero resource requests. The phone width is genuinely 375, with body scroll width 375. No `host.html` is left in the tool directory.

#### Voice walk

Bank `calm-professor`, requested voice `Schedar`, with the specified quiet planetarium-presenter style. No audio was recorded. The shared kit uses browser speech fallback, so an acoustic claim about the bank voice is not made.

Held inputs at two-second gaps produce one spoken hint when Manual is the first gesture; later instrument actions remain silent. Read reports the current date, time, place and selected magnitude or Moon phase, including with Sound off. The colour-and-distance walk speaks Betelgeuse, magnitude 0.50. No late hint interrupts that reading. Logs: `voice2-result.json` and `walk2-3.json`. The browser was muted as required; listening quality remains unverified.

#### Short test

Six valid 100-second observation windows total ten minutes, with real held controls, a real drag, keyboard input, time transport, seasonal stepping, a southern site, colour / distance inspection, trails and the ancient pole. The same walk is judged from the grade-1 teacher-operated perspective and the adult perspective. This is an unattended agent proxy, not a child usability study. Two earlier timed-harness attempts were discarded because their sequencing was wrong; only the six successful replacement windows count.

- Would a kid open it unassigned? **Yes, provisionally.** The rings and changing sky give an immediate reaction with one quiet hint. A daylight opening shows the Sun first, and moving time reveals the stars.
- Would an adult use it for fun? **Yes.** The complete figure set, actual colours, wider place search, measured object fields, planetary trails and ancient pole keep providing comparisons beyond the initial turn.
- Is the real thing the interface? **Yes.** Yale stars, actual catalogue measurements, computed sky positions and checked Messier centres are the working surface.
- Does it work without a score or finish line? **Yes.** It stays an open observatory with every control available.

![Sky Dome beside Elements Inspector](../../_scratch/sky-dome/second-comparison.png)

The new dome has the model tools' whole-screen density and instrument confidence, with its own observatory material. The four approved model tools were reopened and used before implementation; their frames are retained in `second-models/`.

#### Lesson creep check

Searched `src.html` and `voice/lines.json` for score, points, level, goal, sticker, badge, correct, wrong, try again, complete and well done. Eight remaining “points” occurrences name geometric data or trail samples. “Minute-level” describes timing uncertainty in the Manual. None is lesson or game language. No score, goal, level, reward, quiz, finish screen, mode pills or kit header is present. No em dash in authored source.

#### Done when

1. **PASS for the tested Denver opening; FAIL for universal zone coverage:** America/Denver opens over the sourced Denver centre, with no welcome or permission request. Natural Earth supplies 302 zone associations / aliases, with an additional unique city-name match. Unrecognised zones remain explicitly labelled estimates, rather than a claimed geolocation. Manual coordinates work anywhere, but the default city is not guaranteed for every possible device zone.
2. **PASS:** ten date-precessed star positions agree with the separate Python rotation implementation far inside 0.1 degrees; their source distributions agree within 0.000067 degrees. The five independent JPL Horizons errors are Mercury 0.00282, Venus 0.00370, Mars 0.00348, Jupiter 0.02645 and Saturn 0.08127 degrees. ICRF references are precessed to the instrument's date frame before comparison. Evidence: `numeric-verification2.json`.
3. **FAIL for the exact requested USNO reference:** the USNO API and calculated-page routes remained unavailable after bounded attempts. Independent JPL solar crossings do pass: summer rise / set differ by +0.78 / +1.44 seconds, winter by -0.67 / +2.00 seconds. Evidence: `solar-verification2.json`. The model is checked; the named USNO-table acceptance check is still open.
4. **PASS at displayed precision against the retained reference:** the first build recorded USNO new / quarter / full times of 2026-11-09 07:02, 11-17 11:48 and 11-24 14:53 UTC. The current readouts are New Moon / approximately 0.0 d, First quarter / 8.2 d and Full Moon / 15.3 d. LIT rounds to 0, 50 and 100 percent. The numerical new-Moon root is still about 93 seconds after that published minute, which is explicitly below the displayed age precision. Same-time stepping preserves the displayed local clock and shows seasonal drift. This does not claim a refreshed USNO fetch.
5. **PASS:** astronomical year -2799, meaning 2800 BC, puts Thuban 0.09163 degrees from the pole.
6. **PASS for tested input paths:** accessible names / values and keyboard controls are retained; new deep-sky selection works with real J / Shift J. Main time, date, year and Play targets are at least 60 pixels; secondary controls at least 44. Phone modal focus, Enter and closing paths pass. No physical touch-device test is claimed.
7. **FAIL for hardware qualification:** live desktop cadence is about 60 Hz, with 6.0 / 7.0 ms median / 95th-percentile draws. No school Chromebook or established equivalent profile was available. That hardware-specific requirement remains unverified.
8. **PASS:** the single audit covers 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and the 375x812 iframe. The plate and Manual stay lower-left and main controls remain visible. The final selected-card follow-ups reserve 20 pixels above the short-preview rim and 19 pixels above the phone rim, with its top below the Moon strip. Tall cards scroll.
9. **PASS:** Motion off never advances time automatically. Contrast ratios: cream on control 11.17:1; muted on night 9.39:1; plate 7.08:1; control labels 6.99:1. Grayscale frame inspected.
10. **PASS:** one offline file, zero runtime resource requests, sources and licences in both Manual and `tool.draft.json`, full BSD notice retained. The bundle is **524,294 bytes**, below the 600 KB spec goal and the 2 MB general goal.
11. **PASS, provisional agent judgement:** the ten-minute proxy walk, four answers and fresh frame comparison are retained. No human-participant or acoustic validation is claimed.
12. **PASS:** no game or lesson gates, reward system, mode pills or finish screen.

#### Audit leads

One full audit, including held-control and speech stress walks, completed on Chrome 9981 and host 8785. It reports **259 mechanical leads** and saves 22 frames. The dispositions below cover all 223 overlap leads, 32 hidden-text leads and four missing-hint leads.

- Canvas under telemetry, rim controls, readout contents and object cards: intentional whole-screen instrument composition. The canvas carries astronomical graphics, not a page of prose hidden underneath another panel. Parent wheel controls and their engraved labels intentionally share their geometry.
- Manual coverage of the dome, HUD and view buttons: intentional native modal coverage. The scrollable Manual keeps a sticky Close button; focus is contained and returns on closing. The phone Place sheet likewise makes its background inert and returns focus on closing.
- Selected-object coverage of sky graphics and star labels: intentional inspector overlay. View buttons are hidden while a card is open; sky-wheel and keyboard zoom remain available.
- The actual short-preview view-readout collision was fixed by reserving bottom clearance for the rim at all three card breakpoints. Final focused boxes have 20 pixels of clearance in the 680x425 preview and 19 pixels on the phone. The phone card was also moved below the full Moon telemetry line. These affected views were re-shot and inspected.
- Missing first-action hint: required disappearance after an action, not lost guidance. Read speaks the current sky. “Welcome not heard” in the generic walk is expected because this Curiosity has no welcome or mode introduction.
- All 20 fresh-page held-control walks report an okay result and okay Enter path, with no other control jumping. The Manual / Read five-tap speech checks and Manual quick-tap check are clean. Motion off reports no perpetual motion; resize checks report no exceptions or stuck disabled controls.
- Follow-up keyboard checking keeps ordinary Tab out of the 30-object list: five Tabs reach the date wheel with no card opened. Dome deliberately focuses the canvas; Tab and Enter then select Saturn. Real J / Shift J were separately verified. The variability note was made conservative, and the Manual explicitly names the unmodelled planet magnitudes.

The full audit snapshot precedes those final card-clearance, keyboard-entry and honesty-copy fixes. Its original report is preserved, and only the affected views / paths received focused checks in `second-final-focus/`, `second-card-final/` and `second-phone-final/`. There was no second full audit or polish round. The mechanical lead count is not presented as a clean-audit verdict.

#### Frames looked at

The four model frames; all four initial second-build frames; the deep-key retry; all six focused frames; three actual-width phone frames; the tight-loop and live-cadence frames; all six successful timed-walk frames; and every final audit PNG, individually or on contact sheets. Original frames and sheets stay in `_scratch/sky-dome/`. Focused follow-ups, if any, are listed with the audit dispositions.

#### Art made

Zero painted images, placeholder images or outside photographs. Canvas draws the actual sky, catalogue symbols and measured connections; CSS and SVG draw the instrument and rings. The art manifest explains this choice. Screenshots and source-chart references are evidence in Scratch, not bundled artwork.

#### Engine changes wanted

None. No shared kit or script was edited. The Scratch drive adapter adds letter keys and a post-observation result hook for these checks; the ordinary audit uses a direct M31 setup because its key map also lacks J. Real J selection was tested separately.

#### Left open

- The exact USNO solstice-table comparison, and refreshing the historical USNO phase reference. Independent JPL planet and solar checks are complete.
- Universal device-zone city inference and planet apparent magnitudes remain outside the retained material. Unrecognised zones are labelled estimates; planet MAG says “not available”, and the navigation list prioritises solar-system bodies before catalogue-ranked stars. Both limits are stated in the Manual.
- Actual school-Chromebook and physical touch-device qualification; recorded voice and acoustic listening verification.
- Approximate ancient Moon / Earth-rotation accuracy and the minute-scale lunar conjunction boundary. The Manual states these limits and makes no telescope-pointing or eclipse-prediction claim.
- The 13 omitted place entries are documented, with no guessed replacements. Further distance measurements require the same licence and two-source checks; the present 14-star fallback is functional and explicit.
- Cultural sky stories remain omitted as the spec advises. No teacher `plan.md` is supplied, so this Build does not authorise replacing the anchor lesson card.

All browsers and servers started by this Build were closed before this report was written. No approval or unanswered question remains for this unattended Build.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: sky-dome

#### Played

Cold play preceded builder report, handoff, notes and source. Grade 1 teacher-projector, grade 5 solo and adult perspectives, using held clicks, a jittered ring drag, keyboard navigation, sky selection and long observation windows. This is an unattended reviewer proxy, not a child usability study.
Instrument time exceeded ten minutes: six 90-second windows plus at least 73.42 seconds of held-input/voice observation, excluding loading and Chrome startup. There are 108 recorded sky states; `review-summary.json` gives a conservative total of 613.5 seconds.
The night wheel, dense catalogue and brass deck invite exploration. Kept their confidence, colour and density.

#### Findings fixed

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

#### Findings left

- **Verification limit, spec 7 still unqualified:** actual school-Chromebook 60 fps and physical touch-device qualification remain unavailable. Desktop draw median/p95 is 4.2/4.9 ms and frame intervals 16.7/16.7 ms. Fourfold CPU stress draw median improved from 28.0 to 19.95 ms, but cadence remains about 15 fps. That synthetic stress result is not a 60 fps pass or a Chromebook certification; further hardware-specific rendering work remains open.
- **Disclosed material limits:** incomplete device-zone inference, 2022 name snapshot, 14 sourced stellar distances, no planet magnitude model and approximate ancient Moon/Earth rotation. Manual states these limits; no invented measurements added.

#### Break it

No score, check, quiz, progression or finish exists. Sun/Moon/object readouts were tested as measurements, with external numerical references rather than a passing strategy.
Year -2999/-2799/0/1/2026/3000 crossed with latitudes -90/0/90 stayed finite. Longitude endpoints, empty and excessive numeric input, 20/180 degree FOV, both directions, all rate detents, all levers both ways, rapid clicks, city rejection and duplicate-city selection were exercised. Endpoint/field contradictions were repaired and retested.
Motion off: repeated held Play steps once per press and remains stopped. Date endpoint tests preserve 12:30 and yield day 1/day 366 in 2024. Real pointer-ring and keyboard paths work. Running-resize and final audit results are recorded below.
Lesson-creep search: remaining hits are geometric `points`, `minute-level` precision and an honesty note saying the snapshot is not the `complete` current list. No lesson or reward mechanic remains.

#### Voice walk

Held Play -> Lines -> Names off/on -> Read, two-second gaps: `Drag the time dial.` once, followed only by the explicit Read's date, time, place and Moon illumination. Real dial drag separately speaks the same hint once. Read freezes the reported sky.

| Line | Kind | Expected | Observed |
| --- | --- | --- | --- |
| Drag the time dial | first instrument hint | 1 | 1 on Play and drag fresh pages |
| Read sky, Sound off | explicit reading | 5 | 5 |
| Lever/date/transport actions | unsolicited commentary | 0 after hint | 0 |

No recorded voice was supplied. Chrome was muted as required; logs establish dispatch and timing, not acoustic quality. Fixed line matches voice/lines.json and allLines; variable readings use live values.

#### Facts checked

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

#### Sensitivity

No cultural narratives, etymologies or people imagery are included. IAU names are credited identifiers and constellation figures explicitly modern conventions. Cultural sky stories stay omitted, as the spec leans; any future stories need their own fresh sensitivity review. The geographic name error is fixed rather than disguised.

#### Short test

- **Kid opens it unassigned:** yes, provisionally. One turn changes the real sky; selection reveals measurements without a required reading path. Grade 1 remains teacher-operated as specified.
- **Adult plays for fun:** yes. Seasons, Moon geometry, planetary trails and the changing pole sustain comparisons beyond the opening wheel.
- **Real material is the interface:** yes. The catalogue, computed positions, illuminated Moon and changing horizon are the working surface; they remain dominant after fixes.
- **Works without score/finish:** yes. No goals, levels, quiz, finish, kit header or game layer was added.

| Sky Dome, fresh review frame | Elements Inspector, fresh cold model frame |
| --- | --- |
| ![Sky Dome](../../_scratch/sky-dome/review-rim-fixed/post-audit-voice.png) | ![Elements Inspector](../../_scratch/sky-dome/review-cold/model-elements.png) |

Both have dense real material and instrument controls. Sky Dome keeps its own observatory palette and full-screen scene.

#### Flattest moment left

Daylight can leave a nearly empty blue dome. That is an honest consequence of time and place; a turn of the time ring reveals the stars. The repaired thin crescent and dynamic pole readout make the quieter observations more rewarding without adding a game.

#### Graphics

Zero painted/people images or placeholders. Inspected cold desktop, night, day, both poles, selected-object, Manual, keyboard, phone Place, grayscale and Motion-off frames, plus all 25 final audit PNGs. Original sky density, brass controls and palette retained. All eight post-audit rim-label viewport checks have zero glyph-corner violations, with their frames inspected; real South Pole and voice frames also inspected. Final bundle: **532,025 bytes, about 520 KiB**, below the spec's 600 KB target. Contrast: control 11.17:1, plate 7.08:1, captions 6.99:1; outlined sky text 10.50:1 or better against its dark outline.

#### Audit

One complete audit, exit 0, Chrome 9951/host 8755, under the 40-minute limit: `../../_scratch/sky-dome/review-audit/audit.md`. All eight sizes clean; no perpetual motion, resize exceptions, stuck disabled controls or held-control/keyboard errors. Nineteen fresh-page control walks and the five-held/two-rapid checks are clean.
All five leads flag the first hint being hidden after instrument action, required by CODEX-CURIOSITY. No lesson welcome is expected; `Drag the time dial.` is the only automatic hint. The apparent stale city field in the synthetic southern fixture came from bypassing the real city control; the fixture now uses the city change path, checked separately.
The audit frames confirmed canvas-name clipping; corrected only that placement and the observed singular Read wording afterward, then re-shot affected sizes and re-walked voice. No second audit or full review was run.

#### Brief/spec checks

- **1, 2, 3:** tested Denver home opening PASS with no permission request; ten stellar and five planetary comparisons PASS; fresh USNO solstice comparisons PASS. Universal home-zone coverage is not claimed.
- **4, 5:** three USNO lunar phases/ages and same-time seasonal stepping PASS; 2800 BC Thuban offset 0.0916 degrees PASS.
- **6, 8, 9:** tested keyboard/control paths and 60 px primary targets PASS; eight layouts and plate/Manual placement PASS; Motion-off steps and contrast PASS. Physical pinch qualification remains unverified.
- **7:** desktop cadence PASS in the measured window; school-Chromebook qualification **NOT PASSED**, with the below-target fourfold stress result explicitly retained above.
- **10, 11, 12:** offline/no runtime requests and credited material PASS; the short test passes as a reviewer proxy, with the model comparison; no score, goal, level, quiz, finish or kit header PASS.

#### Left open

Hardware/acoustic/physical-touch validation and disclosed catalogue/model limits above. No plan.md was requested or added; this review does not authorize replacing the anchor lesson card. No questions were asked in this unattended session; spec lean retained omission of cultural stories and NASA distance fallback.
Initial 100-second async-JS observation attempts exceeded the shared driver's 60-second reply limit and do not count. Replacements use bounded observation waits and recorded intervals. Early read-only file inspection lacked a separate kill timeout; substantive browser, bundle, download and audit processes were explicitly bounded. All authored edits stay in the two permitted folders; shared scripts/kit are unchanged and no git commits were made. All started browsers/servers are closed: ports 9950, 9951 and 8755 verified not listening, with no tool-folder host.html. The corrected packer is deterministic. Final hashes and checks are in `review-final-manifest.json` in Scratch.

<!-- end part -->

## Refine

<!-- part: refine.md -->

PASS (exit re-check 2026-11-06, after Codex round 2: Done when 7 met with the GPU on; see last section)
Counts: blockers 1 (general 0, family 1), should fix 11 (general 8, family 3), polish accepted 14

### Refine: sky-dome

Merged from `refine/teaching.md`, `refine/play.md` and `refine/craft.md`. No sensitivity file (none needed, see Settled
calls). Lens frames live under `S:/CurioClass-codex-scratch/sky-dome/` (`teaching/`, `play/`, `craft/`, `audit-r1/`).
Integrator spot-checks (code read of src.html): the stretched projection (819-827, 1180-1181), the late hint (540-552),
the Sydney message (1291-1294) and Escape (1397-1398) are all as the lenses describe. The astronomy itself checked out
against JPL Horizons, SIMBAD and USNO (Teaching lens): do not touch the position, rise/set or phase math.

#### Blocker
1. **The dome stretches the sky, so star patterns are the wrong shape and change shape as they turn.** `src.html:819-827`
   (`projectVector`, and `fromScreen` just below) scales x by `rx` and y by `ry`, which `resize` (`src.html:1180-1181`)
   sets separately from width and height. At 1366x768 rx 621 and ry 233: 1 degree is 24.8 px across and 9.3 px down
   at every zoom, about 2.7 to 1; at 680x425 about 4.6 to 1. Orion is a flat smear (Betelgeuse to Rigel 393 px across,
   92 px down) and the Big Dipper is a long ladle at 22:00 and a tall one at 04:00, so spec Things to do 13 ("the same
   stars, turned") and the first reaction show distortion first. A planetarium whose patterns are wrong is a readout
   that lies; the Manual's "oval viewport" note does not cover it. Seen: `craft/orion-1366-fov50.png`,
   `play/f1/dipper-a.png` beside `play/f1/dipper-b.png`, every `audit-r1/size-*.png`. Fixed: one scale for both axes
   (min of rx, ry, or a true equal-scale view that fills the stage when zoomed in); the 180 degree dome and its brass
   horizon ring are round, with the spare width going to readouts or deck. `fromScreen`, tap hit-testing, labels,
   trails and the ring all use the same scale. Re-shoot Orion at FOV 50 and the Dipper pair. (family:curiosity)

#### Should fix
1. **No constellation is named anywhere.** `src.html:953` draws `figure.slice(1)` only; each figure's name
   (`DATA.figures[i][0]`) is bundled but never shown, and the object card has no constellation row. Spec Things to do 4
   (the Sun's constellation), 7 (the Southern Cross: Acrux and Mimosa labelled, nothing says Crux), 12 (Thuban "in
   Draco") and 13 (the Big Dipper) cannot be answered alone; with Lines on the dome shows 88 nameless figures. Seen:
   `teaching/out/noon-daylight-off-lines.png`, `play/f1/noon-nodaylight.png`, `audit-r1/state-running-1366x768.png`,
   `audit-r1/state-southern-sky-1366x768.png`. Fixed: a CONST row on the star, Sun, Moon and planet card, and faint
   figure names drawn while Lines (and Names) are on, placed so they do not crowd star labels. Real material, no game.
   (family:curiosity)
2. **60 fps fails on a Chromebook-class CPU (Done when 7).** `draw()` `src.html:926-951` sets `globalAlpha`,
   `fillStyle` and a separate arc path for each of about 4,600 stars, and every frame runs `querySelectorAll` and
   `getComputedStyle` for label boxes (983-986). Measured at 1366x768, Play 1 h/s, all on: 1x 7.0 ms median, 2x
   20.8 ms (48 fps), 4x throttle 34.7 ms (29 fps); stars alone cost 23.8 ms per draw at 4x (Craft lens, `perf.py`,
   `prof.py`). Fixed: batch stars by colour and alpha bucket into a few paths, or render the star field to an offscreen
   canvas per sidereal step and blit it; read overlay rects and the mono font once on resize. Target 4x throttle
   median at or under 16.7 ms. (general)
3. **The zoom buttons hide the W on the horizon ring.** `.view-tools` `src.html:52` (desktop), `:179` and `:195`
   (narrow) sit over the ring's west marker at the default whole-dome view at 1366x768, 1280x720, 1920x1080, 680x425
   and on the phone. West is where every star the student watches sets. Seen: `craft/w-marker-crop.png`,
   `audit-r1/size-1366x768.png`, `play/crop-phonedome.png`. Fixed: view tools clear of the ring (deck, or outside the
   round dome once Blocker 1 lands); all four letters visible at every checked size. (general)
4. **The spoken hint plays after the student already acted, with the on-screen hint gone.** Capture listener
   `src.html:546-552` queues "Drag the time dial." on the first pointerdown or keydown, and `act()` (540-541) hides
   the on-screen hint on the same gesture. A student who drags the dial or presses Play hears an instruction for what
   they just did; one who taps a lever hears it with no hint on screen. Seen: audit held-click rows 0 to 14, 16 and 18;
   `play/f5/drag-dial.png`; Craft `voice.py` V1 (hint already hidden when the line started at 1.52 s), V8, V9. Fixed:
   say nothing when the first gesture is the time dial, date wheel, Play or the play knob (the time is already
   moving); for any other first gesture, speak the line and keep the on-screen hint visible until the line ends or the
   student moves time, whichever is first. Read and Sound stay as they are (Craft's voice table is right there).
   (family:curiosity)
5. **The Sun has no distance.** Sun card `src.html:1118-1128`: MAG -26.74 but no DIST, while planets show au and the
   Moon km. The 5-ESS1-1 comparison (Sun 1 au, about 8.3 light minutes, against Sirius 8.6 ly) cannot be read off the
   instrument. Seen: `teaching/calc2-out.json` `sunCard`. Fixed: a DIST row on the Sun card in au to three decimals
   plus light minutes. (general)
6. **The Manual leaves out seasons and the Sun's path.** Spec Manual contents (`spec.md` "The Manual") list "seasons
   and the Sun's path"; "Why it changes" (`src.html:336-341`) covers the daily spin, the yearly star drift, phases and
   loops but never says Earth's tilt makes the Sun's path higher and longer in summer, which is what DAYLIGHT shows
   (1-ESS1-2, MS-ESS1-1). Seen: Manual read in full, `audit-r1/state-manual-1366x768.png`. Fixed: a short plain
   paragraph on tilt, the Sun's path and daylight, plus a "Things people have found" entry using the instrument's own
   checked numbers (Denver about 15 h on June 21 and about 9 h 21 min on December 21, USNO), sourced.
   (family:curiosity)
7. **Date and time wheel engravings cannot be read and fail AA.** `wheelControl` `src.html:1257-1258`: `font-size="5"`
   in a 100-unit viewBox (about 5 px), `#e1c68d` on a gold band, about 1.9 to 1. The month and hour marks are the
   instrument's scale. Seen: `craft/wheels-crop.png`. Fixed: dark engraving `#2a1f10` (the spec palette) at 8 px or
   more on the gold, or the marks on the dark inner ring, at 4.5 to 1 or better. (general)
8. **Read speaks clock time as a duration: "20 hours 22 minutes".** `speakText` `src.html:520`. On a grade 1
   projector that is heard as an amount of time. Seen: audit row 18; Craft voice check ("20 hours 37 minutes"). Fixed:
   spoken as a time of day, for example "8:22 in the evening" (midnight and noon said as such); the on-screen readout
   stays 24-hour. (general)
9. **Long star labels run over neighbours and put the wrong name on the Southern Cross.** Label placement
   `src.html:997-1005` tries right then left with no leader. Over Sydney (2026-05-01 20:04) "Rigil Kentaurus" runs
   right across Crux, "Toliman" is labelled separately at the same point, and Acrux and Hadar get no label; a star dot
   sits on the P of "Pollux". Seen: `play/f3/sydney-sky.png`, `play/crop-cross.png`, `play/crop-rollux.png`. Fixed: a
   label box may not cover another drawn star brighter than about mag 2.5 or another label; a short tick joins a
   label that sits off its star; a close pair (Rigil Kentaurus and Toliman) is labelled once. Acrux gets its label
   over Sydney. (general)
10. **Typing "Sydney" says the place is not bundled.** `$("city").onchange` `src.html:1291-1294`: a name that matches
    two places (Sydney, Australia and Canada) falls through to "Place not in bundled selection. Enter latitude and
    longitude." and marks the field invalid. That message is false. Seen: `play/f3` shot "sydney"; Craft `read.py`.
    Fixed: "Two places match. Choose Sydney · Australia or Sydney · Canada." with the list offered, field not marked
    invalid. (general)
11. **Escape anywhere throws focus to the sky.** `src.html:1397-1398`: with no Place sheet open, Escape clicks
    `close-object`, which runs `act()` and `canvas.focus()` even with no readout open, so Escape in the place search or
    on a lever moves focus and hides the hint. Seen: Craft `kb.py` (focus after Escape in `#city` and on `#lines` =
    `sky`). Fixed: Escape closes the readout only when `#object` is open; inside inputs it does nothing beyond the
    input's own behaviour. (general)

#### Polish accepted
1. **Manual in plain words first.** `src.html:298-356`, 352-442: "precessed to the chosen date", "proleptic Gregorian",
   "truncated periodic expansion", "local mean solar time (longitude divided by 15)". Plain sentences first, each term
   glossed once; the dataset audit trail (vertex counts, place corrections) moves into a collapsed "Sources and
   checks" `details` beside the licence terms. Nothing removed. (family:curiosity)
2. **Distances shown one way.** `src.html:1123` rounds to whole ly: Sirius "9 ly" on the card, 8.6 in the Manual;
   Alpha Centauri 4 for 4.3. Show one decimal under 20 ly so the card matches the Manual. Seen:
   `teaching/calc2-out.json` `card`. (general)
3. **The classic bright-but-far stars get distances.** Rigel, Deneb, Canopus and Antares show no distance, so Things
   to do 11 has only Betelgeuse as a far, bright star. Add the ones with a NASA or ESA fact page, confirmed against a
   second source, marked ≈ where uncertain; skip any that cannot be confirmed. (general)
4. **Year window shows the BC year.** `#year` `src.html:252-254` shows "-2799" large with "2800 BC" small; typing
   -2800 gives 2801 BC. The window shows the plain year with an era flag (BC or AD) the student can switch, and typing
   "2800 BC" works; astronomical numbering stays in the Manual. Seen: `audit-r1/state-ancient-pole-1366x768.png`.
   (general)
5. **Sun, Moon and planet names stay in daylight.** `src.html:993` drops every label when `day >= .85`. Keep star
   names fading; keep Sun, Moon and visible planet labels. Seen: `play/f5/drag-dial.png`, `play/f1/noon-daylight.png`.
   (general)
6. **Phone plate on one line, rivets clear.** `.plate` `src.html:172` with `::before/::after` at 98-99: at 375 wide it
   wraps ("Sky / Dome") and the dots touch "Curio" and "Dome" (also at 680x425 and 800x500). Smaller size or tighter
   spacing on one line, padding clear of the rivets. Seen: `play/crop-plate.png`. (family:curiosity)
7. **Phone dome toward the spec's 60 percent, readouts kept.** `src.html:1180-1181` (`top=112`), `#hint` `:182`: the
   dome is about 220 px tall at 375x667, the hint sits on the Capella labels, and Sun and Moon rise and set are dropped.
   Grow the dome toward 60 percent of the height at 375x812, keep rise and set reachable (the two-row strip or the
   card), and place the hint off the star labels. Seen: `play/f4/phone-default-tall.png`. (general)
8. **Live-region words use visible names.** `src.html:1286, 1299` announce "milky off", "lat 39.7 degrees". Use the
   lever's visible name ("Milky Way off") and "Latitude 39.7 degrees north". (general)
9. **Play knob and reverse switch in the brass grammar.** The play knob is a native `<select>` (`src.html:248`) and the
   reverse switch shows only "↶". Spec asks for a knob with detents: draw it as one (keeping its keyboard and announced
   value), and engrave REV beside the switch. (family:curiosity)
10. **Deep-sky hint only when a range shows.** `src.html:1136` always says "Magnitude range reflects the two source
    estimates." (M31 shows one value). Add that sentence only when two values are shown. (general)
11. **"DIST not verified" reads as doubt.** `src.html:1123`: say "no checked value" instead. (general)
12. **Compass letters at the poles.** From either pole every direction is south or north. Add one Manual line saying
    so (Things to do 6 sends students there). Seen: `audit-r1/state-southern-sky-1366x768.png`. (general)
13. **Time dial focus ring overlaps its label.** The 3 px outline runs over "TIME · 24 HOURS". Seen:
    `play/f1/keys-time.png`. (general)
14. **Ring through "AGE" at 680x425.** The brass ring crosses "AGE 26.5 d" (`craft/680-top-right-crop.png`); check
    again after Blocker 1 and clear it if it remains. (general)

#### Settled calls
- **The six audit leads ("hint out of view: Drag the time dial.") are wrong leads.** All three lenses agree: a
  Curiosity's hint is gone after the first action. Do not bring the on-screen hint back after an action.
- **Hint timing (Should fix 4).** Play wanted silence after any instrument control; Craft wanted silence only after the
  dial or Play, with the visual hint held while the line plays. Settled toward Craft plus the date wheel and play knob:
  the line is spoken once and only while it is true on screen. No second hint, no extra lines.
- **Read's clock phrasing is a should fix, not polish** (Teaching should fix, Play polish): grade 1 hears this on a
  projector, and a time heard as a duration misleads.
- **"Sydney" is a should fix, not polish** (Play should fix, Craft polish): the message states something false.
- **Hint tag:** family:curiosity (Play), not general (Craft), because the browser needs a gesture before speech, so
  every Curiosity's once-spoken hint meets this.
- **Fixes add real material only.** Constellation names, the Sun's distance and the seasons paragraph are readouts and
  Manual text; none becomes a task, target or checklist (CODEX-CURIOSITY, BASELINE rule 2 read with the Curiosity
  shape).
- **Keep:** the astronomy and its tolerances, Motion off stepping, Same time each night, the Read voice table, the
  Manual's honesty notes (moved, not cut), no network requests, no sky stories.
- **No sensitivity review needed.** No cultural sky stories; star names are IAU identifiers with no origin claims. If
  sky stories are added later, they need one (rule 5).
- **Note for the integrator, not for Codex:** the Craft lens ran `python scripts/check_tools.py --help`, which has no
  help flag and rebundled about 80 non-draft tools' git-ignored `tools/<id>/<id>.html` from their current src.html. No
  tracked file was written; sky-dome was skipped. Matters only if a runner compares bundle timestamps.

#### To the spec's open questions
- **Drop science-9-stars-and-the-big-bang from "Also reaches"?** Its codes (HS-ESS1-1, -2, -3: the Sun's life span and
  fusion, Big Bang evidence, nucleosynthesis) are not taught by anything in the instrument; it shows positions,
  magnitude, B-V and temperature. BASELINE rule 2 says remove it and make sure another tool teaches it. Teaching lens
  recommends dropping it (`spec.md` Map, and wherever the module map row is written).
- **science-5-sun-stars-and-shadows: add a SHADOW readout or call the reach partial?** Day, night and seasonal stars are
  taught; shadow length and direction are not. A SHADOW row on the Sun card (a 1 m stick's shadow length and
  direction from the Sun's ALT and AZ) would cover it; otherwise the reach is partial and rule 2 applies.
- **The default view and the "faint ground silhouette".** At the whole-dome view looking straight up the horizon is
  the rim, so the spec's first-view ground silhouette never shows (`audit-r1/size-1366x768.png`). Either the opening
  view tilts toward the horizon or the spec line changes to the brass ring alone.

#### Not taken
- Dropping the compass letters at the poles: the one-line Manual note (Polish 12) is enough and keeps the ring stable.
- A rolling odometer drawing for the year: the era fix (Polish 4) solves what the student misreads; a full odometer
  animation is optional decoration.
- Typing "2800 BC" being mandatory to reach Thuban: covered by Polish 4; no separate change.

#### Exit check (2026-11-06)

Cold exit check by Claude on the current bundle (`sky-dome.html`, 584,934 bytes, not rebundled). Frames and logs in
`S:/CurioClass-codex-scratch/sky-dome/exit/` (`audit-r2/`, `drive/`, `drive.log`, `perf.py`, `perf2.py`).

##### Merged items

- **Blocker 1, stretched sky: fixed.** `resize` sets `rx=ry` (`src.html:1435`); `projectVector` and `fromScreen` share
  it. Orion at FOV 50 (21:00 Denver, 2026-01-14) has its true shape: Betelgeuse to Rigel 158 px across, 99 px down
  (was 393 by 92). The ring is round in every `audit-r2/size-*.png`. Note: the re-shoot landed at
  `craft/orion-1366-fov50.png` (my helper's output path was wrong), so the Craft lens's original frame there was
  overwritten by the fixed one; the original is still beside Codex's `fix-before-orion/`.
- **Should fix 1, constellation names: fixed.** CONST row on the Sun card (Taurus, June 21) and star cards; faint
  figure names with Lines and Names on (Orion, Canis Minor, Monoceros; Crux and Centaurus over Sydney).
- **Should fix 2, 60 fps on a Chromebook profile: open.** Re-measured at 1366x768, Play 1 h/s, 21:00 Denver (night, so
  the star field is drawn): 1x throttle holds 16.7 ms frames; 4x throttle with Lines, Names, Ground, Milky Way and
  Trails on gives draw 18.6 ms median (27.3 p95) and frame interval 66.7 ms median (15 fps); with those off, draw
  14.8 ms but frames still 50 ms (20 fps). The rAF interval is well above the draw time, so work outside `draw()`
  (readouts, label layout, time step) also costs per frame. A daytime measure looks fine only because stars are not
  drawn; measure at night. Codex's own account agrees this is open.
- **Should fix 3, zoom buttons over W: fixed.** Zoom sits below the round ring; N, E, S, W clear at 1366x768
  (`drive/default-1366.png`) and every audit size.
- **Should fix 4, late spoken hint: fixed.** Held clicks on the time dial, date wheel, Play and rate knob speak nothing
  (audit rows 3, 4, 6, 9). A first Lines click speaks "Drag the time dial." with the on-screen hint still shown
  (`drive.log` first-lines-hint: hidden false). Observation, not open: Year era and Now also move time yet speak the
  line once (rows 5, 7); a quick second tap cuts it. Within the settled call ("whichever is first"), left as is.
- **Should fix 5, Sun distance: fixed.** "DIST 1.016 au · 8.5 light min" on June 21 (`drive.log` sun-card).
- **Should fix 6, seasons in the Manual: fixed.** Tilt paragraph (`src.html:402-403`) and the Denver "A longer Sun
  path" entry (`:410`).
- **Should fix 7, wheel engravings: fixed.** Dark `#2a1f10` marks at 9 units with a gold halo (`src.html:1530`);
  legible on `drive/default-1366.png` and the 375 frames.
- **Should fix 8, Read clock phrasing: fixed.** "January 14, 2026. 8:22 in the evening. Denver. ..." (`drive.log`
  read-clock); audit row 20 "10:16 in the morning".
- **Should fix 9, colliding star labels: fixed.** Sydney 2026-05-01 20:04: Acrux, Hadar, Mimosa, Gacrux labelled; one
  "Rigil Kentaurus / Toliman" label (`audit-r2/state-sydney-lines-1366x768.png`).
- **Should fix 10, Sydney message: fixed.** Typing "Sydney" offers "Sydney · Australia" and "Sydney · Canada",
  announces "Two places match. Choose ...", aria-invalid unset.
- **Should fix 11, Escape focus: fixed.** Escape in `#city` leaves focus in `#city` (`src.html:1684-1688`).
- **Polish (spot-checked in bulk): fixed as described.** Seen: plain Manual with "Sources and checks" collapsed,
  AD/BC era button, daylight body names (Sun, Venus, Mercury, Moon, Mars, Jupiter at 10:22), one-line plate with clear
  rivets at 375, phone rise and set rows kept, REV engraved, brass rate knob, polar compass line in the Manual. Canopus
  and Deneb distances left out under Polish 3's skip allowance.

Fixed: 11 of 12 (blocker 1 of 1, should fix 10 of 11). Polish: 14 of 14 addressed.

##### Regressions

None found. Default screen, the nine audit states at eight sizes, Motion off, the resize stress and the held-click walk
are clean: no exceptions, no console errors or warnings, nothing left disabled, no control moved more than 12 px. The
Sydney frame with Lines and Names on is dense but readable.

##### Gate

1. Every Done when: **no.** Done when 7 (60 fps on a school Chromebook profile) fails at 4x throttle, see Should fix 2.
   The rest hold as checked by the lenses and the fixes (astronomy math unchanged).
2. Codes taught or moved: unchanged from round 1; the two spec open questions (science-9 reach, SHADOW readout) are
   still for the integrator, not a fix item.
3. Solo defaults work: yes (opens on tonight's sky over the home city, one quiet hint, no welcome).
4. Sensitivity: not needed (no sky stories), per Settled calls.
5. No blocker or should-fix open: **no**, Should fix 2.
6. Bundle clean: yes. 585 KB, under 2 MB; zero console errors; the only requests are the tool file itself.
7. Voice counts: right. `voice/lines.json` holds the one line "Drag the time dial."; Read is dynamic; the calm-professor
   recording is still absent (browser fallback), a recording item, not a count error.

#### Audit pilot

- Leads: 10, all "hint out of view: Drag the time dial." across the nine states plus two quick-tap "how line cut"
  rows (Year era, Now). All are wrong leads under the settled Curiosity hint call; none confirmed.
- Useful rows: held-click table (silent dial, wheel, Play, knob; Read phrasing) and the clean stress, Motion off and
  size rows were enough to confirm Should fix 4 and 8 and the regressions sweep.
- Missed: performance. The audit has no frame-rate row, and a daytime run would hide the star-field cost anyway;
  Should fix 2 needed a separate throttled night measure. It also reports no network row directly (checked by hand).

#### Exit re-check (2026-11-06, Claude integrator, after Codex round 2)
The one open item was should fix 2 / Done when 7 (60 fps, 1366x768, night, all stars and lines on, 4x CPU throttle).
Codex's round 2 numbers (frame interval median 45 ms) came from scripts/drive.py, which starts Chrome with
--disable-gpu, so WebGL ran on the Microsoft Basic Render Driver (software). A school Chromebook draws WebGL on its GPU.
Same scene and script (Codex's r2-precision-shots final-night), run twice in this session:
- GPU off (Microsoft Basic Render Driver): 4x draw median 6.7 / p95 8.5 ms, frame interval median 28.9 / p95 35.8 ms.
- GPU on (ANGLE D3D11): 4x draw median 5.6 / p95 8.6 ms, frame interval median 7.4 / p95 10.7 ms; 1x interval 7.0 ms.
The CPU-side draw fits the 16.7 ms frame with room to spare at 4x, and with a GPU the frame interval is well under it.
This PC's GPU is far stronger than a Chromebook's, so the GPU number is an upper bound; the CPU-side draw at 4x is the
honest Chromebook reading and it passes. Verdict: Done when 7 met. No other item was open; Codex's round 2 polish.md
records the regression checks. Evidence: the Claude session scratchpad skygpu folder (soft-* and gpu-* json).
Lesson for later checks: WebGL tools must be timed with the GPU on, or the gate reads the software rasteriser.

<!-- end part -->

<!-- part: refine/craft.md -->

### Craft lens: sky-dome (Curiosity No. 05), round 1

Cold lens, judged against CODEX-CURIOSITY.md, VISION "Curiosities", STANDARDS and BASELINE. Bundle as built
(532 KB), headless Chrome on port 9761, with the GPU on for frame timing. Scratch and frames:
`S:/CurioClass-codex-scratch/sky-dome/craft/` (scripts cc.py, perf.py, prof.py, kb.py, voice.py, read.py, motion.py).

#### Findings

##### 1. The dome squashes the sky: star patterns are drawn 2.7 times wider than tall (blocker, family:curiosity)
- Where: `src.html:819-827` `projectVector` (and `fromScreen`, `resize` 1180-1181). The normalized radius goes to
  `r*rx` horizontally and `r*ry` vertically. At 1366x768 rx = 621 and ry = 233, so this happens at **every** zoom, not
  only the whole-dome fisheye.
- What: at FOV 50 on Orion (2026-01-15 04:00 UTC, Denver), 1 degree is 24.8 px across and 9.3 px down. Orion is
  flattened into a wide smear you can't recognise (Betelgeuse to Rigel: 393 px across, 92 px down). At 680x425 (the
  site preview) the dome is about 4.6:1. Shapes also change as they turn, so "the Big Dipper on a spring evening and an
  autumn evening: the same stars, turned" (spec Things to do 13) shows a different shape, not a turned one. A
  planetarium whose star patterns are wrong breaks the "readout that lies" rule, even with the Manual's honesty
  note (`src.html:356`). The real instrument is round.
- How seen: `craft/orion-1366-fov50.png` (with object pixel coordinates from perf.py), `audit-r1/size-1366x768.png`,
  `size-1920x1080.png`, `size-680x425.png`.
- Better: use one scale (min(rx, ry)) for both axes. Fill the width with a round dome, or let a zoomed view fill the
  stage at a true aspect, the way planetarium software does. Keep the brass horizon ring round at whole-dome view.

##### 2. 60 fps fails on a Chromebook-class CPU (should fix, general; Done when 7 fails as measured)
- Where: `draw()` `src.html:926-951`. Each of about 4,600 visible stars gets its own `globalAlpha`, `fillStyle`,
  `beginPath/arc/fill`. Every frame also runs `querySelectorAll` and `getComputedStyle` for label boxes (983-986).
- Measured (1366x768, Play at 1 h/s, all stars, lines and trails on, GPU Chrome):

  | CPU throttle | rAF frame median | p95 | draw() median |
  |---|---|---|---|
  | 1x (this desktop) | 7.0 ms | 13.9 ms | 7.7 ms |
  | 2x | 20.8 ms (48 fps) | 20.9 ms | 16.8 ms |
  | 4x (common Chromebook proxy) | 34.7 ms (29 fps) | 48.6 ms | 30.1 ms |

  With lines and trails off, 4x still gives 41.7 ms. Stars alone (everything else off) cost 23.8 ms per draw at 4x
  (prof.py). The star loop is the cost, not the lines.
- Better: batch the stars by colour and alpha bucket into a few paths, or draw them once to an offscreen canvas per
  sidereal step and blit it. Read the overlay rects once on resize, not every frame.

##### 3. The west compass letter is hidden under the zoom buttons (should fix, general)
- Where: `.view-tools` `src.html:52` sits over the ring's W marker at the whole-dome default.
- How seen: `craft/w-marker-crop.png` (from audit `size-1366x768.png`); the same at 1920x1080 and 1280x720. W shows
  at 800x500. West is where every star the student watches goes to set.
- Better: move the view tools clear of the ring (into the deck or below the ring), or inset rx past them.

##### 4. Date and time wheel engravings can't be read (should fix, general)
- Where: `wheelControl` `src.html:1257-1258`. The text is `font-size="5"` in a 100-unit viewBox, so about 5 px:
  `#e1c68d` on a gold band (#9a7945 to #ceb37b), about 1.9:1.
- What: the month marks (JAN APR JUL OCT) and hour marks (0 6 12 18) are the instrument's scale. They are blurs, and
  they fail AA (Done when 9).
- How seen: `craft/wheels-crop.png`.
- Better: dark engraving (#2a1f10, as the spec's palette says) at 8 px or more on the gold, or put the marks on the
  dark inner ring.

##### 5. The spoken hint plays after the student already did it, with the on-screen hint gone (should fix, general)
- Where: `src.html:547-552` (capture listener) with `act()` at 540-541.
- What: the first pointerdown anywhere queues "Drag the time dial." and the same gesture hides the on-screen hint. So
  a student who drags the time dial first hears "Drag the time dial." after doing it. Dragging the sky or tapping a
  lever gives the same line, now with no hint on screen. The rule is that a spoken line matches the screen; here
  `valid` checks only the Manual and Place sheet. With Tab as the first key it is fine (the hint stays shown).
- How seen: voice.py V1 (hint `hidden` was already true when the line started at 1.52 s), V8, V9.
- Better: skip the line when the first gesture is on the time dial or play, and keep the visual hint until the line
  finishes. Or speak it only from a first gesture that doesn't count as the first action (Tab, Read).

##### 6. Escape anywhere moves focus to the sky canvas (should fix, general)
- Where: `src.html:1397-1398`. With no Place sheet open, Escape calls `$("close-object").click()`, which runs `act()`
  and `canvas.focus()` even when no readout is open.
- What: Escape in the place search (the normal way to clear a search box) or on a lever throws focus onto the canvas
  and hides the hint.
- How seen: kb.py, focus after Escape in `#city` = `sky`, and after Escape on `#lines` = `sky`.
- Better: act only when `#object` is open, and do nothing for Escape inside inputs.

##### 7. "Sydney" says the place isn't in the bundle, but it is (twice) (polish, general)
- Where: `src.html:1291-1294`. A name matching more than one place falls through to "Place not in bundled selection.
  Enter latitude and longitude."
- What: Sydney (Australia and Canada) is bundled, so the message is wrong, and the field is marked invalid.
- How seen: read.py.
- Better: "Two places match. Choose Sydney · Australia or Sydney · Canada." (the datalist already lists them).

##### 8. Live-region words use internal ids (polish, general)
- Where: `src.html:1299, 1286`. Screen readers hear "milky off", "lines on", "lat 39.7 degrees".
- Better: the lever's visible name ("Milky Way off", "Latitude 39.7 degrees north").

##### 9. The deep-sky card claims a magnitude range when only one value shows (nit, general)
- Where: `src.html:1136`. The hint always says "Magnitude range reflects the two source estimates." M31 shows `MAG 3.40`.
- How seen: read.py (M31 card text).
- Better: add that sentence only when the range is shown.

##### 10. Readout and plate small collisions (nit, general)
- At 680x425 the brass ring runs through "AGE 26.5 d" (`craft/680-top-right-crop.png`).
- At 680x425, 800x500 and 375x812 the plate's corner dots (`.plate::before/::after`) touch "Curio" and "Dome", and
  at 375 the plate wraps to two lines ("Sky / Dome").

##### 11. Two controls are not instrument-styled (polish, family:curiosity)
- The play knob with detents (spec) is a native `<select>` (`src.html:248`). The year odometer is a plain number box.
  Both work and announce their values. A detent knob and a rolling odometer would match the brass grammar of the
  wheels. The reverse switch shows only "↶"; a small engraved REV label would help.

#### Checks that passed
- **Contract:** one file, 532 KB (under the spec's 600 KB). No network requests across 20+ page loads and every
  interaction (only the file itself, Network domain). No console errors or exceptions. The kit is used for voice, tone,
  Motion and Sound, with its own controls drawn. No `art:` tokens; prompts.json has none, rightly.
- **Look:** fills the screen, no header, welcome, score, goal or finish. Manual drawer and plate lower-left at
  1366x768. At 375 the plate is lower-left with Manual beside it on the right. Motion, Sound and Read are on their own
  power panel. Readouts are monospace with units.
- **Keyboard:** the Tab order runs view tools, wheels, year, transport, place, levers, Manual, power. Every one has a
  visible 3 px outline. The wheels are `role=slider` with valuetext ("20:45 local time", "2026-12-05"), announced in
  the live region. Arrow and Shift steps work, and so does Home/End. Year ArrowUp commits and announces "Year 2027".
  The rate select announces "Projector rate: 1 hour per second". Dome then Tab walks bright objects ("Moon. Enter
  selects."). Main targets: wheels 100 px, play/now/year 60 px, the rest 44 px.
- **Motion off:** Play steps 10 minutes ("Motion off. Stepped time."). Same time each night steps one day at the same
  clock. Nothing moves on its own (motion.py). Audit Motion-off row clean.
- **Words:** no em dashes in src, notes, tool.draft.json or lines. "Curio Class" is always in full. The lesson-creep
  grep only hit non-lesson uses (autocomplete, "corrected", "minute-level"). Privacy is stated ("Motion preference
  stays on this device").
- **Lines:** `voice/lines.json` holds the one line, word for word, same as `L.hint` (`allLines()`). Read's text is
  built live (date, time, place, then the object or Moon phase), as the spec says.

#### Voice check (Sound on, held clicks, `__tool.vlog`)

| line | kind | expected | spoken |
|---|---|---|---|
| "Drag the time dial." (5 time-dial drags, 2 s apart) | how | 1 | 1 |
| "Drag the time dial." first tap = Read | how | 0 | 0 (Read spoke the sky) |
| "Drag the time dial." first tap = Sound | how | 0 | 0 |
| Read, 5 presses | read | 5 | 5 |
| Read with Sound off | read | 1 | 1 |
| Read 0.25 s into the hint | read cuts hint | hint cut, Read plays | hint `cut: read`, Read at +0.5 s |
| Read while Play runs | read | projector stops | stopped (`playing: false`) |

- Stale lines: the only stale case is finding 5 (the hint after its moment). Nothing plays after Reset, Now or a
  place change. No other lines exist.
- Sound off at first tap, then on: the hint never plays. That is right for a Curiosity (the hint is gone after the
  first action).
- Read text with Sirius: "November 5, 2026. 20 hours 37 minutes. Denver. Sirius, magnitude -1.46." That matches the
  card on screen.

#### Note from this lens
While looking for check_tools options I ran `python scripts/check_tools.py --help`. It has no help flag and ran in
full, rebundling about 80 non-draft tools' generated `tools/<id>/<id>.html` from their current `src.html` (git-ignored
outputs; the draft tools, sky-dome included, were skipped and not touched). No src, json or tracked file was written.
The integrator should know in case a runner compares bundle timestamps.

#### Audit pilot
- **Leads confirmed:** none of the 6 needed action. All 6 are "hint out of view: Drag the time dial." in states after
  an action. That is by design for a Curiosity (the hint goes after the first action), so they were **wrong leads**
  here. The audit shows "welcome not heard" on every first tap because this tool has no welcome, only the hint, which
  the "spoken" column shows correctly.
- **Clean rows cited:** sizes, Motion off, resize mid-action, five clicks and two quick taps. These agree with my own
  runs.
- **What it missed:** the anisotropic dome (1), frame time under a CPU throttle (2), the W letter under the zoom
  buttons (3; a canvas-drawn label under a DOM button), the unreadable SVG wheel engravings and their contrast (4),
  the hint spoken after the gesture it asks for while hidden (5; it logs the line but not the hint's visibility),
  Escape stealing focus (6), and the wrong ambiguous-place message (7).

<!-- end part -->

<!-- part: refine/play.md -->

### Play lens: sky-dome (Curiosity No. 05), round 1

Played twice: as a grade 5 to 6 student alone at home (opened it, dragged the time dial, chased the Moon, tried the
year, went to Sydney, the equator and the North Pole) and as a teacher projecting it for grade 1 (Play at 10 min/s,
Same time each night, daylight on and off, Read). Judged against CODEX-CURIOSITY.md and VISION "Curiosities", not
lesson norms. Frames are mine in `S:/CurioClass-codex-scratch/sky-dome/play/f1` to `f5` (plus crops), and the shared
audit's frames in `S:/CurioClass-codex-scratch/sky-dome/audit-r1`.

#### Short test

- **Would a kid open it unassigned?** Yes. The first drag of the time dial makes the whole sky wheel, the Moon
  and Saturn move, day floods in. That reaction comes with nothing read.
- **Would an adult play for fun?** Yes. Mars tracing its loop with Trails (f2/mars-zoom.png), Thuban at the pole in
  2800 BC, Polaris Australis over Sydney, Same time each night sliding the sky west (5 days in 6 s, clock held at
  20:33). That depth would last a month.
- **Is the real thing the interface?** Yes, but the sky is drawn stretched (first finding). The figures a student is
  told to watch turning change shape as they turn. This is the one place the short test bends.
- **Does it work with no finish line?** Yes. Lesson creep search finds no score, goal, level, sticker or finish. The
  hits ("points", "complete", "level", "correct") are code names and Manual prose.

#### Findings

##### 1. The dome stretches the sky, so constellations change shape as they turn
- **Where:** `src.html:1181` (`rx` set from the width, `ry` from the height, separately), and `projectVector`
  `src.html:819-826`, which scales x by `rx` and y by `ry`.
- **What:** at 1366x768 the 180 degree dome is an oval about 1240 by 470 px, so east-west angles are drawn about 2.6
  times larger than north-south ones. At 680x425 the stretch is close to 4 to 1. The Big Dipper is a long flat ladle at
  22:00 and a tall narrow one at 04:00 the same night: the same stars, a different shape. Spec "Things to do" 13 ("the
  same stars, turned") and the first reaction ("the whole sky wheels around one still point") both show this
  distortion first. The Manual admits it ("an equal-angle sky map fitted to an oval viewport"), but a student never
  reads that, and a planetarium dome has one scale in every direction. The Mars loop and Saturn's ring are drawn
  squashed the same way.
- **Seen:** `play/f1/dipper-a.png` beside `play/f1/dipper-b.png` (Denver, 2026-04-14 22:00 and 04:00, az 0, alt 45,
  FOV 90); every audit frame (`audit-r1/size-1366x768.png`, `size-680x425.png`).
- **Better:** one scale for both axes. Keep the 180 degree dome a circle and fill the spare width with the readouts
  and the dial deck, or with a wide equal-scale view when zoomed in.
- **Level:** blocker. **Tag:** family:curiosity (the real material is the interface; here it is drawn wrong).

##### 2. The zoom buttons cover the W on the horizon ring
- **Where:** `.view-tools` `src.html:52` (desktop), `:179` and `:195` (narrow).
- **What:** the + and minus buttons sit on the dome's west edge, hiding the W compass letter at 1366x768, 680x425 and on
  the phone. That leaves three compass points visible on a tool built around them (stars "setting in the west").
- **Seen:** `audit-r1/size-1366x768.png` (W under the minus button), `play/crop-phonedome.png`,
  `audit-r1/size-680x425.png` (buttons over the lower-right rim).
- **Level:** should fix. **Tag:** general.

##### 3. The first-run hint is spoken just after the student has already acted
- **Where:** `src.html:546-551` (the hint plays on the first pointerdown or keydown) and `act()` `src.html:540-541`
  (the same gesture hides it).
- **What:** whatever the first gesture is (Play, Zoom in, Lines, Now, even dragging the time dial itself), the voice
  says "Drag the time dial." while the line vanishes from the dome. A student who pressed Play hears an instruction
  for something else as the sky starts moving. The words no longer match the state (POLISH).
- **Seen:** audit "One held click per control" table, rows 0 to 14, 16 and 18: every control speaks "Drag the time
  dial." on its first tap. Confirmed on `play/f5/drag-dial.png`, where the hint was hidden after the drag.
- **Better:** if the first gesture is on any instrument control, say nothing; speak the hint only when the first
  gesture is a tap on the empty dome or deck, or only on Read.
- **Level:** should fix. **Tag:** family:curiosity (the browser needs a gesture before speech, so every Curiosity's
  "spoken once" hint lands late).

##### 4. No constellation names anywhere, so half the "Things to do" cannot be found alone
- **Where:** no constellation label or readout exists in `src.html`. FIGURES (`:804`) are drawn as unnamed lines; the
  star card (`object-type`) gives "HR 2491 · A1Vm" but not the constellation.
- **What:** spec items 4 ("which constellation the Sun is in"), 7 (the Southern Cross), 12 (Thuban "in Draco") and 13
  (the Big Dipper) all need names a student cannot get from the dome. With Lines on, the dome shows 88 nameless stick
  figures. A grade 5 student alone at home cannot tell which one is Orion. This is also the depth a month of use would
  look for: learning the sky by name.
- **Seen:** `play/f1/noon-nodaylight.png` (the Sun with daylight off; nothing says where it is),
  `audit-r1/state-running-1366x768.png` (Lines on, no names).
- **Better:** constellation names as a lever (or tied to Lines), and a CONST row on the readout card. Real material,
  not a game.
- **Level:** should fix. **Tag:** family:curiosity.

##### 5. Long star labels run over neighbouring stars and mislabel the Southern Cross
- **Where:** label placement `src.html:997-1005`, which tries right and then left of each star with no leader line.
- **What:** over Sydney (2026-05-01 20:04), "Rigil Kentaurus" starts at its star (x 498) and runs right across Crux,
  so the label sits on the Southern Cross; "Toliman" is labelled separately at the same point; Acrux and Hadar get no
  label. A student hunting for the Southern Cross (spec item 7) reads the wrong name on it. Labels are also drawn over
  other stars: a star dot sits on the P of "Pollux".
- **Seen:** `play/f3/sydney-sky.png`, `play/crop-cross.png`, `play/crop-rollux.png`; positions from `__tool.objects`
  (Rigil Kentaurus 498,389; Acrux 599,372; Mimosa 572,366; Gacrux 579,358).
- **Better:** a short tick from star to label when the label clears it, skip a label whose box covers a brighter
  labelled neighbour, and label a binary once.
- **Level:** should fix. **Tag:** general.

##### 6. Typing "Sydney" says the place is not in the selection
- **Where:** `$("city").onchange` `src.html:1291-1294`.
- **What:** "Sydney" matches two bundled places (Australia, Canada), so the tool answers "Place not in bundled
  selection. Enter latitude and longitude." That is untrue: both are bundled. A student following "go to the far
  south" types the city and is told it is missing. "Paris" alone works because it is unique.
- **Seen:** `play/f3` shot "sydney": live text plus `places` filter `["Sydney · Australia","Sydney · Canada"]`.
- **Better:** "Two places match: pick one from the list" and open the list, or prefer the most populous match.
- **Level:** should fix. **Tag:** general.

##### 7. The year odometer shows "-2799" for 2800 BC
- **Where:** `#year` `src.html:252-254` (astronomical year numbering, with the era beneath).
- **What:** spec item 12 says "set the year to 2800 BC". A student types -2800 and gets 2801 BC; the big window reads
  "-2799" with "2800 BC" small beneath. Two numbers for one year, and the large one is the unfamiliar one. In AD
  years the window and the line beneath say the same thing twice ("2026" and "AD 2026").
- **Seen:** `audit-r1/state-ancient-pole-1366x768.png`; `play/f1` shot "year-bc" (era "2800 BC" from -2799).
- **Better:** the window shows "2800" with a BC/AD switch beside it (a real odometer with an era flag); keep the
  astronomical year in the Manual.
- **Level:** polish. **Tag:** general.

##### 8. In daylight the Sun, Moon and planets lose their names
- **Where:** `src.html:993` (`if(state.names && day<.85)` drops every label in daylight).
- **What:** dragging the time dial into the morning leaves a bright disc, a white dot and a crescent with no names
  (Venus and the Moon in `play/f5/drag-dial.png`). This is the moment a grade 1 class is asked "where is the Moon in
  the daytime?", and the dome goes quiet. Star names fading in daylight is right; Sun, Moon and planet names fading is
  a flat moment.
- **Seen:** `play/f5/drag-dial.png`, `play/f1/noon-daylight.png`.
- **Better:** keep labels for the Sun, Moon and visible planets in daylight.
- **Level:** polish. **Tag:** general.

##### 9. The phone plate wraps and its rivet sits on the C
- **Where:** `.plate` `src.html:172` (`white-space:normal; max-width:250px`) with the `::before` dot at `:98-99`.
- **What:** at 375 wide the plate reads "Curio Class Curiosities · No. 05 · Sky / Dome" over two lines, and the left
  rivet dot overlaps the first letter of "Curio Class". The plate is a family mark and should read as one engraved line.
- **Seen:** `play/crop-plate.png` (from `play/f4/phone-default-tall.png`), `audit-r1/size-375x812 (iframe host).png`.
- **Better:** a smaller size or tighter letter-spacing so it fits on one line, with padding that clears the rivets.
- **Level:** polish. **Tag:** family:curiosity.

##### 10. Phone: the dome is small and the hint sits on the star labels
- **Where:** phone layout `src.html:1180-1181` (`top=112`) and `#hint` `:182`.
- **What:** at 375x667 the dome is about 220 px tall (the spec asks for about 60 percent of the height), and "Drag the
  time dial." sits under N over the Capella area. Sun and Moon rise and set times are dropped on the phone, so the
  phone student loses the readouts behind spec items 3 and 5.
- **Seen:** `play/f4/phone-default-tall.png`, `play/crop-phonedome.png`.
- **Level:** polish. **Tag:** general.

##### 11. Read speaks clock time as "20 hours 22 minutes"
- **Where:** `speakText` `src.html:520`.
- **What:** for a grade 1 room on a projector, "twenty hours twenty-two minutes" is not how anyone says the time.
- **Seen:** audit row 18 ("November 5, 2026. 20 hours 22 minutes. Denver.").
- **Better:** "8:22 in the evening" (or "8:22 p.m.") when at home; keep 24-hour in the readout.
- **Level:** polish. **Tag:** general.

##### 12. Nits
- The time dial's focus ring overlaps its "TIME · 24 HOURS" label (`play/f1/keys-time.png`). nit, general.
- At the full 180 degree view looking straight up, the Ground lever has nothing to show, so the spec's "faint ground
  silhouette" first view does not appear (`audit-r1/size-1366x768.png`). nit, family:curiosity.

#### What worked (checked, nothing to report)

- Time dial drag is direct and crosses midnight into the next date (20:35 to 08:02 next day, `play/f5/drag-dial.png`).
  Arrow and Shift-Arrow steps on the dial work and focus is visible (`play/f1/keys-time.png`).
- Motion off: Play steps 10 minutes and the sky never runs on its own (`play/f1/calm-play.png`; audit "Motion off" clean).
- Same time each night holds the clock and steps the date (5 days in 6 s). Equator, North Pole, Sydney and 2800 BC all
  give clear, distinct skies (`play/f1/equator.png`, `north-pole.png`, `play/f3/sydney-sky.png`).
- Tapping a star selects it and opens the card (Vega, `play/f5/tap-vega.png`). The Manual drawer is tidy, with
  "Things people have found" as closed details, never targets (`play/f2/manual.png`).
- Frame times at 1366x768 with 1 day/s, Lines and Trails on: median 7 ms, worst 12 ms on this PC (not a Chromebook;
  Craft owns that).

#### Audit pilot

- **Leads confirmed:** none of the six leads is a fault. "Hint out of view" after every state is expected: the hint is
  meant to go after the first action.
- **Leads wrong:** the six "hint out of view" rows (see above).
- **Clean rows cited:** sizes, Motion off, resize mid-action, five clicks and two quick taps.
- **What it missed:** the stretched projection (finding 1; all its frames show it, but it cannot judge shape); the zoom
  buttons covering W (2: no clipped text, since the letter is canvas-drawn); the late hint speech (3: its table shows it,
  but it marks it "spoken", not wrong); missing constellation names (4); labels over the wrong stars (5); the
  "not in selection" message (6); the year window (7); the phone plate wrap (9).

No cultural, Native or hard-history content found. The tool leaves cultural sky stories out and credits star names as
identifiers.

<!-- end part -->

<!-- part: refine/teaching.md -->

### Refine, Teaching lens: sky-dome (Curiosity No. 05)

Judged against CODEX-CURIOSITY.md and VISION "Curiosities: the second shape", not lesson norms. Bundle as built
(`tools/sky-dome/sky-dome.html`), driven in headless Chrome (zone America/Denver). My frames and numbers are in
`S:/CurioClass-codex-scratch/sky-dome/teaching/` (`out/*.png`, `calc-out.json`, `calc2-out.json`). Reference values
fetched today from JPL Horizons (apparent RA/Dec, geocentric) and the USNO API (Denver rise/set, 2026 lunar phases).

Short version: the astronomy is excellent. Every position, time and phase I checked is right, well inside the spec's
tolerances. The gaps are in what a student can *find out* with it: no constellation is ever named, the Sun has no
distance, one reach module is not taught at all, and the Manual skips seasons.

#### Findings

1. **No constellation is named anywhere.** `src.html:953` draws `figure.slice(1)` only. Every figure's name
   (`DATA.figures[i][0]`, for example "Andromeda") is bundled but never shown, either on the dome or as a row on the
   object card. Several of the spec's Things to do cannot be answered: #4 "find which constellation the Sun is in",
   #7 "find the Southern Cross" (Acrux and Mimosa are labelled, but nothing says Crux) and #13 "find the Big Dipper"
   (Dubhe and Alioth are labelled, but there is no Ursa Major). Star patterns are the heart of the anchor's 1-ESS1-1.
   Better: a CONST row on the star, Sun, Moon and planet card, plus faint figure names while Lines is on.
   Seen: `out/noon-daylight-off-lines.png` (June 21 noon, Daylight off, Lines on, Sun selected: the Sun sits among
   lines between Taurus and Gemini, with no name anywhere), and the audit's `state-southern-sky-1366x768.png`.
   **should fix**, family:curiosity.

2. **The science-9 reach (HS-ESS1-1, HS-ESS1-2, HS-ESS1-3) is not taught by anything in the tool.** Those codes
   cover the Sun's life span and fusion, Big Bang evidence and stellar nucleosynthesis. Sky Dome shows positions,
   magnitude, B−V and an estimated temperature. That touches stellar properties, but none of the three codes.
   No activity in this instrument would reasonably teach them, so drop science-9-stars-and-the-big-bang from "Also
   reaches" (`spec.md:12-13`, and wherever the map row is written). Seen: code read of every readout
   (`updateObject`, `src.html:1103-1138`) against `data/modules.csv`. **should fix**, general.

3. **The Sun has no distance, so the 5-ESS1-1 reach can't be read off the instrument.** That module is "the Sun's
   apparent brightness compared with other stars depends on distance". The Sun card shows MAG −26.74 but no DIST
   (`src.html:1120-1128`). Planets get au and the Moon gets km. The comparison the standard wants (Sun 1 au, about
   8.3 light minutes, against Sirius at 8.6 ly) is therefore impossible. Add DIST to the Sun (au, plus light
   minutes). Also, of the 14 verified distances, the only bright-but-far star is Betelgeuse. Rigel, Deneb, Canopus
   and Antares all say "not verified", but they are the classic contrast with Sirius for Thing to do #11 ("some are
   bright because they are close"). NASA fact pages exist for at least Rigel and Canopus. Seen: `calc2-out.json`
   `sunCard` and `rigel`. **should fix** (the Sun DIST row); the extra star distances are polish. general.

4. **The Manual leaves out seasons and the Sun's path**, which the spec lists in its contents (`spec.md:72-73`) and
   which the anchor's 1-ESS1-2 (daylight across seasons) and MS-ESS1-1 depend on. "Why it changes"
   (`src.html:336-341`) explains the daily spin, why the night stars change through the year, Moon phases and planet
   loops. It never says that Earth's tilt makes the Sun's path higher and longer in summer, which is what the DAYLIGHT
   readout shows. Add a short paragraph, and add a daylight entry to "Things people have found". The instrument
   gives real numbers that match USNO: Denver 14 h 59 min on June 21 and 9 h 21 min on December 21. Seen: Manual
   read in full, plus `state-manual-1366x768.png`. **should fix**, family:curiosity.

5. **Read speaks clock time as a duration: "20 hours 22 minutes".** `speakText`, `src.html:520`, confirmed in
   audit row 18 ("November 5, 2026. 20 hours 22 minutes. Denver. ..."). The grade 1 class hearing this on a
   projector will take it as an amount of time, not a time of day. Better: "8:22 in the evening" (or "twenty
   twenty-two" for the 24-hour readout). BC years are spoken "2800 B C", which is fine. **should fix**, general.

6. **The Manual's language sits above the grade band and is mostly provenance.** Grades 5 to 9 drive this alone.
   Examples: "precessed to the chosen date" (309), "proleptic Gregorian calendar" (306), "truncated periodic
   expansion" (354), "equal-angle sky map fitted to an oval viewport" (356), "local mean solar time (longitude divided
   by 15)" (298). The honesty section and the sources section (352-442) read like a build log: 893 vertices matched,
   the Maradi/Niamey correction, "Factual numbers, not a copied protected presentation". All of it is honest, but a
   student looking for "why does the Moon rise later" wades through it. Better: plain sentences first, with each
   technical term glossed once. Move the dataset audit trail into a collapsed "Sources and checks" `details`, where
   the BSD terms already sit. **polish**, family:curiosity.

7. **Sirius's distance is shown two ways.** The card says "DIST 9 ly ≈" (`src.html:1123` rounds to whole light
   years). The Manual's found-note (349) and the spec say "about 8.6 light years". Alpha Centauri also becomes "4 ly"
   from 4.3. Anything shown twice should match: show one decimal under about 20 ly. Seen: `calc2-out.json` `card`.
   **polish**, general.

8. **"DIST not verified" reads as doubt about the star**, not as "not in this set" (`src.html:1123`). A student
   tapping Rigel may think its distance is disputed. Better: "not in this set" or "no checked value". **nit**,
   general.

9. **Compass letters at the poles.** At the South Pole frame the ring shows N, E, S and W as usual, but from
   either pole every direction is north (or south). The letters there come from an arbitrary meridian. Thing to do #6
   sends students to the poles, so either a one-line Manual note or dropping the letters when |LAT| > 89.9 would keep
   the ring from teaching something false. Seen: `state-southern-sky-1366x768.png`. **nit**, general.

10. **Year entry uses astronomical numbering.** Thing to do #12 says "set the year to 2800 BC", but typing −2800
   gives 2801 BC (the Manual says to enter −2799). The era label under the odometer does show "2801 BC", so nothing
   lies, but a kid will miss it. It could accept "2800 BC" typed, or the Up/Down steps could make the BC side
   obvious. **nit**, general.

#### Standards on the module

- **1-ESS1-1 (anchor, patterns of Sun, Moon and stars):** taught. Running time shows rising and setting and the
  still pole. The date wheel and Same time each night show the seasonal drift. Stepping days shows phases, LIT and
  AGE. Weakened only by finding 1.
- **1-ESS1-2 (anchor, daylight across the year):** taught by the DAYLIGHT readout, which matches USNO. Missing its
  Manual explanation (finding 4).
- **5-ESS1-2 (reach, shadows, day and night, seasonal stars):** day and night and seasonal stars are taught. Shadow
  length and direction are not: nothing shows a shadow. A small SHADOW readout on the Sun card (a 1 m stick's shadow
  length and direction from Sun ALT and AZ) would cover it; otherwise say the reach is partial. **polish**.
- **5-ESS1-1 (reach):** finding 3.
- **MS-ESS1-1 (reach, phases, eclipses, seasons):** phases are strong. Seasons are there in the readouts but not
  explained (finding 4). Eclipses can't be watched in the shadow sense ("No eclipse shadows are modelled"), though
  Sun and Moon conjunctions are visible. Acceptable as a reach.
- **HS-ESS1-1, -2, -3 (reach):** finding 2.

#### Done when (spec)

| # | Item | Result | Evidence |
|---|---|---|---|
| 1 | Opens on tonight over the time-zone city, no welcome, no permission | PASS | audit `size-1366x768.png`; zone America/Denver gives Denver 39.74, −104.99 |
| 2 | Ten stars within 0.1°, five planets within 1° | PASS | 12 Yale stars against SIMBAD J2000, all within 0.0002°. Horizons apparent RA/Dec: 7 bodies on 2026-11-05 plus Sun, Moon, Venus, Mars and Jupiter on 2026-03-20 and 2027-02-19 (17 checks), worst Saturn 0.074° |
| 3 | Denver solstices within 2 min of USNO | PASS | June 21: 05:32 / 20:31 (USNO 05:32 / 20:31). Dec 21: 07:17 / 16:38 (USNO 07:17 / 16:39) |
| 4 | Moon phase and age match USNO for three dates | PASS | Computed new Moons 2026-10-10 15:51 and 11-09 07:03 (USNO 15:50 and 07:02). At USNO first quarter LIT 50.0%, at full 99.8%, at last quarter 50.0%. Same time each night steps `addDays` at a fixed clock time (code read, not filmed) |
| 5 | 2800 BC puts Thuban within about 2° of the pole | PASS | rim reads "THUBAN · POLE OFFSET 0.1°" |
| 6 | Keyboard and 60 px targets | not mine | audit held-click and Enter-twice rows clean; Craft owns it |
| 7 | 60 fps | not mine | Craft |
| 8 | Layout and plate lower-left | cited | audit sizes clean |
| 9 | Motion off | cited | audit "Motion off: clean" |
| 10 | No network; sources in Manual and draft | sources PASS | network is Craft's |
| 12 | No score, goal, level, sticker or finish | PASS | lesson-creep grep of src.html: no hits; voice has one line, the hint |

#### Facts spot-checked (second source mine)

All matched: 12 star positions (SIMBAD J2000); 17 Sun, Moon and planet positions (JPL Horizons); Denver solstice
rise and set (USNO); 2026 new Moon times (USNO); Thuban 0.1° from the pole at 2800 BC (NASA SVS 13512 says about
2800 BC); Venus greatest elongation over 2026 to 2030 computed at 47.01° (NASA: about 47°); Mars 2027 retrograde
computed 2027-01-13 to 04-03 (published: about Jan 12 to Apr 2); Polaris altitude 40.19° at latitude 39.74°;
sidereal drift 3.94 min a day; Sirius −1.46, Betelgeuse B−V +1.85, Rigel −0.03 (BSC5); distances Sirius 8.6,
Procyon 11.4, Altair 17, Vega 25, Arcturus 37, Capella 43, Alpha Centauri 4.3, Betelgeuse 650 (NASA pages; Betelgeuse
is uncertain, about 550 to 700, and the card marks it ≈); daylight at the equator on Dec 21, 12 h 08 m; Sydney on
June 21, 9 h 53 m. No readout lies, and the dataset is not oversold: the 14 distances, 333 names and 1,238 places
are stated as selections.

#### Notes, home ideas, guardrails

`notes.md` is true of this tool. The home ideas are ones a family can do tonight, with a Sun-safety line. Grade 1 is
teacher-led per the spec and the notes. No hard history, health or Native content. Cultural sky stories are omitted
and star names are given as IAU identifiers with no origin claims, so **nothing to send for a sensitivity review**.
If sky stories are added later (spec Open questions), they need one.

#### Audit pilot

- **Leads confirmed:** none.
- **Leads wrong:** all six ("hint out of view: Drag the time dial." in running, star-readout, southern-sky,
  ancient-pole, phone-place and deep-readout). Each state starts with an action, and a Curiosity's hint is meant to
  go after the first action. Correct behaviour, not a fault.
- **What it missed:** no constellation names (it can't judge whether a task is answerable); Read speaking the time
  as a duration (it logged the line but can't judge wording); the Sun card missing DIST; Sirius 9 ly on the card
  against 8.6 in the Manual; compass letters at the poles; the Manual missing seasons.

<!-- end part -->

## Fix

<!-- part: polish.md -->

### Polish: sky-dome (Codex fix, round 2)

Should fix 2 remains NOT FIXED. The renderer is substantially faster, but actual 4x-throttled night frame delivery still fails 60 fps. No passing claim is based only on draw duration or on daylight. The current refine.md exit check had already closed the other items; they are retained and regression-checked below, rather than presented as new fixes. No questions were asked during this unattended run. The Curiosity brief takes precedence over lesson gates: no welcome, goal, score, level, quiz, finish or kit header was introduced.

Work ran from S:/CurioClass-codex. Writes stayed in tools/sky-dome/ and _scratch/sky-dome/. No commits; refine.md and refine/ untouched. Chrome 9920 through 9925 and host 8725 only. Evidence paths below are relative to _scratch/sky-dome/.

#### Blocker

1. **FIXED in round 1, retained: stretched sky.** Equal-radius projection, inverse projection and ring are unchanged. Fresh Orion at FOV 50 and the 22:00/04:00 Dipper pair: r2-regression/orion.png, dipper-22.png, dipper-04.png. Round rings and clear compass letters at all tested sizes: r2-sizes/. The new GPU star projection was independently checked by reading the actual point pixels for ten stars: maximum centroid discrepancy 0.02889 px, equivalent to 0.01045 degrees on this dome (r2-gpu-positions.json). That checks rendering against the unchanged reference projection, not a new observational validation of the catalogue.

#### Should fix

1. **FIXED in round 1, retained: constellation names.** Fresh Sydney shows Crux and Centaurus; star, Sun and Moon cards retain CONST. See r2-regression/sydney.png, sun-card.png and r2-states/moon-card.png, sirius-card.png, ancient.png. Constellation function unchanged.
2. **NOT FIXED: 60 fps at 4x throttle.** Reproduced at 1366x768, Denver winter night, Play 1 h/s, Lines, Names, Ground, Milky Way and Trails on: draw median 23.6 ms/p95 30.0; frame interval median 76.9 ms/p95 89.0 (r2-before-4x.json, r2-before-night/night-4x.png). Final: draw median 10.1 ms/p95 13.1, but frame interval median 45.1 ms/p95 53.7, about 22 fps (r2-final-night-4x.json, r2-precision/final-night-4x.png). At 1x: draw median 1.9 ms, frame interval median 15.6 ms (r2-final-night-1x.json). Each final sample set contains 90 observed rAF intervals after warmup, with daylight enabled and the entire sample in astronomical night. A prior all-night layer run gave 8.6 ms draw and 36.1 ms frame intervals; the final, slower result is reported. The renderer uses one GPU point buffer for all 9,096 stars, uploads date-precessed vectors once per date, and composites directly between background and foreground canvases. CPU projection remains for bright stars/line endpoints, with full projection on a tap. No stars or lines were culled to obtain a number. The canvas fallback remains. The slower CPU pixel tile was discarded. The bounded optimization pass ended with the real gate still open.
3. **FIXED in round 1, retained: zoom hides W.** N/E/S/W and zoom are clear in r2-sizes/ at 680x425, 1280x720, 1366x768 and 1920x1080; phone evidence comes from the audit. Controls and ring geometry unchanged.
4. **FIXED in round 1, retained: late spoken hint.** Held-click Play-first path logs no hint; Lines-first path logs exactly one hint and one later Read. r2-voice-time.json and r2-voice-nontime.json. Hint handlers unchanged; audit covers the other time controls.
5. **FIXED in round 1, retained: Sun distance.** Fresh card shows 1.016 au and 8.5 light min on June 21: r2-regression/sun-card.png and r2-sun-card.json. Orbit and Sun-distance calculations unchanged.
6. **FIXED in round 1, retained: seasons.** Manual retains the tilt/Sun-path paragraph and sourced Denver solstice discovery entry. Manual text unchanged; r2-states/manual.png and final audit Manual states.
7. **FIXED in round 1, retained: wheel engravings.** Dark 9-unit engraving and gold halo unchanged. Fresh r2-sizes/size-680x425.png and size-800x500.png show the scale. Original checked contrast is 9.39:1; no colour or engraving change this round.
8. **FIXED in round 1, retained: clock as duration.** Held-click Read says "8:22 in the evening" while the screen reads 20:22: r2-voice-nontime.json. speakText is byte-for-byte unchanged.
9. **FIXED in round 1, retained: star-label collisions.** Fresh Sydney at May 1, 20:04 solar time has Acrux, Hadar, Crux and one Rigil Kentaurus / Toliman label: r2-regression/sydney.png, r2-sydney.json. Collision reservations and leader placement unchanged.
10. **FIXED in round 1, retained: Sydney ambiguity.** Both Australia and Canada choices remain visible: r2-states/sydney-search.png. Search handler unchanged.
11. **FIXED in round 1, retained: Escape focus.** Real Escape in the city field leaves focus in city: r2-escape-input.json. Handler unchanged; r2-extra/escape-input.png.

#### Polish accepted

1. **FIXED in round 1, retained:** plain Manual and collapsed Sources and checks; no text removed. r2-states/manual.png; source unchanged.
2. **FIXED in round 1, retained:** Sirius card says 8.6 ly. r2-states/sirius-card.png and r2-sirius-card.json.
3. **FIXED within the round 1 skip allowance, retained:** checked Rigel/Antares facts remain; Canopus and Deneb still have no checked distance. No dataset or distance fact changed.
4. **FIXED in round 1, retained:** typing 2800 BC reaches astronomical -2799 and shows 2800/BC. r2-states/ancient.png and r2-ancient.json.
5. **FIXED in round 1, retained:** Sun, Moon and planet labels remain in daylight. r2-states/daylight.png and default.png.
6. **FIXED in round 1, retained:** one-line plate/rivet spacing unchanged; r2-sizes/size-680x425.png, size-800x500.png, plus phone audit frames.
7. **FIXED in round 1, retained:** phone dome/readout layout unchanged; phone audit frames keep rise/set and the lower hint.
8. **FIXED in round 1, retained:** visible-name live-region wording unchanged, including Milky Way and latitude directions.
9. **FIXED in round 1, retained:** brass detent rate knob and REV unchanged and visible in r2-sizes/.
10. **FIXED in round 1, retained:** conditional deep-sky range wording unchanged; final audit includes the deep readout.
11. **FIXED in round 1, retained:** missing distance remains "no checked value"; r2-states/ancient.png and r2-extra/faint-picking.png.
12. **FIXED in round 1, retained:** polar compass explanation remains in the unchanged Manual.
13. **FIXED in round 1, retained:** inset wheel focus outline unchanged; audit keyboard walk checks the wheel.
14. **FIXED in round 1, retained:** ring clears AGE at 680x425; r2-sizes/size-680x425.png.

#### Settled calls

- Kept the Curiosity's one quiet first-run hint. Hidden-hint audit leads are interpreted under the existing settled call, without adding a welcome or continuing instruction.
- Astronomy, tolerances, Same time each night, Motion-off stepping, Read/Sound semantics, honest missing values and offline operation remain. Fourteen reference astronomy/projection/reading functions compare equal to the saved original (r2-preserved.json); the data SHA256 also compares equal.
- No cultural sky stories or origin claims added. No people art or sensitivity scope added.
- Spec open questions, Not taken items and the integrator-only note were left alone. No new standard reach or shadow readout was claimed.
- Unattended choice: retain and report the open performance gate; do not substitute daytime figures, remove faint stars/lines, lower resolution or claim physical Chromebook validation.

#### Cheats tried

There is no score, check, quiz or skill gate to pass. Instrument attempts: 18 combinations of latitude -90/0/90, camera altitude -90/0/90, and FOV 20/180, with Ground off; every projected coordinate finite (r2-extremes.json). A real sky tap picked faint HR 4, magnitude 5.51, after the fast path had been running (r2-faint-picking.json). Forced WebGL context loss recovered the canvas sky with 4,605 visible stellar nodes at the test time (r2-fallback.json, r2-states/fallback.png). Motion off Play stepped time, then left it unchanged for 1.2 seconds (r2-motion-off.json). Audit adds resize stress and keyboard input. Performance testing kept all stars/lines on and stayed in night, closing the cheap daytime-measurement escape but not the performance item.

#### Voice walk

120 ms held clicks, 2-second gaps. Lines, Trails, Read: one "Drag the time dial." followed by "January 14, 2026. 8:22 in the evening. Denver. Moon, Waning crescent, 13 percent lit." Play, Pause, Read: no hint; Read speaks the new current time, "8:43 in the evening". r2-voice-nontime.json and r2-voice-time.json. allLines() equals voice/lines.json: one fixed line. No voice code or lines changed. Existing calm-professor recording is still absent; the bundle uses the existing browser fallback.

#### Engine changes wanted

None. The rendering change is tool-local; kit and scripts unchanged. Handoff documents the new draw(true) diagnostic/full-picking path and context-loss fallback.

#### Audit

One full audit finished within the 2,400-second limit, Chrome 9921, host 8725. See r2-audit/audit.md. 10 mechanical leads were reviewed: eight hidden-hint state leads plus two quick-tap hint cuts on Year era and Now. All are the previously settled Curiosity behavior: the first-action hint disappears, and moving time ends it. No welcome or persistent hint was added. Every size is clean; the 21-control held-click/Enter walk has no errors, focus loss or shifted controls; repeated how-to lines do not repeat; Motion off and resize stress are clean. All 30 audit frames were inspected. No new confirmed defect was found.

Final bundle: 591,705 bytes, SHA256 40a3a00818fe9b1339093ad4cc3e23d7a1047b1dd9c888b524fa7a562ba5963c. All 30 saved resource probes show zero automatic requests. The final driver batches have zero product console warnings/errors/exceptions. The fixed recording is still absent, as the existing bundle warning states. The audit does not measure frame rate; the separate all-night 4x measure above keeps Done when 7 open. Driver/audit cleanup exited successfully and all seven used test ports were confirmed closed before this report was written (r2-ports-closed.json). An additional orphan-process inventory was denied by Windows CIM permissions; it did not identify or terminate any unrelated process.

#### The real material

No gathering or new facts were needed. sky-data.json is byte-for-byte unchanged from the saved starting file; all source entries and licence text remain in the Manual and tool.draft.json. Previous download dates are 2026-11-05, not represented as fresh downloads this round. This round changes drawing machinery and retains the original numerical readouts.

| Material used | Named source and licence | Scope retained |
|---|---|---|
| Stars, magnitudes, B-V, proper motion, spectra | Hoffleit and Warren, Yale BSC5, [NASA HEASARC](https://heasarc.gsfc.nasa.gov/W3Browse/star-catalog/bsc5p.html), public domain / US Government Works; existing CDS/CfA comparison | All 9,096 bundled stellar records; all 8,786 measured colours. Existing display colour/opacity bins retained. No resampling. |
| Proper names | IAU WGSN, [2022-04-04 snapshot](https://github.com/mirandadam/iau-starnames/blob/master/catalog_data/IAU-CSN.txt), Creative Commons Attribution as stated in its header; existing Manual links current IAU CC BY 4.0 text policy | Same 333 HR-matched names and attribution; no etymologies. |
| Constellation figures, areas and names | Olaf Frohn, [d3-celestial](https://github.com/ofrohn/d3-celestial), BSD 3-Clause, expressly allowed fallback; full licence in Manual; existing IAU name/chart cross-check | All 88 figures and all existing area/label records. CPU continues to project every line endpoint. |
| Sun, Moon, planets and transformations | [JPL Standish/Williams approximate elements](https://ssd.jpl.nasa.gov/planets/approx_pos.html), government numerical facts; Jean Meeus, Astronomical Algorithms, independently implemented mathematics, no reproduced book prose or code | Original ephemerides, precession, phases, rise/set and readouts unchanged. New original vertex shader applies the same observer rotation, average refraction and equal-angle mapping. Actual GPU pixels checked against the reference calculation. |
| Places | [Natural Earth populated places](https://www.naturalearthdata.com/about/terms-of-use/), public domain, and existing [Wikidata](https://www.wikidata.org/wiki/Wikidata:Licensing) coordinate checks, CC0 | Same 1,238 entries, corrections and home-zone mapping. |
| Deep-sky markers | NASA HEASARC Messier numerical facts, public domain / US Government Works; existing SEDS independent checks, no protected prose/images reproduced | Same 20 records, magnitude ranges and uncertainty notes. |
| Distances, seasons and discovery notes | Existing NASA/JPL/USNO public-domain factual material, with two-source records and URLs retained in Manual/tool.draft.json and round 1 polish report | Same 16 checked distances; no inferred values or new numerical fact. Canopus/Deneb omissions retained. |

#### Lesson creep check

r2-verification.json records eleven lexical hits: nine geometric point-array or WebGL POINTS references, "minute-level model errors", and the historical name list's "complete current list". None is a score, task or reward. No em dash appears in src.html. No lesson flow was added; changes are decorative drawing surfaces, a rendering buffer and on-demand projection.

#### Frames looked at

Fresh Orion FOV 50, Dipper pair, Sydney, size contact sheet (seven sizes), ten-state contact sheet (Manual, object cards, BC year, daylight, grid, search and fallback), six-frame voice/input/extreme sheet. Individual 1366 and 680/800 scenes were also inspected at their actual sizes. All 30 audit frames were inspected through four contact sheets; the default, running and Sydney phone frames were also opened individually. Before/after night timing frames were opened. The initial size-probe script declared its test variable twice; that probe was corrected and all seven size shots rerun successfully in r2-sizes/. No product error was involved.

#### Left open

- Should fix 2 / Done when 7: 4x night frame interval remains above 16.7 ms. It is still an open exit gate.
- Existing recording-production item: absent calm-professor fixed recording.
- Existing Canopus/Deneb omissions remain within the accepted skip allowance.
- Spec open questions remain for the integrator.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Sky Dome build handoff

`src.html` holds the observatory CSS, accessible controls, Manual and independent astronomy/rendering code. `sky-data.json` holds a compact binary catalogue, spectra, flags, names, figures, cities and markers; bundle_tool inlines it and kit/curio.js. Edit source, then rebundle with CURIO_DRAFT=1.

#### Data and calculations

Second-build raw sources and manifests are in `_scratch/sky-dome/data/second/`. `gather2.py`, `gather_checks2.py`, `distance_sources2.py` and `retry_wiki2.py` preserve bounded downloads. `place_check2.py` verifies city centres. For repacking after this review, run `_scratch/sky-dome/review_pack.py`, then bundle. It wraps `pack2.py` with the verified Maradi name correction before sorting cities and computing zone indexes. Do not run pack2.py alone: it restores the Natural Earth error that misnames Maradi as Niamey and selects the wrong home city for Africa/Niamey. Fourteen non-stellar HR rows are excluded. Every retained B-V and other required star field agrees across HEASARC and CDS/CfA. Thirteen unverified or conflicting city entries are omitted, leaving 1,238. The source's timezone fields provide 302 home-zone names/aliases, with direct city-name matching too. IANA was investigated but is not bundled; Natural Earth supplied the needed zone identifiers.

The star record is 18 bytes, little-endian: uint16 HR, uint32 RA times 100000, int32 DEC times 100000, int16 magnitude times 100, int16 pmRA and pmDEC times 1000, int16 B-V times 100. B-V -32768 means missing. Spectra and uncertainty/variable flags stay alongside. Keep missing measurements missing.

All 88 figures use the explicit d3-celestial BSD fallback, converted to HR paths; all 893 endpoint occurrences match Yale within 0.003 degrees. The licence text is embedded in the Manual. The IAU list validates identities; its archive was unavailable. Do not claim a new hand tracing or a separate observational validation of this conventional connectivity. The 20 lowest-magnitude HEASARC Messier rows have separate SEDS checks; magnitude differences appear as ranges. M41 centre disagreement is documented.

Fourteen distances use the specification's NASA fact-page fallback, with second-source checks in `distance-checks.json`. ESA's public catalogue page now specifies CC BY-NC 3.0 IGO; do not redistribute it under this brief. All astronomy code remains independently written; no astronomy library is bundled.

#### Tricky parts

Sky coordinates have epoch-of-date precession and proper motion. Planet coordinates begin in J2000 ecliptic coordinates; they must be precessed before the horizontal transform. The Moon has topocentric parallax. Its previous conjunction is solved numerically even across a cycle boundary, rather than subtracting a mean month; the display explicitly rounds the uncertain conjunction boundary to approximately zero. Raw age remains available for numerical checks. Home clock and away solar clock use different midnight calculations. Year zero means 1 BC.

The ordinary Tab path skips the long sky-object list. Dome deliberately focuses the canvas; Tab then visits its bright objects, and J visits Messier markers. Preserve the readout-card clearance below the top telemetry and above the bottom rim at desktop, short-preview and phone breakpoints. Tall cards scroll. Catalogue variability IDs can include suspected entries, so the UI says "variability listed" rather than asserting confirmed variation. Planet magnitudes remain unmodelled and explicitly unavailable; their navigation entries precede catalogue-ranked stars.

#### Engine changes wanted

None. The shared kit is unchanged. The local power labels remove decorative kit emoji after shared setting handlers run.

#### Cold review changes

The first instrument gesture now queues the single hint through Curio.voice; it is no longer restricted to opening Manual. Read pauses transport and uses spoken month/time units. Keep automatic narration to that one hint. Dynamic sky readings remain browser speech, with the fixed line listed in voice/lines.json.

Numeric change handlers immediately reconcile committed values, including blank input, with the model. Year changes preserve the local civil clock and clamp leap-day dates. Home/End is specific to each wheel, with a leap-year date range. On pinch release, the remaining pointer's drag origin is rebased. The rim chooses the closest named star to the appropriate pole from the date-precessed catalogue.

Horizon events scan from one local midnight to the next, including 23/25-hour daylight-saving dates at home. Keep that interval separate from a fixed 24-hour astronomical day. The phone transport keeps Reverse visible; its primary Play/Now/Place controls remain 60 px and Reverse meets the secondary 44 px width.

Time clamps use local calendar years, including after place changes near the year endpoints. The renderer caches observer/precession bases and date-updated stellar unit vectors, and projects those vectors directly with the same refraction. The original star disks/glows and all colours remain; a slower sprite-atlas experiment was removed. The Milky Way geometry is date-cached like the stars. Equatorial grid coordinates are already in the current-date frame and must not be precessed again. Preserve the reference horizontal/project helpers and _scratch/sky-dome/review-render-parity.json when changing this fast path.

Phone dial captions reserve their own row; short-preview captions do not wrap. Deep-sky labels share collision reservations with star labels and telemetry, while every marker remains selectable. The Moon's shadow uses the local sky background and its glow scales with illuminated fraction. Duplicate city-and-country names receive coordinate suffixes without changing the source data or zone indexes.

Independent review evidence is under _scratch/sky-dome/review-*. Fresh USNO solstice and November 2026 phase responses are in data/review/. Current IAU licensing is linked in the Manual. The review report supersedes old open-verification claims only where it supplies fresh evidence. Maradi's corrected name is corroborated by Natural Earth's NAMEASCII and Wikidata Q664550; the separate Niamey record Q3674 supplies the correct home-zone city.

#### Sensitivity

No cultural narratives, etymologies or illustrations of people are included. Constellation figures are explicitly a modern convention rather than universal sky boundaries. IAU proper names remain credited identifiers. A later addition of cultural stories needs its own fresh sensitivity review.

#### Follow-up material

The final audit's only five mechanical leads were the required hidden first-run hint. Its frames exposed canvas-name clipping, repaired by testing each label's corners against the oval and trying the left side for stars near its edge. Focused re-shoots and glyph-corner checks cover every standard viewport. Read's singular hour/minute wording was re-walked, including Sound off. The southern audit fixture now changes the real city control so its city field and coordinates agree.

Keep `codex-report-1.md` as historical evidence. This is a second Build, with no commits, shared changes, deployment or polish round. Recorded narration and actual Chromebook performance remain separate verification needs. Cultural sky stories stay omitted as the spec advises. The fresh report names any reference services that remained unreachable.

#### Refine round 1

The current merged list is refine.md and the item-by-item outcome is polish.md. No shared engine files or review
files were edited. The scientific position, phase, rise/set, precession and orbital functions are unchanged:
_scratch/sky-dome/fix-math-preserved.json records the comparison. Projection and its inverse now use one radius.

The star renderer batches display colours/opacity, caches overlay geometry and fonts, and uses sampled refraction
only in rendering. Exact horizontal() still owns all object readouts. The renderer lookup's high-altitude and
minus-one-degree discontinuities are handled exactly. Keep fix-numbers.json's angular/pixel parity checks when
changing this path. Sprite atlas, reusable transformed paths and SVG string paths were slower and were removed.
The 4x CPU target is still an explicit open gate unless polish.md supplies a passing final measurement.

Constellation areas and labels are from the specified d3-celestial BSD fallback, with the complete existing notice
retained in the Manual. Spherical polygon orientation uses signed triangle area, including concave Draco and polar
areas; the inverse precession basis puts the readout direction back in the source's J2000 frame. Raw downloads and
licence checks are in _scratch/sky-dome/data/fix/. Repack with fix_pack_data.py in Scratch. Added checked distance
facts are Rigel and Antares only; Canopus and Deneb were omitted under the item's explicit skip allowance.

The hint uses Curio.voice's wait promise: no time-control first hint, and a non-time first hint stays visible until
the line resolves or time changes. There is one fixed voice line; Read remains dynamic and works with Sound off.
The visual rate knob is a keyboard slider. Sydney's duplicate matches are ordinary keyboard buttons.

No welcome, task list, score, quiz, levels, finish or kit header was added. Source URLs, dates, licences, sampling and
limitations are recorded in the Manual, tool.draft.json and polish.md. The unresolved spec questions stay untouched.

#### Refine round 2

The remaining list item is Should fix 2, night-time performance. The new star surface uses one WebGL point buffer,
with the date-precessed catalogue vectors uploaded only when their date changes. Its vertex shader applies the
existing observer rotation, average refraction and equal-angle projection. The browser composites the surface
between the drawn background and the labels, lines, bodies, ground and ring, avoiding a synchronous canvas copy.
Colours and opacity retain the existing display bins; catalogue values, sources and licences are unchanged.

The CPU still projects bright stars and every constellation endpoint each frame. A sky tap projects the full
catalogue before hit testing, so faint stars remain selectable. `draw(true)` explicitly requests those full projected
nodes for diagnostics. If WebGL is absent or its context is lost, the existing canvas batches render the full sky.
All decorative canvases are hidden from accessibility APIs and pointer input; the original sky canvas owns input.

This improves rendering but does not establish 60 fps at 4x CPU throttle. See the round 2 polish report and
`_scratch/sky-dome/r2-*-perf.json` for draw times and actual frame intervals. Keep Done when 7 open unless a final
measurement there explicitly passes it. The CPU pixel-tile experiment was slower and was removed.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-07)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-07)
- 2026-11-25: refine.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/craft.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/play.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-11-07)
- 2026-11-25: polish.md folded in (last changed 2026-11-07)
- 2026-11-25: handoff.md folded in (last changed 2026-11-07)
- 2026-11-25: earlier round codex-report-1.md moved to S:/CurioClass-archive/tool-rounds-2026-11-25/sky-dome
- 2026-11-25: earlier round polish-1.md moved to S:/CurioClass-archive/tool-rounds-2026-11-25/sky-dome

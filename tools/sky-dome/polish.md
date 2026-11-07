# Polish: sky-dome (Codex fix, round 2)

Should fix 2 remains NOT FIXED. The renderer is substantially faster, but actual 4x-throttled night frame delivery still fails 60 fps. No passing claim is based only on draw duration or on daylight. The current refine.md exit check had already closed the other items; they are retained and regression-checked below, rather than presented as new fixes. No questions were asked during this unattended run. The Curiosity brief takes precedence over lesson gates: no welcome, goal, score, level, quiz, finish or kit header was introduced.

Work ran from S:/CurioClass-codex. Writes stayed in tools/sky-dome/ and _scratch/sky-dome/. No commits; refine.md and refine/ untouched. Chrome 9920 through 9925 and host 8725 only. Evidence paths below are relative to _scratch/sky-dome/.

## Blocker

1. **FIXED in round 1, retained: stretched sky.** Equal-radius projection, inverse projection and ring are unchanged. Fresh Orion at FOV 50 and the 22:00/04:00 Dipper pair: r2-regression/orion.png, dipper-22.png, dipper-04.png. Round rings and clear compass letters at all tested sizes: r2-sizes/. The new GPU star projection was independently checked by reading the actual point pixels for ten stars: maximum centroid discrepancy 0.02889 px, equivalent to 0.01045 degrees on this dome (r2-gpu-positions.json). That checks rendering against the unchanged reference projection, not a new observational validation of the catalogue.

## Should fix

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

## Polish accepted

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

## Settled calls

- Kept the Curiosity's one quiet first-run hint. Hidden-hint audit leads are interpreted under the existing settled call, without adding a welcome or continuing instruction.
- Astronomy, tolerances, Same time each night, Motion-off stepping, Read/Sound semantics, honest missing values and offline operation remain. Fourteen reference astronomy/projection/reading functions compare equal to the saved original (r2-preserved.json); the data SHA256 also compares equal.
- No cultural sky stories or origin claims added. No people art or sensitivity scope added.
- Spec open questions, Not taken items and the integrator-only note were left alone. No new standard reach or shadow readout was claimed.
- Unattended choice: retain and report the open performance gate; do not substitute daytime figures, remove faint stars/lines, lower resolution or claim physical Chromebook validation.

## Cheats tried

There is no score, check, quiz or skill gate to pass. Instrument attempts: 18 combinations of latitude -90/0/90, camera altitude -90/0/90, and FOV 20/180, with Ground off; every projected coordinate finite (r2-extremes.json). A real sky tap picked faint HR 4, magnitude 5.51, after the fast path had been running (r2-faint-picking.json). Forced WebGL context loss recovered the canvas sky with 4,605 visible stellar nodes at the test time (r2-fallback.json, r2-states/fallback.png). Motion off Play stepped time, then left it unchanged for 1.2 seconds (r2-motion-off.json). Audit adds resize stress and keyboard input. Performance testing kept all stars/lines on and stayed in night, closing the cheap daytime-measurement escape but not the performance item.

## Voice walk

120 ms held clicks, 2-second gaps. Lines, Trails, Read: one "Drag the time dial." followed by "January 14, 2026. 8:22 in the evening. Denver. Moon, Waning crescent, 13 percent lit." Play, Pause, Read: no hint; Read speaks the new current time, "8:43 in the evening". r2-voice-nontime.json and r2-voice-time.json. allLines() equals voice/lines.json: one fixed line. No voice code or lines changed. Existing calm-professor recording is still absent; the bundle uses the existing browser fallback.

## Engine changes wanted

None. The rendering change is tool-local; kit and scripts unchanged. Handoff documents the new draw(true) diagnostic/full-picking path and context-loss fallback.

## Audit

One full audit finished within the 2,400-second limit, Chrome 9921, host 8725. See r2-audit/audit.md. 10 mechanical leads were reviewed: eight hidden-hint state leads plus two quick-tap hint cuts on Year era and Now. All are the previously settled Curiosity behavior: the first-action hint disappears, and moving time ends it. No welcome or persistent hint was added. Every size is clean; the 21-control held-click/Enter walk has no errors, focus loss or shifted controls; repeated how-to lines do not repeat; Motion off and resize stress are clean. All 30 audit frames were inspected. No new confirmed defect was found.

Final bundle: 591,705 bytes, SHA256 40a3a00818fe9b1339093ad4cc3e23d7a1047b1dd9c888b524fa7a562ba5963c. All 30 saved resource probes show zero automatic requests. The final driver batches have zero product console warnings/errors/exceptions. The fixed recording is still absent, as the existing bundle warning states. The audit does not measure frame rate; the separate all-night 4x measure above keeps Done when 7 open. Driver/audit cleanup exited successfully and all seven used test ports were confirmed closed before this report was written (r2-ports-closed.json). An additional orphan-process inventory was denied by Windows CIM permissions; it did not identify or terminate any unrelated process.

## The real material

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

## Lesson creep check

r2-verification.json records eleven lexical hits: nine geometric point-array or WebGL POINTS references, "minute-level model errors", and the historical name list's "complete current list". None is a score, task or reward. No em dash appears in src.html. No lesson flow was added; changes are decorative drawing surfaces, a rendering buffer and on-demand projection.

## Frames looked at

Fresh Orion FOV 50, Dipper pair, Sydney, size contact sheet (seven sizes), ten-state contact sheet (Manual, object cards, BC year, daylight, grid, search and fallback), six-frame voice/input/extreme sheet. Individual 1366 and 680/800 scenes were also inspected at their actual sizes. All 30 audit frames were inspected through four contact sheets; the default, running and Sydney phone frames were also opened individually. Before/after night timing frames were opened. The initial size-probe script declared its test variable twice; that probe was corrected and all seven size shots rerun successfully in r2-sizes/. No product error was involved.

## Left open

- Should fix 2 / Done when 7: 4x night frame interval remains above 16.7 ms. It is still an open exit gate.
- Existing recording-production item: absent calm-professor fixed recording.
- Existing Canopus/Deneb omissions remain within the accepted skip allowance.
- Spec open questions remain for the integrator.

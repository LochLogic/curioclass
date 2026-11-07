# Polish: living-earth (Codex fix, round 1)

Evidence paths below are relative to `_scratch/living-earth/`. The bundle is `tools/living-earth/living-earth.html`. All blocker and should-fix causes were reproduced before editing. No changes were made to `refine.md`, its review folder, the packed material, the kit, or other tools. No commits were made.

## Blocker

1. **FIXED: plate reference-frame drift.** Removed the area-weighted shared rotation from the original Merdith 0-5 Ma angular velocities, using a 5-degree surface grid and its full inertia tensor. Resolved coverage is 99.811%. Denver changes from 6.2 cm/yr at 253° to 1.6 at 247°; Sydney from 2.8 at 325° to 5.9 at 17°. All five supplied ITRF2014 comparisons pass, with maximum errors 0.28 cm/yr and 5.45°. Pin adds relative normal EDGE MOTION; the equatorial Atlantic example opens at 3.3 cm/yr. Arrows use the same corrected motion. The fingernail note now describes a few centimetres per year and distinguishes relative spreading. Proof: `fix-before/motion.png`, `fix-after/motion.png`, `fix-after-motion.json`, `fix-independent-numbers.json`; reproducible derivation in `fix_nnr.js`. Merdith is retained for Rewind; no replacement model was introduced.

## Should fix

1. **FIXED: S marker cannot be dragged first.** S starts at 1560 s, P and S have separate labelled grab handles, and each has its own placement flag. At 1366x768 the real S-first drag previously changed P to 1057 s with S still 0; afterward it changes S to 1057.5 s with P still 0. Proof: `fix-before/station-S.png`, `fix-after/station-S.png`, their JSON probes, and `fix-phone/phone-stations.png` at 375x812. Marker labels no longer coincide at zero.
2. **FIXED: first-run speech asks for an action already done.** First Play speaks only “Drag to spin.” First drag speaks only “Press play.” Opening Slice first speaks nothing. Both halves have validity checks. Proof: `fix-before-voice-play.json`, `fix-before-voice-slice.json`, `fix-after-voice-play.json`, `fix-after-voice-drag.json`, `fix-after-voice-slice.json`; held native repeat walk in `fix-native-results.json` records one automatic line.
3. **FIXED: sea floor plotted below shallow quakes.** Relief is in a separate labelled sea-level/sea-floor strip above the true-depth plot. Its vertical scale is exactly 20 times the horizontal kilometre scale; quake axes stay 1:1. The Mid-Atlantic sample retains the same 12 quakes, 10-33 km deep. Proof at 1366x768: `fix-before/slice-mar.png`, `fix-verified/section-1366.png`; compact proofs at 680x425, 800x500 and 760x900 in `fix-delivery/` and `fix-breakpoint/`.
4. **FIXED: inconsistent wave edges and unreachable arrival.** The direct-branch table sets P's edge at 98°, S's at 99°, and the far-side P return at 140°. The ring and arc use that S edge. The window and trace now reach 1560 s; the last S at 99° is 1514.185 s and is reachable. Missing arrivals say “no direct wave here” after the appropriate front arrives; before then they say “await rays”. The Manual explains omitted diffraction and the textbook 104° comparison. Proof: `fix-before/wave-100.png`, `fix-independent-numbers.json`, `fix-after/wave-end.png`, `fix-wave-timing/wave-0.png`, `fix-wave-timing/wave-1560.png`, all at 1366x768.
5. **FIXED: station words and verdict do not follow state.** The visible status follows placement, Strike, marker measurement, Circles and Reveal. Unplaced markers produce no distance circles. FIT text and its 200 km label threshold are removed; CATALOG has a numerical offset, and Reveal has no OUTSIDE FILTERS tag. The measured example has an 8 km offset. Proof: `fix-before/station-reveal.png`, `fix-final-targets/final-stations-measured.png`, `fix-native-results.json`, `fix-audit-followup/stations-680.png`, and the 375x812 Reveal in `fix-phone/phone-stations.png`.
6. **FIXED: geophysicist-first language.** Each how-to Manual section opens with plain sentences, followed by “For the curious” and the retained precise limitations. Captions use plain words, S-P has a short explanation beside the markers at laptop size, the unknown plate wording is plain, and findings are shorter. Proof: `fix-before/manual.png`, `fix-after/manual.png`, the Manual's eight audit size frames and `src.html`. Instructions formerly opening the findings section now belong to the relevant how-to sections.
7. **FIXED: selected record covers the globe.** The record docks as one line at the top of an open instrument. At 680x425 and 800x500 with no tool it occupies its own line between globe and toolbelt. The open Stations overlap was reproduced at 1366x768; the Sumatra closed-tool selections at 680/800 stayed just left of the globe, so those particular overlap variants were not reproduced. Their final collapsed layouts were inspected. Proof: `fix-before/station-reveal.png`, `fix-final-targets/final-stations-measured.png`, `fix-delivery/selected-680.png`, `fix-delivery/selected-800.png`. The compact selector and record are also separate: selector bottom 84 px, record top 84 px, in `fix-last-reveal-680.json`.
8. **FIXED: shortcuts stop on focused buttons.** Letter and bracket shortcuts pass through button focus. Space plays with globe/Play focus and activates another focused button normally; the Manual states this rule. Native Q/V/P/F/A each toggle after button clicks, bracket changes speed to index 2, Space starts transport from the globe, and Space toggles a focused Volcanoes button. Proof: `fix-before-keyboard.json`, `fix-after-keyboard.json`, `fix-native-results.json`; S also triggers Strike and a native station-B tap selects channel 1.
9. **FIXED: volcano rendering halves frame rate.** Volcanoes now use one GPU triangle-point layer; the canvas fallback batches triangles into one path. Shader locations and arrow vectors are cached. The paired 1366x768, 4x CPU test changes the volcano median frame interval from 33.4 ms to 16.7 ms and the all-layer median from 33.4 ms to 16.7 ms. Per-frame volcano canvas fills/strokes fall from 920/920 to 0/0 with WebGL. Proof: `fix-raf-before.json`, `fix-raf-after.json`, `fix-raf-pair-perf/`. Mean intervals remain 17.2 ms with volcanoes and 20.2 ms with all layers, so sustained 60 fps is not claimed.
10. **FIXED: compact labels and plots collapse.** D ≥ / D ≤ remain visible on the joined depth track; readouts have separators and layer switches keep their names. Compact tool panels receive usable space, and portrait plots stack below the globe. Final section heights are 110 px at 680x425, 184 px at 800x500 and 190 px at 760x900. Station traces are wider, their ruler stays in view, and the slim drum is 44 px high. The audit's additional small-target and clipped-S leads were fixed with 44 px tool tabs/catalog selection and stretched marker rows. Proof: `fix-before/`, `fix-delivery/`, `fix-breakpoint/`, `fix-audit-followup/`, and `fix-phone/`. At 680x425 after Reveal, the S slider ends at y=223 inside the panel ending at y=227.
11. **FIXED: source links replace the instrument.** All 30 external Manual links have `target="_blank" rel="noopener"`. Proof: `fix-before-manual.json` reports 0/30; `fix-after-manual.json` reports 30/30. No instrument state is replaced by those links.

## Polish accepted

1. **FIXED: keep first-Play turn.** Autonomous turning now stops on an actual globe turn rather than any first action. `fix-after-voice-play.json` records Play still running and longitude advanced to 157.1°; `fix-after/voice-play.png` is the 1366x768 frame.
2. **FIXED: delayed shadow finding and larger cutaway.** Shadow arc, label and missing-wave text wait for their fronts. At T+0, the readout says “await rays” and no shadow arc is drawn; at T+26:00 it reports missing direct waves and draws the S shadow. The laptop cutaway canvas is 250 px high, with layer names on their layers and faders alongside. Proof: `fix-wave-timing/`, `fix-final/final-wave.png`, `fix-phone/phone-wave.png`.
3. **FIXED: Rewind transport.** Play runs toward 200 Ma and reverses, with whole-Ma steps in calm mode. The held-click probe crosses the end and records ma=120, direction=-1, running=true. Proof: `fix-after-rewind-play.json`, `fix-polish/rewind-play.png`.
4. **FIXED: station triangle chooses trace.** A native tap on B changes channel from 0 to 1 without placing a fourth station. The keyboard select remains. Proof: `fix-native-results.json`, `triangle_channel: 1`.
5. **FIXED: readable motion arrows.** There are 133 sampled sites, several near the edges of each large plate, using the corrected motion. Their canvas layer sits above the quake GPU layer. Proof: `fix-after-motion.json`, `fix-after/motion.png`, `fix-pointer/grayscale.png` at 1366x768.
6. **FIXED: calm waves keep time.** Fire starts at zero and advances by whole minutes at the same 70x model-time pace. The calm probe records 180 s with waveRunning=true, rather than jumping to the end. Proof: `fix-after-calm-wave.json`, `fix-polish/calm-wave.png`.
7. **FIXED: plain Read speech.** Read says “1970. 475 earthquakes of magnitude 5.5 or more so far.” Counts use commas and the current magnitude floor; the view count is separate. Proof: `fix-after-default-count.json`, `fix-native-results.json`. Wave Read also waits for the fronts before disclosing missing arrivals: `fix-wave-timing-0.json` and `fix-wave-timing-1560.json`.
8. **FIXED: IN VIEW count.** At the same filters, Pacific-facing count is 19,578, opposite Atlantic-facing count 6,652, total 26,230. The Manual defines this as the half facing the student. Proof: `fix-after-in-view.json`, `fix-polish/in-view.png`.
9. **FIXED: compact drum.** A 44 px drum row remains in compact desktop layouts; phone has its own 40 px row below the controls. Proof: `fix-audit-followup/`, `fix-phone/phone-stations.png`.
10. **FIXED: relief mipmaps.** The relief texture has generated mipmaps and active minification filter 9987, equal to LINEAR_MIPMAP_LINEAR. Relief remains rendered and unchanged as data. Proof: `fix-last-hardware.json`, `fix-pointer/grayscale.png` and `fix-verified/hardware-mipmap.png`.
11. **FIXED: station hardware.** The speed control is a four-detent brass dial with a contained needle; the depth handles share one track. Native detents announce 1, 3, 10 and 30 years per second. Actual independent thumb drags yield depths 220/700 and 0/480 km. Proof: `fix-native-results.json`, `fix-pointer-depth-min.json`, `fix-pointer-depth-max.json`, `fix-pointer/`.
12. **FIXED: readable control type.** Fader labels, layer names and survey labels measure 12 px at 1366x768; Read and Manual both measure 13 px. Compact captions stay at least 10 px. Proof: `fix-last-hardware.json`, `fix-verified/hardware-mipmap.png`, and audit size frames.
13. **FIXED: teacher notes.** Added one content paragraph naming the real disaster context, with no tolls or harm imagery. Three practical home ideas remain, including pinning familiar places and comparing Japan with the Atlantic tonight. Proof: `notes.md`, sections Support at home and Good to know. The paragraph distinguishes the full archive from the narrower M8+ and Strike lists.
14. **FIXED: initial year agreement.** Load and setting the dial to 1970 both give 475 events. Chose end-of-1970, as the accepted item permits. Proof: `fix-after-default-count.json`, `fix-polish/default-count.png`.
15. **FIXED: random first Strike.** Twenty-five reset-first-Strike probes produce 14 different starts; later strikes cycle the unchanged 20-event curated set. Proof: `fix-last-hardware.json`.
16. **FIXED: Rewind readouts.** QUAKES and IN VIEW read OFF; the depth legend is hidden. Proof: `fix-after-rewind-play.json`, `fix-final/final-rewind.png`, `fix-phone/phone-rewind.png`.
17. **FIXED: marker Shift jumps.** Native Shift+Right changes S from 1000 to 1010 s. Both markers share the 10 s jump handler. Proof: `fix-after-marker-shift.json`, `fix-polish/marker-shift.png`.
18. **FIXED: source-name honesty line.** The Manual explains about 500 names containing a supplied question mark. Independent count is 525; no names were repaired or guessed. Proof: `fix-independent-numbers.json`, `src.html` Manual, and unchanged material hash.
19. **FIXED: trace-axis separation.** The longer ruler shows 20 and terminal 26 min separately; 25 is an unlabelled tick. The final phone trace also keeps 20 visible. Proof: `fix-audit-followup/stations-680.png`, `fix-phone/phone-stations.png`, `fix-final-targets/final-stations-measured.png`.

## Settled calls

- **Applied: Curiosity shape.** No welcome screen, goal, score, level, quiz, finish screen or kit header was added. The short first-run hint is the only automatic narration. The engraved plate and lower-left Manual remain.
- **Applied: audit interpretation.** Full-stage canvas intersections, the dismissed hint and controls behind the open Manual are intentional. The genuine compact geometry leads were fixed and checked separately.
- **Applied: sensitivity.** No sensitivity agent was added. Disasters stay observations; the teacher-notes content paragraph is present.
- **Applied: Wave finding.** There is no question or “found it” moment. The shadow and its text appear with the travelling fronts.
- **Applied: Stations.** Status is a short instrument readout, with no FIT verdict or threshold label. Offset remains kilometres.
- **Applied: retained material.** Merdith Rewind, the M5.5 floor and explanation, original ComCat names, place-only event naming and technical honesty notes remain. Findings' instructional prose moved into how-to sections. Tag counts did not change the scope.
- **Unattended choices.** Used the successful NNR route, end-of-1970 initialization, random first Strike and stacked portrait panels. The spec's open questions were left unchanged; no age layer, continent-fitting activity, replacement motion model or stacked record section was added.

## Cheats tried

There is no score to pass. The probes target false measurements instead. In `fix-native-results.json`:

- Circles and Reveal with untouched markers: all radii null, no intersection; status asks for P and S.
- Equal P/S markers at all three distinct stations: no intersection.
- S before P: negative gaps give null radii and no intersection.
- Three coincident stations: no unique intersection.
- Clear after Reveal: selected=-1, reveal=false, station count=0, record hidden.
- Calibrated markers on three drawn arrivals: 8 km catalog offset. It is a distance, with no passing label or colour change.

## Voice walk

Held 120 ms native clicks at 2 s pacing: Play speaks “Drag to spin.” once; another Play and later layer actions do not repeat it. A separate fresh native drag speaks “Press play.” once. A fresh Slice action speaks nothing. Read speaks current measurements and stops stale speech. Audit five-click and two-quick-tap checks are clean for Play and Read. `voice/lines.json` equals `allLines()`: exactly two fixed lines, in the same order. The browser voice fallback is used; the bundler explicitly reports that recordings are absent. Proof: `fix-after-voice-*.json`, `fix-native-results.json`, `fix-audit/audit.md`, `fix-wave-timing-0.json`.

## Engine changes wanted

Deferred shared-kit request only: `kit/curio.js`, `showMotion()`, could offer plain Motion / Motion off wording without the emoji on engraved instrument panels. Logged in `handoff.md`; no kit edit was made.

## Audit

The single full audit completed within its 2400 s limit, on Chrome 9911 and host 8715. It produced 73 frames and 736 mechanical leads. All were classified in `fix-audit-triage.json`:

- 551 full-stage canvas intersections, 7 dismissed-hint rows and 35 Manual-modal rows are the settled intentional cases.
- 16 joined-depth-track hit-test rows are intentional; both actual thumbs were pointer-dragged successfully.
- 5 record/dock and 10 marker/parent rows are ancestor hit-test findings; the text is visible on the corresponding frames.
- 109 small-target rows were fixed with 44 px compact tabs and catalog selection. The 2 Close overlaps were fixed with a 48 px button and 12 px clearance. The 1 clipped-S row was fixed with stretched marker rows. After Reveal at 680x425, the S input ends 4 px inside the panel. Proof: `fix-audit-followup-*.json`, `fix-audit-followup/`, `fix-phone/`.

Motion off and resize stress checks are clean: no exceptions or controls left disabled. The native walk records zero HTTP requests and zero runtime exceptions. Every final drive batch reports zero browser errors. The local phone server occasionally logs ConnectionResetError when muted Chrome is killed during cleanup; that occurs after successful shots and is not a tool exception. The full audit was not repeated. Only the confirmed geometry leads, compact Pin readability and Wave's finding timing received scoped follow-up shots.

## The real material

The original data pack is unchanged: SHA-256 `edbf5382d7d1d8ac85da83705302c1e46cc7f3975196212196ae7384dbe54698`. The sources and licences remain in the Manual and `tool.draft.json`. Original fetch date for the bundled material is 2026-11-05; the Merdith licence was rechecked during this pass on the same date.

| Material or fact | Named source and licence | Sampling or treatment |
|---|---|---|
| Quake positions, dates, magnitude, depth and names | [USGS ComCat](https://earthquake.usgs.gov/fdsnws/event/1/), [US public domain](https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits) | Unchanged 26,230 M5.5+ events, 1970-2025; existing rounding and source-name limitations retained. |
| Sea-floor and land relief | [NOAA NCEI ETOPO 2022](https://doi.org/10.25921/fd45-gt74), [CC0 metadata](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ngdc.mgg.dem:etopo_2022/html) | Unchanged 2048x1024 relief texture and 0.5° elevation grid; only display filtering and section layout changed. |
| Coasts and city search | [Natural Earth](https://www.naturalearthdata.com/about/terms-of-use/), public domain | Unchanged thinned 50m coasts and 1,251 cities. |
| Volcano locations | [NOAA NCEI Global Volcano Locations](https://catalog.data.gov/dataset/global-volcano-locations-database), CC0 1.0 | Unchanged 1,609 locations; GPU representation changed. No direct Smithsonian download. |
| Plate geometry, motion and Rewind | [Merdith et al. 2021, v1.1b](https://doi.org/10.5281/zenodo.4485738), CC BY 4.0 | Original polygons and 5 Ma rotations retained. Surface-weighted reference-frame removal and relative edge motion are attributed derivatives. Raw licence response: `data/fix/zenodo-record.json`; reproducible calculation: `fix_nnr.js`. |
| Layered Earth, ray paths and arrival times | [Dziewonski and Anderson, PREM](https://doi.org/10.1016/0031-9201(81)90046-7), [Kennett and Engdahl, iasp91](https://doi.org/10.1111/j.1365-246X.1991.tb06724.x), numerical calculations from [TauP](https://www.seis.sc.edu/webtaup/) | Published physical numerical facts; no paper text, figures or TauP software copied. Existing bundled tables and paths retained. Table edges and reachable window independently recomputed. |
| Fossils, rock belts and retained field findings | [USGS This Dynamic Earth](https://pubs.usgs.gov/gip/dynamic/continents.html), public domain; the independent corroborating sources remain individually named in the Manual and metadata | Schematic geometry unchanged. No source prose or third-party figure copied. |
| Centimetres-per-year and fingernail comparison | [USGS motion account](https://pubs.usgs.gov/gip/dynamic/understanding.html), public-domain factual account; independent [NOAA account](https://repository.library.noaa.gov/view/noaa/42205/noaa_42205_DS1.pdf), physical facts only | Rechecked as a rough scale comparison, with no fixed rate claimed everywhere. The displayed equatorial Atlantic model opening is 3.3 cm/yr. No prose or media copied. |

Independent Python checks are in `fix_numbers.py` and `fix-independent-numbers.json`. The supplied ITRF2014 city numbers are validation comparisons, not a new bundled dataset. No new scientific dataset was downloaded. The existing raw pack provenance is under `data/build2/`; only the fresh Zenodo licence metadata was saved under `data/fix/`.

## Frames looked at

Before frames: all 17 in `fix-before/`, plus the paired before performance frame. After and regression frames: `fix-after/`, `fix-final/`, `fix-final-targets/`, `fix-verified/`, `fix-breakpoint/`, `fix-audit-followup/`, `fix-delivery/`, `fix-pointer/`, `fix-wave-timing/`, and the 375x812 iframe frames in `fix-phone/`. All 73 audit frames were examined through labelled contact pages `fix-contacts/audit-01.png` to `audit-10.png`, with confirmed leads also opened at full size. Remaining iteration frames were examined in `fix-contacts/checks-01.png` to `checks-04.png`. The four permitted model tools were opened and compared in `fix-models/`; the globe, actual data and scientific controls remain central.

## Left open

- A physical school Chromebook and physical touch hardware were unavailable. The muted Chrome, native pointer/keyboard, 4x CPU and phone-iframe evidence is stated above. The all-layer benchmark has a 16.7 ms median and 20.2 ms mean, so sustained 60 fps across hardware remains unverified.
- Fixed narration recordings are still absent; the two correct hint halves use the existing browser-voice fallback.
- The deferred shared-kit wording and the spec's open questions remain with the owner. No blocker or should-fix item from this list remains open in the tested states.

Final byte counts, protected hashes, contrast ratios and closed test ports are recorded in `fix-final-manifest.json`. The source lesson-creep scan contains only scientific “sea level” and geometric point variables/GL.POINTS; no lesson outcome or reward UI was introduced.

# Codex report: living-earth (Curiosity No. 04)

## Built

Built an explicitly limited archival edition, not the full instrument required by the spec.
The offline file is [living-earth.html](living-earth.html), 154,660 bytes, about 151 KiB.
It contains a code-drawn coordinate globe, time transport, magnitude and depth filters, event inspection,
great-circle sections, synthetic station records, spherical distance circles, radial seismic rays and survey pins.
The maker's plate, lower-left Manual and separate Motion, Sound and Read power panel are present.
There is no lesson frame, score, progression or finish screen.

Bulk source retrieval was blocked by the environment. The build preserves 11 verified historical earthquakes,
clearly identified on the instrument and in its Manual. This is a data-dependent scope deviation, not the spec's
M5.5 size fallback. The requested worldwide catalog and geographic layers must be restored before release.
No commits, deployment or polish round were made. Explicit writes stayed in the two authorized folders.

## The real material

Source checks and transcriptions: 2026-11-05. Detailed event-by-event corroboration and origin discrepancies are in
[_scratch/living-earth/source-review.md](../../_scratch/living-earth/source-review.md).

| Material | Source and permission | What is actually bundled |
| --- | --- | --- |
| Earthquakes | [USGS ComCat](https://earthquake.usgs.gov/data/comcat/), event pages and [OFR 2016-1192](https://pubs.usgs.gov/of/2016/1192/ofr20161192.pdf); US public domain under the [USGS policy](https://www.usgs.gov/faqs/are-usgs-reportspublications-copyrighted) | 11 selected events, 1994-2018, M8.2-9.1. Dates, coordinates, depth, magnitude, place and source ID. Not a representative sample. |
| Radial Earth parameters | Kennett and Engdahl (1991), [iasp91](https://doi.org/10.1111/j.1365-246X.1991.tb06724.x), transcribed from its [published parameter listing](https://github.com/obspy/obspy/blob/master/obspy/taup/data/iasp91.tvel) | 138 radial parameter rows. Published scientific numerical facts under the spec's Earth-model allowance; no ObsPy software or figures are bundled. |
| Wave shadows | [USGS Shadow Zone](https://www.usgs.gov/media/images/shadowzonegif), public domain; corroborated with [IRIS](https://www.iris.edu/hq/inclass/software-web-app/seismic_waves_viewer) | Direct S shadow beyond about 104 degrees; direct P shadow about 104-140 degrees. Facts only, no copied media. |
| Geometry | Great-circle geometry and spherical Snell's law; original implementation | Radius 6,371 km from the Earth model, shortest surface distances, cross-track sections and analytic constant-velocity shell integrals. |

The archive includes Bolivia, Peru, Sumatra-Andaman, Nias, Bengkulu, Maule, Tohoku, Wharton Basin,
Okhotsk, Illapel and Fiji. Coordinates are packed at 0.01 degree, depths at 0.1 km, dates at UTC days.
Historical origins differ from later solutions. In particular, the archive preserves Okhotsk at 608.9 km;
a later USGS publication gives 598.1 km. The Manual identifies this edition as historical throughout.

The direct acquisition batch used 45 second request limits. Every attempted bulk URL and socket denial is in
`_scratch/living-earth/data/fetch-log.json`. Gathering remained within the 45 minute allowance.
The raw numerical listing, verified-event transcription, acquisition script, packing script and manifest are preserved.

| Material not bundled | Source permission checked | Reason |
| --- | --- | --- |
| ETOPO 2022 | [NOAA metadata](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ngdc.mgg.dem:etopo_2022/html), CC0-1.0, DOI 10.25921/fd45-gt74 | Data download unavailable. No fabricated relief. |
| Coastlines and cities | [Natural Earth terms](https://www.naturalearthdata.com/about/terms-of-use/), public domain | Download unavailable. No guessed coastline or city list. |
| Volcanoes | [NOAA Global Volcano Locations](https://catalog.data.gov/dataset/global-volcano-locations-database), CC0 | Download unavailable. Smithsonian data were not substituted. |
| Plate polygons, velocities and Rewind | [Merdith model record](https://zenodo.org/records/4485738) | Archive unavailable; the license badge was not exposed by text extraction, and pygplates was absent. No reconstruction or license claim is bundled. |

The 2 MB budget cannot be considered validated for the full instrument: the missing material accounts for much of its planned size.

## Break the instrument

- 32 of 32 calculation checks passed in `_scratch/living-earth/calculations.json`.
- Checked dateline distances, antipodal interpolation, zero-length sections, empty filters, deep-only and M9 filters.
- Checked zero-time arrivals, negative S-P gaps, P preceding S, shadow boundaries and receiver/time extremes.
- Three well-spaced stations with model arrival markers intersected at 0 km offset from the bundled epicentre.
  Coincident stations returned an ambiguous intersection instead of a spurious position.
- A real jittered pointer drag made a 2,541 km section containing one event. The section remained below its 3,000 km cap.
- Playback reached 2025 with all 11 events and stopped quietly. At default speed the 56-year interval takes about 18.7 seconds.
- The measured unthrottled browser mean was 16.67 ms per frame. This is not a Chromebook or full-catalog performance result.
- The audit's resize stress checks found no exceptions or controls left disabled. Motion off had no continuing visual animation.
- Pinch input is implemented but was not verified with a physical touch device.

The model is a 2 km shell integration of iasp91, not a reference TauP implementation. Reflected, converted,
diffracted and head-wave branches are omitted. Missing branches display NO BRANCH. Reference calibration remains open.
Stations deliberately uses a surface focus even when its catalog event is deep. Its traces are not recorded seismograms.

## Voice walk

`gravel-ranger` and the requested style are declared in `voice/lines.json`. No audio was recorded.
The kit supplies browser speech until bank recordings exist; gravelly voice quality is therefore unverified.
Held clicks at a two-second pace exercised Pin, Read, Stations, Strike and Read again.
The log contains one first hint and current-state Read entries. Read's interruption of the first hint is intentional.
There is no automatic narration after that hint. The audit's five-click and rapid-tap voice checks were clean.
Evidence: `_scratch/living-earth/voice-walk.json` and the audit report.

## Short test

Overall: FAIL for the requested finished Curiosity.

- Would a kid open it unassigned? Not convincingly yet. A coordinate sphere with 11 events lacks the geographic discovery the brief promises.
- Would an adult play for fun? The station and wave engines offer something real to inspect, but the requested month of breadth is unproven.
- Is the real material the interface? Yes for the bundled earthquake parameters, sections and numerical wave model.
- Does it work without a score or finish? Yes.

The build was exercised through automated and direct inspection paths. Two separate ten-minute open-ended
student and adult play sessions were not completed, so no claim is made that this acceptance condition passed.

![Living Earth beside Elements Inspector](../../_scratch/living-earth/final-frames/family-comparison.png)

The comparison also makes the missing material obvious: Elements Inspector has much greater authentic data density.

## Lesson creep check

The requested search found 14 occurrences of `points`: one refers to geographic endpoints in the Manual,
and the remainder are geometric plotting arrays. All other searched lesson terms are absent from `src.html`.
Voice has only the first hint. No em dash occurs in the source. The artifact has no mode pills or kit header.

## Done when

| Spec item | Result | Evidence or limit |
| --- | --- | --- |
| 1. Opens on globe; 1970-2025 playback | FAIL | Direct opening and transport work, but 11 events cannot draw the worldwide plate margins. |
| 2. All five instruments | FAIL | Four partial instruments exist. Ideal station intersection and S shadow work. Japan's dipping zone cannot be established from this archive; Rewind, plate speed and nearest volcano are absent. |
| 3. Numbers trace to sources; ten live ComCat checks | FAIL | Archival parameter corroboration and numerical checks are preserved. Ten current API spot checks and reference travel-time calibration were not completed. |
| 4. Attribution, permissions and offline file | PASS for bundled material | Manual and draft metadata name the used material. No external automatic resource elements; browser resource list was empty for the offline file. Unretrieved layers are omitted. |
| 5. Keyboard controls and value announcements | PASS for implemented controls | Native labelled ranges/buttons, globe arrows, Shift increments, zoom keys, centre-placement buttons and dynamic Read were exercised. Missing spec controls remain covered by item 2. |
| 6. Full-catalog 60 fps Chromebook profile | FAIL | Only an unthrottled 11-event desktop run was measured. |
| 7. Required layouts and family marks | FAIL against complete visibility rule | All required sizes were inspected and the plate/Manual remain lower-left. Compact instrument panels still need internal scrolling. Phone transport obstruction was fixed. |
| 8. Motion off and AA text contrast | PASS for checked states | Globe stops automatic turning, archive advances in year steps; measured text ratios 5.50:1 to 12.72:1. |
| 9. Short test and reference comparison | FAIL | Comparison exists; discovery depth and the required extended play test do not pass. |
| 10. No game structure or finish | PASS | Counts and station offset are measurements only. Playback has no finish screen. |

## Audit leads

The single full audit completed with 367 grouped leads; its original result is preserved, not presented as clean.
It comprises 32 target-size, 264 overlap, 50 hidden-text, five disappearing-hint, eight keep-region and eight scroll-panel leads.

- Most overlap leads are the intentional full-viewport canvas behind its labels and controls. The Manual intentionally covers and makes the instrument inert.
- The hint disappears after first action as explicitly allowed. Its resulting out-of-view leads are intentional.
- Narrow zoom targets and small Manual source links were enlarged. A targeted browser check measured all 21 source links at least 44 by 44 px.
- The old phone sheet covered transport, tool tabs and coordinate labels. It was repositioned inside the globe region; the targeted 375 px check confirmed Play exposed and no horizontal overflow.
- Station marker-row overflow and coincident catalog/intersection labels were fixed and rechecked.
- The year range's generous hit area crosses the readonly archive caption by four pixels in two compact sizes; the visible track, caption and selector remain distinct.
- The eight scroll-panel leads are retained limitations. Wave controls and multiple station traces cannot all be seen at once in compact panels.

No audit console exceptions, resize failures or stuck controls were reported. Final targeted shots had zero console errors.
An earlier phone test fixture requested a missing favicon; the local fixture was corrected and its follow-up was clean.
The full audit was not repeated after these build fixes. Evidence is in `audit/`, `audit-triage.json`, `final-frames/` and `post-frames/` under Scratch.

## Frames looked at

Inspected the four named reference instruments, three early frames, all 12 size/calculation frames, nine targeted
final frames and three final correction frames. Triaged all 57 audit PNGs through six contact sheets, with selected
phone and instrument frames also inspected individually. Contact sheets do not establish a full text-by-text review.
The size sweep included 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and a real 375x812 iframe.
Motion off, grayscale, keyboard input, jittered dragging, the Manual, wave rays and station records were inspected.
All evidence and the final SHA-256 manifest are in `_scratch/living-earth/`.

## Art made

None. `art/prompts.json` intentionally has no assets. The scientific surfaces are canvas drawings driven by data
and geometry. There are no painted data, placeholder coastlines or invented relief textures.

## Engine changes wanted

None. Shared kit, scripts, docs and other tools were not edited.

## Left open

- Restore the actual M5.0 catalog, or the stated M5.5 size fallback, plus ETOPO, Natural Earth, NOAA volcanoes and licensed plate material.
- Implement the omitted geographic layers, city search, plate identity/velocity, volcano readouts and licensed Rewind/fossil material.
- Calibrate travel times and surface-focus limitations against a reference implementation; add PREM if retaining that spec claim.
- Resolve compact instrument-panel scrolling before claiming full layout acceptance.
- Run the full-catalog Chromebook profile, physical touch checks and extended short test.
- Do not replace the anchor module's lesson card: this build does not cover MS-ESS2-3 in full.
- All successful driver helpers executed their Chrome cleanup and server shutdown paths. Independent process/listener inventory was denied by Windows CIM permissions; socket probes were inconclusive. No test process was deliberately left running.
- The first two immediate readonly inspection commands lacked explicit hard timeouts. Subsequent commands had hard bounds. No permission or security setting was changed.

Unattended decisions: omit unavailable layers, preserve real archival data with explicit limitations, use browser
speech without recordings, keep compact panels scrollable, and leave the result as a blocked draft rather than claim spec completion.

# living-earth: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: living-earth (Curiosity No. 04)

#### Built

Second build, Cory's 2026-11-05 decision. The instrument opens directly on its globe and runs entirely from `living-earth.html`.
Changed from the first build: replaced the eleven-event demonstration with 26,230 real M5.5+ ComCat earthquakes; added ETOPO relief and section heights, Natural Earth coasts and cities, NOAA volcanoes, licensed plate geometry and finite rotations, every geographic layer, city search, plate/volcano measurements and Rewind to 200 Ma.
Also replaced the uncalibrated arrival table with TauP-calculated iasp91 values and the cutaway paths with PREM numerical paths. Fixed compact panels, end-of-playback counts, inconsistent station-circle fits, readable Pin narration and keyboard inspection of ordinary earthquake dots.
Kept the first build's spherical geometry, great-circle sections, synthetic station traces, station intersection, drum, brass controls and family marks. Maker's plate and Manual remain lower-left; Motion, Sound and Read have their own power panel.
No welcome, lesson route, mode pills, game structure or finish screen. Five brass tabs select physical instruments. No painted scientific material.
Final file: **1,951,146 bytes**, 48,854 bytes below the decimal 2 MB goal. All data is embedded. `src.html` and `material.json` remain editable; `handoff.md` maps the preparation and evidence.
`codex-report-1.md` is unchanged, SHA-256 `06c24a9e44103ead51dde356980dde15b19f845ec9da5bce4655012ebccb1893`.
Build only: no commits, deployment or polish round. Writes were confined to `tools/living-earth/` and `_scratch/living-earth/`.

#### The real material

All sources below were retrieved **2026-11-05**. Raw responses, licence records and URL/date/SHA-256/duration receipts are in `_scratch/living-earth/data/build2/`. The receipt window is 22:37:14 to 23:18:38 UTC, about 42 minutes, within the owner's 75-minute gathering cap. Downloads had 60-second limits. No software was installed and no downloaded executable was run.

| Material | Source and permission | What ships |
| --- | --- | --- |
| Earthquakes | [USGS ComCat](https://earthquake.usgs.gov/fdsnws/event/1/), US public domain under [USGS policy](https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits) | Every returned M5.5+ event in 1970-2025, 26,230 events. UTC days, 0.01-degree coordinates, 0.1-km depths, 0.1 magnitude; negative source depths clamped to zero. Names and IDs retained. |
| Relief | [NOAA ETOPO 2022, DOI 10.25921/fd45-gt74](https://doi.org/10.25921/fd45-gt74), CC0 1.0 in [NOAA metadata](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ngdc.mgg.dem:etopo_2022/html) | 60-arc-second ice-surface product sampled every 10 arc minutes for code shading; 2048x1024 WebP, 164,330 bytes. Separate 720x360 half-degree int16 metre grid for sections. |
| Coasts and cities | [Natural Earth](https://www.naturalearthdata.com/), [public domain](https://www.naturalearthdata.com/about/terms-of-use/) | 50m coastlines thinned near 0.1 degree, 1,429 segments; all 1,251 populated places from that product. Coast coordinates 0.01 degree, cities 0.001 degree. |
| Volcanoes | [NOAA NCEI Global Volcano Locations Database](https://catalog.data.gov/dataset/global-volcano-locations-database), CC0 1.0; [NOAA HazEL API](https://www.ngdc.noaa.gov/hazel/hazard-service/api/v1/volcanolocs) | All 1,609 returned locations, elevations and types. NOAA's compilation is used; no direct Smithsonian GVP material is downloaded. A triangle does not mean currently erupting. |
| Plates and Rewind | [Andrew Merdith et al. 2021, model v1.1b](https://doi.org/10.5281/zenodo.4485738), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), verified in Zenodo metadata | Original GPML and finite-rotation circuits resolved with standard-library preparation code. 44 of 51 present topologies resolved; 886 continental fragments stored; 280 usable rotation IDs sampled every 5 Ma to 200 Ma and interpolated by quaternion slerp. Modifications and omissions are credited in the Manual. |
| Earth interior | [Dziewonski and Anderson 1981, PREM](https://doi.org/10.1016/0031-9201(81)90046-7); [Kennett and Engdahl 1991, iasp91](https://doi.org/10.1111/j.1365-246X.1991.tb06724.x); [TauP service](https://www.seis.sc.edu/webtaup/) | Published physical numerical facts and calculated outputs: 54 PREM ray paths, iasp91 times sampled every degree. Paths rounded to 0.01 degree, 0.1 km and 0.1 s. No TauP or ObsPy software is bundled. |
| Fossils and mountains | [Kious and Tilling 1996, USGS This Dynamic Earth](https://pubs.usgs.gov/gip/dynamic/continents.html), public domain; [historical figure](https://pubs.usgs.gov/gip/dynamic/historical.html) | Original code outlines of broad Mesosaurus/Glossopteris regions and Appalachian/Scotland/Scandinavia mountain traces. Schematic regions, not specimen coordinates or ancient shores. |

The complete M5.0 query returned **90,290 events**. Its numeric gzip/base64 pack alone was **899,688 bytes**, exceeding the spec's 700 KB threshold. The stated M5.5 fallback is therefore used, openly in the face, Manual and metadata. Millions of smaller quakes are absent. Older magnitude scales and revised event origins are explained.
The Merdith model is in its palaeomagnetic frame. Pin speed and arrows report its **0-5 Ma average**, not a present GPS velocity. The original README excludes Pacific hotspot-track analysis, so the Manual explicitly bars using these arrows to explain the Hawaiian-Emperor bend. Unresolved polygons and unavailable rotations stay unknown. Rewind transports crustal outlines; it does not recover ancient shorelines or ocean floor.
Sections use a 300-km swath and equal horizontal/vertical kilometres for quakes. Only the ETOPO surface profile is exaggerated x20. Stations uses 20 shallow catalogue epicentres with idealized surface-focus, synthetic iasp91 traces. The Wave cutaway interpolates precomputed PREM paths; weak/converted phases are omitted, rather than inventing arrivals in the direct-wave shadows.

Manual field notes are original paraphrases of facts, with no copied third-party prose or media. Their corroboration and permissions:

- Tonga/Fiji depths approaching 700 km: [USGS depth notes](https://www.usgs.gov/faqs/what-depth-do-earthquakes-occur-what-significance-depth), public-domain government facts, and [IRIS source-studies report](https://dev.iris.edu/hq/files/publications/iris_proposals/doc/IRIS_Core_Proposal_2010_Vol_II_Accomplishments_lorez.pdf), facts only.
- Pacific rim's historical 81-percent estimate for the largest earthquakes: [USGS belts](https://www.usgs.gov/faqs/where-do-earthquakes-occur) and [FEMA CERT Hazard Annexes](https://www.ready.gov/sites/default/files/2019.CERT_.HazardAnnexes.PM_.FINAL_.508c.pdf), public-domain government facts. It is not a percentage computed from these filters.
- M9.5 Chile, 22 May 1960, largest instrumentally recorded quake, before this archive: [USGS record](https://pubs.usgs.gov/of/2010/1152/of2010-1152.pdf) and [NOAA account](https://www.ncei.noaa.gov/news/day-1960-chilean-earthquake-and-tsunami), public-domain government facts.
- Liquid outer core and approximately 104-degree direct S shadow, with approximately 104-140-degree direct P shadow: [USGS Shadow Zone](https://www.usgs.gov/media/images/shadowzonegif), public domain, and [IRIS Seismic Waves Viewer](https://www.iris.edu/hq/inclass/software-web-app/seismic_waves_viewer), facts only.
- Lehmann's 1936 inner-core inference: [University of Copenhagen](https://nbi.ku.dk/english/www/inge/lehmann/) and [American Physical Society](https://www.aps.org/apsnews/2023/08/seismologist-lehmann-earth-inner-core), historical facts only; no text or figures copied.
- Mid-Atlantic spreading about 2.5 cm/year on average, varying along the ridge: [USGS](https://pubs.usgs.gov/gip/dynamic/understanding.html), public domain, and [University of Malta research account](https://www.um.edu.mt/library/oar/bitstream/123456789/123491/1/THINK36-Mantle.pdf), numerical fact only.
- Hawaii inside the Pacific plate and its chain older toward the northwest: [USGS HVO](https://www.usgs.gov/observatories/hvo/evolution-hawaiian-volcanoes) and [NOAA](https://oceanservice.noaa.gov/facts/hawaii.html), public-domain government facts.
- Fossils connecting separated continents: USGS figure above plus [Freie Universitat Berlin](https://www.geo.fu-berlin.de/en/v/geolearning/gondwana/evidences/flora_and_fauna/index.html), factual corroboration only. Mountain connections also checked with [National Park Service](https://www.nps.gov/subjects/fossils/supercontinent-pangea.htm), public-domain government facts.

The Manual and the 13 `tool.draft.json` source entries preserve this attribution. Data packing is reproducible with `build2_fetch.py`, `build2_sources.py`, `build2_more.py`, `build2_taup.py`, `build2_plates.py` and `build2_pack.py` in Scratch. Browser texture conversion and source assembly inputs are preserved there too.

#### Break the instrument

- **38/38 numerical probes passed**, preserved in `build2-numbers-final.json`: full/empty filters, depth/magnitude extremes, antimeridian distance, seven major-plate city checks, relief signs, reference arrivals, shadows, inverse S-P distances, sections, dataset counts and offline resource checks.
- **10/10 independent event-detail queries** agree with the packed catalogue within its stated rounding. Events span 1970-01-01 to 2025-12-31. Fresh source receipts and `data/build2/spot-checks.json` retain each comparison.
- Japan reference section: **377 events, deepest 560 km**. Mid-Atlantic reference section: **157 events, deepest 33 km**. A native jittered pointer section reached **3,000 km, 388 events, deepest 448.3 km**. Zero-length sections remain finite and empty filters stay usable.
- Three ideal station circles meet the selected epicentre with approximately **0 km** numerical offset. Coincident stations and a set of circles deliberately made inconsistent by 500 km return ambiguous. A 200-km residual gate prevents normalization from pretending inconsistent circles fit. Physical traces remain synthetic, not observed records.
- Surface S paths stop above the liquid core: minimum S-path radius **3545.7 km**, versus outer-core radius 3480 km. Far-side P paths cross the core. Reference iasp91 arrivals at 30 degrees are **P 370.264 s, S 670.266 s**.
- Default playback reaches 2025.999 and all **26,230 events in 18.681 s**. The opening count is zero. An earlier stale final count was fixed and this measurement repeated.
- The Chrome 4x CPU-throttle profile, 1366x768, all dots loaded, pointer-move rendering path: **330 frames, mean 16.666 ms, p95 16.8 ms, 60.003 fps**. Deliberately refiltering/rebuilding readouts every animation frame gave **58.24 fps**. Both are retained in `build2-performance-final/`; this is an emulated profile, not physical Chromebook certification.
- The one full audit completed: no console exceptions, no resize exceptions/stuck controls, and Motion off clean. All successful final product shots have zero console errors and zero horizontal overflow. Final positive and empty keyboard inspection paths announce the event or empty result.
- Bounded browser-fixture failures are retained separately: new-profile Chrome/contact-sheet runs timed out or disconnected. A known working 9992 profile completed the targeted product checks. Contact sheets were generated with Windows GDI+. No product pass is inferred from a failed driver run.

#### Voice walk

The declared bank is `gravel-ranger`, with the field-seismologist direction retained. No recordings were generated; speech uses the kit's browser fallback. Voice timbre and physical speakers were not verified.
The first hint, "Drag to spin. Press play.", is issued once after first interaction, then voice speaks only when Read is pressed. State changes update the screen-reader status without unsolicited spoken commentary.
Held input, five taps two seconds apart, quick taps, settled focus and Enter paths were exercised by the audit. No welcome replay or narration pile-up was reported. Pin's former run-together text was replaced and rechecked as sentences with kilometres, cm/year averaging interval and heading units.
Read reports year and filtered count, selected quake or volcano, then the active instrument's measurement. It reports Ma in Rewind. Evidence: `build2-voice-walk.json`, `build2-post-pin.json`, audit voice walk and keyboard result files.

#### Short test

Completed two **600-second builder explorations**, one through the grade-6 student's lens and one as an adult. These are recorded builder judgments with real browser input, **not a child user study**. Neither opened the Manual in its first two minutes. `build2-explore/walk.json`, twelve frames and two empty error logs preserve them.
The student walk started with Play, rotation and depth/magnitude changes, then explored layers, Japan's section, station records, rays, city search and 200 Ma. The adult walk compared regions, used a dateline section and extreme filters, inspected Hawaii, changed station geometry and deep-time evidence. Poor station geometry honestly returned ambiguous.

1. **Would a kid open it unassigned? Yes, provisionally.** Play produces worldwide plate-margin patterns in about nineteen seconds; spinning and filtering immediately change the material without reading.
2. **Would an adult play for fun? Yes.** Real places, detailed ocean relief, contrasting sections and the reconstruction sustained the adult walk. No compulsory sequence interrupts it.
3. **Is the real thing the interface? Yes.** Quakes, relief, plate geography, measurable synthetic traces and model rays form the working surface. Readouts carry units and provenance is available in the Manual.
4. **Does it work without a score or finish? Yes.** The archive and five instruments can be revisited indefinitely. A month can still find new regional depth patterns, station geometries and model comparisons among 26,230 observations; playback stopping creates no completion screen.

![Living Earth beside Elements Inspector](../../_scratch/living-earth/build2-final/family-comparison.png)

The comparison was inspected beside the actual Elements Inspector instrument. Living Earth's data density now supports the same immediate confidence; the instruments retain their own visual grammar. The comparison frame predates the final small layout and attribution fixes.

#### Lesson creep check

Search terms: score, points, level, goal, sticker, badge, correct, wrong, try again, complete and well done.
Only **14 source-line hits for `points`** remain: geographic arrays, section-data properties, a rendering comment and WebGL `POINTS`. None is a reward. Every other term is absent from the source and all terms are absent from voice lines. Source contains zero em dashes. No kit header, mode pills or lesson progression appears.

#### Done when

| Spec item | Result | Evidence or limit |
| --- | --- | --- |
| 1. Direct globe; approximately 20-second archive | PASS | No welcome; zero initial dots; full run 18.681 s. |
| 2. Five working instruments | PASS with stated model limits | Japan's dipping depths; ideal station fit within 200 km; S shadow; Rewind to 200 Ma; plate, model speed and nearest volcano. Small unresolved plate areas remain unknown. |
| 3. Traceable numbers; ten ComCat checks | PASS | Packed data/model provenance, 38 numerical probes and ten fresh event-detail comparisons. |
| 4. Sources, permissions, offline file | PASS | Manual plus 13 metadata entries, licence receipts and no automatic external resources in the browser check. |
| 5. Keyboard and value announcements | PASS | Native labelled controls, arrows/Shift, zoom, centre placement, marker nudges and positive/empty Enter inspection. Read and screen-reader status expose results. |
| 6. Full-catalogue 60 fps Chromebook profile | PASS in emulated profile | Chrome 4x CPU: 60.003 fps in the pointer rendering probe. Physical school hardware remains unverified; heavier synthetic readout stress was 58.24 fps. |
| 7. Layout and family marks | PASS for checked sizes | All eight required sizes, real 375x812 iframe, compact instrument states and targeted audit fixes. Manual intentionally scrolls; main instrument controls fit. |
| 8. Motion off and AA | PASS | Audit says nothing runs forever; year-step playback. Checked text contrast minimum 5.24:1, grayscale frame inspected. |
| 9. Short test and Elements comparison | PASS as builder assessment | Two ten-minute walks, four answers and inspected comparison above; no user-study claim. |
| 10. No game structure or finish | PASS | Term scan and interaction walks; station offset remains a distance. |

#### Audit leads

The single full audit is preserved in `build2-audit/audit.md`, **499 grouped leads**: 425 overlap, 59 hidden-text/scroll-edge, eight keep-region, six disappearing-hint and one choices-cut-by-scroll-panel lead. It was not rerun after the targeted fixes.

- Intentional: the viewport canvas lies behind its labels and controls; its rectangular hit region is larger than the visible globe. The modal Manual covers and makes the instrument inert, accounting for its keep-region and hidden-under-modal leads. The hint is supposed to disappear after first action.
- Fixed: the archive selector covered the coordinate caption at middle widths. The caption now sits beside it; at short sizes the selector moves to the empty right side until a tool opens.
- Fixed: the short selected-quake card collided with the archive selector. The record was reflowed and the selector moved; record details are withheld while a short-screen instrument is open, with selected-event Read still available.
- Fixed: at 1000x625 the Wave faders, station readout and Pin-centre button were cut by the panel. Targeted measurements now show Wave **315/315**, Stations **323/323**, Pin **318/318** client/scroll height, with those controls exposed. Compact Wave is **180/180** and the three-station compact check **187/187**.
- Additional functional corrections: short cutaway labels no longer collide; map annotations use magnitude with the full event in its record; Enter inspection retains the complete status announcement. Selecting a smaller dot leaves the M8+ archive menu's prompt intact instead of blank.
- Read-only coordinate captions use `pointer-events:none`; an `elementFromPoint` result naming the canvas there is intentional, not evidence of occlusion. Their corrected text was inspected on frames.

No outstanding product obstruction was seen in the targeted follow-ups. Native long dropdown option text may truncate until opened; the selected event's full name is in its record and Read. Detailed triage is preserved in `build2-audit-triage.json`.

#### Frames looked at

Opened and used all four required reference instruments before design. Inspected all twelve late size/calculation/Motion/grayscale/Manual/comparison frames, twelve exploration frames, early instrument checks, compact and phone follow-ups, relief conversion frames and the final targeted fixes.
Required size sweep: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and a real 375x812 iframe. Every size reported no horizontal overflow. The source/data renderer was ready in every successful final size shot.
All 65 audit PNGs and twelve other pending frames were reviewed through ten labelled contact sheets; selected affected audit frames and all subsequent product corrections were also viewed individually. Contact review does not establish a full text-by-text inspection at every size.
Evidence folders are prefixed `build2` in Scratch. Earlier failed or superseded fixtures are retained and distinguished from the final measurements. Final checks and file hashes are recorded in `build2-final-manifest.json`.

#### Art made

No painted assets. `art/prompts.json` has no assets. The only raster scientific surface is the code-shaded ETOPO WebP, generated from actual elevations, with quality 0.72 after visual comparison. Coastlines, event dots, volcano triangles, plate geometry, fossils, traces, sections and rays are drawn in code.

#### Engine changes wanted

None. No shared engine, kit, script, documentation or other tool was intentionally edited. No package or system software was installed.

#### Left open

- Seven small present topology regions reference absent features; simplified joins include two gaps of about 0.93 degree, roughly 100 km. Full GPlates topology parity is not claimed. These limits and unknown-area behavior are visible in the Manual.
- Some continental fragment IDs lack a continuous rotation circuit over 0-200 Ma and are omitted from Rewind. Model sampling is 5 Ma; older fossil regions are schematic evidence carried on crust, not claims of occurrence at each dial date. Plate motion is not GPS or a Hawaiian hotspot reconstruction.
- Physical touch devices, a real school Chromebook and the exact browser-voice timbre still need hardware verification. Emulated performance and browser input tests are reported separately.
- Driver cleanup and host shutdown paths completed. Final socket probes returned Windows 10035 timeouts, so they do not independently establish that every test listener exited. No test process was deliberately left running.
- The existing anchor lesson card and module teacher plan were not replaced. This build does not authorize that curriculum decision.
- Process deviations: the first two immediate read-only inspection commands lacked explicit hard timeouts. A combined prerequisite read printed broader regular-build text than the Curiosity brief permits. Later commands were bounded; implementation followed the Curiosity brief. No permission or security setting was changed.

Unattended decisions: use the specified M5.5 fallback; resolve the published finite rotations in standard-library code rather than install pygplates; use a five-million-year motion average consistent with the model's warning; retain explicit unknown geometry; multiplex station channels so the controls fit; use browser speech without recordings. The first build's missing data-dependent instruments are now present.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: living-earth

#### Played
Cold play preceded reading the builder report, handoff, notes and source. Used grade-6 and adult lenses: Play through the archive, jittered globe drags, all five instruments, Manual, layers, filters and real keyboard input. The quake arcs and detailed relief are worth exploring without an assignment; this is an instrument, not a lesson route. This is reviewer judgment, not a participant study.

#### Findings fixed
- **Blocker, general, phone instruments:** the panel obscured most of an already tiny globe. Compact panels now leave the entire visible globe above them; Slice and Wave retain readable plots. Verified every phone instrument and reachable Close controls at 375x812.
- **Should fix, general, Stations:** Clear left old P/S labels beside zero-valued controls; editing a marker or replacing stations retained the revealed catalog record. Reset labels and invalidate the old reveal together. Guarded clearing during a captured pointer drag.
- **Should fix, general, Read and keyboard placement:** raw S-P, T+, timestamps and km abbreviations made poor speech; centre placement replaced its result announcement with coordinates. Read now uses sentences and units, keeps the measurement announcement, identifies out-of-filter selections and stops old speech on an instrument switch.
- **Should fix, general, Wave:** changing the source during a running firing continued automatically. A new source now resets elapsed time and waits for Fire.
- **Should fix, general, canvas fallback:** Relief off redrew the same relief. It now shows the flat land/ocean surface; pixel signatures differ and the fallback frame was inspected.
- **Should fix, general, Pin:** entering Lima selected the earlier substring Quelimane. Exact city names now rank before partial matches; Lima, Peru was independently driven and inspected.
- **Should fix, general, Rewind:** the two fossil-region keys depended on colour. Glossopteris now has a solid outline and Mesosaurus a dashed outline, with the small Mesosaurus regions drawn above the broader regions. The same distinction is in the Manual and legend; the grayscale evidence was rechecked.
- **Polish, general, Stations:** the flattest moment was aligning six markers on unlabelled, 18-pixel compact traces. Added a five-minute ruler and a 66-pixel trace beside its markers; kept synthetic arrivals and measuring under the student's control.
- Preserved the real-data pack, rich ETOPO globe, physical controls, family plate, lower-left Manual and free exploration. Added no topic, goal, rating, quiz, kit header or endpoint.

#### Findings left
No known blocker or should-fix remains. Small model gaps and emulated hardware checks are limitations, listed below. Recorded voice timbre remains a polish/release follow-up.

#### Break it
- No score, check, quiz or success gate exists to cheat. Station OFFSET is a physical separation; zero/inverted/unusable gaps and coincident stations return no circle or an ambiguous fit.
- Native Home/End reached both limits of all ten ranges. Depth handles crossing remain ordered; zero-length and dateline sections stay finite. Every layer and P/S switch was rapidly toggled twenty times.
- Independently decoded eight filter cases match the interface: 475 in 1970; 26,230 total; M9+ 2; M8+ 44; depth 300-700 km 1,548; zero-depth 13; exactly 700 km 1; M9+ at 700 km 0.
- Japan section [35,144] to [40,130]: 1,352 km, 329 events, deepest 560 km. Atlantic [0,-32] to [0,-12]: 2,224 km, 178 events, deepest 35 km. Depth axes remain true; only relief is x20.
- Rounded half-second picks on three synthetic traces put the intersection 3.36 km from the 2004 Sumatra catalog epicentre. Deliberately invalid gaps do not produce a persuasive fit. Clear during a real captured drag produced no exception.
- Empty, whitespace, long Unicode and accented city input stay usable. Exact Lima now chooses Peru. A fourth station restarts the station set without losing access to a channel.
- Archive and Wave survive real viewport flips while running. A new source stops the previous firing. Motion off fixes longitude and the drum. Zoom/polar endpoint evidence is in review-final-targets.
- Four-times CPU throttling, 1366x768, every quake loaded and the globe drawing: 179 frames, mean 16.666 ms, p95 16.7 ms, about 60 fps. This is an emulation, not a physical Chromebook certification.

#### Voice walk
Held presses at a two-second pace: Play, Read; Slice and centre placement, Read; Stations and Place, Read; Wave and Fire, Read; Rewind and Fossils, Read; Pin and centre placement, Read; Sound off, Read.

| Kind | Expected | Observed |
| --- | --- | --- |
| Opening hint | once | 1 spoken |
| Read current instrument | each press | 7 reads, including Sound off |
| Unsolicited mode/teaching speech | none after hint | 0 |

Order: archive year/count; section length/count/depth convention; station P/S/gap in seconds; wave source, elapsed minutes/seconds, receiver degrees and missing direct arrivals; Ma/model; plate/edge/speed/history/volcano; same Pin state with Sound off. No narration pile-up or console exception. Fixed lines still exactly match voice/lines.json and allLines(). Browser fallback was exercised in muted Chrome; a gravel-ranger recording and physical speaker sound were not verified.

#### Facts checked
The pack was retained. Independent retrievals are dated 2026-11-05 in review-source-evidence; the Manual and tool.draft.json name the sources and permissions.

| Material or claim | Named source, permission and check |
| --- | --- |
| 26,230 M5.5+ quakes, 1970-2025 | [USGS ComCat](https://earthquake.usgs.gov/fdsnws/event/1/), [US public domain](https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits). Unique IDs and both date endpoints checked; ten fresh event-ID queries agree within 0.005 degree, 0.05 km and 0.05 magnitude rounding. M5.5 is the declared size fallback. |
| Relief and section heights | [NOAA ETOPO 2022 metadata](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ngdc.mgg.dem%3Aetopo_2022/html), DOI 10.25921/fd45-gt74, CC0 1.0. Sampled 2048x1024 shading and 0.5-degree elevation grid are disclosed. |
| Coasts and 1,251 cities | Natural Earth 50m products, [public domain](https://www.naturalearthdata.com/about/terms-of-use/). Decimation and limited gazetteer stated; no geolocation lookup. |
| 1,609 volcano locations | [NOAA NCEI](https://www.ncei.noaa.gov/products/natural-hazards/tsunamis-earthquakes-volcanoes/volcanoes), DOI 10.7289/V5JW8BSH; [data.gov record](https://catalog.data.gov/dataset/global-volcano-locations-database) explicitly CC0 1.0. NOAA compilation, no direct GVP download; triangles do not assert eruption. |
| Plates, speeds and 0-200 Ma | [Merdith et al. model v1.1b](https://zenodo.org/records/4485738), CC BY 4.0 confirmed independently through Zenodo API. Modified circuits, 5 Ma sampling, 44 resolved polygons and omitted areas disclosed. Speed conversion is km times 0.02 to cm/year over 5 Ma; model frame and hotspot exclusion remain explicit. |
| PREM and iasp91 | Dziewonski/Anderson 1981 and Kennett/Engdahl 1991, published physical numerical facts; [TauP service](https://www.seis.sc.edu/webtaup/) calculated outputs, no software/media bundled. Fresh 30-degree P/S values 370.26385/670.2658 seconds match the pack. Far-side P branches and S absence are explicit. |
| Deep Tonga/Fiji quakes; section meaning | [USGS depth guidance](https://www.usgs.gov/faqs/what-depth-do-earthquakes-occur-what-significance-depth), public domain, and [IRIS source studies](https://dev.iris.edu/hq/files/publications/iris_proposals/doc/IRIS_Core_Proposal_2010_Vol_II_Accomplishments_lorez.pdf), facts only, support nearly 700 km in descending slabs. |
| 81 percent Pacific-rim estimate | [USGS belts](https://www.usgs.gov/faqs/where-do-earthquakes-occur) and [FEMA CERT](https://www.ready.gov/sites/default/files/2019.CERT_.HazardAnnexes.PM_.FINAL_.508c.pdf), government factual summaries. Correctly distinguished from a percentage computed by this filter. |
| Chile M9.5, 22 May 1960 | USGS record and [NOAA account](https://www.ncei.noaa.gov/news/day-1960-chilean-earthquake-and-tsunami), public-domain facts; correctly outside this archive. |
| Liquid core, direct S shadow about 104 degrees; P shadow about 104-140 | [USGS Shadow Zone](https://www.usgs.gov/media/images/shadowzonegif), public domain; IRIS viewer and BGS wave guidance corroborate the physics. Weak and converted branches are expressly omitted. |
| Lehmann, 1936 | University of Copenhagen and [APS historical account](https://www.aps.org/apsnews/2023/08/seismologist-lehmann-earth-inner-core), independently corroborated by AMNH. Facts paraphrased; no copyrighted text or image copied. |
| Atlantic roughly 2.5 cm/year and fingernail comparison | USGS This Dynamic Earth and [University of Malta research account](https://www.um.edu.mt/library/oar/bitstream/123456789/123491/1/THINK36-Mantle.pdf), factual paraphrase only. The latter explicitly contains both statements. |
| Hawaii interior hotspot and older chain northwest | [USGS HVO](https://www.usgs.gov/observatories/hvo/evolution-hawaiian-volcanoes) and [NOAA](https://oceanservice.noaa.gov/facts/hawaii.html), public-domain facts. The model arrows are expressly barred from explaining that hotspot track. |
| Fossil regions and mountain connections | Kious/Tilling, USGS This Dynamic Earth, public domain; [Freie Universitat Berlin](https://www.geo.fu-berlin.de/en/v/geolearning/gondwana/evidences/flora_and_fauna/index.html), Geological Society and [NPS](https://www.nps.gov/subjects/fossils/supercontinent-pangea.htm) corroborate the connections. Original schematic outlines, not specimen positions or organisms living at the dial date. No outside figures copied. |

#### Sensitivity
Real disasters remain observations, without deaths, harm photography or ratings. Historical local counts are not hazard forecasts. Place names come from named catalogs; no claim about people or cultural traditions is added. A later cultural lens can check geographic naming, especially Hawaiian names, without treating this as a disaster game.

#### Flattest moment left
Precise arrival picking still benefits from the half-second keyboard nudges, especially on a phone. The ruler and taller trace make it an intelligible measuring task; no automatic answer, reward or lesson ladder replaces it.

#### Graphics
All cold, before/after, phone, keyboard, fallback and comparison PNGs were inspected; all 73 audit frames were inspected through thirteen contact sheets, with affected frames also opened individually. No new painted image was needed: scientific surfaces remain code and licensed data. Final HTML is 1,957,170 bytes, about 1,911 KiB, below 2 MB. Checked text pairs span 5.50:1 to 8.92:1; grayscale was inspected. Every required size was covered, including a real 375x812 iframe.

#### Short test
- Would a kid open it unassigned? **Yes, provisionally:** spin and Play produce an immediate real-world pattern worth poking; no assigned route is needed.
- Would an adult play for fun? **Yes:** actual geography, deep sections, measured arrivals and reconstruction support repeated comparisons.
- Is the real thing the interface? **Yes after the phone fix:** observations, relief, traces and model rays carry the interaction; prose stays in the Manual.
- Does it work with no score or finish? **Yes:** free exploration works indefinitely; stopping the archive produces no completion screen.

![Cold Living Earth full-archive frame beside Elements Inspector](../../_scratch/living-earth/review-family-comparison.png)
Lesson-creep scan: only 19 uses of points remain, all geometry/data/WebGL or section properties. Every other requested search term is absent from src.html and all are absent from fixed voice lines. No em dash appears in source.

#### Audit
Ran once with a 40-minute cap on Chrome 9951 and host 8755: **finished, 525 grouped leads**, all triaged in review-audit-triage.json. No console errors, undersized-control leads, horizontal overflow, stuck resize states or infinite Motion-off animation were reported.
454 leads are the full-stage canvas behind its controls/readouts; 7 are the intentionally disappearing first hint; 20 concern visible marker text above the native range hit areas; 39 concern the modal Manual covering the inert instrument. Frames confirm these are intentional, not hidden working controls.
The other 5 are the opening hint canceled by rapid instrument switches. Kept that cancellation: the stale hint should stop, and the Curiosity brief permits only the initial hint followed by user-requested Read, not automatic mode instructions or a repeated welcome. The normal paced voice walk hears the hint whole.
The audit host predates the final city-ranking and fossil-outline changes; those narrow changes were separately rechecked, without a second full audit. Failed Chrome launches were bounded and retained. An early host favicon 404 and the pixel-test readback performance advisory came from review fixtures, not automatic product network calls or product exceptions.

#### Left open
Physical touch hardware, physical Chromebook performance and recorded gravel-ranger timbre were not certified. The model's unresolved plate areas, 5 Ma velocity average, synthetic surface-focus seismograms and schematic fossil regions remain openly stated scientific limits. No engine change is requested.
Unattended choices followed the brief: retain the explicit M5.5 fallback and licensed model, rank an exact city first, and fix access by exposing the material rather than adding a lesson flow. No commits or writes outside the two allowed folders were made.

<!-- end part -->

## Refine

<!-- part: refine.md -->

PASS (exit check 2026-11-06)
Counts: blockers 1 (general 0, family 1), should fix 11 (general 7, family 4), polish accepted 19

### Refine: living-earth

Merged from `refine/teaching.md`, `refine/play.md` and `refine/craft.md` (no sensitivity file; all three lenses found
nothing cultural, Native or hard-history, and disasters appear as data only). Frames: teaching
`S:/CurioClass-codex-scratch/living-earth/teaching/out/`, play `S:/CurioClass-codex-scratch/living-earth/play/`
(r1 to r4), craft `S:/CurioClass-codex-scratch/living-earth/craft/f1/`, shared audit
`S:/CurioClass-codex-scratch/living-earth/audit-r1/`. Integrator spot-checked src.html:1660-1669 (plateMotion),
974-985 (renderSection), 1001 and 1944-1948 (station markers), 1318 (key handler) and 745-746 (touch): each lead holds.

The short test passes in every lens (play runs 1970 to 2025 in 18.7 s, the slices show the slabs, no score or finish
anywhere). Ten quakes and the ComCat totals check out (teaching: 14 events by id, 26,230 events, 44 M8+). Do not undo
any of that while fixing.

#### Blocker
1. **Pin SPEED and the Arrows layer show the model's reference-frame drift, not how fast the plate moves.**
   src.html:1660-1669 (`plateMotion`), Pin readout 1695-1696, Read text 1175, Arrows 1797-1806. Speed and heading come
   from Merdith et al. 2021's 0-5 Ma rotation relative to plate 000 (its absolute, palaeomagnetic frame), which carries
   a large rotation shared by every plate. Against ITRF2014 GPS poles (teaching, recomputed in Python): Denver reads
   6.2 cm/yr at 253 deg (GPS 1.6 at 247), Sydney 2.8 at 325 (GPS 5.7 at 19), Perth 4.5 at 356 (6.9 at 34), Cairo 5.5
   at 12 (2.9 at 53), Honolulu 9.3 at 264 (7.1 at 299). Australia, the fastest continent, reads slower than North
   America and in the wrong direction; Arrows show most plates drifting the same way, which hides "two plates heading
   at each other" (spec Things to do 10, 11). Seen: teaching numbers.json, nums2.json, rot.json; pin-sydney.png,
   atlantic-all.png; play r1/pin-denver, pin-hawaii. Fixed looks like: keep Merdith for Rewind; for present-day
   motion, remove the shared rotation (a no-net-rotation frame built from the model's own plates, area-weighted) and
   add the motion relative to the plate across the nearest edge ("opening 2.5 cm/yr" or "closing 6 cm/yr" beside
   EDGE). Check the result against the ITRF2014 table above (within about 1 cm/yr and 20 deg is a pass), redraw the
   Arrows from the same numbers, and re-check the fingernail field note against what the readout now shows. If the
   Merdith rotations cannot give that, leave SPEED as relative-across-edge only and note it in notes.md; switching to
   another plate motion model is a spec question (below). (family:curiosity)

#### Should fix
1. **Stations: a drag on the trace can never set the S marker.** src.html:1001 creates each station with `p:0,s:0`;
   1944-1948 picks the nearer marker, so a press at the S packet always moves P (play: press at S 990.8 s on Sumatra
   2004 left P 997.5, S 0, "S−P -997.5 s"; r2/st-drag-S-first.png, r2/st-drag-S-afterP.png). Only Shift-drag (no
   Shift on a phone) or the small sliders reach S. Fixed: start S at the right end of the trace (or hide each marker
   until placed) and give each marker its own grab handle, so a press near either packet moves the right one. Also
   separates the P and S labels that overlap at 0 as an "8" (craft zoom-trace.png). (family:curiosity)
2. **The first-run line is spoken after the action it asks for.** src.html:745-746 `touch()` speaks "Drag to spin.
   Press play." on any first action: after Play it says "Press play" while the archive runs, after a drag it says
   "Drag to spin", after a tool tab it says "Drag to spin" where a drag now draws a slice line; the on-screen hint is
   hidden at the same moment. Seen: play r3 voice logs (v-first-play, v-first-slice, v-first-drag), craft v-play5,
   v-drag-first, audit one-click rows 0 to 13. Fixed: speak only the half not yet done ("Press play." after a drag,
   "Drag to spin." after Play), and nothing once a tool panel is open; give the line a `valid` check. (family:curiosity)
3. **Slice draws the sea floor below the shallow quakes.** src.html:974-985: quake depths are 1:1 but the ETOPO
   profile is multiplied by 20 on the same axis, so a 4 to 5 km sea floor sits at 80 to 100 km and every Mid-Atlantic
   quake (10 to 20 km) floats above it, the opposite of the lesson. Seen: teaching slice-mar.png, slice-japan.png,
   slice-peru.png. Fixed: draw the exaggerated profile in its own strip above the 0 km line (or exaggerate only above
   a sea-level baseline) and label "sea level" and "sea floor"; keep the x20 note. (family:curiosity)
4. **Wave shows three different shadow edges and an unreachable S arrival.** src.html:735-742 (`arrival`), 1096
   (shadow arc), 1104-1106, 936 (globe ring at 104 deg), Manual line 580. The iasp91 table has direct P to 98 deg and
   direct S to 99 deg, so from 99 to 104 deg the readout says "P NO BRANCH · S NO BRANCH" while the receiver sits
   outside the drawn S SHADOW arc; S at 98 to 99 deg arrives at 25:06 to 25:14, past the 25:00 end of the fader and the
   trace. Seen: teaching nums2.json, wave-100.png. Fixed: draw the arc and ring from the table's real edges (about 99
   deg for direct S, 98 to 140 deg for direct P), replace "NO BRANCH" with "no direct wave here", say in the Manual
   that waves bend round the core there (diffracted waves, not drawn), and run the window to 26 min. (family:curiosity)
5. **Stations words do not follow the state.** Panel line src.html:475 keeps "Tap three stations" after three are
   placed, struck and solved; the readout shows "FIT AMBIGUOUS" before anything is measured; Circles with unset
   markers reads "DIST 0 km" and draws zero circles; every revealed quake at the default year is tagged "OUTSIDE
   FILTERS"; under 200 km the label becomes "CATALOG / FIT", a threshold verdict close to Done-when 10's "never a
   rating" (src.html:930, 1846). Seen: play r2/st-solved.png, audit state-stations-1366x768.png. Fixed: one short
   instrument-status line that follows the state ("Tap three places for stations", "Strike to record a quake", "Set
   P and S on each trace", "Circles", "Reveal"), "SET P AND S" until both markers have moved, no FIT text at all,
   the marker labelled "CATALOG" with the offset in km beside it, and no OUTSIDE FILTERS tag on a Reveal (or move the
   year to the event, as the catalogue list does). This is a status line, not numbered steps or progress. (general)
6. **The Manual and panel captions are written for a geophysicist.** Manual src.html:550-664; captions 459, 475, 490,
   499, 507; readouts "NO BRANCH", "UNRESOLVED MODEL AREA", "QUAKES HELD", "FIT AMBIGUOUS". Examples: "finite rotations
   are resolved through the published plate circuit relative to plate 000 ... quaternion interpolation", "normalized
   three-plane fit", "schematic older fossil evidence · modern overlays withheld", "Pn and far-side PKP/PKIKP". Grade
   band 4 to 12, anchor grade 6, solo at home (rule 4). Fixed: each Manual section opens with one or two plain
   sentences at about grade 6 (what to do, what you will see: "Each dot is a real earthquake. Bigger dot, bigger
   quake. Colour shows how deep it was."), with the precise honesty notes kept below a "For the curious" line; one
   plain sentence on S-P beside the markers; captions in plain words ("rays bend through a model Earth");
   "UNRESOLVED MODEL AREA" becomes "plate not known here". "Things people have found" becomes short findings, with
   its two opening paragraphs of instructions moved into the how-to sections. (general)
7. **The selected-quake record card covers the globe when a tool is open.** With a panel open the globe moves left
   (`x = w*0.29`, about src.html:886) and the card at x 25 to 250 covers its west limb: station B and the Reveal marker
   run under it (only the "G" of CATALOG shows). Same at 680x425 and 800x500 with no tool. Seen: play r2/st-solved.png,
   audit state-stations-1366x768.png, state-selected-680x425.png. Fixed: dock the record inside the open tool panel, or
   collapse it to one line while an instrument is open, keeping the globe clear. (general)
8. **Shortcut keys go dead after any button click.** src.html:1318 returns early whenever a BUTTON has focus, so after
   clicking Play, a layer, a tool tab or zoom, Q/V/P/F/A, [ ] and S do nothing, and Space presses the focused button
   (after clicking Volcanoes, Space toggles Volcanoes). Seen: reading the handler (integrator confirmed), craft
   k-space-body. Fixed: let the letter and bracket keys through on buttons; keep Space as Play unless the focused
   button is something else the student would expect Space to press, and say the rule in the Manual. (general)
9. **The Volcanoes layer halves the frame rate on a slow machine.** `drawGeography` draws 1,609 triangles as 1,609
   fill+stroke paths every frame; at 4x CPU throttle the median frame goes 16.7 ms (default) to 33 ms (+Volcanoes) to
   50 ms (all layers). Done-when 6 asks 60 fps on a Chromebook. Seen: craft throttle.py, throttle2.py. Fixed: one
   path for all triangles (one fill, one stroke), or a GL point layer like the quakes; re-measure. (general)
10. **The compact console loses its labels under about 1050 px wide.** At 680x425, 800x500 and 760x900 the depth
    faders read "≥ 0 km" and "≤ 700 km" with no DEPTH, "TIME 1970 SPEED 3 yr/s MAGNITUDE ≥ 5.5" runs as one line, the
    layer buttons show only Q V P F A, the section is about 40 px tall with "A" printed over "2009 km → B", the trace
    is about 50 px and its axis prints "20 25 min" as "2025 min". Seen: audit size-680x425.png,
    state-stations-680x425.png, craft f1/t-pin-760.png, play r2/preview-680-slice.png, preview-680-stations.png.
    Fixed: keep "DEPTH" (or "D ≥", "D ≤"), a gap or rule between fader readouts, layer names (short words, not
    letters), and give an open panel the globe's room at this size (or stack) so the section and trace are usable.
    (general)
11. **The Manual's 29 source links navigate the tool away.** No link has a target; on the site a tap on "USGS record"
    loses the instrument state. Seen: craft grep (0 of 29). Fixed: `target="_blank" rel="noopener"` on every
    external link. (general)

#### Polish accepted
1. **Keep the slow turn during the first Play.** src.html:1344 (`!state.touched`) stops the globe on Play, so the
   first run shows only the West Pacific and the Atlantic seam in the spec's first reaction never appears (play
   r1/play-end.png). Keep turning until the student drags. (general)
2. **Wave: label the shadow only once the rays get there, and give the cutaway room.** The violet "S SHADOW" arc and
   readout show before Fire (audit state-wave-1366x768.png); the disc is about 135 to 140 px in a 390 px panel at
   1366x768 (play r1/wave-end.png, craft f1/t-wave.png) and the MANTLE and LIQUID OUTER CORE labels sit in the corners.
   Show the shadow arc and label after the S front reaches the core's far side, let the cutaway fill the panel height,
   and put the layer labels on the layers. (family:curiosity)
3. **Rewind on the Play pad.** Play is disabled in Rewind (play r1/rewind-200-atlantic.png); let it run 0 to 200 Ma (and
   back) at a steady pace, stepping in calm mode. (family:curiosity)
4. **Tap a station triangle to choose its trace.** Today the channel is only a select (play finding 9). Tapping A, B or
   C on the globe selects that trace; keep the select for keyboard. (family:curiosity)
5. **Motion arrows that can be read.** After Blocker 1: a few arrows per plate near its edges, drawn above the dots,
   not one small cyan arrow at the centroid under them (play r1/layers-hawaii.png). (general)
6. **Calm mode steps the wave.** Fire with Motion off jumps to 25:00 (src.html:1223); step it by the minute as year
   playback steps by years (POLISH, calm keeps time). (general)
7. **Read in plain speech.** "1974. 2252 earthquakes in the magnitude 5.5 and greater catalogue under these filters"
   becomes "1974. 2,252 earthquakes of magnitude 5.5 or more so far." (play r3 v-read-after-play). (general)
8. **An in-view quake count for Things to do 13.** QUAKES counts the whole sphere, so "compare the Pacific rim with the
   rest of the world" cannot be done. Add IN VIEW (quakes on the visible face of the globe) beside QUAKES, so a student
   can turn the Pacific to face them and then the Atlantic. (family:curiosity)
9. **A slim drum row in compact layouts.** The drum is hidden below 1050 px (CSS lines 280, 380); the spec keeps it at
   375 under the sheet. A 40 to 50 px row. (family:curiosity)
10. **Mipmaps on the relief texture.** src.html:1495 uses LINEAR with no mipmaps, so Tibet and the Andes shimmer as
    white grain at 1x (craft zoom-tibet.png, play r1/zoom6-tibet.png). `generateMipmap` with LINEAR_MIPMAP_LINEAR (the
    texture is power-of-two). (general)
11. **Station hardware for the speed knob and depth fader.** The spec names a speed knob with four detents and one
    two-handle depth fader; they ship as plain range sliders. Draw the knob with detents and join the two depth
    handles on one track, keeping keys and announced values. (family:curiosity)
12. **Readable type at 1366x768.** Layer names and survey labels 10 px, fader readouts and Read 11 px. Raise anything
    read while using a control to 12 to 13 px, with Read matching Manual. (general)
13. **Teacher notes: a content line and real home ideas.** notes.md gets one line that the M8+ catalog and Strike name
    real deadly events (2004 Sumatra, 2011 Tohoku, 2008 Sichuan, 2015 Nepal, 2023 Kahramanmaras) some students or
    families may have lived through (rule 8). Replace "Ask a family member what a map leaves out" and the paper-map
    string idea with ones doable tonight, such as "pin your town together and look up the last quake felt there".
    (general)

Nits accepted (cheap and clearly right):
14. On load the strip reads YEAR 1970, QUAKES 0, but moving the dial to 1970 gives 475 (src.html:677, 750, 1189). Make
    load and dial agree (start at the end of 1970, or show 0 until play and say so). (general)
15. Strike starts at a random event of the curated set instead of always Sumatra 2004 in a fixed order.
    (family:curiosity)
16. In Rewind, "QUAKES HELD" becomes "QUAKES OFF" (or the pair hides) and the depth legend hides. (general)
17. Station marker faders get a Shift jump (10 s) like every other fader. (general)
18. One Manual line: about 500 ComCat place names show "?" for a lost accent letter, as ComCat itself does.
    (general)
19. The trace axis keeps "20" and "25 min" apart at every size (covered with Should fix 10 if done there). (general)

#### Settled calls
- **Audit leads.** All three lenses agree: the ~460 "#globe overlaps" rows (the globe is the full-bleed stage),
  every "hint out of view" row (the hint is meant to go after the first action), and the Manual "keep region" rows
  (modal dialog) are not findings. Do not move overlays off the globe to clear them.
- **No sensitivity agent.** All three lenses: nothing cultural or Native; disasters shown as place, date, depth, size,
  never tolls. Keep it that way; the teacher-notes content line (Polish 13) is all that is needed.
- **Wave giveaway.** Teaching found no giveaways; play saw the shadow labelled before Fire. Settled for play: the
  shadow is the finding, so it shows when the rays get there (Polish 2). No question, score or "found it" moment is
  added.
- **Stations status line and FIT.** The fix (Should fix 5) is an instrument status line, not numbered steps, a
  progress bar or a verdict. The 200 km threshold label goes; the offset stays a km readout (Done-when 10, CODEX-CURIOSITY).
- **Tags on merged items.** Should fix 5 (play general, craft family) and 6 (teaching general, play family) are
  counted general: the fix is the POLISH and rule 4 rule any tool keeps.
- **Keep:** Merdith for Rewind; the M5.5 floor and its Manual line; ComCat place names as ComCat has them; Strike
  naming events by place only; no welcome screen; the honesty notes (moved under "For the curious", not cut).

#### To the spec's open questions
- **HS-ESS1-5 (science-9-orbits-and-earth-s-history) is listed under "Also reaches" but nothing shows the ages of
  crustal rocks** (teaching S4). Either add a sea-floor age layer (an ocean age grid such as Seton et al. 2020, CC BY
  4.0 to be verified), readable by Pin and along a Slice, which would also give Hawaii's chain (Things to do 12,
  teaching P1) and the Atlantic opening real ages; or drop science-9 from "Also reaches" (rule 2, never a thin
  activity). Codex does not add the layer in this round.
- **Present-day plate motion source** (Blocker 1). If Merdith's own rotations cannot give a believable no-net-rotation
  speed, should Pin use a present-day plate motion model (ITRF2014-PMM or NNR-MORVEL56, licence to check) instead? That
  changes the spec's source line.
- **Rewind as a test, not only a playback** (teaching P4): a "drag South America to fit Africa" try before or beside
  the model, as Wegener did, with no score. A new mode, so it is the spec's call.
- **Stacked record section** (play 9): A, B and C traces stacked as a real record section instead of one trace at a
  time. A layout change to the Stations panel; worth deciding with the 375x812 sheet in mind.

#### Not taken
- Wave: draw the receiver on the globe along a great circle from the source (play 7, second half): the globe ring at
  104 deg already ties the cutaway to the globe; revisit after Should fix 4.
- Kit "✨ Motion" emoji on the power panel (craft 10): a kit change touching every tool, outside this tool's files; log
  it for the kit, not here.
- Reykjavik reading Eurasia at the 0.1 deg model (teaching N4): the panel already says "boundary area"; model honesty.
- Nearest volcano "Unnamed" for Honolulu and Mumbai (teaching N4, play 18): faithful to the NOAA list.
- 375x812 marker sliders too coarse (play 9, second half): covered by the trace drag fix (Should fix 1) and Shift
  jumps (nit 17).

#### Exit check (2026-11-06)

Scoped re-check of the merged list on the current bundle (`living-earth.html`, 1,991,170 bytes), with a fresh audit
(`S:/CurioClass-codex-scratch/living-earth/exit/audit-r2/`) and my own drive frames (`S:/CurioClass-codex-scratch/living-earth/exit/d1/` to `d4/`, all 1366x768 unless named).

##### Blocker
1. **Fixed.** `plateMotion` now subtracts an area-weighted NNR vector (src.html:2117-2128). Recomputed in the bundle:
   Denver 1.6 cm/yr at 247 deg (ITRF2014 1.6 at 247), Sydney 5.9 at 17 (5.7 at 19), Perth 7.2 at 33 (6.9 at 34), Cairo
   3.2 at 53 (2.9 at 53), Honolulu 6.9 at 294 (7.1 at 299): all five within 0.3 cm/yr and 6 deg (d1 default js).
   Pin at Sydney shows SPEED 5.9 cm/yr at 17 deg plus EDGE MOTION closing 0.4 cm/yr against the Pacific (d1/pin-sydney).
   Arrows now diverge across the Atlantic, South America west, Africa north-east, many arrows near the edges, above
   the dots (d1/arrows.png). The fingernail line now says "a few centimetres a year" and points to EDGE MOTION.

##### Should fix
1. **Fixed.** S starts at 1560 s with its own labelled handle at the right end (d3/stations-drag-S.png). A real drag
   from the S handle to the S packet set S 1031.5 s (true S 1031.4), P untouched (d4). Note: a press in the trace body
   still moves the nearer marker (at the S packet with S unplaced that is P), which is the handle design asked for, and
   the P and S labels no longer overlap.
2. **Fixed.** Held click on Play speaks "Drag to spin." only, the globe keeps turning (lon 156.3, running); a fresh
   Slice click speaks nothing (d1 voice-play, voice-slice). Audit one-click table: only Play and Read speak; five-click
   and two-tap rows clean. `valid` checks present (src.html:1092-1093).
3. **Fixed.** Relief in its own "sea level / sea floor x20" strip above the 0 km line; the Mid-Atlantic slice (2025)
   puts 18 quakes, deepest 20 km, just under 0 km (d2/slice-mar-2025.png); Japan slice reads 358 quakes to 560 km.
4. **Fixed.** At 100 deg after 26:00: "P no direct wave here, S no direct wave here", receiver inside the drawn S shadow
   arc (d2/wave-100-end.png); at 99 deg S arrives 25:14 inside the 26:00 window (d2 wave-99-end). Direct P edge 98.
5. **Fixed.** Status follows the state ("Tap three places for stations 0/3", "Set P and S on each trace", "Catalog
   location shown"); readout "SET P AND S" until both are set; no FIT text; Reveal shows OFFSET in km and no OUTSIDE
   FILTERS tag on a 1998 event at year 1970 (d2/stations-solved.png, d3).
6. **Fixed (spot-checked).** Manual opens with plain sentences ("Each dot is a real earthquake. Bigger dots mean bigger
   quakes...") with "For the curious" below; captions plain ("Rays bend through a model Earth"); "S minus P is the wait
   between the two waves" beside the markers. Old readout words (NO BRANCH, FIT AMBIGUOUS, UNRESOLVED MODEL AREA,
   QUAKES HELD) no longer in src.html.
7. **Fixed.** Record docks as one line at the top of the Stations panel (d2/stations-solved.png); at 680x425 it sits on
   its own line between globe and toolbelt (d1/selected-680.png).
8. **Fixed.** After a click on Volcanoes: "]" moved speed 1 to 2, Space toggled the focused Volcanoes (the stated
   rule), a keydown "q" on the focused button toggled Quakes (d2 keys; q dispatched as a page event, the driver has no
   letter keys; Codex's native Q/V/P/F/A walk agrees). Manual states the Space rule.
9. **Fixed (not re-measured).** Volcanoes are a GL point layer; Codex's paired 4x-throttle medians 16.7 ms. Accepted on
   its evidence; no regression seen in frames.
10. **Fixed.** At 680x425 and 800x500: "D >= 0 km / D <= 700 km", spaced readouts, layer names in words, the open
    panel gets usable room, slim drum row present (sheet `S:/CurioClass-codex-scratch/living-earth/exit/sheet2.png`). Audit's two depth "text hidden" rows are
    the joined track's own thumbs (settled by Codex, both thumbs drag).
11. **Fixed.** 30 of 30 Manual links have `target="_blank" rel="noopener"` (d1 manual js, bundle grep).

##### Polish (bulk spot-check)
Seen fixed: 1 (turn continues on first Play), 2 (no shadow before rays: "await rays" at T+1:12), 3 (Rewind plays,
d1 rewind), 5, 7 (Read: "1970. 475 earthquakes of magnitude 5.5 or more so far. 343 on this face"), 8 (IN VIEW in the
strip), 9, 11 (dial and joined track visible), 14 (load and dial both 475), 16 (QUAKES OFF in Rewind), 19 (trace axis
"20" and "26 min" apart). Not re-checked: 4, 6, 10, 12, 13, 15, 17, 18 (Codex evidence only; polish never blocks).

##### Regressions
None found. Default screen, Slice, Stations, Wave, Rewind and Pin each shot once; the frames tied to each fix above.
OUTSIDE FILTERS remains on a normal catalogue selection outside the filters (src.html:1150), as intended. One exception
in my d1 wave shot was my own probe calling `arrival(100,1)` with a wrong phase key, not the tool.

##### Gate
1. Done when: no regression on the short test frames; Codex's checks plus mine hold. Yes.
2. Codes: anchor MS-ESS2-3 taught; science-9 (HS-ESS1-5) stays an open spec question already written down in this file
   (add a sea-floor age layer or drop it from "Also reaches"). Carry it to the Review Desk. Yes, with that note.
3. Solo defaults: one quiet hint, first action speaks only the half not done, Manual plain-first. Yes.
4. Sensitivity: not flagged by any lens; teacher-notes content line added. Not required.
5. No blocker or should-fix open. Yes.
6. Bundle: 1,991,170 bytes (under 2 MB); audit shows no errors in any row; no fetch, external script or stylesheet in the
   bundle (the audit itself does not list network). Yes.
7. Voice: `voice/lines.json` holds exactly the two hint halves, matching the two `V.how` calls; audit counts clean;
   recordings absent, browser-voice fallback. Yes.

#### Audit pilot
- Leads confirmed: none new that are findings; Play speaks one line and Read speaks current state (matches my frames).
- Leads wrong: the ~550 "#globe overlaps" rows, Manual-modal "text hidden" and "keep region" rows (settled), the depth
  track "text hidden" rows (joined two-thumb track), marker label "hidden under label" rows (ancestor hit-test, text
  visible in d3/d4 frames), record "hidden under #record-dock" rows (dock is its parent).
- Missed: no network-request check in the report; the trace drag (handle versus body press) needs a held drag, which
  the audit does not do; the first save is written while it still runs, so wait for the "Not finished" banner to clear.

<!-- end part -->

<!-- part: refine/craft.md -->

### Refine, Craft lens: living-earth (Curiosity No. 04), round 1

Cold lens on the built bundle `tools/living-earth/living-earth.html` (not re-bundled). Judged against
CODEX-CURIOSITY.md, the VISION "Curiosities" section, STANDARDS and BASELINE. My frames and scripts:
`S:/CurioClass-codex-scratch/living-earth/craft/` (frames in `f1/`). Shared audit: `audit-r1/`.

#### Contract

- One file, 1,957,170 bytes: under the 2 MB goal. Kit used for voice, tone and Motion/Sound (no kit header or cards).
- No network requests: `performance.getEntriesByType('resource')` is empty after load (`f1/c-default`).
- No console errors or exceptions in any of my 20 shots; the audit's every-control and resize rows are clean too.
- Motion off: cited from the audit ("clean: nothing runs forever"); the code steps playback by whole years when reduced.
- Lesson creep: no score, goal, level, sticker, badge or finish anywhere (grep and frames). See finding 12 for "FIT".
- Words: no em dashes in src, notes or tool.draft.json; "Curio Class" never "Curio" alone; the Manual states that
  settings stay on this device (src.html:663). Art: `art/prompts.json` has no assets and src has no `art:` tokens.
- Contrast: every small label I sampled is light on near-black slate (well above AA). Cultural/Native/hard-history:
  nothing to flag; disasters appear as data only.

#### Findings

1. **should fix** (family:curiosity). src.html:746 `touch()`. The first-run line "Drag to spin. Press play." is
   spoken after the student's first action, whatever that action was. After a first press of Play it says "Press
   play" while the archive is already playing; after a first drag it says "Drag to spin"; after a first tap on a tool
   tab it plays with the Slice/Stations/Wave panel open, where a drag on the globe no longer spins (in Slice it draws
   the section line). The hint on screen is hidden at the same moment, so the voice is the only place the stale line
   appears. Seen: `vlog` in my `v-play5`, `v-drag-first`, `v-sound-first` shots (the line plays at t~1.3 s, after
   the click), and the audit's one-click table (rows 0 to 13 all speak it). Better: give the line a `valid` check
   (no tool open, not running, no drag yet). If the first action already did one half, say only the other half
   ("Press play." after a drag), and skip the line unmarked when a tool panel opened.
2. **should fix** (general). src.html:1318. The global key handler returns early whenever a BUTTON has focus. After
   any click on a button (Play, a layer, a tool tab, zoom), Q/V/P/F/A and [ ] do nothing and S never strikes. Space
   then presses the focused button instead of Play, so after clicking Volcanoes, Space toggles Volcanoes. Seen by
   reading the handler; my `k-space-body` shot confirms Space and ] work only when nothing is focused. Better: let
   the letter and bracket keys through on buttons. Keep Space for Play unless the button is Play itself, or document
   Space as "press the focused control".
3. **should fix** (general). src.html `drawGeography` (volcano loop). The Volcanoes layer draws 1,609 triangles as
   1,609 separate fill+stroke paths every frame. With Chrome's CPU throttled 4x (my Chromebook stand-in, headless
   with software GL), spinning the globe:

   | layers | median frame | p90 |
   |---|---|---|
   | default (every dot, relief) | 16.7 ms | 33 ms |
   | + Volcanoes | 33 ms | 50 ms |
   | all layers (Volcanoes, Edges, Arrows) | 50 ms | 67 ms |

   Unthrottled, everything holds 16.7 ms (60 fps) with all 26,230 dots. Software GL inflates every row, so treat
   these as relative costs. Volcanoes is the one layer that halves the rate by itself. Better: one path for all
   triangles (one fill, one stroke) or a GL point layer like the quakes. Seen: `throttle.py`, `throttle2.py`.
4. **should fix** (general). With a tool panel open at 1366x768 the globe moves left (`x = w*0.29`, src.html ~886),
   and the selected-quake record card (top-left) covers the globe's left limb. In the audit's Stations state the
   Reveal marker for the struck quake (CATALOG, Sumatra) sits under the card; only the "G" of its label shows.
   Seen: `audit-r1/state-stations-1366x768.png`. Better: collapse the card to one line while an instrument is open,
   or keep the globe clear of it.
5. **should fix** (general). Compact console under about 1050 px wide (680x425, 800x500, 760x900): the depth faders
   lose their names, leaving "≥ 0 km" and "≤ 700 km" unlabeled, and "TIME 1970 SPEED 3 yr/s MAGNITUDE ≥ 5.5" runs
   together as one line. Seen: `audit-r1/size-680x425.png`, `f1/t-pin-760.png`. Better: keep "DEPTH" (or "D≥", "D≤")
   and put a gap or rule between fader readouts.
6. **should fix** (general). The Manual's 29 source links have no `target="_blank"`. On the site a student who taps
   "USGS record" navigates the tool's own frame away and loses the instrument state. Seen: grep (0 of 29 links have
   a target). Better: `target="_blank" rel="noopener"`.
7. **polish** (family:curiosity). The drum seismograph is hidden below 1050 px wide (CSS lines 280 and 380), so it
   is gone at 1000x625, 800x500, 680x425, 760x900 and 375x812. The spec keeps it at 375 under the bottom sheet, and
   the drum is part of the station grammar. Seen: every audit size frame under 1050 wide. Better: a slim 40 to 50 px
   drum row in compact layouts.
8. **polish** (general). src.html:1495. The relief texture uses `LINEAR` minification with no mipmaps, so the
   2048x1024 image speckles and shimmers when minified at 1x: the Tibetan Plateau and Andes show as white grain,
   worst near the limb. Seen: `zoom-tibet.png` (from `f1/c-default`); at 3x (`f1/c-asia-zoom`) it is clean. Better:
   `generateMipmap` with `LINEAR_MIPMAP_LINEAR` (the texture is power-of-two).
9. **polish** (family:curiosity). The spec's instrument controls are flattened to plain range sliders: the time
   dial, the speed knob with detents and the two-handle depth fader (shipped as two separate sliders). They work and
   announce their values, but they read as a web form, not station hardware. Seen: every size frame. Better: at
   least the speed knob with its four detents and a joined two-handle depth fader.
10. **polish** (general, kit). The kit writes "✨ Motion" / "⏸ Motion" on the power panel (kit/curio.js:15). An
    emoji on a station toggle breaks the instrument grammar, and the Sound and Read beside it have no icon. Seen:
    every frame. Better: a kit option for a plain label (benefits every Curiosity).
11. **polish** (general). Type is small at the main size, 1366x768: layer button names 10 px, fader readouts 11 px,
    survey labels 10 px, Read 11 px next to Manual 13 px. Seen: computed styles in `f1/c-default`. Better: 12 to 13
    px for anything a grade 4 student reads while using a control, with Read matching Manual.
12. **polish** (family:curiosity). Stations readouts before the markers are set. Circles with both markers still at
    0 reads "DIST 0 km" and draws zero-radius circles. Reveal reads "FIT AMBIGUOUS". At under 200 km the globe label
    becomes "CATALOG / FIT", a threshold verdict that sits close to the "never a rating" rule (spec Done when 10).
    Seen: `audit-r1/state-stations-1366x768.png`, src.html:930 and 1846. Better: "SET P AND S" until both markers
    have moved, and label the marker plainly ("CATALOG") with the offset in km beside it.
13. **polish** (general). The Wave cutaway is about 140 px across in its panel at 1366x768, small for the
    instrument's main picture. Its MANTLE and LIQUID OUTER CORE labels sit in the corners, pointing at nothing. Seen:
    `f1/t-wave.png`. Better: let the cutaway fill the panel height and put the labels on the layers.
14. **nit**. In Rewind the survey strip reads "QUAKES HELD", and the depth legend stays on screen with no quakes
    drawn. Seen: `f1/t-rewind.png`. Better: "QUAKES OFF" or hide the pair, and hide the legend.
15. **nit**. The P and S labels overlap at 0 on the trace and draw one "8"-like glyph (`zoom-trace.png`). At 680x425
    the trace axis prints "20 25 min" as "2025 min" (`audit-r1/state-stations-680x425.png`).
16. **nit**. The station marker sliders run 0 to 1500 s at 0.5 s with no Shift jump, unlike every other fader.
    Arrow keys alone need about 1,000 presses to reach a 9-minute P arrival (PageUp works).
17. **nit**. At 680x425 the layer buttons show only Q, V, P, F, A. "F" for relief and "P" for edges are cryptic
    without the full names (the aria-labels are fine). Seen: `audit-r1/size-680x425.png`.

#### Access walk

- Tab order (1366x768, `f1/k-tabwalk`): globe, five tool tabs, Play, Year, Speed, Magnitude, Depth min, Depth max,
  catalogue select, five layers, zoom out, zoom in, Manual, Motion, Sound, Read, then back to the globe. Every stop
  has a visible 3 px outline, and every target is at least 44x44.
- Globe keys work (`f1/k-globe-keys`): Right, Shift+Up, = = and Enter select the nearest filtered quake and announce
  it in the live region. Magnitude: Down stops at 5.5, Shift+Up adds 0.5. Speed and Ma set `aria-valuetext`.
- The Manual is a modal `<dialog>`: it traps focus, and Close returns focus to Manual. Close on a tool returns focus
  to its tab.

#### Standard voice check

The tool has one fixed line (`voice/lines.json` and `allLines()` match word for word). Read speaks a live
`readState()` text.

| line | kind | expected | spoken |
|---|---|---|---|
| Drag to spin. Press play. | how | once per load | once (5 held Play clicks 2.5 s apart: 1) |
| Read (state text) | read | every press | every press; it cut the how line (`cut: read`) and was heard whole |

- First tap: a plain Play tap, a drag or a tool tab gets the how line at once, but it is stale (finding 1). Sound
  first: nothing spoken (correct). Read first: the state text only (audit row 17). There is no welcome by design.
- Two quick taps on a tool tab: `setTool` hushes the how line and it is never heard whole (audit). Acceptable once
  finding 1 is fixed, since the line is stale there anyway.
- Order: no line plays after a newer action in any run.

#### Audit pilot

- **Confirmed:** the record card over the globe in the Stations state (finding 4). The quick-tap hush of the how
  line (voice table). The Stations trace and marker area at 680x425 (finding 15's axis labels).
- **Wrong:** about 470 "#globe overlaps X" rows. The globe canvas is a full-bleed stage by design, and the legend,
  hint, position and toolbelt are meant to float over it. Every "hint out of view" row: the hint is meant to go
  after the first action. Manual "keep region" and "hidden under manual-drawer" rows: the Manual is a modal dialog
  by design. The marker-slider overlap rows ("P 0.0 s" under `#marker-p`): the label wraps its slider and reads
  cleanly on the frames.
- **Missed:** findings 1 (stale first line), 2 (shortcut keys dead after a button click), 3 (volcano layer frame
  cost), 5 (unlabeled depth readouts in compact layouts), 6 (links navigate away), 7 (drum hidden), 8 (texture
  speckle), 12 (readouts before markers are set) and 13 (Wave cutaway size).

<!-- end part -->

<!-- part: refine/play.md -->

### Play lens: living-earth (Curiosity No. 04)

Played cold twice: as a grade 6 student alone at home (anchor MS-ESS2-3), and as a teacher projecting it at 1366x768.
Frames are in `S:/CurioClass-codex-scratch/living-earth/play/` (r1 to r4) plus the shared audit
`S:/CurioClass-codex-scratch/living-earth/audit-r1/`. Chrome on port 9781, started and closed by drive.py.

#### Short test (Curiosity)

- **Would a kid open it unassigned?** Yes. Play draws the Ring of Fire out of 26,230 real quakes in 18.7 s
  (measured), the dots bloom, the year and count tick up (r1/play-6s.png, r1/play-end.png). It is a real "whoa".
- **Would an adult play with it for fun?** Yes. The slices are the best thing here: Japan shows the slab dipping
  west to 560 km (r1/slice-japan.png), Peru-Chile to 600 km (r1/slice-peru.png), the Mid-Atlantic only 13 quakes
  at no more than 20 km (r1/slice-atlantic.png), Tonga down to 700 km. Three Stations circles meeting 10 km from the
  2004 epicentre is a real payoff (r2/st-solved.png).
- **Is the real thing the interface?** Yes: real catalogue, real relief, real sections.
- **Does it work with no finish line?** Yes. No score, goal, level, sticker, quiz or finish screen anywhere
  (checked src, Manual, every panel). The Stations OFFSET is a distance readout.

Short test passes. Mean frame 16.7 ms over the full play run with every dot (headless, r1 play-end-read).

#### Findings

##### Should fix

1. **Stations: dragging on the trace can never set the S marker.** src.html:1945-1948. Both markers start at 0 s, and
   a press picks the nearer marker, so a press at the S packet always moves P (S stays at 0 because |t-P| < |t|
   whenever t > P/2). Shown with real mouse input on Sumatra 2004, station A: press at the true S (990.8 s) left
   P = 997.5, S = 0, readout "S−P -997.5 s", with or without P set first (r2/st-drag-S-first.png,
   r2/st-drag-S-afterP.png). Only Shift-drag or the small sliders reach S, and a phone has no Shift. This is the
   tool's main hands-on measurement. Better: start S at the right end (or hide each marker until placed), and let a
   press choose by which packet it is nearer, or give each marker its own grab handle on the trace.
   family:curiosity.
2. **The first-run hint is spoken after the action it asks for, and in the wrong place.** src.html:745-746.
   `touch()` speaks "Drag to spin. Press play." on the first action, whatever it was. Voice log, held clicks:
   after Play it says "Press play" while the archive runs (r3 v-first-play); after the Slice tab it says
   "Drag to spin" where a drag now draws a section line (r3 v-first-slice); after a drag it says "Drag to spin"
   (r3 v-first-drag). The on-screen hint is hidden at the same moment, so the voice and screen disagree.
   Better: if the first action already spun or played, say nothing (or only the half not yet done); never say it once
   a tool is open. family:curiosity (any Curiosity whose hint can only be voiced after the first gesture).
3. **Stations caption never moves on.** src.html:475 and the readout line. The panel keeps saying
   "Tap three stations" after three are placed, struck and solved (r2/st-solved.png), and the readout shows
   "FIT AMBIGUOUS" before anything has been measured (audit state-stations-1366x768.png), which reads like an error.
   It is a five-step procedure (place three, Strike, set six markers across three channels, Circles, Reveal) with no
   word on screen about the next one. Better: one short instrument-style line that follows the state ("Strike to
   record a quake", "Set P and S on each station", "Circles"), and no FIT text until Reveal. POLISH "words match the
   state". general.
4. **The quake record card covers the globe when a tool is open.** The card sits at the left edge (x 25 to 250) and
   the globe moves left to make room for the tool panel, so the card covers the west of the globe: in Stations the
   catalogue circles and station B run under the card text (r2/st-solved.png; audit state-stations-1366x768.png).
   Same at 680x425 and 800x500 with no tool open (audit state-selected-680x425.png). Better: dock the record inside the
   tool panel when one is open, or move it above the drum. general.
5. **The Manual is written for adults.** src.html:550-603. "Normalized three-plane fit", "finite rotations are
   resolved through the published plate circuit relative to plate 000 ... quaternion interpolation", "palaeomagnetic
   reference frame", "Pn and far-side PKP/PKIKP". The grade band is 4 to 12 and the anchor is grade 6; a student who
   opens the drawer to learn how Stations works will not get through it. The panel captions carry the same register
   ("±150 km swath · quake depths 1:1 · surface relief ×20", "schematic older fossil evidence · modern overlays
   withheld", "0–5 Ma average, in its own reference frame"). Better: each Manual section opens with two plain
   sentences a grade 6 student can follow (what to do, what you will see), with the precise honesty notes kept
   below them. "Things people have found" also opens with two paragraphs of instructions ("Change only the depth
   floor and compare the patterns"); the brief wants short findings read after the fact. family:curiosity.

##### Polish

6. **The globe stops turning the moment Play is pressed.** src.html:1344 (`!state.touched`). The first play run
   shows only the West Pacific (r1/play-end.png), so "the thin line down the middle of the Atlantic" in the spec's
   first reaction never appears unless the student thinks to drag. Better: keep the slow turn during play until the
   student drags. general.
7. **Wave gives its finding away and the globe source does not matter.** The cutaway prints the violet "S SHADOW"
   arc and the readout says "S SHADOW" before Fire is pressed (audit state-wave-1366x768.png), and since the cutaway
   always puts the source on top, tapping a new source changes nothing in it (the Manual says so). The disc is about
   135 px across in a 390 px box at 1366x768 (r1/wave-end.png), so the 25-minute ray fan is crowded. Better: reveal
   the shadow label only after the rays have reached the far side, draw the receiver on the globe along a great
   circle from the source, and give the cutaway the room. family:curiosity.
8. **Rewind can only be dragged.** The big Play pad is disabled in Rewind (r1/rewind-200-atlantic.png). "Watch the
   fossil belts join up" wants a run from 0 to 200 Ma on the same pad. family:curiosity.
9. **Stations makes the student switch channels with a select.** Three stations, six markers, one trace at a time
   behind a dropdown; tapping a station triangle on the globe does nothing. A real record section stacks the three
   traces. Better: stack A, B and C (each short) or let a tap on a triangle choose its trace. On 375x812 the P and S
   sliders are about 80 px for 1,500 s (about 19 s per pixel, roughly 150 km of distance), too coarse to land a
   circle (audit state-stations-375x812.png). family:curiosity.
10. **Motion arrows are hard to read.** One small cyan arrow per plate at its centroid, under the dots
    (r1/layers-hawaii.png); "find two plates heading straight at each other" is hard to do. Better: a few arrows
    along each plate near its edges, drawn above the dots. general.
11. **Calm mode skips the wave.** Fire with Motion off jumps straight to 25:00 (src.html:1223). Year playback in calm
    steps by years and keeps time (r2/calm-play.png); Wave should step too (POLISH, calm keeps time). general.
12. **Preview size (680x425) instruments are too small to use.** The section is about 40 px tall and its "A" label
    prints over "2009 km → B" (r2/preview-680-slice.png); the station trace is about 50 px (r2/preview-680-stations.png);
    layer buttons shrink to Q V P F A with no word for Relief or Arrows; the depth faders lose the word DEPTH
    (audit size-680x425.png). Better: give the open panel the globe's room at this size, or stack. general.
13. **Read reads stiffly.** "1974. 2252 earthquakes in the magnitude 5.5 and greater catalogue under these filters."
    (r3 v-read-after-play). Better: "1974. 2,252 earthquakes of magnitude 5.5 or more so far." general.
14. **"OUTSIDE FILTERS" on the revealed Stations quake.** At the default year 1970 every revealed quake is labelled
    OUTSIDE FILTERS (r2/st-solved.png), which reads as an error at the payoff moment. Better: drop the tag on a
    Reveal, or move the year to the event as the catalogue list already does. general.

##### Nit

15. At load the time dial says 1970 and QUAKES 0 (state.year 1970.0), but dragging the dial back to 1970 shows 1970's
    quakes (year + .999). Read at load says "0 earthquakes". src.html:677 versus 1189. general.
16. The Tibetan Plateau reads as a white hatched patch at 1x (moire in the shaded relief), visible on every default
    frame; fine at 4x (r1/zoom6-tibet.png). general.
17. Strike always starts at Sumatra 2004 and cycles the same fixed order. A random start would make the second visit
    fresh. family:curiosity.
18. Pin at Honolulu names its nearest volcano "Unnamed · 105 km" (r1/pin-hawaii.png). general.

##### For the Teaching lens (not judged here)

- Pin SPEED reads 6.2 cm/yr for Denver and 9.3 cm/yr at 264° for Honolulu (r1 pin-denver, pin-hawaii). These are the
  Merdith model's 0 to 5 Ma palaeomagnetic-frame average, as the Manual says, but a student will read them as how fast
  their ground moves now, and they are well above the usual present-day figures for North America. Worth a check
  against "a readout that misleads is a blocker".
- Nothing cultural or Native here. The Strike list names deadly events (2004 Sumatra, 2011 Tohoku, 2015 Nepal) by
  place only, with no tolls, as the spec asks; no sensitivity review needed in my view.

#### Frames looked at

Audit: size-* (all nine), state-selected/slice/stations/wave/rewind/pin/manual at 1366x768, state-stations and
state-stations-cleared and state-wave at 375x812, state-slice 680x425, calm-1366x768.
Mine: r1 first-0s, play-6s, play-end, japan-deep300, slice-japan, slice-peru, slice-atlantic, mag8, mag8-select,
layers-hawaii, zoom6-hawaii, zoom6-tibet, rewind-100-atlantic, rewind-200-atlantic, pin-denver, wave-end; r2
st-drag-S-first, st-drag-S-afterP, st-solved, narrow-760-slice, preview-680-slice, preview-680-stations, calm-play;
r3 voice logs (first tap by Play, Slice, drag, Read; Play x5; Sound off and on).

#### Audit pilot

- **Confirmed:** the record card over the globe at 680x425 and 800x500 (finding 4; it also happens at 1366x768 with a
  tool open, which the audit listed only inside the "overlap: #globe" block); the tool-tab "how line cut (hush)" rows
  point at the same wrong first-hint line as finding 2.
- **Wrong:** every "overlap: #globe" row (the globe canvas is the full-bleed stage, every overlay sits on it by
  design; about 400 of the 523 rows); "hint out of view" in every state (the hint is meant to be gone after the first
  action); Manual "keep region covered" rows (the Manual is a modal dialog); the marker label overlaps in
  stations and stations-cleared at small sizes (the labels sit above the sliders and read, see audit
  state-stations-cleared-375x812.png).
- **Missed:** the Stations drag that cannot set S (finding 1), the first hint spoken after its action (2), the
  stuck Stations caption (3), Manual and caption reading level (5), the globe stopping on Play (6), the Wave
  shadow labelled before Fire (7), calm Wave jumping to the end (11), Read wording (13).

<!-- end part -->

<!-- part: refine/teaching.md -->

### Teaching lens: living-earth (Curiosity No. 04), round 1

Cold lens, judged against CODEX-CURIOSITY.md, VISION.md "Curiosities: the second shape", BASELINE and the spec.
Bundle as built (1,957,170 bytes). My frames and checks: `S:/CurioClass-codex-scratch/living-earth/teaching/out/`
(numbers saved beside them as facts.json, numbers.json, nums2.json, rot.json). Shared audit:
`S:/CurioClass-codex-scratch/living-earth/audit-r1/`.

Counts: 1 blocker, 4 should fix, 4 polish, 5 nits.

#### Blocker

**B1. Pin SPEED and the Arrows layer report a reference-frame drift, not how fast the plate moves.**
- Where: src.html:1660-1669 (`plateMotion`), Pin readout 1695-1696, Read text 1175, Arrows 1797-1806; spec "Things to
  do" 10 and 11.
- What: the speed and heading come from Merdith et al. 2021's 0-5 Ma rotation relative to plate 000, its absolute
  (palaeomagnetic) frame. That frame carries a large common rotation shared by every plate: North America, Africa and
  Australia all turn 2.3 to 3.0 degrees in 5 Myr about nearly the same axis, and each 10 Ma sample is exactly twice the
  5 Ma one. The readout is dominated by that drift. Against ITRF2014 plate motion poles (Altamimi et al. 2017,
  recomputed in Python):

  | Pin | Tool | ITRF2014 (GPS) |
  |---|---|---|
  | Denver, North America | 6.2 cm/yr, 253 deg | 1.6 cm/yr, 247 deg |
  | Sydney, Australia | 2.8 cm/yr, 325 deg | 5.7 cm/yr, 19 deg |
  | Perth, Australia | 4.5 cm/yr, 356 deg | 6.9 cm/yr, 34 deg |
  | London, Eurasia | 5.3 cm/yr, 0 deg | 2.4 cm/yr, 46 deg |
  | Cairo, Africa | 5.5 cm/yr, 12 deg | 2.9 cm/yr, 53 deg |
  | Lima, South America | 2.9 cm/yr, 309 deg | 1.1 cm/yr, 345 deg |
  | Honolulu, Pacific | 9.3 cm/yr, 264 deg | 7.1 cm/yr, 299 deg |

  Australia, the fastest-moving continent, reads slower than North America, and in the wrong direction. Africa reads
  5.5 cm/yr due north. A student doing "Pin your town and read how fast your plate moves" gets a number two to four
  times off any textbook or GPS figure, and the Arrows layer (frame atlantic-all.png, pin-sydney.png) shows Africa and
  most plates drifting north or west together, which hides the relative motion "two plates heading at each other" is
  meant to show. The small instrument note ("motion is the model's 0-5 Ma average, in its own reference frame") is
  true but cannot rescue a grade 6 reader; REFINE: an estimate that misleads when its assumption does not hold is a
  blocker.
- How seen: numbers.json, nums2.json and rot.json (pinData and plateMotion run in the page), ITRF2014 comparison
  computed in Python; frames pin-sydney.png, atlantic-all.png.
- Better: keep Merdith for Rewind (its job), but take present-day motion from a present-day plate motion model in a
  no-net-rotation frame (ITRF2014-PMM or MORVEL/NNR-MORVEL56; check the licence), or at least remove the common
  rotation and show motion relative to the neighbouring plate across the nearest edge (opening or closing, cm/yr),
  which is what a seismologist and MS-ESS2-3 care about. Re-check the fingernail field note against what the readout
  then shows.
- Tag: family:curiosity (a model chosen for one instrument reused for a readout it was not built for).

#### Should fix

**S1. Slice draws the sea floor below the shallow earthquakes, so ridge and trench quakes look like they sit in the
water.**
- Where: src.html:974-985 (`renderSection`).
- What: quake depths are plotted at true scale below sea level, but the ETOPO profile is multiplied by 20 on the same
  axis, so a 4 to 5 km deep sea floor is drawn at 80 to 100 km. In the Mid-Atlantic section every quake (10 to 20 km)
  sits above the sea-floor line; in the Japan section the shallow cluster floats above the drawn ocean floor. The note
  "surface relief x20" is there, but the picture says the opposite of the lesson (quakes happen in rock, under the
  ridge).
- How seen: slice-mar.png, slice-japan.png, slice-peru.png (my own; the Peru-Chile and Japan sections otherwise show
  the dipping slab well, Done-when 2 Slice passes).
- Better: draw the exaggerated profile in its own strip above the 0 km line (or exaggerate only above a sea-level
  baseline), or plot quakes below the local surface. Say "sea floor" and "sea level" on the section.
- Tag: family:curiosity.

**S2. Wave and Stations disagree with their own 104 degree shadow between 99 and 104 degrees.**
- Where: src.html:735-742 (`arrival`), 1104-1106, 1096 (shadow arc), 936 (globe ring at 104 deg); Manual "Wave".
- What: the bundled iasp91 table has direct P only to 98 deg and direct S only to 99 deg. From 99 to 104 deg the
  readout says "P NO BRANCH · S NO BRANCH" while the receiver dot sits outside the drawn "S SHADOW" arc and inside the
  globe ring. From 104 to 140 deg P says SHADOW; past 140 P returns. So the instrument shows three different shadow
  edges and the words "NO BRANCH" are not explained in plain language. Also S at 98 to 99 deg arrives at 25:06 to
  25:14, past the 25:00 end of both the elapsed fader and the station trace, so it can never be reached or marked.
- How seen: nums2.json (`arrival` at 94 to 106 and 136 to 142 deg), wave-100.png.
- Better: draw the shadow from the table's real edges (about 99 deg for direct S, 98 to 140 deg for direct P), say in
  the Manual that waves bend round the core there (diffracted waves, left out), and replace "NO BRANCH" with words a
  student can read ("no direct wave arrives here"). Extend the window to 26 min or say why it stops.
- Tag: family:curiosity.

**S3. The words are written for a geophysicist, not a grade 4 to 8 student alone at home.**
- Where: Manual (src.html:550-664) and on-screen notes 459, 475, 490, 499, 507, readouts "NO BRANCH", "UNRESOLVED
  MODEL AREA", "QUAKES HELD", "FIT AMBIGUOUS".
- What: examples a grade 6 reader meets: "Finite rotations are resolved through the published plate circuit relative
  to plate 000, sampled every 5 Ma, with quaternion interpolation between samples"; "The normalized three-plane fit
  must agree with every measured circle within 200 km"; "schematic older fossil evidence · modern overlays withheld";
  "motion is the model's 0-5 Ma average, in its own reference frame"; "Tap three stations · drawn model traces · surface
  focus · iasp91". The honesty is right; the reading level is not (REFINE teaching 5, rule 4). The Manual also has no
  short plain "how to read this" line before the detail for each instrument.
- How seen: reading src.html and the frames (state-*-1366x768.png in the audit, my slice/wave/pin frames).
- Better: for each Manual section, lead with one or two plain sentences at about grade 6 ("Each dot is a real
  earthquake. Bigger dot, bigger quake. Colour shows how deep it was."), then keep the technical honesty notes under
  a "For the curious" line. Plain on-screen notes ("Rays bend through a model Earth. Arrival times from a standard
  model."). Explain S-P in one sentence where the markers are.
- Tag: general.

**S4. science-9-orbits-and-earth-s-history (HS-ESS1-5) is listed as reached, but nothing lets a student see the ages
of crustal rocks.**
- Where: spec "Map"; module codes in data/modules.csv (HS-ESS1-4; HS-ESS1-5; HS-ESS1-6).
- What: HS-ESS1-5 is about using plate motions to explain the ages of crustal rocks (sea floor older away from
  ridges). The tool has relief, quakes, a reconstruction and a model speed, but no rock or sea-floor age anywhere. The
  anchor MS-ESS2-3 is exercised by doing (fossil and mountain belts and continent shapes in Rewind, ridges and trenches
  in relief and Slice; its boundary excludes palaeomagnetic anomalies), and 4-ESS2-2 is exercised well (frames
  pacific-all.png, tonga-deep.png, hawaii.png). MS-ESS3-2 is touched only as "where quakes cluster"; the Manual
  rightly refuses forecasting, which is the code's verb, so it is thin but honest.
- Better: add a sea-floor age layer (an ocean age grid such as Seton et al. 2020, CC BY 4.0 at source, to be
  verified), readable by Pin and visible along a Slice, which also gives Hawaii's chain and the Atlantic opening real
  numbers. Otherwise drop science-9 from "Also reaches" (rule 2: never a thin activity to make a code honest).
- Tag: general.

#### Polish

**P1. "Find Hawaii ... follow the chain of older islands to the northwest" (spec Things to do 12) has nothing on screen
that says older.** The chain and the Emperor bend are visible in relief (hawaii.png), but ages live only in the Manual
field note. A sea-floor or volcano age readout (see S4) would let the student find it. family:curiosity.

**P2. "Compare the visible-quake count around the Pacific rim with the rest of the world" (Things to do 13) cannot be
done.** QUAKES counts the whole sphere; the only local count is Pin's 300 km circle. The Manual itself says the 81
percent figure is not measured from the display. A hemisphere or "within the globe's view" count, or a count inside
the Edges layer's Pacific plates, would turn the field note into something the student can check. family:curiosity.

**P3. Teacher notes do not name the sensitive side.** The M8+ catalog and Strike name real deadly events (2004
Sumatra, 2011 Tohoku, 2008 Sichuan, 2015 Nepal, 2023 Kahramanmaras). Showing them as data is right (spec), but
notes.md should carry a one-line content note that some students or families may have lived through these (rule 8).
Two Support at home ideas are weak: "Ask a family member what a map leaves out" is vague and the string one needs a
paper map most homes lack; something like "find your town on the globe, pin it, and look up the last quake felt there
together" is doable tonight. Not a cultural or Native item: no sensitivity agent needed. general.

**P4. Rewind shows the answer, never the test.** The dial runs the model; the student cannot try fitting South America
to Africa themselves and then compare with the model, which is the evidence-reasoning MS-ESS2-3 asks for and what
Wegener did. A "drag a continent" fit before or beside the model would add depth without a score. Rewind itself
passes Done-when 2 (rewind-200-satl.png, rewind-200-gond.png, rewind-200-laur.png: fossil belts and the
Appalachian-Caledonian traces line up at 200 Ma; rewind-100.png shows a narrow Atlantic). family:curiosity.

#### Nits

- **N1.** On load the top strip reads YEAR 1970, QUAKES 0 and the TIME fader shows 1970; moving the fader to 1970 gives
  475 quakes (the Manual says the fader includes the chosen year). Same dial position, two counts. src.html:677, 750,
  1189.
- **N2.** 525 ComCat place names contain a literal "?" for a lost diacritic ("17 km NW of Bhach?u, India", "K?h
  Sef?d, Iran"). Checked: ComCat's API returns the same, so it is faithful, but on screen it reads as broken.
- **N3.** Strike always starts with 2004 Sumatra and cycles in a fixed order; a returning student knows the answer
  before Reveal.
- **N4.** Pin plate names follow the 0.1 degree model: Reykjavik reads Eurasia (it sits on the North American side of
  the rift; "boundary area" is shown, so not a lie). Honolulu's and Mumbai's nearest volcano read "Unnamed".
- **N5.** In Rewind the depth legend (DEPTH / km) stays on screen though dots are withheld.

#### Done when (teaching items)

1. Opens to the globe, no welcome; play 1970 to 2025 at the default 3 yr/s is 18.7 s. PASS (src.html:674, 1338).
2. Slice Wadati-Benioff under Japan and Peru PASS (slice-japan.png, slice-peru.png). Stations with markers on the drawn
   arrivals: offset 6 km for all 20 Strike events (numbers.json). PASS. Wave S shadow: PASS with S2. Rewind to 200 Ma
   PASS. Pin gives plate, speed, nearest volcano: works, but the speed fails B1.
3. Every number traced: 14 quakes checked against the live ComCat API by event id (Nepal 2015, Kahramanmaras 2023,
   Loma Prieta, Northridge, Bhuj, Sichuan, Tohoku, Sumatra, Bolivia 1994 deep, Kamchatka 2025, Chimbote 1970, Okhotsk
   2013, Fiji 2018, Tangshan): date, magnitude, position (0.01 deg) and depth all match. Total 26,230 matches ComCat's
   count for M5.5+, eventtype=earthquake, 1970 to 2025 exactly; per-year counts for 1970, 1990, 2011 and 2025 match
   (475, 522, 714, 514); 44 M8+ events match ComCat's 44. iasp91 times (P 30 deg 6:10, P 90 deg 13:01, S 90 deg
   23:56), PREM core radii (3480 and 1221.5 km) and the S-P to distance inversion (100 s to 967 km) are right. Plate
   speeds FAIL (B1). Field notes (M9.5 Chile 22 May 1960, 81 percent Pacific rim, Lehmann 1936, about 2.5 cm/yr
   Atlantic, Tonga near 700 km: bundled deepest is 700 km, Fiji 1985) agree with their cited USGS pages.
4. Sources and licences are in the Manual and tool.draft.json. PASS (licences not re-verified by me beyond the
   records cited).
10. No score, goal, level, sticker or finish; the Stations offset is a distance. PASS (lesson creep grep clean).

Giveaways: Strike hides the event until Reveal (src.html:1068); Circles use the student's own markers. Fine apart from
N3.

#### Audit pilot

- Leads confirmed: none of the 523 is a teaching problem. The "keep region" and "text hidden" leads on #marker-p-out
  and #marker-s-out at 680x425, 800x500 and 375x812 are real in the sense that the values sit over the range inputs
  (state-stations-680x425.png), but they stay readable there.
- Leads wrong (grouped by cause): 460 "overlap" rows are the full-bleed #globe canvas under its own overlays (legend,
  hint, position, toolbelt, event list): by design. The 7 "hint out of view" rows are wrong: the hint is plainly on
  screen at 1366x768 (size-1366x768.png). The 45 "text hidden" rows in the manual state are the modal Manual dialog
  covering the station, as it should. The 4 "keep region" rows for #play, #manual, .maker and .power are the same
  modal.
- What it missed (it cannot judge these): B1 plate speeds two to four times off and in the wrong direction; S1 sea
  floor drawn below the quakes; S2 the three different shadow edges and the unreachable S arrival at 98 to 99 deg;
  S3 reading level; S4 the unexercised HS-ESS1-5; N1 the 0 versus 475 count at the same dial position; N2 the "?"
  place names.

<!-- end part -->

## Fix

<!-- part: polish.md -->

### Polish: living-earth (Codex fix, round 1)

Evidence paths below are relative to `_scratch/living-earth/`. The bundle is `tools/living-earth/living-earth.html`. All blocker and should-fix causes were reproduced before editing. No changes were made to `refine.md`, its review folder, the packed material, the kit, or other tools. No commits were made.

#### Blocker

1. **FIXED: plate reference-frame drift.** Removed the area-weighted shared rotation from the original Merdith 0-5 Ma angular velocities, using a 5-degree surface grid and its full inertia tensor. Resolved coverage is 99.811%. Denver changes from 6.2 cm/yr at 253° to 1.6 at 247°; Sydney from 2.8 at 325° to 5.9 at 17°. All five supplied ITRF2014 comparisons pass, with maximum errors 0.28 cm/yr and 5.45°. Pin adds relative normal EDGE MOTION; the equatorial Atlantic example opens at 3.3 cm/yr. Arrows use the same corrected motion. The fingernail note now describes a few centimetres per year and distinguishes relative spreading. Proof: `fix-before/motion.png`, `fix-after/motion.png`, `fix-after-motion.json`, `fix-independent-numbers.json`; reproducible derivation in `fix_nnr.js`. Merdith is retained for Rewind; no replacement model was introduced.

#### Should fix

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

#### Polish accepted

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

#### Settled calls

- **Applied: Curiosity shape.** No welcome screen, goal, score, level, quiz, finish screen or kit header was added. The short first-run hint is the only automatic narration. The engraved plate and lower-left Manual remain.
- **Applied: audit interpretation.** Full-stage canvas intersections, the dismissed hint and controls behind the open Manual are intentional. The genuine compact geometry leads were fixed and checked separately.
- **Applied: sensitivity.** No sensitivity agent was added. Disasters stay observations; the teacher-notes content paragraph is present.
- **Applied: Wave finding.** There is no question or “found it” moment. The shadow and its text appear with the travelling fronts.
- **Applied: Stations.** Status is a short instrument readout, with no FIT verdict or threshold label. Offset remains kilometres.
- **Applied: retained material.** Merdith Rewind, the M5.5 floor and explanation, original ComCat names, place-only event naming and technical honesty notes remain. Findings' instructional prose moved into how-to sections. Tag counts did not change the scope.
- **Unattended choices.** Used the successful NNR route, end-of-1970 initialization, random first Strike and stacked portrait panels. The spec's open questions were left unchanged; no age layer, continent-fitting activity, replacement motion model or stacked record section was added.

#### Cheats tried

There is no score to pass. The probes target false measurements instead. In `fix-native-results.json`:

- Circles and Reveal with untouched markers: all radii null, no intersection; status asks for P and S.
- Equal P/S markers at all three distinct stations: no intersection.
- S before P: negative gaps give null radii and no intersection.
- Three coincident stations: no unique intersection.
- Clear after Reveal: selected=-1, reveal=false, station count=0, record hidden.
- Calibrated markers on three drawn arrivals: 8 km catalog offset. It is a distance, with no passing label or colour change.

#### Voice walk

Held 120 ms native clicks at 2 s pacing: Play speaks “Drag to spin.” once; another Play and later layer actions do not repeat it. A separate fresh native drag speaks “Press play.” once. A fresh Slice action speaks nothing. Read speaks current measurements and stops stale speech. Audit five-click and two-quick-tap checks are clean for Play and Read. `voice/lines.json` equals `allLines()`: exactly two fixed lines, in the same order. The browser voice fallback is used; the bundler explicitly reports that recordings are absent. Proof: `fix-after-voice-*.json`, `fix-native-results.json`, `fix-audit/audit.md`, `fix-wave-timing-0.json`.

#### Engine changes wanted

Deferred shared-kit request only: `kit/curio.js`, `showMotion()`, could offer plain Motion / Motion off wording without the emoji on engraved instrument panels. Logged in `handoff.md`; no kit edit was made.

#### Audit

The single full audit completed within its 2400 s limit, on Chrome 9911 and host 8715. It produced 73 frames and 736 mechanical leads. All were classified in `fix-audit-triage.json`:

- 551 full-stage canvas intersections, 7 dismissed-hint rows and 35 Manual-modal rows are the settled intentional cases.
- 16 joined-depth-track hit-test rows are intentional; both actual thumbs were pointer-dragged successfully.
- 5 record/dock and 10 marker/parent rows are ancestor hit-test findings; the text is visible on the corresponding frames.
- 109 small-target rows were fixed with 44 px compact tabs and catalog selection. The 2 Close overlaps were fixed with a 48 px button and 12 px clearance. The 1 clipped-S row was fixed with stretched marker rows. After Reveal at 680x425, the S input ends 4 px inside the panel. Proof: `fix-audit-followup-*.json`, `fix-audit-followup/`, `fix-phone/`.

Motion off and resize stress checks are clean: no exceptions or controls left disabled. The native walk records zero HTTP requests and zero runtime exceptions. Every final drive batch reports zero browser errors. The local phone server occasionally logs ConnectionResetError when muted Chrome is killed during cleanup; that occurs after successful shots and is not a tool exception. The full audit was not repeated. Only the confirmed geometry leads, compact Pin readability and Wave's finding timing received scoped follow-up shots.

#### The real material

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

#### Frames looked at

Before frames: all 17 in `fix-before/`, plus the paired before performance frame. After and regression frames: `fix-after/`, `fix-final/`, `fix-final-targets/`, `fix-verified/`, `fix-breakpoint/`, `fix-audit-followup/`, `fix-delivery/`, `fix-pointer/`, `fix-wave-timing/`, and the 375x812 iframe frames in `fix-phone/`. All 73 audit frames were examined through labelled contact pages `fix-contacts/audit-01.png` to `audit-10.png`, with confirmed leads also opened at full size. Remaining iteration frames were examined in `fix-contacts/checks-01.png` to `checks-04.png`. The four permitted model tools were opened and compared in `fix-models/`; the globe, actual data and scientific controls remain central.

#### Left open

- A physical school Chromebook and physical touch hardware were unavailable. The muted Chrome, native pointer/keyboard, 4x CPU and phone-iframe evidence is stated above. The all-layer benchmark has a 16.7 ms median and 20.2 ms mean, so sustained 60 fps across hardware remains unverified.
- Fixed narration recordings are still absent; the two correct hint halves use the existing browser-voice fallback.
- The deferred shared-kit wording and the spec's open questions remain with the owner. No blocker or should-fix item from this list remains open in the tested states.

Final byte counts, protected hashes, contrast ratios and closed test ports are recorded in `fix-final-manifest.json`. The source lesson-creep scan contains only scientific “sea level” and geometric point variables/GL.POINTS; no lesson outcome or reward UI was introduced.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Living Earth build handoff

#### Structure
The first build's spherical geometry, great-circle sections, station intersection, input handling, drum and family marks remain in src.html. The second build adds a WebGL material surface with a bounded canvas fallback, full M5.5 catalogue, geography, city search, model plate readouts and Rewind. material.json is the only data file and is embedded by bundle_tool.py.

#### Reproduce the real material
All second-build raw downloads are in _scratch/living-earth/data/build2/ with source URL, date, checksum and download duration beside them. build2_fetch.py and the sources/more/taup/spotcheck batch scripts retrieve them with limits. build2_plates.py resolves the original GPML and finite rotation circuit. build2_pack.py produces the compressed material and code-shaded relief PNG. The final texture conversion is build2_texture72.py, texture72.html and build2-texture72.json, using Chrome at WebP quality 0.72; its saved data URL is data/build2/texture-webp.json. Run pack again to embed that result. The packer preserves this cached texture when present. build2_patch.py preserves the first source and assembles build2_renderer.js and build2_instruments.js with its substitutions. Editing src.html directly is fine; do not re-run assembly afterward without carrying edits back to its Scratch inputs.

#### Numerical conventions
Spherical Earth radius 6371 km. Dates are UTC days; the selected year includes its whole calendar year. Catalogue playback progresses continuously; Motion off updates in year steps. Local pin history is independent of current filters. Quake depths stay true in sections; ETOPO surface relief alone is x20.
TauP-calculated iasp91 times replace the first build's uncalibrated shell table. PREM paths replace its iasp91 paths. They are numerical model outputs, not bundled software. Stations remain a surface-focus idealization with synthetic traces and shallow real catalogue epicentres.
Merdith finite rotations are recursively composed relative to plate 000, sampled each 5 Ma, then slerped in the browser. Present plate polygons are simplified resolved topologies. Some small polygons reference absent archive features; those places remain unknown. The manifest records every omitted reference and join. The model's motion frame and hotspot exclusion must remain visible.

#### Sensitivity
Real earthquakes are presented as observations, without tolls, gore, disaster photography or ratings. A local event count is not hazard guidance. No location or student data is transmitted.

#### Validation
Second-build evidence is prefixed build2 in Scratch. build2-numbers-final.json has 38 numerical probes; data/build2/spot-checks.json has ten fresh ComCat checks. build2-performance-final contains the 4x CPU pointer profile and playback measurement. build2-explore records two ten-minute builder walks. build2-audit/audit.md is the single full audit, with build2-audit-triage.json recording its dispositions. build2-after-audit and build2-verified-targets contain the affected layout follow-ups. build2-keyboard-last-retry contains the last native keyboard inspection. build2-final-manifest.json freezes hashes, sizes and evidence paths. codex-report.md records results and limitations; codex-report-1.md is preserved unchanged.

#### Engine changes wanted
Log only, not implemented: `kit/curio.js`, `showMotion()`, could offer plain `Motion` and `Motion off` text without the emoji for engraved instrument panels. This is the Refine's deferred shared-kit request. Kit, scripts, docs and other tools were not edited; no commits or deployment were made.

#### Cold review changes, 2026-11-05
The review preserves the scientific pack and renderer. Station Clear and marker edits now remove stale labels and revealed records, and clearing during a pointer drag is guarded. The trace has a five-minute ruler and a taller compact layout. Phone panels retain an unobscured globe, working Close controls and readable measurement plots.
Read expands section, station and wave units into sentences, announces out-of-filter selections and stops on instrument switches. Keyboard centre placement keeps the result announcement. A new Wave source waits for Fire. The canvas fallback now honors Relief off.
Independent evidence uses the review-* and cold-* prefixes in Scratch: ten fresh ComCat checks, primary licence responses, numerical before/after probes, native range endpoints, voice logs, size frames and performance. The existing build2 evidence is historical builder evidence. Do not rerun build2 assembly over the reviewed source.

City search ranks an exact town name before partial matches: Lima now selects Lima rather than the earlier substring match Quelimane. Accent folding and the limited offline gazetteer remain.

Rewind fossil regions now have a solid Glossopteris outline and dashed Mesosaurus outline, with the latter drawn above broad regions. This retains the existing schematic data while adding a non-colour key.

#### Refine fixes, round 1, 2026-11-05
The original `material.json` pack is unchanged. Present-day motion now removes the surface-area-weighted shared rotation from the original 0-5 Ma angular velocities. `_scratch/living-earth/fix_nnr.js` reproduces the correction by integrating `(I - r r^T) omega` over a cosine-weighted 5 degree grid of the model's own polygons, covering 99.811 percent of the sphere. `fix-independent-numbers.json` independently checks all five cities against the Refine's ITRF2014 comparison, with maximum errors 0.28 cm/year and 5.45 degrees. This is still a model average, not GPS. EDGE MOTION is the normal component of relative motion at the nearest plate edge; the shared rotation cancels in that difference. Rewind still uses the original finite rotations. Do not rerun the older source assembly over these changes.

Stations keeps independent P/S placement flags and separate trace handles; S starts at the end of the 26-minute ruler. No inferred circle or intersection uses an unplaced marker. Catalog records dock above the active instrument; offsets remain measurements with no fit verdict. The sea-floor profile has its own strip and scale derived from its actual sampled range; its vertical exaggeration is exactly twenty relative to horizontal kilometres. Quake axes remain 1:1. Wave's ring, shadow arc and readouts use the bundled direct-branch edges (P 98, S 99, far-side P 140 degrees) and a 1560 second window. The Manual explains the difference from the usual 104 degree textbook shadow and the omitted diffraction.

Volcanoes are one WebGL triangle point layer, with one batched canvas path as the fallback. Immutable shader locations and motion-arrow vectors are cached. The same paired 4x CPU benchmark at 1366x768 changes the volcano median frame interval from 33.4 ms to 16.7 ms. Occasional slower frames remain; a sustained 60 fps hardware claim is not established. The NNR arrows are drawn above the quake layer at several sites near each large plate's edge.

The first native Play speaks only `Drag to spin.`; the first drag speaks only `Press play.`; an instrument switch stays silent. Both lines have validity checks and match `voice/lines.json`. Read uses plain speech. Compact layouts retain names, depth labels and a 40 px drum; phone evidence uses a 375x812 iframe on host port 8715. Rewind now plays both directions, and calm Wave advances by whole minutes at the same pace as full motion. The family maker's plate, Manual drawer and power panel remain; there is no lesson flow, score, goal or finish.

All fix scripts, before/after frames, native-input probes, source metadata and the final audit are under `_scratch/living-earth/` with the `fix-` prefix. `polish.md` is the item-by-item disposition. `refine.md` and its review folder were not changed.

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
- 2026-11-25: earlier round codex-report-1.md moved to S:/CurioClass-archive/tool-rounds-2026-11-25/living-earth

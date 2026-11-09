# Codex report: living-earth (Curiosity No. 04)

## Built

Second build, Cory's 2026-11-05 decision. The instrument opens directly on its globe and runs entirely from `living-earth.html`.
Changed from the first build: replaced the eleven-event demonstration with 26,230 real M5.5+ ComCat earthquakes; added ETOPO relief and section heights, Natural Earth coasts and cities, NOAA volcanoes, licensed plate geometry and finite rotations, every geographic layer, city search, plate/volcano measurements and Rewind to 200 Ma.
Also replaced the uncalibrated arrival table with TauP-calculated iasp91 values and the cutaway paths with PREM numerical paths. Fixed compact panels, end-of-playback counts, inconsistent station-circle fits, readable Pin narration and keyboard inspection of ordinary earthquake dots.
Kept the first build's spherical geometry, great-circle sections, synthetic station traces, station intersection, drum, brass controls and family marks. Maker's plate and Manual remain lower-left; Motion, Sound and Read have their own power panel.
No welcome, lesson route, mode pills, game structure or finish screen. Five brass tabs select physical instruments. No painted scientific material.
Final file: **1,951,146 bytes**, 48,854 bytes below the decimal 2 MB goal. All data is embedded. `src.html` and `material.json` remain editable; `handoff.md` maps the preparation and evidence.
`codex-report-1.md` is unchanged, SHA-256 `06c24a9e44103ead51dde356980dde15b19f845ec9da5bce4655012ebccb1893`.
Build only: no commits, deployment or polish round. Writes were confined to `tools/living-earth/` and `_scratch/living-earth/`.

## The real material

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

## Break the instrument

- **38/38 numerical probes passed**, preserved in `build2-numbers-final.json`: full/empty filters, depth/magnitude extremes, antimeridian distance, seven major-plate city checks, relief signs, reference arrivals, shadows, inverse S-P distances, sections, dataset counts and offline resource checks.
- **10/10 independent event-detail queries** agree with the packed catalogue within its stated rounding. Events span 1970-01-01 to 2025-12-31. Fresh source receipts and `data/build2/spot-checks.json` retain each comparison.
- Japan reference section: **377 events, deepest 560 km**. Mid-Atlantic reference section: **157 events, deepest 33 km**. A native jittered pointer section reached **3,000 km, 388 events, deepest 448.3 km**. Zero-length sections remain finite and empty filters stay usable.
- Three ideal station circles meet the selected epicentre with approximately **0 km** numerical offset. Coincident stations and a set of circles deliberately made inconsistent by 500 km return ambiguous. A 200-km residual gate prevents normalization from pretending inconsistent circles fit. Physical traces remain synthetic, not observed records.
- Surface S paths stop above the liquid core: minimum S-path radius **3545.7 km**, versus outer-core radius 3480 km. Far-side P paths cross the core. Reference iasp91 arrivals at 30 degrees are **P 370.264 s, S 670.266 s**.
- Default playback reaches 2025.999 and all **26,230 events in 18.681 s**. The opening count is zero. An earlier stale final count was fixed and this measurement repeated.
- The Chrome 4x CPU-throttle profile, 1366x768, all dots loaded, pointer-move rendering path: **330 frames, mean 16.666 ms, p95 16.8 ms, 60.003 fps**. Deliberately refiltering/rebuilding readouts every animation frame gave **58.24 fps**. Both are retained in `build2-performance-final/`; this is an emulated profile, not physical Chromebook certification.
- The one full audit completed: no console exceptions, no resize exceptions/stuck controls, and Motion off clean. All successful final product shots have zero console errors and zero horizontal overflow. Final positive and empty keyboard inspection paths announce the event or empty result.
- Bounded browser-fixture failures are retained separately: new-profile Chrome/contact-sheet runs timed out or disconnected. A known working 9992 profile completed the targeted product checks. Contact sheets were generated with Windows GDI+. No product pass is inferred from a failed driver run.

## Voice walk

The declared bank is `gravel-ranger`, with the field-seismologist direction retained. No recordings were generated; speech uses the kit's browser fallback. Voice timbre and physical speakers were not verified.
The first hint, "Drag to spin. Press play.", is issued once after first interaction, then voice speaks only when Read is pressed. State changes update the screen-reader status without unsolicited spoken commentary.
Held input, five taps two seconds apart, quick taps, settled focus and Enter paths were exercised by the audit. No welcome replay or narration pile-up was reported. Pin's former run-together text was replaced and rechecked as sentences with kilometres, cm/year averaging interval and heading units.
Read reports year and filtered count, selected quake or volcano, then the active instrument's measurement. It reports Ma in Rewind. Evidence: `build2-voice-walk.json`, `build2-post-pin.json`, audit voice walk and keyboard result files.

## Short test

Completed two **600-second builder explorations**, one through the grade-6 student's lens and one as an adult. These are recorded builder judgments with real browser input, **not a child user study**. Neither opened the Manual in its first two minutes. `build2-explore/walk.json`, twelve frames and two empty error logs preserve them.
The student walk started with Play, rotation and depth/magnitude changes, then explored layers, Japan's section, station records, rays, city search and 200 Ma. The adult walk compared regions, used a dateline section and extreme filters, inspected Hawaii, changed station geometry and deep-time evidence. Poor station geometry honestly returned ambiguous.

1. **Would a kid open it unassigned? Yes, provisionally.** Play produces worldwide plate-margin patterns in about nineteen seconds; spinning and filtering immediately change the material without reading.
2. **Would an adult play for fun? Yes.** Real places, detailed ocean relief, contrasting sections and the reconstruction sustained the adult walk. No compulsory sequence interrupts it.
3. **Is the real thing the interface? Yes.** Quakes, relief, plate geography, measurable synthetic traces and model rays form the working surface. Readouts carry units and provenance is available in the Manual.
4. **Does it work without a score or finish? Yes.** The archive and five instruments can be revisited indefinitely. A month can still find new regional depth patterns, station geometries and model comparisons among 26,230 observations; playback stopping creates no completion screen.

![Living Earth beside Elements Inspector](../../_scratch/living-earth/build2-final/family-comparison.png)

The comparison was inspected beside the actual Elements Inspector instrument. Living Earth's data density now supports the same immediate confidence; the instruments retain their own visual grammar. The comparison frame predates the final small layout and attribution fixes.

## Lesson creep check

Search terms: score, points, level, goal, sticker, badge, correct, wrong, try again, complete and well done.
Only **14 source-line hits for `points`** remain: geographic arrays, section-data properties, a rendering comment and WebGL `POINTS`. None is a reward. Every other term is absent from the source and all terms are absent from voice lines. Source contains zero em dashes. No kit header, mode pills or lesson progression appears.

## Done when

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

## Audit leads

The single full audit is preserved in `build2-audit/audit.md`, **499 grouped leads**: 425 overlap, 59 hidden-text/scroll-edge, eight keep-region, six disappearing-hint and one choices-cut-by-scroll-panel lead. It was not rerun after the targeted fixes.

- Intentional: the viewport canvas lies behind its labels and controls; its rectangular hit region is larger than the visible globe. The modal Manual covers and makes the instrument inert, accounting for its keep-region and hidden-under-modal leads. The hint is supposed to disappear after first action.
- Fixed: the archive selector covered the coordinate caption at middle widths. The caption now sits beside it; at short sizes the selector moves to the empty right side until a tool opens.
- Fixed: the short selected-quake card collided with the archive selector. The record was reflowed and the selector moved; record details are withheld while a short-screen instrument is open, with selected-event Read still available.
- Fixed: at 1000x625 the Wave faders, station readout and Pin-centre button were cut by the panel. Targeted measurements now show Wave **315/315**, Stations **323/323**, Pin **318/318** client/scroll height, with those controls exposed. Compact Wave is **180/180** and the three-station compact check **187/187**.
- Additional functional corrections: short cutaway labels no longer collide; map annotations use magnitude with the full event in its record; Enter inspection retains the complete status announcement. Selecting a smaller dot leaves the M8+ archive menu's prompt intact instead of blank.
- Read-only coordinate captions use `pointer-events:none`; an `elementFromPoint` result naming the canvas there is intentional, not evidence of occlusion. Their corrected text was inspected on frames.

No outstanding product obstruction was seen in the targeted follow-ups. Native long dropdown option text may truncate until opened; the selected event's full name is in its record and Read. Detailed triage is preserved in `build2-audit-triage.json`.

## Frames looked at

Opened and used all four required reference instruments before design. Inspected all twelve late size/calculation/Motion/grayscale/Manual/comparison frames, twelve exploration frames, early instrument checks, compact and phone follow-ups, relief conversion frames and the final targeted fixes.
Required size sweep: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and a real 375x812 iframe. Every size reported no horizontal overflow. The source/data renderer was ready in every successful final size shot.
All 65 audit PNGs and twelve other pending frames were reviewed through ten labelled contact sheets; selected affected audit frames and all subsequent product corrections were also viewed individually. Contact review does not establish a full text-by-text inspection at every size.
Evidence folders are prefixed `build2` in Scratch. Earlier failed or superseded fixtures are retained and distinguished from the final measurements. Final checks and file hashes are recorded in `build2-final-manifest.json`.

## Art made

No painted assets. `art/prompts.json` has no assets. The only raster scientific surface is the code-shaded ETOPO WebP, generated from actual elevations, with quality 0.72 after visual comparison. Coastlines, event dots, volcano triangles, plate geometry, fossils, traces, sections and rays are drawn in code.

## Engine changes wanted

None. No shared engine, kit, script, documentation or other tool was intentionally edited. No package or system software was installed.

## Left open

- Seven small present topology regions reference absent features; simplified joins include two gaps of about 0.93 degree, roughly 100 km. Full GPlates topology parity is not claimed. These limits and unknown-area behavior are visible in the Manual.
- Some continental fragment IDs lack a continuous rotation circuit over 0-200 Ma and are omitted from Rewind. Model sampling is 5 Ma; older fossil regions are schematic evidence carried on crust, not claims of occurrence at each dial date. Plate motion is not GPS or a Hawaiian hotspot reconstruction.
- Physical touch devices, a real school Chromebook and the exact browser-voice timbre still need hardware verification. Emulated performance and browser input tests are reported separately.
- Driver cleanup and host shutdown paths completed. Final socket probes returned Windows 10035 timeouts, so they do not independently establish that every test listener exited. No test process was deliberately left running.
- The existing anchor lesson card and module teacher plan were not replaced. This build does not authorize that curriculum decision.
- Process deviations: the first two immediate read-only inspection commands lacked explicit hard timeouts. A combined prerequisite read printed broader regular-build text than the Curiosity brief permits. Later commands were bounded; implementation followed the Curiosity brief. No permission or security setting was changed.

Unattended decisions: use the specified M5.5 fallback; resolve the published finite rotations in standard-library code rather than install pygplates; use a five-million-year motion average consistent with the model's warning; retain explicit unknown geometry; multiplex station channels so the controls fit; use browser speech without recordings. The first build's missing data-dependent instruments are now present.

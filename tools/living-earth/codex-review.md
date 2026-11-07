# Codex review: living-earth

## Played
Cold play preceded reading the builder report, handoff, notes and source. Used grade-6 and adult lenses: Play through the archive, jittered globe drags, all five instruments, Manual, layers, filters and real keyboard input. The quake arcs and detailed relief are worth exploring without an assignment; this is an instrument, not a lesson route. This is reviewer judgment, not a participant study.

## Findings fixed
- **Blocker, general, phone instruments:** the panel obscured most of an already tiny globe. Compact panels now leave the entire visible globe above them; Slice and Wave retain readable plots. Verified every phone instrument and reachable Close controls at 375x812.
- **Should fix, general, Stations:** Clear left old P/S labels beside zero-valued controls; editing a marker or replacing stations retained the revealed catalog record. Reset labels and invalidate the old reveal together. Guarded clearing during a captured pointer drag.
- **Should fix, general, Read and keyboard placement:** raw S-P, T+, timestamps and km abbreviations made poor speech; centre placement replaced its result announcement with coordinates. Read now uses sentences and units, keeps the measurement announcement, identifies out-of-filter selections and stops old speech on an instrument switch.
- **Should fix, general, Wave:** changing the source during a running firing continued automatically. A new source now resets elapsed time and waits for Fire.
- **Should fix, general, canvas fallback:** Relief off redrew the same relief. It now shows the flat land/ocean surface; pixel signatures differ and the fallback frame was inspected.
- **Should fix, general, Pin:** entering Lima selected the earlier substring Quelimane. Exact city names now rank before partial matches; Lima, Peru was independently driven and inspected.
- **Should fix, general, Rewind:** the two fossil-region keys depended on colour. Glossopteris now has a solid outline and Mesosaurus a dashed outline, with the small Mesosaurus regions drawn above the broader regions. The same distinction is in the Manual and legend; the grayscale evidence was rechecked.
- **Polish, general, Stations:** the flattest moment was aligning six markers on unlabelled, 18-pixel compact traces. Added a five-minute ruler and a 66-pixel trace beside its markers; kept synthetic arrivals and measuring under the student's control.
- Preserved the real-data pack, rich ETOPO globe, physical controls, family plate, lower-left Manual and free exploration. Added no topic, goal, rating, quiz, kit header or endpoint.

## Findings left
No known blocker or should-fix remains. Small model gaps and emulated hardware checks are limitations, listed below. Recorded voice timbre remains a polish/release follow-up.

## Break it
- No score, check, quiz or success gate exists to cheat. Station OFFSET is a physical separation; zero/inverted/unusable gaps and coincident stations return no circle or an ambiguous fit.
- Native Home/End reached both limits of all ten ranges. Depth handles crossing remain ordered; zero-length and dateline sections stay finite. Every layer and P/S switch was rapidly toggled twenty times.
- Independently decoded eight filter cases match the interface: 475 in 1970; 26,230 total; M9+ 2; M8+ 44; depth 300-700 km 1,548; zero-depth 13; exactly 700 km 1; M9+ at 700 km 0.
- Japan section [35,144] to [40,130]: 1,352 km, 329 events, deepest 560 km. Atlantic [0,-32] to [0,-12]: 2,224 km, 178 events, deepest 35 km. Depth axes remain true; only relief is x20.
- Rounded half-second picks on three synthetic traces put the intersection 3.36 km from the 2004 Sumatra catalog epicentre. Deliberately invalid gaps do not produce a persuasive fit. Clear during a real captured drag produced no exception.
- Empty, whitespace, long Unicode and accented city input stay usable. Exact Lima now chooses Peru. A fourth station restarts the station set without losing access to a channel.
- Archive and Wave survive real viewport flips while running. A new source stops the previous firing. Motion off fixes longitude and the drum. Zoom/polar endpoint evidence is in review-final-targets.
- Four-times CPU throttling, 1366x768, every quake loaded and the globe drawing: 179 frames, mean 16.666 ms, p95 16.7 ms, about 60 fps. This is an emulation, not a physical Chromebook certification.

## Voice walk
Held presses at a two-second pace: Play, Read; Slice and centre placement, Read; Stations and Place, Read; Wave and Fire, Read; Rewind and Fossils, Read; Pin and centre placement, Read; Sound off, Read.

| Kind | Expected | Observed |
| --- | --- | --- |
| Opening hint | once | 1 spoken |
| Read current instrument | each press | 7 reads, including Sound off |
| Unsolicited mode/teaching speech | none after hint | 0 |

Order: archive year/count; section length/count/depth convention; station P/S/gap in seconds; wave source, elapsed minutes/seconds, receiver degrees and missing direct arrivals; Ma/model; plate/edge/speed/history/volcano; same Pin state with Sound off. No narration pile-up or console exception. Fixed lines still exactly match voice/lines.json and allLines(). Browser fallback was exercised in muted Chrome; a gravel-ranger recording and physical speaker sound were not verified.

## Facts checked
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

## Sensitivity
Real disasters remain observations, without deaths, harm photography or ratings. Historical local counts are not hazard forecasts. Place names come from named catalogs; no claim about people or cultural traditions is added. A later cultural lens can check geographic naming, especially Hawaiian names, without treating this as a disaster game.

## Flattest moment left
Precise arrival picking still benefits from the half-second keyboard nudges, especially on a phone. The ruler and taller trace make it an intelligible measuring task; no automatic answer, reward or lesson ladder replaces it.

## Graphics
All cold, before/after, phone, keyboard, fallback and comparison PNGs were inspected; all 73 audit frames were inspected through thirteen contact sheets, with affected frames also opened individually. No new painted image was needed: scientific surfaces remain code and licensed data. Final HTML is 1,957,170 bytes, about 1,911 KiB, below 2 MB. Checked text pairs span 5.50:1 to 8.92:1; grayscale was inspected. Every required size was covered, including a real 375x812 iframe.

## Short test
- Would a kid open it unassigned? **Yes, provisionally:** spin and Play produce an immediate real-world pattern worth poking; no assigned route is needed.
- Would an adult play for fun? **Yes:** actual geography, deep sections, measured arrivals and reconstruction support repeated comparisons.
- Is the real thing the interface? **Yes after the phone fix:** observations, relief, traces and model rays carry the interaction; prose stays in the Manual.
- Does it work with no score or finish? **Yes:** free exploration works indefinitely; stopping the archive produces no completion screen.

![Cold Living Earth full-archive frame beside Elements Inspector](../../_scratch/living-earth/review-family-comparison.png)
Lesson-creep scan: only 19 uses of points remain, all geometry/data/WebGL or section properties. Every other requested search term is absent from src.html and all are absent from fixed voice lines. No em dash appears in source.

## Audit
Ran once with a 40-minute cap on Chrome 9951 and host 8755: **finished, 525 grouped leads**, all triaged in review-audit-triage.json. No console errors, undersized-control leads, horizontal overflow, stuck resize states or infinite Motion-off animation were reported.
454 leads are the full-stage canvas behind its controls/readouts; 7 are the intentionally disappearing first hint; 20 concern visible marker text above the native range hit areas; 39 concern the modal Manual covering the inert instrument. Frames confirm these are intentional, not hidden working controls.
The other 5 are the opening hint canceled by rapid instrument switches. Kept that cancellation: the stale hint should stop, and the Curiosity brief permits only the initial hint followed by user-requested Read, not automatic mode instructions or a repeated welcome. The normal paced voice walk hears the hint whole.
The audit host predates the final city-ranking and fossil-outline changes; those narrow changes were separately rechecked, without a second full audit. Failed Chrome launches were bounded and retained. An early host favicon 404 and the pixel-test readback performance advisory came from review fixtures, not automatic product network calls or product exceptions.

## Left open
Physical touch hardware, physical Chromebook performance and recorded gravel-ranger timbre were not certified. The model's unresolved plate areas, 5 Ma velocity average, synthetic surface-focus seismograms and schematic fossil regions remain openly stated scientific limits. No engine change is requested.
Unattended choices followed the brief: retain the explicit M5.5 fallback and licensed model, rank an exact city first, and fix access by exposing the material rather than adding a lesson flow. No commits or writes outside the two allowed folders were made.

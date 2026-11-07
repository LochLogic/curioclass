# Polish: sky-dome (Codex fix, round 1)

One blocker fixed; ten should-fix items fixed; performance remains NOT FIXED. All fourteen accepted polish items addressed, including the expressly permitted distance omissions. No commits. refine.md and refine/ untouched. All work ran from S:/CurioClass-codex; writes stayed in tools/sky-dome/ and _scratch/sky-dome/. Chrome ports 9910 to 9914 and host 8715 only.

Evidence paths below are relative to `_scratch/sky-dome/`. `fix-before/` contains the reproduced original; `fix-confirm/` contains the final geometry/card rechecks; `fix-final/` holds the full 65-state walk. `fix-followup/` checks the final audit-driven type changes. Full console log: `fix-confirm.log` and `fix-followup.log`.

## Blocker

1. **FIXED: stretched sky.** One radius drives projection, inverse projection, ring, hit positions, lines, trails and labels. Original equal-angle x/y scale ratio was 2.665 at 1366x768 and 3.634 at 680x425; final ratio is 1.000. See `fix-before-orion/orion-centred.png` beside `fix-confirm/orion.png` (FOV 50), and `fix-before/dipper-22.png`, `dipper-4.png` beside the same names in `fix-confirm/`. Default ring is round at all nine tested viewports. `fix-numbers.json`: inverse error 2.27e-13 degrees; 14,522 visible rendering samples, worst difference 1.27e-07 px. Ten astronomy functions are byte-for-byte unchanged (`fix-math-preserved.json`).

## Should fix

1. **FIXED: constellation names.** CONST appears on every stellar, Sun, Moon and planet card; Lines plus Names draws faint figure names with collision reservations. Whole-sphere area lookup includes concave and polar polygons. `fix-confirm/card-Sun.png`, `card-Moon.png`, five `card-<planet>.png`, `card-4730.png` (Crux), `card-5291.png` (Draco), `dipper-22.png` (Ursa Major), and `fix-numbers.json`. Independent numeric implementation: `fix-constellation-independent.json`.
2. **NOT FIXED: 60 fps at 4x CPU.** Reproduced 41.0 ms median (`fix-before-performance.json`). Batched stars and Milky Way, cached overlay rectangles/fonts/text widths, reused projected nodes and added a checked rendering lookup. Final 1366x768, Play 1 h/s, 90 retained draws at 4x: False: 23.1 ms median, 27.1 ms p95, True: 22.7 ms median, 26.9 ms p95. False means stars, Lines, Names, Ground and Milky Way; True adds both grid and trails. The 16.7 ms target still fails. Slower sprite-atlas, transformed-path and SVG-string experiments were removed. Keep this gate open; no physical-Chromebook claim is made.
3. **FIXED: zoom controls hide W.** Zoom controls sit below the circular ring. N/E/S/W are all drawn and clear at 1366x768, 1280x720, 1920x1080, 680x425 and the 375-wide hosts. See every `fix-confirm/size-*.png`; final narrow type frames are in `fix-followup/`. FOV readout also clears the buttons.
4. **FIXED: late spoken hint.** Original Play spoke with the hint hidden (`fix-before-hint-play.json`). Time dial, date wheel, Play and rate knob now produce zero hint entries. A first Lines gesture produces exactly one entry while hidden=false; its promise hides the line on completion. Moving time interrupts it immediately. `fix-final-hint-*.json`, `fix-final/hint-playing.png`, and the real dial drags in `fix-extra/` prove these cases. Read and Sound retain their previous semantics.
5. **FIXED: Sun distance.** DIST uses the unchanged JPL Earth orbit, shown to three decimals in au plus light minutes. June 21: 1.016 au, 8.5 light min; December 21: 0.984 au, 8.2 light min. `fix-confirm/card-Sun.png`, `fix-numbers.json`.
6. **FIXED: seasons and Sun path.** Manual now explains tilt, a higher/longer summer path, shorter winter path and opposite hemispheres. A discovery entry uses Denver's checked solstice readouts: 14 h 59 min and 9 h 21 min, described as about 15 hours and 9 hours 21 minutes. `fix-extra/manual-seasons.png`, `fix-numbers.json`, fresh USNO JSON in `data/fix/`.
7. **FIXED: wheel engraving.** Original SVG marks were 5 units; final marks are 9 units, about 8.64 physical px on the 96 px wheels, with dark #2a1f10 engraving against a gold halo. The text/halo contrast is 9.39:1. Marks sit outside the central value window; the pointer clears them. `fix-followup/size-680x425.png`, `size-800x500.png`, `size-375x812.png`; `fix-static.json`.
8. **FIXED: Read clock phrasing.** Original said “21 hours 22 minutes” (`fix-before-read-clock.json`). Final says “8:22 in the evening”, “1:01 in the morning”, “noon” and “midnight”, with the screen staying 24-hour. `fix-final-read-*.json`.
9. **FIXED: colliding star names.** Short names reserve space first; longer names try more positions, with leader ticks. Boxes reject other bright stars and labels. The unresolved Alpha Centauri pair gets one combined label. Sydney 2026-05-01 20:04 solar time shows Acrux and Hadar. `fix-before/sydney.png` versus `fix-confirm/sydney.png`; all 65 state probes found zero label/bright-star collisions. `fix-final-sydney.json` and `fix-numbers.json` preserve boxes and points.
10. **FIXED: Sydney ambiguity.** Original marked the field invalid and said unbundled. Final offers “Sydney · Australia” and “Sydney · Canada”, announces the two matches and leaves aria-invalid unset. A real held click chooses Australia. `fix-final/sydney-search.png`, `sydney-choice.png` and their JSON probes.
11. **FIXED: Escape focus theft.** Original focus became sky (`fix-before-escape-focus.json`). Final Escape leaves #city and #lines focused when no card is open; Escape in an input leaves an open card alone; Escape on a lever closes an actually open card and returns focus to the sky. `fix-final-escape-*.json` and frames.

## Polish accepted

1. **FIXED: plain Manual first.** Terms follow their plain explanations. Original counts, vertex checks, corrections, methods and licence notices remain under collapsed Sources and checks. `fix-extra/manual-seasons.png`, `manual-checks.png` and JSON text capture; final Manual recheck in `fix-followup/manual.png`.
2. **FIXED: distance precision.** Sirius is 8.6 ly and Rigil Kentaurus 4.3 ly; all checked distances below 20 ly use one decimal. `fix-confirm/card-2491.png`, `card-5459.png`.
3. **FIXED within the stated skip allowance: distant bright stars.** Added approximate Rigel 860 ly and Antares 550 ly with NASA primary facts and independent numerical checks. `fix-confirm/card-1713.png`, `card-6134.png`. Canopus was omitted because an acceptable NASA/ESA fact-page primary was not confirmed; Deneb was omitted because the checked NASA material explicitly gives competing 1,500 and 2,600 ly estimates. Neither was guessed. Their cards retain no checked value.
4. **FIXED: BC year window.** Typing 2800 BC shows 2800 with BC and stores astronomical -2799. BC/AD is switchable; arrows and Shift arrows retain year/century steps. `fix-final/ancient-year.png`, `era-switch.png`, `fix-numbers.json` covers 1 BC, 1 AD and both 3000-year endpoints.
5. **FIXED: daylight body names.** Sun, Moon and planet labels remain while stellar labels fade. `fix-final/noon-daylight.png` and midday Read frames.
6. **FIXED: one-line plate and clear rivets.** Removed the forced narrow wrapping; final plate is 10 px, nowrap, with inset text and rivets. `fix-followup/size-375x812.png`, `size-680x425.png`, `size-800x500.png` and font probes.
7. **FIXED: phone sky and accessible events.** At 375x812, the sky stage is 512 px (63% of the screen) with a 299 px round sky, up from the original roughly 220 px tall oval. The circle itself is 37% of screen height, constrained by phone width. Both rise/set rows stay visible; hint and zoom controls sit off the stars. The long southern pole readout has its own upper row; FOV sits beside the lower view controls. `fix-before/size-375x812.png` versus `fix-followup/size-375x812.png`; 375x667 also checked.
8. **FIXED: live-region names.** “Milky Way off” and “Latitude 39.7 degrees south” use visible names and directions. `fix-final-milky-live.json`, `fix-final-latitude-live.json`.
9. **FIXED: brass rate knob and REV.** Keyboard slider has seven detents, announced values, pointer turning and a value window. Reverse is engraved REV. `fix-final/keyboard-knob.png`, its JSON state (rate 5 after Home, two Rights, End, Left), final narrow frames.
10. **FIXED: deep-sky range hint.** M31 omits the range explanation; M45 shows it with two source estimates. `fix-confirm/card-M31.png`, `card-M45.png`, `fix-numbers.json`.
11. **FIXED: missing distance wording.** It says “no checked value”. `fix-confirm/card-4730.png`, `card-5291.png`.
12. **FIXED: polar compass explanation.** Manual explains that all ground directions from the North Pole are south, and from the South Pole are north. `fix-extra/manual-seasons.png` and its text capture.
13. **FIXED: time-dial focus outline.** Focus outline is inset 8 px into the dial, clear of its caption. `fix-confirm/wheel-focus.png` and keyboard real drag followups.
14. **FIXED: ring through AGE at 680x425.** The round ring clears the AGE telemetry. `fix-before/size-680x425.png` versus `fix-followup/size-680x425.png`.

## Settled calls

- Applied: hidden first-action hint audit leads remain rejected. No continuing hint or welcome was introduced.
- Applied: Craft's hint timing plus date wheel/rate knob silence; one fixed line only.
- Applied: Read's clock fix was treated as a should-fix item, including projector-friendly clock speech.
- Applied: Sydney ambiguity was treated as a should-fix item; the field now offers the two places.
- Applied: hint remains a Curiosity interaction, with no lesson flow added.
- Applied: all additions are measurements, names, controls or Manual explanations; no task, target, score, quiz, level, finish or kit header.
- Applied: preserved astronomy, tolerances, Motion off stepping, Same time each night, Read/Sound behavior, honesty notes and offline operation. Sources and checks was moved rather than cut.
- Applied: no cultural sky stories or origin claims; no new sensitivity review needed.
- Integrator-only rebundling note: no other tool or shared engine was edited by this pass. Spec open questions and “Not taken” remain unchanged.

## Cheats tried

No score, meter, quiz or check exists to pass. Instrument break attempts: rate Home/End and reverse; keyboard time/date changes; real whole-pixel, jittered time/date/sky drags; FOV 20/50/90/180 with camera altitudes -45/0/45/90; latitudes -90/-89.9/0/89.9/90 and longitudes -180/180; BC/AD endpoints; ambiguous and selected Sydney; Escape with no card, with a card and inside an input; hint interrupted by Play; Sound off then Read; Motion off Play stepping. No freeze or non-finite object coordinate appeared. Audit additionally resized live states to 760x900 and back.

## Voice walk

Held clicks were 120 ms and the normal voice walk used 2 s gaps. First Lines: “Drag the time dial.” once, visible when it starts, hidden after it ends. First time/date/Play/rate: no hint. Lines then Play at short spacing cuts the hint and removes its visual line. Read: date, time of day, place, then current object magnitude or Moon phase. The four clock cases and Sound-off Read are preserved in `fix-final-read-*.json`. `voice/lines.json` equals `allLines()`: only “Drag the time dial.” Dynamic Read stays dynamic. No new recordings were made; the existing browser fallback remains and the bundler reports that the fixed recording is absent.

## Engine changes wanted

None. The existing voice wait promise was sufficient; no kit edits.

## Audit

One full `scripts/audit_tool.py` run, Chrome 9911, host 8715, explicit 2,400-second limit. It finished. Original audit: 34 leads, preserved in `fix-audit/audit.md`.

All small-type leads were addressed after their original audit captures: plate at 680/800 and phone place, Sun/Moon events, pole, FOV, rate and plate now compute to 10 px or more. Final rechecks include default, southern, ancient and Sydney phone states (`fix-followup-*.json` and frames). All hidden-hint leads are expected Curiosity behavior under the settled call. The two quick-tap hint cuts on Year era and Now are also expected: those controls move time, ending the hint under Should fix 4's “whichever is first” rule. The full per-control table and final stress/voice rows are preserved in audit.md. No welcome or goal was added.

The full audit was not repeated. Focused followups checked the type changes and the corrected Antares corroboration citation. No functional astronomy calculation changed after the full regression walk. Final bundle is 584,934 bytes, below 2 MB. Driver rechecks report zero console warnings/errors/exceptions. Manual resource probes show zero requests; all runtime code and data are bundled. Source links are user-activated references.

## The real material

All source names and terms remain in the Manual and tool.draft.json. Raw Refine gathering is in `data/fix/manifest.json`, fetched 2026-11-05; downloads had 25-second limits. Gathering used substantially less than the 45-minute allowance. No executable or system software was downloaded or installed.

| Material touched | Named sources and terms | Selection / use |
|---|---|---|
| Constellation figures, names and areas | Olaf Frohn, [d3-celestial](https://github.com/ofrohn/d3-celestial), BSD 3-Clause, expressly listed fallback; licence read first and full notice retained. [IAU list/charts](https://www.iau.org/IAU/Astronomy-FAQs/Constellations.aspx), CC BY 4.0 name check. | All 89 area rings and label points (Serpens split), no vertex thinning. J2000 frame. `fix_pack_data.py` reproduces the packing. No cultural narratives. |
| Stellar cards / colour | Yale BSC5, Hoffleit and Warren 1991, [NASA HEASARC](https://heasarc.gsfc.nasa.gov/W3Browse/star-catalog/bsc5p.html), US Government Works/public domain; IAU WGSN proper-name snapshot, Attribution/current web-text policy CC BY 4.0. | Existing 9,096 stars, proper motion, flags and B−V values retained. Rendering uses colour/opacity bins, disclosed; card values are unchanged. |
| Added distance facts | [NASA: Orion/Rigel](https://science.nasa.gov/universe/stories/quick-reads/discovering-the-universe-through-the-constellation-orion/) and [de Almeida et al. 2022](https://arxiv.org/abs/2204.00372), 0.26 ± 0.02 kpc; [NASA: Antares](https://science.nasa.gov/image-article/apod-2012-april-17-antares-and-clouds/) and [Nature Astronomy 2017](https://www.nature.com/articles/s41550-017-0279-x), 170 pc. | NASA public-domain numerical facts; only original numerical readouts, no protected paper prose or photographs copied. 860 and 550 ly marked approximate. ESO release eso1726 did not contain distance and was replaced as corroboration. |
| Sun DIST and light time | [JPL orbital elements](https://ssd.jpl.nasa.gov/planets/approx_pos.html), [JPL constants](https://ssd.jpl.nasa.gov/astro_par.html), checked against [NASA Sun Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html). US Government numerical facts, public domain. | Existing Earth orbit; au = 149597870700 m; c = 299792458 m/s. Original calculations only. |
| Seasons and daylight | [USNO seasons](https://aa.usno.navy.mil/faq/seasons_orbit), [NASA seasons](https://science.nasa.gov/helio-and-you-seasons-on-earth-mars-and-beyond/), [USNO one-day service](https://aa.usno.navy.mil/data/RS_OneDay). US Government factual material, public domain. | Original plain paraphrases. Fresh 2026-06-21 and 2026-12-21 results at 39.7392,-104.9903; summer DST on, winter off. No tables or source prose copied. |
| Sydney choice / place readouts | [Natural Earth populated places](https://www.naturalearthdata.com/downloads/50m-cultural-vectors/50m-populated-places/), public domain; existing Wikidata coordinate checks, CC0. | Existing 1,238 places and coordinates unchanged; only ambiguity behavior corrected. |
| Calendar and astronomical readouts | Existing independently implemented Meeus methods and JPL tables; named chapters and terms retained in the Manual. | BC/AD display conversion and spoken clock wording changed; no position, phase, rise/set or orbit method changed. |

## Lesson creep check

`fix-static.json`: no score, goal, sticker, badge, correct/wrong, try again or well done. “points” hits are geometry arrays, “level” is the physical phrase “minute-level model errors”, and “complete” describes the historical IAU name list. None creates a lesson reward or task.

## Frames looked at

Original 21-state contact sheet and correctly centred original Orion; the complete 65-state walk (`fix-final-contact-1.png`, `fix-contact-2.png` through `fix-contact-4.png`); the 29-state final geometry/card confirmation (`fix-confirm-contact.png`); full phone, 680, Sydney and Orion frames; real drags and Manual (`fix-extra-contact.png`); final audit contact sheets and focused followups. No painted art was added.

## Left open

- Should fix 2 / Done when 7: 4x CPU median remains above 16.7 ms. This is a real open exit gate.
- Canopus and Deneb distances remain omitted under Polish 3's explicit skip allowance. No HIPPARCOS dataset with non-permitted redistribution terms was added.
- Existing missing calm-professor recording remains a recording-production item; no new voice line was added.
- Spec open questions (module reach, shadows, initial ground silhouette and future stories) were left unchanged as instructed. No registrations, uploads, publication, shared edits or commits.

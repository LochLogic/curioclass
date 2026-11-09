# Codex review: graph-studio

## Played

Cold opening, exponent drag, typed parameter, table, Manual, sinc, keyboard and empty-input play preceded the builder report and source. Then explored as a grade 9 student and an adult: 18 completed paced segments, 10.390 minutes total, plus native pointer/keyboard walks. These are agent explorations, not a human user study. It felt like a usable plotter; the strongest surprise was a 2:1 Lissajous pair becoming a parabola.

## Findings fixed

- **Blocker, family:graphing, hole probes:** a symmetric pole, `1e-10/x^2`, was labelled as a finite hole at height 10000. Four-distance, two-sided convergence now rejects that pole and its tiny scaled variant while retaining sinc and zero-height removable holes. Evidence: `review-before-probes.json`, `review-verification.json`.
- **Should fix, family:graphing, pins:** a native drag visually merged pins but retained a tiny denominator and printed a finite rate. Dragging one within six pixels of the other now snaps their parameters together; the real drag re-check reads undefined. No denominator or slope is fabricated.
- **Should fix, general, real data:** matched the Census series to its declared source versions; modern 1940, 1970 and 1980 become 132.17, 203.21 and 226.55 million. Saturn's approximate sidereal period becomes 29.45 years. The spec remains unchanged; source versions and rounding are explicit.
- **Should fix, general, permissions:** OpenStax's current licence is CC BY-NC-SA 4.0, not the recorded CC BY 4.0. It and MathWorld are verification references only; no publisher prose, figures or datasets are imported. Corrected the rose URL, expanded government-source credits and included the project's MIT notice.
- **Should fix, general, drawers:** modal drawers made Read unreachable. They now allow the power panel, close with Escape, restore focus to their handles, and stop an obsolete Read on a context change. Manual Read follows the visible paragraphs.
- **Should fix and flattest-moment lift, family:graphing, fitting:** the wide dimmed editor hid the real data. Measurements now occupies the tape, leaving the paper live; columns fold away, R² stays in its heading on small screens, and Read names the actual dataset, units, fit and R².
- **Should fix, family:graphing, state/readouts:** an open table now follows rulers; a data setup opens Table on its fit at the first measurement. Setup/load refresh dataset labels and clear obsolete measurements. Rapid scrubbing publishes its final live value. A 1001-pair paste preserves the prior data; empty/invalid controls are rejected explicitly.
- **Should fix, family:graphing, extremes:** guarded underflowing or invalid paper bounds during form entry, fitting, pan, zoom and square-grid resizing. Aliasing warnings inspect current trigonometric arguments, including parameters, and remain visible in compact views.
- **Should fix, general, audit-confirmed layout:** Load grew from 40 to 44 pixels. Short landscape tape navigation and rulers now keep the first slider visible at 680x425 and 800x500 without reducing its 44-pixel height. Fixed root/live-region overflow; all eight required viewport sizes measure zero page overflow.
- **Polish, general, voice:** equation Read expands sine, inverse functions, square root and function notation for the ear. Preserved the quiet first hint, plotter hardware, engineering paper, eight inks, maker's plate and open-ended play.

## Findings left

No confirmed blocker or should-fix remains. Verification limits are listed below. Internal scrolling for additional rulers, end caps, long tables, source citations and the optional columns editor remains intentional.

## Break it

45 numerical/data checks and 35 extreme-input checks passed. Cases include precedence, implicit multiplication, f(4) = 4, inverse trig in both units, circular definitions, poles/holes, corners, all four regressions, constant-data R², log-domain rejection, 1000/1001 pairs, bad/empty rows, four save slots, source restoration, zero/negative steps and bounds.

Tried 100 rapid equation edits, eight pens and removal back to one, ±1e100 rulers and travel limits, repeated zoom to both limits, every toggle both ways, table paging, rapid drawer switches and Motion off during ruler play. Native pointer checks cover exponent scrubbing, a point and coincident pins; native arrows change a ruler while retaining focus. The audit resizes running states and controls. No instrument console exceptions occurred in the completed checks.

There is no pass state to cheat. R² describes a fitted model, never the student; its coordinate space, point count and undefined constant-data case remain explicit. Sweeping a ruler changes the mathematics and earns nothing.

## Voice walk

Held clicks, 120 ms presses, two-second main-path spacing, Sound on: equation tape, number tab, Read. Final log: **“Drag the 2 up or down.” once**, then **“y equals x squared. At x equals 1.000, y equals 1.000.”** as part of requested Read. Final scrollX, scrollY and page overflow are zero.

Side paths logged the NOAA dataset, 67 pairs, quadratic fit and ordinary-space R squared 0.9995; a rose Read says “sine”; a scrolled Manual Read supplies the visible sources. Sound-off Read works, and closing its drawer releases it for a new plotter Read. No automatic lesson or praise sequence was added.

| Line/action | Expected | Logged |
|---|---|---|
| Initial hint on relevant first tap | Once | Once |
| Main, data and rose Read | Current text on each press | Current text |
| Five Read presses and two quick presses | No stale queue or lost action | Audit clean |

Chrome is muted by the required driver. These are dispatch/log checks; audible quality and a recorded wise-mentor take were not auditioned. The permitted browser-speech fallback is active.

## Facts checked

Live sources checked 2026-11-05. Data and licences are named in the Manual and draft metadata. Extracts, source responses and reproducible calculations are in `_scratch/graph-studio/data/review/`, `review-pack-check.py` and `review-reference.py`.

| Material/fact | Named source, licence and check |
|---|---|
| CO₂ annual means | [NOAA GML annual file](https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_annmean_mlo.txt), all 67 years 1959-2025, ppm to two decimals; [public-domain terms](https://gml.noaa.gov/about/disclaimer.html). Credits include GML, Xin Lan, Ralph Keeling and the early Scripps record. The Maunakea interruption is stated. |
| Planet measurements | [NASA individual fact sheets](https://nssdc.gsfc.nasa.gov/planetary/planetfact.html), eight rounded J2000 mean semimajor axes and approximate sidereal periods; US government work, public domain. Explicitly distinguish these from instantaneous distances and tropical periods. |
| Historical population | [Census 1910-2020 resident counts](https://www.census.gov/data/tables/time-series/dec/popchange-data-text.html) and [Statistical Abstract 2012 table 1](https://www2.census.gov/library/publications/2011/compendia/statab/131ed/tables/12s0002.pdf), one row per decade, rounded to 0.01 million; public domain. Earlier rows use the declared unrevised 1870 count. All 12 modern rows pass the independent packing check. |
| Computed fits and slopes | Original Curio Class mathematics, MIT, plus an independent Python solver: CO₂ line R² 0.9805554803 and quadratic 0.9994830149; planet exponent 1.4997021008; x² secant from 1 to 3 is 4. The spec's line value 0.981 uses three decimals; the instrument correctly shows 0.9806 at four. |
| Growth, e and crossings | [OpenStax College Algebra 6.1](https://openstax.org/books/college-algebra-2e/pages/6-1-exponential-functions), current [CC BY-NC-SA 4.0](https://openstax.org/books/college-algebra-2e/pages/preface), reference only; independent calculations give crossings -0.9371092012, 1.0775501500, 58.7701059379 and early Census growth about 3.015% per year. Preserve the builder's correct distinction between two positive crossings and three real crossings. |
| Kepler, roses, sinc and Lissajous | [NASA Kepler laws](https://science.nasa.gov/solar-system/orbits-and-keplers-laws/) and OpenStax astronomy; [MathWorld Rose Curve](https://mathworld.wolfram.com/RoseCurve.html) with OpenStax polar graphs; [Emory limits](https://mathcenter.oxford.emory.edu/site/math111/probSetLimits/) with OpenStax calculus; [MathWorld Lissajous](https://mathworld.wolfram.com/LissajousCurve.html) with [Wisconsin's museum](https://www.physics.wisc.edu/ingersollmuseum/exhibits/waves/lissajous/). NASA is public domain; current OpenStax is CC BY-NC-SA; the other pages retain author copyright. References only, no protected content imported. Sinc's hole is height 1 in radians and pi/180 in degrees. |

## Sensitivity

The Census curve represents changing boundaries and enumeration coverage, not everyone in fixed modern boundaries. Early exclusions of many Indigenous people are now stated, checked against the [Census Bureau](https://www.census.gov/about/history/census-records-family-history/census-records/censuses-of-american-indians.html) and [National Archives](https://www.archives.gov/news/articles/native-americans-census), both public-domain government sources. A later cultural lens should inspect that wording and the declared historical count versions. There are no people images or claims about a whole culture.

## Short test

- **Would a kid open it unassigned? Yes, plausibly:** glowing number tabs, reversible shape changes and rose curves invite immediate poking without instructions to clear.
- **Would an adult play for fun? Yes:** parameter families, the Lissajous/parabola connection, remote crossings and real-data fits sustain exploration.
- **Is the real thing the interface? Yes:** evaluated ink and measured data fill the paper; fitting now keeps them visible while adjusting the model.
- **Does it work with no score or finish line? Yes:** nothing judges or ends the session. These are review judgments, not participant-study results.

![Graph Studio beside Elements Inspector](../../_scratch/graph-studio/review-comparison-0.png)

## Flattest moment left

Editing many end caps or a long column paste on a phone still needs internal scrolling. The frequent curve controls and first ruler remain available; the fit and its R² no longer disappear behind a dimmed editor.

## Graphics

Exact canvas mathematics and CSS hardware; no raster art needed or added. Inspected the cold, before, verification, 18 exploration, final, proof, 33 audit and targeted-fix frames, including grayscale and both reference tools. Kept the paper, rail, carriage, ink weight and slide-rule cursors. Final bundle: **121,581 bytes**, one offline file. Exact `check_tools.py` validation functions pass in a Scratch fixture; its global rebundle was excluded to respect the folder boundary. All eight ink contrasts in notes exceed 4.5:1.

## Audit

One audit only: `_scratch/graph-studio/review-audit/audit.md`, 530.859 seconds, Chrome 9931, host 8735. It completed with 60 leads, 33 inspected frames, no console errors, no infinite Motion-off animation, no lost focus across 23 held-click/Enter walks, clean Read repeats/quick presses and no resize exceptions or stuck controls.

Confirmed leads fixed: 40-pixel Load and the hidden first short-landscape ruler. Re-shot 680x425, 800x500, 1366x768 and 375x812 as applicable: Load is 44x44; the first ruler is fully visible and native arrows work. A subsequent focused root-overflow check gives zero horizontal/vertical page overflow at every required size.

Other leads are intentional: the quiet hint and measurement tags overlay paper; pointer-transparent tags fail hit-test coverage despite being visible. Drawers cover the underlying tape/paper by design. Manual references and optional editors scroll; closed details are not answer choices. The phone Add glyph has a 44-pixel target and an accessible name despite zero-sized replaced text. Hints disappear after action. The 20 missing-premise warnings apply a lesson welcome norm to a Curiosity with zero lesson modes; no premise was added.

The audit snapshot precedes the final compact-layout, target-width, root-overflow and visible-Manual-Read fixes. Their targeted evidence is in `review-auditfix/`, `review-scrollproof/` and `review-last-voice/`; no second full audit or polish round was run. Final hashes are in `review-final-manifest.json`.

## Left open

- Physical Chromebook 60 fps, physical screen-reader operation and audible narration quality are unverified. Do not promote desktop checks into hardware claims. The bank clip is absent; recording was outside this run's ground rules.
- Numerical sampling, hole probes and feature finding remain approximate, as the Manual states. Direct trace/pins apply to equation-tape curves; fitted curves have their own readout and table. Inequalities and general implicit equations remain deferred by the spec's lean.
- Raw socket downloads were denied; live web-source inspection and preserved extracts supplied verification. One Chrome connection-loss batch was excluded and retried once in smaller batches. An early selector fixture failure and host favicon 404 were corrected, not counted as instrument failures.
- The drivers issued owned Chrome cleanup and servers shut down in finally blocks; independent local-port probes timed out, so they do not independently certify process state. No git commits, publishing or out-of-folder project edits were made.
- Some instantaneous file-read commands lacked an external hard-deadline wrapper. Bundles, browser batches and the audit used explicit 120-second, 300-second and 2400-second limits.

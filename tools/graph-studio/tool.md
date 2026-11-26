# graph-studio: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: graph-studio (Curiosity No. 08)

#### Built

A working mathematical pen plotter, with cream engineering paper filling the working area, a metal rail and carriage, equation tape, eight pen inks, hairline slide-rule cursors and a brass measurement tag. The lower-left Manual and maker's plate read Curio Class Curiosities · No. 08 · Graph Studio. Motion, Sound and Read occupy the plotter's own power panel.

The instrument supports the listed arithmetic and elementary functions, implicit multiplication, f and g definitions and evaluations, vertical equations, movable points, polar and parametric curves, automatic rulers with animation and editable bounds, pan, wheel/pinch zoom, equal axis spacing, log axes, degrees/radians, tracing, pins, secants, numerical tangents and key features. Tables remember start and step per pen and also tabulate fitted curves. Data has all three bundled datasets, pasted columns and four least-squares fit families. Notebook has six setups and four browser-local save slots. A read-only URL hash can preload an expression.

One offline bundle: 110,927 bytes (108.3 KiB), below the spec's 400 KB target and the 2 MB goal. Data is under 3 KB. No image, library, font or data downloads are needed. Draft metadata remains draft; nothing was published or committed. This was Build with verification fixes, with no polish round.

Choices made unattended: inequalities and general implicit equations stay out, as the spec leans; URL hash preload is included. No plan.md was made, as specified. No lesson frame, sequence, reward or finish was introduced. The report was written last because the user's report-and-stop instruction overrides the machinery's early-report suggestion.

#### The real material

All bundled values are transcribed from the supplied spec, rather than represented as a new live download. Names, links, permissions, rounding and numerical limitations are in the Manual and tool.draft.json.

| Material or fact | Source and permission |
|---|---|
| 67 annual Mauna Loa CO₂ means, 1959-2025, ppm | NOAA Global Monitoring Laboratory, co2_annmean_mlo.txt; US government data, public domain, credited to GML. |
| Eight planetary distances in AU and periods in Earth years | NASA Planetary Fact Sheet; rounded spec values, US government data, public domain. |
| 24 US decennial population values, 1790-2020, millions | US Census Bureau decennial counts; rounded spec values, public domain. |
| Exponential growth, eventual dominance and the limit defining e | OpenStax College Algebra 2e, chapter 6; CC BY 4.0. |
| Rose petal counts for positive integer n; 3:2 Lissajous figures | Wolfram MathWorld, Rose and Lissajous Curve; mathematical facts paraphrased, pages copyright Wolfram Research, no text or images copied. |
| Parsing, sampling, fitting, slopes and drawings | Original project code; no external mathematics library or branded calculator implementation. |

Independent Python arithmetic in ../../_scratch/graph-studio/reference.json gives Mauna Loa line R² = 0.9805554802502504 and quadratic R² = 0.999483014858906. The first rounds to the spec's 0.981 at three decimals; the instrument shows 0.9806 at four. NASA's power exponent is 1.4997221898541817. Pins at x = 1 and x = 3 on x² give 4 exactly.

One spec correction: 2^x and x^10 have three real crossings, at -0.9371092012, 1.0775501500 and 58.7701059379. The two quoted in the spec are the positive crossings. The Manual says this explicitly and the plotter finds all three.

#### Break the instrument

- Final functional suite: 19 of 19 passed, including precedence, implicit multiplication, every named elementary function, definitions, real-domain failures, polar/parametric/vertical forms, holes, intersections, secants, tangents, regressions, per-pen tables, fitted tables, notebook serialization, tiny nonzero values, eight pens and empty input.
- Trusted browser text input created a ruler while preserving equation focus, typed f(x) followed by Enter and f(4), and produced f(4) = 4.000. Native keyboard scrubbing preserved decimal and scientific precision: 0.10 to 0.11 and 1e3 to 3e3. An Alt precision drag changed x² to x^0.5, with the negative branch undefined and f(4) = 2.
- Whole-pixel jittered pointer tests moved a ruler to -10, dragged a pin along x² and moved an ordinary point. Coincident pins print undefined; a corner has no fabricated tangent. tan(x) and 1/x have breaks; sin(x)/x has an open circle at (0, 1).
- Unsafe syntax, excessive nesting and recursive definitions are bounded. No typed expression enters JavaScript evaluation. Empty data clears the fit; an invalid row keeps prior data and names its row. Logged fits reject nonpositive data and constant data have undefined R². Oversized measurement columns request rescaling.
- Four real Save clicks and a later Load verified all four slots. Storage stays on this device and the Notebook says so. No account, upload or transfer code.
- 10.52 minutes of qualifying exploration across 14 bounded segments: 5.26 minutes from the grade-9 perspective and 5.26 from the adult perspective. Parabolas, roses, Lissajous figures, widely separated crossings and all four fit families were varied. An early fixture that assigned a fit without redraw was excluded and replaced. These are automated agent explorations, not observations of actual children or an adult user study.
- Sampled desktop Chrome frame intervals had median 16.7 ms and 95th percentile 16.7-16.8 ms. This supports about 60 fps on this test machine; no school Chromebook was available.

Evidence: ../../_scratch/graph-studio/ui-walk/results.json, reference.json, exploration-summary.json, functional-results.json, final-checks frames and the audit folder. Build fixes addressed native-input focus, the Enter target, held-pointer stability, readout overlap and uniform refinement budgets.

#### Voice walk

wise-mentor is selected in voice/lines.json. No recordings were generated, as required; Curio.voice uses the supported browser-speech fallback. The one bank line is “Drag the 2 up or down.” There are no automatic teaching or praise sequences.

Held clicks at a two-second pace on the main path logged the hint once, then Read's current equation, trace and pin text. The side path used Sound off, a rose setup and Read; Read still supplied current text. Ordinary actions did not repeat the hint or queue stale narration. Current readouts also use native labels, values, output elements and a polite live region. The recorded bank voice itself was not auditioned because the clip does not exist; test Chrome was muted.

#### Short test

These are judgments after the bounded exploration, not user-study results.

- Would a kid open it unassigned? **Yes, plausibly:** the opening pen makes a curve immediately, changing a number changes its shape, and a letter makes a physical ruler. There is no reading gate.
- Would an adult use it for fun? **Yes:** parameter families, rose curves and Lissajous figures invite play; regressions, log axes and measurements give real reasons to keep using it.
- Is the real material the interface? **Yes:** the ink is evaluated mathematics, pins measure its coordinates, and measurements determine the fitted curve. No painted data or simulated success.
- Does it work without a score or finish line? **Yes:** the working state persists as an instrument page. It never evaluates the person using it.

![Graph Studio beside Beat Lab](../../_scratch/graph-studio/comparison.png)

The comparison uses a live typed equation and ruler beside Beat Lab in use. Elements Inspector, Span and Spire and Pocket Universe were also opened and used before design. The shared marks were adopted; their palettes and scenes were not copied.

#### Lesson creep check

The source and voice lines were searched case-insensitively for score, points, level, goal, sticker, badge, correct, wrong, try again, complete and well done. Only “points” remains: 11 occurrences describing mathematical/data points, key points and an internal points array. None is a reward. Every other search term has zero hits. No em dashes occur in the produced source, bundle or metadata/notes. The original spec was not edited.

#### Done when

| Spec item | Result and evidence |
|---|---|
| 1. Opening parabola, scrub and responsiveness | FAIL to verify the Chromebook clause: that hardware was unavailable. The 1.2-second draw, native scrubbing and about 60 fps on desktop Chrome pass. |
| 2. Automatic letters and playing ruler | PASS: trusted typing created a while keeping input focus; real Play input swept its value and plot. |
| 3. f definition and f(4) | PASS: native typing and Enter produced f(4) = 4.000. |
| 4. Exponential/polynomial crossings | PASS: positive crossings 1.078 and 58.77 are labelled; the negative crossing is included too. |
| 5. Mauna Loa fits | PASS: independent Python and browser agree; R² is 0.9806 and 0.9995 at four decimals. |
| 6. Planet power fit on log axes | PASS: exponent 1.4997221899, displayed 1.500, with eight real data pairs. |
| 7. Average rate on x² | PASS: pins (1, 1) and (3, 9) read 4.000. |
| 8. Poles and hole | PASS: discontinuity frame and numerical tests show breaks and the open circle at (0, 1). |
| 9. Keyboard, announced values and Motion off | PASS: all 23 walked controls retained usable focus and passed Enter twice; native text input and scrubbing passed. Motion-off and resize audits were clean. Native ARIA values and live outputs are present; no physical screen-reader session was available. |
| 10. Required sizes | PASS: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and the 375x812 iframe were inspected. The confirmed 760-pixel base overlap and small Data drawer fold were fixed and re-shot. Long forms/tapes scroll internally; the active equation is sticky. |
| 11. One offline file and contract | PASS: 110,927 bytes, no external resources, zero contract/syntax problems and no em dashes. Exact check_tools.py functions ran on this draft in an isolated Scratch fixture to avoid its global rebundle of other tools. |
| 12. No lesson/reward frame | PASS: source search, frames and open-ended use. |

#### Audit leads

The completed audit produced 72 mechanical leads and zero console errors. All 27 audit frames were inspected, including full-size views of the flagged layouts. Its 23-control held-click/Enter walk, resize checks, Motion-off check and repeated/quick Read checks finished without errors or lost focus.

- **Fixed, 760-pixel base:** reserve room for two rows of controls. The targeted frame measures paper bottom 773 px and controls top 777 px, with no overlap.

- **Fixed, small Data drawer:** reduce the textarea height only in short landscape windows. Plot data, Fit paper to data and the fit selector are all visible at 680x425. The long readout area still scrolls normally.

- **Fixed, Manual references and code:** all six citation links now have at least 44-by-44-pixel hit areas, verified at desktop and 375 pixels. Inline equations stay together, and the phone code-box overlap count is zero. Source references at the end of a field guide are intentionally reached by scrolling; they are citations, not hidden choices in an exercise.

- **Intentional canvas overlays:** the first hint and brass measurement tags sit on the graph paper. Tags have pointer-events disabled, so the audit's hit test reports the canvas as covering them. Full-size frames confirm they are visible, separate and legible. The initial hint disappears after meaningful input, as the Curiosity brief requires; its later hidden-state leads are expected.

- **Intentional modal coverage:** Manual, Data and Notebook temporarily make the background inert. The audit's global keep regions refer to the underlying paper, equation and family plate, so native dialog hit testing reports them as covered. Close restores the instrument; keyboard focus is retained.

- **Intentional phone Add icon:** the text is visually replaced by a 23-pixel plus glyph on a 44-pixel button. Its accessible name is Add equation. The zero font-size lead describes the replaced text, not the visible glyph.

- **Welcome leads:** the Curiosity has zero lesson modes and no premise speech. Once an action makes the hint obsolete it is removed, rather than followed by a delayed welcome. The initial hint path and requested Read paths were logged; repeated Read and quick Read were clean. A final held-click check also verifies that typing cuts an obsolete hint while Read supplies the new cubic equation.

Targeted post-audit checks also verified that Tangent immediately exposes a trace and slope, t makes a ruler in Cartesian equations while remaining the parameter in polar/parametric forms, and signed/scientific scrubbing preserves its number. The 19-case suite was repeated after that math change and passed. No second full audit was run. See audit-fixes/, latest-proof.json and parser-check.json.

The audit ran once, with its 40-minute cap, on Chrome port 9991 and host port 8795. Only affected views were re-shot for confirmed build fixes; no second full audit or polish round was started. Its mechanical findings remain preserved beside these answers.

#### Frames looked at

All captured instrument frames were examined individually or on labelled contact sheets, with flagged views opened full size. Evidence folders: models (all four references), first, checks, mobile, late, final-checks, exploration, ui-walk, audit and audit-fixes, all under ../../_scratch/graph-studio/. The comparison PNG was also inspected. Default, grayscale, phone iframe, both pointer and keyboard paths, every setup family, drawers, poles, holes, labels, fits, pins, Motion off and audit resize states are covered.

#### Art made

No painted assets. Canvas draws all mathematical material; CSS draws the paper, rail, carriage, tape, clear hairline rulers, power panel and engraved plate. art/prompts.json has an empty asset list. Screenshots and the comparison are evidence only and are not bundled into the instrument.

#### Engine changes wanted

None. Shared kit, scripts, docs, other tools and git history were not changed. All implementation work is confined to tools/graph-studio/ and its specified Scratch folder.

#### Left open

- School Chromebook performance and actual screen-reader operation were not tested on that hardware. Desktop Chrome measurements and native semantics are evidence, not substitutes for those checks.
- A recorded wise-mentor clip is absent; the permitted browser fallback is configured, with dispatch/queue behavior verified in muted Chrome. Audible quality was not verified. First-load drawing is silent until a user gesture permits sound; controls then use quiet kit tones.
- Numerical sampling can alias, hole probes are not symbolic limits, and closely spaced or repeated features can be missed. Key-feature finding currently covers explicit y curves. Direct tracing/pins use equation-tape curves; fitted curves have their own readout and table. These limits are documented rather than presented as exact symbolic algebra.
- Inequalities and general implicit equations are deferred by the spec's lean. No lesson plan, publication, commit or polish round was requested or performed.
- One parallel Chrome connection reset was retried in smaller serial checks. Earlier test-fixture issues and the native typing failures were corrected and the successful evidence retained. All owned Chrome/server processes were closed.
- The initial workspace/brief read returned in 0.17 seconds before the hard-deadline wrapper was installed; later shell commands had explicit limits. The report was generated only after verification so its creation can be the requested stopping point.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: graph-studio

#### Played

Cold opening, exponent drag, typed parameter, table, Manual, sinc, keyboard and empty-input play preceded the builder report and source. Then explored as a grade 9 student and an adult: 18 completed paced segments, 10.390 minutes total, plus native pointer/keyboard walks. These are agent explorations, not a human user study. It felt like a usable plotter; the strongest surprise was a 2:1 Lissajous pair becoming a parabola.

#### Findings fixed

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

#### Findings left

No confirmed blocker or should-fix remains. Verification limits are listed below. Internal scrolling for additional rulers, end caps, long tables, source citations and the optional columns editor remains intentional.

#### Break it

45 numerical/data checks and 35 extreme-input checks passed. Cases include precedence, implicit multiplication, f(4) = 4, inverse trig in both units, circular definitions, poles/holes, corners, all four regressions, constant-data R², log-domain rejection, 1000/1001 pairs, bad/empty rows, four save slots, source restoration, zero/negative steps and bounds.

Tried 100 rapid equation edits, eight pens and removal back to one, ±1e100 rulers and travel limits, repeated zoom to both limits, every toggle both ways, table paging, rapid drawer switches and Motion off during ruler play. Native pointer checks cover exponent scrubbing, a point and coincident pins; native arrows change a ruler while retaining focus. The audit resizes running states and controls. No instrument console exceptions occurred in the completed checks.

There is no pass state to cheat. R² describes a fitted model, never the student; its coordinate space, point count and undefined constant-data case remain explicit. Sweeping a ruler changes the mathematics and earns nothing.

#### Voice walk

Held clicks, 120 ms presses, two-second main-path spacing, Sound on: equation tape, number tab, Read. Final log: **“Drag the 2 up or down.” once**, then **“y equals x squared. At x equals 1.000, y equals 1.000.”** as part of requested Read. Final scrollX, scrollY and page overflow are zero.

Side paths logged the NOAA dataset, 67 pairs, quadratic fit and ordinary-space R squared 0.9995; a rose Read says “sine”; a scrolled Manual Read supplies the visible sources. Sound-off Read works, and closing its drawer releases it for a new plotter Read. No automatic lesson or praise sequence was added.

| Line/action | Expected | Logged |
|---|---|---|
| Initial hint on relevant first tap | Once | Once |
| Main, data and rose Read | Current text on each press | Current text |
| Five Read presses and two quick presses | No stale queue or lost action | Audit clean |

Chrome is muted by the required driver. These are dispatch/log checks; audible quality and a recorded wise-mentor take were not auditioned. The permitted browser-speech fallback is active.

#### Facts checked

Live sources checked 2026-11-05. Data and licences are named in the Manual and draft metadata. Extracts, source responses and reproducible calculations are in `_scratch/graph-studio/data/review/`, `review-pack-check.py` and `review-reference.py`.

| Material/fact | Named source, licence and check |
|---|---|
| CO₂ annual means | [NOAA GML annual file](https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_annmean_mlo.txt), all 67 years 1959-2025, ppm to two decimals; [public-domain terms](https://gml.noaa.gov/about/disclaimer.html). Credits include GML, Xin Lan, Ralph Keeling and the early Scripps record. The Maunakea interruption is stated. |
| Planet measurements | [NASA individual fact sheets](https://nssdc.gsfc.nasa.gov/planetary/planetfact.html), eight rounded J2000 mean semimajor axes and approximate sidereal periods; US government work, public domain. Explicitly distinguish these from instantaneous distances and tropical periods. |
| Historical population | [Census 1910-2020 resident counts](https://www.census.gov/data/tables/time-series/dec/popchange-data-text.html) and [Statistical Abstract 2012 table 1](https://www2.census.gov/library/publications/2011/compendia/statab/131ed/tables/12s0002.pdf), one row per decade, rounded to 0.01 million; public domain. Earlier rows use the declared unrevised 1870 count. All 12 modern rows pass the independent packing check. |
| Computed fits and slopes | Original Curio Class mathematics, MIT, plus an independent Python solver: CO₂ line R² 0.9805554803 and quadratic 0.9994830149; planet exponent 1.4997021008; x² secant from 1 to 3 is 4. The spec's line value 0.981 uses three decimals; the instrument correctly shows 0.9806 at four. |
| Growth, e and crossings | [OpenStax College Algebra 6.1](https://openstax.org/books/college-algebra-2e/pages/6-1-exponential-functions), current [CC BY-NC-SA 4.0](https://openstax.org/books/college-algebra-2e/pages/preface), reference only; independent calculations give crossings -0.9371092012, 1.0775501500, 58.7701059379 and early Census growth about 3.015% per year. Preserve the builder's correct distinction between two positive crossings and three real crossings. |
| Kepler, roses, sinc and Lissajous | [NASA Kepler laws](https://science.nasa.gov/solar-system/orbits-and-keplers-laws/) and OpenStax astronomy; [MathWorld Rose Curve](https://mathworld.wolfram.com/RoseCurve.html) with OpenStax polar graphs; [Emory limits](https://mathcenter.oxford.emory.edu/site/math111/probSetLimits/) with OpenStax calculus; [MathWorld Lissajous](https://mathworld.wolfram.com/LissajousCurve.html) with [Wisconsin's museum](https://www.physics.wisc.edu/ingersollmuseum/exhibits/waves/lissajous/). NASA is public domain; current OpenStax is CC BY-NC-SA; the other pages retain author copyright. References only, no protected content imported. Sinc's hole is height 1 in radians and pi/180 in degrees. |

#### Sensitivity

The Census curve represents changing boundaries and enumeration coverage, not everyone in fixed modern boundaries. Early exclusions of many Indigenous people are now stated, checked against the [Census Bureau](https://www.census.gov/about/history/census-records-family-history/census-records/censuses-of-american-indians.html) and [National Archives](https://www.archives.gov/news/articles/native-americans-census), both public-domain government sources. A later cultural lens should inspect that wording and the declared historical count versions. There are no people images or claims about a whole culture.

#### Short test

- **Would a kid open it unassigned? Yes, plausibly:** glowing number tabs, reversible shape changes and rose curves invite immediate poking without instructions to clear.
- **Would an adult play for fun? Yes:** parameter families, the Lissajous/parabola connection, remote crossings and real-data fits sustain exploration.
- **Is the real thing the interface? Yes:** evaluated ink and measured data fill the paper; fitting now keeps them visible while adjusting the model.
- **Does it work with no score or finish line? Yes:** nothing judges or ends the session. These are review judgments, not participant-study results.

![Graph Studio beside Elements Inspector](../../_scratch/graph-studio/review-comparison-0.png)

#### Flattest moment left

Editing many end caps or a long column paste on a phone still needs internal scrolling. The frequent curve controls and first ruler remain available; the fit and its R² no longer disappear behind a dimmed editor.

#### Graphics

Exact canvas mathematics and CSS hardware; no raster art needed or added. Inspected the cold, before, verification, 18 exploration, final, proof, 33 audit and targeted-fix frames, including grayscale and both reference tools. Kept the paper, rail, carriage, ink weight and slide-rule cursors. Final bundle: **121,581 bytes**, one offline file. Exact `check_tools.py` validation functions pass in a Scratch fixture; its global rebundle was excluded to respect the folder boundary. All eight ink contrasts in notes exceed 4.5:1.

#### Audit

One audit only: `_scratch/graph-studio/review-audit/audit.md`, 530.859 seconds, Chrome 9931, host 8735. It completed with 60 leads, 33 inspected frames, no console errors, no infinite Motion-off animation, no lost focus across 23 held-click/Enter walks, clean Read repeats/quick presses and no resize exceptions or stuck controls.

Confirmed leads fixed: 40-pixel Load and the hidden first short-landscape ruler. Re-shot 680x425, 800x500, 1366x768 and 375x812 as applicable: Load is 44x44; the first ruler is fully visible and native arrows work. A subsequent focused root-overflow check gives zero horizontal/vertical page overflow at every required size.

Other leads are intentional: the quiet hint and measurement tags overlay paper; pointer-transparent tags fail hit-test coverage despite being visible. Drawers cover the underlying tape/paper by design. Manual references and optional editors scroll; closed details are not answer choices. The phone Add glyph has a 44-pixel target and an accessible name despite zero-sized replaced text. Hints disappear after action. The 20 missing-premise warnings apply a lesson welcome norm to a Curiosity with zero lesson modes; no premise was added.

The audit snapshot precedes the final compact-layout, target-width, root-overflow and visible-Manual-Read fixes. Their targeted evidence is in `review-auditfix/`, `review-scrollproof/` and `review-last-voice/`; no second full audit or polish round was run. Final hashes are in `review-final-manifest.json`.

#### Left open

- Physical Chromebook 60 fps, physical screen-reader operation and audible narration quality are unverified. Do not promote desktop checks into hardware claims. The bank clip is absent; recording was outside this run's ground rules.
- Numerical sampling, hole probes and feature finding remain approximate, as the Manual states. Direct trace/pins apply to equation-tape curves; fitted curves have their own readout and table. Inequalities and general implicit equations remain deferred by the spec's lean.
- Raw socket downloads were denied; live web-source inspection and preserved extracts supplied verification. One Chrome connection-loss batch was excluded and retried once in smaller batches. An early selector fixture failure and host favicon 404 were corrected, not counted as instrument failures.
- The drivers issued owned Chrome cleanup and servers shut down in finally blocks; independent local-port probes timed out, so they do not independently certify process state. No git commits, publishing or out-of-folder project edits were made.
- Some instantaneous file-read commands lacked an external hard-deadline wrapper. Bundles, browser batches and the audit used explicit 120-second, 300-second and 2400-second limits.

<!-- end part -->

## Refine

<!-- part: refine.md -->

OPEN (round 1, Claude Refine 2026-11-06; Codex fixes next)
Counts: blockers 0 (general 0, family 0), should fix 13 (general 6, family 7), polish accepted 17

### Refine: graph-studio

Curiosity No. 08. Merged from `refine/teaching.md`, `refine/play.md`, `refine/craft.md` (no sensitivity.md yet).
Frame folders, short names used below: T = `S:/CurioClass-codex-scratch/graph-studio/teaching/frames/`,
P = `.../graph-studio/play/frames/`, C = `.../graph-studio/craft/r1/`, A = `.../graph-studio/audit-r1/`.
Spot-checked in src.html by the integrator: items 1, 2, 3, 4, 5, 7, 8 and 12 (the cited code is as the lenses say).

#### Blocker
None. All three lenses pass the short test; no score, goal, level or finish anywhere.

#### Should fix
1. **Key points miss a zero where the curve touches the axis (a double root).** src.html:1050-1061 (`roots` only
   takes sign changes or an exact 0 sample) and 1091. `y = (x-1.3)^2` with Key points shows `1 turn (1.300,
   4.930e-32)` and no zero (T/t-squared-double.png); the default `y = x^2` finds its zero only because a sample lands
   on x = 0, so panning loses it. A vertex on the axis is the commonest grade 9 case. Fixed: a turn whose |y| is below
   a tolerance relative to the view is also marked as a zero, and its y prints as 0.000. (general)
2. **Negative bases with fraction exponents draw a wrong domain.** src.html:598 `Math.pow(a,b)` gives NaN for
   `(-8)^(1/3)`, so `y = x^(1/3)` draws only its right half while the Manual says blanks mean undefined. Misleads on
   domain, the anchor's F-IF.A.1. Fixed: when the exponent is a literal fraction p/q with odd q (written `1/3`, `2/3`;
   decimal exponents stay as now), take the real root; add one Manual line on it. x^0.5 losing
   its left half stays (correct). (general)
3. **Log axis titles say `log₁₀ x` / `log₁₀ y` while the ticks show x values.** src.html:983-984 against 961-962. On the
   planets plot "log₁₀ y" sits beside "100", read as log y = 100 (C/d4-planets-frame.png). Fixed: title stays "x" / "y"
   (or the data's unit) with "log scale" beside it. (family:curiosity)
4. **Key points make every redraw slow with several lines.** src.html:1093 and 1098-1105 (pairwise intersections at
   3,500 samples), run from `rebuildPaper` (1151) every dirty frame: scrub, pan, zoom and each frame of a playing ruler.
   Eight lines with Key points: 31 ms a redraw, a playing ruler at 33 ms frames (C/perf-play-eight-keys.png,
   perf-bench.png, perf-four-keys.png), so a Chromebook falls far below the 60 fps of Done when 1. Fixed: compute
   features when the pointer or ruler settles (or every few frames while animating), cache per view, and intersect the
   active line against the others rather than every pair. (family:curiosity)
5. **Pressing Read, Sound or Motion removes the first-run hint.** src.html:1735-1737 calls `dismissHint()` for any
   button. A student presses Read to hear the hint, hears it once, and the next Read says the fallback line (C/v5-sound-
   off-read.png, v6-read5-trace-off.png). Fixed: the power panel buttons (#read, #sound, #motion) do not dismiss the
   hint. (family:curiosity)
6. **Toggles announce element ids; the reset button's name is "0".** src.html:1433 announces `${id} on` ("angle on",
   "log-x on", "keypoints on", "square on"); #home (295) has only a title, so its name is "0" (C/a3-announce.png).
   Done when 9. Fixed: "Degrees" / "Radians", "Log scale on x", "Key points on", "Square grid on", and an aria-label
   such as "Reset axes to minus ten to ten". (general)
7. **Polar and parametric setups draw on unequal axes: circles are ellipses, roses squashed.** `r = 5` on the default
   view draws a 1.74:1 ellipse (P/33-circle-polar.png); the Rose curves and Lissajous setups (src.html:1629-1630) set
   -1.5..1.5 on both axes without Square (P/15-lissajous.png, A/size-1366x768.png). A kid counting petals sees them
   stretched. Fixed: those setups open with Square on; when the first `r =` or parametric line is typed while the view
   is still the default, switch to the square view (the toggle still turns it off). (family:curiosity)
8. **The ruler sweep ignores the ruler's step.** src.html:1187 moves `v.value` continuously, so the Rose setup (step 1)
   shows "a = 6.291" and an unclosed tangle that matches no petal rule (A/ animated-ruler state, P/14-rose.png).
   Words and state disagree. Fixed: when the step is whole or coarse, the sweep dwells on each step value (readout and
   curve on the step); fine steps sweep as now. (family:curiosity)
9. **Read says "y equals x squared .5" for `y = x^2.5`.** src.html:1698: `/\^2\b/` matches inside `^2.5` (and `^3\b`
   inside `^3.1`). Alt-scrubbing the exponent, the spec's first action, produces exactly these (T/t-read.png). Fixed:
   match `^2` and `^3` only when not followed by a digit or a decimal point. (general)
10. **The trace tag and the table say x twice.** Trace tag src.html:1223 reads "Pen 1 · x 1.000 | x 1.000 · y 1.000"
    (P/16-pins.png, 17-tangent.png, A/ trace state); Table header src.html:442 with 1561 reads "x | x | y"
    (T/t-table.png, P/20-table.png). Teaching rated these polish, Play should fix, Craft nit: settled as should fix,
    since every student sees both. Fixed: the parameter column and part appear only for polar and parametric lines;
    for an `f(x) =` line the tag uses the notation the anchor teaches, `f(3.000) = 9.000`, and the table header reads
    `x | f(x)`. (general)
11. **"x / y" under every equation reads as a quotient.** src.html:773 ("x / y", "y / x", "polar · t / r",
    "parametric · t / x / y") and the samples footer src.html:1176 ("x / y unitless"). Seen on every frame
    (P/01-default-pen-mid.png). Fixed: "in x · out y" (and "in t · out r", "in t · out x, y"), or "x → y"; same in the
    footer. (general)
12. **The Table drawer hides the rulers it says it follows.** src.html:163-169 (dialog 610 px wide, lower-left). At
    1366x768 it covers the whole tape, so a, b, k cannot be dragged with the table open; at 680x425 one table row shows
    (P/20-table.png, A/ live-table state at 1366x768 and 680x425). notes.md promises "an open table follows changing
    rulers". Fixed: the table drawer leaves the active line and its rulers visible (for example it sits beside the tape
    over the paper at 1366, and as a shorter bottom sheet at small sizes). Spec puts drawers over the tape; Done when 10
    and the notes' own promise settle that the active line stays usable. (family:curiosity)
13. **The pen is silent and draws only once; the carriage then hides under the power panel.** The spec's first two
    minutes promise a soft scratch while the pen draws (Sound on), and the Look has the carriage running to where the
    pen draws; the only sounds are the button and scrub ticks (src.html:892, 1738), and after the 1.2 s opening every
    typed or setup curve appears at once with the carriage parked at 95 percent of the rail (src.html:1200), behind
    #power at every size (P/01 vs 04, 14, 15; A/size-1366x768.png, size-680x425.png). Fixed: with Motion on, a newly
    typed, loaded or setup curve is inked by the pen with a quiet scratch (Sound on) and the carriage tracks the ink;
    scrubs and ruler drags stay instant (Done when 1); the carriage rests left of the power panel. Motion off: at once,
    no travel (Done when 9). (family:curiosity)

#### Polish accepted
1. **Fit readouts say the rate.** Data drawer foot: under an exponential fit also print the growth per x step ("× 1.030
   per year, 3.0 percent"), under a line its slope with units ("1.672 ppm per year"). The Manual's 3.0 percent fact is
   then readable on screen (T/t-co2.png). (general)
2. **R² in log space says so on the readout.** "R² 0.9897 (log space, not comparable with a line's)" instead of the small
   "(log)". (general)
3. **(1 + 1/n)^n entry.** The default ruler -10..10 reaches only 2.594 (T/t-e.png). One sentence in that "Things people
   have found" entry: set n's maximum to 1000. (general)
4. **Words on handles.** "Travel limits" becomes "Axes" (or "Window"); the "Notebook" handle reads "Setups · Notebook" so
   the roses, race, Lissajous and data are findable (P/19-notebook.png). Contents unchanged. "Ready for ink" may stay.
   (family:curiosity)
5. **Number tabs point at their numbers.** Hovering, focusing or dragging a tab highlights its digits in the equation
   (three "2" tabs on `y = 2(x-2)^2` are otherwise alike), and the drag slows to about 12 px a step (now 2 to 7 in
   32 px, P/02, 03). The tab's accessible name or title mentions Alt for tenths. (family:curiosity)
6. **The 2^x race opens showing its point.** The setup turns Key points on, and key-point labels near the paper's foot
   are placed clear of the tick numbers and the edge (P/07-race-keys.png, C/d2-race-keys.png). (family:curiosity)
7. **Read speaks for the ear.** Speak the trace point only while tracing (now it always says "At x equals 1.000",
   src.html:1721-1724, C/v6), and trim trailing zeros ("x equals 1, y equals 1"), as in the spec's example. (general)
8. **Projected sizes.** Tick labels, line labels and key-point labels 12 to 13 px at 1280 wide and up; the 10 px tape
   engraving, end-cap captions and samples footer up a step where they fit (src.html:76, 115, 155, 161). (general)
9. **`|x|` gets a helpful refusal.** "Use abs(x) for absolute value." instead of the generic grammar message.
   (family:curiosity)
10. **First tap on the 2 speaks the hint at once.** The tab's pointerup rebuilds the tape (src.html:892, 751-755), so no
    click fires and the hint waits for the kit's 1.5 s fallback (C/v1-repeat-number.png, d7-firsttap-click.png).
    Refresh the scrubbers in place on a tap without movement. (general)
11. **Units in readouts with data loaded.** Cursor "year 1992 · 371.7 ppm", the trace tag likewise, axis titles from
    the dataset's units (src.html:1335, 1223, 1175; C/d8-data-units.png). (family:curiosity)
12. **Paper focus ring visible.** The canvas outline is clipped by `#paper { overflow: hidden }` and the rail
    (src.html:62; C/a2-canvas-focus.png). Draw an inset outline or a focus frame inside the paper. (general)
13. **Pen numbers on the paper.** A small pen number at each curve's end, so close inks (green and teal, brown and
    orange) tie to their tape lines (C/d9-eight-lines-1366.png). (general)
14. **Exponent notation.** Ticks and key-point labels show `6.00×10^18`, not `6.00e+18`, on an instrument where e is
    2.718 (T/t-race.png); values within the tolerance of zero print 0.000. (general)
15. **Cursor readout before the pointer arrives.** Blank (or "x · y") instead of "x 0.000 · y 0.000". (general)
16. **760x900: the power panel covers "No. 08" and the carriage label** (A/size-760x900.png). Move one clear. (general)
17. **The aliasing warning sits on the "y" axis label** (P/10-alias.png). Place it clear of the label. (general)

#### Settled calls
- Duplicate x in the trace tag and table header: three levels across lenses; settled as one should fix (item 10).
- Pen scratch and pen travel: Play said should fix, Craft polish. The spec's first two minutes and Look promise both, so
  should fix (item 13), merged with Craft's carriage-under-panel polish. Scope kept to newly inked curves so live scrubs
  stay at 60 fps.
- Table drawer: the spec puts drawers over the tape; that layout stays for Data, Manual and Notebook. Only the Table
  drawer moves, because its own promise (following rulers) needs the rulers in view.
- Square view: only the polar and parametric setups, and a typed first polar or parametric line on the default view.
  Ordinary y lines keep the -10..10 view.
- Audit leads judged wrong by all three lenses, not to change: the first-run hint over #plot, trace and pin tags over
  #plot, drawers over the tape (except item 12), "hint out of view" after the first action, scrolling panels in the
  Manual and Data drawers, the 375 "+" icon button, the welcome cut by a first tap (BASELINE rule 16).
- Census note ("early censuses excluded many Indigenous people", Manual src.html:385-394 and notes.md, with the
  Censuses of American Indians link): not judged in this merge. It goes to the fresh-agent sensitivity review
  (BASELINE rule 5). Codex leaves the wording as is.
- No goal, score, challenge or finish was added anywhere in this list (CODEX-CURIOSITY.md).

#### To the spec's open questions
- **Module standards (rule 2).** Not exercised: F-IF.A.3 (sequences as functions, recursive; recursive definitions are
  refused today), F-IF.B.4 in context (Key points ignore data and fitted curves), F-IF.B.5 (domain in context). No small
  activity clearly fits without changing the spec. Options: a sequence form (`a(n) = 2a(n-1)`, `a(1) = 3`, dots on
  integer n with a table); Key points and Trace on the fitted curve ("when does the Mauna Loa quadratic reach 450
  ppm"); or move these codes to graph-story-lab or another module tool that teaches them in full. Lean: Trace and Key
  points on the fitted curve here (it is the instrument's own move) and move F-IF.A.3 and F-IF.B.5 to another tool,
  never a thin Manual entry.
- **Spec data list.** The spec's Census figures for 1940, 1970 and 1980 (132.16, 203.30, 226.54) are older values;
  notes.md and the bundle use the Bureau's current table (132.17, 203.21, 226.55), checked by Teaching. Update the spec.
- **`|x|` as grammar** (Play 13): accept bars for absolute value? Lean: yes, a later fix round; polish 9 covers the
  message now.

#### Not taken
- Race setup inset or second zoomed setup page (Play 10): adds a seventh setup; polish 6 covers the opening.
- Header row of pasted columns as axis names (Play 17): a nice new behaviour, not cheap; later.
- Domain-in-context "Things people have found" entry (Teaching 3): a thin activity for a code, which rule 2 forbids;
  see open questions.
- "Ready for ink" wording (Teaching 11): plotter flavour, harmless once the other words are plain.

<!-- end part -->

<!-- part: refine/craft.md -->

### Refine, Craft lens: graph-studio (Curiosity No. 08)

Round 1, 2026-11-06. Cold lens, judged against CODEX-CURIOSITY.md, VISION "Curiosities: the second shape",
STANDARDS and BASELINE. Bundle `tools/graph-studio/graph-studio.html` as built (not re-bundled). My frames and logs:
`S:/CurioClass-codex-scratch/graph-studio/craft/r1/` (shots `perf.json`, `v.json`, `d.json` beside it), Chrome on
port 9431, closed after. No host server started; the 375 frames are cited from the audit.

Counts: blocker 0, should fix 4, polish 7, nit 2.

#### Contract (clean)

- One file, 121,581 bytes (goal 2 MB). `performance.getEntriesByType('resource')` is empty after load and a full
  setup walk: no network requests. The Manual's source links are plain `target=_blank` anchors, not requests.
- No console errors, warnings or exceptions in 29 driven shots; the audit's resize-mid-action and Motion off rows are
  clean. `scripts/check_tools.py` lists it as a draft with no failure.
- No em dashes in src, bundle, notes or spec. "Curio Class" is never shortened. Lesson creep search: "points" appears
  only as "key points" and "data points"; no score, goal, level, sticker, finish or quiz. No welcome screen or kit header.
- Look rules: the paper fills the screen, the plate and Manual sit lower-left (src.html:305-310), Motion, Sound and
  Read sit on the plotter's own power panel (src.html:288-290), readouts are monospace. Kit used for voice, tones,
  Motion and Sound only (src.html:1726-1734), controls are the tool's own.
- Privacy is stated where pages are saved (src.html:353-354, 453). Art: `prompts.json` has no assets and the source
  has no `art:` tokens; everything is drawn in code, as a Curiosity should.
- Done when, craft side: 1 PASS (real drag on the exponent: 268 frames, median 16.7 ms, none over 20 ms;
  `perf-drag-exponent`), 3 PASS (`f(4) = 4.000`), 4 PASS (crossings 1.0776 and 58.7701, plus -0.9371), 5 PASS
  (line 0.9806, quadratic 0.9995), 6 PASS (`y = 1.000 x^1.500`), 7 PASS (`Δy/Δx = 4.000`, `d5-trace-pins-frame.png`),
  8 PASS (`d1-breaks.png`: tan and 1/x break, open circle at (0, 1)), 9 PASS with the naming gap below, 10 PASS on
  the audit's size frames, 11 and 12 PASS.

#### Findings

##### Should fix

1. **Key points make every redraw slow once there are several lines.** src.html:1098-1105 (pairwise intersections,
   3,500 samples per pair) and 1093 (turning points), run from `rebuildPaper` (1151) on every dirty frame: each
   scrub, pan, zoom and every frame of a playing ruler. Measured on a 32-thread desktop: one to four lines with
   key points on cost 2 to 3.5 ms per redraw and hold 16.7 ms frames; eight lines with key points on cost 31 ms per
   redraw and a playing ruler drops to 33 ms frames (92 of 119 over 20 ms, `perf-play-eight-keys`); eight lines with
   key points off cost 6.3 ms. On a school Chromebook (roughly 3 to 5 times slower) that is about 8 fps with key
   points and under 60 fps even without. Better: compute features only when the pointer or ruler settles (or every
   few frames while animating), cache them per view, and limit intersections to the active line against the others.
   How seen: `perf-bench`, `perf-play-eight-keys`, `perf-four-keys`. Tag: family:curiosity (the 60 fps rule).
2. **Pressing Read, Sound or Motion removes the first-run hint.** src.html:1735-1737 calls `dismissHint()` for any
   button click, including #read, #sound and #motion. A student who presses Read to hear the hint hears it once, the
   hint vanishes from the paper, and the next Read says "Type an equation, drag a number tab, or move a ruler."
   instead. The Curiosity rule is that the hint stays until the first action on the instrument and Read speaks it;
   the power panel is not that action. Better: skip `dismissHint` for the power panel buttons. How seen: `v5`
   (Sound then Read reads the fallback line), `v6` (five Reads: the first says the hint, the rest do not).
   Tag: family:curiosity.
3. **Toggles announce element ids, and the reset button is named "0".** src.html:1433 announces `${id} on`, so a
   screen reader hears "angle on" (meaning degrees), "log-x on", "keypoints on", "square on". #home
   (src.html:295) has only a `title`, so its accessible name is "0". Done when 9 asks every control to announce its
   value. Better: "Degrees" / "Radians", "Log scale on x", "Key points on", "Square grid on", and
   `aria-label="Reset axes to minus ten to ten"`. How seen: `a3-announce` (live region log). Tag: general.
4. **The log axis title says log₁₀ x while the ticks show x.** src.html:983-984 writes "log₁₀ x" and "log₁₀ y" as
   axis titles, but the tick labels are the values themselves (1, 10, 100; src.html:961-962). A student reading the
   planets plot sees "log₁₀ y" beside "100" and can take it as log y = 100. A readout that misleads. Better: keep the
   title "x" / "y" (or the data's unit) and mark the scale as "log scale". How seen: `d4-planets-frame.png`.
   Tag: family:curiosity (graphing readouts).

##### Polish

5. **The hint line comes 1.5 s late on a first tap of the 2.** The number tab's pointerup re-renders the tape
   (src.html:892 `renderTape()`, with the deferral at 751-755), so the button under the pointer is replaced and no
   `click` fires; the kit's first-tap decision then waits for its 1.5 s fallback. The 2 is the one control the hint
   names, so this is the tap most students make first. Logged: first tap about 1.25 s, hint spoken at 2.72 s (`v1`);
   `d7-firsttap-click` shows no click event at all. Better: refresh the scrubbers in place on a tap without movement
   instead of rebuilding the line. Tag: general.
6. **Read speaks a trace point that is not on the paper.** src.html:1721-1724 always adds "At x equals 1.000, y equals
   1.000." from `state.traceT`, even with the trace pen parked and no tag showing (`v6`, `tracing: false`). Numbers
   are spoken with four significant figures ("one point zero zero zero"), where the spec's example is "At x equals 3,
   y equals 9". Better: speak the point only while tracing, and trim trailing zeros for the ear. Tag: general.
7. **Readouts lose their units when data is loaded.** With Mauna Loa loaded the cursor reads "x 1992 · y 371.7"
   (src.html:1335), the trace tag "x ... · y ..." (1223) and the axes "x" and "y"; the unit is only in the 10 px
   footer ("year / ppm", 1175). The look rule asks for readouts with units. Better: "year 1992 · 371.7 ppm" and unit
   axis titles when a dataset is loaded. How seen: `d8-data-units`, audit `state-data-375x812.png`.
   Tag: family:curiosity.
8. **The pen carriage parks under the power panel.** After the opening draw the carriage stops at 95 percent of the
   rail (src.html:1200), which is behind #power (136) at every size, so the plotter's signature object is hidden at
   rest. Better: park it at the curve's last visible point left of the panel, or move the panel off the rail end.
   How seen: audit `size-1366x768.png`, `size-680x425.png`, `size-375x812 (iframe host).png`. Tag: family:curiosity.
9. **The paper's focus ring is mostly clipped.** The canvas outline (src.html:62) is cut by `#paper { overflow:
   hidden }` on the sides and covered by the rail on top, so a keyboard user sees one blue line along the bottom
   edge. Better: an inset outline or a focus frame drawn inside the paper. How seen: `a2-canvas-focus.png`.
   Tag: general.
10. **On the paper, colour is the only link from a curve to its tape line.** With several pens the inks pair up
    closely (green #2d6a3e and teal #116466, brown #7a4a1e and orange #a4480a) and no curve carries its pen number.
    Tracing names the pen, but only after a tap. Better: a small pen number at each curve's end on the paper.
    How seen: `d9-eight-lines-1366.png`. Tag: general.
11. **Sound is only a click tick.** The spec's first two minutes have the pen draw "with a soft scratch"; the only
    sounds are a 135 Hz button tick and a 160 Hz scrub tick (src.html:892, 1738), and only the opening draw animates
    the pen. Better: a quiet pen scratch while a redraw inks (after the first tap). Tag: family:curiosity.

##### Nit

12. The table header reads "x | x | y" for ordinary curves (src.html:442 with 1561). Name the first column
    "step" or drop it when the parameter is x. Tag: general.
13. Several labels are 10 px: the tape engraving, the plate, the end-cap captions, the samples footer
    (src.html:76, 115, 155, 161). Readable, but small on a projector. Tag: general.

#### Standard voice check

One line in `voice/lines.json`, "Drag the 2 up or down.", identical to `allLines()`. Driven with held clicks (0.12 s),
Sound and Motion on.

| line | kind | expected | spoken |
|---|---|---|---|
| "Drag the 2 up or down." (5 taps on the 2, 3 s apart) | welcome / how | once | 1 |
| Read (5 presses, 2 s apart) | read | 5 | 5 (the first with the hint, the rest with the fallback: finding 2) |

- First tap: Tab key, hint at once (`v4`); the 2, hint 1.5 s late (finding 5); the paper, a mode drawer, Zoom and the
  other buttons, no line, and the hint leaves the screen: allowed by BASELINE rule 16, the hint has done its job.
  Read speaks the hint only before the first action; Sound says nothing.
- Read: speaks with Sound off (`v5`); a drawer change after Read hushes it, as a mode change should.
- Stale lines: four taps 0.2 s apart (the 2, paper, Zoom in, Data) spoke nothing late (`v3`). Order: one line, nothing
  to reorder.

#### Sensitivity

The Census series notes (Manual, src.html:385-394; notes.md "Good to know") say early censuses excluded many
Indigenous people and link the Bureau's "Censuses of American Indians" page. Not judged here: flag for the
sensitivity agent (rule 5).

#### Audit pilot

- Leads confirmed: none that are faults. The #hint over #plot overlap and the trace and pin tags over #plot are the
  instrument's own labels, as designed.
- Leads wrong: "hint out of view" in every state (the hint is meant to leave after the first action); "keep region"
  for #plot and #equation-0 under the Manual, Notebook and Table drawers (drawers slide over the tape and paper by
  design, and the paper stays visible beside them at 1366); "choices cut short" in the Manual and Data drawers and the
  rose ruler's end caps at 680x425 and 375x812 (they scroll inside their panels and are reachable); "#add text under
  10 px" at 375 (an icon button drawn with `::after`, named "Add equation").
- Partly right: the held-click table marks the 2 as "heard"; it was heard, but 1.5 s late (finding 5).
- Missed: the key-point frame cost (finding 1), Read, Sound and Motion removing the hint (2), id-named announcements
  and the "0" button name (3), the misleading log axis title (4), the clipped canvas focus ring (9) and the carriage
  parked under the power panel (8).

<!-- end part -->

<!-- part: refine/play.md -->

### Play lens: graph-studio (Curiosity No. 08), round 1

Cold lens, 2026-11-06. Played twice: as a grade 9 student alone at home (nothing assigned, nothing read first) and as
a teacher projecting it at 1366x768. Judged against CODEX-CURIOSITY.md and VISION.md "Curiosities: the second shape",
plus POLISH.md and STANDARDS.md where they still bind.

My frames: `S:/CurioClass-codex-scratch/graph-studio/play/frames/` (shots1.json and shots2.json beside them, run with
`scripts/drive.py --port 9421`). Shared audit: `S:/CurioClass-codex-scratch/graph-studio/audit-r1/`.

#### Short test

- **Would a kid open it unassigned?** Yes, narrowly. The first action works with nothing read: drag the gold 2 and the
  bowl snaps to an S and a cliff (02-drag-exponent.png). Typing `a` makes a ruler at once (04-type-a.png). The pull
  that would hook a kid (roses, Lissajous, the 2^x race, real CO2) sits behind a button called Notebook (see item 8).
- **Would an adult play with it for fun?** Yes. It is a real grapher: f and g that call each other, f(4) = 4.000,
  polar, parametric, pins with average rate of change, tangent slope, key points, log axes, least-squares fits on real
  NOAA, NASA and Census data, paste your own columns. Planets on log-log give y = 1.000 x^1.500, R² 1.0000 (11-planets.png).
- **Is the real thing the interface?** Yes: the paper, the ink and the numbers are the whole tool. No decoration.
- **Does it work with no finish line?** Yes. No score, goal, level, sticker, quiz or finish screen anywhere; lesson
  creep is absent. The only first-run element is the quiet hint, gone after the first action.

Nothing here fails the short test. Depth a month of use would still find: yes (f/g composition, polar petals rule,
holes at removable discontinuities, the third 2^x crossing at -0.9371, log-space R² on the population series).

#### Findings

##### Should fix

1. **The Table drawer hides the rulers it claims to follow.** `src.html:163-169` (dialog 610 px wide, anchored
   lower-left). notes.md says "An open table follows changing rulers", but at 1366x768 the Table drawer covers the
   whole tape, so rulers a, b, k cannot be dragged while the table is open; at 680x425 it also covers the paper, with
   one table row visible. Seen: audit `state-live-table-1366x768.png`, `state-live-table-680x425.png`, my 20-table.png.
   Better: dock the table over the paper's right side (or under the active line), leaving the active line and its
   rulers in view. Tag: family:curiosity.

2. **Polar and parametric curves draw on unequal axes, so a circle is an ellipse.** Default view is -10..10 on both
   axes over a 1064x610 paper; `r = 5` draws a 1.74:1 ellipse (33-circle-polar.png). The Rose curves and Lissajous
   setups (`src.html:1629-1630`) set -1.5..1.5 on both axes without Square, so every rose is stretched sideways (audit
   `state-animated-ruler-1366x768.png`, my 15-lissajous.png). A kid counting petals sees squashed petals and a circle
   that is not round. Better: polar and parametric setups open with Square on, and typing an `r =` line could offer it.
   Tag: family:curiosity.

3. **The trace tag says x twice.** `src.html:1223`: for y = f(x) the tag reads "Pen 1 · x 1.000 | x 1.000 · y 1.000"
   (audit `state-trace-1366x768.png`, my 16-pins.png, 17-tangent.png). The parameter column only means something for
   polar and parametric. Better: "Pen 1 · x 1.000 · y 1.000" for y and x lines, the t part only when there is a t.
   Tag: general.

4. **The table header repeats x: "x | x | y".** `src.html:442` and `1561`, same cause as item 3 (my 20-table.png,
   audit `state-live-table-*`). A grade 9 student reads two identical columns and wonders what differs. Better: hide the
   parameter column unless the line is polar or parametric. Tag: general.

5. **"x / y" under every equation reads as division.** `src.html:773` labels each line "x / y", "polar · t / r",
   "parametric · t / x / y", and the sampling readout says "x / y unitless" (`src.html:1176`). In a maths tool a slash
   between letters is a quotient; under `y = x^2` "x / y" looks like a second expression. Seen on every frame (e.g.
   01-default-pen-mid.png). Better: "input x, output y", "x → y", or "in x · out y". Tag: general.

6. **The ruler sweep ignores its step, so the rose setup shows off-step values and broken roses.** `src.html:1187`
   moves `v.value` continuously. The Rose curves setup sets step 1 for petal counting, yet the sweeping ruler reads
   "a = 6.291" with step 1 (audit `state-animated-ruler-1366x768.png`, `-375x812.png`: "a = 6.333") and the curve is an
   unclosed tangle that matches no petal rule. Words do not match the state (POLISH, Consistency). Better: when the
   step is whole or coarse, the sweep dwells on each step value (or snaps the readout and curve to the step).
   Tag: family:curiosity.

7. **The pen is silent, and it only travels once.** The spec's first two minutes promise the pen drawing "with a soft
   scratch (Sound on)"; the only sounds are a click tone on buttons and a tick at the end of a scrub (`src.html:892`,
   `1738`). After the 1.2 s opening the carriage never draws again: typed or setup curves appear instantly, so the pen
   plotter that gives the tool its look stops being a plotter (01 vs 04, 14, 15 frames: carriage parked top-right). A
   flat moment exactly where the first reaction should land. Better: a short scratch while the pen inks a newly typed
   or loaded curve (Motion on), and the carriage tracking that ink. Tag: family:curiosity.

##### Polish

8. **The best material is hidden behind "Notebook".** Rose curves, the 2^x race, Lissajous, Mauna Loa and Planets
   live inside the Notebook drawer, a name that reads as "saved pages" (19-notebook.png). A kid exploring alone will
   try Data, Table and Travel limits before guessing that Notebook holds the fun. "Travel limits" is also plotter
   jargon a grade 9 student will not decode as "axis range". Better: a "Setups" handle (or a setups strip at the foot of
   the tape) and "Paper limits" or "Axes". Tag: family:curiosity.

9. **Number tabs are detached from their numbers.** `src.html:738` renders each number as a tab under the equation,
   labelled only with its value. `y = 2(x-2)^2` gives three identical "2 ↕" tabs with no clue which is which. Drag
   steps are whole units (2 to -2 in a 30 px drag, 03-drag-exponent-down.png; 2 to 7 in 32 px up, 02), so the spec's
   "drag it to 0.5 and half the curve vanishes" is unreachable without the Alt key, which only the Manual mentions.
   Better: highlight the matching digits in the equation while a tab is hovered or dragged, and slow the drag (about
   12 px a step). Tag: family:curiosity.

10. **The 2^x race opens with its point hidden.** The setup does not turn Key points on, and at its 6e18 scale the
    first two crossings sit on the bottom edge. With Key points on, three labels pile up over the x tick numbers at the
    foot of the paper and the -0.9371 label is half under the edge (07-race-keys.png). Better: open with Key points on
    and a small inset or a second setup page zoomed near x = 1. Tag: family:curiosity.

11. **Read speaks readout formatting, and a point nobody chose.** Read says "At x equals 1.000, y equals 1.000" (audit
    one-held-click row 10) even when the trace pen is off: it reads the default trace point. "One point zero zero zero"
    is hard on the ear. Better: speak trimmed numbers ("x equals 1, y equals 1") and only when tracing. Tag: general.

12. **Projected, the numbers are small.** Tick labels, line labels and key-point labels are 11 px monospace; from the
    back of a classroom at 1366x768 the axis numbers and "x / y" are hard to read (01, 08 frames). Better: 12 to 13 px
    ticks at 1280 wide and up. Tag: general.

13. **`|x|` is refused with a generic message.** "Use numbers, letters and the listed mathematical operators." Kids
    type bars for absolute value. Better: accept `|x|`, or say "Use abs(x) for absolute value." Tag: family:curiosity.

##### Nits

14. Cursor readout shows "x 0.000 · y 0.000" before the pointer has touched the paper (every frame); blank or "x ·
    y" until then reads truer. Tag: general.
15. At 760x900 the power panel covers "No. 08" on the rail label and the carriage label (audit `size-760x900.png`).
    Tag: general.
16. The aliasing warning sits on top of the "y" axis label in the paper's top-left corner (10-alias.png). Tag: general.
17. Pasted columns with a header row ("time distance") drop the header and the readout stays "x / y unitless"
    (41-paste). Using the header as axis names would be a small delight. Tag: family:curiosity.

##### Checked and fine

f(x) = x^2 - 3x then f(4) prints "f(4) = 4.000". Pins at x = 1 and 3 read Δy/Δx = 4.000. Tangent at x = 2 reads slope
4.000. Mauna Loa line R² 0.9806, quadratic 0.9995. Planets power exponent 1.500. tan(x) and 1/x break at poles;
sin(x)/x shows an open circle at (0, 1) (09-breaks.png). sin(1000x) shows the sampling warning. Zoom to ±6.5e6 and
±5.7e-11 stays sane. Motion off: the play button says "Motion is off. Turn Motion on to sweep a ruler." Enter adds a
line and moves focus. No console errors in 41 shots. The Manual's "Things people have found" already names the third
2^x crossing near -0.9371.

#### Audit pilot

- **Leads confirmed:** Table drawer covering the tape and rulers (`keep region #equation-0` in live-table): confirmed
  and reported as item 1. Ruler end caps cut by the tape scroll at 680x425 and 375x812: confirmed, but the tape scrolls
  and the cursor stays visible, so not reported.
- **Leads wrong:** "#plot / #hint overlap" at every size: the hint is meant to sit on the paper. "#plot / #trace-tag and
  #pin-tag overlap": the tags ride on the paper by design. "#add text under 10 px" at 375: an icon "+" button with an
  aria label. "Welcome not heard" after a first tap: allowed by BASELINE rule 16; the hint stays reachable by Read.
  Manual and Notebook covering the tape: drawers over the tape are the spec's layout.
- **What it missed:** circles drawn as ellipses on unequal axes (item 2), the duplicated x in the trace tag and table
  header (items 3, 4), the sweep ignoring the step (item 6), the silent one-shot pen (item 7), labels piling up in the
  race setup (item 10), and every word-level issue ("x / y", "Notebook", "Travel limits").

<!-- end part -->

<!-- part: refine/teaching.md -->

### Refine, Teaching lens: graph-studio (Curiosity No. 08), round 1

Cold lens, 2026-11-06. Judged against CODEX-CURIOSITY.md and VISION "Curiosities: the second shape", not lesson norms.
Bundle `tools/graph-studio/graph-studio.html` driven with `scripts/drive.py` (port 9411). My shots, frames and JS
probes: `S:/CurioClass-codex-scratch/graph-studio/teaching/shots.json` and `.../teaching/frames/`.
Shared audit: `S:/CurioClass-codex-scratch/graph-studio/audit-r1/audit.md`.

Counts: blocker 0, should fix 4, polish 5, nit 2. Sensitivity flag: 1.

#### Standards on the module (anchor math-9-function-notation-and-graphs: F-IF.A, F-IF.B)

| Code | Exercised by something the student does and sees? |
|---|---|
| F-IF.A.1 (function, domain, range) | Partly. Curves show where they exist, x = ... shows a non-function. No domain or range readout, and one domain is drawn wrong (finding 2). |
| F-IF.A.2 (notation, evaluate) | Yes. `f(x) = x^2 - 3x` then `f(4)` prints `f(4) = 4.000`; `g(x)=f(x)+1`, `g(-1)` prints 5.000 (t-fnotation). |
| F-IF.A.3 (sequences as functions, recursive) | No. There is no sequence form, and recursive definitions are refused ("Recursive definitions have no plotted value"). |
| F-IF.B.4 (key features in context) | Features yes (Key points: zeros, turns, intercept, intersections). In context, barely: Key points ignore data and fitted curves. |
| F-IF.B.5 (domain in context) | No activity relates a domain to a quantity. |
| F-IF.B.6 (average rate of change) | Yes, well. Pins on y = x^2 at 1 and 3 read `Δy/Δx = 4.000 · average rate of change` (t-pins). |

#### Findings

1. **should fix** · general · findFeatures/roots, src.html:1050-1061 and 1091. Key points miss a zero wherever the
   curve touches the axis without crossing (a double root). `y = (x-1.3)^2` with Key points shows `1 turn (1.300,
   4.930e-32)` and no zero at all (frame `teaching/frames/t-squared-double.png`). The default `y = x^2` finds its zero
   only because a sample lands exactly on x = 0; pan the paper and it goes. A vertex on the x axis is the most common
   grade 9 case, and the readout `4.930e-32` where the student expects 0 is confusing. Better: when a turn's |y| is
   below a tolerance relative to the view, mark it as a zero too and print 0.000. The Manual's "repeated roots can be
   missed" is honest but this is the textbook case, not an edge.

2. **should fix** · general · evaluate `^`, src.html:598. Negative bases with fractional exponents return NaN, so
   `y = x^(1/3)` draws only the right half (probe: `(-8)^(1/3)` evaluates to NaN). The cube root's domain is all real
   numbers; a student exploring domain (F-IF.A.1, the anchor) is shown a wrong one, on an instrument whose Manual says
   "undefined values are left blank", which reads as "undefined here". Better: when the exponent is a literal fraction
   with an odd denominator (or a `cbrt`/odd-root form), take the real root; or at least say in the Manual that x^(1/3)
   is drawn for x >= 0 only and why. (x^0.5 losing its left half, from the spec's first two minutes, is correct.)

3. **should fix** · family:curiosity · module standards. F-IF.A.3 has no activity at all, and F-IF.B.4 "in context" and
   F-IF.B.5 are not really exercised (table above). Rule 2 says a code on the module must be really taught. Options,
   any one per code: a sequence form (`a(n) = 2a(n-1)`, `a(1) = 3`, drawn as dots on integer n with a table), or the
   module lists F-IF.A.3 against another tool; let Key points (or Trace) run on the fitted curve, so "when does the
   Mauna Loa quadratic reach 450 ppm" or the population curve's features are readable in context; a "Things people
   have found" entry on domain in context (the planets data only exist for x > 0; a year axis has no meaning before
   1959 for this series). Spec already notes there is no plan.md and the tool is a second card beside graph-story-lab,
   so moving the code is acceptable.

4. **should fix** · general · Read, spokenEquation, src.html:1698. `/\^2\b/` matches inside `^2.5`, so Read says
   "y equals x squared .5" for `y = x^2.5` (vlog from shot t-read). Scrubbing the exponent with Alt gives exactly these
   decimals, so the spec's own first action produces a spoken equation that is wrong. Better: only match `^2` and
   `^3` when not followed by a digit or a decimal point.

5. **polish** · general · trace tag, src.html:1223. For an ordinary curve the tag reads `Pen 1 · x 3.000 | x 3.000 ·
   y 9.000`: x printed twice. For an `f(x) =` line this is the place to show the notation the anchor teaches:
   `f(3.000) = 9.000`. Better: drop the duplicate parameter for y and x lines; use the function's name when it has one.

6. **polish** · general · Table drawer, src.html:442. The header is `x | x | y` for ordinary curves (t-table), the
   same doubling. Better: two columns `x | y` (or `x | f(x)`) unless the line is polar or parametric.

7. **polish** · general · Data drawer, fit readout. Fitted equations print in centered form, for example
   `y = exp(5.886 + 0.004599 (x − 1992))` (t-co2). The spec's found fact "about 3.0 percent a year" for 1790 to 1860
   (I recomputed 3.02 percent from the counts, 2.995 percent from a log fit) cannot be read from this without
   computing e^0.0299 - 1 by hand. Better: under an exponential fit also print the growth per step of x
   ("× 1.030 per year, 3.0 percent") and for a line its slope with units ("1.672 ppm per year").

8. **polish** · general · Data drawer, R² readout. Line 0.9806, exponential 0.9897 (log), quadratic 0.9995 sit in
   the same slot. The Manual says log-space R² is not comparable, but a grade 9 student comparing fits will read
   0.9897 > 0.9806 as "exponential beats line". The "(log)" mark is small. Better: say it on the readout itself,
   e.g. "R² 0.9897 in log space, not comparable with a line's".

9. **polish** · general · Manual "Things people have found", `(1 + 1/n)^n`. The made ruler for n runs -10 to 10 (t-e),
   where the value reaches only 2.594; the approach to e is not visible unless the student finds the max end cap.
   Better: a Notebook setup or a sentence in that entry ("set n's maximum to 1000").

10. **nit** · general · axis ticks and Key point labels use JavaScript exponent notation (`6.00e+18`,
    `4.915e+17`, frame t-race.png) on an instrument where `e` also means 2.718. Better: `6.00×10^18`.

11. **nit** · general · words. "Travel limits" (the viewing window) and "Ready for ink" are plotter flavour a grade 9
    student will not decode; the Manual explains, so it is optional. "Window" in the Manual heading would help.

#### Sensitivity flag (not judged)

Manual "Sources and permissions" and notes.md "Good to know": "early censuses excluded many Indigenous people" and
the linked Censuses of American Indians page. Native content: send to the sensitivity agent (rule 5).

#### Done when, tested

- 1 PASS for the open (default `y = x^2`, hint "Drag the 2 up or down.", t-default); frame rate is Craft's.
- 2 Not tested by me; audit state animated-ruler is clean (no exceptions).
- 3 PASS: `f(4) = 4.000`.
- 4 PASS: crossings at 1.0776 and 58.77 (and -0.93711), race setup; my scipy roots 1.07755, 58.7701, -0.937109.
- 5 PASS: line R² 0.9806 (shows as 0.9806, rounds to 0.981), quadratic 0.9995; numpy agrees (0.98056, 0.99948).
- 6 PASS: planets power fit `y = 1.000 x^1.500`, numpy exponent 1.4997.
- 7 PASS: `Δy/Δx = 4.000`.
- 8 PASS: tan(x) and 1/x drawn with breaks, open circle at (0, 1) for sin(x)/x and at (3, 6) for (x^2-9)/(x-3)
  (t-holes.png).
- 9 to 12: Craft and Play; no score, goal, level or finish seen anywhere.

#### Facts checked against a second source

All match. NOAA file fetched 2026-11-06: 1959 315.98, 1960 316.91, 1975 331.13, 1990 354.45, 2000 369.71,
2010 390.10, 2020 414.21, 2023 421.08, 2024 424.61, 2025 427.35, and the Maunakea note (Dec 2022 to 4 July 2023).
Census popchange table: 1910 92.23, 1940 132.17, 1970 203.21, 1980 226.55, 2000 281.42, 2020 331.45 (so notes.md's
"corrected" values are right and the spec's are the old ones). NASA individual sheets: Saturn 9.537 AU and 10,755.7
days (29.45 yr), Neptune 30.07 AU and 60,189 days (164.8 yr). Recomputed: 3.0 percent a year 1790-1860, rose petal
rule, sin(x°)/x limit pi/180, 3:2 Lissajous. Every number on screen I checked has a named source and licence in the
Manual and tool.draft.json. No readout that lies apart from findings 1, 2 and 4.

#### Audit pilot

- Leads confirmed: none that bear on teaching.
- Leads wrong (for this lens): "hint out of view" in every state is the first-run hint correctly gone after an
  action; "choices cut short by a scroll panel" in the Manual is ordinary drawer scrolling; the hint/plot overlap is
  the hint sitting on the paper by design.
- What it missed: the double-root zero (1), the cube-root domain (2), Read's "x squared .5" (4), the doubled x in
  the trace tag and table (5, 6). All need maths or spoken-text checks it does not do.

<!-- end part -->

## Fix

<!-- part: polish.md -->

### Polish: graph-studio (Codex fix, round 1)

Curiosity No. 08. All 13 should-fix and 17 accepted polish items were reproduced or checked and observed fixed. No lesson flow was added. Work stayed in the two authorized folders; no commits or refine edits.

Evidence root: `S:/CurioClass-codex/_scratch/graph-studio/`. Unless stated otherwise, item frames are 1366x768. JSON beside each frame contains its measurements. `before3` uses the frozen original source to let the opening finish before reproducing the missing re-ink at every named size.

#### Blocker

None on the merged list.

#### Should fix

1. **FIXED, double roots.** A numerical turning point within a view-relative tolerance is also a zero; tolerance is capped at 1e-6 to avoid inventing roots in enormous windows. `(x-1.3)^2` now has both turn and zero at `(1.300, 0.000)` through three panned windows. A positive minimum remains positive. Before `before/s01-double-root`; [frame](../../_scratch/graph-studio/after/s01-double-root.png), `verify-a/numerical-regressions.json`, `audit-followup/bounded-zero-tolerance.json`.
2. **FIXED, fraction powers.** Parser metadata reduces literal integer fractions; odd denominators select the real root on negative bases in the shared evaluator. At -8: 1/3 gives -2, 2/3 gives 4; 0.5 remains undefined. Signed/reducible fractions and even denominators checked. Before `before/s02-fraction-domain`; [frame](../../_scratch/graph-studio/after/s02-fraction-domain.png). Manual and draft name both references and licences.
3. **FIXED, log titles.** Axes retain data units with “log scale”; ticks remain original coordinate values. Before `before/s03-log-labels`; [frame](../../_scratch/graph-studio/modes/setup-planets.png) and `after/s03-log-labels.json`.
4. **FIXED, redraw cost.** View/expression/parameter signatures cache features; input settles for 120 ms and ruler animation refreshes at 250 ms. Intersections compare the active pen with others. Identical cached eight-line redraw benchmark: 27.77 ms before, 3.25 ms after. Separate playing fixture: redraw 4.31 ms, steady frame mean 16.67 ms; maximum recorded interval including startup was 116.6 ms. `before/s04-eight-keypoints.json`, `after/s04-eight-keypoints.json`, [frame](../../_scratch/graph-studio/verify-a/cache-and-play-performance.png) and its JSON. These are this desktop's measurements, not Chromebook certification.
5. **FIXED, power buttons and hint.** Read, Sound and Motion preserve the first-run hint. Before `before/s05-power-hint`; [frame](../../_scratch/graph-studio/after/s05-power-hint.png), JSON `hint:true`, `hidden:false` after all three held clicks.
6. **FIXED, names.** Announcements are “Degrees”, “Radians”, “Log scale on x/y”, “Key points on” and “Square grid on”. Reset has its explicit axis-reset aria-label. Before `before/s06-announcements`; `verify-a/announced-control-names.json`, [frame](../../_scratch/graph-studio/verify-a/announced-control-names.png).
7. **FIXED, equal scales.** First polar/parametric ink on the untouched default window switches to Square; rose and Lissajous setups start square and contain the whole shape. Circle physical scale ratio: 1.7414 before, 1.0000 after. [frame](../../_scratch/graph-studio/after/s07-polar-square.png), `edges/first-polar-param.json`, `modes/setup-rose.png`, `modes/setup-lissajous.png`. Ordinary y input keeps its original default window.
8. **FIXED, sweep steps.** Coarse steps dwell on their min-anchored lattice; fine sweeps retain continuous travel. Rose samples changed from 4.583…6.708 to whole 5, 6, 7. A -2..8 ruler with step 3 stayed on 1 and 4. Before `before/s08-ruler-step`; [frame](../../_scratch/graph-studio/after/s08-ruler-step.png), `edges/ruler-lattice.json`.
9. **FIXED, fractional spoken exponents.** Squared/cubed matches exclude following digits, decimal points and scientific-literal continuations. 2.5 reads “to the power 2.5”; 3.1 reads “to the power 3.1”. Before `before/s09-fraction-speech`; `after/s09-fraction-speech.json` and the 34-check numerical run.
10. **FIXED, duplicate parameters.** Ordinary table/trace coordinates appear once. Named functions use `f(3.000) = 9.000` and `x | f(x)`; polar/parametric tables retain t, x, y; vertical equations use y, x. Before `before/s10-trace-table`; [frame](../../_scratch/graph-studio/after/s10-trace-table.png), `verify-a/numerical-regressions.json`.
11. **FIXED, input/output words.** Tape and desktop footer use “in x · out y”; polar/parametric forms name their input and outputs. Compact phone footer uses the accepted arrow notation. Before `before/s11-flow-labels`; [frame](../../_scratch/graph-studio/after/s11-flow-labels.png) and final phone footer frames.
12. **FIXED, live Table placement.** Table sits beside the tape at 1366 and 680, and above the tape at 375. The ruler is unobscured at all three sizes and changes the first result from 25.00 to 50.00. At 680 several rows now show. Before `before/s12-table-wide` and `before2/s12-table-680`; [frame](../../_scratch/graph-studio/edges/table-live-1366.png), [frame](../../_scratch/graph-studio/edges/table-live-680.png), [frame](../../_scratch/graph-studio/edges/table-live-375.png), matching JSON.
13. **FIXED, ink and carriage.** Typed curves, setups, fitted ink and loaded notebook pages restart a 1.2 s pen pass. Visible ink begins without spending the opening on off-screen segments. Live scrubs/rulers remain instant. Real held setup clicks started one quiet scratch source (gain 0.009), moved the carriage 524→380 px, then stopped it; Sound off started none and Motion off drew instantly. Before `before2/s13-pen-*` and `before3/s13-reink-*`; `after2/s13-reink-*`, [frame](../../_scratch/graph-studio/verify-b/pen-audio.png), `verify-b/pen-audio.json`, `target/typed-curve-ink.png`, `edges/saved-page-reink.json`. Rest clearance is 18 px at 1366x768, 680x425, 760x900 and the 375x812 iframe: `polish-final/pen-rest-*`.

#### Polish accepted

1. **FIXED, fit rates.** Census 1790–1860 exponential readout gives ×1.030 per year, 3.0 percent; NOAA line gives 1.672 ppm per year. [frame](../../_scratch/graph-studio/after2/p-data-fit.png), [frame](../../_scratch/graph-studio/verify-b/fit-line-rate.png). Independent decimal recomputation is in `independent-numbers.json`.
2. **FIXED, log R².** Both fit summary and result state “log space, not comparable with a line's”. `after2/p-data-fit.png/json`.
3. **FIXED, e entry.** Manual says to set n's maximum to 1000. Actual ruler setup reaches 2.716923932…; [frame](../../_scratch/graph-studio/polish-final/manual-e-1000.png) and JSON.
4. **FIXED, handles.** “Axes” and “Setups · Notebook”; contents retained. [frame](../../_scratch/graph-studio/sizes/default-1366x768.png) and all size frames.
5. **FIXED, number tabs.** Hover/focus/drag highlight the matching digits; a 24 px real drag changes the middle 2 by two steps. Native Tab focus selects character 8; moving the pointer away retains its highlight. Alt gives tenths and appears in the name/title. [frame](../../_scratch/graph-studio/verify-a/scrub-highlight.png), `polish-final/hover-token.json`, `polish-final/focus-token-keyboard.json`, [frame](../../_scratch/graph-studio/target/focused-token-persists.png).
6. **FIXED, race opening.** Setup enables Key points. Bottom labels lift clear of ticks and the edge; both positive intersections show, near 1.078 and 58.77. [frame](../../_scratch/graph-studio/verify-b/race-key-labels.png) and `modes/setup-race.png`.
7. **FIXED, Read for the ear.** Trace values are spoken only during tracing; “x equals 1, y equals 1” has no padded zeros. `verify-a/voice-walk.json`.
8. **FIXED, projected type.** At width 1280 and above, ticks, curve pen numbers, key labels and tape line labels are 12 px; engraving/end-cap captions/footer are 11 px and numeric end caps 12 px. `polish-final/font-readouts.json`, `modes/setup-parabola.png`, [frame](../../_scratch/graph-studio/polish-final/eight-pen-labels.png).
9. **FIXED, bars refusal.** `|x|` says “Use abs(x) for absolute value.” [frame](../../_scratch/graph-studio/edges/absolute-value-message.png).
10. **FIXED, first tap.** A tap retains its number node through click, so the hint starts at once. At 0.1 s after the held tap, before vlog was empty; after vlog already contains one spoken hint at 1371 ms. `before2/p05-number-tap.json`, `after2/p05-number-tap.json`.
11. **FIXED, data units.** Native pointer movement produces “year 1992 · 371.7 ppm”; trace and axis labels likewise carry the bundled units. [frame](../../_scratch/graph-studio/verify-b/units-co2.png) and JSON. Planets use AU and Earth years.
12. **FIXED, paper focus.** Inset 3 px outline, offset -4 px, visible on all four paper edges after actual Tab/Shift-Tab. [frame](../../_scratch/graph-studio/sizes/paper-focus.png) and JSON.
13. **FIXED, pen numbers.** All eight curve ends have their tape pen number. [frame](../../_scratch/graph-studio/polish-final/eight-pen-labels.png).
14. **FIXED, exponent notation.** Ticks show `6.00×10^18`, feature/readout exponents use ×10^ notation, and the double-root zero prints 0.000. `verify-b/race-key-labels.png`, `after/s01-double-root.png`.
15. **FIXED, initial coordinates.** Cursor output is blank until pointer movement. All eight `sizes/default-*.json` contain an empty cursor; native movement is checked in the data-units case.
16. **FIXED, 760x900 overlap.** Compact rail caption is omitted; carriage parks clear of power and the maker's plate remains intact. [frame](../../_scratch/graph-studio/sizes/default-760x900.png), `polish-final/pen-rest-760.png` (18 px clearance).
17. **FIXED, alias warning.** Warning sits below the y title, retaining the title and its own text. [frame](../../_scratch/graph-studio/edges/alias-focus.png) and `after2/p-focus-alias.png`.

#### Settled calls

- Applied the merged trace/table item once (should fix 10) and the ink/scratch item once (should fix 13).
- Data, Manual and Notebook keep their drawer layout; only Table moved over paper to keep the tape usable.
- Square changes are limited to polar/parametric default input and those two setups; ordinary y defaults stay unchanged.
- Hint/tags over paper, a dismissed hint after action, intentional drawers and internal Manual/Data scrolling stay. Phone Add keeps its plus icon.
- Census sensitivity wording is unchanged. There is no sensitivity.md; the fresh sensitivity review and module-standards moves remain the integrator's open questions.
- The Curiosity brief wins over lesson norms: no welcome screen, goal, score, level, quiz, finish or kit header was added.
- Unattended choices followed the list's lean: Axes, Setups · Notebook, paper-side Table, 12 px scrub steps, and coarse lattice dwells.

#### Cheats tried

- No score/check/quiz exists to pass. Mathematical counterexamples were used instead.
- Double root under three pans: still found; a nearby positive minimum did not become zero. A huge 6×10^18 y window prompted a tolerance cap; the positive minimum 1 stays 1 and has no zero in the final follow-up.
- Odd/even, signed and reducible literal fractions, decimal approximations, and 0^0: correct real values or undefined; 13 domain cases pass.
- Coarse ruler on a non-dividing step (min -2, max 8, step 3): every observed value stayed on its lattice.
- Pins at x=1 and 3 on x² give 4.000; coincident pins give undefined. Empty input, poles, sinc hole, 1000x oscillations and 1e99x stayed responsive; no false hole at the poles. `verify-a/numerical-regressions.json`, `polish-final/extreme-instrument.json`.

#### Voice walk

Held clicks at roughly 2 s gaps: number tab, Read, Read, Trace, Read. Vlog shows one automatic “Drag the 2 up or down.” at 1360 ms; explicit Reads repeat the current hint at 3487 and 5627 ms; after Trace, Read at 9908 ms includes “At x equals 1, y equals 1.”
The fractional exponent path reads “y equals x to the power 2.5”. Read/Sound/Motion retain the hint. Audible recordings are absent; muted Chrome telemetry verifies starts/text and cancellation, not a physical speaker audition.
`voice/lines.json` equals `allLines()`: one fixed line. The audit's five-click and quick-tap checks for Number, Motion and Read are clean. A first tap may cut/skip the hint under BASELINE 16.

#### Engine changes wanted

None. Kit files were unchanged; scratch uses the kit's audio context and Sound/Motion state.

#### Audit

One full audit, port 9921, host 8725, hard 40-minute limit, completed. All 33 audit frames were inspected. Its 23-control walk has no errors, focus loss or unintended control jumps; repeat/quick Read checks are clean; Motion off and resize checks are clean.
Two confirmed layout causes were corrected after that single audit: Next is now at least 44×44 at all eight required sizes, and phone sampling is one line clear of controls. All follow-ups are in `audit-followup/`; no second audit or lens run was made. The audit is the pre-follow-up snapshot.
Every lead, including individual first-tap welcome leads, is answered in [audit-dispositions.md](../../_scratch/graph-studio/audit-dispositions.md). Intentional drawer coverage and the established hint/tag treatment were retained per Settled calls; ruler end caps use internal tape scrolling while the frequent-use slider stays visible.
Final bundle: 136,489 bytes. Scoped repository check functions report no errors. The site-wide check command was not run because it bundles other tools; its actual checker functions were applied to a Scratch copy with draft metadata. No external resource entries in the tested offline/default/data paths; no em dashes. Lesson search hits only mathematical points, sample points and their code variables.

#### The real material

- No datasets were downloaded or changed. Exact original arrays were compared; hashes and independent calculations are in `independent-numbers.json`. New data gathering time was zero.
- NOAA GML: all 67 annual means, 1959–2025, ppm; retained source check dated 2026-11-05. Public domain under [GML's disclaimer](https://gml.noaa.gov/about/disclaimer.html); [annual means](https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_annmean_mlo.txt). Independent line slope 1.671965839 ppm/year, R² 0.9805554803; quadratic R² 0.9994830149.
- US Census Bureau: unchanged decennial counts rounded to 0.01 million, retained versions/coverage notes. US government work, public domain; [Historical Population Change](https://www.census.gov/data/tables/time-series/dec/popchange-data-text.html) and [Statistical Abstract 2012](https://www2.census.gov/library/publications/2011/compendia/statab/131ed/tables/12s0002.pdf). The 1790–1860 subset's fitted annual factor is 1.029950249, 2.9950249 percent.
- NASA: unchanged eight rounded J2000 semimajor axes and approximate sidereal periods, AU/Earth years; public-domain US government data; [planetary fact sheets](https://nssdc.gsfc.nasa.gov/planetary/planetfact.html). Original sampling and Saturn rounding retained.
- Rational-power convention rechecked 2026-11-06 against [OpenStax College Algebra 2e 1.3](https://openstax.org/books/college-algebra-2e/pages/1-3-radicals-and-rational-exponents), current CC BY-NC-SA 4.0, and independent [MathWorld Cube Root](https://mathworld.wolfram.com/CubeRoot.html), copyright Wolfram Research. References only: no restricted text, images or datasets copied. Parser implementation, drawings and synthesized scratch are original Curio Class code under MIT.
- Growth and the e limit use the existing OpenStax chapter 6 reference, current CC BY-NC-SA 4.0, without copied content. `(1+1/1000)^1000 = 2.716923932…` is independently recomputed. Named sources/licences are in the Manual and tool.draft.json.

#### Frames looked at

All produced PNGs in `before/`, `before2/`, `before3/`, `after/`, `after2/`, `verify-a/`, `verify-b/`, `sizes/`, `modes/`, `edges/`, `polish-final/`, `target/`, `fix-audit/` and `audit-followup/` were inspected through labeled contact sheets; the named root, domain, log, circle, table, focus, race and phone follow-up frames were also opened directly where needed. The 1366 regression run covers all six setups and five drawers. Eight default sizes, grayscale and keyboard frames are retained. Beat Lab and Elements Inspector were opened/used as the permitted material/density references; frames are in `polish-final/`.

#### Left open

- No merged blocker, should-fix or accepted polish item remains open. Spec open questions and Census sensitivity review are unchanged; this report is not the fresh exit verdict.
- School Chromebook hardware, physical screen readers and audible speech/scratch audition were unavailable. The initial maximum frame interval is reported above; no universal 60 fps guarantee is claimed. Browser audio requires a user gesture, so initial pre-gesture ink is silent.
- Initial read-only discovery commands lacked hard timeouts; the recursive inventory was interrupted. Subsequent shell work uses explicit subprocess limits (120 s bundle, 300 s drive, 2400 s audit).
- A test batch initially overlapped the preceding Chrome shutdown and failed its connection; it was retried as smaller serial batches. An early host favicon 404 was removed. Completed product batches have no console errors. All owned test Chrome/server processes have ended.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Graph Studio build handoff

The source is one readable HTML file: instrument CSS and semantic drawers, then parser, tape controls, paper transforms, adaptive sampling, numerical features, input, regressions, tables, notebook and kit voice integration. The bundle inlines kit/curio.js and the optional voice bank map. No raster art or external libraries.

The parser uses bounded recursive descent with operator binding powers; no typed text is evaluated as JavaScript. f and g definitions are looked up separately, circular definitions stay undefined, and evaluation has a fuel limit. Curve coordinates share the same evaluator as table and trace. Least squares uses normalized x before solving small normal systems. Data and fits retain full precision; readouts round. Numeric scrubbing has separate keyboard and precision-drag paths; tape rebuilds wait for a held pointer to release.

Native typing keeps the equation input node in place. `reconcileRulers` updates only its dependent rulers; number tabs update separately. `addLine` retains the new target index across focus restoration. These details matter: replacing the focused input during a trusted input event lost focus in Chrome, and restoring the old input changed the active index during Enter. Both were found and verified with actual CDP text input, not only direct state assignment. Decimal and scientific literals retain their scrubbing precision.

Adaptive refinement has a budget for each pixel segment so a difficult region cannot consume the whole page's refinement budget. Hole probes are numerical at zero and literal constants, not a general symbolic limit system. Key features currently cover ordinary y curves. A fit uses a centered basis in its printed equation; the full-precision function is retained separately. Exact round halves go away from zero; 0^0 is undefined.

Tables remember start and step per pen and can also sample the fitted curve. Square uses axis coordinates, including base-ten decades on log axes. Direct tracing and pins currently operate on equation-tape curves; data fits have their own readout and table.

The report records spec discrepancies. Independent build evidence lives only in _scratch/graph-studio/. No other tool or shared engine was modified. The original build and review reports are historical; see polish.md for the Claude Refine fix round.

#### Engine changes wanted

None required. The existing kit's emoji power labels are restyled locally to the plotter's simple lamps. Curio.voice handles speech and Read priority.

#### Next review

Check keyboard and real-pointer numeric scrubbing, oscillation alias warnings, large-coordinate numerical features, mobile tape scrolling, and source-data fit discrepancies. General implicit equations and inequalities are explicitly deferred by the spec. Notebook is browser-local and storage errors are reported without erasing the current page.

#### Cold review changes

The one-pass review keeps the plotter surface and eight inks. Measurements now sits over the tape with a collapsible columns editor, so fitting leaves the data visible. Drawers use native modeless dialogs: Read remains usable, Escape closes the drawer, and Close restores its handle. The live table updates with parameter edits. Its choices preserve the current selection when recomputed.

Hole probes check approach on both sides at four distances, preventing symmetric poles from posing as finite holes. This remains numerical evidence, not a symbolic proof. Aliasing warnings inspect trigonometric argument ASTs with current parameter values; the warning stays visible in compact views. Live announcements retain the last value after rapid input. Empty ruler bounds and subnormal paper limits are refused explicitly; more than 1,000 data pairs preserves the previous data. Notebook restore refreshes data-source labels too.

Dragging a pin within six paper pixels of the other pin on the same curve snaps their parameters together, so an apparently coincident pair cannot retain a spurious tiny denominator. Table opens directly on an existing fit if the active pen has no curve, starting at the first measurement. Drawer transitions stop an obsolete Read; data Read names the actual dataset and fit, and equation Read expands function names for the ear. Bounds are guarded during pan, zoom and square-grid resize as well as form submission.

Current primary-source checks corrected Census 1940, 1970 and 1980, Saturn rounding, the MathWorld rose link and OpenStax's licence. Manual and draft metadata name versions, measurement units and permissions. No reference text or figures from restrictive licences are bundled. Reproduction and verification evidence is under _scratch/graph-studio/review-*; the builder's report remains historical.

#### Sensitivity

The historical Census series excludes many Indigenous people in early enumerations and changes geographic coverage. The Manual now states that plainly and cites the Census Bureau. A later cultural lens should check that wording and ensure no one interprets the curve as all people in fixed present-day boundaries. Census and National Archives explanations were checked independently. No people imagery is present.

#### Review verification

Independent review checks passed 45 numerical/data cases and 35 extreme-input cases. Native point dragging, coincident-pin dragging, numeric scrubbing and keyboard rulers were checked separately. The 18 completed exploration segments total 10.390 minutes; one failed Chrome connection run is excluded. The single audit completed in 530.859 seconds on port 9931 with host 8735, producing 33 frames and 60 leads. Its 23-control walk, repeat/quick Read, Motion off and resize checks had no console errors or stuck controls.

Confirmed audit faults were Load at 40 pixels wide and a clipped first ruler in the short landscape preview. Load is now 44 pixels; compact tape navigation, an inline number row and a compact ruler keep the first slider visible. Targeted re-shoots cover 680x425, 800x500, 1366x768 and the 375x812 iframe. A later root/live-region overflow guard gives zero page overflow at all eight required sizes. The Manual's Read follows its visible paragraphs when scrolled. No second audit was run: review-audit is the pre-layout-fix snapshot, and review-auditfix plus review-scrollproof are the final targeted evidence.

No recorded clip, audible audition, physical screen reader or school Chromebook was available. These remain verification limits, not claims of tested hardware. All produced code and metadata remain local and draft.

#### Claude Refine fix round 1

See polish.md and _scratch/graph-studio/ for numbered before/after frames and measurements. The original source snapshot is retained in Scratch. Literal rational exponent metadata is attached once by the parser, shared by plot, trace and table. Feature signatures include the view, expressions, parameters and active pen; idle input waits 120 ms, animated rulers refresh at 250 ms. New ink restarts a 1.2 second drawing pass with a bounded carriage and a short synthesized scratch through the kit audio context. A real user gesture activates browser audio. Motion and Sound stop the scratch immediately.

Table uses two columns for ordinary functions, three for polar and parametric ink, and is placed over paper so rulers remain available. Hover, focus and scrubbing highlight the numeric token inside the existing input without replacing the input. A tap keeps its button until click reaches the voice controller. Census sensitivity wording and spec open questions remain unchanged. No shared engine changes, external messages, uploads or commits.

#### Fix audit follow-up

The single fix audit completed with 83 mechanical leads and 33 inspected frames. Its 23-control walk, repeated/quick Read, Motion off and resize checks were clean. Most leads describe the settled hint/tag and drawer geometry. Confirmed layout faults were a 40 px Table Next button and a wrapping phone samples footer; local min-width and compact one-line readouts address them. Targeted follow-up frames at all eight table sizes and three phone footer states are in _scratch/graph-studio/audit-followup. The audit itself remains the pre-follow-up snapshot; no second audit was run. Turning-point zero tolerance is capped at 1e-6 so enormous y windows cannot turn a positive minimum into a zero.

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

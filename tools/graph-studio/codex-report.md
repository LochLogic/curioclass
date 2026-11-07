# Codex report: graph-studio (Curiosity No. 08)

## Built

A working mathematical pen plotter, with cream engineering paper filling the working area, a metal rail and carriage, equation tape, eight pen inks, hairline slide-rule cursors and a brass measurement tag. The lower-left Manual and maker's plate read Curio Class Curiosities · No. 08 · Graph Studio. Motion, Sound and Read occupy the plotter's own power panel.

The instrument supports the listed arithmetic and elementary functions, implicit multiplication, f and g definitions and evaluations, vertical equations, movable points, polar and parametric curves, automatic rulers with animation and editable bounds, pan, wheel/pinch zoom, equal axis spacing, log axes, degrees/radians, tracing, pins, secants, numerical tangents and key features. Tables remember start and step per pen and also tabulate fitted curves. Data has all three bundled datasets, pasted columns and four least-squares fit families. Notebook has six setups and four browser-local save slots. A read-only URL hash can preload an expression.

One offline bundle: 110,927 bytes (108.3 KiB), below the spec's 400 KB target and the 2 MB goal. Data is under 3 KB. No image, library, font or data downloads are needed. Draft metadata remains draft; nothing was published or committed. This was Build with verification fixes, with no polish round.

Choices made unattended: inequalities and general implicit equations stay out, as the spec leans; URL hash preload is included. No plan.md was made, as specified. No lesson frame, sequence, reward or finish was introduced. The report was written last because the user's report-and-stop instruction overrides the machinery's early-report suggestion.

## The real material

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

## Break the instrument

- Final functional suite: 19 of 19 passed, including precedence, implicit multiplication, every named elementary function, definitions, real-domain failures, polar/parametric/vertical forms, holes, intersections, secants, tangents, regressions, per-pen tables, fitted tables, notebook serialization, tiny nonzero values, eight pens and empty input.
- Trusted browser text input created a ruler while preserving equation focus, typed f(x) followed by Enter and f(4), and produced f(4) = 4.000. Native keyboard scrubbing preserved decimal and scientific precision: 0.10 to 0.11 and 1e3 to 3e3. An Alt precision drag changed x² to x^0.5, with the negative branch undefined and f(4) = 2.
- Whole-pixel jittered pointer tests moved a ruler to -10, dragged a pin along x² and moved an ordinary point. Coincident pins print undefined; a corner has no fabricated tangent. tan(x) and 1/x have breaks; sin(x)/x has an open circle at (0, 1).
- Unsafe syntax, excessive nesting and recursive definitions are bounded. No typed expression enters JavaScript evaluation. Empty data clears the fit; an invalid row keeps prior data and names its row. Logged fits reject nonpositive data and constant data have undefined R². Oversized measurement columns request rescaling.
- Four real Save clicks and a later Load verified all four slots. Storage stays on this device and the Notebook says so. No account, upload or transfer code.
- 10.52 minutes of qualifying exploration across 14 bounded segments: 5.26 minutes from the grade-9 perspective and 5.26 from the adult perspective. Parabolas, roses, Lissajous figures, widely separated crossings and all four fit families were varied. An early fixture that assigned a fit without redraw was excluded and replaced. These are automated agent explorations, not observations of actual children or an adult user study.
- Sampled desktop Chrome frame intervals had median 16.7 ms and 95th percentile 16.7-16.8 ms. This supports about 60 fps on this test machine; no school Chromebook was available.

Evidence: ../../_scratch/graph-studio/ui-walk/results.json, reference.json, exploration-summary.json, functional-results.json, final-checks frames and the audit folder. Build fixes addressed native-input focus, the Enter target, held-pointer stability, readout overlap and uniform refinement budgets.

## Voice walk

wise-mentor is selected in voice/lines.json. No recordings were generated, as required; Curio.voice uses the supported browser-speech fallback. The one bank line is “Drag the 2 up or down.” There are no automatic teaching or praise sequences.

Held clicks at a two-second pace on the main path logged the hint once, then Read's current equation, trace and pin text. The side path used Sound off, a rose setup and Read; Read still supplied current text. Ordinary actions did not repeat the hint or queue stale narration. Current readouts also use native labels, values, output elements and a polite live region. The recorded bank voice itself was not auditioned because the clip does not exist; test Chrome was muted.

## Short test

These are judgments after the bounded exploration, not user-study results.

- Would a kid open it unassigned? **Yes, plausibly:** the opening pen makes a curve immediately, changing a number changes its shape, and a letter makes a physical ruler. There is no reading gate.
- Would an adult use it for fun? **Yes:** parameter families, rose curves and Lissajous figures invite play; regressions, log axes and measurements give real reasons to keep using it.
- Is the real material the interface? **Yes:** the ink is evaluated mathematics, pins measure its coordinates, and measurements determine the fitted curve. No painted data or simulated success.
- Does it work without a score or finish line? **Yes:** the working state persists as an instrument page. It never evaluates the person using it.

![Graph Studio beside Beat Lab](../../_scratch/graph-studio/comparison.png)

The comparison uses a live typed equation and ruler beside Beat Lab in use. Elements Inspector, Span and Spire and Pocket Universe were also opened and used before design. The shared marks were adopted; their palettes and scenes were not copied.

## Lesson creep check

The source and voice lines were searched case-insensitively for score, points, level, goal, sticker, badge, correct, wrong, try again, complete and well done. Only “points” remains: 11 occurrences describing mathematical/data points, key points and an internal points array. None is a reward. Every other search term has zero hits. No em dashes occur in the produced source, bundle or metadata/notes. The original spec was not edited.

## Done when

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

## Audit leads

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

## Frames looked at

All captured instrument frames were examined individually or on labelled contact sheets, with flagged views opened full size. Evidence folders: models (all four references), first, checks, mobile, late, final-checks, exploration, ui-walk, audit and audit-fixes, all under ../../_scratch/graph-studio/. The comparison PNG was also inspected. Default, grayscale, phone iframe, both pointer and keyboard paths, every setup family, drawers, poles, holes, labels, fits, pins, Motion off and audit resize states are covered.

## Art made

No painted assets. Canvas draws all mathematical material; CSS draws the paper, rail, carriage, tape, clear hairline rulers, power panel and engraved plate. art/prompts.json has an empty asset list. Screenshots and the comparison are evidence only and are not bundled into the instrument.

## Engine changes wanted

None. Shared kit, scripts, docs, other tools and git history were not changed. All implementation work is confined to tools/graph-studio/ and its specified Scratch folder.

## Left open

- School Chromebook performance and actual screen-reader operation were not tested on that hardware. Desktop Chrome measurements and native semantics are evidence, not substitutes for those checks.
- A recorded wise-mentor clip is absent; the permitted browser fallback is configured, with dispatch/queue behavior verified in muted Chrome. Audible quality was not verified. First-load drawing is silent until a user gesture permits sound; controls then use quiet kit tones.
- Numerical sampling can alias, hole probes are not symbolic limits, and closely spaced or repeated features can be missed. Key-feature finding currently covers explicit y curves. Direct tracing/pins use equation-tape curves; fitted curves have their own readout and table. These limits are documented rather than presented as exact symbolic algebra.
- Inequalities and general implicit equations are deferred by the spec's lean. No lesson plan, publication, commit or polish round was requested or performed.
- One parallel Chrome connection reset was retried in smaller serial checks. Earlier test-fixture issues and the native typing failures were corrected and the successful evidence retained. All owned Chrome/server processes were closed.
- The initial workspace/brief read returned in 0.17 seconds before the hard-deadline wrapper was installed; later shell commands had explicit limits. The report was generated only after verification so its creation can be the requested stopping point.

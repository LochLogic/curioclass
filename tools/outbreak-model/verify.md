FIX (1 blocker, 5 should fix, 6 nits)

# Verify: outbreak-model (2026-10-25)

Checked cold against spec.md, POLISH.md, VERIFY.md, BATCH-G11.md and docs/families/graphing.md. Draft bundle (`CURIO_DRAFT=1`, 375 KB with the 9 recorded clips). Frames and console errors came from my own headless Chrome harness (error capture injected into the page, DOM dumps for state, iframe host page for 680x425, 800x500, 1000x625, 760x900 and 375x800). Everything is in my scratchpad. No console errors in any normal run; the only error I saw is the blocker below.

## Numbers (all recomputed in Python, all match the spec and the screen)

- Rumor to 1,000: 16.7616 h (base 2, 10 and e agree). Virus X to 1 million: 49.8289 days; day 49 = 825,702, day 50 = 1,040,319. Viral post to 1 million: 51.6124 h. Fading rumor to 10: 38.2193 days. Steady spread to 1 million: 55.2620 days.
- Virus X: k = 0.231049, W = 9.9658, times 1.25992 a day, up 25.99 percent; 1 thousand to 1 million = 29.8974 days = 1 million to 1 billion; 2 to the 20 = 1,048,576, log2(1e6) = 19.93.
- Ceilings (a = 10, D = 3): Denver 48.380, Colorado 57.417, United States 74.947, World 88.726 days; logistic half-K times equal these to 4 decimals. Steady Virus X to 1 million: 384,728 days (notes say "about 385 thousand").
- Solve cards on screen: 49.83 x3, 38.22 x3, 16.76 x3, 51.61 x3, 55.26 x3; calculator lines check (3 x 5 / 0.30103, 9.9658 x 5, 11.513 / 0.23105).
- Populations: US 331,449,281 confirmed on the Census 2020 apportionment press release (it is the resident population; the page is the apportionment release, so the label is fine). UN page confirms 8 billion on 15 November 2022. Denver 715,522 and Colorado 5,773,714 match the 2020 Census figures I know, but QuickFacts returned 403 and the Census API needs a key, so I could not load them live. Unsure on those two only in that sense.

## Findings

1. **Blocker. Toggling Linear/Log during an animated zoom hangs the page or freezes the graph.** src.html:427-431 (`labY`/`gridY` read `state.scale`) with kit/graphing.js:133-137 (step functions re-evaluated on every frame). A story change, place change, quick target button, typed target or target drop starts a 650 ms `g.view` animation. If Log is pressed inside that window, the step functions already return 1 (log units) while the animated y range still spans millions to billions, so `drawGrid` tries to make one SVG line per unit. Seen two ways with a rAF-to-setTimeout shim (headless does not run rAF; a real browser does): Hit the ceiling, pick Denver, press Log at once gives `RangeError: Invalid array length` at the grid `steps` loop, `viewBusy` never clears, and every later view change is ignored (range stuck at [0, 102] x [0, 7e8] after further target changes). Viral post, then Log at once: Chrome hung for over 2 minutes and had to be killed. Fix idea: make the step functions depend on the range they are given, not on `state.scale`, or switch scale only after the view settles; the engine could also cap lines per axis.
2. **Should fix. Guess first leaves the answer readable on the graph.** Ask when, Guess first on (frame f_guess): the Solve panel is covered, but the curve still visibly crosses the target line at day 50, the trace dot can be dragged to it, and for a far target the window right edge is t x 1.2 (windowX at src.html:472 ignores `answerVisible()`). POLISH: "Nothing on screen gives the answer away" in a predict mode. Hide or clip the curve past the target (or the crossing region) until the answer is shown, and do not widen the window from the hidden answer.
3. **Should fix. Solve cards print "Infinity" and "0 / 0".** k = 0 and target equal to a (Done-when 7 case): all three cards show steps like "10 · 2^(t/Infinity) = 10", "t = Infinity · log(1) / log 2" and "= 0 / 0 = 0.00" (renderSolve, src.html:880-919, D = LN2 / k with k = 0). The message line is right ("The target equals the start, so t = 0"); the cards should be skipped or replaced for k = 0.
4. **Should fix. Model controls are below the fold in the 16:10 embed.** At 680x425, 800x500 and 1000x625 (compact layout) the panel shows Play/Pause/Reset, Linear/Log and the Target or Place box first; Story, Describe growth by, Start (a) and the rate slider are only reached by scrolling the panel (frames z_grow_680, z_ask_800, z_grow_1000). Batch rule: controls visible without scrolling. At 1000x625 Story shows but the sliders do not.
5. **Should fix. Legend text is too small in small boxes.** Measured at 680x425: legend text box 10.1 px tall (about 8 px type), versus tick labels 14.3 px; the same at 375 px wide (frame z_ask_375) and at 800x500. The `--ts` boost reaches ticks and labels but the legend still renders tiny. "cases" and "time (days)" titles are borderline at 375.
6. **Should fix. A target below 0.01 is reported as "less than 0.01".** a = 1, k = -0.5, target typed 0.001: the answer says "Falls to less than 0.01 cases on day 13.82" and the target label says "target: less than 0.01", while the Solve cards correctly solve for 0.001 (`wordsShort`, src.html:372). Show the actual target (0.001) in answer and label.
7. Nit. "Reaches 1,000 students who heard it on hour 16.76" (answerSentence, src.html:851): "at hour 16.76" reads better; "on day 49.83" is fine.
8. Nit. "The exponential is past United States's 331 million people" (src.html:755): "the United States'" or "past the population of the United States".
9. Nit. Numbers at or above 10 to the 15 print with a caret in plain text: answer "Reaches 1.0 × 10^15 cases" and target label "target: 1.0 × 10^15" (words text mode). The counter uses a real superscript; the answer and label could too.
10. Nit. The target box (9em) shows only part of a 19-digit number such as 1,000,000,000,000,000.
11. Nit. With a small shrinking target the answer label "t = 13.82 days" sits on the x tick labels ("30" shows through it; frame f_ext2).
12. Nit. Read speaks the hint text with the browser voice; the three hint texts are fixed sentences that could be recorded like the 9 lines (POLISH: recorded speech beats any browser voice).

## Checked and fine

- Done when: 1 (49.83 in all three columns; Check it stops the clock at 49.83 and the counter at "1.00 million = 1,000,000"), 2 (path data identical across Doubling/Tenfold/Continuous; D 3, W 9.97, k 0.2310, up 26.0 percent), 3 (38.22; 2,100 and PageUp to 2.1 million say "Never" and show the negative formula t), 4 (log line straight; gaps 9.97, 29.90 per three decades), 5 (US day 74.95, shaded and hatched, labeled, logistic levels under K), 6 (covered until pin moved and Show pressed, no score), 7 (k = 0 "Never. No growth", target = a gives t = 0, below a "Already past", "abc" message keeps the old target, "1e6" and "2,000,000" accepted, 0 and -5 refused with the spec sentence), 8 (Motion off: Play, Check it and zooms instant), 9 (no images, no network requests in the bundle, no em dashes, "Curio Class" only, made-up label on the story card).
- Story presets, units, givens and default targets match the table; milestones light with ✓ and gap column; steady line and column; "off the chart" arrow; logistic equation with numbers; window widens to t x 1.2 for far targets and caps y at 10 to the 12.
- Voice: lines.json bank/voice/style per batch rule, 9 lines word for word identical in spec, lines.json and `L`/`allLines()`, all under 110 characters; 9 clips bundled.
- Art: prompts.json has no assets and the tool uses no `art:` tokens. Guardrails: neutral health framing, every story marked invented, no celebration.
- Colors are never the only signal (dashes on steady and logistic, hatching on the shaded region, ▸ and "(main)" on the main description). Buttons measured 44 px at 680x425; handle hit areas 46 px.
- No horizontal scroll at any size; 375 px stack layout readable apart from finding 5.
- kit/graphing.js change: backward compatible. Number steps still work, default labels still `Plane.fmt`, `trace` keeps its old defaults, `point` already had `hit`/`setHit`. Tick and axis text now live in their own group, so a tool's own labels-layer items survive `g.view` (documented in docs/families/graphing.md, "Changing ranges"). rollercoaster-polynomials (uses the labels layer, never calls `g.view`) and imaginary-island (calls `g.view` for zoom) both rebundled and ran through every mode, plus imaginary-island Zoom in x2, Zoom out x2 and Fit, with no console errors; text counts return to the same values after Fit (no duplicated labels). Frames of both look normal. The engine does not guard against a step function that returns a very small step for the current range (finding 1).

## Not verified / unsure

- Real pointer drags (I used keyboard events and the `__tool` helpers), sound and voice playback (not listened to), screen reader output.
- Headless Chrome does not run requestAnimationFrame here, and its screenshots sometimes show stale button colors and graph scale; I checked button states and ranges in the DOM instead and used a setTimeout shim to emulate rAF. The motion-on view animation therefore was tested with that shim, not in a real visible browser.
- I rebundled rollercoaster-polynomials and imaginary-island (their .html bundles are regenerated, sources untouched). Nothing fixed, nothing committed.

## Re-verify (2026-10-25)

FIX (0 blockers, 2 should fix, 4 nits; 11 of the 12 earlier findings fixed, 12 still open)

Cold re-check on a fresh draft bundle (379 KB) with my own CDP harness (console errors and exceptions captured per run). Real requestAnimationFrame runs in this headless Chrome (62 frames a second measured), so the zoom was tested both natively and with a setTimeout shim. Narrow and 16:10 sizes went through a same-origin iframe host on localhost.

### Earlier findings

1. **Blocker, fixed.** I could not re-break it. Runs: Hit the ceiling, Denver then Log at 0, 20, 100, 300, 500 and 640 ms, then World then Linear at the same delays. Viral post then Log at 0, 50, 300 and 600 ms. Story change in Grow with Linear/Log/Linear 30 ms apart. Typed 1e15, 2,000 and 0.001 each followed by a toggle mid-zoom. All three quick buttons, each followed by a toggle. Handle PageUp then Log. Mode switches with toggles inside each zoom. 11 random fuzz runs of 150 to 200 actions each (mode, scale, story, place, quick, typed targets including "abc", k = 0, -0.5 and 2, Guess first, Play) with random 0 to 700 ms gaps at 375, 680x425, 800x500, 1000x625 and 1400x900, plus one with Motion off. No exception and no hang. The longest main-thread gap was 23 ms. The most grid lines ever seen was 76. The view always settled to a sane range for the current scale, and later view changes still applied (for example Viral post, Log, then typed 1e12 moved the range from [1, 8] to [1, 15], and a story change still moved it). Two things make this work: the engine guard in `drawGrid` (kit/graphing.js:138-141, MAX_LINES 400) and range-based step functions (src.html:444-447). A newer `view()` cancels the running one (kit/graphing.js:373-377).
2. **Should fix, fixed.** With Guess first on, the curve is drawn only up to the clock (empty at day 0), the trace dot is hidden and the off-chart arrow is suppressed. For a far target the window now only doubles: 1e12 gives [0, 240], not t x 1.2 = 131.6 (frame f2_guess_far). The remainder is nit N5 below.
3. **Should fix, fixed.** k = 0 with the target equal to a: the message reads "The target equals the start, so t = 0. With no growth (k = 0), N stays at 10 the whole time." and the cards are empty. k = 0 with target 1000 reads "Never. No growth ...". No "Infinity" and no "0 / 0".
4. **Should fix, fixed.** At 680x425, 800x500 and 1000x625 (compact) the panel now shows Play/Pause/Reset, Lin/Log, Story, Double/Tenfold/Rate, Grow/Shrink, Start a (268 to 312 px) and the rate slider (318 to 362 px) without scrolling. The remainder is nit N6 below.
5. **Should fix, fixed.** Legend text height against tick label height: 16.8 vs 13.8 px at 680x425, 15.2 vs 14.5 at 800x500, 18.6 vs 16.6 at 1000x625, 17.6 vs 14.6 at 375.
6. **Should fix, fixed.** a = 1, k = -0.5, target 0.001: "Falls to 0.001 cases on day 13.82.", label "target: 0.001", cards 13.82 x3.
7. Nit, fixed. "Reaches 1,000 students who heard it at hour 16.76."
8. Nit, fixed. "The exponential is past the population of the United States."
9. Nit, fixed. "Reaches 1.0 × 10¹⁵ cases on day 139.52.", label "target: 1.0 × 10¹⁵".
10. Nit, fixed. The box is now 13.5em and shows all of 100,000,000,000,000 (scrollWidth equals clientWidth). Targets above 1e15 are refused with "Pick a number up to 10 to the 15 (1e15)."
11. Nit, fixed. a = 1, k = -0.5, target 0.001: the answer label spans y 413.6 to 431.6 and the x tick labels start at 444, so they no longer overlap.
12. Nit, still open (as the builder said). Read still speaks the hint text with the browser voice (src.html:1152-1158). lines.json still holds the same 9 lines, word for word equal to `allLines()`.

### New findings

- **N1. Should fix. Console errors from the trace dot at fast rates.** kit/graphing.js:313 writes the point transform with `v.toFixed(1)`, which switches to exponent form at 1e21 and above. In Grow, set D to 0.5 days, W to 1 or k to 1.5 with the real sliders and press Play. The y window caps at 10 to the 12, so the trace dot runs far above it: transform="translate(512.0,-5.85e+27)" (D 0.5), "-5.37e+30" (k 1.5), "-4.40e+51" (W 1). Chrome logs "Error: <g> attribute transform: Trailing garbage" up to about 50 times in one Play (runs tr_D, tr_k, tr_W, tr_on). Nothing shows on screen, because the dot is hidden when it is off the plot, but the run is not clean. Clamping the pixel value in the engine, or not moving a hidden point, would stop it.
- **N2. Should fix. Horizontal scroll at 680x425.** The document is 685 px wide in a 680 px frame (25 px too wide at 660). HEADER, MAIN and the panel all end at 685. Cause: src.html:42 `body.compact header{...flex-wrap:nowrap}`, so the title, the three mode tabs and Motion/Sound/Read cannot wrap. It is the same in all three modes. 700 px and wider are fine.
- N3. Nit. Log tick labels below a millionth use exponent notation: "1e-8", "1e-10", "1e-12", "1e-14" (decadeWords, src.html:404-406, `String(+...)`). Seen with Viral post, Shrink, Tenfold, Log, Ask (frame fuzzN_5_1000).
- N4. Nit. When the target sits at the top of the log window (Viral post shrinking, target 10 million, y range [-15, 7]), the target label is clamped onto the line itself, so the line strikes through "target: 10 million" (src.html:583, same frame).
- N5. Nit. With Guess first on, Play is still enabled. Running it draws the curve through the target crossing, and the counter ticks past the target day, so the covered answer can be read off before a guess is placed (frame f2_guess). This may be intended, but it works against "Nothing on screen gives the answer away".
- N6. Nit. At 680x425 in Ask when, the Target number box (424 to 468 px) and the quick buttons sit just below the fold. Only the "Target" heading shows. The on-graph target handle is still in view. In Hit the ceiling the Place select is cut at the bottom edge but can still be used.

### Kit change: other tools

rollercoaster-polynomials and imaginary-island rebundled (CURIO_DRAFT=1; plain bundling skips them because of tool.draft.json). I ran every mode of both at 1000x625 and 375x800, with native rAF and with the shim. Then imaginary-island Zoom in x2, Zoom out x2 and Fit, then six alternating zoom clicks 40 ms apart and Fit. No console errors and no exceptions. Text element counts were the same before and after zooming (55, 55, 55), so no duplicated labels. The frames look normal.

### Not verified

- Real pointer drags (keyboard and `__tool` helpers only), sound and voice playback, screen reader output.
- Nothing fixed and nothing committed. All frames and run scripts are in my scratchpad (rv folder).

# Codex report: fair-dice-investigation

## Built

- Offline Grade 12 statistics mystery: three ordered cases and Dice lab. Uses the kit frame, 9-12 theme and Curio.voice.
- Seven new painted assets, the retained café backdrop, adaptive canvas charts, interruptible seeded rolls, expected-cell dragging, slope inference, shuffles and simulation history.
- All files are inside the tool and its Scratch folder. No commits, branch changes, kit edits, audio recording or polish round.

## Numbers check

- Scratch setup.py, numbers.json and strategies.py independently recompute the supplied arithmetic with NumPy/SciPy.
- Worked counts: χ² 17.16, p 0.00420614; contributions 8.41, .16, .16, .01, .01, 8.41. Fair-looking 60: χ² 1, p .96256577.
- Case 2: columns 115, 88, 81, 76; expected 38.3333, 29.3333, 27, 25.3333; χ² 14.39680828, df 6, p .02550441. Largest contribution 6.40289855, Castle seat 1.
- Weight: slope .28496503, SE .05620169, t 5.07039939, p .000484545, interval (.159739857, .410190213). Temperature: slope .00118881, p .780529823, interval (-.008064795, .010442417).
- Critical values, normalized weights, noncentral power, multiple testing rates, binomial spreads, residual summaries and contrasts match the spec's rounded arithmetic.
- Independent 20,000-run estimates vary from the spec's particular simulation: fair rates ranged .0443 to .0539, not its .047 to .052. Loaded power ranged .07665 at n 30 to .9615 at n 1,000. No fixed result is substituted for simulation.
- Independent 10,000-case strategies: equal allocation .435; 150 then leader .4702; 100 then fixed leader .410; adaptive 1,200 .5762, 1,500 .6528, 2,000 .7196. The 5,000-shuffle extreme fraction was .0008, versus the spec's .0006. Both are stochastic variation.
- Contrast: brand/panel 5.62:1, brand/section 5.33:1, brand/paper 6.38:1, dark ink/brand 5.89:1, card/felt 10.54:1.

## Feel check

- Played the full real-input path through all three cases, including wrong-cell and temperature-decoy feedback, then compared fair and loaded simulations.
- Best moment: the 1,000-dot field changes from a few false alarms to roughly four fifths flagged, and the student's case closes with their evidence filed.
- Flattest moment 1: native drag did not register reliably. Replaced it with a moving total chip and pointer-capture drop handling. Real drags now build the expected count.
- Flattest moment 2: compact plots compressed into almost flat strips. Reclaimed readout space, reduced tick density and reserved scatter/residual height. Also gave a six-row lab history an adaptive dot strip.
- Opened and bundled both bar tools in Scratch. feel-comparison.png places the 1366x768 evidence view beside Beat Lab. The painted felt, resin dice and paper readout have comparable visual weight without mimicking its palette or interaction.

## Done when

1. PASS: goodness API reproduces the worked example, exact contributions and displayed p .0042; functional.json.
2. PASS: real-input expected cells build, Fill the rest unlocks after three, only Castle seat 1 closes the case; verification.json and table frames.
3. PASS: actual regressions reproduce slope .2850, t 5.07, p ≈ .00048 and (.160,.410); decoy p ≈ .781. Four-place p readouts retain a separate precision note for the tiny slope p.
4. PASS: checked 1,000-run fair share .048 and loaded share .797; a separate UI loaded run .796. These satisfy the requested bands.
5. PASS: tests below 30 refused; 13 requests for Roll 100 stop at exactly 1,200; Accuse stays live. Two wrong accusations reveal four true distributions and open Case 2.
6. PASS: at 1366x768 and 1000x625, face bars, winning-seat table, scatter/residual chart and share-flagged chart dominate their stages; full sweep and targeted frames.
7. PASS: interrupted roll kept 28 completed rolls, then exactly 10 on the other die. Shuffle tab changes and lab slider changes cancel the draw immediately; no delayed stale result.
8. PASS: the complete real-input path saved all three cases and the first evidence snapshot through reload. Clear restored no solved cases and a 1,200-roll budget.
9. PASS with focused post-audit checks: all required sizes shot once, affected sizes rechecked. Held clicks, keyboard activation, grayscale and Motion off checked. A host fixture favicon 404 was removed from the subsequent phone checks; the actual offline tool made no HTTP requests.

## Wave lessons

- PASS, Hint and voice: current hints update before narration; Read read the exact live hint; first roll acts immediately. How lines use Curio.voice and stale checks. The audit found no errors or lost repeated events in its 2-second tap checks.
- PASS, Focus and layout: static controls stay mounted, no focus taken on load, dialog focus returns with preventScroll, hint space reserved. The final focus checks return to pick2 after closing Case 2, point-cell after filling, and next-case or m-lab on closure.
- PASS, Sizes: full eight-size sweep, including 375x812 iframe, then targeted compact/table/plot/lab corrections. The repaired phone Cases button and all six sliders measure at least 44 pixels in each target dimension.
- PASS, No giveaways: hidden die index stays in the closure until a case closes; names and artwork do not signal loading. True probabilities appear only after accusation.
- PASS, Honest numbers: each test names H₀, df, expected counts and α; simulation results identify false alarm rate or power and their assumptions.
- PASS, Standards: students perform goodness of fit and homogeneity for U8, and both slope tests and intervals for U9. No family engine applies.
- PASS, Motion off: tumble and idle-light loops explicitly stop. Roll accounting and 650 ms roll duration remain the same.
- PASS, Short choices: dice, decision/citation buttons, totals and lab settings are visible; long help and logs may scroll. Full-size and targeted phone frames were inspected.
- PASS, Resize mid-animation: charts redraw from state; controls are not rebuilt and pending animation state is retained or canceled by its owner.
- PASS, Welcome timing: no welcomeAfter. The first Roll is declared as speaking later and skips a stale welcome. Case briefings delay the welcome until the student returns to evidence.
- PASS, Unknown as unknown: untested statistics, unbuilt expected counts and the initial lab share show question marks.
- PASS, One look, one meaning: dashed line always means expected counts; filled versus outlined lab dots mean flagged versus not flagged.
- PASS, Badge truth: case stamps reflect either a solved file or the two-error evidence limit; non-rejection never claims the die is proven fair.
- PASS, Reversible hints: mode, plot, n, α and weight changes replace the hint immediately.
- PASS, No answer by copying: students compare contributions and inferential results; briefing text does not identify the loaded die or largest cell.

## Audit leads

One full audit completed on port 9981 with host 8785: 26 leads. It found no exceptions, no stuck disabled controls on resize, no infinite animation with Motion off, and clean five-click, 2-second narration checks. The full audit predates the final repairs and was not rerun.
- FIXED, 5 alpha-label leads: replaced font-size zero text with a hidden redundant span and a visible alpha symbol. The select retains its accessible name.
- FIXED, 1 phone target lead: Cases is at least 44 by 44 pixels. All six phone sliders now have 44-pixel hit heights too.
- FIXED, 4 dialog-return focus leads: reject a saved body or nonfocusable opener, then return on the next frame to a visible control or the active case card. Real clicks and Enter twice now end on pick2.
- FIXED, 3 Fill the rest focus leads: capture focus before disabling the button, then move it to Point to the cell. Verified active id point-cell.
- FIXED, 2 phone table-heading overlap leads: recovered header room and tightened the formula row. The measured briefing bottom is 140 and table top is 143, with zero overlap.
- INTENTIONAL, 2 briefing hint/keep leads: the modal covers the background hint and makes the background inert. The dialog has its own readable, focusable text and an always-visible Back to evidence control.
- INTENTIONAL, 4 first-welcome leads on Roll 1/10/100 and Test: STANDARDS requires the first action's own line or animation to skip a stale welcome. The premise is visible in the opening briefing; Test gives its own under-30 instruction.
- FIXED, 1 late Accuse welcome: the welcome becomes invalid on accusation or closure, and the action hushes stale speech. Seed 7's first Accuse logs only the closed event.
- FIXED, 1 Enter-twice focus lead: capture the active button before it disables and focus Next case or Dice lab afterward. Enter twice through the next briefing now leaves focus on pick2.
- FIXED, 3 quick-tap welcome-cut leads: tapping the current mode or current case no longer hushes it. Real repeated Cases, case-card and Dice lab taps log one welcome without a cut.
- Additional focused repairs: honest-die reaccusation is refused without spending the second attempt; wrong cell selection stays in pointing mode; closed Case 3 never names a hidden Next case; Case 2 uses its specified fixed alpha 0.05; compact dot stacks and six-row history fit their boxes.

## Frames looked at

- Scratch bar-frames: Snowy Mail Route and Beat Lab, 1366x768.
- All 3 check frames and 10 journey frames, including interruption, exhausted budget, wrong accusation, table drag, both slopes, shuffle, lab cancel and keyboard activation.
- All 32 full-sweep frames: four evidence views at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812.
- All 14 targeted frames, including affected compact/phone states, grayscale, Motion off and briefing.
- All 7 final frames: opening, compact opening, n/α extremes, zero weights, second wrong accusation and six-row history.
- All 59 audit frames, reviewed in labeled contact sheets.
- Two last compact/phone truth-reveal frames: every revealed probability is visible on the main card, whose bottom stays inside the viewport.
- All 9 final-source preview repair frames, then 13 finished-bundle frames plus the focus diagnostic and 2 final keyboard/welcome frames. Phone target measurements, zero table overlap, and the Enter-twice path are in finish.log and the final tool output.

## Art made

- Seven new images through the built-in image tool. Existing café retained. Eight final WebPs total 164.5 KB. Final bundled file is 519.9 KB, below 2 MB.
- Raw PNGs copied into art/raw, prompts and drawn_by recorded. Processed only with art.py --rekey. Each finished asset reviewed on a dark contact sheet and in context. No redraw needed.

## Art still to paint

- Librarian and suspect portraits: people true, deferred for owner review. Faceless code silhouettes remain. No people or body parts were generated.

## Engine changes wanted

None.

## Left open

- Recorded curious-librarian narration is absent by the build-only no-recording instruction. Browser speech remains the fallback and has not had a listening review.
- No live classroom session or cold review has occurred. Small-screen density remains a useful cold-review focus.
- The full audit was run once before the final focused repairs. Its original 26 leads and the targeted repair evidence remain in Scratch for the cold reviewer.
- No final full audit or second complete size sweep was run after the focused repairs. The affected header layouts were rechecked at every required size, with additional phone table/lab, focus, keyboard and welcome checks.

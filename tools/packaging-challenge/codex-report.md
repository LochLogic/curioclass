# Codex report: packaging-challenge

## Built
Grade 10 offline Orders, Shelf and Case: six fixed-volume designs, direct dragging, sliders and number entry, trial dots, analytic material curves, exact minima, flat pieces, weighted lids, four real-size cans and row-by-row case packing.

Uses the starter frame, 9-12 theme, Curio.voice, kit tones and Plane. All 13 images are placed. Readable source, stable controls and handle, draft metadata marked built. No commits, shared-engine edits or polish round.

Final bundle: **430,670 bytes**, about **421 KiB**, below 2 MB. Owned Chrome processes and temporary servers were closed; tool host.html is absent.

## Numbers check
PASS. Independent calculations: `_scratch/packaging-challenge/numbers.json` and `source-details.json`. Eleven browser assertions passed in `math-results.json`.

- O2 at r = 3.00: h = 12.555556, area = 293.215334, displayed 12.56 and 293.22. Exact best: r = 3.837215, h = 7.674430, area = 277.545024, mass = 8.33 g.
- Entering rounded radius 3.84 gives h = 7.66; the exact best card correctly shows 7.67. O6 similarly distinguishes entered 2.66 from the exact 2.660576 minimum.
- O1 best area 348.734205; O3 1211.119192; cube 600; comparison ghost 700; tray side 10, height 5, area 300.
- O6 at three times lid cost: best r = 2.660576, h = 15.963459, cost = 400.289192. At one times it matches O2. Height divided by radius equals two times lid cost at all seven supported settings.
- O2's half-percent band on the 0.01 cm grid is 3.58 to 4.11. Can case fill is pi divided by four; square-base fill is 100%.
- Shelf differs slightly from the spec's example table when using its listed rounded centimeter dimensions. Model volumes are 572.5, 996.2 and 3450.9 cm³ for No. 303, No. 2½ and No. 10. Computation wins. Full material and minimum-area differences are in handoff.md; excess percentages still display 4.1%, 1.1%, 0.2% and 0.2%.
- Brand contrast: 5.70:1 on panel, 5.40:1 on secondary background, 5.20:1 on the specified dark bench; brand-ink on brand 5.97:1.

## Feel check
Played a student path with a real whole-pixel, jittered drag, then held clicks through curve, best, two Shelf cans and case packing. Keyboard-only O2 finished at radius 3.84 with 17 trials, best revealed and focus retained on Reveal best.

Best moment: the trial dots settle toward the curve's low point while the can becomes nearly as wide as it is tall, then the ring confirms the design. Costlier lids make the next design problem meaningfully different.

Two flattest moments and fixes: the first version left the best can too small within its stage, so its artificial zoom cap was removed; compact layouts buried material, so a live readout now stays on the bench beside the student's record. Net also moved below the package so it cannot cover the graph.

Opened Snowy Mail Route for its feedback bar and compared the finished frame beside Beat Lab. The painted workshop, tactile metal, pantry cans and case lids give this tool a substantial setting, with the package and graph still dominant.

![Packaging Challenge beside Beat Lab](S:/CurioClass-codex/_scratch/packaging-challenge/feel-comparison.jpg)

## Done when
1. PASS: O2 samples and optimum verified independently and in browser; final frame shows 277.55 and height = two times radius.
2. PASS: cube 600, labeled ghost 700, tray 300 at side 10 and height 5. Box and tray frames inspected.
3. PASS: O6 minimum and price-one equality verified. Weighted cost is distinct from actual material and mass.
4. PASS: drink 4.1% and 1.86; No. 10 0.2% and 1.13. All four painted cans share one outside-size scale; target sizing does not stretch their images.
5. PASS: 24 can packages give 78.5%; square bases 100.0%. Case mass applies the practice factor; square packages label it a metal equivalent, not actual cardboard mass.
6. PASS: O2 and O3 radius 1 and 12 inspected at 680x425. Zoom, graph range and readouts remain contained. Closed-box side 2 and 30 also inspected.
7. PASS: package and graph cards have equal size at 1366x768 and 1000x625. Shelf and Case dominate their stages.
8. PASS: controls never lock. Pack was immediately interrupted through order, mode and shape changes. Audit resize-after-input and resize-after-click checks found no exceptions or disabled controls left behind.
9. PASS: speech uses scope, valid and needs checks; lid speech requires its visible slider. Held-click, two-second repeat and quick-tap logs checked. Intentional first-tap welcome omissions are explained below.
10. PASS: keyboard-only O2 completion recorded. Every standard size keeps the package, graph and primary slider visible without page scrolling. Short O6 layouts were repaired and rechecked with the hint fully visible.
11. PASS: clean tool console, no remote resources, network APIs, unbundled assets or em dashes; Curio Class branding in full. An initial test-host favicon 404 was resolved and subsequent phone runs were clean.

## Wave lessons
- PASS, hint and voice: hints change synchronously and name the next action. Read speaks the current hint; how-to lines use the kit's heard state. First actions never wait for speech.
- PASS, focus and layout: no focus on load or controls rebuilt under the pointer. Handle focus uses preventScroll. Keyboard completion and audit Enter-twice checks retained focus.
- PASS, sizes: every standard size inspected, including a 375x812 iframe. Case's 42 px target became 44 px; O6's short hint now fits.
- PASS, no giveaways: this is the specified explorer. The curve requires five releases or Show curve, and the minimum requires Reveal best. No hidden-answer quiz or sweep-to-win score.
- PASS, honest numbers: fixed volume, outside-size cylinder assumptions, weighted cost and practice grams per area are explicitly distinguished.
- PASS, standards: students design under constraints, compare real cylindrical models, and calculate case fill and mass from area. No family engine was replaced.
- PASS, Motion off: final check returned 24 instantly packed items and zero running animations; audit found nothing running forever.
- PASS, short choice sets: six orders use a native picker; all four Shelf cans stay visible. No short choice set is buried in a scroll panel.
- PASS, resize mid-animation: the audit's complete resize stress was clean, including packing and all listed states.
- PASS, deferred welcomes: welcomeAfter is not used. A tap's own speech skips the welcome as STANDARDS requires.
- PASS, unknown states: curves and minima stay absent until revealed. No invented hidden clue or diagnosis state.
- PASS, one look and meaning: white trial dots, a current-design diamond, a ring plus BEST, and case-gap hatching. Grayscale frame inspected.
- PASS, truthful badges: locked volume stays exact; package count matches the case; personal records belong to the current order and price rule.
- PASS, hints change back: mode, order, clear and completed-packing paths reset their next-action hints immediately.
- PASS, no answer by copying: no matching-answer quiz. Students generate designs and observations before the optional best reveal.

## Audit leads
One full audit completed with **24 leads**, at `_scratch/packaging-challenge/audit/audit.md`. All 89 frames were inspected. The full audit was not repeated after repairs; affected states received targeted checks.

- FIXED, 1 target lead: Case at 680x425 was 42 by 44; it is now at least 44 by 44.
- FIXED, 13 height-label overlap leads: eight initial sizes, drink-best, radius minimum, radius maximum, and two lid-cost size groups. Dimensions moved left, away from the right-side handle. Targeted normal, needle and flat checks report zero overlap and labels inside the SVG.
- FIXED, 2 hint leads: O6's hint and keep region extended below 680x425. Its decorative order card now yields room on short landscape screens. Both 680x425 and 800x500 keep the hint and both sliders visible.
- FIXED, 1 curve-crossing lead: BEST sits below the minimum, clear of the curve. Phone O6 at four times lid cost inspected.
- FIXED, 4 quick-tap speech leads: the current mode no longer hushes its welcome; Clear preserves an active Orders welcome. Double taps on all three modes and Clear returned welcome logs without cuts.
- ACCEPTED, 3 first-tap welcome leads: handle release makes Orders welcome stale by explicit spec; Show curve and Reveal best have their own speech, which skips welcome under STANDARDS. Fixed volume stays visible and Read gives the current action. No late welcome is inserted after these actions.

The audit found no runtime exceptions, stuck disabled controls, repeated how-to speech in its two-second repeats, or infinite Motion-off animations. Net intentionally changes the package viewport. The kit Sound label may change header spacing while controls stay visible.

## Frames looked at
Every PNG in `first-frames`, `play-frames`, `sweep-frames`, `targeted-frames`, `post-audit-frames` and `bar-frames` was inspected directly or on contact sheets, plus all 89 audit PNGs. Coverage includes all standard sizes and modes, six orders, can and box limits, tray net, lid cost, grayscale, Motion off, keyboard completion, real drag, interruption, real cans, phone layouts and focused repairs. Original frames and contact sheets stay in Scratch.

## Art made
13 placed WebPs: 12 new OpenAI gpt-image illustrations and the retained kraft texture. Finished art: **227,016 bytes**, about **222 KiB**. Prompts and selected originals are retained. Soup was redrawn twice for neutral steam; soda once for clean highlights. Soup uses the free art.py despill option. No people were generated. Final bundle: **430,670 bytes**.

## Art still to paint
None. Every specified image is present and inspected. Narration recordings were not made, as instructed.

## Engine changes wanted
None.

## Left open
- Narration uses browser speech, not a recorded hero-coach / Puck performance. No listening or headphone review was performed.
- Dense secondary readouts scroll within their own compact panel; main controls, live material, package and graph stay visible.
- The full audit predates the focused repairs; only affected states were rechecked afterward.
- No live-classroom trial. The Shelf open question was settled in handoff.md: keep four real, unbranded cans.

# Packaging Challenge: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: packaging-challenge

#### Built
Grade 10 offline Orders, Shelf and Case: six fixed-volume designs, direct dragging, sliders and number entry, trial dots, analytic material curves, exact minima, flat pieces, weighted lids, four real-size cans and row-by-row case packing.

Uses the starter frame, 9-12 theme, Curio.voice, kit tones and Plane. All 13 images are placed. Readable source, stable controls and handle, draft metadata marked built. No commits, shared-engine edits or polish round.

Final bundle: **430,670 bytes**, about **421 KiB**, below 2 MB. Owned Chrome processes and temporary servers were closed; tool host.html is absent.

#### Numbers check
PASS. Independent calculations: `_scratch/packaging-challenge/numbers.json` and `source-details.json`. Eleven browser assertions passed in `math-results.json`.

- O2 at r = 3.00: h = 12.555556, area = 293.215334, displayed 12.56 and 293.22. Exact best: r = 3.837215, h = 7.674430, area = 277.545024, mass = 8.33 g.
- Entering rounded radius 3.84 gives h = 7.66; the exact best card correctly shows 7.67. O6 similarly distinguishes entered 2.66 from the exact 2.660576 minimum.
- O1 best area 348.734205; O3 1211.119192; cube 600; comparison ghost 700; tray side 10, height 5, area 300.
- O6 at three times lid cost: best r = 2.660576, h = 15.963459, cost = 400.289192. At one times it matches O2. Height divided by radius equals two times lid cost at all seven supported settings.
- O2's half-percent band on the 0.01 cm grid is 3.58 to 4.11. Can case fill is pi divided by four; square-base fill is 100%.
- Shelf differs slightly from the spec's example table when using its listed rounded centimeter dimensions. Model volumes are 572.5, 996.2 and 3450.9 cm³ for No. 303, No. 2½ and No. 10. Computation wins. Full material and minimum-area differences are in handoff.md; excess percentages still display 4.1%, 1.1%, 0.2% and 0.2%.
- Brand contrast: 5.70:1 on panel, 5.40:1 on secondary background, 5.20:1 on the specified dark bench; brand-ink on brand 5.97:1.

#### Feel check
Played a student path with a real whole-pixel, jittered drag, then held clicks through curve, best, two Shelf cans and case packing. Keyboard-only O2 finished at radius 3.84 with 17 trials, best revealed and focus retained on Reveal best.

Best moment: the trial dots settle toward the curve's low point while the can becomes nearly as wide as it is tall, then the ring confirms the design. Costlier lids make the next design problem meaningfully different.

Two flattest moments and fixes: the first version left the best can too small within its stage, so its artificial zoom cap was removed; compact layouts buried material, so a live readout now stays on the bench beside the student's record. Net also moved below the package so it cannot cover the graph.

Opened Snowy Mail Route for its feedback bar and compared the finished frame beside Beat Lab. The painted workshop, tactile metal, pantry cans and case lids give this tool a substantial setting, with the package and graph still dominant.

![Packaging Challenge beside Beat Lab](S:/CurioClass-codex/_scratch/packaging-challenge/feel-comparison.jpg)

#### Done when
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

#### Wave lessons
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

#### Audit leads
One full audit completed with **24 leads**, at `_scratch/packaging-challenge/audit/audit.md`. All 89 frames were inspected. The full audit was not repeated after repairs; affected states received targeted checks.

- FIXED, 1 target lead: Case at 680x425 was 42 by 44; it is now at least 44 by 44.
- FIXED, 13 height-label overlap leads: eight initial sizes, drink-best, radius minimum, radius maximum, and two lid-cost size groups. Dimensions moved left, away from the right-side handle. Targeted normal, needle and flat checks report zero overlap and labels inside the SVG.
- FIXED, 2 hint leads: O6's hint and keep region extended below 680x425. Its decorative order card now yields room on short landscape screens. Both 680x425 and 800x500 keep the hint and both sliders visible.
- FIXED, 1 curve-crossing lead: BEST sits below the minimum, clear of the curve. Phone O6 at four times lid cost inspected.
- FIXED, 4 quick-tap speech leads: the current mode no longer hushes its welcome; Clear preserves an active Orders welcome. Double taps on all three modes and Clear returned welcome logs without cuts.
- ACCEPTED, 3 first-tap welcome leads: handle release makes Orders welcome stale by explicit spec; Show curve and Reveal best have their own speech, which skips welcome under STANDARDS. Fixed volume stays visible and Read gives the current action. No late welcome is inserted after these actions.

The audit found no runtime exceptions, stuck disabled controls, repeated how-to speech in its two-second repeats, or infinite Motion-off animations. Net intentionally changes the package viewport. The kit Sound label may change header spacing while controls stay visible.

#### Frames looked at
Every PNG in `first-frames`, `play-frames`, `sweep-frames`, `targeted-frames`, `post-audit-frames` and `bar-frames` was inspected directly or on contact sheets, plus all 89 audit PNGs. Coverage includes all standard sizes and modes, six orders, can and box limits, tray net, lid cost, grayscale, Motion off, keyboard completion, real drag, interruption, real cans, phone layouts and focused repairs. Original frames and contact sheets stay in Scratch.

#### Art made
13 placed WebPs: 12 new OpenAI gpt-image illustrations and the retained kraft texture. Finished art: **227,016 bytes**, about **222 KiB**. Prompts and selected originals are retained. Soup was redrawn twice for neutral steam; soda once for clean highlights. Soup uses the free art.py despill option. No people were generated. Final bundle: **430,670 bytes**.

#### Art still to paint
None. Every specified image is present and inspected. Narration recordings were not made, as instructed.

#### Engine changes wanted
None.

#### Left open
- Narration uses browser speech, not a recorded hero-coach / Puck performance. No listening or headphone review was performed.
- Dense secondary readouts scroll within their own compact panel; main controls, live material, package and graph stay visible.
- The full audit predates the focused repairs; only affected states were rechecked afterward.
- No live-classroom trial. The Shelf open question was settled in handoff.md: keep four real, unbranded cans.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: packaging-challenge
#### Played
Cold Grade 10 solo path, then a projected-class comparison: Orders, all four Shelf cans and Case, before reading builder reports, handoff, notes or source. The brushed-metal transformation and same-scale shelf are strong; the original reveal was flatter than the build-up.
Evidence: `_scratch/packaging-challenge/` folders cold, play, find, final-sizes, post, post-voice and review-audit. No commits or shared-file edits.
Temporary host.html removed. Owned Chrome and host processes closed; ports 9940, 9941 and 8745 verified closed. Direct process termination succeeded after Windows denied taskkill for two host children.
#### Findings fixed
- **Blocker, general, O6 entry:** invalid text produced NaN. Validate in the tool's parser before the kit slider accepts text, retain the prior price, and guard the model API. The first repair protected the model but the kit rewrote the field as NaN; the parser repair addresses that too.
- **Blocker, general, Orders praise:** revealing the answer and typing 3.84 earned "Great build." Replaced achievement praise with a factual comparison, suppressed after Reveal best. Sampled minima describe observations, not demonstrated skill.
- **Should fix, general, O6 voice:** decreasing price said pricier lids. Added the reverse event and interrupt stale price speech. O6 comparisons say cost; actual mass stays unweighted.
- **Should fix, general, graph teaching:** Show curve with no dots credited the student's dots. It now describes the mathematical model, including after identical releases.
- **Should fix, general, O6 record:** weighted cost was called least material. It now says Lowest sampled cost, including after repricing earlier dots.
- **Should fix, general, Shelf facts:** wording implied manufactured metal was measured. It now explicitly compares cylinder-model area at each can's own modeled volume.
- **Should fix, general, graphics:** colored fringes on cutouts. Redrew the weakest glass illustration and rekeyed nine cutouts with despill and holes; retained the coherent painted bench, shelf, cans and kraft.
- **Should fix, general, small graphs:** four-digit y ticks clipped at the smallest width. The margin now allows for their digit count. Moved Shelf's Best label clear of its marker and phone tick.
- **Should fix, general, Case meter:** the empty case's panel could read as already 78.5% filled. Labeled it Full-case fill and Product in 24, separating the planned full-case comparison from the visible packed count.
- **Polish, general, reveal payoff:** best dimensions could be buried in the scrolling readout. They now appear on the bench beside the sampled result, with a brief Motion-aware marker fade. Removed an initial scale animation after frames showed marker displacement.
#### Findings left
No blocker or should-fix remains.
- **Polish:** browser speech, no recorded hero-coach performance or headphone review. Recording is outside this pass under CODEX-BUILD.md.
- **Nit:** paper texture repeats on very large flat box faces. It remains warm and readable; no flattening or restyle applied.
#### Break it
- **Near-best / sampled record:** copied revealed radius through the number field and real Enter. Before: achievement praise. After: zero best events, truthful sample value, no score, badge or saved achievement. `post-copy.json`.
- **Sweep:** real 100-point slider drag records only its final release; ending at radius 12 gives one poor trial, not the best point crossed. Repeated pre/post in drive.py.
- **Five releases / curve:** identical inputs show the model curve as specified, not five different designs or a pass. Show curve is already an explicit early-reveal aid. Narration no longer invents a discovery.
- **Reveal:** immediately leaves the current design in place and marks the analytic minimum. It is a reference, not an earned gate. Copying does not earn the event.
- **Lid price:** invalid text, decrease, endpoints, all seven prices and repricing a record exercised. Weighted cost, actual area and practice mass remain distinct.
- **Shelf:** tapped all cans and switched quickly. Each uses its own volume and minimum. No quiz, reflection gate, pass or hidden answer exists.
- **Case:** packed all six orders, double-tapped, changed order/mode during packing and used Motion off. Full-case comparisons stay 78.5% for cans and 100.0% for square bases; count matches drawn rows. Repacking earns nothing.
- Independent computation plus 11 browser formula assertions passed; fill/count checks passed for all six orders. `numbers.json`, `post-math.json`.
#### Voice walk
Default Sound on, 0.12-second held clicks, two-second pace: package, Radius, Show curve, Reveal best, Shelf, Drink, No. 10, Case, Pack. `voice-main-post.json`.
Spoken order: wOrders, afterBest, wShelf, afterShelf, wCase, afterPack. All three mode instructions started once. Curve became obsolete after Reveal best and dropped; mode changes cut outgoing instructions without late old-mode speech.
Followed the welcome: change width while volume stays locked, then compare the graph. A first release can skip wOrders on the faster path, as BASELINE 16 permits; hint and volume readout retain the premise.
Repeat counts: near-minimum event expected 5, spoken 5 (7-second gaps so each line finishes); curve how-to expected 1, spoken 1 (five taps at 2-second gaps); each mode welcome expected 1, spoken 1. `voice-events.json`, `voice-how.json`.
Read interrupts the current line, reads the current hint even with Sound off, and releases immediately on a mode switch. Rapid switching drops obsolete queued lines. Lid increase/decrease events each start once; reversing the price cuts the old-direction line. `voice-stale.json`, `voice-lid.json`, `read-off.json`. Muted log verification, not a listening review.
#### Facts checked
- **Formulas:** cylinder volume and closed area; prism volume and face areas, including the open tray: [OpenStax Prealgebra 2e 9.6](https://openstax.org/books/prealgebra-2e/pages/9-6-solve-geometry-applications-volume-and-surface-area).
- **Minima derived from those formulas, independently recomputed:** O1 r 4.30127, h 8.60254, A 348.73421; O2 r 3.83722, h 7.67443, A 277.54502; O3 r 8.01573, h 16.03145, A 1211.11919. Closed-can h = 2r.
- **Square/weighted models, same source and computation:** cube side 10 gives 600; 20 by 10 by 5 ghost gives 700; tray side 10, h 5 gives 300. O6 at price 3: r 2.66058, h 15.96346, cost 400.28919; h/r = 2k at all seven prices. Price 1 matches O2.
- **Samples/extremes, same formulas:** O2 r 3 gives h 12.56, A 293.22; r 3.84 gives A 277.55 but h 7.66, while exact best rounds to h 7.67. Samples 2.5, 4.5, 5 reproduce. O2 r 1/12 gives h 113.00/0.78; O3 r 1 gives 1030.05. O4 side 2/30 gives h 250/1.11.
- **Units:** 1 mL = 1 cubic centimetre and 1 US fl oz = 29.57353 mL: [NIST Handbook 44, 2026 Appendix C](https://www.nist.gov/document/2026-nist-handbook-44-appendix-c), C-16 and C-24. Spec capacities convert to 354.9, 499.2, 881.0 and 3236.2 mL.
- **Shelf inputs:** food-can inch sizes/capacities match the spec's [Tin can table](https://en.wikipedia.org/wiki/Tin_can#Standard_sizes); nominal-size convention cross-checked against USDA AMS Technical Procedures Manual, February 2013, pages 88-89. Cm inputs are rounded specimen values.
- **Drink:** spec's [Beverage can source](https://en.wikipedia.org/wiki/Beverage_can#United_States) lists 6.60 by 12.3 cm. [Crown's 355 mL specification](https://www.crowncork.com/beverage-packaging/products/beverage-cans/12oz-355ml-standard) confirms 66 mm diameter but gives 122.22 mm height. Retained the spec's approximate specimen, not a universal manufacturing size.
- **Shelf calculations from stated cm inputs:** volumes 420.8, 572.5, 996.2, 3450.9; areas 323.5, 385.8, 553.4, 1266.3; minima 310.9, 381.7, 552.2, 1264.2; excess 4.1%, 1.1%, 0.2%, 0.2%; h/diameter 1.86, 1.37, 1.15, 1.13. OpenStax formulas, full precision. Spec example totals differ slightly through rounding.
- **Packing:** case volume 96 r squared h versus product 24 pi r squared h gives pi/4 = 78.5%; square bases give 100%. Derived from OpenStax volumes. Assumes square grid, bounding volumes, no dividers or case-wall thickness.
- **Mass:** 0.03 g per square cm is the spec's labeled practice factor; O2 best gives 8.33 g; case mass is 24 times unweighted area times 0.03. It is not measured real metal density or cardboard mass.
- **Standards:** [Common Core G-MG.A](https://www.thecorestandards.org/Math/Content/HSG/MG/): Shelf models objects, Orders designs under a volume constraint, Case compares volume density and area-based mass. Notes have the required opening sections and practical home activities.
#### Sensitivity
None: unbranded geometric packaging and food/plant objects, no cultural, historical, religious or bodily subject. No people in the art. This object-scale workbench and pantry do not need a person to explain the task.
#### Flattest moment left
Repacking the same order repeats its grid. The useful contrast comes from changing circular to square bases. Added no new challenge or score beyond the spec. Reveal is stronger because its exact result stays on the bench.
#### Graphics
All 13 assets checked in scenes/contact sheets and final-size cutouts. One glass redraw; nine cutouts rekeyed. Metal package, painted bench, shelf scale, kraft nets and case retain their detail. All art tokens have entries/files; no people or placeholders.
All standard sizes, phone iframe, grayscale, Motion off, keyboard completion and can extremes inspected. The final keyboard run reaches O2 r 3.84 with 17 trials, then reveals best; focus stays on Reveal best. A whole-pixel jittered handle drag records one trial and retains handle focus. Motion off packs 24 instantly and has zero running animations after settling.
BUILD wave checks: synchronous action hints and Read; stable focus/controls; 44 px targets and visible choices; no hidden-answer gate; explicit model assumptions; all three standards practiced; calm motion; resize during action; no late welcome; unknown data stays absent until shown; distinct dot/diamond/ring meanings; truthful labels; hints restore on mode/order changes; no word-matching answer shortcut. Evidence is in the focused logs, source inspection and final audit.
Final art: 222,798 bytes (217.6 KiB); bundle: 426,876 bytes (416.9 KiB), below 2 MB.
#### Audit
Completed once within the 40-minute limit, Chrome 9941, host 8745: `review-audit/audit.md`. All 91 audit PNGs inspected, plus focused pre/post frames.
- One fixture lead corrected: the duplicate sidebar `#material` is intentionally below the compact fold. The keep target is now the persistent bench `#liveMaterial`; fixture focus uses preventScroll and the phone size key is corrected. Scoped 680x425 re-shot confirms the live readout in view and invalid price restored.
- Three first-tap welcome leads accepted under BASELINE 16 and the explicit spec: handle release makes wOrders stale; Show curve and Reveal best speak their own instruction. Locked volume stays visible and the main walk hears all three mode how-to lines. No late welcome added.
- All eight first-screen sizes clean; other listed states clean. Motion off has no infinite animations. No runtime errors, stuck disabled controls, lost focus, repeated how-to nagging or quick-tap speech defect. Final resize stress clean.
- No second audit. Only the corrected fixture and the changed graph's remaining extreme-value margins received scoped closure frames.
#### Left open
- Unattended choice: retain four real unbranded cans rather than introduce invented box dimensions.
- Retain approximate specimen dimensions and document differences from precise manufacturer sizes; changing inputs needs a spec decision.
- Browser voice fallback remains. No recording, classroom trial or subjective listening validation performed.
- Initial location/document reads returned immediately before the bounded helper was installed. Subsequent commands have explicit limits; no command remains running without a deadline.

- Two manual phone batches logged a parent test-host favicon 404; the offline tool has an inline icon and no remote resources. The audit host is clean.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Packaging Challenge handoff

#### Cold review changes, 2026-11-07
The single cold review played the bundle before reading this handoff or src.html. Full evidence and scripts are in `_scratch/packaging-challenge/`.

Lid cost rejects nonfinite input and restores its last valid price. Its event now follows price direction, interrupts stale price speech, and distinguishes cost from actual material. The sampled minimum is explicitly descriptive; near-minimum events report geometry rather than achievement, and are suppressed after Reveal best so copying the reference earns no praise.

Show curve describes a model curve even with zero or repeated dots. Reveal best keeps the best dimensions and objective on the bench, outside the scrolling detail panel, and gives its marker a brief Motion-aware arrival. Shelf describes model area rather than claiming measured real metal usage, and its Best label is separated from the point.

The drink illustration was redrawn with the built-in imagegen tool using the prompt in `art/prompts.json`. All keyed cutouts except the already-clean soup were reprocessed with art.py's despill option; the painted bench, shelf, metal cans and kraft style remain. No people are needed in this object-scale workbench or pantry scene.

The spec's four-can Shelf is retained. Its stated centimeter inputs remain the model's inputs; numerical results are recomputed from them. The spec's beverage height is an approximate specimen size, not a universal manufacturing dimension. Narration still uses the browser; no recordings were made.

Case labels its planned ratio Full-case fill, separate from the packed count. Small graph margins allow four-digit y values. The invalid-lid audit state keeps the permanent bench readout rather than a duplicate inside the scrolling detail panel, and purposeful fixture focus uses preventScroll.

Focused review evidence: `post-copy.json` has zero best-event credit after copying; `post-math.json` passes all 11 formula checks and all six case comparisons; `keyboard-final.json` reaches O2 at 3.84 with 17 keyboard trials and Reveal best focused. `voice-events.json` has five factual events, `voice-how.json` one how-to over five taps, `voice-main-post.json` all three mode instructions, and `read-off.json` Read with Sound off. The settled calm case has 24 packages and no running animations.

The cold review's single final audit completed within 40 minutes at `_scratch/packaging-challenge/review-audit/audit.md`: four leads, with all 91 frames inspected. One fixture selector was corrected to the bench's live readout; three first-tap welcome omissions are permitted by BASELINE 16 and the spec. All other size, state, Motion off, focus, runtime, repeat, quick-tap and resize checks passed. No second audit was run.

Build only, 2026-11-03. No commits, shared engines or other tools changed.

#### Implementation
`src.html` uses the starter's kit header and control structure, the 9-12 theme, Curio.voice, Curio.tone and Plane. It lays out at actual pixel dimensions with ResizeObserver rather than scaling a fixed scene. The package SVG redraws while its stable handle retains focus and pointer capture. All buttons, sliders and number fields remain stable DOM nodes.

Orders store their shape, price rule, trial dots and personal minimum for this page session. Release records a trial; five dots reveal the curve. Reveal best leaves the student's shape in place and adds the exact analytic minimum. O6 reprices previous dots when the lid cost changes. Actual mass always uses unweighted material area.

Shelf cutouts are cropped through art.py and stretched to the published outside height and diameter on one shared scale. Their transparent button targets may be wider than a small can; the painted can itself retains the exact scale. Selection lifts a can by 10 pixels. Each graph uses that can's own outside-size cylinder volume.

Case uses 24 packages in a 4 by 6 grid. Six arrive immediately, with another six at 0.5, 1.0 and 1.5 seconds. A second tap, order change, mode switch, slider input or Motion change finishes a running drop immediately. Switching to a new order clears the packed count for that order. Resizing carries the current packing count forward.

`window.__tool` exposes state, setMode, order, set, best, shelf, lidCost, pack, model, optimum, allLines, vlog and vq. Modes accept title case or lower case. `set(value)` records a trial; `set(value, false)` updates without a release.

#### Numbers and modeling decisions
- Compute from listed centimeter dimensions, not the rounded Shelf example results. No. 303 therefore has volume 572.5 cm³, material 385.8 cm² and best 381.7 cm²; No. 2½ has 996.2, 553.4 and 552.2; No. 10 has 3450.9, 1266.3 and 1264.2. Drink remains 420.8, 323.5 and 310.9. Percentage comparisons retain full precision, giving 4.1%, 1.1%, 0.2% and 0.2%.
- The exact O2 minimum is r = 3.837215..., h = 7.674430..., area 277.545024.... At the entered radius 3.84, h = 7.663304..., displayed 7.66. Reveal best correctly displays its own 7.67 height. The same distinction applies to entering 2.66 in O6 versus the exact 2.660576... minimum.
- Case mass uses 24 × actual area × 0.03 g/cm², explicitly a practice number. Box and tray readouts label it a practice metal equivalent, not real cardboard mass.
- No personal work is saved. Only the kit's shared Motion preference persists on this device.

#### Open question settled
Keep four real, unbranded cans. This is the option the spec leans toward. Do not add an invented cereal box with brand-dependent dimensions.

#### Art and narration
Twelve new OpenAI gpt-image illustrations plus the existing kraft texture, all in `art/`. Prompts and provenance are in `art/prompts.json`; original generated PNGs are in ignored `art/raw/`. Soup was redrawn twice to make neutral steam; the soda was redrawn once to remove key-color reflections. Final soup also uses art.py's despill option. No people were generated.

Voice bank: hero-coach / Puck. `voice/lines.json` lists nine lines. No recordings were made, as this build forbids recording. Browser speech is the active fallback, so the intended bank voice is not yet audible. Tests use muted Chrome and inspect the kit's narration log; no listening review was performed.

#### Layout and verification
Main controls remain visible at the standard sizes and 375x812 iframe. Short landscape keeps stage and panel beside one another. Portrait stacks controls beneath the stage. The live material is also printed on the stage so dense secondary readouts can scroll within their own panel. On the shortest landscape screens O6 omits its decorative order card to make room for both sliders and the hint. Net occupies a strip below the package, with no overlay on the graph, and starts open at 900 pixels tall or above unless the user has chosen its visibility.

Evidence lives only in `_scratch/packaging-challenge/`: independent numbers, math assertions, real jittered drag, held-click student path, keyboard completion, all-size frames, extreme shapes, Motion off, grayscale and final audit. The keyboard run uses native closed-select arrows followed by Tab; Enter on a closed select opens its menu and is not needed to confirm an arrow-key change.

The first phone host requested its own missing favicon. The host and tool now use an inline empty icon; subsequent phone shots were clean. A screenshot batch also overlapped a previous Chrome process; only the interrupted shots were retried with an isolated allowed port. Neither was a tool runtime failure.

#### Engine changes wanted
None. All workarounds remain in this tool.

#### Next review
Read `codex-report.md` and the audit leads before making changes. This is the end of the build, not a polish round. A classroom trial, headphone review and recorded narration remain outside this run.

#### Audit closure
The single full mechanical audit completed with 24 leads in `_scratch/packaging-challenge/audit/audit.md`. Its 89 frames were inspected. Post-audit changes fixed 21 leads: the Case target, every height-label overlap category, O6 hint clipping, the curve crossing BEST on a phone, and welcome speech cut by repeated mode or Clear taps. Targeted checks cover these repairs; the full audit was not repeated.

Three first-tap welcome omissions are intentional. The spec makes the Orders welcome stale after the first release; Show curve and Reveal best have their own first-tap instruction. STANDARDS says a tap's own speech skips the welcome. The fixed-volume premise remains visible, and Read speaks the current next action.

Repeated clicks on the selected mode now finish any visual motion without stopping valid speech. Clear preserves an active Orders welcome, which still fits the unchanged order. Height labels are to the left of the package, outside the right-side handle's transparent target. BEST is below the minimum, where the material curve cannot cross it.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)

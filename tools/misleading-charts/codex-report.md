# Codex report: misleading-charts

## Built
Built both modes: six nonlinear investigations at a painted newspaper desk, and a live chart-manipulation sandbox at an agency desk. The kit owns Motion, Sound, Read, effects and voice. SVG charts use actual viewport dimensions.
Delivered the self-contained HTML, readable source, draft metadata with stage built, notes, fifteen authored voice lines, audit states, handoff, preview and fourteen paintings.
Build only. No commits, shared-engine edits, publication or polish round.

## Numbers check
Independent Python results are in `numbers.json`; assertions and all ten daily rates are in `check_numbers.py` in Scratch.

| Case | Independent result |
|---|---|
| 1 | (1050-950)/(1000-950) = 2; 1050/1000 = 1.05; lie factor 20.0 |
| 2 | Nov 840/19 = 44.2; Dec 510/12 = 42.5; Jan 830/19 = 43.7. Published picture and number ratios both 510/840 |
| 3 | Height and width both double: area 4, data 2, lie factor 3.0 |
| 4 | Exact second-axis bounds 2/3 and 19/6; first and last endpoints at 0.133333 and 0.933333 of chart height |
| 5 | Oak 5, Elm 10, Birch 6 per 100. Oak/Elm totals 1.5; rates 0.5 |
| 6 | All seven annualized slopes 1; 19 members gained over 19 years |
| Extreme | Baseline 999: picture 51.0, data 1.05, lie factor 1000.0 |

Ratios use unrounded model geometry. Pixel labels are rounded annotations. Auto-scaled picture axes stay aligned with the marks; dense pictures get sufficient range to avoid collisions. The meter identifies height, area or slope and the pair it compares.

## Facts checked
| Student-facing fact | Source and check |
|---|---|
| All publishers, places, years and raw values are invented | The spec's six case tables; each publication says made up. No real school is judged |
| The lie factor compares proportional graphical and numerical changes | Tufte, The Visual Display of Quantitative Information, 1983, chapter 2; independent ratio calculations above |
| Zero baselines matter for bar lengths | Cairo, How Charts Lie, 2019; student measures the cut-off and corrected bars |
| A short window can hide the wider record | Cairo 2019; the complete ten-month school-year array is shown with Nov-Dec marked |
| Visits do not establish that students stopped reading | Spec's visits-only measurement and Cairo's claim/evidence principle; table includes school-day denominators |
| Scaling both dimensions squares the height ratio | Geometry and spec; independently computed for recycling and tested on every sandbox data set |
| Rising together does not show that one causes the other | Cairo 2019 and spec; correction uses two zero-based charts and states this explicitly |
| Rates make unequal school groups comparable | Spec's invented denominators; all three rates recomputed independently |
| Equal spaces can disguise different year gaps | Spec's year/member arrays; every step recomputed per year |
| Every dynamic tick, rate, pixel label and ratio | Derived from those fictional values and the displayed chart model; no additional real-world quantities asserted |

Contrast recomputed: white/brand 6.32, ink/paper 15.26, muted/paper 6.10, focus/paper 5.54, published gray/panel 10.66, correction blue/panel 5.08. Header focus uses white.

## Break it
- PASS: all 108 trick/headline pairs without evidence are refused; no correctness oracle appears before diagnostic evidence.
- PASS: all 108 pairs with fresh diagnostic evidence accept exactly the six canonical pairs. Correct trick plus wrong ruling is rejected as a whole.
- PASS: changing choices after a wrong filing without fresh evidence is refused. A newly opened, unrelated data sheet cannot purchase another guess. Each required diagnostic proof must be renewed.
- PASS: repeating one mark does not form a ruler pair; a third pick clears the previous ratio. Robotics requires first and last endpoints. Mixed smoothie/win units are not divided into a comparison.
- PASS: cutoff extremes, picture area in every data set, rate comparisons, crossed time-window endpoints, honest resets, saved closures and reset confirmation.
- PASS: chart controls retain node identity; real clicks work through labels and overlapping transparent hit planes route to the nearest bar center. A keyboard-only run closes a case.
- The sandbox has no pass threshold, score or saved best. Sweeping its sliders is the intended exploration. Case closure is an activity record, not a mastery score or proof against a lucky answer.
Final deterministic regression: 392/392 assertions. `post-audit-regression.json` preserves each result. `full-student-walk.json` preserves all six closures using held clicks.

## Voice walk
Main path, default Motion on: Case 1 folder, Ruler and both bars, Axis check, both choices, File it, Fix it; then all remaining cases and their diagnostic tools, followed by Spin Room, Fact-checker's view and Make it honest. Held presses 120 ms, taps about 2 seconds apart.
Spoken starts: wCases once, ruler2 once, firstClue once, filedRight six times, each of the six closed lines once, wSpin once, factView once. The allClosed announcement was dropped when Next entered Spin Room, as its scope requires.
The side retry path speaks filedWrong once, then filedRight and the Case 5 closure once after renewed rate/data evidence. Read and Sound-off Read were also walked in `voice-side.json` before the final voice guard changes.
The firstClue instruction waits until File it is enabled. Its earlier stale queue entries remain unmarked. Events start immediately and obsolete instructions give way to the student's action. First-tap welcome cuts are allowed by BASELINE rule 16. The final full-run log verifies the once-only instructions after these fixes.
Fifteen fixed lines are authored for news-reader, Rasalgethi. No audio was recorded, per Build instructions; actual playback uses the kit's best-browser-voice fallback. Queue starts are verified, not recorded-voice quality.

## Feel check
Played all six cases with real held clicks, then the sandbox. Best moment: the ruler exposes a four-times-area recycling picture, then the correction prints ordinary two-times bars beside it and the case receives its stamp. The school's ranking reversal and the straightened robotics trend make later cases materially different.
Flattest moment 1: the small robotics chart fell onto the laptop keyboard and its dates ran together. Refitted the painted screen and staggered dates across readable rows.
Flattest moment 2: context and rate clues became cramped labels, and the inspector could cover the live meter. Kept a dashed published-window outline, gave the ghost rates an explicit scale, and moved short-screen inspector notes above the chart.
`feel-comparison.jpg` puts the closed recycling case beside Beat Lab. Both bar tools were bundled into Scratch, opened and inspected before implementation. This build has its own material detail, lighting, large props and clear action focus; it does not look plainer than that reference. No confetti or unrelated rewards were added.

## Done when
1. PASS: Case 1 reads Picture 2.0, Numbers 1.05, lie factor 20.0; Axis check says Starts at 950. Held-click and independent math evidence.
2. PASS: ten school months, Nov-Dec outlined/shaded; Data sheet has Nov 44.2 and Dec 42.5 per school day.
3. PASS: recycling area 4, numbers 2, lie factor 3.0; accepted ruling True, but blown up.
4. PASS: Oak 5, Elm 10, Birch 6 per 100; Holds up refused with the trick-is-right hint. Final real retry path closes only after fresh evidence and corrected ruling.
5. PASS: every canonical pair checked; correction required before closure. Cases 1, 3 and 5 have lie factor 1.0; cases 2, 4 and 6 say Honest with the contextual correction.
6. PASS: baseline 950 gives 2.0 and lie factor 20.0; inspector identifies Cut-off axis. Real drag to 999 gives uncapped 51.0 and 1000.0.
7. PASS: final 2-second held-click run has each requested how line once and filing/closure event starts every time.
8. PASS: all clues, all nine ruling choices and File it fit at 680x425 and 1366x768. Original/Correction have separate labels and styles in grayscale. Phone controls are above the scrolling desk.
9. PASS: published item is largest at 1366 and 1000; spun chart occupies the main working paper. All required sizes inspected.
10. PASS: rapid Zoom out/case switch acts immediately; real drag updates the meter. Full audit resize checks report no exceptions and nothing stuck disabled.
11. PASS: all six publication props painted and placed; chart text at least 11 px. Small laptop view deliberately extends its keyboard below the working area to keep labels on the screen. No image lettering.

## Wave lessons
- Hint and voice: PASS. Tool owns immediate hints; Read uses that exact text. Disabled File it is no longer named before both choices. How lines use V.heard; events remain repeatable.
- Focus and layout: PASS. Stable panel nodes and reused chart mark nodes, preventScroll focus restoration, reserved hint/readout space, no load focus. Closing Data sheet restores the ruling hint.
- Sizes: PASS. Full required-size run, 375 iframe host, minimum 44 px mark targets corrected after audit. Compact controls remain visible.
- No giveaways: PASS within the specified activity. Unnumbered mixed-order trick cards, both choices required, diagnostic proof gate, no score/best meter. No universal badge supplies a headline ruling.
- Honest numbers: PASS. Pair, units and area/slope/height basis stated; exact unrounded ratios; no change hides the lie factor; dense picture marks remain aligned with their axes.
- Standards/family: PASS. Students inspect values, transform to rates, compare representations and redraw them. Spec's CSTA codes and math links are covered. Family is explicitly none.
- Motion off: PASS. Blink loop disabled, redraws immediate, narration pacing retained; audit found no infinite animation.
- Short choices never hidden in a scroller: PASS. All six tricks and all three rulings stay visible. Short-screen sandbox controls use three columns; inspector does not displace a control.
- Resize mid-animation: PASS. Model state persists, pending reveals finish, controls act immediately; audit stress checks clean.
- No late deferred welcome: PASS. No welcomeAfter. Obsolete welcomes are cut or skipped under the standing rule.
- Unknown stays unknown: PASS. Correction is blank until filing and fixing; closures do not appear after failed filings.
- One look, one meaning: PASS. Published ink, dashed ghosts, fuchsia ruler marks and labeled blue corrections have distinct roles, including grayscale.
- Badge says what is true: PASS. Filed is distinct from Closed; closing requires the correction switch. Saved cases reconstruct their canonical ruling and correction.
- Hint changes back: PASS. Data-sheet close, case/mode changes and honest reset restore current next actions.
- No word-copy diagnosis: PASS. Case clues give measured baselines, rates, gaps and quantities rather than repeating a trick-card title. The revealing inspector belongs to the sandbox.

## Audit leads
Ran the full audit exactly once, to completion, on 9991 with host 8795. It saved 69 frames, 388 leads, clean Motion off, clean held-click repetition checks and no resize exceptions or stuck controls. Leads were reviewed, not treated as an automatic verdict.
The audited snapshot predates the listed fixes. It remains in Scratch/audit/host/tool.html; targeted post-audit checks cover the changes. The full audit was not repeated.

| Every lead in these categories | Disposition |
|---|---|
| Small mark targets | Fixed to at least 44 px high; compact default and ten-month targets measured after fix |
| Header text at zero px | Fixed with visible icon spans and visually hidden word spans, preserving accessible names |
| Hint or voice names disabled File it | Fixed with choice-specific hints and a valid/enabled guard on firstClue |
| Ghost legend overlapping group names | Fixed: units at top and a separate labeled ghost scale |
| Inspector covers meter / sandbox control cut short | Fixed: notes above chart, three-column controls in short windows; real extreme checked at 1280x720 |
| Data-sheet overlays / covered labels | Intentional inspector; made a dialog and covered papers inert. Phone sheet is now fully inside viewport and above the footer |
| Transparent mark/mark and mark/text overlaps | Invisible enlarged hit planes, not colliding drawn bars. Nearest-center pointer routing and stable nodes added; visible text inspected |
| Text reported under an SVG | Pointer-events-through labels / measured bounding boxes; inspected ruler and staggered-year frames show the text. No visible clipping accepted |
| Phone chart/readout/meter below viewport | Intended controls-first phone layout; the desk scrolls below. All primary choices are initially in view; data sheet uses a viewport overlay |
| Reset dialog covers hint and chart | Intentional modal backdrop. Cancel and Reset are visible, accessible and confirmed |
| "1 means" | Correct singular verb, not a count/noun error; retained exact meaning |
| "1 years" / "1 soccer wins" | Reworded gaps with singular 1 year and fixed the singular soccer-win accessible label |
| Welcome cut / not heard whole on first or quick taps | Settled BASELINE 16 behavior. Premise remains in the frame and mode context; no late welcome queue |

Audited bundle SHA256: `347818b52a1ee461e5c74f6a767a8b6ab8f267bb92d30dbc514b5a59cd403aaf`.
Delivered bundle SHA256: `6eb1452f09590f889d8bec966419055feea8fb75590529f50d76789936a8a348`.

## Frames looked at
All own drive PNGs in Scratch: `bar-frames`, `early-frames`, `check-frames`, `check-frames2`, `voice-frames`, `final-sizes`, `final-cases`, `final-gallery`, `final-touchups`, `post-audit-frames` and `phone-frames`.
All 69 audit PNGs reviewed on nine contact sheets in `audit-sheets`; specific small ruler, rate, sheet, correction and inspector states were also checked at full size in the targeted runs. Art contact sheet and both finish-reference frames inspected.
The single full-size sweep covered 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x900, plus 375x812 through host 8795. Later shots were limited to affected states.

## Art made
14 images: two desks, six blank publication props, six picture icons. Built-in image tool, complete prompts in art/prompts.json, raw PNGs preserved in art/raw, finished WebP through the free art.py --rekey path.
Art 821.2 KB; recorded voice 0 KB; delivered bundle 1459.3 KB against the 2048 KB goal. Art exceeded the initial 700 KB allocation after sizing for large screens; the complete file remains under the goal with voice headroom.
No generation redraws needed. Rekeyed cutouts to remove green/magenta fringe and resized to their largest intended use. All assets carry drawn_by codex, source credit and people false.
Art processing dependencies were installed only into Scratch/vendor because the available Python initially lacked NumPy. They are not bundled or runtime dependencies.

## Art still to paint
None. No people appear.

## Engine changes wanted
None. Shared files were not changed.

## Left open
- Recorded news-reader clips are not made in this Build-only run. Browser speech is functional; bank-voice fidelity and future recording timing remain for the later workflow.
- The spec accepts one primary technique per case even where secondary critiques are valid, notably library rates and the smoothie baseline. Canonical answers retained; teacher notes explain this limitation.
- On a phone, reaching the chart requires scrolling below the controls. This keeps the complete ruling set visible rather than hiding answer choices.
- This was Build only. No cold review or polish round was started. Chrome debug ports 9990-9997 and host 8795 are closed; host.html removed. CIM process inventory was denied, so only port shutdown is independently verified. See cleanup.json and build-manifest.json in Scratch.

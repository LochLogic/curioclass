# Misleading Charts: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: misleading-charts

#### Built
Built both modes: six nonlinear investigations at a painted newspaper desk, and a live chart-manipulation sandbox at an agency desk. The kit owns Motion, Sound, Read, effects and voice. SVG charts use actual viewport dimensions.
Delivered the self-contained HTML, readable source, draft metadata with stage built, notes, fifteen authored voice lines, audit states, handoff, preview and fourteen paintings.
Build only. No commits, shared-engine edits, publication or polish round.

#### Numbers check
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

#### Facts checked
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

#### Break it
- PASS: all 108 trick/headline pairs without evidence are refused; no correctness oracle appears before diagnostic evidence.
- PASS: all 108 pairs with fresh diagnostic evidence accept exactly the six canonical pairs. Correct trick plus wrong ruling is rejected as a whole.
- PASS: changing choices after a wrong filing without fresh evidence is refused. A newly opened, unrelated data sheet cannot purchase another guess. Each required diagnostic proof must be renewed.
- PASS: repeating one mark does not form a ruler pair; a third pick clears the previous ratio. Robotics requires first and last endpoints. Mixed smoothie/win units are not divided into a comparison.
- PASS: cutoff extremes, picture area in every data set, rate comparisons, crossed time-window endpoints, honest resets, saved closures and reset confirmation.
- PASS: chart controls retain node identity; real clicks work through labels and overlapping transparent hit planes route to the nearest bar center. A keyboard-only run closes a case.
- The sandbox has no pass threshold, score or saved best. Sweeping its sliders is the intended exploration. Case closure is an activity record, not a mastery score or proof against a lucky answer.
Final deterministic regression: 392/392 assertions. `post-audit-regression.json` preserves each result. `full-student-walk.json` preserves all six closures using held clicks.

#### Voice walk
Main path, default Motion on: Case 1 folder, Ruler and both bars, Axis check, both choices, File it, Fix it; then all remaining cases and their diagnostic tools, followed by Spin Room, Fact-checker's view and Make it honest. Held presses 120 ms, taps about 2 seconds apart.
Spoken starts: wCases once, ruler2 once, firstClue once, filedRight six times, each of the six closed lines once, wSpin once, factView once. The allClosed announcement was dropped when Next entered Spin Room, as its scope requires.
The side retry path speaks filedWrong once, then filedRight and the Case 5 closure once after renewed rate/data evidence. Read and Sound-off Read were also walked in `voice-side.json` before the final voice guard changes.
The firstClue instruction waits until File it is enabled. Its earlier stale queue entries remain unmarked. Events start immediately and obsolete instructions give way to the student's action. First-tap welcome cuts are allowed by BASELINE rule 16. The final full-run log verifies the once-only instructions after these fixes.
Fifteen fixed lines are authored for news-reader, Rasalgethi. No audio was recorded, per Build instructions; actual playback uses the kit's best-browser-voice fallback. Queue starts are verified, not recorded-voice quality.

#### Feel check
Played all six cases with real held clicks, then the sandbox. Best moment: the ruler exposes a four-times-area recycling picture, then the correction prints ordinary two-times bars beside it and the case receives its stamp. The school's ranking reversal and the straightened robotics trend make later cases materially different.
Flattest moment 1: the small robotics chart fell onto the laptop keyboard and its dates ran together. Refitted the painted screen and staggered dates across readable rows.
Flattest moment 2: context and rate clues became cramped labels, and the inspector could cover the live meter. Kept a dashed published-window outline, gave the ghost rates an explicit scale, and moved short-screen inspector notes above the chart.
`feel-comparison.jpg` puts the closed recycling case beside Beat Lab. Both bar tools were bundled into Scratch, opened and inspected before implementation. This build has its own material detail, lighting, large props and clear action focus; it does not look plainer than that reference. No confetti or unrelated rewards were added.

#### Done when
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

#### Wave lessons
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

#### Audit leads
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

#### Frames looked at
All own drive PNGs in Scratch: `bar-frames`, `early-frames`, `check-frames`, `check-frames2`, `voice-frames`, `final-sizes`, `final-cases`, `final-gallery`, `final-touchups`, `post-audit-frames` and `phone-frames`.
All 69 audit PNGs reviewed on nine contact sheets in `audit-sheets`; specific small ruler, rate, sheet, correction and inspector states were also checked at full size in the targeted runs. Art contact sheet and both finish-reference frames inspected.
The single full-size sweep covered 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x900, plus 375x812 through host 8795. Later shots were limited to affected states.

#### Art made
14 images: two desks, six blank publication props, six picture icons. Built-in image tool, complete prompts in art/prompts.json, raw PNGs preserved in art/raw, finished WebP through the free art.py --rekey path.
Art 821.2 KB; recorded voice 0 KB; delivered bundle 1459.3 KB against the 2048 KB goal. Art exceeded the initial 700 KB allocation after sizing for large screens; the complete file remains under the goal with voice headroom.
No generation redraws needed. Rekeyed cutouts to remove green/magenta fringe and resized to their largest intended use. All assets carry drawn_by codex, source credit and people false.
Art processing dependencies were installed only into Scratch/vendor because the available Python initially lacked NumPy. They are not bundled or runtime dependencies.

#### Art still to paint
None. No people appear.

#### Engine changes wanted
None. Shared files were not changed.

#### Left open
- Recorded news-reader clips are not made in this Build-only run. Browser speech is functional; bank-voice fidelity and future recording timing remain for the later workflow.
- The spec accepts one primary technique per case even where secondary critiques are valid, notably library rates and the smoothie baseline. Canonical answers retained; teacher notes explain this limitation.
- On a phone, reaching the chart requires scrolling below the controls. This keeps the complete ruling set visible rather than hiding answer choices.
- This was Build only. No cold review or polish round was started. Chrome debug ports 9990-9997 and host 8795 are closed; host.html removed. CIM process inventory was denied, so only port shutdown is independently verified. See cleanup.json and build-manifest.json in Scratch.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: misleading-charts

Verdict: not ready; a spec-level enumeration blocker remains. Evidence is in `_scratch/misleading-charts/`.

#### Played

Cold grade 7 play: six publications and both modes before reading the builder; handsome, investigative, with a repetitive evidence gate.

#### Findings fixed

- Blocker, general, Spin Room: a two-axis chart reported an honest primary series while ignoring the distorted wins line. Meter now names smoothies and separately measures wins; the causal caution stays visible.
- Should fix, general, filing: changing accepted choices could retain the Filed state and correction. Choices freeze on acceptance, File it disables, and keyboard focus moves to Fix it without scrolling.
- Blocker, general, robotics ruler: unrelated picks silently returned the fixed first/last slope comparison. Only the requested endpoints now produce that comparison; rejected picks clear their stray rulers.
- Blocker, general, phone Data sheet: Tab could reach covered controls. The covered panel and case folders are now inert; access restores on close and resize, with current-state speech guards.
- Should fix, general, voice/hints: wrong-answer speech invited a filing before the proof gate allowed it; hints named unrelated unused tools. Both now request the actual diagnostic recheck. Stale speech retires, and returning from Spin Room restores the pending ruler instruction.
- Should fix, general, meter: a robotics window with only equal annual gaps was still called uneven. Inspector tests the visible gaps.
- Should fix, general, access: ghost rate values disappeared on dark bars in grayscale; outlined labels stay legible. Published text no longer fades with its blinking dot. Phone hint names the chart below the controls.
- Should fix, general, compact Spin Room: the explanatory meter squeezed the chart; tightened paper margins and text without dropping its context or art.
- Should fix, general, notes: overstated standards coverage corrected; unsupported catalog mappings documented for reassignment.
- Polish, general, payoff/art: correction printing canceled the stamp animation; both now play together. Redrew the fringed flat laptop icon with shaded materials, bumpers and hinges.
- Should fix, general, audit leads: reserved a lower paper margin for the full-size stamp, moved the compact baseline note above the plot, and shortened wrong-ruling hints to fit every required size. Viewport-only animation interruption prevents the reveal itself from canceling the payoff.

#### Findings left

- Blocker, general: enumerating the trick/headline options, renewing the same ruler proof each time, closes Case 3. Reproduced with held clicks before and after fixes. Fixed-choice checking plus informative retry feedback intrinsically permits this. A new reasoning gate or different checking model would change the spec; left open per the review's scope rule.
- Should fix, general: the catalog's DC-23, DI-25 and 2017 2-DA-09 claims exceed this activity. Notes state the actual coverage; shared module changes are outside the allowed folders.
- Should fix, general: valid secondary critiques of cases 2 and 4 remain canonical-only filing rejections, as the spec explicitly requires. Named in the notes and handoff.

#### Break it

- All six checks: 108 no-evidence answer pairs refused; all six canonical filings accepted with the required evidence; no closure before Fix it.
- Case 3 cheap loop: Ruler, first mark, second mark, next trick, next ruling, File it, Fix it, repeated across the options. It closes; the blocker remains explicit.
- Repeated one-proof renewal and stale-proof retries refused. Filed-answer edits refused. Unrelated robotics endpoints refused. Same-line versus mixed-unit measurements are distinguished by the existing guard.
- Sandbox has no score or saved best. Slider sweeping is intended exploration; 999 produces 51.0 and 1000.0. All six data sets and three drawings have finite meters; honest resets clear the active tricks. Fixed the false honest/timing labels.
- 175/175 assertions in review-functional-confirmed.json. Keyboard-only real keys close Case 1. No reflection gate exists.

#### Voice walk

Held presses 0.12 seconds, gaps 2 seconds, default settings: Ruler and two bars, Axis check, both choices, File it, Fix it, Next; each remaining case's diagnostic tools, ruling and correction; Next into Spin Room, Fact-checker's view, Make it honest.
Final starts in order: ruler2, firstClue, filedRight, closed1, wCases, filedRight/closed2 through filedRight/closed6, allClosed, wSpin, factView. First-tap welcome skip is allowed; wCases fits its later fresh case. allClosed retires on entering Spin Room.

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| ruler2 / firstClue / wSpin / factView | how | 1 each | 1 each |
| filedRight | event | 6 | 6 |
| closed1 to closed6 | event | 1 each | 1 each |
| allClosed | event | 1 | 1 |

Read interrupts, works with Sound off, and a mode change releases it. Returning to a half-measured case restores the second-mark hint; verified by held-click Read. Authored lines match voice/lines.json. Browser fallback, not recorded bank takes.

#### Facts checked

- Invented places, publishers, years, units and all raw arrays: all six tables in spec.md; each on-screen source says made up. No real school is judged.
- Case 1: 2.0 drawn, 1.05 numerical, factor 20.0; extreme 51.0 and 1000.0. Case 3: doubled height and width gives area 4, data 2, factor 3. Tufte, The Visual Display of Quantitative Information (1983), chapter 2; [author-hosted formula discussion](https://www.edwardtufte.com/notebook/computing-lie-factor-by-dividing-percentages/). Independently recomputed with fractions in review-numbers.json.
- Case 2: 840/19 = 44.2, 510/12 = 42.5, 830/19 = 43.7; ten months; visits cannot establish reading habits. Spec's data and Cairo, How Charts Lie (2019).
- Case 4: exact right bounds 2/3 and 19/6 align the first/last points at 0.1333 and 0.9333; correlation does not show cause. Spec arithmetic, Cairo (2019), [Datawrapper's dual-axis guidance](https://www.datawrapper.de/blog/dualaxis).
- Case 5: 45/900, 30/300, 27/450 give 5, 10, 6 per 100; totals ratio 1.5, rate ratio 0.5. Spec arithmetic and Cairo's totals/rates principle.
- Case 6: all seven annualized steps equal 1; 19 added members across 19 years. Spec arithmetic and [Datawrapper time-series guidance](https://www.datawrapper.de/blog/line-charts).
- Bar lengths need a zero reference: Cairo (2019), corroborated by [Datawrapper's bar-baseline explanation](https://www.datawrapper.de/academy/why-our-column-and-bar-charts-start-at-zero).
- Curriculum: [official CSTA 2026 PDF](https://csteachers.org/2026-csta-pk-12-computer-science-standards/), pp. 65 and 69-70 in the printed numbering, supports DI-26 directly; DC-23 sorting/grouping is absent and DI-25 is limited. [CSTA 2017 progression](https://csteachers.org/wp-content/uploads/2025/06/2017-csta-k-12-standards-progression-chart.pdf) makes 2-DA-09 a modeling requirement. [Common Core 6.SP.B.4](https://www.thecorestandards.org/Math/Content/6/SP/B/4/) names dot plots, histograms and box plots, absent here. Notes no longer claim full coverage.

#### Sensitivity

No culture, religion, Indigenous content, hard history, bodies or people art. A cultural reviewer need only check the fictional school's stigmatizing headline is clearly a claim under challenge, never the tool's conclusion. The corrected comparison reverses that ranking.

#### Flattest moment left

Recollecting the same proof after a wrong filing remains mechanical and enables the documented shortcut. The correction payoff now prints and stamps together; the best moments, recycling area and the rate reversal, are retained.

#### Graphics

All 14 paintings inspected on contact sheets, including icons at display scale; both desks, all six blank props and the two chart modes were also inspected in live frames. They share the editorial style. No missing art tokens, lettering artifacts, people or unmarked people assets.
Redrew pic-laptop via imagegen and art.py --rekey, rejected the first transparent edit, and inspected the second at its rendered size. Retained the other 13 paintings. Compared the desk scene with the existing Beat Lab and Snowy Mail Route frames; the tactile finish holds.
Bundle approximately 1460.1 KB; art 819.8 KB. No art was removed. All required sizes, 375 iframe, grayscale, Motion off and keyboard frames inspected. Subsequent frames only cover affected states.

#### Audit

Completed once in about 29 minutes, with a 40-minute bound, Chrome 9951 and host 8755. All 73 audit PNGs inspected on ten contact sheets, with confirmed findings opened full size. No console exceptions, resize failures or controls stuck disabled; five-tap repetition rows clean.
All 170 leads reviewed: fixed the actual stamp/footer and compact axis overlaps, clipped retry hint, stray invalid measurements and covered phone keyboard controls. Re-shot affected states at each relevant size; the hint fits all eight sizes, stamp/print coexist at 120 ms and clear by 540 ms, and the stamp clears the footer at 1280, 1366 and 1920.
Remaining mechanical leads are transparent enlarged hit areas over labels, pointer-events-through SVG text, intended modal coverage and the controls-first phone layout. "1 means" is correct grammar. First-tap and rapid-tap welcome cuts follow BASELINE rule 16; no how-to or event loss was accepted on the main path.
Coverage correction: the configured spin-extreme drag originally returned no path, so its audit frames were at zero. Fixed audit-states.json. A real drag during picture growth produced 25 live updates and reached 999, 51.0 and 1000.0. The full audit was not repeated; its frozen bundle remains in review-audit/host/tool.html. Targeted evidence covers later changes.
Final targeted drives reported zero errors. Host file removed and ports 8755 and 9950-9957 verified closed. Audited and delivered hashes, checks and closure evidence are in review-validation.json.

#### Left open

- Enumeration blocker requires a spec-level decision; no extra quiz or topic was invented.
- Shared curriculum metadata needs reassignment as above. Canonical primary-trick marking retained under the spec.
- Recorded news-reader clips remain absent per the build-only recording boundary. Browser narration and queues were tested; fidelity to Rasalgethi cannot be claimed.
- On phones the stage follows the complete control set and requires scrolling, as documented in notes; primary choices stay in view.
- Unattended choices: retain the complete illustrated set and the spec's canonical filings; document contradictions instead of changing scope. No commits; repository writes stayed within the two allowed folders.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Misleading Charts handoff

#### Structure
`src.html` starts from the kit starter. It contains the responsive desk, publication and correction styles, two sets of controls, six data sets, SVG rendering, and state transitions. The shared kit owns Motion, Sound, Read, chimes and voice queuing. No family engine applies because these charts must permit intentionally misleading geometry.

The panel precedes the stage in DOM order for keyboard navigation. Wide layouts show the original and correction beside each other. Short layouts use publication/correction tabs and move the privacy/reset footer under the stage. On a phone the desk and panel stack.

`chartConfig` describes the visible chart in model units. `compare` uses that model before pixel rounding. Screen pixels only annotate the ruler. `drawChart` lays out at actual pixel dimensions. The exact right axis on case 4 is 2/3 to 19/6. Case 6 compares first and last growth steps, rather than member totals, in its line view.

Only closed case ids are stored in `mc-closed`, inside try/catch. The kit's shared Motion setting is also stored. Notebook findings and Spin Room controls are not persisted. No network requests occur in the bundled tool.

#### Decisions and contradictions
- Open question, fourteen paintings: accepted. Two desks, six blank publication props and six picture icons were made during this build, all with `people: false`.
- The brief requires the image tool; the older Art section names local FLUX. Followed the brief and used built-in OpenAI gpt-image, then the required `art.py --rekey` path. Added matching source credit.
- BUILD.md says not to draw or record; CODEX-BUILD.md and the user explicitly require painted art. Painted art was made; voice was authored, not recorded, as the build-only instruction says.
- The general Done when says every correction has lie factor 1.0, while its parenthetical allows "honest" for cases 2, 4 and 6. Used the specified contextual honest statements for those three. Rate correction uses rate for both picture and numerical comparisons, giving lie factor 1.0.
- Full year in case 2 contains ten school months. Labeled and explained this as the school year; did not invent summer values.
- The no-free-enumeration brief conflicts with a checker accepting any matching pair without evidence. Kept File it enabled when both choices are picked, but evaluate correctness only after diagnostic evidence. Each failed filing consumes its diagnostic proofs. Repeating an unrelated clue does not unlock another guess; the required diagnostic tools and ruler comparison must be used again. No score, attempt counter or new quiz was added.
- The six case numbers intrinsically match the listed trick-card order in the spec. Cards are unnumbered and displayed in a different order, removing that positional answer key.
- Baseline sliders use the full data set's minimum so moving a time window never leaves negative bar heights.
- A double-axis ruler only compares within the same quantity. Dividing wins by smoothies is not a meaningful relative change, so mixed-series picks ask for another point on the same line.
- Cases can contain secondary issues: case 2 also benefits from daily rates, and case 4 also has a nonzero baseline. The checker retains the spec's canonical technique for each case. The notes name this ambiguity; these are teaching cases, not a unique-classification test.
- Props fill the usable publication area, which can exceed the Art section's 55 percent of stage height. Readable charts and the explicit largest-item focus requirement take priority over that illustrative size suggestion. In the smallest robotics view the keyboard extends below the working paper area so its chart stays on a blank screen.
- Dense year labels stagger across rows. Compact gap annotations use "y" for years; the Notebook spells out the year gaps.
- Full-source robotics picture marks stay small to respect actual one-year spacing. Narrowing the time window lets the same painted robot appear larger without overlapping its neighbors.
- On a phone the controls precede the desk so the complete choice set and File it are initially visible. The chart is reached by scrolling. Disabled Spin Room controls have accessible descriptions and tooltip reasons; the longer reason text is visible in wide layouts.
- The standing rule against naming a disabled control takes priority over playing firstClue immediately after the first finding. It starts once both choices enable File it. The generic second-ruler line names bars, pictures and points so it fits all six cases.
- For the two line-based data sets, the first Draw as option is labeled "Lines". This describes the chart that the specification's honest spacing and separate-axis corrections preserve; its internal value remains `bars` for the common rendering path.
- Chart mark nodes retain their identity across redraws. Dense bar hit planes route pointer input to the closest center, and all marks have at least 44 px hit height. Enter and Space use the focused mark directly.
- The data sheet is a nonmodal dialog; the papers it covers are inert until it closes. On phones it is fixed within the viewport. Closing it restores the current ruling hint. Short-screen inspector notes sit above the chart so the live meter stays visible.

#### Cold review decisions
- Reproduced a blocker in the existing filing design: held clicks through all choices, renewing the required ruler proof each time, close Case 3 without interpreting anything. The earlier report's proof gate does not prevent this. There is no score or saved best, but a Closed stamp is still a check result. Fully preventing enumeration requires a spec-level change to the fixed-answer interaction. Left open under CODEX-REVIEW.md's no-new-feature rule; not described as solved.
- Filed choices are now frozen and File it is genuinely disabled after acceptance, so a student cannot replace the accepted answers while retaining the printed correction.
- Fixed the two-axis meter's misleading honest result: it now names smoothies as its main comparison and reports the wins comparison separately, with the causation caution. Do not turn a one-series lie factor into an overall chart verdict.
- An evenly spaced robotics window is flagged only when its visible time intervals actually differ. Ruler rejects an unrelated endpoint pair instead of silently measuring the fixed first and last steps.
- Wrong-filing hints now name the required diagnostic tools, and the spoken retry line agrees. Stale ruler and wrong-answer speech retires when its step ends.
- The stamp and print effects now run together; one formerly canceled the other. Published text stays readable while its small dot blinks. Motion off removes both effects.
- Final audit fixes reserve a lower paper margin for the full-size stamp, move the compact baseline annotation above the plot, shorten wrong-ruling hints, and clear stray rulers after unrelated robotics picks. ResizeObserver now interrupts effects only for a real viewport resize, so revealing the correction does not cancel the print and stamp.
- On phones the data sheet makes its covered panel and case folders inert; header controls and Close remain reachable. Closing or resizing restores access. First-clue speech waits until the sheet closes.
- The audit completed once with 73 frames, clean repetition checks and clean resize stress. Its slider path had no outer return and stopped before the physical end: the configuration now returns its path and drags beyond the thumb center. Separate native-drag evidence supplements that audited snapshot. No second full audit.
- Redrew pic-laptop with rubber bumpers, beveled material, visible hinges and a clean magenta-keyed edge. First transparent edit was rejected because the shared keyer removed dark hinges. The second painting passed the required art.py --rekey route. No kit change.
- Corrected notes' standards claims: 2017 2-DA-08 is partial, 2-DA-09 should move to a modeling activity, and 6.SP.B.4 names display types absent here. Shared module metadata and spec are outside this review's write scope.
- The official 2026 CSTA PDF confirms DI-26 directly fits chart design; DC-23 has no sorting/grouping activity here and DI-25 is limited. Notes state those limits. Catalog scope should move unsupported full-coverage mappings rather than add thin activities to this tool.
- Unattended choices follow the brief: retain the canonical primary trick per case, browser narration and the complete illustrated set. No new topics, quizzes, accounts or recording workflow.

#### Next step
Review findings, including the remaining enumeration blocker and curriculum mapping, before treating the tool as ready. No further review pass, recording workflow or publication is authorized by this run.

#### Sensitivity
No people, religion, cultures, hard history, health, law or financial guidance. School names and publishers are invented. Case 5 challenges a stigmatizing school headline through equal-sized comparisons; the correction must never endorse the original claim.

#### Engine changes wanted
None. No kit or shared files changed.

#### Build evidence
All plans, input batches, generated-art paths, number checks, functional tests, frames and mechanical audit live under `_scratch/misleading-charts/`. `art/prompts.json` records every prompt and generated-art provenance. No commits or polish round were made. Read `codex-report.md` for the final validation record and remaining gaps.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)

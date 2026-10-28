# Codex report: biased-bot

## Built

- `src.html`: both modes, seeded cards, real-pixel SVG cafeteria, adaptive panel, pointer and keyboard pad, room viewer, My cards, shared engine and kit narration.
- `tool.draft.json`: beta metadata, stage built, required modes and date, supplied sources and art provenance.
- `notes.md`: five-minute start, modes, discussion, verified table, standards actions, privacy and teacher-only Gender Shades context.
- `voice/lines.json`: 58 unique lines exported from the browser's V.allLines(), including all 33 fixed room totals; news-reader, Rasalgethi; no recordings.
- `handoff.md`: architecture, testing setup, numerical reproduction, narration conflict and engine workaround.
- `codex-report.md`: this report.
- `biased-bot.html`: generated, ignored bundle, 182,478 bytes, under 2 MB. Not committed.

Only this tool folder and the authorized scratch folder were written. The existing spec, brief and both art files were left unchanged. Both art SHA-256 hashes match the initial hashes. No commits, branch changes, stash, downloaded/generated art, recordings or internet research. All Chrome instances started for this work and both test hosts were closed. Ports 8795 and 9990 to 9992 had no listeners at closeout. Temporary host.html was deleted.

Evidence root: `S:/CurioClass-codex-scratch/biased-bot/`.

The exact stock driver command initially failed because the available Python lacked websockets; the ordinary Chrome launch also failed in the managed environment. Checks then used scratch copies of the supplied drivers, a stdlib, localhost-only WebSocket adapter, and muted Chrome with --no-sandbox. The audit's host port was changed in its scratch copy to 8795. Shared scripts were untouched. The final compact-size pass also removed the driver's --hide-scrollbars flag so native Windows scrollbars were actually visible. This exposed and verified the fix for the 44 px target edge case.

Bundle command: `$env:CURIO_DRAFT=1; python scripts/bundle_tool.py biased-bot`. It succeeds with the expected notices about deliberately unrecorded lines. Node syntax checking passes. Static inspection finds no external src/href attributes in the bundle. Drawing data is memory-only; the kit alone remembers Motion in guarded localStorage.

## Numbers check

Units: right lunches out of 10. Jar order is Room 12 / Room 9 / Room 3. Score order is Room 12 / Room 3 / Room 9.

Before building the page, `numbers.cjs` reproduced the exact templates, random-call order, seeds, first-N-per-digit rule, line interleaving, centering/scaling, 32 by 32 samples, 6-unit ink radius, 8 by 8 features and engine vote. Its generation block is byte-identical inside src.html. `independent_check.py` separately implements the numerical pipeline and nearest-neighbor vote in Python, without importing that JavaScript. Python and the browser's checkTable() match every row and every mistaken digit.

| Jars | Spec scores | Node scores | Python and browser scores | Mistakes checked |
|---|---|---|---|---|
| 15 / 0 / 0 | 10 / 10 / 6 | 10 / 10 / 6 | 10 / 10 / 6 | Room 9: four 1s read as 4 |
| 30 / 0 / 0 | 10 / 10 / 6 | 10 / 10 / 6 | 10 / 10 / 6 | Room 9: four 1s read as 4 |
| 15 / 0 / 30 | 10 / 10 / 6 | 10 / 10 / 6 | 10 / 10 / 6 | Room 9: four 1s read as 4 |
| 15 / 3 / 0 | 10 / 10 / 6 | 10 / 10 / 6 | 10 / 10 / 6 | Room 9: four 1s read as 4 |
| 15 / 6 / 0 | 10 / 10 / 10 | 10 / 10 / 10 | 10 / 10 / 10 | None |
| 15 / 15 / 15 | 10 / 10 / 10 | 10 / 10 / 10 | 10 / 10 / 10 | None |
| 0 / 15 / 0 | 6 / 6 / 10 | 6 / 6 / 10 | 6 / 6 / 10 | Room 12 and Room 3: four 1s each read as 7 |
| 3 / 0 / 0 | 10 / 10 / 5 | 10 / 10 / 5 | 10 / 10 / 5 | Room 9: two 1s read as 4; three 4s read as 1 |

No numerical difference from the spec. Evidence: `numbers.cjs`, `final-number-lines.json`, `independent_check.py`, `independent-python-results.json`.

Contrast was independently recomputed: white/brand 5.93:1, ink/paper 14.80:1, muted/paper 6.02:1, brand/paper 5.70:1, brand/tile 5.16:1, focus/paper 5.59:1; white on blue 5.28:1, green 5.49:1, berry 5.64:1; ink/pasta 8.12:1. All named pairs pass AA.

## Done when

1. PASS: `detail/done-1-start.png`, `detail/lunch-full-timed.png`, `done1.json` give [10,10,6]. Four Room 9 mistakes are exactly wrote 1, read 4; the visible list groups them as "Room 9: wrote 1, got tacos (4), 4 cards". V.log starts fixed room lines in Room 12, Room 3, Room 9 order, followed by under. The final wrong-lunch frames show tacos plus a Wanted pasta sticker and pasta icon.
2. PASS: `detail/done-2-more-same.png`, `done2.json` give [10,10,6] with Room 12 at 30. V.log includes `same`, as spoken: "More cards from the same rooms did not help Room 9."
3. PASS: `detail/done-3-three.png` gives [10,10,6] with Room 9 at 3. `detail/done-3-six.png`, `done3.json` give [10,10,10] at 6. V.log includes `all`, as spoken: "Every room got the right lunch. Bitsy learned from everyone."
4. PASS: `detail/done-4-flip.png`, `done4.json` give [6,6,10] after a perfect prior run. The eight mistakes are four 1-to-7 substitutions in each other room. V.log includes `flip`, as spoken: "Now a different room is getting the wrong lunch."
5. PASS: `detail/done-5-old.png` shows grey old results, Train enabled, Run aria-disabled true. Both handlers enforce their disabled state while preserving keyboard focus. After training, Run enables and Train disables; `detail/focus-train.png` retains focus on train.
6. PASS: a whole-pixel, uneven real pointer drag reads 1 in `detail/done-6-read.png` and `done6-read.json`. The grid has the expected two center columns of ink, with edge values 0.3125 and inner values 0.5. Three nearest cards carry Room 12 badges and labels. The early exact-stick relabel probe did not change the guess because existing grids tie exactly; this was investigated, not counted as a pass. The subsequent flagged-1 probe in `supplement/final-writing-read-and-teach.png` and `final-teach.json` changes from 4 to 1 after two correctly labeled My cards. Its three neighbors are My cards, My cards, Room 12. Real teaching clicks were held and two seconds apart.
7. PASS: `detail/grayscale.png` was viewed with all color removed. Circle, square and triangle badges plus complete room names distinguish jars and results. Viewer and look-alike frames also show shape plus name.
8. PASS: all required sizes were shot and viewed. Final compact checks with actual Windows scrollbars are `native/native-scrollbars-680x425.png`, `native/native-scrollbars-760x900.png` and their saved rectangles; Run, Train and every jar control are above the fold. At 680x425, jar step buttons are at least 44.328 by 44 px, bottom 307 px. At 760 wide they are at least 44 px in both dimensions, bottom 321 px. `audit-final/size-1366x768.png` covers the school laptop. `cleanup/phone-clean.png` and `phone-rects.json` use a 375x812 iframe on port 8795: step buttons are 55.5 by 44 px, bottom 390.1 px, with Run and Train bottom 263.1 px. No page scrolling is needed to reach these primary controls.

## Self-check (section 6)

- PASS, hint names the next control and Read speaks exactly it: hints are set synchronously, independently of speech; `voice-transition-final.json` logs Read with exactly the snapshot's ready hint. Empty, drawing, read, taught, dirty, training, running, stopped and viewer states have separate hints.
- PASS, mode-switch hint changes at once: setMode updates hint before requesting welcome; held mode switches in `voice-transition-final.json` show the correct writing and lunch welcomes and final hint. Old speech is hushed.
- PASS, how lines selected by V.heard: source inspection of hint and readPad; no how-to counters. The kit full audit's five-click repeats report no how line spoken twice.
- PASS, first action never waits behind narration: UI handlers perform actions immediately; no action awaits V.say. First held Run immediately enters running state, without a welcome ahead of it. Jar changes and training hush obsolete narration.
- FAIL, literal "No line names a disabled control": the spec itself requires mutually exclusive instructions. Required line 4 says "Press Train Bitsy, then run the lunch line again." Train is enabled only when Run must be disabled; when Run enables, Train must disable. Required writing welcome similarly names reading as a later step while an empty pad must disable Read. Required wording is preserved. `needs` guards the immediate actionable control, and valid checks guard state, but the later prerequisite-dependent control cannot already be enabled. This conflict is also recorded in handoff.md, rather than falsely marked PASS.
- PASS, no applicable event lost at two-second tap pace: after fixing duplicate event keys, `final-teach.json` logs read4-1, teachHow, learned-2, learned-3 and read1-4 all as spoken, at about 1362, 5070, 12704, 17131 and 21554 ms. Both teaching events survive. The final mode/jar/train/Read sequence logs change and ready as spoken. Stale lines and speech explicitly interrupted by Read or mode/reset are dropped on purpose. The full mechanical audit's ten repeated controls were clean.
- PASS, focus retained and none taken on load: the audit reports no rebuilt control/focus loss in its 14 fresh held-click cases; final-layout-invariants records body focus on load. Train remains focused after completion. Skip returns focus to Run in `supplement/final-skip-focus.png` and its JS snapshot. Run/Stop reuse the same element.
- PASS, nothing rebuilds under the pointer: buttons are created once; counts and disabled attributes update in place. The full audit reports no rebuilt controls. Drawings, results SVG and noninteractive counts may repaint.
- PASS, reserved hint height: 57 px in the shortest layout, 60 px in compact layouts, 66 px wide. Buttons have a fixed 54 px action row. Native scrollbar frames and read-mode frames show the long hint without covering controls.
- PASS, labels and badges: viewed every listed PNG, including all-three-at-30, 99 My cards, every room viewer, stopped/old results, narrow look-alikes and wrong-food stickers. Fixed the initial menu/story overlap, narrow empty-viewer message and compact look-alike widths. The robot name has a real-pixel 10 px floor.
- PASS, 44 px targets and unclipped hint at every size: initial and final mechanical size audits, phone rectangle test, plus final native-scrollbar measurements at 680, 800, 1000 and 760 wide. The compact panel is 316 px so real scrollbar width is accounted for. All tested native-control dimensions are at least 44 px. Scene text is at least 10 px; typography is laid out in real stage pixels.
- PASS, no unintended giveaways: this is an explorer. Room badges intentionally identify source handwriting and never enter features. No score appears before a run; jar names/ids do not encode predictions. The model sees only the 64 ink cells.
- PASS, no free sweep result: changing data only marks results old; it cannot compute a new score until Train and Run. Skip is the explicitly specified way to finish an already started run.
- PASS, honest numbers: visible text defines right lunch, identical 10-card-per-room tests, partial denominators, old/stopped states, and the 8 by 8 grid. Normalization and dataset limits are explained in notes. No synthetic result is presented as evidence about a real school.
- PASS, every module code taught by student action: E4-ALG-ML-02, alter example sources, retrain and compare fixed tests; E4-SOC-HU-18, inspect who receives wrong lunches and repair missing representation; E4-DAT-IM-11, compare group effects of selected data and contribute a personal example privately; E3-ALG-ML-02, label drawings and see changed example-based guesses. These actions work for a solo user.
- PASS, engine use: rng and uni generate examples, train('knn') and knn use exactly 64 features and k=3, evaluate groups by item.tags.room, groupBars renders results. Python, Node and browser independently agree. The engine and family doc were not edited.
- PASS, no infinite animation: both mechanical calm checks report clean. All tool animations have finite iteration counts.
- PASS, motion timing unchanged: actual 30-card durations were 27.3031 seconds on and 27.3150 seconds off. Per-card intervals were 0.9022 to 0.9225 seconds on and 0.9033 to 0.9172 seconds off, including processing overhead. Both use the same 900 ms wait. Training uses the same 600 ms wait in both settings.
- PASS, console errors resolved: detail, cleanup, last, empty-final, voice-final and native passes all report errors in 0 shots. The initial writing-mode negative-width error was traced to the engine and worked around. The generated host's initial favicon 404 was fixed and the clean phone pass has none. Early failures remain in the evidence rather than being concealed.
- PASS, Escape closes viewer and returns to jar: `detail/viewer-escape.png` and snapshot focus jar-12. A final keyboard viewer test tabs into viewer-cards and scrolls 120 px with arrow keys. Close and the scrolling grid form its tab loop.
- PASS, keyboard pen: actual Space and 24 ArrowDown events produce 25 points from [50,15] to [50,87], with the correct ink grid. Evidence: `keyboard.json`, `detail/keyboard-pen.png`.
- PASS, seventh stroke clears first: six prepared strokes, then real Space, ArrowDown, Space leave one stroke [[50,15],[50,18]]. Evidence: `detail/seventh-stroke.png` and driver JS.
- PASS, empty pad disables reading and teaching: `detail/writing-empty.png`, phone writing frame and source/native disabled properties. Clear removes the guess and neighbors as well as ink.
- PASS, all jars zero disables Train and Run and asks for cards: `detail/jars-empty.png`, snapshot dirty true with the add-cards hint. All-three-at-30 disables every More control in `detail/jars-full.png`.
- PASS, Start over empties My cards: `detail/reset-my.png` was prepared with a taught drawing; final snapshot my=0, counts 15/0/0, no result, no ink and reset focus retained.

Mechanical audit leads were individually reviewed. The full audit had seven phone overlap leads; the later size/calm audit had ten. Every one compares text below the scrolling panel's clipping edge with the separately visible stage. Screenshots show no such overlap. The later ten pairs were: result-label/story; Room 12/story line 2; Room 12/story line 3; zero-result label/menu title; zero-result label/story line 3; Room 3/queue title; zero-result label/Tacos; zero-result label/Salad; explanation/robot screen; privacy/robot name. These are clipped-content false positives, not visible collisions. All other mechanical size categories are clean. The final native-scrollbar frames verify the subsequent 316 px compact-panel adjustment.

## Frames looked at

I opened and viewed every one of the 90 PNG files below. Sizes are the actual PNG dimensions. Phone host images contain a 375x812 tool iframe, even when the outer screenshot is wider. Earlier failures are labeled below; later dedicated frames verify their fixes. All paths are relative to the evidence root above.

| PNG | Pixels | What I viewed |
|---|---|---|
| `initial/initial-1000x625.png` | 1000x625 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `initial/initial-1280x720.png` | 1280x720 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `initial/initial-1366x768.png` | 1366x768 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `initial/initial-1920x1080.png` | 1920x1080 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `initial/initial-680x425.png` | 680x425 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `initial/initial-760x900.png` | 760x900 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `initial/initial-800x500.png` | 800x500 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `initial/table.png` | 1366x768 | Viewed: Initial browser table and voice export setup, first screen. |
| `initial/writing-empty.png` | 1366x768 | Viewed: Preliminary failure: cafeteria SVG remained over writing mode; subsequently fixed. |
| `audit/calm-1366x768.png` | 1366x768 | Viewed: Motion off, first screen, no infinite animation. |
| `audit/size-1000x625.png` | 1000x625 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `audit/size-1280x720.png` | 1280x720 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `audit/size-1366x768.png` | 1366x768 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `audit/size-1920x1080.png` | 1920x1080 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `audit/size-375x812 (iframe host).png` | 395x832 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `audit/size-680x425.png` | 680x425 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `audit/size-760x900.png` | 760x900 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `audit/size-800x500.png` | 800x500 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `detail/done-1-start.png` | 1366x768 | Viewed: Start results: 10, 10, 6 and four Room 9 taco mix-ups. |
| `detail/done-2-more-same.png` | 1366x768 | Viewed: Room 12 at 30, unchanged Room 9 score. |
| `detail/done-3-six.png` | 1366x768 | Viewed: Room 9 at 6, all three scores 10. |
| `detail/done-3-three.png` | 1366x768 | Viewed: Room 9 at 3, score remains 6. |
| `detail/done-4-flip.png` | 1366x768 | Viewed: Only Room 9 training: 6, 6, 10 with 1-to-7 mix-ups. |
| `detail/done-5-old.png` | 1366x768 | Viewed: Old, greyed results, Train enabled and Run disabled. |
| `detail/done-6-read.png` | 1366x768 | Viewed: Actual uneven pointer stick, guess 1, ink grid and three badges. |
| `detail/done-6-taught.png` | 1366x768 | Viewed: Early exact-stick relabel probe, unchanged guess due tied grids; not the passing teaching demonstration. |
| `detail/final-initial-1000x625.png` | 1000x625 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `detail/final-initial-1280x720.png` | 1280x720 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `detail/final-initial-1366x768.png` | 1366x768 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `detail/final-initial-1920x1080.png` | 1920x1080 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `detail/final-initial-680x425.png` | 680x425 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `detail/final-initial-760x900.png` | 760x900 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `detail/final-initial-800x500.png` | 800x500 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `detail/focus-train.png` | 1366x768 | Viewed: After training, focused Train control retains identity. |
| `detail/grayscale.png` | 1366x768 | Viewed: All color removed, room shapes and names remain distinct. |
| `detail/jars-empty.png` | 1366x768 | Viewed: All jars zero, disabled training/run and add-cards hint. |
| `detail/jars-full.png` | 1366x768 | Viewed: Every room at 30, all More buttons disabled. |
| `detail/keyboard-pen.png` | 1366x768 | Viewed: Real keyboard-drawn stick and its grid. |
| `detail/lunch-full-timed.png` | 1366x768 | Viewed: Completed full timed run, 10, 10, 6. |
| `detail/lunch-mid-run.png` | 1366x768 | Viewed: Room 9 flagged 1 served tacos, partial bars and wanted sticker. |
| `detail/motion-off-mid.png` | 1366x768 | Viewed: Motion off during partial run, normal timing. |
| `detail/motion-off-timed.png` | 1366x768 | Viewed: Motion off completed timed run, unchanged scores. |
| `detail/reset-my.png` | 1366x768 | Viewed: Start over after teaching: My cards zero and results cleared. |
| `detail/seventh-stroke.png` | 1366x768 | Viewed: Seventh stroke clears six earlier strokes first. |
| `detail/stop-compact.png` | 680x425 | Viewed: Short-window Stop state and partial results. |
| `detail/viewer-12.png` | 1366x768 | Viewed: Full 30-card jar viewer for 12, grouped 1, 4, 7. |
| `detail/viewer-3.png` | 1366x768 | Viewed: Full 30-card jar viewer for 3, grouped 1, 4, 7. |
| `detail/viewer-9.png` | 1366x768 | Viewed: Full 30-card jar viewer for 9, grouped 1, 4, 7. |
| `detail/viewer-escape.png` | 1366x768 | Viewed: Escape closes viewer and returns focus to Room 12 jar. |
| `detail/writing-760.png` | 760x900 | Viewed: 760-wide writing layout, 300 px pad and ink grid. |
| `detail/writing-compact.png` | 680x425 | Viewed: Short-window writing, full 300 px pad in its stage scroll area. |
| `detail/writing-drawing.png` | 1366x768 | Viewed: Actual pointer drawing and matching live grid, before reading. |
| `detail/writing-empty.png` | 1366x768 | Viewed: Empty writing mode with disabled read and teaching controls. |
| `detail/writing-many-my-cards.png` | 1366x768 | Viewed: 99 My cards, readable counts and neighbor labels. |
| `supplement/final-number-lines.png` | 1366x768 | Viewed: First screen used for numerical, voice and inline-resource checks. |
| `supplement/final-short-mid.png` | 680x425 | Viewed: Compact mid-run, Stop and Skip accessible. |
| `supplement/final-short-result.png` | 680x425 | Viewed: Compact results panel deliberately scrolled to bars and mix-ups. |
| `supplement/final-short-writing-read.png` | 680x425 | Viewed: Earlier narrow result with wrapped neighbor names; later widened cards and automatic stage scroll. |
| `supplement/final-skip-focus.png` | 1366x768 | Viewed: Completed skip returns keyboard focus to Run. |
| `supplement/final-viewer-small.png` | 680x425 | Viewed: Compact Room 9 viewer, all jars at 30. |
| `supplement/final-voice-read-and-switch.png` | 1366x768 | Viewed: Earlier mode/jar/train/Read probe, later refined by final voice transition. |
| `supplement/final-writing-read-and-teach.png` | 1366x768 | Viewed: Passing flagged-1 teaching demonstration, My cards 2, read changes from 4 to 1. |
| `supplement/phone-initial.png` | 550x840 | Viewed: Phone first screen; initial host favicon 404 subsequently fixed. |
| `supplement/phone-results.png` | 550x840 | Viewed: 375-wide results panel deliberately scrolled to all bars and mix-ups. |
| `supplement/phone-viewer.png` | 550x840 | Viewed: 375-wide Room 9 viewer, full-height overlay and card grid. |
| `supplement/phone-writing.png` | 550x840 | Viewed: 375-wide writing mode, main controls, privacy and 300 px pad. |
| `cleanup/final-layout-invariants.png` | 1366x768 | Viewed: First screen used for numerical, voice and inline-resource checks. |
| `cleanup/phone-clean.png` | 550x840 | Viewed: Clean phone first screen and measured controls. |
| `cleanup/small-read-clean.png` | 680x425 | Viewed: Short-window ink grid and three readable look-alikes. |
| `cleanup/small-stop-clean.png` | 680x425 | Viewed: Stopped partial lunch line, card separated from robot screen. |
| `cleanup/viewer-keyboard-clean.png` | 680x425 | Viewed: Focused viewer grid after real keyboard scrolling. |
| `audit-final/calm-1366x768.png` | 1366x768 | Viewed: Motion off, first screen, no infinite animation. |
| `audit-final/size-1000x625.png` | 1000x625 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `audit-final/size-1280x720.png` | 1280x720 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `audit-final/size-1366x768.png` | 1366x768 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `audit-final/size-1920x1080.png` | 1920x1080 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `audit-final/size-375x812 (iframe host).png` | 395x832 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `audit-final/size-680x425.png` | 680x425 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `audit-final/size-760x900.png` | 760x900 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `audit-final/size-800x500.png` | 800x500 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `last/final-big-wrong-lunch.png` | 1366x768 | Viewed: Final school-laptop wrong lunch and feeding card. |
| `last/final-small-wrong-lunch.png` | 680x425 | Viewed: Final compact wrong lunch with wanted-food icon and 10 px robot name. |
| `empty/empty-viewer.png` | 680x425 | Viewed: Correct empty-jar hint, narrow message column found and subsequently fixed. |
| `empty-final/empty-viewer-fixed.png` | 680x425 | Viewed: Empty jar with correct hint and full-width message. |
| `voice-final/voice-transition-final.png` | 1366x768 | Viewed: Final held mode, jar, train and Read transition state. |
| `native/native-scrollbars-1000x625.png` | 1000x625 | Viewed: Final first screen, 316 px panel, actual Windows scrollbars and measured 44 px targets. |
| `native/native-scrollbars-680x425.png` | 680x425 | Viewed: Final first screen, 316 px panel, actual Windows scrollbars and measured 44 px targets. |
| `native/native-scrollbars-760x900.png` | 760x900 | Viewed: Final first screen, 316 px panel, actual Windows scrollbars and measured 44 px targets. |
| `native/native-scrollbars-800x500.png` | 800x500 | Viewed: Final first screen, 316 px panel, actual Windows scrollbars and measured 44 px targets. |
| `native/native-scrollbars-writing-read.png` | 680x425 | Viewed: Final short writing result with actual Windows scrollbars visible. |

## Engine changes wanted

- File: `kit/ml-lab.js`.
- Function: private `host(el, draw)`, inside `go`, used by `view.groupBars`.
- Problem: hiding a chart sets the host rectangle to zero. The engine forces a 60 px width, while groupBars reserves at least 80 px for labels and another 12 px, producing SVG rect width -32 and console errors.
- Exact change wanted: after reading `const r = el.getBoundingClientRect()`, return without drawing when `r.width <= 0 || r.height <= 0`. Keep the previous measured dimensions so the existing ResizeObserver redraws when a real size returns. Consider also guarding the view's available bar width.
- Why needed: mode switching legitimately hides the Lunch Line results while keeping its state.
- Tool workaround: in writing mode, keep the results at a fixed 326 px width, positioned off screen with `visibility:hidden`, and do not call `bars.update` there. The hidden chart retains valid geometry. No engine or family document was edited.

## Left open

- The literal disabled-control narration conflict described above is unresolved. Required sequential wording is preserved; the report does not claim that every later-step control is already enabled. It needs a wording decision, not an engine change.
- The supplied art still has its existing review-pending status. It was not edited or reclassified.
- Voice clips were deliberately not recorded. The bank/voice/style and complete fixed line inventory are ready; current speech uses the kit browser fallback. Queue starts were checked through V.log in muted Chrome; recorded-voice quality was not assessed.
- Verification was on Windows headless Chrome 156 with actual CDP clicks, pointer drags and keys, including a 375-wide iframe. Physical school hardware and a live classroom were not tested.

No other requested build work or verification remains open. All eight Done when items pass in these checks; the single literal narration self-check remains FAIL for the documented spec conflict.

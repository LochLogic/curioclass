# Codex report: choreography-board
## Built
Build only in the requested checkout and folders. No commits, branch operations or polish round.
Offline Build, Compare and Show; 12 starters, 24 moves, eight devices, five formations, four synthesized tracks, custom phrases, 40-version history, reasons, local save and clear.
Uses kit:curio, Curio.voice and kit:dance. The moving kit figure is temporary, as the owner requests. No people images were generated.

## Numbers check
spec-calculations.py independently recomputed all supplied numeric claims. No discrepancies.
Contrast: mint/paper 10.400, mint/panel 9.504, dark ink/mint 10.150, ink/panel 14.193, muted/panel 7.158.
Dancer colors/paper: 8.025, 9.800, 12.747, 10.107. All specified text pairs exceed AA.
24 counts at Pulse/Drift/Strut/Storm: 12.857/18.947/15.000/10.909 seconds. 96 counts: 51.429/75.789/60.000/43.636 seconds.
Maximum block: 8 x 2 x 2 + 3 x 2 = 38 counts. Three maximum blocks = 114, refused. Double time with four dancers and Canon 1 = 7 counts.
Rise's levels per dancer: 4 Low, 2 Middle, 2 High. Half time: 8/4/4. The browser hand recount for two dancers gives 16/8/8 over 32 dancer-counts.

## Feel check
Played the entire starter and an entire Show without seeking. Both ended naturally; Show used its title, changing light and bow. Best moment: four dancers passing Rise through a two-count canon while the playhead tracks the longer block.
Two flattest moments: paired Wave poses initially held the same arm shape, so I added folded-to-open wave keyframes; crowded Line arms crossed neighboring bodies, so I spread the line and fitted larger casts. Floor shapes also received native Low/High treatment.
The painted theater has strong foreground floor grain, middle-stage depth and a lit cyclorama. Bar tools were bundled into Scratch without altering their folders, opened, and viewed. Side-by-side frame evidence is _scratch/choreography-board/bar-comparison.jpg. The scene has comparable atmosphere; the code dancers remain visibly provisional.

## Done when
1. PASS: starter plays, Stop acts immediately, Loop wraps, count and playhead agree. Complete starter ends at Count 24 of 24.
2. PASS: device transformations and stacked durations checked in the browser. Retrograde begins with the original final shape; Half time 16, Double time 4, Repeat doubles, Canon delays and grows the block.
3. PASS: solo Canon, 114 counts and nine blocks refused. Exactly 96 counts accepted.
4. PASS: one clock feeds both versions; Ghost outlines render. Retrograde measures are identical, with the Same ingredients line. Half time hand recount matches. One-version Compare says No changes yet.
5. PASS: Go back appends a version, Undo/Redo restore choices, reload preserves title/custom phrases/history, Clear saved removes the storage key. Forty-version cap checked.
6. PASS: Arc and fold saved with its chosen moves and levels, appears in the library, places with Enter, and survives reload.
7. PASS: full Show finished, bowed, hid the panel; Stop cancels the title delay and Back returns immediately.
8. PASS on inspected frames: stage is 998 x 496.6 at 1366 x 768 and 912 x 448.6 at 1280 x 720. Both exceed 55% width and 60% height. Compare's equal stages together exceed the panel width. Contact stays on painted boards.
9. PASS: live device edit restarts the current block; track swap keeps the current count; Stop immediate. Measured device edit about 5 ms after icon caching.
10. PASS: all specified sizes inspected; stage/timeline/Play together on laptops, block names 12 px at 1000 x 625. Phone page overflow is zero; only the timeline scrolls sideways. Main device buttons fit at 375 and 680.
11. PASS with browser speech: Mirror teaching line once over five taps; five canon refusals all started with two-second taps; Read stops play, and no welcome plays over music. Recorded hero-coach clips remain unmade, as instructed.

## Wave lessons
- Hint and voice: PASS. Hints update synchronously, action controls named, Curio.voice heard keys, scoped validity and event keys; held-click logs saved.
- Focus and layout: PASS in targeted corrections. Phrase chips and timeline selection update in place. Keyed history focus, Try focus on editor entry, Show entry/exit focus, Save/place focus and Undo/Redo boundary focus verified. Fixed hint head prevents overlap.
- Sizes: PASS for 44 px targets and the inspected primary controls. The audit found no small-target leads. Try and Save were corrected and rechecked at 680 and 375. Secondary authoring sections intentionally scroll vertically.
- No giveaways: N/A. Open-ended studio, no scored correct option or puzzle meter.
- Honest numbers: PASS. Every-dancer/every-count definition, canon holds and rounding assumptions are stated in notes and Compare.
- Standards: PASS. Students make phrases, apply and organize devices, compare revisions and record reasons.
- Motion off: PASS. Timing is unchanged, keyframes replace interpolation, standby animation is explicitly disabled.
- Short choices: FAIL under a literal all-choices-at-once reading. The eight main devices fit, but the library, formation/history sections and 24-move palette require vertical scrolling. This preserves the specified large stage; retained as an explicit cold-review ergonomics question.
- Resize mid-animation: PASS in the full audit: no exceptions or controls left disabled. Existing actors retain state while the floor and crop resize. The later panel/focus fixes received targeted checks, not another full audit.
- Deferred welcome: PASS. No welcomeAfter; Play is a speaks control, welcome has a playback validity check.
- Unknown as unknown: N/A. No hidden factual clues.
- One look, one meaning: PASS. Badge shape and color consistently identify each dancer; device tags include symbols.
- Badge says true: PASS. Count, version, cast and formation labels derive from current data; editor labels show one dancer and eight counts.
- Hint changes back: PASS. Mode, selection, placement, reset and editor transitions replace the hint immediately.
- No answer by copying: N/A. No diagnosis quiz or answer cards.

## Audit leads
The full audit ran once and completed, reporting 461 leads. It found no console errors, no resize exceptions or stuck controls, and no infinite Motion-off animation. It is not a clean final audit: the full run preceded the corrections below and was not rerun.
All 447 listed bullet rows have individual line-numbered answers in _scratch/choreography-board/audit/dispositions.json. The other 14 walk warnings are answered below. The original 587-line report is audit.md beside that ledger.
- 11 naming rows: FIXED. Explicit aria-labels added to title and reason-note; associated visible labels were already present.
- 308 below-fold rows: RETAINED. These are secondary library, cast, formation, move, reason and history controls in the required stacked layouts at 760 and 375. Main Play and the eight device buttons fit. See the short-choice exception above.
- 16 timeline-scroll rows: INTENTIONAL. Proportional blocks and the eight editor slots scroll within their own box, as required at 375. They remain keyboard reachable. No page-wide horizontal overflow.
- 53 overlap rows: FIXED. Transport/hint moved above a separate scrolling body; the phrase editor hides the duplicate transport. Targeted frames show no transport/hint or editor-control overlap.
- 9 editor keep/hint rows: FIXED. Editor resets scroll, focuses Try, and exposes stage, slots, Try and Save. Save's bottom is 323 px at 680x425 and 721.1 px in the 375x812 host.
- 2 editor short-panel rows: FIXED for Try/Save visibility; the 24-move palette intentionally scrolls.
- 2 state focus rows: FIXED. Show opens with focus on Play; Make opens with focus on Try.
- 1 hidden Show hint row: INTENTIONAL. Show hides the panel and presents only its stage, title and slim controls, as the spec requests.
- 43 modal coverage rows: INTENTIONAL. Confirmation covers the stage and background controls. Background is now inert, focus trapped, and audit keep regions are scoped to the dialog rather than the covered stage.
- 2 quick-mode welcome rows: FIXED. Repeating an already active mode no longer hushes the line. Held taps 0.7 seconds apart produced one complete, uncut welcome in Build and Compare.
- Additional walk warnings, 10 skipped welcomes: EXPECTED. Play suppresses narration over music; phrase and block taps give their own how line priority, per STANDARDS. No welcomeAfter is used.
- Additional walk warnings, 3 focus losses: FIXED. Show entry, the version picker/list and Back now retain or deliberately transfer focus. Targeted focus checks passed.
- Additional walk warning, 1 idle Show Stop with no change: EXPECTED. There is no performance or title delay to stop on initial Show entry.
Other walk observations: Loop selecting the first block intentionally reveals its controls. Phrase and pure timeline selection no longer rebuild their buttons. Compare timeline taps now use Compare instructions and insertion gaps are disabled there.
Post-audit checks: nine held-input/state frames passed with zero errors, covering quick welcomes, panel overlap, compact/phone editor, Show focus, Compare controls, inert dialog and Clear saved. Earlier targeted focus checks verified placement, version selection and Undo/Redo.

## Frames looked at
Bar Snowy Mail Route and Beat Lab; early five frames; 11 main size/keyboard/Motion/grayscale frames plus targeted phone, portrait and compact corrections; eight interaction frames; seven extreme/mode frames; three voice frames; four full-play/event frames. Contact sheets and full frames are in _scratch/choreography-board/.
Audit contact sheets audit-0.jpg through audit-10.jpg were all viewed, covering all 81 audit PNGs. Final correction evidence: post-audit-frames, editor-final-frames, focus-final-frames and final-frames, also viewed. All artifacts are in Scratch.

## Art made
One generated empty theater, 1600 x 900 WebP, 79.6 KiB (81474 bytes). Raw PNG retained in art/raw. Built-in imagegen; no redraw required. Bundle: 291.2 KiB (298171 bytes), below 2 MB.
Full prompt and fitted crop geometry are in art/prompts.json. Credit is in metadata and source.

## Art still to paint
Owner's final direction is painted dancers. Fifty-six people:true pose assets and registration/facing/level/badge requirements are recorded for the next painter. No people assets generated in this build.

## Engine changes wanted
kit/dance.js floor.draw: explicit options to suppress engine stage decoration over a painting.
kit/dance.js level: native low floor poses and higher variants that rise upright. Local poseFor workarounds are in this tool; the shared kit was not modified.

## Left open
Painted dancer replacement and recorded hero-coach narration are intentionally deferred. Storm/Strut instrument colors use kit synth approximations.
Secondary-panel ergonomics remain open under the literal short-choice rule. The full audit was not rerun after the documented narrow fixes; do not call the final build audit-clean. Storm/Strut timbres are kit synth approximations, not acoustic recordings.
Cold review is next. No polish round was started. host.html was removed. Ports 8795, 9990, 9991 and 9992 were checked closed; all Chrome/server processes started here were shut down.
Final static checks: voice manifest matches all 19 fixed lines; no external resource URLs, no em dashes, and no source line exceeds 157 characters.

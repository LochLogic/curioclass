# Handoff: biased-bot

Built 2026-10-28 for Curio Class, grade 4, ml-lab family. The deliverable remains a draft because the supplied art is marked review pending and narration is deliberately unrecorded.

## File layout

- `src.html`: starter-based kit frame, mustard palette, responsive layouts, inline SVG cafeteria scene, canvas pad, modal card viewer, data generation, classifier wiring and narration.
- The numerical block, from `ROOMS` through `checkTable`, is identical to the standalone Node check in `S:/CurioClass-codex-scratch/biased-bot/numbers.cjs`. All eight spec rows and every mistaken digit match.
- `state` keeps jar counts separately from trained counts, current and previous evaluations, old/stopped flags, cancellation tokens, the current run and pad versions, My cards, strokes and keyboard pen. No handwriting is saved.
- `update` changes existing controls, preserving their identity. `paintScene` re-lays out real pixels per stage size. Only the background art and the robot geometry scale; scene text is at least 10 px.
- `run` waits 900 ms per card with the kit's wait, in both motion settings. Stop cancels with a token. Skip finishes immediately and restores focus to Run. Training waits 600 ms. Gear and scene animations have finite iteration counts.
- `raster` is shared by generated cards and pointer/keyboard strokes. `MLLab.train`, `knn`, `evaluate` and `view.groupBars` provide the model, guesses and results. No classifier, random generator or chart is reimplemented.
- The writing results move into view within the stage's own scroll area in short windows. Clear returns that area to the pad. The card viewer has Close and a focusable, keyboard-scrollable grid; Escape returns to the opening jar.
- `window.__tool` exposes state, mode switching, all lines, the kit voice log/queue, numerical table, model, training items, pad grid, actions, snapshots and setup hooks. `setJars` is asynchronous and includes the actual 600 ms training delay.

## Narration

`Curio.voice` owns all narration. The hint is written synchronously from state and Read returns exactly that text. Welcomes are once per mode, how-to lines use `V.heard`, and event ids are explicit. Pad events have distinct queue keys, so two teaching clicks two seconds apart do not replace each other's unstarted events. Jar changes and training hush obsolete narration. Pad version, current guess and run id checks drop stale narration.

`voice/lines.json` is exported from the actual browser's `V.allLines()`. It includes all 33 fixed room totals, in Room 12, Room 3, Room 9 order. Bank news-reader, voice Rasalgethi. No recording was made.

## Spec conflict

The literal rule "No line names a disabled control" cannot coexist with required line 4, "Press Train Bitsy, then run the lunch line again." Train is enabled only while jars are dirty, exactly when Run must be disabled; after training, Train must be disabled and Run enabled. Line 8 similarly tells an empty-pad student to write, then press a Read control that must be disabled until there is ink. The empty-jars instruction also names Train as a later step while it must be disabled.

The required sequential wording is preserved. `needs` guards the immediate enabled action, such as Train for a jar change, while the named later action becomes enabled after its prerequisite. The report marks the literal no-disabled-control self-check FAIL rather than claiming every named future control is already enabled. Resolving that literal conflict requires permission to split or change the spec's required narration. Everything else is built and checked.

## Teacher context

The Gender Shades question is resolved by the source line and the build brief: teacher notes only. Notes distinguish the paper's commercial gender-classification task from a general claim about every face-recognition system. No real region or population appears on screen or in narration.

## Engine changes wanted

- File: `kit/ml-lab.js`.
- Function: private `host(el, draw)`, inside `go`, used by `view.groupBars`.
- Problem: hiding a chart sets the host rectangle to zero. The engine forces a 60 px width, while groupBars reserves at least 80 px for labels and another 12 px, producing SVG rect width -32 and console errors.
- Exact change wanted: after reading `const r = el.getBoundingClientRect()`, return without drawing when `r.width <= 0 || r.height <= 0`. Keep the previous measured dimensions so the existing ResizeObserver redraws when a real size returns. Consider also guarding the view's available bar width.
- Why needed: mode switching legitimately hides the Lunch Line results while keeping its state.
- Tool workaround: in writing mode, keep the results at a fixed 326 px width, positioned off screen with `visibility:hidden`, and do not call `bars.update` there. The hidden chart retains valid geometry. No engine or family document was edited.

## Checking and next work

Evidence, scripts, screenshots and Chrome profiles are in `S:/CurioClass-codex-scratch/biased-bot/`. See `codex-report.md` for individual outcomes and every viewed frame.

The system Python is LibreOffice Python without the `websockets` dependency, and Chrome could not start with its normal sandbox inside this managed execution environment. Scratch copies of the supplied drivers use a stdlib-only, localhost-only WebSocket adapter and add `--no-sandbox` to the muted headless Chrome launch. The audit's iframe host was relocated from its default port-plus-one to the brief's required port 8795. Shared scripts were untouched. An initial generated-host favicon 404 was fixed with an inline empty favicon in the temporary host and tool.

Next: settle the literal narration conflict above, review the supplied art, and record the listed narration in the approved voice bank when authorized. Do not infer a need to alter any numerical rule or seed. Exact duplicate grids can tie existing examples; teaching two identical straight sticks with different labels need not change a vote, because engine ties follow training order. The checked teaching demonstration uses a flagged 1, read as 4 before teaching and 1 after two correctly labeled personal examples.

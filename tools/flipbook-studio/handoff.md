# Flipbook Studio handoff

Build only, 2026-11-04. No commits or separate polish round. All work is confined to this tool and `_scratch/flipbook-studio/`.

## Layout of the source

`src.html` starts from the kit starter and uses `kit:curio` CSS, Motion, Sound, Read, tones and the `Curio.voice` queue. It then contains the desk layout, modal tools, vector drawing and timing engine. The page is resized in real pixels by `layout()`. Drawings remain in a 960 by 720 coordinate space. `svgPath()` supplies the same smoothed curves to canvas and print.

The main sections are saved-book validation, per-page history, drawing and spacing chart, stable thumbnail controls, starter factories, editing, animation clock, printing, modal tools and input wiring. `window.__tool` exposes state, operations, voice log, clock transitions and print construction for repeatable checks.

## Tricky parts

- `requestAnimationFrame` advances against an accumulated clock deadline. Held frames do not emit extra ticks. Edits rebase the clock on the drawing being shown, rather than restarting the loop.
- A hold drag retains pointer capture on a stable slider. Playback and hold edits update controls in place. Only structural page operations rebuild the strip, restoring thumbnail focus when applicable.
- Undo and Redo snapshot strokes per page, capped at 50 undo states. Eraser measures distance to a stroke's segments and removes the complete stroke.
- Thumbnail drag reorders the pages; Alt + Left and Alt + Right provide a keyboard equivalent. The selected thumbnail is kept visible using only the strip's horizontal scroll, without scrolling the document.
- In compact landscapes and on phones, secondary tools move into a modal, then return to their original DOM positions. This preserves their event handlers. Main page operations and Play remain in view.
- Print repeats each drawing once per held frame, eight per sheet. It uses only black vector paths, cutting boundaries, frame numbers and the staple margin. No onion skin, chart or painted texture is in the print DOM.
- Saved data is validated before loading. Storage writes are wrapped in try/catch. A storage failure updates the visible hint as well as the status label.
- Spacing labels use collision-free grid rings and light gray leaders when centers coincide. Layout is cached by canvas width and book revision. All 48 labels were checked for overlap in the smallest preview.
- Each dialog keeps its own return-focus target, including a starter library opened from the compact Tools dialog.
- Re-selecting the current mode preserves its narration. The selected thumbnail is kept in view after resizing or changing modes. A live hold drag locks automatic strip following until release so its handle stays under the pointer.
- Limits and unchanged presets acknowledge that nothing changed. Print speech is valid only during the print operation and is hushed when it closes.
- Live timing speech supersedes its prior event at the next change. Hold drags announce once on release; Stop hushes it. Read retains the kit's priority. A deferred spacing explanation can play after Stop.

## Artwork and placement

Two original OpenAI gpt-image paintings are in `art/`, with prompts and raw PNGs retained. No painted people. The Blink starter is an editable schematic face made from strokes, as required by the spec.

The measured clear glass in `fb-desk` occupies approximately x=13.3%-86.8%, y=10.6%-87.6%. The page uses an inset rectangle x=15.1%-85%, y=12.7%-85.3%, intersected with the visible cover crop. Pencils stay outside this region. The paper texture is shown at 26% opacity over cream, keeping the page quiet enough for pencil strokes.

## Open questions resolved unattended

- Omit Download GIF. The spec leans toward saved work on this device plus its existing Print pages craft.
- Keep Print pages. The spec explicitly retains the physical flipbook activity; this is not a print card for transferring work between devices.
- Preserve Blink's explicit 8,1,1,1 timing, totaling 11 frames and 0.9 seconds at 12 fps. This conflicts with the general six-frame hold limit. Editing that exceptional hold returns it to the normal 1-6 range. The cold review corrected the bar to eight actual cells with a starter label. That track stays stable during a captured drag; normal holds retain six-cell tracks.
- On Real bounce drawings 3 and 9, preserve the explicitly required floor contact at y=660 with a 28-unit vertical radius. This places the squashed center at y=632, while the unsquashed formula says 620. Other drawings follow the formula exactly.
- Use the requested image tool rather than the older local-FLUX wording in the spec. The current build brief and user instruction require self-generated art during the build.
- Write `codex-report.md` last, since the user's explicit stop trigger overrides the brief's request to create it after the first bundle. Intermediate results are retained in scratch.
- Voice recordings were not made, as instructed. `friendly-dad` / Achird is recorded in the line manifest; the kit currently uses browser speech fallback.

## Engine changes wanted

None. No shared kit files were changed.

## Claude Refine fix, round 1, 2026-11-05

- `state.selected` is the student's timing selection; `state.index` is the drawing currently shown by playback. The hold readout, minus, plus and Hold the key use the selection. Explicit thumbnail and handle actions change it. Stop selects the paused drawing. A red underline marks playback separately from the selected border.
- Thumbnail canvases are painted on creation or an artwork change, with only the edited thumbnail repainted. Reorder moves existing tiles and restores focused controls. Stroke paths and centers are cached by their data; holds and frame rate do not invalidate artwork.
- Input and loaded legacy points are rounded to a tenth of a drawing unit. Legacy blue strokes remain accepted and keep their original color. New Blue pencil uses indigo so it differs from the preceding-page ghost.
- Hold drags debounce saves for 180 ms and flush on release or pagehide. Other changes save immediately. The storage warning speaks once per continuous failure, with a successful save allowing a later failure to speak again.
- Print narration finishes before the dialog opens, with the same words in the hint. Sound off opens print immediately. A second tap while narration is pending cannot duplicate printing. Canceling narration cancels that pending print. This also works in headless Chrome, which does not emit `afterprint`.
- Flip uses a slim numbered strip. Coincident chart centers use one ringed dot and an explanatory caption. Compact Draw exposes Undo beside Tools.
- The Why dialog and teacher notes now distinguish film's 24 fps twos from the starter's 12 fps twos, give a feasible bowling-ball timing recipe, define key drawings and ask students to plan their keys before in-between drawings.
- No spec open question was taken up. Keep the 12 fps starters and exceptional Blink opener. No new art, recordings or shared engine changes were needed.
- Evidence and reproducible checks are under `_scratch/flipbook-studio/fix-*` and the associated shots JSON files. The final fix report is `polish.md`.

## Validation evidence

Scratch contains the independent number recomputation, bar-tool bundles and frames, real mouse and touch input checks, saved-book reload check, functional assertions, narration logs, all-size frames and the final mechanical audit. `codex-report.md` records the final outcomes and any remaining leads.

## Cold review repairs, 2026-11-04

The cold review played the UI before reading this handoff. Keep the two measured raster paintings and the editable starter geometry.

- Dialogs now finish an active stroke and pause playback before opening. A confirmed Delete or Clear therefore applies to the drawing the student saw, rather than a later playback drawing.
- Spacing guidance now explicitly assumes equal holds, on the stage at compact sizes too. The Why text identifies 24 fps as a common film rate and states that twos means 12 drawings per second at that rate.
- Stop retries an unheard mode welcome after entering that mode during playback. Compact Flip speech names Options. Eraser has its own once-only guidance; Pencil, Onion and thumbnail selection restore matching hints.
- Modal entry hushes desk guidance. No welcome names the inert desk behind a dialog; closing without changing the book brings the still-relevant instruction back. Loading a starter from a compact drawer closes that drawer so Play is reachable. First Play and dialog-opening actions explicitly skip stale welcomes.
- The eraser tests the actual smoothed Path2D, including its stroke width. One pointer owns each stroke; another finger cannot overwrite it or finish it. Structural edits finish the current stroke and reset held-frame state.
- A separate persistent save warning remains visible through subsequent actions and is included in Read. It clears after a successful save. The warning was rechecked at 680x425 and inside a 375x812 host.
- Onion direction has a pattern as well as color: previous drawings are solid blue and following drawings dashed green. The student strokes, thumbnails, timing view and printed paths stay unchanged.
- Flat starter icons now use the starter geometry in shaded paper previews. New and copied pages settle into place briefly, and hold bars respond with short transitions. Motion off removes these movements.

Review evidence is in scratch `before/`, `after/`, `input/`, `voice/`, `phone-recheck/` and `review-audit/`. The independent functional check passed 28 assertions. The real mouse/touch walk, five-repeat narration check and keyboard navigation reported no runtime errors. Keyboard Step twice reached drawing 3; Alt + Right reordered a thumbnail, and focus stayed visible with no page scrolling.

The first custom keyboard test used an incomplete CDP Enter event; its corrected event and the standard drive.py keyboard test both passed. The test error was not a product defect.

The review audit ran once with a 40-minute deadline, Chrome 9951 and host 8755. The session interruption stopped it after all size/state checks, Motion off, held-control walks, five-repeat and quick-tap checks. Its 28 leads are retained in scratch `review-audit/audit.md`; the resize-stress phase was not completed. Do not read its provisional clean stress heading as a completed check. The audit was not restarted, following the one-pass instruction.

Final targeted rechecks covered the onion pattern, truthful eight-cell starter bar, compact modal guidance and storage recovery at their affected sizes. The saved-book, mouse/touch and keyboard checks passed. The final bundle and evidence hash are in scratch `review-validation.json`; codex-review.md records the remaining spec conflicts and validation limits.

## Next reviewer

The two numerical spec conflicts above remain explicit. The cold review's actual 375-pixel iframe checks passed, including the save warning and eight-frame starter bar. Its single audit was interrupted before resize stress; retain that limitation rather than treating the provisional stress heading as a pass. Physical printer output was not tested. See codex-review.md and scratch review-validation.json for the review evidence. No further review or polish round was started.

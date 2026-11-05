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
- Preserve Blink's explicit 8,1,1,1 timing, totaling 11 frames and 0.9 seconds at 12 fps. This conflicts with the general six-frame hold limit. Editing that exceptional hold returns it to the normal 1-6 range. Its bar fills the six available cells; its numeric label and readout retain eight.
- On Real bounce drawings 3 and 9, preserve the explicitly required floor contact at y=660 with a 28-unit vertical radius. This places the squashed center at y=632, while the unsquashed formula says 620. Other drawings follow the formula exactly.
- Use the requested image tool rather than the older local-FLUX wording in the spec. The current build brief and user instruction require self-generated art during the build.
- Write `codex-report.md` last, since the user's explicit stop trigger overrides the brief's request to create it after the first bundle. Intermediate results are retained in scratch.
- Voice recordings were not made, as instructed. `friendly-dad` / Achird is recorded in the line manifest; the kit currently uses browser speech fallback.

## Engine changes wanted

None. No shared kit files were changed.

## Validation evidence

Scratch contains the independent number recomputation, bar-tool bundles and frames, real mouse and touch input checks, saved-book reload check, functional assertions, narration logs, all-size frames and the final mechanical audit. `codex-report.md` records the final outcomes and any remaining leads.

## Next reviewer

Start with the two numerical spec conflicts above. The audit's phone-context lookup failed, so use the independent 375-pixel iframe evidence as well as an actual tablet if available. Physical printer output was not tested. No further build or polish round was started.

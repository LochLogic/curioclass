# Image Transformer handoff after cold review

## Structure
src.html uses the shared kit and 9-12 theme. CSS, stable controls, arithmetic, canvas drawing, task checks and narration follow in order.
`__tool` exposes state, arithmetic, matrix editing, geometry, redraw and voice logs for verification.

## Tricky parts
- The picture occupies (0, 0) to (4, 3), y up. The same matrix moves the grid, image, basis arrows and unit square.
- Rendering uses device pixels and a 20 percent home ghost. Singular matrices draw a collapsed boundary or origin dot.
- Animation has a cancelable token; any matrix edit, mode or Move change stops it. Resize redraws the current interpolation.
- Inputs stay mounted. Arrow targets are 44 pixels and choose the nearest tip when they overlap. Keyboard tips stay distinct.
- Compact Undo matrices retain two bracketed rows. Compact Order sliders retain their full 44-pixel interaction height and useful track width.
- responsiveControls relocates existing hints and Move buttons at short sizes; it restores active focus with preventScroll after relocation.
- Filter samples are controlled invented pixels, explicitly labeled, rather than samples taken from the painting.
- Correct Blend recovery restores the painting and controlled sample; Gray remains gray after its correct non-inverse explanation.
- Pixel-origin guesses draw an X at their actual destination, with a dashed discrepancy line to the target ring.
- Gray explanations permute the current original channels; both triples match the active displayed equation.
- Narration uses Curio.voice. The zero matrix has a separate point event; all eleven fixed lines are in voice/lines.json.
- Event occurrences use distinct queue keys so repeated singular results are not replaced before they speak.
- Re-selecting the active mode is a no-op; it preserves the current result and welcome. Reset restores a fitting Studio welcome.
- Only the Studio canvas is in the tab order. The static comparison and Undo canvases have descriptive labels and tabindex -1.
- Balloon was redrawn with built-in image generation, then processed by scripts/art.py --rekey. Lighthouse and fox remain supplied art.

## Engine changes wanted
None. All repairs are local to this tool.

## Spec constraints / Left open
- The required fixed -6 to 6 grid clips Move 3's pixel at (5, 11). Its equation remains visible. A zoom or off-grid locator would change the spec.
- Two or three full fixed grids stacked in short previews leave little space for each actual 4 by 3 picture. Controls now fit; the small mathematical image footprint remains.
- The spec's (270, 0, 0) Gray example is outside RGB range and is excluded from the UI.
- No recorded clips exist. Browser narration is retained because this pass prohibits recording.
- The spec's open question about additional 3 by 3 systems remains a curriculum decision; no extra topic was added.

## Validation
The cold reviewer played all modes and Undo cards before reading builder files. Exact rational recomputation verifies the spec's examples.
One full all-size run covers Studio, Order, Undo and Color at eight sizes; changed states receive targeted rechecks only.
Functional checks cover all inverse moves, singular rejection, origins, all three color triples, actual recovered canvas samples,
fraction and invalid inputs, determinant/area, commutation, scalar multiplication and animation cancellation.
Held-click narration, real jittered dragging, keyboard arrows, Motion off and grayscale are checked in Scratch.
The final audit status and any confirmed leads are in codex-review.md. No commits, publication or shared-kit edits.

## Cold audit closure
The single final audit completed in 1855.1 seconds, within its 40-minute limit, on Chrome 9961 and host 8765.
Its 64 leads group as 50 intentional canvas/arrow target overlays, 9 skipped welcomes, 2 static canvas tab stops,
and 3 active-mode double taps cutting a welcome. Three no-change welcome cases, both canvas tab stops and all
three double-tap cuts were repaired. Six changing presets legitimately stale the Studio welcome once their matrix
boxes change; the current hint names the next control, and Reflect/Flatten speak their own event instead.
All 107 audit frames were inspected. Motion off and mid-action resize are clean, with no exceptions or stuck controls.
Only affected voice/focus paths and overlapping-arrow input were rechecked after these repairs; no second audit.
The overlay confirmation found a real compact drag fault: changing hint/readout heights changed the canvas origin
while the pointer was held. Studio now reserves their height in short and phone layouts; the grid stays stationary.
Studio entry boxes also fit a signed three-decimal value. Native whole-pixel drags rechecked both tips at 680 and
375 wide, with the expected one-decimal precision of the small grid, and zero-matrix tips remained keyboard operable.

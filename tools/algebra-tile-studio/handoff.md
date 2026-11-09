# Algebra Tile Studio handoff

Build only. No commit, publication or polish round. All implementation is in src.html. CSS follows the starter and Grade 9 kit theme. Code sections cover integer polynomial arithmetic, content, kit voice, state, signed-cell validation, square construction, responsive SVG rendering and input.

## Important implementation details

Frame cells form an outer product. Edge signs are read from the first row and column; kinds depend on x and unit edge bands. The second x² can extend either axis. Checks require every tile in the frame and exact agreement of both the expanded factors and the signed tile inventory with the card. Shape alone is insufficient. Cards 9 and 10 use an integer factor-pair search. Mat cancellation checks exact expression invariance.

The last valid placement closes the frame automatically, lights the edges and reveals the factors. Check also runs the same exact test. No rectangle claim, arbitrary flipping, overlapping tiles, extra pile tiles and deleting terms cannot bypass the inventory comparison. No scores or work are saved.

The pile groups equal loose tiles into visible stacks. Drag or select a stack tile and tap a dashed cell. Keyboard arrows move a loose selected tile into the corner, then move by symbolic cells. F flips, T turns and Delete removes. The tray stays before the SVG tiles in keyboard order. Tile focus is restored with preventScroll after redraw. Mode state stays in memory only.

Mat finds an unoccupied spot for new tiles and side-by-side zero pairs. A full mat asks for Remove or Clear mat. Frame and Square tray additions wait until a card is selected. Square supports individual strip drags as well as Split strips. At short heights the SVG number-line dot is the primary x control; the duplicate panel slider is hidden so the x-length control stays in view.

Square adds every corner unit together with an outside negative unit. Outside unit pairs cancel exactly, leaving the remainder. Editing the square invalidates its result and requires Start over. Negative strips are formal signed-area cells, not literal negative physical lengths. The inset square uses an absolute side length. Its scale is printed because the −8 to 8 slider could otherwise require a very large inset.

## Open questions and conflicts resolved

- Keep three modes. BASELINE specifically assigns A-SSE.B.3c to exponent-rule-builder and B.4 to savings-plan. The catalog/module was not edited, because writes are restricted to this tool.
- Use built-in image generation rather than the spec's local FLUX instruction, following the user's explicit art request and the build brief. One painted studio-mat asset, people false.
- Missing kit/algebra-tiles.js and docs/families/algebra-tiles.md: use isolated local helpers without touching kit. See engine request below.
- Negative algebraic edges cannot be represented as physical negative distances. Use signed-cell bands with positive display lengths, with an explicit explanation in notes. The minimum inset is a separate absolute-length square.
- The spec's full-width tray at short heights cannot fit all seven 44 px controls in the narrowest stage. The tray wraps inside the stage at those widths. Keep controls usable and document any frame-space limitation.
- Start-report-early conflicts with the user's instruction to stop when codex-report.md is written. Keep working evidence in Scratch and create the final report as the final build action.

## Sensitivity

No people, cultural, health or body content. Review signed-area language to ensure negative edge values are never mistaken for physical negative lengths.

## Engine changes wanted

- Missing file kit/algebra-tiles.js: provide Poly, TileMat and Frame with the spec's exact integer polynomial operations, signed-cell read rule, input and zero-pair behavior. No shared file was created or changed. Local helpers can be migrated after the engine exists.
- Missing file docs/families/algebra-tiles.md: document the same API and formal signed-area treatment for negative edge pieces.

## Cold review repairs

- Dense diagrams now use a persistent full-size tile selector and 44 px movement buttons. Small SVG pieces are noninteractive pictures, rather than overlapping tiny targets. Mat and Frame retain drag and keyboard input when the drawing has room. Compact Square retains its specified guided Split and Fill path, plus selection and editing through the tile list.
- A No rectangle request displays all signed constant-factor pairs and their middle-coefficient sums. It never sets solved or plays a success chime. The specified claim remains available, as a worked explanation rather than an assessment.
- A closed frame now names the next action, and Mat's first added tile queues its editing instruction. Negative Square bands explain their signed meaning on screen. Tile bevels and outside-unit drawings were strengthened without changing the painted mat.
- New voice strings are inventoried in voice/lines.json. Review evidence is in _scratch/algebra-tile-studio/review-* and the final codex-review.md. The earlier build report is historical evidence, not a description of these repairs.
- Square editing now speaks its Start over instruction. Split, Fill and editing preserve Read priority, while ordinary narration that no longer fits gives way. The first Mat addition cuts an obsolete welcome so its editing instruction can start at the normal tap pace.

## Next review

Review the open limits and evidence in codex-report.md, especially negative-strip Square geometry, compact tile hit targets, keyboard-only completion and voice timing. This is a local draft build, not a cold-review approval.

The build audit spans a pre-fix baseline and later control guards. The cold review runs a separate final audit after its repairs. The number-line dot has a transparent 44 px hit box over a tick label; the painted dot does not cover that number.

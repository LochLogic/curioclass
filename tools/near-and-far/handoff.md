# Near and Far build handoff

## Structure

src.html starts from the kit starter. It contains local styling, the postcard stage and notebook panel,
then the content tables and camera, interaction, puzzle, narration and print functions.
Curio.voice owns the queue; the tool owns the visible hint. No family engine is imported.
The single-file offline bundle is near-and-far.html. Build with CURIO_DRAFT=1.

## Important implementation choices

- Coordinates are fractions of a true 16:10 postcard. The normalized focal length is 1.44 postcard heights.
- The Side View has a logarithmic 4 to 1000 m horizontal scale. Object heights share a linear vertical scale
  sized to the current objects; hills are a scenic-band exception. Diagram ghosts show both conflicting distances.
- Every picture has a minimum 44 px grab area independent of its painted size. The resize handle has a separate
  44 px target. The DOM nodes for objects remain stable during manipulation.
- The generated valley is shifted down 2.35 percent inside the clipped postcard so the painted shore meets
  the 42 percent horizon. The shoreline polygon and interpolated snapping edge are beside lakeLeft().
- The valley, nine supplied cutouts and the Met print were retained. Cold review redrew hills and the windmill.
- Hills use the top band as their placement cue, with size ignored. This reconciles the specified wide scenic band
  and its horizon condition; treating the bottom as an ordinary 300 m object makes those instructions conflict.
- Soft and misty use SVG color matrices toward #d9e6ee, plus reduced edge detail, rather than transparency.
- New taps stop or replace old animations and invalidate narration immediately. No interaction awaits an animation.
- Valley data and solved indices alone use the two tool storage keys; the shared kit additionally stores Motion.

## Open question decided

The spec asks whether to join the perspective family. It names Family engine: None and leans toward remaining
independent, so this build stays on its own. The ground-plane formula is shared in principle, without importing
the perspective engine or changing kit files.

## Spec discrepancies

- A balloon first fits fully at 193.7142857 m. The stated 81 px height and 89.25 px basket bottom are at 200 m,
  not at 194 m. The Sources section gives the correct 200 m example. Camera arithmetic follows the formula.
- Solid has a 25 percent ratio tolerance, so Done when 2 cannot universally imply post tops within 2 px.
  Exact solutions do meet the horizon within floating-point error. The tolerance was retained, as specified.
- Cold review replaced the supplied masonry windmill with the specified wooden tower and redrew the flat hills.
- Extreme saved objects can fall below 2 painted pixels when a large viewport is shrunk. Keeping normalized
  size and placement unchanged preserves the composition and its depth; enforcing a new pixel floor would change
  that depth. The 2 px constraint applies when editing, and the grab area remains at least 44 px after resizing.

## Art and voice

art/prompts.json records nine retained FLUX cutouts, the generated valley and two cold-review redraws with provenance.
art/public-domain.json is the supplied Met credit record. The house style is soft painted storybook gouache.
voice/lines.json lists all fixed lines, with gravel-ranger selected. No speech was recorded; browser fallback is active.

## Cold review changes, 2026-11-01

- Puzzle 3's cover goal now requires actual overlap before ticking.
- Pointer selection focuses the stable object node with preventScroll, so arrows work immediately after a click.
- A no-movement press preserves applicable speech; actual dragging invalidates it on the first movement.
- The Side View uses the true 1.5 m eye on its shared vertical scale and makes a lone small subject visible.
- Valley and Misty Hills readouts explain every incorrect fade band, rather than only misty near objects.
- Zoom spotlights are recomputed on resize, including the phone layout's first fit.
- The completed print hunt offers revisiting and gives a current next action.
- Every fixed Read hint is included in allLines() and voice/lines.json.
- Built-in imagegen redrew hills and the wooden windmill; full prompts and provenance are in art/prompts.json.

## Engine changes wanted

None. No kit or shared file was changed.

## Evidence

All scripts, screenshots, comparison frames and checks are in _scratch/near-and-far/.
numbers.json contains the independent camera and contrast calculations. functional-results.json records the
camera examples, eight puzzle solutions, incorrect overlap, storage clearing and print-hunt checks.
keyboard-results.json records a solution of puzzle 1 using only Tab, Enter, arrows, equals and minus.
The final codex-report.md gives the inspection results and any remaining limits. No polish round was started.

## Build audit disposition, before cold review

The full audit completed with 43 leads. Twenty-nine were addressed by caption/horizon layout, native checkbox size,
side-view check placement, block setting text on phones, and preserving applicable speech across quick repeats.
Twelve welcome-skip leads follow the explicit first-action rule: placing an object speaks its current drag how-to,
and the empty-Valley welcome becomes stale. Two readout keep leads remain: the secondary notebook readout needs
scrolling at 680x425 and 375 wide, while the live Side View and main controls remain in view.

Focused checks using the same audit geometry routine are clean for empty, selected cow and balloons at 680 and 375.
voice-quick-results.json records three welcomes and dragHow each starting once and remaining uncut across repeats.
The full audit was not repeated. A solved-wipe recipe was added to audit-states.json after that full run;
the same solution and wipe were separately played through the real controls and inspected.

## Cold review audit, 2026-11-01

The single full cold-review audit finished inside its 40-minute limit with 32 leads, in
_scratch/near-and-far/review-audit/. Five confirmed leads were fixed: three cropped selected-cow readouts and
two consequences of a solved-wipe recipe whose drag expressions did not return their points.
Targeted rechecks in review-audit-fixes/ show the complete readouts at 680, 1280 and 375, and an actual solved
wipe at 680, 1366 and 375. The final two readout checks have no mechanical leads or console errors.
The other 27 full-audit leads were 14 intentional hill/object overlaps, 12 expected first-action welcome skips,
and one transparent-caption hit-test false positive. All 68 audit PNGs were inspected in labeled sheets.
Motion off and resize-mid-action checks were clean. No full audit was rerun after the scoped fixes.
The compact Valley layout hides its redundant notebook title and tightens shelf spacing; the postcard stays large.
See codex-review.md for the final review, spec conflicts and voice counts.

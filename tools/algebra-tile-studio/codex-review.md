# Codex review: algebra-tile-studio
## Played
Cold Grade 9 play covered Mat additions, Frame card selection and Square completion before reading the builder's report, handoff, notes and source. The first full Frame completion came during the subsequent checks, using held inputs; card 1 also passed using keyboard alone. As a projecting teacher, the signed rectangles and exact rewrites remain the strongest teaching moment. One review pass, followed by scoped repair checks.

## Findings fixed
- **Blocker, family:algebra-tiles, Frame / No rectangle:** untouched cards 9 and 10 set `solved` and said "Right". A binary guess now requests an exhaustive signed factor-pair explanation, grants no solved state and plays no success chime. This preserves the spec's claim button without pretending it assesses factoring.
- **Should fix, general, compact input:** Frame and Square had targets about 12 to 35 px. Dense diagrams now provide a persistent full-size tile list, with 44 px movement buttons in Mat and Frame. Small SVG pieces are pictures, not overlapping hit areas. Larger views retain direct dragging and tile keys. Compact Square retains its specified Split / Fill construction and selection/editing controls.
- **Should fix, general, hint layout:** short hints could shrink beneath the next button. Hints no longer shrink; the probe instruction is shorter, and the phone tray fits one row. Checked at 680x425 and through the real 375 px iframe.
- **Should fix, general, voice:** Mat's editing instruction could wait behind an obsolete welcome and disappear at normal tap pace. The first addition now releases that welcome. Instructions no longer name a disabled Turn button.
- **Should fix, general, Square recovery:** edits hid the result but did not speak Start over. Recovery now speaks once; Split, Fill and edits preserve Read priority. A remaining "missing corner" caption on an already filled, altered square was corrected during the scoped recovery check.
- **Should fix, general, completed Frame:** its hint still requested dragging. Completion now directs the student to read their factors and zeros, then choose another card or Start over.
- **Should fix, family:algebra-tiles, negative Square:** signed widths were qualified only in notes. The completed negative-strip scene now explains that hatching subtracts and drawn widths show magnitude.
- **Polish, family:algebra-tiles, payoff and art:** added a finite 400 ms edge-light response, strengthened tile bevels and small material details, and enlarged the outside remainder tiles. Outside labels follow those tiles without overlap. Kept the painted mat, palette, hatching and exact stretchable geometry.
- **Should fix, general, focus:** compact selection uses stable native controls; focus moves to the tile list when a focused large tile becomes a small diagram, and the number-line dot retains focus after redraw.
- **Should fix, general, compact instructions:** the phone Frame tip still suggested tapping its noninteractive diagram, and a caption touched the loose pile. The tip now names the tile list and arrow buttons; the caption sits clear at the bottom. Compact Mat uses the same spoken and visible controls. Real phone keyboard input placed and moved tiles successfully in both modes.

## Findings left
No known product blocker remains in the exercised paths. The mechanical audit did not finish, so this is not a full audit approval. The unavailable shared engine and catalog scope are named under Left open.

## Break it
- **Frame Check / automatic closure:** repeated empty Check never passed. Wrong sign, wrong kind, missing corner, overlapping tiles and an extra unused term all failed. Exact full constructions passed on all eight cards, in both factor orientations. Native held selection/cell placement and a jittered real drag were also exercised.
- **Zero-pair requirements:** cards 5 and 6 failed with every insufficient pair count, then closed with respectively two and three x zero pairs. Their factors and difference-of-squares text are exact.
- **No rectangle:** tried every card, plus five two-second taps on an untouched impossible card. Claims are refused on 1 to 8; 9 and 10 show all signed constant-factor sums. No claim earns `solved`, a badge or a stored result.
- **Square:** Fill before Split stayed unavailable; direct callback checks also refused it. Repeating Fill did not add more tiles. Changing the inventory invalidated the rewrite and blocked rebuilding until Start over. All six minimum insets vanish at their independently calculated x values.
- **Meters / cheap slider sweeps:** tile count reports inventory, not achievement. Sweeping x length from 1.3 to 4.7 never changes fit correctness. The number-line minimum is a labelled exploration, not an assessment. Square's two buttons are a guided demonstration, not earned mastery.
- **Mat:** exact signed expression and zero-pair invariance checked, including x² + 3x − 2 and value 12.56 at x = 2.6. A jittered real opposite-strip drag left expression 0; an immediate Add unit during the fade produced exactly 1 and cleared the ghosts. No score, saved best or reflection gate exists.
- Evidence: `review-before/`, `review-after/`, `review-logic-final.json` (175 passing browser assertions), and `review-walk/` in Scratch. The early final string assertion was a UTF-8 test-loader error, corrected before the passing run.

## Voice walk
Default Sound and Motion, real 120 ms held clicks at a two-second pace: plain stage tap, Mat additions, Frame, card selection and Check, Square, card selection, Split strips, Fill the corner, then the number line.
Spoken order: `wMat`, `matAct`, `wFrame`, `frameAct`, `wSquare`, `squareAct`, `fillAct`, `square`, `probeAct`. Every mode's how-to started once. Mode switches cut obsolete speech; skipped queued gap speech did not spill into Square.
Side paths: Read first speaks only the hint; Read works with Sound off; a mode switch releases Read promptly; Read during Split is not cut; altering a completed Square speaks `restoreAct` and hides its result. Logs checked against the visible state, using muted Chrome, not an audible audition.

| Line / kind | Expected | Spoken |
|---|---:|---:|
| Main mode / how lines | 1 each | 1 each |
| Empty Check gap / event | 5 | 5 |
| Zero pair added / event | 5 | 5 |
| Completed Check / event | 5 plus automatic close | 6 |
| Frame done / how | 1 | 1 |
| Square / event across rebuild | 2 | 2 |
| Restore / how | 1 | 1 |
| Compact Mat / how | 1 | 1 |

Twenty fixed lines match `allLines()` and `voice/lines.json` word for word. Main and side logs: `review-walk/final-voice-evidence.json`; keyboard and repeated completion logs: `review-walk/evidence.json`.

## Facts checked
| Fact | Named source and independent check |
|---|---|
| Terms, coefficients, constants, expression structure, factors, zeros and minimum | [Common Core A-SSE](https://www.thecorestandards.org/Math/Content/HSA/SSE/) and [OpenStax Elementary Algebra 2e 1.2](https://openstax.org/books/elementary-algebra-2e/pages/1-2-use-the-language-of-algebra). Each listed skill is exercised, rather than only named in notes. |
| Every one of the eight frame products, signs and zeros | [OpenStax Elementary Algebra 2e 7.3](https://openstax.org/books/elementary-algebra-2e/pages/7-3-factor-trinomials-of-the-form-ax2-bx-c); independently expanded every product and substituted every zero, including −1/2 on cards 7 and 8. |
| Cards 9 and 10 have no whole-number factor rectangle | The same OpenStax factor-pair method; independently enumerated all signed constant-factor pairs. No sum is respectively 1 or 0. |
| Corner size (b/2)², remainder c − (b/2)², minimum at x = −b/2 | [OpenStax Intermediate Algebra 2e 9.2](https://openstax.org/books/intermediate-algebra-2e/pages/9-2-solve-quadratic-equations-by-completing-the-square). Corners 9, 4, 16, 9, 1, 4; minima −4, 3, 0, 1, −4, −4 at −3, −2, −4, 3, −1, 2. Every rewrite expanded and checked over the whole half-step probe range. |
| Opposite matching tiles sum to zero; tile lengths are representational | [NCETM Algebra Tiles guidance, pp. 3 to 5](https://www.ncetm.org.uk/media/dj5o223w/ncetm_ks3_representations_algebra_tilespdf.pdf), plus exact inventory invariants. The spec's NCTM Illuminations URL returned 402 and could not be verified live. NCETM also names the limitations of negative-area models; the screen and notes distinguish signed bands from physical negative lengths. |
| Mat value and contrast | Independent arithmetic gives 12.56. WCAG relative-luminance calculations reproduce brand/panel 9.05:1, brand/secondary 8.57:1, brand ink 9.32:1, and tile-ink contrasts 9.97, 11.73, 13.23 and 8.41:1. Detailed calculations: `review-numbers.json`. |

## Sensitivity
None requiring a cultural review: abstract algebra only, with no people, culture, religion, history or body content. The signed-area representation needs mathematical care, described above, rather than a cultural judgment.

## Flattest moment left
Square still follows Split then Fill. It is an intentionally guided demonstration in the spec, so supplying the corner is not an earned challenge. The completion response, larger remainder tiles and disappearing inset make its consequence clearer without adding a quiz.

## Graphics
Inspected the studio-mat painting at its final 1440x900 size and in every mode. Kept this strong asset; no missing art tokens, new raster assets or people images. Improved exact vector tiles and the weak tiny outside units, rather than replacing the mathematical drawing with a painting.
One coherent mat/blue/green/gold/red set. Positive and negative signs remain clear in grayscale. Motion off stops the idle lamp and decorative effects. Viewed both existing bar tools without rebundling or editing them; the studio keeps its tactile mathematical identity.
Raster art: 195.4 KB. Final bundle: 353.8 KB. Frames inspected in `review-cold/`, `review-play/`, `review-cards/`, `review-before/`, `review-after/`, `review-full/`, `review-walk/` and the scoped `review-last/`, `review-phone-final/` and `review-cancel/`.

## Audit
**Audit not finished.** The single final attempt used a 2400-second limit, Chrome port 9951, host 8755 and the required review profile. It exited before its first size completed with `ConnectionResetError: [WinError 64]` in the CDP connection.
No `audit.md`, leads or audit PNGs were emitted. The failure receipt is `review-audit-attempt.txt`; only host copies exist in `review-audit/`. No second audit was run. Manual coverage includes all eight STANDARDS sizes, real hosted phone input, keyboard completion, grayscale, Motion off, both slider extremes, every card's algebra and main/side voice paths. Manual test consoles were clean; self-containment, required notes headings and the voice inventory passed. Automatic resize stress remains unverified.

## Left open
- The full mechanical audit is unverified. Keep beta status; this report does not claim its gate passed.
- `kit/algebra-tiles.js` and its family document are absent. The isolated local implementation stays; no kit files were changed. The exact requested shared APIs remain recorded in handoff.md.
- The catalog still uses broad A-SSE.A / A-SSE.B cluster labels. BASELINE assigns exponential rewriting and geometric series elsewhere. No fourth mode was added and no catalog file was changed outside the authorized folders.
- Negative bands remain a formal signed-area model, and the small inset has its own printed scale. Changing those spec choices would need a separate design decision.
- No recorded narration, audible audition, physical touchscreen or screen-reader hardware test. Browser voice timing and keyboard behavior were exercised.
- Procedural note: the first brief/memory read commands lacked a hard process deadline. Subsequent commands used bounded runners. Two early keyboard harness failures were corrected to send Enter as drive.py does; no product change was needed for keyboard completion.
- Unattended choices followed the spec and BASELINE: retain three modes, keep the successful painting, use tool-local controls instead of changing the missing engine, and preserve the binary claim only as an unscored worked explanation. No git commits or shared-file edits.

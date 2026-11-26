# Algebra Tile Studio: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: algebra-tile-studio

#### Built

Built Mat, Frame and Square, all ten Frame cards and six Square cards, in one offline HTML bundle. Tactile signed tiles sit on a generated studio mat. The last valid placement lights the factor frame automatically. Individual Square strips can be dragged, or Split strips builds both edges. Corner filling cancels outside unit pairs and exposes the remainder and minimum. No score or work is saved.

The specified algebra-tiles engine and family document are absent. Exact local helpers are isolated in src.html. No shared engine was edited. This is a beta build with the accessibility limits below, not a cold-review approval. No commit, publication, registration or polish round.

#### Numbers check

Independent exact arithmetic: `_scratch/algebra-tile-studio/numbers.py` and `numbers.json`.

- Eight products expand to the specified integer coefficient triples. Zeros also checked, including −1/2 for cards 7 and 8.
- Cards 9 and 10 have no integer factor pairs with the required middle coefficient.
- Cards 5 and 6 need respectively two and three pairs of opposite x strips.
- Square corners: 9, 4, 16, 9, 1, 4. Remainders: −4, 3, 0, 1, −4, −4. Minimum locations: −3, −2, −4, 3, −1, 2.
- x² + 3x − 2 at x = 2.6 is exactly 12.56. All stated base-color contrast ratios agree with the spec's rounding.
- Contrast: sky blue on panel 9.048:1; on section 8.574:1; brand ink on sky blue 9.322:1. Tile ink on blue, green, yellow and red: 9.973, 11.735, 13.231 and 8.408:1.
- 60 browser assertions passed before the final presentation fixes. The final source passed 55 logic assertions, including full-mat bounds. Targeted browser checks covered the later changes.

#### Facts checked

| Student-facing fact | Named source and verification |
|---|---|
| Terms, coefficients, constants, structure, factors and zeros | [CCSS A-SSE](https://www.thecorestandards.org/Math/Content/HSA/SSE/), checked live. Each expression and zero independently recomputed. |
| Rectangle edges multiply to the quadratic; signs multiply cell by cell | OpenStax Elementary Algebra 2e 7.3, named in the spec; integer expansion and signed-cell tests cover every card. |
| Half the middle coefficient determines the corner; the remainder is the minimum when the square vanishes | [OpenStax Intermediate Algebra 2e 9.2](https://openstax.org/books/intermediate-algebra-2e/pages/9-2-solve-quadratic-equations-by-completing-the-square), checked live, plus independent exact arithmetic for all six cards. |
| Opposite matching tiles add zero and preserve the expression | NCTM Illuminations Algebra Tiles, the spec's named source; its linked page returned HTTP 402, so live access was not verified. The identity and removal invariant were independently tested. |
| Variable x edges stretch together; a unit remains one unit | Algebraic definitions in the spec and independent geometric measurement. Frame units measured 57.924 px at both x-length extremes; Square units measured 49.353 px at both extremes in that viewport. |
| All numeric expression, value, factor, corner, remainder and minimum readouts | The exact calculations above, FRAME/SQUARE content, and functional-results.json. No unrelated factual content added. |

#### Break it

- No score, saved best, progress meter or reflection gate exists. Tile count reports inventory only.
- Frame Check: tried empty frames, deletion, an extra pile tile, overlap, a wrong sign, a wrong tile kind and incomplete inventories. All refused. Full rectangles require exact factor expansion and exact signed inventory, with the entire pile used.
- Reversed factor order and a transposed leading-two rectangle pass. Simultaneously negating both factors remains an accepted equivalent arrangement.
- Cards 5 and 6 cannot obtain the necessary signed strip counts with too few zero pairs. Adding pairs preserves the exact expression. A jittered real drag canceled opposite Mat strips and left zero tiles and expression 0.
- No rectangle was tried on every card: refused on 1 through 8, accepted on 9 and 10. This is an unscored claim with factor-pair feedback; a lucky binary guess earns no persistent result.
- Square: Fill before Split does nothing; repeated Fill cannot inflate the corner; changing the inventory blocks construction. Editing a completed square removes its completed rewrite and requires Start over. This last misleading-state exploit was found and fixed.
- Sweeping x length cannot change a fit result. The number-line slider is an unscored exploration of the displayed square, so reaching its labelled minimum is intentional.
- Repeated Mat additions stop when no free spot remains. Inventory and expression stay exact. New zero pairs occupy free side-by-side positions, rather than hiding under earlier pairs.

#### Voice walk

`voice-walk.json`: real held clicks, two-second tap pace, default Sound. Main spoken order: wMat, wFrame, frameAct, wSquare, squareAct, fillAct, square, probeAct. The path used Mat tiles, Frame card selection and Check, then Square selection, Split and Fill. No exceptions. Read followed by Start over and rebuilding spoke the Square event again while how-to lines remained once-only.

The audit found one lost Zero pair event in five taps. Fixed with short event speech, unique event keys and retention through Read. Targeted logs `zero-five.json` and `zero-after-read.json` each show five of five events spoken. Frame success and gap events also have unique occurrence keys: `closed-five.json` and `gap-five.json` each show five of five events at a two-second tap pace. Repeated empty Clear and active-mode taps now leave their current instruction playing; `clear-quick.json` and `mode-quick.json` show no cuts. The final hint names the number-line dot, which remains available in compact views.

Seventeen fixed lines use wise-mentor metadata, the kept Gacrux bank entry, and Curio.voice. No recording was made, as instructed. Tests used muted Chrome and verified the narration log, not an audible human audition. The final minor hint wording was inventoried after the main walk.

#### Feel check

Best moment: the last unit tile closes the rectangle, lights its edges and turns the student's placement into factors and zeros. Verified with automatic-result.json and a complete keyboard-only first card.

Two flat moments and their build fixes: the early rectangle was small and stranded in a corner, so it was centered and given more of the working area; Square initially left canceling outside piles on screen, so the pairs now cancel and leave the actual remainder, including an empty outside area for a perfect square. Individual strip dragging and immediate placement feedback keep Square connected to the same physical tiles.

Viewed both bar tools. `bar-comparison.png` puts this tool beside Beat Lab. The tile bevels, shadows, hatching and generated material surface give the algebra objects weight. Its lower control density is appropriate to this one area model. This is a build feel check, not an owner approval or an assertion that the small-preview limitations are acceptable.

#### Done when

| Item | Result and evidence |
|---|---|
| 1. Mat expression and cancellation | PASS: exact x² + 3x − 2, 12.56; native jittered opposite-strip drag removes both and preserves 0. |
| 2. Card 1 factors and zeros | PASS: exact rectangle, (x + 2)(x + 3), zeros −2 and −3. Keyboard run also completed it. |
| 3. Cards 5 and 6 zero pairs | PASS: required counts, correct factors, and difference-of-squares text. Grayscale card 6 inspected. |
| 4. Leading-two card and bad unit | PASS: card 7 closes; wrong unit kind is in frameRead.bad and receives the outline and reason. |
| 5. No rectangle | PASS: every card's claim tested against an independent integer pair search. |
| 6. Square cards and vanishing inset | PASS arithmetic: every rewrite and minimum tested; all six insets have width 0 at their minima. The physical signed-area and inset-scale qualification below remains. |
| 7. x length | PASS: x edges change and unit size is invariant; both extreme fit checks remain true. |
| 8. Main visual focus | PASS: Mat, Frame and Square are the largest objects in their stages at 1000x625 and 1366x768. Frames inspected. |
| 9. Interruptible motion | PASS implementation and audit resize paths: no animation lock or delayed mutation. State is synchronous; new input finishes decoration. Zero-pair and corner durations are 250 and 400 ms, instant with Motion off. |
| 10. Keyboard, sign, voice and small layouts | FAIL the strict overall accessibility bar: keyboard card 1 passes, negative signs survive grayscale, main controls remain visible, but dense Frame/Square tile targets fall below 44 px in small views. |
| 11. Runtime and wording | PASS packaged tool: clean standalone browser paths, inline assets, no external resource references, no em dashes and Curio Class written in full. Host-harness 404s and failed driver attempts are excluded and recorded below. |

#### Wave lessons

| Lesson | Result |
|---|---|
| Hint and voice | PASS targeted main and side walks, immediate hints, Read priority, repeat events and once-only how lines. |
| Focus and layout | PASS keyboard first card; compact Fill moves focus to the SVG dot. Controls persist while hints reserve space. |
| All sizes and 44 px | FAIL individual dense tile targets. Main controls pass, including the final 375 px measurements. |
| No giveaways | PASS construction checks inspect geometry and inventory. No factor answer or score is exposed before a valid construction; the specified unscored No rectangle claim remains binary. |
| Honest numbers | PASS exact integer coefficients, signed area, labelled drawing x, separately labelled inset scale. |
| Standards | PASS listed tile-work standards. A-SSE.B.3c and B.4 remain outside this tool, per BASELINE. The module catalog was not edited. |
| Motion off | PASS finite effects become instant and the idle lamp stops. Audit found no infinite running animation. |
| Short choice sets | PASS native card selector; no custom hidden answer list. |
| Resize mid-animation | PASS no exceptions or animation locks. Ten changed-enabled comparisons are explained below. |
| Late welcome | PASS no welcomeAfter; repeated active-mode clicks no longer hush their welcome. |
| Unknown shown honestly | PASS unfinished frame remains dashed, altered Square hides the result, and no card means additions wait. |
| One look, one meaning | PASS positive solid, negative hatch and minus glyph, dashed empty cell, white selected outline. |
| Badges tell the truth | PASS factors and closed status require an exact construction; no saved achievement. |
| Hints change back | PASS mode state retained; current action, restoration, gaps and results update synchronously. |
| No answer by copying | PASS a rectangle must actually be assembled. Square's explicit guided construction is an exploration, not a scored quiz. |

#### Audit leads

Single audit completed: 131 mechanical leads and 50 frames. `_scratch/algebra-tile-studio/audit/audit.md` is preserved. No second audit was run. The audit spans its earlier baseline and later fixes, so its rows are not a final clean bill.

| Lead group, covering every reported category | Disposition |
|---|---|
| Mat mode width 39 px; narrow expression terms; short Mat x hit area | Fixed. Targeted measurement gives 44x44 for the mode and terms and at least 44 px height for Mat tiles. |
| Loose unit stack hit area overlaps ×6 | Fixed: badge follows max(44, tile width), with a gap; compact pile frame inspected. |
| All small Square strip/unit/x² targets, including compact and stacked views | LEFT OPEN: true individual geometry is too small. Keyboard and tray controls remain usable, but this does not satisfy the 44 px rule. |
| Number-line dot hit box overlaps tick 0 | Transparent-target false positive for painted overlap: the actual dot does not cover the number. The generous 44 px hit area is retained. |
| Square heading overlaps its edge label at short heights | Fixed: compact edge-label baseline and type size separated; final compact frame inspected. |
| x-length control below panel fold in completed Square | Fixed: duplicate expression removed in short layouts; the stage dot replaces the duplicate compact panel probe; all controls verified at 680 and final 375. |
| Iframe context missing; no hint in that failed host page | Harness failure: an orphan test host served the tool directory instead of the audit's host directory. Identified by exact process arguments and closed. Independent final 375x812 tests cover all three modes with no page overflow. |
| Five first-action welcomes not heard | Permitted by BASELINE rule 16. The action runs immediately; current instructions stay in the hint and Read. |
| Quick mode welcome and empty Clear instruction cuts | Fixed: retapping an already active mode or an already empty Mat no longer hushes current speech. Targeted logs inspected. |
| Zero pair event spoken only four of five times | Fixed and retested: five of five normally and five of five after Read, no dropped events. |
| Ten resized controls reported left disabled | Baseline mismatch after intentional no-card guards were added during the audit. Loading a card enables its tray; no-card additions are deliberately disabled. No runtime exceptions or animation locks were reported. |

#### Frames looked at

Looked at both bar frames; default and functional frames; all 12 full-run frames covering every STANDARDS size, negatives, leading two, perfect square, Motion off and grayscale; nine targeted frames; native drag, keyboard and voice frames; and every later fix frame. All 50 audit PNGs were inspected on seven contact sheets, with `audit-sheet-map.json` identifying each source frame. Final 375 px Mat, Frame and Square frames were inspected individually. Failed host/driver artifacts are preserved separately and are not counted as passes.

#### Art made

One studio-mat painting, made with the built-in image tool, saved in art/raw/studio-mat.png and converted with art.py --rekey to art/studio-mat.webp. Full house style and prompt are in art/prompts.json; drawn_by is codex, people is false. First candidate retained after final-size inspection. No downloaded images or recorded audio.

Art: 200,120 bytes, 195.4 KB, above the initial 150 KB estimate. Voice assets: 0 KB. Final bundle: 357354 bytes, 349.0 KB, comfortably below the 2 MB goal. Tiles, signed hatching, frame, unit grid, number line and inset remain exact responsive vectors.

#### Art still to paint

None. No people assets are needed or present.

#### Engine changes wanted

Missing kit/algebra-tiles.js: provide the spec's Poly integer/fraction API, TileMat input/zero-pair API and Frame.read signed-cell contract. Missing docs/families/algebra-tiles.md: document those APIs and signed-area treatment. The local implementation can then migrate; no shared file was created or changed.

#### Left open

- Dense compact Frame/Square targets miss 44 px; phone tile labels and the physical construction are small. This is the main unresolved build limitation.
- Negative edge bands are formal signed areas drawn with positive display widths. They are not literal negative physical distances. The inset is drawn at its own printed scale to keep it small, a deliberate qualification of the spec's unit-scale request.
- No recorded wise-mentor audio or audible audition, physical screen reader, touch hardware or school Chromebook test. All browser testing was muted.
- NCTM's linked page could not be fetched live. Initial interactive driver attempts timed out; smaller retries and later runs succeeded. An experimental phone route returned 404; subsequent proper hosted phone checks passed. Parent host favicon requests also produced 404 logs, outside the packaged tool.
- Procedural exception: I mistakenly rebundled the two reference bar tools, regenerating ignored reference HTML outside the allowed write folders. Their source files were not edited. I made no git operations and made no further edits in those folders.
- The earliest read commands lacked a hard process deadline. Later commands used bounded runners. LibreOffice's Python launcher also left host children; exact matching tool-host processes were identified and closed, and the runner was corrected to invoke the actual Python binary.
- Open question resolved: retain three modes and leave exponential rewriting and series to their assigned tools. The restricted module/catalog files remain untouched.

Final validation and process-cleanup evidence: `_scratch/algebra-tile-studio/final-manifest.json`. Build only stops with this report.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: algebra-tile-studio
#### Played
Cold Grade 9 play covered Mat additions, Frame card selection and Square completion before reading the builder's report, handoff, notes and source. The first full Frame completion came during the subsequent checks, using held inputs; card 1 also passed using keyboard alone. As a projecting teacher, the signed rectangles and exact rewrites remain the strongest teaching moment. One review pass, followed by scoped repair checks.

#### Findings fixed
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

#### Findings left
No known product blocker remains in the exercised paths. The mechanical audit did not finish, so this is not a full audit approval. The unavailable shared engine and catalog scope are named under Left open.

#### Break it
- **Frame Check / automatic closure:** repeated empty Check never passed. Wrong sign, wrong kind, missing corner, overlapping tiles and an extra unused term all failed. Exact full constructions passed on all eight cards, in both factor orientations. Native held selection/cell placement and a jittered real drag were also exercised.
- **Zero-pair requirements:** cards 5 and 6 failed with every insufficient pair count, then closed with respectively two and three x zero pairs. Their factors and difference-of-squares text are exact.
- **No rectangle:** tried every card, plus five two-second taps on an untouched impossible card. Claims are refused on 1 to 8; 9 and 10 show all signed constant-factor sums. No claim earns `solved`, a badge or a stored result.
- **Square:** Fill before Split stayed unavailable; direct callback checks also refused it. Repeating Fill did not add more tiles. Changing the inventory invalidated the rewrite and blocked rebuilding until Start over. All six minimum insets vanish at their independently calculated x values.
- **Meters / cheap slider sweeps:** tile count reports inventory, not achievement. Sweeping x length from 1.3 to 4.7 never changes fit correctness. The number-line minimum is a labelled exploration, not an assessment. Square's two buttons are a guided demonstration, not earned mastery.
- **Mat:** exact signed expression and zero-pair invariance checked, including x² + 3x − 2 and value 12.56 at x = 2.6. A jittered real opposite-strip drag left expression 0; an immediate Add unit during the fade produced exactly 1 and cleared the ghosts. No score, saved best or reflection gate exists.
- Evidence: `review-before/`, `review-after/`, `review-logic-final.json` (175 passing browser assertions), and `review-walk/` in Scratch. The early final string assertion was a UTF-8 test-loader error, corrected before the passing run.

#### Voice walk
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

#### Facts checked
| Fact | Named source and independent check |
|---|---|
| Terms, coefficients, constants, expression structure, factors, zeros and minimum | [Common Core A-SSE](https://www.thecorestandards.org/Math/Content/HSA/SSE/) and [OpenStax Elementary Algebra 2e 1.2](https://openstax.org/books/elementary-algebra-2e/pages/1-2-use-the-language-of-algebra). Each listed skill is exercised, rather than only named in notes. |
| Every one of the eight frame products, signs and zeros | [OpenStax Elementary Algebra 2e 7.3](https://openstax.org/books/elementary-algebra-2e/pages/7-3-factor-trinomials-of-the-form-ax2-bx-c); independently expanded every product and substituted every zero, including −1/2 on cards 7 and 8. |
| Cards 9 and 10 have no whole-number factor rectangle | The same OpenStax factor-pair method; independently enumerated all signed constant-factor pairs. No sum is respectively 1 or 0. |
| Corner size (b/2)², remainder c − (b/2)², minimum at x = −b/2 | [OpenStax Intermediate Algebra 2e 9.2](https://openstax.org/books/intermediate-algebra-2e/pages/9-2-solve-quadratic-equations-by-completing-the-square). Corners 9, 4, 16, 9, 1, 4; minima −4, 3, 0, 1, −4, −4 at −3, −2, −4, 3, −1, 2. Every rewrite expanded and checked over the whole half-step probe range. |
| Opposite matching tiles sum to zero; tile lengths are representational | [NCETM Algebra Tiles guidance, pp. 3 to 5](https://www.ncetm.org.uk/media/dj5o223w/ncetm_ks3_representations_algebra_tilespdf.pdf), plus exact inventory invariants. The spec's NCTM Illuminations URL returned 402 and could not be verified live. NCETM also names the limitations of negative-area models; the screen and notes distinguish signed bands from physical negative lengths. |
| Mat value and contrast | Independent arithmetic gives 12.56. WCAG relative-luminance calculations reproduce brand/panel 9.05:1, brand/secondary 8.57:1, brand ink 9.32:1, and tile-ink contrasts 9.97, 11.73, 13.23 and 8.41:1. Detailed calculations: `review-numbers.json`. |

#### Sensitivity
None requiring a cultural review: abstract algebra only, with no people, culture, religion, history or body content. The signed-area representation needs mathematical care, described above, rather than a cultural judgment.

#### Flattest moment left
Square still follows Split then Fill. It is an intentionally guided demonstration in the spec, so supplying the corner is not an earned challenge. The completion response, larger remainder tiles and disappearing inset make its consequence clearer without adding a quiz.

#### Graphics
Inspected the studio-mat painting at its final 1440x900 size and in every mode. Kept this strong asset; no missing art tokens, new raster assets or people images. Improved exact vector tiles and the weak tiny outside units, rather than replacing the mathematical drawing with a painting.
One coherent mat/blue/green/gold/red set. Positive and negative signs remain clear in grayscale. Motion off stops the idle lamp and decorative effects. Viewed both existing bar tools without rebundling or editing them; the studio keeps its tactile mathematical identity.
Raster art: 195.4 KB. Final bundle: 353.8 KB. Frames inspected in `review-cold/`, `review-play/`, `review-cards/`, `review-before/`, `review-after/`, `review-full/`, `review-walk/` and the scoped `review-last/`, `review-phone-final/` and `review-cancel/`.

#### Audit
**Audit not finished.** The single final attempt used a 2400-second limit, Chrome port 9951, host 8755 and the required review profile. It exited before its first size completed with `ConnectionResetError: [WinError 64]` in the CDP connection.
No `audit.md`, leads or audit PNGs were emitted. The failure receipt is `review-audit-attempt.txt`; only host copies exist in `review-audit/`. No second audit was run. Manual coverage includes all eight STANDARDS sizes, real hosted phone input, keyboard completion, grayscale, Motion off, both slider extremes, every card's algebra and main/side voice paths. Manual test consoles were clean; self-containment, required notes headings and the voice inventory passed. Automatic resize stress remains unverified.

#### Left open
- The full mechanical audit is unverified. Keep beta status; this report does not claim its gate passed.
- `kit/algebra-tiles.js` and its family document are absent. The isolated local implementation stays; no kit files were changed. The exact requested shared APIs remain recorded in handoff.md.
- The catalog still uses broad A-SSE.A / A-SSE.B cluster labels. BASELINE assigns exponential rewriting and geometric series elsewhere. No fourth mode was added and no catalog file was changed outside the authorized folders.
- Negative bands remain a formal signed-area model, and the small inset has its own printed scale. Changing those spec choices would need a separate design decision.
- No recorded narration, audible audition, physical touchscreen or screen-reader hardware test. Browser voice timing and keyboard behavior were exercised.
- Procedural note: the first brief/memory read commands lacked a hard process deadline. Subsequent commands used bounded runners. Two early keyboard harness failures were corrected to send Enter as drive.py does; no product change was needed for keyboard completion.
- Unattended choices followed the spec and BASELINE: retain three modes, keep the successful painting, use tool-local controls instead of changing the missing engine, and preserve the binary claim only as an unscored worked explanation. No git commits or shared-file edits.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Algebra Tile Studio handoff

Build only. No commit, publication or polish round. All implementation is in src.html. CSS follows the starter and Grade 9 kit theme. Code sections cover integer polynomial arithmetic, content, kit voice, state, signed-cell validation, square construction, responsive SVG rendering and input.

#### Important implementation details

Frame cells form an outer product. Edge signs are read from the first row and column; kinds depend on x and unit edge bands. The second x² can extend either axis. Checks require every tile in the frame and exact agreement of both the expanded factors and the signed tile inventory with the card. Shape alone is insufficient. Cards 9 and 10 use an integer factor-pair search. Mat cancellation checks exact expression invariance.

The last valid placement closes the frame automatically, lights the edges and reveals the factors. Check also runs the same exact test. No rectangle claim, arbitrary flipping, overlapping tiles, extra pile tiles and deleting terms cannot bypass the inventory comparison. No scores or work are saved.

The pile groups equal loose tiles into visible stacks. Drag or select a stack tile and tap a dashed cell. Keyboard arrows move a loose selected tile into the corner, then move by symbolic cells. F flips, T turns and Delete removes. The tray stays before the SVG tiles in keyboard order. Tile focus is restored with preventScroll after redraw. Mode state stays in memory only.

Mat finds an unoccupied spot for new tiles and side-by-side zero pairs. A full mat asks for Remove or Clear mat. Frame and Square tray additions wait until a card is selected. Square supports individual strip drags as well as Split strips. At short heights the SVG number-line dot is the primary x control; the duplicate panel slider is hidden so the x-length control stays in view.

Square adds every corner unit together with an outside negative unit. Outside unit pairs cancel exactly, leaving the remainder. Editing the square invalidates its result and requires Start over. Negative strips are formal signed-area cells, not literal negative physical lengths. The inset square uses an absolute side length. Its scale is printed because the −8 to 8 slider could otherwise require a very large inset.

#### Open questions and conflicts resolved

- Keep three modes. BASELINE specifically assigns A-SSE.B.3c to exponent-rule-builder and B.4 to savings-plan. The catalog/module was not edited, because writes are restricted to this tool.
- Use built-in image generation rather than the spec's local FLUX instruction, following the user's explicit art request and the build brief. One painted studio-mat asset, people false.
- Missing kit/algebra-tiles.js and docs/families/algebra-tiles.md: use isolated local helpers without touching kit. See engine request below.
- Negative algebraic edges cannot be represented as physical negative distances. Use signed-cell bands with positive display lengths, with an explicit explanation in notes. The minimum inset is a separate absolute-length square.
- The spec's full-width tray at short heights cannot fit all seven 44 px controls in the narrowest stage. The tray wraps inside the stage at those widths. Keep controls usable and document any frame-space limitation.
- Start-report-early conflicts with the user's instruction to stop when codex-report.md is written. Keep working evidence in Scratch and create the final report as the final build action.

#### Sensitivity

No people, cultural, health or body content. Review signed-area language to ensure negative edge values are never mistaken for physical negative lengths.

#### Engine changes wanted

- Missing file kit/algebra-tiles.js: provide Poly, TileMat and Frame with the spec's exact integer polynomial operations, signed-cell read rule, input and zero-pair behavior. No shared file was created or changed. Local helpers can be migrated after the engine exists.
- Missing file docs/families/algebra-tiles.md: document the same API and formal signed-area treatment for negative edge pieces.

#### Cold review repairs

- Dense diagrams now use a persistent full-size tile selector and 44 px movement buttons. Small SVG pieces are noninteractive pictures, rather than overlapping tiny targets. Mat and Frame retain drag and keyboard input when the drawing has room. Compact Square retains its specified guided Split and Fill path, plus selection and editing through the tile list.
- A No rectangle request displays all signed constant-factor pairs and their middle-coefficient sums. It never sets solved or plays a success chime. The specified claim remains available, as a worked explanation rather than an assessment.
- A closed frame now names the next action, and Mat's first added tile queues its editing instruction. Negative Square bands explain their signed meaning on screen. Tile bevels and outside-unit drawings were strengthened without changing the painted mat.
- New voice strings are inventoried in voice/lines.json. Review evidence is in _scratch/algebra-tile-studio/review-* and the final codex-review.md. The earlier build report is historical evidence, not a description of these repairs.
- Square editing now speaks its Start over instruction. Split, Fill and editing preserve Read priority, while ordinary narration that no longer fits gives way. The first Mat addition cuts an obsolete welcome so its editing instruction can start at the normal tap pace.

#### Next review

Review the open limits and evidence in codex-report.md, especially negative-strip Square geometry, compact tile hit targets, keyboard-only completion and voice timing. This is a local draft build, not a cold-review approval.

The build audit spans a pre-fix baseline and later control guards. The cold review runs a separate final audit after its repairs. The number-line dot has a transparent 44 px hit box over a tick label; the painted dot does not cover that number.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)

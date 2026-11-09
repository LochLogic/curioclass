# Codex report: algebra-tile-studio

## Built

Built Mat, Frame and Square, all ten Frame cards and six Square cards, in one offline HTML bundle. Tactile signed tiles sit on a generated studio mat. The last valid placement lights the factor frame automatically. Individual Square strips can be dragged, or Split strips builds both edges. Corner filling cancels outside unit pairs and exposes the remainder and minimum. No score or work is saved.

The specified algebra-tiles engine and family document are absent. Exact local helpers are isolated in src.html. No shared engine was edited. This is a beta build with the accessibility limits below, not a cold-review approval. No commit, publication, registration or polish round.

## Numbers check

Independent exact arithmetic: `_scratch/algebra-tile-studio/numbers.py` and `numbers.json`.

- Eight products expand to the specified integer coefficient triples. Zeros also checked, including −1/2 for cards 7 and 8.
- Cards 9 and 10 have no integer factor pairs with the required middle coefficient.
- Cards 5 and 6 need respectively two and three pairs of opposite x strips.
- Square corners: 9, 4, 16, 9, 1, 4. Remainders: −4, 3, 0, 1, −4, −4. Minimum locations: −3, −2, −4, 3, −1, 2.
- x² + 3x − 2 at x = 2.6 is exactly 12.56. All stated base-color contrast ratios agree with the spec's rounding.
- Contrast: sky blue on panel 9.048:1; on section 8.574:1; brand ink on sky blue 9.322:1. Tile ink on blue, green, yellow and red: 9.973, 11.735, 13.231 and 8.408:1.
- 60 browser assertions passed before the final presentation fixes. The final source passed 55 logic assertions, including full-mat bounds. Targeted browser checks covered the later changes.

## Facts checked

| Student-facing fact | Named source and verification |
|---|---|
| Terms, coefficients, constants, structure, factors and zeros | [CCSS A-SSE](https://www.thecorestandards.org/Math/Content/HSA/SSE/), checked live. Each expression and zero independently recomputed. |
| Rectangle edges multiply to the quadratic; signs multiply cell by cell | OpenStax Elementary Algebra 2e 7.3, named in the spec; integer expansion and signed-cell tests cover every card. |
| Half the middle coefficient determines the corner; the remainder is the minimum when the square vanishes | [OpenStax Intermediate Algebra 2e 9.2](https://openstax.org/books/intermediate-algebra-2e/pages/9-2-solve-quadratic-equations-by-completing-the-square), checked live, plus independent exact arithmetic for all six cards. |
| Opposite matching tiles add zero and preserve the expression | NCTM Illuminations Algebra Tiles, the spec's named source; its linked page returned HTTP 402, so live access was not verified. The identity and removal invariant were independently tested. |
| Variable x edges stretch together; a unit remains one unit | Algebraic definitions in the spec and independent geometric measurement. Frame units measured 57.924 px at both x-length extremes; Square units measured 49.353 px at both extremes in that viewport. |
| All numeric expression, value, factor, corner, remainder and minimum readouts | The exact calculations above, FRAME/SQUARE content, and functional-results.json. No unrelated factual content added. |

## Break it

- No score, saved best, progress meter or reflection gate exists. Tile count reports inventory only.
- Frame Check: tried empty frames, deletion, an extra pile tile, overlap, a wrong sign, a wrong tile kind and incomplete inventories. All refused. Full rectangles require exact factor expansion and exact signed inventory, with the entire pile used.
- Reversed factor order and a transposed leading-two rectangle pass. Simultaneously negating both factors remains an accepted equivalent arrangement.
- Cards 5 and 6 cannot obtain the necessary signed strip counts with too few zero pairs. Adding pairs preserves the exact expression. A jittered real drag canceled opposite Mat strips and left zero tiles and expression 0.
- No rectangle was tried on every card: refused on 1 through 8, accepted on 9 and 10. This is an unscored claim with factor-pair feedback; a lucky binary guess earns no persistent result.
- Square: Fill before Split does nothing; repeated Fill cannot inflate the corner; changing the inventory blocks construction. Editing a completed square removes its completed rewrite and requires Start over. This last misleading-state exploit was found and fixed.
- Sweeping x length cannot change a fit result. The number-line slider is an unscored exploration of the displayed square, so reaching its labelled minimum is intentional.
- Repeated Mat additions stop when no free spot remains. Inventory and expression stay exact. New zero pairs occupy free side-by-side positions, rather than hiding under earlier pairs.

## Voice walk

`voice-walk.json`: real held clicks, two-second tap pace, default Sound. Main spoken order: wMat, wFrame, frameAct, wSquare, squareAct, fillAct, square, probeAct. The path used Mat tiles, Frame card selection and Check, then Square selection, Split and Fill. No exceptions. Read followed by Start over and rebuilding spoke the Square event again while how-to lines remained once-only.

The audit found one lost Zero pair event in five taps. Fixed with short event speech, unique event keys and retention through Read. Targeted logs `zero-five.json` and `zero-after-read.json` each show five of five events spoken. Frame success and gap events also have unique occurrence keys: `closed-five.json` and `gap-five.json` each show five of five events at a two-second tap pace. Repeated empty Clear and active-mode taps now leave their current instruction playing; `clear-quick.json` and `mode-quick.json` show no cuts. The final hint names the number-line dot, which remains available in compact views.

Seventeen fixed lines use wise-mentor metadata, the kept Gacrux bank entry, and Curio.voice. No recording was made, as instructed. Tests used muted Chrome and verified the narration log, not an audible human audition. The final minor hint wording was inventoried after the main walk.

## Feel check

Best moment: the last unit tile closes the rectangle, lights its edges and turns the student's placement into factors and zeros. Verified with automatic-result.json and a complete keyboard-only first card.

Two flat moments and their build fixes: the early rectangle was small and stranded in a corner, so it was centered and given more of the working area; Square initially left canceling outside piles on screen, so the pairs now cancel and leave the actual remainder, including an empty outside area for a perfect square. Individual strip dragging and immediate placement feedback keep Square connected to the same physical tiles.

Viewed both bar tools. `bar-comparison.png` puts this tool beside Beat Lab. The tile bevels, shadows, hatching and generated material surface give the algebra objects weight. Its lower control density is appropriate to this one area model. This is a build feel check, not an owner approval or an assertion that the small-preview limitations are acceptable.

## Done when

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

## Wave lessons

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

## Audit leads

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

## Frames looked at

Looked at both bar frames; default and functional frames; all 12 full-run frames covering every STANDARDS size, negatives, leading two, perfect square, Motion off and grayscale; nine targeted frames; native drag, keyboard and voice frames; and every later fix frame. All 50 audit PNGs were inspected on seven contact sheets, with `audit-sheet-map.json` identifying each source frame. Final 375 px Mat, Frame and Square frames were inspected individually. Failed host/driver artifacts are preserved separately and are not counted as passes.

## Art made

One studio-mat painting, made with the built-in image tool, saved in art/raw/studio-mat.png and converted with art.py --rekey to art/studio-mat.webp. Full house style and prompt are in art/prompts.json; drawn_by is codex, people is false. First candidate retained after final-size inspection. No downloaded images or recorded audio.

Art: 200,120 bytes, 195.4 KB, above the initial 150 KB estimate. Voice assets: 0 KB. Final bundle: 357354 bytes, 349.0 KB, comfortably below the 2 MB goal. Tiles, signed hatching, frame, unit grid, number line and inset remain exact responsive vectors.

## Art still to paint

None. No people assets are needed or present.

## Engine changes wanted

Missing kit/algebra-tiles.js: provide the spec's Poly integer/fraction API, TileMat input/zero-pair API and Frame.read signed-cell contract. Missing docs/families/algebra-tiles.md: document those APIs and signed-area treatment. The local implementation can then migrate; no shared file was created or changed.

## Left open

- Dense compact Frame/Square targets miss 44 px; phone tile labels and the physical construction are small. This is the main unresolved build limitation.
- Negative edge bands are formal signed areas drawn with positive display widths. They are not literal negative physical distances. The inset is drawn at its own printed scale to keep it small, a deliberate qualification of the spec's unit-scale request.
- No recorded wise-mentor audio or audible audition, physical screen reader, touch hardware or school Chromebook test. All browser testing was muted.
- NCTM's linked page could not be fetched live. Initial interactive driver attempts timed out; smaller retries and later runs succeeded. An experimental phone route returned 404; subsequent proper hosted phone checks passed. Parent host favicon requests also produced 404 logs, outside the packaged tool.
- Procedural exception: I mistakenly rebundled the two reference bar tools, regenerating ignored reference HTML outside the allowed write folders. Their source files were not edited. I made no git operations and made no further edits in those folders.
- The earliest read commands lacked a hard process deadline. Later commands used bounded runners. LibreOffice's Python launcher also left host children; exact matching tool-host processes were identified and closed, and the runner was corrected to invoke the actual Python binary.
- Open question resolved: retain three modes and leave exponential rewriting and series to their assigned tools. The restricted module/catalog files remain untouched.

Final validation and process-cleanup evidence: `_scratch/algebra-tile-studio/final-manifest.json`. Build only stops with this report.

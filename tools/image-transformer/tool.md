# Image Transformer: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: image-transformer

#### Built
Three modes and all three Undo cards in one offline file. Supplied lighthouse, balloon and fox paintings remain untouched. Canvas moves the image, grid, unit square, arrows and probe together, with a 20 percent home ghost. Stable controls, real arrow dragging, fraction inputs, matrix-entry animation, failure equations and inverse recovery use the kit frame, theme, voice and sound. Final bundle: 214368 bytes. Source lines stay at or below 160 characters.

Built metadata remains tool.draft.json with stage built. No commits, branch changes, art generation, recording, publication or polish round. Repository writes stayed inside tools/image-transformer/. Scratch: S:/CurioClass-codex-scratch/image-transformer/.

#### Numbers check
PASS: numbers_and_first.py and numbers.txt independently recompute every numerical example using exact rational arithmetic: all presets, both order examples, commutation, four move determinants, three inverses and pixel origins, Blend determinant and inverse, all three color triples, Gray examples, probe, scalar determinant, areas and failed-row example. No numerical disagreement with the spec.

Turn 30 determinant is 0.999956, displayed as 1. Contrast: violet on panel 6.43:1, on secondary background 6.09:1, dark ink on violet 6.74:1. The spec's (270, 0, 0) Gray example is outside valid RGB input range; the UI uses its two valid triples to explain nonuniqueness. Move 3's pin is above the required fixed grid, at y = 11.

#### Feel check
Played Studio, product order, inverse moves, singular move, pixel recovery and color recovery. Best moment: a typed inverse brings the stretched picture exactly onto its ghost and retains the student's own U times M result. Wrong inverses play their actual product instead of merely saying wrong.

Two flattest moments were a failed answer that could have ended as text alone, and dense Undo controls hiding the next action. The build shows the failed product on the picture, reports its exact failed row, and moves worked results into a stage-side work strip. Compact color actions share a row. The phone header was rebuilt after the first run exposed hidden mode buttons. Arrow dragging resolves the nearest tip when their 44-pixel targets overlap.

Frames compared side by side in Scratch/feel-comparison.png: full-frames/undo-home.png with bar-frames/beat-lab.png, both at 1366x768. Both bar tools were bundled into Scratch and opened before implementation. The tool uses painted image content, directional gradients, inset highlights, shaded controls, viewport screws and a quiet lamp. Studio and Undo are visually stronger than the initial diagram, but small stacked Order previews remain plainer and less satisfying than the bar. That limitation is not a claimed visual pass.

#### Done when
1. PASS: functional checks verify Shear matrix and area 12, Stretch area 24, Reflect orientation.
2. PASS: jittered real drag at 1366 sets column 1 to (2, 1); keyboard probe verifies (1, 1) maps to (3, 2). A compact real drag also verifies nearest-tip selection.
3. PASS: Flatten line, zero-matrix point and 3I determinant 9 checked in browser.
4. PASS: initial BA and AB match; two rounded turn matrices compare as Same picture.
5. PASS: Move 1 and Move 3 accept the stated inverses, end at identity after the animation, and Move 4 rejects Apply but accepts the singular answer.
6. PASS: both stated pixel origins and first Blend RGB triple pass. Failed origin (3, 1) reports row 1 gives 7, not 5. Two misses reveal Show me.
7. PASS: stretch/turn products and Identity commutation match. Swap and the optional sum stage are checked.
8. PASS: inspected 1366x768 and 1000x625 in all modes; the live scene and paired Order scenes occupy the largest region.
9. PASS: browser checks interrupt Animate with a preset and a box edit, then wait past its old end; no jump back. Audit includes interruption and resize stress.
10. FAIL: held clicks at 2 seconds start flipped twice and flat twice; Read cuts the last flat line deliberately. Five repeated card visits start each how line at most once. Mode changes deliberately cut speech. Full audit voice findings are addressed below; this is not a claim that every clip was heard to completion.
11. FAIL: controls fit 1366x768, Order stages stack at 760, and canvas draws at actual device pixels at 1920. Phone Order Swap and some secondary controls extend below 812 pixels. Short stacked stages make the actual image very small. See Left open.
12. PASS: the bundle embeds supplied art and kit code; no external resources or networking APIs. Three paintings contain no people. No em dashes in authored files.

#### Wave lessons
- Hint and voice: PASS for immediate state-owned hints, current-hint Read, V.heard how-to selection and valid welcomes. Singular pixel hints name the available explanation button. Voice caveats are recorded above.
- Focus and layout: FAIL as a whole. Stable inputs, no focus on load, preventScroll arrow focus and reserved hint space pass, but arrow labels crowd in short stacked previews.
- Sizes: FAIL; 44-pixel controls are used, but small-layout and below-fold leads remain.
- No giveaways: PASS; inverse, origin and RGB answers start unsolved, formulas require an explicit control, and Show me requires two misses. No answer meter or slider solves the Undo cards.
- Honest numbers: PASS; area states 12 original square units, RGB identifies its controlled sample tile, and rounded determinant behavior is documented.
- Standards: PASS; students manipulate columns, scalar multiples, sums, ordered products, inverses and a three-channel system. No family engine applies.
- Motion off: PASS in targeted zero/Animate check; lamp uses animation none when calm. Timing is not accelerated.
- Short choice sets: FAIL; all primary desktop choices fit, but phone Order and some compact picture choices need scrolling.
- Resize mid-animation: FAIL for complete verification. Cancellation and interrupted edits passed targeted checks, but the audit did not export its full stress results before timeout.
- Late welcome: PASS by kit queue and valid state checks; no welcomeAfter.
- Unknown stays unknown: PASS; Undo entries begin as guesses, never prefilled with an inverse. The color ring is explicitly a controlled known filtered sample.
- One look, one meaning: PASS; column 1 is solid blue, column 2 dashed violet, home is faint, current image is opaque, probe is a ring. Grayscale frame inspected.
- Badges say what is true: PASS; orientation derives from determinant and comparison from the actual matrix products.
- Hints change back: PASS; mode/card changes and reset update them immediately.
- No answer by copying: PASS; failed rows show the student's calculation; the solution is available only via an intentional formula or Show me path.

#### Audit leads
Audit not finished. The single final audit ran on port 9991 with host 8795 and stopped at its 1770-second limit. No audit.md was exported. The process log is Scratch/audit-process.log, with the timeout record in audit-timeout.txt. No second full audit was run.

All 99 captured audit frames were inspected. Manual leads and disposition:
- Fixed: phone mode buttons hidden by flex shrink; rebuilt header into three explicit rows.
- Fixed: compact Undo controls overlapping; stable controls and a separate result/formula strip.
- Fixed: phone color results and inverse consuming the canvas; reserve color-stage height and omit repeated explanatory footer paragraphs at phone width. Final affected frames retain 97 and 99 pixels of canvas, with Check inside the viewport.
- Fixed: Letter F bypassing the color filter; it now uses the same matrix kernel. Sampled Blend RGB (78, 106, 92) and Gray RGB (92, 92, 92) match independent expectations.
- Fixed: changing back to Studio after a filter formula must restore its 295-pixel phone stage; targeted regression passed.
- Left open: small stacked Order stages, tight arrow labels, phone Order Swap partly below the fold, and some secondary picture choices requiring scrolling. Resolving these needs another layout decision; no polish round was started.
- Left open: full audit control-walk, repeated-event and resize-stress findings were not exported. No clean mechanical-audit claim is made.

After the timeout, only five frames affected by the two final build fixes were checked. All five passed with zero console errors. Audit Chrome was closed explicitly; the final drive closed its own Chrome and host.

#### Frames looked at
Both bar-tool frames; all five first frames; all four check frames; functional-pass; all 34 full-run frames via contact-0 through contact-8; all seven successful targeted frames; all three last frames. All 99 audit frames via audit-look-00 through audit-look-24 are mapped in audit-contact-manifest.json. All five post-audit frames were also opened and inspected.

One full all-size run was performed, then only affected layouts and interaction fixes were re-shot. A bad test-script encoding was fixed before the 33-check functional run passed. One nested-quote selector failure was fixed and re-shot. The final targeted batch has zero errors; earlier host-only favicon 404s disappeared after fixing the generated host timing. These were harness issues, not ignored tool exceptions.

#### Engine changes wanted
None.

#### Left open
- The fixed -6 to 6 grid clips the Move 3 pixel at (5, 11). Its equation stays visible; no off-spec zoom was added.
- Phone Order and some compact optional controls still need scrolling. Stacked short Order stages have small pictures and crowded arrow labels. This is a build limitation and a visual FAIL for those previews.
- No recorded voice clips were generated, as instructed. The casual-peer bank entry is specified; narration currently falls back to browser speech.
- The gray example with channel 270 is excluded from the UI, as documented above.
- Full mechanical control-walk and resize verification remain open because the audit hit its limit. All started Chrome trees and servers are closed; ports 9990, 9991 and 8795 are closed, and host.html is removed.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: image-transformer

#### Played

Cold Grade 12 solo run before builder files: Studio, all pictures, shear/flatten, Order/Swap/sum, all three Undo cards, wrong and correct paths. A six-second card walk checked projection pacing. Best: the inverse returns the picture exactly to its ghost; preserved.

#### Findings fixed

- blocker, general, compact Undo: bracketed 2x2 entries became one 1x4 row; retained the two mathematical rows at every size.
- should fix, general, compact layouts: short choice sets and Swap fell below the fold. Existing hints/Move controls relocate at short sizes; compact matrices, full-height sliders and phone header keep controls visible.
- should fix, general, narration: the zero matrix spoke about a line; added the accurate point event and matching voice manifest.
- should fix, general, event queue: repeated singular successes replaced queued events. Unique event keys preserve all five results at a two-second tap pace; the final queue drains completely.
- should fix, general, audit-confirmed: tapping the already active mode cut its welcome. Active-mode taps now preserve work and speech; no-change Identity/Scale/Reset provide the fitting skipped welcome.
- should fix, general, audit-confirmed: static Order/Undo canvases were dead keyboard stops. They now leave the tab order and carry descriptive labels; Studio remains interactive.
- should fix, general, audit overlay confirmation: compact hint/readout wrapping moved the grid during a drag. Studio reserves those heights; numeric fields now fit signed three-decimal entries. Both native arrow drags were rechecked at 680 and 375 wide.
- should fix, general, color card: correct answers left the painting filtered. The inverse now restores the picture and sample, with recovered RGB and an accurate Next pixel hint.
- should fix, general, Gray: its explanation used a different sample from the active equation. Permuting the current RGB supplies two valid originals; a wrong average now reports the actual failed row.
- should fix, general, pixel origin: wrong guesses only changed text. Their destination now gets an X and dashed discrepancy line to the target; success wording states the 0.01 tolerance honestly.
- polish, general, craft: suppress empty work strips, keep finite effects still with Motion off, and avoid off-edge/crowded arrow labels.
- polish, general, art: redrew the flat balloon as a detailed red/yellow balloon over layered fields, matching the existing photo-like paintings. Darkroom lighting, screws, lamp, live grids and strong lighthouse/fox art remain.

#### Findings left

- should fix, general, spec conflict: Move 3 pin (5, 11) is outside the required fixed -6 to 6 axes. Equation remains visible; adding zoom or a locator would change the spec.
- polish, general: full fixed grids stacked in the shortest previews leave small actual pictures, especially with formula/help open. Controls and mathematics remain usable; the specified range/stacking constrain the image footprint.

#### Flattest moment left

The optional third sum picture in a short stacked preview. The full-screen comparison and recovery are stronger. The former text-only RGB recovery now visibly restores the student's picture.

#### Graphics

All three paintings inspected as finished WebP and in the tool; no people or lettering. One redraw, no missing art. Full prompt and built-in generation provenance: art/prompts.json. Balloon outputs: art/raw/imt-balloon.png and art/imt-balloon.webp.
Bundle: 298996 bytes (292.0 KiB). Three final paintings: 148.4 KiB; balloon: 78.0 KiB. Beat Lab and Snowy Mail Route frames compared; the darkroom keeps its instrument character, while small fixed-grid pictures remain less expressive.
All 107 initial audit frames were inspected through review-audit-look/ (manifest names every frame). Targeted functional and visual frames were opened separately.

#### Audit

The single audit finished in 1855.1 seconds (30.9 minutes), Chrome 9961 / host 8765. No runtime errors, infinite calm motion, resize exceptions or stuck controls. No second audit.
All 64 leads answered: 50 intentional canvas/44-pixel arrow overlays; 3 no-change skipped welcomes repaired; 6 changing-preset welcomes correctly stale after their matrix boxes change; 2 static canvas tab stops repaired; 3 active-mode speech cuts repaired.
Overlay confirmation exposed and fixed the compact drag layout shift. Whole-pixel compact drags reach the intended column within 0.1; the 1366 drag reaches (2, 1) exactly. Zero-matrix keyboard checks reach both targets. Only affected frames/paths were re-shot after audit; the full audit was not rerun on those narrow repairs.
Before audit: exact Fraction checks of every worked example; contrast 6.43:1 / 6.09:1 / 6.74:1; 37 browser functional checks; jittered native drag; keyboard-only arrows; Motion off; grayscale; all eight sizes in four states. Targeted rechecks have no runtime errors or warnings.
Wave lessons checked: immediate state-owned hints/Read, stable focus, 44-pixel controls and visible short choice sets, no answer giveaways, honest numbers, hands-on standards, calm loops, resize safety, stale welcomes and returning hints. No family engine applies.

| Line | Kind | Expected | Spoken |
|---|---|---:|---:|
| undo / pixel / color | how | 1 each | 1 each |
| flipped / flat / home / noUndo | event | 5 each | 5 each |
| point | event | 1 | 1 |

Read/Sound and fast mode changes drop stale queues. Two-second event tests and six-second card visits use held 120 ms clicks; no line invents a hidden control.
Post-audit: all three active-mode double taps preserve their single complete welcome; fresh Identity, Scale by 1 and Reset each start the Studio welcome. Changing Shear correctly skips the stale introduction.

#### Left open

- Browser speech fallback remains; no recordings were made under the review/build rule.
- The spec's out-of-range Gray example (270, 0, 0) stays excluded; active channel permutations are within 0 to 255.
- The existing open question about another 3x3 system is a spec decision. No new activity, topic or shared-kit change was added.
- No git commits, branch changes or publication. Authored files and Scratch stay in the two authorized directories. All started Chrome/server processes are closed; host.html is removed.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Image Transformer handoff after cold review

#### Structure
src.html uses the shared kit and 9-12 theme. CSS, stable controls, arithmetic, canvas drawing, task checks and narration follow in order.
`__tool` exposes state, arithmetic, matrix editing, geometry, redraw and voice logs for verification.

#### Tricky parts
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

#### Engine changes wanted
None. All repairs are local to this tool.

#### Spec constraints / Left open
- The required fixed -6 to 6 grid clips Move 3's pixel at (5, 11). Its equation remains visible. A zoom or off-grid locator would change the spec.
- Two or three full fixed grids stacked in short previews leave little space for each actual 4 by 3 picture. Controls now fit; the small mathematical image footprint remains.
- The spec's (270, 0, 0) Gray example is outside RGB range and is excluded from the UI.
- No recorded clips exist. Browser narration is retained because this pass prohibits recording.
- The spec's open question about additional 3 by 3 systems remains a curriculum decision; no extra topic was added.

#### Validation
The cold reviewer played all modes and Undo cards before reading builder files. Exact rational recomputation verifies the spec's examples.
One full all-size run covers Studio, Order, Undo and Color at eight sizes; changed states receive targeted rechecks only.
Functional checks cover all inverse moves, singular rejection, origins, all three color triples, actual recovered canvas samples,
fraction and invalid inputs, determinant/area, commutation, scalar multiplication and animation cancellation.
Held-click narration, real jittered dragging, keyboard arrows, Motion off and grayscale are checked in Scratch.
The final audit status and any confirmed leads are in codex-review.md. No commits, publication or shared-kit edits.

#### Cold audit closure
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

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: handoff.md folded in (last changed 2026-11-04)

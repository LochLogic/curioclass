# Codex report: image-transformer

## Built
Three modes and all three Undo cards in one offline file. Supplied lighthouse, balloon and fox paintings remain untouched. Canvas moves the image, grid, unit square, arrows and probe together, with a 20 percent home ghost. Stable controls, real arrow dragging, fraction inputs, matrix-entry animation, failure equations and inverse recovery use the kit frame, theme, voice and sound. Final bundle: 214368 bytes. Source lines stay at or below 160 characters.

Built metadata remains tool.draft.json with stage built. No commits, branch changes, art generation, recording, publication or polish round. Repository writes stayed inside tools/image-transformer/. Scratch: S:/CurioClass-codex-scratch/image-transformer/.

## Numbers check
PASS: numbers_and_first.py and numbers.txt independently recompute every numerical example using exact rational arithmetic: all presets, both order examples, commutation, four move determinants, three inverses and pixel origins, Blend determinant and inverse, all three color triples, Gray examples, probe, scalar determinant, areas and failed-row example. No numerical disagreement with the spec.

Turn 30 determinant is 0.999956, displayed as 1. Contrast: violet on panel 6.43:1, on secondary background 6.09:1, dark ink on violet 6.74:1. The spec's (270, 0, 0) Gray example is outside valid RGB input range; the UI uses its two valid triples to explain nonuniqueness. Move 3's pin is above the required fixed grid, at y = 11.

## Feel check
Played Studio, product order, inverse moves, singular move, pixel recovery and color recovery. Best moment: a typed inverse brings the stretched picture exactly onto its ghost and retains the student's own U times M result. Wrong inverses play their actual product instead of merely saying wrong.

Two flattest moments were a failed answer that could have ended as text alone, and dense Undo controls hiding the next action. The build shows the failed product on the picture, reports its exact failed row, and moves worked results into a stage-side work strip. Compact color actions share a row. The phone header was rebuilt after the first run exposed hidden mode buttons. Arrow dragging resolves the nearest tip when their 44-pixel targets overlap.

Frames compared side by side in Scratch/feel-comparison.png: full-frames/undo-home.png with bar-frames/beat-lab.png, both at 1366x768. Both bar tools were bundled into Scratch and opened before implementation. The tool uses painted image content, directional gradients, inset highlights, shaded controls, viewport screws and a quiet lamp. Studio and Undo are visually stronger than the initial diagram, but small stacked Order previews remain plainer and less satisfying than the bar. That limitation is not a claimed visual pass.

## Done when
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

## Wave lessons
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

## Audit leads
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

## Frames looked at
Both bar-tool frames; all five first frames; all four check frames; functional-pass; all 34 full-run frames via contact-0 through contact-8; all seven successful targeted frames; all three last frames. All 99 audit frames via audit-look-00 through audit-look-24 are mapped in audit-contact-manifest.json. All five post-audit frames were also opened and inspected.

One full all-size run was performed, then only affected layouts and interaction fixes were re-shot. A bad test-script encoding was fixed before the 33-check functional run passed. One nested-quote selector failure was fixed and re-shot. The final targeted batch has zero errors; earlier host-only favicon 404s disappeared after fixing the generated host timing. These were harness issues, not ignored tool exceptions.

## Engine changes wanted
None.

## Left open
- The fixed -6 to 6 grid clips the Move 3 pixel at (5, 11). Its equation stays visible; no off-spec zoom was added.
- Phone Order and some compact optional controls still need scrolling. Stacked short Order stages have small pictures and crowded arrow labels. This is a build limitation and a visual FAIL for those previews.
- No recorded voice clips were generated, as instructed. The casual-peer bank entry is specified; narration currently falls back to browser speech.
- The gray example with channel 270 is excluded from the UI, as documented above.
- Full mechanical control-walk and resize verification remain open because the audit hit its limit. All started Chrome trees and servers are closed; ports 9990, 9991 and 8795 are closed, and host.html is removed.

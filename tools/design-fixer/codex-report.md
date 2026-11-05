# Codex report: design-fixer

## Built

- Studio and ten freely accessible Fix briefs, with editable vector posters, five live meters, Squint, eye-path badges, guides, layers, keyboard editing and an earned before-and-after wipe.
- Generated and integrated the painted designer's desk during this build. Final offline bundle: **266,281 bytes, 260.04 KiB**, below 2 MB.
- No commits, branch changes, deployment, shared-source edits or polish round. Project writes stayed inside tools/design-fixer/ and _scratch/design-fixer/.
- The early working report stayed in Scratch because the user's instruction requires stopping when this report is written.

## Numbers check

- Independent Python: every broken start is unsolved; all ten reference repairs meet every goal using their own palettes. Every reference element stays inside the page, and Biscuit's locked fields remain unchanged.
- Browser/Python reference results agree: Bake Sale tilt 0, Biscuit +0.0590816, Car Wash 0. The real single-cupcake repair ends at -0.00761296, within the 0.08 balance limit.
- With other Bake Sale parts centered, real left/right cupcake drags give -0.15319896 and +0.19444480, reversing the seesaw.
- Look ratios: white/brand 7.9031, brand/paper 7.2353, ink/paper 15.3671, paper/mat 9.9241, muted/paper 6.0500, stamp/paper 4.7409. Guides: 4.5966 on white, 4.5686 on black.
- Additional UI ratios: header 14.3259, hint 11.5765, stamp on its opaque label 5.0819, goal check 5.1567.
- Three browser/Python poster pairs agree: pale yellow/white 1.129829, navy/black 1.429077, indigo/white 7.903111.
- Model cap thresholds: 42.42 normal, 33.936 bold; minimum 16.968 and maximum 282.8 per line. Source discrepancy: 18.7 divided by 24 is 0.779167, not exactly 0.8. Used the stated 3 percent and 2.4 percent thresholds.
- The source's illustrative Bake/Cat/Robotics examples omit full coordinates and colors, so their exact sample outputs cannot be uniquely reproduced. Shipped layouts have separate reproducible checks in Scratch.
- Bigger uses 1.05 and Smaller uses 0.95. A held Smaller click changed the title from 630 by 270 to 598.5 by 256.5, exactly 5 percent smaller.

## Feel check

- Best moment: dragging the cupcake levels the seesaw, earns a restrained Fixed stamp, and opens a wipe showing this student's actual repair.
- Flat moment 1: the first crowded editor pushed the hint below the laptop fold. Combined the guide/type/layer row and compacted short previews; final compact hints fit, including the longest final brief.
- Flat moment 2: overlapping text could look broken yet pass contrast. Added cached foreground glyph masks and prior text to background sampling. A same-color overlap now reports 1:1 and fails.
- Also repaired the initially hidden Squint copy, moved the stamp clear of Science Night's footer, and prevented active mode taps from resetting edits.
- Later briefs add locked asymmetry, light-on-dark contrast, competing focal points, repeated gaps/sizes, type/color/alignment consistency and a final mixed brief.
- Compared both reference tools and made the side-by-side frame below. The painted materials, paper shadows and large editable poster carry the finish; poster parts intentionally stay flat and measurable.

![Design Fixer beside Beat Lab](S:/CurioClass-codex/_scratch/design-fixer/feel-comparison.png)

## Done when

1. **PASS:** independent Python and browser reference checks cover all ten starts/fixes; real pointer input repaired all ten briefs.
2. **PASS:** Squint 7 shows Title, Cupcake and Price as badges 1, 2 and 3. Editing works while blurred.
3. **PASS:** real cupcake drags reverse the seesaw in a centered layout; weighted-center calculations and displayed tilt agree.
4. **PASS:** the three WCAG pairs above independently match Python.
5. **PASS:** every repaired poster opened its stored-start comparison. ArrowRight moved 50 to 52, Home/End reached 0/100, and a real pointer drag reached 76 with a matching 24 percent right inset. The handle remains 44 pixels wide and clickable at both ends.
6. **PASS:** pointer/keyboard attempts leave the cat unchanged and produce the locked explanation. Its editing controls stay disabled.
7. **PASS:** inspected 1366x768, 1280x720 and 680x425. The poster is the largest scene object, centered on the empty mat rather than the ruler or desk edge.
8. **PASS:** jittered real drags update the model through one-frame rendering. A tap during Squint registered in about 2.76 ms. The model averaged about 0.18 ms per overlap calculation; this is not a full frame-rate measurement.
9. **PASS for the stated poster/Squint and laptop requirements:** meters and selected tools fit at 1366 and 1280. The poster and Squint stay visible at every required size. Compact preview editors and the specified phone panel require scrolling, as discussed below.
10. **PASS:** five selections at two-second intervals spoke selectHow once. Five subsequent goal re-ticks each produced a new spoken result. Audit repeat checks were clean. Rapid mode/reset cuts were fixed and rechecked.
11. **PASS:** Clear progress removes design-fixer-solved and does not immediately re-save a still-met layout. It closes comparison safely; Hint then names Start over instead of a hidden Before and after button. Reload persistence also passed.

## Wave lessons

- **PASS, hint/voice:** next control/action named, hint updated synchronously, Read uses it, heard-based how lines and valid event lines. Clearing hushes stale narration.
- **PASS, focus/layout:** stable editing nodes, no focus on load, preventScroll for deliberate focus, reserved hint area, root SVG excluded from Tab. Wipe and clear focus checked.
- **FAIL, complete size/target floor:** standard editor/header controls meet 44 pixels, including 44.09-pixel swatches at 1920. Small measured poster parts remain below 44. Phone/preview scrolling is documented below.
- **PASS, no giveaways:** live meters are the explicit teaching model. No auto-fix, hidden-answer matching or single slider sweep solves the briefs.
- **PASS, honest numbers:** model notice accompanies the meters; bounding-box weight and finite contrast sampling are explained in notes and handoff.
- **PASS, standards:** solo choices, organization, revision and interpretation of client intent cover VA:Cr1, VA:Cr2, VA:Cr3 and VA:Re8. No family engine applies.
- **PASS, Motion off:** no infinite animations; Squint jumps directly to 7 while editing remains available.
- **PASS, short choices:** ten swatches stay together in one row or a five-by-two set. Posters use a native menu; the compact editor can be scrolled into view as one group.
- **PASS, resize mid-action:** audit reported no exceptions or controls left disabled when resizing after inputs.
- **PASS, late welcome:** scoped Curio.voice, no welcomeAfter, no welcome delayed behind the first action's own line.
- **PASS, unknowns:** no hidden-state scene applies; visible meter values are computed from the visible layout.
- **PASS, one look/meaning:** numbered eye path, magenta guides/selection and worded goal ticks have separate roles.
- **PASS, badge truth:** Fixed records an earned attempt; later un-ticks remain visible. Menu checks identify previously earned completions.
- **PASS, hint reversibility:** mode/poster/sharp/blurred/selected/deselected and cleared states immediately name the current action.
- **PASS, no copying answers:** client notes describe communication problems; repairs require position, scale, type and color choices.

## Audit leads

- Full audit ran once, completed in about **29 minutes**, and produced **356 raw leads**. Raw report: `_scratch/design-fixer/audit/audit.md`. No runtime exceptions, stuck controls or infinite animations; five-click narration repeat checks were clean.
- **Fixed:** narrow Read targets at 680, 760 and 375. Minimum width is now 44; hosted phone and compact follow-ups confirm it.
- **Fixed:** hints below the 1000x625 fold and the final brief's 680 hint. Short-layout ordering/spacing now puts the final hint bottom at 420.38 in a 425-pixel viewport and 413.66 at 1000x625.
- **Fixed:** quick active Studio/Fix taps cut welcomes and reset work. Active mode taps now preserve work. Reset on a pristine poster is a no-op. Two held taps 0.7 seconds apart produced no cut in all three follow-ups.
- **Fixed:** Sound changed header positions. Its label now reserves width; measured largest shift is 0.
- **Audit setup corrected:** fixed-wipe used a returning expression where Audit.steps requires a function body with return, so that audit state never opened comparison. Corrected audit-states.json. Real drag plus held Before clicks subsequently reached the wipe at 680, 800 and 1000; separate laptop and phone comparison checks also passed.
- **Not a visual failure:** title text reported hidden under rect is under a transparent selection hit rectangle. Inspected lettering remains visible.
- **Expected first-tap behavior:** element/Squint actions speak their own how-to and skip welcome as required. Fix's actual welcome was spoken but logged as kind how, so the audit's welcome-kind check misses it. No late welcome was added.
- **Kept per explicit phone layout:** the 375-pixel stage and Squint come first, with meters/tools below. The repeated phone below-fold and hint-out-of-view leads describe that stack. This cannot simultaneously satisfy the general no-scroll-controls rule.
- **Left open:** small target leads for actual poster parts across sizes, especially tiny text and extreme shrink. Precise geometric selection and keyboard access remain; enlarging their hit rectangles would create overlapping targets in compact posters.
- Full audit was not repeated after local fixes. Only affected layouts, welcome taps, clear states, stamp placement and controls were rechecked; final drives had no console errors or warnings.

## Frames looked at

- Both bar tools bundled in Scratch and inspected at 1366x768; side-by-side comparison above.
- All standard sizes: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and hosted 375x812.
- Every real repaired poster, first/final wipes, locked cat, Squint, Motion off, grayscale, minimum/maximum resize, overlap regression, keyboard and voice/input frames.
- All 72 audit frames reviewed in contact sheets, plus full-size critical frames. The original audit wipe frames did not reach comparison; corrected comparison frames were inspected separately.
- Final follow-ups include compact hints, real pointer wipe, wipe endpoints, phone header/stamp/wipe, quick taps, sound geometry, cleared states, 1920 targets and exact five-percent shrink.

## Art made

- **1 image**, generated with the built-in imagegen tool. Full house style/prompt is in art/prompts.json; raw PNG is art/raw/df-desk.png.
- Finished art/df-desk.webp: **1500x938, 133,262 bytes, 130.14 KiB**. Processed only with free art.py --rekey df-desk and inspected at final size. No redraw needed.
- Empty usable center recorded as approximately x 18-84 percent and y 2-97 percent. Art placement checked across sizes. Bundle: **260.04 KiB**.

## Art still to paint

None. No generated people and no placeholder art. No audio was recorded, as instructed.

## Engine changes wanted

None. The audit drag-format documentation distinction is recorded in handoff.md; no shared file was edited.

## Left open

- The general 44-pixel target floor is not met by small editable poster parts. Keyboard selection works, but compact touch selection needs cold review.
- The specified stacked phone layout requires scrolling to editing controls. Short preview editors also scroll; the poster, Squint, meters and hint retain their intended compact layout.
- Contrast uses finite glyph/shape samples and can miss very small overlaps. It is documented as a teaching model.
- The manifest specifies big-sister/Leda, but narration uses the browser voice until recordings are supplied.
- Cold review is next. No polish round or commit was started. host.html was removed, servers stopped, and no owned Chrome processes remained at cleanup.

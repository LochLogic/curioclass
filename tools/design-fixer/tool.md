# Design Fixer: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: design-fixer

#### Built

- Studio and ten freely accessible Fix briefs, with editable vector posters, five live meters, Squint, eye-path badges, guides, layers, keyboard editing and an earned before-and-after wipe.
- Generated and integrated the painted designer's desk during this build. Final offline bundle: **266,281 bytes, 260.04 KiB**, below 2 MB.
- No commits, branch changes, deployment, shared-source edits or polish round. Project writes stayed inside tools/design-fixer/ and _scratch/design-fixer/.
- The early working report stayed in Scratch because the user's instruction requires stopping when this report is written.

#### Numbers check

- Independent Python: every broken start is unsolved; all ten reference repairs meet every goal using their own palettes. Every reference element stays inside the page, and Biscuit's locked fields remain unchanged.
- Browser/Python reference results agree: Bake Sale tilt 0, Biscuit +0.0590816, Car Wash 0. The real single-cupcake repair ends at -0.00761296, within the 0.08 balance limit.
- With other Bake Sale parts centered, real left/right cupcake drags give -0.15319896 and +0.19444480, reversing the seesaw.
- Look ratios: white/brand 7.9031, brand/paper 7.2353, ink/paper 15.3671, paper/mat 9.9241, muted/paper 6.0500, stamp/paper 4.7409. Guides: 4.5966 on white, 4.5686 on black.
- Additional UI ratios: header 14.3259, hint 11.5765, stamp on its opaque label 5.0819, goal check 5.1567.
- Three browser/Python poster pairs agree: pale yellow/white 1.129829, navy/black 1.429077, indigo/white 7.903111.
- Model cap thresholds: 42.42 normal, 33.936 bold; minimum 16.968 and maximum 282.8 per line. Source discrepancy: 18.7 divided by 24 is 0.779167, not exactly 0.8. Used the stated 3 percent and 2.4 percent thresholds.
- The source's illustrative Bake/Cat/Robotics examples omit full coordinates and colors, so their exact sample outputs cannot be uniquely reproduced. Shipped layouts have separate reproducible checks in Scratch.
- Bigger uses 1.05 and Smaller uses 0.95. A held Smaller click changed the title from 630 by 270 to 598.5 by 256.5, exactly 5 percent smaller.

#### Feel check

- Best moment: dragging the cupcake levels the seesaw, earns a restrained Fixed stamp, and opens a wipe showing this student's actual repair.
- Flat moment 1: the first crowded editor pushed the hint below the laptop fold. Combined the guide/type/layer row and compacted short previews; final compact hints fit, including the longest final brief.
- Flat moment 2: overlapping text could look broken yet pass contrast. Added cached foreground glyph masks and prior text to background sampling. A same-color overlap now reports 1:1 and fails.
- Also repaired the initially hidden Squint copy, moved the stamp clear of Science Night's footer, and prevented active mode taps from resetting edits.
- Later briefs add locked asymmetry, light-on-dark contrast, competing focal points, repeated gaps/sizes, type/color/alignment consistency and a final mixed brief.
- Compared both reference tools and made the side-by-side frame below. The painted materials, paper shadows and large editable poster carry the finish; poster parts intentionally stay flat and measurable.

![Design Fixer beside Beat Lab](S:/CurioClass-codex/_scratch/design-fixer/feel-comparison.png)

#### Done when

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

#### Wave lessons

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

#### Audit leads

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

#### Frames looked at

- Both bar tools bundled in Scratch and inspected at 1366x768; side-by-side comparison above.
- All standard sizes: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and hosted 375x812.
- Every real repaired poster, first/final wipes, locked cat, Squint, Motion off, grayscale, minimum/maximum resize, overlap regression, keyboard and voice/input frames.
- All 72 audit frames reviewed in contact sheets, plus full-size critical frames. The original audit wipe frames did not reach comparison; corrected comparison frames were inspected separately.
- Final follow-ups include compact hints, real pointer wipe, wipe endpoints, phone header/stamp/wipe, quick taps, sound geometry, cleared states, 1920 targets and exact five-percent shrink.

#### Art made

- **1 image**, generated with the built-in imagegen tool. Full house style/prompt is in art/prompts.json; raw PNG is art/raw/df-desk.png.
- Finished art/df-desk.webp: **1500x938, 133,262 bytes, 130.14 KiB**. Processed only with free art.py --rekey df-desk and inspected at final size. No redraw needed.
- Empty usable center recorded as approximately x 18-84 percent and y 2-97 percent. Art placement checked across sizes. Bundle: **260.04 KiB**.

#### Art still to paint

None. No generated people and no placeholder art. No audio was recorded, as instructed.

#### Engine changes wanted

None. The audit drag-format documentation distinction is recorded in handoff.md; no shared file was edited.

#### Left open

- The general 44-pixel target floor is not met by small editable poster parts. Keyboard selection works, but compact touch selection needs cold review.
- The specified stacked phone layout requires scrolling to editing controls. Short preview editors also scroll; the poster, Squint, meters and hint retain their intended compact layout.
- Contrast uses finite glyph/shape samples and can miss very small overlaps. It is documented as a teaching model.
- The manifest specifies big-sister/Leda, but narration uses the browser voice until recordings are supplied.
- Cold review is next. No polish round or commit was started. host.html was removed, servers stopped, and no owned Chrome processes remained at cleanup.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: design-fixer

#### Played

Cold Grade 7 exploration of Studio and all ten Fix briefs before reading the builder's files. Repaired Bake Sale with real dragging and keyboard input, used the earned wipe, and checked projector/preview use. Squint and the live seesaw are strong.

#### Findings fixed

- **Blocker, general, Contrast:** covered text could still earn All text readable and Fixed. Replaced unreliable detached-SVG shape queries with cached Canvas Path2D masks; sample preceding backgrounds and later occlusion. Covered text now fails and gets a move/Bring forward explanation. Confirmed in `review-followup/review-covered-text.png`.
- **Should fix, general, Studio:** Biscuit stayed locked without a client brief. Locks now apply only in Fix. Studio Bigger changed its width from 460 to 483; Fix pointer/key attempts kept it unchanged.
- **Should fix, general, selection:** small text had small targets. Added 44-pixel hit regions, actual-content priority where they overlap, and a part menu for unambiguous small/covered-part selection. Keyboard selected the Robotics date. Pale swatch boundaries now contrast 4.82:1 against the panel.
- **Should fix, general, typography:** forced stretching flattened letters and box height overstated cap height. Fit natural letter shapes, match the glyph masks, and use fitted cap height for readability thresholds. Rechecked size extremes and all ten reference repairs.
- **Should fix, general, voice/hints:** selection instructions could remain queued after an edit; Squint easing overwrote newer hints; returning to sharp in Fix gave Studio wording. Fixed validity and synchronous hints. All 51 fixed Read/narration lines match the manifest.
- **Should fix, general, part-menu narration:** a welcome held up the menu's selection instruction until an edit expired it. The kit only recognizes buttons for speaks; a local picker-focus validity guard now suppresses that welcome. Recheck: selectHow spoken once, welcome not spoken, no stale selection drop.
- **Should fix, general, comparison:** covered parts remained in Tab order, Squint stayed active without affecting the wipe, and Hint could name the hidden Before and after button. Removed background parts from Tab/accessibility content, dimmed the inert editor, disabled Squint, and made Hint describe the wipe. Opening/closing comparison hushes the previous view's speech.
- **Should fix, general, annotations:** compact comparison labels covered the title; gap labels could cover the date or clip at the page edge. Comparison labels now sit on the mat margins. Gap labels stay within the paper and omit collisions. Checked 680, 800, 1000, laptop, narrow and hosted-phone frames.
- **Polish, general, play/art:** lifted the flat rhythm repair with live edge-gap dimensions beside selected repeated parts. Added brief goal/stamp ink impressions, absent with Motion off. Redrew the severe angular cat as a smoother sitting pet with a curled tail. Kept the desk and every poster part.

#### Findings left

- **Should fix, general, spec conflict:** short previews require panel scrolling; the specified 375-pixel phone stack puts tools and Read's hint below the first screen. All 44-pixel editing controls cannot fit alongside the required poster, five meters and brief in a 680x425 box. Kept the specified layouts and documented the conflict rather than changing the spec. Main laptop tools and hint fit at 1280x720 and 1366x768.

#### Flattest moment left

**Polish, general:** Library Book Swap still needs repeated individual font/color edits. The part menu makes selection easier; an auto-fix or a new activity would change the specified play.

#### Graphics

Checked the desk painting at final size and all ten vector posters. Retained the strong painting; redrew Biscuit in code because poster colors/geometry must remain measurable. No missing art tokens or people assets. Painting: 130.1 KiB. Final offline bundle: **274,158 bytes (267.7 KiB)**.

#### Audit

Ran once, last, on Chrome 9931 and host 8735 with a 40-minute process-tree limit. Completed in **29.7 minutes**, with **329 raw leads**; inspected all **75 frames**. Evidence: `_scratch/design-fixer/review-audit/audit.md`.

Confirmed and repaired the picker instruction drop and comparison/annotation problems above. Remaining mechanical leads group into transparent expanded hit-region overlaps, the intentional wipe overlay, and the documented phone/preview scrolling. The comparison's covered parts are now excluded from Tab/accessibility content. Clear progress scrolling is a utility-row lead, not a hidden answer set.

Welcome misses on self-speaking controls are required first-tap behavior; Fix's welcome is present as a how line. Start over on a pristine poster intentionally changes nothing. Audit repeat/rapid-tap checks were clean; resize stress found no exceptions or stuck controls; Motion off had no infinite animation.

| Voice check | Expected | Observed |
|---|---:|---:|
| Selection instruction, five selections | 1 | 1 |
| Balance result, five new goal ticks | 5 | 5 |
| First Sound tap | 0 | 0 |
| First part-menu selection after repair | 1 selection, 0 welcome | 1 selection, 0 welcome |

Independent Python recomputed D65 pull/weight, tilt, repeated gaps and palette/locked constraints; all ten starts remain unsolved and all ten reference repairs meet their goals. WCAG pairs agree at 1.129829, 1.429077 and 7.903111. Module codes VA:Cr1, Cr2, Cr3 and Re8 have solo activities; notes open with the required three sections.

Only affected screens/voice paths were re-shot after audit repairs. Final drives had no console errors or warnings. No second full audit, commits, shared-source changes or out-of-scope writes. Owned Chrome/server processes closed; host.html removed.

#### Left open

- The layout conflict above needs a spec decision, not a hidden exception.
- Browser narration remains the fallback; the brief prohibits recording audio.
- Contrast uses finite sampling and can miss extremely small overlaps. Pull/weight use editable box area as specified; a tick is a model check, not an aesthetic verdict.
- Spec arithmetic: 18.7 / 24 is 0.77917, not 0.8. Kept the stated 3 percent and 2.4 percent thresholds.
- Kit change wanted is detailed in handoff.md: Curio.voice's first-tap target lookup should include native selects/inputs when matching speaks. The tool has a working local guard; the shared kit was untouched.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Design Fixer build handoff

#### Cold review changes

- Read the current source over historical implementation details below. Text now fits its box at natural letter proportions; the WCAG threshold uses the fitted cap height. Bounding-box pull and weight remain the spec's model. Cached canvas masks use the same text layout and have a 128-entry limit.
- Contrast samples later layers as well as earlier ones. Detached SVG geometry queries were unreliable; exact code paths now become cached Canvas Path2D hit masks, including strokes and cutouts. Covered text fails readability and receives a move/Bring forward explanation, including Hint. The foreground/background sampling remains finite.
- Poster hit rectangles expand to 44 screen pixels and stay inside the page. Overlapping enlarged targets favor the actual topmost content box. The part selector above Bigger provides an unambiguous keyboard/touch route to every element, including tiny/covered parts and locked Biscuit. The actual element geometry and model do not include the expanded hit area.
- Biscuit is a smoother sitting-pet silhouette with a curled tail. It stays flat, editable in Studio except for the brief lock, and uses the same single measured color and bounding box. The desk painting stays unchanged.
- Selecting a repeated part shows edge-gap dimensions while Guides is on. Guide numbers use contrasting ink; short gaps omit their label instead of colliding. Ticks and the earned stamp receive short ink animations, removed by Motion off.
- Queued selection instructions expire after an edit. Squint easing cannot overwrite a newer selection/edit hint. Returning to sharp in Fix restores that brief's instruction. All fixed Read hints are now included in the voice manifest.
- Biscuit's brief lock applies only in Fix. Studio permits moving, resizing and recoloring every part, as specified. Locked status is visible in the part menu without adding a row that pushes the laptop hint below the fold.
- Confirmed audit repairs: comparison removes covered poster parts from Tab/accessible content, dims the inert editor, disables inapplicable Squint controls, and gives the wipe instruction when Hint is pressed. Closing comparison restores editing. Comparison labels sit outside the paper, vertically in compact layouts, so they cannot cover the starting title.
- Gap dimensions sit above the bins; their labels stay inside the paper and are omitted if they collide with a part. The part picker is listed in Curio.voice speaks and the welcome also checks picker focus, working around the kit's button-only first-tap target. Opening its native menu cannot put a welcome ahead of the selection instruction. Entering/leaving comparison hushes the previous view's speech.
- Review evidence is in `_scratch/design-fixer/review-*`. The final audit outcome will be recorded in codex-review.md. No shared source or spec changed.
- The cold-review audit completed once in 29.7 minutes: 329 raw leads, 75 frames inspected, no runtime exceptions or controls stuck after resize. Confirmed comparison, annotation and picker-voice repairs received targeted rechecks afterward, including a hosted 375-pixel phone. No second full audit was run. Final bundle: 274,158 bytes (267.7 KiB). Owned Chrome/server processes were closed and host.html removed.

#### Built

Two modes, ten broken posters, five live meters, Squint and eye-path badges, selection and keyboard editing, drag/corner resizing, snapping guides, layers, locked Biscuit, goal ticks, a persistent completion list and the before-and-after wipe. One generated desk painting is bundled; the measured poster parts remain flat editable vector art.

`src.html` starts with responsive desk/panel styles and markup, then poster data and lines, the numerical model, icon geometry and glyph masks, stable poster nodes, rendering, pointer/keyboard controls and mode/persistence wiring. `window.__tool` exposes the model and read-only diagnostics for checks. Only poster changes rebuild poster nodes; editing keeps the interactive nodes stable.

#### Model and tricky parts

- Model coordinates are 1000 by 1414. Pull and weight use element bounding-box area, D65 sRGB CIELAB lightness and chroma. Text cap height is block height divided by its number of lines. The model notice is always under the meters.
- Contrast checks WCAG sRGB luminance. For overlaps, a 48 by 12 grid samples foreground glyphs against prior painted text and icon geometry. Canvas glyph masks cache normalized text and SVG paths provide icon masks. This is finite sampling; tiny overlaps can fall between samples. It is a teaching model, not a substitute for an accessibility checker.
- Icon cutouts paint the paper color, and the overlap model treats them that way. Color changes preserve these cutouts even after an icon has been white.
- The blurred poster is a separate SVG copy with CSS blur/grayscale. It explicitly toggles the SVG `hidden` attribute; setting an SVG `.hidden` property alone leaves the copy hidden. The transparent live SVG keeps receiving input.
- Corner dragging changes width and height independently. Bigger, Smaller, plus and minus resize proportionally. All movement is clamped. Snapping uses four screen pixels; unity edges and star-row alignment use four poster units.
- Tab skips the root SVG and visits poster parts in current top-to-bottom order, independently of the visual layer order. Programmatic focus always uses preventScroll.
- Every goal is recomputed on each rendered edit. Un-ticks are silent. The current attempt keeps its earned stamp after further edits; Start over or loading a poster starts a fresh broken attempt. Previously earned completions remain checkmarked in the menu.
- Clear progress removes `design-fixer-solved` and will not immediately re-award a still-met goal. Progress is a map of earned completions, not stored poster layouts. Studio work is intentionally temporary.
- Clearing hushes stale narration, closes the comparison and keeps focus on Clear progress. If all goals still tick after clearing, Hint names Start over instead of the hidden Before and after control.
- Active mode taps preserve edits. Reset on an already pristine poster is a no-op, so quick repeated taps do not cut the welcome. Sound reserves its label width to keep the header steady.
- Curio.voice owns narration scheduling; the tool owns the hint. How lines use V.heard and state validity; goal, fixed, locked and hint lines are events. Voice is big-sister, Leda, in the manifest. No audio was recorded in this build, as instructed; browser speech is the fallback.

#### Art

`art/prompts.json` stores the house style and full desk prompt. The built-in image tool made `art/raw/df-desk.png`; the only art.py invocation was `--rekey df-desk`. Finished art is 1500 by 938, about 130 KB. The usable center is approximately x 18-84 percent, y 2-97 percent. The poster is centered inside this region after cover crop, with a width guard in tall narrow stages. No people occur in the image.

#### Decisions and open questions

The spec contains no open-question section. These implementation interpretations are explicit:

- Keep all ten posters as listed: one unity brief and the final mixed brief, despite the introductory shorthand about two per principle.
- Use the stated 3 percent and 2.4 percent cap-height thresholds. Their 0.8 ratio is not exactly the source example's 18.7 divided by 24, which is about 0.779.
- Use flat measured vector parts and one rich painted desk, as the Art section leans toward. Do not add non-editable paintings inside posters.
- Add the small orange block to Biscuit's broken inventory so it can be enlarged and moved; there is no Add element control. This supplies the asymmetric repair described by the Sources example without extending the feature set.
- Honor the explicit "Nothing plays on its own" rule: no decorative idle animation. Squint easing and immediate edit/goal feedback provide motion when requested.
- At short preview sizes, the meters and hint remain together while the editor can scroll. At 375 wide, the stage and Squint appear first and the panel follows below, as specified. Small actual poster parts can be smaller than a 44-pixel tap target; their keyboard path remains available.

#### Evidence

Scratch contains independent Python formula checks and reference fixes, browser/Python comparisons, real pointer repairs of all ten briefs, all required sizes, hosted 375-pixel phone frames, Motion off, grayscale, min/max resize, overlap regression, keyboard and voice logs. The full audit runs last and its findings are summarized in codex-report.md.

The full audit completed in about 29 minutes with 356 raw leads. No runtime errors, stuck controls, infinite animations or repeated how-to failures were found. Read width, compact hint placement and rapid mode/reset welcome cuts were repaired and checked with targeted follow-ups. Phone below-fold leads follow the specified stacked layout; small poster-part targets remain open. Transparent hit rectangles account for the reported hidden title text; the frames show the lettering clearly. The full audit was not repeated after those local fixes.

The final comparison and stamp checks include 680x425, 1280x720, 1366x768 and the hosted phone. The stamp sits slightly across the paper's lower edge so Science Night's footer stays visible. The finished bundle is approximately 260 KiB, including 130.14 KiB of painted art. All 36 runtime lines match the voice manifest.

#### Engine changes wanted

`kit/curio.js`, `Curio.voice`, first-tap pointer/key listener: change the `closest('button')` target lookup to include native `select` and `input` controls before matching `opts.speaks`. The documented option currently cannot suppress a welcome for a native picker whose own instruction arrives on change. Design Fixer works around this using welcome validity while its part picker has focus. No shared file was changed.

#### Audit harness note

The audit's `steps` method wraps a drag string in a function body. It needs a body with a top-level return, whereas drive.py needs a returning expression. The first audit recipe used the latter format, so that one audit state did not reach its wipe. The stored recipe was corrected for cold review and the missing comparison coverage was checked separately with real pointer input. A helpful shared documentation change would name this distinction in `scripts/audit_tool.py`, function `Audit.steps`; no shared file was edited here.

#### Next

Cold review only. No commit, deployment or polish round was performed. Inspect small-poster hit targets and finite contrast sampling in the cold review. The 1280 by 720 editor and hint fit; the less-used Clear progress row can require a small panel scroll for the longest briefs. The specified stacked phone flow necessarily puts the editing panel below the first screen, so the general no-scroll rule cannot also be met there.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: handoff.md folded in (last changed 2026-11-04)

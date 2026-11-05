# Codex review: storyboard-studio

## Played

Cold, as a grade 10 student alone, with a projected-class view considered: composed a sequence, played both samples through, inspected cuts, repaired cameras, reordered, retimed and printed. Played before reading builder notes or source. Walked Teaching, Play and Craft personally. Strong studio atmosphere and immediate camera feedback; the ending needed a clearer visual payoff.

## Findings fixed

- Blocker, general, Plan: floor-footprint collision checks blocked cameras above objects, preventing centered overhead framing. A beat could also move Nico into an Eye camera. Clearance now respects height, and beat/height changes move an obstructed lower camera to a nearby clear position with an explanation. Rechecked High, Overhead, lowering and Nico's moving beat.
- Should fix, general, dialogs: Read was inaccessible behind native modal focus and its callback read the background hint. Added modal Read, active explanation/confirmation text, next-action narration and stale-welcome guards. Close, Keep and Escape hush speech. Combined explanations scroll while their action row remains visible.
- Should fix, general, voice: dynamic Board/collision hints were absent from the line registry. All variants and complete dialog readings now appear verbatim in allLines and voice/lines.json. Overhead hints explain the next action and distinguish Plan from Board.
- Should fix, general, mini-plan: The line label collided with camera numbers. Moved it into open space.
- Should fix, general, Board: the first sample view could name markers below the visible grid without explaining how to reach them. Added an explicit scroll cue to its hint and narration; checked it at laptop and compact sizes.
- Polish, general, renderer: the slice was a flat shape and the final beat barely changed. Added a shallow shaded wedge, raised crust, flat toppings, downward-looking poses and two separated halves near table height. Kept the marker grays and camera-dependent drawing.
- Polish, general, Animatic: playback ended without a clear status. Added Finished with this board's panel count and running time; it clears when the context changes.

## Findings left

- Polish/spec tension, general: long authored boards, twelve-panel strips and mixed-duration timelines scroll. Phone secondary fields follow the first viewport. Readable pictures, 44 px controls and the specified stacked phone layout prevent satisfying the blanket no-scroll checklist simultaneously. The primary viewfinder, camera and Add remain visible.
- Nit, general, renderer: very close or oblique placements can expose painter-sort intersections. The working-storyboard renderer is retained.

## Flattest moment left

The sample's final camera still aims at Remy during Ash's sharing action. Its exact coordinates and target are prescribed and produce the jump-cut exercise. A student's wider or Ash-facing revision shows the action better. The sharing pose and prop now visibly change when framed to include them.

## Graphics

Checked the existing 1500x844 editing-desk image at final size and in the layouts. No generated people, missing art tokens or placeholders. Kept the backdrop; redrew the procedural slice and adjusted poses because arbitrary camera projection requires code. No new raster assets. Existing bar comparison inspected without writing to other tools. Final bundle: 280,381 bytes, about 274 KiB.

## Audit

Completed once in 1571.5 seconds, within the 40-minute limit: 56 leads, no console errors, no infinite motion, no resize exceptions and no stuck-disabled controls. Evidence: `_scratch/storyboard-studio/review-audit/`. All 72 audit PNGs inspected in 20 contact sheets. No second full audit; final fixes received scoped rechecks.

Lead numbers below follow the report's rows in order:

- A01-A06: phone secondary fields below the first viewport. Retained layout limit above; independently measured Add bottom at 766.8 px in the 375x812 iframe, with viewfinder and camera visible and no horizontal overflow.
- A07-A08: 21 px checkbox glyphs. False positive: their clickable labels measure 79.5x44 and 115.1x44 px.
- A09-A14: two-panel phone secondary fields. Same retained page-flow limit as A01-A06.
- A15-A23: sample cards/markers outside the initial grid or phone viewport. Added spoken and visible scroll guidance; retained the authored sequence's readable pictures and all cut notes.
- A24-A30: scrolled background cards and hint behind a marker modal. Inactive background; the active diagram, explanation, Read, Close and Go to panel are visible. Rechecked a combined warning at 680 and 375.
- A31-A32: Late Bus phone Aim/Beat fields. Same secondary-field page flow.
- A33-A38: secondary fields behind Clear confirmation. Inactive background; the active confirmation and its three controls fit.
- A39-A40: playing-state checkbox glyphs. Same measured 44 px label targets as A07-A08.
- A41: viewfinder sample points covered by captions. Specified caption overlay, immediately switchable; the viewfinder itself is fully in view.
- A42-A48: twelve-panel strip scrolling and phone secondary fields. Retained sequence/page flow; active panel 12 is revealed and navigation remains available.
- A49-A51: Add, Duplicate and Clear skip the welcome. Required first-tap behavior: their own relevant line starts instead. Welcomes remain scoped and unmarked when skipped.
- A52-A54: idle Stop/Back/Step change nothing on a one-panel board. Expected boundary behavior; multi-panel playback assertions confirm immediate control actions.
- A55-A56: older Add/Duplicate warnings dropped as newer panels supersede them. Required staleness behavior, confirmed in the revision checks and logs; two fresh line-crossing events spoke twice.

43 independent functional assertions passed before the final scoped fixes; 11 scoped assertions passed afterward. Recomputed lens fields, all sample frame heights, 96-second maximum, exact sample markers, neutral boundary and 29/31-degree cases. Motion-on/off panel timing stayed within 50 ms. Real held keyboard repair/reorder and jittered pointer reorder passed. Reload preserved boards; practice copies stayed separate. Print is grayscale with patterns and notes. Checked every required size, phone iframe, grayscale and touched frames. Contrast: accent/panel 6.24:1; button ink/accent 6.60:1. All four standard codes are practiced through planning, ordering, continuity repair and retiming. No hidden-answer or unknown-clue mechanic applies.

Voice counts:

| Line/action | Kind | Expected | Spoken |
|---|---|---|---|
| lineHow across five held Add taps, 2 s apart | how | 1 | 1 |
| Two fresh line crossings | event | 2 | 2 |
| Dialog Read | read | Current dialog | Matched |

All 37 runtime line strings match the manifest. Audit rapid-tap checks were clean. State hints update immediately, focus survives reorder, warnings pair words with icons, and Motion off preserves timing. Final desktop and phone rechecks have no tool console errors. A host-only favicon 404 was corrected in the temporary harness and its affected shot rerun cleanly.

## Left open

- No recorded narration, following the no-recording build rule. Browser speech remains the fallback.
- Phone secondary fields and long-sequence scrolling are documented limits, not an entirely clean mechanical-audit claim.
- High/Overhead clearance uses the specified physical heights above the actors and table; no scripts, sample cameras, continuity thresholds, topics or modes changed.
- No commits. Review writes stayed in the two allowed folders. Test Chrome instances and servers are closed; host.html is absent. This report was written last to honor the stop instruction.

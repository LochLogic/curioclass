# Virtual Gallery build handoff

## Claude Refine fixes, 2026-11-05

This section supersedes the historical camera, landscape-art and compact-label descriptions below. The active list
is refine.md, unchanged. The scoped result and evidence map are in polish.md after the final audit.

The door camera stays straight ahead and adjusts its focal length to include a back- or side-wall first-seen frame's edges.
That frame has a double outline. The floor cone projects from the doorway toward those edges. Hang keeps the main
three-wall room and unfolds the inward-facing door wall below it, with the door gap and both sets of pictures.
The unfolded surfaces use the same placement data and collision solver. Pointer coordinates on them are mapped
back into physical centimeters, so moving a picture there remains an actual hang operation.

Walk's large duplicate label is a disclosure below the room. The current wall label is drawn at readable screen
resolution at every width. Neighboring label cards keep blank paper rather than enlarged 3 px text. Squeezed cards
carry a persistent data-squeezed flag through camera redraws and travel. A jump stop awaits the voice promise as well
as the usual two seconds, while Stop, Step, Back, strip taps and Route retain their immediate interruption behavior.

The checklist uses two columns with Why and Show me side by side. Why opens the same explanation in a dialog.
Blank, whitespace-only or punctuation-only notes keep a visible missing-note warning. Blank notes still meet the
specified format check. One-word statements, matching tags and starring the named first-seen work remain possible
mechanical passes by the settled calls; meaning and prediction are not graded. Do not silently add new writing
requirements or a locked star. The 145 cm default is explicitly the tool's standing-viewer starting height, not
Smithsonian guidance. The guide's lower small-item recommendation is explained in Line Why and notes.md.

Seven landscape works were redrawn with built-in OpenAI imagegen at 3:4 portrait and processed using art.py --rekey.
They are 600 by 800 pixels and each is under 50,000 bytes. Kitchen Window has a clean right window jamb.
Map of My Block and Fire Escape Garden were also compressed below 50,000 bytes and inspected at card and detail size.
No people, lettering, new topics, shared-engine changes or git commits were added. Spec open questions stay open.

### Round 2 first-seen repair, 2026-11-06

The exit check explicitly resolves the earlier door-wall question: inward-facing door-wall works are behind a
visitor looking straight ahead, so firstSeen() excludes them. With no back- or side-wall work, it returns null,
Anchor fails, and Walk says no work is in view from the door. The visitor may still walk to every hung work.
The end comparison also requires a real first-seen id before claiming it matched the star.

The legal Kitchen Window left corner, placed through place() at x=577 cm, reproduced the missing picture despite
its visible DOM box. The left wall's flattened compositing surface clipped its far-end children in Chrome.
Only the Walk left wall now preserves its 3D children. A controlled preserve-3d probe paints the frame; removing
the child transform, allowing backfaces, and promoting only the frame do not. Do not apply preserve-3d to every
wall: that introduces a texture seam on the back wall. Keep Hang's existing flat wall surfaces.

Compact wall choices read Back, Right, Door R, Door L, Left. The selected wall's full name is in its accessible
label and its full name and dimensions remain in the title. This fits the 63 px preview selector without
changing its 44 px target. Legal-left-corner and all-door-wall fixtures are in audit-states.json.

The corner stop also exposed that drawWalkArt() skipped its readable label when the physical card was squeezed.
The readable overlay now uses the work's projected label-height center and available screen space independently
of the physical card width. The physical squeezed card still stays hidden during travel and at a stop.

Round 2 evidence and the report draft are in _scratch/virtual-gallery/round2/. The final polish.md distinguishes
new before/after repairs from the twelve should-fix items already closed by the cold exit check.

### New round 2 audit lead left open

The final audit found real focus losses on empty Checklist Show me for Selection, Theme and Labels at 1366x768.
showProblem() enters empty Hang, then tries to focus wall-choice or edit-label, which the empty panel does not
render. The Labels branch also overwrites the correct empty hint with Tap Label to edit. This means the original
should-fix 8 is not fully closed for every empty Show me path, despite the prior exit check's closure.

The exact local follow-up is in src.html, showProblem(): handle !state.chosen.length before choosing a per-work
target, preserve L.emptyHang, and focus an enabled Select control with preventScroll. Preserve the separate
empty-statement path and do not describe a nonempty, unhung tray as empty. Reproduce all three empty Show me
buttons with held clicks, then verify focus and Read's hint at 1366x768 and 680x425. This is a tool fix, not a kit
change. No post-audit repair round was started; polish.md reports the lead as NOT FIXED.

## Cold review, 2026-11-04

The build notes below are historical. The compact scrolling limitation is repaired: all workbench controls retain 44 px targets and fit at every required size, including the desktop Plan supplement. Panel controls precede the tray in keyboard order.

The review preserves the room and portfolio. Seed Packets, Map of My Block and Fire Escape Garden were redrawn with built-in OpenAI imagegen and processed with art.py --rekey. All assets explicitly mark people false. Paintings keep their native aspect within physical frames; dense map/photo replacements exceed the old individual 50 KB target while the whole bundle remains about 1.1 MB.

Checklist claims are limited to measured conditions. Punctuation-only titles/statements fail; length and shared-tag checks remain mechanical. Notes explain the need for human interpretation, and allow fictional home settings. Do not add an arbitrary word minimum or treat nine ticks as an artistic grade.

Other repairs synchronize every gap readout, reject cramped Auto space with corrective feedback, show room gap rulers while dragging, constrain label paper to available frame gaps, preserve between-stop camera state without a stale label, expire obsolete jump speech, bound long text, repair empty diagnostics, and re-arm readiness events. Modal how lines and generic own-work/theme events are in voice/lines.json. The upper metric label range converts to about 66 inches; the Smithsonian guide prints 67, an inconsistency now identified in notes.

Independent evidence is under S:/CurioClass-codex/_scratch/virtual-gallery/: cold/, checks/, student-review/, side/, final-checks/, last/, pre-audit/ and scope-recheck/. Functional checks passed 39/39; imports passed 6/6; actual keyboard deltas were +5/-25 cm, Delete and Enter; the eight-work Motion-off walk took 24.158 seconds. Main-path and side-path voice logs are saved. The one final audit under review-audit/ was interrupted by the session restart after the size/state/Motion-off stages. Its 17 grouped leads concern the specified scrolling checklist and inert modal backgrounds. All 89 frames were inspected; full automated resize/control-walk coverage is incomplete and is not claimed as passing. Focused post-audit re-checks and the disposition are recorded in codex-review.md.

Final state guidance also keeps Hang on a chosen work after removal, directs an unhung selection to hanging, and lets empty-phone text span the strip. Checkmarks now say Meets check, with an explicit limit to measured conditions.

Fresh restarted checks passed the corrected state guidance, all 36 declared narration lines, an actual slider sweep, and a Motion-on mid-walk resize from 1366 to 760 and back. All task Chrome/server sessions are closed; host.html is removed.

No shared engine, scripts or documentation changes. No git commits. The requested review report is the final write and stop point.

## Structure

src.html begins with the shared kit and grade 9-12 theme, followed by gallery-specific responsive styles. The script contains the exact portfolio, physical room geometry, persistence, voice table, nine independent checks, four views, camera projection, pointer and keyboard input, and editors. Images use art tokens. window.__tool exposes state, geometry, checks, voice log and actions for independent review.

## Important implementation choices

- The show starts in Select when empty, and Hang after restoring a chosen work. Adding a work keeps Select open so comparison remains easy.
- Hanging is possible by pointer or by selecting a tray work, choosing a wall, and activating Hang on wall. Arrow keys use centimeters and the same collision solver as dragging.
- The camera uses a look-at matrix applied to a CSS 3D room. The first-seen calculation uses physical frame edges and does not infer attention from camera pixels.
- First-seen includes vertical distance to the 160 cm eye line. A low small frame does not receive a zero angle merely because it is centered horizontally.
- Each wall is a flat local compositing plane in the 3D world. This avoids Chrome software-compositor gaps at corners with unlit work. High-resolution artwork and wall-label overlays preserve detail at walk stops.
- Front-wall segments are separate 340 cm surfaces with a 120 cm door opening. The bowl has a 30 cm shelf rather than a mat and frame.
- Plan supplements the room in the desktop panel. A short preview and a phone use the plan as the main Hang view automatically. The full visitor view remains available on the phone.
- A work starts unlit to make the lighting decision visible. The spotlight appears as soon as Light is used.
- First-seen uses the frame area to break angular ties. Shared-tag jumps refer to hung works in tray order.
- Selection does not silently add a statement, star, lights, or tags to imported work.
- Saved shows may contain imported-work references, but no imported image pixels. Restore drops those references and shows the specified message.
- Imported work is not attributed to Jordan Reyes. Its artist name is left blank, including on the room label and the large visitor label.

## Open questions and spec corrections

The spec contains no explicit open-question list. The following ambiguities were resolved using its stated direction:

- Default mode after a choice: keep Select while actively comparing; restored nonempty shows open in Hang.
- Counterclockwise changes the route direction from the door; the required stops remain in tray order, as the spec explicitly states.
- Spec arithmetic says eight widest framed works need 745 cm. The listed widths, plus 16 cm framing and seven 30 cm gaps, total 685 cm. The actual dimensions are used. spec.md is unchanged.
- Supplied portfolio images include several landscape assets despite the revised spec asking for portrait assets. Existing art is retained at its native aspect in the portfolio and displayed in the specified physical frame sizes. This preserves supplied work rather than inventing a replacement portfolio.
- Imported pictures use a nominal 40 cm long print edge, proportional dimensions, and student-set tags. The size is labeled Preview print. No dimension editor was added because the spec does not request one.
- The bowl's shelf is 30 cm wide; its drawing uses a 22 cm vertical envelope. Only its 18 cm diameter is given in the spec, so this height is a rendering setting, not an additional supplied measurement.

## Compact layout limitation

At 680x425 and 375 wide, the tray, main view, selection, lighting, label editor, wall picker, Hang on wall, Auto space, Statement and Walk remain accessible in the initial viewport. Secondary height/order/remove controls require scrolling the workbench. This does not meet the strict reading of Done when 10; the report marks it FAIL instead of claiming every tool is simultaneously visible.

Gap numbers are shown in the room status, workbench and drag hint. They are not drawn as dimension rulers between frames on the wall. The plan connects the work stops in tray order; the camera uses a directional aisle route between stops so Counterclockwise can change travel without reversing the required tray order.

## Build verification

Thirty browser functional assertions passed, including all nine checks on passing and failing cases and a vertical-angle first-seen case. A complete keyboard-only six-work student run reached nine of nine ready checks and produced the printed exhibition sheet with no exceptions. The five-hang held-click voice run logged welcomeHang, lightHow and hangMore once each. The eight-work Motion-off walk measured 24.14 seconds. See Scratch artifacts listed in the report for results and reviewed frames.

## Mechanical audit and final repairs

The single full audit completed in 1,646 seconds and reported 122 leads. Its Motion off, resize recovery, held-click runtime errors and five-click repetition sections were clean. All 81 audit frames were reviewed in nine contact sheets, with the main sizes and modes also inspected independently at full size.

Final repairs set header targets to at least 44 px, name both textareas explicitly, reserve the compact workbench footer, reduce short-editor height, fix the singular stop count, and make taps on the current mode leave its narration running. Decorative scaled room lettering is hidden from assistive technology; the tray, editors, workbench readouts and large visitor label provide the corresponding accessible information. Small viewer layouts use the large label without an overlapping miniature replica.

Eleven targeted final cases passed, including actual growing/night narration, a same-mode welcome with no cut, a scrolled lower-card pointer click with focus retained, imported work with no false artist attribution, a Motion-off cut at the correct time, visible compact editor Done buttons, automatic phone plan, and visible primary phone controls. The desktop plan supplement was re-shot after its viewport and ink contrast repairs. No full audit was repeated after these changes; audit/audit.md is the earlier snapshot and codex-report.md gives the final dispositions.

The bowl was also checked in Hang and Walk after seating its 18 cm image on the 30 cm shelf; the enlarged view has no transparent frame border consuming its width.

Final bundle: 956,507 bytes. Sixteen WebP assets total 567,480 bytes. Source has 1,848 lines with a maximum line length of 160. All test Chrome instances and servers are closed, and host.html is removed. Repository changes are confined to tools/virtual-gallery/. No git commit or polish round was made.

## Art

Fourteen portfolio images were already present. Missing warm plaster and oak floor textures are generated during this build with the imagegen skill and converted through scripts/art.py --rekey. A monochrome charcoal tomato drawing replaces the supplied red-colored rendering to match the stated medium. Full prompts and provenance are in art/prompts.json.

## Engine changes wanted

None. No kit, scripts, documentation or other tools were edited.

## Review next

Read codex-report.md for measured results and any incomplete requirements. This is Build only, with no git commit or polish round. The report distinguishes verified checks from limitations.

A final whole-pixel, jittered pointer drag on the desktop plan moved Map of My Block from 400 cm to 531.41 cm on the back wall. The room and plan updated together with no console errors. Evidence: Scratch plan-drag-result.json and plan-drag-frames/plan-drag-final.png.

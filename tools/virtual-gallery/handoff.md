# Virtual Gallery build handoff

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

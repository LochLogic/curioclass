# Compass and Straightedge handoff

src.html contains independent CSS, semantic controls, the geometric engine, SVG rendering, and the 15-page Book.
The source is bundled with kit:curio for shared voice and power settings. No kit stylesheet is used.
History stores only points, objects, log, serial, nextName and unitLabel. Instrument settings, view and Book ghosts stay put.
Made intersections record parent object IDs; deletion cascades.
Ghost reference geometry is kept outside the student's point set. Book sub-constructions are compound where named.
Scratch contains bounded command runner, numerical/interaction evidence, screenshots, and audit results.
Geometry changes are synchronous; createObject coalesces SVG painting through requestRender. Keep that separation:
the 47-object, 1,115-point classical pentagon replay otherwise spends too long redrawing intermediate states.
The full replay is _scratch/compass-and-straightedge/pentagon-method.js. It adds no free points and never retains a radius.
Blank paper labels its unchanged reference unit u, because its new free points can also be named A and B.

## Cold review changes
Read uses currentHint() for the active instrument, selected anchors and blank paper. Only the initial hint speaks automatically.
The Book figure renders requested steps too, so the open drawer never hides an action's only visual response.
IV.16's bisector now points midway between the 72-degree and 120-degree vertices; the trisection page draws both halvings.
lineShape clips infinite lines to the paper, including when both defining points are off screen.
validSavedState checks a device slot before checkpoint/restore. Malformed data must leave the live sheet untouched.
MacTutor's CC BY-SA 4.0 text licence is named explicitly; only factual paraphrases are incorporated.
Audit follow-up: nearby point labels try alternate positions with fine dashed leaders; geometry and hit areas stay exact.
The phone zoom tag sits at the upper-left, clear of the idle compass. The resting edge is under the strokes at the table edge.
Counts use singular nouns at one; tiny nonzero magnifications use scientific notation.
Repeated presses of the same instrument retain valid speech; actual tool changes still hush it.

## Refine fixes
Tangencies collapse roots with half-separation within 1e-7 times the larger radius. Crossings merge within
1e-7 times the largest stroke size (at least one unit); free and given points retain the 1e-9 threshold.
Book guides use similarities onto matching givens. Unmatched studies sit beyond the drawing with primed letters.
IV.11 shows each compound sub-construction separately so its repeated A and B cannot label different points at once.
Point names after Z use numeric subscripts. Dense, unselected crossing labels hide until hovered or selected.
Pointer motion requests one render per animation frame. Point dots share SVG paths, the record is cached, and a
readout's live text changes only when its value does. Its position avoids visible point labels and controls.
The two new margin identifications require a closed square or regular hexagon of actual chords on the given circle.
Book lettering is placed from actual SVG glyph bounds, with short leaders where needed. The drawer opens before
the figure is measured so the first figure is as legible as subsequent steps at 680x425.
Older saves without reference-placement metadata derive it on the next Book step; malformed placement data is rejected.
The IV.10 transfer explicitly refers to the longer part of the preceding golden division, rather than an absent H.

## Engine changes wanted
kit/curio.js: allow a caller-supplied power-button label formatter instead of replacing button text with emoji.
This tool applies its own plain lamp-panel labels through onMotion and onSound callbacks.

## Decisions
The report is written last because the user's explicit stop condition overrides the early-report instruction.
Trisection says no construction works for every angle; some angles do trisect.
The first triangle requires selecting Edge after the two compass circles. The spec implicitly changes instruments.
Join A to B to close the drawn outline too; the three-vertex triangle can already be measured before that final stroke.
No marked-ruler extension; the spec defers it. No raster art, because exact drafting material is the interface.

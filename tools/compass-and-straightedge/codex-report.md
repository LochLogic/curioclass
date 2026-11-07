# Codex report: compass-and-straightedge (Curiosity No. 09)

## Built

An offline drafting instrument on cream paper, with a swinging brass compass, unmarked steel straightedge,
computed crossing points, ink, erasure, measurements, a chronological record, undo and redo, pan and zoom.
The lower-left maker's plate and Manual, and the separate Motion, Sound and Read lamp panel, carry the family marks.
The Book has 15 independent pages. Four local save slots, given sheets and printing are in the Paper cabinet.
The wide log collapses; narrow screens use a log drawer. Phone Book and log drawers open at the bottom.

Bundle: **83,369 bytes (81.4 KiB)**, below the 500 KB specification budget and the 2 MB goal.
Source: [src.html](src.html). Offline file: [compass-and-straightedge.html](compass-and-straightedge.html).
Build only: no commits, deployment, shared-engine edits or polish round. Required tool files are present.

## The real material

- Original analytic geometry: double-precision line/line, line/circle and circle/circle intersections;
  segment bounds, isolated tangencies, coincident cases, and a 1e-9 sheet-unit merge tolerance.
  Counts and measurements come from the drawing, not a reference answer. No outside dataset.
- Euclid, *Elements*, T. L. Heath translation, Cambridge 1908: the 14 supplied enunciations and three postulates,
  Books I and IV constructions, and XIII.8's pentagon relationship. Public domain in the US.
  The specification's supplied wording was used; no Perseus transcription markup was copied.
- MacTutor, University of St Andrews: Wantzel, Gauss, Lindemann, Mohr and Mascheroni historical facts,
  paraphrased from the specification's named sources. Facts are not copyrightable; article text retains copyright.
  No article prose or images were reproduced. Links and permission notes are in the Manual and metadata.
- Original code-drawn instruments, paper and Book figures. No painted data, downloaded art or outside library.
  Blank sheets retain the reference unit as u, so new free points named A and B do not falsely redefine AB.

## Break the instrument

- **29 numerical assertions passed**: intersections, tangencies, disjoint and coincident circles,
  finite-segment bounds, parallels, right and undefined angles, equilateral sides and angles, and six-step closure.
- I.2 transfers a length using made points with the collapsing compass; its opening remains zero.
- The full Book-method pentagon replay uses I.46, II.11, I.2, IV.10, IV.2 via I.23, and I.9 before IV.11.
  Result: **47 objects, 1,115 made points, zero free points**, equal sides, and diagonal/side **1.6180339887498931**.
  This is an actual instrument replay, not just the finished reference figure. See pentagon-method.js and its result JSON.
- An initial rapid pentagon replay timed out while repainting intermediate states. Geometry now updates synchronously
  and SVG painting coalesces into the next frame. The same constructive replay then passed without console errors.
- Jittered, held real drags make the two circles and I.1 sides. Keyboard input measures 60.00 degrees.
  Degenerate or unmade anchors are rejected. Repeated free points do not create false free-point log entries.
- Undo/redo restores geometry and ink; erasing a point removes dependent objects. Empty paper and both zoom bounds work.
  Local save/load restores the drawing; blocked storage reports the problem while preserving the current paper.
- Real phone panning and two-finger pinch passed in a 375x812 iframe; scale changed from 114.2308 to 159.9231 px/unit.
  Two circles and four points remained usable, with no page scroll. A resized running sheet retained its objects.
- Forty rapid circle additions and their undo passed. The tested clean triangle prints on one landscape page with its log,
  with zero visible instrument decorations and zero external network requests. See print-check.json and printed-sheet-final.pdf.
- Final focused checks verify a live circle, log collapse/reopen, a clear point label beside the radius tag,
  u on blank sheets, and five source links at least 44 by 44 pixels. A disconnected Chrome batch passed on its smaller retry.

## Voice walk

knowing-guide is selected in voice/lines.json; no audio was recorded, as instructed. The shared kit uses browser speech fallback.
The main drag path speaks "Drag from A to B." once. The 606.4-second replay records one welcome and one requested Read,
with no automatic speech on Book pages or repeated drawing actions. Read also speaks with Sound off.
Read includes the current hint, last log sentence and selected readout. Status regions expose point names and measurements.
The first timed automation left the Manual open after an ineffective synthetic Escape. Explicit Escape handling and cursor
reset were added, virtual key codes corrected, and the full timed walkthrough was replayed with all adult-path drawers closed.

## Short test

The controlled agent exploration lasted **606.4 seconds**, using grade-10 and adult lenses. This is not a child user study.

- Would a kid open it unassigned? Likely: the first drag physically sets and swings the compass; crossings invite another action.
- Would an adult play for fun? Yes by this assessment: collapsing-compass transfers and the full pentagon are real construction problems.
- Is the real thing the interface? Yes: every working circle, segment, crossing and readout comes from the analytic drawing.
- Does it work without a score or finish? Yes. The Book was browsed in all 15 positions in a deliberately mixed order,
  with no prerequisites, ticks, ratings or saved page achievements. Its method steps appear only when requested.

Our instrument beside Elements Inspector, both opened and used during the build:

![Compass and Straightedge beside Elements Inspector](../../_scratch/compass-and-straightedge/targeted/frame-comparison.png)

## Lesson creep check

The requested word search was run on src.html and the voice lines. No score, level, goal, sticker, badge, correct,
wrong, try again, complete or well done hits remain. "Points" denotes geometric points and their data structures,
never rewards. The log's numbers order construction moves; the zoom percentage is magnification.
There is no kit header, mode-pill row, task ladder, quiz, timer, celebration or finish screen.

## Done when

| Item | Result and evidence |
|---|---|
| 1. Open and draw two circles | PASS: initial A/B and instruments; real drags produce two circles and two crossings. |
| 2. I.1 lengths and angles | PASS: 1.0000, 1.0000, 1.0000 and three computed 60.00-degree angles. |
| 3. Six-step closure | PASS: six made-point circles return to the original rim point, including with the collapsing compass. |
| 4. Book-method pentagon | PASS: full 47-object construction from A/B alone; measured ratio 1.6180. |
| 5. Collapsing compass and I.2 | PASS: opening returns to zero and the copied length matches numerically. |
| 6. Made points, log, undo/redo | PASS: invalid anchors rejected; chronological log and dependency-aware erasure restore through history. |
| 7. Fifteen independent pages | PASS: every page browsed out of order; ghosts only on request; no completion marks. |
| 8. Keyboard, announcements, Motion off | PASS: drawing, free points, measurement, ink, erasure, history and view keys; named native controls; instant calm circles. |
| 9. Responsive sizes | PASS: all eight STANDARDS sizes, including the real 375x812 iframe, with no page scroll. |
| 10. Print, offline, checker, punctuation | PASS for the tested sheet: one print page plus log; no requests; production checker functions pass; no em dashes. |
| 11. Honest short test | PASS: answered above with the frame comparison and the Book's deliberately nonsequential exploration. |
| 12. No lesson game layer | PASS: source and voice search, visual inspection and timed use. |

The opening's implied switch from compass to straightedge is made explicitly by the student; no automatic tool change.
Join A to B as well to close the drawn outline. Its three-vertex triangle can be measured before that final stroke.
The trisection note distinguishes particular trisectible angles from the impossible general construction.
The user's stop instruction takes precedence over the machinery's early-report instruction, so this report is written last.

## Audit leads

The mechanical audit ran once and finished: **320 leads, 23 frames**. It reports clean Motion-off and mid-action resize checks,
no errors on 19 held-control paths, and clean recorded repeated/rapid speech paths.

- 201 overlap leads: the focusable full-screen SVG lies under its instruments, maker's plate and measurement tags by design.
- 112 hidden-background leads: modal Book, Manual and Paper drawers intentionally cover the inert paper controls.
- Five small source links: fixed to 44-pixel minimum targets, confirmed by the final DOM measurement and frame.
- One scroll-panel lead: bibliography links are below the first viewport of the long, scrollable Manual; its Close stays available.
- One missing-hint lead: the permitted first-run hint disappears after the first drawing action.
- Sound cutting speech and Read skipping the welcome are the specified kit behaviors, not missing narration.

The full audit was not rerun after the focused source-link, unit-label, redraw and log-control fixes.
Those changes received targeted checks instead. The global check_tools.py entry point would rebundle other tools,
so its actual check() and notes_sections() functions were run on a scoped draft mirror, with all production rules intact.

## Frames looked at

Beat Lab, Elements Inspector, Span and Spire, Pocket Universe; all early and full-size frames; grayscale and Motion off;
the real-drag triangle; Book and ghost frames; corrected timed student/adult frames; phone circles and Book;
both print previews; ratio and full constructive pentagon frames; final source-link, unit and log-control frames.
All 23 audit PNGs were inspected in four contact sheets, including short and phone Book pages and all drawer states.
Failed-fixture and first-walkthrough evidence is preserved separately rather than presented as passing evidence.
Evidence and hashes: ../../_scratch/compass-and-straightedge/validation-manifest.json.

## Art made

No raster images. Paper tooth and lamp gradient, brass compass, steel straightedge, cloth Book control, point labels,
pencil and ink strokes, and exact Book figures are drawn in CSS and SVG. No placeholders or art left to paint.

## Engine changes wanted

None required. Optional: kit/curio.js showMotion() and Curio.init() could accept a power-label formatter,
so an instrument need not replace the shared emoji labels in onMotion/onSound callbacks. The kit was not edited.

## Left open

- The knowing-guide recording is not produced in Build; browser fallback depends on the device's installed speech voices.
- No physical school-Chromebook frame-rate measurement, screen-reader hardware walk or human child usability study was performed.
- Very dense constructions can have overlapping point labels; pan and zoom inspect them. The 600-object guard and
  numerical limits are disclosed in the Manual. A month of depth is a design assessment, not a month-long observation.
- Print pagination was verified on the documented triangle sheet, not every possible length of construction record.
- The marked-ruler extension remains deferred, following the specification's lean. No plan.md was invented; this remains a second card.
- No test servers or debugging listeners remain on the assigned ports; cleanup-check.json verifies kernel TCP state.

# City Skyline Studio

## One idea
The camera is real: the horizon is always your eye height and the two vanishing points come from the angle you stand at, so lifting the eye from the sidewalk to a rooftop to a helicopter redraws the whole skyline correctly, and you ink your own drawing over guides that obey the same rules.

## Not like
- vanishing-point-studio (6-8, studio, same family): one vanishing point, fronts flat to the page, boxes drawn by dragging. Here two vanishing points (three with Tilt), buildings set at any angle on a city plan, and a camera you move; its Line snapping is extended to two points.
- near-and-far (3-5, same group): depth cues with a fixed camera and cut-outs. Here the camera is the thing you move.
- frame-it (6-8, lab): a photo camera for composition rules. Here the camera's height, turn and lens build a perspective construction you then draw.
- storyboard-studio (9-12): shots and cuts over time. Here one drawing.
- virtual-gallery (9-12, same group): a room you walk through to hang art; its view is a simple room box, not a construction tool.

## Who and how
- Grade 9-12, visual arts, module "Two-Point Perspective and Composition (Visual Arts)".
- Topic line: two-point perspective
- Driver: students (laptops). 20 to 45 minutes; works across several sessions (the drawing is saved on this device).
- Standards: NCAS VA:Cr2 (organize and develop artistic ideas and work), VA:Cr3 (refine and complete) for the Ink stage.

## Screens and modes
Header: title, topic line, `Read`, `Motion`, `Sound`. Kit theme `theme-912`. Modes (`.seg`): `Build` (the default), `Ink`, `Find the Camera` (optional).

**Build.** Stage: the perspective view of a city block at dusk, drawn at real pixels: sky, the horizon line (labeled "horizon = eye level, 1.6 m"), the two vanishing points as red dots on it (labeled VP L and VP R; an arrow at the edge when one is off the page), the ground with a street grid, and the buildings as shaded boxes. Panel, top to bottom:
1. Camera (section): `Eye height` slider (log scale, 1.6 m to 400 m, with stops labeled `Sidewalk 1.6 m`, `3rd floor 10 m`, `Rooftop 60 m`, `Drone 150 m`, `Helicopter 400 m`); `Turn` slider (0 to 90 degrees, the street grid's angle to the picture plane; 45 marked); `Lens` buttons `24 mm`, `35 mm`, `50 mm`, `85 mm`; `Horizon on page` slider (20% to 80% of the stage height); `Tilt` slider (-25 to 25 degrees, 0 by default, with "Tilt makes it three-point" beside it).
2. Readouts (`dl.readouts`): eye height, turn, lens and its horizontal field of view, VP distance apart in px and "focal lengths", and, with Tilt, the third vanishing point's position (above or below, in px).
3. Buildings (section): a palette, `Tower` (20 by 20 m, 40 floors), `Block` (40 by 30 m, 8 floors), `Slab` (60 by 15 m, 20 floors), `Stepped` (three stacked boxes), `Water tower` (a cylinder on legs; drawn as a box frame with an ellipse top). Tap one to drop it on the next free lot. For the selected building: `Floors` (1 to 80, 3.5 m each), `Width`, `Depth`, `Remove`. Floors count changes height live.
4. Overlays: `Guides` (lines from every visible corner to its vanishing point), `Plan` (a top-down inset of the block, the eye, the picture plane, the two sight lines to the VPs and the 90 degree mark between them), `Windows` (window grids drawn in perspective on every face), `Sun` (a dial for light direction; faces shade in three values).
- Drag a building on the stage to move it across the ground (or on the Plan inset). Buildings sit on a 10 m lot grid; they cannot overlap (they push aside).
- `Example city` loads a finished block of nine buildings; `Clear city`.

**Ink.** The same camera, frozen (the camera panel collapses to a line of readouts and an `Edit camera` link back to Build). The render fades to 20% and the guides stay. The student draws on a transparent layer:
- `Line`: drag; the stroke snaps to the nearest of VP L, VP R, VP 3 (with Tilt), vertical, or horizontal when within 6 degrees, and shows which ("to VP L"). Hold Shift (or turn off `Snap`) for free lines.
- `Hatch`: drag over a face; fills it with parallel lines aimed at that face's vanishing point, spacing from a slider.
- `Fill`: tap a face to fill with one of three values (light, mid, dark) or a dusk color.
- `Erase`, `Undo`, `Redo`, `Show render` (toggle the 20% render), `Hide guides`.
- `Save picture` (PNG at the stage size, without guides). The ink layer and the city are saved on this device (localStorage `city-skyline-studio`), `Clear drawing` empties the ink only.

**Find the Camera** (optional). A target skyline drawing (a line drawing of a set city from a hidden camera) shows as a pale overlay. The student moves `Eye height`, `Turn` and `Lens` until their render's outline matches. A match meter shows the overlap of the two silhouettes as a percent; at 92% or more: "Matched. Eye height 60 m, turn 30 degrees, 35 mm." and `Next target`. Six targets (Content). No timer.

## Content
**Camera model.** Picture width W px. Focal length in px f = (lens mm / 36) x W (a 36 mm wide full-frame sensor). Field of view = 2 atan(18 / lens mm): 24 mm 73.7 degrees, 35 mm 54.4, 50 mm 39.6, 85 mm 23.9. The eye at height e, level unless Tilt. A world point (x, y, z) (x right, y up, z forward from the eye) projects to u = W/2 + f x / z, v = h - f (y - e) / z, where h is the horizon's screen y (the `Horizon on page` setting is a lens shift; it never changes the drawing's geometry, only where it sits on the page).
**Vanishing points** for a grid turned by angle t: one family of edges runs along (cos t, 0, sin t), the other along (-sin t, 0, cos t). VP R is at u = W/2 + f cot t and VP L at u = W/2 - f tan t, both on the horizon. Distance between them = f (tan t + cot t) = 2f / sin 2t, smallest (2f) at 45 degrees. Seen from the eye, the two VPs are always 90 degrees apart (the Plan inset shows this). At t near 0 or 90, one VP runs off the page: "Nearly one-point perspective: see Vanishing Point Studio."
Worked check, W = 1200, 35 mm: f = 1166.7 px. At t = 45, VPs at 600 - 1166.7 = -566.7 and 600 + 1166.7 = 1766.7 (both off a 1200 px page). At t = 30: VP L at 600 - 673.6 = -73.6, VP R at 600 + 2020.7 = 2620.7. With 85 mm (f = 2833.3) at 45 they are 5666.7 px apart. The builder recomputes in Python and keeps these as tests.
**Tilt** (three-point): the camera pitches by p; verticals meet at VP 3, at distance f / tan p from the image center along the vertical (above for looking up, below for looking down); the horizon moves by f tan p the other way.
**Facts shown on screen:** "The horizon is always at your eye height." "Every building is crossed by the horizon at the same real height: your eye height." "Above the horizon you see bottoms, below it you see tops." "From the eye, the two vanishing points are 90 degrees apart." "A wider lens puts the vanishing points closer together and stretches the edges."
**Lots:** a 7 by 5 grid of 30 m lots with 15 m streets, the grid centered 120 m in front of the eye at Turn 30 by default.
**Example city:** nine buildings on the central lots (heights 6 to 52 floors), mixing all five types.
**Find the Camera targets** (eye height, turn, lens): 1.6 m, 45, 35 mm (street level, symmetric); 60 m, 30, 35 mm; 150 m, 20, 24 mm; 10 m, 60, 50 mm; 400 m, 40, 85 mm; 1.6 m, 15, 24 mm with Tilt 15 (looking up, three-point). Each uses the Example city layout.

## Interactions in detail
- Rendering: SVG or canvas at real pixels, redrawn on every control change (target 60 fps at 1920x1080 with 20 buildings). Faces are sorted far to near (painter's order by face center depth) and back faces culled; the ground grid is clipped at the horizon.
- Points behind the eye (z under 1 m) are clipped; buildings partly behind the eye are cut at the near plane. A building can't be dragged closer than 15 m.
- Eye height above a building's top shows its roof; below it, the horizon line crosses the building at eye height. The readout names how many buildings the horizon crosses.
- Windows: each face is divided into floors and bays in perspective (projective division, so rows get closer together as they recede); off when a face is under 40 px wide.
- Ink snapping uses the angle from the stroke start to each VP; with VPs off the page the snap still works (lines aim off the page). Strokes are stored in world-free screen space with the camera they were drawn under; changing the camera in Build asks "Your ink was drawn for the old camera. Keep it, or clear it?"
- Sliders show their value in the readout font; keyboard arrows step them (Eye height in the labeled stops with Page Up and Page Down).
- Motion off: slider changes jump instead of easing; nothing else changes.
- Sizes: stage and panel side by side down to 1000 px; the camera section stays at the top of the panel; under 900 px tall, Overlays fold into a row of toggles. In the 680x425 preview the panel shows only Camera; the stage keeps labels at 11 px or more. At 375 wide the stage sits on top and the panel scrolls below with Camera first.

## Look
- Kit `theme-912` base; accent (`--brand`) #6fd6e8 blueprint cyan. Scene: dusk sky from #1b2440 at the top to #f0a36b at the horizon, ground #1a1f2b with a grid at 10% white, buildings in three values of blue-gray (#9fb3c8 light, #6b7f96 mid, #3c4a5c dark) shifted warm by the sun dial; vanishing points #ff6b5a with labels; guides cyan at 60%.
- Contrast: brand on panel 10.3:1; brand on section 9.7:1; brand-ink on brand 11.0:1; label ink on the top sky 13.0:1; VP labels sit on a dark chip.
- Different from vanishing-point-studio (cream paper, charcoal, red and blue), gallery-critique (pink), virtual-gallery (lime).

## Art
None: the city, sky, guides and plan are drawn in code.

## Voice
Bank voice: `casual-peer` (a teen who draws cities in a sketchbook; different from every tool in this group; vanishing-point-studio has no voice). Style: relaxed, specific.
- welcomeBuild (how): "Drag the eye height slider and watch the horizon stay with your eyes."
- turnHow (how, after the first eye-height change): "Now try Turn. The two red dots are your vanishing points."
- guidesHow (how, the first time Guides is turned on): "Every edge runs to one of the two dots. That's two-point perspective."
- offPage (event, the first time in a session a VP goes off the page; stale if it comes back before it plays): "One vanishing point just went off the page. The lines still aim at it."
- welcomeInk (how): "Drag to draw. Your lines snap to the vanishing points."
- tiltHow (how, first nonzero Tilt): "Tilting makes the up-and-down edges meet too. That's a third vanishing point."
- welcomeFind (how): "Move the eye height, turn and lens until your city matches the outline."
- matched (event): "Matched." followed by the target's settings.

## Family engine
perspective. This spec holds the full description; vanishing-point-studio (6-8, built first) is the reference for the look of guides and snapping and moves onto the engine when next touched. Near-and-far uses the same projection (see its spec).
`kit/perspective.js`:
- `camera({W, H, lensMm, eye, horizonY, pitch})` returns f and helpers.
- `project(cam, [x, y, z])` and `ground(cam, u, v)` (screen to ground point, for dragging; null above the horizon).
- `vps(cam, turn)` returns VP L, VP R (and VP 3 with pitch), allowing off-page values.
- `box(cam, {x, z, w, d, h, turn})` returns visible faces, each with screen points, normal, depth and its VP, in draw order.
- `divide(face, rows, cols)` divides a face in perspective (projective division).
- `snap(cam, start, end, targets, maxDeg)` returns the snapped end and which target.
- `shade(normal, sunAngle)` returns light, mid or dark.
vanishing-point-studio feeds: one VP (turn 0, fronts on the picture plane). This tool feeds: turn, buildings, tilt.

## Sources
- NCAS Visual Arts VA:Cr2, VA:Cr3: https://www.nationalartsstandards.org/
- Horizon at eye level; two-point construction; the 90 degree angle between the sight lines to the two vanishing points; three-point when the picture plane tilts: Joseph D'Amelio, Perspective Drawing Handbook (Dover, 2004); and "Perspective (graphical)", Wikipedia, https://en.wikipedia.org/wiki/Perspective_(graphical)
- Pinhole projection and vanishing point formulas: Richard Szeliski, Computer Vision: Algorithms and Applications, 2nd ed. (2022), section 2.1, https://szeliski.org/Book/
- Field of view from focal length on a 36 mm wide sensor: "Angle of view (photography)", Wikipedia, https://en.wikipedia.org/wiki/Angle_of_view_(photography)
- Floor height 3.5 m is this tool's setting for a typical office floor (stated as a setting, not a fact).

## Done when
1. The horizon stays at eye level for every Eye height and crosses every building at the eye's real height (check two buildings in Python at 60 m).
2. VP positions match the worked check at W = 1200 for 35 mm at 30 and 45 degrees, and for 85 mm at 45.
3. Guides from every visible corner meet at the shown VPs within 1 px.
4. Tilt 15 shows a third VP at f / tan 15 from center, and verticals meet there.
5. Ink lines snap to the right target and say which; Save picture gives a PNG without guides; the drawing survives a reload; Clear drawing empties it.
6. Find the Camera: each of the six targets can be matched to 92% or more with its listed settings.
7. Camera sliders and the stage are visible without scrolling at every STANDARDS.md size; 60 fps with 20 buildings at 1920x1080.
8. How lines once in five slider moves in a row; matched every time.

## Refine changes
Round 1 (2026-10-28), from refine.md. These replace the matching lines above where they differ.
- **Check my drawing** (Ink, VA:Cr3 revise step). A `Check my drawing` button turns Snap off and puts the Line pen on. The student draws building edges by eye; any line whose direction misses every vanishing point it could aim at (VP L, VP R, VP 3 with Tilt, the upright when level, a level line) by more than 2.5 degrees, measured from the line's midpoint, turns red, and a count shows ("2 lines miss their vanishing point."). The student fixes them (erase and redraw, or Undo). When every line hits (after at least one red line, or after three lines drawn), one reflection opens: "What did you change to make your lines hit their vanishing points?" with a short text box and `Done`. Done keeps the note with the drawing (this browser only), turns the check off and gives Snap back as it was. The how line plays once ("Snap is off now..."), then "Fix the red lines..." and "Every line hits its point now...".
- **Stand-back and horizon.** The eye stands back 120 m + 0.6 m per meter above 1.6 m (120 m at the sidewalk, 209 m at Drone, 359 m at Helicopter), so Drone looks about 36 degrees down and Helicopter about 48 degrees down. `Horizon on page` runs from 600% above the page to 80% down it and has an `Auto` button (on by default): Auto keeps the block's near ground low on the stage, so at Drone and Helicopter the horizon goes above the page and the city with its street grid fills the stage. Dragging the slider turns Auto off; an eye height stop turns it back on. The ground is a street grid (outer blocks and 7 by 5 lots).
- **Find the Camera.** Targets (eye, turn, lens, tilt): 40 m, 30, 24 mm; 3 m, 45, 35 mm; 100 m, 20, 24 mm; 20 m, 55, 35 mm; 300 m, 40, 35 mm; 2.5 m, 15, 24 mm, tilt 15. None is an eye height stop, and stops do not snap in Find. The match is per setting: eye 1 - |ln(e/e*)| / ln 10, turn 1 - |difference| / 40 degrees, lens 1, 0.5, 0.2, 0 by stops apart, tilt 1 - |difference| / 30 (only when either tilts); the meter shows their mean and rises toward the answer one setting at a time. Matched means every setting at 95% or more. After each missed Check camera (round 2; the meter is not live) a reading hint names the setting furthest off (eye height, turn, lens, tilt) and offers `Extend outline edges`, which draws the outline's edges out to its own horizon and vanishing points. The outline is amber over a dark halo, on top of Guides and Windows (framing: see round 2). Found targets are marked; after target 6, Next says `Start over` and sets Tilt back to level.
- **Other.** The readouts explain "1 focal length = lens / 36 x page width" and, with Tilt, the horizon shift. The "you see bottoms" fact shows only when undersides are on screen. With Tilt, upright strokes snap to VP 3 (no screen vertical). Build gives one composition goal after the first building is moved or added. New buildings go to a free lot that the camera can see. "Saved on this device only" shows in every mode. Done when 6 now reads: each target can be matched (every setting at 95% or more) with its listed settings, and no eye height stop matches any target.

Round 2 (2026-10-28), from the exit check.
- **Check camera** (Find). The meter is no longer live. The student reads the outline, sets the camera and presses
  `Check camera` (in the panel and on the stage chip beside the target number). Each press is one try. Only then do the
  meter and a score for each setting show (Eye height, Turn, Lens, Tilt, a check mark at 95% or more); any later camera
  change marks them "Last check" and asks for a new check. Matched still needs every setting at 95% or more. A check
  that misses says how many settings are off and names the first one in reading order; the hint becomes that setting's
  reading hint (where the outline's horizon crosses the buildings, where its edges meet, how far apart its VPs are, how
  its uprights lean) and `Extend outline edges` is offered. The Check step is voiced once ("When you think your camera
  matches, press Check camera..."), on the first camera change in Find; the Find welcome names it too.
- **Outlines whole at every size.** Find shrinks the picture by one uniform scale per target (the same as a shorter
  focal length for both cameras, so every angle, VP and match is unchanged and the lens is still compared in mm) so the
  outline fits under the target chip, then centers it. The focal-length readout says when the picture is shrunk. Every
  target fits whole at every STANDARDS size and at 375 wide; no target was made shorter.
- **Off-page VPs.** An off-page VP's dot and arrow sit at the page edge where its direction leaves the page (above the
  page: the top edge near its own u), with labels kept clear of each other and of the horizon chip. turnHow now reads
  "Now try Turn. The red dots are your two vanishing points. An arrow at the edge points to one off the page."
- **Check my drawing** runs its count on every check: lines that all hit open the reflection after three lines, a line
  erased without being drawn again is reported as missing (and closes the reflection), stale messages clear, and the
  reflection's note and Done scroll into view when they open.

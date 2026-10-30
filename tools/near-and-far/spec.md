# Near and Far
Renamed from: Depth Detective

## One idea
Every picture tells the eye how far away each thing is, and the Side View shows exactly what yours told: a cow drawn big but high up shows up as a giant cow floating far away, until size, place, overlap and fading all agree.

## Not like
- vanishing-point-studio (6-8, studio): draws boxes and roads with ruler lines to one vanishing point. Here there are no lines and no drawing: you move, size and stack ready-made cut-outs, and the Side View (a cross-section from the side) checks the depth your cues tell.
- city-skyline-studio (9-12, studio): a camera and two vanishing points over buildings. Here the camera never moves; only the objects do, and the cues are the four a grade 3 to 5 artist uses (place, size, overlap, fade).
- paint-mixer (3-5, lab): color mixing. Fading here is a three-step cue (crisp, soft, misty), not a color lesson.
- art-style-match (3-5, cards, same group): reads styles from real paintings. Here the one real artwork (Hogarth) is a hunt for depth mistakes, not a style.
- frame-it (6-8, lab): moves a camera over a scene for composition. Here the camera is fixed and the objects move.
- The 'Detective' title clash is solved by the rename; the topic line carries the topic.

## Who and how
- Grade 3-5, visual arts, module "Perspective and Space (Visual Arts)": overlap, size and horizon lines.
- Topic line: perspective and space in art
- Driver: students or teacher (students on laptops, or a teacher on a projector asking the class "bigger or smaller?"). 10 to 25 minutes.
- Standards: NCAS VA:Cr2 (organize and develop artistic ideas and work), with VA:Re7 for the Hogarth mode (perceive and analyze artwork).

## Screens and modes
Header: title, topic line, `Read`, `Motion`, `Sound` (kit). Mode buttons (`.seg`): `Valley` (explore, the default), `Puzzles`, `Mixed-Up Picture`.

**Valley (explore first).** Focus: the postcard, the biggest, central thing; the Side View under it is the check. The stage is a landscape postcard: the painted valley (Art) with sky, a horizon line across the postcard at 42% of its height, a green ground that runs to the horizon, a lake on the right third. The postcard always keeps a 16:10 shape (fitted to the stage at real pixels, any spare room filled with the sky and ground colors in Look), so the same place and size mean the same distance at every screen size. Below the postcard, the Side View strip (about 22% of stage height): the same scene seen from the side, eye at the left, ground running right, a log distance scale with ticks `5 m`, `20 m`, `100 m`, `500 m`.
- Panel: a shelf of cut-out objects (Content "Objects"), each a button with its picture and name. Tap one to drop it into the postcard at a middle distance; drag it in from the shelf on a pointer device.
- On the postcard: every object has a grab area at least 44 px square, centered on it, even when the object is drawn smaller (a far cow is a few pixels tall). Drag an object to move it (its bottom edge is its place on the ground). A round corner handle resizes it (keeps its shape). Two small buttons on the selected object: `Front` and `Back` (overlap order). A `Fade` button cycles crisp, soft, misty (the object gets paler and bluer and loses edge detail).
- `Remove` (on the selected object), `Clear valley` (panel), `Show horizon` toggle (the horizon is a dashed line with the label "horizon: your eye level"; on by default).
- The Side View updates live: each object is drawn at its real height at the distance its cues tell (Interactions). An object whose cues agree is solid with a check and its distance ("cow, 30 m"). An object whose size and place disagree shows as two faint ghosts joined by a dashed bracket with words: "size says 30 m, place says 120 m". An overlap that disagrees shows both objects with a crossed sightline icon and "covers it, but is farther".
- Panel readout, the selected object: "Place says 40 m. Size says 40 m. Solid." or the disagreement in words.

**Puzzles.** Focus: the postcard, with the goals beside it. Eight postcards, harder each time (Content "Puzzles"). Top of the panel: the puzzle's brief (two or three short sentences), a step list of its goals, each with a tick when met. Same controls as Valley, but only the puzzle's objects (no shelf). `Check` is not needed: goals tick live. When every goal is met: the postcard frame turns gold, a short line ("It looks deep now."), and `Next postcard`. Buttons: `Previous`, `Next postcard` (always available; puzzles are not locked), `Start over` (this puzzle), `Hint` (one hint per goal, from Content).
- A puzzle opens "flat": its objects in a row, all the same size, all on one line, all crisp. That is the before; a `Before and after` button appears when solved and wipes between the flat start and the student's finished postcard.

**Mixed-Up Picture.** Focus: the print, filling the stage. William Hogarth's 1754 print *Satire on False Perspective* (The Met), full stage. The caption under it in plain words: "Hogarth drew this on purpose to be full of depth mistakes." Panel: a counter "Found 0 of 8" and the eight cue icons (size, overlap, place). Tap a spot on the print: if it is one of the eight finds (Content), the view zooms in on it (the art-passport zoom: 2.4 times, clamped, dimmed ring), names the mistake and the cue it breaks, and adds it to the list. A tap elsewhere: "Look again. Try something that is too big or too small." `Whole picture` (or Escape) zooms out. `Show me one` zooms to the next unfound mistake. No timer, no score beyond the count.

## Content
**Camera (the same for every postcard).** Eye height 1.5 m above the ground. Horizon at 42% of the postcard height from the top. Focal length f = 0.9 times the postcard width in pixels. The postcard is always 16:10, and positions are stored as fractions of it, so puzzles work the same at every size.

**Objects** (scene heights, stated on screen as "In this valley, a barn is 8 m tall"; these are the scene's settings, not world facts):
| id | name | height | elevation | notes |
|---|---|---|---|---|
| pine | pine tree | 12 m | 0 | |
| oak | round tree | 9 m | 0 | |
| barn | barn | 8 m | 0 | |
| mill | windmill | 16 m | 0 | |
| hay | haystack | 2.5 m | 0 | |
| cow | cow | 1.5 m | 0 | as tall as your eyes |
| fox | fox | 0.6 m | 0 | |
| post | fence post | 1.5 m | 0 | as tall as your eyes |
| boat | sailboat | 6 m | 0 | only on the lake |
| balloon | hot air balloon | 18 m | 40 m (basket bottom) | flies above the horizon |
| hill | far hills | 300 m | 0 | a wide band, distance only from place and fade |

**Puzzles** (brief, objects, goals; "solid" means place and size agree):
1. Two Trees. "One pine is near you. One pine is far away." Objects: 2 pines. Goals: both solid; one closer than 40 m, one farther than 100 m. Hint: "Far things are smaller and closer to the horizon."
2. Fence Line. "Make the fence run back into the distance." Objects: 5 posts. Goals: all solid; each post farther than the one to its left. Hint: "Each post is as tall as your eyes. Its top touches the horizon." This is the puzzle's aha: once solid, every post top sits on the horizon line.
3. Who Is in Front. "The haystack is in front of the barn." Objects: barn, haystack. Goals: both solid; they overlap; the haystack covers the barn and is closer. Hint: "Tap the haystack, then Front."
4. Cow Parade. "Three cows: one near, one in the middle, one far." Objects: 3 cows. Goals: all solid; distances under 15 m, 30 to 80 m, over 150 m. Hint: "The cow's back touches the horizon wherever she stands."
5. Barnyard. "The fox is closest. The windmill is farthest. The round tree is in front of the barn." Objects: fox, oak, barn, windmill. Goals: all solid; the order; the oak overlaps and covers the barn.
6. Misty Hills. "The hills are far. The pine is near. Make the far things misty." Objects: hill, pine, barn. Goals: all solid (the hill counts as solid when its top band is within 2% of the horizon); fade matches distance: crisp under 40 m, soft 40 to 150 m, misty beyond 150 m. Hint: "Tap Fade until the hills look misty."
7. On the Lake. "A sailboat is far out on the lake. Another is near the shore." Objects: 2 boats. Goals: both solid, both on the lake, one under 30 m, one over 150 m.
8. Up in the Air. "All the balloons fly at the same height. Put one near and one far." Objects: 3 balloons. Goals: all solid; one closer than 250 m, one farther than 600 m (a balloon is only fully on stage from about 200 m; Interactions). Hint: "Up in the sky, far things are lower, closer to the horizon." The aha: above the horizon, farther means lower.

**Mixed-Up Picture finds** (all from the print; the list of its errors is in Sources). Each: the zoom spot (the builder places x, y after fetching the image), the line shown and spoken, and the cue:
1. "These sheep get bigger as they go farther away." (size)
2. "This bird is huge next to the tree it sits on." (size)
3. "The man on the far hill is taller than the trees." (size)
4. "The swan is bigger than the men in the boat." (size)
5. "The far trees are in front of the near sign." (overlap)
6. "The near fisherman's line goes behind the far fisherman's line." (overlap)
7. "The woman in a near window holds a candle up to a man on a far hill." (place)
8. "You can see the top and the bottom of this barrel at once." (place)
Teacher note on screen under the counter: "Hogarth made this in 1754 for a book that taught perspective."

## Interactions in detail
- Depth from the cues (postcard px; y down; yh horizon; f focal; e = 1.5 m; z elevation; R height): an object whose bottom edge is at yb and drawn height h has place distance dp = f(e - z)/(yb - yh) and size distance ds = fR/h. Solid when max(dp, ds)/min(dp, ds) is 1.25 or less; its distance is the mean. Worked check at a 1000 x 625 postcard (yh = 262.5, f = 900): a cow 30 m away is 45 px tall with its bottom at 307.5; a barn 120 m away is 60 px tall with its bottom at 273.75; a balloon 100 m away would be 162 px tall with its basket bottom at 262.5 - 346.5, off the top, so a balloon is first fully on the postcard at about 194 m (81 px tall, bottom at 89.25) and at 600 m is 27 px tall with its bottom at 204.75. The builder recomputes these in Python and puts them in the test.
- A ground object cannot sit above the horizon (it clamps 1 px below and the readout says "That is past the horizon."). A balloon cannot go below the horizon. A boat snaps to the lake area (a polygon the builder traces on the painted lake, from the horizon down to at least 60% of the postcard height on the right third). Distance range 4 m to 1000 m; beyond that the object clamps and the readout says "Too far to see." Drawn size 2 px to 90% of postcard height (a smaller object is "Too far to see"); an object may run off the top edge and is clipped there.
- Overlap: two objects overlap when their drawn boxes intersect by 10% of the smaller box or more. The one drawn on top must be the closer (by mean distance); otherwise both get the overlap mark. Objects that do not overlap carry no overlap claim.
- Fade: crisp (full color), soft (60% toward the sky color, edges softened), misty (85% toward the sky color, no detail). Fade is only checked in puzzle 6 and in the Valley readout ("Misty, but only 20 m away: fade says far.").
- Side View: a log scale from 4 m to 1000 m. Sightlines from the eye to each solid object's top and bottom are thin lines; with Motion off nothing animates, otherwise objects slide to their new place in 200 ms.
- Nothing waits on a motion: a drag or tap during a Side View slide, a zoom (0.9 s) or the Before and after wipe acts at once (the slide jumps to its end, the zoom goes to the new spot, the wipe stops where it is) and the old line stops.
- Snap help: while dragging, if the object is within 4% of solid, a faint target outline shows where it would be solid at this size (grade 3 support); the readout says "Almost. A little higher." It never snaps by itself.
- Keyboard: Tab through objects (panel before the many postcard objects); arrows move 1% (Shift 5%); `+` and `-` resize 5%; `F` front, `B` back; `M` fade; Delete removes (Valley only).
- Puzzle state is per puzzle for the session; solved puzzles are remembered on this device (localStorage `near-and-far-solved`), cleared by `Clear progress` under the puzzle list. Valley is saved the same way (`near-and-far-valley`) and cleared by `Clear valley`.
- Reset: `Start over` restores the flat row. Changing mode calls `V.hush()`.
- Sizes: the postcard and Side View are laid out at real pixels per box; in short landscape boxes the Side View shrinks to 16% and the panel goes compact beside the stage (brief, goals, Hint, Next). At 375 wide the panel stacks under the stage with the brief first.

## Look
- Accent (`--brand`, header and primary buttons) #2e6440 valley green. Paper #f3f6ee (pale meadow), ink #1f2a1c, muted #55614f. Scene: sky gradient #bfe0f2 to #e9f4fa at the horizon, near ground #8cc274 to far ground #b9d4a8, lake #7fb6d4, haze color #d9e6ee. Solid check and gold frame #e0b43a with a check icon and words (never color alone).
- The painted valley keeps to this palette (sky blue to pale at the horizon, meadow greens, a blue lake); the code colors above fill any room around the 16:10 postcard and are the haze target for Fade.
- Contrast: white on brand 6.97:1; brand on paper 6.38:1; ink on paper 13.67:1; muted on paper 5.99:1; ink on sky #bfe0f2 10.78:1 (labels on the postcard sit on a white chip, ink on white 14.93:1). All AA.
- Different from neighbors: paint-mixer purple, art-passport blue, vanishing-point-studio charcoal and red, art-style-match magenta.

## Art
Local FLUX (`scripts/localart.py`), one session, no people. Style line: "soft painted storybook look, flat light, gentle shading, for a grade 4 art lesson."
- valley: "a wide empty green valley under a soft blue sky, a flat meadow running back to a low straight horizon with only a thin line of far blue hills at it, a calm blue lake on the right third stretching from the horizon down toward the viewer, soft painted storybook look, flat light"; 16:10; cutout no; people no; the postcard background in all three postcard modes. The builder checks the horizon sits at 42% of the height (crops or shifts the image to put it there) and traces the lake polygon.
- Postcard objects (cutouts, one style, each "<item>, full object, side or front view, soft painted storybook look, flat light, gentle shading, plain white background"; people no; each drawn at the size the camera gives it and faded in code for Fade):
  - pine: a single tall green pine tree standing straight, from roots to tip; 3:4.
  - oak: a single round leafy green oak tree with a short trunk; 1:1.
  - barn: a red wooden barn seen from the front at a slight angle, with blank walls; 4:3.
  - mill: a white farm windmill with four sails on a wooden tower; 3:4.
  - hay: one round golden haystack; 1:1.
  - cow: one brown and white cow standing side-on; 4:3.
  - fox: one red fox standing side-on; 4:3.
  - post: one wooden fence post with a short rail stub; 3:4.
  - boat: one small white sailboat with a white sail, side view; 3:4.
  - balloon: one striped hot air balloon in red and yellow with a wicker basket; 3:4.
  - hills: a wide band of gentle rolling hills, full width, top edge cut out; 4:1.
- Real artwork: Satire on False Perspective, Luke Sullivan after William Hogarth, 1754, The Met 365241 (Open Access, public domain), long side 1000 px, about 60 KB. People in the print are fine (not generated).
- 12 generated images, none with people. Drawn in code: the Side View (a diagram), the horizon line, ghosts, brackets, sightlines, handles, the target outline, the cue icons and every label.

## Voice
Bank voice: `gravel-ranger` (an old park ranger looking out over the valley; different from art-passport's knowing-guide and from every other tool in this group). Style: warm and unhurried, a guide on a lookout. `Curio.voice` with `scope: () => state.mode + ':' + state.puzzle`.
Lines (how = once, then hint only; event = every time, dropped when stale):
- welcomeValley (how; entering Valley with an empty postcard; stale when an object lands): "Welcome to the lookout. Tap a picture on the shelf to put it in the valley."
- dragHow (how; after the first object lands; stale when it is dragged): "Drag it to move it. Pull the round corner to make it bigger or smaller."
- sideHow (how; after the first drag ends; stale on the next drag): "Look at the side view. It shows how far away your picture says it is."
- ghost (event; when a drag or resize ends with size and place apart; stale when that object becomes solid or is deselected): "Size and place don't agree yet. Drag it up or down, or pull the round corner."
- solid (event; the first time each object becomes solid in a session; stale on a new drag): "Solid. Now they agree."
- welcomePuzzles (how; entering Puzzles; stale when an object is dragged): "Read the postcard's note. Drag and size things until every goal has a tick."
- Each puzzle brief (how; when that puzzle first opens; stale when the puzzle is left): the briefs in Content.
- frontHow (how; puzzle 3, the first time the two overlap with the barn on top; stale when Front or Back is tapped): "Tap the haystack, then tap Front."
- fadeHow (how; puzzle 6, the first time the hills are solid but not misty; stale when Fade is tapped): "Tap the hills, then tap Fade until they look misty."
- solved (event; stale when the student leaves the puzzle): "It looks deep now. Tap Next postcard when you're ready."
- welcomeMixed (how; entering Mixed-Up Picture; stale on the first tap on the print): "Hogarth drew this picture full of mistakes on purpose. Tap something that looks wrong."
- miss (event; stale on the next tap): "Look again. Try something that is too big or too small."
- each find's line (event; stale on the next tap): the eight lines in Content.
- allFound (event; stale when the mode changes): "You found all eight. Every one breaks a rule of near and far."

## Family engine
None (no family). It uses the same ground-plane camera formula as the perspective engine described in city-skyline-studio's spec (bottom of an object at yh + f(e - z)/d), so a builder may share that one function. The Mixed-Up Picture zoom reuses art-passport's `zoomTo` behavior (copied, not a family import).

## Sources
- NCAS Visual Arts standards, VA:Cr2 and VA:Re7: https://www.nationalartsstandards.org/
- Satire on False Perspective, Luke Sullivan after William Hogarth, February 1754, etching and engraving, The Met 365241: https://www.metmuseum.org/art/collection/search/365241
- The list of the print's deliberate errors (sheep, bird, man on the hill, swan, sign and trees, fishing lines, candle, barrel): "Satire on False Perspective", Wikipedia, https://en.wikipedia.org/wiki/Satire_on_False_Perspective ; the builder checks each against the image before placing its spot.
- Depth cues for artists (overlap, size, placement, atmospheric perspective): Gene Mittler and Rosalind Ragans, ArtTalk (Glencoe), chapter on space; and Getty "Elements of Art: Space" teaching resource, https://www.getty.edu/education/teachers/classroom_resources/
- Horizon line is the viewer's eye level, objects as tall as the eye touch it: Joseph D'Amelio, Perspective Drawing Handbook (Dover, 2004), ch. 2.
- Object heights are the scene's own settings, stated as such on screen.
- Checks run (Python, 2026-10-29), at a 1000 x 625 postcard (horizon 262.5, f = 900): cow at 30 m is 45 px with its bottom at 307.5; barn at 120 m is 60 px, bottom 273.75; balloon at 100 m is 162 px with its bottom at -84 (off the top); a balloon's top reaches the postcard edge at 900 x 56.5 / 262.5 = 193.7 m (about 200 m as stated), at 200 m it is 81 px with its bottom at 89.25, at 600 m 27 px with its bottom at 204.75. Posts and cows (1.5 m, eye height) have their tops on the horizon at 10, 25, 60 and 200 m. Fixes from the checks: (1) Puzzle 1's near pine had to be closer than 20 m, but a 12 m pine is 90% of the postcard height at 19.2 m, leaving a 0.8 m window and the tree 210 px off the top; the goal is now closer than 40 m (at 40 m the pine is 43% of the height and fits). (2) The old 6 px minimum size made Puzzle 4's far cow (over 150 m, 3.4 px on a 375 px postcard) impossible on phones; the minimum is now 2 px, and grab areas are 44 px whatever the drawn size. (3) Distances depended on the stage's shape (f from the width, horizon from the height), so goals in meters changed between sizes; the postcard is now always 16:10. Boats: a boat at 150 m has its bottom at 43.4% of the height and at 30 m at 49.2%, so the lake must reach from the horizon to below about 50% (the spec asks for 60%). Contrast ratios in Look recomputed with the WCAG 2.1 formula.

## Done when
1. In Valley, a cow dragged so its back meets the horizon reads Solid at any distance; resizing it without moving shows the ghost pair with both distances in words.
2. Puzzle 2: once all five posts are solid, every post top lies on the horizon within 2 px (check in Python at 1366x768).
3. Puzzle 3 fails while the barn covers the haystack and passes after `Front`; the overlap mark has words, not just color.
4. Puzzle 8: a balloon moved toward the horizon gets farther in the Side View, and the worked numbers in "Interactions" match the build at 1000 x 625.
5. Mixed-Up Picture: all eight finds zoom to the right place on the print; `Show me one` walks the rest; Escape returns to the whole picture.
6. Each how line is spoken once in a run of five drags in a row; solved and finds are spoken every time.
7. Main controls (object handles, Front, Back, Fade, Next postcard) are visible without scrolling at every size in STANDARDS.md, and postcard objects are at least 44 px to grab.
8. Keyboard alone can solve puzzle 1.
9. `Clear progress` and `Clear valley` empty localStorage; nothing else is stored.
10. Focus: at 1366x768, 680x425 and 375 wide the postcard is the largest thing on the stage, always 16:10, with the painted valley's horizon on the 42% line.
11. Tap while it plays: a drag during a Side View slide, a tap during a zoom and a tap during the Before and after wipe each act at once, and no stale line plays after.

## Open questions
- Should Near and Far join the perspective family with vanishing-point-studio and city-skyline-studio (it uses the same camera formula), or stay on its own?

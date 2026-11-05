# city-skyline-studio: Play lens (2026-10-28)

Played cold, twice: as a grade 10 student alone at home on a 1366x768 laptop (built and inked a city, then all six
Find the Camera targets at a real pace, held clicks, real slider drags and arrow keys, about 0.25 to 3 s between
actions), and as a teacher projecting at 1920x1080. Bundle: `CURIO_DRAFT=1`, 125 KB. Own headless Chrome on port
9660 with a persistent tab (state carried across steps), iframe host on 9661 for 375 wide. Frames in
`C:\Users\Cory\AppData\Local\Temp\claude\S--\98b8b046-f7f2-48d0-a719-c61ce01237be\scratchpad\lens-css-play\out`
(01 to 55, plus `sz-*` for 1920x1080, 1280x720, 1000x625, 800x500, 680x425, 760x900 and 375). No console errors or
exceptions in any step.

Counts: **0 blockers, 8 should fix, 10 polish, 4 nits.**

## What works

- The core idea lands. Dragging Eye height from Sidewalk to Rooftop is a real "oh" moment (frames 01, 03): the
  horizon label follows, "Horizon crosses 5 of 9 buildings" updates, and at 35 mm with Windows on the sidewalk view
  (frame 21, 55) looks like a real street.
- Ink feels like a drafting tool: lines snap with a live "to VP R" chip at the pen tip (frame 28z), the panel says
  "Last line: to VP L / vertical / free", hatch aims at the face's VP, fill and Undo/Redo behave, and the drawing and
  city survive a reload. Privacy line is on screen.
- Find targets 2, 3 and 5 are good puzzles: pick the stop, pick the lens, then the meter climbs steadily as Turn
  closes in (target 2: 43, 44, 47 ... 84, 92, 100 from 45 down to 30 degrees). Matched is spoken once with the
  settings, then "Press Next target" is spoken and Next target appears on the stage too. Target 6 tells you to use
  Tilt, and 24 mm, turn 15, tilt 15 reaches 100%.
- Voice order was right in every run: welcomeBuild, turnHow after the first eye move, guidesNext, guidesHow, buildNext,
  tiltHow, welcomeInk, inkMore, pen how-tos once each, inkAsk, welcomeFind, matched + settings, findNext. Read logged as
  read. The offCity line was dropped when its moment passed.

## Findings

### Should fix

1. **Clear city's confirm press runs away** (src.html:965-966, Build, 1366x768; frame 14). The first press changes the
   label to "Sure? Clear city"; the wider label wraps the button onto a new row, below the panel's fold. The student's
   second press lands on empty panel and the 3 s arm times out; I needed two tries and a scroll. Keep the button the
   same width (fixed width, or "Sure?" in a tooltip/second button beside it). **general**
2. **The high stops fall flat** (src.html:240 standoff; Build; frames 04, 07, 08). At Helicopter with the default
   24 mm lens the whole city is a ~50 px speck; even at 85 mm with Horizon on page at 20% it is about 150 px tall in a
   1006 px stage. The ground there is two thin crossed strips of street lines on an empty dark plain, which reads as a
   glitch. The spec's promise "lifting the eye ... to a helicopter redraws the whole skyline" is the reason to touch
   the slider, and its top end is the least rewarding view in the tool. Options: a gentler standoff above Rooftop, or
   a lens or horizon that follows the stop, plus ground drawn beyond the lot grid. (The standoff itself is already on
   Cory's list in handoff.md; this is the student-side cost.) **family:perspective**
3. **Tilt up in Build gets "Your city is off the page"** (src.html:620-632; Build at Sidewalk, 35 mm, tilt 17; frame
   22). Looking up is what Tilt is for; the buildings fill the whole stage, yet the hint and the stage chip say "your
   city is below the page. Move Horizon on page, or pick a wider lens." Words don't match the state (POLISH,
   Consistency), and they push the student to undo the move. Count a building as seen when any part of it is on the
   page, or skip the check while Tilt is not 0. Same frame: the "horizon = eye level, 1.6 m (below the page)" label
   sits under the "VP L (off the page)" chip at the bottom left (frame 22z); stack or offset them. **family:perspective**
4. **Find starts with street-level targets cropped and buried** (src.html:314 `findCam ... hor: 35`; Find; frames 31,
   32, 42). At horizon 35% the tops of the street-level targets (1, 4, 6) run off the top of the stage and the bottom
   60% is empty ground, so there is no skyline outline to read, only a forest of vertical dashes. Guides and Windows
   carry over from Build, and the target's white dashed outline is then lost among cyan dashed guides and the white
   dashed horizon (frame 31). Start Find with the horizon low enough to show the targets' tops (or per target), and
   hide or quiet Guides and Windows in Find (or draw the target in a style nothing else uses). **family:perspective**
5. **The match meter has false peaks on street-level targets** (Find; turn swept with arrow keys). Target 1 (answer
   45): 0 to 20 degrees climbs 37, 42, 49, 51, 52%, then falls to 40% at 25 to 35, then 71% at 45. Target 4 (answer
   60): 47% at 35, down to 25% at 45, 39% at 50. Target 6: picking the right lens (85 to 24 mm) dropped the meter from
   40% to 19%. A student following the meter stops at the false peak and decides the tool is broken. Smooth the score
   (for example blend in VP position or edge-direction agreement) so it rises toward the answer from either side.
   **family:perspective**
6. **The whole panel jumps when the hint changes length** (wide layout, `#hint` above the panel sections; frames 23,
   26, 27). The hint is one, two or three lines; every control below moves about 23 px each time. Switching Ink pens
   moved the pen buttons up under the pointer (Fill to Erase: 320 to 297 px); the Tilt slider moved from y 443 to 466
   between two Build steps and my drag missed it. Reserve three lines for the hint (or let it overflow into a fixed
   box). **general**
7. **At 760x900 Horizon on page and Tilt are below the fold** (stack layout; frame sz-760x900-build; measured eye
   730-774, lenses 866-910, hor 910-954, tilt 954-998). Done when 7 asks for every camera slider without scrolling at
   every STANDARDS size; at 760 wide the header also wraps to two rows (Sound and Read alone on row 2), costing
   about 65 px. **general**
8. **A new building can land completely hidden** (src.html:918 addBuilding; Build at Rooftop, turn 45; frame 16).
   After Clear city I added Tower, Tower, Slab, Water tower, Stepped: the Stepped went to the lot straight behind the
   first tower, so tapping Stepped showed nothing new except a dashed selection outline through the tower. Prefer the
   free lot that is most visible from the current camera (or nearest the front). **family:perspective**

### Polish

1. **Windows can do nothing with no word why** (Build at Rooftop 24 mm; frame 19). Faces are under 40 px, so pressing
   Windows changes nothing. Better: the hint (silently) says "Windows show on bigger faces. Try a longer lens or a
   lower eye." **family:perspective**
2. **The first screen is a gray wall** (Build default, frames 01, 54). Sidewalk, 24 mm, horizon 60%: the near block
   covers the left half, every top is cut off, Windows are off and the bottom 37% is empty ground. Projected, it does
   not look like a skyline. Opening with Windows on and the horizon lower (about 80% at Sidewalk) would sell the tool
   in one glance. **family:perspective**
3. **No record of the six targets** (Find; frame 52). After target 6, Next target silently wraps to target 1 with
   Tilt still at 15, the target-1 hint does not mention Tilt, and nothing shows which targets were matched. A quiet
   "Found 6 of 6" or a tick per target fits 9-12; on wrap, either reset Tilt or say "This one is level: set Tilt to 0."
   **family:perspective**
4. **Empty city hint** (Build after Clear city; frame 15). The hint still says "Turn on Guides under Overlays..." and
   the readout says "0 of 0 buildings". Better: "Tap Tower, Block, Slab, Stepped or Water tower to add a building."
   **general**
5. **Keep it / Clear it is asked about ink you can't see** (Build after inking; frame 29). The ask appears in Build,
   where the ink is hidden, and the buttons wrap (Keep it beside the text, Clear it alone below). Show a small
   preview of the ink or ask on entering Ink; keep both buttons on one row. **family:perspective**
6. **"Add one from Buildings" points below the fold** (Build at 1366x768). buildNext names Buildings, which starts at
   y 840 in a 768 px window. Fine once you scroll, but a "Buildings below" cue or moving the palette up would help a
   solo student. **general**
7. **Selected building blends with Guides** (Build with Guides on; frame 13). The selection is a dashed cyan outline,
   the same look as the guides. Use a solid outline or a different color. **family:perspective**
8. **Fast erase swipes miss** (src.html:1197 eraseAt tests sampled points only). A coarse drag (about 30 px between
   samples) crossed the free line without erasing it; a dense one worked. A real flick on a trackpad can do the same.
   Test the segment between samples. **general**
9. **Small Find targets at Drone and Helicopter** (targets 3 and 5; frames 40, 45). The outline is about 130 px tall,
   so comparing by eye is hard and the meter does all the work. Same cause as should-fix 2. **family:perspective**
10. **680x425 preview, Find:** the "VP 3 (off the page)" chip sits half under the hint dock (frame
    sz-680x425-find). **general**

### Nits

1. Floors, Width and Depth look enabled when no building is selected (bright thumbs, no value). Dim them. **general**
2. "Tap a building to pick i" is cut off in the Selected box at 1920x1080 (frame 54). **general**
3. The Plan inset's "90°" label crowds the picture-plane line and the eye mark (frame 19z). **family:perspective**
4. Dragging a building past the lot grid's edge stops it silently, about 80 px short of the pointer (frame 18). A
   brief edge flash would explain it. **family:perspective**

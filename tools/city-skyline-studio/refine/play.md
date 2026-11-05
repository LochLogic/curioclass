# Play lens: city-skyline-studio (round 1)

Fresh and cold. Played twice: as a grade 9-12 student alone at home on a 1366x768 laptop, and as a teacher projecting
at 1920x1080. Bundle: `city-skyline-studio.html` (CURIO_DRAFT=1, as handed over). Frames are in
`C:\Users\Cory\AppData\Local\Temp\claude\912539a76ace91d0\c55c8920-4b50-4aa7-8632-31d061e89e76\scratchpad\refine\city-skyline-studio\play\`
(f1 Build extremes, f2 Ink, f3 Check my drawing, f4 Find the Camera, f5 voice walks as JSON, f6 empty states), plus the
shared audit frames in `audit-r1\`. Voice was walked with a real first tap and the kit's `V.log` (f5/w1-walk.json,
f5/w2-find.json).

**Counts: blockers 0, should fix 3, polish 6, nit 6.**

## Should fix

1. **Build, 1366x768: the Buildings section the hints name is below the fold, with no cue.** (general)
   The panel order is Camera, Overlays, Readouts, Buildings (src.html:253-257). At 1366x768 the panel ends at the
   Readouts heading; Tower, Block, Slab, Stepped, Water tower, Example city and Clear city all need a panel scroll.
   Three lines send the student there: `addFirst` ("Your city is empty. Tap Tower, Block... under Buildings"),
   `buildNext` ("...or add one from Buildings") and `composeGoal`. Seen: f6/e1-empty.png (empty city, hint names
   Buildings, nothing of Buildings on screen), f1/01..16 at 1366, audit "off screen at load" rows 21-27. A solo student
   who clears the city is told to tap something they cannot see. Better: put Readouts after Buildings (or fold Readouts
   to a one-line summary with a toggle), so the palette sits under Overlays at 1366x768; the fact tip (src.html:275)
   would then also come closer to view (see polish 1).

2. **Ink, Check my drawing passes on any three upright lines anywhere, then asks "What did you change?" when nothing
   was ever red.** (family:perspective)
   I turned the check on and drew three short vertical strokes in the empty street (keyboard cursor, Enter, ArrowDown
   x10, Enter). Result: "All 3 lines hit their vanishing points." and the reflection opened: "What did you change to make
   your lines hit their vanishing points?" Seen: f3/c4-three-hits-no-miss.png. The check only measures direction
   (src.html:2131: ready when no misses and either a red line was seen or three lines were drawn), so the cheap way
   through the revise step is three verticals or three level lines, none on a building edge. And when no line was ever
   red, the question assumes a fix that never happened: words do not match the state. Better: count only lines that
   are not upright or level (receding edges) toward the three, or require at least one receding line; and when nothing
   was red, ask a different question ("Which vanishing point did your slanted lines aim at?") or open nothing.

3. **Find the Camera: the per-setting scores let a student solve any target without reading the outline.** (general)
   After each Check camera the panel lists Eye height, Turn, Lens (and Tilt) as percents with check marks. Each score
   is a plain distance: turn 1 - |difference| / 40, eye 1 - |ln ratio| / ln 10. Target 1, eye only: 10 m gave 39%, 20 m
   69%, 80 m 69%; turn 20 and 40 both 75%, so the answer is 30. Two or three checks per setting pin each one, and the
   check marks say which are already right (f4/f2-miss "Eye height 39%, Turn ✓ 100%, Lens ✓ 100%", f3b, f3c). The
   reading hints are good, but the numbers make them optional. Better: after a missed check, show only which settings
   are off (no percent) and the reading hint for the first one; keep the meter for the overall match, or show coarse
   words ("close", "far") without direction-free exact distances.

## Polish

1. **The facts tip sits at the very bottom of the panel, out of view at 1366x768.** (general) `#tip` (src.html:275)
   changes with the state ("Where the horizon crosses a building, it marks your real eye height.", "Above the horizon
   you see bottoms", "Nearly one-point perspective") but is only seen after scrolling the whole panel (f1/15, f6/e2).
   These are the spec's "Facts shown on screen". Better: show the current fact under the hint, or as a small chip on
   the stage near the horizon label.

2. **760x900 and 375: a blank band under the hint pushes Overlays below the fold.** (general) The hint keeps a reserved
   height (src.html:106-107, `min-height: calc(4 * 1.45em)` when stacked) but holds one line, leaving about 90 px of
   empty panel (audit size-760x900.png, f4/f14-760.png). `guidesNext` says "Turn on Guides under Overlays", and at
   760x900 Overlays starts at 928 px. Better: let the stacked hint size to its text (keep the reserve only for the
   side-by-side layout), which brings Overlays above the fold at 760x900.

3. **Drone or Helicopter with an 85 mm lens: "Your city is off the page" while a building fills the stage.**
   (family:perspective) With Auto on, Drone + 85 mm shows one or two buildings filling the left of the stage, yet the
   hint and the stage chip say "Your city is off the page" and "your city is above the page" (f1/10-drone-85.png,
   f1/13-add-all.png, where a slab roof fills the stage). The test is "fewer than a third of the buildings show"
   (src.html:1199-1209), so the words overstate it, and the advice "Move Horizon on page" switches Auto off.
   Better: "Most of your city is off the page" and, while Auto is on, lead with "pick a wider lens".

4. **Find, after a match the big panel button is still Check camera.** (general) The stage chip swaps to Next target,
   but in the panel the wide primary button stays "Check camera" and Next target is the small button beside the target
   number (f4/f4-match.png, f7-last-match.png). The hint says "Press Next target". Better: after a match, the big
   button becomes Next target (Start over on target 6), like the chip.

5. **Find: the Build-only `offPage` line plays in Find before `findCheck`.** (family:perspective) In the Find walk
   (f5/w2-find.json) the first eye change in Find spoke "One vanishing point just went off the page. The lines still
   aim at it." at 10.4 s and pushed "When you think your camera matches, press Check camera..." to 14.8 s. Find starts
   at Turn 0, so a VP is "infinitely far" from the first frame; the line adds nothing to the Find task and delays the
   how-to the student needs. Better: keep `offPage` to Build.

6. **Projected at 1920x1080, the stage labels are small.** (general) The horizon label, VP L / VP R chips and "the
   outline's horizon" are about 11-12 px bold (audit size-1920x1080.png, f4/f15-1920.png). Fine on a laptop, hard to
   read from the back of a room. Better: scale stage label type with the stage width above about 1400 px (13-15 px at
   1920).

## Nit

1. **Water tower:** it is sized in "Floors" ("1. Water tower, 6 floors"), and its Width and Depth read "8 m" while the
   sliders' minimum is 10, so the thumbs sit at 10 (f6/e2-water.png; src.html:1781-1786). Say "Height" for the water
   tower, or let the sliders reach 8.
2. **Empty city readout:** "Horizon crosses 0 of 0 buildings" (f6/e1-empty). Hide the row or say "No buildings yet".
3. **Selection outline shows through nearer buildings.** The amber outline of the selected building is drawn on top
   of everything, so at the sidewalk it reads as a box floating on the front slab (f1/16-example-drag.png,
   f2/i11). A thinner or dashed line where it is hidden would read as "behind".
4. **Undo is off after a reload** although the strokes are back (f2/i5-fill.png: 3 strokes, Undo greyed). Either keep
   the undo list with the drawing or let Undo remove saved strokes.
5. **Fill on empty sky does nothing, silently** (f2/i5: tap at 800,300 in the sky, no fill, no message). A short
   "Tap a face of a building" status would help.
6. **`buildNext` is cut after 0.2 s** when a building is added just as it starts (f5/w1-walk.json: buildNext spoken
   40.8 s, composeGoal 41.0 s). Drop `buildNext` from the queue as soon as a building is added or moved, before it can
   start.

## What worked (checked, no finding)

- First screen at every size says what to do and names the control; the welcome is spoken once, then each next step
  (turnHow, guidesNext, guidesHow, buildNext, composeGoal, tiltHow) is spoken once and only updates the hint after
  (f5/w1-walk.json: five more eye moves, no repeat). Read speaks the current hint.
- Extremes hold up: Turn 0 and 90 ("VP R: infinitely far", the one-point fact), Tilt +25 and -25 (VP 3 above or
  below, labels clear), Horizon 600% above ("your city is above the page"), 80 floors at 80 m, 20 buildings, empty city
  (f1, f6).
- Ink: snapping labels the line ("horizontal", "vertical"), Hatch aims at the face's VP, the drawing survives a reload,
  Save picture gives a PNG without guides (f2/i10), and changing the camera in Build asks Keep it or Clear it (f2/i11).
  Clear city and Clear drawing take two presses ("Really clear?").
- Find: every target's outline sits whole under the chip at 1366, 1920, 1000, 760 and 680 (f4/f9 to f15); Extend
  outline edges draws the outline's own horizon and VPs, which makes the eye height easy to read (f4/f3-extend.png);
  matching lines the render up with the outline, which is a satisfying moment; Start over resets Tilt and says so.
- Motion off: the audit's calm run is clean.

## Audit pilot

**Confirmed on my own frames:**
- Build controls below the fold at 1366x768 (rows 21-27, "off screen at load"): confirmed, and it matters because the
  empty-city and buildNext hints name Buildings (should fix 1).
- 760x900 and 375: Overlays and Buildings below the fold: confirmed; the reserved hint height is the cause of most of it
  (polish 2).
- Find, "others moved 4-5 of 25" after Check camera: confirmed, the scores list opens and pushes Overlays down; all
  below the fold, harmless.

**Leads that were wrong, or right but not a problem:**
- Every `#cv` overlap with `#hint` (680x425, 800x500), `#fchipT`, `#fchipM`, `#checkCam2`, `#extendQuick`: by design.
  The hint docks over the stage top in the compact layout and the Find chip sits on the stage; no outline or label is
  covered (Find shrinks the outline under the chip).
- "choices cut short by a scroll panel" in Find (680x425, 800x500, 1366x768): the hint names Check camera and Extend
  outline edges, and both are on the stage chip, visible. The only gap is the chip's label "Extend" against the hint's
  "Extend outline edges" (the chip's aria-label and title say the full name); fine.
- "Welcome not heard" after a first tap on an eye stop, 50 mm, 85 mm or Guides: the tap queued its own line, so the
  welcome is skipped by rule, and the hint still shows the welcome until the eye moves, so Read gives it. Not a problem.
- "nothing changed" for `#cv` in Ink and Find and `#clearInk`: a tap without a drag draws nothing, Find's canvas has no
  tap action, and Clear drawing on an empty drawing has nothing to clear. Expected.

**What it missed:**
- The cheap pass in Check my drawing and its reflection question that assumes a fix (should fix 2).
- The per-setting scores that let Find be solved by trial (should fix 3).
- The "city off the page" wording at Drone + 85 mm (polish 3), the fact tip out of view (polish 1), the panel's primary
  button after a match (polish 4), `offPage` in Find (polish 5), projector label size (polish 6).
- A real first tap matters for its voice rows: my first walk without one logged every line as silent "early".

# city-skyline-studio: Teaching lens (Refine, 2026-10-28)

Cold read of spec.md, src.html, notes.md, art/prompts.json, voice/lines.json and kit/perspective.js. Bundled with
CURIO_DRAFT=1, driven with scripts/drive.py (port 9650, own profile). Frames and scripts are in the lens scratch folder
(out/: eye-1.6, eye-10, eye-60, eye-150, eye-400, eye-400-hor20, guides-tilt, plan, find-t2-start, find-t5-start,
find-t5-eye400, find-t6-matched, ink-default, turn-0, turn-45-lens, pic).

**Counts: 0 blockers, 4 should fix, 6 polish, 1 nit.**

## Numbers recomputed (Python, then in the app)

- Field of view 2 atan(18 / lens): 24 mm 73.74, 35 mm 54.43, 50 mm 39.60, 85 mm 23.91 degrees. Spec and readout agree.
- Worked check, W = 1200: 35 mm f = 1166.7 px; turn 45: VP L -566.7, VP R 1766.7; turn 30: VP L -73.6, VP R 2620.7;
  85 mm at 45: 5666.7 px apart (= 2f / sin 2t). All match the spec.
- In the app (1366x768, stage W = 1006): 35 mm f = 978.06; turn 30 VP L -61.68, VP R 2197.04, both on the horizon
  (v 411.6); turn 45 apart 1956.11 = 2f; 85 mm apart 4750.56 = 2f. Each equals the formula to 1e-12 px. Readout "2.00
  focal lengths" at 45 degrees and "2.31" at 30 degrees (2 / sin 60 = 2.309): right.
- Tilt 15 at 24 mm, W 1006: f = 670.7; VP 3 2503.0 px above center = f / tan 15; horizon moves 179.7 px = f tan 15;
  VPs apart grows to 1603 px (1549 / cos 15). Readout "VP 3 2503 px above center": right.
- Eye standoff D = 120 + 6 (e - 1.6) m: 120, 170, 470, 1010, 2510 m at the five stops; look-down angle to the block
  atan(e / D) = 0.76, 3.36, 7.27, 8.44, 9.05 degrees (see S1).
- Find the Camera, the six targets: each gives 100% at its listed settings. A scan of every stop x lens x turn 0 to 90
  (tilt as listed) finds no other setting at 92% or more except the target's own turn plus or minus 1 degree; the best
  wrong eye/lens pair reaches 71% (target 1), 29%, 21%, 62%, 9%, 48%. Target 6 without Tilt: 33%. Unique and reachable.

## Done when

1. Pass. Eye 60 m: the 60 m point on the 34, 52 and 40 floor buildings projects to v = 411.6 = the horizon row.
2. Pass (formulas exact at W 1006 in the app; Python at W 1200 matches the spec's numbers).
3. Pass. Every unclipped wall's horizontal edges pass through its VP within 1e-10 px at three cameras (60 m / 30 / 35 mm;
   1.6 m / 15 / 24 mm / tilt 15; 10 m / 60 / 50 mm / tilt -10); verticals pass through VP 3 within 2e-11 px.
4. Pass (above).
5. Pass for the parts tested: a real drag 3 degrees off the line to VP L snapped onto it (line passes VP L within 1e-13
   px), said "to VP L" and "Last line: to VP L."; the stroke survived a new tab (localStorage); Save picture draws the
   render and ink only (frame pic). Clear drawing not re-tested.
6. Pass (scan above).
7, 8: sizes, frame rate and voice counts belong to the Play and Craft lenses.

## Findings

### Should fix

**S1. The eye stands back so fast that Drone and Helicopter look like a shrunken Rooftop.** src.html:240 (`standoff`),
frames eye-60, eye-150, eye-400. Seen by computing atan(e / D) and looking at the frames. The spec's one idea is that
lifting the eye from the sidewalk to a helicopter "redraws the whole skyline". With D = 120 + 6 (e - 1.6) the look-down
angle only goes from 7.3 degrees (Rooftop) to 8.4 (Drone) to 9.1 (Helicopter), so a student sees about the same view
getting smaller: the 52-floor tower is 258 px tall at 60 m and 48 px at 400 m (24 mm, f 670), a smudge in an empty
plain. Nothing new about tops, streets or the grid appears above 60 m. Better: a slower standoff, for example
120 + 1.5 (e - 1.6) m (400 m gives D 718 m and 29 degrees down; the block base sits 373 px below the horizon, which fits
with Horizon on page at 20 to 30 percent), raising the default horizon as the eye climbs, or a Helicopter hint that
invites Tilt down (real aerial shots look down and are three-point). The builder flagged this choice for Cory
(handoff "For Cory"); the teaching evidence says the current rate loses the tool's main idea. Tag: family:perspective
(how the camera is placed for high eyes).

**S2. A teacher-note question plants a misconception.** notes.md line 23: "Which show their bottoms when you tilt up?"
Seen by reading kit/perspective.js box(): which faces show depends on where the eye is, not where it points, so tilting
never reveals a bottom. Buildings on the ground never show a bottom; only the water tower's raised tank does, and only
when the eye is below it, tilted or not. Better: "Tilt up. Do the building edges still stand straight? Where do they
meet?" or "From the sidewalk, which thing shows its underside? (the water tower's tank)". Tag: general.

**S3. VA:Cr3 (refine and complete) is mentioned more than taught.** Ink (src.html:1114-1258), notes.md "Standards".
Seen by walking Ink: the student can draw, erase, undo and save, but nothing asks them to judge the drawing against
criteria and revise it, which is what Cr3 asks at high school (apply criteria, reflect, plan revisions). With Snap on
and the render showing, the tool does the aiming for them. Rule 2 (taught well, above the minimum). Activity that would
teach it: a "Check my drawing" step: turn Snap off, draw, then the tool marks each line that misses its nearest VP or
vertical by more than a few degrees and counts them; the student fixes the marked lines and sees the count fall, with
one short "what I changed" prompt saved with the drawing on this device. Otherwise move VA:Cr3 off the module. Tag:
general.

**S4. Find the Camera rewards sweeping the sliders, not reading the picture.** Hint and voice (src.html:298, 770),
frames find-t2-start, find-t5-eye400. Seen by playing targets 2 and 5: the only guidance is "Move the eye height, turn
and lens until your city matches the outline", and the match meter works as hot and cold. The cues a real camera
match uses are already on screen: the outline is drawn on the student's horizon row, so the horizon crosses the target
buildings at the hidden eye height (count floors x 3.5 m); the outline's edges, extended, meet at the hidden VPs (turn);
how far apart they are in focal lengths gives the lens (2 / sin 2t). Better: a hint per step (horizon first, then
turn, then lens), a short "How to find a camera" note in notes.md, and a toggle that extends the outline's edges
(this shows the method, not the answer). Tag: family:perspective.

### Polish

**P1. Eye height in Find is a five-way pick.** src.html:235, 266, 844. The five stops are exactly the target heights
and the slider snaps to a stop within 8 of its 1000 steps, so with S4 a student can solve each target by trying five
heights. Better: some targets between stops (with an eye tolerance in the match), or no snapping in Find. Tag:
family:perspective.

**P2. "Horizon on page" stops meaning the horizon once Tilt is on.** src.html:152-155, frame guides-tilt. At 70% with
tilt 15 the horizon draws at 96% of the stage (moved f tan 15 = 180 px), but the slider still says 70%. The spec's Tilt
fact (the horizon moves f tan p the other way) is never shown. Better: a readout row with Tilt, "Horizon moved 180 px
down (f tan 15 degrees)", or name the slider "Picture center" while tilted. Tag: family:perspective.

**P3. A fact line with nothing on screen to match it.** src.html:271, 883; frames eye-60, eye-150. "Above the horizon
you see bottoms, below it you see tops" shows at 60 m and 150 m, where no bottom is visible (the only raised thing, the
water tank, is below the eye). Better, from what the screen shows: "Buildings shorter than your eye show their roofs;
taller ones hide theirs." Tag: general.

**P4. Ink still offers "vertical" in three-point.** kit/perspective.js targets(); src.html:1178. With Tilt, building
verticals run to VP 3 (the tiltHow line says so), yet a near-vertical stroke away from the center can snap to "vertical"
and be labeled that way. Better: drop the vertical target when pitch is not 0 (VP 3 takes its place). Tag:
family:perspective.

**P5. "Focal lengths" is never explained.** src.html:872. The readout says "1549 px = 2.31 focal lengths" while the
lens buttons are in mm. Better: a note under the readout, "1 focal length = lens / 36 x page width = 670 px now", which
also shows the spec's f formula and why the number in focal lengths does not change with the lens. Tag: general.

**P6. Composition (the module's second word, VA:Cr2) has no goal.** Build gives full camera control but never asks the
student to choose a view for an effect. Better: one or two prompts in Build, for example "Make the tallest tower feel
huge: low eye, wide lens, horizon low. Now make the city feel small." Tag: general.

### Nit

**N1.** src.html:718. A match at turn 29 says "Matched. ... turn 30 degrees". It is the hidden camera's setting; "The
hidden camera: eye height 60 m, turn 30 degrees, 35 mm" would match the state. Tag: general.

## Other checks

- Facts on screen are all in the spec's Content and Sources; settings (3.5 m floors, lots, example city, standoff) are
  labeled as settings in notes and the source comment.
- Nothing in Find shows the hidden camera's horizon, VPs or numbers before the match; the readouts describe only the
  student's camera.
- Language is plain and right for 9-12. No sensitive topics; no cultural, Native or hard-history content, so no
  sensitivity review is needed. No em dashes in src.html, notes.md or voice/lines.json.

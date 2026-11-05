PASS (round 2 re-check, 2026-10-28): A, B, C and D fixed, no regressions; polish only (Check camera 3 px low in the panel at 1280x720, small Find outlines at 375, stale "four tries" line in the spec)
Counts: blockers 0, should fix 14 (general 12, family 2), polish accepted 14

# city-skyline-studio: Refine

Lens files: refine/teaching.md (T), refine/play.md (P), refine/craft.md (C). Read them for frames and detail.

## Blockers
None.

## Should fix
1. **The high eye stops don't look down** (T-S1, P-S2; family:perspective). The eye stands back 6 m per meter it
   rises, so the look-down angle only goes from 7.3 to 9.1 degrees and Drone and Helicopter are a shrunken Rooftop
   (the city is about a 50 px speck at Helicopter, 24 mm; the ground is two thin crossed strips). This is the tool's one
   idea, so settled with BASELINE (standards taught well): at Drone and Helicopter the student must see the city from
   above (roofs and the street grid), with the city filling at least half the stage at 24 mm. A slower stand-back, a
   horizon that rises with the eye, or both; the VP math stays as it is. Show the ground as a real street grid. Record
   the new rule in docs/families/perspective.md.
2. **"Which show their bottoms when you tilt up?"** (T-S2). Tilt never changes which faces are visible, only the eye's
   position does. Reword notes.md (and any line or fact saying it).
3. **VA:Cr3 is named, not taught** (T-S3; rule 2). Settled with BASELINE (standards taught well): add a "Check my
   drawing" step in Ink: with Snap off the student draws, the tool marks the lines that miss their vanishing point,
   the student revises them, and one short reflection prompt closes it. Voice the step once (how line). Add it to the
   spec under "Refine changes".
4. **Find the Camera rewards sweeping, and the meter misleads** (T-S4, P-S5, T-P1; family:perspective for the meter).
   The meter has false peaks on the street-level targets (target 1 peaks at 52% at 20 degrees, target 4 at 47% at 35,
   the right lens on target 6 drops it from 40% to 19%). Make the meter rise toward the answer, setting by setting, and
   teach reading the camera from the picture: hints that point at where the horizon crosses the buildings, where the
   edges meet and how far apart the VPs are, offered after a few tries. The eye-height stops must not be exactly the
   target heights (or must not snap), so eye height is read, not picked from five.
5. **Clear city's confirm press runs away** (P-S1). "Sure? Clear city" wraps the button below the fold at 1366x768
   and the second press misses. The confirm stays under the pointer at every size.
6. **Tilting up at Sidewalk says "Your city is off the page"** while buildings fill the stage (P-S3). The hint must
   match the state; the horizon label must not sit under the VP L chip.
7. **Find starts with the horizon at 35%, cropping targets 1, 4 and 6; Guides and Windows carry over and bury the
   target outline** (P-S4). Start Find so each target shows whole, and keep the outline readable over any overlay.
8. **The panel jumps about 23 px when the hint changes length** (P-S6). Pen buttons and Tilt move under the pointer.
   Reserve the hint's height.
9. **760x900: Lens, Horizon on page and Tilt below the fold; the header wraps** (P-S7, C-S5; Done when 7). Fix it,
   and correct the handoff claim.
10. **A new building can land hidden behind another** (P-S8). Place it on a free lot that is visible from the camera.
11. **Find with Plan on draws the Build city in the inset** (C-S1). The inset shows the city the view and target use.
12. **Ink's welcome and the Line hint ignore the pen and Snap** (C-S2). "Your lines snap" only when Snap is on and the
    pen is Line; Read speaks the right one.
13. **The view's focus ring is about 1.2:1 on the Ink drawing** (C-S3). At least 3:1 on every background.
14. **"Saved on this device only" appears only in Ink** (C-S4; rule 7). Build and Find save too: say it where the
    student sees it in every mode.

## Polish accepted
15. With Tilt on, "Horizon on page" still places the horizon, and the horizon shift is shown (T-P2).
16. The "you see bottoms" fact only when bottoms are on screen (T-P3).
17. No screen "vertical" snap in three-point; upright strokes go to VP 3 (T-P4, C-P3; family:perspective).
18. The "focal lengths" readout is explained in one short line (T-P5).
19. Build gives one composition goal for VA:Cr2 (T-P6).
20. Windows at Rooftop/24 mm says why nothing shows (P).
21. The first screen shows a city, not a gray wall over empty ground (P).
22. After target 6, Next says it starts over and resets Tilt; found targets are marked (P).
23. The empty-city hint names the next action (add a building), not Guides (P).
24. The keep or clear question about old ink is asked where the ink is visible, or says what it refers to (P).
25. Fast erase swipes erase along the whole swipe, not only sampled points (P).
26. The tool's how() wrapper does not drop a queued event line when a how line cuts in (C-P1).
27. "Then press Ink" comes back as the hint if its line was cut (C-P2).
28. The Guides line counts the dots right with Tilt on (C-P4).

Nits are optional; fix the cheap ones (match wording at turn 29, focalLengths in the doc, snap()'s unused cam, baseY
and size noted as level camera, a ray helper exported instead of the copied fromCamDir, a one-point VP not labeled
"VP L", panel text under 12 px, the contrast comment, the duplicated comment, aria-valuetext on #hatchSp).

## Settled calls (builder's decisions in handoff.md, settled with BASELINE)
- Find compares labeled silhouettes (plain overlap gave 85% at the start): kept, but see item 4.
- Lots snap to 5 m, not 10 m; the default lens is 24 mm; Overlays sit under Camera; a newer how line cuts an older
  how line (never an event or Read): all kept.
- The stand-back rule is replaced by item 1. Nothing goes to Cory from this tool.

## Exit check, round 1 (fresh cold agent, 2026-10-28)

Bundled with CURIO_DRAFT=1 (146 KB, no URLs in the bundle). Frames and logs are in my scratch folder
(exit-css/out/s1 to v4): default, Build, Ink and Find at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080,
760x900 and 375 (drive.py --host, host.html deleted after), Drone and Helicopter at every size, all six Find targets at
1366, 680, 1920 and 760, and the frames for each fix. No console errors or exceptions in any shot (the only log line was
the host server's favicon 404). Placeholder art and the browser voice, as expected.

### VP math (recomputed, unchanged)
- Engine in node, W 1200, 35 mm: f 1166.67. Turn 45: VPs at -566.67 and 1766.67. Turn 30: -73.58 and 2620.73. At 85 mm
  and turn 45 they sit 5666.67 apart. Every box edge passes through its VP (worst 2e-15) at pitch 0, 15 and -10. VP 3
  sits f / tan p from the center and the horizon moves f tan p the other way, exactly. An eye-height point projects to
  the horizon, and ground() round-trips project().
- In the app (W 1006): eye 1.6, 60, 150 and 400 m, turns 30 and 45, 35 and 85 mm. All of these differences are 0:
  VP L - (cx - f tan t), VP R - (cx + f cot t), both VPs' v - horizon, and apart - 2f / sin 2t. With tilt 15 at every
  eye, VP 3 and the f tan p shift are exact. The stand-back and Auto move only the horizon row (a lens shift).
- Done when 1 at 60 m: the 60 m point on two buildings lands on the horizon (68.6 = 68.6), with their bases below it.

### The merged list, re-checked
1. **High eyes look down: fixed, with one regression (A).**
   - Drone stands 209 m back (35.7 degrees down) and Helicopter 359 m (48.1 degrees), both recomputed.
   - Frames b-drone-* and b-heli-* show roofs, lit windows and a real street grid at every size.
   - City size at 24 mm:
     - Drone: buildings cover 46% of the stage area (full height, 52% of the width).
     - Helicopter: buildings cover 19 to 27% (62 to 88% of the height, 30% of the width). The central block with its
       lots spans 68% of the width and the lower three quarters, so the city reads as filling the stage.
   - The rule is recorded in docs/families/perspective.md.
   - **A (should fix, family:perspective): VP L is drawn at the wrong edge.**
     - With Auto at Drone and Helicopter (turn 30, 24 mm), VP L is at u 116, v -171: above the page, inside its width.
     - drawVP() sends any off-page L or R point to the left or right edge by the sign of u only. So VP L gets an arrow
       at the top RIGHT corner, on top of VP R's.
     - Only one red dot shows, labeled VP R, while the Guides run up and to the left (frame c2/drone-guides). turnHow
       still says "The two red dots are your vanishing points."
     - Point the arrow at the VP's own u (up, or the nearest edge), and keep the two chips apart.
2. Tilt and bottoms: fixed. notes.md is reworded, and the bottoms fact shows only when an underside is on the page.
3. **Check my drawing: partly fixed (C, should fix, general).**
   - The red path works with real drags:
     - Snap goes off.
     - A free line 45 degrees up turns red ("1 line misses its vanishing point.").
     - A line 0.8 degrees off VP L hits.
     - Undoing the red line opens the reflection.
     - Done saves the note (in localStorage too), restores Snap and says "Checked."
   - On that path it does teach revise and reflect (VA:Cr3). Open:
     - **The "three lines drawn" path never fires.** checkCount() runs only when the miss count changes. Three lines
       that all hit (to VP L, upright, level) leave the message empty and open no reflection, and the hint stays on
       "Snap is off now..." (c1/check3ok). A careful student dead-ends.
     - **Erasing the red line without redrawing it passes.** With every line erased, the panel still said "All 1 line
       hits a vanishing point." and asked "What did you change...". Ask for the redraw, as the hint already says
       ("draw it again").
     - **The reflection opens below the fold.** At 1366x768 the reflection box and Done open at 749 to 877 px, and the
       panel does not scroll to them, while the hint says "then press Done". Bring them into view when they open.
   - Polish: the tool marks a line red at once, so the student never judges first. A "which of your lines do you think
     miss?" moment before the red would make the judging the student's own.
4. **Find the Camera: meter fixed, sweeping not (B, should fix, family:perspective).**
   - What works, recomputed with the tool's own matchOf on all six new targets:
     - Sweeping each setting alone has one peak, at the answer, and rises toward it monotonically. The sweeps were
       eye over all 1001 slider steps, turn 0 to 90, the four lenses, and tilt -25 to 25.
     - No eye-height stop scores 0.95 on any target (best 0.875, Helicopter on target 5).
     - The start camera scores 15 to 53%, and stops do not snap in Find.
   - What fails:
     - A student who only watches the live meter, one slider at a time, matches every target in one pass. A simulated
       coordinate ascent from the start camera matched 6 of 6 with no reading.
     - The reading hints and the Extend outline edges appear only after four tries without a match, so a sweeper never
       meets them.
     - The camera is still swept, not read.
   - One way out: the meter answers only when the student presses a Check camera button (each press counts as a try),
     with the reading hint before the first try. The per-setting meter stays as it is.
5. Clear city: fixed. "Really clear?" appears in the same rect at 1366 and 680, and the second press clears.
6. Tilt up at the sidewalk: fixed. No off-page hint at tilt 20, and the horizon chip stays clear of the VP chips.
7. **Find framing and outline: outline readable, but targets do not show whole (D, should fix, family:perspective).**
   - Fine: the outline is amber over a dark halo, above Guides and Windows, and Plan and the found marks work.
   - The outline's top is cut on 5 of 6 targets at 1366x768: target 1 by 339 px, 2 by 688, 3 by 257, 4 by 855 and
     5 by 375. Only target 6 fits. Targets 1, 2, 4 and 5 are also cut at 1920 and 760.
   - The spec's Refine changes say "Find frames each target so its outline shows whole", and handoff.md names only
     target 4.
   - The base, the horizon crossings and the edges stay readable. Either fit the outlines (a uniform screen scale in
     Find keeps every angle), or change the spec line and handoff.md with the reason.
8. Hint height: fixed. The Camera section's top stays at 199 px through four hint changes.
9. 760x900: fixed.
   - Tilt sits at 822 to 866 in Find, and the pens at 851 to 895 in Ink.
   - The header is one row, and the title is for screen readers only.
10. New buildings: fixed. A block and a tower were added on visible lots, with the roof outlined.
11. Plan in Find: fixed (it shows the Example city). Nit: the Plan inset covers the horizon label at street level.
12. Ink welcome and Line hint: fixed. They follow the pen and Snap, and Read says the same.
13. Focus ring: fixed. It is dark 3 px with a cyan inset, visible on the Ink paper, and Tab from Read lands on the view.
14. Saved notices: present in Build, Ink and Find. Polish: in Build the notice sits at 1296 px, far below the fold.
15 to 28. Checked in code and frames, all fine:
   - Tilt readouts (VP 3 and the tilt shift), the bottoms fact, and no screen vertical with pitch.
   - The focal-length note, composeGoal, winSmall, and a first screen with a city and windows.
   - Start over (target 1, Tilt level, message) and the empty-city hint.
   - Faint ink under the ask, and swipe erase (it erased along the whole swipe).
   - how() re-queuing offPage, bridge(), and guidesHow3.

### Family doc against kit/perspective.js
- Every export is documented with the signature and fields the code has: camera, project, ground, ray, vp, dirs, vps,
  poly, line, clipRect, box, order, corners, homography, divide, targets, snap, shade, hatch, inside, chord, fov, focal,
  baseY, size, toCam and SENSOR.
- The details match too: camera's horizon and focalLengths, box's center and clipped, targets' pitch rule, snap's
  unused cam, and baseY and size being level-only.
- The Auto rule matches autoHor(): nearest block corner at 90%, horizon at most 600% above and 80% down.
- The Find fit rule matches fitHor().
- Nit: the "What each tool brings" row still says "Find the Camera (silhouette match by face side)". It is now the
  per-setting match.
- Nit (outside scope): docs/KIT.md has no line for perspective.js yet.

### Regressions and other finds
- A, above (new with the high horizon).
- Polish:
  - In compact layouts an off-page VP arrow at the top sits under the hint band (b-heli-680).
  - In Find, VP L's arrow and label at the top left sit under the target chip (s2/tgt5-1366).
  - In Find, the long settings line ("The hidden camera: ...", about 5 s) keeps playing after the match is undone, and
    holds back the next "Matched." by up to 3.4 s (v3).

### Gate
1. **Done when:** 1 to 5, 7 and 8 pass.
   - 5: a stroke 3 degrees off snapped "to VP L"; the PNG is 1006x686 with no guide pixels; the drawing survived a new
     tab; Clear drawing emptied it.
   - 7: sliders and stage sit above the fold at every size; a frame takes 3.2 ms with 20 buildings and Guides at
     1920x1080.
   - 6 passes as written (every target matches at 100% with its settings and no stop matches), but see B.
2. **Codes:** VA:Cr2 is taught (construction plus the composition goal). VA:Cr3 is taught on the red path, with C open.
3. **Solo defaults:** yes, apart from C's dead end and B.
4. **Sensitivity:** not needed (no cultural, Native or hard-history content).
5. **Open should-fix:** A, B, C and D. **Fails.**
6. **Bundle:** 146 KB, one file, no URLs, no console errors or exceptions in any shot.
7. **Voice** (held clicks, 2 s pace, Sound and Motion on):

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| welcomeBuild, welcomeInk, welcomeFind | how | 1 per page | 1 each |
| turnHow (5 eye stops) | how | 1 | 1 |
| guidesNext (5 turns) | how | 1 | 1 |
| guidesHow, buildNext (5 Guides taps) | how | 1 each | 1, 1 |
| tiltHow (3 tilts from level) | how | 1 | 1, then 2 silent |
| inkHatch, inkFill (10 pen taps) | how | 1 each | 1 each, then 4 silent each |
| checkHow (5 toggles) | how | 1 | 1 (1 dropped stale when switched off first, 1 silent) |
| offPage | event, once per session by design | 1 | 1 |
| matched (5 matches, 5 s pace) | event | 5 | 5 |
| matched (5 matches, alternating 2 s) | event | 5 | 4 (1 dropped: its match was undone before the queue freed) |
| hidden camera settings (5 s pace) | event | 5 | 5 (at 2 s alternating: 2, the rest dropped stale after unmatch, correct) |

   - **First taps:**
     - Stage: welcome at 132 ms. A key: welcome at 2 ms.
     - Turn: its own guidesNext only. Guides: guidesHow, then buildNext.
     - Ink: welcomeInk. Read: the hint only.
     - Sound: nothing. Sound back on brings the welcome once.
   - **Read and mode changes:**
     - Read during the welcome speaks the hint.
     - A stop tapped during Read waits, and is dropped (unmarked) on the next mode change, which then speaks at once.
   - **Fast taps (0.2 s)** through Rooftop, Turn, Guides, Find, Build and Clear city:
     - Each newer how line cuts the older one.
     - Queued Build lines are dropped on the mode change.
     - Nothing plays after its moment, and the order is kept.
   - **Lines:** all 38 of allLines() match voice/lines.json word for word, with no em dashes. Counts right.

## Round 2 re-check (same cold agent, 2026-10-28)

I re-bundled with CURIO_DRAFT=1 (152 KB, one file, no URLs) and re-shot everything in exit-css/out2:
- Default, Build, Ink and Find at the 7 STANDARDS sizes.
- Drone and Helicopter with Guides at 680, 1000, 1366, 1920 and 760x900.
- All six targets at 1366, 680 and 1280.
- The 375 frames via drive.py --host (host.html deleted after, my server stopped, ports 9730-9739 clear).

There were no console errors or exceptions in any shot; the only log line was the host's favicon 404. I fixed nothing and committed nothing.

### A. Off-page VPs: fixed
- At Drone (1366x768) VP L is at u 116, v -171, and it now shows at the top edge near u 256, with its own arrow and chip. VP R shows at the right edge. The Guides run toward the VP L mark (frame r2/A-4-1366).
- The same holds at Helicopter and at 680, 1000, 1920 and 760x900.
- At 680, VP L (v 33) sits under the compact hint band. It is drawn at the band's edge as off the page, which is correct.
- turnHow now reads "The red dots are your two vanishing points. An arrow at the edge points to one off the page."
- Polish: at 680 the VP L chip is pushed about 75 px below its dot, because it is kept clear of the horizon chip (r2/A-4-680).

### B. Find meter: fixed (the meter is not live)
- **Before any Check:** a first visit shows "Not checked", 0%, no per-setting scores, and the welcome names Check camera. After real slider moves it still says "Not checked", and the hint becomes findCheck.
- **First Check** (panel button): it shows "Match 55%" with Eye height 87%, Turn 60% and Lens 20%. The message says "Not yet: 3 settings are off. Read the eye height next." The hint becomes the eye reading hint, and Extend outline edges appears.
- **After a change:** the stage chip says "Last check 55%" and the stale note shows.
- **Sweep test:** I swept eye over 10 values and turn over 6 with the tool's own setter. The meter, chip, bar, per-setting scores and message showed exactly one state throughout, so nothing on the page follows the camera between checks.
- **Match:** the exact settings plus the stage chip's Check camera give Match 100%, all ticks, and found [0]. Next target shows and the chip's Check button hides. A later change undoes the match until the next check.
- **Sweeping no longer solves.** The only feedback is one Check press per probe. A student who never reads, steps one setting at a time and checks each step:
  - needed 5 to 26 checks per target;
  - still missed 5 of 6 targets at a coarse step (about 11% eye steps, 2 degree turn steps).
  - Every miss names a setting and shows its reading hint, which reads the picture: where the outline's horizon crosses the buildings, the edges extended to the outline's own VPs, how far apart the VPs are, and how the uprights lean.
- **Still exact:** the per-setting match is unchanged (matchOf sweeps identical to round 1: one peak per setting, rising, no eye height stop at 0.95, start 15 to 53%).
- Residual (no change asked): the per-setting percentages after each check still let a determined student hill-climb in about 10 to 25 checks. Each check costs a press and comes with the reading hint, so I accept it.

### C. Check my drawing: fixed
- **Three hitting lines** (to VP L, upright, level) now open the reflection at 1366, 1280, 680 and 760x900. The messages are "All 1/2/3 lines hit...", and the hint becomes checkReflect.
- **Done comes into view** when the reflection opens:
  - 1366x768: Done at 724 to 768
  - 1280x720: 676 to 720
  - 680x425: 381 to 425
  - 760x900: 856 to 900
- **Erase without redraw:** a red line erased without redrawing says "A line is missing. Draw it again toward its vanishing point." and keeps the reflection closed. Undo of the red line does the same.
- **Redraw:** redrawing toward VP L opens the reflection, and Done saves the note and restores Snap ("Checked. Your note is kept with the drawing.").
- **Reset:** toggling Check off and on clears the messages ("Draw a few building edges by eye.").
- Round 1 polish still open: the reflection asks "Write what you changed" when nothing was red, and the tool still marks red before the student judges.

### D. Find outlines whole: fixed, with the math recomputed
For each of the 6 targets at all 7 STANDARDS sizes, I set the student camera to the target and checked:
- **Fit:** 0 of 42 outlines are cut. Every outline is below the target chip and inside the stage. The picture scale s runs from 0.37 to 0.72, and 0.19 to 0.42 on the 308 px stage at 760x900.
- **Same picture, scaled:** I projected every outline corner with the scaled camera and with the true focal length (same horizon row). A least-squares fit gives a similarity whose scale equals s to 1e-6, with residuals of 2e-13 to 6e-13 px. So the Find picture is the true picture, uniformly scaled: every angle and VP direction is unchanged.
- **VPs:** the VPs sit exactly at cx - f' tan t and cx + f' cot t on the horizon, where f' = s x lens / 36 x W. Their spacing is 2f' / sin 2t, and VP 3 on target 6 is at f' / tan p. All differences are 0.
- **Overlay:** the student's frame at the target settings overlays the target outline exactly (max difference 0 px).
- **s depends only on the target.** With the student's eye x3 and a different lens, f / (lens / 36 x W) stays s.
- **Match unchanged:** the match is computed on settings and is 1 at each target's own settings.
- **Readouts:** the lens readout stays in true mm ("24 mm, 73.7 degrees wide"). The focal-length readout says "x 58% (Find shrinks the picture so the whole outline fits) = 390 px now".
- **At 375** (host): all six outlines fit whole in the 200 px stage (rows 74 to 188, under the chip ending at 64).
- kit/perspective.js was not touched, and the node engine checks still pass (2e-15; eye-height point on the horizon).

### Family doc
- The "What each tool brings" row is now current: per-setting match on Check camera, outlines fitted by a uniform scale, and Check my drawing.
- New rules match the code:
  - uniform fit (findScale, fitHor);
  - a meter that answers only on Check;
  - off-page VPs placed along their direction (vpEdge), with a VP under a band counted as off.
- spec.md has a Round 2 section that matches the build. Nit: the older Find paragraph in the spec still says reading hints come "after four tries (bursts of changes)", which round 2 supersedes.
- Nit (outside scope, from round 1): docs/KIT.md still has no perspective.js line.

### Regressions: none found
- **VP math:** recomputed at eyes 1.6, 60, 150 and 400, turns 30 and 45, lenses 35 and 85, tilt 15. Every value is identical to round 1 (all differences 0; at 60 m the eye-height points sit on the horizon at 68.6).
- **Round 1 items re-run from a clean state:**
  - Clear city: same rect at 1366 and 680, "Really clear?".
  - Tilt up at the sidewalk: no off-page hint.
  - Camera top: stays at 199 px through four hint changes.
  - New buildings: added on visible lots.
  - Plan in Find, the empty hint, Start over (target 1, Tilt level) and the focus ring (stage kfocus): all fine.
  - Saved notice: in all three modes (Build still low, at 1296 px, polish).
  - Snap: "to VP L".
  - PNG: 1006x686 with no guide pixels.
  - Reload: keeps the drawing, and Clear works.
  - Speed: 3.4 ms per frame with 20 buildings at 1920.
  - 375: no horizontal scroll, and the sliders are reachable.
- Drone and Helicopter extents are unchanged (Drone 46% of the stage, Helicopter 19 to 27%).

### Voice at a 2 s held-click pace (clean first visit, Sound and Motion on)

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| welcomeBuild, welcomeInk, welcomeFind | how | 1 per page | 1 each |
| turnHow (5 eye stops) | how | 1 | 1 |
| guidesNext (5 turns) | how | 1 | 1 |
| guidesHow, buildNext (5 Guides taps) | how | 1 each | 1, 1 |
| tiltHow (5 tilts) | how | 1 | 1, then 1 silent |
| inkHatch, inkFill (10 pen taps) | how | 1 each | 1 each, then 4 silent each |
| checkHow (5 toggles) | how | 1 | 1 (1 dropped stale, 1 silent) |
| offPage | event, once by design | 1 | 1 in Build |
| findCheck (first camera change, then 4 more) | how | 1 | 1 |
| findEye (5 missing checks) | how | 1 | 1, then 1 dropped (newer) and 1 silent |
| findLens (5 missing checks, alternating) | how | 1 | 1, then 4 silent |
| matched (5 matching checks, alternating 2 s) | event | 5 | 5 |
| hidden camera settings (same) | event | 5 | 3 (2 dropped stale: the match was undone before they could play) |

- First taps:
  - stage, key and Sound back on: welcome
  - Turn: guidesNext
  - Guides: guidesHow, then buildNext
  - Ink: welcomeInk
  - Read: the hint only
- Read cuts and fast-tap stale drops are as in round 1.
- findNext was dropped as stale or newer at this pace (the student had moved on). The hint keeps showing it.
- All 39 lines in allLines() match voice/lines.json, with no em dashes. Three new texts still need clips (the browser voice is expected).

### The builder's two notes
- **Check camera below the fold at 1280x720:** the panel button sits at 675 to 723, 3 px below the fold. The stage chip's Check camera (238, 99) is always on screen and does the same thing. Polish, accepted.
- **375 Find stage:** the stage is 200 px tall, so the outlines are only 114 px tall (60 to 210 px wide). They are whole, but the VP and horizon chips crowd them (s375/h375-find2). Before round 2 they were cut. Polish, accepted. A taller Find stage at phone width would help.

### Gate
1. Done when: passes. Item 6 passes with the meter answering only on Check.
2. Codes:
   - VA:Cr2 is taught.
   - VA:Cr3 is now taught on both paths (red then fix, and three by-eye lines), with a reflection.
3. Solo defaults: yes.
4. Sensitivity: not needed.
5. Open should-fix: none.
6. Bundle: 152 KB, no URLs, no console errors.
7. Voice: counts right.

**PASS.** Remaining polish:
- the 1280 panel button 3 px low;
- small outlines at 375;
- the VP L chip offset at 680;
- the Build saved notice sitting low;
- the reflection wording;
- the stale "four tries" line in the spec.

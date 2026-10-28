# city-skyline-studio: build handoff (2026-10-28)

## What was built

- `src.html` (bundled as `city-skyline-studio.html`, CURIO_DRAFT=1), `tool.draft.json` (stage "built"), `notes.md`,
  `art/prompts.json` (no art: everything drawn in code), `voice/lines.json` (casual-peer, Zubenelgenubi, 25 lines from
  `__tool.allLines()`; clips not generated yet).
- New shared engine `kit/perspective.js` (global `Persp`) and family doc `docs/families/perspective.md`.
- No existing kit file was changed. `docs/KIT.md` does not list perspective.js yet (outside my write scope): add a line
  pointing at docs/families/perspective.md.

Modes: Build (camera, buildings, overlays Guides / Plan / Windows / Sun), Ink (Line with snap, Hatch, Fill, Erase,
Undo, Redo, Show render, Hide guides, Save picture, Clear drawing), Find the Camera (6 targets, match meter, 92%).

Layouts as collision-lab: wide (w >= 1000 and h >= 700, 360 px panel), compact (short landscape, 300 px panel, one-row
header, the hint docked on top of the stage in `#hintDock` so it is never clipped), stack (stage on top, panel below,
page scrolls). Canvas drawn at real pixels (dpr up to 2), one draw per animation frame when dirty.

## Engine API

See docs/families/perspective.md (exact). In short: `camera, project, ground, vp, vps, dirs, box, order, corners,
divide, homography, targets, snap, shade, poly, line, clipRect, hatch, inside, chord, toCam, fov, focal, baseY, size,
SENSOR`.

## Decisions (settings, not facts)

- **Eye distance (replaced in round 1 by 120 + 0.6 (eye - 1.6) m and Auto horizon, see below):** the eye stands back as it rises, D = 120 + 6 (eye - 1.6) m from the block center (120 m on the
  sidewalk, 470 m at 60 m, 1010 m at 150 m, 2.5 km at 400 m). Without it, high eyes look over the block entirely. Shown
  in the Eye height readout ("470 m from the block") and on the Plan (eye with a break mark and its distance). It does
  not affect any VP position (those depend only on f and turn).
- Lot positions snap to 5 m, not the spec's 10 m: 10 m left some building widths unable to sit centered on a lot.
- Default lens 24 mm (so VP L is on the page at turn 30 and "the two red dots" is true at once); default horizon 60%.
  Find uses its own camera, starting at 1.6 m, turn 0, 50 mm, horizon 35%.
- **Find the Camera match:** the spec says "overlap of the two silhouettes". Plain silhouette IoU at street level was
  85% at the start (the buildings fill the frame whatever the turn), so the match compares the silhouettes with each
  face labeled by which side it is (which way it faces). Exact settings give 100% on all six targets; turn off by 2
  gives 81 to 90%, the start camera 0 to 37%. The target uses the student's Horizon on page so that slider can't
  block a match.
- Off-page help: when fewer than a third of the buildings have their base on the page (high eye, long lens, horizon
  low), the hint says "Your city is off the page. Move Horizon on page, or pick a wider lens." with an arrow chip.
- Overlays sit right under Camera (so Guides, which the hint names, is on screen at 1366x768).
- A newer step's how-to cuts in on an older how-to that is still playing (its step is done), never on an event or Read
  (`how()` wrapper, kit `now`). Without it, at 2 s taps "Turn on Guides" played on after Guides was on.
- Selection starts empty (nothing outlined until a tap or the Selected list).

## Checked (frames in my scratch folder, out1..out11)

- Worked check (W = 1200, 35/85 mm) and edge-meets-VP within 1e-11 px in node; the app at 1200 px stage width: VP L
  -51.50, VP R 1834.51, apart 1886.01 at 35 mm turn 30 (Python agrees). Tilt 15 at 24 mm, W 1006: VP 3 at
  2503 px above center = f / tan 15, apart grows by 1 / cos 15 (1603 px).
- Done-when 1: eye 60 m, two buildings (34 and 52 floors): the 60 m point on each projects exactly to the horizon
  (v = 430.8 = horizon), their bases below and tops above; Python matches to 1e-9.
- 60 fps: 2.2 ms per frame at 1920x1080 with 20 buildings, windows and guides on.
- Ink: a line dragged toward VP L snapped onto the exact line to VP L and said "to VP L"; hatch lines aim at the face's
  VP; fill, erase (one Undo step), Save picture gives a PNG without guides; the drawing survives a reload; Clear
  drawing empties it (Undo brings it back); the keep-or-clear ask shows in Build after a camera change.
- Sizes 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375 (drive.py --host): all targets
  44 px or more (the compact Ink tab was 39 px, fixed), hint never clipped, no horizontal scroll at 375, no console
  errors. CORRECTION (refine round 1): the claim that all camera sliders were visible without scrolling was wrong at
  760x900 (Lens, Horizon on page and Tilt sat below the fold and the header wrapped). Fixed in round 1, see below.
- Voice with held clicks at 2.2 s and 0.6 s gaps: each how-to spoken once, the welcome skipped (unmarked) when the
  first tap queues its own line, stale lines dropped on mode change, Read speaks the current hint (recorded line texts).
- Keyboard: the view takes focus; arrows move the selected building 10 m (Build) or a cursor (Ink, Enter starts and
  ends a snapped line). Buttons that hide themselves (Keep it, Clear it, Next target on the stage, Edit camera) move
  focus to the view, the panel's Next target or the Build tab. Nothing takes focus on load.

## Known gaps

- Voice clips not generated (lines.json ready).
- (Replaced in round 1: the match is now per setting, and the targets are not the stops.)
- Building drag on the view uses a level plane through the grabbed point; dragging a face near eye height falls back
  to half the eye height, which feels slightly loose. The Plan drag is exact.
- Sun-lit faces are a warm gray-mauve; could use a pass on color.
- The offPage line plays at most once per session by design (spec); it can arrive a few seconds after the turn when a
  how-to is ahead of it, but is dropped if the VP has come back.

## For Cory

- (Round 1: the stand-back rule was replaced per refine item 1 and settled with BASELINE; nothing goes to Cory.)
- The Find match compares which way faces point, not only the outline (reason above).

## Refine round 1 (2026-10-28)

Items from refine.md, one line each. Scope: this folder, kit/perspective.js, docs/families/perspective.md.

1. Stand-back is now 120 m + 0.6 m per meter (Drone 209 m back, 36 degrees down; Helicopter 359 m, 48 degrees down) and
   Horizon on page has Auto (on by default, down to 600% above the page) that keeps the block low, so high stops look
   down on roofs and a drawn street grid (outer blocks plus 7 by 5 lots); the city fills well over half the stage at
   24 mm (frames r5/b-drone, b-heli). Rule recorded in docs/families/perspective.md.
2. Bottoms come from the eye's position, not tilt: notes.md reworded; the fact is now "Tiers above your eye show their
   undersides" and shows only when one is on screen.
3. Check my drawing added to Ink (Snap off, misses over 2.5 degrees turn red with a count, fix, one reflection note,
   Done restores Snap); how line once; spec "Refine changes" records it. Verified: red 1, fixed 0, reflect, Done.
4. Meter is per setting (eye log ratio, turn /40, lens stops, tilt /30), mean shown, matched at every part 95%+.
   Recomputed on all six targets: each setting sweep has a single peak at the answer and rises toward it (meter.json);
   start camera 15 to 53%; new targets (40, 3, 100, 20, 300, 2.5 m) are not stops and stops do not snap in Find;
   after four tries a reading hint (eye, turn, lens, tilt in that order) and Extend outline edges.
5. Clear city sits in a 3-column row; the confirm reads "Really clear?" in the same box (same rect at 680, 1366, 760).
6. Off-city check counts any face point on the page (tilted up at 5 m: no off-page hint); horizon label sits clear of
   the VP chips (off-page label centered).
7. Find frames each target with the lens shift (fitHor per target: centered when it fits, else its base at 95% of the
   height, the horizon allowed below the page); target 4 (20 m, 35 mm) is taller than any stage, so its tops crop but
   its base and horizon show. The outline is amber over a dark halo, drawn above Guides and Windows. The Horizon
   readout says "51% above" or "20% below" for off-page horizons.
8. The hint reserves four lines of height; the panel no longer jumps.
9. 760x900: header title screen-reader only in narrow stack, stage height leaves room for Camera (Build, Find) or the
   camera line plus pens (Ink); pens bottom 895 of 900, Tilt above the fold. Handoff claim corrected above.
10. New buildings prefer a free lot whose roof is on the page and not covered by a nearer face.
11. The Plan inset in Find draws the Example city (the city the view and target use).
12. Ink's welcome and Line hint follow the pen and Snap ("snap" only with Snap on and Line); Read speaks the same.
13. View focus ring is a dark 3 px border plus a 3 px cyan inset, 3:1 or more on dark sky, ground and the faded Ink.
14. "Saved on this device only" shows in Build, Ink and Find.
15. With Tilt, Horizon on page still places the horizon; readouts show VP 3 and the tilt shift (f x tan tilt).
16. Bottoms fact only when an underside is on screen.
17. kit targets() leaves out the screen vertical when pitched; upright strokes go to VP 3.
18. VPs apart readout adds "1 focal length = lens / 36 x page width = N px now".
19. One composition goal (composeGoal) after the first building moved or added post-guides; it becomes the hint.
20. Windows at a size too small to show say why (winSmall: longer lens or lower eye).
21. Windows on by default and the first screen shows the Example city at the sidewalk with lit windows.
22. Found targets get a check and "Found n of 6"; after target 6 Next reads "Start over" and sets Tilt level (verified).
23. Empty city hint is addFirst ("Tap Tower, Block, Slab, Stepped or Water tower").
24. The keep-or-clear ask shows the old ink faintly on the stage and says "Your Ink drawing (shown faintly)".
25. Erase tests every 4 px along the swipe between samples.
26. how() puts a queued offPage back after a cutting how line.
27. bridge() re-queues "Then press Ink" (buildNext) after later Build actions if it was cut.
28. Guides line with Tilt is guidesHow3 (three dots).
Nits: match wording, focalLengths, snap's unused cam, baseY/size level-only and the ray export noted in the family doc;
kit exports ray and hitOnFace now uses Persp.ray (no copied fromCamDir); a one-point VP is labeled "VP"; panel text 12 px or more; contrast comment
9.4:1; the doubled off-page comment trimmed; #hatchSp has aria-valuetext.

Checked: every mode at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375 (host): no target
under 44 px, no panel text under 12 px, no control below the fold, no horizontal scroll, no console errors; frames
looked at. Voice at a 2 s held-click pace: each how line once (turnHow, offPage, welcomeInk, checkHow, welcomeFind),
stale lines dropped on mode change. voice/lines.json regenerated (38 lines; clips still to record). Bundled with
CURIO_DRAFT=1. Frames: scratch r5 to r10.

## Refine round 2 (2026-10-28)

From the exit check (refine.md, round 1 exit). VP math untouched.

A. Off-page VPs are placed where their direction leaves the page (vpEdge: the line from the page middle, or from the
   horizon row for an infinite VP). At Drone 1366x768 VP L now shows at the top edge near u 256 with its own arrow
   and chip, VP R at the right edge; chips keep clear of each other and of the horizon chip; a VP under the compact
   hint band counts as off. turnHow no longer promises two dots ("The red dots are your two vanishing points. An arrow
   at the edge points to one off the page."). Rule in the family doc.
B. Find meter is not live: Check camera (panel and stage chip) shows the meter and per-setting scores, stale after any
   change; matched needs every setting at 95%; a miss names the first setting in reading order and its reading hint,
   and offers Extend outline edges. Voiced once (findCheck) on the first camera change. Recorded in spec Refine
   changes round 2. Verified: before = "Not checked", after a change = still "Not checked", check = "Match 28%" with
   Eye 39 / Turn 25 / Lens 20 and the eye reading hint, a change = "Last check 28%", the exact settings + check =
   matched, found [0], Next shown.
C. checkCount keys on (misses, lines, peak, lines drawn), so it runs on every check: three hitting lines open the
   reflection (verified); erasing a red line without redrawing says "A line is missing. Draw it again toward its
   vanishing point." and keeps the reflection closed, redrawing opens it (verified); messages reset on check on/off;
   the note and Done scroll into view (Done bottom at or inside the viewport at all 7 sizes and 375).
D. Find outlines fit whole by a uniform per-target scale (a shorter effective focal length for both cameras) plus
   centering under the target chip: 0 of 6 targets cut at 680x425, 800x500, 1000x625, 1280x720, 1366x768,
   1920x1080, 760x900 and 375 (outline extents measured on the stage). No target made shorter. The Find section now
   sits right under Camera, and the stage chip carries Check camera (one row at small sizes).
Family doc: the "What each tool brings" row is updated (per-setting match on Check camera, fitted outlines, Check my
drawing), plus rules for the uniform fit, the Check meter and off-page VPs.

Checked: Build, Ink, Find and Helicopter with Guides at all 7 STANDARDS sizes (no target under 44 px, no panel text
under 12 px, no control below the fold, no horizontal scroll, no console errors), 375 via --host (host.html deleted),
frames looked at. Voice at a 2 s held-click pace: 5 eye stops gave turnHow 1 and offPage 1; in Find a stop then 5
checks gave findCheck 1 and findEye 1 (later ones silent as heard); 5 Check my drawing toggles gave checkHow 1 (one
dropped stale when switched off, one silent as heard). voice/lines.json regenerated (39 lines; 3 new texts need
clips). Bundled with CURIO_DRAFT=1 (152 KB). Frames: scratch r11 to r13.
Open polish: at 375 the Find stage is 200 px tall, so outlines are small (whole, but small); the panel's Check camera
sits just below the fold at 1280x720 (the stage chip's copy is always on screen).

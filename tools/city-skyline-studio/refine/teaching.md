# Teaching lens: city-skyline-studio (round 1, 2026-11-04)

Fresh cold read of spec.md (with its Refine changes), src.html, notes.md, tool.draft.json, voice/lines.json and
kit/perspective.js, against REFINE.md, STANDARDS.md, BASELINE.md and the BUILD.md wave lessons. Shared audit:
`audit-r1/audit.md` and its frames. My own frames and scripts are in the scratch folder `teaching/` (f1/, f2/,
shots1.json, shots2.json, dw.js).

Counts: blockers 1, should fix 3, polish 3, nit 1.

## Standards (module arts-9-12-two-point-perspective-and-composition: VA:Cr2, VA:Cr3)

- **VA:Cr2 (organize and develop artistic ideas and work): taught.** The student sets up a construction (eye height,
  turn, lens, tilt), places and sizes buildings on a lot grid and reads the result through Guides and Plan. That is
  real skill building through experiment. The "composition" half of the module title is thin (polish 2).
- **VA:Cr3 (refine and complete): taught in design, undermined in practice.** Ink, Check my drawing, the reflection
  note and Save picture make a real revise-and-finish loop, but the check accepts the most common two-point error
  (blocker 1), so a student can pass the revise step without revising anything.

## Done when

| # | Check | Result | How |
|---|---|---|---|
| 1 | Horizon at eye level; crosses buildings at the eye's real height (60 m) | pass | dw.js: points at y = 60 m, z = 150 and 400 project exactly to the horizon row; "Horizon crosses N of 9" counts buildings taller than the eye |
| 2 | Worked check at W = 1200 | pass | 35 mm: f 1166.7; t 30: VP L -73.6, VP R 2620.7; t 45: -566.7, 1766.7; 85 mm at 45: 5666.7 px apart. FOV 73.7, 54.4, 39.6, 23.9 |
| 3 | Guides meet at the VPs within 1 px | pass | worst edge-line distance to its VP 5e-13 px; f1/t1 frame shows guides converging on VP L |
| 4 | Tilt 15: VP 3 at f / tan 15; verticals meet there | pass | 4354.06 px both ways; a projected upright passes through VP 3 (u 600.000); horizon shift = f tan 15 |
| 5 | Ink snaps and says which; PNG without guides; survives reload; Clear empties | pass | f2/saved.png has render and ink, no guides, horizon or VPs; 2 strokes after a new tab; Clear drawing then 0 with "Undo brings it back" |
| 6 | Each target matched with its listed settings; no stop matches a target | pass | every target scores 1.000 and says "Matched."; best stop score per target 0.82, 0.73, 0.82, 0.70, 0.88, 0.81 (all under 0.95) |
| 7 | Camera and stage above the fold at every size; 60 fps with 20 buildings at 1920x1080 | pass | audit size rows (only Overlays and Buildings fall below the fold at 760 and 375); 2.1 ms per draw with 20 buildings, Guides and Windows on |
| 8 | How lines once in five slider moves; matched every time | pass (cited) | audit "Five held clicks" clean on the stops; Matched plus the settings line played on each of six matches (t8). The counts table is Craft's |

## Findings

### Blocker

1. **Check my drawing passes flat lines, and Snap teaches them.** Where: Ink, `misses()` (src.html:1102) and
   `lineEnd()` (src.html:2212), both using `Persp.targets()` with its default `horizontal` target
   (kit/perspective.js `targets`). What: at Turn 30 no building edge is level on the page (edges on the horizon aim at
   the VPs anyway), yet any screen-level line counts as a hit. I drew three flat lines across the towers with Check on:
   "All 3 lines hit their vanishing points." and the reflection opened, asking what I changed (f1/t1-check-level-lines.png).
   Drawing a roof edge flat is the classic two-point mistake, and this is the tool's one revise step (VA:Cr3). With
   Snap on, a roof edge 300 px above the horizon drawn 3 degrees off level snapped to "horizontal" and the status
   read "Last line: horizontal." (f1/t2), so the pen itself rewards the error. With Tilt 15 the same flat lines still
   pass (f2/t11). The check's message is a meter that misleads when its assumption fails, so this is a blocker
   (REFINE, Rounds). Better: drop the level target in this tool (snap and check). It is never needed: when Turn is 0
   or 90 the far VP comes back from `vps()` as an infinite direction whose angle is already level, so one-point views
   still snap and pass. Keep the upright only when Tilt is 0, as now. Tag: **family:perspective** (the engine's
   default target list).

### Should fix

2. **Find the Camera can be solved from the scores, not the picture.** Where: Find, `showScores()` (src.html:1356)
   and the miss message (src.html:1422). What: after each Check the panel shows an exact percent per setting, and each
   score is a straight line toward the answer (turn 1 - |diff| / 40, eye 1 - |ln ratio| / ln 10). From Turn 0 the
   turn reads 25%, so the answer is 30; one check per lens button finds the lens. I matched target 1 in five checks
   without looking at the outline (f1/t3: turn 0, lens 24, eye 10, turn 30, eye 40). Checks cost nothing, so this is
   "trying every option for free" (BUILD.md wave lessons, No giveaways), and the round 2 change that took the live
   meter away only slowed the sweep down. Better: after a check show per setting only "matches" or "not yet" (no
   percent), keep the "read the X next" hint, and let the overall meter move in coarse steps; or count tries per
   target and offer Extend outline edges as the help instead of numbers. Tag: **general**.

3. **The two street-level targets ask for a precision the picture can't show.** Where: Find targets 2 (3 m) and 6
   (2.5 m), eye tolerance 95% = within 12%. What: at target 2 with eye 2.4 m (Turn and Lens right) the student's
   render and the amber outline are almost the same picture, the outline's horizon a few pixels off (f2/t8t9.png, top
   2.4 m, bottom 3.0 m), yet the eye scores 90% and the target is "Not yet". The outline has no floor lines, so 3 m
   cannot be told from 2.5 m or 3.4 m by reading; the student can only nudge the slider and press Check until the
   percent passes, which is finding 2 again. The hint for both says "Roofs below eye level are visible", but at 3 m
   no roof is. Better: give the eye score a tolerance tied to what shows on the page (for example the outline's
   horizon within a few pixels of the student's, or within 0.6 m below 10 m), or raise these two targets to heights
   that read clearly (for example 6 m and 4 m, still off every stop), and give low targets a hint about where the
   horizon cuts the nearest building's base. Tag: **general**.

4. **A fact on screen says tiers show undersides; they don't.** Where: Build fact line, `FACTS.bottoms`
   (src.html:346) and `bottomsShown()` (src.html:1691); notes.md "Things to talk about". What: the fact "Tiers above
   your eye show their undersides: above the horizon you see bottoms." came up at the sidewalk (f1/t4 tips), because
   `bottomsShown()` counts any bottom face projected on the page. The stepped tower's tiers sit on the wider tier
   below, so their undersides are hidden: the zoomed frame shows only walls at both setbacks (f1/t4-crop.png). The
   only real underside on screen is the water tank between its legs. notes.md asks "Which tiers show their
   undersides", which sends a class looking for something that is not there. Better: say "Things above your eye
   show their undersides, like the water tank on its legs: above the horizon you see bottoms.", show it only when a
   bottom face is actually drawn uncovered (the tank), and fix the notes question to the tank. Tag: **general**
   (a fact keyed to geometry, not to what the student sees).

### Polish

5. **The reflection asks "What did you change" when nothing changed.** Where: Ink, Check my drawing, `#reflect`
   (src.html:246). After three lines that all hit with no red line ever (f1/t1), the question reads as a trick. Better:
   when `checkHadRed` is false ask "How did you aim each line at its vanishing point?" and keep the current question for
   a real fix. Tag: **general**.

6. **Composition is one recipe line.** Where: Build, `composeGoal` (src.html:365). The module is "Two-Point
   Perspective and Composition", but the only composition moment is one hint that gives the answer with the goal ("a
   low eye, a wide lens, the horizon low"). Better: two or three short briefs to pick from (make the tower feel huge,
   a calm wide street, a map-like view from above), each saved with the drawing, and let the student find the settings.
   This touches what the tool teaches, so it may belong in the spec's open questions. Tag: **general**.

7. **"Looking 48 degrees down" with parallel uprights needs one sentence.** Where: Readouts, Eye height
   (src.html:1675), audit frame state-helicopter-guides-plan-1366x768.png. From the Helicopter stop the readout says the
   block is 48 degrees down, but the camera stays level (the page is shifted), so uprights stay parallel. A student who
   knows real aerial photos lean will wonder why. Better: a readout note "The picture stays upright, like a drafting
   view; Tilt shows the real lean (three-point)." and the same line in notes.md "Good to know". Tag:
   **family:perspective**.

### Nit

8. **Check my drawing tests direction, not place.** A line in empty sky aimed at VP R passes. Fine for a first
   check; a later version could ask that each line start on a building corner. Tag: **family:perspective**.

## Other checks (nothing found)

- Facts recomputed: stand-back 155 m, 209 m, 359 m and 21, 36, 48 degrees down; "1 focal length = lens / 36 x page
  width"; VPs 2 / sin 2t focal lengths apart (the same number for every lens, as notes.md says); VP 3 and tilt-shift
  directions (looking up: VP 3 above center, center above the horizon). All match the spec's Sources.
- Hidden information: no target value is in the DOM before a match; the eye stops do not settle in Find; target 6
  says only "looks up". The giveaway is the scores (finding 2), not leaked text.
- Language is plain and right for 9-12. What it teaches, Key skills and Support at home describe this tool; the home
  ideas (a box from a low seat, receding room edges, a ruled box sketch) are doable tonight. No sensitive topics.
- Guardrails: no timers, no points beyond "Found N of 6". Nothing cultural, Native or hard-history: no sensitivity
  review needed.

## Audit pilot

- **Confirmed:** the size rows I leaned on for Done when 7 (camera section and stage above the fold everywhere;
  Overlays and Buildings below it at 760 and 375); the five-held-clicks rows for Done when 8.
- **Wrong or by design:** "#clearInk nothing changed" (a fresh page has no ink; with two strokes it clears and says
  Undo brings it back, f2/t6); "#cv nothing changed" in Find (the stage takes no clicks in Find by design); the
  #cv / #checkCam2 overlap "at every size" is the stage chip, and the outline is fitted under it (f2/t8t9).
- **Missed (it can't see these):** the level-line pass in Check my drawing and the "horizontal" snap (blocker 1); Find
  solved from the per-setting percents (2); street-level targets that can't be read at the tolerance (3); the false
  underside fact (4); the reflection wording (5).

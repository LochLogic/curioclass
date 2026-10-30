# Curling Stones

## One idea
Push a curling stone out of the hack with a force you choose for a time you choose, then let it glide: F = ma gives
the speed at release, friction alone decides the glide, and a student who does the math can call the stop to within a
stone's width before the stone even moves.

## Not like
- collision-lab (gr 11, built, forces family): momentum and impulse in collisions on an air track. Here there is no
  collision: one object, a net force, an acceleration, then a steady friction force slowing it to a stop.
- field-lines (gr 11): forces at a distance and inverse square laws. Here contact forces (a push, ice friction).
- motion-graph-match (gr 11, built): you move to match position and velocity graphs. Here the graphs are the record
  of a push you designed; the question is why the line has that slope (a = F_net / m).
- launch-pad (gr 9 math, wave 1) and flight-planner (wave 2 math): projectile and vector math. Here the physics
  (forces, mass, friction) is the point; the algebra is short.
- skate-park-energy (gr 8): energy on a ramp. Here no heights and no energy bars: forces and accelerations only.
- tug-of-war-arena (gr 3) and crash-test-lab (gr 8), forces family, not built: balanced forces and Newton's third law
  in carts. Same engine, older students, quantitative F = ma.

## Who and how
Grade 11, physics (Newton's Laws). Students drive, 25 to 40 minutes. Explore first: Push Bench opens with a stone in
the hack and a push ready to run.
Topic line: "Newton's second law, F = ma".
Standards: HS-PS2-1.
tool.json: driver "students", minutes "25-40", modes ["Push Bench", "Sheet", "Notebook"].

## Screens and modes
Header (kit, 9-12 theme): "Curling Stones", small line "Push, glide, predict." Modes `Push Bench`, `Sheet`,
`Notebook`; kit `Motion`, `Sound`, `Read` (Sound starts on as the kit sets it).

Panel (all modes): three sliders with typed boxes beside them: Push force F (0 to 40 N, step 0.5, default 27),
Push time t (0.5 to 3.0 s, step 0.1, default 2.0), Stone mass m (10.0 to 25.0 kg, step 0.5, default 19.0; the legal
band 17.24 to 19.96 kg is shaded on the slider track with the label "match stones"). Readouts: friction force (μmg),
net force, acceleration, speed at release, release point. Toggles: `Predict first` (off), `Measurement noise` (off).

### Push Bench (explore, default)
Focus: the stone and its two force arrows, centred in the top 60 percent of the stage; the two plots share the rest.
Stage: a side view of the first 12 m of ice over the painted arena (cs-arena), the painted hack (cs-hack) at the
left, the near hog line at 10.06 m drawn as a thick line. The painted stone (cs-stone-side) sits in the hack with the
painted delivery stick (cs-stick) against its back, and two arrows in code: the push (accent, length proportional to
F) and ice friction (red, pointing back, length proportional to μmg, drawn at 20 times scale with the label "x20, it
is small"). Below, two engine plots sharing a time axis 0 to 4 s: "force on the stone (N)" (push, friction and net
as three step lines) and "velocity (m/s)" (a straight rising line during the push, then a gently falling one).
- `Push` (Space) runs the push in real time: the stick pushes for t seconds, the velocity line climbs, then the stick
  stops and the push arrow vanishes at release and a "released" tick drops on both plots. The run continues 1 s past
  release (at most 4 s in all), then `Follow it to the Sheet` appears.
- With `Predict first` on, `Push` is replaced by a box "Predict the acceleration (m/s²)" and `Lock in`; after the
  run the readout shows "predicted 1.32, measured 1.32".
- `Reset` (R) puts the stone back in the hack.

### Sheet
Focus: the moving stone and the house ahead of it; the camera follows the stone so it stays in the middle third, and
the house is always on screen in the last 10 m.
Stage: a top view of the full 43.9 m sheet, long and thin, on the painted pebbled ice (cs-ice, tiled), the painted
stone from above (cs-stone-top), the camera following it with a minimap strip on top showing the whole sheet. Drawn in
code: hack, near hog line, far hog line, tee line, the house (four rings), back line. A ghost stone marks "predicted
stop" (`Show prediction` toggle, off by default).
- `Throw` (Space) plays the push then the glide in real time (about 29 s for a draw: 2 s push and 27 s glide; the `x4`
  toggle makes it about 7 s).
- `Sweep` (hold the button, or hold S): while held, the painted broom heads (cs-brooms) scrub back and forth on the
  2 m strip of ice just ahead of the stone and the swept stretch is painted as a light brushed band. Sweeping lowers
  friction there (Content). The stretch counter shows "swept 8.4 m".
- Result strip after each throw: stop position from the hack, distance from the tee ("1.60 m past the tee, in the
  house"), and a rule note when one applies: "released past the hog line: removed", "stopped short of the far hog
  line: removed", "through the back line: removed".
- Cards: C1 to C5 (Content), each sets the mass and a target; `Next card`. Cards are optional; the sheet works with any
  settings.

### Notebook
Focus: plot 1, the largest thing, with the table under it.
- Table of every push and throw this session: m, F, t, friction, F_net, F_net/m, measured a, release speed v, glide
  distance, stop, swept m. `Copy table` (tab-separated), `Clear notebook`.
- Plot 1: measured a against F_net/m, with the line a = F_net/m drawn after three points (`Show the law`). Plot 2: glide
  distance after release against v², with the best line and its slope printed ("slope 5.10 m per (m/s)²").
- Two conclusion boxes (unsaved, cleared with the notebook): "What does the slope of plot 1 tell you?" and "Why does
  the glide depend on v² and not on mass?" Each opens a model answer with `Compare`.

## Content
Model (stated on screen under `How this model works`):
- During the push: net force F_net = F − μmg, a = F_net / m, v = a t, push distance d = a t² / 2.
- If F ≤ μmg the stone does not move: "Your push is smaller than friction. Nothing moves."
- After release: only friction acts, deceleration μg (the same for every mass), glide distance v² / (2μg).
- Ice: μ = 0.0100 unswept, μ = 0.0080 swept (lab settings inside the measured range 0.006 to 0.016), g = 9.81 m/s².
  Glide constant 1 / (2μg) = 5.097 m per (m/s)². Each swept meter adds 0.2 m to the stop (L_s (μ − μ_s) / μ).
- Left out (said on screen): the stone's spin and curl, air drag, the slider's own motion, ice that changes along the
  sheet. Stones go straight down the centre line.

Sheet geometry (World Curling, Rules of Curling, July 2023 edition), distances from the hack line along the centre
line: near hog line 10.059 m, far hog line 32.007 m, tee line 38.408 m, back line 40.237 m, far end 43.893 m. House
ring radii 1.829, 1.219, 0.610 and 0.152 m; stone radius 0.146 m (circumference at most 914 mm); stone mass 17.24 to
19.96 kg. Rules used: release before the near hog line; a stone must pass the far hog line to stay in play; past the
back line it is out.

Check values (F, t, m as given; stop measured from the hack):
| Case | m (kg) | F (N) | t (s) | a (m/s²) | v (m/s) | stop (m) | Note |
|---|---|---|---|---|---|---|---|
| default | 19.0 | 27 | 2.0 | 1.3230 | 2.6459 | 38.328 | 0.08 short of the tee, in the house |
| soft | 19.0 | 24 | 2.0 | 1.1651 | 2.3301 | 30.003 | short of the far hog line, removed |
| guard | 19.0 | 26 | 2.0 | 1.2703 | 2.5406 | 35.44 | guard zone |
| light | 12.0 | 17 | 2.0 | 1.3186 | 2.6371 | 38.083 | same F/m idea |
| heavy | 24.0 | 34 | 2.0 | 1.3186 | 2.6371 | 38.083 | same stop as light |
| same push, light | 12.0 | 27 | 2.0 | | | 98.71 | through the back line |
| same push, heavy | 24.0 | 27 | 2.0 | | | 23.553 | short, removed |
| short push | 19.0 | 27 | 1.0 | | | 9.582 | short, removed |
| half force | 19.0 | 13.5 | 2.0 | | | 8.871 | short, removed |
| hog violation | 10.0 | 25 | 3.0 | | | | push covers 10.809 m, past 10.059: removed |
| swept | 19.0 | 27 | 2.0 | | | 40.008 | swept 30.0 to 38.4 (8.4 m): 1.60 m past the tee |
Draw to the tee in 2.0 s needs a = 1.3244 m/s² whatever the mass: F = 17.07 N (12 kg), 24.52 (17.24), 27.03 (19.0),
28.39 (19.96), 34.14 (24). Release speed needed from the near hog line to the tee, unswept: 2.358 m/s.

Cards (Sheet):
- C1 "Draw to the button": 19.0 kg, t fixed 2.0 s. Stop within 0.30 m of the tee. Answer F 27.0 (on the 0.5 N steps
  26.5 stops 1.54 m short and 27.5 goes 1.41 m past).
- C2 "Guard": 19.0 kg. Stop between the far hog line and the front of the house (32.01 to 36.58 m).
- C3 "Same push, new stone": the default push on a 24 kg stone falls short; change only F so it reaches the house.
  Answer 33.5 to 34.5 N (the house spans F = 33.35 to 34.91 N; the stone's centre counts).
- C4 "Sweep it in": 19.0 kg, F 26, t 2.0 locked (stops at 35.44). Sweep so it reaches the house: sweep at least
  (36.58 − 35.44) / 0.2 = 5.7 m.
- C5 "Call it": random legal mass and push; type the predicted stop before `Throw`. Pass within 0.30 m.

## Interactions in detail
- Engine: exact piecewise formulas (no stepping) for the stop; the animation samples the same formulas every frame,
  so the drawn stone and the numbers always agree.
- Measurement noise on: measured a and v readouts get ±2 percent Gaussian noise (seeded per run, shown with the
  label "measured"); the stop and the motion stay exact. Off by default.
- The release point is checked against the near hog line before the glide; a violation ends the throw at release with
  the stone lifted off (removed), not a crash.
- Sweeping: Hold to sweep; the swept zone is the stone's path while held (from the stone's front edge to 2 m ahead),
  merged into strips. A stone already stopped cannot be swept. Sweeping before the stone moves does nothing. Sweep
  acts in the same frame it is pressed: the brooms appear and the predicted stop (when shown) moves at once.
- Controls stay live during a run: moving a slider, or changing mode, ends the run at once and puts the stone back in
  the hack with the new setting shown in the readouts (the run is not logged); `x4` and `Show prediction` change on the
  next frame without ending it.
- Extremes: F 0 or below friction: "Nothing moves" and no run. Very long stops are drawn to the far end, then the
  stone exits with the note.
- Sound: a low rumble that fades with speed (Web Audio filtered noise), a brush hiss while sweeping, a soft knock at
  release; off with Sound.
- Keyboard: Space = Push or Throw, S hold = Sweep, R = Reset; sliders reachable by Tab with arrows and PageUp/PageDown;
  focus({preventScroll: true}) on mode change.
- Layout by real stage pixels (like collision-lab): wide (side panel), compact (panel under stage), stack (375 wide:
  plots fold into tabs `Force` and `Velocity`).
- Mode change: `Curio.stop()`, `V.hush()`. Notebook rows and passed cards per device (localStorage
  `curio-curling-stones`, try/catch), `Clear notebook` clears both.

## Look
Accent (`--brand`) #ff7a8f, handle red (the red stone handles): 6.95:1 on --panel #141b25, 6.59:1 on --sec-bg #18202b;
--brand-ink #10161f on it 7.29:1. Collision-lab's cyan #3cc8dc is far from it; nearest 9-12 accents are unit-detective
#ff8f9e (math) and body-thermostat #e25a7e (biology); in this batch hot-meets-cold #ff8f5e is ΔE 34 away.
Scene: the painted arena and ice set the scene. Code colors over them: house rings blue #3d6fd8 and red #d84a4a,
white 4 ft ring #f6f8fb, lines #2b3440, brushed band #ffffff at 35 percent. Text on the ice uses #10161f (over 14:1
on the ice's #dfe9f1 average; the tile is checked to stay lighter than #c8d6e2). Plots: push `--gr-1`, friction
`--gr-4`, net force and velocity `--gr-3`.

## Art
Local FLUX (`scripts/localart.py`). No people anywhere: the push is a delivery stick and the sweepers are shown as
their broom heads only. 7 images.
- cs-arena: an empty indoor curling arena at night seen from ice level, a long sheet of white ice stretching away,
  low boards, dim stands and warm ceiling lights in the distance; 16:9; cutout no; people no; the Push Bench backdrop
  behind the side view of the ice.
- cs-ice: pebbled white curling ice seen straight from above, fine frozen droplets evenly spread, cool even light,
  seamless texture; 1:1; cutout no; people no; tiled under the Sheet top view (house and lines drawn in code on top).
- cs-stone-side: a gray granite curling stone with a red plastic handle, side view at ice level, studio light, on a
  plain white background; 4:3; cutout yes; people no; the stone in Push Bench.
- cs-stone-top: the same gray granite curling stone with a red handle seen straight from above, on a plain white
  background; 1:1; cutout yes; people no; the stone on the Sheet and the minimap, rotated with a slow turn while it
  glides.
- cs-stick: a curling delivery stick, a long black pole with a small gray head shaped to cup a stone handle, side view
  on a plain white background; 4:1; cutout yes; people no; pushes the stone in Push Bench, moves with it and stops at
  release.
- cs-brooms: two curling broom heads with dark fabric pads and short handles cut off at the edge, seen from above on a
  plain white background; 4:3; cutout yes; people no; shown scrubbing in front of the stone while Sweep is held
  (a small back and forth slide in code; still with Motion off).
- cs-hack: a black rubber curling hack, a low foothold block frozen into the ice, side view on a plain white
  background; 4:3; cutout yes; people no; at the left end in Push Bench.
Drawn in code: arrows, lines, house rings, brushed band, ghost stone, minimap, plots, table, preview.svg.

## Voice
`easy-coach` (Umbriel), style "Say in an easy-going, encouraging way, like a relaxed curling coach at the rink." No
grade 10 or 11 science neighbor or batch sibling uses it; lake-commons (grade 9) does. `Curio.voice`,
`scope: () => state.mode`. Hints change at once on every mode or state change; lines queue with a `valid` check.
- bench (how; Push Bench welcome; stale once Push or Lock in is pressed): "Pick a force and a time, then press Push.
  Watch the velocity line while you push."
- slope (how; after the first push ends; stale on a mode switch): "The steeper the velocity line, the bigger the
  acceleration. Net force over mass."
- nomove (event; Push or Throw with F at or below friction; stale on any slider change): "That push is smaller than
  friction. Nothing moves."
- sheet (how; Sheet welcome; stale once Throw is pressed): "Press Throw. While the stone glides, hold Sweep to make
  the ice a little slicker in front of it."
- hog (event; a hog line violation; stale on Reset or the next throw): "Let go before the hog line. That one comes
  off."
- house (event; a stop in the house; stale on the next throw): "In the house."
- button (event; a stop within 0.15 m of the tee, said instead of house; stale on the next throw): "On the button.
  Nice call."
- notebook (how; Notebook welcome; stale once Show the law is pressed): "Every push is in the table. Press Show the
  law and check if the points sit on the line."

## Family engine
Family forces. Collision-lab (built) keeps its physics in one block, `/* FORCES ENGINE: begin */ ...
/* FORCES ENGINE: end */`, as `const Forces = (() => { ... })()` with no DOM inside. This tool copies that block
unchanged and adds to it, so the block can move to `kit/forces.js` and serve the whole family:
- Already there (collision-lab): constants `GLIDER` 0.20, `TRACK` 2.00, `END_LO`, `END_HI`, `K_BACK` 50000, `DT` 1e-5,
  `AFTER` 3; `collide1D(m1, v1, m2, v2, e)` → `{v1, v2, p0, p1, ke0, ke1, vcm}`; `contactTime1D(x1, v1, x2, v2, gap)` →
  seconds or null; `airRun(s)` → `{kind: 'still' | 'none' | 'collide', ...}`; `noseRun(m, v, nose)` velocity Verlet →
  `{samples, peak, tPeak, contactTime, crushUsed, vAfter, impulse, dp, ke0, result}`.
- Added here: `G` 9.81; `netForce(list)` → `{sum, dir: -1 | 0 | 1, balanced}` for a list of signed forces in N;
  `pushRun(m, F, t, mu)` → `{moved, fr, net, a, v, d, samples: [[time, x, v]...]}` (moved false when F ≤ μmg);
  `glide(x0, v0, mu, muSwept, zones)` → `{stop, time, samples}` exact piecewise over swept zones `[[x1, x2]...]`;
  `stopFor(m, F, t, mu, muSwept, zones)` → stop position.
- Lower siblings to use it: tug-of-war-arena (grade 3) uses `netForce` for balanced and unbalanced teams and
  `pushRun` with mu for the cart; crash-test-lab (grade 8) uses `collide1D` for carts and `noseRun` for the bumper.
- Plots use `kit/graphing.js` `Plane` (step lines with `g.trace`, points with `g.point`) if present; otherwise the
  tool's own SVG.

## Sources
- Sheet layout, house rings, stone size and mass, hog line and back line rules: World Curling, "The Rules of Curling
  and Rules of Competition", July 2023 edition, rules R1, R2, R5 (sheet diagram), https://worldcurling.org/rules/ (read
  2026-10-27; distances from the hack computed from the sheet diagram).
- Ice friction range: "Friction Coefficient of Curling Stones on the Ice of the Beijing Olympic Rink", Lubricants
  10(10):265 (2022), MDPI, https://www.mdpi.com/2075-4442/10/10/265 (μ about 0.006 to 0.016). The lab values 0.0100
  and 0.0080 are settings chosen inside that range.
- Newton's second law and kinetic friction: OpenStax, University Physics Volume 1, 5.3 "Newton's Second Law" and 6.2
  "Friction", https://openstax.org/books/university-physics-volume-1/pages/6-2-friction
- g = 9.81 m/s² (rounded standard gravity 9.80665): NIST SP 330, https://www.nist.gov/pml/special-publication-330
- Number checks (Python, 2026-10-29, exact piecewise model): every row of the check table matched (default 38.328,
  soft 30.003, guard 35.44, light and heavy 38.083, 98.711, 23.553, 9.582, 8.871, hog push 10.809, swept 40.008);
  draw-to-tee forces matched; C3 house band F 33.347 to 34.915 N; C4 5 m swept stops at 36.44 (fails), 5.7 m at
  36.58 and 6 m at 36.64 (pass); C1 on 0.5 N steps only 27.0 passes. Draw timing: glide 27.0 s plus 2 s push, 29 s
  in all (was printed "15 to 25 s", fixed); x4 gives 7.2 s. Short push and half force rows now say "removed" (both
  stop short of the far hog line).

## Done when
1. Default throw (19.0 kg, 27 N, 2.0 s) reads friction 1.86 N, a 1.323 m/s², release 2.646 m/s at 2.646 m, and stops
   at 38.33 m, "0.08 m short of the tee, in the house", in about 29 s at x1.
2. 12 kg at 17 N and 24 kg at 34 N both stop at 38.08 m; 27 N on 12 kg goes through the back line, on 24 kg stops at
   23.55 m (removed).
3. 24 N on 19 kg stops at 30.00 m with "stopped short of the far hog line: removed".
4. 10 kg, 25 N, 3.0 s ends at release with "released past the hog line: removed".
5. Default throw swept from 30.0 to 38.4 m stops at 40.01 m, "1.60 m past the tee, in the house"; C4 passes with 6 m
   swept and fails with 5 m.
6. F = 1.5 N on 19 kg shows "Nothing moves" and the nomove line each time it is tried.
7. Notebook plot 1 points sit on a = F_net/m (noise off); plot 2 slope prints 5.10.
8. Predict first: a typed 1.32 shows "predicted 1.32, measured 1.32".
9. Focus: in Push Bench the stone and arrows are the largest thing at 1366x768 and in the 680x425 preview; in Sheet
   the stone stays in the middle third while it moves and the house is on screen for the last 10 m.
10. A tap while the stone glides: holding Sweep shows the brooms and starts the band in the same frame; moving a
    slider ends the run at once and resets the stone.
11. How-to lines spoken once each, then hint only; "In the house." on each throw that lands there; all 7 images load,
    none shows a person.
12. At 1366x768 the sheet, plots and controls all show; at 760 wide the panel sits under the stage; at 375 wide the
    plots fold into tabs; labels at least 10 px in the 680x425 preview; no network, no em dashes.

## Open questions
- [curling-stones] Sweeping is a simple lower μ over the swept stretch (0.0100 to 0.0080, a lab setting), no curl.
  Enough for grade 11, or add curl later as a separate idea?
- [curling-stones] Sweepers are shown as broom heads only and the push as a delivery stick, to keep people out of
  the art. Fine, or should a painted curler (people: true, Gemini, Cory's review) deliver and sweep?

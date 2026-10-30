# Zoom to the Limit

## One idea
Put any curve under a microscope and keep zooming at one point until the curve looks like a straight line; the slope
of that line is the rate of change at the point, and a secant line sliding its second point in, with a table of
average rates closing in on one number, shows the same thing from the outside (while a corner never straightens).

## Not like
- speedometer (this group): uses the derivative as a car's speed and its rules. Here there are no rules and no car: only average rates over shrinking intervals, the precalculus idea that comes first.
- hole-hunter (this group): limits of function values, holes, jumps and asymptotes. Here the limit is of slopes, and the specimens are all continuous.
- motion-graph-match (gr 11, built): position, velocity and acceleration graphs driven live. Here no motion; one point, one zoom.
- graph-story-lab (gr 9, graphing): reads key features off whole graphs. Here everything happens at one point, at powers of ten.
- size-of-everything (gr 8, explorer): zooms through scales of the universe. Here the zoom is into a curve, and the reward is straightness.

## Who and how
Grade 12, precalculus (Limits and Rates of Change). Students drive, 20 to 35 minutes. Explore first: Zoom opens on
y = x² at x = 1 with the lens ready.
Topic line: "average and instantaneous rate of change".
Standards: AP-PRECALC.U1 (1.1 change in tandem, 1.2 rates of change: the rate at a point is approximated by average
rates over small intervals, 1.3 linear and quadratic rates, 1.4 concavity from changing rates). The CCSS cluster this
serves is F-IF.B.6 (average rate of change over an interval), named here as support.
tool.json: driver "students", minutes "20-35", modes ["Zoom", "Secant", "Equal steps"].

## Screens and modes
Header (kit, 9-12 theme): "Zoom to the Limit", small line "Every smooth curve is straight up close." Modes `Zoom`,
`Secant`, `Equal steps`; kit `Motion`, `Sound`, `Read`.

Stage: the painted lab bench at night (art: lab-bench, dimmed) behind both views. One view is the whole curve on a
graphing plane (the "slide"); the other is a round lens (a circular clipped second plane) framed by a painted brass
eyepiece ring (art: lens-ring), showing the zoomed window around the point. A small square on the slide marks the lens
window (it shrinks as you zoom). Both planes from `kit/graphing.js`.

Panel top: specimen picker (a list of 10 cards, Content; the three context cards carry painted icons, art:
specimen-icons) and the point a (slider or box, within the specimen's range; the specimen's default a is preloaded).

### Zoom (explore, default)
Focus: the lens, centered and the largest thing on the stage (about 55 percent of the stage width); the slide is the
smaller view beside it.
- Zoom control: buttons `Zoom in x10`, `Zoom out x10`, and a log slider from x1 to x1,000,000; the lens animates
  (`g.view`, about 300 ms, instant with Motion off). The lens grid relabels at each scale (tick labels at the lens's
  own step).
- Straightness meter: "Looks straight" when the curve's largest gap from its own chord across the lens is under one
  pixel of the lens; otherwise "Still curved" with the gap in pixels. A corner specimen shows "Never straightens: two
  different slopes meet here."
- `Read the slope`: draws the line through the two points where the curve leaves the lens and prints its slope to 6
  significant figures with the lens width ("slope across the lens: 2.00000 (lens 0.0001 wide)").
- `Show tangent`: draws the line with the exact slope through the point on both planes (labeled with its equation).

### Secant
Focus: the slide with the secant line pivoting on (a, f(a)), now the largest view (the lens shrinks to a corner inset
that keeps the point in view); the table sits in the panel.
- A second point b on the curve, draggable (on the slide), with a secant line through (a, f(a)) and (b, f(b)).
  Readout: "average rate = (f(b) - f(a)) / (b - a) = ...", with units for context specimens.
- `Step closer` sets h = b - a to the next of 1, 0.1, 0.01, 0.001, 0.0001 (from the right); `From the
  left` toggles to h negative. Each step adds a table row: h, f(a + h), average rate (6 significant figures).
- Once the h = 0.001 row is in the table, a line under it says "These close in on ...", naming the specimen's exact
  slope to 3 significant figures; for corners and vertical tangents it says what happens instead (Content).

### Equal steps (change in tandem)
Focus: the slide with its rise bars under the curve, the largest view; the table sits in the panel.
- The curve split into equal steps of x (step size buttons `0.5`, `1`, `2`; 6 steps from a start x). Each step's rise
  is drawn as a vertical bar under the curve and listed in a table: x, f(x), change in f, change in the change.
- Line under the table, by specimen: linear "Every step rises the same: constant rate."; quadratic "The rises change
  by the same amount each step: the rate changes at a constant rate."; exponential "Each rise is the same multiple of
  the last."; otherwise "Rises growing: concave up" or "Rises shrinking: concave down" per stretch.
- Specimens for this mode add y = 3x - 2 (linear) and y = 2ˣ (exponential) to the list.

## Content
Specimens (f, default a, range of a, true slope at default a, lens unit):
| # | Specimen | f | a | true slope |
|---|---|---|---|---|
| 1 | Parabola | x² | 1 | 2 |
| 2 | Hill and valley | x³ - 3x | 1 (flat) | 0 (at a = 2: 9) |
| 3 | Growth | eˣ | 0 | 1 |
| 4 | Wave | sin x (radians) | 0 | 1 (at π/2: 0) |
| 5 | Log | ln x (a from 0.2) | 2 | 0.5 |
| 6 | Root | √x (a from 0) | 4 | 0.25 (at 0: none, vertical) |
| 7 | Corner | abs(x - 1) | 1 | none (left -1, right 1) |
| 8 | Thrown ball | h(t) = 20t - 4.9t² m | 1 s | 10.2 m/s |
| 9 | Cooling tea | T(t) = 20 + 70(0.9)ᵗ °C, t in minutes | 5 | -4.355 °C per minute |
| 10 | Savings | A(t) = 1000(1.05)ᵗ dollars, t in years | 10 | 79.47 dollars per year |
Context specimens 8 to 10 are made-up situations with stated formulas (a ball thrown up at 20 m/s on Earth; tea
cooling toward a 20 °C room; 5 percent yearly growth).

Secant tables (from the right, h = 1, 0.1, 0.01, 0.001, 0.0001):
- Parabola at 1: 3, 2.1, 2.01, 2.001, 2.0001; from the left 1, 1.9, 1.99, 1.999, 1.9999. Close-in line: 2.00.
- Thrown ball at 1: 5.3, 9.71, 10.151, 10.1951, 10.1995 (from the left 15.1, 10.69, 10.249, 10.2049). Close-in line:
  10.2.
- Growth at 0: 1.71828, 1.05171, 1.00502, 1.00050, 1.00005. Close-in line: 1.00.
- Root at 4: 0.236068, 0.248457, 0.249844, 0.249984, 0.249998. Close-in line: 0.250.
- Root at 0: 1, 3.16228, 10, 31.6228, 100: growing without bound: "No single slope: the curve stands straight up here."
- Cooling tea at 5: -4.13343, -4.33214, -4.35271, -4.35477, -4.35498. Close-in line: -4.36.
- Savings at 10: 81.4447, 79.6682, 79.4934, 79.4760, 79.4742. Close-in line: 79.5.
- Corner at 1: 1, 1, 1, 1 from the right and -1, -1, -1 from the left: "Right side and left side disagree, so there is
  no one rate here."
Lens at the corner: straightness meter never says "Looks straight"; the lens shows a V at every zoom.

## Interactions in detail
- Lens: a circular clip of a second `Plane` centered on (a, f(a)) with equal x and y scale (so the slope looks like
  itself); width 2 / zoom units at zoom x1 = width 2. At very high zoom (x1,000,000, width 2e-6) values stay in
  double precision; f is evaluated directly (no stored samples).
- Straightness: sample 64 points across the lens, compare with the chord through the two edge points, convert the
  largest gap to lens pixels.
- `Read the slope` is a secant across the lens, not the exact derivative; `Show tangent` uses the exact slope from a
  formula stored per specimen (2x, 3x² - 3, eˣ, cos x, 1/x, 1/(2√x), ±1, 20 - 9.8t, 70 ln(0.9) 0.9ᵗ, 1000 ln(1.05)
  1.05ᵗ). Corner and Root at 0 have no tangent: the button is disabled with the reason.
- Close-in line: shown once the h = 0.001 row exists (from either side), naming the stored exact slope rounded to 3
  significant figures (0 shows as "0"); never for Corner or Root at 0, which show their own lines.
- Changing a resets zoom to x1 and clears the secant table. Points outside the specimen's domain are refused (ln at 0,
  √ below 0) with the domain named.
- Numbers: 6 significant figures, true minus sign, trailing zeros dropped except in the secant table (fixed digits
  so columns line up).
- Taps while it plays: a zoom press during the 300 ms zoom animation retargets at once (the lens jumps toward the new
  scale on that frame); dragging a or b, or changing specimen, during any animation acts at once.
- Sound (on as the kit sets it): a soft lens click per x10 step; off with Sound.
- Keyboard: a and b are engine points (arrows move 0.1, Shift 0.01); zoom buttons in tab order before the table.
- Mode change: `Curio.stop()`, `V.hush()`. Nothing is saved.

## Look
Accent (`--brand`) #c6f25a, lime (a microscope highlighter): 13.39:1 on --panel #141b25, 12.69:1 on --sec-bg #18202b;
--brand-ink #10161f on it 14.05:1. Distinct from the group's leaf green (slope-field-garden) and lemon (hole-hunter) by
hue, and from every 9-12 math neighbor.
Scene: the painted lab bench at night (dark wood, cool blue window light, a warm desk lamp glow) dimmed 40 percent
behind the views; the slide plane on #0e1520 (theme) as a panel over it; the lens inside the painted brass ring with a
faint code vignette; crosshair at the point in the accent. The curve `--gr-1`, secant `--gr-2`, tangent `--gr-3` (each
with its dash pattern); labels on a #10161f chip at 85 percent (15.4:1).

## Art
Local FLUX (`scripts/localart.py`); no people. One style: precise painted illustration, cool night lab light with a
warm lamp.
- lab-bench: "A tidy science lab bench at night, dark wooden bench top, a brass microscope at the far side, glass
  slides in a small rack and a notebook with blank pages, cool blue light from a window and a warm desk lamp glow,
  precise painted illustration"; 16:9; cutout no; people no; the stage background in every mode, dimmed 40 percent.
- lens-ring: "A round polished brass microscope eyepiece ring seen straight on, a thick knurled rim around a perfectly
  round empty dark center, precise painted illustration, plain white background"; 1:1; cutout yes; people no; frames
  the lens (scaled to the lens size; the zoomed plane is clipped to its inner circle).
- specimen-icons (kit of three, one shared prompt, each "a single <piece> centered, precise painted illustration,
  plain white background"): a red rubber ball in mid-air with a faint upward motion trail; a white porcelain teacup of
  tea with a slim glass thermometer standing in it; a glass jar half full of coins with a blank paper label. 1:1;
  cutout yes; people no; sizing: each fills 80 percent of the icon square on cards 8, 9 and 10 and beside the unit
  readout in Secant.
The planes, curves, lens grid, crosshair, secant, tangent, rise bars and preview.svg are drawn in code (they are
graphs).

## Voice
`science-narrator` (Charon), style "Say in a clear, curious way, like a documentary narrator at a microscope." Not
used by a group sibling or 9-12 math neighbor. `Curio.voice`, `scope: () => state.mode`. Tables and readouts are read
on screen; Read speaks the hint.
- zoom (how, Zoom welcome; stale on the first zoom): "Press Zoom in a few times. Watch the curve in the lens straighten out."
- straight (event, the meter first reads Looks straight for a specimen and a; stale when a or the specimen changes): "Straight. The slope of this line is the rate of change right here."
- corner (event, Corner specimen zoomed past x1000; stale on a change): "Still a corner. Two different slopes meet here, so there is no one rate."
- secant (how, Secant welcome; stale on the first Step closer or drag of b): "Press Step closer. The second point slides in, and the average rates close in on one number."
- closeIn (event, the close-in line appears; stale on a change of a, side or specimen): "The average rates are closing in on one number."
- steps (how, Equal steps welcome; stale on the first step size press): "Press a step size, then compare the bars. Equal bars mean a constant rate. Growing bars mean the rate is growing."

## Family engine
Graphing (`kit/graphing.js`) used as a plotting tool (this tool is not in the graphing family): two `Plane`s (slide
and lens), `g.fn` for curves, `g.view` for the zoom, `g.point` for a and b, `g.segment` for secant, chord and step bars,
`tickFormat` for lens labels, `g.clear`.

## Sources
- Average rate of change, rate of change at a point approximated by average rates over small intervals, change in
  tandem, concavity: College Board, AP Precalculus Course and Exam Description (2023), Unit 1 topics 1.1 to 1.4,
  https://apcentral.collegeboard.org/courses/ap-precalculus
- Average rate of change: OpenStax, Precalculus 2e, 1.3 "Rates of Change and Behavior of Graphs",
  https://openstax.org/books/precalculus-2e/pages/1-3-rates-of-change-and-behavior-of-graphs
- Gravity 9.8 m/s² (the ball's -4.9t² term): NIST, standard acceleration of gravity 9.80665 m/s²,
  https://physics.nist.gov/cgi-bin/cuu/Value?gn
- The tea and savings situations are made up.
- Checks run (Python, 2026-10-29): every secant row in Content recomputed to 6 significant figures (rows for h = 0.0001
  added). Exact slopes: tea 70 ln(0.9)(0.9⁵) = -4.35500, savings 1000 ln(1.05)(1.05¹⁰) = 79.4740. The first draft
  showed the close-in line "once the last two rates agree to 3 significant figures"; tested on every specimen, that
  rule never fired for Hill and valley at 1 or at 2 (slopes 0 and 9: 9.006 then 9.0006), would fire on the Corner's
  right side (1, 1) without its special case, and with a 0.5 percent band named 79.49 for savings and -4.36 or -4.35 for tea depending on the side. The line now
  appears at the h = 0.001 row and names the stored exact slope. Straightness with a 300 px lens: parabola gap 15, 1.5,
  0.15 px at x10, x100, x1,000 (straight at x1,000; a 150 px lens is straight at x100); savings 0.29 px and Hill and
  valley at 2 0.90 px at x1,000; Corner 148 px at every zoom. Read the slope across a x1,000 lens on x² at 1: 2.00000.
  Equal steps x² step 1 from 0: rises 1, 3, 5, 7, 9, 11; 2ˣ: 1, 2, 4, 8, 16, 32.
- Contrast ratios in Look computed with the WCAG 2.1 formula.

## Done when
1. Zoom on x² at 1: after x1,000 the meter reads "Looks straight" and Read the slope gives 2.000 (to 4 figures).
2. Corner at 1 never reads "Looks straight", even at x1,000,000; Show tangent is disabled with its reason.
3. Secant on x² at 1: rows 3, 2.1, 2.01, 2.001; from the left 1, 1.9, 1.99; "These close in on 2.00" appears with the
   h = 0.001 row.
4. Thrown ball at 1 s closes in on 10.2 m/s with units in the readout; Hill and valley at 2 closes in on 9.00.
5. Root at 0: secant rates 1, 3.16228, 10, 31.6228 and the "stands straight up" line, never a close-in line.
6. Equal steps on x² with step 1 from 0: rises 1, 3, 5, 7, 9, 11 and changes of change all 2; on 2ˣ rises double.
7. ln at a = 0 or √ at a = -1 is refused with the domain named.
8. Focus: at 1366x768 and 1000x625 the lens is the largest thing on the stage in Zoom, and the slide is in Secant and
   Equal steps; the brass ring fits the lens at every size.
9. Tap while it plays: pressing Zoom in x10 three times fast lands at x1,000 with no lag; dragging a during a zoom
   animation moves the point at once.
10. How-to lines spoken once each in five actions; "Straight." spoken each new specimen it happens on; no line names a
    control that is not on screen.
11. Lens and slide side by side at 1366x768 and 1280x720 with controls visible; at 760 wide the lens sits above the
    slide; lens text at least 10 px in the 680x425 preview; no network, no em dashes.

## Open questions
- zoom-to-the-limit: the module's only code is AP-PRECALC.U1; this spec also names F-IF.B.6 as the CCSS cluster it
  serves. Add F-IF.B.6 to the module, or leave the code list as is?

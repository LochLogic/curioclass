# Polar Rose Studio

## One idea
A pen arm sweeps around the center like a clock hand while its length follows r = f(θ), so roses, cardioids and
spirals draw themselves stroke by stroke; every point the pen touches is a complex number r(cos θ + i sin θ), and
stamping your drawing by multiplying, adding or conjugating complex numbers turns one curve into a kaleidoscope.

## Not like
- imaginary-island (gr 11, map): complex arithmetic as travel on an island map, one point at a time. Here the whole curve is made of complex numbers and arithmetic stamps copies of an artwork; the focus is graphing r = f(θ).
- ferris-wheel (gr 11): a circle traced as height over time (sine wave). Here the radius itself changes with the angle.
- image-transformer (this group): any 2x2 matrix moves a picture. Here only complex multiplication (turn and scale), addition (shift) and conjugation (mirror), applied to a drawing you made.
- function-family-reunion (this group): y = f(x) transformations with sliders. Here polar equations and a sweeping pen.
- cone-slicer (Conic Focus Finder, this group): curves from a distance rule; here curves from an angle rule.

## Who and how
Grade 12, precalculus (Polar Coordinates and Complex Plane). Students drive, 20 to 40 minutes. Explore first: Studio
opens with a 4-petal rose drawing itself.
Topic line: "polar graphs and complex numbers".
Standards: N-CN.B (N-CN.4 polar and rectangular forms of the same number, N-CN.5 adding, multiplying and conjugating
on the plane, N-CN.6 distance and midpoint with the Ruler), AP-PRECALC.U3 (3.13 to 3.15: polar coordinates, polar
function graphs, rates of change in polar functions read off the sweep).
CCSS per mode: Studio N-CN.4 (pen readout); Stamps N-CN.5; Ruler N-CN.6.
tool.json: driver "students", minutes "20-40", modes ["Studio", "Stamps", "Gallery"].

## Screens and modes
Header (kit, 9-12 theme): "Polar Rose Studio", small line "Draw with r and θ." Modes `Studio`, `Stamps`, `Gallery`;
kit `Motion`, `Sound`, `Read`.

Stage: a square polar canvas (radius 6 units to the edge), as tall as the stage allows and centered, black velvet
background, faint polar grid (circles every 1, rays every 15°, labels at 0°, 90°, 180°, 270° and on the circles 2, 4,
6), the real axis and imaginary axis labeled "Re" and "Im". The pen: a thin arm from the center to the pen tip, with
an angle arc showing θ. When a limaçon reaches past the edge (a + b > 6), the canvas zooms out to radius 9 or 12 and
labels the circles to match ("zoomed out" shows in a corner); every other family fits radius 6.

### Studio (explore, default)
Focus: the polar canvas with the sweeping pen and the curve, center stage and largest; the curve, pen and ink controls
are in the panel.
Panel:
- "Curve": family buttons `Rose`, `Limaçon`, `Spiral`, `Circle`, `Lemniscate`; the equation in large type, for
  example "r = 4 cos(2θ)". Sliders per family (Content). `cos` / `sin` toggle where it applies.
- "Pen": `Draw` (sweeps θ from the start to the closing angle in 4 s; instant with Motion off), `Pause`, a θ slider to
  scrub the pen by hand, and the readout: θ (degrees and radians), r, rectangular (x, y) and complex x + yi, plus
  polar form r(cos θ + i sin θ). When r < 0 the tip is drawn hollow at the opposite side and the readout adds "r is
  negative, so the point is on the opposite side, at θ + 180°."
- "Ink": six ink colors, line width (2, 4, 6 px), `Add layer` (keeps the drawn curve and starts a new one; up to 6
  layers), `Remove layer`, layer list.
- Readouts: petal count (roses with whole-number k), "closes after θ = ...".
- `Ruler` toggle: tap two points of the drawing; shows z1, z2, distance |z1 - z2| and midpoint (z1 + z2)/2.

### Stamps
Focus: the canvas with the stamp's live preview drawn over the tile, center stage and largest; the stamp cards in the
panel.
The current layers become the "tile". Stamp cards (each previews at once; `Apply` bakes it into a new layer):
- `Turn`: copies the tile n times (n 2 to 12), each multiplied by w = cos(360°/n) + i sin(360°/n). Shows w in both forms
  and "multiplying by w adds 360°/n to every angle and keeps every distance".
- `Spiral`: copies k times (k 2 to 24), each multiplied by w = s(cos α + i sin α), s from 0.70 to 1.00, α from 5° to 90°.
  Shows "each copy: distance x s, angle + α". Copy j has modulus s^j.
- `Mirror`: adds the conjugate of every point (reflection across the real axis).
- `Shift`: adds a complex number c (drag c on the canvas; snaps to 0.5) to every point.
The stamp list shows what was applied, in order, with `Undo stamp`.

### Gallery
Focus: the grid of design thumbnails, center stage; tapping one shows it large on the canvas with `Open`.
Up to 12 saved designs on this device (localStorage `curio-polar-rose-studio`, try/catch): thumbnail, equations and
stamps. `Save`, `Open`, `Delete`, `Clear gallery`, and `Download PNG` (the canvas at 1200 x 1200, made in the page,
a file saved by the browser). Also six starter designs (Content) that can be opened but not deleted.

## Content
Families, sliders and closing angle (all angles in the equation are in radians inside the math, shown in degrees on
the pen readout):
- Rose: r = a cos(kθ) or a sin(kθ). a 0.5 to 6 (step 0.5), default 4. k: whole 1 to 12, or with `Fraction k` on,
  k = p/q with p and q 1 to 7. Draw θ from 0 to 2π for whole k; 0 to 2qπ for k = p/q in lowest terms (always closes).
  Petals for whole k: k when k is odd, 2k when k is even (k = 1 is a circle: "1 petal, a circle").
- Limaçon: r = a + b cos θ (or sin). a and b 0 to 6. Readout of shape: b = 0 circle; a < b inner loop; a = b cardioid;
  b < a < 2b dimpled; a ≥ 2b convex. 0 to 2π.
- Spiral: r = aθ, a 0.1 to 1 (step 0.05), turns 1 to 6, θ from 0 to turns x 2π; drawing stops at the canvas edge.
- Circle: r = 2a cos θ (or sin), a 0.5 to 3: a circle of radius a through the center. Plus r = c (c 0.5 to 6).
- Lemniscate: r² = a² cos(2θ) (or sin), a 1 to 6; draws r = ±a√cos(2θ) where cos(2θ) ≥ 0 and skips the rest; note:
  "No points where cos 2θ is negative."
Default on load: Rose, a = 4, k = 2, cos (4 petals).
Starter designs: "Eight petals" r = 5 cos 4θ; "Five star" r = 5 sin 5θ with Turn n = 2; "Heart" r = 3 - 3 sin θ;
"Snail" r = 0.25θ, 3 turns, Spiral stamp s = 0.9, α = 30°, k = 12; "Bloom" r = 4 cos(5θ/3); "Mirror bow"
r² = 25 cos 2θ with Shift c = 0 + 2i and Mirror.
Ruler worked case on r = 4 cos 2θ: tap the point at θ = 0 (r = 4, the number 4) and the point at θ = 270° (r = 4 cos 540°
= -4, so it lands at 90°: the number 4i). Distance √32 ≈ 5.66, midpoint 2 + 2i.

## Interactions in detail
- Point for θ: x = r cos θ, y = r sin θ, sampled every 0.5° (finer, 0.1°, when |dr/dθ| is large, so tips stay sharp).
  Readouts to 2 decimals; θ to 1 decimal degree and 3 decimal radians; "π" forms shown for multiples of 15°
  (θ = 90° shows "π/2").
- Pen speed: the sweep is constant in θ, so the tip visibly speeds up where r changes fast; a small "dr/dθ" readout
  (exact from the formula) shows the rate, and its sign says "moving away from the center" or "toward".
- The 4 s Draw never blocks: during it every slider, family button, toggle and ink stays live. A curve change redraws
  the new curve at once up to the pen's current θ and the sweep carries on from there; `Pause` stops the pen where it
  is; grabbing the θ slider takes the pen by hand; changing mode stops the sweep and shows the whole curve.
- Stamps operate on stored points (complex numbers), never on pixels, so they stay crisp. Total points are capped at
  200,000; a stamp that would pass it is disabled with "Too many copies for one drawing; remove a layer."
- Spiral stamp copies that fall under 0.05 units are skipped.
- Fraction k uses lowest terms (gcd), so 4/2 draws as 2/1.
- Lemniscate and limaçon readouts handle a = 0 and b = 0 (a point, or a circle) with their own labels.
- Download PNG: canvas `toBlob`, filename "polar-rose-<date>.png"; nothing leaves the page except the download.
- Keyboard: θ slider steps 1° (Shift 15°); family buttons and stamps in tab order before the layer list.
- Mode change: `Curio.stop()`, `V.hush()`; the drawing stays.

## Look
Accent (`--brand`) #ff8ab6, rose pink: 7.9:1 on --panel #141b25, 7.5:1 on --sec-bg #18202b, 9.0:1 on the velvet;
--brand-ink #10161f on it 8.3:1. Not used by any 9-12 math neighbor; in this group fuchsia (identity-proof-race) is
bluer and darker.
Canvas: velvet #0b0a12, grid rgba(255,255,255,0.08), labels #a6b3c4 (8.1:1). Inks: rose #ff8ab6, gold #ffd166, mint
#7ee0c3, sky #7cc4ff, lilac #c9a0ff, white #f2f2f2 (each over 7:1 on the velvet). Ink choice is never the only cue:
each layer is listed by number and equation.

## Art
none: drawn in code. The whole stage is a polar graph and the student's own drawing: the grid, the pen arm whose
length changes every frame, the curves, the stamped copies and preview.svg (a glowing 8-petal rose) are diagram and
artwork made from the math, so a painted image would only cover them.

## Voice
`smooth-narrator` (Algieba), style "Say smoothly and warmly, like an artist talking through a sketch." Not used by a
group sibling, a 9-12 math neighbor or another spec in batch R05. `Curio.voice`, `scope: () => state.mode`. Readouts
are read on screen; Read speaks the hint.
- studio (how, Studio welcome; stale once Draw is pressed or a slider moves): "Pick a curve, then press Draw. The pen sweeps around while r grows and shrinks."
- negative (how, first time r goes negative under the pen; stale on a family change): "When r is negative, the point lands on the opposite side of the center."
- petals (how, first k change on a rose; stale on a family change): "Odd k gives k petals. Even k gives twice as many."
- stamps (how, Stamps welcome; stale once a stamp card is picked): "Pick a stamp card to preview it, then press Apply. Multiplying turns and stretches, adding shifts, and conjugating mirrors."
- turn (how, first Turn preview; stale once Apply is pressed): "Multiplying by w adds its angle to every point and keeps every distance."
- gallery (how, Gallery welcome; stale once Save or Open is pressed): "Press Save to keep this design, or tap a starter and press Open."
- saved (event, a design saved; stale after 3 s): "Saved to the gallery."
- full (event, a stamp refused for too many points; stale on any change): "That's too many copies for one drawing. Remove a layer first."

## Family engine
none (polar canvas; it does not use the graphing plane).

## Sources
- Polar coordinates, conversion, rose petal rule (k odd: k petals; k even: 2k), limaçon shapes, lemniscates, spirals:
  OpenStax, Precalculus 2e, 8.3 "Polar Coordinates" and 8.4 "Polar Coordinates: Graphs",
  https://openstax.org/books/precalculus-2e/pages/8-4-polar-coordinates-graphs
- Polar form of complex numbers, multiplying multiplies moduli and adds arguments, conjugate as reflection:
  OpenStax, Precalculus 2e, 8.5 "Polar Form of Complex Numbers",
  https://openstax.org/books/precalculus-2e/pages/8-5-polar-form-of-complex-numbers
- Standards: CCSS Math N-CN.B, https://www.thecorestandards.org/Math/Content/HSN/CN/ ; College Board, AP Precalculus
  CED (2023), Unit 3 topics 3.13 to 3.15.
- Closing angle for r = cos(pθ/q): cos(p(θ + 2qπ)/q) = cos(pθ/q + 2pπ), so 2qπ always closes (worked here).
- Checks run (Python, 2026-10-29): petals counted from the drawn points (distinct tips at full radius) for k = 1 to 12:
  1, 4, 3, 8, 5, 12, 7, 16, 9, 20, 11, 24, matching the rule; sin 3θ also gives 3. Pen at θ = 90° on r = 4 cos 2θ: r = -4
  at (0, -4). Ruler: 4 and 4i, distance 5.657, midpoint 2 + 2i. Turn n = 6: w = 0.5 + 0.866i. 0.9^11 = 0.314. k = 2/3
  closes at 6π. Largest r: the Heart starter reaches 6.00 and the 3, 3 cardioid 6, so they fit; but limaçon a = 5, b = 2
  (a Done when case) reaches 7 and a = b = 6 reaches 12, past the radius 6 canvas, so the canvas now zooms out to 9 or
  12 for limaçons. Limaçon labels for (2, 4), (3, 3), (5, 2), (3, 2): inner loop, cardioid, convex, dimpled. Point
  counts per curve stay far under the 200,000 cap (a 6-turn spiral is 4,320 samples; a 1/7 rose 5,040).

## Done when
1. Load shows r = 4 cos(2θ) and Draw makes 4 petals; k = 3 makes 3, k = 4 makes 8; k = 1 says "a circle".
2. Pen at θ = 90° on r = 4 cos 2θ reads r = -4, hollow tip at the bottom (0, -4), complex -4i, with the negative-r note.
3. Limaçon a = 2, b = 4 says inner loop; a = b = 3 says cardioid; a = 5, b = 2 says convex and the canvas zooms out so
   the whole curve shows.
4. Fraction k = 2/3 draws a closed curve over 0 to 6π; k = 4/2 is treated as 2.
5. Turn with n = 6 makes 6 copies; w reads 0.5 + 0.866i and "60°". Mirror on r = 3 sin 3θ gives a drawing symmetric
   across the real axis.
6. Spiral s = 0.9, α = 30°, k = 12: the last copy's points are 0.9^11 ≈ 0.31 times as far out.
7. Ruler between 4 and 4i shows distance 5.66 and midpoint 2 + 2i.
8. Save, reload, Open restores the design; Clear gallery empties it; Download PNG produces a file.
9. Focus: at 1366x768 and 1000x625 the canvas is the largest thing on the stage in Studio and Stamps, and centered.
10. Tap while it plays: halfway through Draw, changing k redraws the new rose at once and the pen keeps sweeping;
    `Pause` stops the pen at once.
11. How-to lines spoken once each in five actions; nothing is spoken on every slider move; no line names a control
    that is not on screen.
12. Main controls visible without scrolling at 1366x768; at 375 wide the canvas fits the width; no network; no em
    dashes.

## Open questions
- polar-rose-studio: Download PNG saves a file on the student's device. Fine, or keep only the on-device gallery?

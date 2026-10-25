# Field Lines

## One idea
Twin boards: one layout of objects drawn twice, as gravity on the left and as electric field on the right, so you see
that both laws fall off as one over r squared, and that the only real difference is that charge comes in two signs
and mass comes in one.

## Not like
- circuit-builder: also a grade 11 sandbox, but it is current in wires; here there are no wires, only empty space and
  the fields around objects.
- space-cargo: forces there are pushes you apply with contact; here the force reaches across empty space and you
  read a field, not apply a push.
- collision-lab: momentum in contact events; nothing here ever collides as a scored event.
- roller-coaster-physics: energy along a track; no energy bookkeeping here.
- spectrum-explorer: moving EM waves; this tool is static fields only.
- elements-inspector: atom structure and properties; Field Lines only uses a proton and an electron as one data pair.

## Who and how
- Grade 11, science (physics). Driver: students (often alone on a laptop), also works on a projector.
- 10 to 25 minutes. Standard: HS-PS2-4 (use Newton's law of gravitation and Coulomb's law to describe and predict the
  gravitational and electrostatic forces between objects).
- Pure explore. No score, no timer, no win state. 9-12 look: link `kit:curio` then `kit:theme-912`, dark instrument
  panel, no confetti or mascot.
- Accents set on this tool (check AA contrast on the 9-12 panel color; adjust lightness only if it fails):
  gravity amber `#E8B54A`, positive charge red `#FF6E61`, negative charge blue `#62AEFF`, field lines `#C9D3E3`.
  Color is never the only signal: charges always show "+" or "-" glyphs, masses show "m".

## Screens and modes
Header: title "Field Lines", subtitle "Gravity and Electrostatics", mode buttons (`.seg`) "Twin boards", "Spread",
"Real pairs", then the kit icon buttons Motion, Sound, Read (ids `motion`, `sound`, `read`). Default mode: Twin boards.

### Twin boards (default)
- Stage: two square boards side by side, each 12 by 12 board units with a faint 1 unit grid. Left title "Gravity
  (mass)", right title "Electric (charge)". Below 720px wide they stack, gravity on top.
- Every object exists on both boards at the same spot. It has a size from 1 to 5 that is its mass on the gravity board
  and the size of its charge on the electric board. On the electric board it also has a sign. Gravity draws it as an
  amber disc labeled "m 3"; electric draws it red "+3" or blue "-3". Disc radius = 0.25 + 0.08 x size units.
- One probe: a small white ring with a crosshair, present on both boards at the same spot. It is a test mass on the
  left and a small positive test charge on the right.
- Panel (right side, `.panel`), top to bottom:
  - Add buttons: "Add +", "Add -" (both add an object of size 2 near the board center, offset so it does not overlap).
  - Selected object controls (shown only when one is selected): "Smaller", "Bigger", "Flip sign", "Remove", and a
    readout "Size 3, mass 3, charge +3".
  - View toggles (`aria-pressed`): "Field lines" (on), "Arrow grid" (off), "Strength shading" (off).
  - Probe readout (mono font): "Gravity field here: 0.42 units, pointing in" style lines for each board, plus
    "Distance to selected: 3.0 units". If nothing is selected it uses the nearest object.
  - Probe buttons: "Double distance", "Halve distance", "Release probe", "Clear paths".
  - Presets: "Single", "Like pair", "Opposite pair", "Big and small", "Row of three", "Clear all".
  - Hint paragraph (id `hint`), which changes with what was last done (texts in Content).

### Spread
- Stage left: the classic spreading diagram drawn in code in a simple oblique 3D view. A point source at the left, 36
  straight lines fanning out in a square pyramid, and a square screen you move with the "Distance" slider (1 to 5,
  step 0.5). The screen is drawn as an r by r grid of tiles (r squared tiles), so at distance 1 it is 1 tile, at 2 it
  is 4 tiles, at 3 it is 9 tiles. The lines that pass through one tile are highlighted.
- Stage right: a plot of strength against distance (r from 0.5 to 6). The curve 36 / r squared drawn solid, the
  current point marked. Toggle "Show one over r" adds a dashed 36 / r curve for comparison.
- Panel: "Distance" slider, readouts "Area: 4 tiles", "Lines per tile: 9", "Strength: 1/4 of distance 1". Buttons
  "Gravity", "Electric" (`.seg`) switch the formula card text and the source color (amber mass or red charge), and
  nothing else, because the shape is identical. Toggle "Show one over r". Hint paragraph.
- Formula card (on screen text, symbols allowed): Gravity "g = G M / r^2, G = 6.674 x 10^-11 N m^2 / kg^2";
  Electric "E = k q / r^2, k = 8.988 x 10^9 N m^2 / C^2".

### Real pairs
- Stage: two horizontal bars on one shared log scale from 10^-70 N to 10^40 N (tick every 10 powers), "Gravity force"
  (amber) and "Electric force" (red/blue striped), each with its value in newtons in scientific notation at the bar
  end. Above the bars, a line drawing of the pair (two circles and a distance arrow labeled with the distance).
  Below, the ratio line in large text.
- Panel: five pair buttons (Content), the distance readout, buttons "Double distance", "Halve distance", "Reset
  distance". A short "Why" note for the selected pair. Hint paragraph.

## Content

### Twin boards presets (board units, origin at top left, size, sign)
- Single: (6, 6) size 3 +. Probe at (9, 6).
- Like pair: (4, 6) size 3 +, (8, 6) size 3 +. Probe at (6, 6), the zero point.
- Opposite pair: (4, 6) size 3 +, (8, 6) size 3 -. Probe at (6, 8.5).
- Big and small: (4.5, 6) size 5 +, (9, 6) size 1 +. Probe at (6.5, 8).
- Row of three: (3, 6) size 2 +, (6, 6) size 2 -, (9, 6) size 2 +. Probe at (6, 9).
- Clear all: no objects; probe stays where it is.
- On first load: Opposite pair (it shows the difference at once).

### Hint texts (Twin boards)
- Start: "Same objects, two laws. Drag the probe and compare the two readouts."
- After any object is set negative: "On the left, every mass pulls. Gravity looks exactly like a world where every
  charge is negative: all lines point in."
- After Opposite pair, or two objects of opposite sign: "The electric board shows a dipole: lines run from plus to
  minus. The gravity board shows two masses that both pull."
- After Like pair or the probe near a zero point (both fields under 2 percent of the strongest object field at
  distance 1): "Between two equal pulls there is a spot where they cancel. The field reads zero here."
- After Double distance: "Twice as far, one quarter the field. Both boards obey one over r squared."
- After Halve distance: "Half as far, four times the field."
- After Release probe: "Starting from rest, the probe follows the field. Gravity only ever pulls it in."
- When the probe would pass a disc edge on Double distance: "That would put the probe off the board. Move it closer
  first."
- Field-line note (shown once, under the toggles): "Line spacing on a flat screen is a sketch. In 3D the lines spread
  over a sphere, so trust the readout and the Spread mode for strength."

### Twin boards physics (board units)
- Each object i at p_i with size s_i and sign c_i (+1 or -1). Gravity field at x: sum of s_i / r^2 pointing toward
  p_i. Electric field at x: sum of c_i x s_i / r^2 pointing away from p_i when c_i is +1. Same constant (1) on both
  boards so like-shaped pictures match exactly.
- Inside a disc (r under its radius), use r = radius so values stay finite.
- Readouts round to 2 decimals; under 0.005 shows "0.00, the pulls cancel" (gravity) or "0.00, the fields cancel"
  (electric). Direction words: "pointing in" when the field at the probe points toward the nearest object, else
  "pointing out", and for the general case also an arrow glyph drawn in the readout row.
- These are board units, labeled "units" everywhere; the panel says "Board units. Real values are in Real pairs."

### Spread numbers
36 lines. Lines per tile = 36 / r^2: r 1 gives 36, 1.5 gives 16, 2 gives 9, 2.5 gives 5.76, 3 gives 4, 3.5 gives
2.94, 4 gives 2.25, 4.5 gives 1.78, 5 gives 1.44. Strength readout as a fraction of distance 1: show "1/4", "1/9",
"1/16", "1/25" at whole numbers, else a decimal to 3 places ("0.444"). Area readout: r squared tiles to 2 decimals.

### Real pairs (constants in Sources; computed live, not hard coded, so Double and Halve stay exact)
G = 6.6743 x 10^-11 N m^2 / kg^2; k = 8.9875517923 x 10^9 N m^2 / C^2; e = 1.602176634 x 10^-19 C; proton mass
1.67262192 x 10^-27 kg; electron mass 9.1093837 x 10^-31 kg.
1. Hydrogen atom: proton and electron, 5.29 x 10^-11 m (Bohr radius). Gravity 3.63 x 10^-47 N, electric 8.24 x 10^-8 N,
   attract. Ratio "Electric is 2.27 x 10^39 times stronger." Why: "This electric pull is what holds the atom together.
   Gravity is far too weak to matter."
2. Two protons: 1.0 x 10^-15 m apart (about the size of a nucleus). Gravity 1.87 x 10^-34 N, electric 231 N, repel.
   Ratio "Electric is 1.24 x 10^36 times stronger." Why: "Two protons push apart. Something stronger than both,
   the strong nuclear force, holds a nucleus together."
3. Two 1 kg balls, 1 m apart, each given 1 microcoulomb of extra charge. Gravity 6.67 x 10^-11 N, electric 8.99 x
   10^-3 N, repel. Ratio "Electric is 1.35 x 10^8 times stronger." Why: "Even a small extra charge beats the gravity
   between everyday objects."
4. Earth and a 1 kg apple at Earth's surface: Earth mass 5.972 x 10^24 kg, distance 6.371 x 10^6 m (mean radius).
   Gravity 9.82 N. Electric shown as "about 0: both are neutral overall" with no bar. Ratio line "Gravity wins
   here." Why: "This is the apple's weight. Matter is almost perfectly neutral, so its charges cancel out."
5. Earth and Moon: Moon mass 7.346 x 10^22 kg, 3.844 x 10^8 m apart. Gravity 1.98 x 10^20 N. Electric "about 0".
   Ratio line "Gravity wins here." Why: "Gravity is weak but it only adds up. Charge cancels, so at the scale of
   planets gravity is the force that is left."
- Distance steps: Double and Halve multiply or divide by 2, limited to 1/8 and 8 times the starting distance (button
  disables at the limit). Forces update; the ratio line never changes, and a small note appears after the first
  step: "Both forces changed by the same factor. The ratio stayed the same."
- Number format: 3 significant figures, "2.27 x 10^39" with a real superscript on screen.

## Interactions in detail
- Drag objects and the probe on either board with pointer; the twin moves too. Objects and probe stay inside the
  board. Dropping an object on another nudges it to the nearest free spot (no overlap). The probe cannot sit inside
  a disc: it is pushed to the disc edge.
- Click selects an object (ring highlight on both boards). Keyboard: Tab moves through objects then the probe; arrow
  keys move 0.25 units (Shift: 1 unit); "+" and "-" change size; "S" flips sign; Delete removes. Escape deselects.
- Limit 6 objects. At 6, the Add buttons disable and the hint says "Six objects is the limit. Remove one to add more."
  Size stops at 1 and 5 (buttons disable at the ends).
- Flip sign changes only the electric board. The gravity board does not change at all, and a 300 ms pulse on the
  gravity disc reminds that mass has no sign (no pulse when Motion is off).
- Field lines: seed 6 lines per size unit evenly around each object, traced with fixed steps (RK4, step 0.05 units) in
  the field direction for positives and against it for negatives. A line stops when it reaches another disc, leaves
  a 2 unit margin around the board, or reaches 2000 steps. A line seeded from a negative charge that ends on a
  positive is dropped (it is already drawn from the positive). Gravity board traces as if every object were negative.
  Arrowheads every 2 units along each line. Redraw on every move, throttled to animation frames.
- Arrow grid: 13 by 13 arrows. Length is the log of strength, capped at 0.8 units; brightness also scales with strength.
- Strength shading: a soft heat map of log strength, the same scale on both boards.
- Double distance: moves the probe along the line from the selected (or nearest) object to twice its current
  distance; Halve moves it to half, but never inside the disc. Readouts show the change, such as "x 0.25".
- Release probe: the probe starts at rest at its spot, both boards at once, and moves with acceleration equal to the
  field (unit mass, unit test charge), small time step. Each path is drawn as a trail in that board's color. A path
  stops when it touches a disc ("landed"), leaves the board ("escaped"), or after 8 seconds. Readout lists the end
  for each board, for example "Gravity: landed on m 3. Electric: escaped." If the field at the start is 0, the probe
  stays and the hint says "The probe sits still: the pulls cancel here." With Motion off, both full paths appear at
  once. The probe goes back to its start spot afterward; "Clear paths" removes trails. Moving anything clears trails.
- Spread: slider and keyboard arrows; the screen, tiles, highlighted lines and plot point move together. With Motion
  off the screen jumps instead of gliding.
- Real pairs: pair buttons switch everything at once; the distance arrow in the drawing stretches visually (log of
  the distance step, so the drawing stays on screen).
- Mode changes call `Curio.stop()`. Each mode keeps its own state while you switch. "Clear all" is the reset for
  Twin boards; reloading the page restores Opposite pair. Nothing is saved except the kit's Motion setting.

## Art
none: drawn in code (boards, discs, field lines, spreading diagram, plot, bars and pair drawings are all SVG or canvas).

## Voice
Bank "hs-narrator", voice "Kore", style "Read clearly and naturally, at a moderate pace". Welcome lines play once per
mode the first time it opens (after the first tap); the rest play on the named trigger. Read reads the hint.
1. tb-welcome (Twin boards opens): "Welcome to Field Lines. Each object has a mass and a charge. The left board shows its gravity, and the right board shows its electric field."
2. tb-howto (after tb-welcome): "Drag the objects to move them. Drag the small ring, the probe, to read the field at any spot."
3. tb-negative (first time any object is negative): "Mass comes in only one sign, so gravity always pulls. Charge comes in two, so it can push or pull."
4. tb-double (first Double distance): "Twice as far away, the field is one quarter as strong, on both boards."
5. tb-release (first Release probe): "The probe starts at rest. Watch where each field sends it."
6. tb-zero (first time the probe reads zero): "Here the pulls cancel, and the field is zero."
7. sp-welcome (Spread opens): "Here is why both laws use one over r squared. The same lines spread out over more area as you move away."
8. sp-two (slider first reaches 2): "At twice the distance, the lines cover four times the area, so each patch gets one quarter of them."
9. rp-welcome (Real pairs opens): "Now with real numbers. Pick a pair and compare the gravity and electric forces between them."
10. rp-ratio (first Double or Halve): "Both forces changed by the same factor, so the ratio between them did not change."
11. rp-hydrogen (Hydrogen atom chosen the first time): "In a hydrogen atom, the electric pull is about two times ten to the thirty nine times stronger than gravity."
12. rp-earthmoon (Earth and Moon chosen the first time): "Earth and the Moon are neutral overall, so their charges cancel and gravity is the force that is left."

## Family engine
none (no forces engine exists). Keep the field math, line tracer and probe integrator in one clearly marked block
("FIELD ENGINE") so it can move to a kit file later. For the Spread plot, use `kit/graphing.js` (Plane, fn, point)
if it exists when this tool is built; otherwise draw the plot in that same tool block.

## Sources
- G, k, e, proton and electron mass, Bohr radius: NIST CODATA 2018 recommended values, https://physics.nist.gov/cuu/Constants/
- Earth mass 5.9722 x 10^24 kg, mean radius 6371.0 km: NASA Earth Fact Sheet, https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
- Moon mass 0.07346 x 10^24 kg, mean Earth to Moon distance 384,400 km: NASA Moon Fact Sheet, https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html
- Nucleus scale about 10^-15 m: OpenStax College Physics 2e, section 31.1, https://openstax.org/books/college-physics-2e/pages/31-1-nuclear-radioactivity
- Field direction conventions (lines leave positive charges, gravity field points toward mass) and the inverse square
  spreading argument: OpenStax University Physics Volume 2, sections 5.4 and 5.6, and Volume 1, section 13.2,
  https://openstax.org/details/books/university-physics-volume-2
- Derived values (forces and ratios in Real pairs) are computed from the constants above: hydrogen 8.24 x 10^-8 N and
  3.63 x 10^-47 N, ratio 2.27 x 10^39; proton pair ratio 1.24 x 10^36; apple 9.82 N; Earth and Moon 1.98 x 10^20 N.
- HS-PS2-4: NGSS, https://www.nextgenscience.org/pe/hs-ps2-4-motion-and-stability-forces-and-interactions

## Done when
1. On load, Opposite pair shows: gravity board with two amber "m 3" discs and all lines pointing in; electric board
   with a "+3" and a "-3" and lines running from plus to minus.
2. Dragging an object or the probe on one board moves it on the other; readouts update while dragging.
3. Flip sign changes only the electric board; the gravity board picture stays identical.
4. With Single, probe at distance 2 then Double distance: both readouts drop to one quarter (within rounding) and show "x 0.25".
5. Like pair with the probe at (6, 6) reads 0.00 on both boards; Release probe there leaves it still with the cancel hint.
6. Release probe in Opposite pair: the gravity trail lands on a disc; the electric trail moves away from the plus toward the minus.
7. Spread at distance 3 shows 9 tiles, "Lines per tile: 4", strength 1/9, and the plot point sits on the solid curve.
8. Real pairs: Hydrogen shows 8.24 x 10^-8 N and 3.63 x 10^-47 N; after Double distance both values are one quarter and the ratio line is unchanged.
9. Earth and Moon shows 1.98 x 10^20 N gravity and "about 0" electric with "Gravity wins here."
10. Keyboard alone can select, move, resize, flip and remove objects; Motion off makes Release draw paths instantly; no
    em dashes or network requests in the file.

# Imaginary Island

## One idea
Every spot on an island map is a complex number, and arithmetic is travel: adding walks you a fixed step, multiplying by i swings you a quarter turn around the harbor, and multiplying by any complex number turns you by its heading and stretches you by its distance.

## Not like
- transformation-golf: that rotates shapes onto a twin in the fewest moves; here there is no shape and no move count, and the turn is a side effect of ordinary multiplication you can read off the arithmetic.
- image-transformer: that applies 2x2 matrices to a photo; here a single complex number does the turning and stretching, and no matrix appears.
- ferris-wheel: that turns rotation into a sine graph of height over time; here rotation is the operation itself, with no time axis or wave.
- polar-rose-studio: that draws curves from polar equations; here heading and distance are readouts of one point, never a curve.
- rollercoaster-polynomials: that builds a polynomial from its real zeros; Springs here only shows where a quadratic's two solutions land, and its point is the complex case where they leave the real line.

## Who and how
Grade 11, math (Algebra 2, module Complex Numbers). Driver: students, on their own laptops; also projects well. 15 to 25 minutes.
Standards: N-CN.A.1, N-CN.A.2, N-CN.C.7. Touches the plus standards N-CN.A.3 (conjugate, modulus) and N-CN.B.4, N-CN.B.5 (complex plane, operations as geometry) without requiring them.
Look: 9-12 dark instrument theme (`kit:curio` then `kit:theme-912`), styled as a night nautical chart. Own `--brand` accent: a sea teal. No confetti, no mascot.
tool.json modes: ["Explore", "Clue Trail", "Springs"].

## Screens and modes
Header: title "Imaginary Island" with subtitle "Complex numbers as places", mode buttons (`.seg`) **Explore**, **Clue Trail**, **Springs**, then **Motion**, **Sound**, **Read** (ids `motion`, `sound`, `read`). Explore is the default and needs no instructions.

Layout: stage on the left (the map, SVG, scaled with `Curio.fit`), panel on the right (stacks below the map under 900 px wide). The panel's hint paragraph has id `hint`.

### The map (all modes)
- Square chart, default view x and y from -7 to 7. Horizontal axis is the **Real Road** (labeled "Real Road (real part)"), vertical axis is the **Imaginary Road** (labeled "Imaginary Road (imaginary part)"). They cross at the **Harbor** (0).
- Tick labels every 1 unit: 1, 2, 3 on the Real Road; i, 2i, 3i on the Imaginary Road (and negatives). At wider zooms, label every 5 or 10.
- The island is drawn in code (see Content). Sea outside it: dark navy with faint wave hatching.
- Layer toggles under the map, each a 44 px button with aria-pressed: **Grid** (on), **Landmarks** (on), **Distance rings** (off: circles about the harbor at radius 1 to 10, labeled 1 to 10), **Heading spokes** (off: lines from the harbor every 30 degrees, labeled 0, 30, ... 330), **Trail** (on).
- Zoom: **Zoom in** and **Zoom out** buttons, mouse wheel and pinch. View half-widths: 3, 5, 7, 10, 15, 25, 50. Dragging empty map pans. **Fit** returns to the default view.

### Explore
On screen: the **traveler** (a round lantern marker, 44 px hit area) starting at 1 (the Lighthouse), a dashed **rope** from the Harbor to the traveler, and the **step marker w** (a diamond, different shape and color from the traveler) starting at 1 + i, drawn as an arrow from the Harbor.
Panel, top to bottom:
1. Readout: "Traveler z = 3 + 2i", "Distance from harbor |z| = 3.61", "Heading 33.7°", and the landmark name when z sits on one ("You are at the Orchard").
2. Step readout: "w = 1 + i, |w| = 1.41, heading 45°".
3. Operation buttons: **× i**, **× (-1)**, **× (-i)**, **Reflect** (conjugate), **Square it**, **+ w**, **× w**.
4. Worked line: the last operation written out with the i² step shown (see Content, "Worked lines").
5. The i-power dial: four cells "i¹ = i", "i² = -1", "i³ = -i", "i⁴ = 1". Each press of × i in a row lights the next cell and shows, for example, "× i pressed 6 times in a row: i⁶ = i² = -1". Any other operation, drag or Undo resets the run to 0.
6. **Undo** (one position back, up to 50), **Reset** (traveler to 1, w to 1 + i, trail cleared, dial cleared, view to Fit), **Snap** cycle button: "Snap: whole", "Snap: half" (default), "Snap: off" (0.01).
7. Hint (id `hint`): "Drag the lantern, then try × i a few times. Turn on Distance rings to see what stays the same."

### Clue Trail (optional practice)
On screen: the same map; the traveler parked at the clue's start; w hidden. Panel: "Clue 3 of 12", the clue text, and its steps as a numbered list.
The student clicks the map to drop a **guess pin** (an X marker, draggable, snaps to the Snap setting, arrow keys move it). Buttons: **Walk it** (disabled until a guess exists), **Previous clue**, **Next clue**, **Show the arithmetic** (reveals each step's worked line without walking).
Walk it: the traveler performs each step in order with the Explore animation and worked lines, then a line from guess to landing and the result: "Your guess was 0 away. Landed it." (within 0.25) or "Your guess was 2.24 away. The trail ends at -2 + 3i, the Fox Den." A quiet tally under the clue: "Landed 4 of 6 tried". No timer, no stars; only `Curio.yes()` on a landing.
Hint: "Tap the map where you think the clue ends, then press Walk it."

### Springs (quadratics with complex solutions)
On screen: the map with the Real Road highlighted, a faint vertical **spring line** at real part -b/2, and two **spring** markers (water-drop shapes, labeled r1 and r2 with values). Inset at the top-left of the stage (about 30 percent of its width): the graph of y = x² + bx + c, x from -8 to 8, y from -10 to 20, real roots marked where it crosses the x-axis.
Panel: the equation "x² + bx + c = 0" with live values, sliders **b** (-6 to 6, step 0.5, default 0) and **c** (-4 to 13, step 0.5, default -4), the discriminant "b² - 4c = 16", a status line, the worked quadratic formula, six preset buttons (see Content), and **Reset** (b = 0, c = -4).
Responds: as c rises past b²/4 the two springs slide together along the Real Road, meet at -b/2, then split straight north and south along the spring line as a mirror pair. The inset parabola lifts off the x-axis at the same moment.
Hint: "Raise c slowly and watch the springs meet, then leave the road."

## Content

### Landmarks (name, value, note shown on hover or focus)
| Name | Value | Note |
|---|---|---|
| Harbor | 0 | Every turn is centered here. |
| Lighthouse | 1 | One step east. |
| Bell Tower | i | One step north. |
| Old Pier | -1 | One step west. |
| Fern Well | -i | One step south. |
| Summit | 1 + i | Highest point. |
| Twin Rocks | 2i | |
| Sea Arch | -4 | On the west shore. |
| Orchard | 3 + 2i | |
| Fox Den | -2 + 3i | |
| Salt Flats | -3 - 2i | |
| Waterfall | 2 - 3i | |
| Hidden Cove | -3 + 2i | |
| Cave | 4 + i | |
| Hermit Hut | -1 + 4i | |
| Shipwreck | -4 - i | |
| Tide Pools | 1 - 4i | |
| Black Sand Beach | 5 - 3i | On the southeast shore. |
| Far Buoy | 13 | Out at sea. |

Hidden patterns (not announced; Distance rings make them visible): Orchard, Fox Den, Salt Flats and Waterfall are 3 + 2i after 0, 1, 2 and 3 quarter turns, all at distance 3.61 (square root of 13). Cave, Hermit Hut, Shipwreck and Tide Pools do the same for 4 + i, all at distance 4.12 (square root of 17).
Landmark glyphs drawn in code: simple icons (tower, bell, well, peak, rocks, arch, tree, den, flats, falls, cove, cave, hut, wreck, pools, beach, buoy), each with its text name, so color is never the only signal.

### Island shape
Coastline in polar form about the Harbor: r(theta) = 5.3 + 0.7 sin(3 theta + 0.5) + 0.35 cos(5 theta), sampled every 2 degrees and smoothed. The builder may tune the constants so that Sea Arch (-4) and Black Sand Beach (5 - 3i) sit on the shore (within 0.4 of the line), every other landmark except Far Buoy is inland by at least 0.3, and Far Buoy is at sea. Fill: muted green with a sandy beach band 0.3 wide; if the terrain image exists it fills the island, clipped to the coastline.

### Worked lines (format)
- × i: "(3 + 2i) × i = 3i + 2i² = 3i - 2 = -2 + 3i"
- × (-1): "(3 + 2i) × (-1) = -3 - 2i"
- × (-i): "(4 + i) × (-i) = -4i - i² = -4i + 1 = 1 - 4i"
- Reflect: "conjugate of (3 + 2i) = 3 - 2i (mirror across the Real Road)"
- Square it: "(1 + i)² = 1 + 2i + i² = 1 + 2i - 1 = 2i"
- + w: "(-2 + 3i) + (6 - 2i) = 4 + i (walk 6 east, 2 south)"
- × w: "(4 + i)(1 - i) = 4 - 4i + i - i² = 4 - 3i + 1 = 5 - 3i", then a second line "Turned by -45° and stretched by 1.41".

Number display: up to 2 decimals, trailing zeros dropped, -0 shown as 0, "1i" as "i", "-1i" as "-i", "0 + 2i" as "2i", "3 + 0i" as "3", and a negative imaginary part written "3 - 2i", not "3 + -2i". In worked lines, wrap negative factors in parentheses.
Heading: degrees counterclockwise from east, 0 to under 360, one decimal. Turn amounts in the × w line use -180 to 180. At the Harbor: "Heading: none (you are at the harbor)".

### Clues (start, steps, end)
1. Start at the Lighthouse (1). × i. Ends at i, Bell Tower.
2. Start at the Lighthouse (1). × i, then × i again. Ends at -1, Old Pier.
3. Start at the Orchard (3 + 2i). × i. Ends at -2 + 3i, Fox Den.
4. Start at the Orchard (3 + 2i). × (-1). Ends at -3 - 2i, Salt Flats.
5. Start at the Cave (4 + i). × (-i). Ends at 1 - 4i, Tide Pools.
6. Start at the Fox Den (-2 + 3i). Add 6 - 2i. Ends at 4 + i, Cave.
7. Start at the Summit (1 + i). Square it. Ends at 2i, Twin Rocks.
8. Start at Twin Rocks (2i). Square it. Ends at -4, Sea Arch.
9. Start at the Cave (4 + i). Multiply by 1 - i. Ends at 5 - 3i, Black Sand Beach.
10. Start at the Salt Flats (-3 - 2i). Reflect across the Real Road. Ends at -3 + 2i, Hidden Cove.
11. Start at the Orchard (3 + 2i). Multiply by its conjugate, 3 - 2i. Ends at 13, Far Buoy. After the walk: "A number times its conjugate is always real: its distance squared."
12. Start at the Hermit Hut (-1 + 4i). × i four times. Ends at -1 + 4i, Hermit Hut. After the walk: "Four quarter turns is a full circle."

Clue text format: "Start at the Orchard. Multiply by i. Where do you end up?"

### Springs presets (button label, b, c, roots)
- **x² - 4 = 0**: b 0, c -4, roots 2 and -2 (two real springs).
- **x² - 2x + 1 = 0**: b -2, c 1, root 1 twice (one double spring, at the Lighthouse).
- **x² + 1 = 0**: b 0, c 1, roots i and -i (Bell Tower and Fern Well).
- **x² + 4 = 0**: b 0, c 4, roots 2i and -2i (Twin Rocks and its mirror).
- **x² - 2x + 2 = 0**: b -2, c 2, roots 1 + i and 1 - i (Summit and its mirror).
- **x² + 6x + 13 = 0**: b 6, c 13, roots -3 + 2i and -3 - 2i (Hidden Cove and Salt Flats).

Status lines: discriminant above 0: "Two real solutions: both springs sit on the Real Road." Equal to 0: "One repeated solution: the springs meet at -b/2." Below 0: "No real solutions. The parabola misses the x-axis, so the springs leave the road as a conjugate pair."
Worked formula, for b = -2, c = 2: "x = (2 ± √(4 - 8)) / 2 = (2 ± √(-4)) / 2 = (2 ± 2i) / 2 = 1 ± i". Monic quadratics only (a = 1); say so under the sliders: "Leading coefficient fixed at 1."

## Interactions in detail
- Traveler, w and guess pin: pointer drag, or focus plus arrow keys (one snap step, 0.1 when Snap is off; Shift moves 1). Readouts update on every frame of a drag.
- Keyboard shortcuts in Explore when the map has focus: I = × i, R = Reflect, S = Square it, A = + w, M = × w, U = Undo. Listed in a small "Keys" line under the buttons.
- Animations (900 ms, ease in-out): × i and × (-i) sweep the traveler along a circular arc of radius |z| through +90 or -90 degrees while the rope sweeps with it; × (-1) sweeps 180 degrees counterclockwise; × w and Square it follow a spiral that interpolates heading linearly (by the turn amount, shortest signed angle for × w, the start heading again for Square it) and distance geometrically from start to end; + w walks a straight line while a ghost copy of the w arrow is drawn from the start point; Reflect slides straight across the Real Road. The path stays on the map as a trail segment labeled with its operation.
- Motion off (`body.calm` / `Curio.reduce`): the traveler jumps, but the same arc, spiral or line is drawn at once as a dashed trail so the geometry still shows.
- Operation buttons are disabled while an animation runs; extra presses are ignored, not queued.
- Trail: last 12 segments kept, older ones fade. Trail off hides them; Reset clears them.
- At the Harbor: × anything and Square it leave the traveler at 0 with the note "0 times anything is 0. The harbor turns in place." w at 0: × w sends the traveler to the harbor with the same note.
- Far out: if a result leaves the view, the view zooms out to the next half-width that fits (up to 50). Beyond 50, the traveler is pinned to the map edge with an arrow and its value. If |z| would exceed 10,000, the operation is refused: "Too far out to chart. Try Undo, Reflect or Reset." Square it with |z| under 1 pulls toward the harbor; below 0.005 snap to 0.
- Rounding: round stored values to 6 decimals after each operation so four × i presses return exactly to the start.
- Landmark match: "You are at the ..." when the traveler is within 0.05 of a landmark.
- Clue Trail: changing clues clears the guess pin and trail. Walk it again replays the walk. The tally counts each clue once, at its first walk. The landing check is the distance from guess to the true end.
- Springs: sliders step 0.5 by arrow keys with visible values. Roots come straight from the formula; a discriminant within 1e-9 of 0 counts as 0. Springs glide between slider values (jump when Motion is off). The view fits both springs (half-width at least 7). Traveler and w are hidden here; landmarks stay, and a spring on a landmark shows its name.
- Mode switch: `Curio.stop()`; each mode keeps its state for the session (Explore position, current clue, slider values).
- Read: reads the current mode's hint.
- Resize: the map scales to fit; the panel stacks below at narrow widths; targets stay 44 px or larger.

## Art
- island-terrain: "Top-down painted map texture of an island interior, gentle green hills, small groves of trees, winding dirt paths, muted night-time colors, no text, no labels, no buildings, no people"; aspect 1:1; cutout no; people no. Optional: the tool must look finished with the code-drawn fill if this image is dropped.

Everything else (sea, coastline, landmark icons, markers, inset graph) is drawn in code.

## Voice
Bank "hs-narrator", voice "Kore", style "Read clearly and naturally, at a moderate pace". Each line plays once per session at its trigger.
1. (Explore, first entry) "Welcome to Imaginary Island. Every spot on this map is a complex number. Drag the lantern anywhere to read its address."
2. (Explore, after the first drag) "East and west is the Real Road. North and south is the Imaginary Road. The harbor is zero."
3. (Explore, first press of times i) "Times i swings you a quarter turn counterclockwise around the harbor. Your distance stays the same."
4. (Explore, dial first reaches i squared) "Two quarter turns make a half turn, to the opposite side. That is why i squared is negative one."
5. (Explore, dial first reaches i to the fourth) "Four quarter turns bring you all the way around. So i to the fourth power is one."
6. (Explore, first plus w) "Adding is walking. The step w moves you the same distance and direction from anywhere on the island."
7. (Explore, first times w) "Multiplying by w turns you by its heading and stretches you by its distance from the harbor."
8. (Explore, first Reflect) "The conjugate flips the sign of the imaginary part. On the map, it is a mirror across the Real Road."
9. (Clue Trail, first entry) "Clue Trail. Read the clue, tap where you think it leads, then press Walk it to check."
10. (Clue Trail, first walk of clue 11) "A number times its conjugate is always real. It equals its distance from the harbor, squared."
11. (Springs, first entry) "Springs. Slide b and c, and watch where the two solutions of the quadratic come up."
12. (Springs, first time the discriminant goes negative) "The parabola no longer touches the x-axis, so the solutions leave the Real Road. They come up as a mirror pair, one north and one south."

## Family engine
None for the map: the map, travel animations and complex arithmetic live in one clearly marked block ("COMPLEX PLANE MAP") so they can be lifted to a kit file later. The Springs inset parabola uses `kit/graphing.js` (`Plane`, `g.fn`, `g.roots`) if it exists when this tool is built; otherwise it is drawn in the same self-contained block.

## Sources
- Common Core State Standards for Mathematics, High School Number and Quantity, N-CN.A.1 to A.3, N-CN.B.4 to B.5, N-CN.C.7: https://www.thecorestandards.org/Math/Content/HSN/CN/
- Definition of i, adding and multiplying complex numbers, conjugates: OpenStax, College Algebra 2e, section 2.4 "Complex Numbers": https://openstax.org/books/college-algebra-2e/pages/2-4-complex-numbers
- Quadratic formula and complex solutions for a negative discriminant: OpenStax, College Algebra 2e, section 2.5 "Quadratic Equations": https://openstax.org/books/college-algebra-2e/pages/2-5-quadratic-equations
- Complex plane, modulus, argument, and multiplication as multiplying moduli and adding arguments: OpenStax, Precalculus 2e, section 8.5 "Polar Form of Complex Numbers": https://openstax.org/books/precalculus-2e/pages/8-5-polar-form-of-complex-numbers
- Landmark values, clues and presets are arithmetic computed in this spec; no outside facts.

## Done when
1. Explore works with no instructions: dragging the lantern updates z, |z| and heading live, and landing on 3 + 2i says "You are at the Orchard".
2. Four presses of × i from 3 + 2i visit Fox Den, Salt Flats and Waterfall and return exactly to 3 + 2i; each worked line shows the i² = -1 step and the dial cycles i, -1, -i, 1.
3. × w with w = 1 - i from 4 + i lands on 5 - 3i (Black Sand Beach) with the worked line and "Turned by -45° and stretched by 1.41".
4. With Motion off, every operation jumps but still leaves its arc, spiral or line as a dashed trail.
5. Square it at 0 stays at 0 with the harbor note; repeated Square it from 3 + 3i zooms out, then pins to the edge, then refuses past 10,000 without breaking.
6. All 12 clues end at their listed values and landmarks; a guess within 0.25 reports "Landed it" and the tally counts each clue once.
7. In Springs, the x² + 6x + 13 = 0 preset puts the springs on Hidden Cove and Salt Flats; with b = 0, sliding c from -4 to 13 shows the springs meet at 0 when c = 0 and split north and south after, as the inset parabola leaves the x-axis.
8. Every control works by keyboard with visible focus, targets are 44 px or larger, and no layer or marker relies on color alone.
9. The file is one self-contained HTML under 2 MB with no network requests, usable in a 16:10 iframe and full screen.
10. Each voice line plays once at its trigger, never before the first tap, and stops on mode change.

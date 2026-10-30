# Circuit Builder

## One idea
You are the power plant: build a circuit, then crank a generator to light it, and watch every bulb you add make the crank slow down because the current you draw pushes back on the magnet.

## Not like
- field-lines: static gravitational and electric fields from placed masses and charges, no circuits; here the only field shown is the magnetic one made by a current (compass) and the one that makes a current (generator).
- electromagnet-lab (grade 8): uses current to make a pulling coil; here the coil is spun to make current, and the load's back torque is the point.
- power-grid-tycoon: a city's grid economics (cost, emissions, mix); here it is one hand-cranked generator and one board, all physics, no money.
- sound-studio: a scope of sound waves you mix; the trace here is the generator's EMF, locked to the coil's angle as you turn it.
- collision-lab, space-cargo, roller-coaster-physics: mechanics only; the only mechanics here is the crank's torque and speed.
- rube-goldberg-workshop (grade 4): chains energy conversions for fun; here one conversion (your work to electrical energy) is measured in watts.
- Real-world comparator, PhET Circuit Construction Kit: also a resistor/bulb/battery board; ours adds the generator whose speed is set by the load, and a compass for Oersted's result.

## Who and how
Grade 11, physical science (Electricity and Magnetism). Driver: students (own laptops), also fine on a projector.
10 to 30 minutes. Standards: HS-PS2-5 (current makes a magnetic field; a changing magnetic field makes a current),
HS-PS3-5 (forces and energy changes in field interactions). tool.json modes: [] (pure sandbox).
Look: link `kit:curio` then `kit:theme-912`; accent in Look below. Readouts use the theme's readout font. No
celebration of any kind. Sound starts on as the kit sets it.

## Screens and modes
Header: `.seg` mode buttons **Board** and **Inside the generator**; then **Motion**, **Sound**, **Read** (kit ids).
Both modes solve the same circuit live; switching modes never pauses or resets it.

### Board (default)
Focus: the board, the largest thing on screen and in the centre; the crank box is second, at the top of the panel
whenever a generator is placed.
- Stage: the painted work mat (cb-mat) with a grid of 10 columns by 6 rows of node dots drawn in code (fixed design
  1000 x 620, `Curio.fit`). Parts sit on the edges between neighboring nodes (one part per edge), each shown as its
  painted cutout (Art) laid along the edge.
- Parts tray along the bottom of the stage, one button each with its painted part: **Wire**, **Battery**,
  **Resistor**, **Bulb**, **Switch**, **Ammeter**, **Generator**, **Compass**, **Erase**. The chosen one stays
  pressed (aria-pressed).
- Voltmeter: a red probe and a black probe (painted) parked at the tray's right end. Drag either onto any node. The
  voltmeter readout shows V(red) minus V(black); parked or floating probe shows "--".
- Panel (right): the generator crank (only while a generator is on the board), **Starters** dropdown (see Content),
  the hint line, an inspector for the selected part, a power summary, and a **Things to try** list.
- Panel buttons: **Clear board** (asks "Clear the board?" with **Clear** / **Keep**), **Flip** and **Delete** (in the
  inspector), **Replace bulb** (on a burned-out bulb), toggle **Current: Conventional | Electrons**.

### Inside the generator
Focus: the cutaway, the largest thing, on the left two thirds of the stage; the strip chart is beside it.
- Stage left: a large cutaway of the generator: two painted magnet poles (N red, S blue, the letters in code) with
  straight field lines between, a rectangular coil that rotates with the crank, and either slip rings or a split-ring
  commutator (whichever is set). Coil, rings and field lines are drawn in code (they turn in 3D and change density).
  Field lines through the coil are drawn denser or thinner with the flux through it (proportional to cos of angle).
- Stage right: a strip chart, 4 seconds wide, of EMF (volts) and current from the generator (amps) against time,
  plus a dial showing coil angle. A vertical marker shows "now".
- Panel: the same crank control, sliders **Turns** (50, 100, 200, 400) and **Magnet** (0.1, 0.2, 0.4 tesla),
  toggle **Output: AC (slip rings) | DC (commutator)**, readouts, and a live line of the formula with numbers:
  "EMF = N B A omega sin(theta) = 200 x 0.2 T x 0.008 m^2 x 18.8 rad/s x 0.71 = 4.3 V".
- If there is no generator on the board, the stage shows the generator idle and the hint says to place one on the
  Board; the button **Add a generator** places one using the "Generator" starter.

## Content
Grid nodes are (column, row), columns 0 to 9 left to right, rows 0 to 5 top to bottom. A part goes "A to B".
For battery and generator, A is the minus terminal and B is plus. Ammeter reads positive when current flows A to B.

Parts (model values, shown in the inspector):
- Wire: 0.001 ohm (shown as 0).
- Battery: EMF 1.5, 3, 4.5, 6, 9 or 12 V (inspector buttons), default 6 V; internal resistance 0.2 ohm. Any number.
- Resistor: 5, 10, 20, 50 or 100 ohm (inspector buttons), default 10 ohm. Its color bands for the value are drawn in
  code over the painted blank body.
- Bulb: 10 ohm, rated 6 V and 3.6 W. Treated as a constant resistance (a real filament's resistance rises as it heats;
  the inspector says so in one line: "Real bulbs change resistance as they heat. This one is kept at 10 ohms.").
- Switch: open (no connection) or closed (0.001 ohm); click it, or Enter, to toggle. Placed open.
- Ammeter: 0.001 ohm, reads current with sign.
- Generator: at most one. EMF = N B A omega sin(theta) (AC) or N B A omega |sin(theta)| (DC). Coil area A = 0.008 m^2
  (8 cm by 10 cm), default N = 200, B = 0.2 T, so N B A = 0.32 V s. Internal resistance 1 ohm.
- Compass: at most one, placed on a wire, ammeter or resistor edge. Sits 1 cm under the part.

Crank model (model values; keep in one marked block):
- Coil and crank share angle theta and speed omega. Flywheel inertia 0.002 kg m^2. Bearing friction 0.002 N m s
  times omega. Speed capped at 6 rev/s.
- Electrical back torque = (EMF / omega) x generator current, which equals N B A sin(theta) x I (AC) or
  N B A |sin(theta)| x I (DC). This is what slows the crank as the load draws more current.
- Hand torque: maximum 1.0 N m. Two ways to crank:
  1. Drag the crank handle around in circles: hand torque = 0.5 N m per radian the handle lags the pointer,
     clipped to 1.0 N m. Under heavy load the handle visibly falls behind the pointer.
  2. **Hold to crank** button (or hold Space): applies the **Effort** slider's torque (0 to 100 percent of 1.0 N m,
     default 20 percent) for as long as it is held. Released, the crank coasts down.
- Readouts in the crank box: speed (rev/s and rad/s), EMF (V), generator current (A), hand torque bar labeled
  "Your effort", mechanical power in (torque x omega, W), electrical power out (W).
- Expected feel at 20 percent effort, 200 turns, 0.2 T (same for AC and DC): with the switch open the crank spins up
  to the 6 rev/s cap ("max"); one bulb settles near 4.8 rev/s (4.6 to 5.0 within a turn) and 9.6 V peak; two bulbs in
  parallel near 3.0 rev/s and 6.2 V peak; a short circuit nearly stalls it, near 0.6 rev/s.

Compass model: field from the part's current B = mu0 I / (2 pi r), r = 0.01 m, mu0 = 4 pi x 10^-7 T m/A, added to
Earth's horizontal field taken as 20 microtesla pointing screen-up (north). Wire is above the compass. Direction by the
right-hand rule: screen up is north, right is east, toward the viewer is up. Current flowing north makes the needle's
north end swing west. The needle shows the vector sum; the inspector shows wire field, Earth field and angle.

Starters dropdown (loading one replaces the board; the hint names it):
1. Blank.
2. One bulb: loop of wires around (1,1), (5,1), (5,4), (1,4); battery 6 V on (1,3) to (1,2); bulb on (3,1)-(4,1).
3. Series bulbs: same loop; battery 6 V on (1,3) to (1,2); bulbs on (2,1)-(3,1) and (3,1)-(4,1); ammeter (5,2) to (5,3).
4. Parallel bulbs: top rail wires (1,1) to (6,1), bottom rail (1,4) to (6,4); battery 6 V on (1,3) to (1,2) with wires
   (1,4)-(1,3) and (1,2)-(1,1). Rung at column 3: wire (3,1)-(3,2), bulb (3,2)-(3,3), wire (3,3)-(3,4). Rung at column 5:
   switch (open) (5,1)-(5,2), bulb (5,2)-(5,3), wire (5,3)-(5,4). Ammeter on the bottom rail (2,4) to (1,4).
5. Mixed: Parallel bulbs starter with its switch closed, plus a bulb in place of the top rail wire (1,1)-(2,1).
6. Generator: One bulb starter with the generator in the battery's place, plus a rung at column 4 like starter 4's
   column 5 rung (open switch (4,1)-(4,2), bulb (4,2)-(4,3), wire (4,3)-(4,4)), so closing the switch adds a parallel bulb.
7. Short circuit: One bulb starter, plus wires (3,1)-(3,2) and (4,2)-(4,1) and an open switch (3,2)-(4,2) labeled
   "Short". Closing it bypasses the bulb.
8. Voltage divider: loop as in One bulb; battery 9 V on (1,3) to (1,2); 100 ohm on (2,1)-(3,1); 50 ohm on (4,1)-(5,1);
   red probe on (4,1), black probe on (1,4).
9. Oersted: loop as in One bulb; battery 3 V on (1,3) to (1,2); 5 ohm resistor on (3,4)-(4,4); open switch (3,1)-(4,1);
   compass on the right wire (5,2)-(5,3). Closed, the current is about 0.58 A, wire field about 12 microtesla, needle
   about 30 degrees.

Things to try (plain list, no checkboxes, no scoring):
- Put two bulbs in series, then in parallel. Which pair is brighter, and why?
- Use the ammeter at three places in a series loop. What do you notice?
- Use the voltmeter across each bulb in Series bulbs. Add the readings.
- Load Generator. Crank at 20 percent effort, then close the switch. What happened to the crank's speed?
- Switch the generator to AC and crank slowly. Why does the bulb flicker?
- Double the turns. What happens to the EMF at the same speed?
- Load Oersted. Flip the battery. What does the compass do?
- Close the short. Compare the power the battery delivers with and without it.

## Interactions in detail
- Placing: choose a part, click or tap an edge (hit area at least 44 px wide around the edge). Clicking an occupied edge
  with a part chosen replaces it. Drag from a node with Wire chosen to lay wires along every edge the pointer passes.
  With Erase, click or drag across edges to remove parts. To select a part, press Escape (or click the pressed tray
  button again) to clear the tool, then click the part; the selected part gets a focus ring and fills the inspector.
  Clicking a switch toggles it whatever tool is chosen.
- Painted parts on the board: each cutout is scaled to span its edge (aspect kept) and rotated 0, 90, 180 or 270
  degrees to match the edge and its A to B direction; Flip turns it 180. The switch swaps between its open and closed
  cutouts; a burned-out bulb swaps to cb-bulb-broken; the compass needle and the crank are separate cutouts that
  rotate.
- Keyboard: arrow keys move an edge cursor; Enter places the chosen part or toggles a switch; Delete removes; F flips;
  letters choose parts (W wire, B battery, R resistor, L bulb, S switch, A ammeter, G generator, C compass, E erase);
  Escape clears the tool. Probes: Tab to a probe, arrows move it node to node.
- Solver (one marked block): every frame, nodal analysis on the conductance matrix. Batteries and the generator are
  Norton sources (EMF over internal resistance, in parallel with that resistance). Add 1e-9 siemens from every node to a
  reference so floating parts solve to 0 V. Gaussian elimination is plenty (60 nodes). Parts on edges with no closed path
  carry 0 A. The generator uses its instant EMF each frame; all parts are resistive, so this is exact.
- Everything stays live while the crank turns: placing, erasing or switching a part changes the current, the glow and
  the crank's load in the same frame; Turns, Magnet and Output change the EMF at once.
- Current display: dots move along each part at a speed proportional to its current (60 px/s per amp, capped at
  400 px/s; under 1 mA no dots). Conventional shows amber dots in the + to minus direction outside the source; Electrons
  shows blue dots the other way and a hint line "Electrons drift the other way, much slower than this." Motion off: dots
  stop and each part shows a still arrow whose thickness scales with current.
- Bulbs: glow (drawn in code over the painted bulb) tracks power with a 0.1 s lag; full glow at 3.6 W, whiter halo
  above. Burnout uses the power averaged over the last 0.5 s, so AC ripple alone never trips it: over 9 W averaged,
  the bulb burns out: it swaps to the broken cutout, becomes an open circuit, the inspector says "Burned out: over 9 W",
  and **Replace bulb** restores it. A 12 V battery across one bulb (13.8 W) burns it out; 9 V (7.8 W) does not. The
  generator cannot burn out a bulb (at the 6 rev/s cap one bulb averages 6.0 W).
- Short circuit: any part over 5 A gets an orange glow and a chip "Short circuit: X A" by the source; Curio.tone low
  buzz once if Sound is on. Nothing explodes. The battery inspector shows power wasted inside it (I squared r).
- Inspector for a selected part: type, value buttons where it has them, voltage across, current through, power, and
  for sources power delivered. Units switch to mA under 0.1 A and mV under 0.1 V. Values update every 0.1 s on screen
  (solver runs every frame). AC readings also show "average over 1 s" under the live number.
- Power summary: total delivered by sources, total used by resistors and bulbs, and their difference (internal losses),
  so energy accounting closes.
- Generator: removing it stops the crank box. At 6 rev/s cap the speed readout shows "max". Open circuit: crank spins
  easily and coasts down slowly.
- Mode switch, Starters and Clear board call Curio.stop. Starters do not keep the crank speed (it resets to 0).
  Board state is not saved (no localStorage beyond the kit's Motion setting).
- Extremes: a board with no source shows all 0; two batteries opposing each other solve normally; a battery shorted by a
  plain wire shows about 30 A at 6 V (6 / 0.2) and the short chip.

## Look
Accent `--brand` #8fa0ff, spark blue (an electric arc): 7.12:1 on --panel #141b25, 6.75:1 on --sec-bg #18202b;
--brand-ink #10161f on it 7.47:1. Changed from copper #d98a4a, which sat only ΔE 15 from hot-meets-cold's #ff8f5e in
this batch; ΔE 57 from motion-graph-match #36c9dd and 56 from collision-lab, over 40 from every other R15 accent.
Scene: the painted green work mat; node dots #c8d0dc, wires #d8dde4 two px, amber current dots #ffb547, electron dots
#6fb7ff, short glow #ff8a4a. Strip chart: EMF `--gr-1`, current `--gr-3`.

## Art
Local FLUX (`scripts/localart.py`). No people anywhere. 16 images.
- cb-mat: a dark green rubber electronics work mat seen straight from above, faint scuffs and soft even light; 16:10;
  cutout no; people no; the Board stage under the code grid.
- Parts kit (one shared prompt line, each piece a separate cutout, people no): "a single electronics lab part seen
  straight from above on a plain white background, soft even light, blank surfaces", pieces: cb-battery (a battery
  holder with one large cylindrical cell in a plain blue wrapper, 16:9), cb-resistor (a plain beige resistor body with
  two straight wire leads, 4:1; bands in code), cb-bulb (a small round clear glass bulb with a thin coiled filament
  in a black screw socket, 1:1), cb-bulb-broken (the same bulb with a snapped filament and smoky gray glass, 1:1),
  cb-switch-open (a copper knife switch on a small wooden base with its blade raised, 16:9), cb-switch-closed (the same
  knife switch with its blade pressed down into the clip, 16:9), cb-ammeter (a small analog meter in a black case
  with a blank white dial face, 1:1; needle and number in code), cb-compass (a brass pocket compass case with a plain
  white face, 1:1), cb-needle (a slim red and white compass needle on a tiny brass pivot, 1:1; rotates), cb-generator
  (a hand-crank generator: a small gray metal box with a round hub on one side, 1:1), cb-crank (a steel crank arm
  with a round wooden handle at one end and a hub at the other, 1:1; rotates about the hub), cb-probe-red and
  cb-probe-black (a meter probe with a pointed steel tip and a red, or black, plastic handle, 1:1). Sizing rule: on
  the board every two-ended part spans its edge end to end; the compass, generator and probes fit a 70 px square
  centred on their spot; in the tray every piece fits the same 56 px box.
- cb-magnet-n and cb-magnet-s (shared line: "a large rectangular magnet pole block, side view, smooth painted metal,
  studio light, on a plain white background", one painted red, one painted blue); 3:4; cutout yes; people no; the two
  poles of the Inside cutaway, N and S in code.
Drawn in code: grid and node dots, wires, current dots and arrows, resistor bands, glows, meter needle and numbers,
the coil, slip rings and commutator, field lines, strip chart and angle dial, preview.svg.

## Voice
Bank `calm-professor` ("Say evenly and clearly, like a calm, friendly college professor"), here a physics professor
at the demo bench. Changed from hs-narrator, which the built grade 11 neighbors collision-lab, motion-graph-match and
field-lines all use (and sound-studio used in this batch). No grade 10 or 11 neighbor or batch sibling uses
calm-professor; energy-accountant (grade 9) does. `Curio.voice`, `scope: () => state.mode`. Hints change at once on
every mode or state change; lines queue with a `valid` check.
- board (how; Board welcome; stale once a part is placed or a starter loads): "Pick a part from the tray, then click
  between two dots to place it."
- starters (how; first time the Starters list opens; stale once a starter loads): "Pick a starter from the list to
  load a ready circuit."
- probes (how; first probe picked up; stale once both probes sit on dots): "Drop the red and black probes on two dots
  to read the voltage between them."
- ammeter (how; first ammeter placed; stale once current flows through it): "An ammeter goes in the path of the
  current, not beside it."
- gen (how; first generator on the board; stale once the crank passes 1 rev/s): "Drag the crank handle in circles, or
  hold the Hold to crank button."
- load (how; first bulb added or switched in while the crank turns; stale on a mode switch): "Watch the crank speed as
  you add bulbs. More current means the magnets push back harder."
- insideEmpty (how; Inside with no generator; stale once a generator exists): "There is no generator yet. Press Add a
  generator."
- inside (how; Inside welcome with a generator; stale once the crank turns): "Turn the crank and watch the coil. The
  changing field through it makes a voltage."
- ac (how; first spin with AC output; stale on an Output change): "With slip rings the current flips direction every
  half turn. That is alternating current."
- dc (how; first spin with DC output; stale on an Output change): "With a commutator the current always flows the same
  way, but it still pulses."
- short (event; each time the short chip appears; stale once the short is gone): "That is a short circuit. Almost all
  the energy is turning into heat inside the source."
- burnout (event; each burnout; stale on Replace bulb): "That bulb burned out. It got far more power than it was made
  for."
- oersted (how; Oersted starter loads; stale once the needle has swung past 10 degrees): "Close the switch and watch
  the compass needle. A current makes a magnetic field."

## Family engine
none. Keep the circuit solver, the crank model and the compass model as three clearly marked blocks so a future
circuits kit file can lift them.

## Sources
- Ohm's law, series and parallel resistance, Kirchhoff's rules, internal resistance: OpenStax, College Physics 2e,
  chapters 20 and 21, https://openstax.org/details/books/college-physics-2e
- Generator EMF = N B A omega sin(omega t): OpenStax College Physics 2e, 23.5 Electric Generators,
  https://openstax.org/books/college-physics-2e/pages/23-5-electric-generators
- Back EMF and the load opposing the generator (Lenz's law): OpenStax College Physics 2e, 23.2 and 23.6,
  https://openstax.org/books/college-physics-2e/pages/23-2-faradays-law-of-induction-lenzs-law
- Field of a long straight wire B = mu0 I / (2 pi r) and right-hand rule: OpenStax College Physics 2e, 22.9,
  https://openstax.org/books/college-physics-2e/pages/22-9-magnetic-fields-produced-by-currents-amperes-law
- mu0 = 4 pi x 10^-7 T m/A (exact before 2019; CODATA 2018 value 1.25663706212e-6 N/A^2): NIST,
  https://physics.nist.gov/cgi-bin/cuu/Value?mu0
- Earth's horizontal field about 20 microtesla in much of the US: NOAA NCEI World Magnetic Model calculator,
  https://www.ngdc.noaa.gov/geomag/calculators/magcalc.shtml
- Oersted's 1820 result (current north above needle swings north end west): OpenStax 22.9 above; Britannica
  "Hans Christian Orsted", https://www.britannica.com/biography/Hans-Christian-Orsted
- Filament resistance rises with temperature: OpenStax College Physics 2e, 20.3 Resistance and Resistivity.
- Standards text: NGSS HS-PS2-5 and HS-PS3-5, https://www.nextgenscience.org/dci-arrangement/hs-ps2-motion-and-stability-forces-and-interactions
- Model values (bulb 10 ohm, internal resistances, coil size, inertia, friction, hand torque, burnout at 9 W) are design
  choices, not facts; teacher notes must say so.
- Number checks (Python, 2026-10-29): One bulb 0.587 A, 5.88 V; Series 0.297 A, 2.97 V each; Parallel 1.154 A on the
  rail, 0.577 A and 5.77 V per bulb; divider reads 3.00 V; Oersted 0.577 A, 11.5 microtesla, needle 30.0 degrees;
  bulb power 3.46 W at 6 V, 7.79 W at 9 V, 13.8 W at 12 V (was printed 14.4 W, which ignored the 0.2 ohm internal
  resistance; fixed). Crank, time-stepped at 0.1 ms over 40 s with the model above at 20 percent effort: open circuit
  hits the 6 rev/s cap; one bulb 4.78 rev/s mean, 9.6 V peak; two bulbs 3.02 rev/s, 6.2 V; short 0.57 rev/s; AC and DC
  give the same speeds. The old "one bulb near 3 rev/s and 6 V" was wrong at 20 percent (it needs 12.5 percent):
  fixed to the computed values. The formula line example (18.8 rad/s, 0.71) gives 4.27 V.

## Done when
1. One bulb starter at 6 V reads about 0.59 A on the bulb and about 5.9 V across it; the bulb glows near full.
2. Series bulbs: ammeter reads about 0.30 A, each bulb about 2.97 V by voltmeter, both dimmer than One bulb.
3. Parallel bulbs with the switch closed: each bulb near full, the rail ammeter about double one rung's current.
4. Generator starter at 20 percent effort, DC: speed settles near 4.8 rev/s; closing the switch drops it to near
   3.0 rev/s and dims the first bulb; power in exceeds power out only by friction.
5. AC output at about 1 rev/s makes the bulb flicker and the strip chart shows a sine that changes sign; DC shows humps
   that do not.
6. Doubling Turns at the same speed doubles the EMF readout; the live formula line matches the readout.
7. Oersted starter: closing the switch swings the needle about 30 degrees; flipping the battery swings it the other way.
8. Short circuit starter: closing the short shows the short chip, the bulb goes dark, nothing breaks; 12 V on one bulb
   burns it out (the broken bulb shows) and Replace bulb restores it.
9. Focus: the board is the largest, central thing in Board at 1366x768 and in the 680x425 preview; the cutaway is the
   largest thing in Inside.
10. A tap while the crank turns: closing a switch or placing a bulb changes the crank's speed trend and the glow in the
    same frame; Turns changes the EMF readout at once.
11. How-to lines once each per load, then hint only; short and burnout lines every time; no line names Hold to crank
    when there is no generator. All 16 images load, none shows a person; parts line up on their edges at every
    rotation.
12. Everything placeable and operable by keyboard; Motion off stops dots and shows still arrows; one file passes
    `python scripts/check_tools.py`, no network, no em dashes, fits a 16:10 iframe.

## Open questions
- [circuit-builder] Voice moved from hs-narrator to calm-professor (hs-narrator is on three built grade 11 neighbors).
  calm-professor is also on energy-accountant (grade 9). OK?
- [circuit-builder] The parts are now painted top-view cutouts on a painted mat. The PhET-style flat symbols are what
  physics classes draw on paper; should the inspector also show each part's circuit symbol beside its picture?

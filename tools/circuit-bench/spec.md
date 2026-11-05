# Circuit Bench (Curiosity No. 07)

## The real thing
An electronics bench: a solderless breadboard on a green work mat, a parts bin, battery packs, jumper wires and a
handheld digital multimeter with a rotary dial and two probes. Electricians, hobbyists, engineers and physics teachers
use exactly this setup to try a circuit before soldering it. Every part here obeys a real circuit solver (Ohm's and
Kirchhoff's laws by nodal analysis), so the meter never lies and nothing is scripted.

## Map
- Anchor: science-8-electric-and-magnetic-forces (MS-PS2-3, MS-PS2-5). Also reaches:
  science-3-magnets-and-static-electricity, science-11-electricity-and-magnetism, science-4-energy-conversion-devices
  (the concept's "grade 4 energy": 4-PS3-2, 4-PS3-4). Grade band 3 to 12, tuned for grade 8.
- tools/circuit-builder/spec.md (a paused grade 11 lesson spec) lends only its solver approach and checked physics.
- Teacher plan: yes, a plan could teach MS-PS2-3 well (the coil's field changes with current and turns, read on the
  compass and the field readout) and MS-PS2-5 in part. No plan.md in this build, so it is a second card in the module.

## The first two minutes
- On open: the bench from above. A breadboard fills the middle; on it sit a 2 x AA battery pack (3.0 V) and a small
  bulb, not connected. A red and a black jumper lie loose beside them. The multimeter rests at the right, dial at OFF.
  One quiet line is printed on the mat: "Drag a wire from the battery to the bulb."
- First action, nothing read: drag the red jumper from the battery's red lead to a bulb leg. Nothing. Drag the black
  one to close the loop: the filament warms from dull red to bright yellow in about 0.1 s, amber dots flow through the
  wires, and a faint warm hum plays (Sound on).
- First reaction: drag a second bulb into the same loop and both drop to a dim orange. Move it beside the first
  (parallel) and both are bright again, while the dots in the battery leads double their speed.

## Things to do
1. Light one bulb, then two in a row, then two side by side, and compare the glow.
2. Turn the dial to V and touch the probes across each bulb in turn; the readings add up to the battery.
3. Put the meter on mA in the loop at three places and find the same number every time.
4. Plug an LED in backwards, see it stay dark, then turn it round.
5. Wire an LED straight to the 9 V battery, watch it flash and go dark, then try again with a resistor.
6. Turn a resistor's knob and watch its colour bands repaint and the LED brighten or fade.
7. Build a staircase light: two slide switches that each turn the same bulb on or off from either end.
8. Hold the motor's shaft and watch the current jump; let go and it falls as the motor speeds up.
9. Set the compass on top of a wire, close the switch, watch the needle swing, then reverse the battery.
10. Give the coil more turns, slide the iron core in, and watch the field readout and the needle grow.
11. Short the battery with one bare wire and see the wire glow red; nothing explodes.
12. Measure a bulb's ohms cold, then compare with volts divided by amps while it is lit.
13. Read how long the battery would run this circuit, then add parts and watch the hours fall.
14. Save a circuit to a slot on this device and open it again next week.

## Controls
- Parts bin, a row of labelled drawers along the bottom. Drag a part onto the board, or press its key and Enter at the
  cursor: W wire, B battery (2 x AA, 4 x AA, 9 V), L bulb (3.0 V 0.3 A), D LED, R resistor, P potentiometer, S slide
  switch (two-way, three legs), U push button, M DC motor, Z buzzer, C coil, K compass.
- Breadboard: 30 columns of two 5-hole strips plus red and blue power rails top and bottom, 2.54 mm pitch as on a real
  board. Arrows move a hole cursor; Enter picks up or drops a leg or wire end; T turns the held part 90 degrees;
  Delete removes; Escape clears the tool.
- Resistor knob: E12 values 10 ohm to 100 kilohm (61 detents); up and down one step, Page Up and Down one decade.
- Potentiometer knob: 0 to 10 kilohm over 270 degrees, 100 steps; arrows 1 step, Page keys 10.
- Battery pack: cell-count switch on AA packs (1 to 4 cells) and a reverse toggle (F).
- Slide switch and push button: click, Space or Enter; the button conducts only while held.
- Motor: press and hold the shaft to stall it (H). Coil: turns dial 50, 100, 200, 400 and an iron core toggle (I).
  LED: colour selector red, yellow, green, blue (keys 1 to 4).
- Multimeter dial: OFF, V (DC), mA (to 200 mA, fused), A (to 10 A), ohms, continuity (beeps under 30 ohm); keys 0 to 5
  with the meter focused. Probes: drag the tips to any hole, or Tab to a probe and move it with arrows.
- Current view toggle on the meter's side: conventional (amber dots, plus to minus) or electrons (blue, the other way).
- Bench notebook (a small book on the mat): 4 save slots on this device, 8 starter setups, Clear bench (confirms).
- Power strip, top right: three toggle switches for Motion, Sound and Read.

## Readouts
- Multimeter LCD, in the meter body: 3.5 digits (to 1999 counts), auto-ranging mV or V, uA, mA or A, ohm, kilohm or
  megohm, 3 significant figures; "OL" over range, "- -" with a probe floating, a minus sign when red is lower. 5 per s.
- Part tag (hover, focus or tap): V across, I through, P in mW or W, 3 significant figures; a paper tag by the part.
- Battery tag: terminal volts (2 decimals), mA drawn, and "runs about 4 h 10 min at this draw" from 2000 mAh per AA
  and 500 mAh for the 9 V, rounded to 10 minutes.
- Motor: rpm to the nearest 100, on its flywheel. Coil: centre field in mT, 2 decimals, on its label. Compass: needle
  angle from north in whole degrees, on its rim. Short chip: "Short: 6.4 A" in orange by any source over 3 A.

## The Manual
Lower-left drawer. Contents: placing parts and using the meter (volts across, amps in line); each part and its model
values; honesty notes; sources and licences. "Things people have found":
- Two bulbs in a row each glow dimmer than one alone, and the meter reads the same current anywhere in that loop
  (Kirchhoff's current rule; OpenStax College Physics 2e, 21.3).
- Two bulbs side by side each glow about as bright as one alone, but the battery supplies about twice the current
  (OpenStax College Physics 2e, 21.1).
- An LED turned around stays dark: a diode passes current one way only (HyperPhysics, "Diode").
- A lit bulb's volts divided by amps is many times its cold ohms reading, because tungsten's resistance rises as it
  heats (OpenStax College Physics 2e, 20.3).
- A wire carrying current swings a compass needle above or below it, as Hans Christian Oersted found in 1820
  (OpenStax College Physics 2e, 22.9; Britannica, "Hans Christian Orsted").
- More turns or more current make a coil's field stronger, and an iron core makes it much stronger (OpenStax College
  Physics 2e, 22.9, solenoid B = mu0 n I, and 22.2, "Ferromagnets and Electromagnets").
- A spinning motor draws far less current than one held still, because a turning motor makes its own back voltage
  (OpenStax College Physics 2e, 23.6, "Back Emf").
- A meter set to amps has almost no resistance, so its probes across a battery make a short; real meters carry a
  fuse for it (OpenStax College Physics 2e, 21.4: ammeters go in series).

## Look
- Grammar: an electronics bench from above. Dark green rubber mat with faint scuffs; an off-white breadboard with square
  holes, red and blue rail stripes, column numbers and row letters a to j moulded in; parts drawn in code as parts, not
  symbols (banded resistor, glass bulb with coiled filament, LED dome with one longer leg, can motor with a flywheel,
  copper coil); jumpers with soft curves; a charcoal meter with a grey-green LCD, rotary dial and coiled leads. Our own
  look: it must not resemble an existing circuit simulator or any meter brand's colours.
- Palette: mat #1f4a3a, board #ece8dc, holes #3a3a36, rails #c8302c and #2a5db0, copper #b87333, LCD #b9c4a8 with
  digits #1a1f17, meter #2b2e33, conventional dots #ffb547, electron dots #6fb7ff, short glow #ff6a3d, mat text #e8efe9
  (about 8.5:1; LCD digits 9.2:1). notes.md states every measured ratio.
- 1366x768: breadboard centre (about 880 x 430 px, 28 px pitch); meter standing at the right (about 250 x 440 px);
  parts drawers along the bottom; power strip top right; the plate "Curio Class Curiosities · No. 07 · Circuit Bench"
  and the Manual handle lower-left, as on Span and Spire and Pocket Universe.
- 375x812: meter as a compact band across the top (LCD and dial side by side); board in the middle, panned by dragging
  empty board, with zoom buttons (pitch at least 20 px); drawers as a horizontal strip near the bottom; plate and Manual
  handle lower-left under the strip.
- Notebook starters: one bulb; two in a row; two side by side; LED with 330 ohm on 9 V; staircase light; Oersted (wire,
  switch, compass); coil and compass; motor and push button.

## Real material and sources
- The physics is the material: a nodal-analysis solver written for this tool; no data files. OpenStax College Physics
  2e, chapters 20 to 23, cited for facts only, no text copied (its page reads CC BY-NC-SA 4.0, checked 2026-11-05);
  HyperPhysics (Georgia State University) for the diode, facts only; NOAA World Magnetic Model for Earth's field.
- Model values (design choices, stated in the Manual): AA 1.5 V with 0.15 ohm inside; 9 V with 1.5 ohm; bulb 3.0 V
  0.3 A, R = 1 + 9 x sqrt(P / 0.9 W) ohm (capped at 10), smoothed over 80 ms, burns above 2 W averaged 0.5 s; LEDs turn
  on at red 2.0, yellow 2.1, green 2.2, blue 3.0 V plus 10 ohm, burn above 50 mA averaged 0.2 s; motor 2 ohm, back
  voltage 0.0022 V per rad/s, no-load 0.15 A; coil 4 ohm, 4 cm long, 1 cm radius, finite-solenoid formula, iron core
  x 100; compass 1 cm from a part, B = mu0 I / (2 pi r) plus Earth's 20 uT north; wires 0.01 ohm, glow red above 3 A.
- Solver: conductance matrix each frame, sources as Norton equivalents, 1e-9 S from every node to ground, LED states
  iterated to stable (at most 20 passes). Keep solver, part models and compass as three marked blocks.
- Checked (Python, 2026-11-05): one bulb on 2 x AA 0.297 A at 9.8 ohm; two in a row 0.227 A, 0.33 W each; two side by
  side 0.586 A from the battery; red LED and 330 ohm on 9 V 20.5 mA; red LED straight on 2 x AA 97 mA (burns); motor
  on 2 x AA about 11,500 rpm, stalled 1.30 A; 0.3 A wire over the compass 6.0 uT, needle about 17 degrees; air-core coil
  with 200 turns 5.6 mT per amp at its centre.
- Budget: code and drawn parts about 300 KB, optional painted mat texture 120 KB. Goal under 600 KB.

## Honesty notes
In the Manual: wires and the board are near-perfect conductors; batteries do not drain (the runtime is an estimate);
LEDs switch on at one voltage; the core's x 100 is a design value (real cores vary and saturate); motor and coil values
are typical hobby parts, not one product; the compass ignores nearby steel; dots move far faster than electrons drift.

## Voice
Bank voice calm-professor (a physics professor at the demo bench), unlike Span and Spire (firm-captain) and Pocket
Universe (casual-peer). First-run hint, spoken once: "Drag a wire from the battery to the bulb." Read speaks the
current hint, then the meter: "Meter on volts. 2.94 volts." Events, every time: "That is a short circuit." and "That
part burned out. Tap it to replace it." The numbers are spoken only if the kit's read fallback speaks text that has no
recording; otherwise Read gives the hint alone and the readouts reach screen readers through a polite live region.

## Done when
1. Opening shows the unconnected battery and bulb; two wires light the bulb with nothing read.
2. One bulb on 2 x AA reads 0.30 A in line and about 2.9 V across; two in a row read 0.23 A anywhere in the loop.
3. Red LED with 330 ohm on 9 V reads 20 to 21 mA; a red LED straight on a battery burns out and can be replaced.
4. A reversed LED stays dark at 0 mA; reversing the battery swings the compass needle the other way.
5. Holding the motor's shaft raises its current to about 1.3 A; releasing it drops back near 0.15 A.
6. The meter on A across a battery shows the short chip; on mA it blows its fuse (shown, and replaceable).
7. Everything is placeable, wireable and measurable by keyboard; every control announces its value.
8. Motion off: dots stop and become still arrows sized by current; bulb glow stays.
9. Works at 680x425, 1366x768, 1920x1080 and 375x812 with board, drawers and meter reachable without page scroll.
10. One offline file, no network requests, passes scripts/check_tools.py, no em dashes, 60 fps with 30 parts.
11. The short test is answered honestly in codex-report.md.
12. No score, goal, level, sticker or finish screen anywhere.

## Open questions
- A schematic view that redraws the board as circuit symbols? Lean: yes, in a later fix round, not this build.
- Bring over circuit-builder's hand-crank generator? Lean: no; the motor is enough for now.
- Buzzer: a fixed 2.4 kHz piezo-style tone, louder with voltage? Lean: yes, capped quiet, only with Sound on.

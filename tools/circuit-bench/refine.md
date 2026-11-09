PASS (exit check 2026-11-06)
Counts: blockers 2 (general 1, family 1), should fix 17 (general 11, family 6), polish accepted 17

# Refine: circuit-bench

Lens files: `refine/teaching.md`, `refine/play.md`, `refine/craft.md`. No sensitivity review needed (all three lenses
agree: nothing cultural, Native or hard-history). Frames below are under `S:/CurioClass-codex-scratch/circuit-bench/`
(`teaching/f/`, `play/f1` to `f6`, `craft/`, `audit-r1/`). The circuit side is strong: every checked number matches the
spec (0.296 A one bulb, 0.226 A series, 20.5 mA LED, 1.28 A stall, 9.68 A short). The magnet side is where the work is.

## Blocker
1. **Coil + compass: the needle is pinned at 90 degrees, and beside the coil it points the wrong way.** src.html:561
   (coil centre field) and 582-585 (compassFields, coil branch); starter loadSetup n===6 (src.html:1052-1058). The
   coil's external field is the centre field divided by 1 + (d / 2 cm)^3, about 2.7 to 3.9 mT at the compass against
   Earth's 20 uT, so the needle reads 88 to 90 degrees at 50, 100, 200 and 400 turns and 90.0 with the core; at the
   board's far corner it is still 82 to 90 (teaching t16, t24; play f3/30-coil.png, f3/31-coil-iron.png,
   f4/42-coil-far-50.png, f4/43-coil-far-50-iron.png). The field also always points along the coil axis, so a compass
   beside the coil swings the same way as one on the axis, which is backwards for a real coil (teaching t24). Only the
   mT label moves; the needle, the one thing that shows a force, does not. Why a blocker: MS-PS2-3 is the anchor code
   and spec Things to do 10 ("watch the field readout and the needle grow") is its only activity; BASELINE rule 2 says
   the anchor must be really taught, CODEX-CURIOSITY's short test asks that the real thing be the interface, and REFINE
   makes a readout that misleads a blocker. Fixed looks like: a dipole far field (moment N I pi r^2, times 100 with the
   core; radial and axial parts, so the field beside the coil runs back the other way), and a starter whose compass sits
   where 50 turns gives roughly 20 to 40 degrees, so each turns step, the core and the cell count visibly swing the
   needle and reversing the battery swings it across north. Add a slide switch to the starter so closing it swings the
   needle. Update the Manual's honesty note on the coil field to say what the model now does. (family:curiosity)
2. **Oersted wire: the needle swings 4 degrees, and the wrong way for what the student sees.** src.html:586-596
   (Biot-Savart with rz = -0.01, compass 1 cm BELOW the wire) against draw order src.html:1801-1802 (wires drawn
   first, the compass disc drawn on top, so the picture says the compass sits ABOVE the wire); starter loadSetup
   n===5 (src.html:1043-1051). In the starter the compass sits between the outgoing and return leads, which run on
   the diagonal and mostly cancel: +4.3 degrees closed, -3.8 reversed, 4.4 at the best hole (teaching t15, t15b, t21;
   play f4/40-oersted-on, f4/41-oersted-reversed). The spec's checked case (0.3 A at 1 cm, about 17 degrees) is never
   staged; a north-south wire gives 11 (teaching t23). A student checking with the right-hand rule or a real compass on
   a real wire gets the opposite swing. Done when 4 passes only on the letter. Fixed looks like: the geometry and the
   picture agree (compute for the compass above the wire, or draw jumpers arching over the compass and say "under" in
   the Manual; pick one and make the Manual match); the starter runs one straight jumper north-south across the compass
   with the return path routed far away, so closing the switch gives a clear swing near the spec's 17 degrees and
   reversing the battery swings it as far the other way. Add a "Things people have found" entry: a wire lined up with
   the needle swings it most; one across it barely moves it. (general)

## Should fix
1. **The short and burnout event lines are never spoken, and the events make no sound.** src.html:296-297 (L.short,
   L.burn), 565-570 (burn() sends L.burn only to status()); grep for `V.say` finds no hits. A short sets no status at
   all. Seen by Play (voice log after a burn and a short) and Craft (`results.json` voice run: 0 of 1 for each). The
   spec's Voice section says both are spoken every time. Fixed: queue both as event lines each time (not once-only),
   plus a short pop on a burn and a crackle while a short lasts, Sound on only. (general)
2. **A part that burns while selected keeps a stale tag with no Replace, and the line names the wrong move.**
   src.html:565 (burn() never calls showControls()). The tag reads "Red LED · × OPEN" but still offers Red, Turn LED,
   Move, Turn, Remove, and `#replace-part` is absent (craft `voice-burned-led-1366.png`). Fixed: rebuild the tag on
   burn so Replace shows; and keep the spec's line "Tap it to replace it." true by making a tap on a burned part
   replace it (see Settled calls). (family:curiosity)
3. **Motor + push button starter: one pointer cannot stall the motor.** loadSetup n===7 (src.html:1059-1065); the
   tag's hold control (src.html:773-775) and the canvas shaft hold (1230, 1275) only stall while held. The motor turns
   only while the button is held, so a mouse or one finger cannot also hold the shaft; Play needed Space plus a mouse
   hold (play f3/26-motor-running.png, f3/27-motor-stalled.png). Things to do 8 fails for a solo student (rule 4).
   Fixed: make the tag's "Hold shaft · H" a latch (press to grab, press again to let go, aria-pressed and a visible
   state), keeping press-and-hold on the shaft itself. Keep the push-button starter. (general)
4. **The ammeter shows "- -" in a complete loop that carries no current.** src.html:617 (`connected()` false for a
   blocked or open loop). With mA in the gap of the reversed-LED loop the LCD shows "- -" while the tag says 0.00 A
   (teaching t20); the same with any open switch in series. The Manual defines "- -" as a floating probe. Done when 4
   wants 0 mA. Fixed: in A and mA, show 0.00 when both probes sit on nodes of the board; keep "- -" for a probe in an
   empty hole or off the board. (general)
5. **The short chip covers the glowing wire.** src.html:1768-1770 (chip 47 px below the battery). A short wire laid
   next to the pack, the obvious place, sits under "Short: 9.7 A" (play f3/z25.png); the probe labels also land on it
   (craft `voice-short-chip-1366.png`). Things to do 11 is "see the wire glow red". Fixed: place the chip clear of
   every wire and probe (above the pack or to the free side). (general)
6. **The 9 V battery reads "9AAV".** src.html:1634: the cell loop draws "+" and "AA" for the single 9 V cell, then
   "9 V" on top (play f3/z20.png; craft `zoom-9v.png`). Fixed: skip the AA cell drawing for the 9 V pack and draw a
   9 V battery body with its snap terminals. (family:curiosity)
7. **Every label printed on a part has a ghost copy.** src.html:1620-1622: shadowOffsetY 4 stays set while part text
   is drawn, so "3 V · 0.3 A", "2 × 1.5 V", "RED" and the live rpm and mT readouts are doubled (play
   f1/zoom-04-lit.png; craft `zoom-labels.png`, `zoom-calm-arrows.png`). Fixed: reset shadow (colour transparent,
   offset 0, blur 0) before any text. (family:curiosity)
8. **The mA range blows on every bulb circuit and the screen does not say why.** Fuse check in simulate(); status
   "Meter fuse open." A bulb draws 0.23 to 0.30 A plus cold inrush, over the 200 mA fuse, so Things to do 3 on mA with
   any bulb starter always ends in FUSE (play f2/11-mA-in-line.png). Honest, but a solo student is stuck. Fixed: the
   status says the rule where it happens, for example "Fuse open: over 200 mA. Use A for bulbs." and the Manual's
   meter section says the same. (general)
9. **The coil is 4 ohm at every turn count, with no word about it.** src.html:512; Manual line 235. Going 50 to 400
   turns multiplies the field at the same 0.694 A (teaching t16), so a student may conclude "more turns, stronger" at
   the same battery, which a real coil wound from the same wire does not give. Fixed: one honesty line in the Manual
   ("every coil here is 4 ohm, as if wound with thicker wire as turns rise; a real coil from the same wire gains
   resistance with its turns"). Scaling R with turns is a spec change: see open questions. (family:curiosity)
10. **No real-world safety line about shorts.** Manual lines 217-222; notes.md. The tool invites a student to short a
    battery and shows nothing bad happening; a grade 3 to 8 student alone at home can try it with real cells and a
    paper clip. Fixed: one plain line in the Manual's meter section and in teacher notes: "On a real bench a short
    heats the wire fast and can burn you; never short a real battery, and never use mains power." Teacher notes add
    that the bench is for battery-level DC only. (general)
11. **Motion and Sound show on or off by shade alone.** src.html:15, 158. Both buttons keep the same words; the pressed
    fill differs by 1.07 to 1.61:1 (craft `zoom-power-on.png`, `zoom-power-off.png`). Color is the only signal, and
    the look rule asks for toggle switches. Fixed: drawn toggles with an ON/OFF legend or a lit pilot lamp plus the
    word. (family:curiosity)
12. **Focus on the breadboard has no visible outline.** src.html:16, 28: `.board-wrap { overflow:hidden }` clips the
    canvas's focus-visible outline (craft `focus-4tabs-1366.png`). Fixed: draw the focus ring inside the canvas or on
    the wrapper. (general)
13. **The focus ring vanishes on paper surfaces.** src.html:16: #ffda73 is 1.03 to 1.2:1 on the tag, Manual, Notebook
    and board papers (craft `zoom-focus-hold.png`, audit `state-part-tag-680x425.png`). Fixed: a dark ring (for example
    #1a1f17 with a light inner ring) inside paper areas; measure and record it in notes.md. (general)
14. **Read speaks symbols and run-on text.** src.html:328-331. Logged: "Meter on OFF. OFF.", "Bulb. 2.81 V · 293 mA ·
    823 mW Meter on volts. 2.81 V.", "... Meter on milliamps. FUSE." (craft read run; play s4 voice log). Fixed: a
    spoken formatter (volts, milliamps, milliwatts, ohms, kilohms, "no reading" for "- -", "fuse open"), a full stop
    before "Meter", and "Meter off." The spec's own example is "Meter on volts. 2.94 volts." (general)
15. **A parts drawer stays pressed after its tool is used up.** src.html:383, 1166: pickTool sets aria-pressed but
    placeAt and select never clear it (craft `kb-probe-focus-1366.png`). Fixed: clear the pressed state whenever the
    tool is cleared. (general)
16. **The draw loop never rests, and 30 parts drop well below 60 fps on a slow machine.** src.html:1814-1840;
    `circuitDirty` is set in ten places but never read. At 4x CPU throttle: opening bench about 30 fps, 30 parts with
    five lit about 13 fps (craft `perf2.py`, `results.json`). Done when 10 asks for 60 fps with 30 parts. Fixed: cache
    the board (holes, rails, numbers) in an offscreen canvas, drop per-part shadowBlur, solve only when circuitDirty or
    a part is time-varying, skip the redraw when nothing moves; re-measure and record the numbers in notes.md.
    (general)
17. **The compact Adjust drawer hides what it adjusts.** src.html:888 and the `adjust-part` handler: below 1050 px the
    part controls open in a modal dialog over the board and tag (audit `state-part-tag-680x425.png`), so turning the
    resistor or pot hides the LED and the numbers. Things to do 6 is exactly that. Fixed: a non-modal tray that leaves
    the part and its tag values in view. (family:curiosity)

## Polish accepted
1. **Lit bulb glow is a faint haze.** drawPart bulb case (halo alpha at most 0.5). Warm the glass fill with the glow,
   a stronger bloom at full power, a real dull-red stage at low power (play f1/zoom-04-lit.png). (general)
2. **Burnout has no moment.** burn(). A bright flash for a few frames, a wisp of smoke with Motion on, then the dark ×
   (the spec says "watch it flash and go dark"; play f3/22-led-burning-50ms.png, f6/63-bulb-burned.png). (general)
3. **Battery tag shows "-296 mA".** src.html:655. Show "supplies 296 mA" as the spec's battery tag reads; keep the sign
   for the meter (teaching t03; play f1/04-lit.png). (general)
4. **Restore the Manual's attributions.** Manual lines 249-256: the spec's short sources per "Things people have
   found" entry, including "as Hans Christian Oersted found in 1820", so the "Oersted wire" starter has its name
   explained. (family:curiosity)
5. **The opening jumpers look already plugged in.** reset() ends at e12 and f16. Lay the loose tips off the hole grid
   at an angle, or give them a visible open-end mark (play f1/zoom-01-open.png). Keep the hint text. (general)
6. **Nothing follows the pointer when dragging from a drawer.** Draw the part under the pointer while dragging (play
   f6/64-drawer-mid-drag.png). (general)
7. **Probe leads end in mid-air, and the dial has no legends.** src.html:1778 (drawProbes ends at x 965). Run the leads
   off the board edge to the meter's jacks; print OFF, V, mA, A, ohm and beep legends round the dial (play
   f2/10-volts-across-bulb.png; craft `calm-parallel-1366.png`). (family:curiosity)
8. **Numbers too small when projected at 1920x1080.** resize() caps the board at 1.25; tag values are about 12 px. Let
   the board grow with the screen and size tag values near the LCD's (audit `state-parallel-1920x1080.png`). (general)
9. **Short preview sizes crop the instrument.** At 680x425 the Notebook, zoom and centre buttons cover the top rail and
   columns 1 to 8; at 800x500 the motor starter's push button sits behind the meter. Keep board tools off the board at
   short heights and centre the view on a starter's parts when it loads (audit `size-680x425.png`,
   `state-motor-800x500.png`). (family:curiosity)
10. **The LCD live region chatters.** src.html:172: `#meter-reading` aria-live polite rewrites up to five times a
    second. Announce on settle (value steady about 1 s) or on Read. (general)
11. **Compass tag shows "0.00 V · 0.00 A · 0.00 W".** src.html:655. Show only the angle (teaching t15b). (general)
12. **Leakage shows up as readings.** "0.0360 μW" on an open pack, "0.0600 μV" on an idle resistor (the 1 nS leak).
    Show 0 below a floor on tags (play s3, s6 logs). (general)
13. **A turned LED draws "RED" upside down** ("038"). Keep part text upright at any rotation (play
    f3/21-led-reversed.png). (general)
14. **Both AA cells are drawn the same way up.** Alternate them as a real holder does (play f1/zoom-01-open.png).
    (general)
15. **Two honesty clauses.** Battery runtime: "real cells give less at high draw" (2000 mAh at 0.3 A gives 6 h 40
    min, generous for alkaline). Ohms on a diode: the 1 mA test source forces an LED on (2.01 kohm, teaching t19);
    say so in the honesty notes. (general)
16. **Ω reaches screen readers as a symbol.** The resistor's aria-valuetext "3.90 kΩ resistor": write "3.9 kilohm
    resistor". Share the formatter from should fix 14. (general)
17. **The top-left "CIRCUIT BENCH / DC · 2.54 mm · NO. 07" repeats the plate.** src.html:156. Drop the name and
    number, keep "DC · 2.54 mm" if wanted (play and craft both noted it). (family:curiosity)

## Settled calls
- **Magnetism as a blocker (Play and Teaching both raised it).** Teaching rated the coil and Oersted items should fix;
  Play said "mostly no" to "is the real thing the interface" for the magnet side. Settled as blockers under
  CODEX-CURIOSITY.md and REFINE: MS-PS2-3 is the anchor code, the needle is the instrument's only showing of a force,
  and today it is pinned (coil), points the wrong way beside a coil, and swings opposite to the drawn geometry
  (Oersted). Those are readouts that mislead, and the anchor standard is not really exercised. The fix is the real
  physics shown plainly, never a goal, target angle or challenge.
- **Welcome cut short by the first tap, or skipped when a drawer opens:** fine (BASELINE rule 16). The hint stays on
  the mat and Read speaks it. Do not change.
- **"Hint out of view" on every starter:** correct; loadSetup hides the hint after the first action, as the Curiosity
  brief asks. Do not change.
- **Manual, Notebook and part-tag drawers covering the bench, and the 375 drawer strip scrolling sideways:** by
  design (spec). Not findings. The compact Adjust drawer is different (should fix 17) because the student must watch
  the board while adjusting.
- **The burn line keeps the spec's wording** ("That part burned out. Tap it to replace it."). Craft suggested "Tap
  Replace on its tag."; settled by making a tap on a burned part replace it, so the spoken line is true and the voice
  bank stays as specced.
- **Motor stall:** fixed by a latching tag control, not by changing the starter's push button to a slide switch (the
  spec lists "motor and push button" as the starter).
- **Do not add** a target angle, a "make the needle reach X" prompt, or any score or finish while fixing the magnet
  side. The circuit solver and its numbers are verified; do not retune AA, bulb, LED or motor values.

## To the spec's open questions
- **MS-PS2-5 is half exercised.** Only the magnetic field side (a compass moving with nothing touching it) is here; no
  electric field or charge. The spec says "in part". Integrator or Cory: confirm the module's lesson tool carries the
  electric half, or the code's claim on this module rests on the lesson tool alone (BASELINE rule 2).
- **Also-reaches overclaim.** science-3-magnets-and-static-electricity (3-PS2-3, 3-PS2-4) has no static electricity
  and no magnet-to-magnet force; science-11 HS-PS2-5 has only the current-makes-a-field half (no generator, by the
  spec's own open question). Suggest listing both as "touches", not reaches. Grade 4 (4-PS3-2) is genuinely exercised
  by the bulb, buzzer, motor and hot wire.
- **Scale coil resistance with turns?** It would show the real trade-off (more turns, less current on the same
  battery) as MS-PS2-3 data, but changes the spec's model values. Lean: yes, after the blocker fix lands.

## Not taken
- Changing the first-run hint to "Drag each loose wire end to a bulb leg." (Play): the hint is a spec voice line;
  polish 5 fixes the look that caused the doubt.
- Replacing the motor starter's push button with a slide switch (Play): settled by the latching hold instead.

## Exit check (2026-11-06)

Claude, cold exit check on the bundle `circuit-bench.html` (version circuit-bench-fix-1, 118,824 bytes). Frames and JSON
under `S:/CurioClass-codex-scratch/circuit-bench/exit/` (`f/` for drive.py shots s1 to s15, `audit-r2/` for the audit,
`perf.py` and `perf_noshort.py` for the craft lens's 30-part build re-run). Chrome 9701, host 8911. Note: my first
timing checks shared Chrome 9701 with the running audit and gave throttled background-tab results; every timing number
below was re-run with the audit finished.

### Blockers
1. **Coil + compass: FIXED.** Coil starter (50 turns, switch closed) re-solved at each step: 50/100/200/400 turns give
   28.4/46.9/64.6/76.3 degrees; core 88.1; 1 to 4 cells 15.7/28.4/37.9/45.0; battery reversed -29.0; switch open 0.00;
   closed again 28.4 (f/coil.png, s2 result). Moving the compass beside the coil (above its middle) gives -83.9 against
   +28.4 on the axis, so the side field runs back the other way. compassFields (src.html:717-728) is the dipole formula
   B = mu0/(4 pi r^3)[3(m.r)r - m], checked by hand. Manual line 312 names the dipole model; line 302 the 4 ohm note.
2. **Oersted wire: FIXED.** Starter: closed -13.71, reversed +13.79, open 0, closed again -13.71 (s2). Hand check of
   src.html:730-739: dl x r with the compass 1 cm above the wire; current runs rail 0 to rail 13 (south on screen,
   0.296 A), so the field above points west and the needle swings west (negative). Picture and maths agree: the
   compass is drawn over the jumper (f/oersted.png) and the Manual says above. "Things people have found" has the
   alignment entry (src.html:323).

### Should fix
1. **Short and burn spoken: FIXED.** After a real first tap: burn logged "burn:spoken", a separate short logged
   "short:spoken", status "That is a short circuit." (s5, s7). Event lines are not once-only (V.say kind event).
2. **Burned tag and tap-to-replace: FIXED.** Selected LED burns, tag rebuilds to "Red LED · × OPEN" with Replace first
   (s5). A real tap on the burned LED body (with its supply removed) replaced it: burned false (s7 burn-tap2).
3. **Motor latch: FIXED.** Real click on #hold-part: aria-pressed true, text "Release shaft · H", 1.282 A with the
   button closed; second click releases to 0.150 A (s3 motor-latch).
4. **Ammeter zero in a blocked loop: FIXED.** Reversed LED loop broken and bridged by the probes: 0.00 on mA and A
   (real clicks on the range buttons); probe moved to an empty hole: "- -" (s9). Nit, not counted: the mA range shows
   "0.00 A" and A shows "-296 mA" (auto-ranged units), fine for a 1999-count meter.
5. **Short chip clear of wires: FIXED, with a regression.** The chip sits above the pack, clear of the wires
   (f/short-chip.png). But drawShortChips (src.html:2068-2085) rebuilds every obstacle and re-runs clearance() inside the
   sort comparator for 208 candidates, every frame, while a short lasts. See Regressions.
6. **9 V body: FIXED.** f/nine-volt-led.png: one "9 V" body with snaps, no AA drawing.
7. **Ghost labels: FIXED.** Labels sharp in f/adjust-680.png and f/nine-volt-led.png ("330 Ω", "RED", "9 V").
8. **Fuse explains itself: FIXED.** One bulb, probes across a real gap, real mA click: LCD "FUSE", status "Fuse open:
   over 200 mA. Use A for bulbs.", fuse cover "FUSE OPEN · tap to replace"; A then reads 296 mA (s9). Manual line 284.
9. **4 ohm coil honesty: FIXED.** Manual line 302.
10. **Safety line: FIXED.** Manual line 287; notes.md lines 49-50 (battery-level DC only).
11. **Motion and Sound toggles: FIXED.** Real clicks: "Motion OFF" / "Sound OFF" words, aria-label, and the drawn
    switch flips (f/z-toggles-focus.png).
12. **Board focus: FIXED.** Four Tabs land on #board; the inset ring shows (f/z-toggles-focus.png).
13. **Paper focus ring: FIXED.** Focused "Reverse · F" on the tag: outline rgb(26,31,23) 3 px plus a 5 px light rim,
    clearly visible (f/z-paper-focus.png); ratios recorded in notes.md line 60.
14. **Read formatter: FIXED.** Held Read: "Bulb. 2.91 volts , 296 milliamps , 861 milliwatts. Meter on volts. 2.91
    volts."; with the meter off: "... Meter off." (s3). Nit, not counted: the logged text has a space before each comma.
15. **Drawer pressed state: FIXED.** Real click on the Resistor drawer, real tap on the board: part placed, no drawer
    left pressed (s10).
16. **60 fps with 30 parts: PARTLY FIXED.** The craft lens's own 30-part build (5 lit) with its two accidental shorts
    removed (its 9 V packs sat on one rail): 16.67 ms frames at 1x (0.3 ms work) and 17.0 ms at 4x CPU throttle
    (1.3 ms work), so the ordinary bench now meets the bar, better than polish.md claimed. With a short on the bench it
    does not: one short on that 30-part, 17-wire board gives 25.4 ms per draw and 29.5 ms frames (about 34 fps) on this
    desktop; the original build with two shorts gives 46 to 51 ms draws (about 18 to 20 fps) at 1x and 263 ms at 4x
    (perf.py output). Cost grows with wires times candidates, so a busier mat is worse. Things to do 11 is "make a
    short", so this is on the main path.
17. **Compact Adjust: FIXED.** 680x425, resistor Adjust: the tray is non-modal (`:modal` false), sits under the tag,
    and the resistor, LED glow and the 20.5 mA values stay in view (f/adjust-680.png).

**Of 19 blocker and should-fix items: 17 fixed, should fix 16 partly, and should fix 5 fixed but carrying the
regression below.**

### Polish (spot-checked in bulk, never blocking)
Seen fixed: battery tag "supplies" (3), AA cells alternate (14), top-left reads only "DC · 2.54 mm" (17), opening
jumper tips sit off the grid with open-end rings (5), dial legends and probe jacks (7), warmer bulb glow (1), compass on
the starters shows its angle (11). Taken from polish.md, not re-checked: smoke and flash timing (2), drag ghost (6),
1920 tag size (8), live-region settle (10), kilohm aria-valuetext (16).

### Regressions
- **Short chip search per frame (from should fix 5).** drawShortChips recomputes all obstacles and calls clearance()
  twice per sort comparison, about 1.5 million distance checks per short per frame on a 17-wire mat. Narrow fix:
  compute the chip spot once when a short starts (and again only when wires or probes change), score each candidate
  once before sorting, and keep the result in p.chip. Then re-measure s15 (one short, 30 parts) and the perf.py build.
- Default screen, every starter, Manual, Notebook and calm frames at 1366x768 (audit-r2 state-*.png,
  f/z-states.png): no other regressions. Coil starter shows the needle at 28 degrees; Oersted at -14.
- No console errors in any shot or in the audit; resized mid-action clean; Motion off: nothing runs forever.

### Gate
1. Done when: 1 to 9 pass in my checks or the audit (4 now real: 0 mA on the reversed LED, the needle crosses north on
   reversal; 5 at 1.28 A / 0.15 A; 6 chip and fuse). 10 partly: one file, no network requests (only the file itself
   loaded), no em dashes, but not 60 fps while a short is on a busy mat. 11 and 12 hold (no score, goal or finish).
2. Codes: MS-PS2-3 is now really exercised (needle swings with turns, core, cells and direction). Open for the
   integrator, carried from the merged list: the written call on MS-PS2-5 (only the magnetic half here) and listing
   3-PS2-3, 3-PS2-4 and HS-PS2-5 as "touches". Not a tool fix, but rule 2 wants it written before PASS.
3. Solo defaults: hold for one pointer now (motor latch, fuse message, tap-to-replace).
4. Sensitivity: not needed (all three lenses agree).
5. Blockers and should-fix: one open (should fix 16 under a short, caused by the should fix 5 change).
6. Bundle: 118,824 bytes, far under 2 MB; no console errors; no network requests.
7. Voice: hint once on the first tap (audit), Read speaks the hint plus the formatted meter, burn and short spoken each
   time as events, Sound off silent per polish.md; voice/lines.json holds the same three lines as L.

## Audit pilot
- Leads confirmed: none that are findings. The overlap rows (board tools, cursor label and hint over the board) are by
  design; the Manual and Notebook "keep region" and hidden-text rows are the modal drawers, settled as by design;
  "hint out of view" on starters is settled; the 375 drawer strip scrolling sideways is settled.
- Leads wrong: "welcome not heard" after a first tap on Notebook or Manual: a Curiosity has no welcome, only the hint,
  which is shown on the mat and spoken on Read (settled call).
- What it missed: the short-chip frame cost (it never builds a short on a busy board and measures no frame times), and
  every physics readout (the needle numbers needed drive.py and src.html).

## Integrator call (2026-11-06, BASELINE rule 2)
Settled in spec.md Map: MS-PS2-5 stays on the anchor as "in part" (magnetic half only; the electric half rests on the
module's lesson tool). 3-PS2-3, 3-PS2-4 and HS-PS2-5 move to "touches", not claimed. Codex: make tool.draft.json and
any notes match spec.md Map (claimed codes MS-PS2-3, MS-PS2-5 in part, 4-PS3-2, 4-PS3-4). The only tool fix left is
should fix 16: work out each short chip's spot once per short (or when wires change), not every frame.

## Exit check (2026-11-06)

Round 2 re-check (Claude, cold). Bundle circuit-bench.html, version circuit-bench-fix-2, 119,919 bytes. Scope: the two
items the first exit check left open (should fix 16 and its should fix 5 regression; the integrator's standards call),
plus a no-regression look at the frames they touch. Frames and JSON under
`S:/CurioClass-codex-scratch/circuit-bench/exit2/` (`audit-r2/` audit, `perf*.py` and `*.out.json` timing on the same
30-part fixtures as the first exit check, `inval-1366.png`, `contact-1366.png`). Chrome 9310, host 8310, both closed.

### Blockers
1. Coil + compass: FIXED (first exit check). Coil starter frame re-seen: needle off north, 0.97 mT, 50 turns. Polish.md
   re-measured 28.37 to 76.26 degrees across turns, matching the first exit check; no magnetic code changed.
2. Oersted wire: FIXED (first exit check). Starter frame re-seen, compass over the jumper.

### Should fix
1 to 4, 6 to 15, 17: FIXED (first exit check), unchanged code; spot-seen in the audit frames (9 V body, burn wording in
lines.json, toggles, Read logs "Drag a wire from the battery to the bulb. Meter off.").
5. Short chip clear of wires: FIXED, regression gone. drawShortChips (src.html:2071-2129) now samples obstacles once
   per wire/probe key and keeps each chip in a WeakMap keyed on that key and the source centre. Live: one short gave
   one layout, 60 explicit redraws plus 4 s of animation kept it at 1; adding a wire made exactly one new layout; the
   chip sits clear on the top strip (x300 y52, 47 px clearance; perf-1short-30parts-1366.png, perf2-30parts-lit-1366.png);
   removing the shorted pack with the real Remove button cleared the chip and the short (inval-1366.png).
16. 60 fps with 30 parts: FIXED. Same fixtures as the first exit check, 1366x768, 16 wires, 5 lit:
    | case | 1x frame / work | 4x frame avg, p50 / work |
    |---|---|---|
    | no short | 16.67 / 0.32 ms | 17.4, 16.7 / 1.47 ms |
    | one short | 16.67 / 0.41 ms | 17.7, 16.7 / 1.97 ms |
    | two shorts | 16.67 / 0.41 ms | 18.2, 16.7 / 1.98 ms |
    (Before: one short 29.5 ms frames at 1x, two shorts 263 ms draws at 4x.) A short now costs about 0.5 ms of work
    at 4x, and every case matches the no-short control the first exit check accepted. The occasional 33 ms frames at
    4x come with the software rasteriser (--disable-gpu); script work stays near 2 ms of a 16.7 ms budget.
    Polish.md's 38.75 fps no-short 4x control did not reproduce here (likely a contended or background tab); its
    "not fixed" was over-cautious.

**Of 19 blocker and should-fix items: 19 fixed.**

### Integrator call (standards)
Applied: tool.draft.json standards MS-PS2-3, MS-PS2-5 (standards_scope: in part, magnetic half), 4-PS3-2, 4-PS3-4;
3-PS2-3, 3-PS2-4, HS-PS2-5 listed as touches_not_claimed; notes.md line 30 says the same as spec.md Map.

### Polish (spot-checked in bulk, never blocking)
Unchanged since the first exit check; seen again in the audit frames: AA polarity, open-end rings, top-left label,
maker plate, warm bulbs. Known, not done (polish.md Left open): at 680x425 the AA battery Adjust tray puts Turn and
Remove in horizontal overflow (cell count and Reverse stay visible).

### Regressions
None. Default, all eight starters and the Manual at 1366x768 (contact-1366.png) match the first exit check. Motion
off: nothing runs forever. Resized mid-action: clean. 36 held clicks, five-click and quick-tap rows: no errors,
focus kept. No console errors and only the file itself loaded in every timing and invalidation run.

### Gate
1. Done when: 1 to 12 pass; 10 now holds under a short too (one file, no network, no em dashes, 60 fps bar met as
   the no-short bench was).
2. Codes: MS-PS2-3 exercised; MS-PS2-5 in part and the touches written in spec.md Map, tool.draft.json and notes.md.
3. Solo defaults: hold (first exit check; nothing touched).
4. Sensitivity: not needed (all three lenses agree).
5. Blockers and should-fix: none open.
6. Bundle: 119,919 bytes, far under 2 MB; no console errors; no network requests.
7. Voice: hint heard once on the first tap (audit rows 0, 3, 5 to 34), Read speaks hint plus meter, Sound off silent;
   voice/lines.json holds the same three lines as L (polish.md allLines check). Event narration code unchanged.

## Audit pilot
- Leads confirmed: none that are findings. All 112 leads are the settled categories (board overlays, modal Manual
  and Notebook coverage, hint hidden on starters, phone strip scroll).
- Leads wrong: "welcome not heard" after a first tap on Notebook or Manual; a Curiosity has no welcome (settled).
- What it missed: frame cost with a short on a busy mat, and the chip layout count; both needed the perf fixtures.

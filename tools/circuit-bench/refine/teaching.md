# Teaching lens: circuit-bench (Curiosity No. 07), round 1

Judged as a Curiosity (CODEX-CURIOSITY.md, VISION "Curiosities: the second shape"). I did not read codex-report,
codex-review or handoff. Frames: `S:/CurioClass-codex-scratch/circuit-bench/teaching/f/` (t01 to t31). Every number
below came from the running bundle (drive.py, port 9771). I recomputed each one in Python as well.

## What holds (checked, no finding)

- The circuit physics matches the spec's checked values and my own recompute:
  - one bulb: 296 mA in line, 2.91 V across it (t10);
  - two bulbs in series: 226 mA in all three gaps, 1.46 V + 1.46 V = 2.93 V (t11);
  - two bulbs in parallel: 0.585 A from the battery (t12);
  - red LED + 330 ohm on 9 V: 20.5 mA (t13);
  - red LED straight on 2 x AA: 97 mA, burns, then a Replace button appears (t14);
  - motor: 11,500 rpm and 0.150 A running, 1.28 A when held, back to 0.150 A when let go (t17);
  - A range across 2 x AA: 9.68 A with "Short: 9.7 A". On mA the fuse opens and can be replaced (t18);
  - bulb resistance: 1.00 ohm cold, 2.91 V / 0.296 A = 9.8 ohm hot, ohms mode says LIVE on a powered bulb (t19);
  - coil: 5.62 mT per amp at 200 turns. The solver, meter ranges and E12 colour bands are right.
- Done when 1 (two jumpers light the bulb, t02/t03), 2, 3, 5, 6, 7 (keyboard place, wire and probe, t31),
  8 (Motion off shows still arrows and the glow, t30) and 12 (no score, goal, level or finish anywhere; the
  lesson-creep grep is clean) pass. Done when 9: cite the audit's size rows and frames; the board, drawers and
  meter are present at every size. Done when 10: Craft's job. Done when 11: not checked, by brief rule.
- No predict, quiz or hidden-information mode, so nothing can give an answer away.
- notes.md "What it teaches", "Key skills" and "A five-minute start" are true of this tool. The home ideas can be
  done tonight.
- Nothing cultural, Native or hard-history. No sensitivity review needed.

## Fact spot-checks (second source, 2026-11-05)

1. OpenStax College Physics 2e licence is CC BY-NC-SA 4.0 (book page footer): matches. Section 21.3 is Kirchhoff's
   Rules, 21.4 is DC Voltmeters and Ammeters: matches the Manual's section list.
2. Finite-solenoid centre field: OpenStax UP2 eq. 12.27 at the midpoint gives mu0 N I / sqrt(L^2 + 4R^2), the same
   as the Manual's formula and the code.
3. Oersted, 1820, a compass needle near a wire; reversing the current reverses the swing (National MagLab, Linda
   Hall Library): matches the spec. (The Manual drops the name and date; see finding 10.)
4. Earth's horizontal field of about 20 uT for mid-latitude North America: a fair round value. I could not pin an
   exact US range from a second source; it is labelled a design value, so that is fine.
5. AA internal resistance: Energizer E91 sheet gives 150 to 300 milliohm fresh. The model's 0.15 ohm is at the low
   end. That is fine.
6. AA capacity: Energizer rates 2850 mAh at 25 mA, and less at high drain. The model's 2000 mAh gives "6 h 40 min" at
   0.3 A, which is generous for an alkaline cell at that drain. It is labelled an estimate (finding 13).
7. LED forward voltages: red 1.8 to 2.2 V and blue 3.0 to 3.4 V in common tables. The model's 2.0 and 3.0 V fit.
8. Tungsten hot/cold ratio about 10 to 15: the model's 9.8 / 1.0 fits.
9. E12 decade values (Vishay 31001): 10 12 15 18 22 27 33 39 47 56 68 82. The code's array matches; 49 settings is
   correct for four decades plus the endpoint.
10. Straight-wire field mu0 I / (2 pi r): 0.3 A at 1 cm is 6.0 uT, so a needle 16.7 degrees off north under a wire
    running north-south. The code's Biot-Savart reproduces this: 11 degrees for the drawn arc, t23.
11. Continuity beep: meters set it somewhere between about 0 and 100 ohm (forum reports, no maker figure found).
    30 ohm is a fair design value.

## Findings

1. **Coil + compass starter: the needle is pinned at 90 degrees, so "more turns, more current, iron core" never
   shows on it** (src.html:1052-1058 loadSetup(6); compassFields 582-585). Level: should fix. Tag: family:curiosity.
   - What: with 200 turns on 2 x AA, the coil's external field at the compass is about 2.7 mT against Earth's 20 uT.
     The needle reads 88.4 / 89.2 / 89.6 / 89.8 degrees at 50 / 100 / 200 / 400 turns, and 90.0 degrees with the
     core.
   - Even at the board's far corner, 50 turns gives 82 degrees and 400 turns gives 89 degrees. 1 cell vs 4 cells
     gives 75 vs 86 degrees.
   - Why it matters: MS-PS2-3 (factors that affect the strength of magnetic forces) and the spec's Things to do 10
     ("watch the field readout and the needle grow") depend on seeing the force change. Only the mT readout moves;
     the one thing that shows a force does not.
   - Better: a starter where the compass sits far enough away (or the external-field falloff is realistic: a dipole
     of N I pi r^2 gives about 20 uT at 7.6 cm, not the model's 70 uT). Then 50 turns sits near 20 to 40 degrees
     and turns, cells and core visibly swing it.
   - The starter also has no switch, so the needle never swings on closing.
   - Seen: t16-coil.png, t24 values.

2. **Oersted wire starter swings the needle only 4 degrees** (src.html:1043-1051). Level: should fix. Tag: general.
   - What: the compass sits between the outgoing and the return jumper, which run diagonally and partly cancel. The
     reading is +4.3 degrees closed and -3.8 degrees reversed (t15, t15b).
   - Scanning every hole in that setup, the best is 4.4 degrees (t21). The spec's checked value is about 17 degrees.
   - Done when 4 technically passes (the swing does reverse), but 4 degrees on a 60 px dial is barely visible.
   - The physics is right: wires on this board mostly run east-west, which barely moves a needle. A north-south
     wire gives 11 degrees (t23). The tool never says this.
   - Better: lay the starter's jumper north-south straight over the compass, away from the return lead. Add a
     "Things people have found" line: a wire lined up with the needle swings it most, and one across it barely
     moves it. That is the real Oersted condition.
   - Seen: t15b-oersted-on.png, t22, t23.

3. **The compass is drawn on top of the wire but its field is computed as if it sat 1 cm below the wire, so the
   needle swings the wrong way for what the student sees** (src.html:586-596, draw order 1801-1802). Level: should
   fix. Tag: general.
   - What: in t23 the compass disc covers the jumper, so the picture says the compass is above the wire. The code
     puts it 1 cm below (rz = -0.01), and the Manual says so.
   - For a wire under a compass, the deflection is opposite. A student or teacher checking with the right-hand
     rule, or with a real compass on a real wire, gets the reverse answer.
   - Better: draw jumpers over the compass (they arch above the board), or compute for the compass above.
   - Seen: t23-ns-wire.png.

4. **The coil's field points the same way all round it** (src.html:582-585). Level: should fix. Tag:
   family:curiosity.
   - What: the field to the compass is always along the coil's axis, scaled by distance. With the compass beside
     the coil (t24: 18,11 and 18,13) the needle points the same way as on the axis (87 to 88 degrees east). A real
     coil's field beside it runs the other way, back round to close the loop.
   - Mapping a field with a compass is the natural investigation for MS-PS2-5 (evidence that a field exists around
     the object). Here that map is wrong off the axis.
   - The Manual's honesty note says only "falls away with distance".
   - Better: a dipole field (radial and axial parts). If that is out of scope, an honesty line saying the compass
     model only holds near the coil's axis.

5. **The coil keeps 4 ohm at every turn count** (src.html:512; Manual line 235). Level: should fix. Tag:
   family:curiosity.
   - What: going from 50 to 400 turns doubles and redoubles the field at the same 0.694 A (t16). A real coil wound
     from the same wire gains resistance with its length, so on the same battery its current falls as turns rise.
   - The result "more turns, stronger" is the standard's claim at equal current, and that is how the textbooks say
     it. The tool lets students conclude it holds at equal battery too, without saying why.
   - Better: one honesty line ("every coil here is 4 ohm, as if made of thicker wire as turns rise; a real coil
     gains resistance with turns"), or scale R with turns so the current readout shows the trade-off. The second
     is richer MS-PS2-3 data.

6. **The ammeter reads "- -" in a loop that is open or blocked, not 0** (src.html:617, connected() 473-483).
   Level: should fix. Tag: general.
   - What: with the meter on mA in the gap of the reversed-LED loop, the LCD shows "- -" (t20). The tag says
     0.00 A.
   - The Manual defines "- -" as "a probe or its circuit is floating", but both probes are firmly in a complete
     loop. The same happens with any open switch in series.
   - Done when 4 says the reversed LED reads 0 mA. A real meter reads 0.00 mA here, and "the current is zero" is
     exactly the observation the student should make.
   - Better: in A and mA, show 0.00 when both probes are on nodes of the solved network. Keep "- -" for a probe in
     an empty hole.
   - Seen: t20 values.

7. **The anchor module's second code is only half exercised, and two also-reaches overclaim** (spec Map; module
   science-8-electric-and-magnetic-forces = MS-PS2-3; MS-PS2-5). Level: should fix. Tag: family:curiosity.
   - MS-PS2-3: really exercised, through the coil turns, cells and core with the mT readout. Findings 1 and 5 weaken
     it.
   - MS-PS2-5: covers fields between objects not in contact, electric as well as magnetic. Only the magnetic half
     can be done here (the compass moves with nothing touching it). Electric fields and charges are absent.
   - The spec says "in part", and the tool is a second card beside the module's lesson tool. That is acceptable only
     if the lesson tool carries the electric half and the module card says so. Under BASELINE rule 2 the integrator
     should confirm it does, or the code's claim should rest on the lesson tool alone.
   - Also-reaches: science-3-magnets-and-static-electricity (3-PS2-3, 3-PS2-4) has no static electricity and no
     magnet-to-magnet interaction (only Earth on a compass). science-11 HS-PS2-5 has its current-makes-a-field half
     but not its changing-field-makes-a-current half (no generator, by the spec's own open question).
   - Better: list science-3 and science-11 as "touches" in the module data, not as reaches the tool fills. Grade 4
     (4-PS3-2: electric current turned into light, heat, sound and motion) is genuinely exercised by the bulb,
     buzzer, motor and hot short wire.

8. **No real-world safety line about shorts** (Manual lines 217-222; notes.md; spec Things to do 11 "nothing
   explodes"). Level: should fix. Tag: general.
   - What: the tool invites a student to short a battery, watch the wire glow red, and sees nothing bad happen.
   - A grade 3 to 8 student alone at home (rule 4) can try that with real AA or 9 V batteries and a paper clip. Real
     shorts get hot enough to burn fingers, and a 9 V on steel wool or foil can start a fire. Lithium cells are worse.
   - Better: one plain line in the Manual's meter section and in teacher notes ("On a real bench a short heats the
     wire fast and can burn you; never short a real battery, and never use mains power"). Add a teacher-notes line
     that the bench is for battery-level DC only.

9. **Battery tag shows negative current ("-296 mA")** (src.html:655; t03). Level: polish. Tag: general.
   - A grade 8 student reads "-296 mA" next to a bulb's "+296 mA" and may think the battery takes current in.
   - The Manual explains signed current, but only in the dense "What the instrument assumes" paragraph.
   - Better: show the battery as "supplies 296 mA" (as the spec's battery tag reads), and keep the sign for the
     meter.

10. **"Things people have found" lost the Oersted name and the sources the spec gave each entry** (Manual lines
    249-256). Level: polish. Tag: family:curiosity.
    - The notebook calls a starter "Oersted wire" but nothing on screen says who Oersted was or that this is the
      1820 discovery.
    - Better: restore the spec's short attributions, e.g. "as Hans Christian Oersted found in 1820".

11. **Compass tag shows "0.00 V · 0.00 A · 0.00 W"** (src.html:655 for type compass; t15b). Level: nit. Tag:
    general. An electrical reading on a part with no legs reads as broken. Show only the angle.

12. **Ohms across a forward LED reads 2.01 kohm** (meterRead 607-615; t19). Level: nit. Tag: general.
    - The 1 mA test source has unlimited compliance, so it forces the LED on.
    - A real meter's low test voltage usually reads OL in ohms; makers add a diode mode for this.
    - Better: cap the test source near 2 V, or add a line to the honesty notes.

13. **Battery runtime is generous at bulb-level draw** (src.html:658). Level: nit. Tag: general.
    - 2000 mAh at 0.3 A gives 6 h 40 min. Alkaline cells deliver well under their rated capacity at that drain.
    - It is labelled an estimate. One honesty clause ("real cells give less at high draw") would make it true.

## Audit pilot

- **Leads confirmed:**
  - The manual, notebook and part-tag dialogs cover the board while they are open. That is expected for modal
    drawers, not a teaching issue.
  - The phone drawer strip scrolls sideways (7 of 12 out of view at 375). That is real, but Play and Craft own it.
- **Leads wrong:**
  - "hint out of view" on every starter state: loadSetup() hides the hint on purpose (reset(false) sets
    state.hint = false), and Read then speaks the selected part's tag. Not a fault.
  - The board/notebook/zoom "overlap" rows: those buttons sit on the mat above the canvas by design.
- **What it missed:** everything above. Findings 1 to 6 are physics and readout behaviour that only show when the
  setups are driven and the numbers read: the pinned coil needle, the 4 degree Oersted swing, the drawn-vs-computed
  compass geometry, the one-direction coil field, the fixed coil resistance and the ammeter's "- -" in a complete
  open loop. The audit also cannot see the module-code coverage or the missing safety line.

Counts: blocker 0, should fix 8, polish 2, nit 3.

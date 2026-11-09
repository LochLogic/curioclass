## What it teaches
Circuit Bench makes electric current, voltage and magnetic effects available to investigate with a working breadboard and meter. Students can compare series and parallel circuits, take measurements and see how resistance, polarity, heat and a turning motor change a circuit.

## Key skills
- Make and trace closed circuits, including branching paths.
- Measure voltage across a part and current in a gap in the circuit.
- Connect the brightness of a filament with electrical power and temperature.
- Change a coil's turns or core and observe a magnetic field.
- Save a circuit and revisit an observation.

## Support at home
- Look for battery markings and polarity symbols on an unpowered household device, without opening it.
- Talk about how a flashlight's switch interrupts its path from the battery to the lamp.
- Listen for a small fan changing pitch as it starts; compare that with the spinning motor on the bench.

## A five-minute start
Open the instrument and connect the waiting battery and bulb with two jumpers. Let the student decide what to change next. The notebook offers series, parallel, LED, switch, compass and motor arrangements to take apart. These are editable circuits, with no tasks to finish.

## The instrument
The code groups each vertical five-hole strip and each full-width rail electrically. Contacts on opposite sides of the trench are separate. Wires crossing on screen stay separate. A component's paper tag shows its voltage, signed current and power. Sources deliver power; other parts consume it. There is one bench, with no lesson modes.

The meter measures DC voltage across its probes, or conducts current when used in A or mA. The 200 mA fuse opens above its rating. Ohms injects a small test current into an unpowered circuit and reports LIVE on a powered pair. The Manual has keyboard instructions and exact model assumptions.

## Talk questions
What changed when you moved a bulb from a series path to a branch? Where would you put a meter to measure one branch? What did the motor do when held? How did the compass respond to reversal?

## Good to know
This is an exploratory Curiosity for grades 3 to 12, anchored in grade 8. It is a second module card; no teacher lesson plan or claim of full standards coverage is included. All circuits stay on the device in four local storage slots. Storage can be unavailable in private or restricted browser contexts; the instrument then keeps the circuit on its mat and says that saving failed.

Standards scope follows the integrator's 2026-11-06 call in spec.md Map: MS-PS2-3; MS-PS2-5 in part, magnetic field half only (the electric half rests on the module's lesson tool); 4-PS3-2 and 4-PS3-4. The instrument touches 3-PS2-3, 3-PS2-4 and HS-PS2-5 without claiming them: static electricity, magnet-to-magnet force and a generator are absent.

The supplied E12 range has 49 unique settings, including both 10 Ω and 100 kΩ. The spec's 61 detents would extend through a fifth decade, so this build keeps the requested resistance range. AA pack internal resistance scales with cell count. Batteries do not drain, and runtime is an estimate rounded to ten minutes. The Manual lists the bulb, LED, motor and coil simplifications.

Potentiometer tags show the outer-terminal voltage, current entering leg A and dissipation in both sections. Motor watts are electrical input, which includes mechanical output. Bulb light warms over 80 ms and changes from orange to yellow with solved power. Saved switches keep their positions; momentary contacts and shaft latches release on loading or window focus loss. The motor tag latches its shaft, so one pointer can then hold the separate push button. The mat holds 60 parts and 150 wires so every circuit it saves can reopen.

## Sources and licences
OpenStax College Physics 2e, chapters 20 to 23, CC BY-NC-SA 4.0, facts cited only. Georgia State University HyperPhysics, Diode, copyrighted site, facts cited only. NOAA / BGS World Magnetic Model, public government geomagnetic context, no coefficients used. All component constants and the fixed 20 μT northward field are design assumptions. Original code MIT, original text and graphics CC BY 4.0.

The finite-solenoid equation is also checked against OpenStax University Physics Volume 2, section 12.6, current online edition CC BY-NC-SA 4.0, checked 2026-11-05. Facts only; no text or images copied. Review corroboration used MIT electromagnetism notes, SparkFun's meter guidance, Fluke's resistance guidance and Rose-Hulman's filament laboratory; these supplied no bundled assets or data.

E12 values are checked against Vishay's Standard Decade Resistance Values, document 31001 (copyright Vishay, facts only). There are four decades of twelve intervals plus the 100 kΩ endpoint, giving 49 settings.

## Contrast
Measured sRGB ratios: #e8efe9 on #1f4a3a 8.55:1, #eff2e9 on #454944 8.1:1, #1a1f17 on #b9c4a8 9.2:1, #282d23 on #d2cbb0 8.67:1, #294438 on #ece8dc 8.67:1, #ffda73 on #1f4a3a 7.4:1, #55594d on #ece8dc 5.87:1, #eeead9 on #51594c 6.04:1. Mat text #e8efe9 on #1f4a3a, instrument text #eff2e9 on #454944, LCD #1a1f17 on #b9c4a8, paper text #282d23 on #d2cbb0, board text #294438 on #ece8dc, and focus #ffda73 on #1f4a3a are the tested pairs. Controls have shapes, labels, polarity signs and numeric readouts in addition to colour.

## Size
No bitmap assets, audio recordings, network data or fonts. The working surface and all parts are drawn in code. The generated single HTML file embeds the shared voice, sound and Motion helpers and runs offline.


## Battery-level DC only
On a real bench a short heats the wire fast and can burn you; never short a real battery, and never use mains power.
This simulated bench is for battery-level DC only. In the meter's mA range a bulb exceeds the 200 mA fuse rating; use A for bulbs.

## Refine model notes
Coil resistance remains 4 ohms for all turns, as if thicker wire is used for larger turn counts. A coil wound from one wire gauge gains resistance with length (OpenStax College Physics 2e, 20.3).
The compass is 1 cm above the jumper plane, matching the drawing. Coil centre labels keep the finite-solenoid equation; external compass fields use the vector dipole equation, softened below one radius.
Battery runtime is a nominal capacity estimate: real cells give less at high draw. The ohmmeter's 1 mA test source can turn an LED on, so the displayed ratio is not a fixed resistance of that diode.

Paper focus ring #1a1f17 against #ece8dc, #d2cbb0 and #e8e0c9 is measured in the fix evidence; it has a #f5f1e5 outer rim. The board ring is inset 6 px so the wrapper cannot clip it.
The LCD has no live-region attribute. A changed reading is announced after it settles for one second, or on Read. Read expands engineering symbols into spoken units.

Measured paper focus contrast, 2026-11-06: #ece8dc 13.69:1, #d2cbb0 10.31:1, #e8e0c9 12.73:1.


## Refine performance measurement, 2026-11-06
Muted desktop Chrome at 1366x768, 4x CPU throttle, 30 parts with five lit bulbs: original 20.62 fps, first board-cache pass 46.69 fps, final board/part-cache pass 45.39 fps. Final mean measured frame work was 1.16 ms versus 5.86 ms originally; scheduling/compositing still kept observed throughput below 60 fps. This requirement remains open. The two-lit 30-part run varied from 54.02 to 39.42 fps, so a steady 60 fps is not claimed. On an idle bench, counters stayed at one solve and two draws during a two-second observation. This is a headless desktop measurement, not a school Chromebook test.
The mandatory final audit disconnected with Windows error 64 at its first browser size; it produced no report or leads. No second audit was run.

## Refine round 2 performance, 2026-11-06
The figures above are round 1 history. The exit check's 30-part, five-lit, 16 to 17 wire fixture was reproduced at 1366x768. With one/two shorts, mean drawing cost fell from 29.01/52.49 ms to 0.19/0.17 ms, and observed throughput rose from 31.38/18.08 fps to 59.81/60.05 fps. Chip positions and measured wire clearance stayed identical. Across 180 animated frames and 60 extra draws, the layout counter did not increase.

At 4x CPU throttle, one/two shorts measured 42.68/43.54 fps with 2.23/2.02 ms mean frame work. The matching no-short control measured 38.75 fps and 2.42 ms work. The per-frame placement regression is removed, but a strict 60 fps at 4x throttle is not demonstrated. These are headless desktop measurements, not a physical Chromebook test. Reproducible drivers, raw frame intervals and screenshots are in `_scratch/circuit-bench/r2-*`.


## Refine round 2 final audit
The final round 2 audit completed once within the 40-minute limit, using Chrome 9911 and iframe host 8715. All 94 frames were reviewed. Its 112 mechanical leads are classified in polish.md: intentional canvas/modal/scroll and hidden-hint behavior, accepted drawer-first hint suppression, and the existing 680x425 battery tray's horizontally scrolled Turn/Remove controls. No console errors, endless calm motion, focus loss, resize exceptions or stuck controls were reported. The ten repeated-input and ten quick-tap rows are clean. This audit does not establish frame rate or independently repeat the burn/short event walk. Strict 60 fps at 4x throttle remains unproved; the short-label placement regression is removed.

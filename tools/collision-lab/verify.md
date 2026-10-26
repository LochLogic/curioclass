FIX (no blockers: all 10 "Done when" items pass and the physics checks out. Two small should-fix items and some nits.)

Checked cold on 2026-10-25 against the bundle built with `CURIO_DRAFT=1` (all 23 voice clips were present and inlined by the time I rebundled). Chrome ran headless with --mute-audio through a copy of the CDP driver, which also logged console errors and network requests. Result: 0 console errors and 0 network requests in every frame. The only 404s were favicon requests to my own test server.

## Physics (independent Python closed forms, plus the tool's own engine run in Node)
- All 7 presets match the spec: momentum before = after (0.150 / 0.150 / 0.200 / 0.060 / 0.000 / 0.150 / 0.300 kg·m/s), the after velocities, and KE kept (100 / 50 / 100 / 100 / 0 / 68 / 67 percent). The measured e, (vB' - vA') / (vA - vB), comes out to 1, 0, 1, 1, 0, 0.6, 0.
- Center of mass frame: preset 3 gives v_cm +0.333 and momenta ±0.0333 before and after, with Total 0.000 in both rows. In the browser the center of mass marker stayed at x = 513.0 px across 7 samples. KE kept in this frame is e squared (0 percent Velcro, 36 percent Rubber), as notes.md says.
- Noses at 0.50 kg and 1.00 m/s: Steel 158.1 N, 9.9 ms, 0.32 cm, -1.00 m/s. Spring 10.0 N, 157.1 ms, 5.00 cm. Rubber 22.4 N, 52.7 ms, 2.24 cm, -0.50 m/s, 0.75 N·s. Crumple 6 N / 5 cm: 6.0 N, 83.3 ms, 4.17 cm, Stopped. Crumple 2 N / 5 cm: Bottomed out, 122.5 N, -0.76 m/s. Crumple 5 N / 5 cm: Stopped with crush 5.00 cm. Every value is within 0.1 percent of the closed forms.
- Impulse vs change in momentum: the worst gap over the whole slider grid is 0.5 percent (limit 1 percent).
- Specs: I swept every Crumple slider setting (Fc 1 to 40 step 0.5, L 1 to 10 step 0.5) in Node, and spec 4 in the browser too (1501 runs, 0 met). Spec 1 meets with 5.0 to 9.5 N at 5 cm. Spec 2 meets with 19.0 to 29.5 N at 6 cm. Spec 3 meets with 10.0 to 14.5 N at 10 cm. Spec 4 is never met: its lowest no-bounce peak is 20.0 N (Fc 20, L 10, Stopped), and 14.5 N bottoms out at 235 N. Steel, Spring and Rubber always bounce. Students can prove spec 4 from what is on screen: "Energy to absorb 2.00 J" on the spec button, the "Energy at impact 2.00 J" readout (shown even before a run), and the 10.0 cm limit give 2.00 / 0.10 = 20 N, over the 15 N limit. The card never says which spec is impossible, and spec 4 is shown as "Heavy and fast".

## Findings
1. **Read as the first tap drops the Air Track welcome** (src.html:1450-1456, first-tap listener). Seen in voice test v5: Read pressed first, then Reset. The hint played, and at-welcome was never queued or said. It plays only if the student leaves Air Track and comes back. The other voice rules held with held clicks: Read cut off a welcome and spoke the hint; a line queued during Read (at-cm-frame) waited until Read finished; rapid mode clicks dropped the queued lines. One effect of "said when it starts playing": switching modes quickly marks each welcome said after about 1.3 s of audio, so it does not replay on return. That follows the rule; I note it in case Cory wants it different. **Should fix.**
2. **Measurement noise can show "Kinetic energy kept: 106 percent", but Notebook plot 2 clamps the point to 100** (src.html:1348, `clamp(r.kept, 0, 100)`). Seen in run n2: Spring preset with noise on. With ±2 percent on each velocity, Spring runs can read up to about 108 percent, so the table and the plot disagree, and nothing on screen explains a reading over 100. Either extend the plot's y axis past 100 or add a short note. **Should fix.**
3. **A glider stopped at an end stop keeps its after-collision velocity arrow** ("B +0.67 m/s"), and the arrow runs past the end stop and off the stage edge. Seen in frames z1280x720_air, z800x500_air and z760x900_air (preset 3, run finished). **Nit.**
4. **The no-collision voice line is the same for both reasons** (src.html:573). When a glider reaches an end stop first, the voice says "Glider A never catches glider B". The hint says "a glider reached an end stop before A caught B". **Nit.**
5. **Spec 2 shows "Energy to absorb 1.13 J"** (true value 1.125). A student working from the screen gets 18.8 N instead of 18.75 N. This does not affect which slider settings work. **Nit.**
6. **The scene is not a fixed 1440 x 810 design scaled with Curio.fit** (as the spec says). It is drawn at real pixel size with three layouts (wide, compact, stack), following motion-graph-match. This looks deliberate and is noted in the CSS. Scene text stays 10 to 12 px at every size I checked. **Nit (spec deviation).**
7. **At 375 px (iframe host), the "Momentum change" readout label touches its cell's right edge.** Seen in frame i375_cz. **Nit.**
8. **After a bounce, the magnified inset is an empty window**, because the glider has rolled out of view. Seen in c2, c5 and c8. **Nit.**
9. **Custom e = 0.50 shows "Kinetic energy kept: 62 percent"** (exact value 62.5; floating point makes it 62.4999). **Nit.**

## Also checked, fine
- Done when 1 to 10 all pass. That covers the ledger lines, Total bars equal, the no-collision hint with Record disabled, the "Nothing is moving" hint, "peak off scale: 158 N" with axes locked, at most 3 ghosts with the oldest dropped first, the Spec met line with locked sliders and Leave spec, Record to the tables and plots, Copy table (TSV with units in the headers; the fallback box appears when the clipboard is refused), Clear needing two presses, reload keeping rows and conclusion text, blocked localStorage (every mode runs; "Notes will not be saved on this device."), and Motion off (runs end at once with the same values).
- Predict: Launch stays locked until both boxes are filled, the comparison lines appear afterward, and nothing gives the after values away beforehand. Jump to collision appears when contact is 30 s away.
- Keyboard: tab order is header, gliders, then panel. Space launches and R resets on both benches. Arrow keys move a glider 0.05 m with a visible focus ring. Drag limits hold (B stops at A + 0.25, A stops at 0.15). Every control is 44 px or more; the 20 px checkboxes sit inside 44 px labels.
- Lines: all 23 spoken lines appear word for word in `voice/lines.json` and `allLines()`, and all 23 clips are in the bundle. The longest is 135 characters.
- Art: no `art:` tokens, prompts.json has no assets, and there are no people.
- Words: no em dashes, "Curio Class" is never shortened to "Curio", no confetti, no scores, and the spec card says the specs are invented.
- Sizes: 680x425, 800x500 and 1000x625 use the compact layout with Launch, Reset, Record and the main settings visible without scrolling. 1280x720 is wide, 760 stacks, and 375 in the iframe host stacks with no horizontal scroll. On the smallest box the spec card's result lines are below the fold, which is normal panel scrolling.

## Unsure
- Whether the welcome behavior in item 1 and the quick-switch behavior are what Cory wants. Both are judgment calls under the batch rule.
- Item 2 may be intended as a lesson about noise, but the plot clamp hides it either way.

## Re-verify

FIX (one new should-fix in voice; both earlier should-fix items and all fixable nits are fixed.)

Checked cold on 2026-10-25 against a fresh `CURIO_DRAFT=1` bundle (724 KB, 23 clips inlined). Headless Chrome with --mute-audio through my own copy of the CDP driver. Voice was logged by hooking `HTMLMediaElement.play`/`pause`/`ended` and `Curio.stop`, with every clip mapped back to its line, and every click held about 120 ms. 0 console errors in every frame (only favicon 404s from my test server). No network URLs in the bundle besides the SVG namespace.

### Earlier findings
1. Read as first tap drops the welcome: **fixed.** Read first: the hint plays at once and at-welcome starts when it ends (log: hint 1634 to 9578 ms, welcome 9735). Read first, then Reset 0.5 s later: same, Read is not cut. Launch first and R key first: welcome plays, at-first-run waits until it ends. Mode button first: that mode's welcome only.
2. Noisy KE over 100 percent clamped in plot 2: **fixed.** Spring with noise recorded runs at 104, 104, 102, 101 percent; the plot points sit at distinct heights above the 100 line (y axis grows to fit) and a note under the plot says a measured value can land above 100 percent. Frame z1280x720_nb.
3. Stopped glider keeps its after arrow: **fixed.** Preset 3 finished: "B 0.00 m/s", no arrow, nothing past the end stop at 1280x720, 1000x625, 760 and 375.
4. Same no-collision voice line for both reasons: **fixed** (src.html:610 narrates `endFirst` for the end-stop case; the line is in lines.json). Hint verified in the browser for both reasons.
5. Spec 2 "1.13 J": **fixed.** Spec buttons read 0.25, 1.125, 1.00, 2.00 J.
6. Real-pixel stage instead of Curio.fit: **unchanged, deliberate.** Still a nit (spec deviation).
7. 375 px "Momentum change" label touching its edge: **fixed** (reads "Change in p" in narrow cells). Frame i375_cz.
8. Empty magnified inset after a bounce: **fixed**, with a new nit (item C below).
9. Custom e = 0.50 shows 62 percent: **fixed** (63 percent).

### Physics spot checks (in the browser)
- Preset 2: p 0.1500 to 0.1500, both +0.300, KE kept 50.0. Preset 3: 0.2000 to 0.2000, A +0.267, B +0.667, 100. Preset 4: 0.0600 to 0.0600, A minus 0.400, B +0.200, 100.
- Noses at 0.50 kg, 1.00 m/s: Steel 158.1 N, 9.9 ms, 0.32 cm, minus 1.00, 1.000 N·s. Rubber 22.4 N, 52.7 ms, 2.24 cm, minus 0.50, 0.750 N·s. Crumple 6/5: 6.0 N, 83.3 ms, 4.17 cm, Stopped. Crumple 2/5: Bottomed out, 122.5 N, minus 0.76 m/s.
- Full Crumple slider sweep (1501 runs per spec, plus Steel, Spring, Rubber): spec 1 met by 33 settings (5.0 to 9.5 N), spec 2 by 69 (19.0 to 29.5 N), spec 3 by 40 (10.0 to 14.5 N), spec 4 by 0. Lowest no-bounce peak on spec 4 is 20.0 N; "Energy to absorb 2.00 J" and the 10.0 cm limit still prove it on screen.

### Voice runs (held clicks; clips that started, in order)
- Mode hopping (Crumple, Notebook, Air, Crumple at 0.7 s gaps): each welcome starts and is cut by the next; all three are marked said, so none replays on return. Same as the first verify noted; follows the rule.
- Read during a welcome, then tick Ride: welcome cut, hint plays to the end, then at-cm-frame. Read during Read: restarts the hint, nothing else. Read during at-first-run: cut, hint plays, then a queued at-cm-frame waits for it.
- Read during a run, then the run finishes, then Read again: the queued at-first-run is dropped by the second Read (never started), as the rule allows.

### New findings
A. **Switching mode while Read is speaking leaves about 10 s of silence, then the new mode's welcome starts on its own** (src.html:1500 to 1509). `narrate` waits on `readP`, but `hush()` from `setMode` only pauses the Read clip, and a paused clip never fires `ended`, so `readP` resolves only at its fallback timer (2500 + 80 x hint length, about 10 s for the Air Track hint). Seen in two runs: Read at 14.78 s, Crumple Zone at 15.41 s, cz-welcome started at 25.13 s; and Read as the first tap, Crumple Zone 0.6 s later, cz-welcome at 11.97 s. The welcome arrives late and out of nowhere, and anything the student triggers in those 10 s queues behind it. **Should fix.**
B. **Sound pressed first (off), then pressed again (on): Air Track's welcome never plays** until the student leaves and comes back. The first tap went to Sound, so no welcome was queued, and turning Sound back on queues nothing. Log "sound-off-on": no clip in 4 s after Sound on and a Reset. Arguably fine (the student did silence it), so a judgment call. **Nit.**
C. **The magnified inset now pins the glider about 1 cm from the wall after a bounce, under a ruler labeled "cm from wall", while its label says "now 15 cm away"** (src.html:1283, `away ? -.012`). The ruler and the label disagree. Seen in z1280x720_cz (Rubber): nose tip at about 1.2 cm on the ruler. **Nit.**
D. **At 680x425 and 375 wide the "15 cm away" label crowds the "magnified, cm from wall" caption**, and at 375 the caption's last word touches the wall plate. Readable. Frames z680x425_cz, i375_cz. **Nit.**

### Sizes
680x425, 800x500, 1000x625 compact; 1280x720 wide; 760x900 and 375 (http iframe host) stack, no horizontal scroll at 375 (scrollWidth 375). Air, Crumple and Notebook frames at each size show no overlaps beyond item D.

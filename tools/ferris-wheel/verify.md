FIX

Verify of ferris-wheel, 2026-10-25. Checked against spec.md, POLISH.md, VERIFY.md and BATCH-G11.md. I bundled it with CURIO_DRAFT=1 (105 KB), drove it in headless Chrome over CDP with console and exception capture, and used an http-served iframe host for 375 px. No console errors or exceptions in any shot. Frames are in C:\Users\Cory\AppData\Local\Temp\claude\S--\90ed2a60-e34a-41ef-b258-25144edd2387\scratchpad\fwv\shots

## Findings

1. **16:10 embed, 680x425 and 800x500: the scene text can't be read.** Where: relayout()/fit() in src.html, lines 957-980. The 1100x640 scene is drawn at scale 0.345 (680x425) and 0.455 (800x500). The text boost `--ts` stops at 1.5, so tick labels, "you", "height (m)", the rim labels and "1 radian, about 57.3 degrees" come out about 6.7 px at 680x425 and about 8.9 px at 800x500. The car is about 6 px across, but its hit area is still 46 px. The stage also has empty bands above and below the scene. 1000x625 is fine (about 11 px). Seen in: s_680x425_ride/unit/real/match.png, zoomed in z_680_ride.png, and s_800x500_real.png. How serious: **blocker** for the site embed, which is 680x425. I'm not sure whether the site page has a full-screen button that would ease this.

2. **Match in the 16:10 embed: the wheel controls are below the fold.** Where: compact panel order (src.html lines 56-57). At 680x425 and 800x500 the target buttons, Check, Show my curve, Reveal and the result come first, then Clock. The Radius slider ends at y 474 in a 425/500 px box, and Board at and Turn are lower still. To change the wheel you have to scroll the panel, which goes against "controls visible without scrolling". Seen in: s_680x425_match.png and the measured button positions. How serious: should fix.

3. **The first tap uses up the Ride welcome.** Where: the first-tap listener (src.html lines 925-928). If a student's first tap is on Unit Circle, Real Wheels or Match, the capture pointerdown queues narrate(WELCOME[ride]) while the mode is still Ride. The Ride welcome starts, the click then cuts it off with hush(), and rideWelcome is marked said, so going back to Ride later stays silent. Tapping Sound first has the same effect. Seen in: shot 52_voice, where after clicking Unit, Real, Unit, Read, Match the said set was [rideWelcome, unitWelcome, realWelcome, matchWelcome]. Done-when 9 holds otherwise: Read speaks the hint and a mode switch stops the speech and the clock. How serious: should fix.

4. **"Try boarding from the side" plays on any wheel change.** Where: wheelChanged() (src.html line 803). It narrates rideBoard on the first slider, Board or Turn change. If that first change is already "Right side" or "Left side", the line asks the student to do what they just did. How serious: nit.

5. **Labels collide in Unit Circle.** "1 radian, about 57.3 degrees" sits right on the π/2 rim label (wide, 11_unit_rad.png). At 375 px it also runs to the right edge (c375_unit.png), and the radian tick "6" lands on the "sin θ" label. "0, 2π" crowds the graph's "height" axis label (10_unit.png). How serious: nit.

6. **The dashed height line runs through graph tick labels.** For example "20" in 05_clear.png, "0.5" in 12_unit_unroll.png, and the y-axis title "height (m)" in s_800x500_real.png. How serious: nit.

7. **Stack layout (760 and 375 px): Play and the graph are never on screen together.** At 760x900 the scene and equation fill about 1130 px, and Play is at y 1434 to 1621. At 375 px in an 812 px frame the stage and equation fill the whole screen. So a student can't press Play and watch the graph grow without scrolling back. Seen in: s_760_ridex.png and c375_ride.png. I'm not sure the spec asks for more than "usable" here. How serious: should fix (a small sticky clock row would do).

8. **"Clamped" note on Try it in Ride.** Chicago's radius 38.1 to 38 and hub 42.3 to 42 are rounding to the slider step, not clamping. Only the turn time (540 to 120 s) is really clamped (23_real_try.png). How serious: nit.

9. **Singapore Flyer fact card: "Opened April 2008".** That is the official opening (15 April 2008). Wikipedia gives first public rides on 14 February 2008 and a soft opening on 1 March 2008. "Officially opened April 2008" would be exact. How serious: nit.

10. **Spec says Sound is off by default.** Spec line: "Sound (off by default per kit)". The kit and POLISH.md have sound on by default, and the tool follows the kit. This is a spec wording error, not a tool bug. How serious: nit.

11. **Compact equation bar wraps mid-phrase.** At 680x425, "same as" ends one line and "h(t) = 18 − 15 cos(2πt / 40)" starts the next (s_680x425_ride.png). How serious: nit.

## Checked and correct

**Ride math (recomputed):** h(t) = D + r sin(θ0 + ωt), with ω = ±2π/P and θ0 = −π/2, 0, π/2, π.
- Defaults give 3 m at t 0, 18 at 10, 33 at 20, 18 at 30, 3 at 40.
- Rim speed is 2π·15/40 = 2.36 m/s.
- The equation and its "same as" line match the spec in all 8 board and direction cases.
- Bottom CCW = Bottom CW, and Top CCW = Top CW.
- Right CCW rises and Right CW falls. Left CCW falls and Left CW rises.
- Done-when 1, 3 and 4 pass. Radius 40 pushes Hub to 41 with the clearance hint, and Hub can't go below r + 1.
- Extremes: r 40, D 60, P 10 gives 12 smooth turns topping at 100 m.

**Drag and keys (real mouse and keyboard events):**
- A quarter-turn car drag gives t 10, h 18. Dragging the dot to t 30 puts the car on the opposite (left) side. Dragging while playing pauses first.
- Arrow keys step π/12 of a turn. Tab reaches the car, and its focus ring shows (46_tabfocus.png). Done-when 2 passes.

**Sideways distance and arc:** the sideways readout, the x² + (h − D)² = r² line, and the arc with its turn count (1.25 at t 50) are correct.

**Keep:** keeps up to 3 and replaces the oldest. The labels are boxed with dash swatches.

**Unit Circle:**
- Three π/6 steps give π/2, sin 1.000, cos 0.000.
- θ = 7 gives 401.1°, sin 0.657, cos 0.754.
- The identity line reads 1.000 at 50 random angles.
- One radian is labeled 57.3 degrees with marks 1 to 6. Unroll ends exactly under the graph dot (x 629.9 vs 629.86).
- Rim marks are every π/6 and π/4. Axis ticks run π/2 to 4π.
- The graph is full at 4π. Done-when 5 passes.

**Real Wheels (fetched from sources):**
- Chicago: 80.4 m (264 ft), 36 cars, up to 60 people with 40 chairs, 9-minute nonstop turn, June 21, 1893 (Wikipedia). 76 m / 250 ft diameter (Guinness).
- London Eye: 135 m, 120 m, 32 capsules, about 30 min, public opening 9 March 2000.
- Singapore Flyer: 165 m, 150 m, 28 capsules, about 32 min.
- High Roller: 550 ft (167.6 m), 520 ft (158.5 m), 28 cabins, 30 min, opened March 31, 2014.
- Model values are correct: hubs 42.3, 75, 90, 88.35; lowest points 4.2, 15, 15, 9.1.
- Computed speeds: 0.44 m/s (1.6 km/h), 0.21 (0.75), 0.25 (0.88), 0.28 (1.0).
- 60x and 300x run at 1 and 5 min per second. Four kept, labeled, dashed curves share one set of axes. Done-when 6 passes.

**Match:** all 8 targets were checked.
- Each target matches its own wheel, in either direction where the spec says "either".
- 5 fails with CW, 6 fails with CCW, and 8 fails with CW (gap 40, 40, 16 m).
- Equivalent wheels also count: Left CW matches target 5, and Right CW matches target 8.
- Target 6 with the target 5 wheel: "Biggest gap: 40 m near t = 15 s", with a marker.
- The default wheel against target 1 reports a 28 m gap at t = 60, which is correct.
- The notes are correct: 3 turns for P 40, 6 turns for P 20, 1 turn for P 120, Top opens at a maximum.
- Reveal works. No score or timer. Done-when 7 passes.

**Motion off:** One radian and Unroll jump to the end, and Play moves in 0.25 s steps. **Sound off:** tone() is gated by the kit and nothing plays. Done-when 8 passes.

**Contract:**
- One file, no network URLs, kit used.
- 18 lines in allLines() match voice/lines.json word for word.
- One art token (river-night-sky), marked people false.
- No em dashes in src, notes, spec, lines, prompts or draft json. "Curio" appears alone only as the kit's JS name.
- No buttons under 44 px at 375 px. No horizontal scroll at any size.

**Not judged yet:** the art is still the draft placeholder (the grey ellipse labeled "river-night-sky"), and the voice is not recorded. Both are expected at this stage.

## Re-verify

FIX

Cold re-verify, 2026-10-25. Rebuilt with CURIO_DRAFT=1 (613 KB; the real art is in, so no placeholder), drove it in headless Chrome over CDP with console and exception capture, real mouse clicks for the voice tests, and an http-served 375x812 iframe host for narrow. No console errors or exceptions in any shot. Frames are in C:\Users\Cory\AppData\Local\Temp\claude\S--\90ed2a60-e34a-41ef-b258-25144edd2387\scratchpad\fwr (shots, reg, v, st, m).

### Earlier findings

1. **Scene text in the 16:10 preview: fixed.** The compact 600x470 scene is used at 680x425 and 800x500. The smallest scene text is 10.3 px at 680x425, 11.4 px at 800x500 and 10.3 px at 1000x625 (measured font size times stage scale over every visible text node), and the stage has no big empty bands now (shots/s680x425_*.png, s800x500_*.png).
2. **Match controls in the preview: partly fixed, now the other half is under the fold.** Radius, Hub, Time, Board at and Turn are all on screen at 680x425 and 800x500. But Previous/Next target (y 435 to 479) and Check, Show my curve, Reveal (y 485 to 529) are now under the fold at 680x425, and Check is cut off at 800x500. Play and Restart in Match sit at y 618 to 662, so they are under the fold at all three compact sizes, 1000x625 included (shots/s1000x625_match.png). So at 680x425 a student can change the wheel but has to scroll the panel to Check it. How serious: should fix.
3. **First tap and the Ride welcome: fixed, but it broke Read.** Clicking Unit Circle first, then Ride, plays and marks unitWelcome and then rideWelcome (v/v1). Sound off then on as the first taps works too (v/v4). But now a welcome that gets cut off stays unsaid, and the page-wide click listener queues it again after every click. Read hushes, starts the hint, and then the queued welcome cuts the hint off. Seen two ways. With Read as the very first tap, the welcome plays instead of the hint (v/v2: last = the Ride welcome, said = []). With Unit Circle, then Read 1.5 s later, the Unit welcome starts over and the hint never plays (v/v3). Read works once that mode's welcome has played to the end (v/v3b). Restart during the welcome also restarts the welcome from the beginning (v/v6). Where: src.html lines 970-984 (the click listener plus narrate, together with the Read handler at line 1049). How serious: should fix. Read has to read the hint.
4. **"Try boarding from the side" on any wheel change: fixed.** It now speaks only while Board at is Bottom. A first click on Right side, then Left side, says only the Ride welcome (v/v5).
5. **Unit Circle label collisions: fixed in the wide and tall scenes, but they come back in the compact scene.** At 1400x900, "1 radian, about 57.3 degrees" sits clear of π/2, and "0, 2π" is clear of the graph's "height" label (reg/11_unit_rad.png). At 375 px the label is inside the circle and clear (m/n375_unit_rad.png). At 680x425 the label "1 radian, about 57.3°" runs into radian mark "3" (it reads "31 radian,"), and mark "4" touches "57.3°" (m/s680_unit_rad.png). How serious: nit.
6. **Height line through tick labels: fixed.** The line breaks before the graph axis, so "20", "0.5" and "height (m)" are clear (m/w_clear.png, m/w_unit_unroll.png, m/s800_real_t.png).
7. **Stack layout, Play and the graph: fixed.** The clock row sticks to the bottom. At 760x900 the graph ends at y 833 and Play is at 850 to 894. At 375x812 the graph ends at 734 and Play is at 762 to 806, with no scrolling needed (st/st760_*.png, st/st375_*.png). There is no horizontal scroll.
8. **"Clamped" note: fixed.** Chicago now reads "Clamped to the Ride ranges: turn 540 to 120 s. Rounded to the slider steps: radius 38.1 to 38 m, hub 42.3 to 42 m." High Roller lists radius, hub and turn as clamped, which is correct.
9. **Singapore Flyer opening: fixed on screen.** It now reads "public rides from February 14, 2008; officially opened April 15, 2008". Small leftover: the tool.draft.json Sources line still says "opened April 2008". How serious: nit.
10. **Spec says Sound is off by default:** unchanged. It is a spec wording issue, not a tool bug. How serious: nit.
11. **Compact equation bar wrap: fixed.** Each part is now its own unbroken line at 680x425.

### New

12. **Compact Ride with Show sideways distance and Show arc traveled: labels collide.** At 680x425, "x = 15.0 m" is printed over the wheel's spokes and rim. "turns: 1.25" runs into "ground, height 0", so it reads "turns: 1.25ground, height 0". "you" sits on the arc stroke (m/s680_ride_x.png, zoomed in z680x.png). The readouts panel still shows x. How serious: nit, because these are optional toggles in the preview.
13. **Ride at 680x425: the Turn buttons start at y 426,** just under the 425 px fold. The "Turn" label shows but the buttons don't. How serious: nit.
14. **The art is in, but the tool is still a draft.** tool.draft.json has not been renamed to tool.json, and art/prompts.json still has `"review": "pending"`. Until then, a plain `bundle_tool.py` skips the tool and the site keeps it on the bench. This is a step for Cory or the builder, not a bug in the tool.

### Regression checks (all pass)

- **Ride math:** 3 / 18 / 33 / 18 / 3 m at t 0 to 40, rim speed 2.36 m/s. All 8 board and direction equations and their curves are unchanged. Radius 40 pushes Hub to 41 with the clearance hint. r 40, D 60, P 10 gives 12 turns.
- **Drags and keys:** dragging the car a quarter turn gives t 10, h 18. Dragging the dot to t 30 moves the car to the left side. A drag during Play pauses. Arrow keys step π/12, Tab reaches the car, and the focus ring shows.
- **Unit Circle:** three π/6 steps give π/2, sin 1.000. θ = 7 gives 401.1°, sin 0.657, cos 0.754. The identity line reads 1.000. Unroll ends under the graph dot (629.9 vs 629.86). The graph is full at 4π.
- **Real Wheels:** the four fact cards, model values and speeds match the earlier sourced check. London at 10 min is 105 m (75 − 60 cos 2π/3). Four kept curves show with labels.
- **Match:** the 8 targets give the same results as before. Each matches its own wheel. 5 fails CW, 6 fails CCW, 8 fails CW (gaps 40, 40, 16 m). The equivalent wheels match. The default wheel against target 1 gives a 28 m gap at t 60. Target 4 gives the one-slow-turn note.
- **Motion off:** One radian and Unroll jump to the end, and Play moves in 0.25 s steps.
- **Art:** the bundle inlines one image/webp (art/river-night-sky.webp, 1600x914): a dark navy sky, faint stars, a distant lit shoreline, no people, no text. It sits behind the wheel pane in Ride and Match and doesn't get in the way of any labels at any size.
- **Voice:** the bundle has 18 data:audio/mpeg clips, one per line in voice/lines.json (18). local.json lists the same 18. The bundler reported no missing recordings.
- **Contract:** one file, no network URLs, no buttons under 44 px at any size checked, no em dashes, "Curio" appears alone only as the kit's JS name.

## Voice helper migration

2026-10-27. Narration moved from the tool's own queue onto the kit's `Curio.voice` (docs/KIT.md "Voice"). The spoken lines, the hints and `allLines()` are unchanged word for word (18 lines, still equal to voice/lines.json), so no clip needs recording again. The tool's queue, pump, hush, Read handler, `saidChange` flag and first-tap code are gone (31 lines of voice code down to 6 lines of setup).

Line kinds: the four mode welcomes go through the `welcome` option. `matchYes` is the one event line (spoken on every match). `rideDrag`, `rideChange`, `rideBoard`, `unitRadian`, `unitUnroll`, `unitCosine`, `realPeriod` and `full` are how-to or teaching lines (spoken once, then silent). Each line is checked when its turn comes: `rideBoard` only while Ride boards at the bottom (needs Right side shown), `full` only while the graph is still full (needs Restart), `rideChange` after `full` has had its turn (needs the Radius slider), the Unit Circle lines only while their rod, unrolled arc or cosine is still on screen, and `matchYes` only while that target's match is still on screen. The hint stays the tool's own (the mode hint, or the "graph is full" and "hub raised" notes), so lines never write it.

How it was checked: rebundled, then driven in muted headless Chrome (own profile, port 9671) with held clicks (press, 120 ms, release) through `scripts/drive.py`, once on the old build and once on the new one, in the same 26 fresh-page runs. A hook on the page logged every clip that really started, ended or was cut; on the new build V.log's spoken and read lines matched those clips exactly in all 26 runs. No console errors or exceptions. `python scripts/check_tools.py` passes; `python scripts/test_voice.py` passes 25 of 25.

| Check | Old build | New build |
|---|---|---|
| Pause x5 (rideDrag, how) | 1 | 1, then 4 silent |
| Bottom x5 (rideBoard, how) | 1 | 1, then 4 silent |
| Graph full x5 (full, rideChange, how) | 1 each | 1 each, then 4 silent each |
| One radian, Unroll, Show cosine, a wheel in Real Wheels x5 (how) | 1 each | 1 each, then 4 silent each |
| Check with a matching wheel x5 (matchYes, event) | **1** | **5** |
| Check with a wrong wheel x5, Step pi/6 x5 | nothing | nothing |
| Play, Pause, Bottom, Right side, fast | rideBoard plays with Right side chosen | rideDrag dropped (newer), rideBoard dropped (stale) |
| Graph full, then the car dragged back to t 30 s | full and rideChange play anyway | full dropped (stale), rideChange never queued |
| Match, then the radius changed before "Matched" | "Matched" plays on a wheel that no longer matches | matchYes dropped (stale) |
| Play, Pause, Bottom, Unit Circle, Restart, fast | the queued lines are marked said without playing | dropped by the hush, unmarked |
| First tap: stage, Play, Tab key, mode button | welcome | welcome (mode button: the new mode's) |
| First tap: Bottom (a control with its own line) | rideBoard, then the Ride welcome | rideBoard only; the welcome stays unsaid |
| First tap: Read, then Sound off and on | hint read; the welcome is marked said and never plays | hint read; the Ride welcome plays on Sound on |
| First tap: Sound off, Sound on | nothing until the next tap | the Ride welcome on Sound on |
| Read during a welcome, then One radian | One radian's line cuts Read off after 1.3 s | Read plays to the end (9 s), then unitRadian |
| Read, then a mode change right away | the new welcome starts at once | the same |
| Read with Sound off | reads the hint | the same |
| Sound off, Unit Circle, One radian, Sound on | nothing | unitRadian silent; Unit welcome plays on Sound on |

Hint at the STANDARDS sizes (not changed by this migration, the layout is the same): 14 to 16 px everywhere, no horizontal scroll. It is on screen at 1000x625 and up in every mode. It is below the fold in the compact panel for Ride and Match at 680x425 (top 437 and 444) and for Match at 800x500, and below the stage in the stack layout (760x900 at y 1357, 375x812 at y 882). With how-to lines now silent after their first time, the hint is the only place they stay visible, so this matters a little more than before.

Not changed, worth a later look: the welcomes in Unit Circle and Real Wheels, and "Matched", do not name the next action and control; a failed Check has no spoken line.

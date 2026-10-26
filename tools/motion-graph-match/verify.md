FIX: the physics is right, but a Hand lag that can make a perfectly tracked run fail, a voice timing bug after Read, and two text collisions need fixing.

Verified cold on 2026-10-25 against spec.md, docs/POLISH.md and BATCH-G11.md. Built with `CURIO_DRAFT=1 python scripts/bundle_tool.py motion-graph-match` after the art (track-bench.webp) and the 13 voice clips landed. I drove it in headless Chrome over CDP (my own copy of cdp.py, with held clicks of 120 ms) and stepped the physics through `__tool.drive`. No console errors or exceptions in any frame. The only error was a host-page favicon 404 in the 375 px iframe host.

## Findings

1. **Hand control: steady lag (src.html:236-264, TUNE.handBrake/handSoft/handLook/follow). Should fix, close to a blocker for Race fairness.**
   - What is wrong: the cart chases the pointer with a braking law and no feed-forward. A steady 1 m/s drag trails the pointer by 0.52 m (measured: pointer at 7.00 m, cart at 6.48 m). That is more than the 0.4 m position band.
   - Effect on scores (pointer placed exactly on the target, `pointer = B.x(t)`):
     - Target 1 scores 56 percent.
     - Target 2 scores 11 percent.
     - Target 9 scores 57 percent.
     - Target 3 scores 65 percent.
   - Hand is the suggested control on targets 1 and 2. Leading the pointer by 0.3 to 0.7 s gives 100 percent on 1, 2 and 9. So a careful run can top 80 percent (Done when 7 passes), but only through a hidden trick. The obvious move ("put the cart on the line") is punished hardest on target 2.
   - The spec wanted lag only on fast flicks ("a fast flick makes the cart lag behind"). It also described Hand as x following the pointer, with v and a as smoothed differences. notes.md does tell teachers to "lead a little". But students drive this tool alone, so the fix belongs in the model, not the notes.
   - Suggestion: add the smoothed pointer velocity as feed-forward, so a steady drag tracks within about 0.1 m. Keep the 3 m/s cap and the 2 m/s² rate limit for flicks.

2. **Voice: a cut Read still blocks queued lines (src.html:1154-1155, narrate/hush/readP). Should fix.**
   - What is wrong: `hush()` stops the Read clip, but it never resets `readP`. A paused clip fires neither `ended` nor `error`, so `readP` only settles on its timeout of 2.5 s plus 80 ms per character (up to about 10 s). Every line queued after that waits.
   - Seen with held clicks:
     - Race, then Read, then Start at about 5 s: "Three, two, one, go." started at 11.9 s. That was about 4 s into the run, after the countdown had finished.
     - Race, then Read, then card 6 at 2.8 s: the turnaround question started at 11.6 s, after 8.7 s of silence.
   - Suggestion: `readP = Promise.resolve()` inside `hush()`.

3. **Show links: labels collide late in a run (x graph). Should fix.**
   - Frame 1400x900_explore_links_late (cursor at 11 s): "change in x = 1.6 m" is drawn on top of "slope 0.30 m/s". The text is unreadable.
   - Both labels are pushed to the left of the cursor when it is near the right edge, at about the same height.
   - Early cursors are fine. At 680x425 the labels are tight but readable.

4. **Show all three: the kink note is clipped in small boxes (drawTarget, src.html:605-610). Should fix.**
   - At 680x425 the note "a real cart needs a sudden large push" is cut off at the graph's right edge ("needs a sudden lar"). At 375 px it reads "sudden l".
   - At 1000 px and wider it fits. The kink arrow also runs through the text in those two sizes.

5. **First tap held more than 350 ms on the Race button (src.html:1140). Nit.**
   - The timeout narrates the welcome for `state.mode`, which is still Explore at that point. With a 500 ms press, the Explore welcome starts, plays for about 0.17 s, and is cut by the Race welcome.
   - Because it started, it is marked said, so Explore never gives its welcome later.
   - At 120 ms this does not happen. The fix is to narrate the button's mode, or to skip the timeout for mode buttons.

6. **Stale control lines queue up (narrate). Nit.**
   - Clicking Hand and then Throttle during a Read queues both lines. The Hand line plays in full (7.6 s) even though Throttle is already picked, and the Throttle line starts 12 s after its click.
   - Suggestion: drop a queued control line when another control is picked.

7. **Done when 2: Throttle at 1.0 m/s for 5 s from rest gives x +4.71 m, not 5 m. Nit, and it comes from the spec.**
   - The v readout reads 1.00, as it should.
   - The 2 m/s² rate limit in the spec costs at least 0.25 m, and the 0.2 s easing costs the rest. Over seconds 1 to 6 the rise is exactly 5.0 m.
   - Teacher-facing wording should say "about 5 m" or "rises 1 m each second".

8. **Graph titles sit under the traces (frames 1400x900_explore_hand_run, race_results*). Nit.**
   - A v trace at 2 to 3 m/s, or an a trace near +2, runs through the "Velocity v (m/s)" and "Acceleration a" titles. The halo keeps the text readable.
   - The "target" label also sits on the trace start on several targets.
   - At 1400x900 the bottom tick label of one graph ("0" or "−3") nearly touches the top tick label of the next ("3" or "2").

## Checked and correct

- **Targets:** I recomputed all 10 targets on my own from the spec's piecewise definitions (Python).
  - The tool's values match the spec and mine exactly.
  - End positions: 1 at 8, 2 at 1, 3 at 9 (still moving at 0.25 m/s, which the spec allows), 4 at 8, 5 at 8.5, 6 at 1.75, 7 at 8, 8 at 2.5, 9 at 9, 10 at 2.
  - Target 6 reaches its farthest point, 6.25 m, at 3 s.
  - Every target loads at its x0. Target 6 starts at 1.5 m/s, and its card says "starts moving".
- **Slopes and areas:** v is the slope of x, and a is the slope of v.
  - Over whole runs with every control, the largest gaps are 0.05 between slope of x and v, 0.000 between slope of v and a, and 0.003 between the area under v and the change in x. The spec allows 0.1 (Done when 5).
  - Near an end stop the gap is large, as expected: the stop's push is left out of the a record by design.
  - On-screen labels agree, for example: slope 1.75 m/s with v = 1.75 m/s, slope 0.50 m/s² with a = 0.50, area 3.1 m with change in x 3.1 m.
- **Done when 3 (Pedal):** 0.2 m/s² for 5 s gives v = 1.00 m/s and x up 2.50 m, the a line is flat, and the arrow reads 0.40 N. F = m a with 2.0 kg is right everywhere I looked: 0.80 N at −0.4 m/s², 2.87 N at 1.43 m/s².
- **Top speed:** Pedal at 2 m/s² clamps v at 3.00, a reads 0.00, the note "top speed" shows, and the force arrow hides (net force is 0).
- **End stops (Done when 4):**
  - Driving into 10 m: x clamps, v goes to 0, there is no spike on the a graph (minimum a 0), and one "end stop" mark appears at the bottom. A left-stop hit is marked at the top.
  - Pushing the Pedal into the stop: the cart stays parked, the arrow shows 2.00 N with "the end stop pushes back", and a reads 0.00.
  - Reversing the Pedal pulls the cart away normally.
- **Hand (Done when 1):** a drag from 1 m to 7 m gives a rising x, a v bump (peak 2.98), and a positive then negative a (+2.00, then −1.45).
- **Keyboard on the cart:** holding an arrow moves at 1.00 m/s, and Shift gives 0.30 m/s.
- **Scoring:**
  - Sitting still on target 1 scores 28 percent, with RMS 3.88 m (Done when 7).
  - Match percent is samples in band out of 240.
  - RMS is printed with units (m, m/s, m/s²). An early Stop shows "(first 6 s)", and missing samples count as misses (50 percent on a perfect half run).
  - Ties keep the older best (strict `>`).
  - Exact Pedal input on targets 4 to 10 scores 100 percent with RMS 0. Exact Throttle input scores 100 percent on targets 1, 4, 5, 6 and 9, 87 percent on 10, and 68 percent on 3. On target 3 the jump from rest to 1.5 m/s at t = 0 costs about 0.6 m that the student must make up. That is fair as a challenge.
- **Race:**
  - Ghost trace and ghost cart: dotted, in step with the run.
  - Bests survive reloads (shared profile). "Forget my bests" clears memory, localStorage and the ghost after the confirm.
  - Hard-way tags appear on the card, the target name and the results (for example target 9 with Pedal).
  - Show all three draws open gaps at the kinks, with the "a jumps here" note.
  - The picker greys out during a run.
- **Motion off:** the countdown digits drop the zoom class, and traces still move.
- **Voice with held clicks:**
  - The first tap on Throttle or Pedal plays the Explore welcome in full, then the control line.
  - The first tap on Race plays only the Race welcome.
  - The first tap on the track plays the Explore welcome.
  - Start cuts the welcome and "Three, two, one, go." starts at once (when no Read happened first).
  - Read cuts the welcome and reads the hint.
  - With Sound off, nothing is narrated and Read still speaks.
  - Card 6 plays the turnaround line after the Race welcome.
  - All 13 lines are in lines.json, allLines() and voice/local.json word for word. The longest is 97 characters, and none has a symbol a voice would misread.
- **Layout:** 1400x900, 1280x720, 1000x625, 800x500, 680x425 (compact, controls visible without scrolling), 760x900 (stack), and 375 px in an http-served iframe host (stack, scrollWidth 375, no sideways scroll). Scene text is 11 px or more in every size.
- **Contract:**
  - One file, with no network URLs. kit:curio, kit:theme-912 and kit:graphing (Plane) are used.
  - Tab order: header, cart (Hand only), run buttons, Start at, control picker, slider, then the target cards last.
  - Graph cursor stops are focusable only with Show links on, and arrows move the cursor with a readable aria-valuetext.
  - Enter on Start begins the countdown and focus moves to Stop. Slider keys step 0.1 and announce "0.3 meters per second".
  - Lines are told apart by dash pattern (solid, dotted, dashed), not by color alone, and the two area fills use different patterns.
- **Art:** track-bench is an empty dark bench and rail, with no people. It is marked people: false and drawn at 40 percent under a wash.
- **Words:** no em dashes in src, notes or lines. "Curio Class" is written in full in user text.
- **Sources:** OpenStax UP1 ch 3 and 5.3, OpenStax Physics ch 2, NGSS HS-PS2-1, McDermott 1987, Beichner 1994. Every number on screen is either a model constant from the spec or computed.

## What I was unsure of

- Whether finding 1 is a blocker or only "should fix". It does not break the physics, and a student who watches the trace will learn to lead. But the suggested control punishes the most natural strategy (11 percent on target 2), so I would not ship Race without fixing it.
- I did not test real touch dragging on a phone. All Hand driving was scripted pointer input or CDP mouse.

## Re-verify

FIX: the Hand lag, the Read delay, the kink note and the voice nits are fixed. But the Hand feed-forward fix brought a new problem: with real mouse input, the acceleration graph is mostly noise. Show links labels also still collide in the compact embed sizes.

Re-checked cold on 2026-10-25. I rebuilt with `CURIO_DRAFT=1 python scripts/bundle_tool.py motion-graph-match` (454 KB) and served it over http. I drove it in muted headless Chrome over CDP (my own cdp.py copy with real mouse presses, 120 ms holds, and an audio play/pause log). I ran the MOTION ENGINE block, taken unchanged from src.html, in Node to check the physics. The art (1 webp) and all 13 clips are inlined, and the only network URL is the SVG namespace. No console errors or exceptions. The only error was a favicon 404 from the test server.

### Earlier findings

1. **Hand lag: fixed.**
   - A steady drag now trails by 0.017 m at 0.5 m/s and 0.033 m at 1 m/s (it was 0.52 m).
   - Pointer placed exactly on the target scores: target 1 100 percent, target 2 87, target 3 93, target 9 100.
   - The 87 percent ceiling on target 2 holds up. Work it out by hand:
     - The cart cannot know the pointer will turn until it turns.
     - With a 2 m/s² limit, a reversal that starts at 6 s leaves the cart out of the 0.4 m band from about 6.25 s to 7.75 s.
     - That is 31 of the 240 samples, so 209/240 = 87 percent. No control law that reacts after the fact can beat it.
   - It is a ceiling only for a pointer exactly on the line:
     - A pointer that rounds the turn early (a 2 m/s² parabola from 5.5 s to 6.5 s) scores 100 percent.
     - A plain 0.3 s lead scores 91 to 93 percent.
     - So "a careful run scores over 80 percent" holds, and notes.md says this accurately.
   - Flicks do not overshoot:
     - A step of the pointer from 2 m to 7 m peaks at 7.001 m, with one push and one brake on the a graph.
     - A 2 m to 2.5 m step overshoots by 0.001 m.
     - A sudden stop from 1 m/s runs 0.23 m past the pointer and comes back. That is the 2 m/s² limit (at least 0.25 m to stop), as the notes say.
2. **Voice, a cut Read blocking queued lines: fixed.** `hush()` now resets `readP`. Measured with held clicks:
   - Race, then Read, then Start at 5 s: "Three, two, one, go." starts at the Start click (0 ms after it). Before, it started 5.6 s late.
   - Race, then Read, then card 6: the turnaround line starts at the card click. Before, it came after 8.7 s of silence.
3. **Show links labels colliding: fixed at the reported size, still present in compact sizes. Should fix.**
   - I swept the cursor every 0.2 s over four runs (Hand ramp, slow Throttle, Throttle out and back, Pedal). For each step I checked whether any two `text.lk` boxes overlapped.
   - No overlaps at 1000x625, 1280x720, 1400x900 or 760x900.
   - At 680x425, the 16:10 embed size, labels overlap at many cursor positions: 32 to 56 of 60 on three of the four runs. Frames:
     - `680x425_links_pedal_c60`: "change in x = 2.2 m" sits on top of "slope 1.50 m/s" on the x graph, and the area label clips the v slope label.
     - `680x425_links_slow_c20`: "slope 0.00 m/s²" is drawn under the "Velocity v (m/s)" title and its "you control this" tag. The detector missed this one because the title is not `.lk`.
   - At 800x500 and at 375 px, on the out-and-back run at 5.2 to 5.6 s, "slope −2.00 m/s²" covers "v = 0.40 m/s" (`800x500_links_outback_c108`).
4. **Kink note clipped: fixed.**
   - At 680x425, 800x500 and 375 px the graph shows a short "a jumps here", and the full sentence moves into the results panel.
   - At 1000 px and wider the two-line note fits inside the plot. No overlaps, and nothing runs past the frame.
5. **First tap held on Race: fixed.** With a 500 ms press on Race, only the Race welcome plays.
6. **Stale control lines: fixed.**
   - Read, then Throttle, then Pedal: the Throttle line is dropped. The Pedal line plays after Read ends, and Read is not cut off.
7. **Throttle 1 m/s for 5 s gives +4.71 m: fixed in the words.** notes.md now says "position climbs 1 m every second". The physics is unchanged and correct.
8. **Graph titles under traces: mostly fixed, nit left.**
   - The tick labels between graphs no longer touch (about 20 px apart at 1400x900).
   - An a trace that sits at +2 still runs along the "Acceleration a (m/s²)" title (`1400x900_race_t2_all3`). The kink note has the trace running through it. The halo keeps both readable.

### New finding

9. **Hand: the acceleration graph is noise under real mouse input (src.html, step(), TUNE.handFF and follow). Blocker for Explore with Hand, which is the default.**
   - What is wrong: the cart's wanted velocity now includes the pointer's own velocity, smoothed over only 0.1 s. The applied acceleration is then (wanted − v) / 0.1, which multiplies any ripple in the pointer's speed by 10. Real pointer positions come in whole pixels (about 90 px per meter at 1400x900) and arrive per frame with uneven timing. So the feed-forward ripples, and the a graph and the force arrow follow the ripple.
   - How I saw it:
     - Frame `drag1400`: a real CDP mouse drag of the cart at a steady pace of about 0.55 m/s. The a trace swings between −1.9 and +1.9 m/s² over the whole drag, and the force arrow flickers (3.33 N in the frame). The a band is ±0.15 m/s².
     - Frame-timed drag (one integer-pixel move per animation frame, a very smooth mouse): the a trace alternates ±0.19 every sample, with spikes to ±0.9 (standard deviation 0.28). With fractional pixels it is worse (standard deviation 0.48, peak 1.27).
     - Node simulation of the same engine, 1 m/s drag, 60 Hz frames with 30 percent timing jitter and 1/90 m pixels:

       | Feed-forward smoothing (`handFF`) | Standard deviation of a |
       |---|---|
       | 0.1 s (shipped) | 0.65 m/s² |
       | 0.2 s | 0.45 m/s² |
       | 0.3 s | 0.38 m/s² |
       | none (the old law) | 0.04 m/s² |

       Lag and the target 2 score do not change with the smoothing (87 percent in every case).
     - With an ideal analytic pointer (how `__tool.drive` and the builder's tuning feed it), the a graph is clean. That is why this only shows with real input.
   - Effect: Done when 1 and the notes' 5-minute start ask "why does the acceleration graph go up and then down?" after a drag. The real answer is buried in ±1 to 2 m/s² of jitter, on the default control, in the first minute.
   - Suggestion: low-pass the feed-forward much harder, or estimate the pointer velocity with a regression over the last 0.15 to 0.3 s (the spec's own smoothing window), and soften the `follow` gain. Then re-check with real or pixel-quantized, frame-jittered input, not analytic pointers.

### Physics and voice regressions (no change found)

- **Targets:** all ten end positions match the spec and my own numeric integration. Target 6 peaks at 6.25 m.
- **Done when 2:** v = 1.000. **Done when 3:** x +2.500 m, v 1.000, a flat at 0.200, F 0.40 N.
- **Top speed:** clamps at 3 m/s, with a = 0 and the top flag set.
- **End stops:**
  - Driving into 10 m: x = 10, v = 0, one stop mark, a stays between 0 and 2 (no spike).
  - Pedal into the stop: parked, push 2 m/s² held.
  - Reversing pulls away.
- **Keyboard:** 1.000 and 0.300 m/s.
- **Done when 1:** a scripted drag from 1 m to 7 m gives a positive then negative a, and the cart ends at 7.000 m.
- **Slopes and areas:** the largest gaps over sine-driven runs, by control:

  | Control | slope of x vs v | slope of v vs a | area under v vs change in x |
  |---|---|---|---|
  | Hand | 0.020 | 0.000 | 0.0006 |
  | Throttle | 0.004 | 0.000 | 0.0004 |
  | Pedal | 0.000 | 0.000 | 0.0004 |

- **Scoring:**
  - Sitting still on target 1 scores 28 percent, RMS 3.88 m.
  - Exact Pedal input scores 100 percent on targets 4 to 10.
  - Exact Throttle input scores 87 on target 10 and 68 on target 3, as before.
- **Voice, with held clicks, all as BATCH-G11 asks:**
  - The first tap on the track gives the Explore welcome.
  - The first tap on Throttle gives the welcome, then the Throttle line.
  - Start cuts the Race welcome, and "go" starts at once.
  - Read cuts the welcome.
  - With Sound off, nothing is narrated and Read still speaks.
  - Card 6 plays the turnaround line.
  - A hard-way Start plays the hard-way line.
  - lines.json, `allLines()` and local.json hold the same 13 lines.
- **Layout:**
  - The page layouts are compact at 680x425, 800x500 and 1000x625, wide at 1280x720 and 1400x900, and stack at 760 and at 375.
  - scrollWidth equals the width everywhere, including inside the 375 px http iframe host.
- **Words:** no em dashes in src.html, notes.md or lines.json.

## Final check

FIX: Show links is fixed, and steady, start-stop and flick drags now give a clean acceleration graph under real mouse input. But a natural drag that eases to a stop (the kind notes.md step 1 asks for) still draws the slowing-down half of the a graph as a jagged comb, and it starts about 1 s late.

Checked cold on 2026-10-25, narrow to findings 9 and 3 plus a short regression. I rebuilt with `CURIO_DRAFT=1 python scripts/bundle_tool.py motion-graph-match` (461 KB) and served it over http. I drove it in muted headless Chrome over CDP in two ways: real `Input.dispatchMouseEvent` drags, and synthetic whole-pixel PointerEvents scheduled in the page. Both used 60 Hz moves with 30 percent timing jitter, and some runs used 125 Hz. Nothing used `__tool.drive`. Sizes were 1280x720 (77.8 px per meter) and 680x425 (28 px per meter). No console errors or exceptions. The only error was a favicon 404 from the test server.

### Finding 9: Hand acceleration under real input. Mostly fixed, one should-fix left.

- **Steady drags: fixed.** I read a over the steady part of each drag, from 2 s in to just before the stop. The two input methods agree.

  | Drag | Size | sd of a (m/s²) | largest a | samples outside ±0.15 | lag, mean / max (m) |
  |---|---|---|---|---|---|
  | 1 m/s | 1280x720 | 0.033 to 0.035 | 0.13 | 0 of 110 | −0.02 / 0.04 |
  | 0.5 m/s | 1280x720 | 0.020 to 0.024 | 0.09 | 0 of 150 | −0.01 / 0.03 |
  | 1 m/s, 125 Hz | 1280x720 | 0.030 to 0.032 | 0.16 | 0 to 1 of 110 | −0.02 / 0.04 |
  | 1 m/s | 680x425 | 0.072 to 0.077 | 0.24 | 6 to 7 of 110 | −0.02 / 0.06 |
  | 0.5 m/s | 680x425 | 0.037 to 0.044 | 0.19 | 0 to 2 of 150 | −0.02 / 0.05 |

  - At 680x425 the misses are single samples at 0.17 to 0.24. They read as a slight fuzz, not noise. The last round measured an sd of 0.65 m/s² with swings to ±1.9.
  - Lag is small everywhere. A negative lag means the cart sits a few cm ahead of the pointer.
- **Start-stop drag at a constant speed: clean.**
  - Test: 0.6 m/s from 1 m to 5 m.
  - The a graph shows a +2 push for 0.6 s, then a flat line (largest a 0.07 at 1280, 0.21 at 680), then a −2 brake for 0.7 s, then a small +0.3 settle.
  - Frame: `680x425_startstop_cdp60`.
- **Fast flick: clean.**
  - Test: the pointer jumps from 1 m to 8 m in 0.25 s.
  - The a graph shows +2 for 1.5 s, then about −1.06 for 3.3 s.
  - The cart stops at 7.995 to 8.000 m with no overshoot. Both sizes match.
- **Sudden stop: bounded, but more overshoot than the code comment claims. Nit.**
  - The cart always comes back and settles within 0.005 m of the pointer. Nothing runs away.
  - Peak overshoot against the 2 m/s² minimum:

    | Speed at the stop | Overshoot | Minimum at 2 m/s² |
    |---|---|---|
    | 0.6 m/s | 0.19 to 0.20 m | 0.09 m |
    | 1.0 m/s | 0.40 to 0.46 m | 0.25 m |
    | 1.2 m/s | 0.50 to 0.60 m | 0.36 m |

  - The MOTION ENGINE comment says "up to about 0.25 m".
  - In some runs the a graph shows a forward blip of +0.2 to +1.0 at the moment of the stop, before the brake. Frame data: `1280x720_steady1_syn60`, +0.98 at 8.4 s.
  - Likely cause: for the first 0.1 s of idle, the linear fit keeps extrapolating the pointer forward before the fade starts.
- **New: a drag that eases to a stop draws a jagged down half. Should fix.**
  - Test: smooth human-style drags, with a minimum-jerk path from 1 m to 7 m over 8 s and over 5 s, and a cosine ease from 1 m to 5 m over 6 s.
  - The speed-up half of a is smooth and close to the pointer's true acceleration.
  - The slowing-down half is wrong in two ways:
    - **Late.** On the 8 s drag the true a turns negative at 4.5 s and reaches −0.5. The graph stays between −0.01 and −0.13 until about 5.7 s, and the v graph shows a flat top in that time.
    - **Jagged.** The graph then jumps between about −0.1 and −1.0 on neighboring 0.05 s samples, while the true a is a smooth −0.1 to −0.54. The rms change from one sample to the next is 0.23 to 0.26 m/s² at 1280x720. On the 5 s drag at 680x425 it is 0.39 to 0.46, with spikes to −2.
  - Both input methods show it at both sizes.
  - Frames: `1280x720_mj8_cdp60` (the comb from 5.7 s to 8.5 s is plain to see) and `680x425_mj5_cdp60`.
  - The cart also overshoots a gentle stop by 0.13 to 0.21 m and then comes back.
  - Why it matters: notes.md step 1 is "drag the cart from 1 m to about 7 m and let go", then "why does the acceleration graph go up and then down?" A real hand eases in and out like this. The up half reads well. The down half reads as a noisy band that starts late. All of its samples are negative, so the sign is still right.
  - Likely cause (not proven): the slowing-down branch in `tracker().get` swaps the linear fit for the quadratic fit only while the short fit is slower by more than one pixel's worth. On a steady deceleration that test flips on and off from frame to frame, and `step()` turns each flip into an acceleration step through `follow` (0.3 s).
  - Suggestion: add hysteresis to the switch, or blend the two fits by how far apart they are, or always use the quadratic fit on the long window once its curvature is significant. Re-check with the same eased drags at both sizes.

### Finding 3: Show links label collisions. Fixed.

- Test: the cursor swept every 0.2 s (61 positions) over five runs: Hand ramp, Hand flick and back, slow Throttle, Throttle out and back, and Pedal.
- Sizes: 680x425, 800x500, 375 px (inside the http iframe host) and 1280x720.
- The check: on every step, does any `text.lk` box overlap any other text in the stage (titles and tags included), or run past the stage edge?
- Result: 0 overlaps and 0 out-of-frame labels on all 20 sweeps.
- Graphs shorter than 110 px (680x425, 800x500, 375) now print each link once. The detector does see those labels (for example "slope 0.97 m/s" and "area = change in x = 4.7 m").
- scrollWidth equals the width at every size.
- Frames: `links_680x425_outback`, `links_800x500_outback`.

### Regression (no change found)

- **Race, with real clicks held 120 ms:**
  - Start counts down and runs.
  - A real mouse drag on target 1, following the target in step with the run, scored 100 percent.
  - Replay plays (phase replay), then returns to done.
  - Try again loads the ghost, and the ghost group is visible during run 2. Run 2 with no input scored 28 percent and kept the best at 100.
- **Voice after Read is still prompt:**
  - Race, then Read, then Start 3.1 s later: Read is paused and "Three, two, one, go." starts within 1 ms of the Start click.
  - Race, then Read, then card 6: the turnaround line starts within 1 ms of the click.
- **Nit, comment only:** src.html:597 says "press anywhere on the track to grab it there". But the track art is `.deco` (`pointer-events: none`), so only a press on the cart grabs it. The words students see all say "drag the cart", so only the comment is wrong.

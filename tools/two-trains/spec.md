# Two Trains

## One idea
The gap between two trains on the track is the vertical gap between their two lines on the graph, so the meeting is the moment that gap hits zero, and when the trains have the same speed and direction the gap never changes and they never meet. The three 8.EE.C.8 cases (one solution, no solution, infinitely many) are things you see happen on a railroad.

## Not like
- phone-plan-showdown (grade 7, roleplay): two cost lines and "which plan is cheaper after how many minutes", argued by characters. Here the lines are moving trains, the crossing is a place and a time you watch happen, and the no-solution and infinitely-many cases are the point.
- intersection-quest (grade 9, graphing): one system solved three ways against a timer. Here there is no timer and no method drill; one graph, one track, and you change the system by dragging.
- ski-slope-designer (grade 8, graphing): slope as a feeling on one line. Here slope is speed, but the subject is two lines and their gap.
- story-graphs (grade 8, graphing): match written stories to graph shapes. Here every line is a train you set up and run, never a story to match.
- motion-graph-match (grade 11): one cart, linked x, v and a graphs, matching targets. Here two objects on one distance-time graph, constant speeds only.
- ferris-wheel (grade 11, same format): one object seen two ways (wheel and sine graph). Here two objects, and what matters is the space between them.
- collision-lab (grade 11): carts that hit. Here trains never touch: the line has two tracks and trains pass side by side.
- model-my-world, data-detective (grades 8 to 9): fit or write one equation from data. Here the equations are given by the settings and the question is where two of them agree.

## Who and how
- Grade 8, math. Module: Linear Equations and Systems. Standards: 8.EE.C.8 (8.EE.C.8a graph shows the solution as the intersection; 8.EE.C.8b solve algebraically, including no solution and infinitely many; 8.EE.C.8c real-world problems with two linear equations).
- Students drive on laptops, alone or in pairs; also works on a projector for a teacher demo.
- 10 minutes for Yard alone; 25 to 35 minutes with Dispatch.
- Band 6-8, first tool of the band: light theme, the tool sets its own `:root` colors (do not link `kit/theme-912.css`). Link `kit:curio` then `kit:graphing`. Playful but never babyish: a scene, a small earned celebration, no mascot, no stickers.

## Screens and modes
Header: title "Two Trains", subtitle "Systems of linear equations", mode buttons (`.seg`) **Yard** and **Dispatch**, then kit buttons **Motion**, **Sound**, **Read**.

Stage (left, drawn at real pixel size and re-laid out per size, like collision-lab and motion-graph-match):
- **Scene strip** (top, about 20 percent of stage height, at least 90 px): the Prairie Line drawn left to right from Ashford (mile 0) to Brookport (mile 300) over the `prairie-backdrop` art. Two rails drawn in code (Train A always rides the upper track and Train B the lower one, so the two never overlap in the picture whatever their directions; both tracks run the whole way). Station posts with names at their miles. Train A and Train B images ride at their current mile; a big white letter "A" or "B" on a dark rounded badge is drawn in code on each. A train that has not left yet waits at its station, faded to 40 percent with the label "departs 1:00 pm". A train that arrived sits at the terminus labeled "arrived". A gap bracket between the two trains reads "gap 120 miles" when **Show gap** is on.
- **Graph** (below): `Plane` with x = "time (hours after noon)" 0 to 7, y = "distance from Ashford (miles)" 0 to 300; grid every 0.5 h and 15 mi, labels every 1 h and 60 mi, `ticks: 'edge'`. Under each hour label a small clock label (12 pm, 1 pm ... 7 pm).
- **Route ladder**: a thin vertical copy of the line drawn just left of the graph's y axis, aligned to the y scale, station names at their miles, with a small A and B marker at each train's current mile. This is the bridge: a train's height on the ladder equals its line's height on the graph at the clock time.
- On the graph: each train's line solid from its departure to its arrival (or 7 h), its equation as the curve label; the same equation dashed and faint outside that span (the equation keeps going, the train does not). A departure dot (draggable) and a speed handle (draggable, see Interactions). A vertical **clock cursor** at the current time (draggable), with a clock tab above the plane drawn by the tool (its own pointer and keyboard handling); clicking anywhere on the plane also sets the clock. With **Show gap** on, a vertical segment between the two lines at the cursor, labeled with the gap. The meeting point (when there is one) gets a ring and a label "meet 3:00 pm, mile 180".

Panel (right; under about 900 px tall use this buttons-first order, compact):
1. Status banner (one of the four in Content), always visible.
2. Clock row: **Play** / **Pause** (one toggle), **Jump to meeting** (disabled when there is none), **Restart** (clock to 0), clock readout "2:15 pm (t = 2.25 h)".
3. Train cards A and B, side by side when the panel is wide enough, else stacked. Each: direction buttons **Eastbound** / **Westbound**, sliders with number boxes **Starts at (mile)**, **Departs**, **Speed (miles per hour)**, then the equation in two forms (Content).
3. Dispatch only: the card text with **Check**, **Show a hint** and **Next card** (and card 6's prediction boxes), right under the clock row so Check is visible without scrolling at 1366x768 and 1280x720.
4. Train cards (see 3 above).
4b. Dispatch only: the row of 8 numbered ticket buttons (title on hover and in the label), after the train cards.
5. Toggles **Show gap**, **Show the algebra**. The algebra box (Content) shows under the toggles.
6. Yard only: **Presets** dropdown, then the fact line (Content).
7. Hint paragraph `hint`.

### Yard (default)
Free play. Change either train any way; everything updates live, including during Play. Presets load a setup and restart the clock.

### Dispatch (optional challenge)
A row of 8 numbered ticket-shaped buttons (the current card's title shows above its text). Picking one loads its setup, locks the controls the card says are fixed (shown greyed with a small lock icon and "set by dispatch"), and shows the card text with **Check**, **Show a hint**, and **Next card**. Card 6 adds two boxes, "Your meeting time" (a clock time or hours after noon; placeholder "like 1:45 pm") and "Your mile" (placeholder "like 95"; neither placeholder is the answer), that must be filled before **Play** is enabled; after the meeting the card shows "You said 3:00 pm at mile 150. They met at 3:00 pm at mile 150." Card 7 has **It can't be done** instead of Check. A correct answer shows an "On time" stamp right then (it clears on any change, on picking a card, and on a wrong Check; earlier solves show only as the tick on their ticket). The stamp is drawn in code, rail-ticket style, with a short two-note horn chime. The tick is remembered on this device (localStorage `curio-two-trains`, try/catch; works without it). No points, no timer, no streaks. Until card 6's trains meet: the status reads "Your call"; the ring, meeting label, algebra and Jump are hidden; each line is drawn only up to the current clock and grows as the trains run (no dashed full lines); Show gap is disabled; the clock moves only with Play (the clock tab, plane clicks and arrow keys are off, with a tip). The equations stay in the panel and legend, since students predict from them. After the meeting everything shows as usual. The hint line is "card-predict" on card 6 and "card-twice" on card 7 (they have no Check); other cards use hint-dispatch.

## Content
The Prairie Line (fictional; both tracks run the whole way). Stations and miles from Ashford: Ashford 0, Cedar Flats 45, Millbrook 120, Pine Hollow 180, Granite Falls 240, Brookport 300.

Train A: the passenger express, color `--gr-1`, art `train-a`. Train B: the freight, color `--gr-2`, art `train-b`. Each train is: direction (east = +, west = minus), start mile p (0 to 300, step 5), departure time s (0 to 4 h, step 0.25 h = 15 minutes, shown as a clock time 12:00 pm to 4:00 pm), speed v (10 to 100 miles per hour, step 5). Signed rate m = +v east, minus v west.
- Story form: d = m(t − s) + p, for example "d = 60(t − 1) + 0". Slope-intercept form: d = mt + b with b = p − m s, for example "d = 60t − 60". Shown with a true minus sign, coefficients via `Plane.fmt`.
- Running span: from t = s until it reaches its terminus (mile 300 east, mile 0 west) or t = 7. A train never runs past a terminus; it stops there.
- Direction change: if a train would start at its own terminus (eastbound at 300, westbound at 0), its start moves to the other end and the hint says "An eastbound train can't start at Brookport, so it starts at Ashford."
- Fact line in the panel in Yard (on screen only): "Real US track rules: on Class 4 track, freight trains may run up to 60 miles per hour and passenger trains up to 80 (49 CFR 213.9)." Kept per integrator decision 2 because the exact source is cited in notes.md and Sources.

Status banner (computed from the two equations, then checked against both running spans):
1. **One meeting**: lines cross at a time when both trains are running. "They meet at 3:00 pm, 180 miles from Ashford (Pine Hollow)." Station name only when the mile is within 0.5 of a station.
2. **Never meet**: same signed rate, different b. When the gap on the track really is constant from 0 to 7 h: "Same speed, same direction: the gap stays 45 miles forever. No solution." Otherwise (a train waits or stops at the end): "Same speed, same direction: the lines stay 100 miles apart and never cross. No solution. On the track the gap changes while a train waits to leave or after it stops at the end of the line." The first-never voice line plays only in the constant case.
3. **Always together**: same signed rate and same b. "Same equation: wherever one is, the other is too. Infinitely many solutions." Plus the span when both run: "Side by side from 2:00 pm to 5:00 pm." If the spans never overlap: "Same equation, but they are never on the line at the same time."
4. **Lines cross, trains don't meet** (banner title, with a plain why sentence): crossing exists but outside the time both trains run (or past 7 pm). "The equations cross at 4.5 hours before noon, at mile −180. The trains never meet on the track." Negative hours read "hours before noon".
Time shown to the nearest minute plus hours to 2 decimals; a value that is not exact gets "about". Miles to 1 decimal, written "about mile 171.4" (not "mile about 171.4").

The algebra box (built from the current settings, live):
- One meeting example (default): "A: d = 60t" / "B: d = −40t + 300" / "Set them equal: 60t = −40t + 300" / "100t = 300" / "t = 3, so 3:00 pm" / "d = 60(3) = 180 miles".
- Never (preset 3): "35t + 45 = 35t" / "45 = 0. That is never true: no solution."
- Always: "60t = 60t" / "0 = 0. That is always true: infinitely many solutions."

Presets (Yard), all recomputed in Python:
1. "Head on" (default): A east, mile 0, 12:00 pm, 60. B west, mile 300, 12:00 pm, 40. Meet 3:00 pm, mile 180, Pine Hollow.
2. "Catch up": A east, 0, 12:00 pm, 40. B east, 0, 1:00 pm, 60. Meet 3:00 pm, mile 120, Millbrook.
3. "Same speed": A east, 45, 12:00 pm, 35. B east, 0, 12:00 pm, 35. Never meet, gap 45 at every time 0 to 7 h. (Changed from 50 mph: at 50, A reaches Brookport at about 5.1 h and B catches it there, so the gap was not 45 at every time. At 35, A reaches mile 290 and B mile 245 at 7 pm.)
4. "Same schedule": A east, 0, 12:00 pm, 60. B east, 120, 2:00 pm, 60. Always together, side by side 2:00 pm to 5:00 pm.
5. "Too slow to catch": A east, 45, 12:00 pm, 50. B east, 0, 12:00 pm, 40. Lines cross at t = −4.5 (4:30 hours before noon), mile −180: not on the track.

Dispatch cards (locked = fixed by the card; tolerance: exact on the slider steps):
1. "Meet at Millbrook": A east, 0, 12:00, 40 (locked). B west, 300, 12:00 (locked). Set B's speed. Answer 60 (meet 3:00 pm, mile 120). Hint: "When does A reach Millbrook? B has that long to cover 180 miles."
2. "The catch": A east, 0, 12:00, 40 (locked). B east, 0, speed 80 (locked). Set B's departure so B catches A at Granite Falls. Answer 3:00 pm (meet 6:00 pm, mile 240). Hint: "A reaches mile 240 at 6:00 pm. How long does B need for 240 miles?"
3. "Hold the gap": A east, 45, 12:00, 35 (locked). B east, 0, 12:00 (locked), B starts at 20. Make the gap stay the same the whole trip. Answer 35 (gap 45, Never meet). (Changed from 50 for the same reason as preset 3.) Hint: "Turn on Show gap and watch it as you change B's speed. When does it stop changing?"
4. "One schedule": A east, 0, 12:00, 60 (locked). B east, 120, 2:00 pm (locked). Give B the same equation as A. Answer 60 (Always together). Hint: "Write both equations in d = mt + b form and compare."
5. "Late start": A west, 300, 12:00, 40 (locked). B east, 0, speed 60 (locked). Set B's departure so they meet at Millbrook. Answer 2:30 pm (meet 4:30 pm, mile 120). Hint: "A reaches Millbrook at 4:30 pm. B needs 2 hours to get there."
6. "Call it first": A east, 0, 1:00 pm, 75. B west, 300, 12:00, 50 (all locked). Predict the meeting, then Play. Answer 3:00 pm (t = 3), mile 150 (between Millbrook and Pine Hollow). Accept time within 1 minute and mile within 1. Hint: "Set 75(t − 1) equal to 300 − 50t."
7. "Meet twice": nothing locked. Make A and B meet at two different places. Hint: "Try every case: lines that cross, lines side by side, and the same line. How many meetings does each give?" Check is replaced by **It can't be done**, which shows: "Two different straight lines cross at most once. The only way to meet more than once is the same line, and then they meet everywhere, not twice." If the student reaches Always together first, the card says "That's infinitely many meetings, not two. Can you get exactly two?"
8. "Junction at four": A west, 300, 12:00 (locked). B east, 0, 12:00 (locked). Set both speeds so they meet at Granite Falls at 4:00 pm. Answer A 15, B 60. Hint: "A has 4 hours to go 60 miles. B has 4 hours to go 240."
A card is solved when its target holds in the current settings (cards 1 to 5 and 8 on Check; 6 after Play with the prediction within tolerance; 7 on It can't be done). Check on a wrong setting says what happened plainly, for example "They meet at 3:45 pm at mile 150, not at Millbrook." (B at 40 on card 1) and never reveals the answer.

## Interactions in detail
- **Departure dot**: at (s, p). Drag moves both start time and start mile (snap 0.25 h and 5 mi, and to a station within 3 mi). Arrow keys: left/right 0.25 h, up/down 5 mi. Its `aria-valuetext`: "Train A departs 1:00 pm from mile 0".
- **Speed handle**: on the train's line one hour after departure, at (s + 1, p + m), shown as a small square with "+60 mi in 1 h". Locked to the vertical line t = s + 1 (engine `lock: {x}`); dragging up or down sets the signed rate (snap 5), and crossing the departure height flips direction. Speed stays 10 to 100; direction flips skip the zero band. When s + 1 is past 7 the handle sits at s + 0.5 and reads per half hour.
- Sliders, boxes, buttons and dots all drive the same state; the equation text, the lines, the scene and the status update together. Locked controls ignore drags and keys and say "set by dispatch" on focus.
- **Play**: the clock runs from the current time to 7:00 pm at 2 seconds per hour (14 s full run); trains move in the scene and on the ladder; the clock cursor sweeps. At a meeting moment during Play: a short two-note horn chime (both trains), the trains flash once, and the meeting label appears on the graph and a small flag at that mile in the scene. With Motion off, Play jumps the clock to the end and shows the final frame; the meeting label still shows.
- **Clock cursor**: draggable along t (0 to 7, snap 0.05 h, arrow keys 0.25 h); dragging pauses Play. The scene, ladder, gap and clock readout follow it.
- **Jump to meeting**: puts the cursor at the meeting time (only for One meeting).
- **Show gap**: off by default; first turn-on queues the gap line. Gap at the cursor is |dA − dB| using where the trains actually are (a waiting train counts at its station; an arrived train at its terminus). When neither has left, the label says "not left yet".
- Changing any setting during Play keeps playing from the current time.
- Mode switch calls `Curio.stop()`, pauses, keeps Yard settings separately from the Dispatch card.
- First-time voice beats (once per page load): first meeting seen during Play, first Never meet, first Always together, first "not on the track", first Show the algebra.
- Keyboard: Space = Play/Pause, R = Restart clock (when focus is not in a text box). All targets at least 44 px; visible focus in `--focus`.
- Extremes: two trains at the same mile and time at departure count as One meeting at that instant. A meeting exactly at a terminus at arrival counts (card 2 meets at 6:00 pm, not at arrival, but test 300-mile meets too). Meetings exactly at t = 7 count.

## Look
Light 6-8 theme set on `:root` by the tool. Accent `--brand: #8c2f39` (railway maroon; no built tool uses it; the graphing neighbors use orange #f2a93b and cyan). `--paper: #fbf7ef` (warm ticket paper), `--panel: #ffffff`, `--ink: #22303c`, `--muted: #5b6470`, `--line: #d9cfbf`, `--focus: #c2410c`. Graph: `--gr-1: #c2410c` (Train A, solid), `--gr-2: #1d4ed8` (Train B, dashed `10 6`), grid and axis variables set by the tool in warm greys. Contrast: brand on paper 7.61, white on brand 8.14, ink on paper 12.63, muted on paper 5.61, A color on paper 4.85 and on white 5.18, B color on paper 6.27. Letters A and B always ride with the colors (badges, curve labels, panel cards), so color is never the only signal. Ticket-style Dispatch cards with a perforated edge drawn in CSS. Celebration is the stamp and chime only, no confetti.

## Art
FLUX via `scripts/cfart.py`; no people anywhere.
- `prairie-backdrop`: "wide flat golden prairie under a pale blue sky, low distant hills, a few cottonwood trees, soft afternoon light, flat illustration style"; 5:1; cutout no; people no; full-width backdrop of the scene strip (rails, stations and labels drawn in code over it).
- `train-a`: "side view of a short maroon and cream passenger train, one streamlined locomotive and two coaches, blank plain sides, flat illustration, plain white background"; generated 4:1, delivered 693x160 (4.33:1); cutout yes; people no; Train A in the scene at its own aspect ratio (no squash), wheels on the rail, the A badge over the middle, mirrored when westbound.
- `train-b`: "side view of a short blue freight train, one diesel locomotive and three plain boxcars, blank plain sides, flat illustration, plain white background"; generated 4:1, delivered 865x160 (5.41:1); cutout yes; people no; Train B at its own aspect ratio, wheels on the rail, the B badge over the middle, mirrored when westbound.
Drawn in code: rails, stations, ladder, graph, letter badges, flags, gap bracket, stamp, tickets.

## Voice
Bank voice `news-reader` (Rasalgethi), style "Say clearly and warmly, like a friendly train station announcer" (integrator decision 1). Not used by any neighbor (graphing and grade 11 simulators use hs-narrator Kore) or by the recent batches. Fits a station announcer. Lines:
1. yard-welcome: "Two trains, one railroad, one graph. Change a train's start, departure time or speed, then press Play and watch where they meet."
2. yard-ladder: "The strip beside the graph is the railroad turned on its side. Each train sits at the height of its line."
3. first-meet: "They met. On the graph, that is exactly where the two lines cross."
4. first-never: "Same speed, same direction. The gap never shrinks, so the lines never cross. That system has no solution."
5. first-always: "Same equation. The two lines sit on top of each other, so every point is a solution."
6. first-offtrack: "The equations cross, but at a time when the trains are not both running. On the track, they never meet."
7. gap: "The gap between the trains is the distance between the two lines, straight up and down."
8. algebra: "Setting the two equations equal finds the one time when both trains are at the same mile."
9. dispatch-welcome: "This is dispatch. Each ticket sets part of a schedule. You set the rest so the trains do what the ticket asks."
10. card-solved: "On time. Nice work."
11. card-predict: "Work out the meeting time and mile first. Then press Play and see if you called it."
12. card-twice: "Can two straight lines cross twice? Try it, and if you think it can't be done, say so."
13. hint-yard: "Drag the round dot to move a departure. Drag the square to change the speed."
14. hint-dispatch: "Locked settings come from the ticket. Change the others, then press Check."
Hints shown in `hint` and read by Read are lines 13 and 14 plus the current status banner text (read by browser voice fallback).

## Family engine
`kit/graphing.js` unchanged: `Plane` with `ticks: 'edge'`, `tickFormat` for clock sublabels; `g.fn` per train with `domain` for the running span (solid) and a second dashed, faint `g.fn` for the full equation; `color: 1` and `2`; `g.point` for departure dots (`snap` function to 0.25 h, 5 mi and stations), speed handles (`lock: {x: s + 1}`), and the meeting ring (not draggable); `g.trace` or a locked point for the clock cursor; `g.segment` for the gap; `g.label`; `g.intersect` is not needed (closed form: t = (b2 − b1) / (m1 − m2)), but use exact arithmetic on the step grid. The scene strip and route ladder are the tool's own SVG positioned with `g.px` for the ladder. Sliders via `Plane.slider` with `box: true`, `format` showing "1:15 pm" for Departs and "60 miles per hour" as `aria-valuetext`. The tool must define `--gr-1`, `--gr-2`, `--gr-grid`, `--gr-grid-major`, `--gr-axis`, `--gr-text` itself, since it does not load the 9-12 theme.

## Sources
- 8.EE.C.8 text: Common Core State Standards, Grade 8 Expressions and Equations. https://www.thecorestandards.org/Math/Content/8/EE/
- Systems with one, no, or infinitely many solutions (parallel and coincident lines): OpenStax, Elementary Algebra 2e, 5.1 Solve Systems of Equations by Graphing. https://openstax.org/books/elementary-algebra-2e/pages/5-1-solve-systems-of-equations-by-graphing
- Distance = rate x time, uniform motion problems: OpenStax, Elementary Algebra 2e, 3.5 Solve Uniform Motion Applications. https://openstax.org/books/elementary-algebra-2e/pages/3-5-solve-uniform-motion-applications
- Freight 60 and passenger 80 miles per hour on Class 4 track: 49 CFR 213.9, Classes of track: operating speed limits (also at https://www.law.cornell.edu/cfr/text/49/213.9). https://www.ecfr.gov/current/title-49/subtitle-B/chapter-II/part-213/subpart-A/section-213.9
- Prairie Line, its towns and miles, train settings, presets and cards are invented for the tool (fine per integrator decision 4). All meeting times and miles above were recomputed in Python with exact fractions (default 3 h, 180 mi; cards 1 to 8 as listed; preset 5 crosses at t = −4.5, d = −180).

## Done when
1. Default "Head on": status reads "They meet at 3:00 pm, 180 miles from Ashford (Pine Hollow)"; Play shows the trains passing at Pine Hollow when the cursor reaches t = 3, with the chime and graph ring at (3, 180).
2. Preset "Same speed" shows Never meet with "gap stays 45 miles", the gap label reads 45 at every cursor time, and the algebra box ends "45 = 0 ... no solution".
3. Preset "Same schedule" shows Always together, "side by side from 2:00 pm to 5:00 pm", and the algebra box ends "0 = 0 ... infinitely many solutions".
4. Preset "Too slow to catch" shows the not-on-the-track banner with 4.5 hours before noon and mile −180.
5. Dragging Train B's speed handle changes the slider, both equation forms and the line together; flipping direction by dragging works; keyboard on dots and sliders gives the same results.
6. Each Dispatch card's listed answer passes Check and a wrong value fails with a plain description that does not reveal the answer; card 6 needs both predictions before Play; card 7 accepts It can't be done.
7. At 1366x768 the status banner, Play, and both trains' speed and departure controls are visible without scrolling; at 375 wide (iframe host) the tool is usable; scene text is at least 10 px in the 680x425 preview.
8. Motion off: Play jumps to the final frame with no animation and the same status; Sound off makes no audio; Read reads the hint and status.
9. Every number on screen matches a Python recompute with units; no em dashes, no network requests, no console errors.

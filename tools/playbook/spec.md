# Playbook

## One idea
Draw your team's runs and passes on a top-down field, press Test play, and watch defenders that follow simple, visible rules react, so you find out for yourself that moving into open space beats standing still.

## Not like
- stage-blocker (6-8 arts, builder): places actors on a top-down stage for an audience to see. Playbook's top-down pieces are teams in a game, and the test is a match against defenders that move.
- fitness-circuit (3-5 PE, race): a projected workout timer for the body. Playbook is a strategy board for the mind; nobody moves in the room.
- rules-referee (6-8 PE, escape): calls real sport rules on clips. Playbook uses one tiny made-up game so the lesson is tactics (space, give and go, marking), not rules.
- robot-mouse-mail (grade 1 CS, puzzle): plans a path with arrow commands. Playbook paths are drawn freely and timed against moving opponents; the point is open space, not sequencing.

## Who and how
- Grade 3-5, Physical Education, module Game Strategies (offense, defense and space in games).
- Driver: students or teacher (pairs on a laptop, or the teacher on a projector with the class calling out where to run).
- Minutes: 15-30. Fits right before an invasion game in the gym (soccer, basketball, ultimate, handball, flag games).
- Standards: SHAPE.S2 (applies tactics: creating space, reducing space), SHAPE.S3 (social skills: every player has a job, teammates communicate).
- Topic line: "offense, defense and open space".
- Modes (tool.json): ["Offense", "Defense", "Playbook"].

## Screens and modes
Header: title "Playbook" with small line "Offense, defense and open space", mode buttons **Offense**, **Defense**, **Playbook** (keys 1 to 3), then **Motion**, **Sound**, **Read**. Stage (the field) on the left; panel on the right, below the stage under 760 px wide.

Focus in every mode: the field. It is the biggest thing on screen, centered on the stage; in Offense the eye is on the play you draw and then the ball's flight, in Defense on your defenders against the attack's faint paths, in Playbook on the mini fields of the play cards.

### The field (all modes)
- Top-down rectangle 30 units long and 20 wide, drawn at real pixel size per box (no fixed-scene scaling). The attack moves left to right. The end zone is x 25 to 30, striped.
- Attackers: three orange circles numbered 1, 2, 3. Defenders: navy squares lettered A, B, C. Shapes differ, not only color. The ball is a yellow dot with a dark ring, held beside its player.
- Under the field, a beat strip: 8 numbered beats (1 second each) with a playhead, and pass markers sitting on their beats.

### Offense (opens first)
- Starting spots: 1 at (5, 10) holding the ball, 2 at (8, 4), 3 at (8, 16). Defense is set by a **Defense card** in the panel: **Mark everyone**, **Guard the space**, **Pressure and mark** (Content). Defenders start at the card's spots.
- Draw a run: tap a player to select it (it gets a thick outline), then tap up to 4 points on the field; a dotted path with arrowheads joins them. Drag a point to move it. **Clear run** removes the selected player's path.
- Add a pass: **Add pass**, then tap the thrower, then the catcher; the pass appears on the next free beat after the previous pass. Drag a pass marker along the beat strip to change its beat. Up to 3 passes. **Remove pass** removes the last one.
- **▶ Test play** runs the play. Then **🐢 Replay slow** (half speed), **⏯ Step** (one beat at a time), **✏ Edit** (back to drawing, everything kept).
- **Show open lanes** toggle: from the ball holder to each teammate, an open lane is a solid light-green line with a check, a blocked lane is a white dashed line with an X. Shown while drawing (from starting spots), while paused and while stepping.
- Results banner over the field after a test: "Score!", "Picked off by B", "Caught, but no score. Time!", "Time! The ball never moved." Plus one line saying why (Content).

### Defense
- An offense play from the book attacks (pick it from a list of the six sample plays and the student's saved plays). Its runs show as faint dotted paths before the test so you can read them.
- Drag each defender anywhere in x 10 to 30. Tap a defender to cycle its job: **Mark 1**, **Mark 2**, **Mark 3**, **Guard space**, **Pressure ball**. The job shows as a tag beside it.
- **Defenders: 3 / 2** toggle (2 removes C).
- **▶ Test defense**, **🐢 Replay slow**, **⏯ Step**, **✏ Edit**. Banner: "Stopped them!" or "They scored."

### Playbook
- A list of plays: the six samples (locked, can be loaded and changed as a copy) and up to 8 saved plays. Each card shows a mini field with the runs, the name, and which defense cards it beat in its last test (three small badges with check or dash and words).
- Buttons: **Save this play** (asks for a name from a word list: two taps, a color word and an animal word, for example "Orange Hawk"; no typing), **Load**, **Delete**, **Clear all saved** (confirm).
- Challenges (optional, a short checklist below the list, ticks remembered on this device): see Content.
- Strategy cards: five cards that flip (Content).

## Content

### The game on screen: End Zone Pass (made up, shown once as a rule card)
1. The player with the ball can't run. Pass it to a teammate.
2. Catch a pass in the end zone to score.
3. If a defender gets to the ball, it's picked off.
4. A play lasts 8 beats.
5. Defenders stay 2 steps back from the player with the ball.

### Simulation rules (fixed, so the same play always gives the same result)
- Units: field units. Tick 50 ms, 160 ticks per play (beat b starts at tick 20 x (b - 1)). Attackers move 4 units per second (0.2 a tick), defenders 3.4 (0.17 a tick), the ball 10 (0.5 a tick). A mover that is closer to its target than one tick's step lands on it.
- Each tick runs these steps in this order (the order matters; the sample results below come from it):
  1. Passes: on the first tick of a pass's beat, if its thrower holds the ball, the ball leaves the thrower's spot; otherwise the pass is skipped and the banner reason says "Pass 2 skipped: 3 didn't have the ball".
  2. Attackers: every attacker except the holder moves toward its next waypoint and drops the waypoint on reaching it. The holder stands still until it passes, then runs its remaining path. The catcher of a ball in flight keeps running its path; once it catches, it is the holder and stands.
  3. Defenders move toward a target worked out from this tick's spots. Mark N: one unit goal-side of attacker N (its spot plus 1 in x), or 2 units when N holds the ball. Guard space: home is where it started; the attacker nearest home (ties go to 1, then 2, then 3), if within 6 units of home, plus 1 in x (2 if it holds the ball); else home. Pressure ball: 2 units goal-side of the holder; while the ball flies, the ball's spot.
  4. The ball moves toward the catcher's current spot.
  5. Picked off: if the ball is within 0.8 units of a defender (checked A, then B, then C), that defender picks it off and the play ends.
  6. Caught: if the ball is within 0.7 units of the catcher, the catcher holds it; a catch at x 25 or more is a score and the play ends.
- After tick 160 the play ends on Time.
- Lanes: a lane is blocked when any defender is within 1.5 units of the straight line from holder to teammate.

### Defense cards (Offense mode)
| Card | A | B | C |
|---|---|---|---|
| Mark everyone | (11, 4) Mark 2 | (11, 16) Mark 3 | (9, 10) Mark 1 |
| Guard the space | (13, 5) Guard space | (13, 15) Guard space | (21, 10) Guard space |
| Pressure and mark | (11, 4) Mark 2 | (11, 16) Mark 3 | (7, 10) Pressure ball |

### Sample plays (start spots as in Offense; paths are waypoints; passes as beat: thrower to catcher)
| Name | 1 | 2 | 3 | Passes |
|---|---|---|---|---|
| Give and go | after passing: (14, 11), (25, 12) | (15, 5) | (14, 18) | 1: 1 to 2; 5: 2 to 1 |
| Clear out | after passing: (12, 10) | (20, 2), (27, 5) | (12, 18), (12, 12) | 1: 1 to 3; 5: 3 to 2 |
| Crossing | (none) | (14, 14), (26, 15) | (14, 6), (26, 5) | 4: 1 to 2 |
| Stack | (none) | (10, 8), (18, 4), (26, 4) | (10, 10), (18, 17), (26, 16) | 3: 1 to 3; 5: 3 to 2 |
| Spread | after passing: (16, 10), (26, 10) | (8, 1), (20, 2) | (8, 19), (20, 19) | 1: 1 to 2; 5: 2 to 1 |
| Long throw | (none) | (27, 5) | (12, 15) | 6: 1 to 2 |
Results with the rules above (reference run, Sources; the sample cards show these, and the builder's own test must give the same):
| Sample | Mark everyone | Guard the space | Pressure and mark |
|---|---|---|---|
| Give and go | picked off by C (about 5.5 s) | Score (1, about 5.6 s) | Score (1, about 5.6 s) |
| Clear out | Score (2, about 6.0 s) | picked off by C (about 5.2 s) | Score (2, about 6.0 s) |
| Crossing | picked off by C (about 3.2 s) | picked off by B (about 4.3 s) | picked off by C (about 3.2 s) |
| Stack | picked off by C (about 2.1 s) | Score (2, about 5.5 s) | picked off by C (about 2.1 s) |
| Spread | Score (1, about 5.9 s) | picked off by A (about 4.4 s) | picked off by C (about 4.2 s) |
| Long throw | picked off by C (about 5.1 s) | Score (2, about 7.2 s) | picked off by C (about 5.1 s) |
Every defense card is beaten by at least two samples, no sample beats all three, and Crossing beats none (a play that needs changing is part of the lesson).

### Why lines (banner second line), first match
- Picked off: "{letter} was in the lane. Check Show open lanes before you pass." ({letter} is the defender who picked it off.)
- Caught short of the end zone: "Good catch. Next, run deeper before the pass comes."
- Time with no pass: "Someone has to get open. Draw a run away from a defender."
- Score against Mark everyone: "Your runner was faster than the marker. Sharp cuts make space."
- Score against Guard the space: "You found the gap between zones."
- Score against Pressure and mark: "You got the pass off before the pressure closed in."
- Defense stopped them: "Your defenders took away the open space."
- Defense scored on: "Look for the runner nobody was marking."

### Challenges (optional, Playbook mode)
1. Score against Mark everyone with one pass.
2. Score against Guard the space.
3. Score against Pressure and mark.
4. Score with every attacker touching the ball.
5. In Defense, stop Give and go.
6. In Defense, stop Spread with only two defenders.

### Strategy cards (front / back)
1. Get open / Move to space away from defenders, so the passer has a clear lane.
2. Give and go / Pass, then run to space to get it back.
3. Spread out / Players who stay wide pull defenders apart and open the middle.
4. Mark up / Stay between your player and the goal you defend.
5. Talk / Call out who you are marking, so no one is left open.

## Interactions in detail
- Tap and drag with real pointer input (whole-pixel, jittered) must hit points on the first try: a waypoint's hit area is 44 px even though it is drawn at 14 px. Points snap to half units and stay inside the field.
- Drawing a path for the holder: its run starts after its own pass. If the holder never passes, its path shows faded with a tip "1 has the ball. Add a pass so 1 can run."
- During a test the Test button becomes **■ Stop**. Stop, **⏯ Step**, **Show open lanes** and the mode buttons stay live and act at once: Stop returns to Edit at beat 0 mid-flight; Step pauses on the current tick and then moves a beat per press; the lanes toggle shows or hides at once. Drawing (players, points, passes) waits for Edit, because changing a play mid-run would change the play being tested.
- Step: each press moves one beat (20 ticks) and pauses; lanes show. Replay slow uses the same ticks at half speed. Motion off: the play still runs (it is the content), but the ball trail and banner pop-in are removed.
- A pass to the thrower itself is not allowed (the catcher tap is ignored with a buzz and the hint says "Tap a teammate").
- Saving stores plays only (paths, passes, name) in localStorage key `playbook-plays`, wrapped in try/catch; Clear all saved removes it.
- Sizes: at 1366x768 the field is at least 640 px wide; at 1000x625 and in the preview sizes the beat strip and Test button stay visible; under 900 px tall the panel puts Test play and the mode's main buttons first.
- Tab order: panel controls, then players, then waypoints. Arrow keys move a selected waypoint by half a unit.

## Look
- Accent `--brand` #1e7a3c (field green), on a light theme on its own `:root`: paper #f3f7f0, ink #1d2a22, muted #4f5f55, line #d3e0cf, focus #e0662a (the accent differs from group siblings: purple, raspberry, amber, indigo, lime and coral; nearby 3-5 tools: germ-spread-sim #1f7a6a and label-detective #1d5c63 are teal).
- Contrast: accent on paper 4.96:1, white on accent 5.38:1, ink on paper 13.77:1, muted on paper 6.25:1.
- Field: turf #2f7a3a with lighter mowing stripes, white lines (5.3:1 on turf). Attackers orange #ff9a3c with dark #2a1500 numerals (8.24:1) and a white outline; defenders navy #1b2a6b with white letters (13.21:1) and a white outline (tokens 5.3:1 against turf through the outline). Ball yellow #ffe14d (4.07:1 on turf) with a dark ring. Open lane #b6ff8a (4.45:1).
- Chalkboard-style font for play names (Trebuchet MS or system fallback).

## Art
none: drawn in code. The whole tool is a top-down tactics board, a diagram: the field, the round and square tokens, the paths, lanes, beat strip and mini fields must sit at exact field units and move by the simulation every 50 ms, and the plain board is what makes open space readable. A painted field would add texture and nothing to learn.

## Voice
`lively-host` (Sadachbia): "Say with lively energy, like a friendly game show host", used here as a play-by-play announcer. Different from body-systems-tour (upbeat-guide), fitness-circuit (big-sister) and growing-up-q-a (clear-teacher). `Curio.voice`, scope mode plus play.

| Key | Kind | When it plays | Line | Stale when |
|---|---|---|---|---|
| wOff | how | entering Offense, first time | Welcome to the playbook. Tap a player, then tap the field to draw a run. | a player tapped; mode left |
| wDef | how | entering Defense, first time | Now you're on defense. Drag a defender, then tap it to give it a job. | a defender moved or tapped; mode left |
| wBook | how | entering Playbook, first time | Here are your plays. Tap a play, then tap Load to change it. | a play tapped; mode left |
| howPass | how | after the first run is drawn, if no pass exists | Tap Add pass, then tap who throws and who catches. | a pass exists |
| howTest | how | after the first pass is added | Tap Test play to see it run. | test started |
| howLanes | how | after the first picked-off result, if lanes are off | Turn on Show open lanes to see where a pass can go. | lanes turned on |
| score | event | each scoring result | Score! | Edit or Stop pressed |
| picked | event | each pick-off | Picked off! | Edit or Stop pressed |
| time | event | each Time result | Time! No score. | Edit or Stop pressed |
| stopped | event | each Defense stop | Stopped them! | Edit or Stop pressed |
| scored | event | each Defense score against | They scored. Move a defender and test again. | Edit or Stop pressed |
| why | event | after each result line | the eight Why lines above | Edit or Stop pressed |
| chall | event | each challenge ticked | Challenge done! | mode left |
Rule card and strategy cards are read on screen (Read speaks them).

## Family engine
none

## Sources
- SHAPE America, National Physical Education Standards (2024), Standards 2 and 3: https://www.shapeamerica.org/standards/pe/
- Invasion game tactics (creating space, give and go, marking, defending space, communication): Mitchell, Oslin and Griffin, Teaching Sport Concepts and Skills: A Tactical Games Approach, 4th ed. (Human Kinetics, 2021); Bunker and Thorpe, "A model for the teaching of games in secondary schools," Bulletin of Physical Education 18(1), 1982.
- End Zone Pass is an original made-up game for this tool; its no-running-with-the-ball rule is modeled on ultimate and netball (USA Ultimate Official Rules of Ultimate: https://usaultimate.org/rules/).
- Checks run (Python, 2026-10-29, a reference simulation of the rules above): with the old rules (marker 1 unit goal-side of the holder, pressure 1.5) the old samples gave 14 pick-offs in 18 tests: a marker one unit in front of a standing holder picks off every pass aimed within about 53 degrees of straight ahead, so Clear out beat all three cards and nothing else scored except Long throw against Guard the space; nudging waypoints a unit or two could not fix it. Fix: rule 5 (defenders stay 2 units from the holder; Mark and Guard use 2 units for the holder, Pressure 2 instead of 1.5), the exact tick order above, and new waypoints and beats for Give and go, Clear out, Stack and Spread (Crossing and Long throw unchanged); the results table is that run. The run is deterministic (each test repeated gives the same result). Defense checks: Give and go is stopped by 1,961 of 4,000 random three-defender setups inside x 10 to 30 (challenge 5), and Spread by 1,710 of 4,000 two-defender setups (challenge 6). Contrast in Look recomputed (WCAG 2.1): all match to rounding.

## Done when
1. Drawing a run with jittered whole-pixel taps places points where tapped; dragging moves them; Clear run clears only the selected player.
2. The same play and defense give the identical result on three runs (deterministic), and Replay slow and Step end in the same result.
3. A pass whose thrower lacks the ball is skipped and the banner says so.
4. The sample-play badges match a fresh test of every sample against every defense card, and the fresh test matches the results table in Content cell for cell (who scores or who picks it off).
5. Show open lanes marks a lane blocked exactly when a defender is within 1.5 units of it (verify agent recomputes two cases).
6. Defense mode: Give and go can be stopped with some placement of three defenders (verify finds one).
7. Saved plays survive a reload; Clear all saved empties the list; no other data is stored.
8. At 1366x768, 1000x625 and 760 wide the Test button and beat strip are visible without scrolling; at 375 wide in the host the field fits the width.
9. Each how-to line is spoken once per load; results speak every time.
10. Focus: at 1366x768 and 680x425 the field is the biggest, central thing in Offense and Defense, and during a test the ball and tokens are never covered by the banner until the play ends.
11. Tap while it plays: during a test, Stop returns to Edit at once mid-flight, Step pauses on the current tick, the lanes toggle shows at once, and no result line plays after Stop.

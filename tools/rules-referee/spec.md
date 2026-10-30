# Rules Referee

## One idea
You sit in the replay booth: scrub a short animated play frame by frame, line up the key moment with a real official's tool (an offside line, a step counter, a landing zoom, a split clock), make the call with the actual rule, and every right call opens part of the locker room lock.

## Not like
- playbook (3-5 PE, builder): designs plays in a made-up game to learn tactics. Rules Referee uses the real rules of four sports and the student judges plays, never designs them.
- captain-s-choices (9-12 PE, story): sportsmanship in a self-officiated sport, with no referee. Rules Referee is about knowing and applying the written rules.
- screen-time-detective, pressure-point (6-8 health): stories and data about the student's own life. Rules Referee is a sports rules escape room.

## Who and how
- Grade 6-8, Physical Education, module Sport Skills and Rules (invasion, net and striking games).
- Driver: students (teams of 2 to 4 on one laptop, talking each call through), or the teacher on a projector with the class voting.
- Minutes: 15-25.
- Standards: SHAPE.S1 (motor skills in invasion, net and striking/fielding games), SHAPE.S2 (applies knowledge of rules and concepts).
- Topic line: "rules of invasion, net and striking games".
- Modes (tool.json): ["Escape", "Replay booth"].

## Screens and modes
Header: title "Rules Referee" with small line "Rules of invasion, net and striking games", mode buttons **Escape**, **Replay booth** (keys 1, 2), **Motion**, **Sound**, **Read**.

### Escape (opens first)
- Focus: in the locker room, the four lockers and their locks across the middle of the stage; in the booth, the clip, which fills the stage.
- Stage, locker room view: the painted locker room (Art) with four painted locker cutouts standing in a row in front of it, each labelled in code by sport and icon: **Soccer**, **Basketball**, **Volleyball**, **Softball**. Each locker has a lock with three tumbler lights (code). The painted blank whiteboard on the wall carries, in code, "Game day order: Volleyball, Softball, Soccer, Basketball". The painted exit door has a four-slot keypad of symbols (code, with the painted symbol pictures on its keys).
- Tap a locker: the booth opens on that sport's next unsolved clip.
- Booth view: the clip fills the stage (players and ball drawn in code over the sport's painted surface, Art). Under it, the scrubber (time readout "t = 1.0 s", tenths), **▶ Play**, **🐢 Half speed**, **⏮ Back 0.1 s**, **⏭ Forward 0.1 s**, and the sport's booth tool button (Content). Panel: the question ("What's the call?"), four call cards, **🔑 Key moment** (enabled after one wrong call), **🚪 Back to the locker room**.
- A right call: a rule card (the call, the rule in plain words, the rulebook source), one tumbler lights, **Next clip** or, on the third, the locker swings open (the open-locker cutout replaces the closed one) and shows its painted symbol.
- Door: when all four lockers are open, tap the keypad, then tap the four symbols in the whiteboard's sport order. Right order: the door opens to the painted sunny field and a "Ready for game day" card listing the 12 calls. Wrong order: the keypad shakes and clears; no penalty.
- **Timer** toggle in the panel on the locker room view: **Off** (default), **15 min**, **25 min**. When time runs out: "Time! You opened 2 of 4 lockers." with **Keep going** (continues untimed) and **Start over**.

### Replay booth
- All 12 clips in a grid by sport; any clip opens in the booth with Key moment always on, and the call cards and rule card work the same. No locks, no timer. A good projector mode for teaching one rule.

## Content

### Booth tools (one per sport)
- Soccer, **Offside line**: drag a vertical line onto any player; it snaps to that player's x and shows for every frame.
- Basketball, **Step counter**: footprints appear under the ball handler, numbered from the moment the ball is gathered, and a "Dribble: on / off" light.
- Volleyball, **Touch counter and zoom**: tick marks count team touches since the ball crossed the net; the zoom lens enlarges the ball where it meets the floor or net.
- Softball, **Split clock**: two clocks both start at the crack of the bat; the ball clock stops when the ball reaches the fielder's glove at the base, the runner clock when the runner's foot reaches the base. Same start, so the smaller time got there first.

### Clips (positions in meters on the drawn field; team Red in filled circles, team White in rings; the ball yellow)
Soccer: attacking half seen from above, goal at the right (goal line x = 52, posts at y 30.3 and 37.7).
1. **Offside.** t 0: Red 7 at (20, 30) with the ball; Red 9 at (37, 42); White 4 at (36, 20), White 5 at (35, 45), White keeper at (50, 34). t 1.0: Red 7 passes; Red 9 at (39, 42). t 2.2: Red 9 receives at (44, 39), shoots, scores. Calls: **Goal**, **Offside: indirect free kick to White**, **Corner kick**, **Foul: direct free kick**. Right: Offside. Key moment t 1.0. Rule: at the moment a teammate plays the ball, an attacker in the opponents' half who is nearer the goal line than both the ball and the second-last opponent, and then plays the ball, is offside. (IFAB Laws of the Game, Law 11)
2. **Level is on.** As clip 1, but at t 1.0 Red 9 is at (36, 42), level with White 4, and runs past after the pass; scores at t 2.4. Calls: **Goal**, **Offside: indirect free kick to White**, **Goal kick**, **Throw-in**. Right: Goal. Key moment t 1.0. Rule: a player level with the second-last opponent is not in an offside position. (Law 11)
3. **Over the line.** t 0: Red 11 crosses from (46, 8); t 0.8: White 5 at (49, 31) heads the ball; t 1.3: the ball crosses the goal line at (52, 24), outside the post. Calls: **Goal kick**, **Corner kick to Red**, **Throw-in**, **Play on**. Right: Corner kick. Key moment t 0.8. Rule: when the whole ball crosses the goal line outside the goal, last touched by a defender, the attackers get a corner kick. (Law 17)
Basketball: half court from above, basket at the left (x 1.6, y 7.5).
4. **Too many steps.** t 0 to 1.4: White 5 dribbles from (10, 4) toward the basket (bounces every 0.45 s); t 1.5: catches the ball with both hands at (6, 6); t 1.7, 2.0, 2.3: three steps; t 2.5: shoots. Calls: **Travel: White loses the ball**, **Double dribble**, **Personal foul**, **Good basket, 2 points**. Right: Travel. Key moment t 1.5. Rule: after gathering the ball while moving, a player may take two steps to stop, pass or shoot. (FIBA Official Basketball Rules 2024, Art. 25)
5. **Dribble, stop, dribble.** t 0 to 1.2: White 8 dribbles from (12, 10) to (9, 10); t 1.2: holds the ball with both hands; t 1.9: starts dribbling again. Calls: **Double dribble: White loses the ball**, **Travel**, **Jump ball**, **Play on**. Right: Double dribble. Key moment t 1.9. Rule: once a dribble ends, a player may not dribble again until another player touches the ball. (FIBA Art. 24)
6. **Hit on the arm.** t 0: Red 4 at (5, 9) rises to shoot from inside the arc; t 0.6: Red's defender White 9 slaps the shooting arm (a flash at the forearm); t 1.2: the shot misses. Calls: **Shooting foul: 2 free throws**, **Shooting foul: 3 free throws**, **No call**, **Charge on the shooter**. Right: 2 free throws. Key moment t 0.6. Rule: a shooter fouled on a missed two-point try gets two free throws (three on a three-point try). (FIBA Art. 34)
Volleyball: side view, net in the middle (x 9), Red on the left.
7. **Four hits.** The ball comes over to Red; touches: t 0.5 Red 2 passes, t 1.3 Red 6 sets, t 2.0 Red 2 touches again to save a bad set, t 2.8 Red 4 hits it over. Calls: **Four hits: point to White**, **Play on**, **Net fault**, **Ball out**. Right: Four hits. Key moment t 2.8. Rule: a team may touch the ball at most three times before it goes back over the net (a block does not count). (FIVB Official Volleyball Rules 2025-2028, Rule 9.1)
8. **Net touch.** t 0.8: Red 4 spikes; t 1.0: her hand brushes the top band of the net (the net ripples); t 1.3: the ball lands in White's court. Calls: **Net fault: point to White**, **Point to Red**, **Four hits**, **Replay the rally**. Right: Net fault. Key moment t 1.0. Rule: touching the net between the antennae while playing the ball is a fault. (FIVB Rule 11.3.1)
9. **On the line.** t 0.6: White 3 spikes; t 1.4: the ball lands with its edge touching the end line on Red's side (zoom shows the contact patch overlapping the line). Calls: **Ball in: point to White**, **Ball out: point to Red**, **Net fault**, **Replay the rally**. Right: Ball in. Key moment t 1.4. Rule: a ball is in when it touches the court, including the boundary lines. (FIVB Rule 8.3)
Softball: diamond from above, home at the bottom, bases 18.29 m (60 ft) apart.
10. **Beat the throw.** t 0: Red batter hits a grounder to White's shortstop; t 1.4: shortstop fields; t 1.7: throws; t 3.1: first baseman, foot on the bag, catches; t 3.3: the runner's foot reaches the bag. Calls: **Out**, **Safe**, **Foul ball**, **Dead ball**. Right: Out. Key moment t 3.1 (split clock: ball 3.1 s, runner 3.3 s). Rule: a batter-runner is out when a fielder holding the ball touches first base before the runner gets there. (WBSC Official Rules of Softball, Rule 8, batter-runner is out)
11. **Fair past the bag.** t 0: Red batter hits a slow grounder up the first base line; t 1.5: the ball passes beside first base over fair ground; t 2.4: it rolls into foul ground beyond the base. Calls: **Fair ball**, **Foul ball**, **Out**, **Dead ball**. Right: Fair ball. Key moment t 1.5. Rule: a ball that bounds past first or third base over fair territory is fair, even if it rolls foul after. (WBSC, Rule 1 definitions: fair ball)
12. **Caught in foul ground.** t 0: Red batter pops the ball up; t 2.8: White's third baseman catches it 3 m outside the third base line. Calls: **Out**, **Foul ball: strike**, **Fair ball**, **Dead ball**. Right: Out. Key moment t 2.8. Rule: a fly ball caught before it touches the ground is an out, in fair or foul territory. (WBSC, Rule 8, batter is out)

### Wrong-call feedback (one per clip, shown and spoken after a wrong call; the call card greys with "Not the call")
1 and 2: "Freeze it when the pass is played. Put the offside line on the second-last defender." 3: "Who touched it last before it crossed?" 4: "Count the steps after the catch." 5: "Watch the moment the ball is held, then what happens next." 6: "Was there contact, and was it a two or a three?" 7: "Count the touches on one side." 8: "Zoom on the net at the spike." 9: "Zoom where the ball lands." 10: "Compare the two clocks." 11: "Where was the ball when it passed the base?" 12: "Did the ball touch the ground before the catch?"

### Locker symbols
Soccer: corner flag. Basketball: hoop. Volleyball: net. Softball: glove. Door order from the whiteboard: net, glove, corner flag, hoop.

## Interactions in detail
- Clips are drawn in code at real pixel size over the painted surface and tweened between keyframes (players ease between their listed spots; unlisted players stand still). Players are numbered tokens, not painted people: they must sit at exact meters and move every frame, and the booth tools snap to them. Default playback at real speed; the scrubber and step buttons move by 0.1 s and pause.
- Tap while it plays: every booth control stays live while a clip runs. Pause, a step button or a scrubber drag stops the clip on that frame at once; the booth tool can be turned on mid-play; Back to the locker room stops the clip and any line at once.
- Call cards are disabled until the clip has played once to the end (or been scrubbed to its end), so teams watch before calling.
- Wrong calls cost nothing but the wrong card stays greyed for that clip. Key moment jumps to and pauses at the key time with the booth tool on.
- Progress in Escape is in memory only; Start over (on the locker room view) clears it. Replay booth keeps nothing.
- Motion off: clips still play (they are the content); camera shakes, locker swings and door opening become instant swaps.
- Keyboard: Space plays or pauses, Left and Right step 0.1 s, keys A to D pick a call card.
- Sizes: at 1366x768 the clip, scrubber and all four call cards show without scrolling; under 900 px tall the panel puts call cards before the question text. Preview sizes keep jersey numbers at 10 px or more.

## Look
- Accent `--brand` #f0b429 (referee whistle amber) with ink-on-accent #1a1300, on a dark "replay booth" theme on its own `:root`: paper #11151c, panel #181e28, ink #e9edf2, muted #a3adbb, line #2b3443, focus #8fe3ff.
- Contrast: accent on paper 9.81:1, accent on panel 8.98:1, ink on accent 9.91:1, ink on panel 14.23:1, muted on panel 7.37:1.
- Fields are the painted surfaces (Art), toned by the builder so the base color stays near these values: soccer grass #2a5e3a with white lines (7.61:1), basketball maple #e9c48f, volleyball court orange-tan with a white net, softball dirt and grass. Red team filled circles #c62828 with white numbers (5.62:1); White team white rings with dark numbers. The ball yellow with a dark ring. Neighbors: group siblings use purple, green, raspberry, indigo, lime and coral; no 6-8 neighbor is built yet.

## Art
Local FLUX (`scripts/localart.py`), one style for all: "clean flat illustration, muted colors, soft shading". 12 images, none with people.
- rr-locker-room: "An empty school locker room, a long row of tall dark green metal lockers along the back wall, a wooden bench, a blank white whiteboard on the wall at the left, a plain grey exit door on the right, soft overhead light, clean flat illustration"; 16:9; cutout no; people no; the Escape backdrop (the open floor in front of the back row is where the four painted lockers stand).
- rr-locker-closed: "One tall grey-blue metal school locker, closed, with a blank door and vents, front view, clean flat illustration, plain white background"; 9:16; cutout yes; people no; the four sport lockers (labels, icons and the lock drawn in code).
- rr-locker-open: "The same tall grey-blue metal locker with its door swung open, an empty shelf inside, front view, clean flat illustration, plain white background"; 9:16; cutout yes; people no; replaces the closed one when its lock opens (the symbol sits on the shelf).
- Locker symbols (kit, 4 cutouts, one shared prompt "{item}, clean flat illustration, plain white background"; 1:1; cutout yes; people no; on the locker shelf, on the keypad keys and on the "Ready for game day" card): rr-sym-flag (a soccer corner flag on a short pole), rr-sym-hoop (a basketball hoop with a white net), rr-sym-net (a section of a volleyball net between two posts), rr-sym-glove (a brown softball glove).
- rr-field-sunny: "A sunny sports field seen through an open doorway, green grass, a blue sky with small clouds, clean flat illustration"; 16:9; cutout no; people no; behind the opened exit door.
- Clip surfaces (full-frame textures; lines, bases, net, players and ball are code on top; cutout no; people no):
  - rr-tex-grass: "Top-down view of freshly mown green grass with soft stripes, full frame, clean flat illustration"; 16:10; the soccer half, and the softball outfield and foul ground.
  - rr-tex-maple: "Top-down view of light maple hardwood floor boards, full frame, clean flat illustration"; 16:10; the basketball half court.
  - rr-tex-court: "Side view of an indoor gym, a tall pale grey wall with high windows above an orange-tan court floor along the bottom, clean flat illustration"; 16:9; the volleyball side view (the net and antennae are code so they can ripple).
  - rr-tex-dirt: "Top-down view of smooth reddish-brown infield dirt, full frame, clean flat illustration"; 16:10; clipped to the softball infield shape.
Drawn in code: the players (numbered tokens), ball, field lines, net, bases, the booth tools, locks and tumbler lights, sport labels, whiteboard text, the keypad, timer, call and rule cards, and preview.svg.

## Voice
`firm-captain` (Alnilam): "Say firmly but kindly, like a ship captain giving clear directions", here the head referee. Differs from every group sibling (goal-tracker easy-coach, pressure-point smooth-narrator, relationship-spectrum wise-mentor, stress-toolkit soft-breath, screen-week science-narrator) and from the nearest built tools. `Curio.voice`, scope mode plus clip.

| Key | Kind | When it plays | Line | Stale when |
|---|---|---|---|---|
| wEsc | how | entering Escape, first time | You're locked in the locker room. Tap a locker to open the replay booth. | a locker tapped; mode left |
| wBooth | how | entering Replay booth, first time | Tap any clip to open it in the booth. | a clip tapped; mode left |
| howWatch | how | the first clip opened | Tap Play and watch the whole clip. The call cards wake up when it ends. | the clip reaches its end |
| howCall | how | the first time the call cards wake up | Now tap your call. | a call card tapped |
| howTool | how | after the first wrong call | Use the step buttons and the booth tool to find the key moment, or tap Key moment. | clip changed |
| good | event | each right call | Good call. | clip changed |
| wrong.1-12 | event | each wrong call | the twelve wrong-call lines above | clip changed or another call tapped |
| tumbler | event | each tumbler lit (not the third) | One more light on the lock. | clip changed |
| open | event | each locker opened | The locker is open. Remember its symbol. | view changed |
| door | how | the first time all four lockers are open | All four lockers are open. Tap the door and enter the symbols in game day order. | the door tapped; view changed |
| doorWrong | event | each wrong keypad order | That's not the order. Check the whiteboard. | keypad tapped again |
| out | event | the door opens | The door is open. You're ready for game day. | mode left |
| time | event | the timer runs out | Time! Tap Keep going, or Start over. | button tapped |
Rule cards are read on screen; Read speaks the current one.

## Family engine
none

## Sources
- SHAPE America, National Physical Education Standards (2024), Standards 1 and 2: https://www.shapeamerica.org/standards/pe/
- Soccer, offside, level is onside, corner kick: IFAB Laws of the Game 2025/26, Laws 11 and 17: https://www.theifab.com/laws/latest/
- Basketball, travel (two steps after gathering), dribble, shooting foul free throws: FIBA Official Basketball Rules 2024, Articles 24, 25 and 34: https://www.fiba.basketball/documents
- Volleyball, three hits, net touch, ball on the line: FIVB Official Volleyball Rules 2025-2028, Rules 8.3, 9.1, 11.3.1: https://www.fivb.com/volleyball/the-game/official-volleyball-rules/
- Softball, 60 ft bases (fastpitch), fair ball definition, batter-runner out at first, caught foul fly: WBSC Official Rules of Softball (current edition), Rule 1 definitions and Rule 8: https://www.wbsc.org/en/documents
- Verify agent: check every rule line and section number against the current edition; if a section has been renumbered, keep the rule and fix the number.
- Art: original paintings made for this tool with local FLUX (Art).
- Checks run (Python, 2026-10-29): clip 1, at the pass (t 1.0) the opponents nearest the goal line are the keeper (x 50) then White 4 (x 36), so the second-last opponent is at x 36; Red 9 at x 39 is nearer the goal line than it and than the ball (x 20): offside. Clip 2, Red 9 at x 36 is level: not offside. Clip 3, the posts are 7.4 m apart around y 34 (the real goal is 7.32 m), and the ball crosses at y 24, outside the post. Clip 4, three steps after the gather at t 1.5 (more than two). Clip 6, the shooter at (5, 9) is 3.72 m from the basket, inside the 6.75 m arc: two free throws. Clip 10: the old split clock started its two clocks at different moments (throw at t 2.1, hit at t 0), so it would read 1.0 s and 3.3 s and not show who arrived first; both clocks now start at the hit and read 3.1 s and 3.3 s. The old throw also flew 1.0 s from shortstop to first (about 26 m, so about 26 m per second, too fast for the age); fielding and throwing moved to t 1.4 and t 1.7, a 1.4 s throw. The runner covers 18.29 m in 3.3 s (5.5 m per second). Whiteboard order Volleyball, Softball, Soccer, Basketball gives net, glove, corner flag, hoop. Contrast in Look recomputed (WCAG 2.1): all match to rounding.

## Done when
1. Each of the 12 clips plays, scrubs and steps by 0.1 s; the key moment frame shows the situation the rule needs (verify agent checks clip 1: Red 9 nearer the goal line than White 4 at t 1.0; clip 2: level).
2. Call cards stay disabled until the clip has been seen to the end; a right call shows the rule card and lights one tumbler; a wrong call greys that card and speaks its hint.
3. Three right calls open a locker and show its symbol; four open lockers enable the door; only the whiteboard order opens it.
4. Booth tools work on their sport: offside line snaps to a player's x, step counter numbers steps from the gather, zoom shows the line contact, split clock reads ball 3.1 s and runner 3.3 s on clip 10 (both timed from the hit).
5. Timer 15 min ends with the Keep going card; Keep going continues untimed with progress kept.
6. Replay booth opens any clip with Key moment on and keeps no progress.
7. At 1366x768 the clip, scrubber and four call cards are visible together; at 375 wide in the host the call cards stack under the clip and stay reachable.
8. How-to lines are spoken once per load; good-call and wrong-call lines every time.
9. Focus: at 1366x768 and 680x425 the clip is the biggest thing in the booth, and the four painted lockers with their locks fill the middle of the locker room view.
10. Tap while it plays: Pause, Back 0.1 s, Forward 0.1 s and a scrubber drag stop a playing clip on that frame at once; no how line names the call cards while they are still disabled.

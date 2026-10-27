# Robot Dance

## One idea
Bolt the robot dances exactly what the picture cards say, side by side with Dot, who knows the real dance; the moment the two robots don't match, Bolt trips on that step, and the class finds and fixes the wrong card (a bug) together.

## Not like
- loop-garden: repeat blocks and fewest-blocks stars on a garden grid. Robot Dance has no grid, no repeat block and no "shortest program" goal: it is about the order of steps and finding the one wrong step. Different robot, palette (night dance stage, magenta, not lawn green) and voice.
- bee-bot-garden: arrow commands that move a bee around a grid to a goal. Robot Dance moves never travel anywhere; every card is a dance move done in place, so the only thing that matters is which move and in what order.
- traffic-light-coder: if-then rules (conditions). Robot Dance has no conditions, only a straight sequence.
- pattern-finder: the class trains an AI that guesses. Bolt never guesses or learns; it does exactly what the cards say, every time.
- computer-builder, secret-keeper, class-snack-vote: different ideas entirely (parts, privacy, data); no shared mechanic.

## Who and how
- Grade K, computer science. Module: Step-by-Step (Algorithms and Programming).
- Driver: teacher, on a projector or smartboard. The class calls out moves, points, votes, and dances along standing up.
- 10 to 20 minutes (Dance Floor alone works as a 5 minute brain break).
- Standards (CSTA K-12 CS Standards, 2026 identifiers from the module): EK-ALG-PS-01, EK-PRO-PD-04, EK-PRO-TR-07. 2017 crosswalk for teachers who still use it: 1A-AP-08 (follow and create algorithms), 1A-AP-10 (programs with sequences), 1A-AP-14 (debug errors in a sequence).
- tool.json: driver "teacher", minutes "10-20", modes ["Dance Floor", "Fix-It Show"], grades_label "Kindergarten".
- No reading needed: every control has a picture; every fixed line is spoken.

## Screens and modes
Layout (kit frame): header, then stage (left) and panel (right). Header: title "Robot Dance" with small line "Step by step, card by card", mode buttons (`.seg`) "Dance Floor" (music note icon) and "Fix-It Show" (wrench with a star icon), then Motion, Sound, Read (ids `motion`, `sound`, `read`).

Stage (both modes), drawn in code, laid out per size (no fixed-design scaling):
- A night dance stage: dark floor of checker tiles in front, two soft spotlight cones from the top, a row of small bulbs along the top edge that blink on each beat.
- Bolt (our robot) center-left. In Fix-It Show, Dot (the dance star) center-right, slightly smaller, on a round star-shaped rug. In Dance Floor, Dot is not shown and Bolt stands center.
- Above Bolt, a big move bubble that shows the icon of the move Bolt is doing right now (empty when idle).
- The card strip along the bottom of the stage: up to 8 cards in a row, each a white rounded card with a colored top band, a mini Bolt drawn in that move's pose, and the move word under it (the word is for the teacher; kids read the picture). Each card has a small step number circle (1 to 8) in its corner. Empty slots show as dashed outlines so the strip length is visible.
- A step pointer: a glowing arrow above the strip on the card being danced.
- When a card is selected: it lifts 12 px with a thick outline, and three round 60 px buttons appear under the strip: "Move earlier" (left arrow), "Take away" (trash can), "Move later" (right arrow).

Panel (both modes):
- `#hint`: one short line (always one of the fixed voice lines below; during the finale it shows line 33).
- Move tray: 8 move buttons in a 2 x 4 grid (4 x 2 in the wide-short layout), each at least 72 px tall, with the move icon (same mini Bolt pose as the card) and the move word.
- Big buttons: "Go!" (play triangle, `.big-btn.gold`), "Stop" (square, shown in place of Go while dancing), "Speed" toggle (turtle = Slow, rabbit = Quick; default turtle).
- Dance Floor only: "Clear" (broom icon).
- Fix-It Show only: "Watch Dot" (eye icon), "Start over" (circular arrow; resets this round's cards to the buggy version), "Next round" (right arrow; enabled only after this round is fixed), round dots (8 dots, filled for fixed rounds), and the Teams box: "Teams" toggle (two faces icon; on by default), Team Star and Team Moon badges with star counts (icon plus number), the active team's badge glowing.

### Mode 1: Dance Floor (explore, opens first)
- Tap a move in the tray: a card for it is added at the end of the strip, Bolt does that move once (preview), and the narrator says the move name.
- With a card selected, tapping a move replaces that card's move (the card flips over to the new one).
- Go: Bolt dances every card in order, left to right, with a beat. Each card lights as it runs. At the end Bolt strikes a pose and the bulbs flash.
- Clear empties the strip.
- No targets, no score, no tripping: Bolt never makes a mistake on its own.

### Mode 2: Fix-It Show (showdown)
- 8 rounds, one dance each. Each round starts with Bolt's cards already in the strip, with one bug in them.
- Watch Dot: Dot dances the real dance alone (Bolt stands and watches, head turning on each step). The class can watch as often as they like.
- Go: both robots dance together, beat for beat. Dot does the real dance; Bolt does exactly what its cards say. At the first step where they differ, Bolt trips (see Interactions), the dance stops, that card wobbles with a red "?" badge, and a thought bubble over Dot shows the move Dot did on that step.
- The class fixes the cards (replace, move, take away, add) and presses Go again. When all of Bolt's steps match Dot's and the length is the same, both robots finish together: confetti (Motion on), a fanfare, the round dot fills, and with Teams on the active team gets a star.
- Next round moves on. Teams alternate rounds: odd rounds Team Star, even rounds Team Moon. With Teams off, there are no badges or stars; the narrator praises "everyone".
- After round 8 is fixed: the Finale screen. Both robots dance the round 8 dance together in a loop of 2 times with bulbs flashing, team totals shown large, and a "Play again" button (circular arrow) that resets all rounds and stars.

## Content
Moves (8). Each: word, card band color, glyph drawn on the card corner (so color is never the only signal), Bolt's pose, and sound.
| Move | Color | Corner glyph | Bolt does | Sound (synth via Curio.tone) |
|---|---|---|---|---|
| Clap | gold #e0a800 | two short lines | arms swing in, hands meet in front, twice | two short noise-like clicks |
| Jump | green #2e9a4f | up arrow | crouch, rise 40 px, land | rising boing |
| Spin | violet #7b4fd0 | circle arrow | turns one full circle (squash-x rotation in 2D) | whoosh (sliding tone) |
| Wave | sky blue #2b86d6 | wavy line | one arm up, hand waves side to side 3 times | three soft chimes |
| Hands Up | orange #e36a1c | two up ticks | both arms straight up, small bounce | bright up chord |
| Touch Toes | teal #12938a | down arrow | bends at waist, hands to feet, back up | falling tone |
| Wiggle | pink #d63f8c | zigzag | hips and antenna wiggle side to side | wobbly tone |
| Stomp | brown #8a5a2b | foot print | lifts one foot, stomps, floor tile flashes | low thud |

Fix-It rounds (target = Dot's real dance; cards = Bolt's buggy start; trip step is the first mismatch):
| # | Name (spoken) | Team | Dot's dance | Bolt's cards | Bug kind | Trip at |
|---|---|---|---|---|---|---|
| 1 | The Hello Dance | Star | Wave, Clap, Jump | Wave, Clap, Spin | wrong move | step 3 |
| 2 | Clap Clap Stomp | Moon | Clap, Clap, Stomp, Hands Up | Clap, Wiggle, Stomp, Hands Up | wrong move | step 2 |
| 3 | Wiggle Time | Star | Wiggle, Touch Toes, Wiggle, Jump | Hands Up, Touch Toes, Wiggle, Jump | wrong move | step 1 |
| 4 | Robot Stomp | Moon | Stomp, Stomp, Spin, Clap, Hands Up | Stomp, Stomp, Spin, Jump, Hands Up | wrong move | step 4 |
| 5 | Mixed Up | Star | Jump, Clap, Spin, Wave | Jump, Spin, Clap, Wave | two swapped | step 2 |
| 6 | Toes and Stomps | Moon | Touch Toes, Hands Up, Wiggle, Stomp, Clap | Touch Toes, Hands Up, Wiggle, Clap, Stomp | two swapped | step 4 |
| 7 | Something's Missing | Star | Wave, Jump, Spin, Clap | Wave, Spin, Clap | missing step | step 2 |
| 8 | One Too Many | Moon | Clap, Wiggle, Jump, Hands Up | Clap, Wiggle, Wiggle, Jump, Hands Up | extra step | step 3 |

Words on screen (teacher-facing, also spoken): "bug" = a wrong card that makes the dance go wrong; "debugging" = finding and fixing the bug. "Bolt does exactly what the cards say."

## Interactions in detail
- Timing: one step per beat. Slow (default) 1400 ms per step, Quick 900 ms. A soft beat tick plays on each step start (Sound on). Bulbs blink on each beat. The move animation fills about 80 percent of the beat, then Bolt returns to standing.
- Preview from the tray: Bolt does the move once at Slow timing. Tapping again during a preview cancels it and starts the new one (no queue pile-up). Narrator says only the latest move name (drop older queued move names).
- Strip limit 8 cards. Tapping a move with 8 cards and none selected does not add: the strip flashes its outline and the "That's eight cards" line plays.
- Selecting: tap a card to select it; tap it again, tap empty stage, or press Escape to deselect. Only one card selected at a time. Move earlier is disabled on card 1; Move later on the last card. Take away removes the card and selects nothing. Move earlier/later animate the two cards sliding past each other (300 ms) and keep the moved card selected, so tapping again keeps moving it.
- Adding a missing step: with nothing selected, a tray tap adds at the end; the class then uses Move earlier to walk it into place. (Round 7 hint says this.)
- While dancing (Go, Watch Dot, a preview): the tray, card buttons, Clear, Start over and mode-switch to the same mode are disabled (dimmed, not hidden); Stop is shown in place of Go. Stop ends the dance at once, both robots return to standing, the pointer clears. Switching mode or pressing Reset also stops.
- Go with an empty strip (Dance Floor or after taking all cards in Fix-It): nothing dances; the "Add a card first" line plays and the tray outline pulses once.
- Comparison in Fix-It (general, not tied to the designed bug): for step i from 1, if Bolt has no card i but Dot has a step i, Bolt stands still with a puzzled tilt and a "?" over its head while Dot does step i; stop there, "ran out of cards" line. If Bolt has card i but Dot has no step i (Dot already finished and is bowing), Bolt does the extra move and trips; "extra step" line. If both have a step and they differ, Bolt starts its card's move, bumps into a wobble and sits down on the floor with a bounce (600 ms), stars circle its head; "which card is wrong" line. Dot's thought bubble shows Dot's move for that step (empty bubble with "..." in the ran-out case is not needed: in that case Dot simply does the step). The tripped card gets the red "?" badge until the next Go or edit.
- Trip is comic, never sad: no buzzer, a slide-whistle-down tone and a cartoon "boing". Bolt gets back up by itself when any edit is made or Go is pressed.
- Success check: all steps match and lengths are equal. Then both robots do a final pose together, confetti for 2 s (Motion off: no confetti, the bulbs turn all-on instead), fanfare (Curio.yes plus a short arpeggio), round dot fills, team star added (if Teams on). Next round glows.
- Fixing before the first Go is allowed (a sharp class may spot the bug from Watch Dot alone): Go then succeeds straight away.
- Stars: one star per fixed round, no penalty for trips (trips are how we find bugs). Stars can't be lost. Start over keeps the star if the round was already fixed.
- Teams toggle mid-show: hides or shows badges; stars already earned are kept and reappear when turned back on.
- Mode switch keeps each mode's state for the page load (Dance Floor strip, current Fix-It round and its cards). Nothing is saved to localStorage except the kit's Motion setting.
- Keyboard: Tab order is mode buttons, header buttons, tray moves, Go/Stop, Speed, Watch Dot, Start over, Next round, Teams, then the strip cards, then the three card buttons. Enter or Space activates; on a selected card, Left/Right arrow keys move it, Delete takes it away. Visible focus everywhere.
- Motion off (body.calm): robots change pose without tweening (pose holds for the same beat time), no confetti, no trip roll (Bolt switches straight to the sitting pose), card slides are instant. Timing and sounds stay the same.
- Sizes (all in STANDARDS.md): Go, the tray and the strip must be visible without scrolling at every size. At 680x425 and 800x500 the panel is a compact column (tray as 4 x 2 small icon buttons, 52 px minimum, words hidden, labels in aria-label), robots smaller, strip cards at least 64 px wide with the pose icon; scene text at least 10 px. Under about 900 px tall in the wide layout put buttons before the tray in the panel. At 760 wide and 375 wide, stack stage over panel with the tray directly under the strip and Go beside the tray.

## Look
- Band: K-2, own `:root` (no band theme file).
- `--paper #fbf6fb`, `--ink #2a1830`, `--muted #6a5670`, `--line #ead9e8`, `--brand #b0206a` (magenta, the accent; header background), `--focus #2f5bd3` (on light) with a 3 px white inner ring so it also shows on the dark stage, `--gold #ffd23f` for Go.
- Stage: navy night #1d2346 with floor tiles #2b3266 / #343c78, spotlight cones as white at 12 percent opacity, bulbs #ffd23f.
- Bolt: teal body #19a7a0 with a white face screen, round antenna ball in magenta #b0206a, dark outline #132036. Dot: warm coral #ff8a65 body with a gold star on the chest, same outline. Two clearly different silhouettes: Bolt boxy with a square head, Dot round with a dome head.
- Neighbor check: loop-garden is lawn green with dark-green header; beat-buddies (same voice, music) uses red-orange #c2482f; calm-corner green #2f7a62. Magenta on a night stage is unlike all of them.
- Contrast (WCAG): white on #b0206a header 6.44:1; #fff4fa on #b0206a 6.0:1; ink on paper 15.47:1; muted on paper 6.19:1; brand text on paper 6.03:1; white on stage navy 15.21:1; gold on navy 10.53:1; ink on gold (Go label) 11.43:1; focus blue on paper 5.53:1. All pass AA. Card words are ink on white (16.51:1); the colored band is decoration plus the corner glyph.

## Art
none: drawn in code. Bolt, Dot, their 8 poses each (plus stand, trip-sit, puzzled, bow and final pose), the 8 card icons (mini Bolt poses), stage, bulbs, spotlights, confetti and preview.svg are SVG drawn in the tool. No raster images, so no overlap with computer-builder or other tools in the batch. preview.svg: the night stage with Bolt mid-jump, Dot clapping, and four cards in the strip.

## Voice
Bank voice `lively-host` (Sadachbia), style "Say with lively energy, like a friendly game show host". Fits a whole-class showdown. Not used by any neighbor here: loop-garden uses hero-coach (Puck), computer-builder will use bright-teacher; the only other lively-host tool is beat-buddies (music), not a neighbor. Every spoken line is fixed (list below); `voice/lines.json` holds exactly these. Queue follows collision-lab (narrate, hush, readNow, firstTap) as STANDARDS.md says.

Welcomes and hints:
1. "Welcome to Robot Dance! Meet Bolt. Bolt does exactly what the cards say."
2. "Tap a move to add a card. Then press Go, and dance along!"
3. "Welcome to the Fix-It Show! Dot knows the dance. Bolt reads the cards. Can you find the wrong card?"
4. "Press Watch Dot to see the dance. Then press Go."
5. "Now press Go and see if Bolt can do it too."
6. "Tap the wrong card. Then tap the right move."
7. "Use the arrows to move a card."
8. "Tap the trash can to take a card away."
9. "Add the missing move. Then use the arrows to move it into place."
10. "Add a card first. Tap a move!"
11. "That's eight cards! Press Go to see your dance."
12. "All clear! Make a new dance."
13. "Ta-da! Bolt danced every card, in order."

Rounds (said when the round opens, once per round per page load):
14. "Round one: the Hello Dance! Watch Dot first."
15. "Round two: Clap Clap Stomp! Watch Dot first."
16. "Round three: Wiggle Time! Watch Dot first."
17. "Round four: Robot Stomp! Watch Dot first."
18. "Round five: Mixed Up! Two cards are in the wrong order."
19. "Round six: Toes and Stomps! Two cards are in the wrong order."
20. "Round seven: Something's Missing! Watch Dot carefully."
21. "Round eight: One Too Many! Watch Dot carefully."
22. "Team Star, it's your turn!"
23. "Team Moon, it's your turn!"

Trips and wins:
24. "Oops! Bolt tripped. Which card is wrong?"
25. "Look at Dot. What move should Bolt do here?"
26. "Uh oh! Bolt ran out of cards. Something is missing!"
27. "Whoa! Bolt has an extra step. Dot was all done!"
28. "Hooray! Bolt did the whole dance! You fixed the bug!"
29. "A wrong card is called a bug. Finding and fixing it is called debugging!" (once per page load, after the first win)
30. "A star for Team Star!"
31. "A star for Team Moon!"
32. "Great job, everyone!" (Teams off)
33. "That's the show! Everybody take a bow!"
34. "Team Star and Team Moon, you're both dance champs!" (finale, Teams on)

Move names (tray taps and previews):
35. "Clap!" 36. "Jump!" 37. "Spin!" 38. "Wave!" 39. "Hands up!" 40. "Touch your toes!" 41. "Wiggle!" 42. "Stomp!"

Which line when: Dance Floor entry queues 1 then 2. Fix-It entry queues 3 then the round line (14 to 21) then the team line (22/23, Teams on). After Watch Dot ends: 5. Trip: 24 then 25, or 26 or 27 alone. Second trip in the same round: the round's fix hint (rounds 1-4: 6; 5-6: 7; 7: 9; 8: 8) after a wrong move, 26 again after running out, 8 after an extra step. Win: 28, then 29 (first win only), then 30/31 or 32. Finale: 33 then 34 (Teams on). Read speaks the current `#hint` line (always one of 2 to 13 or 24 to 28, and 33 in the finale). The finale has no team winner line on purpose: the show celebrates both.

## Family engine
none. The robot family (loop-garden, bee-bot-garden, traffic-light-coder) has no `docs/families/robot.md` or `kit/robot.js` yet, and loop-garden carries its own code. Do not write a family engine for this tool; keep the card strip and step runner inside `src.html`, written cleanly (a `program` array of move ids, a `run(program, target)` step loop with an onStep callback) so a later family engine can lift it.

## Sources
- CSTA K-12 Computer Science Standards, 2026 PK-12 identifiers EK-ALG-PS-01, EK-PRO-PD-04, EK-PRO-TR-07 (csteachers.org; ids from data/standards/csta-2026-ids.txt).
- CSTA K-12 Computer Science Standards (2017), 1A-AP-08, 1A-AP-10, 1A-AP-14: https://csteachers.org/k12standards/
- Code.org CS Fundamentals glossary (algorithm: a list of steps to finish a task; bug: part of a program that does not work correctly; debugging: finding and fixing problems in an algorithm or program): https://code.org/curriculum/docs/k-5/glossary
- "A computer does exactly what the instructions say": Code.org unplugged lesson "My Robotic Friends" (Course A to C), https://code.org/curriculum/unplugged
- Move set and round content are original to Curio Class.

## Done when
1. Dance Floor: tapping each of the 8 moves adds a matching card, Bolt does that pose, and the move name is heard (voice log shows the clip start); a 9th tap is refused with line 11.
2. Go in Dance Floor runs every card left to right, the pointer and card glow follow each step, and the move bubble over Bolt matches the lit card on every step; Stop halts at once.
3. Fix-It round 1 to 8: pressing Go on the starting cards trips Bolt on exactly the step in the "Trip at" column, with line 24 then 25 (all 8 designed bugs, including the missing and extra rounds, first show up as a mismatch, so lines 26 and 27 are tested separately in check 5), and Dot's bubble shows Dot's move for that step.
4. Each round can be fixed with the panel and card buttons alone (replace, move earlier/later, take away, add then move), then Go succeeds: confetti, fanfare, round dot filled, star to the right team; Next round enables only then.
5. Edge cases from Interactions behave as written: empty Go, cards shorter than Dot's dance (puzzled stand, line 26), longer (line 27), fixing before any Go, Start over after a win keeps the star, Teams toggle hides and restores stars.
6. Keyboard only: a full round can be played and fixed with Tab, Enter, arrows and Delete, with visible focus on the dark stage and on paper.
7. Every size in STANDARDS.md (680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760 wide, 375 wide in the host): Go, the tray and the whole strip visible without scrolling; scene text 10 px or more in the preview; targets 60 px or more at full screen.
8. Voice: held clicks (press about 120 ms, release) on the first tap give the right welcome or skip rule; Read stops speech and speaks the hint; Sound off then on queues the unsaid welcome; mode switch and Stop drop unstarted lines; no line waits about 10 s after Read.
9. Motion off: no tweening or confetti, same beat timing and sounds; console clean (no errors or exceptions) through a full show and finale.

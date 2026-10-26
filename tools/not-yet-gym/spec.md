# Not Yet Gym

(Renamed from "Brain Gym" on 2026-10-26: that name is a registered trademark of a commercial program. Folder and id are now not-yet-gym.)

## One idea
Bix, a little brain buddy, visibly levels up from what you do after a mistake: every "not yet" that you come back from with a strategy adds a gold comeback stripe to Bix's headband, and first-try wins are worth less than comebacks.

## Not like
- walk-in-their-shoes (3-5, story): that tool is a story seen through several characters' feelings. Not Yet Gym has no story or perspectives; it is a training loop with one creature, real puzzles and goal setting.
- habit-hero (K-2 health, creature): Pip's meters go down after a less healthy choice. Bix's meters never go down. A mistake costs nothing and opens the door to the biggest reward.
- calm-corner (K-2 SEL): a guided calm-down tool. Not Yet Gym has one 3-breath pause as a single strategy card, never a guided calm activity.

## Who and how
- Grade 3-5, Social and Emotional Learning, module Growth Mindset and Goals.
- Driver: students or teacher (one student per laptop, or the teacher on a projector with the class voting on answers and strategies).
- Minutes: 15-25 (one advisory or morning-meeting period). Progress can be saved for a later day.
- Standards: CASEL.Self-Management (setting personal goals, showing self-discipline and self-motivation, using planning and organizational skills).
- Modes (tool.json): ["Gym", "Goals", "Locker"].

## Screens and modes
Header: title "Not Yet Gym" with small line "Practice, mistakes and goals", the mode buttons **Gym**, **Goals**, **Locker** (keys 1 to 3), then **Motion**, **Sound**, **Read**. Stage on the left, panel on the right (panel below on narrow screens). Panel always has the hint paragraph (`hint`), Bix's **Know-how** bar with the stage name, and the comeback stripe count.

### Gym (opens first)
- Stage: a side view of a gym hall drawn in code over the gym-hall backdrop. Five room doors in a row: **Pattern Ladder** and **Memory Mirror** (open), **Light Mat** and **Number Lift** (locked, padlock drawn on the door), **Summit Circuit** (locked, at the top of a short climbing wall). Bix stands on the floor in front of the doors.
- Tap Bix: Bix does its current move (see Content, stages) and says a short line.
- Tap an open door: enter that room. Tap a locked door: the door rattles, the hint reads "This room opens when you finish a goal. Go to Goals to pick one." and a **Pick a goal** button appears in the panel.
- Inside a room: the puzzle fills the stage, Bix stands in the lower left corner and reacts. Room controls in the panel: **I'm stuck** (opens the strategy cards), **Back to gym**, and a rung row (small numbered circles, solved ones filled, current one outlined; tap any solved or current rung to play it).
- After a solve: a **Next rung** button. After the last rung of a room: "Room complete" card with **Back to gym**.

### Goals
- Stage: a goal board (cork board drawn in code) with goal cards. Cards for rooms that are still locked are not shown.
- Step 1, "Pick one goal": tap a card to make it the active goal (only one at a time). **Change goal** replaces it (no penalty).
- Step 2, "Make a plan": pick one strategy card you will try first when you get stuck. The plan shows on the active goal card ("When I'm stuck, I'll try: Slow down and check").
- The active goal shows a progress line in the panel in every mode ("2 of 3 strategies used").
- On finishing a goal: Bix cheers, the next locked room opens (order: Light Mat, then Number Lift, then Summit Circuit), and a reflection card asks "What helped most?" with the six strategy cards to tap (or **Skip**). The answer only adds a sticker to the Locker; nothing is typed.
- Finished goals move to a "Done" column with a check mark and can't be picked again.

### Locker
- Stage: Bix large in the center, wearing all gear earned so far; a sticker wall (one sticker per strategy used at least once, grey outlines for unused ones); the comeback stripes on the headband; a row of six Coach's corner fact cards (tap to flip).
- Buttons: five color swatches for Bix (**Pink**, **Mint**, **Sky**, **Sun**, **Lilac**), **Save Bix**, **Start over**.

## Content

### Stages of Bix (Know-how never goes down)
| Stage | Know-how | Name | Gear added | Move when tapped |
|---|---|---|---|---|
| 1 | 0 | Rookie | none | a small hop |
| 2 | 8 | Warming up | sweatband (holds the comeback stripes) | jumping jacks (3) |
| 3 | 20 | On a roll | sneakers | a spin |
| 4 | 35 | Smooth mover | gym bag over one shoulder | juggles three small balls |
| 5 | 55 | Summit buddy | star medal | a cartwheel |

Know-how points: solve on the first try +1; comeback (a solve after a not-yet or an "I'm stuck" in the same puzzle) +3; extra +1 if a strategy card was used before that comeback solve; finish a goal +5. Points come only the first time a puzzle is solved; replays are free practice. Each comeback adds one gold stripe (up to 10 drawn, then a number on the band).

### Strategy cards (six, same everywhere)
1. **Try a new way**: shows the room's "new way" tip.
2. **Slow down and check**: the room's slow-down effect (below).
3. **Use a hint**: shows the puzzle's hint.
4. **Take three breaths**: Bix breathes in and out three times on screen (4 s in, 4 s out, so 24 s), with **Skip**. Then back to the puzzle.
5. **Break it into parts**: the room's parts effect.
6. **Ask a friend**: "Turn to a neighbor. Ask: what do you notice?" with **Show a friend's idea**, which shows the puzzle's hint in a speech bubble from Dot (a small round brain friend drawn in code).

### Pattern Ladder (open at start), 9 rungs. Pick what comes next (4 choices).
| # | Sequence | Answer | Other choices | Hint |
|---|---|---|---|---|
| 1 | red circle, blue square, red circle, blue square, ? | red circle | blue square, red square, blue circle | Say it out loud: circle, square, circle, square... |
| 2 | 2, 4, 6, 8, ? | 10 | 9, 12, 16 | How much bigger is each number than the one before? |
| 3 | triangle, triangle, star, triangle, triangle, star, triangle, ? | triangle | star, circle, square | Find the part that repeats. How long is it? |
| 4 | 3, 6, 9, 12, ? | 15 | 13, 14, 24 | Count the jump from 3 to 6. Does it stay the same? |
| 5 | 1, 2, 4, 7, 11, ? | 16 | 15, 14, 22 | Write the jumps: 1, 2, 3, 4... What is the next jump? |
| 6 | 1 dot, 3 dots, 5 dots, 7 dots, ? | 9 dots | 8 dots, 10 dots, 14 dots | Count how many dots get added each time. |
| 7 | 5, 10, 20, 40, ? | 80 | 45, 50, 60 | Is it adding the same amount, or something else? |
| 8 | arrow up, right, down, left, ? | arrow up | arrow right, arrow down, arrow left | Turn your hand the way the arrow turns. |
| 9 | 1, 1, 2, 3, 5, 8, ? | 13 | 11, 10, 16 | Add the two numbers just before the blank. |
- New way tip: "Look at the jumps between neighbors, not just the items."
- Slow down: the sequence items light up one at a time, 1 s apart.
- Parts: the sequence is split into its repeating chunk or its jumps, drawn as small labels under the gaps (for 2, 4, 5, 7, 9 the jumps "+2", "+3", "+1 +2 +3 +4", "double" in words, "add the two before"; for 1, 3, 8 brackets around each repeat).
- Not yet: the tapped choice greys out with "Not yet" on it; the others stay.

### Memory Mirror (open at start), 6 rungs
Four big pads, each with a color and a shape: **Star** (gold), **Moon** (blue), **Leaf** (green), **Heart** (coral). Bix shows a sequence (each pad lights 0.7 s, 0.3 s gap); you repeat it. Rung lengths: 3, 4, 5, 6, 7, 8. Sequences are random per attempt, but a retry after a not-yet replays the same sequence.
- Hint: the next pad in your answer glows once.
- New way tip: "Say the names as they light up: star, moon, leaf..."
- Slow down: replays the sequence at half speed (1.4 s per pad).
- Parts: replays it in chunks of 2 or 3 with a 1 s pause between chunks.
- Not yet: a wrong pad, then **Watch again**.

### Light Mat (opens with the first goal), 6 rungs
A 3x3 mat. Tapping a square flips it and the squares above, below, left and right of it. Goal: light all 9. Start states (# lit, . dark, rows top to bottom), each made from all-lit by the listed presses (squares numbered 0 to 8, left to right, top to bottom); the press count is the fewest possible.
| # | Start | Fewest presses | Solution squares |
|---|---|---|---|
| 1 | #.# / ... / #.# | 1 | 4 |
| 2 | ... / ### / ... | 2 | 1, 7 |
| 3 | ..# / .#. / #.. | 2 | 0, 8 |
| 4 | ... / #.# / ... | 3 | 3, 4, 5 |
| 5 | .#. / ### / .#. | 4 | 0, 2, 6, 8 |
| 6 | ### / .## / .## | 5 | 0, 1, 2, 4, 6 |
- Move limit: fewest + 4. A counter shows "Moves: 3 of 6". Reaching the limit unsolved is a not yet; the mat resets to its start.
- Hint: one square glows that is in (solution XOR squares pressed an odd number of times). Every 3x3 start has exactly one set of presses that solves it, so this is always right.
- New way tip: "Pressing a square twice undoes it. Each square needs at most one press."
- Slow down: after each press, the 5 flipped squares outline for 1 s before the next tap counts.
- Parts: "Fix the top row first. Then look at what is left." The top row gets a bracket.

### Number Lift (opens with the second goal), 6 rungs
An elevator on floors 0 to 20, starting at 0. Two buttons per rung. Reach the target floor within the move limit (fewest + 2). Buttons that would go below 0 or above 20 are greyed with "Can't go there" (not a mistake).
| # | Buttons | Target | Fewest moves | One fewest path |
|---|---|---|---|---|
| 1 | +3, +5 | 11 | 3 | +3 +3 +5 |
| 2 | +4, -1 | 7 | 3 | +4 +4 -1 |
| 3 | +6, -4 | 2 | 2 | +6 -4 |
| 4 | +7, -5 | 4 | 4 | +7 +7 -5 -5 |
| 5 | +5, -3 | 1 | 5 | +5 +5 -3 -3 -3 |
| 6 | ×2, +1 | 11 | 6 | +1 ×2 ×2 +1 ×2 +1 |
- Hint: the button that starts a fewest path from the current floor glows (builder computes it by breadth-first search).
- Solving in the fewest moves shows a small "Fewest moves" star.
- New way tip: "Try working backward from the target floor."
- Slow down: each move animates floor by floor and shows the math ("7 - 5 = 2") under the elevator.
- Parts: shows a halfway floor to aim for first (the floor reached after half of a fewest path, rounded down).
- Not yet: out of moves; the lift returns to 0.

### Summit Circuit (opens with the third goal), 4 rungs, one from each room, harder
1. Pattern: 2, 3, 5, 9, 17, ? Answer 33; others 25, 34, 18. Hint: "Double the number, then take away 1." Parts: jumps +1, +2, +4, +8.
2. Memory: length 9.
3. Light Mat: start #.# / .#. / #.# (fewest 4: squares 1, 3, 5, 7), limit 8.
4. Number Lift: +9, -4, target 6, fewest 5 (+9 +9 -4 -4 -4), limit 7.
Finishing all four gives Bix the star medal even below stage 5 and a short celebration (confetti unless Motion is off).

### Goal cards
| Goal | Done when | Shown |
|---|---|---|
| Climb to rung 6 on the Pattern Ladder. | Pattern rung 6 solved | always |
| Remember a 5-step pattern in Memory Mirror. | Memory rung 3 solved | always |
| Use 3 different strategy cards. | 3 different cards used | always |
| Keep going after 5 not-yets. | 5 not-yets each followed by another try | always |
| Make 2 comebacks. | 2 comebacks | always |
| Finish 3 rungs in one room in a row. | 3 solves in a row in one room without leaving | always |
| Solve a Light Mat puzzle without a hint. | any Light Mat solve with no hint used | after Light Mat opens |
| Reach a floor in Number Lift in the fewest moves. | any fewest-moves star | after Number Lift opens |
Progress counts only from when the goal is picked.

### Coach's corner fact cards (front / back)
1. Practice helps / When you keep practicing something hard, it usually gets easier over time.
2. Not yet / A mistake shows you what to practice next. "Not yet" means you are still learning.
3. New strategies / Trying a different way often works better than trying harder the same way.
4. Ask for help / Asking someone for an idea is a strategy that strong learners use.
5. Slow breaths / A few slow breaths can help you feel calmer when you are stuck or upset.
6. Clear goals / A good goal is specific, so you can tell when you have reached it.
Do not say the brain grows, builds neurons or gets "stronger" like a muscle. Bix's growth is a picture of skill and practice.

## Interactions in detail
- Bix's faces (drawn in code): happy (idle), focused (puzzle showing), thinking (after a not-yet: hand on chin, never sad or crying), cheering (comeback: big jump plus a gold stripe sliding onto the band), proud (first-try solve: thumbs up), calm (breathing card). Stage-ups: Bix glows, the new gear drops on, and the stage name shows for 2 s.
- After every not-yet the strategy cards slide up automatically, with **Just try again** as a seventh, plain button. "I'm stuck" opens the same cards at any time.
- Cards can be used any number of times; each card used the first time puts its sticker on the Locker wall.
- A puzzle remembers its not-yet flag until solved or until you leave the room; leaving and coming back starts the rung fresh (no comeback credit carried over).
- Taps during a Memory playback are ignored; the pads show "Watch" until playback ends.
- Teacher on a projector: every target at least 60 px in rooms; choices and pads are big enough for "point and vote".
- Extremes: after stage 5 the bar reads "Summit buddy" and stays full; points still count as a number. More than 10 stripes shows "x12" on the band.
- Save Bix stores {know-how, stripes, stage, open rooms, solved rungs, goals done, active goal and plan, stickers, color} to localStorage `curio-not-yet-gym` (try/catch). No text is ever typed. On load with a save: "Welcome back" and resume. Without Save, nothing persists on reload.
- Start over: asks "Start over with a new Bix? Your saved progress will be cleared." with **Yes, start over** and **Cancel**; clears the save and returns to Gym stage 1.
- Mode switch or Back to gym stops speech and any playback; a breathing card in progress is cancelled.
- Keyboard: arrows move between choices, pads and mat squares; Enter or Space taps; 1 to 3 switch modes; Escape closes the strategy cards.

## Look
- Accent `--brand: #5a2fb8` (electric violet), header background, white header text 8.29:1. Neighbors use green #2f7a62 (calm-corner), red #d6492f (habit-hero), teal #26627a, magenta #b0407a; walk-in-their-shoes must pick something other than violet.
- `:root`: `--paper #fbf7ff`, `--ink #2a2340` (14.05:1 on paper), `--muted #5f5878` (6.29:1), `--brand` on paper 7.84:1, `--line #e3dcf2`, `--focus #ff8a1f` (outline only, 4 px).
- Scene: gym floor wood #e8c38e (ink on it 8.94:1), mats #2f6fd0 (white text 4.88:1), gold stripes and stars #ffcf4a (ink 10.1:1), Bix default pink #f6b3c8 (ink 8.64:1), mint #9fe3c9 (ink 10.12:1). Memory pads always carry a shape and a name, never color alone.
- Stage drawn at real pixel size and re-laid out per size (STANDARDS.md "Sizes"); room controls and the strategy cards stay visible without scrolling at 1366x768 and in the 680x425 preview.

## Art
- gym-hall: "bright empty school gymnasium, warm wooden floor, pale lavender walls, a short colorful climbing wall, plain solid color pennant flags, soft daylight from high windows, flat illustration"; 16:9; cutout no; people no; behind the Gym map with a white 40% overlay so doors and Bix read clearly. Local FLUX.
- Everything else (Bix, Dot, gear, doors, puzzles, goal board, stickers, locker) is drawn in code.

## Voice
Bank voice: `upbeat-guide` (Zephyr, bright and clear), style: "Say brightly and clearly, in a friendly, encouraging way, like an upbeat coach at the gym." Bix speaks in the first person. (Spec check 2026-10-26: conflict-coach has big-sister; walk-in-their-shoes has gentle-storyteller.)
Welcomes (one per mode):
- "Welcome to the Not Yet Gym! I'm Bix. Pick a room and let's practice something hard."
- "Let's set a goal. Pick one card, then pick what you'll try when you get stuck."
- "This is my locker. Everything here, I earned by practicing with you."
Room instructions (first entry):
- "Pattern Ladder. Find what comes next."
- "Memory Mirror. Watch the pads, then copy them."
- "Light Mat. Tap a square to flip it and its neighbors. Light them all."
- "Number Lift. Use the buttons to reach the target floor."
- "Summit Circuit. One hard puzzle from every room. Let's go."
Reactions:
- Not yet (rotate): "Not yet. What could we try?" / "Hmm. That one's tricky. Pick a strategy." / "Not yet is okay. Let's look again."
- First try: "Got it!" / "Nice thinking!"
- Comeback: "We came back! That's a comeback stripe." / "You didn't give up. Look at my headband!"
- Stage up: "All that practice is paying off!"
- Goal done: "Goal done! A new room just opened."
- Summit done: "We made it to the summit. Thanks for practicing with me."
- Tap Bix (rotate): "Practice makes things easier." / "Mistakes show us what to practice next." / "Want to try a new room?"
- Locked door: "This room opens when you finish a goal."
Strategy cards: "Try a new way." / "Slow down and check." / "Here's a hint." / "Let's take three slow breaths. In... and out." / "Let's break it into parts." / "Ask a friend what they notice."
Breathing: "Breathe in." / "Breathe out." / "Ready to try again?"
Panel hints (Read): every fixed hint in the Pattern Ladder table and Summit rung 1, every "new way" tip and "parts" text above, plus "Next is the star." / "Next is the moon." / "Next is the leaf." / "Next is the heart." / "Try the glowing square." / "Try the glowing button next." Spoken text says "times two", never "×2".

## Family engine
none

## Sources
- CASEL, "What Is the CASEL Framework?" Self-Management competencies (goal setting, self-motivation): https://casel.org/fundamentals-of-sel/what-is-the-casel-framework/
- Dweck, C. S. (2006). Mindset: The New Psychology of Success. Random House ("not yet" framing, mistakes as information).
- Dweck, C. S. (2015, Sept 22). "Carol Dweck Revisits the 'Growth Mindset'." Education Week (effort alone is not enough; new strategies and help from others): https://www.edweek.org/leadership/opinion-carol-dweck-revisits-the-growth-mindset/2015/09
- Sisk, V. F., et al. (2018). "To What Extent and Under Which Circumstances Are Growth Mind-Sets Important to Academic Achievement?" Psychological Science 29(4), 549-571 (effects are small; why the tool says "practice helps" only).
- Yeager, D. S., et al. (2019). "A national experiment reveals where a growth mindset improves achievement." Nature 573, 364-369 (small average effects).
- American Psychological Association, "Building your resilience" (practice, asking for help): https://www.apa.org/topics/resilience/building-your-resilience
- CDC, "Coping with Stress" (take deep breaths): https://www.cdc.gov/mental-health/living-with/index.html
- Anderson, M. and Feil, T. (1998). "Turning Lights Out with Linear Algebra." Mathematics Magazine 71(4), 300-303 (every 3x3 Lights Out start has a unique solution); start states and fewest presses also checked by brute force over all 512 press sets.
- Number Lift fewest moves checked by breadth-first search over floors 0 to 20; pattern answers are arithmetic.

## Done when
1. Gym opens with two open rooms, three locked; tapping a locked door shows the goal message and Pick a goal button; tapping Bix plays the stage 1 hop.
2. A wrong Pattern Ladder choice greys out with "Not yet", the strategy cards appear, and Bix shows the thinking face, never a sad one; Know-how never decreases at any point.
3. Solving a rung after a not-yet with a strategy card adds 4 Know-how and one gold stripe; a first-try solve adds 1; replaying a solved rung adds 0.
4. Picking a goal and a plan, then meeting it, opens Light Mat, then Number Lift, then Summit Circuit in that order, with the reflection card each time.
5. Every Light Mat and Number Lift rung is solvable in the listed fewest moves, the hint glow always lies on a fewest path, and hitting the move limit resets the puzzle as a not-yet.
6. Memory Mirror ignores taps during playback; Watch again replays the same sequence; Slow down and Break it into parts change the replay as specified.
7. Save Bix then reload resumes with the same stage, stripes, rooms and color; reload without saving starts fresh; Start over clears the save after the confirm.
8. Mode switches stop speech and playback; Read speaks the current hint; Motion off stops Bix's animations and confetti but keeps the breathing timing.
9. At 1366x768, 680x425 and 375 wide, the puzzle, I'm stuck and the strategy cards are visible without scrolling; no console errors.
10. No on-screen text claims the brain grows or gets stronger like a muscle; no em dashes anywhere.

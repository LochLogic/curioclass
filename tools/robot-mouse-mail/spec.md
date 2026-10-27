# Snowy Mail Route
Renamed from: Robot Mouse Mail

## One idea
Pip the mail penguin walks exactly the arrow cards the class lays down and leaves numbered footprints in the snow, one
pair per card, so after every run the class can tap any footprint and see the card that made it: a wrong turn in the
snow points straight at the wrong card.

## Not like
- robot-dance (K, built): moves in place beside a robot that knows the dance, and the tool finds the bug for you (Bolt
  trips). Here there is no reference robot: Pip travels on a grid, the class predicts where Pip will stop, and the
  footprint trail is the evidence they read to find the bug themselves.
- loop-garden (2, built): relative turns (step, turn left, turn right), repeat blocks and fewest-block stars. Here the
  arrows are absolute (up, down, left, right on the screen), there is no repeat, and no stars or block count.
- computer-builder (1, built): its Nibbles the mouse unplugs parts. That is one reason the courier here is a penguin,
  not a mouse (the other is the trademark, see Open questions).
- traffic-light-coder (3, this group): if-then rules checked again and again. Here a straight sequence runs once.
- teach-the-robot, spot-the-ai, input-or-output: AI and hardware ideas, no programs to write.

## Who and how
- Grade 1, computer science. Module: Code a Path (Algorithms and Programming).
- Topic line: coding a path with arrow commands
- Driver: teacher on a projector or smartboard. The class calls out arrows, traces the route in the air with a finger,
  and votes on where Pip will stop.
- 15 to 25 minutes. tool.json: driver "teacher", minutes "15-25", modes ["Snow Town", "Mail Route"],
  grades_label "Grade 1".
- Standards (CSTA 2026 ids from the module): E1-ALG-PS-01, E1-PRO-PD-04, E1-PRO-TR-07. 2017 crosswalk for teachers:
  1A-AP-08 (model daily processes by creating and following algorithms), 1A-AP-10 (programs with sequences),
  1A-AP-14 (debug errors in an algorithm or program).
- Reads nothing: every control has an icon, every fixed line is spoken, targets at least 60 px at full screen.

## Screens and modes
Header (kit): title "Snowy Mail Route", small line "Arrow by arrow through the snow"; mode buttons `.seg` "Snow Town"
(snowflake icon) and "Mail Route" (envelope icon); Motion, Sound, Read (ids `motion`, `sound`, `read`).

Stage (both modes), drawn in code at real pixel size per layout:
- A 6 column by 4 row town of snowy squares (white #ffffff with faint blue grid lines). Square size fills the stage.
- The Post Office (red roof, envelope sign) sits on Pip's start square. Houses: each a small house with a big door
  symbol and its own roof color: Star (yellow roof), Heart (pink), Moon (navy), Fish (teal), Tree (green), Sun
  (orange). The symbol is the address, so non-readers can match it.
- Snowbanks: rounded white mounds with blue shadow; Pip cannot walk into them.
- Pip: a round penguin with a red mail bag. Pip faces the way it last moved. The letter in Pip's bag shows the
  address symbol of today's house.
- Guess flag: a small red flag on a square, only when the class has made a guess.
- Footprints: after a run, each card leaves a pair of webbed footprints on the square Pip stepped into, tinted the
  card's color, with the card's number in a small circle beside them. A bump leaves a snow puff on the blocked square.
- The card strip along the bottom of the stage: up to 12 slots, numbered 1 to 12, empty ones dashed (robot family
  strip, see Family engine). A run pointer (glowing chevron) sits over the card being walked.

Panel:
- `#hint`: one line, always one of the fixed lines below.
- Arrow tray: four 72 px buttons in a plus shape (Up on top, Left and Right in the middle row, Down below), each with a
  big white arrow on its color: Up blue #2563c9, Right purple #7a3fc0, Down green #1f8a4c, Left orange #c4560f. The
  shape (arrow direction) is the signal, color is extra.
- Big buttons: "Guess" (flag icon), "Go" (play, `.big-btn.gold`; becomes "Stop" while walking), "Step" (one footprint
  icon: walk the next card only), "Speed" toggle (turtle Slow default, rabbit Quick).
- Snow Town only: "Clear" (broom).
- Mail Route only: level dots 1 to 8 (filled when delivered), "Start over" (circular arrow: this level's starting
  cards), "Next" (right arrow; enabled after a delivery).

### Mode 1: Snow Town (explore, opens first)
All six houses and the Post Office on one map, three snowbanks. Tap any house: Pip's letter takes that address (the
house glows). Lay arrows, press Go, and Pip walks. Stopping on the addressed house delivers the letter (the door opens,
a heart puff, the house keeps a small envelope badge for the page load). No levels, no score: a free map to play.

### Mode 2: Mail Route (puzzle levels)
Eight levels (Content). Five are Build levels (the strip starts empty). Three are Fix-it levels: the strip starts with
another mail carrier's cards that have one bug, and the hint says so. Each level shows only its own houses and banks.

## Content
Map coordinates: column 1 to 6 left to right, row 1 to 4 top to bottom. "Shortest" is checked by search (BFS) and only
used for the teacher notes; the tool never scores length.

Snow Town: Post Office (1,4). Houses Fish (1,1), Star (2,1), Heart (6,1), Moon (4,2), Sun (3,4), Tree (6,4). Banks
(2,3), (3,2), (5,3). Every house can be reached.

| # | Name (spoken) | Kind | Start | House | Other houses | Banks | Starting cards | Shortest |
|---|---|---|---|---|---|---|---|---|
| 1 | First Delivery | Build | (1,2) | Star (4,2) | Heart (4,4) | none | none | 3: R R R |
| 2 | Down the Lane | Build | (1,1) | Heart (4,3) | Moon (6,1) | none | none | 5: R R R D D |
| 3 | The Snowbank | Build | (1,3) | Moon (5,3) | Star (5,1) | (3,2) (3,3) | none | 6: D R R R R U |
| 4 | Wrong Way | Fix-it | (1,4) | Fish (5,2) | Sun (2,1) | (3,3) (3,4) | U U R R D R | 6: U U R R R R |
| 5 | Long Lane | Build | (1,1) | Tree (5,4) | Sun (3,4) | (2,2) (2,3) (4,2) (4,3) | none | 7: R R R R D D D |
| 6 | One Too Many | Fix-it | (2,1) | Sun (6,2) | Fish (1,4) | (4,1) (4,2) | D D R R R R R U | 7: D D R R R R U |
| 7 | Mixed Up | Fix-it | (1,4) | Star (6,1) | Heart (1,1) | (2,2) (2,3) (5,4) | R U R U U R R R | 8: R R U U U R R R |
| 8 | Big Town | Build | (1,4) | Heart (5,4) | Moon (3,1), Fish (6,4) | (2,3) (2,4) (4,1) (4,2) (4,3) (6,3) | none | 8: U U R R D D R R |

Designed bugs (checked by simulation): level 4 card 5 (Down) walks into the bank at (3,3), bump at card 5, fix: make
it Right. Level 6 has one Right too many: Pip reaches (6,3) after card 6 and card 7 bumps the right edge, fix: take away
any one Right. Level 7 has cards 2 and 3 swapped: card 2 (Up) walks into the bank at (2,3), fix: swap them back.

## Interactions in detail
- Tray tap with nothing selected adds that arrow at the end of the strip; with a card selected it replaces that card
  (the card flips). The arrow name is spoken (move names are events, latest only).
- Card editing is the family strip: tap a card to select (lifts, thick outline); under the strip three 60 px buttons
  appear: Move earlier, Take away, Move later. Escape or tapping the map deselects. Strip limit 12: a 13th tap flashes
  the strip and plays line 17.
- Guess: tap Guess, then tap any square: the flag lands there (tap another square to move it, tap Guess again to remove
  it). Squares are the targets while guessing (at least 60 px). Guessing is optional; Go works without it.
- Go: footprints from the last run fade out, Pip walks one card per beat (Slow 1100 ms, Quick 700 ms), the pointer and
  card glow follow, footprints appear as each step lands, a soft crunch per step.
- Step: walks only the next card and pauses; the pointer waits on the next card. Go after Steps continues from there.
  Any edit resets Pip to the start square.
- Bump (bank or edge): Pip slides back with a wobble, a snow puff on the blocked square, the card that bumped wobbles
  with a "?" badge, the run ends. Comic, never sad: a soft "flump" sound, no buzzer.
- End of cards: Pip stops. On the addressed house: delivered (door opens, chime, letter flies in, level dot fills).
  On another house: "wrong house" (that door stays shut, Pip shrugs). On an empty square: "Pip stopped in the snow".
- Guess check after any run with a flag: flag square equals Pip's last square (a bump counts as where Pip stopped):
  line 24, else line 25. No points.
- Footprint taps: tapping a footprint pair (or its number) selects that card in the strip; selecting a card makes its
  footprints pulse. This is the debugging move the tool exists for.
- Go with an empty strip: line 16, the tray pulses once. Edits are disabled while walking (dimmed, not hidden).
- Fix-it levels: Start over restores the starting cards. Fixing before any Go is allowed.
- Mode switch and level change stop Pip and keep each mode's strip for the page load. Nothing saved to localStorage
  except the kit Motion setting.
- Keyboard: arrow keys on the tray area add arrows; on a selected card Left and Right move it, Delete takes it away;
  G is Go, S is Step. Tab order: mode buttons, header buttons, tray, Guess, Go, Step, Speed, level controls, strip
  cards, card buttons, map squares (only while guessing). Visible focus everywhere.
- Motion off: Pip jumps square to square with no tween, no slide-back, footprints appear without fading; same beat
  timing and sounds.
- Sizes (STANDARDS.md): the tray, Go and the whole strip visible without scrolling at every size. At 680x425 and
  800x500 the tray is a compact 52 px plus, the strip cards at least 44 px, house symbols at least 16 px. Under 760
  wide stack stage over panel with the tray right under the strip.

## Look
- Band K-2, own `:root`: `--paper #f5f9fd`, `--ink #1c2433`, `--muted #55607a`, `--line #d8e3f0`, `--brand #b3261e`
  (post office red, the accent; header), `--focus #1d5fd1` with a 3 px white inner ring, `--gold #ffd23f` for Go.
- Scene: snow #ffffff, grid lines #cfdcec, bank shadow #9db6d6, a dusk sky band #24345a along the top with a few
  lit windows. Pip is navy and white with an orange beak and the red bag.
- Neighbors: robot-dance magenta night stage, loop-garden lawn green, computer-builder cobalt, teach-the-robot grape.
  A white snow map with post red is unlike them; traffic-light-coder (sibling) is asphalt charcoal with amber.
- Contrast: white on header #b3261e 6.54:1; ink on paper 14.71:1; muted on paper 5.94:1; brand red on snow 6.54:1;
  white on dusk sky 12.25:1; focus blue on paper 5.5:1. Arrow buttons are white glyphs on their colors (all above
  4.5:1 by design: the builder checks and darkens a color that fails).

## Art
none: drawn in code (Pip in four facing poses plus shrug and slide, houses, symbols, snowbanks, footprints, flag,
preview.svg with Pip mid-route and a footprint trail).

## Voice
Bank voice `gentle-storyteller` (Vindemiatrix), "Say gently and expressively, like a grandmother reading a picture
book aloud": a snowy picture-book town. Neighbors use lively-host (robot-dance), hero-coach (loop-garden),
bright-teacher (computer-builder), playful-friend (teach-the-robot); no sibling in this group uses it.
Narration through `Curio.voice` (scope: mode plus level). Every spoken line is fixed:

Welcomes and how-to (how: spoken once per page load, then hint only):
1. how, welcome Snow Town: "Welcome to Snow Town! Pip the penguin carries the mail. Pip walks exactly what the arrows say."
2. how: "Tap a house to choose where the letter goes. Then tap the arrows to make Pip's path."
3. how: "Before you press Go, trace the path with your finger. Where will Pip stop? Tap Guess, then tap that square."
4. how, welcome Mail Route: "Time to deliver the mail! Look at the letter in Pip's bag. Find the house with that picture."
5. how: "Tap a card to change it. Use the arrows under the cards to move it, or the trash can to take it away."
6. how: "Press Step to walk one card at a time."
7. how: "Tap a footprint to find the card that made it."
Level lines (how, once per level per page load, on opening the level):
8. "Level one: First Delivery. Take the letter to the Star house." 9. "Level two: Down the Lane. Take the letter to the
Heart house." 10. "Level three: The Snowbank. Pip can't walk through snow. Find a way around." 11. "Level four: Wrong
Way. Another mail carrier made these cards. One card is wrong. Press Go, then find it." 12. "Level five: Long Lane.
Take the letter to the Tree house." 13. "Level six: One Too Many. These cards have an extra step. Find it and take it
away." 14. "Level seven: Mixed Up. Two cards are in the wrong order. Swap them." 15. "Level eight: Big Town. This is a
long one. Go slowly, one arrow at a time."
Events (spoken every time; stale when Pip moves again, the strip is edited, or the mode or level changes):
16. "Add an arrow card first!" 17. "That's twelve cards! Press Go to see where Pip walks." 18. "Delivered! Pip followed
every arrow." 19. "Oh! That's the wrong house. Tap the footprints to see where Pip turned." 20. "Pip stopped in the
snow. Is there a card missing?" 21. "Flump! Pip bumped into a snowbank. Which card sent Pip that way?" 22. "Flump!
That's the edge of town. Which card sent Pip that way?" 23. "All clear. Make a new path!" 24. "Your guess was right!
Pip stopped right on your flag." 25. "Pip stopped somewhere else. Look at the footprints." 26. "That's every level!
Pip's mail bag is empty. Thank you, mail carriers!"
Arrow names (events, latest only): 27. "Up!" 28. "Down!" 29. "Left!" 30. "Right!"
Which line when: Snow Town entry 1 then 2; first Go without a flag in a page load: 3 (how, before Pip walks, the walk
waits for it). Mail Route entry 4 then the level line; level 4 also queues 5. The first bump or wrong stop of the page
load adds 7, the second adds 6. Read speaks `#hint`.

## Family engine
Robot family engine, `kit/robot.js` (new in this wave; this is the full description, traffic-light-coder feeds it the
same way). Lift it from robot-dance's strip and `run(program, target, onStep)` (tools/robot-dance/src.html, "the step
runner"); robot-dance and loop-garden move onto it only when next reworked.
1. Program model: `prog = [{id, op, args}]`. Edits: `add(op, at)`, `replace(i, op)`, `move(i, d)`, `remove(i)`,
   `clear()`, `load(list)`, each firing `onEdit` and bumping a generation number. A `max` length per tool.
2. Card list UI: `Robot.strip(el, {max, layout: 'row'|'column', renderCard, onSelect})` draws numbered cards and dashed
   empty slots, one selection at a time, the three card buttons (Move earlier, Take away, Move later; Move up and Move
   down in a column), keys (arrows, Delete, Escape), card states (`now`, `bug` badge, `pulse`) and the run pointer.
3. Runner: `Robot.run(prog, {style, exec, beat, onStep, target})` with Stop, Step (one card or one tick, then pause),
   Go (continue) and a generation guard so late callbacks of a stopped run are ignored.
   - `style: 'sequence'`: each card once, in order. `exec(card, i)` returns `{ok: true}` or `{stop: reason}`. With a
     `target` it returns robot-dance's results (ok, wrong, ranout, extra).
   - `style: 'rules'`: every tick, cards are checked top to bottom with `when(card, world)`; the first that holds runs
     `exec(card)`; at most one fires per tick; it runs until the tool's script ends or Stop.
4. Trace: `trace = [{t, i, op, result, snap}]` and `Robot.traceFor(i)`, so a tool can draw what each card did.
Sound, voice, art and the world stay in the tool.
This tool feeds it: style sequence, ops `up down left right`, max 12, row layout, `exec` moves Pip on the grid and
returns `{stop: 'bank'|'edge'}` on a bump; the trace draws the footprints and links footprint taps to cards.

## Sources
- CSTA K-12 CS Standards (2017) 1A-AP-08, 1A-AP-10, 1A-AP-14: https://csteachers.org/k12standards/ ; 2026 ids from
  data/standards/csta-2026-ids.txt.
- Code.org CS Fundamentals glossary (algorithm, bug, debugging, program): https://code.org/curriculum/docs/k-5/glossary
- Arrow paths on a grid as a first sequencing activity: Code.org unplugged "Graph Paper Programming",
  https://code.org/curriculum/unplugged
- Maps, levels and bugs are original to Curio Class (paths and bumps checked by simulation in the spec session).

## Done when
1. Snow Town: tapping each house addresses the letter, and a correct path to each of the six houses delivers it.
2. Levels 1 to 8 load the table's map exactly; each Build level can be delivered with its listed shortest path.
3. Fix-it levels: Go on the starting cards bumps at card 5 (level 4), card 7 at the edge (level 6) and card 2
   (level 7), and the fix in Content delivers.
4. After any run, each footprint pair shows its card number; tapping it selects that card, and selecting a card
   pulses its footprints.
5. Guess: the flag places, moves and removes; lines 24 and 25 match where Pip stopped, including after a bump.
6. Step walks one card at a time and Go continues; any edit resets Pip; Stop halts at once.
7. Keyboard only: a level can be built, run and fixed with Tab, Enter, arrows, Delete, G and S, focus visible.
8. Every size in STANDARDS.md: tray, Go and the full strip visible without scrolling; scene text 10 px or more in the
   preview; 60 px targets at full screen.
9. Voice: held-click first tap follows the welcome rules; how-to lines 2, 3, 5, 6, 7 spoken at most once in a run of
   five actions; events 18 to 25 spoken every time and dropped when stale; Read and Sound rules pass.
10. Motion off: no tweens, same timing; console clean through all eight levels.

## Open questions
- Title: the overlap pass gave "Robot Mouse Mail", but "Code & Go Robot Mouse" is a well known coding toy that does
  this exact activity, and computer-builder already has a mouse. This spec renames it "Snowy Mail Route" with a penguin.
  Keep the rename, or prefer another title?

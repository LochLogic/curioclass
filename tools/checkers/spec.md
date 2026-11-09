# Checkers (Recess game)

A night arcade where neon pucks hop across a glowing grid: chain your jumps, pop a crown, and outsmart a kind computer, a
friend, or a short puzzle.

## One idea

Checkers is the game of "if I give one, can I take two?". Because a jump must be taken, you can make your opponent's move
for them: offer a puck they are forced to jump, and the jump lands right where your double jump starts. Every mode keeps
that one thought in view. The board always lights the pieces that must jump, and the puzzle set climbs from a single hop to
the classic "shot" and the old two-against-two endgame problems.

## The world

**Look.** A late-night arcade, seen as if you leaned over a glass-topped game table. A painted backdrop (dark cabinet row,
blurred marquee lights in magenta and cyan, a faint haze) sits behind a board drawn in code: a deep navy table with a thin
glowing grid, the 32 playable dark squares slightly lifted, and pucks that look like lit acrylic: a bright rim, a softer
face, a glow that spills onto the square around them. Light comes from the pucks themselves; the backdrop stays dim so the
board is the brightest thing on screen.

**Two sides, told apart without color.** Amber moves first (Amber plays the classic "Black" side, starting on squares
1 to 12). Blue moves second. Every Amber puck carries a solid round dot in its ink color; every Blue puck carries a hollow
ring. A king keeps its side mark and gains a second rim (a stacked-puck edge) and a crown drawn in the side's ink, so
"king or man" and "Amber or Blue" both read in grayscale.

**Palette** (matches the shelf row's background `linear-gradient(160deg,#151a4a,#070a22)` in data/recess.json):

| Token | Hex | Use |
|---|---|---|
| bg | #070A22 | page behind everything |
| frame | #151A4A | table rim, side panels, cards |
| dark | #121842 | playable squares |
| light | #232B6E | the unplayable squares (inert) |
| grid | #5B6CFF | 2 px grid lines and board edge glow |
| amber | #FFA51F | Amber pucks, accent `--rc-accent` |
| amberInk | #2B1600 | Amber dot mark, crown, outline |
| blue | #2F8BFF | Blue pucks |
| blueInk | #04112E | Blue ring mark, crown, outline |
| text | #F4F6FF | all text |
| dim | #AEB6E8 | secondary text (counters, captions) |
| sel | #7CFFB2 | selection ring, legal-move dots, keyboard cursor |
| must | #FF5FD2 | "must jump" ring |

Contrast checked in Python (WCAG relative luminance, `ck_color.py`): amber on dark 8.63, blue on dark 5.07; amberInk on
amber 8.75; blueInk on blue 5.56; text on bg 18.11, on frame 15.23, on dark 15.77; dim on frame 8.33, on bg 9.91; sel on
dark 13.61, on light 10.23, on frame 13.14; must on dark 6.33, on frame 6.12; grid on dark 4.08; light vs dark only 1.33,
on purpose: the light squares are never used, and the grid lines carry the checkerboard. Amber vs blue is only 1.70
(Machado 2009 color-blind simulation: protan 1.29, deutan 2.03, tritan 1.32), which is why the dot and ring marks are
required, never optional. A white crown on amber would be 1.97, so crowns are drawn in the side's ink instead.

**Materials.** Pucks: an SVG circle (82 percent of the square) with a 3 px rim one step lighter than the face, the mark in
ink, a radial highlight at the top left, and a glow (a blurred copy at 35 percent opacity). Board: flat navy with the grid
glow; each dark square has a 1 px inner highlight on its top edge, so it reads as a lifted tile.

**The grab moment.** Touch a puck and it lifts: it grows 8 percent, its glow brightens, and small mint dots pulse on every
square it may go to. A jump is the show: the puck stretches tall as it leaves, arcs over the jumped piece, and squashes
flat on landing, hop after hop, each hop a higher note. The jumped pucks flash white and pop into a little ring of sparks.
Reach the far row and a crown drops on from above, overshoots, and settles with a chime.

**Calm mode** (Recess.calm, Recess.onMotion): no stretch, squash, arc, sparks or bounce. Moves land after a 120 ms
crossfade, a jumped puck fades out, a crown appears in place, the must-jump ring is steady instead of pulsing. Glows stay
(they are static), so the world still reads as a lit arcade table.

## Rules

Standard American checkers (English draughts), as in the Laws in Lyman 1881 (see Sources), with modern practice from the World Checkers Draughts Federation (no huffing). The "How to play" card states
these in kid words; the builder must get every line right.

- **Board.** 8x8, play on the 32 dark squares only. Each player has a dark square in the corner at their left hand.
  Squares are numbered 1 to 32 in the data: row by row from Amber's back row, four per row. In code: row r = floor((s-1)/4)
  from Amber's side; rows 0, 2, 4, 6 use columns 1, 3, 5, 7 and rows 1, 3, 5, 7 use columns 0, 2, 4, 6. So square 1
  touches 5 and 6, square 4 touches only 8, square 5 touches only 1 and 9.
- **Start.** 12 Amber men on 1 to 12, 12 Blue men on 21 to 32. Amber moves first (checked: 7 legal first moves).
- **Men** move one step diagonally forward to an empty dark square. Men never move or jump backward.
- **Jumping.** Jump an adjacent enemy piece diagonally, landing on the empty square right behind it; the jumped piece is
  removed. If the landing piece can jump again, it must keep going in the same move (a chain).
- **A jump must be taken.** If any of your pieces can jump, you must jump. You may choose which jump or chain, even a
  shorter one (there is no "take the most" rule in American checkers), but once you start a chain you must finish it.
- **Jumped pieces** come off at the end of the move, and no piece may be jumped twice in one move.
- **Crowning.** A man that reaches the far row becomes a king. If it got there by jumping, the move ends there, even if
  the new king could jump again: it waits for the next turn.
- **Kings** move and jump one square diagonally in all four directions (no long-range "flying" kings).
- **Winning.** You win when the other side has no pieces left or no legal move on their turn (blocked pieces lose).
- **Draws, explained kindly.** (1) The same position with the same player to move comes up a third time: automatic draw,
  "The same position came up three times. Neither side can get ahead, so it is a draw." (2) 40 moves by each side (80 turns)
  with no jump and no man moving: automatic draw, "40 moves each with no jumps and no men moving. Nobody can break
  through, so it is a draw." From 20 such moves each, a small "No progress: 20 of 40" counter shows in the side panel so
  it is never a surprise. This automates the old referee rule (a player must show the win within 40 moves). In Play a
  friend there is also "Call it a draw" (both players tap it).

**Edge cases a builder gets wrong** (each needs a unit test in the file's self-check, see Done when):
1. Men capturing backward (not allowed). 2. Flying kings (not allowed). 3. Forcing the longest capture (not a rule).
4. Crowning mid-chain: the move stops (test: Amber man 22, Blue men 26 and 27 on the board as in `pos('22','','26 27')`:
the only move is 22x31 and it stops; the same piece as a king continues 22x31x24). 5. A king may jump back across the
square it started from in a chain (the start square is empty while it moves). 6. Jumped pieces stay on the board until
the move ends (they block landings and can't be jumped twice). 7. Blocked means lost, even with pieces left. 8. A plain
move is illegal while any jump exists anywhere: the tapped puck shakes and the pieces that can jump glow.

**House rules and a "casual" toggle: not shipped.** Many kids learned "jumps are optional" or "huff" (take the piece that
skipped a jump). A toggle would split the puzzles (every shot depends on forced capture) and the computer's play, and the
must-jump glow already removes the usual confusion: you never have to spot a forced jump yourself. The How to play card
says it plainly: "In real checkers, if you can jump, you must. The board shows you when." (Open question 2.)

## Modes and levels

On load the game shows the **Marquee**, a game-owned attract screen styled like a lit cabinet header (not a shell card):
Play the computer, Play a friend, Puzzles, Today's puzzle, How to play. "Menu" (P) in the side panel returns to it any time;
a game in progress is kept in Recess.store and resumes.

| Mode | Recess.level key | Label shown |
|---|---|---|
| Computer, Pip | `cpu-1` | "Versus Pip" |
| Computer, Dot | `cpu-2` | "Versus Dot" |
| Computer, Nova | `cpu-3` | "Versus Nova" |
| Computer, Comet | `cpu-4` | "Versus Comet" |
| Computer, Blaze | `cpu-5` | "Versus Blaze" |
| Computer, Titan | `cpu-6` | "Versus Titan" |
| Play a friend | `friend` | "Play a friend" |
| Puzzle rounds (5) | `p-1` ... `p-5` | "Puzzles: First jumps" etc. |
| Today's puzzle | `daily-YYYY-M-D` (Recess's own date format) | "Today's puzzle" |

`Recess.start({id: 'checkers', title: 'Checkers', score: {label: 'Moves', lower: true}, onUndo, onRestart, onNext})`.
One score everywhere: **Moves you made**, fewer is better. Every move you play counts, including moves later taken back and
wrong puzzle tries, so Undo can never lower it.

**Play the computer.** Full games on a ladder of six opponents, ordered by strength (checked by level-against-level games,
see Content). The gentle three, Pip, Dot and Nova, are kind and slip on purpose. The strong three, Comet, Blaze and Titan,
never slip and play a real engine: Titan thinks up to 3 seconds a move and is meant to challenge a good adult player. The
ladder card shows each opponent as a row of 1 to 6 lit bulbs, with a line under the strong three: "No slips. Plays to
win." Pick an opponent and a side (Amber, Blue, Either; Either uses Math.random). Win:
Recess.win({score: moves made, stars}). Stars: 3 = no takebacks, 2 = one to three takebacks, 1 = any win. A loss or draw
shows the game's own result card ("Blaze wins this one. Take back a few moves, or play again?") with Undo still live; no
Recess.win. onNext after a win starts a new game one rung up (Titan stays on Titan). A draw against Titan gets its own
warm line on the result card ("A draw with Titan is a real result."), still no Recess.win.

**Play a friend.** Pass-and-play on one device. The prompt says "Blue's turn"; the board stays put (Flip turns it; a
"Turn the board each move" switch, default off, flips after every move for face-to-face play). Game end shows the result
card ("Amber wins: Blue has no moves left!"). No Recess.win and no stars: two players, one score would mean nothing.

**Puzzles.** Five rounds of five (25 puzzles, data under Content), gentle first: 1 First jumps, 2 Give one, take two,
3 Shots, 4 Endings from 1913, 5 Classic finishes. The board turns so the solver's side is at the bottom; the prompt names
the goal ("Amber to play. Give one, take two."). The computer plays the replies.
- **Line puzzles** (`kind:'line'`): your move must be the book move at each step. A move listed in `also` for that step
  ("That wins too! This puzzle follows the book's way; try another.") springs back and is not a try. A move that ends the
  game on the spot always counts (Fence has two: 10-14 and 10-15). Any other move is shown for 0.9 s, springs back with a
  kind line that says what was off ("After that, Blue is not forced to jump. Look for a puck you can give away." for shots;
  "That lets Blue slip away. Look again." for endings) and counts as a try.
- **Ending:** a puzzle ends when the line is finished or the game is won. The eleven 1913 endings stop where the book stops,
  at a position the solver proved won; the card says "Blue is trapped. From here Amber wins every time."
- **Clue** (C) lights the piece to move and counts as a try. After three tries the answer plays itself slowly ("Here is how
  it goes.") and the puzzle counts as three tries.
- **Round scoring.** Recess.win after the fifth puzzle. Score = moves made across the round. Best possible (sum of your
  moves in the lines, checked in Python): round 1 = 6, round 2 = 10, round 3 = 12, round 4 = 23, round 5 = 40. Stars:
  3 = no tries or clues, 2 = one or two, 1 = finished.
- **First run counts.** The round's tally (puzzle index, moves, tries) lives in Recess.store(`run:<key>`) until the round
  ends, so Restart and reload never clear it. Replays are Encore runs: same puzzles, a game-owned Encore card at the end
  ("You already finished this round with 2 stars. Encores are for fun."), and no second Recess.win.

**Today's puzzle.** `const r = Recess.daily(); const i = Math.floor(r() * 25); const swap = r() < 0.5;` If `swap`, every
square s becomes 33 - s and the colors trade places (Amber pieces become Blue and the other side moves), a mirror that keeps
every move legal (checked in Python on 5000 random positions, 0 mismatches). Same for everyone that day. One-puzzle level,
scored and starred as a puzzle; first run counts, later runs that day get the Encore card.

## Screens and controls

**1366x768 (Chromebook).** Shell bar on top (about 54 px). Below, the backdrop fills the page and the board sits centered,
600x600 (75 px squares, puck 62 px). Left panel (240 px): the opponent badge (painted, name, "thinking" lights) or "Blue"
in friend mode, and Blue's taken-pucks tray. Right panel (240 px): Amber's tray, the prompt box (two lines, text on frame),
the no-progress counter when shown, then buttons: Menu, Clue (puzzles), Flip, Hints, and in friend mode "Turn the board
each move" and "Call it a draw". Everything above the fold.

**390x844 (phone portrait).** Shell bar collapses to icons (the shell does this under 760 px). Then: opponent strip (badge
40 px, name, tray), the board at 374x374 (46.75 px squares, above the 44 px tap target), your tray, the prompt box, one row
of four 44 px buttons (Menu, Clue or Flip, Hints, More). The backdrop uses its portrait crop.

**Pointer and touch.** Tap a puck, then tap where it goes; or drag it (pointer events, one code path; under 6 px of drag is a
tap). For a chain, tap each landing in turn, or tap the final square when only one chain ends there; the chain so far is
drawn as a glowing path and the move is not played until the chain is complete. Tap the start puck again to cancel.

**Keyboard.** The board is a grid of 32 dark-square buttons with roving tabindex, each named "square 14, Amber man" or
"square 18, empty". Arrow keys move the mint cursor diagonally: Up and Down go to the forward or back diagonal on the
cursor's side (Left and Right switch which diagonal), and Home/End jump to the first or last of your movable pieces.
Enter or Space picks up and puts down, and continues a chain hop by hop; Escape cancels the move in progress. Game keys
avoid the shell's U, R, M, S: H toggles Hints, F flips, C is Clue, P opens the Menu. Ctrl+Z is the shell's Undo.

**Hints** (legal-move dots, on by default, Recess.store('hints')). The must-jump ring is not a hint: it is always on, because
it is a rule display. Hints never show the best move and cost nothing.

**Undo and Restart by mode.**

| Mode | Undo | Restart |
|---|---|---|
| Computer | Takes back your last move and the computer's reply (if it is still thinking, the search is cancelled). Counts one takeback. Live after a loss or draw; off after a win. | New game, same opponent and side. |
| Friend | Takes back one move. Unlimited. After a finished game it reopens it. | New game. |
| Puzzle | Back to the last solved step (your move plus its reply). Never lowers the tally. | This puzzle from its start; the round's tally stays. |
| Today's puzzle | As Puzzle. | As Puzzle. |

Recess.canUndo is true whenever the rule above has something to take back.

## Motion and sound

| Event | Motion | Calm version | Sound |
|---|---|---|---|
| New game | Pucks drop onto their squares row by row with a squash on landing, 40 ms stagger, about 700 ms | Fade in 150 ms | game layer: "power up" chirp, square wave 330 to 660 Hz, 0.15 s, volume .05 |
| Pick up | Puck grows 8 percent, glow brightens, dots pulse | Mint ring and dots only | Recess.play('tap') |
| Step | Slide 160 ms, small squash on arrival (scaleX 1.12, scaleY .88, 80 ms) | Land after 120 ms crossfade | Recess.play('place') |
| Each hop of a jump | Arc 200 ms (apex 18 percent of a square), stretch in flight (scaleY 1.15), squash on landing; jumped puck flashes white and pops into 6 sparks | Hop to hop at 120 ms, jumped puck fades | Recess.play('capture') plus game layer blip, square wave at 440 Hz times 1.26 to the hop index (440, 554, 698, 880), 0.08 s, volume .06 |
| Must jump | Must ring pulses (1.2 s cycle) on every piece that can jump | Steady ring | none |
| Illegal or wrong | Puck shakes 3 px twice and returns | Returns at once | Recess.play('nope') |
| Crowning | Crown drops from above, scale 1.4 to 1 with overshoot, second rim appears, sparkle | Crown appears | Recess.play('pop') plus game layer chime, sines 1046 and 1568 Hz, 0.25 s, volume .07 |
| Computer thinking (at least 350 ms; up to 3 s for Titan, never blocking the page) | Badge's marquee lights chase | "thinking..." text | none |
| You win | Your pucks bounce in a wave, then Recess.win (card, confetti) | Card only | Recess.play('win') via Recess.win |
| You lose, or a draw | Grid glow dims to half, result card | Same without the dim animation | game layer: two soft low notes (196 then 165 Hz sine, .2 s each), never a buzzer |
| Puzzle step solved | Mint flash on the landing square | Mint outline | Recess.play('pop') |

Sound is one tap away (shell Sound button, M). The game layer makes its own nodes only when Recess.sound is true, after the
first pointerdown, the same pattern as the shell.

## Content

### The computer opponents (exact design)

Six opponents in two families that share the one move generator. All search runs in a Web Worker built from a Blob inside
the file (offline, the page never freezes); the 350 ms minimum think time keeps every reply feeling like a turn.

| Rung | Name | Engine | Strength setting | Slips |
|---|---|---|---|---|
| 1 | Pip | Gentle | depth 1 | 0.35, +0.25 when 2 or more ahead |
| 2 | Dot | Gentle | depth 2 | 0.15, +0.25 when 2 or more ahead |
| 3 | Nova | Gentle | depth 4 | 0.05 |
| 4 | Comet | Strong | fixed depth 6 | none |
| 5 | Blaze | Strong | fixed depth 8 | none |
| 6 | Titan | Strong | iterative deepening, 3 s a move (stops starting a new depth after 1 s), at least depth 10 | none |

#### The gentle engine (Pip, Dot, Nova)

A small minimax with alpha-beta:

- **Search.** Depth in plies per level. At depth 0, if the side to move has a jump, keep searching (capture extension, up to
  6 extra plies), else evaluate. No legal move = loss for the side to move (score -10000 for the computer's side).
- **Evaluation** from the computer's side (own minus opponent): man 100 + 4 per row advanced from its own back row, +10
  while it still sits on its own back row (guards the crowning squares); king 150; +6 for a piece on 14, 15, 18 or 19.
- **Levels and slips.** Pip: depth 1, slip 0.35. Dot: depth 2, slip 0.15. Nova: depth 4, slip 0.05. Kindness: Pip and Dot
  add 0.25 to the slip chance while they are 2 or more pieces ahead. A slip plays a random move from the non-best moves
  that score above -5000 (a slip is never a move that walks into a forced loss inside the search). With one legal move,
  play it.
- **Ties** go to the move first in generator order (from-square ascending, then to-square ascending).
- **Randomness is seeded** by `Recess.rng(level + ':' + positionKey)`: the same position always gets the same reply, so
  Undo cannot fish for a slip.
- **How kind is it** (Python, `ck_ai.py`, 60 games per pairing, sides alternated, same draw rules). "Beginner" is a model
  child: takes the longest jump, else a random move that does not hang a piece.

| Pairing | Result (wins, losses, draws for the first named) |
|---|---|
| Pip vs random mover | 51, 6, 3 |
| Pip vs beginner | 2, 35, 23 |
| Dot vs beginner | 15, 22, 23 |
| Nova vs beginner | 41, 2, 17 |
| Dot vs Pip | 48, 3, 9 |
| Nova vs Dot | 53, 4, 3 |

So a beginner beats Pip most games, has a real fight with Dot, and needs to learn the shot to beat Nova. Never crushing:
Nova still slips 1 move in 20 and is depth 4.

#### The strong engine (Comet, Blaze, Titan)

A real alpha-beta engine (negamax form), as simulated in `ck_strong.py`:

- **Iterative deepening** from depth 1 up to the rung's depth (Titan: until the time budget), each pass seeding the next.
- **Transposition table:** a Map keyed by a 64-bit Zobrist hash (two 32-bit halves: 32 squares x 4 piece kinds, plus side
  to move), entries {depth, value, bound (exact, lower, upper), best move}, capped at 1,000,000 entries (cleared when
  full and at the start of each new game).
- **Move ordering:** the table's best move first, then longer jumps first, then the history heuristic (a quiet move that
  caused a cutoff gets depth squared added to its from-to score).
- **Extensions:** jumps are always searched out at depth 0 (capture quiescence, up to 8 plies past the horizon), and a
  position with only one legal move does not use up depth.
- **Evaluation** from the side to move, own minus opponent: man 100 plus advancement (3 per row while more than 12 pieces
  are on the board, 6 per row after); king 140, +8 on 14, 15, 18, 19 and +4 on 10, 11, 22, 23; man on 14, 15, 18, 19 +5;
  back-row guard +12 for a man still on its side's 1 and 3 (Blue: 30 and 32) while more than 10 pieces remain; any piece
  on a side edge (5, 12, 13, 20, 21, 28) -2. Trade-down term: when ahead, add (2400 minus all material on the board) / 30, so
  the same lead is worth more with fewer pieces, which makes the engine trade when winning. A win is 100000 minus plies
  to it, so it takes the fastest win and the slowest loss.
- **Variety without slips:** in the first 4 plies of a game, the strong rungs pick at random (seeded by
  `Recess.rng(level + ':' + positionKey)`) among moves within 15 points of the best, so games differ; after that, always
  the best move.
- **Speed:** measured in Python (about 40,000 positions a second): from the opening, depth 8 = 92,577 positions in 2.5 s;
  from a middle-game position, depth 6 = 15,107, depth 8 = 99,875, depth 10 = 743,889 (17.5 s), so each 2 plies cost
  about 7 times more. A JavaScript build in a Worker is expected to search on the order of 1 to 2 million positions a
  second on a Chromebook, which puts Titan at about depth 11 to 13 in its 3 s; the builder logs the depth reached (Done
  when). Comet and Blaze answer in well under a second.

**The ladder is ordered by strength** (Python, `ck_strong.py`, each pair plays the same random 3-ply opening twice with
sides swapped, the tournament "ballot" idea; same draw rules; "D" = strong engine at that depth):

| Pairing | Result (wins, losses, draws for the higher rung) |
|---|---|
| Dot vs Pip (rung 2 vs 1) | 48, 3, 9 of 60 (above) |
| Nova vs Dot (3 vs 2) | 53, 4, 3 of 60 (above); 17, 0, 3 of 20 in the ballot run |
| Comet vs Nova (4 vs 3) | 15, 0, 5 of 20 |
| Blaze vs Comet (5 vs 4) | 3, 0, 9 of 12 |
| Titan stand-in at fixed depth 10 vs Blaze (6 vs 5) | 3, 0, 3 of 6 (Titan in JavaScript searches deeper than 10, so this is a floor) |

No higher rung lost a game to the rung below in any run. Draws grow up the ladder because checkers between careful players
is drawish; the strong rungs are separated by not losing, then by wins. Samples are small (Python is slow at depth 10), so
the in-file `?ladder` check repeats them in JavaScript.

### Puzzle set (25, ships in the file)

Squares as in Rules. `move:'A'` = Amber to move, `'B'` = Blue to move. `am, ak, bm, bk` = Amber men and kings, Blue men
and kings. `line` = the moves in order, both sides (`-` a step, `x` a jump with every landing). `also` = 0-based ply index:
other moves that the solver proved also win at that step. Every puzzle is `kind:'line'`.

```js
const PUZZLES = [
// Round 1: First jumps (our own)
{id:'r1-1', name:"Hop", src:'own', kind:'line', move:'A', am:[14], ak:[], bm:[18], bk:[], line:'14x23', goal:"Jump the blue puck."},
{id:'r1-2', name:"Double", src:'own', kind:'line', move:'A', am:[1,5,11], ak:[], bm:[6,15], bk:[], line:'1x10x19', goal:"Take both blue pucks in one move."},
{id:'r1-3', name:"Triple", src:'own', kind:'line', move:'A', am:[1,3], ak:[], bm:[6,15,24], bk:[], line:'1x10x19x28', goal:"Keep jumping: take all three."},
{id:'r1-4', name:"Crown", src:'own', kind:'line', move:'A', am:[1,26], ak:[], bm:[5,29], bk:[], line:'26-30 29-25 30x21', goal:"Make a king, then win."},
{id:'r1-5', name:"Fence", src:'own', kind:'line', move:'A', am:[10,13,17], ak:[], bm:[21], bk:[], line:'10-14', goal:"Win without jumping: leave Blue no move."},
// Round 2: Give one, take two (our own)
{id:'r2-1', name:"Give one, take two", src:'own', kind:'line', move:'A', am:[3,8], ak:[], bm:[14,16], bk:[], line:'8-11 16x7 3x10x17', goal:"Give one puck away to take two."},
{id:'r2-2', name:"Side door", src:'own', kind:'line', move:'A', am:[1,4,5,7,12], ak:[], bm:[13,15,17,21,26], bk:[], line:'5-9 13x6 1x10x19', goal:"Give one, take two."},
{id:'r2-3', name:"Middle march", src:'own', kind:'line', move:'A', am:[4,8,10,12,14], ak:[], bm:[13,16,19,24,25], bk:[], line:'10-15 19x10 12x19x28', goal:"Give one, take two."},
{id:'r2-4', name:"Edge trick", src:'own', kind:'line', move:'A', am:[9,11,12,16,20], ak:[], bm:[17,21,26,28,32], bk:[], line:'20-24 28x19 16x23x30', goal:"Give one, take two."},
{id:'r2-5', name:"Swing", src:'own', kind:'line', move:'A', am:[3,6,8,10,15], ak:[], bm:[20,22,24,30,31], bk:[], line:'15-18 22x15 10x19x28', goal:"Give one, take two."},
// Round 3: Shots (our own), then a 1913 king ending
{id:'r3-1', name:"Long reach", src:'own', kind:'line', move:'A', am:[3,6,11,15,18,20], ak:[], bm:[17,21,25,27,30,31], bk:[], line:'18-23 27x18 15x22x29', goal:"Give one, take two."},
{id:'r3-2', name:"Back row", src:'own', kind:'line', move:'A', am:[1,2,7,8,13,14], ak:[], bm:[15,16,20,24,27,30], bk:[], line:'7-11 16x7 2x11x18', goal:"Give one, take two."},
{id:'r3-3', name:"Into the corner", src:'own', kind:'line', move:'A', am:[2,5,13,17,18,19], ak:[], bm:[14,15,25,26,30,31], bk:[], line:'17-22 26x17 13x22x29', goal:"Give one, take two."},
{id:'r3-4', name:"Three for one", src:'own', kind:'line', move:'A', am:[1,5,6,9,12,18], ak:[], bm:[17,19,21,25,27,29], bk:[], line:'9-14 17x10 6x15x24x31', goal:"Give one, take three."},
{id:'r3-5', name:"Mar's corner", src:'callMar', kind:'line', move:'A', am:[], ak:[10,14], bm:[11], bk:[3], line:'10-15 11-8 15-11 8-4 11-16 3-8 16-12', goal:"Amber to play and win."},
// Round 4: Endings from 1913 (Call, Midget Problems)
{id:'r4-1', name:"Sturges' squeeze", src:'call14', kind:'line', move:'A', am:[1], ak:[10], bm:[5,17], bk:[], line:'10-7 17-14 1-6 5-1 6-9', goal:"Amber to play and win."},
{id:'r4-2', name:"Wardell's walk", src:'call22', kind:'line', move:'A', am:[2], ak:[27], bm:[13,30], bk:[], line:'2-6 30-25 27-23 25-22 6-10 13-9 10-14', goal:"Amber to play and win."},
{id:'r4-3', name:"Slocum's pin", src:'call63', kind:'line', move:'A', am:[6], ak:[5], bm:[29], bk:[4], line:'5-9 29-25 9-14 25-22 6-9 4-8 14-10 22-18 10-7', goal:"Amber to play and win."},
{id:'r4-4', name:"Potterdon's pair", src:'call51', kind:'line', move:'A', am:[], ak:[3,23], bm:[12], bk:[20], line:'23-27 20-16 3-7 12-8 7-3 8-4 27-23 16-12 23-19', also:{6:'27-24', 8:'3-7 23-18'}, goal:"Amber to play and win."},
{id:'r4-5', name:"Slocum's crown race", src:'call58', kind:'line', move:'A', am:[6], ak:[18], bm:[32], bk:[29], line:'6-10 32-27 10-15 27-24 18-22 24-20 15-18 20-16 22-17 29-25 17-21', also:{2:'10-14'}, goal:"Amber to play and win."},
// Round 5: Classic finishes (Call 1913)
{id:'r5-1', name:"Wilder's chase", src:'callWilder', kind:'line', move:'A', am:[5], ak:[23], bm:[28], bk:[31], line:'5-9 28-24 9-14 24-20 14-18 20-16 23-19 16-11 18-23', also:{8:'19-15'}, goal:"Amber to play and win."},
{id:'r5-2', name:"Brown's long walk", src:'call12', kind:'line', move:'A', am:[1], ak:[9], bm:[30], bk:[4], line:'9-14 30-26 14-18 4-8 1-5 8-11 5-9 11-7 18-15 7-2 15-10 26-23 10-15', also:{4:'1-6'}, goal:"Amber to play and win."},
{id:'r5-3', name:"Wardell's tempo", src:'call13', kind:'line', move:'A', am:[5], ak:[9], bm:[25,26], bk:[], line:'9-14 25-22 5-9 26-23 14-10 22-18 10-7 18-15 9-14 15-10 7-11 10-6 11-15', also:{12:'11-16 11-7 11-8'}, goal:"Amber to play and win."},
{id:'r5-4', name:"Brown's chase", src:'callBrown41', kind:'line', move:'A', am:[2], ak:[22], bm:[32], bk:[30], line:'2-7 32-27 7-11 27-24 11-15 24-20 15-18 20-16 22-17 30-25 17-21 25-29 18-22 16-11 21-17', also:{12:'21-17'}, goal:"Amber to play and win."},
{id:'r5-5', name:"Brown's pin", src:'callBrown40', kind:'line', move:'A', am:[], ak:[4,15], bm:[26], bk:[12], line:'15-18 12-16 4-8 16-20 8-11 20-24 11-15 24-27 15-19 27-32 18-14 32-27 14-10 27-32 19-24 32-28 24-27 28-32 27-31 26-23 10-7 32-28 31-27 23-19 7-11', also:{4:'8-12', 6:'11-16', 12:'14-18 14-9', 14:'10-14', 16:'24-19', 18:'27-24', 22:'31-26'}, goal:"Amber to play and win."},
];
```

**What was checked in Python** (scratch scripts, own move generator `ck_engine.py`, not shipped):
- Every line is legal move by move and each move matches exactly one legal move under forced capture (`ck_final.py`,
  `ck_emit.py`). Every Blue reply in the shots is the only legal move (a forced jump), so forced capture is what makes them
  work.
- Rounds 1 to 3 (ours): each ends with Blue out of moves (rounds 1 and r2-1) or a material gain (+1, and +2 for Three for
  one); a 3-ply material search with capture extension, repeated at 5 plies, finds the book first move as the only gaining
  move (next best gains 0). Fence: 10-14 and 10-15 both block at once (the "ends the game" rule accepts both).
- All eleven Call puzzles (r3-5, round 4, round 5): an exact retrograde solve of every reachable position (`ck_retro.py`,
  `ck_callr.py`, `ck_callfix.py`, `ck_rep.py`; 299,313 to 1,383,862 positions each) shows the start is a forced win for
  Amber, the book line is legal under forced capture, every book move keeps the win, and the alternatives that also win
  are exactly the `also` lists. Where the book stops, Blue to move is lost, in plies: r3-5 42; round 4: 4, 40, 46, 40, 42;
  round 5: 8, 46, 40, 12, 24.
- Two positions read wrong from the text were caught on the page images (Potterdon's 20 and Slocum's 29 are kings).

## Sources and licences

| Source | Verified at | Licence or status (quoted) | What ships |
|---|---|---|---|
| W. T. Call, *Midget Problems: All the Ideas in Positions of 2 vs. 2 Pieces in Checkers*, Brooklyn, 1913 | archive.org/details/midgetproblemsal00call (page images read for pp. 16, 17, 21, 37, 40, 41, 44) | Title verso: "Copyright, 1913, by William Timothy Call". Published 1913, so public domain in the US (before 1931); Call died 1917, so also out of copyright in life plus 70 countries | Positions and move lists of 11 problems (r3-5, r4-1 to r5-5) with the composers' names; no diagrams, no prose |
| J. Lyman, *A Game of Draughts* laws, 1881 | archive.org/details/gameofdraughtsse00lyma | Library of Congress: no known copyright restrictions | Nothing (rules cross-check only; its problem index was too garbled to use) |
| English draughts rules (WCDF practice) | en.wikipedia.org/wiki/English_draughts | Facts only; no text copied | Rules as written above, in our words |

Rounds 1 to 3 except r3-5 (14 of 25) are our own positions, made by a search in Python. Box art, backdrop, badges, sounds: ours.

## Can it be beaten?

| Score, star or win | No-skill path | How it is closed |
|---|---|---|
| Computer win and stars | Random moves | Random beat Pip 6 of 60 (left open on purpose: Pip is for the youngest players). Dot and up: random loses (Pip alone beats random 51 of 60, and each rung beats the one below, Content) |
| Strong rungs (Comet, Blaze, Titan) | Learn one winning line and replay it | Seeded variety in the first 4 plies and a fresh table each game make exact replays unreliable; left partly open: a player who finds a real win against an engine has earned it |
| Strong rungs | Undo until the engine errs | The strong rungs never slip, so the same position gets the same best move; Undo only lets a player try their own other ideas, at a star and a move each |
| Computer stars | Undo abuse | Each takeback drops stars (3, 2, then 1) and adds to Moves; seeded replies mean retrying the same move gets the same answer |
| Computer stars | Restart abuse | Restart is a new game with nothing banked; same positions get same replies, so restarting cannot fish for an early blunder |
| Moves score (computer) | Undo to "replay faster" | Taken-back moves still count |
| Puzzle stars | Random tapping | Only the book (or proved) move counts; every other move is a try; 3 tries plays the answer and gives 1 star |
| Puzzle stars | Undo or Restart a puzzle | Tally lives in Recess.store until the round ends; Undo never lowers it, Restart keeps it, reload keeps it |
| Puzzle stars | Clue spam | Each clue counts as a try |
| Round score | Replay a learned round | Encores never call Recess.win again |
| Daily | Replays | First run only; later runs that day are Encores. The daily may repeat a round puzzle (25 puzzles, possibly mirrored): left open, low stakes |
| Initials board | Initials spam | The shell keeps one top 10 per level; entries need a real win or a first run, so spam costs real play |
| Friend mode | Anything | No score, no stars, nothing to beat |

## Not like

- **Go** (`go`): stones are placed, never moved; capture by surrounding; territory. Checkers is one moving piece, diagonal
  steps and forced jumps.
- **Chess** (`chess`): six piece kinds and checkmate on a paper stage. Checkers has one kind of man plus kings, wins by
  taking or blocking everything, and its puzzles are about forcing jumps, not mates.
- **Cargo Hold** (sliding blocks): a solo route-planning puzzle with no opponent. **Untangle**: a solo spatial drag puzzle.
- **Classroom tools and Curiosities:** grep of tools/ for "checkers" and "draughts" (815 folders) finds no game; the hits are
  fake-or-fact-lab ("fact checkers"), illusion-lab (the checker-shadow illusion), compass-and-straightedge ("draughtsmen")
  and the chess spec's own Not like line. No tool covers move-and-jump board play.

## Art list

| Item | Painted or code | Size |
|---|---|---|
| Arcade backdrop, landscape (cabinet row, blurred marquee lights, haze; no readable brand or game names) | Painted, WebP | 1600x900, about 140 KB |
| Arcade backdrop, portrait crop for phones | Painted, WebP | 780x1688, about 110 KB |
| Opponent badges Pip, Dot, Nova, Comet, Blaze, Titan (round arcade robots with lit faces, growing bigger and brighter up the ladder: Pip small and sleepy, Dot cheerful, Nova bright, Comet with a streak, Blaze flame-lit, Titan tall and calm) | Painted, WebP | 6 at 160x160, about 10 KB each |
| Board, grid, squares, pucks, marks, crowns, glows, sparks, chain path, trays, Marquee | Code (SVG and CSS) | 0 |

**Size budget:** code and CSS about 110 KB (the strong engine and Worker add about 20 KB), puzzle data about 5 KB, images
about 310 KB (about 415 KB inline as base64), shell inlined about 25 KB: about 0.55 MB of the 2 MB goal.

## notes.md

```
# Checkers: a note for teachers and parents

Checkers is a real game of looking ahead. Your child moves round pieces diagonally, jumps the other side's pieces, and
makes a king by reaching the far row. Under the rules of real (American) checkers, a jump must be taken, and that is
where the thinking lives: a player can give a piece away on purpose so that the forced jump sets up a double jump.

What it builds:
- Planning two or three moves ahead ("if I go here, they must jump, then I jump two").
- Seeing patterns on a grid: diagonals, edges, corners.
- Patience and fair play: the game explains draws and never punishes a loss.

Ways to play: against the computer on a ladder of six opponents (Pip, Dot and Nova are gentle and make small slips;
Comet, Blaze and Titan play to win, and Titan is a challenge for a good adult player), with a friend on one device,
or 25 short puzzles. The later puzzles are real endgame problems printed in 1913.

Good questions to ask: "Which piece did you give away, and why did they have to take it?" "Why is the edge a safe
place?" "How did you trap the king?"

House rules: many families play that jumps are optional. Here jumps are required, as in tournaments, and the board
glows to show when a jump is waiting.

Everything stays on this device. No accounts, no ads, no data collected. Best scores use three-letter initials only.
```

## Done when

- [ ] Built on kit:recess (`<script src="kit:recess">`, `<link rel="stylesheet" href="kit:recess">`); no kit:curio header;
      no custom score, stars, initials or high-score UI.
- [ ] A self-check (run on load in dev, `?test`) passes: 7 opening moves; the eight edge cases in Rules; every puzzle line
      plays move by move with one matching legal move each; the 5000-position mirror test from Today's puzzle.
- [ ] Draws fire at the third repetition and at 80 quiet turns, with the kind text; the counter shows from 20 each.
- [ ] Pip, Dot and Nova match the design (depth, slip, kindness, seeded replies); a 20-game Pip vs Nova run in the console
      has Nova winning most.
- [ ] The strong engine runs in a Worker with iterative deepening, the Zobrist transposition table, the move ordering and
      the evaluation as written; Comet and Blaze search exactly depth 6 and 8; Titan answers within 3.2 s on a 1366x768
      Chromebook and logs the depth reached (target at least 10, expected 11 to 13 from the opening).
- [ ] A console ladder check (`?ladder`, 10 ballot games per pair) has each rung scoring more than the rung below.
- [ ] Undo, Restart and Menu while an engine is thinking cancel the search (the Worker is told to stop) and nothing is
      played afterward.
- [ ] Each puzzle accepts the book move, treats every `also` move as described, and accepts any move that ends the game;
      wrong moves show the kind line and count.
- [ ] Round best scores are 6, 10, 12, 23, 40; stars and first-run tally behave as written; Encores never call Recess.win.
- [ ] Amber and Blue are told apart in grayscale (dot vs ring) and kings by rim plus crown.
- [ ] Calm mode: no squash, arcs, sparks or bounce; the board still reads.
- [ ] Works by mouse, touch and keyboard at 1366x768 and 390x844 with no scrolling of the board.
- [ ] No em dashes in the file; "Curio Class" never shortened; notes.md written with the text above.
- [ ] One file under 2 MB, works offline.

## Open questions

Owner: default accepted, Cory 2026-11-08; may tweak later. Each question below stands at its default.

1. Casual "jumps are optional" toggle: default no (see Rules). Say yes and it goes in Play a friend only.
2. Side names Amber and Blue (Amber in the classic Black role). Default: keep.
3. Grade band: the shelf row says k2 with "Grades K-12". Default: keep; Pip and round 1 are for the youngest.
4. Titan's real strength against people is untested: "challenges a good adult" rests on depth 10 or more with a
   transposition table, which is the level of classic home checkers programs. Default: ship as written, then raise the
   time budget to 5 s if adult testers beat it easily.

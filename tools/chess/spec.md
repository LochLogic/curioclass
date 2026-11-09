# Chess (Recess game)

A paper theatre on a little stage, lit from the side: play a kind computer puppet, a friend, or a short puzzle act.

## One idea

Chess is the game of "if I go here, what can they do back?". Every mode keeps that one thought front and center: the
board is the whole stage, the pieces are big cut-paper shapes a kid can read at a glance, and a wrong move is never a
dead end, only a kind line that shows what was off and a hand that puts the piece back.

## The world

**Look.** A toy paper theatre seen from the front row. A painted proscenium (red velvet curtains pulled to the wings, a
scalloped valance, gold trim, a wooden stage floor) frames the board, which sits on the stage like a printed paper
board laid flat and seen from slightly above (straight-on in code; the painted floor gives the depth). Pieces stand up
as cut-paper figures on little paper feet, each with a thin dark ink outline and a second, slightly offset paper layer
behind it so it reads as card with thickness. Light comes from the viewer's left (stage right, in theatre terms): a warm spotlight pool on
the board, and every piece throws a soft shadow down and to the right.

**Pieces** (painted cut-paper sprites, see Art list): the classic Staunton-family silhouettes every kid knows from books
(pawn ball-on-collar, rook battlements, horse-head knight, mitred bishop with a slit, crowned queen with points, king
with a cross), redrawn as flat cut-paper shapes with our own proportions. White's set is ivory card with ink outline;
Black's set is deep ink card with an ivory edge line, so both read on both squares.

**Palette** (shared with the shelf box art `site/templates/recess/art-chess.svg`):

| Token | Hex | Use |
|---|---|---|
| backdrop | #26091a | page behind the theatre |
| curtain | #8e1530 / highlight #b3203f | painted curtains (the image), code fallback colors |
| floor | #3a1408 | stage floor strip, wing panels |
| gold | #ffd27a | trim, focus ring, selected piece rim, accent `--rc-accent` |
| text | #fff4e0 | all text on the dark stage |
| light square | #ecd9b0 | board |
| dark square | #a5714a | board |
| ivory piece | #f7efe0 | White's pieces |
| ink piece | #2a2140 | Black's pieces |
| line | #2a1a14 | outlines, legal-move dots, board coordinates |
| check | #d23a2e | check halo |

Contrast checked in Python (WCAG relative luminance): text on curtain 8.38, on backdrop 16.96, on floor 15.01; gold on
floor 11.49; ink piece on light square 10.88, on dark square 3.64; ivory piece on dark square 3.63, on light square
1.22 (so every piece carries the 2.5 px line outline: line on ivory 14.63, line on light square 12.03, line on dark
square 4.03); ivory vs ink piece 13.22; light vs dark square 2.99; check red on light square 3.45 but on dark square
only 1.15, so the check marker is a red halo plus a 3 px ivory ring (ivory on dark square 3.63) plus the word "Check!".

**The grab moment.** You touch a piece and it lifts off the stage: it rises 6 px, tilts 3 degrees, its shadow stretches
longer to the right, a gold rim lights its edge, and small ink dots bloom on every square it may go to. Drop it and it
lands with a papery tap. Take a piece and the captured figure folds flat backwards like a cardboard cutout knocked
over, then slides off into the wings on its owner's side, where the fallen pieces lie in a neat row.

**Calm mode** (Recess.calm): no lift, tilt, fold or slide. A selected piece gets the gold rim and the dots; a move
appears at once with a 120 ms crossfade; a captured piece appears lying flat in the wing row. Shadows stay (they are
static), so the world still reads as a lit paper stage.

## Rules

Standard chess (FIDE Laws of Chess, the moves and endings). The builder must get every line below right.

- **Board.** White on ranks 1 and 2, a light square in each player's right-hand corner (h1 is light). Queen on her own
  color (White queen d1, Black queen d8).
- **Moves.** King one square any way; queen, rook, bishop slide any distance on lines, never jumping; knight jumps in
  an L and is the only piece that jumps; pawn moves one forward to an empty square, two from its starting rank if both
  squares are empty, captures one square diagonally forward.
- **No move may leave your own king in check.** This covers pinned pieces, moving the king next to the other king, and
  a king "capturing" a defended piece. In double check only a king move can answer.
- **Castling.** King moves two squares toward a rook, the rook jumps to the square the king crossed. Allowed only if:
  neither piece has moved this game (rights are lost for good once either moves, and a rook's right is lost if that
  rook is captured on its home square); every square between them is empty (b1 must be empty for queen-side castling
  even though the king never crosses it); the king is not in check now, does not cross an attacked square and does
  not land in check. Input: drag or tap the king two squares (also accept tapping the king then its own rook).
- **En passant.** Only on the very next move after an enemy pawn moves two squares and lands beside your pawn; you
  capture it as if it had moved one. The captured pawn is removed from the square beside, not the landing square.
  Edge case: en passant is illegal if removing both pawns from the rank exposes your king to a rook or queen on that
  rank (perft position 3 tests this).
- **Promotion.** A pawn reaching the last rank must become a queen, rook, bishop or knight of its color (choice
  required, also when the move is a capture). Show the four cut-paper choices in a small fan over the square; Queen is
  first and focused. Escape or tapping off the fan cancels the move (the pawn goes back). The computer promotes to
  queen unless a knight gives checkmate.
- **Check, checkmate, stalemate.** In check with no legal move: checkmate, the other side wins. Not in check with no
  legal move: stalemate, a draw.
- **Threefold repetition: an automatic draw** the third time the same position appears with the same side to move,
  the same castling rights and the same en passant capture actually available (an en passant square counts only when a
  legal en passant capture exists). FIDE makes threefold a claim; Recess declares it at once so no one has to know to
  claim. Positions before an irreversible move (capture, pawn move, lost castling right) can never repeat, so the
  history may be cleared at each one.
- **Fifty-move rule: an automatic draw** when 50 moves by each side (100 half-moves) pass with no capture and no pawn
  move. If the 100th half-move gives checkmate, checkmate wins.
- **Insufficient material: an automatic draw** when neither side can ever mate: king vs king; king and one bishop vs
  king; king and one knight vs king; kings with bishops only, all bishops on squares of one color. Not a draw on its
  own: two knights vs king, knight vs knight, a single pawn anywhere. Re-check after every capture and promotion.
- No clocks, no resign button (Restart is enough), no draw offers.

**Draws, said kindly** (the game's own result card, Recess.win is not called for a draw):

| Draw | Card line |
|---|---|
| Stalemate | "Stalemate, a draw. The king is not in check, but there is no safe square left and nothing else can move. Tip: when you are winning, leave the king a square to breathe." |
| Threefold | "A draw by repetition. The same position came round three times, so the show ends in a tie." |
| Fifty moves | "A draw: fifty moves each with no capture and no pawn move. Nobody could break through." |
| Not enough pieces | "A draw: there are not enough pieces left for anyone to checkmate. A lone king with one bishop or one knight cannot do it." |

Every draw card ends with "A draw is a fair result. Nobody lost." and offers New game and Look at the board.

**Kind fail messages** (in the prompt box below the board, never a popup; Recess.play('nope'); the piece springs back):

| Cause | Message (fill in piece and squares) |
|---|---|
| Move leaves own king in check (pin, wandering king) | "That would leave your king in check. The rook on e8 could take it." The attacker gets a dashed ink line to the king for 2 s. |
| In check and the move does not help | "Your king is in check from the bishop on b5. Move the king, block the line, or take the bishop." |
| Castling after the king or rook moved | "No castling this game: your king has already moved." (or "that rook has already moved") |
| Castling through or into check / out of check | "You can't castle through check. The knight on e3 watches f1." |
| Castling with pieces between | "Castling needs the squares between the king and rook to be empty." |
| A square the piece can't reach (dots off) | "A bishop moves on diagonals." (one short shape line per piece) |
| Tapping an opponent piece first | "That is Black's piece. It's White's turn." |

## Modes and levels

On load the game opens the **playbill** (a game-owned card styled as a printed theatre programme, not a shell card):
Play the computer, Play a friend, Puzzles, Today's puzzle. A returning player sees the playbill with the last mode
highlighted. "Playbill" is also a button in the stage wing, so modes switch any time (a game in progress is kept in
Recess.store and resumes).

| Mode | Recess.level key | Label shown |
|---|---|---|
| Computer, Mouse | `cpu-mouse` | "Versus Mouse" |
| Computer, Rabbit | `cpu-rabbit` | "Versus Rabbit" |
| Computer, Fox | `cpu-fox` | "Versus Fox" |
| Computer, Owl | `cpu-owl` | "Versus Owl" |
| Computer, Badger | `cpu-badger` | "Versus Badger" |
| Computer, Raven | `cpu-raven` | "Versus Raven" |
| Computer, Lion | `cpu-lion` | "Versus Lion" |
| Play a friend | `friends` | "Play a friend" |
| Puzzle acts (9) | `p-m1-1` ... `p-mat-3` | "Mate in one, Act 1" etc. |
| Today's puzzle | `daily-<lichessId>` (keyed by the puzzle, not the date) | "Today's puzzle" |

Recess.start({id: 'chess', title: 'Chess', score: {label: 'Moves', lower: true}, onUndo, onRestart, onNext}).
One score everywhere: **Moves you made**, fewer is better. Every move you play counts, including moves later taken
back and wrong puzzle tries, so Undo can never lower it.

**Play the computer.** Pick a puppet from the ladder of seven, gentlest first (Mouse, Rabbit, Fox, Owl, Badger, Raven,
Lion; the playbill shows each one's "Plays like" line from Content) and a side (White, Black, Either: Either picks with
Math.random). Win by checkmate: Recess.win({score: moves made, stars}). Stars: 3 = no takebacks, 2 = one to three
takebacks, 1 = any win. A loss shows the game's result card ("Fox wins this one. Take back a few moves, or start a new
show?") with Undo still live; no Recess.win. A draw shows the draw card. onNext after a win starts a new game at the
next puppet up (Lion stays on Lion). All seven are open from the start: no unlocking. The three top puppets show
a small "thinking" bar (search depth reached) so a long think reads as effort, not a freeze.

**Play a friend.** Pass-and-play on one device. White moves, the prompt says "Black's turn" and the board stays put
(Flip button turns it; a "Turn the board each move" switch in the wing, default off, flips after every move for
face-to-face play on a tablet). Game end shows the result card ("White wins by checkmate!"), no Recess.win, no stars
(two players, one score would mean nothing).

**Puzzles.** Nine acts of five puzzles: three kinds (Mate in one, Mate in two, Win a piece) times three bands (Act 1
gentle, Act 2 middle, Act 3 harder). Each puzzle opens with the other side's last move played on the stage (the first
move of the Lichess line, animated, last-move squares tinted), then "Your move. White to play: find checkmate." The
board is turned so the solver's side is at the bottom. The computer plays the replies from the data.
- **Mate in one:** any move that gives checkmate solves it (Python found how many mates each puzzle has; all count).
- **Mate in two:** the stated first move solves step one; any other first move is played, gets "Close, but Black can
  escape: look for a move that leaves no way out." and springs back. Every shipped mate in two has exactly one first
  move that forces mate in two (checked), and no mate in one. Step two: any checkmating move solves it.
- **Win a piece:** the stated moves solve it; a different move gets "A fine move, but there is a stronger one here."
  plus the clue word for the theme (fork, pin, skewer, loose piece, discovered attack) on the second wrong try. Every
  shipped puzzle was checked to have one best first move and one best second move by at least a pawn (search below),
  so the game never rejects a move that wins as much. A checkmating move is always accepted (Lichess does the same).
- **Wrong tries and clues:** a wrong move is shown for 0.9 s, the "nope" line plays, it springs back, it counts as a
  try. A **Clue** button (in the wing) lights the piece to move and counts as a try. After three tries in one puzzle
  the answer plays itself slowly ("Here is how it goes.") and the puzzle counts as three tries.
- **Act scoring:** Recess.win after the fifth puzzle. Score = moves made across the act (best possible: 5 for Mate in
  one, 10 for Mate in two and Win a piece). Stars: 3 = no tries or clues, 2 = one or two, 1 = finished.
- **First run counts.** The act's tally (puzzle index, moves, tries) lives in Recess.store(`run:<key>`) until the act
  ends, so Restart and reload never clear it. After an act is finished once, replays are "Encore" runs: same puzzles in
  the same order, a game-owned Encore card at the end ("You already finished this act with 2 stars. Encores are for
  fun."), and Recess.win is not called again.

**Today's puzzle.** `const r = Recess.daily(); index = Math.floor(r() * 45)` into the 45 puzzles (all kinds), the same
for everyone that day. One-puzzle level: score = moves made, stars 3/2/1 as above. First run counts the same way;
replays get the Encore card, and so does a later day that draws a puzzle already played as today's puzzle.

## Screens and controls

**1366x768 (Chromebook).** Shell bar on top (about 54 px). Below it the stage fills the page: the painted proscenium
behind, the board centered, 600x600 px (75 px squares, coordinates a to h and 1 to 8 in small ink type on the board
edge). Left wing (240 px): the opponent's puppet card (painted portrait, name, "thinking" state) or "Black" in friend
mode, and the opponent's fallen pieces row. Right wing (240 px): your fallen pieces row, the prompt box (two lines,
#fff4e0 on floor), then buttons: Playbill, Clue (puzzles only), Flip, Hints (on/off), and in friend mode the "Turn the
board each move" switch. All of it above the fold.

**390x844 (phone portrait).** Shell bar collapses to icons (the shell does this under 760 px). Then: opponent strip
(puppet head 40 px, name, fallen pieces), the board at 374x374 (46.75 px squares, above the 44 px tap target), your
fallen pieces strip, the prompt box, a row of 44 px buttons (Playbill, Hints, Flip, and Clue in puzzles; the "Turn the
board each move" switch moves into the playbill on phones). The
curtains shrink to a 16 px painted edge on each side and the valance to a 28 px band; the floor shows under the board.

**Pointer and touch.** Tap a piece then a square, or drag it (pointer events, so mouse and touch share code; a drag
under 6 px counts as a tap). Tap the selected piece again to put it down. Tap a different own piece to switch.

**Keyboard.** The board is a grid of 64 buttons with roving tabindex, each named "e2, white pawn" or "e4, empty".
Arrows move the cursor (gold square outline), Enter or Space picks up and puts down, Escape cancels. Promotion fan:
Left and Right or 1 to 4 (Queen, Rook, Bishop, Knight), Enter to choose. Game keys avoid the shell's U, R, M, S: H
toggles Hints, F flips, C is Clue, P opens the Playbill. Ctrl+Z is the shell's Undo.

**Hints** (legal-move dots, on by default, saved with Recess.store('hints')): a 22 percent-of-square line-color dot
with an ivory ring on each empty legal square, a ring on each capturable piece, castling shown on the king's two-square
target. Hints never show which move is best; they are allowed in puzzles and cost nothing.

**Undo and Restart by mode.**

| Mode | Undo | Restart |
|---|---|---|
| Computer | Takes back your last move and the computer's reply (if the computer has moved). Counts one takeback. Live after a loss too; off after a win. | New game, same puppet and side. |
| Friend | Takes back one half-move. Unlimited. After a finished game it reopens it. | New game. |
| Puzzle | Takes back to the last solved step inside the puzzle (only after a step of a mate in two or win a piece). Never lowers the tally. | This puzzle from its first position; the act's tally stays. |
| Today's puzzle | As Puzzle. | As Puzzle. |

Recess.canUndo is true whenever the rule above has something to take back.

## Motion and sound

| Event | Motion (Recess.calm: off) | Calm version | Sound |
|---|---|---|---|
| New game | Curtains (two painted wing panels in CSS) sweep in to center and back out, 500 ms | Fade 150 ms | game layer: soft "whoosh", band-passed noise sweep 400 to 1200 Hz, 0.35 s |
| Pick up | Lift 6 px, tilt 3 deg, shadow lengthens, dots bloom (scale 0 to 1, 120 ms) | Gold rim and dots only | game layer: paper rustle, high-passed noise above 3 kHz, 0.06 s, volume .05 |
| Move | Slide along a shallow arc, 180 ms; knights hop a higher arc | Instant, 120 ms crossfade | Recess.play('place') |
| Capture | Taken piece folds flat backwards (rotateX to 85 deg, 200 ms) then slides to its wing row (300 ms); taker lands | Taken piece appears flat in the wing row | Recess.play('capture'), then Recess.play('slide') as it leaves |
| Castling | King slides, then rook hops over, 180 ms each | Both at once | 'place' twice, 120 ms apart |
| Promotion | Pawn spins on its vertical axis like a turned card (rotateY 180 deg, 300 ms) and shows the new piece | Swap at once | Recess.play('pop') |
| Check | King shudders (3 px, 3 times, 240 ms); red halo fades in | Static halo and "Check!" | game layer: small bell, sines 880 and 1320 Hz, 0.3 s, volume .08 |
| Illegal move | Piece springs back with a small overshoot | Back at once | Recess.play('nope') |
| Computer thinking | Puppet portrait bobs gently | Text "thinking..." | none |
| Checkmate (you win) | Spotlight narrows on the mated king, it tips over (rotate 80 deg), then Recess.win (card, confetti) | King lies down at once, card | Recess.play('win') via Recess.win |
| Checkmate (you lose) or draw | Spotlight dims to a warm half light; result card | Same without the dim animation | game layer: two soft low notes (196 then 165 Hz sine, .2 s each), never a buzzer |
| Puzzle step solved | Gold sparkle on the target square | Gold outline | Recess.play('pop') |

Sound is one tap away (shell Sound button, M). The game layer uses the shell's AudioContext pattern: create its own
nodes only when Recess.sound is true, after the first pointerdown.

## Content

### The computer opponent (exact design)

Owner decision (Cory, 2026-11-08): the top puppet plays at about **2250 Elo**, the gentle bottom stays, and the seven
puppets sit on even steps of about 300 Elo. Kids never see a number; grown-ups get one line in notes.md.

One engine serves all seven puppets, in a Web Worker built from a Blob inside the file (so the stage never freezes),
offline, written from the rules above. The same move generator serves the rules, hints and the engine. Build it as a
0x88 board (or 10x12 mailbox) with make and unmake (no board copies in the search), incremental Zobrist hashing (two
32-bit halves: one indexes the table, the other verifies) and incremental material and piece-square sums. The builder
must run perft on the five positions under "Sources" and match every count before anything else. Typed arrays
everywhere in the hot path; no objects allocated per node. Aim for at least 1,000,000 nodes a second on a desktop.

**Search** (every puppet uses the same search; weaker puppets are made weaker only by the puppet table below):
- **Iterative deepening** from depth 1, with **aspiration windows** from depth 5 (start at +/- 25 cp around the last
  score, widen 4x on a fail, then full window).
- **Negamax alpha-beta with PVS** (principal variation search: every move after the first gets a null window first,
  then a full re-search if it lands inside the window).
- **Transposition table**: 2^21 entries in typed arrays (verify key, best move, score, depth, bound, age), about 28 MB
  of memory at run time, nothing in the file. Mate scores are stored relative to the node and adjusted by ply.
- **Null-move pruning**: not in check, not a PV node, depth at least 3, side to move has a knight, bishop, rook or
  queen, static eval at least beta. Reduction R = 3 + floor(depth / 6); a fail-high returns beta. At depth 10 and up,
  verify with a reduced normal search (zugzwang guard).
- **Late move reductions**: from the 4th move at PV nodes and the 3rd elsewhere, depth at least 3, quiet, not a killer,
  not in check, not giving check. Reduction from a precomputed table `floor(0.75 + ln(depth) * ln(moveIndex) / 2.25)`,
  one less at PV nodes and for moves with a high history score; re-search at full depth if it beats alpha.
- **Move ordering**: table move, then winning and even captures by MVV-LVA (captures that lose material by SEE go after
  the quiet moves), promotions, two **killer moves** per ply, a counter-move, then quiet moves by **history score**
  (butterfly table, bonus depth squared on a cutoff, a malus for quiets tried before it, halved before each new search).
- **Quiescence**: captures and queen promotions (all moves when in check), stand pat on the static eval, delta pruning,
  and skip captures that lose material by SEE.
- **Extensions and smaller prunings**: check extension (+1 ply); reverse futility pruning at depth 1 to 6 (return when
  static eval minus 90 x depth is at least beta); futility pruning of quiet moves at depth 1 to 2; late move pruning of
  quiet moves past a count that grows with depth. None of these at PV nodes or when in check.
- **Draws**: a repeated position (against game history or inside the search) or the 100th half-move scores 0; mate
  scores are 100000 minus ply, so a nearer mate is preferred.
- **Stopping**: the search stops at the puppet's node budget or its time limit, whichever comes first, checking the
  clock every 2,048 nodes. When a stop cuts an iteration short, play the best move of the last finished iteration, or
  of the cut iteration only if its first move (the old best) finished and another finished move beat it. Never mix
  scores from two depths.

**Evaluation** (tapered between middlegame and endgame by a phase count: N and B 1, R 2, Q 4, 24 = full middlegame;
every term has a middlegame and an endgame weight, written mg/eg). These are starting weights; the builder may tune
them (for example Texel tuning on positions from engine self-play) as long as the calibration below passes:
- **Material**: mg P 82, N 337, B 365, R 477, Q 1025; eg P 94, N 281, B 297, R 512, Q 936.
- **Piece-square tables**: the tables below are the middlegame set (White's view, index 0 = a1, rank by rank; Black
  reads them mirrored by rank). The endgame uses the same tables at half weight, except the king, which uses a
  centralizing table (14 - 4 x king-distance to the nearest of d4, e4, d5, e5).
```
P: 0,0,0,0,0,0,0,0, 0,0,0,-10,-10,0,0,0, 2,2,4,6,6,4,2,2, 4,4,8,20,20,8,4,4, 6,6,12,24,24,12,6,6,
   12,12,18,28,28,18,12,12, 40,40,40,40,40,40,40,40, 0,0,0,0,0,0,0,0
N: -40,-25,-20,-20,-20,-20,-25,-40, -25,-10,0,5,5,0,-10,-25, -20,5,10,12,12,10,5,-20, -20,0,12,18,18,12,0,-20,
   -20,5,12,18,18,12,5,-20, -20,0,10,12,12,10,0,-20, -25,-10,0,0,0,0,-10,-25, -40,-25,-20,-20,-20,-20,-25,-40
B: -15,-10,-10,-10,-10,-10,-10,-15, -10,8,0,4,4,0,8,-10, -10,6,8,8,8,8,6,-10, -10,0,8,12,12,8,0,-10,
   -10,4,8,12,12,8,4,-10, -10,0,6,8,8,6,0,-10, -10,0,0,0,0,0,0,-10, -15,-10,-10,-10,-10,-10,-10,-15
R: 0,0,4,8,8,4,0,0, then -4,0,0,0,0,0,0,-4 for ranks 2 to 6, 10 x8 on rank 7, 0 x8 on rank 8
Q: -10,-5,-5,0,0,-5,-5,-10, -5,0,0,0,0,0,0,-5, then -5,0,4,4,4,4,0,-5 for ranks 3 to 6, -5,0,0,0,0,0,0,-5,
   -10,-5,-5,0,0,-5,-5,-10
K: 10,20,15,0,0,5,20,10, 5,5,-5,-10,-10,-5,5,5, -15 x8 on rank 3, -25 x8 on ranks 4 to 8
```
- **Mobility**: per piece, squares attacked that hold no own piece and are not attacked by an enemy pawn, minus a
  baseline (N 4, B 7, R 7, Q 14); weight per square mg/eg: N 4/4, B 5/5, R 2/4, Q 1/2.
- **King safety** (middlegame only): pawn shield on the three files around the king (missing pawn -15, pawn pushed two
  squares -8, open file next to the king -20); attack units for each enemy piece attacking the king zone (the king's
  square, the squares next to it and the three in front): N 2, B 2, R 3, Q 5, counted only when at least two pieces
  attack; the penalty grows with the square of the units (units squared x 2 cp), capped at 500 cp.
- **Pawn structure**: passed pawn by rank (ranks 3 to 7) mg 5, 10, 15, 25, 40 and eg 10, 20, 35, 60, 100, plus a
  free-path bonus when the squares ahead are empty, and in the endgame 5 x (enemy king distance minus own king
  distance) to the square in front; doubled -12/-20; isolated -10/-12; backward -8/-10; connected or side by side +5/+7.
- **Pieces**: bishop pair +30/+50; rook on an open file +20/+10, half-open +10/+5; rook or queen on the 7th rank with
  the enemy king on the 8th +20/+30; knight outpost (protected by a pawn, no enemy pawn can ever attack it) +15/+10.
- **Tempo** +10 for the side to move; drawish endings (no pawns and a material edge under a rook) scaled to a quarter.

**Puppets.** Weaker puppets get a depth limit, a smaller node budget, score noise and occasional random moves. Raven
and Lion get no handicap at all, only their node budget.

| Puppet | Target Elo | Depth limit | Node budget | Think (desktop), cap | Blunder | Noise (cp) | Opening margin | Plays like |
|---|---|---|---|---|---|---|---|---|
| Mouse | 450 | 1 | 5,000 | 0.5 s, cap 1 s | 30% | 120 | 0 | Just learned how the pieces move. Grabs a free piece when it sees one, misses most threats, often leaves pieces hanging. |
| Rabbit | 750 | 2 | 20,000 | 0.5 s, cap 1 s | 15% | 70 | 0 | Guards its pieces and trades fairly, still falls for two-move tricks like forks. |
| Fox | 1050 | 3 | 60,000 | 0.7 s, cap 1.5 s | 6% | 40 | 0 | A steady beginner: sees loose pieces and simple forks, rarely hangs a piece, can be out-planned. |
| Owl | 1350 | 4 | 150,000 | 1 s, cap 2 s | 2% | 20 | 20 | A careful casual player. Looks a few moves ahead and punishes big mistakes, still slips now and then. |
| Badger | 1650 | 6 | 500,000 | 1.5 s, cap 3 s | 0.5% | 10 | 20 | A solid tournament player. Never hangs a piece, sees two-move tactics both ways, plays sensible endgames. |
| Raven | 1950 | none | 2,000,000 | 2.5 s, cap 5 s | 0 | 0 | 15 | A sharp club player. Finds deep combinations and punishes loose play. |
| Lion | 2250 | none | 6,000,000 | 5 s, cap 8 s | 0 | 0 | 10 | The top of the ladder: plays like a strong tournament player and gives grown-up club players a real fight. |

These are starting values. The calibration below sets the final depth limits, node budgets, noise and blunder rates
so each puppet lands on its target; the builder records the final table in the report. Raven and Lion are tuned by
their node budget alone; the lower five by depth, noise and blunder rate.

**Same strength on every machine.** The node budget, not the clock, sets a puppet's strength. On load the worker runs
a 300 ms speed test (a fixed search from the start position) and keeps nodes per second in Recess.store. A puppet
whose budget would take longer than its desktop think time on this machine keeps searching up to its cap, then stops.
On a desktop at 1,000,000 nodes a second Lion spends about 5 s a move; on a Chromebook about 3 times slower it uses its
full 8 s cap and reaches about half its budget, which costs roughly 50 to 80 Elo. The calibration measures Lion at
half budget, and notes.md says it plainly ("about 2250 on a fast computer, a little less on a slow one").

**Root and choosing a move:** with probability `blunder` play a uniformly random legal move. Otherwise, for puppets
with noise or an opening margin, search the root with the window lowered by a margin (twice the noise, or the opening
margin), so every move within that margin of the best gets an exact score; add uniform noise in [-noise, +noise] to
non-mate scores and play the highest. Opening variety for the top four: in the first 8 half-moves of the game, pick at
random among moves within the opening margin of the best. A forced mate is always played. Two traps the first
prototype fell into, both required fixes: (1) a root move that fails low returns only an upper bound that can equal
the window edge exactly, so mark it strictly below the window (subtract 0.5) or a move that loses to mate in one gets
drawn as an "equal" opening choice; (2) when a stop cuts an iteration short, choose only among moves finished at that
depth (the old best is searched first), never mix in scores from the shallower iteration.

Every puppet waits at least 500 ms before moving (it "thinks"). The top three show the thinking bar (depth reached).
While a puppet thinks, Undo, Sound, Motion and the Playbill stay live; Undo or leaving stops the search at once.

**Where this started.** A 15 KB JavaScript prototype of the earlier, smaller design (scratchpad `eng.js`, `sim.js`,
plain alpha-beta, PVS, null move and LMR on the top level only, about 680,000 nodes a second in Node) already put its
seven puppets in strength order: each beat the one below it in at least 16 of 20 games (top level over the next 22 to
0 with 2 draws). The design above keeps that shape, adds the full search and evaluation to every level, and replaces
"in order" with measured Elo.

**Calibration** (the builder runs it at dev time; Stockfish is a test tool only and never ships):
- **Tool**: a desktop Stockfish (version recorded) over UCI with `UCI_LimitStrength true` and `UCI_Elo` set. Our engine
  runs headless in Node from the file's own engine code, unchanged. A small harness plays the matches, colors
  alternating, from 50 balanced opening positions (4 to 8 moves into common openings, each played once with each
  color), adjudicating a win when both engines agree a side is ahead by more than 1000 cp for 5 moves, and a draw after
  150 moves each.
- **Time**: each puppet plays at its own node budget; Stockfish plays at a fixed time per move equal to the puppet's
  measured average think time on the same machine (record the time used next to each result).
- **Anchors**: Stockfish's `UCI_Elo` floor is 1320, so it calibrates Owl and up directly: Owl against 1320 and 1500;
  Badger against 1500 and 1800; Raven against 1800, 2000 and 2250; Lion against 2000, 2250 and 2400. Mouse, Rabbit and
  Fox are placed by a chain: each plays the puppet above it, and its Elo is that puppet's estimate minus the
  head-to-head difference.
- **Games**: at least 40 games per anchor pairing (at least 120 for Lion). Each puppet's Elo is the maximum likelihood
  estimate across its anchors (logistic model, draws as half), with a 95% interval; 120 games give about +/- 60.
- **Pass mark**: Lion's estimate lands within 2250 +/- 100. Every other puppet lands within 150 of its target, and each
  still beats the one below it in a direct 20-game match. Lion at half its node budget is also measured and reported.
- **Report**: a table in codex-report.md, one row per puppet: target, final settings, games, score per anchor,
  estimate and interval, average and longest think time on the desktop, and the estimated Chromebook time.

### Puzzle set (45 Lichess puzzles, ships in the file)

Selection (run 2026-11-08 against the Lichess puzzle set as mirrored by Lichess on Hugging Face, `Lichess/chess-puzzles`,
the same CC0 data as database.lichess.org, 6,157,341 puzzles): rows with Popularity at least 90 and RatingDeviation at
most 80, in four rating bands (400 to 799, 800 to 1099, 1100 to 1399, and 1400 to 1699 as a spare that was not needed), the
300 most-played rows per band; of those, the 14 most-played mate-in-two rows and 24 most-played win-a-piece rows per
band, and all 79 mate-in-one rows, were verified (the checks are slow in plain Python). Kinds: themes `mateIn1` with one solving move; `mateIn2` with three solution moves; Win a
piece = no mate theme, two solution moves, theme `crushing` or `advantage` and one of fork, hangingPiece, pin, skewer,
discoveredAttack, trappedPiece. Then verified and filtered (Sources): five per act, the five most-played that passed,
shown gentlest first. Acts for Mate in two and Win a piece use the bands 400 to 799, 800 to 1099, 1100 to 1399. Popular
mate-in-one puzzles all sit between 639 and 1098 (all 79 found), so its acts split at under 760, 760 to 999, and 1000
up. Ratings run 639 to 1392 in all. Two puzzles test edge rules on purpose: OxJo0 has two mating moves (g6h6 and
g6h5, both accepted) and ZrgCo needs promotion to a knight (e7e8n), so the promotion fan is part of the solution.

Format: `[act, lichessId, rating, fen, moves, clue]` (act `m1-1` is level key `p-m1-1`; clue is the Win a piece
theme word). `fen` is the position before the opponent's lead-in move (Lichess
format); `moves` is UCI, the first is the lead-in the game plays for the opponent, then solver, reply, solver.

```
const PUZZLES = [
['m1-1', 'yd6eW', 639, '3r2k1/pb4p1/4pr1p/1B1qNp1n/3P3P/P7/3Q1PP1/2R1R1K1 w - - 7 26', 'b5c4 d5g2', ''],
['m1-1', 'BKLTK', 687, 'r2r2k1/pb3ppp/1p2p3/3q4/1P1b1P2/P4N2/4B1PP/2RQ1RK1 w - - 0 17', 'f3d4 d5g2', ''],
['m1-1', 'FPBtR', 693, 'r4rk1/ppp2ppp/1bn5/4p3/3qP3/1PN3Pb/PBPN1P1P/R2QK2R w KQ - 3 12', 'c3a4 d4f2', ''],
['m1-1', 'Oo2Yb', 736, '6k1/1pp2ppp/6r1/2Pp4/pP1Br1P1/P3nPPK/8/R1R5 w - - 0 28', 'f3e4 g6h6', ''],
['m1-1', '9Bsuq', 755, 'r2q1b1r/ppp1kBp1/2n2n1p/3p1P2/8/4Q3/PPP2PPP/RNB1K2R b KQ - 1 11', 'e7f7 e3e6', ''],
['m1-2', '6FooS', 865, '2k1R3/ppb3qp/2p5/2P2p2/PPQr1p2/5P2/5NPP/5K2 b - - 1 25', 'c8d7 c4e6', ''],
['m1-2', 'WS1ZL', 922, '7r/p4Rk1/2p2Rp1/4p3/4P1Pr/2qn2Q1/P1P1K1P1/8 b - - 0 29', 'g7h6 g3h4', ''],
['m1-2', 'OxJo0', 925, '1Q6/6bk/3P2q1/3Qp3/4Np2/5P2/3R2bK/2r5 w - - 1 48', 'd2g2 g6h6', ''],
['m1-2', 'LKlGq', 969, 'r1bq1r2/1p3pp1/p1nbN1k1/4p3/3P2Q1/8/PP3PPP/R1B2RK1 b - - 1 15', 'g6h7 g4g7', ''],
['m1-2', 'COr8l', 986, '8/p6p/6bk/1p5p/4PQ2/2KR4/2P5/6q1 b - - 3 33', 'g1g5 f4f8', ''],
['m1-3', 'ITD5U', 1037, 'r3r1k1/p1pp1p1p/1pn3p1/3N4/2P5/5q2/PP1QBP1P/R3K2R w KQ - 0 15', 'd5c7 f3h1', ''],
['m1-3', 'iziys', 1068, 'r4k1r/pp1b1p2/2pP1n1p/2b3p1/NqQ4B/5P2/PPP2P1P/2K1RB1R w - - 5 16', 'a4c5 b4e1', ''],
['m1-3', 'X74cN', 1084, 'r1b2Qnr/ppk2N1p/3pp1p1/4q3/4P3/8/P1P2PPP/5RK1 b - - 5 19', 'e5f6 f8d6', ''],
['m1-3', 'cVJhU', 1098, '2kr1q1r/pbpp2pp/1pn2P2/2bN2B1/2B5/6Q1/PPP2PPP/R4RK1 b - - 0 14', 'g7f6 g3c7', ''],
['m1-3', 'XkzBv', 1098, 'r2q1rk1/p1p2ppp/2B5/3QP3/2b1n3/8/PP3bPP/RN3K1R w - - 0 14', 'd5c4 d8d1', ''],
['m2-1', 'jqG75', 734, 'rn4k1/p4ppp/b7/3P4/4qBn1/7P/PP2QPP1/2R1KB1R b K - 1 20', 'a6e2 c1c8 e4e8 c8e8', ''],
['m2-1', '97cz2', 754, '2rk4/1b2bppp/p2p1n2/3Pp1B1/B3P3/P6Q/1P3PPP/6K1 w - - 8 24', 'g5f6 c8c1 a4d1 c1d1', ''],
['m2-1', 'bkWnP', 756, 'r2r2k1/p4ppp/8/2QR4/1PP3q1/P7/5PPP/R5K1 w - - 5 23', 'a1d1 g4d1 d5d1 d8d1', ''],
['m2-1', 'F8NkT', 784, 'rnbq1rk1/4bpp1/2p1p2p/p7/1p1PN3/2PQ4/PPB1NPPP/R4RK1 b - - 1 15', 'c8a6 e4f6 e7f6 d3h7', ''],
['m2-1', 'pdf76', 787, '2r3k1/4ppbp/1Q4p1/1P2p3/8/1qN1B3/5PPP/2R3K1 w - - 1 22', 'c3e2 c8c1 e2c1 b3d1', ''],
['m2-2', 'su5D2', 982, 'r4rk1/pp3pp1/3p4/3Nn3/2P1P3/6P1/PP2BR2/4K3 b - - 0 27', 'a8c8 d5e7 g8h7 f2h2', ''],
['m2-2', 'popOX', 983, '4r1k1/2R2ppp/3n4/8/8/4BQ2/5PPP/1q4K1 w - - 1 24', 'c7c1 b1c1 e3c1 e8e1', ''],
['m2-2', 'hLvdJ', 1038, 'r4rk1/1b1p1pp1/p1n1p2p/qp2P3/4N1nP/B2Q4/P1B1KPP1/R6R b - - 6 17', 'g4e5 e4f6 g7f6 d3h7', ''],
['m2-2', '1JTIv', 1066, '5r1k/Q2R1n2/4qPp1/1p2p1P1/2p1P3/2P2B2/P5K1/8 b - - 0 42', 'f7g5 d7h7 g5h7 a7g7', ''],
['m2-2', '4KfY8', 1087, 'r2qk2r/4npbp/p1npp1pB/1pp5/2B1P1N1/3P4/PPPQ1PPP/1R3RK1 b kq - 1 17', 'g7h6 g4f6 e8f8 d2h6', ''],
['m2-3', 'MS7Mo', 1202, '4rrk1/5ppp/2Q5/3p4/8/1NPqp2P/PP1N2P1/R1BK3R w - - 0 21', 'b3c5 e3e2 d1e1 d3g3', ''],
['m2-3', '8tsRc', 1234, 'r4r1k/bp1pN1pp/4p3/p3q3/2P5/P5p1/1PQ1NP1P/3RKB1R w K - 2 20', 'h2g3 a7f2 e1d2 e5e3', ''],
['m2-3', 'ZrgCo', 1256, '8/p3P2R/1p1k4/2p2K1p/2P4r/1P6/P6p/8 b - - 0 52', 'h2h1q e7e8n d6c6 h7c7', ''],
['m2-3', 'QtZPh', 1303, 'r2qkbr1/1ppn1pp1/p2p1nNp/4pB2/2Q2P2/7P/PPP3P1/R1B2RK1 b q - 0 16', 'f7g6 f5g6 e8e7 c4f7', ''],
['m2-3', 'c4h9d', 1392, '8/6k1/5bpp/pp6/2p1pPKP/P1P1r3/1P1qQ3/4R1N1 w - - 0 39', 'e2e3 d2g2 e3g3 h6h5', ''],
['mat-1', 'w8biZ', 743, 'r4rk1/1pp1bppp/1q6/p2Np3/PnP2n2/BP1P1N1b/4BPP1/R2Q1RK1 b - - 1 16', 'b6g6 d5e7 g8h8 e7g6', 'fork'],
['mat-1', 'mDxnD', 760, '3br3/1p3pkp/pnr3p1/n1p5/P3P1N1/2P1BP2/4B1PP/1R1R2K1 w - - 8 26', 'e3c5 c6c5 d1d8 e8d8', 'loose piece'],
['mat-1', 'ugKOP', 773, 'r3r1k1/6p1/p4p2/2pqbP1p/3pN2P/P4Q2/1PP3P1/3R1R1K b - - 1 22', 'c5c4 e4f6 e5f6 f3d5', 'discovered attack'],
['mat-1', '8BvWL', 782, '4r1k1/1ppq1ppp/p1n5/2Pp4/1P1r4/P1RB3P/3Q1PP1/3R2K1 b - - 1 24', 'c6e5 d3h7 g8h7 d2d4', 'discovered attack'],
['mat-1', 'tHNM3', 789, '8/6pp/1R6/5pk1/6P1/2n1K3/P7/8 w - - 3 46', 'g4f5 c3d5 e3d4 d5b6', 'fork'],
['mat-2', 'RRRzQ', 966, 'r3kb1r/1pp2pp1/p2pbn2/6Bp/1P1qP3/P2B3P/2P2PP1/R2Q1RK1 b kq - 3 13', 'd6d5 d3b5 a6b5 d1d4', 'discovered attack'],
['mat-2', 'Xak5l', 1041, 'r1bqk2r/pppp1ppp/5nn1/3Pp1B1/1bP1P3/2N2N2/PP3PPP/R2QKB1R b KQkq - 6 7', 'd7d6 d1a4 c8d7 a4b4', 'fork'],
['mat-2', 'P88XH', 1057, 'r3k1nr/ppp2Bpp/2nq4/8/Nb2p1b1/1P2PN2/PB1P1PPP/R2Q1RK1 b kq - 0 11', 'e8f7 f3g5 f7e8 d1g4', 'discovered attack'],
['mat-2', 'qMMfE', 1086, '8/2r5/p1P4p/4k3/1P5r/P5K1/6Bp/3R4 b - - 0 47', 'h4h5 d1d5 e5e6 d5h5', 'skewer'],
['mat-2', 'Bv8Tk', 1095, 'r1b1Rbk1/ppB2ppp/2p5/8/P2P4/8/1P1N1PPP/6K1 b - - 0 18', 'f7f6 c7d6 g8f7 e8f8', 'pin'],
['mat-3', 'VQjbl', 1264, '1kr5/pp3pp1/4p1p1/1NqnP1P1/7P/P4Q2/1PP4R/2K5 w - - 5 29', 'b5d6 c5g1 f3d1 g1h2', 'fork'],
['mat-3', 'ZuAAs', 1345, 'rn2k2r/p3pp1p/2p2npb/q4bN1/3P4/N1PBP3/P1Q2PPP/R1B1K2R w KQkq - 4 12', 'a3c4 f5d3 c2d3 a5g5', 'discovered attack'],
['mat-3', 'LDMBw', 1349, '4rrk1/pp1q1ppp/2pp1b2/4nP2/4PB2/1BQ4P/PPP2P1K/3R1R2 w - - 5 20', 'f1g1 e5g4 g1g4 f6c3', 'discovered attack'],
['mat-3', 'PEWkx', 1377, '1rb2rk1/4ppbp/5np1/2p1P3/1n1q4/2NP3P/1P2B1PN/R1BQ1R1K b - - 2 16', 'd4e5 c1f4 e5e6 f4b8', 'skewer'],
['mat-3', 'Q2ZXU', 1388, 'r1b3k1/1pNnqrpp/p7/4P3/4p3/1Q2P3/PP3PPP/R4RK1 b - - 2 17', 'a8b8 e5e6 d7e5 e6f7', 'fork'],
];
```

Verification log (Python, from the Lichess source FEN; "gain" in centipawns of material: the line's actual gain, the
search's value of the stated first move, the best other first move, and the second move's margin over the next best):

```
m1-1 yd6eW Black to play: mating moves: 1 (d5g2)
m1-1 BKLTK Black to play: mating moves: 1 (d5g2)
m1-1 FPBtR Black to play: mating moves: 1 (d4f2)
m1-1 Oo2Yb Black to play: mating moves: 1 (g6h6)
m1-1 9Bsuq White to play: mating moves: 1 (e3e6)
m1-2 6FooS White to play: mating moves: 1 (c4e6)
m1-2 WS1ZL White to play: mating moves: 1 (g3h4)
m1-2 OxJo0 Black to play: mating moves: 2 (g6h6 g6h5)
m1-2 LKlGq White to play: mating moves: 1 (g4g7)
m1-2 COr8l White to play: mating moves: 1 (f4f8)
m1-3 ITD5U Black to play: mating moves: 1 (f3h1)
m1-3 iziys Black to play: mating moves: 1 (b4e1)
m1-3 X74cN White to play: mating moves: 1 (f8d6)
m1-3 cVJhU White to play: mating moves: 1 (g3c7)
m1-3 XkzBv Black to play: mating moves: 1 (d8d1)
m2-1 jqG75 White to play: keys: ['c1c8']; defences after key: 1; mates after stated defence: 1
m2-1 97cz2 Black to play: keys: ['c8c1']; defences after key: 1; mates after stated defence: 1
m2-1 bkWnP Black to play: keys: ['g4d1']; defences after key: 1; mates after stated defence: 1
m2-1 F8NkT White to play: keys: ['e4f6']; defences after key: 3; mates after stated defence: 1
m2-1 pdf76 Black to play: keys: ['c8c1']; defences after key: 2; mates after stated defence: 1
m2-2 su5D2 White to play: keys: ['d5e7']; defences after key: 2; mates after stated defence: 1
m2-2 popOX Black to play: keys: ['b1c1']; defences after key: 2; mates after stated defence: 1
m2-2 hLvdJ White to play: keys: ['e4f6']; defences after key: 2; mates after stated defence: 1
m2-2 1JTIv White to play: keys: ['d7h7']; defences after key: 2; mates after stated defence: 1
m2-2 4KfY8 White to play: keys: ['g4f6']; defences after key: 1; mates after stated defence: 1
m2-3 MS7Mo Black to play: keys: ['e3e2']; defences after key: 1; mates after stated defence: 1
m2-3 8tsRc Black to play: keys: ['a7f2']; defences after key: 1; mates after stated defence: 1
m2-3 ZrgCo White to play: keys: ['e7e8n']; defences after key: 1; mates after stated defence: 1
m2-3 QtZPh White to play: keys: ['f5g6']; defences after key: 1; mates after stated defence: 1
m2-3 c4h9d Black to play: keys: ['d2g2']; defences after key: 1; mates after stated defence: 1
mat-1 w8biZ White to play: gain 1200, search gain 1200, best other 0, move2 margin 600
mat-1 mDxnD Black to play: gain 500, search gain 300, best other 100, move2 margin 300
mat-1 ugKOP White to play: gain 700, search gain 700, best other 100, move2 margin 900
mat-1 8BvWL White to play: gain 300, search gain 300, best other 0, move2 margin 500
mat-1 tHNM3 Black to play: gain 500, search gain 500, best other 100, move2 margin 400
mat-2 RRRzQ White to play: gain 600, search gain 500, best other 100, move2 margin 800
mat-2 Xak5l White to play: gain 300, search gain 300, best other 0, move2 margin 300
mat-2 P88XH White to play: gain 300, search gain 300, best other 0, move2 margin 300
mat-2 qMMfE White to play: gain 500, search gain 500, best other 0, move2 margin 600
mat-2 Bv8Tk White to play: gain 300, search gain 300, best other 0, move2 margin 300
mat-3 VQjbl Black to play: gain 500, search gain 300, best other -100, move2 margin 300
mat-3 ZuAAs Black to play: gain 300, search gain 300, best other 0, move2 margin 300
mat-3 LDMBw Black to play: gain 600, search gain 400, best other 100, move2 margin 500
mat-3 PEWkx White to play: gain 500, search gain 500, best other 0, move2 margin 400
mat-3 Q2ZXU White to play: gain 500, search gain 300, best other 0, move2 margin 400
```

## Sources and licences

| Source | Checked at | Licence (quoted) | Ships |
|---|---|---|---|
| Lichess puzzle database | database.lichess.org (puzzle section), read 2026-11-08 | "Database exports are released under the Creative Commons CC0 license." and "Use them for research, commercial purpose, publication, anything you like. You can download, modify and redistribute them, without asking for permission." | 45 puzzles: ids, FEN, UCI moves, rating |
| Same data, queried | huggingface.co/datasets/Lichess/chess-puzzles (author: Lichess), tagged `license:cc0-1.0` | CC0 1.0 | (query route only) |
| Chess rules | FIDE Laws of Chess (public domain game; we write our own wording) | rules are not copyrightable | our own text |
| Piece shapes | Our own SVG paths in the Staunton family (a public domain design from 1849) | ours | Painted sprites (our own) |
| Engine, tables, art, sounds | Written for this game | ours | in the file |

Lichess's page states the puzzle format: "FEN is the position before the opponent makes their move" and "The second
move is the beginning of the solution", moves in UCI. The game credits it on the playbill: "Puzzles from the Lichess
puzzle database (CC0). Thank you, Lichess." (a credit, not a logo or Lichess's look).

**What I ran (Python).** python-chess is not installed, so I wrote a legal-move checker (`mini.py`) and proved it
with perft against the published counts: start position depth 1 to 3: 20, 400, 8902; "Kiwipete" 48, 2039, 97862;
position 3 to depth 4: 14, 191, 2812, 43238 (tests the en passant pin); position 4: 6, 264, 9467; position 5: 44, 1486,
62379. All matched. The JavaScript engine prototype (`eng.js`) matched the same positions one level deeper: 20, 400,
8902, 197281; 48, 2039, 97862, 4085603; 14, 191, 2812, 43238, 674624; 6, 264, 9467, 422333; 44, 1486, 62379, 2103487.
The five perft positions (standard test FENs):

```
rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq - 0 1
8/2p5/3p4/KP5r/1R3p1k/8/4P1P1/8 w - - 0 1
r3k2r/Pppp1ppp/1b3nbN/nP6/BBP1P3/q4N2/Pp1P2PP/R2Q1RK1 w kq - 0 1
rnbq1k1r/pp1Pbppp/2p5/8/2B5/8/PPP1NnPP/RNBQK2R w KQ - 1 8
```
 Selection results: 180 rows verified, every Lichess line legal and every stated mate a mate; 9 of
96 win-a-piece rows failed the one-best-move test and were dropped; all 56 mate-in-two rows checked had no mate in one. Then for every
shipped puzzle (`pick.py`, an independent second pass): replayed the Lichess line from its source FEN with legality checks;
mate in one: the stated move mates, and listed every mating move (all are accepted by the game); mate in two: no mate in
one exists, the stated first move forces mate against every defence, it is the only first move that does, and the
stated finish mates; win a piece: a material search (3 full plies, solver-reply-solver, then captures only up to 4
more plies) finds the stated first move at least 2 pawns up and every other first move at least 1 pawn worse, and the stated second move
beats every other second move by at least a pawn (2 full plies plus captures). Contrast ratios: WCAG formula on the hex values above. Engine: the ladder games
above (`sim.js`; an earlier Python prototype, `engine_sim.py`, agreed for the first four). Fastest wins (fool's mate f3 e5 g4 Qh4, and e4 f6 d4 g5 Qh5) replayed as mate.
Scratch scripts live in the session scratchpad only; nothing else ships.

**Dev-time test tool, not shipped:** Stockfish (stockfishchess.org, GPL v3) is used only on the builder's machine to
calibrate the puppets. No Stockfish code, weights or output tables go into the file, so its licence places nothing on
the game. Record the version used in the report.

## Can it be beaten?

| Check | No-skill path | Closed how |
|---|---|---|
| Win vs computer (stars, score) | Random moves | Mouse beat a random mover in 18 of 20 prototype games (2 draws, no losses); random play does not win. |
| Win vs computer | Undo until the computer blunders | Every takeback costs stars (3 needs none, 2 allows three) and every taken-back move still adds to Moves. Raven and Lion never blunder on purpose (Badger at most 1 move in 200), so undo only buys a second try at your own move. |
| Win vs Owl to Lion | Replay a memorized winning game | The top four pick at random among near-equal moves for the first 8 half-moves, so games split early; after that they are deterministic for a given position, so a kid who reaches the same position again can repeat a win. That takes real chess (reaching it) and is left open. |
| Win vs Lion | Let another engine or app choose the moves | Cannot be closed on a device-only game; it only fills the player's own local board. Left open. |
| Win vs computer | A machine so slow the time cap weakens the top puppets | Strength is set by the node budget; on a slow device the time cap stops the search early, so a puppet plays a little weaker (Lion about 50 to 80 Elo at half budget, measured), never stronger. Accepted. |
| Win vs computer | Restart until Mouse falls for a fast trap | Setting a trap is real chess, and the computer's blunders are random, so fishing costs many games; the score floor is the same for everyone (2 moves as Black after the computer plays f3 and g4, 3 as White; both lines checked as mate in Python). Left open on purpose. |
| Puzzle act stars | Guess at random | A random move mates in one about 1 time in 35 (2.8 percent averaged over the 15 shipped puzzles, which have 16 to 51 legal moves each); each miss is a try, three tries plays the answer and caps the act at 2 or 1 star. |
| Puzzle act stars | Fail to see the answer, Restart, solve clean | Tally lives in Recess.store until the act ends; Restart and reload keep it. |
| Puzzle act stars | Replay a finished act from memory | Encore runs never call Recess.win, so stars and best stay from the first run. |
| Puzzle | Use Hints to find it | Hints show legal squares only, never the best one. |
| Puzzle | Undo a wrong try | Wrong tries spring back by themselves and stay counted; Undo never lowers the tally. |
| Win a piece | A second good move is rejected | Search check above: no shipped puzzle has another move within a pawn of the stated one; mates are always accepted. |
| Today's puzzle | Replay all day | First run counts; replays get the Encore card. |
| Today's puzzle | Change the device clock to farm stars | The level key is the puzzle id, not the date, so each of the 45 puzzles can earn daily stars once; a repeat is an Encore. |
| Initials board | Spam entries | The shell asks for initials only on a top 10 score from Recess.win; Encore runs and draws never call it; friend games never call it. |

## Not like

- **Go** (`go`): territory by surrounding, stones never move, ink-and-stone world. Chess is about one king and pieces
  that each move their own way, on a paper stage.
- **Checkers** (`checkers`): one kind of move (diagonal steps and forced jumps), neon arcade. Chess is many piece shapes,
  check and mate, warm theatre light.
- **Cargo Hold** (`sliding-blocks`): a solo route puzzle with no opponent. Chess always answers back.
- **Untangle** (`untangle`): drag points until no lines cross; spatial, solo, no turns.
- Classroom tools and Curiosities: `grep -ril chess tools/` finds no chess tool (the only hits are unrelated words).
  Nothing in Curio Class teaches chess, so there is no overlap to manage.

## Art list

Painted (WebP, embedded as data URIs, our own, no people):
Painted first (Cory, 2026-11-08; docs/agents/CODEX-RECESS.md, "Visually amazing"): everything a kid looks at is painted and placed exactly by code; this list is a floor, not a ceiling. Paint the look board (three hero frames) before writing game logic.

1. **Stage proscenium**, 1600x1000, about 160 KB: red velvet curtains gathered at both wings, scalloped valance with
   gold trim, warm spotlight from the left, dark wooden stage floor in the lower third, center left plain for the
   board. Desktop uses it whole; phone uses the left and right 140 px strips and the valance band (CSS crops of the same
   image, so one file).
2. **Puppet sheets**, 7 sheets of 640x320 (two 320x320 poses each), about 40 KB each: a paper-cutout Mouse, Rabbit,
   Fox, Owl, Badger, Raven and Lion on sticks, each in a little costume (Mouse in a stagehand cap, Rabbit with a bow
   tie, Fox in a cape, Owl with spectacles, Badger in a waistcoat with a pocket watch, Raven in a magician's top hat,
   Lion in a director's beret and long scarf), same side
   light, transparent background; left pose waiting, right pose "thinking" (eyes up, paw or wing at chin).
3. **Playbill paper**, 800x1100, about 60 KB: an old printed programme sheet, cream, with an empty ornamental border
   (text is set in code).

4. **Pieces**, 12 painted cut-paper sprites (K, Q, R, B, N, P for each side), each about 240x300 (twice their largest
   on-screen size), transparent, about 20 KB each: the Staunton-family silhouettes described under The world, as real
   card with an ink outline, a visible card edge and paper grain, lit from the viewer's left. White is ivory card,
   Black deep ink card with an ivory edge line. Silhouettes must tell apart at a glance at 40 px and in grayscale.
   Optional extras that make captures sing: a folded-flat frame for each piece (for the fold-and-slide), a paper
   confetti sheet for the win.
5. **Board card**, 1200x1200, about 150 KB: a printed paper chessboard with an ornamental border, laid flat, warm
   spotlight falling from the left, light and dark squares in the palette's board tones, painted to an exact 8x8 grid
   so code can place pieces square by square (the builder checks the grid lines against the painting).
6. **Cover**, `art/cover.webp`, 1200x750, about 120 KB, no text: the shelf box art, the stage at its most striking (a
   paper Lion puppet facing a Mouse across a lit board, curtains open).

Drawn in code (must stay exact, lit to match the painting): coordinates, legal-move dots, selection rings, check halo,
last-move tint (#ffd27a at 35%), focus cursor and hit areas; the drop shadow under each piece sprite (CSS, offset right
to match the light); curtain sweep panels; the promotion fan's layout (it shows the piece sprites); prompt box, wing
rows, buttons and cards.

**Size budget** (Recess cap 6 MB): painted art about 1.0 MB as WebP (stage 160, 7 puppet sheets x 40, playbill 60,
12 pieces x 20, board 150, cover 120, extras about 50), about 1.35 MB once base64; code about 155 KB: the engine about
45 to 60 KB unminified (move generator, search with every feature above, evaluation with its tables, the speed test and
the Worker glue; the earlier 15 KB prototype had about a third of the features), plus rules, UI, motion and sound about
95 KB; puzzle data 4 KB (measured on the block above); shell inlined 20 KB (kit/recess.js plus recess.css measured at
20,013 bytes). Total about 1.55 MB, well under the cap; more painting is welcome inside it. The builder reports the
measured engine and file size. The transposition table (about 28 MB), history tables and search stack are memory at
run time, not file size; nothing is precomputed into the file (no opening book, no endgame tables).

## notes.md

```
# Chess: a note for grown-ups

Chess is the classic look-ahead game. Every move asks the same question: "If I go here, what
can they do back?" That habit of picturing the next move, and the one after, is the thinking this game is built on.

What a child practises without being told:
- Planning a few steps ahead and checking a plan before acting.
- Seeing patterns: a fork (one piece attacks two), a pin, a back-rank mate.
- Spatial reasoning: lines, diagonals, the L of a knight, coordinates like e4.
- Losing kindly and trying again. A wrong move is never punished; the game shows what was off and puts the piece back.

How it plays:
- Play the computer: seven puppets on a ladder in even steps, from Mouse (just learned the moves) up to Lion, which
  plays at about 2250 on the Elo rating scale, the level of a strong tournament player (a little less on a slow
  computer). The ladder was measured against a standard chess engine. Children never see the numbers. Pick any of them; takebacks are allowed and cost a star.
- Play a friend on one device.
- Puzzles: short acts of five, mate in one, mate in two and win a piece, from the free Lichess puzzle database (CC0).
- Hints (dots on the squares a piece can reach) are on by default for younger players and can be switched off.

Draws are explained in plain words: stalemate, the same position three times, fifty moves with no capture or pawn
move, or not enough pieces left to checkmate.

Nothing leaves the device. There are no accounts, no ads and no chat. Initials on the score board are three letters
only. A good next step for a keen child is a local chess club or a school chess program.
```

## Done when

- [ ] perft from the start position and the four other positions in Sources matches every count to depth 4 (start
      197281, Kiwipete 4085603, position 3 to depth 5 674624, position 4 422333, position 5 2103487), from the game's
      own move generator.
- [ ] Castling works both sides for both colors and is refused (with the right kind line) after the king or that rook
      moved, through an attacked square, out of check and with b1 occupied.
- [ ] En passant works only on the next move, removes the right pawn, and is refused when it would expose the king on
      the rank.
- [ ] Promotion offers Queen, Rook, Bishop, Knight by tap and by keys 1 to 4; Escape puts the pawn back.
- [ ] Checkmate, stalemate, threefold, fifty-move and each insufficient-material case end the game with the right card
      and wording.
- [ ] Trying a pinned piece shows "That would leave your king in check..." with the attacker named and lined.
- [ ] Every puppet answers within its cap (Mouse and Rabbit 1 s, Fox 1.5 s, Owl 2 s, Badger 3 s, Raven 5 s, Lion 8 s)
      on a 1366x768 Chromebook, and the page (Undo, Sound, scrolling) stays responsive while any puppet thinks; Undo
      during a think stops the search at once.
- [ ] Calibration against Stockfish (Content, "Calibration") is run and reported: Lion lands at 2250 +/- 100 with its
      95% interval, every other puppet within 150 of its target, Lion at half budget measured. Stockfish is not in the
      file and the game makes no network requests.
- [ ] The engine's search features (iterative deepening, aspiration, PVS, transposition table, null move, LMR, killers,
      history, SEE, quiescence, tapered evaluation with mobility, king safety and pawn structure) are each listed in the
      report with where they live in the code; a test position suite (for example 50 tactical positions with known best
      moves) shows Lion solving at least 80 percent within its budget.
- [ ] A browser self-play check (a hidden test hook, 20 games per pair, Lion vs Raven may run 10) shows Mouse beating
      a random mover and each of the seven puppets beating the one below it more often than not, so the Node
      calibration matches what runs in the browser.
- [ ] Every one of the 45 puzzles solves with its stated line; each mate in one accepts every mating move Python listed.
- [ ] Undo vs computer takes back two half-moves and costs a star; Moves never goes down after Undo.
- [ ] Restart in a puzzle act keeps the tally; a finished act's replay shows the Encore card and no Recess.win.
- [ ] Full game playable by keyboard only and by touch only at 390x844; every control above the fold at 1366x768.
- [ ] Calm mode: no lift, fold, slide, shudder or curtain sweep; the stage still reads (shadows, rims, flat wing rows).
- [ ] Shell keys U, R, M, S never clash with game keys; Ctrl+Z undoes.
- [ ] Look board (three hero frames at 1366x768) and `art/cover.webp` painted before game logic; pieces, board,
      stage and puppets are painted sprites; code draws only the geometry listed under Art list. File under 6 MB.

## Open questions

Owner: default accepted, Cory 2026-11-08; may tweak later.

1. Grade band: keep Grades 3-12 with the 3-5 edge (K-2 kids can still play with hints on).
2. Pass-and-play orientation: the board stays put by default; the "Turn the board each move" switch stays.
3. Lion's strength: settled by the owner at about 2250 Elo, measured against Stockfish in calibration (Content).

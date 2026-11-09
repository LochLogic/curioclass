# Go (Recess game)

Wood and stone: click dark and pale stones onto a warm wood board, surround more of it than your rival, and watch
captured groups wash away like ink in water.

## One idea

Go is the game of "who is surrounding whom?". Every stone you place is a little bet about space: it can make a wall,
close a gap, or take a group's last liberty, and the fun is seeing a shape a move before it happens. The game keeps
that one thought in view: the board is almost the whole screen, a group's liberties glow when you touch it, and a
capture is the most satisfying thing that can happen on it.

## The world

**Look.** A wooden tabletop at night under one warm lamp, seen from straight above. The board is a slab of honey wood
with a fine straight grain, its grid drawn in dark ink lines with five or nine small star points. Two plain turned
wooden bowls sit beside it, each with its lid upturned to hold the stones it has captured. The stones are round,
slightly domed and soft-shadowed: the dark stone is matte slate with a faint cool sheen, the pale stone is a warm
off-white with a soft pearly gradient (no stripes). The lamp sits up and to the left, so every stone throws a short
shadow down and to the right and has a small highlight at its upper left.

**Palette** (all checked with the WCAG formula in Python, see Sources):

| Token | Hex | Use | Contrast |
|---|---|---|---|
| room | #1d130a to #3a2614 | page background (same as the shelf box), lamp pool lighter at upper left | text 15.3 / 12.0 |
| cream | #f3eadb | text and icons on the room | 15.3 on room |
| muted | #c9b89c | secondary text on the room | 9.4 on room |
| board | #d9a95f, grain #c48d45 | board wood (painted texture, code fallback color) | |
| ink | #3b2a17 | grid lines and star points | 6.4 on board, 4.7 on grain |
| slate | #1c1d21, sheen #4a4d55 | dark stones | 7.9 on board |
| shell | #f4efe4, shade #cfc6b4, rim #4e3e28 (1.5 px) | pale stones; the rim makes them read on wood | rim 4.8 on board, 3.5 on grain |
| lamp | #f2b544 | --rc-accent (shell buttons, stars), focus ring on the room | 10.0 on room; ink #1b1630 on it 9.5 |
| river | #1f3f66 | liberty dots, hint glow, ko ring, keyboard cursor on the board | 5.0 on board, 3.7 on grain |
| marks | dots: shell on slate, slate on shell | last-move dot | 14.7 |
| dead | #f2b544 cross on slate, #a3341f cross on shell | stones marked dead while counting | 9.2 / 6.0 |

Body sets `--rc-accent: #f2b544`, `--rc-accent-ink: #1b1630`, `--rc-glass: rgba(29,19,10,.72)`.

**Light and materials.** The room is a radial gradient from #3a2614 at the upper left to #1d130a, over the painted
tabletop. The board has a 2 px darker bevel and a long soft shadow. Stones are painted sprites (see Art list) with a drop shadow of
0 2px 3px rgba(0,0,0,.35) under each. Captured stones in a lid are smaller (60%) and piled by a seeded
jitter so the pile looks natural and stays the same after Undo.

**The grab moment.** A stone drops from 6% larger with its shadow tightening to the board in 140 ms and a wood
"click". When a capture happens, each captured stone's color bleeds outward into a soft ink bloom (the painted bloom
sprite, tinted slate or warm gray), grows to about 1.8 stone widths, and fades over 700 ms as if dropped in water; the
stone itself thins and vanishes inside it, and a matching small stone pops into the capturer's lid. Bigger captures
stagger by 40 ms per stone from the capturing move outward, so a long group washes away like a ripple.

**Calm mode** (`Recess.calm`, also prefers-reduced-motion): stones appear in place with no drop; captured stones fade
out over 200 ms with no bloom and no stagger; the lid count updates at once. The world still reads: the last-move dot,
the capture count in each lid and the one-line status ("White took 3") carry everything the motion did.

## Rules

Classic Go, written so a builder cannot get an edge case wrong. The house rules are Chinese-style area scoring with a
superko rule, the simplest set to explain and to count on a device.

1. **Board and start.** 9x9 (default), 13x13 or 19x19 lines; stones go on the points where lines cross. The board
   starts empty. Black plays first (in a handicap game, Black's handicap stones are placed and White plays first).
   Players take turns placing one stone, or passing. Stones never move once placed.
2. **Liberties and chains.** Stones of one color joined along the lines (not diagonally) form a chain. A chain's
   liberties are the empty points next to it along the lines.
3. **Capture.** After you place a stone, remove every opposing chain with no liberties (they go to your lid). Only
   then check your own stone.
4. **No suicide.** A move that leaves your own chain with no liberties, after step 3 removes captures, is illegal.
   A move that looks like suicide but captures first is legal (the builder must resolve captures before the
   self-check).
5. **Ko and superko.** A move may not recreate any earlier whole-board position of this game (positional superko,
   checked with a 64-bit Zobrist hash of the stones only). Almost always this is the basic ko: you may not retake a
   single stone straight back. The game marks the forbidden point with a river ring and says "Ko: play somewhere else
   first, then you can take back."
6. **Passing and the end.** You may pass at any time. Two passes in a row end play and open the count. A pass is not a
   lost point (area scoring needs no pass stones).
7. **Counting (area scoring).** Your score is your stones on the board plus the empty points only your stones surround
   (an empty region whose border touches only your color). Regions touching both colors count for nobody. Dead stones
   are removed first and count for nobody but leave their points to be surrounded. Captures do not count separately.
8. **Komi.** White adds 7.5 points in an even game (the Chinese and AGA value; the half point means no ties). In a
   handicap game White adds 0.5 (our house rule, so a close game still has a winner).
9. **Handicap stones** (against the computer only, kid takes Black): 2 to 4 on 9x9 and 2 to 5 on 13x13 at the star
   points; 2 to 9 on 19x19 at the standard star points, placed in the usual order (2: upper right and lower left; 3:
   plus lower right; 4: plus upper left; 5: plus center; 6: plus left and right middle; 7: plus center; 8: plus top
   and bottom middle, center removed; 9: plus center). 9x9 star points are C3, G3, C7, G7 and E5; 13x13 D4, K4, D10,
   K10 and G7; 19x19 D4, K4, Q4, D10, K10, Q10, D16, K16, Q16.

**Why area scoring (it is easier for kids).** Every point at the end is plainly black, white or nobody's, so the count
is something a kid can see and check by eye. Playing inside your own area or filling a neutral point never changes the
score, so "keep playing until you are sure" costs nothing, which is what lets a device with no referee settle any
argument by playing it out (rule 7 below). No one has to remember prisoners. Area and territory scoring almost always
give the same winner (Wikipedia, Rules of Go; British Go Association rules comparison).

**Dead stones, agreed on one device (no referee).** After two passes the board dims slightly and the game proposes
which stones are dead: a chain is proposed dead when, over 200 quick random playouts from the current position (no
filling of one's own eyes), its points end up owned by the other color in more than 70% of them; chains that are
unconditionally alive by Benson's algorithm are never proposed dead. Dead stones show a cross. Then:
- **Play a friend:** either player taps a chain to toggle it dead or alive; the count updates live. Two buttons, "Black
  agrees" and "White agrees", must both be pressed; any toggle after that clears both. "Play on" goes back to play
  (the player who passed first moves next). Because counting is by area, playing on to prove a group alive or dead
  never costs either side a point.
- **Against the computer:** the computer proposes. The kid may toggle any chain. "Count it" scores the board if the
  computer agrees with every mark; if it does not, it says "I think that group can still live. Let's play it out."
  and play resumes with the kid to move. The computer then plays to prove its view (it captures or makes life), and
  the next two passes open the count again. The computer never refuses a kid's mark that helps the computer.

**Edge cases a builder gets wrong** (each is a Done when check): a capture that also fills your last liberty is legal;
capturing two chains at once; a snapback (playing into a capture that recaptures more); ko recaptured after one move
elsewhere is legal; the superko check uses the position after captures; passing does not clear the ko history; a
stone on the edge has 3 liberties and in the corner 2; Undo restores captured stones, lid counts and the ko state.

## Modes and levels

The first visit opens Puzzles at "First stones 1", because the rules land best by doing them; every later visit opens
the mode last used. A three-tab strip under the board picks the mode: **Computer**, **Friend**, **Puzzles**.

**Play the computer.** Board size (9, 13, 19; 9 is selected first), level and handicap (none, 2 to the maximum for
the size) are chosen on a small setup card with "Play" as the first button; the kid is Black. The level picker shows
each level's line, gentlest first:

| Level | Sizes | Picker line (on screen) | Think time on a Chromebook |
|---|---|---|---|
| Pebble | 9, 13, 19 | "Just learned the rules. Makes friendly mistakes." | under 0.2 s |
| Stream | 9, 13, 19 | "Knows captures and ladders. A fair first match." | under 0.3 s |
| Mountain | 9, 13, 19 | "Reads ahead and plays kindly: it wins without crushing." | under 0.5 s |
| Ridge | 9, 13, 19 | "Plays to win. A real game on 9x9." (on 13 and 19: "Plays to win, but big boards are hard for it.") | about 1 s (9), 2 s (13), 4 s (19) |
| Summit | 9 only | "Our strongest. Thinks a few seconds and gives no gifts." | 3 to 5 s |

`Recess.level` key `cpu-<size>-<level>` (for example `cpu-9-pebble`), or `cpu-<size>-<level>-h<n>` with a handicap;
label "9x9 · Pebble" or "9x9 · Summit · 3 stones". How strong each one really is, and the check that orders them, is
in Content.

**Play a friend** (pass-and-play on one device). Size 9, 13 or 19; both sides at even komi. Key `friend-<size>`. The
turn indicator is the bowl that glows. On a phone the board does not flip; the status line says whose turn it is.

**Puzzles.** Two chapters on one list: "First stones" (8 small puzzles of ours that teach capture and life) and "From
an old book" (11 classic life problems from Gokyo Shumyo, 1812). Key `puzzle-<id>` (`puzzle-f1` to `puzzle-f8`,
`puzzle-b01` to `puzzle-b11`); label "First stones 3" or "Old book 7". Easy first, as listed in Content. Every puzzle is
open from the start (no gates); the list shows each one's stars.

**Today's puzzle.** `Recess.daily()` picks one of the 11 book problems (index `floor(r() * 11)`), one of 8 board
symmetries (`floor(r() * 8)`) and a color swap (`r() < 0.5`), so a known problem still looks new. Same puzzle for
everyone that day. Key `daily-<YYYY-MM-DD>`; label "Today's puzzle".

**Stars and score** (`Recess.start({id: 'go', title: 'Go', score: {label: 'Points', lower: false}, ...})`):

| Mode | Stars (`Recess.win`) | Score |
|---|---|---|
| Computer, even game | win: 1; win with 3 or fewer undos: 2; win with 0 undos: 3 | winning margin in points (e.g. 12.5); `null` if more than 3 undos were used |
| Computer, handicap | win: 1; win with 3 or fewer undos: 2 (never 3) | margin, under the handicap key only; `null` past 3 undos |
| Computer, a loss | `Recess.win` is not called; the count card says the result kindly ("White by 6.5. Close one! Play again?") and offers Play again | none |
| Friend | `Recess.win({score: null, stars: 0})` once the count is agreed (the shell card titles it "Done!"); the count card above it names the winner | none |
| Puzzle or daily | 3: no wrong try and no hint; 2: one or two wrong tries, or the first hint; 1: anything more, or the second hint | `null` |

Wrong tries are counted per puzzle in `Recess.store('tries:<key>')` and only cleared when that puzzle is solved, so
Restart and Undo never wipe them. The margin is shown with one decimal place (komi makes it end in .5).

## Screens and controls

**1366x768 (Chromebook).** The shell bar across the top (about 64 px). Below it, the board is the center and the
biggest thing: a square of `min(100vh - 120px, 62vw)`, about 640 px, so 9x9 cells are about 64 px and 19x19 about
32 px. Left of the board, a 300 px column: the mode tabs, then the mode's card (setup, puzzle list, or puzzle text).
Right of the board, a 220 px column: the white bowl at top and the black bowl at bottom (each with its lid and the
capture count as a number), between them the status line ("Your move", "Pebble is thinking", "Ko: play somewhere
else first") and the big **Pass** button (and **Hint** in puzzles). All of it sits above the fold.

**390x844 (phone portrait).** Shell bar, then the board at full width minus 16 px gutters (358 px; 19x19 cells about
18 px), then one row: black bowl, status, white bowl; then **Pass** (and **Hint**); then the mode tabs and card,
scrolled to below. On boards of 13 and 19, touch play uses aim and confirm: touch and drag shows a ghost stone with a
2.2x round loupe above the finger; lifting leaves the ghost; tapping the ghost (or the "Place" button that appears
beside Pass) places it, tapping elsewhere moves it. 9x9 places on one tap.

**Controls.**
- Mouse: hover shows a ghost stone (55% opacity) on legal points only; click places. Pressing and holding on a chain
  for 300 ms (or hovering it for 600 ms) shows its liberties as river dots.
- Keyboard: arrow keys move a river cursor on the board (it starts on the center point); Enter or Space places; L shows
  the liberties of the chain under the cursor; P passes; H asks for a hint (puzzles); 1, 2, 3 pick the mode tab; Tab
  reaches the side cards. The shell owns U, R, M, S and Ctrl+Z. The board is one `role="grid"` with an
  `aria-label` per point ("D4, empty" / "D4, black, 3 liberties"), and the status line is `aria-live="polite"`.
- Every button is at least 44x44 px.

**What Undo does.** Computer: takes back the computer's reply and your move (both), restoring captures, ko and the
lids, and adds one to the undo count shown under the status ("Undos: 2"). Friend: takes back one move. Puzzle: takes
back your last move and the reply. Count stage: leaves the count and goes back to play (the last pass is undone).
`Recess.canUndo` is false on an empty move list.

**What Restart does.** A new game with the same settings at once (no confirm), or the puzzle's start position. For a
game with 10 or more moves, a small toast "Back to that game?" stays for 8 seconds and puts it back if tapped.

**Kind fail messages.** Illegal suicide: the ghost shakes, "No liberties there: that stone would be captured at
once." Ko: river ring on the point plus the ko line from Rules. Wrong puzzle move: the stone sits for 600 ms, fades,
and the status says "Not this one. Look for the point that gives the group two separate eyes" (life puzzles) or "Not
this one. Count the white stones' liberties" (capture puzzles). A loss to the computer names where it turned: the
largest group that was captured or died is outlined for 3 seconds on the count card ("Your group at the top fell
here. Next time, give it two eyes early.").

## Motion and sound

| Event | Motion | Sound |
|---|---|---|
| Place a stone | drop from 106% with shadow tightening, 140 ms | game "click" (below), not `Recess.play('place')` |
| Capture | ink bloom per stone, 700 ms, 40 ms stagger; small stone pops into the lid | `Recess.play('capture')` once, plus the game "wash" |
| Illegal move | ghost shakes 3 px, 180 ms | `Recess.play('nope')` |
| Pass | the passer's bowl lid lifts 4 px and settles, 200 ms | `Recess.play('tap')` |
| Computer thinking | a single ink drop pulses beside the computer's bowl | none |
| Count opens | board dims 12%, area marks fade in by region, 30 ms apart | `Recess.play('slide')` |
| Puzzle solved | the living group's two eyes glow river for 900 ms, then the shell win card | shell `win` (inside `Recess.win`) |
| Wrong puzzle move | stone fades over 600 ms | `Recess.play('nope')` |

**Game-owned sound layer** (Web Audio, plays only when `Recess.sound` is true, unlocked on first pointerdown like the
shell): "click" is a 35 ms band-passed noise burst at 2.4 kHz (Q 6, gain 0.35) over a 160 Hz sine thump decaying in
60 ms (gain 0.25), pitch varied by plus or minus 4% per stone so a run of moves does not sound mechanical. "wash" is a
600 ms low-passed noise sweep from 1,400 Hz to 300 Hz at gain 0.06, one per capture event, not per stone.

**Calm mode**: no drop, no shake (the ghost turns red-brown #a3341f for 400 ms instead), no bloom, no lid lift, no
pulse (the status line says "Thinking..."), count marks appear at once. Sounds are unchanged (Sound is its own toggle).

## Content

### Computer opponent (one Worker, three gentle levels and two strong ones)

Runs in a Web Worker built from an inline blob (no network), so the page never freezes; every level has a playout or
node budget and a hard time ceiling, and the computer waits at least 400 ms so it feels like a turn. While Ridge or
Summit thinks, Undo, Restart, Sound and the mode tabs still work (they cancel the search). Its moves are deterministic
for a given position and level (its random source is `Recess.rng('<zobrist hash>:<level>')`; a level that hits its
time ceiling on a slow device plays its best move so far), so Undo then replaying the same move gets the same reply:
no fishing for a better answer.

**Move scoring** (every legal move, never filling its own true eye: an empty point whose four neighbors are its own
color or the edge and with at most one diagonal held by the opponent, none on the edge or corner):

| Feature | Points |
|---|---|
| Captures n stones | +10 x n (+10 more if it also saves its own chain in atari) |
| Saves its own chain from atari (the chain then has 3 or more liberties) | +8 x chain size |
| Ataris an opponent chain | +3 (+6 if the ladder reader says it cannot escape; Stream and Mountain only) |
| Self-atari that captures nothing | -15 |
| Next to the last opponent move | +2 |
| Opening (first 6 moves on 9x9, 10 on 13, 16 on 19): 3rd or 4th line from the edge | +3; first or second line -4 |
| Inside its own settled area (ownership of 0.9 or more from the last playouts) | -6 |

The ladder reader follows a chain with 2 liberties: atari on each liberty in turn, the chain extends on its last
liberty, up to 40 plies; it reports "captured" when the chain reaches one liberty with no capture available.

**Gentle levels by the table** (names are plain nature words):
- **Pebble.** Picks by score plus a uniform random 0 to 12; one move in four is instead a random move with score of 0
  or more; no ladder reader; never sees a capture more than one move away. Ceiling 100 ms.
- **Stream.** Score plus random 0 to 4; uses the ladder reader; checks one move ahead that its move is not
  self-atari. Ceiling 200 ms.

**Tree search (Mountain, Ridge, Summit): UCT Monte Carlo tree search**, one engine, strength set by playouts:
- *Tree.* Each node keeps visits n, wins w (for the player who moved into it) and the sum of playout margins. Selection
  takes the child with the highest w/n + 0.8 x sqrt(ln N / n). A new child starts with 8 virtual visits at win rate
  0.5 + 0.04 x its move score from the table above, clamped to 0.05 to 0.95 (the table is the prior, so Captures and
  saves are looked at first). Progressive widening: a node may hold at most 4 + 1.5 x sqrt(its visits) children,
  added best prior first. Tree moves never fill their own true eye and obey positional superko.
- *Playouts* (light, simple ko only, at most 3 x points moves, then area count with komi): (1) if a chain next to the
  last move is in atari, capture it, or extend it when that gives it 2 or more liberties; (2) else, with probability
  0.6, a light pattern move on one of the 8 points around the last move, tried in random order: a hane (diagonal to
  the last move, next to one of our stones that touches it), a cut (splits two enemy stones that touch only
  diagonally, with the other diagonal empty), or a block on the first line next to an enemy edge stone; a pattern move
  that is self-atari for 2 or more stones is skipped; (3) else a random legal move that is not its own true eye and not
  self-atari for 3 or more stones; no legal move means pass, two passes end it.
- *Backup and choice.* Win or loss (margin above 0 for Black) goes up the path; the margin sum goes up beside it. The
  move played is the root child with the most real visits.
- *Budgets* (playouts per move; the time ceiling stops it early on a slow device):

| Level | 9x9 | 13x13 | 19x19 | Ceiling |
|---|---|---|---|---|
| Mountain | 600 | 800 | 1,000 | 0.5 s |
| Ridge | 4,000 | 3,000 | 3,000 | 1.5 s (9), 2.5 s (13), 4 s (19) |
| Summit | 30,000 | not offered | not offered | 5 s |

- **Mountain's kindness cap** (gentle levels only; Ridge and Summit play to win): if the chosen child's average real
  playout margin is above +12 on 9x9 (+20 on 13x13, +30 on 19x19), it plays instead the child, among those with at
  least a tenth of the chosen child's visits and a positive margin, whose average margin is closest to +6.
- **Passing** (every level): it passes when every point is settled (ownership 0.9 or more for one side in its last
  playouts, or from 200 fresh playouts for Pebble and Stream) and its best move would not change the area count, or
  when the kid has passed and no move would change the area count. It never resigns.

**How strong, honestly.** No offline test can give a rating, so these are our estimates from what plain UCT programs
of this size have shown: on 9x9 Summit should beat most children and casual adults and lose to any club player
(roughly 10 kyu on 9x9); Ridge is a real but beatable game on 9x9. On 13x13 Ridge is a beginner's opponent, and on
19x19 every level is weak (playouts are about 4.5 times slower and the board is 4.5 times bigger, so 3,000 playouts
read far less), which is why Summit is 9x9 only and the 19x19 picker line says so. Nothing on 19x19 will trouble a kid
who has climbed the 9x9 ladder; 19x19 is mainly for friend games and for seeing the full board.

**Ladder check (Python, `go9.py`).** A port of a simplified table (no ladder reader, no settled-area term), the
playout policy (rule 1 and the eye rule of rule 3; no light patterns, so the port is weaker than the spec) and the
tree above, at Mountain 100, Ridge 400 and Summit 1,600 playouts, a sixth to a twentieth of the browser's (Python is
that much slower: 3.4 ms per 9x9 playout, measured), so each step is a smaller jump than in the browser. Games on 9x9
with komi 7.5, colors alternating, each game's seed fixed, ended by two passes or at 110 moves, then settled by a
light playout and an area count:

| Pair (stronger first) | Wins | Rate | One-sided binomial p |
|---|---|---|---|
| Pebble over a random mover | 40 of 40 | 100% | 9e-13 |
| Stream over Pebble | 107 of 140 | 76% | 1e-10 |
| Mountain over Stream | 59 of 80 | 74% | 1e-05 |
| Ridge over Mountain | 23 of 24 | 96% | 2e-06 |
| Summit over Ridge | 32 of 40 | 80% | 9e-05 |

Every step holds. The first tree-search version (no prior, no widening) lost to Stream (7 of 20), which is why the
table prior and progressive widening are part of the spec.

### Puzzles

Coordinates use the usual letters A to T without I (A to J without I on 9x9), and numbers counted from the bottom.
In each puzzle the kid plays the color named; the computer plays the other color's replies from the line. `lines` are
the accepted sequences (kid, reply, kid, ...); where a puzzle has two lines the computer picks one reply with
`Recess.rng('<puzzle id>')` per attempt. A puzzle is solved when the kid plays the last move of a line. Any other kid
move is a wrong try (see Screens). `view` is the window shown (corners given as top-left, bottom-right), drawn with
the open sides of the board fading out so a kid sees it is a corner of a bigger board.

**First stones** (ours, 9x9, whole board shown):

```
{"id":"f1","name":"Last liberty","toPlay":"B","black":"E6 D5 F5","white":"E5","goal":"capture","lines":["E4"]},
{"id":"f2","name":"At the edge","toPlay":"B","black":"A7 B6 B5","white":"A6 A5","goal":"capture","lines":["A4"]},
{"id":"f3","name":"Two at once","toPlay":"B","black":"C5 F5 D6 E6 D4","white":"D5 E5","goal":"capture","lines":["E4"]},
{"id":"f4","name":"Run!","toPlay":"B","black":"E5","white":"D5 F5 E6","goal":"save","lines":["E4"]},
{"id":"f5","name":"Squeeze","toPlay":"B","black":"A3 B3 C3 D3 A2 E2 A1 E1","white":"B2 C2 B1 D1","goal":"capture","lines":["D2 pass C1"]},
{"id":"f6","name":"Two eyes","toPlay":"B","black":"A2 B2 C2 D2 D1","white":"A3 B3 C3 D3 E3 E2 E1","goal":"live","lines":["B1"]},
{"id":"f7","name":"Take the eye","toPlay":"B","black":"J7 H7 G7 F7 E7 E8 E9","white":"J8 H8 G8 F8 F9","goal":"kill","lines":["H9"]},
{"id":"f8","name":"The ladder","toPlay":"B","black":"E6 D5 F6","white":"E5","goal":"capture","lines":["E4 F5 G5 F4 F3 G4 H4 G3 G2 H3 H2 J3 J4 J2 J1"]}
```

On f5 the computer cannot save its stones, so it passes ("White can't save them") and the kid captures. On f8 the
computer always runs (extends on its last liberty) until it is caught at the edge.

**From an old book** (Gokyo Shumyo, problems from the first section, "making life"; `book` is the problem number as
printed, `printed` is the book's answer as printed in the 1898 edition's appendix, for anyone checking):

```
{"id": "b01", "book": 1, "toPlay": "W", "view": ["N19", "T13"], "black": "P18 O17 Q17 R17 R15 S15", "white": "Q18 R18 S18 S17 S16", "lines": ["T19"], "printed": ["十九ノ一"]},
{"id": "b02", "book": 15, "toPlay": "B", "view": ["A19", "H13"], "black": "F19 D18 E18 B17 C17 B16", "white": "F18 G18 D17 E17 A16 C16 B15 C15", "lines": ["B19"], "printed": ["十九ノ十八"]},
{"id": "b03", "book": 3, "toPlay": "B", "view": ["A19", "G11"], "black": "B18 C18 B17 C16 B15 B14 A13", "white": "D18 C17 D17 F17 E16 C15 A14 C14 B13 C13 B11", "lines": ["A18 A16 B16"], "printed": ["十八ノ十九・十六ノ十九・十六ノ十八"]},
{"id": "b04", "book": 6, "toPlay": "W", "view": ["M7", "T1"], "black": "R6 S5 P4 Q4 R4 T4 P3 N2 O2 P1", "white": "S4 Q3 R3 S3 P2 Q2 O1", "lines": ["S2 R1 S1"], "printed": ["二ノ二・一ノ三・一ノ二"]},
{"id": "b05", "book": 12, "toPlay": "B", "view": ["A7", "G1"], "black": "A5 B4 B3 C3 D3 D2", "white": "B6 B5 D5 A4 C4 E4 E3 E2", "lines": ["B1 A2 B2"], "printed": ["一ノ十八・二ノ十九・二ノ十八"]},
{"id": "b06", "book": 8, "toPlay": "B", "view": ["A7", "G1"], "black": "B4 B3 D3 D2 E1", "white": "B5 D5 C4 E4 E3 E2 G2", "lines": ["A2 A4 B1"], "printed": ["二ノ十九・四ノ十九・一ノ十八"]},
{"id": "b07", "book": 2, "toPlay": "B", "view": ["N7", "T1"], "black": "R4 S4 S3 R2", "white": "R5 S5 Q4 O3 Q3 R3", "lines": ["T2 S1 T4 Q2 R1"], "printed": ["二ノ一・一ノ二・四ノ一・二ノ四・一ノ三"]},
{"id": "b08", "book": 4, "toPlay": "W", "view": ["A7", "G1"], "black": "B4 C4 D3 E3 G3 F2", "white": "B3 C3 D2 E2", "lines": ["B2 C1 B1 D1 C2"], "printed": ["二ノ十八・一ノ十七・一ノ十八・一ノ十六・二ノ十七"]},
{"id": "b09", "book": 18, "toPlay": "B", "view": ["N8", "T1"], "black": "S5 S4 Q3 R3 S2 R1", "white": "R7 P6 R6 Q4 R4 P3 P2 Q2 R2", "lines": ["T3 S6 T5 S3 R3"], "printed": ["三ノ一・六ノ二・五ノ一・三ノ二・三ノ三"]},
{"id": "b10", "book": 11, "toPlay": "W", "view": ["A19", "G13"], "black": "E18 D17 E17 C16 A15 C15 B14 C14", "white": "C18 D18 C17 B16 B15", "lines": ["A17 B19 B18 A14 C19 A16 A19 B17 B16"], "printed": ["十七ノ十九・十九ノ十八・十八ノ十八・十四ノ十九・十九ノ十七・十六ノ十九・十九ノ十九・十七ノ十八・十六ノ十八"]},
{"id": "b11", "book": 7, "toPlay": "W", "view": ["A19", "G10"], "black": "B17 A16 C16 D16 D15 E14 E13 C12 D12 B11 C10", "white": "B16 B15 C15 D14 B13 C13 D13 B12", "lines": ["C17 C18 D17 E17 B18 D18 A18 B19 A12 A14 B14"], "printed": ["十七ノ十七・十八ノ十七・十七ノ十六・十七ノ十五・十八ノ十八・十八ノ十六・十八ノ十九・十九ノ十八・十二ノ十九・十四ノ十九・十四ノ十八"]}
```

## Sources and licences

| Source | Checked at | Licence or status | Ships |
|---|---|---|---|
| Gokyo Shumyo (碁経衆妙), Hayashi Genbi (林元美), 1812 (文化9年) | ja.wikipedia.org/wiki/碁経衆妙 (author, year, seven sections, the first on making life); en.wikipedia.org/wiki/Gokyo_Shumyo; senseis.xmp.net/?GokyoShumyo | Published 1812, so public domain everywhere (US: published before 1931; Japan: the author died far more than 70 years ago) | Positions and answer lines of 11 problems, transcribed by us |
| The scan we transcribed from: the 1898 edition, publisher 東生書店, National Diet Library pid 861157 | dl.ndl.go.jp/pid/861157 and its IIIF manifest dl.ndl.go.jp/api/iiif/861157/manifest.json, read 2026-11-08: field "Access Restrictions" = "PDM" (Public Domain Mark); attribution "国立国会図書館 National Diet Library, JAPAN" | Public Domain Mark: the library adds no copyright to the scan | No images ship; only stone positions and move lists, read off pages R4 to R6 (problems) and R79 to R80 (the answer appendix, 付録, 生之部) |
| Rules and komi | britgo.org/rules/compare.html (British Go Association rules comparison); en.wikipedia.org/wiki/Komi_(Go); en.wikipedia.org/wiki/Go_(game) | Rules are not copyrightable; our own wording | Our text |
| Engine, puzzles f1 to f8, art, sounds | Written for this game | Ours | In the file |

No modern tsumego site or collection was used (tsumego.tasuki.org and two GitHub sets were looked at only to see that
Gokyo Shumyo is commonly reprinted; nothing was copied). Credit line on the puzzle card: "Old book problems from Gokyo
Shumyo (碁経衆妙) by Hayashi Genbi (林元美), 1812, read from the public domain scan at the National Diet Library of
Japan."

**Facts on screen, each with two sources:**

| Claim | Sources |
|---|---|
| Go began in China and is more than 2,500 years old | Wikipedia, Go (game); Wikipedia, History of Go (earliest written reference in the Zuo Zhuan, about 548 BCE; also mentioned in the Analects of Confucius) |
| It is called weiqi in China, igo in Japan and baduk in Korea | Wikipedia, Go (game); britgo.org/intro/history (Wei Qi, baduk) and Sensei's Library, senseis.xmp.net/?Igo (igo) |
| Komi is 7.5 under Chinese and AGA rules, 6.5 under Japanese and Korean | britgo.org/rules/compare.html; Wikipedia, Komi (Go) |
| Suicide is not allowed under Chinese, Japanese and AGA rules | britgo.org/rules/compare.html; Wikipedia, Rules of Go |
| Area and territory scoring almost always agree on the winner | Wikipedia, Rules of Go; britgo.org/rules/compare.html |

**What I ran (Python).** Contrast: the WCAG relative-luminance formula on every pair in the palette table. Puzzles:
`solver2.py`, a life-and-death prover (outside each puzzle's box is an unbreakable wall of the attacker's stones;
capture, no suicide, ko and path superko, passes; Benson's algorithm proves unconditional life; three-valued AND-OR
search with a transposition table). For every book problem, all printed answer lines replay legally on our
transcription (a strong check that the transcription is right) and the book's capture notes match (problem 11 takes 2
then 1 stone; problem 7 takes 2 on move 6); then, from the end of each shipped line with the attacker to move, the
defender is proven alive at search depth 6 to 8. Problem 1 was also searched from the start: T19 is the only first
move that lives. For f1 to f8, a capture search (moves limited to liberties and nearby points) or the life prover found
the stated first move and no other: f1 E4, f2 A4 (in one move), f3 E4, f4 E4 escapes, f5 D2 starts the squeeze, f6 B1
is the only living move, f7 H9 the only killing move, f8 E4 the only start of a ladder that captures (depth 15). The
ladder of levels: `go9.py`, results in Content. Scratch scripts stay in the session scratchpad; nothing else ships.

**Not shipped:** book problems 5, 9, 10 and 16 (their printed lines replay legally, but the prover could not settle
life within depth 6 to 8, so they wait for a stronger check), and the second printed reply to problem 8 (the computer
always answers A4, the line that was proven). Problems 13, 14, 17, 19 and 20 of the first section were not transcribed
in this pass.

## Roots and word choice

For the later fresh-agent sensitivity check.
- **Whose game.** Go began in China, where it is called weiqi (围棋); it grew in Japan as igo (囲碁) and in Korea as
  baduk (바둑), and all three have strong professional traditions today. The about line on the setup card says so
  once, in plain words: "Go began in China more than 2,500 years ago. It is called weiqi in China, igo in Japan and
  baduk in Korea." We use "Go", the usual English name (from the Japanese), because that is what a kid will hear at a
  club.
- **Terms.** Plain English for every idea: stone, liberty, capture, chain, eye, pass, area, ko, and
  "White's extra points for going second" (the Japanese word komi stays in this spec for builders, never on screen).
  "Ko" stays because every English source uses it; its help line says: "Ko is the Japanese word used in English; in
  Chinese it is jie (劫) and in Korean pae (패)." No other borrowed words on screen (no atari, tsumego, sente, gote,
  joseki; "atari" appears only in this spec, for builders).
- **Art.** A plain modern wooden board and turned wooden bowls, as in clubs everywhere. No clamshell stripes, no legged
  floor board, no lanterns, dragons, cherry blossom, temples, seals, brush-stroke fonts or "ancient wisdom" lines. The
  ink bloom on capture is a physical effect (ink spreading in water), drawn as a soft blot, not calligraphy. Type is
  the shell's own face.
- **Names.** The computer levels are plain nature words (Pebble, Stream, Mountain, Ridge, Summit), not invented
  "Eastern" names, masters or monks.
- **Puzzle source.** The classics come from a Japanese book, credited by author, title and year in romaji and in the
  original characters. A later pass could add problems from the Chinese classic Xuanxuan Qijing (玄玄棋經, 1349), so
  Chinese sources are represented too (Open questions).

## Can it be beaten?

| Check | No-skill path | Closed how |
|---|---|---|
| Win vs computer | Random moves | Pebble beats random play; the ladder check shows every level above it stronger. |
| Win vs computer | Undo until it blunders | Replies are deterministic per position, so Undo then the same move gets the same reply; each Undo costs stars (3 needs none, 2 allows three) and past three the score is `null`. |
| Win vs computer | Pass early to end the game | The count is by area, so passing or filling never shifts points; a lost position stays lost in the count. |
| Win vs computer | Mark its live groups dead at the count | The computer checks every mark and plays it out if it disagrees ("Let's play it out."). |
| Win vs computer | Handicap stones to farm a big margin | Handicap games have their own level keys, so their scores never mix with even games, and they top out at 2 stars. |
| Win vs Ridge or Summit | Replay a memorized winning game | Deterministic replies mean a won game can be repeated move for move. Reaching it took real Go; left open. |
| Win vs Summit | Let another program choose the moves | Cannot be closed in a device-only game; it only fills the player's own local board. Left open. |
| Win vs Ridge or Summit | A slow device stops the search early | The time ceiling makes the computer a little weaker there, never stronger. Accepted. |
| Puzzle stars | Guess at random | Every wrong try is counted; one guess among 15 to 40 empty points in a corner rarely lands. |
| Puzzle stars | Restart or reload to wipe misses | Tries live in `Recess.store('tries:<key>')`, cleared only on solving. |
| Puzzle stars | Undo a wrong try | A wrong stone fades by itself and stays counted; Undo never lowers the count. |
| Puzzle stars | Use hints | The first hint caps the puzzle at 2 stars, the second at 1. |
| Today's puzzle | Change the clock to farm stars | Daily scores are `null` (no board entry), and stars per date are only a daily badge; the book problems keep their own keys and stars. |
| Friend game | Play yourself for a score | Friend games send `score: null`; no board entry. |
| Initials board | Spam entries | The shell asks for initials only for a top score from `Recess.win`, which only computer wins send. |

## Not like

- **Chess** (`chess`): one king and pieces that each move their own way, on a paper stage. Go has one kind of piece,
  stones never move, and the goal is area, not a king.
- **Checkers** (`checkers`): diagonal moves and forced jumps in a neon arcade; pieces move and are taken by jumping.
- **Cargo Hold** (`sliding-blocks`) and **Untangle** (`untangle`): solo puzzles with no opponent.
- Classroom tools and Curiosities: a search of `tools/` for Go, baduk, weiqi, igo and tsumego finds no Go tool (only
  the word "Go" on buttons and base64 noise). Nothing in Curio Class teaches Go, so there is no overlap to manage.

## Art list

Painted (WebP, embedded as data URIs, our own, no people, no text in images):
Painted first (Cory, 2026-11-08; docs/agents/CODEX-RECESS.md, "Visually amazing"): everything a kid looks at is painted and placed exactly by code; this list is a floor, not a ceiling. Paint the look board (three hero frames) before writing game logic.

1. **Room**, 1600x1000, about 140 KB: a dark wooden tabletop at night seen from above, one warm lamp pool at the upper
   left, the middle left plain for the board, nothing else on the table (no teacups, plants, scrolls,
   lanterns or other props); the phone uses a CSS crop of the same file.
2. **Board wood**, 1024x1024, about 120 KB: honey-colored straight-grain wood, even light, no grid (the grid is code),
   tileable so 9, 13 and 19 boards share it.
3. **Bowls**, two cutouts 384x384, about 35 KB each: a plain turned wooden bowl from above with its lid upturned beside
   it (walnut for Black, maple for White), transparent background, same lamp.
4. **Ink bloom**, 512x512, about 40 KB: one round, soft-edged cloud, like a drop of ink in a glass of water,
   grayscale on transparent, tinted in code. No brush strokes, splatter or painted texture.

5. **Stones**, painted sprites, 4 variants per color so a full board looks natural (slate: matte near-black with a soft
   sheen; shell: pearly white with faint natural banding, no clamshell stripes), each 160x160 (twice the 9x9 size),
   transparent, same lamp, about 8 KB each. Captured stones in a lid use the same sprites at 60 percent.
6. **Board edge**, the board's frame and thickness as a painted cutout (honey wood edge, soft shadow on the table),
   1200x1200 outer, about 80 KB, sized so the 9, 13 and 19 grids are drawn inside it.
7. **Cover**, `art/cover.webp`, 1200x750, about 120 KB, no text: the board under the lamp mid-game, a captured group
   washing away in the ink bloom.

Drawn in code (must stay exact, lit to match the painting: warm lamp tint, soft glow, never a flat diagram line): grid
lines, star points, coordinates, ghost stones (the stone sprite at 55 percent), liberty dots, last-move dot, ko ring,
dead crosses, area marks, keyboard cursor, the loupe frame, the "thinking" drop (the ink bloom sprite, small), the lid
pile layout, cards and buttons.

**Size budget** (Recess cap 6 MB): painted art about 630 KB as WebP (140 + 120 + 2 x 35 + 40, stones 8 x 8, board edge
80, cover 120), about 840 KB once base64; more painting is welcome inside the cap;
code about 130 KB (rules, Worker engine about 25 KB, UI, motion and sound); puzzle data about 5 KB (the classic block
measured at 2,761 bytes, plus the 8 first stones); the shell inlined 20 KB (kit/recess.js 14,980 bytes plus
kit/recess.css 5,033 bytes, measured). Total about 1.0 MB. Search trees are run-time memory, not file size.

## notes.md

```
# Go: a note for grown-ups

Go is one of the oldest board games still played. It began in China more than 2,500 years ago, where it is called
weiqi; in Japan it is igo and in Korea baduk. The English name Go comes from Japanese, because the game
first reached Europe and America mostly through Japan. Two players take turns placing black and white stones, and whoever
surrounds more of the board wins. A stone, or a group of stones, that is completely surrounded is captured.

What a child practises without being told:
- Seeing space and shape: which areas are walled in, which gaps are still open.
- Counting: liberties (the empty points next to a group), captured stones, and the area at the end.
- Reading ahead: "if I play here, can they escape?" The puzzles train exactly this in small corners.
- Balancing attack and safety, and losing kindly. Undo is always there, and a wrong puzzle move just fades away.

How it plays:
- Puzzles first: eight short ones that teach capturing and making "two eyes" (the way a group stays alive), then
  life-and-death problems from Gokyo Shumyo, a Japanese problem book from 1812. China, Japan and
  Korea all have classic problem books; this first set happens to come from one of them.
- Play the computer on 9x9, 13x13 or 19x19. Pebble, Stream and Mountain are gentle; Mountain wins without crushing.
  Ridge plays to win, and Summit, on the small board only, thinks a few seconds a move and gives most grown-ups a
  real game (a club player will still beat it). On the big boards the computer is weak; those are best for playing
  a friend.
- Play a friend on one device. At the end both players agree which stones are dead; if you disagree, keep playing,
  which never costs points under the rules used here.

The rules are Chinese-style area rules: count your stones plus the empty points you surround, and White gets 7.5
extra points for going second. Japanese and Korean rules count a little differently (6.5 extra points) but almost
always pick the same winner. A good next step for a keen child is a local Go club or school club; many
teach on the same small 9x9 board.

Nothing leaves the device. There are no accounts, no ads and no chat. Initials on the score board are three letters
only.
```

## Done when

- [ ] Every edge case under Rules works: capture that fills your last liberty, double capture, snapback, ko retake
      after one move elsewhere, superko after captures, edge and corner liberties, Undo restoring captures, lids, ko.
- [ ] Suicide and ko show their kind lines; illegal points never show a ghost.
- [ ] Count: area marks, dead-stone proposal (Benson-alive chains never proposed), both "agrees" needed with a friend,
      the computer playing out a disputed group; scores end in .5.
- [ ] Each of the 19 puzzles solves by its line; any other kid move is a wrong try; the computer's replies
      follow the line; f5 shows its pass.
- [ ] Today's puzzle is the same for everyone on a date and draws the symmetry and color swap correctly.
- [ ] On a 1366x768 Chromebook: Pebble, Stream and Mountain answer within 0.5 s; Ridge and Summit within their
      ceilings in Content; the page (Undo, Sound, scrolling, tabs) stays responsive while any level thinks.
- [ ] A browser self-play check (a hidden test hook, 9x9, colors alternating, 40 games per pair; Summit vs Ridge may run
      20) shows Pebble beating a random mover and each level beating the one below it in more than half the games; on
      13x13, Ridge beats Mountain and Mountain beats Stream over 20 games each. Record the JS playouts per second
      measured on the Chromebook beside the budgets.
- [ ] Mountain's kindness cap: over 20 Mountain wins against Pebble on 9x9, the median margin is under 25 points.
- [ ] Undo vs computer takes back two moves and costs a star; replaying the same move gets the same reply.
- [ ] 13x13 and 19x19 aim-and-confirm on a 390x844 phone; a full game by keyboard only; every control above the fold
      at 1366x768.
- [ ] Calm mode: no drop, bloom, shake, lid lift or pulse; the board still reads (last-move dot, lid counts, status).
- [ ] Shell keys U, R, M, S never clash with game keys (L, P, H, 1 to 3, arrows); Ctrl+Z undoes.
- [ ] No network requests after load.

## Open questions

Owner: default accepted, Cory 2026-11-08; may tweak later. Each question below stands at its default.

1. Add Chinese classic problems (Xuanxuan Qijing, 1349) beside the Japanese ones, after a public domain check of a
   scan, and a Korean classic if a public domain source is found? Default: yes, in a later pass, so the puzzles
   do not come from one country only.
2. Summit's strength: the ladder check orders the levels but cannot rate Summit. Default: ship as specced; if club kids
   beat Summit easily, raise its playouts (the one number that sets its strength) or add RAVE to its tree.
3. The 19x19 computer is weak. Default: keep it (it lets a kid try the full board), with the picker line saying so.
   Or offer only Friend on 19x19?
4. Grade band: data/recess.json says "All grades". Default: keep; the puzzles and Pebble suit young kids.

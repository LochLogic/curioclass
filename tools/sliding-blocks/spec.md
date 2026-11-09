# Cargo Hold (Recess game)

Slide the crates around a ship's hold until the sea chest sits in the square of daylight under the hatch, then watch it
get hauled up and out.

## One idea

A crowded hold where every crate is in somebody's way: the fun is working backward from "the chest must sit in that
patch of light" to "so that barrel moves first", and then finding the shortest order of slides. Crates slide any
direction and any distance, so the hold is a little maze that changes shape with every move. Stars reward the fewest
moves, which turns "I got it out" into "can I get it out in 9?".

## The world

**A cargo hold seen from straight above**, lit by one shaft of daylight from an open hatch grating overhead. Around the
hull, painted dark sea at dusk. Inside, tarred deck planks, pine crates with rope handles, iron-hooped barrels, long
timber crates, round mast stumps, and one teal sea chest with brass corners. The hold's outline changes level to
level (a skiff's rounded locker, a barge's long flat bay, a brig's tapering bow, a steamer's hold split by its
funnel casing, a galleon's deep stern), so each level looks like a different hold.

**How it differs from the brand-name car puzzle and from Klotski.** That puzzle is a 6x6 parking grid, vehicles that
only slide along their length, and one exit in the right wall for a red car. Klotski is a 4x5 box whose 2x2 block
leaves through a slot in the bottom edge. Cargo Hold has none of these. Nine hull shapes (5x5 up to 8x7) with
cut-off corners, a tapering bow and mast stumps inside the floor. Every crate slides in all four directions. Nothing
leaves through a wall: the goal is a 2x2 patch of light *inside* the hold, and the chest is lifted up out of it by a
rope. The hatch moves from level to level. No vehicles, roads, parking or exits anywhere, and every layout is our own
(Content).

**Palette** (checked in Python, WCAG contrast ratio):

| Part | Hex | Against | Ratio |
|---|---|---|---|
| Sea night (page background, outside the hull) | `#0f2a33` | | |
| Ink (in-game text: tally, captions, chart) | `#fff6e0` | sea night | 13.94 |
| Nudge caption ink | `#ffd9a8` | sea night | 11.25 |
| Deck floor (planks, seams `#3a2414`) | `#4e321c` | | |
| Hull rim (thick timber outline) | `#1e140b` with a 2px rim light `#b98a4f` | rim light on floor 3.79, on hull 5.87 | |
| Pine crate (slats `#c4904e`, rope `#e8d3a6`) | `#e0ad66` | deck floor | 5.75 |
| Crate and barrel outline, 2px | `#2a170a` | pine crate | 8.44 |
| Barrel (hoops `#2a2a33`) | `#c9783c` | deck floor 3.47; hoop on barrel 4.22 | |
| Sea chest (body; brass corners and bands `#f2c14e` on its darker sides `#1b6b68`) | `#3fb8ac` | deck floor 4.82; brass on side 3.74 | |
| Hatch light (2x2 glow, grating shadow lines `#4e321c` at 40%) | `#ffe08a` | deck floor | 9.06 |
| Focus ring: outer 3px | `#7ff0e6` | deck floor | 8.63 |
| Focus ring: inner 2px | `#082a33` | pine crate 7.44, chest 6.24 | |
| Shell accent `--rc-accent` (stars, buttons), `--rc-accent-ink` | `#f2c14e`, `#1b1630` | each other | 10.39 |

The chest and a pine crate are close in lightness (1.19), so they never rely on colour alone: the chest is the only
2x2 piece, the only teal one, and the only one with brass corners; every piece has the dark 2px outline (8.44 on pine).
Set `--rc-glass: rgba(8,26,32,.66)` so the shell's bar sits in the same sea tone.

**Light.** One warm key light from the hatch: the 2x2 patch of `#ffe08a` with a soft 18px glow and the grating's
shadow bars across it; a slow drift of dust motes in the shaft (6 to 10 dots, 0.3 opacity). Everything else in the hold
is a little darker toward the hull (a radial vignette on the floor), so the eye goes to the light.

**Materials.** Painted first (CODEX-RECESS.md "Visually amazing", Cory 2026-11-08): the deck planks, the hull rim and
walls, the mast stumps, every crate, barrel and long crate, the sea chest and the hatch light are painted sprites
(cut-out WebP on transparency) that code places exactly on the grid; see Art list. The paintings carry the wood: plank
seams every half cell running bow to stern, grain, iron hoops, rope handles, a darker bottom edge on each crate for
depth. Code adds only a soft drop shadow (2px down, 4px blur) that grows while a crate is held, tinted to the hatch
light.

**The grab moment.** The chest settles into the light, the hatch grating's shadow swings aside as the doors open, the
light floods brighter, a rope and iron hook drop in, and the chest rises toward you (grows, its shadow spreads and
fades) and is gone. Then the shell's win card.

**Calm mode** (`Recess.calm`, also live through `Recess.onMotion`): no dust, no lift, no rope travel, no bump. Crates
move to their new cell in one step. On a win the light brightens in one step, the chest gets a 3px brass ring and a
"Lifted!" tag over it, and the win card follows after 300 ms. Everything still reads: which crate is held (focus
ring), where it went, where the light is.

## Rules

Classic sliding-block rules on our own boards.

1. The hold is a grid of floor cells. Hull cells and mast stumps are not floor. Pieces are rectangles: the chest 2x2,
   barrels 1x1, crates 1x2 or 2x1, long crates 1x3 or 3x1. Pieces never rotate, never overlap, and never leave the hold.
2. **A move is one piece sliding in one straight line (up, down, left or right) by one or more cells**, through empty
   floor only. It stops at the first thing in its way; it can never hop a gap or pass through a piece, wall or stump.
3. **The level is solved** when the chest rests exactly on the 2x2 light (its top-left cell on the hatch's top-left
   cell), after a move ends. Passing over the light mid-drag does not count; ending a drag there does.
4. **Fold rule.** If a slide moves the same piece along the same line (same row for left and right, same column for up
   and down) as the move just before it, it joins that move instead of starting a new one. If the joined move ends
   where the piece began, the move disappears (the count goes back down). This makes keyboard steps and second drags
   fair, and matches the solver: in a shortest solution no piece ever slides twice in a row on one line.
5. **Moves** shown = moves in the history now. Undo removes the last move (a folded move goes back whole), so
   **undone moves do not count**. Restart puts every piece back and sets Moves to 0.

Builder traps: a drag past an obstacle must stop flush against it, not jump past; snap to the nearest legal cell on
release; a drag that ends where it started is no move and makes no sound; Undo is off once the level is won; identical
crates are separate pieces in the game even though the solver treats them as alike (this does not change any count).

## Modes and levels

Three parts, all open from the start (no gates, no locks; GAMES.md): the First voyage, the Fleet, and Today's hold.

**First voyage: 24 hand-placed holds.** Key `hold-<n>` (n = 1 to 24), label `Hold <n>: <name>`, for example
`Recess.level('hold-3', 'Hold 3: Rope Locker')`. Minimums 2 to 22 (Content). Unchanged.

**The Fleet: 540 holds on 12 ships** (owner decision, Cory 2026-11-08: a progressive difficulty ladder with room for
500 and more). Each ship has 45 holds. Difficulty is measured, not guessed: a hold's **minimum** (the breadth-first
search optimal solution length, in moves as defined in Rules) never goes down from one Fleet hold to the next, across
all 540. Each minimum value from 8 to 44 has a plateau of 14 or 15 holds. Inside a plateau, holds within one ship are
ordered by a second measured number, the **search size**: how many different arrangements can be reached from the
start in fewer than `min` moves (identical crates count as alike), which is how much a breadth-first solver has to
look at before it finds the answer; a bigger search size means more tempting wrong turns. Hull size and crate count
are the other knobs: early ships use the small hulls and easy crate mixes, late ships the big hulls with long crates
(the table's last column; Content has the packing and checks).

| Ship | Holds (Fleet number) | Minimum moves | Search size | Main hulls |
|---|---|---|---|---|
| 1 Fishing Boat | 1 to 45 | 8 to 11 | 11 to 537 | skiff, sloop |
| 2 River Barge | 46 to 90 | 11 to 14 | 13 to 2,669 | sloop, skiff, barge |
| 3 Coastal Sloop | 91 to 135 | 14 to 17 | 23 to 6,839 | sloop, skiff |
| 4 Pilot Cutter | 136 to 180 | 17 to 20 | 45 to 2,782 | sloop, cutter, barge |
| 5 Merchant Brig | 181 to 225 | 20 to 23 | 41 to 3,378 | barge, cutter, brig |
| 6 Trading Schooner | 226 to 270 | 23 to 26 | 104 to 9,635 | cutter, schooner, brig |
| 7 Mail Packet | 271 to 315 | 26 to 29 | 109 to 9,616 | barge, cutter, brig |
| 8 Cargo Steamer | 316 to 360 | 29 to 32 | 99 to 12,605 | brig, steamer, schooner |
| 9 Tea Clipper | 361 to 405 | 32 to 35 | 142 to 7,317 | schooner, clipper, steamer |
| 10 Treasure Galleon | 406 to 450 | 35 to 38 | 118 to 36,508 | schooner, galleon, clipper |
| 11 Ocean Freighter | 451 to 495 | 38 to 41 | 187 to 31,204 | steamer, schooner, galleon, clipper |
| 12 Flagship | 496 to 540 | 41 to 44 | 197 to 21,632 | galleon, schooner, steamer, clipper |

The Fleet starts gentler than Hold 24 (8 moves, a breather after the First voyage) and climbs past it from Ship 5 on.
Ships 1 to 3 use barrels and short crates only; long crates appear from Ship 4 (in 18 of its 45 holds) and are in
every Flagship hold. Pieces per hold, the chest included, rise from 8 to 16 on the first three ships to 14 to 22 on
the last four.

- **Key** `fleet-<token>`, where `<token>` is the hold's own packed code (Content), for example
  `Recess.level('fleet-IBFB4hJsA', 'Fishing Boat 1')`. The token is unique per hold and never changes, so stars and
  bests stay put when holds are added, reordered or a new ship is appended. Label `<Ship> <k>` (k = 1 to 45 within the
  ship).
- **Growing it later**: append new ships (45 holds each, minimum 44 and up) as new lines, or add holds into a plateau;
  the stored keys do not move either way. The decoder reads any number of lines.

**Where the game opens.** The game stores the last level key it started (`Recess.store('last')`). On load it opens
that level, or the next one if it was won; on a first visit, Hold 1. The holds chart's `Next unplayed` button jumps to
the first level in the order First voyage, Fleet 1 to 540 with no stars yet.

**Today's hold.** One puzzle a day from a pool of 120 verified puzzles in the file (Content):
`const r = Recess.daily(); const i = Math.floor(r() * POOL.length);`. Key `daily-<i>` (so a puzzle drawn again on
a later day shares its own scores board and best), label `Today's hold`. Every pool puzzle has a minimum of 11 to 15
moves, the same as Holds 11 to 17: hard enough to feel like a treat, short enough for one sitting. Fair because each
was solved by breadth-first search twice (Sources), every visitor gets the same puzzle that day, and stars use the same
formula as the First voyage and the Fleet.

**Score and stars.** `Recess.start({id: 'sliding-blocks', title: 'Cargo Hold', score: {label: 'Moves', lower: true},
onUndo, onRestart, onNext})`. On a solve: `Recess.win({score: moves, stars})` with, for minimum `m`:

- 3 stars: moves <= m + floor(m / 6) (the minimum, or a step or two above on long holds)
- 2 stars: moves <= m + max(3, ceil(m / 2))
- 1 star: any solve

The same formula covers every part (First voyage, Fleet, Today's hold); for the Fleet's 44-move holds that is 3 stars
at 51 or fewer, 2 stars at 66 or fewer.

`onNext` goes to the next hold: Hold 24 goes on to Fishing Boat 1, each ship's 45th hold to the next ship's first,
and Flagship 45 and Today's hold go to the holds chart. The game shows the cutoffs before you start (Screens), never
the solution.

## Screens and controls

**Focus**: the hold, as large as fits, centred. Cell size = min(80px, what fits); never under 44px.

**1366x768.** Shell bar on top (about 64px). The hold centred below it, up to 560px tall (the 7x8 galleon at 64px
cells is 448x512). To its right a narrow tally plank (200px): `Moves 7`, then three star rows such as `★★★ 9 or
fewer`, `★★ 12 or fewer`, `★ any`, the current star row lit brass; `Best 9` when there is one; a `Holds` button.
Under the hold, one caption line (hints and nudges). Nothing scrolls.

**390x844 portrait.** Shell bar on top (icons only). The hold full width with 16px gutters (7-wide hulls 51px cells;
the 8-wide steamer and clipper 44px, the floor, so no hull is ever wider than 8 cells). Below
it the tally as one line (`Moves 7 · ★★★ at 9`), the caption, and the `Holds` button. Fits without scrolling.

**The holds chart** (`Holds` button, or H): a sea chart card over the game, two levels deep so 564 holds never show
at once.

- **Top: the ships.** A `Today's hold` card and a `Next unplayed` button on top, then 13 ship cards: First voyage,
  then the 12 Fleet ships in order. Each card has the painted ship badge (Art list), the name, its move range ("8 to
  11 moves") and stars earned out of 135 (72 for the First voyage), with a thin brass bar for progress. Desktop: 4
  columns. Phone: one column of 72px rows (badge left, text right), scrolling inside the card; the ship holding the
  current level is scrolled into view and outlined.
- **Inside a ship: its holds.** A back arrow and the ship name on top, then 45 tiles (24 for the First voyage) in
  reading order, each 56px square on a phone (5 columns, 9 rows, scrolls inside the card) and 64px on desktop (9
  columns, 5 rows, no scroll): the hold number, a tiny hull silhouette, and three star dots (filled brass when
  earned). The current hold is outlined. Tap a tile to play it.
- Keyboard: arrows move over cards and tiles, Enter opens, Backspace goes back to the ships, Esc or the X closes. All
  open; nothing greyed out or locked. The game's own card, styled like the shell's.

**Pointer and touch.** Press a piece: it lifts (focus ring, shadow grows). Drag: the axis locks after 8px of travel,
the piece follows the finger along that line and stops flush at the first obstacle; release snaps to the nearest
cell. One drag = one move (fold rule). A tap on a piece selects it; then a tap on an empty floor cell in the same row
or column slides it there if the path is clear (for anyone who finds dragging hard); a tap on a cell it cannot reach
plays `nope` and the caption says why ("The barrel is in the way."). A tap on empty floor with nothing selected does
nothing. `touch-action: none` on the board only.

**Keyboard.** Tab and Shift+Tab move the focus over the pieces (chest first, then reading order). Arrow keys slide the
focused piece one cell (folds into one move); Shift+Arrow slides it as far as it can go. H opens the holds chart. The
shell owns U, Ctrl+Z (Undo), R (Restart), M (Sound), S (Scores). Each piece has an `aria-label` such as "Long crate,
row 3, columns 2 to 4"; after a move, a polite live region reads "Barrel moved left 2. Moves 4."

**Undo** (both modes): steps back one move with the piece sliding back; Moves goes down by one; `Recess.canUndo`
tracks the history. **Restart** (both modes): every piece slides home at once, Moves 0, history cleared, no confirm
(levels are short). After a win the board is locked until Next or Play again.

**First hold hints** (caption, Hold 1 only, each shown once and gone after the first move): "Drag the teal chest into
the square of light." On Hold 2: "Crates slide any way, as far as you like, until something stops them."

**Kind nudges** (caption, no buzzers): bumping a wall or piece names it once per drag ("The hull stops it here.",
"The long crate is in the way.") while the blocker's outline flashes brass for 400 ms. When Moves passes the 2-star
cutoff the first time in an attempt: "Still afloat. Undo or Restart any time to try a shorter way." Never a fail state.

## Motion and sound

| Event | Motion (calm version in brackets) | Recess.play | Game-owned layer |
|---|---|---|---|
| Pick up a piece | lifts 2px, shadow grows, scale 1.03 (ring only) | `tap` | none |
| Slide ends (crate) | settles with a 90 ms ease-out, 4 dust specks puff at the leading edge (one-step move) | `place` | low thunk: sine 90 to 55 Hz, 0.12 s |
| Slide ends (barrel) | hoops roll a quarter turn while sliding (no roll) | `clack` | short wooden rattle: noise burst through a 900 Hz band-pass, 0.08 s |
| Slide ends (long crate) | as crate, 120 ms | `place` | deeper thunk 70 to 45 Hz, 0.16 s |
| Bump into an obstacle | 3px bounce back, blocker outline flashes (flash only) | `clack` once per drag | none |
| Tap an unreachable cell | selected piece shakes 3px twice (no shake) | `nope` | none |
| Undo | piece slides back 120 ms (one step) | `slide` | none |
| Restart | all pieces slide home together 250 ms (one step) | `slide` | none |
| Chest on the light | doors' shadow swings aside 300 ms, light brightens, rope and hook drop 300 ms, chest rises and fades 500 ms (light brightens in one step, brass ring, "Lifted!") | `pop` as the doors open; the shell plays `win` | hinge creak: sawtooth 300 to 180 Hz through a 1.2 kHz low-pass, 0.35 s; rope pulley ticks: three 2 kHz clicks 70 ms apart |
| Hold ambience | dust motes drift (none) | none | very quiet hull creak: brown noise through a 300 Hz low-pass at gain 0.02 with a 0.1 Hz swell; starts on the first tap |

All game-owned sounds are WebAudio synths in the file (no audio files) and play only when `Recess.sound` is true.
Burst: `Recess.burst` at the chest's last spot with `['#f2c14e', '#ffe08a', '#3fb8ac', '#fff6e0']` (the shell skips
it in calm).

## Content

**Data format.** Each hold is rows of characters: `#` not floor (hull or mast stump), `.` empty floor, `A` the sea
chest (2x2), every other letter one piece (each letter one rectangle: 1x1 barrel, 1x2 or 2x1 crate, 1x3 or 3x1 long
crate). `hatch` is the cell under the light's top-left corner, as [x, y] from the top-left of the rows. A `#` cell
that a flood fill from the grid's edge cannot reach through other `#` cells is a mast stump, drawn as a round post;
the rest are outside the hull and drawn as sea. The hull outline is traced around the floor cells with rounded outer
corners.

**How the holds were made.** Six hull shapes and each hatch spot were drawn by hand; the crate mix (barrels and crates
first, long crates from Hold 9) and the number of open cells were set by hand for each hold (9 open cells on Hold 1
down to 3 on the last). A seeded packing filled the hold, a breadth-first search of every reachable arrangement found
each one's exact distance from solved, and the start was picked at exactly the target minimum with the chest as far
from the light as that minimum allows. Every hold was then checked by a second, separate solver (Sources). The
minimum rises from 2 to 22, with easier small-hull holds mixed in (Holds 10 and 16) as breathers.

**The 24 holds** (minimum = fewest moves by the rules above; stars by the formula in Modes):

| Hold | Name | Hull | Size | Barrels / crates / long crates | Open cells | Minimum | 3 stars | 2 stars | 1 star |
|---|---|---|---|---|---|---|---|---|---|
| 1 | First Light | skiff | 5x5 | 2 / 3 / 0 | 9 | 2 | 2 or fewer | 5 or fewer | any solve |
| 2 | Two Barrels | skiff | 5x5 | 2 / 4 / 0 | 7 | 3 | 3 or fewer | 6 or fewer | any solve |
| 3 | Rope Locker | skiff | 5x5 | 0 / 6 / 0 | 5 | 4 | 4 or fewer | 7 or fewer | any solve |
| 4 | Sail Store | sloop | 6x5 | 0 / 8 / 0 | 6 | 5 | 5 or fewer | 8 or fewer | any solve |
| 5 | Galley | sloop | 6x5 | 2 / 8 / 0 | 4 | 6 | 7 or fewer | 9 or fewer | any solve |
| 6 | Cooper's Corner | skiff | 5x5 | 3 / 5 / 0 | 4 | 7 | 8 or fewer | 11 or fewer | any solve |
| 7 | The Mast Step | cutter | 6x6 | 4 / 10 / 0 | 3 | 8 | 9 or fewer | 12 or fewer | any solve |
| 8 | Bilge Walk | sloop | 6x5 | 0 / 9 / 0 | 4 | 9 | 10 or fewer | 14 or fewer | any solve |
| 9 | Lantern Room | cutter | 6x6 | 2 / 6 / 3 | 4 | 10 | 11 or fewer | 15 or fewer | any solve |
| 10 | Powder Dry | skiff | 5x5 | 2 / 6 / 0 | 3 | 10 | 11 or fewer | 15 or fewer | any solve |
| 11 | Bosun's Store | brig | 6x7 | 2 / 7 / 3 | 4 | 11 | 12 or fewer | 17 or fewer | any solve |
| 12 | Salt Pork | sloop | 6x5 | 3 / 8 / 0 | 3 | 12 | 14 or fewer | 18 or fewer | any solve |
| 13 | Tight Squeeze | cutter | 6x6 | 2 / 11 / 0 | 3 | 12 | 14 or fewer | 18 or fewer | any solve |
| 14 | Tar and Twine | brig | 6x7 | 3 / 8 / 2 | 4 | 13 | 15 or fewer | 20 or fewer | any solve |
| 15 | Twin Posts | schooner | 7x7 | 4 / 5 / 5 | 4 | 14 | 16 or fewer | 21 or fewer | any solve |
| 16 | Ballast | skiff | 5x5 | 4 / 5 / 0 | 3 | 14 | 16 or fewer | 21 or fewer | any solve |
| 17 | Spice Hold | schooner | 7x7 | 4 / 8 / 3 | 4 | 15 | 17 or fewer | 23 or fewer | any solve |
| 18 | Below the Bow | galleon | 7x8 | 3 / 7 / 4 | 4 | 16 | 18 or fewer | 24 or fewer | any solve |
| 19 | Anchor Chain | brig | 6x7 | 3 / 10 / 1 | 3 | 16 | 18 or fewer | 24 or fewer | any solve |
| 20 | Captain's Wine | schooner | 7x7 | 4 / 10 / 2 | 3 | 17 | 19 or fewer | 26 or fewer | any solve |
| 21 | Deep Stern | galleon | 7x8 | 10 / 4 / 4 | 3 | 18 | 21 or fewer | 27 or fewer | any solve |
| 22 | Storm Stow | cutter | 6x6 | 6 / 6 / 2 | 3 | 19 | 22 or fewer | 29 or fewer | any solve |
| 23 | Long Haul | galleon | 7x8 | 4 / 7 / 4 | 3 | 20 | 23 or fewer | 30 or fewer | any solve |
| 24 | Homeward | schooner | 7x7 | 2 / 11 / 2 | 3 | 22 | 25 or fewer | 33 or fewer | any solve |

```js
const HOLDS = [
  {n: 1, name: "First Light", hatch: [2, 1], min: 2, rows: ["#B..#", ".D..E", "FD..E", "FAA.C", "#AA.#"]},
  {n: 2, name: "Two Barrels", hatch: [1, 2], min: 3, rows: ["#.AA#", ".BAAD", "E...D", "E..FC", "#GGF#"]},
  {n: 3, name: "Rope Locker", hatch: [2, 2], min: 4, rows: ["#DDB#", "EE.B.", "C..AA", "CFFAA", "#GG.#"]},
  {n: 4, name: "Sail Store", hatch: [2, 1], min: 5, rows: ["#GGHH#", "BC.D.E", "BC.D.E", "IIFAA.", "#.FAA#"]},
  {n: 5, name: "Galley", hatch: [3, 2], min: 6, rows: ["#.BD.#", "GG.DHH", "EIIJJF", "EKKAAF", "#C.AA#"]},
  {n: 6, name: "Cooper's Corner", hatch: [1, 1], min: 7, rows: ["#GGB#", "CHHII", "E...F", "E.AAF", "#DAA#"]},
  {n: 7, name: "The Mast Step", hatch: [3, 3], min: 8, rows: ["#.FGH#", ".IFGHJ", "KI#AAJ", "KLBAAM", "CLNOOM", "#.NDE#"]},
  {n: 8, name: "Bilge Walk", hatch: [1, 1], min: 9, rows: ["#..B.#", "CGGBDE", "CHHFDE", ".AAFII", "#AAJJ#"]},
  {n: 9, name: "Lantern Room", hatch: [3, 0], min: 10, rows: ["#HHII#", ".G.BAA", "DG#.AA", "DGKKKE", "CFLLLE", "#F.JJ#"]},
  {n: 10, name: "Powder Dry", hatch: [1, 2], min: 10, rows: ["#FFB#", "AAGG.", "AAHHD", "IIE.D", "#.EC#"]},
  {n: 11, name: "Bosun's Store", hatch: [2, 1], min: 11, rows: ["##AA##", "#IAA.#", "DIEBJF", "DIE#JF", "MMM.J.", "CGHKK.", "#GHLL#"]},
  {n: 12, name: "Salt Pork", hatch: [3, 1], min: 12, rows: ["#FFGG#", "HHIIE.", "BAA.E.", "CAAJJD", "#KKLL#"]},
  {n: 13, name: "Tight Squeeze", hatch: [0, 3], min: 12, rows: ["#.DKK#", "AADLLE", "AA#FGE", "..BFGH", "CMMIJH", "#NNIJ#"]},
  {n: 14, name: "Tar and Twine", hatch: [3, 4], min: 13, rows: ["##GG##", "#HH.B#", "IIJJ.F", "NNN#.F", "E.CKKF", "EAALLD", "#AAMM#"]},
  {n: 15, name: "Twin Posts", hatch: [2, 1], min: 14, rows: ["##BIJ##", "#AAIJC#", "FAAIJKD", "FL#.#KG", "HLMMEKG", "HL..NN.", "##OOO##"]},
  {n: 16, name: "Ballast", hatch: [2, 2], min: 14, rows: ["#AA.#", "BAA.F", "C.HHF", "DGIIE", "#GJJ#"]},
  {n: 17, name: "Spice Hold", hatch: [3, 4], min: 15, rows: ["##JJ.##", "#FKKGH#", "BFLLGHI", "MM#C#HI", "NNDPPPI", "OOAA.E.", "##AA.##"]},
  {n: 18, name: "Below the Bow", hatch: [2, 1], min: 16, rows: ["###B###", "##CAA##", "#HHAAF#", ".II#.FG", "JJDKKFG", ".LLMMEG", "#NNN.E#", "##OOO##"]},
  {n: 19, name: "Anchor Chain", hatch: [1, 1], min: 16, rows: ["##MM##", "#EAAF#", "GEAAFH", "GNN#.H", "OOB.LI", ".JKCLI", "#JKDL#"]},
  {n: 20, name: "Captain's Wine", hatch: [4, 4], min: 17, rows: ["##QQQ##", "#BFGHI#", ".JFGHIK", "LJ#C#NK", "LOO.DNM", "PPAA.NM", "##AAE##"]},
  {n: 21, name: "Deep Stern", hatch: [3, 5], min: 18, rows: ["###.###", "##BOO##", "#NCQQQ#", "DNL#RRR", "ENLFGPP", "HAAM.IJ", "#AAMK.#", "##SSS##"]},
  {n: 22, name: "Storm Stow", hatch: [3, 1], min: 19, rows: ["#HOOO#", "IH.JBC", "IM#JDE", "KML.AA", "KML.AA", "#FNNG#"]},
  {n: 23, name: "Long Haul", hatch: [2, 4], min: 20, rows: ["###K###", "##FKL##", "#BFKLG#", "HIC#LGM", "HIDJ.EM", ".AAJNNM", "#AA.OO#", "##PPP##"]},
  {n: 24, name: "Homeward", hatch: [0, 4], min: 22, rows: ["##DE.##", "#FDEKK#", "GFPPPLL", "GH#B#MM", "IHAAJ..", "ICAAJNN", "##OOJ##"]},
];
```

**One shortest solution per hold** (for the builder's tests; never shown in the game). `chest R1` = the chest slides
right 1; `2x1@3,4 L2` = the 2-wide, 1-tall piece whose top-left is at x 3, y 4 slides left 2; positions are at that
moment.

```
 1. chest R1; chest U2
 2. 1x1@1,1 L1; chest L1; chest D2
 3. 2x1@0,1 R1; 1x2@0,2 U1; 2x1@1,3 L1; chest L1
 4. 1x2@3,1 L1; chest U2; 1x2@2,3 R1; 1x2@2,1 D2; chest L1
 5. 1x1@2,0 L1; 1x2@3,0 L1; 2x1@4,1 L1; 2x1@3,1 U1; 2x1@3,2 U1; chest U1
 6. chest U1; chest L1; 1x2@4,2 L1; 1x2@3,2 D1; 2x1@3,1 D1; 2x1@1,1 R2; chest U1
 7. 1x2@1,1 U1; 1x2@1,3 U1; 1x2@2,4 L1; 1x1@3,5 L1; 1x1@2,5 U1; 1x1@4,5 L2; 2x1@3,4 D1; chest D1
 8. 2x1@1,1 U1; 2x1@1,2 U1; chest U1; 2x1@3,4 L2; 1x2@3,2 D1; 1x2@3,0 D1; 2x1@1,0 R2; 2x1@1,1 U1; chest U1
 9. 1x1@3,1 L1; chest L1; 1x2@5,3 U1; 3x1@2,4 R1; 1x2@1,4 R1; 1x3@1,1 D1; 1x1@2,1 L2; 2x1@1,0 D1; 2x1@3,0 L2; chest U1
10. 1x1@3,4 U1; 1x2@4,2 U1; 1x1@3,3 R1; 1x2@2,3 R1; 2x1@0,3 R1; 2x1@1,3 D1; chest D1; 2x1@2,1 L2; 2x1@2,2 U1; chest R1
11. 1x3@4,2 U1; 3x1@0,4 R3; 1x1@0,5 U1; 1x1@0,4 R2; 1x2@1,5 U1; 1x2@1,4 L1; 1x3@1,1 D3; 1x2@2,2 L1; 1x1@3,2 L1; 1x1@2,2 D1; chest D1
12. 1x1@5,3 U1; 2x1@3,3 R1; chest R1; 1x1@0,2 R1; 1x1@1,2 D1; 2x1@0,1 D1; 2x1@2,1 L2; chest U1; 2x1@4,3 L1; 1x1@5,2 D1; 1x2@4,1 R1; chest R1
13. chest D1; 1x2@2,0 L1; 2x1@3,0 L1; 2x1@3,1 L1; 1x2@4,2 U2; 1x2@3,2 R1; 1x2@3,4 U2; 2x1@1,4 R1; 1x1@0,4 R1; 2x1@1,5 R1; 1x1@1,4 D1; chest D1
14. 1x1@4,1 D2; 2x1@2,2 R1; 2x1@3,2 U1; 2x1@0,2 R3; 3x1@0,3 U1; 1x1@2,4 U1; 1x1@2,3 L2; 2x1@3,4 L2; 2x1@1,4 U1; chest U1; 2x1@3,6 L2; 2x1@3,5 D1; chest R2
15. 1x2@6,3 D1; 1x1@6,2 D1; 2x1@4,5 L1; 1x3@5,2 D1; 1x1@5,1 D1; 1x1@5,2 R1; 1x3@5,3 U2; 2x1@3,5 R1; 2x1@2,4 D1; 1x1@4,4 L2; 2x1@4,5 U1; 2x1@2,5 R2; 1x3@3,0 D3; chest R1
16. chest R1; 1x1@0,2 R1; 1x1@1,2 U2; 1x2@1,3 U2; 1x1@0,3 R1; 1x1@1,3 D1; 2x1@2,3 L2; 2x1@2,2 D1; chest D1; 1x1@1,0 R1; 1x2@1,1 U1; 2x1@0,3 U1; 2x1@2,3 L2; chest D1
17. chest R1; 1x1@2,4 D1; 1x1@5,5 R1; 3x1@3,4 L1; 1x3@5,1 D2; 1x2@4,1 R1; 2x1@2,1 R1; 2x1@2,2 R1; 1x2@1,1 R1; 1x1@0,2 R1; 1x1@1,2 U1; 2x1@0,3 U1; 2x1@0,4 U1; 3x1@2,4 L2; chest U1
18. 2x1@1,3 L1; 1x1@2,4 U1; 2x1@1,5 L1; 2x1@3,4 L1; 2x1@3,5 L1; 1x2@5,5 L1; 1x2@4,5 U2; 2x1@2,5 R2; 2x1@0,5 R2; 2x1@0,4 D1; 2x1@0,3 D1; 1x1@2,3 L2; 2x1@1,2 D1; 1x1@2,1 D1; 1x1@2,2 L1; chest L1
19. 1x1@2,4 R1; 1x3@4,4 U1; 1x1@3,6 R1; 1x1@3,5 D1; 1x1@3,4 D1; 2x1@0,4 R2; 1x2@1,5 U1; 1x2@1,4 L1; 1x2@2,5 L1; 1x1@3,5 L1; 1x1@2,5 D1; 2x1@2,4 D1; 2x1@1,3 D1; 2x1@1,4 R1; 1x2@1,1 D2; chest L1
20. 1x2@0,3 U1; 2x1@1,4 L1; chest U1; 1x1@4,6 L1; 1x1@4,4 D2; chest R1; 2x1@0,4 R1; 2x1@0,5 R1; 1x2@0,2 D2; 1x2@1,2 L1; 1x1@1,1 D2; 1x2@2,1 L1; 1x2@3,1 L1; 1x2@4,1 L1; 1x2@5,1 L1; 1x3@5,3 U2; chest R1
21. 1x1@4,6 R1; 1x2@3,5 R1; chest R1; 1x3@1,2 D2; 1x1@2,2 L1; 1x1@1,2 D1; 1x1@2,1 D1; 1x1@2,2 L1; 1x2@2,3 U2; 1x1@3,4 L1; 1x1@2,4 U1; 1x1@4,4 L2; 2x1@5,4 L2; 1x1@5,5 U1; 1x1@5,4 R1; 1x1@5,6 U2; 1x2@4,5 R1; chest R1
22. 1x2@3,1 D2; 1x1@4,1 L2; 1x1@4,2 U1; 1x1@5,2 L2; chest U1; 1x1@4,5 U1; 1x1@4,4 R1; 2x1@2,5 R1; 1x1@1,5 R1; 1x3@1,2 D1; 1x2@1,0 D1; 3x1@2,0 L1; 1x1@4,1 U1; 1x1@5,1 L2; chest U1; 1x2@3,3 R1; 1x1@3,2 D2; 1x1@3,1 D2; chest L1
23. 1x2@0,3 D1; 1x2@3,4 D1; 1x1@2,4 R2; 1x1@2,3 D1; 1x1@2,4 R1; 1x2@1,3 R1; 1x1@1,2 D1; 1x1@1,3 L1; 1x2@2,3 L1; 1x1@3,4 L1; 1x1@2,4 U1; 1x2@1,3 U1; chest U1; 1x2@3,5 U1; 2x1@4,6 L2; 2x1@4,5 D1; 1x1@4,4 D1; 1x1@4,5 R1; 1x2@3,4 R1; chest R1
24. 2x1@5,3 D1; 2x1@5,2 D1; 3x1@2,2 R2; 1x1@3,3 U1; 1x1@3,2 L1; 1x2@3,0 D2; 1x2@2,0 R1; 1x1@2,2 U2; 1x2@1,1 R1; 1x2@1,3 U2; 1x1@1,5 U2; chest L1; 1x2@3,2 D2; 1x2@3,0 D2; 1x1@2,0 R2; 1x2@2,1 U1; 1x2@2,0 R1; 1x2@1,1 R1; 1x1@1,3 U2; 1x2@0,2 R1; 1x2@0,4 U2; chest L1
```

**Today's hold pool** (120 puzzles, minimum 11 to 15; histogram 11: 24, 12: 28, 13: 29, 14: 18, 15: 21; hulls:
62 skiff, 27 sloop, 12 cutter, 8 brig, 8 schooner, 3 galleon). Same characters, rows joined by `/`. None repeats a
First voyage or Fleet hold (checked again with the Fleet).

```js
const POOL = [  // [hatchX, hatchY, minimum, rows joined by "/"]
  [2,3,11,"#BGG#/AA..E/AA..E/CFHHD/#FII#"],
  [2,1,12,"#BHH#/C.EF./AAEF./AADG./#IIG#"],
  [2,0,11,"#BC.#/F.DGH/FAAGH/.AAII/#JJE#"],
  [0,1,13,"#BHH#/.EF.G/.EF.G/IIAAC/#DAA#"],
  [0,2,12,"#.BC#/D.AAH/.EAAH/FIJKG/#IJK#"],
  [3,1,14,"#EFG#/BEFG./.HHII/CAA.D/#AA.#"],
  [1,1,12,"#BEF#/C.EFD/G..AA/GH.AA/#HII#"],
  [2,3,15,"#BEF#/AAEFG/AAHCG/..HID/#..I#"],
  [3,1,15,"#AA.#/.AAB./EFGGG/EFHHH/#CD.#"],
  [1,1,14,"#...#/HHBE./CIIEF/DGAAF/#GAA#"],
  [2,1,12,"#.BAA#/.GGAAC/HHDFII/JJDFE./#KKFE#"],
  [0,4,13,"##II##/#JJEB#/KKKEF./LLL#FH/.AA.GH/CAADGH/#.MMM#"],
  [1,2,15,"#..AA#/BCDAAH/ECDIIH/E..FGH/#JJFG#"],
  [5,4,15,"##.MM##/#BNNFC#/GHDIFOO/GH#I#E./JPPAAKL/JQQAAKL/##RR.##"],
  [2,1,11,"#..CD#/JJJCD./EAAFFB/EAAGG./#HHII#"],
  [3,4,11,"##CD##/#ECDF#/.EIIFB/.G.#AA/HGJJAA/HKK.LL/#MMNN#"],
  [4,2,14,"###B###/##NN.##/#CGDEF#/KHG#AAL/KHIJAAL/K.IJM.L/#PPPM.#/##OOM##"],
  [1,0,15,"#EF.#/BEF../GC.AA/GHIAA/#HID#"],
  [3,1,11,"#FG.#/BFGII/HAA.C/HAADE/#.JJ#"],
  [2,0,15,"#CD.E#/GCD.EF/G.HH.F/GAABII/#AAJJ#"],
  [0,2,13,"#...#/AACFF/AACDE/GGBDE/#HH.#"],
  [3,2,11,"#AAB#/CAAHH/E..FG/E..FG/#IID#"],
  [4,2,13,"#.CDE#/..CDEF/KK#B.F/GHIAAJ/GHIAAJ/#LLMM#"],
  [1,1,12,"#.GGC#/DHHFCE/D..FBE/.AAFII/#AAJJ#"],
  [2,0,11,"#AAB.#/EAACHH/EF#IIG/EFLLLG/.F.D.G/#JJKK#"],
  [2,1,13,"#EBF#/.E.FG/CHH.G/.AAII/#AAD#"],
  [4,4,13,"##PPP##/#JMMB.#/KJCQQQD/KJ#E#LF/KGAAHLI/NNAA.LI/##OO.##"],
  [1,3,11,"#BHH#/E..AA/E..AA/IIFGC/#DFG#"],
  [3,2,13,"#AAB#/.AAFF/EGGHH/E.IIC/#.D.#"],
  [1,2,14,"#BAA#/CEAAD/.E..F/GGHHF/#II.#"],
  [0,1,15,"#GGHH#/.BIIDE/JJ#CDE/.AAKKF/.AALLF/#MMNN#"],
  [1,2,11,"#IIB#/C.EAA/FGEAA/FGHD./#.H.#"],
  [3,1,15,"#BD..#/.EDLLL/.E#FAA/GJKFAA/GJKHIC/#JKHI#"],
  [2,2,13,"#AA.#/BAAEC/FHHE./FG.D./#GII#"],
  [2,0,13,"#.FG#/H.FGI/HAA.I/BAACD/#EJJ#"],
  [0,2,11,"#.GG.#/AAHH.C/AADIIC/JJDEFB/#KKEF#"],
  [4,3,15,"#KKK.#/GLLLHH/GD#AA./GD.AA./BEFCII/#EFJJ#"],
  [1,4,11,"##B.F##/#GH.F.#/CGHIDMM/LJ#I#NN/LJAAKOO/L.AAKPP/##EQQ##"],
  [0,3,11,"##.K.##/#BCKMM#/AADKQQQ/AA#L#HI/EF.L.HI/GNNLJOO/##PPJ##"],
  [3,1,14,"#.AA#/C.AA./C.DDB/CEEFF/#GGG#"],
  [1,2,12,"#HHII#/DAA.JJ/DAAGE./KKFGE./#BFGC#"],
  [0,1,11,"#.BC#/..DGG/HHDFE/.AAFE/#AAF#"],
  [2,2,15,"#EEFF#/AAB.GG/AAHHII/C.DJJ./#.DKK#"],
  [1,2,12,"#FFF#/AAGGG/AA.EE/.CD.B/#CD.#"],
  [4,1,12,"#BLLE#/.FG.EC/HFGIAA/HJKIAA/#JK.D#"],
  [1,5,11,"##LL##/#DMMB#/EDNNFG/EAA#FG/HAAIJK/HOOIJK/#..C.#"],
  [0,1,13,"#..AA#/..BAAC/JJJDDC/EEFFGG/#HHII#"],
  [2,0,15,"#.BEC#/.AAEGH/FAA.GH/FIIIGH/#JJJD#"],
  [3,3,13,"#JJJB#/CEFKKK/GEFHD./GAAHII/#AA..#"],
  [2,0,13,"#F.B#/CF.DG/HHAAG/E.AAG/#III#"],
  [2,0,13,"#BF.#/GCFH./GAAH./DAAII/#JJE#"],
  [2,3,14,"#.JJ#/BAAF./GAAFC/GHID./#HIE#"],
  [3,4,12,"##JJC##/#DKKCE#/.DLL.EF/MM#B#IF/NNAAGIH/..AAGIH/##OOO##"],
  [1,1,15,"#.BC#/DEFHH/.EFAA/.G.AA/#GII#"],
  [3,2,11,"#EGG.#/CEHH.B/CEFIID/JJFAAD/#.FAA#"],
  [4,3,12,"###.###/##KBH##/#LKCHD#/ILK#NNM/ILJAA.M/OOJAAEM/#F.QQQ#/##PPG##"],
  [0,1,12,"#BCDI#/.JJFIG/.E#FIG/AAKK.H/AANNNH/#LLMM#"],
  [3,2,12,"#AAB#/CAAGG/EHHII/E..FD/#..F#"],
  [2,0,14,"#AAKK#/DAAH.E/D.#HFE/GIJHFB/GIJ.LL/#IJ.C#"],
  [3,2,15,"#.BEE#/FFB.AA/CDGGAA/CD..HH/#IIJJ#"],
  [0,3,15,"#JJKK#/LLNNN./AA#BIC/AAFGIH/MMFGIH/#.D.E#"],
  [1,1,13,"#DAA#/.DAA./GGFE./HHFEB/#CF.#"],
  [0,4,13,"##KK##/#I...#/FIBNNN/FI.#JG/CLLHJG/DAAHJE/#AAMM#"],
  [1,3,11,"#BE.#/GGEC./III.F/HHAAF/#DAA#"],
  [3,4,15,"###B###/##.GH##/#I.GH.#/JIC#KLM/JDAAKLM/OOAAPPE/#RRRNF#/##QQN##"],
  [1,3,13,"#FFC#/.GGC./DBHH./DEAA./#EAA#"],
  [3,0,13,"#DEII#/HDE.FG/HAA.FG/HAA.JJ/#BKKC#"],
  [4,4,13,"##RRR##/#INNBJ#/.ICOOJ./PP#D#AA/KEMLFAA/KGML..H/##MQQ##"],
  [0,1,11,"#AAGG#/.AAHHE/BCD.FE/IID.FE/#JJJF#"],
  [0,1,15,"#JJKK#/NNNEFG/..#EFG/AALLMM/AAHI.B/#CHID#"],
  [3,1,12,"##HH##/#AADB#/.AADE./IIC#E./FJJKKG/FLLMMG/#NNOO#"],
  [1,1,15,"#C.D#/BC.DE/GGAAE/.FAA./#FHH#"],
  [1,0,13,"#.C.D#/E.C.DF/EG#AAF/HGBAAI/HJKLLI/#JKMM#"],
  [2,0,12,"#.BF#/GC.FD/GAAHH/.AAII/#EJJ#"],
  [1,2,15,"#EAA#/.EAAB/.HH.C/IIFG./#DFG#"],
  [3,1,13,"#IB.C#/.I.GJJ/HIDGAA/HLLLAA/#EFKK#"],
  [3,0,12,"#..FF#/AAGG.E/AAHH.E/BIIICE/#DJJJ#"],
  [1,0,14,"#FFB#/GGE../HHEAA/.C.AA/#DII#"],
  [3,1,14,"#EB.#/FECII/FHGAA/DHGAA/#H..#"],
  [1,3,12,"#C..#/DC.EE/DFFGG/HHAA./#BAA#"],
  [3,2,15,"#AAB#/.AAFF/.EGG./.EHHC/#DII#"],
  [1,3,12,"#BHH#/E..AA/E.FAA/IIFGC/#D.G#"],
  [1,3,14,"#.B.#/.IIAA/EF.AA/EFGHC/#DGH#"],
  [1,2,11,"#CFF#/.CAA./GGAAD/.B.ED/#HHE#"],
  [2,2,12,"#AA.#/.AABE/F.GCE/FDGHH/#II.#"],
  [5,3,13,"##BE.##/#IIEJJ#/...FKKG/LL#F#CG/HMMNNAA/HOOPPAA/##QQD##"],
  [1,0,13,"#.BE#/FG.EC/FGHAA/..HAA/#DII#"],
  [2,1,12,"#...#/AA.EE/AABFF/GGCHH/#DII#"],
  [1,2,14,"#..AA#/BDDAAC/BEEFFC/GG..HH/#IIJJ#"],
  [2,4,13,"##LLB##/#.CMMD#/KGNNOO./KG#H#IJ/KAAH.IJ/EAAPPQQ/##RRF##"],
  [2,2,13,"#FFF#/GGGAA/.DDAA/.B.C./#EEC#"],
  [2,0,14,"#.DB#/..DCE/AAFFE/AAGG./#HHH#"],
  [1,2,13,"#.EB#/AAECF/AA.GF/HHDG./#III#"],
  [4,3,14,"#KKBC#/DLLJAA/EI#JAA/FI.J../NNNOOO/#GMMH#"],
  [1,2,13,"#.JJJ#/FBDAAG/F.DAAG/FCHHEG/#II.E#"],
  [0,2,12,"#BJJJ#/.AAKKK/.AAEFG/HHCEFG/#IID.#"],
  [0,4,11,"##GH##/#DGHI#/.DGHI./EAA#IF/EAA.BF/JJKKLL/#.CMM#"],
  [2,4,13,"##KK##/#LLMM#/BJ.NN./.JD#EF/GJDCEF/GAAHI./#AAHI#"],
  [2,2,11,"#AA.#/FAABG/FC..G/DHIIE/#HJJ#"],
  [1,3,14,"##DE##/#.DE.#/AALLBF/AA.#GF/HIMMGJ/HINNKJ/#OOCK#"],
  [1,0,12,"#EE.#/D.BFF/D..AA/CGGAA/#HHH#"],
  [2,1,12,"#GGG#/F..CD/FB.CD/FEAA./#EAA#"],
  [0,2,12,"#II.#/.BAAC/D.AAF/JJGHF/#EGH#"],
  [0,1,12,"#.GG.#/..BJJJ/CDAAEF/CDAAEF/#HHII#"],
  [2,2,11,"#HHB#/AAII./AACFG/D..FG/#JJE#"],
  [2,1,12,"#AAD#/BAAD./E.FHH/EGFII/#GC.#"],
  [2,2,12,"#IIIB#/F.DEAA/F.DEAA/FGGHHC/#.JJJ#"],
  [1,2,12,"#FFAA#/CGGAAD/C....D/JJJEHH/#IIEB#"],
  [0,2,15,"#.AA#/BCAAF/.GG.F/DEHHF/#.II#"],
  [1,1,14,"#JJJF#/BE.CFG/.EHHFG/II.AAG/#D.AA#"],
  [0,2,13,"#.AA#/B.AAC/.HHII/.EFGD/#EFG#"],
  [0,2,15,"#..GG#/AAHHE./AACFED/IICFED/#JJFB#"],
  [2,3,11,"#FFB#/GG.AA/HHHAA/CDE../#DE.#"],
  [1,4,14,"#BKKC#/LLMM.I/JD#.GI/JNNNGI/J.HAAE/#FHAA#"],
  [2,2,14,"#AAB#/EAAC./EGGF./HHDF./#.II#"],
  [0,2,12,"#BAA#/HHAAC/EF.G./EF.G./#IID#"],
  [1,3,13,"#.CAA#/BDCAAH/EDFIIH/EGF..H/#G.JJ#"],
  [0,1,14,"#HHF#/.B.FG/IIAAG/CDAA./#EJJ#"],
  [3,2,11,"#BGG#/CAAHH/FAAII/FD.../#EJJ#"],
  [2,2,11,"#AAB#/EAA.F/EGHHF/.G.II/#CD.#"],
];
```

**The Fleet: hulls, packing and the 540 holds.**

Nine hulls. The first six are the First voyage's hulls; barge, steamer and clipper are new for the Fleet. A hull id is
its index here and is stored in each packed hold, so this table may only grow at the end (16 ids fit). No hull is
wider or taller than 8 cells. `#` is not floor: cells joined to the grid's edge through other `#` are outside the hull
(sea), the rest are mast stumps or, on the steamer, its funnel casing (two stumps side by side, drawn as one casing).

```js
const HULLS = [  // id = index; never reorder, only append
  {name: "skiff", rows: ["#...#", ".....", ".....", ".....", "#...#"]},
  {name: "sloop", rows: ["#....#", "......", "......", "......", "#....#"]},
  {name: "cutter", rows: ["#....#", "......", "..#...", "......", "......", "#....#"]},
  {name: "brig", rows: ["##..##", "#....#", "......", "...#..", "......", "......", "#....#"]},
  {name: "schooner", rows: ["##...##", "#.....#", ".......", "..#.#..", ".......", ".......", "##...##"]},
  {name: "galleon", rows: ["###.###", "##...##", "#.....#", "...#...", ".......", ".......", "#.....#", "##...##"]},
  {name: "barge", rows: ["#.....#", ".......", ".......", ".......", "#.....#"]},
  {name: "steamer", rows: ["#......#", "........", "...##...", "........", "........", "#......#"]},
  {name: "clipper", rows: ["##....##", "#......#", "........", "..#..#..", "........", "#......#", "##....##"]},
];
```

**Packed format** (one hold = one token of base64url characters). Read the token as a string of bits, 6 per
character, most significant bit first, using the alphabet `A-Z a-z 0-9 - _` (A = 0, _ = 63). Then:

| Bits | Field |
|---|---|
| 6 | `min`, the minimum number of moves (0 to 63) |
| 4 | hull id (row in the table above) |
| 6 | hatch = y * 8 + x, the light's top-left cell |
| 3 each | one code per floor cell, in reading order (top row first, left to right), skipping cells an earlier piece already covers: 0 empty floor, 1 barrel 1x1, 2 crate 2 wide 1 tall, 3 crate 1 wide 2 tall, 4 long crate 3 wide, 5 long crate 3 tall, 6 sea chest 2x2, 7 unused. A piece's code sits at its top-left cell |
| 0 to 5 | zero padding to a whole character |

The stream ends when every floor cell is decided, so tokens need no length field. Exactly one code 6 per hold.

**Worked example**, Fishing Boat 1, token `IBFB4hJsA` (9 characters):

```
I      B      F      B      4      h      J      s      A
001000 000001 000101 000001 111000 100001 001001 101100 000000
min 001000 = 8 | hull 0000 = skiff | hatch 010001 = 17 -> x 1, y 2
cells: (1,0) 010 crate 2x1 | (3,0) 000 empty | (0,1) 011 crate 1x2 | (1,1) 110 chest | (3,1) 001 barrel
       (4,1) 000 empty | (3,2) 010 crate 2x1 | (0,3) 010 crate 2x1 | (2,3) 011 crate 1x2 | (3,3) 011 crate 1x2
       (4,3) 000 empty | (1,4) 000 empty | then 00 padding
result (same characters as the First voyage):  #BB.#  CAAD.  CAAEE  FFGH.  #.GH#   hatch [1, 2], min 8
```

A decoder, tested against all 540 holds (every hold, hull, hatch and minimum matched):

```js
const B64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_';
const SHAPES = [null, [1, 1], [2, 1], [1, 2], [3, 1], [1, 3], [2, 2]];   // code -> [w, h]; 6 = the sea chest
function decodeLevel(tok) {
  let bits = '';
  for (const ch of tok) bits += B64.indexOf(ch).toString(2).padStart(6, '0');
  let p = 0; const take = n => parseInt(bits.slice(p, p += n), 2);
  const min = take(6), hull = take(4), hv = take(6), hatch = [hv % 8, Math.floor(hv / 8)];
  const grid = HULLS[hull].rows.map(r => [...r]);
  let next = 0; const L = 'BCDEFGHIJKLMNOPQRSTUVWXYZ';
  grid.forEach((row, y) => row.forEach((c, x) => {
    if (c !== '.') return;                       // hull, stump, or covered by an earlier piece
    const code = take(3);
    if (code === 0) { row[x] = ','; return; }    // empty floor, decided
    const [w, h] = SHAPES[code], ch = code === 6 ? 'A' : L[next++];
    for (let j = 0; j < h; j++) for (let i = 0; i < w; i++) grid[y + j][x + i] = ch;
  }));
  return {min, hull, hatch, rows: grid.map(r => r.join('').replaceAll(',', '.'))};
}
```

**How the Fleet was made** (dev time, Python, scripts in the session scratchpad `cargo/ladder/`; nothing is generated
in the browser). Shipping a verified packed table beat a runtime seed generator on both counts: it is small (below)
and safe (every hold is solved and checked before it ships, and a phone never runs a search). Each Fleet slot n
(0 to 539) has a target minimum `8 + floor(n * 37 / 540)` and a hull from its ship's rotation. `ladgen.py`: a seeded
packing fills the hull around a 2x2 chest on a random hatch, leaving 2 to 4 open cells; a breadth-first search lists
the whole state space (up to 150,000 arrangements) and every arrangement's exact distance from solved (moves are
reversible, so that distance is the minimum); the start is an arrangement at exactly the target with the chest as far
(Manhattan) from the light as possible. `gen2.py` filled the deepest slots by mutating deep holds already found
(split a crate into two barrels, merge two barrels, drop or add a barrel, move the hatch) and searching each mutant
from scratch. At most one hold per state space and light (fingerprint: hull, state-space size, deepest distance),
so no hold is just a later position of another hold's puzzle. `finish.py` then
re-solved every hold with the second, separate solver, measured the search size, ordered each ship by (minimum,
search size), packed, round-tripped and checked uniqueness (Sources). Open cells: 2 in 137 holds, 3 in 296, 4 in 107.

**Size.** 73.2 bits per hold on average (9.2 bytes raw); a token is 9 to 16 characters, 12.2 on average, so 13.2
bytes per hold in the file with its separator. Per 100 holds: about 915 bytes raw, about 1.32 KB as it sits in the
HTML. All 540: 7,129 bytes (lines grow from 496 bytes on the Fishing Boat to 684 on the Tea Clipper). A thousand
more holds would add about 14 KB.

**The Fleet data.** 12 lines, one per ship in Fleet order, 45 tokens per line separated by single spaces. Fleet hold
n is token n. Copy the block exactly into the file as one string per ship (`const FLEET = [...]`, with the ship names
from Modes); the 12 lines joined with LF plus a final LF are 7,129 bytes with SHA-256
`94ba9e9a8e7fbde816b9954cbd1f2c57d44eb5d380f82b8bf5e64d2ea73bee32`. At about 7 KB the table sits here rather
than in a separate `ladder.txt`.

```
IBFB4hJsA IAloENZBE IAF4NMEMI IFoBtBttYo IApMYtsMg IEJvMpNNgA IELNhltBBI IBlEthsnAg IEpoFJ5BBI IEwNJpt4IA IFoBsopJPEg IBJAjNBJA IEslHNtthgA IBIoZNsgI IAk4kkppAA JBBHBJlsE JFHItNJNAA JBotsBIZg JEElPBJpkBA JFkhlpZENIA JFJhHMtsJI JBJFptgYE JAk5gokNog JBENoNF4g JBAkZpEtEA JYxDNplspsBA JZNFI4BpNNgk JEhNks5hloA JAkolDFIFA JAosNoZAI KFtIJshFZAg KZApZpFpNgBA KYIoM5NhNtoA KALMENlho KAIgHJsslA KFoNtNtAYI KFFkMo4NthA KElElvEMNtg KBMsLIJBA KAgolA4sNA KAk4kklsII KBkpFMZsA KBkkrFtkAE KBIkkNtjMA LBEI4FotEg
LApMYNBsk LBlskNIPA LEnJoppNgA LEJjAhNNJI LY0tBtJPJsAA LFothhJMZs LEwsNtgZJI LBBA5AMNI LYxHJNMoBtIA LEMlEPNBtsA LAIkkAl5Io LBoknJtgEk LAkpIkPAFA LBkpYpoAkA MAlo4JpgE MAgJMHJsA MFRJLMttAA MFMhLFophFA MZlNtMoNsPAA MAtAhpZEI MFtJtIIDNA MZkhostt5tEE MZMDFpttFMJA MEEnMAlNpJA MZttsENJBPBA MBkpYlskEE MBMo5NEgBA MEvEkttsNgA NEllHEtltAg NFRMhvFpogA NZMtFhNtoZIA NExJoprFgI NFHIkNpJsI NBMpYskNkA NZFtshtl4pIA NFMNMNZshI NBooMJo5g NZNssNhlpZhA NZRrFFstNoIA NEsZptBhBI NExtFBtYBI NAhMpk4EIA NAIlsA5FBA OEk5skMtpkg OZkpBZlsMNtA
OFENJNgs5I OEtZoFthBI OAotsDIMI OEEgsZltpkk OEwBNNLItA OKFJlItYIhJA OBJN4pBAA OBMAJ5spA OFtYptJABI OEtIlEPIoJA OBPAgJApFA OAkokkI5Ao OBkrFFEhAE PIxJsoIJZJI PKFtNtjIMJI PEl4FNtsBI PExJlhAZJI PFItEFNFZBA PFRJLMNtEA PEpZFppIIA PFQNNnJBpA PFRYtlkhIJA PBE4shBIIA PBA5EhtgBA PAkklEIZAo PBk5FtgAFA PAokpgYMNA QFRtgYppsgg QJNhBNosk5NA QElJFFnMgJA QElZplgJso QEF5tpANoA QENlFNvAIog QBktlsYMEg QFQoNPINhI QEkpgJtMZI QEoNJs4MNkg QFRIvEsNsMA QBPEopBhAA QAokoN4BIg QAFkkkIYIo QFMkktthjNg RAktoZMgI RFLElFgJptA RFpIZstgNkg
REFpjFBhJI RZJFhsFIovFI RKJVxgtJlYA RFBLJtJggI RENIvBkFtog REshIItJrI RElFpgYNpI REEotvFhtgA RFFYpskMowA RFRallkBIQ RElYtsgBtsA SJtolNoFJl4A SFE4sEpNIJA SEIlk5ttsBA SEIkl5gJJJA SYw4BtNtJooA SZIltiusZRA SJooFNJPFBgo SKIywMIDOFE SFMYoNpNhI SFFZFtkNEhA SEENJsYBJI SFNBrBthBI SFM1mksUZg SFQy2DEgFE SJutONMhYIA TKEhViqklh4g TZSZU1VAIBA TKNE1RlZkMAk TKKG2MCE4EI TZKwMtoVh5g TENIttAMLI TIgttNIZMBlA TKGshxFEILBA TEttEtskYJA TKEothuhKYEA TJxJLEtlgNsk TFRYotFBEJA TJtkhwM2sjBA TFsYIgpMpJA TFkjFsMBtpA UKNoANJLFoko UZIGXSt0CE UJkIRNJNNYA UFNItlMB5Eg
UZOmOhVUDI UKFJtIspMLEA UOAtBKh5slokA UZEytOhMYiA UNEvEINhIspJA UZtJhvMVJgI UJlMtIFZtsIA UKKGuFt4QgA UKMslEh2YkMEg UJlwGYkpIBmA VMtYMFlNMtJI VNEnIlNgtEthI VZOGkVVikZA VJRUVYpEBwI VKIwwlsJJPAg VZRohtvFNhBA VNFHMssIMpNlA VItZsAJpNIog VKIsNMApZtJA VKJMVkNQsZkA VYJk5km0NsiA VMlPENlJNosAg VJNIMNkNZoJA VYJk5km0NsCA VZJFVR1IDBA WZUNFtvFNoBA WY1lllssPJhE WOF0Fo0l4hMQ WJkNvNsgsJtA WNFFBlLMsFtsA WZRpgLJoNKA WNQlhMBtNHRI WILItEIJMJtA WZkpJtthhvAA WJkukui0pjA WJlNlC24gBI WZFrVuh1BAA WZOY0NioOBA WZVmXFUKAQA XIEYFphJNIpA XOBOAFPEpkxI XZJlGxFMHBlA XZBIHJBFhNJA XZAhPBNJNtgg XYFpFJoYoJIA
XSBENPIMtEFKQ XKIs1th40lEg XOG1gNnNtooA XKIk1st40gokA XItFtojMpBJA XSEstoQ6oFEgqA XJtKalsIBpA XSoqN2ENNw4AA XKMwrVJBQIA YJsBtptljNlA YJssluK5kJAA YONJ0qgtILBA YNBJl5slINIgg YKMslBOxEDME YIstNklgFZJI YJAppNIZtgIg YKEoNNBYhJJA YSNNNlFusEYlIA YKMslBOzEBgkg YKNJkphYNsJA YIEsBvNphstA YRBstklrJIFIhA YJoxF6ttgCA YIJIphoJjIJA ZSBEuIlYsoBFKA ZOJkOsAop5lw ZSpshNEoBJFFZE ZJwoELJppNhA ZOlJFFXOgIpA ZKExJEM3CskA ZJkwotpphrAA ZSEgswGPNkOFQ ZOtNgCUtHNJA ZQrFkhFJttkktAA ZJRUFYtxoAQ ZJNJEJtMpHBA ZIIlhsZttsJA ZJRJtFlvBpAA aQxBYlNtttsBkg aNFZANtJNJgk aJQwk4oswtkBA aIhJFtojIBJA aQPFolpoNpMNkA aJtYooBuBiQ aIsttttsAZBA
aQkovBNpkNtpgg aZtsoNtvNABA aZVslvG0MkGA aIEsBvFokpJI aZIyiwsktnEA aItItIpvMAJA aZwpMzAWoJA aZFHVsUVpoA bJNIhZsJstIg bNFZMotlsAopA bJptkG5NAFJA bYwotpNtAZIg bZNNtMtjNIgA bOtJtAoWg5JA bZIvBJJMBplA bIItlvNANNBA bZA5JoAWtBo bMtYhhMJottI bZqEKMTMtsg bZKa1NJBIAA bJAkPJsNJsJA bKERIt1DMBI cNBFNMPNhkNo cJitsFpygYg cSJBsJwgrNyQ cZAmYmNshMJA cNBkthNoPIJI cJkNYppFJAJA cNBkMNM5tNkhA cJNMFZBJJMhA cOJGOlMVoYFA cZFalttkBBQ cNFZEopFslhgkg cYhNIhDJsJIg cKJNlNZkslIA cZIylyipDAA cJtLEIJtIBJA dZourK10BgA dZRIFxO5lgI dNEvFooAppFIk dIgkksNsZNslA dOkkQBppt5skg dSqFF1UkFpEPAg dYMtNJpI5ABA dJokhhIRpNvA
ddAxZw1Ip0wgJA deKpBxMNlZhtJA dNxksFtmlYoGA dSNEspStsPAEw dSMolGJukErIiA dQlo4hNpkMNpsA deONNqO1ikDEEk eMlE5poJNhpA eOCloQ5tlFgI eMpLJsEJkNJI eQlE5JMkMlNgokk edgxDGEKop0uJA eOREMNnV0JFE eMsnAsIFNNNpA eNAtFANtPIJI eMpLNskNsIJI eSQqJlDNtoANI eOFJspxoloYA edhNtvNFNphgNI eOtJDFVFUIgI ecMknFAGEhut1MlA fNhJZJssMNsE fOEnJpsNppIA fOtVMsNk4NBI fOlJJJMlh5IA fd0pkhpsMVXNFIg fONEukupBIYI fQko5hMpsJJkok fNFslJkotjMJA fOsltNHJstEBA fMlE5ptgJpNA fNlJYpguNshA fMlFNtEN5BBI fOslNtBnNKAI fMpEtsNgPJpI fOEkt1G10AZA gNFDAhIppNNo gMstN4MoJpoI gOtMptFstDIEg gdgUlIBrOp1Jok gMpZkptlosIIg gOshotyp6sAA gOB0k50psAJI gMlFoANp5Ntk gOtJVI40gpAI
gQxF5kkphhJIoo ghgsgFHFJqyFNsg gSUkxFM5tsIBpA ghgsgFHFJqyFNkk gSFCJpmsZsNgk hQlAZJNkMpsFEkg hQpHFEposlltAIg hgw2hvMlUkpEmIA heWqFEogMxoTKE hc2RFNIKIZJsoA hQpHFEpotoNkkIg hSOFElUt1koZAA hRWoRtkBNLFko hSEkopgRl3Mtkk hcMgPJGEFut1MhA hiMtgtLQmsulgiA hiNEJtVBh1s5BI hiMyF2E1BmYlIE hQk4kkkp0MKJtA hdpNpBlxupMgZA iQkpvEoBpBtplA iSFAlBqMu5tkkg iQwpYNlAttooEkg iQwIvFsktlFptA iQssLEJoNtptgg iQxo5tEkhphJEo iSEpFMysPMskkg id2pBxNhpBh5NA iQpHFEpoMotpsE iRBBtEpZsltMBA igslPMiq0ERKJA ieSRxBrOutgEI iSQokt0ptljENk iQtonElktglNNoA iSGMlNButkoZA jQI5NpMstJosAA jQlE5JNkMpsFEkg jQxEZlNptlgJFA jcIl4gNJNtJpFJA jipIpstpNpEkLME jhss2sm4MtJghtA jQtArINsNlthlA jQtonMkkNtppoE jcgBltoPJpNttI jQtonEIJhstFJE
jWsyC1sVZoCA jR2pwrNhpEtEA jSEkopmVh5tsEg jitJFs1pt1YIIA kSEooBqMu5sskg kSEogJqMu5lskg kQo5NpMsNAtNEA kSRGIpjMNtoIo kWowuUG3EMJQ kSKFFoUuskInIA kWkTIlhtGogpFA kQtonFothpFFAo kRgkICxNM5tlkg kiwyFuF1GzBAog kQuFYs1usglsgA kSQkpMtF1kF4Nk kiNtOEZNmukgIQ kSSpwrNklgJhI kixMqqphhssZBI lSFAkJqMu5tsk lgwWhnMFqskqJI lQkknJJshlNlAkk lQxF5kkpokBFJIg lgw2hvMlVhFQkhA lhss2kmnBlpMENo lSUpRtDNsNIAo lRBFsoslpjEsSA lWsxuUi5VEgQ lWswuUm3EkIKA lVwlQhBVZJQAo liMsBsIqN6ukFQ lWswuUG3EIkKA lWMozEipJICII mWsssgllVnVkgw mUs6hphJFJEoIA mUs6hplJFJEoIA mUs6lplJFJEoIA mQuNZlt1mhkkA mUoPB1k0xJokI mXMwtBmJEBxZk miQktMOsJotPBtA mgzIBmsolJkpJEIg mSFAlBqMO5tsk mQpDFEpotkltAFA miMhhsJqHVl1kQ
mQok4olNFlMNNgg mds2B1QOsFvMw mWMlQhFVJBDQo nSQJFuosstjFsg nSQJFuossNjFsg nQlA5JNkMpsokkA ngNEvFVg2gRKJA nUoPB0k0mJNEhA ncMgPJGUlmtosFE nWsyuBmlUZAQ nVEwpVVEhDIMo niMtNgAqE6sukkw nSFFRFV5tsBkE nVwgmIpVEqYIFA nc6QpQugNk4oqE neIiNmMp12jBw nQzEkkkp0MKJtA nd6RFZhJFhqBJA oQwpYtlAtsIsokg oc6lkO1AkuYpRE oUs6tkNNUMMoo oUs6tkFNUhhlFA oeWwBpIIxlGZmA oQxFYmhigpNIlA oc6lkO1AkuYJRE oUoHIlVJIopFAg oUs6tkNNUMMIo oQyA6osktt1sA oitJos1NkNq5BA oQsk4osh0hGJtA oiMtNgBqPVmkEmA odAp2sIkE5QlKIg pQlEZJNgMlMoskg peJJuJuvBsJJAA pQtErNNlthtghA pcPMplNhNAppJFA piMsBsJqHVl1kw pWkttklUkl0PCA piMyF2F1CB4oog pSMttkJvBttgQ pVkQqipII5oFE piMhhsJqHVl0lQ pWswmXG1IsgCA pcMkvIAxpmk1tkI pcMkjJAxNmkutkI
pWMww1m0IZhQ piUyEuEipuwLEk qdlBk2NJs5IIGI qWsyG1sVZgKA qWsltkkKt4VkmA qSVFRsMrNpgIo qSUtkkAOWq5tA qWRkGGloUPKGA qiVJJusVltIYIE qWswuUm3JgBQ qWoTIl1tFEFBFA qV0shgGmpHSKA qSUtkigOVu4JA qSEpQkqvMNgNkg qVwI1jGswlMNs qdWRtRlO0BsYI rSMttsJ5ltsAw rRUqwAuVJZMgg rSsOpsokWlYhkg rSNEto0tuk4BhA reR0QoJItZkMqI riMtNgBqHVl0kmA rSAopnJksgNuGA rXI0llWaAwMkEg rdoptgJwN1JlYo rcMp4BGNM0mtsFA rcE0qqMA40JuGA rc6RVRkBtYlFGA rdAp2lpgjKEpRE rVwoxFKolTBAI rVkwkqpBJZ0gI seONOqO1snAAoA siUyMuMVCzEkpA siVJMsVMh0MprI sduRiJrOuhtEA sSKFEOhNloNrE sc4qRRppLIJoAg sWNkxtMpFnBBBA sQIk5kFOkkBxNI sVkTFEltpExFEA sSMklImN0glYIw sixqlGwklFnQtAA sRgow4UNwKIiA sR2GGuNhYhMBA sXISNkmojSlkA
```

## Sources and licences

Nothing from any source ships in the file. Rules are the classic public domain sliding-block rules; all holds (First voyage
and Fleet), the pool, the art direction and the sounds are our own; the Fleet was generated by our own scripts.

| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| Sliding-block puzzles in a shallow box are over a century old (L. W. Hardy's US patent 1,017,752, filed 1907, granted 1912), so the mechanic is free to use | Google Patents, US1017752A, "Puzzle", Lewis W. Hardy, filed 1907-12-14, granted 1912-02-20 (a sliding block puzzle in a flat box) | Wikipedia, "Klotski" (Hardy's patent filed 1907, granted 1912) | Yes |
| The well-known car puzzle is a 6x6 grid, vehicles slide only along their length, a red car leaves through an exit; made by ThinkFun | Wikipedia, "Rush Hour (puzzle)" | The owner's brief for this game (6x6, exit on the right, red car) | Yes; we copy none of it |
| Klotski is a 4x5 box whose 2x2 block leaves at the bottom middle; counting "one piece slid any distance" as one move is the usual convention | Wikipedia, "Klotski" | Wikipedia, "Sliding puzzle" (sliding puzzles overview; the fifteen puzzle by Noyes Chapman, 1880) | Yes, on the board; our move counts straight lines only (stricter) |

Licences quoted: Wikipedia text is "available under the Creative Commons Attribution-ShareAlike 4.0 License" (read
at the page foot, 2026-11-08); used for facts only, no text ships. US patents are public domain US government works,
and this one expired long ago. The painted backdrop and rope cutout are made for Curio Class (Art list).

**Checks run (Python 3.13, scripts in the session scratchpad `cargo/`).**
- `fast.py` + `levels_build.py`: bitmask BFS over each hold's whole state space; start picked at the exact target.
- `verify.py`: a separate set-based forward BFS (`solver.py`) from each start; all 24 minimums matched (2 to 22),
  every hold solvable, star cutoffs computed, one shortest solution printed (above). Search sizes 22 to 3,246 states.
- `verify_pool.py`: the same forward BFS on all 120 pool puzzles; every minimum matched, no duplicates, no overlap
  with the First voyage.
- After writing this file, the HOLDS and POOL blocks were read back out of this spec and solved again: all matched.
- `contrast.py`: every ratio in the palette table.
- `sim.py`: random play (300 runs per hold, 400-move cap, fold rule on). Results under Can it be beaten.

**Fleet checks (scripts in `cargo/ladder/`, 2026-11-08).**
- `finish.py`: the separate set-based forward BFS (`solver.py`) re-solved all 540 Fleet holds from their starts:
  540 of 540 solvable, every minimum equal to the generator's (0 mismatches). Minimums never drop from hold to hold
  (asserted), 8 to 44, 14 or 15 holds per value.
- Uniqueness: each hold's smallest description over the 8 grid symmetries (mirrors, turns, and the transpose, hull
  and light included) was compared across the 540 Fleet holds, the 24 First voyage holds and the 120 pool puzzles
  (read back from this spec): 0 duplicates, 0 mirror or rotation duplicates, 0 overlaps. All 540 tokens differ.
- Round trip: every hold packed, unpacked by the Python decoder and by the JavaScript decoder above (Node 24), and
  compared: 0 mismatches. SHA-256 of the 12 lines as stated.
- `sim_ladder.py`: random play on every 9th Fleet hold (60 holds, 100 runs each, 600-move cap): 1,243 random solves,
  3 stars once (one 9-move hold), 2 stars 16 times (only holds with minimum 14 or less).
- After writing this file, the Fleet block was read back out of this spec: checksum matched, all 540 decoded and
  solved again by `solver.py`, minimums matched.

## Can it be beaten?

| Check | No-skill path | What happens | Closed by |
|---|---|---|---|
| 3 stars on a hold | Random sliding | 300 random runs per hold: 3 stars on Hold 1 in 4 runs, Hold 3 in 4, Hold 5 in 1, Hold 10 in 1, never on any other hold; median random solve 55 to 282 moves | Tight cutoff (minimum or a little above) |
| 2 stars | Random sliding | At most 16 of 300 (Hold 1), 0 from Hold 6 on except Hold 10 (5) | 2-star cutoff at min + max(3, half) |
| Moves count | Undo after a wrong turn | Undone moves leave the count; a player who explores with Undo still has to land on a short path, which is the planning skill | By design; said in notes.md |
| Moves count | Wiggling a piece back and forth, or stepping with arrows | Fold rule joins same-piece same-line slides and cancels a return to start, so the count cannot fall below the true minimum and is not inflated | Fold rule, matches the solver |
| Moves count | Restart mid-level | Resets to 0 with the pieces at the start; gains nothing | Nothing to close |
| Moves count | Win, then Undo for a lower score | Undo is off after a win | Locked board |
| Solve | Tap-to-slide across a gap or through a piece | Path must be clear; else `nope` and a caption | Rule 2 |
| Solve | Dragging the chest over the light and away | Only a move that ends on the light wins | Rule 3 |
| Star cutoffs shown | The tally shows "★★★ 9 or fewer" | Gives the target length, not which piece moves; finding it is the game | Accepted |
| Daily stars | Replaying today's hold | Same puzzle, same cutoffs; replays only improve your own best, stars cap at 3 | Shell stores the max |
| Daily stars | Changing the device clock to farm new dailies | Each pool puzzle is its own key; at most 3 stars each, 120 puzzles; on this device only | Accepted (device-only) |
| Holds open | Skip to Hold 24 or Flagship 45 | All holds are open by design (no gates); stars still need a solve | GAMES.md rule |
| Fleet stars | Random sliding on the Fleet | 60 sampled holds x 100 random runs: 3 stars once (a 9-move hold), 2 stars 16 times, none above a 14-move minimum | Same cutoffs as the First voyage |
| Fleet stars | A wrong minimum lets 3 stars be impossible or too easy | Every minimum is BFS-exact, re-solved by a second solver, and the builder re-solves all 540 again (Done when) | Two solvers plus the build test |
| Fleet bests | Saved stars lost or moved to another hold when the Fleet grows | Keys are the hold's own token, not its position | Token keys |
| Scores board | Initials spam | Shell keeps the top 10 per key on this device; a spammer can only crowd their own machine | Shell |

## Not like

- **Go, Chess, Checkers** (first collection; `tools/chess/spec.md`): two-player look-ahead against a rival or the
  computer. Cargo Hold is solo, no opponent, a fixed puzzle with a shortest answer.
- **Untangle** (first collection): drag points freely on a plane until lines stop crossing; any order works. Here
  pieces only slide on a grid and order is everything.
- **The shell demo** (`kit/recess-demo.html`): a 3x3 numbered tile slide, one hole, only for testing the shell.
  Cargo Hold has many piece sizes, irregular hulls, posts and a target inside the hold.
- **parallel-parking** (ELA 9 grammar tool) and **traffic-light-coder**: car and street worlds; nothing shared.
- **box-packer** (crates filled by layers, volume): a counting tool, no sliding.
- **GAMES-RESEARCH.md concept 4 "Slide Plan"** ("get the cart out of the yard") was scored as a weak academic tie and
  set aside; Cargo Hold returns as a Recess game where the planning is the point, with no cart and no yard exit.
- `grep -ril "sokoban|sliding block|slide puzzle" tools docs` finds no other sliding-block game or tool.

## Art list

Painted first (CODEX-RECESS.md "Visually amazing", Cory 2026-11-08). Everything a kid looks at is painted unless it
is pure geometry; code places every sprite exactly. **This list is a floor, not a ceiling**: add any painted piece that
makes the hold richer (a lantern on a post, a coil of rope in a hull corner, gulls over the sea). The palette table
guides contrast and mood; the paintings may refine it as long as the contrast checks still pass. All painted pieces
share one light: warm daylight from the hatch, straight above. Sprites at about twice their largest on-screen size
(cells are drawn at up to 80px, so a 1x1 sprite is 160x160). No text in any image.

| Image | Size, format | Prompt | Use |
|---|---|---|---|
| `cover` | 1200x750 WebP, about 120 KB | The shelf box art (`art/cover.webp`): a ship's cargo hold seen from above at a slight angle, packed with pine crates and iron-hooped barrels, one teal sea chest with brass corners sitting in a bright square of daylight under an open hatch, dust in the light, dark teal sea at dusk around the hull, painterly, deep saturated colours, no text | The game's box on `/recess/` |
| `sea-dusk` | 1600x1200 WebP, about 150 KB | Calm dark teal sea at dusk seen from straight above, soft long swells, a few glints of warm lantern light on the water, painterly, deep saturated colours, nothing in the centre | Page background behind the hull, `object-fit: cover`; darkened 20% under the tally |
| `deck` | 1024x1024 WebP, tileable, about 200 KB | Tarred dark oak deck planks seen from straight above, planks running top to bottom, seams and treenails, worn and warm, evenly lit, seamless tile | Hold floor, clipped to the floor cells (one plank seam every half cell) |
| `hull-rim` | 9-slice sheet 512x512 WebP with alpha, about 80 KB | Thick dark ship's timber framing seen from above, a rounded outer corner piece, a straight piece and an inner corner piece, warm rim light on the inner edge | The hull wall traced around the floor cells (Content), corners rounded |
| `stump` | 160x160 WebP with alpha, about 15 KB | A round sawn-off wooden mast stump with iron band, seen from straight above, warm top light | Each mast stump cell |
| `barrel` | 160x160 WebP with alpha, about 20 KB | A wooden barrel seen from straight above, iron hoops, round lid with staves, warm top light, dark outline | Barrel (1x1) |
| `crate-2` | 320x160 WebP with alpha, about 35 KB | A pine shipping crate seen from straight above, slats, two rope handles, a darker bottom edge, warm top light, dark outline | Crate 2x1 (not rotated for 1x2: its light is baked in from the top, so 1x2 uses `crate-2v`) |
| `crate-2v` | 160x320 WebP with alpha, about 35 KB | As `crate-2`, long side vertical | Crate 1x2 |
| `long-3` / `long-3v` | 480x160 and 160x480 WebP with alpha, about 50 KB each | A long timber crate with three slat sections and iron straps, from straight above, warm top light, dark outline | Long crate 3x1 and 1x3 |
| `chest` | 320x320 WebP with alpha, about 45 KB | A teal sea chest with brass corners and bands seen from straight above, rounded lid, warm top light, dark outline | The sea chest (2x2) |
| `hatch-light` | 320x320 WebP with alpha, about 40 KB | A square shaft of warm golden daylight falling on a deck, the shadow of a wooden hatch grating across it, soft glowing edges | The 2x2 light; brightens on a win |
| `hatch-doors` | 320x320 WebP with alpha, about 40 KB | Two open wooden hatch doors seen from below, edges lit gold | The doors' shadow swinging aside on a win (not in calm) |
| `rope-hook` | 160x640 WebP with alpha, about 30 KB | A thick hemp rope hanging straight down ending in a black iron cargo hook, seen from above at a slight angle, painterly, warm light from above | Drops into the light on a win (not shown in calm) |
| `ships` | 13 badges, 320x200 WebP with alpha, about 25 KB each | Each Fleet ship (Modes) seen from the side on a dusk sea, small and charming, same painterly light: a fishing boat, a river barge, a coastal sloop, a pilot cutter, a merchant brig, a trading schooner, a mail packet, a cargo steamer, a tea clipper, a treasure galleon, an ocean freighter, a flagship, plus a rowing skiff for the First voyage | The holds chart's ship cards |

Drawn in code, geometry only (SVG or canvas, exact to the grid), lit to match the painting (soft glow, shadow,
texture and the painting's palette, so it sits inside the picture rather than on top like a diagram): hit areas, the
focus and selection rings, the brass blocker flash, the faint grid of cell seams if the deck paint needs it, the drop
shadows, the dust motes in the shaft, the small hull silhouettes on the level tiles, the star dots, and the tally
plank's text.

## notes.md

```
# Cargo Hold: a note for teachers and parents

Cargo Hold is a sliding-block puzzle. Crates sit packed in a ship's hold, and the goal is to slide them until the sea
chest rests in the square of light under the hatch. Each slide is one move, and stars go to players who use the
fewest moves.

What it builds
- Planning ahead: before moving anything, players picture what has to move first, and what has to move before that.
- Working backward: the best players start from the goal ("the chest has to end up there, so this crate must go").
- Spatial reasoning: fitting pieces of different sizes into gaps, and seeing a path through a crowded space.
- Sticking with it: Undo and Restart are always there, so trying an idea costs nothing. Undone moves do not count,
  so a child can explore freely and still earn three stars by finding a shorter route.

Under the hood this is the same kind of problem as finding the shortest route through a maze. Every hold was checked
by a computer to make sure it can be solved and to find its fewest possible moves; the star targets come from that
number.

Things to try together
- "Which crate is really in the way? What is in its way?"
- After a solve: "Can you do it in fewer moves?" The star rows show the target.
- Talk through a solution out loud, one move at a time, before touching anything.

How it works
- A first voyage of 24 holds that get gently harder, then a fleet of 12 ships with 45 holds each (540 more). Every
  fleet hold is a step at least as hard as the one before it, measured by a computer as its fewest possible moves:
  8 on the first ship, 44 on the last. Everything is open from the start, plus one new puzzle every day.
- Early holds take about 30 to 90 seconds once a player has the hang of it; the last ships are long puzzles for
  patient planners and can take several minutes.
- The game picks up where the player left off.
- Scores, stars and three-letter initials are saved on this device only. No accounts, no ads, nothing sent anywhere.
- Sound and motion can be turned down with the buttons at the top.
```

## Done when

- [ ] Built on `kit:recess` (script and stylesheet); `Recess.start` with `{id: 'sliding-blocks', title: 'Cargo
      Hold', score: {label: 'Moves', lower: true}}`; no own score, star, initials or high-score UI; no kit:curio header.
- [ ] The 24 HOLDS and 120 POOL entries are copied exactly; a test plays each shortest solution above and wins with
      Moves equal to the listed minimum and 3 stars.
- [ ] A move is one straight slide; the fold rule joins and cancels same-piece same-line slides; Undo removes a whole
      move and lowers Moves; Restart sets Moves 0; Undo is off after a win.
- [ ] Only a move ending with the chest exactly on the light wins; the grab plays (doors, rope, lift) and calm shows
      the one-step version.
- [ ] The Fleet block is copied exactly: a test joins the 12 lines with LF plus a final LF and gets SHA-256
      `94ba9e9a8e7fbde816b9954cbd1f2c57d44eb5d380f82b8bf5e64d2ea73bee32` (7,129 bytes), decodes all 540 tokens,
      re-solves every one by breadth-first search under the Rules (identical crates alike, fold rule moves) in a
      script in Scratch, and confirms: each is solvable, each solved minimum equals its packed `min`, the minimums
      never drop from Fleet 1 to Fleet 540, and no two decoded holds are the same or mirror images. Any mismatch is a
      blocker, never patched by editing a minimum.
- [ ] Fleet keys are `fleet-<token>` and labels `<Ship> <k>`; Hold 24's Next opens Fishing Boat 1; each ship's 45th
      goes to the next ship; the game reopens the last level played (or the next one after a win).
- [ ] The holds chart shows 13 ship cards then a ship's tiles, works by touch and keyboard, scrolls inside the card on
      a phone, and nothing is locked.
- [ ] Today's hold uses `Recess.daily()` and key `daily-<i>`; the same pick on two devices on the same date.
- [ ] Drag (with axis lock and flush stops), tap-to-slide, and keyboard (Tab, arrows, Shift+arrows, H) all work.
- [ ] At 1366x768 the galleon and every 8-wide hull, tally and caption fit with no scroll; at 390x844 every cell is
      at least 44px.
- [ ] Each blocked slide or unreachable tap names what is in the way, kindly; no fail state.
- [ ] Sound off silences the game-owned layer too; calm mode removes dust, lift, bumps and rope travel.
- [ ] Painted first: the deck, hull rim, stumps, every crate, barrel and long crate, the chest, the hatch light and
      doors are painted sprites placed exactly on the grid (Art list); code draws only geometry (rings, hit areas,
      shadows, dust, silhouettes), lit to match. `art/cover.webp` (1200x750, no text) exists. Look board of three
      hero frames at 1366x768 in the report, as CODEX-RECESS.md "Visually amazing" asks.
- [ ] One HTML file, offline, at most 6 MB with every image (CODEX-RECESS.md size rule); the report states the size.
- [ ] Playtest: three players new to it finish Holds 1 to 12 at 30 to 90 seconds each on average (estimate to
      confirm; adjust star wording only, never the data).

## Open questions

Owner: default accepted, Cory 2026-11-08; may tweak later. Each default below is the decision.

1. Ambient hull creak: default on at very low volume (default here), or off until asked for?
2. The daily pool leans on the small skiff hull (62 of 120) because small holds are quick to verify. Fine for launch
   (default), or rebalance toward the bigger hulls before ship?
3. No hint button (default). If kids stall on Holds 20 to 24, a "show the next move" button that caps that solve at 1
   star could come later.
4. The Fleet restarts at 8 moves after Hold 24's 22 (default: a breather, and Ship 1 is a fair start for a kid who
   skips the First voyage), rather than starting at 22.
5. The Fleet tops out at 44 moves (default). Holds that long take minutes, beyond the 30 to 90 second guide; they are
   the far end of a 540-hold ladder for patient planners. Lower the top later by trimming ships, never by editing
   minimums.
6. Ship names describe the voyage (Fishing Boat to Flagship); each ship's holds use a mix of hull outlines rather than
   one hull per ship (default), so a "Cargo Steamer" hold may be a brig's outline. Fine, or regenerate with one hull
   per ship?

Size budget: game code about 50 KB, shell about 15 KB, data about 17 KB (holds 3 KB, pool 6 KB, Fleet 7.1 KB, hull
table and decoder 1 KB), painted images about 1.25 MB (Art list: cover 120 KB, sea 150 KB, deck 200 KB, sprites about
475 KB, 13 ship badges about 325 KB): about 1.35 MB total against the 6 MB Recess cap (CODEX-RECESS.md, Cory
2026-11-08), leaving room for the extra painting the art list invites. Every further 100 Fleet holds adds about
1.3 KB.

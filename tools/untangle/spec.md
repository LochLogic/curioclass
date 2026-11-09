# Untangle (Recess game)

Drag the stars of a tangled night sky until no two lines cross, then watch them glide into a picture.

## One idea

You look at a knot of lines and see which star is causing the trouble, where it belongs, and what the shape
underneath wants to be. Every drag is a guess you can watch: dashed lines and little rings show every crossing live,
and the count falls as the tangle opens. When the last crossing goes, the stars glide into a creature or a ship you
uncovered without knowing what it was.

## The world

**Constellations, our own.** A deep indigo night sky with faint violet nebula cloud. The stars are warm white points
with a soft glow; the lines between them are thin threads of pale periwinkle light. Every picture is invented for
this game (a kite, a fox, a whale, a dragon). We do not use the real sky's constellations: Sky Dome (Curiosity) owns
the real sky, and invented pictures avoid any one culture's sky stories.

**Light.** The only light is the stars and the lines. A crossed line burns a hotter coral and goes dashed; a solved
sky turns every line gold and fills the picture with a soft nebula colour.

**Materials.** Stars feel like glass beads of light: they swell when lifted, settle with a tiny bounce when dropped.
Lines are taut threads: they stretch with the star, never sag.

**The grab moment.** The last crossing clears: all lines flash gold, the stars glide (900 ms, ease in-out) from
wherever you left them into the picture, the picture fills with its colour, its name rises under it ("The Whale"),
then the shell's win card.

**Palette** (contrast checked in Python, WCAG formula, against the sky's darkest #0a0b26 and lightest #1b1f5e):

| Role | Hex | vs #0a0b26 | vs #1b1f5e |
|---|---|---|---|
| Sky gradient (top to bottom) | #1b1f5e to #0a0b26 | | |
| Star core | #fff6dc | 17.88 | 13.86 |
| Clear line (solid, 2 px, 85% opacity) | #8fa8ff | 8.46 | 6.56 |
| Crossed line (dashed 7/5, 3 px) and crossing ring | #ff9e6b | 9.51 | 7.37 |
| Solved line, readout zero state | #ffd166 | 13.38 | 10.37 |
| Text | #f4f1ff | 17.33 | 13.44 |
| Quiet text | #b9b6e0 | 9.95 | 7.71 |
| Readout pill background | #14163d at 85% | text 15.57 | |

Shell: body sets `--rc-accent:#ffd166` (ink #1b1630, contrast 12.1) and `--rc-glass:rgba(20,22,61,.62)`.
Crossed and clear lines are only 1.12 apart in contrast with each other, so colour is never the signal: crossed lines
are dashed and thicker, and every crossing gets a ring (see Screens).

Picture fills (one per level, used at 35% opacity as a radial gradient inside the picture's outline) are in the level
data; they are decoration on a solved sky, never information.

**Calm mode.** Same sky, same dashes and rings, but nothing moves on its own: no marching dashes, no twinkle, no
background star shimmer, no bounce. The win shows the picture by a 200 ms cross-fade instead of the glide. The
world still reads: dashed means crossed, rings mark where, gold means solved.

## Rules

The classic untangle puzzle (Mary Radcliffe's idea, made famous by John Tantalo's 2005 Planarity): a set of points
joined by straight lines; move the points so no two lines cross. Our exact rules:

1. **Stars move, lines follow.** Any star can be dragged anywhere inside the sky. Lines are always straight between
   their two stars and are never edited.
2. **What counts as trouble.** The live count ("crossings") is the number of trouble pairs, measured in screen pixels
   on the sky as drawn:
   - Two lines that share no star are a trouble pair if they come closer than **7 px** anywhere. This one rule covers
     a true crossing, two lines touching, two lines nearly touching, and a star sitting on (or nearly on) a line that
     is not its own (that star's own lines start at the star, so they come within 7 px of the other line).
   - Two lines that share a star are a trouble pair if the angle between them is under **4 degrees**, or if the far
     star of either one is within 7 px of the other line (one line lying along its neighbour).
   - Each pair of stars closer than **21.5 px** adds one trouble (only reachable by shrinking the window; see 4).
   Every star in every level and daily sky has at least one line, so no star can hide on a line unseen.
3. **Win.** The sky is solved the moment a star is dropped and the count is 0. The count is checked on every drop
   (and on Undo); while a star is held the count updates live but the win waits for the drop, so a star swept through
   a lucky spot does not end the level by accident. The picture lights only on a 0 count.
4. **No stacking.** When a star is dropped within 22 px of another star, it slides to the nearest free spot: try
   radius 2, 4, 6 ... px around the drop point, 24 directions each (starting due east, going clockwise every 15
   degrees), first spot that is 22 px or more from every other star and 12 px or more inside the sky edge. Only the
   dropped star moves. Stars dropped past the edge are clamped 12 px inside.
5. **Any crossing-free layout wins.** The kid's layout does not need to look like the picture (a mirror image, a
   squashed one, a different arrangement all win). On the win the stars glide from the kid's layout to the picture.
6. **Positions are stored as fractions of the sky** (0 to 1 on each axis); pixels come from the current sky size.
   On a resize or rotation the count is recomputed from new pixels; nothing counts as a move. Stretching a layout is
   an affine map, so true crossings never appear or vanish on resize; only the near-touch rules can change, and they
   then show as trouble the kid can fix.
7. **A move** is one drop that leaves the star 4 px or more from where it was lifted. A drop back in place is not a
   move and makes no Undo step. A keyboard lift, arrow steps and drop is one move. Escape while holding returns the
   star to where it was lifted (not a move).

Builder traps: count pairs once (i < j); test shared-star pairs with the angle rule, never with the 7 px rule (two
lines meeting at a star are always 0 px apart); use pixel coordinates from the current layout, not the 0 to 100
picture grid; recount on resize; never declare the win from a count taken mid-drag.

## Modes and levels

**Skies (20 hand-made levels).** Keys `L01` to `L20` for `Recess.level(key, label)`. Label is `Sky 7` until that sky
has been solved once on this device (stored with `Recess.store('named:L07', true)`), then `Sky 7 · The Turtle`, so
the picture stays a surprise the first time. Star counts rise 6, 6, 7, 8, 9, 9, 10, 11, 11, 12, 12, 13, 13, 13, 13,
13, 14, 16, 16, 18; lines rise from 8 to 32; the start's true crossings rise from 3 to 34 (table in Content). All
skies are open from the start (no gates); the Star chart marks the first unsolved one.

**Tonight's sky (daily).** Key `daily:` plus the same date string the shell uses (`2026-11-8`, month and day not
padded); label `Tonight's sky`. Built from `Recess.daily()` by the generator in Content: 6 random straight lines,
a star at each place two lines meet, a line between neighbouring stars on each straight line. Always 15 stars and 24
lines, the same sky for everyone on that day. It starts with the stars in a ring in shuffled order. When solved, the
stars glide into the true web and the six straight beams that made it glow across the sky for 1.5 s (the reveal: your
tangle was six straight lines all along). Calm: the beams just appear and fade.

**Score: moves (lower is better).** `Recess.start({id: 'untangle', title: 'Untangle', score: {label: 'Moves', lower:
true}, onUndo, onRestart, onNext})`. On a solve, `Recess.win({score: moves, stars})`.

**Stars by moves, not time.** Time would reward fast hands and punish a kid who stops to look, and GAMES.md rules out
timers that punish. Moves reward exactly the thinking: seeing where a star belongs before you drag it.

| Stars | Rule | Shown in the readout as |
|---|---|---|
| 3 | moves at most n (the number of stars in the sky) | `★★★ within 9` |
| 2 | moves at most 2n | `★★ within 18` once moves pass n |
| 1 | any solve | nothing extra once moves pass 2n |

"About one touch per star" is a pace any kid can understand. It is always reachable: moving each star once straight
to its spot in the picture solves every sky in n moves (checked in Python with the slide rule, all 20 skies and the
daily). Good planners beat it easily: a sweep-and-watch bot solved 13 of 20 skies in 1 to 7 moves (Can it be beaten?).

**Next.** After Sky N, Next opens Sky N+1; after Sky 20, Tonight's sky; after Tonight's sky, the Star chart.

## Screens and controls

**On load.** The first unsolved sky opens at once (Sky 1 on a first visit), tangled, with the hint line in the bottom
strip: "Drag a star. Make the lines stop crossing." The hint fades after the first drop that lowers the count, and
does not show again on this device (`Recess.store('hinted', true)`). First tap on a star lifts it; first tap on empty
sky does nothing.

**Layout, Chromebook 1366x768.** Shell bar on top (about 64 px). The sky field fills everything between the bar and a
56 px bottom strip, full width with 16 px side gutters (about 1334 x 640). Bottom strip, left to right: the **Star
chart** button (game-owned, 44 px tall pill, a little star-map icon and the word), the **crossings readout** (centre;
a knot icon drawn as two crossing strokes plus "5 crossings" / "1 crossing", and at zero a gold four-point star icon
plus "No crossings"), and the **moves readout** ("Moves 4 · ★★★ within 9"). The hint line floats just above the
strip, centred, quiet text.

**Layout, phone 390x844 portrait.** Shell bar on top (labels hidden by the shell under 760 px). Sky field about 366 x
690. Bottom strip 64 px: Star chart as a 44 px icon button, crossings readout (still the words,
"5 crossings", in 15 px; never a bare symbol), moves readout shortened to "4 / ★★★ 9". Nothing scrolls.

**The sky field** is an SVG filling the field, `touch-action: none`. Draw order: background specks, picture fills
(only when solved), clear lines, crossed lines, crossing rings, stars, the held star on top.

**Live crossing marks.** Every trouble pair marks itself two ways besides colour: both lines turn dashed (7 on, 5
off) and 3 px wide, and a hollow ring (7 px radius, 2 px stroke) sits at the crossing point; for a near-touch or
overlap the ring sits at the midpoint of the two closest points. A star whose lines are in trouble gets a slow
twinkle (motion mode only). In motion mode the dashes march slowly (1 px per 60 ms), so crossed lines "fizz".
Recount every animation frame while a star is held (at most 32 lines, 496 pairs: cheap).

**Mouse and touch.** Pointer down within 26 px (mouse) or 32 px (touch) of a star lifts the nearest one (pointer
capture); the star grows to 1.35x with a 34 px halo ring so it shows around a fingertip. It follows the pointer
exactly (no offset). Pointer up drops it (rules 4 and 7). Pointer down on empty sky does nothing (no panning, no
zoom). Pinch zoom is blocked on the field only.

**Keyboard.** Stars are focusable (`tabindex=0`, `role=button`, aria-label "Star 3 of 9, 2 lines crossed", updated
on each drop). Tab and Shift+Tab move between stars in index order; focus shows a 3 px gold ring. Enter or Space
lifts the focused star (it grows, aria-live says "Lifted. Arrow keys move it."); arrows move it 16 px (with Shift,
4 px), live count updating; Enter or Space drops; Escape puts it back. `C` opens the Star chart. The shell owns U
(Undo), R (Restart), M (Sound), S (Scores) and Ctrl+Z; the game binds no other letters. After each drop an aria-live
line reads the count: "3 crossings left" or "No crossings. Solved!".

**Kind feedback.** There is no fail. What is off is always on screen: dashes and rings. A stall helper: after 6 drops
in a row that do not lower the count, the star touching the most dashed lines gets a slow gold ring and the hint line
says "Try the star with the most dashed lines." (once per attempt, gone on the next drop that lowers the count).
A drop that slides away from another star shows once per attempt: "Stars need a little room."

**Star chart** (game-owned overlay, opened by its button or C, closed by Escape, its Back button, or picking a
sky). A dark card over the sky: 20 sky tiles plus a wide Tonight's sky tile. Chromebook: 5 columns x 4 rows of 104 px
tiles plus the daily tile under them, all above the fold. Phone: 4 columns x 5 rows of 78 px tiles, daily tile under,
fits in 844 px without scrolling. An unsolved tile shows its tangled start as tiny dim dots and lines with "Sky 7"; a
solved tile shows the lit picture, its name, and its stars from `Recess.stars(key)`. The first unsolved tile has a
gold outline. Tiles are buttons (Tab, Enter).

**Undo and Restart.**

| | Skies | Tonight's sky | After a solve |
|---|---|---|---|
| Undo | Puts the last moved star back where it was lifted; moves go down by one; recount. `Recess.canUndo(stack.length > 0)` | same | disabled (`canUndo(false)`) once the sky is solved |
| Restart | Stars jump back to this sky's start, moves 0, Undo stack cleared, picture unlit | same start (the day's ring) | starts the sky again from its tangled start |

Undo taking the count back down is fair because exploring is already free while holding a star (the count is live);
only kept drops are moves. Restart plays `slide` and never asks to confirm.

## Motion and sound

The game owns a small sound layer on top of `Recess.play`: a soft chime, a sine plus a quiet triangle an octave up,
8 ms attack, 600 ms release, on the C major pentatonic (C5 D5 E5 G5 A5 C6 D6 E6). It plays only when `Recess.sound`
is true.

| Event | Motion (motion mode) | Sound | Calm mode |
|---|---|---|---|
| Lift a star | grows to 1.35x over 120 ms, halo appears | `Recess.play('tap')` | grows at once |
| Drag | lines stretch live, dashes and rings update | none | same, dashes still |
| Drop, count went down | tiny settle bounce (scale 1.1 to 1, 160 ms) | chime; pitch rises as the count nears 0 (note index = max(0, 7 - count)) | no bounce, same chime |
| Drop, count same | settle bounce | `Recess.play('place')` | no bounce |
| Drop, count went up | settle bounce | `Recess.play('slide')` | no bounce |
| Drop slides off a neighbour | star glides 120 ms to its free spot | `Recess.play('place')` | jumps |
| Undo | star glides back 160 ms | `Recess.play('slide')` | jumps |
| Restart | all stars glide 250 ms to start | `Recess.play('slide')` | jump |
| Solve | lines flash gold, stars glide 900 ms into the picture, fill fades in 500 ms, name rises 12 px and fades in, then `Recess.win` at 1.6 s | one chime per star as it lands (40 ms apart, rising notes, volume capped), then the shell's `win` | gold lines, 200 ms cross-fade to the picture, name appears, `Recess.win` at 0.4 s; chimes still play |
| Daily solve | as above, then the six beams sweep across the sky for 1.5 s | as above | beams appear and fade |
| Background | 60 tiny specks drawn in code twinkle slowly (opacity 0.3 to 0.8, 3 to 7 s) | none | specks still, no twinkle |

`Recess.onMotion(calm => ...)` switches dash marching, twinkle and the glide on and off at once.

## Content

### The 20 skies (exact data, copy as is)

Per sky: `pts` are the picture positions on a 0 to 100 grid (y down), index = star id; `edges` are the lines as star
id pairs; `polys` are the outlines filled when lit (each an ordered star list); `start` is the tangled start, each
star as thousandths of the sky's width and height (x/1000, y/1000). `fill` is the lit colour.
The picture is fitted into the sky keeping its shape (scale = min of the two axis fits, 8% margin each side, centred).

```json
[
{"key":"L01","name":"The Kite","fill":"#ff7a9c","pts":[[50,4],[78,34],[50,72],[22,34],[50,36],[66,96]],"edges":[[0,1],[0,3],[0,4],[1,2],[1,4],[2,3],[2,5],[3,4]],"polys":[[0,1,2,3]],"start":[[761,112],[729,819],[140,854],[752,418],[390,631],[413,563]]},
{"key":"L02","name":"The Paper Plane","fill":"#9ad7ff","pts":[[4,46],[40,44],[96,10],[58,92],[46,62],[24,62]],"edges":[[0,1],[0,2],[0,5],[1,4],[1,5],[2,3],[3,4],[4,5]],"polys":[[0,2,3,4,5]],"start":[[700,500],[744,556],[835,839],[587,61],[295,511],[934,106]]},
{"key":"L03","name":"The Crown","fill":"#ffd166","pts":[[10,80],[10,30],[30,55],[50,18],[70,55],[90,30],[90,80]],"edges":[[0,1],[0,2],[0,6],[1,2],[2,3],[3,4],[4,5],[4,6],[5,6]],"polys":[[0,1,2,3,4,5,6]],"start":[[316,451],[370,274],[309,655],[877,479],[895,861],[591,385],[818,894]]},
{"key":"L04","name":"The Fish","fill":"#ff9e6b","pts":[[6,50],[36,24],[64,42],[94,20],[94,80],[64,58],[36,76],[26,46]],"edges":[[0,1],[0,6],[0,7],[1,2],[1,7],[2,3],[2,5],[3,4],[4,5],[5,6],[6,7]],"polys":[[0,1,2,3,4,5,6]],"start":[[426,181],[230,738],[674,715],[807,473],[921,736],[504,417],[379,902],[161,166]]},
{"key":"L05","name":"The Sailboat","fill":"#7ee0c3","pts":[[6,68],[50,68],[94,68],[78,90],[22,90],[50,6],[84,58],[50,58],[14,58]],"edges":[[0,1],[0,4],[1,2],[1,3],[1,4],[1,7],[2,3],[3,4],[5,6],[5,7],[5,8],[6,7],[7,8]],"polys":[[0,1,2,3,4],[5,6,7,8]],"start":[[562,613],[710,558],[165,172],[564,536],[468,672],[230,407],[103,701],[847,522],[257,185]]},
{"key":"L06","name":"The Bird","fill":"#b79cff","pts":[[4,42],[30,32],[44,6],[58,30],[80,34],[96,22],[90,50],[62,60],[32,58]],"edges":[[0,1],[0,8],[1,2],[1,3],[1,8],[2,3],[3,4],[3,7],[4,5],[4,6],[5,6],[6,7],[7,8]],"polys":[[0,1,2,3,4,5,6,7,8]],"start":[[504,294],[763,473],[799,351],[423,111],[674,281],[762,297],[889,917],[208,482],[635,864]]},
{"key":"L07","name":"The Turtle","fill":"#7ee0a0","pts":[[20,62],[30,32],[50,20],[70,32],[80,62],[96,52],[26,84],[74,84],[50,44],[6,70]],"edges":[[0,1],[0,4],[0,6],[0,9],[1,2],[1,8],[2,3],[3,4],[3,5],[3,8],[4,5],[4,7],[6,7],[6,9]],"polys":[[0,1,2,3,4],[3,5,4],[0,4,7,6],[9,0,6]],"start":[[806,281],[859,361],[137,741],[396,811],[831,803],[808,621],[238,244],[585,315],[614,892],[612,366]]},
{"key":"L08","name":"The Cat","fill":"#ffb38a","pts":[[16,6],[36,28],[64,28],[84,6],[86,46],[70,82],[30,82],[14,46],[36,50],[64,50],[50,66]],"edges":[[0,1],[0,7],[1,2],[1,8],[2,3],[2,9],[3,4],[4,5],[4,9],[5,6],[5,10],[6,7],[6,10],[7,8],[8,10],[9,10]],"polys":[[0,1,2,3,4,5,6,7]],"start":[[574,801],[710,238],[567,653],[434,455],[251,742],[316,111],[719,100],[629,443],[746,812],[197,640],[445,924]]},
{"key":"L09","name":"The Rocket","fill":"#ff7a7a","pts":[[50,2],[64,24],[64,66],[82,86],[58,76],[42,76],[18,86],[36,66],[36,24],[50,40],[50,98]],"edges":[[0,1],[0,8],[1,2],[1,9],[2,3],[2,4],[2,9],[3,4],[4,5],[4,10],[5,6],[5,7],[5,10],[6,7],[7,8],[8,9]],"polys":[[0,1,2,3,4,5,6,7,8]],"start":[[848,590],[802,465],[401,640],[597,560],[161,409],[380,877],[402,938],[630,658],[405,283],[233,215],[680,912]]},
{"key":"L10","name":"The Owl","fill":"#c9a6ff","pts":[[24,6],[50,22],[76,6],[82,40],[76,74],[60,94],[40,94],[24,74],[18,40],[36,42],[64,42],[50,58]],"edges":[[0,1],[0,8],[1,2],[1,9],[1,10],[2,3],[3,4],[3,10],[4,5],[4,11],[5,6],[5,11],[6,7],[7,8],[7,11],[8,9],[9,11],[10,11]],"polys":[[0,1,2,3,4,5,6,7,8]],"start":[[795,679],[589,900],[361,857],[382,616],[435,744],[564,622],[86,328],[828,151],[205,93],[937,631],[778,893],[929,820]]},
{"key":"L11","name":"The Fox","fill":"#ff9e4f","pts":[[12,6],[34,30],[66,30],[88,6],[90,42],[72,60],[50,94],[28,60],[10,42],[34,46],[66,46],[50,72]],"edges":[[0,1],[0,8],[1,2],[1,9],[2,3],[2,10],[3,4],[4,5],[4,10],[5,6],[5,10],[5,11],[6,7],[6,11],[7,8],[7,9],[7,11],[8,9]],"polys":[[0,1,2,3,4,5,6,7,8]],"start":[[678,395],[927,592],[286,574],[71,691],[659,571],[805,540],[276,197],[594,475],[542,140],[232,670],[358,611],[438,442]]},
{"key":"L12","name":"The Lighthouse","fill":"#ffe08a","pts":[[38,92],[62,92],[58,64],[56,40],[44,40],[42,64],[42,24],[58,24],[50,8],[8,12],[92,12],[12,96],[88,96]],"edges":[[0,1],[0,2],[0,5],[0,11],[1,2],[1,12],[2,3],[2,4],[2,5],[3,4],[3,6],[3,7],[4,5],[4,6],[6,7],[6,8],[6,9],[7,8],[7,10]],"polys":[[0,1,2,3,4,5],[4,3,7,6],[6,7,8]],"start":[[786,345],[586,592],[62,552],[177,841],[283,122],[283,265],[356,851],[554,544],[272,412],[640,899],[365,562],[809,110],[514,64]]},
{"key":"L13","name":"The Butterfly","fill":"#ff8fd0","pts":[[50,22],[50,82],[26,4],[2,14],[18,50],[4,80],[30,96],[74,4],[98,14],[82,50],[96,80],[70,96],[50,52]],"edges":[[0,2],[0,4],[0,7],[0,12],[1,5],[1,6],[1,10],[1,11],[1,12],[2,3],[2,4],[3,4],[4,5],[4,12],[5,6],[7,8],[7,9],[8,9],[9,10],[9,12],[10,11]],"polys":[[0,2,3,4,12],[12,4,5,6,1],[0,12,9,8,7],[12,1,11,10,9]],"start":[[684,385],[554,603],[556,63],[532,555],[80,315],[432,251],[489,180],[340,891],[129,926],[184,451],[344,832],[775,778],[892,529]]},
{"key":"L14","name":"The Rabbit","fill":"#d9d2ff","pts":[[22,48],[28,4],[40,34],[54,4],[52,38],[66,50],[80,62],[96,70],[86,92],[32,92],[30,66],[42,48],[62,74]],"edges":[[0,1],[0,2],[0,10],[0,11],[1,2],[2,3],[2,4],[2,11],[3,4],[4,5],[4,11],[5,6],[5,12],[6,7],[6,12],[7,8],[7,12],[8,9],[8,12],[9,10],[10,11]],"polys":[[0,1,2,3,4,5,6,7,8,9,10]],"start":[[522,425],[466,838],[381,278],[473,251],[482,535],[761,105],[691,224],[604,336],[636,713],[423,884],[666,511],[225,781],[889,592]]},
{"key":"L15","name":"The Ship","fill":"#8fc6ff","pts":[[4,62],[36,62],[64,62],[96,62],[84,86],[16,86],[36,12],[12,50],[64,4],[90,50],[30,76],[50,76],[70,76]],"edges":[[0,1],[0,5],[1,2],[1,6],[1,7],[1,10],[1,11],[2,3],[2,8],[2,9],[2,11],[2,12],[3,4],[4,5],[4,12],[5,10],[6,7],[6,8],[8,9],[10,11],[11,12]],"polys":[[0,1,2,3,4,5],[1,7,6],[2,8,9],[1,6,8,2]],"start":[[824,523],[918,280],[260,458],[154,590],[913,786],[388,460],[76,64],[583,317],[479,273],[562,739],[135,225],[748,288],[906,719]]},
{"key":"L16","name":"The Snail","fill":"#a0e6b8","pts":[[30,70],[20,46],[34,22],[58,16],[78,32],[78,58],[62,70],[44,40],[60,46],[6,86],[96,86],[92,62],[98,36]],"edges":[[0,1],[0,6],[0,7],[0,9],[1,2],[1,7],[2,3],[2,7],[3,4],[3,7],[3,8],[4,5],[4,8],[5,6],[5,8],[5,10],[5,11],[6,8],[7,8],[9,10],[10,11],[11,12]],"polys":[[0,1,2,3,4,5,6],[9,0,6,5,11,10]],"start":[[343,513],[286,147],[139,548],[161,302],[584,329],[776,624],[672,691],[135,133],[197,817],[618,734],[393,722],[899,218],[679,310]]},
{"key":"L17","name":"The Whale","fill":"#6fb8ff","pts":[[4,52],[14,30],[40,20],[66,26],[80,40],[90,28],[98,10],[96,46],[84,56],[66,70],[36,74],[14,66],[22,46],[26,4]],"edges":[[0,1],[0,11],[0,12],[1,2],[1,12],[1,13],[2,3],[2,12],[2,13],[3,4],[3,9],[4,5],[4,7],[4,8],[4,9],[5,6],[5,7],[6,7],[7,8],[8,9],[9,10],[10,11],[10,12],[11,12]],"polys":[[0,1,2,3,4,5,6,7,8,9,10,11]],"start":[[688,651],[98,570],[912,353],[627,562],[445,510],[263,549],[60,659],[211,444],[766,496],[557,504],[798,622],[501,843],[517,589],[109,363]]},
{"key":"L18","name":"The Stag","fill":"#e8b37a","pts":[[10,6],[26,26],[30,4],[40,32],[60,32],[70,4],[74,26],[90,6],[80,42],[62,52],[58,92],[42,92],[38,52],[20,42],[42,62],[58,62]],"edges":[[0,1],[0,13],[1,2],[1,3],[1,13],[2,3],[3,4],[3,12],[3,13],[4,5],[4,6],[4,8],[4,9],[4,14],[5,6],[6,7],[6,8],[7,8],[8,9],[9,10],[9,14],[10,11],[11,12],[11,15],[12,13],[14,15]],"polys":[[0,1,2,3,4,5,6,7,8,9,10,11,12,13]],"start":[[329,844],[881,455],[540,469],[808,322],[343,496],[420,222],[326,550],[150,363],[381,747],[548,277],[870,203],[881,633],[831,571],[669,683],[734,438],[724,267]]},
{"key":"L19","name":"The Octopus","fill":"#c58cff","pts":[[30,42],[32,14],[50,4],[68,14],[70,42],[92,70],[66,58],[72,94],[56,64],[50,96],[44,64],[28,94],[34,58],[8,70],[42,28],[58,28]],"edges":[[0,1],[0,10],[0,12],[0,13],[0,14],[1,2],[1,14],[2,3],[2,14],[2,15],[3,4],[3,15],[4,5],[4,6],[4,8],[4,15],[5,6],[6,7],[6,8],[7,8],[8,9],[8,10],[9,10],[10,11],[10,12],[11,12],[12,13],[14,15]],"polys":[[0,1,2,3,4,5,6,7,8,9,10,11,12,13]],"start":[[406,757],[577,829],[864,751],[757,910],[294,158],[185,657],[91,855],[79,404],[611,317],[415,243],[742,762],[757,235],[725,639],[615,674],[632,789],[798,299]]},
{"key":"L20","name":"The Dragon","fill":"#5fe0b0","pts":[[4,30],[18,18],[24,2],[30,20],[42,26],[54,4],[62,28],[78,34],[98,18],[90,46],[72,56],[70,84],[56,62],[38,62],[34,86],[26,58],[12,42],[20,30]],"edges":[[0,1],[0,16],[0,17],[1,2],[1,3],[1,17],[2,3],[3,4],[3,17],[4,5],[4,6],[4,13],[4,17],[5,6],[6,7],[6,10],[6,12],[7,8],[7,9],[7,10],[8,9],[9,10],[10,11],[10,12],[11,12],[12,13],[13,14],[13,15],[14,15],[15,16],[15,17],[16,17]],"polys":[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]],"start":[[156,596],[512,298],[375,232],[333,413],[194,924],[860,89],[376,606],[856,200],[868,151],[879,744],[726,780],[789,525],[569,620],[160,721],[311,877],[744,459],[609,351],[343,474]]}
]
```

Level table (all checked in Python, see Sources): n stars, lines, true crossings at the start, 3-star pace (n),
chance that random flinging solves it within n and within 2n moves (3000 runs each), and the sweep bot's moves.

| Sky | Picture | Stars | Lines | Start crossings | ★★★ within | Random ★★★ / ★★ | Sweep bot |
|---|---|---|---|---|---|---|---|
| 1 | The Kite | 6 | 8 | 3 | 6 | 10.6% / 20.5% | 2 |
| 2 | The Paper Plane | 6 | 8 | 4 | 6 | 7.6% / 18.6% | 2 |
| 3 | The Crown | 7 | 9 | 4 | 7 | 12.8% / 20.9% | 1 |
| 4 | The Fish | 8 | 11 | 5 | 8 | 1.1% / 2.2% | 3 |
| 5 | The Sailboat | 9 | 13 | 7 | 9 | 0.3% / 0.8% | stuck at 1 |
| 6 | The Bird | 9 | 13 | 8 | 9 | 0.2% / 0.5% | 2 |
| 7 | The Turtle | 10 | 14 | 8 | 10 | 0.0% / 0.1% | 3 |
| 8 | The Cat | 11 | 16 | 11 | 11 | 0.0% / 0.0% | stuck at 1 |
| 9 | The Rocket | 11 | 16 | 11 | 11 | 0.0% / 0.1% | 6 |
| 10 | The Owl | 12 | 18 | 12 | 12 | 0.0% / 0.0% | 5 |
| 11 | The Fox | 12 | 18 | 14 | 12 | 0.0% / 0.0% | stuck at 2 |
| 12 | The Lighthouse | 13 | 19 | 16 | 13 | 0.0% / 0.0% | stuck at 1 |
| 13 | The Butterfly | 13 | 21 | 18 | 13 | 0.0% / 0.0% | 7 |
| 14 | The Rabbit | 13 | 21 | 17 | 13 | 0.0% / 0.0% | 5 |
| 15 | The Ship | 13 | 21 | 19 | 13 | 0.0% / 0.0% | stuck at 3 |
| 16 | The Snail | 13 | 22 | 19 | 13 | 0.0% / 0.0% | stuck at 1 |
| 17 | The Whale | 14 | 24 | 21 | 14 | 0.0% / 0.0% | stuck at 2 |
| 18 | The Stag | 16 | 26 | 23 | 16 | 0.0% / 0.0% | 7 |
| 19 | The Octopus | 16 | 28 | 27 | 16 | 0.0% / 0.0% | 6 |
| 20 | The Dragon | 18 | 32 | 34 | 18 | 0.0% / 0.0% | 7 |

### The lit picture

On a solve, each star glides to its `pts` spot fitted into the sky. Each `polys` outline fills with a radial gradient
of its `fill` (35% opacity at the centre to 10% at the edge) plus a 2 px soft inner glow of the same colour; all lines
draw gold #ffd166 at 2.5 px; the name (from `name`) sits centred under the picture's lowest star in 26 px (18 px on a
phone) bold rounded type, #f4f1ff. The picture stays lit until Restart, Next or the Star chart.

### Tonight's sky generator (exact, so every device builds the same sky)

```
r = Recess.daily()
lines = []
repeat:                                    # build 6 lines
  t1 = 4*r(); t2 = 4*r()
  if floor(t1) == floor(t2): continue      # both ends on the same side of the square
  p = perim(t1); q = perim(t2); d = q - p  # perim(t): side s=floor(t), f=t-s:
                                           # s0 (f,0)  s1 (1,f)  s2 (1-f,1)  s3 (0,1-f)
  reject if, for any line already kept, |cross(d, d2)| < 0.2079116908177593 * |d| * |d2|   (under 12 degrees)
  reject if any meeting point of two kept lines is within 0.03 of the new line
  keep (p, d); stop at 6 lines; after 400 draws without 6 lines, start over with lines = []
stars: one per pair i<j of lines, in that order (15), at their meeting point
edges: along each line, sort its 5 stars by position along d; join neighbours (6 x 4 = 24 lines)
check: fit the stars into a 1300x620 sky and a 366x690 sky (picture fit, 8% margin); if either has any trouble
       (rules 2), throw it all away and build again from "lines = []", still drawing from the same r
start: Fisher-Yates shuffle of the 15 star ids with r (for i from 14 down to 1: j = floor(r()*(i+1)), swap);
       the star in ring slot k sits at (0.5 + 0.42*cos(a), 0.5 + 0.42*sin(a)), a = 2*pi*k/15 - pi/2, rounded to 4
       decimals; if that ring has no true crossing, shuffle again
```

Only +, -, x, / and sqrt decide which sky is built (no trig until the ring), so all browsers agree; the ring's
cos/sin are rounded to 4 decimals. Python port checked against Node: the first three draws for
`untangle:2026-11-8` match to the last digit (0.332221889635548, 0.7861403457354754, 0.4289726600982249).
Checked in Python for 3650 days from 2026-11-01: every day builds 15 stars and 24 lines, planar (networkx), 0 trouble when fitted on both skies; the ring start has 16 to 133 true crossings (median 72); the rebuild loop ran at most 433 times (mean 44), each a few microseconds of arithmetic, so no cap is needed. An n-move solution (each star once to its web spot, slide rule on) exists every day: in star order on 3649 days, in a shuffled order on the other one.

## Sources and licences

Nothing from any source ships in the file: rules, pictures, levels, generator code and art are all ours. Sources back
the mechanic's history and the maths.

| Source | Read at (2026-11-08) | What it backs | Licence |
|---|---|---|---|
| Wikipedia, "Planarity" | en.wikipedia.org/wiki/Planarity | Tantalo, 2005, from Mary Radcliffe's concept; generator: random lines, a vertex per crossing, an edge per segment between crossings, start on a circle | text CC BY-SA 4.0 (we copy no text) |
| Simon Tatham, Untangle manual | chiark.greenend.org.uk/~sgtatham/puzzles/doc/untangle.html | the same rule ("position the points so that no line crosses another"); credits Planarity by Tantalo | MIT-style licence (doc/licence.html); no code used |
| Wikipedia, "Fáry's theorem" | en.wikipedia.org/wiki/F%C3%A1ry%27s_theorem | any simple planar graph can be drawn with straight lines and no crossings (why a straight-line win always exists) | text CC BY-SA 4.0 |

The genre mechanic (untangle a graph) is not ownable; we use none of Planarity's or Tatham's names, art, levels or
code. Two sources agree on the rule and on Tantalo's credit (Wikipedia and Tatham's manual).

**Python checks run** (scripts in the spec agent's scratchpad, networkx 3.6.1):
- every sky: `networkx.check_planarity` true; connected; picture has 0 true crossings and 0 trouble (rules 2) when
  fitted into 1300x620 and 366x690; the closest pair of stars in any picture is 34.9 px apart (Sailboat, phone).
- every start: true crossings as in the table, trouble above 0 on both skies, all stars at least 34 px apart on both.
- witness: moving each star once to its picture spot (with the slide rule) leaves 0 trouble on every sky: n moves
  always suffice for 3 stars.
- random flinging and the sweep bot (table above); degenerate layouts (below).
- palette contrast (table in The world).
- daily: 3650 days from 2026-11-01, see the generator section.

## Can it be beaten?

| Check | No-skill path | Result and how it is closed |
|---|---|---|
| Win (0 trouble) | Stack all stars on one spot | Closed: the slide rule keeps 22 px between stars; and the count adds a trouble for every pair under 21.5 px. Python: all stars stacked gives trouble above 0 on all 20 skies |
| Win | Line all stars up in a row 30 px apart | Closed: lines overlap their neighbours (angle and 7 px rules). Python: trouble above 0 on all 20 skies; also with a 0.5 px zigzag |
| Win | Shrink the whole layout tiny so lines blur together | Closed: the picture scaled to 15 px wide gives trouble above 0 on all 20 (stars too close, lines within 7 px) |
| Win | Sweep a star through a lucky spot mid-drag | Closed: the win is only checked on a drop |
| Win | Star parked right on a line, or lines just touching | Closed: anything closer than 7 px is trouble (checked: 3 px and 6 px gaps count, 8 px does not) |
| Win | Shrink the window so stars crowd | Closed: count recomputed on resize; crowded pairs show as trouble |
| ★★★ (moves at most n) | Random flinging, n drops | Left open on skies 1 to 3 on purpose (they are the warm-up): 10.6%, 7.6%, 12.8% of runs solve by chance; Sky 4 1.1%, Sky 5 0.3%, Sky 6 0.2%, Sky 7 and up 0.0% |
| ★★★ | Random flinging plus Restart until lucky | Same as above: possible only on skies 1 to 3, slower than thinking. Leaving it is the cost of tiny first skies |
| ★★★ | Sweep each star around, watching the live count, drop at the lowest | Allowed: reading the count and the dashes is the skill. A bot doing this solved 13 of 20 skies in 1 to 7 moves and got stuck in a local knot on the other 7 (those need real planning) |
| ★★★ | Undo to erase bad moves | Allowed and fair: Undo removes the move from the count, the same as never making it; the kept moves are a real solution path |
| ★★ (at most 2n) | Random flinging | Skies 1 to 3: 18.6% to 20.9%; Sky 4 2.2%; Sky 7 and up 0.1% or less |
| Best score board | Replay the same sky with the answer known | Allowed: hand-made skies are fixed; a better second run is learning. Local device only |
| Daily | Replay today's sky after solving | Allowed: per-day key, local only; tomorrow's sky is new |
| Initials board | Spam initials | Shell-owned, local top 10 per sky; nothing leaves the device |
| Stars total | Earn stars on the same sky again | Shell keeps the best stars per key, never adds them up twice |

## Not like

- **Go, Chess, Checkers** (Recess): opponent games on a fixed grid; Untangle has no opponent and no grid, and the
  pieces are moved freely in 2D.
- **Cargo Hold** (`sliding-blocks`, Recess): also scored in moves, but crates slide along grid rows to free one
  hatch; here any star goes anywhere and the goal is a layout with no crossings.
- **Sky Dome** (Curiosity, `tools/sky-dome`): the real sky and real constellations; Untangle's stars are invented and
  never claim to be real.
- **Circle Theorem Explorer, Intersection Quest** (classroom tools, grep of `tools/` for crossing and intersection):
  they drag points to see a theorem hold or solve equations; no tool or Curiosity does untangling or planar graphs
  (grep for planar and untangle: none).

## Art list

| Item | Made how | Size | Use |
|---|---|---|---|
| Night sky backdrop | **Painted**: a deep indigo night sky, soft violet and teal nebula clouds drifting across, a scatter of faint tiny distant stars, painterly, dark enough that white points and thin lines read on every part of it; no constellations, no lines, no text | 1920x1200, WebP q70, about 180 KB | full-window background, `object-fit: cover`, behind the field |
| Stars, lines, dashes, rings, picture fills, names, beams, specks | drawn in code (SVG) | | they must sit exactly on the puzzle's coordinates |
| Knot icon, four-point star icon, star-map icon | drawn in code (SVG, 20 px) | | readouts and the Star chart button |
| Star chart tiles | drawn in code from each sky's data | | thumbnails of start or lit picture |

One painted image. The pictures are drawn in code on purpose: a painted creature could not line up with the stars at
every sky size, and the drawn outline is what makes it a constellation.

**Size budget** against the 2 MB goal: shell (kit:recess) about 14 KB, game code about 35 KB, sky data about 9 KB,
painted backdrop about 180 KB. Total about 240 KB.

## notes.md

```
# Untangle: a note for grown-ups

What it is: a puzzle game. Each sky is a set of stars joined by straight lines, all tangled up. Your child drags the
stars until no two lines cross. When the last crossing clears, the stars glide into a hidden picture: a kite, a fish,
a fox, a whale, a dragon. There are 20 skies that grow from 6 stars to 18, plus a new sky every day.

What it builds: seeing shapes in space and planning a move before making it. Underneath, it is a real idea from
mathematics called graph theory: dots (vertices) joined by lines (edges). A drawing where no lines cross is called
planar, and every sky in this game can be drawn that way. Mathematicians, map makers and computer chip designers all
work on this same question: can these connections be laid out flat without crossing?

How stars work: three stars if the sky is solved in about one move per star, two stars within twice that, one star
for any solve. Undo and Restart are always free. There is no timer.

Things to try together: count the crossings before you move anything. Which star is in the most trouble? Can you
solve a sky, then solve it again in fewer moves? On the daily sky, after it lights up, look at the six straight beams:
the whole tangle was made from just six straight lines.

Privacy: everything saves on this device only. No accounts, no ads, nothing sent anywhere. High scores use three
initials, never a name.
```

## Done when

1. Every sky in Content loads with its exact start, and the picture it lights into matches its `pts`, `edges` and
   `polys` (spot-check Skies 1, 10, 20 against the data).
2. The count shown equals the rules: a 3 px and a 6 px gap count, an 8 px gap does not; two lines meeting at a star
   do not count unless under 4 degrees.
3. The picture lights only on a drop with 0 trouble; holding a star over a 0 spot shows "No crossings" but does not
   win until dropped.
4. Stacking, a straight row and a tiny cluster never win (try each by hand on Sky 5).
5. Crossed lines are dashed and ringed in calm mode too; with colour removed (greyscale), crossed and clear lines
   still differ.
6. Moves: a drop back in place is not a move; Undo lowers moves by one; Restart returns to the exact start with moves 0.
7. Stars: 3 at n moves or fewer, 2 at 2n or fewer, 1 otherwise; the readout's "within" number changes from n to 2n
   once moves pass n.
8. Tonight's sky is identical on two browsers on the same day (compare the first three star positions) and has 15
   stars and 24 lines; solving it shows the six beams.
9. 1366x768: the whole sky, the bottom strip and the shell bar fit with no scroll; 390x844 the same; the Star chart
   fits without scrolling on both.
10. Keyboard only: Tab to a star, Enter, arrows, Enter solves Sky 1; Escape cancels a lift; C opens the Star chart.
11. Touch: a star is easy to lift with a finger on a phone, the halo shows around the finger, and the page never
    scrolls or zooms while dragging.
12. Playtest: three kids aged 8 to 13 each finish Skies 1 to 10 in 30 to 90 seconds a sky (median); adjust nothing
    in the data without rerunning the Python checks.
13. One file, offline, under 300 KB; no fetches.

## Open questions

1. **The name.** "Untangle" is the genre's plain name and GAMES.md uses it, but it is also the title of one puzzle in
   Simon Tatham's free collection. Default: keep "Untangle" (a common word, no shared art or code); the fallback
   would be "Star Knots".
2. **Daily size.** Tonight's sky has 15 stars and 24 lines, bigger than the 30 to 90 second skies (about 2 to 3
   minutes for a kid). Default: keep 15 as the day's treat; 10 stars (5 lines) is the smaller option.

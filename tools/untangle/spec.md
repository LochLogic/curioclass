# Untangle (Recess game)

Drag the stars of a tangled night sky until no two lines cross, then watch them glide into a picture.
20 hand-made opening skies, a ladder of 550 generated skies in 22 painted worlds that grows steadily harder, and a
new sky every day.

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

**Painted first (Cory, 2026-11-08, CODEX-RECESS.md "Visually amazing").** Everything a kid looks at is painted except
the exact geometry. Painted: the night sky backdrop of every world (23 scenes: the First Skies and 22 worlds, each its
own landscape under the stars), the star sprites (warm glints with a soft halo, placed exactly by code at each star's
coordinates), the constellation pictures that light up on a solve (20 hand-made skies plus one per world), and the box
art. Code draws only what must sit on exact coordinates: the lines, the dashes, the crossing rings, the gold solved
lines, hit areas and focus rings. Those code layers take the painting's light: lines get a soft outer glow in their
own colour, gold lines a warm bloom, rings a faint halo, so they read as light in the painted sky, never as a diagram
laid on top. The art list below is a floor, not a ceiling.

**Paintings keep the contrast.** Every backdrop is painted dark: behind the sky field no area brighter (relative
luminance) than #1b1f5e that is more than 8 px across at 1366x768, checked in Python on the WebP by the builder; if a painting fails, it is
repainted or a #0a0b26 veil at up to 40% sits over it. The palette's contrast table below then holds on every world.

**Light.** The only light is the stars and the lines. A crossed line burns a hotter coral and goes dashed; a solved
sky turns every line gold and fills the picture with a soft nebula colour.

**Materials.** Stars feel like glass beads of light: they swell when lifted, settle with a tiny bounce when dropped.
Lines are taut threads: they stretch with the star, never sag.

**The grab moment.** The last crossing clears: all lines flash gold, the stars glide (900 ms, ease in-out) from
wherever you left them into the picture, the painted constellation blooms in behind them, its name rises under it
("The Whale"), then the shell's win card. On a ladder sky the stars glide into the true shape the sky was built from
(a net, a web, a lantern), its outline fills with the world's glow and its name card rises ("The Silver Web" for R003); the
last sky of each world also blooms that world's painted constellation (see The ladder).

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

Picture fills (one per hand-made sky, one per world for the ladder) sit under the painted picture as a soft glow
inside its outline; the painted constellations and fills are decoration on a solved sky, never information.

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

Three kinds of sky: the First Skies (20 hand-made), the Ladder (550 generated, in 22 worlds of 25) and Tonight's sky
(one a day). Every sky is open from the start (no gates); the Star chart marks the first unsolved one.

**First Skies (20 hand-made levels).** Keys `L01` to `L20` for `Recess.level(key, label)`. Label is `Sky 7` until that sky
has been solved once on this device (stored with `Recess.store('named:L07', true)`), then `Sky 7 · The Turtle`, so
the picture stays a surprise the first time. Star counts rise 6, 6, 7, 8, 9, 9, 10, 11, 11, 12, 12, 13, 13, 13, 13,
13, 14, 16, 16, 18; lines rise from 8 to 32; the start's true crossings rise from 3 to 34 (table in Content).

**The Ladder (550 generated levels, 22 worlds).** Keys `R001` to `R550` (ladder position, three digits; `R1000` and on
if it ever grows that far). Each world is 25 levels: World w holds R(25w-24) to R(25w). Label `<world name> <place in
world>`, for example `Lantern Garden 12` for R162, and once solved on this device (`Recess.store('named:R162', true)`)
`Lantern Garden 12 · The Wandering Snowflake`. Every ladder sky comes from an 8-character record in a packed table and a
deterministic generator (Content, The ladder); the builder re-verifies all 550 against two SHA-256 checksums.

What rises through the ladder (all measured in Python, per-world table in Content):

| Knob | World 1 | World 11 | World 22 |
|---|---|---|---|
| Stars | 9 to 15 | 17 to 25 | 28 to 36 |
| Lines | 11 to 30 | 21 to 64 | 57 to 85 |
| True crossings at the start | 10 to 31 | 58 to 178 | 402 to 624 |
| Stars the scramble moved | 3 to 13 | 6 to 24 | 16 to 36 |
| Shape families | net, web, lantern | net, web, lantern | net, web |
| Difficulty D | 3.0 to 3.5 | 13.4 to 15.4 | 69.2 to 80.0 |

**One difficulty number, D, never drops.** D is the expected number of moves a sweep player needs (a player who drags
each star around, watches the live count and drops it at the lowest spot), predicted from four knobs:

`D = exp(0.82 + 1.66 ln(1 + X/n) + 0.16 ln(n) - 0.79 m/n) - 1`

with n stars, m lines and X true crossings at the start; the shape family enters through m/n (nets are sparse, webs
and filled-in nets dense, lanterns in between) and was measured to add nothing further (family terms 0.27 or less in
the fit, dropped). The coefficients come from a least-squares fit of ln(1 + bot moves) on 1015 candidate skies across
every family and size (R² 0.82), then rounded. On the shipped ladder D runs from 3.0 (R001) to 80.0 (R550), rising
about 0.6% per level (about 16% per world, a geometric curve, so each world feels a similar step harder than the last),
and D(R k+1) is at least D(R k) for every k (2 exact plateaus, no drops). Validation: the greedy sweep bot (3 runs per
level) agrees with D in rank order (Spearman 0.84 over all 550); its median moves per world rise from 4.0 (World 1) to
91.3 (World 22). For comparison the bot needs 1 to 9 moves on the First Skies, so World 1 starts at about the level
of Skies 10 to 20 and climbs from there.

Shape families (the true shape each sky is built from; Content has the exact generator):

| Family | Built from | Kid-facing name card nouns |
|---|---|---|
| Net (`g`) | a grid of stars joined to their neighbours, some cells crossed by a diagonal (a filled-in net is a triangulated grid; 2 rows make a triangulated strip, which is outerplanar) | Net, Quilt, Window, Garden ... |
| Web (`w`) | a hub star, rings of stars around it, spokes; some web cells crossed by a diagonal (1 ring is a wheel) | Web, Wheel, Flower, Sun ... |
| Lantern (`p`) | a ring of stars (a cycle) with some non-crossing chords inside (all chords: a maximal outerplanar graph) | Lantern, Crystal, Shell, Fan ... |

Lanterns top out around D 24 on a phone-sized sky, so Worlds 16 to 22 are nets and webs only; Worlds 1 to 14 hold
8 to 10 of each family, never the same family twice in a row and never the same build within 12 levels.

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

Every sky has a pace p, a measured number of moves: on the First Skies and Tonight's sky p = n (the number of stars);
on a ladder sky p = the number of stars the scramble moved (n when the whole sky was scrambled), because moving each
of those once straight back to its home spot solves it (the witness, checked for all 550 with the slide rule on both
sky sizes). So it is the same rule everywhere: about one touch per star that is out of place.

| Stars | Rule | Shown in the readout as |
|---|---|---|
| 3 | moves at most p | `★★★ within 9` |
| 2 | moves at most 2p | `★★ within 18` once moves pass p |
| 1 | any solve | nothing extra once moves pass 2p |

"About one touch per star" is a pace any kid can understand. It is always reachable: moving each star once straight
to its spot in the picture solves every First Sky and the daily in n moves, and every ladder sky in p moves (checked in
Python with the slide rule). Good planners beat it: a sweep-and-watch bot solved 13 of 20 First Skies in 1 to 7 moves
(Can it be beaten?), and 408 of the 550 ladder skies within p.

**Next.** After Sky N, Next opens Sky N+1; after Sky 20, R001; after R k, R k+1; after R550, the Star chart. After
Tonight's sky, Next opens the first unsolved sky (First Skies, then the ladder), or the Star chart if none is left.

## Screens and controls

**On load.** The first unsolved sky opens at once (First Skies in order, then R001 on; Sky 1 on a first visit), with
its world's painted backdrop (the First Skies share one), tangled, with the hint line in the bottom
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
4 px), live count updating; Enter or Space drops; Escape puts it back. `C` opens the Star chart (inside it, `W` flips to the
worlds overview). The shell owns U (Undo), R (Restart), M (Sound), S (Scores) and Ctrl+Z; the game binds no other
letters. After each drop an aria-live
line reads the count: "3 crossings left" or "No crossings. Solved!".

**Kind feedback.** There is no fail. What is off is always on screen: dashes and rings. A stall helper: after 6 drops
in a row that do not lower the count, the star touching the most dashed lines gets a slow gold ring and the hint line
says "Try the star with the most dashed lines." (once per attempt, gone on the next drop that lowers the count).
A drop that slides away from another star shows once per attempt: "Stars need a little room."

**Star chart** (game-owned overlay, opened by its button or C, closed by Escape, its Back button, or picking a
sky). A dark card over the sky, paged so 570 skies never make a wall or a long scroll. It always opens on the page
that holds the current sky.

- **A page** is one world (or the First Skies). Header: `‹` button, the world's name and number ("Lantern Garden ·
  World 7 of 22"), its star total ("41 of 75 ★") and `›` button; under it the page's tiles. A strip of the world's
  painted scenery runs behind the header.
  - First Skies page: 20 sky tiles plus a wide Tonight's sky tile. Chromebook: 5 x 4 tiles of 104 px, daily tile
    under. Phone: 4 x 5 tiles of 70 px, daily tile under.
  - World page: 25 tiles, 5 x 5. Chromebook 104 px tiles; phone 62 px tiles (5 x 62 + 4 x 6 gap = 334 px, inside
    the 366 px field). The 25th tile is a little larger frame with the world's painted constellation, dim and
    silhouetted until that sky is solved.
- **The Worlds button** (top right of the card, also the key W while the chart is open) flips to the overview: 23
  world tiles (First Skies plus 22), each a crop of that world's painted backdrop with its number, a progress ring
  (skies solved of 25) and, once its last sky is solved, its painted constellation. Chromebook 6 x 4 tiles of 150 x
  96 px; phone 4 x 6 tiles of 80 x 80 px (numbers only, the name in the tile's aria-label and shown on focus). Picking
  a world opens its page.
- **Keys:** arrows move between tiles, PageUp and PageDown (and `‹` `›`) change page, Home jumps to the page with the
  first unsolved sky. Swipe left or right on the tile grid changes page on a phone.
- **A tile.** Unsolved: its tangled start as tiny dim dots and lines and the place number ("12"); solved: its true
  shape in gold, and its stars from `Recess.stars(key)`. The first unsolved tile has a gold outline. Tiles are buttons
  (Tab, Enter). A page draws only its own 25 thumbnails (each generated on demand from its record, under 1 ms), so
  the chart stays quick.

Both layouts fit without scrolling at 1366x768 and 390x844.

**Undo and Restart.**

| | First Skies and ladder | Tonight's sky | After a solve |
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
| Solve | lines flash gold, stars glide 900 ms into the picture (ladder: into the true shape), the painted constellation (ladder: the world's glow in the outline) fades in 500 ms, name rises 12 px and fades in, then `Recess.win` at 1.6 s (a world's 25th sky: the world's painted constellation then rises behind the shape over 600 ms, `Recess.win` at 2.2 s) | one chime per star as it lands (40 ms apart, rising notes, volume capped), then the shell's `win` | gold lines, 200 ms cross-fade to the picture, name appears, `Recess.win` at 0.4 s; chimes still play |
| Daily solve | as above, then the six beams sweep across the sky for 1.5 s | as above | beams appear and fade |
| Background | the world's painted backdrop with a slow parallax drift (2 layers: the scenery and a sheer nebula layer, at most 12 px over 40 s), plus 60 tiny specks drawn in code that twinkle slowly (opacity 0.3 to 0.8, 3 to 7 s) | none | backdrop still, specks still |
| New world | the backdrop cross-fades to the next world's painting over 800 ms; the world's name floats in for 1.5 s | `Recess.play('pop')` | 200 ms cross-fade, name shown |

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

On a solve, each star glides to its `pts` spot fitted into the sky. The sky's painted constellation (Art list:
`art/sky-L07.webp` and so on) fades in, placed with the same fit as the stars: it is painted on a 1000 x 1000 canvas
where grid point (x, y) of `pts` sits at pixel (10x, 10y), so the painting's bright points land under the stars at
every sky size (painted from a guide image of the `pts` and `edges`; the builder checks each star lands within 12 px
of a painted glint at 1366x768). Each `polys` outline also fills with a radial gradient of its `fill` (35% opacity at
the centre to 10% at the edge) under the painting; all lines draw gold #ffd166 at 2.5 px with a warm bloom; the name (from `name`) sits centred under the picture's lowest star in 26 px (18 px on a
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

### The ladder (550 generated skies, exact)

**Decision: generated at dev time, shipped as a packed table of seeds and parameters.** Each level is an 8-character
record: the shape family, its size, how filled-in it is, how many stars the scramble moved, a seed digit, and the
start's true crossing count as a check value. The game rebuilds the sky from the record with a short deterministic
generator (integers only, apart from rounding cos and sin to whole numbers). This is the smallest safe form: 8 bytes
per level, 800 bytes per 100 levels, 4,400 bytes for all 550 (under the 10 KB line, so the table lives here and no
`ladder.txt` is needed). A fully drawn-out table for the same 550 measured 96 KB bit-packed (129 KB as base64; 323 KB
as plain text), with nothing gained: the spec's Python and an independent Node port of this text build byte-identical
levels (checksums below). The table is append-only: a shipped record never changes and a new level only joins at the
end as R551 and on (harder than R550), so `Recess.level` keys and the stars kids earned stay put.

**Record.** 8 characters, base 36 digits `0-9a-z` (digit value = index in `0123456789abcdefghijklmnopqrstuvwxyz`):

| Char | Field | Meaning |
|---|---|---|
| 1 | f | family: `g` net (grid), `w` web, `p` lantern (polygon) |
| 2 | a | net: columns; web: spokes k; lantern: stars k |
| 3 | b | net: rows; web: rings R; lantern: always `0` |
| 4 | e | extras: diagonals (net, web) or chords (lantern) |
| 5 | s | stars the scramble moves; `0` means all of them |
| 6 | seed | seed digit |
| 7 and 8 | X | true crossings at the start, X = 36 x char7 + char8 (the builder's check value) |

**Generator** (exact; `r = Recess.rng('untangle:' + record.slice(0, 6))`, the shell's own seeded random; every draw
below happens in exactly this order, including draws whose result is not used):

```
round(v) = floor(v + 0.5)                      # Math.floor(v + 0.5) in JS; not Python's round()
shuffle(L): for i from len(L)-1 down to 1: j = floor(r() * (i+1)); swap L[i], L[j]       (as the daily's)
ring(j, i, k): t = 2*pi*i/k - pi/2; (round(1000*j*cos(t)), round(1000*j*sin(t)))

NET g (a columns, b rows):   star id(x, y) = y*a + x, shape spot (1000x, 1000y)
  lines: every row left to right (id(x,y), id(x+1,y)), rows top to bottom; then every column (id(x,y), id(x,y+1)),
         y outer, x inner
  cells: (x, y) for y in 0..b-2, x in 0..a-2 (y outer); shuffle(cells); then one bit per cell in shuffled order:
         bit = r() < 0.5 (all cells draw a bit); the first e cells get a diagonal:
         bit ? (id(x,y), id(x+1,y+1)) : (id(x+1,y), id(x,y+1))
  outline: top row left to right, right column down, bottom row right to left, left column up
WEB w (k = a spokes, R = b rings):  hub id 0 at shape spot (0,0); id(j, i) = 1 + (j-1)*k + (i mod k) at ring(j, i, k)
  lines: hub spokes (0, id(1,i)) for i in 0..k-1; ring loops (id(j,i), id(j,i+1)) for j in 1..R, i in 0..k-1;
         radials (id(j,i), id(j+1,i)) for j in 1..R-1, i in 0..k-1
  cells: (j, i) for j in 1..R-1, i in 0..k-1 (j outer); shuffle; one bit each as for nets; first e get
         bit ? (id(j,i), id(j+1,i+1)) : (id(j,i+1), id(j+1,i))
  outline: the outer ring, i = 0..k-1
LANTERN p (k = a stars):  star i at ring(1, i, k); lines (i, (i+1) mod k) for i in 0..k-1
  chords: L = [0..k-1]; while len(L) > 3: i = floor(r() * len(L)); chord (L[i-1 mod len], L[i+1 mod len]);
          remove L[i]. This makes k-3 chords (always all drawn); keep the first e.
  outline: 0..k-1
every line is stored as (smaller id, larger id), in the order made.

HOMES (the scramble's frame, thousandths of the sky, the stretched true shape):
  W = max x - min x, H = max y - min y over the shape spots
  home(i) = (80 + floor((1680*(x - minx) + W) / (2W)), 80 + floor((1680*(y - miny) + H) / (2H)))
SCRAMBLE:
  order = shuffle([0..n-1]); moved = the first s of order (all n when s = 0); the rest sit at their homes
  slots = shuffle([0..99]); slot q sits at (80 + 93*(q mod 10), 80 + 93*floor(q/10)) thousandths
  for each moved star v in order: take slots from the shuffled list in turn (a slot that fails is skipped for good)
     until one is at Chebyshev distance >= 93 (max of |dx|, |dy|, thousandths) from every star placed so far
     (unmoved stars at their homes and moved stars already given slots) and from v's own home; v starts there
  start = each star's position, thousandths (the same form as the First Skies' `start`)
```

Integers decide everything except `ring`: cos and sin times 1000 are rounded to whole numbers, and across every ring
point the ladder uses the closest any value comes to a .5 rounding edge is 0.00085, millions of times larger than any
engine's floating-point difference, so all browsers build the same stars. Web and lantern shape spots are those
rounded integers.

**The true shape on a solve** (the reveal target, not the scramble's frame): the shape spots fitted into the sky like
a First Sky picture (scale = min of the two axis fits, 8% margin, centred), turned a quarter turn first (x, y) to
(y, -x) when the sky is portrait and the shape is wider than tall, or the sky is landscape and the shape is taller
than wide. All 550 checked on 1300x620 and 366x690: 0 trouble (rules 2), stars at least 33.3 px apart.

**Worked example, R001 = `g522040d`.** f `g` net; a `5` columns; b `2` rows; e `2` diagonals; s `0` (all 10 stars
moved); seed `4`; X = 36 x 0 + 13 (`d`) = 13. `r = Recess.rng('untangle:g52204')`, first draws 0.9726372351869941,
0.4953342501539737, 0.2729168273508549. It builds 10 stars and 15 lines: rows (0,1) (1,2) (2,3) (3,4) (5,6) (6,7)
(7,8) (8,9), columns (0,5) (1,6) (2,7) (3,8) (4,9), diagonals (3,7) (1,5). Shape spots (0,0) to (4000,1000).
Moved order 9, 7, 2, 0, 1, 8, 4, 6, 5, 3. Start (thousandths, star 0 to 9): (917,80) (452,266) (359,266) (545,545)
(824,359) (731,359) (545,638) (359,173) (731,824) (545,731), with 13 true crossings; pace p = 10. Second check,
R002 = `pa023h0a`: a lantern of 10 stars with chords (2,4) (5,7), 3 stars moved (5, 4, 0), 10 crossings, p = 3.

**Checksums** (the builder recomputes both):
- SHA-256 of the 550 records joined with no spaces or newlines (4,400 characters):
  `677f292415a7264a81578f4d1cdb36e4d470aaf0a33cccb343d419fabd0e8884`
- SHA-256 of the generated levels, one line per level ending in `\n`, fields joined by `|`:
  `key|n|lines as u,v joined by ;|true-shape spots as x,y joined by ;|start as x,y joined by ;|moved ids joined by ,`
  (R001's line begins `R001|10|0,1;1,2;2,3;`):
  `2be9e60bcfc3865508214b4ac18040ad19fca26c4efadb0d83051e5945b65b49`

Both match between the Python generator and an independent Node 24 port written from this text.

**The packed table** (550 records, R001 first, 10 per line; whitespace is not part of the table):

```
g522040d pa023h0a w810000f g726430m pd020x0c w6236v0q g433450i pd0a4e0l w6264g0v g432400h
pc07020h w624020s g622030g p902080a wb106g0l g522090e pd00010b w8100t0g g5200h0c pb060c0g
w910050i g3330t0f pb000a0a w5243g0q g5384j0u pf0c4h0q w6264k0x g620020f pc09070l w521300m
g522060f pd00060c w724480y g521030e pe000j0d wb10010n g534420q pf000h0e w7208p0t g5364b0t
pc040h0g w626420z g4334k0l pe067c0k w624680w g432440k pd080v0m w7204a0u g6220d0j pf008x0f
w5210d0o g4498e11 pc04410h w5253n0v g5308m0n pc02060f w910040l g522070h pd0a460q w5385i1b
g521020g pg03080k w6264q12 g5304v0o pc04000i w520610o g432690m pe084x0p w5305l0z g536bt0x
pd00080f w8245u18 g433410o ph000r0j w8208812 g6204m0j pc070n0n w6224c0x g4478012 pb080k0o
w8205913 g726410v ph008l0k w5206g0q g7234d0r pc076g0o w820dl14 g7224w0q pg038n0n wb10020t
g534450x pg00000k w6236511 g5384h14 pc00020g w7244v18 g724050u pf09880v w6224y10 g4360p0w
pd02at0k w6204o0x g430070n pc076j0q w622a711 g6305n0z pf06830s w828581n g5364f13 pe0b0c0z
w626471a g5324s0x pf0c4n12 w5325i1a g4425r10 pc04060n w7220o18 g6309311 pf0c8b13 w535561h
g430000p pf064k0u w5305h18 g4475w1a pf09890z w6366i1s g8245g12 pd05a70r w6200d11 g449511f
pj0c6p19 w7208v17 g538421b ph0e0e1b w538541r g7230k0y pi000p0s w9246l1r g54cax1w pe00080n
w623at19 g546ah1l pe08070z w8245e1n g7240211 pk08a717 w7244s1i g538b51e pf06bj0y w53a5020
g7244212 pf038x0u w5325z1i g549a91u pk0da01h w724871k g5406y1e pf0c0b1a w7258b1n g7220210
pf090015 w8288421 g536011d pi0b911d w6366l23 g6350x1j pg0d0a1f w8248k1t g7366s1t ph070g16
w7274b1v g5324c17 pk0h6b1t w924ae21 g5300314 pk040z17 w7240z1p g7220h13 pe087415 wa2a622o
g825541e pi0b961h w8208s1o g5436h1q pf060014 w5385125 g8200316 ph0a0a1f w724851s g444841i
pf030u10 wa20a424 g7366g20 pk0ha41z w630631y g730gf1p pi040x18 w7250a1x g440831c ph07031c
w5308r1p g8278x1n pj04031b wa25682k g5380i1r pl00gj19 wb287e30 g5368h1n pg030e15 w5358624
g4490z1z pj04aj1d w5328e1x g8270s1q pl000f1b w53a5h2l g7330s21 ph078e1g wb2b7k3e g8250l1n
pg0ac51l wb267g31 g4440y1q pk00021b wb287638 g632ek1s pi089a1m w6336w2g g447031z ph04d01d
w73ab43d g830i729 pg0a0e1o w5385x2l g83e7c38 pm000t1i w5380z2m g6300q1r ph0e8q21 w5328g25
g8240u1q pj08031s w8260d2m g820061i pk04f81n w929an35 g540f122 pi00011c w9226j2l g730gp25
ph070p1o w922az2m g5430f2b pk0hai2j w73e7043 g648c534 pi0b0x21 wc298240 g7300128 pl000b1m
w734bf39 g546fy2m po00051u wb260j3l g83ac23b ph07dj1s w9246x2y g549fp2x pj0ge92k wb20c336
g73c6r39 ph040g1n w83g8l4y g64fc43y pl000y1q w730bw34 g648cw3e pi000z1j w633ah30 g554cv39
pi04er1s w630au2s g543aw2m pi080922 wb287843 g63a9i2y pi08e023 w63c6441 g736a62z pk040f20
w730b33b g64bce3v pj0c002i w924al3a g6350t2m pk0ha030 wc26cf4d g8340g3a pj04eb20 w922ei36
g54ca03m pm00gq21 w838ce4o g540fb2m pi0f0b2t wa20gq3d g73c0q3r pl000t20 w838804s g7300r2r
pj08ei2e w633633f g7360n3a pn00h128 w83cc85c g8340a3j pk08072j w73ab24q g8300v39 pk04002a
w83g8q5y g7330r35 pk04fc2b w73a784u g54cac3z pj0c0b2v w73e7c5e g550j93m pj0ge339 wb2bce58
g5400r2x po000j2i wa220u3y g55c8d4u pk0df235 w630043g g55ccw4w pk0h023k w73eb65n g64fcb54
pk0d0q38 wc29cn5k g6440d41 pk080n2u wb20h94a g5500o3w pk0hfd3p wc230150 g54caj4d pk08f42x
wb26cr52 g736gs3u pm00ga2j w73eba5z g7330e3l pk0h0t3t wc298k5w g550j743 pk0dft3h w73ag45k
g736033z pk0dah3i wc2cce6f g64fc75m pk0d0o3k wb2bc860 g64bci57 wa250f4w g74e8t68 wb20h44q
g5500l4b wb26hb5h g736gp46 wc2c8n6p g8300x43 w93iee86 g83a0856 w838j569 g550jb4g wa2a005t
g5540q4w wb230h5b g65f9r73 w73ebq6p g558jd5f wc298m6l g55c8e5y wb2bci6j g83eii5x wc26cb6a
g74eef6s wb260g5x g64bc15r w830co5m g55ccz65 wa25aa5g g739064y w730gb52 g55gc86s wb230m5p
g55c0o6a wc29j470 g64fiw6j w830j75u g648iw5n w83gck88 g8340053 wa35gd7w g65ffa7u w7340c5u
g83eih6g wc26cp6u g83aiy5y w737gl6d g655f86q w934e77c g64f096w wc29cz7g g64bi46d wa30gi7l
g744lg6b wb26hn6n g83e0s6r wb230d69 g65a0q7n wb280x72 g834025i wa3fgia3 g7400q61 wb20hg5z
g8370g5z w838jw7p g7440d6m wa35g98q g830it57 wc200e6m g845of7p wa30nf85 g74e0c86 wb28ht7g
g74i858v wa3agr9s g65af887 wb2bhc83 g650036x w930lc7n g55c0c7i w834c77j g834iw60 wa30gd8j
g64b0177 wb2b0n8c g84aom8w w83gjz9v g83aik70 wc29028m g84a0v91 w93eemad g84ggya1 wc23jl7q
g840gq7s w93elsaj g74il49n w838cn8p g64fic8a w83cj99i g8450e8n wc26ja8h g740lc72 w83g0bah
g650mw7o w83gj5ak g64bit7u wc26078o g655mt8i wa3anyb5 g84aof9r w8300e7s g558j17t w83c0ba1
g744lf7z w939etad g6440370 wa3kg4dj g75oiadf wa3k9xdn g648027r wc29jk9q g74ilran wc23j98o
g65a0r9v wa30gfa1 g5540h7l w930lp97 g55gj09s w934ej9z g750ig9v wa3agtc4 g84a0kam wc2c0cat
g55c0n98 wc260p9n g84aosas w93i0zd9 g74i0fbb wc2cjsb2 g65f00bf wc230x9a g74ilebh w93e04cm
g66cigcr wa3kn4f1 g55gjoah w83gjjcd g74ellax wa35gaby g75c0tcq w9300ga3 g8400w9r wa300nb6
g66pitfx w9390uc2 g756qgbx w93ilqea g66pr3g6 w9340pb6 g6660qcg w93e0zdi g66jr0f3 wa3a0ddo
g74i0och wa3fgeey g7560mce w939l2cm g666r9cu wa3k0ngi g66cr3e3 w93i0sf1 g8450mbf wa3anae7
g66prbh6 w934labw g75cqre2 w93el7ec g75i00fg wa3fgrfr g84gote1 wa35nmdi g65amgcb wa3k0ihc
```

**Verified for every one of the 550 in Python** (networkx 3.6.1): built from the record alone, the start's true
crossings equal X; the graph is planar, connected, every star has at least 2 lines; the true shape and the home
layout have 0 true crossings, and 0 trouble (rules 2) on 1300x620 and 366x690; the start has trouble above 0 on both;
stars at least 34 px apart at the start and 33.3 px in the true shape and home layouts on both; the witness (each moved
star once to its home, slide rule on, both skies) solves it in p moves; D never drops; the 550 records are distinct.
Same family twice in a row: never. Same build (record's first 5 characters) twice within 12 levels: never.

**Name cards.** The j-th ladder sky of a family (j counted from 0 in ladder order) is named
`The <ADJ[j mod 24]> <NOUN[(j + floor(j/24)) mod 12]>`, so names stay unique through all 550 (214 nets, 214 webs, 122
lanterns; checked: 550 different names).

```
ADJ:     Silver Sleepy Quiet Bright Little Wandering Northern Glowing Hidden Brave Gentle Shining Dreaming Frosty
         Golden Velvet Midnight Humming Drifting Sparkling Lucky Patient Secret Twinkling
NET:     Net Quilt Window Garden Ladder Map Weave Fence Bridge Raft Basket Kite
WEB:     Web Wheel Flower Sun Shield Compass Daisy Snowflake Umbrella Clock Pinwheel Spiral
LANTERN: Lantern Crystal Shell Fan Gem Locket Ring Bell Drum Bubble Coin Mirror
```

**The ladder reveal, without 550 paintings.** Every ladder solve: lines flash gold, the stars glide into the true
shape (a net, a web or a lantern, which reads as a pleasing, even pattern after the tangle), the shape's outline fills
with the world's fill colour as a soft glow (35% to 10%, the First Skies' recipe), the name card rises ("The Silver
Web" for R003). The 25th sky of each world is that world's finale: after the shape settles, the world's painted constellation
(22 paintings, one per world, a creature or thing drawn in starlight) rises behind it and stays on the world's tile in
the Star chart. So a kid meets a new painted picture every 25 skies on top of the 20 hand-made ones, and every sky
gets its own named shape.

**Worlds.** Each world has its own painted backdrop (the scenery under the night sky), its fill colour (decoration
only, contrast not needed) and its finale constellation. Names and pictures are invented; none is a real
constellation.

| # | World | Skies | Painted scenery | Finale constellation | Fill | D | Stars | Lines | Start crossings | Nets/webs/lanterns | Bot median moves |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | First Skies | L01 to L20 | the night sky over a quiet hill (the current backdrop) | 20 hand-made pictures | per sky | | 6 to 18 | 8 to 32 | 3 to 34 | | 1 to 9 |
| 1 | Firefly Meadow | R001 to R025 | tall summer grass, fireflies drifting low | The Firefly | #ffe08a | 3.0 to 3.5 | 9 to 15 | 11 to 30 | 10 to 31 | 9/8/8 | 4.0 |
| 2 | Pine Hollow | R026 to R050 | dark pines around a clearing, a woodpile | The Hedgehog | #a0e6b8 | 3.5 to 4.0 | 10 to 15 | 13 to 32 | 12 to 35 | 8/8/9 | 3.7 |
| 3 | Reed Lake | R051 to R075 | still lake, reeds, the sky mirrored | The Heron | #9ad7ff | 4.0 to 4.7 | 10 to 17 | 13 to 38 | 15 to 47 | 8/9/8 | 4.0 |
| 4 | Lily Pond | R076 to R100 | lily pads, glowing water, a stone bridge | The Frog | #7ee0a0 | 4.7 to 5.4 | 11 to 17 | 12 to 32 | 16 to 44 | 9/8/8 | 4.0 |
| 5 | Coral Shallows | R101 to R125 | shallow sea over pale coral, a sandbar | The Seahorse | #ff9e6b | 5.5 to 6.3 | 12 to 18 | 15 to 40 | 20 to 59 | 8/8/9 | 4.7 |
| 6 | Snowy Ridge | R126 to R150 | snowfields, a ridge of fir trees | The Bear | #d9d2ff | 6.3 to 7.3 | 13 to 20 | 14 to 43 | 23 to 72 | 8/9/8 | 5.3 |
| 7 | Lantern Garden | R151 to R175 | a hedge garden, paper lanterns in the trees | The Moth | #ffb38a | 7.4 to 8.5 | 14 to 21 | 18 to 42 | 30 to 75 | 9/8/8 | 6.0 |
| 8 | Cloud Harbor | R176 to R200 | a harbour of moored boats under rolling cloud | The Balloon | #8fc6ff | 8.5 to 9.9 | 14 to 21 | 18 to 50 | 36 to 96 | 8/8/9 | 7.0 |
| 9 | Ice Shelf | R201 to R225 | ice cliffs over a calm polar sea | The Penguin | #b9e6ff | 9.9 to 11.5 | 15 to 23 | 19 to 55 | 41 to 122 | 8/9/8 | 7.0 |
| 10 | Acorn Wood | R226 to R250 | old oaks, mossy roots, fallen leaves | The Squirrel | #e8b37a | 11.5 to 13.3 | 16 to 24 | 18 to 52 | 48 to 121 | 9/8/8 | 10.3 |
| 11 | Jelly Deep | R251 to R275 | deep blue water glowing from below | The Jellyfish | #ff8fd0 | 13.4 to 15.4 | 17 to 25 | 21 to 64 | 58 to 178 | 8/8/9 | 10.0 |
| 12 | Tide Pools | R276 to R300 | rock pools and a long beach at low tide | The Crab | #ff7a7a | 15.5 to 17.9 | 18 to 25 | 18 to 54 | 55 to 157 | 8/9/8 | 11.7 |
| 13 | Dusty Plains | R301 to R325 | wide grassland, one great tree | The Elephant | #e8c48f | 18.0 to 20.8 | 18 to 25 | 21 to 64 | 72 to 214 | 9/8/8 | 13.3 |
| 14 | Dune Sea | R326 to R350 | rolling sand dunes, wind ripples | The Camel | #ffcf8a | 21.0 to 24.4 | 19 to 25 | 24 to 57 | 90 to 203 | 8/8/9 | 17.0 |
| 15 | Blossom Hill | R351 to R375 | a hillside of blossom trees, petals in the air | The Hummingbird | #ff9ec4 | 24.4 to 28.1 | 20 to 28 | 22 to 60 | 91 to 241 | 10/10/5 | 14.3 |
| 16 | Bamboo Mist | R376 to R400 | bamboo forest in low mist | The Panda | #9fe0b0 | 28.3 to 32.6 | 21 to 30 | 40 to 72 | 160 to 294 | 12/13/0 | 31.0 |
| 17 | Howling Peaks | R401 to R425 | jagged mountains, a frozen waterfall | The Wolf | #c9a6ff | 32.8 to 37.9 | 22 to 31 | 41 to 65 | 183 to 296 | 13/12/0 | 36.7 |
| 18 | Rainbow Falls | R426 to R450 | a tall waterfall, moonbow in the spray | The Unicorn | #b79cff | 38.1 to 44.0 | 23 to 32 | 37 to 75 | 187 to 363 | 12/13/0 | 39.3 |
| 19 | Comet Coast | R451 to R475 | sea cliffs, a lighthouse far off, a comet overhead | The Comet | #7ee0c3 | 44.2 to 51.1 | 23 to 32 | 45 to 68 | 252 to 380 | 13/12/0 | 64.7 |
| 20 | Polar Night | R476 to R500 | sea ice and green-violet sky glow | The Narwhal | #6fb8ff | 51.4 to 59.3 | 24 to 35 | 42 to 82 | 252 to 491 | 12/13/0 | 51.7 |
| 21 | Cliff Top | R501 to R525 | high crags, a lone pine, valley lights far below | The Mountain Goat | #d0d6e8 | 59.7 to 68.9 | 25 to 36 | 51 to 85 | 332 to 582 | 13/12/0 | 73.7 |
| 22 | Far Galaxy | R526 to R550 | no ground at all: a spiral galaxy and planets | The Starship | #5fe0b0 | 69.2 to 80.0 | 28 to 36 | 57 to 85 | 402 to 624 | 12/13/0 | 91.3 |

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
- ladder (2026-11-08): a pool of 1119 knob settings (nets 2 to 8 columns by 2 to 6 rows, webs 5 to 12 spokes by 1 to
  3 rings, lanterns 6 to 24 stars; 0 to all extras; a third to all stars moved), 36 seeds each; 104 settings failed
  the phone sky (webs with 11 or 12 spokes and 3 rings, lanterns of 21 to 24 stars: stars or lines too close) and
  were dropped. The sweep bot ran 3 times on the other 1015 to fit D. The 550 were picked in order from the pool's
  36,540 seeded skies: D at or above the last level's and as close as possible to a geometric target from 3 to 80,
  stars in a window that rises from 8 to 14 at R001 to 26 to 38 at R550, family and build variety, then every check in
  "Verified for every one" above. Random flinging (2000 runs each, first 30 ladder skies): solves within p at most
  5.3% (R002, a 10-star lantern with 3 stars moved) and 3.6% (R014), all others 0.6% or less.
  Scripts: `gen.py` (generator and checks), `solver.py` (sweep bot), `pool.py`, `precompute.py`, `select_ladder.py`,
  `check_all.py`, `gen.js` (the Node port) in the spec agent's scratchpad.

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
| ★★★ on the ladder (moves at most p) | Random flinging | First 30 ladder skies: R002 5.3% and R014 3.6% by chance, all others 0.6% or less; harder skies 0%. Left open on those two (early warm-ups, slower than thinking) |
| ★★★ on the ladder | Sweep each star, drop at the lowest count | Allowed (the skill): the bot made p or better on 408 of 550 and 2p or better on 516; it gets stuck more as the worlds climb (stuck in at least one of 3 runs on 0 of 25 skies in World 1, 20 of 25 in World 22), where planning wins |
| ★★★ on the ladder | Edit local storage or the table to make easy levels | Nothing to gain: stars and bests are local only; the builder checks the table's checksum in its tests, and a changed table changes nothing anyone else sees |
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

Painted first (see The world). This list is the minimum; the builder adds painted art wherever it makes the world
richer, never text in a painting.

| Item | Made how | Size | Use |
|---|---|---|---|
| First Skies backdrop `art/sky-0.webp` | **Painted**: a deep indigo night sky over a quiet dark hill, soft violet and teal nebula clouds, a scatter of faint tiny distant stars, painterly, dark enough that white points and thin lines read on every part of it; no constellations, no lines, no text | 1600x1000, WebP about q55, about 80 KB | full-window background, `object-fit: cover`, behind the field |
| World backdrops `art/sky-1.webp` to `art/sky-22.webp` | **Painted**, one per world: the same night sky style over that world's scenery (Worlds table: meadow, lake, dunes, galaxy ...), the land low and dark along the bottom fifth, the sky above kept clear and dark for the puzzle; a separate sheer nebula layer per world is optional for the parallax | 1600x1000, about 80 KB each, 1.76 MB | backdrop of every sky in that world, Star chart page header and world tiles |
| Star sprites `art/star.webp`, `art/star-held.webp`, `art/star-gold.webp` | **Painted** cut-outs on transparency: a warm white glint with a soft halo and faint 4-point flare; a larger held version with a wider halo; a gold one for a solved sky | 128x128 each, about 6 KB | placed by code exactly on every star (drawn at 22 px, held 30 px), so painting costs no exactness |
| First Skies constellations `art/sky-L01.webp` to `art/sky-L20.webp` | **Painted**, one per hand-made sky: the creature or thing (The Kite ... The Dragon) as a luminous starlight figure in its `fill` colour, on transparency, painted on a 1000x1000 canvas over a guide of its `pts` and `edges` so its bright points sit at (10x, 10y) | 1000x1000 painted, shipped 640x640, about 35 KB each, 0.7 MB | the reveal behind the gold lines (The lit picture) and the solved tile |
| World constellations `art/world-1.webp` to `art/world-22.webp` | **Painted**, one per world, the same starlight style: The Firefly ... The Starship (Worlds table); not tied to any star positions | 640x640, about 35 KB each, 0.77 MB | rises behind the shape on each world's 25th sky; the world's tile and its 25th tile in the Star chart |
| Box art `art/cover.webp` | **Painted**, no text: a tangled constellation of warm stars and periwinkle threads over the night sky, half of it already untangled and blooming gold into a starlight whale, the land of two worlds at the bottom edge | 1200x750, about 150 KB | the shelf's game box (`/recess/`); not bundled into the game file |
| Lines, dashes, rings, gold lines, outline glow, beams, specks, hit areas, focus rings | drawn in code (SVG), lit to match the painting: soft glow on lines in their own colour, warm bloom on gold, faint halo on rings | | they must sit exactly on the puzzle's coordinates |
| Knot icon, four-point star icon, star-map icon | drawn in code (SVG, 20 px) with the same glow | | readouts and the Star chart button |
| Star chart tiles | thumbnails drawn in code from each sky's data, on a crop of the world's painting | | start or solved shape |

Each painting can be redrawn up to three times (CODEX-RECESS.md, The bar); prompts go in `art/prompts.json`.

**Size budget** against the 6 MB Recess limit, measured as the bundled file (images are base64 inside it, about a
third larger than the WebP): shell (kit:recess) about 14 KB, game code about 45 KB (generator about 3 KB), data about
16 KB (First Skies 9 KB, ladder table 4.4 KB, worlds and name lists 2 KB). Art: 23 backdrops 1.84 MB, 42
constellations 1.47 MB, star sprites 0.02 MB, so about 3.3 MB of WebP, about 4.4 MB once base64. Total about 4.5 MB,
leaving 1.5 MB for the builder's extra painted art. Box art ships separately. If the bundle passes 5.5 MB, lower the
backdrops' WebP quality before cutting any painting.

## notes.md

```
# Untangle: a note for grown-ups

What it is: a puzzle game. Each sky is a set of stars joined by straight lines, all tangled up. Your child drags the
stars until no two lines cross. When the last crossing clears, the stars glide into a hidden picture: a kite, a fish,
a fox, a whale, a dragon. There are 20 hand-made skies that grow from 6 stars to 18, then a ladder of 550 more in 22
painted worlds of 25 skies each, growing steadily harder (up to 36 stars), plus a new sky every day. The worlds are
there to give a sense of place and progress, not a wall: every sky is open from the start, so a child can jump ahead
or go back whenever they like.

What it builds: seeing shapes in space and planning a move before making it. Underneath, it is a real idea from
mathematics called graph theory: dots (vertices) joined by lines (edges). A drawing where no lines cross is called
planar, and every sky in this game can be drawn that way. Mathematicians, map makers and computer chip designers all
work on this same question: can these connections be laid out flat without crossing?

How stars work: three stars if the sky is solved in about one move per star that is out of place, two stars within
twice that, one star for any solve. Undo and Restart are always free. There is no timer.

How the ladder is made: each ladder sky is built by the game from a tiny recipe (a grid, a web or a ring of stars,
then some stars thrown out of place). Every one of the 550 was checked by computer before release: it can be untangled,
and it is at least as hard as the one before it, measured by how many moves a simple computer player needs.

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
12. Playtest: three kids aged 8 to 13 each finish Skies 1 to 10 in 30 to 90 seconds a sky (median), and play World 1
    and World 5 without stalling; adjust nothing in the data without rerunning the Python checks.
13. One file, offline, at most 6 MB (measured, base64 images included; about 4.5 MB expected); no fetches.
14. Ladder: a script in Scratch rebuilds all 550 records from the table with the game's own generator code and
    reproduces both SHA-256 checksums in The ladder (records joined; generated levels). R001 matches the worked
    example (draws, lines, start). For each of the 550 it re-verifies: start true crossings equal the record's X;
    planar, connected, every star with 2 or more lines; the true shape and the home layout have 0 trouble on 1300x620
    and 366x690 and the start has trouble above 0; stars at least 34 px apart at the start; the witness solves it in p
    moves with the slide rule; D(R k+1) is at least D(R k). List any failure; none is expected.
15. Ladder play: R001, R162 (`Lantern Garden 12`) and R550 load, show their labels, solve, glide into the true shape
    with the name card ("The Silver Net" for R001), and earn 3 stars at p moves; R025 and R550 also raise their
    world's painted constellation. Next runs Sky 20 to R001 and R025 to R026 (new world: the backdrop changes).
16. Star chart: opens on the current sky's page; `‹` `›`, PageUp/PageDown, swipe and the Worlds overview reach all 23
    pages; 25 tiles fit on a phone without scrolling; Home jumps to the first unsolved sky.
17. Painted first: every backdrop, star sprite, constellation and the cover is painted; the code-drawn lines, dashes
    and rings carry glow and sit inside the painting (Look board frames in the report). Each backdrop passes the
    darkness check in The world; each First Skies painting puts a glint within 12 px of every star at 1366x768.
18. `art/cover.webp` exists, 1200x750, no text.

## Open questions

Owner: default accepted, Cory 2026-11-08; may tweak later.

1. **The name.** Decision: keep "Untangle" (a common word, no shared art or code with Simon Tatham's puzzle of that
   name); "Star Knots" stays the fallback if it is ever wanted.
2. **Daily size.** Decision: Tonight's sky keeps 15 stars and 24 lines as the day's treat (about 2 to 3 minutes for
   a kid); 10 stars (5 lines) stays the smaller option if it is ever wanted.
3. **Level ladder** (Cory, 2026-11-08: "a progressive level difficulty ladder ... room for a large number
   of levels 500+ without getting too huge in file size"). Decision: 550 generated skies in 22 worlds of 25, packed
   as 8-character records (4.4 KB), D rising from 3 to 80 with no drops; the hand-made 20 and the daily stay.

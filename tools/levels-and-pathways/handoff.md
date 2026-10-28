# levels-and-pathways: build handoff (2026-10-28, Refine round 1 fixes)

## What was built

A K-2 dance tool, teacher led on a projector, the first tool of the dance family.

- `src.html` (the tool), `levels-and-pathways.html` (the draft bundle), `tool.draft.json`, `notes.md`,
  `voice/lines.json` (42 lines, warm-teacher, Sulafat; equal to `allLines()`, checked in the browser),
  `art/prompts.json` (no assets: everything is drawn in code).
- `kit/dance.js` (the family engine, `Dance`) and `docs/families/dance.md` (its reference).
- No other kit file was changed.

Layout: a studio floor (wood, back wall, mirror strip with the dancer's reflection, a barre) fills the stage; a top bar
holds the four mode buttons (icons, keys 1 to 4), Sound and Motion; the control row under the stage changes by mode.
Sizes: stack below 640 wide or taller than 1.15 times the width, wide at 1000 by 700 and up, compact between. Every
control has an icon and a voiced label; every target is 60 px or more at every STANDARDS size.

Modes:

1. **Levels:** six moves in place (stretch, twist, bend, swing, shake, curl), each with its own high, middle and low
   keyframes, a 4-click count-in and 8 counts ending in a freeze. A level tap mid-move takes effect on the next count.
   **Up and down** runs one move for 40 counts through high, middle, low, middle, high. **Surprise** picks both.
2. **Pathways:** straight, curved or zigzag; walk, skip, gallop or slide; at a level. The dancer travels and leaves a
   ribbon: shape = pathway, color + pattern + end badge icon = level. Up to three ribbons stay; Clean floor.
3. **Mystery path:** 8 rounds. The ribbon is hidden during the trip; the class draws the path in the air, then taps
   the answer. A right path paints a neutral gold "magic" ribbon (shape only); a right level restyles it in the
   level's look. A wrong answer replays the trip once. The rounds end in a gallery of all eight ribbons and a bow.
4. **Draw a path:** draw from the star; `Dance.readPath` splits the drawing into straight, curved and zigzag parts,
   numbered in order, each drawn in its level's color. Tapping a part's number badge cycles that part's level (high,
   middle, low; badge shows the level icon); a level tile sets every part. Dance it performs each part at its own
   level, the ribbon changing look part by part. Surprise path draws a non-crossing path with mixed levels.

## Refine round 1: what changed, item by item

1. **Big zigzags named straight (blocker).** New `Dance.readPath(points, opts)` in kit/dance.js replaces the tool's
   own analyzer. Corners come from a simplified line (tolerance 2) and must turn 45 degrees or more within 8 dense
   points, be calm on at least one side, and not be a hook at the ends. Two or more corners in a run that alternate
   left and right make a zigzag at any leg length (legs up to 66 units). See the drawn-shape table below.
2. **Low reads tall from the front (blocker).** New low keyframes for all six moves (straddle sit, cross sit, kneel on
   heels, lie on the back, curl on the floor); the stand-low pose is a deep squat. Contact sheet below: every Low
   pose, its freeze and every count keeps the head at 0.62 of standing height or less; every Middle pose 0.77 or more (corrected in round 2: Middle measured 0.77, and Low Curl's in-betweens rose to 0.72 until round 2 changed it).
3. **Drawn path split wrong.** Same rules as 1: a straight, zigzag, arch line names three parts (straight, zigzag,
   curved); a smooth arch is one curved part; an S-curve and S-wave are curved. A straight run is split off a curve
   only at a real corner. Table below.
4. **Header buttons under 60 px.** Header buttons have min-height 60 at every size in this tool's CSS; narrow-header
   mode buttons are min-width 60 (icon only at 561 px and wider in stack, with no subtitle).
5. **Mystery after Next.** After Next the hint is "Tap Go" at once; the Go how line is spoken when the walk back ends
   and Go is live (it needs Go enabled), so it is not dropped; Read speaks it.
6. **Welcome during a round.** The Mystery welcome follows the round's step: askPath, askLevel, nextHow or wMystery.
   Checked: coming back at a path step queued nothing stale and the hint and spoken line were the path question.
7. **Round 8 to gallery.** The last right level says "Yes! That's the level." at once (cuts in), the gallery starts
   straight away, sets the hint to the all-done line and says it. Timing in the Mystery run below.
8. **Waiting hints name the next action.** After the freeze and after Up and down the hint returns to the Levels how
   line; after a trip to the Pathways how line (once spoken it only sets the hint). The right-level line no longer
   says "Tap Next"; a separate how line (nextHow, "Tap Next for a new mystery.") is spoken once, then hint only.
9. **Move icons look the same.** Each move has a fixed icon pose (from its own keyframes) plus a motion mark (stretch:
   arrows out; twist: a turning arrow; bend: a fold arrow; swing: a two-way arc; shake: zigzag ticks; curl: a curling arc). Icons are drawn once and stay the same at every
   level, so the six are distinct; tiles show the icon at 52 px (44 compact).
10. **Gallery crowded.** Gallery ribbons are scaled 0.23 into a 4 by 2 grid of cells, each with its own end badge; the
    dancer bows to the right of the grid; round dots sit right of the mirror. Screenshot checked: nothing overlaps.
11. **Mystery cites the wrong code.** Mystery now cites DA:Re7.1.Kb in spec.md and notes.md; Cr1.1 is cited as
    Cr1.1.Ka and Cr1.1.Kb with their wording. **Re7 moves (for the integrator):** DA:Re7.1.1a and Re7.1.2a go to
    dance-pattern-puzzle; DA:Re7.1.1b and Re7.1.2b go to dance-styles-explorer. No other tool was edited. Pr5.1.2a
    is not cited: this tool does not teach it.
12. **Draw a path claimed Cr3.1.1b, Cr3.1.2b, Cr1.1.2b.** Per-part levels added (see Draw a path above). New how line
    tapPart ("Tap a number to change that part's level.") is spoken once after the part names. Surprise path sets
    mixed levels (200 of 200 tries). Spec has a "Refine changes (round 1)" section.
13. **Late "Yes!".** rightPath and rightLevel cut in (`now: true`), so an answer given during the question gets its
    Yes at once.
14. **Leftover phrase boxes.** `Dance.counts` shows phrase pips only while counting and only for the phrases the run
    has; none are left over after a run.
15. **Low end pose looks like a fall.** Pathways and Draw end poses face front (facing 0) and use the new low freeze.
16. **Surprise paths cross themselves / circle off the floor.** Surprise paths that cross are rejected and redrawn;
    the round 7 circle is centered at (25, 35.5) and stays on the floor.
17. **Count-in under Read.** A Read tap sets a read-until time from the hint's length; every count-in waits for it.
18. **Mystery round dots clear the mirror frame.** Dots are a 2 by 4 grid right of the mirror; if there is no room
    there, one row on the back edge of the floor.
19. **Sizes.** At 760x900 the move grid is at y 705 to 887, in view; at 375 the Level row is at 515 to 590, in view;
    at 680x425 the hint is not clipped (compact tiny mode, 60 px tiles).
20. **dance.md.** Lists `Dance.flat`, the skeleton, BASE, `shade`, `heard`, stand low, yaw, what facing angles mean,
    low-height guidance, `readPath` (with a "Reading a drawn pathway" section), styleAt runs, print scaling, the calm
    trail start and counts pips.

Nits fixed: narrow-header mode buttons have aria-labels; the curved ribbon starts on the star in calm mode; a long
first drag in Draw mode no longer plays the welcome before the part names (pointerdown marks the welcome said).

## Drawn-shape test (real drags in headless Chrome at 1280x720)

Each shape is a mouse drag (51 to 170 points about 1.2 floor units apart, with hand wobble) through the tool's own
pointer handlers, read back from `state.parts`. 30 of 30 read as listed.

| Shape | Read as |
|---|---|
| Line | straight |
| Diagonal line | straight |
| Semicircle | curved |
| Shallow arch | curved |
| Half-sine hump | curved |
| Sine arch, rise 30 | curved |
| Rainbow, rise 40 | curved |
| S-curve | curved |
| S-wave | curved |
| Gentle wave | curved |
| Circle (round 7 shape) | curved |
| Zigzag, tool size (legs 36) | zigzag |
| Deep zigzag (legs 46) | zigzag |
| 3-leg zigzag (two versions) | zigzag |
| Zigzag, legs 30 | zigzag |
| Zigzag, legs 60 | zigzag |
| Small zigzag, legs 15 | zigzag |
| Z | zigzag |
| Scribble | zigzag |
| L | straight, straight |
| Box | straight, straight, straight |
| Straight then semicircle | straight, curved |
| Semicircle then straight | curved, straight |
| Straight, zigzag, arch | straight, zigzag, curved |
| Straight then zigzag | straight, zigzag |
| Zigzag then long straight | zigzag, straight |
| Curve then zigzag | curved, zigzag |
| Starts off the star | straight, straight (the lead-in from the star is a part) |
| Too short | too short (the tool asks for a longer path) |

A node test of `readPath` on 30 synthetic shapes passes 29; the one miss is a very gentle wave (bend under 45
degrees with a sharp hand wobble) read as zigzag. The real drag of a gentle wave reads curved; recorded as an edge.

Per-part levels (real clicks): badge 2 tapped twice gave zigzag at high, badge 3 tapped once gave curved at low, no
level tile showed pressed, and the dance ran a green ribbon run, then blue prints, then amber stripes.

## Contact sheet (every move at each level, from the front)

Head height as a share of standing height, over every count of each phrase and its freeze:

- High: all six moves stand tall or reach up.
- Middle: lowest head 0.77 (bend B, a forward fold at lean 58; round 1 said 0.80, which was wrong).
- Low: see Refine round 2 for the measured in-betweens (round 1 measured keyframes only and missed Low Curl's rise).
  The freeze poses are on the floor. A and B keyframes of each move look distinct.

## Sizes (STANDARDS frames, all re-shot)

No header or panel control is under 60 px at any size. 760x900: move grid in view. 375 (hosted frame): the Level
row is in view. 680x425: hint not clipped. All four modes shot at 375, 680x425, 760x900, 800x500, 1000x625,
1280x720, 1366x768 and 1920x1080 and checked by eye; nothing overlaps or is clipped.

## Mystery to the gallery at real speed

One real-speed run, all eight rounds, answers tapped 0.9 s into each question (while the question plays) and Next
tapped 3 s after each right level. Whole run 169 s, no errors.

- Every right answer got its "Yes!" in the same 1 ms as the tap (rightPath and rightLevel cut in), 8 of 8 each.
- After each Next the hint was the Go line at once (300 ms later) and stayed until Go was live; the Go how line was
  logged after the walk each round (spoken in round 1, hint only after that), never dropped.
- Round 8: the right level's "Yes! That's the level." at 162.2 s, then the gallery's all-done line at 164.4 s, the
  gap being the Yes line itself (no silence). The hint showed the all-done line through the gallery. Screenshot: badges
  in clear cells, dots right of the mirror, dancer bowing at the right, nothing covered.
- One quirk: in round 1 the nextHow line was still waiting behind the Yes when Next was tapped 3 s later, so Next's
  hush dropped it; it was spoken in round 2 instead (once), hint only after that.

## Session checks (real speed)

- Levels: twist, a level change to Low mid-move, then the freeze; 2.5 s later the hint is the Levels how line.
- Pathways: Go, then Read 150 ms later. The count-in started 10.3 s after Read (the walk to the star and the spoken
  lines come first); the read estimate was 1.3 s, so the counts never sound under Read.
- After the trip the ribbon line is spoken and the Pathways how line follows it (hint only, it was said before).
- Mystery at a path step (round 3, after watching): nothing stale queued; hint and spoken line are the path
  question (askPath).

## Voice counts

From the Mystery run (whole game) and the session run. spoken = said aloud, silent = hint only (already heard or
too early), dropped = cleared by a hush.

| Key | Spoken | Silent | Dropped |
|---|---|---|---|
| wMystery | 1 | 7 | 0 |
| askPath | 1 | 7 | 0 |
| askLevel | 1 | 7 | 0 |
| rightPath | 8 | 0 | 0 |
| rightLevel | 8 | 0 | 0 |
| nextHow | 1 | 5 | 1 (see quirk above) |
| allDone | 1 | 0 | 0 |
| wLevels | 1 | 2 | 0 |
| twist, atMiddle, copyMe, atLow, freeze | 1 each | 0 | 0 |
| wPaths | 1 | 0 | 1 (hushed by the mode change) |
| straight, walk, ribbon | 1 each | 0 | 0 |

Each how line is spoken once and then only sets the hint. `allLines()` equals the 42 lines in voice/lines.json
(checked in the browser, exact match).

## Decisions and deviations

- **No kit/movement.js and no docs/families/movement.md.** BASELINE w1-21 (Cory, 2026-10-27): PE and dance each get
  their own figure. The figure stays inside `kit/dance.js`.
- **Neutral magic ribbon in Mystery** (gold dashed, `plain` style) so a right pathway does not reveal the level.
- **Dancer size:** 40 percent of stage height holds in Levels only. On the travel floors the dancer is at scale 0.7
  so a whole pathway fits; the mirror image is reflect 0.35, scale 0.8 so its head stays inside the mirror strip.
- Middle swing is a side swing with a twist (a forward swing read the same as bend at the middle level).
- Pr5.1.2a is not cited (the tool does not teach it).

## Known gaps

- `readPath` edges: a very gentle wave can read straight; on 375 and 680x425 stages a shape squeezed to fit reads
  less reliably (Refine round 2 has the numbers).
- In Draw mode the end badge can sit close to the last part's number badge on short paths.
- After a trip the Pathways hint changes only when the ribbon line has finished (about 3 s).
- If Next is tapped while the nextHow line is still waiting, it is dropped that round and said on a later one.

## For Cory

- The movement.js question is answered by w1-21; fitness-circuit's spec note is out of date (integrator fixes it).
- Re7.1.1a and Re7.1.2a to dance-pattern-puzzle, Re7.1.1b and Re7.1.2b to dance-styles-explorer: for the integrator.
- No commit made.

## Refine round 2

1. **B1, front-to-back curves (blocker).** `Dance.readPath` now takes the floor (`{start, floor}`) and reads the line
   as it looks on screen, in units of the floor's scale at mid depth, so a shape reads the same whichever way it is
   drawn. A corner also needs a real tip (0.47 of its turn within 1.5 units, 8 px on a small stage, of the sharpest
   point on a barely smoothed copy), so the top of a wave or an S is never a corner. Scribble hairpins (both 100
   degrees or more) count as a zigzag even when they turn the same way; a side leg joins a zigzag only when its corner
   turns 0.6 of the run's middle turn. Rules in kit/dance.js and docs/families/dance.md. Without a floor, curve stays
   30 (the round 1 node test: 29 of 30, the same gentle-wave edge as before).
   Real drags (seeded hand, 3 to 9 px samples with wobble) through the tool's own pointer handlers: 77 shapes (the
   round 1 table, the exit check's shapes, wobbly lines) each side to side (0), front to back both ways (90, 270),
   back to front (180) and on both slants (45, -45). A shape too big for the turned floor is squeezed to fit (x shown).
   - 1280x720: 457 of 462 right. Misses: wave3 at 90 and 270 (x0.58), wave3 at 45 (x0.78), gentle wave (the
     round 1 edge) at 90 and -45.
   - 1366x768: 454 of 462. Misses: wave3 at 0 (curved, curved), 90, 270 (x0.57); sWave2 at 90 (x0.56); sSZA at 0
     (an extra straight end); gentle wave at 0, 90, 270.
   - 760x900: 451 of 462. Misses: wave3 at 90, 270, 45, -45 (x0.49 to 0.7); sWave2 at 45; scribble3 at 0
     (straight, curved, zigzag); S wave at -45 (x0.59); gentle wave at 90, 180, 270, -45.
   - The exit check's own failures (vS10 to vS20, the vertical S, the 3-hump wave side to side, the 3-corner scribble)
     read right at 1280. What is left is a 3-hump wave squeezed into half its size front to back, whose humps then
     look pointed on screen too.
   - Node run (3 hands, 6 turns, 462 cases a size), failing cases, round 1 rules then now: 1280 148 then 9, 1366 136
     then 9, 760x900 170 then 17, 680x425 150 then 59, 375 157 then 69. No case that passed under round 1 fails now
     at 1280, 1366 or 760x900. On the two small stages 11 single orientations that passed now fail (sScribble_alt,
     straight_zig_arch_big, sZig3, sZig4, arch_tall, sS_horiz_from_star, straight then zigzag), most of them squeezed
     to fit: recorded as a known gap.
2. **S1, Low Curl.** Low Curl is now a seated tuck (head 0.34) that opens into a seated star (0.52). Every in-between
   (81 per move) of every Low move: stretch 0.52, twist 0.56, bend 0.53, swing 0.43, shake 0.08, curl 0.53. Changing
   from one Low move straight to another used to pass 0.72 (stretch to bend); it now goes through the seated tuck
   (250 ms), and a live sample of every animation frame over 14 back-to-back Low moves topped at 0.56.
   Middle's lowest head is 0.77 (bend B), corrected above.
3. **S2, fast level answer.** A level tapped during the 1.5 s right-path paint now finishes the paint at once and runs
   the same code as a slow answer; the path-only badge goes on only while the level is still open. Real taps 0.3 s
   and 2.6 s after the path: round 1 both end with the full badge (no path-only badge) and rightLevel then nextHow;
   round 8 both keep the gallery badge and say allDone. The only difference is askLevel, which the fast tap skips.
4. **S3, standards.** DA:Cr1.1.2b cited in spec.md, the src.html header and notes.md. **DA:Cr3.1.1b moves off this
   module (for the integrator)**: a way icon on every part badge would crowd the badges on a K-2 projector and at 375,
   so the way stays one choice per path. No K-2 dance tool cites it yet; the integrator picks its home.
5. **S4, part badges.** Each badge takes the first clear spot (middle of the part outward, above then below, then
   nudged sideways) that is on the stage, clear of the dancer, the level guide and the other badges; the hit area stays
   64 px or more. 45 Surprise paths at each size, with the dancer at the star and again at random spots: 0 off the
   stage, 0 on the dancer, 0 on the guide, 0 overlapping, at 375 (host), 680x425, 760x900, 1000x625, 1280x720,
   1366x768 and 1920x1080. Surprise path never fell back.
6. **Polish.** The gallery bow is a hip fold with the arms hanging, turned 35 degrees toward the ribbons, so the fold
   shows from the front (the tool's own pose; the kit's bow is unchanged).

Re-shot at 375 (host), 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x900: Levels at Low Curl,
Draw a path with a Surprise path, and the gallery. No control under 60 px, no horizontal scroll. `allLines()` still
equals the 42 lines in voice/lines.json. No commit made.

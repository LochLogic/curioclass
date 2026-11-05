# levels-and-pathways: Play lens (round 1, 2026-10-28)

Played cold from the draft bundle (`CURIO_DRAFT=1`, 149 KB), as a teacher projecting to a K-2 class moving along,
and as a child alone at home. Real held clicks (120 ms) and drags over CDP, Sound on, Motion on unless noted. All
four modes at real speed, including all 8 Mystery rounds with a wrong path (round 2) and a wrong level (round 3), and
the round 8 to gallery hand-off at real speed (frames at 0.3, 1.0, 1.8, 2.6, 4, 6 and 9 s after the last tap).
No console errors or exceptions in any run.

Limit of this run: headless Chrome lists 22 voices but its utterances never end, so each line ran to the kit's cap
(2.5 s + 80 ms a character). Line order and drop/silent logic come from `V.log`; voice durations were not measured,
and nothing below rests on them.

Frames looked at (scratch, `lens-lp-play/`): default screen at 1366x768, 1920x1080, 1280x720, 1000x625, 800x500,
680x425, 760x900, 520x900; every mode at 1366x768, 1000x625 and 680x425; 375 wide in the iframe host (Levels,
Pathways, Mystery); calm mode mid-trip and Mystery; Levels (first tap, count-in, mid-move, freeze, level change
mid-move, Up and down at each level change, Surprise, Read mid-line); all 36 move keyframes (6 moves x 3 levels x A/B)
and the move icon rows at each level; Pathways (4 trips, all ways, all levels, fourth trip clearing the oldest,
Clean floor); Mystery (every round: travel, ask, paint, ask level, solved, next; wrong answers; gallery; Play again);
Draw (a drawn multi-part line, Dance it, end, too-short line, three Surprise paths, a drag starting off the star).

## Blocker

1. **Low level reads tall in the front view; Curl at Low freezes standing tall.** Levels mode, `MOVES.curl.low[1]`
   (and the `sit` keyframes of Stretch and Bend at Low). Seen in `poses/grid-low.png`: Curl Low's B frame (the pose
   held on count 8, "And freeze!") is a spread-arm figure with long legs reaching to the bottom of the mat, taller on
   screen than any Middle pose. Stretch Low A and Bend Low A (sitting, legs forward) project as legs hanging straight
   down, so the dancer looks like someone standing (`lev/l2-low-idle.png`: head lower, but the figure is as tall as at
   Middle). The class is told "Low level. Get close to the floor." and then freezes copying a tall shape: the one
   concept this mode teaches is shown wrong at the freeze. Better: keep every Low keyframe visibly low from the front
   (Curl Low "open" as a wide shape lying or kneeling, sitting legs foreshortened or the body turned three-quarter for
   sit poses), and check all 18 B frames against the level guide. **family:dance**

## Should fix

2. **After Next, the hint says "Tap Next for a new mystery" while Next is off and Go is the move.** Mystery,
   `nextRound()`: `V.how('wMystery', {valid: ... && !state.busy})` is queued right after `newRun('return')` sets busy,
   so it is dropped stale every round (`V.log`: wMystery dropped stale after each Next) and the hint never updates.
   Frame `pd/y1-after-next.png`; Read at that moment speaks "Yes! That's the level. Tap Next for a new mystery."
   Rounds 2 to 8 all open on this wrong hint. Better: set the hint (silently, how-to already heard) once the walk back
   ends, as `playAgain()` does. **general**
3. **Round 8 to gallery hand-off: stale hint, no praise, a silent gap.** Mystery, `answerLevel()` r = 7. At real speed
   the right level gets the chime, then for about 4 s (frames `m7-hand-1.8`, `-2.6`, `-4`) the gallery is on screen,
   the answer buttons are gone, and the hint still reads "Which level was the dancer? Tap high, middle or low." The
   last right answer gets no "Yes!" (rightLevel is skipped for round 8), and nothing is spoken until "Eight mysteries
   solved!" about 4 s after the tap, after the walk and bow. For a class, the biggest moment of the mode is the flattest.
   Better: speak a short praise (or allDone) as the ribbons gather, and set the hint to allDone when the gallery starts.
   **general** (hint) / tool (pacing)
4. **Idle hints after a run don't name the next action.** Levels ends on "And freeze!" (`lev/l5-after.png`),
   Pathways on "Look at the floor! The ribbon shows our pathway." (`pd/p1-end.png`); that is what Read says while the
   tool waits. STANDARDS "Say how to act": the waiting hint names the control. Better: after the event line, the hint
   returns silently to the mode's how-to ("Tap a move...", "Tap a pathway, then tap Go"). Draw already does this
   ("Draw a new one, or dance it again."). **general**
5. **Move icons can't be told apart.** Levels move grid, `drawMoveIcons()`. At High, five of six icons are the same
   tiny tiptoe figure with arms up (`poses/icons-all.png`); at Middle, Stretch and Twist are identical. The figure is
   about 30 px tall in a 72 px tile. For a child who can't read, the icon is the label (rule 4, K-2 "reads nothing").
   Better: one fixed, distinct icon per move (not level-dependent), drawn larger, with a motion mark (twist arrows,
   shake lines, swing arc). **family:dance**
6. **Ribbon gallery is crowded.** Mystery gallery (`mys/m8-gallery-end.png`): the end badges of rounds 6 and 7
   overlap each other; the bowing dancer stands on the front row and covers most of round 6's zigzag and round 7's
   circle. The gallery is the payoff the class looks at together. Better: place the dancer in front of the floor edge or beside the grid, and give each cell's
   badge its own spot (the known "badges overlap" gap shows here worst). **general**
7. **A drawn straight + zigzag + arch is named as one zigzag.** Draw, `analyze()` (frame `pd/d1-drawn.png`): a 20-unit
   straight run from the star, four 27-unit zigzag legs, then a half arch were one part, "First, zigzag." The lead-in
   and the arch join the zigzag because `reach = min(40, 1.5 x median leg)` is longer than both. A child who drew three
   kinds hears one. Better: an end leg joins a zigzag only when it is itself about as long as the zigzag legs and
   straight; a curved stretch never joins. **family:dance** (the splitter is the engine's drawn-path rule)

## Polish

8. **"Yes!" comes late when the class answers during the question.** Mystery: tapping a level while askLevel is still
   playing queues rightLevel behind it (`answerLevel` drops queued lines but lets the current how-to finish); frame
   `m05-solved` 0.6 s after the tap still shows the question. Better: an answer cuts the question line (`now: true`).
   **general**
9. **Leftover phrase boxes in the count strip.** After a run, small rounded boxes stay to the right of the 8 count dots
   in idle (2 after a 16-count trip, 3 after a longer Draw dance: `pd/d3-dance-end.png`). They mean nothing to a K-2
   class at rest. Better: hide them when the clock stops. **family:dance**
10. **Low end pose on the travel floors looks like a fall.** Pathways and Draw: after a Low trip the dancer sprawls
    with one leg kicked out sideways (`pd/p4-end.png`, `pd/d6-offstar.png`). Better: a low crouch facing the class.
    **family:dance**
11. **Surprise path can tangle.** Draw, `surprisePath()`: one of three tries made a zigzag then a curve that loops back
    across itself, with part badges 1 and 3 stacked (`pd/d5-surprise2.png`). Hard for a class to follow in the room.
    Better: reject paths that cross themselves or bring two badges within a badge width. tool
12. **Round 7 circle spills off the floor.** Mystery round 7 (Low, full circle): the wide striped ribbon runs past the
    front edge of the floor onto the count dots (`mys/m65-solved.png`). Better: shrink the circle a little or move its
    center back. tool
13. **High ribbons almost vanish in the gallery.** At gallery scale (0.27) the high ribbon's dotted footprints and thin
    line are faint next to the solid bands (`mys/m8-gallery-end.png`, rounds 2 and 5). Better: thicker prints at small
    scale. **family:dance**
14. **Read mid-call lets the move start under it.** Levels: Read during "Twist!" hushes the call chain, the move's
    `say(..., {wait: true})` resolves dropped, and the count-in clicks and music start while Read is speaking. Better:
    wait for Read before the count-in. **general**

## Nits

15. 680x425 compact: the hint's last line is cut off at the bottom (known gap; `f1/paths-680x425.png`). general
16. 375 wide (host): Pathways' Level row is below the fold (Go and the pathway row are visible; all buttons stay 60 px).
    general
17. Calm mode: the curved ribbon starts a little off the star rather than at it (`f2/calm-trip.png`). family:dance

## What worked (for the merge, not findings)

- Mystery is the best mode: answers are disabled while the dancer travels, the gold "magic" ribbon keeps the level
  hidden, the guide stays dark, wrong answers replay once, the 8 rounds match Content, Play again resets cleanly.
  Each round runs about 11 to 13 s of travel; all 8 with talk fit in about 4 minutes.
- Pathways: four trips leave three ribbons (oldest cleared), pattern + badge carry the level, Clean floor works.
- Calm mode keeps the timing and still paints the ribbon; 1366x768 and 1920x1080 show floor, dancer and the main
  buttons together; 375 wide keeps 60 px targets.
- Event lines (moves, levels, answers) speak every time; how-to lines (copyMe, askPath, askLevel) speak once, then
  stay silent.

Counts: blocker 1 (general 0, family 1), should fix 6 (general 4: items 2, 3, 4, 6; family 2: items 5, 7),
polish 7, nit 3.

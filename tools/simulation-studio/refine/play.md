# Play lens: simulation-studio (round 1)

Cold play, 2026-10-28. Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py simulation-studio` (149 KB). Driven with
`scripts/drive.py` (held clicks, 0.12 s), port 9750, own profile; `--host 9751` for 375 wide (host.html deleted after).
No console errors or exceptions in any shot (the only log line was the host page's own favicon 404).

Played as (1) a grade 10 statistics student alone at home, at a real pace through Raw log, Clean, Model, Answer,
including the wrong cleaning order, Flag or Drop without Pair, removing every step, and a student who skips straight to
Model and to Answer; and (2) a teacher projecting it at 1366x768 and 1920x1080.

Counts: blockers 1, should fix 4, polish 4, nits 4.

## Blocker

1. **Model, pairs table and fill after "Pair, then Drop": the Real column counts eruptions that were never next to
   each other.** `pairsOf(state.res.rows)` (src.html:426) pairs consecutive rows of the *cleaned* log. Once Drop has
   removed the 78 night rows, consecutive rows are no longer consecutive eruptions, so the table shows Real "Short then
   short 3" (and 78, 79, 60), and Fill sets "after a short, chance long" to 0.96. The real geyser has 0 short-then-short
   pairs; the tool's own punchline is that it never happens. This is the path the tool itself steers a student onto:
   add Drop, add Pair, get "Careful..." and the hint "Move Pair above Drop with its up arrow", obey it, see "Your log is
   clean", go to Model, Fill, Run: Match 88 percent, Real 3 / Simulated 3, and the hint says "The humps match. Now check
   the pairs table." The line "That's a geyser that never follows a short one with a short one" can never play on this
   path (`resultKey` needs real SS = 0), and the class means shift (55.3 / 81.8, sign test 267 not 269). Seen in frame
   `f3/34-pair-drop-model` and the voice log of the full-pace run (`f5/40-flow`: Drop, Pair, up arrow, Flag, Model,
   Fill, Run spoke "The humps match" twice, never "never"). Better: pairs (and the "after short" chance) should come from
   true neighbours in the file (`r.src === r.i + 1` after Pair, or the original row order), with dropped rows breaking
   the chain rather than joining across it; Drop-after-Pair should then give 0 short then short. Tag: family:data-desk.

## Should fix

2. **Model from the uncleaned log: the hint loops, and some runs praise it as "just like the real thing".** A student
   who skips Clean and taps Fill from my clean log gets "Filled from: raw log" (raw means 83.2 after short, 66.4 after
   long: backwards). Seed 1 gives Match 84 percent and the hint "The humps don't match yet. Change a rule or tap Fill
   from my clean log, then run again." They just did tap it; nothing names Clean. Tapping New run a few times, seeds
   17, 19, 44, 49 and 55 reach 85 to 87 percent and the tool says "That's a geyser that never follows a short one with a
   short one. Just like the real thing. Tap Answer to write the ranger's sign." That is praise for the backwards model,
   the exact thing the tool exists to catch (spec: the raw fill is 78 to 86 percent). Seen in `f2/21-rawfill-seeds` and
   `f3/33-rawfill-seeds` (seed sweep through the real Run path). Better: when the recipe has no Pair step, the Model
   result line and hint point back to Clean ("Your geyser copies the raw log. Tap Clean and fix the log first.") and the
   "never" praise needs a paired log. Tag: family:data-desk.
3. **Clean, first step is not Pair: "Order matters. Try moving one." with only one step.** Adding Drop or Flag first
   speaks and shows the recipe line while both arrows on the single step are disabled, then "The ranger's rule still
   looks backwards. Add another step from Add a step." The instruction cannot be followed. Seen in `f1/04-clean-drop-only`
   and `f1/10-clean-flag-only` (hint text in the readout). Better: speak the recipe how-to when there are two steps to
   move, or word it for one step ("Each step is a line of the recipe. Add another; then order matters."). Words match
   the state (POLISH). Tag: general.
4. **Small and narrow windows hide the main chart or the main controls.**
   - 680x425 and 800x500 (the site's preview), Raw log: the `ns` layout stacks the scatter under the table, so the
     raw scatter with r = -0.64 (the hook) is fully below the fold. Done when 8 asks for the main chart visible at
     680x425. Frame `f4/680x425-raw`. (Clean, Model and Answer pass at 680x425.)
   - 760x1000 (stack): the hint, Add a step, Run 299 eruptions sit below the charts (Run at y 1081, hint at 1024 to 1168
     on three benches); at 375 wide the same, so the first screen never says what to do. STANDARDS: the main controls
     are visible without scrolling at every size. Frames `f4/760x1000-*`, `f6/375-raw`, `f6/375-scroll`.
   Better: in `ns`, put the scatter beside a narrower table or above it; in stack, put the hint and the bench's main
   button (Add a step, Run, Test) above the stage. Tag: general.

## Polish

5. **Model, after a rule change: "Match: 89%" stays at full strength** while the veil says "Changed: run again" and the
   pipeline says "Run again". Dim it or add "(last run)" as the pairs column already does with brackets. Frame
   `f1/16-model-dirty`. Tag: general.
6. **Model legend says "Real, cleaned log" when the recipe is empty** (the student skipped Clean); the histogram is then
   the raw waiting column. Say "Real, raw log" until a step exists. Frame `f1/11-model-skip`. Tag: family:data-desk.
7. **Model panel at 1366x768: the last slider (Wait after a long eruption, spread) is cut off below the fold**; a
   student moving rules by hand may not know it exists. Two sliders per row, or a tighter rule block, would fit all six.
   Frames `f1/14`, `f1/16`. Tag: general.
8. **Clean panel: a blank band about 55 px tall between the hint and Add a step** at 1366 and 1920 (the reserved hint
   height for the longest variant). Fine for stability, but it reads as a gap; a smaller reserve or the shorter hint
   variants would tighten it. Frames `f1/03`, `f4/1920x1080-clean`. Tag: general.

## Nits

9. Histogram y-axis titles ("eruptions", "share of eruptions") collide with the top tick label (60, 100%), clearest at
   1920x1080 and at the all-short extreme. Frames `f4/1920x1080-clean`, `f2/28-alt-zero`. Tag: family:data-desk.
10. Answer, before any test: the real-log bar shows a thin blue sliver at width 0 (its 2 px border). Frame
    `f1/17-answer-skip`. Tag: general.
11. Raw r reads -0.64 on screen and in notes.md; the spec's Done when 1 says -0.65 (r = -0.6446). Screen and notes agree;
    the spec line should be corrected (for the Teaching lens to confirm). Tag: general.
12. Answer at all extremes (cut 5.5, 130 after short, 30 after long, window 20) works: 0 of 298, the clock wedge and
    hands draw correctly, summer 2 percent. Model extremes (both chances 1.00: all long, one hump, 0 short; both 0 with
    means 30 and 120: 297 short then short, Match 0%) also draw cleanly. No action; listed so the Exit check need not
    redo them.

## What worked (no action)

- The hook lands: the raw scatter slopes down, the ranger's rule card says the opposite, and Pair flips r to 0.89 with
  the line rising. The wrong-order warning, the peach rings on the 26 wrong pairs and "2 steps, check order" on the
  pipeline are clear. Removing every step returns focus to Flag's Add button and the hint to "Tap a step under Add a
  step".
- Full clean path (Pair, Flag; Fill; Run) gives Match 89 percent, pairs 0, 100, 100, 98 and the "never" line; Answer
  with Fill gives 269 of 298 and a summer of 88 percent; 72 for both gives 136; the raw fill gives 49.
- Every waiting moment names the next action and control in the hint (raw, page turn, marks, each Clean state, each
  Model state, each Answer state). How-to lines spoke once in the five-minute full-pace run; results spoke each time.
- Calm mode (Motion off) keeps every result; the teacher view at 1366x768 and 1920x1080 is readable from the back
  (pipeline, park sign, Match, class table).

Frames looked at: f1 01 to 20 (all benches and the main paths at 1366x768), f2 21 to 32 (marks, removing steps,
Flag/Drop without Pair, Drop-Pair-Flag, model and sign extremes, stale sign, reset), f3 33 to 35, f4 (680x425, 800x500,
1000x625, 1280x720, 760x1000, 1920x1080 on all four benches), f5 (full-pace voice run, fast taps, calm), f6 (375 host),
all under C:\Users\Cory\AppData\Local\Temp\claude\S--\98b8b046-f7f2-48d0-a719-c61ce01237be\scratchpad\lens-sim-play.

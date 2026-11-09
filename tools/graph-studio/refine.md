OPEN (round 1, Claude Refine 2026-11-06; Codex fixes next)
Counts: blockers 0 (general 0, family 0), should fix 13 (general 6, family 7), polish accepted 17

# Refine: graph-studio

Curiosity No. 08. Merged from `refine/teaching.md`, `refine/play.md`, `refine/craft.md` (no sensitivity.md yet).
Frame folders, short names used below: T = `S:/CurioClass-codex-scratch/graph-studio/teaching/frames/`,
P = `.../graph-studio/play/frames/`, C = `.../graph-studio/craft/r1/`, A = `.../graph-studio/audit-r1/`.
Spot-checked in src.html by the integrator: items 1, 2, 3, 4, 5, 7, 8 and 12 (the cited code is as the lenses say).

## Blocker
None. All three lenses pass the short test; no score, goal, level or finish anywhere.

## Should fix
1. **Key points miss a zero where the curve touches the axis (a double root).** src.html:1050-1061 (`roots` only
   takes sign changes or an exact 0 sample) and 1091. `y = (x-1.3)^2` with Key points shows `1 turn (1.300,
   4.930e-32)` and no zero (T/t-squared-double.png); the default `y = x^2` finds its zero only because a sample lands
   on x = 0, so panning loses it. A vertex on the axis is the commonest grade 9 case. Fixed: a turn whose |y| is below
   a tolerance relative to the view is also marked as a zero, and its y prints as 0.000. (general)
2. **Negative bases with fraction exponents draw a wrong domain.** src.html:598 `Math.pow(a,b)` gives NaN for
   `(-8)^(1/3)`, so `y = x^(1/3)` draws only its right half while the Manual says blanks mean undefined. Misleads on
   domain, the anchor's F-IF.A.1. Fixed: when the exponent is a literal fraction p/q with odd q (written `1/3`, `2/3`;
   decimal exponents stay as now), take the real root; add one Manual line on it. x^0.5 losing
   its left half stays (correct). (general)
3. **Log axis titles say `log₁₀ x` / `log₁₀ y` while the ticks show x values.** src.html:983-984 against 961-962. On the
   planets plot "log₁₀ y" sits beside "100", read as log y = 100 (C/d4-planets-frame.png). Fixed: title stays "x" / "y"
   (or the data's unit) with "log scale" beside it. (family:curiosity)
4. **Key points make every redraw slow with several lines.** src.html:1093 and 1098-1105 (pairwise intersections at
   3,500 samples), run from `rebuildPaper` (1151) every dirty frame: scrub, pan, zoom and each frame of a playing ruler.
   Eight lines with Key points: 31 ms a redraw, a playing ruler at 33 ms frames (C/perf-play-eight-keys.png,
   perf-bench.png, perf-four-keys.png), so a Chromebook falls far below the 60 fps of Done when 1. Fixed: compute
   features when the pointer or ruler settles (or every few frames while animating), cache per view, and intersect the
   active line against the others rather than every pair. (family:curiosity)
5. **Pressing Read, Sound or Motion removes the first-run hint.** src.html:1735-1737 calls `dismissHint()` for any
   button. A student presses Read to hear the hint, hears it once, and the next Read says the fallback line (C/v5-sound-
   off-read.png, v6-read5-trace-off.png). Fixed: the power panel buttons (#read, #sound, #motion) do not dismiss the
   hint. (family:curiosity)
6. **Toggles announce element ids; the reset button's name is "0".** src.html:1433 announces `${id} on` ("angle on",
   "log-x on", "keypoints on", "square on"); #home (295) has only a title, so its name is "0" (C/a3-announce.png).
   Done when 9. Fixed: "Degrees" / "Radians", "Log scale on x", "Key points on", "Square grid on", and an aria-label
   such as "Reset axes to minus ten to ten". (general)
7. **Polar and parametric setups draw on unequal axes: circles are ellipses, roses squashed.** `r = 5` on the default
   view draws a 1.74:1 ellipse (P/33-circle-polar.png); the Rose curves and Lissajous setups (src.html:1629-1630) set
   -1.5..1.5 on both axes without Square (P/15-lissajous.png, A/size-1366x768.png). A kid counting petals sees them
   stretched. Fixed: those setups open with Square on; when the first `r =` or parametric line is typed while the view
   is still the default, switch to the square view (the toggle still turns it off). (family:curiosity)
8. **The ruler sweep ignores the ruler's step.** src.html:1187 moves `v.value` continuously, so the Rose setup (step 1)
   shows "a = 6.291" and an unclosed tangle that matches no petal rule (A/ animated-ruler state, P/14-rose.png).
   Words and state disagree. Fixed: when the step is whole or coarse, the sweep dwells on each step value (readout and
   curve on the step); fine steps sweep as now. (family:curiosity)
9. **Read says "y equals x squared .5" for `y = x^2.5`.** src.html:1698: `/\^2\b/` matches inside `^2.5` (and `^3\b`
   inside `^3.1`). Alt-scrubbing the exponent, the spec's first action, produces exactly these (T/t-read.png). Fixed:
   match `^2` and `^3` only when not followed by a digit or a decimal point. (general)
10. **The trace tag and the table say x twice.** Trace tag src.html:1223 reads "Pen 1 · x 1.000 | x 1.000 · y 1.000"
    (P/16-pins.png, 17-tangent.png, A/ trace state); Table header src.html:442 with 1561 reads "x | x | y"
    (T/t-table.png, P/20-table.png). Teaching rated these polish, Play should fix, Craft nit: settled as should fix,
    since every student sees both. Fixed: the parameter column and part appear only for polar and parametric lines;
    for an `f(x) =` line the tag uses the notation the anchor teaches, `f(3.000) = 9.000`, and the table header reads
    `x | f(x)`. (general)
11. **"x / y" under every equation reads as a quotient.** src.html:773 ("x / y", "y / x", "polar · t / r",
    "parametric · t / x / y") and the samples footer src.html:1176 ("x / y unitless"). Seen on every frame
    (P/01-default-pen-mid.png). Fixed: "in x · out y" (and "in t · out r", "in t · out x, y"), or "x → y"; same in the
    footer. (general)
12. **The Table drawer hides the rulers it says it follows.** src.html:163-169 (dialog 610 px wide, lower-left). At
    1366x768 it covers the whole tape, so a, b, k cannot be dragged with the table open; at 680x425 one table row shows
    (P/20-table.png, A/ live-table state at 1366x768 and 680x425). notes.md promises "an open table follows changing
    rulers". Fixed: the table drawer leaves the active line and its rulers visible (for example it sits beside the tape
    over the paper at 1366, and as a shorter bottom sheet at small sizes). Spec puts drawers over the tape; Done when 10
    and the notes' own promise settle that the active line stays usable. (family:curiosity)
13. **The pen is silent and draws only once; the carriage then hides under the power panel.** The spec's first two
    minutes promise a soft scratch while the pen draws (Sound on), and the Look has the carriage running to where the
    pen draws; the only sounds are the button and scrub ticks (src.html:892, 1738), and after the 1.2 s opening every
    typed or setup curve appears at once with the carriage parked at 95 percent of the rail (src.html:1200), behind
    #power at every size (P/01 vs 04, 14, 15; A/size-1366x768.png, size-680x425.png). Fixed: with Motion on, a newly
    typed, loaded or setup curve is inked by the pen with a quiet scratch (Sound on) and the carriage tracks the ink;
    scrubs and ruler drags stay instant (Done when 1); the carriage rests left of the power panel. Motion off: at once,
    no travel (Done when 9). (family:curiosity)

## Polish accepted
1. **Fit readouts say the rate.** Data drawer foot: under an exponential fit also print the growth per x step ("× 1.030
   per year, 3.0 percent"), under a line its slope with units ("1.672 ppm per year"). The Manual's 3.0 percent fact is
   then readable on screen (T/t-co2.png). (general)
2. **R² in log space says so on the readout.** "R² 0.9897 (log space, not comparable with a line's)" instead of the small
   "(log)". (general)
3. **(1 + 1/n)^n entry.** The default ruler -10..10 reaches only 2.594 (T/t-e.png). One sentence in that "Things people
   have found" entry: set n's maximum to 1000. (general)
4. **Words on handles.** "Travel limits" becomes "Axes" (or "Window"); the "Notebook" handle reads "Setups · Notebook" so
   the roses, race, Lissajous and data are findable (P/19-notebook.png). Contents unchanged. "Ready for ink" may stay.
   (family:curiosity)
5. **Number tabs point at their numbers.** Hovering, focusing or dragging a tab highlights its digits in the equation
   (three "2" tabs on `y = 2(x-2)^2` are otherwise alike), and the drag slows to about 12 px a step (now 2 to 7 in
   32 px, P/02, 03). The tab's accessible name or title mentions Alt for tenths. (family:curiosity)
6. **The 2^x race opens showing its point.** The setup turns Key points on, and key-point labels near the paper's foot
   are placed clear of the tick numbers and the edge (P/07-race-keys.png, C/d2-race-keys.png). (family:curiosity)
7. **Read speaks for the ear.** Speak the trace point only while tracing (now it always says "At x equals 1.000",
   src.html:1721-1724, C/v6), and trim trailing zeros ("x equals 1, y equals 1"), as in the spec's example. (general)
8. **Projected sizes.** Tick labels, line labels and key-point labels 12 to 13 px at 1280 wide and up; the 10 px tape
   engraving, end-cap captions and samples footer up a step where they fit (src.html:76, 115, 155, 161). (general)
9. **`|x|` gets a helpful refusal.** "Use abs(x) for absolute value." instead of the generic grammar message.
   (family:curiosity)
10. **First tap on the 2 speaks the hint at once.** The tab's pointerup rebuilds the tape (src.html:892, 751-755), so no
    click fires and the hint waits for the kit's 1.5 s fallback (C/v1-repeat-number.png, d7-firsttap-click.png).
    Refresh the scrubbers in place on a tap without movement. (general)
11. **Units in readouts with data loaded.** Cursor "year 1992 · 371.7 ppm", the trace tag likewise, axis titles from
    the dataset's units (src.html:1335, 1223, 1175; C/d8-data-units.png). (family:curiosity)
12. **Paper focus ring visible.** The canvas outline is clipped by `#paper { overflow: hidden }` and the rail
    (src.html:62; C/a2-canvas-focus.png). Draw an inset outline or a focus frame inside the paper. (general)
13. **Pen numbers on the paper.** A small pen number at each curve's end, so close inks (green and teal, brown and
    orange) tie to their tape lines (C/d9-eight-lines-1366.png). (general)
14. **Exponent notation.** Ticks and key-point labels show `6.00×10^18`, not `6.00e+18`, on an instrument where e is
    2.718 (T/t-race.png); values within the tolerance of zero print 0.000. (general)
15. **Cursor readout before the pointer arrives.** Blank (or "x · y") instead of "x 0.000 · y 0.000". (general)
16. **760x900: the power panel covers "No. 08" and the carriage label** (A/size-760x900.png). Move one clear. (general)
17. **The aliasing warning sits on the "y" axis label** (P/10-alias.png). Place it clear of the label. (general)

## Settled calls
- Duplicate x in the trace tag and table header: three levels across lenses; settled as one should fix (item 10).
- Pen scratch and pen travel: Play said should fix, Craft polish. The spec's first two minutes and Look promise both, so
  should fix (item 13), merged with Craft's carriage-under-panel polish. Scope kept to newly inked curves so live scrubs
  stay at 60 fps.
- Table drawer: the spec puts drawers over the tape; that layout stays for Data, Manual and Notebook. Only the Table
  drawer moves, because its own promise (following rulers) needs the rulers in view.
- Square view: only the polar and parametric setups, and a typed first polar or parametric line on the default view.
  Ordinary y lines keep the -10..10 view.
- Audit leads judged wrong by all three lenses, not to change: the first-run hint over #plot, trace and pin tags over
  #plot, drawers over the tape (except item 12), "hint out of view" after the first action, scrolling panels in the
  Manual and Data drawers, the 375 "+" icon button, the welcome cut by a first tap (BASELINE rule 16).
- Census note ("early censuses excluded many Indigenous people", Manual src.html:385-394 and notes.md, with the
  Censuses of American Indians link): not judged in this merge. It goes to the fresh-agent sensitivity review
  (BASELINE rule 5). Codex leaves the wording as is.
- No goal, score, challenge or finish was added anywhere in this list (CODEX-CURIOSITY.md).

## To the spec's open questions
- **Module standards (rule 2).** Not exercised: F-IF.A.3 (sequences as functions, recursive; recursive definitions are
  refused today), F-IF.B.4 in context (Key points ignore data and fitted curves), F-IF.B.5 (domain in context). No small
  activity clearly fits without changing the spec. Options: a sequence form (`a(n) = 2a(n-1)`, `a(1) = 3`, dots on
  integer n with a table); Key points and Trace on the fitted curve ("when does the Mauna Loa quadratic reach 450
  ppm"); or move these codes to graph-story-lab or another module tool that teaches them in full. Lean: Trace and Key
  points on the fitted curve here (it is the instrument's own move) and move F-IF.A.3 and F-IF.B.5 to another tool,
  never a thin Manual entry.
- **Spec data list.** The spec's Census figures for 1940, 1970 and 1980 (132.16, 203.30, 226.54) are older values;
  notes.md and the bundle use the Bureau's current table (132.17, 203.21, 226.55), checked by Teaching. Update the spec.
- **`|x|` as grammar** (Play 13): accept bars for absolute value? Lean: yes, a later fix round; polish 9 covers the
  message now.

## Not taken
- Race setup inset or second zoomed setup page (Play 10): adds a seventh setup; polish 6 covers the opening.
- Header row of pasted columns as axis names (Play 17): a nice new behaviour, not cheap; later.
- Domain-in-context "Things people have found" entry (Teaching 3): a thin activity for a code, which rule 2 forbids;
  see open questions.
- "Ready for ink" wording (Teaching 11): plotter flavour, harmless once the other words are plain.

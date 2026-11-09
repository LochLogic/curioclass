# Play lens: graph-studio (Curiosity No. 08), round 1

Cold lens, 2026-11-06. Played twice: as a grade 9 student alone at home (nothing assigned, nothing read first) and as
a teacher projecting it at 1366x768. Judged against CODEX-CURIOSITY.md and VISION.md "Curiosities: the second shape",
plus POLISH.md and STANDARDS.md where they still bind.

My frames: `S:/CurioClass-codex-scratch/graph-studio/play/frames/` (shots1.json and shots2.json beside them, run with
`scripts/drive.py --port 9421`). Shared audit: `S:/CurioClass-codex-scratch/graph-studio/audit-r1/`.

## Short test

- **Would a kid open it unassigned?** Yes, narrowly. The first action works with nothing read: drag the gold 2 and the
  bowl snaps to an S and a cliff (02-drag-exponent.png). Typing `a` makes a ruler at once (04-type-a.png). The pull
  that would hook a kid (roses, Lissajous, the 2^x race, real CO2) sits behind a button called Notebook (see item 8).
- **Would an adult play with it for fun?** Yes. It is a real grapher: f and g that call each other, f(4) = 4.000,
  polar, parametric, pins with average rate of change, tangent slope, key points, log axes, least-squares fits on real
  NOAA, NASA and Census data, paste your own columns. Planets on log-log give y = 1.000 x^1.500, R² 1.0000 (11-planets.png).
- **Is the real thing the interface?** Yes: the paper, the ink and the numbers are the whole tool. No decoration.
- **Does it work with no finish line?** Yes. No score, goal, level, sticker, quiz or finish screen anywhere; lesson
  creep is absent. The only first-run element is the quiet hint, gone after the first action.

Nothing here fails the short test. Depth a month of use would still find: yes (f/g composition, polar petals rule,
holes at removable discontinuities, the third 2^x crossing at -0.9371, log-space R² on the population series).

## Findings

### Should fix

1. **The Table drawer hides the rulers it claims to follow.** `src.html:163-169` (dialog 610 px wide, anchored
   lower-left). notes.md says "An open table follows changing rulers", but at 1366x768 the Table drawer covers the
   whole tape, so rulers a, b, k cannot be dragged while the table is open; at 680x425 it also covers the paper, with
   one table row visible. Seen: audit `state-live-table-1366x768.png`, `state-live-table-680x425.png`, my 20-table.png.
   Better: dock the table over the paper's right side (or under the active line), leaving the active line and its
   rulers in view. Tag: family:curiosity.

2. **Polar and parametric curves draw on unequal axes, so a circle is an ellipse.** Default view is -10..10 on both
   axes over a 1064x610 paper; `r = 5` draws a 1.74:1 ellipse (33-circle-polar.png). The Rose curves and Lissajous
   setups (`src.html:1629-1630`) set -1.5..1.5 on both axes without Square, so every rose is stretched sideways (audit
   `state-animated-ruler-1366x768.png`, my 15-lissajous.png). A kid counting petals sees squashed petals and a circle
   that is not round. Better: polar and parametric setups open with Square on, and typing an `r =` line could offer it.
   Tag: family:curiosity.

3. **The trace tag says x twice.** `src.html:1223`: for y = f(x) the tag reads "Pen 1 · x 1.000 | x 1.000 · y 1.000"
   (audit `state-trace-1366x768.png`, my 16-pins.png, 17-tangent.png). The parameter column only means something for
   polar and parametric. Better: "Pen 1 · x 1.000 · y 1.000" for y and x lines, the t part only when there is a t.
   Tag: general.

4. **The table header repeats x: "x | x | y".** `src.html:442` and `1561`, same cause as item 3 (my 20-table.png,
   audit `state-live-table-*`). A grade 9 student reads two identical columns and wonders what differs. Better: hide the
   parameter column unless the line is polar or parametric. Tag: general.

5. **"x / y" under every equation reads as division.** `src.html:773` labels each line "x / y", "polar · t / r",
   "parametric · t / x / y", and the sampling readout says "x / y unitless" (`src.html:1176`). In a maths tool a slash
   between letters is a quotient; under `y = x^2` "x / y" looks like a second expression. Seen on every frame (e.g.
   01-default-pen-mid.png). Better: "input x, output y", "x → y", or "in x · out y". Tag: general.

6. **The ruler sweep ignores its step, so the rose setup shows off-step values and broken roses.** `src.html:1187`
   moves `v.value` continuously. The Rose curves setup sets step 1 for petal counting, yet the sweeping ruler reads
   "a = 6.291" with step 1 (audit `state-animated-ruler-1366x768.png`, `-375x812.png`: "a = 6.333") and the curve is an
   unclosed tangle that matches no petal rule. Words do not match the state (POLISH, Consistency). Better: when the
   step is whole or coarse, the sweep dwells on each step value (or snaps the readout and curve to the step).
   Tag: family:curiosity.

7. **The pen is silent, and it only travels once.** The spec's first two minutes promise the pen drawing "with a soft
   scratch (Sound on)"; the only sounds are a click tone on buttons and a tick at the end of a scrub (`src.html:892`,
   `1738`). After the 1.2 s opening the carriage never draws again: typed or setup curves appear instantly, so the pen
   plotter that gives the tool its look stops being a plotter (01 vs 04, 14, 15 frames: carriage parked top-right). A
   flat moment exactly where the first reaction should land. Better: a short scratch while the pen inks a newly typed
   or loaded curve (Motion on), and the carriage tracking that ink. Tag: family:curiosity.

### Polish

8. **The best material is hidden behind "Notebook".** Rose curves, the 2^x race, Lissajous, Mauna Loa and Planets
   live inside the Notebook drawer, a name that reads as "saved pages" (19-notebook.png). A kid exploring alone will
   try Data, Table and Travel limits before guessing that Notebook holds the fun. "Travel limits" is also plotter
   jargon a grade 9 student will not decode as "axis range". Better: a "Setups" handle (or a setups strip at the foot of
   the tape) and "Paper limits" or "Axes". Tag: family:curiosity.

9. **Number tabs are detached from their numbers.** `src.html:738` renders each number as a tab under the equation,
   labelled only with its value. `y = 2(x-2)^2` gives three identical "2 ↕" tabs with no clue which is which. Drag
   steps are whole units (2 to -2 in a 30 px drag, 03-drag-exponent-down.png; 2 to 7 in 32 px up, 02), so the spec's
   "drag it to 0.5 and half the curve vanishes" is unreachable without the Alt key, which only the Manual mentions.
   Better: highlight the matching digits in the equation while a tab is hovered or dragged, and slow the drag (about
   12 px a step). Tag: family:curiosity.

10. **The 2^x race opens with its point hidden.** The setup does not turn Key points on, and at its 6e18 scale the
    first two crossings sit on the bottom edge. With Key points on, three labels pile up over the x tick numbers at the
    foot of the paper and the -0.9371 label is half under the edge (07-race-keys.png). Better: open with Key points on
    and a small inset or a second setup page zoomed near x = 1. Tag: family:curiosity.

11. **Read speaks readout formatting, and a point nobody chose.** Read says "At x equals 1.000, y equals 1.000" (audit
    one-held-click row 10) even when the trace pen is off: it reads the default trace point. "One point zero zero zero"
    is hard on the ear. Better: speak trimmed numbers ("x equals 1, y equals 1") and only when tracing. Tag: general.

12. **Projected, the numbers are small.** Tick labels, line labels and key-point labels are 11 px monospace; from the
    back of a classroom at 1366x768 the axis numbers and "x / y" are hard to read (01, 08 frames). Better: 12 to 13 px
    ticks at 1280 wide and up. Tag: general.

13. **`|x|` is refused with a generic message.** "Use numbers, letters and the listed mathematical operators." Kids
    type bars for absolute value. Better: accept `|x|`, or say "Use abs(x) for absolute value." Tag: family:curiosity.

### Nits

14. Cursor readout shows "x 0.000 · y 0.000" before the pointer has touched the paper (every frame); blank or "x ·
    y" until then reads truer. Tag: general.
15. At 760x900 the power panel covers "No. 08" on the rail label and the carriage label (audit `size-760x900.png`).
    Tag: general.
16. The aliasing warning sits on top of the "y" axis label in the paper's top-left corner (10-alias.png). Tag: general.
17. Pasted columns with a header row ("time distance") drop the header and the readout stays "x / y unitless"
    (41-paste). Using the header as axis names would be a small delight. Tag: family:curiosity.

### Checked and fine

f(x) = x^2 - 3x then f(4) prints "f(4) = 4.000". Pins at x = 1 and 3 read Δy/Δx = 4.000. Tangent at x = 2 reads slope
4.000. Mauna Loa line R² 0.9806, quadratic 0.9995. Planets power exponent 1.500. tan(x) and 1/x break at poles;
sin(x)/x shows an open circle at (0, 1) (09-breaks.png). sin(1000x) shows the sampling warning. Zoom to ±6.5e6 and
±5.7e-11 stays sane. Motion off: the play button says "Motion is off. Turn Motion on to sweep a ruler." Enter adds a
line and moves focus. No console errors in 41 shots. The Manual's "Things people have found" already names the third
2^x crossing near -0.9371.

## Audit pilot

- **Leads confirmed:** Table drawer covering the tape and rulers (`keep region #equation-0` in live-table): confirmed
  and reported as item 1. Ruler end caps cut by the tape scroll at 680x425 and 375x812: confirmed, but the tape scrolls
  and the cursor stays visible, so not reported.
- **Leads wrong:** "#plot / #hint overlap" at every size: the hint is meant to sit on the paper. "#plot / #trace-tag and
  #pin-tag overlap": the tags ride on the paper by design. "#add text under 10 px" at 375: an icon "+" button with an
  aria label. "Welcome not heard" after a first tap: allowed by BASELINE rule 16; the hint stays reachable by Read.
  Manual and Notebook covering the tape: drawers over the tape are the spec's layout.
- **What it missed:** circles drawn as ellipses on unequal axes (item 2), the duplicated x in the trace tag and table
  header (items 3, 4), the sweep ignoring the step (item 6), the silent one-shot pen (item 7), labels piling up in the
  race setup (item 10), and every word-level issue ("x / y", "Notebook", "Travel limits").

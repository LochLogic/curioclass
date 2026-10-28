PASS
Counts: blockers 1 (general 1, family 0), should fix 15 (general 11, family 4), polish accepted 7

# simulation-studio: Refine

Lens files: refine/teaching.md (T), refine/play.md (P), refine/craft.md (C). Read them for frames and detail.

## Blockers
1. **pairsOf pairs across dropped rows** (T-B1, P-B1; src.html:426). Whenever Drop is in the recipe, even in the right
   order (Pair, then Drop), neighbouring rows of the cleaned log are paired: Real pairs read 3, 78, 79, 60 instead of
   0, 104, 105, 89, Fill gives 0.96 and 0.43, and "never short then short" can't play. The tool makes the pairing error
   it teaches. Pair by the original row order (a pair exists only if both eruptions were next to each other in the
   raw log and both survive cleaning). Recompute the pairs table and Fill for every recipe order against Python.

## Should fix
2. **Drop's cost is invisible** (T-S1). Dropping removes 78 night eruptions (26%; classes 104/194 to 82/139) with the
   same scatter, r and hint as Flag. Show the rows lost and what they were, so Drop and Flag differ on screen.
3. **The recipe "code" isn't valid pandas** (T-S2). 9-12 works like the real thing: make every line run in pandas
   (isin, boolean masks, assign or a new column), or label it pseudocode. Prefer real pandas.
4. **The simulated summer looks like a second test** (T-S3). It is built from the same 1985 numbers as the sign, and
   269 of 298 is in sample. Say what a simulation can and can't show, and add a real out-of-sample check (fill from
   the first 150 eruptions, test on the other 148: 131 of 148, 89%). Recompute.
5. **The raw r = -0.64 is called "backwards"** (T-S4). It is a real pattern (short eruptions are always followed by
   long ones). Frame it truthfully, and name the column "waiting" as in the data.
6. **Sources** (T-S5). The NPS URL in tool.draft.json is a 404. Use the confirmed sources (the YELL_003 worksheet PDF
   and predict7.htm) and the MASS data citation.
7. **3A-DA-11 (create interactive visualizations) is barely taught** (T-S6; rule 2). Check the code text. Settled with
   BASELINE (standards taught well): if it stays, the student makes a chart choice that matters (which columns on the
   scatter, bin width on the histogram, or similar); otherwise move the code off the module and record it in
   handoff.md for the integrator.
8. **A model from the uncleaned log** (P-S1). The hint loops ("tap Fill from my clean log" with an empty recipe) and
   never names Clean; seeds 17, 19, 44, 49 and 55 reach 85% and praise the backwards model. Name Clean, and no praise
   for a model filled from an uncleaned log.
9. **"Order matters. Try moving one." with one step** (P-S2, C-S2). Wait for a second step.
10. **Raw log scatter below the fold at 680x425 and 800x500** (P-S3, C-S1; Done when 8). The r = -0.64 hook is on the
    first screen at every size.
11. **At 760 (stack) and 375 the hint and main controls sit below the charts** (P-S4). The first screen says what to
    do.
12. **"Read the data notes" plays on any page change** (C-S3). Only when the notes are the next action; don't spend
    the once-only line on a chip jump.
13. **Engine table controls under 44 px outside the 9-12 theme** (C-S4; family:data-desk). Editable cells, remove x
    and add row at least 44 px in every theme, as the doc says.
14. **Grouped bar charts** (C-S5; family:data-desk). groupLabels honoured, a legend, groups told apart by more than
    color, and a text alternative with readable names.
15. **fmt puts separators in years** (C-S6; family:data-desk). A year or format option, so 2000 reads 2000.
16. **Box plot pick layer says left and right but uses Up and Down** (C-S7; family:data-desk). Make them agree.

## Polish accepted
17. After a rule change the old "Match" fades or says it is stale (P).
18. The legend says "Real, cleaned log" only when cleaning steps exist (P).
19. The last Model slider is on screen at 1366x768 (P).
20. No blank band under the Clean hint (P).
21. No real-log result sliver before any test (P, C).
22. Night-code cells marked by more than grey text (C).
23. Histogram axis titles clear of the top tick label (P nit).

Nits are optional; fix the cheap ones (the dead ternary at src.html:631, hard-coded legend colors, engine and doc
drift). Fix Done when 1 in the spec to r = -0.64 and the summer range to the recomputed one.

## Settled calls (builder's questions, settled with BASELINE; Cory may overrule)
- A published research data set (Azzalini and Bowman 1990, R's MASS), tied to the real NPS prediction, is an
  acceptable public source: its real flaws are the lesson.
- 299 rows with paging stays: trimming would remove the flaws the tool teaches. The family doc notes the exception.
- Old Faithful belongs to simulation-studio; data-desk-distributions and data-detective pick other data sets (the
  integrator notes it in their specs before they are built).
- t.validate(dictionary) for catalog-column-rules is built with that tool, not now.

## Exit check, round 1 (2026-10-28, fresh cold agent)

Bundle `CURIO_DRAFT=1 python scripts/bundle_tool.py simulation-studio`: 161 KB, one file. No console errors or
exceptions in any driven page, and no network requests. Own Chrome profile on port 9780; 375 wide through
`drive.py --host`; host.html deleted after.

### Numbers (Python, from the Rdatasets CSV; the embedded data is identical)
- Raw r -0.6446, waiting = 99.31 - 7.80 x duration. Pair 0.8885 (34.95 + 10.78x, classes 55.6 and 81.2); Pair, Flag
  0.8980 on 221 (34.88 + 10.63x); Drop then Pair 0.8164 on 220 with 26 wrong pairs (classes 56.8 and 81.0). Flag
  only or Drop only -0.6869. Night codes 78 (23, 2, 53).
- Every recipe order: real pairs 0/104/105/89 without Drop, 0/75/71/48 with Drop. Fill, seed 1 Match and sign agree
  with the tool: Pair or Pair, Flag .8903 and 269; Pair then Drop .8841 and 267; Drop before Pair .8344 and 269
  (57, 81); raw fill .8395 and 49. Simulated pairs at seed 1: 0/100/100/98.
- Match yardstick, seeds 1-200, 5th to 95th percentile: clean fill against real 79-86 / 85-93 / 91-97 at 2 / 5 / 10
  minute bins; two runs of one geyser 79-87 / 86-94 / 89-97; seed 1 .857 / .890 / .948. Start rules .656. Both
  chances .65: .902 with short then short 37 (25 to 46 over seeds).
- Signs on the real log: 56/81 gives 163, 269 and 294 at windows 5, 10 and 15; 72 gives 60, 136 and 205; 83/66
  gives 49. Out of sample (fill rows 1-150, test the other 148): 131 of 148 (56/81 from the first half; 57/81 with Drop
  before Pair, also 131); raw fill 83/66 gives 25.
- Summer (1,830 eruptions): seed 1 1,616 (88.3 percent, 91.7 days); seeds 1-200 86.6 to 90.7, seeds 1-50 86.8 to
  90.5. Done when 6 (87 to 91 whole percent) holds.
- The three recipe lines run as written in pandas on the CSV, with the same rows and r as the tool. The 2:01 (twice),
  2:02, 4:01 and 4:02 neighbours in notes.md are real.
- Sources: the YELL_003 PDF (68 and 94 minutes), predict7.htm (about 90 percent within plus or minus 10 minutes) and
  the Rdatasets doc (night codes, the 7.3-30 correction) all load and say what is claimed.
- The statistics teaching is honest. The raw r is framed as a real relation to a different question (the wait before).
  The real-log result is labeled in sample. The out-of-sample row says it refits from the first 150 and tests the other
  148. The summer says it is built from the same 1985 numbers. Match is defined as histogram overlap with its bin
  width and a sample-size yardstick. No praise for a raw or wrong-order model.

### Merged list, item by item
1. Blocker, pairs: fixed. Pairs follow file adjacency, every order matches Python, and the UI with Drop shows
   0/75/71/48.
2. Drop's cost: fixed (78 dropped, classes 82 and 139, were 104 and 194; Flag has its own line).
3. Real pandas: fixed (run in pandas).
4. Out of sample and summer caveat: fixed (131 of 148).
5. "Backwards" r: fixed on screen. notes.md still says the raw class means are "backwards" against the rangers' rule,
   explained right after (nit).
6. Sources: fixed.
7. 3A-DA-11: kept with a real chart choice (2/5/10 minute bins change the chart, Match and the yardstick). Accepted.
8. Uncleaned model: fixed (rawModel and orderModel name Clean, no praise).
9. Recipe line waits for a second step: fixed.
10. Raw scatter on the first screen at 680x425 and 800x500: fixed.
11. Stack (760, 375): hint and main controls above the charts: fixed.
12. Notes line only on a student page turn: fixed (not spoken on a chip jump or a marked Next).
13. Table controls 44 px: fixed. In a harness with editable, removable, addRow and paging, with and without
    theme-912, no control is under 44 px.
14. Grouped bars: fixed (legend with swatch, shape and label; shapes on bar tops; dashed second series; text
    alternative uses the labels).
15. Years: **partly open.** A `'year'` column prints plain in tables, scatter and line ticks and text, and histogram
    and box ticks, and `fmt(n, d, {group: false})` works. But the histogram text alternative formats bin edges with
    `fmt` ("1,990 to 2,000"), the box plot text formats its five numbers with `fmt` ("minimum 1,991"), and the dot plot
    text uses `fmt` ("1,991, 2,000"). So neither a year column nor `xFormat` reaches those three text alternatives
    (kit/data-desk.js, drawHist, drawBox and drawDot). The family doc says years print plain "in tables, axes ... and
    text alternatives" and that `xFormat` covers "the text alternative". A screen reader hears "one thousand nine
    hundred ninety". Fix: use the axis formatter in those three text alternatives. Should fix, family:data-desk.
16. Box pick keys: fixed (label and keys both up and down).
17. Stale Match: fixed ("(last run)", dimmed).
18. Legend: fixed ("Real, raw log" until a step exists).
19. Last Model slider at 1366x768: fixed.
20. Clean hint band: smaller (about 38 px at 1366x768). Polish, known.
21. Real-log sliver before a test: fixed.
22. Night-code cells: fixed (moon mark and a key under the table).
23. Histogram axis titles clear of the top tick: fixed.
Spec Done when 1 (-0.64) and Done when 6 (87 to 91): fixed.

### Done when
1 to 8 pass in the bundle, with real held clicks: 299 rows and r = -0.64; 0.89 with 55.6 and 81.2, Flag 0.90 on 221;
the wrong-order warning, rings and 0.82; Match 89 percent with 0/100/100/98, and both .65 gives 90 percent with 37;
signs 269, 136 and 49; summer 88 percent; voice (below); pipeline, main chart and main button on screen at 1366x768
and 680x425, with outline and circles against fill and triangles.

### Layout (680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812, every bench)
No horizontal scroll, no clipped hint, and no target under 44 px (the night codes checkbox is 20 px inside a 44 px
label). The builder's two open points, judged:
- Compact sizes scroll inside the bench (680x425: tables and Answer results sit below the fold). Done when 8 and
  STANDARDS hold: the pipeline, main chart and main button are on screen at these preview sizes. Not open.
- Model at 1280x720: the panel overflows by 41 px and the last slider (spread after a long eruption) is half cut. Run,
  New run, Fill and Reset are on screen, Fill sets all six, and 1366x768 fits. Polish, not a should-fix (known, not
  done). Same kind: the Model panel at 1000x625 (55 px) and the Answer bench at 1280x720 (30 px, the park line).
- New nit: at 760 (stack) the Clean scatter and histogram are drawn at about half the box width.
Keyboard: pipeline tabs move with arrows, focus is visible (4 px), and Alt+Up moves a step with focus kept. Motion off:
no pulse, same numbers.

### Voice (drive.py, held clicks, Sound on, browser voice)
| Line | Kind | Expected | Spoken at a 2 s gap | Spoken at a 6 s gap |
|---|---|---|---|---|
| notes (5 Next presses) | how | 1 | 1 | |
| recipe (2nd step, then moves) | how | 1 | 1 | 1 |
| modelHow (first Model visit) | how | 1 | 1 | 1 |
| answerHow (first Answer visit) | how | 1 | 1 | |
| bins (5 width changes) | how | 1 | 1 | |
| dropFirst (Drop moved above Pair 5 times) | event | 5 | 2 (3 made stale by the move back) | 5 |
| never (Run 5 times) | event | 5 | 3 (queued ones replaced by the next run) | 5 |
| rawModel (Run 5 times, no recipe) | event | 5 | 2 to 3 (same) | 5 |
| onTime (Test 5 times) | event | 5 | 3 to 4 (same) | 5 |

At a 2 s pace an event line (2 to 3 s long) is still queued when the next tap comes; the queued one is dropped and the
newest result is spoken, so the latest result is always heard and nothing plays late. That is the stale rule; with a
gap longer than the lines every event is spoken 5 of 5. A fast stale run dropped every superseded line. First taps:
a stage tap gives the welcome at about 0.1 s; Next gives only the notes line; a bench tab gives only its welcome; Read
speaks the hint; Sound off says nothing, and Sound back on brings the skipped welcome once. Read cuts a playing line
and works with Sound off. allLines() equals voice/lines.json (326 lines), none over 200 characters, no em dashes.
`python scripts/test_voice.py`: 42 passed.

### Engine (kit/data-desk.js 1.1 against docs/families/data-desk.md, function by function, harness with and without
theme-912)
DataTable (types, on, batch, add, set parsing number and year, remove, replace, values, column, stats, count, crosstab,
label, where, renderTable with page, editable, removable, addRow, and onPage `{user}`), Chart (scatter, line,
histogram with overlay, share, tops and faded, box with groupLabels, grouped bar with legend, dot; fit, highlight,
onPoint, pick, text starting with the title) and DataDesk (fmt with and without group, nice, stats, linreg, and fits
equal to numpy) all work as written, except item 15.

### Gate
1 Done when: pass. 2 Codes: pass. 3 Solo defaults: pass. 4 Sensitivity: does not apply. 5 No open should-fix:
**fails on item 15** (family:data-desk). 6 Bundle: pass. 7 Voice counts: pass.
Known, not done (polish): Model panel at 1280x720 and 1000x625, Answer bench at 1280x720, Clean hint band, half-width
Clean charts at 760, "backwards" in notes.md. Side note: an accidental `scripts/check_tools.py --help` run rebundled
five other tools' ignored .html outputs (animal-moves to calm-corner) before it was stopped; no source changed.

## Exit check, round 2 (2026-10-28, item 15 only)

Item 15: fixed. kit/data-desk.js now formats the histogram bin edges, the box plot five numbers and outliers, and the
dot plot values with `fx`; the rebundled simulation-studio.html (167,548 bytes) carries the same code. Harness pages
with and without theme-912, no errors:
- Year column: "1990 to 1995: 5", "minimum 1990, ... maximum 2001" (also grouped boxes), "1990, 1991, ... 2001"; share
  and overlay histograms too. Ticks stay plain (1990, 1992 ...).
- `xFormat` (v -> "~v u"): reaches all three text alternatives, outliers included ("outliers ~40 u").
- No regression on plain numbers: "0 to 20,000", "minimum 12,500", "98,000" keep their separators.
- In the tool: the Clean histogram and box alternatives read as before (40 to 45: 1, 45 to 50: 15 ...; minimum 69,
  median 83), no console errors.
Nits, not blocking: the mean and median mark labels drawn on a histogram still use `fmt` ("mean 1,994.43" on a year
column); the tool's box alternative reads "Waits by class. Box plot of . after short ..." because it passes
`xLabel: ''`.
Gate 5 now clear; all seven gate points pass.

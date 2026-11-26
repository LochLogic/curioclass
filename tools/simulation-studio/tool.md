# Simulation Studio: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Refine

<!-- part: refine.md -->

PASS
Counts: blockers 1 (general 1, family 0), should fix 15 (general 11, family 4), polish accepted 7

### simulation-studio: Refine

Lens files: refine/teaching.md (T), refine/play.md (P), refine/craft.md (C). Read them for frames and detail.

#### Blockers
1. **pairsOf pairs across dropped rows** (T-B1, P-B1; src.html:426). Whenever Drop is in the recipe, even in the right
   order (Pair, then Drop), neighbouring rows of the cleaned log are paired: Real pairs read 3, 78, 79, 60 instead of
   0, 104, 105, 89, Fill gives 0.96 and 0.43, and "never short then short" can't play. The tool makes the pairing error
   it teaches. Pair by the original row order (a pair exists only if both eruptions were next to each other in the
   raw log and both survive cleaning). Recompute the pairs table and Fill for every recipe order against Python.

#### Should fix
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

#### Polish accepted
17. After a rule change the old "Match" fades or says it is stale (P).
18. The legend says "Real, cleaned log" only when cleaning steps exist (P).
19. The last Model slider is on screen at 1366x768 (P).
20. No blank band under the Clean hint (P).
21. No real-log result sliver before any test (P, C).
22. Night-code cells marked by more than grey text (C).
23. Histogram axis titles clear of the top tick label (P nit).

Nits are optional; fix the cheap ones (the dead ternary at src.html:631, hard-coded legend colors, engine and doc
drift). Fix Done when 1 in the spec to r = -0.64 and the summer range to the recomputed one.

#### Settled calls (builder's questions, settled with BASELINE; Cory may overrule)
- A published research data set (Azzalini and Bowman 1990, R's MASS), tied to the real NPS prediction, is an
  acceptable public source: its real flaws are the lesson.
- 299 rows with paging stays: trimming would remove the flaws the tool teaches. The family doc notes the exception.
- Old Faithful belongs to simulation-studio; data-desk-distributions and data-detective pick other data sets (the
  integrator notes it in their specs before they are built).
- t.validate(dictionary) for catalog-column-rules is built with that tool, not now.

#### Exit check, round 1 (2026-10-28, fresh cold agent)

Bundle `CURIO_DRAFT=1 python scripts/bundle_tool.py simulation-studio`: 161 KB, one file. No console errors or
exceptions in any driven page, and no network requests. Own Chrome profile on port 9780; 375 wide through
`drive.py --host`; host.html deleted after.

##### Numbers (Python, from the Rdatasets CSV; the embedded data is identical)
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

##### Merged list, item by item
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

##### Done when
1 to 8 pass in the bundle, with real held clicks: 299 rows and r = -0.64; 0.89 with 55.6 and 81.2, Flag 0.90 on 221;
the wrong-order warning, rings and 0.82; Match 89 percent with 0/100/100/98, and both .65 gives 90 percent with 37;
signs 269, 136 and 49; summer 88 percent; voice (below); pipeline, main chart and main button on screen at 1366x768
and 680x425, with outline and circles against fill and triangles.

##### Layout (680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812, every bench)
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

##### Voice (drive.py, held clicks, Sound on, browser voice)
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

##### Engine (kit/data-desk.js 1.1 against docs/families/data-desk.md, function by function, harness with and without
theme-912)
DataTable (types, on, batch, add, set parsing number and year, remove, replace, values, column, stats, count, crosstab,
label, where, renderTable with page, editable, removable, addRow, and onPage `{user}`), Chart (scatter, line,
histogram with overlay, share, tops and faded, box with groupLabels, grouped bar with legend, dot; fit, highlight,
onPoint, pick, text starting with the title) and DataDesk (fmt with and without group, nice, stats, linreg, and fits
equal to numpy) all work as written, except item 15.

##### Gate
1 Done when: pass. 2 Codes: pass. 3 Solo defaults: pass. 4 Sensitivity: does not apply. 5 No open should-fix:
**fails on item 15** (family:data-desk). 6 Bundle: pass. 7 Voice counts: pass.
Known, not done (polish): Model panel at 1280x720 and 1000x625, Answer bench at 1280x720, Clean hint band, half-width
Clean charts at 760, "backwards" in notes.md. Side note: an accidental `scripts/check_tools.py --help` run rebundled
five other tools' ignored .html outputs (animal-moves to calm-corner) before it was stopped; no source changed.

#### Exit check, round 2 (2026-10-28, item 15 only)

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

<!-- end part -->

<!-- part: refine/craft.md -->

### Craft lens: simulation-studio (round 1)

Cold read of spec.md, src.html, notes.md, art/prompts.json, voice/lines.json, kit/data-desk.js and
docs/families/data-desk.md. Bundled with `CURIO_DRAFT=1 python scripts/bundle_tool.py simulation-studio` (149 KB).
Driven with `scripts/drive.py` (muted headless Chrome, own profile, ports 9760-9769, held clicks 0.12 s), plus a
light-theme harness page that loads only kit/curio.css, kit/curio.js and kit/data-desk.js to exercise the engine API the
siblings will use. The pairsOf blocker (src.html:426, pairs across dropped rows) is already reported by Teaching and
Play and is not repeated here. Placeholder art and the browser voice are expected and not reported.

Counts: blockers 0, should fix 7 (general 3, family 4), polish 2, nit 3.

#### Contract

- One file, 149 KB, no external src/href (only `kit:` names inside comments), no fetch/XHR/WebSocket. The three inline
  scripts pass `node --check`.
- Kit used, not re-implemented: tables and charts are `DataTable`/`Chart`, fits are `chart.fit('linear')`, class stats
  are `DataDesk.stats`, narration is `Curio.voice`.
- No console errors or exceptions in 30+ driven tabs: every bench at 1366x768, 1280x720, 1920x1080, 1000x625,
  800x500, 680x425, 760x900 and 520x800, a full workflow (wrong order, fix, flag, show night, marks, fill, runs with
  extreme rules, sign fill and tests, mark stepping, remove every step) with Motion on and off.
- Every change recomputes well under the spec's 150 ms (add step 49 ms, move 33, run 8, test 1).

#### Engine against the family doc (kit/data-desk.js vs docs/families/data-desk.md)

Fits checked against numpy on the geyser data (Python `np.polyfit`, `np.corrcoef`):

| Fit | n | numpy a, b, r | engine a, b, r |
|---|---|---|---|
| raw, same row | 299 | 99.309856, -7.800326, -0.644623 | identical to 6 decimals |
| Pair | 298 | 34.945157, 10.775100, 0.888487 | identical |
| Pair, Flag (night rows faint) | 221 | 34.876177, 10.628622, 0.898028 | identical |
| quadratic (Pair) | 298 | 21.008186, 20.837429, -1.571588; r2 0.797696 | identical |
| exponential (Pair, fitted on ln y) | 298 | a 40.709835, b 0.159907; r2 on y 0.776127 | identical |

`stats` matches numpy sd (n-1) and population sd, school-rule quartiles, MAD, 1.5 IQR fences and whiskers. `fmt` gives
a true minus, no "−0.00". DataTable `set` (text to number, '' to null), `count` in the column's `values` order,
`crosstab`, `where`, `label`, inferred types, `batch`; renderTable paging with aria-disabled ends, `onRow` 44 px row
buttons, `rowClass`/`cellClass`; Chart into a `<g>` (svg left to the tool), scatter/line/dot/box/bar/histogram,
`overlay`, `share`, `tops`, `faded`, `marks`, `bands`, multi-y lines, `highlight`, `pick`, `onPoint`, keyboard picking
(histogram bin 50 to 55 by three Right arrows and Enter marks 38 rows, as the data says) and calm mode (no tween, no
pulse) all behave as documented. The issues are below (findings 4 to 7).

#### Access

- Keyboard: Tab reaches every control on every bench in a sensible order (header, the selected pipeline tab, bench,
  panel); pipeline tabs move with arrow keys and wrap; Alt plus Up moved Flag above Pair and kept focus on its button;
  the histogram pick layers take arrows, Enter and Escape. Every stop showed the kit's 4 px focus outline.
- Targets: every button and input measured 44 px or more at all sizes (the Show night codes checkbox is 20 px, but its
  label row is 44 px and clickable).
- Color is not the only signal: real vs simulated is outline plus circle vs fill plus triangle; wrong pairs carry a
  ring plus the warning line; marked rows carry a background plus a ▶ glyph. One weak spot is in polish 2.
- Motion off: no histogram tween (bar heights identical across frames), no arrow pulse, no recipe flash. Sound and
  Read: see the voice check.

#### Standard voice check

Held clicks, Sound on, Motion on. Gaps of 8 s for the repeat runs (a 4.5 s first try was shorter than a how-to plus
an event, so queued events went stale, as they should). Log read from `__tool.vlog`.

| Line | Kind | Action, five times | Expected | Spoken |
|---|---|---|---|---|
| notes (line 2) | how | Next page | 1 | 1 |
| recipe (line 3) | how | add Pair, remove it | 1 | 1 (then silent x4) |
| pairDone (line 4) | event | add Pair | 5 | 5 |
| dropFirst (line 5) | event | move Pair below Drop | 5 | 6 of 6 |
| pairDone (line 4) | event | move Pair above Drop | 5 | 5 of 5 |
| modelHow (line 6) | welcome | visit Model | 1 | 1 |
| answerHow (line 9) | welcome | visit Answer | 1 | 1 |
| noMatch | event | Run (start rules) | 5 | 5 |
| noMatch | event | New run (raw fill) | 5 | 5 |
| never (line 8) | event | Run / New run (clean fill) | 5 | 5 |
| humps (line 7) | event | Run / New run (0.65, 0.65) | 5 | 5 |
| onTime (line 10) | event | Test the sign | 5 | 5 |
| cleanStart, welcome (raw) | welcome | entering the bench | 1 | 1 |

- Stale lines: fast taps (0.2 s) through add Pair, add Drop, move, Model, Fill, Run, Reset, and Run, slider, Answer,
  Test, window slider, Raw: every queued line was dropped (hush, newer) when its moment passed; nothing played late.
  A line already playing finishes (the kit's rule).
- First tap: the stage gets the welcome in 124 ms; a pipeline tab gets only its own bench welcome; the Next page button
  gets only line 2; Read speaks the hint only; Sound says nothing; Tab gets the welcome. Read first, then Sound off and
  on brings the skipped welcome once; a page turn first, then Clean and back to Raw, brings it once.
- Read: stops a playing line and speaks the hint, with Sound off too; a mode change right after Read starts the new
  welcome in 141 ms.
- Order: spoken lines follow the actions in every run.
- Lines: `__tool.allLines()` and voice/lines.json hold the same 323 lines word for word (24 lines plus 299 onTime).
- Two lines do not match their moment: findings 2 and 3.

#### Art and words

- No `art:` tokens; art/prompts.json has no assets, no people. Everything drawn in code, as the spec says.
- No em dashes in src.html, notes.md, lines.json, data-desk.js or the family doc; "Curio Class" never shortened;
  classroom-safe language. Nothing is stored (no localStorage in the tool or engine); notes say nothing is saved or
  sent, so no on-screen privacy line is needed.

#### Findings

##### Should fix

1. **Raw log main chart below the fold at 680x425 and 800x500** (src.html:973-986, `layoutRaw`). In compact the stage
   is about 390 px wide, so the raw grid stacks and the scatter with r = -0.64 (the tool's hook) sits under the 15-row
   table; the bench scrolls 374 px at 680x425 and 365 px at 800x500. Clean and Model fit. Done when 8 fails for Raw.
   Seen in frames f8/r800.png and f7/raw-marked.png and the scroll measures. Better: in compact, put the scatter
   beside a narrower table (fewer columns padding, the 11.5 px table type) or give the table fewer rows per page.
   **general**. (Play may report the same.)
2. **"Try moving one" is spoken when nothing can move** (src.html:660, line `recipe`). The how-to is spoken on the
   first added step, when the recipe has one step and both its arrows are aria-disabled. STANDARDS: a how-to that
   assumes room to change must not play when the screen says otherwise. Seen in the rep-pair and rep-order logs
   (spoken at the first add). Better: queue it with `valid: () => state.steps.length > 1` (it then plays at the
   second step, still once), or say "Add another step, then try moving one." **general**.
3. **"Read the data notes" plays when the student did not turn a page** (src.html:573-575). `onPage` fires for every
   page change, including `rawPager.show()` from "N marked: see on Raw log", Next marked and `showFirstMark`. Seen:
   marks on row 201, tap the Model chip: line 2 spoken at 7.6 s while the hint says "The marked rows are the ones you
   picked..." (run markjump). It also uses up the once-only line, so a later real page turn is silent. Better: set
   `turned` and queue line 2 only from the Previous/Next buttons (a click flag), not from programmatic jumps.
   **general**.
4. **Engine table controls are not 44 px outside the 9-12 theme** (kit/data-desk.js:55, 58, 244, 300). Editable cells
   are 32 px tall, the remove × is 27x27, and an `addRow` button without a pager is 27 px tall and full width, because
   `.btn` is sized only in theme-912 and `input.dd-cell` has `min-height:32px`. The family doc says "Pager buttons and
   inputs are 44 px". The siblings that edit tables (data-table-builder grade 4, lunch-survey-cleanup 6-8) use the
   light theme. Seen in the harness (sizes printed: dd-cell 96x32, dd-remove 27x27, dd-add 1200x27). Better: size
   `.dd-cell`, `.dd-remove` and `.dd-add` in the engine's own style (44 px, add-row not stretched). **family:data-desk**.
5. **Grouped bar charts have no names for the groups** (kit/data-desk.js:633-667). `groupLabels` is ignored for bars,
   no legend is drawn, and the groups differ only by color and a 1 px stroke dash; the text alternative uses raw keys
   ("Asia: f 1, m 1"). The doc says `groupBy, groups, groupLabels, colorGroups` serve box and bar. region-compare and
   data-table-builder need grouped bars. Seen in the harness (chart text and every `<text>` in the svg). Better: a
   legend row (swatch with the series shape plus the label) and labels in the text alternative. **family:data-desk**.
6. **Years print with a thousands separator** (kit/data-desk.js:68-76, used by every axis and text alternative). A line
   chart over years shows ticks and text "2,000", "2,000.5" ("(2,000, 1)"). economy-dashboard plots decades of
   years. Seen in the harness line chart. Better: an axis `format` option (or `digits`/no grouping per column, e.g.
   `columns.year.type = 'year'`) documented in the family doc. **family:data-desk**.
7. **Box plot picking tells keyboard users the wrong keys** (kit/data-desk.js:725-726 vs 760). The pick layer's
   aria-label says "left and right arrows choose", but box plots step with Up and Down. Not used by this tool (its box
   plot has no `onPoint`), but box-plot-builder and data-desk-distributions will. Seen in the harness label. Better:
   name Up and Down for box plots. **family:data-desk**.

##### Polish

1. **The real-log result bar shows a blue sliver before any test** (src.html:117-119). The 0-width `<i>` keeps its 2 px
   border, so "not tested yet" sits over a bar that looks started. Seen in f1/t1366x768.png. Better: no border at
   width 0 (or hide the fill until a test). **general**.
2. **Night-code cells are marked by grey text only** (src.html:73, `td.ng`). The integer value is a second hint, but
   only for a reader who already knows the codes. Better: a small glyph or "(code)" after the value, as the marked rows
   have ▶. **general**.

##### Nit

1. src.html:631: `state.res.paired ? r.i : r.i` (both branches the same). **general**.
2. src.html:259-260: the Model legend swatches hard-code `#5aa9ff`, `#ffd166` and `#0e1520` instead of `var(--real)`,
   `var(--sim)` and `var(--chart-bg)`. **general**.
3. Engine and doc drift, small: the header comment lists a `legend` option (not implemented) and a 'category' column
   type; `--dd-bg` is set but never used; `domainFaint` and `--dd-bgline` are used but not in the doc; `ch.text()`
   leaves out `title` although the doc says title starts the text alternative (only the aria-label has it); box text
   alternative says "1 values". **family:data-desk**.

Frames and logs: scratchpad lens-sim-craft/f1 (all sizes), f3 and f4 (voice logs), f5 (keyboard), f6 (workflow,
calm), f7 and f8 (bench frames), f9 (engine harness).

<!-- end part -->

<!-- part: refine/play.md -->

### Play lens: simulation-studio (round 1)

Cold play, 2026-10-28. Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py simulation-studio` (149 KB). Driven with
`scripts/drive.py` (held clicks, 0.12 s), port 9750, own profile; `--host 9751` for 375 wide (host.html deleted after).
No console errors or exceptions in any shot (the only log line was the host page's own favicon 404).

Played as (1) a grade 10 statistics student alone at home, at a real pace through Raw log, Clean, Model, Answer,
including the wrong cleaning order, Flag or Drop without Pair, removing every step, and a student who skips straight to
Model and to Answer; and (2) a teacher projecting it at 1366x768 and 1920x1080.

Counts: blockers 1, should fix 4, polish 4, nits 4.

#### Blocker

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

#### Should fix

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

#### Polish

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

#### Nits

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

#### What worked (no action)

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

<!-- end part -->

<!-- part: refine/teaching.md -->

### simulation-studio: Teaching lens (round 1, 2026-10-28)

Read cold: REFINE.md (Teaching lens), STANDARDS.md, BASELINE.md, spec.md, handoff.md, notes.md, tool.draft.json, src.html.
Bundled with `CURIO_DRAFT=1 python scripts/bundle_tool.py simulation-studio` (149 KB) and driven with `scripts/drive.py`
(own profile, port 9741; frames raw, pair, dropfirst, pairdrop-model, model, answer, answer-unrun, v-pages, v-recipe,
v-model-answer, clean-1366, model-680, answer-1366, pairdrop-model-1366; 0 console errors). Every number below was
recomputed in Python from a fresh download of the Rdatasets CSV (299 rows), with the tool's mulberry32, Box-Muller,
JS rounding, clamp and 5 minute bins ported exactly.

Counts: blockers 1, should fix 6, polish 3, nits 2.

#### Blocker

**B1. The pairs table and the model fill join eruptions that were not next to each other whenever Drop is in the
recipe, including the right order.** general
- Where: src.html:426-430 (`pairsOf(state.res.rows)`), used by the pairs table (804-812), "Fill from my clean log"
  (766-768), the result line choice (786-787) and the pair-row marks (742).
- What: `pairsOf` pairs consecutive rows of the cleaned log. After Drop, consecutive rows are not consecutive
  eruptions. With Pair, then Drop (the order the tool approves: hint "Your log is clean. Tap Model to build a geyser
  from it.") the Real column reads Short then short 3, Short then long 78, Long then short 79, Long then long 60. The
  real geyser has none: on the true timeline the counts are 0, 104, 105, 89. The 3 fake pairs are file rows 51 and 53,
  200 and 202, 268 and 270, each two short eruptions joined across a dropped night-coded long one (rows 52, 201, 269,
  coded 4.0). "Fill" then sets 0.96 and 0.43 instead of 1.00 and 0.46; seed 1 gives Match 88 percent and simulated
  Short then short 3, so the student sees 3 beside 3, is told "The humps match. Now check the pairs table", and the
  key result ("never follows a short one with a short one") can no longer be reached. The same 3 appear with Drop
  first.
- Why it blocks: this is the exact pairing error the tool teaches (the "26 pairs now join eruptions that were not next
  to each other" warning), made silently by the tool itself on the order it calls clean, and it reverses the Model
  bench's main finding.
- How seen: drive.py `__tool.readout()` after addStep pair, drop (realPairs {SS:3, SL:78, LS:79, LL:60}; model
  {pS:0.96, pL:0.43}; Match 0.880; simPairs SS 3), frame pairdrop-model-1366.png; Python on the CSV.
- Fix direction: count a pair only when the two rows are neighbors in the file (`rows[k+1].i === rows[k].i + 1`), or
  always count pairs on the full timeline and say so under the table.

#### Should fix

**S1. Drop's cost is never shown or named.** general
- Where: Clean bench readout (src.html:711-718) and hint `cleanDone`; notes.md.
- What: Pair then Flag and Pair then Drop give the same scatter (r = 0.90 on 221, line 34.88 + 10.63 x duration) and
  the same "Your log is clean." Drop silently removes 78 eruptions (26 percent of the log, all at night): the class
  counts fall from 104 and 194 to 82 and 139 (means 55.3 and 81.8, spreads 6.7 and 6.7) and the geyser is then fitted
  on daytime eruptions only. "Cleaning choices and their effect" is the core of the DC codes, and here the choice
  has no visible effect except the B1 bug.
- How seen: drive readout pairThenDrop; Python.
- Better: a readout line when Drop is in the recipe ("78 eruptions dropped, 26 percent of the log, all at night"), and
  a notes line on why Flag fits this log (only the coded durations are untrustworthy; the waits and the timeline are
  real, so keep the rows).

**S2. The recipe code is not real code.** general
- Where: src.html:304-306 and 362-364 (Clean step buttons and recipe lines); spec Clean.
- What: written like pandas, but three of the four parts fail in pandas: `log.duration in [2, 3, 4]` raises ValueError
  (the truth value of a Series is ambiguous), `log.drop(mask)` drops by index labels, not by a mask, and
  `log.night = ...` sets an attribute, not a column (pandas warns and makes no column). Only `.shift(-1)` is right.
  9-12 tools should work like the real thing; a student who types these into Python gets errors.
- Better: real pandas, about the same length on screen: `log["wait_after"] = log["waiting"].shift(-1)`,
  `log["night"] = log["duration"].isin([2, 3, 4])`, `log = log[~log["duration"].isin([2, 3, 4])]`; or label the
  lines as pseudocode.

**S3. The simulated summer reads as a second test of the sign, but it is built from the same 1985 numbers.** general
- Where: Answer bench, second result bar (src.html:878-880); notes.md "Talk about it".
- What: the summer geyser's waits are normal with spreads 6.3 and 6.8, so its on-time rate is what those spreads imply
  (about 87 to 89 percent within 10 minutes for this mix of short and long eruptions), not evidence that the sign works
  on the real geyser. Over seeds 1 to 200 it runs 86.6 to 90.7 percent (seed 1: 1,616 of 1,830, 88.3 percent). Nothing
  on screen or in the notes says what the simulation cannot show, and the Talk question "What does a simulation let you
  test that the 15 days of real data cannot?" invites the overclaim. 3B-DA-07 (evaluate what models and simulations
  can test) is the code this should teach. Also, 269 of 298 is in sample: the sign is filled from the same eruptions
  it is tested on.
- How seen: Python (normal-theory estimate and 200 seeds); frame answer-1366.png.
- Better: one small line under the summer bar ("Built from the same 1985 numbers: it shows how the on-time rate
  wobbles from summer to summer, not whether the geyser still acts this way"), and a notes answer: a simulation shows
  the spread of outcomes (New run) and lets you try rules you never saw; it cannot show anything the model leaves out
  (the drift since 1985 that the park's 68 and 94 show, earthquakes, the night codes). An honest out-of-sample check
  for the notes: fill from the first 150 eruptions (means 56 and 81) and test on the other 148: 131 of 148, 89
  percent; the reverse (55 and 82) gets 136 of 150, 91 percent. So the 90 percent holds up.

**S4. The raw r = -0.64 is a real pattern, not a mistake, and nothing says so.** general
- Where: welcome line ("Something in it is backwards"), Raw readout (src.html:579, "wait = 99.31 - 7.80 x duration"),
  notes.md step 1 ("who is wrong, the rangers or the log?").
- What: the same-row scatter is the wait before an eruption against that eruption's length. It is negative for a true
  reason: a short eruption is always followed by a long one (Short then short = 0, the Model bench's finding), so a
  short wait comes before a long eruption. The error is reading "the wait before" as "the wait after", not the
  correlation. As written, a student can leave thinking a negative r meant bad data. The readout also calls the
  column "wait" when it is the file's "waiting" (the wait before).
- Better: the Raw readout says "waiting" (or "wait before"); a notes paragraph: both correlations are real and answer
  different questions (what comes before an eruption, what comes after); the pairing decides which question you
  asked. "Talk about it" already has "The file was not wrong; the column's meaning was"; this completes it.

**S5. The public sources for the park's numbers are wrong.** general
- Where: tool.draft.json `sources`.
- What: it lists https://www.nps.gov/yell/planyourvisit/predict-old-faithful.htm, which returns 404 (curl,
  2026-10-28). The on-screen claims come from two other pages, both checked and both missing from tool.draft.json:
  the YELL 003 worksheet PDF (https://www.nps.gov/common/uploads/teachers/lessonplans/YELL_003-PredictOldFaithful.pdf:
  "< 3 minutes, 68 minutes; > 3 minutes, 94 minutes", confirmed) and the virtual visitor center exhibit
  https://home.nps.gov/features/yell/ofvec/exhibits/eruption/prediction/predict7.htm ("about 90 percent" of
  predictions within plus or minus 10 minutes, confirmed; predict8.htm confirms only one eruption ahead can be
  predicted).
- Better: replace the dead link with those two URLs.

**S6. One crosswalked code is only lightly taught: 3A-DA-11, create interactive data visualizations.** general
- Where: the module codes (HS-DAT-DC-21, DC-23, DI-25, DI-26; crosswalk 3A-DA-11, 3A-DA-12, 3B-DA-05, 3B-DA-07).
- What: modeling (3A-DA-12), finding patterns (3B-DA-05) and judging a model (3B-DA-07, once S3 is done) are taught by
  what the student does. Creating a visualization is not: every chart is fixed; the student never picks what is
  plotted, how it is binned or which chart answers the question. Bin taps and marks are reading, not making. Which
  2026 id carries 3A-DA-11 could not be confirmed here (data/standards has ids only; the CSTA page renders by script),
  so check that before acting.
- Better (only if it teaches well, BASELINE rule 2): a real choice with a consequence, such as the bin width on the
  Model histogram (Match changes with it, which itself teaches that a fit measure depends on choices), or the x and y
  columns on Clean. Otherwise move that code to a tool where building the chart is the job.

#### Polish

**P1. Match has no yardstick.** general. A perfect model cannot reach 100 percent with 299 eruptions: two runs of the
clean-fill geyser against each other (seeds s and s + 1000, 200 pairs) overlap 86 to 94 percent (median 90); the real
log's first half against its second half overlaps 88 percent. So 89 percent is as good as a run can show, and students
chasing 100 would be chasing noise. Say this in the notes and in a short line by Match ("A perfect geyser scores about
86 to 94 percent: New run shows the wobble").

**P2. "spread" is never named.** general. For 9-12, name it once as the standard deviation (class table header
"spread (SD)" or the notes). The fill uses the sample SD (6.31, 6.80), which matches.

**P3. The night-code rule is an assumption.** general. Flag and Drop treat every duration of exactly 2:00, 3:00 or 4:00
as a code. Measured neighbors appear once or twice each (2:01 twice, 2:02, 4:01 and 4:02 once), so one or two of the
78 may be real daytime measurements. One notes line ("a cleaning rule is a guess that can catch good rows too") turns
this into the lesson the DC codes ask for.

#### Nits

**N1.** The comparison line (src.html:881) says "The park's worksheet today"; the worksheet PDF is dated 2018-08-16
(its metadata). "The park's 2018 worksheet" is exact.

**N2.** Spec Sources call the exhibit the "Old Faithful Visitor Education Center exhibit"; the page is the "Old
Faithful Virtual Visitor Center". Spec wording only.

#### Checked and right

- Data: the 299 waiting and duration values in src.html equal the Rdatasets CSV exactly. Night codes 78 (2.0 x 23,
  3.0 x 2, 4.0 x 53). The data notes match the MASS documentation (nocturnal codes 2, 3, 4 for short, medium, long;
  waiting described as the time to the next eruption in the original files, corrected in MASS 7.3-30; 1 to 15 August
  1985).
- Clean: raw r -0.6446, line 99.31 - 7.80 x duration, 299 rows (the tool shows -0.64, correct rounding; the spec's
  -0.65 is already in handoff). Pair r 0.8885, 34.95 + 10.78 x duration, 298. Pair then Flag r 0.8980,
  34.88 + 10.63 x duration, 221. Drop then Pair r 0.8164 on 220, 26 wrong pairs. Class means after Pair 55.6 (SD 6.3,
  n 104) and 81.2 (6.8, 194); raw 83.2 (6.6, 105) and 66.4 (13.2, 194). Waits 43 to 108, mean 72.3, SD 13.9; the
  histogram from 40 matches the spec.
- Model (seeds 1 to 200, 5th to 95th percentile): start 0.60 to 0.69, seed 1 0.656, SS 59 to 89; clean fill 0.85 to
  0.93, seed 1 0.8903 with pairs 0, 100, 100, 98, SS always 0; 0.65 and 0.65 0.85 to 0.93, seed 1 0.9017 with SS 37,
  SS 25 to 46; raw fill 0.78 to 0.86, seed 1 0.840. Fill gives 1.00 and 0.46.
- Answer: 56 and 81 gives 163, 269, 294 at windows 5, 10, 15; 72 always gives 60, 136, 205; 83 and 66 gives 49 at 10.
  Summer seed 1: 1,616 of 1,830 (88 percent), 91.7 days. The park's 68 and 94 on the 1985 log get 106 of 298, which
  supports "the 1985 sign would not work now".
- Every number in notes.md matches (including "87 to 91 percent over other seeds": seeds 1 to 200 round to 87 to 91).
- Nothing gives an answer away: there is no predict, quiz or hidden-information mode.
- Language is plain and right for 9-12. No sensitive topics in these standards (rule 8). Nothing cultural, Native or
  hard-history: no sensitivity referral.

#### Done when

| # | Result |
|---|---|
| 1 | Pass: 299 rows, 20 pages, r = -0.64 (the spec's -0.65 is the rounding note already in handoff) |
| 2 | Pass: r 0.89, means 55.6 and 81.2; with Flag r 0.90 on 221 |
| 3 | Pass: Drop before Pair shows the 26-pair warning and r 0.82; moved after, r 0.90 (but see B1: the pairs table is wrong in both orders) |
| 4 | Pass: seed 1 clean fill Match 89 percent, pairs 0, 100, 100, 98; 0.65 and 0.65 Match 90 percent, SS 37 |
| 5 | Pass: 269, 136, 49 |
| 6 | Pass: 88 percent (seed 1); seeds 1 to 50 run 86.8 to 90.5, already in handoff |
| 7 | Pass: held clicks; 5 page turns speak `notes` once; the recipe line is spoken once, then silent; `modelHow` and `answerHow` once; `onTime` on 5 of 5 tests |
| 8 | Pass: pipeline, main chart and Run button visible at 1366x768 and 680x425 (frames model-680, pairdrop-model-1366); real is outline plus circle, simulated is fill plus triangle |

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### simulation-studio: build handoff (2026-10-28)

#### What was built

- `tools/simulation-studio/src.html`: one studio, four benches joined as a pipeline tablist (Raw log, Clean, Model,
  Answer), each with its own stage and panel, built once and toggled (never rebuilt on a switch). Status lines on each
  node ("299 rows, 4 marked", "2 steps, check order", "Match 89%", "90% on time"); the arrows pulse downstream when
  something upstream changes. Real-pixel stage on a ResizeObserver, wide, compact and stack layouts as collision-lab,
  plus a second layout pass that takes any spill off the charts.
- Data: MASS `geyser` (299 rows) embedded in the file, durations as in the CSV. Credit comment with every source and
  the date pulled.
- `kit/data-desk.js` (new, version 1.0): the family engine, see below.
- `docs/families/data-desk.md`: rewritten as the engine reference; every documented function exists and was run.
  Family table now 11 tools (lunch-survey-cleanup, catalog-column-rules added) with a data set column; the Old
  Faithful claim recorded.
- `tool.draft.json`, `notes.md`, `art/prompts.json` (no assets: all drawn in code), `voice/lines.json` (bank
  gravel-ranger, voice Algenib, 323 lines, equal to `allLines()`), `preview.svg` (the Model bench after a clean fill).
- Bundled with `CURIO_DRAFT=1 python scripts/bundle_tool.py simulation-studio` (149 KB). No recordings yet:
  `scripts/voice.py simulation-studio` is the next step.

#### Checked (drive.py, port 9690, own profile; 375 through --host 9691)

- Every number against Python: raw r −0.6446 and 99.31 − 7.80x; Pair r 0.8885, class means 55.6 / 81.2; Pair then
  Flag r 0.8980 on 221; Drop then Pair r 0.8164 on 220 with 26 wrong pairs; seed 1 clean fill Match 0.8903, pairs 0,
  100, 100, 98; both chances 0.65 Match 0.902 with SS 37; start model 0.656; signs 269 / 136 / 49; summer 1,616 of
  1,830 (88.3 percent), 91.7 days. Engine fits checked against numpy (linear, quadratic, exponential r2 and params).
- Done-when 1 to 8 pass, with one note on item 1 (below).
- Voice: lines 2, 3, 6 and 9 spoken once in a run of five actions at 2 s held taps; line 10 after every test; tab
  switches hush and speak the bench's welcome; stale lines dropped by `valid`; Read speaks the hint. The tool owns
  the hint (`hint: false`); it changes at once on every switch and change, and its min-height is the tallest variant
  for that bench, so it neither clips nor jumps.
- Focus: nothing focused on load; recipe buttons rebuilt with focus put back on the same step's same button (after a
  remove: the next step's remove, else the Add button); aria-disabled, never disabled; Alt+Up/Down moves a step;
  the chart pick layer is now kept across redraws, so a tap on a bin keeps focus there.
- 44 px targets, no hint clipping and no horizontal scroll at 680x425, 800x500, 1000x625, 1280x720, 1366x768,
  1920x1080, 760x900 and 375x812.

#### Engine API (kit/data-desk.js, full reference in docs/families/data-desk.md)

- `DataTable(rows, {columns})`: `rows`, `columns`, `on`, `emit`, `batch`, `add`, `set`, `remove`, `replace`, `values`,
  `column`, `stats`, `count`, `crosstab`, `label`, `where`, `renderTable(el, {page, columns, index, caption,
  editable, removable, addRow, rowClass, onRow, cellClass})` returning `{el, table, update, go, show, page, pages,
  onPage, destroy}`.
- `Chart(svg, t, opts)`: dot, bar, histogram, box, scatter, line; overlay series (`overlay`, `share`, `tops`,
  `faded`), `marks`, `bands`, `point()` per-point shape, ring, faint; returns `update`, `resize`, `highlight`,
  `onPoint`, `pick`, `fit` (returns `{kind, f, params, r2, r, residuals, n, eq}`), `curve`, `drag`, `text`.
- `DataDesk`: `fmt`, `nice`, `stats`, `linreg`, `fit`, `shape`, `SHAPES`, `DASH`, `mk`, `version`.
- Two engine changes made during the build, both in the doc: a chart given an `<svg>` sizes it (width, height,
  viewBox); the pick layer is kept across redraws (never rebuilt under the pointer or focus).
- No existing kit file was changed. No other tool loads data-desk yet.

#### Known gaps and notes for Refine

- Done-when 1 says r = −0.65; the data gives −0.6446, so the tool shows −0.64 (correct rounding). Spec wording to fix.
- Spec says the summer lands "between 87 and 90 percent"; over seeds 1 to 50 it runs 86.8 to 90.5 (seed 1: 88.3).
- At 680x425 and 800x500 the benches scroll inside the stage (pipeline, main chart and main button stay visible, as
  Done-when 8 asks; the class table, pairs table and strip sit below).
- In the stack layout (375 wide) the panel, with the hint, sits below the stage, as in collision-lab.
- The welcome line (line 1) is replaced when the first tap is a page turn on Raw log (that tap queues line 2); it
  does play when the first tap is anything else.
- The pairs-table and histogram marks pick file rows; with Flag on, night rows are still marked (they are in the log).
- catalog-column-rules' spec asks for `t.validate(dictionary)` in the engine; not built here.

#### For Cory

1. Source: the data-desk rule asks for public data such as government statistics. This is a published research
   data set (Azzalini and Bowman 1990, measured at Yellowstone, distributed in R's MASS). Its real flaws (night
   codes, the corrected column meaning) are the lesson. Acceptable?
2. Size: 299 rows, over the family's "under about 200 rows on screen". The table pages 15 at a time (rule now reads
   "or paged"). Keep, or trim to the first 10 days (about 200 eruptions; every number would be recomputed)?
3. Claim: Old Faithful is also a classic for data-desk-distributions (grade 12). This build claims it for
   simulation-studio in the family doc. Say if you would rather keep it for distributions.
4. data-detective's concept mentions "geyser wait vs eruption" as a scatter example. With the one-dataset-per-tool
   rule it would need a different data set; flag for its spec.
5. KIT.md does not list kit/data-desk.js yet (outside this build's write scope); one line there would help siblings.

#### Refine round 1 (2026-10-28)

All 23 items in refine.md, plus the cheap nits. Engine is now version 1.1.

- Blocker fixed: `pairsOf` pairs by original row order (both eruptions next to each other in the file and both
  kept). Every recipe order matches Python (scratch py/refine.py): pairs 0/104/105/89 without Drop, 0/75/71/48
  with Drop; seed 1 Match .8903 (Pair, Flag), .8841 (Pair, Drop), .8344, .8401, .8395 for the wrong orders and the
  raw fill; sign 269, 267, 41, 49 of 298.
- Teaching changes (recorded in spec.md under "Refine changes"): the recipe is real pandas (`shift(-1)`, `isin`,
  a boolean mask); an out-of-sample check on the Answer bench (fill from rows 1-150, test on the other 148: 131 of
  148, raw fill 25); a 2/5/10 minute bin chooser with a yardstick line, which keeps 3A-DA-11 on the module (seed 1:
  .857, .890, .948); Drop states its cost (78 eruptions, classes 82 and 139).
- Checked again: every STANDARDS size and 375 through --host (no targets under 44 px, no horizontal scroll, no
  clipped hints, the main chart and main button on the first screen; last Model slider 690-734 at 1366x768). The
  compact sizes still scroll inside the bench, as in the build. Voice at a 2 s tap pace: the notes line plays only on
  a student page turn, the recipe line waits for a second step, no praise for a raw or wrong-order fill. At that pace
  an event line can be dropped when the bench changes (queue behavior).
- Engine (kit/data-desk.js 1.1, doc updated): 44 px table controls in every theme; a `'year'` column type and
  `fmt(n, d, {group: false})`; `xFormat`/`yFormat`; a grouped-bar legend with shapes and label names; the box pick
  label says up and down; `onPage` gets `{user}`; measured top and right margins; `ch.text()` starts with the title.
- Settled calls applied: the source and the 299 rows stay (exception noted in the family doc); Old Faithful stays
  here, and data-detective and data-desk-distributions pick other data (doc note); `t.validate` waits for
  catalog-column-rules. The "For Cory" questions above are answered by these calls.
- Voice: voice/lines.json regenerated (326 lines, 6 new or changed); new recordings are needed.
- Still open: KIT.md does not list kit/data-desk.js (outside this scope).

<!-- end part -->

## Log

- 2026-11-25: refine.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/craft.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/play.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-10-28)
- 2026-11-25: handoff.md folded in (last changed 2026-10-28)

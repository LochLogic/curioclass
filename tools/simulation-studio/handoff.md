# simulation-studio: build handoff (2026-10-28)

## What was built

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

## Checked (drive.py, port 9690, own profile; 375 through --host 9691)

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

## Engine API (kit/data-desk.js, full reference in docs/families/data-desk.md)

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

## Known gaps and notes for Refine

- Done-when 1 says r = −0.65; the data gives −0.6446, so the tool shows −0.64 (correct rounding). Spec wording to fix.
- Spec says the summer lands "between 87 and 90 percent"; over seeds 1 to 50 it runs 86.8 to 90.5 (seed 1: 88.3).
- At 680x425 and 800x500 the benches scroll inside the stage (pipeline, main chart and main button stay visible, as
  Done-when 8 asks; the class table, pairs table and strip sit below).
- In the stack layout (375 wide) the panel, with the hint, sits below the stage, as in collision-lab.
- The welcome line (line 1) is replaced when the first tap is a page turn on Raw log (that tap queues line 2); it
  does play when the first tap is anything else.
- The pairs-table and histogram marks pick file rows; with Flag on, night rows are still marked (they are in the log).
- catalog-column-rules' spec asks for `t.validate(dictionary)` in the engine; not built here.

## For Cory

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

## Refine round 1 (2026-10-28)

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

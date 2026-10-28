# Craft lens: simulation-studio (round 1)

Cold read of spec.md, src.html, notes.md, art/prompts.json, voice/lines.json, kit/data-desk.js and
docs/families/data-desk.md. Bundled with `CURIO_DRAFT=1 python scripts/bundle_tool.py simulation-studio` (149 KB).
Driven with `scripts/drive.py` (muted headless Chrome, own profile, ports 9760-9769, held clicks 0.12 s), plus a
light-theme harness page that loads only kit/curio.css, kit/curio.js and kit/data-desk.js to exercise the engine API the
siblings will use. The pairsOf blocker (src.html:426, pairs across dropped rows) is already reported by Teaching and
Play and is not repeated here. Placeholder art and the browser voice are expected and not reported.

Counts: blockers 0, should fix 7 (general 3, family 4), polish 2, nit 3.

## Contract

- One file, 149 KB, no external src/href (only `kit:` names inside comments), no fetch/XHR/WebSocket. The three inline
  scripts pass `node --check`.
- Kit used, not re-implemented: tables and charts are `DataTable`/`Chart`, fits are `chart.fit('linear')`, class stats
  are `DataDesk.stats`, narration is `Curio.voice`.
- No console errors or exceptions in 30+ driven tabs: every bench at 1366x768, 1280x720, 1920x1080, 1000x625,
  800x500, 680x425, 760x900 and 520x800, a full workflow (wrong order, fix, flag, show night, marks, fill, runs with
  extreme rules, sign fill and tests, mark stepping, remove every step) with Motion on and off.
- Every change recomputes well under the spec's 150 ms (add step 49 ms, move 33, run 8, test 1).

## Engine against the family doc (kit/data-desk.js vs docs/families/data-desk.md)

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

## Access

- Keyboard: Tab reaches every control on every bench in a sensible order (header, the selected pipeline tab, bench,
  panel); pipeline tabs move with arrow keys and wrap; Alt plus Up moved Flag above Pair and kept focus on its button;
  the histogram pick layers take arrows, Enter and Escape. Every stop showed the kit's 4 px focus outline.
- Targets: every button and input measured 44 px or more at all sizes (the Show night codes checkbox is 20 px, but its
  label row is 44 px and clickable).
- Color is not the only signal: real vs simulated is outline plus circle vs fill plus triangle; wrong pairs carry a
  ring plus the warning line; marked rows carry a background plus a ▶ glyph. One weak spot is in polish 2.
- Motion off: no histogram tween (bar heights identical across frames), no arrow pulse, no recipe flash. Sound and
  Read: see the voice check.

## Standard voice check

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

## Art and words

- No `art:` tokens; art/prompts.json has no assets, no people. Everything drawn in code, as the spec says.
- No em dashes in src.html, notes.md, lines.json, data-desk.js or the family doc; "Curio Class" never shortened;
  classroom-safe language. Nothing is stored (no localStorage in the tool or engine); notes say nothing is saved or
  sent, so no on-screen privacy line is needed.

## Findings

### Should fix

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

### Polish

1. **The real-log result bar shows a blue sliver before any test** (src.html:117-119). The 0-width `<i>` keeps its 2 px
   border, so "not tested yet" sits over a bar that looks started. Seen in f1/t1366x768.png. Better: no border at
   width 0 (or hide the fill until a test). **general**.
2. **Night-code cells are marked by grey text only** (src.html:73, `td.ng`). The integer value is a second hint, but
   only for a reader who already knows the codes. Better: a small glyph or "(code)" after the value, as the marked rows
   have ▶. **general**.

### Nit

1. src.html:631: `state.res.paired ? r.i : r.i` (both branches the same). **general**.
2. src.html:259-260: the Model legend swatches hard-code `#5aa9ff`, `#ffd166` and `#0e1520` instead of `var(--real)`,
   `var(--sim)` and `var(--chart-bg)`. **general**.
3. Engine and doc drift, small: the header comment lists a `legend` option (not implemented) and a 'category' column
   type; `--dd-bg` is set but never used; `domainFaint` and `--dd-bgline` are used but not in the doc; `ch.text()`
   leaves out `title` although the doc says title starts the text alternative (only the aria-label has it); box text
   alternative says "1 values". **family:data-desk**.

Frames and logs: scratchpad lens-sim-craft/f1 (all sizes), f3 and f4 (voice logs), f5 (keyboard), f6 (workflow,
calm), f7 and f8 (bench frames), f9 (engine harness).

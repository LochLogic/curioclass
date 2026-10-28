# Family: data desk

Eleven tools, grade 4 to 12 (math, computer science, social studies), share one data engine: `kit/data-desk.js`,
inlined with `<script src="kit:data-desk"></script>` after `kit:curio`. The engine was first written by
simulation-studio (2026-10-28, version 1.0; 1.1 after its Refine round 1); this file is its reference. Every function below exists in the engine
and works as written.

## What the engine does (shared)

A small table and the charts that read from it, all drawn in SVG, all updating live when data changes. Globals:
`DataTable`, `Chart` and `DataDesk` (helpers). No network requests, no dependencies.

### DataTable

```js
const t = DataTable([{name: 'Ava', shoe: 7, height: 152}, ...], {
  columns: {shoe: {label: 'Shoe size'}, height: {label: 'Height', unit: 'cm', digits: 0},
            grade: {label: 'Grade', type: 'text', values: ['K', '1', '2']}},   // values: the column's own order
});
t.rows                                   // plain objects; given column keys first, then any other key seen
t.columns[key]                           // {label, unit, digits, type: 'number' | 'year' | 'text' | 'bool', values}; type inferred when not given
t.on('change', fn) -> off()              // fn(info, t); info.type: add | set | remove | replace | batch
t.batch(fn)                              // run fn with change events held, then send one
t.add(row) -> i;  t.set(i, key, v);  t.remove(i);  t.replace(rows)
                                         // set() turns text into a number on number and year columns; '' becomes null
                                         // 'year' is numeric but prints without a separator (2000), in tables,
                                         // axes (whole-number ticks) and text alternatives
t.values(key, keep?)                     // raw values (keep(row, i) filters)
t.column(key, keep?)                     // numbers only
t.stats(key, keep?)                      // see Stats below
t.count(key, keep?) -> [{value, n}]      // in the column's values order, else first appearance
t.crosstab(a, b, keep?) -> {rows, cols, n(ra, cb), total}
t.label(key, unit = true)                // "Height (cm)"
t.where(keep) -> a new DataTable         // a filtered copy with the same columns
t.renderTable(el, opts) -> controller
```

`renderTable` draws a real `<table>` (caption, `th scope`) into `el`. Options: `page` (rows per page; adds a pager),
`columns` (keys to show), `index` ('#' by default, a row-number column, or false), `caption`, `editable` (number
and text inputs; Enter moves down), `removable`, `addRow` (a button label), `rowClass(row, i)`, `onRow(i, row,
event)`, `cellClass(row, i, key)`. The controller: `{el, table, update(), go(page), show(rowIndex), page, pages,
onPage(fn), destroy()}`. The pager is Previous, "Page x of y" (aria-live) and Next; the buttons stay put and use
`aria-disabled` at the ends, so keyboard focus is never lost. Pager buttons, editable cells, the remove x and the add-row button are at least 44 px in every
theme (the engine's own style). `onPage(fn)` calls `fn(page, {user})`: `user` is true for a Previous or Next press and
false for `go()` or `show()` from code, so a tool can tell a student's page turn from its own jump.

### Chart

```js
const ch = Chart(svgOrGroup, t, {type: 'dot' | 'bar' | 'histogram' | 'box' | 'scatter' | 'line', x: 'shoe', y: 'height'});
```

Given an `<svg>`, the chart owns it and sets its `width`, `height` and `viewBox` to the chart size in real pixels.
Given a `<g>`, it draws inside it and the tool sizes the svg.

Options (all optional except `type` and `x`):

| Option | Meaning |
|---|---|
| `y` | a key, or a list of keys (several series on one scatter or line) |
| bar charts | with `y`: one bar per row (x names it, y is its height); without `y`: a count per value of x, side by side per `groupBy` value |
| `width`, `height` | in px (default 400 by 260); change with `resize(w, h)` |
| `font` | axis text size in px (default 12); `margin` `{l, r, t, b}` overrides the measured margins |
| `xDomain`, `yDomain` | fixed `[lo, hi]`; needed for dragging and whenever charts must line up or stay still |
| `xFormat`, `yFormat` | `v -> text` for tick labels and the text alternative (default `fmt`; year columns print plain) |
| `domainFaint` | scatter and line: false keeps faint points from stretching the axes (default true) |
| `xLabel`, `yLabel`, `title` | axis titles (default: the column label and unit); `''` hides one. `title` starts the text alternative |
| `filter(row, i)` | rows to draw |
| `series` | series number 1 to 6 (color `--dd-n` and shape) for the main data |
| `point(row, i)` | per point: `{shape, series, ring (a color), faint, hidden}`. Faint points are drawn pale and left out of fits |
| `pointSize` | point radius (default 3.5, 5 on touch) |
| `bins` | histogram: a bin width, or `{width, start}` |
| `share` | histogram: bars show the share of each series instead of counts (so different sizes compare) |
| `style` | histogram: 'fill' or 'outline' for the main series |
| `label` | the main series' name in the text alternative |
| `overlay` | histogram: a second series on the same bins, `{table, x, filter, style, series, label, faded}`; `faded` dims it (for example after the inputs changed) |
| `tops` | histogram: the series shape on top of each bar, so outline and fill also differ by shape |
| `marks` | `['mean', 'median']` lines on dot plots and histograms; a diamond for the mean on box plots |
| `bands` | scatter and line: `[{from, to, label, color}]` shaded x ranges |
| `groupBy`, `groups`, `groupLabels`, `colorGroups` | box and bar: one box or bar per group value, in `groups` order, named by `groupLabels`; `colorGroups` gives each box its own series. Grouped bars always get a series each, a legend row above the plot (swatch, shape, label) and the series shape on each bar top, so groups differ by more than color; the text alternative uses the labels |
| `dragStep` | `{x, y}` snap steps while dragging |
| `animate` | ms for histogram bar changes (300; 0 when Curio Class Motion is off) |
| `live` | redraw on every table change (default true); false when the tool redraws itself |

Methods (all return the chart unless noted):

```js
ch.update(opts)            // merge options and redraw
ch.resize(w, h)
ch.highlight(rows)         // a row index or a set of them: ringed in --dd-ring; null clears
ch.onPoint(fn)             // picking on; fn(info) or fn(null) when cleared (see Picking)
ch.pick(k)                 // choose a bin, box or bar by index from code; null clears
ch.fit(kind, style?)       // 'linear' | 'quadratic' | 'exponential' through the drawn, non-faint points; returns the fit (below); null removes it
ch.curve(f, style?)        // draw y = f(x), for example a student's own guess; null clears every curve
ch.drag(on = true)         // drag points (pointer or arrow keys); the table changes and every live chart follows
ch.text()                  // the text alternative, starting with the title (also in the chart's <desc> and aria-label)
ch.options, ch.lastFit, ch.bins, ch.boxes, ch.barRects, ch.dots, ch.scales, ch.el, ch.destroy()
```

**Picking.** With `onPoint` or `drag` on, one focusable layer covers the plot, so even a 6 px bin is a 44 px target
and the layer is kept across redraws (a tap or key never rebuilds the control under it). Pointer: tap a bin, box, bar
or the nearest point. Keys: left and right (up and down for box plots, as the layer's label says) choose, Enter or Space picks, Escape clears;
on scatter and line plots Page Up and Page Down choose a point and the arrows move it when dragging. `info` is
`{type: 'bin', bin, lo, hi, n, rows, series: [{n, share}]}`, `{type: 'box', group, stats, rows}`,
`{type: 'bar', cat, group, value, rows}` or `{type: 'point', i, row}`; `rows` are row indexes of the main table.

### Helpers (DataDesk)

```js
DataDesk.fmt(n, digits?, {group}) // true minus sign, thousands separators (group: false drops them); without digits, up to 2 decimals, zeros trimmed
DataDesk.nice(lo, hi, count)    // {lo, hi, step, ticks}: "nice" 1, 2, 5 steps
DataDesk.stats(values)
DataDesk.linreg(xs, ys)         // {a, b, r, r2, n}: y = a + b x
DataDesk.fit(kind, xs, ys)      // {kind, f, params, r2, r, residuals, n, eq}
DataDesk.shape(g, kind, x, y, r, attrs), DataDesk.SHAPES, DataDesk.DASH, DataDesk.mk(tag, attrs, parent), DataDesk.version
```

**Stats:** `{n, min, max, mean, median, q1, q3, iqr, mad, sd, sdp, sum, lo, hi, whiskerLo, whiskerHi, outliers}`.
Quartiles are medians of the lower and upper halves, leaving out the median when n is odd (the school rule).
`mad` is the mean absolute deviation (grade 6). `sd` is the sample standard deviation (n - 1), `sdp` the population
one. `lo` and `hi` are the 1.5 IQR fences; whiskers reach the furthest values inside them; `outliers` lie outside.

**Fits:** least squares. `params` are `{a, b}` for linear (y = a + b x), `{a, b, c}` for quadratic
(y = a + b x + c x squared) and `{a, b}` for exponential (y = a e^(b x), fitted on ln y, so y must be positive). `r2`
is on the original scale for all three, `r` is the signed Pearson r for linear and the square root of `r2` for the
others, `residuals` are y minus f(x) in point order, and `eq` is a readable equation string.

### Look

Fixed by the engine: axis style, nice ticks, point size (larger on touch), number formatting, the 1.5 IQR outlier
rule, series shapes (circle, triangle, square, diamond, cross, star) and dashes, so color is never the only signal.
Colors come from CSS variables a tool may set on `:root`: `--dd-1` to `--dd-6` (series), `--dd-text`, `--dd-axis`,
`--dd-grid`, `--dd-ring` (highlights), `--dd-bgline` (the thin edge of solid marks) and `--dd-bg-solid` (the inside of hollow marks; falls back to
`--paper`). The engine's defaults sit in `:where(:root)`, colorblind-safe light ones, or dark ones when the 9-12
theme is loaded, so any tool's own values win. Every chart has a text alternative listing its numbers.

## Data rules (all siblings)

- **Real data, with a source** in the spec and in the tool's credit comment. Public datasets only (government
  statistics, NOAA, World Bank, sports reference tables, published research data sets), copied in as JSON with the
  date pulled.
- Student-entered data stays in the browser (localStorage at most), and nothing is ever sent anywhere.
- Keep each dataset small enough to read: under about 200 rows on screen, or paged (`renderTable` `page`).
  Settled exception: simulation-studio keeps all 299 rows of its log, 15 a page, because trimming would remove the
  flaws it teaches.

## What each tool brings (its own)

| Tool | Grade | Its one idea (not shared) | Data set |
|---|---|---|---|
| data-table-builder | 4 | the class collects its own data, then picks the chart that answers its question | |
| box-plot-builder | 6 | drag one point and watch mean and median react differently; outliers get dramatic | |
| region-compare | 6 | world regions side by side on population, income, language and climate | |
| data-detective | 8 | scatter plots and lines of fit; a two-way table hiding a surprise | |
| which-model-wins | 9 | linear vs quadratic vs exponential on the same data; pick and defend the best | |
| where-s-my-phone-from | 10 | a phone's parts traced across a world map, with the trade numbers | |
| economy-dashboard | 12 | GDP, inflation and unemployment over decades; spot the recessions | |
| data-desk-distributions | 12 | describe shape, center, spread and the unusual, with guided prompts | |
| simulation-studio | 9-12 | clean a real log with ordered steps, build a simulated geyser from it, test a prediction | Old Faithful, August 1985 (MASS `geyser`, Azzalini and Bowman 1990), 299 rows, paged |
| lunch-survey-cleanup | 6-8 | fixing data quality problems in a school lunch survey and reporting the limits | school lunch survey |
| catalog-column-rules | 9-12 | drop, reformat or keep per column rules the student writes, checked three ways (its spec asks for a `t.validate(dictionary)` engine addition, settled to be built with that tool, not before) | Seattle Public Library catalog |

## Rules for siblings

- Charts, stats and fitting come from the engine. A sibling adds its own scene (a map, a scoreboard, a world)
  and its own questions.
- No two siblings use the same dataset. Claimed so far: Old Faithful 1985 (simulation-studio). Settled:
  data-detective and data-desk-distributions pick other data sets (noted in their specs before they are built).
- New engine features go into the engine and this file in the same change, keeping existing calls working.
- Charts that a student compares side by side, or drags in, use fixed `xDomain` and `yDomain`.

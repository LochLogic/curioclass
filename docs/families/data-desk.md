# Family: data desk

Nine tools, grade 4 to 12 (math, computer science, social studies), share one data engine: `kit/data-desk.js`,
inlined with `<script src="kit:data-desk"></script>` after `kit:curio`. The first tool built in this family writes
the engine to this spec.

## What the engine does (shared)

A small table and the charts that read from it, all drawn in SVG, all updating live when data changes.

```js
const t = DataTable([{name: 'Ava', shoe: 7, height: 152}, ...], {
  columns: {shoe: {label: 'Shoe size', unit: ''}, height: {label: 'Height', unit: 'cm'}},
});
t.rows, t.add(row), t.set(i, key, v), t.remove(i), t.on('change', fn)
t.column(key) -> numbers; t.stats(key) -> {n, min, max, mean, median, q1, q3, iqr, mad, sd, outliers}
t.renderTable(el, {editable: true})                 // a real <table>, keyboard editable, screen-reader friendly

Chart(svgGroup, t, {type: 'dot' | 'bar' | 'histogram' | 'box' | 'scatter' | 'line', x: 'shoe', y: 'height',
                     width, height, bins, groupBy})  // returns {update(), highlight(i), onPoint(fn)}
chart.fit('linear' | 'quadratic' | 'exponential')   // least squares; returns {f, params, r2, residuals}
chart.drag(true)                                    // drag points; the table and every chart follow
```

Fixed by the engine: axis style, tick choice ("nice" steps), point size (larger on touch), colors per series from
`--dd-1` to `--dd-6` (colorblind-safe, never the only signal: shapes too), number formatting, the readout of stats,
the outlier rule (1.5 IQR). Every chart has a text alternative listing its numbers.

## Data rules (all siblings)

- **Real data, with a source** in the spec and in the tool's credit comment. Public datasets only (government
  statistics, NOAA, World Bank, sports reference tables), copied in as JSON with the date pulled.
- Student-entered data stays in the browser (localStorage at most), and nothing is ever sent anywhere.
- Keep each dataset small enough to read: under about 200 rows on screen.

## What each tool brings (its own)

| Tool | Grade | Its one idea (not shared) |
|---|---|---|
| data-table-builder | 4 | the class collects its own data, then picks the chart that answers its question |
| box-plot-builder | 6 | drag one point and watch mean and median react differently; outliers get dramatic |
| region-compare | 6 | world regions side by side on population, income, language and climate |
| data-detective | 8 | scatter plots and lines of fit; a two-way table hiding a surprise |
| which-model-wins | 9 | linear vs quadratic vs exponential on the same data; pick and defend the best |
| where-s-my-phone-from | 10 | a phone's parts traced across a world map, with the trade numbers |
| economy-dashboard | 12 | GDP, inflation and unemployment over decades; spot the recessions |
| data-desk-distributions | 12 | describe shape, center, spread and the unusual, with guided prompts |
| simulation-studio | 9-12 | simulate chance, clean a messy dataset, then chart what it says |

## Rules for siblings

- Charts, stats and fitting come from the engine. A sibling adds its own scene (a map, a scoreboard, a world)
  and its own questions.
- No two siblings use the same dataset.
- New engine features go into the engine and this file in the same change, keeping existing calls working.

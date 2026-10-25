# Family: graphing

Eight tools, grades 8 to 12 (algebra to precalculus), share one coordinate-plane engine: `kit/graphing.js`, inlined
with `<script src="kit:graphing"></script>` after `kit:curio`. The first tool built in this family writes the engine
to this spec.

## What the engine does (shared)

A coordinate plane in SVG that plots functions and points and lets people drag things that change them.

```js
const g = Plane(svgGroup, {x: [-10, 10], y: [-10, 10], width: 600, height: 600, grid: 1, labels: 5,
                           xLabel: 'time (s)', yLabel: 'height (m)', left: 0, top: 0, ticks: 'axis', tickFormat});
g.px(x, y) / g.coord(px, py) / g.eventCoord(pointerEvent)   // data <-> plane pixels (handles a scaled stage)
g.fn(f, {color, width, domain: [a, b], id, dashed, arrows, label, class, layer, opacity})
                                                          // plot y = f(x), adaptive sampling, breaks at asymptotes
g.param(f, [t0, t1], {...})                               // parametric: f(t) returns [x, y]
g.point(x, y, {label, color, draggable, onMove, onDrop, onKey, snap, lock, range, step, shape, r, hit, ariaLabel, valueText})
                                                          // pointer and keyboard; returns a handle
g.segment(a, b, {color, width, dashed, arrow: 'end', id, layer}); g.label(x, y, text, {anchor, dx, dy, id, layer})
g.intersect(f1, f2, [a, b]) -> [x...]                     // numeric roots and crossings
g.roots(f, [a, b]) -> [x...]                              // sign changes and touching (even multiplicity) roots
g.extrema(f, [a, b]) -> [{x, y, kind: 'max' | 'min'}]     // interior turning points; a flat crossing is not one
g.trace(f, {x, onMove, draggable, readout, domain, valueText, hit})  // a moving dot that reads out (x, f(x)); t.set(x)
g.view([x0, x1], [y0, y1], {ms})                          // animated zoom and pan (instant with Motion off)
g.slider(container, {label, min, max, step, value, onInput, scale: 'log', box, format, parse})
                                                          // labeled, keyboard-friendly parameter slider
g.clear(id)                                               // remove everything with that id (no id: all)
g.layer('back' | 'grid' | 'plot' | 'front' | 'points' | 'labels'); g.onClick((x, y, e) => ...); g.onView(fn)
Plane.fmt(n, dp) / Plane.fmtSig(n, sig) / Plane.roots / Plane.extrema / Plane.slider   // usable without a plane
```

Details (added by rollercoaster-polynomials, 2026-10-25):

- **Options.** `grid` and `labels` take one step or `[xStep, yStep]`. `ticks: 'axis'` puts tick labels beside the
  axes; `'edge'` puts them outside the bottom and left edges, 16 px clear of the plane so a handle on the edge does not cover them (leave about 60 px of margin) with the axis labels
  centered under and beside the plane. `left`/`top` place the plane inside its SVG group.
- **Changing ranges** (added by outbreak-model, 2026-10-25). A `grid` or `labels` step may also be a function
  `(lo, hi) => step`, worked out again on every view change, so a plane whose range grows from 10 to 10 billion
  keeps about the same number of lines. `tickFormat: (v, axis) => text` (axis `'x'` or `'y'`) writes the tick
  labels; return null or `''` to leave a tick unlabeled (for example to place your own with `g.label`). Default:
  `Plane.fmt`. `g.trace` also takes `valueText(x, y)` (its screen-reader value, for a plane whose y is not the
  value itself, such as log10 N) and `hit`, and returns `setHit(r)` and `point`; its `domain` array is read live,
  so a tool may change it in place when the window widens.
  Tick and axis text live in their own group inside the `labels` layer, so a tool's own `g.label(..., {layer:
  'labels'})` items survive a `g.view` (before this they were wiped on the first view change).
- **Colors.** `color: 1` to `4` means `var(--gr-1)` to `var(--gr-4)` and also applies that series' dash pattern
  (1 solid, 2 `10 6`, 3 `2 5`, 4 `12 4 2 4`), so color is never the only signal; any CSS color also works.
  `dashed: true` or a dash string overrides. The grid, axes and tick text read `--gr-grid`, `--gr-grid-major`,
  `--gr-axis` and `--gr-text` (the 9-12 theme sets them all).
- **Curves.** `arrows: 'start' | 'end' | 'both'` puts arrowheads where the visible curve ends (end behavior).
  Curves are clipped to the plane; the returned item has `.el` (its group) and `.path` for extra styling such as a
  tool's own `clip-path`.
- **Points.** `lock: {y: 0}` keeps a point on the line y = 0 so it slides left and right only (`{x: c}` locks it to
  a vertical line); arrow keys then move it along that line only and its `aria-valuetext` reads "x = ...".
  `snap` is a step or `fn(x, y) -> [x, y]`, and can be changed later as `handle.snap`. `range: {x: [a, b]}` clamps.
  `onMove` fires while it moves, `onDrop(x, y, h, from)` when a drag or key press ends (each arrow press is a move
  and a drop). `onKey(e, h)` sees other keys first and returns true when it handled one (Delete, 1, 2, 3...).
  `shape: 'none'` plus `handle.body` lets a tool draw its own marker in pixels around the point. The pointer target
  is a circle of radius `hit` (default 22, a 44 px target at scale 1); raise it when the stage is scaled down,
  or later with `handle.setHit(r)` (for example from a resize observer, as 22 divided by the stage scale).
  Focus shows a ring in `--focus`.
- **Layers**, bottom to top: `back` (with a transparent hit area for `onClick`), `grid`, `plot`, `front` (all
  clipped to the plane), then `points` and `labels` (not clipped). A tool's own scene goes in these with `g.px`.
  Plotted curves, segments, labels and the grid ignore the pointer, so `onClick` sees the whole plane.
- **Slider.** `scale: 'log'` spreads min to max (both above 0) evenly in powers of ten. `box: true` adds a number
  box; `format(v)` sets its text and the slider's `aria-valuetext`; `parse(text)` returns the value to use or
  null to refuse (the box then shows the last value). `onInput(v, source)` gets `'slider'`, `'box'` or `'set'`.
  Handle: `{value, set(v, quiet), refresh(), el, range, box}`.

Fixed by the engine: axes and grid style, tick labels, the colors `--gr-1` to `--gr-4` (with dash patterns so color
is never the only signal), point handles (44 px hit area), readout format (`Plane.fmt`: trailing zeros dropped, a
true minus sign), keyboard nudging, the sampling that keeps curves smooth. Every plotted function also shows its
equation in text: in the tool's panel, and as the curve's `label` (its accessible name).

## What each tool brings (its own)

| Tool | Grade | Its one idea (not shared) |
|---|---|---|
| ski-slope-designer | 8 | slope as a feeling: too steep crashes, too flat stalls |
| two-trains | 8 | two lines, one meeting point, and the case where they never meet |
| story-graphs | 8 | stories matched to shapes of graphs, then drawing your own |
| intersection-quest | 9 | one system solved three ways, racing your own best time |
| graph-story-lab | 9 | real graphs labeled with domain, range, max and intervals |
| launch-pad | 9 | a projectile's path is a quadratic; its roots are where it lands |
| rollercoaster-polynomials | 11 | build a coaster from zeros and degree; it must start and end on the ground |
| function-family-reunion | 12 | parent functions and their transformed relatives, one slider per parameter |

## Rules for siblings

- Plotting, dragging, solving and sliders come from the engine; a sibling adds its scene (a ski hill, a rail line,
  a launch pad) drawn in its own SVG, positioned with `g.px`.
- No sibling repeats another's scenario.
- New engine features go into the engine and this file in the same change, keeping existing calls working.

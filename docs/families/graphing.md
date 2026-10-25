# Family: graphing

Eight tools, grades 8 to 12 (algebra to precalculus), share one coordinate-plane engine: `kit/graphing.js`, inlined
with `<script src="kit:graphing"></script>` after `kit:curio`. The first tool built in this family writes the engine
to this spec.

## What the engine does (shared)

A coordinate plane in SVG that plots functions and points and lets people drag things that change them.

```js
const g = Plane(svgGroup, {x: [-10, 10], y: [-10, 10], width: 600, height: 600, grid: 1, labels: 5,
                           xLabel: 'time (s)', yLabel: 'height (m)'});
g.px(x, y) / g.coord(px, py)
g.fn(f, {color, width, domain: [a, b], id, dashed})       // plot y = f(x), adaptive sampling, breaks at asymptotes
g.param(f, [t0, t1], {...})                               // parametric (x(t), y(t))
g.point(x, y, {label, color, draggable, onMove, snap})    // pointer and keyboard; returns a handle
g.segment(a, b, {...}); g.label(x, y, text)
g.intersect(f1, f2, [a, b]) -> [x...]                     // numeric roots and crossings
g.roots(f, [a, b]); g.extrema(f, [a, b])
g.trace(f, {onMove})                                      // a moving dot that reads out (x, f(x))
g.view([x0, x1], [y0, y1], {ms})                          // animated zoom and pan
g.slider(container, {label, min, max, step, value, onInput}) // labeled, keyboard-friendly parameter slider
g.clear(id)
```

Fixed by the engine: axes and grid style, tick labels, the colors `--gr-1` to `--gr-4` (with dash patterns so color
is never the only signal), point handles (44 px hit area), readout format, keyboard nudging, the sampling that keeps
curves smooth. Every plotted function also shows its equation in text.

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

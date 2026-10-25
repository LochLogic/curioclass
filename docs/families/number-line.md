# Family: number line

Five tools, grades 2 to 8, share one number-line engine: `kit/number-line.js`, inlined with
`<script src="kit:number-line"></script>` after `kit:curio`. The first tool built in this family writes the engine to
this spec; later siblings use it and only add what the spec below allows.

## What the engine does (shared)

An SVG number line that any tool can draw into its own scene, horizontal or vertical.

```js
const nl = NumberLine(svgGroup, {
  from: 0, to: 100,            // visible range
  length: 860,                 // px along the line
  vertical: false,             // deep-sea-dive turns it upright (up is positive)
  ticks: [{every: 10, size: 'big', labels: true}, {every: 1, size: 'small'}],
  format: v => String(v),      // tick labels: fractions, decimals, negatives
  snap: 1,                     // drag and tap snap to this step (or a function)
});
nl.x(value)                    // value -> px along the line
nl.value(px)                   // px -> value (unsnapped)
nl.mark(value, {label, color, shape: 'dot' | 'flag' | 'pin', id})   // add or move a marker; returns it
nl.jump(from, to, {label, color, above: true})                       // an arc with an arrowhead, animated unless Curio.reduce
nl.span(a, b, {color, label})                                        // a shaded stretch (distance, an interval)
nl.zoom(from, to, {ms})        // animate the visible range (square-root-hunt), relabeling ticks
nl.draggable(marker, {onMove, onDrop, min, max})                    // pointer and keyboard (arrows step by snap)
nl.clear(kind)                 // remove marks, jumps or spans
nl.on('tap', value => ...)     // a tap on the line, snapped
```

Fixed by the engine, so every sibling feels related: line weight, tick lengths, label font, marker shapes, jump arc
shape and its arrowhead, keyboard steps, focus ring, the 60 px drag handles for K-2 sizes. Colors come from the
tool's CSS variables (`--nl-ink`, `--nl-mark`, `--nl-jump`).

## What each tool brings (its own)

The world around the line, the story, the content and the mode. The engine never draws scenery.

| Tool | Grade | The line is... | Its one idea (not shared) |
|---|---|---|---|
| jump-line | 2 | an open line with no ticks until you place them | many jump paths to the same answer, compared side by side |
| roller-coaster-rounding | 3 | a coaster track with hills at the tens and hundreds | the car rolls to the nearer hill; 45 rolls up |
| fraction-trail | 3 | a hiking trail split into halves, thirds, fourths... | campsites at 3/4 and 6/8 land on the same spot |
| deep-sea-dive | 6 | a vertical line through sea level | above and below zero; distance and absolute value |
| square-root-hunt | 8 | a line that zooms in between decimals | squeezing the square root of 2 forever closer |

## Rules for siblings

- Use the engine for the line, markers, jumps, spans, zoom and dragging. Do not draw a second number line.
- Don't reuse another sibling's scenery or metaphor. A sibling may add tool-only marks (a coaster car, a diver)
  as its own SVG positioned with `nl.x(value)`.
- If a sibling truly needs a new engine feature, add it to the engine and to this file in the same change, keeping
  the existing calls working.

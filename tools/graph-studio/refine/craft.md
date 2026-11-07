# Refine, Craft lens: graph-studio (Curiosity No. 08)

Round 1, 2026-11-06. Cold lens, judged against CODEX-CURIOSITY.md, VISION "Curiosities: the second shape",
STANDARDS and BASELINE. Bundle `tools/graph-studio/graph-studio.html` as built (not re-bundled). My frames and logs:
`S:/CurioClass-codex-scratch/graph-studio/craft/r1/` (shots `perf.json`, `v.json`, `d.json` beside it), Chrome on
port 9431, closed after. No host server started; the 375 frames are cited from the audit.

Counts: blocker 0, should fix 4, polish 7, nit 2.

## Contract (clean)

- One file, 121,581 bytes (goal 2 MB). `performance.getEntriesByType('resource')` is empty after load and a full
  setup walk: no network requests. The Manual's source links are plain `target=_blank` anchors, not requests.
- No console errors, warnings or exceptions in 29 driven shots; the audit's resize-mid-action and Motion off rows are
  clean. `scripts/check_tools.py` lists it as a draft with no failure.
- No em dashes in src, bundle, notes or spec. "Curio Class" is never shortened. Lesson creep search: "points" appears
  only as "key points" and "data points"; no score, goal, level, sticker, finish or quiz. No welcome screen or kit header.
- Look rules: the paper fills the screen, the plate and Manual sit lower-left (src.html:305-310), Motion, Sound and
  Read sit on the plotter's own power panel (src.html:288-290), readouts are monospace. Kit used for voice, tones,
  Motion and Sound only (src.html:1726-1734), controls are the tool's own.
- Privacy is stated where pages are saved (src.html:353-354, 453). Art: `prompts.json` has no assets and the source
  has no `art:` tokens; everything is drawn in code, as a Curiosity should.
- Done when, craft side: 1 PASS (real drag on the exponent: 268 frames, median 16.7 ms, none over 20 ms;
  `perf-drag-exponent`), 3 PASS (`f(4) = 4.000`), 4 PASS (crossings 1.0776 and 58.7701, plus -0.9371), 5 PASS
  (line 0.9806, quadratic 0.9995), 6 PASS (`y = 1.000 x^1.500`), 7 PASS (`Δy/Δx = 4.000`, `d5-trace-pins-frame.png`),
  8 PASS (`d1-breaks.png`: tan and 1/x break, open circle at (0, 1)), 9 PASS with the naming gap below, 10 PASS on
  the audit's size frames, 11 and 12 PASS.

## Findings

### Should fix

1. **Key points make every redraw slow once there are several lines.** src.html:1098-1105 (pairwise intersections,
   3,500 samples per pair) and 1093 (turning points), run from `rebuildPaper` (1151) on every dirty frame: each
   scrub, pan, zoom and every frame of a playing ruler. Measured on a 32-thread desktop: one to four lines with
   key points on cost 2 to 3.5 ms per redraw and hold 16.7 ms frames; eight lines with key points on cost 31 ms per
   redraw and a playing ruler drops to 33 ms frames (92 of 119 over 20 ms, `perf-play-eight-keys`); eight lines with
   key points off cost 6.3 ms. On a school Chromebook (roughly 3 to 5 times slower) that is about 8 fps with key
   points and under 60 fps even without. Better: compute features only when the pointer or ruler settles (or every
   few frames while animating), cache them per view, and limit intersections to the active line against the others.
   How seen: `perf-bench`, `perf-play-eight-keys`, `perf-four-keys`. Tag: family:curiosity (the 60 fps rule).
2. **Pressing Read, Sound or Motion removes the first-run hint.** src.html:1735-1737 calls `dismissHint()` for any
   button click, including #read, #sound and #motion. A student who presses Read to hear the hint hears it once, the
   hint vanishes from the paper, and the next Read says "Type an equation, drag a number tab, or move a ruler."
   instead. The Curiosity rule is that the hint stays until the first action on the instrument and Read speaks it;
   the power panel is not that action. Better: skip `dismissHint` for the power panel buttons. How seen: `v5`
   (Sound then Read reads the fallback line), `v6` (five Reads: the first says the hint, the rest do not).
   Tag: family:curiosity.
3. **Toggles announce element ids, and the reset button is named "0".** src.html:1433 announces `${id} on`, so a
   screen reader hears "angle on" (meaning degrees), "log-x on", "keypoints on", "square on". #home
   (src.html:295) has only a `title`, so its accessible name is "0". Done when 9 asks every control to announce its
   value. Better: "Degrees" / "Radians", "Log scale on x", "Key points on", "Square grid on", and
   `aria-label="Reset axes to minus ten to ten"`. How seen: `a3-announce` (live region log). Tag: general.
4. **The log axis title says log₁₀ x while the ticks show x.** src.html:983-984 writes "log₁₀ x" and "log₁₀ y" as
   axis titles, but the tick labels are the values themselves (1, 10, 100; src.html:961-962). A student reading the
   planets plot sees "log₁₀ y" beside "100" and can take it as log y = 100. A readout that misleads. Better: keep the
   title "x" / "y" (or the data's unit) and mark the scale as "log scale". How seen: `d4-planets-frame.png`.
   Tag: family:curiosity (graphing readouts).

### Polish

5. **The hint line comes 1.5 s late on a first tap of the 2.** The number tab's pointerup re-renders the tape
   (src.html:892 `renderTape()`, with the deferral at 751-755), so the button under the pointer is replaced and no
   `click` fires; the kit's first-tap decision then waits for its 1.5 s fallback. The 2 is the one control the hint
   names, so this is the tap most students make first. Logged: first tap about 1.25 s, hint spoken at 2.72 s (`v1`);
   `d7-firsttap-click` shows no click event at all. Better: refresh the scrubbers in place on a tap without movement
   instead of rebuilding the line. Tag: general.
6. **Read speaks a trace point that is not on the paper.** src.html:1721-1724 always adds "At x equals 1.000, y equals
   1.000." from `state.traceT`, even with the trace pen parked and no tag showing (`v6`, `tracing: false`). Numbers
   are spoken with four significant figures ("one point zero zero zero"), where the spec's example is "At x equals 3,
   y equals 9". Better: speak the point only while tracing, and trim trailing zeros for the ear. Tag: general.
7. **Readouts lose their units when data is loaded.** With Mauna Loa loaded the cursor reads "x 1992 · y 371.7"
   (src.html:1335), the trace tag "x ... · y ..." (1223) and the axes "x" and "y"; the unit is only in the 10 px
   footer ("year / ppm", 1175). The look rule asks for readouts with units. Better: "year 1992 · 371.7 ppm" and unit
   axis titles when a dataset is loaded. How seen: `d8-data-units`, audit `state-data-375x812.png`.
   Tag: family:curiosity.
8. **The pen carriage parks under the power panel.** After the opening draw the carriage stops at 95 percent of the
   rail (src.html:1200), which is behind #power (136) at every size, so the plotter's signature object is hidden at
   rest. Better: park it at the curve's last visible point left of the panel, or move the panel off the rail end.
   How seen: audit `size-1366x768.png`, `size-680x425.png`, `size-375x812 (iframe host).png`. Tag: family:curiosity.
9. **The paper's focus ring is mostly clipped.** The canvas outline (src.html:62) is cut by `#paper { overflow:
   hidden }` on the sides and covered by the rail on top, so a keyboard user sees one blue line along the bottom
   edge. Better: an inset outline or a focus frame drawn inside the paper. How seen: `a2-canvas-focus.png`.
   Tag: general.
10. **On the paper, colour is the only link from a curve to its tape line.** With several pens the inks pair up
    closely (green #2d6a3e and teal #116466, brown #7a4a1e and orange #a4480a) and no curve carries its pen number.
    Tracing names the pen, but only after a tap. Better: a small pen number at each curve's end on the paper.
    How seen: `d9-eight-lines-1366.png`. Tag: general.
11. **Sound is only a click tick.** The spec's first two minutes have the pen draw "with a soft scratch"; the only
    sounds are a 135 Hz button tick and a 160 Hz scrub tick (src.html:892, 1738), and only the opening draw animates
    the pen. Better: a quiet pen scratch while a redraw inks (after the first tap). Tag: family:curiosity.

### Nit

12. The table header reads "x | x | y" for ordinary curves (src.html:442 with 1561). Name the first column
    "step" or drop it when the parameter is x. Tag: general.
13. Several labels are 10 px: the tape engraving, the plate, the end-cap captions, the samples footer
    (src.html:76, 115, 155, 161). Readable, but small on a projector. Tag: general.

## Standard voice check

One line in `voice/lines.json`, "Drag the 2 up or down.", identical to `allLines()`. Driven with held clicks (0.12 s),
Sound and Motion on.

| line | kind | expected | spoken |
|---|---|---|---|
| "Drag the 2 up or down." (5 taps on the 2, 3 s apart) | welcome / how | once | 1 |
| Read (5 presses, 2 s apart) | read | 5 | 5 (the first with the hint, the rest with the fallback: finding 2) |

- First tap: Tab key, hint at once (`v4`); the 2, hint 1.5 s late (finding 5); the paper, a mode drawer, Zoom and the
  other buttons, no line, and the hint leaves the screen: allowed by BASELINE rule 16, the hint has done its job.
  Read speaks the hint only before the first action; Sound says nothing.
- Read: speaks with Sound off (`v5`); a drawer change after Read hushes it, as a mode change should.
- Stale lines: four taps 0.2 s apart (the 2, paper, Zoom in, Data) spoke nothing late (`v3`). Order: one line, nothing
  to reorder.

## Sensitivity

The Census series notes (Manual, src.html:385-394; notes.md "Good to know") say early censuses excluded many
Indigenous people and link the Bureau's "Censuses of American Indians" page. Not judged here: flag for the
sensitivity agent (rule 5).

## Audit pilot

- Leads confirmed: none that are faults. The #hint over #plot overlap and the trace and pin tags over #plot are the
  instrument's own labels, as designed.
- Leads wrong: "hint out of view" in every state (the hint is meant to leave after the first action); "keep region"
  for #plot and #equation-0 under the Manual, Notebook and Table drawers (drawers slide over the tape and paper by
  design, and the paper stays visible beside them at 1366); "choices cut short" in the Manual and Data drawers and the
  rose ruler's end caps at 680x425 and 375x812 (they scroll inside their panels and are reachable); "#add text under
  10 px" at 375 (an icon button drawn with `::after`, named "Add equation").
- Partly right: the held-click table marks the 2 as "heard"; it was heard, but 1.5 s late (finding 5).
- Missed: the key-point frame cost (finding 1), Read, Sound and Motion removing the hint (2), id-named announcements
  and the "0" button name (3), the misleading log axis title (4), the clipped canvas focus ring (9) and the carriage
  parked under the power panel (8).

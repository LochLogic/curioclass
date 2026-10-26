# Resilience Map art plan (island map and body figure)

Cory's review: "graphics can be improved" (voice is handled separately). Today the tool has no art files: the island,
pins, icons, lighthouse, body figure and chart are all drawn in code (spec "Art: none"). Students in grades 9-12 are the
audience, so the look should be grown up: a real illustrated island seen from above and a calm medical-illustration
body figure, not storybook shapes. Prompts are in `art/prompts.json` (two assets).

Everything interactive stays code on top of the paintings: pins, pin icons, labels, area names, route paths, the
harbor dot, the lighthouse beam pulse, the legend, the body hotspot pills, leader lines and dots, the sleep moon and the
week chart. The paintings carry no text, letters or labels.

## Assets

| # | Name | Source | Aspect / output | Size budget (WebP) | Replaces (code-drawn) | Where in src.html |
|---|---|---|---|---|---|---|
| 1 | map-island | Cloudflare FLUX.2 klein (`scripts/cfart.py`, free, no people) | 16:9, drawn 1344x768, saved at width 1600, quality 72 | 120-200 KB (aim 150) | the island outline, sand shore, ridge with hatch pattern, Mind Woods and village ellipses, sea wave marks, the dock | `buildMap`, lines 550-566 (outline, ridge, `clipPath#isl`, `pattern#hatch`, sea rect, wave marks, island fill, ridge, ellipses) and line 570 (dock path) |
| 2 | body-figure | Codex gpt-image-2 (`scripts/gptart.py`, `"people": true`) | 9:16 (Codex draws 2:3 portrait), cutout on green, despill, height 800, quality 74 | 45-75 KB (aim 60) | the rounded-rect figure (arms, legs, torso, neck) and head circle | `buildBody`, lines 725-733 (the `<g fill="#71879e">` group); `PT` table lines 735-736 is re-measured |

Codex images: 1 first draw, allow 2-3 redraws (pose, organ placement, a face sneaking in). Cloudflare: draw 6-8
candidates of the map (`--n 8`, about 100 neurons each, well inside the free day) and pick the one whose regions sit
closest to today's pin layout.

What stays as it is: the 25 pin and area icons in `ICON` (lines 489-514) and the route glyphs `WRENCH` / `WAVE`
(517-518). They are 13-18 px line icons; painted icons at that size turn to mush, and line icons already read as
grown up. The week chart (`drawBodyState`, 773-807) stays code (it is data, and Done when 2 checks it in grayscale).
The plan card stays code (print is white paper, black ink).

### Why these two only

Those are the two big surfaces a student looks at the whole time, and the two places the code drawing looks most
like a placeholder (a blob island with ellipses, a figure made of rounded rectangles). Smaller ornaments (a compass
rose, area emblems) were left out: FLUX tends to letter compass roses (N, E, S, W), and the area names already carry
code icons.

## Look and neighbors

- Map: twilight atlas painting, deep navy sea `#10263a` (the spec's `--sea`, so the stage background and the
  painting's edge match), pale sand west shore, dark green forest north, a small village center, grey-blue ridge east,
  a white lighthouse on a south point. Colors in the prompt are the spec's scene colors, so the contrast table stays
  close. It must look different from the nearest map neighbor, mind-map (a pale watercolor explorer's map): ours is
  dark, top-down and painterly.
- Figure: smooth featureless mannequin form in the spec's `--fig` slate blue `#71879e`, no face, no hair, no gender
  cues (all as the spec asks today), plus the four organs the hotspots point at (brain, heart, stomach, neck and
  shoulder muscles) softly visible inside, in muted tones. No skeleton, no blood, nothing gory.

## Size

Measured 2026-10-26: `python scripts/bundle_tool.py resilience-map` reports 273 KB; `resilience-map.html` on disk is
281,600 bytes (275 KiB). Limit (`scripts/check_tools.py`): 2 MiB = 2,097,152 bytes, so headroom today is about
1,773 KiB.

- New art: map about 150 KB + figure about 60 KB = about 210 KB as files (range 165-275 KB).
- Inlined as base64 that is x 4/3: about 280 KB (range 220-365 KB).
- The removed vector drawing code is small (about 3 KB).
- Bundle after: about 275 + 280 - 3 = about 552 KiB (range 490-640). Headroom after: about 1,495 KiB (1,400-1,555).
- There is room to spare, so a sharper map is affordable if it looks soft on 1920x1080: width 1920 at quality 76 is
  about 220-280 KB (about +100 KB in the bundle). Try 1600 first.
- If an image comes back over budget, drop quality by 6 with `localart.py --pick` again (free); never below 64.

## Display sizes

Stage sizes (from the page layouts in `relayout`, lines 1059-1078; legend band about 30-50 px off the bottom):

| Box | Layout | Map stage (approx.) | Island box shown (approx.) |
|---|---|---|---|
| 1920x1080 | wide | 1560 x 985 | about 940 tall, so the full painting about 1120 x 1990 (sides cropped) |
| 1366x768 | wide | 1006 x 670 | about 620 tall, painting about 740 x 1315 |
| 1280x720 | wide | 920 x 625 | painting about 690 x 1230 |
| 1000x625 | compact | 680 x 545 | island fits by width |
| 680x425 | compact | 390 x 340 | island fits by width, small sea bands top and bottom |
| 375 wide | stack | 375 x about 345 | island fits by width |

The 1600 px painting is shown at 0.5x to 1.25x of its pixels: sharp at 1366, slightly soft at 1920 (painterly
texture hides it).

Figure: `side2` layout (wide boxes) shows it at most about 236 x 520 CSS px (k = 2.36 on today's 100 x 220 design, set
by the pill columns); `side1` (preview) about 120 x 260; `vert` (narrow, tall) up to about half the stage height.
800 px tall covers 1.5x the largest display.

## Wiring notes (phase 2)

### Map

1. **Fixed aspect.** Today `buildMap` stretches the island box separately in x and y (`bw`, `bh`, line 546) to fill
   any stage. A painting cannot stretch, so the box becomes uniform: after the pick, measure where the island box
   (u, v from 0 to 1, the frame every pin uses) sits in the image as fractions, `ISL = {x0, y0, w, h}`, plus the
   image aspect `AR`. Then per size: fit the island box (with its outline margin, as today: -0.04 to 1.05 across,
   -0.08 to 1.06 down) inside `W x (H - legH)` with uniform scale `s`, center it, and place the image at
   `imgX = box.x - ISL.x0 * imgW`, `imgY = box.y - ISL.y0 * imgH`, `imgW = box.w / ISL.w`, `imgH = imgW / AR`.
   `P(u, v)` keeps its formula (`box.x + u * box.w`, `box.y + v * box.h`); only `box` is now uniform.
2. **Sea outside the painting.** The stage background is already `--sea` (`#10263a`). On wide stages the painting
   overflows the sides and is clipped by the SVG; on near-square stages (stack, preview) thin sea bands show above and
   below. The prompt asks the sea to darken evenly to the edges; after the pick, sample the four edge strips. If any
   is more than about 6 levels off `#10263a`, add an SVG `<mask>` that fades the painting's outer 4 percent to
   transparent (no seam).
3. **Draw order** in the SVG: sea rect, `<image href="art:map-island" preserveAspectRatio="none" aria-hidden="true">`
   at the rect above, then the beam, `#routeLayer`, `#pinLayer`, `#labelLayer`, legend band (unchanged).
4. **Re-place the pins on the painting.** The painting will not land exactly on today's layout. After the pick, put a
   debug cross at every `LM[].u, v` and `HARBOR` over the image (a one-off frame with `drive.py`), then edit the u, v
   values so each pin sits on its region: Body Coast pins on the west sand and dunes, Mind Woods on the forest edge
   or clearings, People Village on or beside the houses, Action Ridge on the hills, `help` just west of the painted
   lighthouse (the pin disc must not hide the tower), `HARBOR` at the land end of the painted dock. Keep pins at least
   2r + 22 px apart at 680x425 (today's spacing) so the 44 px hit circles do not overlap. Add `LAMP = {u, v}` for the
   painted lamp and start the beam (line 575) there instead of at the pin.
5. **Hit areas line up by construction.** Pins, hit circles (`r="22"` transparent circle, line 595), labels and the
   painting all come from the same `box` and `P(u, v)`, so a pin stays on its painted spot at every size; nothing is
   positioned in image pixels. Check with `drive.py` frames at every STANDARDS size, plus one debug frame at 1366x768
   and 680x425 with the hit circles stroked.
6. **Removed:** `outline`, `ridge`, `blob()` (used only here), the `isl` clip path, the `hatch` pattern, the wave
   marks loop, the island and ellipse fills, the dock path. `M.AL` area-label candidate spots (lines 612-614) are
   re-picked to sit over each painted region (open meadow or sea next to it).
7. **Label legibility on a busy painting.** Add a halo to `.lbl` and `.alab`: `paint-order: stroke;
   stroke: #0b1a28; stroke-width: 3.5px; stroke-linejoin: round`. Ink `#e8edf3` on the halo is about 15.0:1, so the
   label passes AA whatever is under it. Update the contrast lines in the spec "Look" (land and sand are now painted
   areas; quote the halo ratio instead).
8. **Dimming.** With a situation picked, add a `#10263a` scrim at about 0.25 opacity over the painting (under the
   route and pins) so the lit route reads first; fade it with the route (300 ms, instant with Motion off).
9. **Grayscale check** (Done when 2): the route is still solid vs long dashes with wrench vs wave glyphs; confirm the
   painting has no line that reads as a route (the prompt asks for no roads or paths).

### Body figure

1. After the pick, record the cutout's aspect `FAR` (width / height) and each hotspot point as fractions of the image:
   brain (center of the brain), head (temple), focus (forehead), heart, muscles (top of the shoulder), stomach, and
   the sleep moon spot (beside the head, in empty space). Replace `PT` (lines 735-736) with one table of fractions,
   used by every layout; the `one` (side1) table goes away.
2. Size: figure height `fh = min(fig.h - 30, availW / FAR)` where `availW` is `fig.w - 2 * pillW - 40` (side2),
   `fig.w - pillW - 34` (side1) or `fig.w - 40` (vert); `ox`, `oy` center it as today. Then a hotspot point is
   `(ox + PT.u * fh * FAR, oy + PT.v * fh)`.
3. Replace the `<g fill="#71879e">...</g>` group (lines 732-733) with
   `<image href="art:body-figure" x y width height aria-hidden="true">`. The moon icon (line 737), the leader lines,
   the rose dots (r 4.5) and the pills (lines 743-763) are unchanged and draw on top, so every hit area is the same
   44 px pill rect as today. The dot on the painted organ is where the leader line ends.
4. Pill spreading (lines 746-749) is unchanged; check that no leader line crosses the face of another pill at
   760 wide and 680x425.

### Docs and credits (when wired)

- spec.md: "Art" section (two paintings, sources), "Look" (figure description, contrast lines for labels), the stage
  description "an island drawn in code"; notes.md "All art is drawn in code"; src.html header comment line 21.
- tool.json sources: replace "Island, pins, icons, figure and chart drawn in code" with
  "Island painting drawn with FLUX.2 [klein] 4B (Apache 2.0) on Cloudflare Workers AI, edited for Curio Class",
  "Body figure generated with OpenAI gpt-image, edited for Curio Class" and
  "Pins, icons and chart drawn in code".
- Rebuild `preview.svg` (`python scripts/preview.py resilience-map`): it is drawn in code today.

## Draw order

1. Map: `python scripts/cfart.py resilience-map map-island --n 8`, look at the contact sheet
   (`art/raw/_sheet-map-island-cf.jpg`), pick the closest layout:
   `python scripts/localart.py resilience-map --pick map-island:<k>`.
   Check at full size: no lettering anywhere (FLUX sometimes writes on roofs or in the sea), no boats or people, one
   lighthouse, regions where the plan expects them, sea dark at every edge.
2. Figure: `python scripts/gptart.py resilience-map body-figure`, then
   `python scripts/localart.py resilience-map --pick body-figure:20`.
   Check: no face, no hair, no gender cues, organs where the hotspots need them (heart on the body's left, which is
   the picture's right), nothing gory, clean cutout around the fingers.
3. Set `review` in prompts.json for both, then wire (above).

Cory runs the generation commands; this plan only writes prompts.

## Questions for Cory

1. The spec says the figure is "a plain standing figure ... no face, one neutral gray-blue fill". The new one keeps no
   face, no gender cues and the same slate blue, but shows the brain, heart, stomach and neck and shoulder muscles
   softly inside. This is the sensitive (full-review) tier: OK to show organs, or keep a plain silhouette (still
   painted, just no organs)?
2. The map is FLUX (free) per the source rules. FLUX may not put five regions and the lighthouse where asked; plan B
   is re-placing pins on whatever it draws (planned anyway). If none of 8 candidates has a usable south lighthouse
   point, switch the map to Codex gpt-image-2 (one Codex image, better layout control)?
3. Twilight palette (dark, matches the 9-12 dark theme and the lighthouse idea) or a daylight atlas look (brighter, more
   like a textbook map, but the dark UI around it would then frame a bright picture)?
4. Pins keep their code line icons on navy discs. Fine, or restyle them as map markers (teardrop pins) while wiring?

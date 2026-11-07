# Refine, Craft lens: living-earth (Curiosity No. 04), round 1

Cold lens on the built bundle `tools/living-earth/living-earth.html` (not re-bundled). Judged against
CODEX-CURIOSITY.md, the VISION "Curiosities" section, STANDARDS and BASELINE. My frames and scripts:
`S:/CurioClass-codex-scratch/living-earth/craft/` (frames in `f1/`). Shared audit: `audit-r1/`.

## Contract

- One file, 1,957,170 bytes: under the 2 MB goal. Kit used for voice, tone and Motion/Sound (no kit header or cards).
- No network requests: `performance.getEntriesByType('resource')` is empty after load (`f1/c-default`).
- No console errors or exceptions in any of my 20 shots; the audit's every-control and resize rows are clean too.
- Motion off: cited from the audit ("clean: nothing runs forever"); the code steps playback by whole years when reduced.
- Lesson creep: no score, goal, level, sticker, badge or finish anywhere (grep and frames). See finding 12 for "FIT".
- Words: no em dashes in src, notes or tool.draft.json; "Curio Class" never "Curio" alone; the Manual states that
  settings stay on this device (src.html:663). Art: `art/prompts.json` has no assets and src has no `art:` tokens.
- Contrast: every small label I sampled is light on near-black slate (well above AA). Cultural/Native/hard-history:
  nothing to flag; disasters appear as data only.

## Findings

1. **should fix** (family:curiosity). src.html:746 `touch()`. The first-run line "Drag to spin. Press play." is
   spoken after the student's first action, whatever that action was. After a first press of Play it says "Press
   play" while the archive is already playing; after a first drag it says "Drag to spin"; after a first tap on a tool
   tab it plays with the Slice/Stations/Wave panel open, where a drag on the globe no longer spins (in Slice it draws
   the section line). The hint on screen is hidden at the same moment, so the voice is the only place the stale line
   appears. Seen: `vlog` in my `v-play5`, `v-drag-first`, `v-sound-first` shots (the line plays at t~1.3 s, after
   the click), and the audit's one-click table (rows 0 to 13 all speak it). Better: give the line a `valid` check
   (no tool open, not running, no drag yet). If the first action already did one half, say only the other half
   ("Press play." after a drag), and skip the line unmarked when a tool panel opened.
2. **should fix** (general). src.html:1318. The global key handler returns early whenever a BUTTON has focus. After
   any click on a button (Play, a layer, a tool tab, zoom), Q/V/P/F/A and [ ] do nothing and S never strikes. Space
   then presses the focused button instead of Play, so after clicking Volcanoes, Space toggles Volcanoes. Seen by
   reading the handler; my `k-space-body` shot confirms Space and ] work only when nothing is focused. Better: let
   the letter and bracket keys through on buttons. Keep Space for Play unless the button is Play itself, or document
   Space as "press the focused control".
3. **should fix** (general). src.html `drawGeography` (volcano loop). The Volcanoes layer draws 1,609 triangles as
   1,609 separate fill+stroke paths every frame. With Chrome's CPU throttled 4x (my Chromebook stand-in, headless
   with software GL), spinning the globe:

   | layers | median frame | p90 |
   |---|---|---|
   | default (every dot, relief) | 16.7 ms | 33 ms |
   | + Volcanoes | 33 ms | 50 ms |
   | all layers (Volcanoes, Edges, Arrows) | 50 ms | 67 ms |

   Unthrottled, everything holds 16.7 ms (60 fps) with all 26,230 dots. Software GL inflates every row, so treat
   these as relative costs. Volcanoes is the one layer that halves the rate by itself. Better: one path for all
   triangles (one fill, one stroke) or a GL point layer like the quakes. Seen: `throttle.py`, `throttle2.py`.
4. **should fix** (general). With a tool panel open at 1366x768 the globe moves left (`x = w*0.29`, src.html ~886),
   and the selected-quake record card (top-left) covers the globe's left limb. In the audit's Stations state the
   Reveal marker for the struck quake (CATALOG, Sumatra) sits under the card; only the "G" of its label shows.
   Seen: `audit-r1/state-stations-1366x768.png`. Better: collapse the card to one line while an instrument is open,
   or keep the globe clear of it.
5. **should fix** (general). Compact console under about 1050 px wide (680x425, 800x500, 760x900): the depth faders
   lose their names, leaving "≥ 0 km" and "≤ 700 km" unlabeled, and "TIME 1970 SPEED 3 yr/s MAGNITUDE ≥ 5.5" runs
   together as one line. Seen: `audit-r1/size-680x425.png`, `f1/t-pin-760.png`. Better: keep "DEPTH" (or "D≥", "D≤")
   and put a gap or rule between fader readouts.
6. **should fix** (general). The Manual's 29 source links have no `target="_blank"`. On the site a student who taps
   "USGS record" navigates the tool's own frame away and loses the instrument state. Seen: grep (0 of 29 links have
   a target). Better: `target="_blank" rel="noopener"`.
7. **polish** (family:curiosity). The drum seismograph is hidden below 1050 px wide (CSS lines 280 and 380), so it
   is gone at 1000x625, 800x500, 680x425, 760x900 and 375x812. The spec keeps it at 375 under the bottom sheet, and
   the drum is part of the station grammar. Seen: every audit size frame under 1050 wide. Better: a slim 40 to 50 px
   drum row in compact layouts.
8. **polish** (general). src.html:1495. The relief texture uses `LINEAR` minification with no mipmaps, so the
   2048x1024 image speckles and shimmers when minified at 1x: the Tibetan Plateau and Andes show as white grain,
   worst near the limb. Seen: `zoom-tibet.png` (from `f1/c-default`); at 3x (`f1/c-asia-zoom`) it is clean. Better:
   `generateMipmap` with `LINEAR_MIPMAP_LINEAR` (the texture is power-of-two).
9. **polish** (family:curiosity). The spec's instrument controls are flattened to plain range sliders: the time
   dial, the speed knob with detents and the two-handle depth fader (shipped as two separate sliders). They work and
   announce their values, but they read as a web form, not station hardware. Seen: every size frame. Better: at
   least the speed knob with its four detents and a joined two-handle depth fader.
10. **polish** (general, kit). The kit writes "✨ Motion" / "⏸ Motion" on the power panel (kit/curio.js:15). An
    emoji on a station toggle breaks the instrument grammar, and the Sound and Read beside it have no icon. Seen:
    every frame. Better: a kit option for a plain label (benefits every Curiosity).
11. **polish** (general). Type is small at the main size, 1366x768: layer button names 10 px, fader readouts 11 px,
    survey labels 10 px, Read 11 px next to Manual 13 px. Seen: computed styles in `f1/c-default`. Better: 12 to 13
    px for anything a grade 4 student reads while using a control, with Read matching Manual.
12. **polish** (family:curiosity). Stations readouts before the markers are set. Circles with both markers still at
    0 reads "DIST 0 km" and draws zero-radius circles. Reveal reads "FIT AMBIGUOUS". At under 200 km the globe label
    becomes "CATALOG / FIT", a threshold verdict that sits close to the "never a rating" rule (spec Done when 10).
    Seen: `audit-r1/state-stations-1366x768.png`, src.html:930 and 1846. Better: "SET P AND S" until both markers
    have moved, and label the marker plainly ("CATALOG") with the offset in km beside it.
13. **polish** (general). The Wave cutaway is about 140 px across in its panel at 1366x768, small for the
    instrument's main picture. Its MANTLE and LIQUID OUTER CORE labels sit in the corners, pointing at nothing. Seen:
    `f1/t-wave.png`. Better: let the cutaway fill the panel height and put the labels on the layers.
14. **nit**. In Rewind the survey strip reads "QUAKES HELD", and the depth legend stays on screen with no quakes
    drawn. Seen: `f1/t-rewind.png`. Better: "QUAKES OFF" or hide the pair, and hide the legend.
15. **nit**. The P and S labels overlap at 0 on the trace and draw one "8"-like glyph (`zoom-trace.png`). At 680x425
    the trace axis prints "20 25 min" as "2025 min" (`audit-r1/state-stations-680x425.png`).
16. **nit**. The station marker sliders run 0 to 1500 s at 0.5 s with no Shift jump, unlike every other fader.
    Arrow keys alone need about 1,000 presses to reach a 9-minute P arrival (PageUp works).
17. **nit**. At 680x425 the layer buttons show only Q, V, P, F, A. "F" for relief and "P" for edges are cryptic
    without the full names (the aria-labels are fine). Seen: `audit-r1/size-680x425.png`.

## Access walk

- Tab order (1366x768, `f1/k-tabwalk`): globe, five tool tabs, Play, Year, Speed, Magnitude, Depth min, Depth max,
  catalogue select, five layers, zoom out, zoom in, Manual, Motion, Sound, Read, then back to the globe. Every stop
  has a visible 3 px outline, and every target is at least 44x44.
- Globe keys work (`f1/k-globe-keys`): Right, Shift+Up, = = and Enter select the nearest filtered quake and announce
  it in the live region. Magnitude: Down stops at 5.5, Shift+Up adds 0.5. Speed and Ma set `aria-valuetext`.
- The Manual is a modal `<dialog>`: it traps focus, and Close returns focus to Manual. Close on a tool returns focus
  to its tab.

## Standard voice check

The tool has one fixed line (`voice/lines.json` and `allLines()` match word for word). Read speaks a live
`readState()` text.

| line | kind | expected | spoken |
|---|---|---|---|
| Drag to spin. Press play. | how | once per load | once (5 held Play clicks 2.5 s apart: 1) |
| Read (state text) | read | every press | every press; it cut the how line (`cut: read`) and was heard whole |

- First tap: a plain Play tap, a drag or a tool tab gets the how line at once, but it is stale (finding 1). Sound
  first: nothing spoken (correct). Read first: the state text only (audit row 17). There is no welcome by design.
- Two quick taps on a tool tab: `setTool` hushes the how line and it is never heard whole (audit). Acceptable once
  finding 1 is fixed, since the line is stale there anyway.
- Order: no line plays after a newer action in any run.

## Audit pilot

- **Confirmed:** the record card over the globe in the Stations state (finding 4). The quick-tap hush of the how
  line (voice table). The Stations trace and marker area at 680x425 (finding 15's axis labels).
- **Wrong:** about 470 "#globe overlaps X" rows. The globe canvas is a full-bleed stage by design, and the legend,
  hint, position and toolbelt are meant to float over it. Every "hint out of view" row: the hint is meant to go
  after the first action. Manual "keep region" and "hidden under manual-drawer" rows: the Manual is a modal dialog
  by design. The marker-slider overlap rows ("P 0.0 s" under `#marker-p`): the label wraps its slider and reads
  cleanly on the frames.
- **Missed:** findings 1 (stale first line), 2 (shortcut keys dead after a button click), 3 (volcano layer frame
  cost), 5 (unlabeled depth readouts in compact layouts), 6 (links navigate away), 7 (drum hidden), 8 (texture
  speckle), 12 (readouts before markers are set) and 13 (Wave cutaway size).

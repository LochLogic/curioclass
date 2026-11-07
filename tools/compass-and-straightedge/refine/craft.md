# Craft lens: compass-and-straightedge (Curiosity No. 09), round 1

Cold Craft lens, 2026-11-06. Judged against CODEX-CURIOSITY.md, VISION.md "Curiosities: the second shape", STANDARDS,
BASELINE and the spec. Bundle `tools/compass-and-straightedge/compass-and-straightedge.html` as built (not re-bundled).
My frames: `S:/CurioClass-codex-scratch/compass-and-straightedge/craft/out/`. Shared audit:
`S:/CurioClass-codex-scratch/compass-and-straightedge/audit-r1/`.

Counts: blocker 1, should fix 5, polish 6, nit 5.

## Contract (clean)

- One file, 90,431 bytes bundled (goal 2 MB): clean.
- No network requests: `performance.getEntriesByType('resource')` empty after load and a drag (c1-first-drag). The
  Manual's source links are plain anchors, fetched only if clicked.
- No console errors or exceptions in any of my runs or the audit's (the one exception in my log came from my own
  synthetic KeyboardEvent dispatched on `document`, not from the tool).
- Kit used for voice, tones, Motion and Sound (`Curio.voice`, `Curio.tone`, `Curio.init`); no kit header or lesson frame.
- `scripts/check_tools.py`: listed as `draft compass-and-straightedge`, no failure.
- Words: no em dashes in src.html, lines.json, notes.md; "Curio Class" only; privacy stated in the Paper cabinet and
  Manual ("Saves stay on this device. Nothing leaves the device."). Classroom-safe.
- Lines: all 14 `L` entries match `voice/lines.json` word for word (scripted diff).
- Art: no raster art, `art/prompts.json` has no assets, no people. Nothing to check.
- Lesson creep: no score, goal, level, sticker, finish screen or kit header.
- Look rules: the paper fills the screen; readouts and counts in monospace with units (AB, u, degrees); Manual handle
  and engraved plate lower-left with the middle dot; Motion, Sound and Read on their own lamp plate; toggles carry
  `aria-pressed`; controls 44 to 56 px. Exceptions below.

## Findings

### Blocker

1. **Tangent circles and tangent lines make phantom duplicate points.** `src.html:413-420` (circle-circle) and
   `:406-411` (line-circle). When two circles just touch, `h2` comes out a tiny positive number from rounding and
   `h = sqrt(h2)` is about 1.5e-8, larger than the 1e-9 merge distance, so one touching point becomes two points.
   How I saw it: the spec's own hexagon walk (Things to do 5, Done when 3) on the Given circle sheet. Opposite rim
   circles (centres E and C) touch at the centre A, and the sheet grows points M and N at 1.49e-8 from A, both labelled
   beside A with leader lines; the counts read "15 points" where 13 exist (`out/h1-hexagon.png`, numbers from
   `out/h2-hexagon-phantoms` js: `{"n":"M","d":1.49e-8,"parents":["E","C"]}`). Arrow keys cycle through them, they can
   anchor new circles (which then spawn more near-duplicates), and the Manual's honesty note says tangencies are
   handled ("Tangencies use a small relative numerical tolerance"), so the readout lies on the flagship construction.
   Better: treat `h` (and `dt`) below a relative tolerance of the radius, around 1e-7, as one touching point, or merge
   new crossings with a tolerance scaled to the radii. Tag family:curiosity.

### Should fix

2. **Undo also rewinds the instrument settings and the view.** `src.html:363-366`: `checkpoint()` clones the whole
   `state`, so Undo restores `tool`, `euclid`, `extend`, `hold`, `view` and the Book ghosts along with the drawing.
   Check (`u1-undo-scope`): draw a circle, pick Edge, switch on Euclid's rule and Extend, pan; Ctrl+Z gives back
   `tool:"compass", euclid:false, extend:false` and the view jumps back 0.7 units. A student working under Euclid's rule
   (Done when 5) silently loses it on the first Undo. Better: history holds points, objects, log, serial and names
   only. Tag general.

3. **The record and announcements use internal ids.** `src.html:477` "Erased p6; dependent objects removed.",
   `:485` "Inked line o7.", `:866` `[`/`]` announce "circle o3. radius 1.0000 AB", `:493` tool switch announces
   "line. Arrows choose..." and "erase. ...". Seen in the log card (`out/c3-erase-ink-log.png`: rows 5 and 6) and the
   status region (`k3-brackets`, `k2-words`). The log is meant to read "in Euclid's style" and Read speaks its last row.
   Better: "Erased circle with centre A through B.", "Inked line CA.", "Straightedge." Tag general.

4. **The readout live region re-announces on every pointer move.** `src.html:168` makes `#readout` `aria-live=polite`
   and `render()` rewrites its text on every call (`:736`), including each `pointermove` while panning (`:819`). Check
   (`p1-pan-triangle-live`): with the I.1 triangle readout showing, a 30-step pan caused 32 mutations of the live region,
   so a screen reader repeats "AB 1.0000 AC 1.0000..." through the whole drag. Better: only write when the text changes,
   or drop `aria-live` from `#readout` and keep the one `#status` announcement per move. Tag general.

5. **Frame time falls under 60 fps at moderate density.** `render()` (`:641`) rebuilds the whole SVG and re-places every
   point label on each `pointermove` (`:819`), not once per animation frame. Measured on Cory's desktop (fast CPU,
   headless): 60 objects and 757 crossings, render median 12.9 ms, max 19.8 ms; during a 60-step pan, 61 of 181 frames
   over 20 ms, p95 31.9 ms, max 40 ms (`out/p2-dense.png`). A school Chromebook is several times slower, so a month-of-use
   sheet (a Book pentagon is about 30 to 40 objects) will stutter well below the 60 fps rule. Small sheets are fine (the
   hexagon, 13 objects: 0.5 ms). Better: coalesce pointer renders with the existing `requestRender()`, and skip labels
   for points off screen or below a zoom where they would collide. Tag family:curiosity.

6. **Book ghost steps do not sit on the student's points.** `src.html:964` puts the Book's A and B at (-0.5, 0) and
   (0.5, 0); the sheet's A and B are at (0, 0) and (1, 0), and `:1105-1106` pushes the ghost unchanged. Frame
   `out/g1-ghosts-on-paper.png`: after "Show next step" twice on I.1, the ghost circles are centred half a unit left of
   A and on the midpoint of AB, while the step text says "Set the compass at A through B." A reference laid "on the
   paper" that misses the paper's own A and B reads as wrong. Better: map Book coordinates so its A and B land on the
   sheet's A and B when they exist (or draw the ghosts well clear of the drawing, as the code comment intended).
   Tag family:curiosity.

### Polish

7. **A selected stroke is hard to see.** `src.html:653` adds 0.7 px to the width (1.2 to 1.9 px pencil). In
   `out/c4-select-weight.png` the selected CA is barely distinguishable from DB; only the readout tag tells you which
   one is selected. Better: a soft red halo or the crossing red at 2.5 px while selected. Tag general.
8. **Undo and redo glyphs are tiny.** `src.html:191-192` with `.bench button` at 12px system-ui: the arrows render about
   8 px in a 48 px button (`audit-r1/size-1366x768.png`, `size-680x425.png`). Better: draw them as 22 px SVG icons like
   the toolbelt. Tag general.
9. **The readout tag covers point labels on a phone.** `src.html:750-755` keeps the tag inside the edges but not off
   labels: at 375x812 "radius 1.0000 AB" sits on B's label (`audit-r1/state-circles-375x812.png`). Tag general.
10. **The Manual opens as a centred modal, not a lower-left drawer.** `src.html:65-66, 202`. Span and Spire's Manual is
    a drawer anchored at the lower-left handle (`span-and-spire/src.html:151`); here the same handle opens a 740 px
    centred dialog (`audit-r1/state-manual-1366x768.png`). Better: anchor it at the handle like the family mark.
    Tag family:curiosity.
11. **Strokes have an 18 px tap band.** `src.html:778` `min=9` px. Selecting, inking, erasing or measuring a 1.2 px
    pencil line by touch (the 375 toolbelt layout) needs a tap within 9 px. Points already get 44 px. Better: 22 px on
    coarse pointers. Tag general.
12. **Every crossing gets a letter label.** `src.html:695-702`. At density the sheet turns into a block of overlapping
    two- and three-letter names (`out/p2-dense.png`). Better: label given, free and chosen points always, crossings on
    hover, choice or above a zoom threshold. Tag family:curiosity.

### Nit

13. The keyboard cursor ring (`:703-707`) shows for mouse users: any click focuses the sheet (`:796`), so a dashed red
    ring sits on A after a drag or after "Back to paper" (`out/c2-triangle.png`, `out/g1-ghosts-on-paper.png`). It looks
    like A is chosen. Show it only after a key press. Tag general.
14. Visible "Edge" and "Erase" vs accessible names "Straightedge, S" and "Eraser, E" (`:174, :176`): voice-control users
    saying "click Edge" may miss. Tag general.
15. At 375 wide the idle compass drawing (`:718`, at 44,65) lies over the zoom tag "AB = 1 unit · 62%"
    (`audit-r1/size-375x812 (iframe host).png`). Tag family:curiosity.
16. The resting straightedge (`:720-724`) is drawn above the construction and covers the lower circles near D at
    1366x768 (`out/c2-triangle.png`). Draw it under the strokes or let it slide aside. Tag family:curiosity.
17. Each move clones the whole state into history (`:363`) with no cap; a 600-object sheet with thousands of crossings
    keeps hundreds of full copies. Fine for now; worth a cap or diff history if finding 5 is reworked. Tag general.

## Access (clean rows)

- Keyboard: Tab lands on the paper first; arrows move the point cursor, Enter, Enter draws (`k1-keyboard-circle`: log
  "Circle with centre B through A.", status announces it with the radius; `k1b`: "B. Choose the second point.").
  O, crosshair and Enter place a free point; `[` `]` select strokes; Escape cancels; Ctrl+Z/Y. Focus visible (3 px red
  outline). Audit: Enter twice after each click keeps focus, nothing disabled after resize.
- Color is not the only signal: chosen points get a ring, crossings are red dots plus labels.
- Motion off: circles appear at once; audit "nothing runs forever" clean.

## Standard voice check

A Curiosity: one first-run hint, then Read only. No how-to or event line is spoken on its own, and none should be.

| line | kind | expected | spoken |
|---|---|---|---|
| "Drag from A to B." (hint) | how-to, first run | once on the first plain tap | once (`v2`: sheet, compass, edge, compass, sheet, 2.2 s apart: one entry) |
| hint on first tap of Edge, Point, Erase, Measure, Paper, Book, Manual | how-to | not required (BASELINE 16) | not spoken; reachable by Read (the hint for that tool) |
| hint on a first real drag A to B | how-to | not required | not spoken; the student already did it |
| Read, five presses 2.5 s apart | read | five | five (`v1`) |
| Read with Sound off | read | speaks | speaks (`v3`) |
| Read on Blank sheet | read | blank-paper hint | "Blank paper. Choose Point to place free points..." (`v4`) |

Stale lines and order: nothing queues behind an action (opening a drawer, changing a Book page or a sheet hushes);
audit's five clicks and two quick taps clean on every control that spoke. Read joins the hint, the last log row and the
readout, so it never matches a recording and always uses browser speech; this is the spec's stated fallback, but it
will speak finding 3's "o7" ids aloud.

## Not checked

Print output (no print emulation in drive.py); the CSS (`:150-161`) hides the instruments and ghosts and prints the
log in three columns, which reads right.

## Audit pilot

**Why 368 leads.** Almost all are two quirks of this layout, not defects:
- 210 rows: `#sheet` is a focusable full-bleed `role=application` SVG under every control, so the audit reports an
  overlap between it and each of the ~25 floating controls at each of 8 sizes. The Curiosity look ("the object fills
  the screen") makes this the intended layout.
- 147 rows: the Book, Manual and Paper cabinet are `showModal()` dialogs, which make the page behind them inert; the
  audit reports every covered control as "text hidden under another box" per size and state.
- The remaining handful: "hint out of view" in the circles, blank-paper and infinite-line states (the first-run hint
  is meant to vanish after the first action), "choices cut short" in the Manual (its source links sit in a scrolling
  text, as they should), and "welcome not heard" after a first tap on a non-compass control (by design: the hint is
  compass-specific, BASELINE 16, and Read reaches each tool's hint).
- Audit fix to suggest: skip overlap rows with an element whose box equals the stage, and skip controls under an open
  modal `dialog`.

**Leads confirmed:** none as defects. **Leads wrong:** all of the above, for the reasons given. Its clean rows (no
console errors, Motion off, resize mid-action, five clicks and quick taps) held in my runs.

**What it missed:** the phantom tangency points (1), Undo rewinding settings and view (2), internal ids in the log
and announcements (3), the live region firing on every pointer move (4), frame time at density (5), the misplaced Book
ghosts (6), the faint selection, tiny undo glyphs, the readout over a label at 375 and label clutter (7 to 12).

No cultural, Native or hard-history content; no sensitivity review needed from this lens.

# Craft lens: cipher-vault (Cipher Workbench, Curiosity No. 11), round 1

Cold lens, 2026-11-06. Judged against CODEX-CURIOSITY.md and VISION "Curiosities: the second shape", plus STANDARDS and
BASELINE. Bundle `tools/cipher-vault/cipher-vault.html` as built (not re-bundled). Own probes: CDP scripts in
`S:/CurioClass-codex-scratch/cipher-vault/craft/` (`probe.py`, `run2.py` to `run4.py`), Chrome on port 9431, muted,
closed after. Frames cited are in that folder or in the shared audit folder `audit-r1/`.

Counts: blocker 0, should fix 7, polish 4, nit 2.

## Should fix

1. **Square tableau is rebuilt on every update, and misses 60 fps at 4x.** `src.html:943-967` (`renderTableau`)
   rewrites 729 SVG `<text>` nodes and forces two scroll layouts on every `update()`. With a 600-letter tape and three
   tools open, one `update()` costs 5 ms at 1x and 31 ms at 4x CPU slowdown (every other machine is under 1 ms at 4x).
   One key change per frame at 4x ran at a median 50 ms frame (20 fps, 59 of 59 frames over 20 ms); a single keystroke
   in the tape takes 40 ms to reach the screen at 4x. Done when 7 fails for this machine. Better: draw the 26 by 26
   letters once and move only the three highlight rects and the chosen-letter fill. Check: `perf` and `perf2` probes
   (probe-results in the craft scratch). Tag: general.

2. **The first-run hint is spoken after its moment has passed.** `src.html:1636-1637` (`welcome` fires on any first
   tap while the Wheel is up) with `setShift` clearing `#hint` (`src.html:911`). A student whose first action is
   dragging the ring, or pressing Right on the focused wheel, sees the hint vanish and the ring move, then hears "Drag
   the inner ring." (vlog: spoken at 1325 ms after three Right presses that already read THE DIE IS CAST; spoken at
   2396 ms after a real drag). STANDARDS: a line whose moment has passed is dropped, and the spoken line matches the
   screen. Better: `valid` = the hint is still showing. Frame: `craft/wheel-dragged-cw.png` (hint already gone).
   Tag: family:curiosity.

3. **Read never speaks the first-run hint.** `src.html:1627-1633` (`readText`) and `hint:false` on `Curio.voice`.
   On a fresh page Read says "Wheel. Decode. SHIFT 00 · A to A. Output: WKH GLH LV FDVW. LETTERS 12 · Too few letters
   to read the bars." and never "Drag the inner ring." CODEX-CURIOSITY: the hint is spoken once, "then only when Read
   is pressed". A student who cannot read the brass, and whose first tap was Read or a non-wheel control, has no way to
   hear what to do. Better: while `#hint` has text, Read speaks it first, then the readout summary. Check: audit
   one-click row 4 and `voice_soundoff_read` probe. Tag: family:curiosity.

4. **The hint text runs over the inner ring letters at the preview sizes.** `src.html:415` (`#hint { font-size:30px }`
   inside the compact media query). At 680x425, 800x500 and 1000x625 "Drag the inner ring." is wider than the hub and
   sits on top of the inner ring's D and J. Better: keep it inside the hub (smaller size, or two lines). Frames:
   `audit-r1/size-680x425.png`, `audit-r1/size-1000x625.png`, zoom `craft/zoom-hint-680.png`. Tag: general.

5. **Two readouts disagree on Grid and Symbols.** `src.html:1069` (`renderCounter`). On Grid or Symbols the Counter
   counts glyphs only, so with the default letter tape it reads "LETTERS 0 · Too few letters to read the bars." with a
   1 to 26 axis, while the input tape beside it reads "12 LETTERS". A readout must say what it counted: "SYMBOLS 0"
   (and say the tape holds letters, not symbols), or count what the tape holds. Frames:
   `audit-r1/state-grid-1366x768.png`, `audit-r1/state-symbols-680x425.png`. Tag: family:curiosity.

6. **The rotor keyboard and lampboard are below the fold at 680x425 and 375x812.** Mode Rotors. Only a sliver of the
   lamp row shows; the 26 typing keys (Things to do 8, "type on the rotor machine") need a scroll inside the machine.
   STANDARDS: the main controls are visible without scrolling at every size. Better: in short boxes put the keyboard
   first and fold the ring fields and order selects behind the window row. Frames: `audit-r1/state-rotors-680x425.png`,
   `audit-r1/state-rotors-375x812.png`. Tag: general.

7. **Splitter gives a key guess with no small-sample guard.** `src.html:1083-1087`. With the 12-letter default tape the
   Splitter at length 5 shows "BUMPINESS 0.0 AT LENGTH 5" and "KEY GUESS DSDND" with a `Use key` button, from 2 or 3
   letters per column, while the Counter beside it says "Too few letters". The seal card already knows the threshold
   ("Too few letters per column for reliable counting", `src.html:1387`). Better: the same note on the Splitter under
   10 letters per column, and no `Use key` offer there. Frame: `audit-r1/state-three-tools-1366x768.png`,
   `craft/manual-1366.png` (behind the drawer). Tag: family:curiosity. Teaching lens may rate this a blocker under the
   "readout that misleads" rule; from Craft it is at least should fix.

## Polish

8. **Analyzer panel's sticky header lets scrolled content show around it.** `.analysis-top` in the tool panel. With
   several tools open, the BUMPINESS line is cut under the "Tools read" bar and the edges of scrolled-away controls
   peek out above it at the panel's top edge (the audit's overlap rows on three-tools and weather-search). Better: an
   opaque header pinned at `top:0` with the panel's padding inside it. Frames: `audit-r1/state-three-tools-1366x768.png`,
   `audit-r1/state-weather-search-1366x768.png`, zoom `craft/zoom-three-tools-head.png`. Tag: general.

9. **Event messages live in small muted type on the plate, far from the action.** `#status` in the plate
   (`src.html:607`) carries "One setting left · tap it, then Run tape", "600 letters is the limit" and the seal and box
   messages at about 10 to 11 px in the lower-left corner, while the bombe and tape are top and right. A student running
   the bombe will not look there. Better: show the event beside its instrument (the bombe readout, the input tape
   count) and keep the plate for "Stays on this device". Frame: `audit-r1/state-weather-search-1366x768.png`.
   Tag: family:curiosity.

10. **Range controls announce bare numbers.** The English ghost slider (`#ghost`) and the column ghost sliders announce
    0 to 25, not a letter or shift, while the brass wheel announces "Shift 3, A to D". Better: `aria-valuetext` such as
    "Ghost shift 3, A to D" and "Column 2 key S". Check: focus walk (`walk_wheel`, `three-tools`). Tag: general.

11. **Rotor ring fields are bare inputs reading "1".** The ring settings show as large empty dark boxes with a single
    digit, unlike the spec's "rings 01 to 26" readout and the engraved look of the window row. Better: a two-digit
    monospace dial (01 to 26) with Up / Down like the windows. Frame: `audit-r1/state-rotors-680x425.png`,
    `audit-r1/state-weather-search-1366x768.png`. Tag: family:curiosity.

## Nit

12. **Spec and build disagree on voice lines.** spec.md "Voice" lists four event lines ("One setting left. Tap it, then
    Run." and three more); `voice/lines.json` has only the hint and notes the omission under CODEX-CURIOSITY.md, which
    does say voice speaks the hint and then only Read. The build follows the brief; the spec line should be updated so
    the next round does not re-flag it. `voice/lines.json` matches `allLines()` word for word. Tag: family:curiosity.

13. **The plate wraps to two lines at 680x425** ("Cipher" / "Workbench" with the screw heads crowding). Frame:
    `audit-r1/size-680x425.png`. Tag: family:curiosity.

## Checked and clean

- Contract: one file, 152 KB bundle (no images, fonts or audio); no network requests in any probe (CDP Network log,
  every machine, bombe, drawers); no console errors or exceptions in any probe; kit used for voice, Motion and Sound
  (`Curio.voice`, `Curio.onMotion`), no kit header or lesson frame. Manual source links are ordinary outbound links, not
  requests.
- Engine: AAAAA to BDZGO at I II III, B, AAA; double step ADU to ADV, AEW, BFX; bombe 17,576 settings in 77 ms, all six
  orders 105,456 in 406 ms (1,349 ms at 4x), one survivor I II III B O X. Wheel, Grid, Symbols, Rotors and Pad
  `update()` under 1 ms at 4x with 600 letters and three tools.
- 600-letter limit: "600 LETTERS · LIMIT" and "600 letters is the limit". Storage blocked: "Storage blocked · plays
  without saving", tool plays.
- Access: Tab reaches every control on all six machines (focus walks `walk_*`), amber 3 px focus ring on every stop;
  the wheel is a `slider` with "Shift 0, A to A"; rotor windows are spinbuttons; pigpen, symbol and plugboard keys are
  labelled buttons. No target under 44 px at 1366x768, 1000x625 or 680x425 on any machine. Keys 1 to 6, C, S, R, K, B,
  O, M work with no field focused; Escape closes every drawer and focus returns to the opener (Case file, Boxes,
  Manual, Fan, Seal). Wheel drag direction matches the ring's turn (`craft/wheel-dragged-cw.png`).
- Look rules: the bench fills the screen, no header bar or pill panel; readouts are monospace with units (all
  `*-readout`, tapes, windows); Manual and plate lower-left; Motion, Sound and Read on their own panel top-right (as the
  spec places it), with `aria-pressed`. Motion off: audit clean; Fan lists all 26 shifts at once in calm.
- Words: no em dashes in src, bundle, notes or tool.draft.json; "Curio Class" never "Curio" alone; classroom-safe;
  privacy stated on the plate ("Stays on this device") and in notes. Lesson creep search (score, points, level, goal,
  sticker, badge, correct, wrong, try again, complete, well done): only CSS `pointer` and "point" in prose.
- Art: `art/prompts.json` has no assets and no `art:` tokens are used; everything is drawn in code, as the brief allows.

## Voice check

Sound on, Motion on, held clicks (120 ms), fresh page per run.

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| "Drag the inner ring." | how-to (first-run hint) | once per load, only while the hint shows | once across 5 Increase shift + 5 Counter taps; but also after the hint was already gone (finding 2) |
| Read (machine, setting, output, tool readouts) | read | every press, Sound off too | every press, Sound off too; never includes the hint (finding 3) |

- Repeats: the hint line never repeats; Read speaks each press. No event lines exist (nit 12).
- Stale: Increase shift then Grid 0.2 s later: the hint started at the first tap, nothing queued after. After a drag or
  arrow-key first move, the hint plays with the hint gone (finding 2).
- First tap: Grid or Symbols first: nothing (the hint is the Wheel's only); Sound first: nothing; Read first: the
  readout summary only; a wheel control first: the hint at once.
- Read cut: Read 0.25 s into the hint stops it and speaks; a following tap and machine change start cleanly.
- Order: no line out of order (there is one line).

## Audit pilot

- **Leads confirmed:** `#hint` under the ring at 680x425, 800x500, 1000x625 (finding 4); rotor keyboard cut by the
  machine's scroll at 680x425 and 375x812 (finding 6); the three-tools and weather-search overlaps are the sticky tool
  header over scrolled content (finding 8, real but polish).
- **Leads wrong or noise:** the ring letters "under circle" (SVG letters drawn on brass discs); "hint out of view" on
  every non-Wheel state (the hint belongs to the brass wheel, which is hidden there); "welcome not heard" after a first
  tap on Case file, Boxes, the machine buttons, Fan, Seal, Manual (a Curiosity has no welcome; the hint lives on the
  brass); the Manual keep-region rows (a modal drawer); the symbol card and letter strip "cut sideways" at 680x425 and
  375x812 and the column sliders below the scroll at 375x812 (deliberate scroll strips, every item reachable).
- **Missed by the audit:** the Square's 31 ms update at 4x (finding 1); the hint spoken after its moment (2); Read not
  speaking the hint (3); Counter "LETTERS 0" against the tape's 12 LETTERS on Grid and Symbols (5); the Splitter key
  guess from 2 or 3 letters per column (7); event messages parked on the plate (9); range values announced as bare
  numbers (10).

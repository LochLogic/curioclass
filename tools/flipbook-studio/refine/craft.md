# Craft lens: flipbook-studio (round 1)

Cold Craft lens, 2026-11-05. Bundle `tools/flipbook-studio/flipbook-studio.html` as built (not re-bundled).
Shared audit: `S:/CurioClass-codex-scratch/flipbook-studio/audit-r1/audit.md`. My frames and logs:
`S:/CurioClass-codex-scratch/flipbook-studio/craft/frames/` (shot files `shotsA..F.json` beside them).
Not a Curiosity (no "(Curiosity No." line), so judged against lesson norms.

## Contract: passes

- One file, 227,031 bytes (goal 2 MB). Only embedded data: two `data:image/webp` (fb-desk, fb-paper). No `http`
  URL in the bundle except the SVG namespace; no fetch, XHR, WebSocket or import.
- No network requests: `performance.getEntriesByType('resource')` is empty after load (a-default-1366).
- No console errors or exceptions in any of my 25 shots or in the audit.
- Kit used, not re-implemented: `Curio.voice`, `Curio.tone`, `Curio.init`, `Curio.onMotion`, `Curio.reduce`, kit header.
- Play clock: 24 fps on Real bounce for 5.3 s (127 drawings shown, over 10 loops): worst drift 9.7 ms, last -1.0 ms,
  well inside one frame (41.7 ms). rAF frame times median 16.7, p95 16.7, max 16.8 ms (c3-clock24). Done when 5 holds.

## Access: passes, with one contrast miss

- Every visible control is at least 44 x 44 px at 1366x768 and at 375 wide (a-default-1366, a-default-375x).
- Tab reaches header, then every panel control, then the strip (panel before the long list, as STANDARDS asks). Every
  stop shows a 4 px solid outline (gold in the header, #a52a13 in the panel) (c5-keys).
- Color is never the only signal: onion before is solid, after is dashed; holds show "x3" as text; selected
  thumbnail has a border and `aria-current`; mode and toggle buttons use `aria-pressed`.
- Motion off and Sound: the audit's Motion-off row is clean; the curl and paper-settle check `Curio.reduce`.
- Read: speaks the hint, cuts a playing line, works with Sound off; Sound back on brings the skipped welcome once
  (b8-read-during, b9-read-soundoff).

## Lines and art: pass

- `voice/lines.json` (12 lines) and `allLines()` (12) match word for word both ways (a-default-1366 check).
- Art tokens `art:fb-desk` and `art:fb-paper` both have prompts.json entries, `people: false`; no people drawn.
- Words: no em dashes in src, bundle, notes, spec or lines; "Curio Class" never "Curio" alone; classroom safe;
  privacy stated on screen twice ("Saved on this device. Your drawings never leave it." and the footer).

## Standard voice check

Held clicks (0.12 s), Sound on, Motion on, gaps 2 to 3 s; headless Chrome has no system voice, so line lengths are
the kit's cap and some "cut" marks are only the next action arriving (not a finding).

| line | kind | expected in 5 actions | spoken | run |
|---|---|---|---|---|
| welcomeDraw | how | 1 | 1 | b4-modes (5 Draw entries) |
| welcomeTime | how | 1 | 1 | b4-modes |
| welcomeFlip | how | 1 | 1 | b4-modes |
| spacingHow | how | 1 | 1 (then silent x3) | b4-modes |
| onionHow | how | 1 in five pages drawn | 1 (then silent x4) | b1-five-pages (Done when 11) |
| eraserHow | how | 1 | 1 (then silent/dropped) | b5-eraser |
| starterBounce | event | 4 of 4 loads | 4 | c1-starters |
| starterBlink | event | 1 | 1 | c1-starters |
| holdChanged | event | 5 while playing | 5 | b2-hold-playing (Done when 11) |
| printed | event | 1 | **0 (dropped, hush)** | b7-print |
| tooBig | event | once per failure, but see finding 2 | 5 in 5 actions | f1-toobig |

Stale lines (c2-stale, 10 actions 0.6 s apart through Starters, Time, Play, hold +, Flip, Stop, Draw, New book):
no line played after its moment; welcomeFlip was dropped as stale while the book played and spoken after Stop; order
followed the actions. Read during welcomeTime cut it and spoke the hint at once. First-tap rows: the audit's table
covers them; I did not re-shoot. welcomeFlipCompact (compact Flip) was not exercised by me.

## Findings

1. **should fix** (general). `src.html:1416-1424` `printBook()`: the `printed` line ("Print the pages, cut on the
   lines and staple the left edge.") can never be heard. `V.say` only queues (the pump starts in a microtask), then
   `window.print()` blocks the thread, and the `finally { finishPrint() }` runs `V.hush()` synchronously when the
   dialog closes, before the queued line can start. Seen: b7-print log `printed dropped hush`. In headless print
   returns at once; in desktop Chrome the order is the same, so the spoken how-to-make-the-paper-book is lost every
   time (the hint still shows it). Better: speak it before opening print (await the line, or `setTimeout` the print
   call after it starts), or speak it after `afterprint` as the next step.
2. **should fix** (general). `src.html:557-564` `save()` catch: when storage is unavailable or full, `tooBig` is
   queued as an event on every change, so each stroke, Copy page or hold change says "This book is too big to save
   here..." again. f1-toobig (setItem throwing, five actions 2.5 s apart): spoken 5 times, twice within 170 ms at one
   point, and the onionHow lesson was pushed out (dropped) both times it came up. It is a standing condition, not a
   new event: say it once per failure run (speak again only after a save has worked and then fails again). Students on
   locked-down school browsers where localStorage throws would hear it on every mark.
3. **should fix** (general). Empty-state line "Draw here, or open a starter book." (`#empty span`, `src.html:91-94`)
   is #84786a on the #fbf6ea page at 12 px: 3.99:1, under AA 4.5:1 (recomputed in Python; the paper texture lowers it
   a little more). Frame a-default-1366. Darken to the spec's muted #6b6258 (5.54:1).
4. **polish** (family:drawing). Pencil colors collide with the tool's own overlays: `Blue pencil` is #2f6fd6, exactly
   the onion "before" ghost color, and `Red` is #c8341a, exactly the spacing chart's dots and line. Frames
   e1-blue-pencil-onion (a full-strength blue stroke beside 35% blue ghosts reads as one more ghost) and
   e2-red-pencil-chart (a red stroke on drawing 1 sits in the chart's color). Better: shift Blue pencil to a cyan or
   indigo distinct from the ghost, and draw the chart in a color no pencil uses (or outline its dots).
5. **polish** (general). Heavy books get slow: `changed()` calls `render()`, which repaints all 48 thumbnails, and
   `save()` writes the whole book on every stroke end, hold step and reorder. With the spec's limits (48 drawings,
   a 400-stroke page plus 120 strokes on the others) one full render took 67 ms, a reorder 109 ms, and the save was
   3.86 million characters, near Chrome's ~5 MB localStorage quota (d1-heavy, on this fast desktop; a modest
   laptop is several times slower, so a hold drag while playing would stutter). Points are saved at full float
   precision (`position()` in `src.html:1305-1308`). Better: repaint only the changed page's thumbnail, round points
   to 0.1 unit, and debounce the save during a drag. Normal classroom books (a dozen pages, a few strokes each) are
   unaffected: playback held 16.7 ms frames.
6. **nit** (general). `src.html:1331-1334`: the eraser pushes an undo step on every press even when it touches no
   stroke, so Undo after a missed erase appears to do nothing.
7. **nit** (family:drawing). `src.html:885`: a tap on the hold track uses `Math.round(x/15)`, so tapping the left
   half of cell 3 sets a hold of 2. `Math.ceil` would match the cell tapped (the handle drag is unaffected).
8. **nit** (general). `src.html:369`: the canvas label says "Use arrow keys to step pages", but the canvas is not
   focusable; the arrows do work from the page, so the words are only slightly off.
9. **nit** (general). Several labels are 10 to 11 px (eyebrows, hold captions, page numbers, footer privacy line,
   strip label); all pass contrast, but 10 px is small for a laptop at arm's length.

Nothing cultural, Native or hard-history: no sensitivity review needed.

Counts: blockers 0, should fix 3, polish 2, nits 4.

## Audit pilot

- Leads confirmed: none of the audit's leads is a real Craft defect.
- Leads wrong: "count and word disagree: 1 seconds" at every size: the readout says "1 drawing, 1 frame, 0.1 seconds
  at 12 per second", which is correct English (the check read "0.1" as "1"). "keep region covered" in
  starter-library and timing-help: those are modal dialogs, covering is expected. "choices cut short by a scroll
  panel" on `#film`: the spec asks for a sideways-scrolling strip and the selected thumbnail is kept in view.
  "Welcome not heard" after New page, Copy page, Delete page, Clear page, Play, Starters, New book: these follow the
  spec's stale rules for welcomeDraw (a page button counts as starting) and the welcome returns after Stop or a closed
  dialog; whether the premise should still be spoken is the Play lens's call, not a voice bug.
- What it missed: the `printed` line that can never play (finding 1), `tooBig` repeating on every action (2), the
  empty-state contrast (3), pencil colors that match the onion and chart colors (4), and cost on a large book (5).

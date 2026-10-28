# Handoff: snowy-mail-route (build, 2026-10-28)

## What was built

- `src.html`: Snow Town (free play, six houses, the address glows) and Mail Route (8 levels, 5 build and 3 fix-it,
  as in the spec's table). Pip walks the arrow cards on a 6x4 snow grid, leaves a numbered footprint pair per card,
  bumps snowbanks and the town edge with a flump and a snow puff, shrugs on a wrong stop, and delivers with an open
  door, a flying letter and hearts. Guess flag (toggle), Go / Stop, Step (then Go walks the rest), Slow / Quick,
  Clear, Start over, Next, level dots. Footprint taps pick their card; a picked card pulses its footprints.
- `kit/robot.js` (new, the family engine) and `docs/families/robot.md` (its API and sibling rules).
- `tool.draft.json`, `notes.md`, `voice/lines.json` (40 lines, gentle-storyteller / Vindemiatrix),
  `art/prompts.json` (none: drawn in code), `preview.svg` (Pip mid-route in Snow Town, footprint trail, strip).
- All spec data checked in the page: every level's start cards (fix-its bump at card 5, the edge at card 7, card 2),
  every listed best path and fix delivers (played through the real UI), and all six Snow Town paths deliver.

## Engine API (kit/robot.js, global `Robot`, version 1)

- `Robot.program({max, onEdit})`: `list [{id, op, args}]`, `gen`, `add(op, at, args)`, `replace(i, op, args)`,
  `move(i, d)`, `remove(i)`, `clear()`, `load(list)`, `on(fn)`, `ops()`, `card(i)`, `indexOf(id)`, `length`, `full`.
- `Robot.strip(el, {prog, max, layout, renderCard, cardLabel, onSelect, onMove, onRemove, canEdit, buttons, bounds,
  emptyFocus, names, label, buttonsLabel})`: `select`, `deselect`, `sel`, `setNow`, `setBug`, `pulse`, `lock`,
  `flash`, `flip`, `size({...})`, `place`, `render`, `card(i)`, `cell(i)`.
- `Robot.run(prog, {style: 'sequence'|'rules', beat, exec, onStep, onPause, onEnd, target, same, pause, world,
  when, tick, ticks, snap, traceIdle})`: `go()`, `step()`, `stop()`, `status`, `busy`, `next`, `tick`, `trace`,
  `traceFor(i)`, `result`; `Robot.trace`, `Robot.traceFor(i)` for the last run.
- Checked in Node: target results (wrong), rules style (stop after 3 ticks), step / pause / go, `edited` when the
  program changes mid-run, and a stopped run ignores its late beat.
- No existing kit file was changed. robot-dance and loop-garden were not touched.

## Spec additions (decided in the build)

- How lines added so every waiting moment's hint names the next control (Read speaks the hint):
  hBuild, hFix, hFlag, hGo, hWalk, hPaused, hSel, hHouse, hNext, hAgain (texts in `voice/lines.json`). hFlag, hGo,
  hPaused, hSel and hHouse are spoken once when their moment first comes; the others are hint only or part of a
  level / result sequence. The tool owns `#hint` (`hint: false`), so welcome and event lines never overwrite it.
- Arrow colors darkened so the white glyph passes 4.5:1: Down #1c8247 (4.85:1), Left #bb520e (4.85:1). Up #2563c9
  (5.67) and Right #7a3fc0 (6.36) as planned.
- Footprint card numbers are drawn on a layer above Pip so the number of the square Pip stands on stays readable.
- On a phone (under 560 px) the four arrows sit in one row with Go beside them, so tray, Go and the whole strip fit
  at 375x812 without scrolling.
- The guess flag can go on any square, snowbanks included (a guess there is simply wrong).

## Checked

- Sizes 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812 (host): no target under 44 px
  (map squares 47 px at 680x425, 53 px at 375), tray, Go and the strip on screen, no hint clipping, no horizontal
  scroll. Console clean through all eight levels.
- Voice with held clicks at 2 s: first tap then the welcome; lines that go stale (walking, a newer how) are dropped,
  never played late; the first Go without a flag speaks line 3 and the walk waits for it; level 4 queues line 5.
- Keyboard: tab order is mode, header, tray, Guess, Go, Step, Speed, level controls, cards, houses (Snow Town) or
  squares (while guessing); nothing moves focus on load.

## Known gaps / for Cory

- The Snow Town welcome is dropped (not replayed) if the first tap starts a walk before it is said: it is only valid
  while Pip is idle. It plays the next time the mode is opened.
- Snowbank faces and footprints are small at 680x425 (squares 47 px) but legible; the footprint numbers are 11 px there.
- `voice/` has no recordings yet (run `scripts/voice.py snowy-mail-route`).
- Open question from the spec stays open: keep the title "Snowy Mail Route" (penguin) over "Robot Mouse Mail".

## Refine round 1 (2026-10-28)

All 10 should-fix and 13 polish items from refine.md, plus the cheap nits. One line each:

1. First Go walks at once: Go hushes a queued guess or flag line and walks; no wait, no line names a disabled control
   (voice check: walk starts about 20 ms after the press, Go pressed 2 s into the welcome).
2. How lines are chosen by `V.heard()`, not a problem counter: after a run the hint is the footprint line until heard,
   then Step; the voice check hears it on the first result.
3. Footprints are toe-forward prints (pad plus three toes) turned the way Pip stepped, scaled to the square (about
   0.36 of it), readable on a projector at 1366x768.
4. Pip stands at the right of a square, prints and numbers sit at the left; on a house the prints and number sit low
   left, off the door, so the house symbol stays readable on a wrong-house stop.
5. The level dots are one button between Start over and Next; it opens a picker of eight letter buttons (number,
   house picture, a check when delivered), any level opens, the current one has a gold ring. Escape or a tap outside
   closes it and focus returns to the dots.
6. 680x425: every target is at least 44 px (probe at all seven sizes and 375); the speed button drops its word in the
   compact layout.
7. Line 10 says "Pip can't walk through a snowbank"; spec and lines.json match.
8. Motion off: the flakes stand still (`.calm .flake{animation:none}`).
9. kit/robot.js: under `.calm` the pulse is a still ring and the bug wobble is off.
10. The "?" badge shows only after the class taps a footprint or card, or after the hint has asked twice; rule in
    docs/families/robot.md.
11. After a bump the hint names the last footprint ("The card after it made Pip bump"), or card one when Pip bumped
    before any footprint.
12. "Bug" is said when level 4 opens; "debugging" when a fix-it level is delivered; notes.md says where.
13. notes.md talk question: "We changed one card. What changed for Pip?" (IM-03).
14. Level 8 says "Press Step to walk one arrow at a time."
15. Ending on the Post Office says "Pip walked back to the Post Office! Look at the footprints."
16. Delivery shows a gold ring, the letter flying in and hearts at the door; level 8 adds hearts and stars over every
    house, Pip cheers with an empty bag.
17. A footprint picks its card and the next arrow replaces it; a tap on that picked card keeps it (engine: a card the
    tool picked stays picked on the first tap, the second tap puts it down).
18. The Mail Route welcome says "Look at the letter up in the corner", the envelope in the sky band.
19. Wide layout reserves the hint's two-line height, so the panel does not drop when the hint wraps.
20. Hearts show with Motion off (no animation class, still visible).
21. The caption sits on a dark plate (#141f3c, 94 percent) over the sky at every size.
22. Line 5 says "the buttons under the cards".
23. docs/families/robot.md: run.alive(g), run.gen, canEdit blocking card taps, sequence snap() with no argument,
    strip.locked/el/box/cells, Robot.last and Robot.version, the picking rule and the calm rules.
- Nits: notes.md says "bumps the edge of town at card 7"; levels 6 and 7 have their own fix-it hints; mode buttons are
  not dimmed while Pip walks; a new address clears the guess flag; footprints are in the Tab order once Pip has
  walked; empty-slot numbers darkened to #5f7397 (about 3.6 to 4:1 on the apron).

Checked: all levels and Snow Town (default, wrong house, picker, level 4 bump, level 8 finale) at all seven STANDARDS
sizes, L1-L8 at 1366 and at 680 with Motion off, 375x812 through --host (town, picker, route after a bump, level 1):
no target under 44 px, no horizontal scroll, controls on screen, console clean. Simulation: every level delivers with
its best path, fix-it levels bump where notes.md says. Voice check at a 2 s tap pace with Go pressed during the
welcome: Snow Town, level 4 via the picker (bank, footprint, fix, "fixed the bug") and level 1, no stalls.
voice/lines.json regenerated (47 lines, 12 new or changed; still no recordings). preview.svg regenerated.

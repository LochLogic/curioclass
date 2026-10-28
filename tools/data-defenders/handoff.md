# Data Defenders: build handoff

Grade 5 escape room, the first tool of the security family. Built 2026-10-27 to `spec.md`; Refine round 1 applied
2026-10-28 (see the end of this file). Stage: built (not committed). Bundle:
`CURIO_DRAFT=1 python scripts/bundle_tool.py data-defenders` (about 241 KB).

## What was built

- `kit/security.js` (new): the family engine, global `Sec`. Full API in `docs/families/security.md`.
- `docs/families/security.md` (new): the family doc (engine API, sibling rules, sibling table).
- `tools/data-defenders/`: `src.html`, `tool.draft.json` (stage built), `notes.md`, `voice/lines.json` (59 lines
  from `allLines()`, bank hero-coach, voice Puck; not recorded), `handoff.md`. `art/prompts.json` and
  `art/dd-night-hallway.webp` were already there and are used as is.
- No other kit file was changed. The Network closet reads `kit/network.js` (`Net.graph`, `Net.reach`, `Net.draw`,
  `Net.icon`) as is.

## How src.html is laid out

- Header: title, "Cedar Hollow Elementary", one Escape mode button, Motion, Sound, Read.
- Panel (first in the DOM, for tab order): `#hint`, `#ctl` (the active puzzle's check controls), Clue, the room's
  story card, Team timer (Off / 20 / 30), Start over with a Yes / No confirm, the made-up note.
- Stage: `#hall` (hallway art plus four HTML door buttons laid out in JS at real size) and `#room` (top bar with
  Back, room name and the room lock; tabs; `#stations`). `#escape` is the final card.
- Layout follows collision-lab: `wide`, `compact`, `stack`. In `stack` the hint moves to `#topSlot` and the controls
  to `#ctlDock`, right by the puzzle. Stations are `split` when the room has two puzzles and the stage is at least 880 px
  wide, `tabbed` otherwise (always for the Server Closet's three), `single` in the exit. `.compactui` (compact layout or stage under 560 px) tightens everything and moves the tabs into
  the room's top bar with short names; `.tiny` (stage under 440 px) lets seal-check rows wrap; `.n3` (three puzzles) drops the tab icons and tightens
  the tabs so the short names fit.
- Content tables at the top of the script: `WORLD`, `ROOMS`, `PUZ`, the line table `L` (with two clues per
  puzzle), and each puzzle's data. Every puzzle has a `Sec.lock` in `LK`; `solved(p)` is the one path to success.
- Test hook: `window.__tool = {state, sec, Sec, world, enter, toHall, solve(p, answer), setActive, setTimer, clock,
  locks, cards(), c1Errors, allLines, vlog, vq, restart, relayout, Net, online, parts}`. `solve('a3', {sort, picks})`
  runs both A3 steps.

## Tricky parts

- Voice: `welcomeAfter` with the welcome valid only in the hall before any room is entered (and `hint: false`, so
  it never overwrites a hint), so a first tap on a door goes straight to the room story instead. On entry the hint
  shows the puzzle's action at once; the story is spoken with `hint: false`, then the action. Each room's story plus its how line is spoken once; symbol, secured and
  wrong lines every time. A wrong line cuts in (`now: true`) and goes stale on the next tap (`state.tap`), so fast tapping never queues a pile.
- The door swing and the Motion-off outline flash both take 450 ms, so timing is the same either way.
- Renders rebuild a station's DOM; focus (by `data-k`) and scroll are restored across a rebuild. In split mode,
  `setActive` only toggles `.station.active` and redraws the panel, so the station under the pointer is never rebuilt
  mid-tap (this was Refine blocker 1).
- A3's answer is not hand-written: `ONLINE` is `Net.reach(net(), 'router')` filtered to the five devices, with the
  access point `up: false`.
- Tests: `enter()` called synchronously then a click can race a ResizeObserver relayout; wait about 500 ms.
- In `stack`, the kit's `html, body {height: 100%}` would clamp `main`; `body.stack` sets height auto and
  `align-content: start` so the room and the panel never overlap.

## Done when (spec)

1. Rooms in any order, exit locked until all three are secured: pass.
2. C1 opens only with the right grid; wrong checks report counts, "!" badges after two. C2 bands Weak, Weak, Weak,
   Strong; only the fourth opens: pass.
3. I1 sums 70, 67, 79, 65; only Cy opens. I2 needs row 5, then the backup-and-new-password fix: pass.
4. A1 opens only at 3; 1, 2 and 4 give their results. A2 opens only with plan C. A3 opens only with the right sort,
   then exactly office, nurse and printer: pass.
5. Exit opens only with all six right; wrong cards slide back; real pointer drag works: pass.
6. Timer Off / 20 / 30; at 0 it says "Time!" and nothing locks: pass.
7. Voice: welcome once, how lines once, events every time, Read speaks hint and clue: pass (checked on the voice log
   with held clicks).
8. Every STANDARDS size with the active check button visible without scrolling, 375 via `drive.py --host`: pass
   (frames looked at: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x1000 stack, 375x812).
9. `Sec.safeDomain('evil.com')` and `('gmail.com')` false; console clean; no network requests; nothing stored by the
   tool (only the kit's Motion choice); "Curio Class" only: pass.

## Spec notes

- A1 with 1 server: the spec now says 5 p.m. to 8 p.m. (4 p.m. has 450 visits).
- A2 day strip: "Mon to Fri" read as last Friday through Thursday, since the disk broke Thursday afternoon.
- The exit's two clues are not in the spec; I wrote them. I2's wrong-fix reasons are my wording (now spoken too, and in the spec).

## Known gaps

- 1920x1080: the puzzles sit at real size, so the stations have empty space below.
- 680x425: the I2 change log scrolls inside its station; the exit pool scrolls too. Both work.
- Voice lines are not recorded yet (`voice/lines.json` is ready).

## Refine round 1 (2026-10-28)

All items in `refine.md` were applied: both blockers (split-room taps, the new Network closet puzzle), should-fix 3
to 12, polish 13 to 22 and the cheap nits. Summary in the spec's "Refine changes (round 1)". Engine changes in
`kit/security.js`: `band(r, names)` and `reasons(r, names)` take names for string input, `safeDomain` rejects a real
top-level label before the reserved suffix, `world` checks files, 44 px targets, focus ring over marked spots
(documented in docs/families/security.md). Checked: logic run at 1366 (every puzzle wrong then right, exit), 5 of 5
split taps at 1280, 1366 and 1920, the voice log (locked exit, entry hint, cut-in, Read, fix reasons), target sizes
and focus rings at 680, and frames at every STANDARDS size including 375 via `drive.py --host`.

## Refine round 2 (2026-10-28, exit check items, all in A3)

- Part notes and the wired / wireless definition show at every size (shorter notes; the prompt is no longer `opt`).
  At 375 (`.tiny`) the cards stay two columns (tile icon and button icons dropped), and sorting the last part
  scrolls Check sort into view (measured: top 380 of 812).
- Result and "!" marks are the tool's own SVG overlay (`.a3over`), not `view.badge`: a pill centered on each tile's
  bottom edge, its font shrunk to fit the narrowest gap between devices; the pick check is a small circle inside the
  tile's top right corner. No overlap at 375 to 1920.
- The access point is drawn as a plain Wi-Fi symbol (`skin.drawIcon`); its Wi-Fi links to the laptop and tablet
  show only the radio arcs (the dashed line and break mark are hidden), and the two devices carry a small Wi-Fi mark.
  Its note says it plugs into the switch with a cable and sends out Wi-Fi; the key says "Wi-Fi (wireless, no cable)".
- Check sort with parts left speaks `a3left` as an event (3 taps, 3 lines). The done note sits under the map, so the
  finished map is in view at 680x425. Tablet note: "no network cable port; uses Wi-Fi".

### Engine bug for the network family (kit/network.js, not changed here)

`badgeOn` with `{icon: 'x', text}` draws the x at the pill's start and centers the text over it, and the width
(`10 + text.length * 8`) leaves no room for the x, so `{icon: 'x', text: 'offline'}` reads "Xffline". It also uses the
class `net-x` for that badge, the same class as the down-node x, so one replaces the other. Pills are not clamped to
the gap between tiles, so at narrow sizes they spill over neighbours. Fix: give the x icon the same 16 px allowance and
left text anchor as check / lock, and keep a separate class for a tool's x badge.

## For Cory

- Settled in Refine: the Team timer stays Off by default; a teacher turns it on.

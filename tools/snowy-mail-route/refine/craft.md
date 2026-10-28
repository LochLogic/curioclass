# Craft lens: snowy-mail-route (round 1, 2026-10-28)

Cold read of spec.md, src.html, notes.md, handoff.md, art/prompts.json, voice/lines.json, kit/robot.js and
docs/families/robot.md. Bundled with `CURIO_DRAFT=1 python scripts/bundle_tool.py snowy-mail-route` (127 KB). Driven
in muted headless Chrome (ports 9720 to 9722, own profile) with held clicks (0.12 s), real keys, Sound on, Motion on
unless noted. Frames and logs in the lens scratch folder (f1/, out2/, outk/, outc/, outl/, outp/).

Counts: blockers 0, should fix 3 (general 2, family 1), polish 6, nit 2.

## Findings

### Should fix

1. **The footprint how-to (line 7) can be lost for the whole page load.** `src.html` onEnd (line ~983) picks the
   how line by a counter: `state.problems === 1 ? 'hFoot' : state.problems === 2 ? 'hStep' : null`. When line 7 is
   dropped as stale (the class presses Go or Step again, or edits a card, while the result line is still playing), it
   is never queued again, because the next problem is number 2 and gets line 6. Seen in three runs: edge5 (`hFoot`
   dropped `newer` at 28.9 s, then `hStep` at the second bump, `hFoot` never spoken), step5 and stale2 (same). Line 7
   is the tool's one idea ("Tap a footprint to find the card that made it"); a lively class that taps fast never hears
   it. Better: choose by `V.heard('hFoot')` (then `V.heard('hStep')`), not by the problem count. **general**
2. **Motion off makes the falling snow strobe.** `.flake{animation:fall linear infinite}` (src.html line 107) has no
   calm rule, so the kit's `.calm *{animation-duration:.01ms!important}` turns each flake into a 0.01 ms infinite loop:
   every frame lands at a random point of the fall. Measured in calm mode (outc): 16 running `fall` animations,
   duration 0.01, iterations Infinity; the first flake's y went 110.9, then 136.1 px 50 ms later. Motion off should
   be the calm view, and this is flicker. Better: `.calm .flake{animation:none}` (they stay scattered, as the comment
   on line 598 intends). **general** (any infinite CSS animation under the kit calm rule)
3. **Engine: the card pulse has the same calm problem.** kit/robot.js line 207 runs `rb-pulse` infinite; line 209
   only sets a static box-shadow under `.calm`, but the animation still runs at 0.01 ms per loop and overrides it, so
   a pulsing card flickers with Motion off. This tool never calls `strip.pulse` (it pulses footprints, which are
   handled), so nothing shows here, but traffic-light-coder and later siblings inherit it. Better:
   `.calm .rb-cell.pulse .rb-card{animation:none}` beside the static shadow. **family:robot**

### Polish

4. **Hearts never show with Motion off.** `.calm .hearts{animation:hcalm 1.6s step-end both}` (line 119) is meant to
   hold the hearts for 1.6 s, but the kit's `.calm *` duration override wins, so they vanish at once and the delivery
   has only the open door. Better: show them as a static group and remove them with the existing 1.7 s timeout.
   **general**
5. **The caption competes with the sky art at preview and phone sizes.** In compact and stack the hint sits in the dusk
   band over the far roofs, lit windows (#ffd77a, white text on it is 1.38:1) and falling flakes, which pass through
   the letters (f1/size-680x425, zoom680.png; outp/phone-a). Readable with the text shadow, but busy at the size the
   tool page shows first. Better: keep windows and flakes out of the caption box (or a soft dark plate behind it).
   **general**
6. **Wrong-house stop hides the house symbol.** On a wrong stop Pip stands on the right of the door and footprint
   number 3 sits on the door's left, so the Fish symbol is covered (out2/go5-end). The class is told "that's the wrong
   house" but cannot see which house it is. Better: on a house square put the last footprint number outside the door
   circle. **general**
7. **Line 5 (hCard) says "Use the arrows under the cards"**, but the engine's card buttons are deliberately
   chevron-and-bar icons that do not look like arrow commands, and in this tool "arrows" means the tray. For grade 1,
   "the buttons under the cards" (as hSel already says) matches the screen. This is a spec line, so it goes to the
   spec's open questions. **general**
8. **The first Go can wait about 12 s before Pip moves.** If Go is pressed while a welcome is playing, the walk waits
   for the welcome and then line 3 (kb-route: Go at about 3.5 s, `hGuess` started 8.6 s, walk after it ends). The wait
   for line 3 is in the spec; waiting behind the welcome too feels broken on a projector. Better: `now: true` on that
   one `hGuess`, or skip the rest of the welcome when Go is pressed. **general**
9. **Engine doc gaps against the code** (docs/families/robot.md vs kit/robot.js, checked function by function):
   `run.alive(g)` and `run.gen` are not documented, yet the tool uses `run.alive()`; `strip.locked`, `strip.el`,
   `strip.box`, `strip.cells`, `Robot.version` and `Robot.last` are undocumented; `canEdit()` also blocks card taps
   (the doc says only the buttons and keys); in sequence style `snap()` is called with no argument (the doc says
   `snap(world)`, which is true only for rules). Everything else matches (see below). **family:robot**

### Nit

10. Footprint buttons are `tabIndex = -1`, so a keyboard user cannot reach them; selecting a card pulses its
    footprints, so the debugging move still works by keyboard. Fine as is, or say so in notes. **general**
11. Empty slot numbers (#8ea3c4 on the apron, about 2.2:1) are faint; they are a placeholder, not a control. **general**

## Checks that passed

**Contract.** One file, 127 KB. No network requests (CDP Network log empty in every run). Kit used: `Curio.voice`,
`Curio.tone`, `Curio.yes`, `Curio.init`, kit Motion, Sound and Read; the strip, program and runner come from
`kit/robot.js`, not re-implemented. No console errors or warnings in any run, including all eight levels (fix-it
starting cards bump at card 5, the edge at card 7 and card 2; every best path and fix delivers) and all six Snow Town
houses with the notes' paths, run with Motion off.

**Engine vs the spec's "Family engine" (function by function).** 1. Program: `add(op, at)`, `replace(i, op)`,
`move(i, d)`, `remove(i)`, `clear()`, `load(list)`, `onEdit`, `gen`, `max`: all present (Node checks: full returns
null, move off the end returns -1, load cuts to max). 2. Strip: numbered cards, dashed numbered empty slots, one
selection, the three buttons (row and column names), keys (arrows, Delete/Backspace, Escape), `now`, bug badge,
pulse, run pointer: all present. 3. Runner: `style` sequence and rules, `exec`, `beat`, `onStep`, `target`; Stop,
Step, Go, generation guard. Node checks: target gives `wrong`, `ranout`, `extra`, `done`; step then go walks the rest;
step while busy is refused; an edit mid-run ends `edited`; a stopped run fires no late onStep and refuses go; rules
fire at most one card per tick and end on `{stop}` or `ticks`. 4. Trace: `{t, i, op, result, reason, snap}`,
`traceFor(i)`, `Robot.trace`. The lift matches robot-dance's `run(program, target, onStep)` results and its strip
behaviour.

**Untouched.** `git status` shows no change to tools/robot-dance, tools/loop-garden, kit/curio.js, kit/curio.css or
scripts/bundle_tool.py; robot.js and robot.md are new files only.

**Access.** At 1280x720, 1366x768, 1920x1080 and 760x900 every visible control is 60 px or more; at the 16:10 preview
sizes (680x425 to 1000x625) the smallest are 44 px and the map squares 47 px, as the family doc allows. Tray, Go and
all twelve slots on screen with no scroll at every size, including 375 wide (iframe host). Keyboard: tab order mode,
header, tray, Guess, Go, Step, Speed, level controls, cards, houses (or squares while guessing); level 1 built and run
with arrows and G; level 4 fixed with Enter and Delete, focus moved to the next card; visible focus ring on tray and
cards (outk). Color is never the only signal (arrow shape on cards and footprints, numbers on footprints). Motion off:
no tweens, Pip jumps, same beat timing (apart from findings 2 to 4). Sound off and on, Read: see below.

**Lines.** `allLines()` has 40 lines, the same set as voice/lines.json, word for word; the 30 spec lines match the
code exactly; the 10 added how lines are listed in handoff.md. Each spoken line matched the frame at its time in the
runs below. Art: prompts.json has no assets and src.html no `art:` tokens (all drawn in code). Words: no em dashes in
any file; "Curio Class" in full; classroom-safe; nothing stored but the kit Motion setting.

## Standard voice check

Held clicks, gap longer than the lines, Sound and Motion on. "Spoken" counts `as: spoken` in `__tool.vlog`.

| Line | Kind | Run (5 in a row) | Expected | Spoken |
|---|---|---|---|---|
| Up! (arrow names) | event, latest only | 5 arrow taps | 5 | 5 |
| 16 empty | event | Go x5, no cards | 5 | 5 |
| 17 full | event | 13th card x5 | 5 | 5 |
| 23 cleared | event | add, Clear x5 | 5 | 5 |
| 18 delivered | event | Go x5 (Star) | 5 | 5 |
| 24 guessYes | event | same, flag on Star | 5 | 5 |
| 19 wrongHouse | event | Go x5 (Fish) | 5 | 5 |
| 21 bank | event | Go x5 | 5 | 5 |
| 25 guessNo | event | same, flag elsewhere | 5 | 5 |
| 22 edge | event | Go x5 | 5 | 5 |
| 3 hGuess | how | first Go of the page | 1 | 1 |
| 7 hFoot | how | first problem | 1 | 1 (go5, bank5, route); **0** when dropped stale (edge5, step5, stale2): finding 1 |
| 6 hStep | how | second problem | 1 | 1 |
| hPaused | how | Step x5 | 1 | 1 (then silent x3) |
| hSel | how | pick and put down a card x5 | 1 | 1 (then silent x4) |
| hFlag | how | Guess on, flag, Guess off x5 | 1 | 1 (then silent x4) |
| hGo | how | same | 1 | 1 (then silent x4) |
| hHouse | how | delivery x5 | 1 | 1 (then silent x3) |
| hNext | how | level 1 delivered | 1 | 1 |
| 1, 2 welcome Snow Town | welcome | page | 1 each | 1 each |
| 4, 8, 9 welcome Mail Route, levels 1, 2 | welcome, how | entry, Next | 1 each | 1 each |
| 11 lv4 then 5 hCard | how | open level 4 | 1 each | 1 each |

- **Stale lines:** fast taps (0.2 s) through arrows, Go, Stop, a mode switch, Start over, Go, back to Snow Town and
  Clear: queued how lines were dropped (`newer`, `hush`, `chain`), never played late; the only line after the burst
  was "All clear" on the Clear that triggered it. After a result, an arrow tap dropped the queued wrongHouse (`stale`)
  and its hStep (`chain`). No line named a hidden or disabled control.
- **First tap (fresh page each):** map square: welcome about 140 ms after the tap. Arrow: "Up!" only, then the welcome
  after it (welcomeAfter). Mail Route button: its welcome and level line only. Read: the hint only, no welcome; the
  next mode entry brought its welcome. Sound off then on: nothing on the first tap, then the welcome once. Key G with
  no cards: "Add an arrow card first!", then the welcome. House tap: the welcome. Nothing spoke before a tap.
- **Read:** Read during line 3 stopped it and read the hint; Read again during Read restarted cleanly; Read with Sound
  off read the hint; a mode change right after Read started its welcome at once. Nothing cut Read off.
- **Order:** in every log, spoken lines follow the order of the actions.

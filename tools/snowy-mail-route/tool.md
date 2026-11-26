# Snowy Mail Route: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Refine

<!-- part: refine.md -->

PASS
Counts: blockers 0, should fix 10 (general 8, family 2), polish accepted 13

### snowy-mail-route: Refine

Lens files: refine/teaching.md (T), refine/play.md (P), refine/craft.md (C). Read them for frames and detail.

#### Blockers
None.

#### Should fix
1. **The first Go of a page load freezes Pip for 8 to 14 s** (P-S1, C polish). Line 3 plays after any welcome still
   speaking, Go shows Stop, the arrows are dead, and the line says "Tap Guess" while Guess is disabled. The first Go
   walks at once (line 3 cuts in short or comes before Go is live, never as a wait), and no line names a disabled
   control.
2. **The footprint how line (line 7) can be lost for the whole page load** (T-S2, C-S1). Pick the how line by what has
   been heard (V.heard('hFoot')), not by a problem counter; line 6 the same. The footprint move is the tool's main
   debugging step, so it must be heard once.
3. **Footprints read as pointing backwards, and are about 20 px** (P-S2). Each print points the way Pip stepped and is
   readable on a projector at 1366x768.
4. **Pip hides the last footprint; number circles cover the house symbol** (P-S3, C polish). After a bump the last
   prints and the tapped print's pulse are visible; door and house symbols stay readable on a wrong-house stop.
5. **No way to choose a level** (P-S4). Settled with BASELINE (a standalone tool a teacher drives): the level dots are
   buttons, any level can be opened, and the bar says which one is current. Saving progress is not needed.
6. **680x425: Start over and Next are 29 px wide** (P-S5, T-N3). Every target at least 44 px; the Speed button gives
   up its width.
7. **"Pip can't walk through snow"** (T-S1). Pip walks on snow every step: say snowbank (line 10, the spec and
   lines.json).
8. **Motion off makes the falling snow strobe** (C-S2). The flakes stop or stay still with Motion off.
9. **The engine's .rb-cell.pulse strobes under .calm** (C-S3; family:robot). Give it a calm rule in kit/robot.js.
10. **The "?" badge answers the narrator's question** (T-P1, promoted under the wave rule that the screen never gives
    an answer away; family:robot). On levels 4 and 7 the bumping card is the bug. Show the badge only after the class
    answers (a footprint or card tap) or after the hint has asked twice; record the rule in docs/families/robot.md.

#### Polish accepted
11. After a bump the hint doesn't send the class to footprints the bad card never left; it names the last print
    (T-P2; family:robot).
12. "Bug" and "debugging" are heard where notes.md lists them (T-P3).
13. One talk question names IM-03, such as "We changed one card. What changed for Pip?" (T-P4).
14. Level 8 doesn't say "Go slowly"; it names Step or the speed (T-P5).
15. Ending on the Post Office doesn't play "Pip stopped in the snow" (T-P6).
16. Delivery reads on a projector, and level 8 has a small finale (P6; minimal, K-2 warm).
17. A footprint tap picks its card and the next arrow replaces it; tapping the same card doesn't drop it (P7).
18. The welcome's "letter in Pip's bag" matches what is on screen (P8).
19. The panel doesn't drop when the hint wraps: reserve its height (P9).
20. Hearts show with Motion off (C).
21. The caption stays readable over the sky at preview and phone sizes (C, P-N12).
22. Line 5 says "the buttons under the cards", matching the chevrons (C; spec line).
23. docs/families/robot.md documents run.alive(), canEdit blocking taps, sequence snap() and the getters (C;
    family:robot).

Nits are optional; fix the cheap ones (notes.md "bumps the edge", the fix-it hint on levels 6 and 7, the dimmed mode
button while Pip walks, the guess flag on a new address, footprints in the tab order, empty-slot numbers at 3:1).

#### For Cory
- The title: keep "Snowy Mail Route" with Pip the penguin? (spec open question; the builder kept it).

#### Exit check (round 1, 2026-10-28)

Cold exit check. Bundle `CURIO_DRAFT=1 python scripts/bundle_tool.py snowy-mail-route`: 135 KB. Driven in muted
headless Chrome (own profile, ports 9770 to 9778) with held clicks (0.12 s) and a speech stub paced at 30 to 70 ms per
character (browser voice, no clips yet, as expected). Frames and logs:
`C:\Users\Cory\AppData\Local\Temp\claude\S--\98b8b046-f7f2-48d0-a719-c61ce01237be\scratchpad\exit-smr` (out1 to out8,
sheet-1366.png, sheet-680.png, sheet375.png, z-l8feet.png). host.html deleted after the 375 run.

##### Open
10. **Still open (should fix, family:robot).** The "?" badge shows the moment Pip bumps, before anyone answers.
    src.html:971, in `onStep`'s bump branch, still calls `strip.setBug(i, '?')`, so the gate added in `onEnd` (lines
    998 to 999, `state.asked >= 2`) and `onSelect` (line 400) never gets a say. Seen: level 4, first Go, no taps: card 5 has
    `.rb-cell.bug` during the bump and after the run ends with `state.asked` 1 (out1/l4badge-l4bump.png, l4end.png).
    The same happens at 375 (out8, third frame) and in Snow Town. Fix: drop the setBug at line 971 (onStep keeps
    `setNow`), then re-check levels 4 and 7.
24. **New (should fix, general).** At 1280x720 the footprint buttons are 58x58 px (`.fpb`,
    `size = max(44, min(s * .62, 96))` with s = 93). Done when 8 and the K-2 band ask for 60 px at full screen, and the
    footprint tap is the tool's main move. 1366x768 gives 63 px and 1920x1080 gives 96 px. Fix: a 60 px floor in the
    wide layout.

##### Re-checked and fixed
1. **First Go: fixed.** Go pressed 2 s into the Snow Town welcome: the walk starts 63 ms after the press (trace 1,
   running). The welcome plays on and names nothing that is off. A first Go after a house tap also walks at once. A
   queued hGuess goes stale on Go and never plays.
2. **Footprint line: fixed.** The tool now picks the line with `V.heard`. At a 2 s pace (out2/pace2town), hFoot was
   dropped four times when the class acted during the result line, came back on every new problem, and was spoken
   once at the first quiet moment (42 s). It is never lost for the page load. After a bump, hLast fills the same role.
3. **Footprints: fixed.** The prints are toe-forward and point the way Pip stepped: Up up, Right right, Down down
   (z-l8feet.png). They are about 25 px at 1366x768 and readable.
4. **Fixed.** Pip stands at the right of the square and the prints sit at the left. On a wrong-house stop the house
   symbol stays visible at 1366 (Sun, out4/town-1366x768-wrong). At 680x425 the number circle touches the door ring
   but does not hide the symbol.
5. **Level picker: fixed.** Eight 140 px letter buttons at 1366 and 76 px at 375, each with a number and the house
   picture. The current level has a gold ring and delivered levels a check. Level 4 opens and the level bar is 60 px
   or more at full screen. Keyboard: Enter opens it, focus lands on the current level, Escape closes it and focus goes
   back to the dots.
6. **Fixed.** At 680x425 no target is under 44 px, Start over and Next included.
7, 8, 9, 20. **Fixed.** Line 10 now says snowbank. With Motion off, `getAnimations()` shows 0 running and no infinite
   animations: the flakes are still, the footprint and card pulse is a still ring (`animation: none`, box-shadow), and
   the bug wobble is off. Turning Motion on and off again gives the same result. The hearts show with Motion off
   (opacity 1).
11 to 19, 21 to 23. **Fixed.** hLast and hFirst (an edge at card 1 gives the first-card line); "bug" at level 4 and
   "debugging" on a fix-it delivery; the IM-03 talk question; level 8 names Step; the Post Office ending says "home";
   the delivery ring and letter, and a finale on level 8; the picking rule (a footprint picks card 2, a tap on card 2
   keeps it, Down replaces it, and a plain card tapped twice is put down); the welcome names the letter in the corner;
   the hint keeps its height (the tray is at the same y with a one-line and a two-line hint); the caption sits on a
   dark plate; line 5 says "the buttons under the cards"; robot.md is complete.
- Nits fixed: mode buttons are not dimmed while Pip walks, a new address clears the flag, footprints are in the Tab
  order, empty slots are #5f7397.

##### kit/robot.js against docs/families/robot.md, function by function
`program` (add, replace, move, remove, clear, load, on, ops, card, indexOf, gen, length, full, max), `run` (sequence and
rules, go, step, stop, status, busy, gen, alive with and without g, next, tick, trace, traceFor, generation guard,
finish before onEnd), `strip` (select, deselect, sel, locked, el, box, cells, setNow, setBug, pulse, lock, flash,
flip, size, place, render, card, cell, canEdit blocking card taps, keys, focus rescue) and `Robot.version`,
`Robot.last`, `Robot.trace`, `Robot.traceFor`: all match the doc. The calm rule and the picking rule match the code.
The badge rule is in the doc, but this tool breaks it (item 10). robot-dance, loop-garden, kit/curio.js and
kit/curio.css have no changes (`git status`, `git diff`). Only snowy-mail-route uses `kit:robot`.

##### Recomputed (Python BFS and walk)
Shortest paths: 3, 5, 6, 6, 7, 7, 8, 8. Every listed best path is a shortest path and delivers, both in the
simulation and in the page at 1366 and at 680 with Motion off. The maps match the spec table. Starting cards:
level 4 bumps the bank on card 5 at (3,2) to (3,3), level 6 bumps the edge on card 7 at (6,3), and level 7 bumps the
bank on card 2 at (2,4) to (2,3). The fixes deliver: level 4 (card 5 to Right), level 6 (any one Right removed:
D D R R R R U) and level 7 (cards 2 and 3 swapped). In Snow Town every notes path is shortest (Fish 3, Star 4, Sun 2,
Tree 5, Moon 5, Heart 8), all six deliver in the page, and `town.delivered` lists all six.

##### Frames
- Default screen and Snow Town wrong house, level 8 delivered and the picker at 680x425, 800x500, 1000x625, 1280x720,
  1366x768, 1920x1080, 760x900, plus 375x812 through --host. Tray, Go, Step, Guess and all 12 slots are on screen
  with no horizontal scroll at every size. The only target under its floor is item 24.
- Levels 1 to 8 at 1366 (Motion on) and at 680 (Motion off): each opens with the right map, cards, letter and hint.
- No console errors in any run. No network requests from the tool: the only ones were the host page and its
  favicon on the 375 run.

##### Gate
1. Done when: 1 to 7, 9 and 10 pass. 8 fails only on item 24.
2. All four codes are taught (see the Teaching lens). bug and debugging are now spoken.
3. The defaults work for a solo student: the first screen speaks the welcome and how-to, and every waiting moment
   names its control.
4. No sensitivity review needed (rule 5 does not apply).
5. **Not met:** items 10 and 24 are still open.
6. Bundle clean, 135 KB, no console errors, no network requests.
7. Voice counts are right (table below).

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| Up! (arrow), 5 taps | event | 5 | 5 |
| 16 empty, Go x5 | event | 5 | 5 |
| 17 full, 13th card x5 | event | 5 | 5 |
| 23 cleared x5 | event | 5 | 5 |
| 18 delivered x5 | event | 5 | 5 |
| 24 guessYes (flag on Star) | event | 1 per run | 1 |
| 19 wrongHouse x5 / 25 guessNo x5 | event | 5 / 5 | 5 / 5 |
| 21 bank x5 / 22 edge x5 | event | 5 / 5 | 5 / 5 |
| home x5 / 20 snow x5 | event | 5 / 5 | 5 / 5 |
| fixedBug, level 4 fixed, x5 | event | 5 | 5 |
| 7 hFoot, hLast, 6 hStep, 3 hGuess | how | 1 each | 1 each |
| hPaused (Step x5), hSel (x5), hFlag, hGo (x5), hHouse | how | 1 each | 1 each, then silent |
| hNext; welcomes 1, 2, 4; levels 1, 2, 4; 5 hCard | how / welcome | 1 each | 1 each |

First tap on a fresh page:
- Stage: the welcome at 157 ms.
- Arrow: "Up!", then the welcome after it.
- Mail Route: its welcome and line 8.
- House: the welcome at 153 ms.
- Key G: "Add an arrow card first!", then the welcome.
- Read: the hint only. Sound off and on then gave the welcome once, and the next mode entry gave its welcome.
- Sound: nothing.

Nothing spoke before a tap. Read stops a line and speaks the hint, with Sound off too, and a mode change right after
Read starts at once. In a fast 0.2 s burst (arrows, Go, Stop, Mail Route, Start over, Snow Town, Clear) nothing played
late, and the only line after the burst was "All clear". Spoken lines followed the order of the actions.

##### Nits (optional)
- After a second problem the voice says line 6 (Step) while the hint still shows the footprint or last-footprint
  line, so Read says something else. general.
- If the class presses Go while the Snow Town welcome's second line (hTown) is playing, "Tap a house..." plays on
  during the walk. general.

##### Re-check of the integrator fixes (items 10 and 24, 2026-10-28)
Rebundled with CURIO_DRAFT=1 (135 KB). Driven in my own Chrome; host.html was deleted after the 375 run. Frames are in exit-smr/out9 and out10.
- **Item 10: fixed.** `onStep` no longer badges.
  - With no answer yet, no badge: level 4 (card 5), level 7 (card 2) and a Snow Town bank (R U, card 2), at 1366 and at 375.
  - The badge shows on the right card after a footprint tap, after a card tap, and after the second Go (the hint has asked twice). Seen in all three places at 1366 and at 375.
  - A delivery or a new level resets the count.
- **Item 24: fixed.** Footprint buttons are 60 px at 1280x720, 63 px at 1366x768 and 96 px at 1920x1080. They are 44 px at 680x425, 800x500 and 375, 55 px at 1000x625, and 60 px at 760x900.
  - At full screen and in the preview, no footprint button overlaps another.
  - At 760x900 and 680x425, neighbors overlap by up to 23 percent of a button, and a button covers up to 12 percent of Pip. Pip is not a target, so this is harmless.
- **Bump flow: no regression.**
  - Snow Town bank, Go x5: bank 5, hLast 1, hStep 1, hGuess 1.
  - Level 4, Go x5: bank 5, hLast 1, hStep 1. The hint stays "Tap the last footprint. The card after it made Pip bump."
  - Console clean, no network requests.
- **Polish, not blocking (general).** In Snow Town, footprint buttons sit over part of a house's tap square, and the footprint wins the tap: about 30 percent of the square at full screen (true before this fix) and 53 percent at 760x900 and 680x425 (new from the 60 px floor in stack). A tap on a house's lower left picks a card instead of sending the letter. Tapping the roof still works.
- **Gate: all seven points hold.** The two nits above remain optional.

<!-- end part -->

<!-- part: refine/craft.md -->

### Craft lens: snowy-mail-route (round 1, 2026-10-28)

Cold read of spec.md, src.html, notes.md, handoff.md, art/prompts.json, voice/lines.json, kit/robot.js and
docs/families/robot.md. Bundled with `CURIO_DRAFT=1 python scripts/bundle_tool.py snowy-mail-route` (127 KB). Driven
in muted headless Chrome (ports 9720 to 9722, own profile) with held clicks (0.12 s), real keys, Sound on, Motion on
unless noted. Frames and logs in the lens scratch folder (f1/, out2/, outk/, outc/, outl/, outp/).

Counts: blockers 0, should fix 3 (general 2, family 1), polish 6, nit 2.

#### Findings

##### Should fix

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

##### Polish

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

##### Nit

10. Footprint buttons are `tabIndex = -1`, so a keyboard user cannot reach them; selecting a card pulses its
    footprints, so the debugging move still works by keyboard. Fine as is, or say so in notes. **general**
11. Empty slot numbers (#8ea3c4 on the apron, about 2.2:1) are faint; they are a placeholder, not a control. **general**

#### Checks that passed

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

#### Standard voice check

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

<!-- end part -->

<!-- part: refine/play.md -->

### Play lens: snowy-mail-route

Cold Play lens, 2026-10-28. Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py snowy-mail-route` (127 KB). Driven
with a one-tab CDP driver (held clicks, 120 ms), muted headless Chrome, a speech stub that paces the browser voice at
about 70 ms per character (no clips recorded yet, as expected). Frames and scripts in
`C:\Users\Cory\AppData\Local\Temp\claude\S--\98b8b046-f7f2-48d0-a719-c61ce01237be\scratchpad\lens-smr-play\shots`.

Runs:
- **Teacher on a projector (1366x768), Snow Town:** class calls "Up!", a child shouts "Go!" after one card, then
  builds to the Star house, Guess and flag, Go, footprint tap, Heart address, a bump, Go pressed twice, Clear.
- **Teacher, Mail Route, all eight levels at a real pace** (arrows about 2 s apart): level 1 with Go too early (Pip
  stops in the snow) then fixed; level 2 with a correct guess; level 3 bump, footprint tap, fix by changing card 1;
  level 4 Go, bump at card 5, change it to Right; level 5 with Quick and Step x7; level 6 edge at card 7, take it
  away; level 7 bump at card 2, move it later; level 8 built and delivered; Next wraps to level 1. Every fix-it bug
  bumps where the spec says and every fix delivers. Console clean throughout.
- **Solo student (1366x768):** first tap on a house, Read, Mail Route, wrong house (R R R D D on level 1), then fixed.
- **Sizes** after a full run (Snow Town wrong house, Big Town edge) and with a card picked: 680x425, 800x500,
  1000x625, 1280x720, 1366x768, 1920x1080, 760x900, 375x812 (iframe host). No horizontal scroll, tray, Go and the
  full strip on screen at every size.
- **Motion off:** a three-card walk takes 3341 ms against 3339 ms with Motion on (calm keeps time).

#### Findings

##### Should fix

1. **The first Go of the page load freezes for 8 to 14 seconds, and the line it plays contradicts the screen.**
   Where: `go()` (src.html, "the first Go of the page load without a flag"). How: teacher run, Go pressed after one
   card while the Snow Town welcome was still speaking: hGuess waited for the welcome, then played, and Pip only
   started 14 s after the press (log: Go at 4.1 s, hGuess at 9.4 s, walk ends 18.5 s; frames A02, A03). In Mail
   Route level 1 the same Go took 12 s to walk two cards (B01). During the wait Go shows **Stop**, the arrows and
   Guess are dimmed, and the voice says "Before you press Go ... Tap Guess, then tap that square" right after Go was
   pressed, while Guess is disabled. Arrows the class calls during the wait are ignored, and a teacher who presses Go
   again because nothing moved stops the walk (seen in the first route run). Better: say the trace-and-guess idea
   before the first Go (with the first arrow card or the level hint), or let the first Go walk and give line 3 after
   the first result; never name Guess while it is off. general.
2. **Footprints read as pointing the wrong way, and they are small.** Where: `FOOT` and `drawFoot`. How: zoomed frames
   z-feet.png, z-feet2.png, B26, S-town-1920x1080. The webbed foot has a narrow pointed heel and a wide toe end, so
   at this size each print reads as an arrowhead pointing backwards: Down prints look like little up-pointing trees,
   Up prints like down arrows, Right prints like left arrows. Grade 1 children compare a print with the arrow card
   that made it, so a correct trail looks wrong. Prints are about 20 px long at 1366x768 (31 px at 1920x1080), hard to
   see from the back of a room. Better: a clear toe-forward print (three round toes ahead of a round pad), or a small
   arrow chevron in the card color beside each pair, and larger prints. general.
3. **Pip stands on the last footprint pair and hides it, the very clue the debugging move needs.** Where: `pipSpot` /
   `footAt` on plain squares. How: A09, A12, B07 (the footprint tap on level 3: footprint 1 pulses under Pip, only its
   number shows), B10, B16. After a bump the last print is under Pip and the bug card is the one after it, so "find
   the last footprint" is the hardest one to see. On house squares the number circle sits over the door symbol
   (3 over Fish, 4 over Star, 8 over Heart in S-town-1920x1080; 5 over Heart in C02), hiding the address the class
   needs to see after a wrong house. Better: offset Pip or the print on the square Pip ends on, and move number
   circles off the door symbol. family:robot (the trace drawing).
4. **No way to choose or skip a level.** Where: `#dots` (plain `<i>`, not buttons), `#next` (enabled only after a
   delivery), nothing saved. How: full route run. A teacher who wants the fix-it levels (4, 6, 7), who resumes the
   next day after a reload, or whose class is stuck must replay every earlier level first. Better: make the level
   dots 60 px buttons (or a level picker) so the teacher can open any level. general.
5. **Start over and Next are 29 px wide at 680x425.** Where: compact panel grid, `body.compact .panel`
   ("speed lv" row). How: size sweep, `over:29x44`, `next:29x44` (S-route8-680x425, S-sel-680x425); the Speed toggle
   beside them takes 158 px. The handoff says no target is under 44 px. Better: give speed and the level buttons an
   even split in the compact row. general.

##### Polish

6. **The payoff moments are small.** Delivery is a thin door swing, three hearts about 20 px tall and a roof badge
   (C04, B02), easy to miss on a projector; finishing level 8 shows only the filled dots and a line (B26). Better: a
   bigger door and letter moment sized to the square, and a short finale after level 8 (every house with its badge,
   Pip waving an empty bag). general.
7. **Footprint tap, then card tap, drops the card.** How: route run, level 3: the footprint tap picked card 1, the
   natural next tap on card 1 ("that one!") put it down again, so the next arrow was added at the end instead of
   changing card 1. Better: a tap on the card a footprint just picked keeps it picked. family:robot.
8. **The Mail Route welcome points at the smallest letter on screen.** "Look at the letter in Pip's bag" (wRoute),
   but the letter in Pip's bag is about 12 px; the big letter card is in the sky's top left corner (B00). Better:
   "Look at the letter up in the corner", or make Pip's bag letter big while Pip stands at the Post Office.
   general.
9. **The panel moves when the hint wraps.** The tray, Guess and Go drop 23 px when the hint goes from two lines to
   three (A00 against A02, 1366x768), so a teacher at a smartboard reaches for a button that has moved. Better:
   reserve three lines for the hint in the wide panel. general.

##### Nit

10. While Pip walks, the active mode button turns a dim orange (`setOff('m-town', busy && !rt)`), which looks like a
    state change (A02). general.
11. In Snow Town the guess flag stays on the old square after a new address is picked (A11, A12). general.
12. In the compact and phone layouts the white caption runs over the sky's roofs and falling flakes (S-route8-680x425,
    P-375); readable but busy. general.

#### Checked and fine

- Every level loads the spec's map; the three fix-it bugs bump at cards 5, 7 (edge) and 2; the fixes deliver;
  level 8 and the wrap to level 1 work; the dots fill.
- Go too early with an empty strip, too few cards (stopped in the snow), wrong house, bank and edge bumps all give the
  right line and frame; the bug card gets its "?" badge.
- Results, guess lines and arrow names are spoken every time; hNext, hBuild, hPaused and the level how lines are
  spoken once, then hint only; Read speaks the hint.
- Step at Quick walks one card per press and the hint names Step and Go; Stop halts at once.
- Calm mode keeps the beat timing.

<!-- end part -->

<!-- part: refine/teaching.md -->

### Teaching lens: snowy-mail-route (grade 1, robot family)

Round 1, 2026-10-28. Cold read of spec.md, src.html, notes.md, voice/lines.json, art (none: drawn in code), against
REFINE.md (Teaching lens), STANDARDS.md and BASELINE.md. Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py
snowy-mail-route` (127 KB). Driven with `scripts/drive.py` (port 9701, own profile), 1366x768 unless named.

Counts: blockers 0, should fix 2 (general 2, family 0), polish 6 (general 4, family 2), nits 3.

#### What I recomputed (Python BFS and a walk simulator, then the real page)

- **Snow Town** (Post Office (1,4); banks (2,3) (3,2) (5,3)): shortest steps Fish 3, Star 4, Sun 2, Tree 5, Moon 5,
  Heart 8. Every notes path is a shortest path and delivers in the page (tapping each house addresses the letter,
  `town.delivered` ends with all six).
- **Levels**, page map equals the spec table for all eight (start, house, other houses, banks, starting cards).
  Shortest lengths 3, 5, 6, 6, 7, 7, 8, 8, as listed; each listed path is one of them (count of shortest paths: 1, 10,
  4, 3, 3, 6, 17, 1) and each delivers in the page.
- **Fix-its:** L4 `U U R R D R` bumps the bank (3,3) on card 5 from (3,2); fix (card 5 to R) delivers. L6
  `D D R R R R R U` reaches (6,3) after card 6, card 7 bumps the right edge; removing any of cards 3 to 7 (the Rights)
  delivers, removing a D or the U does not. L7 `R U R U U R R R` bumps the bank (2,3) on card 2 from (2,4); the 2-3
  swap is the only adjacent swap that delivers. Page agrees: `?` badge on card 5, 7 and 2.
- Guess: flag on (3,2) before the L4 bump gives line 24, flag on (3,3) gives line 25 (a bump counts as where Pip
  stopped). Flag places, moves ((2,2) then (4,2)) and removes.

#### Standards (rule 2)

The 2026 statements are not in the repo; I used the gap-fill reading (docs/agents/gapfill/cs/notes.md) and the 2017
crosswalk.
- **E1-ALG-PS-01** (create and follow an algorithm for a daily process): taught. The class builds a mail route and
  follows it before running (trace with a finger, Guess flag, checked by line 24/25).
- **E1-PRO-PD-04** (a program as a sequence that does a task): taught. Five build levels and Snow Town; the card
  strip is the sequence, Step shows one card at a time.
- **E1-PRO-TR-07** (find and fix errors): taught. Three fix-it levels (wrong card, extra card, swapped order), each
  verified above, plus the footprint-to-card link.
- **E1-ALG-IM-03** (grade 1: change a step, the result changes): taught by doing (every fix-it is one change that
  turns a bump into a delivery; Mixed Up is the same cards in a new order). It is never said out loud; see polish P4.

#### Done when

1. Snow Town: PASS (each house tap addresses; all six notes paths deliver).
2. Levels load the table exactly, each build level delivers with its listed path: PASS.
3. Fix-its bump at card 5, card 7 (edge), card 2, and the fixes deliver: PASS.
4. Footprints numbered; tapping footprint 3 on L4 selects card 3 (`strip.sel = 2`) and pulses its pair: PASS.
5. Guess places, moves, removes; 24/25 right including after a bump: PASS.
6. Step one card (paused, `next` 1), Step again, an edit (add Up) resets Pip to start and clears footprints, Step
   then Go finishes, Stop halts at once (Pip unchanged 1.5 s later): PASS.
7. Keyboard only: L4 fixed with real keys (Tab to Go, Enter; Tab to card 5, Enter; Shift-Tab to Right, Enter; Go):
   delivered. L6 card removed with Delete. G and S work (synthetic keydown; drive.py has no letter keys): PASS.
8. Tray, Go and all 12 strip slots visible, no horizontal scroll at 680x425, 800x500, 1000x625, 1280x720, 1366x768,
   1920x1080, 760x900; 60 px minimum at 1280 and up: PASS (see nit N3 for the preview).
9. Voice, light check only (the Craft lens owns the counts): five held Go taps on L4 spoke line 21 five times, line 3
   once, line 6 once. Line 7 was dropped and never came back: see should fix S2.
10. Motion off (reduce): all eight levels deliver, no console errors in any run: PASS.

#### Findings

##### Should fix

**S1. Level 3 line says Pip can't walk through snow.** src.html:314 (`lv3`), voice/lines.json, spec line 10:
"Pip can't walk through snow. Find a way around." The whole town is snow, Pip walks on it every step, and line 20 says
"Pip stopped in the snow". A grade 1 class hears a contradiction on the first level about obstacles. Better: "Pip
can't walk through a snowbank. Find a way around." (Seen: read against lines 20 and the L3 frame.) **general**

**S2. Line 7, the tool's main debugging move, can be lost for the whole page load.** src.html:983 queues `hFoot`
(line 7) only on the page's first problem, after the event line; if that how line goes stale (the class presses Go
again or edits a card while line 21 is still being read, a normal classroom moment), it is dropped and never queued
again: the second problem queues line 6, later ones nothing, and `hFoot` is not in `SPEAK_HOW`, so the hint changes
silently. Seen: five held Go taps on L4, 14 s apart: `hFoot` "dropped, stale" at t=17.6 s, never spoken in the run.
K-2 reads nothing, so "Tap a footprint to find the card that made it" may never reach the class. Better: keep line 7
pending until it is actually spoken (queue it again on the next problem if it was dropped), and do the same for line
6. **general**

##### Polish

**P1. The `?` badge answers the question the narrator just asked.** src.html:935: on a bump the bumping card gets a
red `?` at once, while line 21/22 asks "Which card sent Pip that way?". On L4 and L7 the badged card is the bug (L6:
one of the extra Rights), so the fix-its are solved by looking at the badge, not by reading the footprints, which is
the tool's stated idea ("the footprint trail is the evidence they read to find the bug themselves", spec Not like).
The badge is in the spec, so this goes to the spec's open questions: e.g. show the snow puff only, and put the `?` on
the card after the class taps the last footprint (or after Step reaches it). Frames: out/l4bump.png, l7bump.png,
l6bump.png. **family:robot**

**P2. After a bump the hint points at footprints the bad card never made.** src.html:1085: the hint after a bump is
"Tap a footprint to find the card that made it." The bumping card leaves a snow puff, not footprints, so the trail
ends one card before the bug. Notes' talk question gets it right ("Which footprint is the last one? Which card comes
right after it?"). Better hint after a bump: "Tap the last footprint. The card after it bumped." **family:robot**

**P3. The words bug and debugging are never heard.** notes.md:46 says "Words used: algorithm, program, bug,
debugging", but no line or on-screen text uses any of them; only the teacher's talk questions do. For TR-07 the word is
part of the idea at this grade (Code.org glossary, the spec's source). Better: the fix-it level lines name it, e.g.
L4 "One card is wrong. A mistake in the cards is called a bug." and the delivery after a fix-it "You fixed the bug!"
**general**

**P4. IM-03 is done but never named.** The class changes one card and Pip's whole route changes, but nothing asks
them to notice that. Add a talk question to notes.md (and optionally the delivery line after a fix-it): "We changed one
card. What changed for Pip?" **general**

**P5. Level 8 says "Go slowly"; Go is a button that walks every card.** src.html:319: "Go slowly, one arrow at a
time." A grade 1 class hears "Go" as the yellow button. Better: "Press Step to walk one arrow at a time." **general**

**P6. Stopping on the Post Office is called "in the snow".** src.html:324 and the outcome code: Snow Town `U D`
ends on the Post Office square and line 20 plays, "Pip stopped in the snow. Is there a card missing?" (seen in the
town run). Words don't match the picture. Better: a Post Office case ("Pip came back to the Post Office!") or treat
it as snow without the missing-card guess. **general**

##### Nits

**N1.** notes.md:18: "Pip walks off the edge at card 7". Pip bumps the edge and slides back; say "bumps the edge of
town at card 7". **general**

**N2.** src.html:334 `hFix` "find the card that is wrong" stays on L6 (an extra card) and L7 (two swapped cards); the
level lines are right, the hint is generic. Optional per-level hint. **general**

**N3.** At 680x425 (site preview) Start over and Next are 29 px wide (frame out/sz680x425.png). Full screen is 60
px, so Done when 8 passes; noting it for the Craft and Play lenses. **general**

#### Guardrails and flags

- K-2 teacher-led: driver "teacher", every fixed line spoken, icons on every control. No points, timers or score;
  delivery is a win state, which is fine here (not hard history). No health content.
- Nothing gives the stop square away before Go in Guess mode (no ghost path; the strip carries no marks before a run).
  The only give-away is P1, after the run.
- Sensitivity (rule 5): nothing cultural, Native or hard-history (a penguin, snow, houses with symbol addresses). No
  sensitivity review needed. Rule 8: no sensitive topics in these standards.

Frames and data: C:\Users\Cory\AppData\Local\Temp\claude\S--\98b8b046-f7f2-48d0-a719-c61ce01237be\scratchpad\lens-smr-teaching\out
(default, l4start, l4bump, l6bump, l7bump, l8open, sz680x425 to sz1920x1080, sz760x900, kbfix2, motionoff, voice5) and
levels.json, town.json, guess.json, step.json; sim.py is the BFS and walk simulator.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Handoff: snowy-mail-route (build, 2026-10-28)

#### What was built

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

#### Engine API (kit/robot.js, global `Robot`, version 1)

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

#### Spec additions (decided in the build)

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

#### Checked

- Sizes 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812 (host): no target under 44 px
  (map squares 47 px at 680x425, 53 px at 375), tray, Go and the strip on screen, no hint clipping, no horizontal
  scroll. Console clean through all eight levels.
- Voice with held clicks at 2 s: first tap then the welcome; lines that go stale (walking, a newer how) are dropped,
  never played late; the first Go without a flag speaks line 3 and the walk waits for it; level 4 queues line 5.
- Keyboard: tab order is mode, header, tray, Guess, Go, Step, Speed, level controls, cards, houses (Snow Town) or
  squares (while guessing); nothing moves focus on load.

#### Known gaps / for Cory

- The Snow Town welcome is dropped (not replayed) if the first tap starts a walk before it is said: it is only valid
  while Pip is idle. It plays the next time the mode is opened.
- Snowbank faces and footprints are small at 680x425 (squares 47 px) but legible; the footprint numbers are 11 px there.
- `voice/` has no recordings yet (run `scripts/voice.py snowy-mail-route`).
- Open question from the spec stays open: keep the title "Snowy Mail Route" (penguin) over "Robot Mouse Mail".

#### Refine round 1 (2026-10-28)

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

<!-- end part -->

## Finish check

<!-- part: final.md -->

PASS (re-check 2026-10-29: all 3 should-fix items and polish items 4 and 5 fixed and confirmed; no regressions)

Round 1 verdict, kept for the record: (1) the Snow Town welcome holds the voice queue: its second line plays after its moment, and result lines land up to 13 s late; (2) a level intro keeps talking over the walk after Go, and the bump line comes about 5 s after the bump; (3) the welcome take reads "Welcome to Snow Town, Pip. The penguin carries the mail."

### snowy-mail-route: Final look (round 1, 2026-10-29)

Cold Final look with the real assets: 47 recorded clips (local Qwen3-TTS, voice/*.mp3), pictures drawn in code (no art
files). I read refine.md and handoff.md first. Everything settled there still holds unless listed below.
Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py snowy-mail-route`, 963 KB, and the bundler reported no missing
recordings. Muted headless Chrome on ports 9211 and 9212. A scratch iframe host served the 375 run on port 8812, so
nothing was written to the tool folder. Everything is in `S:/CurioClass-codex-scratch/final/snowy-mail-route/`:
- `audit/`: the fresh audit_tool.py run (127 leads)
- `a/`: 1366x768 with Motion on, and 680x425 with Motion off
- `b/`: 800x500, 1000x625, 1280x720, 1920x1080 and 760x900
- `c/out/`: 375x812 through the host
- `v/`: the voice runs, with full logs (`*.json`), timestamps on every clip and `show.py`
- `asr.json`: a Whisper transcript of every clip

Counts: blockers 0, should fix 3 (general 3, family 0), polish 3.

#### Should fix

1. **The Snow Town welcome holds the queue, so result lines land late and its second line plays after its moment**
   (general; wave lesson "a welcome put off past a first tap's own line lands late", `welcomeAfter: true` at
   src.html:1197 in a two-mode tool).
   - Where: src.html:1192 to 1198, the welcome lines `wTown` and `hTown`. Each has only `valid: idle`.
   - Why it matters now: with the real clips the two lines are 7.4 s and 5.9 s, so 13.3 s of talk. The queue plays
     them before any later line, and `hTown` still plays once the class has done what it asks.
   - Seen 1 (`v/v10-first-go-guess.json`, `v/w5-first-go-frame.png`): tap Star, Up, Go at 0.8 s gaps. Pip stops in
     the snow at about 4.5 s. Then "Tap a house to choose where the letter goes. Then tap the arrows..." plays from
     8.95 s to 15.0 s, with the house picked and a card already walked. "Pip stopped in the snow" comes at 15.1 s,
     about 10.5 s after the stop.
   - Seen 2 (`v/w1-burst-again.json`, `v/w3-clear-plain.json`): Clear pressed during the welcome. "All clear" waits
     behind `hTown`, 6 s late in w2 and still not played 8 s after the tap in w1 and w3.
   - Seen 3 (`v/w4-first-guess-frame.png`, `v/v4-first-guess.json`): the first tap is Guess. The hint says "Tap the
     square where you think Pip will stop." At 12.1 s the voice says "Tap a house to choose where the letter goes",
     but a house tap there would place the flag.
   - The audit confirms it: the welcome is late after the first tap on Up, Left, Right, Down, Guess, Go, Step and
     Clear (`audit/audit.md`, walk table).
   - Better: drop `welcomeAfter` (a skipped welcome comes back on the next mode entry or Sound on). Give `hTown`
     `valid: () => howNow() === 'hTown'`. Let a result line or Clear hush a welcome that has not started. Done when, at
     a 0.8 s first-tap pace, no result line plays more than about 1 s after Pip stops, and no line names a house
     while Guess is on.

2. **A level intro talks over the walk, and the bump line lands about 5 s late** (general).
   - Where: `go()` at src.html:1058 to 1068 only hushes hGuess, hFlag and hGo.
   - Seen (`v/v3-l4-go-during.json`): level 4, Go pressed 3 s into the 13.75 s intro. The intro plays on to 17.5 s,
     still saying "Press Go, then find it" while Pip walks and bumps at about 12 s. "Flump! Pip bumped into a
     snowbank" starts at 17.6 s, about 5.5 s after the bump.
   - The same thing happens on level 1 (`v/v7-l1-deliver.json`) and level 8 (`v/v8-l8-allDone.json`): the level line
     and hBuild run during the walk. Those are shorter, so the result there is under 1 s late.
   - Teachers will press Go early on fix-it levels, because the class can see the cards.
   - Better: Go also hushes a playing level intro and the build or fix how line (lv1 to lv8, hBuild, hFix, hFix6,
     hFix7, hCard), as it already does for the guess lines. The hint still shows them, and Read still says them.

3. **Take 0 (the Snow Town welcome) puts its pause in the wrong place** (general; voice).
   - Where: voice/9ceae64313f5.mp3.
   - Seen (`asr.json`): Whisper base.en and large-v3 both transcribe "Welcome to Snowtown Pip. The penguin carries the
     mail."
   - The raw take bears that out: there is no pause between "Town" and "Pip" (60 ms gap at 1.97 s), then a 0.41 s
     pause after "Pip" (2.37 to 2.78 s). So it reads as welcoming Pip, and "the penguin" loses its name.
   - It is the first line every student hears. The liveliness reading does not measure this, so it did not flag it.
   - Fix: `localvoice.py snowy-mail-route --redo 0`, then listen to the new take.
   - Every other take matches its line word for word in large-v3 or base.en (the rest of the differences were "1"
     for "one", "treehouse" and "male carrier" in base.en, and large-v3 hears "mail carrier").

#### Polish

4. **The level 4 clip only just beats the kit's hold cap** (general; kit/curio.js:83).
   - `cap = 2500 + 80 * length` gives 14.02 s for a 144-character line. The take is 13.75 s.
   - In `v/v2-l4-listen.json` it played 3683 to 17515 ms, with 170 ms to spare before hCard would have cut its tail
     ("then find it"). Not cut in any of my runs, but a slower laptop could cut it.
   - Better: the cap uses the clip's own duration when there is one. Or split lv4 into two lines, which would also
     help item 2.
   - No other clip is within 1.6 s of its cap.
5. **680x425: on a wrong-house stop, Pip and the number circle cover about half the Fish symbol**
   (`a/z-680-wrong-fish.png`; the same at 800x500, `b/800x500-town-wrong.png`). The fish is still readable, and at
   1366 and up the symbol is clear (`a/1366-town-wrong.png`). The preview size only.
6. **Arrow names go quiet while the welcome or an intro plays.** "Up!" and "Right!" are dropped as `newer` or `stale`
   (maxAge 1800) in every run that starts with arrows (`v/v1`, `v/v7`, `v/v8`). That is by design (latest only), but
   with 13 s of welcome a class tapping arrows hears nothing back. Item 1 mostly fixes this.

#### Checked and clean

- **Frames** (looked at every one):
  - Default screen, Snow Town delivered, wrong house, bank bump, Guess with the flag, Mail Route level 1, the picker,
    the level 4 bump, the level 4 footprint tap (badge on card 5 only after the tap), the level 8 finale and its end.
    All of these at 1366x768 with Motion on and at 680x425 with Motion off (`a/`).
  - Default, wrong house, level 4 bump and level 8 end at 800x500, 1000x625, 1280x720, 1920x1080 and 760x900 (`b/`).
  - Town wrong house, route delivered and Guess at 375x812 (`c/out/`).
  - The audit's size and mode frames (`audit/`).
  - No overlaps, clipping, sideways scroll or placeholders anywhere. The tray, Go and all 12 slots are in view at
    every size. The caption plate stays readable over the sky. Footprints point the way Pip stepped and are readable
    at 1366.
- **Art:** none by spec (art/prompts.json has no assets), no `art:` tokens in the bundle, and no people.
- **Targets:** 1280x720, 1366x768, 1920x1080 and 760x900 are clean at 60 px (audit). Under 60 px only at the preview
  sizes and 375, where the spec and refine.md settled a 44 px floor. Nothing is under 44.
- **Motion off:** nothing runs forever (audit `calm`). In the 680 runs the flakes stand still and the hearts show.
- **Voice, the standard checks:**
  - Five held clicks 2 s apart and two quick taps are clean on every control that speaks (audit).
  - Read speaks the hint only. Sound as the first tap says nothing.
  - A mode switch, the picker and Start over cut the line playing, as designed (`v/v9`, `v/v2`).
  - The finale sequence (Delivered, then allDone, then hAgain) plays whole with no cuts (`v/v8`).
  - Every played clip's text is in voice/lines.json. `__tool.allLines` equals lines.json, all 47 lines, and every
    line has its clip (K-2).
- **Contract:** 963 KB, under 2 MB. No console errors or exceptions in any run. No network requests from the tool:
  the resource list was empty on file://, and the 375 run fetched only the host page and its favicon. No em dashes,
  and "Curio" never appears alone in the words.
- **Solo student and teacher run:** the Snow Town free play and all eight levels through the picker play end to end.
  The finale lands warmly. The one flat or confusing stretch is the opening: 13 s of Snow Town welcome, and 15.6 s
  into Mail Route level 1 (wRoute, lv1, hBuild). The class's first actions get no voice back, and a result arrives
  late (items 1 and 2). On a projector the screen itself reads clearly.

#### Audit pilot

- **Leads confirmed:** the welcome is late after the first tap on 8 controls. That is item 1, and my runs show the
  worse effect: result lines held behind hTown.
- **Leads that were wrong or already settled:** the small-target rows at 680x425, 800x500, 1000x625 and 375 are the
  spec's 44 px floor, settled in refine.md.
- **What it missed:** a level intro running over a walk (item 2), a take's phrasing (item 3), and how close a clip is
  to the kit cap (item 4). It has no way to see lines that wait long behind the queue.

#### Re-check (2026-10-29, after final-fix.md)

I read final-fix.md as claims and checked each one on my own runs.
- Bundle: 970 KB, with the new take in.
- Ports: 9211 and 9212. The scratch host on 8812 got a copy of the new bundle.
- Output: `S:/CurioClass-codex-scratch/final/snowy-mail-route/r2/`. The voice runs are in `v/` (full logs with clip
  start, end and cut times, plus walk start and stop times). The frames are in `a/` and `b/` (the same plans as
  round 1), with contact sheets `sheet-a.png` and `sheet-b.png`, and 375 is in `c/`.
- Kit change: kit/curio.js only adds an opt-in `hold` (max of the cap and hold, never shorter).
  `python scripts/test_voice.py` gives 42 passed, 0 failed.

##### Items
1. **Fixed.** The welcome no longer holds the queue.
   - Star, Up, Go at 0.8 s (`v/f1`): the welcome is cut at Go (3278 ms), and "Pip stopped in the snow" starts at
     4385 ms, the same ms the walk stops.
   - Clear during the welcome (`v/f2`, `v/f10` burst): "All clear" starts at the tap, about 10 ms later.
   - First tap Guess (`v/f3`): only "Tap the square..." is said. Guess pressed during the welcome (`v/f4`): hTown is
     dropped as stale, and "Tap the square..." follows. No line names a house while Guess is on.
   - A plain first tap (`v/f5`) still gets wTown then hTown whole.
   - Sound as the first tap, then Sound on (`v/r7`), brings the welcome once.
   - Read cuts the welcome and speaks the hint (`v/r6`).
2. **Fixed.** Go cuts the intro, and the bump line comes at the bump.
   - Level 4, Go 3 s into the intro (`v/f6`): the intro is cut at 7656 ms (Go) and the queued hCard is dropped.
     "Flump!" starts at 13191 ms, the same ms the walk stops, and hLast follows.
   - On levels 1 and 8 (`v/f8`, `v/f9`) the intro or hBuild is cut at Go, and Delivered starts at the stop ms.
   - The level 8 finale (Delivered, allDone, hAgain) plays whole with no cuts.
3. **Fixed.** The new take reads right.
   - Whisper: base.en hears "Welcome to Snow Town. Pip, the penguin, carries the mail." and large-v3 hears
     "Welcome to Snowtown! Pip the Penguin carries the mail." Both now put the sentence break after "Town". The rest
     of the line is word for word (`r2/asr-*-0.json`).
   - The raw take bears that out: 0.30 s pause after "Town" (2.03 to 2.33 s), "Pip" from 2.33 to 2.52 s, then a
     0.34 s breath before "the penguin". It reads as a name with an appositive, not "Welcome to Snow Town, Pip".
     I did not listen myself.
   - The take is 8.03 s, inside its 10.0 s cap.
4. **Fixed.** Level 4 left alone (`v/f7`) plays 3656 to 17483 ms, uncut, then hCard plays whole.
5. **Fixed.** At 680x425 and 800x500 the Fish symbol is clear of Pip and the number circle (`r2/z-680-fish.png`,
   `r2/z-800-fish.png`). The same holds at 1366, at 375 (`r2/c/375-town-wrong.png`) and on deliveries.

##### Repeat counts (five each, real clips)
| Line | Kind | Expected | Spoken |
|---|---|---|---|
| Up! (5 taps, 2 s apart, `v/r1`) | event | 5 | 5 |
| Add an arrow card first! (Go x5 on empty, `v/r2`) | event | 5 | 5 |
| All clear (x5, `v/r4`) | event | 5 | 5 |
| Flump! bank (Go x5, `v/r3`) | event | 5 | 5, each at its walk stop |
| Wrong house (Go x5, `v/r5`) | event | 5 | 5, each at its walk stop |
| hLast, hFoot (during those runs) | how | 1 | 1 each, at the first quiet moment, dropped unmarked before then |
| wTown, hTown | welcome | 1 | 1 |

- **K-2 lines:** every fixed line has its clip. `__tool.allLines` equals voice/lines.json (47 of 47). No line text
  changed, and only take 0 was re-recorded. No played clip was cut except by Go, Step, a result, a mode or level
  switch, or Read, as designed.

##### No regression
- **Frames:** all 22 of set A (1366 with Motion on, 680 with Motion off) and all 20 of set B (800x500, 1000x625,
  1280x720, 1920x1080, 760x900) were re-shot and looked at, plus three at 375. No overlaps, clipping or controls out
  of view.
- **Console and network:** no console errors, and no network requests beyond the 375 host page and its favicon.

##### The two known items (not blocking)
- **Arrow names drop while the welcome plays:** they are latest-only events with a 1.8 s maxAge, by design. Any
  result or Clear now cuts the welcome, so nothing waits behind it. A nit.
- **Level 8 hBuild after cards are down** (`v/f9`): "Tap the arrows to make Pip's path. Then press Go" started at
  9966 ms with cards on the strip, and Go cut it at 10316 ms. Its second half is still the next action, and Go cuts
  it. A nit.

<!-- end part -->

<!-- part: final-fix.md -->

### snowy-mail-route: Final look fix (after round 2, 2026-10-29)

Bundle `CURIO_DRAFT=1 python scripts/bundle_tool.py snowy-mail-route`: 968 KB. No line text changed: `__tool.allLines()` equals voice/lines.json (47 of 47), no voice file touched. Runs, logs (clip start, end and cut times from a patched HTMLMediaElement, plus walk start and stop times) and frames are in `S:/CurioClass-codex-scratch/final/snowy-mail-route-fix/` (`v/` voice, `r/` repeats, `geo/` sizes, `c/out/` 375 through `--host`). No console errors in any run. No network requests.

1. Welcome holds the queue: removed `welcomeAfter` (two-mode tool, BUILD lesson), and `hTown` is now valid only while `howNow() === 'hTown'`. A new `hushTalk()` runs before every event line (results, Clear, empty, full): it cuts a playing welcome, level intro or how line and drops queued ones unmarked. Verified: Star, Up, Go at 0.8 s (`v/f1`): welcome cut, "Pip stopped in the snow" starts 0 ms after Pip stops. Clear during the welcome (`v/f3`): "All clear" starts at the tap. First tap Guess (`v/f4`) and Guess during the welcome (`v/f5`): hTown dropped as stale, only "Tap the square..." is said. A plain first tap (`v/f12`) still gets wTown then hTown whole. Sound off and on after a skipped welcome (`v/f11`) brings it once. Five-tap repeats (`r/`): empty 5, cleared 5, bank 5, hLast once.
2. Go does not hush an intro: Go and Step call `hushTalk()` too (replaces the hGuess/hFlag/hGo-only hush). Verified: level 4, Go 3 s into the intro (`v/f6`, frame looked at): the intro is cut at the press and "Flump!" starts at the bump (13187 ms, walk stop 13187 ms). Level 1 (`v/f8`) and level 8 (`v/f9`): intro or hBuild cut on Go, Delivered on time, the level 8 finale (Delivered, allDone, hAgain) plays whole.
3. Fish symbol covered: on a house Pip stands at +.45 s and .42 s tall (was +.37 s, .5 s), and the number circle rises beside the roof when its 10 px floor would reach the door picture. Verified by measured boxes (`geo/`): at 680x425, 800x500, 1000x625, 1366x768 and 1920x1080 neither Pip nor a number circle overlaps the symbol; frames looked at (`geo/z-680-wrong.png`, `geo/z-800-wrong.png`, delivery at 680 and 1366, 375 town wrong house in `c/out/`).
4. Level 4 clip near the cap: the kit had no per-line hold, so I added an opt-in `hold` option to `Curio.voice` say (kit/curio.js, documented in docs/KIT.md; it only lengthens the cap, default unchanged) and level 4's intro passes `hold: 17000` (cap was 14.02 s, clip 13.75 s). Verified: `python scripts/test_voice.py` 42 passed, 0 failed; level 4 left alone (`v/f7`) plays 3679 to 17512 ms uncut, then hCard.

<!-- end part -->

## Log

- 2026-11-25: refine.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/craft.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/play.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-10-28)
- 2026-11-25: handoff.md folded in (last changed 2026-10-28)
- 2026-11-25: final.md folded in (last changed 2026-10-29)
- 2026-11-25: final-fix.md folded in (last changed 2026-10-29)

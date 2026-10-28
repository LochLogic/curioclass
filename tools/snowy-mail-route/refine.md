PASS
Counts: blockers 0, should fix 10 (general 8, family 2), polish accepted 13

# snowy-mail-route: Refine

Lens files: refine/teaching.md (T), refine/play.md (P), refine/craft.md (C). Read them for frames and detail.

## Blockers
None.

## Should fix
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

## Polish accepted
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

## For Cory
- The title: keep "Snowy Mail Route" with Pip the penguin? (spec open question; the builder kept it).

## Exit check (round 1, 2026-10-28)

Cold exit check. Bundle `CURIO_DRAFT=1 python scripts/bundle_tool.py snowy-mail-route`: 135 KB. Driven in muted
headless Chrome (own profile, ports 9770 to 9778) with held clicks (0.12 s) and a speech stub paced at 30 to 70 ms per
character (browser voice, no clips yet, as expected). Frames and logs:
`C:\Users\Cory\AppData\Local\Temp\claude\S--\98b8b046-f7f2-48d0-a719-c61ce01237be\scratchpad\exit-smr` (out1 to out8,
sheet-1366.png, sheet-680.png, sheet375.png, z-l8feet.png). host.html deleted after the 375 run.

### Open
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

### Re-checked and fixed
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

### kit/robot.js against docs/families/robot.md, function by function
`program` (add, replace, move, remove, clear, load, on, ops, card, indexOf, gen, length, full, max), `run` (sequence and
rules, go, step, stop, status, busy, gen, alive with and without g, next, tick, trace, traceFor, generation guard,
finish before onEnd), `strip` (select, deselect, sel, locked, el, box, cells, setNow, setBug, pulse, lock, flash,
flip, size, place, render, card, cell, canEdit blocking card taps, keys, focus rescue) and `Robot.version`,
`Robot.last`, `Robot.trace`, `Robot.traceFor`: all match the doc. The calm rule and the picking rule match the code.
The badge rule is in the doc, but this tool breaks it (item 10). robot-dance, loop-garden, kit/curio.js and
kit/curio.css have no changes (`git status`, `git diff`). Only snowy-mail-route uses `kit:robot`.

### Recomputed (Python BFS and walk)
Shortest paths: 3, 5, 6, 6, 7, 7, 8, 8. Every listed best path is a shortest path and delivers, both in the
simulation and in the page at 1366 and at 680 with Motion off. The maps match the spec table. Starting cards:
level 4 bumps the bank on card 5 at (3,2) to (3,3), level 6 bumps the edge on card 7 at (6,3), and level 7 bumps the
bank on card 2 at (2,4) to (2,3). The fixes deliver: level 4 (card 5 to Right), level 6 (any one Right removed:
D D R R R R U) and level 7 (cards 2 and 3 swapped). In Snow Town every notes path is shortest (Fish 3, Star 4, Sun 2,
Tree 5, Moon 5, Heart 8), all six deliver in the page, and `town.delivered` lists all six.

### Frames
- Default screen and Snow Town wrong house, level 8 delivered and the picker at 680x425, 800x500, 1000x625, 1280x720,
  1366x768, 1920x1080, 760x900, plus 375x812 through --host. Tray, Go, Step, Guess and all 12 slots are on screen
  with no horizontal scroll at every size. The only target under its floor is item 24.
- Levels 1 to 8 at 1366 (Motion on) and at 680 (Motion off): each opens with the right map, cards, letter and hint.
- No console errors in any run. No network requests from the tool: the only ones were the host page and its
  favicon on the 375 run.

### Gate
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

### Nits (optional)
- After a second problem the voice says line 6 (Step) while the hint still shows the footprint or last-footprint
  line, so Read says something else. general.
- If the class presses Go while the Snow Town welcome's second line (hTown) is playing, "Tap a house..." plays on
  during the walk. general.

### Re-check of the integrator fixes (items 10 and 24, 2026-10-28)
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

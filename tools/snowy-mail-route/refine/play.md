# Play lens: snowy-mail-route

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

## Findings

### Should fix

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

### Polish

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

### Nit

10. While Pip walks, the active mode button turns a dim orange (`setOff('m-town', busy && !rt)`), which looks like a
    state change (A02). general.
11. In Snow Town the guess flag stays on the old square after a new address is picked (A11, A12). general.
12. In the compact and phone layouts the white caption runs over the sky's roofs and falling flakes (S-route8-680x425,
    P-375); readable but busy. general.

## Checked and fine

- Every level loads the spec's map; the three fix-it bugs bump at cards 5, 7 (edge) and 2; the fixes deliver;
  level 8 and the wrap to level 1 work; the dots fill.
- Go too early with an empty strip, too few cards (stopped in the snow), wrong house, bank and edge bumps all give the
  right line and frame; the bug card gets its "?" badge.
- Results, guess lines and arrow names are spoken every time; hNext, hBuild, hPaused and the level how lines are
  spoken once, then hint only; Read speaks the hint.
- Step at Quick walks one card per press and the hint names Step and Go; Stop halts at once.
- Calm mode keeps the beat timing.

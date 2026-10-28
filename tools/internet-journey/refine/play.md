# internet-journey: Play lens

Cold run, 2026-10-28. Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py internet-journey` (194 KB). Driven with
`scripts/drive.py` (port 9450-9457, own profile), held clicks for voice, `__tool.timeScale` only for reaching frames.
Browser voice, art as it stands (not judged).

Played twice: (1) as a grade 3 student alone at home, Sound on, reading little, tapping fast; (2) as a teacher
projecting at 1366x768 and 1920x1080, pausing at each stop for a class vote.

## Frames looked at

- 1366x768, Story, every stop in an all-A run and an all-B run: stop 1 empty, 1 picked, 1 sent, 2 to 6 at choose and
  at Next, 7 ending (E1 and E2).
- Sizes, all-B run at stop 1, 4 (Next), 6 (Next), 7: 680x425, 800x500, 1000x625, 1280x720, 1920x1080, 760x900 (stack),
  520x900 (stack); 375x812 via `--host` at stop 1, 1 picked, 3, 6, 7 and Trip map.
- Trip map at 1366: default, a stop picked, a test mid-flight, test landed, test with Close a road; plus 680x425,
  760x900, 520x900, 1920x1080 with a stop picked and a landed test.
- Calm mode at stop 4 (A, bounce), keyboard only from load through Send, Next and the stop 2 cards (focus ring frame).
- Voice logs: first taps (stage, a card, Read, Sound off/on, Trip map), a full real-time all-A run with 11 s gaps, two
  runs back to back (Try other choices), a fast tapper run (card about 2 s after each stop opens, Next as soon as it
  shows), fast taps then mode switch and Start over, Read during a line, Trip map Send a test five times and Close a road.
- Console: clean in every shot (the only entry was the host page's favicon 404).

## What works

The story idea lands: the invite card fills in as you pick, then turns into 8 numbered chips; the "open" or lock
badge stays on your router, Router A gets its X, the server gets "copy", the 12 phones appear for 6B, and the slots
fill 1, 3, 5, 7, 2, 4, 6, 8 before "Juno sees" reads the whole invite. The board is a clear payoff and the two runs
(all safe, all risky) compare well on a projector. Keyboard: focus starts on the first card, Enter picks, focus moves
to Next and then to the new cards, the ring is visible. At an unhurried pace (11 s per action) every chapter line,
result and ending is spoken in order and "Press Next" is spoken once then only shown, as the rules ask.

## Findings

### Should fix

1. **A student who taps at a normal pace loses most of the story's narration.** (Story, stops 2 to 6; general)
   Seen in the fast-tapper voice log (card about 2 s after the stop opens, Next as soon as it shows): stop 2's and stop
   3's chapter text were `dropped`; the results of stops 3, 4, 5 and 6 were all `dropped`; stop 2's result ("Your
   pieces made it. On an open network...") was still playing during stop 3 while the pop-up was on screen. Cause: the
   chapter text and the result queue behind whatever is playing, Next appears before the result has started, and Next
   drops the queued result without cutting the line still playing. For a non-reader the consequences ("That is a copy
   you can't take back", "Juno shared it with 12 phones") are the lesson, and they vanish. Better: the result line cuts
   in when a card is picked (`V.say(..., {now: true})`, which the kit supports), and Next cuts the playing line and
   starts the new chapter at once; or Next shows only after the result has been spoken (with Sound on).
2. **Stop 1's story text is never spoken, and nothing says "press Send".** (Story, stop 1; general)
   First-tap logs: `ch1` is logged `silent` at load (before any tap) and the first tap plays only the welcome. Nothing
   after that ever speaks "You are inviting your friend Juno to your party..." unless the student presses Read. The
   Send how-to ("Pick a card for Place, Extra and Photo. Then press Send.") is hint-only. A solo child who cannot read
   picks three cards and then waits at a pale yellow button nobody named. Better: after the welcome, speak stop 1's
   text once; when the third pick is made, speak the Send how-to once (V.how, needs `#send`).
3. **E3 says the wrong thing for "no private cards, but Juno shared it".** (Stop 7; general)
   All-A cards with 6B (also 3A, 5A) gives E3: "Some private details went along, but only to people you know." In that
   run no private detail went anywhere, and the invite went to 12 phones of kids you don't know (the board shows that
   row). Words don't match the state (POLISH, Consistency). The builder flagged it in handoff.md. Better: a fourth
   ending for this case (no private details, but the invite spread further than you chose), or route it to a line that
   says exactly that.
4. **Trip map: the envelope (the "outside address, locked inside" idea) cannot be found.** (Trip map; general)
   Neither the hint ("Tap any stop to see what it does, or press Send a test."), the stop card's empty text, nor any
   spoken line mentions tapping a moving piece, and at the default Quick speed a piece crosses a hop in 0.4 s. In my
   map frames I never saw the envelope card without calling it from code. Better: after the first test lands, the hint
   (and one how line) says "Press Send a test again and tap a moving piece to see its envelope"; consider Slow as the
   default for this mode, or keep the last piece of each test resting at Juno's tablet as a tappable envelope.
5. **"Juno sees" covers "Juno's internet provider" on narrow and preview boxes.** (Story stops 6 and 7; family:network)
   At 680x425 (the tool page preview) the bubble hides "provider"; at 760 and 375 wide it cuts the label to "Juno's
   internet" or "Juno's". Frames sz680x425-c6-next, sz760x900-c6-next, h375-c6-next. Better: place the bubble where
   it clears node labels (over the slot strip column, or above the phones), or drop it to the panel in compact and
   stack layouts.

### Polish

6. **Ending board: the map ghosts through.** (Stop 7, every wide and compact size; general) The board is 97 percent
   opaque; the "Juno sees" bubble, the slot numbers and node labels show through behind the rows (pixel check: 48,43,72
   over the bubble vs 31,26,59 board). It reads as clutter behind the most important screen. Better: fully opaque, or
   dim and hide the right half of the map under it.
7. **Ending board cuts the server tile in half.** (Stop 7, 1366 and 1280; family:network) The board's left edge runs
   through "The message app's server" ("The me... app's"). Better: pan or shrink the map into the left half so the
   remaining stops are whole, or lay the board over the right of the server.
8. **The ending's count line and Try other choices fall below the fold.** (Stop 7; general) At 680x425 the count line
   ("Your invite is on 15 devices...") needs scrolling inside the board; in stack layouts (760, 520, 375) Try other
   choices sits under the full board, about 600 px down. The count is the punch line and Try other choices is the next
   action the voice names. Better: count line at the top of the board in compact; in stack, the buttons above the
   board or sticky at the bottom.
9. **Stop 4 is a choice nobody would make.** (Stop 4; general) "Take the closed road anyway" vs "Take the open road
   through Router B": the student steers like a router, then result B says "Routers found another way", which the
   student did, not the routers. It plays as a trick question and the moment is flat. Better: make the student the
   watcher ("Wait and see what the routers do" vs a second, real-feeling option), or let the routers pick and ask the
   student to predict which road (then show it).
10. **Stop 5 has no picture of its consequence.** (Stop 5; family:network) Every other choice leaves a mark on the
    map (open/lock badge, pop-up stamp, Router A X, 12 phones); "Everyone on the app" changes nothing you can see
    until the board. Better: a small badge on the server ("profile: everyone" with a globe, or a lock for friends).
11. **Trail dots draw over the tiles.** (Every stop after 2, Trip map; family:network) The gold trail dots run across
    the faces of Router A, the server, the ISPs and Router D (zoom of stop 5). Better: clip the trail at the tile
    edges, or draw it under the tiles.
12. **The map stays small on a projector.** (1920x1080; family:network) Icons stay 44 px and labels 14 px while the
    stage is 1560 px wide, so the class sees a sparse map with small names; the panel story text is 17 px. Better: let
    icon and label size grow a step on big boxes (for example 56 px icons and 17 px labels above about 1400 px of
    stage), and a larger story font in wide layouts.
13. **Stack layout: the invite card is below Send.** (Stop 1 at 760, 520, 375; general) On a phone or narrow window the
    message that fills in as you pick sits under Send and the hint, off screen, so the "watch your invite build" moment
    is lost. At 760x900 the header also wraps Read onto its own row, which pushes Send to the fold. Better: the invite
    card right under the cards (above Send), and keep the header on one row at 760.
14. **1366x768: the hint under Next is cut at the bottom edge.** (Stop 1 after Send; general) "Press Next to send the
    pieces on to the next stop" loses its last word at the window edge and Start over is below it (frame A-c1-next).
    Better: drop the picked ch1 cards to one compact row after Send in wide layout too, as the other layouts do.

### Nit

15. The pop-up's ✕ looks tappable but does nothing (stop 3). Tapping it could pick "Close it and tell a grown-up", or
    draw it as plain text. (general)
16. The "copy" badge on the server is crossed by the line to Router C. (stop 5 on; family:network)
17. A closed Router A's label turns a dim violet on the dark sky, noticeably harder to read than the others.
    (stop 4 on, Trip map with Close a road; family:network)
18. The soccer group row's icon (three phones) reads as a folded map at 30 px. (stop 7; general)

## Counts

Blocker 0, should fix 5, polish 9, nit 4.

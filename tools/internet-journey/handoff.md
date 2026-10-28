# internet-journey: build handoff

Built 2026-10-27 (wave BR1), the first tool of the network family. New files: this folder's src.html,
tool.draft.json, notes.md, voice/lines.json (29 lines; 34 after Refine round 1), handoff.md; `kit/network.js` (the engine);
`docs/families/network.md`. No existing kit file was changed. Art (ij-dusk-town, ij-server-hall) was already in
art/ from the art pass; review is still "pending" in art/prompts.json.

## What it is

Story (7 stops, one two-card choice each) follows a party invite cut into 8 numbered envelopes from your tablet to
Juno's, then the **Where copies live** board. Trip map lets you tap any stop, send a "Hello Juno!" test (odd pieces by
Router C, even by Router D, so they land out of order), close Router A and watch the test reroute through Router B,
and tap a moving envelope to see its outside (To, From, Piece n of 8) with the words locked.

## src.html layout

- CSS: palette per spec, three page layouts like collision-lab (`wide` w>=1000 and h>=700, `compact` w>=600 and
  w/h>=1.25, `stack`). The panel is first in the DOM (tab order); the grid puts the stage left.
- Line table `L` (every spoken line), `PAIRS1` (chapter 1 Place, Extra, Photo), `CH` (chapters 2 to 6 cards and
  results), `STOPS` (Trip map stop cards), the two graphs (`gStory`, `gMap`, 11 stops, rA..rD).
- State: `mode, ch, phase (intro|choose|moving|next|end), choices, step1, pieces, flying, trail, copy, map{...}, ui{...}`.
- `relayout()` sizes the svg at real pixels; when the map would scale below 0.72 it is windowed (scale 0.86, 0.8 under
  520 px) and pans to the current stop (`panFor`, `setPan`, Left/Right buttons in the Trip map panel, drag, focus).
- `renderStage()` badges, ring, gold trail, piece stacks with a count badge, slots, "Juno sees" bubble, phones (6B).
- Story beats: `openChapter(ch)` then `choose(ch, pick)` then `afterChoice` moves pieces (`moveAll`, `fly`,
  `travel6`); `next()`; `ending()` builds the board rows and the who block, and picks E1, E2, E3 or E4.
- Trip map: `pickStop`, `sendTest` (routes from `Net.path`, so Close a road reroutes for real), `showEnvelope`.
- `window.__tool`: `state, net, setMode, choose, ending, allLines, vlog, vq, gStory, gMap, L, openChapter, startOver,
  sendTest, pickStop, next, send, timeScale(k), layout, hint`. `timeScale` is a test hook (all story timers scale).

## Engine API (kit/network.js, global `Net`)

Full list in docs/families/network.md. Pure: `graph, addNode, addLink, removeNode, removeLink, key, path (by ms|hops,
skip, avoid; ties fewer hops then lower index), cost, reach, flows, around, split, join, step, KINDS, DEVICES`. DOM:
`draw(svg, g, skin) -> view` (pos, linkPoints, nodeEl, linkEl, update, badge, ring, setPickable, focus, labelBox,
layers), `icon, token, place, send (arrived|dropped|bounced|stopped, onDown 'bounce'), stop, ICONS`. Checked in Node:
the spec's routing examples (Town and City maps, with and without a down router) give the expected paths.

## Checks (Done when, round 0 build)

1. All A: E1, 3 rows, "Your invite is on 3 devices.", no chips. PASS.
2. Place B + 3B + 6B: E2, soccer group row, pop-up website row, address chip on every invite row, "15 devices and one
   website you don't know". PASS.
3. Chapter 4 A bounces at Router A and arrives later; Router A stays closed (X badge) to the end. PASS, but at the
   Story's slow speed A finishes 2.7 s after B (6.98 s vs 4.24 s), a bit more than "about 2 s".
4. Chapter 6 lands 1, 3, 5, 7, 2, 4, 6, 8 into numbered slots; "Juno sees" reads the whole invite from chapter 1. PASS.
5. Trip map stop cards per Content; Send a test lands 8; with Close a road the route goes through Router B and
   `__tool.net.path` agrees. PASS.
6. Voice: welcome once; chapter and result lines each time; Next's how line through `V.how` (once, then shown only);
   Read speaks the chapter text. PASS (log checked on a held-click run).
7. Sizes: 1920, 1366, 1280, 1000x625, 800x500, 760 stack, 680x425 compact, 375 via `--host`. Cards and Next visible
   without scrolling in compact; map labels 14 px (13 under 520). PASS.
8. Motion off + keyboard only (Tab, Enter) from chapter 1 to the ending and Try other choices: PASS. Console clean
   in every shot; no fetch or storage in the code; the name appears only as "Curio Class". PASS.

## Refine round 1 (2026-10-28): what changed

Items as numbered in refine.md.

1. **Endings.** New E4 for "no private detail, but 6B" ("...then 12 phones of kids you don't know. No private
   details went along this time, but copies can't be taken back. Ask before a message is shared."). E3 now says "only
   to Juno and the app's server". Rule order in `ending()`: E2 (chips and 6B, or 3B, or 5B), else E4 (6B), else E3
   (any chip), else E1. All 256 runs are in the table below.
2. **Narration at a 2 s pace.** A chapter change drops only queued how-to lines. Story lines (results, the look-up,
   Juno's question) are never cut: the chapter line waits behind them. Next shows only after the result has been
   heard (Sound on; cap 30 s of real time). Next does cut a "Press Next" line that is still playing. Checked on three
   real-time runs, tapping every 2 s: every chapter line, result, look-up, question and ending line was spoken (see
   below).
3. **ch1 and Send.** ch1 is spoken after the welcome, as a welcome entry. It is valid only while stop 1 is waiting
   for choices, so it is dropped (stale) if Send comes first. The Send how-to is a `V.how`, said once, when all three
   parts are picked.
4. **Welcome and hint.** The welcome and ch1 use `hint: false`, so the hint keeps "Pick a card...".
5. **Open badge.** It sits on its own node: Free_Fast_WiFi (an access point under your Wi-Fi router, shown from stop 2).
   2A puts a lock badge on your Wi-Fi router, 2B the red "open" badge on Free_Fast_WiFi, and the pieces' route
   follows the pick.
6. **Look-up beat.** Stop 6 adds "A map website" under Juno's tablet: a "?" piece goes out, an envelope comes back,
   then "Juno looks up the way..." and Juno's question. Packets-first for grade 3 is in the spec's Open questions.
7. **The board names who was touched.** You and Juno, each with a good thing it did ("reached Juno in seconds",
   "read it now or later, and come to your party"); your family (where the home address went); and the soccer kids if
   6B (a risk). notes.md asks "Who did this app touch? Name one good thing it did and one risk."
8. **Private tags.** No private tags before Send. After Send, "What this message gives away" lists each private
   detail (or "Nothing private"). The spec has a "Refine changes (round 1)" line.
9. **Mode switch.** It stops every mover and clears `state.flying`. Checked: switching to Story mid-test leaves 0
   tokens.
10. **Moving envelopes.** `Net.token(..., {onPick})` adds a 48 px hit circle, picks on pointerdown, is a tab stop
    (role button) and answers Enter and Space. Trip map says "Press Send a test again, and tap a moving piece to look
    inside it." once, after the first test. Checked: a real held click on a moving piece opens its envelope. Tab
    reaches the pieces after the 11 stops, and Enter opens one.
11. **badge() and tab order.** A redrawn node replaces the old one in place and keeps keyboard focus. An unchanged
    badge is not redrawn. Checked: Tab walks the 11 stops in order during a test, then reaches the pieces.
12. **labelBox.** Added to the engine (`view.labelBox(id)`). Every function in docs/families/network.md exists in
    `Net` (checked in Node).
13. **No focus move on load.** Focus moves only when it was already in the panel (Next hid, a card was disabled).
14. **"Juno sees".** It is on the stage only in the wide layout. In compact and stack it is a panel box under the
    result, so it covers no label at 680x425, 760 or 375.
15. **Hint and ending.** Event lines never write the hint. The Trip map hint names the next step: tap a moving piece,
    or close a road. The ending text shows once (story text only, no result line).
16. **Back to Story.** Returning to Story retells the chapter line (Juno's question at stop 6) while it waits for a
    choice. Checked: Story, Trip map, Story speaks ch1 again.
17. **4A.** The 4A result is said at the bounce.
18. **Contrast.** The invite blanks and the pop-up fields use --muted (#5e5470 on white, about 7:1).
19. **Board.** The board is opaque (#1f1b3a). Its left edge starts right of the server tile, or it goes full width
    when narrow.
20. **Count and Try other choices.** The count line is at the top of the board. Try other choices sits in the
    panel; measured in view at 680x425 (229-277), 800x500, 760 and 375.
21. **Stop 5 mark.** From stop 5 the server shows a "copy" badge (left side): with a lock for 5A ("copy, friends"),
    red and open for 5B ("copy, everyone"). It is hidden under the board at stop 7.
22. **Trail and big screens.** The trail is drawn under the tiles. At 1400x640 and up, icons are 54 px and labels
    17 px (1920 frames).
23. **1366.** The hint under Next is in full (Next 540-596 at stop 6, hint under it).
24. **Card sides and ch4.** The safe card alternates sides (left for place, photo, 3 and 5; right for extra, 2, 4
    and 6). Stop 4 asks "What will the routers do with pieces 5 to 8?" (A: "Wait for Router A to open again.",
    B: "Find another road.").

**Nits.**
- The pop-up has a 44 px close button (it counts as 3A).
- The copy badge is item 21.
- A closed router's name uses colors.downLabel (#d4cde6).
- The svg is no longer an empty Tab stop.
- `send(..., {keep})` marks a token that `Net.stop` keeps.
- colors.ring and labelHaloWidth are documented.
- The tie rule now reads "fewer hops, then the lower node index" in both the spec and the doc.
- The invite always ends with a period.
- The envelope reads "To: Juno, through the message app".
- The soccer row icon is one phone with a "12" badge.

**Also changed while re-shooting.**
- On compact and stack pages, stop 6 shows only Juno's question once the look-up is done. The voice and Read keep
  the full text. This keeps Next in view at 680x425 and 800x500.
- At 561 to 999 px wide, the stack header stays on one row.
- On a stacked page, Send, Next and Try other choices scroll into view when they appear.
- The map website's height comes from the row gap, and its name sits on its left, so it clears Juno's tablet at
  every size.
- The engine draws rings under the tiles, so badges are not crossed by the ring (layer order back, links, marks,
  nodes, ...).
- The Trip map speed starts at Slow.
- voice/lines.json was regenerated from `__tool.allLines()` (34 lines; voice Algieba and its style kept).

### All 256 runs

The ending depends on place, extra, photo, 3, 5 and 6. Stops 2 and 4 never change it, so each row shows the four
runs for 2A/2B and 4A/4B. Totals: E1 4, E2 220, E3 28, E4 4. E1 needs every chapter 1 card A plus 3A, 5A and 6A.
E4 is the same with 6B.

| place extra photo | 3 | 5 | 6 | 2A 4A | 2A 4B | 2B 4A | 2B 4B |
|---|---|---|---|---|---|---|---|
| A A A | A | A | A | E1 | E1 | E1 | E1 |
| A A A | A | A | B | E4 | E4 | E4 | E4 |
| A A A | A | B | A | E2 | E2 | E2 | E2 |
| A A A | A | B | B | E2 | E2 | E2 | E2 |
| A A A | B | A | A | E2 | E2 | E2 | E2 |
| A A A | B | A | B | E2 | E2 | E2 | E2 |
| A A A | B | B | A | E2 | E2 | E2 | E2 |
| A A A | B | B | B | E2 | E2 | E2 | E2 |
| A A B | A | A | A | E3 | E3 | E3 | E3 |
| A A B | A | A | B | E2 | E2 | E2 | E2 |
| A A B | A | B | A | E2 | E2 | E2 | E2 |
| A A B | A | B | B | E2 | E2 | E2 | E2 |
| A A B | B | A | A | E2 | E2 | E2 | E2 |
| A A B | B | A | B | E2 | E2 | E2 | E2 |
| A A B | B | B | A | E2 | E2 | E2 | E2 |
| A A B | B | B | B | E2 | E2 | E2 | E2 |
| A B A | A | A | A | E3 | E3 | E3 | E3 |
| A B A | A | A | B | E2 | E2 | E2 | E2 |
| A B A | A | B | A | E2 | E2 | E2 | E2 |
| A B A | A | B | B | E2 | E2 | E2 | E2 |
| A B A | B | A | A | E2 | E2 | E2 | E2 |
| A B A | B | A | B | E2 | E2 | E2 | E2 |
| A B A | B | B | A | E2 | E2 | E2 | E2 |
| A B A | B | B | B | E2 | E2 | E2 | E2 |
| A B B | A | A | A | E3 | E3 | E3 | E3 |
| A B B | A | A | B | E2 | E2 | E2 | E2 |
| A B B | A | B | A | E2 | E2 | E2 | E2 |
| A B B | A | B | B | E2 | E2 | E2 | E2 |
| A B B | B | A | A | E2 | E2 | E2 | E2 |
| A B B | B | A | B | E2 | E2 | E2 | E2 |
| A B B | B | B | A | E2 | E2 | E2 | E2 |
| A B B | B | B | B | E2 | E2 | E2 | E2 |
| B A A | A | A | A | E3 | E3 | E3 | E3 |
| B A A | A | A | B | E2 | E2 | E2 | E2 |
| B A A | A | B | A | E2 | E2 | E2 | E2 |
| B A A | A | B | B | E2 | E2 | E2 | E2 |
| B A A | B | A | A | E2 | E2 | E2 | E2 |
| B A A | B | A | B | E2 | E2 | E2 | E2 |
| B A A | B | B | A | E2 | E2 | E2 | E2 |
| B A A | B | B | B | E2 | E2 | E2 | E2 |
| B A B | A | A | A | E3 | E3 | E3 | E3 |
| B A B | A | A | B | E2 | E2 | E2 | E2 |
| B A B | A | B | A | E2 | E2 | E2 | E2 |
| B A B | A | B | B | E2 | E2 | E2 | E2 |
| B A B | B | A | A | E2 | E2 | E2 | E2 |
| B A B | B | A | B | E2 | E2 | E2 | E2 |
| B A B | B | B | A | E2 | E2 | E2 | E2 |
| B A B | B | B | B | E2 | E2 | E2 | E2 |
| B B A | A | A | A | E3 | E3 | E3 | E3 |
| B B A | A | A | B | E2 | E2 | E2 | E2 |
| B B A | A | B | A | E2 | E2 | E2 | E2 |
| B B A | A | B | B | E2 | E2 | E2 | E2 |
| B B A | B | A | A | E2 | E2 | E2 | E2 |
| B B A | B | A | B | E2 | E2 | E2 | E2 |
| B B A | B | B | A | E2 | E2 | E2 | E2 |
| B B A | B | B | B | E2 | E2 | E2 | E2 |
| B B B | A | A | A | E3 | E3 | E3 | E3 |
| B B B | A | A | B | E2 | E2 | E2 | E2 |
| B B B | A | B | A | E2 | E2 | E2 | E2 |
| B B B | A | B | B | E2 | E2 | E2 | E2 |
| B B B | B | A | A | E2 | E2 | E2 | E2 |
| B B B | B | A | B | E2 | E2 | E2 | E2 |
| B B B | B | B | A | E2 | E2 | E2 | E2 |
| B B B | B | B | B | E2 | E2 | E2 | E2 |

### Voice at a 2 s pace (real time, Sound on, held first tap)

Three runs: all A; B B B, 2B, 3A, 4B, 5B, 6B; A B A, 2A, 3B, 4A, 5A, 6B. Each spoke:
- welcome once;
- ch1 dropped as stale, because Send came 6 s in, before the welcome ended;
- the stop 1 result;
- "Press Next" once, then silent;
- ch2 to ch6, each result, the look-up and Juno's question;
- the ending.

Nothing was dropped except the stale ch1 and the Send how-to, whose moment had passed. Order always followed the
taps; the result is heard before Next shows.

First taps on fresh pages:
- stage: welcome at 0.14 s, then ch1;
- Read: the hint only;
- Trip map: its welcome;
- Sound off then on: the welcome once, then ch1;
- Story, Trip map, Story: ch1 retold.

## Checks after Refine round 1

- Frames at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x900: stops 1, 1 sent, 2, 4 and 6,
  and the end.
- 375 via `--host`: start, stop 1, stop 2, stop 6, the end and Trip map. No horizontal scroll (scrollWidth 375). The
  host server was stopped and host.html deleted.
- Send, Next and Try other choices are in view at every size. At 760 the page scrolls them into view.
- Trip map: pointer pick on a moving piece, keyboard pick, and a closed-road test that lands 8 via Router B.
- Motion off and keyboard only: 6 Tabs to the first card, then Enter through every stop to E4. Focus lands on Try
  other choices.
- Console clean in every shot. The only error was the host page's own favicon 404.

## Refine round 2 (2026-10-28): what changed

25. **Free_Fast_WiFi at short sizes (regression from item 5).** Rows closer than 100 px (680x425, 375) put the hotspot
    above your Wi-Fi router, at a distance worked out from the row gap. Its name goes on its right and its "open"
    badge on its left. Taller stages keep it below (760, 800x500 and up, as before). Checked at 680x425 and at 375:
    "Your Wi-Fi router", "Your internet provider", "Free_Fast_WiFi" and the badge all read in full.
26. **Check circle.** A picked card's text keeps 10 px clear of the check circle. "Home Wi-Fi" uses a non-breaking
    hyphen, so at 1920 it wraps as "Home / Wi-Fi", never "Wi- / Fi".
27. **680x425 after Send.** On compact pages the pieces card is tighter (full stage width, smaller padding and note):
    62 to 191 px, clear of the Your tablet tile (top 223). Only the stack's count circle touches its bottom edge.
28. **Server stack at 5B.** The server's piece stack moved to the tile's top right corner, clear of the
    "copy, everyone" badge (800x500 and every other size).
29. **Spec.** The Refine changes line now says "What this message gives away", records the Your tablet stop card
    sentence, and notes items 25 and 30.
30. **4A timing.** Each 4A piece goes on by Router B as soon as it bounces back. Measured at real speed: 4A 6.24 s,
    4B 4.19 s, so A lands 2.06 s later.

No engine change in round 2 (kit/network.js untouched since round 1; the label function and badge side were already
there). Frames: stop 2 (A and B) at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x900, and at
375 via `--host`; stop 1 after Send and stop 5B at every size and at 375. Console clean except the host page's
favicon 404. The host server is stopped and host.html deleted.

## Known gaps and judgement calls

- A student who taps Send before the welcome ends never hears ch1 (it is stale by then; the text is on screen).
- At a fast pace, stop 6's cards are active before Juno's question is spoken. The question still plays before the
  result.
- Keyboard users reach the moving pieces after the 11 stops (about 16 Tabs). At Slow the test lasts long enough.
- **E2 includes 5B** (profile seen by everyone) as a "stranger" copy (spec open question, kept).
- **Narrow chapter 1** (stack under 560 px, or compact under 450 px tall) shows one pair at a time with a Place,
  Extra, Photo stepper.
- **Stack layout** shows the invite, pop-up and copies board inside the panel instead of over the map.
- Trip map Quick lands in the order the routes give (1, 3, 5, 2, 7, 4, 6, 8), not the story's scripted order.
- At 375 the three kit buttons show their icon only (accessible names intact).
- Voice: `scripts/voice.py internet-journey` not run (BUILD.md: do not record). The headless voice check used the
  browser fallback voice, so clip lengths will differ a little.

## For Cory

- Art review for the two FLUX.1 [schnell] images is still pending (credit added to tool.draft.json sources).
- Nothing else needs a decision.

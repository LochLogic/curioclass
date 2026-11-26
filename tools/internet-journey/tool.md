# Internet Journey: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Refine

<!-- part: refine.md -->

PASS (round 2 re-check: item 25 fixed, polish 26 to 28 and nits 29 and 30 done, no regressions; new polish 31 noted, not gating)
Counts: blockers 1 (general 1, family 0), should fix 13 (general 10, family 3), polish accepted 10

### internet-journey: Refine

Lens files: refine/teaching.md (T), refine/play.md (P), refine/craft.md (C). Each item names its source; read the
lens file for frames and detail. Settled with BASELINE where lenses or spec left a call.

#### Blockers
1. **Wrong ending line for the "no private details, invite spread" runs** (T-B1, C-S7, P-S3; general). All safe cards
   except 6B (and the other 3 runs T found) end on E3, "Some private details went along, but only to people you know";
   both halves are false. Add a fourth ending (no private details went anywhere, but the invite reached 12 phones of
   kids you don't know), with its own spoken line in voice/lines.json and allLines(). Re-run all 256 combinations and
   list which ending each gets in handoff.md. Also fix T-P3: E3 must not say "only to people you know" while the board
   shows the detail on the app's server.

#### Should fix
2. **Narration lost at a normal pace** (P-S1; general). Results queue behind the playing line and Next drops them.
   Speak the result as soon as a card is picked (cut in), let Next cut the old line, and keep Next from dropping the
   result. Re-run the voice check at a 2 s tap pace: every chapter and result line heard.
3. **Stop 1 story line never spoken; "press Send" never spoken** (C-S1, P-S2; general). Re-queue chapter 1 after the
   first tap and speak the Send how-to once.
4. **Story welcome replaces the panel hint** (C-S2; general). The hint must keep naming the next action (Send); Read
   speaks the hint, not the welcome.
5. **Picking Free_Fast_WiFi marks your home router "open"** (T-S1; general). Put the open badge on a separate public
   hotspot node the pieces go through, not on "Your Wi-Fi router".
6. **E3-SYS-NT-14 half taught** (T-S2; general, rule 2). Add a short look-up beat inside the story (for example Juno
   looks up the way to the park: a request goes to a server and the answer comes back on the map), using the engine.
   Keep it one stop, inside the spec's scope. The packets-first question goes to the spec's open questions.
7. **E3-SYS-IM-15 partly taught** (T-S3; general, rule 2). The ending board names who the choices touched (you, Juno,
   your family, the soccer kids) and one benefit (the invite arrived in seconds), with one discussion question in the
   teacher notes.
8. **Private tags give the answer away** (T-S4; general, rule 2 "evaluate"). Settled with BASELINE (standards taught
   well): no red "private" tags before Send; after Send, the card shows what the message gave away, the school-shirt
   photo included. Note the change in the spec under a "Refine changes" line.
9. **Trip map pieces stay "in flight" after switching to Story** (C-S3; general). Clear them on mode switch; the stack
   shows 8.
10. **Moving envelopes can't be tapped or reached by keyboard, and nothing says you can** (C-S4, P-S4; family:network).
    Hit on press (pointerdown) with a target of at least 44 px around the token, make each moving token focusable (or
    a "Look inside a piece" button that pauses the nearest one), and say it once in the Trip map how-to.
11. **badge() re-adds the node at the end, breaking tab order** (C-S5; family:network). Fix in kit/network.js.
12. **Family doc lists view.labelBox(id), which the engine lacks** (C-S6; family:network). Add it or remove it from
    docs/families/network.md; check every documented function exists.
13. **Focus jumps to the first card on load** (C-S8; general). No focus move on load; first Tab lands on the header.
14. **"Juno sees" bubble covers "Juno's internet provider"** (P-S5; general). At 680x425, 760 and 375.

#### Polish accepted
15. The landed line and the ending line overwrite the hint; the Trip map hint keeps naming a next step, and the
    ending text shows once (C-P1).
16. Coming back to Story retells the cut chapter line (C-P2).
17. 4A's result line is spoken when the bounce happens, not 7 s before (C-P3).
18. AA contrast for the invite's blanks and the pop-up's fields (C-P4).
19. The map no longer shows through the ending board; the board doesn't cut the server tile (P, polish 1-2; C-N4).
20. Device-count line and Try other choices visible without scrolling on small and stacked screens (P polish).
21. Stop 5's choice leaves a mark on the map (P polish).
22. Trail dots draw under the tiles; map icons and labels larger at 1920 (P polish).
23. At 1366x768 the hint under Next is not cut off (P polish).
24. Safe card not always on the left (T-P2); chapter 4 framed as a prediction of the routers' road (T-P1).

Nits are optional (lens files): fix the cheap ones (pop-up close button, "copy" badge, closed router label, empty
stage Tab stop, Net.stop keep option, colors.ring in the doc, the tie rule worded the same in spec and doc, the
missing period, the envelope's "To:" line).

#### For the spec's open questions
- Packets and routing are middle school in CSTA's notes (T-S2): should grade 3 stay packets-first? Not blocking.
- 5B counted as a stranger copy for E2 (builder's reading); stays.

#### Exit check (round 1)

Fresh cold agent, 2026-10-28. Bundled with `CURIO_DRAFT=1 python scripts/bundle_tool.py internet-journey` (209 KB;
voice clips not recorded yet, browser voice, as expected). Driven in muted headless Chrome on my own profile and ports
9580-9584 (`scripts/drive.py` plus a small held-click harness with a timed stand-in for speechSynthesis, about 60 ms a
character). Frames: default, Trip map, stops 1 (picked, sent), 2B, 3, 3B, 4A, 5B, 6, 6B and all four endings at
680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x900, and nine frames at 375 via `--host` (host.html
deleted after).

##### The merged list, re-checked
1. Endings: PASS. All 256 runs through `__tool.ending()` match the spec rules recomputed in Python (E1 4, E2 220, E3 28,
   E4 4; counts and count lines right). E3 rows are only your tablet, the server and Juno's tablet, so "only to Juno and
   the app's server" is true. E4 line and voice/lines.json entry present.
2. Narration at a 2 s pace: PASS. Three real-time runs (all A; all B with 3A, 4B; mixed with 3B, 4A, 6B): every chapter
   line, every result, the look-up, Juno's question and the ending spoken, in order; Next appears after the result.
3. ch1 and Send: PASS. ch1 follows the welcome; the Send how-to is spoken once on a patient run and dropped (newer) when
   Send comes first.
4. Welcome and hint: PASS. The hint keeps "Pick a card for Place, Extra and Photo. Then press Send."
5. Open badge: PASS in logic (badge on Free_Fast_WiFi, lock on your router, route follows the pick), but see new item 25.
6. Look-up beat: PASS. Map website shows, "?" piece out, envelope back, line spoken; spec and open question updated.
7. Who it touched: PASS. You, Juno (good), your family (address line right in every case), soccer kids if 6B; notes ask
   the question.
8. No private tags before Send: PASS; "What this message gives away" after Send (frame ch1sent).
9. Mode switch: PASS. Switching to Story mid-test leaves 0 tokens and an empty flying set.
10. Moving envelopes: PASS. A real held click on a moving piece opens "Piece 1 of 8" with To/From and the lock line;
    pieces are tab stops; the peek how-to is said once.
11. badge() tab order: PASS (node replaced in place, unchanged badge not redrawn; code read).
12. labelBox: PASS. Every function named in docs/families/network.md exists in Net or the view.
13. Focus on load: PASS (activeElement is BODY; Tab 1 is the Story button).
14. "Juno sees": PASS. On the stage only in wide; in the panel at 680x425, 760 and 375.
15-24. PASS: hint not overwritten by events, chapter retold on return to Story, 4A said at the bounce, contrast (muted on
    cream 6.64:1, on white 7.05:1), board opaque, count and Try other choices in view at every size, stop 5 copy badge,
    trail under tiles and larger icons at 1920, 1366 hint in full, safe card alternates and ch4 is a prediction.

##### New items
25. **should fix, general (regression from item 5).** Stop 2 at 680x425 (the tool page preview) and at 375: the
    Free_Fast_WiFi tile sits on the "Your Wi-Fi router" label (only "Your Wi" shows) and its red "open" badge covers the
    start of "Your internet provider". Frames ch2B-680x425, h-ch2B (375). Fine at 760, 800x500 and up. Better: place
    the hotspot from the row gap the way the map website is placed, or put its badge on the left.
26. polish, general. The picked card's check circle covers the last letters of "Free_Fast_WiFi" (680 to 1366); at
    1920 "Home Wi-Fi" wraps as "Wi- / Fi". Frame ch2B-1280x720.
27. polish, general. 680x425 after Send: the "Cut into 8 numbered pieces" card covers the top of the Your tablet tile
    and its stack. Frame ch1sent-680x425.
28. polish, family:network. 800x500 stop 5B: the piece stack overlaps the end of the "copy, everyone" badge. Frame
    ch5B-800x500.
29. nit. The Your tablet stop card adds "People use the internet to look things up and to talk to each other." (from
    T-S2), which spec Content and Done when 5 do not list; record it in the spec's Refine changes. The Refine changes
    line says "What your message gave away"; the screen says "What this message gives away".
30. nit. 4A still lands 2.8 s after 4B (6.99 s vs 4.23 s at Story speed); the spec says about 2 s. Known in handoff.

##### Gate
1. Done when: PASS (1, 2, 4, 5, 6, 7, 8 as specified; 3 at 2.8 s; 5 with nit 29). Keyboard only with Motion off reached
   the ending (focus on Try other choices); the "bounced" tag shows with Motion off.
2. Codes taught: PASS. NT-14 both halves (the trip and the look-up), SE-13 (choices and the board), IM-15 (who it
   touched, benefit and risk).
3. Solo student: PASS. Every waiting moment names the control (Send, Next, Try other choices, Send a test, a moving
   piece, Close a road).
4. Sensitivity: not needed (rule 5 does not apply).
5. No blocker or should-fix open: FAIL, item 25.
6. Bundle: PASS. 209 KB, one file, no console errors or exceptions in any run (the only log was the host page's own
   favicon 404), no fetch, XHR or WebSocket; storage only the kit's Motion setting.
7. Voice counts: PASS.

| line | kind | expected | spoken |
|---|---|---|---|
| wStory welcome | welcome | 1 | 1 |
| ch1 (load + 5 Start over + 2 Try other choices) | event | 7 | 7 (the load one dropped by the first Start over) |
| ch2 to ch6, look, ask6 (2 runs) | event | 2 each | 2 each |
| results (2 runs of 6) | event | 12 | 12 |
| next (12 triggers) | how | 1 | 1, then silent 11 |
| end (2 runs) | event | 2 | 2 |
| again (2 triggers) | how | 1 | 1, then silent 1 |
| send (patient run) | how | 1 | 1 (dropped as stale when Send came first) |
| wMap | welcome | 1 | 1 |
| landed (6 tests) | event | 6 | 6 |
| peek | how | 1 | 1 |
| closed (3 times on) | how | 1 | 1, then silent 2 |

First taps on fresh pages: the stage, a card and a Tab key each get the welcome at about 0.13 s, then ch1; Trip map gets
its welcome only; Read speaks the Read text only; Sound says nothing, and Sound off then on brings the welcome once;
Motion gets the welcome. Read during the welcome or a result stops it and reads; Read with Sound off works; Trip map
right after Read starts its welcome at once. Fast taps (0.2 s) through picks, Send, mode switches, Close a road and
Start over: no line played after its moment (results and how-tos hushed or dropped stale), order always followed the
taps.

#### Round 2 re-check
Builder's "Refine round 2" (handoff.md) checked against fresh frames: all 105 frames at 680x425, 800x500, 1000x625,
1280x720, 1366x768, 1920x1080 and 760x900 viewed one by one (default, Trip map, ch1 pick and sent, ch2B, ch3, ch3B, ch4A,
ch5B, ch6, ch6B, the four endings), plus 375x812 through the host page (h-ch1sent, h-ch2A, h-ch2B, h-ch3, h-ch5B).
Bundle with CURIO_DRAFT=1: 210 KB, one file, no console errors (only the host page's own favicon 404).

##### Items
25. FIXED. 680x425 and 375 stop 2: the Free_Fast_WiFi hotspot sits above your Wi-Fi router, its name on its right and
    the "open" badge (lock badge for 2A) on its left; "Your Wi-Fi router", "Your internet provider", "Free_Fast_WiFi"
    and the badge all read in full, no horizontal scroll at 375. 760x900, 800x500, 1000x625, 1280x720, 1366x768 and
    1920x1080 keep the old layout (hotspot below the router, badge on its right), every label clear. Frames ch2B-*,
    h-ch2A, h-ch2B.
26. DONE. The picked card's text clears the check circle at every size ("Free_Fast_WiFi" in full); "Home Wi-Fi" wraps
    as "Home / Wi-Fi" at 1920 and never splits "Wi-Fi". A card clip scan over every chapter and size found no clipped
    card text.
27. DONE. 680x425 after Send: the pieces card ends about 30 px above the Your tablet tile; the tile and its stack show
    in full. Fine at 375, 760x900 and 1000x625 too.
28. DONE. The piece stack sits on the server tile's top right corner and clears the "copy, everyone" badge at 680, 800,
    1000, 1280, 1366 and 1920.
29. DONE. Spec Refine changes now says "What this message gives away" (matches the screen) and records the Your tablet
    stop card sentence and the round 2 changes.
30. DONE. Story speed: 4A lands 6.21 s, 4B 4.21 s, a 2.0 s gap. The "bounced" tag still shows with Motion off.

##### New
31. polish, family:network (not a regression, same in round 1 frame f1/ch5B-680x425). Stop 5B at 680x425 and 375: the
    "copy, everyone" badge sits over the closed Router A tile's label (680: label hidden; 375: lower edge of the tile).
    Router A is already named at stop 4 and keeps its red X, so it reads; a later pass could put the badge on the
    server's right. 800x500 and up are clear.

##### Regressions
None found. Every frame matches round 1 apart from the four fixes. The only fold note is unchanged: at 760x900 the
disabled Send sits below the fold on the first screen and scrolls into view when it becomes ready.

256-ending table (rerun): E1 4, E2 220, E3 28, E4 4, 0 against the spec rules. allLines matches voice/lines.json (34
lines). Chapter 6 lands 1, 3, 5, 7, 2, 4, 6, 8. Trip map with Close a road goes through Router B (net.path agrees).

Voice at 2 s pace (allA, mixB, 4A; realistic speech timing): each run speaks the welcome, ch1, the cut line, then every
chapter line, result, look, ask6, end and again once, in order, no errors; the only cut is the "Press Next" how line
when ch2 starts, the same as round 1. Start over x5 plus two endings: the counts table above holds line for line (ch1
7, ch2 to ch6, look and ask6 2 each, results 12, next 1 then 11 silent, end 2, again 1 then 1 silent). The 4A change
moved no line.

Keyboard only (Motion off, Tab and Enter): reached the ending (E2) with focus on Try other choices; no errors.

##### Gate (round 2)
1. Done when: PASS (3 now at 2.0 s; 5 with the spec updated).
2. Codes taught: PASS (unchanged).
3. Solo student: PASS (unchanged).
4. Sensitivity: not needed.
5. No blocker or should-fix open: PASS (25 fixed; 31 is polish).
6. Bundle: PASS (210 KB, no errors, no network, storage only the Motion setting).
7. Voice counts: PASS (table above unchanged; clips still browser voice, as expected).

<!-- end part -->

<!-- part: refine/craft.md -->

### internet-journey: Craft lens (round 1)

Cold read of spec.md, src.html, notes.md, art/prompts.json, voice/lines.json, kit/network.js and
docs/families/network.md, against REFINE.md (Craft lens), STANDARDS.md and BASELINE.md. Bundled with
`CURIO_DRAFT=1 python scripts/bundle_tool.py internet-journey` (194 KB). Driven in muted headless Chrome on my own
profile and ports 9461-9466 (a small CDP harness on top of scripts/drive.py, held clicks of 120 ms, real keys).
Browser voice only (no clips yet), so a "spoken" line in headless lasts until the kit's cap; timings below are relative.

Counts: blockers 0, should fix 8 (general 5, family 3), polish 4, nits 5 (general 3, family 2)

#### Contract (passes)

- One file, 194 KB. No network requests (Network domain and `performance.getEntriesByType('resource')` both empty
  in every run). No fetch, XHR, storage or WebSocket in src.html or kit/network.js.
- No console errors, warnings or exceptions in any run (13 page loads, both modes, Motion on and off, two full Story
  runs, Trip map tests, fast-tap runs, sizes 680x425 to 1920x1080).
- Kit used: header buttons, `Curio.voice`, `Curio.tone/yes/wait/reduce`, and the new `kit/network.js` (graph, draw,
  token, send with bounce, split, join, path). Nothing in the kit is re-implemented.
- Engine pure part runs in Node (path with a down node reroutes, reach, split by words, join with "___", step with
  ttl). The engine matches the spec's "Family engine" description except the items under S5, S6, N2, N3.
- `allLines()` (29) equals voice/lines.json (29), word for word and in the same order.
- Words: no em dashes in src.html, notes.md, lines.json, tool.draft.json, prompts.json, network.js or network.md;
  "Curio Class" never "Curio" alone; classroom-safe; nothing stored, and notes say so.
- Art: both `art:` tokens (ij-dusk-town, ij-server-hall) have prompts.json entries; no people in either.
- Targets: every button and focusable stop is at least 44 x 44 px at 680x425, 800x500, 1000x625, 1280x720,
  1920x1080 and 760x900 (measured in Story chapter 1, chapter 2 and Trip map). Map labels 13 px at 680x425.
- Motion off: pieces jump hop to hop, the "bounced" tag shows at Router A (frame kb-calm-ch4-bounce), no pan.
  Sound off hushes and drops queued lines unmarked; Read works with Sound off.
- Keyboard only with Motion off, all B in chapter 1 then A: reaches the ending, then See the trip map, every stop
  by Tab. The focus ring (4 px `--focus`) shows on cards, Send, Next, Try other choices, the header and every map
  stop.

#### Standard voice check

Two full Story runs at real speed (all A, then Try other choices, all B, then Try other choices again), then Trip map:
Send a test five times, Close a road toggled five times, Send a test, five stops tapped.

| line | kind | expected | spoken |
|---|---|---|---|
| w-story "Welcome to Internet Journey..." | welcome | 1 | 1 |
| ch1 "You are inviting your friend Juno..." (3 chapter-1 openings) | event | 3 | **2** (first load: silent "early", never re-queued; see S1) |
| ch2 to ch6 chapter texts (2 runs) | event | 2 each | 2 each |
| result 1 "Your tablet cut the invite..." | event | 2 | 2 |
| results 2A..6A (run 1), 2B..6B (run 2) | event | 1 each | 1 each |
| next "Press Next to send the pieces on..." (12 triggers) | how | 1 | 1 (then silent x11) |
| E1 (run 1), E2 (run 2) | event | 1 each | 1 each |
| again "Press Try other choices..." (2 triggers) | how | 1 | 1 (then silent x1) |
| w-map "This is the whole trip..." | welcome | 1 | 1 |
| landed "All 8 pieces arrived..." (6 tests) | event | 6 | 6 |
| closed "Router A is closed..." (3 times on) | how | 1 | 1 (then silent x2) |
| hints send / choose / watch | hint only | 0 (Read) | 0 (but see S1: the Send step is never spoken) |

First tap, one fresh page each (time after the tap):

| first tap | expected | got |
|---|---|---|
| the stage | welcome within ~0.5 s | w-story at 133 ms |
| a chapter 1 card (no line of its own) | welcome | w-story at 146 ms |
| Trip map | its welcome only | w-map at 135 ms |
| Read | the Read text only | read at 137 ms, nothing else |
| Tab key | welcome | w-story at 3 ms |
| Motion | welcome | w-story at 136 ms |
| Sound off | nothing; Sound on brings the welcome once | nothing; w-story on Sound on; a second off/on adds nothing |

Stale lines and order: fast taps (gap 0.2 s) through the three chapter 1 cards, Send, Trip map, Send a test, Close a
road, Story: the result, the closed line and Next's line were dropped (`hush`, `newer`); nothing played after its
moment and nothing from an older action played after a newer one. With the time scale at 0.2 through chapters 1 to 3,
each chapter text and result was dropped `newer` when the next action came. Read during the welcome stopped it; lines
queued during Read waited for it; Read with Sound off spoke; Trip map right after Read started its welcome 141 ms
later. Every spoken line was checked against the frame at its time (frames r1-*, r2-*): they match, except S7 and P3.

#### Findings

##### Should fix

**S1. Chapter 1's story line is never spoken on a first visit, and the Send step is never spoken at all.**
general. src.html:886 (`V.say(L.ch[n]...)` in `openChapter(1)` runs at load), 1160. How seen: every first-tap log
starts `event silent early "You are inviting your friend Juno..."`; nothing re-queues it, so a pre-reader's first
visit hears only the welcome ("tap a card to choose"). The chapter 1 how-to "Pick a card for Place, Extra and Photo.
Then press Send." (L.h.send) is hint only, so after picking three cards nothing spoken names Send. Done when 6 says
"chapter and result lines play each time". Better: queue the chapter 1 text after the welcome on the first tap
(welcome list `[wStory, ch1]` or `welcomeAfter`), and speak L.h.send once as a `V.how` (needs '#send').

**S2. The Story welcome overwrites the panel hint.** general. src.html:395-400 (welcome uses the kit default
`hint: true`). How seen (s9): after the first tap the Story hint reads "Welcome to Internet Journey..." instead of
"Pick a card for Place, Extra and Photo. Then press Send."; Read then says the chapter text plus the welcome, never the
Send step. Better: give the welcome `hint: false` (a `[key, {hint: false}]` welcome entry), so the panel hint and Read
keep naming the next action.

**S3. Trip map pieces leak into Story's stacks.** general. src.html:1077 (`state.flying.add` in `sendTest`), 1127
(leaving Trip map does not clear `state.flying`), 617. How seen (s8 stale1, s9): Send, Trip map, Send a test, back to
Story within 1 s: `state.flying` is `[1, 2, 3, 4, 5]`, the stack at Your Wi-Fi router shows "3" (frame stale-end shows
"5" in another run) while the story says 8 pieces; it stays wrong until the next chapter's pieces fly (returning at
chapter 5 keeps it through chapter 5). Better: clear `state.flying` when leaving Trip map, or keep a separate set per
mode.

**S4. Tapping a moving envelope almost never works, and the envelope is not reachable by keyboard.** family:network
(engine tokens, kit/network.js:451-466, and src.html:1046-1050). How seen (s5): a token is 34 x 24 px and moves; the
tool listens for `click`, which needs press and release on the token. Four tries each: Quick with a 120 ms hold 0 of 4,
Quick 30 ms 0 of 4, Slow 120 ms 0 of 4, Slow 30 ms 4 of 4. A grade 3 tap is about 120 ms, so the envelope view (To,
From, "Piece n of 8", the lock: the spec's way of showing what a router reads) is out of reach, and tokens have no
tabindex. Better: in the engine, an invisible hit circle of at least 44 px on tokens and a `pointerdown` pick (or a
token `onPick` option); in the tool, pause the test while an envelope is open, and a keyboard route (for example the
stop card of the stop a piece is at offers "Look at piece n").

**S5. `view.badge()` changes the map's tab order.** family:network. kit/network.js:356-359 and 416 (`drawNode`
removes the node and appends the new one at the end of the nodes layer). How seen (s6, Trip map Tab order): you, ispA,
rA, rB, rC, rD, ispB, home2, juno, then home, srv (the two nodes that Trip map un-badges on entry). The family rule says
node tab order follows `nodes`. Better: replace the old element in place (`old.replaceWith(gEl)`) in drawNode.

**S6. The family doc promises `view.labelBox(id)`, which the engine does not have.** family:network.
docs/families/network.md:37 and the handoff list `labelBox`; the view object (kit/network.js:408-429) has no
`labelBox`, so a sibling calling it throws. Better: add it (the label's bounding box in px) or remove it from the doc.

**S7. Ending E3 says details went along when none did.** general (needs a spec change, so it may belong in the spec's
open questions). src.html:450-453, spec chapter 7. How seen (`ending()` with every A except 6B): no private chips, the
invite on 15 devices including 12 strangers' phones, and the spoken and shown line is "Some private details went
along, but only to people you know." Both halves are false on that screen. The build handoff flagged it. Better: a
fourth line for "no private details, but shared with people you don't know", or send 6B to E2 with wording that fits.

**S8. Focus jumps to the first card on page load.** general. src.html:910 with 913 (`lostFocus()` is true at load,
since nothing has focus yet) and 1160. How seen (s6): the first Tab lands on the second card (at my house) and the
header (Story, Trip map, Motion, Sound, Read) comes only after the cards, Start over, the map and Body. In the site's
16:10 preview iframe this focus() also pulls keyboard focus out of the host page on load. Better: only move focus when
a control inside the panel had it and went away (remember that before re-rendering), never on the first render.

##### Polish

**P1. Event lines write over the hint and leave no next action.** general. src.html:903 and 1094 (`V.say` with the
default `hint: true`). Seen (s12): after a Trip map test the hint (and Read) says "All 8 pieces arrived, and the numbers
put them back in order."; during the ending line the panel shows the ending text twice (story text and hint) instead
of "Press Try other choices...". Better: `hint: false` on both, and a Trip map hint after a test that names a next step
("Close a road, then press Send a test again.").

**P2. Coming back to Story does not retell the chapter cut off by the mode switch.** general. src.html:1118-1139.
Seen (s8 stale2): chapter 3's text was hushed by the switch to Trip map; back in Story at chapter 3 "choose" nothing was
spoken. Better: on return, re-queue the current chapter text when it was not heard in this visit.

**P3. The 4A result is spoken before the bounce happens.** general. src.html:921-933. Seen (frame kb-calm-ch4-bounce
and r1-ch4 frames): "The pieces bounced back from the closed router and went around. They got there, just later." plays
at the tap, while pieces 5 to 8 are still at the internet provider for about 7 s. Better: speak and show the result
after `moveAll` for chapter 4 (the same holds, more mildly, for 2A/2B "Your pieces made it").

**P4. Low contrast placeholders.** general. src.html:143 and 155. The invite's blank "place / extra / photo" is
#8a7fa0 on cream, 3.51:1 at 15 px; the pop-up's field text 3.73:1 at 12 px (AA needs 4.5). Better: `--muted` #5e5470
(7.05:1 on white).

##### Nits

- **N1** general: the stage `<svg id="sv">` is an empty Tab stop in both modes (s6 Tab order shows `sv` after Start
  over and after Quick). Give it `tabindex="-1"` or `focusable="false"`.
- **N2** family:network: `Net.stop()` keeps tokens marked `__keep` (kit/network.js:548), but nothing sets `__keep`;
  `send({keep})` is never honored by `stop()`, unlike the doc ("removes tokens not marked keep").
- **N3** family:network: `colors.ring` is used by the engine and passed by the tool but missing from the documented
  skin colors; the spec says path ties go "to the lower node index" while the engine and network.md say "fewer hops,
  then lower node index". Align the two docs.
- **N4** general: the ending board (1366x768, frame r2-ch7) lets the map's "Juno sees" bubble and slot numbers ghost
  through behind the rows; a fully opaque board background reads cleaner.
- **N5** general: the soccer group row's "phones" icon (three tall rectangles) reads as a folded map at 30 px
  (frame r2-ch7); a small phone with a "12" badge would read at once.

#### Frames looked at

s1-default-1366, r1-ch1-next, r1/r2 ch2 to ch6 choose and next, r1-ch7, r2-ch7, r2-ch3-next, map-landed,
map-envelope, map-env2, map-stop, kb-focus-ch1, kb-calm-ch4-choose, kb-calm-ch4-bounce, kb-calm-ch7, kb-map-focus,
next-focus, stale-end, flying-leak-ch2, end-line-hint, size-{680x425, 800x500, 1000x625, 1280x720, 1920x1080,
760x900}-{ch2, map}, 375-ch1, 375-map (in the lens scratch folder, not committed).

<!-- end part -->

<!-- part: refine/play.md -->

### internet-journey: Play lens

Cold run, 2026-10-28. Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py internet-journey` (194 KB). Driven with
`scripts/drive.py` (port 9450-9457, own profile), held clicks for voice, `__tool.timeScale` only for reaching frames.
Browser voice, art as it stands (not judged).

Played twice: (1) as a grade 3 student alone at home, Sound on, reading little, tapping fast; (2) as a teacher
projecting at 1366x768 and 1920x1080, pausing at each stop for a class vote.

#### Frames looked at

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

#### What works

The story idea lands: the invite card fills in as you pick, then turns into 8 numbered chips; the "open" or lock
badge stays on your router, Router A gets its X, the server gets "copy", the 12 phones appear for 6B, and the slots
fill 1, 3, 5, 7, 2, 4, 6, 8 before "Juno sees" reads the whole invite. The board is a clear payoff and the two runs
(all safe, all risky) compare well on a projector. Keyboard: focus starts on the first card, Enter picks, focus moves
to Next and then to the new cards, the ring is visible. At an unhurried pace (11 s per action) every chapter line,
result and ending is spoken in order and "Press Next" is spoken once then only shown, as the rules ask.

#### Findings

##### Should fix

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

##### Polish

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

##### Nit

15. The pop-up's ✕ looks tappable but does nothing (stop 3). Tapping it could pick "Close it and tell a grown-up", or
    draw it as plain text. (general)
16. The "copy" badge on the server is crossed by the line to Router C. (stop 5 on; family:network)
17. A closed Router A's label turns a dim violet on the dark sky, noticeably harder to read than the others.
    (stop 4 on, Trip map with Close a road; family:network)
18. The soccer group row's icon (three phones) reads as a folded map at 30 px. (stop 7; general)

#### Counts

Blocker 0, should fix 5, polish 9, nit 4.

<!-- end part -->

<!-- part: refine/teaching.md -->

### internet-journey: Teaching lens (round 1)

Cold read of spec.md, src.html, notes.md, art/prompts.json, voice/lines.json; bundle with `CURIO_DRAFT=1` (194 KB).
Driven with `scripts/drive.py` (ports 9441-9443, own profile). Every ending recomputed for all 256 choice combinations
(`__tool.ending(c)` against the spec's rules, in Python). Standard wording read from the official PDF, "2026 CSTA PK-12
Computer Science Standards" (statements and boundary statements, pp. 83-89 and Appendix A p. 180), since the repo holds
only the ids.

Counts: blocker 1, should fix 4, polish 3, nit 3.

#### Standards (rule 2)

| Code | Statement (CSTA 2026) | Taught by | Verdict |
|---|---|---|---|
| E3-SYS-SE-13 | Evaluate how sharing information online might reveal personally identifiable information and other details. Boundary names "providing their address in response to a pop-up ... saying they won a prize" and seemingly harmless details that reveal PII. | Chapter 1 cards (address, phone, school shirt photo), chapter 3 pop-up (the boundary's own example), chapter 5 profile, chapter 6 sharing, the Where copies live board, a second run to compare. | Taught well, but see should fix 4: the "private" tags do the evaluating for the student. |
| E3-SYS-NT-14 | Explain how people access the internet to gain information and communicate with each other. Boundary: devices that connect, using a search engine to look up facts, video chat; "not expected to describe ... routing protocols ... or data packet transmission." | The communicate half: tablet, Wi-Fi router, internet provider (chapters 1 to 3, stop cards). | Half taught. Should fix 2. |
| E3-SYS-IM-15 | Describe how widely used computing systems may impact an individual's life and community. Boundary: benefits and harms (safety, privacy...), identify which individuals or communities are impacted and how. | The board shows harms to "you" (copies on a server, profile seen by everyone, 12 strangers' phones). | Partly taught. Should fix 3. |

#### Done when

| # | Check | How | Result |
|---|---|---|---|
| 1 | All A: E1, 3 rows, "Your invite is on 3 devices", no chips | frame 02-allA-end, board text | PASS |
| 2 | Place B, 3B, 6B: E2, soccer and pop-up rows, address chip on every invite row, "15 devices and one website you don't know" | frame 03-E2-spec; N = 3 + 12 = 15 | PASS |
| 3 | Chapter 4 A bounces, about 2 s later than B; Router A closed for the rest | real time: A 6.97 s, B 4.20 s, so 2.77 s later; rA X badge at the ending (03) | PASS on behavior; timing is nit 2 |
| 4 | Chapter 6 lands 1, 3, 5, 7, 2, 4, 6, 8 into slots; invite reads whole and matches chapter 1 | `state.landOrder` [1,3,5,7,2,4,6,8] in every run; "Juno sees" matched the picks (02, 05, 09). Recomputed at Slow: odd arrive 3.2, 3.7, 4.2, 4.7 s, even 5.45, 5.95, 6.45, 6.95 s | PASS |
| 5 | Trip map stop cards match Content; test lands 8; Close a road goes through Router B and `net.path` agrees | 11-map-cards (all 11 word for word); 12: landed 1,3,5,2,7,4,6,8 (recomputed at Quick: 3.20, 3.70, 4.20, 4.45, 4.70, 4.95, 5.45, 5.95 s); 13: route via rB, `net.path` = you,home,ispA,rB,srv,rC,ispB,home2,juno | PASS |
| 6 | Voice: chapter and result lines each time, welcome once, Next how-to once then shown, Read speaks chapter text | held-click runs v4a, v4b: welcome spoken once; ch1 to ch3 and results spoken; `next` spoken once then silent; after Start over ch1, ch2 and result spoken again; Read read the ch3 text | PASS (full counts are the Craft lens's) |
| 7 | Sizes; map labels at least 12 px at 680x425 | v2-680: SVG text 12.5 to 14 px | PASS for labels; other sizes are the Play lens's |
| 8 | Motion off, keyboard, console, network, storage, name | console clean in all 20 frames; no fetch, XHR or storage in src.html or kit/network.js; "Curio Class" only | PASS for what I checked; keyboard and Motion off runs left to Craft and Play |

#### Findings

##### Blocker

**B1. Ending E3 says something false for "all safe, but Sure, share it".** `src.html:451-453` (`ending()`), mode Story,
chapter 7. With no private card in chapter 1, 3A, 5A and 6B, the board shows "Juno's soccer group, 12 phones" and "Your
invite is on 15 devices", no private chips at all, yet the story text and the spoken ending say "Some private details
went along, but only to people you know." Both halves are wrong: no private details went, and the invite did reach
12 kids the student doesn't know. Seen in frame 04-E3-6Bonly; the 256-run sweep finds it in 4 runs (ch2 and ch4 either
way). The code follows the spec's first-match rules literally (the builder flagged it in handoff.md). A grade 3
student who picked every safe card and then said "Sure, share it" is a likely run, and the line contradicts the board
in front of them. Better: a fourth ending for this case, for example "Your invite reached Juno, and then 12 phones of
kids you don't know. No private details went along this time, but copies can't be taken back. Ask before a message is
shared." (add to voice/lines.json and `allLines()`). **general**

##### Should fix

**S1. Choosing Free_Fast_WiFi turns your own home router "open".** Chapter 2, `src.html:597` (badge on `home`), frame
07-ch2-B. The pieces already sit at "Your Wi-Fi router" (chapter 1 moved them there) before the student picks a network;
picking B puts a red "open" badge on the stop still labeled "Your Wi-Fi router", whose Trip map card says "Your
family's Wi-Fi password keeps strangers off it." The picture teaches that your family's router became the stranger's
network. Better: in chapter 2 keep the pieces on the tablet until the pick (chapter 1 moves them only to the edge of the
tablet), and on 2B relabel that stop "Free_Fast_WiFi" for the rest of the run (or draw it as a separate hotspot), so the
map matches the choice. **general**

**S2. E3-SYS-NT-14 is only half taught.** The code is "how people access the internet to gain information and
communicate with each other". The tool teaches the communicate half through the access chain (device, Wi-Fi, internet
provider). Nothing the student does is getting information: no looking something up, no page coming back from a server.
Also, the boundary says grade 3 is "not expected to describe ... routing protocols ... or data packet transmission", and
CSTA's research summary (Appendix A, p. 180) puts the network-of-networks picture in middle school
(MS-SYS-NT-34, MS-SYS-NT-35, module computer-science-6-8-packets-and-the-internet). The packets and rerouting are the
2017 1B-NI-04 crosswalk, fine as the story's vehicle, but they don't carry NT-14. A real activity that teaches the
missing half: in Trip map, a **Look something up** test (you ask the app's server, or a library website, a question and
the answer's pieces come back to your tablet), plus one line on the tablet stop card naming both uses ("People use the
internet to look things up and to talk to each other"). Otherwise move NT-14 to a tool where looking things up is the
task. The packet-centric focus versus CSTA 2026's grade placement goes to the spec's open questions. **general**

**S3. E3-SYS-IM-15 is only partly taught.** The code asks students to describe how a widely used system impacts an
individual's life and community: benefits and harms, and which people or communities are affected. The board shows harms
to "you" only. No moment names a benefit (the app let you invite Juno from home, she can read it later), and nothing asks
who else is touched (Juno, the 12 soccer kids who now hold your address, your family whose home address is out). The
notes' "Talk about it" has no impact question either. A real activity: a closing "Who did this app touch?" step on the
board where the student taps people (you, Juno, your family, the soccer group) and sees one benefit or harm for each,
drawn from the run's choices, plus a matching discussion question in notes.md. If that can't be done well here, move
IM-15 to a grade 3 tool built around benefits and harms. **general**

**S4. The "private" tags do SE-13's evaluating for the student.** Chapter 1 cards, `src.html:357-359` and `ptag()`, frame
01-default. Every risky card carries a red "private" tag before the student chooses, including "a photo of me in my
school shirt" tagged "your school", which is exactly the "seemingly harmless detail" the boundary statement wants
students to notice themselves. The standard's verb is evaluate; here the label decides. Not a scored quiz, but the
same rule applies (POLISH, nothing gives an answer away). Better: no tags on the cards; after Send, the invite card
marks what the message reveals ("This tells people where you live", "This shows your school") so the student checks
their own pick, and the board keeps its chips. The spec asks for the tags, so this goes to the spec's open questions
with the recommendation. **general**

##### Polish

**P1. Chapter 4 makes the student pick the route, then says routers did.** Card A "Take the closed road anyway" versus
result B "Routers found another way". The lesson ("routers find another road") is undercut by a choice that puts the
sender in charge of routing, and real routers don't send pieces into a router they know is down. Better: make it a
prediction ("Router A is closed. What will the routers do?" Stop the message / Find another road), then show the reroute
either way. Spec change, so open questions. **family:network**

**P2. The safe card is always on the left.** All 8 pairs put the safe pick as card A. On the second run ("pick the
opposite cards", notes.md) a student just taps the other side. Better: alternate sides per chapter (fixed, not random,
so the teacher's notes stay right). **general**

**P3. E3 says "only to people you know" while the board shows the chip on the app's server.** Frame 05-E3-placeB:
"home address" chip on "The message app's server" row, yet the line says the details went "only to people you know".
Better: "...went along, but only to Juno and the app's server." **general**

##### Nit

**N1. Envelope "To: Juno's tablet".** Trip map envelope card (`src.html:1042`) and chapter 1 result. In the spec's own
model the app's server keeps the copy, so pieces are really addressed to the server first. Fine as a grade 3
simplification; if touched, "To: Juno (through the app)". **family:network**

**N2. Chapter 4 A is 2.77 s later than B, spec says about 2 s.** Measured in real time (6.97 s vs 4.20 s). Trim the bounce
or change the spec to "about 3 s". **family:network**

**N3. "Juno sees" ends without a period with the phone card.** Frame 09: "...14 Birch Lane. Call me at 555-0142". The
invite text has no end punctuation when Extra is B. Add a period. **general**

#### Other checks

- Facts: every on-screen number recomputed (8 pieces; 3 or 15 devices; land orders in both modes; 555-0142 sits in
  NANPA's 555-0100 to 555-0199 fiction range). Wi-Fi and HTTPS lock lines, pop-up, and "ask a grown-up" lines match the
  spec's Sources (Cloudflare, FTC, Common Sense). Notes match the tool.
- Endings across all 256 runs: E2 220, E3 32, E1 4; every one matches the spec's rules as the builder read them
  (5B counts as private details going to everyone).
- Language: plain and right for grade 3; the grown-up word "packets" is kept to the notes.
- Guardrails: grade 3, no points, timers or win states; no health or hard-history content.
- Sensitivity (rule 5): nothing cultural, Native or hard-history. No flag.

Frames: out/01-default, 02-allA-end, 03-E2-spec, 04-E3-6Bonly, 05-E3-placeB, 06-allB-end, 07-ch2-B, 08-ch3-B,
09-ch6-allB-photo, 11-map-cards, 12-map-test, 13-map-closed, 14-ch4-A/B-timing, 15-ch5; out2/v2-680; out3/v4a, v4b.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### internet-journey: build handoff

Built 2026-10-27 (wave BR1), the first tool of the network family. New files: this folder's src.html,
tool.draft.json, notes.md, voice/lines.json (29 lines; 34 after Refine round 1), handoff.md; `kit/network.js` (the engine);
`docs/families/network.md`. No existing kit file was changed. Art (ij-dusk-town, ij-server-hall) was already in
art/ from the art pass; review is still "pending" in art/prompts.json.

#### What it is

Story (7 stops, one two-card choice each) follows a party invite cut into 8 numbered envelopes from your tablet to
Juno's, then the **Where copies live** board. Trip map lets you tap any stop, send a "Hello Juno!" test (odd pieces by
Router C, even by Router D, so they land out of order), close Router A and watch the test reroute through Router B,
and tap a moving envelope to see its outside (To, From, Piece n of 8) with the words locked.

#### src.html layout

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

#### Engine API (kit/network.js, global `Net`)

Full list in docs/families/network.md. Pure: `graph, addNode, addLink, removeNode, removeLink, key, path (by ms|hops,
skip, avoid; ties fewer hops then lower index), cost, reach, flows, around, split, join, step, KINDS, DEVICES`. DOM:
`draw(svg, g, skin) -> view` (pos, linkPoints, nodeEl, linkEl, update, badge, ring, setPickable, focus, labelBox,
layers), `icon, token, place, send (arrived|dropped|bounced|stopped, onDown 'bounce'), stop, ICONS`. Checked in Node:
the spec's routing examples (Town and City maps, with and without a down router) give the expected paths.

#### Checks (Done when, round 0 build)

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

#### Refine round 1 (2026-10-28): what changed

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

##### All 256 runs

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

##### Voice at a 2 s pace (real time, Sound on, held first tap)

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

#### Checks after Refine round 1

- Frames at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x900: stops 1, 1 sent, 2, 4 and 6,
  and the end.
- 375 via `--host`: start, stop 1, stop 2, stop 6, the end and Trip map. No horizontal scroll (scrollWidth 375). The
  host server was stopped and host.html deleted.
- Send, Next and Try other choices are in view at every size. At 760 the page scrolls them into view.
- Trip map: pointer pick on a moving piece, keyboard pick, and a closed-road test that lands 8 via Router B.
- Motion off and keyboard only: 6 Tabs to the first card, then Enter through every stop to E4. Focus lands on Try
  other choices.
- Console clean in every shot. The only error was the host page's own favicon 404.

#### Refine round 2 (2026-10-28): what changed

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

#### Known gaps and judgement calls

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

#### For Cory

- Art review for the two FLUX.1 [schnell] images is still pending (credit added to tool.draft.json sources).
- Nothing else needs a decision.

<!-- end part -->

## Log

- 2026-11-25: refine.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/craft.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/play.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-10-28)
- 2026-11-25: handoff.md folded in (last changed 2026-10-28)

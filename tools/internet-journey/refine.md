PASS (round 2 re-check: item 25 fixed, polish 26 to 28 and nits 29 and 30 done, no regressions; new polish 31 noted, not gating)
Counts: blockers 1 (general 1, family 0), should fix 13 (general 10, family 3), polish accepted 10

# internet-journey: Refine

Lens files: refine/teaching.md (T), refine/play.md (P), refine/craft.md (C). Each item names its source; read the
lens file for frames and detail. Settled with BASELINE where lenses or spec left a call.

## Blockers
1. **Wrong ending line for the "no private details, invite spread" runs** (T-B1, C-S7, P-S3; general). All safe cards
   except 6B (and the other 3 runs T found) end on E3, "Some private details went along, but only to people you know";
   both halves are false. Add a fourth ending (no private details went anywhere, but the invite reached 12 phones of
   kids you don't know), with its own spoken line in voice/lines.json and allLines(). Re-run all 256 combinations and
   list which ending each gets in handoff.md. Also fix T-P3: E3 must not say "only to people you know" while the board
   shows the detail on the app's server.

## Should fix
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

## Polish accepted
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

## For the spec's open questions
- Packets and routing are middle school in CSTA's notes (T-S2): should grade 3 stay packets-first? Not blocking.
- 5B counted as a stranger copy for E2 (builder's reading); stays.

## Exit check (round 1)

Fresh cold agent, 2026-10-28. Bundled with `CURIO_DRAFT=1 python scripts/bundle_tool.py internet-journey` (209 KB;
voice clips not recorded yet, browser voice, as expected). Driven in muted headless Chrome on my own profile and ports
9580-9584 (`scripts/drive.py` plus a small held-click harness with a timed stand-in for speechSynthesis, about 60 ms a
character). Frames: default, Trip map, stops 1 (picked, sent), 2B, 3, 3B, 4A, 5B, 6, 6B and all four endings at
680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x900, and nine frames at 375 via `--host` (host.html
deleted after).

### The merged list, re-checked
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

### New items
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

### Gate
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

## Round 2 re-check
Builder's "Refine round 2" (handoff.md) checked against fresh frames: all 105 frames at 680x425, 800x500, 1000x625,
1280x720, 1366x768, 1920x1080 and 760x900 viewed one by one (default, Trip map, ch1 pick and sent, ch2B, ch3, ch3B, ch4A,
ch5B, ch6, ch6B, the four endings), plus 375x812 through the host page (h-ch1sent, h-ch2A, h-ch2B, h-ch3, h-ch5B).
Bundle with CURIO_DRAFT=1: 210 KB, one file, no console errors (only the host page's own favicon 404).

### Items
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

### New
31. polish, family:network (not a regression, same in round 1 frame f1/ch5B-680x425). Stop 5B at 680x425 and 375: the
    "copy, everyone" badge sits over the closed Router A tile's label (680: label hidden; 375: lower edge of the tile).
    Router A is already named at stop 4 and keeps its red X, so it reads; a later pass could put the badge on the
    server's right. 800x500 and up are clear.

### Regressions
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

### Gate (round 2)
1. Done when: PASS (3 now at 2.0 s; 5 with the spec updated).
2. Codes taught: PASS (unchanged).
3. Solo student: PASS (unchanged).
4. Sensitivity: not needed.
5. No blocker or should-fix open: PASS (25 fixed; 31 is polish).
6. Bundle: PASS (210 KB, no errors, no network, storage only the Motion setting).
7. Voice counts: PASS (table above unchanged; clips still browser voice, as expected).

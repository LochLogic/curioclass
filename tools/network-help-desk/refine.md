PASS (exit round 2 failed one narrow item, router links sharing the cable's run at 680x425 and 800x500; integrator fixed it and verified by driving, 2026-10-29)
Counts: blockers 0 (general 0, family 0), should fix 15 (general 13, family 2), polish accepted 11

# Refine: network-help-desk

Builder: Codex (single-tool test, 2026-10-28). Lenses: refine/teaching.md (0 / 8 / 6 / 2), refine/play.md
(0 / 11 / 8 / 3), refine/craft.md (0 / 6 / 5 / 4). Merged by the integrator. Each item names its sources
(T = Teaching, P = Play, C = Craft) and keeps its tag. Spec changes are marked; one cluster waits on Cory.

## Should fix

1. **The cause can be found without diagnosing** (T S1, S2, P1; P on Play 1; C nit 3; T P2) general. SPEC CHANGE,
   WAITS ON CORY (see Spec open questions). Three ways in: the "Right cause" reply confirms a cause on any weak clue,
   so sweeping the 7 cards is free; the cause board prints the kind over each card, so the student never sorts
   Connection vs Logging in vs Permission (the sort that carries E4-SYS-SE-13); and six Q4 answers name the cause card
   almost word for word, so "ask Q4, copy the words" solves most calls (Play solved all 8 with one question each).
   Missed wave lesson (no free sweep). The need-clue double wording (T P6, P nit 1) goes with this fix.
2. **The map draws unknown parts as working** (T S3, C 5, P 8) general. After Q1 alone call 1 shows the cable plugged
   in, calls 2 and 4 a working Wi-Fi link, call 3 a joined Wi-Fi link though the password failed; call 5 and House
   router-off still show Wi-Fi arcs and live links from a dead router. Until its question is asked a part is drawn
   as unknown (the grey dotted "?" style), never as working; a router with no power draws no arcs and every link
   down.
3. **The Internet cloud sits inside the Kitchen; its line runs through devices** (T S4, C 2, P polish 3, audit lead,
   C nit 1) family:network. The router-to-Internet line crosses the Phone, Mr. Patel's and Ana's laptops and their
   labels, so they look wired into the path. Put the cloud outside the house walls at every size (the 375 layout
   already does), or route the link with `via` so no tile or label sits on it.
4. **The cause board hides whole groups** (T S6, P 2, P 3, C 3) general. At 1366x768 after any nudge "Not allowed"
   (the only Permission card, the answer to calls 7 and 8) drops below the board's scroll edge; at 680x425 only the
   Connection group shows; at 800x500, 760x900 and 375 Logging in or Permission are cut under the clue title. All
   seven causes (or, after item 1, all three kinds and the chosen kind's causes) in view in every claim state at
   every size, no scroll.
5. **A resize during a wrong-claim ping throws and locks the call** (T S7) general. `runPing` adds a `fault` node the
   ResizeObserver redraw drops; `linkPoints` throws on `px`; the call stays busy with Send fix and Back disabled.
   Carry the fault node into the redraw, or let the redraw wait for the ping. Re-test by resizing mid-ping on calls
   1, 2, 4, 5 and mid-fix on every kind.
6. **Call 8's Solved badge says "Allowed" on the guest laptop** (T S5, P 10, C 6) general. Ana is still not allowed;
   a family laptop printed. Badge her "Sent" (or keep "Guest") and put the check on the family laptop and printer;
   label the two "Ana's laptop" and "Family laptop". Keep "Allowed" for Leo's Student page. Settled: the Permission
   kind line becomes "Logging in worked. That account or network just isn't allowed to do that, and that is on
   purpose." (fits calls 7 and 8), and the Logging in line "The Wi-Fi or website was in reach. The device had to
   prove who it was with the right password." (fits calls 3 and 6; T N2). Update voice/lines.json if a spoken line
   changes; the solved lines stay as the spec wrote them.
7. **A broken link uses the Guest look** (P 7, C 4) family:network. Down links are the same orange dashes as Guest.
   Set the skin's `down` color to its own style (grey dashes with the break mark, or red with an X) and add "Broken"
   to the legend; orange stays Guest only. No engine change needed (skin colors).
8. **The next-call line is lost and its hint names the wrong control** (P 4; C heard it once in 5) general. Play's
   log shows it dropped 2.4 s after the solved line or never queued. Make it play once after the first Solved, and
   word line and hint for what is there: "Tap Next call, or a phone on the call strip." (spoken line change: update
   lines.json).
9. **680x425: Next call, Shift report and the 8th phone are cut off** (P 5, C polish 3) general. The hint names Shift
   report while it is out of view. At short heights put Next call beside the stamp, keep Shift report in view, and
   let the call strip fit all 8 phones (680 and 375).
10. **The skipped welcome plays after the first tap's own line** (P 6, C polish 1) general. Settled by STANDARDS and
    KIT.md: `welcomeAfter` is for one-mode tools; this tool has two. Drop `welcomeAfter`; on a first tap that has its
    own line, skip the welcome and let Sound off/on or the next mode entry bring it (as the kit does by default).
11. **The Shed spot is drawn on the Shed's wall** (P 9) general. Rooms are drawn on screen fractions while devices use
    the design box, so they drift apart near the edges: Sam's phone and the shed tablet sit on the wall over "Back
    door". Derive the room drawing from the same design-to-pixel transform as the devices, so every named spot lands
    inside its room at every size.
12. **House "No bars" hint sticks after the tablet comes back in range** (C 1) general. `moveTablet` never calls
    `updateHint`; Read then speaks a false line. Restore the House hint when bars go above 0.
13. **"about 1 bars of 3"** (P 11) general. "about 1 bar of 3".
14. **Builder talk in the teacher notes** (T S8) general. Delete "although the spec lists 255" sentence; the line
    before already says the thresholds are a Curio Class model. Also "design units" / "20 units per press" in notes
    and the tablet aria-label become "one small step per press" (T N1).
15. **The first-screen hint names no control** (P polish 7, wave lesson "hint names the next control") general.
    "Tap a question to ask the caller. Then tap Make a claim." (if this is the `ask` line, update lines.json).

## Polish accepted

1. The Solved card shows the clue that proved it ("Proved by: ..."), and the Shift report marks each call's key
   question (P polish 4).
2. House results carry the kind stamp (plug, key, hand) and a pass/fail glyph; `houseTry` already computes the kind
   (T P3, P polish 5).
3. House shows only the settings a device has: no Account for printer and TV; a printer on Guest reads "Not allowed:
   the printer is on the Guest Wi-Fi, away from home devices" (T P4).
4. Call 5's wrong-claim X sits on the dark router, not mid-link (T P5); the X on calls 3 and 8 must not cover the
   router icon (P nit 3).
5. Small maps: short device labels at 12 px or more (or distinct icons) so desktop/TV and phone/tablet can be told
   apart; room names 14 px at the laptop sizes and as large as fits in the preview (P polish 1, C polish 2)
   family:network.
6. 375 wide: per spec, show the caller's room and the router with the rest faded, so badges stop covering icons and
   room labels; at 680x425 badges and room names never overlap (P polish 2).
7. Wi-Fi bars drawn beside the tablet on the map while dragging, so the drag is the experiment (P polish 6).
8. 1920x1080: map notes, legend and call time large enough to read projected (P polish 8).
9. House at 680x425: fixed room-label spots per layout ("Living room" stays in the Living room); drop the half-cut
   duplicate "About" line in the panel (C polish 4).
10. Badges ("Online", "On") never sit over a device tile or another device (P nit 2).
11. Labels "Phone" and "Laptop" off the wall lines and the cloud link (C nit 1).

## Settled by the integrator

- Engine change wanted, `glide` reads `calm()` per tick: APPROVED. Backward compatible; re-check internet-journey's
  Motion-off frames and timing after it, and remove the tool-side Net.place workaround.
- Engine change, skin `linkStyle(link)`: APPROVED (from C polish 5). An optional skin function returning
  `{color, width, dash}` (any may be omitted) for a link that is up, applied in `draw` and `update`; down links keep
  `colors.down`. Backward compatible (no option, no change). Document it in docs/families/network.md's skin options
  (the integrator added the guest recipe that names it), re-check internet-journey's frames, and move the tool's
  guest styling onto it.
- Engine change wanted, `homeOnly` on path/reach: DECLINED. The tool's `skip: l => l.guest` is the documented way;
  the integrator adds the guest recipe to docs/families/network.md and corrects the spec's Family engine line.
- Not findings: audit "Tablet: nothing changed" (selected by default; all three lenses); `__tool.claim` from the ask
  step (test API only, C nit 4); Kitchen 255 vs 255.54 (nothing on screen shows a distance).
- C nit 2 (network.md table row lists fewer engine parts): integrator doc edit with the guest recipe.

## Spec open questions

- **Item 1: SETTLED by Cory 2026-10-28, "all three".** The integrator wrote it into spec.md (claim step, need-clue,
  kind and wrong-kind lines, Q4 answers for calls 1, 3, 6, 7, call 1 keys Q4 and Q1 together). The proposal as asked:

- **Item 1, for Cory.** The spec's own design (labeled groups, Q4 answers, "Right cause" reply) lets a student skip
  the diagnosis. Proposed, all three together: (a) judge the clue before the cause: if no selected clue is a key
  clue, every cause gets the same reply ("That clue doesn't prove a cause yet. Pick a clue that shows what is
  broken."); (b) the claim step starts with three kind buttons (Connection, Logging in, Permission), then shows that
  kind's causes; a wrong kind gets a kind nudge ("Logging in worked here. Look at the login clue."); (c) Q4 answers
  on calls 1, 3, 6 and 7 describe what the caller sees rather than name the cause, and call 1's keys become Q4, Q1
  (call 2's Q3 is a rule-out clue only, accepted alongside Q4) (T P1).

## Integrator fix after polish (2026-10-28)

- Call 2's keys were Q4, Q3 in the spec; the proposal Cory approved made its Q3 a rule-out clue, accepted only
  alongside Q4 (Codex flagged it under Left open in polish.md). Spec row and Key clues line, and `CALLS[1].keys` in
  src.html, are now Q4 only. Q3 alone on call 2 now gets the need-clue reply; Q3 with Q4 still solves.

## Exit check, round 1

Checked cold on the worktree build (bundle 131,561 bytes, rebuilt with the same md5), with drive.py on ports 9961 and
9962 and the 375 host on 8804, real held clicks where it matters, every frame looked at. Polish.md read as claims.

Should fix:
- 1 Cause found without diagnosis: held. Kind buttons come first; a weak clue gets need-clue for any cause and no time
  (call 1 with Q2, Q4 alone, Q1 alone; call 2 with Q3 alone); wrong kind +2; wrong cause +2 with a ping and a nudge
  quoting the key clue; Q4 answers describe what the caller sees. Checked by claim() runs and held clicks.
- 2 Map draws unknown as working: held. Unknown links grey dotted after Q1 on calls 1 to 4; call 5 and House router
  off show every link down, no Wi-Fi arcs. Frames.
- 3 Cloud inside the Kitchen, line through devices: not held (partly). The cloud is outside the walls and the line
  misses the device tiles, but the Internet line crosses the "Back door" label at every size and the "Internet" label
  at 1280, 1366 and 1920; call 4's fixed Wi-Fi link runs through the Tablet tile and the fixed phone sits on the
  house's right wall. Frames and zoom crops.
- 4 Cause board hides groups: held for kinds and causes (all in view at every size). The clue cards in the same step
  are not (see New 1).
- 5 Resize mid-ping throws: held. Own test on the 375 host: calls 1 to 7 claimed, the iframe resized four times
  mid-ping and mid-fix; no errors, busy false, Send fix and Back enabled after, solves recorded.
- 6 Call 8 "Allowed" badge: held. "Sent" on Ana's laptop, labels "Ana's laptop" and "Family laptop", checks on the
  family laptop and printer, kind lines match. Frames.
- 7 Broken link uses the Guest look: held. Broken is grey dashes with a break mark, Guest orange dash-dot, legend
  shows Broken. Frames.
- 8 Next-call line lost, wrong hint: held. Held clicks through calls 1 to 4: next-call spoken once about 4 s after
  the first solve, silent after; each solved line spoken every time; hint reads right.
- 9 680x425 controls cut: held. Solved state has Next call beside the stamp and all 8 phones; shift report buttons in
  view. Frames.
- 10 Skipped welcome late: held. No welcomeAfter; a first question tap speaks ask only; Sound off and on brings the
  welcome back once. vlog.
- 11 Shed spot on the wall: held for the shed (tablet and phone inside the Shed in call 4 and House). The call 4 fixed
  phone on the right wall is logged under 3.
- 12 "No bars" hint sticks: held. Drag to the shed speaks "far"; arrow keys back give the house hint.
- 13 "1 bars": held ("1 bar" in code and frame).
- 14 Builder talk in notes: held (no 255, units or spec; "one small step per press").
- 15 First hint names no control: held ("Tap a question to ask the caller. Then tap Make a claim.").

Polish accepted:
- 1 Proved by and key marks: held. Solved cards show "Proved by: Qn" and the answer.
- 2 House kind stamps: held.
- 3 Device-only settings: held (the tablet panel shows only its own controls).
- 4 X placement: held (call 5 X on the dark router, call 3 beside the router).
- 5 Small-map labels and icons: partly held; compact desktop/TV and phone/tablet icons are only slightly distinct.
- 6 375 faded: not held. Badges sit over tiles and a check covers the "Office" label at 375 (calls 1, 3, 6).
- 7 Bars by the tablet: held ("2 / 3" under the tablet).
- 8 1920 readable: held.
- 9 680 House labels, no duplicate About: mostly held; at 680x425 and 1000x625 the help text runs behind Reset house
  and the Router and Desktop cable buttons sit in house-scroll (map taps still work).
- 10 Badges never over tiles: not held. 680x425: router "On" under the printer tile, the TV check on the desktop
  tile; 760x900: "On" under the printer, the TV tile on a wall; 1366 call 5: the "?" badge on the TV tile; caller
  badges (Online, Grown-up, Sent, Allowed, Guest, Signed in) float on the top wall away from their device.
- 11 Phone and Laptop labels off walls, the cloud link: not held. "Laptop" sits on the Kitchen wall in call 3 at 1366,
  "Ana's laptop" on a wall in call 8; the cloud link crosses Back door (see 3).

Settled calls: held. Welcome not re-said after a first tap (Should fix 10); Motion off keeps timing (fix about 1503
vs 1512 ms, ping 1232 vs 1223 ms); only Motion is saved.

Engine changes:
- glide reads calm() per tick: held. internet-journey bundled (210 KB): first screen at 1366 and 680 fine, a send
  takes 5852 ms with Motion on and 5989 ms off, bounce 4A at 6204 vs 6211 ms, 4B about 4.2 s, all 8 pieces arrive,
  the calm mid-bounce frame shows "bounced", no console errors.
- skin linkStyle: held. Custom color, width and dash for up links only; defaults unchanged; documented in
  docs/families/network.md with the Guest recipe.

Integrator fix after polish: held. Call 2 Q3 alone gives need-clue; Q4 solves; Q3 with Q4 and a wrong cause gives
wrong. CALLS[1].keys is [4].

New (not on the merged list):
- New 1 (should fix, BUILD lesson "a short set of choices never hides in a scroll panel"): the claim step's clue
  cards sit in a scroll panel. 680x425: only Q1 and Q2 show, 4 of 6 hidden with no peek (even the Q1 + Q4 minimum is
  clipped); 375: Q1 and Q2 show, Q3 and Q4 peek; 800x500 and 760x900: Q5 and Q6 hidden (keys on calls 3, 6, 7, 8).
  The Questions-step clue list is cut the same way at 375 and 1000x625.
- New 2 (nit): in the shed drop the X badge covers the "Shed" label.

Gate:
1. Every Done when: passes, except that Done when 7 holds only in letter (Questions and Make a claim are in view at
   every size; the claim step's clue choices are not). All 8 calls solved by held clicks; House combos fail only the
   right targets; keyboard-only solve works; 375 works in the host.
2. Codes taught: held. CSTA E4-SYS-NT-14, E4-SYS-SE-13, 1B-CS-03, 1B-NI-05 are taught by the calls and House.
3. Solo defaults: held. Opens on call 1 with the first hint naming the control; no setup needed.
4. Sensitivity: n/a (no people pictured, no rule 5 topic; callers are icon badges).
5. No open blocker or should-fix: fails (New 1, Should fix 3).
6. Bundle: 127 KB, no console errors in any shot (only the host favicon 404), no network requests.
7. Voice counts: right (table below).

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| w-calls | welcome | once per mode, back once after Sound off and on | once; once more after the Sound cycle |
| w-house | welcome | once | once |
| ask | how | once, then hint | once (dropped under the welcome, then once) |
| kind | how | once | once |
| claim | how | once | once |
| house | how | once | once (dropped if the mode changes first) |
| all-clues | how | once | once |
| next-call | how | once | once in 4 solves |
| need-clue | event | 5 of 5 | 5 |
| wrong | event | 5 of 5 | 5 |
| wrong-kind | event | 5 of 5 | 5 |
| solved-* | event | 4 of 4 | 4 |
| far | event | on a drag to the shed | spoken |
| read | Read | speaks the hint, also with Sound off | read both times |
| stale line after a mode change or reset | none | 0 | 0 |

## Audit pilot (exit)

- Leads confirmed: the claim-step clue cards "cut short by a scroll panel" (680x425, 375, 800x500, 760x900); the
  Internet line across "Back door" and "Internet"; "Laptop" and "Ana's laptop" on walls; house-scroll hiding the
  cable buttons at 680x425 and 1000x625; the 375 router and "2 / 3" overlap.
- Leads wrong or noise: most "line drawn across" leads on tile tspans (Printer, Router, TV, Desktop) and on badge
  text ("On", "Off", "Plug out") are wall or route lines passing near a label and read fine on the frames. The
  "welcome not heard after a first tap" rows are the settled behavior (Should fix 10), not a finding.
- Missed: badges under tiles ("On" under the printer at 680x425 and 760x900), the "?" on the TV tile in call 5,
  caller badges detached from their device on the top wall, call 4's fixed link through the Tablet tile, the fixed
  phone on the right wall, the X over the "Shed" label.

## Exit check, round 2

Cold, on the worktree bundle (md5 eac43f34, 145,718 bytes), drive.py on 9961/9962, 375 host on 8804; frames in
S:/CurioClass-codex-scratch/network-help-desk/exit-r2/f/ (claim, early, solved, regress), sheets in exit-r2/sheets/.
Every call with Q1 to Q6 asked and its kind chosen, plus call 1 with each kind and with no kind, at all six sizes;
every call after Q1 only and every call solved at all six sizes. Frames looked at, zoomed where close.
- 1 Clue cards in a scroll panel: held. All six cards fully in view, no scroll or clip ancestor, Send fix and Back in
  view, at 680x425, 800x500, 760x900, 1366x768, 1920x1080 and 375 (claim/<size>-c1..c8-claim, -c1-kind-*).
- 2 Lines: not held (narrow). Held parts: the Internet line no longer crosses "Back door" or "Internet" at any size
  (680x425-c5-claim and 375x812-c5-claim: the break mark ends right against the "B", touching, not over); call 4's
  fixed phone sits inside the Bedroom and its Wi-Fi link misses the Tablet at every size (solved/*-c4-solved).
  Not held: at 680x425 the fixed Wi-Fi link in call 4 runs along the Internet cable from the router, so only a short
  blue stub shows and the path reads as a cable (solved/680x425-c4-solved); the same shared run puts call 3's Wi-Fi
  and call 8's Guest dashes on top of the cable at 680x425 and 800x500 (680x425-c3/c8-solved, 800x500-c3/c8-solved,
  claim frames too). Fix: give links leaving the router their own lane, or route the cable first and avoid it.
- 3 Badges and labels: held. "On" sits beside the router (not under the printer); call 5's "?" sits beside the
  router, clear of the TV (early/1366x768-c5-q1); caller badges sit on their own device; no check over "Office" at
  375; "Laptop" and "Ana's laptop" inside the Kitchen. A rect test over every badge, label, tile, room name and wall
  found no overlap in 168 frames. Polish only: 800x500-c4-solved the router's Wi-Fi arcs draw through the "On" badge;
  680x425-c3-solved "Signed in" and -c4-solved "Online" end a few px from the house's right wall.
Other notes (polish): the Internet cable often runs on or just beside a wall (680 calls 1 and 4 solved, 800 call 4
solved) and through the Shed at 680, 800 and 1366; reads as a wall line, not a crossing.
Regression look: held. Real held clicks solved call 1 (Connection), call 3 (Logging in, also at 680x425) and call 7
(Permission): stamps, fix, "Proved by" and focus on Next call right. Shift report at 1366, 680 and 375: all 8 rows,
Start a new shift and Open House in view. House at 1366 and 680: router off shows every link down and "No
connection". Keyboard: Tab from the claim step reaches kind, cause, all six clue cards, Send fix, Back and the strip
in order at 1366 and 680; Enter toggles a card. Console: no errors or exceptions (only the host server's favicon 404).
Shared audit: audit-r2exit/audit.md did not exist when this check finished (frames only); not waited for.

## Integrator fix after exit round 2 (2026-10-29)

- Item 2, links leaving the router on the Internet cable's run (call 4 Wi-Fi at 680x425; call 3 Wi-Fi and call 8 Guest
  at 680x425 and 800x500): routeMapLinks now remembers each routed link's segments, adds lanes 7 px either side of
  them to the route grid, and charges 400 for any step along an earlier link's line, so each later link takes its
  own lane. Checked by re-running the exit check's 48 solved shots, the claim shots at 680x425 and 800x500 and its 12
  regression shots: call 4's Wi-Fi reads as one blue path to the tablet, call 3's Wi-Fi and call 8's Guest run in
  their own lanes, no route issues, the exit check's badge and label rect tests still empty, a call of each kind solves,
  Shift report and House as before, no console errors (host favicon only). Frames: exit-r2/lanes/, exit-r2/lanes-regress/.
- Left as is: the printer cable meets the Internet cable at the router's corner (an 11 to 30 px junction, not a
  shared run), and the Polish notes from exit round 2 (Wi-Fi arcs through the "On" badge at 800x500 on call 4 solved;
  two badges a few px from the right wall at 680).
- No fresh exit round was run on this change; the drive checks above are the evidence.

PASS
Counts: blockers 2 (general 2, family 0), should fix 10 (general 8, family 2), polish accepted 10

# data-defenders: Refine

Lens files: refine/teaching.md (T), refine/play.md (P), refine/craft.md (C). Read them for frames and detail.

## Blockers
1. **Taps on the second puzzle are lost at 1280 and wider** (C-B1). The tap rebuilds that puzzle's controls under the
   pointer and focus returns to the first puzzle, which plays its how-to. Don't rebuild a control on the tap that
   activates its puzzle (activate on pointerdown and keep the nodes, or rebuild only after the click lands), and don't
   move focus to the other puzzle. Re-run "Use this one" 5 times in each room at 1280, 1366 and 1920: 5 of 5.
2. **E5-SYS-NT-14 (wired and wireless network components) is not taught** (T-B1; rule 2). Settled with BASELINE
   (standards taught well): add a Network closet puzzle in the Server Closet. The student sorts the closet's parts
   into wired and wireless (cable, switch, access point, laptop on Wi-Fi, desktop on a cable...), then the Wi-Fi
   access point fails and the student predicts which devices stay online; the room shows it. Use made-up names only,
   the security engine's look, the room's lock count, voice lines in allLines() and voice/lines.json, and the
   network engine (kit/network.js) only if it fits without changing it. Add it to the spec under "Refine changes".

## Should fix
3. **A2 shows each plan's kept and lost days before the pick** (T-S1, P-S2). The student reads the three plans and
   predicts; the day strips appear after the pick, with the reason (the plan A `why` already in the data, and one for
   each plan; P polish).
4. **I2's log row 4 names "Cy's" scores** (P-S1). Reword it so the row is found by time and device, as the spec means.
5. **Integrity wording** (T-S2). Use "stays correct, and changes can be checked" for the promise, matching the exit
   card "A typo changed a bus time".
6. **C1 gives Jordan's dad the whole Bus routes folder** (T-S3). Give a parent only public info; the right answer must
   not show other families' stops.
7. **375 wide, I2 step 2: the fix buttons are under the log, off screen** (P-S3). The next control is in view when its
   hint plays (Done when 8).
8. **Hint stuck on the room story; Read repeats the story** (P-S4, C-P2). The hint names the room's first action as
   soon as the story starts; Read speaks the action.
9. **Locked Exit says nothing and its hint is overwritten** (C-S3, P polish). Speak a locked line ("The exit opens
   when all three rooms are secured"), keep it in the hint; when all rooms are secured, highlight the Exit and name the
   action.
10. **Marked score chip has no focus ring** (C-S1; family:security). Fix in kit/security.js so focus shows over
    "marked".
11. **Targets under 44 px** (C-S2; family:security for chips and rows, general for Back). Score chips, change-log rows
    and the compact Back button at least 44 px.
12. **Compact puzzle tab focus ring at 1.7:1** (C-S4). At least 3:1 on the room's bar.

## Polish accepted
13. C2: the meter rates only after the student chooses, so the "Strong" word doesn't solve it (T-P, P).
14. Cy's card "Added: 0" keeps its label on small screens (P).
15. A2 day chips at least 14 px at 1920 (P).
16. A wrong I2 fix's reason is spoken, like C2's (P).
17. The lock slot pops with Motion on (C-P1).
18. A wrong-answer line cuts in instead of waiting behind the room story (C-P3).
19. Engine sort buttons, select and login fields at least 44 px for the siblings (C-P4; family:security).
20. Sec.band() on a plain string uses the world's names, so "Cedar2026" is Weak (C-P5; family:security).
21. I2 row 4 found by time and device (see 4) and the I1 cards don't sit beside it before I1 is solved, if the layout
    allows (P).
22. Exit highlight when all rooms are secured (see 9).

Nits are optional; fix the cheap ones (unused variable, lock count by hand, focus trap in the escape card, Sec.world
checks files, family doc drift, Quiz 5 row in the log, `google.com.example` passing safeDomain: make safeDomain
reject a real brand name before a reserved suffix, family:security).

## Settled calls
- Team timer stays Off by default (BASELINE: the defaults work for a solo student); a teacher turns it on.
- The 1-server stripes start at 5 p.m. (4 p.m. is 450, under 500): the tool is right, the spec's "4 p.m. on" is a typo.

## Exit check (round 1, 2026-10-28)

Cold re-check of every merged item, the new Network closet (A3) and the gate. Bundle `CURIO_DRAFT=1` 236 KB. Driven
with `scripts/drive.py` (ports 9610 to 9616, own profiles), 91 frames at 680x425, 800x500, 1000x625, 1280x720, 1366x768,
1920x1080 and 760x900 (hall, every puzzle, A3 step 1 with badges, A3 step 2 with badges, A3 done, exit, escape, all
secured), 13 at 375x812 via `--host` (host.html deleted after). Console clean in every shot. All looked at.

### Merged items
- 1 (split taps): real held clicks, fresh page each, first tap on the second puzzle (C2 "Use this one", I2 row 2) at
  1280, 1366 and 1920: 30 of 30 land, focus stays on the tapped control. Closed.
- 2 (E5-SYS-NT-14): A3 exists and teaches it at full screen: eight parts with a type tag (device, connecting hardware,
  signal) sorted wired or wireless, then the network engine's map with the access point down. Facts right: the
  desktops and printer reach the router through the switch, the laptop and tablet only through the access point
  (`Net.reach` gives office, nurse, printer; my own small graph test agrees). Lock opens only on the full right sort,
  then only on exactly those three. Closed, but see the new should-fix items below (sizes).
- 3 to 9: A2 strip and reason only after a pick; I2 row 5 is the 2:14 a.m. unknown-laptop change, row 3 the daytime
  one; integrity promise reworded everywhere; C1 all-ticked gives "9 boxes give too much access" (12 private cells
  minus 3 needed = 9, right now that the dad gets only Public); I2 fix buttons in view at 375; hint names the first
  action on entry and Read speaks it; locked Exit speaks every tap and keeps the hint, the Exit glows when all are
  secured. Closed.
- 10 to 12: marked chip and compact tab have focus-visible rings (blue over marked; white 3 px on the room bar,
  white on C/I/A 6.39, 5.05, 5.61:1); chips, rows, Back, tabs, Changed, A3 toggles all at least 44 px at 680x425.
  Closed.
- Polish 13 to 22 and the nits: seen in frames and logic (meter after the pick, "Sum" label, day chips, spoken fix
  and plan reasons, cut-in wrong lines, `band("Cedar2026")` Weak, `safeDomain` false for evil.com, gmail.com,
  google.com.example). Done.

### Logic and numbers (recomputed in Python)
Sums 70, 67, 79, 65 (only Cy opens). Over capacity: 1 server 5 to 8 p.m., 2 servers 6 and 7 p.m., 3 = ceil(1400/500)
opens, 4 gives the idle line. A2 only C. Exit: one wrong card slides back ("5 of 6 are right"), all six escape.
Timer 20/30/Off, at 0 "Time!" and C1 still solves. No resource requests, localStorage only `curio-motion`, no em
dashes, no bare "Curio". voice/lines.json = allLines(), 58 of 58 word for word.

### Voice check (held clicks, 0.12 s, Sound and Motion on)
| Line | Kind | Expected | Spoken |
|---|---|---|---|
| hExitLocked (5 taps) | event | 5 | 5 |
| wrong, C1 Check lock x5 / A1 Set servers x5 / A3 Check x5 | event | 5 each | 5 each |
| rShortName, C2 "cedar" x5 | event | 5 | 5 |
| a2A x2, a2B, a2D; fix1, fix2, fix1 | event | each tap | each tap |
| symbol, secC (secured twice via Start over) | event | 2, 2 | 2, 2 |
| welcome | welcome | 1 | 1 |
| c1, c2, a3 (5 toggles), a3b, i2, i2b | how | 1 then silent | 1 then silent |
| storyC on re-entry after Start over | how | silent | silent |
First taps: hallway 1.3 s after load gives the welcome only; door gives only its story; locked Exit only its line;
Read only `read`; Sound says nothing and off/on brings the welcome once; Motion, mode and Tab give the welcome. Stale:
fast taps through A1, A3 tab, Back, Grade Book, Start over: queued symbol and how lines dropped, nothing played late.
Read cuts the story and speaks the hint; a wrong line during Read waits and is dropped by Sound off; Read with Sound off
reads. Order kept in every run. Counts right.

### Open (ROUND 2)
Should fix:
- **A3 step 1 at compact sizes (680x425, 800x500, 1000x625, 375): the part notes and the prompt are hidden**
  (`.compactui .part .pn small` and `.compactui .prompt.opt` are display none; frames 680x425-a3s1, 800x500-a3s1,
  1000x625-a3s1, host/375-a3s1). The notes ("a cable runs from it to the switch", "joins the school Wi-Fi") are the
  only thing that settles the office desktop, printer and laptop, which can be either in real life, and the prompt is
  where wired and wireless are defined. In the preview and on a phone the sort is a guess and a right-thinking
  student is told "2 parts are in the wrong group". Keep each note (one short line is enough) and the definition at
  every size. general
- **A3 step 1 at 375 wide: Check sort is at 1021 to 1073 px in an 812 px view** (host/375-a3s1; Done when 8). The
  eight cards sit in one column. Two columns as in compact, or the check docked in view, so it shows without
  scrolling. general
- **A3 result badges read "Xffline" and overlap** (1920x1080-a3done, 1000x625-a3done, host/375-a3done). The tool
  passes `{icon: 'x', text: 'offline'}`; `kit/network.js` badgeOn draws the x over the start of the text (width
  leaves no room for the x icon) and the pills spill over neighbouring tiles; at 375 they collide into "onli",
  "ffli" and clip at the edge. This is the puzzle's payoff. Give the x room (or use text only), keep the pills inside
  their tile's column at narrow sizes. family:network (the engine) plus general

Polish (known, not blocking):
- The access point is sorted "wireless" but is drawn cabled to the switch in step 2. Say both in its note ("plugs into
  the switch with a cable and sends out the Wi-Fi signal") so the map does not look like a contradiction.
- Check sort with parts left only beeps and shows "Sort every part first: N left"; nothing is spoken (5 taps, 0
  lines). Speak it as an event, like the wrong lines.
- 680x425 A3 done: the done note fills the station and the online/offline map is below the fold (scrolls inside).
- At 375 step 2 the nurse desktop's "!" covers the office desktop's check badge.
- Nit: "has no cable port" for the tablet; it has a charging port. "has no network cable port".

## Round 2 re-check (2026-10-28)

Cold re-check after the builder's "Refine round 2". Bundle `CURIO_DRAFT=1` 241 KB (250,191 bytes). Same ports and
scratch folder. 49 frames: A3 fresh, A3 step 1 with badges, step 2 with badges, done, plus C1, I2 and hall, at
680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x900. 7 more at 375x812 via `--host`, and host.html
deleted after. Console clean in every shot.

### The three A3 should-fix items
- **Notes and the rule: closed.** Every part card shows its note and type tag at every size, 375 included. The
  prompt "Wired uses cables. Wireless uses Wi-Fi signals through the air" shows at every size too (680x425-a3fresh,
  800x500-a3fresh, 1000x625-a3s1, 375-a3fresh). The notes settle each part. The facts are right: the access point
  "plugs into the switch and sends out Wi-Fi", and the tablet has "no network cable port".
- **Check sort at 375: closed.** The cards stay in two columns. On a fresh page the button's top edge is in view at
  790 of 812 px. Sorting all eight parts by click scrolls it fully into view, and after Check sort the step 2 Check
  is in view.
- **Online/offline pills: closed.** They are now the tool's own overlay, centered under each tile. They read
  "online" and "offline" cleanly and overlap nothing at 375, 680, 1000, 1366 and 1920 (zoomed 680x425-a3done). The
  "!" marks and the pick checks sit apart.

### Polish
- **Access point drawing: done.** It is a plain Wi-Fi symbol with a cable to the switch. Its links to the laptop and
  tablet are radio arcs only, and the key says "Wi-Fi (wireless, no cable)". The map now matches the sort.
- **a3left: done.** It is spoken 5 times out of 5 taps of Check sort with parts left.
- **Done map at 680x425: done.** All five devices and their pills are in view, with the note below them.
- **Tablet note: done.**
- The engine bug (`badgeOn` with an x icon and text) is written up in handoff.md for the network family. The tool
  works around it.

### Regressions
- **A3 logic:** a partial sort says "7 left". One wrong part gives "1 part is in the wrong group". The right sort
  opens step 2. Online is still office, nurse and printer. Wrong picks give the right counts, and exactly the three
  open the lock.
- **Rest of the logic:** unchanged and passing: C1 shows 9 boxes, the bands are Weak, Weak, Weak, Strong, Cy, row 5
  then fix 0, 3 servers, plan C, the exit, the timer, and safeDomain.
- **Contract:** no resource requests, localStorage holds only `curio-motion`, no em dashes.
- **Lines:** voice/lines.json = allLines(), 59 of 59 word for word.
- **Split taps:** 30 of 30 again at 1280, 1366 and 1920.
- **Focus rings and targets:** the rings are present, and every target is at least 44 px at 680x425.
- **A3 voice counts (held clicks, gap 4 s):**

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| a3 (5 toggles) | how | 1 | 1 |
| a3left (Check sort x5, parts left) | event | 5 | 5 |
| wrong (Check sort x5, 1 wrong) | event | 5 | 5 |
| a3b | how | 1 | 1 |
| wrong (Check x5) | event | 5 | 5 |
| office node x5 | none | 0 | 0 |

### Open
**Should fix: a tab change while a line plays leaves the old puzzle's hint, and Read speaks it** (general; it was
there in round 1 and I missed it then). `setActive()` only queues `V.how(k)`. `Curio.voice` writes the hint when a
line starts, not when it is queued. So a puzzle tab tapped during the room story (or any line) keeps the previous
puzzle's hint. If Read or a wrong line then drops the queued how line, the hint stays wrong until another line plays.

Tested with real held clicks:
- Server Closet, tab Network closet 1.5 s after entering, then Read: the hint and Read both say "Change the number of
  servers, then press Set servers." while the sorting puzzle is on screen.
- Records Room at 1000x625, tab Password, then Read: "Tap a box to take a folder away. Then press Check lock."

A solo student who presses Read hears the wrong puzzle's how-to (rule 4; POLISH "words match the state"). Fix:
`setActive` sets `setHint(L[k])` at once, as `enter()` already does, and keeps the spoken line as it is.

Gate:
1. Done when: pass. Done when 8 now holds at 375.
2. Every code taught: pass.
3. Defaults for a solo student: fails on the item above.
4. Sensitivity: does not apply.
5. No blocker or should-fix open: fails, one should-fix open.
6. Bundle clean: pass.
7. Voice counts: pass.

This was round 2, so by REFINE "Rounds" the integrator either makes this narrow fix itself or brings it to Cory.

**Integrator fix re-check (2026-10-28): PASS.** `setActive` now sets the hint straight away (src.html:863-864). I
re-tested with real held clicks:
- Server Closet, then the Network closet tab during the story, then Read: the hint and Read both say "Sort each part:
  wired or wireless. Then press Check sort."
- Records Room at 1000x625, then the Password tab, then Read: the C2 how-to.
- Plain tab switches (A2, A3, A1, A3, A2 and C2, C1, C2): each how line is spoken once and is silent on return.
  There are no doubles, and the hint matches the tab.
- Split taps: 30 of 30 at 1280, 1366 and 1920.

The gate now holds on all seven points.


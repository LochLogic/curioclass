# Data Defenders: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Refine

<!-- part: refine.md -->

PASS
Counts: blockers 2 (general 2, family 0), should fix 10 (general 8, family 2), polish accepted 10

### data-defenders: Refine

Lens files: refine/teaching.md (T), refine/play.md (P), refine/craft.md (C). Read them for frames and detail.

#### Blockers
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

#### Should fix
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

#### Polish accepted
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

#### Settled calls
- Team timer stays Off by default (BASELINE: the defaults work for a solo student); a teacher turns it on.
- The 1-server stripes start at 5 p.m. (4 p.m. is 450, under 500): the tool is right, the spec's "4 p.m. on" is a typo.

#### Exit check (round 1, 2026-10-28)

Cold re-check of every merged item, the new Network closet (A3) and the gate. Bundle `CURIO_DRAFT=1` 236 KB. Driven
with `scripts/drive.py` (ports 9610 to 9616, own profiles), 91 frames at 680x425, 800x500, 1000x625, 1280x720, 1366x768,
1920x1080 and 760x900 (hall, every puzzle, A3 step 1 with badges, A3 step 2 with badges, A3 done, exit, escape, all
secured), 13 at 375x812 via `--host` (host.html deleted after). Console clean in every shot. All looked at.

##### Merged items
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

##### Logic and numbers (recomputed in Python)
Sums 70, 67, 79, 65 (only Cy opens). Over capacity: 1 server 5 to 8 p.m., 2 servers 6 and 7 p.m., 3 = ceil(1400/500)
opens, 4 gives the idle line. A2 only C. Exit: one wrong card slides back ("5 of 6 are right"), all six escape.
Timer 20/30/Off, at 0 "Time!" and C1 still solves. No resource requests, localStorage only `curio-motion`, no em
dashes, no bare "Curio". voice/lines.json = allLines(), 58 of 58 word for word.

##### Voice check (held clicks, 0.12 s, Sound and Motion on)
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

##### Open (ROUND 2)
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

#### Round 2 re-check (2026-10-28)

Cold re-check after the builder's "Refine round 2". Bundle `CURIO_DRAFT=1` 241 KB (250,191 bytes). Same ports and
scratch folder. 49 frames: A3 fresh, A3 step 1 with badges, step 2 with badges, done, plus C1, I2 and hall, at
680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x900. 7 more at 375x812 via `--host`, and host.html
deleted after. Console clean in every shot.

##### The three A3 should-fix items
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

##### Polish
- **Access point drawing: done.** It is a plain Wi-Fi symbol with a cable to the switch. Its links to the laptop and
  tablet are radio arcs only, and the key says "Wi-Fi (wireless, no cable)". The map now matches the sort.
- **a3left: done.** It is spoken 5 times out of 5 taps of Check sort with parts left.
- **Done map at 680x425: done.** All five devices and their pills are in view, with the note below them.
- **Tablet note: done.**
- The engine bug (`badgeOn` with an x icon and text) is written up in handoff.md for the network family. The tool
  works around it.

##### Regressions
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

##### Open
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

<!-- end part -->

<!-- part: refine/craft.md -->

### data-defenders: Craft lens (round 1)

Cold read of spec.md, src.html, notes.md, handoff.md, art/prompts.json, voice/lines.json, kit/security.js and
docs/families/security.md (the new family engine and its doc). Bundled with `CURIO_DRAFT=1` (181 KB). Driven with
`scripts/drive.py` and held clicks (`hold 0.12`) on ports 9550-9556, own profiles in the lens scratch folder; about 90
shots. Browser voice (no clips yet) and placeholder art are expected and not reported.

Counts: blocker 1, should fix 4, polish 5, nit 4.

#### Contract

| Check | How | Result |
|---|---|---|
| One file | bundle `tools/data-defenders/data-defenders.html` | pass, 187,622 bytes (181 KB), under 2 MB |
| No network requests | `performance.getEntriesByType('resource')` after load: `[]`; grep of the bundle for `http`: only the SVG namespace and a code comment | pass |
| Nothing stored | localStorage holds only the kit's `curio-motion`; sessionStorage and cookies empty | pass; privacy line on screen ("Nothing you do here is saved or sent anywhere") |
| Console | every drive.py shot (about 90, every size and room, full solves, voice runs): no errors, warnings or exceptions | pass |
| Kit used | `Curio.voice`, `Curio.yes/tone`, kit header and Motion; `Sec.lock`, `Sec.clock`, `Sec.strength/band`, `Sec.seal`, `Sec.artifact('file' row / 'log')`, `Sec.world` | pass, nothing re-implemented |
| `sec.safeDomain` | `evil.com`, `gmail.com`, `x.test.evil.com`, `http://localhost`, `test`, `.test` false; `cedarhollow.example`, `https://x.example.com/a`, `a@b.test`, `EXAMPLE.ORG`, `https://evil.com@x.test` (real host x.test) true | pass |
| Engine numbers | bands Weak, Weak, Weak, Strong (with the tool's names); seals 70, 67, 79, 65 | pass |

#### Engine against the spec's family description, and the doc against the code

The engine matches the spec's family section: World `{name, people, accounts, files, domains}` with a guard that logs
one console error per non-reserved name; artifacts email, sms, login (fields never take typing), log, file, call, note;
spots with tap, Enter and Space; links that never navigate and show the real href in a status bar; `strength` pools
26/26/10/33, `bits`, `wordBits` (7776 words), the 20-password common list exactly as the spec lists it, `band` cut-offs
8 and 15, `seal` = sum, `caesar`, `vigenere(text, key, dir)`, `b64` (UTF-8 safe); `lock({check, normalize})` with
trim and lowercase default; `clock({mode, ms, onEnd})` with pause and reset; the pure block has no DOM and is
`__tool.sec`. `world()` does not look inside `files` (the spec lists files in the World); nit 3. Doc drift is in
nit 4 and polish 5.

#### Findings

##### Blocker

**B1. Split rooms swallow the first tap on the other puzzle (1280x720, 1366x768, 1920x1080).** general
- Where: src.html:836-837 (`renderRoom`: station `pointerdown` calls `setActive`, `focusin` calls `setActive` in split
  mode) with src.html:809/842 (focus restored by `data-k` after the rebuild).
- What: in split mode (stage at least 880 px wide, so every laptop and big-screen size) both puzzles show side by side.
  Pressing any control in the inactive station runs `setActive` on `pointerdown`, which rebuilds the station DOM under
  the pointer, so the `click` never reaches the button. Worse, the rebuild restores focus to the element focused before
  (`enter()` focuses the first C1 cell), whose `focusin` calls `setActive` back to the first puzzle. Net effect: the
  first one or two taps on Puzzle 2 do nothing, and the first puzzle's how-to line plays while the student is working
  on the second.
- How seen: `drive.py` held clicks at 1366x768, `__tool.state` after each (scratch sp0-sp3, spA, spI, spM):
  1 tap on "Tap to test" in Pick the password: active still `c1`, nothing tested; 2 taps: active `c2`, still nothing
  tested; 3 taps: tested. With no prior focus (mouse only): 1 tap only switches. A2 plan B and I2 row 2: first tap
  ignored. Voice logs: rep_c2 (5 taps on "Use this one" gave 3 results; "Tap a box to take a folder away. Then press
  Check lock." spoken at 11.5 s, after the student tapped the password station), rep_a2 (5 taps, 4 results), rep_i2
  (6 taps, 4 results), i2b (the right row needed three taps; "Add up each card..." spoken after the first tap on the log). At 1000x625 and below (tabbed) the bug does not occur.
- Better: switch the active station without rebuilding the pressed control (toggle classes on `pointerdown`, render on
  the next frame after `click`), and do not restore focus into the other station after a pointer switch.

##### Should fix

**S1. Focus is invisible on a marked score chip (Seal check).** family:security
- Where: kit/security.js:191-192 (`.sec-spot:focus-visible` and `.sec-spot.sec-marked` have the same specificity; the
  later `sec-marked` outline wins) and :254.
- What: a keyboard user who presses Enter on a score chip marks it; the chip is rebuilt and refocused, and its focus
  ring is replaced by the pale gold "marked" outline (`#ffd27a` on white), identical to the other marked chips. You
  cannot tell where focus is. Same for any marked/right/wrong spot that uses an outline in the siblings.
- How seen: frame `kb_i1_marked` (Enter on Ari Q1, Tab, Enter on Ari Q2; `document.activeElement` is Ari Q2, which
  looks the same as Q1).
- Better: give `.sec-spot:focus-visible` higher specificity (or put it after the mark rules) and draw marks with
  background/border so the focus outline stays on top.

**S2. Tap targets under 44 px.** family:security (chips, rows), general (Back)
- Where: kit/security.js:248 (`.sec-chip` min-width 40), src.html:242 (`.compactui .sec-chip{min-width:34px}`),
  kit/security.js:225 (`.sec-table` cell padding 6/8 px), src.html:224 (`.tabtop .back>span{display:none}`).
- What: Seal-check score chips are 40x44 at 1280 to 1920 and 760 wide, 34x44 at 680x425, 800x500, 1000x625 and 375
  wide (16 tap targets the student uses in every attempt). Change-log rows (the I2 spots) are 29-31 px tall at
  800x500, 1000x625 and 1920x1080. The icon-only Back button is 40x44 at 680x425, 800x500, 1000x625 and 375 wide.
- How seen: bounding boxes of every visible button and `role=button` per size (scratch m_*.json, h375_*).
- Better: chips at least 44 px wide (two rows of chips or a tighter seal chip in compact), `min-height: 44px` on
  spot rows in the engine, Back padding to 44 px.

**S3. The locked Exit door says nothing; its tap brings a late welcome over its hint.** general
- Where: src.html:715-717 (`doorTap`, locked Exit: `setHint(L.hExitLocked)` and a low tone only) with `speaks: '.door'`
  and `welcomeAfter` (src.html:632).
- What: a solo student who cannot read taps the Exit (the brass door is the most inviting) and hears only a buzz. The
  waiting moment does not say how to act (STANDARDS, "Say how to act"). On a first tap the welcome then arrives about
  4 s later and overwrites the "The exit opens when all three rooms are secured" hint.
- How seen: voice check first-tap run `ft_exitlocked`: tap at 1.21 s, welcome spoken at 5.35 s, final hint = welcome.
  Every later locked-Exit tap: no line at all.
- Better: speak `hExitLocked` as a how line (once, then hint only), and let it count as the tap's own line so the
  welcome is queued after it, or skipped.

**S4. Focus ring on the compact puzzle tabs is dark blue on the room's blue bar.** general
- Where: src.html:185 (`.tab:focus-visible` uses `--focus` #1d4ed8 inset) with src.html:216-219 (tabs moved into the
  room-colored `.rtop` in `compactui`).
- What: at 1000x625, 800x500, 680x425 and 375 wide the unselected tab is translucent white over #2f5ea8 (Records Room);
  the focus outline #1d4ed8 on it is about 1.7:1, below the 3:1 a focus indicator needs. On the green and orange rooms
  it is low too.
- How seen: frames `ctab_kb` (Shift+Tab from the first cell onto "Password"), zoomed.
- Better: in `.rtop` use the gold focus the Back button already uses (`outline: 4px solid var(--gold)`).

##### Polish

**P1. Lock slots never "pop" with Motion on.** general
- Where: src.html:176-178. `.rlock .ls.pop{animation:pop}` is followed by `.rlock .ls.pop{animation:flash}` (it was
  meant to be `.calm .rlock .ls.pop`), and line 177 repeats `.rlock .cnt` under `.calm`.
- What: Motion on and off both show the calm outline flash when a symbol is found; the pop the code defines never runs.
- How seen: `getComputedStyle(.rlock .ls.pop).animationName` = `flash` with Motion on (shot `pop_on`) and off.
- Better: scope the flash rule to `.calm`, so the found symbol pops with Motion on (same 0.6 s).

**P2. On room entry the hint, and so Read, is the story, not the action.** general
- Where: src.html:734 (`setHint(story)` on a first entry).
- What: while the story plays (about 10 s with the browser voice), Read speaks the story again, and Read pressed then
  also drops the queued how-to ("Tap a box to take a folder away...") until the next action. A non-reader who presses
  Read to learn what to do hears the story twice.
- How seen: voice run `read_during`: Read at 3.0 s spoke the story text; `c1` dropped (hush); nothing re-queued it.
- Better: keep the room's how line in the hint from the start (the story card in the panel already shows the story),
  or have `read` return the story plus the how line.

**P3. Wrong results wait behind the 10 s room story.** general
- Where: src.html:736 (story and how queued as one sequence) with `sayWrong` (src.html:647).
- What: a team that presses Check lock while the story is still playing hears "Not yet" only after the story ends, by
  then often dropped by their next tap. The panel result shows at once, so this is about the voice only.
- How seen: probe run: Check lock at 5.3 s, its "Not yet" dropped as newer at 9.6 s; the second one spoken at 11.7 s.
- Better: shorter story lines, or let a check result cut a how/story line already playing (`now: true` for results).

**P4. Engine controls the siblings will use are under 44 px.** family:security
- Where: kit/security.js:227 (`.sec-table th button` sort buttons, min-height 28 px), :240 (`.sec-tools select`,
  32 px), :220 and :222 (login fields and fake button, 40 px).
- What: not used by Data Defenders, but phishing-spotter and capture-the-flag will inherit them.
- How seen: code read.
- Better: 44 px minimums in the engine now, before the siblings build on it.

**P5. `Sec.band(string)` silently ignores names.** family:security
- Where: kit/security.js:56-58; docs/families/security.md "Pure checks".
- What: `band('Cedar2026')` is `OK`; only `band(strength('Cedar2026', ['cedar','hollow']))` is `Weak`. Data Defenders
  does it right, but the doc shows `Sec.band(r)` and the string shortcut is undocumented, so a sibling passing a string
  would teach a wrong band.
- How seen: shot `contract`: `Cedar2026` Weak with names, OK as a string.
- Better: `band(r, names)` (names passed through when r is a string), and say so in the doc.

##### Nit

**N1.** src.html:891-892, 905: `b` is computed and unused in `meterKey`; `i2Row` bumps `LK.i2.misses` directly
(src.html:988) instead of going through the lock. general

**N2.** Escape card (src.html:1169) has `role="dialog"` but no `aria-modal` or focus trap; Tab leaves it for the
panel behind the scrim. general

**N3.** `Sec.world` (kit/security.js:158-168) checks `domains`, `accounts` and `people` but not `files`, which the
spec's World includes. family:security

**N4.** Doc drift in docs/families/security.md: the `note` row says "`sticky` or `text`" (the code reads
`style: 'text'`, else sticky, plus `text`); the file-row seal's `icon` and the file `title` are not listed;
`onSpot` is called with `(id, el, tell, e)`, not `(id, el)`; the code comment at kit/security.js:389 lists `sort` as a
column key where the code and doc use `nowrap`. family:security

#### Access

- Keyboard: Tab goes header (Escape, Motion, Sound, Read), panel (timer, Start over, and in rooms Check lock / Clue),
  then Back, then the puzzle; in the hallway the four doors come after the panel (shots `kb_hall`, `kb_roomC`). Space
  and Enter toggle the C1 checkboxes; Enter on a log row picks it; Enter on an exit card then Enter on a slot head sorts
  it (`kb_exit_sort`). Tabbing from Puzzle 1 into Puzzle 2 in split mode switches the active station correctly
  (`kb_roomC_fwd`).
- Visible focus: kit 4 px outline everywhere except S1 and S4; doors and Back use gold on the dark/colored bars.
- Color never the only signal: C1 cells show a check or an x with "can open" / "no"; meter has the word and a pattern
  bar; A1 over-capacity bars are striped and labeled "too many" (or the number at narrow widths); A2 lost days are
  struck through with an x; doors carry their letter and icon.
- Motion: door swing and card slides off with Motion off, replaced by outline flashes of the same length (shots
  `door_calm`, `pop_calm`); see P1. Sound off: lines go silent and the hint still updates (`read_soundoff`). Read works
  with Sound off.

#### Lines

`__tool.allLines()` returns 48 strings; `voice/lines.json` has the same 48, word for word and in the same order. All
under 200 characters, no em dashes, nothing a voice would misread. Every spoken line in the runs below matched the
state on screen at its time (checked against the hint, room and active puzzle sampled when each line started), except
the stale `c1` line in B1.

#### Standard voice check

Held clicks, Sound and Motion on, 1366x768 unless named. Logs read from `__tool.vlog`.

**1. Repeats** (each action five times in a row; `rounds` = five full games on one page, with Start over between)

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| welcome | welcome | 1 | 1 (stage, mode button, timer, Tab key; 0 after Sound first, then 1 on Sound on, not again on off/on) |
| storyC, storyI, storyA | how | 1 each per page | 1 each, then silent 4 (rounds); storyC 1 over 5 entries (rep_enterC) |
| c1 | how | 1 | 1, then silent (rep_enterC: dropped by Back once, spoken on the next entry, silent 3) |
| c2, i1, i2, a1, a2, exit | how | 1 each | 1 each, then silent 4 (rounds) |
| i2b | how | 1 | 1 (run i2b) |
| back | how | 1 | 1, then silent 9 (rounds) |
| exitOpen | how | 1 | 1, then silent 9 (rounds) |
| hPlace (Open the exit with cards left) | how | 1 | 1, then silent 3 (exit_hplace) |
| wrong, C1 Check lock x5 | event | 5 | 5 |
| rShortName + wrong, C2 "Use this one" on "cedar" x5 | event | 5 + 5 | **3 + 3** (B1: first two taps swallowed) |
| i1wrong + wrong, I1 "This one was changed" on Ari x5 | event | 5 + 5 | 5 + 5 |
| wrong, I2 row 1 x5 (6 taps) | event | 5 | **4** (B1) |
| wrong, I2 wrong fix x5 | event | 5 | 5 |
| a1four + wrong, A1 Set servers at 4 x5 | event | 5 + 5 | 5 + 5 |
| wrong, A2 plan A x5 | event | 5 | **4** (B1) |
| wrong, exit with wrong cards x5 | event | 5 | 5 |
| symbol | event | 30 (6 per game x 5) | 30 |
| secC, secI, secA | event | 5 each | 5 each |
| escaped | event | 5 | 5 |
| time (timer at 0) | event | 1 | 1 queued, hint "Time! Keep going to finish." at once (time_evt) |

**2. Stale lines.** Fast taps (gap 0.2-0.25 s) through Check lock x3, Back, Start over, Yes (stale_c); Check lock, the
Password tab, two "Use this one", Back, Server Closet door at 1000x625 (stale_tabs); three "This one was changed" then
Back at 1366 (stale_late). Every overtaken line was dropped (`newer`, `chain`, `hush`); no line played after its
moment, none named a hidden control. The one stale line found is B1's (the first puzzle's how-to spoken after a tap on
the second puzzle, in split mode).

**3. First-tap timing.** Stage: welcome at +0.12 s. Mode button: +0.14 s. Timer button: +0.12 s. Tab key: at once.
Read: speaks the hint only ("Tap a door to go in...."), no welcome. Sound: nothing; Sound on brings the welcome once,
a second off/on does not repeat it. Door (its own line): story then how-to, no welcome (by design: the welcome is
valid only in the hall before any room). Locked Exit door: no line of its own, welcome 4.1 s later over its hint (S3).

**4. Read.** Read during the room story stops it and speaks the hint (read_during); with Sound off Read speaks the hint
(read_soundoff); Back right after Read takes the next line at once (read_then_back). See P2: during the story the hint
is the story.

**5. Order.** In every log the spoken lines follow the order of the actions; no older action's line played after a newer
one's.

#### Words

No em dashes in src.html, notes.md, voice/lines.json, kit/security.js or the family doc. "Curio Class" only (every
other "Curio" is `Curio.` code). Language classroom safe. Privacy stated on screen and in notes. Art: one token,
`art:dd-night-hallway`, has its prompts.json entry; no people.

#### Frames and runs looked at

contract; hall, C, I, I2, A, X at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x1000 (target and
fold measurements); 375x812 via `--host` (hall, C, I, A, X); kb_hall, kb_roomC, kb_roomC_fwd, kb_c1_space,
kb_i1_marked, kb_exit_sort, kb_compact_tabfocus, ctab_kb, ctab_kb2, kb_i2_rowfocus, i2row_kb, kb_i2_enter; pop_on,
pop_calm, door_calm, esc_card, esc_card_375; split0-3, splitI, splitA, splitC_mouseonly; voice runs probe, rep_c1,
rep_c2, rep_i1, rep_i2, rep_a1, rep_a2, rep_enterC, rep_exit, exit_hplace, exit_wrong, ft_stage, ft_door,
ft_exitlocked, ft_mode, ft_read, ft_sound, ft_timer, ft_key, read_during, read_then_back, read_soundoff, stale_c,
stale_tabs, stale_late, time_evt, rounds, i2b.

<!-- end part -->

<!-- part: refine/play.md -->

### Play lens: data-defenders (round 1)

Played twice: as a grade 5 student alone at home (real clicks, held presses, voice log read after each run) and as a
teacher projecting at 1366x768 and 1920x1080. Bundle `CURIO_DRAFT=1`, 181 KB. Driven with `scripts/drive.py` on port
9540 (own profile), 375 wide through `drive.py --host 9541` (host.html deleted after). No console errors in any of the
82 shots (the only log line was the host server's missing favicon).

Counts: blockers 0, should fix 4 (general 4, family 0), polish 7 (general 6, family 1), nits 5.

#### Should fix

1. **I2 log gives away I1** (Grade Book Room, both puzzles; src.html LOG row 4, "changed Cy's scores"). Rooms and
   puzzles can be done in any order, and in the split view the log sits right beside the seal cards. Row 4's action
   names Cy, so the answer to "which card was changed" is on screen before any adding (frames `i1-1366x768`,
   `i2-wrongfix`). It also makes I2 a word search for "Cy" instead of reading times and devices. Better: a neutral
   action ("changed quiz scores") until I1 is solved, or for good. The wording is in the spec's Content, so the
   integrator decides. Tag: general (POLISH, Games and quizzes).
2. **A2 strips show the answer before any pick** (Server Closet, Backup plan). Every plan's Mon to Fri strip is shown
   from the start, so the question "which plan loses the least work?" becomes "which card has the fewest red X's"
   (plan C has four green ticks, frame `a2-1366x768`). The thinking the clues ask for (same machine breaks with it, more
   often loses less) is never needed. Better: show a plan's strip after it is picked (wrong picks show their loss, the
   right one shows only Thursday lost), or have the student predict first. The spec draws the strips, so this may go
   to the spec's open questions. Tag: general (POLISH, Games and quizzes).
3. **375 wide: the I2 fix buttons are off screen** (`drive.py --host`, frame `f2/n-i2b`). After tapping row 4 the hint
   says "Now pick the first fix." but the three fix buttons sit at y 903 to 960 in an 812 tall phone, under the
   8-row log, with nothing in view pointing down. Done when 8 asks for the active puzzle's check control without
   scrolling. Better: scroll the fixes into view (preventScroll off for this one move, or scrollIntoView on the fix
   group) or dock them above the log on phones. Tag: general.
4. **The hint can stick on the room's story and never name the control** (any room, first entry). On first entry the
   hint shows the story (also shown in the story card) and only changes to the how-to when that line is spoken, about
   6 s later (`f4/h-door`: story at 3.5 to 5.5 s, "Add up each card..." at 7.5 s). If the how line is dropped, the
   hint never changes: pressing Read during the Server Closet story dropped `a1`, and 6 s later the hint still showed
   the story, which names no control (`f4/h-readdur`). A solo student is left without "press Set servers". Better: put
   the how-to in the hint at once on entry (the story already lives in the story card) and let the voice speak story
   then how-to. Tag: general (rule 4, "say how to act").

#### Polish

5. **C2 is solved by the meter word alone** (Records Room, Pick the password). Testing all four cards shows "Strong"
   on one, so the pick needs no judgment (frame `c2-1366x768`). Better: the meter shows the bar and the reason, and
   the band word appears after "Use this one", so the student weighs length and names first. Tag: family:security
   (the meter is the engine's `band`).
6. **Locked Exit as the first tap goes quiet, then the hint is overwritten.** Fresh page, tap the Exit: only a low
   tone, the hint shows "The exit opens when all three rooms are secured...", then about 4 s later the welcome is
   spoken and replaces that hint (`f4/h-exitlocked1`, welcome at 5.4 s, final hint = welcome). Better: speak the
   welcome within half a second and keep the locked hint, or give the locked door its own spoken line. Tag: general.
7. **All three rooms secured: the Exit door does not invite a tap** (frame `hall-all`). The door just shows an open
   padlock; the hint says "The exit door is waiting." without naming the action. Better: a soft brass glow on the Exit
   (an outline flash with Motion off) and "Tap the Exit door to open it." Tag: general.
8. **I1 sums read wrong after solving, and bare on small screens.** After the seal check is done, Cy's card shows
   "Added: 0" while the done bar says his scores add to 79 (frame `i2b-1366x768`). At 680x425 and 375 the "Added:"
   label is hidden, leaving a lone "0" next to a button that only says "Changed" (frames `i1-680x425`, `f2/n-i1`).
   Better: keep the last sum (or show 79 on Cy's card when done) and keep a short "Sum" label. Tag: general.
9. **A2 wrong pick explains nothing.** A wrong plan gets a dashed red outline and "Not yet. Look again, or press
   Clue." only (frame `a2-1366x768`); PLANS already holds a `why` for plan A that is never shown. Better: one line per
   wrong plan in the result area ("Plan B loses Monday to Thursday: a week-old backup."). Tag: general.
10. **Projected A2 day chips are tiny.** At 1920x1080 the "last Fri / Mon ..." chips are about 11 px with a strike
    through, hard to read from the back of a room, while half the station is empty (frame `a1-1920x1080`). Better:
    scale the plan cards and chips with the station. Tag: general.
11. **Spoken wrong reason for a wrong fix in I2 is missing.** The why ("The log is how you found the change...") shows
    in the panel but only "Not yet" is spoken, unlike C2 where the meter reason is spoken. Better: speak the why as
    the event line, like C2. Tag: general.

#### Nits

12. Exit slot head truncates to "Confidenti..." at 680x425 and 375, and at 680x425 the slot boxes are mostly below
    the station's fold (frames `exit-680x425`, `f2/n-exit`).
13. A1 chart: the value labels "450" (1 server) and "300" sit on the dashed capacity line (frames `a1-1366x768`,
    `a1-680x425`).
14. Escape card: behind the dialog the empty pool still reads "All six cards are in slots. Press Open the exit."; the
    exit station header says "Puzzle 1" though there is only one (frame `escaped`).
15. 375 hallway: "Grade Book Room" wraps to two lines, so the first row's doors differ in height (284 vs 303 px).
16. I2: the fix the student picked wrongly gets no visual mark (only the result text).

#### What worked

- First screen says what to do ("Tap a door to go in"), the hallway reads at once, doors are big at every size.
- Voice (held clicks, 3.5 s gaps): five wrong checks in C1 gave 4 spoken "Not yet" plus 1 dropped as stale on the next
  tap, as the spec asks; C2 meter reasons spoken each time; how lines spoken once then `silent` on tab switches; Sound
  off and on brings the welcome once; Read speaks the hint and clues; rapid taps then Back then a new door left no
  stale line.
- Keyboard: Tab through header and panel to the doors, Enter opens a room and focus lands on the first grid cell.
- Calm mode keeps the same timing (door 450 ms, auto-advance 1600 ms either way); Team timer 20 min counts, at 0 shows
  "Time!" and nothing locks.
- Main controls in view at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760 wide; in the 375 host
  every check control is in view except the I2 fixes (item 3).

#### Frames looked at

Scratch: `C:\Users\Cory\AppData\Local\Temp\claude\S--\98b8b046-f7f2-48d0-a719-c61ce01237be\scratchpad\lens-dd-play`
- `f1/`: hallway at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x1000; each of C1, C2, I1, I2
  step 2, A1, A2, exit at 1366x768, 800x500, 760x1000, 1920x1080, 680x425; extremes c1-badges, c1-clue2, c1-done,
  c-secured, hall-1secured, i2-wrongrow, i2-wrongfix, a1-two, a1-four, a1-done, hall-all, exit-partial, exit-wrong,
  escaped, timer20, timeup, startover, exitlocked-tap, calm-hall.
- `f2/` (375 host): hallway, C1, C1 wrong x2, C2 tested, I1, I2, I2 step 2, A1 two servers, A2, exit, all secured,
  escaped.
- `f3/`, `f4/`, `f5/`: voice and hint runs (first taps, Read, Sound, tab switches, fast taps, keyboard, Sound off).

<!-- end part -->

<!-- part: refine/teaching.md -->

### data-defenders: Teaching lens (round 1)

Cold read of spec.md, src.html, notes.md, art/prompts.json, voice/lines.json, kit/security.js (pure checks); bundle with
`CURIO_DRAFT=1` (181 KB). Driven with `scripts/drive.py` (ports 9530-9531, own profile in the lens scratch folder), 21
shots, console clean in all. Every number recomputed in Python. Standard wording read from the official PDF, "2026 CSTA
PK-12 Computer Science Standards" (statements and boundary statements, pp. 79-82), since the repo holds only the ids.

Counts: blocker 1, should fix 3, polish 2, nit 3.

#### Standards (rule 2)

| Code | Statement (CSTA 2026) | Taught by | Verdict |
|---|---|---|---|
| E5-SYS-SE-13 | Describe the concepts of the CIA triad and how each component is important in protecting information. Boundary: confidentiality as keeping a password secret and not sharing PII; integrity as data accurate and unchanged ("grades in a gradebook haven't been improperly changed"); availability as accounts and systems there when needed ("the system isn't down or blocked"). | Three rooms, each fixed by a real action: C1 least privilege, C2 password; I1 seal (checksum), I2 log review; A1 enough servers, A2 backups kept apart. Secured lines name each promise; the exit sort makes the student apply all three to six new cases. | Taught well, above the minimum (the gradebook example is the boundary's own). See should fix 2 on the integrity wording. |
| E5-SYS-NT-14 | Distinguish between the components of wired and wireless networks. Boundary: devices (computers, tablets, phones), connecting hardware (routers, switches, cables), wireless connections (Wi-Fi signals). | Nothing. No router, switch, cable, Wi-Fi or device-connection appears anywhere; "server" in A1 is a capacity unit, not a network component. | Not taught. Blocker 1. |

#### Done when

| # | Check | How | Result |
|---|---|---|---|
| 1 | Rooms in any order; Exit locked until all three secured | 02: real held click on Exit at start, room stays `hall`, hint "The exit opens when all three rooms are secured..."; 10/11: rooms solved in C, I, A order and via direct `enter` in others | PASS |
| 2 | C1 only with Content grid; counts; badges after two. C2 bands; only card 4 | 03: all ticked gives "8 boxes give too much access." (4 x 3 private cells - 4 needed = 8), twice, then 4 "!" badges; 04: one wrong cell each way gives "1 box gives too much access. 1 person can't do their job."; right grid opens. `sec.band`: cedar 5 ch Weak (name), Cedar2026 9 ch Weak (name), password1 9 ch Weak (list), "purple tiger skates home" 24 ch Strong; cards 0 to 2 do not open, 3 does | PASS |
| 3 | I1 sums 70, 67, 79, 65, only Cy. I2 row 4 then backup fix | 06: on-screen "18 + 15 + 20 + 17 = 70", "= 67", "= 79", "= 65" (Python agrees; Cy's seal 59); Ari, Bea, Dot do not open. 07: rows 1-3, 5-8 keep step 1; row 4 moves to step 2; fixes 2 and 3 do not open; fix 1 does | PASS |
| 4 | A1 only at 3; 1, 2, 4 results. A2 only plan C | 08: 1 server "5 p.m. to 8 p.m. have too many visits" (Python: 900, 1,400, 1,100, 600 > 500); 2 "6 p.m. and 7 p.m." (1,400, 1,100 > 1,000); 3 opens (1,500 >= 1,400, ceil(1400/500) = 3); 4 "That works, but one server would sit idle." 09: A, B, D do not open, C does | PASS (spec text wrong for 1 server, nit 1) |
| 5 | Exit only with all six right; wrong slide back | 10: five right, one wrong: "5 of 6 are right and stay put. 1 slid back"; the wrong card back in the pool, right cards keep a check; 11: all six right gives the escape card | PASS |
| 6 | Timer Off/20/30; at 0 nothing locks | 12: timer forced to 0.12 s, `timeUp` true, " Time!" shown, C1 then solves | PASS |
| 7 | Voice | held-click run: welcome spoken once, storyC once, c1 spoken once then `silent`, wrong spoken 3 of 3, Read `read` | PASS on this run (full counts are the Craft lens's) |
| 8 | Sizes, check button visible | 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x1000: Check lock, Changed and Set servers all inside the viewport | PASS for these; 375 via `--host` left to Play |
| 9 | safeDomain, console, network, storage, name | `safeDomain`: evil.com false, gmail.com false, cedarhollow.example, example.com, x.test true; console clean; localStorage holds only `curio-motion`; "Curio Class" only | PASS |

#### Facts

All checked against the spec's Sources: NIST CSRC definitions (C, I, A, least privilege, checksum: "stored together with the
object, for detecting changes" matches the seal), NIST SP 800-63B-4 (length first, block context words and common
passwords; 15+ for Strong), the NCSC list (cedar/Cedar2026/password1 reasons), CISA backups kept apart and DoS framing.
Lengths 5, 9, 9, 24; sums 70, 67, 79, 65; capacities 500, 1,000, 1,500, 2,000; C1 extra boxes 8. All match the screen
and notes.md.

**Security family check:** Cedar Hollow and everyone in it are made up; the only addresses are `cedarhollow.example`
and its subdomains (gradebook, room12-laptop, office-desk, nurse-desk), all reserved under RFC 6761. No real brand, site,
product or person. No attack steps: the stolen password is named as the cause, never how it was taken; the virus and the
report-card-night load are outcomes only; the defenses (least privilege, strong password, checksum, log review, capacity,
off-site backups) are all defensive. Rule 5: nothing cultural, Native or hard-history; no sensitivity agent needed.
Rule 8: no sensitive standards topic. Guardrails: grade 5, timer off by default, no hard history.

#### Findings

##### Blocker

**B1. E5-SYS-NT-14 is on the module and not taught at all.** spec.md "Who and how", src.html:10, module
`computer-science-5-the-cia-triad`. The code is "Distinguish between the components of wired and wireless networks"
(devices, routers, switches, cables, Wi-Fi). Nothing in the tool shows or asks about a network component; the spec's
own crosswalk lists only 1B-NI-05, so the code was carried over from the module list without an activity. No other
grade 5 tool teaches it (the grade 5 CS modules are Remix a Program, Train a Classifier, Human-Centered Design;
network-help-desk teaches the grade 4 version, E4-SYS-NT-14, comparing wired and wireless connections). REFINE gate
item 2 fails until this is settled. A real activity that fits the Availability room: a **Network closet** puzzle with
the school's network drawn in code (router, switch, cables to the office desktops, a Wi-Fi access point, Room 12
laptops and tablets). The student first sorts each part as wired or wireless (or device, connecting hardware, signal),
then on report card night the Wi-Fi access point fails and the student predicts which devices stay online (the cabled
ones) and picks the fix (a second access point or a cable to the front-desk computer), so the component distinction is
what keeps the system available. That adds a puzzle, so it goes to the spec's open questions; otherwise move NT-14 off
this module and queue a grade 5 networks tool (rule 10), with the move written down. **general**

##### Should fix

**S1. A2 shows the answer on every plan card before the student picks.** Server Closet, Backup plan, `src.html:1052`
(the `.days` strip is drawn for every plan from the start), frame 09-a2. The question is "Which plan loses the least
work?" and each card already shows its kept and lost days in green and red: plan C has four green checks, the rest one
or none. A student counts green and taps C without thinking about where the copy lives or how often it is made, which
is the whole lesson (the spec's clues "A backup on the same machine breaks with it" and "More often means less lost"
never get needed). Better: show each card as text plus a blank Fri-to-Thu strip; on a pick, the disk breaks on Thursday
afternoon and that plan's strip fills in (lost days struck), with a one-line reason ("The backup broke with the
server."), so a wrong pick teaches and the right one is reasoned first. **general**

**S2. The Integrity promise, "nobody changes it in secret", does not fit the exit card it must sort.** `ROOMS.I.promise`
(`src.html:478`), shown in the hallway story card, the exit's I slot head, and the escape card; the spec's One idea
uses it too. Frame 10-exit. The exit card "A typo changed a bus time, and nobody checked it." is I, but a typo is an
honest mistake, not a secret change, so a grade 5 student matching the card to the slot heads has no reason to pick I.
NIST's integrity is "guarding against improper information modification or destruction", accidental or not, and the
tool's own secured line already says it better: "Integrity means data stays correct, and changes can be checked."
Better: promise "it stays correct, and changes can be checked" (or "it stays correct and nobody changes it without
a check") everywhere the promise appears, and the same in spec.md. **general**

**S3. The least-privilege answer gives a parent the whole Bus routes folder.** C1, `C1P` (`src.html:546`), frame 03.
Jordan's dad's job card is "I check when the bus comes", and the only answer that opens the lock gives him Bus routes,
the same folder the bus driver uses, which in a real school lists every child's stop. A teacher talking about least
privilege will notice that the "right" answer hands a parent other families' information, the opposite of the room's
point. Better, keeping four columns: make the public column "Lunch menu and bus times" (public) and Jordan's dad's
correct row nothing private at all ("a parent only needs what is public"), with clue 2 changed to "Some people need
only the public folder." If the grid changes shape it goes to the spec's open questions. **general**

##### Polish

**P1. I2 row 4 can be found by the name, not by reading the log.** `LOG` row 4 action "changed Cy's scores"
(`src.html:562`), frame 07-i2. The student has just found Cy in I1, so "Cy" in the action column points straight at
the row; the time (2:14 a.m.) and the device (unknown laptop), which are what log review teaches, are never needed.
Better: action "changed Quiz 4 scores", and change one daytime row to a normal edit (for example Mon 8:12 a.m.,
ms.ortiz, Room 12 laptop, "changed Quiz 4 scores", fixing a typo), so two rows make the same change and only the time
and device tell them apart. The I1 link still holds (the done bar names Cy). **general**

**P2. C2's meter rates every password before the student chooses.** Records Room, Pick the password, `BUILD.c2`
(`src.html:909`), frame 05-c2-tested. Tapping a card shows Weak or Strong and the reason, and the how line says "Then
press Use this one on the strongest", so the choice is reading a label. The reasons are good teaching; the order wastes
them. Better: the student picks first with "Use this one"; the meter then runs on that pick and gives its reason, and a
Weak pick says "Not yet" with the reason (the spec's wrong-text path already does this). Testing other cards can open
after the first pick. Keeps the spec's content, changes only the order. **general**

##### Nit

**N1. Spec text for A1 at 1 server says the striped bars start "4 p.m. on".** spec.md Content, A1. 4 p.m. has 450
visits, under 500; the tool correctly shows 5 p.m. to 8 p.m. (handoff says so). Fix the spec line. **general**

**N2. Log row 8, "entered Quiz 5 scores", sits after the tampering but the cards show only Q1 to Q4 with the old
seal.** `src.html:566`. A grade book that saves Quiz 5 would store a new seal over Cy's changed scores, and the cards
have no Q5. Better: row 8 "printed a class list" or similar, touching no scores. **general**

**N3. `Sec.safeDomain` passes brand look-alikes inside reserved names.** `kit/security.js:28`; a test call gave
`google.com.example` true. Not an issue here (only cedarhollow.example), but phishing-spotter and capture-the-flag
will draw look-alike addresses; a short brand blocklist check (or a rule that the label before `.example` holds no
real domain) would keep "no real brands" enforced by the engine, as the family doc promises. **family:security**

#### Frames looked at

01-hall, 02-exit-locked, 03-c1-wrong2, 04-c1-partial, 05-c2-tested, 06-i1, 07-i2, 08-a1-1, 09-a2, 10-exit, 11-escaped,
12-timer, s-680x425, s-800x500, s-1000x625, s-1280x720, s-1366x768, s-1920x1080, s-760x1000, v-voice (in the lens
scratch folder, `lens-dd-teaching/frames`).

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Data Defenders: build handoff

Grade 5 escape room, the first tool of the security family. Built 2026-10-27 to `spec.md`; Refine round 1 applied
2026-10-28 (see the end of this file). Stage: built (not committed). Bundle:
`CURIO_DRAFT=1 python scripts/bundle_tool.py data-defenders` (about 241 KB).

#### What was built

- `kit/security.js` (new): the family engine, global `Sec`. Full API in `docs/families/security.md`.
- `docs/families/security.md` (new): the family doc (engine API, sibling rules, sibling table).
- `tools/data-defenders/`: `src.html`, `tool.draft.json` (stage built), `notes.md`, `voice/lines.json` (59 lines
  from `allLines()`, bank hero-coach, voice Puck; not recorded), `handoff.md`. `art/prompts.json` and
  `art/dd-night-hallway.webp` were already there and are used as is.
- No other kit file was changed. The Network closet reads `kit/network.js` (`Net.graph`, `Net.reach`, `Net.draw`,
  `Net.icon`) as is.

#### How src.html is laid out

- Header: title, "Cedar Hollow Elementary", one Escape mode button, Motion, Sound, Read.
- Panel (first in the DOM, for tab order): `#hint`, `#ctl` (the active puzzle's check controls), Clue, the room's
  story card, Team timer (Off / 20 / 30), Start over with a Yes / No confirm, the made-up note.
- Stage: `#hall` (hallway art plus four HTML door buttons laid out in JS at real size) and `#room` (top bar with
  Back, room name and the room lock; tabs; `#stations`). `#escape` is the final card.
- Layout follows collision-lab: `wide`, `compact`, `stack`. In `stack` the hint moves to `#topSlot` and the controls
  to `#ctlDock`, right by the puzzle. Stations are `split` when the room has two puzzles and the stage is at least 880 px
  wide, `tabbed` otherwise (always for the Server Closet's three), `single` in the exit. `.compactui` (compact layout or stage under 560 px) tightens everything and moves the tabs into
  the room's top bar with short names; `.tiny` (stage under 440 px) lets seal-check rows wrap; `.n3` (three puzzles) drops the tab icons and tightens
  the tabs so the short names fit.
- Content tables at the top of the script: `WORLD`, `ROOMS`, `PUZ`, the line table `L` (with two clues per
  puzzle), and each puzzle's data. Every puzzle has a `Sec.lock` in `LK`; `solved(p)` is the one path to success.
- Test hook: `window.__tool = {state, sec, Sec, world, enter, toHall, solve(p, answer), setActive, setTimer, clock,
  locks, cards(), c1Errors, allLines, vlog, vq, restart, relayout, Net, online, parts}`. `solve('a3', {sort, picks})`
  runs both A3 steps.

#### Tricky parts

- Voice: `welcomeAfter` with the welcome valid only in the hall before any room is entered (and `hint: false`, so
  it never overwrites a hint), so a first tap on a door goes straight to the room story instead. On entry the hint
  shows the puzzle's action at once; the story is spoken with `hint: false`, then the action. Each room's story plus its how line is spoken once; symbol, secured and
  wrong lines every time. A wrong line cuts in (`now: true`) and goes stale on the next tap (`state.tap`), so fast tapping never queues a pile.
- The door swing and the Motion-off outline flash both take 450 ms, so timing is the same either way.
- Renders rebuild a station's DOM; focus (by `data-k`) and scroll are restored across a rebuild. In split mode,
  `setActive` only toggles `.station.active` and redraws the panel, so the station under the pointer is never rebuilt
  mid-tap (this was Refine blocker 1).
- A3's answer is not hand-written: `ONLINE` is `Net.reach(net(), 'router')` filtered to the five devices, with the
  access point `up: false`.
- Tests: `enter()` called synchronously then a click can race a ResizeObserver relayout; wait about 500 ms.
- In `stack`, the kit's `html, body {height: 100%}` would clamp `main`; `body.stack` sets height auto and
  `align-content: start` so the room and the panel never overlap.

#### Done when (spec)

1. Rooms in any order, exit locked until all three are secured: pass.
2. C1 opens only with the right grid; wrong checks report counts, "!" badges after two. C2 bands Weak, Weak, Weak,
   Strong; only the fourth opens: pass.
3. I1 sums 70, 67, 79, 65; only Cy opens. I2 needs row 5, then the backup-and-new-password fix: pass.
4. A1 opens only at 3; 1, 2 and 4 give their results. A2 opens only with plan C. A3 opens only with the right sort,
   then exactly office, nurse and printer: pass.
5. Exit opens only with all six right; wrong cards slide back; real pointer drag works: pass.
6. Timer Off / 20 / 30; at 0 it says "Time!" and nothing locks: pass.
7. Voice: welcome once, how lines once, events every time, Read speaks hint and clue: pass (checked on the voice log
   with held clicks).
8. Every STANDARDS size with the active check button visible without scrolling, 375 via `drive.py --host`: pass
   (frames looked at: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x1000 stack, 375x812).
9. `Sec.safeDomain('evil.com')` and `('gmail.com')` false; console clean; no network requests; nothing stored by the
   tool (only the kit's Motion choice); "Curio Class" only: pass.

#### Spec notes

- A1 with 1 server: the spec now says 5 p.m. to 8 p.m. (4 p.m. has 450 visits).
- A2 day strip: "Mon to Fri" read as last Friday through Thursday, since the disk broke Thursday afternoon.
- The exit's two clues are not in the spec; I wrote them. I2's wrong-fix reasons are my wording (now spoken too, and in the spec).

#### Known gaps

- 1920x1080: the puzzles sit at real size, so the stations have empty space below.
- 680x425: the I2 change log scrolls inside its station; the exit pool scrolls too. Both work.
- Voice lines are not recorded yet (`voice/lines.json` is ready).

#### Refine round 1 (2026-10-28)

All items in `refine.md` were applied: both blockers (split-room taps, the new Network closet puzzle), should-fix 3
to 12, polish 13 to 22 and the cheap nits. Summary in the spec's "Refine changes (round 1)". Engine changes in
`kit/security.js`: `band(r, names)` and `reasons(r, names)` take names for string input, `safeDomain` rejects a real
top-level label before the reserved suffix, `world` checks files, 44 px targets, focus ring over marked spots
(documented in docs/families/security.md). Checked: logic run at 1366 (every puzzle wrong then right, exit), 5 of 5
split taps at 1280, 1366 and 1920, the voice log (locked exit, entry hint, cut-in, Read, fix reasons), target sizes
and focus rings at 680, and frames at every STANDARDS size including 375 via `drive.py --host`.

#### Refine round 2 (2026-10-28, exit check items, all in A3)

- Part notes and the wired / wireless definition show at every size (shorter notes; the prompt is no longer `opt`).
  At 375 (`.tiny`) the cards stay two columns (tile icon and button icons dropped), and sorting the last part
  scrolls Check sort into view (measured: top 380 of 812).
- Result and "!" marks are the tool's own SVG overlay (`.a3over`), not `view.badge`: a pill centered on each tile's
  bottom edge, its font shrunk to fit the narrowest gap between devices; the pick check is a small circle inside the
  tile's top right corner. No overlap at 375 to 1920.
- The access point is drawn as a plain Wi-Fi symbol (`skin.drawIcon`); its Wi-Fi links to the laptop and tablet
  show only the radio arcs (the dashed line and break mark are hidden), and the two devices carry a small Wi-Fi mark.
  Its note says it plugs into the switch with a cable and sends out Wi-Fi; the key says "Wi-Fi (wireless, no cable)".
- Check sort with parts left speaks `a3left` as an event (3 taps, 3 lines). The done note sits under the map, so the
  finished map is in view at 680x425. Tablet note: "no network cable port; uses Wi-Fi".

##### Engine bug for the network family (kit/network.js, not changed here)

`badgeOn` with `{icon: 'x', text}` draws the x at the pill's start and centers the text over it, and the width
(`10 + text.length * 8`) leaves no room for the x, so `{icon: 'x', text: 'offline'}` reads "Xffline". It also uses the
class `net-x` for that badge, the same class as the down-node x, so one replaces the other. Pills are not clamped to
the gap between tiles, so at narrow sizes they spill over neighbours. Fix: give the x icon the same 16 px allowance and
left text anchor as check / lock, and keep a separate class for a tool's x badge.

#### For Cory

- Settled in Refine: the Team timer stays Off by default; a teacher turns it on.

<!-- end part -->

## Log

- 2026-11-25: refine.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/craft.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/play.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-10-28)
- 2026-11-25: handoff.md folded in (last changed 2026-10-28)

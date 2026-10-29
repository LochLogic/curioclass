# Teaching lens: network-help-desk

Cold read of spec.md, src.html, notes.md, voice/lines.json (no art folder: the spec says art is drawn in code), the
draft bundle (`CURIO_DRAFT=1`, 119 KB), then my own drives at 1366x768 (`drive.py`, port 9402, held clicks and
`__tool` calls) and `audit_tool.py` (ports 9400 and 9401). Frames and JSON results are in
`S:/CurioClass-codex-scratch/lens-teaching/` (`frames/`, `drive/`, `audit/`, `calls-result.json`, `house-result.json`).
I did not read codex-report.md, handoff.md or CODEX-BRIEF.md before writing the findings.

Counts: blockers 0, should fix 8, polish 6, nit 2.

## Standards on the module (rule 2)

Module computer-science-4-wired-wireless-and-login: E4-SYS-NT-14, E4-SYS-SE-13, E4-SYS-HW-12 ("Network connections;
authentication vs authorization").

- **E4-SYS-NT-14 (network connections): taught.** Q1 reveals cable, Wi-Fi or Guest Wi-Fi on the map; calls 1, 2, 4, 5
  are four different broken paths; House lets the student pull the desktop cable, turn Wi-Fi off, flip the router and
  drag the tablet through 3, 2, 1, 0 bars. Something the student does, every time.
- **E4-SYS-HW-12 (troubleshoot and test a fix): taught.** Ask, back a cause with a clue, send the fix, watch the test
  ping, and a wrong claim pings to the broken spot. Weakened by the cheap paths in S1 and P2, but the loop is real.
- **E4-SYS-SE-13 (authentication vs authorization): taught, but thinner than the tool's "One idea" promises.** Calls
  3 and 6 (Logging in) against 7 and 8 (Permission), and House (Caps Lock fails Library site only; Kid or Guest
  account fails Parent settings only), do put the difference in front of the student. But the student never has to
  sort a call into a kind: see S2.

## Done when

| # | Check | Result | How I saw it |
|---|---|---|---|
| 1 | All six answers per call, map lights the matching part | Pass on text (all 48 answers match the Content table word for word); map caveat in S3 | `calls-result.json`: each call opened, Q1 to Q6 asked, clue text, badges, screen and login notes read after each |
| 2 | Cause plus one key clue: right stamp and fix sentence, ping reaches the cloud, printer or page | Pass, 8 of 8 (Connection 1, 2, 4, 5; Logging in 3, 6; Permission 7, 8; call 8 pings laptop to printer) | same run, solved card text and `state.ping.arrived` |
| 3 | Right cause with non-key clue asks for a proving clue; wrong cause stops at an X with the nudge for the first unasked key | Pass, 8 of 8 (nudge checked with no key asked, then with the first key asked, for every call) | `nudge*.json`, frames `t-c1-needclue`, `t-c5-wrong` |
| 4 | +1 per question, +2 per wrong claim, no score, Shift report lists 8 | Pass (6 questions = 6 min, one wrong claim = 8 min; need-clue adds nothing; report has 8 rows) | `calls-result.json`, frame `t-report` |
| 5 | House rules | Pass: router off fails all 24 device and target pairs; shed tablet 0 bars fails all four; Caps Lock fails Library site only; Guest network fails Family printer only; Kid and Guest accounts fail Parent settings only | `house-result.json` (6 devices x 4 targets in 10 states) |
| 6 | Voice | Audit voice rows, see Audit pilot; the Craft lens owns the full count table | audit |
| 7 | Sizes | See Audit pilot | audit |
| 8 | Keyboard-only solve; Motion off keeps timing; console clean | Keyboard: pass (call 1 solved with Tab and Enter only, focus lands on Next call). Motion off: pass (fix 1503 ms on, 1510 ms off; ping 1221 ms on, 1222 ms off). Console: clean in every normal run, but S7 throws | `kb.json`, frames `t-c6-solved`, `t-c6-solved-calm` |

## Facts

- Wi-Fi bars recomputed from router (300, 330), straight distance in design units: Living room 108.17 (3), Kitchen
  255.54 (2), Bedroom 361.39 (2), Back door 480.83 (1), Shed 648.46 (0). The code's thresholds (250, 420, 560) give
  the same bars as the spec. The spec's "Kitchen 255" is 255.54 cut short; it changes nothing on screen (no distance
  is ever shown, only "about N bars of 3").
- Call fix sentences, kind lines and cause groups match the spec. Airplane mode, case-sensitive passwords, guest
  networks and distance through walls each trace to a listed source.
- The "Allowed" badge on Ana's laptop after call 8 states something the lesson says is false: S5.

## Findings

### S1. Should fix (general): the cause can be found by trying every card
Where: Calls, claim step (`claim()`, the `need-clue` branch). What: with any one clue selected (even one that proves
nothing), a right cause answers "Right cause. Which clue proves it? Tap a different clue." and a wrong cause answers
"I tried that." So a student can ask one question, pick that clue, and tap down the 7 cause cards until "Right cause"
appears, then try clues. It costs only display minutes. All 8 calls answer `need-clue` for the right cause with a
non-key clue (`calls-result.json`). This is the wave lesson "no puzzle can be solved by trying every option for
free". Better: judge the clue before the cause. If no selected clue is a key clue, answer the same way for every cause
("That clue doesn't prove a cause yet. Pick a clue that shows what is broken."), so the reply never confirms a cause on
weak evidence. Spec change (the need-clue line), so the integrator may route it.

### S2. Should fix (general): the student never sorts a call into one of the three kinds
Where: Calls, claim step and Solved card; spec "One idea". What: the tool promises "you learn to sort every 'it won't
connect' into one of three kinds", and that sort is what carries E4-SYS-SE-13. But the cause board prints the kind
over each card (Connection, Logging in, Permission), and the Solved card stamps it afterwards. A student who matches
the screen words to a card (P2) solves calls 3, 6, 7 and 8 without once deciding "is this logging in or
permission?". Better: make the kind the student's own call. Either the claim step opens with three big kind buttons
and then shows only that kind's causes (a wrong kind gets a kind nudge: "Logging in worked here. Look at Q5."), or
the cause cards come unlabeled and the student picks the kind stamp before Send fix. House could ask the same (P3).
Spec change; integrator may route it to open questions, but rule 2 says the code should be taught well, not only met.

### S3. Should fix (general): the map draws unknown parts as working
Where: Calls map (`updateMap`, `l.up=...asked.includes(4)?original.up:true`; router `n.up=!s.asked.includes(2)||m.up`).
What: after Q1 alone, call 1 shows a solid, plugged-in cable from the desktop to the router (frame `t-c1-q1`); call
3 shows a working Wi-Fi link though the Wi-Fi password failed (`t-c3-q1`); call 5 shows the router sending Wi-Fi arcs
and a live line to the internet before Q2, though it has no power (`t-c5-q1`). The map then reverses itself on Q4 or
Q2. A student reading the map as evidence learns the wrong thing first ("the cable is fine"). Better: until the
question that reveals it is asked, draw the part as unknown (the grey dotted "?" style the tool already uses before
Q1), never as working.

### S4. Should fix (general): the internet cloud sits in the Kitchen and its line runs through devices
Where: Calls and House map, cloud node at (850, 80) inside the house outline. What: the router-to-internet line passes
through the Phone in House and in calls 1, 5 and 6 (frames `t-house`, `t-c1-q1`, `t-c5-q1`), and through Mr. Patel's
laptop in call 3 and Ana's in call 8 (`t-c3-q1`, `t-c8-solved`). Those devices look cabled to the internet, which is
exactly the thing Q1 asks about. Better: put the Internet cloud outside the house walls (beyond the top right corner,
on the lawn side) so its line crosses no room with a device. The 375 wide layout already does this (audit frame
`size-375x812 (iframe host).png`); the wide layouts don't.

### S5. Should fix (general): call 8's Solved badge says "Allowed" on the guest laptop
Where: Calls, call 8 Solved (`updateMap`, solved badge text by kind). What: after the fix, Ana's guest laptop wears a
green "Allowed" badge (frame `t-c8-solved`), while the fix sentence says the Guest Wi-Fi keeps her away from home
devices on purpose. She is still not allowed; a family laptop prints. The kind line also says "The account just
isn't allowed" where the block is the guest network. Better: Ana's badge "File sent" (or keep "Guest") with the check
on the family laptop, and a kind line that fits both calls 7 and 8 ("Logging in worked. That account or network just
isn't allowed to do that, on purpose.").

### S6. Should fix (general): after a nudge the Permission cause is cut off at 1366x768
Where: Calls, claim step at 1366x768. What: once a wrong claim or the need-clue reply puts the nudge on screen, the
cause board shrinks and the Permission group shows only its heading; "Not allowed" is below the board's edge (frames
`t-c5-wrong`, `t-c1-needclue`). The board scrolls, so the audit does not flag it, but a student retrying a call sees
two kinds and not the third. With two clues and no nudge it fits (`t-c1-claim`). Better: all seven cards in view in
every claim state at 1366x768 (tighter cards, or the nudge under Send fix in the space the clue strip leaves).

### S7. Should fix (general): a resize during a wrong-claim ping locks the call
Where: Calls, connection calls 1, 2, 4, 5 (`runPing` adds a `fault` node; a `ResizeObserver` redraw rebuilds the map
without it). What: when the map box changes size during the wrong-claim ping, the engine throws (`px` in
`linkPoints`, an uncaught exception) and the call stays `busy`: Send fix and Back to questions both stay disabled and
the questions are hidden. Only another phone or a mode change gets out. Reproduced by changing the map's size 250 ms
into the ping (`dbg3.json`) and by asking a question and claiming at once through `__tool` (`dbg.json`). A teacher
dragging a projector window or a tablet turning sideways will hit it. Better: carry the fault node into the redraw,
or finish the ping before redrawing.

### S8. Should fix (general): the teacher notes talk about the spec
Where: notes.md, Good to know. What: "Kitchen distance rounds to 256 design units, although the spec lists 255, with
two bars either way." A teacher has never seen a spec, and no distance is shown in the tool. Better: delete the
sentence; the line before it already says the thresholds are a Curio Class model.

### P1. Polish (general): two key clues don't prove their cause
Where: spec Content, calls 1 and 2 keys. What: call 1 accepts Q1 "A cable. The blue one." as proof of "Cable
unplugged", and call 2 accepts Q3 "Mom's phone works." as proof of "Wi-Fi turned off". Each only rules something out.
The step says "Tap 1 or 2 clues that prove it". Call 1's nudge after both keys are asked also quotes Q1 instead of the
screen clue. Better: call 1 keys [4, 1] (nudge quotes the screen), and accept a rule-out clue only alongside the
direct one, or drop it from the keys. Spec change.

### P2. Polish (general): the screen answer repeats the cause card's words
Where: Q4 answers, calls 1, 3, 7. What: "Network cable unplugged" matches "Cable unplugged", "Incorrect Wi-Fi password"
matches "Wrong Wi-Fi password", "You don't have permission" matches "Not allowed". Q4 is a key clue in 6 of 8 calls,
so "ask Q4, copy the words" is the fastest strategy for most of a shift. Real error screens do say these things, so
this is not wrong, but it turns three calls into word matching. Better: describe what the caller sees in their words
("A little computer with a red X and a cable picture", "It shows our Wi-Fi name and asks for the password again",
"A page with a lock on it: Teachers only"), so the student still has to name the cause.

### P3. Polish (general): House results don't name the kind
Where: House, result chip (`houseTry` computes `h.result.kind` but `renderHouse` shows only the text). What: "Wrong
password" and "Not allowed: Parent account only" appear with no Connection, Logging in or Permission stamp, so House
never links back to the three kinds. Better: show the same stamp (plug, key, hand) in the result chip.

### P4. Polish (general): House offers settings that make no sense for the printer and TV
Where: House panel with Printer or TV selected. What: both get Network and Account menus and every Try button. Setting
the printer to Guest makes every home device's Family printer try answer "Not allowed: guests can't reach home
devices" (all six, `house-result.json`, `printer-guest`), blaming a Home laptop for being a guest. The TV "Signed in"
to the Library site and the printer printing to itself read oddly. Better: for the printer and TV show only what they
have (power path, Network for the TV), hide Account, and word a printer-on-guest result as "Not allowed: the printer
is on the Guest Wi-Fi, away from home devices".

### P5. Polish (general): call 5's wrong-claim X lands on the Wi-Fi link, not the dark router
Where: Calls, call 5 wrong claim (`runPing`, calls 1, 2, 4, 5 share the mid-link fault). What: the X sits halfway
between Aunt Rosa's laptop and the router (frame `t-c5-wrong`); the broken spot is the router itself. Better: for
call 5 stop the ping at the router with the X there.

### P6. Polish (general): the need-clue reply shows two wordings at once
Where: Calls, claim step after right cause and weak clue. What: the nudge says "Right cause. Which clue proves it? Tap
a different clue." and the hint under it says "Right cause. Now tap a clue that proves it." (frame `t-c1-needclue`).
Better: one sentence in one place (and see S1, which changes the reply anyway).

### N1. Nit (general): "design units" and "20 units per press"
Where: notes.md (House), tablet aria-label. What: an engine term a grade 4 student or teacher won't know. Better:
"one small step per press".

### N2. Nit (general): Wi-Fi password call says "The path was fine"
Where: call 3 Solved kind line. What: Mr. Patel's laptop never joined the Wi-Fi, so the path to the internet was not
fine; the radio was in reach but the router refused it. Fine at grade 4, but "The Wi-Fi was in reach. The device had
to prove who it was with the right password." would fit both login calls.

## Grade, language, guardrails, sensitivity

- Language reads right for grade 4: short questions, plain cause names, "Logging in" and "Permission" on screen, the
  technical words (authentication, authorization) only in the teacher notes. Callers' words are on screen only.
- Grade 4, students or teacher: not K-2, no teacher-led requirement. Not hard history, not health. Call time is
  labeled "not a clock" and is display only; no score, stars or win state.
- Rule 7: privacy is stated in both panels ("Nothing sent or saved. Only Motion is remembered on this device.").
- Rule 8: the standards here cover no sensitive topic; nothing missing in the notes.
- Rule 5: nothing cultural, Native or hard-history. No sensitivity agent needed.

## Wave lessons (BUILD.md)

- No giveaways: missed (S1, and P2 as a lighter case).
- Honest numbers: bars say "about" on screen and Call time says what it counts. Pass.
- Standards: every code is done by the student, but SE-13's sort is thin (S2).
- Focus and layout, hint and voice, sizes, Motion off: see the Audit pilot rows and the Play and Craft lenses.

## Audit pilot

`python scripts/audit_tool.py network-help-desk <scratch>/audit --port 9400 --profile <scratch>/profile`, full walk,
3 leads. Report: `S:/CurioClass-codex-scratch/lens-teaching/audit/audit.md`.

Leads I confirmed:
- shift-report, "Laptop" text under another box at 1280x720, 1366x768, 1920x1080: confirmed on
  `state-shift-report-1366x768.png`: the router-to-internet line runs through Ana's "Laptop" label. Same cause as S4.
- shift-report, "Phone" under a rect: confirmed in part. In call 8 the Kitchen phone sits under Ana's laptop tile,
  so it is not visible at all. Harmless for teaching; part of the S4 placement problem.

Leads that were wrong (or not a flaw):
- House, "Tablet ... nothing changed": the tablet is already the selected device on a fresh House page, so a tap
  changes nothing by design. Not a dead control.

Clean rows I cite instead of re-shooting: all 8 sizes (Questions and Make a claim in view, Done when 7), Motion off,
focus on load, no console errors in the walk, the five-click and quick-tap voice rows for the mode buttons, Read and
Q1 to Q6 (Done when 6, as far as the audit reaches; the Craft lens owns the full count table).

What it missed (found by this lens):
- S7, the uncaught exception and locked call when the map resizes during a wrong-claim ping: the walk never resizes
  mid-ping, so its "no console errors" row does not cover it.
- S6, the Permission cause cut off after a nudge at 1366x768: the cause board is a scroll panel, so the audit treats
  a hidden card as fine. A scroll panel that hides one of three answer groups is a teaching problem.
- S1, S2, S3, S5, P1, P2 (giveaways, the kind sort, the map drawing unknown parts as working, "Allowed" on the guest
  laptop, weak proof clues): outside what it can see, as its header says.
- S4 at the wide sizes: it saw one label crossed in one state, not that the internet line crosses devices on every
  call screen.

Verdict: useful as a floor. Its clean size, Motion off and voice rows saved me re-shooting; its three leads were
small. The findings that matter here all came from driving the calls and reading the map.

## Builder claims checked afterwards (codex-report.md, read after the findings above)

- "PASS, no free sweep: all eight frozen right-cause/non-key claims rejected": the claims are refused, but the reply
  says "Right cause", which is the sweep (S1).
- "PASS, no giveaways ... Status appears only after relevant evidence": the map shows the cable plugged in (call 1),
  the Wi-Fi link working (call 3) and the router broadcasting (call 5) before the revealing question (S3).
- "Final drivers and stress report zero console errors": true for the runs it made; a resize during a wrong-claim
  ping throws (S7).
- "PASS, standards by solo action ... Authentication and authorization require different student actions": they
  need different cause cards, but the kind is printed on the board, so the student never makes the sort (S2).

# data-defenders: Teaching lens (round 1)

Cold read of spec.md, src.html, notes.md, art/prompts.json, voice/lines.json, kit/security.js (pure checks); bundle with
`CURIO_DRAFT=1` (181 KB). Driven with `scripts/drive.py` (ports 9530-9531, own profile in the lens scratch folder), 21
shots, console clean in all. Every number recomputed in Python. Standard wording read from the official PDF, "2026 CSTA
PK-12 Computer Science Standards" (statements and boundary statements, pp. 79-82), since the repo holds only the ids.

Counts: blocker 1, should fix 3, polish 2, nit 3.

## Standards (rule 2)

| Code | Statement (CSTA 2026) | Taught by | Verdict |
|---|---|---|---|
| E5-SYS-SE-13 | Describe the concepts of the CIA triad and how each component is important in protecting information. Boundary: confidentiality as keeping a password secret and not sharing PII; integrity as data accurate and unchanged ("grades in a gradebook haven't been improperly changed"); availability as accounts and systems there when needed ("the system isn't down or blocked"). | Three rooms, each fixed by a real action: C1 least privilege, C2 password; I1 seal (checksum), I2 log review; A1 enough servers, A2 backups kept apart. Secured lines name each promise; the exit sort makes the student apply all three to six new cases. | Taught well, above the minimum (the gradebook example is the boundary's own). See should fix 2 on the integrity wording. |
| E5-SYS-NT-14 | Distinguish between the components of wired and wireless networks. Boundary: devices (computers, tablets, phones), connecting hardware (routers, switches, cables), wireless connections (Wi-Fi signals). | Nothing. No router, switch, cable, Wi-Fi or device-connection appears anywhere; "server" in A1 is a capacity unit, not a network component. | Not taught. Blocker 1. |

## Done when

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

## Facts

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

## Findings

### Blocker

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

### Should fix

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

### Polish

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

### Nit

**N1. Spec text for A1 at 1 server says the striped bars start "4 p.m. on".** spec.md Content, A1. 4 p.m. has 450
visits, under 500; the tool correctly shows 5 p.m. to 8 p.m. (handoff says so). Fix the spec line. **general**

**N2. Log row 8, "entered Quiz 5 scores", sits after the tampering but the cards show only Q1 to Q4 with the old
seal.** `src.html:566`. A grade book that saves Quiz 5 would store a new seal over Cy's changed scores, and the cards
have no Q5. Better: row 8 "printed a class list" or similar, touching no scores. **general**

**N3. `Sec.safeDomain` passes brand look-alikes inside reserved names.** `kit/security.js:28`; a test call gave
`google.com.example` true. Not an issue here (only cedarhollow.example), but phishing-spotter and capture-the-flag
will draw look-alike addresses; a short brand blocklist check (or a rule that the label before `.example` holds no
real domain) would keep "no real brands" enforced by the engine, as the family doc promises. **family:security**

## Frames looked at

01-hall, 02-exit-locked, 03-c1-wrong2, 04-c1-partial, 05-c2-tested, 06-i1, 07-i2, 08-a1-1, 09-a2, 10-exit, 11-escaped,
12-timer, s-680x425, s-800x500, s-1000x625, s-1280x720, s-1366x768, s-1920x1080, s-760x1000, v-voice (in the lens
scratch folder, `lens-dd-teaching/frames`).

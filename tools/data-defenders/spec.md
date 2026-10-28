# Data Defenders

## One idea
Three locked rooms in a made-up school each guard one promise about data (only the right people can see it, it stays correct and changes can be checked, it is there when people need it), and a room's door opens only when your team fixes the real weak spot inside, so confidentiality, integrity and availability become three rooms you can name by what broke.

## Not like
- phishing-spotter (6-8, same family): fast rounds spotting tricks in messages. Here there is no inbox; you repair a school's stored data in slow, talk-it-over puzzles.
- capture-the-flag (9-12, same family): find a hidden flag, then patch. Here every puzzle is the repair itself, and the goal is to name the C, I or A each room protects.
- network-help-desk (grade 4): logging in and permission as reasons a device is stuck. Here access is something you set on purpose (who gets which folder).
- internet-journey (grade 3): personal info in a message. Here it is a school's records.
- game-remix, leaf-sorter-ai, design-for-a-friend (grade 5): code, AI and design; no security.

## Who and how
- Grade 5, computer science. Module: The CIA Triad (Systems and Security), "Confidentiality, integrity and availability".
- Topic line: "keeping data private, correct and available".
- Driver: students in teams of 2 or 3 on one laptop (escape room), or the teacher on a projector with table groups calling answers.
- 25 to 35 minutes: three rooms (about 8 min each), the exit door (3 min).
- Standards (CSTA 2026, as listed): E5-SYS-SE-13, E5-SYS-NT-14. 2017 crosswalk: 1B-NI-05 (discuss real-world cybersecurity problems and how personal information can be protected).
- tool.json: driver "students or teacher", minutes "25-35", modes ["Escape"], grades_label "Grade 5". Kit starter plus `kit:security`.

## Screens and modes
Header (kit): "Data Defenders", small line "Cedar Hollow Elementary". One mode (Escape), then Motion, Sound, Read.

Stage, two views:
1. **Hallway** (start): a school hallway at night (art behind) with four doors drawn in code: **Records Room** (blue, letter C hidden until secured), **Grade Book Room** (green, I), **Server Closet** (orange, A), and the **Exit** (brass, three empty shield slots). Each room door has a brass lock with one symbol slot per puzzle (two, two and three) that light as its puzzles are solved. When all three rooms are secured the Exit door glows (an outline flash with Motion off). Tap a door to enter. Rooms open in any order; the Exit unlocks only when all three rooms are secured.
2. **Room**: the room's puzzle stations side by side on a wide stage when the room has two (tabs otherwise, and always tabs for the Server Closet's three), a **Back to hallway** button (door icon), the room's lock with one slot per puzzle at the top.

Panel: `#hint`; the room's story card (2 sentences); the current puzzle's controls (below); **Clue** (lightbulb; first press clue 1, second press clue 2); **Team timer**: Off (default) / 20 min / 30 min, with the time left; **Start over** (confirm Yes/No).

## Content
School and people are made up. People: Ms. Ortiz (teacher, Room 12), Nurse Kim, Mr. Bell (bus driver), Jordan's dad (a parent), Mr. Lee (office). Students on score cards: Ari, Bea, Cy, Dot.

### Room C: Records Room (Confidentiality: only the right people can see it)
Story: "Right now, everyone at Cedar Hollow can open every folder. Lock it down so each person sees only what their job needs, then protect the records account."
- **C1 Who needs what** (symbol: key). Grid rows: Ms. Ortiz, Nurse Kim, Mr. Bell, Jordan's dad. Columns: Class grades, Health notes, Bus routes (every family's stop), Public (lunch menu and bus times). Public is ticked for everyone and locked (padlock-open icon, "public"). Each row has a job card: Ortiz "I enter grades for my class." Kim "I keep the health notes." Bell "I drive Bus 4." Jordan's dad "I check what's for lunch and when the bus comes." All other cells start ticked. **Check lock**. Answer: Ortiz Grades; Kim Health notes; Bell Bus routes; Jordan's dad nothing beyond Public (a parent gets only public information). Wrong: "N boxes give too much access" or "N people can't do their job" (counts only); after the second wrong check, rows with an error get a "!" badge. Clue 1: "Read each job card. Give a folder only if the job needs it." Clue 2: "Some people need only the public folder."
- **C2 Pick the password** (symbol: closed eye). Four cards for the records account and **Use this one** on each. The meter (bar, Weak / OK / Strong, and the reason) rates a pick after it is made; after the first pick, tapping a card tests it too. Cards and meter results: "cedar" Weak (too short; uses the school's name); "Cedar2026" Weak (uses the school's name, easy to guess); "password1" Weak (on the common passwords list); "purple tiger skates home" Strong (24 characters). Answer: the fourth. Wrong: the meter reason is spoken as the result. Clue 1: "Longer is stronger." Clue 2: "Stay away from names and common passwords."
- Secured line: "Room C is secured. Confidentiality means only the right people can see the data."

### Room I: Grade Book Room (Integrity: it stays correct, and changes can be checked)
Story: "Someone changed a grade overnight. Find the changed card, then find out how it happened."
- **I1 Seal check** (symbol: wax seal). When Ms. Ortiz saves scores, the grade book adds them up and stores the total as a seal. Cards (four quiz scores, then the seal): Ari 18, 15, 20, 17, seal 70; Bea 16, 19, 14, 18, seal 67; Cy 20, 20, 19, 20, seal 59; Dot 13, 17, 16, 19, seal 65. Sums (computed): 70, 67, 79, 65. Tap numbers on a card to add them with the **Add up** helper (a running total under the card). **This one was changed** on each card. Answer: Cy (79 is not 59). Wrong: "Add that card up. Does it match its seal?" Clue 1: "Add each card's four scores." Clue 2: "One card adds up to 79."
- **I2 Who changed it?** (symbol: magnifier). Change log, 8 rows (day and time, account, device, action): 1 Mon 8:05 a.m., ms.ortiz, Room 12 laptop, opened Grade Book. 2 Mon 8:10 a.m., ms.ortiz, Room 12 laptop, entered quiz scores. 3 Mon 8:12 a.m., ms.ortiz, Room 12 laptop, changed quiz scores (a typo fix). 4 Mon 3:30 p.m., ms.ortiz, Room 12 laptop, closed Grade Book. 5 Tue 2:14 a.m., ms.ortiz, unknown laptop, changed quiz scores. 6 Tue 7:55 a.m., mr.lee, Office desktop, printed the lunch list. 7 Tue 8:02 a.m., ms.ortiz, Room 12 laptop, opened Grade Book. 8 Tue 9:40 a.m., nurse.kim, Nurse desktop, updated a health note. Rows 3 and 5 make the same change, so the time and the device tell them apart. Step 1: tap the row that doesn't fit (answer row 5). Step 2: choose the first fix: "Put the real scores back from Monday's backup, and change Ms. Ortiz's password" (right) / "Delete the log so nobody sees it" / "Let everyone edit the grade book"; a wrong fix's reason is shown and spoken. Clue 1: "Look at the times and the devices." Clue 2: "Which change came at night, from a laptop the school does not know?"
- Secured line: "Room I is secured. Integrity means data stays correct, and changes can be checked."

### Room A: Server Closet (Availability: it is there when people need it)
Story: "On report card night the school website went down, the server's disk broke, and then the Wi-Fi stopped working. Keep the site up, the work safe and the network running."
- **A1 Report card night** (symbol: lightning). Bar chart of website visits per hour: 3 p.m. 200, 4 p.m. 450, 5 p.m. 900, 6 p.m. 1,400, 7 p.m. 1,100, 8 p.m. 600, 9 p.m. 300. One server handles 500 visits an hour (a made-up number for this school); a capacity line shows servers x 500. **Servers** stepper 1 to 4, **Set servers**. Prompt: "the fewest servers that keep the site up all evening". Answer 3 (1,500 covers 1,400). With 1: bars over 500 turn striped "too many" (5 p.m. to 8 p.m.; 4 p.m. is 450); with 2: 6 p.m. and 7 p.m. striped; with 4: "That works, but one server would sit idle. Try fewer." Clue 1: "Find the busiest hour." Clue 2: "Each server handles 500. How many cover 1,400?"
- **A2 Backup plan** (symbol: stacked copies). The disk broke Thursday afternoon. Four plan cards, text only until picked: A "Back up every Friday onto the same server"; B "Back up every Friday to a server in another building"; C "Back up every night to a server in another building"; D "No backups". A picked plan shows its last Friday to Thursday strip (struck days with an X) and its reason, spoken when wrong: A "The copy was on the same server, so it broke too. All the work is lost." B "The copy is safe in another building, but it is from last Friday. Monday to Thursday are lost." C "The copy is in another building, and it was made last night. Only Thursday is lost." D "With no copy at all, all the work is lost." Prompt: "Which plan loses the least work?" Answer C. Clue 1: "A backup on the same machine breaks with it." Clue 2: "More often means less lost."
- **A3 Network closet** (symbol: Wi-Fi; E5-SYS-NT-14). Step 1: eight part cards, each with a type tag (device, connecting hardware, signal) and a Wired / Wireless toggle: Network cable (wired), Wi-Fi access point (wireless; it plugs into the switch and sends out Wi-Fi), Office desktop (wired, a cable to the switch), Wi-Fi signal (wireless), Switch (wired), Room 12 laptop (wireless), Printer (wired), Library tablet (wireless; no network cable port). Each card's note and the definition ("Wired uses cables. Wireless uses Wi-Fi signals through the air.") show at every size. Check sort with parts left says so aloud. **Check sort** reports "N parts are in the wrong group" (or how many are left); after two misses the wrong cards get a "!". Step 2: the school network drawn by the network engine (router, switch, access point wired to the switch; office desktop, nurse desktop and printer wired to the switch; Room 12 laptop and library tablet on Wi-Fi), with the access point down. Tap each device that stays online, then **Check**. The answer comes from `Net.reach` from the router: the office desktop, nurse desktop and printer. Wrong: "N devices you marked lose their link" and "N devices that stay online are not marked"; after two misses the wrong devices get a "!". Solved: each device shows online or offline. The access point is drawn as a Wi-Fi symbol with no line to the laptop and tablet (only radio arcs). Clue 1: "A cable is wired. A signal through the air is wireless." Clue 2: "When the access point breaks, only the devices on Wi-Fi lose their link."
- Secured line: "Room A is secured. Availability means data and systems are there when people need them."

### Exit door (the CIA lock)
Six cards to sort into C, I and A slots (tap a card, then a slot; or drag): "Someone read the health notes over the nurse's shoulder." C. "A virus changed the numbers in the lunch money file." I. "A storm knocked out power, and the website went dark." A. "A stolen password was used to copy the grade book." C. "A typo changed a bus time, and nobody checked it." I. "So many people visited at once that the site stopped loading." A. **Open the exit** checks all six; wrong cards slide back with a small shake, right ones stay. Escape card: "Cedar Hollow's data is safe," the three letter shields, time used (if the timer was on), **Play again**.

## Interactions in detail
- Every puzzle can be retried without penalty; Clue never costs anything. A solved puzzle stays solved (its station shows "Done" and the answer).
- Lock slots light with a soft chime (`Curio.yes`). A secured room's door shows its letter on a shield in the hallway.
- Team timer: counts down from the chosen time; at 0 it shows "Time!" and the hint "Keep going to finish." Nothing locks. Off by default.
- Start over clears all rooms (confirm). Progress is kept for the page load only; nothing is stored except the kit Motion setting.
- Motion off: no door swing or card slides; slots and shields appear with an outline flash, same timing.
- Sizes: the hallway scales its door spacing per box at real size; doors stay at least 120 px wide (tap targets); at 375 wide doors are a 2 x 2 grid. In rooms, the active puzzle and its check button are visible without scrolling at every size in STANDARDS.md (the other station collapses to a tab).
- Keyboard: Tab goes header, panel controls, then doors or puzzle items; grid cells toggle with Space; sorting by Enter on a card then Enter on a slot.
- `window.__tool = {state, sec, enter(room), solve(puzzle, answer), cards()}`.

## Look
Accent `--brand #875a00` (vault brass). Band 3-5, own `:root`. A school after dark, warm brass locks, three room colors.
- `--paper #f7f2e7`, `--panel #ffffff`, `--ink #2a2116`, `--muted #64584a`, `--line #e6dccb`, `--btn #875a00`, `--head-ink #ffffff`, `--focus #1d4ed8`.
- Hallway: night `#1e2a3a` with labels `#e6eef7`, lock and slot glow `#ffd27a`. Doors: C `#2f5ea8`, I `#2e7d4f`, A `#b0461f`, each with white letter and its own icon (eye, seal, lightning), never color alone.
- Contrast (computed): white on brand 6.01:1; brand on paper 5.39:1; ink on paper 14.17:1; muted on paper 6.19:1; focus on paper 6.00:1; white on C blue 6.39:1, on I green 5.05:1, on A orange 5.61:1; ink on gold 11.11:1; hallway labels 12.39:1; gold on night 10.19:1. All pass AA.
- Neighbors: game-remix teal, code-tracer orange on cream, network-help-desk green; brass is new. No confetti; the escape card is the one flourish.

## Art
- dd-night-hallway: an empty elementary school hallway at night, blank lockers along the left wall, a long polished floor, soft blue moonlight from high windows, painted storybook style, plain walls with no signs; 16:9; cutout no; people no; hallway background, darkened 40 percent behind the code-drawn doors. FLUX.2 (`scripts/cfart.py`).
Doors, locks, puzzle cards, grids, charts, logs and preview.svg are drawn in code.

## Voice
Bank voice `hero-coach` (Puck), "Say with bright, encouraging energy, like a friendly superhero coach", for a team of data defenders. Not used by any grade 4 to 5 CS neighbor (code-tracer clear-teacher, game-remix big-sister, network-help-desk upbeat-guide) or group sibling; its other user is loop-garden (grade 2). `Curio.voice`, `scope: () => state.room`.
- welcome (how): "Welcome, Data Defenders. Three rooms guard Cedar Hollow's data. Tap a door to go in. Solve every puzzle in a room to secure it." (it never overwrites the hint)
- Room story cards (how, once each when the room opens, then the room's first how-to): the three Story texts in Content. The hint shows the how-to at once; the story stays in the story card.
- c1 (how): "Tap a box to take a folder away. Then press Check lock." c2 (how): "Press Use this one on the strongest password. The meter checks your pick." i1 (how): "Add up each card and compare it with its seal. Tap This one was changed on the card that doesn't match." i2 (how): "Tap the row in the log that doesn't fit." i2b (how): "Now pick the first fix." a1 (how): "Change the number of servers, then press Set servers." a2 (how): "Pick the plan that loses the least work." a3 (how): "Sort each part: wired or wireless. Then press Check sort." a3b (how): "The Wi-Fi access point broke. Tap each device that stays online. Then press Check." exit (how): "Tap a card, then tap C, I or A. Then press Open the exit."
- wrong (event, any wrong check; cuts in over a waiting line; stale on the next tap): "Not yet. Look again, or press Clue." Plus the puzzle's own wrong text when it has one (C2 meter reasons, I1, the I2 fix reasons, A1 "That works, but one server would sit idle. Try fewer.", the A2 plan reasons).
- hExitLocked (event, each tap on the locked Exit, kept in the hint): "The exit opens when all three rooms are secured. Tap a room door first."
- symbol (event): "Lock symbol found!"
- Secured lines C, I, A (event): in Content.
- back (how, after the first secured room): "Tap Back to hallway and pick another door."
- exit-open (how, when all three rooms are secured): "All three rooms are secured. Tap the Exit door to open it."
- escaped (event): "You escaped! Confidentiality, integrity and availability: Cedar Hollow's data is safe."
- time (event, timer at 0): "Time! Keep going to finish."

## Family engine
`kit/security.js` (the security family: data-defenders, phishing-spotter, capture-the-flag). This spec holds the full description; the siblings say what they feed it.
- **World**: each tool passes a made-up organization `{name, people:[{id, name, role}], accounts, files, domains}`. Every web address and email domain must be a reserved name (`example.com`, `example.org`, `example.net`, or ending `.example`, `.test`, `.invalid`); `sec.safeDomain(url)` checks it and the engine logs a console error for any other, so no real site or brand can slip into a lesson.
- **Artifacts** (DOM renderers into a card, each part addressable): `email` (from name, from address, reply-to, to, subject, time, body paragraphs, links `{text, href}`, attachments `{name}`), `sms` (sender, bubbles, links), `login` (a fake browser frame: address bar with lock icon, page title, a code-drawn logo shape with the org's name, fields that never take real typing: they show dots or a scripted fill), `log` (table: time, account, device, action, plus extra columns), `file` (title, fields, seal), `call` (transcript lines by speaker), `note` (a sticky note or text file in monospace).
- **Spots**: any artifact part can be a spot `{id, tell}`. Tapping or Enter marks it and fires `onSpot(id)`; the tool decides if it is right. Links: hover, focus or long-press shows the real `href` in a status bar at the bottom of the card, like a real browser.
- **Checks** (pure): `sec.strength(pw)` returns `{length, pools, bits, wordBits, onList, hasName}`: pools are lowercase 26, uppercase 26, digits 10, symbols and space 33; `bits = length x log2(pool total)`; when the password is two or more lowercase words split by single spaces, `wordBits = words x log2(7776)`; `onList` checks the common list below (exact, case-insensitive); `hasName` checks words the tool passes (here "cedar", "hollow"). `sec.band(r, names)` (grade 3 to 5; r is a strength result or a password string checked against names): Weak if onList, hasName or length under 8; OK for 8 to 14; Strong for 15 or more. `sec.seal(numbers)` = their sum (a toy checksum). `sec.caesar(text, k)`, `sec.vigenere(text, key, dir)` (letters only, case kept, other characters unchanged), `sec.b64(text, dir)` (UTF-8 safe).
- Common passwords list (20, all in the UK NCSC list of the 100,000 most-used breached passwords): 123456, 123456789, qwerty, password, 1111111, 12345678, abc123, password1, iloveyou, sunshine, princess, football, monkey, letmein, dragon, baseball, welcome, 123123, qwerty123, 000000.
- **Locks** (pure): `sec.lock({check, normalize})`: `normalize` trims and lowercases by default; `check` returns `{open, misses}`; after 2 misses the tool may show a stronger clue.
- **Clock**: `sec.clock({mode:'down'|'up', ms, onEnd})` with pause and reset; used for escape timers and arcade rounds.
- Pure parts in one marked block with no DOM, exposed as `__tool.sec`.
This tool uses: World (Cedar Hollow, with `cedarhollow.example` only in the log's device names, no links), Artifacts `file` and `log`, Spots (log rows, score cards), Checks (`band`, `strength`, `seal`), Locks (each puzzle), Clock (Team timer). The Network closet also uses the network engine (`kit/network.js`, docs/families/network.md, unchanged): `Net.graph`, `Net.reach`, `Net.draw` and `Net.icon`.

## Sources
- CSTA 2026 ids E5-SYS-SE-13, E5-SYS-NT-14 (`data/standards/csta-2026-ids.txt`); CSTA 2017 1B-NI-05: https://csteachers.org/k12standards/
- Confidentiality, integrity and availability defined: NIST CSRC Glossary, "confidentiality", "integrity", "availability" (from 44 U.S.C. 3552), https://csrc.nist.gov/glossary
- Least privilege (give only the access a job needs): NIST CSRC Glossary, "least privilege", https://csrc.nist.gov/glossary/term/least_privilege
- Length matters most; block common, expected or context-specific passwords (like the organization's name); a password used alone should be at least 15 characters: NIST SP 800-63B-4, section 3.1.1.2, https://pages.nist.gov/800-63-4/sp800-63b.html
- Common passwords: UK National Cyber Security Centre, "Most hacked passwords revealed" (2019) and its 100,000 list, https://www.ncsc.gov.uk/news/most-hacked-passwords-revealed
- Checksums detect changes to data: NIST CSRC Glossary, "checksum", https://csrc.nist.gov/glossary/term/checksum
- Logs record who did what and when; review them for unusual activity: CISA, "Logging Made Easy" and Cybersecurity Best Practices, https://www.cisa.gov/topics/cybersecurity-best-practices
- Keep backups often, and keep a copy separate from the original system: CISA (US-CERT), "Data Backup Options" (2012), cisa.gov publications; the 3-2-1 practice (one copy kept off-site) is described there
- Too much traffic can make a website unavailable; more servers share the load: CISA, "Understanding Denial-of-Service Attacks", https://www.cisa.gov/news-events/news/understanding-denial-service-attacks
- Reserved example domains: RFC 2606 and RFC 6761, https://www.rfc-editor.org/rfc/rfc2606
- Wired networks connect devices with cables through switches; wireless networks use Wi-Fi radio signals from access points: CSTA 2026 E5-SYS-NT-14 boundary (devices, connecting hardware, wireless connections), and CISA, "Securing Wireless Networks", https://www.cisa.gov/news-events/news/securing-wireless-networks
- School, people, scores, visits, the network and the 500 visits per server are made up for Curio Class; sums computed.

## Done when
1. All three rooms can be entered in any order; the Exit stays locked until all three are secured.
2. C1 opens only with the Content grid; wrong checks report counts and, after two, row badges. C2 meter results match Content (`__tool.sec.band`), and only the fourth card opens it.
3. I1: card sums are 70, 67, 79, 65; only Cy opens it. I2 needs row 5 then the backup-and-password fix.
4. A1 opens only at 3 servers; 1, 2 and 4 give the Content results. A2 opens only with plan C. A3 step 1 opens only with all eight parts sorted right; step 2 only with exactly the devices `Net.reach` finds online.
5. Exit opens only with all six cards right; wrong cards slide back.
6. Team timer Off, 20 and 30 work; at 0 nothing locks.
7. Voice: welcome once; each how line spoken once then hint only; secured and symbol lines every time; Read speaks the hint.
8. Every size in STANDARDS.md with the active puzzle's check button visible without scrolling; 375 wide works in `drive.py --host`.
9. `sec.safeDomain` rejects any non-reserved domain in a test call; console clean; no network requests; nothing stored; the name only as "Curio Class".

## Refine changes (round 1)
Split rooms switch puzzles in place, so a tap on the second puzzle lands the first time. New Network closet puzzle (A3) in the Server Closet for E5-SYS-NT-14: sort eight parts into wired and wireless, then predict which devices stay online when the Wi-Fi access point fails (the network engine's map and reach; the room has three lock slots and tabs). A2 shows each plan's strip and reason only after it is picked. I2's log row 5 (was row 4) says "changed quiz scores", and a daytime row 3 makes the same change from her own laptop, so time and device find it; the Quiz 5 row is gone and the fix no longer names Cy. Integrity's promise is "it stays correct, and changes can be checked". C1: Jordan's dad gets only the public folder (lunch menu and bus times). C2's meter rates a pick after it is made. The hint names the room's first action on entry; Read speaks it. The locked Exit speaks and keeps its line; when all rooms are secured the Exit glows and the line says to tap it. Wrong answers cut in and speak their reasons (I2 fixes, A2 plans). Larger targets and focus rings (score chips, log rows, compact Back, compact tabs), the I1 "Sum" label on small screens and Cy's 79 when done, A2 day chips at 13 to 14 px, the lock slot pop with Motion on, the escape card as a modal, the 1-server stripe typo (5 p.m. on). Round 2 (exit check): A3 notes and definition at every size, Check sort in view at 375, the tool's own online / offline pills (the network engine's x badge overlaps its text), the access point drawn as Wi-Fi with no line to the devices, a spoken line for an unfinished sort, the finished map first.

## Open questions
- The escape room format calls for timed team play; this spec makes the Team timer optional and Off by default, so no team is rushed on the CIA ideas. Keep it off by default, or start at 20 minutes?

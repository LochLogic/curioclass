# Capture the Flag

## One idea
A twelve-tile board of small security challenges inside a made-up freight company, where every flag you find by careful reading (decoding a note, auditing passwords, reading logs, catching a pretext call) unlocks a second step that asks you to patch the hole it came from, and a tile only turns fully green when the hole is fixed, not just found.

## Not like
- data-defenders (grade 5, same family): an escape room where each puzzle is a repair with lots of clues. Here you find a flag string first, then choose the patch, with real-thing tools (decoders, a password meter, logs).
- phishing-spotter (6-8, same family): fast rounds of keep-or-report. Here one deep case at a time, with no clock, and phishing is only one of four categories.
- network-architect (9-12, same wave group): designs a network and tests it. Here the systems already exist and you audit them.
- data-policy-council (9-12): writes privacy policy. Here the work is hands-on finding and fixing.
- api-playground, ai-evaluator (9-12): software and AI; no security.

## Who and how
- Grades 9 to 12, computer science. Module: Cybersecurity (Systems and Security), "Security measures, breaches, social engineering and fixes".
- Topic line: "passwords, encryption, social engineering and logs".
- Driver: students, one laptop each or pairs (pairs work well: one reads the artifact aloud). 30 to 50 minutes (about 3 minutes per tile; the board can span two periods since progress saves).
- Standards (CSTA 2026, as listed): HS-SYS-SE-31, HS-SYS-SE-32, HS-SYS-SE-33. 2017 crosswalk: 3A-NI-05 (how sensitive data can be affected by attacks), 3A-NI-06 (recommend security measures), 3A-NI-07 (tradeoffs between usability and security), 3A-NI-08 (tradeoffs of cybersecurity recommendations), 3B-NI-04 (ways to protect devices and information from unauthorized access).
- tool.json: driver "students", minutes "30-50", modes ["Board", "Toolbox"], grades_label "Grades 9-12". Kit starter with `kit:theme-912` and `kit:security`.

## Screens and modes
Header (kit, 9-12 theme): "Capture the Flag", small line "Larkspur Freight, a made-up company". Mode buttons: **Board** (opens first), **Toolbox**. Then Motion, Sound, Read.

Board view (stage): a 4 by 3 grid. Columns **Passwords**, **Codes**, **People**, **Logs**; rows 100, 200, 300. Tile states, each with an icon and a word: Open (outline), Flag found (amber border, flag icon, "patch it"), Patched (green, shield icon, "patched"). Above the grid: Score, "Flags 5 of 12", "Patched 4 of 12". Panel: `#hint`, a short how-it-works list ("Find the flag. It looks like flag{...}. Then patch the hole."), **Clear progress** (confirm Yes/No).

Challenge view (stage, replaces the grid): the brief (2 sentences), the artifact(s) drawn by the security engine, and a **Back to board** button. Panel: **Flag** input (monospace, placeholder `flag{...}`) and **Submit**; **Hint** (shows the hint and halves this tile's flag points; says so on the button: "Hint (half points)"); the **Toolbox** drawer (the same four tools as Toolbox mode, opened on the one this challenge needs); after the flag, the **Patch** card: the question and three choices, each with its reason after you pick.

Toolbox view: four tabs. **Shift** (Caesar: a two-ring wheel and a shift stepper 0 to 25, text in, text out), **Keyword** (Vigenere: key field, Encode/Decode), **Base64** (Encode/Decode), **Strength** (password box, readouts: length, pools, bits by letters, bits by words when it is words, the lower one used, "time to try every possibility at 10 billion guesses a second", and "On the common list: yes/no"). A note under Strength: "Don't type a password you really use. Nothing here is saved or sent."

## Content
Larkspur Freight (larkspur.example) and everyone in it are made up. Scores: flag 100, 200 or 300 (half with a hint), patch +50 on the first right choice. Maximum 3,000.
Flags are accepted with or without the `flag{ }` wrapper, any letter case, spaces trimmed. Wrong: "Not this one." After 3 misses the Hint button pulses.

**Passwords**
- **P100 On the list.** Brief: "An old sign-up form saved passwords in plain text. Which account uses a password from the common list?" Artifact `file` "signup-export.csv": amaya.r Tidepool-Lantern-88; bkoh password1; cdiaz Orchard9Comet!; dfinch violet harbor bicycle; evance Winter2026!; fgrant m0nkeyB@rs. Tool: Strength. Flag `flag{bkoh}`. Hint: "Run each one through the Strength tool and look at On the common list." Patch "What stops this at sign-up?": A "Block any password found on a common or breached list" (right: "NIST's guidance: check new passwords against such lists."); B "Require one symbol" ("password1! would pass."); C "Force a new password every 30 days" ("NIST advises against forced changes; people pick patterns like Winter2026! then Spring2026!"). After the patch: "Also: never store passwords in plain text. Systems store salted hashes."
- **P200 Length wins.** Brief: "Four choices for the new admin password. The guesser knows people use words. Find one the meter rates at 70 bits or more." Artifact `note`: Gr4v1ty#7 / bluemoon / kettle orbit maple / kettle orbit maple fog lantern drum. Strength results (computed): Gr4v1ty#7 59.1 bits (9 characters, pool 95), about 2 years; bluemoon 37.6 bits, about 21 seconds; kettle orbit maple 105.9 by letters but 38.8 by words, so 38.8, about 47 seconds; the six words 205.9 by letters, 77.5 by words, so 77.5, about 700,000 years. When the shown bits are 70 or more the meter prints `flag{six_random_words}`. Hint: "Look at the bits by words line." Patch "What should the password rules allow?": A "Long passphrases: at least 64 characters, spaces allowed" (right: "Length is what makes guessing slow; words must be picked at random."); B "Cap passwords at 12 characters" ("That forbids the strongest choice."); C "Ban spaces" ("Spaces help people type long passphrases.").
- **P300 Second step.** Brief: "Someone had cdiaz's password at 3 a.m. Why didn't they get in? Open the row that explains it." Artifact `log` "Sign-in record: cdiaz" (time, device, place, password, second step, result): Mon 08:02, Laptop L-114 (known), Office, correct, not asked (known device), signed in. Mon 12:40, Phone P-22 (known), Office, correct, not asked, signed in. Tue 03:02, new device, new place, correct, code sent to cdiaz's phone: denied, blocked. Tue 03:04, new device, new place, correct, code sent: no answer, blocked. Tue 08:05, Laptop L-114, Office, correct, not asked, signed in. Tue 08:06, Laptop L-114, Office, password changed by cdiaz, none, done. Rows expand on tap; the 03:02 row's details read "Second step denied by the account owner. flag{second_step_held}". Hint: "The password was right. What else does the log check?" Patch "What fix should every account get?": A "Turn on a second step (multi-factor sign-in)" (right); B "Hide the sign-in page's address" ("Hiding a page doesn't stop someone who has the password."); C "Email everyone their password each month" ("Email is not a safe place for passwords.").

**Codes**
- **C100 Not a lock.** Brief: "A note for the night guard looks scrambled. Is it locked?" Artifact `note`: "Message for the night guard: ZmxhZ3tub3RfYV9sb2NrfQ==". Tool: Base64 decodes it to `flag{not_a_lock}`. Hint: "Text ending in == is often Base64." Patch: A "Base64 is encoding, not encryption: keep secrets out of notes, or encrypt them with a real key" (right); B "Base64 it twice" ("Anyone can decode it twice."); C "Make the note longer" ("Length doesn't hide it.").
- **C200 Only 26 keys.** Brief: "A sticky note on a monitor: every letter is shifted the same amount." Artifact `note`: "mshn{vusf_26_rlfz}". Tool: Shift; shifting back 7 gives `flag{only_26_keys}`. Hint: "Try shifts until the first word reads flag." Patch: A "Use modern encryption such as AES; a shift cipher has only 26 keys to try" (right); B "Use shift 13 instead" ("Still only 26 keys."); C "Write it in capitals" ("Capitals change nothing.").
- **C300 Key on the doormat.** Brief: "A shared folder holds a locked plan. Can you open it?" Artifact `file` folder "Shared/Projects": plan.txt "qlnz{ovra_krrw_rclrg}"; readme.txt "The plan is locked with the keyword LANTERN. Do not lose it!" Tool: Keyword, Decode with LANTERN gives `flag{keep_keys_apart}`. Hint: "Read every file in the folder." Patch: A "Keep keys apart from the data they lock, in a key manager" (right); B "Use a longer keyword in the same readme" ("Anyone who opens the folder still has it."); C "Rename readme.txt" ("A new name doesn't hide it.").

**People**
- **S100 The urgent caller.** Brief: "Dana at the front desk got this call. Tap the two lines that should have stopped her." Artifact `call`: 1 Caller "Hi Dana, this is Sam from IT." 2 Caller "We have an urgent security upgrade, and your account will be locked in ten minutes." 3 Dana "Oh no. What do I need to do?" 4 Caller "I'm sending a code to your phone right now." 5 Caller "Read me the six-digit code and I'll finish the upgrade for you." 6 Dana "Okay, it says..." 7 Caller "Quick, the timer is running." 8 Dana "Wait. I'll call the help desk back first." Marking lines 2 and 5 (line 7 also counts as the rush line in place of 2) shows `flag{call_back}`. Hint: "One line makes you hurry. One asks for something you never share." Patch: A "Hang up and call the help desk at the number in the company directory" (right); B "Ask the caller for an employee ID" ("Anyone can make one up."); C "Give the code if the caller knows your name" ("Names are easy to find.").
- **S200 One badge, two people.** Brief: "The door counter and the badge reader disagree once this morning. When?" Artifact `log` (time, door, badge, people through): 07:41 Front b-1021 1; 07:44 Front b-1033 1; 07:46 Dock b-2007 1; 07:49 Front b-1040 1; 07:52 Dock b-2011 2; 07:55 Front b-1002 1; 07:58 Front b-1019 1; 08:01 Dock b-2007 1; 08:03 Front b-1044 1; 08:06 Front b-1050 1. Flag `flag{0752}` (07:52 also accepted). Hint: "One badge should let in one person." Patch: A "One badge, one person: ask anyone following to badge in or go to the front desk" (right); B "Prop the dock door open at rush hour" ("That invites tailgating."); C "Put up a sign and do nothing else" ("Signs alone don't stop it.").
- **S300 New bank details.** Brief: "A supplier says it changed banks. Compare with last month." Artifact two `email`s: last month, Birchline Paper, billing@birchline.example, "Invoice 4471 attached. Same bank as always." This month, Birchline Paper, billing@birchline-billing.example, "We changed banks. Please send this month's payment to the new account below. Our finance team needs it today." Flag `flag{birchline-billing.example}`. Hint: "Compare the two sender addresses letter by letter." Patch: A "Confirm any payment change by calling the supplier at the number already on file" (right); B "Reply to the email to confirm" ("The reply goes to the fake sender."); C "Pay half to the new account" ("Half is still lost.").

**Logs**
- **L100 Too many tries.** Brief: "Which account was guessed into overnight?" Artifact `log` (time, account, device, result): 01:58 amaya.r L-102 success; 02:10 gnair new device failed; 02:10 gnair new device failed; 02:11 gnair new device failed; 02:11 gnair new device failed; 02:12 gnair new device failed; 02:13 gnair new device success; 02:20 hwu L-131 success; 07:55 bkoh L-108 success; 08:01 cdiaz L-114 success; 08:03 evance D-009 failed; 08:03 evance D-009 success. Flag `flag{gnair}`. Hint: "One typo is normal. Five in a row from a new device is not." Patch: A "Slow down or lock sign-ins after repeated failures, and add a second step" (right); B "Tell users which letter was wrong" ("That helps the guesser."); C "Allow unlimited tries" ("That is what let it happen.").
- **L200 Midnight download.** Brief: "Which account read far more files than usual?" Artifact `log` (time, account, share, files read): Mon 09:12 hwu Shipping 6; Mon 11:40 bkoh Finance 3; Mon 14:05 hwu Shipping 9; Mon 16:30 amaya.r HR 2; Tue 01:47 hwu Shipping 312; Tue 01:49 hwu Finance 140; Tue 08:15 cdiaz Shipping 4; Tue 09:02 hwu Shipping 7; Tue 10:20 bkoh Finance 5; Tue 13:44 evance HR 1. Flag `flag{hwu}`. Hint: "Sort by files read." Patch: A "Give each account only the shares its job needs, and alert on unusual volume" (right: "hwu works in Shipping; Finance access shouldn't exist."); B "Delete old logs to save space" ("Logs are how this was found."); C "Give everyone every share" ("More access, more damage.").
- **L300 Put it in order.** Brief: "Five events from one break-in, shuffled. Put them in order; the letters spell the flag." Cards: R "Password typed into a fake sign-in page" (no time); T "09:14 Phishing email opened by jlam"; A "09:31 Sign-in as jlam from a new device; a new phone added for sign-in codes (jlam had none set up)"; C "09:40 Mail rule created: forward all invoices outside"; E "10:02 312 files downloaded from Shipping". Order T, R, A, C, E gives `flag{TRACE}`. Hint: "The password had to be stolen before it was used." Patch "Which single fix stops the chain earliest?": A "Phishing-resistant sign-in, like a security key that only works on the real site" (right: "It breaks the chain at R."); B "Delete mail forwarding rules each week" ("That only stops step C."); C "A bigger mailbox" ("Unrelated.").

## Interactions in detail
- Tiles open in any order. A flag-found tile reopens straight to its Patch card; a patched tile opens read-only with the answers shown.
- Patch: choosing a wrong option shows its reason and lets you choose again; +50 only for a right first choice; the tile turns green whenever the right one is chosen.
- Hint use is shown on the tile (a small "hint" tag) and halves that flag's points.
- Log artifacts get a small toolbar: sort by any column, filter by account. Row taps expand details where Content gives them.
- Text tools work on any text; Strength runs on each keystroke; nothing typed is stored.
- Progress saves on this device: localStorage `curio-capture-the-flag` holds only tile states, hint use and patch results (no typed text). Clear progress asks Yes/No.
- When all 12 tiles are patched: one line under the score, "Every hole is patched." No celebration beyond that.
- Motion off: no tile flip; states change in place.
- Sizes: board tiles at least 96 x 64 px; in the challenge view the artifact scrolls inside its own card while Flag and Submit stay visible without page scrolling at every size in STANDARDS.md; at 760 wide the panel goes below with Flag first; at 375 wide the board is 2 columns by category with row labels. Artifact text is monospace 14 px or more (13 px in the 680x425 preview).
- Keyboard: Tab goes modes, header, tiles (arrow keys move within the grid), then in a challenge: artifact spots, Flag, Submit, Hint, Toolbox, Patch.
- `window.__tool = {state, sec, setMode, open(tile), submit(tile, text), patch(tile, choice)}`.

## Look
Accent `--brand #ff7ac8` (signal pink) on the 9-12 theme, `--brand-ink #2a0a1c`.
- Artifacts: terminal cards `#0a0f14` with text `#d6e2ee` and muted `#a6b3c4`; email and sign-in artifacts use a light card (`#fbfbf8`, ink `#1c1f26`) so they read like the real thing. Tile states: flag found `#f2a93b` border plus flag icon; patched theme `--ok #6fdca6` fill with ink text plus shield icon.
- Contrast (computed): brand on panel `#141b25` 7.31:1, on `--sec-bg` 6.93:1; brand-ink on brand 7.66:1; terminal text 14.64:1; terminal muted 9.04:1; amber on `--sec-bg` 8.21:1; ok green on `--sec-bg` 9.73:1; theme ink on `--sec-bg` 13.93:1. All pass AA; states always add an icon and a word.
- Neighbors: network-architect blueprint blue on the same theme; theme default amber; phishing-spotter lime. Pink is unused in this group.

## Art
none: drawn in code. Board, artifacts (sticky note, folder, call transcript, logs, emails), Caesar wheel and preview.svg are SVG and CSS.

## Voice
Bank voice `hs-narrator` (Kore), "Read clearly and naturally, at a moderate pace". 9-12 narration stays short: artifacts, briefs and patch reasons are read on screen. Changed at the wave check from wise-mentor, which ai-evaluator (9-12 CS) also uses; no other 9-12 CS tool uses hs-narrator. `Curio.voice`, `scope: () => state.mode`.
- w-board (how): "Pick any tile. Find the flag, then patch the hole it came from."
- w-toolbox (how): "These are the tools from the challenges. Try them on any text."
- flag (event, each right flag; stale when the view changes): "Flag found. Now patch the hole."
- patched (event, each right patch; stale when the view changes): "Patched."
- notyet (how, first wrong flag): "Not this one. Read the artifact again, or open the Toolbox."
- all (event): "Every hole is patched. That's the job: finding is only half of it."

## Family engine
`kit/security.js`, described in full in tools/data-defenders/spec.md. This tool uses: **World** (Larkspur Freight; larkspur.example, birchline.example and the fake birchline-billing.example all pass `sec.safeDomain`), **Artifacts** (`file`, `note`, `log`, `call`, `email`), **Spots** (call lines, log rows, event cards), **Checks** (`strength` with `wordBits`, the common list, `caesar`, `vigenere`, `b64`), and **Locks** (each flag, normalized as above). No Clock.

## Sources
- CSTA 2026 ids HS-SYS-SE-31, HS-SYS-SE-32, HS-SYS-SE-33 (`data/standards/csta-2026-ids.txt`); CSTA 2017 3A-NI-05 to 3A-NI-08, 3B-NI-04: https://csteachers.org/k12standards/
- Check passwords against common and breached lists; allow at least 64 characters and spaces; no composition rules; no forced periodic changes; store passwords salted and hashed: NIST SP 800-63B-4, section 3.1.1.2, https://pages.nist.gov/800-63-4/sp800-63b.html
- Common passwords list: UK NCSC, "Most hacked passwords revealed" (2019), https://www.ncsc.gov.uk/news/most-hacked-passwords-revealed
- Passphrases of random words from a 7,776-word list (12.9 bits per word): EFF, "Dice-Generated Passphrases", https://www.eff.org/dice
- Bits and times computed in Python (bits = length x log2 pool; time = 2 to the power of bits divided by 10 billion per second, a model guess rate stated on screen).
- Multi-factor and phishing-resistant sign-in: CISA, "More than a Password" and "Implementing Phishing-Resistant MFA" (fact sheet, 2022), https://www.cisa.gov/MFA
- Base64 is an encoding with no key: RFC 4648, https://www.rfc-editor.org/rfc/rfc4648 . AES as the standard modern cipher: NIST FIPS 197, https://csrc.nist.gov/pubs/fips/197/final . Key management (keep keys apart from data): NIST SP 800-57 Part 1, https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final
- Caesar and Vigenere ciphers: Khan Academy, "Cryptography" (Computer Science), https://www.khanacademy.org/computing/computer-science/cryptography
- Pretext calls, tailgating and payment-change (business email compromise) scams, and calling back on a known number: CISA, "Avoiding Social Engineering and Phishing Attacks", https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks ; FBI IC3, "Business Email Compromise", https://www.ic3.gov
- Limit failed sign-in attempts; least privilege; review logs for unusual activity: NIST SP 800-63B-4 (rate limiting) and NIST CSRC Glossary "least privilege", https://csrc.nist.gov/glossary/term/least_privilege
- Encrypted strings computed in Python: Base64 of flag{not_a_lock} is ZmxhZ3tub3RfYV9sb2NrfQ==; shift 7 of flag{only_26_keys} is mshn{vusf_26_rlfz}; Vigenere LANTERN of flag{keep_keys_apart} is qlnz{ovra_krrw_rclrg}.
- Company, people, logs and messages are made up for Curio Class; no real site, brand or attack tool appears.

## Done when
1. Every flag is accepted in the forms described (with or without wrapper, any case) and only from its own tile; the Toolbox decodes C100, C200 (shift back 7) and C300 (LANTERN) to the Content flags.
2. Strength shows the Content bits and times for the four P200 candidates and prints the flag only for the six-word one; "On the common list" is yes only for password1 in P100.
3. P300's 03:02 row details hold the flag; S100 shows the flag after lines 2 and 5 (or 7 and 5); L300 shows TRACE only in the right order.
4. Scores: hint halves the flag, +50 only for a first-try patch; maximum 3,000; tile states show icon and word.
5. Progress survives a reload and stores no typed text; Clear progress (after Yes) resets.
6. Every size in STANDARDS.md: Flag and Submit visible without page scrolling in every challenge; 375 wide works in `drive.py --host`.
7. Keyboard-only solve of one tile per category; Motion off; voice lines as listed (how once, events each time); Read speaks the hint.
8. Every domain passes `sec.safeDomain`; console clean; no network requests; the name only as "Curio Class".

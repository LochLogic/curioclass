# Refine lens: Teaching, cipher-vault (Cipher Workbench, Curiosity No. 11)

Cold lens, round 1, 2026-11-06. Judged against docs/agents/CODEX-CURIOSITY.md and VISION.md "Curiosities: the second
shape", plus REFINE.md Teaching, STANDARDS.md and BASELINE.md. Bundle `tools/cipher-vault/cipher-vault.html` as built.
My frames and check scripts: `S:/CurioClass-codex-scratch/cipher-vault/teaching/` (frames/, checks.json, gv.json,
g2.json). Shared audit: `S:/CurioClass-codex-scratch/cipher-vault/audit-r1/`.

Counts: 1 blocker, 6 should fix, 5 polish, 2 nits.

## Findings

### 1. Encode toggle shows the whole secret key in Boxes and practice sheets (blocker, general)
- Where: src.html:921-931 (`renderSymbols`, Encode labels each glyph with `encoderLetter`), 1427-1450 (`openBox` keeps
  `state.symbolKey`), 1687-1694 (direction toggle).
- What: a partner opening a sealed Symbols box presses E (or Decode/Encode) once and the key card prints the sealer's
  letter under every glyph. The same toggle turns the counting sheet's 26-glyph puzzle and the Gold-Bug into a printed
  answer key. Boxes is the bench's one hidden-information activity ("sealed boxes let a partner try to crack your
  message"), and the toggle is not recorded as a Peek, so the box still shows "sealed" or "open" as if earned.
- How seen: gv.json shots `symbox-encode` (sealed a fresh New key box, opened it, clicked #direction: card read
  `DXWAGOKEUSZQHPBMCLNJITVFRY`) and `counting-encode` (frame `frames/counting-encode.png`: every glyph labelled).
- Better: in Encode with a box or sheet loaded, use a fresh key (or the partner's own key) rather than the hidden one,
  or count switching to Encode on a box as a Peek.

### 2. Switching to Encode wipes a glyph tape with no way back (should fix, general)
- Where: src.html:1690 (`if (!state.decode && /[\uE000-\uE0FF]/.test(state.input)) state.input = ''`), 1771.
- What: a student halfway through the counting sheet or Gold-Bug who presses E (one stray key; E is a shortcut) loses
  the 296- or 203-glyph tape. Toggling back leaves an empty tape; the only recovery is re-opening the sheet, which also
  clears every letter they assigned (`loadSheet` resets `symbolMap`). The status line says nothing.
- How seen: `counting-encode` returned `input: 0` after one click; frame shows 0 LETTERS.

### 3. The Counter's English ghost silently freezes on ordinary pasted text (should fix, general)
- Where: src.html:1074 (`$('ghost').disabled = ... !/^[A-Z\s.,'!:;?\-]*$/.test(analysisText())`), 1807.
- What: one digit, double quote, parenthesis or curly apostrophe anywhere on the tape disables the ghost fader and the
  chart drag, with no message. "Count anything: paste a paragraph" (spec, Things to do 2) is the core counting move,
  and most pasted paragraphs contain one of these. The ghost stays drawn at its old offset, so it looks alive.
- How seen: g2.json `ghost-digit` (`IN 1863 ... "HOLD ON"`: ghostDisabled true, 55 letters) and `ghost-curly`
  (`IT’S ...`: ghostDisabled true). The text already has letters only counted; the ghost needs only letters too.

### 4. Glyph counters are labelled 1 to 26, so "count the symbols, guess E" needs a lookup the card does not show (should fix, family:curiosity)
- Where: src.html:1037-1045 (`barChart`: non-letter bars get the index `i+1`), 1066.
- What: on the Gold-Bug and the counting sheet the bars read 1, 2, 3... while the key card shows no numbers. To learn
  that bar 5 (33) is Poe's `8` the student must click the bar (undocumented on screen) or hover for a title. Poe's own
  table lists the characters themselves. The frequency attack (the main thing these two sheets teach, and the
  attack side of the anchor) is one hidden step harder than it should be.
- How seen: `frames/poe-loaded.png` (bars 1 to 20, card shows glyphs only), `frames/counting-loaded.png`,
  `frames/leeson-loaded.png`. Counts themselves are right: 8:33, ;:26, 4:19, ‡ and ) 16, *:13, 5:12, 6:11 match the
  table in Poe's story (checked in Python on material.json).
- Better: draw each glyph under its bar (the SVG glyphs already exist), and in Sorted mode show the sorted English
  profile beside the sorted glyph bars so "biggest bar is probably E" can be seen, not remembered.

### 5. RAVEN and Vicksburg open already solved (should fix, family:curiosity)
- Where: src.html:1330-1339 (RAVEN: split 5, crib THE SAME at offset 53, three tools open), 1299-1307 (Vicksburg:
  PEMBERTON preset at offset 4), 1083 (`colGhosts = cols.map(guessShift)`).
- What: the RAVEN sheet loads with `KEY GUESS RAVEN` and a `Use key` button at the top of the panel, length 5 lit,
  columns labelled R A V E N, and the crib showing ENRAVEN. Vicksburg loads with `IMPLIED KEY HESTERBLU` while the case
  card says "Slide the crib PEMBERTON". Things to do 6 and 7 (Repeats finds the gaps, the Splitter at 5 makes five
  Caesars, slide the crib and watch the key appear) never happen; the student reads an answer. Sweeping the cheap
  way (REFINE Rounds) costs zero moves here. Curiosity rules say the "Things people have found" are found, not shown.
- How seen: `frames/raven-loaded.png`, `frames/wheel3.png` (Vicksburg state carried over), checks.json `vicksburg`.
- Better: open sheets at length 1 and offset 0 with ghosts at A, so the student finds the bumpiness spike, the factor,
  and the crib spot. Keep auto-fit as a button ("Fit ghosts") rather than the starting state.

### 6. Seal card key count overstates a rotor box by six times (should fix, general)
- Where: src.html:1389-1391 (`1.05456 × 10^5`, "six rotor orders"), 1439-1441 (`openBox` hands the partner the
  sealer's order, rings and plugboard; only the start is reset).
- What: the partner gets the rotor order, so the real search is 17,576 starts, and with the plugboard set the box
  silently disables the bombe but the card still says "Fixed-ring starts only". A meter that misleads when its
  assumption does not hold is a blocker class item in REFINE Rounds; I rate it should fix because the card also says
  "Bench estimate, not a real security rating". Either hide order and rings on open, or count what is actually hidden.
- How seen: gv.json `rotorbox`: sealed order III I II, rings 5 6 7, start H I J; opened box had order [2,0,1], rings
  [4,5,6], start [0,0,0].

### 7. Manual and notes read at a college level for a grade 5 to 12 bench anchored at 6-8 (should fix, general)
- Where: src.html:1581-1626 (Manual), notes.md "Key skills".
- What: "arithmetic mean of the columns' indices of coincidence ... sum f(f−1) divided by N(N−1)", "26!/6! ... injective
  mappings", "rejection-sampled crypto.getRandomValues", "chi-square", "Ring numbers shift the wiring, not the visible
  notch letters", "Separate a changing rotor state from an initial setting". The math is right and should stay
  reachable, but each entry needs a plain first sentence a sixth grader can use ("Bumpiness: how often two letters
  picked from a column match. English scores about 6.6, random letters about 3.8.") with the formula after it.
  Respecting the kid is not the same as writing for a cryptographer.
- How seen: read in source; Manual drawer frames `audit-r1/state-manual-1366x768.png`.

### 8. Vicksburg date is wrong against its own cited source (should fix, general)
- Where: src.html:1268 ("The museum dates opening to 2009").
- What: Catherine M. Wright's museum article (the cited source, acwm.org PDF, pp. 4-5) says the conservator examined
  the bottle in December 2008 and removed the message then; only the photograph reached the museum in January 2009.
  The bench should say the bottle was opened in December 2008 (and the message read in 2010, publicized 25 December
  2010, which it gets right).
- How seen: fetched and read the article PDF.

### 9. Padding tails print as words on the solved sheets (polish, general)
- Where: material.json `counting` ends `... TO COUNT. PAD YIWG`, `raven` ends `PAD LPVO`, `weather` ends `PAD CHRL`.
- What: a student who solves the counting sheet ends on "PAD YIWG" and will reasonably think they made a mistake, or
  connect it to the Pad machine. The only explanation is one clause in Sources ("Padding tails preserve the original
  comparison texts"). Say so on the sheet's card (for example "Ends with PAD and four filler letters, as real
  operators padded messages"), or drop the tails if the checked numbers still hold.

### 10. The real Vicksburg cipher slip is legible and published, but the bench uses a recomputed one (polish, family:curiosity)
- Where: src.html:1267, 1300.
- What: the museum article prints the slip's ciphertext (`SEAN WIEUIIZH DTG CNP LBNXGK OZ BJQB FEQT FEQT XZBW ...`),
  which nearly matches the bench's recomputation (`SEA'N WIEUIIZH, DTG CNP LBHXGK ...`), including a real clerk's
  doubled group `FEQT FEQT`. Real material is load-bearing in a Curiosity; the real slip, with its errors noted, is a
  better case than a clean reconstruction. Not wrong as built: the reconstruction is labelled honestly.

### 11. Leeson's stone reads itself (polish, family:curiosity)
- Where: src.html:1294-1297, 756-763.
- What: the case loads in Decode and the output tape shows REMEMBER DEATH at once, so "Read James Leeson's gravestone
  with the pigpen grid" (Things to do 3) is done by the bench. Pigpen has no key, so this is honest; but the student
  learns that by seeing the answer, not by matching shapes. Opening with the output covered until the student taps
  each shape on the card (or loads it in Encode-from-card) would keep the lesson.
- How seen: `frames/leeson-loaded.png`.

### 12. Splitter bar at length 10 is taller than at 5, unexplained (polish, general)
- Where: src.html:1081, Manual "Things people have found".
- What: on RAVEN the bumpiness bars are 4.7 4.7 4.6 4.7 **8.8** 4.5 5.0 4.4 4.4 **9.1** 4.2 4.4: the tallest bar is 10,
  not 5. Correct maths (multiples of the period also spike), but a student hunting the tallest bar picks 10. One
  "Things people have found" line ("Multiples of the key length spike too; the smallest spike is the key") fixes it.
- How seen: g2/gv `splitter12` and `frames/raven-loaded.png`.

### 13. Sorted mode hides the English model (polish, general)
- Where: src.html:1039 (`if (!sorted)` skips the ghost).
- What: "A Caesar shift slides the bars without changing their sorted heights" is the bench's best found thing, but in
  Sorted the comparison English profile disappears, so the student cannot see it match. Draw the sorted English
  ghost (E T A O I N...) in Sorted mode.

### 14. Plain English IC on the practice sheets is well above the stated "about 6.6" (nit, general)
- Where: Manual Splitter paragraph (src.html:1591), material.json.
- What: the RAVEN plaintext's own IC × 100 is 8.56 and the counting text's 7.19 (repetitive practice prose). A student
  comparing will see "English 6.6" and an English sheet at 8.6. A short note ("short, repetitive texts score higher")
  would cover it.

### 15. Read speaks "IC × 100" (nit, general)
- Where: src.html:1086, 1630. Read reads the splitter readout verbatim, `BUMPINESS 8.8 AT LENGTH 5 · IC × 100`; the
  spec's spoken form is "Bumpiness 8.8 at length 5". A voice says "I C times one hundred". Craft may own this.

## Standards (BASELINE rule 2)

Anchor module computer-science-6-8-cyber-attacks-and-defense ("Common attacks and the CIA triad"): MS-SYS-SE-32 (per
CSTA's alignment pages, the consequences of ignoring confidentiality, integrity and availability when handling data)
and MS-SYS-SE-33 (evaluate common cyber attack types and their preventions).
- Confidentiality and the cost of breaking it are taught well by doing: weak keys fall to the Fan, Counter and bombe;
  a reused pad becomes a Vigenere key; Venona is in the Manual. Integrity and availability are not exercised anywhere.
- Attacks taught are cryptanalytic (brute force, frequency, known plaintext, crib), real and hands-on, but not the
  "common cyber attacks" of the 6-8 standard (phishing, malware, password guessing), and no modern prevention is
  practised.
- The 2017 crosswalk 2-NI-06 (apply multiple methods of encryption) is taught thoroughly by all six machines.
- Verdict: consistent with the spec's own call ("a second card ... takes over no card"). Not a finding as long as the
  map lists this tool as a second card and the lesson tool owns MS-SYS-SE-32 and 33. If the map credits this tool
  with either code, that is a should fix: move them to the lesson tool. No thin activity should be added here.

## Done when (Teaching-relevant items)
1. PASS: shift 3 reads THE DIE IS CAST, every notch re-decodes (`audit-r1/state-wheel-three-1366x768.png`).
2. PASS: AAAAA to BDZGO; ADU to ADV, AEW, BFX; 1930 example dropped with reason (reflector A, confirmed at Weierud's
   cryptocellar page).
3. PASS: bumpiness 8.8 at 5, 20 of 23 gaps, THE SAME at offset 53 gives ENRAVEN, bombe leaves only B O X at @10 over 27
   spots (17,576 tests, 71 ms; all six orders 105,456 tests, 432 ms, one survivor), all three pad keys decrypt.
4. PASS: all cases and sheets load in any order; nothing locked or marked.
5. Seal/open works; Encode giveaway (finding 1) undermines it.
8. PASS: no score, goal, level or finish; lesson creep words absent from src.html.

## Facts spot-checked against a second source (13)
1. Enigma I wirings and test vector AAAAA to BDZGO: computed in the bench, matches the standard published vector.
2. Double step ADU, ADV, AEW, BFX: computed, matches the standard published sequence.
3. Norvig letter percentages, all 26: match norvig.com/mayzner.html exactly.
4. 1930 manual example uses Umkehrwalze A: confirmed at cryptocellar.org (Weierud).
5. Leeson died 28 September 1794 aged 38; key of three series, one dot, two dots, none, I standing for J: confirmed in
   Hemstreet 1899 (Gutenberg 39789); the bench's grid code matches it; REMEMBER DEATH decodes.
6. Gold-Bug: 1845 Tales text reads forty-one (eapoe.org); a later Poe correction to twenty-one is attested (Kern, The
   Nation, 1913, on eapoe.org). Bench claim holds.
7. Gold-Bug cipher counts (8:33, ;:26, 4:19, ‡ 16, ) 16, * 13, 5 12, 6 11): match Poe's table; cryptogram decodes to
   the plaintext character for character (checked in the bench).
8. Vicksburg plaintext wording ("I have sent some caps. I subjoin despatch from Gen. Johnston."): matches the museum
   article. Opening date: does not match (finding 8). AP story 25 December 2010: matches.
9. Vicksburg key MANCHESTER BLUFF: recomputed ciphertext nearly matches the slip printed in the museum article.
10. Mary, Queen of Scots: 57 letters, Lasry, Biermann and Tomokiyo, misfiled in the BnF archive: confirmed by multiple
    2023 news reports (WGBH, PopSci); 1578-1584 is in the paper's title.
11. 26! = 4.03 × 10^26, 26!/6! = 5.60 × 10^23, 6 × 26^3 = 105,456: recomputed.
12. Caesar shift 3 (Suetonius, Julius 56) and Augustus AA for X (Augustus 88, Loeb): consistent with the Loeb text as
    I know it; not refetched.
13. Weather sheet decrypts at I II III, B, rings A, start B O X: computed.

## Sensitivity review (rule 5): flag, not judged
- Vicksburg case and history: Confederate dispatch, "The Confederacy fought to preserve slavery", Pemberton's surrender.
- Mary, Queen of Scots: trial and execution stated plainly.
- Leeson stone: REMEMBER DEATH memento mori for grades 5 to 12 (spec open question).
- Al-Kindi attribution and wording ("Baghdad", Arab contributions).
- Map reach to social-studies-10-world-war-ii-and-the-holocaust: the bench's Enigma content is technical only; a
  reviewer should confirm that listing is appropriate.

## Audit pilot
- Leads confirmed: none are Teaching leads. The audit's clean rows I relied on: first screen at 1366x768 shows the
  hint and DECODE wheel; wheel-three state shows THE DIE IS CAST; no console errors or exceptions in any state.
- Leads wrong or noise for this lens: the "text hidden under circle" rows at small sizes are the wheel's own letters
  inside its rings; "hint out of view" in other machine states is the wheel hint correctly hidden on another page;
  manual-state "keep region covered" rows are the modal drawer by design.
- What it missed (all Teaching): the Encode giveaway on boxes and sheets (1), the destructive Encode wipe (2), the
  ghost freezing on digits and quotes (3), numbered glyph bars (4), pre-solved sheets (5), the rotor box key count (6),
  the wrong Vicksburg date (8), the PAD tails (9). None are mechanical; they need the state walked by intent.

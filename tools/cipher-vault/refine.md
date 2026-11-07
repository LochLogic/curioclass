OPEN (round 1, Claude Refine 2026-11-06; Codex fixes next)
Counts: blockers 2 (general 1, family 1), should fix 19 (general 10, family 9), polish accepted 18

# Refine: cipher-vault

Merged from `refine/teaching.md`, `refine/play.md`, `refine/craft.md` (round 1, 2026-11-06). Judged as a Curiosity
(CODEX-CURIOSITY.md, BASELINE). Frames: Teaching `S:/CurioClass-codex-scratch/cipher-vault/teaching/`, Play
`.../cipher-vault/play/frames/`, Craft `.../cipher-vault/craft/`, shared audit `.../cipher-vault/audit-r1/`.
Integrator spot-checks: src.html 921-931, 1037-1045, 1062-1089, 1260-1450, 1687-1694 read; both blockers confirmed in
code. No sensitivity.md yet: the sensitivity items below go to the fresh-agent review.

## Blocker
1. **Encode toggle prints a sealed box's key and turns sheets into answer keys.** src.html:924-926 (`renderSymbols`:
   in Encode every glyph is labelled with `encoderLetter`, from `state.symbolKey` or `MATERIAL.poeKey`), 1427-1450
   (`openBox` never replaces `state.symbolKey`, so the sealer's key is still loaded), 1687-1694 (`#direction`, also key
   E). A partner opening a sealed Symbols box presses E once and the key card shows the sealer's letter under every
   glyph; the same press labels all 26 glyphs of the counting sheet and Poe's whole key on the Gold-Bug. It is not
   recorded as a Peek, so the shelf still says "sealed" or "open" as if earned. Seen: Teaching gv.json `symbox-encode`
   (card read `DXWAGOKEUSZQHPBMCLNJITVFRY`), `teaching/frames/counting-encode.png`. Fixed looks like: while a box, the
   counting sheet or the Gold-Bug is on the bench, Encode never shows the hidden key (switch the card to a fresh key for
   the student's own writing, or treat the switch as a Peek and mark the box "peeked"); `openBox` loads the box's own
   symbol key instead of relying on what happens to be in state. Wheel, Square and Pad boxes already reset their keys;
   check Grid and Rotors give nothing away the same way (Rotors: see should fix 4). (general)
2. **Glyph counter bars are labelled by key-card position, so Poe's digit glyphs are mislabelled.** src.html:1043-1044
   (`barChart`: any non-letter bar gets `${i+1}`), 1066-1067 (aria "glyph N"). Poe's alphabet is digits and marks, so
   the position numbers read as glyphs: the tallest bar (33, glyph `8`) is labelled **5**, and glyph `5` occurs 12
   times. Sorted puts "5" on the top bar. The spec's own path (Things to do 4: count the symbols, guess E) leads the
   student to assign E to the wrong symbol, and every later guess builds on it. On the counting sheet the numbers 1 to
   26 match nothing on the key card, so the frequency attack needs an undocumented bar click. Seen: Play
   `play/frames/d08-case-poe.png`, `p02-poe-sorted.png`; Teaching `teaching/frames/poe-loaded.png`,
   `counting-loaded.png`. Counts themselves are right (8:33, ;:26, 4:19, ‡ and ) 16, *:13, 5:12, 6:11 match Poe).
   Fixed looks like: draw each glyph under its bar with `glyphSVG` (as the key card does), on every bar or at least on
   every labelled bar, for Poe and the drawn shapes alike; aria names the glyph (Poe's character, or "symbol N" matching
   the card's own label). (family:curiosity)

## Should fix
1. **RAVEN and Vicksburg open already solved.** src.html:1330-1339 (RAVEN: `split = 5`, crib THE SAME at `offset = 53`,
   three tools open), 1299-1307 (Vicksburg: PEMBERTON at `offset = 4`), 1083 (`colGhosts = cols.map(guessShift)`).
   RAVEN loads with `KEY GUESS RAVEN`, a `Use key` button, length 5 lit and the crib reading ENRAVEN; two clicks decode
   it. Vicksburg loads with `IMPLIED KEY HESTERBLU` while its card says "Slide the crib PEMBERTON". Things to do 6 and 7
   never happen; the finding is handed over before the first move. Seen: Teaching `frames/raven-loaded.png`,
   `frames/wheel3.png`, checks.json `vicksburg`; Play `d11-sheet-raven.png`, `d11b`, `d09-case-vicksburg.png`. Fixed:
   open RAVEN at length 1, offset 0, no key guess shown until the student picks a length; open Vicksburg with the crib
   at offset 0. The checked numbers (8.8 at 5, 20 of 23, ENRAVEN at 53, HESTERBLU) must still appear when the student
   gets there (Done when 3). Weather sheet: see Settled calls. (family:curiosity)
2. **Splitter offers a key guess from 2 or 3 letters per column.** src.html:1083-1087. On the 12-letter default tape at
   length 5 it shows "BUMPINESS 0.0 AT LENGTH 5", "KEY GUESS DSDND" and `Use key`, while the Counter beside it says "Too
   few letters". An estimate whose assumption (enough letters per column) does not hold; a partner cracking a short box
   gets a confident wrong key. Seen: `audit-r1/state-three-tools-1366x768.png`, Craft 7. Fixed: under 10 letters per
   column (the threshold the seal card already uses, src.html:1387) show "Too few letters per column" in place of the
   key guess and no `Use key`; an empty tape says "No letters" rather than "BUMPINESS 0.0" (Play nit, `p14`).
   Weighed as should fix, not blocker: the guess is the best fit on the data and `Use key` shows nonsense at once, so it
   does not lead work silently astray the way blocker 2 does; it still needs the guard. (family:curiosity)
3. **Sealing leaves the secret on the bench.** src.html:1409-1422 (`sealBox`). After Seal the input tape still reads
   MEET AT THE OAK and the wheel still shows SHIFT 07 under "Sealed · hand this device to your partner". Seen: Play
   `d20-sealed-then-shelf.png`. Fixed: on Seal, clear the tapes and reset the machine to its zero setting (or put the
   box's cipher on the tape), so the bench is safe to hand over. (family:curiosity)
4. **Rotor box key count overstates the search six times and ignores the plugboard.** src.html:1389-1391
   (`1.05456 × 10^5`, "six rotor orders"), 1439-1441 (`openBox` hands the partner the sealer's order, rings and plugs;
   only the start is reset). The real search is 17,576 starts; with plugs set the bombe is silently off but the card
   still claims a count. Seen: Teaching gv.json `rotorbox` (sealed III I II, rings 5 6 7, start H I J; opened with the
   same order and rings, start AAA). Fixed: either hide order, rings and plugs on open and count what is hidden, or
   keep handing them over and count 17,576 with the plugboard line stated plainly. Card and box must agree. (general)
5. **Switching to Encode wipes a glyph tape with no way back.** src.html:1690
   (`if (!state.decode && /[\uE000-\uE0FF]/.test(state.input)) state.input = ''`). One stray E on the counting sheet or
   the Gold-Bug loses the 296- or 203-glyph tape; toggling back leaves it empty, and re-opening the sheet clears every
   assigned letter. Status says nothing. Seen: Teaching `counting-encode` (`input: 0`). Fixed: keep the glyph tape and
   the assigned letters and restore them on the way back to Decode (blocker 1's fix can share this). (general)
6. **Square tableau is rebuilt on every update and misses 60 fps at 4x.** src.html:943-967 (`renderTableau` rewrites
   729 SVG text nodes and forces two layouts per `update()`). 600-letter tape, three tools: 31 ms per update at 4x,
   median 50 ms frames (20 fps), 40 ms keystroke latency; every other machine is under 1 ms. Done when 7 fails for this
   machine. Seen: Craft `perf`, `perf2` probes. Fixed: draw the 26 by 26 letters once; move only the highlight rects
   and the chosen-letter fill. (general)
7. **Rotor keyboard is below the fold at 680x425 and 375x812.** Rotors page, `.machine`. Only a sliver of the lamp row
   shows; the 26 typing keys need a scroll inside the machine (Done when 6; Things to do 8). Seen:
   `audit-r1/state-rotors-680x425.png`, `state-rotors-375x812.png`, `state-weather-search-680x425.png` (Play 7,
   Craft 6). Fixed: in short boxes give the lampboard and keys the height; put Run, Set back, Plugboard and ring fields
   in one compact row. (general)
8. **Symbol cracking: the guessed letters cannot be read against the cipher.** Symbols decode (Poe, counting sheet):
   `.tape-face` and `#output` are separate tapes. After E, T, H the output is `...THE...H...H..TE...` with the glyph
   beside THE on another tape, 21 of 203 glyphs per row and no scroll cue (scrollHeight 448 vs 62 visible). Seen: Play
   `p01-poe-ETH.png`, `d10-sheet-counting.png`. Fixed: under Symbols and Grid decode, show stacked pairs (glyph over its
   letter or a dot), as the crib tape already does, with whole rows and a scroll cue. (family:curiosity)
9. **Tools read Input by default, so the machine never moves the bars.** src.html:633 (`toolsRead:'input'`). In Encode,
   turning the wheel or growing the Square key changes only the output; the Counter, Splitter and Repeats sit still, so
   Things to do 5 ("watch the bars flatten as the key grows") and found item 1 are invisible. Seen: Play
   `d24-square-key.png`. Fixed: tools read the ciphertext side by default (input in Decode, output in Encode), with the
   select as an override. (family:curiosity)
10. **The English ghost silently freezes on ordinary pasted text.** src.html:1074 (ghost disabled unless the tape is
    only `[A-Z\s.,'!:;?\-]`). One digit, double quote, parenthesis or curly apostrophe disables the fader and chart drag
    with no message, and the ghost stays drawn at its old offset. Things to do 2 ("paste a paragraph") hits this every
    time. Seen: Teaching g2.json `ghost-digit`, `ghost-curly`. Fixed: the ghost works on the letters already counted;
    disable it only in Sorted (see polish 4) and on Symbols/Grid tapes. (general)
11. **Vicksburg date is wrong against its cited source.** src.html:1268 ("The museum dates opening to 2009"). The cited
    American Civil War Museum article (Catherine M. Wright) says the conservator opened the bottle and removed the
    message in December 2008; only the photograph reached the museum in January 2009. Fixed: "The bottle was opened in
    December 2008; the message was read in 2010." Check notes.md and tool.draft.json for the same date. (general)
12. **Read never speaks the first-run hint.** src.html:1627-1633 (`readText`), `hint:false` on `Curio.voice`. A fresh
    Read says machine, setting and output but never "Drag the inner ring."; CODEX-CURIOSITY says the hint is spoken once,
    then when Read is pressed. Seen: audit one-click row 4, Craft `voice_soundoff_read`. Fixed: while `#hint` shows,
    Read speaks it first. (family:curiosity)
13. **The hint is spoken after its moment has passed.** src.html:1636-1637 (`welcome` on any first tap on the Wheel),
    911 (`setShift` clears `#hint`). A first drag or Right press clears the hint, then "Drag the inner ring." plays
    (1325 ms after three Right presses already reading THE DIE IS CAST). Seen: Craft vlog,
    `craft/wheel-dragged-cw.png`. Fixed: the line's `valid` is "the hint is still showing". (family:curiosity)
14. **The hint runs over the inner ring's letters at compact sizes.** src.html:415 (`#hint { font-size:30px }` in the
    compact query), 520. At 680x425, 800x500 and 1000x625 "Drag the inner ring." is wider than the hub and sits on the
    D and J; the disk is about 155 px with 7 px letters at 680x425. Seen: `audit-r1/size-680x425.png`,
    `size-1000x625.png`, `craft/zoom-hint-680.png`, `play/frames/zoom-680-hint.png` (Play 8, Craft 4). Fixed: keep the
    hint inside the hub at every size (smaller, or two lines) and give the disk more of the compact height. (general)
15. **Counter and tape disagree on Grid and Symbols.** src.html:1069. With a letter tape the Counter reads "LETTERS 0 ·
    Too few letters" on a 1 to 26 axis while the tape says "12 LETTERS". Seen: `audit-r1/state-grid-1366x768.png`,
    `state-symbols-680x425.png`. Fixed: say what was counted ("SYMBOLS 0 · the tape holds letters") or count what the
    tape holds. (family:curiosity)
16. **Rotors opens with its windows at A A M, not A A A.** `update()` leaves `state.positions` at the end of the default
    tape. Typing AAAAA gives BTMCD while the Manual says AAAAA becomes BDZGO. Seen: Play `d22-rotors-type.png`. Fixed:
    on arrival the windows show the start setting (or a "START AAA" readout beside STEP), so the first press matches the
    Manual. (family:curiosity)
17. **Letter keys act as shortcuts while a student types on Rotors.** document keydown, src.html:2014 onward. Typing
    HELLO after clicking the Rotors button flips to Encode (E) and opens the Case file (O); on the wheel W replaces the
    input tape with no undo. Seen: Play `p04`, `p05`. Fixed: on Rotors, letter keys press the machine whenever no text
    field has focus (shortcuts there stay on digits and Escape); Swap gets an undo (one step back to the previous tape).
    Rebinding the spec's letter shortcuts elsewhere is under open questions. (general)
18. **Status still says "press Run tape" after Run.** src.html:1868 (survivor click); `runRotors()` never updates the
    status. Seen: Play `d14-weather-survivor-run.png`. Fixed: Run sets a status that matches the state. (general)
19. **Manual and seal card read at a college level for a band that starts at grade 5.** `showManual()` src.html:
    1581-1626, `keyCount()` 1374-1398, `showSeal()`, notes.md "Key skills": "arithmetic mean of the columns' indices of
    coincidence", "injective mappings", "rejection-sampled crypto.getRandomValues", "25 nonidentity shifts", "KEY COUNT
    2.6 × 10^1" for 26, "Non-ASCII letters", "6,000-character safety bound". Seen: Play `d17-manual.png`, `d19-seal.png`,
    `audit-r1/state-manual-1366x768.png` (Teaching 7, Play 11). Fixed: a plain first sentence per entry a sixth grader
    can use ("Bumpiness: how often two letters picked from a column match. English scores about 6.6, random letters
    about 3.8."), exact terms and formulas after it; small counts as plain numbers, large ones with superscripts.
    (general)

## Polish accepted
1. **Pace the bombe with Motion on.** `runBombe()`: 82 ms for one order, 432 ms for six; "watch 17,576 settings fall to
   one" is over in a blink (Play 13, `d13`, `p08`). With Motion on, step TESTED and the survivor count over about 1.5 s
   with the drums turning; the search stays fast; Motion off shows the result at once. (family:curiosity)
2. **Event messages beside their instrument.** `#status` src.html:205, 607: "Box open · Untitled", "One setting left ·
   tap it, then Run tape", "600 letters is the limit" appear only in 10 px on the plate (Play 14, Craft 9,
   `d21-open-box.png`, `audit-r1/state-weather-search-1366x768.png`). Show each beside what caused it (a stamp on the
   output tape when a box opens, the bombe line in its panel, the limit at the input count); keep the plate for the
   plate. (family:curiosity)
3. **Tool panel sticky header.** `.analysis-top` / `.analyzers`: with two or more tools, CRIB SLIDER and BUMPINESS hide
   under the "Tools read" bar and slivers of controls show above it (Play 15, Craft 8,
   `audit-r1/state-three-tools-1366x768.png`, `craft/zoom-three-tools-head.png`). Opaque header pinned at top 0 with the
   panel's padding inside it. (general)
4. **Sorted mode keeps the English model.** src.html:1039 (`if (!sorted)` skips the ghost). Draw the sorted English
   profile (E T A O I N...) beside the sorted bars, so found item 1 and "the biggest bar is probably E" can be seen.
   (general)
5. **Explain the PAD tails.** material.json `counting` ends `PAD YIWG`, `raven` `PAD LPVO`, `weather` `PAD CHRL`; a
   solved sheet looks like a broken decode (Teaching 9, Play nit, `d14`). One line on each sheet's card ("Ends with PAD
   and four filler letters, as real operators padded messages"). Keep the tails: the checked numbers depend on them.
   (general)
6. **Splitter: multiples of the key length spike too.** RAVEN reads 8.8 at 5 and 9.1 at 10 (Teaching 12,
   `frames/raven-loaded.png`). Add to the Manual's Splitter entry: "Multiples of the key length spike too; the smallest
   spike is the key." (general)
7. **Name the ghost fader.** It reads only "00" (Play 16, `d01`). Label it "English ghost" in the readout.
   (family:curiosity)
8. **Pad as stacked columns.** The Pad is a strip of key letters on a mostly blank card (`d16-sheet-pad-choose.png`).
   Stack cipher, key and plain letters in columns so the letter addition is the picture. (family:curiosity)
9. **Grid key card shows the grids.** It lists 26 glyphs (`d25-grid-encode.png`); draw the two grids and two crosses
   (three grids for Leeson) the shapes come from. (family:curiosity)
10. **Tapes show whole lines or a scroll cue.** Output cut half a line at the bottom (`d28`, `d29`). (general)
11. **Tableau card cut mid-column at the right edge** (`d24`, `d09`): fit it or show a clear scroll edge. (general)
12. **Symbols in Encode** still says "0 ASSIGNED" and shows the A to Z strip that does nothing there (`d26`): hide
    or relabel both in Encode. (family:curiosity)
13. **375x812 Symbols** has an empty band between the glyph controls and the output tape while the counter is cut
    (`audit-r1/state-symbols-375x812.png`): close the gap. (general)
14. **Range controls announce their meaning.** `#ghost` and the column sliders announce 0 to 25; add `aria-valuetext`
    ("Ghost shift 3, A to D", "Column 2 key S"), as the wheel already does (Craft 10). (general)
15. **Rotor ring fields as dials.** Bare inputs reading "1"; the spec reads "rings 01 to 26". Two-digit monospace dial
    with Up / Down like the windows (Craft 11, `audit-r1/state-rotors-680x425.png`). (family:curiosity)
16. **Nit: short practice texts score above 6.6.** RAVEN plaintext IC × 100 is 8.56, counting 7.19. One clause in the
    Manual's Splitter entry: "short, repetitive texts score higher." (general)
17. **Nit: Read speaks "IC × 100".** src.html:1086, 1630. Read says "Bumpiness 8.8 at length 5" (the spec's spoken
    form), not the unit tag. (general)
18. **Nit: plate at 680x425** wraps to "Cipher / Workbench" with the screw heads on the text (Play nit, Craft 13,
    `audit-r1/size-680x425.png`): one line, screws clear. (family:curiosity)

## Settled calls
- **Both blockers stand.** Teaching rated the glyph labels should fix (a lookup step); Play rated it blocker (the label
  names a different real glyph). Integrator read src.html:1043-1044: the label is `i+1`, and Poe's alphabet contains the
  digits 1 to 9, so it misleads, not just inconveniences. Blocker, under REFINE Rounds (a readout that misleads).
- **Splitter guess (should fix 2) is should fix, not blocker.** See its note: the output disproves a bad guess at once.
- **Weather sheet opens as built.** Crib WEATHERREPORT and All crib spots stay on: Things to do 10 is watching the bombe
  run on that crib, and 27 crib spots is a checked number. Only RAVEN and Vicksburg change.
- **Keep the checked readouts.** Pre-solved fixes change the starting state only; 8.8 at 5, 20 of 23 gaps, ENRAVEN at
  53, HESTERBLU, the bombe's B O X and the three pad readings must all still be reachable (Done when 3). Keep `Use key`
  (once enough letters per column).
- **Leeson stays readable on load.** Pigpen has no key; the bench showing REMEMBER DEATH is honest and is the point of
  found item 3 (Kerckhoffs). Do not add a tap-to-reveal step.
- **Standards (BASELINE rule 2):** Teaching found MS-SYS-SE-32 and 33 not taught here (cryptanalytic attacks only),
  consistent with the spec's "second card ... takes over no card". No activity is added. If the map credits this tool
  with either code, move them to the lesson tool; 2-NI-06 is taught well.
- **No goal, score or finish** comes in with any fix: the bombe pacing, stamps and pairs views are readouts, not
  rewards.
- **Voice event lines:** the build follows CODEX-CURIOSITY (hint once, then Read) over the spec's four event lines;
  do not add them. The spec line goes to open questions.
- **Sensitivity, not judged here:** the Vicksburg case and its Confederacy and slavery line and Pemberton's surrender;
  Mary, Queen of Scots' trial and execution; the Leeson REMEMBER DEATH stone for grades 5 to 12; the al-Kindi
  attribution and wording (Baghdad, Arab contributions); the map reach to social-studies-10-world-war-ii-and-the-
  holocaust from technical-only Enigma content. All go to the fresh-agent sensitivity review (`refine/sensitivity.md`).
  Codex does not change these texts in this round except the Vicksburg date (should fix 11).

## To the spec's open questions
- **A rotor case.** The 1930 manual example was dropped (needs reflector A); the rotor machine has only the invented
  weather sheet, while "a German field message" is promised in the first two minutes. Add UKW-A as a selectable
  reflector (wiring on the cited Crypto Museum page) so the 1930 message decrypts exactly, or find another verified
  Enigma I / UKW-B message? Either changes the honesty note "reflector B only" (Play 12).
- **The real Vicksburg slip.** The museum article prints the slip's ciphertext, including a clerk's doubled group
  `FEQT FEQT`; use the real slip with its errors noted instead of the recomputed one? Changes the case material and an
  honesty note (Teaching 10).
- **Letter shortcuts.** The spec binds E, W, F, C, S, R, K, B, O, X, M to bare letters; kids type letters first. Move
  them off bare letters (or behind a modifier) bench-wide? Should fix 17 handles Rotors and Swap's undo inside the spec.
- **Voice section.** The spec lists four event lines; the Curiosity brief allows only the hint and Read. Update the
  spec's Voice section to match the build (Craft nit 12).
- **Fan on the bench.** The Fan opens as a modal over the wheel; a fan beside the disk would keep the brass in view
  (Play 16). A layout change to the spec's `Fan` control.

## Not taken
- Leeson output covered until each shape is tapped (Teaching 11): settled above; pigpen is keyless and the bench is honest.
- Fan as a bench fan instead of a drawer (Play 16): a layout redesign; sent to open questions, not to Codex.
- Real Vicksburg slip, UKW-A rotor case, spec voice lines: spec changes; sent to open questions.

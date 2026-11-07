# Play lens: cipher-vault (Cipher Workbench, Curiosity No. 11), round 1

Played on the bundled `tools/cipher-vault/cipher-vault.html` with `scripts/drive.py` (port 9421), real drags and clicks
where it matters, JS only to set up state. My frames: `S:/CurioClass-codex-scratch/cipher-vault/play/frames/`.
Shared audit: `S:/CurioClass-codex-scratch/cipher-vault/audit-r1/`. Judged as a Curiosity (CODEX-CURIOSITY.md,
VISION "Curiosities: the second shape"), not against lesson norms.

## Short test

- **Would a kid open it unassigned?** Yes, nearly. Dragging the brass ring until WKH GLH LV FDVW turns into THE DIE IS
  CAST works with nothing read (`d01-drag-ring.png`: a real counter-clockwise drag lands on SHIFT 03 and the hint goes),
  and secret messages for a partner are a strong pull. What holds it back is below: the Gold-Bug, the most kid-shaped
  case, is hard to actually work, and the partner game leaks its own secret.
- **Would an adult play for fun?** Yes. Real Enigma I wirings, a crib with red "never itself" cells, a working
  exhaustive bombe (17,576 in about 80 ms, 105,456 in 432 ms), a splitter with real IC. This is the strongest part.
- **Is the real thing the interface?** Yes for the wheel, the tableau, the rotor box and the crib. Weaker for the Pad
  (a strip of letters on a blank card) and the Grid (a glyph list, not the grids the shapes come from).
- **Does it work with no finish line?** Yes. Nothing is locked, scored or marked done; cases open in any order
  (`d05-cases.png`). One risk to depth: the practice sheets open already solved (finding 4).

No question fails outright, so no short-test blocker. The one blocker is a misleading readout.

## Findings

### 1. Gold-Bug counter labels name the wrong glyph (blocker, family:curiosity)
- Where: `src.html:1044` (glyph bars labelled `${i+1}`, the key-card position), Symbols with the Poe case.
- What: Poe's alphabet is made of digits and marks, so the position numbers under the bars read as glyphs. The tallest
  bar (33) is labelled **5**, but it is glyph **8**; glyph 5 occurs 12 times. Sorted makes it worse: the top bar reads
  "5" (`p02-poe-sorted.png`). The spec's own path ("count the symbols, guess E") leads a student to assign E to 5, and
  every later guess builds on that. A readout that misleads when its assumption (labels are not glyphs) fails.
- How: `d08-case-poe.png`, `p02-poe-sorted.png`; counts checked from the material key (E = "8").
- Better: label each bar with the glyph itself (draw it with `glyphSVG`, as the key card does), for both Poe and the
  drawn-shape alphabet.

### 2. Symbol cracking: the output cannot be read against the cipher (should fix, family:curiosity)
- Where: Symbols decode (Poe case, counting sheet); input tape `.tape-face` and `#output` are separate tapes.
- What: after E, T, H the output reads `...THE...H...H..TE...THE.E...` with every other symbol a dot
  (`p01-poe-ETH.png`). To guess the next letter the way Legrand does (`;48;(88` becomes THE TREE) the student needs the
  glyph that sits beside THE, but the cipher is on another tape, spaced wide, and only 21 of its 203 glyphs show in one
  row (scrollHeight 448 vs 62 visible, no scroll cue). The counting sheet's glyph tape shows a half-cut second row
  (`d10-sheet-counting.png`). Things to do 4 is the most kid-shaped activity on the bench and it stalls here.
- Better: under Symbols and Grid decode, show the output as stacked pairs (glyph over its guessed letter or a dot),
  like the crib tape already does, so patterns and neighbours are visible together.

### 3. Tools read Input by default, so the machine never moves the bars (should fix, family:curiosity)
- Where: `src.html:633` (`toolsRead:'input'`), `#tools-read`.
- What: turning the wheel or growing the Square key changes only the output tape; the Counter, Splitter and Repeats
  read the input and stay still. Things to do 1 and 5 ("watch the bars flatten as the key grows from 1 to 10"),
  and found item 1 (a Caesar shift only slides the bars) are invisible until a student discovers the small
  "Tools read" select. With Encode on, the interesting text is the output.
- How: `d24-square-key.png` (Encode with LEMON, counter shows plain-text counts), code path `analysisText()`.
- Better: tools read the ciphertext side by default (input when decoding, output when encoding), with the select
  as an override; or show both as two bar colours.

### 4. Sheets and Vicksburg open already solved (should fix, family:curiosity)
- Where: `loadCase` / `loadSheet`, `src.html:1304` (`offset = 4`), `src.html:1338` (`offset = 53`), splitter at 5.
- What: the cheap pass (REFINE, Rounds). RAVEN opens with Splitter at 5, `KEY GUESS RAVEN` and a `Use key` button, and
  the crib at offset 53 already reading ENRAVEN (`d11-sheet-raven.png`); two clicks decode it (`d11b`). Vicksburg opens
  with PEMBERTON at offset 4 already showing HESTERBLU while the case card says "Slide the crib PEMBERTON"
  (`d09-case-vicksburg.png`). The weather sheet opens with the crib laid at the right length and All crib spots on.
  The finding is the reward; here it is handed over before the first move.
- Better: open sheets at length 1 and offset 0, with no key guess until the length is chosen, so the jump to 8.8 at 5
  and the HESTERBLU moment are the student's own.

### 5. Sealing leaves the secret on the bench (should fix, family:curiosity)
- Where: `sealBox()` `src.html:1409`.
- What: after Seal the input tape still reads MEET AT THE OAK and the wheel still shows SHIFT 07, while the status says
  "Sealed · hand this device to your partner" (`d20-sealed-then-shelf.png`). The partner sits down to the answer.
- Better: on Seal, clear the tapes and reset the machine to its zero setting (or put the box's cipher on the tape), so
  the bench is safe to hand over.

### 6. Letter keys are shortcuts when no field has focus (should fix, general)
- Where: document keydown, `src.html:2014` onward.
- What: on Rotors, a student who clicks the Rotors button and types HELLO on the real keyboard flips Decode to Encode
  (E) and opens the Case file (O) (`p04` result: direction "Encode", drawer "Case file"). On the wheel, S toggles
  Splitter, W swaps tapes, E flips direction (`p05`). W replaces the input tape with the output with no undo. The
  rotor machine's natural action is typing; it only works once a rotor key has focus.
- Better: on Rotors, letter keys press the machine whenever no text field has focus; elsewhere keep single-letter
  shortcuts off the letters a kid types first, or require the shortcut panel, and never bind a destructive action
  (Swap) to a bare letter.

### 7. Rotor keyboard hidden at 680x425 and 375x812 (should fix, family:curiosity)
- Where: `.machine` Rotors page, compact layouts.
- What: only the top of the lampboard shows; the typing keys sit below inside the machine's scroll box
  (`audit-r1/state-rotors-680x425.png`, `state-rotors-375x812.png`, `state-weather-search-680x425.png`). The machine's
  main control is out of sight at the iframe size (Done when 6).
- Better: at compact sizes put Run / Set back / Plugboard and ring inputs in one row and give the lampboard and keys the
  height; ring inputs can be smaller.

### 8. 680x425 wheel: tiny letters and the hint across the ring (should fix, family:curiosity)
- Where: `#hint` `src.html:520` (13 px in the SVG, not scaled with the disk), wheel at compact size.
- What: the disk is about 155 px across, its letters about 7 px, and the first-run hint runs over the inner ring's
  letters (`play/frames/zoom-680-hint.png`, from `audit-r1/size-680x425.png`; same at 800x500 and 1000x625). The first
  screen's one instruction is the hardest thing to read on it.
- Better: give the disk more of the compact height (the tool panel can shrink), and fit the hint inside the inner
  boss at every size.

### 9. Rotors opens with its windows at A A M, not A A A (should fix, family:curiosity)
- Where: `update()` sets `state.positions` to the end of the default tape when Rotors is selected.
- What: typing AAAAA gives BTMCD (`d22-rotors-type.png`), while the Manual says "start AAA. AAAAA becomes BDZGO".
  The windows are honestly where the machine ended, but nothing on screen says so, and a student checking the Manual
  thinks the machine is wrong.
- Better: show the start setting in the windows on arrival (or a "START AAA" readout beside STEP), so the first press
  matches the Manual.

### 10. Status stays "press Run tape" after Run (should fix, general)
- Where: survivor click `src.html:1868`; `runRotors()` never updates the status.
- What: after tapping the survivor and Run tape, the plaintext is on the output tape but the plate still says
  "Setting loaded · press Run tape" (`d14-weather-survivor-run.png`). Words must match the state (POLISH).

### 11. Manual and seal card words are past grade 5 (should fix, general)
- Where: `showManual()`, `keyCount()`, `showSeal()`.
- What: "25 nonidentity shifts", "KEY COUNT 2.6 × 10^1" for 26, "injective mappings", "rejection-sampled",
  "Non-ASCII letters", "a 6,000-character safety bound", "bounding lines" (`d17-manual.png`, `d19-seal.png`). The
  band starts at grade 5; a student who opens the Manual alone gets lost in its first paragraph.
- Better: plain first sentences per entry ("26 settings. Trying them all takes a minute."), with the exact terms
  after; write small key counts as numbers and use superscripts for large ones.

### 12. No rotor case: the bench's best machine has only an English practice sheet (should fix, family:curiosity)
- Where: Case file (`d05b-cases-scrolled.png`), note "1930 manual example omitted: it needs reflector A".
- What: the spec's first two minutes promise "a German field message"; the rotor machine now has only the invented
  weather report. Real material is load-bearing (VISION quality 5).
- Better: add UKW-A as a selectable reflector (its wiring is published beside B on the Crypto Museum page already
  cited) so the 1930 message decrypts exactly, or find another verified Enigma I / UKW-B message.

### 13. The bombe is over before it can be watched (polish, family:curiosity)
- Where: `runBombe()`; 82 ms for one order, 432 ms for six (`d13`, `p08`).
- What: Things to do 10 is "watch 17,576 settings fall to one"; the drums and the TESTED count are gone in a blink.
  The climax of the Rotors bench is flat.
- Better: with Motion on, pace TESTED and the survivor count over about 1.5 s with the drums turning; Motion off shows
  the result at once (the search itself stays fast).

### 14. Every event lands in 10 px on the plate (polish, general)
- Where: `#status` `src.html:205`, inside the maker's plate lower-left.
- What: "Box open · Untitled" (the partner's crack, `d21-open-box.png`), "One setting left · tap it, then Run tape",
  "600 letters is the limit" all appear only there, far from the action, in 10 px. Opening a partner's box is the peak
  of the partner game and it is a status line.
- Better: show the event beside what caused it (a stamp on the output tape when a box opens, the bombe line in its
  panel), and keep the plate for the plate.

### 15. Tool panel: sticky header covers scrolled tools (polish, general)
- Where: `.analyzers` with two or more tools open.
- What: CRIB SLIDER, its Guess field and BUMPINESS are hidden under the "Tools read" bar after the panel auto-scrolls,
  and slivers of controls show above the panel's top border (`play/frames/zoom-d28-top.png`, `d28-all-tools-600.png`,
  `audit-r1/state-three-tools-1366x768.png`).

### 16. Smaller polish
- Ghost fader has no label on screen, only "00" (`d01`). Name it "English ghost" in the readout.
- Pad is a strip of key letters on a mostly blank card (`d16-sheet-pad-choose.png`). Stack cipher, key and plain
  letters in columns so the letter addition is the picture.
- Grid key card lists 26 glyphs (`d25-grid-encode.png`); draw the two grids and two crosses the shapes come from.
- Tapes cut half a line at the bottom (output third line in `d28`, `d29`); show whole lines or a scroll cue.
- Tableau card is cut mid-column at the right edge (`d24`, `d09`).
- Fan opens as a modal over the wheel (`d03-fan.png`); a fan on the bench beside the disk would keep the brass in view.
- Symbols in Encode still says "0 ASSIGNED" and shows the A to Z strip, which does nothing there (`d26`).
- 375x812 Symbols: an empty band between the glyph controls and the output tape while the counter below is cut
  (`audit-r1/state-symbols-375x812.png`).

### 17. Nits
- Plate screws (the ⊖ marks) sit on the wrapped plate text at 680x425 (`audit-r1/size-680x425.png`).
- The weather plaintext ends "PAD CHRL" (padding tail), which reads as a broken decode (`d14`).
- An empty tape reads "BUMPINESS 0.0" rather than saying there are no letters (`p14`).

## For the sensitivity review (not judged here)
Leeson's REMEMBER DEATH stone; the Vicksburg dispatch and its Confederacy and slavery line; Mary, Queen of Scots'
trial and execution in the Manual.

## Checked and fine
Real drag decodes at shift 3 and clears the hint (`d01`); clockwise drag steps back (`d02`); Fan click sets the
shift (`p11`); all four cases and four sheets load in any order; Use key decodes RAVEN; bombe leaves B O X at @10 and
decodes the weather report; three pad keys give the three readings (`d16`); a sealed Wheel box opens when the output
matches (`d21`); 600-letter tape with all five tools at 1366 shows the limit line (`d28`); Motion off bombe and
default (`p06`, `p07`); rotor order select swaps rather than duplicating (my first duplicate test used a non-bubbling
event and was wrong). Read speaks machine, setting, output and the open readout (`p10`). Console clean in every shot.

## Counts
blocker 1 · should fix 11 · polish 4 (plus 8 small polish items under 16) · nit 3

## Audit pilot
- **Confirmed:** the `#hint` "under circle" lead at 680x425, 800x500 and 1000x625 (finding 8); `#keyboard` cut by a
  scroll panel at 680x425 and 375x812 (finding 7); the three-tools and weather-search overlaps with `#tools-read`
  (finding 15, it is the sticky header over scrolled tools).
- **Wrong or noise:** the single ring letters "under circle" (SVG letters over the brass disk, drawn correctly); "hint
  out of view" on other machines (the hint belongs to the wheel); Manual keep-region leads (a modal drawer); "welcome
  not heard" on first taps of Case file, Boxes and other machines (right for a Curiosity: the hint is spoken once on
  the wheel, then only on Read); sideways-scroll symbol and letter strips at compact sizes (deliberate scroll rows).
- **Missed:** the Gold-Bug bar labels (finding 1), the separated symbol tapes (2), Tools read default (3), pre-solved
  sheets (4), the secret left on the bench after Seal (5), letter shortcuts while typing (6), rotor windows at AAM (9),
  stale status (10), the bombe's invisible run (13).

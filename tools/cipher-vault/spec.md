# Cipher Workbench (Curiosity No. 11)

Tool id stays `cipher-vault`. Plate: `Curio Class Curiosities · No. 11 · Cipher Workbench`. Build brief:
docs/agents/CODEX-CURIOSITY.md. In `tool.draft.json`: `"curiosity": true`, `"plate": 11`, title "Cipher Workbench".

## The real thing
A codebreaker's bench. Six working machines (a brass cipher wheel, the pigpen grid, a symbol substitution, the
Vigenere square, a small three-rotor machine with real Enigma I wirings, a one-time pad) and five breaking tools (a
frequency counter, a column splitter, a repeat finder, a crib slider, a bombe), all on any message the student types.
A cipher breaks when it leaks the shape of the language. A case file holds real historical messages in any order;
sealed boxes let a partner try to crack your message on this device.

## Map
- Anchor: computer-science-6-8-cyber-attacks-and-defense (MS-SYS-SE-32, MS-SYS-SE-33; 2017 crosswalk 2-NI-06, apply
  multiple methods of encryption to model the secure transmission of information).
- Also reaches: computer-science-5-the-cia-triad (confidentiality), computer-science-9-12-cybersecurity,
  math-7-probability (an English letter model against observed frequencies), social-studies-6-ancient-rome (Caesar),
  social-studies-8-the-civil-war (the Vicksburg message), social-studies-10-world-war-ii-and-the-holocaust (Enigma).
- Grade band 5 to 12. A second card beside the anchor's lesson tools: a teacher plan would teach 2-NI-06 well but not
  the anchor's attack side, so it takes over no card.

## The first two minutes
- 0 s: the brass wheel (rings A to Z) fills the bench at 0; the input tape reads `WKH GLH LV FDVW`. The inner ring
  rocks once with a tick. Hint on the brass: "Drag the inner ring."
- 3 to 8 s: the ring clicks notch by notch and the output tape re-decodes at every notch until, at 3, it reads `THE
  DIE IS CAST` (`SHIFT 03 · A to D`). Nothing celebrates: the English is the reward. The hint goes.
- 10 to 120 s: they type their own name and watch it encipher; they tap the Counter and drag the grey English ghost
  over the bars; or they open the manila case file: a gravestone, a story's cryptogram, a Civil War slip, a German
  field message.

## Things to do
1. Spin the wheel on any message; show all 26 shifts at once (`Fan`) and spot the one that is English.
2. Count anything: paste a paragraph and watch E, T, A, O rise; drag the ghost over a Caesar text to read its key.
3. Read James Leeson's 1794 gravestone with the pigpen grid, then write your own pigpen.
4. Crack Poe's Gold-Bug cryptogram (1843) the way his character did: count the symbols, guess E, look for THE.
5. Encode with the Vigenere square and watch the counter's bars flatten as the key grows from 1 letter to 10.
6. Break the RAVEN practice sheet: Repeats finds the gaps, and the Splitter at length 5 makes five Caesars.
7. Slide the crib PEMBERTON along the Vicksburg message and watch part of its key (HESTERBLU) appear under it.
8. Type on the rotor machine: the same key lights a new lamp every press, and never its own letter.
9. Set the rotor machine to the 1930 German manual's example settings and read its field message.
10. Run the bombe on the weather report practice sheet and watch 17,576 settings fall to one.
11. Make a pad with `Random key`, then see two other keys that turn the same ciphertext into other messages.
12. Stack ciphers (RAVEN then CAT is one key of length 15), or seal a message in a box and hand it to a partner.

## Controls
- Machine rack, left edge (keys 1 to 6 when no tape has focus): Wheel, Grid, Symbols, Square, Rotors, Pad. `Encode` /
  `Decode` toggle switch (E). `Swap` puts the output on the input tape (W).
- Input tape: up to 600 letters; A to Z enciphered, other characters pass through; at 600, "600 letters is the limit".
- Wheel: ring, 26 detents, 0 to 25; drag or Left / Right. `Fan` (F). Grid: pigpen key card and a 26-key symbol pad.
- Symbols: tap a glyph, then a letter on the A to Z strip; every copy fills in amber; a reused letter moves. `Clear`,
  `New key`. Glyphs: the 26 drawn shapes of the super spec (git fefed72e, Room 3); the Gold-Bug case uses Poe's.
- Square: the 26 by 26 Vigenere tableau as a printed card; key 1 to 40 letters (non-letters ignored with a note); the
  key letter's row and plain letter's column light, and their crossing is the cipher letter.
- Rotors: three thumbwheels A to Z (Up / Down), order of I, II, III, rings 01 to 26, reflector B, plugboard 0 to 10
  cables (drag socket to socket; off by default), QWERTZ keyboard and lampboard, `Run` (whole tape), `Set back`.
- Pad: key strip; `Random key` (crypto.getRandomValues) fills it to the message length; a shorter key repeats and the
  strip turns orange: "A repeated pad is just a Vigenere key."
- Tool rack, right edge (C, S, R, K, B): Counter (`A-Z` / `Sorted`, ghost offset 0 to 25), Splitter (length 1 to 12),
  Repeats (factors 2 to 10; tap one to send it to the Splitter), Crib (up to 20 letters, slide by drag or arrows), Bombe
  (`Run bombe`, Rotors only). `Tools read: Input / Output`.
- Case file (O), Boxes shelf (X, 12), Manual (M), power panel (Motion, Sound, Read). Escape closes any drawer.

## Readouts
Monospace, live, beside what they measure. Wheel `SHIFT 03 · A to D`. Counter: count per bar, `LETTERS 296` (under 20:
"Too few letters to read the bars."). Splitter: bumpiness (index of coincidence x 100, one decimal; English about 6.6,
random 3.8) over lengths 1 to 12, `KEY GUESS` from the columns' ghosts (`Use key`). Repeats: gaps, `5 divides 20 of
23`. Crib: implied key letters, or red "never itself here" cells (Rotors). Rotors `STEP 0050`. Bombe `TESTED 105,456`,
survivors, ms. Key count in scientific notation and the crack meter line on the seal card.

## The Manual
A drawer, lower-left: each machine and tool, the readouts, key counts, case histories (never locked), honesty notes,
sources. Things people have found:
1. A Caesar shift only slides the bars: sort them and the heights match the plain text exactly (super spec checks).
2. Augustus used a shift of one and wrote AA for X instead of wrapping (Suetonius, Augustus 88).
3. Pigpen has no key, so knowing the grid reads every message. Kerckhoffs (1883): only the key may be secret.
4. Counting letters to break a cipher was first written down by al-Kindi in Baghdad in the 800s (Al-Kadi 1992).
5. Splitting a Vigenere text by the key length makes counting work again: RAVEN's bumpiness jumps to 8.8 at length 5.
6. The Vicksburg key MANCHESTER BLUFF was one of a few keys Confederate officers reused (Kahn 1967).
7. Enigma never turns a letter into itself, so codebreakers could rule out where a guessed word sat (Bletchley Park).
8. Soviet one-time pads were reused in the 1940s, and US codebreakers read thousands of messages (NSA, Venona).
9. In 2023 three codebreakers read 57 lost letters of Mary, Queen of Scots, misfiled in France's national library
   (Lasry, Biermann and Tomokiyo, Cryptologia 2023).

## Look
A codebreaker's bench: a dark oiled worktop, a brass cipher disk with engraved letters, the Vigenere tableau printed
like an old reference card, paper tape for input and output, a wooden rotor box with an amber lampboard, the bombe's
three coloured drums, manila folders. Palette (contrasts computed in the super spec): bench `#15171c` with faint grain,
panel `#1e2128`, ink `#efe9dc` (14.82:1), muted `#a9a294` (6.35:1 on panel), verdigris `#3cc7a2` (8.44:1) with
`#06231b` on it, lamp amber `#ffc94a` (10.52:1; also the focus ring), card and tape `#efe4cc` with ink `#2a2118`
(12.52:1). Tapes in a typewriter monospace.
- 1366x768: input tape across the top; machine centre-left, at least half the height; open tool centre-right; output
  tape along the lower third; racks on the side edges; case folder and power panel top-right; plate and `Manual`
  lower-left. 375x812: input tape, machine full width (about 340 px), output tape, one tool panel, two scrolling tab
  rows (machines, tools) above the plate; plate and `Manual` lower-left; no sideways scroll.
- Sound: wheel tick, rotor click, lamp hum, bombe whirr, seal thump, box spring. Motion off: no spins, results at once.

## Real material and sources
Cases (all in code, about 6 KB):
- Caesar: `THE DIE IS CAST` at shift 3 (`WKH GLH LV FDVW`). Suetonius, Julius 56 (shift of three) and 32 (the phrase,
  Rubicon, 49 BCE), Loeb translation on LacusCurtius, public domain.
- Leeson stone (Trinity Churchyard, New York, died 1794): pigpen REMEMBER DEATH (Atlas Obscura). Key: grid A to I,
  dotted grid J to R, X with S T U V (opening up, left, right, down), dotted X with W X Y Z.
- The Gold-Bug (Poe, 1843, public domain): "A good glass in the bishop's hostel in the devil's seat forty-one degrees
  and thirteen minutes northeast and by north main branch seventh limb east side shoot from the left eye of the
  death's-head a bee line from the tree through the shot fifty feet out". Poe's key: a 5, b 2, c dash, d dagger, e 8,
  f 1, g 3, h 4, i 6, l 0, m 9, n *, o double dagger, p period, r (, s ), t ;, u ?, v pilcrow, y colon; letters run
  together. Compute the cryptogram from the key and check it against a printed copy. Draw the dash as a short rule in
  code; never put an em dash character in the source.
- Vicksburg, 4 July 1863, Maj. Gen. John G. Walker to Lt. Gen. John C. Pemberton, found in a bottle, decoded 2010 by
  David Gaddy (AP, December 2010; American Civil War Museum): "Gen'l Pemberton: You can expect no help from this side
  of the river. Let Gen'l Johnston know, if possible, when you can attack the same point on the enemy's line. Inform me
  also and I will endeavor to make a diversion. I have sent you some caps. I subjoin a despatch from General
  Johnston." Key MANCHESTER BLUFF, letters only. Recheck the wording against the museum's record at build.
- Enigma, 1930 German Army manual example: order II I III, rings 24 13 22, plugs AM FI NV PS TU WZ, start ABL. Plain
  `FEIND LIQEI NFANT ERIEK OLONN EBEOB AQTET XANFA NGSUE DAUSG ANGBA ERWAL DEXEN DEDRE IKMOS TWAER TSNEU STADT` ("Enemy
  infantry column observed. Start at the south exit of Baerwalde. End 3 km east of Neustadt."). Cipher `GCDSE AHUGW
  TQGRK VLFGX UCALX VYMIG MMNMF DXTGN VHVRM MEVOU YFZSL RHDRR XFJWC FHUHM UNZEF RDISI KBGPM YVXUZ`. Sources: D.
  Rijmenants, "Enigma message procedures"; Crypto Museum. If the built machine does not decrypt it exactly, drop the case.
Practice sheets (written for this bench, labelled so). Copy texts, keys and ciphertexts exactly from the super spec
(git fefed72e, Rooms 3 to 6): the 296-letter counting text and its symbol key; the 259-letter RAVEN text; the weather
report (rotors I II III, B, rings A, no plugs, start B O X); the pad `XADHN ANJMN GKACE VFVUV C` with keys for NOW GO
STUMP YOUR PARTNER, THE CAT SLEEPS ON MY BOOKS and THE VAULT IS EMPTY GO HOME.
Engine data: Enigma I rotor I `EKMFLGDQVZNTOWYHXUSPAIBRCJ` notch Q, II `AJDKSIRUXBLHWTMCQGZNPYFVOE` E, III
`BDFHJLCPRTXVZNYEIWGAKMUSQO` V, UKW-B `YRUHQSLDPXNGOKMIEBFZCWVJAT`, real double step (Crypto Museum wiring page).
English frequencies for the ghost (Norvig, "Mayzner Revisited"): E 12.49 T 9.28 A 8.04 O 7.64 I 7.57 N 7.23 S 6.51
R 6.28 H 5.05 L 4.07 D 3.82 C 3.34 U 2.73 M 2.51 F 2.40 P 2.14 G 1.87 W 1.68 Y 1.66 B 1.48 V 1.05 K 0.54 X 0.23 J 0.16
Q 0.12 Z 0.09. Crack meter lines and key counts: unchanged from the super spec (git fefed72e); thresholds 50 and 150
letters (Symbols) and 10 and 30 letters per column (Vigenere) come from its Python sweeps.
History: Singh (1999); Kahn (1967); Kerckhoffs (1883); Al-Kadi, Cryptologia 16(2) 1992; Shannon, BSTJ 28 (1949);
NSA, "Venona"; Bletchley Park; NIST FIPS 197. Art: at most 5 painted images (bench top, rotor box, folder, gravestone,
brass), about 500 KB WebP; all letters, glyphs, lamps and bars in code. Budget about 0.8 MB (goal 2 MB, ceiling 6 MB).

## Honesty notes
- No message in Caesar's hand survives: the case is his method on a line Suetonius reports. The Gold-Bug is fiction.
  The Vicksburg ciphertext is recomputed from the published plaintext and key. Each case says so.
- The rotor machine has rotors I to III and reflector B only (the army had five rotors from 1938; the navy a four-rotor
  model). The bombe works only with the plugboard off; Welchman's diagonal board is not modelled.
- The crack meter describes these tools on this bench, not real security. Nothing here is modern encryption, and the
  Manual says modern ciphers (AES, since 2001) leak no pattern of English.

## Voice
`gravel-ranger` (an old codebreaker). First-run hint on the brass, spoken once after the first touch: "Drag the inner
ring." Event lines only: "One setting left. Tap it, then Run." / "Nothing fits there. Slide the guess." / "Sealed.
Hand it to your partner." / "Cracked. Show the maker how." Read speaks the machine and setting, the output tape's first
80 letters and the open tool's main readout ("Bumpiness 8.8 at length 5").

## Done when
1. First two minutes with no reading: dragging the ring re-decodes every notch and shift 3 reads THE DIE IS CAST.
2. Every machine encodes and decodes any typed message; Rotors gives AAAAA to BDZGO (I II III, B, AAA) and the double
   step ADU, ADV, AEW, BFX; the 1930 example decrypts exactly or its case is dropped and reported.
3. The super spec's checked numbers show where claimed: bumpiness 8.8 at 5, 20 of 23 gaps, crib THE SAME shows ENRAVEN,
   the bombe leaves only B O X over 27 crib spots, the three pad keys.
4. All five cases and four practice sheets open in any order; nothing is locked or marked done.
5. Boxes seal, open on a matching output, Peek and Delete confirm, 12-box cap; boxes and the last tape survive a reload;
   storage blocked still plays with one line saying so.
6. The bench is the screen at 1366x768, 680x425 and 375x812: machine and both tapes visible without scrolling.
7. A 600-letter tape with three tools open holds 60 fps at 4x CPU slowdown; 105,456 bombe tests finish under 2 s.
   Keyboard reaches every control and each announces its value; Read speaks as above.
8. No score, goal, level, sticker or finish screen anywhere; no timer, no room order, no "you did it".
9. Short test passed and reported with one frame beside Elements Inspector; console clean, no network, no em dashes.

## Open questions
- Leeson's stone reads REMEMBER DEATH. Keep it for grades 5 to 12? Lean: keep; it is a real 1794 memento mori.
- Say plainly that Mary's letters were used at her trial and she was executed in 1587? Lean: yes (BASELINE rule 5).
- A pencil "read" mark on a case once its plaintext appears? Lean: no; the readable text is the only sign.
- The plugboard (new, needed for the 1930 case): keep? Lean: keep, off by default.

## What changed from the super tool spec
- Six rooms in a fixed order became a case file of real messages in any order; room texts became practice sheets.
- Goals, the stamp Book, door locks, pad pieces, the Clock and "Open all doors" removed; their lessons went to the Manual.
- Keyword became the Vigenere Square; the rotor machine gained ring settings and a plugboard.
- Three modes and the kit header became one bench; the Boxes timer, 25 images and the room voice lines were cut.

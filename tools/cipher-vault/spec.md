# Cipher Vault

## One idea
Every lock in the vault is a real historical cipher machine you can grab and play (a brass wheel you spin, a rotor box
whose lamps light as you type), and the same few breaking tools (a letter counter, a column splitter, a guessed word)
crack each one for one reason you can see: the cipher leaks the shape of English. Then you build a message of your own
and the tool tells you, honestly, whether your partner can crack it.

## First minute
No reading needed. Nothing speaks before the first tap (kit rule).
- 0 s: Vault mode opens straight into Room 1, Caesar's Door. A painted stone doorway; above it, carved letters (drawn
  in code on a blank painted lintel) read `WKH GLH LV FDVW. SDG NPKEC`. In the middle of the stage, much bigger than
  anything else, a brass cipher wheel: outer ring A to Z, inner ring A to Z. The inner ring glints and rocks a few
  degrees back and forth, once, with a soft tick.
- 3 s: the student grabs the inner ring and drags. It turns notch by notch, with a click per notch, and the strip
  under the lintel (the "reading strip") re-decodes live at every notch: `VJG FKG KU ECUV`, `UIF EJF JT DBTU`. The
  welcome line starts (Voice wVault).
- 6 s: one more notch and the strip snaps into `THE DIE IS CAST. PAD KMHBZ`. The words flash warm white, two iron bolts
  in the door slide back with a deep clunk, the door swings in, and five gold letters (`KMHBZ`) fly off the strip into
  the pad strip along the bottom of the stage. The keeper says "The die is cast. Caesar said that at the Rubicon."
- 10 to 60 s: the room map slides in: six doors in a row, door 1 open, door 2 glowing. Tapping it shows the Mason's
  Stone: a painted gravestone with shapes of lines and dots (pigpen). Tapping any shape lights its cell in a grid card
  and drops its letter into the reading strip. Without a word of instructions the student has learned "a cipher is a
  rule plus a setting, and the strip shows what the setting does".

## Not like
- capture-the-flag (9-12, security family): twelve audit tiles with a Shift and Keyword decoder as side tools; ciphers
  there are "not a lock" notes to find a flag in, then patch. Here the cipher machines are the toy, the breaking tools
  are the lesson, and there is no flag, patch or score.
- phishing-spotter (6-8, same module): fast keep-or-report rounds about attacks on people. Here no attacks, no people,
  no clock: how ciphers work and why they break, on historical ciphers and the student's own messages.
- data-defenders (5, security family): escape rooms of repair puzzles for confidentiality, integrity and
  availability. Here the escape chain is six real ciphers in historical order, and confidentiality only.
- packet-race, internet-journey (6-8 networks): how data moves. Here what happens to a message before it moves.
- New card in this module (SUPER.md); it takes over no other card.

## Who and how
- Grades 5 to 12 (catalog: grade 6-8, Computer Science, Cyber Attacks and Defense, Systems and Security). Students
  drive, solo or in pairs on one laptop (pairs swap seats for Boxes). 15 to 45 minutes, built to be reopened.
- Topic line: "how historical ciphers work and how they are broken".
- Standards (CSTA 2026, as listed): MS-SYS-SE-32, MS-SYS-SE-33. 2017 crosswalk: 2-NI-06 (apply multiple methods of
  encryption to model the secure transmission of information).
- tool.json: driver "students", minutes "15-45", modes ["Vault", "Workshop", "Boxes"], grades_label "Grades 5-12".
  Kit starter; band 6-8 own `:root` (see Look).

## Screens and modes
Header: title "Cipher Vault", subtitle "Every lock leaks." Mode buttons `Vault` (opens first), `Workshop`, `Boxes`;
`Book` (the goal sticker book, with a counter "4 / 22"); kit `Motion`, `Sound`, `Read`. Layout: stage in the middle
and largest; the tool tray as a row of big round buttons under the stage; the panel on the right with `#hint`, the
current tool's controls and readouts. Under 1000 px wide the panel goes below the stage; under 900 px tall the panel
compacts to buttons first. The machine and the reading strip stay visible without scrolling at every STANDARDS size.

### Vault (the escape chain, opens first)
Focus: the room's machine, center stage at least half the stage height, with the ciphertext on its painted surface
above and the reading strip (live output) right under it.
- Room map: a strip of six doors along the top of the stage (Content "Rooms"). Opened doors are lit and can be
  re-entered; the next door glows; doors past it are dark with a padlock and say "Opens after door N". Tap a lit door
  to enter.
- In a room: the painted backdrop, the ciphertext, the machine, the reading strip, and the tool tray showing only the
  tools this room offers (Content lists them). The pad strip (21 slots, filled pieces in gold) runs along the bottom.
- The door opens when the reading strip equals the room's plaintext (letters only, case and punctuation ignored).
  Nothing is typed as an answer: the machine's setting is the answer.
- `Story` (panel) opens a short card with the room's history (Content), its painted portrait-free picture, and its
  source line. Closed by default except the first visit to each room, when it sits folded under the hint as one line
  with `More`.
- `Clock` (panel footer, off by default): a count-up timer for team races, shown on the room map; `Reset vault`
  (confirm Yes/No) closes every door and empties the pad; `Open all doors` (confirm, for teachers) lights every door
  and fills the pad.

### Workshop (free play)
Focus: the chosen machine, center stage; the message box above it and the output strip below.
- Machine picker (6 big buttons): `Wheel` (Caesar), `Grid` (pigpen), `Symbols` (substitution with symbols),
  `Keyword` (Vigenere), `Rotors` (simplified Enigma), `Pad` (one-time pad).
- Message box: type up to 600 letters (any characters; only A to Z are enciphered, other characters pass through
  unchanged, case shown as capitals). `Encode` / `Decode` switch (Rotors and Pad show one `Run` button, since they
  are their own inverse or say so). `Swap` puts the output into the message box (so stacking ciphers is two taps).
  `Example` loads one of the room plaintexts.
- Breaking tools tray (same as Vault): `Counter`, `Splitter`, `Repeats`, `Crib`, `Bombe` (only with Rotors). Each acts
  on the output strip, or on the message box when `Tools read: Message / Output` is switched.
- `Seal a box` (panel): opens the seal card (Interactions "Sealing") with the crack meter.
- `Key count` (panel, small): how many keys this machine has (Content "Key counts") next to whether the tools here crack
  it: the "big number is not enough" lesson in one table.

### Boxes (stump a partner, on this device)
Focus: the open box's ciphertext and the partner's working strip, center stage.
- A shelf of up to 12 sealed boxes (painted box cutouts, each with its nickname and machine name on a code-drawn tag,
  and a crack meter word). Tap one to open it.
- An open box shows its ciphertext, the machine it was sealed with (said on purpose: Content "Kerckhoffs"), its length,
  and the breaking tools plus that machine with an empty key. The partner works the machine; the box springs open
  when their output equals the sealed message (letters only).
- `Peek` (confirm "Show the message and key? The box counts as not cracked."), `Delete` (confirm), `Back to shelf`.
- Cracked boxes show a green seal and how long it took; peeked ones a grey seal.

## Goals
Optional; 22 goals, easy to hard. Each met goal: a stamp sound, the Book button flashes, line `goalDone` with the goal
name. The Book shows found stamps (painted wax seals) and unfound ones as outlines with their title. Goals never block
play. Checks run on the real state.
1. First turn. Turn the wheel at least one notch. Teaches: a key is a setting.
2. Caesar's Door. Room 1 opens. Teaches: 25 keys can simply all be tried.
3. Every key. In Workshop, show one message at all 26 wheel positions (set of visited shifts has 26). Teaches: brute
   force on a small keyspace.
4. The grid is the key. Room 2 opens. Teaches: a cipher whose method is the secret falls once the method is known.
5. Write like a Mason. In Workshop, Grid-encode a message of 10 or more letters. Teaches: pigpen is substitution with
   shapes.
6. Same old shape. Run the Counter (sorted view) on two texts where one is a Caesar shift (1 to 25) of the other.
   Sorted bar heights match exactly. Teaches: Caesar only slides the bars.
7. Slide the ghost. In the Counter on a Caesar text of 40+ letters, drag the English ghost to the real shift (the
   ghost's offset equals the shift). Teaches: matching the bump pattern.
8. Top three. In Room 3, the first three correct glyph assignments are the three tallest bars (E, T, O in that text).
   Teaches: count first.
9. Short words. In Room 3, have T, H and E all correct while 6 or fewer glyphs are assigned. Teaches: word shapes.
10. The Queen's Letter. Room 3 opens.
11. Gap hunter. In Repeats on Room 4, tap the factor that divides at least 80 percent of the gaps (only 5 does: 20 of
    23). Teaches: Kasiski's method.
12. Bumpy columns. In the Splitter on Room 4, set length 5 (bumpiness 8.8 against 4.5 to 5.0 for lengths 1 to 4, 6 to
    8). Teaches: the right length turns one flat mess into five Caesars.
13. A word leaks the key. In Room 4 slide the Crib `THE SAME` (or any crib of 4+ letters) to a spot where the implied
    key shows 4 or more letters of RAVEN in order (at letters 54, 134 or 169 it reads ENRAVEN). Teaches: known words
    give away key letters.
14. Le chiffre indechiffrable. Room 4 opens.
15. Double lock. In Workshop, Keyword-encode a 150+ letter message twice with keys of lengths a and b that share no
    factor, then set the Splitter to a times b (lcm). Teaches: two keys make one longer key, not a new kind of lock.
16. Mirror machine. On Rotors, Run a message, set the rotors back, Run the output: the original returns. Teaches: the
    reflector makes Enigma its own inverse.
17. Never itself. Press one key 26 times on the Rotors keyboard; its own lamp never lights. Teaches: the flaw cribs
    exploit.
18. Bombe. Run the Bombe and leave exactly one setting. Teaches: a machine that tests keys, guided by a guess.
19. The Rotor Room. Room 5 opens.
20. The Last Door. Room 6 opens (the vault is open). Teaches: only the key opens a one-time pad.
21. Stumped. A box made on this device is cracked in Boxes without Peek. Teaches: your cipher was breakable, and how.
22. Out of reach. Seal a Pad box with `Random key`; the meter reads "Cannot be cracked". Teaches: perfect secrecy, and
    its price (a key as long as the message, used once).

## Content

### Rooms (all texts original except the quoted Caesar phrase; ciphertexts computed and checked, see Sources)
Pad: `KMHBZIUPAYIWGLPVOCHRL` (21 letters, random, seed 1794), handed out as pieces KMHBZ, IUPA, YIWG, LPVO, CHRL.

**Room 1, Caesar's Door (Rome, 49 BCE).** Machine: Wheel. Tools: Counter. Shift 3.
- Plaintext: `THE DIE IS CAST. PAD KMHBZ`
- Ciphertext: `WKH GLH LV FDVW. SDG NPKEC`
- Story: "Julius Caesar wrote private letters by shifting each letter three places: D for A, E for B. The historian
  Suetonius described it more than 150 years later. He also reports Caesar saying 'The die is cast' as he crossed the
  Rubicon river in 49 BCE, starting a civil war. There are only 25 real shifts, so anyone can try them all."

**Room 2, The Mason's Stone (New York, 1794).** Machine: Grid (standard pigpen key card). Tools: none needed.
- Plaintext and stone text: `THE GRID IS THE KEY. PAD IUPA`, drawn in pigpen on a painted blank gravestone.
- Pigpen key (the builder draws each symbol as its cell's lines): grid 1 (a 3 by 3 tic-tac-toe) A B C / D E F / G H I;
  grid 2 the same with a dot in each cell: J K L / M N O / P Q R; an X: S top, T left, U right, V bottom; the X with
  dots: W X Y Z in the same places. A grid cell's symbol is the lines that border it (A: right and bottom; E: all four
  sides; I: left and top). An X region's symbol is the V its two lines make (S opens up, T opens left, U opens right,
  V opens down).
- Story: "Freemasons used this grid cipher in the 1700s. James Leeson's gravestone in Trinity Churchyard, New York
  (he died in 1794), carries pigpen that reads 'Remember death'. Pigpen has no key to change: once you know the grid,
  you can read every pigpen message. In 1883 Auguste Kerckhoffs wrote the rule codebreakers still use: assume the
  enemy knows your method; only the key may be secret."

**Room 3, The Queen's Letter (England, 1586).** Machine: Symbols. Tools: Counter.
- Plaintext (296 letters, 24 different letters; J and Z do not appear): `WHEN A QUEEN WRITES IN SECRET SHE TRUSTS HER
  SYMBOLS, BUT EVERY SYMBOL STAYS THE SAME LETTER ALL THE WAY THROUGH. COPY THE LETTER AND COUNT THE SYMBOLS. IN
  ENGLISH THE MOST COMMON LETTER IS E, THEN T, A AND O. LOOK FOR SHORT WORDS NEXT: A ONE LETTER WORD IS A OR I, AND A
  COMMON THREE LETTER WORD IS THE. A CODEBREAKER NEEDS NO KEY WHEN THE MESSAGE IS LONG ENOUGH TO COUNT. PAD YIWG`
- Key, plain letter to glyph number: A18 B24 C14 D11 E10 F7 G19 H2 I6 J17 K20 L1 M23 N22 O9 P21 Q16 R4 S8 T15 U25
  V13 W26 X3 Y5 Z12. Spaces and punctuation are kept (a simplification: real letters of the time ran words together
  and added dummy symbols and code words; the Story says so).
- Glyphs (drawn in code, ink on parchment, 1 to 26): circle; circle with dot; circle with bar; half circle open up;
  half circle open down; triangle up; triangle down; triangle with dot; square; square with X; diamond; diamond with
  dot; plus; X; hooked line; two bars; wave; zigzag; crescent open left; crescent open right; six-line asterisk; arrow
  up; arrow down; figure eight; hourglass; trident.
- The door opens when all 24 used glyphs carry the right letter.
- Story: "Mary, Queen of Scots, was held prisoner in England. Her secret letters used a symbol for each letter, plus
  symbols for whole words. Thomas Phelippes, a codebreaker for Queen Elizabeth's spymaster, counted the symbols and
  read them. The letters were used against Mary at her trial in 1586. Counting letters to break a cipher was first
  described by al-Kindi in Baghdad in the 800s."

**Room 4, The Unbreakable Cipher (1553 to 1863).** Machine: Keyword. Tools: Counter, Splitter, Repeats, Crib. Key
RAVEN (the key advances on letters only).
- Plaintext (259 letters): `FOR THREE HUNDRED YEARS PEOPLE CALLED THIS CIPHER UNBREAKABLE. THE SAME LETTER TURNS
  INTO DIFFERENT LETTERS, SO COUNTING SEEMS USELESS. BUT THE KEY REPEATS. WHEN THE SAME WORDS MEET THE SAME PART OF THE
  KEY, THE SAME LETTERS COME OUT AGAIN. MEASURE THE GAPS BETWEEN THE REPEATS AND THE LENGTH OF THE KEY APPEARS. PAD
  LPVO`
- Ciphertext: `WOM XUIEZ LHEDMIQ PEVVF GEJTYV CVPYVD OLVJ CDTUVR PROIEVONSLZ. XUV SVQR CEOXRI TPVAJ IIXB
  UIAJRIEIX YVTOIEJ, SJ GBLNOMAX SZIZJ UNIYVSN. FHK TCI XVY MICVAOW. JYEI XUV SVQR NOMHF DEZX GYE NEZV PVVG FF OLR BET,
  XUV SVQR CEOXRIS XSZV OPX NXADR. ZVANYEV TCI TRPN FRKWZIA KHZ VRGEVXF RNY XUV LZRTKH JJ GYE FIL RPKINIS. KEQ CPQS`
- The door opens when the Keyword key reads RAVEN and Decode is on.
- Story: "Giovan Battista Bellaso published this keyword cipher in 1553; it was later named after Blaise de Vigenere.
  People called it le chiffre indechiffrable, the unbreakable cipher. Confederate officers used it in the Civil War.
  Charles Babbage broke it in the 1850s but never published; Friedrich Kasiski published the method in 1863: find
  repeats, measure the gaps, and the key length appears."

**Room 5, The Rotor Room (1932 to 1945).** Machine: Rotors, set to order I, II, III, reflector B, ring settings A, no
plugboard. The start setting is the secret (17,576 possibilities in this room). Tools: Crib, Bombe.
- Plaintext: `KEEPER HERE. WEATHER REPORT: FOG AT DAWN, CLEAR BY NOON. PAD CHRL`
- Ciphertext: `QMMHJG ADQC. RRGDCIY YTIVMC: WIL NI YSJY, ZWUYH XJ UYJY. XXL PRJK` (start setting B O X;
  after the 50 letters the windows read B P V).
- The clue on the wall: "The keeper's notes always say WEATHER REPORT near the start." The Crib starts loaded with
  `WEATHERREPORT`. The door opens when the rotors are set to B O X and `Run` turns the ciphertext into the plaintext.
- Story: "The German military Enigma scrambled each letter through three turning rotors, so the same key press gave a
  different letter every time. Marian Rejewski of the Polish Cipher Bureau broke it in 1932. Alan Turing and Gordon
  Welchman designed the British bombe, first run at Bletchley Park in 1940. It tested settings against a crib, a
  guessed word such as the German for weather report. Enigma never turns a letter into itself, which tells you where a
  crib cannot sit. This machine is simplified: the real one also had a plugboard and ring settings, which multiplied the
  keys enormously."

**Room 6, The Last Door (1917 to now).** Machine: Pad. Tools: all breaking tools (they find nothing).
- Ciphertext: `XADHN ANJMN GKACE VFVUV C` (21 letters). Rule: cipher = plain + key, letter by letter, A=0 to Z=25, wrap
  past Z.
- Pad: the five pieces from rooms 1 to 5 in order. The door opens when the student drags the pad strip onto the
  ciphertext: `NOW GO STUMP YOUR PARTNER`, and the vault's back wall opens onto Workshop (a button `Go to Workshop`).
- Before the pad is applied, the panel shows why no tool works: "This ciphertext fits every 21-letter message. With key
  ETZFNHVYIJRSMPSXEHGLK it says THE CAT SLEEPS ON MY BOOKS; with key ETZMNGCQEVCYLJGPROGJY it says THE VAULT IS EMPTY GO
  HOME." (both computed).
- Story, then the epilogue card: "Gilbert Vernam and Joseph Mauborgne built the one-time pad around 1917 to 1918. In
  1949 Claude Shannon proved it cannot be broken, if the key is random, as long as the message, and never used again.
  That is also its problem: you must deliver a huge secret key before every message. Modern encryption such as AES
  (a US standard since 2001) uses a short key, 128 bits or more, and math that leaks no pattern of English. Public-key
  math, published in 1976, lets two people agree on a key in the open."

### Key counts (the Key count card)
Wheel 25 real shifts, cracked by trying all. Grid: no key. Symbols: 26! = about 4 x 10^26 keys, cracked by counting.
Keyword of length n: 26^n (RAVEN: 11,881,376), cracked by splitting and counting. Rotors here: 17,576 starts times 6
orders = 105,456; the real army Enigma, with its plugboard, had about 1.6 x 10^20 settings per day key (Sources), and
was cracked by cribs and bombes. Pad: one key for every possible message, never cracked. AES-128: 2^128, about
3.4 x 10^38. Line under it: "A big number is not enough. Every cracked cipher here leaked a pattern."

### Crack meter (the seal card; rules from the Python checks in Sources)
- Wheel: "Crackable. Only 25 shifts: your partner can try them all."
- Grid: "Readable. Pigpen has no key: anyone who knows the grid reads it."
- Symbols, by letters n: under 50 "Too short to count. Many messages fit (SEND HELP NOW has 1,634 look-alikes in a
  400-word list)."; 50 to 149 "Partly crackable. Counting gets the big letters; word shapes might do the rest.";
  150 or more "Crackable. Long enough to count."
- Keyword, by letters per column (n divided by key length): under 10 "Hard to crack with these tools: too few letters in
  each column."; 10 to 29 "Partly crackable."; 30 or more "Crackable: split by the key length, then count each column."
  Key as long as the message or longer: "This is a running key. If the key is real words it can still be attacked; for
  a true pad use Pad with Random key."
- Rotors: "Crackable with a guess. If your partner guesses a word of 6 or more letters in it, the Bombe finds your
  setting among 105,456. Without a good guess, it is very hard here."
- Pad with `Random key` and key at least as long: "Cannot be cracked, as long as you never use this key again." Pad
  with a typed key: the running-key line above.
- Extra line for Symbols when the message has no E and 100+ letters: "No E! The counter's first guess will be wrong."

### Kerckhoffs
Boxes always show the machine name. The panel line: "Your partner knows the machine. Only the key is secret. That is
Kerckhoffs's rule, and every real cipher is designed for it."

## Interactions in detail
- Wheel: drag the inner ring (pointer angle, snaps to notches; arrow keys or `-` and `+` buttons step one notch). The
  shift readout says "Shift 3: A becomes D". Encode reads inner to outer; Decode outer to inner. The output re-renders on
  every notch within the same frame.
- Grid: tap a symbol in a pigpen text to light its cell; in Workshop, Encode draws pigpen symbols in the output strip;
  Decode takes pigpen typed with an on-screen symbol pad (26 buttons in the key card).
- Symbols: tap a glyph (in the text or in the Counter), then tap a letter in the A to Z strip (or drag the letter onto
  the glyph). Every copy of that glyph fills at once in amber; a letter already used elsewhere moves (the old glyph
  clears). `Clear` empties all. In Room 3 there is no right/wrong marking until the door opens: the text is the check.
  In Workshop, Symbols encodes with a scrambled key (`New key` shuffles; the key card shows it).
- Counter: bars for each letter or glyph in the text, `A-Z` or `Sorted` view, count labels, and a ghost of English
  (Norvig percentages scaled to the text length) that the student can drag sideways in A-Z view; the ghost's offset is
  shown as "Ghost shifted by 3". Recomputes on every change. Under 20 letters it shows "Too few letters to read the
  bars."
- Splitter: length stepper 1 to 12. Shows the text in that many colored columns, a bumpiness score per length
  (index of coincidence times 100: English text about 6.6, random letters about 3.8) as a small bar chart over lengths
  1 to 12, and per column a mini Counter with its own draggable ghost; the ghost offset becomes that column's key
  letter, and the letters assemble into a "Key guess" the student can send to the Keyword machine (`Use key`).
- Repeats: highlights every 3-letter group that appears more than once, lists the gaps between consecutive
  appearances, and a factor row 2 to 10 with how many gaps each divides. Tap a factor to send it to the Splitter.
- Crib: type a guessed word (up to 20 letters), slide it along the ciphertext (drag or arrows). With Rotors, positions
  where any crib letter sits on the same ciphertext letter turn red and say "Enigma never does this here". With Wheel or
  Keyword, it shows the implied key letters under the crib (ciphertext minus crib).
- Bombe: with Rotors and a crib placed at an allowed spot, `Run bombe` tests every start setting (Vault: the room's
  17,576; Workshop and Boxes: 105,456 across 6 orders) and lists the survivors; tapping one sets the rotors. Animated:
  three painted drums spin, a counter climbs, a click per 1,000 tested; the work runs in chunks of about 4,000 tests per
  frame (under 2 s on a school Chromebook) and any tap during it shows the final result at once. With a crib under 4
  letters it warns "Short guesses leave many settings" and still runs.
- Rotors: three rotor windows with up and down arrows, an order picker (Workshop and Boxes: any order of I, II, III),
  a 26-key keyboard and a 26-lamp lampboard (QWERTZ layout as on Enigma). Each key press steps the rotors first (right
  rotor every press; the middle at the right rotor's turnover, and the middle again on the next press if it sits at its
  own turnover: the real double step), then lights the lamp. `Run` feeds the whole message. `Set back` returns the
  windows to where Run started.
- Pad: key strip under the message; `Random key` fills it to the message length with random letters
  (crypto.getRandomValues). A shorter key repeats and the strip turns orange: "A repeated pad is just a Keyword cipher."
- Sealing: the seal card asks a nickname (up to 12 characters, made up), shows the crack meter for the current machine,
  key and length, then `Seal` (wax stamp sound, box flies to the Boxes shelf). The 13th box asks to delete one first.
- Boxes cracking: the partner's machine output is compared after every change; a match springs the box (chime,
  a gold light, time taken) and the line `boxCracked`.
- Reset: Vault `Reset vault`; Workshop `Clear`; Book `Reset book` (confirm) clears stamps. Storage blocked: everything
  plays, nothing persists, one line in the panel says so.
- Extremes: empty message shows "Type a message." in the strip; 600 letters is the cap (the box stops taking letters and
  says "600 letters is the limit here."); non-letters pass through; a Keyword key of non-letters is ignored with a note.

## Look
Band 6-8 own `:root`: a dark stone vault. `--paper #15171c` (stage night), `--panel #1e2128`, `--ink #efe9dc`
(parchment white), `--muted #a9a294`, accent `--brand #3cc7a2` (verdigris, old bronze gone green), `--brand-ink
#06231b`, `--focus #ffc94a` (lamp amber, also the Enigma lamps and filled Symbols letters). Parchment cards `#efe4cc`
with ink `#2a2118`. Contrast (computed): ink on paper 14.82:1, ink on panel 13.32:1, muted on panel 6.35:1, brand on
paper 8.44:1, brand-ink on brand 7.82:1, amber on panel 10.52:1, parchment ink 12.52:1. Accent distance (CIE76) from
neighbors: phishing-spotter cyan 36.3, molecule-forge 46.8, chore-flowcharts 50.6, model-mechanic 66.3, data-defenders
brass 77.7, capture-the-flag pink 107.7. Each room has its own scene light: Rome warm torch, Stone grey dawn, Queen
candle, Unbreakable lamp green, Rotor cold electric, Last Door gold.

Shine and sound (Web Audio, synthesized): wheel click per notch (short 2 kHz tick); strip snap to English (bright
two-note); bolts (80 Hz thud) and door (low creak then boom); pad piece flying (rising glide); counter bars grow with a
blip per bar; rotor step click; lamp glow with a soft hum; bombe whirr (filtered noise with clicks); wax seal thump; box
spring and chime. Glows: correct-room text flashes warm white; lamps bloom amber; the bumpiness bar at the right length
glows verdigris. Budget: texts up to 600 letters, the bombe chunked as above, at most 40 animated glyph fills per frame;
all at 60 fps on a school Chromebook. Motion off: no swings or spins, results appear at once, sounds unchanged.

## Art
Local FLUX, no people, blank surfaces where code draws text. 30 images.
- room-rome: torch-lit Roman stone doorway with a blank stone lintel and heavy oak door, warm light; 16:10; no; scene.
- room-stone: misty old churchyard at dawn, iron fence, trees, empty center for a gravestone; 16:10; no; scene.
- room-queen: candle-lit castle chamber, writing desk, tapestry, window bars; 16:10; no; scene.
- room-unbreakable: 1800s study with brass lamp, green glass shade, bookshelves, a slate board with a blank surface;
  16:10; no; scene.
- room-rotor: 1940s wooden hut interior, blackout curtains, bare bulb, long table; 16:10; no; scene.
- room-last: round vault chamber, gold light, polished steel walls, a blank steel plate in the center; 16:10; no; scene.
- workshop-bench: cozy codebreaker's workbench with tools, lamps and paper scraps seen from above, blank center; 16:10;
  no; Workshop backdrop.
- boxes-shelf: wooden shelf wall with empty shelves, warm light; 16:10; no; Boxes backdrop.
- door-closed and door-open: iron-banded oak vault door, front view, closed / swung inward; 3:4; cutouts; room doors.
- bolt: thick iron door bolt with bracket; 4:1; cutout; slides on the door.
- wheel-outer and wheel-inner: polished brass disc ring with a blank engraved band, top view; 1:1; cutouts; Wheel (letters
  drawn in code on the band).
- gravestone: weathered grey slate gravestone with blank smooth face, rounded top; 3:4; cutout; Room 2.
- parchment: aged parchment sheet, blank, soft edges; 4:3; cutout; Room 3 letter and Story cards.
- wax-seal: red wax seal with a plain round impression; 1:1; cutout; sealing and Book stamps.
- slate: dark slate tablet with a wooden frame, blank; 16:10; cutout; Room 4 ciphertext.
- rotor-machine: wooden box cipher machine with an open lid, blank round key tops and blank lamp windows, top view;
  4:3; cutout; Rotors (keys, lamps and letters drawn in code over it).
- rotor-wheel: single brass-and-black rotor wheel with a blank rim, side view; 1:1; cutout; spins in the windows.
- bombe-drum: one colored drum of an electromechanical code machine, front face, blank; 1:1; cutout; three spin.
- steel-plate: brushed steel plate with rivets, blank; 4:1; cutout; Room 6 ciphertext and pad slot.
- pad-strip: long paper tape strip, blank; 5:1; cutout; the pad strip.
- box-closed and box-open: small iron-bound wooden strongbox with a blank tag, closed / lid open with gold glow; 1:1;
  cutouts; Boxes shelf.
- padlock: old iron padlock; 1:1; cutout; dark doors.
- torch, candle, desk-lamp: one wall torch, one candlestick, one green-shade lamp, each lit; 9:16; cutouts; flicker on
  their rooms.
- book-cover: leather-bound book with brass corners, blank cover; 3:4; cutout; Book button and Book page backdrop.
- key-ring: iron key ring with three old keys; 1:1; cutout; Key count card icon.
- lantern: old brass lantern, lit; 1:1; cutout; the keeper's mark beside spoken hints.

## Voice
Bank voice `gravel-ranger` (Algenib), style "Say warmly with a gravelly voice, like an old park ranger telling
stories": the old vault keeper. Not used by any neighbor (phishing-spotter lively-host, data-defenders hero-coach,
capture-the-flag hs-narrator, molecule-forge knowing-guide, packet-race firm-captain, internet-journey smooth-narrator).
`Curio.voice`, `scope: () => state.mode + ':' + state.room`, `welcomeAfter: true` in Vault. Every waiting line names the
action and the control, never a disabled one.
- wVault (how; first entry to Room 1; stale once the door opens): "Welcome to the vault. Drag the inner ring of the
  wheel until the words make sense."
- r1Open (event; Room 1 opens): "The die is cast. Caesar said that at the Rubicon. Tap the next door."
- r2 (how; Room 2 entered; stale when it opens): "Tap a shape on the stone. The grid card shows its letter."
- r2Open (event): "Once you know the grid, there is nothing left to crack. On to the next door."
- r3 (how; Room 3 entered; stale after the first assignment): "Tap Counter to see which symbol comes up most. Then tap
  a symbol and tap a letter."
- r3Words (how; after 3 assignments; stale when the door opens): "Look at the short words. A one-symbol word is A or I."
- r3Open (event): "She trusted her symbols. Counting beat them."
- r4 (how; Room 4 entered; stale when Repeats is opened): "The bars look flat. Tap Repeats to find letters that come
  back."
- r4Split (how; after a factor is tapped; stale when the door opens): "Now split by that length. Drag each column's ghost
  until the bumps line up."
- r4Open (event): "Three hundred years unbroken, and the gaps gave it away."
- r5 (how; Room 5 entered; stale when the Bombe runs): "Slide the guessed word along the message. Red spots are
  impossible. Then tap Run bombe."
- bombeOne (event; a bombe leaves one setting): "One setting left. Tap it, then tap Run."
- bombeNone (event; zero survivors): "Nothing fits there. Slide the guess and try again."
- r5Open (event): "Enigma never turned a letter into itself. That was enough."
- r6 (how; Room 6 entered; stale when the pad is applied): "Try any tool you like. Then drag the pad strip onto the
  message."
- r6Open (event): "Now go stump your partner. The workshop is open."
- wWorkshop (how; Workshop first entered): "Pick a machine, type a message, and watch it change."
- sealHow (how; first time the seal card opens): "Read the crack meter, then tap Seal."
- sealed (event): "Sealed. Hand the laptop to your partner."
- wBoxes (how; Boxes entered with at least one box; not queued when the shelf is empty): "Tap a box. Work the machine
  until the box springs open."
- boxCracked (event): "Cracked it. Show the maker how."
- goalDone (event): "Stamp in the book."
- lockedDoor (event; tap on a dark door): "That door opens after the one that's glowing."

## Family engine
none (catalog family "none"). Cipher math is the tool's own; it may inline `kit:security` only for `Sec.caesar` and
`Sec.vigenere`, which match this spec's rules (letters only, case kept, key advances on letters only). Do not use the
security family's renderers.

## Sources
History
- Caesar's shift of three (D for A) and "The die is cast" at the Rubicon: Suetonius, Life of Julius Caesar 56 and 32,
  Loeb translation, https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Suetonius/12Caesars/Julius*.html (fetched
  2026-10-29). Rubicon crossing 49 BCE: Britannica, "Rubicon".
- Pigpen used by Freemasons in the 1700s; Leeson's stone (died 1794, Trinity Churchyard) reads "Remember death": Atlas
  Obscura, "Trinity Churchyard", https://www.atlasobscura.com/places/trinity-churchyard; Untapped Cities, 2021-10-22.
- Kerckhoffs's principle (1883): A. Kerckhoffs, "La cryptographie militaire", Journal des sciences militaires IX (1883).
- Mary, Queen of Scots, Phelippes, trial 1586: S. Singh, The Code Book (1999), ch. 1; The National Archives (UK),
  "Mary Queen of Scots" education pages.
- Al-Kindi's frequency analysis, 800s: I. A. Al-Kadi, "Origins of cryptology: the Arab contributions", Cryptologia
  16(2), 1992.
- Bellaso 1553, Vigenere misattribution, Babbage 1850s unpublished, Kasiski 1863: Wikipedia "Vigenere cipher" and
  historyofinformation.com id 1678 (search 2026-10-29); D. Kahn, The Codebreakers (1967), ch. 6-7, also for Confederate
  use.
- Enigma I wirings (I EKMFLGDQVZNTOWYHXUSPAIBRCJ turnover Q; II AJDKSIRUXBLHWTMCQGZNPYFVOE turnover E; III
  BDFHJLCPRTXVZNYEIWGAKMUSQO turnover V; UKW-B YRUHQSLDPXNGOKMIEBFZCWVJAT): Crypto Museum,
  https://www.cryptomuseum.com/crypto/enigma/wiring.htm (fetched 2026-10-29). Rejewski 1932, bombe 1940, cribs, no
  self-encryption, about 1.6 x 10^20 daily settings with plugboard: Bletchley Park, https://bletchleypark.org.uk/ and
  Singh (1999) ch. 4; recheck the 1.6 x 10^20 figure at build.
- One-time pad (Vernam, Mauborgne 1917-18), Shannon 1949: C. Shannon, "Communication Theory of Secrecy Systems", Bell
  System Technical Journal 28 (1949); Kahn ch. 13. AES 2001, 128-bit keys: NIST FIPS 197. Public key 1976: Diffie and
  Hellman, "New Directions in Cryptography", IEEE Trans. Inf. Theory 22(6).
- English letter frequencies (Counter ghost): P. Norvig, "English Letter Frequency Counts: Mayzner Revisited",
  https://norvig.com/mayzner.html (fetched 2026-10-29): E 12.49, T 9.28, A 8.04, O 7.64, I 7.57, N 7.23, S 6.51, R 6.28,
  H 5.05, L 4.07, D 3.82, C 3.34, U 2.73, M 2.51, F 2.40, P 2.14, G 1.87, W 1.68, Y 1.66, B 1.48, V 1.05, K 0.54,
  X 0.23, J 0.16, Q 0.12, Z 0.09.
Checks run (Python 3, scratch scripts, 2026-10-29)
- Round trips: all five room ciphertexts decrypt to their plaintexts with the stated keys; the pad room decrypts.
  Enigma implementation matches the standard test vector (I-II-III, B, AAA: AAAAA gives BDZGO) and the double step
  (from ADU: ADV, AEW, BFX).
- Room 1: of 26 shifts, a quadgram English score ranks shift 3 first.
- Room 3: an automatic hill-climbing solver (quadgrams plus word scores, model built from 1.2 million letters of English
  docstrings) recovers 100 percent of the letters in 3 of 3 runs at 296 letters. Counting alone (rank match to English)
  gets only E, G and T right (28 percent of letters), so word shapes are needed: the room's hint ladder matches.
- Substitution length sweep (5 original texts, 2 keys each): cracked (90 percent of letters) 0 of 10 at 30 and 50
  letters, 3 of 10 at 75, 5 of 10 at 100, 9 of 10 at 150 and 200. At 30 letters, 4 of 10 ciphertexts had another
  decoding the model liked better (ambiguous). Short-message worst case: from a 400-word list, MEET AT TEN has 23
  same-pattern look-alikes (KEEP UP PEN), SEND HELP NOW 1,634. Source of the meter thresholds 50 and 150.
- Room 4: 3-letter repeats give 23 gaps; 5 divides 20, 2 divides 10, 10 divides 8, no other factor more than 7.
  Bumpiness by length 1-8: 4.7, 4.7, 4.6, 4.7, 8.8, 4.5, 5.0, 4.5. Chi-square per column at length 5 gives RAVEN.
  Crib THE SAME at letters 54, 134, 169 shows ENRAVEN.
- Keyword sweep (200 random keys of length 3-7 per row): whole key right with 10 letters per column 22 percent, 15: 53,
  20: 78, 30: 94, 40: 100; key length found by the splitter at 40 letters 53 percent, 80: 82, 120: 90, 200: 96.
  Source of the meter thresholds 10 and 30.
- Room 5: 27 of 38 crib positions survive the no-self-encryption rule; the bombe over 17,576 starts at all 27 leaves
  only B O X at position 11. Crib length at the true spot: 2 letters leave 339 settings over 12 positions, 3 leave 10,
  4 leave 1; over 6 orders a 4-letter crib at 3 wrong spots still left 1 false setting, so the meter asks for 6+.
  300 random settings, 18,000 letters: 0 self-encryptions, all reciprocal.
- Room 6: the 21-letter ciphertext has keys giving THE CAT SLEEPS ON MY BOOKS and THE VAULT IS EMPTY GO HOME (keys
  above, verified by decryption).
- Combinations (all True): Caesar 3 then 5 equals Caesar 8; ROT13 twice is no change; Keyword K equals Caesar 10;
  key ABAB equals AB; key A changes nothing; RAVEN then CAT equals one key of length 15 (splitter bumpiness 7.8 at 15,
  under 4.6 elsewhere from 1 to 16); a Caesar shift keeps the sorted bar heights; Enigma typing A 26 times at B O X
  gives IBSXPIHNTUVGGHIFQTGZXLGYQC (never A); a 192-letter text with no E has A, S, I as its top three letters and the
  solver got only 57 percent of it.
- Contrast and accent distances: computed (Look).

## Done when
1. First minute with no reading: dragging the wheel re-decodes Room 1 every notch and shift 3 opens the door with the
   clunk, swing and the pad piece flying; the map then shows door 2 glowing.
2. All six rooms open by their stated settings and only by them; Room 3 opens only with all 24 used glyphs right; Room
   5's crib marks exactly 27 allowed spots and the bombe leaves only B O X; Room 6 decodes to NOW GO STUMP YOUR PARTNER.
3. Every number in Sources' checks shows up in the tool where it is claimed (bumpiness 8.8 at 5; 20 of 23 gaps; Key
   count values; the two other pad keys); the Enigma test vector AAAAA to BDZGO holds in the built Rotors.
4. All 6 surprising combinations listed in Goals 6, 15, 16, 17 and the no-E and pad lines can be produced by play.
5. Focus: in every mode the machine and its strip are the largest thing on stage at 1366x768 and in the 680x425 preview;
   main controls visible without scrolling at every STANDARDS size.
6. A tap during the bombe, a door swing or a pad drag shows the end state in the same frame; mode buttons work mid-run.
7. Boxes: seal, swap seats, crack, see the time; Peek and Delete confirm; 12-box cap; boxes, stamps and vault progress
   survive a reload; storage blocked still plays.
8. Voice: how lines once per load, event lines every time; no line names a disabled control; Read speaks the hint.
9. 600-letter text in Workshop with the Counter, Splitter and Repeats open holds 60 fps at 4x CPU slowdown; the bombe's
   105,456 tests finish under 2 s; console clean, no network, no em dashes, no people in any image.
10. Ten-minute check: a fresh player with no instructions is still choosing to play after 10 minutes, and can name one
    thing they figured out.

## Teacher note
Three ways to use it in a period: free play (open as many doors as you can, then tell a partner which tool cracked
which door and why); a goal set (goals 6, 11, 12 and 13: "why does splitting the Vigenere text make counting work
again?"); a room challenge (pairs seal a box for another pair, and the class compares crack meters: who made the
hardest one that still fits the rules, and what did it cost?). Reaches MS-SYS-SE-32 and MS-SYS-SE-33 (2017: 2-NI-06,
apply multiple methods of encryption to model secure transmission). No worksheets.

## Open questions
- Room 3's Story says Mary's letters were used at her trial in 1586 (she was executed in 1587, not said on screen).
  Right level for grade 5, or soften to "her secret plans were read"?
- Room 2 quotes the Leeson gravestone's "Remember death". Keep it for grades 5 to 12, or drop the reading and keep only
  "a Mason's gravestone in New York carries pigpen"?
- Doors open in order (the escape chain), with `Open all doors` behind a confirm for teachers. Or should all six doors
  be open from the start?

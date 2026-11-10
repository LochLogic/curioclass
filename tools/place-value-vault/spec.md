# Place Value Vault

## One idea
A bank vault has five locks and a raccoon guard named Penny, and each lock opens with a three-digit code given as a place-value clue, so the child reads the clue and turns three big dials (hundreds, tens, ones) while a tray of base-ten blocks shows what the dials say; the bundle lock snaps ten tens into a flat and asks how many hundreds now; the word lock gives "four hundred six" or 300 + 50 + 8; the skip-count lock clicks the dial by 5s, 10s or 100s to a target (count by 10s from 340 to 400); the compare lock asks for the bigger code (608 or 680) and the sign; in the trick lock the clue is scrambled ("7 tens, 2 hundreds, 0 ones") and the child must set 270, not 720, as the dials make the order plain; an alarm can tick softly but is off by default, and the vault opens on a prize room of silly treasures, so a second grader learns that the three digits of a three-digit number stand for hundreds, tens and ones, that 100 is ten tens, to count within 1000 and skip-count by 5s, 10s and 100s, to read and write numbers to 1000 as numerals, number names and expanded form, and to compare two three-digit numbers with >, = and <.

## Not like
- crayon-boxes (1, spec): tens and ones, same family. Here hundreds.
- stadium-count (4, concept): numbers to a million. Here to 1000.
- jump-line (2, spec): adding and subtracting to 1000. Here reading, writing and comparing.
- bead-slider (1, spec): sliding tens and ones to 100. Here three-digit codes.

## Who and how
- Grade 2, Math, module "Hundreds, Tens and Ones". Standards: 2.NBT.1 (understand that the three digits of a three-digit number represent amounts of hundreds, tens, and ones; e.g., 706 equals 7 hundreds, 0 tens, and 6 ones; understand the following as special cases: (a) 100 can be thought of as a bundle of ten tens, called a "hundred"; (b) the numbers 100, 200, 300, 400, 500, 600, 700, 800, 900 refer to one, two, three, four, five, six, seven, eight, or nine hundreds (and 0 tens and 0 ones)), 2.NBT.2 (count within 1000; skip-count by 5s, 10s, and 100s), 2.NBT.3 (read and write numbers to 1000 using base-ten numerals, number names, and expanded form), 2.NBT.4 (compare two three-digit numbers based on meanings of the hundreds, tens, and ones digits, using >, =, and < symbols to record the results of comparisons).
- Format: escape. Driver: one student (tool.json `driver: "student"`). Every card is spoken. Controls 56 px or more.
- Three vaults of five locks (bundle, word, skip-count, compare, trick), the dials, the block tray, the soft alarm switch. Extra: Team heist (teams race the soft alarm on a projector). tool.json `modes: ["Vault", "Team heist"]`, `minutes: "15-20"`, `grades_label: "Grade 2"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 2.NBT.1 | Bundle tens into a hundred; set scrambled clues | the flat snapping; the dials in order | 2 |
| 2.NBT.2, 2.NBT.3 | Skip-count the dial; turn words and expanded form into digits | dial clicks; the code | 3 |
| 2.NBT.4 | Pick the bigger code and the sign | the block trays side by side | 4 |

## Screens and modes
Header (kit): title "Place Value Vault"; `Vault`, `Team heist`; `Read`, `Motion`, `Sound`, `Print`; an `Alarm` switch (off first). Controls 56 px or more.

**On load and first tap.** A round steel vault door with five locks, Penny the raccoon in a guard cap, three big dials and a block tray. The welcome is queued (`welcomeAfter: true`): "Hi, I'm Penny. I guard the vault, but I'll tell you a secret. Each lock needs a code. Read the clue, then turn the dials. Tap the first lock." First hint: "Tap the first lock."

**A lock (focus: the dials).** At 1366x768 the vault is center with dials below and the block tray at the right; at 680x425 the tray folds under the dials. Each dial has a plus and minus button and can be dragged. The tray shows flats, rods and units for the dials. `Try code` checks.

**Lock types.** Bundle: ten rods sit loose; the child drags them together and they snap into a flat. "How many hundreds now?" Word: "four hundred six" or 300 + 50 + 8. Skip-count: the dial clicks by 10s from 340 to 400, saying each number. Compare: two codes (608 and 680); the child picks the bigger and the sign.

**The trick lock (the aha).** "7 tens, 2 hundreds, 0 ones." Many children set 720. The tray shows 2 flats and 7 rods: 270. Penny: "The dials keep the order. Hundreds first, whatever order the clue says!"

**The prize room.** The door swings open on silly treasures (a golden sock, a giant acorn).

**The end.** A list of every code cracked with its clue. `Print` prints a clue sheet.

**Team heist (extra).** Teams take turns at the dials; the soft alarm can tick.

## Content
- Fifteen locks across three vaults, codes 100 to 999, clues in digits, words, expanded form and scrambled order, all spoken. No one steals; Penny invites the child in.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Dials can be changed until `Try code`.
- Keyboard: Tab to each dial, the tray and buttons; arrows turn a dial; Enter tries the code.
- With Motion off the door opens without swinging and the flat appears snapped.

## Look
- Accent `--brand` #3b3f8f vault indigo (header, dials, buttons); gold #f4c542 (the open lock, the flat snapping); paper #f2f2fa; ink #11122c; muted #51526a.
- Contrast (WCAG 2.1, computed): white on brand 9.16:1; brand on paper 8.22:1; ink on paper 16.44:1; muted on paper 6.82:1; ink on gold 11.26:1.
- Never color alone: dials are labeled hundreds, tens and ones.
- Different from this batch (closet blue, gym red, park green, court orange).

## Art
- Local FLUX (`scripts/localart.py`): the vault door (1, 16:9), the prize room (1, 16:9), Penny in three poses (wave, think, cheer) (3, 1:1).
- Drawn in code: dials, base-ten blocks, clue cards, signs.
About 5 images.

## Voice
Two bank voices, each unique in this batch: `big-sister` as Penny; `clear-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.vault + ':' + state.lock + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `dial`: "Turn the dials to match the clue."
- how `bundle`: "Drag ten rods together."
- how `skip`: "Tap plus to click the dial."
- how `compare`: "Tap the bigger code, then the sign."
- event, whole, each lock opening (short).
- event, whole, the trick lock.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
base-ten (family "base-ten"). Uses the shared pieces from the marked block `/* BASE-TEN ENGINE: begin */ ... /* end */` as described in crayon-boxes' spec, adding hundreds (flats) to the bundles. Tool-only code: dials, locks, clue cards.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Code | Spin dials at random | `Try code` shows what the dials make in blocks beside the clue. |
| Trick | Copy the clue's order | The tray shows 720 is not 7 tens. |
| Compare | Guess the sign | The trays line up hundreds first. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `dial`.
2. `bundle`; `skip`.
3. `compare`.
4. Trick lock (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 2.NBT.1 to 2.NBT.4 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| 100 as ten tens and three-digit place value in grade 2 | Common Core Standards Writing Team (2015), "Progressions for the CCSS, K-5 Number and Operations in Base Ten" | Fuson (1990), "Conceptual structures for multiunit numbers", Cognition and Instruction | yes |
| Children often write numbers in the order the parts are said, so scrambled clues test real understanding | Common Core Standards Writing Team (2015), "Progressions for the CCSS, K-5 Number and Operations in Base Ten" | National Research Council (2001), "Adding It Up" | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad r9, 2026-11-10): 2 hundreds, 7 tens and 0 ones is 270; four hundred six is 406; 300 + 50 + 8 = 358; 340 to 400 by 10s is 6 clicks; 680 beats 608; ten tens make 100; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 vault, dials and tray; at 680x425 tray under dials.
2. Bundle and trick locks show hundreds, tens and ones. (2.NBT.1)
3. Skip-count and word locks are cracked. (2.NBT.2, 2.NBT.3)
4. Compare locks use >, = and <. (2.NBT.4)
5. Every card is spoken; every control is 56 px or more.
6. The alarm is off by default; nothing is stolen.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: jumps; no network requests.

## Open questions
None.

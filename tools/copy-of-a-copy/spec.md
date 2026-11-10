# Copy of a Copy

## One idea
A message (a short word the student types, or a picked snippet of a song melody) has to cross a valley through five relay towers, and each tower picks up a little static before passing the signal on; the student sends it once as an analog signal (a smooth wave whose height carries the message) and once as a digital signal (the same message turned into 32 on-off pulses, 8 for each of four letters), and watches each tower's screen: the analog wave gets fuzzier at every tower because the tower copies the noise along with the message, so by the fifth tower the static has piled up to about 22 percent and the word comes out garbled or the tune sounds rough, while each digital tower only has to decide "on or off" against a halfway line, rebuilds clean pulses and passes them on, so the message arrives exact; then the student turns up the static until even digital fails, adds a check bit that catches the error, and compares a scratchy record with a streamed song; at the end a claim card holds the student's evidence, so an eighth grader learns that digitized signals are a more reliable way to encode and transmit information than analog signals.

## Not like
- secret-code-signals (4, spec): patterns that carry a message. Here why on-off pulses survive noise.
- wave-tank (8, concept): wave properties. Here waves carrying information.
- nerve-signal-relay (7, spec): signals relayed through the body. Here signals relayed through towers.
- inside-the-keypress (3, concept): a keypress through a computer. Here a message across distance.

## Who and how
- Grade 8, Science, module "Analog and Digital Signals". Standard: MS-PS4-3 (integrate qualitative scientific and technical information to support the claim that digitized signals are a more reliable way to encode and transmit information than analog signals).
- Format: lab. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Five towers, two ways to send (analog, digital), a static dial, a check bit switch, two message types (a four-letter word, a short melody), the record and stream card, the claim card. Extra: Telephone game (the class passes a whispered word and compares it to a digital copy). tool.json `modes: ["Valley", "Telephone game"]`, `minutes: "20-30"`, `grades_label: "Grade 8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-PS4-3 (encode) | Turn a word into a wave and into 32 pulses | the wave; the pulse train; the letter table | 2 |
| MS-PS4-3 (transmit) | Send both through five noisy towers | each tower's screen; the arriving message | 3 |
| MS-PS4-3 (claim) | Raise static, add a check bit, write a claim with evidence | the static dial; the check bit; the claim card | 4 |

## Screens and modes
Header (kit): title "Copy of a Copy"; `Valley`, `Telephone game`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A wide valley at dusk with five radio towers on hilltops, a sender's hut on the left and a receiver's hut on the right. A message box says "MOON". The welcome is queued (`welcomeAfter: true`): "Get this word across the valley without it changing. Send it as a wave first. Tap Send wave." First hint: "Tap Send wave."

**Sending (focus: the towers).** At 1366x768 the valley spans the top and five tower screens sit in a row below; at 680x425 one tower screen shows at a time with arrows. The wave travels tower to tower; each screen shows what came in and what went out. Static is drawn as small random wiggles. The receiver's hut shows what arrived.

**Analog.** The wave's height carries the letters. Each tower copies it, wiggles and all, and adds more. By tower 5 the wave is about 22 percent off, and the word reads "MOOM" or "NOON".

**Digital.** The student taps `Send pulses`. A letter table shows each letter as 8 on-off pulses (MOON is 32). Each tower measures each pulse against a halfway line and rebuilds it clean. The word arrives "MOON".

**Turn up the static.** A dial raises static. Analog gets worse smoothly; digital stays perfect until the noise crosses the halfway line, then a pulse flips. The student switches on a check bit (an extra pulse that makes the count of ons even) and sees the receiver flag the bad letter and ask for it again.

**Sound.** With a melody, analog sounds hissy at the receiver; digital sounds the same as the start. A card compares a scratchy record copied five times to a song file copied five times.

**The claim card (the aha).** "Digital signals are more reliable because ___. My evidence: ___." Narrator: "A copy of a copy of a wave keeps every mistake. A copy of pulses starts fresh at every step."

**The end.** The five screens for both runs and the claim. `Print` prints them.

**Telephone game (extra).** The class whispers a word down a line and compares it to a digital pass.

## Content
- Letter table (8-bit codes for capital letters), a stated noise model (random noise of a set size added at each tower), the halfway rule, the check bit rule, three melodies, the record and stream card, the claim card.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The message can be any four capital letters.
- Keyboard: Tab to the message box, `Send wave`, `Send pulses`, the dial, the check bit and tower screens; Enter sends.
- With Motion off the signal jumps tower to tower and the static is drawn still.

## Look
- Accent `--brand` #2c4a6e radio navy (header, the clean signal, the towers); gold #f4c542 (the tower in focus, a flipped pulse); paper #f1f4f8; ink #0c1624; muted #4d5664.
- Contrast (WCAG 2.1, computed): white on brand 9.08:1; brand on paper 8.23:1; ink on paper 16.47:1; muted on paper 6.72:1; ink on gold 11.17:1.
- Never color alone: flipped pulses carry an X mark; analog and digital carry labels.
- Different from this batch (orchid, bone tan, safety orange, town green).

## Art
- Local FLUX (`scripts/localart.py`): the valley at dusk with towers (1, 16:9), the record player and phone card (1, 4:3).
- Drawn in code: waves, pulses, tower screens, the letter table, the dial.
About 2 images.

## Voice
Two bank voices, each unique in this batch: `news-reader` as the radio station voice; `clear-teacher` as the engineer and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.send + ':' + state.tower + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `wave`: "Tap Send wave."
- how `pulses`: "Tap Send pulses."
- event, whole, each arrival.
- how `static`: "Turn the static dial up."
- how `check`: "Tap the check bit switch."
- how `claim`: "Fill in the claim card."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the noise model, the halfway rule, the check bit, the screens. Letter codes and melodies sit in a marked block `/* SIGNALS DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Sends | Send only digital | The claim card needs both arrivals. |
| Static | Leave it at zero | The check bit step needs a flipped pulse first. |
| Claim | Say "digital is better" | The card needs evidence from a tower screen. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `wave`.
2. Arrival (whole), waits. `pulses`; arrival (whole), waits.
3. `static`; `check`.
4. `claim`.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for MS-PS4-3 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Analog copies add noise at each step; digital repeaters regenerate the signal | Federal Communications Commission, "Digital television" consumer guide | OpenStax, "College Physics 2e", digital and analog signals | yes |
| Letters coded as 8 bits | Library of Congress, "ASCII" format description | Computer History Museum, "ASCII" | yes |
| A parity bit lets the receiver detect a single flipped bit | National Institute of Standards and Technology, "Dictionary of Algorithms and Data Structures", parity | Computer History Museum, "Error-correcting codes" | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad r4, 2026-11-10): four letters of 8 pulses is 32; five towers each adding noise of 0.1 pile up to about 0.22; noise of 0.1 stays under the halfway line at 0.5; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 valley and five screens; at 680x425 one screen with arrows.
2. A word is turned into a wave and into 32 pulses. (MS-PS4-3)
3. Both signals cross five towers and the arrivals are compared. (MS-PS4-3)
4. Static is raised, a check bit catches an error, and a claim cites a screen. (MS-PS4-3)
5. The noise model is stated on screen.
6. The melody works with Sound off through a waveform picture.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: jumps and still static; no network requests.

## Open questions
- Overlap risk with secret-code-signals (default used: that tool keeps making and reading pattern codes; this tool teaches only why digital signals survive noise better than analog).

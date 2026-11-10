# Secret Code Signals

## One idea
At dusk on a lake two cabins face each other across the water, and the student pushes a wave paddle near the dock and watches a floating buoy bob up and down while the waves travel past it; wave puzzles ask for a wave tall enough to ring the buoy's bell (amplitude), waves spaced to match the dock posts (wavelength), and proof that the buoy only goes up and down while the wave moves on; then a friend in the far cabin sends messages as light flashes, beeps and wave patterns, and the student decodes them with a key, invents their own code (short and long, on and off, a grid of lights) and sends a reply; fog, wind and noise roll in, and the student sends the same message with two or three codes, a table compares how fast each was and how many mistakes got through, and the student picks the best code for each kind of weather; at the end a signal log holds the wave findings and the code comparison, so a fourth grader learns to model waves by their amplitude and wavelength and see that waves can move objects, and to compare solutions that use patterns to send information.

## Not like
- vibration-station (1, spec): building a sound or light maker. Here what waves are and how patterns carry messages.
- how-animals-see (3-5, live): light and eyes. Here light as a signal.
- magnet-maze (3, spec): forces without touching. Here energy and information without touching.
- bowling-lab (4, spec): energy in a collision. Here energy in a wave.

## Who and how
- Grade 4, Science, module "Waves and Information". Standards: 4-PS4-1 (develop a model of waves to describe patterns in terms of amplitude and wavelength and that waves can cause objects to move), 4-PS4-3 (generate and compare multiple solutions that use patterns to transfer information).
- Format: puzzle. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Six wave puzzles, five incoming messages, a code maker with three code types, three weather conditions, the comparison table, the signal log. Extra: Code partner (two students on two devices or one screen send each other messages). tool.json `modes: ["Lake", "Code partner"]`, `minutes: "20-30"`, `grades_label: "Grade 4"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 4-PS4-1 (amplitude, wavelength) | Set push size and speed to make tall or spaced waves | the ruler on the wave | 2 |
| 4-PS4-1 (objects move) | Watch the buoy bob and ring the bell | the buoy's up-and-down path | 2 |
| 4-PS4-3 (decode, invent) | Decode five messages and invent a code | the key; the student's code | 3 |
| 4-PS4-3 (compare) | Send one message with several codes in three weathers and compare | the speed and errors table | 4 |

## Screens and modes
Header (kit): title "Secret Code Signals"; `Lake`, `Code partner`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A lake at dusk, two cabins, a dock with posts, a wave paddle and a buoy with a bell. The welcome is queued (`welcomeAfter: true`): "Push the paddle. Watch the buoy. Tap the paddle." First hint: "Tap the paddle."

**Wave puzzles (focus: the water).** At 1366x768 the lake fills the screen with a control strip below; at 680x425 the strip is a bottom bar. Two controls: push size and push speed. A ruler shows the height from middle to top (amplitude) and the distance from crest to crest (wavelength). Six puzzles: ring the bell (tall enough), match the dock posts (spacing), make small fast waves, make big slow waves, show the buoy stays in place (a trail traces its path straight up and down), and push a toy boat a little with a big wave. A note says the buoy only rocks up and down because the water itself mostly moves in small circles as the wave passes.

**Messages (4-PS4-3).** The friend sends five messages as flashes, beeps or wave patterns, using a key of short and long signals. The student decodes each. Then the code maker: pick a type (short and long; on and off counts; a grid of lights) and build a code for a reply.

**Weather and comparing.** Fog makes faint flashes hard to see, wind makes small waves messy, and boat motors cover beeps. The student sends "MEET AT DOCK" with two or three codes in each weather. A table records time to send and mistakes. The student picks the best code for each weather and says why.

**The signal log (the aha).** Wave findings and the comparison table on one page. Narrator: "Waves carry energy across the water without carrying the water away. And a pattern of signals can carry a whole message across a lake."

**The end.** The log. `Print` prints it with the student's code key.

**Code partner (extra).** Two students send each other messages.

## Content
- Six wave puzzles with a stated wave model, five messages, three code types, International Morse code as one example key, three weathers with stated effects, the table.
- Messages are friendly and short (plans, jokes, a picnic).

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Signals in the code maker are tapped (short tap, long press) or picked from buttons.
- Keyboard: Tab to the paddle, sliders, the key, the code maker and the table; arrow keys set sliders; Space sends a short signal and holding Space a long one; Enter sends.
- With Motion off waves show as a still wave with the ruler, and flashes show as a row of marks.

## Look
- Accent `--brand` #5b2a86 dusk purple (header, the key, the table); gold #f4c542 (a light flash, the chosen code); paper #f5f0fa; ink #1c0c2c; muted #5a5265.
- Contrast (WCAG 2.1, computed): white on brand 9.90:1; brand on paper 8.83:1; ink on paper 16.45:1; muted on paper 6.62:1; ink on gold 11.34:1.
- Never color alone: flashes and beeps also show as dots and dashes; the ruler carries numbers.
- Different from this batch (workshop teal, civic blue, canyon rust, moss green).
- Flashes stay under three per second.

## Art
- Local FLUX (`scripts/localart.py`): the lake at dusk (1, 16:9), the far cabin with a lamp (1, 4:3), fog, wind and a boat (3, 16:9).
- Drawn in code: water waves, the buoy, the ruler, flashes, the key, the code maker, the table.
About 5 images.

## Voice
Two bank voices, each unique in this batch: `casual-peer` as the friend across the lake; `gentle-storyteller` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.puzzle + ':' + state.message + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `wave`: "Move push size or push speed, then tap the paddle."
- event, whole, each puzzle solved.
- how `decode`: "Tap the letter each signal stands for."
- how `invent`: "Pick a code type and build your code."
- how `compare`: "Send the message with each code."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the wave model, the buoy, the decoder, the code maker, the weather noise and table.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Waves | Max out both sliders | The spacing puzzle needs the right wavelength, not the biggest. |
| Decoding | Guess letters | Each letter checks against the key. |
| Compare | Use one code for all weather | The table needs two codes in each weather. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `wave`; puzzle solved (whole), waits.
2. `decode`; `invent`.
3. `compare`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for 4-PS4-1, 4-PS4-3 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Amplitude and wavelength; water moves in small circles as a wave passes, so floating things bob | NOAA Ocean Service, "What is a wave" and Ocean Explorer, "Waves" | The Physics Classroom, "Water waves" | yes |
| International Morse code letters and signal patterns | International Telecommunication Union, Recommendation M.1677 | Smithsonian National Museum of American History, "Telegraph" | yes |
| Fog and noise affect light and sound signals | U.S. Coast Guard Navigation Center, sound and light signals | NOAA National Weather Service, "Fog" | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad r29, 2026-11-09): in International Morse code "SOS" is nine signals and "HI" is six; "MEET AT DOCK" is ten letters; six puzzles, five messages and three weathers; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 lake and strip; at 680x425 bottom bar.
2. Six wave puzzles use amplitude and wavelength and show the buoy moving up and down. (4-PS4-1)
3. Five messages are decoded and a new code is invented. (4-PS4-3)
4. One message is sent with several codes in three weathers and compared. (4-PS4-3)
5. Flashes stay under three per second.
6. Every signal also shows as dots and dashes.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: still waves and marks; no network requests.

## Open questions
None.

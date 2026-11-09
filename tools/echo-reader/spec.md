# Echo Reader

## One idea
In Echo Cave, Echo the bat reads a sentence and the child reads it right back like an echo, and the two readings show up as two sound waves one above the other, so the child can see what reading well looks like: the flat gaps where a voice rests at a period, the voice line that climbs at a question mark, a too-fast reading squashed short, and a second try that lines up better than the first; one sentence in each story is read wrong on purpose (Ben rode his house to the pond), and the picture shows the silly result until the child rereads and fixes it.

## Not like
- poem-drum (k-2, spec): poems read to a beat, with a recording that plays back with instruments. Here prose sentences, echo reading and comparing two waves.
- blend-bakery (1, spec): blending single words from sound jars. Here whole sentences read with pace and expression.
- read-along-shelf (k-2, spec): reading books with help that fades. Here an experiment: one sentence, two readings, compare.
- script-read-through (3-5, concept, same family): parts in a script with a prompter. This tool sets the shared read-aloud engine.
- who-said-that (1, spec): voices played back to find the speaker. Here the child's own voice, measured against a model.

## Who and how
- Grade 1, ELA, module "Reading Fluency" (Foundational Skills). Standard: RF.1.4 (a, b, c).
- Driver: one student at a device with a microphone (tool.json `driver: "student"`); works on a projector for a class demo with the teacher reading. Every sentence is read by Echo first and on tap (BASELINE rule 4).
- Three stories, four experiments each: `Echo`, `Fast and Slow`, `Flat and Feeling`, `Does It Make Sense?`, then `My Best Read`. tool.json `modes: []`, `minutes: "10-15"`, `grades_label: "Grade 1"`.
- Privacy (BASELINE rule 7), shown on screen before the first recording and in the footer: "Your recordings stay on this device and are gone when you close the page. Nothing is sent anywhere, and the computer does not listen for words."

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RF.1.4a | After each story, answer a picture question about what happened | three picture picks | 7 |
| RF.1.4b | Echo each sentence, then compare the two waves: tap the rest gap at the period, see the voice line rise at a question; read too fast and just right; read flat and with feeling | two waves, rest gaps, a voice line, a length bar | 2, 3, 4 |
| RF.1.4b | My Best Read: read the whole story alone, then hear and see the first try and the last try back to back | two whole-story waves | 6 |
| RF.1.4c | Does It Make Sense?: hear a line read wrong, see the silly picture, reread, and tap the word that was wrong to fix it | the picture changes back when fixed | 5 |

## Screens and modes
Header (kit): title "Echo Reader"; `Stories`; `Read`, `Motion`, `Sound`. Controls 60 px or more at 1366x768 (44 px at 680x425), icon plus word.

**On load and first tap.** Echo Cave at dusk with Echo hanging from a ledge and three story stones. First hint: "Tap a story stone to start." The first tap opens the story with its line; the welcome is queued after it (`welcomeAfter: true`). Before the first recording, the privacy card shows with `Got it`, and the browser's microphone prompt follows.

**Echo.** Focus: the story picture (640 x 360) with one sentence under it, word by word lit as Echo reads (the model is a recorded whole-sentence clip with word timings). Below: two wave strips, 900 x 120 each, Echo's on top (violet) and the child's under it (gold, with a dotted outline). `Listen` (Echo reads), `Echo it` (record: a 3, 2, 1 count, then a red ring while recording; it stops at a tap or after the sentence's length plus 3 s), `Play mine`, `Play both` (Echo's then the child's). After each echo, one look-at question with a tap on the wave: "Find where Echo rested at the period" (the gap glows when tapped right) or "See the voice line climb at the question mark?" (the voice line, a thin line over the wave that rises and falls with the voice, is drawn on both strips).

**Fast and Slow.** One sentence, two takes: "Read it super fast!" then "Now just right." A length bar under each wave shows how long each took next to Echo's. Then a conclude pick with pictures: "Which was easier to understand?" (a squashed wave | a just-right wave). No right answer is forced; Echo says what she noticed ("Your fast one was squashed, and the words ran together").

**Flat and Feeling.** "Read it like a robot" then "Read it like Mia feels." The voice line is flat on one and moves on the other; Echo's own robot and feeling reads are there to compare.

**Does It Make Sense?** Echo reads the story with one word wrong; the picture shows that wrong version (a boy riding a little house down a path). "Hmm. Does that make sense?" The child taps `Reread` (Echo reads it again slowly, the wrong word lit), then taps the word and picks the word that makes sense from two pictures (a house | a horse). The picture changes to the right one, and the child echoes the fixed sentence.

**My Best Read.** The whole story on one page; the child reads it alone (one recording). Then `First and last`: the child's first full echo and this read play back to back with both waves stacked. No score.

At 1366x768 the picture, sentence and two waves fit above the fold. At 680x425 the picture is 400 x 225 and waves 600 x 80.

## Content
Three stories, written for Curio Class. Each has 5 sentences mixing a period, a question and an exclamation, and one line read wrong in Does It Make Sense?

**The Lost Mitten:** Mia lost her red mitten. She looked under the bed. Was it in the toy box? "Here it is!" said Dad. It was on the dog's nose! Misread: "She looked under the bread." (picture: Mia peeking under a giant loaf) | fix: bed (pictures: a bed | a loaf of bread). Question: Where was the mitten? (on the dog's nose | under the bed | in the toy box).

**Ben's Ride:** Ben rode his horse to the pond. The horse took a big drink. Then a frog jumped out! "Ribbit!" said the frog. Did the horse jump too? Misread: "Ben rode his house to the pond." (picture: a boy riding a little house) | fix: horse (pictures: a house | a horse). Question: What jumped out? (a frog | a horse | a fish).

**Rain Day:** Drip, drop, the rain came down. Kim put on her boots. She jumped in a big puddle. Splash! Was Kim wet? Misread: "She jumped in a big poodle." (picture: Kim jumping on a surprised poodle) | fix: puddle (pictures: a puddle | a poodle). Question: What did Kim put on? (boots | a hat | mittens).

Echo's model clips: each sentence read three ways (just right, robot, with feeling), plus the whole story and the three misread lines, all recorded as whole sentences with word timings.

## Interactions in detail
- Every tap acts at once; a new line or playback stops the old one. Recording stops any playback.
- Recording: the browser's media recorder, kept in memory only; at most the last two takes per sentence and the first and last whole reads are kept; `Start over` and closing the page drop them. No speech recognition: the tool never checks the child's words.
- Waves: drawn from the audio in the browser. Rest gaps: stretches quieter than a set level for 250 ms or more, marked lightly. Voice line: pitch found by a simple autocorrelation per 30 ms frame between 80 and 600 Hz, drawn only where the voice is steady; where it is not found, the line breaks.
- If the microphone is blocked or missing, the tool says "No microphone? You can still read aloud. Echo will show you her waves." and the child strip shows "Read aloud with Echo" with no wave.
- The look-at questions take a tap within the glowing area; a miss says where to look ("Look for the flat part after 'mitten'").
- The Does It Make Sense? word pick has two pictures; the wrong pick says "Would that make sense? Look at the picture again."

## Look
- Accent `--brand` #4b3f8f dusk violet (header, Echo's wave, frames); gold #f4c542 (the child's wave, the voice line on the child's strip, stars); paper #f7f6fc; ink #1c1830; muted #565070. Scene: a friendly cave at dusk with glow stones.
- Contrast (WCAG 2.1, computed): white on brand 8.73:1; brand on paper 8.12:1; ink on paper 15.98:1; muted on paper 7.04:1; ink on gold 10.56:1.
- Never color alone: Echo's wave is solid and labeled with her picture, the child's has a dotted outline and their star icon; the recording state is a ring plus the word "Recording".
- Different from this batch (teal workshop, brick map, coral sea, olive post office).

## Art
Local FLUX (`scripts/localart.py`); no people in close-up (the three children are drawn as simple young animals: Mia a mouse, Ben a bear cub, Kim a kitten).
- cave (1): "A friendly cave at dusk with glowing stones and a ledge, soft gouache, no text"; 16:9; cutout no.
- Echo (4, hang, listen, read, cheer): "A cute small purple bat <hanging upside down / cupping an ear / holding a little book / cheering>, soft gouache, plain white background"; 1:1; cutout yes.
- story pictures (15: 5 per story): "<Mia the mouse looking for a red mitten / ...>, soft gouache"; 16:9; cutout no.
- misread pictures (3): "a bear cub riding a little house down a path, funny, soft gouache" and the bread and poodle scenes; 16:9; cutout no.
- fix and question picks (12): "<a bed / a loaf of bread / a horse / ...>, simple soft gouache icon, plain white background"; 1:1; cutout yes.
About 35 images. Drawn in code: waves, voice lines, rest gaps, length bars, the recording ring, controls.

## Voice
Bank voice `soft-breath` as Echo, both the guide and the model reader (unique in this batch). `Curio.voice` with `scope: () => state.story + ':' + state.exp + ':' + state.line`, `welcomeAfter: true`.
- event `story`: "{The Lost Mitten}."
- how `welcome`: "Welcome to Echo Cave! I read, then you read it back, like an echo. Then we look at our sound waves."
- how `privacy`: "Your recordings stay right here and go away when you close the page."
- event, whole, `model`: the sentence clip (just right, robot or with feeling).
- how `echoHow`: "Tap Echo it, wait for three, two, one, and read it back."
- event `gotIt`: "I heard you! Look at our waves."
- event, whole, `look`: "Find where I rested at the period. Tap the flat part." / "See my voice line climb at the question mark? Does yours?"
- event `lookYes` / `lookNo`: "Yes! A rest at the period." / "Look for the flat part after {mitten}."
- event, whole, `fastSlow`: "Read it super fast!" then "Now just right." event `noticed`: "Your fast one was squashed, and the words ran together."
- event, whole, `flatFeel`: "Read it like a robot." then "Now read it like {Mia} feels."
- event, whole, `misread`: the misread line. event `sense`: "Hmm. Does that make sense? Look at the picture."
- event `fixYes` / `fixNo`: "Yes! {Horse} makes sense." / "Would that make sense? Look at the picture again."
- event, whole, `ask`: the story question. event `askYes` / `askNo`: "Right!" / "Listen again: {It was on the dog's nose!}"
- event `best`: "Here is your first read, then your last read. Listen to how you grew."
- event `noMic`: "No microphone? You can still read aloud. I'll show you my waves."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
`kit/read-aloud.js` (the read-aloud family). No family doc exists and the only sibling, script-read-through (3-5), is a concept, so this spec describes the engine for both. Pure parts in one marked block, exposed as `__tool.ra`.
- **Passage**: `{id, title, lines:[{id, text, words:[{text, start, end}], clips:{model, robot, feeling}, part?}]}`; word timings are stored, never guessed.
- **Highlight**: `ra.follow(line, clip, onWord)` lights each word on the audio clock.
- **Take**: `ra.record({maxMs, countIn})` records with the media recorder into memory; `ra.takes` keeps a capped list per line; `ra.forget()` on leave. Never uploads, never runs speech recognition.
- **Wave**: `ra.wave(buffer)` gives a downsampled envelope; `ra.rests(buffer, level, ms)` gives quiet spans; `ra.pitch(buffer)` gives a voice line by autocorrelation with gaps where unsteady; `ra.length(buffer)`.
- **Compare**: draws two strips aligned at their first sound, with a shared time scale.
- **Prompter** (script-read-through): scrolls lines by part and plays recorded cast lines for the other parts; not used here.
- **Split**: tap a long word to show syllables and parts from stored data (script-read-through); not used here.
This tool uses Passage, Highlight, Take, Wave, Compare.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Look at the waves | Tap anywhere on the wave | Only the rest gap after the period glows; the gap spans under 10 percent of the strip, so a miss is the usual result and Echo says where to look. |
| Does It Make Sense? | Pick either picture | Two picks, but the picture only changes back on the word that makes sense, and the child must then echo the fixed line. |
| Echo it | Stay silent | Nothing to score is the design: a silent take shows a flat wave, and Echo says "I didn't hear you. Try again, nice and loud." (a take quieter than the rest level throughout). |
| Story question | Tap the first pick | The right pick is first in one of three stories (data order varies: first, second, third). |
Nothing is scored; the tool never claims a child read well, only shows the two waves.

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a story stone: `story`, `welcome` (queued, first time), `privacy` (first recording only).
2. Each sentence: `model` (whole), `echoHow` (first time), the child's take, `gotIt`, `look` (whole), `lookYes` or `lookNo`.
3. Fast and Slow: `fastSlow` (whole), takes, `noticed`. Flat and Feeling: `flatFeel` (whole), takes.
4. Does It Make Sense?: `misread` (whole), `sense`, then `fixYes` or `fixNo`.
5. `ask` (whole), `askYes` or `askNo`; My Best Read: the take, then `best` and the two takes.
No line contains a bare letter or letter sound.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RF.1.4 wording (a purpose and understanding; b accuracy, appropriate rate and expression on successive readings; c context to confirm or self-correct, rereading as necessary) | thecorestandards.org, RF Grade 1 | CCSS ELA 2010 PDF | yes |
| Echo reading: a teacher reads a sentence or passage aloud and the student reads it back right away, as a fluency practice | Brookes Publishing resource library, "Echo Reading" | Decoda Literacy Solutions, "Back to Basics: Echo Reading" | yes |
| Repeated reading improves fluency for beginning readers | National Reading Panel report (2000), Fluency chapter (guided repeated oral reading) | Therrien (2004), "Fluency and comprehension gains as a result of repeated reading", Remedial and Special Education | yes |
| Pitch in speech can be estimated by autocorrelation of short frames | Rabiner, "On the use of autocorrelation analysis for pitch detection" (IEEE, 1977) | Boersma, Praat manual, "Sound: To Pitch (ac)..." | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad b6, 2026-11-08): each story has 5 sentences with a period, a question mark and an exclamation point; each misread differs from its word by one or two letters (bed/bread, horse/house, puddle/poodle); story question right-pick positions 1, 2, 3; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the picture, sentence and both wave strips show with no scroll; at 680x425 the same, smaller.
2. Echo: a take records after the count, stops on tap or at the cap, and shows under Echo's wave on the same time scale. (RF.1.4b)
3. Rest gaps and voice line: on a test clip with a 400 ms pause after a period and a rising question, the gap is marked and the voice line rises at the end. (RF.1.4b)
4. Fast and Slow and Flat and Feeling: both takes show with length bars and voice lines next to Echo's. (RF.1.4b)
5. Does It Make Sense?: the silly picture shows on the misread, the right word changes it back, and the wrong pick leaves it. (RF.1.4c)
6. My Best Read: the first and last whole reads play back to back with both waves stacked. (RF.1.4b)
7. Each story question takes only its right picture. (RF.1.4a)
8. Privacy: the privacy card shows before the first recording; no network requests at any time; reloading the page leaves no recordings.
9. No microphone: blocked or missing mic gives the `noMic` line and the tool still runs with Echo's waves only.
10. Tap while it plays: any tap during a line or playback acts at once; no older line plays after a newer one.
11. Motion off: no swooping bat; waves draw at once.

## Open questions
- None for Cory.

# First, Next, Last

## One idea
Robo the robot does exactly what the writing says and nothing more, so the class writes for Robo: a how-to with a missing step makes Robo spread jam on the table, a story with no ending makes Robo ask "And then? And then?" until there is one, and an opinion with no reason gets "Why?" until there is a reason that fits; when the piece is whole, Robo reads it back as one short paragraph and does it right.

## Not like
- sentence-train (k, spec, same family): one sentence built from word cars. Here several sentences in order, with sequence words, a topic and a closing.
- my-story-strip (k, spec): drawing and telling a three-panel strip. Here writing a how-to, a story or an opinion from sentence cards, tested by a literal robot.
- story-map-treasure (1, spec): retelling someone else's story on a map. Here writing your own.
- because-bridge (k-2, spec): joining a claim to a reason in a text. Here writing an opinion whose reason must fit.
- echo-reader (1, spec): reading aloud. Here writing.

## Who and how
- Grade 1, ELA, module "Writing Sentences and Stories" (Writing). Standards: W.1.1, W.1.2, W.1.3.
- Driver: a pair at one device or the teacher on a projector (tool.json `driver: "either"`). Every card is read on tap and has a picture, so a pre-reader can build (BASELINE rule 4).
- Three jobs from the workshop door: `How-To` (two topics), `Story` (two topics), `Opinion` (pick a pet). tool.json `modes: []`, `minutes: "15-20"`, `grades_label: "Grade 1"`. Nothing is saved; `Print` prints the finished piece.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| W.1.2 | How-To: pick a topic sentence, put step cards in order with sequence words, add a closing; Robo acts it out | Robo's kitchen or garden; a mess for a missing or swapped step | 2, 3 |
| W.1.3 | Story: put event cards in order with time words, pick a detail for each, and add an ending with a feeling | Robo's puppet screen; "And then?" until the ending | 4 |
| W.1.1 | Opinion: pick a pet, a reason that fits it, and a closing | Robo's "Why?" and "So?" lights | 5 |
| W.1.1, W.1.2, W.1.3 | Read the finished piece back as one paragraph | the paragraph with each card's words | 6 |

## Screens and modes
Header (kit): title "First, Next, Last"; `Jobs`; `Read`, `Motion`, `Sound`, `Print`. Controls 60 px or more at 1366x768 (44 px at 680x425), icon plus word.

**On load and first tap.** Robo's workshop with three job doors (a spatula, a puppet, a heart). First hint: "Tap a door to give Robo a job." The first tap opens the job with its own line; the welcome is queued after it (`welcomeAfter: true`).

**The writing rail.** Every job uses one screen: the writing rail on the left (a vertical strip of sentence slots, 520 x 600: Topic, then steps or events, then Closing or Ending), the card tray at the bottom (picture cards with their sentence, 180 x 140), and Robo's stage on the right (620 x 420). A sentence slot has two parts: a sequence-word car (`First`, `Next`, `Then`, `Last` for how-to; `First`, `Next`, `Then`, `At the end` for story) and the card. Drag a card into a slot (or tap it, then the slot); tap the sequence car to cycle its word. `Run Robo` is always on.

**How-To.** Topics: "Make a jam sandwich" and "Plant a seed". Run Robo: Robo acts each sentence in order, literally. A missing step shows its mess (no bread: jam on the counter); a swapped pair shows its mess (top slice before jam: jam on the outside); the distractor card (Put on your shoes) makes Robo stop and put on boots in the kitchen. No topic sentence: Robo says "What are we making?" No closing: Robo stands holding the sandwich, "Am I done?"

**Story.** Topics: "Kip at the Park" and "Snow Day". Each event card has two detail picks (a sound or a feeling word: "with a splash", "slowly"). Run Robo: Robo plays the events with paper puppets. With no ending card Robo asks "And then?" and keeps the puppets frozen; with an ending but no feeling, Robo asks "How did Kip feel?"

**Opinion.** Pick a pet card (dog, cat, fish). The rail: "I think a {dog} is the best pet." / reason slot / closing slot. Reasons on the tray come from all three pets (fetch a ball, purr on my lap, swim in a bowl) plus "it is blue". Run Robo: no reason, Robo's Why light blinks and Robo asks "Why?"; a reason that doesn't fit the pet (a dog because it swims in a bowl), Robo pictures it (a dog in a fishbowl) and asks "Does that fit?"; no closing, the So light blinks: "So?" When whole, Robo nods and holds up the pet.

**Read it back.** When Robo does a job right: `Read it` reads the whole piece as one paragraph in Robo's voice with each sentence lit; `Print` prints it with the child's name line left blank to write by hand.

At 1366x768 the rail, tray and stage fit above the fold. At 680x425 the stage moves above the rail and cards are 130 x 100.

## Content
All written for Curio Class. Each card: the sentence read on tap and a picture.

**How-To, Make a jam sandwich.** Topic picks: "I will tell you how to make a jam sandwich." (right) | "I like jam." Steps in order: Get two slices of bread. | Spread jam on one slice. | Put the other slice on top. | Cut it in half. Distractor: Put on your shoes. Closing picks: "Now you have a jam sandwich!" (right) | "The bread is soft." Messes: no bread: jam on counter; jam before bread: jam on counter, then bread on top of nothing; top before jam: jam on the outside; cut before top: half slices with jam, open.

**How-To, Plant a seed.** Topic: "Here is how to plant a seed." | "Seeds are small." Steps: Dig a little hole. | Drop in a seed. | Cover it with soil. | Water it every day. Distractor: Put it in the freezer. Closing: "Soon you will have a plant!" | "Dirt is brown." Messes: no hole: the seed rolls away; cover before seed: a seed sits on top of a filled hole; water before cover: the seed floats out.

**Story, Kip at the Park.** Events in order: Kip the dog found a red ball. | Kip kicked the ball into the pond. | A duck pushed the ball back to Kip. Details: found (happily | slowly), kicked (with a splash | very hard), pushed (with her beak | with a quack). Ending picks: "At the end, Kip and the duck played all day. Kip felt happy." (right) | "The pond is wet." (no closure: Robo asks "And then?")

**Story, Snow Day.** Events: Ana woke up and saw snow. | She built a snowman with a carrot nose. | Her little brother put his hat on it. Details: woke up (with a big yawn | early), built (with Dad | slowly), put (with a giggle | very carefully). Ending: "At the end, they had hot cocoa. Ana felt warm and happy." | "Snow is cold."

On screen, the right ending is first for Kip at the Park and second for Snow Day.

**Opinion.** Pets and fitting reasons: dog, it can fetch a ball; cat, it purrs on my lap; fish, it swims in a bowl all day. Off-topic reason: it is blue. Topic: "I think a {pet} is the best pet." Closing: "That is why a {pet} is the best pet!" | "I have a sock." The reason card reads "because {reason}."

## Interactions in detail
- Every tap acts at once; a new line stops the old one. `Run Robo` while Robo is acting stops and restarts.
- A card can sit in any slot; slots can be left empty; Run Robo shows the first problem only (from the engine's ordered rules), and Robo's mess or question names it.
- Sequence words: `sequence` rules ask for `First` on the first step, `Last` (how-to) or `At the end` (story) on the ending or last step, and `Next` or `Then` between; Robo reads a wrong one literally ("Last, get two slices of bread. Then I'm done? But I didn't make anything!").
- Order is checked against the one order in the data; Robo acts the order given so the reason is seen.
- Detail picks for story events: any detail is fine; a story with no details runs, but Robo says "Tell me more! How did Kip kick it?" once (the piece still counts; details add stars).
- Each job ends with a star; a second star for a story with a detail on every event.
- `Start over` clears the rail after one confirm.

## Look
- Accent `--brand` #1d6b73 workshop teal (header, rail, Robo's trim); gold #f4c542 (stars, the Why and So lights); paper #f4fafa; ink #10292c; muted #4a5f61. Scene: a tidy robot workshop with pegboards.
- Contrast (WCAG 2.1, computed): white on brand 6.17:1; brand on paper 5.85:1; ink on paper 14.47:1; muted on paper 6.42:1; ink on gold 9.39:1.
- Never color alone: slot kinds have icons (a flag for Topic, numbered gears for steps, a checkered flag for Closing); Robo's lights have the words Why and So.
- Different from this batch (dusk violet, brick map, coral sea, olive post office).

## Art
Local FLUX (`scripts/localart.py`); story characters are animals (Kip the dog, the duck, Ana the bunny and her little brother).
- workshop (1): "A tidy cartoon robot workshop with pegboards and three doors, soft gouache, no text"; 16:9; cutout no.
- Robo (8: stand, act, puzzled, nod, hold sandwich, hold plant, boots, bow): "A friendly round teal robot with a screen face, <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- step and event cards (22): "<two slices of bread / a hand spreading jam / ...>, simple soft gouache, plain white background"; 4:3; cutout yes.
- messes (8): "<jam spread on a kitchen counter / a sandwich with jam on the outside / a seed floating in a puddle / ...>, funny, soft gouache"; 4:3; cutout no.
- pets and reason pictures (7): "<a dog fetching a ball / a cat on a lap / a fish in a bowl / a dog in a fishbowl / ...>, soft gouache, plain white background"; 1:1; cutout yes.
About 46 images. Drawn in code: the rail, slots, sequence cars, lights, puppet rods, controls.

## Voice
Bank voice `casual-peer` as Robo, with the style override "Cheerful and very literal, a little robotic" (unique in this batch). `Curio.voice` with `scope: () => state.job + ':' + state.slot`, `welcomeAfter: true`.
- event `door`: "{How-To}! Beep."
- how `welcome`: "Hi! I'm Robo. I do exactly what you write. Put the cards in order, then tap Run Robo."
- event, whole, `card`: the card's sentence.
- event, whole, `run`: each sentence read as Robo acts it.
- event `mess`: "Uh oh. {I spread jam, but there was no bread.} What step is missing?"
- event `swap`: "{The jam is on the outside!} Which step should come first?"
- event `extra`: "{Put on your shoes?} In the kitchen?"
- event `noTopic`: "What are we making?" / "What is this story about?"
- event `noClose`: "Am I done?"
- event `andThen`: "And then? And then?"
- event `feel`: "How did {Kip} feel?"
- event `why` / `fits` / `so`: "Why?" / "{A dog that swims in a bowl?} Does that fit?" / "So?"
- event `more`: "Tell me more! How did {Kip kick it}?"
- event `done`: "I did it! Beep boop."
- event, whole, `readBack`: the whole paragraph.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
`kit/sentence-train.js`, described in tools/sentence-train/spec.md, exposed as `__tool.st`. This tool uses Car (adds kinds `sequence`, `topic`, `closing`, `step`), Train (one train per sentence; a piece is a list of trains), Check with the `sequence` rule set (`topic`, `stepsAll`, `stepsOrder`, `noExtra`, `seqWord`, `closing`, and for opinion `reason`, `reasonFits`), and Target (`st.matches` per sentence against the data order). Not Trace or Depart; Robo's acting replaces Depart.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| How-To order | Drop cards in any order | 4 steps from 5 cards in order: 120 ordered picks (computed), one right; Robo acts the given order, so a wrong one is seen. |
| How-To | Use every card | The distractor makes Robo stop. |
| Sequence words | All Next | The first step needs First and the last needs Last; Robo reads them literally. |
| Story ending | Pick the first ending | Right ending is first in one story, second in the other. |
| Opinion reason | Any reason | Only 1 of 4 fits each pet; the wrong pet's reason is pictured. |
| Read it back | Skip | It only appears after Robo does the job right. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a door: `door`, `welcome` (queued, first time).
2. Tap a card: `card` (whole).
3. Run Robo: `run` (whole, sentence by sentence) until the first problem, then one of `mess`, `swap`, `extra`, `noTopic`, `noClose`, `andThen`, `feel`, `why`, `fits`, `so`; or `more` then `done`.
4. Read it: `readBack` (whole).
No line contains a bare letter or letter sound.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| W.1.1, W.1.2, W.1.3 wording (opinion with a reason and closure; informative with a topic, facts and closure; narrative with two or more sequenced events, details, temporal words and closure) | thecorestandards.org, Writing Grade 1 | CCSS ELA 2010 PDF | yes |
| Plant a seed steps (dig, drop in, cover with soil, water) | RHS, "How to sow seeds outdoors" (rhs.org.uk) | BBC Gardeners' World, "How to sow seeds outdoors" | yes |
Backed twice: 2. Cut: 0.

Checks run (Python, scratchpad b6, 2026-11-08): ordered picks of 4 from 5 cards = 120; each opinion pet has exactly one fitting reason among 4; story ending right-pick positions 1 and 2; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the rail, tray and Robo's stage show with no scroll; at 680x425 the stage sits above the rail.
2. How-To: the right order, sequence words, topic and closing make Robo finish; each missing or swapped step shows its own mess. (W.1.2)
3. The distractor card stops Robo; a wrong sequence word is read literally.
4. Story: no ending gives "And then?"; an ending with a feeling finishes; details add the second star. (W.1.3)
5. Opinion: no reason gives "Why?", a reason that doesn't fit is pictured, no closing gives "So?"; a fitting reason and closing finish. (W.1.1)
6. Read it back reads the whole piece as one paragraph, sentence by sentence lit; Print prints it.
7. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
8. Pre-reader: every card is read on tap and has a picture.
9. Motion off: Robo's acting is shown as still frames with the line read; no network requests; nothing saved.

## Open questions
- None for Cory.

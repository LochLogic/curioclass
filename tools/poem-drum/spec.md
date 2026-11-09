# Poem Drum

## One idea
A poem has a heartbeat you can play: a hand drum taps the beat under every line while the class claps along, and each thing that makes it a poem the class finds (the rhyming words, the line that comes back, the words you can feel or hear, the words that start the same way) adds its own instrument to the drum, so by the end the poem plays as a little song built from its own parts, and the class reads it aloud in time and records it.

## Not like
- rhyme-time-rumble (k, spec): listen-only sound bouts with no print. Here a printed poem, where rhymes, repeats and beats are found in the words.
- read-along-shelf (k-2, spec): six books with reading help that fades page by page. Here one poem at a time, read to a steady beat, and its parts turned into sounds.
- little-book-press (k-2, spec, same format): making a book. Here performing and recording a poem.
- question-cube (k-2, spec): questions about a story. Here what makes a poem sound like a poem.
- poetry-soundboard (7, concept, same family): muting rhyme, repetition and meter channels in a stanza and a sonnet. Here K-2: adding one instrument per part found, and a drum for the beat.

## Who and how
- Grades K to 2, ELA, module "Poems and Songs Aloud" (Reading Literature). Standards: RL.K.5, RF.K.4, RL.1.4, RF.1.4, RL.2.4, RF.2.4, SL.2.5.
- Driver: teacher on a projector, or a small group at one device (tool.json `driver: "either"`). The class claps, says answers and reads aloud; a helper taps. Every word, line and card is spoken, so a pre-reader can play (BASELINE rule 4).
- Three poems, tagged K, 1 and 2; any class can open any. Steps per poem: Poem or story?, Clap the beat, Find the parts, Read with the drum, Record. tool.json `modes: []`, `minutes: "10-15"` per poem, `grades_label: "Grades K-2"`.
- Recording: needs the microphone; the recording is kept only on this device while the page is open, never sent anywhere, and is gone when the page closes. The record screen says so in words and it is read once. (BASELINE rule 7.)

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.K.5 | Poem or story?: two pages on one topic; pick the poem, then pick every clue that shows it is a poem | two pages side by side; four clue cards | 2 |
| RF.K.4 | Read with the drum: read the K poem along as each beat lights, with a purpose ("Read it like rain on a roof") | the poem with beat dots under the stressed words | 6 |
| RL.1.4 | Find the parts (poem 1): tap the words that tell how the cat feels to touch, the words that are sounds, and the word that tells how the cat feels inside | the poem; tapped words glow in that question's color | 4 |
| RF.1.4 | Read with the drum at slow, then poem speed; read again with expression | the beat dots; a speed switch | 6 |
| RL.2.4 | Clap the beat and count beats per line; find rhymes, the repeated line, and the phrases whose words start the same way; each adds an instrument | beat dots; instrument badges; a beats picker | 3, 4, 5 |
| RF.2.4 | Read poem 2 with the drum, then without the dots | the poem; dots fade at `I read` | 6 |
| SL.2.5 | Record a reading of the poem in time with the drum and play it back with the instruments | the record button, count-in, playback | 7 |

## Screens and modes
Header (kit): title "Poem Drum"; `Poems` (book icon); `Read`, `Motion`, `Sound`. Controls 60 px or more at 1366x768 (44 px at 680x425), icon plus word.

**On load and first tap.** A cozy night porch: a big hand drum, three poem cards on a string (Rain Drum, tag K; Sunny Spot, tag 1; Big Brown Bear, tag 2). First hint: "Pick a poem. Tap a card to start." The first tap opens the poem's first step with its line; the welcome is queued after it (`welcomeAfter: true`).

**Poem or story?** Focus: two pages side by side (each 560 x 420): the poem and a short story about the same thing. Both are read aloud. "Which one is the poem?" The class picks; then four clue cards: "Which clues show it's a poem? Pick all that fit." `Check` lights each right clue; a missed or extra clue is named ("That one is true of the story too.").

**Clap the beat.** Focus: the poem (40 px type), a dot under each beat syllable, and the drum. `Play the beat`: the drum taps and each dot lights on its beat while the line is read; the class claps. Poem 2 adds "How many beats in this line?" with 2, 3, 4 cards for two lines.

**Find the parts.** Focus: the poem and a row of part buttons (Rhymes with a bell icon, Same line with a shaker, Sense words with a chime (poem 1), Same start with a woodblock (poem 2)). Pick a part; its ask is read; tap words or lines in the poem; `Check`. Right: the part's instrument badge appears and its sound joins the drum ("Hear the bells on the rhymes!"). A miss or an extra is named and those taps stay so the class can fix them. After the parts, `Play it all`: the poem is read with the drum and every instrument found.

**Read with the drum.** Focus: the poem. Three speeds: `Slow`, `Medium`, `Poem speed`, and three helps: `Read to us` (the voice reads, dots light), `Read with us` (dots light, the voice drops out on the last word of each line), `I read` (drum only, dots fade). The purpose line is read first.

**Record.** Focus: a round record button (120 px) and the poem. `Record`: the drum counts in four beats, then plays softly as the class reads; tap again or it stops 4 s after the last line's beat. `Play ours`: the recording plays with the instruments the class found. `Again` records over it.

At 1366x768 the poem, its dots and the step's controls fit above the fold. At 680x425 the poem is 26 px and two pages in Poem or story? become tabs.

## Content
Beat syllables are in capitals. All three poems and stories are written for Curio Class.

**Poem K: "Rain Drum"** (purpose: "Read it like rain on a roof")
- DRIP, DROP, RAIN on the ROOF,
- DRIP, DROP, RAIN on the STREET,
- DRIP, DROP, RAIN on my HAT,
- and SPLISH, SPLASH, RAIN on my FEET!
Story: "It rained today. I wore my hat and my red boots. I jumped in a puddle, and my feet got wet."
Parts: Rhymes: street, feet (end words roof, street, hat, feet). Same line: the start "Drip, drop, rain on the" in lines 1, 2 and 3.

**Poem 1: "Sunny Spot"** (purpose: "Read it softly, like a sleepy cat")
- my CAT naps IN a SUN-ny SPOT,
- so WARM and SOFT and ROUND.
- her PURR is LIKE a TI-ny DRUM,
- a SLEEP-y, HUM-ming SOUND.
Story: "My cat sleeps in the sun every day. She likes the warm spot by the window. When I pet her, she purrs."
Parts: Rhymes: round, sound (end words spot, round, drum, sound). Sense words, three asks: "Which words tell how the cat feels to touch?" {warm, soft}; "Which words are sounds?" {purr, humming}; "Which word tells how the cat feels inside?" {sleepy}.

**Poem 2: "Big Brown Bear"** (purpose: "Read it with a bouncy, bumbly beat")
- BUM-ble, BUM-ble, BIG brown BEAR,
- BUM-bling HERE and BUM-bling THERE,
- LOOK-ing LOW and LOOK-ing HIGH,
- HUNT-ing HON-ey, BEES buzz BY.
- BUM-ble, BUM-ble, BIG brown BEAR,
- STICK-y HON-ey EV-ery-WHERE!
Story: "A bear looked for food in the woods. It found a beehive in a tree and ate the honey. The bees were not happy."
Parts: Beats: four in every line (asked for lines 1 and 3). Rhymes: two groups, {bear, there, bear, everywhere} and {high, by}. Same line: lines 1 and 5. Same start, phrase chips: "big brown bear" yes, "here and there" no, "looking low" yes, "hunting honey" yes, "bees buzz by" yes, "sticky honey everywhere" no.

**Clue cards** (every poem): "It has a beat you can clap." (yes) | "Its lines end with words that rhyme." (yes) | "It tells about {rain}." (no, both do) | "It is written in sentences that run across the page." (no, that's the story).

**Instruments**: drum (beat), bell (rhymes), shaker (same line), chime (sense words), woodblock (same start). Each is a short recorded sound.

## Interactions in detail
- Every tap acts at once; a new line stops the old one; Play the beat can be stopped with the same button.
- Word taps in Find the parts toggle; `Check` is always on and names what is missing or extra. Rhymes: tap a word, then the word that rhymes with it; a group is found when all its words are tapped together.
- The beat: each poem has a set tempo (Rain 96, Sunny Spot 72, Bear 104 beats a minute at poem speed; Slow is 70 percent, Medium 85 percent). Dots light on the beat; Motion off keeps the dots lighting with no bounce.
- Nothing is scored; each poem's card on the string gets a star per part found.
- Record: microphone refused or missing says "No microphone. You can still read with the drum." and the other steps work.
- `Poems` returns to the porch; found parts stay until `Start over`.

## Look
- Accent `--brand` #2b2d6e night indigo (header, drum rim, dots); gold #ffcc3d (lit dots, stars); bell, shaker, chime and woodblock each have their own icon shape and a pale tint; paper #f8f6fb; ink #18182e; muted #5a5870. Scene: a cozy porch at night with string lights.
- Contrast (WCAG 2.1, computed): white on brand 12.33:1; brand on paper 11.49:1; ink on paper 16.18:1; muted on paper 6.38:1; ink on gold 11.54:1.
- Never color alone: each part has an icon and a word; tapped words get an underline in the part's shape as well as a tint.
- Different from this batch (moss, engine black, curtain wine, wind cyan) and the K-2 ELA neighbors.

## Art
Local FLUX (`scripts/localart.py`); no people.
- porch (1): "A cozy wooden porch at night with string lights, a big hand drum, soft gouache, no text"; 16:9; cutout no.
- poem pictures (3 poems x 2 = 6): "<rain falling on a roof and a puddle / a cat napping in a sunny window / a bumbling brown bear finding a beehive, bees buzzing> soft gouache, gentle, simple background"; 4:3; cutout no; one beside the poem, one beside the story.
- instruments (5): "<a hand drum / a small bell / an egg shaker / a wind chime / a woodblock>, soft gouache, plain white background"; 1:1; cutout yes.
About 12 images. Drawn in code: dots, part underlines, clue cards, the record button and count-in, every control.

## Voice
Bank voice `playful-friend` (style "like a fun music teacher") as the narrator. Not used by the K-2 ELA neighbors or the rest of this batch. `Curio.voice` with `scope: () => state.poem + ':' + state.step`, `welcomeAfter: true`.
- event `poemCard`: "{Rain Drum}!"
- how `welcome`: "Welcome to Poem Drum! Every poem has a beat. Let's find it and play it."
- event, whole, `line`: each line or story sentence as read.
- event, whole, `whichAsk`: "Which one is the poem?" event `whichYes` / `whichNo`: "Yes! That's the poem." / "Listen again. Which one has a beat?"
- event `cluesAsk`: "Which clues show it's a poem? Pick all that fit." event `clueNo`: "That one is true of the story too." / "Is that true of the poem?"
- how `clapHow`: "Clap with the drum! One clap on every beat."
- event, whole, `beatsAsk`: "How many beats in this line?" event `beatsYes` / `beatsNo`: "Four beats!" / "Let's clap it again and count."
- event, whole, `partAsk`: the part's ask (for example "Find two words that rhyme." / "Which line comes back again?" / "Which words tell how the cat feels to touch?" / "Which groups of words start the same way?").
- event `partYes`: "Yes! Hear the {bells} on the {rhymes}!" event `partMiss` / `partExtra`: "There's one more to find." / "Listen to that one again. Does it fit?"
- event, whole, `purpose`: the poem's purpose line.
- how `recordHow` (once): "Your recording stays on this device, and it's gone when you close the page. Tap Record, wait for four drum beats, then read."
- event `countIn`: the four drum beats (sound only). event `recDone`: "Let's hear it!"
- event `noMic`: "No microphone. You can still read with the drum."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
`kit/poetry.js` (the poetry family). No family doc exists and the only sibling, poetry-soundboard (7), is a concept, so this spec describes the engine for both. Pure parts in one marked block, exposed as `__tool.po`.
- **Poem**: `{id, title, lines:[{text, beats:[wordIndex...], syllables}], tempo, parts}`; beat syllables are stored per word, never guessed at run time.
- **Parts**: named sets on the poem: `rhyme` (groups of word ids), `repeat` (line or phrase ids), `sense` (asks with exact word sets), `samestart` (phrase chips with yes or no), and for poetry-soundboard `meter` and `alliteration` by line. `po.check(part, picks)` returns `{right, missing, extra}`.
- **Beat clock**: `po.clock(tempo, speed)` drives the lit dots and the drum; it uses the audio clock, not timers, so beats do not drift.
- **Channels**: each part found turns on an instrument channel; `po.play(poem, channels)` reads or plays the poem with the drum and the on channels; poetry-soundboard uses the same channels to mute one part at a time.
- **Record**: `po.record(clock, countIn)` records with the browser's media recorder after a count-in, keeps the clip in memory only, and `po.playback(clip, channels)` plays it with the instruments; `po.forget()` on leave.
This tool uses all parts but `meter` and `alliteration`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Poem or story? | Guess the page | 1 in 2, so the clue cards follow: an exact set of 2 of 4, 1 right of 16 ways (computed), and two wrong clues are true of the poem or the story, so "it's true" does not pick. |
| Rhymes | Tap end words at random | K and poem 1: 1 right pair of 6 (computed); poem 2 needs both groups; end words that do not rhyme sit at the same place in the line. |
| Same line | Tap the first line | K needs lines 1, 2 and 3 exactly; poem 2 needs 1 and 5; extras are named. |
| Sense words | Tap every describing word | Each ask is an exact set; "round" and "tiny" are describing words but answer none of the three asks, so tapping all describing words leaves extras. |
| Same start | Tap every chip | Two of six chips are not (exact set, 1 of 64, computed); "sticky honey everywhere" has a repeated word from the right chips to tempt. |
| Beats | Always pick four | Every Bear line has four beats, so this check teaches counting more than it tests it; it is never the only check of RL.2.4. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a poem card: `poemCard`, `welcome` (queued, first time), then the poem and story `line`s (whole, each waits), then `whichAsk`.
2. `whichYes` or `whichNo`, then `cluesAsk`; Check plays `clueNo` per wrong clue.
3. `clapHow`, then the beat with the lines; `beatsAsk` (poem 2).
4. Each part: `partAsk` (whole), Check plays `partYes` and the instrument, or `partMiss` / `partExtra`.
5. Read with the drum: `purpose` (whole), then the poem at the chosen speed.
6. Record: `recordHow` (once), `countIn`, the recording, `recDone`, playback.
No line contains a bare letter or letter sound ("start the same way" is always said with whole words).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.K.5, RF.K.4, RL.1.4, RF.1.4, RL.2.4, RF.2.4, SL.2.5 wording (recognize common types of texts such as storybooks and poems; read emergent-reader texts with purpose and understanding; words that suggest feelings or appeal to the senses; read with accuracy, rate and expression; regular beats, alliteration, rhymes and repeated lines supply rhythm and meaning; create audio recordings of stories or poems) | thecorestandards.org, RL, RF and SL K-2 | CCSS ELA 2010 PDF | yes |
| Bears raid beehives to eat the honey (poem 2 and its story) | National Park Service, "What do bears eat?" | National Wildlife Federation, "Black bear" | yes |
Backed twice: 2. Cut: 0. The poems and stories are written for Curio Class; cats purring and rain on roofs are everyday experience, not claims.

Checks run (Python, scratchpad b4, 2026-11-08): clue sets 16 ways; rhyme pairs 6 ways; same-start chips 64 ways; beats per line counted from the capitals (Rain 4, 4, 4, 4; Sunny Spot 4, 3, 4, 3; Bear 4 in every line); contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the poem, its dots and the step's controls show with no scroll; at 680x425 the same, with the two pages as tabs.
2. Poem or story?: only the poem page is right; only the two poem clues check right, and each wrong clue is named. (RL.K.5)
3. Clap the beat: dots light on the capital syllables at the poem's tempo with no drift over three plays; Bear asks beats for lines 1 and 3, only four is right. (RL.2.4)
4. Parts: each part's exact set checks right and only then adds its instrument; Sunny Spot's three sense asks take only {warm, soft}, {purr, humming}, {sleepy}. (RL.1.4, RL.2.4)
5. Play it all: the poem plays with the drum and only the found instruments, on their words. (RL.2.4)
6. Read with the drum: the three speeds and three helps change the dots and the voice as described; the purpose line comes first. (RF.K.4, RF.1.4, RF.2.4)
7. Record: count-in of four, recording plays back with the instruments; nothing is stored after the page closes; no network requests. (SL.2.5)
8. No microphone: Record says so and every other step works.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Pre-reader: every line, card and ask is spoken. Motion off: dots light with no bounce.

## Open questions
- None for Cory.

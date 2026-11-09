# Sentence Train

## One idea
A sentence is a train that has to work before it can leave the station: the engine is the first word and wears a capital, the caboose is the end mark, and in between the class couples word cars (a naming car, a doing car, a where car, a describing car) to match a picture, so the whistle only blows when the sentence is whole, and when a car is missing or out of place Conductor Wally the walrus says exactly what the train still needs.

## Not like
- big-book-pointer (k, spec): print concepts and letters in a big book. Here building and fixing sentences.
- word-meaning-yard (k, spec): sorting words by meaning. Here putting words together into sentences that work.
- rhyme-time-rumble (k, spec): sounds only, no print. Here print: capitals, end marks and spelling by sound.
- owl-wants-more (k-2, spec): adding details and fixing capitals in a story. Here one sentence at a time, built from cars, with the grammar parts named.
- first-next-last (1, concept, same family): steps of a how-to or story as cars that Robo acts out. Here the cars are words inside one sentence.

## Who and how
- Kindergarten, ELA, module "Words and Sentences" (Language). Standards: L.K.1 (a to f), L.K.2 (a to d).
- Driver: teacher on a projector (tool.json `driver: "teacher"`); the class says which car comes next and a helper drags or taps. Every car is read when tapped and has a picture (small words like "the" and "is" are short gray cars), so a pre-reader can play (BASELINE rule 4).
- Seven stations on a track map, any order: `Who and Do`, `One or More`, `Where`, `Ask It`, `Capital and End`, `Cargo`, `Grow the Train`. tool.json `modes: []`, `minutes: "5-10"` per station, `grades_label: "Kindergarten"`. Nothing is saved.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| L.K.1a | Capital and End: trace the capital on the engine car | a big dotted capital with a start dot | 6 |
| L.K.1b | Who and Do: couple a naming car and a doing car that match the picture | the picture; word cars with pictures | 2 |
| L.K.1c | One or More: hear three spoken choices and pick the car that says the right word for more than one (cats, boxes) | the picture; three cars | 3 |
| L.K.1d | Ask It: pick the question word engine (who, what, where, when, why, how) that asks about the picture | the train with a gap at the front | 5 |
| L.K.1e | Where: couple the where car (in, on, off, out, by, with, to, from, for) that matches the picture | three where cars | 4 |
| L.K.1f | Grow the Train: add a describing car and a where group to a short sentence so it says more about the picture | the short train; new cars; the longer train read aloud | 8 |
| L.K.2a | Capital and End: fix a train whose engine or "I" car is lowercase | the train with a lowercase car | 6 |
| L.K.2b | Ask It and Capital and End: pick the caboose (period, question mark, exclamation point) and name it | three cabooses | 5, 6 |
| L.K.2c, d | Cargo: hear a word, then load letter tiles into the boxcar to spell it by its sounds | a picture, three slots, six tiles | 7 |

## Screens and modes
Header (kit): title "Sentence Train"; `Map` (track icon); `Read`, `Motion`, `Sound`. Controls 60 px or more at 1366x768 (44 px at 680x425), icon plus word.

**On load and first tap.** The track map (painted, 1046 x 640): seven little stations along a looping track, each with a sign (picture and words), and Conductor Wally the walrus by the first one with a whistle. First hint: "Pick a station. Tap Who and Do to start." The first tap opens that station with its line; the welcome is queued after it (`welcomeAfter: true`).

**A station.** Focus: the station picture (600 x 340, top center), the train on the track below it (engine, slots, caboose; each car 150 x 110), and the car yard below that (four to six cars). Tap a car to hear it; drag it (or tap it, then a slot) to couple it; drag it off to uncouple. `Go!` (a whistle, always on): if the sentence works, the whistle blows, the train reads itself aloud word by word as each car lights, and it chugs off (Motion off: it fades and the next train appears). If not, it shakes once and Wally names the first thing missing or wrong ("This train has no doing car. What is the dog doing?"). Six trains per station; finished stations get a ticket on the map.

**Cargo.** Focus: a picture (300 px), a boxcar with three slots, and six letter tiles. `Hear it` says the word, then says it slowly and smoothly. Tap a tile to hear its letter name and a picture word ("m, like moon"); drag it into a slot. `Go!` checks the slots: a wrong slot's tile pops up and Wally says the word slowly again ("Listen to the start of sun."). Right: the spelled word becomes a car in the Grow the Train yard.

At 1366x768 the picture, train and yard fit above the fold. At 680x425: picture 360 x 200, cars 90 x 66, the yard scrolls in one row.

## Content
**Who and Do** (picture: the sentence the train should say; yard cars, right first):
1. a dog running: "The dog runs." (The, dog, runs | sleeps, cat)
2. a bird singing: "The bird sings." (The, bird, sings | swims, frog)
3. a frog jumping: "A frog jumps." (A, frog, jumps | eats, bus)
4. a bear cub sleeping: "The bear sleeps." (The, bear, sleeps | runs, bed)
5. a fish swimming: "The fish swims." (The, fish, swims | flies, ball)
6. a cat eating: "My cat eats." (My, cat, eats | jumps, hat)

**One or More** (picture; the three spoken cars, right first): three cats (cats | cat, catses); two dogs (dogs | dog, dogses); four hats (hats | hat, hatses); two boxes (boxes | box, boxeses); three foxes (foxes | fox, foxeses); two dishes (dishes | dish, disheses). The wrong cars are the two common slips: no plural, or one plural too many. The chosen word is coupled into "I see two {boxes}."

**Where** (picture; sentence with the gap; where cars, right first):
1. a cat sitting on a box: "The cat is ___ the box." (on | in, by)
2. a cat inside a box: "The cat is ___ the box." (in | on, out)
3. a frog jumping off a log: "The frog jumps ___ the log." (off | on, with)
4. a dog walking with a bear cub: "The dog walks ___ the cub." (with | off, in)
5. a bus going to a school: "The bus goes ___ school." (to | from, of)
6. a bird flying out of a cage door: "The bird flies ___ the cage." (out of | in, on)

**Ask It** (picture with a question mark cloud; train with a gap at the front; engines, right first; caboose choices period, question mark, exclamation point, right is question mark):
1. a covered box: "___ is in the box?" (What | Who, When)
2. a knock at a door, a shadow: "___ is at the door?" (Who | What, How)
3. a lost ball, empty field: "___ is my ball?" (Where | Why, Who)
4. a clock and a cake: "___ is the party?" (When | Where, What)
5. a crying bear cub: "___ is the cub sad?" (Why | When, Who)
6. a tall tower of blocks: "___ did you build it?" (How | Who, Where)

**Capital and End** (a train that needs fixing; tap the car to fix):
1. "the sun is hot." (engine to "The"; trace the T)
2. "We see a bus" (caboose: period)
3. "can you jump?" (engine to "Can"; trace the C)
4. "My dog and i play." ("i" car to "I"; trace the I)
5. "Look out" (caboose: exclamation point)
6. "Is it cold" (caboose: question mark)
Fixes: tap a lowercase car and pick the capital from three tiles (the right capital, the same letter lowercase, a look-alike capital), then trace it.

**Cargo** words (picture: tiles, right three first): sun (s, u, n | m, a, t); cat (c, a, t | g, o, p); pig (p, i, g | b, e, d); map (m, a, p | n, u, b); hen (h, e, n | f, i, m); bus (b, u, s | d, a, m).

**Grow the Train** (start train; added cars; the grown sentence):
1. "The dog runs." + big, to the park: "The big dog runs to the park."
2. "A bird sings." + little, in the tree: "A little bird sings in the tree."
3. "The cat naps." + sleepy, on the bed: "The sleepy cat naps on the bed."
4. "The frog jumps." + green, off the log: "The green frog jumps off the log."
Plus the Cargo words as cars (sun, cat, pig, map, hen, bus) for free building; the train reads anything the class builds and Wally says whether it works.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- `Go!` checks in this order and names only the first problem: engine (no first word, or a lowercase first word), a naming car, a doing car, words in a place that does not work (a doing car before the naming car), a where car with no thing after it, the caboose (missing, or a period on a question).
- One or More: the three cars show a speaker icon and the station picture, not the word, until one is picked (the standard is oral); the picked car then shows its word.
- Cars can be coupled in any slot; the train grows a slot when every slot is full (up to eight cars).
- Capital and End tracing: the capital is traced on a dotted guide with a start dot; it passes when the path stays within 24 px of the guide and covers its strokes in order; `Help me` shows the strokes moving.
- Cargo: tiles can be swapped; `Hear it` can be tapped any time.
- Nothing is scored; a station's ticket appears when its six trains have left.
- `Map` returns to the map; stations keep their state until `Start over`.

## Look
- Accent `--brand` #2e2e38 engine black (header, engine, track); brass #d9a521 (whistle, tickets, coupling pins); car colors by kind, each also with an icon: naming cars blue with a person-place-thing icon, doing cars green with a running icon, where cars orange with an arrow, describing cars purple with a sparkle, small words gray; paper #f8f7f4; ink #1a1a20; muted #5d5b57. Scene: a sunny country station.
- Contrast (WCAG 2.1, computed): white on brand 13.43:1; brand on paper 12.53:1; ink on paper 16.17:1; muted on paper 6.32:1; ink on brass 7.71:1. Car words are ink on pale tints of the car colors, each at least 7:1 (checked at build).
- Never color alone: every car kind has an icon; cabooses show the mark large; a train that fails shakes and shows the missing car as a dashed outline.
- Different from this batch (indigo, moss, curtain wine, wind cyan) and the K ELA neighbors.

## Art
Local FLUX (`scripts/localart.py`); no people.
- map (1): "A looping toy train track through green hills with seven small stations, seen from above, soft gouache, no text"; 16:10; cutout no.
- wally (stand, whistle, point, cheer: 4): "A friendly walrus train conductor in a blue cap <standing / blowing a whistle / pointing / cheering>, soft gouache, plain white background"; 1:1; cutout yes.
- station pictures (Who and Do 6, One or More 6, Where 6, Ask It 6, Capital and End 6, Grow the Train 4 = 34): "<the item's scene with animals>, soft gouache, simple background"; 16:9; cutout no.
- car pictures (about 40 words: dog, cat, bird, frog, bear, fish, bus, ball, hat, bed, runs, sleeps, sings, swims, jumps, eats, flies, big, little, sleepy, green and the Cargo words): "<subject>, simple soft gouache icon, plain white background"; 1:1; cutout yes.
- cargo pictures reuse car pictures.
About 79 images. Drawn in code: train cars and their icons, cabooses and marks, tiles, the trace guide, tickets, every control.

## Voice
Bank voice `firm-captain` (style "firmly but kindly, like a ship captain giving clear directions") as Conductor Wally. Not used by the K ELA neighbors or the rest of this batch. `Curio.voice` with `scope: () => state.station + ':' + state.item`, `welcomeAfter: true`.
- event `station`: "{Who and Do} station!"
- how `welcome`: "All aboard! I'm Conductor Wally. A sentence is a train: an engine with a capital, cars in a row, and a caboose at the end. It only leaves when it works."
- how per station (once): Who and Do "Who is it, and what are they doing?"; One or More "Listen. Which car says more than one?"; Where "Where is it? Pick the where car."; Ask It "This train asks a question. Pick the question word for the front."; Capital and End "Something's wrong with this train. Tap the car to fix."; Cargo "Load the boxcar. Spell the word by its sounds."; Grow the Train "Make the train say more!"
- event `car`: the car's word. event, whole, `read`: the train read aloud as it leaves.
- event `need`: one of "This train has no engine." / "The engine needs a capital." / "This train has no naming car. Who is it about?" / "This train has no doing car. What is {the dog} doing?" / "Those cars are in a funny order. Listen." (then the train is read as built) / "Where to? This car needs a place after it." / "This train needs a caboose." / "This train asks a question. Which caboose asks?"
- event `whistle`: the whistle (sound) then "All aboard!"
- event `capital`: "Trace the capital. Start at the dot."
- event, whole, `hear`: the Cargo word, then the word said slowly and smoothly.
- event `tile`: "{m}, like {moon}." event `slotNo`: "Listen to the {start} of {sun}."
- event `ticket`: "A ticket for this station!"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
`kit/sentence-train.js` (the sentence-train family). No family doc exists and the only sibling, first-next-last (1), is a concept, so this spec describes the engine for both. Pure parts in one marked block, exposed as `__tool.st`.
- **Car**: `{id, text, kind: 'engine'|'name'|'do'|'where'|'describe'|'small'|'question'|'caboose', pic, plural}`.
- **Train**: an ordered list of cars; `st.say(train)` gives the text with spacing and the caboose mark; `st.read(train, onCar)` reads it aloud lighting each car.
- **Check**: `st.check(train, rules)` returns the first problem from an ordered rule list: `engine`, `capital` (first word and the word "I"), `name`, `do`, `order` (simple patterns: [small] [describe] name do [where small? name]; question: question-word [do/is] ...), `where` (a where car must have a thing after it), `caboose`, `endFits` (question mark for a question-word engine). A tool picks which rules apply (first-next-last swaps in `sequence` rules for steps).
- **Target**: an optional target sentence for a picture; `st.matches(train, target)` for stations with one right train, and `st.works(train)` for free building.
- **Trace**: `st.trace(letter, path)` scores a traced capital against a stroke guide (within a tolerance, strokes in order).
- **Depart**: the leaving animation and whistle, with a Motion off fade.
This tool uses all parts. Not first-next-last's `sequence` rules.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Who and Do | Couple every car | The yard always has a second doing car and a second naming car; a train must match its picture (`matches`), so "The dog sleeps runs." fails on order and "The dog sleeps." fails the picture. |
| One or More | Always pick the longest word; always pick the middle length | The longest car is always wrong (catses, boxeses); the middle length is right in every set, so the cars are shown in a shuffled order and spoken only, with no word printed until a pick, which leaves the ear to decide. |
| Where | Guess | 1 in 3, and pictures pair (on and in the same box) so the picture, not the box, decides. |
| Ask It | Always pick What | Each question word is right once (computed); the caboose step follows. |
| Capital and End | Capitalize every car; always pick the period | Only the broken car can be tapped to fix; the three caboose fixes need three different marks (period, exclamation point, question mark), so one mark is right once. |
| Cargo | Guess tiles | Six tiles, three slots in order: 1 in 120 (computed); wrong tiles share letters with the picture word's look-alikes (b and d, m and n). |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a station: `station`, `welcome` (queued, first time), the station's how line, then the picture's prompt.
2. Car taps read at once; `Go!` plays `need` (and the shake) or `whistle` then `read` (whole).
3. Capital and End: the fix pick, then `capital`, then the trace; then `Go!`.
4. Cargo: `hear` (whole), tile taps play `tile`, `Go!` plays `slotNo` or the new car's word.
5. `ticket` after a station's sixth train.
No line contains a bare letter sound: letters are only said by name with a picture word, and words are said whole or slowly as one word.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| L.K.1 a to f and L.K.2 a to d wording (print upper- and lowercase letters; frequently occurring nouns and verbs; regular plural nouns orally with /s/ or /es/; question words; frequently occurring prepositions such as to, from, in, out, on, off, for, of, by, with; produce and expand complete sentences; capitalize the first word and the pronoun I; recognize and name end punctuation; write a letter for most consonant and short-vowel sounds; spell simple words phonetically) | thecorestandards.org, Language K | CCSS ELA 2010 PDF, Language Standards K-5 | yes |
| Plural rule: add -es after s, x, z, ch, sh (boxes, foxes, dishes); -s otherwise | Merriam-Webster, "Plural" usage guide | Purdue OWL, "Plurals" | yes |
Backed twice: 2. Cut: 0.

Checks run (Python, scratchpad b4, 2026-11-08): Ask It question words each right once; Capital and End caboose fixes one per mark; Cargo 6 x 5 x 4 = 120 tile orders, and no wrong tile spells the word another way by sound; One or More: longest always wrong, middle always right; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 a station's picture, train and yard show with no scroll; at 680x425 the same, yard in one row.
2. Who and Do: each of the six trains leaves only as its target; a missing doing car gives the doing-car line. (L.K.1b, L.K.1f)
3. One or More: only the right plural car is taken; the sentence "I see two {boxes}." is read. (L.K.1c)
4. Where: only the right where car leaves with each picture. (L.K.1e)
5. Ask It: only the right question word and the question mark caboose leave. (L.K.1d, L.K.2b)
6. Capital and End: each of the six broken trains leaves only when fixed; traced capitals pass the guide. (L.K.1a, L.K.2a, L.K.2b)
7. Cargo: each word is spelled only by its three tiles in order and becomes a car. (L.K.2c, d)
8. Grow the Train: each grown sentence leaves and is read; a describing car after the naming car gives the order line. (L.K.1f)
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Pre-reader: every car, tile and sign is spoken. Motion off: trains fade instead of chugging; no network requests; nothing saved.

## Open questions
- None for Cory.

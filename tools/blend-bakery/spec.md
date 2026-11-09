# Blend Bakery

## One idea
A busy little bakery where every order is a word: a customer says what they want (a ship cookie!), the baker lines up sound jars on the tray in order (sh, i, p), and the oven blends whatever is on the tray into one word and says it out loud, so a missing or swapped jar comes out of the oven as a different word (sip, chip, hip) that the customer did not order; counters add magic-e muffins, vowel-team tarts, two-layer cakes, endings and tricky words that can't be baked by sound at all.

## Not like
- rhyme-time-rumble (k, spec): listen-only sound bouts with no print. Here print: jars with letters and letter teams, decoding and spelling words.
- sentence-train (k, spec): building sentences from word cars. Here building words from sound jars.
- nonsense-words (2, built): a calm drill reading made-up words one at a time. Here real words ordered by customers, built and baked, in fast replayable rounds.
- sight-words (2, built): plain practice of sight-word lists. Here tricky words are one counter among many and are picked by look, not drilled.
- letter-lanterns (k, draft): one letter and its sound at a time. Here letter teams, blends, final e and two-syllable words.

## Who and how
- Grade 1, ELA, module "Phonics: Blends and Digraphs" (Foundational Skills). Standards: RF.1.2 (a to d), RF.1.3 (a to g).
- Driver: a child alone, a pair, or the class on a projector (tool.json `driver: "either"`). Every order is spoken and pictured; every jar plays its sound clip when tapped.
- Seven counters, any order: `Digraph Donuts`, `Blend Buns`, `Magic-e Muffins`, `Team Tarts`, `Two-Layer Cakes`, `Ending Eclairs`, `Tricky Treats`; then `Rush Hour`, a 90-second mix. tool.json `modes: ["Counters", "Rush Hour"]`, `minutes: "5-10"`, `grades_label: "Grade 1"`.
- Saved: only the best Rush Hour score and which counters are done, in this browser on this device (localStorage), shown as a sentence on the Rush Hour card; `Clear` removes it. Nothing else. (BASELINE rule 7.)

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RF.1.2a | Magic-e Muffins: hear an order and decide if it has a long or short vowel (cap or cape), then add or leave off the e jar | two muffin tins (short, long) | 4 |
| RF.1.2b | The oven blends the tray's sound clips into one word; Blend Buns orders have consonant blends (fr, st, cl, mp, nd) | the oven, the word on the box | 3 |
| RF.1.2c | When an order comes out wrong, hear the first, middle or last sound of the word ordered and fix that jar | the jar that changed glows | 2, 3 |
| RF.1.2d | Every order: hear the whole word and pick the jars for all its sounds in order | the tray with slots | 2, 3 |
| RF.1.3a | Digraph Donuts: sh, ch, th, wh and ck jars | jars with two letters | 2 |
| RF.1.3b | Read the box: the baked word's label is read by the child before the oven says it | the box label | 2 |
| RF.1.3c | Magic-e Muffins and Team Tarts: the e jar and vowel-team jars (ai, ay, ee, ea, oa) | the e sprinkle; team jars | 4, 5 |
| RF.1.3d, e | Two-Layer Cakes: each layer holds one syllable and needs one vowel jar; build each layer, then stack | two cake layers, one vowel spot each | 6 |
| RF.1.3f | Ending Eclairs: add -s, -ed or -ing to a base word to match the order | the base eclair and three ending jars | 7 |
| RF.1.3g | Tricky Treats: hear a tricky word and pick the box with its label from three | three labeled boxes | 8 |

## Screens and modes
Header (kit): title "Blend Bakery"; mode tabs `Counters` and `Rush Hour`; `Read`, `Motion`, `Sound`. Controls 60 px or more at 1366x768 (44 px at 680x425), icon plus word.

**On load and first tap.** The bakery front: seven counters with picture signs, Baker Bea the badger in an apron behind them, and a customer at the door. First hint: "Pick a counter. Tap Digraph Donuts to start." The first tap opens the counter with its line; the welcome is queued after it (`welcomeAfter: true`).

**A counter.** Focus: the customer (left, with a speech bubble showing the order's picture), the tray (center, 700 x 140, three to five slots), the oven (right), and the pantry shelf below (eight to ten jars, each 96 x 96 with its letters; tap to hear its sound clip). The order is spoken ("One ship, please!"); `Hear it again` repeats it. Drag jars to slots (or tap a jar to drop it in the next empty slot); tap a slot to empty it. `Bake` (oven icon): the tray slides into the oven, the jars' sounds play smoothly together as one word, the box comes out with the word's label, and the child reads it (`Read it` waits 3 s, then the oven says it). Right: the customer cheers, a coin drops, next customer. Wrong: the customer looks puzzled: "That's a {chip}. I asked for a {ship}." Then the jar that differs glows and its place is named: "Listen to the start of {ship}." with the sound clip of the ordered word's first sound. Six orders per counter.

**Magic-e Muffins.** Each order is a muffin with a long or short vowel. First pick the tin: `Short` (a little muffin) or `Long` (a tall muffin); then build; the e jar is a sprinkle shaker. A long order without an e bakes the short word ("You baked a {cap}. I wanted a {cape}!").

**Two-Layer Cakes.** Two trays, one per layer, each with one marked vowel spot. Build the bottom layer, then the top; `Stack` bakes the two layers together and says the word.

**Ending Eclairs.** The base word is already baked (a jump eclair). The order is a sentence ("Yesterday, the frog ___."); pick the ending jar (-s, -ed, -ing) and `Bake`.

**Tricky Treats.** No jars: "This one can't be baked by sound. Find the box that says {said}." Three boxes with labels, one right and two look-alikes.

**Rush Hour.** Customers from every counter for 90 seconds with a patience bar each; coins and a streak. `Relaxed` (default on for the class) turns patience off. At the end, the score and the best score.

At 1366x768 the customer, tray, oven and pantry fit above the fold. At 680x425 jars are 60 px and the pantry is two rows.

## Content
Each order: word (picture) | jars on the tray | pantry extras (the near-word jars first).

**Digraph Donuts**: ship (sh, i, p | s, h, ch, a); chop (ch, o, p | sh, c, a, t); thin (th, i, n | t, h, f, a); whip (wh, i, p | w, sh, ch, o); duck (d, u, ck | k, c, b, o); fish (f, i, sh | s, h, ch, a).

**Blend Buns**: frog (f, r, o, g | d, l, a); stop (s, t, o, p | t, a, sh); clap (c, l, a, p | k, i, b); drum (d, r, u, m | b, n, o); nest (n, e, s, t | t, ck, a); hand (h, a, n, d | m, b, e).

**Magic-e Muffins** (tin, word): long cape; short pin; long hope; short cub; long kite; short tap. Pantry each: the base word's jars, e, and two extras.

**Team Tarts**: rain (r, ai, n | ay, a, e); play (p, l, ay | ai, a, ee); feet (f, ee, t | ea, e, i); seat (s, ea, t | ee, e, a); boat (b, oa, t | o, d, ai); green (g, r, ee, n | ea, e, n). Note on the order bubble for ee and ea words: the picture decides which spelling the customer wants (feet, not feat; seat, not seet), and when a child bakes a real word with the other team (feat for feet), the customer says "That's {feat}, a big brave deed. I want {feet} for my socks."

**Two-Layer Cakes**: rabbit (rab + bit); napkin (nap + kin); sunset (sun + set); cupcake (cup + cake); picnic (pic + nic); muffin (muf + fin). The vowel spots must hold a vowel jar.

**Ending Eclairs** (sentence; base; ending; the word): "Yesterday, the frog ___." jump, -ed, jumped. "Look! The dog is ___." dig, -ing, digging (the oven adds the second g and says why once). "Every day, Sam ___ the plants." water, -s, waters. "The cat ___ the yarn yesterday." pull, -ed, pulled. "We are ___ a cake." bake, -ing, baking (the oven drops the e and says why once). "The bird ___ every morning." sing, -s, sings.

**Tricky Treats** (word | two look-alikes): said | sad, sand; was | saw, wax; of | off, if; come | came, cone; one | on, own; could | cold, cloud.

**Sound clips** (recorded separately as clean isolated sounds, no added "uh", held sounds about 0.8 s): every consonant and short vowel used above, sh, ch, th (voiceless and voiced), wh, ck, the long vowels for ai, ay, ee, ea, oa and the magic-e words, and the endings /s/, /z/, /t/, /d/, /ed/ and "ing". Every order word and baked word (including every near word the pantry can make) is a whole-word clip.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- `Bake` is on once every slot is full. The oven blends by playing the jars' clips with overlap, then plays the whole-word clip of what was built; if the tray spells no real word, the oven says "Hmm, that's not a word I know," and plays the blended clips only.
- A wrong bake names one place (first, middle or last sound) and plays the ordered word's sound clip for that place; it never plays a bare letter name.
- Two-Layer Cakes: a layer with no vowel jar won't stack ("Every layer needs a vowel.").
- Ending Eclairs: doubling and dropping rules are shown, not tested: the oven makes the change and says it once.
- Coins: one per right bake; three in a row lights a streak bell. Nothing is lost for a wrong bake.
- Counters done get a ribbon (saved on this device).

## Look
- Accent `--brand` #a8325e deep rose (header, awning stripes, oven door); gold #f6c94a (coins, ribbons); jars by kind, each with a shape as well as a tint: consonant jars round, vowel jars tall, team jars double, ending jars short and wide; paper #fff8f6; ink #2a1219; muted #6b5058. Scene: a warm little bakery with an awning.
- Contrast (WCAG 2.1, computed): white on brand 6.40:1; brand on paper 6.10:1; ink on paper 16.69:1; muted on paper 6.87:1; ink on gold 11.15:1. Jar letters are ink on pale tints, each at least 7:1 (checked at build).
- Never color alone: jar kinds have shapes; the vowel spot on a cake layer has a dotted ring and the word "vowel".
- Different from this batch (plum, airmail blue, storybook green, savanna) and the K-2 ELA neighbors.

## Art
Local FLUX (`scripts/localart.py`); no people.
- bakery (1): "A warm little bakery with a rose striped awning, counters and an oven, soft gouache, no text"; 16:9; cutout no.
- bea (stand, cheer, point, think: 4): "A friendly badger baker in an apron and chef hat, <standing / cheering / pointing / thinking>, soft gouache, plain white background"; 1:1; cutout yes.
- customers (6 animals x 2 moods = 12): "A <rabbit / goat / hedgehog / duck / mouse / bear> customer, <happy / puzzled>, soft gouache, plain white background"; 1:1; cutout yes.
- order pictures (about 40, the order words and their near words that are picturable): "<subject>, simple soft gouache icon, plain white background"; 1:1; cutout yes.
About 57 images. Drawn in code: jars, trays, oven, boxes, cake layers, coins, every control.

## Voice
Bank voice `upbeat-guide` as Baker Bea; customers' lines in the same voice. Not used by the rest of this batch. Sound clips are separate recordings (see Content). `Curio.voice` with `scope: () => state.counter + ':' + state.order`, `welcomeAfter: true`.
- event `counter`: "{Digraph Donuts}!"
- how `welcome`: "Welcome to Blend Bakery! Every order is a word. Line up the sound jars, and the oven blends them."
- how per counter (once): Digraph "Some jars hold two letters that make one sound." Blend "Two sounds side by side, and you hear them both." Muffins "Short or long? Listen to the middle." Tarts "Two letters team up for one long sound." Cakes "Every layer needs a vowel." Eclairs "Add an ending to match the sentence." Tricky "These words don't follow the rules. Find them by how they look."
- event, whole, `order`: "One {ship}, please!" (Eclairs: the sentence; Tricky: "Find the box that says {said}.")
- event `jar`: the jar's sound clip (clip, not voice).
- event, whole, `bake`: the blended clips, then the word.
- event `readIt`: "Can you read the box?"
- event `yes`: "Yum! A {ship}!" event `wrong`: "That's a {chip}. I asked for a {ship}." then "Listen to the {start} of {ship}." and the clip.
- event `noWord`: "Hmm, that's not a word I know."
- event `noVowel`: "Every layer needs a vowel."
- event `rule`: "The e steps out when ing comes in." / "We double the g to keep the vowel short."
- event `streak`: the bell.
- event `rushEnd`: "Rush hour's over! {12} orders!"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Build an order | Drag jars at random | Six or seven jars and three or four ordered slots: at least 120 ways (computed; Team Tarts is smallest); the pantry holds the jars of near words (sip and chip at the ship order, feat at the feet order), so a near miss bakes a real but wrong word, said aloud. |
| Read the box | Wait for the oven | The oven waits 3 s; reading first is not checked, which is honest: the read step is practice, not a test. |
| Magic-e tin | Always pick Long | Three long and three short (computed); a wrong tin bakes the other word. |
| Two-Layer Cakes | Put one vowel in one layer | A layer with no vowel won't stack, so every cake makes the child find both vowels. |
| Ending Eclairs | Always -ed | Each ending fits two sentences and the time word decides (computed: -ed 2, -ing 2, -s 2). |
| Tricky Treats | Pick the box with the first letter heard | Each set's look-alikes share the first letter or most letters (said, sad, sand), so only the whole shape decides. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a counter: `counter`, `welcome` (queued, first time), the counter's how line, then `order` (whole).
2. Jar taps play `jar` at once.
3. `Bake`: `bake` (whole), `readIt`, then after 3 s the word, then `yes` or `wrong` (and the clip), or `noWord` / `noVowel` / `rule`.
4. Rush Hour: orders back to back; `streak`; `rushEnd`.
Isolated sounds are only ever heard as recorded sound clips, never inside a spoken line.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RF.1.2 a to d and RF.1.3 a to g wording (long and short vowels; blend sounds including consonant blends; isolate initial, medial vowel and final sounds; segment into phonemes; digraphs; decode one-syllable words; final -e and common vowel teams; every syllable has a vowel sound; two-syllable words; inflectional endings; irregularly spelled words) | thecorestandards.org, RF Grade 1 | CCSS ELA 2010 PDF, Foundational Skills K-5 | yes |
| Spelling changes: double the final consonant after a short vowel before -ing (dig, digging); drop silent e before -ing (bake, baking) | Merriam-Webster, "Spelling rules: doubling final consonants" | Reading Rockets, "Spelling: adding suffixes" | yes |
Backed twice: 2. Cut: 0. The ee/ea homophone pairs (feet, feat; seat; meet, meat) are dictionary facts checked in Merriam-Webster.

Checks run (Python, scratchpad b5, 2026-11-08): every order word is its tray jars in order; ship pantry holds sip and chip, feet pantry holds feat; Magic-e long 3, short 3; endings 2 each; ordered ways per pantry (120 to 840, smallest 120); contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the customer, tray, oven and pantry show with no scroll; at 680x425 with two pantry rows.
2. Digraph Donuts: each order bakes right only from its jars in order; a wrong bake names one place and plays the right clip. (RF.1.2c, RF.1.2d, RF.1.3a, RF.1.3b)
3. Blend Buns: the oven's blend of the four-jar words plays smoothly and says the word. (RF.1.2b)
4. Magic-e Muffins: only the right tin and the e (for long) bake right. (RF.1.2a, RF.1.3c)
5. Team Tarts: only the right team jar bakes right; a homophone bake gets its own line. (RF.1.3c)
6. Two-Layer Cakes: layers without a vowel won't stack; each cake bakes right only as its two syllables. (RF.1.3d, e)
7. Ending Eclairs: each sentence takes only its ending; the doubling and dropping lines play once. (RF.1.3f)
8. Tricky Treats: each takes only its box. (RF.1.3g)
9. Rush Hour: 90 seconds, Relaxed turns patience off; the best score is kept on this device and Clear removes it; no network requests.
10. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one. No bare letter sound in any spoken line.

## Open questions
- None for Cory.

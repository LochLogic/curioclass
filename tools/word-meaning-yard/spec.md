# Word Meaning Yard

## One idea
A farmyard where every place sorts words a different way: sentences go into the pen of the meaning they use (a duck that swims, a goat that ducks), word endings change a picture (pig, pigs; lock, unlock), farm things go into bins and the class says why, opposites meet across the fence, words are found at home, and Rocco the rooster walks, marches, struts, prances, tiptoes and stomps so the class can act out how close words differ.

## Not like
- vocabulary-jar (k-2, spec): new words from read-alouds, worked out from clues and reused. Here familiar words sorted by meaning, form and relation.
- context-clue-hunt (1, concept): working out a silly word from clues. Here no clues: the sort is the thinking.
- word-zoo (1, concept): sorting words by part of speech into habitats. Here meanings, endings, categories, opposites and shades.
- rhyme-time-rumble (k, spec): sounds. Here meanings.
- alike-and-different-books (k-2, spec, same format): sorting picture cards into hoops by book. Here pens and bins by meaning.

## Who and how
- Kindergarten, ELA, module "Word Meanings and Word Play" (Language). Standards: L.K.4 (a, b), L.K.5 (a, b, c, d).
- Driver: teacher on a projector (tool.json `driver: "teacher"`); the class says each answer, a helper drags or taps; in Strut Stage the class stands and acts. Every word, sentence and card is spoken and every card is a picture, so a child alone can play (BASELINE rule 4).
- Six places on the yard map, any order: `Two Meanings Pond`, `Endings Shed`, `Feed Bins`, `Opposites Fence`, `Home Words Porch`, `Strut Stage`. tool.json `modes: []`, `minutes: "5-10"` per place, `grades_label: "Kindergarten"`.
- Not a personal prompt (Home Words asks about things, not family). Nothing is saved.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| L.K.4a | Two Meanings Pond: hear sentence cards for one word (duck, bat, bark, ring, fly) and drag each into the pen that shows the meaning it uses | two pens with a picture of each meaning; sentence cards with a speaker | 2 |
| L.K.4b | Endings Shed: hear a word with an ending or beginning (-s, -ed, re-, un-) and pick the picture that shows what the change means | three pictures; a code-drawn strip for -ed (before, after) and re- (done, undone, done again) | 3 |
| L.K.5a | Feed Bins: sort twelve farm things into Animals, Foods and Tools, then pick why one belongs | three bins; the reason cards | 4 |
| L.K.5b | Opposites Fence: drag each picture to its opposite across the fence (big, small; full, empty; open, shut; wet, dry; fast, slow; push, pull) | two rows on a fence; joined pairs | 5 |
| L.K.5c | Home Words Porch: pick the thing you might find at home that is soft, shiny, loud, cold, colorful or bumpy, then name one from your own home aloud | three pictures; the word's card | 6 |
| L.K.5d | Strut Stage: act out walk, march, strut, prance, tiptoe and stomp with Rocco, then pick which Rocco is doing the named one | three Roccos moving side by side | 7 |

## Screens and modes
Header (kit): title "Word Meaning Yard"; `Yard` (map icon); `Read`, `Motion`, `Sound`. Every control is 60 px or more at 1366x768 (44 px at 680x425), icon plus word.

**On load and first tap.** The yard map (painted, 1046 x 640): a pond, a shed, feed bins, a fence, a porch and a little stage, each with a code sign (picture plus word). Rocco the rooster stands at the gate. First hint: "Pick a place in the yard. Tap the pond to start." The first tap on a place opens it with its own line (`place`); the welcome is queued after it (`welcomeAfter: true`). Places done get a corn-cob badge.

**Two Meanings Pond.** Focus: two pens (each 440 x 300) with the meaning picture on the gate (duck: a duck swimming / a goat ducking under a branch), and four sentence cards (a speaker icon and a number, 140 x 100) in a row below. Tap a card to hear its sentence; drag it (or tap it, then a pen) into a pen. Right: it stays, the sentence is read again. Wrong: it slides back, "Listen again. Which {duck} is it?" After four, the next word. Five words.

**Endings Shed.** Focus: the word's base picture on the shed door (240 px) and three picture choices (200 px). "This is {pig}. Now listen: {pigs}. Which picture shows {pigs}?" -ed and re- choices are small three-frame strips (code frames around painted pictures) so before and after can be seen. Right: the change is said in whole words ("Pigs. More than one pig."). Wrong: "That shows {one pig}. Listen to the end: {pigs}." Eight words.

**Feed Bins.** Focus: three bins (Animals with a hoof icon, Foods with a spoon, Tools with a hammer; 300 x 260) and twelve picture cards above. Drag each to a bin; a card is read on tap. A wrong bin: the card bounces back and "Is a {shovel} something to eat?" After all twelve: four `Why?` questions ("Why is the apple with the Foods?") with three reason cards; right: "Yes, you can eat it!"

**Opposites Fence.** Focus: a fence with six pictures on the left rails and six on the right (shuffled), 150 px each. Tap or drag a left picture onto its opposite: both words are said ("Full. Empty. Opposites!") and the pair hops onto the gate. Wrong: "{Full} and {wet}? Those aren't opposites." and the cards stay.

**Home Words Porch.** Focus: the word card (a big picture of the describing word: a feather for soft) and three home pictures. "Which one at home is {soft}?" Right: "Yes! A pillow is soft." then "What else at your home is soft? Say it out loud!" and `We said one!`. Six words.

**Strut Stage.** Focus: a small stage with Rocco. Learn: Rocco does each way of walking for 3 s while the word and its meaning are said; the class stands and does it with him (`Do it with Rocco`). Then Show me: three Roccos side by side each loop a different way; "Which Rocco is {strutting}?" Right: that Rocco takes a bow. Six words; the Learn loop for any word can be replayed with its picture button.

At 1366x768 every place's focus and cards fit above the fold. At 680x425: pens 300 x 200, cards 90 px; Feed Bins shows six cards at a time with arrows; the fence shows three rows of pairs.

## Content
**Two Meanings Pond** (word: meaning A picture / meaning B picture; sentences A, A, B, B):
- duck: a duck swimming / a goat ducking under a branch; "The duck swims in the pond." "A duck says quack." / "Duck under the branch!" "We duck when the ball flies by."
- bat: a bat flying at night / a baseball bat; "The bat sleeps upside down." "A bat flies at night." / "Hit the ball with the bat." "Hold the bat with two hands."
- bark: a dog barking / tree bark; "The dog's bark is loud." "I heard a bark next door." / "The tree's bark is rough." "A bug crawled on the bark."
- ring: a gold ring / a bell ringing; "The ring is shiny gold." "The ring fits on my finger." / "Ring the bell!" "The phone will ring soon."
- fly: a housefly / a bird flying; "A fly buzzed by my ear." "The fly landed on the jam." / "Birds fly south." "Planes fly high."

**Endings Shed** (base, heard word: right picture | two others):
1. pig, pigs: three pigs | one pig | a pig eating
2. hen, hens: two hens | one hen | a hen's egg
3. kick, kicked (strip): the goat's foot down, the ball flying away | the ball at the goat's foot (about to kick) | the goat asleep
4. roll, rolled (strip): a muddy pig beside a mud patch with roll marks | a clean pig at the edge of the mud | a pig eating
5. fill, refill (strip): a full bucket, empty, full again | a bucket filling once | a bucket tipping over
6. paint, repaint (strip): a painted fence, faded, painted again | a bare fence being painted | a fence being washed
7. lock, unlock: a key turning and the gate swinging open | a key locking the gate shut | a key hanging on a hook
8. tie, untie: a knot coming loose | a knot being tied | a coil of rope

**Feed Bins**: Animals: cow, hen, pig, goat. Foods: corn, apple, carrot, bread. Tools: shovel, rake, bucket, hammer. Why questions (right | two others): apple in Foods (You can eat it. | It is red. | It is round.); shovel in Tools (You use it to do a job. | It is long. | It is in the barn.); goat in Animals (It is alive and can move and eat. | It is white. | It lives on a farm.); bread in Foods (You can eat it. | It is soft. | It is brown.).

**Opposites Fence** pairs: big pig / small piglet; full bucket / empty bucket; open gate / shut gate; wet dog / dry dog; fast horse / slow turtle; push a wheelbarrow / pull a wagon.

**Home Words Porch** (word: right | two others): soft: a pillow | a rock | a fork. shiny: a spoon | a sock | a paper bag. loud: an alarm clock ringing | a feather | a sleeping cat. cold: ice cubes | a cup of cocoa | a warm blanket. colorful: a box of crayons | a white plate | a gray stone. bumpy: a pinecone | a smooth plate | a balloon.

**Strut Stage** (word: how Rocco does it, and the meaning line):
- walk: ordinary steps. "Walk: just going along, one foot, then the other."
- march: even steps, knees high, wings swinging, like a parade. "March: strong, even steps, like in a parade."
- strut: chest out, head high, slow proud steps. "Strut: walk proudly, chest out, like you're the best."
- prance: springy, bouncy, high little steps. "Prance: bounce and spring with every step."
- tiptoe: up on toe tips, slow and quiet. "Tiptoe: quietly, up on your toes."
- stomp: heavy, loud steps, feet slapping down. "Stomp: big, heavy, noisy steps."
Show me sets (named | two others): strut | walk, march; prance | tiptoe, strut; march | stomp, walk; tiptoe | prance, stomp; stomp | march, tiptoe; walk | strut, prance.

## Interactions in detail
- Every tap acts at once; a card tap during a line reads that card and stops the line. Drag or tap-then-target both work everywhere.
- Wrong drops never count against anyone; nothing is scored. Each place's corn badge appears when every item is right.
- Two Meanings: a word's four cards are shuffled; the next word comes after all four are right.
- Feed Bins: Why questions come after all twelve are sorted.
- Strut Stage: the three loops in Show me play side by side and keep looping until a pick; Motion off shows each Rocco's pose sequence as three still poses with arrows (the poses differ clearly: chest out, knees high, on tiptoes, bouncing).
- Home Words: `We said one!` plays a cheer; not checked.
- `Yard` returns to the map; places keep their state until `Start over` (on the map).

## Look
- Accent `--brand` #9e2a2b barn red (header, signs' frames, the gate); gold #f2c94c (corn badges, Rocco's bow); paper #fdf8f0; ink #2a1a14; muted #6a5446. Scene: a sunny farmyard in soft gouache.
- Contrast (WCAG 2.1, computed): white on brand 7.45:1; brand on paper 7.04:1; ink on paper 15.81:1; muted on paper 6.69:1; ink on gold 10.53:1.
- Never color alone: right drops get a check; bins and signs have icons and words.
- Different from the K ELA neighbors (big-book-pointer is brick orange; this is deep barn red) and this batch (cobalt, emerald, slate, brown).

## Art
Local FLUX (`scripts/localart.py`); no people.
- yard-map: "A sunny farmyard seen from above with a pond, a small shed, three feed bins, a wooden fence, a porch and a little wooden stage, soft gouache, no signs"; 16:10; cutout no.
- rocco (6 ways x 2 frames, plus bow and stand = 14): "A proud red and gold rooster <walking / marching with knees high / strutting with chest out / prancing mid-bounce / tiptoeing / stomping>, <frame 1 / frame 2>, soft gouache, plain white background"; 1:1; cutout yes; the builder loops the two frames with a small bob (Motion off: still).
- meaning pictures (10, Two Meanings gates), endings pictures (24, Endings Shed choices and strip frames), feed pictures (12), opposite pictures (12), home pictures (18 plus 6 word cards), stage and place backdrops (pond pens, shed door, bins, fence, porch, stage: 6): "<subject>, soft gouache, plain white background" or full-frame for backdrops; 1:1 for objects, 16:9 for backdrops; objects cutout yes.
About 102 images, no people. Each earns its place as a sortable card; the builder lists them from Content. Drawn in code: signs, sentence cards, strips' frames, bins' icons, badges, every control.

## Voice
Bank voice `wise-mentor` (style "Say thoughtfully and warmly, like a wise high school mentor") as the narrator, Granny Goat, who runs the yard. Not used by K ELA neighbors or batches 1 and 2, nor the rest of this batch. `Curio.voice` with `scope: () => state.place + ':' + state.item`, `welcomeAfter: true`.
- event `place`: "The {pond}!"
- how `welcome`: "Welcome to the Word Meaning Yard. I'm Granny Goat. Every place here plays with words a different way."
- how per place (once): Pond "Some words mean two things. Listen to each sentence, then put it in the right pen." Shed "Little word parts change a word. Listen to the change." Bins "Sort the farm things. Animals, foods, or tools?" Fence "Find each picture's opposite across the fence." Porch "Let's find words at home!" Stage "Rocco walks in many ways. Stand up and do it with him!"
- event `sentence`: the card's sentence. event `penYes`: the sentence again. event `penNo`: "Listen again. Which {duck} is it?"
- event, whole, `endingAsk`: "This is {pig}. Now listen: {pigs}. Which picture shows {pigs}?" event, whole, `endingYes`: the meaning line, always in whole words ("{Pigs}. More than one {pig}." / "{Kicked}. The kick already happened." / "{Refill}. Fill it again." / "{Unlock}. The opposite of {lock}."). event `endingNo`: "That shows {one pig}. Listen to the end: {pigs}."
- event `item`: the card's word. event `binNo`: "Is a {shovel} {something to eat}?" event, whole, `whyAsk` / `whyYes` / `whyNo`: the question / "Yes! {reason}" / "That's true, but is that why?"
- event `pairYes`: "{Full}. {Empty}. Opposites!" event `pairNo`: "{Full} and {wet}? Those aren't opposites."
- event, whole, `homeAsk`: "Which one at home is {soft}?" event `homeYes`: "Yes! A {pillow} is {soft}. What else at your home is {soft}? Say it out loud!" event `homeNo`: "Is a {rock} {soft}?"
- event, whole, `learn`: the word and its meaning line. event, whole, `showAsk`: "Which Rocco is {strutting}?" event `showYes` / `showNo`: "Yes! That's {strutting}." / "That Rocco is {marching}. Look again."
- event `badge`: "A corn cob for you!"
Read speaks the hint, which names the current action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Two Meanings | Guess; put cards in alternate pens | Card numbers and order are shuffled; a word's four cards fit 2 and 2, so a random split is right 1 in 6; wrong drops slide back with the sentence read, so the fix is listening. |
| Endings | Guess; the picture that matches the base word | 1 in 3; each set has the base meaning (one pig, a key locking) as the common wrong answer. |
| Feed Bins | Sort by color or by where it is found | Colors mix across bins (a white goat, white bread; a red apple, a red hen's comb); everything is on a farm. Why questions include a true but wrong reason ("It lives on a farm."), so "true" does not pick. |
| Opposites | Pair by look (two buckets, two dogs) | Pairs do share a subject by design (that is the lesson: the same thing, the opposite way); the wrong pairs also share looks with other cards (the big pig and the fast horse are both large), and each pick is read aloud. Six pairs by chance 1 in 720 (computed). |
| Home Words | Guess | 1 in 3, with things found at home in every set, so "it's at home" does not pick. |
| Strut Stage | Pick the most active Rocco | Each word is right once and appears as a wrong option twice (computed), so no single look wins. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a place: `place`, `welcome` (queued, first place), the place's how line, then the first ask (whole where marked).
2. Each item: card taps read; a pick or drop plays its yes or no line; the next ask waits for the yes line.
3. Strut Stage: `learn` for each word in order (whole), then Show me: `showAsk` (whole), `showYes` or `showNo`.
4. `badge` after a place's last item.
No line contains a bare letter or letter sound: endings and beginnings are only ever heard inside whole words ("pigs", "refill"), and the meaning lines name the meaning, never the letters.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| L.K.4a, L.K.4b, L.K.5a-d wording (new meanings for familiar words; inflections and affixes such as -ed, -s, re-, un- as a clue; sort objects into categories; verbs and adjectives and their opposites; real-life connections; shades of meaning among verbs like walk, march, strut, prance, by acting them out) | thecorestandards.org, Language K | CCSS ELA 2010 PDF, Language Standards K-5 | yes |
| Meanings used: duck (bird; lower the head quickly), bat (animal; club), bark (dog's cry; tree's covering), ring (band; to sound a bell), fly (insect; move through air), strut (walk proudly), prance (spring with high steps), march (walk with regular steps), tiptoe, stomp | Merriam-Webster entries | Cambridge Dictionary entries | yes |
| Prefixes re- (again) and un- (opposite, not), suffixes -s (more than one) and -ed (past) | Merriam-Webster, prefix and suffix entries | Reading Rockets, "Root words, roots and affixes" | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad b3, 2026-11-08): Strut Stage sets: each word right once, wrong twice; Two Meanings random split 1 in 6; opposite pairs by chance 1 in 720; Feed Bins sorts 34,650 ways, one right; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 each place's pens, bins, fence or stage and its cards show with no scroll; at 680x425 the same with smaller cards (Feed Bins paged).
2. Pond: all 20 sentence cards go only into their meaning's pen. (L.K.4a)
3. Shed: all eight take only their right picture, and the meaning of the change is said. (L.K.4b)
4. Bins: all twelve sort only into their bin; four Why questions take only their reason. (L.K.5a)
5. Fence: only the six opposite pairs join. (L.K.5b)
6. Porch: all six take only their home picture; We said one cheers. (L.K.5c)
7. Strut Stage: six Learn loops, then six Show me picks, each only right for its word; the six poses differ at a glance with Motion off. (L.K.5d)
8. Tap while it plays: a card tap during a line acts at once; no older line plays after a newer one.
9. Pre-reader: every word, sentence and card is spoken; every card is a picture.
10. Motion off: no loops or hops, same pacing; no network requests; nothing saved.

## Open questions
- None for Cory.

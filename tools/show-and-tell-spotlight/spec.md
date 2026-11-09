# Show and Tell Spotlight

## One idea
A little stage with a real spotlight: Ziggy the hedgehog goes first, and the class lights a star for each kind of detail they actually heard (how it looks, feels, sounds, where, when, who, why I like it), fixes Ziggy's half-sentences, and picks the right way to talk to each listener; then a child takes the spotlight with their own drawing and recording, the class lights stars for what they heard, and the child tells it again for a new listener to light more.

## Not like
- owl-wants-more (k-2, spec): an owl asks questions and written details are added to a story. Here details are spoken, and the class listens for them and lights them.
- class-phone-call (k-2, spec): the class asks a caller questions. Here the class is the audience of a speaker and judges what it heard.
- little-book-press (k-2, spec): records words onto book pages. Here the recording is a show and tell, told twice for two listeners.
- turn-and-talk-wheel (k, concept): a back-and-forth with a talk buddy. Here one speaker, one audience, and how talk changes for the listener.
- big-book-pointer, question-cube (same format): print rules; question words about a text. Here speaking and listening.

## Who and how
- Grades K-2, ELA, module "Show and Tell" (Speaking and Listening). Standards: SL.K.4, SL.K.5, SL.1.4, SL.1.5, SL.1.6, SL.2.4, SL.2.6, L.2.3 (L.2.3a).
- Driver: teacher on a projector (tool.json `driver: "teacher"`); the class votes by thumbs and a helper taps; in Your turn one child is the speaker. Every choice is a picture and every line is spoken, so a child alone can play Ziggy's turn and record their own (BASELINE rule 4).
- Steps in the `Show` menu: `Ziggy's shell`, `Ziggy's pond trip`, `Whole sentences`, `Who's listening?`, `Your turn`. tool.json `modes: []`, `minutes: "10-30"`, `grades_label: "Grades K-2"`.
- Privacy and disclosure: drawings and recordings stay on this device and are gone when the page closes (nothing is saved); Your turn says "Your drawing and voice stay on this device, and they're gone when you close the page." (BASELINE rule 7). A child may pick from the object shelf instead of bringing something personal (`Pick from the shelf` is always offered first). Teacher notes: a child's own object can lead to family or home stories; if a child shares something serious, thank them, move on gently and follow school procedure.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| SL.K.4, SL.1.4 | Listen to Ziggy describe a shell and light the detail stars heard; in Your turn, describe a thing, then add more detail when telling it again | seven star buttons with pictures; lit stars; the Ziggy check names each missed or extra star | 2, 7 |
| SL.2.4 | Listen to Ziggy recount a pond trip, light its stars, and put its three events in order; in Your turn, recount an experience | the three event cards and their numbered slots; the loudness meter while recording | 3, 7 |
| SL.1.6, SL.2.6 | Whole sentences: when a friend asks Ziggy for a detail, pick the whole-sentence answer, not the half-sentence | three spoken answers with sentence-shape pictures | 4 |
| L.2.3a | Who's listening?: pick the way to talk that fits the listener (friend or principal, family or a whole assembly) | the listener's painting; two openers | 5 |
| SL.K.5, SL.1.5 | Your turn: draw the object (or stamp it) to show details the words tell | the drawing pad in the spotlight beside the speaker's star board | 6 |

## Screens and modes
Header (kit): title "Show and Tell Spotlight"; `Show` (menu icon); `Read`, `Motion`, `Sound`. Every control is 60 px or more at 1366x768 (44 px at 680x425), icon plus word.

**On load and first tap.** The stage (painted: velvet violet curtains, a wooden stage edge, an empty stool) with the spotlight off; Ziggy peeks from behind the curtain. First hint: "Ziggy is ready to go first. Tap Lights up!" The first tap on `Lights up!` (spotlight icon, gold, 120 px) turns on the spotlight, Ziggy walks to the stool, and `Ziggy's shell` starts with its own line; the welcome is queued after it (`welcomeAfter: true`).

**Ziggy's shell and Ziggy's pond trip (listening).**
- Focus: the stage with Ziggy in the spotlight holding the shell (or, for the pond trip, a painted memory bubble that shows each part as he tells it), and under it the star board: seven star buttons (130 x 130), each a gold star with a picture inside: Looks (an eye), Feels (a hand), Sounds (an ear), Where (a map pin), When (a clock), Who (two faces), Why I like it (a heart). Each star's name is spoken on tap.
- Ziggy tells it (`tell`, whole, about 20 s). `Hear it again` (ear) replays it. The class votes on each star by thumbs; the helper taps stars to light or unlight them. `Check` (magnifier): every star right glows and Ziggy says the words that earned it ("You heard where: at the beach!"); a missed star pulses with "I said {it}: listen again"; an extra lit star wiggles with "Did I say how it sounds?". Right stars stay lit; the board can be fixed and checked again.
- Pond trip adds `Order it`: three event cards (painted: the frog on a lily pad; the frog jumping with a plop; Ziggy and his dad eating apples on a log) and three slots, 1, 2, 3; drag or tap a card then a slot. `Check` tells which are in place; Ziggy retells using first, next, then.
- 1366x768: header 56, stage 400 (Ziggy cutout 300 tall, all of him visible), star board 150: above the fold. At 680x425: stage 220, stars 80 px in one row.

**Whole sentences.** A friend (Bunny, in the front row cutout) asks Ziggy for a detail; Ziggy offers three ways to answer, each a card with a sentence-shape picture (a full train of word blocks for a whole sentence; a short train missing its engine or its cars for a half sentence; code-drawn) and spoken on tap. The class picks the whole-sentence answer. Right: Ziggy says it proudly, Bunny nods. Wrong: "That's only part of a sentence. Who did it? What happened?" (per item), the card dims. Six items in order.

**Who's listening?** A listener card comes into the spotlight's edge (painted animal listener). Ziggy has two openers, each on a card, read on tap. The class picks the one that fits. Right: the listener smiles; wrong: the listener looks puzzled and Ziggy says why ("For the principal, I use my school voice and polite words."). Six listeners.

**Your turn.**
- `Pick from the shelf` (12 painted objects: a pinecone, a toy car, a seashell, a teddy bear, a rock, a feather, a ball, a book, a leaf, a mitten, a toy dinosaur, a flower) or `My own thing` (a blank card).
- `Draw it` (pencil icon): the drawing pad (640 x 400) opens on the stage: pen with 6 colors and 2 sizes, eraser, `Clear` (with a confirm), and, for a shelf object, its picture as a faint guide to trace or ignore. The drawing then stands in the spotlight.
- `Record` (red dot, 120 px): the speaker tells it, up to 60 s; `Stop` ends it. While recording, the loudness meter (a bar that fills toward a picture of the back row's ears) moves with the voice, labeled "Can the back row hear you?"; it is a guide only (microphones differ). `Play` plays it back.
- The class listens and lights the stars it heard on the speaker's star board (unchecked: the class decides). The count shows under the board as lit stars, never a score.
- `Tell it again` (two arrows): pick a new listener card (the same six), record again, and light a second board. The two boards sit side by side ("First telling", "Second telling") so the class can see what was added and how the talk changed for the listener.
- Microphone refused: Record shows "Microphone off"; the speaker tells it live and the class still lights stars.

## Content
**Ziggy's shell** (description): "This is my shell. It is pink inside and white outside. It is about as big as my hand. It feels smooth on the inside and bumpy on the outside. I found it at the beach with my grandma." Stars: Looks (pink, white, as big as my hand), Feels (smooth, bumpy), Where (at the beach), Who (my grandma). Not said: Sounds, When, Why I like it.

**Ziggy's pond trip** (recount): "Last Saturday, I went to the pond with my dad. First, we saw a green frog on a lily pad. Next, the frog jumped into the water with a big plop! Then we sat on a log and ate apples. I liked it because the frog was so funny." Stars: When (last Saturday), Where (the pond), Who (my dad), Looks (a green frog), Sounds (a big plop), Why I like it (the frog was so funny). Not said: Feels. Order: frog on lily pad, frog jumps with a plop, apples on a log.

**Whole sentences** (Bunny's question | whole sentence | two half sentences):
1. Where did you find it? | I found it at the beach. | Found it at the beach with my grandma. / At the beach.
2. What color is it? | My shell is pink inside. | Pink inside. / My pink shell inside.
3. What did the frog do? | The frog jumped into the water. | Jumped into the water. / The big green frog into the cold water.
4. What did you eat? | We ate apples on a log. | Apples on a log. / Ate apples on a log by the pond.
5. How big is it? | It is as big as my hand. | As big as my hand, maybe even bigger. / It as big as my hand.
6. Why do you like it? | I like it because it is smooth. | Because it is smooth. / I like it because.

**Who's listening?** (listener | fits | does not fit, and why):
1. Bunny, your best friend, at recess | "Hey, Bunny! Look what I found!" | "Good morning. I would like to show you my shell." (too formal for a friend at play)
2. Principal Moose, visiting the class | "Good morning, Principal Moose. May I show you my shell?" | "Hey, check this out!" (a principal gets polite words)
3. Grandpa Badger, at home | "Grandpa! Guess what I found at the beach!" | "Hello, sir. Today I will present a shell." (family gets everyday talk)
4. The whole school at an assembly | "Hello, everyone. My name is Ziggy, and today I will show you my shell." | "Um, so, this shell, yeah." (a big audience needs a clear start)
5. A new student who doesn't know Ziggy | "Hi! I'm Ziggy. Want to see my shell?" | "It's me again! You know my shell." (they don't know you yet)
6. Mayor Bear, a visitor to the school | "Hello, Mayor Bear. Thank you for visiting. This is my shell." | "Yo, Mayor! Shell!" (a visitor gets polite words)

## Interactions in detail
- Every tap acts at once; a star, card or control tap during Ziggy's telling stops it (Hear it again restarts it).
- Star checks are exact: every star said must be lit and no other. Check can be pressed any number of times; after a Check, `Hear it again` plays the telling with each detail word glowing in its star's place (a short pulse on that star as the word is said) so the class can hear what they missed.
- Order it accepts drag or tap-then-slot; Check marks each card right or wrong.
- Whole sentences and Who's listening?: one pick checks; a wrong card dims and the item stays until the right pick; feedback plays before the next item.
- Your turn: recordings are kept for this page load only, at most two per speaker (first and second telling); `New speaker` clears both boards, the drawing and the recordings (with a confirm card). Nothing is written to storage.
- The `Show` menu opens any step at any time; each listening step keeps its lit stars until `Start over`.
- Motion off: no spotlight sweep, walking or wiggles; states change at once on the same timing.

## Look
- Accent `--brand` #5a2d91 velvet violet (header, curtains' trim, Record frame); gold #f6c445 (stars, Lights up!, the spotlight's warm edge); paper #fbf7ff; ink #1f1630; muted #5d5270. Scene: a cozy school stage, warm spotlight on violet curtains.
- Contrast (WCAG 2.1, computed): white on brand 9.46:1; brand on paper 8.95:1; ink on paper 16.33:1; muted on paper 6.83:1; ink on gold 10.61:1.
- Never color alone: lit stars glow and fill with their picture in full color; unlit stars are outlines with a faded picture; right and wrong get check and x icons.
- Different from this batch (teal, magenta, olive, red) and batch 1 (plum is red-purple; this is blue-violet with gold).

## Art
Local FLUX (`scripts/localart.py`); no people (Ziggy, his family and every listener are animals).
- stage: "A cozy school stage with violet velvet curtains, a wooden floor edge and a small stool in the middle, warm gouache, the stage center clear"; 16:9; cutout no; spotlight light drawn in code over it.
- ziggy-peek, ziggy-walk, ziggy-hold-shell, ziggy-tell, ziggy-proud, ziggy-oops: "A small friendly hedgehog in a striped scarf <peeking from behind a curtain / walking / holding up a pink seashell / talking with one paw raised / smiling proudly / scratching his head>, warm gouache, plain white background"; 3:4; cutout yes; on the stool in the spotlight, all of him visible.
- memory bubble scenes (3, also the Order it cards): "<a green frog on a lily pad on a pond / a frog jumping into a pond with a splash / a hedgehog and his father hedgehog eating apples on a log by a pond>, warm gouache"; 4:3; cutout no.
- shell: "A pink and white spiral seashell, warm gouache, plain white background"; 1:1; cutout yes.
- listeners (6): "<a bunny in a sweater / a tall moose in a tie / an old badger in a cardigan / rows of animal students on benches in a gym / a shy young fox with a backpack / a big friendly bear with a mayor's sash>, <looking happy> and <looking puzzled> poses, warm gouache, plain white background"; 3:4; cutout yes (12 images); at the stage edge, all visible.
- bunny-front-row: "A bunny sitting in a front row seat, seen from behind, raising a paw, warm gouache, plain white background"; 1:1; cutout yes.
- shelf objects (12): the twelve objects in Your turn, "A <object>, warm gouache, plain white background"; 1:1; cutout yes.
- ears-row: "A row of little animal ears seen from the back of a classroom, warm gouache, plain white background"; 4:1; cutout yes; the loudness meter's goal.
About 41 images, no people. Drawn in code: the spotlight, stars and their pictures, sentence-shape trains, the loudness bar, the drawing pad, every control.

## Voice
Bank voice `casual-peer` (style "Say casually and naturally, like a friendly teenager explaining something") as Ziggy, a big-kid hedgehog; the stage prompts are Ziggy's too. Not used by K-2 ELA neighbors or batch 1. `Curio.voice` with `scope: () => state.step + ':' + state.item`, `welcomeAfter: true`.
- event `lights`: "Lights up! Hi, everybody!"
- how `welcome`: "I'm Ziggy, and this is show and tell. When I talk, listen for my details. Every detail you hear lights a star."
- event, whole, `tell`: the telling (Content). how `starsHow`: "Which stars did you hear? Tap a star to light it. Then tap Check."
- event `star`: the star's name ("Looks." "Feels." ... "Why I like it.").
- event, whole, `checkRight`: "You heard {where}: {at the beach}!" (one per right star, in board order). event `checkMissed`: "I said {who}. Listen again!" event `checkExtra`: "Did I say {how it sounds}? Listen again." event `allStars`: "You heard every detail!"
- how `orderHow`: "Put my trip in order. What happened first?" event, whole, `ordered`: "First, we saw a frog. Next, it jumped in with a plop. Then we ate apples!"
- how `sentHow`: "Bunny asks me a question. Which answer is a whole sentence? Tap it."
- event, whole, `ask`: Bunny's question. event `card`: the card's words. event `sentYes`: Ziggy says the whole sentence. event `sentNo`: "That's only part of a sentence." plus the item's hint ("Who found it?", "What is pink?", "What did the frog do?", "Who ate?", "What is as big as my hand?", "Because of what?").
- how `listenerHow`: "Who's listening? Pick the way I should talk."
- event `listener`: "{Principal Moose} is listening." event `fitYes`: "That fits!" event `fitNo`: the reason (Content).
- how `yourHow`: "Your turn in the spotlight! Pick a thing from the shelf, or your own thing."
- how `drawHow`: "Draw your thing so everyone can see the details." how `recordHow`: "Tap Record and tell about it. Tap Stop when you're done."
- event `recorded`: "Great telling! Now everybody, which stars did you hear?"
- how `againHow`: "Tell it again, for someone new! Pick who's listening."
- event `micOff`: "The microphone is off. Tell it out loud, and we'll still light stars."
Read speaks the hint, which names the current action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Detail stars (shell, pond) | Light all seven; light none; guess; light the stars that fit the object | Checks are exact: light-all has 3 extra for the shell and 1 for the pond, light-none misses 4 and 6 (computed); a random set passes 1 in 128; lighting what a shell "usually" has fails, because the board asks what Ziggy said (he says Who for the shell, and never says when). Each wrong star is named, so the fix comes from listening again. |
| Order it | Guess; the order the cards were shown | 1 in 6; cards are shuffled each time. |
| Whole sentences | Guess; the shortest or longest card; the one that repeats the question's words | 1 in 3 per item, all six by chance 1 in 729; the longest card is the whole sentence in only 2 of 6 items (computed: items 1, 3, 4 and 5 have a longer half sentence), the shortest in none; the sentence-shape pictures show the shape only after a pick; half sentences reuse the question's words too. |
| Who's listening? | Always pick the polite one; always pick the casual one | Fits are 3 casual (friend, grandpa, new student) and 3 formal (principal, assembly, mayor), so either habit gets 3 of 6; guessing all six 1 in 64. |
| Your turn stars | Light every star | Your turn is not checked or scored; the class decides, and two boards side by side show what the second telling added. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap Lights up!: `lights`, then `welcome` (queued), then `tell` (whole), then `starsHow`. Star taps play `star`. Check plays `checkRight` lines in board order, then `checkMissed`/`checkExtra`, or `allStars`.
2. Pond trip: as 1, then `orderHow`, then on a right order `ordered` (whole).
3. Whole sentences: `sentHow` (first), then per item `ask` (whole), card taps `card`, a pick `sentYes` or `sentNo`; the next `ask` waits for `sentYes`.
4. Who's listening?: `listenerHow` (first), then per item `listener`, card taps `card`, a pick `fitYes` or `fitNo`; the next `listener` waits.
5. Your turn: `yourHow`, `drawHow`, `recordHow`, `recorded` after Stop (or `micOff`), `againHow`.
No line contains a bare letter or letter sound.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| SL.K.4, SL.K.5, SL.1.4, SL.1.5, SL.1.6, SL.2.4, SL.2.6 wording (describe familiar people, places, things and events with details; add drawings or visual displays; produce complete sentences when appropriate to task and situation; tell a story or recount an experience with relevant details, speaking audibly in coherent sentences) | thecorestandards.org, Speaking and Listening K, 1, 2 | CCSS ELA 2010 PDF, Speaking and Listening Standards K-5 | yes |
| L.2.3a wording (compare formal and informal uses of English) | thecorestandards.org, Language grade 2 | CCSS ELA 2010 PDF, Language Standards K-5 | yes |
| A complete sentence has a subject and a verb and expresses a complete thought; a fragment lacks one of these | Purdue OWL, "Sentence fragments" | Merriam-Webster, "What is a sentence fragment?" | yes |
Backed twice: 3. Cut: 0. Ziggy, his tellings and the listeners are our own.

Checks run (Python, scratchpad b2/spot.py, 2026-11-08): star sets 4 and 6 of 7, light-all extras 3 and 1, light-none misses 4 and 6, random set 1 in 128; Order 1 in 6; Whole sentences all six by chance 1 in 729, longest card whole in 2 of 6; Who's listening? 3 casual and 3 formal, all six by chance 1 in 64; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the stage with all of Ziggy, and the whole star board, show with no scroll; at 680x425 the stage and one row of stars show.
2. Shell: only Looks, Feels, Where and Who check right; each missed or extra star gets its own line. (SL.K.4, SL.1.4)
3. Pond trip: only When, Where, Who, Looks, Sounds and Why check right; Order it takes only frog, plop, apples. (SL.2.4)
4. Whole sentences: each of the six takes only the whole sentence; wrong cards get the item's hint. (SL.1.6, SL.2.6)
5. Who's listening?: each of the six takes only its fitting opener, with the reason on a wrong pick. (L.2.3a)
6. Your turn: shelf or own thing, draw, record up to 60 s with the loudness meter, play back; the drawing stands in the spotlight. (SL.K.5, SL.1.5)
7. Tell it again: a second listener and recording, two star boards side by side; New speaker clears everything; nothing is saved after reload; the privacy line shows. (SL.K.4, SL.1.4, SL.2.4)
8. Tap while it plays: a star or card tap during Ziggy's telling acts at once and stops it; no older line plays after a newer one.
9. Pre-reader: every star, card, question and listener is spoken; every choice is a picture or has one.
10. Motion off: no spotlight sweep or walking, same pacing; a refused microphone leaves everything else working; no network requests.

## Open questions
- None for Cory.

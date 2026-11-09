# Word Zoo

## One idea
Every word is a little animal that needs the right home: naming words live in the meadow, doing words in the river, describing words in the trees and joining words in the burrow, and the class must say why each one belongs; then the animals put on a show where the stage acts out exactly what the words say, so the spotlights count the animals the verb asks for (hops lights one, hop lights many) and the sky shows the time the verb tells (hopped turns it to yesterday's sunset), and a sentence only gets its applause when the lights and sky match the picture.

## Not like
- sentence-train (k, spec): coupling word cars in order to build a sentence. Here the words are given; the class sorts word kinds and picks the form that agrees in number and time.
- word-meaning-yard (k, spec): sorting by meaning (a duck that swims, a goat that ducks), endings and opposites. Here sorting by word kind, and agreement.
- postcard-writer (1, spec): capitals, commas and spelling heard in a friend's reading. Here grammar shown on a stage with lights and sky.
- who-said-that (1, spec, same format): sorting lines to speakers. Here words to habitats.
- context-clue-hunt (1, spec): meaning from nearby words. Here kind and form, not meaning.

## Who and how
- Grade 1, ELA, module "Grammar Basics" (Language). Standard: L.1.1.
- Driver: teacher on a projector or a pair at one device (tool.json `driver: "either"`). Every word is read on tap and every pick has a picture, so a pre-reader can play (BASELINE rule 4).
- Two parts: `Zoo` (the sort, 18 word animals) and `Show` (three acts: Agree, Time, Join). tool.json `modes: []`, `minutes: "10-20"`, `grades_label: "Grade 1"`. Nothing is saved.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| L.1.1b | Sort naming words to the meadow; for sam and max, tap the first letter to give it a capital because it names one special someone | the meadow; a crown on the capital | 2, 3 |
| L.1.1f, L.1.1g | Sort describing words to the trees and joining words to the burrow, and pick why each belongs | the trees and burrow; the "Why here?" picks | 2 |
| L.1.1c, L.1.1d | Agree act: pick the verb form that matches one or many (The frog hops, The frogs hop, He jumps, They jump) | spotlights: one or many lit | 4 |
| L.1.1e | Time act: pick the verb that matches the time sign (Yesterday, Today, Tomorrow) | the sky: sunset, noon, sunrise | 5 |
| L.1.1g, L.1.1j | Join act: pick the joining word that makes two short sentences one | a rope bridge joins two sentence rafts | 6 |

## Screens and modes
Header (kit): title "Word Zoo"; `Zoo`, `Show`; `Read`, `Motion`, `Sound`. Controls 60 px or more at 1366x768 (44 px at 680x425), icon plus word.

**On load and first tap.** The zoo gate with Keeper Gus the gorilla (cap and keys). First hint: "Tap the gate to open the zoo." The first tap opens it with its own line; the welcome is queued after it (`welcomeAfter: true`).

**Zoo.** Focus: a zoo map with four habitats, each 300 x 260 at 1366x768 (meadow with grass, river with water, trees with branches, burrow with a hole), and the arrival cart at the bottom carrying the next word animal (a small creature holding a word sign, 160 x 160). Tap the animal to hear its word in a short sentence ("hop. Frogs hop."). Drag it (or tap it, then a habitat) home. Right home: the animal settles in and Gus asks "Why does it live here?" with four picture picks (a box with a label: "It names someone or something"; a running figure: "It tells an action"; a paint brush: "It tells what something is like"; a rope knot: "It joins two ideas"). Right reason: a paw-print stamp. Wrong home: the animal waddles back to the cart and Gus says what that home is for. For sam and max in the meadow, Gus says "This one names one special someone. Tap the first letter to give it a capital." The letter grows a little crown and becomes S or M.

**Show.** A stage with two spotlights rigs (one light at center, three lights across) and a sky backdrop (sunset, noon, sunrise). Each item shows a picture and a sentence with one gap; two word animals hold the picks. Pick one: the stage acts it out. Agree: hops lights one spotlight, hop lights three; the picture's animal count must match. Time: the sky changes to the time the verb tells and must match the time sign on the left. Join: the joining word becomes a rope bridge between two sentence rafts; the right one holds and the animals cross, the wrong one sags and Gus reads the whole sentence so it sounds wrong. Each act ends with applause and a star when 4 of 5 (or 7 of 8) were right the first time; wrong ones come back once at the end of the act.

At 1366x768 the map or the stage fits above the fold. At 680x425 habitats are 200 x 170 and the stage shrinks.

## Content
**Zoo (18 word animals; the short sentence read on tap):**
- Meadow (naming): dog (A dog barks.), girl (The girl runs.), park (We play at the park.), sam (Sam is my friend.), max (Max is my dog.)
- River (doing): hop (Frogs hop.), eat (We eat lunch.), sing (Birds sing.), read (I read books.)
- Trees (describing): big (a big bear), red (a red ball), soft (a soft bunny), happy (a happy kid)
- Burrow (joining): and (cats and dogs), but (small but strong), or (milk or juice), so (I was cold, so I put on a hat.), because (I smiled because it was sunny.)
The cart brings them mixed, never two from one habitat in a row (fixed order in the data).

**Show, Agree (picture | sentence | right | other):**
1. one frog | The frog ___. | hops | hop
2. three frogs | The frogs ___. | hop | hops
3. a boy | He ___. | jumps | jump
4. two kids | They ___. | jump | jumps
5. a group with "we" arrow | We ___. | sing | sings
6. a girl | She ___ an apple. | eats | eat
7. a child with "I" arrow | I ___ a book. | read | reads
8. Max and Mia | Max and Mia ___. | swim | swims
Right is the first pick 4 times and the second 4 times (data order: right second on 2, 3, 6, 7).

**Show, Time (time sign | sentence | right | others):**
1. Yesterday | Yesterday the seal ___. | jumped | jumps, will jump
2. Today | Today the seal ___. | jumps | jumped, will jump
3. Tomorrow | Tomorrow the seal ___. | will jump | jumped, jumps
4. Tomorrow | Tomorrow the bird ___. | will play | played, plays
5. Yesterday | Yesterday the bird ___. | played | plays, will play
Time items have three picks (three word animals).

**Show, Join (rafts | right | other):**
1. The lion was tired. / He took a nap. | so | or
2. I like apples. / I do not like pears. | but | so
3. Do you want milk? / Do you want juice? (joined: Do you want milk or juice?) | or | because
4. The monkey ate a banana. / The monkey ate an orange. (joined: The monkey ate a banana and an orange.) | and | because
5. The duck is wet. / It swam in the pond. | because | or
Each joining word is right once.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A word animal can be tapped any time to hear its word and sentence. Dragging needs a 12 px move; a tap-then-tap path works for every drag.
- "Why here?" takes one pick; a wrong reason shows the right one and the stamp is gray. The zoo star counts animals homed and reasons right on the first try (shown as paw prints, 18 each).
- The capital step only appears for sam and max; tapping any other letter says "Tap the first letter."
- Show picks: one tap; the stage acts it out for 2 s (Motion off: a still frame), then the next item. No timer.
- `Start over` (Zoo or Show) asks once, then resets.

## Look
- Accent `--brand` #9a4f0e savanna brown (header, signs, frames); gold #f4c542 (stars, crowns, stamps); habitat tints (meadow green, river blue, tree olive, burrow tan) each with its own shape and icon; paper #fdf8f1; ink #2a1a0c; muted #69594a. Scene: a sunny cartoon zoo.
- Contrast (WCAG 2.1, computed): white on brand 6.00:1; brand on paper 5.68:1; ink on paper 15.88:1; muted on paper 6.35:1; ink on gold 10.32:1.
- Never color alone: habitats differ by shape, texture and icon; spotlights by count; the sky by sun position and a word label (Yesterday, Today, Tomorrow).
- Different from this batch (rose, plum, airmail blue, storybook green) and the grade 1 and K neighbors.

## Art
Local FLUX (`scripts/localart.py`); no people (the two kids, boy and girl pictures in the Show are simple animal-kid characters, drawn as young bears and rabbits, so no people art).
- zoo map (1): "A top-down cartoon zoo map with a meadow, a river, a grove of trees and a burrow hill, soft gouache, no text"; 16:9; cutout no.
- Keeper Gus (3, stand, point, cheer): "A friendly gorilla zookeeper with a cap and a ring of keys, <standing / pointing / cheering>, soft gouache, plain white background"; 1:1; cutout yes.
- word animals (18): "A small cute <animal> holding a blank wooden sign, soft gouache, plain white background" (animals vary: lamb, rabbit, hedgehog, otter, duckling, beaver, frog, fish, koala, parrot, sloth, owl, mole, badger, chipmunk, prairie dog, raccoon, meerkat); 1:1; cutout yes. Sign text is drawn in code.
- Show pictures (13, one per Agree and Time item; Join uses rafts drawn in code): "<one frog / three frogs / a bear cub jumping / two rabbit kids jumping / ...>, soft gouache, plain white background"; 1:1; cutout yes.
- stage (1): "A small cartoon outdoor stage with curtains, empty, soft gouache, no text"; 16:9; cutout no.
About 36 images. Drawn in code: signs, habitat outlines, spotlights, sky, rafts and bridge, crowns, stamps, controls.

## Voice
Bank voice `gravel-ranger` as Keeper Gus (unique in this batch). `Curio.voice` with `scope: () => state.part + ':' + state.item`, `welcomeAfter: true`.
- event `gate`: "The zoo is open!"
- how `welcome`: "Welcome to the Word Zoo! Every word animal needs the right home. Tap one to hear it, then drag it home."
- event, whole, `word`: "{hop}. {Frogs hop.}"
- event `home`: "Home sweet home." how `why`: "Why does it live here? Tap the reason."
- event `whyYes` / `whyNo`: "That's it!" / "This one {tells an action}."
- event `wrongHome`: "The {meadow} is for words that {name someone or something}. Try another home."
- how `capital`: "This one names one special someone. Tap the first letter to give it a capital."
- event `crown`: "Now it's {Sam}, with a capital!"
- event `zooDone`: "Every animal is home!"
- how `showHow`: "Pick the word that matches the picture. The stage will act it out."
- event, whole, `sentence`: the full sentence with the pick in it.
- event `agreeNo`: "One {frog}, but {three} lights. Does that match?"
- event `timeNo`: "The sign says {yesterday}, but the sky says {tomorrow}."
- event `joinNo`: "{The lion was tired, or he took a nap.} Does that sound right?"
- event `applause`: applause (sound) and "Take a bow!"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Zoo sort | Try every habitat until one holds | It homes the animal, but the paw print counts first tries only, and "Why here?" must also be right. |
| Why here? | Always the same reason | Each reason is right for at most 5 of 18 animals. |
| Agree | Always the first pick | Right is first on 4 of 8. Guessing: 7 or more of 8 by chance is 9 in 256 (computed). |
| Agree | Always the -s form | Right on 3 of 8 only. |
| Time | Always the -ed form | Right on 2 of 5 only. Guessing three picks: 4 or more of 5 is 11 in 243 (computed). |
| Join | Always "and" | It is a pick on only one item. Guessing two picks: 4 or more of 5 is 6 in 32 (computed); the star also needs the zoo done. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the gate: `gate`, `welcome` (queued, first time).
2. Tap a word animal: `word` (whole).
3. Drop at home: `home`, `why`; then `whyYes` or `whyNo`; for sam and max then `capital`, `crown`. Wrong home: `wrongHome`.
4. All home: `zooDone`.
5. Show: `showHow` (first time), then per pick `sentence` (whole) and `agreeNo`, `timeNo` or `joinNo` when wrong; end of act `applause`.
No line contains a bare letter or letter sound ("the first letter", never the letter name alone).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| L.1.1 wording, including b, c, d, e, f, g and j | thecorestandards.org, Language Grade 1 | CCSS ELA 2010 PDF | yes |
| Conjunction: a word that joins words or word groups (and, but, or, so, because) | Merriam-Webster, "conjunction" | Purdue OWL, "Conjunctions" | yes |
| Proper nouns (names of particular people, pets and places) begin with a capital | Merriam-Webster, "proper noun" | CCSS L.1.2a (capitalize dates and names of people) | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad b5, 2026-11-08): habitat counts (5, 4, 4, 5 = 18), most animals per reason 5; Agree right-first count 4 of 8 and -s right 3 of 8; Time -ed right 2 of 5; Join each word right once; guessing odds 9/256, 11/243, 6/32; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the four habitats and the cart show with no scroll; at 680x425 the same, smaller.
2. Each of the 18 animals homes only in its habitat, and "Why here?" takes only its reason. (L.1.1b, f, g)
3. sam and max take a capital only on the first letter, and show S and M after. (L.1.1b)
4. Agree: each of the 8 items takes only its right form, and the spotlight count shows one or many. (L.1.1c, d)
5. Time: each of the 5 items takes only its right verb, and the sky matches the verb. (L.1.1e)
6. Join: each of the 5 items takes only its joining word, and the whole joined sentence is read. (L.1.1g, j)
7. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
8. Pre-reader: every word, sentence and pick is read on tap; habitats and reasons have pictures.
9. Motion off: still frames for the show and no waddling; no network requests; nothing saved.

## Open questions
- None for Cory.

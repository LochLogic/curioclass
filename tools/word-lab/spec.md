# Word Lab

## One idea
In Dr. Oyelaran's word lab, words are made by pouring parts together (re + tell, bird + house, add + -ition), and every new word is an experiment: the class predicts what it means from a row of pictures before it glows, tests the guess in a sentence, and checks it in the lab glossary, so the notebook fills with words grouped by the part that did the work; at the end the class invents a word the lab has never made (unjumpy) and defines it from its parts alone, and a measuring tube lines up words like toss, throw and hurl by how strong they are.

## Not like
- context-clue-hunt (1, spec): a silly word's meaning from clues around it. Here meaning from a word's own parts, then checked in context and a glossary.
- vowel-team-tag (2, spec): prefixes and suffixes peeled off for reading. Here for meaning.
- word-meaning-yard (k, spec): sorting by meaning and acting out walk, march and strut. Here prefixes, compounds and roots, with shades measured on a tube.
- root-detective-cards (4, concept, same family): Greek and Latin roots. Here grade 2 parts: prefixes, compounds and root words.
- word-family-tree (12, spec, same family): word histories on a tree. This tool uses the shared engine at its simplest.

## Who and how
- Grade 2, ELA, module "Word Parts and Meanings" (Language). Standards: L.2.4 (a to e), L.2.5 (a, b).
- Driver: a pair at one device or the teacher on a projector (tool.json `driver: "either"`). Every part, word and sentence is read on tap; prediction picks are pictures (BASELINE rule 4).
- Benches: `Prefix Bench`, `Compound Bench`, `Root Bench`, `Shades Tube`, `Taste Test`, then `Mystery Word`. tool.json `modes: []`, `minutes: "15-20"`, `grades_label: "Grade 2"`. Nothing is saved.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| L.2.4b | Pour a prefix into a known word, predict the meaning from three pictures, test, check | the prefix beaker, the new word glowing | 2 |
| L.2.4d | Pour two small words into a compound and predict its meaning | the two beakers joining | 3 |
| L.2.4c | Root Bench: from a known root (add), predict a new word with it (addition, additional) in a sentence | the root's color running through each word | 4 |
| L.2.4a | Test every made word in a sentence: does the predicted meaning fit? | the test tube sentence with the word lit | 2, 3, 4 |
| L.2.4e | Check every made word in the lab glossary (alphabetical) and once in a kid dictionary entry | the glossary page; a dictionary card | 5 |
| L.2.5b | Shades Tube: line up close verbs and adjectives by strength | the measuring tube with marks | 6 |
| L.2.5a | Taste Test: tag real foods spicy, juicy, crunchy or sour, and say a time you tasted one | food cards and tags | 7 |
| L.2.4b, L.2.4d | Mystery Word: build a new word (un + jumpy, sock + boat) and pick its meaning from its parts | the lab's "never made before" flask | 8 |

## Screens and modes
Header (kit): title "Word Lab"; `Benches`; `Read`, `Motion`, `Sound`. Controls 60 px or more at 1366x768 (44 px at 680x425), icon plus word.

**On load and first tap.** A bright lab bench with Dr. Oyelaran in goggles and a rack of beakers. First hint: "Tap a bench to start an experiment." The first tap opens the bench with its line; the welcome is queued after it (`welcomeAfter: true`).

**The experiment loop (Prefix, Compound, Root benches).** Focus: two beaker racks (parts on the left, known words on the right, each beaker 120 x 160 with its part written on it), the mixing flask in the middle (240 x 300), and the lab notebook on the right.
1. Pour: drag a part beaker and a word beaker into the flask (or tap both). If the parts make a word the lab knows, the flask bubbles and the word appears on the flask, read aloud. If not, the flask fizzles: "The lab doesn't know that word. Try another mix." (unknown mixes are kept for Mystery Word).
2. Predict: three picture cards (a sad face, a happy face, a face that is not happy at all) with a short label each; tap one. No answer is shown yet.
3. Test: a sentence fills a test tube with the word lit ("Tia was unhappy when her kite broke."). Then "Does your guess fit the sentence?" with `Yes, it fits` and `No, let me change it`.
4. Check: the glossary page opens at the word's letter (the alphabet runs along the edge; the class taps the right letter tab to open it), and the word's entry shows its meaning and the parts. The prediction card turns gold if it matched; if not, the right card is shown and Dr. Oyelaran says which part did the work.
5. Record: the word drops into the notebook under the part that did the work (un-, re-, bird, house, add).

**Dictionary check.** Once per bench, the Check step uses a kid dictionary card instead of the glossary: guide words at the top (rerun, retire), the entry word, its parts and a numbered meaning; the class taps the meaning that fits the test sentence when there are two (light: not heavy | not dark).

**Shades Tube.** A tall measuring tube with marks from "a little" to "a lot". Word cards for one set (toss, throw, hurl; thin, slender, skinny, scrawny; giggle, laugh, roar; look, stare, glare). Drag each to a mark; tap any card to hear it in a sentence with a little scene (a girl tosses a ball gently; a pitcher hurls it hard). `Check` lights the right order; wrong cards slide. For adjectives, a note: some shades are kind words and some are not (slender sounds nicer than scrawny); Dr. Oyelaran says so once.

**Taste Test.** Food cards (lemon, watermelon, chili pepper, celery, pickle, orange, pretzel, peach) and four tags (spicy, juicy, crunchy, sour); tag each food (some take two). Then "Tell your partner a time you tasted something {juicy}." Nothing is recorded.

**Mystery Word.** The flask shows "never made before". The class pours from a special rack (un-, re-, -less, -ful and words like jumpy, sock, boat, snow, sleep) to make one of six made-up words: unjumpy, reshoe, sockboat, snowless, sleepful, rehop. Then they pick its meaning from three pictures, using only the parts (unjumpy: a calm frog). The notebook stamps it "Invented by us".

At 1366x768 the racks, flask and notebook fit above the fold. At 680x425 the notebook becomes a tab.

## Content
**Prefix Bench** (part + word = made word | three predictions, right first | test sentence):
- un + happy = unhappy | not happy | very happy | happy again | "Tia was unhappy when her kite broke."
- re + tell = retell | tell again | not tell | tell first | "Can you retell the story to your partner?"
- un + lock = unlock | open the lock | lock again | lock it tight | "Dad used a key to unlock the door."
- re + paint = repaint | paint again | not paint | paint a little | "We will repaint the old red fence."
- dis + agree = disagree | not agree | agree again | agree a lot | "My brother and I disagree about the best pizza."
- pre + heat = preheat | heat before | heat again | not heat | "Preheat the oven before you bake."
On screen the right prediction sits at positions 2, 1, 3, 3, 2, 1 for these six.
**Compound Bench:** bird + house = birdhouse; light + house = lighthouse; house + fly = housefly; book + shelf = bookshelf; note + book = notebook; book + mark = bookmark. Predictions are pictures (a little house for birds | a bird that lives in a house | a house shaped like a bird).
On screen the right compound picture sits at positions 1, 3, 2, 2, 3, 1.
**Root Bench:** add: addition (adding numbers), additional (added, extra). help: helper, helpful, helpless. play: player, playful, replay.
**Glossary:** every made word in ABC order with its parts and meaning; written for Curio Class.
**Shades sets** (order from a little to a lot): toss, throw, hurl. giggle, laugh, roar. look, stare, glare. thin, slender, skinny, scrawny (the order follows the tool's glossary: slender and thin are close; the tube accepts thin and slender in either of the first two marks).
**Taste Test tags:** lemon: sour, juicy. watermelon: juicy. chili pepper: spicy. celery: crunchy. pickle: sour, crunchy. orange: juicy. pretzel: crunchy. peach: juicy.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The prediction locks before the test; it can be changed only at the "Does your guess fit?" step.
- Each made word appears once in the notebook; pouring it again just rereads it.
- Fizzled mixes are listed in the Mystery Word rack if they are among the six; others are not saved.
- The Shades Tube accepts the data order, with stated ties (thin and slender).
- Stars per bench: all words made and checked; a second star for predictions that matched on the first try.

## Look
- Accent `--brand` #5a3d8a lab purple (header, beaker labels, flask glow); gold #f4c542 (matched predictions, stars, the "never made before" flask); paper #f8f6fc; ink #1d1530; muted #5a5170. Scene: a bright, tidy lab bench.
- Contrast (WCAG 2.1, computed): white on brand 8.50:1; brand on paper 7.93:1; ink on paper 16.29:1; muted on paper 6.88:1; ink on gold 10.74:1.
- Never color alone: prefixes, words and roots differ by beaker shape (flask, cup, tall tube); the root's color in Root Bench also has an underline.
- Different from this batch (rain blue, wine table, velvet red, playground orange).

## Art
Dr. Oyelaran is a person, so the scientist art goes to Gemini; everything else is local FLUX (`scripts/localart.py`).
- lab (1): "A bright tidy cartoon science lab bench with beakers and a notebook, soft gouache, no text"; 16:9; cutout no.
- Dr. Oyelaran (4, Gemini: pour, think, cheer, point): "A friendly Black woman scientist in goggles and a lab coat <pose>, warm storybook gouache, plain white background"; 1:1; cutout yes.
- prediction and compound pictures (about 40): "<a birdhouse / a lighthouse / a housefly / a calm frog / ...>, simple soft gouache icon, plain white background"; 1:1; cutout yes.
- shades scenes (13): "<a girl tossing a ball gently / a pitcher hurling a ball hard / ...>, soft gouache"; 4:3; cutout no.
- foods (8): "<a lemon / a slice of watermelon / ...>, simple soft gouache icon"; 1:1; cutout yes.
About 66 images. Drawn in code: beakers, flask, bubbles, tube, glossary, dictionary card, notebook, controls.

## Voice
Bank voice `science-narrator` as Dr. Oyelaran (unique in this batch). `Curio.voice` with `scope: () => state.bench + ':' + state.step`, `welcomeAfter: true`.
- event `bench`: "{Prefix Bench}. Goggles on!"
- how `welcome`: "Welcome to my word lab! Pour two parts together. Then we predict, test and check, like real scientists."
- event `made`: "We made {unhappy}!"
- event `fizzle`: "The lab doesn't know that word. Try another mix."
- how `predict`: "What do you think {unhappy} means? Tap a picture."
- event, whole, `test`: the test sentence. how `fits`: "Does your guess fit the sentence?"
- how `check`: "Let's check the glossary. Tap the letter tab where {unhappy} would be." (the letter tab is tapped, never said alone)
- event `match` / `noMatch`: "Your prediction matched!" / "{Unhappy} means {not happy}. The part {un} did the work." ({un} is a recorded clip of the whole prefix)
- event `shadeHow`: "Put each word on the tube from a little to a lot."
- event, whole, `shadeSay`: the word in its sentence.
- event `kind`: "Some words are kinder than others. Slender sounds nicer than scrawny."
- how `taste`: "Tag each food. Then tell your partner a time you tasted something {juicy}."
- event `mystery`: "A word nobody has made before! What could it mean? Use its parts."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
`kit/wordlab.js`, described in tools/word-family-tree/spec.md, exposed as `__tool.wl`. This tool uses Morphemes (prefixes, compound parts and roots at grade 2 level, each with a kid meaning), Word records (with a `test` sentence and `glossary` line added for this tool), Split (to color the part that did the work), Build (the flask: `wl.build` returns the made word or nothing), Lookup (the kid dictionary card), and Guess and verify (the prediction step, here checked against the record because grade 2 needs a right answer). Not Tree view, Card view, Strategy log or Road key. The Shades Tube and Taste Test are tool code.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Pour | Pour everything | Only real words bubble; there is no score for pours. |
| Predict | Always the first picture | Right picks are placed by data, at most 3 of 6 per bench in one spot (computed). |
| Test | Always "Yes, it fits" | The check that follows shows the right meaning either way; the star counts predictions, not test answers. |
| Glossary tab | Tap tabs in order | It works, slowly; the alphabet strip teaches the order it relies on. |
| Shades Tube | Random | 3 words: 6 orders, 1 right; 4 words: 24 orders, 2 accepted with the tie (computed). |
| Mystery Word | Any picture | Three pictures: the right one follows the parts; wrong ones get "Which part tells you {not}?" |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a bench: `bench`, `welcome` (queued, first time).
2. Pour: `made` or `fizzle`; `predict`; `test` (whole) then `fits`; `check`; `match` or `noMatch`.
3. Shades: `shadeHow`, `shadeSay` (whole) on each tap, `kind` once.
4. Taste: `taste`. Mystery: `mystery`, then `match` or `noMatch`.
No line contains a bare letter or letter sound; prefixes are spoken as whole recorded clips.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| L.2.4 and L.2.5 wording, including the examples (happy/unhappy, tell/retell; addition, additional; birdhouse, lighthouse, housefly, bookshelf, notebook, bookmark; spicy or juicy; toss, throw, hurl; thin, slender, skinny, scrawny) | thecorestandards.org, Language Grade 2 | CCSS ELA 2010 PDF | yes |
| Prefix meanings: un- and dis- (not), re- (again), pre- (before) | Merriam-Webster, entries for un-, dis-, re-, pre- | Reading Rockets, "Root words, roots and affixes" | yes |
| Slender is approving, scrawny and skinny can be unkind | Merriam-Webster, "slender" and "scrawny" (usage) | Collins English Dictionary, "scrawny" | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad b7, 2026-11-08): six prefix words, six compounds, three root families; prediction right-position counts per bench; shades orders 3! = 6 and 4! = 24 with 2 accepted; the six mystery words are not in the made-word list; contrast as in Look. At build: confirm each mystery word is not a Merriam-Webster entry.

## Done when
1. Focus and fold: at 1366x768 racks, flask and notebook fit with no scroll; at 680x425 the notebook is a tab.
2. Prefix Bench: each listed mix makes its word; predictions, test, glossary check and notebook work. (L.2.4a, b, e)
3. Compound Bench: each compound forms and checks. (L.2.4d)
4. Root Bench: each root family forms with its root highlighted. (L.2.4c)
5. The glossary opens only from the right letter tab; the dictionary card picks the meaning that fits. (L.2.4e)
6. Shades Tube: each set lights only in its order (thin and slender tie). (L.2.5b)
7. Taste Test: each food takes its tags. (L.2.5a)
8. Mystery Word: each of the six words forms and takes its meaning picture. (L.2.4b, d)
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: no bubbling or pouring animation (the word appears); no network requests; nothing saved.

## Open questions
- None for Cory.

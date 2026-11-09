# Story Blanks

## One idea
Word tiles ride past on a slow belt and the student grabs one for each blank in a silly story, where every blank names its job ("a word that acts", "more than one", "yesterday"), and when the finished story is read aloud a tile that can't do its job makes the narrator stumble and the sentence crack, then shows the fix, so the student hears what each kind of word does in a sentence while the silliness stays theirs.

## Not like
- word-zoo (1, spec): sorting word kinds into habitats. Here words doing jobs inside sentences, with the grade 3 forms (plurals, tenses, agreement, comparing, joining).
- contraction-crusher (2, built): smashing two words into one. Here choosing a word for its job.
- grammar-garage (4, concept): repairing sentences. Here building them on the fly.
- word-lab (2, spec): word parts and meanings. Here grammar.
- syllable-surgeon (3, spec): decoding long words. Here using words in sentences.

## Who and how
- Grade 3, ELA, module "Parts of Speech" (Language). Standard: L.3.1 (a to i).
- Driver: one student, or two sharing a screen in Race (tool.json `driver: "student"`). Every tile and sentence is read on tap.
- Nine rounds, one per part of L.3.1, each a story of 5 to 7 blanks. Two speeds: Calm (the belt waits when the student taps Pause, and tiles loop) and Quick (a gentle score for fit and speed). tool.json `modes: ["Calm", "Quick", "Race"]`, `minutes: "10-20"`, `grades_label: "Grade 3"`.
- Saving: the silliest correct story per round is kept in a "story book" in this browser (localStorage, try/catch); the line under it says "Your stories stay on this device." `Clear my stories` removes them.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| L.3.1a | Round 1: fill blanks labeled "names something", "acts", "describes", "tells how", "stands in for a name" with nouns, verbs, adjectives, adverbs, pronouns | the job label on each blank | 2, 3 |
| L.3.1b | Round 2: "more than one": regular and irregular plurals (cats, mice, geese, teeth) | the plural blank | 3 |
| L.3.1c | Round 3: "a feeling or idea" blanks for abstract nouns (bravery, friendship, childhood) | the idea blank | 3 |
| L.3.1d, e | Round 4: "yesterday", "today", "tomorrow" blanks with regular and irregular verbs (walked, ran, will swim) | time words on blanks | 3 |
| L.3.1f | Round 5: agreement: "the dogs ___" (bark, not barks); "Mia lost ___ hat" (her) | the subject lit with its blank | 3 |
| L.3.1g | Round 6: compare: taller, tallest, more slowly, most slowly | the "compare two" or "compare all" tag | 3 |
| L.3.1h | Round 7: glue words: and, but, so, because, when, after join two lines | two lines snapping into one | 4 |
| L.3.1i | Round 8: build a simple, a compound and a complex sentence from the same two lines | three sentence shapes side by side | 4 |
| L.3.1a to i | Round 9: mixed story | the read-aloud with stumbles fixed | 5 |

## Screens and modes
Header (kit): title "Story Blanks"; `Rounds`, `Story book`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A story stage with a belt of word tiles and Flip the frog, a game-show host with a bow tie. First hint: "Tap a round to get your first story." The first tap opens round 1 with its line; the welcome is queued after it (`welcomeAfter: true`).

**Round screen.** Focus: the story page (640 x 380) with blanks shown as labeled slots (the job in words and an icon). Under it, the belt (a strip 900 wide) carries tiles left to right at a slow speed (one tile every 1.5 seconds in Quick; in Calm, tiles drift and `Pause` stops them). Each round's belt has 18 tiles: the right kind for every blank, near misses (barks for "the dogs ___", mouses, runned), and other kinds. Tap or drag a tile to the lit blank. A tile can be swapped until `Read it`.

**Read it.** The narrator reads the story with the student's words. A tile that doesn't fit its job makes the narrator stop ("The dogs... barks? Hmm."), the sentence shows a crack, and a fix card offers the right form ("The dogs bark. More than one dog, so no s."). The student taps the fix or picks a different tile. Silly right picks are celebrated ("A purple mice? Grammar's perfect. Silly is fine!").

**Glue and shapes (rounds 7 and 8).** Two short lines sit apart; the student drags a glue tile between them and the lines snap into one (with a comma before and, but or so). Round 8 builds the same two lines three ways and labels the shapes simple, compound, complex.

**Race.** Two players share the screen, left and right blanks; the first to drop a fitting tile wins the blank. Only fit scores; a wrong drop costs nothing but time.

At 1366x768 the page and belt fit; at 680x425 the belt becomes a 3-row tile tray.

## Content
Nine stories written for Curio Class (e.g. "The Day the Goats Ran the Bakery", "My Pet Cloud", "Grandma's Rocket Garden"). Word bank per round from data (each tile has a kind, a form and a job set):
- Irregular plurals: mouse/mice, goose/geese, tooth/teeth, foot/feet, child/children, man/men, woman/women, sheep/sheep, fish/fish.
- Irregular past: run/ran, eat/ate, go/went, see/saw, take/took, sing/sang, swim/swam, fly/flew, draw/drew, write/wrote.
- Abstract nouns: bravery, friendship, childhood, kindness, freedom, joy, fear, honesty.
- Comparing: tall/taller/tallest, happy/happier/happiest, good/better/best, bad/worse/worst, slowly/more slowly/most slowly.
- Glue: and, but, so, or (coordinating); because, when, after, before, if, although (subordinating).

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Tiles are 120 x 56 with the word and a small kind icon only after the first round (round 1 hides icons, so the job is the clue).
- Belt speed is never fast; Motion off shows a still tray of tiles instead.
- Fit check per blank: kind, plus form where the blank asks for one (plural, past, comparing).
- Scores (Quick only) show stars for fit; speed adds a small bonus and never removes a star.

## Look
- Accent `--brand` #6a3fa0 game-show violet (header, slots, belt rails); gold #f4c542 (the lit blank, stars); paper #f8f5fc; ink #1d1230; muted #5c5470. Scene: a playful story stage with curtains and a conveyor belt.
- Contrast (WCAG 2.1, computed): white on brand 7.42:1; brand on paper 6.87:1; ink on paper 16.47:1; muted on paper 6.58:1; ink on gold 10.93:1.
- Never color alone: slot jobs are words plus icons; cracks come with the narrator's stop and a fix card.
- Different from this batch (block brick, trail green, fair red, clinic blue).

## Art
Local FLUX (`scripts/localart.py`); characters are animals.
- stage (1): "A playful cartoon story stage with curtains and a conveyor belt, soft gouache, no text"; 16:9; cutout no.
- Flip (4, host, laugh, oops, cheer): "A cheerful frog game-show host in a bow tie <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- spot pictures (about 60): "<a goose wearing a hat / a rocket made of carrots / ...>, sticker style, plain white background"; 1:1; cutout yes. Each noun tile has a spot picture that pops into the story's corner when used.
About 65 images. Drawn in code: belt, tiles, slots, cracks.

## Voice
Bank voice `lively-host` as Flip and as the narrator (unique in this batch). `Curio.voice` with `scope: () => state.round + ':' + state.blank`, `welcomeAfter: true`.
- event `round`: "Round {2}: more than one!"
- how `welcome`: "Welcome to Story Blanks! Every blank has a job. Grab a word that can do that job. Then we read it, and we'll hear if it works."
- event, whole, `tile`: the tile's word.
- how `fillHow`: "Grab a word for the lit blank. It needs {a word that acts}."
- event, whole, `readStory`: the story with the student's words.
- event `stumble`: "{The dogs... barks?} Hmm."
- event `fix`: the fix card.
- event `silly`: "Silly? Yes. Right? Also yes!"
- event `glue`: "Snap! Two lines, one sentence."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Blank fit | Grab any tile | About a third of tiles fit each blank's kind, and fewer fit its form; wrong ones crack on Read it with a fix card (checked per round). |
| Plural and past | Add -s or -ed to everything | Belts include mouses, gooses, runned, swimmed as near misses; they crack. |
| Agreement | Always pick the -s verb | Subjects mix singular and plural in every round 5 story (checked). |
| Glue | Any glue word | Each pair accepts the words that keep the meaning; "because" where "but" belongs gets "Does that make sense? Listen." |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a round: `round`, `welcome` (queued, first time), `fillHow`.
2. Tap a tile: `tile` (whole).
3. Read it: `readStory` (whole), with `stumble` and `fix` at cracks, then `silly` if earned.
4. Rounds 7 and 8: `glue` on each snap.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| L.3.1a to i wording | thecorestandards.org, Language Grade 3 | CCSS ELA 2010 PDF | yes |
| The irregular plurals and past tenses listed | Merriam-Webster entries | Cambridge Dictionary, grammar and entries | yes |
| Coordinating conjunctions (and, but, or, so) and subordinating conjunctions (because, when, after, before, if, although) | Cambridge Dictionary, grammar: conjunctions | Merriam-Webster, conjunction usage guide | yes |
Backed twice: 3. Cut: 0.

Flag: the fill-in-a-silly-story idea echoes a well-known commercial word game; the tool never uses its name, and the job-labeled blanks and the breaking read-aloud are the core.

Checks run (Python, scratchpad b10, 2026-11-08): all 9 irregular plurals differ from a plain -s form and all 10 irregular pasts from a plain -ed form; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the page and belt fit; at 680x425 the belt is a tray.
2. Round 1 blanks show jobs in words and accept the right kinds. (L.3.1a)
3. Rounds 2 to 6 check form as well as kind and crack on near misses. (L.3.1b to g)
4. Rounds 7 and 8 snap lines with glue and show three sentence shapes. (L.3.1h, i)
5. Read it reads the student's story with stumbles and fix cards.
6. Calm mode pauses the belt; Quick scores fit with stars; Race splits blanks.
7. The story book keeps the silliest correct story per round where storage works; `Clear my stories` removes them.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: a still tray replaces the belt; no network requests.

## Open questions
- None for Cory.

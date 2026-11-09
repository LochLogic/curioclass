# Context, Roots, Dictionary

## One idea
The student cracks locked academic words inside short science, history and math passages with three keys used in order (first the context around the word, then a Greek or Latin root, then a dictionary entry), writes a guess after each key, checks the guess against the dictionary at the end, and a strategy log shows which key cracked each word and which guess the dictionary proved wrong, so they learn to work out new words on their own and to check before trusting a guess.

## Not like
- tricky-word-lab (6-8, spec): roots to fix spellings. Here roots, context and dictionary for meaning.
- word-family-tree (12, spec): the history of words through languages. Here solving words in passages.
- word-thermometer (6, spec): connotation of near-synonyms. Here working out unknown words.
- glossary-makers (3-5, spec): building a passage's glossary. Here cracking words with three keys and a strategy log.
- root-detective-cards (4, spec): combining roots, grade 4. Here grade 6-8 academic words in subject passages.

## Who and how
- Grades 6-8, ELA across subjects, module "Academic Vocabulary Strategies" (Language). Standards: L.6.4 (a, b, c, d), L.6.6, L.7.4 (a, b, c, d), L.7.6, L.8.4 (a, b, c, d), L.8.6.
- Driver: one student (tool.json `driver: "student"`). Every passage and word is read on tap.
- Passages written for Curio Class: grade 6 "The Volcano Watchers" (science), grade 7 "Two Kings at War" (history), grade 8 "Shapes That Repeat" (math). tool.json `modes: ["Grade 6", "Grade 7", "Grade 8", "My glossary"]`, `minutes: "15-25"`, `grades_label: "Grades 6-8"`.
- Saving: the personal glossary is kept in this browser; footer and the My glossary panel: "Your glossary stays on this device." `Clear my glossary` removes it.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| L.6.4a, L.7.4a, L.8.4a | Use the Context key: find the clue in the sentence or nearby and name its type (definition, example, contrast, cause) | the clue lit and its type chip | 2 |
| L.6.4b, L.7.4b, L.8.4b | Use the Roots key: split the word and read the root's meaning (audi, hear; bell, war; ced, go) | the split word and root card | 3 |
| L.6.4c, L.7.4c, L.8.4c | Use the Dictionary key: pick the sense that fits from several, with pronunciation and part of speech | the entry with the chosen sense | 4 |
| L.6.4d, L.7.4d, L.8.4d | Check the guess against the chosen sense and mark it right, close or wrong | the guess, sense and verdict | 4 |
| L.6.6, L.7.6, L.8.6 | Write your own sentence with each cracked word; read a new passage that reuses them with no keys | the glossary and the final passage | 5 |

## Screens and modes
Header (kit): title "Context, Roots, Dictionary"; `Passage`, `My glossary`, `Strategy log`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A passage on a desk with three words locked behind small padlocks, and a key ring of three keys: Context, Roots, Dictionary. Professor Halvorsen, a retired lexicographer with reading glasses on a cord, sits at the next desk. First hint: "Tap the passage to hear it." The first tap reads the title; the welcome is queued after it (`welcomeAfter: true`).

**Passage.** About 200 words with three to four locked words. Grade 6 (volcano): hypothesis, magnitude, subsequent, audible. Grade 7 (two kings): belligerent, bellicose, concede, antebellum. Grade 8 (shapes): precede, recede, congruent, symmetry.

**Keys, in order.** Tap a lock:
1. Context: the student taps the words that help; the key glows if the passage has a keyed clue there and asks its type. The student writes a guess.
2. Roots (opens after a guess): the word splits with the word lab's Split (sub + sequ + ent; bell + i + cose; pre + cede); the root card gives the meaning and two family words. The student may refine the guess.
3. Dictionary (opens after the roots step or any time the student taps `Skip to dictionary`): a written-for-Curio-Class entry with pronunciation, part of speech and two or three senses; the student picks the sense that fits the passage.
The verdict compares the guess to the chosen sense: right, close or wrong. The student marks it; the tool shows the key's sense beside it so the student's mark can be checked.

**My glossary.** Each cracked word with the student's sentence (must use the word and be at least 6 words) and the key that cracked it.

**Strategy log.** The word lab's Strategy log: how often context was enough, where roots saved the day, and each guess the dictionary proved wrong.

**Final passage.** A short passage in a new subject that reuses the glossary words, read with no keys; the student answers two meaning questions.

At 1366x768 the passage and key panel fit side by side; at 680x425 the key panel is below.

## Content
- Three passages and a final passage written for Curio Class with keyed clue spans and types.
- 12 word records (parts, roots, family words, senses), built with the word lab's Morphemes and Word records from the etymologies in Sources.
- Dictionary entries written for Curio Class from the senses in two dictionaries.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Keys open in order but the dictionary can be reached by `Skip to dictionary`; the log records the skip.
- With Motion off locks open without turning.

## Look
- Accent `--brand` #1d4e89 roots blue (header, key ring, locks); gold #f4c542 (lit clues, open locks); paper #f1f5fb; ink #081a33; muted #4c5868. Scene: a quiet study desk.
- Contrast (WCAG 2.1, computed): white on brand 8.39:1; brand on paper 7.67:1; ink on paper 15.92:1; muted on paper 6.61:1; ink on gold 10.71:1.
- Never color alone: locks say "locked" or "open"; verdicts are words.
- Different from this batch (ivy green, cart amber, coaster magenta, rally orange).

## Art
- People art goes to Gemini: Professor Halvorsen (a Norwegian American woman in her seventies with reading glasses on a cord), 3 poses; "illustrated friendly retired professor <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): study desk with a key ring (1); volcano with a monitoring station (1); a medieval castle on a river map (1); a geometry workshop with tiles (1).
About 7 images. Drawn in code: locks, keys, split words, entries.

## Voice
Bank voice `calm-professor` as Professor Halvorsen (unique in this batch); passages are read by `science-narrator` (unique in this batch). `Curio.voice` with `scope: () => state.level + ':' + state.word + ':' + state.key`, `welcomeAfter: true`.
- how `welcome`: "Three keys, always in this order: context first, then roots, then the dictionary. Write a guess after each one."
- event, whole, `passage`: the passage.
- event `clue`: "A {contrast} clue. What's your guess?"
- event `root`: "{Bell}, from Latin. It means war."
- event `sense`: "Which sense fits this passage?"
- event `verdict`: "{Close}. You had the idea."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
word-lab (`kit/wordlab.js`, `__tool.wl`), described in full in tools/word-family-tree/spec.md. This tool uses: Morphemes, Word records, Split, Lookup (`wl.entry`, the dictionary key), Strategy log (`wl.log`) and Guess and verify. Not Build, Tree view or Card view. The context key and passages are tool-only code.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Keys | Skip straight to the dictionary | Allowed, but the log records it and the guess step is still required before the verdict. |
| Senses | Pick the first sense | For at least one word per passage the first sense is keyed wrong for that passage. |
| Glossary | Copy the definition | The sentence must use the word itself and at least 6 words; copied definitions are flagged when 4 or more words match the entry. |
| Final passage | Guess | Two meaning questions use the glossary words in a new subject. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the passage: title, `welcome` (queued, first time), then `passage` (whole) on Play.
2. Context: `clue`. Roots: `root`. Dictionary: `sense`, then `verdict`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| L.6.4, L.6.6, L.7.4, L.7.6, L.8.4, L.8.6 wording | thecorestandards.org, Language Grades 6-8 | CCSS ELA 2010 PDF | yes |
| belligerent from Latin bellum (war) and gerere (to wage); bellicose from Latin bellicosus | Wiktionary, belligerent and bellicose (checked 2026-11-09) | Merriam-Webster, etymologies | yes |
| precede from Latin prae- and cedere; recede from re- and cedere (to go) | Wiktionary, precede and recede (checked 2026-11-09) | Merriam-Webster, etymologies | yes |
| subsequent from Latin subsequens; audience from audire (to hear); magnitude from magnus; hypothesis from Greek hypo (under) and tithenai (to put) | Wiktionary, each entry (checked 2026-11-09) | Merriam-Webster, etymologies | yes |
| Context clue types (definition, example, contrast, cause) | Reading Rockets, context clues | ReadWriteThink, context clues | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad b20, 2026-11-09): every sample passage has at least one locked word whose first dictionary sense is keyed wrong for it; each grade's passage has at least one clue of two different types; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 passage and keys fit; at 680x425 the keys are below.
2. The Context key lights clues and takes a type and a guess. (L.6.4a, L.7.4a, L.8.4a)
3. The Roots key splits the word and shows the root. (L.6.4b, L.7.4b, L.8.4b)
4. The Dictionary key shows pronunciation, part of speech and senses; the verdict compares. (L.6.4c, d)
5. The glossary takes sentences; the final passage asks two meaning questions. (L.6.6, L.7.6, L.8.6)
6. The strategy log shows key counts and wrong guesses.
7. My glossary survives a reload where storage works; `Clear my glossary` removes it.
8. Print shows the glossary and log.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: locks open without turning; no network requests.

## Open questions
- None for Cory.

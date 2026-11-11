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
- Passages written for Curio Class: grade 6 "The Volcano Watchers" (science), grade 7 "Two Kings at War" (history), grade 8 "Shapes That Repeat" (math). tool.json `modes: ["Grade 6", "Grade 7", "Grade 8", "My glossary"]`, `minutes: "30-40"` (one grade path; two sittings is fine), `grades_label: "Grades 6-8"`.
- Saving: the personal glossary is kept in this browser; footer and the My glossary panel: "Your glossary stays on this device." `Clear my glossary` removes it.
- Role: lesson. Each grade is its own path with its own passage, its own six words, its own final passage and that grade's wording of the standard on the goal card. A student does the path for their grade; nothing in one path is needed for another.
- Change note (spec fix, 2026-11-11): the desk, the three keys and Professor Halvorsen stay. Each path goes from four words to six. The Professor cracks one word first as the model. The student now picks which words matter, splits each word and reasons from the root in writing, uses a glossary and a thesaurus as well as the dictionary, finds pronunciation and part of speech, looks two words up in a real dictionary, puts the meaning back in the sentence to check it, and the verdict can no longer be marked right for free. The final passage has two new words done on your own. Added the three hooks.
- English learners: every spoken line is also on screen in short sentences. The words context, clue, root, prefix, sense, part of speech and synonym each show with an example from the Professor's word the first time they are used. Every written line offers a frame the student may take or leave ("I think it means __ because __."). A student may add the word in their home language to a glossary card.

## Standards map
| Code | The standard's verb and its parts | Who does the verb | Student action that teaches it | Items that differ | What they see | Done when check |
|---|---|---|---|---|---|---|
| L.6.4a, L.7.4a, L.8.4a | use context (the overall meaning of a sentence or paragraph; a word's position or function in a sentence) as a clue to meaning | the student | Tap the clue words, name the clue type, say what job the word does in its sentence, then write a guess | 6 words a path, 2 on your own | the clue the student tapped; the type and job chips | 2 |
| L.6.4b, L.7.4b, L.8.4b | use common, grade-appropriate Greek or Latin affixes and roots as clues (grade 6 audience, auditory, audible; grade 7 belligerent, bellicose, rebel; grade 8 precede, recede, secede) | the student | Split the word at its joins, work out what the shared part means from two family words, and write a second guess from the root | 6 words a path, 2 on your own | the student's split and the family words; the root card only after | 3 |
| L.6.4c, L.7.4c, L.8.4c | consult reference materials (dictionaries, glossaries, thesauruses), print and digital, to find pronunciation and to determine or clarify precise meaning or part of speech | the student | Choose the right reference for each question, find the stressed syllable and the part of speech, pick the sense that fits, pick the synonym that keeps the meaning; look two words up in a real dictionary | 6 words a path, 2 real look-ups, 2 on your own | three references on a shelf; the entry | 4 |
| L.6.4d, L.7.4d, L.8.4d | verify the preliminary determination of meaning (by checking the inferred meaning in context or in a dictionary) | the student | Read the sentence with the guess in place and with the sense in place, then say same, close or different and show where | 6 words a path, 2 on your own | the sentence twice, side by side | 5 |
| L.6.6, L.7.6, L.8.6 | acquire and use accurately general academic and domain-specific words; gather vocabulary knowledge when a word is important to comprehension or expression | the student | Pick the words that matter from ten, tag each as many-subject or one-subject, choose the sentence that uses it rightly, write your own, then read a new passage | 6 words and 5 questions a path | the glossary and the final passage | 6 |

## Screens and modes
Header (kit): title "Context, Roots, Dictionary"; `Grade 6`, `Grade 7`, `Grade 8`, `My glossary`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word. The goal card under the header gives that grade's standard in its own words.

**On load and first tap.** A passage on a desk with words locked behind small padlocks, and a key ring of three keys: Context, Roots, Dictionary. Professor Halvorsen, a retired lexicographer with reading glasses on a cord, sits at the next desk. First hint: "Tap the passage to hear it." The first tap reads the title; the welcome is queued after it (`welcomeAfter: true`).

**The Professor goes first (the model).** On a three-sentence sample he cracks one word, "nocturnal", aloud: taps the clue ("unlike animals that hunt by day"), names it a contrast, says the word describes the owl, splits it (noct + urn + al), reasons from "nocturne", writes a guess, opens the dictionary, picks the sense, and reads the sentence again with the meaning in place. It cannot be skipped the first time and `The Professor's word` reopens it.

**Which words matter?** The passage (about 250 words) shows ten words underlined. The student picks the six they must know to understand it. The check is of the set and gives a count; one more try, then the six are locked and any the student missed are tagged "the Professor picked it".

**Keys, in order.** Tap a lock:
1. Context: the student taps the words that help and names the clue type (definition, example, contrast, cause). Then a second chip: the word's job in its sentence (names a thing, tells an action, describes), judged from where it sits. Both are checked together; a miss says only "Look around the word again" and a second miss is tagged. The student writes a first guess.
2. Roots (opens after a guess): the word is shown whole and the student taps between letters to split it (sub / sequ / ent). The split is checked whole; one retry, then the Professor splits it. Two family words with plain meanings appear (for audi: audience, auditorium) and the student types what the shared part must mean. Then the root card shows, and the student must write a second guess that uses the root, or tick "my first guess still stands" and say why in a line.
3. References (opens after the roots step; `Skip to dictionary` is gone): a shelf with a dictionary, the passage's own glossary and a thesaurus. Four questions, and for each the student first takes the right book: "How is it said?" (dictionary: tap the stressed syllable); "What part of speech is it here?" (dictionary); "Which sense fits this passage?" (dictionary, or the glossary for a subject word); "Which word could stand in for it here?" (thesaurus: three synonyms, one keeps the passage's meaning). A wrong book opens and plainly lacks the answer; that costs the try.
4. Check it back: the passage sentence shows twice, once with the student's guess in place of the word and once with the chosen sense. The student marks `same`, `close` or `different`, and for close or different taps the part of the guess that is off and types the fix. A mark of `same` on a guess that shares no key word with the sense is turned back once with "Read both again", and if kept it prints as "check with your teacher".

**Real look-up.** For two words in each path the student opens a real dictionary, print or the one the teacher links, and types the part of speech and the first sense it gives. The part of speech is checked; the sense prints for the teacher.

**My glossary.** Professor Halvorsen's own card for "nocturnal" is the model. For each cracked word the student tags it `used in many subjects` or `mostly one subject`, picks which of three sentences uses it rightly (one misuses the meaning, one misuses the part of speech), then writes their own sentence (it must use the word and be at least 6 words) and ticks a three-box guide: the sentence shows what the word means; the word does the right job; it is not the dictionary's sentence.

**Strategy log.** The word lab's Strategy log: how often context was enough, where the root changed the guess, and each guess the dictionary proved wrong.

**Final passage (on your own).** A short passage in a new subject. It reuses the six glossary words, with five meaning questions, and holds two new locked words. For those two the Professor is quiet: no model, no clue chips lit, no family words offered, one answer at each step (clue and job, split and root guess, part of speech and sense, check it back). Nothing is marked until the last question is in.

**The end.** A results strip for the teacher, for that grade's codes: 4a, 4b, 4c and 4d on the two new words, each right or not with what the student gave; L.6 (or 7 or 8).6 as the five questions right; then the counts for the six words before, with every tag.

At 1366x768 the passage and key panel fit side by side; at 680x425 the key panel is below.

## Content
- Three paths, each with a passage of about 250 words and a final passage of about 150, written for Curio Class with keyed clue spans, types and jobs. Reading level rises by grade (grade 6 about 900L, grade 7 about 1000L, grade 8 about 1050L; to be measured at Build).
- Grade 6, "The Volcano Watchers" (science): hypothesis, magnitude, subsequent, audible, dormant, predict. Root family on the goal card: audience, auditory, audible. Final passage: an orchestra rehearsal; new words inaudible, magnify.
- Grade 7, "Two Kings at War" (history): belligerent, bellicose, concede, antebellum, pacify, benevolent. Root family: belligerent, bellicose, rebel. Final passage: a school election; new words rebellion, malevolent.
- Grade 8, "Shapes That Repeat" (math): precede, recede, congruent, symmetry, bisect, equilateral. Root family: precede, recede, secede. Final passage: a coastline at low tide; new words secede, intersect.
- In each path the four words not picked as mattering are common ones the passage explains outright. Each path has clues of all four types and words in all three jobs.
- 18 word records and 6 new-word records (joins, roots, two family words, pronunciation with stress, part of speech in the passage, senses, three synonyms with one keyed, three usage sentences with one keyed), built with the word lab's Morphemes and Word records from the etymologies in Sources.
- Dictionary, glossary and thesaurus entries are written for Curio Class in the form of real entries, from the senses in two dictionaries.
- What a wrong answer on the two new words means: a clue tapped far from the word means the student is hunting for a familiar word and not reading the sentence; a split in the wrong place (ma / gnify) means the word is being cut by sound and not by meaning parts; taking the thesaurus to find how a word is said means the three references are not yet apart; picking the first sense means the entry is not being read against the passage; marking `same` when the guess and the sense differ means the check is being skipped.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Keys open in order; there is no way past the guess, the split or the check.
- Access: every action works by tap and by keyboard. A split is made with a tap between letters or with the arrow keys and Enter; references are opened with a tap or Enter. Clue types, jobs and verdicts are words, and a tagged word carries its tag in words, never color alone. Motion can be paused. Every word heard is also shown.
- On your own: one answer at each step, no feedback until the last question is in.
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
- how `matter`: "Pick the six words you must know to understand this."
- how `split`: "Tap between the letters where the word's parts join."
- how `shelf`: "Take the book that can answer this."
- how `back`: "Read the sentence both ways. Same, close or different?"
- how `own`: "Two new words. These are on your own."
- event, whole, the Professor's word.
Every `how` line is also shown as text beside its control. Instructions use no idioms.

## Family engine
word-lab (`kit/wordlab.js`, `__tool.wl`), described in full in tools/word-family-tree/spec.md. This tool uses: Morphemes, Word records, Split, Lookup (`wl.entry`, the dictionary key), Strategy log (`wl.log`) and Guess and verify. Not Build, Tree view or Card view. The context key and passages are tool-only code.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Which words matter | Tick all ten | The set is checked whole with a count; a second miss tags the words. |
| Context | Tap everything; try each type | Clue, type and job are one answer; a miss does not say which was off. |
| Roots | Wait for the root card | The card shows only after the student's split and the meaning they typed from the family words; a second guess or a reason is required. |
| References | Open every book | A wrong book costs the try. |
| Senses | Pick the first sense | For at least two words a path the first sense is keyed wrong for that passage. |
| Verdict | Mark every guess same | A `same` with no shared key word is turned back and then printed for the teacher. |
| Glossary | Copy the definition | The usage pick is keyed; the sentence must use the word, and copied definitions are flagged when 4 or more words match the entry. |
| Final passage | Guess; lean on the Professor | Five questions in a new subject, and the two new words run with no help and one answer a step. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the passage: title, `welcome` (queued, first time), then the Professor's word (whole), waits. `passage` (whole) on Play. `matter`.
2. Context: `clue`. Roots: `split`, then `root`. References: `shelf`, `sense`. Check it back: `back`, then `verdict`.
3. Final passage: `own`.

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
Spec fix notes (2026-11-11): the added words' roots (dormant from Latin dormire, to sleep; predict from prae and dicere; pacify from pax and facere; benevolent from bene and velle; bisect from bi and secare; equilateral from aequus and latus; nocturnal from nox; magnify from magnus; malevolent from male and velle; intersect from inter and secare; secede from se and cedere; rebel from re and bellum) were written from memory and not opened in this pass: to confirm at Build against the two dictionaries above. Counted, not run: 6 words in each of 3 paths is 18, plus 2 new words a path is 6.

## Done when
1. Focus and fold: at 1366x768 passage and keys fit; at 680x425 the keys are below.
2. Each of the three grade paths has its own passage, six words, goal card and final passage, and none needs another. (L.6.4, L.7.4, L.8.4)
3. The Context key takes the student's clue, its type and the word's job as one answer, then a guess. (4a)
4. The Roots key takes the student's split and the meaning they work out from two family words before the root card shows; a second guess or a reason is required. (4b)
5. The reference shelf makes the student choose dictionary, glossary or thesaurus, find the stress and the part of speech, pick the sense and the synonym; two words a path are looked up in a real dictionary. (4c)
6. Check it back shows the sentence both ways; a free `same` is turned back and then printed for the teacher. (4d)
7. The student picks the six words that matter from ten, tags each, picks the right usage and writes a sentence against the guide; the final passage asks five meaning questions. (L.6.6, L.7.6, L.8.6)
8. The Professor's word plays first and can be reopened.
9. The two new words in the final passage run with no model, chips or family words and one answer a step; the end screen shows the result for each code of that grade.
10. The strategy log shows key counts and wrong guesses. My glossary survives a reload where storage works; `Clear my glossary` removes it. Print shows the glossary, the log and every tag.
11. Every spoken instruction is also on screen; each key word shows with an example at first use; the frames can be left.
12. Every action works by keyboard as well as tap, nothing is shown by color alone, and motion can be paused.
13. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
14. Motion off: locks open without turning; no network requests.

## Open questions
- None for Cory.

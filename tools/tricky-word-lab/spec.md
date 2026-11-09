# Tricky Word Lab

## One idea
A commonly misspelled word sits under glass on a lab bench ("seperate"), and the student settles it by tracing it to its root and family (separate comes from Latin se-, apart, and parare, to prepare, so it keeps the "par"; definite comes from finite), tests a spelling rule against a word list to find where it holds and where it breaks, and keeps a personal tricky-words list that comes back for review until each word is beaten, so they learn to spell hard words by knowing where they come from instead of memorizing them.

## Not like
- context-roots-dictionary (7-8, concept): roots for meaning. Here roots for spelling.
- pause-and-break (6-8, spec): the punctuation parts of the same standards. Here the spelling parts.
- word-family-tree (spec): exploring a root's family tree. Here using a family to fix a spelling.
- root-detective-cards (4, spec): combining roots for meaning. Here grade 6-8 spelling.
- glossary-makers (spec): defining terms. Here spelling them.

## Who and how
- Grades 6-8, ELA, module "Spelling Through Word Families" (Language). Standards: L.6.2b, L.7.2b, L.8.2c (spell correctly). The punctuation parts of L.6.2, L.7.2 and L.8.2 are in pause-and-break.
- Driver: one student; a teacher can add a class list (tool.json `driver: "student"`). Every word is said on tap.
- Specimens: 30 commonly misspelled words in three trays by grade, plus three rule tests. tool.json `modes: ["Specimens", "Rule tests", "My list", "Class list"]`, `minutes: "10-20"`, `grades_label: "Grades 6-8"`.
- Saving: the tricky-words list and review dates are kept in this browser; footer and the My list panel: "Your list stays on this device." `Clear my list` removes it. A class list typed by the teacher is kept the same way.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| L.6.2b, L.7.2b, L.8.2c | Split the specimen into parts and find the family member that proves the tricky letters (separate and prepare; definite and finite) | the split word with the proving letters lit in both words | 2 |
| L.6.2b, L.7.2b, L.8.2c | Spell the word fresh from memory after the glass clears | the typed word, checked letter by letter | 3 |
| L.6.2b, L.7.2b, L.8.2c | Rule tests: sort a list into "follows the rule" and "breaks it" and write the rule's real reach | the two bins and the rule card | 4 |
| L.6.2b, L.7.2b, L.8.2c | Review: words on My list come back after 1, 3 and 7 days until spelled right three times | the review queue | 5 |

## Screens and modes
Header (kit): title "Tricky Word Lab"; `Specimens`, `Rule tests`, `My list`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A lab bench with a bell jar over the misspelled specimen "seperate", a rack of root vials and Dr. Ines Varga, a lab scientist in goggles (seen in a small portrait in the corner of the bench). First hint: "Tap the bell jar to hear the word." The first tap says the word; the welcome is queued after it (`welcomeAfter: true`).

**Specimen.** The word under glass, misspelled the common way. Steps:
1. Split: the student taps between letters to split the word; the word lab's Split (`wl.split`) checks the split against the word record's parts (se + par + ate).
2. Family: three family cards ("prepare", "repair", "apparatus"); the student picks the one that shares the root and sees the root letters lit in both words. Tap a card to hear its road (Latin parare, to prepare).
3. Fix: the glass lifts; the student fixes the misspelled letters.
4. Fresh: the word hides; the student types it from memory. Correct adds a star; a miss adds it to My list.
Each step is logged with the word lab's Strategy log (`wl.log`), so My list shows whether the family or the rule cracked it.

**Specimen trays.** Grade 6: separate, definite, grammar, government, library, February, business, independent, believe, receive. Grade 7: necessary, occurrence, accommodate, rhythm, privilege, cemetery, embarrass, restaurant, conscience, immediately. Grade 8: occasionally, recommend, perseverance, maintenance, pronunciation, bureaucracy, millennium, questionnaire, conscientious, liaison. Each has a word record with parts, road and a family card set; a few (February, rhythm, liaison) have a "say it to spell it" helper instead of a family when the family doesn't help.

**Rule tests.** Three rules: "i before e except after c" (tested on 20 words; it breaks on weird, their, science, neighbor, height and more, and the card ends with the rule's real reach: it holds for the "ee" sound); "drop the silent e before a vowel suffix" (make, making; but noticeable, courageous keep it); "double the final consonant" (begin, beginning; but visit, visiting). The student sorts words into Follows and Breaks, then fills in the rule card's reach line from three choices.

**My list.** Words the student missed, each with its family card and the step that cracked it. A review queue brings words back after 1, 3 and 7 days (by the device's date) until spelled right three times in a row.

**Class list.** The teacher adds words; each needs a family or helper typed in, or it shows as a plain spelling card.

At 1366x768 the bench and panel fit side by side; at 680x425 the panel is a tab.

## Content
- 30 word records (parts, road, family cards, common misspelling) from sourced etymologies (Sources), built with the word lab's Morphemes and Word records.
- Three rule tests with 20 words each, sorted in data.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Typing in the fresh step is checked when the student taps `Check`, not letter by letter while typing.
- Review dates use the device clock; nothing is sent.
- With Motion off the glass lifts without sliding.

## Look
- Accent `--brand` #00666b lab teal (header, vials, bench edge); gold #f4c542 (lit root letters, stars); paper #eff8f8; ink #032426; muted #465d5e. Scene: a bright lab bench.
- Contrast (WCAG 2.1, computed): white on brand 6.75:1; brand on paper 6.25:1; ink on paper 15.15:1; muted on paper 6.51:1; ink on gold 10.05:1.
- Never color alone: lit letters are also bold and underlined; bins have words.
- Different from this batch (thermometer red, x-ray blue, night indigo, desk brown).

## Art
- People art goes to Gemini: Dr. Ines Varga (a Hungarian American woman in her forties with goggles pushed up, lab coat), 3 poses; "illustrated friendly scientist <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): lab bench with a bell jar (1).
About 4 images. Drawn in code: words, vials, bins, queue. The words are the content.

## Voice
Bank voice `calm-professor` as Dr. Varga (unique in this batch). `Curio.voice` with `scope: () => state.view + ':' + state.word + ':' + state.step`, `welcomeAfter: true`.
- event `word`: the specimen word, said clearly, then in a sentence.
- how `welcome`: "Every tricky word has a family that gives it away. Split it, find its family, and the spelling settles."
- event `family`: "{Separate}, {prepare}. Same root: {par}, to make ready."
- event `fresh`: "Now spell it from memory."
- event `star`: "Beaten."
- event `breaks`: "{Weird} breaks the rule."
- event `review`: "{Necessary} is back for review."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
word-lab (`kit/wordlab.js`, `__tool.wl`), described in full in tools/word-family-tree/spec.md. This tool uses: Morphemes, Word records, Split, Card view (family cards), Strategy log (with an added step name 'family' alongside 'parts'), and Road key. Not Build, Tree view, Lookup or Guess and verify. The review queue and rule tests are tool-only code.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Family | Tap every card | A wrong card shows its own root and says "Different family." |
| Fresh | Copy from the screen | The word is hidden in the fresh step. |
| Rule tests | Put everything in Follows | 20 words per rule with at least 5 that break it. |
| Review | Skip it | Words stay on My list until three right in a row. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the bell jar: `word`, `welcome` (queued, first time).
2. Family: `family`. Fresh: `fresh`, then `star` or the word added to My list.
3. Rule tests: `breaks` as words are sorted.
4. My list: `review` per due word.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| L.6.2b, L.7.2b, L.8.2c ("spell correctly") wording | thecorestandards.org, Language Grades 6-8 | CCSS ELA 2010 PDF | yes |
| separate from Latin separare (se-, apart, and parare, to prepare); definite from Latin definitus (related to finis, end, as in finite) | Wiktionary, separate and definite etymology (checked 2026-11-09) | Merriam-Webster, etymology of separate and definite | yes |
| Etymologies of the other 28 words (for example accommodate from ad- and commodus; occurrence from ob- and currere; privilege from privus and lex) | Merriam-Webster, each entry's etymology | Online Etymology Dictionary, each entry | yes |
| "i before e except after c" has many exceptions and holds best for the "ee" sound | Merriam-Webster, "i before e" usage article | Cambridge Dictionary blog or Oxford Learner's Dictionaries spelling notes | yes |
| Spelling instruction that teaches morphology (word parts and families) improves spelling | Reading Rockets, spelling and morphology | International Literacy Association, morphology brief | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad b19, 2026-11-09): every sample rule test has at least 5 words that break the rule out of 20; the sample split for separate is se + par + ate; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 bench and panel fit; at 680x425 the panel is a tab.
2. Split and family steps light the proving letters. (L.6.2b)
3. Fresh spelling stars or adds to My list. (L.7.2b)
4. Rule tests sort and set the rule's reach. (L.8.2c)
5. The review queue brings words back on day 1, 3 and 7 until three in a row.
6. My list survives a reload where storage works and shows the cracking step; `Clear my list` removes it.
7. Class list words work with a family or helper.
8. Print shows My list.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: the glass lifts without sliding; no network requests.

## Open questions
- None for Cory.

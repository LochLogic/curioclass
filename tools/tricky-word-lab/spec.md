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
- Role: practice (a station the student returns to). Each grade is its own path: that grade's tray of ten words, one rule test, a proofread, lab notes and a dictation, with that grade's code on the goal card (L.6.2b, L.7.2b or L.8.2c, each "spell correctly"). No path needs another.
- Change note (spec fix, 2026-11-11): the bench, Dr. Varga, the four specimen steps and the review queue stay. The family step is no longer free: the student picks the card and taps the letters in it that prove the tricky letters, as one answer, and a second miss is logged. Spelling now reaches the student's own writing: a proofread of someone else's paragraph and lab notes the student writes. Each path ends with a dictation of all ten words on your own. Added the three hooks.
- English learners: every word is said and shown. Each tray word shows with its meaning in a short sentence, and a picture where one helps, the first time it is used. The lab notes offer three sentence starters the student may take or leave. Instructions use no idioms.

## Standards map
| Code | The standard's verb and its parts | Who does the verb | Student action that teaches it | Items that differ | What they see | Done when check |
|---|---|---|---|---|---|---|
| L.6.2b, L.7.2b, L.8.2c (the word) | spell correctly | the student | Split the specimen, pick the family member and tap the letters that prove the tricky ones, fix it, then type it from memory | 10 words a path | the split word; the proving letters underlined in both words only after the student's taps | 2, 3 |
| L.6.2b, L.7.2b, L.8.2c (rules) | spell correctly | the student | Sort a list into "follows the rule" and "breaks it" and write the rule's real reach | 20 words, one rule a path | the two bins and the rule card | 4 |
| L.6.2b, L.7.2b, L.8.2c (in writing) | spell correctly, in their own and others' writing | the student | Find and fix five misspellings in a paragraph with nothing marked; write lab notes that use at least four tray words | 5 slips and 1 piece of writing a path | the paragraph; the student's notes | 5 |
| L.6.2b, L.7.2b, L.8.2c (kept) | spell correctly | the student | Dictation of all ten on your own; words missed come back after 1, 3 and 7 days until spelled right three times | 10 a path | the dictation sheet; the review queue | 6, 7 |

## Screens and modes
Header (kit): title "Tricky Word Lab"; `Specimens`, `Rule tests`, `My list`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A lab bench with a bell jar over the misspelled specimen "seperate", a rack of root vials and Dr. Ines Varga, a lab scientist in goggles (seen in a small portrait in the corner of the bench). First hint: "Tap the bell jar to hear the word." The first tap says the word; the welcome is queued after it (`welcomeAfter: true`).

**Specimen.** The word under glass, misspelled the common way. Steps:
1. Split: the student taps between letters to split the word; the word lab's Split (`wl.split`) checks the split against the word record's parts (se + par + ate).
2. Family: three family cards ("prepare", "repair", "apparatus"). The student picks the one that shares the root and taps the letters in it that settle the tricky letters (the "par" in prepare), then taps `Prove it`. Card and letters are judged together. A miss says only "Not proved yet" and does not say which was off; after a second miss Dr. Varga shows the family, and the word is logged "shown" and goes on My list. Only after a right answer are the root letters underlined in both words and the card's road heard (Latin parare, to prepare).
3. Fix: the glass lifts; the student fixes the misspelled letters.
4. Fresh: the word hides; the student types it from memory. Correct adds a star; a miss adds it to My list.
Each step is logged with the word lab's Strategy log (`wl.log`), so My list shows whether the family or the rule cracked it.

**Specimen trays.** Grade 6: separate, definite, grammar, government, library, February, business, independent, believe, receive. Grade 7: necessary, occurrence, accommodate, rhythm, privilege, cemetery, embarrass, restaurant, conscience, immediately. Grade 8: occasionally, recommend, perseverance, maintenance, pronunciation, bureaucracy, millennium, questionnaire, conscientious, liaison. Each has a word record with parts, road and a family card set; a few (February, rhythm, liaison) have a "say it to spell it" helper instead of a family when the family doesn't help.

**Rule tests.** Three rules: "i before e except after c" (tested on 20 words; it breaks on weird, their, science, neighbor, height and more, and the card ends with the rule's real reach: it holds for the "ee" sound); "drop the silent e before a vowel suffix" (make, making; but noticeable, courageous keep it); "double the final consonant" (begin, beginning; but visit, visiting). The student sorts words into Follows and Breaks, then fills in the rule card's reach line from three choices.

**Proofread (after the tenth specimen).** A paragraph of about 90 words in a student's voice, written for that grade's tray, with five tray words misspelled the common way and nothing marked. The student taps a word and types the fix, and has six marks. `Check` gives a count first ("3 of 5 found and fixed"); one more pass, then the rest are shown and logged.

**Lab notes.** The student writes four or more sentences about anything they did this week, using at least four tray words; the tray is hidden while they write. On `Done` each tray word used is checked, a misspelling is underlined with no fix offered, and the student corrects it from memory. Words outside the tray are not judged. The notes print.

**Dictation (on your own).** All ten words of the path, each heard alone and in a sentence, typed with no jar, no steps and no family cards. One try each, and nothing is marked until the tenth is in.

**The end.** A results strip for the teacher under that grade's code: dictation right out of ten with each misspelling as typed; proofread found and fixed out of five; tray words right in the lab notes; words logged "shown".

**My list.** Words the student missed, each with its family card and the step that cracked it. A review queue brings words back after 1, 3 and 7 days (by the device's date) until spelled right three times in a row.

**Class list.** The teacher adds words; each needs a family or helper typed in, or it shows as a plain spelling card.

At 1366x768 the bench and panel fit side by side; at 680x425 the panel is a tab.

## Content
- 30 word records (parts, road, family cards, common misspelling) from sourced etymologies (Sources), built with the word lab's Morphemes and Word records.
- Three rule tests with 20 words each, sorted in data.
- Rule test by path: grade 6, i before e; grade 7, drop the silent e; grade 8, double the final consonant. The other two stay open as extras.
- Three proofread paragraphs, one a path, each with five keyed misspellings: grade 6 (seperate, definate, libary, Febuary, recieve); grade 7 (neccessary, occurence, accomodate, embarass, restaraunt); grade 8 (occassionally, reccomend, maintainance, pronounciation, millenium).
- Ten dictation sentences a path, written for Curio Class.
- What a wrong spelling in the dictation means: "seperate" or "definate" means the word is being spelled by its sound and the family (prepare, finite) is not being called on; "occurence" or "begining" means the doubling rule is not being used; "recieve" means the rule is known as a chant and not for its reach; a word right in the dictation and wrong in the lab notes means it is known as a list word and not yet in the student's writing.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Typing in the fresh step is checked when the student taps `Check`, not letter by letter while typing.
- Review dates use the device clock; nothing is sent.
- With Motion off the glass lifts without sliding.
- Access: every action works by tap and by keyboard. A split is a tap between letters or the arrow keys and Enter; letters in a family card are picked the same way. Proving letters are underlined and a misspelling is underlined with the word "check", never color alone. Motion can be paused. Review uses dates only; nothing in the tool is timed.
- On your own: one try a word, no feedback until the tenth is in.

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
- how `prove`: "Pick the family word. Tap the letters that prove it. Then tap Prove it."
- how `proof`: "Five words are spelled wrong. Tap each one and fix it."
- how `notes`: "Write four sentences. Use four of your words."
- how `own`: "Now all ten, on your own. Listen, then type."
Every `how` line is also shown as text beside its control. Instructions use no idioms.

## Family engine
word-lab (`kit/wordlab.js`, `__tool.wl`), described in full in tools/word-family-tree/spec.md. This tool uses: Morphemes, Word records, Split, Card view (family cards), Strategy log (with an added step name 'family' alongside 'parts'), and Road key. Not Build, Tree view, Lookup or Guess and verify. The review queue and rule tests are tool-only code.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Family | Tap every card | Card and proving letters are one answer; a miss does not say which was off, and a second miss logs the word as shown and puts it on My list. |
| Fresh | Copy from the screen | The word is hidden in the fresh step. |
| Rule tests | Put everything in Follows | 20 words with at least 5 that break the rule. |
| Proofread | Mark every word | Six marks for five slips, and the first check gives only a count. |
| Lab notes | Leave the tray words out | Four tray words are needed before `Done` opens. |
| Dictation | Lean on the steps; retry | No steps or cards, one try a word, nothing marked until the tenth. |
| Review | Skip it | Words stay on My list until three right in a row. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the bell jar: `word`, `welcome` (queued, first time).
2. Family: `family`. Fresh: `fresh`, then `star` or the word added to My list.
3. Rule tests: `breaks` as words are sorted. `proof`; `notes`; `own`.
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
2. Each grade path has its own tray, rule test, proofread, dictation and goal card. (L.6.2b, L.7.2b, L.8.2c)
3. The family step takes the card and its proving letters as one answer; a second miss logs the word as shown. Fresh spelling stars or adds to My list.
4. The rule test sorts and sets the rule's reach.
5. The proofread has five unmarked slips, six marks and a count on the first check; the lab notes need four tray words and check them in the student's own sentences.
6. The dictation of ten runs with no steps or cards and one try a word; the end screen shows the result under that grade's code.
7. The review queue brings words back on day 1, 3 and 7 until three in a row. My list survives a reload where storage works; `Clear my list` removes it. Class list words work with a family or helper.
8. Print shows My list, the lab notes and the results.
9. Every spoken instruction is also on screen; each tray word shows with its meaning at first use; the sentence starters can be left.
10. Every action works by keyboard as well as tap, nothing is shown by color alone, nothing is timed, and motion can be paused.
11. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
12. Motion off: the glass lifts without sliding; no network requests.

## Open questions
- None for Cory.

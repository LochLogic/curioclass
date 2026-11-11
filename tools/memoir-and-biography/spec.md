# Memoir and Biography

## One idea
The student reads three tellings of one morning in April 1887, when Helen Keller understood that the word spelled into her hand meant water: Helen's own memoir (1903), Anne Sullivan's letter written that same day, and a short biography written for Curio Class; they tag how each introduces Helen, which anecdotes it picks and what it wants readers to think, line up where the three differ (Helen remembers a fight over "mug" and "water" and a broken doll before they went out; Sullivan writes that the trouble was "mug" and "milk", and she was the one pumping), and then decide how the biography should handle the difference, so they learn that how a person is presented depends on who is telling and why.

## Not like
- portrait-in-four-media (10, concept): four media on one scientist. Here memoir, letter and biography on one morning, grades 6-8.
- two-authors-one-event (7, concept): two articles' spin on one event. Here a person presented by herself, her teacher and a biographer.
- fact-check-desk (8, concept): conflicting facts in arguments. Here conflicting memories in life writing.
- eyewitness-vs-reporter (4, spec): firsthand and secondhand. Here grades 6-8 point of view and how a person is introduced.
- fact-fusion (5, spec): facts in a table. Here people, anecdotes and point of view.

## Who and how
- Grades 6-8, ELA, module "How Authors Present People and Ideas" (Reading Informational Text). Standards: RI.6.3, RI.6.6, RI.6.9, RI.7.3, RI.8.3, RI.8.6.
- Driver: one student (tool.json `driver: "student"`). Role: lesson. Every sentence is read on tap.
- Three grade paths, each with its own texts, that grade's wording on the goal card, and five or more items for each of its codes. No path needs another.
  - Grade 6, one morning in three texts (Helen Keller's memoir, Anne Sullivan's letter, a biography). RI.6.3: analyze in detail how a key individual, event or idea is introduced, illustrated and elaborated (through examples or anecdotes). RI.6.6: determine an author's point of view or purpose and explain how it is conveyed. RI.6.9: compare and contrast one author's presentation of events with another's (a memoir and a biography of the same person). Two sittings.
  - Grade 7, Booker T. Washington, "Up from Slavery", chapter 3 (the road to Hampton). RI.7.3: analyze the interactions between individuals, events and ideas (how ideas influence individuals or events, how individuals influence ideas or events).
  - Grade 8, Susan B. Anthony's 1873 speech on the right to vote. RI.8.3: analyze how a text makes connections among and distinctions between individuals, ideas or events (through comparisons, analogies or categories). RI.8.6: determine an author's point of view or purpose and analyze how the author acknowledges and responds to conflicting evidence or viewpoints.
- Change note (spec fix, 2026-11-11): the reading desk, Mr. Abernathy, the three Keller texts, the table and the timeline row stay as grade 6. Before, a wrong tag was answered with the right one, wrong table rows said why, threads were not checked, and the conflict round took any choice. Now every item is an answer plus a reason judged together, a miss never names the answer, the student writes each comparison before the timeline lights, grade 7 has its own text with keyed threads, and grade 8 has its own text where the author herself answers the other side. Mr. Abernathy works a model first and the last two items of each code are on your own. Added the three hooks.
- English learners: every spoken line is also on screen in short sentences. The words introduce, anecdote, elaborate, point of view, purpose, influence, distinction, analogy and category each show with an example from Mr. Abernathy's model the first time they are used. Every written line offers a frame the student may take or leave ("The memoir shows __, but the letter __."). Instructions use no idioms.
- tool.json `modes: ["Grade 6", "Grade 7", "Grade 8"]`, `minutes: "30-40"` a sitting, `grades_label: "Grades 6-8"`.
- Nothing is saved; `Print` prints the student's answers, table and lines.

## Standards map
| Code | The standard's verb and its parts | Who does the verb | Student action that teaches it | Items that differ | What they see | Done when check |
|---|---|---|---|---|---|---|
| RI.6.3 | analyze in detail how an individual, event or idea is introduced, illustrated and elaborated | the student | For five marked passages, say what the passage does (introduces, illustrates with an anecdote, elaborates with an example) and choose why the author does it there, then write the why in a line | 5 passages across the three texts | the passage, the job and reason | 2 |
| RI.6.6 | determine point of view or purpose and explain how it is conveyed | the student | At five spots, name whose view and what purpose shows, and tap the words that carry it | 5 spots (2 memoir, 2 letter, 1 biography) | the spot with the tapped words | 2 |
| RI.6.9 | compare and contrast one author's presentation of events with another's | the student | For five moments of the morning, mark same, differs or only one tells it, tap the lines in each text, and write the comparison sentence before the timeline lights | 5 moments | the two tellings side by side; the student's sentence | 3 |
| RI.7.3 | analyze the interactions between individuals, events and ideas | the student | Draw five threads, each with a direction, a kind (idea moves a person; person moves an event; event changes an idea) and the two passages that show it | 5 threads | threads between highlights | 4 |
| RI.8.3 | analyze how a text makes connections and distinctions through comparisons, analogies or categories | the student | For five marked sentences, name the move (comparison, analogy, category, distinction), tap the two things it joins or separates, and say what it makes the listener see | 5 sentences (at least 1 of each move) | the sentence with its two ends tapped | 4 |
| RI.8.6 | determine purpose and analyze how the author acknowledges and responds to conflicting evidence or viewpoints | the student | At five places, tap where Anthony states the other side, tap her answer, and name how she answers (uses their own words, gives a counter-fact, redefines the term, grants part and limits it) | 5 places | objection and answer highlighted as a pair | 5 |

## Screens and modes
Header (kit): title "Memoir and Biography"; `Desk`, `Table` (grade 6), `Threads` (grade 7), `Answers` (grade 8); `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word. The goal card gives the grade's standards in their own words.

**On load and first tap.** A reading desk with the grade's documents, a photograph and a reading lamp. The host is Mr. Abernathy, a librarian in the reading room (seen only as a voice and a hand on the lamp). First hint: "Tap the first text to start reading." The first tap reads its title; the welcome is queued after it (`welcomeAfter: true`).

**Mr. Abernathy goes first (the model).** Two short tellings of one small event, written for Curio Class: a girl's diary line about the day the school bell broke, and the janitor's report of it. For each code of the grade he does one item aloud, pointing at the words: what a passage does and why; whose view shows and which words carry it; where the tellings differ; one thread; one comparison; one objection and answer. It cannot be skipped the first time and `Mr. Abernathy's example` reopens it, except on the items on your own.

**How every item is judged.** Each item is two or three parts answered together (a pick and a reason; a mark and its lines; two ends and a kind). A miss says only "Not yet. Read it again." and never names the right answer or which part was off. After a second miss Mr. Abernathy shows his answer and the item prints as "shown".

**Grade 6 texts.**
- Memoir: Helen Keller, "The Story of My Life" (1903), chapter 4, from "One day, while I was playing with my new doll" through leaving the well-house (exact text, about 450 words).
- Letter: Anne Sullivan's letter of April 5, 1887, printed in the same 1903 book (exact text, about 400 words).
- Biography: written for Curio Class (about 400 words) on Helen's whole life with this morning as one paragraph, naming its sources.
A note at the start says Helen was six, deaf and blind from an illness at 19 months, and that the three texts were written by Helen at 22, by Sullivan that day, and by a writer today.

**Grade 6, What it does (RI.6.3).** Five passages are bracketed. For each the student picks its job (introduces Helen, illustrates with an anecdote, elaborates with an example) and one of four reasons the author might have for doing it there (three are keyed as true of some other passage), then writes the reason in their own line.

**Grade 6, Whose eyes (RI.6.6).** At five spots the student picks the view and purpose (Helen remembering what it felt like; Sullivan reporting what worked, for another teacher; the biographer placing the morning in a life) and taps the words that carry it ("I", feeling words; dates and method words; "according to").

**Grade 6, Table and timeline (RI.6.9).** For five moments of the morning (the trouble before, the doll, who drew the water, the word understood, what came after) the student marks `both tell it the same`, `they differ` or `only one tells it`, taps the lines, and writes one comparison sentence. Only then does that moment light on the timeline row and its row land in the three-column table (only the memoir, only the letter, the biography adds). The student's five sentences print.

**Grade 7 (RI.7.3).** Text: "Up from Slavery" (1901), chapter 3, from overhearing two miners speak of Hampton through the sweeping of the recitation room (about 700 words, with cuts marked). People, events and ideas sit as cards (Washington, Mrs. Ruffner, Miss Mackie; the talk in the mine, the journey, the sweeping test; "a school where work pays the way", "do a thing thoroughly"). The student draws five threads: from one card to another, with its kind, and taps the passage at each end. Twelve threads are possible and seven are keyed as in the text; a thread the text does not support is turned back. Each thread gets a line: "__ led to __ because __."

**Grade 8 (RI.8.3, RI.8.6).** Text: Susan B. Anthony, "Is It a Crime for a Citizen of the United States to Vote?" (1873), the short form (about 550 words). First, five marked sentences: the student names the move (comparison, analogy, category, distinction), taps the two things it joins or separates ("we, the people" and "we, the white male citizens"; "persons" and "citizens"), and says what it makes a listener see. Second, five places where she states the other side: the student taps the objection, taps her answer, and names how she answers. A last line asks for her purpose in the student's own words, with one quote.

**Biographer's desk (extra, any grade, not counted).** The old conflict round: two eyewitnesses tell the water differently; the student chooses how a biography should write it and sees how biographers often handle it.

**On your own.** The last two items of each code run with Mr. Abernathy quiet: no example, nothing turned back, each part answered once, and nothing marked until both are in.

**The end.** A results strip for the teacher under each of the grade's codes: the two items on your own, right or not in their keyed parts, with the student's own lines beside them; then the counts for the three items before and anything printed as "shown".

At 1366x768 two texts fit side by side; at 680x425 texts are tabs.

## Content
- Grade 6 memoir and letter: exact text from Project Gutenberg eBook #2397 ("The Story of My Life", 1903, which prints Sullivan's letters in its supplement). Biography: written for Curio Class from sourced facts (born 1880 in Tuscumbia, Alabama; illness at 19 months; Sullivan arrived March 1887; graduated from Radcliffe College in 1904; a writer and activist for disability rights and other causes; died 1968).
- Grade 7: Booker T. Washington, "Up from Slavery" (1901), chapter 3, Project Gutenberg eBook #2376.
- Grade 8: Susan B. Anthony, "Is It a Crime for a Citizen of the United States to Vote?" (1873), the widely printed short form.
- The model pair (diary line and janitor's report), written for Curio Class.
- Keys for each path: for every item, the right pick, the lines or words that prove it, and what each wrong pick stands for.
- What a wrong answer on your own means. RI.6.3: "anecdote" chosen for every passage means any story is being called an anecdote and the passage's job is not being read. RI.6.6: the right author with words tapped that carry no view means the view is known from the label on the text and not found in it. RI.6.9: "the same" marked where the mug holds water in one and milk in the other means the texts are being skimmed for the story and not read against each other. RI.7.3: a thread drawn backward (the test caused the idea) means the order of events is standing in for cause. RI.8.3: "comparison" for every move means distinction and category are not yet apart from likeness. RI.8.6: an objection tapped that is Anthony's own view means the student does not hear when she is speaking in someone else's voice.
- Sensitivity read, left for the final review: how deafness and blindness are spoken of in 1903 (the tool presents Helen as a full person: her temper, humor, work and opinions, and not as an inspiration story); slavery, poverty and the words of the time in Washington's chapter; the speech's lines about race and sex in 1873. The reviewer sets the exact cuts.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Tags can be changed or removed; the table updates.
- The tool presents Helen as a full person: her temper, humor, work and opinions, not as an inspiration story.
- With Motion off threads appear without drawing.
- Access: every action works by tap and by keyboard. Words and lines are tapped or reached with arrow keys and chosen with Enter; a thread is drawn by drag, or by choosing its two cards in turn. Highlights carry a word label and a pattern, never color alone; threads say their kind in words. Motion can be paused.
- On your own: each part is answered once, with no feedback until both items are in.

## Look
- Accent `--brand` #5c4a7d lilac (header, tags frame, the table rule); gold #f4c542 (the lamp, highlights); paper #f6f4f9; ink #1c1528; muted #58546a. Scene: a quiet reading room.
- Contrast (WCAG 2.1, computed): white on brand 7.69:1; brand on paper 7.04:1; ink on paper 16.19:1; muted on paper 6.65:1; ink on gold 10.88:1.
- Never color alone: tags show their type in words; table columns have headings.
- Different from this batch (editor's red, blueprint blue, web green, lamp amber).

## Art
- Public domain: Library of Congress photographs "Helen Keller and Anne Sullivan" (1897, item 2004672077) and the 1893 seated portrait (item 97513763); the Art step checks each item's rights statement before use.
- Local FLUX (`scripts/localart.py`): reading desk with three documents (1); a water pump under a honeysuckle-covered well-house roof (1); no people.
About 4 images. Drawn in code: tags, threads, table, timeline.

## Voice
Bank voice `knowing-guide` as Mr. Abernathy (unique in this batch); the memoir is read by `gentle-storyteller`, the letter by `big-sister`, and the biography by `clear-teacher` (each unique in this batch); grade 7 and 8 texts by `clear-teacher`. `Curio.voice` with `scope: () => state.grade + ':' + state.text + ':' + state.item`, `welcomeAfter: true`.
- how `welcome`: "I'll do one of each first. Then it's your turn with the real texts."
- event, whole, `sentence`: the tapped sentence in its text's voice.
- how `jobHow`: "What does this passage do? Choose, then choose why the author does it here."
- how `eyesHow`: "Whose view shows here? Tap the words that carry it."
- how `compareHow`: "Same, different, or only one tells it? Tap the lines. Then write one sentence."
- how `threadHow`: "Choose two cards. Say how one moved the other. Tap the passage at each end."
- how `moveHow`: "Name the move. Tap the two things it joins or separates."
- how `answerHow`: "Tap where she states the other side. Tap her answer. Say how she answers."
- event `notYet`: "Not yet. Read it again."
- event `differ`: "Here they tell it differently: {who drew the water}."
- how `own`: "The last two are on your own. Answer each part once."
Every `how` line is also shown as text beside its control. Read speaks the hint, which names the next action and control and never a disabled one. Instructions use no idioms.

## Family engine
None. Tool-only code: span tagging, three-column table, threads, timeline row, conflict choice. (The evidence family's claims and links are for arguments; here tags describe presentation.)

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| What it does | Pick the same job each time; retag to what the tool says | Job and reason are one answer; a miss never names the answer; a second miss prints as shown. |
| Whose eyes | Read the author off the text's label | The words that carry the view must be tapped and are keyed. |
| Table | Move rows until none object | Rows land only after the student's mark, lines and sentence; nothing says why a mark was off. |
| Threads | Join any two cards | Seven of twelve threads are keyed, each needs its kind, direction and both passages. |
| Moves | Call everything a comparison | At least one of each move among five; the two ends must be tapped. |
| Other side | Tap any sentence | Objection and answer are a keyed pair and the kind of answer is picked from four. |
| On your own | Lean on turn-backs | Each part once, nothing marked until both are in. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the first text: title, `welcome` (queued, first time), then Mr. Abernathy's example (whole), waits.
2. Sentences: `sentence` (whole).
3. Grade 6: `jobHow`, `eyesHow`, `compareHow` (each first time); `differ` as a moment lights. Grade 7: `threadHow`. Grade 8: `moveHow`, `answerHow`.
4. `notYet` on a miss. Last two items of each code: `own`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RI.6.3, RI.6.6, RI.6.9, RI.7.3, RI.8.3, RI.8.6 wording | thecorestandards.org, Grades 6-8 | CCSS ELA 2010 PDF | yes |
| The memoir's account (mug and water, the broken doll, the well-house) and Sullivan's letter of April 5, 1887 (mug and milk, she pumped) | Project Gutenberg eBook #2397, chapter 4 and the April 5, 1887 letter (checked 2026-11-09) | Perkins School for the Blind, Helen Keller archive | yes |
| Born 1880 in Tuscumbia, Alabama; illness at 19 months; Sullivan arrived in March 1887; Radcliffe 1904; died 1968 | American Foundation for the Blind, Helen Keller biography | Library of Congress, Helen Keller | yes |
| Photographs of Keller and Sullivan, 1893 and 1897 | Library of Congress, items 97513763 and 2004672077 (checked 2026-11-09) | Perkins School for the Blind, photograph collection | yes |
Backed twice: 4. Cut: 0.

Sensitivity note: disability is presented plainly; Helen is a full person with opinions and a working life; the memoir's other chapters (not used) contain a dated description of a Black child, so only chapter 4 and the letter are used; the tool goes to the fresh-agent review.

Checks run (Python, scratchpad b17, 2026-11-09): the memoir passage contains "m-u-g" and "w-a-t-e-r" and the broken doll; the April 5 letter contains "mug" and "milk", "pump-house" and "while I pumped"; contrast as in Look.
Spec fix notes (2026-11-11): the Washington eBook number and the passage bounds, and the wording and length of the short form of Anthony's speech, were written from memory and not opened in this pass. Build must confirm both texts and count the seven keyed threads against the chapter.

## Done when
1. Focus and fold: at 1366x768 two texts fit; at 680x425 texts are tabs.
2. Grade 6: five passages take a job and a reason as one answer; five spots take a view and the words that carry it. (RI.6.3, RI.6.6)
3. Grade 6: five moments take a mark, lines and the student's comparison sentence before the timeline and table fill. (RI.6.9)
4. Grade 7: five threads take a direction, a kind and both passages, checked against the key. Grade 8: five sentences take a move and its two ends. (RI.7.3, RI.8.3)
5. Grade 8: five places take the objection, the answer and how she answers, and a purpose line with a quote. (RI.8.6)
6. A miss never names the answer; a second miss prints as shown. Mr. Abernathy's example plays first and can be reopened.
7. The last two items of each code run with no example or turn-backs; the end screen shows the result under each code. Print shows answers, table, lines and results.
8. Every spoken instruction is also on screen; each key word shows with an example at first use; the frames can be left.
9. Every action works by keyboard as well as tap, nothing is shown by color alone, and motion can be paused.
10. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
11. Motion off: threads appear without drawing; no network requests.

## Open questions
- For Cory: grades 7 and 8 now have their own texts (Washington, chapter 3; Anthony's 1873 speech), because a band tool needs each grade's own texts and RI.8.6 needs an author who answers the other side. Default used: these two. The old conflict round is kept as an extra that is not counted. Say if different texts are wanted.

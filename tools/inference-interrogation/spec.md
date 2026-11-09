# Inference Interrogation

## One idea
The student solves a short school mystery, "The Case of the Missing Trophy", by answering the detective's questions after each chapter, and every answer counts only when they drag in the exact line that proves it and tag it "says it" (stated outright) or "shows it" (inferred), writing the "so" for each inference; the final accusation needs three quotes, at least two of them inferences, and a red herring falls apart when its quote turns out to prove something else, so they learn the difference between what a text says and what it shows.

## Not like
- eyewitness-vs-reporter (4, spec): two accounts compared. Here one mystery and its clues.
- main-idea-pinboard (3-5, spec): grade 5 exact quotes for main ideas. Here quotes for inferences in fiction.
- theme-tracker (4, spec): details feeding themes. Here details proving facts of a case.
- question-cube (K-2, concept): question words. Here grade 5 quoting.
- stay-in-character (3, spec): predicting choices. Here proving what happened.

## Who and how
- Grade 5, ELA, module "Quoting and Inferring" (Reading Literature). Standard: RL.5.1.
- Driver: one student, or a pair as detective partners (tool.json `driver: "student"`). Every sentence is read on tap.
- Case 1 "The Case of the Missing Trophy" (four chapters, about 1,400 words); Case 2 "The Case of the Silent Bell" (harder inferences). tool.json `modes: ["Case 1", "Case 2"]`, `minutes: "30-40"`, `grades_label: "Grade 5"`.
- Nothing is saved; `Print` prints the notebook.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.5.1 (quote accurately) | Answer each question by dragging an exact span from the chapter; typed paraphrases bounce with "Quote it exactly" | the quote in quotation marks in the notebook | 2 |
| RL.5.1 (explicit) | Tag each answer "says it" when the line states the answer outright | the tag | 3 |
| RL.5.1 (inference) | Tag "shows it" and write the so: "She had chalk on her sleeve, so she had been near the board." | the so line under the quote | 3 |
| RL.5.1 | Wrong quotes still show what they do prove | the "this proves" note | 4 |
| RL.5.1 | Accuse: name the culprit with three quotes, at least two inferences; the red herring's quote proves something else | the accusation board | 5 |

## Screens and modes
Header (kit): title "Inference Interrogation"; `Cases`, `Notebook`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A school gym after the science fair, an empty trophy stand under a spotlight, and Detective Vance Okoro, a tall retired detective (now the school's crossing guard) in a long coat with a notebook. First hint: "Tap Chapter 1 to start reading." The first tap reads the chapter title; the welcome is queued after it (`welcomeAfter: true`).

**Chapter.** Numbered sentences, tap to hear. Suspects' cards line the top (four suspects with a picture and a one-line description).

**Questions.** After each chapter, two or three question cards ("Who was the last person in the gym?"). The student selects a span (tap the first and last word; spans stay inside one paragraph) and drags it to the notebook. Typing in the quote box is not allowed; a typed answer box is for the so line only. The span is checked against the key's accepted spans (a span counts if it contains a key span's core words and is no more than 10 words longer).

**Tag and so.** The student tags "says it" or "shows it". For "shows it", the so line frame: "___, so ___." The key lists the inference each shows-it span supports; the so line is checked for one of the key's idea word groups (generous forms) and is read back.

**Wrong quote.** A span that doesn't answer the question still gets a note of what it proves ("This proves Ms. Reyes locked the side door. Does it say who was last in the gym?").

**Accusation.** After chapter 4, the board shows the four suspects. The student names one and attaches three quotes from the notebook (at least two "shows it"). The red herring (Coach Briggs, seen carrying a big box) has a quote that feels right; when attached, the board shows what it really proves ("The box held the extra folding chairs, chapter 3"). The right accusation plays the reveal scene.

**Case 2.** The same flow with fewer stated answers and a case built on timing.

At 1366x768 the chapter and notebook fit side by side; at 680x425 the notebook is a tab.

## Content
Written for Curio Class:
- Case 1: The science fair trophy goes missing from the gym. Suspects: Coach Briggs (carrying a big box; red herring: chairs), Ms. Reyes (custodian, locks doors, cheerfully), Theo Park (fifth grader, lost to the winner; chalk on his sleeve from the scoreboard), Maya Ellis (the winner's older sister, a ninth grader helping set up, who hid the trophy as a joke to make her sister search for it and planned to put it back). The culprit is Maya; the reveal is gentle: she returns it and apologizes. Clues across chapters: glitter from the winner's poster on the storage closet handle; Maya's "I'll get the lights" when the lights stayed on; the closet key on the ring she borrowed for the poster supplies.
- Case 2: the school bell is silent; timing clues from a schedule and three accounts; culprit: a mouse nest in the bell box (no person did it), so the accusation board accepts "no suspect" with quotes.
- Key: each question's accepted spans with tags, inference idea word groups, and "what this proves" notes for 30 or more other spans per case.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Spans can be re-dragged; the notebook keeps the last answer per question.
- Pairs: one partner selects, the other tags; roles swap per chapter.
- No suspect is shamed: wrong accusations get "The quotes don't hold up. Look again." and the case continues.

## Look
- Accent `--brand` #3b3f6b detective navy (header, notebook cover, suspect frames); gold #f4c542 (spotlight, selected spans); paper #f4f4f9; ink #14152a; muted #535468. Scene: an empty school gym at dusk.
- Contrast (WCAG 2.1, computed): white on brand 9.96:1; brand on paper 9.08:1; ink on paper 16.37:1; muted on paper 6.75:1; ink on gold 11.03:1.
- Never color alone: tags are words; quotes are in quotation marks.
- Different from this batch (stage pink, film sepia, track teal, courtroom mahogany).

## Art
- People art goes to Gemini: Detective Okoro (an older Black man, retired detective, long coat, crossing guard vest, kind face), 4 poses; suspects (Coach Briggs, a white man in his fifties with a whistle; Ms. Reyes, a Latina custodian in her forties with a key ring; Theo Park, a Korean American boy about 10; Maya Ellis, a white teen about 14; the winner, Lily Ellis, about 10), 2 poses each; "illustrated mystery storybook character <description> <pose>, ink and watercolor, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): gym (2: day, dusk), storage closet (1), trophy stand (1), bell tower box (1); 16:9; no people.
About 21 images. Drawn in code: notebook, spans, accusation board.

## Voice
Bank voice `wise-mentor` as Detective Okoro (unique in this batch); chapters are read by `gentle-storyteller` (unique in this batch). `Curio.voice` with `scope: () => state.case + ':' + state.chapter + ':' + state.question`, `welcomeAfter: true`.
- how `welcome`: "Every answer needs proof. Drag the exact line that proves it, then tell me: does it say it, or show it?"
- event, whole, `sentence`: the tapped sentence.
- event `question`: the question card.
- event `exact`: "Quote it exactly. Drag the line from the story."
- event `proves`: "This proves {Ms. Reyes locked the side door}. Does it say {who was last in the gym}?"
- how `soHow`: "It shows it. Now write the so: what does this line tell you?"
- event `herring`: "That box held {the extra folding chairs}. It proves something else."
- event `solved`: "Case closed. Three quotes, and they hold up."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: span picking within a paragraph, key matching, tags and so lines, accusation board.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Quote | Select a whole paragraph | Spans may be at most 10 words longer than the key span; long spans get "Narrow it to the line that proves it." |
| Tags | Tag all "says it" | Each key span has a set tag; wrong tags get "Does it say that in words?" |
| So line | Type anything | Read back aloud; the idea word check asks again when it misses. |
| Accusation | Accuse everyone in turn | Each needs three attached quotes, two inferences; wrong accusations show what the quotes prove. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap Chapter 1: title, `welcome` (queued, first time).
2. Sentences: `sentence` (whole). Questions: `question`.
3. Answers: `exact`, `proves` as they fire; shows-it tags: `soHow` (first time).
4. Accusation: `herring` if attached; `solved`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.5.1 wording | thecorestandards.org, Reading Literature Grade 5 | CCSS ELA 2010 PDF | yes |
| Explicit information is stated in the text; an inference combines text clues with what the reader knows | Reading Rockets, making inferences | ReadWriteThink, inference lessons | yes |
Backed twice: 2. Cut: 0.

Design choices (not claims): the 10-word span allowance; the two-inference rule for the accusation.

Sensitivity note: the culprit is a teen who meant it as a joke and makes it right; people art goes to the fresh-agent review; the custodian is not a suspect by stereotype, and her clue clears her.

Checks run (Python, scratchpad b15, 2026-11-09): in the sample key, Case 1 has at least three shows-it spans that point at Maya and the red herring's span proves a different fact; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the chapter and notebook fit; at 680x425 the notebook is a tab.
2. Answers take exact spans only; typed quotes are not possible. (RL.5.1)
3. Tags and so lines work. (RL.5.1)
4. Wrong spans show what they prove. (RL.5.1)
5. The accusation needs three quotes, two inferences; the red herring exposes itself.
6. Case 2 accepts "no suspect" with quotes.
7. Print shows the notebook.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: the spotlight is still; no network requests.

## Open questions
- None for Cory.

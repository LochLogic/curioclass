# Draft Versus Draft

## One idea
Two revisions of the same student letter face off for a named reader and purpose ("Your principal, who has two minutes, deciding whether to add water bottle filling stations"); the student picks the winner, the tool marks every change as a cut, add, move or reword, a panel of three readers reacts to each draft so the same change can help one reader and lose another, and then the student revises the original themselves for a different reader with the same four tools and sees their change map beside A and B, so they learn that revision is choosing changes for someone, not polishing at random.

## Not like
- draft-car-wash (3-5, concept): stations for add, cut, move and polish. Here whole revisions compared for a reader, grades 6-8.
- editors-in-the-margin (9-12, concept): answering three editors' notes. Here two revisions and a reader panel.
- audience-shift-briefing (9, concept): spoken briefings. Here written letters.
- docent-tour-talk (6-8, spec): a spoken opening for three audiences. Here written revision with a change map.
- essay-rope-team (5, spec): ordering an essay. Here revising for a reader.

## Who and how
- Grades 6-8, ELA, module "Revising for Purpose and Audience" (Writing and Language). Standards: W.6.4, W.6.5, W.7.4, W.7.5, L.7.3, W.8.4, W.8.5.
- Driver: one student; class mode is a projector showdown (tool.json `driver: "student"`). Every sentence is read on tap; the student's revision is read back by the browser's speech voice.
- Grade picker: 6 (letter to the principal), 7 (adds the wordiness meter), 8 (a city council letter and a new-approach round). tool.json `modes: ["Grade 6", "Grade 7", "Grade 8", "Class showdown"]`, `minutes: "25-40"`, `grades_label: "Grades 6-8"`.
- Saving: the student's revision is kept in this browser; footer: "Your revision stays on this device." `Clear my revision` removes it.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| W.6.4, W.7.4, W.8.4 | Vote A or B for the reader card, then say for each change mark whether it helped this reader | the change marks and the helped or hurt choice | 2 |
| W.6.5, W.7.5 | Watch the reader panel react: the same change helps one reader and loses another | three reader faces with a line each | 3 |
| W.6.5, W.7.5 | Revise the original for a new reader with cut, add, move and reword | the student's change map beside A and B | 4 |
| L.7.3 | Grade 7: the wordiness meter counts redundant phrases; cut them | the meter and lit phrases | 5 |
| W.8.5 | Grade 8: a new-approach round turns the letter into a one-page flyer | the flyer frame | 6 |

## Screens and modes
Header (kit): title "Draft Versus Draft"; `Showdown`, `My revision`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** An editor's desk with two drafts side by side under a reader card, and three reader chairs behind: the principal (Dr. Ruiz), a parent from the PTA (Mr. Abbott) and a fifth grader (Kenzie). First hint: "Tap Draft A to hear it." The first tap reads the draft's title; the welcome is queued after it (`welcomeAfter: true`).

**Showdown.** The original letter (about 250 words, a sixth grader asking for water bottle filling stations) was revised two ways. Draft A cuts the long story about a field trip and leads with the request and the cost; Draft B adds a story about a thirsty soccer practice and a joke. The reader card names the reader and purpose. The student votes A or B.

**Change marks.** After the vote, marks appear on both drafts: cuts (struck through, labeled "cut"), adds (underlined, "add"), moves (an arrow, "move"), rewords (a swap, "reword"). For each mark the student picks helped, hurt or no difference for this reader, and the tool shows the key's reading for that reader with a one-line reason.

**Reader panel.** Each reader reacts to each draft with a face and a line set in data: Dr. Ruiz likes A's cost first ("I can decide in two minutes"), Kenzie likes B's story ("That's what practice is like!"), Mr. Abbott wants the number of students it would serve, which neither draft has.

**My revision.** A new reader card (Kenzie's class newsletter, or Mr. Abbott for a PTA vote). The student revises the original with four tools: select and Cut; place the cursor and Add; drag a sentence to Move; select and Reword. Each change is logged as a mark. The tool shows the student's change map beside A's and B's, and the reader panel reacts to the student's version by rules (for example, Mr. Abbott smiles if a number of students is added; Kenzie if the first sentence is under 15 words).

**Wordiness meter (grade 7).** Counts phrases from a list of 40 redundancies ("in my opinion I think", "each and every", "the reason why is because", "past history"); each lit phrase can be tapped to see a shorter form.

**New approach (grade 8).** The reader is a city council member and the letter becomes a one-page flyer: a headline, three bullets, one number, one ask. Line edits alone don't fit the frame.

**Class showdown.** The projector shows A and B; the class votes by count; then the marks reveal.

At 1366x768 the two drafts fit side by side; at 680x425 they are tabs.

## Content
Written for Curio Class:
- The original letter, Draft A and Draft B for grade 6; a tighter-organization pair for grade 7; a city council pair for grade 8.
- Change-mark keys per reader with reasons; the reader panel's lines and reaction rules.
- Redundancy list: 40 phrases with shorter forms.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The student's revision autosaves; Undo steps back one change.
- Marks and reactions are advice; the vote has no right answer, and the tool shows that each draft wins for one reader.
- With Motion off the faces change without animation.

## Look
- Accent `--brand` #a3361f editor's red (header, change marks frame, vote buttons); gold #f4c542 (the winning draft's ribbon, lit phrases); paper #fcf4f2; ink #2a0d07; muted #67524d. Scene: a cluttered, friendly editor's desk.
- Contrast (WCAG 2.1, computed): white on brand 6.76:1; brand on paper 6.24:1; ink on paper 16.70:1; muted on paper 6.70:1; ink on gold 11.14:1.
- Never color alone: marks carry words (cut, add, move, reword) and shapes.
- Different from this batch (blueprint blue, web green, lilac, lamp amber).

## Art
- People art goes to Gemini: Dr. Ruiz (a Latina woman in her fifties, principal's lanyard), Mr. Abbott (a white man in his forties, PTA t-shirt), Kenzie (a Black girl about 10 in a soccer jersey), 3 faces each (pleased, unsure, lost); "illustrated school community member <description> <face>, warm gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): editor's desk (1), a water bottle filling station (1); no people.
About 11 images. Drawn in code: marks, meter, flyer frame.

## Voice
Bank voice `bright-teacher` as the host (unique in this batch); readers: Dr. Ruiz `calm-professor`, Mr. Abbott `friendly-dad`, Kenzie `playful-friend` (each unique in this batch). `Curio.voice` with `scope: () => state.grade + ':' + state.view + ':' + state.mark`, `welcomeAfter: true`.
- how `welcome`: "Same letter, two revisions. Which one works better for this reader? Vote, then we'll see every change."
- event, whole, `sentence`: the tapped sentence.
- how `markHow`: "For each change, did it help this reader, hurt, or make no difference?"
- event `keyReading`: "For {Dr. Ruiz}, this {cut} {helped}: {she can find the ask fast}."
- event `react`: the reader's line in their voice.
- how `reviseHow`: "Now it's yours. New reader. Cut, add, move or reword."
- event `wordy`: "{In my opinion I think} can be {I think}."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: change marks on two drafts, reader panel rules, revision editor with a change log, wordiness list, flyer frame.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Vote | Always pick A | There's no right vote; the marks and panel show who each draft serves. |
| Marks | Mark everything "helped" | Each mark shows the key's reading for this reader with a reason. |
| My revision | Make no changes | The change map shows none, and the panel's rules don't fire. |
| Wordiness | Ignore it | The meter's count stays and prints. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap Draft A: title, `welcome` (queued, first time).
2. Sentences: `sentence` (whole). After the vote: `markHow` (first time), `keyReading` per mark.
3. Panel: `react` per reader (each waits).
4. My revision: `reviseHow`; grade 7: `wordy` on tap.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| W.6.4 to W.8.5 and L.7.3 wording | thecorestandards.org, Writing and Language Grades 6-8 | CCSS ELA 2010 PDF | yes |
| Revision means changing content and organization for a purpose and audience, beyond editing for correctness | Purdue OWL, the writing process: revision | ReadWriteThink, revision strategies (add, cut, move, replace) | yes |
| Redundant phrases such as "past history" and "each and every" can be cut to their shorter forms | Purdue OWL, conciseness | Merriam-Webster, usage notes on redundancy | yes |
Backed twice: 3. Cut: 0.

Design choices (not claims): the reader panel's lines; the 15-word first-sentence rule for Kenzie.

Checks run (Python, scratchpad b17, 2026-11-09): in the sample keys each of the three readers prefers a different draft or neither, and every redundancy in the sample list is longer than its shorter form; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 two drafts fit; at 680x425 they're tabs.
2. Votes and change marks with helped, hurt or no difference work. (W.6.4, W.7.4, W.8.4)
3. The reader panel reacts per draft. (W.6.5, W.7.5)
4. My revision logs cut, add, move and reword and shows the change map. (W.6.5, W.7.5)
5. The grade 7 wordiness meter lights and shortens phrases. (L.7.3)
6. The grade 8 flyer round works. (W.8.5)
7. The revision survives a reload where storage works; `Clear my revision` removes it.
8. Class showdown tallies and reveals.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: faces change without animation; no network requests.

## Open questions
- None for Cory.

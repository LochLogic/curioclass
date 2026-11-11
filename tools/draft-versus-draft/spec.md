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
- Driver: one student; class mode is a projector showdown (tool.json `driver: "student"`). Role: lesson. Every sentence is read on tap; the student's revision is read back by the browser's speech voice.
- Three grade paths, each with its own letter, its own pair of drafts, its own three readers and that grade's wording on the goal card. No path needs another.
  - Grade 6, a letter to the principal asking for water bottle filling stations. W.6.4: produce clear and coherent writing in which the development, organization and style are appropriate to task, purpose and audience. W.6.5: with some guidance, develop and strengthen writing as needed by planning, revising, editing, rewriting or trying a new approach.
  - Grade 7, a letter to the town librarian asking for a teen study hour. W.7.4: as grade 6. W.7.5: as grade 6, focusing on how well purpose and audience have been addressed. L.7.3: choose language that expresses ideas precisely and concisely, recognizing and eliminating wordiness and redundancy.
  - Grade 8, a letter to a city council member asking for a crosswalk. W.8.4: as grade 6. W.8.5: as grade 7.
- Change note (spec fix, 2026-11-11): the desk, the two drafts, the reader chairs, the change marks, the four revision tools and the showdown stay. Before, the grades shared most of one letter, each mark was a pick from three with the key shown at once, the panel's rules were only hinted at, the meter lit the wordy phrases for the student, the flyer had no check, and no one planned, edited or wrote anything of their own. Now a mark is a call plus the reader's need it touches, judged together with nothing shown on a miss; every reader has three stated needs; the student plans, revises with a reason for each change, edits five unmarked slips, and tries a new approach in every grade; grade 7 finds the wordy phrases unaided; and each path ends with a short piece written from nothing for a new reader. The host works a model first. Added the three hooks.
- English learners: every spoken line is also on screen in short sentences. The words draft, revise, reader, purpose, cut, add, move, reword and wordy each show with one marked example from the host's model the first time they are used. The fresh note offers frames the student may take or leave ("I am writing to ask __."). Instructions use no idioms.
- tool.json `modes: ["Grade 6", "Grade 7", "Grade 8", "Class showdown"]`, `minutes: "25-40"` a sitting (two sittings a path), `grades_label: "Grades 6-8"`.
- Saving: the student's revision is kept in this browser; footer: "Your revision stays on this device." `Clear my revision` removes it.

## Standards map
| Code | The standard's verb and its parts | Who does the verb | Student action that teaches it | Items that differ | What they see | Done when check |
|---|---|---|---|---|---|---|
| W.6.4, W.7.4, W.8.4 | produce clear, coherent writing whose development, organization and style fit task, purpose and audience | the student | For eight change marks, call each helped, hurt or no difference for this reader and name the reader's need it touches; then write a fresh note of five sentences or more for a new reader | 8 marks (at least 2 of each call; development, organization and style each marked), 1 fresh note | the marks; the note with the reader's three needs | 2, 7 |
| W.6.5, W.7.5, W.8.5 | develop and strengthen writing by planning, revising, editing, rewriting or trying a new approach (grades 7 and 8: focused on purpose and audience) | the student | Plan: choose and order the new reader's needs. Revise: five or more changes, each with the need it serves. Edit: find and fix five slips. New approach: start one part again a different way | 1 plan, 5 changes, 5 slips, 1 new approach | the change map, the reader panel, the edit count | 3, 4, 6 |
| L.7.3 | choose language that is precise and concise; recognize and eliminate wordiness and redundancy | the student | Find eight wordy or redundant phrases in a paragraph with nothing lit, shorten each, and swap three vague words for exact ones | 8 phrases, 3 words, 2 sentences on your own | the paragraph and a count only | 5 |

## Screens and modes
Header (kit): title "Draft Versus Draft"; `Showdown`, `My revision`, `Fresh note`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word. The goal card gives the grade's standards in their own words.

**On load and first tap.** An editor's desk with two drafts side by side under a reader card, and three reader chairs behind. First hint: "Tap Draft A to hear it." The first tap reads the draft's title; the welcome is queued after it (`welcomeAfter: true`).

**Readers and their needs.** Every reader card lists three needs in plain words, and each need has a rule the tool can check.
- Grade 6: the principal, Dr. Ruiz (the ask in the first two sentences; a cost or a number; polite, formal words); a PTA parent, Mr. Abbott (how many students it serves; who pays; a next step); a fifth grader, Kenzie (a first sentence under 15 words; a story from school life; no hard words left unexplained).
- Grade 7: the librarian, Ms. Okoye (what is asked and when; why the library and not the school; an offer to help); a library board member (a number of teens; a cost; what other towns do); a classmate (a plain first sentence; what is in it for them; where to sign).
- Grade 8: a council member (the ask and the place in the first two sentences; a count or a date from the record; what it costs); a neighbor who drives that road (how it changes the drive; a safety fact; a fair tone toward drivers); a younger student who walks it (a short first sentence; what to do now; a friendly voice).

**The host goes first (the model).** On a four-sentence note asking a coach for new cones, the host makes one change for the coach, says which need it serves, calls one of someone else's changes "hurt" and says why, and fixes one slip. It cannot be skipped the first time and `The host's example` reopens it, except on the items on your own.

**Showdown.** The grade's original letter (about 250 words) was revised two ways, one draft built for each of two readers. The reader card names the reader and purpose. The student votes A or B; the vote is not scored.

**Change marks.** After the vote, eight marks appear across both drafts: cuts (struck through, labeled "cut"), adds (underlined, "add"), moves (an arrow, "move"), rewords (a swap, "reword"). For each the student picks helped, hurt or no difference for this reader and which of the reader's three needs it touches (or "none of them"). Call and need are one answer. A miss says only "Read it as {Dr. Ruiz} would" and shows nothing; after a second miss the host gives the reading with its reason and the mark prints as "shown". Marks cannot be changed after they are judged.

**Reader panel.** Each reader reacts to each draft with a face, a word ("pleased", "lost", "wants more") and a line set in data, and their three needs show met or not met.

**My revision.** A new reader card (the third reader). Four steps.
1. Plan: from six cards, the student chooses the three this reader needs and puts them in the order the letter should meet them. The three are keyed; the plan is judged once the student taps `Plan set`.
2. Revise: the student changes the original with four tools: select and Cut; place the cursor and Add; drag a sentence to Move; select and Reword. Each change is logged as a mark and the student picks the need it serves. Five changes or more, with at least one cut and one add. The reader panel reacts to the student's version by the reader's three rules, only when the student taps `Ask the readers`, and at most three times.
3. Edit: the original carries five slips of convention for that grade (a run-on, a missing capital, a wrong homophone, a missing comma after an opener, a subject and verb that do not agree), none marked. The student taps and fixes; six marks; `Check` gives a count first, one more pass, then the rest are shown.
4. New approach: the student picks one part (grade 6, the opening; grade 7, the opening or the close) and writes it again from a blank box a different way (a question, a number, a short story), then keeps the one that serves the reader better and says why. Grade 8 turns the whole letter into a one-page flyer: a headline of eight words or fewer that holds the ask, three bullets each tagged to a different need of the reader, one number taken from the letter, and one ask that starts with a verb. Each part is checked against those rules.
The student's change map sits beside A's and B's.

**Wordiness (grade 7).** A paragraph of the grade 7 letter with eight wordy or redundant phrases ("in my opinion I think", "each and every", "the reason why is because", "past history") and nothing lit. The student taps a phrase and types a shorter form that keeps the meaning; ten marks for eight phrases; the meter shows only how many are left. Then three vague words are swapped for exact ones from the student's own head (no list).

**Fresh note (on your own).** A fourth reader card with its three needs (grade 6, the custodian; grade 7, the school newspaper; grade 8, a local shop owner). The student writes five sentences or more from a blank box, with no draft, no host, no panel and no frames unless opened, taps the words that meet each need, and hands it in once. Beside it, a short five-sentence draft for that reader takes two changes with their needs and two slip fixes, with nothing marked until all are in. Grade 7 also rewrites two wordy sentences.

**The end.** A results strip for the teacher by code. Production code (W.6.4, W.7.4 or W.8.4): the fresh note's needs met out of three, with the note printed. Process code (W.6.5, W.7.5 or W.8.5): on the short draft, changes that served the need named out of two and slips fixed out of two; then the plan, edit count and new approach from the guided part. L.7.3: the two sentences, shorter and same meaning or not. Marks printed as "shown" are listed.

**Class showdown.** The projector shows A and B; the class votes by count; then the marks are taken one at a time by show of hands before each reading is shown.

At 1366x768 the two drafts fit side by side; at 680x425 they are tabs.

## Content
Written for Curio Class:
- For each grade: the original letter with five seeded slips, Draft A and Draft B, eight change marks keyed for the showdown reader (call, need touched, reason), three readers with three needs and a rule each, six plan cards, a fourth reader, a short five-sentence draft with two slips, and the host's cones note.
- Grade 7: the wordiness paragraph with eight keyed phrases and accepted shorter forms, and two sentences for the end. Redundancy list: 40 phrases with shorter forms, used for judging and never shown.
- Grade 8: the flyer frame and its rules.
- What a wrong answer on your own means. A fresh note that meets none of the reader's needs: the student wrote what they wanted to say and did not read the card. A note that meets the needs in one long sentence each with no order: purpose is there and organization is not. A change tagged to a need it does not serve: revising is being done by feel ("it sounds better"). Slips left: the student rereads for meaning and does not yet read for conventions as a separate pass. Grade 7, a shorter sentence that drops the point: cutting is being done by length and not by meaning; "past history" left in: the pair is not heard as saying one thing twice.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The student's revision autosaves; Undo steps back one change.
- The vote has no right answer, and the panel shows that each draft wins for one reader. The marks do have keyed readings for the named reader.
- Access: every action works by tap and by keyboard. Text is selected with taps on its first and last word or with Shift and arrow keys; Move works by drag, or by pick up and place. Change marks carry a word label and a shape (strike, underline, arrow, swap), never color alone; reader faces carry a word. Read-back has its words on screen. Motion can be paused.
- On your own: the note is handed in once; the short draft's four answers get no feedback until all are in.
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
- event `asReader`: "Read it as {Dr. Ruiz} would."
- how `needHow`: "Did it help, hurt, or make no difference? Then choose the need it touches."
- how `planHow`: "Choose the three things this reader needs. Put them in order. Then tap Plan set."
- how `editHow`: "Five slips are hiding in the letter. Tap each one and fix it."
- how `tryHow`: "Write this part again a different way. Keep the better one and say why."
- how `own`: "New reader, blank page, on your own. Hand it in once."
- event, whole, the host's example.
Every `how` line is also shown as text beside its control. Instructions use no idioms.

## Family engine
None. Tool-only code: change marks on two drafts, reader panel rules, revision editor with a change log, wordiness list, flyer frame.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Vote | Always pick A | The vote is not scored. |
| Marks | Mark everything "helped"; wait for the key | Call and need are one answer, at least two marks have each call, a miss shows nothing, and marks cannot be redone after judging. |
| Plan | Take the first three cards | Three of six are keyed for this reader, in an order, judged once. |
| My revision | Make no changes; ask the readers after every keystroke | Five changes with a cut and an add, each tagged to a need; the panel answers three times at most. |
| Edit | Mark every word | Six marks for five slips and a count first. |
| Wordiness | Wait for the lights | Nothing is lit; ten marks for eight phrases; the shorter form must keep the meaning. |
| Flyer | Fill the boxes with anything | Headline, bullets, number and ask each have a rule tied to the letter and the reader's needs. |
| On your own | Lean on the panel | No panel, one hand-in. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap Draft A: title, `welcome` (queued, first time), then the host's example (whole), waits.
2. Sentences: `sentence` (whole). After the vote: `needHow` (first time); `asReader` on a miss; `keyReading` only for a mark that is shown.
3. Panel: `react` for each reader (each waits).
4. My revision: `planHow`, `reviseHow`, `editHow`, `tryHow`; grade 7: `wordy` only after a phrase is found.
5. Fresh note: `own`.

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
1. Focus and fold: at 1366x768 two drafts fit; at 680x425 they are tabs.
2. Each grade has its own letter, drafts and readers. Eight change marks take a call and the need touched as one answer; a miss shows nothing and a second miss prints as shown. (W.6.4, W.7.4, W.8.4)
3. Every reader has three stated needs with rules, and the panel shows each met or not for each draft. (W.6.5, W.7.5, W.8.5)
4. My revision takes a plan judged once, five or more changes each tagged to a need, and an edit of five unmarked slips with a count first; the panel answers on request, three times at most. (W.6.5, W.7.5, W.8.5)
5. Grade 7 finds and shortens eight unlit phrases and swaps three vague words. (L.7.3)
6. The new approach is written from a blank box in grades 6 and 7; the grade 8 flyer is checked part by part. (W.6.5, W.7.5, W.8.5)
7. The fresh note is written from nothing for a fourth reader and handed in once, with the short draft's changes and fixes; the end screen shows results by code.
8. The host's example plays first and can be reopened. The revision survives a reload where storage works; `Clear my revision` removes it. Print shows the revision, the note and the results.
9. Class showdown tallies and takes the marks by show of hands.
10. Every spoken instruction is also on screen; each key word shows with a marked example at first use; the frames can be left.
11. Every action works by keyboard as well as tap, nothing is shown by color alone, and motion can be paused.
12. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
13. Motion off: faces change without animation; no network requests.

## Open questions
- None for Cory.

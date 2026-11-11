# Pause and Break

## One idea
A reading voice pauses exactly where the punctuation tells it to, and the student adds, moves or removes commas, parentheses, dashes and ellipses on a strip of tape until the sentence sounds the way the writer meant (an aside set off softly or loudly, two adjectives balanced, a thought that trails off, a quotation with words left out), comparing their pause pattern with the target's gaps on a waveform, so they learn that these marks are instructions to the reader's voice and mind.

## Not like
- comma-chameleon (4, spec): commas that change a picture. Here commas, parentheses, dashes and ellipses as pauses, grades 6-8.
- punctuation-power-ups (10, concept): semicolons and colons. Here asides, adjective pairs, breaks and omissions.
- parallel-parking (9, concept): parallel structure. Here punctuation and pauses.
- tense-time-line (5, spec): verbs and time. Here punctuation and voice.
- sentence-remixer (6, spec): combining sentences. Here marking them.

## Who and how
- Grades 6-8, ELA, module "Commas, Dashes and Ellipses" (Language). Standards: L.6.2a, L.7.2a, L.8.2a, L.8.2b. The spelling parts (L.6.2b, L.7.2b, L.8.2c) are not taught here.
- Driver: one student, or partners in the "read it as written" game (tool.json `driver: "student"`). Every sentence is played on tap.
- Grade picker sets the levels: 6 (asides with commas, parentheses or dashes), 7 (coordinate adjectives), 8 (dashes for breaks, ellipses for pauses and omissions). tool.json `modes: ["Grade 6", "Grade 7", "Grade 8", "Partner game"]`, `minutes: "15-25"`, `grades_label: "Grades 6-8"`.
- Nothing is saved; `Print` prints the final paragraph.
- Role: practice (a station), with Reel-E's first three levels in each grade as the model. Each grade is its own path of twelve levels, same-words levels, a final paragraph and four sentences on your own, under that grade's wording on the goal card: grade 6, set off nonrestrictive or parenthetical elements with commas, parentheses or dashes; grade 7, use a comma to separate coordinate adjectives; grade 8, use a comma, an ellipsis or a dash to show a pause or break, and an ellipsis to show an omission.
- Change note (spec fix, 2026-11-11): the tape, Reel-E, the pause table and the pictures stay. Matching can no longer be done by trial: after the three model levels the target's waveform is hidden and the student locks the marks before anything plays. Grade 7 is no longer one comma-or-none choice a pair: the student predicts the swap test and marks whole sentences. Grade 8 now uses the comma as a pause mark beside the dash and the ellipsis, and has four omission levels. Added the three hooks.
- English learners: every sentence is on the tape as it plays, and every instruction is on screen in short sentences. The words aside, extra information, coordinate adjectives, dash, ellipsis and omission each show with a marked example and its picture the first time they are used. Instructions use no idioms.

## Standards map
| Code | The standard's verb and its parts | Who does the verb | Student action that teaches it | Items that differ | What they see | Done when check |
|---|---|---|---|---|---|---|
| L.6.2a | use punctuation (commas, parentheses, dashes) to set off nonrestrictive or parenthetical elements | the student | Say whether the words are extra or needed (pick the picture), choose the pair of marks for a soft or a strong aside, place both halves, lock, then hear it | 12 levels (4 commas, 3 parentheses, 3 dashes, 2 with no aside to set off), 3 same-words, 4 on your own | the tape and the student's marks; waveforms after the lock | 2 |
| L.7.2a | use a comma to separate coordinate adjectives | the student | For each pair say whether it would still sound right swapped with "and", then mark the whole sentence and lock | 12 sentences holding 20 pairs (11 coordinate, 9 not), 3 same-words, 4 on your own | the swap test played only after the prediction | 3 |
| L.8.2a | use punctuation (comma, ellipsis, dash) to indicate a pause or break | the student | Choose the mark for a short pause, a trailing pause or a sudden break, place it, lock | 8 levels (3 comma, 2 ellipsis, 3 dash), 2 on your own | the tape; waveforms after the lock | 4 |
| L.8.2b | use an ellipsis to indicate an omission | the student | Compare the full quotation with the cut one, place the ellipsis where words were removed, and say whether the cut changed the meaning | 4 levels (1 changes the meaning), 2 on your own | both quotations | 4 |
| L.6.2a to L.8.2b | as above, in connected writing | the student | Punctuate the final paragraph from scratch | 1 paragraph a grade | the paragraph, then its playback | 5 |

## Screens and modes
Header (kit): title "Pause and Break"; `Levels`, `Final`, `Partner`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A sentence on a strip of masking tape across a recording desk, a play button and a "how it should sound" card with a waveform showing the target's gaps. The host is a reel-to-reel tape machine called Reel-E with blinking meters. First hint: "Tap Play target to hear how it should sound." The first tap plays the target; the welcome is queued after it (`welcomeAfter: true`).

**A level.** The sentence's words sit on the tape with drop slots between them. A mark tray: comma, pair of commas, pair of parentheses, pair of dashes, single dash, ellipsis. `Play mine` reads the sentence as punctuated. Pauses come from a fixed table (comma 250 ms, dash 400 ms, ellipsis 700 ms, parentheses 250 ms with the words inside 10 percent quieter, dashes 250 ms with the words inside 10 percent louder), built into the playback so the voice always honors the marks: each sentence is played as recorded word groups joined by the table's silences, not as free text-to-speech. Under the strip, two waveforms: target and mine; the gaps line up when the marks match.

**Lock before you listen.** In levels 1 to 3 of each grade Reel-E shows how it works: the target waveform is in view and `Play mine` is free. From level 4 the target's waveform is hidden. The student may hear the target read aloud, places the marks, and taps `Lock`. Only then do `Play mine` and both waveforms show. If the marks are off the student gets one change and one more lock; after a second miss Reel-E places the marks and says why, the level prints as "shown", and a twin level with new words is added.

**Grade 6.** Asides: "My cousin, who lives in Ohio, sent a postcard." versus "My cousin who lives in Ohio sent a postcard." (two cousins). A picture shows the meaning of each version. Three marks for asides; the tool asks "Should the aside sound like a whisper or a shout?" and the target uses one.

**Grade 7.** Each sentence holds one, two or three adjective pairs ("The tired, hungry hikers found a small wooden cabin."). For each pair the student first predicts: `still sounds right swapped` or `sounds wrong swapped`. Then the swap test plays that pair flipped with "and" between. Then the student marks the whole sentence and locks it; the sentence is judged as a whole.

**Grade 8.** Eight levels ask which mark the voice needs: a comma for a short pause ("Well, I suppose so."), an ellipsis for a trailing pause, a dash for a sudden break. Four omission levels follow. Breaks and pauses: "I was about to say yes, but then I saw the clock." becomes "I was about to say yes but then I saw the clock." Omissions: a quotation from a public-domain speech with a cut; the student places the ellipsis where words were removed, and a check shows the full quotation and asks whether the shortened one still means the same (one level's cut changes the meaning, and the student must say so).

**Same words, two meanings.** One level per grade where the same words with different marks say two things aloud ("The coach said the captain is late." against "The coach, said the captain, is late."), each with a picture of who is late.

**Final.** A short paragraph with no marks; the student punctuates it from scratch and locks it once; the target plays after.

**On your own.** Four new sentences for the grade, with Reel-E quiet: no target reading, no waveform, no swap button, one lock each, and nothing is marked until the fourth is locked. In grade 8, two are pauses or breaks and two are omissions.

**The end.** A results strip for the teacher under the grade's code or codes: sentences right out of four on your own, with the marks the student placed on each one missed; the final paragraph's marks right out of its total; levels printed as "shown".

**Partner game.** One partner reads a marked sentence aloud from the screen; the other hears it and places the marks on a blank copy; then both play the target.

At 1366x768 the tape, tray and waveforms fit; at 680x425 the waveforms stack.

## Content
Written for Curio Class: 12 levels per grade with a twin for each, 3 same-words levels, a final paragraph and 4 sentences on your own per grade. Grade 6 has two levels where the clause is needed and takes no marks. Grade 7's 12 sentences hold 20 pairs, 11 coordinate and 9 not. Grade 8 has 8 pause and break levels and 4 omission levels. Omission quotations from Abraham Lincoln's Gettysburg Address (1863, public domain), using the Bliss copy's text.
- What a wrong answer on your own means. Grade 6: one comma with no partner means the aside is not seen as a unit with two ends; marks around words the sentence needs means marks are being placed by breath and not by meaning. Grade 7: a comma in "a bright red kite" means every pair of adjectives is being split; no comma in "a cold, dark night" means the swap test is not being run in the head. Grade 8: an ellipsis for a sudden break means pause and break are not yet apart; an ellipsis in the wrong place in a quotation means the cut was not checked against the full text; saying a cut kept the meaning when it dropped a "not" means only the words left are being read.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Marks snap to slots; pairs place both halves.
- With Motion off the meters don't move.
- Word groups for every level are recorded with the level's bank voice and stored locally.
- Access: every action works by tap and by keyboard. A mark can be dragged to a slot, or picked with a tap and placed with a tap, or with arrow keys and Enter. Sound is never the only carrier: each gap on the waveform is labeled "short pause", "long pause" or "break", the aside's band is labeled "softer" or "louder", and the words stay on the tape, so every level can be done with Sound off. Motion can be paused.
- On your own: one lock a sentence, no feedback until the fourth is locked.

## Look
- Accent `--brand` #2f4858 studio slate (header, tape desk, mark tray); gold #f4c542 (the tape, matching gaps); paper #f3f6f7; ink #0f1a20; muted #505b61. Scene: a small recording studio.
- Contrast (WCAG 2.1, computed): white on brand 9.59:1; brand on paper 8.83:1; ink on paper 16.26:1; muted on paper 6.42:1; ink on gold 10.86:1.
- Never color alone: gaps carry lengths in words (short, long, trailing); marks are shapes.
- Different from this batch (camera purple, raspberry, mixer cyan, press olive).

## Art
Local FLUX (`scripts/localart.py`), no people.
- studio desk (1); Reel-E (4 poses: play, listen, blink, cheer), "A friendly vintage reel-to-reel tape recorder character with meter eyes <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- meaning pictures (12): "<two cousins at two houses / one cousin with a postcard / a bright red kite / a cold dark night street>, flat sticker style"; 1:1.
About 14 images. Drawn in code: tape, slots, waveforms, meters.

## Voice
Bank voice `news-reader` reads every sentence and is Reel-E's voice (unique in this batch). `Curio.voice` with `scope: () => state.grade + ':' + state.level`, `welcomeAfter: true`.
- how `welcome`: "Punctuation tells my voice when to pause. Make my reading match the target."
- event, whole, `target`: the target reading.
- event, whole, `mine`: the student's reading.
- event `match`: "Every pause matches."
- event `swap`: "{Dark, cold night}. Still sounds right? Then it gets a comma."
- event `meaning`: "Did the cut change what {Lincoln} meant?"
Read speaks the hint, which names the next action and control and never a disabled one.
- how `lock`: "Place your marks. Then tap Lock to hear it."
- how `predict`: "Would it still sound right swapped? Choose, then listen."
- how `own`: "Four more on your own. Lock each one once."
Every `how` line is also shown as text beside its control. Instructions use no idioms.

## Family engine
None. Tool-only code: tape slots, pause table, word-group playback, waveforms, swap test.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Match | Try marks until the gaps line up | From level 4 nothing plays or shows until the marks are locked; two locks a level, then it prints as shown and a twin is added. |
| Asides | Put commas round every clause | Two grade 6 levels take no marks, and the picture question comes first. |
| Swap test | Comma every pair; play the swap first | 9 of 20 pairs are not coordinate; the prediction is given before the swap plays, and the sentence is judged whole. |
| Pause or break | Use one mark for all | Three marks, with three, two and three levels each. |
| Omission | Place the ellipsis anywhere | It must sit where the words were cut; one of four cuts changes the meaning and the student must say so. |
| On your own | Listen to the target | No target, no waveform, one lock each. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap Play target: `target`, `welcome` (queued, first time).
2. From level 4: `lock`. After a lock, Play mine: `mine`, then `match` when gaps line up.
3. Grade 7: `predict`, then `swap`. Grade 8: `meaning` after an omission.
4. `own`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| L.6.2a, L.7.2a, L.8.2a, L.8.2b wording | thecorestandards.org, Language Grades 6-8 | CCSS ELA 2010 PDF | yes |
| Coordinate adjectives take a comma and can be reordered or joined by "and"; cumulative adjectives can't | Purdue OWL, commas with coordinate adjectives | Merriam-Webster, coordinate adjectives | yes |
| Dashes set off and emphasize; parentheses set off and play down; an ellipsis marks an omission or a trailing pause | Purdue OWL, dashes, parentheses and ellipses | The Chicago Manual of Style Online, Q&A on dashes and ellipses | yes |
| The Gettysburg Address text (1863), public domain | Library of Congress, Gettysburg Address drafts | Cornell University Library, Gettysburg Address | yes |
Backed twice: 4. Cut: 0.

Design choices (not claims): the pause table's lengths and loudness changes.

Checks run (Python, scratchpad b18, 2026-11-09): the sample grade 7 pairs split into coordinate and cumulative by the swap rule as keyed; the pause table orders comma < dash < ellipsis; contrast as in Look.
Spec fix counts (2026-11-11), counted not run: grade 6 levels 4 + 3 + 3 + 2 = 12; grade 7 pairs 11 + 9 = 20; grade 8 levels 3 + 2 + 3 + 4 = 12.

## Done when
1. Focus and fold: at 1366x768 tape, tray and waveforms fit; at 680x425 waveforms stack.
2. Grade 6 asides play with commas, parentheses and dashes and their loudness; two levels take no marks. (L.6.2a)
3. Grade 7 takes a prediction for each pair before the swap plays, and judges each sentence whole. (L.7.2a)
4. Grade 8 has comma, ellipsis and dash levels for pauses and breaks, and four omission levels with the meaning check. (L.8.2a, L.8.2b)
5. From level 4 the target waveform is hidden and nothing plays until the marks are locked; a second miss prints as shown and adds a twin.
6. The final paragraph is locked once, then plays the student's marks and the target.
7. Four sentences on your own run with no target, waveform or swap button and one lock each; the end screen shows the result under the grade's codes.
8. The partner game shows a blank copy. Print shows the final paragraph and the results.
9. Every spoken instruction is also on screen; each key word shows with a marked example at first use.
10. Every action works by keyboard as well as tap; every pause and loudness has a text label, so each level can be done with Sound off; nothing is shown by color alone; motion can be paused.
11. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
12. Motion off: meters are still; no network requests.

## Open questions
- None for Cory.

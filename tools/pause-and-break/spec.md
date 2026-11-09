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

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| L.6.2a | Set off nonrestrictive and parenthetical elements with commas, parentheses or dashes; hear the aside get softer (parentheses) or louder (dashes) | the tape strip, the gaps on the waveform and a loudness band for the aside | 2 |
| L.7.2a | Put a comma between coordinate adjectives only (they could swap and take "and"): "a cold, dark night" but "a bright red kite" | the swap test and the comma | 3 |
| L.8.2a | Use a dash for a sudden break in thought | the break gap | 4 |
| L.8.2b | Use an ellipsis for a pause, and inside a quotation where words were cut; check the cut didn't change the meaning | the omission with the cut words shown faintly | 4 |
| L.6.2a to L.8.2b | The final paragraph: punctuate from scratch, then hear it | the paragraph and its playback | 5 |

## Screens and modes
Header (kit): title "Pause and Break"; `Levels`, `Final`, `Partner`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A sentence on a strip of masking tape across a recording desk, a play button and a "how it should sound" card with a waveform showing the target's gaps. The host is a reel-to-reel tape machine called Reel-E with blinking meters. First hint: "Tap Play target to hear how it should sound." The first tap plays the target; the welcome is queued after it (`welcomeAfter: true`).

**A level.** The sentence's words sit on the tape with drop slots between them. A mark tray: comma, pair of commas, pair of parentheses, pair of dashes, single dash, ellipsis. `Play mine` reads the sentence as punctuated. Pauses come from a fixed table (comma 250 ms, dash 400 ms, ellipsis 700 ms, parentheses 250 ms with the words inside 10 percent quieter, dashes 250 ms with the words inside 10 percent louder), built into the playback so the voice always honors the marks: each sentence is played as recorded word groups joined by the table's silences, not as free text-to-speech. Under the strip, two waveforms: target and mine; the gaps line up when the marks match.

**Grade 6.** Asides: "My cousin, who lives in Ohio, sent a postcard." versus "My cousin who lives in Ohio sent a postcard." (two cousins). A picture shows the meaning of each version. Three marks for asides; the tool asks "Should the aside sound like a whisper or a shout?" and the target uses one.

**Grade 7.** Adjective pairs: the swap test button flips the two adjectives and adds "and" between them; if both still sound right, they get a comma.

**Grade 8.** Breaks and pauses: "I was about to say yes, but then I saw the clock." becomes "I was about to say yes but then I saw the clock." Omissions: a quotation from a public-domain speech with a cut; the student places the ellipsis where words were removed, and a check shows the full quotation and asks whether the shortened one still means the same (one level's cut changes the meaning, and the student must say so).

**Same words, two meanings.** One level per grade where the same words with different marks say two things aloud ("The coach said the captain is late." against "The coach, said the captain, is late."), each with a picture of who is late.

**Final.** A short paragraph with no marks; the student punctuates it from scratch; the target plays after.

**Partner game.** One partner reads a marked sentence aloud from the screen; the other hears it and places the marks on a blank copy; then both play the target.

At 1366x768 the tape, tray and waveforms fit; at 680x425 the waveforms stack.

## Content
Written for Curio Class: 12 levels per grade, plus 3 same-words levels and a final paragraph per grade. Omission quotations from Abraham Lincoln's Gettysburg Address (1863, public domain), using the Bliss copy's text.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Marks snap to slots; pairs place both halves.
- With Motion off the meters don't move.
- Word groups for every level are recorded with the level's bank voice and stored locally.

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

## Family engine
None. Tool-only code: tape slots, pause table, word-group playback, waveforms, swap test.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Match | Try every slot | Each level has at most 9 slots and the tray has 6 marks, but levels also ask what the marks mean (the picture or the whisper or shout question). |
| Swap test | Comma every pair | Pairs that aren't coordinate fail the swap test aloud. |
| Omission | Place the ellipsis anywhere | It must sit where the words were cut; the meaning check asks for a yes or no with the full quote shown. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap Play target: `target`, `welcome` (queued, first time).
2. Play mine: `mine`, then `match` when gaps line up.
3. Grade 7: `swap` on the swap button. Grade 8: `meaning` after an omission.

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

## Done when
1. Focus and fold: at 1366x768 tape, tray and waveforms fit; at 680x425 waveforms stack.
2. Grade 6 asides play with commas, parentheses and dashes and their loudness. (L.6.2a)
3. Grade 7 swap test and commas work. (L.7.2a)
4. Grade 8 breaks, pauses and omissions with the meaning check work. (L.8.2a, L.8.2b)
5. The final paragraph plays the student's marks then the target.
6. The partner game shows a blank copy.
7. Print shows the final paragraph.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: meters are still; no network requests.

## Open questions
- None for Cory.

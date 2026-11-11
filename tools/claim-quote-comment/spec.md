# Claim, Quote, Comment

## One idea
The student builds an evidence paragraph one link at a time under a night sky: they write a claim about an article on LED streetlights, pick a quote from the article and set it in with a lead-in, then write the comment that explains how the quote proves the claim, and each finished link lights a streetlamp along a street; a lamp stays dark when a quote is dropped in with no lead-in, left unexplained, or repeats what another quote already shows, so they learn that evidence only counts when it is introduced and explained, not just pasted in.

## Not like
- argument-x-ray (6, spec, this batch): tagging someone else's argument. Here building your own paragraph.
- debate-prep-desk (6, spec, this batch): two sides and a coach's objections. Here one claim built link by link.
- quote-picker (5, spec): picking the best quote for a point. Here quote plus lead-in plus comment.
- theme-ledger (spec): tracking a theme across a novel. Here one informational article.
- essay-rope-team (4, spec): reasons and evidence for an opinion essay, grade 4. Here grades 6-8 citation and explanation.

## Who and how
- Grades 6-8, ELA, module "Citing and Explaining Evidence" (Reading Informational Text and Writing). Standards: RI.6.1, RI.7.1, RI.8.1, W.6.9, W.7.9, W.8.9.
- Driver: one student (tool.json `driver: "student"`). Role: lesson. Every sentence is read on tap; the paragraph is read back by the browser's speech voice.
- Three grade paths. Each has its own article of about 600 words, its own street of five lamps, and that grade's wording on the goal card. No path needs another.
  - Grade 6, "Lights On, Stars Out" (LED streetlights). RI.6.1: cite textual evidence to support analysis of what the text says explicitly as well as inferences drawn from the text. W.6.9: draw evidence from informational texts to support analysis, reflection and research.
  - Grade 7, "The First Bell" (school start times). RI.7.1: cite several pieces of textual evidence to support analysis of what the text says explicitly as well as inferences. W.7.9: as grade 6.
  - Grade 8, "The Last Penny" (whether to keep the one-cent coin). RI.8.1: cite the textual evidence that most strongly supports an analysis of what the text says explicitly as well as inferences. W.8.9: as grade 6.
- Change note (spec fix, 2026-11-11): the street, Mr. Okafor, the lamps and the three dark-lamp checks stay. Before, the grades shared one article with two, three and one items, nothing asked for an inference, and a lamp lit whether or not the quote supported anything. Now each grade has its own article and five lamps; two lamps in each path are inferences the article never states; a quote is checked against the point it is meant to prove and a lead-in against the real source; grade 7 needs two quotes a lamp; grade 8 ranks three quotes at every lamp. Mr. Okafor lights a model lamp first, the student checks each comment against a shown guide, and the last two lamps are on your own. The closing now has a reflection line and a research note. Added the three hooks.
- English learners: every spoken line is also on screen in short sentences. The words claim, quote, lead-in, comment, infer and strongest each show with Mr. Okafor's model lamp as the example the first time they are used. Lead-in and comment frames are offered and may be taken or left ("According to __,"; "This shows that __ because __."). Instructions use no idioms.
- tool.json `modes: ["Grade 6", "Grade 7", "Grade 8"]`, `minutes: "30-40"`, `grades_label: "Grades 6-8"`.
- Nothing is saved; `Print` prints the paragraph with its links labeled.

## Standards map
| Code | The standard's verb and its parts | Who does the verb | Student action that teaches it | Items that differ | What they see | Done when check |
|---|---|---|---|---|---|---|
| RI.6.1 | cite textual evidence to support analysis of what the text says explicitly and of inferences drawn from it | the student | For each of five points, find and highlight the quote that proves it; for the two inference points, first choose which statement the article lets a reader work out, then cite the lines it rests on | 5 lamps (3 explicit, 2 inference) | the point card, the quote with its paragraph number | 2, 3 |
| RI.7.1 | cite several pieces of textual evidence, explicit and inferred | the student | The same, with two quotes from different paragraphs for every point | 5 lamps, 10 quotes (3 explicit, 2 inference) | two quotes on each lamp | 2, 3 |
| RI.8.1 | cite the evidence that most strongly supports the analysis | the student | For every point, rank three true quotes, keep the strongest, and say what makes each of the other two weaker | 5 lamps, 15 quotes (3 explicit, 2 inference) | the ranked quotes with reasons | 2, 5 |
| W.6.9, W.7.9, W.8.9 | draw evidence from informational texts to support analysis, reflection and research | the student | Write a lead-in that names the real source and a comment that says what the quote proves; check the comment against the guide; close with a reflection line and a research note | 5 links, 1 reflection, 1 research note a path | lead-in, quote, comment, the guide | 4, 6 |

## Screens and modes
Header (kit): title "Claim, Quote, Comment"; `Article`, `Build`, `Paragraph`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word. The goal card gives the grade's two standards in their own words.

**On load and first tap.** A quiet street at dusk with a row of five unlit streetlamps, a few stars overhead and a lamplighter's ladder; Mr. Okafor, a city lighting engineer with a clipboard, stands by the first lamp. First hint: "Tap the article to hear its title." The first tap reads the title; the welcome is queued after it (`welcomeAfter: true`).

**Mr. Okafor's lamp (the model).** On a five-sentence town notice about a new crosswalk, Mr. Okafor lights one lamp aloud: reads the point, runs his finger to the sentence that proves it, says who said it, and says what it proves, naming each part as he sets it. Then he does one inference: "The notice never says the old crossing was unsafe. But look at these two sentences." It cannot be skipped the first time and `Mr. Okafor's lamp` reopens it, except on the last two lamps.

**Article.** Numbered paragraphs; tap to hear. The student can highlight a span to use as a quote (the evidence engine's Spans).

**Claim.** The path's question sits over the street (grade 6: "Should our town switch to warmer streetlights?"). The student writes a claim or picks a starter; the engine's `ev.claimCheck` asks that it can be argued.

**Build.** One link a lamp, five lamps. Each lamp has a point card that supports either side ("LEDs save cities money"; "Bright white light harms more than moths").
1. Point: three lamps carry a point the article states. Two carry an inference: the student sees four statements, none found word for word in the article, and chooses the one the article lets a reader work out. The other three are keyed as "goes past the text", "the text says the opposite" and "true, but not from this article".
2. Quote: the student highlights a span and drags it into the link, or picks it up and places it with taps or keys. Every sentence of the article is keyed to the points it supports. A quote that does not support the lamp's point leaves the lamp dark with the label "off the point"; the label does not say where to look. For an inference, the keyed spans are the two or three sentences it rests on.
3. Lead-in: write or pick. Each paragraph is keyed to its source or speaker; a lead-in that names no one is "dropped", and one that names the wrong source is "wrong voice".
4. Comment: one or two sentences, at least 8 words, using a word from the point and a word from the quote (word families), and not a repeat of the quote.
5. Check it against the guide: the guide shows three lines ("names what the quote shows", "ties it to the point", "adds something the quote does not say by itself"). The student taps the words in their own comment that do each job; a job with no words tapped sends them back to the comment.
When all parts are set and no check is dark, the lamp lights.

**Dark lamps.** The engine's `ev.checks` run on each link: off the point, dropped, wrong voice, unexplained ("What does it prove?"), repeats (two links with the same keyed point). Each dark lamp has a label and the fix. After a second miss on the same lamp Mr. Okafor shows a quote that works, and the lamp prints as "shown".

**Grade 7.** Every lamp needs two quotes from different paragraphs, each on the point, each with its own lead-in; one comment ties both to the point.

**Grade 8.** At every lamp three candidate quotes are offered, all true and all from the article. The student ranks them with `ev.pickStrong`, keeps the top one, and for each of the other two picks why it is weaker (keyed: about the topic but not this point; one person's opinion; a small case of a bigger fact; needs another fact to mean anything). The last lamp is a counter line ("Some people worry that ___; however, ___"), with its own three quotes.

**Paragraph.** The links join into a paragraph: claim, then each lead-in, quote and comment, then two closing lines the student writes: a reflection ("Reading this changed what I think about __ because __.") and a research note ("To be sure, I would still need to find out __."). Played back aloud with the lamps lighting in order.

**On your own.** Lamps 4 and 5 (one stated point and one inference) run with Mr. Okafor quiet: no starters, no frames unless the student opens them, no labels and no lit or dark lamp until both links are in. Each part is set once.

**The end.** A results strip for the teacher under the grade's two codes. Reading code: on the two lamps on your own, quotes on the point (grade 7 out of four; grade 8 strongest kept and reasons right), and whether the inference chosen was the keyed one. Writing code: lead-ins naming the real source and comments that passed, out of two, with the student's comments printed. Then the counts for lamps 1 to 3 and any lamp printed as "shown".

At 1366x768 the article and street fit side by side; at 680x425 the article is a tab.

## Content
Written for Curio Class from sourced facts, about 600 words each, with each paragraph's source named in it:
- Grade 6, "Lights On, Stars Out": cities switched to LED streetlights to save energy (LEDs use far less electricity than older lamps); the American Medical Association in 2016 recommended outdoor lights with color temperature 3000K or lower to cut glare and blue light; a 2021 study in England (Boyes and others, Science Advances) found LED streetlights cut the number of moth caterpillars by about half compared with dark areas; some cities now use warmer, dimmer or shielded LEDs.
- Grade 7, "The First Bell": in 2014 the American Academy of Pediatrics recommended that middle and high schools start at 8:30 a.m. or later; the Centers for Disease Control and Prevention reported that most U.S. middle and high schools started earlier than that; teenagers need about 8 to 10 hours of sleep; districts that moved the bell weigh bus routes, sports and family schedules.
- Grade 8, "The Last Penny": the United States Mint has reported for years that a one-cent coin costs more than one cent to make; Canada stopped giving out its penny in 2013 and rounds cash totals to the nearest five cents; the U.S. penny is mostly zinc with a copper coat; those who want to keep it point to charity coin drives and to worries about rounding up.
- The model notice (five sentences), written for Curio Class.
- Keys for each path: five points (three stated, two inferences with their three wrong statements and what each stands for); for every sentence, the points it supports; each paragraph's source; grade 8's three quotes a lamp with rank and the reason each lower one is weaker.
- What a wrong answer on your own means. A quote from the right paragraph that does not hold the point: the student matched the topic and did not read for proof. An inference chosen that "goes past the text": the student is answering from what they already believe. A lead-in with the wrong source: the quote was lifted without reading who is speaking. A comment that restates the quote: the student is not yet saying what the quote does for the point. Grade 7, two quotes from one paragraph or making one point twice: "several" is being read as "more words". Grade 8, the most striking quote kept over the one that proves the point: strong is being taken for vivid.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Links can be reordered; the paragraph rebuilds.
- With Motion off lamps switch on without fading.
- Access: every action works by tap and by keyboard. A span is highlighted by tapping its first and last word or with Shift and arrow keys; a quote is placed by drag, or by pick up and place with taps, or with Enter. Dark lamps carry a word label and an icon, never color alone; a lit lamp also says "lit". The read-back has its words on screen. Motion can be paused.
- On your own: each part is set once, with no feedback until both links are in.

## Look
- Accent `--brand` #3d3d8f night indigo (header, sky, lamp posts); gold #f4c542 (lamp light, highlighted quotes); paper #f4f4fb; ink #13132e; muted #55556b. Scene: a street at dusk.
- Contrast (WCAG 2.1, computed): white on brand 9.28:1; brand on paper 8.48:1; ink on paper 16.53:1; muted on paper 6.62:1; ink on gold 11.13:1.
- Never color alone: dark lamps carry labels; lit lamps say "lit".
- Different from this batch (lab teal, thermometer red, x-ray blue, desk brown).

## Art
- People art goes to Gemini: Mr. Okafor (a Nigerian American man in his forties in a city works vest), 3 poses; "illustrated friendly city worker <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): street at dusk with unlit lamps (1); a moth near a warm streetlight (1); a night sky over a small town (1).
About 6 images. Drawn in code: lamps, links, paragraph.

## Voice
Bank voice `knowing-guide` as Mr. Okafor (unique in this batch); the article is read by `science-narrator` (unique in this batch). `Curio.voice` with `scope: () => state.level + ':' + state.view + ':' + state.link`, `welcomeAfter: true`.
- how `welcome`: "Each lamp needs three things: your claim, a quote, and what the quote proves. Light the street."
- event, whole, `para`: the tapped paragraph.
- event `dropped`: "This quote just dropped in. Who said it?"
- event `unexplained`: "What does it prove?"
- event `repeats`: "You already showed this."
- event `lit`: "Lamp {two} is lit."
- event, whole, `paragraph`: the finished paragraph.
Read speaks the hint, which names the next action and control and never a disabled one.
- event `offPoint`: "That's from the article, but it doesn't prove this point."
- event `wrongVoice`: "Check who said that."
- how `infer`: "The article never says this outright. Which one can a reader work out?"
- how `guide`: "Tap the words in your comment that do each job."
- how `own`: "Two more lamps, on your own. Set each part once."
- event, whole, Mr. Okafor's lamp.
Every `how` line is also shown as text beside its control. Instructions use no idioms.

## Family engine
evidence (`__tool.ev`), described in full in tools/theme-ledger/spec.md. This tool uses: Source pack (one article), Spans, Claims with `ev.claimCheck`, Evidence links (span, claim, comment, leadIn), `ev.checks` (dropped, unexplained, repeats), and Draft with `ev.pickStrong` at grade 8. Not Sides, Series, Ledger view or Board view. The street of lamps is tool-only drawing over the links.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Quote | Drag in any sentence | Every sentence is keyed to the points it supports; an off-the-point quote leaves the lamp dark and a second miss prints as shown. |
| Inference | Pick at random; pick a sentence from the article | Four statements, none in the article word for word, three keyed as wrong for a reason; then the lines it rests on must be cited. |
| Lead-in | Take any starter | The source is keyed for each paragraph. |
| Comment | Paste the quote again; write filler | A repeat counts as unexplained; it needs a point word and a quote word; the student must tap the words that do each job on the guide; the teacher sees it printed. |
| Several (grade 7) | Use one paragraph twice | The two quotes must come from different paragraphs and both be on the point. |
| Strongest (grade 8) | Pick at random | Three true quotes at every lamp, rank keyed, and a reason for each weaker one. |
| On your own | Lean on the labels | No labels or lamps until both links are in, and each part is set once. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the article: title, `welcome` (queued, first time), then Mr. Okafor's lamp (whole), waits.
2. Paragraphs: `para` (whole).
3. Build: `infer` at an inference lamp; `offPoint`, `dropped`, `wrongVoice`, `unexplained`, `repeats` as they fire; `guide`; `lit` for each lamp.
4. Lamps 4 and 5: `own`.
5. Paragraph: `paragraph` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RI.6.1 to RI.8.1 and W.6.9 to W.8.9 wording | thecorestandards.org, Grades 6-8 | CCSS ELA 2010 PDF | yes |
| The AMA (2016) recommended outdoor lighting at 3000K or lower | American Medical Association, 2016 policy on LED community lighting | DarkSky International, AMA statement summary | yes |
| LED streetlights cut moth caterpillar numbers by about half in a 2021 English study | Boyes et al. (2021), Science Advances 7(35) | UK Centre for Ecology and Hydrology news release (2021) | yes |
| LED streetlights use much less energy than older streetlights | US Department of Energy, LED street lighting | US EPA or DOE Better Buildings outdoor lighting | yes |
| Introducing quotes with a signal phrase and explaining them makes evidence effective | Purdue OWL, quotations and signal phrases | Harvard College Writing Center, using evidence | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad b19, 2026-11-09): every keyed article point has at least one quote; a sample comment that repeats the quote is flagged as unexplained; contrast as in Look.
Spec fix notes (2026-11-11): the facts for "The First Bell" and "The Last Penny" were written from memory and not opened in this pass. Build must confirm each against the American Academy of Pediatrics statement (2014), the CDC report on school start times, the United States Mint's annual report and the Royal Canadian Mint's notice before the articles are written.

## Done when
1. Focus and fold: at 1366x768 article and street fit; at 680x425 the article is a tab.
2. Each grade path has its own article, five lamps and goal card. A lamp lights only when its quote is keyed to its point; quotes carry paragraph numbers. (RI.6.1, RI.7.1, RI.8.1)
3. Two lamps a path are inferences: the student chooses the statement the text supports from four, then cites the lines it rests on. Grade 7 lamps take two quotes from different paragraphs. (RI.6.1, RI.7.1)
4. A lead-in must name the paragraph's real source; a comment must pass the checks and the student's own check against the guide. Off the point, dropped, wrong voice, unexplained and repeats darken lamps with labels and fixes. (W.6.9, W.7.9, W.8.9)
5. Grade 8 ranks three quotes at every lamp, gives a reason for each weaker one, and ends with a counter line. (RI.8.1, W.8.9)
6. The paragraph builds with a reflection line and a research note and plays back with lamps lighting in order.
7. Mr. Okafor's lamp plays first and can be reopened; a second miss prints as shown.
8. Lamps 4 and 5 run with no labels or lamps until both are in; the end screen shows the result under the grade's two codes. Print shows the paragraph with links labeled and the results.
9. Every spoken instruction is also on screen; each key word shows with the model lamp at first use; the frames can be left.
10. Every action works by keyboard as well as tap, nothing is shown by color alone, and motion can be paused.
11. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
12. Motion off: lamps switch on without fading; no network requests.

## Open questions
- None for Cory.

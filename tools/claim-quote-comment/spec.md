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
- Driver: one student (tool.json `driver: "student"`). Every sentence is read on tap; the paragraph is read back by the browser's speech voice.
- Article: "Lights On, Stars Out" (about 600 words, written for Curio Class from sourced facts about LED streetlights). Levels: grade 6 (one claim, two links), grade 7 (three links, one from a second article section), grade 8 (the strongest-evidence pick and a counter line). tool.json `modes: ["Grade 6", "Grade 7", "Grade 8"]`, `minutes: "20-30"`, `grades_label: "Grades 6-8"`.
- Nothing is saved; `Print` prints the paragraph with its links labeled.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RI.6.1, RI.7.1 | Pick a quote from the article that supports the claim | the quote lifted from the article with its paragraph number | 2 |
| W.6.9, W.7.9 | Introduce the quote with a lead-in that names the source or speaker | the lead-in chip before the quote | 3 |
| RI.7.1, W.7.9 | Write a comment that explains how the quote proves the claim | the comment and the lamp lit | 3 |
| RI.6.1 to RI.8.1 | Fix dark lamps: dropped, unexplained, repeats | dark lamps with labels | 4 |
| RI.8.1, W.8.9 | Grade 8: rank three candidate quotes and keep the strongest; add a counter line | the ranked quotes and counter line | 5 |

## Screens and modes
Header (kit): title "Claim, Quote, Comment"; `Article`, `Build`, `Paragraph`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A quiet street at dusk with a row of unlit streetlamps, a few stars overhead and a lamplighter's ladder; Mr. Okafor, a city lighting engineer with a clipboard, stands by the first lamp. First hint: "Tap the article to hear its title." The first tap reads the title; the welcome is queued after it (`welcomeAfter: true`).

**Article.** Numbered paragraphs; tap to hear. The student can highlight a span to use as a quote (the evidence engine's Spans).

**Build.** One link per lamp:
1. Claim: the student writes it or picks a starter; the engine's `ev.claimCheck` asks that it can be argued ("LED streetlights are bright" is a fact, not a claim).
2. Quote: drag a highlighted span into the link.
3. Lead-in: pick or write ("According to the American Medical Association,", "One study found that"); stored as the link's `leadIn`.
4. Comment: the student writes one or two sentences; the comment must use a word from the claim and a word from the quote (word families) and be at least 8 words.
When all three are set, the lamp lights.

**Dark lamps.** The engine's `ev.checks` run on each link: dropped (no lead-in: "This quote just dropped in."), unexplained (no comment or a comment that only repeats the quote: "What does it prove?"), repeats (two links with the same keyed point: "You already showed this."). Each dark lamp has a label and the fix.

**Grade 8.** Three candidate quotes for one link; the student ranks them with `ev.pickStrong` against the claim and keeps the top one, then adds a counter line ("Some people worry that ___; however, ___").

**Paragraph.** The links join into a paragraph: claim, then each lead-in, quote and comment, then a closing line the student writes. Played back aloud with the lamps lighting in order.

At 1366x768 the article and street fit side by side; at 680x425 the article is a tab.

## Content
Written for Curio Class from sourced facts:
- "Lights On, Stars Out": cities switched to LED streetlights to save energy (LEDs use far less electricity than older lamps); the American Medical Association in 2016 recommended outdoor lights with color temperature 3000K or lower to cut glare and blue light; a 2021 study in England (Boyes and others, Science Advances) found LED streetlights cut the number of moth caterpillars by about half compared with dark areas; some cities now use warmer, dimmer or shielded LEDs.
- Keyed points for each paragraph so the repeats check knows when two quotes show the same thing.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Links can be reordered; the paragraph rebuilds.
- With Motion off lamps switch on without fading.

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

## Family engine
evidence (`__tool.ev`), described in full in tools/theme-ledger/spec.md. This tool uses: Source pack (one article), Spans, Claims with `ev.claimCheck`, Evidence links (span, claim, comment, leadIn), `ev.checks` (dropped, unexplained, repeats), and Draft with `ev.pickStrong` at grade 8. Not Sides, Series, Ledger view or Board view. The street of lamps is tool-only drawing over the links.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Comment | Paste the quote again | A comment that only repeats the quote counts as unexplained. |
| Comment | Write filler | It needs a claim word and a quote word and 8 words; the teacher sees it printed. |
| Quotes | Use one fact twice | The repeats check uses keyed points. |
| Grade 8 rank | Pick at random | `ev.pickStrong` compares to the key and asks for a reason when the pick isn't the strongest. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the article: title, `welcome` (queued, first time).
2. Paragraphs: `para` (whole).
3. Build: `dropped`, `unexplained`, `repeats` as they fire; `lit` per lamp.
4. Paragraph: `paragraph` (whole).

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

## Done when
1. Focus and fold: at 1366x768 article and street fit; at 680x425 the article is a tab.
2. Quotes come from highlighted spans with paragraph numbers. (RI.6.1, RI.7.1)
3. A lamp lights only with claim, lead-in, quote and comment. (W.6.9, W.7.9)
4. Dropped, unexplained and repeats checks darken lamps with labels and fixes. (RI.8.1)
5. Grade 8 ranks three quotes and adds a counter line. (RI.8.1, W.8.9)
6. The paragraph builds and plays back with lamps lighting in order.
7. Print shows the paragraph with links labeled.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: lamps switch on without fading; no network requests.

## Open questions
- None for Cory.

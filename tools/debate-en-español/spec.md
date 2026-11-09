# Debate en español

## One idea
The student joins a town forum in Spanish about a made-up proposal to add a weekday evening to a city's car-free Sunday street program, modeled on Bogotá's real Ciclovía: they read two short articles and hear three residents, choose a side, then write a paragraph that states a position, backs it with two reasons drawn from the sources, answers the rival's strongest point (Aunque es cierto que..., sin embargo...) and closes, while a self-scored checklist and a model paragraph show what each part looks like, so they learn to argue a position in connected paragraphs in Spanish.

## Not like
- consejero (9-12, spec, this batch): personal advice in a chat. Here a public position in a paragraph.
- mundo-hispano (6-12, spec): places and traditions to explore. Here a real program as the ground for an argument.
- opinion-builder (3-5, spec): an opinion letter in English for younger grades. Here a counterargument in Spanish.
- detective-del-pasado (6-12, spec): past narration. Here persuasion in the present with connectors.
- first-impressions-check (9-12, spec, this batch): checking quick judgments about people. Here weighing reasons on a public question.

## Who and how
- Grades 9 to 12, World Languages (Spanish), module "Opinions and Debate". Standards: ACTFL Advanced Low (narrates and describes in paragraphs; supports opinions); World-Readiness Standards Communities 5.1 (uses the language beyond the classroom).
- Driver: one student; class mode is "Foro en vivo", where the projector shows the moderator and two class teams build the opening and the rebuttal together (tool.json `driver: "student"`). Articles appear as text with a glossary on tap and play aloud in Spanish; the hint voice speaks English.
- One question, two articles, three residents and a rival speaker. Help levels: Lots (connector tiles and sentence starters per part), Some (connector bank only), Little (blank paragraph with the checklist). tool.json `modes: ["Foro", "Mi párrafo", "Foro en vivo"]`, `minutes: "30-45"`, `grades_label: "Grades 9-12"`.
- The student's forum comment is kept on this device only (localStorage), and the screen says so: "Your comment stays on this device. Nothing is uploaded." `Borrar mi comentario` clears it. There is no AI grading; the student scores their own paragraph with the checklist.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| ACTFL Advanced Low (interpretive) | Read the two articles and hear the residents, then sort their reasons by side | the reasons board | 2 |
| ACTFL Advanced Low (position and reasons in a paragraph) | Write a position with two reasons from the sources, with connectors (en primer lugar, además, por eso) | the paragraph builder and the source tags | 3 |
| ACTFL Advanced Low (answering another view) | Answer the rival's strongest point with a concession and a rebuttal (aunque, sin embargo, no obstante) | the rebuttal slot | 4 |
| ACTFL Advanced Low (self-assessment) | Score their paragraph with the checklist, then compare with the model paragraph | the checklist and the model side by side | 5 |
| World-Readiness Communities 5.1 | Post the comment to the town forum and read the forum's replies | the forum thread | 6 |

## Screens and modes
Header (kit): title "Debate en español"; `Foro`, `Mi párrafo`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word. Accent buttons (á é í ó ú ñ ¿ ¡) sit beside the paragraph box.

**On load and first tap.** A town forum page for "Villa Serena", a made-up city, with a photo strip of a car-free street on a Sunday morning and a banner: "¿Ciclovía también los miércoles por la noche?" The moderator, Lucía Ramos, sits at a table with a microphone. First hint: "Tap the question to hear it." The first tap reads the question; the welcome is queued after it (`welcomeAfter: true`). A line under the banner says: "Villa Serena and its proposal are made up. The Ciclovía in Bogotá is real."

**Foro.** Two short articles (about 250 words each, written for Curio Class): one on Bogotá's real Ciclovía (started in 1974, official in 1976, Sundays and holidays from 7 am to 2 pm, over 120 km of streets, about 2 million people); one on Villa Serena's proposal, with what it would cost and who would gain or lose (shop owners, bus riders, families, delivery drivers). Three residents speak in short clips: a bakery owner who worries about deliveries, a grandmother who walks with her grandkids on Sundays, and a bus driver. The student drags each reason to "A favor" or "En contra" on the reasons board; each reason keeps a tag showing where it came from.

**Mi párrafo.** Four slots in order: Postura, Razones (two, each with a source tag), Respuesta al otro lado, Conclusión. The rival speaker, Martín Ocampo, gives the strongest point for the other side in one line, and the student answers it. Connector tiles show by function (to add, to give cause, to concede, to contrast, to conclude). The paragraph is read back in the student's chosen voice when done.

**Checklist and model.** The student checks off their own paragraph: clear position; two reasons tied to a source; a concession and a rebuttal; at least four connectors from at least three functions; a closing sentence. Then a model paragraph for the other side appears beside theirs, with the same parts labeled, so the student compares parts, not words.

**Forum thread.** The comment posts to the town thread, and two made-up residents reply in Spanish: one agrees with a reason, one pushes back with a question.

**Foro en vivo.** On the projector, the class builds one opening and one rebuttal together.

At 1366x768 the article and the builder fit side by side; at 680x425 they are tabs.

## Content
- Two articles, three resident clips, the rival's line, the model paragraphs (one per side) and forum replies written for Curio Class. Facts about Bogotá's Ciclovía are backed twice; everything about Villa Serena is made up and labeled.
- Both sides get equally strong reasons and equally good model paragraphs; the tool never says which side is right.
- A teacher note says the topic is a local-policy question chosen to be low-stakes, and how to swap in a local issue.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Slots, reasons and tiles can be changed any time; the checklist is the student's own and has no score.
- With Motion off reasons drop onto the board without sliding and forum replies appear without typing dots.

## Look
- Accent `--brand` #7a1f3d council maroon (header, the forum banner, the slot frames); gold #f4c542 (connectors, source tags); paper #fbf0f3; ink #2a0a15; muted #6a5058. Scene: a town forum page and a council table.
- Contrast (WCAG 2.1, computed): white on brand 10.04:1; brand on paper 9.02:1; ink on paper 16.36:1; muted on paper 6.50:1; ink on gold 11.20:1.
- Never color alone: A favor and En contra carry words and icons; slots and connector functions are labeled.
- Different from this batch (chat teal, dawn indigo).

## Art
- People art goes to Gemini: Lucía Ramos (a Colombian woman in her forties, moderator), Martín Ocampo (a man in his fifties in a suit, the rival), the bakery owner (a Venezuelan man in his sixties in an apron), the grandmother (a Mexican woman in her seventies with a stroller), the bus driver (an Afro-Colombian woman in her thirties in a uniform), 3 poses each; "illustrated town forum speaker <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): a car-free street on a Sunday morning with bicycles and walkers, no faces (2); the council table (1).
About 18 images. Drawn in code: the forum page, reasons board, slots and checklist.

## Voice
Bank voice `clear-teacher` as the English hint voice (unique in this batch); Lucía and the articles are read by `news-reader`, Martín by `firm-captain`, the bakery owner by `friendly-dad`, and the grandmother and the bus driver by `gentle-storyteller` with two styles, all in Spanish (each unique in this batch). `Curio.voice` with `scope: () => state.view + ':' + state.slot`, `welcomeAfter: true`.
- how `welcome`: "Read, listen, and pick a side. Then write a paragraph that answers the other side."
- event, whole, `article`: the tapped article.
- event `resident`: a resident's clip.
- event `rival`: Martín's strongest point.
- event, whole, `paragraph`: the student's paragraph read back.
- event `reply`: a forum reply.
- event `privacy`: "Your comment stays on this device. Nothing is uploaded."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
spanish (`kit/spanish.js`, `__tool.es`), described in full in tools/calendario-vivo/spec.md. This tool uses: word records with audio and `es.say` for articles and clips, `es.card` for the glossary, and `es.tiles` for connectors. Not `es.check`: paragraphs are not graded. The reasons board, slots, checklist, model comparison and forum (localStorage wrapped in try and catch) are tool-only code.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Reasons | Drag reasons at random | Each reason has a keyed side; a misplaced one is shown back with the speaker's line. |
| Paragraph | Paste the model paragraph | The model shows only after the checklist, and it argues the other side. |
| Rebuttal | Skip it | The checklist and the forum reply both point to the empty slot. |
| Checklist | Tick everything | Self-scoring is the point; the model beside the paragraph makes a missing part plain. |
There is no grade to beat, by design.

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the question: the question, `welcome` (queued, first time).
2. Foro: `article` (whole) on tap; `resident` on tap.
3. Mi párrafo: `rival` when the rebuttal slot opens; `paragraph` (whole) when done.
4. Post: `privacy` on first save; `reply` for each forum reply (waits).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| ACTFL Advanced Low: narrates and describes in paragraphs and handles situations with a complication | ACTFL Proficiency Guidelines 2012, Speaking and Writing, Advanced Low | NCSSFL-ACTFL Can-Do Statements (2017), Advanced Low | yes |
| World-Readiness Standards: Communities 5.1, School and Global Communities | ACTFL, World-Readiness Standards for Learning Languages (2015) | ACTFL, World-Readiness Standards summary page | yes |
| Bogotá's Ciclovía began in December 1974 and became official in 1976 | Wikipedia, Ciclovía (checked 2026-11-09) | Instituto Distrital de Recreación y Deporte (IDRD), Ciclovía Bogotana | yes |
| It runs Sundays and holidays, 7 am to 2 pm, on over 120 km of streets, with about 2 million users | Wikipedia, Ciclovía (checked 2026-11-09) | IDRD, Ciclovía Bogotana | yes |
| "Aunque" with a fact takes the indicative; "sin embargo" and "no obstante" mark contrast | Real Academia Española, Nueva gramática, concessive clauses | Instituto Cervantes, Plan curricular, B2 discourse markers | yes |
Backed twice: 5. Cut: 0.

Sensitivity note: a local-politics topic chosen to be low-stakes, with both sides given equal strength and the made-up city labeled; a fresh agent reviews it for balance before build.

Checks run (Python, scratchpad b29, 2026-11-09): the saved Ciclovía page contains "1974", "1976", "7 am", "2 pm", "120 km" and "2 million"; each side has the same number of reasons and its model paragraph has all five checklist parts; the made-up label appears on every screen that names Villa Serena; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 article and builder fit; at 680x425 they are tabs.
2. Articles and residents play with text; reasons sort with source tags. (ACTFL Advanced Low)
3. The paragraph has a position and two sourced reasons with connectors. (ACTFL Advanced Low)
4. The rival's point opens a rebuttal slot with concession tiles. (ACTFL Advanced Low)
5. The checklist and the other side's model show side by side. (ACTFL Advanced Low)
6. The comment posts and two residents reply. (World-Readiness Communities 5.1)
7. Help levels, Foro en vivo and Print work; the privacy line shows; Borrar clears.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: no sliding or typing dots; no network requests.
10. Storage blocked: the tool still works and says the comment won't be kept.

## Open questions
- Spanish audio review: same as calendario-vivo (default used: a fresh agent checks the Spanish text, and Sara or Cory listens to a sample of 20 lines).
- Fresh balance review of the forum topic (default used: a fresh agent checks both sides for equal strength before build).

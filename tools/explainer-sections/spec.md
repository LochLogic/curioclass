# Explainer Sections

## One idea
The student takes apart a short explainer ("How Do Bridge Inspectors Find Cracks?") section by section, putting the shuffled blocks in order and tagging each one's job (hooks, defines, shows steps, compares, explains a cause, answers a worry) while a little reader walks down the page and stops with a question bubble wherever a section arrives too early or is missing; then they build their own explainer by choosing an organizing pattern and writing headings and transitions that fit it, until the reader reaches the end with no questions left, so they learn that structure is how an explainer carries a reader from not knowing to knowing.

## Not like
- explainer-studio (7, concept): the content inside sections (precise words, examples, style). Here the structure between sections.
- blueprint-builder (4, spec): grade 4 text structures from facts. Here grades 6-8 section jobs and a build.
- structure-spotter (3, spec): text features. Here how sections build a whole.
- essay-rope-team (5, spec): essay order and transitions. Here informative sections with jobs and a reader test.
- how-it-works-diagrams (spec): diagrams. Here sections of prose.

## Who and how
- Grades 6-8, ELA, module "Structure in Informative Writing" (Writing and Reading Informational Text). Standards: W.6.2, RI.6.5, RI.7.5, W.7.2, W.8.2.
- Driver: one student, or partners swapping explainers (tool.json `driver: "student"`). Role: lesson. Every block is read on tap; the student's sections are read back by the browser's speech voice.
- Three grade paths, each with its own model explainer to take apart, its own two fact packs to build from, and that grade's wording on the goal card. No path needs another.
  - Grade 6, model "How Inspectors Find Cracks in Bridges". RI.6.5: analyze how a particular sentence, paragraph or section fits into the overall structure of a text and contributes to the development of the ideas. W.6.2: write an informative text that introduces a topic; organizes ideas using definition, classification, comparison or cause and effect; uses headings and graphics; develops the topic with facts, definitions, details and quotations; uses transitions; and ends with a conclusion that follows.
  - Grade 7, model "How Lightning Forms". RI.7.5: analyze the structure an author uses to organize a text, including how the major sections contribute to the whole and to the development of the ideas. W.7.2: as grade 6, with an introduction that previews what is to follow.
  - Grade 8, model "How a Seed Vault Keeps Seeds Alive". W.8.2: as grade 7, organizing ideas into broader categories. Grade 8 takes its model apart as preparation; it carries no reading code.
- Change note (spec fix, 2026-11-11): the page, the blocks, Pip, the walk and the build stay. Before, the grades shared one model, the order could be found by moving blocks until Pip stopped asking, tags were one tap, the section map was not checked, and a built section passed with one line of anything. Now the order is locked before Pip walks; a job tag comes with what the reader would lose; grade 6 also places five single sentences; grade 7 names the overall structure and proves each section's part; each of the five built sections is checked for the facts it uses; and the build asks for a preview, a graphic, a quotation and (grade 8) categories. Pip shows a model section first, the student checks each section against a shown guide, and the last two items are on your own. Added the three hooks.
- English learners: every spoken line is also on screen in short sentences. The words section, heading, job, pattern, transition, preview, category and conclusion each show with the matching part of Pip's model section the first time they are used. Section frames are offered and may be taken or left ("First, __. This matters because __."). Instructions use no idioms.
- tool.json `modes: ["Grade 6", "Grade 7", "Grade 8"]`, `minutes: "30-45"` a sitting (take apart is one sitting, build is one or two), `grades_label: "Grades 6-8"`.
- Saving: the student's explainer is kept in this browser; footer: "Your explainer stays on this device." `Clear my explainer` removes it.

## Standards map
| Code | The standard's verb and its parts | Who does the verb | Student action that teaches it | Items that differ | What they see | Done when check |
|---|---|---|---|---|---|---|
| RI.6.5 | analyze how a sentence, paragraph or section fits the overall structure and contributes to the ideas | the student | Order seven sections and lock; tag each section's job together with what the reader would lose without it; then say where five loose sentences belong and what each does for its section | 7 sections and 5 sentences | the page, the tags, Pip's walk after the lock | 2 |
| RI.7.5 | analyze the structure an author uses, including how major sections contribute to the whole | the student | Name the overall structure from four and tap the two signals that show it; for five sections choose what the whole would lose and tap the later sentence that depends on it | 1 structure, 5 sections | the section map with dependence arrows | 3 |
| W.6.2 | write an informative text: introduce, organize, headings, graphic, facts, definitions, quotation, transitions, conclusion | the student | Build a five-section explainer from a fact pack; check each section against the guide | 5 sections | the student's page, the guide, Pip's walk | 4 |
| W.7.2 | the same, with an introduction that previews what follows | the student | The same, with a preview line that names the sections in order and a comparison chart | 5 sections | the preview matched to the headings | 5 |
| W.8.2 | the same, organizing ideas into broader categories | the student | Sort the pack's facts into three or four categories the student names, then build from the categories, with a common mix-up section | 5 sections | the category bins, then the page | 6 |

## Screens and modes
Header (kit): title "Explainer Sections"; `Take apart`, `Build`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word. The goal card gives the grade's standards in their own words.

**On load and first tap.** A tall page on a drafting table, cut into blocks scattered beside it, and Pip, a little reader made of paper with a magnifier, standing at the top of the page. First hint: "Tap a block to hear it." The first tap reads the block's first line; the welcome is queued after it (`welcomeAfter: true`).

**Pip goes first (the model).** On a four-block explainer about how a zipper works, Pip places two blocks aloud ("This one uses the word 'slider', and that one tells me what a slider is, so that one comes first"), tags one with what a reader would lose, and writes one section from three facts, naming each move against the guide. It cannot be skipped the first time and `Pip's example` reopens it, except on the items on your own.

**Take apart: order.** The grade's model in 7 blocks, each a section of 60 to 90 words. The student orders them and taps `Lock`. Only then does Pip walk. At a block that uses a word not yet defined, or a step with its cause missing, Pip stops with a question ("What's a weld?"). The student gets one more order and lock; after a second walk with a stop, Pip sets the order, says why at each move, and the order prints as "shown". Blocks cannot be moved while Pip walks.

**Take apart: jobs.** For each block the student picks its job from six chips and, with it, what the reader would lose without the block, from four lines written for that explainer. Job and loss are one answer; a miss says only "Not yet" and a second miss prints as shown.

**Grade 6: five sentences.** Five sentences lifted out of the model sit in a tray, with their gaps closed up. For each, the student places it back in its section and picks what it does there (gives an example, defines a word, links to the section before, gives the reason, sums up). Place and job are one answer.

**Grade 7: structure and section map.** The student names the model's overall structure from four (sequence, cause and effect, comparison, problem and solution) and taps two signals in the text that show it. Then, for five sections: what would the whole lose without this one (four choices), and which later sentence depends on it (tapped). An arrow is drawn from section to sentence once both are right. Then one line a section in the student's words: "This section __ so the reader can __."

**Build.** Two fact packs a grade, each 14 to 18 sourced facts, one quotation from a named person, and the data for one graphic. The student picks a pack and a pattern; the pattern suggests section jobs.
- Grade 8 first sorts the facts into three or four bins and names each bin; a bin name must cover its facts (keyed families) and no bin may hold fewer than three. The bins become the sections.
- Five sections: an introduction, three body sections and a conclusion. For each body section the student writes a heading that names its job ("Why lightning needs ice"), three or more sentences, and a transition from the tray or their own, and taps the facts from the pack that the section uses.
- A section passes when it uses at least two facts keyed to its job, says them in the student's own sentences (a copied fact is underlined "your words?"), defines any pack word marked as needing it before or where it is first used, and its transition fits the pattern.
- The introduction names the topic. In grades 7 and 8 it also previews: the sections it names must match the headings, in order.
- One section carries the pack's quotation with who said it. One carries a graphic: grade 6 places the pack's diagram and writes its caption; grades 7 and 8 fill a two-column comparison chart drawn in code from their rows.
- Grade 8 adds a "common mix-up" section that states the mix-up and corrects it with a fact.
- The conclusion must name the end point of the pattern and add no new fact.

**Check it against the guide.** After each section the guide shows four lines (heading names the job; two facts in my own words; new words explained; links to the section before). The student taps the words in their section that do each one. A line with nothing tapped sends them back.

**Pip walks the draft.** Pip stops at a section with no heading, at an undefined pack word, at a section that fails its fact check ("I didn't learn anything new here"), and at a preview that does not match. The bubble names the problem and not the fix.

**On your own.** Reading: a second short explainer for the grade in five blocks, ordered and tagged with one lock, no walk, and nothing marked until order and tags are both in (grade 6 also places two loose sentences; grade 7 names its structure). Writing: body section 3 and the conclusion are written with Pip's example closed, the frames shut unless the student opens them, and no walk until both are in.

**End.** A results strip for the teacher by code. Reading code: on the second explainer, blocks in place out of five, jobs right out of five, and the extra item right or not. Writing code: for the two sections on your own, which of the four guide lines each one met, with the sections printed. Then the counts from the guided parts and anything printed as "shown". The student writes one line on why their pattern fit the topic.

At 1366x768 the page and blocks fit side by side; at 680x425 the blocks are a tray under the page.

## Content
Written for Curio Class from sourced facts:
- Grade 6 model, bridge inspection, 7 blocks: a hook, a definition (what a crack is and why small ones matter), a cause (repeated loads, rust, freezing water), steps (look, touch, test), a comparison (eyes and hammers, dye that seeps in, magnets and iron powder, sound waves), a worry (does a crack mean the bridge will fall?), a conclusion. Facts: federal rules require most highway bridges to be inspected at least every 24 months; methods include visual and hammer checks, dye penetrant, magnetic particle and ultrasonic testing.
- Grade 7 model, lightning, 7 blocks, cause and effect: ice and water particles in a storm cloud collide and separate charge; lightning can and does strike the same place more than once (tall buildings are hit many times a year).
- Grade 8 model, seed vault, 7 blocks: the Svalbard Global Seed Vault in Norway stores seed copies from gene banks around the world at about minus 18 degrees Celsius.
- A second short explainer a grade (5 blocks) for the reading items on your own, and the zipper model (4 blocks).
- Two fact packs a grade, six in all, topics chosen at Build so that no pack repeats a model's topic; each fact keyed to the section jobs it can serve and each pack listing the words that need a definition. The student's own topic is allowed as an extra; it skips the fact check and does not count.
- Transition tray: 16 transitions labeled by pattern.
- What a wrong answer on your own means. Blocks in an order where a word is used before it is defined: the student is ordering by topic and not reading as someone who does not know yet. Job right but loss wrong: the label is known and what the section does for a reader is not. Grade 6, a sentence placed in the right section with the wrong job: the student sees what it is about and not what it does. Grade 7, structure named from the topic ("it is about storms, so problem and solution"): the student is not reading the signals. Writing, a section with facts copied whole: the pack is being moved, not explained. A preview that lists different sections: the introduction was written before the plan and never checked. Grade 8, a bin called "other facts": sorting is being done by what is left over and not by an idea.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Blocks and sections can be reordered any time; Walk can run any time.
- With Motion off Pip jumps from block to block.
- The fact-pack words that need a definition are listed in data; the student's own topic skips that check.
- Access: every action works by tap and by keyboard. A block, a sentence or a fact is moved by drag, or picked up and placed with taps, or with arrow keys and Enter. Pip's stops are a bubble with words and the stopped block is outlined and named, never color alone. Read-back has its words on screen. Motion can be paused.
- On your own: one lock for the order and tags; the two sections get no walk until both are in.

## Look
- Accent `--brand` #2d5a8c blueprint blue (header, block edges, the drafting grid); gold #f4c542 (Pip's magnifier, tags); paper #f3f6fb; ink #0e1b2b; muted #4f5868. Scene: a drafting table under a window.
- Contrast (WCAG 2.1, computed): white on brand 7.11:1; brand on paper 6.57:1; ink on paper 16.02:1; muted on paper 6.62:1; ink on gold 10.67:1.
- Never color alone: tags are words; bubbles carry text.
- Different from this batch (editor's red, web green, lilac, lamp amber).

## Art
Local FLUX (`scripts/localart.py`), no people in focus.
- drafting table (1); Pip (4 poses: walk, stop with a question, read, cheer), "A small friendly paper character holding a magnifying glass <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- topic pictures (4): "<a steel bridge underside with rivets / a seed vault entrance in snowy mountains / lightning over a field / an inspector's tablet showing sound waves, no people>, realistic illustration, no text"; 4:3.
About 9 images. Drawn in code: page, blocks, bubbles, chart.

## Voice
Bank voice `science-narrator` as Pip (unique in this batch). `Curio.voice` with `scope: () => state.grade + ':' + state.view + ':' + state.block`, `welcomeAfter: true`.
- how `welcome`: "An explainer carries a reader from not knowing to knowing. Put the sections in order, then I'll walk down the page."
- event, whole, `block`: the tapped block.
- event `stuck`: Pip's question bubble ("What's a {weld}?").
- event `clear`: "Made it to the end. No questions!"
- how `tagHow`: "What job does this section do? Pick a tag."
- how `buildHow`: "Pick a topic and a pattern. Then write a heading that names each section's job."
- event `whyLine`: "Why did your pattern fit? Write one line."
Read speaks the hint, which names the next action and control and never a disabled one.
- how `lockHow`: "Put the blocks in order. Then tap Lock and I'll walk."
- how `loseHow`: "Choose the job. Then choose what a reader would lose without it."
- how `factsHow`: "Tap the facts from the pack that this section uses."
- how `guide`: "Tap the words in your section that do each line of the guide."
- how `own`: "This part is on your own. One lock, then I'll look."
- event, whole, Pip's example.
Every `how` line is also shown as text beside its control. Instructions use no idioms.

## Family engine
None. Tool-only code: blocks with jobs and dependencies, the reader walk, section editor with pattern suggestions, comparison chart.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Order | Move blocks until Pip stops asking | Pip walks only after a lock; two locks, then the order prints as shown. |
| Jobs | Tag everything "explains" | Job and what the reader would lose are one answer, and a miss does not say which was off. |
| Sentences (grade 6) | Drop each anywhere | Place and job are one answer for five sentences with five different jobs. |
| Structure (grade 7) | Pick from four | Two signals must be tapped, and each section needs the later sentence that depends on it. |
| Build | Write one big section, or one line a section | Five sections, three sentences each, two facts keyed to the section's job in the student's own words, and the student taps the guide lines in their own text. |
| Preview | Write any opening | The sections it names must match the headings in order. |
| Categories (grade 8) | One big bin | Three or four bins, three facts or more each, names keyed to their facts. |
| On your own | Lean on the walk | No walk until everything is in. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a block: its first line, `welcome` (queued, first time), then Pip's example (whole), waits.
2. Blocks: `block` (whole); `lockHow`. After a lock, Walk: `stuck` at each stop, or `clear`.
3. Jobs: `loseHow` (first time).
4. Build: `buildHow`; `factsHow`; `guide` after each section; the walk as in 2.
5. Items on your own: `own`. At the end, `whyLine`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| W.6.2, RI.6.5, RI.7.5, W.7.2, W.8.2 wording | thecorestandards.org, Grades 6-8 | CCSS ELA 2010 PDF | yes |
| Most US highway bridges must be inspected at least every 24 months | Federal Highway Administration, National Bridge Inspection Standards | eCFR, 23 CFR 650 Subpart C | yes |
| Dye penetrant, magnetic particle and ultrasonic testing find surface and hidden cracks in steel | Federal Highway Administration, bridge inspector's reference manual | American Society for Nondestructive Testing, introduction to methods | yes |
| The Svalbard Global Seed Vault stores duplicate seed samples at about minus 18 degrees Celsius | Crop Trust, Svalbard Global Seed Vault | Norwegian Ministry of Agriculture and Food, Svalbard Global Seed Vault | yes |
| Lightning forms as colliding ice and water particles separate charge in a storm cloud; lightning often strikes the same place more than once | NOAA National Severe Storms Laboratory, lightning basics | National Weather Service, lightning myths | yes |
Backed twice: 5. Cut: 1 (a count of how many US bridges are rated in poor condition; the figure changes each year, so the model leaves it out).

Checks run (Python, scratchpad b17, 2026-11-09): in the sample model, the shuffled start triggers at least one stuck bubble and the key order clears the walk; the comparison block depends on the definition block; contrast as in Look.
Spec fix notes (2026-11-11): the six fact packs and the three second explainers are not written yet. Build must source each pack's facts and its quotation from a named, checkable source.

## Done when
1. Focus and fold: at 1366x768 the page and blocks fit; at 680x425 the blocks are a tray.
2. Each grade has its own model. Blocks are ordered and locked before Pip walks; a job tag is judged with what the reader would lose; grade 6 places five sentences with their jobs. (RI.6.5)
3. Grade 7 names the structure with two signals and, for five sections, the loss and the sentence that depends on it, then writes the section map. (RI.7.5)
4. The build has five sections; each body section needs a heading that names its job, two keyed facts in the student's words, defined words and a fitting transition, plus one quotation and one graphic in the piece, and a conclusion with no new fact. (W.6.2)
5. Grades 7 and 8: the preview matches the headings in order, and the chart is filled. (W.7.2)
6. Grade 8: facts are sorted into named categories before writing, and a mix-up section corrects itself with a fact. (W.8.2)
7. The student checks every section against the guide by tapping their own words. Pip's example plays first; a second miss prints as shown.
8. The second explainer and the last two sections run on your own; the end screen shows the result by code.
9. The explainer survives a reload where storage works; `Clear my explainer` removes it. Print shows the explainer, the section map and the results.
10. Every spoken instruction is also on screen; each key word shows with Pip's model at first use; the frames can be left.
11. Every action works by keyboard as well as tap, nothing is shown by color alone, and motion can be paused.
12. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
13. Motion off: Pip jumps; no network requests.

## Open questions
- For Cory: each grade now has its own model and two fact packs of its own (six packs, none written yet). Default used: topics chosen at Build. Say if you want to name the topics.

# Word Problem Decoder

## One idea
The student decodes grade 6 to 8 word problems with a highlighter, marking the math language (per, each, times as many, less than, percent of), then draws what the sentence means as a bar model or ratio table before writing the expression, and catches "keyword traps" where the same word needs different operations ("each box holds 12" multiplies, "share 36 so each gets" divides; "5 less than x" is x minus 5), so they learn that the structure of the sentence, not a keyword, decides the math.

## Not like
- math-explainer (3-5, spec): explaining your own steps to a classmate. Here reading the problem's language before solving.
- idiom-island (built): literal versus real meaning of idioms. Here literal order versus math order.
- cer-builder (6-8, spec later): science claims with evidence. Here math phrases with diagrams.
- detective-del-pasado (6-12, spec, this batch): verb tense as evidence. Here math phrases as evidence.
- perspective-frames (6-8, spec, this batch): sorting quotes by speaker. Here sorting phrases by operation.

## Who and how
- Grades 6 to 8, English Language Development, module "Word Problems Decoded". Standards: WIDA ELD-MA (Standard 3, the language of mathematics), Explain key language use (WIDA 2020).
- Driver: one student; class mode is "Trap or not?", where the projector shows a problem pair and the class votes whether the keyword means the same operation in both (tool.json `driver: "student"`). Every problem and phrase is read on tap.
- Thirty problems in five sets: Each and per; More than and less than; Times as many; Percent of; No keywords at all. Help setting: Lots (phrase hints and a started diagram), Some (diagram tools only), Little (highlighter only, then typing the expression). Teacher notes map them to WIDA 1-2, 3-4 and 5-6. tool.json `modes: ["Decode", "Trap collection", "Make a trap", "Trap or not?"]`, `minutes: "20-30"`, `grades_label: "Grades 6-8"`.
- The trap collection is kept for this session only; `Print` prints it and any trap problems the student wrote.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| WIDA ELD-MA (rate, ratio, percent and comparison phrases) | Highlight the math phrases and tag each with what it does | the highlighted problem with tags | 2 |
| WIDA ELD-MA (phrases to models) | Build a bar model or ratio table that matches the sentence | the diagram beside the problem | 3 |
| WIDA Explain (how the words lead to the operation) | Explain with "The problem says ___, so I ___ because ___." | the frame read back | 4 |
| WIDA ELD-MA (reversal phrases) | Write "5 less than x" as x minus 5 and see the before-and-after diagram | the reversal diagram | 3 |
| WIDA Explain (meaning over keywords) | Solve the no-keyword problems from the meaning | the final set | 5 |

## Screens and modes
Header (kit): title "Word Problem Decoder"; `Decode`, `Trap collection`, `Make a trap`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A notebook page with a problem card taped on and a fat highlighter lying across it; a sticky note: "Find the words that tell you the math. Careful: some of them try to trick you." The coach, Coach Dana Price, leans on the page edge. First hint: "Tap the problem to hear it." The first tap reads it; the welcome is queued after it (`welcomeAfter: true`).

**Decode.** Three steps per problem.
1. Highlight: the student drags the highlighter over the phrases that carry the math. Each highlight gets a tag (rate, groups of, compare, part of, change).
2. Draw: bar model (bars that can be split, joined and labeled) or ratio table (columns that scale). The diagram must match the sentence: for "Lia has 3 times as many stickers as Ben", Lia's bar is three of Ben's.
3. Write: the expression or equation from tiles (or typed at Little help), then the explain frame.
Wrong operations are shown, not buzzed: the diagram redraws from the student's expression next to the one the sentence describes, so the mismatch is visible.

**Traps.** Problems come in pairs that share a keyword but not an operation: "Each box holds 12 pencils. How many in 5 boxes?" and "Share 36 pencils so each student gets 4. How many students?"; "Mia is 5 years older than Sam. Sam is 12. How old is Mia?" (add) and "Mia is 5 years older than Sam. Mia is 17. How old is Sam?" (subtract); "x is 5 less than y" (x = y minus 5). A caught trap goes into the trap collection with both problems and both diagrams.

**No keywords.** The last set has no familiar keywords ("A recipe uses 2 cups of rice for 3 people. Cooking for 12, how much rice?"); the student decodes from meaning.

**Make a trap.** The student writes a trap pair for a classmate from a template, and it prints.

**Trap or not?** On the projector, the class votes on each pair.

At 1366x768 problem and diagram fit side by side; at 680x425 the diagram is below.

## Content
- Thirty problems in fifteen pairs written for Curio Class, each with keyed highlights, tags, diagram, expression and answer. Settings vary (a food truck, a bike repair shop, a garden, a school store).
- Grade 6: rates, ratios, "less than" in expressions. Grade 7: percent of, percent change. Grade 8 stretch: comparing two rates.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Highlights, diagrams and expressions can be changed any time; the mismatch view updates at once.
- With Motion off the highlighter stroke appears whole and diagrams don't grow.

## Look
- Accent `--brand` #5a5410 highlighter olive (header, notebook spine, tags); gold #f4c542 (the highlight itself); paper #fffbea; ink #22200a; muted #5a5747. Scene: a notebook page with a highlighter.
- Contrast (WCAG 2.1, computed): white on brand 7.75:1; brand on paper 7.47:1; ink on paper 15.82:1; muted on paper 7.01:1; ink on gold 10.10:1.
- Never color alone: highlights also get an underline and a tag word; mismatches show a "doesn't match" label.
- Different from this batch (detective teal, earth red, book-group purple, town slate).

## Art
- People art goes to Gemini: Coach Dana Price (a Black woman in her thirties in a track jacket with a whistle), 4 poses; "illustrated middle school math coach <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): the notebook and highlighter (1); problem setting thumbnails, no faces (8).
About 13 images. Drawn in code: highlights, bar models, ratio tables, tiles.

## Voice
Bank voice `clear-teacher` as the hint voice and the problem reader (unique in this batch); Coach Price is read by `easy-coach` (unique in this batch). `Curio.voice` with `scope: () => state.problem + ':' + state.step`, `welcomeAfter: true`.
- how `welcome`: "Highlight the words that tell you the math. Then draw what they mean before you write anything."
- event `problem`: the problem text.
- event `tag`: the tag for a highlight.
- event `mismatch`: "Your expression draws this. The sentence says this."
- event `trap`: "Trap caught! Same word, different math."
- event, whole, `explain`: the explain frame.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: the highlighter with tags, bar model and ratio table builders, the expression-to-diagram redraw, trap pairs and collection, trap maker.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Keywords | "Each means multiply" every time | Half the each problems divide; the diagram mismatch shows. |
| Reversals | Write "5 less than x" as 5 minus x | The reversal diagram shows the bar going the wrong way; the answer key fails. |
| Diagram | Skip the diagram | Write unlocks only after a diagram that matches the sentence. |
| Explain | Fill the frame with the keyword alone | The frame's "because" slot needs the diagram's relationship (times as many, part of, per one). |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the problem: `problem`, `welcome` (queued, first time).
2. Highlight: `tag` per highlight. Draw and write: `mismatch` as it fires.
3. Trap pair done: `trap`. Explain: `explain` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| WIDA 2020: Standard 3 is the language of mathematics; Explain covers how and why | WIDA ELD Standards Framework, 2020 Edition | WIDA, Key Language Uses: A Closer Look (2020) | yes |
| Grade 6 to 7 content: ratios and rates with tables and tape diagrams; expressions from words such as "subtract y from 5"; percent of a quantity | CCSS Math 6.RP.A.3, 6.EE.A.2a, 7.RP.A.3 (thecorestandards.org) | CCSS Math 2010 PDF | yes |
| Keyword strategies mislead students; reading the problem's structure works better | Karp, Bush and Dougherty, "13 Rules That Expire" (Teaching Children Mathematics, 2014), rule on keywords | Clement and Bernhard, "A Problem-Solving Alternative to Using Key Words" (Mathematics Teaching in the Middle School, 2005) | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad b27, 2026-11-09): every problem's keyed expression gives its keyed answer; in each trap pair the shared keyword maps to different operations; "x is 5 less than y" evaluates as y minus 5 for test values; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 problem and diagram fit; at 680x425 diagram below.
2. Highlights take tags. (WIDA ELD-MA)
3. Diagrams must match the sentence; mismatches redraw beside it. (WIDA ELD-MA)
4. The explain frame needs the relationship. (WIDA Explain)
5. Trap pairs fill the collection; the no-keyword set is solved from meaning. (WIDA Explain)
6. Help levels behave as in Who and how.
7. Make a trap, Trap or not? and Print work.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: highlights appear whole; no network requests.

## Open questions
- Home-language support: home-language glossaries for ELD frames (Cory's open question in RUNBOOK.md)? (default used: English only, with pictures and read-aloud)

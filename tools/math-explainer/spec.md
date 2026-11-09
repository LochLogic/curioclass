# Math Explainer

## One idea
The student solves a word problem with base-ten blocks and a number line on a work mat, then explains it to Nico, a classmate who was absent, one sentence per step (First I..., Next I..., So the answer is...), and Nico replays each sentence on his own mat exactly as it is said, so a skipped step, a step out of order or a vague "I did it" shows up as a gap in his replay, and the student learns to explain a math strategy in order with sequence words, math verbs and so.

## Not like
- then-what-happened (6-12, spec): a listener redraws a story from your words. Here the replay is a math strategy, checked for complete steps, on a green chalk-and-blocks mat.
- word-problem-decoder (6-8, spec later): reading the language of a problem. Here explaining your own solution.
- cause-and-effect-rewind (3-5, spec): science chains with because and so. Here math steps with first, next and so.
- mi-día (K-12, spec, this batch): ordering a day in Spanish. Here ordering a solution in English.
- opinion-builder (3-5, spec, this batch): reasons for an opinion. Here reasons for each math step.

## Who and how
- Grades 3 to 5, English Language Development, module "Explaining My Solution". Standards: WIDA ELD-MA (Standard 3, the language of mathematics), Explain key language use (WIDA 2020).
- Driver: one student; class mode is "Two ways", where the projector shows two students' strategies for the same problem side by side (tool.json `driver: "student"`). Every problem, tile and sentence is read on tap.
- Twelve problems in three sets (Add and subtract to 1,000; Equal groups; Fractions on a number line). Help setting: Lots (sentence frames with picture tiles), Some (frames with word tiles), Little (starters only, then typing). Teacher notes map them to WIDA 1-2, 3-4 and 5-6. tool.json `modes: ["Solve and explain", "Two ways"]`, `minutes: "15-25"`, `grades_label: "Grades 3-5"`.
- Optional: record the explanation in your own voice; the screen says "Your recording stays on this device. Nothing is uploaded." No speech recognition. Nothing else is saved; `Print` prints the problem, the mat steps and the explanation.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| WIDA Explain (sequence words) | Build one sentence per step with first, next, then, finally | Nico's replay, step by step | 3 |
| WIDA ELD-MA (math verbs and quantities) | Use the keyed verb and numbers for each step (I grouped 3 tens, I counted on 8) | the tile bank and the replayed step | 3 |
| WIDA Explain (complete, in order) | Fix gaps when Nico's replay jumps or stalls | the gap marker on Nico's mat | 4 |
| WIDA Explain (result with so) | End with "So the answer is ___ because ___." | the final caption | 5 |

## Screens and modes
Header (kit): title "Math Explainer"; `Solve`, `Explain`, `Watch Nico`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A green chalkboard wall above two work mats, the student's and Nico's, with a sticky note: "Nico missed class today. Can you show him how?" The first problem card waits on top: "Maya has 3 bags. Each bag has 8 apples. How many apples does she have?" First hint: "Tap the problem to hear it." The first tap reads it; the welcome is queued after it (`welcomeAfter: true`).

**Solve.** The student solves on their mat with base-ten blocks (ones, tens, hundreds), equal-group circles and a number line. Each move is logged as a step in a side list (Made 3 groups of 8; Counted by 8s; Wrote 24). Any correct strategy is fine; the log keeps the student's own steps.

**Explain.** One sentence slot per logged step. The student builds each from tiles: sequence words (first, next, then, after that, finally), math verbs (I made, I put, I added, I took away, I grouped, I counted on, I traded, I jumped), the numbers and units from the problem, and so or because. Each finished sentence plays its step on Nico's mat at once.

**Watch Nico.** Nico runs the whole explanation from the start. A missing step makes his mat jump and a dashed gap marker appears: "Wait, how did you get from here to here?" A step out of order plays out of order, and his blocks don't add up. A vague sentence ("I did it", "I just knew") replays nothing; Nico shrugs and asks "What did you do first?" When every step replays, Nico tries a new problem of the same kind by following the student's explanation, and gets it.

**Two ways.** On the projector, two built-in strategies for one problem (repeated addition and a number line) play side by side with their explanations, for the class to compare.

At 1366x768 both mats and the tiles fit; at 680x425 Nico's mat is a tab.

## Content
- Twelve word problems written for Curio Class, three or four keyed strategies each, with a keyed verb and numbers per kind of step. Names and settings vary (a bakery, a garden, a bus, a library).
- Steps are compared by what they do to the mat, so a correct strategy the keys didn't list still replays.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Sentences can be rebuilt any time; Watch Nico replays from the start.
- With Motion off Nico's mat shows each step as a still with a step number, and a gap shows as an empty numbered box.

## Look
- Accent `--brand` #33691e chalkboard green (header, mats, tiles); gold #f4c542 (the step playing, the gap marker); paper #f2f8ef; ink #10220a; muted #4f5e48. Scene: a classroom chalkboard with two work mats.
- Contrast (WCAG 2.1, computed): white on brand 6.60:1; brand on paper 6.12:1; ink on paper 15.49:1; muted on paper 6.42:1; ink on gold 10.29:1.
- Never color alone: steps are numbered; gaps show a dashed box with words.
- Different from this batch (party magenta, clock blue, library brown, museum violet).

## Art
- People art goes to Gemini: Nico (a Filipino American boy about nine with glasses), 5 poses (listening, puzzled, shrugging, building, cheering); "illustrated third grade boy <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): the chalkboard wall with two mats (1); problem scene thumbnails, no faces (12).
About 18 images. Drawn in code: blocks, groups, number line, tiles, gap markers.

## Voice
Bank voice `clear-teacher` as the hint voice and the reader of problems and the student's sentences (unique in this batch); Nico is read by `playful-friend` (unique in this batch). `Curio.voice` with `scope: () => state.problem + ':' + state.step`, `welcomeAfter: true`.
- how `welcome`: "Solve it on your mat, then explain it to Nico one step at a time. He'll do exactly what you say."
- event `problem`: the problem text.
- event, whole, `sentence`: the built sentence.
- event `gap`: "Wait, how did you get from here to here?"
- event `vague`: "What did you do first?"
- event `solved`: "I get it! Let me try one."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: the mat and its step log, the sentence tiles keyed by step kind, Nico's replay with gap detection, the strategy comparison, recording with the on-device line.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Steps | Write only "So the answer is 24." | Nico's mat jumps from empty to 24 and the gap marker asks how. |
| Order | Put sentences in any order | The replay runs in the order written; out of order, the blocks don't add up. |
| Vague | "I did it" for every step | Vague sentences replay nothing. |
| Numbers | Use the right verb with wrong numbers | Each sentence replays with its own numbers, so a wrong number shows on the mat. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the problem: `problem`, `welcome` (queued, first time).
2. Explain: `sentence` (whole) as each is built.
3. Watch Nico: `gap` or `vague` as they fire; `solved` at the end.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| WIDA 2020: Standard 3 is the language of mathematics; Explain covers describing steps and strategies in order | WIDA ELD Standards Framework, 2020 Edition | WIDA, Key Language Uses: A Closer Look (2020) | yes |
| Grade 3 work includes equal groups, adding and subtracting within 1,000 and fractions on a number line | CCSS Math 3.OA.A.1, 3.NBT.A.2, 3.NF.A.2 (thecorestandards.org) | CCSS Math 2010 PDF | yes |
| Explaining a strategy and listening to others' is a core math practice | CCSS Mathematical Practice 3 | NCTM, Principles to Actions (2014), meaningful mathematical discourse | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad b26, 2026-11-09): every keyed strategy for all twelve problems ends at the keyed answer; dropping any one step from a keyed explanation makes the replay show a gap; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 both mats and tiles fit; at 680x425 Nico's mat is a tab.
2. Solving logs each step on the mat.
3. Sentences built from tiles replay on Nico's mat at once. (WIDA Explain, ELD-MA)
4. Missing, out-of-order and vague steps show as gaps or stalls. (WIDA Explain)
5. "So the answer is" closes the explanation, and Nico solves a new problem. (WIDA Explain)
6. Help levels behave as in Who and how.
7. Two ways and Print work; recording shows the privacy line.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: stills with step numbers replace the replay; no network requests.

## Open questions
- Home-language support: this follows Cory's open question on home-language glossaries for the ELD tools (default used: English only, with pictures and read-aloud).

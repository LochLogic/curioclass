# Lost and Found

## One idea
A first grader named Sam (made up, labeled "illustration") has lost a stuffed fox, and the school lost-and-found closet has five numbered boxes with stickers (13, 15, 22, 26, 38), so the child reads the closet log one clue at a time, where each clue is a one- or two-step story within 100 ("Box C had 14 mittens. 6 were picked up, then 5 more came in. How many now?"), drags snap-bars into a bar model, writes an equation with a box for the unknown, and the answer matches a sticker that rules that box out ("The fox isn't in the box with 13"); clues vary the unknown (start: some hats were in Box A, 8 came in, then 3 were picked up, now there are 20; compare: Box D has 9 more scarves than Box B's 17; two steps: 45 lunch boxes, 18 picked up Monday, 5 more picked up Tuesday); a wrong answer points to a wrong box, so the check is built in; after four clues one box is left, and the child opens it and Sam hugs the fox, so a second grader learns to use addition and subtraction within 100 to solve one- and two-step word problems of adding to, taking from, putting together, taking apart and comparing, with unknowns in all positions, using drawings and equations with a symbol for the unknown.

## Not like
- story-replay (1, spec): one step within 20. Here two steps within 100.
- pattern-painter (3, concept): two steps with all four operations. Here adding and subtracting.
- fact-rally (2, spec): fluency, no stories. Here stories that need a model.
- jump-line (2, spec): strategies on a line. Here bar models for stories.

## Who and how
- Grade 2, Math, module "Two-Step Word Problems". Standards: 2.OA.1 (use addition and subtraction within 100 to solve one- and two-step word problems involving situations of adding to, taking from, putting together, taking apart, and comparing, with unknowns in all positions, e.g., by using drawings and equations with a symbol for the unknown number to represent the problem).
- Format: mystery. Driver: one student (tool.json `driver: "student"`). Every card is spoken. Controls 56 px or more.
- Three cases of four clues each, five boxes per case, snap-bars, an equation builder, the reveal. Extra: Case maker (the teacher writes clues and stickers). tool.json `modes: ["Closet", "Case maker"]`, `minutes: "15-25"`, `grades_label: "Grade 2"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 2.OA.1 (one step, all positions) | Model start, change and result unknowns | the bar model; the equation with a box | 2 |
| 2.OA.1 (compare) | Model "9 more than" | two bars and the difference | 3 |
| 2.OA.1 (two steps) | Model two-step clues and rule out boxes | the box ruled out; the last box | 4 |

## Screens and modes
Header (kit): title "Lost and Found"; `Closet`, `Case maker`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more.

**On load and first tap.** A cluttered closet with five numbered boxes and stickers, a log book on a stool, and Sam looking worried. The welcome is queued (`welcomeAfter: true`): "Sam lost a stuffed fox! Each clue in the log points to a box where the fox is NOT. Tap the log to read the first clue." First hint: "Tap the log."

**A clue (focus: the bar model).** At 1366x768 the clue card is at the top, the bar model in the middle and the boxes along the bottom; at 680x425 the boxes shrink to sticker chips. The child drags bars (whole and parts) and they snap to numbers from the clue; a box marks the unknown. The equation builder fills in: 14 - 6 + 5 = ?. `Solve` lets the child type the answer.

**Ruling out.** The answer glows on a box's sticker; the box gets a gentle "not here" tag. A wrong answer that matches no sticker: "No box has that number. Check the bars." A wrong answer that hits a sticker still gets checked: "Hmm, let's check that one," and the bars replay.

**Clue types.** Start unknown (? + 8 - 3 = 20), change unknown, result unknown, and compare (17 + 9 = ?). Each case has one two-step clue.

**The last box (the aha).** After four clues, one box is left. The child taps it; the lid opens; Sam hugs the fox. "You used the clues to find it!"

**The end.** The case file with each clue, bar model and equation. `Print` prints it.

**Case maker (extra).** The teacher writes clues and stickers; nothing leaves the device.

## Content
- Three cases (a fox, a lunch box, a library book), twelve clues within 100 with every unknown position, all spoken. Nothing is stolen; things are just lost and found.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Bars can be dragged off and redrawn; `Read again` repeats the clue.
- Keyboard: Tab to the log, bars, the box for the unknown, the keypad and boxes; Enter places; number keys type.
- With Motion off the lid opens without swinging.

## Look
- Accent `--brand` #4a3a7a mystery violet (header, the log, buttons); gold #f4c542 (the unknown box, the matched sticker); paper #f4f2f9; ink #151029; muted #535066.
- Contrast (WCAG 2.1, computed): white on brand 9.64:1; brand on paper 8.69:1; ink on paper 16.62:1; muted on paper 6.99:1; ink on gold 11.35:1.
- Never color alone: ruled-out boxes get a "not here" tag and an X.
- Different from this batch (cafeteria brick, garden green, terracotta brown, lake teal).

## Art
- People (illustrated): Sam and two other first graders for the other cases, labeled "illustration" (Gemini, `people: true`, 3; cutout yes).
- Local FLUX (`scripts/localart.py`): the closet (1, 16:9), the fox, the lunch box, the library book (3, 1:1).
- Drawn in code: boxes and stickers, bars, the equation builder.
About 7 images.

## Voice
Two bank voices, each unique in this batch: `smooth-narrator` as the log; `playful-friend` as Sam and the hints. `Curio.voice` with `scope: () => state.mode + ':' + state.case + ':' + state.clue + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `log`: "Tap the log."
- how `bars`: "Drag bars to show the story."
- how `solve`: "Type the answer, then tap Enter."
- how `open`: "Tap the last box."
- event, whole, each clue.
- event, whole, the last box.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: snap-bars, the equation builder with a box, sticker matching. Cases sit in a marked block `/* LOST-AND-FOUND DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Answer | Type each sticker number | Only the right answer rules a box out; others replay the bars. |
| Last box | Open boxes at random | Boxes open only after their clue is solved or ruled out. |
| Bars | Skip the model | Allowed, but a wrong answer opens the model. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `log`.
2. Clue (whole), waits. `bars`; `solve`.
3. Ruling out.
4. Last box (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 2.OA.1 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Bar (tape) diagrams help children model word problems | Common Core Standards Writing Team (2011), "Progressions for the CCSS, K-5 Operations and Algebraic Thinking" | Ng and Lee (2009), "The model method: Singapore children's tool for representing and solving algebraic word problems", Journal for Research in Mathematics Education | yes |
| Start-unknown and compare problems are harder and need a model | Carpenter and others, "Children's Mathematics: Cognitively Guided Instruction" (1999) | Common Core Standards Writing Team (2011), "Progressions for the CCSS, K-5 Operations and Algebraic Thinking" | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad r10, 2026-11-10): 14 - 6 + 5 = 13; ? + 8 - 3 = 20 gives 15; 17 + 9 = 26; 45 - 18 - 5 = 22; four answers rule out four boxes and leave 38; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 clue, model and boxes; at 680x425 sticker chips.
2. Start, change and result unknowns are modeled and solved. (2.OA.1)
3. Compare clues are modeled with two bars. (2.OA.1)
4. Each case has a two-step clue and ends with one box left. (2.OA.1)
5. Every card is spoken; every control is 56 px or more.
6. Sam is labeled illustration; nothing is stolen.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: jumps; no network requests.

## Open questions
None.

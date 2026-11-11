# Recipe Scaler

## One idea
Grandpa Lou (made up, labeled "illustration") is making his cornbread for the class party, but the measuring cups are lost except a drawer of one-size scoops (1/4 cup, 1/3 cup, 1/8 cup), so the child fills each amount scoop by scoop and writes it as a sum of unit fractions (3/4 cup of milk is 1/4 + 1/4 + 1/4), splits amounts other ways (3/8 = 1/8 + 2/8), fills mixed amounts as wholes and fourths (1 3/4 cups is 7/4 and back), then makes the recipe bigger the only way the scoops allow: a double batch is one batch poured onto another (1 3/4 + 1 3/4 = 3 2/4 cups of flour), and the pantry rounds take away what was used (2 1/4 - 1 3/4 = 2/4 cup of sugar); the finished double-batch card is checked by a test bake that rises only if every amount is right, and the child sees that a bigger recipe is just more scoops of the same size joined together, so a fourth grader learns to see fractions as sums of unit fractions and to add and subtract fractions and mixed numbers with like denominators. Scaling by multiplying (6 batches is 6 x 2/3) is the next tool's job.

## Not like
- fraction-kitchen (5, concept): mixed cup sizes and unlike denominators, same family. Here one-size scoops and like denominators.
- kitchen-lab (3, spec): grams, liters and minutes. Here fractions of a cup.
- pizza-party (1, spec): halves and fourths as fair shares, same family. Here counting unit fractions.
- grocery-run (5, concept): budget shopping. Here scaling amounts.

## Who and how
- Grade 4, Math, module "Adding and Multiplying Fractions". Standards: 4.NF.3 (understand a fraction a/b with a > 1 as a sum of fractions 1/b: a. understand addition and subtraction of fractions as joining and separating parts referring to the same whole; b. decompose a fraction into a sum of fractions with the same denominator in more than one way; c. add and subtract mixed numbers with like denominators; d. solve word problems involving addition and subtraction of fractions referring to the same whole and having like denominators). Not here: 4.NF.4 (a to c), multiplying a fraction by a whole number, which has its own lesson tool in this module (approved 2026-11-10).
- Format: builder (changed from tycoon). Driver: one student alone (tool.json `driver: "student"`). Role: lesson. `Read` reads every card. Controls 48 px or more.
- Three scoop sizes, nine cornbread ingredients, one round Grandpa Lou works first, eight building rounds, six double-batch rounds, ten pantry rounds, eight kitchen story problems, the double-batch card, the test bake, then ten items on your own. Progress saves on the device, so the kitchen can be finished over two sittings. Extra: Family recipe (type in a family recipe and scale it; it stays on the device, said on screen). tool.json `modes: ["Party kitchen", "Family recipe"]`, `minutes: "35-45"`, `grades_label: "Grade 4"`.
- Change note (spec fix, 2026-11-10): the kitchen, Grandpa Lou and the scoops stay. Before, the sum strip wrote every equation and the pour did the adding, most codes had four rounds or fewer, and the story problems were one sentence. Now the child writes every equation in empty boxes and the scoops or the pour only confirm it afterward; Grandpa Lou works one amount first as the model; each code has five or more rounds that differ; the story problems are listed in full with an equation and a shaded strip to make; and the Content list names every amount.
- Change note (split, 2026-11-11): 4.NF.4 (a to c) left for the new lesson tool, so the six scaling rounds, the rule card, the five party stories and the "count times the unit fraction" line are gone. The room went to more items: two more building rounds, seven second ways, eight mixed-number sums and differences, two different-wholes rounds and eight stories. The recipe is now doubled by adding a batch to a batch, which is 4.NF.3c, so the tool still ends on a bigger recipe and a test bake. Added the three hooks: ten items on your own with the end screen by code, English learner supports, access.
- English learners: every spoken line is also on screen in short sentences. The words unit fraction, sum, mixed number, whole and equation each show with a picture of scoops the first time they are used. The because sentence and the story answers come with a frame the child may take or leave.

## Standards map
| Code | The standard's verb and its parts | Who does the verb | Student action that teaches it | Items that differ | What they see | Done when check |
|---|---|---|---|---|---|---|
| 4.NF.3 | understand a fraction a/b with a > 1 as a sum of fractions 1/b | the student | Fill an amount scoop by scoop, then write it as a sum of unit fractions and as one fraction | 8 (fourths, thirds, eighths; three amounts above 1) and 2 on your own | the cup filling; the child's own equation | 2, 7 |
| 4.NF.3b | decompose a fraction into a sum with the same denominator in more than one way; record each by an equation; justify | the student | Ring the scoops into groups a second way, write that equation, and finish "Both ways are the same amount because ..." | 7 (3/4, 3/8, 5/8, 6/8, 7/4, 4/3, 17/8) and 2 on your own | the same scoops in two groupings | 3, 7 |
| 4.NF.3a | understand adding and subtracting as joining and separating parts of the same whole | the student | Pour or take away and write the equation; on two rounds say why parts of different wholes cannot be added | 5 (3 with fractions under 1, 2 different-wholes rounds) and 2 on your own | parts joining in one bowl | 4, 7 |
| 4.NF.3c | add and subtract mixed numbers with like denominators, by equivalent fractions or by properties and the add-subtract relation | the student | Rename each mixed number as fourths, thirds or eighths (or add wholes and parts), type the answer before the pour, and check each subtraction by adding back | 11 (7 sums, 4 differences) and 2 on your own | the pour regrouping only after the answer is typed | 4, 7 |
| 4.NF.3d | solve word problems on adding and subtracting fractions of the same whole, with models and equations | the student | Shade a strip for the story, write an equation with a box for the unknown, solve | 8 kitchen stories and 2 on your own | the shaded strip beside the equation | 5, 7 |

## Screens and modes
Header (kit): title "Recipe Scaler"; `Party kitchen`, `Family recipe`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A kitchen counter, a handwritten recipe card, a drawer of single scoops and Grandpa Lou with a mixing bowl. The welcome is queued (`welcomeAfter: true`): "We lost the measuring cups! All we have is the 1/4 cup scoop. How many scoops is 3/4 cup of milk? Tap the scoop to fill the cup." First hint: "Tap the 1/4 scoop."

**Grandpa Lou goes first (the model).** Lou measures 2/4 cup of oil: two taps of the 1/4 scoop, then he writes on the strip, saying each part, "1/4 + 1/4 = 2/4. Two scoops of one fourth." This round cannot be skipped and `Lou's example` reopens it. A second short model opens the story problems (Lou shades a strip and writes an equation with a box).

**Building (focus: the cup).** At 1366x768 the cup and scoops fill the left with the recipe card right; at 680x425 the card is a sheet. The child taps scoops into the cup, then fills the empty strip: a sum box for each scoop (1/4 + 1/4 + 1/4), the count of scoops (3) and the total (3/4). The strip does not write itself. `Check` compares all three with the cup. On seven of the eight rounds a second step follows: "Fill the same amount a second way." The child drags a ring around scoops to make groups of other sizes (3/8 as one scoop and a group of two), writes the new equation (3/8 = 1/8 + 2/8), and finishes the sentence "Both ways are the same amount because both have __ eighths." Mixed amounts are written both ways (1 3/4 = 4/4 + 3/4 = 7/4).

**Double batch and pantry.** First the six card amounts are doubled, one batch poured onto another (3/4 + 3/4), and each answer goes on the double-batch card. Then ten pantry rounds add and take away. Each round shows two amounts and an empty equation. The child writes the equation, renames mixed numbers (1 3/4 as 7/4 and 2 2/4 as 10/4, or adds wholes and fourths apart, the child's choice), and types the answer. Only then does the pour run, and it is the check: the fourths regroup and the bowl's mark lands on the typed answer or misses it. After each take-away the child adds back to check (2/4 + 1 3/4 = 2 1/4). On the mug round Lou holds 1/4 of a big mug and 1/4 cup: the child taps `Cannot add yet` or `2/4`, and finishes "The wholes must be the __ ." A wrong pick shows the two unequal quarters side by side. The pan round does the same with 1/3 of a small pan and 1/3 of a big pan.

**Kitchen stories.** Eight story cards. For each the child shades a strip cut into the story's pieces, writes an equation with a box for the unknown, and types the answer with its unit. Any true equation for the story is accepted (5/8 + __ = 2 and 2 - 1 3/8 = __ both pass).

**The test bake (the aha).** The double-batch card goes in the oven. Right amounts: the cornbread rises golden. A wrong amount: it comes out flat and the card marks the line to fix. Grandpa Lou: "Twice the bread is the same scoops, twice. A bigger recipe is just more scoops joined together."

**On your own.** Ten items, two for each code, with Lou gone from the counter: `Lou's example` and the hints are hidden, the scoops and the pour do not run, and each item takes one answer. Nothing is marked until all ten are in.

**The end.** The double-batch card and a results strip for the teacher: for each code, how many of its two items were right (shown as numbers and words, such as "4.NF.3c: 1 of 2"), with the item missed. `Print` prints both.

**Family recipe (extra).** The child types a recipe and a batch count; nothing leaves the device.

## Content
- Scoops of 1/3, 1/4 and 1/8 cup. Amounts are kept exact; cups and fill levels are drawn in code. All cards are readable with `Read`.
- Lou's model: oil, 2/4 cup.
- Building rounds: milk 3/4 (1/4 scoop; second way 1/4 + 2/4), cornmeal 2/3 (1/3 scoop; no second way), butter 3/8 (1/8 scoop; 1/8 + 2/8), honey 5/8 (1/8 scoop; 2/8 + 3/8 or 1/8 + 4/8), sugar 6/8 (1/8 scoop; 3/8 + 3/8, 2/8 + 4/8 or 1/8 + 5/8), flour 1 3/4 = 7/4 (1/4 scoop; 4/4 + 3/4), buttermilk 1 1/3 = 4/3 (1/3 scoop; 3/3 + 1/3), yogurt 2 1/8 = 17/8 (1/8 scoop; 8/8 + 8/8 + 1/8). Any second way that sums to the amount and differs from the first passes.
- Double-batch rounds (the card): milk 3/4 + 3/4 = 6/4 = 1 2/4; cornmeal 2/3 + 2/3 = 4/3 = 1 1/3; butter 3/8 + 3/8 = 6/8; honey 5/8 + 5/8 = 10/8 = 1 2/8; flour 1 3/4 + 1 3/4 = 3 2/4; buttermilk 1 1/3 + 1 1/3 = 2 2/3.
- Pantry rounds: butter 2/8 + oil 5/8 = 7/8; 7/8 - 3/8 = 4/8; flour 1 3/4 + 2 2/4 = 4 1/4; sugar 2 1/4 - 1 3/4 = 2/4; milk 3 1/8 - 1 5/8 = 1 4/8; flour 2 3/8 + 1 6/8 = 4 1/8; a 5-cup bag less 1 3/4 = 3 1/4; berries 4 1/3 - 2 2/3 = 1 2/3; the mug round; the pan round. Equal answers in other forms pass (4/8 or 1/2, 17/4 or 4 1/4).
- Kitchen stories: (1) Lou stirs 3/8 cup of honey into the batter and drizzles 2/8 cup on top. How much honey in all? 5/8 cup. (2) The jug holds 3 1/4 cups of milk and the cornbread uses 1 3/4 cups. How much is left? 1 2/4 cups. (3) 5/6 of a pan is left and the class eats 3/6 of the pan. How much now? 2/6. (4) Mia brings 1 2/3 cups of berries and Dev brings 2 2/3 cups. How many together? 4 1/3 cups. (5) The recipe needs 2 cups of cornmeal and Lou has 1 3/8 cups. How much more? 5/8 cup. (6) A bag holds 4 cups of flour. Lou uses 1 3/4 cups for the first pan and 1 3/4 cups for the second. How much is left? 2/4 cup. (7) Dev pours 7/8 cup of juice. That is 3/8 cup more than Mia pours. How much does Mia pour? 4/8 cup. (8) A pan is cut into 12 equal pieces. The class eats 5/12 of the pan at lunch and 4/12 after school. What fraction is left? 3/12.
- On your own, with what each common wrong answer means:
  - 4.NF.3: "Write 5/6 as a sum of unit fractions." (1/6 five times.) "How many 1/8 scoops fill 1 3/8 cups?" (11.) An answer of 3 means the child counted only the eighths after the whole and does not yet see the whole as 8/8.
  - 4.NF.3a: 2/6 + 3/6 (5/6); 9/10 - 4/10 (5/10). An answer of 5/12 or 5/0 means the child is adding or subtracting the bottoms as well, treating the fraction as two whole numbers.
  - 4.NF.3b: "Write 7/8 as a sum two ways." "Write 1 2/5 as a sum two ways." Two equations that only swap the order (1/8 + 6/8 and 6/8 + 1/8) mean the child has one split, not two. A sum that misses the amount means the pieces were not counted.
  - 4.NF.3c: 2 3/5 + 1 4/5 (4 2/5; 3 7/5 passes and is noted "not regrouped"); 5 1/6 - 2 5/6 (2 2/6). An answer of 3 4/6 means the child took the smaller part from the larger in each place and did not rename a whole.
  - 4.NF.3d: "Ana runs 1 3/10 miles on Monday and 2 9/10 miles on Tuesday. How far in all?" (4 2/10 miles.) "A 3-cup jug has 1 5/8 cups of water in it. How much more fills it?" (1 3/8 cups.) An answer of 4 5/8 means the child added the two numbers on the card without reading what was asked.
- The double-batch card for the test bake holds the six doubled amounts.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A scoop can be poured back out until `Check`.
- Keyboard: Tab to scoops, the cup, the sum strip, the batch counter and the oven; Enter scoops or bakes.
- With Motion off cups fill at once and the bake shows a before and after.
- Access: every action works by tap and by keyboard. Rings are made by dragging or by tapping scoops to pick them and then `Group`. Strips are shaded by tap, or by arrow keys and Space. Motion can be paused. The pour's result is also written ("Your mark: 4 1/4. The bowl: 4 1/4.").
- On your own: one answer each, no feedback until the tenth is in, then every item shows right or not with the keyed answer.

## Look
- Accent `--brand` #2b5797 kitchen-tile blue (header, the recipe card, buttons); gold #f4c542 (the scoop in hand, a right line); paper #eef3fa; ink #0a1a30; muted #4f5868.
- Contrast (WCAG 2.1, computed): white on brand 7.21:1; brand on paper 6.47:1; ink on paper 15.65:1; muted on paper 6.43:1; ink on gold 10.73:1.
- Never color alone: every cup shows its amount in numbers; a line to fix carries a mark and words.
- Different from this batch (tomato red, dungeon violet, highway green, soil brown).

## Art
- People (illustrated): Grandpa Lou, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the kitchen counter (1, 16:9), the recipe card (1, 4:3), eight ingredients (8, 1:1), the cornbread (2, 1:1: risen and flat).
- Drawn in code: scoops, cups and fill levels, the sum strip.
About 13 images.

## Voice
Two bank voices, each unique in this batch: `warm-teacher` as Grandpa Lou; `bright-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.item + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `scoop`: "Tap the scoop to fill the cup."
- how `write`: "Type the sum in the boxes on the strip."
- how `split`: "Drag a ring around scoops to group them another way."
- how `pour`: "Write the equation and type your answer. Then tap Pour."
- how `story`: "Shade the strip, then write the equation."
- how `own`: "Now ten on your own. Lou is not helping this time."
- event, whole, Lou's two models.
- how `bake`: "Tap the oven to test bake."
- event, whole, the test bake.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.
Every `how` line is also shown as text beside its control. Instructions use no idioms.

## Family engine
fraction-food (family "fraction-food"). Uses the shared pieces from the marked block `/* FRACTION-FOOD ENGINE: begin */ ... /* end */` as described in pizza-party's spec: share names and the fairness check, here for cup amounts. Tool-only code: scoops and cups, the sum strip, batch scaling, the test bake.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Building | Tap scoops until the cup looks full; wait for the strip | The strip is empty boxes the child fills; sum, scoop count and total must all match the cup. |
| Second way | Write the first way again | The two equations must differ; the because sentence needs the count of unit pieces typed. |
| Pour | Watch the pour, then type | The pour runs only after the answer is typed; a miss shows the gap and the round comes back with new numbers after one retry. |
| Mug and pan | Guess one of two | A wrong pick still needs the sentence finished, and the round is counted only when it is. |
| Stories | Type a number seen on the card | The answer is never a number on the card, and the equation must be true for the story. |
| Test bake | Bake until it rises | A flat bake marks the wrong line; that line's round must be redone before the oven opens again. |
| On your own | Retry until right; use the scoops | One answer each, no scoops, pour or hints, and nothing is marked until all ten are in. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued), then Lou's model (whole). `scoop`; `write`; `split`.
2. `pour`; Lou's story model (whole); `story`.
3. `bake`.
4. Test bake (whole), waits. `own`.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 4.NF.3, 4.NF.4 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| A fraction a/b is a copies of 1/b, so n x a/b is n x a copies of 1/b | Common Core Standards Writing Team (2013), "Progressions for the CCSS, 3-5 Number and Operations, Fractions" | Siegler and others (2010), "Developing effective fractions instruction for kindergarten through 8th grade", IES Practice Guide | yes |
| A cup is 16 tablespoons, so a 1/8 cup scoop holds 2 tablespoons | USDA, "Food Buying Guide for Child Nutrition Programs", measuring equivalents | NIST, Handbook 44, appendix C, units of liquid volume | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s12, 2026-11-10): 3/4 = 3 x 1/4; 3/8 = 1/8 + 2/8; 1 3/4 = 7/4; 1 3/4 + 2 2/4 = 4 1/4; 2 1/4 - 1 3/4 = 2/4; 6 x 2/3 = 4; 7 x 2/3 is under 5 and 8 x 2/3 is over 5; 5 x 3/8 is between 1 and 2; 16 tablespoons over 8 is 2; contrast as in Look.
Checks run again for the spec fix (Python `fractions`, scratchpad s/fx, 2026-11-10): every building amount and second way; 2/8 + 5/8 = 7/8; 7/8 - 3/8 = 4/8; 1 3/4 + 2 2/4 = 4 1/4; 2 1/4 - 1 3/4 = 2/4; 1 2/3 + 1 2/3 = 3 1/3; 3 1/8 - 1 5/8 = 1 4/8; 2 3/8 + 1 6/8 = 4 1/8; the five kitchen stories (5/8, 1 2/4, 2/6, 4 1/3, 5/8); the six scaling rounds (4, 4 2/4, 2 2/8, 2 4/8, 5 1/4, 1 7/8); the five party stories (8 batches since 7 x 2/3 = 14/3 is under 5 and 16/3 is over; 3 3/4; 2 2/3; 1 3/4; 1 7/8). No story answer repeats a number printed on its own card.
Checks run for the split (Python `fractions`, scratchpad s/fx, 2026-11-11): the six doubles (1 2/4, 1 1/3, 6/8, 1 2/8, 3 2/4, 2 2/3); 5 - 1 3/4 = 3 1/4; 4 1/3 - 2 2/3 = 1 2/3; 17/8 = 2 1/8; stories 6 to 8 (2/4, 4/8, 3/12); on your own: 11 scoops, 5/6, 5/10, 4 2/5, 2 2/6, 4 2/10, 1 3/8, and the wrong answer 3 + 1 5/8 = 4 5/8. The earlier scaling checks no longer apply.

## Done when
1. Focus and fold: at 1366x768 cup and card; at 680x425 card as a sheet.
2. Eight amounts are filled and the child writes each as a sum of unit fractions and as one fraction. (4.NF.3)
3. Seven amounts are grouped a second way with the child's own equation and because sentence. (4.NF.3b)
4. Six double-batch rounds and ten pantry rounds: the equation and answer are typed before the pour, take-aways are checked by adding back, and the mug and pan rounds are answered. (4.NF.3a, 4.NF.3c)
5. Eight kitchen stories are solved with a shaded strip and an equation. (4.NF.3d)
6. Lou's models play first and can be reopened; the test bake rises only when all six lines are right.
7. Ten items on your own run with no model, hint, scoops or pour, one answer each; the end screen shows the result for each of the five codes and the items missed. (all codes)
8. `Read` reads every card; every control is 48 px or more; every spoken instruction is also on screen, and each key word shows with a picture at first use.
9. Every action works by keyboard as well as tap, rings and shading have a tap or key way, and nothing is shown by color alone.
10. Family recipes stay on the device, said on screen; Grandpa Lou is labeled illustration.
11. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
12. Motion off: cups fill at once; motion can be paused; no network requests.

## Open questions
- The idea card changes the format from tycoon to builder (default used: builder, since one recipe card is built and tested and nothing runs over time).
- The idea card flags overlap with fraction-kitchen (default used: this tool keeps one-size scoops and like denominators; fraction-kitchen keeps mixed cup sizes and unlike denominators).

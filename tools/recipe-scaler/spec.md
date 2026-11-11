# Recipe Scaler

## One idea
Grandpa Lou (made up, labeled "illustration") is making his cornbread for the class party, but the measuring cups are lost except a drawer of one-size scoops (1/4 cup, 1/3 cup, 1/8 cup), so the child fills each amount scoop by scoop and writes it as a count of unit fractions (3/4 cup of milk is 1/4 + 1/4 + 1/4 = 3 x 1/4), splits amounts other ways (3/8 = 1/8 + 2/8), fills mixed amounts as wholes and fourths (1 3/4 cups is 7/4 and back), pours two bags of flour together (1 3/4 + 2 2/4 = 4 1/4 cups) and takes away what was used (2 1/4 - 1 3/4 = 2/4 cup of sugar); then the party needs 6 batches, and 6 x 2/3 cup becomes 6 x 2 scoops of 1/3, which is 12/3 or 4 cups, filling on screen; questions ask which batch count first needs more than 5 cups and between which two whole numbers 5 x 3/8 lands; the finished recipe card is checked by a test bake that rises only if every amount is right, and the child sees that scaling a recipe is just counting scoops, so a fourth grader learns to see fractions as sums of unit fractions, to add and subtract mixed numbers with like denominators, and to multiply a fraction by a whole number.

## Not like
- fraction-kitchen (5, concept): mixed cup sizes and unlike denominators, same family. Here one-size scoops and like denominators.
- kitchen-lab (3, spec): grams, liters and minutes. Here fractions of a cup.
- pizza-party (1, spec): halves and fourths as fair shares, same family. Here counting unit fractions.
- grocery-run (5, concept): budget shopping. Here scaling amounts.

## Who and how
- Grade 4, Math, module "Adding and Multiplying Fractions". Standards: 4.NF.3 (understand a fraction a/b with a > 1 as a sum of fractions 1/b: a. understand addition and subtraction of fractions as joining and separating parts referring to the same whole; b. decompose a fraction into a sum of fractions with the same denominator in more than one way; c. add and subtract mixed numbers with like denominators; d. solve word problems involving addition and subtraction of fractions referring to the same whole and having like denominators), 4.NF.4 (apply and extend previous understandings of multiplication to multiply a fraction by a whole number: a. understand a fraction a/b as a multiple of 1/b; b. understand a multiple of a/b as a multiple of 1/b, and use this to multiply a fraction by a whole number; c. solve word problems involving multiplication of a fraction by a whole number).
- Format: builder (changed from tycoon). Driver: one student alone (tool.json `driver: "student"`). Role: lesson. `Read` reads every card. Controls 48 px or more.
- Three scoop sizes, eight cornbread ingredients, one round Grandpa Lou works first, six building rounds, eight pour-and-take-away rounds, five kitchen story problems, six scaling rounds, five party story problems, the recipe card, the test bake. Progress saves on the device, so the kitchen can be finished over two sittings. Extra: Family recipe (type in a family recipe and scale it; it stays on the device, said on screen). tool.json `modes: ["Party kitchen", "Family recipe"]`, `minutes: "35-50"`, `grades_label: "Grade 4"`.
- Change note (spec fix, 2026-11-10): the kitchen, Grandpa Lou and the scoops stay. Before, the sum strip wrote every equation and the pour did the adding, most codes had four rounds or fewer, and the story problems were one sentence. Now the child writes every equation in empty boxes and the scoops or the pour only confirm it afterward; Grandpa Lou works one amount first as the model; each code has five or more rounds that differ; the story problems are listed in full with an equation and a shaded strip to make; and the Content list names every amount.

## Standards map
| Code | The standard's verb and its parts | Who does the verb | Student action that teaches it | Items that differ | What they see | Done when check |
|---|---|---|---|---|---|---|
| 4.NF.3, 4.NF.4a | understand a/b as a sum of 1/b pieces and as a x (1/b) | the student | Fill an amount scoop by scoop, then write it as a sum and as a count times the unit fraction | 6 (fourths, thirds, eighths; two amounts above 1) | the cup filling; the child's own equation | 2 |
| 4.NF.3b | decompose a fraction into a sum with the same denominator in more than one way; record each by an equation; justify | the student | Ring the scoops into groups a second way, write that equation, and finish "Both ways are the same amount because ..." | 5 (3/4, 3/8, 5/8, 7/4, 4/3) | the same scoops in two groupings | 3 |
| 4.NF.3a | understand adding and subtracting as joining and separating parts of the same whole | the student | Pour or take away and write the equation; on the mug round, say why 1/4 mug and 1/4 cup cannot be added | 8 pour rounds, 1 of them the mug | parts joining in one bowl | 4 |
| 4.NF.3c | add and subtract mixed numbers with like denominators, by equivalent fractions or by properties and the add-subtract relation | the student | Rename each mixed number as fourths, thirds or eighths (or add wholes and parts), type the answer before the pour, and check each subtraction by adding back | 5 (3 sums, 2 differences) | the pour regrouping only after the answer is typed | 4 |
| 4.NF.3d | solve word problems on adding and subtracting fractions of the same whole, with models and equations | the student | Shade a strip for the story, write an equation with a box for the unknown, solve | 5 kitchen stories | the shaded strip beside the equation | 5 |
| 4.NF.4, 4.NF.4b | understand a multiple of a/b as a multiple of 1/b; multiply a fraction by a whole number | the student | Write n x (a/b) as (n x a) scoops of 1/b, then as one fraction and a mixed number; fill the rule card | 6 (thirds, fourths, eighths; batch counts 3 to 6) | scoops piling into cups after the writing | 6 |
| 4.NF.4c | solve word problems on multiplying a fraction by a whole number, with models and equations | the student | Shade batches on a strip, write the equation, solve, and name the two whole numbers the answer sits between | 5 party stories | the strip of batches | 7 |

## Screens and modes
Header (kit): title "Recipe Scaler"; `Party kitchen`, `Family recipe`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A kitchen counter, a handwritten recipe card, a drawer of single scoops and Grandpa Lou with a mixing bowl. The welcome is queued (`welcomeAfter: true`): "We lost the measuring cups! All we have is the 1/4 cup scoop. How many scoops is 3/4 cup of milk? Tap the scoop to fill the cup." First hint: "Tap the 1/4 scoop."

**Grandpa Lou goes first (the model).** Lou measures 2/4 cup of oil: two taps of the 1/4 scoop, then he writes on the strip, saying each part, "1/4 + 1/4 = 2/4, and that is 2 x 1/4." This round cannot be skipped and `Lou's example` reopens it. A second short model opens the story problems (Lou shades a strip and writes an equation with a box).

**Building (focus: the cup).** At 1366x768 the cup and scoops fill the left with the recipe card right; at 680x425 the card is a sheet. The child taps scoops into the cup, then fills the empty strip: a sum box for each scoop (1/4 + 1/4 + 1/4), the count form (3 x 1/4) and the total (3/4). The strip does not write itself. `Check` compares all three with the cup. On five of the six rounds a second step follows: "Fill the same amount a second way." The child drags a ring around scoops to make groups of other sizes (3/8 as one scoop and a group of two), writes the new equation (3/8 = 1/8 + 2/8), and finishes the sentence "Both ways are the same amount because both have __ eighths." Mixed amounts are written both ways (1 3/4 = 4/4 + 3/4 = 7/4).

**Pour and take away.** Each round shows two amounts and an empty equation. The child writes the equation, renames mixed numbers (1 3/4 as 7/4 and 2 2/4 as 10/4, or adds wholes and fourths apart, the child's choice), and types the answer. Only then does the pour run, and it is the check: the fourths regroup and the bowl's mark lands on the typed answer or misses it. After each take-away the child adds back to check (2/4 + 1 3/4 = 2 1/4). On the mug round Lou holds 1/4 of a big mug and 1/4 cup: the child taps `Cannot add yet` or `2/4`, and finishes "The wholes must be the __ ." A wrong pick shows the two unequal quarters side by side.

**Kitchen stories.** Five story cards. For each the child shades a strip cut into the story's pieces, writes an equation with a box for the unknown, and types the answer with its unit. Any true equation for the story is accepted (5/8 + __ = 2 and 2 - 1 3/8 = __ both pass).

**Scaling.** "The party needs 6 batches." The child writes 6 x 2/3 as scoops (6 x 2 = 12 scoops of 1/3), then as one fraction (12/3) and as cups (4). After the writing the scoops pile into cups as the check. After the third scaling round the rule card appears: "n x (a/b) = (__ x __)/__", filled by dragging n, a and b, with the line "6 batches of 2 scoops is __ scoops" typed under it.

**Party stories.** Five story cards. The child shades one batch after another on a strip, writes the equation, solves, and taps the two whole numbers the answer sits between.

**The test bake (the aha).** The scaled card goes in the oven. Right amounts: the cornbread rises golden. A wrong amount: it comes out flat and the card marks the line to fix. Grandpa Lou: "6 batches is just 6 times the scoops. Scaling is counting."

**The end.** The scaled recipe card. `Print` prints it.

**Family recipe (extra).** The child types a recipe and a batch count; nothing leaves the device.

## Content
- Scoops of 1/3, 1/4 and 1/8 cup. Amounts are kept exact; cups and fill levels are drawn in code. All cards are readable with `Read`.
- Lou's model: oil, 2/4 cup.
- Building rounds: milk 3/4 (1/4 scoop; second way 1/4 + 2/4), cornmeal 2/3 (1/3 scoop; no second way), butter 3/8 (1/8 scoop; 1/8 + 2/8), honey 5/8 (1/8 scoop; 2/8 + 3/8 or 1/8 + 4/8), flour 1 3/4 = 7/4 (1/4 scoop; 4/4 + 3/4), buttermilk 1 1/3 = 4/3 (1/3 scoop; 3/3 + 1/3). Any second way that sums to the amount and differs from the first passes.
- Pour and take away rounds: butter 2/8 + oil 5/8 = 7/8; 7/8 - 3/8 = 4/8; flour 1 3/4 + 2 2/4 = 4 1/4; sugar 2 1/4 - 1 3/4 = 2/4; cornmeal 1 2/3 + 1 2/3 = 3 1/3; milk 3 1/8 - 1 5/8 = 1 4/8; flour 2 3/8 + 1 6/8 = 4 1/8; the mug round. Equal answers in other forms pass (4/8 or 1/2, 17/4 or 4 1/4).
- Kitchen stories: (1) Lou stirs 3/8 cup of honey into the batter and drizzles 2/8 cup on top. How much honey in all? 5/8 cup. (2) The jug holds 3 1/4 cups of milk and the cornbread uses 1 3/4 cups. How much is left? 1 2/4 cups. (3) 5/6 of a pan is left and the class eats 3/6 of the pan. How much now? 2/6. (4) Mia brings 1 2/3 cups of berries and Dev brings 2 2/3 cups. How many together? 4 1/3 cups. (5) The recipe needs 2 cups of cornmeal and Lou has 1 3/8 cups. How much more? 5/8 cup.
- Scaling rounds: 6 x 2/3 = 12/3 = 4 (cornmeal); 6 x 3/4 = 18/4 = 4 2/4 (milk); 6 x 3/8 = 18/8 = 2 2/8 (butter); 4 x 5/8 = 20/8 = 2 4/8 (honey, a smaller party); 3 x 7/4 = 21/4 = 5 1/4 (flour); 5 x 3/8 = 15/8 = 1 7/8 (butter).
- Party stories: (1) One batch takes 2/3 cup of cornmeal. Which batch count first needs more than 5 cups? 8 batches, 16/3 cups. (2) 5 tables each get 3/4 of a pan. How many pans? 15/4 = 3 3/4, between 3 and 4. (3) 4 batches at 2/3 cup each? 8/3 = 2 2/3 cups, between 2 and 3. (4) Each batch takes 1/4 hour to mix. How long for 7 batches? 7/4 = 1 3/4 hours, between 1 and 2. (5) 5 batches at 3/8 cup of butter? 15/8, between 1 and 2.
- The recipe card for the test bake holds the six scaled amounts.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A scoop can be poured back out until `Check`.
- Keyboard: Tab to scoops, the cup, the sum strip, the batch counter and the oven; Enter scoops or bakes.
- With Motion off cups fill at once and the bake shows a before and after.

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
- how `scale`: "Write how many scoops in all."
- event, whole, Lou's two models.
- how `bake`: "Tap the oven to test bake."
- event, whole, the test bake.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
fraction-food (family "fraction-food"). Uses the shared pieces from the marked block `/* FRACTION-FOOD ENGINE: begin */ ... /* end */` as described in pizza-party's spec: share names and the fairness check, here for cup amounts. Tool-only code: scoops and cups, the sum strip, batch scaling, the test bake.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Building | Tap scoops until the cup looks full; wait for the strip | The strip is empty boxes the child fills; sum, count form and total must all match the cup. |
| Second way | Write the first way again | The two equations must differ; the because sentence needs the count of unit pieces typed. |
| Pour | Watch the pour, then type | The pour runs only after the answer is typed; a miss shows the gap and the round comes back with new numbers after one retry. |
| Mug | Guess one of two | A wrong pick still needs the sentence finished, and the round is counted only when it is. |
| Stories | Type a number seen on the card | The answer is never a number on the card, and the equation must be true for the story. |
| Scaling | Multiply both numbers | 6 x 2/3 typed as 12/18 fails; the scoops then show 12 thirds and the line is redone. |
| Between | Guess the pair of whole numbers | Five pairs are offered and a wrong pair sends the child back to the strip. |
| Test bake | Bake until it rises | A flat bake marks the wrong line; that line's round must be redone before the oven opens again. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued), then Lou's model (whole). `scoop`; `write`; `split`.
2. `pour`; Lou's story model (whole); `story`.
3. `scale`; `story`; `bake`.
4. Test bake (whole), waits.
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

## Done when
1. Focus and fold: at 1366x768 cup and card; at 680x425 card as a sheet.
2. Six amounts are filled and the child writes each as a sum and as a count times a unit fraction. (4.NF.3, 4.NF.4a)
3. Five amounts are grouped a second way with the child's own equation and because sentence. (4.NF.3b)
4. Eight pour and take-away rounds: the equation and answer are typed before the pour, take-aways are checked by adding back, and the mug round is answered. (4.NF.3a, 4.NF.3c)
5. Five kitchen stories are solved with a shaded strip and an equation. (4.NF.3d)
6. Six scaling rounds are written as scoops, a fraction and cups, and the rule card is filled. (4.NF.4, 4.NF.4b)
7. Five party stories are solved with a strip, an equation and the two whole numbers. (4.NF.4c)
8. Lou's models play first and can be reopened; the test bake rises only when all six lines are right.
9. `Read` reads every card; every control is 48 px or more.
10. Family recipes stay on the device, said on screen; Grandpa Lou is labeled illustration.
11. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
12. Motion off: cups fill at once; no network requests.

## Open questions
- The idea card changes the format from tycoon to builder (default used: builder, since one recipe card is built and tested and nothing runs over time).
- The idea card flags overlap with fraction-kitchen (default used: this tool keeps one-size scoops and like denominators; fraction-kitchen keeps mixed cup sizes and unlike denominators).

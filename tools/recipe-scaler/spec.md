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
- Format: builder (changed from tycoon). Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Three scoop sizes, eight cornbread ingredients, four building rounds, four add-and-subtract rounds, four scaling rounds, the recipe card, the test bake. Extra: Family recipe (type in a family recipe and scale it; it stays on the device, said on screen). tool.json `modes: ["Party kitchen", "Family recipe"]`, `minutes: "20-30"`, `grades_label: "Grade 4"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 4.NF.3a, 4.NF.3b | Fill amounts scoop by scoop; split them another way | the cup filling; the sum written | 2 |
| 4.NF.3c, 4.NF.3d | Pour two amounts together; take away what was used | wholes and fourths regrouping | 3 |
| 4.NF.4a to 4.NF.4c | Scale to 6 batches by counting scoops; place products between wholes | scoops piling into cups | 4 |

## Screens and modes
Header (kit): title "Recipe Scaler"; `Party kitchen`, `Family recipe`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A kitchen counter, a handwritten recipe card, a drawer of single scoops and Grandpa Lou with a mixing bowl. The welcome is queued (`welcomeAfter: true`): "We lost the measuring cups! All we have is the 1/4 cup scoop. How many scoops is 3/4 cup of milk? Tap the scoop to fill the cup." First hint: "Tap the 1/4 scoop."

**Building (focus: the cup).** At 1366x768 the cup and scoops fill the left with the recipe card right; at 680x425 the card is a sheet. Each tap adds one scoop and writes it into the sum strip (1/4 + 1/4 + 1/4 = 3 x 1/4 = 3/4). A second try splits the same amount another way. Mixed amounts fill as whole cups plus fourths and are rewritten (1 3/4 = 7/4).

**Pour and take away.** Two flour bags (1 3/4 and 2 2/4) pour into one bowl; fourths regroup into a whole: 4 1/4 cups. Sugar: 2 1/4 cups less the 1 3/4 used leaves 2/4. Kitchen word problems follow.

**Scaling.** "The party needs 6 batches." 2/3 cup of cornmeal becomes 6 piles of two 1/3 scoops: 12/3 = 4 cups. Then: "Which batch count first needs more than 5 cups?" (8 batches, 16/3). "5 x 3/8 lands between which two whole numbers?" (1 and 2).

**The test bake (the aha).** The scaled card goes in the oven. Right amounts: the cornbread rises golden. A wrong amount: it comes out flat and the card marks the line to fix. Grandpa Lou: "6 batches is just 6 times the scoops. Scaling is counting."

**The end.** The scaled recipe card. `Print` prints it.

**Family recipe (extra).** The child types a recipe and a batch count; nothing leaves the device.

## Content
- Scoops of 1/3, 1/4 and 1/8 cup; eight ingredients with like-denominator amounts; twelve rounds; all readable with `Read`.
- Amounts are kept exact; cups and fill levels are drawn in code.

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
- how `split`: "Fill it another way."
- how `pour`: "Drag the bag to pour it in."
- how `scale`: "Tap plus to add a batch."
- how `bake`: "Tap the oven to test bake."
- event, whole, the test bake.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
fraction-food (family "fraction-food"). Uses the shared pieces from the marked block `/* FRACTION-FOOD ENGINE: begin */ ... /* end */` as described in pizza-party's spec: share names and the fairness check, here for cup amounts. Tool-only code: scoops and cups, the sum strip, batch scaling, the test bake.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Building | Tap scoops until the cup looks full | The sum strip must match the amount on the card. |
| Pour | Type a total | The fourths must regroup on screen first. |
| Scaling | Multiply both numbers | 6 x 2/3 typed as 12/18 fails the bake; the scoops show 12 thirds. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `scoop`; `split`.
2. `pour`.
3. `scale`; `bake`.
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

## Done when
1. Focus and fold: at 1366x768 cup and card; at 680x425 card as a sheet.
2. Amounts are built as sums of unit fractions and split two ways. (4.NF.3a, 4.NF.3b)
3. Mixed numbers with like denominators are added and subtracted in kitchen problems. (4.NF.3c, 4.NF.3d)
4. Six batches are scaled by counting scoops, with products placed between wholes. (4.NF.4)
5. `Read` reads every card; every control is 48 px or more.
6. Family recipes stay on the device, said on screen; Grandpa Lou is labeled illustration.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: cups fill at once; no network requests.

## Open questions
- The idea card changes the format from tycoon to builder (default used: builder, since one recipe card is built and tested and nothing runs over time).
- The idea card flags overlap with fraction-kitchen (default used: this tool keeps one-size scoops and like denominators; fraction-kitchen keeps mixed cup sizes and unlike denominators).

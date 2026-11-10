# Fraction Kitchen

## One idea
In a bakery test kitchen, Chef Amara (made up, labeled "illustration") needs exact amounts but the shelf holds cups of different sizes (a 1/2 cup, a 1/3 cup, a 1/4 cup), so the child estimates every pour first with benchmarks (more or less than 1/2? will it overflow a 1-cup bowl?), then pours into a mixing bowl whose marks stay blank until the child picks a shared piece size; picking sixths makes 1/2 show as 3/6 and 1/3 as 2/6, so 1/2 + 1/3 lands at 5/6 on the bowl; harder rounds pour three cups at once (1/2 + 1/3 + 1/4 in twelfths is 13/12, just over a cup), add mixed numbers (1 1/2 cups of flour and 2/3 cup more is 2 1/6), and take out (a bowl with 2 1/4 cups less 5/6 cup leaves 1 5/12); fix-the-card rounds give a helper's note saying 2/5 + 1/2 = 3/7, and the child shows with a benchmark that it can't be right (anything added to 1/2 is more than 1/2, and 3/7 is less), then pours to find 9/10; at the end the child sees that unlike pieces add once they are cut the same size and that a quick estimate catches wrong answers, so a fifth grader learns to add and subtract fractions and mixed numbers with unlike denominators by renaming with a common denominator, and to judge answers to word problems with benchmark fractions.

## Not like
- recipe-scaler (4, spec): one-size scoops and like denominators, same family. Here mixed cup sizes and unlike denominators.
- fraction-wall-duel (4, spec): comparing fractions. Here adding them.
- how-many-fit (6, concept): dividing fractions. Here adding and subtracting.
- camp-cook-share-out (5, concept): fractions as division. Here sums and differences.

## Who and how
- Grade 5, Math, module "Adding Unlike Fractions". Standards: 5.NF.1 (add and subtract fractions with unlike denominators, including mixed numbers, by replacing given fractions with equivalent fractions in such a way as to produce an equivalent sum or difference of fractions with like denominators), 5.NF.2 (solve word problems involving addition and subtraction of fractions referring to the same whole, including cases of unlike denominators, e.g., by using visual fraction models or equations to represent the problem; use benchmark fractions and number sense of fractions to estimate mentally and assess the reasonableness of answers).
- Format: puzzle. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Three cup sizes, the markable bowl, six two-cup pours, three three-cup pours, four mixed-number rounds, three take-out rounds, three fix-the-card rounds. Extra: Fewest pours (a challenge list where the class finds the fewest pours for a target). tool.json `modes: ["Test kitchen", "Fewest pours"]`, `minutes: "20-30"`, `grades_label: "Grade 5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 5.NF.1 | Pick a shared piece size and pour | 1/2 as 3/6, 1/3 as 2/6; 5/6 on the bowl | 2 |
| 5.NF.1 (mixed numbers) | Add and take out mixed amounts | 2 1/6 cups; 1 5/12 left | 3 |
| 5.NF.2 | Estimate before each pour; fix wrong cards with a benchmark | the estimate against the result; the half line | 4 |

## Screens and modes
Header (kit): title "Fraction Kitchen"; `Test kitchen`, `Fewest pours`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A bakery test kitchen, a recipe card asking for 5/6 cup of yogurt, a shelf with a 1/2 cup and a 1/3 cup, and Chef Amara. The welcome is queued (`welcomeAfter: true`): "Guess first. Will 1/2 cup and 1/3 cup overflow a 1-cup bowl? Tap your guess." First hint: "Tap a guess."

**Estimate.** Three choices: less than 1/2, between 1/2 and 1, more than 1.

**Mark the bowl (focus: the bowl).** At 1366x768 the bowl fills the middle with the cups left and the recipe card right; at 680x425 the card is a sheet. The bowl's marks are blank. The child picks a piece size (halves, thirds, fourths, sixths, twelfths); only sizes that both cups fit show both amounts as whole marks. With sixths the 1/2 pour lands at 3/6, then 1/3 adds 2/6: 5/6.

**Harder rounds.** Three cups (1/2 + 1/3 + 1/4 = 13/12, so it spills a little over 1 cup). Mixed numbers: 1 1/2 cups of flour and 2/3 cup more (2 1/6). Take out: 2 1/4 cups less 5/6 cup leaves 1 5/12.

**Fix the card.** A helper's note: 2/5 + 1/2 = 3/7. The child picks the benchmark reason (1/2 plus more is more than 1/2; 3/7 is less than 1/2), then pours to find 9/10.

**Same size (the aha).** Chef Amara: "You can't add halves and thirds until they're the same size. Cut them to sixths, and it's just counting."

**The end.** The test recipe with every pour. `Print` prints it.

**Fewest pours (extra).** Targets like 7/12 with the fewest pours.

## Content
- Cups of 1/2, 1/3 and 1/4; bowl marks in halves to twelfths; nineteen rounds; all readable with `Read`.
- Levels are exact and drawn in code.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The piece size can be changed any time; marks redraw.
- Keyboard: Tab to the estimate buttons, cups, the piece-size picker, the bowl and the note; Enter pours.
- With Motion off pours fill at once.

## Look
- Accent `--brand` #a0305a test-kitchen pink (header, the recipe card, buttons); gold #f4c542 (the cup in hand, a level that matches); paper #fbeff4; ink #2e0b19; muted #5f5157.
- Contrast (WCAG 2.1, computed): white on brand 6.85:1; brand on paper 6.12:1; ink on paper 15.92:1; muted on paper 6.70:1; ink on gold 10.96:1.
- Never color alone: marks carry fraction labels; the matching level carries a check and words.
- Different from this batch (greenhouse green, workshop copper, stadium blue, sieve purple).

## Art
- People (illustrated): Chef Amara, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the test kitchen (1, 16:9), six ingredients (6, 1:1).
- Drawn in code: cups, the bowl, marks, pours, the note.
About 8 images.

## Voice
Two bank voices, each unique in this batch: `warm-teacher` as Chef Amara; `upbeat-guide` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.piece + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `estimate`: "Tap your guess."
- how `piece`: "Pick a piece size for the bowl."
- how `pour`: "Drag a cup over the bowl to pour."
- how `fix`: "Pick the reason the note is wrong."
- event, whole, same size.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
fraction-food (family "fraction-food"). Uses the shared pieces from the marked block `/* FRACTION-FOOD ENGINE: begin */ ... /* end */` as described in pizza-party's spec: share names and exact amounts. Tool-only code: cups, the markable bowl, common piece sizes, the benchmark checker.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Piece size | Pick any size | Only a size both cups fit shows whole marks; the others show "between marks". |
| Estimate | Skip it | The cups stay on the shelf until a guess is made. |
| Fix the card | Pour first | The benchmark reason is needed before pouring. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `estimate`; `piece`.
2. `pour`.
3. `fix`.
4. Same size (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 5.NF.1, 5.NF.2 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Adding unlike fractions by renaming with a common denominator | Common Core Standards Writing Team (2013), "Progressions for the CCSS, 3-5 Number and Operations, Fractions" | Siegler and others (2010), "Developing effective fractions instruction for kindergarten through 8th grade", IES Practice Guide | yes |
| Adding tops and bottoms (2/5 + 1/2 = 3/7) is a common mistake that benchmarks catch | Siegler and others (2010), IES Practice Guide, recommendation 3 | Van de Walle, Karp and Bay-Williams (2019), "Elementary and Middle School Mathematics: Teaching Developmentally", 10th edition | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s14, 2026-11-10): 1/2 = 3/6 and 1/3 = 2/6, so 1/2 + 1/3 = 5/6; 1/2 + 1/3 + 1/4 = 13/12; 1 1/2 + 2/3 = 2 1/6; 2 1/4 - 5/6 = 1 5/12; 2/5 + 1/2 = 9/10 and 3/7 < 1/2; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 bowl, cups and card; at 680x425 card as a sheet.
2. Unlike fractions are added by picking a shared piece size. (5.NF.1)
3. Mixed numbers are added and subtracted. (5.NF.1)
4. Every pour is estimated first, and three wrong cards are fixed with benchmarks. (5.NF.2)
5. `Read` reads every card; every control is 48 px or more.
6. Chef Amara is labeled illustration.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: pours fill at once; no network requests.

## Open questions
- The idea card flags overlap with recipe-scaler (default used: mixed cup sizes and unlike denominators here; recipe-scaler keeps one-size scoops and like denominators).

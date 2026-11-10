# Class Poll

## One idea
A classroom of 18 illustrated kids (made up, labeled "illustration") votes on a question card ("Cats, dogs or fish?") one kid at a time, each holding up a picture, and the child adds a tally mark for each vote, with every fifth mark crossing the four; then the child drags one picture per tally into a picture graph with up to three rows, and questions follow (How many voted? How many chose fish? How many more chose dogs than cats?); in the line-up moment the rows of the picture graph sit side by side so the extra 3 dog pictures stick out past the cat row, and the child sees "how many more" at a glance; new polls change the question and the group (a soccer team, a family reunion), and a live mode lets a teacher enter a real class vote that stays on the device, so a first grader learns to organize, represent and interpret data with up to three categories, and to ask and answer questions about the total number of data points, how many are in each category, and how many more or fewer are in one category than in another.

## Not like
- toy-box-sort (K, spec): sorting real objects into bins. Here votes, tallies and a picture graph.
- lunch-line-data (2, concept): bar graphs and line plots, same family. Here picture graphs and tallies.
- graph-glow-up (3, concept): scaled graphs. Here one picture for each vote.
- paperclip-ruler (1, spec): measuring. Here counting answers.

## Who and how
- Grade 1, Math, module "Picture Graphs and Tallies". Standards: 1.MD.4 (organize, represent, and interpret data with up to three categories; ask and answer questions about the total number of data points, how many in each category, and how many more or less are in one category than in another).
- Format: data. Driver: one student (tool.json `driver: "student"`); the live poll is the teacher's. Every card is spoken. Controls 56 px or more.
- Six polls (pets, snacks, weather, recess game, soccer team colors, family reunion dessert), each 12 to 20 votes in three categories, three questions per poll, the line-up. Extra: Live poll (the teacher taps each real vote; nothing leaves the device). tool.json `modes: ["Poll", "Live poll"]`, `minutes: "10-20"`, `grades_label: "Grade 1"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 1.MD.4 (organize) | Tally each vote, crossing every fifth | tally marks in bundles of five | 2 |
| 1.MD.4 (represent) | Drag one picture per tally into the graph | the picture graph growing | 3 |
| 1.MD.4 (interpret) | Answer total, each and how many more | the line-up; the extra pictures | 4 |

## Screens and modes
Header (kit): title "Class Poll"; `Poll`, `Live poll`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more.

**On load and first tap.** A bright classroom with 18 kids at desks and a question card on the board: "Cats, dogs or fish?" A tally sheet with three rows. The welcome is queued (`welcomeAfter: true`): "Today's class poll: cats, dogs or fish? Each friend will hold up a picture. Tap the row to make a tally mark." First hint: "Tap the row for the vote."

**Tallying (focus: the class and sheet).** At 1366x768 the class sits at the left and the tally sheet at the right; at 680x425 one kid at a time stands in a spotlight above the sheet. Each kid holds up a picture; the child taps its row; a tally mark appears. The fifth mark crosses the four: "That's a bundle of five!"

**Picture graph.** The tallies turn into a picture graph: the child drags one picture per tally into its row, each picture on a square so rows line up.

**Questions.** "How many friends voted?" "How many chose fish?" "How many more chose dogs than cats?" Big number buttons answer.

**The line-up (the aha).** The cat row and the dog row slide together. Dogs: 8. Cats: 5. Three dog pictures stick out past the cats and glow. "Those three are how many more!"

**The end.** A poster of each poll's graph. `Print` prints the graphs and a blank tally sheet.

**Live poll (extra).** The teacher types a question and three choices, then taps each vote. Nothing is saved off the device or sent anywhere.

## Content
- Six polls with three categories each, 12 to 20 votes, 18 cartoon kids from different families labeled "illustration", all spoken. Questions are kind and ordinary; no poll ranks people.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- `Undo` removes the last tally or picture.
- Keyboard: Tab to the three rows, pictures, number buttons and Next; Enter tallies and places.
- With Motion off kids show their picture without raising it and rows jump together.

## Look
- Accent `--brand` #5d3a8f ballot violet (header, the tally sheet, buttons); gold #f4c542 (the fifth mark, the extra pictures); paper #f5f1fa; ink #1c0f2c; muted #584f63.
- Contrast (WCAG 2.1, computed): white on brand 8.51:1; brand on paper 7.64:1; ink on paper 16.33:1; muted on paper 6.94:1; ink on gold 11.19:1.
- Never color alone: rows carry picture labels and words; extras get a ring.
- Different from this batch (tomato red, notebook navy, circuit green, brass brown).

## Art
- People (illustrated): 18 cartoon kids from different families, labeled "illustration" (Gemini, `people: true`, 6 sheets of 3; cutout yes).
- Local FLUX (`scripts/localart.py`): the classroom (1, 16:9), the soccer field and the reunion yard (2, 16:9), choice pictures (18, 1:1).
- Drawn in code: tally marks, the graph grid, number buttons.
About 27 images.

## Voice
Two bank voices, each unique in this batch: `news-reader` as the poll announcer; `warm-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.poll + ':' + state.vote + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `tally`: "Tap the row for the vote."
- how `graph`: "Drag a picture into its row."
- how `ask`: "Tap the number for the answer."
- event, whole, each fifth mark.
- event, whole, the line-up.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
class-poll (family "class-poll"; no engine file yet). This tool builds the family's shared pieces first, in a marked block `/* CLASS-POLL ENGINE: begin */ ... /* end */`: a vote stream, tallies in fives, a category graph that can draw pictures (and later bars), and how-many-more line-ups; lunch-line-data reuses them.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Tally | Tap one row every time | The picture graph won't match the votes; the row is checked against the kid's picture. |
| Graph | Drop pictures anywhere | Each picture snaps only to its own row. |
| Questions | Tap numbers until right | The graph rows count themselves on a wrong answer; a new question follows. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `tally`.
2. Fifth mark (whole), waits.
3. `graph`; `ask`.
4. Line-up (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 1.MD.4 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Picture graphs with one picture per item and "how many more" questions belong in grade 1 | Common Core Standards Writing Team (2011), "Progressions for the CCSS, K-3 Categorical Data" | National Council of Teachers of Mathematics, "Principles and Standards", Pre-K to 2 data analysis | yes |
| Lining rows up makes the compare question visible | Common Core Standards Writing Team (2011), "Progressions for the CCSS, K-3 Categorical Data" | Common Core Standards Writing Team (2011), "Progressions for the CCSS, K-5 Operations and Algebraic Thinking", compare problems | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad r8, 2026-11-10): 5 cats, 8 dogs and 5 fish make 18 votes; dogs are 3 more than cats; 8 tallies are one bundle of five and 3; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 class and sheet; at 680x425 spotlight.
2. Votes are tallied in bundles of five. (1.MD.4)
3. Tallies become a picture graph with up to three rows. (1.MD.4)
4. Total, each and how-many-more questions are answered, with the line-up. (1.MD.4)
5. Every card is spoken; every control is 56 px or more.
6. Kids are labeled illustration; live votes stay on the device.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: still kids and jumps; no network requests.

## Open questions
None.

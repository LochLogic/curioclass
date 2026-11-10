# Question Jar

## One idea
On a classroom shelf sits a big glass jar of folded paper slips, and the teacher, Ms. Bell (made up, labeled "illustration"), invites the child to pull one out and decide how the class could find the answer; each slip is read aloud ("How many windows are in our room?", "How tall is the bean plant?", "What snack do most of us like?", "Which color is the best?") and the child drags it to a picture bin, tally marks to count it, a ruler to measure it, a speech bubble to ask people, or a heart for "just what I think", which no count can settle; reword rounds turn "Which color is the best?" into "Which color do most of us like?", and the slip hops from the heart to the speech bubble; first graders choose whether the answers will be numbers or words, and second graders plan when, where and whom to ask, then run the plan on a cartoon class of 20, where asking only at recess misses the 3 friends at the reading table, so only 17 answer and the count comes out wrong until the plan is fixed; at the end the child sees that the same topic can be an opinion or a question data can answer depending on the words, and that a plan that skips people gets a wrong count, so a child in kindergarten to grade 2 learns which questions data can answer, how to collect it, and who a plan can leave out.

## Not like
- wonder-wall (Grades K-2, live): look it up, ask an expert or try it. Here count, measure or ask people.
- me-vs-the-counter (K, spec): counting by hand against a computer. Here choosing how to collect.
- data-table-builder (4, spec): tables and charts. Here the question before the data.
- computer-builder (1, live): parts of a computer. Here data questions.

## Who and how
- Grades K-2, Computer Science, module "Asking With Data". Standards: EK-DAT-DI-09, EK-DAT-DC-08, E1-DAT-DI-09, E1-DAT-DC-08, E1-DAT-IM-10, E2-DAT-DI-09, E2-DAT-DC-08, E2-DAT-IM-10 (CSTA 2026 codes; the module line is quoted because the CSTA 2026 wording is not in data/standards: "Questions data can answer, ways to collect numbers and words, and who a plan leaves out").
- Format: sort. Driver: one student alone (tool.json `driver: "student"`). Every word is spoken; `Read` reads every slip. Controls 60 px or more.
- Twenty slips, eight reword slips, four plans (grade 1 picks answer type; grade 2 picks when, where and whom). Extra: Class jar (the teacher pulls slips on the projector and the class points to a bin). tool.json `modes: ["Jar", "Class jar"]`, `minutes: "10-15"`, `grades_label: "Grades K-2"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| EK-DAT-DI-09, E1-DAT-DI-09 | Sort slips; reword opinion slips | the heart bin; a slip hopping to the speech bubble | 2 |
| EK-DAT-DC-08, E1-DAT-DC-08 | Pick count, measure or ask; numbers or words | four bins; two answer cards | 2 |
| E2-DAT-DC-08, E2-DAT-DI-09 | Plan when, where, whom; read the count | the cartoon class answering | 3 |
| E1-DAT-IM-10, E2-DAT-IM-10 | Find who the plan missed; fix it | 17 of 20, then 20 of 20 | 4 |

## Screens and modes
Header (kit): title "Question Jar"; `Jar`, `Class jar`; `Read`, `Motion`, `Sound`, `Print`. Controls 60 px or more.

**On load and first tap.** A sunny classroom shelf with a big glass jar of folded slips, four picture bins below, and Ms. Bell kneeling beside it. The welcome is queued (`welcomeAfter: true`): "How could we find out? Tap the jar to pull a question." First hint: "Tap the jar."

**Sort (focus: the slip).** At 1366x768 the jar and slip sit center with bins along the bottom; at 680x425 the bins wrap to two rows. The slip unfolds and is read aloud. The child drags it to a bin; a right bin plays a soft chime and the slip tucks in; a wrong bin says why ("We can't count best. That's just what you think.") and the slip floats back.

**Reword.** A heart slip opens with two new wordings; the child taps the one that asking people can answer, and the slip hops to the speech bubble.

**Numbers or words (grade 1).** For an ask slip, the child picks "numbers" or "words" for the answers; a sample answer card shows each.

**Plan (grade 2).** Three picture choices: when (morning, recess, lunch), where (rug, playground, reading table), whom (everyone, only friends). `Ask` runs the plan on a cartoon class of 20; faces light as they answer. Missed friends stay gray, and the tally reads 17. The child fixes the plan and asks again.

**Who got left out (the aha).** Ms. Bell: "The words decide if data can answer. And if we skip friends, our count is wrong."

**The end.** A shelf of sorted slips and the fixed plan. `Print` prints a slip sheet.

**Class jar (extra).** Projector play.

## Content
- Twenty slips about the classroom, snacks, plants, pets and weather, all spoken.
- The cartoon class has varied looks and abilities, labeled "illustration"; no real names.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A slip can be moved until it tucks in; plans can be changed and run again.
- Keyboard: Tab to the jar, the slip, the four bins, reword choices, plan choices and Ask; Enter picks and drops.
- With Motion off slips appear in place and faces light at once.

## Look
- Accent `--brand` #8a4b0f honey brown (header, bins, buttons); gold #f4c542 (the slip in hand, a lit face); paper #fbf3ea; ink #2a1603; muted #5c5146.
- Contrast (WCAG 2.1, computed): white on brand 6.79:1; brand on paper 6.18:1; ink on paper 15.73:1; muted on paper 7.02:1; ink on gold 10.63:1.
- Never color alone: each bin has a picture and a spoken name; missed friends are gray and have a dashed outline.
- Different from this batch (attic rose, street-fair green, board blue, bamboo teal).

## Art
- People (illustrated): Ms. Bell and a cartoon class of 20 in varied looks and abilities, labeled "illustration" (Gemini, `people: true`, 3 sheets; cutout yes).
- Local FLUX (`scripts/localart.py`): the classroom shelf (1, 16:9), the jar (1, 1:1).
- Drawn in code: bins and their icons, slips, the tally.
About 5 images.

## Voice
Two bank voices, each unique in this batch: `curious-librarian` as Ms. Bell; `bright-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.slip + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `pull`: "Tap the jar."
- how `sort`: "Drag the slip to a bin."
- how `reword`: "Tap the question we can ask people."
- how `kind`: "Tap numbers or words."
- how `plan`: "Pick when, where and who, then tap Ask."
- event, whole, who got left out.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the slip deck, bins with reasons, the reword pairs, the plan runner over a fixed class of 20 with seeded who-is-where.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Sort | Drag every slip to one bin | Each slip has one right bin and a spoken reason. |
| Reword | Tap either wording | The opinion wording stays in the heart. |
| Plan | Keep the recess plan | The count stays at 17 until everyone answers. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `pull`; `sort`.
2. `reword`; `kind`.
3. `plan`.
4. Who got left out (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CSTA 2026 codes and the module line | data/modules.csv | data/standards/csta-2026-ids.txt | yes |
| Young children can pose questions that data can answer and plan simple collections | American Statistical Association, "GAISE II" (2020), Level A | National Council of Teachers of Mathematics (2000), "Principles and Standards for School Mathematics", PreK-2 data analysis | yes |
| Who is asked changes the answer (sampling bias) | American Statistical Association, "GAISE II" (2020) | Common Core Standards Writing Team (2011), "Progressions for the CCSS, K-3 Categorical Data" | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s22, 2026-11-10): 20 - 3 = 17; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 jar and bins in one view; at 680x425 bins in two rows.
2. Twenty slips are sorted into count, measure, ask or "just what I think", and opinion slips are reworded. (EK-DAT-DI-09, EK-DAT-DC-08, E1-DAT-DI-09, E1-DAT-DC-08)
3. Grade 2 plans are made and run, and the child says what the count can tell. (E2-DAT-DC-08, E2-DAT-DI-09)
4. A plan that misses friends is fixed and two plans are compared. (E1-DAT-IM-10, E2-DAT-IM-10)
5. Every word is spoken; the class is labeled illustration.
6. `Read` reads every slip; every control is 60 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: slips appear in place; no network requests.

## Open questions
- The CSTA 2026 wording is not in data/standards, so this and the other computer science specs in this round quote the module line (default used: module line from data/modules.csv; swap in the CSTA text when it is filed).
- Overlap with wonder-wall, which also sorts questions (default used: keep both; this one sorts by how data is collected and who it misses).

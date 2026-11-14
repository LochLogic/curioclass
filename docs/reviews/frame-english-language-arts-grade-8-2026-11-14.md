# Frame read: English Language Arts Grade 8, 2026-11-14

Reader: the curriculum expert (docs/agents/EXPERT.md), cold. Brief: docs/pipeline/briefs/frame-read.md, with the
caller's added checks (text picks, the original-text load, the writing split, five units, the 50-minute day,
repeated picks across frames and subjects, every lettered part, the 15 lessons in
docs/pipeline/briefs/frame-write.md).

## What I read

- docs/courses/english-language-arts-grade-8/frame.md in full; its row in data/plans/frames.csv (5 units, 160 days).
  No base text.
- The grade 8 rows of data/progressions/ela.csv, every column, and the grade 7 and grade 9 rows they take from and
  hand to.
- The neighbour frames: docs/courses/english-language-arts-grade-7/frame.md and
  docs/courses/english-language-arts-grade-9/frame.md (its picked-up rows, its rhetoric unit 5, its Ovid).
- The same-year frames: docs/courses/civics-government-and-civic-life/frame.md (social studies 8),
  docs/courses/science-grade-8/frame.md (unit 5). Every frame searched for the grade 8 picks (Banneker, the 1793
  fever, Jones and Allen, Carey, the 1906 food and drug law, Persephone, Anansi, the Declaration);
  docs/courses/english-language-arts-grade-4/frame.md for its myth set.
- docs/agents/lenses/ela.md, docs/RUBRIC-ELA.md, the grade 8 lines of data/standards/ccss-ela-standards-full.txt;
  docs/agents/decisions/DESK-ANSWERS.md (2026-11-12 and 2026-11-13); data/plans/later.csv and the progression-stitch
  review item 11 (RL.8.9 religious works).
- Gates: `python -X utf8 scripts/frame.py check english-language-arts-grade-8` (0 failures);
  `python -X utf8 scripts/plan.py check` (passes); `python -X utf8 scripts/stale.py check` (56 files, 0 failures).
  By hand: unit days 1 to 30, 31 to 58, 59 to 84, check 85 to 88, 89 to 120, check 121 to 124, 125 to 156, check
  157 to 160.
- Not opened, as told: the earlier grade 6 ELA planning and its reviews.

## Verdict

Five units is sound for grade 8: the units are long enough for a novella, a founding-era set, a research unit, a
myth unit with a staged play and a science-paired unit, and the year still has three checks. The frame's faults are
the band's shared one (rule 29, made sharper here because units 2 and 3 are built on primary sources, which the
frame itself asks the lead about), seven lettered parts narrowed to their grade 7 form, RL.8.10 and RI.8.10's
"independently" not placed, and an Anansi tale that grade 4 already reads. The days are set by unit, not by load:
unit 2 carries the hardest texts and the process argument in 28 days, unit 5 four rows in 32.

## Findings

### 1. Units 2 and 3 are built on primary sources that the frame calls paired

- **What is wrong.** The Base text bullet keeps rule 29. Unit 2's RI.8.6 and RI.8.9 work (Carey's account of the 1793
  fever against Jones and Allen's answer; Banneker's 1791 letter) and unit 3's reading of the 1906 law are anchors
  in function. For the lead 4 asks whether these older reads may stand; it is the band question. Unit 2 also reads
  the Declaration "for its rhetoric", grade 9 unit 5's lens.
- **Why it matters.** As in grades 6 and 7; and two grades reading the same document through the same lens.
- **Fix.** The band question to Cory (grade 6 read, finding 1). Change "for its rhetoric" to "for its word choice and
  for who answered it (RI.8.4, RI.8.6), with Banneker's letter as the answer"; add to the reason "The Declaration is
  read again in civics 8 unit 2 (days 16 to 30, for its ideas), ELA grade 10 (liberty set) and ELA grade 11 (its
  reasoning); grade 8 reads it in an excerpt, for word choice and response."
- LAYER frame. REPEAT new. Confidence: firm.

### 2. "Independently" in RL.8.10 and RI.8.10 is not placed

- **What is wrong.** RL.8.10 and RI.8.10 ask students, by the end of grade 8, to read and comprehend texts at the
  high end of the 6 to 8 band "independently and proficiently". The e8 reading-range row asks for independent
  checkpoints. The frame names the band and the support but no point where a student reads a grade-level text
  without support and is checked on it.
- **Why it matters.** This is the bar the band hands grade 9; without a placed check, nobody knows whether it was met.
- **Fix.** In unit 5 and check 3, add: "One unseen text at the top of the 925 to 1185 band, one literary in unit 5
  and one informational in check 3, read without support and scored apart from supported reading (RL.8.10 and
  RI.8.10, independently)."
- LAYER frame. REPEAT yes (lesson 4). Confidence: firm.

### 3. Seven lettered parts are narrowed to grade 7

- **What is wrong.** Checked against data/standards/ccss-ela-standards-full.txt:
  - W.8.3c: grade 8 adds "show the relationships among experiences and events".
  - W.8.2a: grade 8 asks to "introduce a topic clearly, previewing what is to follow", organize "into broader
    categories" and "include formatting (e.g., headings), graphics (e.g., charts, tables), and multimedia".
  - W.8.2b: "relevant, well-chosen facts"; the frame drops "well-chosen".
  - W.8.2c: "appropriate and varied transitions to create cohesion and clarify the relationships among ideas and
    concepts".
  - SL.8.1b: grade 8 adds "track progress toward specific goals and deadlines, and define individual roles as
    needed", with collegial discussions and decision-making.
  - W.8.6: adds "to interact and collaborate with others".
  - L.8.4c: general and specialized reference materials, not only a dictionary.
- **Fix.** Quote each in full where owned: W.8.2a to c in unit 3's research article (headings, one chart or table
  from the 1906 sources, a preview paragraph), W.8.3c in unit 1's process narrative, SL.8.1b in unit 3's research
  groups (decision-making and goals), W.8.6 in unit 3 (shared-draft comments; printed drafts on the paper path),
  L.8.4c in unit 2 (a glossary of eighteenth-century terms and a thesaurus task).
- LAYER frame. REPEAT yes (lesson 4). Confidence: firm.

### 4. The Anansi tale repeats grade 4

- **What is wrong.** Unit 4 reads an Anansi tale from Barker and Sinclair's West African Folk-Tales (1917); grade 4's
  myth set has an Anansi tale (Akan) beside Heracles and Momotaro.
- **Fix.** Replace with a Nasreddin Hodja tale from Henry D. Barnham's Tales of Nasr-ed-Din Khoja (1923; date and
  rights to confirm), a trickster figure students have not met in the course, retold in the unit's modern
  retelling; the sensitivity reader becomes a Turkish or Persian cultural reader.
- LAYER frame. REPEAT yes (lesson 11). Confidence: firm (the repeat); judgment call (the pick, settled below).

### 5. Days do not follow load

- **What is wrong.** Unit 2 (28 days) holds six rows, the year's hardest texts and a process argument; unit 5 (32
  days) holds four rows and no process piece.
- **Fix.** Move 4 days: unit 2 days 31 to 62 (32 days), unit 3 days 63 to 88, check 1 days 89 to 92, unit 4 days 93
  to 124, check 2 days 125 to 128, unit 5 days 129 to 156 (28 days). Science 8 unit 5 (genetics, days 106 to 130)
  still starts before ELA unit 5, so its bridge holds.
- LAYER frame. REPEAT yes (lesson 9). Confidence: likely.

### 6. The knowledge threads drift from their rows

- **What is wrong.** Thread 1 in the frame drops the Constitution and amendments the e8-reading-range row names, and
  its words ("republic, right, press") differ from the row's. Thread 2's words ("claim, trial, risk") differ from the
  row's "trait, gene, source, claim".
- **Fix.** With the grade 7 change (grade 7 read, finding 4): thread 1 words "citizen, democracy, right, press,
  amendment" in both the row and the frame, with the Constitution excerpt named in unit 2; thread 2 words
  "trait, gene, source, claim, trial" in both.
- LAYER progression. REPEAT yes (lesson 7). Confidence: firm.

### 7. One author for the literature, and the original-text count

- **What is wrong and fix.** As in grade 6, finding 4. For the lead says about 20 originals; the units name about
  17. Correct the count; add the voice line and the open-licence search; the writers question goes to Cory.
- LAYER frame. REPEAT new. Confidence: likely.

### 8. The weekly conference and the choice book

- **What is wrong and fix.** As in grade 6, finding 5.
- LAYER frame. REPEAT new. Confidence: likely.

### 9. No readiness checks are placed

- **What is wrong and fix.** As in grade 6, finding 6.
- LAYER frame. REPEAT yes (lesson 5). Confidence: firm.

### 10. A named social studies unit does not exist

- **What is wrong.** Unit 2's cross-subject line points to "social studies' Civil War units"; civics 8 has none by
  that name. The nearest is civics unit 6, rights over time (Civil War amendments, Dred Scott, days 77 to 95).
- **Fix.** "Civics 8 unit 2 (the Declaration, days 16 to 30, before) and unit 6 (rights over time, days 77 to 95,
  after)."
- LAYER frame. REPEAT yes (cross-subject calendar lines). Confidence: firm.

### 11. Two open questions are not carried

- **What is wrong.** (a) The RL.8.9 religious-works pick (progression-stitch item 11) is still Cory's, and the frame
  does not say how unit 4 stands until he answers. (b) The punctuation row's dash note is stale (grade 6 read,
  finding 10).
- **Fix.** Add to For the lead: "RL.8.9 (open with Cory, progression-stitch item 11): unit 4 uses myths only until he
  answers; no religious text is picked." And the grade 6 dash line for e8-pause-omission.
- LAYER process. REPEAT yes (lesson 15). Confidence: firm.

### 12. The novella needs a teacher note

- **What is wrong.** Unit 1's mystery turns on a letter from a parent living apart. No teacher note.
- **Fix.** "Some students live apart from a parent; no task asks students about their own family, and the
  narrative prompt offers a setting outside the home."
- LAYER frame. REPEAT yes (lesson 12). Confidence: likely.

### 13. The writing split

- **What is wrong.** The literary analysis essay is counted as informative; narrative is 25 percent, as in grades 6
  and 7.
- **Fix.** Count the analysis essay as informative and say so (RUBRIC-ELA files literary analysis under it), and add a
  one-sitting narrative in unit 4 ("retell one myth from a minor character's view", W.8.3), making 3, 3 and 3.
- LAYER frame. REPEAT new. Confidence: likely.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Five units | Long units fit the novella, the play and research; three checks remain | grade 8 frame (no change) |
| Nasreddin Hodja (Barnham) replaces Anansi | Grade 4 reads Anansi | grade 8 frame, unit 4 |
| Four days moved from unit 5 to unit 2 | Load | grade 8 frame, Days and units table |
| Declaration read for word choice and response | Grade 9 owns rhetoric | grade 8 frame, unit 2 |
| Unseen independent reads in unit 5 and check 3 | RL.8.10 and RI.8.10 | grade 8 frame |
| A one-sitting myth narrative in unit 4 | Narrative share | grade 8 frame, unit 4 |

## For Cory

- **Primary sources as anchors**: the band question (grade 6 read).
- **Who writes the literary originals**: the band question (grade 6 read).
- **RL.8.9 religious works**: already with him (progression-stitch item 11).

## For the lead items, judged

- **1 (five units):** sound.
- **2 (minutes):** sound, with in-class reading time (finding 8).
- **3 (the "Texts" column):** sound.
- **4 (older paired reads):** they anchor in function; Cory's call (finding 1).
- **5 (about 20 originals):** count corrected (finding 7).

## What is right and should not be touched

- The founding-era unit's pairing of Carey with Jones and Allen: a real point of view argument from two sides of one
  event (RI.8.6 and RI.8.9).
- The 1906 law research unit, a sharp topic with federal sources and a science and civics reach.
- The play staged twice for RL.8.7, the gene stories beside science 8 genetics, the handoff to grade 9's rows.

## Lens checklist

- Every lettered part in full: missed (findings 2 and 3).
- Text picks public domain or licensable: met (Barnham to confirm).
- Informational share: met if the primary sources count.
- Writing split: narrative low (finding 13).
- Picks not repeated: missed once (finding 4).
- Same-year alignment: met after finding 10.
- Readiness checks: missed (finding 9).
- Sensitivity reads: one teacher note missing (finding 12).
- Paper path: met.

## What I could not judge

- The publication date and edition of Barnham's Tales of Nasr-ed-Din Khoja (1923 from memory).
- The quality of texts not yet written.

## Sources

- data/standards/ccss-ela-standards-full.txt for every grade 8 lettered part quoted.
- The civics, science 8, grade 4 and grade 9 ELA frames for the calendar and repeats.
- From memory: Barnham's edition; the 1906 Pure Food and Drug Act.

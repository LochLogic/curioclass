# Frame fixes: Computer Science, grades 1 to 12 (2026-11-26)

The one fix pass of COURSE-RUN stage 3 for the twelve frames docs/courses/computer-science-grade-1 to -grade-12/frame.md,
from the expert reads (docs/reviews/frame-computer-science-grades-1-to-5-2026-11-25.md, "E1-5", and
frame-computer-science-grades-6-to-12-2026-11-25.md, "E6-12") and the twelve Codex reads
(frame-computer-science-grade-N-codex-2026-11-25.md, "C"). Model: frame-computer-science-kindergarten-fixes-2026-11-25.md;
the kindergarten frame was read for consistency and not edited. Cross-grade decisions were set once (below) and then
applied grade by grade.

## Gates

| Gate | Result |
|---|---|
| `python -X utf8 scripts/frame.py sync` | frames.csv 117 courses, calendar.csv 2119 rows |
| `python -X utf8 scripts/frame.py check computer-science-grade-N`, N = 1 to 12 | 0 failures each; grade 8's note "Seams does not name g10-network-of-networks" is gone |
| `python -X utf8 scripts/progression.py check computer-science` | 202 rows, 0 failures |
| `python -X utf8 scripts/stale.py check` | 121 files, 0 failures |
| `frame.py check` on the nine other frames that cite computer science units | 0 failures each (citations drift, listed in For the lead 9) |

Every frame: no em dashes; no UK spellings left except proper names (Open Government Licence, the base lesson title
"Analysing data"); every owned row placed once (scratchpad scripts); unit days plus check and respond days equal the
total.

## Cross-grade decisions

| # | Decision | Where it landed |
|---|---|---|
| D1 | Rule 32 (frame-write.md: "a course never assumes an optional course was taken"). Grades 7 to 11 gain grade 12's **Course order** bullet: a row from the year before opens as retrieval for students who took that course, and for those who did not as a ten-minute readiness check at rule 16's timing plus a short worked example inside the unit's first understanding day, never an added day. Ids an earlier elective begins and this course owns are taught from the start (the earlier use is a head start). Grade 6 needs none (K to 5 is taken by every child). | Grades 7 to 11, Course order bullets and Seams tables |
| D2 | Two-lesson course-level checks in grades 6 to 12: lesson one scores the unit before (standing for its end-of-unit assessment), lesson two samples earlier units; then the respond day. The extra day comes from the largest unit, or where the load notes say. Grade 10 already did this; its For the lead 2 now says it set the rule. | Grades 6, 7, 8, 9, 11, 12 (and 10's note) |
| D3 | Days outside the standards counted one way: "N of T teaching days", T = course days less end-of-unit assessment, check and respond days. | Grades 6 to 12 |
| D4 | Repeated examples, each studied once (swaps below). | Grades 4, 6, 9, 11, 12 |
| D5 | Device share in K to 3 stated against APPROACH Pacing and STANDARD "Devices and rooms": devices per class, device sessions, minutes per child at the keys, share away. | Grades 1 to 3 |
| D6 | "catalog id"; the Practices column named by its heading; "frame-write.md rule 16", never "(lesson 16)". | All twelve |

### Known fixes

| Fix | Result |
|---|---|
| Readiness paths, grades 7 to 11 | Applied (D1). Readiness days: grade 7 days 1, 10, 22, 33, 43, 54; grade 8 days 1, 12, 28, 41, 53; grade 9 days 1, 13, 25, 35, 43, 54; grade 10 days 1, 11, 20, 31, 41, 53; grade 11 days 1, 9, 22, 35, 47, 54. Grade 12 (already the model) moves to days 1, 11, 25, 46, 56. |
| Two-lesson checks, grades 6 to 12 | Applied (D2). Day layout under Days, below. |
| Grade 11 S1 share | Applied: unit 3's redraw folds into the revision session, every split session named; 4.5 of 50 teaching days, 9 percent, about half a day of room. Grade 12: 4.5 of 52, about 8.7 percent. Grade 7: 3 of 50, 6 percent. Grade 8: about 4 of 52, about 8 percent. Grades 6, 9, 10: none (0 of 50, 50, 49). |
| Grade 1 and 2 row changes | Applied in data/progressions/computer-science.csv, notes only, no id moved (list under Row changes). Frames' For the lead items now say they landed. |
| g10-design-hcd "classmates playing roles" | Applied: "User stand-ins are persona cards read aloud, never acted." |
| Hopper, Johnson, census | Applied, each studied once (Swaps). |
| Device share K to 3 | Applied (D5). Grade 1: 15 devices for 30, 5 of 32 sessions, about 40 minutes a child at the keys, about five sixths away. Grade 2: raised to 6 of 32 (unit 3 sessions 4 and 6 now on the editor), about 50 minutes a child, about four fifths away, no longer below grade 1. Grade 3: raised to 12 of 32 (unit 3 sessions 5 and 6 on the editor first, the day 20 solo build, day 21 respond, unit 4 session 2), about 100 minutes a child, 20 of 32 away; sessions the rows call unplugged stay unplugged. K to 2 (and grade 3 still short of "about half") sit below APPROACH: the proposed APPROACH line is For the lead 1. |

### Row changes (data/progressions/computer-science.csv, notes cells only)

Written through scripts/rows.py upsert (ROWS_PLANS pointed at data/, so the tool's byte-preserving write was used;
18 records changed, ids, order and every other column unchanged).

| Row | Change | From |
|---|---|---|
| g1-data-questions | Classroom questions (how many windows; which window has the best view), the school-need questions the frame uses, the game wording pair; never food, pets, homes or bodies | E1-5 S1, S2 |
| g1-keep-safe | Sign in and out of a paper login with a given pretend password, the teacher signs out, say no and tell a trusted adult; "practise" removed | E1-5 S1 |
| g1-responsible-use | Why each rule exists, the child's part, what happens to them and the class | E1-5 S1 |
| g1-patterns-ai | Systems made by people; library next-book suggestion; drawing tool | E1-5 S1 |
| g1-two-kinds-data, g2-ai-training-data, g4-ml-learning | "labeled" | E1-5 S1, m6 |
| g2-name-and-label | "labeled"; "a pet's name" to "the class plant's name" | E1-5 S1, own |
| g2-people-solve | Gains the familiar machines half (E2-SOC-HU-15) | E1-5 S1 |
| g2-data-questions | "which snack" to "which game does our class pick most for indoor recess" | E1-5 S2 |
| g2-benefits-harms | One pictured tool, no child asked about a home device | E1-5 S1 |
| g4-debug-increment | "practice" | E1-5 m6 |
| g4-table-tool | "a pet picture" to "a picture of a class object" | E1-5 m6 |
| g5-network-parts | Gains "switch" | E1-5 m4 |
| g5-variability | Duplicate sentence merged | E1-5 m7 |
| g9-simulate-data | "values in a stated range" for heights | E6-12 minor |
| g10-design-hcd | Persona cards read aloud, never acted | E6-12 M5 |
| g11-emerging-solution | "analyze" | own sweep |

### Swaps (D4)

| Example | Kept in | Swapped out |
|---|---|---|
| Grace Hopper | Grade 12 unit 5 (oral history) | Grade 4 unit 5: card dropped (the first programmers card carries "programs") |
| Katherine Johnson | Grade 12 unit 5 (her NASA account) | Grade 4 unit 5: card becomes Annie Easley (nasa.gov; from memory, checked at source); grade 6 unit 6's NACA pick names Dorothy Vaughan |
| Census | Grade 12 unit 2 (2020 disclosure avoidance) | Grade 6: the Social Security Administration's 1930s punched-card records and 1950s move to computers (ssa.gov; from memory, checked at source). Grade 9 unit 4: a city transit agency's fare-card trip records (from its published privacy policy, dated, agency not named to students); grade 9 year-end unseen case: library catalogs from card drawers to online search (loc.gov). Grade 9 sensitivity notes rewritten |
| COPPA | Grade 10 unit 6 | Grade 12 day 5: COPPA a one-minute retrieval card, FERPA (studentprivacy.ed.gov) the new law card; three laws stay three |
| Data center energy (national laboratory report) | Grade 8 unit 5 | Grade 11 unit 6 opens grade 8's debate as readiness and takes siting and water; grade 11 unit 5's mention became "the environmental cost of storing and processing data" |
| CARE Principles | Grades 7, 11, 12 | Grades 11 and 12 open it as retrieval and say what is new (11: data about a people used at scale to train AI; 12: judging a privacy method by its effect on a community's counts) |
| Phishing | Grades 8, 10, 11 | None: a spiral (expert's call) |

Grade 12's sentence now says grades 4 and 6 name neither Hopper nor Johnson (swapped 2026-11-26).

## Days after the pass

| Grade | Units (days) | Checks (course days) | Respond | Moved against other frames' citations |
|---|---|---|---|---|
| 1 | 6, 6, 8, 4, 4 | 13; 27 | 14; 28 | none |
| 2 | 6, 4, 8, 5, 5 | 11; 26 | 12; 27 | none |
| 3 | 6, 4, 9, 4, 5 | 11; 26 | 12; 27 | none |
| 4 | 6, 4, 9, 5, 6 | 10; 24 | 11; 25 | none |
| 5 | 5, 5, 7, 5, 6 | 18; 25 | 19; 26 | none (unit 3 stays weeks 11 to 17) |
| 6 | 15, 11, 10, 7, 7, 8 | 37-38 (week 19); 62-63 | 39; 64 | unit 1 ends one day earlier (day 15) |
| 7 | 10, 12, 8, 10, 11, 7 | 31-32 (week 16); 62-63 | 33; 64 | unit 6 days 55 to 61, still weeks 28 to 31 |
| 8 | 12, 13, 13, 12, 8 | 26-27 (weeks 13 and 14); 62-63 | 28; 64 | unit 3 days 29 to 41 (two days earlier), weeks 15 to 21 |
| 9 | 13, 12, 7, 8, 11, 7 | 33-34 (week 17); 62-63 | 35; 64 | unit 6 one day earlier, still weeks 28 to 31; unit 4 still weeks 18 to 22 |
| 10 | 11, 9, 8, 10, 12, 8 | 29-30 (week 15); 62-63 | 31; 64 | unit 3 days 21 to 28 (was 22 to 29), unit 4 days 32 to 41 (was 33 to 42) |
| 11 | 9, 13, 10, 12, 7, 7 | 33-34 (week 17); 62-63 | 35; 64 | unit 5 days 48 to 54, weeks 24 to 27 (was 25 to 28) |
| 12 | 11, 11, 21, 7, 8 | 23-24 (week 12); 54-55 (weeks 27, 28) | 25; 56 | unit 3 days 26 to 46, still weeks 13 to 23; unit 5 still weeks 29 to 32; year-end ends by week 28 (rule 31) |

## Findings

### Expert, grades 1 to 5

| # | Result | What changed, or why not |
|---|---|---|
| S1 | Applied | Rows above; grade 1 For the lead 2 and grade 2 For the lead 5 say landed. |
| S2 | Applied | g1 and g2 data questions are classroom ones; health-3 untouched (other subject). |
| M1 | Applied | D5. |
| M2 | Applied | Grade 1 day 13: the whole job as one picture strip with loose cards; the child marks the parts (lines between panels, or part cards with decoys), then orders; two look-fors. |
| M3 | Applied | Grade 3 day 20 scores E3-PRO-PD-04 from each child's five-minute solo build at the device (a credited four-card algorithm as blocks); the pair program is supporting evidence. Day 20 sits in core check week 20: a unit assessment, noted only. |
| M4 | Applied | Grade 4 day 24 budgeted at about 26 minutes; the team quiz is scored from its revised version at unit 4 session 5 (rule 19). |
| M5, J3 | Applied | Grade 5: session 3 models trace by hand and test one part; session 4 adds taking pieces out; reading the tool's message and a temporary output stay short techniques used when a bug calls for them. |
| M6 | Applied | Grade 5 day 18: choose one of three credited segments, place it, change one value, test, credit, one line on what it now does. |
| m1, m2 | Applied | D6 in grades 1 to 5. K and STANDARD.md keep "catalogue" and the column count: For the lead 3. |
| m3 | Applied | Grade 4 Picked up gains g3-benefits-risks to g4-history-limits (unit 5), with a grade 3 unit column. |
| m4, m6, m7 | Applied | Rows above. |
| m5 | Applied | Grade 5 Devices: about 12 of 22 teaching sessions hold device work, several in part, a little under half the teaching time. |
| m8 | Applied | Grade 3: "making a second variable with a near-same name makes a second, separate box". |
| J1 | Closed | Grade 3 For the lead 4 closed on the expert's reading; STANDARD.md line is For the lead 2. |
| J2 | Applied | Grade 3 moved toward half (D5). |
| J4 | Kept | Part met on paper is right by the boundaries. Grade 4 also marks E4-DAT-DI-10 part met on paper (C4-1). |

### Expert, grades 6 to 12

| # | Result | What changed, or why not |
|---|---|---|
| S1 | Applied | D1. Grade 7 and 8 add: where a school left out grade 7 unit 4 or grade 6 unit 4, the readiness check covers the whole class. |
| S2 | Applied | D3, counts above. |
| S3 | Applied | D2. Grade 9 took its extra days from units 4 and 5, not unit 1: taking from units 1 to 3 would push the mid-year check into Biology's week 16. Grade 8 took them from units 2 and 1; grade 7 from units 2 and 5; grade 6 from units 1 and 6; grade 11 from units 2 and 3; grade 12 from units 3 and 4. Check items carry minute budgets. |
| M1 | Applied | Swaps. |
| M2 | Applied | Swaps; grade 9's unseen case is new. |
| M3 | Applied | Swaps. |
| M4 | Applied | Stale notes rewritten in grades 6, 7, 8, 9, 11, 12; grade 9 and 12 seam tables cite grade 8 and grade 11 unit numbers. |
| M5 | Applied | Row above; grade 10 For the lead says landed. |
| M6 | Applied | Grade 8 Handed on gains g8-network-failure to g10-network-of-networks (grade 10 unit 3). |
| M7 | Applied | Grade 12: grade 9 readiness check in the last ten minutes of day 22; day 25 holds only the grade 11 items. |
| M8 | Applied | Grade 10 unit 5 (12 days) ends on its respond day: lesson 10 scored, 11 portfolio, 12 respond; feedback a lesson after the draft; the day came from unit 1 (old lessons 4 and 5 merged). |
| Minor: catalogue, "(lesson N)" | Applied | D6. |
| Minor: grade 9 For the lead numbering | Applied | 1 to 6. |
| Minor: random-pick wording | Applied | "on some runs, though not on average". |
| Minor: g7-pick-approach | Applied | The row (attendance) is the contract: grade 7 session 34 predicts tomorrow's attendance from invented whole-class totals. |
| Minor: grade 8 day 42 attribution | Applied | Dropped. |
| Minor: session numbering | Applied in 7 to 12, kept in 6 | Grades 7 to 12 number by course day (grade 9 converted). Grade 6 keeps per-unit numbering like K to 5; the band-wide call is For the lead 8. |
| Minor: g9-simulate-data | Applied | Row above. |
| Minor: Washington recycling law | Applied | Grade 11 marks it from memory, checked at source by the scope writer (state ecology E-Cycle pages). |
| J: social studies leans | Applied | One-line "by course order" bridge notes in grades 8, 10, 12: the unit teaches the civics it needs. None formal. |
| J: grade 11 unit 5 load | Applied | The hiring case carries both IM-10 and DAT-IM-27; the frame says so. |
| J: outside-standards days, grades 7 and 8 | Kept | Both under the line, now counted by teaching days. |

### Codex reads

| Grade | # | Result | What changed, or why not |
|---|---|---|---|
| 1 | 1 | Applied | Mid-year as M2; year-end E1-DAT-DC-08 uses two cube towers: count, look, record both, answer "alike and different?" with both; three look-fors. |
| 1 | 2 | Applied | Evidence bullet budgets spoken items (one per child in five groups, about 20 seconds); a second spoken look-for is heard earlier on an unseen item after first teaching; partner talk alone never counts. |
| 1 | 3 | Applied | Unit 2 scenes marked invented for practice, each real use pictured gets a dated teacher source; unit 5 one named Computer History Museum timeline entry per activity and two dated views. |
| 1 | 4 | Applied | Clash list corrected (week 13 library; week 27 health, media arts, theater). |
| 2 | 1 | Applied | Year-end E2-DAT-DC-08 adds which column counts and which describes, plus a comparison; E2-PRO-RD-06 gains a block look-for heard in session 5. |
| 2 | 2 | Applied | Same timing rule as grade 1, item by item per unit. |
| 2 | 3 | Applied | Voice and sound-level input removed; a key press to a letter, a button to a tone; no microphone. |
| 2 | 4 | Applied | Unit 5 exact source pages and two dated views; timeline marks documented uses only. |
| 2 | 5 | Applied | Source map lists Events and actions lesson 4 as left out, with reason. |
| 2 | 6 | Applied | Calendar fallback keeps every respond session. |
| 3 | 1 | Applied | As E M3 (day 20, the expert's day, over Codex's session 5). |
| 3 | 2 | Applied | Society claims tied to two dated views; invented scenes marked; timelines never show older ways ending. |
| 3 | 3 | Applied | Fallback rewritten; unit 5's respond day never folded. |
| 3 | 4 | Applied | As E m8; one score variable with a known start. |
| 3 | 5 | Applied | Year-end samples units 1 and 3 with a time budget; science grade 3 meets about four days a week; dance added to week 26's clash list. |
| 4 | 1 | Applied | E4-DAT-DI-10 report written in the table tool's report view beside the chart; unit 3 session 3 now a device session (10 of 22); part met on paper. |
| 4 | 2 | Applied | The quiz starts from a supplied shell with its score logic; students trace it, do not design it (grade 5's). |
| 4 | 3 | Applied | Connections compared on distance, speed, convenience and trust, with a "say no to an unknown network" card; wrong labels added then corrected. Row note text proposed (For the lead 6). |
| 4 | 4 | Applied | Day 5 follows steps, applies a safe fix and checks it; day 24 find, fix, retest; bugs across sequence, event, repeat and choice. |
| 4 | 5, 6, 7 | Applied | As M4, m3, m1/m2/m6. |
| 5 | 1 | Applied | Session 7 scored on the revised project with an individual record; a short supplied-shell modification where a component lacks set, update, compare. |
| 5 | 2 | Applied | Day 25 adds a device rotation collecting fictional case-card answers through the form; variability item adds a relationship. |
| 5 | 3 | Applied | E5-PRO-VD-06 part met without a device; full coverage is building or changing variable behavior in the editor and testing it. Row note proposed. |
| 5 | 4 | Applied | Day 18 and day 25 budgets with rotations; model scored in unit 4 session 4; duplicate items removed. |
| 5 | 5 | Applied | Unit 4 session 3 opens with a teacher-modeled train and test cycle. |
| 5 | 6, 7 | Applied | As M5; math five days a week, science about four; rule references fixed. |
| 6 | 1 | Applied | Mid-year opens a supplied file's properties on the device (printed panel part met); unit 4 end adds choose inputs, run, record, revise; year-end history item from two eras. |
| 6 | 2 | Applied in part | Same day totals as Codex; folded different sessions, keeping unit 1's pair build (the only individual make before the team program). |
| 6 | 3 | Applied | Unit 1 sessions 3 and 5, unit 3 session 6 relabeled Understanding. |
| 6 | 4 | Applied | Source map corrected (Part II lesson 7 mapped, 8 and 9 out; spreadsheet lessons; network lesson 6 out, so unit 5 session 4 is ours). |
| 6 | 5 | Applied | For the lead 3 rewritten; ADOPTION-BAR-SUBJECTS sentence proposed (For the lead 6). |
| 6 | 6 | Applied | Unit 2 question "test it for given inputs". |
| 7 | 1, 4 | Applied | D1, D2. |
| 7 | 2 | Applied | MS-PRO-PD-13 scored inside the product (sessions 17 and 18: a call from a supplied reference entry, a supplied error fixed); day 21's task supplementary. |
| 7 | 3 | Applied | Session 13 labeled Understanding. |
| 7 | 5 | Applied | Year 9 sequences source map: lessons 2 and 4 kept, 1, 3, 5, 6 left out with reasons. |
| 7 | 6, 7, 8 | Applied | Stale lines removed; 19 rows, about 3.4 sessions a row; D6. |
| 8 | 1, 3, 7 | Applied | D1, D2 (with Codex's budgets), D3. |
| 8 | 2 | Applied | Unit 3 adds unfamiliar-input prediction, summary checklist items, presentation choices and the model-results consequence; unit 3 grows to 13 days. |
| 8 | 4 | Applied | Cybersecurity source map: lessons 2, 4 (malware only), 5 used; 1, 3, 6 left out with reasons. |
| 8 | 5, 6, 8 | Applied | As M6, M4, D6. |
| 8 | For Cory (MS-ALG-PS-05) | Raised | Question 5. |
| 9 | 1, 5, 8 | Applied | D1, D2, D6. |
| 9 | 2 | Rejected, raised | Days that begin an id a later grade owns teach this subject's own CSTA ids, so they are not outside the standards; about 7 such days listed with Codex's fallback (about 4.75 of 50) in grade 9 For the lead 5. For the lead 5 here. |
| 9 | 3 | Applied | Days 57 and 58 require one societal and one environmental point from the sources; rubric look-fors. |
| 9 | 4 | Applied | Mid-year gives pseudocode with any random operation shown; classify from the logic, not matching outputs. |
| 9 | 6, 7 | Applied | Day kinds relabeled; seams cite grade 8 units. |
| 9 | For Cory (entry with no programming) | Raised | Question 6. |
| 10 | 1, 3 | Applied | D1, rows. |
| 10 | 2 | Applied | Day 61 an unseen HU-43 sitting. |
| 10 | 4 | Applied | Unit 3 lesson 8 uses a dated federal cybercrime public service announcement; one agency page is a browser check (For the lead 7). |
| 10 | 5 | Applied | Stale lead note fixed; test-table origin includes grade 9 unit 2. |
| 11 | 1 to 5 | Applied | D1, D3 (Codex 3's count adapted to 4.5 of 50); unit 4 splits data into training, comparison and a sealed final test; check budgets in minutes; unit 2 "second-largest distinct value" spec; CARE address corrected. |
| 12 | 1 | Applied | A student with no model of their own uses the supplied model and S1-AIN-HR-09 is recorded part met; HS-ALG-PS-05 stays fully claimed. |
| 12 | 2 | Applied | Each student's own refinement scored from the record handed in at the end of unit 4 day 7. |
| 12 | 3 | Applied | Short form keeps the portfolio evidence and two field cards, with minute budgets. |
| 12 | 4, 5, 6 | Applied | D2, M7, S2. |
| 12 | 7 | To the lead | For the lead 6. |
| 12 | Sources | Applied | Federal accessibility rule summary dated with its compliance dates checked at source; CARE address; the Smithsonian Hopper oral history is a browser check (403); the scope writer picks Johnson's specific first-person account. |

## For the lead

1. **APPROACH.md Pacing,** after the device-share sentence (carried in grade 1 For the lead 6; grades 2 and 3 point to
   it): "K to 3 may sit below this share when the unplugged form teaches the row as well; each frame states its share."
   With a DESK-ANSWERS line. Pick: adopt. Grade 3 now reaches 12 of 32 sessions, still under "about half".
2. **STANDARD.md "Devices and rooms",** after the device-only id list: "E3-PRO-PD-04 is device-only too, because its
   boundary places the code in a block-based environment; E2-PRO-PD-04 is met in full on paper, because its boundary
   counts a robot coded from an algorithm of arrows, which a partner acting on the floor grid from block cards is."
3. **"catalogue" and column counts** remain in STANDARD.md and the kindergarten frame (not mine to edit): "catalog id";
   name the column "the Practices and concept areas column".
4. **frame-write.md rule 32,** after its first sentence: "Where the subject's courses are electives (computer science
   grades 6 to 12), a row from the course the year before opens as a retrieval task for students who took it, and as a
   ten-minute readiness check at rule 16's timing, with a short worked example in the unit's first understanding day,
   for students who did not; the frame says so in a Course order bullet." And one check rule for grades 6 to 12 in
   the After-core section: "A course-level check in a two-a-week course takes two lessons: the first scores the unit
   it follows, the second samples earlier units; the respond day follows." DESK-ANSWERS lines for both.
5. **C1 and begun ids** (grade 9 For the lead 5): proposed for frame-write.md rule 18 or the C1 text: "Days that begin
   an id a later course in the same subject owns count as days inside the standards." Pick: adopt. If not, grade 9
   follows Codex's fallback (about 4.75 of 50) and the same reading reaches other grades' begun ids.
6. **Shared docs proposed by the frames:** docs/ADOPTION-BAR-SUBJECTS.md lines 20 and 21 still say no approach page
   exists (grade 6 For the lead 8, grade 12 For the lead 6; replacement text in both); row note texts proposed for
   g4-wired-wireless, g4-ml-learning, g4-data-explain, g4-team-document (grade 4 For the lead 6), g5-variables-use,
   g5-systematic-debug (grade 5 For the lead 5), and optional g11-build-ml-model and g12-evaluate-ai-output wordings
   (in the frames). Not applied here: they go past the rows the task named.
7. **docs/APPROACH-SOURCES.md additions** listed in each frame's For the lead (grades 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
   item 4, 11 item 5, 12 item 4): exact archive lesson pages, NASA's Annie Easley and Dorothy Vaughan pages, ssa.gov
   history, loc.gov, the FERPA page; Hopper and Johnson pages leave grade 4's list.
8. **Browser checks** (refused automated reads, open in Claude in Chrome): the NFB braille museum page (grade 2), the
   CISA phishing page (grades 8, 10), the ASPE telehealth page (grade 8), the Smithsonian Hopper oral history PDF
   (grade 12). Session numbering by course day across grades 6 to 12 is grade 6 For the lead 9 (grade 6 alone keeps
   per-unit numbering).
9. **Citations in other frames that drifted** (no gate failure; I did not edit them): career-pathways-grades-9-to-12
   line 173 cites grade 10 unit 3 as course days 22 to 29 and unit 4 as 33 to 42 (now 21 to 28 and 32 to 41);
   social-and-emotional-learning-grades-9-to-12 lines 278 and 296 cite grade 11 unit 5 at weeks 25 to 28 (now 24 to
   27); career-exploration-grades-6-to-8 line 126 cites grade 8 unit 3 without days (now days 29 to 41, weeks 15 to
   21; its "if later" line still holds).
10. **Calendar pass** (after-core clashes, not moved): grade 1 weeks 13 (library) and 27 (health, media arts,
    theater); grade 2 weeks 11 and 26; grade 3 week 26 (with dance); grade 8 mid-year respond day on school day 70
    (math's check day, a respond day, not a check); grade 9 week 17 shares with ELD and its respond day sits in World
    History I's week 18; grade 6 to 12 year-end checks in week 32 with most courses.
11. **A new evidence rule in grades 1 to 3:** spoken look-fors may be heard in earlier teaching sessions on unseen
    items after first teaching. The kindergarten frame lacks it; consider it for kindergarten and for APPROACH "The
    form of daily evidence".
12. The agents and I ran no git. I wrote 18 progression notes cells (a shared file, done because the task asked).

## Questions for Cory

1. **The training tool (scope).** Grades 4 to 6 lean on a small tool that trains a sorter; until it exists
   E5-ALG-ML-02 is part met for every child. Pick: build it, small and on the device, as one mode of our own editor.
2. **The K to 2 picture-block mode (scope).** Icon blocks with an event block and a counted repeat whose step-through
   counts each pass. Pick: build it as a mode of our own editor; the paper path meets every K to 2 id meanwhile.
3. **The archived Teach Computing edition and its download.** Confirm the archived edition (2023, no longer
   maintained) as the fixed K to 8 partial base, and say yes to downloading it into the source store (sign-in
   unknown until tried). Pick: yes to both; every title-only mapping stays provisional until then.
4. **NOAA download (grade 11 unit 3).** The Climate Data Online station extract is a download. Pick: yes; until then
   the unit uses an extract invented for practice.
5. **MS-ALG-PS-05 with saved outputs (grade 8).** Can a school with no approved tool meet it in full with Curio
   Class's saved, dated, labeled outputs that each student validates? Pick: keep "part met" until you decide; the
   boundary supports the change.
6. **Grade 9 entry with no programming at all.** Pick: the scope budgets the bridge tasks on days 1 to 5 and reports
   whether they are enough; then you choose an entry provision or a stated prerequisite.
7. **Grade 12 model build (S1-AIN-HR-09).** Pick: no added build day; part met for a student without grade 11's model
   (a build would use the room left under C1).
8. **Table tool report view (grade 4).** Pick: yes, a small mode inside the table tool.

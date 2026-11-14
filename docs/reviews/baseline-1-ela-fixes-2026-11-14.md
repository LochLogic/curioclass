# Baseline 1: ELA fixes, 2026-11-14

The ELA fixer's record for baseline 1. Inputs: docs/reviews/baseline-1-ela-2026-11-14.md (findings 1 to 10 and its
"Settled by the expert" table), ELA's slice of docs/reviews/baseline-1-structure-2026-11-14.md and
docs/reviews/baseline-1-codex-2026-11-14.md, and Cory's Desk answers of 2026-11-14 (BASELINE rule 5: no outside
human reader anywhere). Files changed: the 13 ELA frames (docs/courses/english-language-arts-{kindergarten,
grade-1..12}/frame.md) and data/progressions/ela.csv. No script, brief, glossary or path doc was touched.

## Gates

- `scripts/frame.py check`: all 13 ELA frames, 0 failures, and no notes left beyond the day count (the lettered
  parts, check-table shape, outside-reader wording and grade 8 cross-subject notes are all cleared).
- `scripts/frame.py sync` run; frames.csv and calendar.csv are current.
- `scripts/progression.py check ela`: 374 rows, 0 failures.
- `scripts/stale.py check`: 56 files, 0 failures.
- `scripts/plan.py check`: 0 failures (its notes belong to other subjects' plans).
- No em dashes in any ELA frame. Line endings kept as CRLF in every frame and in ela.csv.

## Applied

### ELA review findings

| # | Finding | File | What changed |
|---|---|---|---|
| 1 | The Declaration's lenses repeat | grade 10, grade 12, ela.csv | Grade 10 unit 6 is now "Liberty, word by word, 1776 to 1941", with the question "What did 'liberty' mean in each document, and how did each writer's words change what it means?" The unit cell now teaches the concept built word by word. The seam line gives each grade its own lens (grade 8 who answered it, grade 10 what liberty means, grade 11 its reasoning, grade 12 the courts plus Walker). Grade 12 unit 4 is now "The 1920s: the American dream and its price", with the question "What does the American dream cost the people who chase it in these 1920s texts, and who pays?" The ela.csv rows e10-ri-seminal-documents and e12-lit-american-modern were changed to match. |
| 2 | The grade 5 to 6 step goes backwards; grade 7 repeats grade 6 | grades 6, 7, 8 | Novellas lengthened: grade 6 to about 25,000 to 30,000 words, grade 7 to 30,000 to 35,000, grade 8 to 35,000 to 45,000. The extra pages go to home reading. Typing is now two pages in grade 6 unit 1 (the readiness check), three in one sitting by grade 6 unit 3, and three from unit 1 in grades 7 and 8, so the climb is in what the pages hold. The For the lead text items are marked settled: written in house, read by the text agent. |
| 3 | Water and drought crowd grades 5 to 7; the ranch story appears twice | grade 7, grade 5, ela.csv | Grade 7 unit 1 is now "The salmon year". The novella follows a present-day Klamath fishing family in the last year before the dams came down. The family is not written as Karuk or Yurok, and the Tribes speak in their own published words in unit 6. The paired texts are federal fisheries and river-flow pages. Unit 2's Dust Bowl is now the year's one drought unit, and grade 5 keeps the band's one ranch-family drought story. The grade 5 For the lead note gives the reason. In ela.csv, e7-story-elements-interact's "a ranch in drought" is now "a fishing family's river". |
| 4 | Gene editing is taught from the same pages in grades 8 and 10 | grade 10 | The unit 2 original essay is now about growing tissues and organs in the lab, and what it means to "make" living things. The teacher note was changed to match. The seam line says gene editing in the news is grade 8's. For the lead 8 names the lab-grown tissue essay. |
| 5 | Literary analysis is filed two ways | grades 8, 10 | Grade 8: "counted as informative, since unit 1 teaches it on W.8.2". Grade 10: "(taught on W.9-10.9, defending a claim)". |
| 6 | The 6 to 8 checks follow two rules | grades 7, 8 | Grades 7 and 8 now use grade 6's rule. Units not followed by a check end in their own end-of-unit assessment. Where a check follows a unit, the check is that unit's end-of-unit assessment, on the unit's topic but never on a text the unit read. Grade 8 says why check 1 waits for unit 3. |
| 7 | The grade 6 and 7 year-end argument items are the same | grades 6, 7 | Grade 6 check 3 now asks for claim, reasons and evidence (W.6.1a, b). Grade 7 check 3 now asks for an argument that acknowledges an opposing claim and cites credible sources (W.7.1a, b). |
| 8 | The screens take 2, 1 and 0 days in grades 3 to 5 | grades 3, 4, 5 | Each Days bullet now gives its reason. Grade 3 is the first year of the long-word sequence. Grade 4 adds only the writing sample. Grade 5 runs the screens one to one in the skills block and uses unit 1's first exit ticket as the writing sample, so no day is added. |
| 9 | Word list size is stated two ways | grades 3 to 12 | One rate everywhere: "about 8 to 10 words a week from the unit's texts, met before, during and after reading", plus the student's own word log from grade 9. The scope and sequence sets each list. |
| 10 | Grade 6's fluency flags are not followed up | grades 7, 8 | Added a Fluency bullet. The one-minute oral reading check is repeated in the first two weeks for students flagged the year before and for new students, with a weekly partner reread. No rate is shown to students. |

### Desk answers and BASELINE rule 5 (all 13 frames)

- **Outside readers.** Every community reader, cultural reader, qualified teacher reader and counselling reader is replaced:
  - Content reads go to the sensitivity agent (docs/pipeline/briefs/sensitivity-read.md).
  - Original texts go to the text agent.
  - Every Sensitivity reads bullet now names the communities and the sources the agent studies first. Examples:
    - grade 9: Yankton Sioux Tribe and Dakota sources for Zitkala-Ša, and safe-messaging guidance for Romeo and Juliet;
    - grade 10: Indian, Filipino, South African, Tswana and Ndebele sources for unit 3, and the Nez Perce Tribe's own history for unit 6;
    - grade 11: Mohegan and Pequot sources for Occom and Apess, Black-led sources for Douglass, and Jewish, Chinese American and Italian American accounts for Riis;
    - grade 12: Irish historians for Swift, Black-led and Jewish-led sources for unit 4, and Colville sources for Mourning Dove.
  - The matching unit cells now point to that study.
  - Every "who reads, and any pay, is Cory's" line is gone.
  - Pilot teachers and students are left as they were.
  - Grade 12's adult panel still comes through the school.
- **Time a day.** Every frame's time item is marked "Settled 2026-11-14", as the frames have it.
- **Recent long text in grade 9.** Marked settled ("grade 9's long text as planned").
- **Primary sources in grades 6 to 8.** Marked settled: they may anchor. Grades 6 to 8 keep them paired by choice.
- **Personal finance.** One light touch inside an existing day (grade 8 unit 5: what a product costs against what it promises, SL.8.2). No day added.

### Structure review, ELA slice

- **Finding 1 (end-of-unit assessment).**
  - Every frame now says each unit opens with a readiness check and closes with its end-of-unit assessment inside its days.
  - K to 5 say which base-unit assessments become mid-unit assessments and which become the end-of-unit assessment.
  - Each K to 5 source map gained an Assessments paragraph.
- **Finding 5 (time a day).** Marked settled, as above.
- **Finding 8 (standards in full).**
  - Every lettered part is now named by full code in its unit row.
  - In grades 6 to 10 and 12, short forms like "(b)" and "4a to 4d" were rewritten in full.
  - Where K to 5 place a part in another unit, the unit row now says which unit teaches it.
- **Finding 10 (one thing, one name).**
  - "Exit question", "exit answer", "grammar opener", "cumulative check" and "course check" became the glossary words: exit ticket, warm-up, course-level check.
  - "Stretch" became "run of units".
- **Finding 11 (per-unit pieces).** K to 2 got one record sheet, family note and sub-ready day per base unit, three a unit and 12 a year.
- **Check-table shape.** Every Course-level checks section is now in the one table shape (Check, After unit, Check days, Respond days, What it checks):
  - K to 2 came from bullets;
  - grades 3 to 12 came from the older tables.
  - Day totals are unchanged.
- **Cross-subject.** Grade 8 names its earlier-year lean on ss7-greek-myth (e8-myth-made-new, unit 4) with a local bridge.

### Codex review, ELA slice

- **Finding 4 (review-role policy reaches the course contracts).** Done through the reader replacement above, in every frame, including grades 4 and 9.
- **Finding 5 (unit ending).** The frames now state the end-of-unit assessment as above.

## Not applied

| Item | Why |
|---|---|
| ELA finding 5's line for docs/RUBRIC-ELA.md (where literary analysis is filed) | A shared doc that holds Cory's bar; the frames now say how each grade counts it. Left for the lead. |
| Structure findings 4, 6 and 9 (checks stacking across subjects, day and week definitions, course ids) | The brief says do nothing in frames for these; they belong to the structure fixer. |
| Codex wording "teaching days" against "course days" | A glossary call, left to the structure fixer. |
| ELA finding 3's "drought in unit 1" phrase in e7-reading-range | The phrase is not in that row. The ranch phrase the finding points to was in e7-story-elements-interact and is changed. |
| Grade 8 For the lead 6 (RL.8.9 and religious works) | Already open with Cory from the progression stitch (item 11). No Desk answer was found, so it stays open as written. Not a new question. |
| Grades 11 and 12 For the lead "ELA check set (Cory)" and the optional volunteer recording | Existing open items, not from this review, left as written. |
| Grade 10 For the lead 1 (one joint research product with World History II) | An existing scope pick in the frame, not raised by this review, left as written. |

## Settled

| Question | Settled | Why |
|---|---|---|
| Which topic replaces grade 7's ranch drought | A Klamath fishing family before the dam removal | It ties unit 1 to unit 6's dam argument and leaves the Dust Bowl as the one drought unit. The family is not written as Native, so no Tribal voice is invented. |
| Novella lengths, grades 6 to 8 | About 25,000 to 30,000, then 30,000 to 35,000, then 35,000 to 45,000 words | Cory's Desk answer: written in house, read by the text agent. The climb now passes grade 5's whole texts. |
| Typing climb, grades 6 to 8 | Two pages, then three by grade 6 unit 3, then three all year in grades 7 and 8 | It ends at the standard's three pages. The climb after that is in what the pages hold. |
| Word list rate | About 8 to 10 words a week, grades 3 to 12 | One stated rate. The scope and sequence sets each list. |
| End-of-unit rule where a check follows | The check is that unit's end-of-unit assessment | Grade 6's rule, now in grades 7 and 8. It means no class is tested twice in a week. |
| Personal finance | One touch in grade 8 unit 5, inside an existing day | Settled rule: light touches only, no added days. |
| Primary sources in grades 6 to 8 | They may anchor; these frames keep them paired | Cory's answer allows it. Pairing keeps the standards taught on the anchors first. |
| Time a day | As the frames have it | Settled by Cory, 2026-11-14. |
| Grade 3 to 5 screen days | 2, 1 and 0 days, each with its reason | The sequences start in grade 3. Grade 5 folds the screens into the skills block. |

## For Cory

None. Every item here is settled or already open (RL.8.9, the ELA check set), and nothing new was raised.

# Section refine: english-language-arts-grade-4 unit 4, u04-1 to u04-7

Date: 2026-11-27. I rebuilt the skeletons with `section_skeleton.py english-language-arts-grade-4 u4` and did not edit them. All seven were written. The first run exited 1, and a second run wrote all seven with no error. I read all seven plans cold against the section plan bar, after the answer-key read of the same unit (docs/reviews/english-language-arts-grade-4/answer-key-english-language-arts-grade-4-u04-2026-11-27.md). The fixes from both jobs are reconciled in the plans, ledger, shared pieces and data rows. The prep notes build/sections/prep/english-language-arts-grade-4/u04-<n>.md do not exist, so no fault comes from them.

## Faults

| File | Fault | Fix or rejected | Stage |
|---|---|---|---|
| u04-2, field 3 | The X125-pronoun and X125-adverb asks could be answered by copying a sentence from the printed reserved ending. | The Ask lines and print rows now say "Write a new sentence about Maya / about the desk...". The keys are new sentences that end "A sentence copied from the ending is not yet." They match items.csv word for word. | write |
| u04-3, field 3 | The X131-adverb ask could be answered by copying "the shelf where she had found the envelope". | The Ask, Key and print row now ask for a new sentence and accept another fitting one. | write |
| u04-3, field 3 probe tables | The 134 word "reconstruct" was used in the unit 3 P119 probe, and the 135 word "retractable" repeats the unit 2 u02-1 probe word "retraction". Both broke rule 4 across units. | P134-spell-1 and parts-1 now use abrupt (ab + rupt). P135-spell-2 and parts-2 now use adjustable (adjust + able). Each spelling row states the meaning and gives a teacher sentence. The wrongs are abrubt (X), abr + upt (R), adjustabel (X) and adjus + table (R). | write |
| u04-4, D3 cold solution | The whose key restated the joined fact as its own main clause. | Now "Maya is the one whose notes her brother reads." | unit plan |
| u04-6, X149-support | The Key credited one of the two card facts that support sharing. | Adds "Also accept that it labels the garden report, so visitors can check the source." | write |
| Ledger, u04-3 case row (134 and 135 probes) | The note named the old pairs and claimed checks against the lower grades only. | Fixed with `ledger.py note`, day blank. It names abrupt/extractable and postscript/adjustable, says why each word was replaced, and records the check against grades K to 3 and grade 4 units 2 and 3. | write |
| u04-7, field 7 | "One 45-second contribution/reply each" next to the day 155 "two 45-second contributions". | Rejected: a contribution plus a reply is two turns. Five children times two 45-second turns is 7.5 minutes in both places. | write |

Checked with no fault found:
- All 37 days have a "Student goal" line in student words and a kind from the linked facts.
- Each day's parts add to 90 minutes.
- Every "Wrong (X)" letter is in the s04 register (A to AJ), and each listed wrong has exactly one letter.
- Every `Ask:` line and print override row matches its items.csv stem and day. My sync script prints no differences.
- Each stem asks one thing, "Shape:" lines are present, and no stem prints its key.
- RI.4.9 items have two texts: F1-integrate (A Composting Place and Reporting Local Work) and X144 (Growing Food Together and Organizing a Garden).
- No spelling check word appears on a same-day punctuation or editing exit slip. On days 134 and 135, every dictation line is collected before the parts card prints the words.
- This unit has no separate probe recording sheet. The field 3 tables are the sheets, and no shared piece prints a probe word.
- Words outside fields 3, 4 and 6 run 1,007 to 1,345, under the 1,600 cap.
- Turns for 30 children:
  - Day 145 R145 hears six readers at 45 seconds each.
  - Day 147 hears 24 children in 18 minutes.
  - Day 152 H2 has thirty 45-second turns in 25 minutes.
  - Day 155 has six groups of five, each child giving two 45-second turns in 7.5 minutes.
  - Day 156 has thirty 45-second capture turns in 22.5 minutes plus 2.5 minutes of handover.
  - Partner rereading hears five due children per 15-minute block.
  - Children not heard hand back a paper note or slip every time.
- Terms are taught before they are tested: relative forms from day 125, the sayings and similes before D2, and release components on day 154 before J1.
- Owed codes, days and assessment items from s04 and the skeletons are present.
- Lower-grade reviews are cited with their grade, for example grade 3 u01-1 day 2, grade 3 u04-6 day 145 and grade 3 u02-9 day 76. Unit 2 rows are marked "planned only".
- No em dashes and no writer placeholders.

Ledger: I checked the writer's unit 4 rows with `ledger.py show ela --course english-language-arts-grade-4`, filtered by term, for the probe pairs, relative forms, sayings, similes and the narrative and release rows. I added no rows. I fixed one note, described above. `ledger.py check ela`: 11,114 rows, 0 problems, and no planned-only finding in unit 4.

Gates:
- `unitplan.py check english-language-arts-grade-4` passes s04.md and u04-1 to u04-7.
- The course gate shows 194 failing lines, the same as the baseline, and 0 new.
- No em dash and no writer placeholder appears in u04-1 to u04-7.

My own errors: the packet header showed the X120 to X127 keys before I had solved those items (see the answer-key report).

## Plan points

For the unit lead. These are outside this job's files:
1. s04.md line 346 still prints the old D3 whose key ("Maya, whose notes her brother reads, owns the notes."). Use "Maya is the one whose notes her brother reads."
2. The frontmatter of the g4-u4-06 text lists Growing Food Together on day 143 and does not reserve paragraph 1 for X155. The plan and sources.csv (s04-src-reading-06) do reserve it. Align the text frontmatter.
3. C1, X127, X138, X148, X149, X150 and X154 are held until the text owners register fixed selections, so they cannot be given yet. C1 has a second issue: archive C on day 120 already teaches its procedure, so the replacement must be a passage the class has not seen.

## Changed for the next unit

- When an exit prints its reserved passage, check that no key can be copied from that passage. Ask for a "new" sentence and mark a copied one "not yet".
- Check dictation and probe words against this course's earlier units' probes and texts as well as the lower-grade ledger.
- A relative-clause key must not restate the joined fact as its own main clause.
- A procedural key must not depend on a number the text leaves out.
- When a card gives two facts that answer the stem, accept both.

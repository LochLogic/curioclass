# Units read: english-language-arts-grade-2 (2026-11-24)

COURSE-RUN stage 4, Reads. The expert read the four unit plans together and fixed them.

## What was read

- Unit plans s01 to s04: fields 1 to 3 and 10 in full, and the field 5 structure and goal maps.
- data/plans/english-language-arts-grade-2: days.csv, items.csv, handbacks.csv, wordlist.csv and source-map.csv. Also the grade 2 rows of data/plans/ela-texts.csv.
- The frame (models carried), the scope and sequence, and the e2 rows of data/progressions/ela.csv.
- Grade 1 s04 field 3 and grade 3 s01 field 4.
- Every written text header under courses/english-language-arts-grade-2/texts/ (all written 2026-11-19).
- Written days d082, d118, d119, d127, d157 and d158.
- docs/reviews/lead-list-lens-pass-2026-11-17.md, the four "english-language-arts-grade-2 sNN" sections.

## Verdict

The four units make a sound arc. Unit 1 builds informative writing and talk, units 2 and 3 build science explanation and research, and unit 4 ends with tales, opinion and a pollinator packet. Every grade 2 progression row has an owner, and grade 3 retrieves those rows correctly. The plans were behind the written texts: all four still called the texts commissions or pending and used old titles, and that is now fixed. The most serious finding was the unitplan gate: 132 errors, because 13 cycle-check observation days in units 3 and 4 had no field 5 record. That is fixed, and all three gates now pass. The rest of what is still open is in shared files (days.csv notes and codes, handbacks.csv and wordlist.csv), plus one question about RL.2.2's "diverse cultures" for Cory.

## Findings

| # | Severity | Finding | Verdict |
|---|---|---|---|
| F1 | high | unitplan.py check failed with 132 errors. The observation gate (added 2026-11-22) needs every code on an assess=observe day to be named in a numbered field 5 row. The 13 cycle-check days (82, 87, 92, 97, 102, 107, 112, 123, 128, 133, 138, 143, 148) only had cycle tables with "82; 13" style first cells, which the gate does not read. | fixed: s03 and s04 field 5 each have an "Observation days that carry a cycle check" table, one row per day, with the codes exactly as in days.csv. Each row says what the cycle check scores, that the oral rotation hears RF.2.4a to c, and that the topic and SL codes are seen in the exit only, unscored. |
| F2 | medium | All four plans described the texts as commissions, pending manuscripts or uncleared, using old titles (*The Green Seat*, *The Lizard and the Sun*, *Puppies and Pennies*, *The Curious Bus*, among others). Every text was written 2026-11-19. | fixed: one edit per plan in fields 2 and 10, with current titles and status, and each Pending line limited to art and the reads in each text's todo. s04 now names 03 *The Hummingbird and the Fire* (told in many places, no single origin claimed) and 04 *The Lizard and the Gray Morning* (invented, claims no culture). |
| F3 | medium | The 118 to 119 hand-back is missing its receiving end. handbacks.csv routes "hear the four children not heard" (retry, 3 minutes) and d118 names the four, but s04 field 3 said no Tomorrow line was on file, and d119 says no repair is routed. | fixed in s04 field 3. Day fault on d119. |
| F4 | medium | Teaching days whose exits hand nothing back: 104, 106, 108, 109, 110, 111, 145, 149 and 155 (the days say "No hand-back is routed"). handbacks.csv also lacks rows for 94 to 95 and 95 to 96, although the days do that repair. | for the structure pass |
| F5 | low | Paragraph-frame is withdrawn in units 1, 3 and 4 without saying where it returns. | fixed: s03 field 2 "returns on 98 for the research paragraph; withdraw it on 99", and s04 field 2 "returns on 135 for the opinion; withdraw it after 136". |
| F6 | low | Goal map day 127: the practice shape named a recount of tale 01 or 02, but the goal and the written day are rhyme and alliteration. | fixed: the s04 row 127 practice shape is now "Marks rhyme pairs and a repeated start sound in 06-b and talks on what repeating a sound emphasizes". |
| F7 | low | The section titles in the plan headers did not match the section plans (s01, s02), or were missing (s03, s04). | fixed in all four |
| F8 | low | s02 field 2 drew the writing-process words for weeks 13 and 14 from text 03, which does not hold them. | fixed: those words now come from the drafts (field 2 and table rows 13 and 14). |
| F9 | medium | wordlist.csv disagrees with the plan tables. Unit 1 weeks 5 and 6 differ, unit 2 weeks 12 to 15 are missing, and unit 3 drops repeated words. | for the structure pass |
| F10 | low | The cycle observe flag is used two ways. Units 3 and 4 flag the cycle days observe and file their items as check=end. Units 1 and 2 do neither. The scope says the embedded checks are not extra unit assessments. | for the structure pass |
| F11 | low | SL.2.2 is thin: only days 13 and 31, plus the course check. | for the structure pass (same as the s01 lead item) |
| F12 | medium | RL.2.2 asks for fables and folktales "from diverse cultures". Unit 4 now has two European fables (Aesop via Jacobs, La Fontaine via Wright), one tale with no origin claimed and one invented tale. The diverse-cultures part is thin. | for Cory |
| F13 | low | The day 118 note and the scope say the oral retry is on "42, 62 and 112". The plan keeps only 112, with fresh oral cards on 108 to 112. The plan is right. | for the structure pass. Day fault on d118 if it repeats the note. |
| F14 | low | Unit 3 has 7 Understanding days and 19 Application days, and some first teaching falls on Respond or Application days: L.2.5a on 84, L.2.3 on 111, SL.2.5 on 112, RI.2.9 on 134 and L.2.2e on 27 (unit 1). | for the structure pass |
| F15 | low | Continuity. s01 field 3 now names grade 1's day 160 needs record. Grade 3 s01 retrieves the grade 2 rows correctly. | fixed (s01 field 3). Otherwise no change. |
| F16 | low | Unit loads. The header days by kind match days.csv in all four units. | no change |

### Day faults

- **d119:** add a 3-minute hearing of the four children named on d118 (retry), and drop "no repair is routed to today".
- **d118:** if its text repeats "42, 62 and 112" for the oral retry, it should say 112 only, after the fresh oral cards on 108 to 112.
- **d104, d106, d108, d109, d110, d111, d145, d149, d155:** each exit should route its not-yet children to the next day, once the structure pass adds the handbacks.csv rows.

### For the structure pass

None of these were edited by this stage.

- **days.csv:**
  - Day 16: move the W.2.2 first teaching to day 17 or later, or reorder.
  - Add SL.2.2 to day 14 and to some days from 16 to 25.
  - Day 29: add W.2.2 and L.2.2e.
  - Day 1 note: replace e1-informative with the grade 1 day 160 needs record.
  - Day 68 note: drop "Reused... RI.2.2 from day 57", or make it true.
  - Day 74: add W.2.6.
  - Days 83, 113 and 117: add the codes listed under lead item s03.
  - Days 102 and 105: add W.2.6.
  - Day 118 note: change "42, 62 and 112" to "112".
  - Day 133: add RI.2.9.
  - Day 144: add L.2.5b and L.2.6.
  - Day 150 goal: name the poem observation.
  - Unit 3 day kinds: make the first teaching days of L.2.5a (84), L.2.3 (111), SL.2.5 (112) and RI.2.9 (134) Understanding days, or add a teaching day before each. Do the same for L.2.2e on 27.
- **handbacks.csv:**
  - Add rows for 94 to 95 and 95 to 96.
  - Add rows for the exits on 104, 106, 108 to 111, 145, 149 and 155, or note on each day why nothing is routed.
- **wordlist.csv:** reconcile with the written days. Unit 1 weeks 5 and 6, unit 2 weeks 12 to 15 (missing; weeks 13 and 14 come from the drafts), and unit 3's repeated words.
- **Cycle observe convention:** pick one for all four units. Either flag every cycle day observe and file its items as end items, or flag none. The scope's "not extra unit assessments" line should match.
- **source-map.csv:**
  - The readers are still "keep, adapt cleared". Mark them replaced by the written Curio Class originals (units 1, 3 and 4).
  - The unit 4 rows still say *The Lizard and the Sun*; point them at g2-u4-04.
- **ela-texts.csv:**
  - Row g2-u4-04: the title "A Mexican tale of a lizard and the sun" and origin "traditional, Mexican" should become *The Lizard and the Gray Morning*, Curio Class, invented, claims no culture.
  - Row g2-u4-03: the title should become *The Hummingbird and the Fire*.
  - Close the s02 sources 9 todo.
- **Frame:** the Anning line should say "the Geological Society of London", not "science societies".
- **Generated "rows to sample" counts in s03** are stale. Regenerate them.
- **docs/courses/english-language-arts-grade-2/TOOL-ASKS.md** is still missing (all four units ask for it).

### For Cory

- **RL.2.2, "fables and folktales from diverse cultures"** (F12). The unit's tales are two European fable tellings, one tale told in many places with no origin claimed, and one invented tale. Pick one:
  - (a) Replace 04 with a documented folktale from a named culture, from a free public-domain edition, with a sensitivity read. Recommended.
  - (b) Keep the unit as written and accept a thin diverse-cultures reach.
- **The g2-u4-03 sensitivity read** is still in that text's todo, and days 123 onward are already written.

## Lead-list items worked

The lead list had 51 items for this course: 35 LEAD and 16 CAP.

| Outcome | Count | Items |
|---|---|---|
| Fixed in the plan | 5 | s03 section titles; s04 texts 03 and 04; s04 section titles; CAP s02 sources 8 (trade books replaced by 01 to 04, none read); CAP s04 sources 7 (05 and 06 titles named) |
| For the structure pass | 21 | s01: source-map readers, day 16 W.2.2, SL.2.2 days, day 29, day 1 note. s02: Anning, day 68 note, day 74 W.2.6, TOOL-ASKS, CAP sources 9. s03: days 83/113/117 codes, rows to sample, W.2.6 on 102/105, TOOL-ASKS, day kinds, day 118 note, source-map readers. s04: days 133/144 codes, day 150 goal, ela-texts row 04, TOOL-ASKS |
| Settled since, or no change (with reason) | 21 | s01: wordlist exists; CAP sources 1 and 4 (superseded by written texts); CAP sequence 11 and 12 (no change). s02: ela-texts rows present; "dig" (the written story has children brush, Amara watches); product names (none found); sequence 2 (days do not use those words early); CAP sources 7 (settled); CAP sequence 3, 8, 12 and 13 (no change). s03: wordlist exists; CAP sources 9, 8c (the scope's shorter path covers it) and 10 (no change). s04: assess flags (observe flags added, the rest assessed earlier); wordlist 05-c and 05-d week rows exist; CAP sequence 9 (no change) |
| For the lead (open) | 4 | s03: Mike Budd photo and NPS checks (browser check); s03: the question budget paragraph, not recounted. s04: the safety agent read; the spray fact in exit 157 (browser check) |

## Gate results

- `python -X utf8 scripts/unitplan.py check english-language-arts-grade-2`: rc 0, every file PASS. Before this stage it failed with 132 observation-day errors (F1).
- `python -X utf8 scripts/sequence.py check english-language-arts-grade-2`: 0 failures, with 3 notes:
  - Day 10 is a Fluency day and the first day for RL.2.10.
  - Day 44 is a Fluency day and the first day for RI.2.10.
  - Day 110 is a Fluency day, but its goal revises writing.

  The notes for days 10 and 44 are fluency practice after earlier read-alouds. Day 110 goes to the structure pass with F14.
- `python -X utf8 scripts/goalmap.py audit english-language-arts-grade-2`: rc 0.

Word counts after the edits:

| Plan | Words | Cap |
|---|---|---|
| s01 | 1,283 | 1,600 |
| s02 | 1,339 | 1,600 |
| s03 | 1,387 | 1,600 |
| s04 (merged) | 1,889 | 2,300 |

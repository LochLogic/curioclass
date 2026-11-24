# Units read: English Language Arts, Kindergarten (2026-11-24)

COURSE-RUN stage 4 "Reads": the four unit plans read together, then fixed. Reader: Claude (expert role, ELA lens).

## What was read

AGENTS.md; docs/COURSE-RUN.md stage 4; docs/agents/EXPERT.md; docs/agents/lenses/ela.md; docs/courses/UNIT-PLAN.md;
the course frame and scope and sequence; data/plans/english-language-arts-kindergarten/days.csv, items.csv and
handbacks.csv (course rows); s01.md to s04.md (counted fields in full, fields 4 and 5 and the goal maps across all
four); the written day pages where a plan claim needed checking (d038, d048 to d071 response slots, d079, d084,
d085, d095, d100, d118, d123, d124, d135, d137); the texts folder titles; the kindergarten rows of
data/plans/ela-texts.csv and source-map.csv; grade 1 s01.md fields 3 and 4 (continuity out). Kindergarten is the
first course, so there is no grade below. The lead list sections for this course
(docs/reviews/lead-list-lens-pass-2026-11-17.md, s01 to s04) were worked item by item.

## Verdict

The four units hold one sound arc: launch routines and letters (unit 1), phonemes, story and narrative process
(unit 2), CVC decoding and shared research (unit 3), long-vowel association, author reasons and comparison (unit 4),
and the hand-backs between units and into grade 1 have both ends. The most serious fault was in field 5 of units 2
to 4: the foundations and retained-record tables were not written as item rows naming their codes, so
`unitplan.py check` failed 139 times, and two of those tables had drifted from items.csv (the data the days are
built from), one with a wrong key. Fixed; all gates now pass. What remains is mostly data alignment in days.csv
and source-map.csv, and one cross-unit pattern the single-unit reads could not see: the same check words come back
in three units.

## Findings

| # | Sev. | Unit | Finding | Outcome |
|---|---|---|---|---|
| 1 | serious | s02, s03, s04 | Field 5 foundations and retained-record tables (s02 R1 and H1; s03 T1 to T3 and P1 to P5; s04 F1 to F7) had no numbered day cell and abbreviated codes ("RF.K.1a, b, c"), so the observe days 64, 67, 68, 84 to 101, 123 to 155 named codes no item row held: 139 gate failures. | Fixed: s04 F rows and s03 T/P rows now open with the day from items.csv and name every code in full; s02 gains an "R1 and H1 by day" table (days 64, 67, 68, 75). |
| 2 | serious | s04 | F3 key wrong: "change /m/ in man to /t/" keyed "top", with "says op instead of top (R)". The answer is tan (items.csv s04-F134c agrees). A teacher marking from the plan marks right answers wrong. | Fixed: key, meets sample and error sample now say tan. |
| 3 | moderate | s04, s03 | Field 5 prompts drifted from items.csv, which the written days use: s04 F1 rhyme "sun, fun, bed" (items: rug, hug, bed; another rhyme for rug) and syllable steps; s03 P4 rhyme cat/hat/sun (items: pig, wig, fox), onset-rime /s/ /un/ (items: /f/ /an/), and its dates. | Fixed: plan text matches items.csv; P4 now names its item days 84, 89, 95, 101, 111. |
| 4 | moderate | s03 | The cycle check cards read in the written days 95 and 100 ("The kid is in that big bin."; "That fun chap has his big jug.") had no plan row, though they are the unit's RF.K.3 and short-vowel RF.K.3b evidence. | Fixed: one row added (keys, errors R and K from the register). |
| 5 | moderate | s02 to s04 (items) | Cross-unit reuse of check words: rabbit syllables (s02 H1e, s03 P4b, s04 F123g); add /s/ before at = sat (s02 P1b3, s03 P4e, s04 F134c); map phonemes (s02 P1a, s03 P4d); /f/ /an/ fan (s03 P4c, s04 F134a). Rule 4 binds only inside a unit, but by unit 4 a child can answer from memory. | For the structure pass (items.csv) and Day faults; plan tables kept matching items.csv until the items change. |
| 6 | moderate | s01, s04 | Goal map exits that do not produce on produce goals: day 31 "explain" exit only circles a picture and claps; day 144 "model" exit only marks a picture. | Fixed in the plan (the day's six also say a topic and detail on 31, the detail they would add on 144); Day faults for d031 and d144. |
| 7 | minor | s03, s04 | Goal map rows 113, 135, 141, 146, 149 claimed "produce" for exits that point or mark (verbs add, retrieve, exchange take either kind). | Fixed: exit kind now recognise, matching the exit. |
| 8 | minor | s02 | Stale text titles: "The Windy Picnic", "Rain at the Window", "A Parcel for Home" (written texts: The Picnic Plan, Priya at the Window, Yusuf and the Parcel), including the R1 prompt. | Fixed (field 2 and the R1 line). |
| 9 | minor | s03 | "Who Depends on Trees?" in field 2 (text: Who Depends on a Tree?); "never day 84, where RL.K.1 and RL.K.10 are first taught" (they are unit 1 rows). | Fixed, two edits. |
| 10 | minor | s03, s04 | Field 3 said no day 79 / day 118 lesson or Tomorrow line exists; both are written and hand on. | Fixed. |
| 11 | minor | s02 | Field 7 cycle response days 40, 46, 53, 59, 66, 71, 76 disagreed with days.csv (40, 46, 48, 54, 60, 64, 76). | Fixed to days.csv. Days 59, 66 and 71 also carry a foundations return and repair: harmless, no change. |
| 12 | minor | s04 | Letter names and print concepts (F1, F2) are heard from every child again in weeks 24 and 25, after course check 1 closed all 26 letters; costs about 40 one-to-one minutes. | No change (settled by the expert: retention evidence the base cycle checks also take; the days are written to it). |
| 13 | minor | s02, s03, s04 | Field 2 promises practice that days.csv codes omit: s02 day 38 (RL.K.1, RI.K.1, SL.K.2); s03 days 85 and 91 (RL.K.1, RL.K.10; RI.K.1, RI.K.2, RI.K.10, SL.K.2); s04 day 124 (RL.K.3, RL.K.7), 135 (RI.K.2, RI.K.3, RI.K.7), 137 (RL.K.10, RI.K.10, SL.K.2). The written days do the work. | For the structure pass (days.csv codes). |

Checked and sound, not to be undone: the unit-to-unit retrievals (day 35, 57, 80, 119) and their plan ends; the
handbacks.csv rows that cross units (70 and 75 into 77 and 78; 150 and 155 into 158 and 159), both ends present;
unit loads and days by kind against days.csv; long vowels placed in unit 4 (F5 to F7) as s03 field 2 says; grade 1
s01 day 1 retrieval picks up every row day 160 hands on.

## Lead-list items worked (33: 30 LEAD, 3 CAP)

- **Fixed in the plan (3):** s02 R1/T1/H1 table rows; s02 response days; s03 text-title line (part of the ela-texts item).
- **Settled by a later pass, no change (11):** s01 ela-texts rights (05 to 07); s02 Weather Words row; s02 CRLF; s03 gk-u3-06 and 05 records; s03 T3 sharing (field 5 names day 100 and next turns); s03 merged document (section plans u03-1 to u03-9 exist); s03 day 86 Time line (generated, passes); s04 ela-texts rows; s04 Time lines; s02 Frame generated line is a frame matter (below); s04 day 131/139/147 RL.K.9 check (below, kept as one structure item).
- **For the structure pass (14):** listed below.
- **Browser check, still open (5):** s01 Head Start Active Supervision headings; s02 NWS and NOAA pages, Magic Bow package and supervision link; s04 Kenya News Agency page and the movement's history page; s03 CAP sources 6 and 8 (photograph source, outdoor-supervision guide, animal-fact sources) and CAP sequence 7 (photograph source in supplies), which are source research, not a reads fix.

## Day faults

- d031 (s01-X31): add for the day's six "Say what this card is about and one detail" before the clap; key: rattles, it shakes or the handle fits a hand.
- d144 (s04-X144): after the mark, the day's six say the detail they would add to the draft.
- Reused check words (finding 5), written inline in d085, d095, d096, d101 and d123 and pulled by item tag elsewhere: change with the items.csv rows below.
- d124 credit names the Skills Block reader "Josh Takes A Bath (keep)" while unit 4 uses original cycle readers; regenerates once source-map.csv is fixed.

## For the structure pass

- items.csv (finding 5, settled by the expert): s03-P4b rabbit to pencil (pen, cil); s03-P4c /f/ /an/ to /h/ /op/, hop; s03-P4d map to bus; s03-P4e to "Add /f/ before in; change /f/ in fin to /p/" (fin, pin); s04-F123g rabbit to basket (bas, ket); s04-F134a /f/ /an/ to /j/ /et/, jet; s04-F134c to "Add /s/ before it; change /h/ in hop to /t/" (sit, top). Then update s03 P4 and s04 F1, F3 rows to match.
- items.csv: s01-X31 and s04-X144 spoken parts (Day faults).
- days.csv codes: add RF.K.1d to days 28 to 31 and RF.K.2c to day 32; W.K.1 to day 16; W.K.2 (revision) to day 29; gk-u1-08 to the day 16 Read list; W.K.2 to day 45; RL.K.1, RI.K.1, SL.K.2 to day 38; T1 codes (RL.K.1, RI.K.1, RI.K.2, SL.K.1a, SL.K.1b, SL.K.2, SL.K.3) to days 67 and 68; W.K.3 to days 70 to 72; SL.K.1 to day 86; W.K.7, W.K.8 to day 83; W.K.2 to day 116; RL.K.1, RL.K.10 to day 85; RI.K.1, RI.K.2, RI.K.10, SL.K.2 to day 91; RL.K.3, RL.K.7 to day 124; RI.K.2, RI.K.3, RI.K.7 to day 135; RL.K.10, RI.K.10, SL.K.2 to day 137; drop RL.K.9 from days 131 and 147 unless a story is read there.
- days.csv observe-day codes do not match the cycle checks held that day (day 123 lists RF.K.3b, 3d, 4 but F1 checks RF.K.1a to d, 2a, 2b, 3c; day 150 lists only RL.K.9 but holds F6): set each observe day's RF codes to its check row.
- days.csv notes for days 144 and 147: name the audio recorder and classroom device.
- days.csv notes (days 134 to 136, 140, 152) and the gk-u4-03 title in ela-texts.csv: drop "millions"; the text itself gives no number.
- source-map.csv: mark the six unit 3 and seven unit 4 Skills Block reader rows "replaced" (original readers gk-u3-cr1 to 6, gk-u4-cr1 to 7).
- docs/courses/english-language-arts-kindergarten/TOOL-ASKS.md does not exist: create it with the shared offline text editor (light), days 69 and 75, and the unit 4 audio recorder.
- frame.md units table, unit 2 "Why here": "Story elements come first" should read information first (days 35 to 48), story elements from day 49 (copied into s02 field 3 by the skeleton).
- days.csv day 33: kind Application with a record-only goal; retype or give it its partner share in the goal.

## For Cory

None. No finding touches scope, audience, money or people.

## Settled by the expert

- Finding 12: unit 4 keeps F1 and F2 letter and print components for every child (retention evidence; days written to it). File: s04.md, none changed.
- Finding 5 replacement words (above). File: items.csv, for the structure pass.
- Finding 7 exit kinds relabelled recognise (113, 135, 141, 146, 149). Files: s03.md, s04.md.

## Gates

- `python -X utf8 scripts/unitplan.py check english-language-arts-kindergarten`: PASS, all 36 files (was FAIL on s02 17, s03 68, s04 54).
- `python -X utf8 scripts/sequence.py check english-language-arts-kindergarten`: 0 failures (one existing note, day 12 kind).
- `python -X utf8 scripts/goalmap.py audit english-language-arts-kindergarten`: runs clean (exit 0); it is a reading dump, not a pass or fail.

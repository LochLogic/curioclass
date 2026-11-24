# English Language Arts units: structure pass, 2026-11-24

COURSE-RUN stage 4 structure pass for the English Language Arts unit plans of kindergarten and grades 1 to 5 and
7 to 12 (grade 6 belongs to another session). Modeled on ss-units-structure-pass-2026-11-14.md. Sources: the
"For the structure pass", "Day faults" and "For Cory" sections of docs/reviews/units-read-<course>-2026-11-24.md.
Each item was checked against the current file before it was applied. Where a days.csv goal or note changed, the
copies in the course's plan files (day-list rows, section plans, skeletons) were synced. No written day was edited;
day faults went to data/plans/defects.csv.

## Gates

| Gate | Before | After |
|---|---|---|
| unitplan.py check (12 courses, 210 plans) | 210 PASS, 0 FAIL | 210 PASS, 0 FAIL |
| sequence.py check, failures | 0 in every course | 0 in every course |
| sequence.py notes (K, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12) | 1, 1, 3, 11, 3, 1, 0, 0, 0, 1, 1, 0 | 1, 0, 3, 11, 3, 0, 0, 0, 0, 1, 1, 0 |
| plan.py check failures (K, 1, 2, 3, 11); frame gates | 35, 38, 310, 45, 12; 0 | 35, 38, 310, 45, 12; 0 |
| lesson.py FAIL lines, these courses (whole repo) | 235 (1,049) | 235 (1,049) |

No progression changed, so the progression gate was not run. A mid-pass run found 16 new unitplan failures, all
from added codes the plans do not name or score. Those additions were undone (listed under "Undone"); the final
run matches the baseline.

## Shared files

- **scripts/unit_skeleton.py**: added `has_order_conflict()`. The skeleton marked "order conflict" on every
  source-map row whose order_conflict cell held any text, including no-conflict prose such as "None; lesson order
  retained." Applied. Grade 3 plans: 113 false marks removed, 3 real conflicts kept. Other courses' skeleton output
  changes only where such prose exists.
- **data/plans/ela-texts.csv**: row edits listed per course below; three grade 8 assessment rows added.
- **data/plans/defects.csv**: 9 rows added (see "Day faults").

## Kindergarten

Applied:
- items.csv s01-X31 (spoken part adds "Say what this card is about and one detail") and s04-X144 (the day's six
  say the detail they would add); answers and steps match.
- days.csv codes: RF.K.1d on 28 to 31, RF.K.2c and RF.K.1d on 32; W.K.1 (16), W.K.2 (29, 45, 116), RL.K.1, RI.K.1,
  SL.K.2 (38), T1 codes (67, 68), W.K.3 (70 to 72), SL.K.1 (86), W.K.7 and W.K.8 (83), RL.K.1 and RL.K.10 (85),
  RI.K.1, 2, 10 and SL.K.2 (91), RL.K.3 and 7 (124), RI.K.2, 3, 7 (135), RL.K.10, RI.K.10, SL.K.2 (137); scored
  item codes added to observe days 89, 94, 95, 111, 123, 129, 134, 150; RL.K.9 dropped from 131 and 147.
- days.csv notes: day 16 Read list adds gk-u1-08; "millions" dropped (134, 135, 136, 140, 152, and the gk-u4-03
  title); tool lines on 144 (audio recorder) and 147 (classroom device); day 33 goal and shows reworded.
- source-map.csv: 13 unit 3 and 4 reader rows set to ours (the days read the Curio Class original cycle readers).
- Plans: "millions" removed from frame, s04, scope and sections; unit 2 "Why here" order (weather first, story
  elements from 49); s02 T1 rows numbered by day; s03 row for SL.K.1 on 86. TOOL-ASKS.md written.

Not applied:
- Reused check words in items.csv: the written days print the words inline, so items and days must change
  together. Defect row added.
- Trimming observe-day codes to the scored sample: the codes column also lists what is taught that day; only
  additions were made.

## Grade 1

Applied: observe-day notes on 38, 43, 53, 58, 63, 68 (foundations parts outside the sample are scored on days 76
and 77) and on 83, 88, 93, 98, 103, 108 (days 158 and 159); SL.1.1a to c source note on 38 and 88; day 45 "teach
-ing" to "practice -ing" (day 44 teaches it).

## Grade 2

Applied:
- days.csv codes: SL.2.2 (14); W.2.2, L.2.2e (29); W.2.6 (74, 102, 105); RI.2.7, 4, 5, 2 and L.2.4 (83); RL.2.10
  (113); W.2.3, L.2.5, L.2.6 (117); RI.2.9 (133); L.2.5b, L.2.6 (144); W.2.2 dropped from 16.
- days.csv notes and goals: day 1 (e1-informative removed; grade 1 day 160 record named); day 118 retry on 112
  only; day 150 goal and shows; day 35 names the Geological Society of London. Plan copies synced.
- handbacks.csv: 94 to 95 and 95 to 96 (error D, repair, 5 minutes).
- source-map.csv: 26 reader rows set to ours; the two Lizard rows name g2-u4-04.
- ela-texts.csv: g2-u4-03 "The Hummingbird and the Fire" with its author; g2-u4-04 "The Lizard and the Gray
  Morning", Curio Class, invented tale that claims no culture.
- s04 text-set skeleton lines refreshed; s03 sample counts recounted (115: 10, 117: 10, 118: 7). TOOL-ASKS.md
  written.

Not applied:
- SL.2.2 on days 16 to 25: the read names no day.
- Unit 3 day kinds and day 27: the days are written; changing kinds means rewriting them.
- Handbacks for the exits on 104 to 155: the receiving days have no slot; left for the lead with the day writers.
- wordlist.csv reconcile: needs a read of the written days.
- Cycle observe convention and "s02 sources 9 todo": lead decision; the second item's meaning is unclear.
- Frame lizard and hummingbird wording: waits on the RL.2.2 choice (For Cory).
- Day 68 "Reused" line: already gone.

## Grade 3

Applied:
- days.csv codes: SL.3.5, RF.3.4a to c (30); RF.3.3a (45); RL.3.3 (47); RI.3.2, RI.3.7 (56); L.3.1b, c (58, 59,
  64, 73); RL.3.2 (99); RF.3.3d, L.3.2e, f, W.3.10, W.3.4 (106); L.3.2c (113); SL.3.1a to d, SL.3.2, SL.3.3 (149);
  SL.3.4, SL.3.6, L.3.3b, W.3.6 (151); SL.3.4, SL.3.6, L.3.3b moved off 107.
- days.csv notes and goals: day 7 retrieval label; I08 note on 66 to 74 (body 69 and 70, separate paragraph 71);
  g3-u2-02 dropped from 51; day 28 goal "practice an explanatory paragraph" (unscored per the plan); day 134 "town
  water-cleaning text". Plan copies synced.
- ela-texts.csv: g3-u4-03 "How a Town Cleans Its Water" (Curio Class); g3-u2-05 retitled; g3-u2-07 glass frogs,
  U.S. Fish and Wildlife Service. Sections u04-5, u04-6 and their skeletons use the new title.
- wrongs.csv s02-A43 error letter x to Y, matching the plan.
- 113 false "order conflict" marks removed from the plans (see unit_skeleton.py).

Not applied:
- Days 2 and 3 kinds: written days; a judgment call.
- Handbacks for exits X39, X119, X124, X152, X154: no receiving slot; left for the lead.
- e2-compare-texts "last day 98": the generator counts the RL.3.9 code on 98 as a use; not a bug.

## Grade 4

Applied: frame names Harry T. Burn's August 19, 1920 explanation in the Tennessee House Journal (page 94; public
domain); lead item 4 reads "reuse Harry Burn's statement".

Not applied: the grade 4 to grade 5 portfolio receiver needs writer content in grade 5's s01.

## Grade 5

Applied:
- days.csv codes: RI.5.4, L.5.4a to c (48); RL.5.10, L.5.5a, b (60); RI.5.4, L.5.4a, b (94); W.5.1, W.5.5 (111);
  W.5.4 (119); RI.5.2 (125); RL.5.5 (142).
- days.csv notes and goals: day 22 "an unfamiliar passage from the novel's world"; day 36 "Model"; day 44 drops
  the g5-u2-04 conditional; day 53 feedback and day 129 "invented for practice" wording; days 97 to 99 refer to
  "02, our explanation of Robinson's 1949 testimony". Plan copies synced; scope marks g5-u2-04 not used.
- ela-texts.csv: g5-u1-05 form "narrative scene"; g5-u4-07 "Four Views of the River" (Curio Class, to write);
  g5-u4-08 Touton's June 14, 2022 Senate opening statement; g5-u4-04 public domain, published 1921, checked
  2026-11-24; g5-u3-02 retitled as our explanation of Robinson's testimony (Curio Class, to write).

Not applied:
- W.5.1 on 119 and 120: the plan says the caption is W.5.4 evidence only.
- Source-map crop names: wait on the novel.
- Frame line "words of their time": a harmless guard; left for the lead.
- Undone: see "Undone".

## Grade 7

Applied:
- days.csv codes: SL.7.1c, d (4); W.7.5 (53); W.7.3, W.7.5, SL.7.1 (56); RI.7.1 (54); RL.7.9 (92, 93); RI.7.10,
  RL.7.10, RL.7.7, SL.7.1, W.7.3 (134); L.7.4b (144, 149, 155); RI.7.1 (155).
- days.csv goals and notes: day 27 "a cold two-view story on a different topic" (matches s01 day 27); day 33
  "Trace interactions between plowing, drought and soil loss" (US spelling); day 14 adds the first 1,050 words of
  the eighth installment (s01); day 16 drops the independent reading sentence; day 74 "the refined question for
  the day 75 choice"; day 95 g7-u4-06 omitted; day 137 two charts, salmon chart on 146. Plan copies synced.
- frame.md: dams removed 2022 to 2024; Mather's July 12, 1716 letter to Woodward (both the text list and the
  excerpt years). scope-and-sequence: five foundations on day 31, pronoun reference on day 34.
- ela-texts.csv: g7-u4-06 status omitted; g7-u6-01 USGS only, 2022 to 2024, Open-File Report 2011-1311 (2012).

Not applied:
- Day 60 retrieval rows, day 79 article length, day 83 rehearsal scoring: not confirmed in the plans in time; lead.
- Day 40 and 67 goals to produce verbs: the read leaves rewording or narrowing the exits open.
- Kinds for 10, 22 to 24 and 130; days 81 and 82 reading minutes; RI.7.1 on 66 or 68; week 22 words: judgment
  calls or "if wanted".
- New ela-texts rows for assessment-only texts (The Notice, Callaway, McNiff, Nationwide Expansion): left for the
  lead with the rule question.
- Shape (units 2 to 6 merged documents) and the source checks: for the lead.

## Grade 8

Applied:
- ela-texts.csv g8-u4-07: The Turkish Jester, trans. George Borrow, 1884, 1924 Norwich reprint (Gutenberg 16244),
  on file, public domain. Added rows g8-u1-03 (National Archives, 2016, day 28), g8-u4-08 (duck-broth tale, page
  265, day 121) and g8-u5-07 (A White Heron section II, day 155), each a cold check text.
- frame.md unit 4 Texts cell names the Borrow edition.

Not applied: s04 still names Barnham (outside the listed items; lead). Undone: see "Undone".

## Grade 9

Applied:
- days.csv codes: RL.9-10.5 (14, 30, 38); L.9-10.4c (17); L.9-10.4b (36, 41); L.9-10.4, 4b, 6 (54, 59, 63, 88,
  91); SL.9-10.3 (104, 109); SL.9-10.1a to d, L.9-10.4b, L.9-10.6, W.9-10.9b, W.9-10.10 (128); SL.9-10.4 to 6 (125
  to 127); L.9-10.4b, L.9-10.6 (152).
- days.csv notes: day 100 drops "selected health pages still to choose"; day 119 drops "anatomy". Plans synced.
- ela-texts.csv: g9-u3-04 composition date unconfirmed (not 1740); g9-u4-07 and g9-u6-04 Curio Class originals
  ("A Trial Is Not a Guarantee"); Gutenberg numbers on g9-u4-01, 03, 04, 08.

Not applied: repair-slot notes (52 to 59), conference windows (39 to 46, 60, 149 to 151), word-family slots and
e9-l-word-strategies, day kinds (54, 56, 59, 83, 110, 113, 126), section 6.2, days 15 and 16 split, day 79 SL day,
day 144 Child 84A, teacher notes on 67 and 68; ela-texts g9-u1 editions, g9-u3-05, g9-u6-01, Vanka, Up from
Slavery, C115 and u8 editions; wordlist.csv; library copies; framework links; the skeleton "frame names no model"
message; the grade 12 seam. Each needs a plan read or a writer; left for the lead. Undone: see "Undone".

## Grade 10

Applied: L.9-10.6 (133), W.9-10.9 and 9b (138), W.9-10.6 (152); day 89 "Before unit 5 (hook on day 90)," with s05
synced.

Not applied: week 25 to 29 focus-word notes, Mill sensitivity flags on 120 to 125, g10-u6-05 newspapers and the
Ballantyne row: need the s06 and s07 tables and sources; left for the lead.

## Grade 11

Applied: RL.11-12.10 on 24 and 25; L.11-12.4, 4b on 127; day 56 note names only the Declaration printing (s04
synced); ela-texts Fowler as an extract, Song of Myself 1892 (1891-92 edition), census label "US Census Office",
1894 volume.

Not applied: assess codes for 76 and 77 (the read names none), the day 59/64 SL move, notes on 90, 123, 131, 132,
143, 152, 156, the missing unit 3, 5 and 6 rows and Mather IX, field 10 editions, wordlist.csv, the frame
sensitivity line, the "Check set adds: Crane" line and the Twain clash; left for the lead.

## Grade 12

Applied: ela-texts g12-u4-08 status "to confirm", todo names the unverified free text; day 65 note "once a free
copy is verified (none assigned until then)", s04 synced.

Not applied: day 24 note waits on Cory's film choice.

## Undone

These additions caused new unitplan failures (code not named in field 2, or an assessment day with no item) and
were reverted; the plans would need field 2 or field 5 rows first:
- Grade 5: W.5.6 (28), W.5.9b and L.5.6 (40), RI.5.4 (124), RI.5.1 and RI.5.4 (126).
- Grade 7: W.7.3 and SL.7.1 on day 53 (W.7.5 kept).
- Grade 8: L.8.1a, b, d (58), L.8.1d (82, 83).
- Grade 9: SL.9-10.1 on 152.

## Day faults (defects.csv rows added)

1. K u01-7/d031: X31 spoken part.
2. K u04-6/d144: X144 detail.
3. K d085, d095, d096, d101, d123: reused check words.
4. K u04-1/d124: Skills Block reader credit; regenerate.
5. Grade 2 u04-1/d119: hear the four children named on d118.
6. Grade 2 u03-12/d118: retry on 112 only.
7. Grade 3 d044 or d045: skills-block reread before 46.
8. Grade 3 d040 to d050: clip-card notes and a reread chance.
9. Grade 3 u04-1/d123: e2-compare-texts retrieval.

Grades 1, 4, 11 and 12 had no day faults; the grade 5, 7, 8, 9 and 10 reads had no day-faults section.

## For Cory

- **Grade 1:** skill-family spacing for L.1.5, L.1.6 and conventions.
- **Grade 2:** RL.2.2 diverse cultures: (a) a documented folktale (recommended) or (b) keep. Also the g2-u4-03
  sensitivity read, with days from 123 already written.
- **Grade 3:** an audience note that the water text's facts are ours to stand behind.
- **Grade 4:** the writing balance 30/35/35: add a narrative piece, or restate the share.
- **Grade 7:** unit 1 audio (make it or drop the line); the novella setting decision.
- **Grade 9:** whether a unit's independent book may go home; the Connell sensitivity rulings and the safety read
  of the suicide-prevention sources are reads to schedule.
- **Grade 11:** Occom's narrative rights (ask the archive, display only, or replace); possibly the grade 11 and 12
  Twain clash.
- **Grade 12:** unit 2 film: approve the original silent film, or keep the 1921 film.
- Kindergarten and grades 5, 8 and 10: none.

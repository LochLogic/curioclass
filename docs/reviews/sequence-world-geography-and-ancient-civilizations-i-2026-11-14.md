# Sequence read: World Geography and Ancient Civilizations I (grade 6), 2026-11-14

Expert cold read of the scope and sequence, per docs/pipeline/briefs/sequence-read.md. Independent of any other read of
this course's scope and sequence (the Codex read was not opened).

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/social-studies.md, the social studies part of
  docs/ADOPTION-BAR-SUBJECTS.md (with the shared core and pass rule), docs/courses/social-studies/STANDARD.md.
- docs/courses/world-geography-and-ancient-civilizations-i/scope-and-sequence.md and
  data/plans/world-geography-and-ancient-civilizations-i/days.csv, cold, in full.
- Beside them: the frame (docs/courses/world-geography-and-ancient-civilizations-i/frame.md), every grade 6 row of
  data/progressions/social-studies.csv and the rows they assume (ss3-money-saving, ss5-independence-war), the grade 6
  standards in data/standards/ma-hss-2018.txt, docs/courses/CALENDAR.md, the grade 6 rows of data/plans/calendar.csv,
  the unit rows of the ELA 6 frame (for the product-load question), docs/pipeline/briefs/sequence-write.md, and the
  frame read docs/reviews/frame-world-geography-and-ancient-civilizations-i-2026-11-13.md.
- Gates: `plan.py check` passes for this course (`sequence world-geography-and-ancient-civilizations-i: 0
  failure(s)`; the run exits 1 on one STALE note in docs/courses/us-history-ii/frame.md:78, not this course).
  `frame.py calendar`: grade 6 social studies checks in weeks 15, 23, 32; no stagger break. `stale.py check`: the same
  single us-history-ii failure, none here.

## Verdict

Sound, and close to ready: every unit runs its inquiry arc to its compelling question or a claim day, every lettered
part of MA.6.T2.6 and MA.6.T3b.4 and MA.6.T3e.3 sits on its own day, the checks sit on CALENDAR.md's target weeks, and
the writing grows from a first short claim (day 14) to two reports. The biggest risk is assessment stacking: in all
three places the last unit's end-of-unit assessment sets nearly the same task as the course-level check two school
days later, and weeks 22 to 24 hold six assessment events in ten school days. The one change that matters most is to
have each course-level check draw its items for the skill just assessed from earlier units' content (finding 1).

## Findings

### 1. Each course-level check repeats the end-of-unit assessment held two days before it

- **LAYER** sequence. **REPEAT** new. **Confidence** likely.
- **What is wrong.** Day 155 (unit 11's end-of-unit assessment) sets "two unseen sources on one society corroborated";
  day 157 (check 3, day 1) sets "corroboration of two unseen sources on one society". Day 112 (unit 8) sets "a
  cause-and-effect chain across places and an unseen source sourced and used"; days 114 and 115 (check 2) set "a
  cause-and-effect chain across places" and "an unseen ... source sourced and used". Day 69 (unit 5) sets "an unseen
  record of Kush sourced"; day 72 (check 1) sets "a short sourced claim from an unseen ancient source". Around check 2
  the calendar also stacks ELA 6's check (days 109 and 110, inside the research drafting days), the report hand-in
  (111), unit 8's assessment (112), check 2 (114, 115) and math 6's check (118).
- **Why it matters.** Two near-identical tasks two school days apart measure the same thing twice, and the check then
  reports the unit just taught rather than what has lasted, which is a course-level check's job (GLOSSARY). A busy
  item writer will copy the unit's task forward.
- **Fix (no day moves).** In each check, the part that tests the skill of the unit just assessed takes its content
  from earlier units: check 1's sourced claim on a unit 4 source (a law or inscription), not Egypt or Kush; check 2's
  cause-and-effect chain on unit 4 or unit 6 content, and its unseen source from unit 6 or 7; check 3's corroboration on
  a unit 9 or unit 10 society, not the Maya or Andes. Day 112: the report stands as the MA.6.T3g.2 and D1.3 to D1.5
  part of the assessment, and the day's own task tests MA.6.T3g.1 and D2.His.1 only, so it is shorter. Settled below.

### 2. Unit 6 opens with a readiness check on a row grade 5 used the year before

- **LAYER** frame, progression. **REPEAT** new (the cross-course question the lead asked about). **Confidence** firm.
- **What is wrong.** Day 75 is a readiness check on ss3-money-saving, as the frame and the ss6-phoenician-trade row
  say ("dormant knowledge"). But ss5-independence-war uses ss3-money-saving and opens with a retrieval task on money,
  price and loans, so the row was used the year before. sequence-write rule 2 says such a row opens as a retrieval
  task inside a day; a readiness check is for a row idle two or more grades. The writer kept the frame's word and named
  the conflict (For the lead 2).
- **The right call: the rule.** The grade 5 use is real, and what unit 6 adds (money as a store of value, saving) is
  taught directly on day 78 anyway. A readiness check plus a small-group reteach costs a share of day 75 and day 76,
  and day 75 already has to place six places on a map (MA.6.T3d.1).
- **Fix.** Day 75: assess blank; goal "The ancient Mediterranean on a map: Greece, Asia Minor, Crete, Phoenicia, the
  Aegean and the Red Sea". Day 78: goal opens "Open with a retrieval task on what money is for and why people save
  (grade 3, used in grade 5)"; note "Retrieval task on ss3-money-saving (used in grade 5's ss5-independence-war)".
  Scope and sequence unit 6: replace the Readiness bullet with the retrieval line. Frame Seams row and Units row 6,
  and the ss6-phoenician-trade notes: "content revisited: the unit opens with a short retrieval task" in place of
  "dormant knowledge ... readiness check ... one-lesson reteach".

### 3. Unit 11 teaches the societies students report on in one day

- **LAYER** sequence. **REPEAT** new. **Confidence** likely.
- **What is wrong.** Day 147 carries the Maya, the Moche and Nazca, Maya, Quechua and Aymara peoples today, and the
  burning of the Maya books, then report days 148 to 154 begin. MA.6.T5c.1 is the unit's only history code and its
  whole shared base is that one day. Unit 10, by contrast, gives the peoples today a day of their own (day 132).
- **Why it matters.** The lens: inquiry rests on taught content. Students choosing between the Maya and an Andean
  society with no writing need to know what each left (glyphs and codices against pottery, murals, lines in the
  desert) before they can plan sources on day 148. The peoples today, a frame rule, get a clause.
- **Fix (a day swap inside the unit, no change in count).** Day 147: the Maya (cities, farming, beliefs, glyphs, the
  burned books) and Maya peoples today. Day 148: early Andean societies (Moche, Nazca: pottery and murals as evidence
  where no writing survives) and Quechua and Aymara peoples today. Report days become 149 to 154, with "hand in" and
  "share and answer the compelling question" joined on day 154 (sharing as a short gallery walk). Settled below.

### 4. MA.6.T4b.1's Islam half is on no day

- **LAYER** sequence. **REPEAT** yes (a code taught in part, as in the frame read's finding 5). **Confidence** firm.
- **What is wrong.** MA.6.T4b.1 asks how Axum "and other East African societies" affected the spread of Christianity
  and Islam. Day 124 gives Axum's turn to Christianity; day 125 (the Swahili coast) names no Islam, and its codes are
  MA.6.T4b.2 only. The ss6-axum-swahili row has it ("East Africa's part in the spread of Christianity and later Islam").
- **Fix.** Day 125 goal: add "and Islam arriving with Arab and Persian traders to the Swahili towns"; codes add
  MA.6.T4b.1. Settled below.

### 5. Two codes are named whole but taught in part on their days

- **LAYER** sequence. **REPEAT** yes. **Confidence** firm.
- **What is wrong.** Day 3 (MA.6.T1.3) has "archaeologists, historians and geographers" combine evidence; the standard
  names economists and political scientists too, and day 1 introduces all five. Day 16 (MA.6.T2.4) is "the Neolithic
  turn to farming"; the code also names animal domestication and metalworking.
- **Fix.** Day 3 goal: "... where archaeologists, historians, geographers, economists and political scientists combine
  their evidence (a dated layer, a tablet, the old river course, a trade record, the king's rule) to test one idea
  about Ur". Day 16 goal: "The Neolithic turn to farming and herding, in several places on their own, and the first
  metalworking, with Catalhoyuk ...". Settled below.

### 6. Units 1 and 3 never ask students to answer their compelling question

- **LAYER** sequence. **REPEAT** new. **Confidence** likely.
- **What is wrong.** Every other unit has a day that answers its compelling question. Unit 1 ("How can we know anything
  about people who lived thousands of years ago?") ends on the out-of-Africa map (day 8) and its assessment (day 9)
  sorts questions and places dates. Unit 3 ("Why do people live where they do in a dry land?") goes from satellite
  images (day 33) to the action days.
- **Why it matters.** Bar item 1 asks the arc to reach a conclusion; without it the question is decoration.
- **Fix.** Day 9's assessment adds one short written answer to unit 1's question from the unseen site plan. Day 33
  ends with a short written claim answering unit 3's question from the climate graphs, resource map and images.
  Settled below.

### 7. The held look-back day and the generated calendar disagree by one day

- **LAYER** process. **REPEAT** new. **Confidence** firm.
- **What is wrong.** Day 55 is unit 3's look-back, held to the start of unit 5 as the frame sets. Unit 4 therefore runs
  39 to 54 here, while data/plans/calendar.csv (built from the frame's day counts) shows 40 to 55.
- **The right call: keep days.csv as written.** The held day is the frame's own design, the writer placed it exactly
  where the frame says, every unit keeps its count, and the one-day shift crosses no check, no stagger day and no lean
  window (ELA 6 unit 2 runs days 33 to 58 either way). The written scope and sequence is the finer record, so the
  calendar should follow it, not the reverse.
- **Fix.** frame.py builds calendar.csv unit ranges from days.csv once one exists (a held day keeps its unit's stretch
  number, so a unit's range is its first to last contiguous run, with the held day listed apart). No change to this
  course's files.

### 8. The standards file drops a digit in MA.6.T2.3

- **LAYER** standard. **REPEAT** new. **Confidence** firm.
- **What is wrong.** data/standards/ma-hss-2018.txt reads "about 2. million to 11,700 years ago". Day 6 rightly uses 2.5
  million, but a day writer quoting the code's line will copy the gap.
- **Fix.** "about 2.5 million to 11,700 years ago" (check against the framework PDF's grade 6 page when the line is
  edited).

## Days by load

Unit by unit the teaching days follow what each part owns: unit 2's four parts at 4, 4, 4 and 1 days; unit 4's
fourteen codes over 12 teaching days, with six on writing and law where the sourcing is first done in full; unit 7 at
5, 3 and 4 days for Judaism, Christianity and Islam, which matches their codes (5, 2 and 3). Unit 8's 5 connection days
and 7 research days (9 with the assessment and respond days) match the frame's "about 5" and "about 9". The only run
under its load is unit 11's one day of shared content for MA.6.T5c.1 (finding 3). Unit 9 gives Axum and the Swahili
coast one day each, which is enough once finding 4 is applied.

## The calendar and leans

- Checks on target weeks 15, 23 and 32; ELA 6 (days 59, 60, 109, 110), math 6 (80, 118) and science 6 (90) share no
  school day with them.
- Leans checked against calendar.csv: math 6 negative numbers (days 120 to 141) and four quadrants after units 1 and 3;
  science 6 climate (52 to 89) after day 28; science 6 geologic time (92 to 115) reuses the timeline; ELA 6 Hammurabi
  (33 to 58) beside unit 4 with day 47's bridge; ELA 6 research (63 to 86) before unit 8; ELA 6 writing systems (87 to
  108) after unit 6; ELA 6 comparing accounts (unit 6 from day 137) before unit 11's corroboration days. All met.
- For the lead 3 (product load) is settled: ELA 6 unit 4 ends in one-sitting pieces, not a large product, so the
  frame's two-week rule holds. The stacking that remains is finding 1.

## Candidate cells

Both settled with their cost: Catalhoyuk inside MA.6.T2.4 at no added day (day 16); Judaism after 70 CE at about half
of day 89. Agreed with both.

## The lens checklist (scope and sequence layer)

| Line | Met, missed or not applicable |
|---|---|
| A unit question answerable without the unit's sources, or with one defensible answer | Met: each question has two or more defensible answers from the unit's sources; units 1 and 3 do not ask for the answer (finding 6) |
| History out of time order with no reason | Met: Islam's origins in unit 7 and the region-by-region order (units 9 to 11) carry the anchor's grouping as the reason |
| A contested event given one telling only | Met: human origins (older and newer views), Kush (outsiders and its own monuments), the Caribbean peoples (European and their own accounts), West Africa (Arabic writers and griots) |
| Writing from sources once a year or never building from short to long | Met: claims from day 14, a sourced claim on the code (day 50), report 1 (unit 8), a longer report (unit 11) |

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| Check items for the skill just assessed draw content from earlier units (check 1: a unit 4 source; check 2: chain on unit 4 or 6, source from unit 6 or 7; check 3: corroboration on a unit 9 or 10 society) | A check measures what lasted, not a repeat of the unit test two days before | days.csv days 72, 114, 115, 157; scope-and-sequence.md course-level check sections |
| Day 112 tests MA.6.T3g.1 and D2.His.1; the report counts for MA.6.T3g.2 and D1.3 to D1.5 | Cuts the double test in the week of four assessments | days.csv day 112 goal |
| Unit 6 opens with a retrieval task on day 78, not a readiness check on day 75 | sequence-write rule 2: the row was used in grade 5 | days.csv days 75, 78; scope-and-sequence.md unit 6; frame.md Seams and unit 6; ss6-phoenician-trade notes |
| Unit 11: day 147 the Maya, day 148 the Andean societies, report on 149 to 154 with hand-in and sharing joined | One day was the whole shared base for the report | days.csv days 147 to 154; scope-and-sequence.md unit 11 |
| Day 125 adds Islam on the Swahili coast and MA.6.T4b.1 | The code's second half had no day | days.csv day 125 |
| Day 3 names all five fields; day 16 adds herding and metalworking | Codes taught in full | days.csv days 3, 16 |
| Day 9 adds a short answer to unit 1's question; day 33 ends on a claim answering unit 3's | The arc reaches its question | days.csv days 9, 33 |
| Keep the held look-back on day 55; the calendar follows days.csv | The frame's design, no check or lean moves | none here (frame.py) |
| MA.6.T2.3: "about 2.5 million" | A dropped digit | data/standards/ma-hss-2018.txt |

## For Cory

Nothing. Every finding is an item-level or process choice.

## What I could not judge

Whether the online map tool on day 121 exists as a single-file Curio Class tool yet (the day keeps its paper path, so
the day is safe either way). Outside sources were not re-fetched on this run: the findings rest on the anchor text in
the repo, the rows and the calendar, so none needs one.

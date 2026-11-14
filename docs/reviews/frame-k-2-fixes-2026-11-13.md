# Fixes: social studies course frames, kindergarten to grade 2, after the two cold reads (2026-11-13)

Applies the expert reads (`frame-social-studies-<course>-2026-11-13.md`) and the Codex reads
(`frame-social-studies-<course>-codex-2026-11-13.md`) for kindergarten, grade 1 and grade 2 to the three frames,
`data/progressions/social-studies.csv` and the seam table of the grade 3 frame. Every expert finding and every
"Settled by the expert" row is applied; each Codex finding was weighed on its merits.

Gates after the fixes: `scripts/frame.py sync` (15 courses); `scripts/stale.py check` 19 files, 0 failures;
`scripts/plan.py check` exit 0 (progression social-studies 384 rows, 0 failures; every frame 0 failures). No unit,
skill or standard moved; every course keeps its unit count and total days (K 6 and 64, grade 1 8 and 96, grade 2 7
and 96).

Files outside this pass (`docs/GLOSSARY.md`, `docs/ROADMAP.md`, `docs/APPROACH.md`, `data/standards/ma-hss-2018.txt`,
earlier review reports) were not edited; the stale notes and clarifications the readers found there are listed
under "For the lead" with the readers' replacement text.

## Kindergarten

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | Three of unit 5's 11 days are on-the-day lessons (Indigenous Peoples' Day or Columbus Day; Veterans Day with Thanksgiving; King Day), each carrying the teacher note; new course brief bullet; unit 5's reason rewritten. Unit stays 11 days, course 64 |
| Expert | 2 | Applied | The informed action is a real classroom problem (coat hooks, block corner, reading corner) with a look back after a week; a plant name is a warm-up vote only. Frame brief, unit 2 and ssk-class-decision notes |
| Expert | 3 | Applied | Cross-subject row: K.CC.B.5, unit 6, about week 28, tokens worth one, prices 1 to 5; lean also added to ssk-goods-services-money |
| Expert | 4 | Applied | Spoken, teacher-led sort, two statements per symbol, picture bins, dates said by the teacher only (unit 5 note and ssk-national-symbols notes); C3 cell now "D2.His.10 (review: an old paper as a clue)" |
| Expert | 5 | Applied | Stale frames.csv note rewritten |
| Expert | settled | Applied | Both rows (tokens; the symbols sort) |
| Codex | 1 | Applied in part | Time words of MA.K.T3.3b in full and an informational read-aloud (ssk-sequence-time, unit 4); first look at two differently designed world maps beside the globe (ssk-maps-globes, unit 3). The standards file paraphrase is for the lead |
| Codex | 2 | Applied, wording mine | Unit 4 question now "Which change from long ago made the biggest difference to everyday work?"; each child picks one change, points to a named photograph or object, gives a reason, names what stayed. Item-level wording chosen to read aloud to five-year-olds |
| Codex | 3 | Applied | One respond day after each check; the final check adds an unseen picture map and a source-based "I think ..., because ..." |
| Codex | 4 | Applied | Unit 3 check-set cell rewritten: California K.4.3, New York K.6; the state on a US map labelled a Curio Class extension informed by California 1.2.1 |
| Codex | 5 | Applied, with expert 1 | Conflict settled: the expert's on-the-day lessons fix the real risk (careful notes after the holidays), and Codex's point holds that the King Day promise was false. Unit 5 is now placed by its prerequisites, the block's dates are left to the scope and sequence ("about February"), minutes corrected to 40 to 60, cross-subject weeks recounted |
| Codex | 6 | Applied | Same as expert 5 |
| Codex | 7 | For the lead | `docs/GLOSSARY.md` course frame status: outside this pass's files |
| Codex | 8 | For the lead | Progression fix report's deferred ownership bullet: outside this pass's files |
| Codex | For Cory | Collected | Time a week; the qualified community read |

Found in passing and fixed: every "confirmed in the unit plan's comparison table" cell in the three frames now reads
"Candidate: ..., checked in the unit plan's comparison table" (the plans do not exist yet; Codex grade 2 F3 named
the wording).

## Grade 1

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | ss1-group-roles hands on to ss3-taking-part; ss3-taking-part assumes it, and its Handoff kind sentence now names a readiness check on roles with a one-lesson reteach; grade 3 seam row updated; this frame's seam row and "six rows skip to grade 3" text updated |
| Expert | 2 | Applied | The flag and bald eagle explained again (row notes and unit 6) |
| Expert | 3 | Applied | Cross-subject row 1.NBT.B.3, made-up whole-dollar flyers within 20; lean added to ss1-goods-services and its notes |
| Expert | 4 | Applied | Stale frames.csv note rewritten; "For the lead" item 2 now records the group-roles link as done |
| Expert | settled | Applied | Whole-dollar prices; no Ghana in unit 6's places |
| Codex | 1 | Applied in part | Every symbol, phrase and song explained for meaning, with a supplied image, text or lyric excerpt as evidence (unit 6, the brief, row notes); the choice not to sing kept. Standards file clarification for the lead |
| Codex | 2 | Applied | Reading-level bullet keeps kindergarten's "who made it" question, teacher-supplied from the credit line |
| Codex | 3 | Applied | One respond day after each check |
| Codex | 4 | Applied | Same as expert 1 |
| Codex | 5 | Applied | Unit 3 check-set: California K.1.2 as review; the leader study anchored in MA.1.T1.4 |
| Codex | 6, 7, 8 | Applied | frames.csv stale notes in grade 1, kindergarten and grade 2 |
| Codex | 9 to 14 | For the lead | GLOSSARY (two lines), ROADMAP (lines 95, 118, 528), the progression fix report, the open-material report: outside this pass's files |
| Codex | For Cory | Collected | Time a week; the qualified community reader |

## Grade 2

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | Unit 7 menu of about 16 countries, at least two per inhabited continent outside the United States, each with its own source set; Ghana, Canada and Mexico left off; a family country welcome with teacher help. The country names are left to the unit plan |
| Expert | 2 | Applied, with Codex F2 | See conflict below |
| Expert | 3 | Applied | Seam lead-in points at the grade 3 frame; "Thread" and "Every unit" became 4, 5, 1, 1 and 7; column renamed "Grade 3 unit" |
| Expert | 4 | Applied | ss2-map-parts and ss2-make-map lean on math:1.MD.A.2; the frame's math table is now a grade 1 (year before) lean |
| Expert | 5 | Applied | D2.Geo.7's goods (unit 4) and ideas (unit 6) named in unit 5 and ss2-why-people-move notes |
| Expert | 6 | Applied | Stale lead items 3 and 4 and the seam sentence rewritten |
| Expert | settled | Applied | The country menu; the main street pair |
| Codex | F1 | Applied in part | Purposes of government, two countries compared by history, culture, language and way of governing, and "not every government is elected" (unit 4 and ss2-countries); unit 4's reason no longer says every country has elected government. Standards file for the lead |
| Codex | F2 | Applied, merged | Conflict: the expert settled one main street at two dates; Codex wants two world regions. Both are met by placing the physical pair in one region and the main street in a town of another world region, each at two dates, saying what changed and what stayed (ss2-climate-regions, unit 2, models table) |
| Codex | F3 | Applied | Opening order claim rewritten (resources and countries before migration, with the reason); every check-set cell marked Candidate with the codes Codex gave (California 2.2.2, 2.4.1, 2.3.2, 2.1.1; New York 2.1; Tennessee 2.10, 2.04, 2.11, 2.07 to 2.08, 2.01 to 2.02); unit 2's photographs and unit 5's island pairing labelled Curio Class choices. The Tennessee codes were not rechecked here; the unit plan's comparison table confirms them |
| Codex | F4 | Applied, wording mine | Unit 6 question "When people move to a new place, do they change the place more, or does the place change them more?"; the old question kept as a supporting question, with two more; modeled claim closing; no ranking of cultures, no private disclosure |
| Codex | F5 | Applied | Same as expert 4 |
| Codex | F6, F7 | Applied | frames.csv stale notes (grade 2, grade 1) |
| Codex | F8 to F12 | For the lead | GLOSSARY, ROADMAP status, APPROACH.md and ROADMAP layer 3 ELA wording, the progression fix report: outside this pass's files |
| Codex | note | Applied | MA.2.T2.1's features on each continent: unit 2's list now names features on all seven |
| Codex | For Cory | Collected | Time a week; K to 2 device assumption; the qualified community read |

## Progression changes (data/progressions/social-studies.csv, 14 rows)

| Row | Change |
|---|---|
| ssk-class-decision | Notes: a real classroom problem, look back after a week, plant name only a warm-up |
| ssk-national-symbols | Notes: spoken, teacher-led sort with picture bins, dates said by the teacher |
| ssk-sequence-time | Notes and words: full MA.K.T3.3b time words, an informational read-aloud |
| ssk-maps-globes | Notes: first look at two differently designed world maps (MA.K.T2.2 clarification) |
| ssk-goods-services-money | cross_subject math:K.CC.B.5; notes: tokens worth one, prices 1 to 5 |
| ss1-group-roles | hands_on ss3-taking-part; notes say so |
| ss3-taking-part | assumes adds ss1-group-roles; Handoff kind sentence covers both rows |
| ss1-national-symbols | Notes: flag and eagle again; meaning of every symbol, phrase and song with evidence |
| ss1-goods-services | cross_subject math:1.NBT.B.3; notes: made-up whole-dollar flyers within 20 |
| ss2-map-parts, ss2-make-map | cross_subject math:1.MD.A.2 in place of 2.MD.A.1 |
| ss2-climate-regions | Notes: cultural change in a town of another world region at two dates |
| ss2-countries | Notes: MA.2.T4.2 clarification in full; not every government is elected |
| ss2-why-people-move | Notes: D2.Geo.7's goods and ideas taught in units 4 and 6 |

Grade 3 frame: only the seam row for the dormant grade 1 civics rows changed (adds ss1-group-roles).

## For the lead (outside this pass's files)

- `data/standards/ma-hss-2018.txt`: widen MA.K.T3.3b (morning, afternoon, night, last or next week, month, year),
  MA.K.T2.2 (the clarification's differently designed maps), MA.1.T3.2c (meaning as well as recognition) and
  MA.2.T4.2 (purposes of government; history, culture, language, type of government).
- `docs/GLOSSARY.md` lines 52 and 53 (progression "planned", course frame "Not built"); `docs/ROADMAP.md` near lines
  95, 118 and 528 and the layer 3 ELA status; `docs/APPROACH.md` opening ELA sentence: the readers' replacement
  text is in Codex K 7, grade 1 9 to 12 and grade 2 F8 to F11.
- `progression-social-studies-fixes-2026-11-13.md` line 43 and the open-material report's open items: dated
  closure notes as Codex grade 1 13 and 14 give them.

## For Cory

- **Time a week (audience).** K two lessons of 20 to 30 minutes (64 days); grade 1 three of about 30 (96); grade 2
  three of 30 to 40 (96). Both readers: keep.
- **The qualified community read (people).** Native and hard-history content in all three grades needs a qualified
  reader before it goes live.
- **K to 2 device assumption (audience).** Codex grade 2 asks for it to be set before presentation and tool
  requirements are fixed.

## Settled (for docs/reviews/DIGEST.md)

| Choice | Course | Reason |
|---|---|---|
| Three on-the-day holiday lessons from unit 5's 11 days; the block placed by prerequisites, dates left to the scope and sequence | K | Careful notes arrive on the day; no false calendar promise |
| Kindergarten informed action is a real classroom problem with a look back | K | Adoption bar item 8 asks for a real problem |
| Class store tokens worth one, prices 1 to 5 | K | No coin values in kindergarten math |
| Unit 4 question "Which change from long ago made the biggest difference to everyday work?" | K | Keeps the claim inside the evidence studied |
| One respond day after each course check | K, 1, 2 | A cumulative check is followed by response; totals unchanged |
| Check-set cells are "Candidate: ..." until the unit plan checks them | K, 1, 2 | The plans do not exist yet |
| ss1-group-roles hands on to ss3-taking-part, dormant with a readiness check | 1, 3 | Closes the orphan civics thread |
| Grade 1 symbols explained for meaning with evidence, flag and eagle included | 1 | MA.1.T3.2 in full |
| Grade 1 flyers whole dollars within 20 | 1 | No money until grade 2 math |
| Grade 2 country menu of about 16, Ghana, Canada and Mexico off | 2 | Buildable source sets; avoids grade 3 and 4 picks |
| D2.Geo.10: physical change in one region, a main street in a town of another, each at two dates | 2 | Both halves of the indicator, in more than one region |
| Map-scale lean math:1.MD.A.2 | 2 | Matches repeated whole units |
| Unit 6 question "When people move to a new place, do they change the place more, or does the place change them more?" | 2 | Needs a conclusion from the unit's evidence |

# Frame read: english-language-arts-kindergarten (ELA, kindergarten), 2026-11-14

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/ela.md, docs/RUBRIC-ELA.md.
- The frame docs/courses/english-language-arts-kindergarten/frame.md and its row in data/plans/frames.csv
  (kindergarten, 4 units, 160 days). No data/plans/english-language-arts-kindergarten/source-map.csv exists; the
  frame's "## Source map" section is the map read here.
- The 29 kindergarten rows of data/progressions/ela.csv, and the grade 1 rows at the seam.
- The frame after, docs/courses/english-language-arts-grade-1/frame.md (no frame before kindergarten).
- Same-year frames: docs/courses/science-kindergarten/frame.md and docs/courses/social-studies-kindergarten/frame.md.
- docs/sources/BASE-TEXTS.md, docs/agents/decisions/DESK-ANSWERS.md (2026-11-12 card) and the base text itself,
  S:\CurioClass-sources\el-education-k5-2017, kindergarten: the curriculum map, module and unit overviews, the lesson
  file lists (counted lesson by lesson, combined files such as L14-15 counted as two), the Skills Block module and
  cycle overviews for cycles 1 to 25, the store's NOTES.md ("Skills Block answer") and
  licence/eleducation-terms-of-use-excerpt-2026-11-12.txt.
- docs/pipeline/briefs/frame-write.md, "Lessons from the social studies frames" (all 15 checked below).
- Gates: `python -X utf8 scripts/frame.py check english-language-arts-kindergarten` gives 0 failures (4 units, 160
  days, 154 in units, 6 for checks and respond days); `plan.py check` passes; `stale.py check` gives 0 failures.
- Standards are judged from my knowledge of the Common Core ELA standards (2010) and NGSS, not re-fetched.

## Verdict

This is a sound frame. The four EL kindergarten modules are kept in order (30 + 40 + 35 + 34 = 139 base lessons in
154 unit days), every kindergarten row sits once, and the foundations thread follows the 2017 Skills Block cycle by
cycle in the base text's own order (cycles 1 to 25 checked against the cycle overviews: an exact match). The
findings are small: some held base files are neither placed nor cut, the licence item is written as an open question
when the record already settles it, and the unit 1 check set names opinion writing the unit does not own.

## Findings, most serious first

### 1. The unit 1 check set names writing the unit does not own (moderate; firm)

**What is wrong.** Unit 1's check set lists "the toy preference writing" as a candidate, and the base text's module 1
does assess W.K.1 on a preferred toy. But ek-opinion (W.K.1) sits in unit 4, and the frame's own For the lead item 3
asks to move it to unit 1 through a row change. Until that row change is made, unit 1 checks a standard placed three
units later, and unit 4's opinion work reads as first teaching when it is the second.

**Why it matters.** A unit writer either drops the base text's module 1 opinion assessment or checks a row before its
placed unit, and the gate cannot see either. The rubric's order-of-first-teaching items read where W.K.1 first sits.

**Fix.** Take the lead's item 3 to Cory as written (it moves a standard between units, so it is his call). If he
says no, change the unit 1 check-set cell to "the toy preference talk (said aloud, as practice for unit 4's opinion)"
and drop the word "writing". LAYER frame and progression. REPEAT yes (the grade 3 read found rows later than the base
lessons that assess them).

### 2. Held base files are neither placed nor cut (minor; firm)

**What is wrong.** The source map places the module lessons, the Skills Block lessons and Learning Letters, and cuts
the Labs, videos and trade books. It does not place or cut: the decodable reader zips for Skills Block modules 3 and 4
(GKM3 and GKM4 Decodables, 7 readers each), the Skills Block cycle overviews and module overviews (the documents the
foundations order is read from), and the Skills Block reference documents in the store.

**Why it matters.** The brief asks for every base unit placed or its cut named. For the lead item 4 already picks
"adapt the 2017 decodables where their pictures are cleared", so the map should hold the row the pick points at.

**Fix.** Add two rows to the source map: "Skills Block decodable readers, modules 3 and 4 (14 readers) | All | 3 and
4 | Adapted where pictures are cleared; gaps written new (For the lead item 4)" and "Skills Block module and cycle
overviews, reference documents | All | 1 to 4 | Teacher-facing order and routines, read for the unit plans, not
carried as student pages". LAYER base text. REPEAT yes (the math frame reads had unplaced source files).

### 3. The licence item is settled fact, written as an open question (minor; firm)

**What is wrong.** For the lead item 2 frames the 2017 Skills Block licence as a pick the lead may rule against. The
record settles it. The store's licence/eleducation-terms-of-use-excerpt-2026-11-12.txt reads: "Except where otherwise
noted, the EL Education K-2 Reading Foundations Skills Block (2017 Edition) is licensed under ... (CC BY 4.0)", and
separately that the Reading Foundational Skills Block (2024 Edition) is CC BY-NC 4.0 (terms page last published
2026-05-07, read 2026-11-12). NOTES.md finds the CC BY 4.0 notice printed in the held 2017 files (23 supporting files
in GKM1_Skills.zip alone) and no NC line in any held file; the files are 2019 printings of the 2017 edition, and the
2024 Skills Block was never downloaded. BASE-TEXTS.md names the base text as the 2017 edition, CC BY 4.0, and lists
only "EL Education 2025 edition and Skills Block 2024: CC BY-NC" as never base texts; DESK-ANSWERS 2026-11-12 says the
same ("Never mix in the 2025 edition or Skills Block 2024"). The pass instruction that called the Skills Block CC
BY-NC was wrong for the edition held.

**Why it matters.** An open "if the lead rules it out" branch invites a later writer to rebuild the foundations block
without the base text for no reason. The real limits are the ones the terms page names: third-party content noted as
such, trade books, logos and videos (CC BY-NC-ND 3.0).

**Fix.** Rewrite item 2 as a settled line under the Base text bullet: "The 2017 K-2 Skills Block is CC BY 4.0 (EL's
terms page, read 2026-11-12, and the printed lines in the held files); only the 2024 Skills Block is CC BY-NC and it is
not held or used. Third-party items noted as such inside the Skills Block files are replaced." Drop the "if the lead
rules it out" branch. LAYER process. REPEAT yes (earlier reads found open questions the record had already closed).

### 4. Science's leans on ELA are not recorded from the ELA side (minor; likely)

**What is wrong.** The cross-subject table lists what ELA takes from science and social studies, and the social
studies leans on ELA are noted, but the science kindergarten frame's statements that ELA teaches SL.K.3, SL.K.5, W.K.1
and W.K.2 have no line here. I checked them: each is consistent with where this frame places those standards (W.K.2
in unit 1, SL.K.5 and SL.K.3 by unit 2, W.K.1 in unit 4, with science's opinion use after it).

**Why it matters.** Lesson 7 of the social studies list asks for both ends of every handoff. If a later edit moves
W.K.1 to unit 1 (finding 1), the science frame's timing still holds, but nobody reading this frame would know to
check.

**Fix.** Add one line under the cross-subject table: "Science kindergarten uses SL.K.3, SL.K.5, W.K.2 (from unit 1
and 2) and W.K.1 (unit 4, or unit 1 if the row moves); its frame states the same weeks." LAYER frame. REPEAT yes.

## Checked and found right (do not undo)

- Source map counts against the base: modules 1 to 4 have 30, 40, 35 and 34 lessons (M4U3 is 15 with the combined
  files counted). Skills Block cycles 1 to 4 are lessons 1 to 25, 5 to 11 are 26 to 60, 12 to 18 are 61 to 95, 19 to
  25 are 96 to 130. All match the frame.
- RF thread order against the cycle overviews: t, a; h, p; c, n; m, r; v, s; i, g; d, f, l; k, y; u, qu, x; b, o, w;
  j, z, e; sh, th, ch; CVC by vowel (a, i, u, o, e); review; digraph review; -am, -an; e and u review with spoken -ink,
  -ank; -ll, -zz, -ss, -ff; long a and i heard; long o and u heard; r-controlled. The frame's unit descriptions match.
  RF.K.1 to RF.K.4 are all reached in full by unit 4.
- The Labs cut has a reason that holds (finding on the 120-minute day under "120-minute day" below).
- Two checks, each with a respond day after; check-set cells start "Candidate:"; picks named; paper path; no student
  account; sensitivity notes on homes, toys and classmates' names are right for this age.
- Every cross-subject lean is coded as the row has it (7 of 7) and science and social studies teach the leaned skill
  first or the "if later" line covers it: K-ESS2-1 weather (science about weeks 5 to 10, ELA unit 2), K-LS1-1 (science
  unit 4, about weeks 16 to 22; ELA's ek-inform in unit 1 uses only animals' needs at the talk level and the "if later"
  line says so), K.MD.B.3 sorting done without counting ahead of math.

## The 120-minute day

The frame drops EL's Labs hour and keeps the module hour and the Skills Block hour. The base text's own curriculum
map says the Labs carry no formal assessment, though it calls them "a critical component". Every standard EL assesses
in kindergarten sits in a module lesson or a Skills Block lesson, and every one of them is placed here, so the
standards are taught in full. What is lost is practice volume: oral language through play, building and drawing.
Kindergarten has the most to lose from that cut, and the frame partly answers it by keeping the talk protocols in the
topic block every day. The real risk is the spare days: 154 unit days hold 139 module lessons, about 15 days of room
for the readiness check and Curio Class additions. That is enough. Judgment: the day holds.

## Seams

- No frame before. The kindergarten readiness check in week 1 sets the start.
- Kindergarten to grade 1: every kindergarten row hands on to a grade 1 row and the grade 1 frame names the same
  pairs (checked row by row in the seam tables). Grade 1 cycle 1 reviews the kindergarten Skills Block, which matches
  what this frame hands on.

## Cross-subject

Science kindergarten: K-ESS2-1 lands about weeks 5 to 10, inside ELA unit 2 (weather); the weather chart starts in
science week 1. K-LS1-1 (science unit 4, about weeks 16 to 22) feeds ek-inform and ek-shared-research; ELA's unit 1
use is at the talk level and the "if later" bridge names it. Social studies kindergarten: ssk-sequence-time,
ssk-i-think-because and ssk-talk-together are all taught in its weeks 1 to 3, before or with ELA's use. Math:
K.MD.B.3 sorting without counting ahead.

## Lessons from the social studies frames

1 respond day after each check: met. 2 "Candidate:" cells: met. 3 time a day stated: met (120 minutes, split
stated). 4 standards in full: met. 5 each thread starts where first used: missed once (finding 1). 6 "first" claims
checked: met. 7 both ends of every handoff: partly (finding 4). 8 "if later" lines: met. 9 days by load: met. 10
questions answerable from the unit: met. 11 picks named: met. 12 sensitivity reads: met. 13 no math ahead of math:
met. 14 paper path: met. 15 no status lines about other files: met, except the licence item written as open (finding
3).

## The lens checklist (course frame layer)

Met: every row once; base text followed in order; RF thread complete and in base order; text band and read-aloud
level; picks; sensitivity; paper path. Missed: the base's first opinion check against the row's unit (finding 1);
every base file placed or cut (finding 2). Not applicable: none.

## What I could not judge

- How a 120-minute day ships under docs/LESSON-DAY.md (one lesson page or two blocks with their own pages): that is
  settled at the step-3 pilot, not in the frame.
- The base text's published K-2 review criteria were not read; the rubric's growth items were read instead.
- Whether the EL decodables' pictures can be cleared: the unit plans judge each one.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| The 2017 Skills Block is CC BY 4.0 and is the foundations base; the 2024 one is CC BY-NC and never used | EL's terms page and the printed lines in the held files; BASE-TEXTS.md and DESK-ANSWERS agree | frame Base text, For the lead item 2 |
| Decodables and Skills Block overviews get source map rows | Every base file placed or cut | frame Source map |
| Labs cut stands | No formal assessment in the Labs; every assessed standard is in the kept hours | frame Source map |
| Science's ELA leans noted from the ELA side | Both ends of every handoff | frame Cross-subject |

## For the lead (row moves, through Cory)

- ek-opinion to unit 1 with the model_in change (the frame's own item 3); else the check-set wording in finding 1.

## For Cory

- Day length: kindergarten to grade 2 run 120 minutes of ELA, grade 3 runs 90. That step down is a real change for a
  family or school using the whole span: scope and audience.
- A qualified kindergarten ELA teacher to read the 22 replacement read-alouds and the decodables before use: people.

## Sources

From memory, not re-fetched: Common Core ELA (2010) kindergarten standards; NGSS kindergarten performance
expectations. EL Education K-5 2017 kindergarten from the repository copy (curriculum map, module, unit and Skills
Block overviews, lesson lists, terms-of-use excerpt). The rest from the repository files above.

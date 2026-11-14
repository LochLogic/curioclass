# Frame read: english-language-arts-grade-1 (ELA, grade 1), 2026-11-14

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/ela.md, docs/RUBRIC-ELA.md.
- The frame docs/courses/english-language-arts-grade-1/frame.md and its row in data/plans/frames.csv (grade-1, 4
  units, 160 days). No data/plans/english-language-arts-grade-1/source-map.csv exists; the frame's "## Source map"
  section is the map read here.
- The 31 grade 1 rows of data/progressions/ela.csv, and the kindergarten and grade 2 rows at the seams.
- The frames before and after: docs/courses/english-language-arts-kindergarten/frame.md and
  docs/courses/english-language-arts-grade-2/frame.md.
- Same-year frames: docs/courses/science-grade-1/frame.md and docs/courses/social-studies-grade-1/frame.md.
- docs/sources/BASE-TEXTS.md, docs/agents/decisions/DESK-ANSWERS.md (2026-11-12 card) and the base text,
  S:\CurioClass-sources\el-education-k5-2017, grade 1: the curriculum map, module and unit overviews, lesson file
  lists counted lesson by lesson (combined files counted as their range), the Skills Block module overviews and all 25
  cycle overviews, the decodables and Learning Letters zips, the module 4 crosswalk files, NOTES.md and the
  terms-of-use excerpt.
- docs/pipeline/briefs/frame-write.md, "Lessons from the social studies frames" (all 15 checked below).
- Gates: `python -X utf8 scripts/frame.py check english-language-arts-grade-1` gives 0 failures (4 units, 160 days,
  154 in units, 6 for checks and respond days); `plan.py check` passes; `stale.py check` gives 0 failures.
- Standards are judged from my knowledge of the Common Core ELA standards (2010) and NGSS, not re-fetched.

## Verdict

The placements are sound: the four EL grade 1 modules are kept in order (31 + 40 + 39 + 36 = 146 base lessons in
33, 42, 41 and 38 unit days), every grade 1 row sits once, and the foundations rows sit in units where their first
cycles fall. But the frame describes the Skills Block cycles wrongly in three of four units and in the source map, so
a unit writer following the text would teach blends, vowel teams and r-controlled vowels in the wrong units. The
source map also misnames three of four performance tasks, and the cross-subject table does not match the rows. Fix
the foundations descriptions first; they are the year's decoding order.

## Findings, most serious first

### 1. The foundations descriptions misstate the base cycles (major; firm)

**What is wrong.** The cycle overviews give this order: C1 review of kindergarten; C2 to C4 letters and sounds
re-taught (th, ch, sh; short a, i, u; qu); C5 o, b, j, w, x, p, g; C6 short e; C7 y as long i; C8 wh, -ck; C9
doubled finals and -ed; C10 l-blends; C11 final blends -lt, -ft, -st, -nt, -nd, -nk, -ng and "ou"; C12 and C13
closed syllables in two-syllable words; C14 open syllables; C15 to C18 CVCe; C19 r-controlled ar, or; C20 er, ir, ur;
C21 oa, ai, ea; C22 ai, ow; C23 oo, ee, y; C24 ie, igh; C25 two-syllable words with every syllable type. The
endings -s and -es come in C5 and -ing and -ed in C7 to C9.

The frame says otherwise:
- Unit 1: "review of short vowels and digraphs, then clusters and -ng, -nk (Skills Block cycles 1 to 4)". Clusters
  and -ng, -nk are C10 and C11, unit 2.
- Unit 3: "long vowels with silent e, the common vowel teams, then r-controlled vowels (cycles 12 to 18 ...)". C12 to
  C18 are closed and open syllables, then CVCe. r-controlled vowels are C19 and C20 and vowel teams C21 to C24.
- Unit 4: "review of all grade 1 patterns ... cycles 19 to 25". These cycles are new teaching: r-controlled vowels,
  five vowel-team cycles and two-syllable words with all types.
- Source map: Skills Block module 1 "Review, short vowels, clusters"; module 3 "Long vowels, vowel teams"; module 4
  "r-controlled vowels, two-syllable words, review" placed in "3 and 4". The unit day math puts cycles 19 to 25 in
  unit 4, not unit 3.

**Why it matters.** This is the course's decoding order. A unit 1 writer would teach blends before the short vowels
are re-secured; a unit 3 writer would write vowel-team decodables for cycles that teach syllables and silent e.
RF.1.3c (final -e and common vowel teams) is only taught in full in unit 4, where the frame says "review".

**Fix.** Replace the four foundations sentences with the cycle text above: unit 1 "review of kindergarten, then
letters and sounds re-taught with short a, i, u and digraphs th, ch, sh (cycles 1 to 4)"; unit 2 "remaining letters
and short o and e, y as long i, wh and -ck, doubled finals, l-blends and final blends with -ng and -nk, and endings
-s, -es, -ed, -ing (cycles 5 to 11)"; unit 3 "closed and open syllables in two-syllable words, then silent-e words
(cycles 12 to 18)"; unit 4 "r-controlled ar, or, er, ir, ur, the vowel teams oa, ai, ea, ow, oo, ee, y, ie, igh, and
two-syllable words with every syllable type (cycles 19 to 25)". Add "continued in unit 4 (vowel teams, RF.1.3c)" to
e1-long-vowels. In the source map: module 1 "Review, letters and sounds, short a, i, u, digraphs"; module 2 "Short o
and e, blends, endings"; module 3 "Closed and open syllables, silent e"; module 4 "r-controlled vowels, vowel teams,
two-syllable words", course unit 4. LAYER frame and base text. REPEAT new.

### 2. Performance tasks misnamed or changed without a reason (moderate; firm)

**What is wrong.** The base's curriculum map gives: M1 a tool made after "The Magnificent Thing" with an informational
piece about it; M2 "What the Sun Sees" narrative poems, revised; M3 an Expert Bird Riddle Card and a Scientific
Drawing matching game; M4 the Feathered Friend Saver (a window bird portrait with an informational paragraph). The
opinion is assessed in M4 unit 2 (the Pale Male nest debate, "Take the Nest Down!"). The source map gives M2 "a class
book about the sky", M3 "bird research" and M4 "an opinion on helping birds". The unit descriptions follow the source
map, and they part from the row notes for e1-narrative and e1-revise-publish (which name the poems) and e1-opinion.
The EL-written texts (for example "What's Best? The Debate About Pale Male's Nest" and "Birds are Human Helpers") are
CC BY and are not said to be adapted or replaced.

**Why it matters.** A changed end task changes what the unit's standards are checked on. W.1.3 through revised
narrative poems is the base's design; a class sky book checks W.1.7 more than W.1.3. The source map must say what is
kept and why anything is changed.

**Fix.** Rename the source map notes to the base tasks: M1U3 "Performance task: a tool and an informational piece
about it"; M2U3 "Performance task: narrative poems about the sun's day, revised (W.1.3, W.1.5)"; M3U3 "Performance
task: a bird riddle card and a scientific drawing game"; M4U2 "Opinion: whether the nest should come down (W.1.1)";
M4U3 "Performance task: a window bird portrait and an informational paragraph". If a unit keeps a different task,
add the reason in the Notes cell. Add "EL-written short texts adapted (CC BY), credited" to the M4 rows. LAYER base
text. REPEAT yes (earlier reads found changed base tasks without reasons).

### 3. The cross-subject table does not match the rows (moderate; firm)

**What is wrong.** The rows code: e1-connections 1-ESS1-1; e1-opinion ss1-claim-reasons; e1-informative 1-LS1-1;
e1-shared-research 1-LS1-1. The frame's table leaves out e1-informative's 1-LS1-1 lean, codes e1-shared-research as
1-ESS1-1, and gives e1-main-topic a lean its row does not have.

**Why it matters.** The table is where a unit writer learns what the science class has taught. The timing happens to
hold (science teaches 1-ESS1-1 in its unit 1, weeks 1 to 4, and 1-LS1-1 in its unit 2, about weeks 5 to 10, before
ELA's unit 2 research and unit 1's informative piece uses only plant and animal parts at the talk level), but the
codes must match the rows or the gate's later cross-subject check will fail.

**Fix.** Make the table four rows matching ela.csv: add e1-informative / 1-LS1-1 / unit 1 / science about weeks 5 to
10, with an "if later" line ("unit 1 names body parts and what they do from the unit's own texts; science's structure
and function comes after"); recode e1-shared-research to 1-LS1-1; drop the e1-main-topic line, or add the lean to the
row through the lead. LAYER frame. REPEAT yes.

### 4. Two standards named in part or mislabelled (minor; firm)

**What is wrong.** Unit 1 owns e1-word-relationships but its standards list stops short of L.1.5c (real-life
connections between words and their use), which the row owns. "A question to clear up what is not understood
(SL.1.2)" is labelled SL.1.2; asking questions to clear up confusion is SL.1.1c (in a conversation) and SL.1.3 (of a
speaker). SL.1.2 is asking and answering about key details in a text read aloud.

**Why it matters.** Lesson 4 of the list: standards in full. A unit plan built from the label teaches the wrong
standard.

**Fix.** Add L.1.5c to unit 1's standards and description ("words tied to real life: tools at home and school");
relabel the phrase "(SL.1.1c, SL.1.3)" and keep SL.1.2 on the key-details line. LAYER standard. REPEAT yes.

### 5. Held base files are neither placed nor cut (minor; firm)

**What is wrong.** The map does not place or cut the Skills Block decodables (modules 1 to 4), Learning Letters, or
the cycle and module overviews. It cuts the module 4 crosswalk files as "later-edition material": right (they are
2025-dated), but say they are not adapted at all.

**Why it matters.** For the lead item 4 picks "adapt the 2017 decodables"; the map should hold the row.

**Fix.** Add "Skills Block decodable readers, modules 1 to 4 | All | 1 to 4, by module | Adapted where pictures are
cleared; gaps written new", "Learning Letters | All | 1 | Handwriting review (L.1.1a)" and "Cycle and module overviews
| All | 1 to 4 | Teacher-facing order, not carried as student pages". LAYER base text. REPEAT yes.

### 6. The licence item is settled fact, written as an open pick (minor; firm)

**What is wrong.** For the lead item 2 is a pick. The record settles it: EL's terms page (excerpt in the store, read
2026-11-12) licenses "the EL Education K-2 Reading Foundations Skills Block (2017 Edition)" under CC BY 4.0 and only
the 2024 edition under CC BY-NC 4.0; the held files are 2019 printings of the 2017 edition with the CC BY line
printed and no NC line (NOTES.md); BASE-TEXTS.md and DESK-ANSWERS 2026-11-12 bar only the 2024 Skills Block.

**Fix.** Rewrite as a settled line under the Base text bullet (same wording as the kindergarten read's finding 3).
LAYER process. REPEAT yes.

### 7. Unit 4 is tight for what it carries (minor; judgment call)

**What is wrong.** Unit 4 has 38 days for 36 base lessons and adds the year's long text (two weeks), the opinion
through the process, e1-compare-two and the whole of L.1.1b to L.1.1i grammar, plus the five vowel-team cycles of
finding 1.

**Why it matters.** Two spare days cannot absorb a two-week long text. Either the long text crowds out base lessons
or grammar is rushed at the end of the year.

**Fix.** Move the long text's first week into unit 3 (41 days for 39 base lessons, also tight), or name which base
lessons in M4U1 the long text replaces. A unit-plan call; the frame should name it. LAYER frame. REPEAT yes (days by
load).

## Checked and found right (do not undo)

- Module lesson counts: M1 8 + 10 + 13 = 31; M2 15 + 12 + 13 = 40; M3 10 + 17 + 12 = 39; M4 9 + 10 + 17 = 36. Skills
  Block 130 lessons in 25 cycles. Unit edges follow the modules.
- Row placements for the foundations rows hold even though the descriptions do not: e1-short-vowels and e1-phonemes
  in unit 1, e1-inflections in unit 2 (C5 to C9), e1-syllables and e1-long-vowels in unit 3 (C12 to C18).
- The Labs cut, two checks with respond days, "Candidate:" cells, picks, paper path and sensitivity lines.
- The pourquoi tales retold in Curio Class words with credit and tradition readers named as a people question.

## The 120-minute day

Every standard EL assesses in grade 1 sits in a module lesson or the Skills Block, and all are placed here, so the
Labs cut does not leave a standard part-taught. The loss is practice volume (building, research play). Spare days are
thin: 154 unit days hold 146 module lessons, 8 days for the readiness check and every Curio Class addition, which is
why finding 7 matters. Judgment: the day holds for the standards; the load needs naming.

## Seams

- Kindergarten to grade 1: cycle 1 reviews the kindergarten Skills Block; every kindergarten handoff is picked up.
- Grade 1 to grade 2: grade 2's cycle 1 reviews all six syllable types, and its cycles 2 to 5 review long-vowel teams.
  That assumes grade 1 taught the vowel teams, which it does in cycles 21 to 24 (unit 4), not where this frame's text
  says. The rows match; the text needs finding 1's fix.
- The Models table: paragraph-frame introduced in e1-informative (unit 1). For the lead item 3 is right that
  e1-opinion's note should say "uses".

## Cross-subject

Science grade 1: 1-ESS1-1 (sun, moon and stars patterns) in its unit 1, weeks 1 to 4, before ELA unit 2; 1-LS1-1 in
its unit 2, about weeks 5 to 10, before ELA's unit 2 research. Science's statements that ELA teaches W.1.8, SL.1.5,
RI.1.2, W.1.2 and RI.1.1 all match this frame's units. Social studies grade 1: ss1-claim-reasons is taught by its unit
2, well before ELA's unit 4 opinion. Codes: finding 3.

## Lessons from the social studies frames

1 respond day after each check: met. 2 "Candidate:" cells: met. 3 time a day stated: met. 4 standards in full:
missed (finding 4; RF.1.3c by finding 1). 5 each thread starts where first used: met for rows, missed in the text
(finding 1). 6 "first" claims checked: met. 7 both ends of every handoff: met. 8 "if later" lines: met, one to add
(finding 3). 9 days by load: partly (finding 7). 10 questions answerable from the unit: met. 11 picks named: met. 12
sensitivity reads: met. 13 no math ahead of math: met. 14 paper path: met. 15 no status lines about other files: met,
except the licence item (finding 6).

## The lens checklist (course frame layer)

Met: every row once; module order kept; band; picks; sensitivity; paper path. Missed: the foundations order as
written (finding 1); base tasks kept or changed with a reason (finding 2); cross-subject codes (finding 3); standards
in full (finding 4). Not applicable: none.

## What I could not judge

- How a 120-minute day ships under docs/LESSON-DAY.md: settled at the step-3 pilot.
- The minute load of the vowel-team cycles with unit 4's added long text: needs a timed lesson.
- The base text's published K-2 review criteria were not read.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Foundations sentences and source map notes rewritten to the real cycles | Cycle overviews read one by one | frame units 1 to 4, Source map |
| Skills Block module 4 maps to unit 4 only | Unit day math and module order | frame Source map |
| Base performance tasks named as EL gives them | Curriculum map | frame Source map |
| 2017 Skills Block is CC BY 4.0, the 2024 one never used | Terms page, printed lines, BASE-TEXTS.md | frame Base text |
| Cross-subject table matches the rows | ela.csv cross_subject column | frame Cross-subject |
| SL.1.2 phrase relabelled SL.1.1c, SL.1.3; L.1.5c named | Standard wording | frame unit 1 |
| Pourquoi tale origins named exactly (an Efik and Ibibio tale of southern Nigeria, collected by Dayrell, 1910, for the sun and moon tale) rather than "West African" | Name the people and place, not a region | frame unit 2 |

## For the lead (row changes, through Cory)

- e1-opinion notes: "uses the paragraph-frame introduced in e1-informative" (the frame's own item 3).
- e1-main-topic: add a lean only if the lead wants one; else drop it from the table (finding 3).

## For Cory

- Day length: 120 minutes in kindergarten to grade 2, 90 in grade 3: scope and audience (same item in all three K-2
  reads).
- A qualified grade 1 ELA teacher for the 28 replacement texts and the decodables, and tradition readers for the unit
  2 tales: people.

## Sources

From memory, not re-fetched: Common Core ELA (2010) grade 1 standards; NGSS grade 1 performance expectations; Dayrell,
Folk Stories from Southern Nigeria (1910), for the sun and moon tale's origin. EL Education K-5 2017 grade 1 from the
repository copy (curriculum map, module, unit and cycle overviews, lesson lists, terms-of-use excerpt). The rest from
the repository files above.

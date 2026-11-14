# Frame read: english-language-arts-grade-2 (ELA, grade 2), 2026-11-14

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/ela.md, docs/RUBRIC-ELA.md.
- The frame docs/courses/english-language-arts-grade-2/frame.md and its row in data/plans/frames.csv (grade-2, 4
  units, 160 days). No data/plans/english-language-arts-grade-2/source-map.csv exists; the frame's "## Source map"
  section is the map read here.
- The 30 grade 2 rows of data/progressions/ela.csv, and the grade 1 and grade 3 rows at the seams.
- The frames before and after: docs/courses/english-language-arts-grade-1/frame.md and
  docs/courses/english-language-arts-grade-3/frame.md.
- Same-year frames: docs/courses/science-grade-2/frame.md and docs/courses/social-studies-grade-2/frame.md.
- docs/sources/BASE-TEXTS.md, docs/agents/decisions/DESK-ANSWERS.md (2026-11-12 card) and the base text,
  S:\CurioClass-sources\el-education-k5-2017, grade 2: the curriculum map, module and unit overviews, lesson file
  lists counted lesson by lesson, the Skills Block module overviews and all 26 cycle overviews (cycles 20 to 26 read
  with pymupdf: 21 to 26 KB of text each), the decodables, Learning Letters and crosswalk files, NOTES.md and the
  terms-of-use excerpt.
- docs/pipeline/briefs/frame-write.md, "Lessons from the social studies frames" (all 15 checked below).
- Gates: `python -X utf8 scripts/frame.py check english-language-arts-grade-2` gives 0 failures (4 units, 160 days,
  154 in units, 6 for checks and respond days); `plan.py check` passes; `stale.py check` gives 0 failures.
- Standards are judged from my knowledge of the Common Core ELA standards (2010) and NGSS, not re-fetched.

## Verdict

The module order and day counts are right (30 + 39 + 38 + 36 = 143 base lessons in 32, 42, 41 and 39 unit days) and
every grade 2 row sits once, but the frame needs fixes before the scope and sequence. The foundations text misstates
the Skills Block cycles in every unit, so new teaching in cycles 20 to 26 (the -ous and schwa patterns grade 3
assumes) is called "review". Unit 3's end product narrows W.2.7, SL.2.4 and SL.2.5 and drops the base's written
informative piece, which also breaks the grade 3 seam. The reading-band line and four cross-subject codes are wrong,
and one lead item claims a store fault that is not there.

## Findings, most serious first

### 1. The foundations descriptions misstate the base cycles (major; firm)

**What is wrong.** The cycle overviews give: C1 syllable-type review; C2 to C5 long-vowel team review; C6 r-controlled
review; C7 oi, oy, ou, ow and not-contractions; C8 ild, old, ind, ost; C9 1-1-1 doubling; C10 -ed's three sounds;
C11 oo, ou, ui, ue, ew; C12 -tion, -sion; C13 and C14 consonant-le; C15 -k, -ck, -ic; C16 -dge, -ge; C17 -ch, -tch;
C18 -ible, -able; C19 review and au, aw; C20 y to -ies; C21 schwa spelled a; C22 schwa spelled e and o; C23 -ate;
C24 compound words; C25 -cal, -cle; C26 -ous, -us. Prefixes un, re, de, dis, im and in are spread through the cycles.

The frame says:
- Unit 1: "long and short vowels reviewed and additional vowel teams (Skills Block cycles 1 to 5)". C1 to C5 only
  review; the additional teams RF.2.3b names are C7, C11 and C19 (units 2 and 3).
- Unit 3: "two-syllable words with long vowels and consonant-le ... cycles 13 to 19 continued". It leaves out -k,
  -ck, -ic, -dge, -tch, -ible, -able and au, aw.
- Unit 4: "review of every grade 2 pattern, cycles 20 to 26". These cycles teach -ies, schwa, -ate, compound words,
  -cal, -cle and -ous: new work.
- No "continued" line for e2-vowel-teams in units 2 and 3, nor for e2-tricky-spellings and e2-prefixes-suffixes in
  unit 3, though the cycles teaching them run there.
- Source map: module 1 "Review, vowel teams"; module 3 placed in "2 and 3"; module 4 "Review and fluency".

**Why it matters.** RF.2.3b is taught in full only when C7, C11 and C19 are taught, so e2-vowel-teams needs its
continued lines. Unit 4's "review" invites a writer to spend those 35 Skills Block lessons on fluency and lose the
schwa and suffix work. The grade 3 frame assumes grade 2 decoded -tion, -sion, -able and -ous.

**Fix.** Rewrite the four foundations sentences with the cycle text: unit 1 "syllable types, long-vowel teams and
r-controlled vowels reviewed (cycles 1 to 6)"; unit 2 "new vowel teams oi, oy, ou, ow and oo, ou, ui, ue, ew; ild,
old, ind, ost; doubling; -ed's three sounds; -tion, -sion; prefixes un, re (cycles 7 to 12)"; unit 3 "consonant-le,
-k, -ck, -ic, -dge, -ge, -ch, -tch, -ible, -able, au, aw (cycles 13 to 19)"; unit 4 "y to -ies, schwa spelled a, e,
o, -ate, compound words, -cal, -cle, -ous, -us (cycles 20 to 26), then end-of-year fluency". Add "continued in units 2
and 3 (new vowel teams, RF.2.3b)" to e2-vowel-teams and "continued in units 3 and 4" to e2-tricky-spellings and
e2-prefixes-suffixes. In the source map, rename module 1 "Review of syllable types and vowel patterns", module 4 "New
patterns: -ies, schwa, compound words, -ous", and give each Skills Block module one course unit, or name the reason it
splits. LAYER frame and base text. REPEAT new.

### 2. Unit 3's end product narrows three standards and breaks the grade 3 seam (major; firm)

**What is wrong.** Unit 3 owns W.2.7, SL.2.4 and SL.2.5. The frame's end task is a spoken research report, recorded.
W.2.7 is shared research that ends in writing (the base's M3 has students take research notes and write an
informative piece, then build a poster and give an oral presentation); the frame's unit 3 has no writing from the
research. SL.2.4 is telling a story or recounting an experience with facts and details; a research report is not what
it names. SL.2.5 is creating audio recordings of stories or poems and adding drawings to clarify ideas. The base's
written informative piece is dropped without a reason in the source map. The grade 3 frame's seam expects
e2-tell-and-record to hand on "recordings of stories or poems".

**Why it matters.** Three owned standards are taught in part (lesson 4 of the list), and grade 3 builds on a recording
skill grade 2 did not teach.

**Fix.** Keep the base's sequence: research notes into a written informative piece (W.2.7 with W.2.8), then a poster
and short talk. Add a second short product for SL.2.4 and SL.2.5: a story told from a pollinator's view, recorded as
audio, with the child's drawings. Name both in unit 3's description and check-set cell, and add to the M3U3 source map
row "Performance task kept: informative piece and presentation; recorded pollinator story added for SL.2.4, SL.2.5".
LAYER frame and standard. REPEAT yes (the codex progression read flagged an SL.2.5 gap).

### 3. The reading band is narrowed (moderate; firm)

**What is wrong.** The Texts line says students read "grade 2 texts and the low end of the grades 2 to 3 band on
their own", and the end-of-year check uses "a text at the low end of the grades 2 to 3 band". RL.2.10 and RI.2.10 ask
students by the end of the year to read and comprehend texts in the grades 2 to 3 band proficiently, with scaffolding
as needed at the high end.

**Why it matters.** The standard in full is the band, not its low end. A check at the low end cannot show the
standard met.

**Fix.** Replace with "By the end of the year students read texts in the grades 2 to 3 band proficiently, with
scaffolding at the high end" and in the check "a text in the grades 2 to 3 band read on their own". LAYER standard.
REPEAT yes (standards in full).

### 4. Four cross-subject codes do not match the rows (moderate; firm)

**What is wrong.** The rows code: e2-fables-folktales ss2-culture-migration; e2-compare-texts ss2-two-accounts;
e2-connections-series 2-LS2-2; e2-opinion ss2-claim-sources; e2-informative 2-LS2-1; e2-research 2-LS2-2;
e2-discussion ss2-family-interviews. The frame's table leaves out e2-informative / 2-LS2-1, codes e2-research
2-LS2-1, gives e2-main-topic-paragraphs a 2-ESS1-1 lean its row lacks, puts the social studies culture lean on
e2-images-and-text instead of e2-fables-folktales, and puts the interview lean on e2-tell-and-record instead of
e2-discussion.

**Why it matters.** The table tells a writer what the other class has taught. Timing mostly holds (science teaches
2-LS2-1 about weeks 23 to 27 and 2-LS2-2 about weeks 27 to 29; ELA's unit 1 informative piece needs an "if later"
line since it comes first; unit 3's research in about weeks 19 to 27 is near or before science's 2-LS2-2, which the
"if later" line must also cover).

**Fix.** Rebuild the table as the seven row leans above, each with its week and an "if later" line where ELA comes
first: e2-informative ("unit 1's piece is on schools; plant needs come from the unit's own text"), e2-research and
e2-connections-series ("pollination is taught in the unit's texts; science's model comes after"). Drop the
e2-main-topic-paragraphs lean or ask the lead to add it to the row. LAYER frame. REPEAT yes.

### 5. A lead item claims a store fault that is not there (moderate; firm)

**What is wrong.** For the lead item 4 says "the grade 2 module 4 cycle overviews give no text". They do: C20 to C26
extract to 21 to 26 KB of text each with pymupdf, and they are where finding 1's cycle list for module 4 comes from.
The other half of the item is true: grade-2/skills-block/module-4/Skills_G1M4_Module_Overview.zip is byte-identical
to the grade 1 file, so the grade 2 module 4 overview is missing.

**Why it matters.** The false half led the source map to describe module 4 from the rows, which is how cycles 20 to
26 came to be called review.

**Fix.** Rewrite item 4: "The store's grade-2/skills-block/module-4/Skills_G1M4_Module_Overview.zip is the grade 1
file (byte-identical); the grade 2 module 4 module overview is missing. The cycle overviews C20 to C26 are held and
read. Pick: fetch the grade 2 module overview at the next store refresh." LAYER process. REPEAT yes (stale or false
status notes).

### 6. Language standards named in part (minor; firm)

**What is wrong.** Unit 2 names L.2.2a as holidays and product names, dropping geographic names. L.2.2b is given as
greetings only; it is commas in greetings and closings of letters. L.2.4e loses "print and digital" glossaries and
beginning dictionaries.

**Fix.** Write them in full: "capitalize holidays, product names and geographic names (L.2.2a)", "commas in greetings
and closings of letters (L.2.2b)", "glossaries and beginning dictionaries, both print and digital (L.2.4e)". LAYER
standard. REPEAT yes.

### 7. One "first" claim in the Models table is wrong (minor; firm)

**What is wrong.** The Models table says paragraph-frame arrives "from e1-opinion". The grade 1 rows introduce it in
e1-informative (unit 1 of grade 1), and e1-opinion uses it.

**Fix.** Change to "carried from grade 1 (e1-informative)". LAYER frame. REPEAT yes.

### 8. Held base files are neither placed nor cut, and the licence item is open (minor; firm)

**What is wrong.** The map does not place or cut the Skills Block decodables (modules 1 to 4), Learning Letters or
the cycle overviews; it cuts the 2025-dated module 4 crosswalk, rightly. For the lead item 2 frames the 2017 Skills
Block licence as a pick, when EL's terms page (store excerpt, read 2026-11-12) licenses the 2017 edition CC BY 4.0
and only the 2024 one CC BY-NC 4.0, the held files print the CC BY line with no NC line (NOTES.md), and BASE-TEXTS.md
and DESK-ANSWERS 2026-11-12 bar only the 2024 Skills Block.

**Fix.** Add source map rows for the decodables ("Adapted where pictures are cleared; gaps written new"), Learning
Letters ("cursive is not a grade 2 standard; handwriting review only, optional") and the overviews ("teacher-facing,
not carried"). Rewrite item 2 as a settled line under the Base text bullet (same wording as the kindergarten read).
LAYER base text and process. REPEAT yes.

## Checked and found right (do not undo)

- Module lesson counts: M1 11 + 9 + 10 = 30; M2 12 + 12 + 15 = 39; M3 10 + 15 + 13 = 38; M4 12 + 11 + 13 = 36 (M4U3
  13 with combined files counted). The source map's per-unit lesson ranges match. Skills Block 130 lessons in 26
  cycles.
- The fossil narrative (M2) and the fables with an opinion on protecting pollinators (M4) follow the base tasks.
- Two checks with respond days, "Candidate:" cells, picks, paper path, sensitivity notes on unit 1 schools around the
  world and unit 4 tales.

## The 120-minute day

Every standard EL assesses in grade 2 sits in a module lesson or the Skills Block, and all are placed, so the Labs cut
leaves no standard part-taught by itself; finding 2's narrowing comes from the end-task change, not the time. Spare
days: 154 unit days for 143 module lessons, 11 for the readiness check and Curio Class additions. Adding the recorded
story in unit 3 (finding 2) costs about 2 days inside its 41 for 38. Judgment: the day holds.

## Seams

- Grade 1 to grade 2: grade 2's C1 to C6 review grade 1's syllable types, vowel teams and r-controlled vowels, which
  grade 1 teaches (in units 3 and 4, per the grade 1 read's finding 1). Every grade 1 handoff is picked up.
- Grade 2 to grade 3: grade 3 assumes -tion, -sion (C12, unit 2), -able (C18, unit 3) and -ous (C26, unit 4), and
  "recordings of stories or poems" from e2-tell-and-record. The first three are in the base once finding 1's text is
  fixed; the last needs finding 2.
- Day length: grade 3 assumes a 90-minute block; this frame runs 120. See For Cory.

## Cross-subject

Science grade 2: 2-ESS1-1 in its unit 2 (about weeks 5 to 12), with ELA's fossil unit 2 (about weeks 7 to 15),
roughly together; science's statements that ELA teaches W.2.8 and RI.2.3 match this frame. 2-LS2-1 and 2-LS2-2 come
late in science (weeks 23 to 29); see finding 4 for the "if later" lines. Social studies grade 2: ss2-culture-migration,
ss2-two-accounts, ss2-claim-sources and ss2-family-interviews are taught in its first half, before ELA's units 1 and
4. Sensitivity: the hummingbird tale's origin is attributed variously in print, so the frame should credit it with
care; the lizard and sun tale must be retold from the traditional Mexican tale and not from Alma Flor Ada's
copyrighted picture book.

## Lessons from the social studies frames

1 respond day after each check: met. 2 "Candidate:" cells: met. 3 time a day stated: met. 4 standards in full:
missed (findings 2, 3, 6). 5 each thread starts where first used: missed in the text (finding 1). 6 "first" claims
checked: missed once (finding 7). 7 both ends of every handoff: missed at the grade 3 seam (finding 2). 8 "if later"
lines: missed for the late science leans (finding 4). 9 days by load: met. 10 questions answerable from the unit: met.
11 picks named: met. 12 sensitivity reads: met, with two notes (Cross-subject). 13 no math ahead of math: met. 14
paper path: met. 15 no status lines about other files: missed (finding 5).

## The lens checklist (course frame layer)

Met: every row once; module order kept; picks; sensitivity; paper path. Missed: foundations order as written (finding
1); standards in full (findings 2, 3, 6); the band (finding 3); cross-subject codes (finding 4). Not applicable: none.

## What I could not judge

- How a 120-minute day ships under docs/LESSON-DAY.md: settled at the step-3 pilot.
- The grade 2 module 4 Skills Block module overview: not held (finding 5); the cycle overviews were enough to check
  the order.
- The base text's published K-2 review criteria were not read.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Foundations sentences, continued lines and source map notes rewritten to the real cycles | Cycle overviews C1 to C26 read | frame units 1 to 4, Source map |
| Unit 3 keeps the written informative piece and adds a recorded pollinator story with drawings | W.2.7, SL.2.4, SL.2.5 in full; grade 3 seam | frame unit 3, Source map |
| Band line written as the standard says | RL.2.10, RI.2.10 | frame Texts, check after unit 4 |
| Cross-subject table matches the seven row leans | ela.csv | frame Cross-subject |
| Lead item 4 rewritten: cycle overviews hold text; only the module overview is mislabelled | Files read | frame For the lead |
| 2017 Skills Block is CC BY 4.0, the 2024 one never used | Terms page, printed lines, BASE-TEXTS.md | frame Base text |
| L.2.2a, L.2.2b, L.2.4e written in full; paragraph-frame credited to e1-informative | Standard wording; grade 1 rows | frame unit 2, Models |
| Lizard tale retold from the tradition, not the picture book; hummingbird tale credited with care | Copyright; contested attribution | frame unit 4 |

## For the lead (row changes, through Cory)

- e2-main-topic-paragraphs: add the 2-ESS1-1 lean to the row only if wanted; else drop it from the table.

## For Cory

- Day length: 120 minutes in kindergarten to grade 2, 90 in grade 3: scope and audience (same item in all three K-2
  reads).
- A qualified grade 2 ELA teacher for the 20 replacement texts, and readers from or expert in the cultures of the unit
  1 school texts and unit 4 tales, with any pay: people and money (the frame's own item 3).

## Sources

From memory, not re-fetched: Common Core ELA (2010) grade 2 standards; NGSS grade 2 performance expectations. EL
Education K-5 2017 grade 2 from the repository copy (curriculum map, module, unit and cycle overviews, lesson lists,
terms-of-use excerpt). The rest from the repository files above.

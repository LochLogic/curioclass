# Expert cold read: course frame, English Language Arts Grade 11 (2026-11-14)

Reader: the curriculum expert (fresh agent, docs/agents/EXPERT.md), on docs/pipeline/briefs/frame-read.md with
{course} = english-language-arts-grade-11, {subject} = ela. I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/ela.md, docs/RUBRIC-ELA.md, docs/pipeline/briefs/frame-read.md and
  frame-write.md (with its "Lessons from the social studies frames" list).
- The frame, docs/courses/english-language-arts-grade-11/frame.md, and its row in data/plans/frames.csv (9 units,
  160 days). No base text, so no source map.
- Every grade 11 row (and every grade 12 row, for the hand-on) of data/progressions/ela.csv, notes in full; the
  e10 rows the seams cite.
- The neighbouring frames: english-language-arts-grade-10 (before) and english-language-arts-grade-12 (after); for
  repeats, every other ELA frame searched for each of this year's titles and authors.
- The same-year and partner frames: us-history-i (whole), us-government-and-politics (units and ELA lean table).
- The 11-12 band text in data/standards/ccss-ela-standards-full.txt, every lettered part.
- docs/agents/decisions/DESK-ANSWERS.md, the 2026-11-12 and 2026-11-13 ELA entries (base texts; "recognizable and
  recent", no library or paid copy).
- Gates: `python -X utf8 scripts/plan.py check` (no failures), `python -X utf8 scripts/frame.py check
  english-language-arts-grade-11` (0 failures: 9 units, 160 days, 148 in units, 12 for checks),
  `python -X utf8 scripts/stale.py check` (55 files, 0 failures). I spent the read on what they cannot see.
- One outside check: the LibriVox catalogue (below, Sources).

Not opened, as instructed: docs/courses/ela-6/, docs/ela-6-spine.md, docs/NEXT-SPINES.md, the ela-6 and reconcile
reviews, and S:\CurioClass-sources\_calibration.

## Verdict

The frame is sound and close to ready: every grade 11 row sits in one unit, the order follows US History I where
the texts lean on history, the two long books and Trifles are read whole, the Douglass and founding-document picks
match the US History I frame, and 14 of the 15 social studies lessons are met. The biggest risk is in the standards
and the rules rather than the order: the eighteenth-century part of RL.11-12.9 has no literary text, and the research
and word work quietly lean on a library catalogue and paid references the rules forbid. The one change that matters
most is to add an eighteenth-century literary pair (Wheatley's poems and Occom's narrative, settled below), which also
brings the year's first Native author into an American literature course.

## Findings, most serious first

### 1. RL.11-12.9: the eighteenth-century part has no literary text (LAYER standard; REPEAT yes)

**What is wrong.** RL.11-12.9 asks for knowledge of "eighteenth-, nineteenth- and early-twentieth-century
foundational works of American literature". The frame gives grade 11 "the eighteenth and nineteenth centuries"
(unit 6), and grade 12 only looks back to grade 11's texts. But unit 6's period work uses The Scarlet Letter,
'Self-Reliance', 'Young Goodman Brown' (all nineteenth century) and Winthrop (1630, seventeenth). The year's
eighteenth-century texts are all read for RI (Paine, the Declaration, Wheatley's letter) or for irony (Franklin's
'Rules', unit 9). The row e11-lit-american-periods names "revolutionary writing (Franklin, Wheatley's poems)"; the
poems were dropped.
**Why it matters.** A standard taught to its headline only (lesson 4); grade 12 assumes the span is done. An adoption
reader checking the band would find no eighteenth-century literature compared anywhere.
**Fix.** In unit 3, beside Wheatley's letter to Occom, read two short literary texts of the same years: Wheatley's
'On Being Brought from Africa to America' (1773) and Samson Occom's 'A Short Narrative of My Life' (written 1768);
both public domain, about 2,000 words together (settled below). In unit 6's RL.11-12.9 cell, add "the eighteenth
century: Wheatley's poem and Occom's narrative (read in unit 3) compared on faith and how each writer is treated",
and the across-periods line keeps Winthrop against Hawthorne. One day moves into unit 3 (see finding 3 for where days
come from). Confidence: firm (the standard's text; the row's own named texts).

### 2. Research and word work lean on a library and on paid references (LAYER frame; REPEAT yes)

**What is wrong.** The brief says "No student is sent to a library or a paid copy" (Cory, 2026-11-13), yet unit 4
gathers sources from "the library catalogue" and the paper path bullet says "research uses open archives and the
school library's own access". L.11-12.4c and the routine rely on "a historical dictionary" unnamed (the obvious one,
the OED, is paywalled); L.11-12.1b on "a usage guide" unnamed (the standard's own examples, Merriam-Webster's
Dictionary of English Usage and Garner's, are paid books); unit 4 cites by "one open style guide", although grade 10
fixed one style for all four high school years (the Curio Class style sheet in the MLA core-elements format, with the
US GPO Style Manual).
**Why it matters.** A writer building days will send students to tools a free, no-account course cannot assume; the
citation thread breaks its one wording across the grade 10 seam (lesson 6).
**Fix.** Brief, paper path bullet: replace "research uses open archives and the school library's own access" with
"research uses open archives (the Library of Congress, Chronicling America, HathiTrust full-view, the Internet
Archive, government sites); a school's own databases are an extra, never required". Unit 4: replace "the library
catalogue" with "a full-text archive search". Unit 4: replace "one open style guide for citation, used all year" with
"the Curio Class style sheet (MLA core-elements format) and the US GPO Style Manual, as in grades 9 and 10". Name the
references (settled below): Webster's 1828 American Dictionary and the Online Etymology Dictionary for old meanings;
Fowler's A Dictionary of Modern English Usage (1926, US public domain) as the usage guide, beside a free current
dictionary's usage notes. Confidence: firm.

### 3. Unit 4's days do not hold what it promises, and its weeks disagree with US History I (LAYER frame; REPEAT yes)

**What is wrong.** Unit 4 has 20 days. Inside them: a readiness task, a three-day short project, "the four-week
project" (20 days on its own), a 1,500-word essay, a six-minute talk, an informal talk, the end-of-unit assessment and
respond time. The row e11-research names a four-week project. The arithmetic leaves about 15 project days, three
weeks, the same as grade 10's "three-week" project, so the claimed climb is not there. The frame also gives the shared
brief as history's "weeks 13 to 15" (unit 4 cell and the cross-subject table), while US History I picks weeks 12 to 15.
**Why it matters.** A scope and sequence writer will either cut the project to three weeks or overrun the unit; the
shared calendar with history starts a week apart.
**Fix.** Unit 4: 20 to 23 days; unit 7 (one row, RL.11-12.4, on short poems): 13 to 10 days. The total stays 160.
Write the shared brief as weeks 12 to 15 in both places. Unit 3 gains its one day for finding 1 from unit 1 (17 to
16; it starts the routines on four short texts) if the writer prefers not to touch unit 7 twice. Confidence: likely.

### 4. W.11-12.6 and SL.11-12.5: the paper path is written as if it met the technology standards (LAYER standard; REPEAT yes)

**What is wrong.** Units 2 and 3 publish "to a shared class page (paper path: a posted copy and the class binder)";
unit 4 presents with "slides or a handout". W.11-12.6 asks students to use technology, including the Internet, to
publish and update; SL.11-12.5 asks for strategic use of digital media. A posted paper copy meets neither. Grade 10
says this plainly ("a room without devices ... does not meet W.9-10.6, and the plan records the standard
unfinished").
**Why it matters.** Grade 11 starts both codes (~); the frame should not teach a teacher that the paper path covers
them, and the thread should keep grade 10's honest wording.
**Fix.** Brief, "Paper path and accounts": add "W.11-12.6 and SL.11-12.5 are met on a shared device or lab session in
the school day with the school's own tools, posted by the teacher, no student account; the paper path keeps every
student working but leaves those two codes unfinished, and the plan records it, as in grade 10." Confidence: firm.

### 5. The writing calendar breaks US History I's two requests (LAYER frame; REPEAT yes)

**What is wrong.** US History I asks that "ELA 11 process essays should not fall due in weeks 12 to 19" and that "ELA
11 keeps a due date out of its last week" (its unit 9, weeks 28 to 31, holds the empire report). The frame writes the
first as "weeks 13 to 19" and sets the narrative due "about week 31".
**Why it matters.** The two longest pieces of the spring land in the same week for a student taking both.
**Fix.** Brief, process calendar: "None falls due in weeks 12 to 19 except the shared research piece". Narrative due
at the end of week 30 (settled below); week 31 holds the interpretations lessons and the end-of-unit assessment.
Confidence: firm (both frames' text).

### 6. Who wrote the texts: no Native, Latino or Asian American author in an American literature year (LAYER frame; REPEAT new)

**What is wrong.** Rubric 2e (reported in words) asks who is in the texts and who wrote them. The year's authors are
white New Englanders and Southerners, Black writers (Wheatley, Douglass, Truth) and two white women's voices (Chopin,
Gilman, Glaspell). Unit 3 reads the Declaration's words on Native peoples "with Native nations' answer" but names no
text (lesson 11, picks named). The independent shelf has no Native, Latino or Asian American writer, although public
domain works exist.
**Why it matters.** The course is the band's survey of American literature; the gap is visible to any adoption
reader and to students.
**Fix.** Finding 1 adds Occom (Mohegan). Name unit 3's Native answer: William Apess, 'An Indian's Looking-Glass for the
White Man' (1833), an excerpt of about 1,500 words (settled below; the Native reader the frame already names confirms
it). Add to the shelf: Sui Sin Far, Mrs. Spring Fragrance (1912) and María Amparo Ruiz de Burton, The Squatter and the
Don (1885). Confidence: likely.

### 7. Unit 8 needs a community reader it does not name (LAYER frame; REPEAT yes)

**What is wrong.** How the Other Half Lives has whole chapters on Jewish, Chinese and Italian New Yorkers written in the
stereotypes and slurs of 1890. The unit's last column handles it well (lines read as evidence of Riis's view, slurs
marked), but the brief's "Sensitivity reads" names only units 3, 5 and 9.
**Fix.** Add unit 8 to the sensitivity line: "a reader from the immigrant communities Riis describes (Jewish, Chinese,
Italian American)". Who, and any pay, is Cory's. Confidence: likely.

### 8. Unit 9 is gathered by a skill, not a topic (LAYER frame; REPEAT new; judgment call)

**What is wrong.** "Saying one thing and meaning another: satire and realism, 1773 to 1916" and its question ("How do
Franklin, Twain, Chopin, Gilman and Glaspell make a reader see what their characters miss?") name a reading move and a
150-year span. The lens names this as a frame error ("a unit is named by a skill or a broad theme"), and rubric 2d
counts only specific topics. Three of the five texts already share one: women's lives inside marriage, 1892 to 1916
(Chopin, Gilman, Glaspell).
**Fix.** Retitle: "Inside the marriage, 1892 to 1916: Chopin, Gilman and Glaspell"; question: "What do these three
writers show about a wife's life that the men around her do not see?" (answerable from the three texts and the play's
two versions). Keep Franklin and 'The War Prayer' as the unit's irony lessons, named as a short satire pair beside US
History I's war weeks. No row moves. Confidence: judgment call.

### 9. Models table: citation is used before its first-use unit (LAYER frame; REPEAT yes)

**What is wrong.** "citation: unit that first uses it here: Unit 4". Unit 2's informative essay is built from three
sources, and unit 3's argument quotes "two other sources"; both need quotation and citation.
**Fix.** citation: first use "Unit 2 (quotations in the informative essay)", used again "3, 4, 6, 9", with the grade 10
style sheet retrieved there (lesson 5). Confidence: firm.

### 10. The seminar seam: endorse the row change, but grade 11 still steps back on roles (LAYER progression; REPEAT yes)

**What is wrong.** For the lead 2 is right that e12-seminar's note ("rotating roles set by the teacher") contradicts
e10-sl-seminar ("set their own rules and roles"). But the frame's own unit 1 gives students "named roles that rotate
(opener, prober, synthesizer)", which is still less than grade 10's students setting roles. SL.11-12.1b ("set clear
goals and deadlines, and establish individual roles") is not started anywhere this year.
**Fix.** Unit 1: "seminars run by students, who choose roles from a named set (opener, prober, synthesizer) or make
their own, and set the seminar's goal (SL.11-12.1b started)". e12-seminar row text as the frame proposes, with "named
rotating roles" read as "roles chosen from a named set". Confidence: likely.

### 11. Shelf overlaps grade 12 (LAYER frame; REPEAT yes)

The Age of Innocence is on both the grade 11 and grade 12 shelves. Fix: keep it in grade 12 (its 1920 date fits grade
12's twentieth-century span) and drop it here; Sui Sin Far (finding 6) takes its place. Confidence: firm.

## What is right and should not be touched

- The Douglass timing (history's excerpts in weeks 11 to 15, the whole Narrative right after) and the founding
  documents a month apart, one lens each: both frames agree.
- Trifles as the band's American play, read whole; the slur in chapter 6 of the Narrative marked and never read aloud.
- The supports bullet (before, during, after; audio beside, never in place of, the text; fading from unit 6).
- Every unit's "if later" line in the US History I calendar (lesson 8), the respond days after each check (lesson 1),
  the stated 50-minute day (lesson 3) and "Candidate:" on every check-set cell (lesson 2).
- The cross-subject math lean: two-way tables from Algebra 1, reading only, nothing computed (lesson 13).

## Lessons from the social studies frames (frame-write.md)

| # | Lesson | Result |
|---|---|---|
| 1 | Respond day after each check | Met (1, 1 and 2) |
| 2 | Check-set cells start "Candidate:" | Met |
| 3 | Time a day stated | Met (five 50-minute lessons, home reading named) |
| 4 | Standards in full | Missed: RL.11-12.9's eighteenth century (finding 1); parts left to grade 12 named for RL.4, RL.7, RI.8 |
| 5 | Each thread starts where first used | Missed once: citation (finding 9) |
| 6 | "First" claims and one wording | Missed: the style sheet's wording (finding 2) |
| 7 | Both ends of every handoff | Met (the seminar row change, finding 10 refines it) |
| 8 | "If later" lines | Met |
| 9 | Days by load | Missed: unit 4 (finding 3) |
| 10 | Questions answerable from the unit | Met, unit 9's reworded in finding 8 |
| 11 | Picks named | Missed once: unit 3's Native answer (finding 6) |
| 12 | Sensitivity reads | Missed once: unit 8 (finding 7) |
| 13 | No math ahead of math | Met |
| 14 | Paper path, no account | Met for access; the paper path's limits on W.6 and SL.5 not said (finding 4) |
| 15 | No status lines about other files | Met |

## The lens checklist (course frame layer)

| Line | Result |
|---|---|
| A unit named by a skill or broad theme | Missed for unit 9 (finding 8); the other eight are named by topic and texts |
| Anchor texts on file with measure, qualitative reason and place | Met in the frame; the text records (texts.csv) come with the first ELA pilot plan, as data/plans/README.md says |
| Texts lean to one era, tradition or kind | Era: the standards fix this year to 1620 to 1916, a reason given. Tradition: missed (finding 6). Kind: met (two novels, a play, poems, speeches, essays, documents) |
| No long text read whole | Met: The Scarlet Letter, the Narrative, Trifles, and the independent book |

## Other checks

- **Owned skills.** All 30 grade 11 rows placed once; no unit teaches another grade's row except as named review. Gate
  agrees.
- **Days.** 160 = 148 + 12; the weeks in the Units table add up (unit 9 ends day 155, week 31). Unit 4 short, unit 7
  long (finding 3).
- **Text picks.** All public domain (1930 or earlier) or US government works; no repeat of another grade's anchor
  except the Declaration (grade 10, a different lens, acknowledged in both frames) and 'Owl Creek' (grade 9 moved off
  it, acknowledged). Informational share by unit days about 55 percent (units 2, 3, 4, 5, 8), literature 45, as the
  brief says "about half". Reading levels placed with reasons (the Narrative at about 1080 for its qualitative demand).
- **Seams.** Grade 10 to 11: every hand-on picked up; the style sheet thread broken (finding 2). Grade 11 to 12: every
  row hands to the grade 12 row of the same standard, and the grade 12 frame's "Picked up" table matches it row for
  row.
- **US Government.** If Government runs in grade 11, its unit 2 sits in weeks 2 to 3 of either half (year weeks 2 to 3
  or 18 to 19), never in ELA unit 3's weeks 8 to 11, so the "not in the same month" request is met either way; the
  cross-subject line may say so.
- **Not logged in the defects ledger:** the brief and caller limit me to this report; the caller may log the findings
  with `scripts/plan.py defect`, found_by `expert`.

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| Eighteenth-century literary pair: Wheatley, 'On Being Brought from Africa to America' (1773), and Samson Occom, 'A Short Narrative of My Life' (1768), read in unit 3 beside the Wheatley letter, compared in unit 6 | Completes RL.11-12.9's span with the row's named Wheatley and the letter's own recipient; short and public domain | Frame units 3 and 6; e11-lit-american-periods notes |
| Unit 3's Native answer: William Apess, 'An Indian's Looking-Glass for the White Man' (1833), excerpt | A Pequot writer answering the founding's equality claims in its own terms; public domain; the Native reader confirms | Frame unit 3 |
| Trifles' two versions: the LibriVox dramatic reading (multi-reader cast) and a live in-class staged reading of the chosen scene; a school production where one exists | RL.11-12.7 counts "recorded or live production"; no recording needs making, so For the lead 5 becomes optional | Frame unit 9, For the lead 5 |
| References: Webster's 1828 American Dictionary and the Online Etymology Dictionary (old meanings); Fowler's A Dictionary of Modern English Usage (1926) beside a free current dictionary's usage notes (usage); the Curio Class style sheet and the GPO Style Manual (citation, spelling) | Free, no account; Fowler itself shows usage changing (L.11-12.1a) | Frame brief and units 1, 3, 4 |
| Narrative due at the end of week 30 | Keeps US History I's last week clear | Frame brief, unit 9 |
| Shelf: drop The Age of Innocence (grade 12 keeps it); add Sui Sin Far, Mrs. Spring Fragrance (1912), and Ruiz de Burton, The Squatter and the Don (1885) | No shelf repeat; wider authorship | Frame brief |

## For Cory

- **People.** Unit 8 adds a reader from the immigrant communities Riis describes (finding 7), beside the readers
  already named for units 3, 5 and 9. Who, and any pay, is yours.
- **Recordings.** With the LibriVox Trifles and a live class staging, no Curio Class recording is needed for grade 11;
  For the lead 5 becomes a nice-to-have, not a need.
- **ELA check set** (For the lead 6): naming the college-level English frameworks and New York's Next Generation 11 to
  12 standards as the ELA 9 to 12 check set is a scope choice; I agree with the pick.

## What I could not judge

The computed measures (no texts.csv yet); whether 'The War Prayer' first printing is 1916 or 1923 (public domain either
way); the qualified reader's view of the Apess and Occom picks.

## Sources

- data/standards/ccss-ela-standards-full.txt: the 11-12 band, every lettered part (findings 1, 4).
- LibriVox catalogue API, https://librivox.org/api/feed/audiobooks/?title=Trifles&format=json : read 2026-11-14; lists
  "Trifles" by Susan Glaspell as a dramatic reading with a cast (settled row 3).
- docs/RUBRIC-ELA.md (EdReports 6-12 criteria in our words): 2a, 2d, 2e (findings 6, 8).
- From memory, to check before a unit rests on them: the public-domain status of Fowler (1926) and Occom's and
  Apess's texts; Wikipedia-level dates for 'The War Prayer'.

## For the source list

- The LibriVox catalogue API (above) answers "is there a public-domain recording of X" in one fetch, with no account.

## Confidence

Finding 1 firm; 2 firm; 3 likely; 4 firm; 5 firm; 6 likely; 7 likely; 8 judgment call; 9 firm; 10 likely; 11 firm.

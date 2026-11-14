# Frame read: us-history-i (US History I, 1763 to the First World War, grade 11), 2026-11-13

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/social-studies.md, docs/courses/social-studies/STANDARD.md (sections 1 to
  4), docs/sources/BASE-TEXTS.md (Since Time Immemorial as a partial base).
- The frame docs/courses/us-history-i/frame.md and its row in data/plans/frames.csv (`us-history-i,9,160`). No source
  map: no base text, only a partial base not mapped lesson by lesson, as allowed.
- All 27 us1-* rows of data/progressions/social-studies.csv; the NML rows across the high school courses.
- The anchor: every MA.USI line of data/standards/ma-hss-2018.txt, and the MA.NML lines.
- Frames before, beside and after: docs/courses/world-history-ii/frame.md and world-history-i/frame.md,
  docs/courses/civics-government-and-civic-life/frame.md (grade 8 "handed on" table), docs/courses/us-history-ii/frame.md
  (its "Picked up" table and the grade 12 timetable), docs/courses/us-government-and-politics/frame.md and
  docs/courses/economics/frame.md (grade 11 or 12, beside this course).
- The ELA 11 rows named (e11-*): each exists in data/progressions/ela.csv. No ELA 11 frame exists yet.
- Earlier reads: docs/reviews/progression-social-studies-2026-11-13.md (its settled skill links), the Codex read and
  fixes, docs/reviews/frame-us-history-ii-2026-11-13.md and frame-us-government-and-politics-2026-11-13.md.
- Gates: `python -X utf8 scripts/plan.py check` (frame us-history-i: 0 failures; 9 units, 160 days, 148 in units, 12
  checks and respond days). `python -X utf8 scripts/stale.py check`: 19 files, 0 failures.

## Verdict

The frame is sound: every USI code and the seven NML codes placed here sit in a unit, the units run in time order with
a reason for the thematic unit 4, the seams to grades 5, 8, 9 and 10 and to US History II match row for row, and the
removal, slavery, Jim Crow and boarding school content is plain, sourced and guarded. The biggest risk is unit 9: in
16 days it asks for a research report, the year's third several-page argument, a structured debate, a news-reading
routine and the whole American war. The one change that matters most is to make the empire research report and the
third argument one product.

## Findings, most serious first

### 1. Unit 9 asks for three products in 16 days (moderate; likely)

**What is wrong.** Unit 9 holds us1-empire (a survey of nine options, then "a research report on one case" with maps
and timelines), us1-news-reading (news against opinion, lateral reading, the 1898 Maine coverage and one current
site), us1-wwi (five codes and "a structured class debate on joining the League"), and, by the C3 column and
us1-argument-writing, "the third several-page argument (the empire or League debate)". Read as a writer would, that is
a report, an essay and a debate. A count: survey 2, report 4 to 5, essay 3, news 2 to 3, the war and the peace 4,
debate 1, assessment 1 gives 17 to 19.
**Why it matters.** The last unit of the year is the one most often cut short; with three products the writer drops
the debate or the news practice, and the argument the year builds to gets the fewest days.
**Fix (frame unit 9, Writing and research arc, and the us1-empire and us1-argument-writing notes).** One product: the
us1-empire research report is written as the third several-page argument, on a question the student's case can answer
("Should the United States have taken this step?"), using the research cycle of unit 1; the League debate is one day,
argued from the positions of the period. No standard moves. Settled below. LAYER frame. REPEAT yes (the grade 5 frame
read, finding 3: a unit short for what it holds).

### 2. The wh1-renaissance hand-on is labelled as dormant content to reteach (moderate; firm)

**What is wrong.** The "Picked up" table calls wh1-renaissance to us1-revolution-war "dormant: readiness check and a
one-lesson reteach", and unit 1's "Why" says the row "opens with a readiness check and a short reteach of the World
History I row it assumes". The progression read kept this link on purpose as a skill link: significance judged over
time (D2.His.3), which is exactly us1-revolution-war's skill (Deborah Sampson, James Armistead Lafayette). The row's
own note says the link is "weighing how new ideas spread and took hold", which is neither.
**Why it matters.** A writer will build a Renaissance reteach lesson in a Revolutionary War unit, and will not teach
the significance worked example the link exists for.
**Fix (frame "Picked up" table and unit 1 "Why"; us1-revolution-war notes).** Kind: "skill link (significance,
D2.His.3), opens with a worked example". Unit 1's sentence: "us1-revolution-war opens with a worked example of judging
significance over time, the skill wh1-renaissance taught." Row note: replace "(weighing how new ideas spread and took
hold)" with "(how significance is judged and changes over time, D2.His.3)" and "a one-lesson reteach of
wh1-renaissance" with "a worked example of the skill". LAYER frame and progression. REPEAT yes (the progression read,
finding 2: a handoff pointed at the wrong skill).

### 3. Owned content sits in "Check set adds", and two additions have no source (minor; firm)

**What is wrong.** Unit 3 lists "Manifest destiny as a phrase and an argument, read from its own sources" as a
candidate, but MA.USI.T2.3 names Manifest Destiny (the row carries it in its words column, not its notes). Unit 3 also
lists the Monroe Doctrine as a candidate, while MA.USI.T7.5e (the Roosevelt Corollary to the Monroe Doctrine) cannot be
taught without it. Two additions carry no check-set source: Manifest Destiny (unit 3) and "Prohibition's road to the
18th Amendment" (unit 8).
**Why it matters.** Candidates are confirmed or dropped at the unit plan; owned content can be dropped with them, and
the lens marks an addition with no recorded source.
**Fix (frame units 3, 8 and 9; row notes).** Unit 3: move Manifest Destiny into "What students learn" and add it to
us1-westward-expansion's notes ("Manifest Destiny read as a phrase and an argument from its 1840s sources"); keep the
Monroe Doctrine in unit 3 as owned background and add to us1-empire's notes "the Monroe Doctrine of 1823 recalled as
the base of the Roosevelt Corollary (T7.5e)". Unit 8: record the check-set member for Prohibition or drop it. LAYER
frame and progression. REPEAT yes (the grade 5 frame read, finding 1: owned content held as a candidate).

### 4. Lateral reading is taught in week 28 but used from week 1 (minor; likely)

**What is wrong.** us1-research-inquiry (unit 1) has students build their own source sets, which today means websites;
unit 8's action asks for "a fact-checked report", and us1-progressivism compares muckrakers with "fact-checking
today". Lateral reading and checking who is behind a site are owned by us1-news-reading in unit 9 (weeks 28 to 31).
Grade 8 taught them (ss8-news-literacy), but the frame never names them as review before unit 9.
**Why it matters.** A unit 1 writer has no prompt to refresh the grade 8 routine before students judge web sources;
the Government read found the same row too late for a grade 11 student taking Government beside this course.
**Fix (frame unit 1 C3 column).** Add: "Review: lateral reading and checking a site's sponsor from ss8-news-literacy,
as one short routine on the first research task; us1-news-reading (unit 9) takes it to full depth." No day or standard
moves. Settled below. LAYER frame. REPEAT yes (the US Government frame read, finding 2: the same row placed late).

### 5. Huckleberry Finn is set as a required read (minor; likely)

**What is wrong.** Unit 6 and us1-jim-crow read "Twain's Huckleberry Finn ... for how it treats race". MA.USI.T5.8
lists it with "such as"; the whole novel is not owned by this course, ELA 11 has no row that reads it, and the text
uses a slur hundreds of times, which rule 6 keeps off student pages.
**Why it matters.** Read as written, a 13-day history unit takes on a novel with no ELA partner and a slur problem on
every page; the Black writers and colleges the standard also names get squeezed.
**Fix (row notes and frame unit 6).** Core: historically Black colleges and Dunbar and Chesnutt from short excerpts;
Huckleberry Finn met through a short slur-free excerpt and the record of how it was received and challenged, as the
"impact" the standard asks to evaluate. Settled below. LAYER frame and progression. REPEAT new.

### 6. Stale notes (minor; firm)

**What is wrong.** (a) data/plans/flow-status.csv reads `frame:us-history-i,active,...,"Writing: ..."`; the frame is
written and passes the gate. (b) docs/reviews/frame-us-history-ii-2026-11-13.md says "US History I has no frame yet"
(lines 10 to 11 and 155). (c) us1-press-history's notes say it "hands on the history of the press that US Government
builds on", but since q-ss-progression-1 no Government row assumes a US History I row.
**Fix.** (a) "Written; expert read 2026-11-13 (docs/reviews/frame-us-history-i-2026-11-13.md)". (b) Add after line 158:
"Since written (2026-11-13): the US History I frame's 'Handed on' table matches this seam row for row (checked in
frame-us-history-i-2026-11-13.md)." (c) Replace the sentence with "Government (grade 11 or 12) teaches press freedom
from grade 8 and does not assume this row." LAYER process. REPEAT yes (stale notes in earlier reads, and the Government
and US History II reads found the same out-of-date "grade 12 courses" sentence in other rows).

## Checked and found right (do not undo)

- **Owned skills.** All 27 rows sit once; review uses are named as review. NML placed here (T1.5, T2.1, T2.2, T3.2,
  T4.1 to T4.3) and in Government (the rest) cover every NML code once.
- **Standards in full.** Every USI code and lettered part sits in a unit and its row (T3.2a to e, T4.2a to e as the
  research choices with the class meeting all, T7.5a to k with j and k in us1-wwi), apart from finding 3's Manifest
  Destiny. T1.3's three views (Parliament, colonists, Native nations) and T6.5's treaties and laws as sources are kept.
- **Order.** The research cycle first; the founding before expansion; removal before the land it opened; the economy
  before resistance and reform; reform and slavery before the sectional crisis; Reconstruction before Jim Crow;
  industry before the Progressive answer. Unit 4's thematic span carries a reason that holds.
- **Days, apart from finding 1.** 19, 15, 13, 21, 21, 13, 13, 17, 16 for 4, 3, 2, 4, 4, 2, 2, 3, 3 rows; units 4 and 5
  are long for the reform research and the two full arguments, as they should be. The week ranges add up to 32.
- **Seams.** Every grade 5 and grade 8 row that names a us1 row, and every World History I and II hand-on, is in the
  "Picked up" table; every us1 hand-on to a us2 row is in the US History II frame's table in the unit named.
  Government and Economics assume no us1 row, as decided.
- **Values and hard history.** The seceding states' declarations as evidence that slavery was the central cause; Lost
  Cause read as an account to test, not a view to balance; court holdings that stand (Worcester, McGirt, the 1980
  Black Hills ruling, Elk v. Wilkins, Wong Kim Ark); Native nations in the present tense from their own materials; the
  2022 federal boarding school report; no role play anywhere; a choice of text on boarding schools.

## Cross-subject

All leans are on ELA 11 (W.11-12.7, W.11-12.8, RI.11-12.9, RI.11-12.1, W.11-12.1, W.11-12.9, RI.11-12.7), and the
frame teaches its own history version first in each case; the Douglass pairing (history excerpts in weeks 11 to 15,
ELA whole in 16 to 18) and the founding documents pairing (ELA from week 8) are well made. Every row named exists. No
ELA 11 frame exists, so "taught first" cannot be checked. If finding 1 is applied, the unit 9 writing load is one
essay, which the ELA 11 frame should keep clear of an ELA due date.

## The lens checklist (course frame layer)

| Line | Result |
|---|---|
| An anchor standard in the course's Massachusetts topic range has no unit | Met (USI.T1 to T7 and the placed NML codes all have units) |
| The replaced grade 3 year, or "your state" in grade 8, keeps Massachusetts-only content | Not applicable (T1.4's Massachusetts people and the Lowell mills are national history, not a state study) |
| No unit lists what the check set adds, or an addition has no recorded source | Missed in part: two additions have no source (finding 3) |

## What I could not judge

- The ELA 11 frame (not written).
- Whether Since Time Immemorial's high school units fit units 2 and 6 as described (the unit plans read them).
- Accuracy of the removal, slavery, Lakota and boarding school content (sensitivity read and a qualified reader).

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| The us1-empire research report is the year's third several-page argument; the League debate is one day | Three products do not fit 16 days; one product meets T7.5 and D4.1 together | docs/courses/us-history-i/frame.md (unit 9, Writing and research arc); us1-empire and us1-argument-writing notes |
| Unit 1 opens the research cycle with a short lateral-reading review from grade 8 | Students judge web sources from week 1; full depth stays in unit 9 | docs/courses/us-history-i/frame.md (unit 1 C3) |
| Huckleberry Finn met by a short slur-free excerpt and its reception; Dunbar, Chesnutt and the Black colleges as the core of T5.8 | The standard says "such as"; rule 6; no ELA partner | docs/courses/us-history-i/frame.md (unit 6); us1-jim-crow notes |

## For Cory

- **Government beside US History I (frame "For the lead" 2).** This is the same question as the grade 12 timetable in
  the US History II frame ("For the lead" 1). One Desk card should carry both.
- **Since Time Immemorial (frame "For the lead" 3).** My read: CC BY 4.0 is the licence; OSPI's request to keep its
  content design is a courtesy, not a term, so it is not a licence question. Honour it where the unit plan adapts a
  whole lesson, and credit as usual.
- **People.** Units 3, 4 and 6 need a qualified person's read before any unit ships (FOUNDATION 7.3).

Not logged in the defect ledger (`plan.py defect`): the brief allows edits to this report only. The caller may log
findings 1 to 6 with found_by `expert`.

## Sources

No outside source was fetched for this read; it rests on the repository files above and memory.
- Massachusetts 2018 as coded in data/standards/ma-hss-2018.txt (USI.T1 to T7, NML.T1 to T5).
- Creative Commons Attribution 4.0, section 2(a)(5)(B) and section 8 (no added restrictions; a licensor's request is
  not a term): from memory (likely; check the legal code before the unit plan relies on it).
- Huckleberry Finn's use of the slur and its challenge record: from memory (firm, widely documented).

## For the source list

Nothing new.

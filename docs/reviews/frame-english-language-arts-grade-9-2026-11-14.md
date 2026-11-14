# Frame read: english-language-arts-grade-9 (English Language Arts Grade 9), 2026-11-14

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/ela.md, docs/RUBRIC-ELA.md (the 6 to 12 figures and Gateway 2), the
  writer's brief docs/pipeline/briefs/frame-write.md (its "Lessons from the social studies frames"), APPROACH-ELA's
  unit-field section (texts.csv, cold checks).
- The frame docs/courses/english-language-arts-grade-9/frame.md and its row in data/plans/frames.csv
  (`english-language-arts-grade-9,8,160`). No base text, so no source map.
- All 24 grade 9 rows and all 27 grade 10 rows of data/progressions/ela.csv; the grade 8 rows' hands_on (no grade 8
  frame exists yet, so the rows stood in for it); the grade 11 and 12 rows' named texts.
- The frame after: docs/courses/english-language-arts-grade-10/frame.md. Grade 6, 7 and 11 frames searched for
  repeated texts.
- Same-year frames: docs/courses/world-history-i/frame.md (units, weeks, its ELA calendar and hard weeks),
  docs/courses/biology/frame.md and docs/courses/algebra-i/frame.md (their ELA leans and weeks).
- DESK-ANSWERS 2026-11-12 (course texts) and 2026-11-13 (q-ela-progression-1, the recency rule); the "For the course
  frames" lists of docs/reviews/progression-cross-2026-11-13.md and the 9-10 items of
  docs/reviews/progression-ela-stitch-2026-11-13.md; earlier frame reads in docs/reviews/ for REPEAT tags.
- The 9-10 lines of data/standards/ccss-ela-standards-full.txt, lettered parts included.
- Gates: `python -X utf8 scripts/plan.py check` (frame english-language-arts-grade-9: 0 failures; 8 units, 160 days,
  148 in units, 12 checks and respond days). `python -X utf8 scripts/frame.py check english-language-arts-grade-9`:
  0 failures. `python -X utf8 scripts/stale.py check`: 54 files, 0 failures. A script of mine confirmed every grade 8
  row's hands_on to a grade 9 row appears in the "Picked up" table.

## Verdict

The frame is sound: every grade 9 row is placed once, every grade 8 hand-on is picked up, every hand-on to grade 10
matches the grade 10 frame, the texts are free to use and do not repeat another grade's picks, and the units sit well
against World History I's hard weeks and writing load. The biggest risk is the cross-subject section, which still
says the biology and Algebra I frames are unwritten and so misses that biology asks ELA 9 not to set a human-impact
topic before week 28, which unit 7 does in weeks 24 to 26. The one change that matters most is to rewrite that
section from the frames now on file and settle the biology conflict; the rest are small wording fixes, and the lack
of a recent long text is a fair question for Cory, not a fault.

## Findings, most serious first

### 1. Cross-subject is stale and misses a conflict with Biology (moderate; firm)

**What is wrong.** The section says "the biology and Algebra I frames are written later, so their units are not
guessed". Both exist. From them: Algebra I teaches alg1-correlation-causation in unit 3, weeks 10 to 12, so unit 6's
lean (weeks 20 to 24) is met first, not "reciprocal". Biology teaches bio-evidence-common-ancestry in unit 7, weeks 20
to 23, so unit 7's HS-LS4-1 lean is met first. Biology teaches bio-define-human-impact-problem in unit 9, weeks 26
to 28, after ELA's unit 7, and biology's frame (line 183) picks: "ELA 9 ... may set this topic only if its piece
falls after week 28, otherwise it picks another topic." ELA's explanatory piece explains the honeycreepers' threats
(avian malaria, introduced species, habitat loss), a human-impact topic, due week 26. Biology's frame also wants ELA
9's explanatory writing "before week 20" and asks that ELA 9's process pieces not share a due week with its unit 9
design report (weeks 26 to 28); ELA's explanatory piece is due week 26.
**Why it matters.** Two frames give opposite instructions for the same unit; a unit writer reading either builds the
wrong topic, and the stale line fails lesson 15.
**Fix (frame, Cross-subject, unit 7 cells).** Replace the stale sentence with the units and weeks above. Unit 7's
process piece explains how the honeycreepers descended from one ancestor and spread across the islands (biology unit
7 has taught common ancestry by week 23); the threats stay in the reading as context, explained only as the sources
say, with no solution asked. That meets biology's pick without moving any week. Keep the piece due in week 26 but
name it under "For the lead" as a possible clash with biology's unit 9 report so the two scope and sequences agree
the day. Biology's "before week 20" wish has its own "if later" line and needs no change here. Also stale, for the
fixer: biology's frame line 135 and chemistry's line 140 say the ELA frames "are written later" (LAYER process).
LAYER frame. REPEAT yes (lesson 15 status lines; lesson 8 leans).

### 2. Unit 1's compelling question does not fit two of its stories (minor; firm)

**What is wrong.** "What does the writer let the reader know before the characters do?" fits "The Monkey's Paw" and
the Poe, but "The Open Window" works by keeping the reader as ignorant as Framton until the last lines, and much of
Connell's suspense comes from not knowing what Rainsford will do. The frame's own list of structural choices (the
twist, Montresor's withheld motive) is about withholding, not telling ahead.
**Why it matters.** Lesson 10: a question students cannot answer from two of the four stories turns into a trick.
**Fix (frame, unit 1 cell).** "In each story, what does the writer let the reader know, and when, and what does
that do to us?" LAYER frame. REPEAT yes (lesson 10).

### 3. Two year-long codes are not said to be taught where they are taught (minor; firm)

**What is wrong.** e9-rl-range-scaffolded (~RL.9-10.10) sits in unit 1, whose texts are "the band's lower part,
short whole texts". The standard's grade 9 line, drama and poems at the high end with scaffolding, is met by the
Odyssey (unit 2) and Romeo and Juliet with the sonnets (unit 8), but neither cell names RL.9-10.10. Likewise W.9-10.9
sits in unit 1 on stories, and the row says 9a and 9b apply; no cell says where 9b (writing that judges an argument
in nonfiction) starts, though unit 6 plainly does it.
**Why it matters.** Lesson 4: a unit writer for unit 2 or 8 will not plan the high-end scaffolding as a standard,
and the scope and sequence cannot show 9b.
**Fix (frame, units 1, 2, 6, 8).** Unit 1: "~W.9-10.9a starts on the stories". Units 2 and 8 add to the review line:
"RL.9-10.10 at the high end with scaffolding: the epic (or the play and sonnets), with audio beside the text."
Unit 6 adds: "~W.9-10.9b starts: analytic paragraphs judging an op-ed's reasoning." LAYER frame. REPEAT yes
(lesson 4).

### 4. Unit 7 is tight for what it holds (minor; judgment call)

**What is wrong.** Fourteen days hold the reading (Darwin, three agency explanations, a 1,500 to 3,000 word original
essay), the RI.9-10.3 and 5 outline work, a separate three-day research project, the full explanatory process piece
with peer response, teacher step and revision log, and the end-of-unit assessment: about 15 to 17 days as written.
**Why it matters.** The process piece is the one full W.9-10.2 piece of the year; a short unit cuts its revision.
**Fix (frame, unit 7 cell).** Make the second short research project the research stage of the explanatory piece
(one island species, sourced and cited, three days), not a separate product. No days move. Settled below. LAYER
frame. REPEAT yes (lesson 9).

### 5. Paper path for film, audio and recorded talks (minor; firm)

**What is wrong.** The Devices bullet covers W.9-10.6 only. RI.9-10.7 in unit 4 rests on a 1919 film, SL.9-10.2 on a
recorded talk, SL.9-10.3 in unit 6 on a recorded speaker, and SL.9-10.5 asks for digital media in the talk.
**Fix (frame, Devices bullet).** Add: "Film, audio and recorded talks are shown on one teacher screen; where none
exists the teacher reads a transcript aloud for SL.9-10.3, and RI.9-10.7 and SL.9-10.5 are recorded unfinished, as
W.9-10.6 is. A printed visual aid meets SL.9-10.5 in part." LAYER frame. REPEAT yes (lesson 14).

### 6. "The text record (texts.csv) gives each anchor its measure" describes a file that does not exist (minor; firm)

**What is wrong.** data/plans/english-language-arts-grade-9/ does not exist; APPROACH-ELA says the files come with
the first ELA unit plans. No anchor in the frame carries a measure, so the claim "most in the lower two thirds"
rests on nothing yet.
**Fix (frame, Base text bullet).** "Pending(data/plans/english-language-arts-grade-9/texts.csv): each anchor's
measure, the four qualitative headings, the task and the reason for its place; the unit plan confirms the lower two
thirds placement." LAYER process. REPEAT yes (stale wording).

### 7. Small accuracy points (minor; firm)

- Unit 1's reason says the stories are "the most recent first-read texts that the standard allows"; the limit is
  the licence (1930), not the standard. Fix: "the most recent the public-domain line allows".
- "For the lead" item 3 says both e9-w-short-research and e10-w-research carry "Choice of style manual: see the lead
  list"; only e9-w-short-research does. Fix: name the one row.
- Unit 3: "The Necklace" in "a translation published before 1931" leaves the pick open (lesson 11). Fix: name the
  translation and its year in the cell.
LAYER frame. REPEAT yes (lesson 11 on picks).

## The data checks

- **Owned skills.** All 24 grade 9 rows placed once (gate and my read). No unit teaches another grade's row except as
  named review.
- **Standards in full.** Grade 9 owns no code in full (every code is ~, grade 10 owns it). Each started lettered part
  is named, and parts left to grade 10 are named in Seams (W.9-10.1b in full, 2a graphics, L.9-10.2b, cumulative
  impact in RL.9-10.4). Gaps in naming: finding 3.
- **Units and reasons.** Each reason holds; no skill or model is used before it is placed (evidence and structure
  in unit 1 before the epic; appeals in unit 5 before validity in unit 6; one counterclaim in unit 6 before the
  literary argument in unit 8; the look-for sheet in unit 4 before the performed passage in unit 8).
- **Days.** 160 = 148 + 12, three checks each with respond days, 32 weeks of five 50-minute lessons stated. Unit
  shares follow load (the two long works 28 and 25); unit 7 tight (finding 4), unit 1 slightly generous, both within
  reason.
- **Seams.** All grade 8 hand-ons picked up with a readiness task in the first using unit. All 29 hand-ons to grade 10
  match the grade 10 frame's "Picked up" table. No grade 10 text read here.
- **Cross-subject.** World History I calendar checked: supporting questions and graphic displays (weeks 1 to 3) come
  before unit 4; ELA's argument (weeks 20 to 24) and explanatory piece (24 to 26) come before World History I unit 10
  (weeks 28 to 31); the literary argument (week 30) and unit 10's argument (week 31) do not share a week; the
  boarding-school memoir (week 14) and book 22 (weeks 9 to 10) sit outside World History I's hard weeks (15 to 18 and
  22 to 25). Biology and Algebra I: finding 1.
- **Stale notes.** Finding 1 (frames "written later") and finding 6 (texts.csv). No others found.

### The text picks

- **Licences.** Every named anchor is US public domain by date (1930 or earlier, the translation's own date checked
  for Butler 1900, Brookes More 1922, Garnett, Goldberg 1921, Giles 1880), a US government work, or original. Connell
  (1924), Hurston (1928) and the 1919 film are correctly inside the line. Two pick gaps: "The Necklace" translation
  (finding 7) and the unit 2 candidate (settled below).
- **Repeats.** None with grades 6, 7, 10, 11 or 12 except the Gettysburg Address (grade 12, a different lens, named
  in the frame). Grade 7 already defers Ovid's Icarus to grade 9. Poe returns in grade 11 with a different story.
- **Reading level.** Short stories in the lower band first, the Odyssey in plain prose, the play last with audio:
  a sound climb. Measures are not yet on file (finding 6).
- **Informational share.** Units 4 to 7 hold 60 of 148 unit days, 40.5 percent. The rubric on file gives a share
  only for grades 6 to 8 (55 percent); the standards' 70 percent by grade 12 counts reading across the school day,
  and the Publishers' Criteria ask high school ELA for substantial literary nonfiction, not a fixed share (from
  memory). About 40 percent in ELA alone is normal for a grade 9 course and the frame's pick (keep, report it) is
  right.
- **No recent long text.** It does not break a standard or the rows (the Odyssey and Romeo and Juliet are the rows'
  contract). It does sit badly with Cory's 2026-11-13 words ("more recognizable and recent literature"), and grade 9
  is the year students leave K to 8's mostly new texts, so its two long works are the oldest of the four years.
  The frame raised it correctly (For the lead 5). The option it does not give Cory: The Murder of Roger Ackroyd
  (1926, US public domain, recognizable, and its unreliable narrator is the cleanest case of RL.9-10.5's structure
  creating surprise) read whole as a class text in unit 1 in place of two of the four stories, unit 1 from 22 to
  about 26 days, the days taken from the Odyssey's books 13 to 23 (read more in summary). For Cory below.

### The proposed row changes

- **e9-rl-structure-time (drop Bierce).** Agreed: grade 11 reads "An Occurrence at Owl Creek Bridge" in
  e11-evidence-uncertain and e11-lit-structure, confirmed in the grade 11 frame's unit 1. Flashback then meets grade 9
  only in the Odyssey review, which is enough since grade 10 owns RL.9-10.5. Use the frame's row text.
- **e9-rl-world-stories (move Tagore).** Agreed: grade 10 reads two Tagore stories and Gitanjali 35, and the
  replacement names the four stories this frame reads. Use the frame's row text.
- **Antigone (e10-rl-world-literature).** Judged in the grade 10 report: agreed, with a wording change.

### Lessons from the social studies frames (frame-write.md)

| # | Lesson | Here |
|---|---|---|
| 1 | Respond day after each check | Met (1, 1, 2) |
| 2 | Check-set cells "Candidate:" | Met |
| 3 | Time a day stated | Met (50 minutes, five a week, 32 weeks) |
| 4 | Standards in full, every part named | Mostly met; finding 3 |
| 5 | Thread starts where first used | Met (readiness task per first using unit; models table) |
| 6 | "First" claims checked | Met; one wording slip (finding 7) |
| 7 | Both ends of every handoff | Met (row changes under For the lead) |
| 8 | "If later" lines | Met for World History I; Biology and Algebra I stale (finding 1) |
| 9 | Days by load | Mostly met; finding 4 |
| 10 | Questions answerable from the unit | Unit 1 missed (finding 2) |
| 11 | Picks named, not repeated | Mostly met; finding 7 |
| 12 | Sensitivity reads line | Met (units 4 and 8 named) |
| 13 | No math ahead of math | Met (correlation without computing; Algebra I teaches it first anyway) |
| 14 | Paper path, no account | W.9-10.6 met; media not (finding 5) |
| 15 | No status lines about other files | Missed (finding 1) |

### The lens checklist (course frame layer)

| Lens line | Here |
|---|---|
| Unit named by a specific topic and its texts | Met in part: units 1 (suspense stories) and 3 (stories in translation) are named by form, not by a knowledge topic. Fair for craft units feeding RL.9-10.5 and 6, and both have a sharp question; no change asked |
| Anchor texts on file with measure, qualitative reason, reason for place | Reason for place met; measures pending (finding 6) |
| Texts lean to one era, tradition or kind | Not a fault: epic, drama, poems, stories from four countries, memoir by Native, immigrant, disabled and Black writers, speeches, government science, originals |
| No long text read whole | Met: Romeo and Juliet whole, the Odyssey in large parts |

## What is right and should not be touched

The placement of every hard text outside World History I's hard weeks; the due-week stagger with history; the
Odyssey book 22 note (the enslaved women treated as people the epic wrongs); the safe-messaging note on Romeo and
Juliet; the readiness task placed in the first unit that uses each grade 8 skill; the regions chosen so no culture
is read twice in the band; the single four-year style sheet.

## What I could not judge

Lexile measures of the anchors (no text record yet, and I did not run any). Whether a public-domain copy of
Deliverance (1919) with usable quality is reachable; the unit plan should check.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Keep Butler's 1900 Odyssey; the unit gives a name key (Ulysses for Odysseus, Minerva for Athena, Jove for Zeus, Neptune for Poseidon) | Butler is the plainest public-domain prose, but he uses Latin names, and grade 7 history taught the Greek ones; the key also links to Tennyson's "Ulysses" (from memory, likely) | frame.md unit 2 cell |
| Unit 2 candidate for the second later answer to the Odyssey: Andrew Lang's sonnet "The Odyssey" (1879) | Public domain, short, answers the epic directly; Cavafy is not usable | frame.md unit 2 check-set cell |
| Unit 7's second short research project becomes the research stage of the explanatory piece | Frees about two days in a tight unit without moving weeks (finding 4) | frame.md unit 7 cell, Writing calendar |
| Unit 7's process piece explains the honeycreepers' descent from one ancestor; threats stay as reading | Honours biology's frame pick without moving weeks (finding 1) | frame.md unit 7 cell, Cross-subject |
| Informational share reported in the scope and sequence both by unit days and by anchor texts | The rubric counts on anchor texts (2a); the frame counts days | scope and sequence (step 3) |

## For Cory

- **A recent long text in grade 9?** The frame keeps the Odyssey and Romeo and Juliet and leaves the recent long
  anchor to grade 10. Expert's pick: yes, add The Murder of Roger Ackroyd (1926) read whole in unit 1, in place of
  two short stories, with about four days moved from the Odyssey's later books. Alternative: keep as drafted.
- **People:** a Native reader (unit 4) and a reader with school counselling background (unit 8), as the frame says.

## Sources

- Common Core State Standards for ELA, grades 9-10 lines (data/standards/ccss-ela-standards-full.txt): the lettered
  parts checked.
- EdReports ELA 6-12 criteria as summarized in docs/RUBRIC-ELA.md: the 55 percent figure applies to grades 6 to 8.
- Publishers' Criteria for the Common Core, grades 3-12 (2012), and CCSS Appendix A text-complexity bands: from
  memory, not re-fetched.
- US copyright term (works published 1930 or earlier in the public domain on 2026-01-01): from memory.

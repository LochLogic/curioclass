# Frame read: english-language-arts-grade-10 (English Language Arts Grade 10), 2026-11-14

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/ela.md, docs/RUBRIC-ELA.md, the writer's brief
  docs/pipeline/briefs/frame-write.md (its "Lessons from the social studies frames"), APPROACH-ELA's unit fields.
- The frame docs/courses/english-language-arts-grade-10/frame.md and its row in data/plans/frames.csv
  (`english-language-arts-grade-10,7,160`). No base text, so no source map.
- All 27 grade 10 rows and all 24 grade 9 rows of data/progressions/ela.csv; the grade 11 rows' assumes and the
  grade 11 and 12 rows' named texts.
- The frames before and after: docs/courses/english-language-arts-grade-9/frame.md and
  docs/courses/english-language-arts-grade-11/frame.md.
- Same-year frames: docs/courses/world-history-ii/frame.md (units, weeks, its ELA calendar, the shared research
  brief, the genocide weeks) and docs/courses/chemistry/frame.md (its ELA leans).
- DESK-ANSWERS 2026-11-12 and 2026-11-13 (the recency rule); docs/reviews/progression-cross-2026-11-13.md
  (finding 8, the shared brief; "For the course frames"); docs/reviews/progression-ela-stitch-2026-11-13.md (items
  12 to 17 and the Douglass swap); earlier frame reads for REPEAT tags.
- The 9-10 lines of data/standards/ccss-ela-standards-full.txt, lettered parts included.
- Gates: `python -X utf8 scripts/plan.py check` (frame english-language-arts-grade-10: 0 failures; 7 units, 160
  days, 148 in units, 12 checks and respond days). `python -X utf8 scripts/frame.py check
  english-language-arts-grade-10`: 0 failures. `python -X utf8 scripts/stale.py check`: 54 files, 0 failures. A
  script of mine confirmed every grade 10 row's hands_on appears in the grade 11 frame and every grade 11 row's
  grade 10 assumes appears in this frame's "Handed on" table.

## Verdict

The frame is sound in its texts and order: every grade 10 row is placed once, every 9-10 code is owned with its
lettered parts, the three long works are read whole, and the seams with grade 9 and grade 11 match both frames. The
biggest risk is the shared research brief with World History II: the frame agrees the weeks and the split but writes
no brief, and its own product (an explanatory report) differs from history's (a research argument), so in a school
that teaches both the year's only full W.9-10.2 piece can disappear. The one change that matters most is to write
that brief into the frame with one named product; next, unit 3 is short for what it reads and the world-literature
row's longer work is taught in unit 5 under the label "review".

## Findings, most serious first

### 1. The shared research brief is agreed but not written, and the two products differ (moderate; firm)

**What is wrong.** e10-w-research and wh2-research-argument both say "the course frames write one shared brief".
This frame (For the lead 1, Cross-subject) and World History II's (For the lead 3) agree only the weeks (29 to 32)
and the split (history the question set and sources, ELA the process and citation). Nothing says what the one
product is, how long, when it is due, or who scores what. The two courses' products differ: ELA's unit 7 ends in an
explanatory research report (W.9-10.2a to 2f, with a figure the writer makes) and an 8 to 10 minute talk in week 31;
history's unit 11 ends in a research argument adapted for audiences in print and digital form, in week 32. Unit 7's
compelling question ("How should one coastal community prepare...") is itself an argument question. And For the lead
1 has a school teaching both replace the sea-level set "with history's question set" from week 26, but history's
unit 11 does not open until week 29.
**Why it matters.** Unit 7 is the only unit that teaches W.9-10.2 in full. If a shared school makes the joint paper
history's argument, grade 10's ownership of W.9-10.2 is lost without anyone deciding it; if it makes it ELA's
report, history's D4 argument is lost. A teacher pair cannot plan from "process and citation".
**Fix (frame, Cross-subject, a short "Shared research brief" block; and unit 7).** Name: weeks 29 to 31 for the
project in a shared school (history supplies the question set by week 28, so ELA's weeks 26 to 28 on argument
judging and source sets run on the sea-level set in every school); one product, a sourced report of 1,500 to 2,000
words in two parts, an explanatory part with headings and a figure (W.9-10.2, scored by ELA) and an argued
recommendation with counterclaims (history's research argument, scored by history); one talk in week 31 serving
SL.9-10.4 to 6 and history's oral form; citation to the Curio Class style sheet. Reword unit 7's question so the
explanatory part answers it: "What is happening to one coastal community as the seas rise, and what does the
evidence say about the ways to prepare?" World History II's frame takes the same block (its fixer). LAYER frame.
REPEAT new.

### 2. Unit 3 is short for its reading, and the row's longer work is taught in unit 5 as "review" (moderate; firm)

**What is wrong.** Unit 3 (15 days) reads two Tagore stories and a poem, chapters of Noli Me Tángere, Mhudi "in
large parts" (a full novel), and chapter 1 of Native Life in South Africa, writes a comparison essay and teaches the
colon. That is more reading than unit 5 (22 days), which owns one row (RI.9-10.6) on one novel and a short set. At
the same time the row placed in unit 3, e10-rl-world-literature, asks for "a longer work"; unit 3 says it is
"finished by the year's longer world work read whole in unit 5", and unit 5 lists that reading as "Review: the novel
read whole as the year's longer world work (RL.9-10.6, placed in unit 3)". It is the first teaching of that part,
not review.
**Why it matters.** Lessons 4 and 9: a writer of unit 3 will rush Mhudi or cut the comparison; a writer of unit 5
will treat RL.9-10.6 as already done and teach only rhetoric, so the standard's longer-work part is planned nowhere.
**Fix (frame, units 3 and 5).** Unit 3: Mhudi in selected chapters (the opening and two or three chapters the unit
plan names, with teacher summaries between), Noli in three or four chapters, Native Life chapter 1 as background for
Mhudi only; days stay 15. Unit 5's "What students learn" gains, outside the review line: "RL.9-10.6, the longer
work: the cultural experience of Paul's generation in Germany, compared with the colonial-era works of unit 3 (the
part of e10-rl-world-literature this unit teaches)." Unit 3's cell names that unit 5 teaches the longer-work part.
LAYER frame. REPEAT yes (lessons 4 and 9).

### 3. The Declaration of Sentiments repeats grade 12's comparison; the Declaration's four readings go unnamed (minor; firm)

**What is wrong.** Unit 6 reads the Declaration of Sentiments as an answer to the Declaration of Independence.
e12-info-founding-documents reads "the Seneca Falls Declaration of Sentiments (1848) against the Declaration of
Independence": the same pair, the same lens. The frame's "Texts not repeated" line names only grade 11's return to the
Declaration; the Declaration is also read in grade 8 (e8-reading-range thread) and grade 12, and the cross review
counted founding documents read seven times across subjects. Also, with Douglass moved to grade 11, the set has no
Black American voice on who liberty includes.
**Why it matters.** Lesson 11; a grade 12 student meets the same pairing twice, and the set misses the most direct
case of its own theme.
**Fix (row e10-ri-seminal-documents and frame unit 6).** Replace the Declaration of Sentiments with Frances Ellen
Watkins Harper, "We Are All Bound Up Together" (1866, US public domain), a speech to the women's rights convention
on race and the vote, which still answers the Declaration and pairs with Anthony. Row text: replace "the Declaration
of Sentiments, " with "Frances Harper's 1866 speech 'We Are All Bound Up Together', ". Add to "Texts not repeated":
"The Declaration of Independence is read in grades 8, 10, 11 and 12, each with a different lens (founding thread;
who liberty includes; reasoning; documents that answer it)." Under "For the lead" as a row change. LAYER progression
and frame. REPEAT yes (lesson 11).

### 4. Three standards not taught in full as written (minor; firm)

- **W.9-10.9b.** Unit 1 names "W.9-10.9a" only (Frankenstein). 9b, applying the reading standards to literary
  nonfiction (judging an argument's reasoning), is done in unit 7 ("a judgment of the whole") and the timed essays
  on nonfiction, but no cell names it. Fix: unit 7 adds "the written judgment of an argument (W.9-10.9b)"; unit 2's
  timed analytic writing on Huxley names W.9-10.9b too.
- **SL.9-10.3.** Unit 7 says "the same judgment of a speaker on the recorded hearing"; the standard also names the
  speaker's point of view, rhetoric, and exaggerated or distorted evidence. Fix: name them in the cell, and use a
  recorded debate as well as the hearing, as the row asks.
- **RL.9-10.10 and RI.9-10.10.** Owned in units 1 and 2 (weeks 1 to 9), but the standard's line is independence by
  the end of grade 10. No cell says where independent proficiency is shown. Fix: the year-end check (week 32)
  states it is the independent reading evidence for both codes: cold literary and informational texts at the high
  end, no before-reading help; units 4 to 7 each carry one independent reading checkpoint.
LAYER frame. REPEAT yes (lesson 4).

### 5. Unit 7's 8 to 10 minute talks have no days (minor; firm)

**What is wrong.** Thirty students at 8 to 10 minutes with questions is 300 to 400 minutes, six to eight lessons,
on top of the source set, argument judging, a three-week project and the report in 28 days.
**Fix (frame, unit 7 cell).** Talks given in small-group panels (five or six students each, three panels at once,
the teacher moving between them with the look-for sheet, one talk per panel recorded where a device exists), two
days. Settled below. LAYER frame. REPEAT yes (lesson 9).

### 6. Cross-subject still calls the chemistry frame unwritten (minor; firm)

**What is wrong.** "The chemistry frame is written later, so its units are not guessed." It exists: chem-climate-forecast
is in unit 9, weeks 23 to 26, so unit 7's HS-ESS3-5 lean is met first; chemistry's frame says ELA may set the climate
topic only if its piece falls after week 26, which the week 31 report does. Chemistry's writing-load line asks that
its unit 9 forecast (weeks 23 to 26) not share a due week with ELA 10's process pieces; unit 6's issue argument is due
week 26.
**Fix (frame, Cross-subject).** Replace the sentence with the unit and weeks; the HS-ESS3-5 row becomes "Taught
first (Chemistry unit 9, weeks 23 to 26)", keeping the "if later" line; name the week 26 possible clash under "For
the lead" so the two scope and sequences agree the day. LAYER frame and process. REPEAT yes (lesson 15).

### 7. Two hard-content claims are not quite right (minor; firm)

**What is wrong.** The hard-content line lists World History II's Armenian genocide weeks (9 to 12) and then places
Mhudi's opening massacre at Kunana in week 11 without noting the overlap. Unit 5's reason says it "starts in week 18,
after the Holocaust weeks"; week 18 is inside 15 to 18 (unit 5 opens on day 90, the last day of week 18).
**Why it matters.** World History II asked only for weeks 15 to 18 and 27 to 29 to be kept clear, so neither breaks
the agreement, but the frame states something the calendar does not show.
**Fix (frame, Cross-subject and unit 5).** Hard-content line: "Mhudi's opening massacre falls in weeks 10 to 12,
beside World History II's Armenian genocide days; the scope and sequences put them on different days." Unit 5:
"starts at the end of week 18, after the Holocaust lessons; its hardest chapters fall in weeks 21 to 22."
On Julius Caesar's act 5 in week 16: the frame's pick (keep, read with the teacher) is right. The suicides are a
safe-messaging matter, not atrocity content; the WHII request was for ELA's hardest texts, which these are not; and
the frame shows the units cannot swap. LAYER frame. REPEAT yes (the hard-weeks lines of the social studies reads).

### 8. Unit 3's question does not fit Tagore's stories, and one citation is garbled (minor; likely)

**What is wrong.** "How does each writer show what life under colonial rule did to the people in the story?"
"Kabuliwallah" (an Afghan peddler and a Calcutta child) and "The Postmaster" (a city clerk in a village post office)
show colonial rule at most as backdrop; students would answer from outside knowledge. The anchor line also cites
"Hungry Stones and Other Stories and The Hungry Stones, 1916", one book named twice.
**Fix (frame, unit 3).** Question: "What does each work show about how its people live with power held by others,
at home and from abroad, and how can a reader tell from the text?" Citation: "in The Hungry Stones and Other
Stories (1916)". LAYER frame. REPEAT yes (lesson 10).

### 9. Unit 2's two cloning explanations may not be "two authors ordering the same material" (minor; judgment call)

**What is wrong.** RI.9-10.3 and 5 are taught on the National Human Genome Research Institute's cloning fact sheet
and the Food and Drug Administration's animal cloning explanation. From memory, the first is a general explainer and
the second is about food safety; neither may lay out Dolly's cloning at the row's length (2,000 to 5,000 words) or
in a comparable order.
**Fix (frame, unit 2 cell).** The unit plan checks both pages first. If they do not order the same material, use two
public-domain accounts of one experiment that fit the unit's question better: Louis Pasteur's 1864 Sorbonne lecture
on spontaneous generation (in a public-domain translation) and John Tyndall's essays on the floating matter of the
air (1881), two scientists explaining whether life can arise from non-life. LAYER frame. REPEAT new.

### 10. Two "see the lead list" pointers in the rows are not answered (minor; firm)

**What is wrong.** e10-ri-seminal-documents says King's letter, the standard's own example, "is not public domain;
see the lead list". e10-rl-world-literature says the public-domain translations lean old, European and South Asian;
"see the lead list". This frame's "For the lead" answers neither.
**Fix (frame, For the lead, with row text).** King: "Not an anchor (under copyright); a teacher may point to it,
and a short quoted excerpt may sit in a lesson as a pointer (2026-11-13 rule)." Translations: "Answered by unit 3
(the Philippines and South Africa beside India) and unit 5 (Germany), with an original Curio Class story for a thin
region (the unit 3 candidate)." Each row's "see the lead list" is replaced by that line. LAYER frame and progression.
REPEAT yes (lesson 7).

### 11. Paper path for media, and two sensitivity gaps (minor; firm)

- **Media.** The Devices bullet covers W.9-10.6 only; SL.9-10.5 (digital media in the talk), RL.9-10.7 (a staged
  recording, if used), the recorded hearing and the audio beside the long texts need the same rule. Fix as in the
  grade 9 read: one teacher screen; a transcript read aloud for SL.9-10.3; otherwise recorded unfinished.
- **All Quiet.** The sensitive-topics cell omits the soldiers' night visit to the French women (sexual content) and
  Kemmerich's amputation. Fix: name both, glossed at the age's level.
- **Mhudi.** Mzilikazi's Ndebele are the attackers at Kunana; the readers named are Tswana only. Fix: add an Ndebele
  reader to unit 3's reads (who and any pay are Cory's).
LAYER frame. REPEAT yes (lessons 12 and 14).

### 12. "The text record (texts.csv) gives each anchor its measure" describes a file that does not exist (minor; firm)

Same as the grade 9 read: data/plans/english-language-arts-grade-10/ does not exist. Fix: "Pending(data/plans/
english-language-arts-grade-10/texts.csv): each anchor's measure, the four qualitative headings, the task and the
reason for its place." LAYER process. REPEAT yes (finding 6 of the grade 9 read).

## The data checks

- **Owned skills.** All 27 grade 10 rows placed once (gate and my read).
- **Standards in full.** Every RL, RI, W, SL and L code of the 9-10 band is owned. Lettered parts named: W.9-10.1a
  to 1e (unit 4), 2a to 2f (unit 7), 3a to 3e (unit 2), SL.9-10.1a to 1d and L.9-10.4a to 4d (unit 1), L.9-10.1a
  and 1b, 3a, 5a and 5b (unit 4), L.9-10.2a to 2c (unit 3). Gaps: finding 4 (W.9-10.9b, SL.9-10.3's parts, the .10
  independence line).
- **Units and reasons.** Each reason holds and no skill is used before it is placed: the nested frames of unit 1
  before unit 2's two-narrator story; history's interpretations (weeks 9 to 12) before unit 4's counterclaims; the
  rhetoric unit before the seminal-documents unit; argument judging and full citation before the research project.
- **Days.** 160 = 148 + 12; three checks each with respond days; 32 weeks of five 50-minute lessons stated. Unit 3
  short (finding 2); unit 7 holds the talks without days (finding 5); unit 5 generous for one owned row but carries a
  whole novel, which is fair once finding 2 names its RL.9-10.6 part.
- **Seams.** All 29 grade 9 hand-ons picked up in a first using unit with a readiness task; all hand-ons to grade 11
  match the grade 11 frame's table; no grade 9 text reread here.
- **Cross-subject.** World History II calendar checked: unit 3 after history's imperialism unit and never in the
  Congo and Herero and Nama weeks; unit 4 after historians' interpretations; unit 5 after totalitarian propaganda;
  the issue argument due in week 26, outside the shared weeks. Shared brief: finding 1. Chemistry: finding 6.
- **Stale notes.** Findings 6 and 12. No others found.

### The text picks

- **Licences.** All named anchors are US public domain by date or US government works: Frankenstein (1818),
  Julius Caesar and North's Plutarch, Gérôme (1867), the four poems (1818 to 1918), Tagore (1912, 1916), Derbyshire's
  Rizal (1912), Plaatje (1916; Mhudi 1930, public domain since 2026-01-01 and, as a South African work by an author
  dead since 1932, not restored), All Quiet in Wheen's translation (1929), Wilson, the posters, Pope and Owen, the
  liberty set. The Mhudi text note (For the lead 3) is right; keep the 1930 text and say so.
- **Repeats.** Frankenstein settled to grade 10 by the stitch; Julius Caesar and All Quiet appear nowhere else; the
  Declaration and Sentiments: finding 3.
- **Reading level.** Climbs well: a whole 1818 novel first with fading scaffolds, Huxley's dense 1868 essay, then
  Shakespeare, a 1929 novel and seminal documents, with independence checked at the end (finding 4).
- **Informational share.** Units 2, 6 and 7 hold 58 of 148 unit days, 39 percent; unit 5 reads Wilson, the posters
  and Pope for an RI row, so by anchor texts the share is a little higher. As in the grade 9 read: normal for a
  high school ELA year, and the frame's pick (keep, report) is right.
- **Recent long text.** All Quiet (1929) is the year's recent, recognizable anchor and meets the 2026-11-13 rule.

### The proposed row change: Antigone (e10-rl-world-literature)

Agreed. Antigone would put a second Greek work beside grade 9's Odyssey and would be the oldest pick of the year;
All Quiet is recognizable, recent, outside the United States, read whole, and sits beside World History II's First
World War. Change the row text as the frame proposes, but name where it is taught: "(All Quiet on the Western Front
in A. W. Wheen's 1929 translation, read whole in a later unit, which teaches this part)". With finding 2, the frame's
unit 5 then says so.

### Lessons from the social studies frames (frame-write.md)

| # | Lesson | Here |
|---|---|---|
| 1 | Respond day after each check | Met (1, 1, 2) |
| 2 | Check-set cells "Candidate:" | Met |
| 3 | Time a day stated | Met |
| 4 | Standards in full | Mostly met; findings 2 and 4 |
| 5 | Thread starts where first used | Met |
| 6 | "First" claims checked | Met |
| 7 | Both ends of every handoff | Mostly met; finding 10 (row pointers), finding 1 (brief) |
| 8 | "If later" lines | Met for World History II; chemistry stale (finding 6) |
| 9 | Days by load | Mostly met; findings 2 and 5 |
| 10 | Questions answerable from the unit | Units 3 and 7 missed (findings 8 and 1) |
| 11 | Picks named, not repeated | Mostly met; finding 3 |
| 12 | Sensitivity reads line | Met, one reader missing (finding 11) |
| 13 | No math ahead of math | Met (reading values from graphs, association only) |
| 14 | Paper path, no account | W.9-10.6 met; media not (finding 11) |
| 15 | No status lines about other files | Missed (finding 6) |

### The lens checklist (course frame layer)

| Lens line | Here |
|---|---|
| Unit named by a specific topic and its texts | Met (each unit has a topic and named texts) |
| Anchor texts on file with measure, qualitative reason, reason for place | Reason for place met; measures pending (finding 12) |
| Texts lean to one era, tradition or kind | Not a fault: 1579 to 1941, Britain, Rome, India, the Philippines, South Africa, Germany, the United States; novel, play, poems, stories, essays, speeches, a trial record |
| No long text read whole | Met: three read whole |

## What is right and should not be touched

Frankenstein first, carrying every routine and setting up the two-narrator story; Julius Caesar with North's
Plutarch line by line; the liberty set with the trial record beside newspaper reports for RI.9-10.4 (the standard's
own court-opinion example); the regions chosen apart from grade 9's; All Quiet as the recent anchor; the agreement
that no other ELA process piece falls due in the shared weeks; the "if later" lines on World History II.

## What I could not judge

Lexile measures (no text record). The length and order of the two federal cloning pages as they stand today
(finding 9). Whether the Wheen translation's US first edition carries any later-added copyrighted matter (the unit
plan should use the 1929 text only).

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Unit 7 talks in small-group panels, two days | Fits the 8 to 10 minute talks with questions into the unit (finding 5) | frame.md unit 7 cell |
| Frances Harper's "We Are All Bound Up Together" (1866) replaces the Declaration of Sentiments in the liberty set | Grade 12 reads the same pairing; adds the missing Black American voice (finding 3) | ela.csv e10-ri-seminal-documents; frame.md unit 6 |
| King's letter: not an anchor, a pointer only | Under copyright; the 2026-11-13 rule allows short excerpts as pointers (finding 10) | ela.csv e10-ri-seminal-documents; frame.md For the lead |
| Mhudi in selected chapters with teacher summaries; Noli in three or four chapters | Fits unit 3's 15 days (finding 2) | frame.md unit 3 cell |
| Unit 2 fallback pair: Pasteur (1864) and Tyndall (1881) on spontaneous generation, if the federal pages fail the check | Same material, two orders, public domain, on the unit's question (finding 9) | frame.md unit 2 cell |
| Informational share reported both by unit days and by anchor texts | The rubric counts on anchor texts | scope and sequence (step 3) |

## For Cory

- **The shared research brief (finding 1):** one joint product in a school that teaches both courses, a report with
  an explanatory part scored by ELA and an argued recommendation scored by history. This sets how much work a
  student does in weeks 29 to 32 across two courses. Expert's pick: as written in finding 1. Alternative: two
  separate products, which keeps each course whole but doubles the load the cross review warned of.
- **People:** readers from the South Asian, Filipino and Southern African communities for unit 3, now including an
  Ndebele reader beside the Tswana one; a reader with school counselling background for unit 5; a Nez Perce reader
  for unit 6.

## Sources

- Common Core State Standards for ELA, grades 9-10 lines (data/standards/ccss-ela-standards-full.txt).
- EdReports ELA 6-12 criteria as summarized in docs/RUBRIC-ELA.md.
- US copyright term and the restoration rule for foreign works (URAA): from memory.
- The content of All Quiet, Mhudi, the Tagore stories and the federal cloning pages: from memory, marked where a
  finding rests on it.

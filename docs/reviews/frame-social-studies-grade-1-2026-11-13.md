# Frame read: social-studies-grade-1 (Grade 1: Leaders, Helpers and Communities), 2026-11-13

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/social-studies.md, section 1 of docs/ADOPTION-BAR-SUBJECTS.md,
  docs/courses/social-studies/STANDARD.md (sections 1 and 2).
- The frame docs/courses/social-studies-grade-1/frame.md and its row in data/plans/frames.csv (8 units, 96 days).
- The 21 grade 1 rows of data/progressions/social-studies.csv, the K rows before and the grade 2 and grade 3 rows
  after; data/progressions/social-studies-excluded.csv (the shared economics topic).
- The frames before and after: docs/courses/social-studies-kindergarten/frame.md and
  docs/courses/social-studies-grade-2/frame.md; for the five rows that hand on past grade 2,
  docs/courses/social-studies-grade-3/frame.md.
- data/standards/ma-hss-2018.txt (MA.1.T1 to T4, lettered parts) and the C3 K-2 indicator wording from the C3 PDF.
- Earlier reads: docs/reviews/progression-social-studies-*2026-11-13.md, progression-cross-*2026-11-13.md. No
  earlier frame read exists.
- Gates: `plan.py check` (frame social-studies-grade-1: 0 failures, 8 units, 96 days); `stale.py check` (0 failures).

## Verdict

The frame is sound: all 21 grade 1 rows are placed once, the units run in an order that never uses a skill before
it is taught (supporting questions, sources and the written claim come before the units that lean on them; the
vote comes before the action cycle that uses it), and the shared economics split with grade 2 is clean and recorded.
Three lessons a week of about 30 minutes (96 days) holds for what the rows own. The biggest risk is small and sits
in the progression: ss1-group-roles hands on to nothing, so its C3 civics thread breaks before grade 3. The one
change that matters most is adding that link, as the frame itself proposes.

## Findings, most serious first

### 1. ss1-group-roles hands on to no row (moderate; firm)

**What is wrong.** ss1-group-roles (MA.1.T1.2, D2.Civ.2.K-2, D2.Civ.6.K-2) has an empty hands_on, and grade 3's
ss3-taking-part owns D2.Civ.2.3-5 and D2.Civ.6.3-5 (the same two indicators, one band up) but assumes only
ss1-voting. The grade 3 frame's "Picked up" table therefore lists no row for it either. The frame names this under
"For the lead" item 2; I agree with its fix.
**Why it matters.** "All people, not just official leaders, play roles in a community" is the grade 1 idea grade 3
builds its taking-part lessons on; with no link, grade 3's readiness check will not test it and the gate cannot
see the thread.
**Fix (progression, data/progressions/social-studies.csv).** Add `ss3-taking-part` to ss1-group-roles's hands_on
and `ss1-group-roles` to ss3-taking-part's assumes; then add the row to the grade 3 frame's "Picked up" table
(unit 2, readiness check, as for the other dormant grade 1 civics rows) and change this frame's hand-on row from
"No later row assumes it" to ss3-taking-part (grade 3). LAYER progression. REPEAT yes (the social studies
progression read found rows that link to nothing, finding 4).

### 2. MA.1.T3.2a is taught in part: the flag and the bald eagle are not named (minor; firm)

**What is wrong.** The frame says "the lettered parts of MA.1.T3.2 are taught in full in ss1-national-symbols". Part
a names four symbols: the flag, the bald eagle, the White House and the Statue of Liberty. The row and unit 6's
"What students learn" name only the White House and the Statue of Liberty (with the motto, the Pledge and the two
songs). The flag and eagle were taught in kindergarten, but grade 1 owns this standard.
**Why it matters.** A coverage trace of MA.1.T3.2a finds half the named symbols missing, and the unit writer will
not plan them.
**Fix (progression row ss1-national-symbols notes and frame unit 6).** Add: "The flag and the bald eagle from
kindergarten, explained again with what each stands for (the record kept apart from later meanings, as in
kindergarten)." No day change. LAYER progression and frame. REPEAT yes (the Codex progression read found a missing
part of a bundled symbols code at kindergarten).

### 3. Store-flyer prices need a math bridge, and none is recorded (minor; likely)

**What is wrong.** ss1-goods-services finds "prices of a few things at a local market or store flyer" and ss1-choices
weighs limited money, in unit 8. Grade 1 Common Core math has no money (dollars and cents come in 2.MD.C.8); the
Cross-subject section records only the saving row's 1.OA.A.1 lean.
**Why it matters.** A writer using a real flyer brings $2.49 and $3.99 into a grade 1 room, and comparing them needs
decimals the class has not met.
**Fix (frame, Cross-subject, Mathematics grade 1).** Add a row: ss1-goods-services and ss1-choices, lean 1.NBT.B.3
(compare two numbers), unit 8, about week 27; bridge: made-up flyers with whole-dollar prices within 20 (settled
below). LAYER frame. REPEAT yes (the progression-cross read found missing and mistimed leans).

### 4. Stale note: frames.csv is already synced (minor; firm)

**What is wrong.** "For the lead" item 3 says `frame.py sync` was not run and the gate reports the csv as
disagreeing. data/plans/frames.csv holds `social-studies-grade-1,8,96`, and the gate passes.
**Fix.** Delete item 3 (or replace it with "data/plans/frames.csv synced: 8 units, 96 days; the gate passes").
LAYER process. REPEAT new.

## Checked and found right (do not undo)

- **Owned skills.** All 21 rows placed once; review uses (timeline in units 3 and 6, map-key in unit 6, claim
  closings) are named as review in the text, never in the Skills column.
- **Standards in full.** MA.1.T1.1 to T1.10, T2.1 to T2.5, T3.1 to T3.3 and T4.4 to T4.9 each sit in a unit;
  MA.1.T4.1 to T4.3 are excluded with a reason that names where grade 2 teaches the same text (MA.2.T5.1 to T5.3).
  Every C3 indicator owned matches its wording, including the parts later reads added: D1.3 (facts per supporting
  question), D4.6 and D4.7 (regional and global problems as well as local), D2.Civ.14 (people who improved their
  communities over time).
- **Order.** Groups before leaders (a leader is a member), sources before leaders from history, leaders before
  elections (what voters weigh), government before capitals, maps before ways of living, the vote before the action
  cycle, economics last where the jar splits need adding within 20.
- **Days.** 91 in units, 5 at course level. The heaviest days go to the leaders, symbols and action rows; unit 8 is
  the densest (4 rows, 11 codes, 13 days) but its rows grow kindergarten's economics, so it holds. Ninety minutes a
  week is below the 2.4 hours grades 1 to 4 averaged in the 2011-12 federal survey, which the rows fit.
- **Seams.** Every K row is picked up (the K frame and this frame's table agree row for row). Hand-ons to grade 2
  match the grade 2 frame's "Picked up" table; the five that skip to grade 3 (leaders, voting, national symbols,
  choices, saving) are each met in the grade 3 frame with a readiness check, and the reason for the skip (grade 2
  is a world geography year) is stated.
- **Values and sensitive topics.** Plyler v. Doe (1982) and Barnette (1943) cited; no child's citizenship or family
  asked; Tubman with slavery named plainly; Wilma Mankiller and Native nations as governments today; the class
  election on a class matter, never a candidate.

## Cross-subject

Same-year leans: ELA grade 1 (RI.1.6, RI.1.3, W.1.1), math grade 1 (1.MD.C.4, 1.OA.A.1), science grade 1 (1-ESS1-2),
each with a bridge that lets social studies go first; one earlier-year lean (K-ESS3-1). No ELA, math or science
grade 1 frame exists yet, so "taught first" cannot be checked. Missing lean: finding 3.

## The lens checklist (course frame layer)

| Line | Result |
|---|---|
| An anchor standard in the course's Massachusetts topic range has no unit | Met (MA.1.T4.1 to T4.3 excluded with a recorded reason) |
| The replaced grade 3 year, or "your state" in grade 8, keeps Massachusetts-only content | Not applicable; the own-state method replaces "Governor of Massachusetts" and the state capital (met) |
| No unit lists what the check set adds, or an addition has no recorded source | Met at frame depth |

## What I could not judge

- The other subjects' grade 1 frames (not written).
- Accuracy of the Tubman, Mankiller and Native-government content (flagged for the sensitivity read).

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| Store-flyer prices in unit 8 are made-up whole dollars within 20 | Grade 1 compares and adds within 20; no money or decimals until grade 2 | docs/courses/social-studies-grade-1/frame.md (unit 8, Cross-subject) |
| The three or four places in ss1-ways-of-living do not include Ghana | The grade 3 frame compares a Ghanaian market town in unit 3 unless grade 1 or 2 uses Ghana; keeping it out lets that pick stand | docs/courses/social-studies-grade-1/frame.md (unit 6) |

## For Cory

- **Time a week (audience).** Grade 1 assumes three lessons a week of about 30 minutes (96 days). My read: keep it.

Not logged in the defect ledger (`plan.py defect`): the brief allows edits to this report only. The caller may log
findings 1 to 4 with found_by `expert`.

## Sources

- C3 Framework, NCSS, revised 2017:
  https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf (K-2 and 3-5
  wording of D2.Civ.2 and D2.Civ.6, and every indicator the rows own).
- Massachusetts 2018 as coded in data/standards/ma-hss-2018.txt (MA.1.T3.2a to c; the shared T4 and 2.T5 texts).
- EdWeek (2023), reporting the 2011-12 Schools and Staffing Survey (grades 1 to 4, 2.4 hours a week):
  https://www.edweek.org/teaching-learning/understanding-the-sharp-drop-in-history-and-civics-naep-scores-4-things-to-know/2023/05
  (search summary only).
- Common Core math grade 1 (no money standard): from memory.

## For the source list

See the kindergarten report of the same date (the EdWeek pointer and the C3 PDF address).

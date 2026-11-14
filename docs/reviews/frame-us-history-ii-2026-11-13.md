# Frame read: us-history-ii (US History II, the 1920s to today), 2026-11-13

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/social-studies.md, section 1 of docs/ADOPTION-BAR-SUBJECTS.md,
  docs/courses/social-studies/STANDARD.md, docs/sources/BASE-TEXTS.md (social studies part).
- The frame docs/courses/us-history-ii/frame.md and its row in data/plans/frames.csv (12 units, 160 days).
- The 25 us2-* rows of data/progressions/social-studies.csv, the 25 us1-* rows (there is no US History I frame yet:
  frame:us-history-i is still "Writing" in data/plans/flow-status.csv), the wh2-* and ss8-* rows that hand on to
  us2-* rows, and the frames of US Government and Politics and Economics (the courses beside it in grade 12).
- data/standards/ma-hss-2018.txt, MA.USII.T1 to T5 with every lettered part, read line by line against the rows.
- The partial bases on disk: the outline of Principles of Economics 2e (chapters 2, 3, 17, 27 confirmed) and the
  first page of Since Time Immemorial high school US history units 3 to 6 (confirmed: Indian Reorganization Act;
  termination and relocation; Indian civil rights and self-determination; nation-building and self-determination).
- data/modules.csv (the course's existing topics), data/plans/later.csv (L8), docs/HANDOFF.md, DESK-ANSWERS
  2026-11-13 (q-ss-progression-1).
- Earlier reads: docs/reviews/progression-social-studies-*2026-11-13.md, progression-cross-*2026-11-13.md and the
  only earlier frame read, frame-social-studies-kindergarten-2026-11-13.md.
- Gates: `python -X utf8 scripts/plan.py check` (frame us-history-ii: 0 failures; 12 units, 160 days, 154 in units,
  6 for checks) and `python -X utf8 scripts/stale.py check` (16 files, 0 failures).

## Verdict

The frame is sound: every us2-* row sits in one unit, every MA.USII code is placed and, apart from a few named
items in two option lists, taught in full, the units run in time order with stated reasons, and every seam from US
History I, World History II and grade 8 civics is picked up where the rows say. The biggest risk is the end of
the year: the capstone, the year's only informed action and the ELA 12 shared research all sit in the last 13
days of a senior year, which many schools cut short, and the frame has no short path for it. The one change that
matters most is starting the capstone's question and source set earlier (as a light strand in units 9 to 11) so
unit 12 can shrink without losing the outside audience or the action.

## Findings, most serious first

### 1. The capstone and the year's action sit in the last days of a senior year, with no short path (moderate; judgment call)

**What is wrong.** Unit 12 runs days 148 to 160 and holds the researched argument, its outside audience and the
year's only informed action; the third course-level check sits just before it (days 146 to 147). Many districts end
grade 12 classes one to two weeks before the other grades (senior finals, graduation), and senior attendance drops
in the last weeks. The frame states 160 days for grade 12 like any other year and names no shorter path.
**Evidence.** From memory: early senior release is common district practice; ADOPTION-BAR-SUBJECTS C2 asks every
course for a shorter path.
**Why it matters.** A school that loses 7 days loses the action and the audience step, which are adoption-bar item
8 and the point of unit 12; the ELA 12 pairing loses its shared finish too.
**Fix (frame: course in brief, unit 12 row, course-level checks).** Add one bullet, "**Senior calendar.**": "Grade 12
may end early. The capstone question is chosen at the respond day after unit 7's check (from the exit-routine notes),
and each of units 9 to 11 gives part of one day to the student's source set. Unit 12 then needs 10 days at most; a
school that ends seniors early keeps unit 12's audience and action and cuts unit 11's check-set additions first."
Move the third course-level check's "Respond day sets each student's capstone question" to "Respond day reviews each
student's capstone question and source set". Days stay 160. LAYER frame. REPEAT new.

### 2. Unit 11 cannot hold its two codes and six additions in 10 days (moderate; likely)

**What is wrong.** Unit 11 (10 days) owns MA.USII.T5.5 and T5.6 and lists as check-set additions the 1991 Gulf War,
the 2008 financial crisis, the Affordable Care Act, the presidential elections since 1992, the COVID-19 pandemic and
Native self-government today. After its retrieval opener, end-of-unit assessment and respond day it has about 7
teaching days for three decades of history. Bar item 10 says additions never push the year past its stated days.
**Why it matters.** A unit writer will either drop additions silently or run over into the capstone (finding 1).
**Fix (frame, units 1 and 11 rows).** Unit 1 to 12 days, unit 11 to 11 days (the 2008 crisis in unit 1 stays a
first pass of the panic and the policy response; its full case is unit 11's, as the frame already says "unit 1
returns"). In unit 11's "Check set adds" mark the order of cutting: keep 2008 and Native self-government (one day
each), fold the Gulf War into T5.6's opening as the first post-Cold War use of force, and treat the elections since
1992, the Affordable Care Act and the pandemic as one survey day on a timeline. LAYER frame. REPEAT new.

### 3. Unit 1 "practises" two indicators that only Economics owns (minor; firm)

**What is wrong.** Unit 1's C3 column reads "Practised (owned in Economics or earlier): D2.Eco.1.9-12,
D2.Eco.12.9-12". In the data each is owned by one row only, econ-incentives and econ-fiscal-monetary. The frame's
own suggested timetable puts Economics in the spring half, after this unit, and a student may never take it.
**Why it matters.** "Practised" tells the unit writer the skill was taught before. For most grade 12 students it
was not, so the writer may skip the teaching that MA.USII.T1.10 and T1.11 need anyway.
**Fix (frame, unit 1 C3 cell).** "Met here at US history depth (MA.USII.T1.10, T1.11); Economics owns D2.Eco.1.9-12 and
D2.Eco.12.9-12 and neither course assumes the other. Practised: D2.His.14.9-12 (owned grade 9)." LAYER frame.
REPEAT new.

### 4. Two option lists and one lettered part are not named in full in the rows (minor; firm)

**What is wrong.** Checked against data/standards/ma-hss-2018.txt:
- MA.USII.T4.8a to f: us2-social-movements leaves out items the options name: for women's rights, feminist writers,
  the birth control pill, NOW and the movement's opponents; for disability rights, deinstitutionalization and
  independent living; for the environment, the wetlands protection law; for workers, protections against
  discrimination and harassment; for Native rights, efforts to preserve Native cultures (the row says "revive
  languages", close but narrower).
- MA.USII.T2.1f asks how eugenics affected segregation and immigration as well as sterilization; us2-twenties-tensions
  names only the sterilization laws and Buck v. Bell (the 1924 quotas sit in the same row but are not tied to it).
**Why it matters.** The movement studied in depth is the one the standard is checked on; a writer working from the
row will teach it short.
**Fix (frame, units 2 and 9 "What students learn").** Unit 9: after the list add "the movement studied in depth
carries every item its option names in MA.USII.T4.8a to f, opponents included". Unit 2: "eugenics and its reach
into segregation, the 1924 quotas and forced sterilization, Buck v. Bell (1927)". A frame-text fix; the row notes may
follow in the next progression fix pass. LAYER standard. REPEAT new.

### 5. No cumulative check at the semester line (minor; judgment call)

**What is wrong.** Checks fall after unit 3 (day 42), unit 7 (day 103) and unit 11 (day 147). The semester line is day
80, inside unit 6 (days 68 to 84), so the fall half ends with no cumulative check and the gap between the first two
checks is 61 days.
**Why it matters.** Schools grade by semester and most set a semester exam; teachers will write their own if the
course has none there.
**Fix (frame, course-level checks).** Move the second check to after unit 6 (days 85 to 86): "Cumulative, units 1 to
6, weighted to 4 to 6: an unseen document set on the war or postwar years and a sourced argument". The counterclaim
then enters at unit 7 as the course-wide writing note already says, and unit 7's own end-of-unit assessment asks for
it. Days stay 160. LAYER frame. REPEAT new.

### 6. Unit 8's dates leave out Eisenhower, whom MA.USII.T3.12 names (minor; firm)

**What is wrong.** Unit 8 is titled "1961 to 1975", while T3.12 and us2-vietnam start with Eisenhower's Vietnam policy
(the 1954 Geneva settlement, support for Diem); the models table says "four presidents".
**Fix (frame, unit 8).** Title "Presidents and the war in Vietnam, 1954 to 1975"; in "What students learn" begin the
Vietnam part with "Eisenhower's commitment after 1954". LAYER frame. REPEAT new.

### 7. Row notes still say Government and Economics are grade 12 courses (minor; firm)

**What is wrong.** us2-econ-toolkit, us2-civil-rights-laws and us2-social-movements still carry "the handoff skips 3
grades because grades 9 to 11 are world and US history; government and economics are grade 12 courses", which
q-ss-progression-1 made untrue. The frame names this itself ("For the lead" item 2); it is listed here because it is
still in the data.
**Fix (data/progressions/social-studies.csv, next fix pass).** In those three notes replace the clause with "grade 8
is the last civics course before grade 12; Government and Economics are taken in grade 11 or 12". LAYER progression.
REPEAT yes (progression-social-studies finding 9: boilerplate that no longer fits).

### 8. Stale notes outside the frame (minor; firm)

- docs/HANDOFF.md, block "Step 1, social studies progression, 2026-11-13": "Open for Cory: Desk card q-ss-progression-1
  ... Next: the science, ELA and math progressions". Cory answered the card (DESK-ANSWERS 2026-11-13) and all four
  progressions are done. Fix: "Cory answered q-ss-progression-1 on 2026-11-13 (Government and Economics open to grade
  11 or 12; the eight calls kept)." The same block style says "Open for Cory" for q-ela-progression-1 and
  q-cross-progression-1, both answered the same day; the same fix applies.
- data/plans/flow-status.csv, frame:us-history-ii: "active ... Writing: docs/pipeline/briefs/frame-write.md". The frame
  is written and passes the gate. Fix: "Written; expert and Codex reads under way (docs/reviews/frame-us-history-ii-*)".
LAYER process. REPEAT yes (kindergarten frame read finding 5, progression finding 9).

## Checked and found right (do not undo)

- **Owned skills.** All 25 us2-* rows are placed once. Revisits of grade 10 and 11 content (the Depression, fascism,
  the Holocaust, the bomb, the Cold War blocs, the Soviet collapse, terrorism) are named as content revisited with a
  retrieval opener, never listed as skills.
- **Standards.** Every MA.USII code is owned and placed, including T1.3a to c, T1.9a and b, T2.1a to j, T2.4a to k,
  T3.5a to f, T3.8a to f, T4.5a to d and T4.7a and b. The C3 codes owned here (D2.Geo.8, D2.Geo.9, D2.Civ.12, D4.3 to
  D4.5) match their rows; Geo.8, Geo.9 and D4.3 to D4.5 carry their depth line over grade 10.
- **Order.** Time order from 1913 to today, with three stated thematic choices (unit 7 runs the civil rights laws to
  2023 before unit 8; unit 9 runs movements to 2022 before units 10 and 11; unit 1's toolkit opens the year, as the
  anchor does). No model is used before it is handed on.
- **Seams.** Every us1-* and wh2-* hands_on that names a us2-* row is picked up in the unit the table says.
- **Sensitive topics.** Incarceration never called relocation; Korematsu with its 2018 repudiation; Buck v. Bell with
  its rejection; Tulsa, My Lai and the Klan named plainly; Holocaust testimony with no simulation; Lavender Scare under
  values rule c; Native content flagged for the sensitivity read with Since Time Immemorial units 3 to 6.
- **Own-state method.** The Boston desegregation case is set beside cases from other regions and never taught as
  every student's own state.
- **The ELA 12 pairing.** One question and one source set, each course still teaching the whole cycle alone.

## Seams

Before: US History I has no frame yet, so the rows were read. Every us1-* row whose hands_on names a us2-* row
(research-inquiry, reform-movements, reconstruction, jim-crow, industrialization, immigration, native-west,
women-work-suffrage, progressivism, civil-rights-1900s, wwi, argument-writing) appears in the seam table with the
right unit. us1-news-reading hands on to nothing in grade 12 here; that is right for this course (Government picks
up news literacy). After: none; the frame says where each thread ends. No finding.

Since written (2026-11-13): the US History I frame's 'Handed on' table matches this seam row for row (checked in
frame-us-history-i-2026-11-13.md).

## Cross-subject

Math leans are all earlier grades (Algebra I, math 7 and 8) with retrieval only. ELA 12 leans (W.11-12.7 on
e12-research, SL.11-12.4 on e12-presentation) exist in data/progressions/ela.csv; no ELA 12 frame exists yet, so
"taught first" cannot be checked. The availability calendar is recorded for it. No finding.

## The lens checklist (course frame layer)

| Line | Result |
|---|---|
| An anchor standard in the course's Massachusetts topic range has no unit | Met: every MA.USII code is placed (finding 4 is depth, not placement) |
| The replaced grade 3 year, or "your state" in grade 8, keeps Massachusetts-only content | Not applicable as worded; the own-state method is met for T4.7. T2.1j's Massachusetts events (Bread and Roses, the Boston police strike, Sacco and Vanzetti) are national events and stay |
| No unit lists what the check set adds, or an addition has no recorded source | Met: every unit names its additions and a source line; the frame flags that the exact lines are from memory and are checked at the unit plan. Days for additions: finding 2 |

## What I could not judge

- The exact California, New York and college-framework lines in "Check set adds" (not opened; the unit plan's
  comparison table checks them, as the frame says).
- Accuracy of the Native and hard-history content (the sensitivity read and the qualified person).
- When ELA 12's research weeks fall (no ELA 12 frame yet).

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| The Cold War flashpoint map (T3.10) is one running map started in unit 6 and added to in units 8 and 10 | Most flashpoints (Cuba, Vietnam, Afghanistan, Central America) are taught after unit 6 | docs/courses/us-history-ii/frame.md (unit 6; models table, map-scale) |
| Unit 3 may adapt Principles of Economics 2e chapters 25 and 26 (the Keynesian and neoclassical perspectives) for the T2.2 comparison | The retired CC BY edition on disk holds both accounts the standard asks to compare | docs/courses/us-history-ii/frame.md (base text bullet) |
| Unit 7's other-region desegregation cases: Detroit (Milliken) and Denver (Keyes, 1973) as the Northern and Western cases, Charlotte (Swann) as the Southern contrast | The frame calls Charlotte a Northern case; it is the Southern busing case | docs/courses/us-history-ii/frame.md (unit 7 teacher notes) |

## For Cory

- **What schools are told about the grade 12 timetable** (the frame's "For the lead" item 1). My pick: as the frame
  suggests, Government in the fall half and Economics in the spring for a student taking all three. An added reason:
  Government's unit 6 (parties and elections) then falls around days 48 to 56, near Election Day.

Not logged in the defect ledger: the brief allows edits to this report only. The caller may log findings 1 to 8
with found_by `expert`.

## Sources

- data/standards/ma-hss-2018.txt (Massachusetts 2018, our own words): every USII code and lettered part.
- S:\CurioClass-sources\openstax-retired-ccby\Economics2e-OP_s2jF42u.pdf, outline read with pypdf: chapter numbers.
- S:\CurioClass-sources\since-time-immemorial\high-school-unit-{3..6}-us-history\, first page of each level 1 file:
  unit topics.
- From memory: early release of seniors as common district practice; the C3 9-12 indicator wording for D2.Eco.1,
  D2.Eco.12, D2.Civ.12, D2.Geo.8, D2.Geo.9 and D4.3 to D4.5; Keyes v. School District No. 1 (1973).

## For the source list

Nothing new.

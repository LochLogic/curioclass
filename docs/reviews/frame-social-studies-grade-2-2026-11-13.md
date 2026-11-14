# Frame read: social-studies-grade-2 (Grade 2: Places and Peoples of the World), 2026-11-13

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/social-studies.md, section 1 of docs/ADOPTION-BAR-SUBJECTS.md,
  docs/courses/social-studies/STANDARD.md (sections 1 and 2).
- The frame docs/courses/social-studies-grade-2/frame.md and its row in data/plans/frames.csv (7 units, 96 days).
- The 18 grade 2 rows of data/progressions/social-studies.csv, the grade 1 rows before, the grade 3 rows after;
  data/progressions/social-studies-excluded.csv.
- The frames before and after: docs/courses/social-studies-grade-1/frame.md and
  docs/courses/social-studies-grade-3/frame.md (it exists, so it is the frame after; the outline
  docs/courses/social-studies/grade-3-outline.md was not needed).
- data/standards/ma-hss-2018.txt (MA.2.T1 to T5) and the C3 K-2 indicator wording from the C3 PDF.
- Earlier reads: docs/reviews/progression-social-studies-*2026-11-13.md, progression-cross-*2026-11-13.md. No
  earlier frame read exists.
- Gates: `plan.py check` (frame social-studies-grade-2: 0 failures, 7 units, 96 days); `stale.py check` (0 failures).

## Verdict

The frame is sound and the strongest of the three: a world geography year in a clear order (maps, land and climate,
living with the land, countries and trade, moves, family stories, the country report), every MA.2 standard taught in
full, sourcing taught on maps in unit 1 and used all year, and hard history (enslavement, Cherokee removal, Angel
Island) told plainly at grade level with Native nations in the present. Three lessons a week of 30 to 40 minutes
(96 days) holds for its 18 heavier rows. The biggest risk is unit 7: "any country outside the United States" with
Curio Class's own source sets is a build no one can finish. The one change that matters most is a fixed menu of
countries, settled below; one C3 indicator (D2.Geo.10) also needs its cultural half.

## Findings, most serious first

### 1. The country report has no bounded list of countries (moderate; likely)

**What is wrong.** Unit 7 lets each student choose any country outside the United States and promises "Source sets
are Curio Class's own or open, each with a rights line, so no student needs a library." With about 190 possible
countries, that promise cannot be kept, and the unit writer cannot plan days, sources or reading levels for an open
list.
**Why it matters.** A writer will either build a few sets and leave most choices unsupported (students then hunt the
open web at age seven), or stall. MA.2.T4.3 asks for a report on "a country outside the United States"; it does not
ask for free choice of every country.
**Fix (frame, unit 7 row).** A menu of about 16 countries, at least two from each inhabited continent outside the
United States, each with a Curio Class source set (one map, two short captioned pages, present-day photographs,
rights lines) at a stated grade 2 difficulty. Leave Ghana off the menu so the grade 3 frame's unit 3 comparison
stands, and leave Canada and Mexico off because grade 4 researches them (ss4-canada-mexico-research). A family
country not on the menu is welcome with the teacher's help, never required. Settled below. LAYER frame. REPEAT new.

### 2. D2.Geo.10.K-2 is taught in part: only physical change (moderate; firm)

**What is wrong.** D2.Geo.10.K-2 reads "Describe changes in the physical and cultural characteristics of various
world regions." ss2-climate-regions, which owns it, and unit 2 teach "one region at two dates" with physical pairs
only (a glacier that shrank, a lake that dried, a forest that grew back). Cultural change is not named in the row or
the unit.
**Why it matters.** A standard taught in part is a C1 miss, and the earlier fix pass added only the physical half.
**Fix (progression row ss2-climate-regions notes; frame unit 2 "What students learn").** Add a cultural pair: "and a
town or city at two dates (the same main street in an old and a new photograph: buildings, how people travel, the
languages on signs) to say what changed in how people live there." No day change. LAYER progression and frame.
REPEAT yes (the Codex progression read raised D2.Geo.10 and the fix kept only the physical half).

### 3. The seam to grade 3 still cites the outline, not the grade 3 frame (minor; firm)

**What is wrong.** The "Handed on to Grade 3" table says it is read beside docs/courses/social-studies/grade-3-outline.md
and gives grade 3 units as "Thread" or "Every unit" for four rows. The grade 3 frame now exists and places them:
ss3-primary-secondary in unit 4 (from ss2-source-maker and ss2-two-accounts), ss3-timeline in unit 5 (from
ss2-family-interviews), ss3-inquiry-questions and ss3-claim-evidence in unit 1 (from ss2-country-report and
ss2-claim-sources), ss3-biography in unit 7 (from ss2-country-report).
**Fix.** Point the table's lead-in at docs/courses/social-studies-grade-3/frame.md and replace "Thread" and "Every
unit" with 4, 5, 1, 1 and 7 as above; rename the column "Grade 3 unit". Every row otherwise matches the grade 3
frame's "Picked up" table. LAYER frame. REPEAT new.

### 4. The scale lean names ruler measuring the rows do not use (minor; firm)

**What is wrong.** ss2-map-parts and ss2-make-map lean on math 2.MD.A.1 (measure with a ruler), but both rows count
scale in whole units and say "not yet measured with a ruler". The frame names this under "For the lead" item 2; I
agree with its fix.
**Fix (progression, both rows' cross_subject).** Change the lean to `math:1.MD.A.2` (length as a whole number of
same-size units laid end to end), taught the year before; then the frame's math table row becomes an earlier-grade
lean with no bridge. LAYER progression. REPEAT yes (the progression-cross read repointed mistimed leans).

### 5. D2.Geo.7 is owned in unit 5 but two of its three parts are taught elsewhere, unnamed (minor; firm)

**What is wrong.** D2.Geo.7.K-2 is "Explain why and how people, goods, and ideas move from place to place." Its
owner, ss2-why-people-move in unit 5, teaches people. Goods move in unit 4 (ss2-trade-world) and ideas in unit 6
(ss2-culture-migration), so the course teaches the indicator in full, but neither the row nor unit 5 says so.
**Why it matters.** A coverage trace from the owning row finds only people, and a unit 5 writer may think goods and
ideas are left to them.
**Fix (frame unit 5 "What students learn"; one sentence in the row's notes).** Add: "People, goods and ideas all
move: goods were traced in unit 4; what moves with people (foods, words, music) is unit 6." LAYER frame. REPEAT new.

### 6. Stale notes: three lines are already answered (minor; firm)

**What is wrong.** (a) "For the lead" item 4: frames.csv is not synced and the gate disagrees; frames.csv holds
`social-studies-grade-2,7,96` and the gate passes. (b) "For the lead" item 3 and the sentence under the seam table
("One note for the grade 3 frame ..."): the grade 3 frame's unit 7 already says the class chooses its problem afresh
and builds on grade 2's storm-readiness work only if it chooses to. (c) The seam lead-in naming the outline (finding 3).
**Fix.** Delete item 4; replace item 3 and the seam sentence with "Settled in the grade 3 frame (unit 7): the class
chooses its problem afresh." LAYER process. REPEAT new.

## Checked and found right (do not undo)

- **Owned skills.** All 18 rows placed once; source-sourcing, claim-evidence-reasoning, timeline and continuity-change
  reuse is named as review. Two shared C3 codes (D2.Geo.1 with K, D4.1 with K) carry depth lines in the rows.
- **Standards in full.** MA.2.T1.1 to T4.3 and T5.1 to T5.3 each sit in a unit, including the parts a busy writer
  misses (maps showing how people relate to their environment, why oceans matter, physical against political
  geography with Africa). MA.2.T5.4 to T5.9 are excluded with a reason pointing at grade 1. The other C3 indicators
  owned match their wording (D3.1's "origin and structure to guide the selection" is in the country report row).
- **Order.** Maps first; regions before the units that use them; resources before trade; why people move before the
  interviews that ask it; the country report last, gathering every unit. Claim with a named source taught in unit 2
  on top of unit 1's sourcing card.
- **Days.** 91 in units, 5 at course level. Unit 3 is the most loaded per day (3 rows, 11 owned codes and the action
  cycle in 16 days, against unit 1's 4 rows and 6 codes in 16), but not far enough off its share to move days at the
  frame; the scope and sequence should keep the action cycle's carry-out to about 4 lessons. Ninety to 120 minutes a
  week is near the 2.4 hours grades 1 to 4 averaged in the 2011-12 federal survey.
- **Seams.** Every grade 1 hand-on is picked up (the grade 1 frame's table and this one agree). Every grade 2 row
  hands on to grade 3, and each is answered by a grade 3 row's assumes and the grade 3 frame's table.
- **Values and hard history.** Forced moves named plainly with the human side; the Cherokee Nation and the Eastern
  Band in the present; Angel Island's exclusion law told plainly; no simulation of capture, removal or flight; no
  child asked for a family or immigration story; storm examples told calmly, readiness checked against published
  advice.

## Cross-subject

Same-year leans: ELA grade 2 (RI.2.6, W.2.1, RI.2.9, SL.2.3, W.2.7), math grade 2 (finding 4), science grade 2
(2-ESS2-2), each with a bridge; earlier-year science leans (K-ESS2-1, K-ESS3-1, K-ESS3-3). No ELA, math or science
grade 2 frame exists yet, so "taught first" cannot be checked.

## The lens checklist (course frame layer)

| Line | Result |
|---|---|
| An anchor standard in the course's Massachusetts topic range has no unit | Met (MA.2.T5.4 to T5.9 excluded with a recorded reason) |
| The replaced grade 3 year, or "your state" in grade 8, keeps Massachusetts-only content | Not applicable; MA.2.T3.3's "came to Massachusetts" becomes "this town or state" (met) |
| No unit lists what the check set adds, or an addition has no recorded source | Met at frame depth |

## What I could not judge

- The other subjects' grade 2 frames (not written).
- Accuracy of the removal, enslavement and Angel Island content (flagged for the sensitivity read).

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| Unit 7 country menu: about 16 countries, at least two per inhabited continent outside the United States; Ghana, Canada and Mexico left off; a family country outside the menu welcome with teacher help | Makes the source-set promise buildable; avoids grade 3's Ghana comparison and grade 4's Canada and Mexico research | docs/courses/social-studies-grade-2/frame.md (unit 7) |
| D2.Geo.10's cultural pair is one main street at two dates (buildings, travel, languages on signs) | Concrete, photographable, open archive photos exist for most towns | data/progressions/social-studies.csv (ss2-climate-regions); frame unit 2 |

## For Cory

- **Time a week (audience).** Grade 2 assumes three lessons a week of 30 to 40 minutes (96 days). My read: keep it.
  The step to grade 3's daily 40-minute block (160 days) is the grade 3 frame's question for you.

Not logged in the defect ledger (`plan.py defect`): the brief allows edits to this report only. The caller may log
findings 1 to 6 with found_by `expert`.

## Sources

- C3 Framework, NCSS, revised 2017:
  https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf (wording of
  D2.Geo.7, D2.Geo.10, D3.1 and every K-2 indicator the rows own).
- Massachusetts 2018 as coded in data/standards/ma-hss-2018.txt (MA.2.T1 to T5; MA.2.T4.3's "a country outside the
  United States").
- EdWeek (2023), reporting the 2011-12 Schools and Staffing Survey (grades 1 to 4, 2.4 hours a week):
  https://www.edweek.org/teaching-learning/understanding-the-sharp-drop-in-history-and-civics-naep-scores-4-things-to-know/2023/05
  (search summary only).
- Common Core math 1.MD.A.2 and 2.MD.A.1: from memory.

## For the source list

See the kindergarten report of the same date (the EdWeek pointer and the C3 PDF address).

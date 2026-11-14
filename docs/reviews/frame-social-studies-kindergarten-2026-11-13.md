# Frame read: social-studies-kindergarten (Kindergarten: Living and Learning Together), 2026-11-13

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/social-studies.md, section 1 of docs/ADOPTION-BAR-SUBJECTS.md,
  docs/courses/social-studies/STANDARD.md (sections 1 and 2).
- The frame docs/courses/social-studies-kindergarten/frame.md and its row in data/plans/frames.csv (6 units, 64 days).
- The 19 grade K rows of data/progressions/social-studies.csv, and the grade 1 rows they hand on to.
- The frame after: docs/courses/social-studies-grade-1/frame.md. There is no course before.
- data/standards/ma-hss-2018.txt (MA.K.T1 to T4 with lettered parts) and the C3 K-2 indicator wording, read from the
  C3 PDF itself (downloaded and extracted; address under Sources), not from memory.
- Earlier reads: docs/reviews/progression-social-studies-*2026-11-13.md and progression-cross-*2026-11-13.md. No
  earlier frame read exists, so every frame-layer finding below is REPEAT new unless marked.
- Gates: `python -X utf8 scripts/plan.py check` (frame social-studies-kindergarten: 0 failures, 6 units, 64 days) and
  `python -X utf8 scripts/stale.py check` (0 failures).

## Verdict

The frame is sound: all 19 kindergarten rows sit in one unit each, every MA.K standard and its lettered parts are
taught in full, every C3 K-2 indicator the rows own matches its wording, and every row hands on to the grade 1 row
that assumes it. The time it assumes (about two 20 to 30 minute lessons a week, 64 days) holds for these short
talk-and-play rows and sits near what primary classrooms really give social studies. The biggest risk is the
calendar: unit 5's careful holiday notes (Thanksgiving from the record and from Wampanoag people, no costume play)
arrive in February, months after teachers have already taught Thanksgiving, Indigenous Peoples' Day or Columbus Day,
Veterans Day and Martin Luther King Jr. Day without them. The one change that matters most is giving each civic
holiday a short on-the-day lesson, paid for from unit 5's days, that carries its teacher note.

## Findings, most serious first

### 1. The holiday notes arrive after the holidays (moderate; likely)

**What is wrong.** Unit 5 says it sits mid-year "so Martin Luther King Jr. Day and Presidents' Day fall inside it",
and that earlier holidays "are only named on the class calendar on the day". The arithmetic does not hold for King
Day: units 1 to 3, the mid-year check and the respond days take 34 lessons (teaching week 17 at two a week), and
unit 4 takes 7 more, so unit 5 opens at lesson 42, teaching week 21. With a Thanksgiving week and a two-week winter
break, that is about calendar week 23 or 24 of a September start: early to mid February, after King Day (third
Monday of January) and just before Presidents' Day. Indigenous Peoples' Day or Columbus Day (October), Veterans Day
and Thanksgiving (November) fall in units 2 and 3.
**Why it matters.** Kindergarten teachers teach Thanksgiving in November whatever the course says. With nothing
from Curio Class on that day, the likely default is the paper-headdress craft the frame forbids, and the Wampanoag
account the row requires comes three months late. The same holds for King Day.
**Fix (frame, unit 5 row and course brief).** Take 3 of unit 5's 11 days as on-the-day holiday lessons, taught when
each date falls: one for Indigenous Peoples' Day or Columbus Day as the community observes it, one for Veterans Day
with Thanksgiving (or one for Thanksgiving alone if the class calendar puts them in different weeks), and one for
Martin Luther King Jr. Day. Each carries the row's teacher note (Thanksgiving from the record and from Wampanoag
people today, no headdress or costume play; King's work against unfair laws named plainly). Unit 5 keeps 8 days,
opens by placing these remembered days on the school-year strip, and teaches Presidents' Day, the symbols and the
traditions. Rewrite "Why this unit, here" to: "Placed so Presidents' Day falls inside it; civic holidays earlier in
the year get an on-the-day lesson from this unit's days, gathered on the timeline when the unit opens." Course days
stay 64. LAYER frame. REPEAT new.

### 2. The year's informed action has no problem in it (moderate; likely)

**What is wrong.** The informed action (unit 2, ssk-class-decision, D4.8.K-2) is a real class decision, but the
examples are "a plant's name, a game". The adoption bar's item 8 asks students to apply what they concluded "to a
real problem near them"; naming a plant is a choice, not a problem, and nothing the class learned informs it.
**Why it matters.** Item 8 is scored, and a reviewer reading the unit would mark this as voting practice, not
informed action. It also wastes the best chance in the year to tie unit 1's "a rule has a reason" to action.
**Fix (frame, unit 2 row and the Informed action bullet; progression row ssk-class-decision notes).** The decision
is about a real classroom problem the class names in unit 1 or 2 (crowding at the coat hooks, sharing the block
corner, keeping the reading corner tidy): the class hears reasons, tries for agreement, votes by hands or blocks,
acts on the result, and looks back after a week at whether it helped. Keep naming the class plant as a warm-up
vote, not as the action. LAYER frame (and progression for the row's examples). REPEAT new.

### 3. The class store needs money kindergarten math does not teach, and no lean is recorded (minor; firm)

**What is wrong.** Unit 6's class store uses "play money", and its reason says the counting the store needs is
secure in math by spring, but the Cross-subject section has no row for unit 6. Kindergarten Common Core math has no
money; coin values come in 2.MD.C.8.
**Why it matters.** A writer reading "play money" will likely print coins and dollar bills, and five-year-olds
cannot add mixed values.
**Fix (frame, Cross-subject, Mathematics kindergarten).** Add a row: ssk-needs-wants-trade and
ssk-goods-services-money, lean K.CC.B.5 (count to tell how many), unit 6, about week 27; bridge: the store's money
is tokens each worth one, prices 1 to 5 tokens (settled below). LAYER frame. REPEAT yes (the progression-cross
read found leans that were missing or mistimed).

### 4. The symbols sort is pitched above pre-readers as written (minor; a judgment call)

**What is wrong.** ssk-national-symbols asks students to sort each statement into "the record says" or "people
say it means", with 1777, 1782 and 1931 as the record. The idea is right (it is how the row answers MA.K.T1.4a
honestly: the flag law gave the colors no meaning), but done with written statements and dates it is a reading
and history-of-documents task for children who mostly cannot read yet. The unit 5 C3 column also files the sort
under "D2 Civics", and no C3 K-2 civics indicator is about it; it is closest to D2.His.10.K-2 (how sources are used
to study the past), owned in unit 4.
**Why it matters.** A busy writer will copy the row's dates and statements onto a student page.
**Fix (frame, unit 5 row).** Add to the teacher note: the sort is spoken and teacher-led, at most two statements
per symbol, with two picture bins (an old paper for "the record says", a speech bubble for "people say"); dates are
said by the teacher ("long, long ago, in 1777") and are not on the student page. Change the C3 cell to "D2.His.10
(review: an old paper as a clue)". LAYER frame. REPEAT new.

### 5. Stale note: frames.csv is already synced (minor; firm)

**What is wrong.** "For the lead" item 2 says `frame.py sync` was not run and "the frame gate reports the csv as
disagreeing until the lead runs it". data/plans/frames.csv holds `social-studies-kindergarten,6,64`, and the gate
passes with 0 failures.
**Fix.** Delete item 2 (or replace it with "data/plans/frames.csv synced: 6 units, 64 days; the gate passes").
LAYER process. REPEAT new.

## Checked and found right (do not undo)

- **Owned skills.** All 19 K rows are placed once; no unit's Skills column holds another grade's row. Review uses
  (perspective in unit 2, claim-evidence-reasoning closings, map-key in unit 6) are named as review in the text.
- **Standards in full.** MA.K.T1.1 to T4.3 each sit in a unit; MA.K.T1.4a to d (colors, stars and stripes, eagle,
  anthem, Pledge's words) and MA.K.T3.3a and b (sequence words, time words) are taught in full in their rows. The
  C3 indicators owned (D1.1, D2.Civ.3, 7, 9, 10, 11, 12, D2.Eco.1, 3, D2.Geo.1, 2, D2.His.1, 2, 10, D4.1, 4.4, 4.8)
  match the C3 wording; D2.Civ.12.K-2 asks how rules work in classroom and school settings, which ssk-rules-why does.
- **Order.** Talk rules and the spoken claim before every unit that closes on them; position words before maps;
  the timeline before holidays and symbols; jobs before work. No skill or model is used before it is taught.
- **Days.** 58 in units, 6 at course level. Unit loads follow the rows (unit 4 at 7 days for two light rows; units 3
  and 5 heaviest). About 50 to 60 minutes a week is below the 2.4 hours grades 1 to 4 averaged in the last federal
  survey (2011-12), and survey data show primary grades get less than grades 3 to 5, so the assumption is honest
  for kindergarten and the rows fit it.
- **Seams.** Every K row hands on to a grade 1 row, and the grade 1 frame's "Picked up" table answers each one.
  All five models (perspective, claim-evidence-reasoning, map-key, timeline, continuity-change) go on to grade 1.
- **Values and sensitive topics.** Barnette (1943) for the Pledge; Thanksgiving from the record and from Wampanoag
  people now; no costume play; no child's address, chores, family photos or tradition required.

## Seams

No course before. Hand-on to grade 1: matched row for row (19 rows, 18 grade 1 rows picking them up). No finding.

## Cross-subject

All leans are same-year ELA K (SL.K.1, SL.K.3, W.K.1, RL.K.3, RI.K.3, RI.K.1) and math K (K.CC.B.5, K.G.A.1), each
with a bridge that lets social studies go first. No ELA, math or science kindergarten frame exists yet
(docs/courses/ holds none), so "taught first" cannot be checked; the needs are recorded for those frames. Missing
lean: finding 3.

## The lens checklist (course frame layer)

| Line | Result |
|---|---|
| An anchor standard in the course's Massachusetts topic range has no unit | Met: every MA.K code placed |
| The replaced grade 3 year, or "your state" in grade 8, keeps Massachusetts-only content | Not applicable to K; the own-state method is used for MA.K.T2.3 (met) |
| No unit lists what the check set adds, or an addition has no recorded source | Met: every unit names its expected addition and the state it comes from; the unit plan's table records the document |

## What I could not judge

- Whether the ELA and math kindergarten frames will teach their leans in time (not written yet).
- Accuracy of the Wampanoag and King Day content (the sensitivity read and a qualified person, as flagged).

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| Class store money is tokens each worth one; prices 1 to 5 tokens | Kindergarten counts to 20 and has no coin values | docs/courses/social-studies-kindergarten/frame.md (unit 6, Cross-subject) |
| The symbols sort uses at most two spoken statements per symbol, with picture bins; dates said by the teacher only | Pre-readers; keeps MA.K.T1.4a honest without a reading task | docs/courses/social-studies-kindergarten/frame.md (unit 5) |

## For Cory

- **Time a week (audience).** Kindergarten assumes about two 20 to 30 minute lessons a week (64 days). My read: keep
  it; it is near what kindergarten classrooms give the subject, and the rows fit it.

Not logged in the defect ledger (`plan.py defect`): the brief allows edits to this report only. The caller may log
findings 1 to 5 with found_by `expert`.

## Sources

- C3 Framework, NCSS, revised 2017 (PDF, downloaded and extracted for this read):
  https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf. Used for the
  wording of every K-2 indicator the rows own.
- Massachusetts 2018 framework as coded in data/standards/ma-hss-2018.txt: lettered parts of MA.K.T1.4 and T3.3.
- EdWeek, "Understanding the sharp drop in history and civics NAEP scores" (2023), reporting the federal Schools and
  Staffing Survey 2011-12 figure (grades 1 to 4: 2.4 hours a week of social studies):
  https://www.edweek.org/teaching-learning/understanding-the-sharp-drop-in-history-and-civics-naep-scores-4-things-to-know/2023/05.
  Read through a search summary only; the article itself was not opened.
- Common Core math, kindergarten and grade 2 (money in 2.MD.C.8): from memory.

## For the source list

- The EdWeek article above, as a pointer to the 2011-12 Schools and Staffing Survey time-on-subject figure (useful
  for any "time a week" judgment). The survey table itself was not reached.
- The C3 PDF address (already noted by the social studies progression read as missing from
  docs/APPROACH-SOURCES.md): it downloads with curl and extracts cleanly with pypdf.

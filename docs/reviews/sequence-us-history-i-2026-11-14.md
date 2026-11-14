# Sequence read: us-history-i (US History I, 1754 to 1920, grade 11, full year), 2026-11-14

Expert cold read per docs/pipeline/briefs/sequence-read.md. Independent of any other read of this scope and sequence.

## What I read

AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/social-studies.md; the social studies part of
docs/ADOPTION-BAR-SUBJECTS.md; docs/courses/social-studies/STANDARD.md; docs/courses/us-history-i/frame.md (units,
course-level checks, cross-subject, the shared research brief with ELA 11); docs/courses/us-history-i/scope-and-sequence.md;
data/plans/us-history-i/days.csv (all 160 rows); data/plans/us-history-i/source-map.csv (the Since Time Immemorial
partial base, every row); the 27 us1-* rows of data/progressions/social-studies.csv and the earlier rows they assume; the
MA.USI lines of data/standards/ma-hss-2018.txt; docs/courses/CALENDAR.md and the grade 11 rows of data/plans/calendar.csv
(ELA 11's units and checks); the cross-subject and process-writing lines of
docs/courses/english-language-arts-grade-11/frame.md; docs/pipeline/briefs/sequence-write.md rule 2; the earlier sequence
reads of this date (not the Codex reads).

Gates: `plan.py check`: sequence us-history-i 0 failures, frame 0 failures. `frame.py calendar`: 9 units, 160 days (148
in units, 12 for checks and respond days), no break. `stale.py check`: 0 failures. Every unit and check in days.csv
matches data/plans/calendar.csv. Script checks: all 59 MA.USI codes and lettered parts appear on at least one day; for
every earlier-grade row the days name, the last grade that used it across all social studies days.csv files.

## Verdict

A sound year: nine units in time order (unit 4's thematic 1800 to 1860 with its reason), every MA.USI code and lettered
part on a named day, the shared reform paper placed exactly on the brief's milestones with ELA 11, hard history taught
plainly with the nations' and communities' own sources, and the partial base used on three days and cut elsewhere with
reasons. The biggest risks are two days that cannot run as written: the informed action is decided but never taken or
looked back on (finding 1), and essay 2 asks for written feedback between two consecutive days (finding 2). Fix those
first; the rest are small moves inside units.

## Findings, most serious first

### 1. The informed action is decided but never taken or looked back on (moderate; likely). LAYER sequence. REPEAT yes (informed-action timing, Government, US History II and World History II reads)

**What is wrong.** Day 136 chooses a local problem and judges the options; day 137 "decide whether and how to act". No
day takes the action and none looks back. Choosing the problem and weighing options from evidence in one 50-minute day
is also thin. Bar item 8 asks students to apply what they concluded to a real problem near them; deciding is not
applying.

**Fix (days.csv rows 126, 137, 160; scope-and-sequence.md unit 8 arc).** Day 126 note adds "each student notes one
present-day local problem like the one this policy targeted: the start of the informed action". Day 137: "Informed
action, step 2: decide, then take the action through an adult (or record a reasoned choice not to act), at the scale
nearest the student". Day 160 note adds "look back on the informed action: the response or its absence so far, and what
the student would do next; no visible change is needed for the action to count". When Government runs the same year,
the look back follows Government's action instead. Settled by the expert, the same call as the other reads of this date.

### 2. Essay 2 needs written feedback overnight (moderate; likely). LAYER sequence. REPEAT new

**What is wrong.** Days 88, 89 and 90 are essay 2 draft 1, "revise from written feedback" and the final, on three
consecutive days. A teacher cannot return written feedback on a several-page essay for a full roster overnight, so draft
2 runs without it and the three-draft cycle the frame owns (D3.4, D4.1) collapses into two. Essay 1 is fine (four days
between draft 1 on day 77 and draft 2 on day 81).

**Fix (days.csv rows 88 to 92; scope-and-sequence.md unit 5 arc).** Reorder the unit's last five days: 88 essay 2 draft 1
(unchanged); 89 the end-of-unit assessment (now day 91); 90 its respond day (now day 92); 91 essay 2 draft 2; 92 essay 2
draft 3, final. Codes travel with their days. The unit then closes on its second full essay, and feedback has two school
days. Settled by the expert (a reorder inside the unit; no day count changes).

### 3. Day 1's readiness check leaves out two rows unit 1 leans on, and unit 8 does not name a retrieval (minor; firm). LAYER sequence. REPEAT yes (readiness calls in the Civics, WGAC II, grade 5 and World History II reads)

**What is wrong.** (a) Day 4 reviews lateral reading from ss8-news-literacy, last used in grade 9 (World History I), and
day 16 links to wh1-renaissance (significance), which us1-revolution-war assumes and only grade 9 used. Both are two
grades back, so the settled rule puts them in unit 1's opening readiness check; day 1 names only ss5-revolution-causes and
ss8-declaration. (b) us1-progressivism assumes wh2-industrial-ideas-reform (grade 10, and day 55 this year); no unit 8 day
names its retrieval.

**Fix (days.csv rows 1, 4, 16, 123, 144).** Day 1 goal: "Readiness check on grade 5's French and Indian War, grade 8's
road to independence and news literacy, and grade 9's significance judgment, then ..."; note adds "ss8-news-literacy
(last used grade 9), wh1-renaissance (last used grade 9)". Day 4 note: "retrieval task: ss8-news-literacy opened at the
readiness check". Day 16 keeps its worked example. Day 123 note adds "retrieval task: wh2-industrial-ideas-reform (met on
day 55)". Day 144's review of ss8-news-literacy is then a retrieval of a row used earlier the same year: right as it
stands. Settled by the expert.

### 4. Two course-level checks repeat the assessment days before them (minor; likely). LAYER sequence. REPEAT yes (Civics, WGAC I and II, World History II finding 4)

**What is wrong.** (a) Unit 5's assessment (day 91; day 89 after finding 2) is "a causal explanation task on unseen
sources" on the sectional crisis; the mid-year check's day 94 is "a long-term cause against trigger argument from unseen
sources" on the same question. (b) Unit 9's assessment (day 154) reads an unseen news item and carries MA.NML.T4.2 (a
site's credibility); the year-end check's day 158 is a news-reading task on an unseen site four days later. Each check
then measures what was just measured.

**Fix (days.csv rows 91, 154, 158).** Day 91's causal task asks how and why Reconstruction ended (D4.2 kept), so day 94
is the first cold argument on why war came. Day 154 tests news against opinion (MA.NML.T1.5) on an unseen 1898-style
pair and drops MA.NML.T4.2, which moves to day 158's codes beside T4.1 and T4.3. Settled by the expert.

### 5. Days 20, 54 and 107 each carry more than one lesson (minor; likely). LAYER sequence. REPEAT yes (overloaded days, grade 2 and World History I reads)

**What is wrong.** Day 20 holds a readiness check on five rows, a retrieval, why the Articles were adopted and their
weaknesses, and the Northwest Ordinance. Day 54 joins two standards and four topics: 1840s immigration and the Irish
famine (MA.USI.T3.2c), the Great Awakenings, Republican Motherhood and anti-Catholic nativism (MA.USI.T4.1). Day 107 holds
three Supreme Court cases, citizenship told apart from voting, and the Chinese and Mexican American West.

**Fix (days.csv rows 20, 21, 54 to 56, 107; candidate table).** Move the Northwest Ordinance to day 21 beside Shays'
Rebellion (both 1786 to 1787 acts of the Confederation; candidate cell day 20 becomes 21). Day 54 keeps immigration and
anti-Catholic nativism; the Second Great Awakening and Republican Motherhood open day 55 as the roots of the reforms its
survey covers, and day 55's reading of the reform question set moves to day 56, where the question is written;
MA.USI.T4.1 goes on days 54 and 55. Day 107's Chinese and Mexican American West moves to the day's survey pages as the
cases' setting (Chinese exclusion is taught on day 118). Settled by the expert.

### 6. The Red Summer of 1919 has a home in this course (minor; judgment call). LAYER sequence. REPEAT new

**What is wrong.** For the lead 1 drops the Red Summer for want of a day in unit 9 and asks for a change to US History
II's frame, a course another writer owns. Day 135 already judges "how far Black Americans reached their goals by 1920,
with the start of the Great Migration"; the Red Summer is the evidence that judgment needs, inside the unit's dates and
under MA.USI.T7.4.

**Fix (days.csv rows 135, 151; scope-and-sequence.md candidate table and For the lead 1).** Day 135 goal: "... with the
start of the Great Migration and the Red Summer of 1919 that met it"; its sensitivity note stays and adds "violence named
plainly". Candidate cell: kept, day 135, 0 added. Day 151 note drops the Red Summer line. For the lead 1 closes; no
change to US History II's frame is needed. Settled by the expert.

### 7. A school without ELA 11 finishes the paper and gives every talk on day 69 (minor; judgment call). LAYER sequence. REPEAT yes (a school teaching alone, World History II finding 6)

**What is wrong.** Day 69: "a school without ELA 11 hands it in and gives the talks today". Finishing a final draft and
hearing a whole class's talks in one 50-minute day cannot both happen. The talk is ELA's (SL.11-12.4), which this course
does not own; history scores the paper for historical reasoning only (day 71).

**Fix (days.csv row 69).** Note: "a school without ELA 11 hands the paper in today; history scores the paper only, and
the talk belongs to the school's ELA course". Settled by the expert.

### 8. Stale "idle" notes on three days and in the scope and sequence (minor; firm). LAYER sequence. REPEAT yes (stale notes in earlier reads of this date)

**What is wrong.** Days 1, 35 and 72 and the scope and sequence's readiness paragraph say grade 5 rows are "idle grades 6
to 10". ss5-revolution-causes (day 1) and ss5-civil-war (day 72) are used in grade 8 Civics; ss5-republic-growth (day 35)
in grade 6. The readiness call is still right (each is two or more grades back), but the notes are wrong.

**Fix (days.csv rows 1, 35, 72; scope-and-sequence.md readiness paragraph).** Day 1: "ss5-revolution-causes (last used
grade 8)"; day 72: "ss5-civil-war (last used grade 8)"; day 35: "ss5-republic-growth (last used grade 6)". The paragraph:
"each on a grade 5, 8 or 9 row last used two or more grades back" (grade 9 after finding 3).

## The readiness versus retrieval call, and the held look-back days

The writer's call is right for units 2 to 6 and 8 (every grade 5 and grade 8 row named is two or more grades back) and
for units 7 and 9 (World History II rows, the year before). Every World History I row the days retrieve
(wh1-sources-of-the-past, wh1-enlightenment, wh1-constitutional-democracy, wh1-empires-1600s, wh1-atlantic-slave-trade)
was used again in World History II, so retrieval is right. Rows met earlier the same year (ss5-native-sovereignty-removal
on day 102, ss5-jim-crow on day 133) are retrieval: right. The one change is finding 3: ss8-news-literacy and
wh1-renaissance join day 1's readiness check. Every cross-subject lean is on ELA 11 and the course needs nothing from ELA
first, so none of them sets a readiness check.

No held look-back day shifts a unit. Every unit and check in days.csv matches data/plans/calendar.csv; nothing to sync.

## Checked and found right (do not undo)

- Standards in full: all 59 MA.USI codes and lettered parts on a teaching day and in their unit's assessment; MA.NML
  T1.5, T2.1, T2.2, T3.2 and T4.1 to T4.3 on days; MA.USI.T6.3's one listed topic and T7.2's one researched policy each
  have survey pages and an in-depth day; T7.5's report rests on survey days covering every lettered part; T7.8's League debate is
  argued from period positions, not personas.
- The shared reform paper: question by the end of week 12 (day 56), source list week 13 (day 61), draft week 14 (day 66),
  paper and talk week 15 in ELA's days, scored on day 71. This matches ELA 11's frame milestone calendar exactly, and ELA
  11's own process pieces avoid weeks 12 to 19 and week 31, where the empire report is due (day 153).
- ELA 11 leans meet: the Declaration on day 11 and the Constitution by week 7, before ELA reads them from week 8;
  Douglass excerpts on day 62 (week 13) before ELA's whole Narrative in weeks 17 to 19; tenement sources on day 119
  (week 24) before ELA's Riis unit (weeks 27 to 28); the reform era (weeks 11 to 15) before The Scarlet Letter (weeks 20
  to 24).
- The calendar: check 1 in week 10, the mid-year check in weeks 19 to 20, the year-end check in week 32, each on
  CALENDAR.md's target.
- The partial base: Since Time Immemorial unit 1 Level 1 on day 25 and unit 2 Level 2 on days 104 and 105, each named
  with its licence and the credit that the content is the tribes'; every other unit and level cut with a reason; the
  base's own order kept; "ours" rows for both sections that hold base days.
- Hard history: removal with the Removal Act's votes, the speeches and the Cherokee memorials, and the five nations today;
  slavery's economy North and South; the Lost Cause tested against the record and never balanced as a view; lynching,
  Wounded Knee and boarding schools named plainly, with a choice of text where content may touch families; slurs never
  printed; no role play; Native nations in the present tense from their own pages.
- Writing grows: short sourced claims in units 1 to 3, the shared research paper, two three-draft essays in unit 5,
  the empire report as the third.
- No unit over 25 days; response time counted once per unit; one informed action, the student's choice.
- Unit 6 answers its compelling question inside the assessment (day 108) rather than on a claim day: acceptable in a
  13-day unit, and the question spans both halves of the unit.
- For the lead 2 (the resumed run's corrections) and 3 (Since Time Immemorial levels left out): accept.

## Lens checklist, scope and sequence layer

| Line | Met? |
|---|---|
| Unit question answerable without the unit's sources, or one defensible answer | Met: all nine are open |
| History out of time order with no reason | Met: unit 4 is thematic across 1800 to 1860 and units 6 and 7 overlap in time, each with its reason |
| A contested event with one telling | Met: removal, Reconstruction and the Lost Cause each carry more than one account |
| Writing from sources once a year or never builds short to long | Met |

## Candidate cells

| Cell | Settled in the draft | My read |
|---|---|---|
| Colonial self-government before 1763; Second Continental Congress and Olive Branch Petition (unit 1) | Kept, days 1, 10 | Right |
| Northwest Ordinance (unit 2) | Kept, day 20 | Right, on day 21 (finding 5) |
| Whiskey Rebellion (unit 2) | Kept, day 29 | Right |
| Tecumseh and the Shawnee-led confederacy (unit 3) | Kept, day 41 | Right |
| Temperance and prison reform; the Lowell mill workers' magazine (unit 4) | Kept, days 55, 53 | Right |
| Lincoln-Douglas debates and John Brown's raid; Homestead and railroad acts (unit 5) | Kept, days 74, 79 | Right |
| Populists and the Omaha Platform (unit 6) | Dropped, named as context on day 123 | Right |
| Chinese and Mexican American West (unit 6) | Kept, day 107 | Right, on day 107's survey pages (finding 5) |
| Political machines; Triangle fire (unit 7) | Kept, days 113, 114 | Right |
| 16th and 17th Amendments, direct democracy (unit 8) | Kept, day 126 | Right |
| Anti-imperialist arguments (unit 9) | Kept, day 143 | Right |
| Red Summer of 1919 (unit 9) | Dropped, no day free | Keep, on day 135 in unit 8 (finding 6) |

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Day 126 starts the informed action; day 137 takes it; day 160 looks back | Informed action was decided but never taken | data/plans/us-history-i/days.csv rows 126, 137, 160 |
| Essay 2 draft 1, assessment, respond, draft 2, draft 3 on days 88 to 92 | Written feedback needs time between drafts | days.csv rows 88 to 92 |
| ss8-news-literacy and wh1-renaissance join day 1's readiness; day 123 names its retrieval | The settled readiness rule | days.csv rows 1, 4, 123 |
| Day 91 tests Reconstruction's end; MA.NML.T4.2 moves from day 154 to day 158 | Checks repeated the assessments just before | days.csv rows 91, 154, 158 |
| Northwest Ordinance to day 21; Awakenings and Republican Motherhood to day 55; day 107's candidate to survey pages | Days 20, 54, 107 overloaded | days.csv rows 20, 21, 54 to 56, 107 |
| Red Summer kept on day 135 | A natural home inside the course's dates | days.csv rows 135, 151; scope-and-sequence.md |
| Day 69: a school alone hands the paper in; no talk in history | The talk is ELA's code | days.csv row 69 |
| "Last used" notes on days 1, 35, 72 | Stale "idle" wording | days.csv rows 1, 35, 72; scope-and-sequence.md |

## For Cory

None.

## Sources

- data/standards/ma-hss-2018.txt (Massachusetts 2018, ids and our words): every USI and NML code checked against the
  days by script and by reading.
- data/standards/c3-indicators.txt: owned indicator ids.
- Since Time Immemorial (Washington OSPI, CC BY 4.0), through the source map; not re-opened.
- All social studies days.csv files under data/plans/ (for the last grade that used each earlier row).
- `plan.py check`, `frame.py calendar`, `stale.py check` output of 2026-11-14.

Confidence: findings 3 and 8 firm; 1, 2, 4 and 5 likely; 6 and 7 judgment calls.

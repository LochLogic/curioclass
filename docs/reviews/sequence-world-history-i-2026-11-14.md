# Sequence read: world-history-i (World History I, about 500 to 1800, grade 9, full year), 2026-11-14

Expert cold read per docs/pipeline/briefs/sequence-read.md. Independent of any other read of this scope and sequence.

## What I read

AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/social-studies.md; the social studies part of
docs/ADOPTION-BAR-SUBJECTS.md; docs/courses/social-studies/STANDARD.md; docs/courses/world-history-i/frame.md (course
in brief, seams, units, course-level checks, cross-subject, For the lead); docs/courses/world-history-i/scope-and-sequence.md;
data/plans/world-history-i/days.csv (all 160 rows); data/plans/world-history-i/source-map.csv (the ETSU base, every
row); the 37 wh1-* rows of data/progressions/social-studies.csv and the grade 8 rows that assume grade 7 rows; the
MA.WHI lines of data/standards/ma-hss-2018.txt; docs/courses/CALENDAR.md and the grade 9 rows of data/plans/calendar.csv;
the English Language Arts grade 9 frame's units, leans and writing-load line; data/plans/civics-government-and-civic-life/days.csv
(to see which grade 7 rows grade 8 uses); docs/pipeline/briefs/sequence-write.md rule 2; the earlier sequence reads of
this date (not the Codex reads).

Gates: `plan.py check`: sequence world-history-i 0 failures, frame 0 failures. `frame.py calendar`: no stagger break;
grade 9 weeks 10, 18 to 19 and 32 match CALENDAR.md. `stale.py check`: 0 failures. Every unit's and check's first and
last day in days.csv matches data/plans/calendar.csv.

## Verdict

A sound year: ten units in time order with the overlaps of units 3 to 6 explained, every MA.WHI code and lettered option
on a teaching day and in its unit's end-of-unit assessment, writing that grows from a paragraph to a multi-page argument,
hard history named plainly with its sensitivity reads, and the ETSU base placed lesson by lesson. The biggest risk is the
readiness rule: the course treats grade 7 rows as "idle one grade" and opens them as retrieval, but under the settled rule
a grade 7 row that grade 8 did not use is two grades back and needs a readiness check, which units 1, 2, 3, 5 and 6 lack.
The one change that matters most: fold those grade 7 rows into readiness checks on each unit's first day (finding 1);
next, move the unit 10 argument's due day out of ELA 9's week 30 (finding 3).

## Findings, most serious first

### 1. Grade 7 rows that grade 8 never used open as retrieval, not readiness (moderate; firm). LAYER sequence and frame. REPEAT yes (readiness calls in the Civics, WGAC II and grade 5 reads)

**What is wrong.** The settled rule: a row used the year before (grade 8) or earlier this year opens as a retrieval task;
any other earlier-grade row the unit assumes opens the unit with a readiness check on its first day. The writer counted
grade 7 as "idle one grade" and opened every grade 7 row as retrieval. Checked against grade 8: only ss7-rome-fall is used
in grade 8 (ss8-haudenosaunee-influence assumes it; Civics day 1 opens with a readiness check on it), so day 1's retrieval
on it is right, though for the wrong stated reason. These grade 7 rows are assumed by a unit, unused in grade 8, and met
first in this course as retrieval:

| Row | First used here | Should be |
|---|---|---|
| ss7-europe-geo (wh1-geography-shapes-contact), ss7-comparing-societies (wh1-graphic-displays) | day 6 retrieval; day 5 none | readiness check, day 1 |
| ss7-hinduism-caste, ss7-shang-zhou-confucius, ss7-buddhism-east-asia | days 17, 18, 23 retrieval | inside day 16's readiness check |
| ss7-silk-road-trade | day 37 retrieval | inside day 31's readiness check |
| ss7-ideas-spread | day 64 retrieval | readiness check, day 64 |
| ss7-roman-slavery-class | day 81 retrieval | readiness check, day 75 |

Rows already used earlier this year stay retrieval and are right as written: ss7-buddhism-east-asia on day 50,
ss7-silk-road-trade on days 70 and 126, ss7-europe-geo on day 133, ss6-christianity-origins on day 102. The grade 5 and 6
readiness checks (days 16, 31, 50, 110) and every grade 8 retrieval (days 12, 13, 35, 138, 143, 145) are right.

**Why it matters.** A grade 9 student last met the Silk Roads, Hinduism or Roman slavery two years ago. Without a check,
a teacher has no read on who needs the reteach before units that lean on them.

**Fix (data/plans/world-history-i/days.csv; scope-and-sequence.md; frame.md).**
- Day 1: assess `readiness`; note: "readiness: ss7-europe-geo, ss7-comparing-societies (grade 7, not used in grade 8);
  retrieval task: ss7-rome-fall (used in grade 8 civics)". Day 6 note: "ss7-europe-geo map retrieval" becomes "uses day 1's
  readiness check".
- Day 16 note: the readiness list adds ss7-hinduism-caste, ss7-shang-zhou-confucius, ss7-buddhism-east-asia (one item
  per faith, matched to the six-faith timeline the day builds); days 17, 18 and 23 notes change "retrieval task" on those
  rows to "uses day 16's readiness check".
- Day 31 note: readiness adds ss7-silk-road-trade; day 37 note says it uses day 31's check.
- Day 64: assess `readiness`; note "readiness: ss7-ideas-spread (grade 7, not used in grade 8)".
- Day 75: assess `readiness`; note adds "readiness: ss7-roman-slavery-class, used on day 81"; day 81's retrieval note
  says it uses day 75's check.
- Scope and sequence: the readiness paragraph becomes "Readiness checks open units 1, 2, 3, 4, 5, 6 and 8: every grade 5,
  6 or 7 row the unit assumes that grade 8 did not use. ss7-rome-fall, used in grade 8, opens as retrieval on day 1." The
  unit 1, 5 and 6 "Readiness: none" lines change to match.
- Frame, "Picked up from grades 7 and 8": rows for the six grade 7 rows above read "opens with a readiness check" in
  place of "opens with retrieval".

Cross-subject leans (science s6-climate-circulation and s7-resource-distribution on day 6; math 3.MD.B.3, 6.RP.A.3c and
7.RP.A.3) stay retrieval: the rule covers rows the unit assumes in its own progression, and the frame's cross-subject
table already handles leans. That reading is mine; say so if the lead reads the rule wider.

### 2. MA.WHI.T4.3's Africa part is on no day (moderate; firm). LAYER sequence. REPEAT yes (a code taught in part, WGAC I finding 5)

**What is wrong.** MA.WHI.T4.3 asks for the Agricultural Revolution in Africa, Europe and Asia. Day 69 carries crops into
Spain, irrigation, the heavy plough, three-field rotation and Champa rice: Europe and Asia, with Africa only as the road
crops took to Spain. Day 69 is also full.

**Why it matters.** The end-of-unit assessment (day 73) names T4.3 whole; a student is assessed on a part no day taught,
and Africa drops out of the one standard that names it beside Europe and Asia.

**Fix (days.csv rows 69 and 71).** Day 69 goal: "Analyze the medieval Agricultural Revolution in Africa and Asia: crops
and irrigation spreading through Egypt and North Africa into Spain, African rice and sorghum in the inner Niger delta
feeding Mali's towns (unit 3), and Champa rice in Song China". Day 71 gains "the heavy plough and three-field rotation"
inside "how farming and settlement changed the land", which already carries D2.Geo.6 and fits Europe's case. Settled by
the expert.

### 3. The unit 10 argument is due in ELA 9's week 30 (moderate; firm). LAYER sequence. REPEAT yes (same-year writing calendar, US History II finding 1)

**What is wrong.** Day 150 hands in the multi-page argument and explanation; day 150 is week 30. Its note says "no ELA 9
process argument falls due this week". The ELA 9 frame's writing-load line says ELA process pieces are due in weeks 9, 24,
26 and 30 (the Romeo and Juliet literary argument in week 30) and that World History I's argument "falls in week 31 or
32". The scope and sequence's "clear of ELA 9's Romeo and Juliet argument" is wrong by the ELA frame.

**Why it matters.** Both frames promise no shared due week; a grade 9 student would hand in two process arguments in one
week, the load both frames set out to avoid.

**Fix (days.csv rows 150 and 153; scope-and-sequence.md unit 10 arc).** Day 150 becomes "Revise the argument where sources
disagree, and the explanation" (no hand-in). Day 153's note adds "the argument and explanation are handed in today (week
31)". The arc line "handed in day 150, week 30" becomes "handed in day 153, week 31". Settled by the expert.

### 4. The year-end check repeats unit 10's assessment three days later (minor; likely). LAYER sequence. REPEAT yes (Civics, WGAC I and II finding 1)

**What is wrong.** Day 154's end-of-unit assessment includes "an unseen source set argued briefly"; day 157, the year-end
check, is "an argument from an unseen document set with a counterclaim". Same task type, three school days apart, and
unit 10's own argument was handed in that week.

**Why it matters.** Three arguments in one week tell the teacher nothing the next one does not, and squeeze the content
items of T6 out of the unit assessment.

**Fix (days.csv row 155, day 154).** Day 154 goal: "End-of-unit assessment: England, the philosophies of government, the
Enlightenment and constitutional democracy, with an unseen source judged for where it places legitimate power". The
argument stays on day 157 only. Settled by the expert.

### 5. Units 6 and 7 ask a compelling question that half the unit does not feed (minor; judgment call). LAYER frame. REPEAT yes (WGAC II finding 4, WGAC I finding 6)

**What is wrong.** Unit 6 asks whether the meetings of faiths around the Mediterranean brought more exchange or more
violence; its slavery and plague sections (days 81 to 87, seven of the unit's thirteen teaching days) do not bear on it,
and day 87 "closes" it from plague maps. Unit 7 asks whether the Renaissance was a rebirth; its Ottoman, Mughal and
Reformation days (ten of fourteen) feed it only loosely, and day 107 answers it.

**Why it matters.** Bar item 1 wants the supporting questions to add up to the compelling question. Sections that sit
outside it read as a second unit in the same days.

**Fix.** For the lead to choose, in the frame's unit rows: unit 6 "Did the meetings of peoples around the Mediterranean
and beyond, 750 to 1400, bring more exchange or more harm?" (the slavery and plague sections then answer it), and unit 7
"Was the age of 1300 to 1600 a rebirth, or a story told about it later?" (Ottoman, Mughal and Reformation sources then
count as evidence). If the questions stay, days 82 and 86 notes name a supporting question each and say it is not part
of the compelling question's answer. A wording change, not a scope change.

### 6. Day 129 holds two lessons (minor; likely). LAYER sequence. REPEAT yes (overloaded days in most earlier reads)

**What is wrong.** Day 129 carries Islamic and Chinese astronomy before 1500 and then the scientific method, the
telescope and the microscope. Day 130 (earth-centred to sun-centred from the evidence of the time) is the natural home for
the earlier astronomy: the Maragha astronomers' corrections to Ptolemy are part of that evidence.

**Fix (days.csv rows 129, 130).** Move "Islamic and Chinese astronomy before 1500" to day 130's goal ("from the
observations available at the time, Islamic and Chinese astronomy before 1500 among them"); day 129 keeps the method and
the instruments. Settled by the expert.

### 7. The informed action gives one day to find a public telling (minor; likely). LAYER sequence. REPEAT new

**What is wrong.** Day 151 asks each student to "find one public telling of world history near you" and check it in the
same lesson. A museum label, plaque or local web page has to be found before class.

**Fix (days.csv rows 138 and 151).** Day 138 note adds: "informed action: from today, note one public telling of world
history near you (label, plaque, web page, textbook passage) to bring by day 151; the teacher keeps a printed bank of
tellings for any student who finds none". Day 151's goal becomes "bring and check". Settled by the expert.

### 8. The source map leaves order and some own days unrecorded (minor; firm). LAYER base text. REPEAT new

**What is wrong.** (a) The course uses ETSU chapter 4 (Ottomans, Mughals) and chapter 2 (Reformations) in unit 7 before
chapter 1 (Europe, Kongo, encomienda) and chapter 2's Americas and Africa in unit 8. The scope and sequence gives the
reason (unit 7's arc), but every `order_conflict` cell is blank. (b) The "ours" rows skip unit 7 to 10 days 98 to 101,
122 to 125, 138, 139 and 145 to 155. (c) Day 95 takes ETSU chapter 4's Ottoman and Safavid sections (source map) but its
note names the base only inside the candidate line.

**Fix (data/plans/world-history-i/source-map.csv; days.csv row 95).** (a) `order_conflict` on etsu-04-ottoman,
etsu-04-safavid, etsu-04-mughal and etsu-01-muslim-empires: "taught before ch. 1 and 2's Atlantic sections: the course
runs from 1300, and Ottoman control of the eastern routes is a cause of the voyages (unit 7 arc)". (b) Add "ours" rows
for 7.2 (98), 7.3 (99 100 101), 8.4 (122 123 124 125), 10.1 (138 139), 10.4 (145), 10.5 (146 to 150) and 10.6 (151 to
155). (c) Day 95 note starts "base: ETSU ch. 4 (Ottoman Empire, Safavid Empire)". Every base section is otherwise placed
or cut with a reason; the cuts (chapter summaries, Americas and Asia in 1500, chapters 6 to 15) are sound.

### 9. Stale or loose lines (minor; firm). LAYER sequence. REPEAT yes (stale notes appear in most earlier reads)

- Day 1 note: "grade 7 rows idle one grade: grade 8 civics in between" is the wrong reason (finding 1 rewrites it).
- Day 141 note: "no check state names it" becomes "no check set member names it" (the frame's words; the
  college-level framework is not a state).
- Day 153: "and answer the compelling question" sits on an informed-action day; the compelling question is answered in
  the argument days. Drop it from day 153 and add to day 150's goal: "and answer the unit's compelling question in the
  explanation's closing paragraph".
- Day 52: the standard names Zen-influenced calligraphy; the goal says "Zen-influenced art". Write "Zen-influenced
  calligraphy and art".

## The readiness versus retrieval call, and the held look-back days

The right call for this course is in finding 1: readiness checks on day 1 and on the first days of units 2, 3, 4, 5, 6
and 8; retrieval for grade 8 rows, for ss7-rome-fall (used in grade 8) and for any row already met this year. The
writer's reading ("idle one grade") matched the older wording of sequence-write rule 2; the settled rule supersedes it,
and the frame's seams table should change with the days.

No held look-back day shifts a unit. Day 160 holds late informed-action sharing inside the year-end check's respond
days; every unit and check in days.csv matches data/plans/calendar.csv. Nothing to sync.

## Checked and found right (do not undo)

- Standards in full: every MA.WHI code and lettered part is on a teaching day and in its unit's end-of-unit assessment,
  apart from T4.3's Africa part (finding 2). All twelve T3.2 options are taught: three in unit 3's map-and-explain task,
  six in unit 4, three in unit 7. All three T2.5 options are surveyed with one in depth and a full route for a student
  alone. Owned C3 indicators (D1.1, D1.4, D1.5, D2.Geo.1, 2, 4, 6, 7, 10, 12, D2.His.1 to 4, 8, 9, 11, 12, 14,
  D2.Civ.8, D3.1, D3.3, D3.4, D4.1, D4.2) each have a teaching day.
- Order inside units: each unit builds as its arc says; nothing is used before it is taught (unit 3's words for power
  before unit 4's feudal comparison; unit 6's slavery comparison before unit 8; unit 5's classical texts before the
  Renaissance; Magna Carta on day 55 before day 141).
- Writing from sources grows: paragraph with one counterclaim (days 13, 36), one-to-two page claim (day 80, week 16,
  clear of ELA's weeks 9 and 24), multi-page argument and explanation (unit 10), tested at mid-year and year-end.
- More than one account wherever an event is contested: al-Andalus (two historians), Mansa Musa (two accounts traced),
  the Crusades (four sides), the Mexica and Inca (their own records beside Spanish ones), the Reformations (both sides'
  pamphlets).
- Hard history named plainly, with no role play: the Rhineland and plague massacres, the devshirme, Luther against the
  Jews, the Banda conquest, encomienda and mita, the Middle Passage from survivors' words; Native nations and Timbuktu's
  manuscript families in the present tense. The slave trade figures (about 12.5 million embarked, about 10.7 million
  landed) match the standard published voyage estimates (from memory).
- Calendar: checks in weeks 10, 18 to 19 and 32, as CALENDAR.md sets; unit 6's claim (week 16) clear of ELA's due
  weeks; the hardest units (weeks 15 to 18, 22 to 25) clear of ELA 9's hardest texts by the ELA frame's own line.
- No unit over 25 days, so no mid-unit assessment is owed. Response time counted once per unit.
- Informed action once, in unit 10, the student's choice, through an adult, with a full route at home.
- For the lead 1 (ten new topic pages) and 3 (ETSU chapter 8 as background on day 141): accept. For the lead 2: the
  corrections it lists are in the days and right.

## Lens checklist, scope and sequence layer

| Line | Met? |
|---|---|
| Unit question answerable without the unit's sources, or one defensible answer | Met: all ten are open; units 6 and 7 reach past their questions (finding 5) |
| History out of time order with no reason | Met: the overlaps of units 3 to 6 and the Ottomans before Iberia each carry a reason |
| A contested event with one telling | Met (see above) |
| Writing from sources once a year or never builds short to long | Met: four steps, paragraph to multi-page |

## Candidate cells

| Cell | Settled in the draft | My read |
|---|---|---|
| Srivijaya; the Indian Ocean as one system (unit 1) | Kept, day 9 | Right |
| Polynesian voyaging (unit 1) | Dropped, no member, no day | Right |
| Tang to Korea and Japan; 1054 split (unit 2) | Kept, days 23, 24 | Right |
| Great Zimbabwe (unit 3) | Kept, a third of day 34 | Right |
| Hausa city-states; Delhi Sultanate (unit 3) | Dropped with reasons | Right |
| Kievan Rus and the Mongol yoke (unit 4) | Kept, day 53 | Right |
| Mississippian cities (unit 4) | Dropped | Right; Goryeo is a frame note, not a candidate |
| al-Khwarizmi and Ibn Sina; Champa rice (unit 5) | Kept, days 64, 69 | Right |
| Reconquista (unit 6) | Kept, day 75 | Right |
| Hundred Years' War (unit 6) | Dropped | Right |
| Safavids; Sikhism (unit 7) | Kept, days 95, 96 | Right |
| Ming before 1600 (unit 7) | Dropped, in units 3 and 9 | Right |
| Pueblo Revolt; Afonso I; Potosi and the galleons (unit 8) | Kept, days 115, 118, 116 | Right |
| Tokugawa and Qing trade limits (unit 9) | Kept, day 133 | Right |
| Women in the Enlightenment (unit 10) | Kept, day 144 | Right |
| Pugachev's revolt (unit 10) | Dropped | Right |

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Readiness checks on days 1, 16, 31, 64 and 75 carry the grade 7 rows grade 8 did not use; later days say they use them | The settled readiness rule | data/plans/world-history-i/days.csv rows 1, 6, 16, 17, 18, 23, 31, 37, 64, 75, 81; scope-and-sequence.md readiness lines |
| Africa added to day 69; heavy plough and three-field rotation moved to day 71 | MA.WHI.T4.3 names Africa; day 69 was full | days.csv rows 69, 71 |
| Argument and explanation handed in on day 153 (week 31); day 150 revises | ELA 9's literary argument is due in week 30 | days.csv rows 150, 153; scope-and-sequence.md unit 10 arc |
| Day 154 judges an unseen source for where it places power; no argument | The year-end check argues three days later | days.csv row 154 |
| Islamic and Chinese astronomy moved from day 129 to day 130 | Day 129 held two lessons | days.csv rows 129, 130 |
| Informed action's public telling announced on day 138, brought by day 151, with a printed bank | One day cannot find and check | days.csv rows 138, 151 |
| Source map order notes, "ours" rows filled, day 95 base named | Base order kept unless a reason is given | data/plans/world-history-i/source-map.csv; days.csv row 95 |
| Wording on days 1, 52, 141, 150, 153 | Stale or loose lines | days.csv |

## For Cory

None. (Finding 5's question wording is the lead's: it does not change what the course teaches.)

## Sources

- data/standards/ma-hss-2018.txt (Massachusetts 2018, ids and our words): every WHI code checked against the days.
- data/standards/c3-indicators.txt: owned indicator ids from the frame and progression rows.
- ETSU, World History Since 1500 (Rankin and Weise, CC BY 4.0), through data/plans/world-history-i/source-map.csv; the
  book itself was not re-opened.
- Slave voyage estimates (embarked and disembarked totals): from memory of the published Trans-Atlantic Slave Trade
  Database estimates; not re-fetched.
- `plan.py check`, `frame.py calendar`, `stale.py check` output of 2026-11-14.

Confidence: findings 1, 2, 3, 8 and 9 firm; 4, 6 and 7 likely; 5 a judgment call.

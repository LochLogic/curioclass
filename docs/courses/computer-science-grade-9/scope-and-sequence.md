# Scope and sequence: Computer Science, Grade 9

Course `computer-science-grade-9`, grade 9, draft, 2026-11-26.

The frame's six units keep their order, owned rows and day counts (13, 12, 7, 8, 11 and 7), with four course-level
check days and two respond days: 64 course days of about 45 minutes, two a week for 32 weeks. The CSV
(data/plans/computer-science-grade-9/days.csv) is the day map; this page gives the reasons. Sections (`unit` column)
group at most seven days for the unit plans.

## Calendar and school days

Course day n sits in week w = ceil(n / 2), on the second and fourth school day of that week: `school_day` = 5(w - 1) + 2
for an odd day and 5(w - 1) + 4 for an even day, so week = (school_day - 1) // 5 + 1 gives back the frame's weeks. Every
check falls in the frame's weeks: unit 1's end-of-unit assessment day 12 (week 6), unit 2's day 24 (week 12), the
mid-year check days 33 and 34 (week 17) with its respond day 35 (week 18), unit 4's day 42 (week 21), unit 5's day 53
(week 27), and the year-end check days 62 (week 31) and 63 (week 32, the finals week) with its respond day 64 (week 32).
Grades 9 to 12 have no stagger rule but the finals week (CALENDAR.md rule 4); these weeks also miss every grade 9 core
check week (ELA 13, 20, 32; Algebra I 12 to 13, 22, 32; Biology 9, 16, 32; World History I 10, 18 to 19, 32) except week
32, which every course shares, and day 35, a respond day in World History I's week 18. Week 17 is shared with ELD's
grade 9 mid-year check (frame For the lead 1, the lead's calendar pass).

## Earlier-grade rows and their treatment

Computer science 6 to 12 is an elective, so a year-before row opens as a retrieval task for a student who took grade 8
and is in a ten-minute readiness check, with a short worked example on the unit's first understanding day, for one who
did not (frame Course order; frame-computer-science-grades-1-to-12-fixes For the lead 4). Every student sits the
readiness items: for a student who took grade 8 they are the year-before retrieval, and the teacher reads them to find
who needs the worked example on the unit's first understanding day (a teacher cannot always tell who took grade 8).
Count by grade number.

| Earlier row | Last used | First needed | Retrieval (took grade 8) | Readiness (did not) |
|---|---|---|---|---|
| g8-text-project | grade 8 | unit 1, day 1; unit 2, day 15 | days 1 to 5, 8, 15 | day 1 (unit 1); day 13 (unit 2) |
| g8-ml-evaluate | grade 8 | unit 3, days 26 and 29 | days 26, 29 | day 25 |
| g8-modify-for-bias | grade 8 | unit 3, day 31 | day 31 | day 25 |
| g8-relationships | grade 8 | unit 4, day 38 | day 38 | day 35 |
| g8-investigation-summary | grade 8 | unit 4, day 36 | day 36 | day 35 |
| g8-biased-decisions | grade 8 | unit 4, day 41 | day 41 | day 35 |
| g8-choose-a-system | grade 8 | unit 5, days 44 and 47 | days 44, 47 | day 43 |
| g8-network-failure | grade 8 | unit 5, day 49 | day 49 | day 43 |
| g8-cyber-attacks | grade 8 | unit 5, day 50 | day 50 | day 43 |
| g8-history-case | grade 8 | unit 6, day 55 | day 55 | day 54 |
| g8-emerging-design; g8-emerging-debate | grade 8 | unit 6, day 59 | day 59 | day 54 |
| g8-career-sketch | grade 8 | unit 6, day 61 | day 61 | day 54 |
| math:m7-chance-probability | grade 7 (two back) | unit 3, day 26; unit 4, days 38 to 40 | none | day 25, every student |

Same-year rows return as the three-minute retrieval trace that opens every day from day 2 (APPROACH.md), named in the
`retrieves` column: unit 1's lists in units 2, 3 and 5; unit 2's procedures and random library in units 3 and 4; unit
3's random choice in unit 4; unit 4's generator and dictionary in unit 5; unit 5's device limits and encryption in
unit 6. Each readiness check sits in the last ten minutes of the day before its unit (unit 1: day 1 after the hook),
never on a unit's first day.

## Unit 1. Lists and records

Course days 1 to 13, weeks 1 to 7. Sections 1.1 (days 1 to 6, structures) and 1.2 (days 7 to 13, design). Concept
areas: programming, algorithms and design. Practices: CT7, CT8, CT9 (day 6's planted bug, day 11's tests), IC5
(driver and navigator on every device day), IC3 (day 10 feedback).

The arc runs read, then modify, then make on the structures: a list traced (day 1), its operations from worked examples
then changed (day 2), a key-value record (days 3 and 4), a list of records (day 5), and a store, find and change
program made against stated tests (day 6, HS-PRO-VD-16 in full), after one planted bug found with predict, run,
compare, first wrong line (about 6 minutes, grade 8's debugging method retrieved and taught in full for a student new
to it). The design half follows because HS-PRO-VD-16 comes
before HS-ALG-PS-01: one problem solved two ways shows that structure changes the algorithm (day 7), a leaderboard is
designed (day 8) and changed for a new need (day 9, modify), then each pair designs for a new problem with feedback
(day 10) and builds, tests and revises it (day 11, HS-ALG-PS-01 in full; the design rubric also carries
HS-PRO-VD-16's look-fors: data stored, accessed and changed in the chosen structure). Days 2, 4, 6 and 11 are device days; days 3,
5, 7 and 8 are unplugged. The unit's load is the heaviest (two device rows, a scored design with its draft, feedback
and revision days), so it has 11 teaching days.

Assessment. Readiness: last ten minutes of day 1. End-of-unit day 12: a paper sitting with unseen items (a trace with a
prompt each for store, access and change, 8 minutes, then a 4-minute write item that adds three lines storing a new
record and changing one value; a structure chosen and justified for two problems with pseudocode for one; a debug
task, the method taught on day 6), plus the revised day 10 and 11 design scored by rubric. Response: day 13, whose last ten minutes hold
unit 2's readiness check. Candidate: the Parsons problem (day 5's program, shuffled) as day 6's opener is kept, 0 days,
five minutes in place of the retrieval trace.

**The bridge for a student with no text programming (frame For the lead 6).** Budgeted inside the days: day 1 six
minutes (a worked program with a variable read "x becomes x plus 1", a loop and a procedure call, line by line); day 2
about twelve (each of four list operations from a worked example traced, about three minutes each, before any change);
day 3 five (a counted loop that adds to a total); day 4 about twelve (four record operations, as day 2); day 5 five (a
procedure called with a parameter). About 40 minutes in all, taken by the whole class, plus the readiness check that
tells the teacher who needs them and the worked examples on days 14, 26, 36, 44 and 55. Judgment: enough for a student
who did some programming before (grade 7, blocks in grade 6, or a club), since it names and traces the constructs they
half know. Not enough for a student who has never programmed: 40 minutes cannot build the notional machine (variables,
assignment, loops, selection, procedures) that grades 6 to 8 build over three years, and that student would meet
day 6's make task too early. Lead call (2026-11-26, after Cory's Desk q-frames-scope-1 answer that the scope budgets and reports): the entry provision is, four worked-program
sheets from grade 8 unit 2's text project (each with a planted-bug step), taken beside days 1 to 6, rather than a
stated prerequisite, which would shut out students the elective should welcome.

## Unit 2. Cleaner programs

Course days 14 to 25, weeks 7 to 13. Sections 2.1 (days 14 to 18, procedures and loops) and 2.2 (days 19 to 25,
modules). Concept areas: algorithms and design, programming. Practices: CT6 (day 15), CT7, CT8, CT9 (days 16, 18 and 21's planted bug),
IC4 (milestones set day 19, met days 22 and 23), IC3 (day 23).

The 60-line report-card anchor is read and predicted twenty lines at a time (day 14), a procedure with parameters is
traced (day 15) and then used to replace repeated steps (day 16, modify), loops and selection streamline a flowchart
(day 17) and the anchor is rewritten with the same tests (day 18, HS-ALG-PS-02 in full). Modules follow because
g9-modular comes after both unit 1 rows and builds on procedures: decomposition on cards (day 19), a library function
and a small class traced (day 20), a given program split, with one planted bug in a module call found the day 6 way
(day 21, modify, a Fluency day), then the pair's own modular program drafted (day 22) and revised after feedback (day
23, HS-PRO-PD-12 in full). The product asks for at least two procedures and one library function, and one object where
it fits the program: the standard asks for procedures, libraries or objects, and the class is the course's
thinnest-taught construct, so the rubric scores reuse and readability, not the count of kinds. Days 16, 18, 21, 22 and 23 are device days; days 15, 17 and
19 unplugged. HS-PRO-PD-12 is device-only: on the paper path the split is done on paper with the solution key and
recorded "part met without a device".

Assessment. End-of-unit day 24: unseen items (find redundancy and rewrite with a procedure and a loop, a prompt for
each; trace a modular call) plus the revised modular program scored by rubric. Response: day 25, whose last ten minutes
hold unit 3's readiness check (chance for every student, the grade 8 rows for a student who did not take grade 8).
Candidate: a code-review checklist for day 23's partner feedback is kept, 0 days.

## Unit 3. Algorithms that decide

Course days 26 to 32, weeks 13 to 16. Sections 3.1 (days 26 to 28, deterministic and probabilistic) and 3.2 (days 29
to 32, AI types and an audit). Concept area: algorithms and design, with machine learning and impacts. Practices: CT6,
CT7 (day 28), ESR1 (day 31), IC3 (days 28 and 32).

Dice and rule algorithms are run on the same input (day 26), then two searches over unit 1's list using unit 2's
random library (day 27; the random pick never repeats a slot), which shows that matching outputs do not prove an
algorithm deterministic; uses of each close HS-ALG-PS-04 (day 28), with why a random pick finds a target sooner on some
runs and later on others, and can beat a front-to-back search when targets tend to sit near the end (the key says
"no faster on average" holds only when every position is equally likely). The AI tour (days 29 and 30) and the audit (days 31 and 32) begin ids owned in grades 10 and 11
and are never scored here. The lean on math grade 7's chance words is covered by day 25's readiness check; no
probability is computed. Days 26, 29 and 31 are unplugged; day 27 is a device day. Sensitivity flags (days 31 and 32)
are in the notes: invented cases, a distance rule that can stand in for income, talk kept on the rule.

Assessment. The mid-year check (days 33 and 34) stands for this unit's end-of-unit assessment (frame); its respond day
35 is the unit's. Day 33 sits on the day right after the unit's last day, so it stands for the unit's end-of-unit
assessment; day 32 is a teaching day with no `assess` mark, and its audit claim is collected for grade 11, unscored.
Candidate: the
class tally of 30 random-pick runs as a dot plot is kept inside day 27, 0 days, about five minutes.

## Unit 4. Data you can trust

Course days 36 to 43, weeks 18 to 22. Sections 4.1 (days 36 and 37, the dictionary), 4.2 (days 38 to 40, simulated
data) and 4.3 (days 41 to 43). Concept area: data and analysis, with impacts. Practices: CT7 (day 37), CT8 (day 40),
HCD12 (day 37), ESR2 (day 41).

The dictionary comes first (fields, types, allowed values and rules between fields on day 36; a pair's dictionary
tested with a bad row on day 37, HS-DAT-DC-22 in full) so the generated data has stated values to fit. The generator
uses unit 3's random choice: traced with a seed (day 38), changed and checked against a dictionary (day 39, modify),
then fed to a supplied queue simulation with one parameter changed and charted (day 40, HS-DAT-DC-21 in full). The
society day closes the unit on the kind of data just defined (day 41, begins HS-DAT-IM-27, grade 11's). Days 36, 37 and
41 are unplugged; 38 to 40 are device days. HS-DAT-DC-21 is device-only: dice and cards on the paper path, recorded
"part met without a device". Transit case sensitivity is in day 41's note.

Assessment. End-of-unit day 42: unseen items (a dictionary with a rule and bad rows, a prompt per part; a generator
changed and its result read). Response: day 43, whose last ten minutes hold unit 5's readiness check. Candidate: the
bad-row game as the three-minute opener of days 38 to 40 is kept, 0 days.

## Unit 5. What the system does for us

Course days 44 to 54, weeks 22 to 27. Sections 5.1 (days 44 to 46, operating systems), 5.2 (days 47 and 48, device
limits) and 5.3 (days 49 to 54, networks and security). Concept area: computing systems and security, with networks.
Practices: IC3 and CT7 (day 45), CT6 (day 47), HCD12 and ESR2 (day 51).

The operating system is acted out on cards (day 44), set apart from applications and utilities and added as a layer
(day 45, HS-SYS-HW-29 in full), then watched on a toy page (day 46). Device limits follow because they rest on the
system-diagram: a task's needs, then a simulated counter pushed until it fails (day 47), then a device chosen with
evidence (day 48, HS-SYS-HW-30 in full). The network read (day 49, begins HS-SYS-NT-34) sits before security so the
measures have a system to protect: measures on the cia-triangle (day 50), trade-offs on a toy system (day 51), a club
security plan (day 52, HS-SYS-SE-31 in full). Days 44, 45, 49 and 50 are unplugged; 46, 47, 48 and 51 are device days.
HS-SYS-HW-30 is device-only (a paper simulator on the paper path, "part met without a device"). Security days carry
the toy-systems rule and health's disclosure steps; day 47 carries the optional board's safety line.

Assessment. End-of-unit day 53: short unseen items with a prompt per part (operating system: memory, peripherals and a
task that has to wait, the software it manages; device limits; one cyber and one physical measure named for the case,
then the trade-offs for users, data and devices; a network trace unscored for grade 10). The
full performances were days 48 and 52, so the end day holds only short items. Response: day 54, whose last ten minutes
hold unit 6's readiness check. Candidate: the security trade-off card game as day 51's opener is kept, 0 days; its
cards carry unit 4's transit case, so it is the day's retrieval. Days 46, 47, 48 and 51 run a page, not the editor, so
their set-up minutes open the page.

## Unit 6. Computing over time

Course days 55 to 61, weeks 28 to 31. Sections 6.1 (days 55 to 58, history) and 6.2 (days 59 to 61, emerging technology
and careers). Concept area: computing and society. Practices: ESR1 and IC3 (day 57), CT6 (day 59), HCD10 (day 61).
All unplugged, one screen for the timeline.

Satellite positioning's trajectory is laid out (day 55) and its social, policy, economic and environmental factors
backed from two supplied sources (day 56); a short analysis is drafted (day 57) and revised after feedback (day 58,
HS-SOC-HI-38 in full; it opens with the commonest wrong point from day 57's drafts, two minutes). The environmental
factor is a nontechnical force, as the standard's boundary asks: the natural-environment uses that drove civilian
adoption (tracking earthquakes and ground movement, precision farming that cuts fuel and fertilizer, wildlife and
weather tracking; gps.gov applications pages). The upper atmosphere bending the signal stays a technical fact. Quantum
against classical computing (day 59: a qubit's state combines 0 and 1 until it is measured, and a measurement gives 0
or 1; it does not try every answer at once) leads to the encryption case, tied to unit 5's
measures (day 60, HS-SOC-ET-40 in full, with a quarter of the day beginning HS-SOC-HU-43). The private career note
(day 61, begins HS-SOC-CE-46) may be left out with no id lost. The 1983 airliner (day 56) is a dated fact with no images
or role play.

Assessment. Day 58's revised analysis is the unit's scored product, scored by rubric before the year-end check and
reported with it; day 58 carries no `assess` mark. Day 62 sits on the day right after the unit's last day, so the
year-end check (days 62 and 63) stands for the unit's end-of-unit assessment, and day 64 is the unit's respond day.
Candidate: a second technology's trajectory as the check's unseen case is kept, 0 days (day 62), changed by the expert
read from library catalogs, which have no clear environmental driver, to numerical weather forecasting by computer,
from the first computer forecasts of the 1950s to today's national forecast models: storms and the need for warnings
drove the computers built, and the public's need for warnings is the societal point. Its sources (noaa.gov) are
checked and dated by the unit writer.

## Course-level checks

| Check | Days and weeks | Lesson one | Lesson two | Respond |
|---|---|---|---|---|
| Mid-year | 33 and 34, week 17 | Scores unit 3 in full with new algorithms (HS-ALG-PS-04, about 25 minutes; begun ML-06 and IM-10 recorded unscored, about 5) | Short new items on units 1 and 2: HS-PRO-VD-16 (10, a trace ending with one written line that changes a value), HS-ALG-PS-01 (8), HS-ALG-PS-02 (12) | Day 35, week 18, plus unit 4's readiness check |
| Year-end | 62 (week 31) and 63 (week 32) | Scores unit 6 in full on the unseen case of numerical weather forecasting by computer: HS-SOC-HI-38 (12), HS-SOC-ET-40 (12) | Short new items on units 2, 4 and 5: HS-PRO-PD-12 (8, a debug item), HS-DAT-DC-22 (7, a field and a rule between fields), HS-SYS-HW-29 (7, a piece of software sorted and one thing the operating system manages), HS-SYS-SE-31 (8, one cyber and one physical measure, then the trade-offs for users, data and devices) | Day 64, week 32 |

Each check's first lesson stands for the end-of-unit assessment of the unit it follows (the frame's shape), so it
scores that unit with unseen items; each second lesson draws its items from earlier units only and repeats no item of
the units' own end days. Ten of the twelve owned codes are sampled on a check day. Not sampled: HS-DAT-DC-21 and
HS-SYS-HW-30, the device-only ids, which are assessed on the device in their units' end days (42 and 53) and carried
unscored, because a paper check item would only reach "part met without a device" and a device item would add a third
check lesson (frame). HS-PRO-PD-12, the third device-only id, is sampled on day 63 by a debug item with a device
version, as day 34's trace item has; on paper it is recorded "part met without a device". The year-end first lesson is a short timed response on a new case, not the drafted analysis form
of days 57 and 58, so no task form repeats within two weeks.

## Devices, tools and paper paths

Device days: 2, 4, 6, 11, 16, 18, 21, 22, 23, 27, 38, 39, 40, 46, 47, 48, 51 (17 of 50 teaching days); every unit has
unplugged days. Each device day's note carries the four ways, the pair roles, the set-up and save minutes and the
safety line. The tools are all tool asks for TOOL-ASKS.md: our own editor's grade 9 Python view (text view, step-through
trace, stated tests, built-in random and math libraries, one small class), a toy operating system page, a simulated
device page, a toy security page and a queue simulation page. Until each exists its days run on the paper path, which
meets every owned id in full except the three device-only ones (HS-PRO-PD-12, HS-DAT-DC-21, HS-SYS-HW-30), recorded
"part met without a device". None of the three editor modes queued at later.csv L148 is used in grade 9.

**Sources not yet loaded (L149).** No grade 9 day leans on an unloaded source: the archived Teach Computing Curriculum
covers K to 8 only and the NOAA extract is grade 11's. The society days' sources (gps.gov history and applications
pages, NIST post-quantum and quantum pages, a transit agency's privacy policy, noaa.gov's history of numerical weather
prediction, NIST SP 1270 for the sensitivity read) are opened and dated by the unit writers.

**Days outside the standards (C1).** None of the 50 teaching days, on the full year and on the shorter path. About 7
teaching days begin ids a later grade owns (days 29, 30, 31, 32, 41, 49, 61 and a quarter of 60); they count inside the
standard, since a begun id is standard content (lead call, 2026-11-26). Grade 9 claims no Specialty id.

## Shorter path

**A shorter period (40 minutes).** Every day holds. Day 1 drops its 3-minute retrieval trace (the readiness check tests
the same grade 8 row) and takes the hook to 4: 4 + 6 + 17 + 3 + 10 = 40. Device days keep their 3 set-up and 4 save
minutes and teach about 28 minutes: on days 2 and 4 the fourth operation's worked example and change move into the next
day's opener in place of the retrieval trace; on other device days the last worked example does. Unplugged days cut
the exit ticket to one question. Check days hold, since each sitting is about 30 to 40 minutes; the 40-minute day
12 and day 53 sittings drop to 35 by printing directions on the paper.

**A year about 10 days short (54 course days).** Ten fold-in days, each a 45-minute session saved; nothing assessed is
on them and no owned part is cut, since each day's core moves into a neighbor's minutes:

| Fold-in day | Folds into | What the host day gives up | Minutes saved |
|---|---|---|---|
| 7 (one problem two ways) | day 8's first 12 minutes | the card sort is one class demonstration, not in pairs | 45 |
| 9 (leaderboard modified) | day 10's opener, 8 minutes | its retrieval trace; the partner feedback holds two look-fors, not three | 45 |
| 14 (anchor traced in parts) | day 15's first 12 minutes | its retrieval; one call traced in place of two | 45 |
| 16 (repeated steps to a procedure) | day 18's first step | the second test-table run is done as the exit ticket | 45 |
| 30 (new AI task cards) | day 29's exit ticket | the third task card is matched as a class, not in pairs | 45 |
| 32 (audit written as a claim; begun HS-ALG-IM-10, never scored) | day 31's last 10 minutes, as its exit ticket | one case card set is audited together as a class | 45 |
| 39 (generator changed) | day 40's first step | count and range changed once on one screen; the chart uses one run per pair | 45 |
| 46 (toy operating system page) | day 45, an 8-minute one-screen demonstration | the software sort uses one set of eight cards | 45 |
| 51 (trade-offs on a toy system) | day 52, whose plan charts the trade-offs first | the partner's review is one written comment | 45 |
| 61 (private career note) | day 64's last 10 minutes, still private | the reteach covers the two most missed items | 45 |

Day 21 (the given program split) is not a fold-in: it is HS-PRO-PD-12's only modify day, and a make day never comes
before a modify day on the same construct (APPROACH.md). The begun-id days fall by one on this path, and no day is
outside the standards (C1 holds).

Total: 450 minutes, ten of the frame's 64 days, leaving 54; every check, end, respond and readiness day stays.

## For the lead

1. **Grade 9 entry with no programming at all.** Settled by the lead 2026-11-26 (the four worked-program sheets, unit 1's bridge
   paragraph); Cory may overrule.
2. **Tool asks for TOOL-ASKS.md:** the editor's grade 9 Python view with one small class, the toy operating system,
   simulated device, toy security and queue simulation pages (frame For the lead 3).
3. **Week 17 and week 18** (frame For the lead 1): unchanged; the mid-year check shares week 17 with ELD and its
   respond day sits in World History I's week 18. No break of a grade 9 to 12 rule.

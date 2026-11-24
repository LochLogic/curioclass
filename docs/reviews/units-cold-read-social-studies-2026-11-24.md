# Cold read, social studies unit plans, 2026-11-24

Stage 4 gate (docs/COURSE-RUN.md): one cold read from the progression down. The reader wrote and fixed none of it.
Scope: data/progressions/social-studies.csv (418 rows) and the 15 core courses in grade order (kindergarten to grade 5,
World Geography and Ancient Civilizations I and II, Civics, World History I and II, US History I and II, US Government
and Politics, Economics); 138 unit plans. Psychology (elective, no unit plans yet) is outside the gate. The progression
and every frame's Units table were read whole; every plan's owned, Builds on, Leads to, field 4 and Goal map lines were
read by script (helpers in _scratch/l87/tmp/ss-cold-read/) and the weak spots read in full.

## Verdict

Not ready for owner approval yet, but close: the chain holds. Every non-psychology progression row is owned by a unit
at its grade, every assumed row sits at an earlier grade, every hand-on is answered, chronology runs in order
from grade 6's deep time through grade 12, and `unitplan.py check social-studies` passes all 15 core
courses. One short fix pass should close it: the generated "owned" lines that list reused rows as owned (26 plans),
grade 2's exits asking less than grade 1's, and seven assumed rows nobody retrieves.

## Findings, most serious first

No serious findings. 3 moderate, 4 minor. None is fixed by a 2026-11-24 ledger: there is no units-read or
units-structure-pass ledger for social studies dated 2026-11-24 (only math, science and English language arts ones,
and structure-pass-core-electives, which covers other courses). All are open.

### 1. Reused rows are labeled "owned" in 26 unit plans (moderate, open)

- **Where:** the generated `Progression skills owned` line (and the Builds on and Leads to lines built from it) in
  kindergarten units 2, 4, 5, 6; grade 1 units 3 to 8; grade 2 units 2 to 7; grade 3 units 1 to 7; grade 5 unit 5;
  World History I units 3 and 9.
- **What:** the skeleton takes "owned" from every row in the unit's days.csv skills column. A row taught in an earlier
  unit of the same course and reused later is then listed as owned again. Examples: grade 5 unit 5 lists
  ss5-revolution-causes (unit 3's row, used only on day 72's timeline review); grade 3 lists ss3-biography as owned in
  six units and ss3-claim-evidence in seven; grade 2 lists ss2-source-maker and ss2-claim-sources in five or six;
  World History I unit 9 lists wh1-sources-of-the-past (unit 1's). The frames own each of these once. The Builds on
  line then carries the reused row's assumes, so grade 3 units 2 to 7 each list ss1-leaders, and grade 2 units 5 to 6
  list ss1 rows, as rows the unit assumes and must retrieve, which it does not.
- **Cost:** a section writer reading "owned" may teach the row as new a second time, and the readiness duty reads as
  unmet when it is not. The plans' own days are right (the days.csv goals are reviews); only the label is wrong.
- **Change:** in scripts/unit_skeleton.py (around lines 1540 to 1550, where the earlier-row split is skipped for social
  studies with `if not ss`), list a row owned by an earlier unit of the same course on a separate "Earlier rows used
  again (review, not owned)" line, and build Builds on and Leads to from the frame's owned rows only. Regenerate the
  skel blocks of the 26 plans. Sweep: the same split for science and English language arts plans.

### 2. Grade 2 exits ask less than grade 1's (moderate, open)

- **Where:** grade 2 Goal maps, units 1 to 4 above all (30 `recognise` exits of 77, against 9 of 75 in grade 1 and 5
  of 135 in grade 3). Unit 1's days 1 to 11 are all circle or token exits.
- **What:** grade 1's map days already ask "circle the capital and say why it is the capital" (grade 1 s05, days 44 to
  53). Grade 2's map days ask only "circle the part of a new map that tells what the diamond means" (day 2), "circle
  the date printed on a fresh credit card" (day 6). Where the goal verb is choose, read, distinguish or source, the
  exit drops the reason grade 1 already asked for. Difficulty falls between grades 1 and 2, then jumps at grade 3.
- **Change:** in grade 2 units 1 to 4, add the spoken reason to every circle exit whose goal is choose, read, source or
  distinguish ("circle it, then say why"), keeping `recognise` only where the goal is identify or locate a named
  place. Day-level wording is the writer's; the Goal map row changes with it.

### 3. Grade 5 unit 1 never checks ss4-native-nations-sites (moderate, open)

- **Where:** social-studies-grade-5/s01.md, field 4.
- **What:** the unit's question ("Whose land was it, and who decided?") rests on ss5-colonial-encounters, which
  assumes ss4-native-nations-sites. Field 4 retrieves ss4-first-peoples-evidence, exploration, map scale, regions and
  state maps, but the Native nations' own sites and homelands appear only in the Builds on line.
- **Cost:** the unit's Native content opens without knowing which nations the class can already place and name.
- **Change:** add the row to the day 1 retrieval: locate two Native nations of the eastern woodlands on a map and say
  one thing each nation's own sources say about its homeland, with a ten-minute repair inside day 2.

### 4. Six more assumed rows with no retrieval (minor, open)

Named only in the Builds on line, nowhere else in the plan:
- grade 1 unit 3: ssk-i-think-because (the base of ss1-claim-reasons, first taught here);
- grade 3 unit 5: ss2-nation-of-immigrants (assumed by ss3-early-colonies);
- grade 4 unit 2: ss3-biography (assumed by ss4-canada-mexico-research);
- grade 4 unit 6: ss3-home-region (assumed by ss4-states-and-statehood and ss4-regions-resources); ss3-state-constitution
  is met only inside the day 126 prompt on levels of government, which is acceptable;
- grade 5 unit 5: ss4-states-and-statehood (assumed by ss5-constitution).

Change: one retrieval task each, in the unit's field 4 and the day's days.csv note, after the hook.

### 5. World Geography and Ancient Civilizations I, field 4 labels (minor, open)

- s01: "Start-of-year check: none needed; retrieval only" while ss5-civil-rights-research and ss5-revolution-causes
  are assumed and never retrieved (day 1's note only says grade 5's sourcing questions are used unprompted). Add a short
  day 1 or 2 retrieval of the grade 5 research and causation moves, or say in field 4 why none is needed.
- s08: field 4 opens "Given: none", which passes the gate but contradicts its form; the unit uses an in-day check on
  day 105, so the line should be "Retrieval only:".

### 6. US History II leans on other courses' checks with no fallback (minor, open)

- u07 relies on Government's unit 2 check of ss8-civil-rights-laws; u10 relies on Economics' unit 1 check of
  wh2-soviet-collapse. Both rows were last used two grades back by US History II's own sequence. A student taking
  Economics in grade 11 or Government in another term is unchecked. Change: keep the retrieval task, and add one line
  per unit saying what the teacher gives a student who did not sit the other course's check (the same task, scored as
  readiness).

### 7. High school goal verbs barely climb (minor, judgment call, open)

"Explain" is the commonest goal verb in every course from grade 1 to grade 12 (for example 78 of 124 days in grade 7,
58 of 130 in US History II); argue, evaluate and defend appear only a handful of times in grades 9 to 12. The exits'
content does rise (counterclaims, limits, source chains), so this is a reading of the Goal map, not of the days.
Change for the section writers: where a high school day's exit asks for a weighed judgment, name the verb (evaluate,
argue) in the Goal map row so the climb is visible.

## Checked and sound

- Ownership: every one of the 384 non-psychology rows is owned by a frame unit at its grade, once in the frame.
- Assumes: no row assumes a later or same-grade later row; every hands_on is answered by the receiving row's assumes.
- Grade-skip revisits (grade 10 to US History II, grade 8 to grade 11 and 12) are labeled in the progression as
  "content revisited" and each has a readiness check or a same-year retrieval.
- US History II unit 1's economics toolkit and Economics overlap on purpose (Desk q-ss-progression-1, recorded in the
  Economics frame); not a finding.
- Goal maps: every teaching day has a row; no practice shape copies its exit.
- Story: K to 5 follows Massachusetts order to civil rights; grades 6 and 7 run deep time to Rome's change; grade 8
  civics; grades 9 and 10 run 500 to today; US History I 1754 to 1920 and US History II 1920s to today.

## For the fix pass

1. Finding 1: skeleton change, regenerate the 26 skel blocks, sweep science and English language arts.
2. Finding 2: grade 2 units 1 to 4 exits and Goal map rows.
3. Findings 3 and 4: seven retrieval tasks (field 4 and days.csv notes).
4. Finding 5: two field 4 fixes in World Geography and Ancient Civilizations I.
5. Finding 6: a fallback line in US History II units 7 and 10.
6. Finding 7: pass to the section brief, no unit plan edit needed.

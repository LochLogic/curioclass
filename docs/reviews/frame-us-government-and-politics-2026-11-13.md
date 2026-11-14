# Frame read: us-government-and-politics (US Government and Politics, half year), 2026-11-13

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/social-studies.md, section 1 of docs/ADOPTION-BAR-SUBJECTS.md,
  docs/courses/social-studies/STANDARD.md, docs/sources/BASE-TEXTS.md (social studies part).
- The frame docs/courses/us-government-and-politics/frame.md and its row in data/plans/frames.csv (9 units, 80 days).
- The 19 gov-* rows of data/progressions/social-studies.csv; every ss8-*, wh1-* and wh2-* row whose hands_on names a
  gov-* row; ss8-news-literacy and us1-news-reading (the news-literacy seam); the us1-* rows the gov-* notes still name.
- The frames before: docs/courses/civics-government-and-civic-life/frame.md (grade 8, its hand-on table and "For the
  lead" item 1) and docs/courses/world-geography-and-ancient-civilizations-ii/frame.md (grade 7). World History II
  has no frame yet (frame:world-history-ii is "Writing"), so its rows were read. The US History II frame, for the
  shared timetable.
- data/standards/ma-hss-2018.txt: MA.GOV.T1 to T5 and MA.NML.T1 to T5 with lettered parts, read against the rows.
- Desk card q-ss-progression-1 (DESK-ANSWERS 2026-11-13): Government open to grade 11 or 12, no US History I skill
  assumed.
- Earlier reads: docs/reviews/progression-social-studies-*2026-11-13.md, progression-cross-*2026-11-13.md,
  frame-social-studies-kindergarten-2026-11-13.md, and my own US History II read of today.
- Gates: `python -X utf8 scripts/plan.py check` (frame us-government-and-politics: 0 failures; 9 units, 80 days, 76
  in units, 4 for checks) and `python -X utf8 scripts/stale.py check` (0 failures).

## Verdict

The frame is sound in shape: all 19 gov-* rows are placed once, every MA.GOV code and the nine NML codes placed here
are taught in full, the order (ideas, levels, branches, rights, groups, the world, policy, local action) is reasoned,
and the own-state method is carried right through. The biggest risk is the promise of q-ss-progression-1: one unit
still practises an indicator only US History II owns, and the news-literacy bridge is drawn from the wrong grade 8
row, so a grade 11 student meets two skills nobody taught them. The one change that matters most is rewiring
gov-policy-news to ss8-news-literacy and reteaching D2.Civ.12 in unit 5; after that, the days of units 1, 3 and 7 and
the size of the check-set additions need a budget.

## Findings, most serious first

### 1. Unit 5 practises D2.Civ.12, which only US History II owns (moderate; firm)

**What is wrong.** Unit 5's C3 cell reads "Practised: D2.Civ.10.9-12, D2.Civ.12.9-12 (owned grade 10 and US History
II)". In the data D2.Civ.12.9-12 is owned by one row, us2-civil-rights-movement (grade 12, unit 7 of a full-year
course). A grade 11 student taking Government has never met it, and a grade 12 student in the fall half meets it
only in about February.
**Why it matters.** q-ss-progression-1 says no Government row assumes a US history skill. "Practised" tells the unit
writer the skill was taught; for most Government students it was not.
**Fix (frame, unit 5 C3 cell and "What students learn").** C3 cell: "Practised: D2.Civ.10.9-12 (owned grade 10),
D3.2.9-12. Met here: how people used and challenged laws and courts to change them, through the two decisions'
background (D2.Civ.12.9-12 is owned by US History II; neither course assumes the other)." Add to "What students
learn": "for each decision, who brought the case and how they used the courts to change the law". No day change.
LAYER frame. REPEAT new.

### 2. The news-literacy bridge is drawn from the wrong grade 8 row (moderate; firm)

**What is wrong.** "For the lead" item 1 rightly sees that gov-policy-news (NML.T4.4, taking apart news and opinion)
leans on us1-news-reading (NML.T1.5, T4.1 to T4.3), which a grade 11 student may not have met: us1-news-reading is
placed "beside us1-empire", late in US History I, so a grade 11 student in either half has likely not had it. The
pick bridges from ss8-election-info and ss8-editorial-analysis. But the grade 8 row that teaches the same base (news
against opinion, who is behind a site, reading across sites, claims and evidence) is ss8-news-literacy (MA.8.T7.3 to
T7.5, civics unit 9), and it hands on only to wh1-sources-of-the-past and us1-news-reading.
**Why it matters.** A one-day bridge from the wrong rows reteaches campaign-finance sourcing and editorial claims, not
lateral reading and assertion against verification, which NML.T4.4 needs.
**Fix.** Frame: replace "For the lead" item 1's pick with "gov-policy-news opens with a readiness check on
ss8-news-literacy (dormant knowledge for a grade 11 student; a one-lesson reteach inside unit 8's 8 days for those
who miss it); a student who has had us1-news-reading meets it as retrieval". Add the row to the seam table:
"ss8-news-literacy (8) | news against opinion, lateral reading, credibility | Unit 8, gov-policy-news: readiness
check". Data (next progression fix pass): gov-policy-news assumes `ss8-election-info; ss8-news-literacy`, and
ss8-news-literacy's hands_on gains gov-policy-news. LAYER progression. REPEAT new.

### 3. Units 1, 3 and 7 have too few teaching days once their checks are counted (moderate; likely)

**What is wrong.** Each unit's days include a readiness check or retrieval opener, its reteach where a grade 8 row is
dormant, an end-of-unit assessment and a respond day. Counted that way:
- Unit 1: 6 days, two dormant grade 8 rows (ss8-citizenship, ss8-greek-roman-roots), 5 MA codes and 2 C3 codes, two of
  them research-and-evidence tasks (T1.4 theories tested on participation data, T1.5 Tocqueville against modern
  writers with membership data): about 2 to 3 teaching days.
- Unit 3: 7 days, two dormant rows (ss8-federal-state-powers, ss8-state-local-government), 5 MA codes, and tribal
  nations as a third sovereign. The civics frame's "For the lead" item 1 says no grade 8 row yet teaches present-day
  tribal governments, so unit 3 teaches it from the start: about 3 teaching days.
- Unit 7: 7 days, 8 MA codes ending in T5.8 (research a world issue, argue against opposing views): about 4 teaching
  days.
The frame's own "Unsure" proposes taking a day for unit 3 from unit 1, the tightest unit.
**Why it matters.** The unit writer will cut the research tasks the anchor names, which C1 reads as taught below
the standard's wording.
**Fix (frame, course in brief and units 1, 3, 4, 7).** (a) Course in brief: "Where a unit has two dormant grade 8
rows, one combined readiness check opens day 1 and one reteach lesson covers both." This frees a day in units 1 and
3; unit 3 keeps it for tribal sovereignty. (b) Unit 4 to 13 days and unit 7 to 8 days: grade 8's ss8-three-branches
already taught Congress's powers, veto and override and party leaders, so the Congress addition takes 2 days
(apportionment and redistricting, committees, how a bill becomes law), not about 3. (c) Delete the "Unsure" line's
idea of moving a day from unit 1. Days stay 80. LAYER frame. REPEAT new.

### 4. The check-set additions have no day budget (moderate; likely)

**What is wrong.** The additions named across the units are, in sum, most of the college-level government
framework: Congress in full; the amendment process and the Bill of Rights read whole; Federalist 70 and 78 and the
Letter from Birmingham Jail; political ideologies and socialization; fiscal federalism and the Commerce Clause cases;
incorporation, the religion clauses and the rights of the accused; the Electoral College and state election rules;
polls; treaty practice; the policy process stages; contacting officials. Each is said to fit "inside its days". Bar
item 10 says additions never push the year past its stated days, and C1 sets a 10 percent limit (about 7 days here)
on time outside the course's standards.
**Why it matters.** Unit 5 alone (9 days, 6 codes, two researched court decisions) cannot also teach incorporation,
the religion clauses and the rights of the accused as extra lessons. A writer told "add inside the days" with no
budget either overruns or picks at random.
**Fix (frame, course in brief and each "Check set adds" cell).** Add: "Additions ride inside an owned code's lesson
where one fits; at most 7 days in the course are for additions with no home code." Then mark each addition:
Federalist 70 (T2.7), Federalist 78 (T2.6), Letter from Birmingham Jail (T1.9), polls (T4.5), treaty practice (T5.3),
the policy process stages (T4.7), contacting officials (T4.8), fiscal federalism (T2.4) and the Bill of Rights read
whole (T3.1) ride inside; incorporation, the religion clauses and the rights of the accused enter unit 5 as the case
pairs students may choose for T3.2 (see "Settled by the expert"); the days go to Congress (2), the Electoral College
and the student's own state's election rules (1), political ideologies and socialization (1) and the Commerce Clause
(1). LAYER frame. REPEAT new.

### 5. Row notes still lean on grade 11 (minor; firm)

**What is wrong.** "For the lead" item 2 names one stale sentence ("government and economics are grade 12
courses"). The rows carry more grade 11 wording than that, all untrue for a grade 11 student since
q-ss-progression-1:
- gov-civic-associations: "set beside the reform groups met in grade 11".
- gov-policy-debates: "Builds directly on the grade 11 Progressive and suffrage studies".
- gov-world-affairs: "with grade 11's empire era as the first case".
- gov-rights-cases, gov-local-action, gov-world-affairs, gov-international-orgs: "the handoff skips a grade because
  grade 11 US History I does not carry it; government and economics are grade 12 courses".
- gov-foundations: "government is a grade 12 course".
**Fix (data/progressions/social-studies.csv, next fix pass).** Replace with: "set beside reform groups of the 1800s,
retaught in brief"; "uses Progressive-era and suffrage debates, retaught in brief from the source"; "with the empire
era of about 1898, retaught in brief, as the first case"; "Government is taken in grade 11 or 12; no civics course
sits in grades 9 to 11". LAYER progression. REPEAT yes (progression-social-studies finding 9).

### 6. One check-set line looks mis-cited (minor; likely)

**What is wrong.** Unit 4 cites New York 12.G2 for Congress in full. In New York's framework 12.G2 is civil rights and
civil liberties (from memory); the structure of government sits under 12.G1 and public policy under 12.G5. Unit 9
cites 12.G5 for contacting officials, which reads as 12.G4 (political and civic participation).
**Fix.** The unit plan's comparison table checks both against the document; until then the frame adds the line the
US History II frame carries: "the exact check-set lines are from the writer's knowledge and are read against the
documents at the unit plan's comparison table". LAYER frame. REPEAT new.

### 7. Stale status note (minor; firm)

data/plans/flow-status.csv, frame:us-government-and-politics: "active ... Writing: docs/pipeline/briefs/frame-write.md".
The frame is written and passes the gate. Fix: "Written; expert and Codex reads under way". The HANDOFF note that
q-ss-progression-1 is open for Cory is in the US History II read (finding 8). LAYER process. REPEAT yes (kindergarten
frame read finding 5).

## Checked and found right (do not undo)

- **Owned skills.** All 19 gov-* rows placed once. No gov-* row's `assumes` names a US History I or II row.
- **Standards in full.** MA.GOV.T1.1 to T5.8 with T2.8a to f, T2.10a to d and T4.6a to e; MA.NML.T1.1 to T1.4, T3.1,
  T3.3 to T3.5, T4.4 and T5.1 to T5.5. The rest of NML sits in us1-* rows (T1.5, T2, T3.2, T4.1 to T4.3), as the frame
  says. The C3 codes owned (D2.Civ.1, 2, 4, 5, 6, 7, 9, 11, 13 and D4.8) match their rows' skills; D2.Civ.1 is split
  across units 3 and 7 with each part named.
- **Own-state method.** Massachusetts's constitution, town meetings, state-local relations and executive offices are
  each taught as the student's own state with Massachusetts as one example beside another state.
- **Order.** Who holds power (unit 3) before how each branch uses it (unit 4); judicial review before rights cases;
  groups and media (unit 6) before world affairs and policy (units 7, 8) that use them; local action last.
- **Deliberation and action.** Mock hearings cast students as citizens and officials, never victims or perpetrators;
  a team may choose not to act publicly and still complete the look back.
- **Partial bases.** American Government 3e chapters map to the units as the book is ordered; Since Time Immemorial
  for tribal sovereignty after the sensitivity read.

## Seams

From grade 8 civics: every ss8-* row whose hands_on names a gov-* row is in the seam table at the right unit, and the
civics frame's hand-on table agrees. Missing: ss8-news-literacy (finding 2). The civics frame's pending fix on tribal
governments has not reached the data, so unit 3 cannot assume it (finding 3). From grade 7: no gov-* row assumes a
grade 7 row directly; ss7-roman-republic reaches Government through ss8-three-branches. From grades 9 and 10:
wh1-philosophies-of-government, wh2-research-argument, wh2-wwii-consequences, wh2-middle-east-since-1980 and
wh2-global-problems are picked up as the table says. After: none; threads end here as stated.

## Cross-subject

ELA 11 or 12 leans (RI.11-12.8, W.11-12.1 and 2, SL.11-12.1) exist in data/progressions/ela.csv under both grades'
row ids; the frame does not wait on them. The Algebra II lean (S-IC.B.6) has a local bridge in unit 6. No ELA 11, ELA
12 or Algebra II frame exists yet, so "taught first" cannot be checked. No finding.

## The lens checklist (course frame layer)

| Line | Result |
|---|---|
| An anchor standard in the course's Massachusetts topic range has no unit | Met: every MA.GOV code and the NML codes placed here have a unit |
| The replaced grade 3 year, or "your state" in grade 8, keeps Massachusetts-only content | Met by analogy: every Massachusetts-only code is taught as the student's own state |
| No unit lists what the check set adds, or an addition has no recorded source | Met for listing and source; days for additions missing (finding 4); two lines likely mis-cited (finding 6) |

## What I could not judge

- The New York, California and college-framework lines (not opened; finding 6).
- Accuracy of the tribal sovereignty content (the sensitivity read and the qualified person).
- When ELA 11 and 12 set the founding documents (no ELA 11 or 12 frame yet).

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| T3.2's two decisions are one pair from a set of four: Schenck (1919) and Brandenburg (1969) on speech; Plessy (1896) and Brown (1954) on equal protection; Betts (1942) and Gideon (1963) on the right to counsel, with incorporation; Minersville (1940) and Barnette (1943) on religion and the flag salute | Each pair shows a right growing between two rulings, and the last two carry the check-set additions (incorporation, rights of the accused, religion clauses) inside the standard's own task | docs/courses/us-government-and-politics/frame.md (unit 5) |
| T2.9's default case for majority and dissent is Youngstown Sheet and Tube v. Sawyer (1952); a teacher may swap in another separation-of-powers case | T2.9 asks what the case shows about how the branches relate, which a presidential-power case shows directly, and it keeps unit 5's rights cases distinct | docs/courses/us-government-and-politics/frame.md (unit 4) |

## For Cory

- **What schools are told about the grade 12 timetable** (this frame's "For the lead" item 4, the US History II
  frame's item 1). My pick: Government in the fall half. Beyond the frame's reason, unit 6 on parties and elections
  then falls near days 48 to 56, close to Election Day.

Not logged in the defect ledger: the brief allows edits to this report only. The caller may log findings 1 to 7
with found_by `expert`.

## Sources

- data/standards/ma-hss-2018.txt: every GOV and NML code and lettered part.
- docs/courses/civics-government-and-civic-life/frame.md: hand-on table and "For the lead" item 1 (tribal governments).
- From memory: the C3 9-12 civics indicator wording; New York's grade 12 Participation in Government strands
  (12.G1 to 12.G5); the Betts, Gideon, Minersville, Barnette and Youngstown decisions and dates; American Government
  3e chapter order.

## For the source list

Nothing new.

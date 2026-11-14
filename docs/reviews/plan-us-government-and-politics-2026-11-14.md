# Plan read: US Government and Politics, units 1 to 9 (2026-11-14)

Expert cold read of docs/courses/us-government-and-politics/s01.md to s09.md, written today by Codex from unit_skeleton.py skeletons. Done to docs/pipeline/briefs/plan-read.md, unit by unit, with the course-wide questions from the lead's brief.

## What I read

- AGENTS.md, docs/agents/EXPERT.md, docs/pipeline/briefs/plan-read.md, docs/agents/lenses/social-studies.md, docs/GLOSSARY.md.
- docs/courses/us-government-and-politics/frame.md and scope-and-sequence.md; data/plans/us-government-and-politics/days.csv (all 80 rows); data/progressions/social-studies.csv (the rows the course cites).
- The social studies part of docs/ADOPTION-BAR-SUBJECTS.md and docs/courses/social-studies/STANDARD.md.
- s01.md to s09.md in full.
- scripts/unit_skeleton.py, field 4 (lines 826 to 865).
- The "Settled by the expert" tables in plan-social-studies-kindergarten-2026-11-14.md, plan-social-studies-grade-1-2026-11-14.md and plan-social-studies-grade-4-2026-11-14.md, applied here and not re-argued.
- Gate: `plan.py check` passes the course (9 units, 80 days, 0 failures). An earlier exit code 255 was a PowerShell stderr artifact; rerun with output to a file, exit 0. No em dashes in any plan.
- Web checks this run, listed under Sources at the end.

Severity follows cost: **serious** (a student is taught or assessed wrongly, or a sensitivity failure reaches a classroom), **moderate** (the plan cannot be run as written, a standard part is weakly evidenced, or balance is not shown), **minor** (wording, a missing teacher note, a data tidy). REPEAT marks a fault already settled in an earlier read.

## Course verdict

The nine plans are careful, well sourced and nonpartisan in posture: invented cases are labelled as invented everywhere, students never disclose politics, status or family details, action in unit 9 is the student's own choice with a safe declining route, and the hard history (Cherokee removal, Saturday Night Massacre, Chile) is named plainly without role play. They are not yet to the bar for four reasons: unit 1's readiness check still sits "before day 1", against the lead rule of today; four end-of-unit assessments and four reteach days do not fit their minutes (REPEAT of the settled sizing rule); the teacher has no dated background on the 2025 and 2026 changes that touch units 2, 4, 6 and 7 (Louisiana v. Callais, the IEEPA tariff ruling, Trump v. Slaughter, Trump v. Barbara, Watson v. RNC, the USAID closure, the WHO exit, the 2026 midterm result); and the sensitivity studies for units 1 and 4 miss the frame's named focus, fairness across parties. No finding is serious; all are fixable inside the existing days.

## Course-wide findings

### CW1. Unit 1's readiness check is placed before day 1 (moderate; LAYER skeleton, data, plan; REPEAT of the lead rule 2026-11-14)

**What is wrong.** s01 field 4 says "**Given:** the start-of-year check, before day 1" and "Give these four short items in ten minutes, a few days ahead at most." The lead rule of today: no sitting before day 1. Unit 1 has readiness rows (four, all grade 8 or grade 10), so the check is the last ten minutes of day 1, after the hook, with the reteach on day 2 or 3. The same "start-of-year check" wording is in days.csv (days 1, 2, 4, 47), scope-and-sequence.md (lines 13, 17, 22, 31, 77) and the skeleton (unit_skeleton.py line 838), so every regeneration will put it back.

**Why it matters.** A teacher cannot give a check on a day that does not exist; a fall course often meets students for the first time on day 1.

**Fix.** The four items and the day 2 reteach station are good and stay. Only the timing moves. Exact edits in "For the fixer" 1 to 5. The frame's seams table already says "day 1", so it needs no change.

### CW2. End-of-unit assessments do not fit their minutes (moderate; LAYER plan; REPEAT)

Units 1 (day 5), 2 (day 14), 4 (day 34) and 6 (day 54). Settled in the grade 4 read: an assessment holds what its field 7 minutes hold, about 1 minute per recall item, 2 per one-sentence explanation, 8 per one-paragraph claim; longer arguments are judged on product days; cut instances, never parts. For a 50-minute grade 12 day with about 40 working minutes, that is one paragraph claim plus about eight short items, or two paragraph claims plus four short items. Unit fixes below.

### CW3. No dated teacher background on 2025 and 2026 changes (moderate; LAYER plan)

Settled in the grade 4 read: political and legal changes get a teacher background line, dated "checked (date)", stated as fact and not argued. The plans state a "Current check, November 14, 2026" in units 8 and 9 only. The changes that touch taught content, all verified today:

- **Louisiana v. Callais**, decided April 29, 2026, 6 to 3: narrowed vote-dilution claims under section 2 of the Voting Rights Act. Touches unit 2 (T1.9 present efforts, reserved 1965 Act text) and unit 6 (districts).
- **Learning Resources v. Trump** with Trump v. V.O.S. Selections, decided February 20, 2026, 6 to 3: the emergency powers law (IEEPA) does not authorize tariffs; the taxing power is Congress's. Touches unit 4 (checks and balances, T2.10).
- **Trump v. Slaughter**, decided June 29, 2026, 6 to 3: overruled Humphrey's Executor; the President may remove FTC commissioners at will. Same day, Trump v. Cook: the Federal Reserve governors keep their protection. Touches unit 4 (bureaucracy, removal).
- **Trump v. Barbara**, decided June 30, 2026: the birthright citizenship order (EO 14160) is unconstitutional under the Fourteenth Amendment. Touches unit 5 (day 39, Fourteenth Amendment) and unit 1 (citizenship).
- **Watson v. RNC**, decided June 29, 2026, 5 to 4: federal Election Day law does not bar counting mail ballots postmarked by Election Day and received later. Touches unit 6 (state voting rules, day 50).
- **Mid-decade redistricting**, 2025 to 2026: Texas (August 2025), Missouri (September 2025, referendum pending), North Carolina (October 2025), California Proposition 50 (November 2025). Touches unit 4 day 23 and unit 6.
- **2026 midterm**, November 3, 2026: Democrats won majorities in both chambers, seated January 3, 2027. A course taught in fall 2027 meets divided government. Touches unit 4 (Congress, leadership) and unit 6.
- **Venezuela**, January 3, 2026: the strikes and capture of Nicolas Maduro; war powers resolutions failed in the Senate (January 14, tie broken by the Vice President) and the House (tie vote). Touches unit 4 (T2.10d) and unit 7 (day 57).
- **Department of War**: a secondary title since the September 2025 executive order; the legal name is still Department of Defense (the fiscal 2027 defense bill would change it; not law as of this read). The plans' "Department of Defense" is correct; add the note so a teacher is not caught out.
- **USAID** closed July 1, 2025; remaining aid functions moved to the State Department. **WHO**: US withdrawal completed January 22, 2026. A January 2026 presidential memorandum withdrew from 66 international organizations, including the IPCC. Touches unit 7 (T5.4, T5.6, T5.7, items 7 and 9).

Fix: one background paragraph per unit, in field 10 under a "Current check" line, in the form the grade 4 settlement gives. Students keep the unit's limits; no student is asked to judge a ruling's merits by party. Wording per unit below.

### CW4. Reteach stations take the day's teaching or product minutes (moderate; LAYER plan)

Day 12 (unit 2, 10 minutes of a seminar day already over-full), day 39 (unit 5, 20 minutes), day 48 (unit 6, 30 of 50 minutes on the scored T4.2 research day), day 58 (unit 7, 20 minutes before six tools and six forces in 30 minutes). This is the same cost the settled rule "observations never take the only teaching minutes of a new skill" guards against. Settled here: a reteach station is ten minutes at the start of the day, for flagged students while the rest begin the day's work; if more than a third are flagged, ten minutes for everyone; never more than ten minutes, and never on a scored product day without moving the product minutes. Unit fixes below.

### CW5. The skeleton copies the wrong text into retrieval rows (minor; LAYER skeleton)

unit_skeleton.py line 832, `re.finditer(r'retrieval tasks?\b[^;]*', r['note'], re.I)`, matches any mention of a retrieval task, including forward references ("opens as a retrieval task on day 27"), and runs to the next semicolon. Result: s04 field 4 has a phantom day 23 row whose cell begins "retrieval task on day 27. Check set addition..."; s08 has a day 64 row carrying day 67's sentence and a day 67 row cut at a semicolon inside a parenthesis ("used last year in US History I" with no close). Fix in "For the structure pass".

### CW6. Sensitivity studies miss the frame's focus for units 1 and 4 (moderate; LAYER plan)

The frame names units 1, 4, 6 and 7 for a sensitivity read on fairness across parties, groups and countries. Units 6 and 7 do this. Unit 1's study (an AME church history, colored conventions minutes, Derrick Spires, the NABJ style guide) and unit 4's (steelworkers, independent-living and autistic self-advocates) are good community voices for some of the content but never study how each party and ideology describes itself, which is what day 2 (ideologies) and day 32 (the movement to limit government) need. Fix per unit below; add, do not replace.

### CW7. Note day references off by one in days.csv (minor; LAYER data)

Day 12 note "for students day 7 flagged" (unit 2's check is given on day 6); day 58 note "for students day 56 flagged" (unit 7's check is given on day 55); day 59 note "checked on day 38" (it is day 37; s07 itself notes this). Exact edits in "For the fixer".

## Unit 1: Foundations of government (days 1 to 6)

**1.1 Readiness check timing (moderate; plan, skeleton, data; REPEAT).** See CW1. s01 field 4, old: "**Given:** the start-of-year check, before day 1 (served in unit 1, which defines it).\nGive these four short items in ten minutes, a few days ahead at most." New: "**Given:** day 1, the last ten minutes, after the hook and the day's teaching (lead rule, 2026-11-14). Give these four short items on one printed page. Day 1's exit ticket moves to the five minutes before the check." Keep "Record each prerequisite separately..." onward, but change "Use results to prepare day 1's vocabulary cards and examples, without replacing its hook." to "Use results to set day 2's station and day 4's opening."

**1.2 Day 5 assessment over-full (moderate; plan; REPEAT CW2).** Seven items in about 40 working minutes, with item 4 a full source essay. Fix: keep the theory-against-data claim as one paragraph with two named sources (8 to 10 minutes); keep one short item per remaining code part (T1.1, T1.2, T1.3, T1.4, D2.Civ.2, D2.Civ.6); T1.5 is already scored from day 4's response, so remove its on-the-day item. Field 7's minutes then hold.

**1.3 Sensitivity study misses fairness across parties (moderate; plan; CW6).** Field 10, add to the study: the two major parties' own latest national platforms (preamble sections) and one self-description each from a conservative, a liberal, a libertarian and a socialist organization, so day 2's ideologies are each described in their own words; then check the day 2 cards for loaded labels. Keep the existing sources for the participation history.

**1.4 Day 2 ideologies not specified (moderate; plan).** Field 2 and the day 2 notes name no ideologies, no source for them and no balance rule. Fix, field 2 Teaching: "On day 2 teach conservatism, liberalism, libertarianism and socialism, each from its own published self-description, with one shared policy question; no student places themselves or their family." Also, the days.csv day 2 note cites "topics 4.1 to 4.4" of the college framework; ideologies of the parties sit later in that unit (topic 4.7 in the edition read before fall 2026). Confirm the fall 2026 topic numbers when the source cards are built and correct the note (likely).

**1.5 Day 2 and day 3 exit tickets too long for quarter-page exits (minor; plan).** Each asks three things. Cut each to one question with one reason.

**1.6 Figures to confirm at build (minor; plan).** The April 30, 2025 Census release is real (2024: 73.6 percent registered, 65.3 percent voted); the by-education and by-sex cells (52.5, 77.2, 82.5; 63.7, 66.9) are in its Table 5 and were not confirmed cell by cell today. The 2023 civic-life figures are confirmed (over 62.9 million members; 54 percent of members in two or more groups); the informal helping rate is 54 percent in the headline report, 54.2 in the Census story. State which source the card uses.

## Unit 2: Founding ideas (days 7 to 15)

**2.1 Day 12 minutes do not hold (moderate; plan; CW4).** Ten minutes of reteach, ten of Douglass, King's reading, twenty of seminar and ten of exit leave no time to read King or to prepare. Fix: reteach station ten minutes for flagged students while the rest read the Douglass extract; Douglass and King extracts together twenty; seminar fifteen; exit five.

**2.2 Day 14 assessment over-full (moderate; plan; REPEAT CW2).** Six items, including a provision for each of seven ideas, in about 32 working minutes. Fix: item 1 asks for four of the seven ideas, the teacher's choice printed on the paper (each idea is already evidenced on days 7 and 8); item 5 is scored from the day 12 and day 13 records, as its key already says, so it takes no assessment minutes. Item 3: replace "the reserved founding provision" with the provision's name (for example "Article IV, section 4") so students know which one.

**2.3 No dated background for T1.9 "present efforts" (moderate; plan; CW3).** Item 3 uses the original 1965 Act, section 2, and item 4's key names "current advocates". Field 10, add: "Current check, November 14, 2026: in Louisiana v. Callais (April 29, 2026), the Court held 6 to 3 that Louisiana's second majority-Black district was a racial gerrymander and narrowed vote-dilution claims under section 2. Present efforts now include work on both sides of that ruling. State it as fact; students compare methods, not parties." The reserved 1965 text stays as a historical text.

**2.4 Framework additions overload days 8 and 10 (minor; plan).** The fall 2026 framework does add required documents (confirmed: Federalist 39 and the Emancipation Proclamation; four in all). The Gettysburg Address was not confirmed as one of them today. Fix: keep Federalist 39 on day 8 as one short paragraph; on day 10, the Emancipation Proclamation only; add the Gettysburg Address only if the clarifications PDF lists it, and then as a five-minute reading.

**2.5 Day 11 presentations at 45 seconds are thin for T1.8 (minor; plan).** T1.8 asks to research and present. Fix: groups of three, ninety seconds each, with the written record collected; whole-class presentation is not needed.

**2.6 days.csv day 12 note, "day 7" should be "day 6" (minor; data; CW7).**

## Unit 3: Federalism and the states (days 16 to 22)

**3.1 Day 20 carries too much for the course's only tribal sovereignty day (moderate; plan).** Worcester, the removal timeline, McGirt, Castro-Huerta, Nisqually governance and institutional duties, with an exit. The plan's own minute line already fills fifty. Fix: teach Worcester (with the removal timeline, kept brief) and McGirt as the two holdings; the Nisqually constitution as the nation's own voice; give Castro-Huerta one teacher sentence ("in 2022 the Court held that states share jurisdiction over some crimes by non-Indians in Indian country") and drop it from the exit and comparison. The frame does not name Castro-Huerta, and treating it as a third holding on a crowded day risks the lesson reading as a slide in sovereignty rather than distinct questions. Facts checked and correct: Worcester (1832), McGirt (2020, Muscogee, Major Crimes Act), Castro-Huerta (2022), Lopez, Raich, the Massachusetts articles cited, "more than 570" nations (574).

**3.2 Sensitivity framing note for day 20 (minor; plan).** Add to field 10's teacher note: "Present the Nisqually Indian Tribe as a governing nation today, from its own constitution; no student represents a nation, and no case is framed as winners and losers." This applies the settled point that nations are varied, each from its own sources (grade 4 read).

## Unit 4: The three branches and checks and balances (days 23 to 35)

**4.1 No dated background on 2026 rulings and war powers (moderate; plan; CW3).** Field 10, add: "Current check, November 14, 2026: Learning Resources v. Trump (February 20, 2026, 6 to 3): emergency powers law does not authorize tariffs; tariffs are Congress's taxing power. Trump v. Slaughter (June 29, 2026, 6 to 3): Humphrey's Executor overruled; the President may remove FTC commissioners at will; the same day Trump v. Cook kept Federal Reserve governors' protection. January 2026: after the Venezuela operation, war powers resolutions failed in the Senate and the House. The November 2026 election gave Democrats both chambers from January 3, 2027. The department's legal name is still Department of Defense; 'Department of War' is a secondary title. Teach these as facts and as checks and balances at work; no student is asked which side was right by party." Day 31's war powers work and day 25's bureaucracy can use the first three as optional current cases.

**4.2 Sensitivity study misaimed (moderate; plan; CW6).** Field 10 "Sensitivity study": keep the steelworkers' and disability voices for deregulation's effects, and add the frame's focus: the movement to limit government described by its own advocates (the Reagan 1981 address is there; add one current advocacy organization for limited government) and by its critics (the Obama 2011 speech is there; add one current organization critical of it), with each side's current claims about 2025 federal workforce cuts stated from its own pages. Day 32 then has equal sources on both sides, which its days.csv note already requires.

**4.3 Day 33 judgment gets ten minutes for two scored products (moderate; plan).** Fix: the written judgment takes twenty minutes; the hearing record is scored from observation during the hearing, not written after.

**4.4 Day 34 assessment over-full (moderate; plan; REPEAT CW2).** Items 7a to 7d each ask for an unused passage plus an evaluation. Fix: students answer two of 7a to 7d on the day (the teacher picks which two and prints them on the paper); the other two parts are scored from days 29 to 31 written work, where each was taught.

**4.5 Reconciliation example from one party only (minor; plan; balance).** Item 7c and its teaching name the 2017 tax law. Add one law passed by reconciliation under the other party's majority (the 2021 American Rescue Plan or the 2022 Inflation Reduction Act) and the 2025 reconciliation law, so students see the procedure used by both.

**4.6 Phantom day 23 retrieval row (minor; skeleton; CW5).** Field 4 lists a day 23 retrieval row whose cell is day 27's sentence. Day 23 already follows day 22's readiness check. Fix: delete the day 23 row; the day 27 row stays.

**4.7 Day 23 apportionment and redistricting with no current case (minor; plan).** Add one teacher line: 2025 mid-decade redistricting in Texas, Missouri, North Carolina and California (Proposition 50), each by its own state's official record; maps change, so check before teaching.

## Unit 5: Rights and liberties (days 38 to 46)

**5.1 Day 44 over-full (moderate; plan).** Five government-control episodes plus the closing claim. Fix: three episodes (one US historical, one present, one from another country), then the claim.

**5.2 "Present" government control uses Russia only (moderate; plan; balance).** The present case points every student at a foreign rival. Add an optional present US case stated from court records, from more than one administration (for example Murthy v. Missouri, 2024, and the 2025 press-access disputes, each from the court's own record), so students judge the principle, not the country.

**5.3 Day 39 reteach takes twenty minutes (moderate; plan; CW4).** Cut to ten per the settlement. Add to day 39's teacher background: "Trump v. Barbara (June 30, 2026): the birthright citizenship order was held unconstitutional under the Fourteenth Amendment's Citizenship Clause." Facts checked and correct: Lovell (Griffin, Georgia, 1938), Mapp, Betts and Gideon (22 states supported Gideon), UDHR Article 12, twelve amendments proposed and ten ratified in 1791.

## Unit 6: Parties, elections and interest groups (days 47 to 55)

**6.1 Day 48 reteach takes thirty of fifty minutes on the scored research day (moderate; plan; CW4).** Fix: reteach ten minutes for flagged students while the rest open the platforms; the T4.2 research keeps at least thirty minutes.

**6.2 Day 54 assessment over-full (moderate; plan; REPEAT CW2).** Nine items with seven packet sources in forty minutes. Fix: four sources; items scored from day 48 and day 51 products come off the sitting; keep one item per remaining code part.

**6.3 No dated background on 2026 election law and results (moderate; plan; CW3).** Field 10, add: "Current check, November 14, 2026: Watson v. RNC (June 29, 2026, 5 to 4): states may count mail ballots postmarked by Election Day and received later; state rules still differ. Louisiana v. Callais (April 29, 2026) narrowed section 2 vote-dilution claims. 2025 to 2026 mid-decade redistricting changed maps in several states. The November 3, 2026 election gave Democrats majorities in both chambers from January 3, 2027." Day 50's state rule comparison keeps its rule: dated official pages only.

**6.4 Live elections during the unit (minor; plan).** Weeks 10 to 11 of a fall half fall near early November. Add a teacher note: a live election is used only through official election offices and all candidates' own statements; no student is asked how anyone at home votes.

**6.5 Platforms are 2024 (minor; plan).** Label them "the latest national platforms (2024)" and check for newer ones at build.

**6.6 Day 47 goal and note wording (minor; data; CW1).** In "For the fixer".

Facts checked and correct: the electoral vote example (22 of 37), the Citizens United statement, King, Schneer and White.

## Unit 7: Foreign policy and the world (days 56 to 63)

**7.1 Aid and international organization content ignores 2025 and 2026 changes (moderate; plan; CW3).** Item 7's and item 9's answers speak of bilateral aid and contributions as if the 2022 channels were unchanged. Field 10, add: "Current check, November 14, 2026: USAID closed July 1, 2025; remaining aid functions moved to the State Department. The US withdrawal from the World Health Organization was completed January 22, 2026. A January 2026 presidential memorandum withdrew the United States from 66 international organizations. State as fact; students judge routes that exist when the course is taught." Item 7 sample answer, old: "Bilateral aid may be quicker but less coordinated." New: "Aid through the State Department may be quicker but less coordinated." Item 9 keeps "within United States funding law".

**7.2 T5.8's "identify" is weakly evidenced by a fixed 2022 case (moderate; plan).** The plan dates the Pakistan 2022 record honestly (field 5, "never present its figures as current"), and its sources are partly jointly authored by the UN and the government, which the plan notes. But students never identify the issue: the course hands it to them. Fix, inside day 60's record: each student adds one dated later source showing whether disaster displacement in Pakistan has recurred (official national or UN reports from a later monsoon season), and says in one sentence why it counts as a current world issue. No added day.

**7.3 Day 58 over-full, and its Middle East reteach comes too late (moderate; plan; CW4).** Twenty minutes of reteach, then six tools, six forces, 1898 and Chile in thirty. Day 56 already uses Kuwait. Settled here (a swap inside the unit): the wh2-middle-east-since-1980 reteach moves to day 56's first ten minutes; day 58 keeps forty minutes for its lesson and five for the exit. Change days.csv notes for days 56 and 58 (see "For the fixer").

**7.4 days.csv day 58 "day 56" should be "day 55"; day 59 "checked on day 38" should be "checked on day 37" (minor; data; CW7).**

Facts checked and correct: Security Council voting (nine yes votes with one permanent-member no fails; abstention does not veto), the treaty process.

## Unit 8: Policy in the news (days 64 to 71)

**8.1 The traceability rule's date (minor; plan).** Field 10 says to "distinguish final rule, proposed extension and congressional enforcement restriction". The extension is now settled: compliance and enforcement move to July 20, 2028 (FDA extension; the 2026 continuing appropriations act bars enforcement before that date). New: "the 2022 final rule; compliance moved to July 20, 2028 by FDA and by the 2026 appropriations act; recheck before teaching." The plan's correction of the consumer group's chronology (the final rule is dated November 15, 2022) is right and careful.

**8.2 Day 66 leaves ten minutes unassigned (minor; plan).** Ten plus twenty-five "within the remaining forty-five". Give the ten to sharing and the exit.

**8.3 Retrieval rows for days 64 and 67 garbled (minor; skeleton; CW5).** Day 64's cell carries day 67's sentence; day 67's is cut at a semicolon. Fix: day 64 cell "Retrieval task on ss8-election-info (a maintained skill, kept in use through grade 11 by us1-research-inquiry)."; day 67 cell "Retrieval task on ss8-news-literacy (used last year in US History I's news reading)."

## Unit 9: Local action (days 74 to 80)

Unit 9 is the strongest plan: the action is the student's choice, the declining route is real, adult-mediated contact and no public posting protect students, the unseen packet is labelled as invented, partial T5.4 and T5.5 coverage is said plainly, and day 80 reflects on a response or its absence without needing a policy win. Retrieval-only handling in field 4 is right (no readiness rows).

**9.1 Day 74 has no minute plan (minor; plan).** It carries the hook, two retrieval questions, modeling of authority, perspective and compromise, teaching fair deliberation, about six observations and an exit. Add: hook five, retrieval five, modeling fifteen, team work twenty (observations here), exit five.

**9.2 Boston's participatory budgeting cycle will be stale (minor; plan).** The hook says proposal development is in autumn 2026 and voting in 2027. A course taught in fall 2027 or later meets a different phase. Field 10 already says "Verify the student's own body's current notice"; add the same for the hook: "Check Boston's current phase before the hook; use it only as a worked example of eligibility rules." This also keeps the settled own-place rule (grade 3 read): Boston is a worked example, not the case students act on.

**9.3 Voice: "On 74" (minor; plan).** Field 2 and field 5 write "On 74", "on 78". Write "on day 74" so a teacher reads it at a glance.

## Course flow

The handoffs hold: each plan carries the next unit's readiness items, and the readiness-before-unit pattern is consistent from unit 2 on. Unit 4 to 5 runs through course-level check 1 (days 36 and 37) cleanly; unit 8 to 9 through check 2 (days 72 and 73), with day 73 confirming the issue, authority and route that unit 9 needs. Unit 9's look back at the day 68 request and day 77 action closes the course. Voice is plain full sentences throughout, dense in places (units 4 and 7 field 5) but readable.

Nothing invented is passed off as real: every fictional case is labelled, and real sources are linked and dated. No company or product names appear in student or family copy; no claim of review or approval.

## Settled by the expert

| Question | Ruling | Where it binds |
|---|---|---|
| When is unit 1's readiness check given? | Lead rule 2026-11-14 applied: the last ten minutes of day 1, after the hook; the reteach station stays on day 2; day 1's exit moves to the five minutes before the check. Earlier rulings (kindergarten, grade 1, grade 4) that placed it "by the start-of-year check" are superseded for this course by the lead rule. | s01 field 4; days.csv days 1, 2, 4, 47; scope-and-sequence.md; unit_skeleton.py |
| How long may an end-of-unit assessment run at grade 12? | Settled earlier (grade 4 read), applied: its field 7 minutes, about 1 per recall item, 2 per one-sentence explanation, 8 to 10 per paragraph claim; parts taught and scored on earlier product days come off the sitting. Cut instances, never parts. | s01, s02, s04, s06 field 5 and 7 |
| How long may a reteach station run? | Ten minutes at the start of the day, flagged students only while others start the day's work; everyone if more than a third are flagged; never more than ten, and never taking a scored product's minutes. Same reason as the settled rule that observations never take the only teaching minutes. | s02 day 12, s05 day 39, s06 day 48, s07 day 58 |
| Unit 7's Middle East reteach day | Moves from day 58 to day 56's first ten minutes, since day 56 uses Kuwait. Swap inside the unit. | s07 fields 4 and 7; days.csv days 56 and 58 notes |
| How are 2025 and 2026 legal and political changes handled? | Settled earlier (grade 4, "current official facts"), applied: a dated teacher background line per unit, stated as fact, never argued by party. | s02, s04, s05, s06, s07 field 10 |
| Native nations | Settled earlier: varied, each from its own sources. Applied to unit 3 day 20 (Nisqually from its own constitution; Castro-Huerta to one teacher sentence). | s03 |
| Balance across parties in examples | Where a procedure or power is shown by one example, add one from the other party's majority or administration. | s04 item 7c, s05 day 44 |
| Unit 7's T5.8 case | Pakistan 2022 stays as the class case; each student adds one later dated source and a one-sentence identification on day 60. No added day. | s07 field 5, day 60 |

## For the fixer

Exact edits, in order. Nothing here adds days. Run `plan.py check` after the data edits. Log each item below with `plan.py defect` (I could not; this read edits only its report).

1. **scripts/unit_skeleton.py line 838.** Old: `'**Given:** the start-of-year check, before day 1 (served in unit 1, which defines it).'` New: `'**Given:** day 1, the last ten minutes, after the hook (lead rule 2026-11-14); reteach on day 2 or 3. If this course has no unit 1 readiness rows, write: none needed; retrieval only.'` Line 839's marker text: replace "Define the start-of-year check" with "Write unit 1's readiness items".
2. **days.csv day 1 note.** Old: "Unit 1's readiness check, served by the start-of-year check before this day, covers" New: "Unit 1's readiness check, given in this day's last ten minutes after the hook, covers". If the assess column marks readiness days elsewhere, mark day 1 the same way and confirm `plan.py check` accepts it.
3. **days.csv day 2 note.** Old: "(in the start-of-year check)" New: "(given in day 1's last ten minutes)". **Day 4 note.** Old: "Uses the start-of-year check's readiness items" New: "Uses day 1's readiness items". **Day 47 goal.** Old: "(checked before unit 1)" New: "(checked on day 1)". **Day 47 note.** Old: "checked in the start-of-year check" New: "checked on day 1".
4. **scope-and-sequence.md.** Line 13, old: "and for unit 1 in the start-of-year check," new: "and for unit 1 in the last ten minutes of day 1, after the hook (lead rule, 2026-11-14),". Line 17, old: "Start-of-year check:" new: "Day 1, last ten minutes, after the hook:". Lines 22 and 77, old: "(checked in the start-of-year check)" new: "(checked on day 1)". Line 31, old: "the start-of-year check, before day 1 (see the table)" new: "the last ten minutes of day 1, after the hook (see the table)".
5. **s01 field 4** per 1.1; mirror the days.csv wording in s01's and s06's day lists (they copy days.csv).
6. **days.csv note day references.** Day 12: "day 7 flagged" to "day 6 flagged". Day 58: "day 56 flagged" to "day 55 flagged". Day 59: "checked on day 38" to "checked on day 37".
7. **Unit 7 reteach swap (7.3).** Day 56 note: add "Reteach station (first ten minutes): wh2-middle-east-since-1980, for students day 55's check flagged." Day 58 note: remove its reteach sentence. s07 fields 4 and 7 to match.
8. **Assessment sizing:** s01 1.2, s02 2.2, s04 4.4, s06 6.2.
9. **Reteach caps:** s02 2.1, s05 5.3, s06 6.1, s07 7.3.
10. **Current-check background lines:** s02 2.3, s04 4.1 and 4.7, s05 5.3, s06 6.3, s07 7.1, s08 8.1.
11. **Sensitivity studies:** s01 1.3, s04 4.2; then the sensitivity agent read for units 1, 4, 6 and 7 as the frame assigns.
12. **Content:** s01 1.4, s03 3.1 and 3.2, s04 4.3 and 4.5, s05 5.1 and 5.2, s07 7.2.
13. **Minor:** s01 1.5, 1.6; s02 2.4, 2.5; s04 4.6; s06 6.4, 6.5; s08 8.2, 8.3; s09 9.1 to 9.3.

## For the structure pass

- **Retrieval rows in field 4 (CW5).** unit_skeleton.py line 832: split each note into sentences first; keep a sentence only if it begins with "Retrieval task" (or contains "retrieval task" and not "on day N" for a different N); take the whole sentence, not up to the first semicolon. This removes the phantom forward rows (s04 day 23, s08 day 64) and the truncation (s08 day 67).
- **Start-of-year wording in data and docs (CW1).** Search the other courses' days.csv and scope-and-sequence files for "start-of-year check" and "before day 1"; the lead rule applies to every course, and the skeleton change in item 1 only fixes new plans.
- **A "Current check" line in the template.** UNIT-PLAN.md field 10 could carry a standing "Current check (date):" line for social studies, so the dated background in CW3 has one home in every plan.

## For Cory

None. Everything here is inside the plans, the data and the skeleton.

## Sources (web checks, November 14, 2026)

- Louisiana v. Callais, April 29, 2026: [CRS legal sidebar](https://www.everycrsreport.com/files/2026-05-14_LSB11431_48af6cb5471173e0592ed8ebda1b472d7f10621b.html), [Constitution Center](https://constitutioncenter.org/blog/the-supreme-courts-callais-decision-sets-new-framework-for-racial-gerrymandering).
- Learning Resources v. Trump, February 20, 2026: [King and Spalding](https://www.kslaw.com/insights/articles/u-s-supreme-court-invalidates-the-president-s-ieepa-tariffs-in-learning-resources-inc-v-trump).
- Trump v. Slaughter and Trump v. Cook, June 29, 2026: [CRS](https://www.everycrsreport.com/reports/LSB11448.html), [Venable](https://www.venable.com/insights/publications/2026/06/supreme-court-overrules-humphreys-executor).
- Trump v. Barbara, June 30, 2026: [CRS](https://www.everycrsreport.com/reports/LSB11468.html).
- Watson v. RNC, June 29, 2026: [Snell and Wilmer](https://www.swlaw.com/publication/supreme-court-holds-federal-election-day-statutes-do-not-preempt-state-receipt-deadlines-for-timely-cast-mail-ballots/).
- Department of War name status: [Breaking Defense, April 2026](https://breakingdefense.com/2026/04/pentagon-formally-requests-name-change-to-war-department-setting-up-fight-with-dems/), [House vote, July 22, 2026](https://www.valleynewslive.com/2026/07/22/house-votes-department-war-renaming-part-an-annual-defense-bill/).
- Venezuela and war powers votes, January 2026: [CRS](https://www.everycrsreport.com/reports/IN12618.html), [Senate vote](https://www.legion.org/information-center/news/security/2026/january/vote-to-curb-military-action-in-venezuela-blocked-in-senate).
- USAID closure, July 1, 2025: [NPR](https://www.npr.org/2025/07/01/nx-s1-5451372/usaid-officially-shuts-down-and-merges-remaining-operations-with-state-department), [CRS](https://www.everycrsreport.com/files/2025-09-05_IF10261_675e6d431c41d3c7bcbda03dda2ee4dd857e4c3e.html).
- WHO withdrawal and the 66-organization memorandum: [ABC7](https://abc7news.com/post/us-completes-withdrawal-world-health-organization/18455132/), [Al Jazeera](https://www.aljazeera.com/news/2026/1/8/trump-to-withdraw-us-from-dozens-of-un-international-organisations).
- Mid-decade redistricting: [Voting Rights Lab](https://votingrightslab.org/2026/05/26/an-emerging-trend-mid-decade-redistricting/), [PBS](https://www.pbs.org/newshour/amp/politics/a-state-by-state-look-at-the-narrowing-redistricting-battle-for-the-u-s-house).
- 2026 midterm result: [OPB/NPR](https://www.opb.org/article/2026/11/04/2026-midterms-democrats-win-the-senate/).
- Fall 2026 framework additions: [clarifications PDF](https://apcentral.collegeboard.org/media/pdf/ap-us-government-and-politics-course-and-exam-description-clarifications-effective-fall-2026.pdf), [course page](https://apcentral.collegeboard.org/courses/ap-united-states-government-and-politics/course).
- Food traceability compliance date: [FDA rule page](https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-requirements-additional-traceability-records-certain-foods), [NC State extension note](https://foodbusiness.ces.ncsu.edu/news/fda-fsma-204-food-traceability-rule-july-20-2028/).
- Census 2024 voting release: [press release, April 30, 2025](https://www.census.gov/newsroom/press-releases/2025/2024-presidential-election-voting-registration-tables.html), [tables](https://www.census.gov/data/tables/time-series/demo/voting-and-registration/p20-587.html).
- Civic engagement 2023: [AmeriCorps headline report](https://americorps.gov/sites/default/files/document/2025-01/CEV2023_HeadlineReport_12192024_508.pdf), [Census story](https://www.census.gov/library/stories/2024/11/civic-engagement-and-volunteerism.html).

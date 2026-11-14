# Baseline 1 read: social studies subject column (2026-11-14)

Reader brief: docs/pipeline/briefs/baseline-1.md. Part: the social studies subject column, all 15 course frames read as one climb from kindergarten to grade 12. Bar: docs/agents/lenses/social-studies.md, the Massachusetts 2018 anchor (data/standards/ma-hss-2018.txt) and the C3 indicators it names. Expert rules: docs/agents/EXPERT.md.

Desk card q-ss-frames-1 holds four open questions for Cory (time a week or a day, the grade 12 timetable, the Since Time Immemorial licence reading, people or pay). This read does not raise them again.

## What was read

- The brief, docs/agents/EXPERT.md, AGENTS.md, docs/GLOSSARY.md, docs/agents/lenses/social-studies.md, docs/pipeline/briefs/frame-write.md (lessons 1 to 15), and docs/PRODUCTION-PATH.md steps 2 to 4.
- All 15 frames: docs/courses/<slug>/frame.md for social-studies-kindergarten, social-studies-grade-1 to -5, world-geography-and-ancient-civilizations-i and -ii, civics-government-and-civic-life, world-history-i and -ii, us-history-i, us-history-ii, us-government-and-politics, economics.
- data/progressions/social-studies.csv. Rows read in full: us1-research-inquiry, us1-argument-writing, us2-research-paper, wh1-historical-argument, wh1-inquiry-questions, wh1-sources-of-the-past, wh1-belief-systems, wh1-african-kingdoms, wh2-research-argument, ss6-research-contribution, ss6-silk-roads-exchange, ss7-rome-fall, ss7-greek-wars, ss7-silk-road-trade, ss8-greek-roman-roots. Every C3 code owned by two rows was listed with a script.
- data/standards/ma-hss-2018.txt and data/standards/c3-indicators.txt (codes only, no indicator text).
- docs/reviews/frame-ss-lead-items-2026-11-14.md and the progression fixes report.
- Gate: `python -X utf8 scripts/plan.py check` gives 0 failures for social studies. Its notes (grade skips, the branches-of-government model unused in grades 6 and 10) were read. ELA gate results were ignored, as instructed.

Shapes found:

| Course | Units | Days | Course checks and respond days | Time a day stated |
|---|---|---|---|---|
| Kindergarten | 6 | 64 | 4 check, 2 respond | 20 to 30 min, 2 a week |
| Grade 1 | 8 | 96 | 3, 2 | about 30 min, 3 a week |
| Grade 2 | 7 | 96 | 3, 2 | 30 to 40 min, 3 a week |
| Grade 3 | 7 | 160 | 6, 4 | 40 min |
| Grade 4 | 7 | 160 | 6, 4 | 40 min |
| Grade 5 | 10 | 160 | 4, 4 | 40 min |
| Grades 6, 7, 8 | 11, 12, 10 | 160 each | 6, 6 (2 + 2 per check pair, roughly) | 45 min |
| World History I | 10 | 160 | 8, 4 | not stated |
| World History II | 11 | 160 | 7, 3 | not stated |
| US History I | 9 | 160 | 8, 4 | not stated |
| US History II | 12 | 160 | 3, 3 (unit respond days inside units) | not stated |
| US Government and Politics | 9 | 80 | 2, 2 | not stated |
| Economics | 9 | 80 | 2, 2 | not stated |

## Verdict

The kindergarten to grade 8 climb is sound: map, scale, timeline and claim skills step up cleanly, the hard-history and values notes are strong, and the gate is clean. The high school column is not yet one climb. The research and argument thread is "taught in full" in three or four courses with depth lines that contradict each other, and many cases (Wampanoag, Cherokee removal, Federalist 51 and Brutus No. 1, Silk Roads, the Constitutional Convention, civil rights law) recur across grades without a retrieval line, so a student would meet them as new more than once. All fixes are frame and progression wording; none needs Cory except the items already on his card.

## Findings (most serious first)

### 1. The high school research and argument thread is taught in full three or four times, with contradicting depth lines
LAYER: progression, frame. REPEAT: new. Confidence: firm.

- Files: data/progressions/social-studies.csv rows us1-research-inquiry, us1-argument-writing, us2-research-paper, wh2-research-argument, wh1-inquiry-questions; frames world-history-i (units 1, 10), world-history-ii (unit 11), us-history-i (units 1, 5), us-history-ii.
- What is wrong: World History I unit 1 teaches the five source checks and inquiry, and unit 10 owns D4.1 and D4.2 at the 9 to 12 level. World History II unit 11 has students find their own sources and answer critique. US History I unit 1 then teaches the research cycle "in full", and its row says "Grade 11 depth: students build their own question and source set, where earlier grades worked from a question and set the teacher gave", which is false against the grade 10 row (and grade 6's research contribution). US History I unit 5 teaches the several-page argument and D4.2 "in full" again. The us2-research-paper grade 12 depth (picks the question, builds the source set, answers the strongest counterargument) repeats grades 10 and 11. D1.1 to D1.5, D3.1 to D3.4, D4.1, D4.2 and D2.His.11, 12 and 16 are each owned by a grade 9 or 10 row and a us1 row; D4.3 to D4.5 by wh2-research-argument and us2-research-paper, with only "two contrasting audiences" between them.
- Why it matters: the progression's promise is that each grade adds something named. Here the grade 11 and 12 days would reteach what grade 10 just did, and the stated depth lines would mislead the day writers.
- Fix:
  - us1-research-inquiry depth: "Grade 11 adds: the student's own enduring question carried across the whole course, with a source set of at least eight, including two the class never saw. Retrieves the grade 9 five source checks and the grade 10 own-source search."
  - us1-argument-writing depth: "Grade 11 adds: a several-page argument taken through three drafts with written feedback, counterclaim answered in each section, not only once."
  - us2-research-paper depth: "Grade 12 adds: an outside audience and two contrasting forms (a written paper and a public piece such as a brief or talk), judged against D4.3 to D4.5."
  - wh2-research-argument depth for D4.3 to D4.5: "Grade 10: presents to the class and one other class. Grade 12 goes further (outside audience, two forms)."
  - US History I frame units 1 and 5: replace "taught in full" with "retrieved from grades 9 and 10, then extended".

### 2. The counterclaim thread changes its name and doubles back
LAYER: frame, progression. REPEAT: new. Confidence: firm.

- Files: world-geography-and-ancient-civilizations-ii frame unit 12; civics-government-and-civic-life frame; us-history-ii frame (writing section, unit 7).
- What is wrong: grade 7 unit 12 "names the strongest opposing claim and says why the evidence still favors its own", which is the full answer, while grade 8 claims "answering in full" as its own new step. US History II says "The counterclaim enters at unit 7" and "Writing builds from a sourced paragraph (unit 2)", in grade 12, after grades 8 to 11 have all required it. The thread is also called opposing claim, counterclaim and counterargument in different places.
- Why it matters: a grade 12 course that starts from a sourced paragraph and introduces the counterclaim halfway through drags seniors back to grade 7.
- Fix: grade 7 unit 12 reads "names the strongest opposing claim" only (drop "and says why the evidence still favors its own"). US History II: replace "The counterclaim enters at unit 7" with "The counterclaim is retrieved from grades 8 to 11 and required in every argument from unit 2", and "builds from a sourced paragraph (unit 2)" with "starts from a full sourced argument (unit 2)". Use "counterclaim" in every frame and row.

### 3. Repeated cases with no retrieval line
LAYER: frame. REPEAT: yes in part (lesson 11 kind). Confidence: likely.

For each, the fix is a line in the later frame: "Met in grade X; this unit adds Y", or a swap where named.

| Case | Where | Fix |
|---|---|---|
| Wampanoag and the 1621 harvest | K unit 5; grade 3 units 4 and 5; grade 5 units 1 and 7 | Grade 3 Northeast case becomes another nation (settled below); grade 5 retrieves K and names what it adds (the treaty and land-loss record) |
| Cherokee removal | grade 2 unit 5; grade 3 unit 4; grade 5 unit 7; US History I unit 3; Government unit 3 | Grade 3 retrieves grade 2; grade 5 adds Worcester v. Georgia and the law; US History I adds the policy debate; Government uses it only as a retrieval case for judicial review limits |
| Persian roads, Alexander, Silk Roads | grade 6 unit 8; grade 7 units 4 and 9; World History I units 1 and 3 | World History I retrieves grades 6 and 7 and adds the comparative network question |
| Faiths | grade 6 unit 7; grade 7 units 2 and 3; World History I unit 2 (six faiths side by side) | Retrieval line for each faith already met, not only Christianity; the row already says "content revisited" |
| Axum, Swahili coast, ancient Ghana | grade 6 unit 9; World History I unit 3 | Retrieval line in the frame (the row has it) |
| Mexica and Tenochtitlan | grade 4 unit 4; World History I unit 4 says "grade 6 offered the Maya" | Name grade 4's Mexica case as retrieval |
| Articles of Confederation, Shays' Rebellion, Convention compromises | grades 5 and 8; US History I unit 2 at the same depth | US History I retrieves and adds the ratification debates by state |
| Federalist 51, Brutus No. 1 | grade 8 unit 2; Government unit 2 | Government retrieves both and teaches Federalist 10 as new (settled below) |
| Locke, Montesquieu, English Bill of Rights | grade 8 unit 1; World History I unit 10 | Retrieval line; World History I adds the comparison with the other revolutions |
| Atomic bombs and how present views shape interpretation | World History II unit 6; US History II unit 5 | US History II retrieves and adds the domestic decision record |
| September 11 and the civil liberties debate | World History II unit 10; US History II unit 11 | US History II retrieves and adds the statute and court record |
| Civil rights acts; 1977 sit-in, ADA, Stonewall, Obergefell | grades 5 and 8; World History II unit 8; US History II units 7 and 9 | Retrieval lines in the later frames, each naming what it adds |
| Government case pairs | Minersville and Barnette (grade 8); Plessy to Brown and Schenck (US History I); Brown (grade 5) | Government's default pair changes (settled below); a student who met a pair earlier picks another |

Why it matters: lesson 11 says picks do not repeat other grades. Without retrieval lines the day writers will teach these as new and spend days twice.

### 4. Informed action repeats a product
LAYER: frame. REPEAT: new. Confidence: likely.

- Files: social-studies-grade-2 frame unit 3; social-studies-grade-4 frame unit 7; us-history-i frame unit 8; us-government-and-politics frame unit 9.
- What is wrong: grade 2's storm readiness plan for the school and grade 4's local hazard preparedness guide are the same product, and the grade 4 frame never names grade 2. A grade 11 student taking US History I with Government runs two local-problem actions in one year.
- Why it matters: informed action is once a year and should climb; a repeated product reads as busywork.
- Fix: grade 4 unit 7 action becomes "a written proposal to the school or town on one hazard response, judged against the policy the class traced", with "retrieves the grade 2 readiness plan". US History I unit 8 adds: "When Government runs the same year, this action is replaced by Government's unit 9 action." (Whether the two run the same year is the timetable question already on Cory's card.)

### 5. Grade 6 teaches the grade 9 source list
LAYER: frame, progression. REPEAT: new. Confidence: likely (C3 wording from memory; the codes file has no text).

- Files: world-geography-and-ancient-civilizations-i frame unit 8; row ss6-research-contribution notes; world-history-i frame unit 1.
- What is wrong: grade 6 teaches "origin, authority, structure, context and corroborative value", the 9 to 12 list (D3.1, D3.2 at 9 to 12), and World History I unit 1 then teaches the same five as new.
- Fix: grade 6 uses the 6 to 8 depth: "origin, structure, context, and whether other sources agree". Leave "authority" and the named five source checks to grade 9.

### 6. Two year-end checks sit below what the year taught
LAYER: frame. REPEAT: new. Confidence: firm for grade 3, likely for grade 8.

- Grade 3 check 3 asks for "a short claim from an unseen source", one source, below grade 2's end check (two accounts compared, a claim with two facts from named sources). Fix: "a short claim with evidence from two unseen sources on a community's change over time, saying where they agree and differ."
- Grade 8 (civics-government-and-civic-life) check 3 has no written argument with a counterclaim, though grade 8 owns the full answer. Fix: add "an argument from an unseen opinion excerpt, with the counterclaim named and answered."

### 7. Respond days and unit assessment follow no shared rule
LAYER: frame. REPEAT: new. Confidence: judgment call.

- What is wrong: course check to respond day ratios run 1:1 (grades 1, 5, 6 to 8), 2:1 (grades 3, 4) and about 3:1 (World History I and II, US History I) with no reason given. Whether each unit's end-of-unit assessment and respond day sit inside its days is stated only in US History II, Government and Economics.
- Fix: one rule written into each frame's brief (settled below), and frames rebalance inside their day totals.

### 8. Time a day missing in six high school frames
LAYER: frame. REPEAT: yes (lesson 3). Confidence: firm.

- Files: world-history-i, world-history-ii, us-history-i, us-history-ii, us-government-and-politics, economics.
- Fix: add "one period a day of about 45 minutes, as grades 6 to 8". This is the minutes in a period, not the week or day pattern on Cory's card.

### 9. Since Time Immemorial worded three ways
LAYER: base text. REPEAT: new. Confidence: likely.

- Files: civics-government-and-civic-life, us-history-i, us-history-ii, us-government-and-politics frames.
- What is wrong: grade 8 and US History II treat it as a design-keeping term; US History I as a courtesy; Government names no unit at all (it may reuse US History I unit 1 Level 1 in the same year).
- Fix: once Cory answers the licence question already on his card, one identical wording in all four frames; Government names its unit. Not raised again here.

### 10. Status lines about other files remain
LAYER: frame, gate. REPEAT: yes (lesson 15). Confidence: firm.

- Files: K to grade 8 frames ("frames.csv agrees with this frame"); us-history-ii, us-government-and-politics, economics ("Done in frame-12-fixes").
- Fix: delete these lines. A gate check for them would stop the return.

### 11. Thread and model names vary
LAYER: frame. REPEAT: yes (lesson 6). Confidence: firm.

- What is wrong: "sourcing talk", "three sourcing questions", "sourcing step", "routine" and "five checks" name one thread; grade 7 calls the model "branches card".
- Fix: settled names below; grade 7 reads "the branches-of-government model".

## Settled by the expert

| Item | Choice | Why |
|---|---|---|
| Grade 3 Northeast nation case | The Penobscot Nation (or a Haudenosaunee nation), from the nation's own pages | Wampanoag already appears in K and grade 5 |
| Government founding documents | Retrieve Federalist 51 and Brutus No. 1; teach Federalist 10 as new, with Brutus No. 1 reread as its pair | Grade 8 taught 51 and Brutus 1 |
| Government default court pair | Betts v. Brady and Gideon v. Wainwright | Not met in an earlier grade; clean reversal |
| Respond-day rule | One respond day after each course-level check pair, plus one at year end; every unit's days include its end-of-unit assessment and one respond day | One rule across 15 frames |
| High school time a day | One period of about 45 minutes | Matches grades 6 to 8 |
| Sourcing thread names | "sourcing questions" up to grade 8; "five source checks" from grade 9 | One wording per band |
| Counterclaim name | "counterclaim" everywhere | One wording across grades |
| Grade 3 check 3 wording | As in finding 6 | Climbs above grade 2 |
| Grade 8 check 3 addition | As in finding 6 | Tests what grade 8 owns |
| Grade 4 informed action | Policy-trace proposal, retrieving grade 2 | Climbs rather than repeats |
| Grade 6 source list | 6 to 8 depth, without "authority" | Leaves the five checks to grade 9 |

## For Cory

Nothing new. The two items that touch him (the grade 11 timetable behind finding 4, and the Since Time Immemorial reading behind finding 9) are already on Desk card q-ss-frames-1.

## What is right

- K to grade 5 map, scale, latitude and timeline skills climb one step per grade.
- The claim climb from kindergarten to grade 2 is clear and testable.
- Model tables are consistent (branches-of-government in grades 3 to 5).
- Hard-history notes and the values rule are careful and age-fit.
- Christianity's retrieval from grade 6 to grade 7 to World History I is the pattern the other cases should copy.
- US History II's retrieval lines on the Depression and the Soviet collapse are well done.
- Economics' two-graph rule is clear.
- The gate passes with 0 social studies failures.

## What it could not judge

- Exact C3 indicator text: data/standards/c3-indicators.txt holds codes only, so the 6 to 8 against 9 to 12 wording in finding 5 is from memory.
- Check set editions and current availability of named primary sources.
- Whether the day totals still fit once the respond-day rule is applied (left to the frame writers).

## Sources

- data/standards/ma-hss-2018.txt (Massachusetts History and Social Science Framework, 2018).
- C3 Framework for Social Studies State Standards (2013), dimensions 1 to 4, codes as listed in data/standards/c3-indicators.txt.
- docs/agents/lenses/social-studies.md; docs/pipeline/briefs/frame-write.md lessons 3, 6, 11 and 15.

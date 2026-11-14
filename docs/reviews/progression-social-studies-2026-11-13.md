# Expert read: the social studies progression, K to 12 (2026-11-13)

Cold read by the curriculum expert. I did not write these rows. Lens: docs/agents/lenses/social-studies.md. Bar:
section 1 of docs/ADOPTION-BAR-SUBJECTS.md and docs/courses/social-studies/STANDARD.md (C3 for skills,
Massachusetts 2018 as content anchor, the values rule).

## What was read

| File | Rows | Notes |
|---|---|---|
| data/progressions/social-studies.csv | 384 | Every row, every column. By grade: K 19, 1 21, 2 18, 3 27, 4 17, 5 21, 6 29, 7 29, 8 27, 9 37, 10 43, 11 27, 12 69 (US History II 25, Government 19, Economics 25) |
| data/progressions/social-studies-excluded.csv | 10 | The shared Massachusetts 1.T4 and 2.T5 topic taught once, and MA.3.T6.2 taught in grade 5 |
| data/standards/ma-hss-2018.txt, data/standards/c3-indicators.txt | | Code lists the rows are checked against |
| data/courses.csv | | The nine social studies courses and their grades |
| C3 Framework PDF, revised 2017 (downloaded, text extracted) | 286 indicators parsed | Every C3 code in the rows (324 uses) checked against its wording |
| docs/reviews/: the three earlier social studies reads, the math 3 to 5 progression read, DIGEST.md, README.md | | For the REPEAT tags |

`python -X utf8 scripts/plan.py check` ran first: 0 failures. Its progression lines are 107 notes that a handoff
skips grades and about 40 that ask for the depth difference where a C3 code is named in two grades. I did not
re-check what the gate checks. Part drafts in data/progressions/parts/ were not read, as the brief said.

Mechanical checks of my own (scripts in the scratchpad, not in the repo): every Massachusetts standard is named
or excluded with a reason (child codes through a named parent); no code is unknown; every C3 indicator is named
by some row; every row names a standard; every `assumes` and `hands_on` pair is mirrored; no `model_in` comes
before the grade whose `model_out` introduces it; every `cross_subject` code exists and sits at or below the row's
grade.

## Verdict

The progression is sound and close to ready. Coverage is complete, chronology hands off cleanly (grade 7 ends
about 500 and grade 9 picks up there; US History I ends about 1920 and US History II starts in the 1920s), hard
history and Native nations are handled plainly and in the present tense, and the values rule is applied with
court rulings stated as decided. The biggest risk is the C3 economics placed inside grade 3 to 8 history and
civics rows: five of the seven C3 codes that do not fully match their skill are economics codes, and the grade 12
economics rows link back to none of that earlier work. The one change that matters most is finding 1's table plus
finding 4: fix the seven C3 placements and give the grade 12 economics rows real `assumes`.

## Findings, most serious first

### 1. Seven C3 codes do not fully match the skill their row teaches (moderate; firm)

LAYER progression. REPEAT yes (same kind as finding 5 of math-3-5-progression-2026-11-11.md: lines placed from
memory that the source does not bear out).

What is wrong. The writers placed C3 codes from memory. Checked against the indicator wording in the C3 PDF,
317 of 324 uses match the skill. One does not, and six match only in part. The wording below is the PDF's,
shortened.

| Row | Code | C3 says | The row teaches | Verdict | Fix |
|---|---|---|---|---|---|
| ss3-money-saving | D2.Eco.9.3-5 | the role of *other* financial institutions (the K-2 indicator is banks) | banks only | mismatch | Add one sentence: "Banks are not the only places that keep or lend money: a credit union is owned by its members, and an insurance company collects small payments to pay for big losses." Add `credit union` to words |
| ss5-independence-war | D2.Eco.11.3-5 | inflation, deflation and unemployment | inflation only | partial | Add: "After the war, hard money was scarce and prices fell (deflation), so farmers' debts grew heavier and work was hard to find." Add `deflation; unemployment` to words |
| ss6-phoenician-trade | D2.Eco.3.6-8 | buyers and sellers in product, labor and financial markets | product market only | partial | Add: "who worked the ships and dye works (paid workers and enslaved people), and how merchants pooled or borrowed money to pay for a voyage and shared the risk" |
| ss7-silk-road-trade | D2.Eco.4.6-8 | competition setting prices and wages | prices only | partial | Add "and why skilled caravan guides could ask high pay" to the competition sentence |
| ss7-silk-road-trade | D2.Eco.6.6-8 | supply and demand moving prices of goods, labor, credit and foreign currencies | goods only | partial | Add: "the same reasoning for how many coins of one land a trader got for coins of another" |
| ss8-public-budget | D2.Eco.11.6-8 | data on employment, unemployment, inflation, total production, income and growth | employment and growth only | partial | Add "inflation and total production (GDP) read from one chart of the state's economy" |
| ss3-globe-grid | D2.Geo.10.3-5 | why environmental characteristics vary among world regions | warmth by distance from the equator | partial, acceptable | No change needed. Optional: add rainfall (rainforest and desert at the same latitude) |

Not flagged after checking: ss7-south-asia-geo with D2.Geo.12.6-8 (population growth changing land use; it
matches). Every grade 9 to 12 code matches its row.

Why it matters. An adoption reviewer who maps the C3 codes finds the economics indicator claimed and not taught.
A teacher building the day has nothing to teach for the missing half.

### 2. Six `assumes` links point at an earlier topic, not at a prerequisite (moderate; firm unless marked)

LAYER progression. REPEAT yes (same kind as finding 2 of the math 3 to 5 read: a handoff to the wrong skill).

| Row | Now assumes | Why it is wrong | Fix |
|---|---|---|---|
| ss6-egypt-society | ss5-independence-war | The skill carried is reading royal art for the ruler's view (sourcing and perspective). The Revolution row teaches neither | `assumes` = ss5-sourcing-corroboration; drop ss6-egypt-society from ss5-independence-war's `hands_on`; add it to ss5-sourcing-corroboration's `hands_on` |
| ss8-amendments-civil-war | ss7-rome-fall; ss5-reconstruction-amendments | The fall of Rome is not a prerequisite for the constitutional causes of the Civil War. The row reads the secession declarations, which ss5-civil-war taught | Replace ss7-rome-fall with ss5-civil-war; add ss8-amendments-civil-war to ss5-civil-war's `hands_on` |
| ss6-phoenician-trade | ss5-new-england-industry | The row teaches barter to coins. Money was last taught in ss3-money-saving, which hands on nothing | Add ss3-money-saving to `assumes` (keep ss5-new-england-industry for specialization); note: "money last taught in grade 3; grades 4 and 5 carry no money content". ss3-money-saving gets `hands_on` ss6-phoenician-trade |
| us1-civil-war | wh2-colonial-culture; ss5-civil-war | wh2-colonial-culture's skill is how writers of empire shaped history. No reason is given in the notes and none is apparent | Drop wh2-colonial-culture from `assumes` (and us1-civil-war from its `hands_on`) |
| ss7-hinduism-caste | ss6-ancient-israel | Judgment call. Taken as "how a faith grows from its texts", it is a reasonable link, but the notes do not say so | Either add a note naming the skill carried, or point at ss6-christianity-origins or ss6-islam-origins if that is the skill meant |
| ss6-timeline-deep-time | ss5-revolution-causes | Judgment call. A timeline drawn to scale was taught in ss4-exploration; the grade 5 link is only "the last timeline" | Add ss4-exploration to `assumes`, with the note "timeline to scale, grade 4" |

Kept on purpose (see "Settled by the expert"): wh2-wwi-causes to us1-sectional-crisis (long-term causes against the
triggering event, D2.His.15) and wh1-renaissance to us1-revolution-war (significance judged over time, D2.His.3).
These carry a named skill across courses. They are not topic links.

### 3. Four skills are handed on to no one, though a later row builds on them (moderate; firm)

LAYER progression. REPEAT new.

- **ss3-deliberation** (D2.Civ.7, 9, 10 for grades 3 to 5) has no `hands_on`. Deliberation next appears in grade 8
  (ss8-civic-action, D2.Civ.9.6-8). Grades 6 and 7 carry only one D2.Civ code between them (ss6-hammurabi-code). Fix:
  ss5-informed-action `assumes` adds ss3-deliberation, because "decide by an agreed process" is deliberation. Judgment
  call: ss7-athenian-democracy also names D2.Civ.9.6-8 and runs one structured class deliberation on a real class
  question under assembly rules (a procedure, not a role play), so that the thread does not skip grades 6 and 7.
- **ss3-rules-rights** has no `hands_on`, yet its own notes say ss5-constitution deepens D2.Civ.3. Fix: ss5-constitution
  `assumes` adds ss3-rules-rights.
- **ss3-sea-trade** (the Triangular Trade) has no `hands_on`. ss5-slavery-colonies teaches the Atlantic trade and the
  Middle Passage. Fix: ss5-slavery-colonies `assumes` adds ss3-sea-trade.
- **ss5-slavery-expansion** has no `hands_on`, and **ss5-war-of-1812** has neither `assumes` nor `hands_on`. Its notes
  name a Tecumseh link to ss5-native-sovereignty-removal that is not in the columns. Fixes: us1-slavery-economy `assumes`
  adds ss5-slavery-expansion (the same 5 to 11 skip as ss5-civil-war to us1-civil-war, with the same reason).
  us1-westward-expansion `assumes` adds ss5-war-of-1812 (it covers the War of 1812). ss5-native-sovereignty-removal
  `assumes` adds ss5-war-of-1812, as its notes say.

### 4. Grade 12 economics links back to nothing, and two rows say supply and demand is "introduced" in grade 12 (moderate; firm)

LAYER progression. REPEAT new.

What is wrong. 14 of the 25 Economics rows and 5 of the 25 US History II rows have an empty `assumes`. For new
content (insurance, credit reports) that is honest. For the economic reasoning it is not. The supply-and-demand
graph is introduced in ss7-silk-road-trade (its notes say "Introduces the supply-and-demand graph") and used in
wh1-dutch-trade, wh2-industrial-revolution, wh2-great-depression, wh2-postwar-prosperity and wh2-globalization. Yet
econ-markets-prices says "with the graph introduced formally here", and us2-econ-toolkit says "Supply and demand is
introduced here and in Economics". A teacher reading those notes would re-teach from zero, and a day writer would
miss the grade 7 to 10 work students bring.

Fix (row edits):
- econ-markets-prices: `assumes` wh2-industrial-revolution. Notes: "the graph met in grades 7 to 10 is formalized
  here" in place of "introduced formally here".
- us2-econ-toolkit: notes "Supply and demand, met in grades 7 to 10, is reviewed here and in Economics, since a
  student may take either first."
- econ-macro-measures and econ-fiscal-monetary: `assumes` wh2-great-depression (unemployment, inflation, monetary
  policy, Keynes against the monetarists).
- econ-productivity-wages: `assumes` wh2-postwar-prosperity (productivity and living standards).
- econ-incentives and econ-saving-interest: `assumes` ss8-public-budget (interest rates on borrowing, D2.Eco.10.6-8).
- econ-systems-property: `assumes` the grade 10 row that teaches Soviet planning (wh2-totalitarian-regimes or
  wh2-soviet-collapse; the writer picks).
- us2-postwar-domestic: `assumes` wh2-industrial-cities (both carry D2.Geo.8.9-12; add the depth line).
- The personal finance rows (econ-spending-consumer, econ-credit, econ-borrowing-plan, econ-insurance-identity)
  may stay empty. Add the note "new content; no earlier skill".
- Mirror every `hands_on`.

### 5. Model gaps a teacher would feel (minor; firm)

LAYER progression. REPEAT new.

Gaps found: map-key (5, 7, 8), compass-directions (5), opportunity-cost (9 to 11), budget (2, 4 to 6, 9 to 11),
map-scale (8), region (8, 11), corroboration (4), latitude-longitude (8), branches-of-government (6, 10) and
supply-demand (8, 11). Most follow the course content (grade 8 is civics, with no maps) and are settled below.
Three need a fix:
- **corroboration at grade 4.** It is met in grade 2 and weighed in grade 5. Grade 4 has two source rows
  (ss4-primary-source, ss4-canada-mexico-research) and neither carries it. Fix: ss4-primary-source `model_in` and
  `model_out` add corroboration, with one task comparing two sources on the same landing or site.
- **supply-demand at grade 11.** wh2-industrial-revolution hands on to us1-industrialization and
  us1-market-revolution, and the railroad booms and the trusts are supply-and-demand cases. Fix: us1-industrialization
  `model_in` and `model_out` add supply-demand.
- **circular-flow.** It is introduced as econ-macro-measures' `model_out`, but that row's notes never teach it.
  econ-business-cycles describes it ("household, business and government spending"). Fix: add "the circular flow
  diagram of households, firms and government" to econ-macro-measures' notes.

### 6. One standard is split between two rows, but only one row names it (minor; firm)

LAYER progression. REPEAT new.

MA.WHI.T5.3 is named only on wh1-colonial-americas. Its transatlantic slave trade part is carried by
wh1-atlantic-slave-trade, which says so only in prose and whose `standard` column names D2.His.8.9-12 alone. The
gate cannot see the split, so a later edit to wh1-atlantic-slave-trade could lose the slave trade part without any
check failing. Fix: wh1-atlantic-slave-trade's `standard` adds MA.WHI.T5.3, and both rows' notes say which part each
owns.

### 7. cross_subject: two leans name the wrong skill, and five rows lean on nothing (minor; firm)

LAYER progression. REPEAT new.

- **ss7-time-zones** names science MS-ESS1-1, which covers lunar phases, eclipses and seasons. Time zones rest on
  Earth's rotation and day and night, which is 5-ESS1-2. Fix: `cross_subject` science:5-ESS1-2.
- **wh1-graphic-displays** names math 6.SP.B.4 (dot plots, histograms, box plots) for bar graphs. Scaled bar graphs
  are 3.MD.B.3. Fix: math:3.MD.B.3, or keep 6.SP.B.4 only if the row makes a histogram.
- No lean, though the row reads a graph or uses scale: wh2-total-war (production data: math:8.F.B.5),
  econ-price-controls (ceiling and floor on the graph: math:A-REI.D.11, as econ-markets-prices has),
  ss4-state-maps (scale distances: math:4.MD.A.2), wh2-imperialism-causes (data at two scales: math:6.SP.B.5) and
  econ-credit (APR and fees: math:7.RP.A.3). Add each.

### 8. Five C3 codes named in two grades carry no depth line (minor; firm)

LAYER process (the gate's notes ask for it). REPEAT new.

41 C3 codes are named in more than one grade. 36 say how the later grade goes deeper; these five do not:
D4.1.K-2 (ssk-i-think-because, ss2-claim-sources), D2.Geo.1.K-2 (ssk-local-maps, ss2-make-map), D2.His.1.K-2
(ssk-sequence-time, ss1-calendar-time), D2.Eco.15.9-12 and D2.Geo.11.9-12 (wh2-globalization, econ-global-economy).
Fix: one "Depth:" sentence on the later row of each pair. For example, on econ-global-economy: "Grade 12 measures
it (balance of payments, exchange rates); grade 10 described who gained and lost."

### 9. Stale and boilerplate notes (minor; firm)

LAYER progression. REPEAT yes (same kind as math finding 6: a pointer that no longer fits).

- ss6-mena-maps still says "Introduces latitude-longitude unless the grade 3 to 5 band already has (then this row
  carries it)". The band has it (ss3-globe-grid introduces it; grade 4 uses it with numbers). Fix: "Carries
  latitude-longitude from grades 3 and 4 into degrees with signs."
- The skip reason "the US founding returns in grade 8 civics" is pasted onto rows that are not about the founding:
  ss8-civic-action, ss8-civil-rights-laws, ss8-amendments-civil-war. Fix: "grade 8 is the civics year".

### 10. Pace and strand counts (minor; judgment call)

LAYER progression. REPEAT new.

Rows by strand, K to 12:

| Strand | K | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| civics | 6 | 7 | 1 | 7 | 1 | 5 | 0 | 1 | 19 | 3 | 2 | 0 | 19 |
| economics | 3 | 4 | 3 | 5 | 1 | 1 | 2 | 2 | 1 | 2 | 4 | 1 | 27 |
| geography | 4 | 4 | 7 | 4 | 7 | 1 | 6 | 5 | 0 | 3 | 1 | 0 | 0 |
| history | 4 | 3 | 4 | 8 | 6 | 12 | 17 | 20 | 3 | 24 | 33 | 22 | 22 |
| inquiry | 2 | 3 | 3 | 3 | 2 | 2 | 4 | 1 | 4 | 5 | 3 | 4 | 1 |

What follows from the table:
- **Grade 12 carries 69 rows, but across three courses.** The real question is per course: Economics (a half year)
  carries 25 rows, as many as the full-year US History II. That is about 3 to 4 days a row. It is workable, but the
  scope and sequence must budget it, so it is flagged now.
- **Grade 4 has 17 rows against 27 at grade 3 and 21 at grade 5.** The rows are wider, not fewer (ss4-states-and-statehood
  names six codes), so this is not a content gap. Watch it at the unit layer.
- **Civic dispositions skip grades 6 and 7.** They have one D2.Civ code between them. Finding 3 gives the fix.
- **Geography as a strand ends at grade 10**, but its reasoning goes on in history rows through C3 Geo codes
  (us1-westward-expansion, us2-depression, us2-postwar-domestic). That is acceptable, since Massachusetts has no
  high school geography course.

### 11. Words: one placement to watch (minor; judgment call)

LAYER progression. REPEAT new.

Words are taught before they are used, and K to 2 words suit the grade. One to watch: `sovereignty` in
ss3-first-nations-region (grade 3). Keep it, because it is the right word and grade 4 builds on it. Add to the notes:
"defined as a nation's right to govern itself; the class uses that phrase until the word is secure."

## The lens checklist, progression layer

| Line | Mark | Where |
|---|---|---|
| A C3 skill owned by no grade, or by two at the same depth | Missed in part | All C3 codes are owned; 5 of 41 repeats lack a depth line (finding 8) |
| A grade assumes a skill no earlier grade hands on | Missed in part | Handoffs missing or wrong in about 10 rows (findings 2, 3, 4) |
| Chronology breaks across grades with no stated reason | Met | Grade 7 ends about 500 and grade 9 picks up; grade 10 starts about 1800; US History I to about 1920, II from the 1920s; every skip has a reason |
| Geography or economics only as content, with no growing reasoning skill | Met for geography, missed in part for economics | Geography models run K to 12. The economics models run, but grade 12 does not link back (finding 4) and seven C3 placements are thin (finding 1) |
| Course frame: an anchor standard with no unit | Not applicable (no units yet) | At this layer every Massachusetts code is named or excluded with a reason |
| Course frame: grade 3 or grade 8 "your state" keeps Massachusetts-only content | Met | Grade 3 rows teach the student's own state and region, with Massachusetts as one worked example; grade 8 and Government do the same |
| Course frame: check-set additions recorded | Not applicable | Course frame layer |
| Sensitive topics carry a teacher note (rule 8) | Met at this layer | Slavery, removal, the Holocaust, genocide, internment, Nanjing, My Lai, the Lavender Scare: all carry notes, and no role play is allowed |
| Values rule (court rulings as decided; groups present where history includes them) | Met | Dobbs, Obergefell, SFFA, Shelby County and Korematsu are stated as decided; LGBTQ, disability and Native history are included |
| Native and hard-history content flagged for the sensitivity read | Not judged here | It belongs to the unit layer; the progression notes already name the cases |

## What is right and should not be touched

- Full coverage, with the exclusions explained in their own file.
- The chronology handoffs, and every skip reason tied to the Massachusetts course order.
- Hard history taught plainly from grade 3. The seceding states' own words are used against the "not about slavery"
  claim (values rule b), and Giza's paid builders are taught while slavery in Egypt is still named.
- Native nations in the present tense at grades 3, 4, 8 (tribal sovereignty), 9 (Taino descendants) and 12
  (gov-federalism's third sovereign).
- Informed action as the students' evidence-based choice, never a cause picked by the course, once a year.
- The grade 3 rewrite that teaches Massachusetts standards in general form.
- Grade 12 personal finance uses made-up offers and brands.

## What I could not judge

- The California, Tennessee and New York check set. This read covers the Massachusetts and C3 placements only.
- The final accuracy of Native and hard-history content. That needs the sensitivity read and the qualified person.
- Whether 25 Economics rows fit a half year. That needs the scope and sequence's day counts.
- Some history facts rest on memory, not on a source opened in this read: deflation in 1780s Massachusetts
  (finding 1's fix) and Phoenician labor. They are marked likely, and the day writer checks them.

## Settled by the expert

| Settled | Why | File |
|---|---|---|
| The far handoffs (grade 5 to 8, 5 to 11, 8 to 12; 55 in all) stay | They follow the Massachusetts course order, and each has a reason in its notes | social-studies.csv |
| Cross-course skill links wh2-wwi-causes to us1-sectional-crisis, and wh1-renaissance to us1-revolution-war, stay | Each carries a named C3 skill (D2.His.15, D2.His.3), not a topic | social-studies.csv |
| The model gaps map-key 5, 7, 8; compass 5; budget; map-scale 8; region 8, 11; lat-long 8; branches 6, 10; opportunity-cost 9 to 11 stay | They follow the course content (the grade 8 civics year; the world history years). Each model returns where it is next needed | social-studies.csv |
| ss3-globe-grid keeps D2.Geo.10.3-5; ss7-south-asia-geo keeps D2.Geo.12.6-8 | Each matches the indicator | social-studies.csv |
| production-possibilities and circular-flow first appear in grade 12 | C3 places them in the 9-12 Economics band; nothing earlier needs them | social-studies.csv |
| `sovereignty` stays a grade 3 word, with a defining phrase | It is the accurate word, and grade 4 builds on it | social-studies.csv |
| The C3 wording fixes in finding 1 and the row edits in findings 2 to 9 | Item-level edits inside the standards' limits | social-studies.csv |

## For Cory

The writers' eight picks, with my view on each:

1. **The shared K-2 economics topic taught once, at grade 1.** Agree. Massachusetts gives grades 1 and 2 the same
   topic. Teaching it twice wastes a unit, and grade 2 still carries C3 economics (three rows).
2. **"Your own state" in K-2, grade 8 and high school government.** Agree. It matches the grade 3 pattern and the
   earlier read's finding 3 (2026-11-12). The cost is that each unit needs worked examples from several states and
   links to each state's own pages. Massachusetts stays one example, never the subject.
3. **Grade 9 and 10 "one example" standards as a short survey with one example in depth.** Agree. The standard asks
   for one example studied. The survey keeps the chronology whole, and depth on one keeps it honest. Let teachers
   choose the in-depth example, as the rows already do.
4. **The grade 10 genocide anchor case.** wh2-genocide-atrocity now leaves any of about ten cases open. I agree that
   one case should anchor the built unit. My pick is Rwanda (1994), with Srebrenica as the second. Both have court
   findings of genocide (the Rwanda tribunal, and the ICJ and ICTY for Srebrenica), so values rule a settles the
   label. Several cases on the Massachusetts list (Northern Ireland, Kashmir, Shi'a and Sunni conflict) are mass
   violence, not legal genocide, and the row's first step ("tell genocide from other mass atrocity") keeps that
   straight. Students with family ties keep their choice of case.
5. **C3 economics placed in grades 3 to 8 inside history units.** Agree, on a condition. It is the right way to give
   economics a growing thread, but five of the seven weak C3 placements (finding 1) are these codes, so each needs a
   named activity, not only a code.
6. **Hard history added in grades 4 and 5.** Agree. It is age-suited as written (plain facts, enslaved people's own
   words, no simulations). It still needs the sensitivity read and the qualified person before any unit ships.
7. **Native nations as governments in grade 8.** Agree. C3 D2.Civ.1 names tribal institutions, and gov-federalism
   builds on it in grade 12.
8. **Economics in both US History II and Economics.** Agree, in part. MA.USII.T1 sits in that course, so the toolkit
   stays. But it is a review of grades 7 to 10, not an introduction (finding 4). Neither grade 12 course may assume
   the other, since students take them in either order.

One more for Cory, a scope point: Economics, a half-year course, carries as many rows as the full-year US History
II (finding 10). Either the course keeps 25 rows at about 3 to 4 days each, or some personal finance rows merge.
This is decided at the scope and sequence.

## Sources

- C3 Framework for Social Studies State Standards, NCSS, revised 2017:
  https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf. Every C3
  code's wording (finding 1, finding 8, For Cory 7).
- Massachusetts History and Social Science Framework 2018, as coded in data/standards/ma-hss-2018.txt. Ownership
  and coverage.
- NGSS (5-ESS1-2, MS-ESS1-1) and Common Core math (3.MD.B.3, 6.SP.B.4), from memory of the code meanings. Finding 7.
- From memory, not opened: the ICTR and ICJ genocide findings (For Cory 4); Massachusetts' 1780s money shortage
  (finding 1).

## For the source list

- The C3 Framework PDF (address above) is not in docs/APPROACH-SOURCES.md. It downloads directly with curl, and
  pymupdf extracts the indicator tables cleanly (286 codes). It is worth filing, with the note "indicator wording;
  NCSS terms apply, read and link only".

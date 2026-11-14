# Sequence fixes: World History I, World History II, US History I (grades 9 to 11), 2026-11-14

The fix pass for the two sequence reads of each course (the expert read, `sequence-<course>-2026-11-14.md`, and the Codex read, `sequence-<course>-codex-2026-11-14.md`), with the four settled rules of 2026-11-14 and each course's For the lead items. Files changed, for these three courses only: `docs/courses/<course>/scope-and-sequence.md`, `docs/courses/<course>/frame.md`, `data/plans/<course>/days.csv` and `source-map.csv`. Nothing else was edited; what other files need is under For the structure pass.

Gates after the pass: `sequence.py check` and `frame.py check` show 0 failures for each of the three courses; `plan.py check` shows 0 failures across all courses and progressions; `frame.py calendar` reports no break. No unit or day count changed, and no check moved off its calendar week.

## World History I

Expert read: 9 findings. Codex read: 12 findings. All 21 applied, 2 of them in part (reasons given).

| Finding | Applied? | File and what changed |
|---|---|---|
| Expert 1: grade 7 rows grade 8 never used open as retrieval | Applied (rule 1) | days.csv: readiness checks on days 1, 16, 31, 64 and 75 name every row last used two or more grades back; the days that use them (6, 17, 18, 19, 23, 37, 81) say "uses day N's readiness check". frame.md: the Seams paragraph states the rule; 14 Kind cells say "opens with a readiness check", and rows met earlier this year or used in grade 8 say why they open as retrieval. ss7-comparing-societies stays retrieval, against the expert: ss8-amendments-civil-war keeps it in use in grade 8, so it was used the year before. |
| Expert 2: MA.WHI.T4.3's Africa part on no day | Applied | days.csv day 69 (irrigation and crops through Egypt and North Africa into Spain, African rice and sorghum in the inner Niger delta, Champa rice) and day 71; frame.md unit 4 cell. |
| Expert 3: unit 10 argument due in ELA 9's week 30 | Applied | days.csv day 150 (final copies stay in class), day 153 (hand-in, week 31); frame.md stagger line. |
| Expert 4: year-end check repeats unit 10's assessment | Applied (rule 3) | days.csv day 154 scores the argument handed in and asks no new argument; day 157's document set is drawn from units 1 to 9; scope-and-sequence.md year-end paragraph. |
| Expert 5: units 6 and 7 questions half the unit does not feed | Applied | frame.md unit 6 and 7 questions (the expert's wording); days.csv days 87 and 107 answer from every strand. |
| Expert 6: day 129 holds two lessons | Applied | days.csv days 129 and 130 split method and instruments from the sun-centred universe. |
| Expert 7: one day to find a public telling | Applied | days.csv day 138 note starts the search, day 151 brings it, with a printed bank. |
| Expert 8: source map order and own days | Applied | source-map.csv: order_conflict filled for the out-of-order chapters; "ours" rows for 7.2, 7.3, 8.4, 10.1, 10.4, 10.5, 10.6; sorted by section. |
| Expert 9: stale lines | Applied | days.csv days 52, 95 (base named), 141. |
| Codex 1: three anchor parts absent | Applied in part | days.csv days 54 (struggles within the Church), 69 and 71 (T4.3), 112 and 124 (Portugal's wars with Muslim states); frame.md units 3, 4, 8. Not applied: Codex's T4.3 wording that leaves Champa rice out; the expert's version keeps it (MA.WHI.T4.3 names Asia, and Champa rice is its clearest case). The own-word standard lines go to the structure pass. |
| Codex 2: C3 performances reduced | Applied | days.csv days 4, 13, 118, 123. |
| Codex 3: assessment descriptions permit incomplete evidence | Applied (rule 4) | days.csv blueprints on days 14, 29, 45, 62, 73, 88, 108, 124, 136, 154 and checks 47, 48, 90 to 92, 156, 157. |
| Codex 4: paper route and the technology part of D2.Geo.1 | Applied | days.csv day 10 note (offline mapping tool page, supplied data, no account); frame.md paper path. Progression row to the structure pass. |
| Codex 5: Axum conflated with Great Zimbabwe | Applied | days.csv day 34. |
| Codex 6: capstone collides with ELA | Applied (expert's day) | Hand-in on day 153, week 31 (expert 3), not Codex's alternative: day 153 is the first history day clear of ELA 9's week 30. |
| Codex 7: overloaded days | Applied | days.csv days 24, 27, 53, 56, 129, 130, 133, 135, 149. |
| Codex 8: source map marks a used passage cut | Applied in part | source-map.csv: chapter 8's Russia passage gets its own row (day 141); order reasons filled. Not applied: page ranges for every section; the unit plans bound each excerpt, and only the chapter 8 passage was ambiguous. |
| Codex 9: action cycle presumes a correction | Applied | days.csv day 152 (correction, contextual addition, or confirmation with its evidence); frame.md informed action. |
| Codex 10: compelling questions do not organize their units | Applied (expert's wording) | frame.md units 6 and 7; the expert's and Codex's fixes agree in aim. |
| Codex 11: shorter path absent | Applied | scope-and-sequence.md new Shorter path (45-minute route; about 154 days folding 2, 25, 44, 105, 127, 134, 160). |
| Codex 12: unresolved candidate, stale descriptions | Applied | Goryeo dropped with its reason (day 53, frame.md unit 3); Tokugawa and Qing limits on day 135. |
| For the lead 1 (L8 thin topics) | To the structure pass | data/modules.csv and later.csv are not this course's files. |
| For the lead 2 | Nothing needed | |
| For the lead 3 | Accepted | Chapter 8 has its own source-map row. |

## World History II

Expert read: 7 findings. Codex read: 8 findings. All 15 applied, 2 of them in part.

| Finding | Applied? | File and what changed |
|---|---|---|
| Expert 1: day 114 drops the cause T5.7d names | Applied | days.csv day 114 (the Arab states' rejection and invasion; Palestinians' loss of land and homes through expulsion by Israeli forces and flight from the fighting; Jewish refugees from Arab countries); scope-and-sequence.md unit 8 topics. |
| Expert 2: a genocide among four topics on day 32 | Applied | days.csv day 32 keeps African states, Berlin and the Congo; day 36 adds Adwa and the Herero and Nama rising and genocide, with its sensitivity note and base (ETSU ch. 10); day 29 names its base. |
| Expert 3: no day to act or look back | Applied | days.csv day 153 (compare efforts across time and place; retrieval of ss8-civic-action, used in grade 9), day 154 (decide, take the action through an adult or record a reasoned choice not to act; D4.7, D4.6), day 157 (look back); frame.md informed action bullet. |
| Expert 4: check 1 repeats unit 3's map task | Applied (rule 3) | days.csv day 38 drops D2.Geo.3; day 41 tests the two-scale map once on unit 1 and 2 content; frame.md check row; scope-and-sequence.md. |
| Expert 5: day 117 leans on grade 5 and 8 rows with no readiness check | Applied (rule 1) | days.csv day 108 is a readiness check (ss8-civil-rights-laws, ss5-civil-rights-movements, not used in grade 9), with a Salt March line on the survey pages; day 117 uses it; frame.md Days and Seams; scope-and-sequence.md. |
| Expert 6: one research launch day for a school alone | Applied | days.csv days 146 and 147 double as research time; day 145 a bounded search. |
| Expert 7: source map order and own days | Applied | source-map.csv: 13 order_conflict reasons; Napoleon (pages 69 to 72) on day 6; etsu-15-power split over days 130 and 131; "ours" rows for every unit day with no base passage, sorted. |
| Codex 1: content lost between progression and goals | Applied | days.csv days 11, 22, 27, 46, 60, 63 (with T4.7), 68, 70, 76, 77, 82, 142. |
| Codex 2: assessments do not secure all owned learning | Applied (rule 4) | Blueprints on days 14, 25, 38, 57, 71, 87, 106, 120, 132, 143, 155 (a composite with the research product); checks 40, 41, 89 to 91, 158, 159. |
| Codex 3: capstone research not located | Applied | days.csv day 145 (modelled search, then a bounded printed archive, at least five sources, primary and interpretive), 150 (modelled talk), 152 (groups of four); frame.md paper path; scope-and-sequence.md unit 11 arc. |
| Codex 4: false common cause for dictatorship | Applied | scope-and-sequence.md unit 5 arc (dated routes; the Depression helped the Nazi rise; Britain as the surviving democracy). |
| Codex 5: C3 performances narrower than codes | Applied | days.csv days 1, 12, 55 (D3.2), 85 (D2.Civ.10 case), 127, 146 (migration and settlement), 147; frame.md unit 11. |
| Codex 6: two power standards on one day | Applied | days.csv day 126 answers the compelling question; day 130 European populism (T6.3); day 131 China (T6.4); scope-and-sequence.md unit 9 arc. The expert was silent; the split costs no day. |
| Codex 7: departures from textbook order | Applied in part | As expert 7. Not applied: page ranges for every section (given for Napoleon only, the one passage split across days). |
| Codex 8: contradictions and pacing | Applied in part | scope-and-sequence.md: Shorter path (45-minute route; about 154 days folding 12, 17, 24, 67, 105, 119), Tanzimat and Gandhi candidate rows, calendar paragraph; frame.md For the lead 2 settled. Not applied here: the literacy-status lines in STANDARD.md and the adoption bar, and the lens lines on a qualified reader (structure pass). |
| For the lead 1 | Answered, no frame change | Days 146 and 147 double as research time; day 145 teaches a bounded search; unit 10's survey day stays (both reads agree). |
| For the lead 2 | Accepted | |
| For the lead 3 | To the structure pass | data/modules.csv. |
| For the lead 4 | Nothing needed | |

Where the reads differ: expert 5 (readiness on day 108) over Codex's "no readiness needed", by settled rule 1; expert 4 and Codex 2 reconciled so D2.Geo.3 is tested once (day 41) on earlier content. The research product shared with ELA 10 is unchanged on the ELA side; no ELA 10 frame change is needed.

## US History I

Expert read: 8 findings. Codex read: 9 findings. All 17 applied, 4 of them in part.

| Finding | Applied? | File and what changed |
|---|---|---|
| Expert 1: the action is decided but never taken or looked back on | Applied, with Codex 6 | days.csv day 126 note (each student notes a local problem: the start of the action), day 136 (investigate and compare the options), day 137 (decide, then take the action through an adult or record a reasoned choice not to act), day 160 note (look back; in a Government year, the look-back follows Government's action); frame.md informed action bullet and unit 8 cell; scope-and-sequence.md unit 8 arc. |
| Expert 2: essay 2 needs feedback overnight | Applied | days.csv days 88 to 92 reordered: 88 draft 1 (5.3); 89 the end-of-unit assessment; 90 its respond day; 91 draft 2; 92 draft 3, final (5.4). Codes travelled with their days. scope-and-sequence.md unit 5 arc and assessment line. |
| Expert 3: day 1 leaves out two rows; unit 8 names no retrieval | Applied (rule 1) | days.csv day 1 (goal names grade 8's news literacy and grade 9's significance judgment; note names ss8-news-literacy and wh1-renaissance, last used grade 9), day 4 (retrieval of ss8-news-literacy), day 16 (keeps its worked example), day 123 (retrieval of wh2-industrial-ideas-reform, met on day 55); day 144 unchanged; frame.md Days bullet, Seams paragraph and Kind cells. |
| Expert 4: two checks repeat the assessments before them | Applied in part (rule 3) | days.csv day 89 (was 91) asks how and why Reconstruction ended (D4.2); day 154 tests news against opinion on an unseen 1898-style pair and drops NML.T4.2, which moves to day 158. Departure: day 94's cause against trigger argument is on why the colonies declared independence, not why war came. Rule 3 asks the check's items for unit 5's skills to draw content from earlier units, and essay 1 already argued why war came in three drafts. |
| Expert 5: days 20, 54 and 107 overloaded | Applied, with Codex 4 | days.csv: the Northwest Ordinance moves to day 21 beside Shays' Rebellion; day 54 keeps immigration and nativism; the Second Great Awakening and Republican Motherhood open day 55 (T4.1 on days 54 and 55); the question set is read on day 56; day 107's Chinese and Mexican American West goes to the survey pages. Candidate table and unit 2, 4, 6 lines in scope-and-sequence.md. |
| Expert 6: the Red Summer has a home here | Applied | days.csv day 135 (the Red Summer of 1919 that met the Great Migration; violence named plainly), day 151 note drops the dropped-candidate line; frame.md units 8 and 9; scope-and-sequence.md unit 8 and 9 candidates, table, For the lead 1 closed. No US History II change. |
| Expert 7: a school alone gives every talk on day 69 | Applied | days.csv day 69 goal and note (the paper is handed in; history scores the paper only; the talk is ELA's). |
| Expert 8: stale "idle" notes | Applied | days.csv days 1, 20, 35, 51, 72, 97, 123 say "last used grade N" (ss5-revolution-causes and ss5-civil-war grade 8, ss5-republic-growth grade 6, the other grade 5 rows grade 5, the grade 8 rows grade 8); scope-and-sequence.md readiness paragraph. |
| Codex 1: assessments do not secure every owned performance | Applied in part (rule 4) | days.csv blueprints on days 18 (adds T1.1 and the D1 codes; the inquiry proposal and source rationale scored as components), 33, 46, 70 (common survey questions on each reform strand; each part of T3.2 and T4.2), 89 (the essays as components for D2.His.16, D3.3, D3.4, D4.1), 108, 121, 138, 154; checks 48, 49, 93 to 95, 156 to 158. Departure: day 154 carries NML.T4.3 but not T4.1; a site's sponsor (T4.1) and credibility methods (T4.2) are tested once, on day 158, on earlier content, so the check does not repeat the unit assessment (expert 4, rule 3). |
| Codex 2: unit 1 inquiry depth | Applied | days.csv day 2 (two scholarly interpretations compared), 3 (supporting questions tied to them, source types justified), 4 (an accessible expert appraisal; printed on the paper path), 13 (date, place, audience; how analysis changes the question). |
| Codex 3: the slavery comparison lost | Applied in part | days.csv day 58 (a short map and evidence table on the Southern states, the Caribbean and Brazil), day 70 blueprint, days 93 and 156; frame.md unit 4. The standard line and the progression row go to the structure pass. |
| Codex 4: the reform survey overloaded | Applied, with expert 5 | days.csv day 55 (abolition; women's rights with Seneca Falls, its ties to abolition and wider schooling; Mann's schools, literacy and print), day 56 (disability schools and asylums; the Transcendentalists' themes; then the question), day 61 (completes the source plan); temperance and prison reform as brief connected examples; frame.md unit 4; scope-and-sequence.md unit 4. The T4.2e paraphrase goes to the structure pass. |
| Codex 5: early republic foreign policy and the transfer of power | Applied | days.csv day 29 (neutrality and the Jay Treaty), day 30 (Codex's wording on 1800 and 1801, with 1797 named in the note), day 33 blueprint; frame.md unit 2; scope-and-sequence.md unit 2. |
| Codex 6: the action stops at deciding; Government substitution undefined | Applied | As expert 1: in a Government year, days 136 and 137 revisit Government's action, compare it with Progressive-era responses and evaluate the outcome. |
| Codex 7: shorter path absent | Applied | scope-and-sequence.md new Shorter path (45-minute route; about 155 days folding 8, 27, 44, 115, 119). |
| Codex 8: candidate cell partly settled | Applied | frame.md unit 7 and scope-and-sequence.md: machines kept within day 113; a separate party-system treatment dropped. |
| Codex 9: status notes contradict the plan | Applied in part | scope-and-sequence.md For the lead 3: day 25 keeps the bounded Level 1 Boldt case. Not applied: putting the Red Summer under For Cory; the band note settles it in this course (expert 6), so no scope question is left. The literacy-status corrections go to the structure pass. |
| For the lead 1 (Red Summer) | Closed | Day 135. |
| For the lead 2 | Accepted | |
| For the lead 3 (Boldt) | Rewritten | As Codex 9. |

Check placement under rule 3: check 1 (days 48 and 49) asks units 1 and 2, with unit 3's map skill on a unit 1 or 2 map; the mid-year check (93 to 95) asks units 1 to 4, with unit 5's cause against trigger argument and critique on earlier content; the year-end check (156 to 158) asks units 1 to 8. The source map needed no change: no day holding a Since Time Immemorial passage moved, and the moved content (days 20, 21, 54 to 56, 88 to 92, 107) has no base. The reform paper shared with ELA 11 changed on the history side only (day 69's note); no ELA 11 frame change is needed.

## Settled

| Course | Choice | Reason | Files |
|---|---|---|---|
| All three | Readiness check for every earlier-grade row last used two or more grades back; retrieval for the year before or earlier this year | Settled rule 1 | days.csv, frame.md Seams, scope-and-sequence.md |
| All three | End-of-unit and check goals name each part of each listed code; sustained products are named components | Settled rule 4; Codex read 1 to 3 | days.csv |
| All three | Each check draws content for the just-assessed unit's skills from earlier units | Settled rule 3 | days.csv, frame.md checks, scope-and-sequence.md |
| All three | Shorter path: a 45-minute route and about 154 or 155 days, folding days whose codes are taught elsewhere | Adoption bar C2 | scope-and-sequence.md |
| World History I | ss7-comparing-societies opens as retrieval | Kept in use in grade 8 by ss8-amendments-civil-war | days.csv day 1, frame.md |
| World History I | Champa rice stays in T4.3 | MA.WHI.T4.3 names Asia | days.csv day 69 |
| World History I | Unit 10 argument handed in day 153 (week 31); day 154 scores it, no new argument | ELA 9's week 30; rule 3 | days.csv days 150, 153, 154 |
| World History II | Day 108 readiness on the grade 5 and 8 civil rights rows | Rule 1 | days.csv days 108, 117 |
| World History II | Populism (day 130) and China (day 131) each get a day | Two power standards | days.csv |
| World History II | The two-scale map tested once, day 41, on unit 1 and 2 content | Rule 3 | days.csv days 38, 41 |
| US History I | Essay 2 order: draft 1, assessment, respond, draft 2, draft 3 (days 88 to 92) | Feedback needs time | days.csv |
| US History I | Red Summer on day 135 | A home inside the course's dates | days.csv, frame.md, scope-and-sequence.md |
| US History I | Day 94's cause against trigger argument on independence, not on why war came | Rule 3; essay 1 argued why war came | days.csv day 94 |
| US History I | NML.T4.1 and T4.2 tested once, day 158; day 154 tests T1.5 and T4.3 | Rule 3, expert 4 with Codex 1 | days.csv days 154, 158 |
| US History I | The action is taken on day 137 and looked back on day 160; in a Government year, days 136 and 137 evaluate Government's action | Bar item 8 | days.csv, frame.md |

## For the structure pass

Exact edits in files this pass does not own.

**data/standards/ma-hss-2018.txt**

1. Line 682, MA.WHI.T5.1: old "the rise of Spain and Portugal, the Spanish Inquisition," new "the rise of Spain and Portugal (with Portugal's conflicts with Muslim states), the Spanish Inquisition,".
2. Line 665, MA.WHI.T3.7: old "growing wealth and power struggles in the 11th century," new "growing wealth and its power struggles in the 11th century, within the Church and with kings,".
3. Line 485, MA.USI.T3.3: old "explain why it grew rapidly after 1800, and analyze how banks and insurers profited from it." New "explain why it grew rapidly after 1800 in the Southern states, the Caribbean islands and South America, and analyze how banks and insurers profited from it."
4. Line 494, MA.USI.T4.2e: old "and its themes of liberty, nature, self-reliance and civil disobedience." New "and its themes of liberty, nature, self-reliance, civil disobedience, materialism and abolitionism." (the official list, per the Codex read).

**data/progressions/social-studies.csv**

5. Row wh1-graphic-displays (line 212): "(a free online mapping tool with layers)" becomes "(an offline mapping tool page with supplied data and no account)".
6. Row wh1-european-kingdoms (line 225): "its 11th century struggles with kings over who appoints bishops" becomes "its 11th century struggles within the Church and with kings over who appoints bishops".
7. Row wh1-iberia-1492 (line 237): old "the Spanish Inquisition, and expeditions to conquer" new "the Spanish Inquisition, Portugal's wars with Muslim states in North Africa and the Indian Ocean, and expeditions to conquer".
8. Row wh1-historical-argument (line 246): old "and if they find it wrong or incomplete, choose whether to propose a correction to its keeper." new "and decide what the evidence supports (a correction, a contextual addition, or a confirmation with its evidence) and whether to send it to its keeper."
9. Rows wh1-geography-shapes-contact, wh1-belief-systems, wh1-religions-spread, wh1-silk-roads-mongols, wh1-classical-learning, wh1-slavery-across-world: in each Handoff kind for a grade 6 or grade 7 row not used in grade 8, "opens with a short retrieval task" becomes "opens its unit with a readiness check".
10. Row wh2-social-movements (line 281): assumes, empty, becomes "ss5-civil-rights-movements; ss8-civil-rights-laws" (handed off as a readiness check).
11. Rows us1-revolution-causes (291), us1-declaration (292, the ss8-declaration handoff), us1-articles-constitution (294, ss8-articles-convention and ss8-ratification-debate), us1-press-history (295), us1-early-republic (296), us1-jackson-removal (297), us1-westward-expansion (298, the ss5 handoffs), us1-slavery-economy (300, ss5-slavery-expansion), us1-reform-movements (302), us1-civil-war (304), us1-reconstruction (305), us1-jim-crow (306), us1-women-work-suffrage (310): in each Handoff kind from a grade 5 or grade 8 row, "opens with a short retrieval task" becomes "opens its unit with a readiness check". The World History I handoffs in the same rows, and rows us1-native-west (309) and us1-civil-rights-1900s (312), stay retrieval (used in grade 10, or met earlier this year).
12. Row us1-revolution-war (line 293): "the unit opens with a worked example of the skill, not a reteach of the Renaissance" becomes "unit 1 opens with a readiness check on it (last used in grade 9), and day 16 uses a worked example of the skill, not a reteach of the Renaissance".
13. Row us1-news-reading (line 314): "is a maintained skill, kept in use between by wh1-sources-of-the-past and wh2-historians-interpretations" becomes "was last used in grade 9 (wh1-sources-of-the-past), so it joins US History I's day 1 readiness check and is retrieved on days 4 and 144".
14. Row us1-early-republic (line 296): "the 1800 election as the first peaceful handover between parties" becomes "the election of 1800 and the first peaceful transfer of the presidency between rival political parties (1801)".
15. Row us1-slavery-economy (line 300): after "Slavery's place in the industrial North as well as the South." add "Its growth compared with plantation slavery in the Caribbean and Brazil."
16. Row us1-reform-movements (line 302): "Students pick one; the class shares findings so each reform is met." becomes "Every reform is surveyed over two days (after the Awakenings and Republican Motherhood), then students pick one and investigate its whole lettered part." and "the Transcendentalists (Emerson, Thoreau, Fuller) and civil disobedience" adds "with their themes of liberty, nature, self-reliance, materialism and abolitionism".
17. Row us1-progressivism (line 311): "decide an action (a fact-checked report or letter to a local official or newspaper) and share it through a safe public route" becomes "decide, then take the action through an adult (a fact-checked report or letter to a local official or newspaper) or record a reasoned choice not to act, and look back on it at the year's end; when Government runs the same year, its action is the year's action and these days evaluate it".

**Other files**

18. Run `python -X utf8 scripts/frame.py sync` for world-history-i (unit 6 and 7 questions and the unit 6 dates changed in frame.md).
19. data/modules.csv: the ten World History I topic pages (World History I For the lead 1); two World History II topics, "Genocide and Terror Since 1945" (unit 10) and "Global Problems Research" (unit 11), beside the world-hist-2 rows at lines 721 to 729 and 793.
20. data/plans/later.csv: mark L8 (thin topics) as named, with the World History I topic list.
21. docs/courses/social-studies/STANDARD.md line 25: "Not loaded: pre-kindergarten; the seven practice standards (C3 carries the skills); the literacy standards." becomes "Not loaded: pre-kindergarten; the seven practice standards (C3 carries the skills). The literacy standards (RH, WHST) are loaded in data/standards/ccss-literacy-6-12.txt as also-met codes, placed per course." (World History II and US History I Codex reads.)
22. docs/ADOPTION-BAR-SUBJECTS.md lines 194 to 196: the sentence saying the literacy standards are not in the ELA records and loading them is open becomes "its literacy standards (RH, WHST) are loaded in data/standards/ccss-literacy-6-12.txt; placing them per course is the remaining work".
23. docs/agents/lenses/social-studies.md line 46 ("needs a qualified person's read (FOUNDATION section 7)") and line 91 ("(the sensitivity read and the qualified person)"): reconcile with FOUNDATION 7.3 as revised 2026-11-14 (an agent read; no outside human reader).
24. ELA frames: no change needed for ELA 9, ELA 10 or ELA 11.

## For Cory

None. The Red Summer is settled inside US History I (day 135), so no course's scope changes.

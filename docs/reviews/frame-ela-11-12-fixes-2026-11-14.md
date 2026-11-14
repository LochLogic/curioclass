# Fixes: ELA course frames, grades 11 and 12, after the two cold reads (2026-11-14)

Applies the expert reads (`frame-english-language-arts-grade-<n>-2026-11-14.md`) and the Codex reads
(`frame-english-language-arts-grade-<n>-codex-2026-11-14.md`) for grades 11 and 12 to the two frames and
`data/progressions/ela.csv` (20 rows, notes and one words cell). Every expert finding and every "Settled by the
expert" row is applied; each Codex finding was weighed on its merits; the writers' "For the lead" items were applied
where they were item-level and rewritten as settled.

Gates after the fixes: `scripts/frame.py sync` (52 courses); `scripts/frame.py check english-language-arts-grade-11
english-language-arts-grade-12` 0 failures each; `scripts/progression.py check ela` 374 rows, 0 failures (also as run
inside `scripts/plan.py check`, which exits 0); `scripts/stale.py check` 56 files, 0 failures. Both courses keep their
unit counts and totals (grade 11: 9 units, 160 days, 148 in units; grade 12: 8 units, 160 days, 149 in units). No skill
moved between units. Days moved inside each course, named below. The grade 10 frame was not edited: no grade 10 to 11
handoff changed, so its Seams table still holds.

Wording rule applied in both frames: no trademarked measure or brand name. "Lexile" became "a quantitative reading
level of about ..."; "CommonLit is not used" became "No commercial text collection is used". Where the expert named
non-government services, the frames name them generically and this report names them for unit writers: the
"public-domain volunteer dramatic reading with a cast" of Trifles and the "full-cast audio recording" of Hamlet are the
LibriVox recordings; the "free online etymology dictionary" is the Online Etymology Dictionary; the "free full-view
archives of public-domain books" are HathiTrust full view and the Internet Archive. Government archives (the Library of
Congress, Chronicling America) and the MLA core-elements format (the grade 9 to 12 thread) are named as before.

## Grade 11

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | Unit 3 adds Wheatley's 'On Being Brought from Africa to America' (1773) and Occom's 'A Short Narrative of My Life' (1768), about 2,000 words; unit 6's RL.11-12.9 cell compares them on faith and how each writer is treated, Winthrop against Hawthorne kept; e11-lit-american-periods notes name them. Unit 3 21 days |
| Expert | 2 | Applied | Paper path bullet: open archives only, a school's databases an extra; unit 4 "a full-text archive search" and the Curio Class style sheet with the GPO Style Manual "as in grades 9 and 10"; a new "References" bullet (Webster's 1828, an etymology dictionary, Fowler 1926 beside a free dictionary's usage notes, the style sheet); units 1 and 3 name them; e11-word-strategies, e11-usage-conventions and e11-research notes name them |
| Expert | 3 | Applied, merged with Codex 4 | Unit 4 20 to 23 days, unit 7 13 to 10, unit 1 17 to 16 (unit 3's day). Shared window weeks 12 to 15 everywhere. Beyond the expert's fix: check 1 sat in week 12 and split the window, so it moves after unit 4 (weeks 16 to 17); unit 4 is short project days 56 to 58, sustained project to day 75 (end of week 15), its own assessment and respond in week 16; milestones the same in both courses (question week 12, sources week 13, draft week 14, essay and talk week 15). To keep Douglass out of US History I's weeks 20 to 22, unit 5 goes 15 to 14 days (weeks 17 to 19) and unit 6 20 to 21; check 2 moves after unit 6 (week 24). Checks now weeks 16 to 17, 24, 32 |
| Expert | 4 | Applied, merged with Codex 2 | Paper path bullet: W.11-12.6 and SL.11-12.5 on a shared device or lab session, teacher posts, no account; the paper path leaves those parts recorded unfinished, as in grade 10. Unit 2 publishes and updates that way, unit 4 uses digital media strategically; e11-process and e11-presentation notes carry the boundary |
| Expert | 5 | Applied | Calendar: none due in weeks 12 to 19 except the shared research piece, none in week 31; narrative due end of week 30, week 31 holds the interpretations lessons and the assessment; literary argument about week 23 |
| Expert | 6 | Applied | Unit 3 names Apess, 'An Indian's Looking-Glass for the White Man' (1833), an excerpt of about 1,500 words; shelf adds Sui Sin Far, Mrs. Spring Fragrance (1912), and Ruiz de Burton, The Squatter and the Don (1885). Further pick of mine: unit 8 sets an excerpt of Sui Sin Far's 'Leaves from the Mental Portfolio of an Eurasian' (1909) beside Riis's Chinatown chapter, an insider account in the source set. A "Who wrote the texts" bullet |
| Expert | 7 | Applied | Sensitivity line and unit 8: a reader from the communities Riis describes (Jewish, Chinese, Italian American) |
| Expert | 8 | Applied, merged with Codex 8 | Unit 9 "Inside the marriage, 1892 to 1916: Chopin, Gilman and Glaspell, with a satire pair"; question "What do these three writers show about a wife's life that the men around her do not see?"; what each text adds to the topic; the narrative tied to it; Franklin and Twain kept as a short satire pair beside history's war weeks |
| Expert | 9 | Applied | citation first used in unit 2 (style sheet retrieved), again in 3, 4, 6, 9; the grade 10 seam row says so |
| Expert | 10 | Applied | Unit 1 and e11-seminar: students choose roles from a named set or make their own and set the goal and deadline (SL.11-12.1b started); e12-seminar notes rewritten (below) |
| Expert | 11 | Applied | The Age of Innocence off the grade 11 shelf (grade 12 keeps it) |
| Expert | settled | Applied | All six rows: the Wheatley and Occom pair; Apess; Trifles' two versions (the volunteer cast reading and a live in-class staging, school production where one exists); the references; narrative end of week 30; the shelf |
| Codex | 1 | Applied | Unit 3 uses US History I's wording (analyse the grievance without printing the slur or requiring students to speak it, with Native-authored accounts, now Apess and Occom); units 5 and 8 and the brief: slurs left out with an omission mark and an editor's note, editions otherwise complete and every omission disclosed |
| Codex | 2 | Applied | With expert 4 |
| Codex | 3 | Applied | Final check: a cold read in the 11-CCR band with documented scaffolding as needed at the high end; supports keep the reading being assessed; supported proficiency recorded, an optional independent read recorded apart as an extension and a grade 12 readiness note. Not in conflict with the expert, who did not read the check |
| Codex | 4 | Applied | With expert 3 |
| Codex | 5 | Applied | Unit 9 and e11-lit-author-choices: Minnie Wright offstage, the action in her kitchen, the men leave and return while the women read the domestic evidence; "the men offstage" removed |
| Codex | 6 | Applied | Unit 3 and the two rows: one premise and its reasoning judged with evidence (RI.11-12.8); each document's theme stated and traced, ending in a two-document theme synthesis (RI.11-12.9); both named in the unit's assessment brief |
| Codex | 7 | Applied in part | Applied: the "standard's own demand" claim replaced ("course selections that serve the historical-literature requirements"); the print-copy claim made a rule (a checked copy before the unit is planned, the text record lists what is on file); open picks named (Mather's Bridget Bishop account, six Dickinson poems from the 1890s editions, the 1890 census table). Rejected: writing the full inventory before the frame is fixed. The frame-write brief puts the course text record with the scope and sequence and the first pilot plan; the frame names every pick and its reason |
| Codex | 8 | Applied | With expert 8. Readers conflict on who decides Franklin and Twain: no anchor is removed, they stay as named satire texts, so it is an item-level framing, not a scope change for Cory |
| Codex | 9 | Not acted on here | The grade 10 frame's Chemistry line is in its Cross-subject section, outside the Seams table this pass may edit: under Cross-subject notes |
| Codex | 10 | Not acted on here | Earlier review files: under For the lead |
| Codex | 11 | Not acted on here | `frame-us-history-i-codex-2026-11-13.md`: under For the lead |
| Codex | settled | Applied | All but the inventory-before-fixing row (Codex 7) and the review-file rows (Codex 10, 11) |
| Writer | lead 1 | Applied | Rewritten as settled with the new days |
| Writer | lead 2 | Applied | The seminar row change, with the expert's refinement |
| Writer | lead 3, 4 | Kept | Second Inaugural in unit 3 (grade 12 rereads it for a new task); the recent-texts rule worded without the mandate claim |
| Writer | lead 5 | Applied | Recordings settled by the expert's versions; a volunteer recording optional |
| Writer | lead 6, 7 | For Cory | Check set; people |

Counts: applied 19 (expert 1 to 11, Codex 1 to 8, Codex 7 in part), rejected 1 (Codex 7's inventory timing), not acted
on 3 (Codex 9 to 11, outside this pass), for Cory 3.

## Grade 12

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | Unit 1: Twain's 'Two Views of the Mississippi' (1883) and Addams's Twenty Years at Hull-House, chapter 4 (1910), with Frost and the model essay, in place of Keller and Hurston (grade 9); the two-text paragraph is Frost and Addams. Unit 4 and e12-lit-american-modern: 'I, Too' (1926) in place of 'The Negro Speaks of Rivers' (grade 5). Unit 6: Four Freedoms candidate dropped (grade 10). The Age of Innocence kept here only. Unit 7 and e12-info-founding-documents: Gettysburg (grade 9) and the Second Inaugural (grade 11) named as rereads for a new task |
| Expert | 2 | Applied | Unit 1 13 to 15 days, unit 8 38 to 36; Pride and Prejudice chapters read at home with one class day; Du Bois chapters 1 and 3 only. Day ranges recomputed (units 1 to 15, 16 to 38, 39 to 50, check 51 to 53, 54 to 71, 72 to 82, check 83 to 86, 87 to 102, 103 to 120, check 121 to 124, 125 to 160); process due days 14, 37, 101, 119, final paper 158 |
| Expert | 3 | Applied, merged with Codex 5 | Unit 8 milestone line (question about day 125, history's 123; eight sources, at least three primary, list about day 135; draft about day 145; presentation taught and rehearsed by day 147; talks days 150 to 156 in two forms for two audiences, one beyond the classroom; final paper about day 158); question 1920 to today in a paired school; cut order (revision days, then the second talk; never the list or draft); the same in the US History II calendar row and e12-research |
| Expert | 4 | Applied, merged with Codex 2 | Paper path bullet as grade 11; W.11-12.6 added to "Where each thread ends" (unit 8, the paper published and updated with the talk's media); e12-process and e12-presentation notes carry the boundary |
| Expert | 5 | Applied | Housing set from government works (a Census Bureau release, a HUD or GAO report, council minutes, a hearing) and two original Curio Class pieces as a news report and an op-ed; Reagan's Challenger address (1986) as the effective-rhetoric pick, the current inaugural read under the balance rule; one question wording |
| Expert | 6 | Applied | Open archives; grade 11's references plus Onions (1911) and Schmidt for Hamlet, in a References bullet and unit 2; L.11-12.3a models from the year's texts (Woolf, Du Bois, Fitzgerald), not a paid style book; e12-word-strategies names Onions and Schmidt |
| Expert | 7 | Applied | Unit 7 teaches court-opinion structure on Tinker (one day) as the structure row's second text; unit 5 says Woolf here, court opinions in unit 7; e12-info-structure notes say the same |
| Expert | 8 | Applied | Unit 7 reason and the Government cross-subject row: Plessy and Brown kept here; Government picks another pair beside it (its frame's choice, under Cross-subject notes) |
| Expert | 9 | Applied | Unit 2: a teacher-led scene discussion and a one-on-one draft conference; unit 1: a partner talk before each seminar; unit 6: an informal two-minute talk; e12-seminar and e12-presentation notes |
| Expert | 10 | Applied, merged with Codex 5 | Hard-content line recomputed with history's checks (Holocaust 42 to 56, bomb 57 to 66, civil rights 86 to 102); Wolfsheim chapters fall after day 56; unit 4 adds a Jewish community reader beside the Black community reader |
| Expert | 11 | Applied | Shelf adds Mourning Dove, Cogewea, the Half-Blood (1927). Sui Sin Far stays in grade 11, and Zitkala-Ša (the expert's fallback) is not taken because grade 9 reads 'The School Days of an Indian Girl'. Unit 4's period choice set adds Sugimoto, A Daughter of the Samurai (1925), Mena, 'The Gold Vanity Set' (1913), and the opening of Cogewea, so Asian American, Mexican American and Native authors are in a unit, not only the shelf |
| Expert | 12 | Applied | Unit 3 "Money, marriage and class: Swift, Austen and Wilde, 1729 to 1895", with the expert's question |
| Expert | row changes | Applied | e12-seminar, e12-info-founding-documents (Walker; words "appeal" for "sentiments"), e12-lit-interpretations (Trifles retrieval, the lesson supplying the scene and both versions) |
| Expert | settled | Applied | All nine rows |
| Codex | 1 | Applied in part | Print-copy claim rewritten as a rule, as in grade 11. Inventory before scope and sequence rejected for the same reason as grade 11 Codex 7 |
| Codex | 2 | Applied | With expert 4. Its "teaching-parent device route" is not added: who uses the course outside a school is an audience question (For Cory) |
| Codex | 3 | Applied | Unit 6 and e12-info-rhetoric: one recorded address's claim, its evidence told apart from assertion or appeal, reasoning and evidence judged, delivery's effect; named in the assessment brief |
| Codex | 4 | Applied | The three rows synced; For the lead 2 to 4 rewritten as settled |
| Codex | 5 | Applied | Government 38 to 46 and 64 to 71, Economics 45 to 51 (year 125 to 131), history's three ranges; presentation rehearsal by day 147 |
| Codex | 6 to 11 | Not acted on here | Earlier review files (US History II, US Government, US History I): under For the lead |
| Codex | settled | Applied | All rows but the inventory timing and the review files |
| Writer | lead 1 | Applied | Settled with the new days |
| Writer | lead 2, 3, 4 | Applied | The three row changes (above) |
| Writer | lead 5 | Kept | Recent texts, with the Challenger address added |
| Writer | lead 6 | Applied | Recordings settled by the expert's versions; a volunteer recording optional |
| Writer | lead 7, 8 | For Cory | Check set; people |

Counts: applied 17 (expert 1 to 12, Codex 1 to 5, Codex 1 in part), rejected 1 (Codex 1's inventory timing), not acted
on 6 (Codex 6 to 11, outside this pass), for Cory 5.

## Progression changes (data/progressions/ela.csv, 20 rows)

No assumes, hands_on, standard or model column changed, so both ends of every handoff are as before.

| Row | Change |
|---|---|
| e11-lit-american-periods | Notes: Wheatley's poem and Occom's narrative named, read in unit 3 and compared |
| e11-lit-author-choices | Notes: the Trifles example (Minnie Wright offstage, the kitchen, the men leave and return) |
| e11-seminar | Notes: roles chosen from a named set or made, goal and deadline set (SL.11-12.1b started); the three settings; grade 12 wording |
| e11-info-founding-reasoning | Notes: a premise and its reasoning judged with evidence |
| e11-info-founding-documents | Notes: Wheatley's letter and Apess beside the set; theme traced, two-document synthesis |
| e11-word-strategies | Notes: free historical dictionaries named |
| e11-usage-conventions | Notes: Fowler (1926) beside a free dictionary's usage notes |
| e11-research | Notes: weeks 12 to 15 shared window; open archives; the style sheet |
| e11-process | Notes: the room-without-devices line replaced by the technology boundary |
| e11-presentation | Notes: the SL.11-12.5 boundary |
| e12-seminar | Notes: the writers' replacement with the expert's refinement; the three settings |
| e12-info-founding-documents | Notes: Walker's Appeal for Seneca Falls; Gettysburg and the Second Inaugural named as rereads. Words: "appeal" for "sentiments" |
| e12-lit-interpretations | Notes: the versions (1921 film, full-cast audio, a live class staging); the Trifles retrieval sentence |
| e12-lit-american-modern | Notes: 'I, Too' for 'The Negro Speaks of Rivers'; the choice set |
| e12-info-rhetoric | Notes: the Challenger address; evidence evaluation (SL.11-12.3) |
| e12-info-structure | Notes: Tinker taught in the law unit, Woolf in the essay unit |
| e12-research | Notes: three primary sources; the shared milestones and cut order |
| e12-process | Notes: the W.11-12.6 boundary |
| e12-presentation | Notes: the SL.11-12.5 boundary; the informal talk in the speeches unit |
| e12-word-strategies | Notes: Onions and Schmidt |

Not changed, noted: e11-reading-band and e12-reading-band notes still carry the trademarked measure's name; a later pass
on the progression may reword it as "reading level" to match the frames.

## Cross-subject notes (for those frames' owners; not edited here)

- **ELA grade 8** (`docs/courses/english-language-arts-grade-8/frame.md`, lines 167 to 168): "the Seneca Falls
  Declaration of Sentiments (grades 10 and 12)" becomes "(grade 10)"; grade 12 now reads Walker's Appeal.
- **ELA grade 10** (Cross-subject lead-in, about line 154, outside its Seams): Codex grade 11 F9 replacement: "Chemistry's
  frame is on file. Its climate-forecast work is in unit 9, weeks 23 to 26, available by week 26 for ELA's later
  explanatory work. Earlier technical writing uses the grade 9 skills and Chemistry's model explanation."
- **US History I**: the shared research window weeks 12 to 15 is now ELA's too, with one milestone calendar (question
  week 12, sources 13, draft 14, essay and talk 15); its line 150 may add the milestones. Douglass is now read in ELA
  weeks 17 to 19 (its lines 153 and 173 say 16 to 18). ELA's narrative is due at the end of week 30 and no ELA piece
  falls in weeks 12 to 19 except the shared one. For the lead 5 ("Needs the ELA 11 frame to agree"): agreed. The
  Declaration's slur is handled in ELA with this frame's own wording.
- **US History II**: the shared brief (lines 137 to 144) and line 168 can drop "sets its milestones ... before the
  pairing is called settled" and "Proposed: ... about days 121 to 160": ELA's unit 8 runs days 125 to 160 with the
  milestones in its unit 8 cell (source list day 135, draft day 145, rehearsal by day 147, talks days 150 to 156, paper
  day 158) and the same cut order; ELA requires at least three primary sources among eight. ELA 12 no longer reads
  Hurston's essay, so history's unit 2 meets it without an ELA reading beside it.
- **US Government**: unit 5's "one rights pair from four": in a school that runs ELA 12 beside it, pick a pair other than
  Plessy and Brown (ELA 12 unit 7 reads them for legal reasoning). If it runs in grade 11, its unit 2 never falls in
  ELA 11's weeks 7 to 11.

## For the lead (outside this pass's files)

Dated corrections to earlier review files, each kept as history with an "Updated 2026-11-14" line (Codex's texts):
- `progression-ela-codex-2026-11-13.md` F7 and `progression-ela-2026-11-13.md` finding 6: "Resolved in
  progression-ela-fixes-2026-11-13.md. Mathematics ownership is now recorded: S-ID.C.9 and S-ID.B.5 in Algebra I,
  grade 9; S-IC.B.6 in Algebra II, grade 11. The grade 10 ELA lean was changed to 8.SP.A.1. Same-year timing is checked
  in course frames." (grade 11 Codex 10)
- `frame-us-history-i-codex-2026-11-13.md` lines 252 and 308 and `frame-us-history-i-2026-11-13.md` lines 140 to 142
  and 154: the ELA 11 frame exists; founding documents in unit 3, research in unit 4 (weeks 12 to 15, now agreed),
  Douglass in unit 5 (weeks 17 to 19). (grade 11 Codex 11, grade 12 Codex 10 and 11)
- `frame-us-history-ii-2026-11-13.md` lines 166 to 168 and 183, `frame-us-history-ii-codex-2026-11-13.md` lines 135 and
  237: the ELA 12 frame exists; research days 125 to 160 with milestones set. (grade 12 Codex 6, 7)
- `frame-us-government-and-politics-2026-11-13.md` lines 169 to 171 and 185, and its Codex read line 276: the ELA 11, ELA
  12 and Algebra II frames exist. (grade 12 Codex 8, 9)
- Source list (`docs/APPROACH-SOURCES.md`): the LibriVox catalogue API (expert, both reads); Codex's standards strand
  pages, the Trifles text route and the curriculum comparison links.

## For Cory

- **ELA check set (scope):** name the college-level English language and English literature frameworks and New York's
  Next Generation 11 to 12 standards as the ELA 9 to 12 check set (both writers' pick, the expert agrees).
- **Community and qualified readers (people, pay):** grade 11 units 3 (Native), 5 (Black community; sexual violence), 8
  (Jewish, Chinese and Italian American), 9 (counselor); grade 12 units 1 (counselor), 2 (counselor), 3 (Irish history),
  4 (Black and Jewish community), 7 (Black community).
- **Senior early release (scope):** grade 12 unit 8's cut order covers it; shortening the course instead is yours.
- **Senior talk panel (people):** comes through the school, never through Curio Class.
- **Optional volunteer recordings (people, money):** no longer needed for either grade.
- **Device route outside schools (audience):** Codex asks for a teaching-parent device route; whether home learners are an
  audience is yours.

## Settled (for docs/reviews/DIGEST.md)

| Choice | Course | Reason |
|---|---|---|
| Wheatley's 'On Being Brought from Africa to America' and Occom's 'A Short Narrative of My Life' in unit 3, compared in unit 6 | ELA 11 | RL.11-12.9's eighteenth century had no literary text |
| Apess's 'An Indian's Looking-Glass for the White Man' (excerpt) as unit 3's Native answer | ELA 11 | A named Native-authored text beside the Declaration |
| Sui Sin Far's 'Leaves from the Mental Portfolio of an Eurasian' beside Riis's Chinatown chapter | ELA 11 | An insider account in the source set |
| Shelf: Mrs. Spring Fragrance and The Squatter and the Don in, The Age of Innocence to grade 12 only | ELA 11 | Wider authorship, no shelf repeat |
| Shared research weeks 12 to 15 with one milestone calendar; check 1 after the research unit | ELA 11 | History's settled window, unbroken |
| Unit 4 23 days, unit 7 10, unit 1 16, unit 3 21, unit 5 14, unit 6 21 | ELA 11 | Days by load; Douglass out of history's weeks 20 to 22 |
| Narrative due end of week 30 | ELA 11 | History's last week clear |
| Final grade 11 check scaffolded at the high end; independence an extension | ELA 11 | The standard's grade 11 line |
| Unit 9 "Inside the marriage, 1892 to 1916", Franklin and Twain a satire pair | ELA 11 | A topic, not a skill |
| Slurs left out with an omission mark and an editor's note; editions otherwise complete | ELA 11, 12 | BASELINE rule 6, US History I's wording |
| Free references: Webster's 1828, an etymology dictionary, Fowler 1926, the style sheet and GPO manual; Onions and Schmidt for Hamlet | ELA 11, 12 | No paid copy, no account |
| W.11-12.6 and SL.11-12.5 on a shared device; paper path leaves the digital part recorded unfinished | ELA 11, 12 | The grade 10 wording |
| Seminar roles chosen from a named set or made; grade 12 groups set goal, deadline and roles | ELA 11, 12 | No step back from grade 10 |
| Twain's 'Two Views of the Mississippi' and Addams's Hull-House chapter 4 for unit 1 | ELA 12 | Keller and Hurston are grade 9's |
| 'I, Too' for 'The Negro Speaks of Rivers'; Four Freedoms dropped | ELA 12 | Grade 5 and grade 10 repeats |
| Walker's Appeal against the Declaration | ELA 12 | Grade 10 reads Seneca Falls |
| Trifles retrieved beside Hamlet, the lesson supplying both versions | ELA 12 | RL.11-12.7 in full without a second American play |
| Hamlet versions: the 1921 film, the full-cast audio, a live class staging | ELA 12 | No Curio Class recording needed |
| Unit 1 15 days, unit 8 36; Pride and Prejudice chapters at home; Du Bois chapters 1 and 3 | ELA 12 | Days by load |
| Senior research milestones and cut order with US History II | ELA 12 | History asked for them |
| Housing set from government works and two original pieces; Reagan's Challenger address | ELA 12 | No paid copy; effective rhetoric, balanced |
| Speech evidence judged (SL.11-12.3) | ELA 12 | The standard in full |
| Court-opinion structure taught on Tinker in unit 7 | ELA 12 | The structure row's second text |
| Unit 3 "Money, marriage and class" | ELA 12 | A topic, not a mode |
| Cogewea on the shelf; Sugimoto, Mena and Cogewea in unit 4's choice set | ELA 12 | Native, Asian American and Mexican American authors in a unit |
| Jewish community reader for unit 4 | ELA 12 | Gatsby's Wolfsheim |

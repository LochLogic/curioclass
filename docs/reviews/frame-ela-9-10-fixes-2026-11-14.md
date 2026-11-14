# Fixes: ELA course frames, grades 9 and 10, after the two cold reads (2026-11-14)

Applies the expert reads (`frame-english-language-arts-grade-<n>-2026-11-14.md`) and the Codex reads
(`frame-english-language-arts-grade-<n>-codex-2026-11-14.md`) for grades 9 and 10 to the two frames, one Seams row of
the grade 11 frame and `data/progressions/ela.csv` (23 rows, notes only). Every expert finding and every "Settled by
the expert" row is applied; each Codex finding was weighed on its merits; the writers' "For the lead" items are
rewritten as settled, applied or passed to Cory. The earlier ELA fix reports were read first; their changes stand.

Gates after the fixes: `scripts/frame.py sync` (52 courses); `scripts/frame.py check english-language-arts-grade-8
english-language-arts-grade-9 english-language-arts-grade-10 english-language-arts-grade-11` 0 failures each;
`scripts/progression.py check ela` 374 rows, 0 failures; `scripts/stale.py check` 56 files, 0 failures. Both courses
keep their unit counts and totals (grade 9: 8 units, 160 days, 148 in units; grade 10: 7 units, 160 days, 148 in
units). No skill moved between units and no unit's days changed: grade 9 unit 7 and grade 10 unit 7 absorb their new
work by merging (the research stage) and by panels, as the expert settled.

Items the earlier passes left for these grades, all done: the stale "written later" lines (biology and Algebra I in
grade 9, chemistry in grade 10) are replaced with the frames' units and weeks; the wording rule (no trademarked
measure or brand name): "Lexile" became "a quantitative reading level of about ..." in both frames and in the grades 9
to 12 rows of ela.csv (e11-reading-band and e12-reading-band included, so grades 9 and 10 hand on in the same terms as
grade 11's frame), and "CommonLit is not used" became "no commercial text collection is used"; the Chemistry overlap:
the science high school pass's Codex rerun withdrew its "if-later line is not needed" note (the units overlap on days
128 to 130), so grade 10 keeps its if-later line and states the overlap; the grade 6 to 8 report's grade 9 lead-in
wording is used. Applied across both frames as the fixer's item-level call, following BASELINE rule 6 and the settled
grade 11 wording: period texts with slurs are printed with each slur left out, an omission mark and an editor's note
(grade 9: Connell's Zaroff, Hurston; grade 10: the Declaration, colonial-era translations, All Quiet).

## Grade 9

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | Cross-subject lead-in names the World History I, Biology and Algebra I frames and their weeks (Biology unit 7 weeks 19 to 23, unit 9 weeks 25 to 28; Algebra I unit 3 weeks 10 to 12); HS-LS4-1 and S-ID.C.9 rows "Taught first" with reorder bridges; unit 7's process piece explains the honeycreepers' descent from one ancestor, threats kept as reading with no solution asked; the leans table gives Biology's units and weeks; the week 26 clash with Biology's unit 9 design report is "For the lead" 8 |
| Expert | 2 | Applied | Unit 1 question: "In each story, what does the writer let the reader know, and when, and what does that do to us?" |
| Expert | 3 | Applied | Unit 1 "~W.9-10.9a starts on the stories"; unit 4 names 9b's start on memoir (merged with Codex 2); unit 6 "~W.9-10.9b, judging an op-ed's reasoning"; units 2 and 8 name RL.9-10.10 at the high end with scaffolding; Reading level bullet says where the grade 9 endpoint is assessed |
| Expert | 4 | Applied | Unit 7's second short project is the research stage of the explanatory piece (three days, own question, cited); 14 days kept |
| Expert | 5 | Applied, merged with Codex 4 | Devices bullet: one teacher screen; a transcript read aloud for the listening tasks; RI.9-10.7's film comparison recorded unfinished without playback; SL.9-10.5's digital element made on a shared device and recorded apart, a printed visual meeting it in part |
| Expert | 6 | Applied | `Pending(data/plans/english-language-arts-grade-9/texts.csv)` with the record's fields; the print-copy claim made a rule (a checked copy before the unit is planned) |
| Expert | 7 | Applied | Unit 1 reason "the most recent the public-domain line allows"; For the lead 3 names the one row; "The Necklace" in the 1903 Original Short Stories translation (McMaster, Henderson, Quesada and others) |
| Expert | settled | Applied | All five rows: Butler with a name key; Lang's sonnet "The Odyssey" (1879) as the unit 2 candidate; unit 7 research stage; unit 7 descent piece; the informational share reported both ways |
| Codex | 1 | Applied in part | Pending note lists edition or translation, copy location, excerpt boundaries, word count, rights basis, measure, four headings, reader and task, supports, reason; unwritten originals and unpicked media listed as such. Rejected: the inventory before the frame is fixed (the frame brief puts text records with the scope and sequence, as in the K to 2, 3 to 5, 6 to 8 and 11 to 12 passes) |
| Codex | 2 | Applied | Unit 2: phrase and clause types by sentence combining (participial, absolute; noun, relative, adverbial clauses), familiar ones retrieved; unit 4: a student-formulated question, narrowed or broadened, findings combined, and the same cycle in unit 7; 9a and 9b as expert 3; unit 8: each oxymoron or euphemism explained for what it adds (L.9-10.5a) |
| Codex | 3 | Applied | Unit 2's cold-passage candidate moves to book 4 (Menelaus and Helen receive Telemachus), unread and kept out of practice |
| Codex | 4 | Applied | With expert 5; unit 6 adds a teacher-delivered speech where no playback exists, still judged for point of view, reasoning and evidence |
| Codex | 5 | Applied in part | The second project's talk is kept and named: three minutes, small-group panels in one lesson. Rejected: three lessons for the talks; panels fit them in one, and the expert settled that no days move |
| Codex | 6 | Applied | With expert 1. Readers conflict on the topic: Codex is right that Biology's current frame (line 183) accepts ELA's source-based route, so there is no conflict to settle; the expert's settled descent pick is applied anyway, since it keeps ELA's piece off Biology's unit 9 topic at no cost |
| Codex | 7 | Applied | Units intro labels the day share (60 of 148) as not the anchor share; For the lead 4 reports the evidence guide's 70 and 30 comparison for grades 9 to 12, unscored, both counts in the scope and sequence, no unit replaced to move the figure |
| Codex | 8 | Applied | Same as expert 2 |
| Codex | 9 | Not acted on here | Earlier review file: under For the lead |
| Codex | 10 | Applied | As expert 7 (the expert's wording for unit 1's reason, which names the licence line as the limit) |
| Writer | lead 1, 2 | Applied | Bierce and Tagore row changes made in ela.csv; rewritten as settled |
| Writer | lead 3 | Applied | Style manual named in e9-w-short-research; rewritten as settled |
| Writer | lead 4 | Applied | Settled with both counts |
| Writer | lead 5, 6 | For Cory | Recent long text; people |
| Writer | lead 7 | Kept | Check set candidates |

Counts: applied 16 (expert 1 to 7, Codex 1 to 8 and 10, two of them in part), rejected 2 parts (Codex 1's inventory
timing, Codex 5's three-lesson budget), not acted on 1 (Codex 9), for Cory 2.

## Grade 10

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied, merged with Codex 1 | A "Shared research brief with World History II" block under Cross-subject: weeks 26 to 28 on the sea-level set in every school; history's question set by the end of week 28; the project weeks 29 to 31; one 1,500 to 2,000 word report in two scored parts (explanatory with a figure, scored by ELA with research, citation and talk; argued recommendation, scored by history); one talk in week 31; one milestone calendar and a cut order. Unit 7 question: "What is happening to one coastal community as the seas rise, and what does the evidence say about the ways to prepare?" Whether two courses share one product is passed to Cory (both readers name it a workload question) |
| Expert | 2 | Applied, merged with Codex 5 | Unit 3: Mhudi chapters 1 to 4 (about 32 printed pages) with teacher summaries of the rest, Noli in three or four chapters, Native Life chapter 1 in excerpt as background; unit 5 teaches RL.9-10.6's longer-work part outside the review line, compared with unit 3's works; unit 3 points to it; 15 days kept |
| Expert | 3 | Applied | Harper's "We Are All Bound Up Together" (1866) in place of the Declaration of Sentiments, in unit 6 and e10-ri-seminal-documents; "Texts not repeated" names the Declaration's four lenses (grades 8, 10, 11, 12). Codex 12 conflicts (see below) |
| Expert | 4 | Applied, merged with Codex 7 and 9 | W.9-10.9b named in unit 2 (Huxley) and unit 7; SL.9-10.3's parts named on the hearing and a recorded floor debate (US government works); the year-end check is the independent evidence for RL.9-10.10 and RI.9-10.10, and units 4 to 7 each carry one independent checkpoint (literary in 4 and 5, nonfiction in 6 and 7) |
| Expert | 5 | Applied | Talks in small-group panels, two days, inside unit 7's day budget (source set 4, two short inquiries 4, argument judging 4, sustained project 12, talk taught and given 3, assessment 1: 28) |
| Expert | 6 | Applied | Chemistry line rewritten with the science rerun's wording (units overlap on about days 128 to 130, the fallback covers it); HS-ESS3-5 row gives unit 9 and keeps the if-later line; Chemistry's units 1 and 2 named in the leans table; week 26 clash as For the lead 10 |
| Expert | 7 | Applied | Hard-content line: Mhudi's massacre beside the Armenian genocide days, set apart by day; unit 5 "starts at the end of week 18, after the Holocaust lessons" |
| Expert | 8 | Applied, merged with Codex 10 | Unit 3 question as the expert wrote it; citation as Codex corrected it (below) |
| Expert | 9 | Applied, merged with Codex 4 | Unit 2 names the two pages as Codex found them and keeps the Pasteur and Tyndall fallback |
| Expert | 10 | Applied | King's letter a pointer only; the translations' lean answered; both rows' "see the lead list" replaced |
| Expert | 11 | Applied | Devices bullet for media; All Quiet's sexual content and Kemmerich's amputation named; an Ndebele reader beside the Tswana reader |
| Expert | 12 | Applied | `Pending(data/plans/english-language-arts-grade-10/texts.csv)` with the record's fields |
| Expert | settled | Applied | All six rows |
| Codex | 1 | Applied in part | With expert 1 and 5. Rejected: eight presentation periods; the expert's settled panels give every student an 8 to 10 minute talk with questions in two days. The joint product goes to Cory, as Codex asks |
| Codex | 2 | Applied | Unit 6 uses grade 11's wording (the description analysed without printing the slur or asking students to speak it, paired with Chief Joseph and Nez Perce sources); the course-wide slur rule; unit 5's content note adds sexual encounters and nudity, the amputation, and suicidal distress (chapters 1 to 2, 7, 10), checked by the counselling reader before use |
| Codex | 3 | Applied | Two two-day short inquiries in unit 7 before the sustained project (bounded question, student search, two sources judged, cited synthesis); e10-w-research notes |
| Codex | 4 | Applied | The pages named as general cloning explanations for different readers; passage-level RI.9-10.5 analysis before the outline comparison |
| Codex | 5 | Applied in part | Mhudi bounded (chapters 1 to 4), Native Life as background, unit 5 named as the longer-work unit. Noli's chapters are left to the unit plan (three or four, checked against Derbyshire's text): the fixer could not verify chapter contents here |
| Codex | 6 | Applied in part | Pending note as expert 12. Rejected: the inventory before the frame is fixed (as grade 9 Codex 1) |
| Codex | 7 | Applied | Unit 1: a one-on-one evidence exchange before each seminar, a teacher-led discussion of the creature's story, decision rules, deadlines, inviting others in, a view revised on evidence; unit 7: a written evaluation of the speakers; the talk's finding explained to a peer first and the changes named (SL.9-10.6) |
| Codex | 8 | Applied | Devices bullet: SL.9-10.5's digital element recorded apart; a transcript serves listening but is not digital-media work; unit 7 names the linked publishing and the talk's digital element |
| Codex | 9 | Applied | With expert 4 |
| Codex | 10 | Applied in part | Citation: "The Postmaster" in Mashi and Other Stories (1918), "The Cabuliwallah" in The Hungry Stones and Other Stories (1916). Rejected: Codex's question; the expert's wording also fits Rizal and Plaatje and still makes students tell the text's evidence from outside knowledge |
| Codex | 11 | Applied | With expert 6 and 7 |
| Codex | 12 | Applied in part | Row pointers replaced; "27 rows" corrected to 26. Rejected: keeping the Declaration of Sentiments; the expert settled Harper, which still adds a Black American voice the set lacked even after grade 12's change. Earlier review files: under For the lead |
| Writer | lead 1 | Applied | Rewritten: the brief is written; the joint product is Cory's |
| Writer | lead 2, 3, 4, 5, 6 | Applied | Antigone row change, Mhudi's 1930 text, share, style manual, week 16 kept: rewritten as settled |
| Writer | lead 7, 8 | For Cory | People, original-text readers |
| Writer | lead 9 | Kept | Check set candidates |

Counts: applied 24 (expert 1 to 12, Codex 1 to 12, six of them in part), rejected 5 parts (Codex 1's eight periods,
Codex 5's named Noli chapters deferred, Codex 6's inventory timing, Codex 10's question, Codex 12's Sentiments), not
acted on 1 (Codex 12's review-file rows), for Cory 2.

## Progression changes (data/progressions/ela.csv, 23 rows)

No assumes, hands_on, standard, model, words or cross_subject cell changed, so both ends of every handoff are as before.

| Row | Change |
|---|---|
| e9-rl-evidence, e9-rl-range-scaffolded, e9-ri-evidence-central-idea | "a quantitative reading level of about 1050 to 1335" |
| e10-rl-evidence, e10-rl-range-independent, e10-ri-evidence-central-idea | "a quantitative reading level of about 1185 to 1335" |
| e11-reading-band, e11-lit-themes, e12-reading-band, e12-lit-author-choices | Measure wording in the same terms (1185 to 1385; the Narrative, Scarlet Letter and Gatsby figures) |
| e9-rl-structure-time | Bierce dropped; Poe, Saki, Jacobs, Connell and the Odyssey's flashback |
| e9-rl-world-stories | Chekhov, Maupassant, Machado de Assis, Pu Songling; Tagore is grade 10's |
| e9-w-short-research | The two projects (unit 7's the research stage); own question, narrowing, synthesis; the style manual named |
| e9-l-phrases-clauses | Noun, relative and adverbial clauses by sentence combining |
| e9-sl-presentation | Second talk in panels; the SL.9-10.5 boundary |
| e9-w-informative | The descent topic; human impact stays Biology's |
| e9-w-analysis-routine | Where 9a and 9b start |
| e10-rl-world-literature | All Quiet as the longer work, taught in a later unit; the translations' lean answered |
| e10-ri-seminal-documents | Harper for the Declaration of Sentiments; King a pointer; the Declaration's slur not printed |
| e10-w-research | Two short inquiries; the shared brief named |
| e10-sl-presentation | Panels; SL.9-10.6 adaptation; the SL.9-10.5 boundary |
| e10-sl-seminar | The standard's range of settings |
| e10-w-process | The W.9-10.6 boundary in the grade 9 and 11 terms |

Not changed, noted: the grade 2 reading row (line 67, "about 420 to 820 Lexile") is outside this band: under For the lead.

## Cross-subject notes (for those frames' owners; not edited here)

- **World History II** (`docs/courses/world-history-ii/frame.md`): add the same "Shared research brief" block as the
  ELA 10 frame's Cross-subject section, verbatim. Line 159's Availability cell becomes: "The shared research brief
  (written in both frames): weeks 26 to 28 on ELA's sea-level set; history supplies the paired-school question set by
  the end of week 28; the project runs weeks 29 to 31, one report in two scored parts (ELA scores the explanatory part,
  history the argued recommendation), one talk in week 31, history's audience adaptation in week 32; each course still
  teaches the whole cycle for schools that use it alone." Line 160: "ELA 10 teaches the talk in week 30; talks are
  given in week 31." For the lead 3: "Agreed with the ELA 10 frame (2026-11-14 fix pass); the joint product is with
  Cory."
- **Biology** (`docs/courses/biology/frame.md`), line 183: append "ELA 9's piece explains the honeycreepers' descent
  from one ancestor; the threats stay in its reading, so the human-impact topic is Biology's." Line 188, Writing load:
  append "ELA 9's explanatory piece is due in week 26; the unit 9 design report is due in week 27 or 28, set by the two
  scope and sequences."
- **Chemistry** (`docs/courses/chemistry/frame.md`), line 196: append "ELA 10's issue argument is due early in week
  26, apart from the forecast (about day 130); if a clear week is needed, ELA moves it to the start of week 27."
- **Algebra I** (`docs/courses/algebra-i/frame.md`), line 178: matches; no change.
- **ELA grade 8** (`docs/courses/english-language-arts-grade-8/frame.md`, line 190, For the lead 7, outside its
  Seams): replace "Grade 8 avoids the Gettysburg Address (grade 9), the Seneca Falls Declaration of Sentiments (grade
  10) and Douglass's July Fifth speech (grade 11)." with "Grade 8 avoids the Gettysburg Address (grade 9), Frances
  Harper's 1866 speech (grade 10) and Douglass's July Fifth speech (grade 11)."
- **ELA grade 12** (`docs/courses/english-language-arts-grade-12/frame.md`, line 179): replace "(grade 10 reads Seneca
  Falls)" with "(grade 10 reads Frances Harper's 1866 speech; no grade reads Seneca Falls)" and the last sentence with
  "The grade 8 frame's line naming Seneca Falls is replaced (2026-11-14 grades 9 and 10 fix pass)."

## For the lead (outside this pass's files)

- **`frame-english-language-arts-grade-9-2026-11-14.md`** (grade 9 Codex 9), append: "Status update, 2026-11-14: the
  grade 8 frame is on file and its grade 9 handoffs were checked. Biology's current frame accepts ELA unit 7's
  source-based explanation, so the topic conflict in finding 1 was already resolved; the fix pass applied the descent
  topic anyway and set the week 26 due-day question for the two scope and sequences."
- **`frame-english-language-arts-grade-10-2026-11-14.md`** (grade 10 Codex 12), append: "Updated 2026-11-14: grade 12
  replaced its Seneca Falls pairing with Walker's Appeal; the fix pass still applied Harper in grade 10 for the voice it
  adds. The course has 26 progression rows, not 27."
- **`progression-ela-stitch-2026-11-13.md`**, the Douglass row under Settled (grade 10 Codex 12), append: "Resolved in
  the reconciliation: grade 11 keeps Douglass; grade 10 uses Anthony."
- **The ELA progression reconcile report**, "Rework for the old files" (grade 10 Codex 12; not opened here under the
  blind rule), append: "Resolved by the 2026-11-14 fix passes: grade 12 uses Walker's Appeal; grade 10 uses Harper's
  1866 speech."
- **data/progressions/ela.csv**, the grade 2 reading row (line 67): "about 420 to 820 Lexile" becomes "a quantitative
  reading level of about 420 to 820" (the wording rule; a K to 2 row, outside this band).
- **Source list (docs/APPROACH-SOURCES.md):** Codex's links: the two grade 9 and one grade 10 curriculum maps, the
  standards PDF addresses, the review criteria and evidence guide addresses, the two federal cloning pages, the two
  Tagore collections, the digitized 1930 Mhudi index, and Wheen's All Quiet.
- **Process note:** a broad search for the measure's name over docs/courses/ returned two lines from a grade 6 spine
  file the blind rule names; the file was not opened and nothing from it was used.

## For Cory

- **A recent long text in grade 9 (scope).** Keep the Odyssey and Romeo and Juliet (writer), or read The Murder of
  Roger Ackroyd (1926) whole in unit 1 with about four days from the Odyssey's later books (expert's pick).
- **One joint research product with World History II (scope, workload).** The frames now write one report in two
  scored parts and one talk for schools that teach both; separate products keep each course whole but double the load.
- **Readers (people, pay).** Grade 9: the readers named for units 4 and 8. Grade 10: South Asian,
  Filipino and Southern African readers with a Tswana and an Ndebele reader (unit 3), a counselling reader (unit 5), a
  Nez Perce reader (unit 6). Both: a qualified ELA teacher for the original texts and a second rights reader.

## Settled (for docs/reviews/DIGEST.md)

| Choice | Course | Reason |
|---|---|---|
| Unit 1 question "what does the writer let the reader know, and when" | ELA 9 | Fits withheld and revealed knowledge |
| Butler's Odyssey with a Latin-to-Greek name key | ELA 9 | Plainest public-domain prose; grade 7 taught the Greek names |
| Lang's sonnet "The Odyssey" (1879) as the second later answer; a book 4 passage as the cold check | ELA 9 | Public domain; books 5 to 12 are taught |
| "The Necklace" in the 1903 Original Short Stories translation | ELA 9 | A named pre-1931 translation |
| Unit 7's second project is the explanatory piece's research stage, with a panel talk in one lesson | ELA 9 | Days by load; the row's talk kept |
| Unit 7's piece explains the honeycreepers' descent; threats as reading | ELA 9 | Keeps Biology's unit 9 topic its own |
| Phrase and clause types by sentence combining; L.9-10.5a figures explained for their role; 9a in unit 1, 9b in units 4 and 6 | ELA 9 | Standards in full |
| Period slurs left out with an omission mark and editor's note | ELA 9, 10 | BASELINE rule 6, the grade 11 wording |
| SL.9-10.5's digital element made on a shared device and recorded apart; transcripts for listening only | ELA 9, 10 | The W.9-10.6 boundary carried to media |
| Text records Pending with edition, boundaries, rights, measure, headings, supports | ELA 9, 10 | Written with the scope and sequence |
| Informational share reported by unit days and by anchor texts, the 70 and 30 comparison named | ELA 9, 10 | Different denominators |
| "A quantitative reading level of about ..." in place of the brand measure, grades 9 to 12 | ELA 9 to 12 | The wording rule |
| Shared research brief: one report in two scored parts, one talk, weeks 29 to 31, milestones | ELA 10 | One product without losing W.9-10.2 (joint product with Cory) |
| Two two-day short inquiries in unit 7; talks in small-group panels over two days | ELA 10 | W.9-10.7 in full; days by load |
| Mhudi chapters 1 to 4 with summaries; Noli three or four chapters; unit 5 teaches the longer work | ELA 10 | Unit 3's load; RL.9-10.6 planned |
| Harper's "We Are All Bound Up Together" (1866) for the Declaration of Sentiments; King a pointer | ELA 10 | A Black American voice; under copyright |
| Unit 3 question on power held by others; Tagore's two collections cited apart | ELA 10 | Answerable from the texts; correct editions |
| Cloning pages as two general explanations; passage-level analysis first; Pasteur and Tyndall fallback | ELA 10 | RI.9-10.5 in full |
| Independent checkpoints in units 4 to 7; the year-end check is the .10 evidence | ELA 10 | The end-of-grade-10 line |
| One-on-one and teacher-led discussion settings; speakers judged in writing; speech adapted | ELA 10 | SL.9-10.1, 3 and 6 in full |
| Ndebele reader for Mhudi; All Quiet's full content note | ELA 10 | Sensitivity |
| Chemistry overlap days 128 to 130 kept with the if-later line; week 26 due days set apart | ELA 10 | The science rerun's correction |

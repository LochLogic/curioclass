# Fixes: ELA course frames, grades 3 to 5, after the two cold reads (2026-11-14)

Applies the expert reads (`frame-english-language-arts-grade-<n>-2026-11-14.md`) and the Codex reads (grades 3 and
4: `frame-english-language-arts-grade-<n>-codex-2026-11-14.md`; grade 5: the rerun,
`frame-english-language-arts-grade-5-codex-rerun-2026-11-14.md`) to the three frames, the grade 6 frame's water seam
row and `data/progressions/ela.csv` (44 rows: 14 grade 3, 14 grade 4, 16 grade 5; notes, words and one
cross_subject cell). Every expert finding and every "Settled by the expert" row is applied; each Codex finding was
weighed on its merits; the frames' "For the lead" items are rewritten as settled, applied or passed to Cory. The
base text was re-read for placement: the grades 3 to 5 curriculum maps (unit assessments and performance tasks) and
the lesson folders for the grade 5 lesson counts.

Gates after the fixes: `scripts/frame.py sync` (52 courses, no collision); `scripts/frame.py check` grades 2, 3, 4,
5 and 6 each 0 failures (grades 3 to 5: 4 units, 160 days, 153 in units, 7 for checks and respond days; grade 2: 154
and 6; grade 6: 6 units, 148 and 12); `scripts/progression.py check ela` 374 rows, 0 failures; `scripts/stale.py
check` 56 files, 0 failures.

**One design across the three grades.** The skills block is laid out week by week (150 minutes): word study and
spelling 10 minutes daily; Monday, Wednesday and Friday 20 minutes of independent reading with conferences inside it;
Tuesday and Thursday a 5-minute grammar opener and 15 minutes of partner rereading with the teacher's feedback.
Grammar is taught in the module lessons; the openers sit inside the 30, not on top of the 60. The base text's second
block is named with its five parts, and the two left out (additional work with complex text, writing practice) are
named as carried by the module lessons. The split is provisional until a day is timed in the probe. Each frame's
Base text bullet carries the licence fact (2017 curriculum CC BY 4.0, store excerpt
licence/eleducation-terms-of-use-excerpt-2026-11-12.txt; only the 2024 Skills Block is CC BY-NC). "Which row sits
where" now reads base-order placement with later lettered parts named continued. Reading levels say "a quantitative
reading measure"; unit measures are labelled targets the commissioned texts must meet, and each anchor's text record
(stable id, measure, four headings, reader and task, why here, rights, whole or excerpt) is written with the scope
and sequence before its unit is planned. Each source map names the Life Science companion module as left out: a
science module designed to run beside module 2, not an ELA module.

## Grade 3

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | e3-literal-nonliteral, e3-word-strategies, e3-fluency and e3-writing-process to unit 1 (base M1 assesses RL.3.4, L.3.4, the recorded reading and the revised reading contract); e3-speaking-reports to unit 3 (base M3 performance task); e3-word-forms to unit 2 by part (1d, e, g in unit 2; 1b, c continued in unit 4). The recording and the reading contract named in unit 1. Row moves within the band are the fixer's, so not sent to Cory |
| Expert | 2 | Applied | Weekly skills-block table with the 20-minutes-three-days floor; grammar openers inside the 30; the ALL Block parts named and the two left out named |
| Expert | 3 | Applied | Source map: Life Science companion left out, with the reason |
| Expert | 4 | Applied | e3-character-actions "poverty, distance or work"; e3-compare-two-texts reworded (unit 2 side by side without the task, unit 4 first teaches) |
| Expert | 5 | Applied | Cross-subject if-later row for social studies unit 5; unit 1 gives its own short context |
| Expert | 6 | Applied | Unit 4 reason: "owns few new rows; its 37 days are the base module's practice and the year-end product" |
| Expert | 7 | Applied | Models table rewritten; the typo is gone |
| Expert | settled | Applied | All four rows |
| Codex | 1 | Applied | As expert 1, plus e3-sentences to unit 2 (base M2 assesses L.3.1h and i), with 1a and 1f continued in unit 3; SL.3.6 named in its grade 2 form in unit 1, owned in unit 3. Ownership is not sent to Cory (brief) |
| Codex | 2 | Applied in part | Measures labelled targets; text records with stable ids, rights and whole or excerpt before each unit is planned; book 2 read in at least three connected chapters. Rejected: an anchor inventory with drafts on file before the frame closes (the frame brief puts text records with the scope and sequence, as in the K-2 and 6-8 passes) |
| Codex | 3 | Applied | Weekly table totalling 450 minutes with every part located; "daily independent reading" in e3-reading-range changed to three days a week; removed base parts named |
| Codex | 4 | Applied | L.3.3b taught as conventions in unit 3 (spoken delivery beside its script, paired model, check), where the base assesses it; the unit 4 announcement repeats it as review |
| Codex | 5 | Applied | Unit 1 recorded library presentation with a labelled bar graph within grade 2 math |
| Codex | 6 | Applied | Unit 3 two-scene script and a unit 2 multi-stanza poem returned to |
| Codex | 7 | Applied | Both rows; the expert's "poverty, distance or work" wording used (it matches the frame) |
| Codex | 8 | Applied | Grade 4 Seams row: "Planning, revising and editing; supported keyboarding and digital production and publishing" |
| Codex | 9 | Applied | Codex's cross-subject wording, verbatim, in the if-later cell |
| Codex | 10, 11 | For the lead | Another file (social studies grade 3 review); text below |
| Codex | settled | Applied | All seven rows (L.3.3b in unit 3 where the row sits, unit 4 as review) |
| Codex | For Cory | Rejected in part | Ownership moves are the fixer's under this brief; time a day and readers stay with Cory |

## Grade 4

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | Unit 3 day swap as settled: M3U1 1 to 3 the canal launch, gist and close read; M3U2 5, 8 and 13 close reads of the 1816 memorial and the opposition speech; myth days from M3U2 11, 12 and M3U1 4 and 5 merged; M3U2 relabelled with its first-person narrative (now a one-sitting scene, review); unit 3 stays 39 |
| Expert | 2 | Applied | e4-informative, e4-writing-process and e4-grammar to unit 1; essay-structure introduced in unit 1; L.4.2b taught there. Grammar parts follow the base map rather than the expert's split: 1f unit 1; 1c, 1d unit 2; 1b, 1e, 1g unit 3; 1a unit 4 (the expert's own rule, "where its parts are taught in the base") |
| Expert | 3 | Applied | RL.4.7 first taught in unit 1 on the prose story and a short drama scene against a recorded or staged reading; poem recordings practice; unit 3 play review. The expert's "unit 2 drama scene" does not exist; the drama is in unit 1, where the row is owned |
| Expert | 4 | Applied | Social studies unit 5 uses the ELA canal set (both ends; their line in Cross-subject notes); the unlawful Oneida purchases named (County of Oneida v. Oneida Indian Nation, 1985), checked at source by the writer |
| Expert | 5 | Applied | Life Science companion left out, with the reason |
| Expert | 6 | Applied | Unit 4 reason names the load; skills-block floor and grammar placement stated |
| Expert | 7 | Applied | Science row rewritten (Codex's wording, same substance) |
| Expert | 8 | Applied | W.4.9b first in unit 2 (base M2, Codex's reading), named again on unit 3 |
| Expert | 9 | Applied (kept) | Optional finding; the myths stay in unit 3 with a stated link (journeys of great labor beside the canal's labor) and their own cultural context |
| Expert | settled | Applied | All five rows (RL.4.7 in unit 1, see 3) |
| Codex | 1 | Applied | As expert 2; not sent to Cory (brief) |
| Codex | 2 | Applied | As expert 1, with M3U2 lesson 8 named |
| Codex | 3 | Applied | Unit 2: teacher-managed internet exchange of drafts or comments, revision from the response, publishing, one typed page in a sitting |
| Codex | 4 | Applied | Unit 1 prose story against a recorded reading (and the drama scene) |
| Codex | 5 | Applied in part | Targets labelled, stable ids, poems and the play placed by qualitative and reader-task reasons. Rejected: manuscripts on file before the frame closes (as grade 3, Codex 2) |
| Codex | 6 | Applied in part | Omitted parts named; grammar inside the module lessons; timing in the probe. Rejected: the 10/10/10 split, in favour of the expert's 20-minutes-three-days floor, one design across grades 3 to 5; independent reading longer on fewer days gives conferences room |
| Codex | 7 | Applied | Science line rewritten; ss4-regional-cultures removed from the frame and from e4-traditional-tales; ELA gives each tale's context |
| Codex | 8 | Applied | Source map line |
| Codex | 9 | Applied | e4-traditional-tales: "read in unit 3 beside the canal play" |
| Codex | settled | Applied but one | All rows except the 10/10/10 allocation (see 6) |

## Grade 5

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | Days 41, 39, 40, 33 (153); base 154; M2U2, M3U3, M4U1 run to lesson 13; M4U1 12 and 13 one audio day; water research takes M4U3's research week; "no base lesson is left out" removed |
| Expert | 2 | Applied | Source map relabelled (M2U2 literary, M2U1 structures and research, M4U1 with the recording, M4U3 research, essay, leaflet, live presentation). Unit 2 gets two original rainforest adventure stories (first and third person); e5-genre-compare and e5-narrator-influence to unit 2 (base M2U2 assesses RL.5.6 and RL.5.9); L.5.3b's comparison continued in unit 4 |
| Expert | 3 | Applied | Monologue and its recorded performance in unit 1; e5-narrative and e5-writing-process to unit 1; e5-research stays in unit 2, previewed in unit 1 |
| Expert | 4 | Applied | All named rows edited in ela.csv, plus e5-informative, e5-integrate-several, e5-opinion; DESK-ANSWERS note for the lead (below) |
| Expert | 5 | Applied | Both unit 4 stories about drought; the seam recorded in both frames (grade 5 Handed-on note, grade 6 Seams row) |
| Expert | 6 | Applied | 1947 reports and the teammate's memory: renewal search, fallback Curio Class account; UDHR in the official 1948 text with Curio Class's own explainers, in unit 1 (the expert's table said "unit 4"; the declaration is read in unit 1) |
| Expert | 7 | Applied | Life Science companion left out, with the reason |
| Expert | 8 | Applied | Unit 4 reason: load is the products; skills-block floor and grammar placement |
| Expert | settled | Applied | All five rows |
| Codex | 1 | Applied | As expert 1 |
| Codex | 2 | Applied | As experts 2 and 3; not sent to Cory (brief) |
| Codex | 3 | Applied in part | Targets labelled; records with ids, rights, whole or excerpt; declaration version, reports and memory resolved by route. Rejected: drafts on file before the frame closes |
| Codex | 4 | Applied | RL.5.10 a two-scene play in unit 1 and a fresh scene read alone; W.5.6 shared-document exchange in unit 2; SL.5.2 a talk with a simple chart in unit 1, the water display as review in unit 4; L.5.2c tag questions in unit 1; L.5.3b compared and contrasted in unit 4 |
| Codex | 5 | Applied in part | As grade 4, Codex 6: expert floor, not 10/10/10; e5-reading-range now three days a week |
| Codex | 6 | Applied | Rows edited, so the DESK-ANSWERS status can say done (for the lead) |
| Codex | 7, 8, 9 | For the lead | Other files; text below |
| Codex | settled | Applied but one | Rejected: "retain the flood-to-weather seam" as a flood story; the expert's settled drought stands, and the seam is kept through water (grade 6 adds floods, weather, warnings) |

Readers in conflict, decided: skills block (expert floor over 10/10/10, one design, both readers ask for timing);
grade 5 flood (expert settled drought; Codex's seam kept by water, not by a flood story); W.4.9b (unit 2 as Codex
reads the base, named again in unit 3 as the expert asked); grade 4 grammar split (the base map, by the expert's own
rule); RL.4.7 and the UDHR unit (the expert's unit numbers were slips; substance applied in the right unit).

Earlier fix reports' items for grades 3 to 5: kindergarten's ek-opinion in unit 1 and the grade 2 recordings handoff
to e3-fluency stand (grade 3 Seams reads them); grade 4 keeps its Anansi tale and grade 5 has no start-over-after-flood
story, so the grade 6 to 8 picks need nothing further. Grade 4's Rossetti picks leave out "Who Has Seen the Wind?"
(grade 6 reads it).

## Progression changes (`data/progressions/ela.csv`)

- Grade 3: e3-central-message (unit 1 fables and folktales; unit 2 tales the base text's own, adapted); e3-character-actions
  ("poverty, distance or work"); e3-literal-nonliteral, e3-word-strategies, e3-fluency, e3-writing-process (unit 1);
  e3-story-parts (two-scene script, multi-stanza poem); e3-same-author (settled); e3-reading-range (three days a
  week); e3-main-idea (SL.3.2 graph task); e3-compare-two-texts; e3-speaking-reports (unit 3, L.3.3b as conventions);
  e3-word-forms and e3-sentences (units and parts).
- Grade 4: e4-academic-words words "canal; surveyor"; e4-reasons-evidence (1816 memorial and the speech against);
  e4-opinion (1817, support or oppose); e4-traditional-tales (unit 3; cross_subject ss4-regional-cultures removed);
  e4-conventions (2b in unit 1); e4-firsthand-secondhand (unit 3 history set dropped); e4-poetry-drama (RL.4.7 in
  unit 1); e4-informative, e4-writing-process, e4-grammar (unit 1, parts by unit); e4-narrative (unit 3 scene,
  review); e4-explain-events (New York split over the canal); e4-evidence-inference (9a unit 1, 9b unit 2);
  e4-reading-range (three days a week).
- Grade 5: e5-visual-multimedia (river story; drought note); e5-locate-sources; e5-reasons-to-points; e5-opinion
  ("qualities"; water); e5-presenting; e5-writing-process (unit 1; water leaflet); e5-academic-words "watershed";
  e5-genre-compare and e5-narrator-influence (unit 2, review and L.5.3b in unit 4); e5-informative;
  e5-integrate-several; e5-narrative (unit 1); e5-research (unit 1 preview); e5-reading-range (plays; three days a
  week); e5-several-main-ideas (charts); e5-conventions (tag questions in unit 1).

No row moved grade; no standard code changed; both ends of every handoff hold (progression check 0 failures).

## Cross-subject notes (for the frames' owners; not edited here)

- **Science grade 4, line 151**, column 4: "ELA grade 4 unit 2 (about school days 39 to 77), after" becomes "ELA
  grade 4 unit 1 (about school days 1 to 38), the same weeks"; column 5 becomes "The bridge stays for the first
  weeks: the explanation is written on a science frame (claim, evidence, reasoning) of three to five sentences; ELA's
  informative essay arrives in the same weeks".
- **Science grade 4, lines 165 to 169**: "ELA grade 4 leans on 4-LS1-1 for its animal defense topic (...)" becomes
  "ELA grade 4 unit 2 (about school days 39 to 77) introduces the animal structures and defense relationships through
  its own texts (e4-main-idea-summary, e4-explain-events, e4-academic-words, e4-research); science unit 6 later
  investigates and models them. ELA leans on 4-ESS3-2 only as an example structure (e4-text-structure)."
- **Social studies grade 4, unit 5**, Candidate cell: "New York grade 4, the Erie Canal as the case of a canal"
  becomes "New York grade 4, the Erie Canal as the case of a canal, using ELA grade 4 unit 3's canal set (about days
  81 to 119), no second canal text".
- **Social studies grade 4**: ELA no longer leans on ss4-regional-cultures; nothing to edit unless its frame names
  that lean.
- **Social studies grade 3, Cross-subject**: add "ELA grade 3 unit 1 (about days 1 to 39) reads a short Booker T.
  Washington selection with its own brief explanation of enslavement and emancipation; social studies unit 5
  develops the history later." Also row "W.3.7 short research, W.3.2 informative writing, SL.3.4 reporting": SL.3.4
  is now taught in ELA unit 3 (about days 81 to 119).

## For the lead

1. **Social studies grade 3 Codex review** (`docs/reviews/frame-social-studies-grade-3-codex-2026-11-13.md`). After
   the paragraph ending "Mark the calendar as provisional until peer frames exist." (about line 213) append: "Superseded
   2026-11-14: the Grade 3 mathematics, ELA and science frames now exist. Check availability against those frames.
   Retain the social studies spoken-claim bridge because full ELA opinion writing begins in Unit 3." After "Cross-subject
   order against peer course frames that do not yet exist." (about line 254) append: "Superseded 2026-11-14: peer
   frames are available. Their planned teaching order can now be checked; daily scheduling and classroom timing remain
   unverified."
2. **DESK-ANSWERS, q-cross-progression-1** (about line 946): "Nine grade 5 rows and e6-reading-range updated in
   data/progressions/ela.csv." becomes "Nine grade 5 rows and e6-reading-range named for update on 2026-11-13; the
   grade 5 rows' remaining disaster wording, product descriptions and placements were edited on 2026-11-14 in the ELA
   grades 3 to 5 fix pass (docs/reviews/frame-ela-3-5-fixes-2026-11-14.md)."
3. **DESK-ANSWERS, lines 529 to 542** (the piece 2 entry): after "Still owed: ..." add: "Resolved after this entry: the
   six questions were answered under q-ela-piece-2 on 2026-11-12. The fallback choice was completed in the subsequent
   fallback-hero decision, and the ELA findings were logged as recorded under "Sara's pieces 1 and 2 taken in." Earlier
   text choices remain historical and must be read alongside the later course-text decision." Keep the rights
   second-read as pending.
4. **DESK-ANSWERS, lines 548 and 554**: "not yet answered" and "Still open with Cory: card q-ela-piece-2" each become
   "q-ela-piece-2 was answered and applied on 2026-11-12; see the following entry."
5. **`docs/reviews/rubric-ela-2026-11-11.md`, lines 309 to 317** (For Cory): add "Resolved 2026-11-12, q-ela-piece-2:
   Curio Class grades 3 to 5 teach foundational skills, and Gateway 1 applies in full. The taught sequence and checks
   remain implementation requirements." and mark the question closed.
6. **Source list**: the Life Science module-2 folders (grades 3, 4, 5) are science companion modules, not alternative
   ELA modules; the base text's old unit web addresses now redirect to its planning page (the local store holds the
   evidence); the working criteria address the Codex reads used.

## For Cory

- **Time a day:** the frames hold 90 minutes (60 lesson, 30 skills block) against the base text's 120; keep 90 until
  a day is timed, or move the yardstick to 120.
- **Readers and pay:** qualified ELA readers for the original texts; a Haudenosaunee community reader (grade 4 unit
  3); readers for the grade 3 slavery excerpt and named places, Puerto Rico (grade 5 unit 2), Black athletes and
  segregation (grade 5 unit 3) and tribal water (grade 5 unit 4): who, and any pay.

## Settled (for DIGEST.md)

| Choice | Reason | File |
|---|---|---|
| Grades 3 to 5 skills block: word study 10 daily; independent reading 20 on three days; grammar opener 5 and partner rereading 15 on two days; grammar taught in module lessons | Expert floor; one design; timed in the probe | grades 3, 4, 5 frames; reading-range rows |
| Rows sit where the kept base lessons first teach and assess them; later parts named continued | Base-order placement | grades 3, 4, 5 frames; ela.csv |
| Grade 3: fluency, writing process, word strategies, literal and nonliteral in unit 1; word forms and sentences in unit 2; speaking reports (with L.3.3b as conventions) in unit 3 | Base M1, M2, M3 assessments | grade 3 frame; ela.csv |
| Grade 4: informative, writing process, grammar in unit 1; grammar parts by the base map; RL.4.7 on prose and drama in unit 1; W.4.9b in unit 2 | Base M1U2 and M2 assessments | grade 4 frame; ela.csv |
| Grade 4 unit 3 day swap; social studies grade 4 unit 5 uses the ELA canal set; the unlawful Oneida purchases named | Base lesson content; one canal set | grade 4 frame; ela.csv |
| Grade 5 days 41, 39, 40, 33 on a base of 154; monologue in unit 1; literary pair and RL.5.6, RL.5.9 in unit 2; both unit 4 stories drought | Lesson counts; base M1U3 and M2U2; grade 6 seam | grade 5 frame; grade 6 Seams row; ela.csv |
| Life Science module-2 folders are science companions, left out in grades 3 to 5 | Their own overviews | grades 3, 4, 5 source maps |
| UDHR official text with Curio Class explainers; 1947 reports by renewal search, Curio Class account as fallback | Clear authorship and rights | grade 5 frame |
| No anchor drafts required before a frame closes; measures are targets until text records | Frame brief | grades 3, 4, 5 frames |

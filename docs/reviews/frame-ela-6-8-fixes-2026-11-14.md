# Fixes: ELA course frames, grades 6 to 8, after the two cold reads (2026-11-14)

Applies the expert reads (`frame-english-language-arts-grade-<n>-2026-11-14.md`) and the Codex reads
(`frame-english-language-arts-grade-<n>-codex-2026-11-14.md`) for grades 6, 7 and 8 to the three frames and
`data/progressions/ela.csv` (6 rows, notes only). Every expert finding and every "Settled by the expert" row is
applied; each Codex finding was weighed on its merits; the writers' "For the lead" items were rewritten as settled
or passed to Cory.

Gates after the fixes: `scripts/frame.py sync` (52 courses); `scripts/frame.py check english-language-arts-grade-6
english-language-arts-grade-7 english-language-arts-grade-8` 0 failures each; `scripts/progression.py check ela` 374
rows, 0 failures (also as run inside `scripts/plan.py check`, which exits 0); `scripts/stale.py check` 56 files, 0
failures. All three courses keep their unit counts and totals (grades 6 and 7: 6 units; grade 8: 5 units; each 160
days, 148 in units). No skill moved between units. Days moved: grade 7's check 2 (after unit 4, not unit 3), grade
8's 4 days from unit 5 to unit 2. The grade 5 and grade 9 frames were not edited: no handoff to or from them changed.

Rule 29 in all three frames: every older primary source is now a paired excerpt, short and read with full support,
and the standard it served is taught first on an original or federal anchor (named per course below). Whether
primary documents may anchor in grades 6 to 8 is collected for Cory, not decided.

## Grade 6

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | Fixed within rule 29: unit 2's anchors are the two features, the two editorials (now on whether a town's rules should be posted), the council talk and the scribe story; RI.6.6 taught on the editorials and the talk, then applied to the paired prologue and epilogue (King, 1910). Unit 6's RI.6.9 compares the original Cline profile with the National Weather Service's history page on the 1900 storm, Cline's report (1900) set beside them as a paired third. Reading level and Base text bullets say so. Band question for Cory (For the lead 4) |
| Expert | 2 | Applied | Unit 2 question "How did Hammurabi want his people to see him, and how did the words on the stone make them believe it?"; process prompt "Should every rule in our town be posted where anyone can read it, as Hammurabi's stone was?"; reason sentence and first Cross-subject row as written by the expert. This also repairs the overlap with social studies 6 unit 4 (same code, same question): ELA reads purpose and word choice, justice stays with social studies' written claim |
| Expert | 3 | Applied | Novella premise: a family of generations in the river town choosing to rebuild low or move uphill; question "What does a river town keep, and what does it change, after a flood?"; prompt "a story in which a character makes a choice the river forces on them". Ends the repeat of grade 5 unit 1's start-over premise |
| Expert | 4 | Applied | (a) count corrected to about 31 by the units' own list; (b) the voice line in Base text; (c) the open-licence search before the poems and play are written; (d) writers to Cory |
| Expert | 5 | Applied | Days bullet replaced (grade 5's 90-minute block ends; 15 minutes of in-class reading twice a week for conferences; choice books from the Curio Class Reading Room shelf or home); unit 1's text cell names the shelf |
| Expert | 6 | Applied | Readiness line under the Seams table; each unit's reason names its readiness tasks on the grade 5 rows of its seam line |
| Expert | 7 | Applied | (a) W.6.6's three pages in one sitting named in unit 6; (b) unit 2's word-list sentence replaced, unit 1 keeps a word list |
| Expert | 8 | Applied | One-sitting narrative scene in unit 4 (learning to write a word in a new script); calendar 3, 3, 3, counted by pieces, the scope and sequence reporting by days |
| Expert | 9 | Applied | Science rows "Science 6 unit 3, days 52 to 90 (beside)" and "Science 6 units 4 and 5, days 93 to 136 (before)"; the tsunami note matched to science; unit 3 reads percent (math 6 unit 3 by day 58), no temperature below zero (math 6 unit 7); math row "Math 6 unit 8, about days 142 to 158" |
| Expert | 10 | Applied | The dash note fixed in e6-punctuation-spelling (and e8-pause-omission); RUBRIC-ELA and lens replacement texts under For the lead below |
| Expert | 11 | Applied | Heroes decision honoured (see "Heroes" below); a brief bullet and For the lead 5 say how |
| Expert | settled | Applied | All six rows (unit 2 question and prompt; unit 1 premise; the unit 4 narrative; percent in unit 3; Rossetti stays, grade 4 leaves it out, recorded in For the lead 5; the Reading Room shelf) |
| Codex | 1 | Rejected | An environment note, not a frame defect: `plan.py check` ran here and exits 0 |
| Codex | 2 | Applied in part | Base text says each original is a commission to the spec and its text record comes with the scope and sequence. Rejected: an anchor inventory and text records before the frame is fixed (the frame brief puts them with step 3, as in the grade 11 and 12 pass) |
| Codex | 3 | Applied | Unit 6's flood wall becomes a second short research project (focused and refocused question, fenced set with FEMA and Army Corps pages and a weak flyer, credibility, notes, basic bibliography) feeding the argument; Days bullet says two projects |
| Codex | 4 | Applied | With expert 1 |
| Codex | 5 | Applied | Unit 3's report published through the school's own digital route with peer comments that lead to a revision; the paper path records that part of W.6.6 unfinished |
| Codex | 6 | Applied | L.6.1e in full in unit 1 (variations identified, the fitting form explained, a model, reference or checklist used to revise); e6-pronouns teacher note matches |
| Codex | 7 | Applied | With expert 10 (the expert's shorter wording) |
| Writer | lead 1 | For Cory | Minutes, now with the in-class reading time |
| Writer | lead 2 | Kept | The Texts column rename (brief owner's edit) |
| Writer | lead 3 | Applied | Count corrected |
| Writer | lead 4 | Kept | Picks, with the unit 1 and 2 changes |

Counts: applied 17 (expert 1 to 11, Codex 2 in part to 7), rejected 1 (Codex 1; Codex 2's inventory timing in
part), for Cory 4 (band anchors, writers, minutes, readers).

**Heroes (Cory, 2026-11-12, q-course-texts item 3).** Unit 1's novella is now the present-day hero story (a
twelve-year-old's trials in the flood year, a choice the river forces), and the paired text is one myth retold in
Curio Class's own words: Yu the Great, who tamed China's floods with channels where his father's dams failed
(from Legge's 1865 Shoo King, public domain). No other frame reads Yu; social studies 6 reads Gilgamesh, so that
flood myth was not used. The frame reconcile still settles where the pilot itself runs.

## Grade 7

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | Fixed within rule 29: unit 4's RI.7.6 taught on the two youth-council editorials and the feature, then applied to Pericles; RI.7.7 taught on a course recording of one editorial delivered as a speech, the 1912 Roosevelt recording an optional paired second; unit 3's RI.7.9 stays on the two original articles, the 1717, 1721 and 1798 excerpts paired. Reading level names them as paired. Band question for Cory |
| Expert | 2 | Applied | Each part in full in its owning unit: W.7.1c in unit 4's process argument (the expert said unit 2, but the argument is unit 4's); W.7.2c in unit 2's informative piece, used again in unit 3; SL.7.1b and SL.7.1c in unit 1 (owner), SL.7.1b used again in unit 3's research groups, SL.7.1c in unit 4's seminar; L.7.4c in unit 3 (owner): dictionary, medical glossary and thesaurus, print and digital; W.7.6 in unit 3 (shared-draft comments, links); SL.7.5 in unit 3 (owner), used again in unit 6's talk |
| Expert | 3 | Applied | The Klamath dam removal (four dams, 2023 to 2024; USGS, NOAA Fisheries, Bureau of Reclamation) replaces the Elwha; Karuk and Yurok readers; the Tribes' pages linked, not copied |
| Expert | 4 | Applied | e7-reading-range thread 1 as the expert wrote it; e8-reading-range "republic" out of the words reused; e6-reading-range hands on "citizens in Athens"; the social studies 7 line under Cross-subject notes; For the lead 3 rewritten as settled |
| Expert | 5 | Applied | Question "How did Pericles want the world to see Athens, and who did his picture leave out?"; "after" replaced by "beside social studies 7 unit 8" |
| Expert | 6 | Applied | A course-made short film of one scene beside the audio. Placed in unit 4, where RL.7.7 is owned (the expert's table says unit 5, which comes after), and unit 5's play also filmed for a second use, so both the settled row and the order hold |
| Expert | 7 | Applied | Count corrected to about 29; voice line; open-licence search |
| Expert | 8 | Applied | Days bullet and the shelf, as grade 6 |
| Expert | 9 | Applied | Readiness line and per-unit readiness tasks |
| Expert | 10 | Applied | Keats, "On First Looking into Chapman's Homer" (1816), replaces Sonnet 18 |
| Expert | 11 | Applied, merged with Codex 7 | Drought maps from the National Integrated Drought Information System (federal); a Drought Monitor map, where shown, carries its own rights line with the attribution its permission page asks |
| Expert | 12 | Applied | Original feature on the 1896 marathon and the legend's sources; teacher note: a legend taught as a legend |
| Expert | 13 | Applied | Check 2 after unit 4: unit 4 days 87 to 108, check 2 109 to 112, unit 5 113 to 134, unit 6 135 to 156; RI.7.6 moves to check 2 |
| Expert | 14 | Applied | African American history reader; teacher note on crediting Onesimus |
| Expert | 15 | Applied | Black Sunday one-sitting narrative in unit 2; calendar 3, 3, 3 |
| Expert | 16 | Applied | Dash rows fixed in the CSV; RUBRIC and lens texts under For the lead |
| Expert | settled | Applied | All seven rows |
| Codex | 1 | Applied in part | As grade 6 Codex 2 |
| Codex | 2 | Applied | With expert 2 (W.7.6 interact and collaborate, shared device or lab, recorded unfinished on paper) |
| Codex | 3 | Applied | Unit 6 adds a second short research project and a findings talk (both "used again", owners stay in unit 3) |
| Codex | 4 | Applied | With expert 2; plus SL.7.6 as a rehearsal to a partner and a formal talk |
| Codex | 5 | Applied | With expert 2 |
| Codex | 6 | Applied, conflict decided | Codex calls Athens-only Cory's scope; the expert settled it and the brief says not to re-decide settled rows. It changes a topic inside a knowledge thread, not a standard, so it is item level; all four ends are now consistent (e6, e7, e8 rows, the frames) and the social studies 7 line is recorded below |
| Codex | 7 | Applied | With expert 11 |
| Codex | 8 | Applied | With expert 5 |
| Codex | 9, 10 | Not acted on here | Earlier review files: replacement texts under For the lead |
| Writer | lead 1 | For Cory | Minutes |
| Writer | lead 2 | Kept | Texts column |
| Writer | lead 3 | Applied | The row change, both ends |
| Writer | lead 4 | Applied | Count corrected |
| Writer | lead 5 | Kept | Picks, with Keats and the Klamath added |

Counts: applied 23 (expert 1 to 16, Codex 1 in part to 8), rejected 0 (Codex 1's inventory timing in part), not
acted on 2 (Codex 9, 10), for Cory 4 (band anchors, writers, minutes, readers).

## Grade 8

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | Fixed within rule 29: unit 2's anchors are the two features, the National Archives pages, two original marker editorials written to answer each other, two original news reports that disagree on a fact and its meaning, the recorded talk. RI.8.4, RI.8.8, RI.8.6 and RI.8.9 are taught on those, then applied to the paired Declaration, Banneker and Jefferson, Carey and Jones and Allen. The Declaration read "for its word choice and for who answered it"; the reason names civics 8 unit 2, ELA 10 and 11. Unit 3's older items marked supporting. Band question for Cory |
| Expert | 2 | Applied, merged with Codex 4 | Unseen literary text in unit 5 and informational text in check 3, top of the band, without before-reading help, scored apart; supported performance recorded separately (Reading level bullet) |
| Expert | 3 | Applied, merged with Codex 2 | In full where owned: W.8.2a to c in unit 1's analytical essay (preview, broader categories, formatting and a graphic; well-chosen; varied transitions for cohesion), used again in unit 3; W.8.3c in unit 4 (the owner; the expert said unit 1, whose narrative is on-demand review); SL.8.1b in unit 1, used again in unit 3's groups; W.8.6 in unit 3 (interact and collaborate); L.8.4c in unit 3 (owner; glossary of 1906 terms, thesaurus) |
| Expert | 4 | Applied | Nasreddin Hodja (Barnham, Tales of Nasr-ed-Din Khoja, 1923, edition to confirm) replaces Anansi; a Turkish or Persian tradition reader |
| Expert | 5 | Applied | Unit 2 32 days (31 to 62), unit 3 63 to 88, check 1 89 to 92, unit 4 93 to 124, check 2 125 to 128, unit 5 28 days (129 to 156); every day reference recomputed (publishing by day 84, research routine by day 76) |
| Expert | 6 | Applied | Thread words in frame and row (citizen, democracy, right, press, constitution, amendment; trait, gene, source, claim, trial); the Preamble named in unit 2 |
| Expert | 7 | Applied | Count about 23; voice line; open-licence search |
| Expert | 8 | Applied | Days bullet and shelf |
| Expert | 9 | Applied | Readiness line and tasks |
| Expert | 10 | Applied, merged with Codex 5 | "Civics unit 2 (days 16 to 30, before) and unit 6 (rights over time, days 77 to 95, after)"; all social studies rows say civics with unit days |
| Expert | 11 | Applied | For the lead 6 (RL.8.9, myths only until Cory answers); dash row fixed |
| Expert | 12 | Applied | Teacher note on a parent living apart |
| Expert | 13 | Applied | Analysis essay counted as informative and said so; one-sitting myth retelling from a minor character in unit 4; 3, 3, 3 |
| Expert | settled | Applied | All six rows |
| Codex | 1 | Applied in part | As grade 6 Codex 2 |
| Codex | 2 | Applied | With expert 3 |
| Codex | 3 | Applied | A findings talk in unit 3; a second research cycle in unit 5 on a student-generated gene question feeding the explanation and the talk |
| Codex | 4 | Applied | With expert 2 |
| Codex | 5 | Applied | Medium-choice and source-motive work from about day 145, after civics unit 9; the newsroom feature teaches the routine if civics is later; Civil War line replaced |
| Codex | 6 | Applied | Unit 1's chapter marked a grade 7 review used as a readiness sample |
| Codex | 7 | Not acted on here | Grade 9 frame line 156 is outside its Seams table: under Cross-subject notes |
| Codex | settled | Applied except one | Codex's "retain 30, 28, 26, 32, 32" conflicts with the expert's settled 4-day move: the expert's stands (unit 2 carries the hardest paired texts, the process argument and now anchor-first teaching; unit 5's added research cycle is short, from a fenced set) |
| Writer | lead 1, 2 | For Cory / kept | Minutes; Texts column |
| Writer | lead 3 | Applied | Five units settled |
| Writer | lead 4 | Applied | Rule 29 kept; band question to Cory |
| Writer | lead 5 | Applied | Count corrected |
| Writer | lead 6 | Applied | Seneca Falls "(grade 10)", per the grade 11 and 12 pass |

Counts: applied 19 (expert 1 to 13, Codex 1 in part to 6), rejected 1 (Codex's allocation row), not acted on 1
(Codex 7), for Cory 5 (band anchors, writers, minutes, readers, RL.8.9).

## Progression changes (data/progressions/ela.csv, 6 rows, notes only)

No assumes, hands_on, standard, model or words column changed.

| Row | Change |
|---|---|
| e6-reading-range | Thread 1 "used again in e7-reading-range (citizens in Athens)" |
| e7-reading-range | Thread 1 "citizens and government in Greece": Athenian democracy and who counted as a citizen; ss7-roman-republic dropped; words citizen and democracy added; Rome stays with social studies |
| e8-reading-range | Inherited from grade 7 Athens; words reused "citizen, democracy, law, with right, press, constitution and amendment added" (the republic from ss8-greek-roman-roots); thread 2 adds "trial" |
| e6-pronouns | L.6.1e teacher note in full (variations recognised, strategies used) |
| e6-punctuation-spelling | Dash note settled (Cory, 2026-11-13) |
| e8-pause-omission | Dash note settled (Cory, 2026-11-13) |

## Cross-subject notes (for those frames' owners; not edited here)

- **Social studies 7** (world-geography-and-ancient-civilizations-ii): its cross-subject line expecting ELA 7 Rome
  texts beside unit 10 (days 121 to 133) goes: "ELA grade 7 reads no Roman text; Latin roots stay in ELA 7's L.7.4b
  word work (unit 3, days 61 to 86)". ELA 7 unit 4 now runs days 87 to 108, beside unit 8, asking how Pericles made
  his case, not whether Athens was a democracy.
- **Social studies 6** (world-geography-and-ancient-civilizations-i), line 148: ELA 6 unit 2 runs beside unit 4, not
  after it; ELA reads the code for purpose and word choice and argues a present-day question, and the "was it just"
  claim is social studies' alone. Its line 146 bridge holds (ELA 6 teaches RI.6.6 by about day 45).
- **Civics 8** (civics-government-and-civic-life): ELA 8 unit 2 is days 31 to 62, unit 3 63 to 88 (research
  routine by day 76, published by day 84), unit 5 129 to 156 with media work from about day 145, after its unit 9.
- **Science 6**: unit 5's 2011 tsunami is also read in ELA 6 unit 6 (days 137 to 156) for how the warning was made;
  content notes should match.
- **Science 8**: ELA 8 unit 5 now starts day 129, at the end of science unit 5 (days 106 to 130).
- **Biology**: unit 9 keeps the Elwha; ELA 7 moved to the Klamath.
- **ELA grade 9** (Cross-subject lead-in, line 156, outside its Seams; grade 8 Codex 7): "The World History I, Biology
  and Algebra I frames are on file and provide the timing references for this calendar. The receiving-unit bridges
  below apply whenever ELA comes first."

## For the lead (outside this pass's files)

- **RUBRIC-ELA.md**, the first sentence under "What each part asks, and where Curio Class answers it", replace with:
  "The grade 6 answers below are from the earlier grade 6 plan (docs/courses/ela-6-spine.md) and are being redone
  against the course frames (docs/courses/english-language-arts-grade-6/frame.md and the grades 7 and 8 frames); the
  frame reconcile settles which holds."
- **docs/agents/lenses/ela.md**, "What this lens does not cover", replace "docs/courses/ela-6/RIGHTS.md" with "each
  course frame's rights lines (the Units table) and the text records".
- **docs/pipeline/briefs/frame-write.md**, column list: "C3 (social studies; ELA: Texts)" (all three writers).
- **progression-ela-2026-11-13.md**, line 214 (grade 7 Codex 9): "Unverified at the original read. Subsequently
  checked against data/progressions/math.csv; the resulting changes are recorded in progression-ela-fixes-2026-11-13.md.
  Within-year availability remains a course-frame check."
- **progression-ela-codex-2026-11-13.md**, F7 and its limits bullet (grade 7 Codex 10): add "Resolved after this read by
  progression-ela-fixes-2026-11-13.md. S-ID.C.9 and S-ID.B.5 have grade 9 owners; S-IC.B.6 has a grade 11 owner. The
  grade 10 ELA lean was replaced with grade 8 scatter-plot work. Annual ownership is settled; same-year timing still
  requires the course frames." (the same item as the grade 11 pass's Codex 10)
- **Unit writers, names the frames keep generic:** the grade 6 to 8 frames name only government sources, the Curio
  Class Reading Room, and public-domain authors; the Drought Monitor's permission page and Barnham's edition are to be
  checked before use.
- **Source list (docs/APPROACH-SOURCES.md):** the drought-map permission page and the curriculum-map links Codex
  used (grades 6, 7 and 8).

## For Cory

- **Primary sources as anchors in grades 6 to 8 (scope).** The frames now keep rule 29 (older documents paired,
  standards taught first on modern anchors). May primary historical and scientific documents (Hammurabi, Cline,
  Pericles, the smallpox letters, Banneker, Carey and Jones and Allen, the 1906 texts) anchor where a standard's
  work is on them? Expert's pick: yes for documents, no change for literature.
- **Who writes the literary originals (money, people).** About 83 originals across the band (31, 29, 23), three
  novellas, three plays, about 20 poems, each read by a qualified ELA teacher; paid human writers for some?
- **The time a day (audience).** 50 minutes a day, home reading four nights, 15 minutes in class twice a week.
- **Readers (people, pay).** Chinese language and culture (G6 unit 1, Yu), Korean (G6 unit 4), African American
  history (G7 unit 3, G8 unit 2), Karuk and Yurok (G7 unit 6), Turkish or Persian tradition (G8 unit 4).
- **RL.8.9 religious works** (already with you, progression stitch item 11): unit 4 uses myths and folk tales only.

## Settled (for docs/reviews/DIGEST.md)

| Choice | Course | Reason |
|---|---|---|
| Older primary sources paired, standards taught first on modern anchors | ELA 6, 7, 8 | Rule 29; the band exception is Cory's |
| Unit 2 question on Hammurabi's self-portrait; prompt on posting a town's rules | ELA 6 | Distinct from social studies 6 unit 4's justice claim |
| Novella: a family that stays and chooses, not one that moves | ELA 6 | Grade 5 unit 1 had the start-over premise |
| Heroes decision carried by unit 1: a present-day hero, Yu the Great retold as the pair | ELA 6 | Cory 2026-11-12; Gilgamesh is social studies 6's |
| RI.6.9 on the Cline profile and the Weather Service's 1900 page, Cline's report third | ELA 6 | Rule 29 |
| Second research project in the last unit | ELA 6, 7, 8 | Rows ask for two or three |
| In-class reading 15 minutes twice a week; choice books from the Reading Room shelf | ELA 6, 7, 8 | Conferences need class time; a free source |
| Readiness tasks named per unit | ELA 6, 7, 8 | Lesson 5 |
| One more one-sitting narrative; 3, 3, 3 by pieces | ELA 6, 7, 8 | Narrative share |
| Klamath for the Elwha; Karuk and Yurok readers | ELA 7 | Biology unit 9 has the Elwha |
| Keats's Chapman's Homer sonnet for Sonnet 18 | ELA 7 | Grade 9 reads Sonnet 18 |
| Course-made film scene for RL.7.7, in unit 4 and again in unit 5 | ELA 7 | Film techniques; the owning unit first |
| Athens only; e6, e7, e8 reading-range rows aligned | ELA 7 | Expert settled; all ends match |
| Check 2 after unit 4 | ELA 7 | Even spacing |
| Drought maps from the federal drought information system | ELA 7 | Rights |
| 1896 marathon feature; legend taught as legend | ELA 7 | Question answerable from the unit |
| Nasreddin Hodja (Barnham) for Anansi | ELA 8 | Grade 4 reads Anansi |
| 4 days from unit 5 to unit 2 | ELA 8 | Load |
| Unseen independent reads in unit 5 and check 3 | ELA 8 | RL.8.10, RI.8.10 |
| Declaration read for word choice and response | ELA 8 | Grade 9 owns rhetoric |
| Unit 1 narrative a grade 7 review sample | ELA 8 | W.8.3 owned in unit 4 |
| Media work after civics unit 9 (about day 145) | ELA 8 | Same-year availability |
| Seneca Falls "(grade 10)" | ELA 8 | Grade 12 reads Walker's Appeal |

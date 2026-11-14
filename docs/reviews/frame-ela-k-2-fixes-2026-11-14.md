# Fixes: ELA course frames, kindergarten to grade 2, after the two cold reads (2026-11-14)

Applies the expert reads (`frame-english-language-arts-<c>-2026-11-14.md`) and the Codex reads (kindergarten:
`frame-english-language-arts-kindergarten-codex-rerun-2026-11-14.md`, the older blocked file set aside; grades 1 and
2: `frame-english-language-arts-grade-<n>-codex-2026-11-14.md`) to the three frames and `data/progressions/ela.csv`
(14 rows: 13 kindergarten to grade 2 rows and e3-fluency, notes and model columns only). Every expert finding and
every "Settled by the expert" row is applied; each Codex finding was weighed on its merits; the writers' "For the
lead" items were rewritten as settled or passed to Cory.

Gates after the fixes: `scripts/frame.py sync` (52 courses); `scripts/frame.py check
english-language-arts-kindergarten english-language-arts-grade-1 english-language-arts-grade-2` 0 failures each (each
4 units, 160 days, 154 in units, 6 for checks and respond days); `scripts/progression.py check ela` 374 rows, 0
failures; `scripts/stale.py check` 56 files, 0 failures. No unit count or unit day count changed. One skill moved
between units: ek-opinion (W.K.1) from kindergarten unit 4 to unit 1. The grade 3 frame was not edited: its Seams
table already names the band with scaffolding, the -tion, -sion, -able and -ous suffixes and "recordings of stories or
poems", which the grade 2 frame now hands on.

The base text was re-read for these fixes: the Skills Block cycle overviews for grades 1 and 2 (grade 1 C1 to C25,
grade 2 C1 to C26), the three curriculum maps for the performance tasks and unit assessments, and the decodables zips
(kindergarten modules 3 and 4: 13 readers and a poem; grade 1: 24 and a poem; grade 2: 25 and a poem).

**Licence (all three frames).** The open question is replaced by the fact and its source under each Base text
bullet: the 2017 K-2 Skills Block is CC BY 4.0 (EL's terms of use, store excerpt
licence/eleducation-terms-of-use-excerpt-2026-11-12.txt; the held 2019 printings carry the CC BY 4.0 line and no
NonCommercial line, NOTES.md "Skills Block answer"); only the 2024 Skills Block is CC BY-NC, not held and never used.

## Kindergarten

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | Settled by moving the row, not by rewording the check set: ek-opinion and W.K.1 now sit in unit 1, where the base text teaches and first checks opinion writing (module 1 unit 2, "Writing about the Classroom Toys We Prefer"). Unit 1's check set names that assessment; unit 4's opinion card is review |
| Expert | 2 | Applied | Source map rows for the module 3 and 4 decodables (adapted) and for the module and cycle overviews and program documents (teacher-facing, not carried) |
| Expert | 3 | Applied | Licence settled line under Base text; For the lead item rewritten as settled |
| Expert | 4 | Applied | Line under the Cross-subject table on what science kindergarten leans on, with W.K.1 now in ELA unit 1 |
| Expert | settled | Applied | All four rows |
| Codex | 1 | Applied in part | Each replacement read-aloud's text record is written with the scope and sequence and read by a qualified teacher (For the lead 4). Rejected: an anchor inventory before the frame is fixed (the frame brief puts text records with step 3, as in the grades 6 to 8 pass) |
| Codex | 2 | Applied | W.K.6 with at least two kinds of tool (typed class story in unit 2, drawing or audio tool in unit 4), each child's part recorded; ek-revise-publish notes match |
| Codex | 3 | Applied, differently | Codex would keep unit 1's opinion work formative pending Cory; the brief makes a unit move inside one course the fixer's call, so the row moved (expert 1) |
| Codex | 4 | Applied | Mid-year retell on a familiar unit 2 story, apart from the cold read-aloud |
| Codex | 5 | Applied | Half-day route keeps the first reading and purposeful returns; the scope and sequence names what is kept and shows the minutes fit. Whether the route is in scope is Cory's |
| Codex | 6 | Applied | Grade 1 frame's "Eight models" corrected to "Eleven" |
| Codex | 7 | Applied | With expert 3 |
| Codex | 8 | For the lead | Another file (`ela-open-material-2026-11-12.md`); closure text below |
| Codex | 9 | For the lead | Another file (`docs/agents/lenses/ela.md`); replacement text below |
| Writer | lead 1 | For Cory | The 120-minute day and the half-day route |
| Writer | lead 2 | Settled | Licence |
| Writer | lead 3 | Applied | ek-opinion to unit 1 with claim-evidence-reasoning introduced there in its first form; ek-author-reasons takes it as model_in in unit 4 |
| Writer | lead 4 | Settled / For Cory | Decodables adapted (settled); the readers are Cory's |

Counts: applied 13 (expert 1 to 4, Codex 1 in part, 2 to 7), rejected 0 (Codex 1's inventory timing in part), for
the lead 2 (Codex 8, 9), for Cory 2 (time a day, readers).

## Grade 1

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | Foundations sentences restated cycle by cycle: unit 1 review then short a, i, u, th, ch, sh, qu, plural -s (C1 to 4); unit 2 short o and e, y as long i, wh, -ck, doubled finals, -ed, l and r blends, final blends with -ng, -nk (C5 to 11); unit 3 closed and open syllables, silent e with endings and drop-e (C12 to 18); unit 4 new ar, or, er, ir, ur and vowel teams, two-syllable words (C19 to 25). Continued lines for e1-short-vowels, e1-inflections, e1-long-vowels and e1-syllables; checks limited to taught patterns |
| Expert | 2 | Applied | Performance tasks named as EL gives them (a magnificent thing for the classroom; "What the Sun Sees" narrative poems; bird riddle card and scientific drawing matching game; feathered friend saver), with the module 3 unit 2 informative assessment and module 4 unit 2 nest opinion kept; writing calendar and check sets match |
| Expert | 3 | Applied | Table matches the rows: e1-connections 1-ESS1-1; e1-informative 1-LS1-1 added; e1-shared-research recoded 1-LS1-1; e1-main-topic lean dropped, the sky and bird texts kept as topic connections |
| Expert | 4 | Applied | L.1.5c named in unit 1; the clearing-confusion phrase relabelled SL.1.1c, SL.1.3, SL.1.2 kept on key details |
| Expert | 5 | Applied | Source map rows for decodables, Learning Letters and the overviews |
| Expert | 6 | Applied | Licence settled line |
| Expert | 7 | Applied | The long text is read in module 4 unit 1's lessons in place of its two trade-book stories, with a second short bird story for RL.1.9, so it adds no days |
| Expert | settled | Applied | All seven rows (module 4 to unit 4 only; the sun and moon tale named as an Efik and Ibibio tale of southern Nigeria, Dayrell 1910) |
| Codex | 1 | Applied | With expert 1; "Where a row sits" rewritten (row in the unit where its thread opens, later units "continued" with cycles, full check where the last pattern is taught) |
| Codex | 2 | Applied in part | The second tale named (the Chinese weaver girl and cowherd); the base text's own module 4 texts named and adapted; text records with the scope and sequence. Inventory before the frame rejected, as kindergarten |
| Codex | 3 | Applied | With expert 3, with weeks and "if later" lines |
| Codex | 4 | Applied | Social studies unit 3 teaches a written claim through shared writing and a sentence frame about week 8; the ELA row and paragraph say so and that ELA checks W.1.1 later |
| Codex | 5 | Applied | L.1.4 multiple-meaning words in unit 4; e1-word-strategies notes match |
| Codex | 6 | Applied | "Eleven models"; paragraph-frame introduced by e1-informative in unit 1, e1-opinion model_in |
| Codex | 7 | For the lead | Another file (`ela-open-material-2026-11-12.md`); same closure as kindergarten Codex 8 |
| Codex | 8, 9 | For the lead | Other files (the science grade 1 reviews); text below |
| Writer | lead 1 | For Cory | Time a day |
| Writer | lead 2 | Settled | Licence |
| Writer | lead 3 | Applied | e1-opinion notes "Uses the paragraph-frame introduced in e1-informative", model_in "claim-evidence-reasoning; paragraph-frame" |
| Writer | lead 4 | Settled / For Cory | Decodables adapted; readers Cory's |

Also applied from the brief: W.1.6 with two kinds of tool (typed class book in unit 2, drawing or audio tool in unit 4).

Counts: applied 13 (expert 1 to 7, Codex 1, 2 in part, 3 to 6), rejected 0 (Codex 2's inventory timing in part),
for the lead 3 (Codex 7 to 9), for Cory 3 (time a day, readers, the device assumption).

## Grade 2

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | Foundations sentences by Skills Block module, one per unit: unit 1 syllable types and long-vowel teams reviewed (C1 to 5); unit 2 r-controlled review (C6), then oi, oy, ou, ow, ild/old/ind/ost, doubling, -ed, oo/ou/ui/ue/ew, -tion, -sion (C7 to 12); unit 3 consonant-le, -k/-ck/-ic with un- and re-, -dge/-ge, -ch/-tch with -er/-est, -ible/-able, au and aw (C13 to 19); unit 4 new -ies, schwa with de-, dis-, im-, in-, -ate, compound words, -cal/-cle, -ous/-us (C20 to 26), then review and fluency. The expert's unit 1 "cycles 1 to 6" follows the module boundary instead (C6 opens module 2), and un- and re- sit in C15 as the overview gives, not cycles 7 to 12. Continued lines for e2-vowel-teams (units 2 and 3, completing RF.2.3b), e2-tricky-spellings and e2-prefixes-suffixes (units 3 and 4). Source map renamed, module 3 to unit 3 only |
| Expert | 2 | Applied | Unit 3: research notes into a written informative paragraph (W.2.7, W.2.8; W.2.2, W.2.5 review), then the poster and oral presentation; then a story told from a pollinator's view, recorded as audio with drawings (SL.2.4, SL.2.5, SL.2.6). Grade 3 seam holds |
| Expert | 3 | Applied | RL/RI.2.10 at the full band with scaffolding at the high end; end check reads a band text alone, a harder one with support, recorded apart |
| Expert | 4 | Applied | The seven row leans rebuilt with weeks and "if later" lines; e2-main-topic-paragraphs' 2-ESS1-1 kept as a topic connection only |
| Expert | 5 | Applied | Lead item 4 rewritten: the module 4 overview zip is the grade 1 file; C20 to C26 held and read |
| Expert | 6 | Applied | L.2.2a with geographic names (invented product names kept), L.2.2b greetings and closings, L.2.4e print and digital glossaries and beginning dictionaries |
| Expert | 7 | Applied | paragraph-frame carried from e1-informative |
| Expert | 8 | Applied | Source map rows for decodables, Learning Letters (optional; cursive is not a grade 2 standard) and overviews; licence line |
| Expert | settled | Applied | All eight rows, including the lizard tale retold from the traditional Mexican tale and the hummingbird tale credited with care |
| Codex | 1 | Applied in part | Module-boundary mapping, cycle-by-cycle text, unit 4 as new teaching, checks on taught patterns only. Rejected: moving e2-vowel-teams and the affix rows to their completing units for Cory. The expert settled "continued" lines, and every K to 2 frame now places a foundations row where its thread opens |
| Codex | 2 | Applied | Recording is a story (the bee story's model); the formal and informal lines compared (L.2.3a); "a live telling alone leaves SL.2.5 unfinished" |
| Codex | 3 | Applied | With expert 3; independent and supported evidence kept apart |
| Codex | 4 | Applied | With expert 2; unit 4 returns to gathering from provided sources before the seed packet |
| Codex | 5 | Applied in part | Higher-band supported student reading in units 3 and 4; text records with the scope and sequence. Inventory before the frame rejected |
| Codex | 6 | Applied | Unit 1 reason now extends grade 1's chapter story; e3-fluency and e2-rhythm-and-meaning notes fixed in the CSV |
| Codex | 7 | Applied | With expert 4; Codex's weeks used (social studies culture and migration about week 24 or later, not guaranteed before ELA unit 4; the expert's "first half" timing was wrong) |
| Codex | 8 to 12 | For the lead | Another file (`frame-science-grade-2-codex-2026-11-14.md`); text below |
| Writer | lead 1 | For Cory | Time a day |
| Writer | lead 2 | Settled | Licence |
| Writer | lead 3 | For Cory | Readers |
| Writer | lead 4 | Rewritten | Expert 5 |

Also applied from the brief: the four performance tasks named as EL names them ("The Most Important Thing about
Schools" informational book; illustrated fossil narrative; the plants and pollinators poster and presentation;
wildflower seed packet), and W.2.6 with two kinds of tool.

Counts: applied 15 (expert 1 to 8, Codex 1 in part, 2 to 4, 5 in part, 6, 7), rejected 1 (Codex 1's ownership move;
Codex 5's inventory timing in part), for the lead 5 (Codex 8 to 12), for Cory 2 (time a day, readers).

## Progression changes (`data/progressions/ela.csv`)

| Row | Change |
|---|---|
| ek-opinion | model_in emptied; introduces claim-evidence-reasoning in its first form, taught and first checked in module 1, used again in module 4 |
| ek-author-reasons | model_in claim-evidence-reasoning; notes say it uses the model from ek-opinion |
| ek-emergent-reader | Decodables: the 2017 Skills Block readers (CC BY 4.0) adapted where pictures are cleared, gaps written new |
| ek-revise-publish, e1-revise-publish, e2-revise-edit | At least two kinds of digital tool across the year, each child's part recorded ("explore a variety" in kindergarten) |
| e1-opinion | model_in "claim-evidence-reasoning; paragraph-frame"; notes "Uses the paragraph-frame introduced in e1-informative" |
| e1-informative | "Introduces paragraph-frame" |
| e1-word-strategies | L.1.4 multiple-meaning words added |
| e1-inflections | Cycle list (plural -s C4, -ing and -s C7, -ed C8 and 9, endings on silent-e words C15 to 18) |
| e2-prefixes-suffixes | un- and re- (C15), dis- and de- (C21), im- and in- (C22) |
| e2-rhythm-and-meaning | Boundary: grade 3 literal and nonliteral; grade 4 simple similes and metaphors (L.4.5a) |
| e2-tell-and-record | A story told from a pollinator's view, recorded with drawings (unit 3) |
| e3-fluency | Other end of that handoff: grade 2 made recordings of stories or poems; grade 3 adds poetry read aloud and recorded reading made fluent |

## Cross-subject notes (for the frames' owners; not edited here)

- **Science kindergarten** (`docs/courses/science-kindergarten/frame.md`, about lines 136 to 137): says ELA teaches
  W.K.1 in unit 4. It is now ELA unit 1 (weeks 1 to 7); science's drawn opinion about week 20 follows it. Replace
  "unit 4" with "unit 1".
- **Social studies kindergarten** (`docs/courses/social-studies-kindergarten/frame.md`, about line 127): "ELA's drawn
  or written opinion can come later in the year". It now comes in ELA unit 1, with or just after week 2.
- **Social studies grade 1**: no change needed; its written claim through shared writing is what the ELA frame now
  records.
- **Science grade 2 and social studies grade 2**: no change needed; the ELA table now matches their calendars.

## For the lead

1. **Kindergarten Codex 8 and grade 1 Codex 7, `docs/reviews/ela-open-material-2026-11-12.md`.** Add beside the
   summary, the 2017 Skills Block row and open items 1 and 2: "Closed 2026-11-14: the stored terms excerpt and the
   printed notices in the held 2017 files establish CC BY 4.0, third-party items excepted; the 2024 edition stays
   excluded. Picture clearance for the decodables is still open." (Codex dated it 2026-11-13; the frames settled it
   today.)
2. **Kindergarten Codex 9, `docs/agents/lenses/ela.md`, "What this lens does not cover".** Replace the parenthesis
   with: "RUBRIC-ELA.md summarizes grades 3 to 12. Separate K to 2 criteria were consulted in
   progression-ela-codex-2026-11-13.md (phonemic awareness, phonics order, aligned decodables); that report states
   its reading limits."
3. **Grade 1 Codex 8 and 9, the science grade 1 reviews** (`frame-science-grade-1-2026-11-14.md` and its Codex file):
   add a dated note beside each "ELA frame not yet written" line: "Superseded 2026-11-14: the grade 1 ELA frame exists
   (docs/courses/english-language-arts-grade-1/frame.md); e1-informative and e1-shared-research lean on 1-LS1-1,
   e1-connections on 1-ESS1-1, with if-later lines."
4. **Grade 2 Codex 8 to 12, `docs/reviews/frame-science-grade-2-codex-2026-11-14.md` lines 22, 160, 178, 215, 259.**
   Add Codex's dated dispositions as written in its report (the grade 2 ELA frame exists; discussion unit 1, narrative
   and revision unit 2, research unit 3, opinion unit 4).
5. **The two Cross-subject notes above** go to the science kindergarten and social studies kindergarten frames at their
   next fix pass.
6. **Store refresh**: fetch the grade 2 module 4 Skills Block module overview (the held zip is the grade 1 file).

## For Cory

- **Time a day:** about 120 minutes of ELA in kindergarten to grade 2 against 90 in grade 3, and whether a half-day
  kindergarten route is in scope (scope and audience).
- **Qualified readers:** a kindergarten, grade 1 and grade 2 ELA teacher for the replacement texts (about 22, 28 and
  20) and the adapted decodables, and any pay (people and money).
- **Cultural readers:** the Kenya tree-planting account (kindergarten); the Efik and Ibibio sun and moon tale and the
  Chinese weaver girl tale (grade 1); the grade 2 school texts from several countries, the Quechua hummingbird tale and
  the Mexican lizard tale; any pay.
- **Devices:** the K to 2 shared-device assumption for W.K.6, W.1.6, W.2.6 and SL.2.5 (grade 1 Codex).

## Settled (for DIGEST.md)

| Choice | Reason | File |
|---|---|---|
| The 2017 K-2 Skills Block is CC BY 4.0 and the foundations base; only the 2024 edition is CC BY-NC, never used | EL terms excerpt; printed lines in the held files | K, 1, 2 frames |
| 2017 Skills Block decodables adapted where pictures are cleared, gaps written new | CC BY 4.0; aligned to the cycles | K, 1, 2 frames; ek-emergent-reader |
| W.K.1 (ek-opinion) in kindergarten unit 1, introducing claim-evidence-reasoning | Base text teaches and checks it in module 1 | K frame; ela.csv |
| paragraph-frame introduced by e1-informative, used by e1-opinion | Unit order | grade 1 frame; ela.csv |
| Foundations rows sit where their thread opens, later units name them continued with cycles, checks only on taught patterns; one Skills Block module per unit | Cycle overviews read | K, 1, 2 frames |
| Performance tasks named as EL names them, kept | Curriculum maps | K, 1, 2 frames |
| Grade 2 unit 3 keeps the written informative paragraph and adds a recorded pollinator story with drawings | W.2.7, SL.2.4, SL.2.5 in full; grade 3 seam | grade 2 frame; e2-tell-and-record |
| RL/RI.2.10 at the full grades 2 to 3 band, independent and supported kept apart | Standard wording | grade 2 frame |
| W.K.6, W.1.6, W.2.6 with at least two kinds of tool across the year | "a variety of digital tools" | K, 1, 2 frames; ela.csv |
| Grade 1 long text read in module 4 unit 1's lessons in place of its two trade books | Days by load | grade 1 frame |
| Cross-subject tables match the rows' leans; unmatched leans become topic connections | ela.csv | K, 1, 2 frames |

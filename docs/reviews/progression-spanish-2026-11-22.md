# Expert cold read: the Spanish progression (Levels 1 to 4), 2026-11-22

Job: docs/pipeline/briefs/progression-read.md, with "grade" read as "level" (L1 to L4). Read blind: no earlier
world languages review was opened. Acting also as the expert world languages teacher and the sensitivity reader.

## What was read

- data/progressions/spanish.csv (51 rows: L1 13, L2 13, L3 13, L4 12), spanish-edges.md, spanish-excluded.csv (11 rows).
- data/standards/actfl-wrs.txt (22 ids) and data/standards/spanish-strands.txt (SPA.Sounds.1 to 11).
- docs/courses/world-languages/STANDARD.md and APPROACH.md, in full.
- docs/agents/EXPERT.md, docs/agents/lenses/world-languages.md, docs/ADOPTION-BAR-SUBJECTS.md ("The shared core" and
  part 6).
- Our own-words notes on the 2024 proficiency guidelines (written for the progression writer, kept outside the repo).
  The guidelines PDF itself was not reopened; the notes were enough for every point below.
- The ten leaned-on ELA and social studies rows, plus ss2-nation-of-immigrants and us1-immigration, in
  data/progressions/ela.csv and social-studies.csv.
- Gate: `python -X utf8 scripts/progression.py check spanish`: 51 rows, 0 failures. `scripts/plan.py check` was not
  run (the batch rules forbid it); the progression gate is the one the brief names as the fallback.

## Verdict

The progression is sound in shape: every World-Readiness id is owned at Level 1 and carried with a real "Harder than"
ladder that tracks the guidelines' functions, contexts, text types and accuracy closely, the sounds strand is complete
and ordered, and the sensitivity notes (no status, home language or family-work questions, heritage learners never the
translator) are better than most published programs. The biggest risk is dose: at about 63 hours a level, the Level 3
and Level 4 exits (Intermediate Mid, Intermediate High) and the grammar loaded onto them sit well above what the hours
are known to buy, and two rows describe Advanced Low control as a Level 4 aim. The one change that matters most is a
call by Cory on the exits or the dose (For Cory, question 1); until then the rows should say plainly that a sublevel
is a proficiency estimate, not a "performance aim" (finding 2), and Levels 1 and 2 need an unrehearsed exchange on the
Check day (finding 3), which the bar names as a fail.

## Findings, most serious first

### 1. The Level 3 and 4 exits and grammar load are above what 63 hours a level supports
- Rows: l3-interpersonal, l3-interpretive, l3-presentational, l4-interpersonal, l4-interpretive, l4-presentational;
  the grammar lists in l2-interpersonal, l3-interpersonal, l4-interpersonal.
- Problem: four levels of about 63 hours make about 250 hours in all, less than two years of a typical daily high
  school class (about 140 hours a year). From memory (the performance ranges ACTFL published with its 2012
  performance descriptors; not reopened, and the CASLS hours page in APPROACH "Pacing" is a PDF this read could not
  open without a download): learners in a cognate language such as Spanish typically reach the Novice range after two
  school years and Intermediate Low to Mid after four. On that evidence Level 1 at Novice Mid and Level 2 at Novice High
  are reachable as performance on taught themes; Level 3 at Intermediate Mid is a stretch; Level 4 at Intermediate
  High (Advanced work much of the time) is not supported by the hours. The grammar lists match it: l2-interpersonal
  holds about a full first-year textbook (all three present conjugations, five irregulars, stem changers, reflexives,
  ir a, time, numbers to 1,000), and l4-interpersonal holds preterite against imperfect, future, conditional,
  subjunctive and relatives, a typical third-year load. A writer will build days that cannot be taught in the time.
- Fix: Cory chooses (For Cory, question 1). Whatever he picks, keep the honest line already in APPROACH "Pacing and
  dose". If the exits are lowered (the pick), edit: l3 comm rows "Intermediate Mid" to "Intermediate Low"; l4 comm
  rows "Intermediate High" to "Intermediate Mid"; rewrite each "Harder than" ladder one step down using the notes'
  sublevel descriptions; in l4-interpersonal change the grammar line to "preterite and imperfect both used in a story,
  slips expected; the future, the conditional and the present subjunctive met as chunks (iré, me gustaría, quiero que,
  es importante que, ojalá), not as paradigms; relative que and donde"; mark the full preterite and imperfect contrast
  and the productive subjunctive as "beyond Level 4".
- LAYER: progression (and standard, section 5). REPEAT: new. Confidence: likely (one remembered source and the hour
  arithmetic).

### 2. A sublevel is called "a performance aim", which the guidelines and STANDARD section 5 rule out
- Rows: all 12 Communication rows (l1 to l4, interpersonal, interpretive, presentational).
- Problem: each opens "Exit aim for this mode: Novice Mid ... a performance aim the course works toward". Performance
  has major levels only; sublevels belong to proficiency. STANDARD section 5 says a sublevel exit is "the proficiency
  estimate a course aims toward". A writer reading "performance aim" will write look-fors that claim to show Novice Mid
  on a Check day, which our checks cannot do.
- Fix: in all 12 rows replace "a performance aim the course works toward and never a rating any Curio Class check
  gives (no proficiency interview)" with "the proficiency estimate the course aims toward; the checks judge performance
  on the taught themes in the Novice range and never give a rating (no proficiency interview)" (write "Intermediate
  range" in the L3 and L4 rows).
- LAYER: progression. REPEAT: new. Confidence: firm (the guidelines notes, section 2, and STANDARD section 5 agree).

### 3. Levels 1 and 2 have no unrehearsed two-way task (a bar "fails if")
- Rows: l1-interpersonal, l2-interpersonal.
- Problem: part 6 fails a course with "no unrehearsed two-way task". L3 and L4 name one on the Check day; L1 and L2
  describe only practiced card exchanges. At Novice the language is rehearsed, but the content can still be new.
- Fix: add to each row after the information-gap sentence: "On the Check day the pair uses a new card neither has
  seen: rehearsed language, unrehearsed content."
- LAYER: progression. REPEAT: new. Confidence: firm (bar part 6, the lens).

### 4. Level 4 presentational asks for Advanced Low control
- Row: l4-presentational.
- Problem: "narrating a past event with preterite and imperfect kept apart" and "proposing a change with future and
  subjunctive forms" describe control of aspect, which the guidelines place at Advanced Low; Intermediate High writing
  shows weakness exactly when time frames shift (the row's own accuracy line says so, so it contradicts itself).
- Fix: replace with "narrating a past event, preterite and imperfect both attempted, with slips when the time frame
  shifts, and proposing a change with taught chunks (recomiendo que, es importante que, iré)". If finding 1 lowers
  the exit, also change "two to four short paragraphs" to "one or two short paragraphs, not yet sustained".
- LAYER: progression. REPEAT: new. Confidence: firm.

### 5. One exit for all three modes at Level 3 and 4 (writer's choice 1)
- Rows: l3-presentational, l4-presentational.
- Problem: STANDARD section 5 says the exit is stated per mode, and the guidelines note the common pattern of
  listening and reading ahead of writing. All three modes carry the same sublevel, so the per-mode rule is met in
  form only. Presentational speaking can keep the level's aim; presentational writing usually lags.
- Fix (settled, see the table): in l3-presentational and l4-presentational add "Writing aims one sublevel below
  speaking (Intermediate Low at Level 3, Intermediate Mid at Level 4)", or one below whatever exit Cory sets in
  question 1. Keep the single aim at Levels 1 and 2, where writing at Novice is lists and forms anyway.
- LAYER: progression. REPEAT: new. Confidence: likely.

### 6. Early-years companion lines: a writing contradiction and nine rows with no line (writer's choice 6)
- Rows: l1-interpersonal ("with no writing asked") against l1-presentational ("draws and labels a picture") and the
  Novice Mid writing aim (fill a form, write words from memory). No companion line: l1-cult-products, l1-conn-info,
  l1-comp-language, l1-commu-school, l2-cult-products, l2-conn-info, l2-comp-language, l2-commu-school,
  l2-commu-lifelong.
- Problem: a companion "uses that level's rows" (STANDARD section 6), so every L1 and L2 row needs a way a young child
  meets it. The rows without one are the most literacy-bound (punctuation fixing, a facts chart, a self-check), and a
  kindergartner may not yet read or write in any language. Short lines are fine at this layer; missing ones are not.
- Fix: add one line to each listed row (settled wording in the table below), and state the companion's writing aim
  once in l1-presentational: "Early-years companion writing: copy and label, as far as the child writes in any
  language; listening and speaking aim at the level's target" (the target itself is Cory's, question 3).
- LAYER: progression. REPEAT: new. Confidence: likely.

### 7. The range of places leans away from the United States, the Caribbean and Africa
- Rows: l1-cult-products, l2-cult-products, l3-cult-products, l4-cult-products, l3-conn-info, l4-cult-practices.
- Problem: named places are Chile, Argentina, the Andes, Peru, Paraguay, Uruguay, Spain and Central America in
  general. Mexico appears only as the source of loanwords, Equatorial Guinea only on a map, Afro-Latin communities not
  at all, and Spanish-speaking communities in the United States (one of the largest Spanish-speaking populations in
  the world) only as old place names. Keeping tasks off immigration (finding 13) does not require leaving US
  Spanish speakers out; leaving them out makes Spanish "foreign", which a heritage learner notices (C12, lens:
  one group carrying the examples).
- Fix: l3-cult-products: after "cumbia, salsa, son" add "and their African roots"; add "murals in US cities made by
  Mexican American and Puerto Rican artists" to the mural line. l4-cult-products: add "a writer or musician from
  Equatorial Guinea or the Caribbean" to the product list. l2-cult-products: add "Spanish-language radio, signs and
  murals in US cities today" beside the old place names. l3-conn-info: make one of the two views "a Spanish-language
  source from the United States" in at least one unit. l4-cult-practices: add "Afro-descendant communities on the
  Caribbean and Pacific coasts" to the languages-and-identity line. Mexico: name it as a source place in at least one
  L2 and one L3 text list.
- LAYER: progression. REPEAT: new. Confidence: judgment call (no fact is wrong; the balance is).

### 8. Heritage path: how a learner joins it, and "records"
- Rows: l1-interpersonal, l1-presentational.
- Problem: no row says how a learner comes onto the heritage path, so a writer may open a unit with "who speaks
  Spanish at home?", which the teacher note forbids. l1-presentational says the learner "records the school register
  beside the home register"; "records" reads as audio, which promise 2 bars.
- Fix: l1-interpersonal teacher note, add "The heritage path is offered when a learner's work shows it (the
  teacher's judgment or the school's placement), never by asking the class who speaks Spanish at home."
  l1-presentational: "records" to "writes".
- LAYER: progression. REPEAT: new. Confidence: firm.

### 9. Describing a person
- Row: l1-interpersonal (theme "describing a person or a character").
- Problem: a writer may set "describe your partner", which invites comments on a classmate's body, skin or clothes.
- Fix: add to the teacher note "descriptions are of a character, a picture or oneself, never a classmate's body or
  looks."
- LAYER: progression. REPEAT: new. Confidence: likely.

### 10. Culture facts from memory: four to tighten, the rest correct
Checked from memory (no source opened; firm where it is common reference knowledge):
- Correct as written: the Chile and Argentina school year (about March to December); double shifts in some schools;
  the pharmacist as a first stop for a minor illness in many places; the minga as shared community work in the Andes
  (from Quechua); chocolate and tomate from Nahuatl (the exact source word of chocolate is debated; "from Nahuatl" is
  safe); cancha from Quechua; Guaraní in Paraguay and Quechua in Peru as official languages beside Spanish; 18
  Spanish-official countries in Latin America plus Puerto Rico, Spain and Equatorial Guinea.
- l1-cult-products: "the 18 countries of Latin America" reads as if Latin America has 18 countries (Brazil, Haiti and
  others are not counted). Fix: "the 18 Spanish-speaking countries of Latin America, Puerto Rico, Spain and Equatorial
  Guinea".
- l1-cult-practices: "two surnames on a form" is not universal (in Argentina one surname is common). Fix: "two
  surnames on a form in many places".
- l3-cult-practices: the voseo list leaves out Paraguay and the voseo of parts of Colombia, Chile and elsewhere. Fix:
  "with voseo in Argentina, Uruguay, Paraguay and much of Central America, and in parts of Colombia, Chile and other
  places, as a variety".
- l3-sounds-varieties: seseo is general in Latin America, not "most", and also in the Canary Islands and parts of
  southern Spain; the sh of Buenos Aires is shared with Montevideo and is also said as zh. Fix: "s said where much of
  Spain says th, in all of Latin America, the Canary Islands and parts of southern Spain; ll and y said alike in most
  places, and as sh or zh in Buenos Aires and Montevideo".
- LAYER: progression. REPEAT: new. Confidence: firm on the facts, from memory.

### 11. Spanish accuracy in words and the strand file
- Rows: l1-sounds-letters, l1-interpretive, l2-interpersonal, l3-presentational; data/standards/spanish-strands.txt
  SPA.Sounds.3.
- Problems and fixes:
  - l1-sounds-letters words "la uve": with a Latin American default the usual name is "la ve" (also "ve corta");
    "uve" is the Spain name. Fix: "la ve (la uve in Spain)".
  - "la elle" and SPA.Sounds.3 call ll a letter; in the current alphabet it is a pair of letters (a digraph). Fix
    SPA.Sounds.3 to "Say and spell the letters h, j, ñ and v and the pair ll, which sound unlike English." and in
    the l1 note "the letters ... and the pair ll".
  - l1-interpretive words "¿qué hora es?" and "a short spoken announcement of numbers or times": telling time is
    taught at L2 (l2-interpersonal). Fix: replace with "¿qué día es hoy?" and "numbers or dates".
  - Gender in words: l2-interpersonal "estoy cansado" to "estoy cansado / cansada"; l3-presentational "cuando era
    niño" to "cuando era niño / niña".
- LAYER: progression and standard (the strand file). REPEAT: new. Confidence: firm.

### 12. Grammar placement (writer's choice 2): keep, with commands added
- Rows: l2-interpersonal, l2-interpretive, l3-interpersonal, l4-interpersonal.
- Judgment: the order is right: chunks of gustar, tener and ser at L1; present paradigms, estar for place and feeling,
  ir a at L2; preterite from L3 with the imperfect as chunks; object pronouns at L3; the contrast, future, conditional
  and a high-frequency subjunctive at L4. Quisiera and ¿me podría decir? are rightly taught as chunks before their
  paradigms. The load per level is the problem (finding 1), not the order. One gap: informal (tú) commands are
  missing, though L2 follows recorded directions and L3 reads recipes, both written in them.
- Fix: l2-interpretive grammar or words: add "tú commands met as chunks in directions (dobla, sigue, mira)";
  l3-interpersonal: "usted and tú affirmative commands"; l4-interpersonal: "negative commands, with the subjunctive
  form, as chunks (no te preocupes)".
- LAYER: progression. REPEAT: new. Confidence: likely.

### 13. Linking at Level 4 is late; varieties at Level 3 is right (writer's choice 4)
- Rows: l3-sounds-varieties, l4-sounds-linking.
- Problem: L3 interpretive already asks learners to follow station announcements and authentic clips, which are
  impossible to follow without hearing words run together. Owning SPA.Sounds.10 at L4 leaves the L3 listening rows
  without the skill they rest on. SPA.Sounds.11 at L3 is right: learners hear several varieties from L1 (the L1 note
  already says varieties are never errors), and naming the features needs the L2 sound work.
- Fix (settled): move SPA.Sounds.10 to l3-sounds-varieties (standard becomes "SPA.Sounds.11; SPA.Sounds.10;
  ~SPA.Sounds.3", note adds "hearing words run together at natural speed, vowel to vowel and consonant to vowel");
  l4-sounds-linking standard becomes "~SPA.Sounds.10; ~SPA.Sounds.7; ~SPA.Sounds.11", note opens "Harder than Level
  3: reading a paragraph aloud with linking and stress, and following connected speech at natural speed across
  varieties". The gate allows a strand owned at any level.
- LAYER: progression. REPEAT: new. Confidence: likely.

### 14. The immigration leans left out (writer's choice 3): keep, but say so in STANDARD
- Rows: none in the CSV; STANDARD.md section 6.
- Judgment: keep. The leans are teacher pointers only, and ss2-nation-of-immigrants and us1-immigration are about
  immigration itself, which a language task does not need. ss2-culture-migration and ss4-regional-cultures, which are
  kept, also touch migration; their teacher notes ("the parts of a culture only; no task asks how or why a family
  moved") are enough. This does not need Cory: it is a pointer choice inside the sensitive-ground rule he has already
  set. It does leave STANDARD listing two leans no row uses (finding 16).
- LAYER: standard. REPEAT: new. Confidence: likely.

### 15. Communities 5.1 is thin by design (writer's choice 5)
- Rows: l1 to l4 commu-school.
- Problem: the rows keep everything inside school and public media, which follows the "no contact outside school"
  rule and the bar's Unsupported line. The standard's "beyond the classroom" and "global" interaction is then met
  only in part, and C1 fails a standard "taught below its wording". This is a door criterion.
- Fix: one of the options in For Cory, question 2. Until then, add to l1-commu-school's teacher note: "The course page
  names the part of this standard not claimed (interaction with communities beyond the school)."
- LAYER: progression and standard. REPEAT: new. Confidence: likely.

### 16. Stale lines now that the Spanish progression exists
STANDARD.md:
- Table at the top, row "Strand id files ...", State column: "Spanish: data/standards/spanish-strands.txt and the
  gate entry made 2026-11-22 (no progression rows)" to "Spanish: data/standards/spanish-strands.txt, the gate entry
  and the progression (data/progressions/spanish.csv, 51 rows, written 2026-11-22). ASL: not made; it waits on
  question 4 (data/plans/later.csv L93)".
- Section 6, first paragraph: "In a progression for this subject (not written; none exists)" to "In a progression for
  this subject (Spanish: data/progressions/spanish.csv, 2026-11-22; ASL: none, waiting on question 4, data/plans/
  later.csv L93)".
- Section 6, "Ownership for the gate": "and the ladder is written with the progression" to "and the ladder is the
  "Harder than Level N" note on each row of data/progressions/spanish.csv".
- Section 6, "What scripts/progression.py does": "file data/progressions/spanish.csv (not written; none exists)" to
  "file data/progressions/spanish.csv (51 rows, with spanish-edges.md beside it)". Keep "ASL has no entry; it waits
  on question 4" and add "(data/plans/later.csv L93)".
- Section 6, "Cross-subject leans", social studies line: after "`us1-immigration`," add "(the Spanish progression
  uses neither, to keep tasks off immigration; spanish-edges.md lists the leans in use)".
APPROACH.md:
- "What world languages add", unit field 3: "one cross-subject link by row id (STANDARD section 6)" to "one
  cross-subject link by row id (for Spanish, the leans in data/progressions/spanish-edges.md; STANDARD section 6)".
Outside the two pages (for the caller, not required by the brief):
- docs/agents/lenses/world-languages.md, Sources: "ACTFL Proficiency Guidelines, 2024: by search summary; not read in
  full" to "ACTFL Proficiency Guidelines, 2024: read in full 2026-11-22 from a copy outside the repo (our notes only)".
- docs/ADOPTION-BAR-SUBJECTS.md part 6, "Two courses today, each 'all levels'" is still true of data/courses.csv, so
  it is not stale yet; it becomes stale when the Option D rows are drawn.
- LAYER: process. REPEAT: new. Confidence: firm.

## The rest of the brief's checks

- **Ownership:** all 11 WRS ids owned at L1 and carried; SPA.Sounds.1, 2, 3, 8, 9 at L1, 4, 5, 6 at L2, 7 and 11 at
  L3, 10 at L4 (finding 13 moves it to L3). Each owner is the right level for the sound order. Nothing is owned in
  part with the rest lost.
- **Coverage:** every WRS id and every SPA.Sounds id is named; the 11 ACTFL ids are excluded with a reason. Met.
- **assumes and hands_on:** every assumes is the same strand one level down; every hands_on is picked up at the next
  level; no level is skipped. Met.
- **Models:** sentence-frame and info-gap-card (L1), comparison-chart and sound-spelling-map (L1), word-parts (L2),
  story-map and paragraph-frame (L3), goal-plan (L1) each appear before use. Met.
- **Words:** taught before use and at the level, except "¿qué hora es?" at L1 (finding 11). Repeats across levels
  (la guía, la fuente, el punto de vista) are review, which is right.
- **cross_subject:** all ten leans name a real row; the grade 6 and later leans sit at L3 and L4. Met. The lean of
  l1-conn-making on grade 3 map reading reaches back from an early-years companion child in K to 2; the unit reteaches
  it, so no change.
- **Pace:** 13, 13, 13, 12 rows. Even. The weight problem is inside rows (finding 1), not in row counts.
- **Lens checklist (progression layer):** a level with a stated target: met (wording, finding 2). Themes with tasks,
  not grammar topics: met. Three modes with a linked task: met at this layer (each unit's link is the unit plan's).
  Standard ids real, no can-do text copied: met. Information gap in every exchange: met; unrehearsed at L1 and L2:
  missed (finding 3). Home language transfer as a reason: met. Heritage path, never translator: met (entry, finding
  8). Vosotros off by default and varieties never corrected: met. One country carrying the examples: part missed
  (finding 7). ASL items: not applicable.
- **Stale notes:** `scripts/stale.py check` passes on STANDARD.md and APPROACH.md; the unmarked stale lines are in
  finding 16.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Presentational writing one sublevel below speaking at L3 and L4 (finding 5) | Guidelines' common pattern; STANDARD's per-mode rule | data/progressions/spanish.csv |
| Unrehearsed card on the L1 and L2 Check day (finding 3) | Bar part 6 fail line | spanish.csv |
| SPA.Sounds.10 owned at L3, carried at L4 (finding 13) | L3 listening rests on it | spanish.csv |
| Tú commands as chunks at L2, negative commands as chunks at L4 (finding 12) | Directions and recipes use them | spanish.csv |
| Word and fact fixes (findings 10, 11) | Plain errors | spanish.csv, spanish-strands.txt |
| Companion lines (finding 6): l1-cult-products "a song and a game, and pointing to places on a big map"; l1-conn-info "a picture weather chart filled by pointing and stickers"; l1-comp-language "sorting picture cards of look-alike words, and drawing the ¿ and ¡ in the air"; l1-commu-school "singing for a younger class"; l2-cult-products "handling play coins and a craft shown by its maker"; l2-conn-info "a picture fact sort from a short read-aloud"; l2-comp-language "matching word endings on picture cards"; l2-commu-school "a class song or poster for a school event"; l2-commu-lifelong "a sticker chart of songs and stories the child can follow" | The companion uses the row, so it needs a way in | spanish.csv |
| Keep the immigration leans out (finding 14) | Pointer choice inside the existing sensitive-ground rule | STANDARD.md section 6 |
| Keep varieties at L3 (finding 13) | Rests on the L2 sound work | none |

## What is right and should not be touched

The "Harder than Level N" ladders, which follow the guidelines' four criteria row by row; the information gap in every
exchange; the heritage path in every Communication row, with spelling and register work and no translator role; the
teacher notes on family, home, status and income; varieties never errors; chunks before rules; frames withdrawn on a
named day; culture as practices, products and perspectives, varied inside each place; ACTFL level ids excluded as a
scale.

## What it could not judge

Hours to proficiency at source (the CASLS page and ACTFL's performance range chart are PDFs; reading them would need
a download, so they were left); finding 1 rests on memory until a person opens them in the browser. Whether the
named themes fit an early-years child at Level 2 in practice (needs a teacher of young learners).

## Sources

- Our own-words notes on the ACTFL Proficiency Guidelines 2024 (outside the repo): sublevel descriptions, performance
  against proficiency, the per-skill rating.
- docs/ADOPTION-BAR-SUBJECTS.md part 6 and C1, C12: the fail lines and the range rule.
- From memory: ACTFL performance ranges by years of study (2012 performance descriptors); the Spanish facts in
  finding 10; Spanish usage in finding 11.

## For Cory

1. **The Level 3 and 4 exits against the dose.** At about 63 hours a level (about 250 hours for all four), the
   remembered evidence puts Intermediate Mid at Level 3 as a stretch and Intermediate High at Level 4 out of reach,
   and the grammar on those levels is a third-year load. Options: (a) keep the exits and the dose, with the page's
   honest line that the hours are not shown to reach them; (b) keep the dose and lower the exits to Intermediate Low at
   Level 3 and Intermediate Mid at Level 4, moving the full past-tense contrast and the subjunctive to "beyond Level
   4"; (c) keep the exits and raise Levels 3 and 4 to a daily period (about 120 hours each), the norm in the middle
   and high schools where those levels are usually taken. Pick: (b), honest without new cost; the pages stay
   reachable and a school can still combine levels.
2. **Communities 5.1 beyond the school.** Keeping every Communities task inside school and public media follows the
   privacy and safety rules, but leaves the standard's "beyond the classroom" part met only in part, which the bar's
   C1 door fails. Options: (a) keep as written and name that part as not claimed on each course page and in the
   family note; (b) add an optional, school-arranged activity at Levels 3 and 4 (a class-to-class letter exchange or a
   guest who has chosen to come, set up by the school, nothing through the site), never required; (c) both. Pick: (c):
   the honest line stays true for a school that skips the option.
3. **The early-years companion's writing aim.** Option D says the companions target the same level as Levels 1 and 2,
   but a kindergartner may not yet write in any language. Options: (a) the same target in all modes; (b) listening and
   speaking at the level's target, reading and writing only as far as the child reads and writes in any language
   (copy and label), stated per mode on the companion page. Pick: (b).

## Fix pass (2026-11-22)

Applied by a fix agent with the lead's decisions. Files changed: data/progressions/spanish.csv,
data/standards/spanish-strands.txt (SPA.Sounds.3 only), docs/courses/world-languages/STANDARD.md and APPROACH.md
(finding 16 lines only), docs/agents/lenses/world-languages.md (the 2024 guidelines source line). spanish-edges.md
needed no change. Gate after: `progression.py check spanish` 51 rows (L1 13, L2 13, L3 13, L4 12), 0 failures;
`stale.py check` passes on every changed file.

- 1. Not applied: the exits, the dose and the grammar load went to Cory on the Desk (question 1).
- 2. All 12 Communication rows now call the sublevel "the proficiency estimate the course aims toward", with checks
  judging performance in the Novice range (L1, L2) or the Intermediate range (L3, L4).
- 3. l1-interpersonal and l2-interpersonal: a new card on the Check day (rehearsed language, unrehearsed content).
- 4. l4-presentational: past narration with both tenses attempted and slips when the time frame shifts, proposals
  with taught chunks. Only the Advanced Low control was fixed; "two to four short paragraphs" stays with finding 1.
- 5. l3-presentational and l4-presentational: writing aims one sublevel below speaking (Intermediate Low at Level 3,
  Intermediate Mid at Level 4).
- 6. The nine rows got the settled companion lines. "No writing asked" in l1-interpersonal became "the exchange is
  spoken", pointing to l1-presentational, which states the companion aim once: listening and speaking at the level's
  target, the reading and writing aim marked Pending for Cory (Desk q-prog-spanish-1).
- 7. African roots and US murals (l3-cult-products), Equatorial Guinea or the Caribbean (l4-cult-products), US
  Spanish-language radio, signs and murals today (l2-cult-products), a US Spanish-language source in at least one
  unit (l3-conn-info), Afro-descendant coastal communities (l4-cult-practices), and Mexico named as a source place in
  the l2-interpretive and l3-interpretive text lists.
- 8. l1-interpersonal teacher note says how the heritage path is offered; l1-presentational "records" to "writes".
- 9. l1-interpersonal teacher note: descriptions are of a character, a picture or oneself.
- 10. The four facts fixed as written (18 Spanish-speaking countries; surnames "in many places"; the voseo list; the
  seseo and ll/y line). In l3-sounds-varieties the old "z and soft c said as th in much of Spain" clause was dropped,
  since the new seseo line says it.
- 11. "la ve (la uve in Spain)"; ll as a pair in the l1 note and in SPA.Sounds.3; "¿qué día es hoy?" and "numbers or
  dates" at l1-interpretive; cansado / cansada; niño / niña.
- 12. Tú commands as chunks in l2-interpretive; usted and tú affirmative commands in l3-interpersonal; negative
  commands as chunks in l4-interpersonal.
- 13. SPA.Sounds.10 now owned at l3-sounds-varieties with the linking line; l4-sounds-linking carries ~SPA.Sounds.10
  and opens with its "Harder than Level 3" line.
- 14. Kept out; STANDARD section 6 now says the Spanish progression uses neither immigration lean.
- 15. Not applied: Communities 5.1 went to Cory on the Desk (question 2); no interim teacher note added.
- 16. STANDARD table row, section 6 opening, ladder line, progression.py line (with later.csv L93) and the
  social studies lean line updated; APPROACH unit field 3 points to spanish-edges.md; the lens source line updated.

Sent to Cory: finding 1 (exits and dose), finding 15 (Communities 5.1), and the companion's reading and writing aim
(finding 6, question 3 above).

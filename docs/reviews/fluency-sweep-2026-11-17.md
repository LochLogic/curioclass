# Fluency sweep, 2026-11-17 (later.csv L64)

Cory asked (2026-11-16) that the Fluency mislabel be fixed where the calendars are made. The unit lenses kept finding
days.csv days typed Fluency that first teach (Understanding) or draft, revise or edit writing (Application). This
record covers the rule, the gate, and one sweep of every days.csv except the math-4 and ela-6 courses (skipped,
blind list).

## The rule (one home)

- docs/GLOSSARY.md, row "teaching day": now the one home of the kind definitions. Understanding is the first explicit
  teaching of anything new (skill, concept, method, model, term set, text structure, a standard's first day), a bridge
  that teaches ahead of another subject included. Fluency is practice of what earlier days taught: it teaches nothing
  new and drafts, revises and edits no writing. Application uses taught work on a new task or case, and every day that
  drafts, revises or edits writing is Application. A day that does both is Understanding. Fluency-day work may still
  be collected and scored later (unit-lens.md, unchanged).
- docs/pipeline/briefs/sequence-write.md: the `kind` column points to the GLOSSARY row and adds the writer check
  (before typing Fluency, an earlier day must teach all the goal and note ask, and the day writes no draft, revision or
  edit). The gate paragraph names the new check.
- docs/pipeline/briefs/frame-write.md lesson 17: now points to the GLOSSARY row instead of restating it.
- scripts/day_skeleton.py KIND_MEANS: the printed Fluency and Application meanings match the row.
- docs/agents/decisions/DESK-ANSWERS.md: one entry.

## The gate (scripts/sequence.py, fluency_checks)

- **Failure:** a Fluency day whose goal says draft, edit, introduce or teach (verb forms only; "before drafting" and the
  noun "introduction" do not match), or "for the first time". The goal is the day's plain statement of what it does, so
  this is reliable; after the sweep no course fails it.
- **Notes, never failures:** a Fluency goal that revises a named piece of writing (science "revise the model" days do
  not match); a note that says introduce or teach (skipping "introduce no", "teach or practise", negated clauses and
  another subject's teaching); a code the Fluency day carries for the first time in the course. The first-code note is
  a note because map routines, fact fluency standards and retrievals of earlier-grade skills carry new codes on true
  practice days. Today: 39 first-code notes, 7 note-verb notes and 6 revise notes across 50 courses; no failures.

## Method

Every Fluency day (about 490 before the sweep) was read by goal and note, with the first-appearance flags, the lens
LEAD lines of docs/reviews/lead-list-lens-pass-2026-11-17.md and the rulings in data/plans/unit-rejections.csv (most
of which the lead had already applied). A candidate was then checked against its written unit plan: where the plan
already moves the first teaching to an earlier day and treats the day as practice, the day stays Fluency (14 such
candidates reverted, listed under "Left Fluency"). Science days that revise a model from new evidence stay Fluency
(model revision is not a piece of writing); K to 2 ELA days stay Fluency where only the foundations block teaches a
new pattern (it does every day; the kind follows the topic goal).

Dependent text: each changed unit plan's "Days by kind" header and day-list kind cells were set from days.csv; the
ELA field 2 "Owned codes by strand" lists (taught = Understanding) were regenerated from the skeleton for the four ELA
units with a day moved to Understanding (grade 12 units 2 and 3, grade 4 unit 1, grade 9 unit 3); the prose kind
counts were corrected in algebra-ii s03 and s06, geometry s01 (and its practice-day list) and math-grade-8 s05. No
scope-and-sequence.md of a changed course states kind totals.

## Days changed

| Course | Day | Unit | Old kind | New kind | Reason |
|---|---|---|---|---|---|
| math-grade-8 | 75 | 5 | Fluency | Understanding | new base-lesson teaching (8.4.4), lens finding |
| math-grade-8 | 76 | 5 | Fluency | Understanding | new base-lesson teaching (8.4.5): first equations needing distribution on both sides |
| math-grade-8 | 77 | 5 | Fluency | Understanding | new base-lesson teaching (8.4.6), lens finding |
| math-grade-8 | 79 | 5 | Fluency | Understanding | new base-lesson teaching (8.4.8): first solution-count equations |
| math-grade-8 | 86 | 5 | Fluency | Understanding | new base-lesson teaching (8.4.13): first solving a system by substitution |
| math-grade-8 | 87 | 5 | Fluency | Understanding | new base-lesson teaching (8.4.14), lens finding |
| algebra-ii | 51 | 3 | Fluency | Understanding | negative rational exponents first taught (base Alg2.3.5), lens finding |
| algebra-ii | 60 | 3 | Fluency | Understanding | first day for N-CN.A.2: complex sums and differences and powers of i are new |
| algebra-ii | 61 | 3 | Fluency | Understanding | complex multiplication first taught (base Alg2.3.13), lens finding |
| algebra-ii | 117 | 6 | Fluency | Understanding | radian inputs on the unit circle first taught (base Alg2.6.4); the plan opens with a worked example |
| algebra-ii | 119 | 6 | Fluency | Understanding | other ratios from one ratio and a quadrant first taught (base Alg2.6.6); worked example |
| algebra-ii | 127 | 6 | Fluency | Understanding | horizontal shift of a periodic rule first taught (base Alg2.6.14); worked example |
| geometry | 6 | 1 | Fluency | Understanding | first angle copy and parallel construction, lens finding |
| geometry | 16 | 1 | Fluency | Understanding | first classification of rotations that carry a figure onto itself, lens finding |
| english-language-arts-grade-4 | 7 | 1 | Fluency | Understanding | first day for L.4.5b; note: "teach idiom, adage and proverb" |
| english-language-arts-grade-7 | 26 | 1 | Fluency | Application | edits the narrative draft |
| english-language-arts-grade-7 | 51 | 2 | Fluency | Application | edits the explanation draft (revision and clean copy), lens finding |
| english-language-arts-grade-7 | 103 | 4 | Fluency | Application | edits the argument draft |
| english-language-arts-grade-8 | 115 | 4 | Fluency | Application | revises description in the draft (replace vague wording) |
| english-language-arts-grade-8 | 119 | 4 | Fluency | Application | edits the retelling draft |
| english-language-arts-grade-9 | 56 | 3 | Fluency | Understanding | first day for L.9-10.2c: first teaches spelling checks (lens: dictionary checking) |
| english-language-arts-grade-9 | 59 | 3 | Fluency | Application | revises the cultural-analysis draft, lens finding |
| english-language-arts-grade-9 | 113 | 6 | Fluency | Application | edits, types and publishes the argument |
| english-language-arts-grade-9 | 114 | 6 | Fluency | Application | finishes the final argument draft against its sources |
| english-language-arts-grade-11 | 27 | 2 | Fluency | Application | revises the informative draft for cohesion and style |
| english-language-arts-grade-11 | 29 | 2 | Fluency | Application | edits the complete explanation |
| english-language-arts-grade-11 | 149 | 9 | Fluency | Application | edits the narrative draft |
| english-language-arts-grade-12 | 18 | 2 | Fluency | Understanding | note: "Teach L.4a to d"; first day for L.11-12.3, L.11-12.4 and parts |
| english-language-arts-grade-12 | 25 | 2 | Fluency | Application | revises the comparison chart and a paragraph |
| english-language-arts-grade-12 | 40 | 3 | Fluency | Understanding | note: "Teach L.5a, figures and role" |
| english-language-arts-grade-12 | 61 | 4 | Fluency | Application | revises a written account for effect |
| biology | 5 | 1 | Fluency | Understanding | note: "teach these displays here" (a bridge that teaches before plotting) |
| biology | 138 | 9 | Fluency | Application | edits the written design justification |
| chemistry | 91 | 7 | Fluency | Understanding | note: "Teach a unit-cancelling worked example" (bridge) |
| civics-government-and-civic-life | 60 | 4 | Fluency | Understanding | first teaches reading turnout tables and percentage points, lens finding |
| civics-government-and-civic-life | 116 | 7 | Fluency | Understanding | first teaches the six economic indicators, lens finding and unit-rejections ruling |
| civics-government-and-civic-life | 136 | 9 | Fluency | Understanding | first models lateral reading, lens finding |
| civics-government-and-civic-life | 137 | 9 | Fluency | Understanding | first models weighing claims and spotting misinformation, lens finding |
| science-grade-6 | 74 | 3 | Fluency | Application | independent drafts P, W and EP are written this day |
| science-grade-8 | 14 | 1 | Fluency | Understanding | new base lessons 8.1 L7 and L8 with a worked-axes bridge, lens finding |
| science-grade-8 | 33 | 2 | Fluency | Understanding | note carries the first worked graph-shape example, lens finding |
| social-studies-grade-3 | 5 | 1 | Fluency | Understanding | first teaches the letter-and-number grid, lens finding |
| social-studies-grade-4 | 22 | 2 | Fluency | Understanding | the only day that teaches checking one fact in two sources, lens finding |
| world-geography-and-ancient-civilizations-i | 31 | 3 | Fluency | Understanding | first teaches climate graphs: "Axes explained before any comparison" |

| Course | To Understanding | To Application | Total |
|---|---|---|---|
| math-grade-8 | 6 | 0 | 6 |
| algebra-ii | 6 | 0 | 6 |
| geometry | 2 | 0 | 2 |
| english-language-arts-grade-4 | 1 | 0 | 1 |
| english-language-arts-grade-7 | 0 | 3 | 3 |
| english-language-arts-grade-8 | 0 | 2 | 2 |
| english-language-arts-grade-9 | 1 | 3 | 4 |
| english-language-arts-grade-11 | 0 | 3 | 3 |
| english-language-arts-grade-12 | 2 | 2 | 4 |
| biology | 1 | 1 | 2 |
| chemistry | 1 | 0 | 1 |
| civics-government-and-civic-life | 4 | 0 | 4 |
| science-grade-6 | 0 | 1 | 1 |
| science-grade-8 | 2 | 0 | 2 |
| social-studies-grade-3 | 1 | 0 | 1 |
| social-studies-grade-4 | 1 | 0 | 1 |
| world-geography-and-ancient-civilizations-i | 1 | 0 | 1 |
| **All 17 courses** | **29** | **15** | **44** |

## Left Fluency (for the lead)

- **Notes that contradict their plan.** The plan already treats these as practice, so the kind stays, but the days.csv
  note still reads as first teaching: math-grade-3 96 ("Introduce the fraction strip") and 106 ("Teach and practise
  n/1 and b/b"), math-grade-8 7 ("Explicitly teach and assess", plan: day 6 teaches) and 33 ("Begin slope", plan: day
  33 checks points). Fix the notes or retype.
- **Reverted after reading the plan** (plan moves the teaching earlier): algebra-i 25, 69, 101; math-grade-3 25;
  math-grade-6 106; math-grade-8 99; math-kindergarten 38, 89 (lens finding 1042 says day 89 first teaches; the plan
  says it rehearses), 106; geometry 72.
- **Unsure, unchanged:** science-grade-6 7 (lens: model revision is Application work); english-language-arts-grade-7
  130 (lens 592); algebra-ii 46 and 101 (rebuild of grade 8 rules; plan moved the f(-x) worked test to day 100);
  math-grade-6 91 (lens 937); math-grade-8 123, 124, 129, 130 (lens 1006 to 1007, plan treats them as practice);
  social-studies-grade-3 134 and 158 (lens 1636, 1648: revisions of records and a fresh observed performance);
  us-history-ii 46 and the world geography "countries, capitals and cities" days (new places through a practised map
  routine); english-language-arts-grade-11 11, english-language-arts-grade-2 110, english-language-arts-grade-12 137
  (one revised sentence or a practice paragraph, not a piece of writing developed).

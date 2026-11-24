# English Language Arts units: cold read from the progression down, 2026-11-24

COURSE-RUN stage 4 gate read ("one cold read from the progression down across every course"). The reader wrote and
fixed none of it. Read: AGENTS.md, docs/COURSE-RUN.md stage 4, docs/agents/EXPERT.md, docs/agents/lenses/ela.md,
docs/courses/UNIT-PLAN.md; data/progressions/ela.csv (374 rows, K to 12) in grade order; for kindergarten, grades 1
to 5 and 7 to 12 (grade 6 belongs to another session and was not opened) each frame's units, each unit plan's
field 2 owned rows, field 3, field 4 last-use and retrieval tables and Goal map (sampled; whole fields read for
grade 3 units 1 to 3, grade 4 unit 1, grade 10 unit 6, grade 11 units 2 and 3, grade 12 unit 1), plus days.csv,
items.csv, source-map.csv, ela-texts.csv and data/plans/ledgers/ela.csv. Gates run read-only, filtered to these
courses: unitplan.py check (0 FAIL), sequence check (0 failures), plan.py check (failures in K, 1, 2, 3 and 11, below).
The 2026-11-24 ledgers (units-read-*, units-structure-pass-english-language-arts) were read only after the findings
below were drafted, to mark status.

## Verdict

Not yet ready for owner approval. The chain itself holds: every one of the 345 progression rows in these twelve
courses is owned in field 2 of a unit at its grade and appears on days.csv, every earlier-grade row a node assumes
sits exactly one grade back and is named, with a retrieval task, in field 3 or 4 of an owning unit, and the unit
arcs follow the progression's story with text demand rising. What blocks approval is outside the arcs: stage 4's
ledger rows were never seeded (grades 4, 5 and 7 to 12 have no ledger rows at all), K to 3 exits sit on invented
cards marked as needing the text, and one cross-grade text clash (grade 11 and 12 Twain) is still open.

## Findings, most serious first

| # | Where | What | Severity | Status |
|---|---|---|---|---|
| 1 | data/plans/ledgers/ela.csv, all courses | COURSE-RUN stage 4 Make says "the ledger gets the unit's rows at stage planned". The ELA ledger holds 6,173 rows, all for K to 3 and all section-level (`where` u0N-N) from the stage 5 ladder run; no course has a unit-level (s0N) row, and grades 4, 5 and 7 to 12 have none. Stage 4's "review entries point at real earlier rows" can only be met through the progression and days.csv last-use tables (which do hold), and the stage 5 citation check and the stage 6 `ledger.py gate` will have nothing to check grades 4 to 12 against. | Serious (process) | Open. Not named in any 2026-11-24 ledger. |
| 2 | items.csv, K to 3 (stage 5 data); Goal maps, grades 4 to 12 | Exits sit on invented cards whose scene is not in the day's text, yet carry needs_text yes: grade 2, 214 of 238 exits (text_ref "an invented insert card ... its scene is not in the text"); grade 3, 282 items (177 of 194 exits, 57 end-of-unit items). Counted honestly, grade 2 falls from 80 to about 47 percent of items needing the text and grade 3 from 61 to about 48; K (11 percent) and grade 1 (15 percent) already fail the 80 percent gate. The lens counts "an exit ticket not about the day's text" as a day error. Grades 4 to 12 Goal maps often specify an exit on "a new passage" or "a fresh passage" without saying whether it comes from the unit's texts, so stage 5 writers there will repeat the pattern. Rule 4 (no reuse) and the 80 percent rule pull against each other and no doc settles it. | Serious | Open. Not in the ledgers. |
| 3 | Grade 11 s02 day 33; grade 12 s01 days 1 and 2 (g12-u1-01) | The grade 11 cold assessment text (Twain, Life on the Mississippi chapter 9, the river passage) is the grade 12 unit 1 anchor for days 1 and 2. Grade 12 opens on a text its students were scored on the year before, so neither its first close read nor its hook is fresh. Verified in both plans. | Medium | Open. Found first by units-read grade 11 (finding 1); the structure pass left it for the lead. |
| 4 | plan.py check, K, 1, 2, 3, 11 | Failures unchanged by the structure pass (35, 38, 310, 45, 12). Most are stage 5 data (shape notes, sections missing from data/units.csv, one-ask stems, exits), but grade 2's 230 source-map rows fail because harms_learning holds prose ("no; teaching and evidence remain in sequence") where the gate wants yes, no or unclear, the same no-conflict prose the structure pass fixed in unit_skeleton.py but not in the data or plan.py. The gates in AGENTS.md are not clean for these courses. | Medium | Open. Counts recorded, not fixed, in the structure pass. |
| 5 | days.csv kinds, 9 rows in 8 courses | These progression rows never fall on an Understanding day: e1-revise-publish, e3-opinion, e5-presenting, e7-produce-publish, e8-narrative-writing, e8-present-reasoning, e9-sl-presentation, e10-w-process, e12-lit-interpretations. Checked e3-opinion: it is taught on day 98 (Goal map "Teaches four boxes of opinion and reason") but the day is marked Application, so field 2's generated "taught: none" for W.3.4 and the opinion codes misleads a section writer into treating the year's first opinion writing as practice only. | Low to medium | Partly open: the reads and the structure pass list day kinds for grades 2, 3, 7 and 9 as judgment calls left unapplied; grades 1, 5, 8, 10 and 12 not raised. |
| 6 | days.csv skills column, grades 1, 7, 8, 10, 11, 12 | Earlier-grade rows tagged as skills on teaching days (grade 7 day 31 lists five e6 rows and day 87 four; grade 1 day 21 ek-unknown-words; grade 8 day 66, grade 10 days 95 and 150, grade 11 day 43, grade 12 day 3). The last-use tables and the ledger gate count tags as uses, so a tag can hide a gap or invent one (the structure pass hit the same effect with e2-compare-texts). One timing case is real: grade 11 day 1 teaches e11-evidence-uncertain, which assumes e10-ri-evidence-central-idea, two days before that row's retrieval on day 3. | Low | Open. |
| 7 | Grade 4 and 5 frames, ela-texts.csv | Grade 4 anchor targets (800 to 1,000, 800 to 1,010, 850 to 1,010) sit as high as grade 5's (750 to 950, 850 to 1,010) within the shared 740 to 1,010 band, so the climb from grade 4 to grade 5 rests on scaffolding against independence alone. Grades 7 and 8 anchors are mostly "to write" with band halves stated in the frames, and grades 9 to 12 measures are "not on file"; the 6 to 12 staircase is checkable only by qualitative reads until the texts exist. | Low | Open. Not in the ledgers. |

## What holds and should not be touched

- Ownership: all 345 rows are in some unit's field 2 at their grade and on days.csv; no unknown progression ids in
  any plan.
- Edges: no assumes cell points two or more grades back or forward; every hands_on has its back link; every assumed
  row is named in field 3 or 4 of an owning unit, with retrieval placed at the first real use (grade 3 unit 1 field 4
  checked row by row: e2-revise-edit on day 20, e2-informative on day 16, e2-opinion on day 98 in unit 3).
- Repeated teaching across units of a grade (Understanding days for the same row in several units) is the base
  text's recursive design: the repeats sampled in grades 4 and 5 are launch-day routine tags, and field 2 names what
  is new each time. Not a double teach.
- Cross-grade text repeats are deliberate and lensed: the Declaration of Independence is read for related themes in
  grade 10 unit 6 and for reasoning in grade 11 unit 3, both plans saying so. No other text repeats across grades.
- Arcs: K to 2 science and social topic sets, grade 3 to 5 topic modules, grades 7 and 8 topic-and-original-text
  units, grades 9 to 12 whole works climbing to the grade 12 research project, fit the progression's handoffs.

## Open items for the fix pass

1. Seed unit-level ledger rows for every course (`scripts/ledger.py seed`), at least grades 4, 5 and 7 to 12 before
   their stage 5 runs; then run `ledger.py check ela --all`.
2. Settle one rule in UNIT-PLAN.md (ELA data) or APPROACH-ELA.md: whether an exit's passage must be the day's text,
   or a card on the unit's text and topic, and how needs_text is set for an invented card; then correct needs_text on
   the K to 3 rows (and decide whether the 80 percent gate applies to K and grade 1 foundational items). A scope-free
   wording decision for the lead; ask Cory only if it changes what the exits test.
3. Resolve the Twain clash: one course changes its passage (grade 11's cold check is the cheaper change).
4. Grade 2 source-map.csv: set harms_learning to the bare word (no) and move the prose to why, or let plan.py accept
   the "no; ..." form as the skeleton fix did; clear the other stage 4 data failures before approval and list the
   stage 5 ones as deferred.
5. Day kinds: relabel the teaching day of each row in finding 5 as Understanding where the Goal map teaches it, in the
   unwritten courses first; in written days leave a defect row.
6. Move earlier-grade tags out of the skills column into the retrieval note; move grade 11's
   e10-ri-evidence-central-idea retrieval to day 1.
7. Grade 4 text spec: aim the original grade 4 anchors at the lower half of the 4 to 5 band (a target of our own,
   untested).

Also still open from the 2026-11-24 ledgers and on the chain: grade 4 day 160's portfolio hand-back has no receiver in
grade 5 s01 (structure pass, grade 4); grade 9 to grade 12 seam note left for the lead.

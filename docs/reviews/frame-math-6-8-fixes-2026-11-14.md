# Fixes: math course frames, grades 6 to 8, after the two cold reads (2026-11-14)

Applies the expert reads (`frame-math-grade-<n>-2026-11-14.md`) and the Codex reruns
(`frame-math-grade-<n>-codex-rerun-2026-11-14.md`) for grades 6, 7 and 8 to the three frames and
`data/progressions/math.csv`. The older `frame-math-grade-<n>-codex-2026-11-14.md` reads withheld their verdicts over a
gate failure and were not used. Every expert finding and every "Settled by the expert" row is applied; each Codex
finding was weighed on its merits. The items the high school fix pass left for the grade 8 fixer (its Cross-subject
notes and For the lead item 4: the stale For the lead item 6; the accelerated path) are applied. The grade 5 and
Algebra I frames were not edited: no handoff with either changed (the grade 5 Cross-subject sentence Codex grade 6
finding 11 names was already fixed by the grades 3 to 5 pass).

Base-text claims were checked against the source store (S:\CurioClass-sources\illustrative-math, lesson titles,
activity timings and optional marks read with a script): 6.1.19 "Designing a Tent" carries no optional mark and tags
6.G.A.1 and 6.G.A.4; 6.5.9 is partial quotients, 6.5.10 introduces long division, 6.5.11 divides to non-whole
quotients, 6.5.12 divides decimals by whole numbers; 6.7.3 to 7 are order and distance from zero, 6.7.8 to 10
inequalities, 6.7.15 and 19 polygons and drawing on the plane; 6.8.17 and 18 are using box plots and using data to
solve problems; 7.4.5 "Say It with Decimals" holds the repeating-decimals activity (7.4.4 is "Half as Much Again",
7.5.12 "Negative Rates"); 7.1.4 measures corresponding angles with protractors; 7.7.17 is optional on its prep page;
7.8.19 is not optional (one activity is) and its information gap runs 30 minutes, so 7.8.18 and 19 together hold about
95 minutes of activity; 8.1.16 gives the exterior angle only in a practice problem; 8.8.10 opens with a square-root
estimate.

Gates after the fixes: `scripts/frame.py sync` (52 courses); `scripts/frame.py check math-grade-6 math-grade-7
math-grade-8 math-grade-5 algebra-i` 0 failures each (grade 6 8 units, 160 days, 154 in units; grade 7 8, 160, 154;
grade 8 8, 160, 154; grade 5 10, 160, 145; Algebra I 7, 160, 151); `scripts/progression.py check math` 305 rows, 0
failures; `scripts/stale.py check` 56 files, 0 failures. Unit counts and totals unchanged; grade 6 moved one day from
unit 8 to unit 1.

## Grade 6

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | 6.1.19 kept (culminating application of 6.G.A.1 and 6.G.A.4, MP4); funded by merging 6.8.1 with 6.8.2. Unit 1 17 to 18 days, unit 8 17 to 16; unit 1 practices MP7 and MP4 (one or two per unit; MP3 stays in units 6 and 8). Day numbers from unit 2 on shift by one in the checks and Cross-subject sections |
| Expert | 2 | Applied | Days bullet rewritten ("where days allow, one mixed-practice day"); every source-map unit row names its Curio Class days |
| Expert | 3 | Applied | Cross-subject rows rewritten against the science 6 and ELA 6 frames as they now stand (science changed its days during this pass: unit 4 92 to 115, unit 5 116 to 135, unit 6 136 to 158, and now uses rate and ratio language as retrieval); items 5 and 6 rewritten |
| Expert | 4 | Applied | Unit 1: retrieves letters for numbers (3.OA.D.8, 4.OA.A.3) and begins this year's letters in formulas, named as variables in unit 6 |
| Expert | 5 | Applied | Unit 6: a variable as one unknown or any number in a set (6.EE.B.6 in full); unit 7: side length of a horizontal or vertical side from coordinates (6.G.A.3 in full, IM 6.7.15 and 19) |
| Expert | 6 | Applied | Row pointers corrected in math.csv by this pass (the expert routed them to For the lead; this pass is the progression fixer) |
| Expert | 7 | Applied | Focus line: 62.5 percent strict by units, 75 with unit 1; 124 of 160 days (78 percent) with connected work after finding 1's day; about 97 of 138 kept lessons (70 percent); item 2 settled |
| Expert | settled | Applied | All four rows |
| Codex | 1 | Rejected | Conflicts with the expert's settled keep of 6.1.19: IM does not mark it optional, and adapting lesson 15 instead would leave the base text's own culminating day out |
| Codex | 2 | Applied in part | Composition spelled out in every unit row; for the 3-day units the expert's settled rule (respond work in the openings of the next two lessons), not Codex's combined 20 and 30 minute day |
| Codex | 3 | Applied | m6-long-division: grade 5 size limit removed (not a grade 6 ceiling); unit 5 says so |
| Codex | 4 | Applied | Unit 6 and m6-one-step-equations: substitution from a specified set into equations and simple supplied inequalities, nonnegative; unknown against a variable over a set; unit 7 meets them again with negatives |
| Codex | 5 | Applied | Pointers as expert 6, plus m6-long-division to 6.5.9 to 11, reinforced in 12 |
| Codex | 6 | Applied | Item 2 closed; "No days move because the strict unit count is under 65 percent"; estimates left for the scope and sequence to verify in minutes |
| Codex | 7 | Applied | Readers conflict on item 5's reason: the expert's text says the base order "ends on major work"; Codex is right that unit 8 is additional. The pick (keep IM's order, settled) stands; its reason now says a swap would end on major work but is not needed because science teaches its own histogram reading |
| Codex | 8 | Applied in part | Item 4 rewritten to fix the tag at its source (`data/modules/math.txt` line 71, rebuild, `data/coverage.csv` line 1710); those files are outside this pass (For the lead) |
| Codex | 9 | Applied | As expert 4 |
| Codex | 10 | For the lead | Lens line, outside this pass's files |
| Codex | 11 | Rejected | Already fixed: the grade 5 Cross-subject intro now says the science and social studies frames are written |
| Codex | For Cory | For Cory | Math content reviewer (people, money) |

Counts: applied 7 expert + 8 Codex (2 in part); rejected 2; for the lead 1; for Cory 1.

## Grade 7

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | Unit 4 begins 7.NS.A.2d (IM 7.4.5); unit 5 names a Curio Class day finishing it (why decimals end or repeat, negative rationals, an independent long-division check); unit 5 begins 7.EE.B.4a (IM 7.5.11, 14 to 16), owned in unit 6; m7-decimal-expansion notes rewritten |
| Expert | 2 | Applied | Focus arithmetic fixed (94 + 4 = 98, 61 percent; 114, 71 percent; 6 of 8 units with units 1 and 8; about 88 of 125 kept lessons); a "Major work practised" line in units 1, 3, 7 and 8; item 2 closed with option (a) |
| Expert | 3 | Applied | Every source-map unit row names its Curio Class days |
| Expert | 4 | Applied | MS-PS1-4 moved to "Earlier grades" (science 6); science 7 design row "close", population row available (days 129 to 158), time zones available (days 78 to 86) |
| Expert | 5 | Applied | 7.7.17: "IM optional (prep page); extension candidate" |
| Expert | settled | Applied | All four rows |
| Codex | 1 | Applied | As expert 1 |
| Codex | 2 | Applied | 7.G.A.2 is a student performance: students construct with a no-account tool, taking turns on a shared device; demonstration and paper do not replace it; the unit plan names the tool and the turn plan; item 4 rewritten (a Curio Class tool goes on later.csv only if none fits) |
| Codex | 3 | Applied | Merge rule under the source map; 7.1.3 and 4 and 7.1.11 and 12 selections written into their rows; the 7.8.18 and 19 merge replaced by lesson 18 alone, lesson 19 cut with the reason that it is not optional but practises lesson 18 and does not fit beside it (unit 8 still 17 IM days) |
| Codex | 4 | Applied | Readiness on angle measure and the protractor in unit 1 (opening of lesson 2's day, before the merged 3 and 4); unit 7 "recheck and refresh"; protractor and tracing paper in unit 1; m7-scale-drawings assumes m4-protractor and m4-protractor hands on to it |
| Codex | 5 | Applied | Connected figure marked provisional; 8,000 minutes, 5,200 qualifying; the scope and sequence lists qualifying activities and minutes without double counting; unit lengths unchanged |
| Codex | 6 | Applied | As expert 4, with Codex's design-task line (supplied comparisons before day 33, the full test after) |
| Codex | 7 | Applied | m7-percent-problems 7.4.6 to 16 (4 and 5 for representations); m7-compare-populations 7.8.11 and 18, 19 an extension, 12 to 16 sampling |
| Codex | 8, 9 | For the lead | `docs/RUBRIC-MATH-K8.md`, outside this pass's files (the grades 3 to 5 pass sent the same) |
| Codex | 10 | For the lead | Lens line, outside this pass's files |
| Codex | 11 | Applied | Grade 8 Seams intro and receiving units (see grade 8, expert 3) |
| Codex | 12 | For the lead | Superseded note on `frame-math-grade-7-codex-2026-11-14.md`, outside this pass's files |

Counts: applied 5 expert + 8 Codex; rejected 0; for the lead 4; for Cory 0.

## Grade 8

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | Source map "keep; adapt 1 to 5 and 8": relationship, line, y = mx + b, not function; practice drawn from IM 8.4 and 8.5 replaced with review of units 1 to 3; unit 4 says so; unit 6 opens by naming unit 4's lines of fit as linear functions; m8-scatter-plots notes; item 2 closed (the move stands) |
| Expert | 2 | Applied | Unit 1: exterior angle and transversal angle pairs (8.G.A.5 in full), "keep; adapt 16" with the added activity; unit 8: estimating expressions with irrational numbers (8.NS.A.2 in full); m8-angle-facts and m8-irrational-numbers notes |
| Expert | 3 | Applied | Seams intro: "Their frames name the receiving units"; every hand-on row gives the Algebra I or Geometry unit from those frames |
| Expert | 4 | Applied, unit 4 changed | Curio Class days named per unit. The expert's unit 4 list (readiness, mid-unit check and respond, assessment and respond) is five days in a four-day allowance (Codex 3): unit 4 uses the grade 6 settled rule instead (mid-unit check, its respond work in the next two openings). The settlement's aim, a respond step after each check, is kept |
| Expert | 5 | Applied | Scatter-plot rows available (science units 4 and 5, days 78 to 130); graph-reading row names both s8-kinetic-energy-graphs and s8-wave-amplitude-energy (science days 1 to 48, earlier, with its bridge); scientific-notation row "earlier: days 78 to 105" |
| Expert | 6 | Applied | 5 of 8 units own only major clusters; units 4, 6 and 8 named with their connections; about 103 of 121 kept lessons (85 percent); 129 days marked an estimate |
| Expert | settled | Applied | All three rows (row 3 as noted under finding 4) |
| Codex | 1 | Applied | As expert 1 |
| Codex | 2 | Applied | As expert 2, with Codex's narrowing: IM 8.8.10 already opens with the estimate, kept for 8.NS.A.2 |
| Codex | 3 | Applied | Units 1 and 2: a short mid-unit check inside a lesson's opening; units 7 and 8: readiness in an opening; days bullet rewritten |
| Codex | 4 | Applied | As expert 6 |
| Codex | 5 | Applied | As expert 3 |
| Codex | 6 | Applied | Item 6 rewritten: N-Q.A.3 is owned (geo-solving-right-triangles); scientific notation keeps no outgoing link and ends in core math, Chemistry retrieving it; the high school pass's stale-item note is closed with it |
| Codex | 7, 8 | For the lead | `docs/RUBRIC-MATH-K8.md`, outside this pass's files |
| Codex | 9 | For the lead | `docs/courses/math-4-spine.md`: outside this pass's files and closed to it by its blind rule; not opened |
| Codex | For Cory | For Cory | Accelerated path (already For the lead item 4) |
| High school pass | lead 4, Cross-subject | Applied | Item 6 (as Codex 6); item 4 now says an accelerated path skips this course and needs the compression plan named in the Algebra I frame's item 4, the offer Cory's |

Counts: applied 6 expert + 6 Codex + the two high school items; rejected 0; for the lead 3; for Cory 1.

## Progression changes (data/progressions/math.csv, 14 rows)

| Row | Change |
|---|---|
| m6-long-division | Notes: IM 6.5.9 to 11, reinforced in 12; the grade 5 size limit is not a grade 6 ceiling |
| m6-order-absolute-value | Notes: IM 6.7.3 to 7 |
| m6-inequalities | Notes: IM 6.7.8 to 10 |
| m6-four-quadrants | Notes: IM 6.7.11 to 15 and 19; horizontal or vertical side length from coordinates (6.G.A.3 in full) |
| m6-summarize-data | Notes: IM 6.8.12 to 18, the summary in 17 and 18; IM 6.9 not needed |
| m6-one-step-equations | Notes: substitution from a set into equations and simple inequalities; unknown against a variable over a set (6.EE.B.5, 6.EE.B.6 in full) |
| m7-decimal-expansion | Notes: begun IM 7.4.5 (unit 4), finished on a Curio Class day in unit 5 |
| m7-percent-problems | Notes: IM 7.4.6 to 16, with 4 and 5 |
| m7-compare-populations | Notes: IM 7.8.11 and 18; 19 an extension; 12 to 16 sampling |
| m7-scale-drawings | assumes + m4-protractor; notes: across grades 5 and 6 on purpose, re-entry before IM 7.1.4 |
| m4-protractor | hands_on + m7-scale-drawings |
| m8-scatter-plots | Notes: practises the linear relationships of 8.EE.B (unit 3); function language joined in unit 6 |
| m8-angle-facts | Notes: exterior-angle activity added to IM 8.1.16 |
| m8-irrational-numbers | Notes: estimate pi squared or a sum of square roots (IM 8.8.10) |

## Cross-subject notes (other subjects' frames, not edited)

- **Science grade 6** (docs/courses/science-grade-6/frame.md, Cross-subject): math 6 days moved by one from unit 2 on.
  Replacement cells: s6-light-paths and s6-insulator-design "Math 6 teaches it later (its unit 8, days 143 to 158)";
  unit rates "math 6 unit 3 teaches unit rates on about days 45 to 51"; geologic time "Available: math 6 days 19 to
  59"; histograms "Math 6 teaches histograms later (unit 8, about days 146 to 148)"; cells "math 6 teaches ratio
  language on days 19 to 39"; thermometer "Math 6 opens negative numbers in its unit 7 (days 121 to 142)". The unit 4
  text (line 117) "math 6 teaches ratios on about days 18 to 58" becomes "about days 19 to 59".
- **ELA grade 6** (docs/courses/english-language-arts-grade-6/frame.md): line 149 "by about day 58" becomes "by about
  day 59"; line 152 and line 179 "about days 142 to 158" become "about days 143 to 158".
- **Science grade 8** (docs/courses/science-grade-8/frame.md, line 146): the scatter-plot row names
  s8-solar-system-scale, whose row leans on 5.NBT.A.2 and 7.G.A.1; the 8.SP.A.1 leans are s8-gravity-mass and
  s8-growth-factors. Replacement: "s8-gravity-mass, s8-growth-factors: math 8.SP.A.1 (m8-scatter-plots), patterns in
  scatter plots".
- **Science grade 7, social studies grades 6 to 8, civics, ELA 7 and 8:** the math frames now quote their days; no
  change needed.

## For the lead (outside this pass's files)

1. **Finance tag** (grade 6 item 4): remove `NSPFE.Earning Income` from line 71 of `data/modules/math.txt`, rebuild with
   `scripts/build_db.py`, and remove line 1710 (math, 6) of `data/coverage.csv`. Editing only `data/modules.csv` is
   undone by the next build.
2. **`docs/agents/lenses/math.md` lines 61 and 62** (Codex grade 6 finding 10, grade 7 finding 10): "data/progressions/math.csv
   records core math ownership, handoffs, models and limits from kindergarten through grade 11, and the course frames'
   Seams tables check them against unit order. The grades 3 to 5 narrative page remains a supplementary explanation;
   other bands have no narrative page."
3. **`docs/RUBRIC-MATH-K8.md`** practices row and teacher-supports row (Codex grade 7 findings 8 and 9, grade 8
   findings 7 and 8): the replacement text in the grades 3 to 5 fix report's "For the lead" stands.
4. **Superseded notes** on `frame-math-grade-6-codex-2026-11-14.md`, `-7-` and `-8-`: "Superseded by
   frame-math-grade-<n>-codex-rerun-2026-11-14.md, which completes the read; applied in
   frame-math-6-8-fixes-2026-11-14.md."
5. **`docs/courses/math-4-spine.md`** status statements (Codex grade 8 finding 9): not opened (blind rule); Codex's
   replacement text is in its report.
6. **Source list** (Codex grades 6 to 8): the archived Progressions index and the standalone draft progressions as
   fallbacks, labelled as drafts so their pages are never mixed with the compiled edition's.

## For Cory

- **Math content reviewer** (people, money): who reads every check item and key before a course is finished, and any
  pay. Already raised by the grades 3 to 5 pass.
- **The accelerated path** (scope): whether Algebra I is offered in grade 8, who may take it, and when; it needs a
  compression plan before it opens.

## Settled (for DIGEST.md)

| Choice | Course | Reason |
|---|---|---|
| 6.1.19 Designing a Tent kept; 6.8.1 and 6.8.2 merged to fund it (unit 1 18 days, unit 8 16) | 6 | Not optional in IM; the unit's only application and MP4 day |
| A unit with 3 Curio Class days: mid-unit check whose respond work runs in the next two openings, assessment, respond day (grade 6 units 3, 4, 7; grade 8 unit 4) | 6, 8 | A respond step after each check without taking a base day |
| Major work counted the guide's way (connected supporting work counts), strict count beside it; no days moved for the strict unit count | 6, 7, 8 | Evidence guide indicator 1e |
| Grade 6 units 7 and 8 keep IM's order; the reason is science's own histogram bridge, not "ends on major work" | 6 | Unit 8 is additional work |
| m6-long-division: no four-digit, two-digit ceiling in grade 6 | 6 | 6.NS.B.2 sets none; that limit is 5.NBT.B.6 |
| Substitution from a set into equations and simple inequalities in unit 6; unknown against variable over a set | 6 | 6.EE.B.5 and 6.EE.B.6 in full |
| 7.NS.A.2d begun on IM 7.4.5 in unit 4, finished on a Curio Class day in unit 5 (ownership unchanged) | 7 | Where the base text teaches it |
| 7.G.A.2 "with technology" done by students at the controls, taking turns on a shared device | 7 | A demonstration is not the student performance |
| 7.8.19 cut (not optional), 7.8.18 a day alone; merges carry named selections | 7 | 95 minutes of activity do not fit one day |
| Protractor readiness in grade 7 unit 1 before IM 7.1.4; m7-scale-drawings assumes m4-protractor | 7 | A thread starts where it is first used |
| Grade 8 data unit stays fourth; 8.6.1 to 5 and 8 adapted to unit 3's language, cumulative practice replaced | 8 | Science 8 needs scatter plots by day 78; functions come in unit 6 |
| Exterior-angle activity added to 8.1.16; 8.8.10's estimate kept for 8.NS.A.2 | 8 | Standards in full |
| m8-scientific-notation keeps no outgoing link; the thread ends in core math, Chemistry retrieves it | 8 | N-Q.A.3 is owned and is not a receiving skill for it |

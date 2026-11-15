# Rule 2 gap fixes, 2026-11-15

Scope: the 56 gap lines in the rule 2 gap list (READINESS-MISSING, WRONG-KIND, RETRIEVAL-UNNAMED, UNTAUGHT, COLLECT-ONCE) plus the ELA word-family items in `structure-pass-ela-2026-11-15.md` "For the lead". Only `data/plans/<course>/days.csv` and `docs/courses/<course>/scope-and-sequence.md` were edited. No unit boundaries, day counts or day order changed. `data/progressions/ela.csv` was read, not edited.

Counting follows `scripts/unit_skeleton.py`: "used" is one-hop (a day teaching a row whose `assumes` names the earlier row counts as a use of it); a day whose note says retrieval or readiness is not a use of a directly listed earlier row; a readiness check names a row if the id is in that day's skills or note.

## Summary

| Kind | Lines | Fixed | Left (false positive) |
|---|---|---|---|
| RETRIEVAL-UNNAMED | 35 | 35 | 0 |
| WRONG-KIND | 7 | 7 | 0 |
| READINESS-MISSING | 4 | 4 | 0 |
| UNTAUGHT | 3 | 3 | 0 |
| COLLECT-ONCE | 7 | 4 | 3 |
| ELA word families | 7 items | 7 | 0 |

## RETRIEVAL-UNNAMED (35, all fixed)

Each fix puts the id in the skills of the first day that leans on the row and names it as retrieval in that day's note.

- chemistry, unit 5: day 57 adds bio-photosynthesis-energy and bio-respiration-energy ("Retrieval:"); day 68 adds bio-population-carrying-capacity.
- chemistry, unit 7: day 88 adds bio-define-human-impact-problem and bio-evaluate-impact-solutions.
- chemistry, unit 9: day 122 adds bio-earth-life-coevolution.
- chemistry, unit 10: day 131 adds bio-carbon-cycle and bio-biodiversity-simulation.
- physics, unit 2: day 19 adds chem-energy-device-design. Unit 3: day 31 adds chem-bulk-properties-forces.
- Chemistry and physics scope docs already describe these retrievals in words; left unchanged.
- science-grade-6, unit 6: day 136 adds s4-structures-function (with s4-senses-brain, below).
- english-language-arts-grade-1, unit 1: day 21 adds ek-unknown-words.
- english-language-arts-grade-10: day 95 adds e9-ri-mediums; day 150 adds e9-sl-presentation.
- english-language-arts-grade-11, unit 3: day 43 adds e10-rl-source-transformation.
- english-language-arts-grade-12, unit 1: day 3 adds e11-word-strategies; note now opens "First retrieve e11-word-strategies".
- english-language-arts-grade-6, unit 3: day 64 adds e5-word-strategies.
- english-language-arts-grade-7: day 31 adds e6-central-idea-summary, e6-media-integrate, e6-idea-development, e6-compare-genres and e6-informative-writing ("Retrieval after hook"); day 65 adds e6-word-strategies; day 87 adds e6-author-purpose, e6-trace-argument, e6-read-vs-watch and e6-argument-writing; day 135 adds e6-section-structure.
- english-language-arts-grade-8, unit 3: day 66 adds e7-word-strategies.
- math-grade-3, unit 1: day 15 adds m2-fluency-within-20 and m2-odd-even, retrieved inside the warm-up.
- math-grade-4, unit 6: day 92 adds m3-area-multiply.
- math-grade-7: day 52 adds m6-equivalent-expressions; day 55 adds m6-gcf-lcm in the 5-minute opening; day 85 adds m6-expressions-variables.

## WRONG-KIND (7, all fixed)

Each row moves out of the readiness check into a "Retrieval: <id>" line on an early day of the unit. The id is removed from the readiness day's skills and note.

- science-grade-2, unit 2: grade 1 used sk-forecast-severe one-hop (s1-parent-offspring work, days 56 to 60). Day 10 loses the id, its readiness assess and readiness note (now a whole-day response, no readiness check); day 11 retrieves it. Scope table, the day 10 sentence and line 65 updated.
- science-grade-2, unit 7: grade 1 used sk-needs-places one-hop (s1-parts-mimic, days 10 to 21). Day 65 loses the id and readiness assess, goal and note rewritten; day 66 retrieves it. Scope table, the day 65 sentence and the unit 7 hook sentence updated.
- science-grade-4, unit 3: grade 3 used s1-signal-device one-hop (day 25). Day 41 readiness now covers only s1-sound-vibrates; day 43 retrieves s1-signal-device. Scope table row, the "Days 41, 76 and 93" sentence and the day 41 paragraph updated.
- science-grade-4, unit 5: grade 3 used s2-land-water-model one-hop (days 104 to 117). Day 76 readiness now covers only s2-water-where; day 78 retrieves s2-land-water-model. Scope table row and day 76 paragraph updated.
- math-grade-4, unit 5: m2-three-digit-place-value and m2-compare-three-digit were used one-hop in grade 3. Day 57 loses both ids, 2.NBT.A.1/3/4 and its readiness assess; day 58 retrieves both. Scope inventory now says one-hop and two readiness slots (days 44 and 76); table rows and lines 43, 93, 127, 137 and 147 updated.
- math-grade-4, unit 9: m2-halves-thirds-fourths was used earlier this year. Day 127 loses the id, 2.G.A.3 and readiness assess, tools set to the area model; day 128 note updated; day 132 retrieves it (tools: angle drawing; circle drawing).

## READINESS-MISSING (4, all fixed)

- science-grade-6, unit 6 (no readiness day): s4-senses-brain is rebuilt by day 13 (id added, note says it rebuilds the row) and retrieved on day 136 with s4-structures-function. Scope table row updated.
- science-grade-7, unit 3, readiness day 41: adds s5-identify-materials and s5-new-substances to skills and note, with responses on days 43 and 58. Day 42 note rewritten; day 43 gains a 5-minute readiness response. Scope table rows and the day 42 sentence updated.
- science-grade-7, unit 4, readiness day 68: adds s5-matter-movement; days 69 and 70 notes and goal cover the three rows. Scope table row and the day 68 readiness paragraph updated.

## UNTAUGHT (3, all fixed)

- english-language-arts-grade-2, days 72 and 117 (W.2.6): day 66 now first teaches W.2.6 (codes add W.2.6; 10-minute guided shared typing). Scope line 113 says so.
- english-language-arts-grade-3, day 36 (SL.3.2): day 17 codes add SL.3.2, first teaching main idea and two details from an expert's read-aloud section; day 25 adds the visual and quantitative formats.

## COLLECT-ONCE (7: 4 fixed, 3 left)

Fixed:
- english-language-arts-kindergarten, days 97, 98 and 99 with 107 and 109: days 107 and 109 now reuse each child's days 97 to 99 record for W.K.7, W.K.8 and RI.K.3 and observe a talk only to fill a missing part. A "Collect once" sentence was added to the scope.
- math-grade-7, days 156 and 159: day 159 "Read day 155-156 scores" became "Reuse day 155-156 scores".

Left unchanged, false positives:
- english-language-arts-grade-5, days 78 and 88: both are written tasks, not child-by-child collections. The child-by-child evidence match comes from the standing independent-reading routine wording ("teacher conferences"), not from the assessment. Day 88 also samples a new case for RI.5.3, a withheld biography passage.
- english-language-arts-grade-5, days 116 and 121: day 116 is a written essay, not child-by-child, and day 121 samples a new form (a presentation) for RI.5.9.
- english-language-arts-kindergarten, days 138 and 142: the match comes from the foundations "small groups" routine wording. Day 142 samples a new case, a card opinion against day 138's planting-place opinion, an existing product.

## ELA word families (7 items, all fixed by labelling the repeat as retrieval)

Source: `data/progressions/ela.csv` row e9-l-word-strategies gives grade 9 analyze, derive, infer, constitute, vary and synthesize; grade 10 create, perceive (cap/cept), reproduce and persuade, with transform built from retrieved parts and synthesize retrieved; grade 11 compel, sustain, legislate and hypothesize (hypo- new, thes/thet retrieved), with conceive and persuade retrieved.

- Grade 10 synthesize (days 111, 116, 121, 128, 131, 137, 141, 146, 151, 159): slot now reads "retrieval of grade 9's family synthesize / synthesis / synthetic ... new contexts, not new teaching". Days 131 and 159 carried the same slot and were relabelled too.
- Grade 10 transform (days 46, 51, 56, 61, 66, 71, 76, 81): slot now reads "built from retrieved parts (Latin form from grade 4, trans- from grade 5) with -ation/-ative, no new root".
- Grade 10 scope: table header now "(new unless marked)"; transform and synthesize rows marked; "These six families are reserved for grade 10's new teaching" replaced with the four new families plus the two retrieved ones.
- Grade 11 conceive (days 4, 8, 11, 17, 22): "retrieval of grade 10's Latin cap/cept (perceive) with con-, not a new root". Day 4 carries the week 1 slot, so it was relabelled with the four listed days.
- Grade 11 persuade (days 51, 56, 61, 66, 71): "retrieval of grade 10's family in new contexts, not new teaching".
- Grade 11 hypothesize (days 126, 131, 136, 141, 146, 151, 159): "Greek hypo- new, thes/thet retrieved from grade 9's synthesize".
- Grade 11 day 4: "Two-minute retrieval of grade 10's recorded families" now says grade 9's.
- Grade 11 scope line 167: now says four new families (pel/puls, ten/tain, leg/lat, hypo-), names conceive and persuade as retrieval runs, and says day 4 retrieves grade 9's families.

## For the lead

- Science grade 2, science grade 4 and math grade 4: the scopes' earlier reasoned readiness calls (content last taught two or more grades back) were overturned by the one-hop count, so those rows are now retrievals.
- Science grade 7: two rows are now checked twice (day 1 and day 41; day 41 and day 68), because a readiness response day does not count as a use.
- Science grade 6: day 13 now carries s4-senses-brain as a teaching use.
- Grade 10 now teaches four new word families, not six, and grade 11 four, not six. Both keep their weekly slots as retrieval runs rather than swapping in new families.

## Gates

- `scripts/sequence.py check` on all 19 touched courses: 0 failures each; no rule 2 notes remain.
- `scripts/plan.py check`: 0 failures.
- Audit, before to after:
  - science: ready_missing 3 units/4 rows to 0/0; retr_unnamed 26 to 15; wrong_kind 4 to 0.
  - ela: retr_unnamed 534 to 516; untaught 3 to 0; collect 11 to 6.
  - math: retr_unnamed 150 to 144; wrong_kind 3 to 0; collect 1 to 0.
  - The remaining retr_unnamed counts are "earlier this year" rows, outside this list. Their count is unchanged at 675.
  - The 6 ELA collect flags are the three false-positive pairs, each counted both ways.

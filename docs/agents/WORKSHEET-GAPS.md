# Worksheet gaps: what generators could make, and what only writers can (2026-11-04)

Cory asked (2026-11-04) to assess the worksheet backlog, then build about 10 generators aimed at the biggest gaps.
This is the assessment. The row-by-row data is in docs/agents/gap/*.csv (one line per unwritten concept row: class,
family, a short reason). Six reviewers read all 7,856 unwritten rows against docs/agents/GEN-OPTIONS.md.

## Where the collection stands

| | Rows |
|---|---|
| Planned (docs/worksheets/*.md, 215 units of 40 to 50) | 8,947 |
| Written by hand | 1,008 |
| Backed by a generator | 83 |
| Not done | 7,856 |

Writing is not slow: the 1,008 sheets came from about two days of waves. The limits are review time and the quality
bar. 171 of 215 units have about five sheets written; world languages has none.

## The classification

Each unwritten row was put in one class: `existing` (a current generator could make it with at most one small new
setting), `new` (a new generator could make it), or `authored` (it needs a writer: a passage, source, named work,
real data, scenario, picture-heavy K-2 task, or open creative content).

| Subject | Authored | Existing | New |
|---|---|---|---|
| Computer science | 359 | 11 | 135 |
| CTE | 102 | 8 | 82 |
| Dance | 224 | 109 | 122 |
| ELA | 367 | 65 | 102 |
| English learners | 322 | 72 | 100 |
| Health | 362 | 48 | 45 |
| Library | 253 | 67 | 141 |
| Math | 42 | 101 | 388 |
| Media arts | 287 | 80 | 87 |
| Music | 216 | 54 | 185 |
| PE | 269 | 108 | 78 |
| Science | 394 | 68 | 42 |
| SEL | 394 | 91 | 9 |
| Social studies | 440 | 43 | 36 |
| Theater | 304 | 71 | 80 |
| Visual arts | 271 | 61 | 110 |
| World languages | 257 | 14 | 180 |
| **All** | **4,863** | **1,071** | **1,922** |

**Read these as ceilings, not promises.** This pass asked "could a generator make this?" The strict pass that backs a
row asks "does it make this sheet, as described, well enough that the promise is kept?", and it keeps far less: in
math, science, social studies and ELA, the strict sift kept 57 rows where this pass counted 277 `existing`. Expect a
strict sift to keep roughly a quarter to a half of these counts. Even so, generators could plausibly carry 800 to
1,500 rows (10 to 17% of the backlog), not the 1% they carry today, and math would become mostly generated.

**About 4,900 rows need a writer whatever we build.** Science, social studies, SEL and health are 80 to 90% authored:
labs, sources, real data, scenarios. That is the backlog-size decision (below).

## The new-generator families, merged

| Family | Rows | Mostly in |
|---|---|---|
| Rubrics, checklists, peer and self feedback (rubric-feedback, can-do, PE skill checklists) | 205 | arts, PE, world languages |
| Other frames (storyboard, script page, dance counts, decision matrix, art thumbnails, stage blocking) | 180 | arts, PE |
| Logs with typed columns (custom-log, reading log) | 141 | arts, PE, library |
| World-language practice (conjugation, agreement, numbers, dates, times, target-language frames) | 141 | world languages |
| Music notation and rhythm | 120 | music |
| Statistics and probability (incl. survey tally, data tables, classifier metrics) | 110 | math, CS |
| High school algebra and precalculus | 101 | math, English learners |
| Finance and economics calculations | 97 | CTE, economics |
| Code and logic (grid arrows, trace tables, ciphers, algorithm traces) | 72 | CS |
| Early number (ten frames, dot cards, place value blocks, clocks, coins, measuring) | 69 | math K-2 |
| Grammar and mechanics | 53 | ELA, English learners |
| Research and presentation planners | 90 | library, ELA |
| Word study (roots, affixes, shades of meaning) | 44 | ELA, English learners |
| Fitness and health calculations | 44 | PE, health |
| Angles and geometry | 41 | math |
| Unit reviews mixed from other generators | 41 | math |
| Smaller: drawing drills 37, calculus 34, English-learner frames 21, arts term sorts 20, practice puzzles 19, trig 19, chemistry calculations 18, phonics 17, search skills 16, ratios 15, citations 15, color theory 14, decimals and percents 14 | | |

The roadmap's earlier list of 10 (place value, decimals and percents, ratios, integers, angles and coordinates,
statistics, phonics and spelling, grammar, unit conversions, balancing equations) was mostly small math families.
The data points elsewhere: the arts, world languages, CS, CTE and K-2 math have the biggest generator-shaped gaps.

## The 10 to build (chosen by rows unlocked, cost, and gaps no writer fills cheaply)

1. **rubric-checklist**: rubrics, can-do checklists, skill-cue checklists, peer and self feedback, with typed criteria
   and levels. Cheapest build, biggest family, every arts subject and PE.
2. **world-language**: Spanish and French practice (regular and common irregular verbs, agreement, numbers, dates,
   times, sentence frames). Fills the subject with zero written sheets. ASL is left to writers.
3. **music-notation**: staff and rhythm drawing: note naming, rhythm counting, scales, intervals, chords, blank
   composition staves. Nothing else can make these.
4. **statistics**: center and spread, box and dot plots, two-way tables, probability, sampling, survey tallies.
5. **algebra**: high school functions, systems, quadratics, exponents and logs, polynomials.
6. **finance**: pay stubs, budgets, simple and compound interest, loans, unit price, supply and demand.
7. **code-logic**: grid-arrow programs, trace tables, Boolean logic, binary, ciphers, sorting traces.
8. **early-number**: ten frames, dot cards, base-ten blocks, number lines, clocks, coins, measuring lines (K-2).
9. **grammar-words**: grammar, mechanics and word study from one sentence and word bank (parts of speech,
   punctuation, tense, roots and affixes, shades of meaning), with an English-learner frames mode.
10. **project-frames**: research, presentation, storyboard, script, dance count, stage blocking and decision-matrix
    layouts, like the organizer generator.

Plus one setting, not a generator: **typed columns on planner-log logs** (the custom-log family).

Next after these, by the same data: fitness and health calculations, unit reviews mixed from other generators,
angles and geometry, calculus and trig, chemistry calculations, drawing drills, citations and library skills.

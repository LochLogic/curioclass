# Unit skeleton spot check, 2026-11-15

A read-only check of 12 unit plan skeletons written by `scripts/unit_skeleton.py`. Each was compared with that unit's rows in `data/plans/<course>/days.csv`, the unit row in `docs/courses/<course>/frame.md`, `data/progressions/<subject>.csv`, `data/standards/`, `source-map.csv` and `data/plans/calendar.csv`. The rules applied are rule 2 of `docs/pipeline/briefs/sequence-write.md` and `docs/GLOSSARY.md`. No file other than this one was changed.

Verdicts: 0 ready for a writer, 11 ready with fixes, 1 not ready (science grade 7 unit 4).

Most problems come from the script, not from the data. Eight script patterns recur across subjects. Six data fixes are each local to one course.

## Word counts

| Unit | Words | TODO(writer) markers | Largest parts |
|---|---|---|---|
| science-kindergarten s03 | 2,993 | 23 | |
| science-grade-4 s02 | 4,647 | 25 | |
| science-grade-7 s04 | 6,984 | 27 | field 10: 2,732 |
| chemistry s05 | 3,841 | 28 | |
| english-language-arts-kindergarten s04 | 27,004 | 49 | day list 9,812; field 10 9,293; field 5 5,153 |
| english-language-arts-grade-3 s02 | 20,009 | about 140 | day list 5,748; field 5 4,418; field 10 4,216; field 2 3,296 |
| english-language-arts-grade-7 s03 | 7,365 | 63 | |
| english-language-arts-grade-11 s05 | 4,404 | 43 | |
| math-grade-1 s03 | 6,871 | 45 | field 10: 2,241 |
| math-grade-5 s04 | 3,750 | 26 | field 10: 1,664 |
| math-grade-8 s02 | 4,057 | 33 | field 10: 1,013 |
| geometry s03 | 4,979 | 36 | field 10: 1,272 |

**Bulk.** ELA K to 2 is long because the unit's days.csv notes alone hold 8,588 words over 39 days, and the skeleton prints them twice: once in field 5 and again in the day list. It also prints about 80 full source-map rows in field 10.

Yes, it should summarise:
- Field 5 should give the assessment day, its codes and a pointer to the day list, not the note again.
- Field 10 should give one line per source-map row (id, our days, decision) or counts plus "see source-map.csv".

That would cut ELA K from about 27,000 words to about 12,000 without losing any fact. ELA 3 has the same problem at a smaller scale, plus a padded earlier-rows table (see that unit). Science 7 and the math units carry the same field 10 boilerplate.

## Per unit

### science-kindergarten s03 (days 20 to 28): ready with fixes

1. `docs/courses/science-kindergarten/s03.md:33`: the anchor is garbled ("Design problem: ...block tower our ball rolls...").
   - Source: `frame.md:134` has no full stop before "Anchor:", and `split_science_cell` runs the two pieces together.
   - Fix both the data and the script.
2. `s03.md:42`: the K-2-ETS1-1 crosscutting cell reads "TODO(writer): no crosscutting concept on file". NGSS lists none for this PE, and the brief says to fill it from the Framework, so the writer will invent one. The cell should say "NGSS lists none" and point to the frame's focal concept, cause and effect.
3. Day 28 (Respond, assess observe): field 5 gives "Time: 30 minutes", but the days.csv note gives 10 response minutes.
4. Field 10 TODO asks for "the base unit and lessons adapted with each credit line". K-5 science has no base text; Curio Class writes its own and OpenSciEd is reference only.
5. `s03.md:15-17` (hook, question board, closing explanation) overlap the Storyline TODO at :46 and the Carried TODO at :48. The writer will answer the same thing three times.
6. The days.csv notes appear twice, in field 5 and in the day list.
7. "school days 46 to 64" is a span, while the course meets 3 days a week. Say "school days 46 to 64 (3 a week)", or list them.
8. Field 8 "Days whose notes name tools: 27" and "safety: 25" are weak keyword hits.

### science-grade-4 s02 (days 16 to 38): ready with fixes

Correct: the kind counts, the readiness check on day 15 for sk-sun-warms (`s02.md:76, :89`), and the retrievals.

1. `s02.md:89` says sk-sun-warms was last used in grade 1 (day 68). That use is a one-hop reach through a course-level Respond day. The day 15 note and the frame say "last explicitly taught in kindergarten". The rule outcome (readiness) is the same, but the writer sees two different stories. `used_on` should not count Respond or C days as a use.
2. The day 18 note "Refresh s1-light-materials" is not surfaced in field 4. It is not in the progression assumes, and its last use was grade 2, two grades back. It is a retrieval with no rule-2 row.
3. `s02.md:200` prints the frame's check-set cell "Candidate: the class's state energy profile" as still open. Day 34 in days.csv (`s02.md:230`) says "Candidate kept".
4. Field 8 lists near-duplicates as separate items: "foil strip switch (household stand-in)" at :161 and "foil strip switch" at :163, "metal spoons" and "spoon", and repeated hazards. `group_column` matches exact strings only.
5. The day 36 note asks for collision evidence (4-PS3-3), which is not in day 36's codes. This is a data fix.
6. `s02.md:204`: the base-text TODO is wrong for K-5 (same as science K finding 4).
7. "Hook for day 1" (`:14`) should name day 16.

### science-grade-7 s04 (days 69 to 96): not ready

Correct: the mid on day 82, the readiness on day 68 for the three grade 5 rows, and the retrievals on days 69 and 88.

1. Field 5 (`s04.md:111-129`) has item rows only for MS-LS1-6 (days 82 and 95). The other two owned PEs never get rows:
   - MS-LS2-3 end evidence is collected on day 93.
   - MS-PS1-3 end evidence is collected on day 94.
   - Both days have a blank assess (`s04.md:240-241`).
   - Day 95's codes list only MS-LS1-6 (`:242`), although its note "reuses" the other two.
   - Data fix: mark days 93 and 94 assess=end, or add the codes to day 95.
   - Script fix: warn when an owned code is on no assessment day.
2. Field 10 runs to 2,732 words because `field10_extras` prints whole source-map rows with the same boilerplate on each.
3. `s04.md:35`: food-web is labelled "introduced or first used here", but its own text says unit 3 introduced it (`frame_models`).
4. `s04.md:173`: "Days whose notes name safety: 75, 90 and 94" includes false hits on "harms" and "chemical" (`SAFEWORDS`).
5. "Hook for day 1" (`:15`) should be day 69.
6. `s04.md:208`: the base-text TODO is correct here (6-8 uses OpenSciEd).

### chemistry s05 (days 57 to 74): ready with fixes

Correct: the readiness on day 56, and the end assessment on day 73 with three codes and retained products.

1. `s05.md:26` lists Biology retrieval ids (bio-photosynthesis-energy, bio-respiration-energy, bio-population-carrying-capacity) as "Progression skills owned". They are grade 9 rows in the skills column for retrieval.
2. `s05.md:58` "Builds on" lists seven rows, including the grade 7 assumes of those bio rows. The field 4 earlier-rows table lists only two, and the three grade 9 rows the unit actually retrieves are missing from it. `earlier_rows` drops any assume that appears in skills.
3. `s05.md:175` "Note: the progression lists HS-LS1-5, HS-LS1-7, HS-LS2-3, HS-LS2-1 ... days.csv does not cite them" is a false alarm caused by the same retrieval ids.
4. `s05.md:95` reads "retrieval, basic algebra only." `retrieval_clauses` cut off "Grade 9 A-CED.A.4"; compare the day 68 note at `:198`.
5. `s05.md:179`: the base-text TODO is wrong for 9-12 (Curio Class's own).
6. `s05.md:162`: "chemical reaction" is a false safety hit.

### english-language-arts-kindergarten s04 (days 119 to 157): ready with fixes (summarise first)

1. `s04.md:1`: the title keeps "*Why do people care for trees?*", and there is no compelling-question line. `split_title` does not handle the italic form, so the hook TODO (`:13`) points at a question the skeleton never states.
2. `s04.md:5`: a 39-day unit has one section, 4.1 (days 119 to 157), so no section-naming TODO is produced. Either the data needs sections, or the script should flag a section over about 15 days.
3. Bulk (see Word counts): 13 assessment days each repeat a note of about 250 to 300 words in field 5, and field 10 holds about 80 full rows.
4. `s04.md:57-59`: the text set rows show "edition: not stated; rights: not stated", while the TODO says "Rights stay as the file has them". For Curio Class-written texts the rights are known, so `ela-texts.csv` should fill them.
5. Many owned codes are on no assessment day (RF.K.3, RF.K.4, RL.K.1 and others). A coverage line in field 5 would show this.
6. `s04.md:288`: the Note (L.K.1f, L.K.1, L.K.2a ...) is the same exact-code mismatch seen elsewhere. A parent code cited only through its parts, or the reverse, counts as missing.
7. Correct: "Collect once" is flagged for days 138 and 142.

### english-language-arts-grade-3 s02 (days 40 to 77): ready with fixes

1. `s02.md:159-182`: 18 grade 2 rows appear as "this course, last day 37/38, retrieval, not named by id". Each produces a retrieval-task TODO, although these rows are in continuous use through unit 1 skills that are cited again here. `earlier_rows` should take assumes only from skills new to this unit, or treat a use in the previous unit as continuous.
2. `s02.md:191` is a junk retrieval row: "42, 44, 47 ... 77 | retrieval." It comes from "then grammar retrieval." in the notes (`retrieval_clauses`).
3. `s02.md:195`: a same-unit review clause ("Retrieve and apply verb forms ... taught on days 43, 45 and 48") is treated as retrieval of an earlier row.
4. Field 5 (`:219-313`) has 8 to 10 rows per assessment day, listing the parent code beside its parts. With six mid days and an end window, that is about 50 rows. Drop the parent when its parts are listed.
5. `s02.md:96-102`: rights are "not stated" for every text, including EL Education texts whose licence is known.

### english-language-arts-grade-7 s03 (days 61 to 86): ready with fixes

Correct: the mid on day 73 and the day 83/85 reuse.

1. `s03.md:1`: the compelling question is lost. The title is `Smallpox: who gets the credit? "Who should ...?"`, and `split_title` fails because the title part ends in "?".
2. `s03.md:41` lists e6-word-strategies (a retrieval id) as owned. It is then missing from the field 4 table, although day 65 retrieves it, and `:87` "Builds on" lists its grade 5 assumes.
3. `s03.md:127` is a junk retrieval row: "retrieval, 3 words, 17 supported reading ..." is a minute budget, not a task.
4. `s03.md:134`: the day 86 row "retrieval of e6-author-purpose, e6-trace-argument ..." is unit 4's retrieval, placed on unit 3's last day (the goal at `:271` says "retrieve Athens foundations"). It is credited to unit 3 here, and unit 4's skeleton will miss it.
5. `s03.md:111-118`: five more "not named by id" rows come from continuous use (same cause as ELA 3 finding 1).
6. `s03.md:152, :186`: parent L.7.4 is listed alongside L.7.4a-d.
7. `s03.md:233`: the Note is a false alarm. W.7.2 is cited through its parts, and L.6.4 and L.6.5b come from the retrieval id.
8. `s03.md:51-58`: rights are "not stated" for public-domain texts (Jenner 1798, Montagu, Mather).

### english-language-arts-grade-11 s05 (days 82 to 95): ready with fixes

1. `s05.md:21, :30, :31, :121, :131-132`: the progression and frame mark RI.11-12.3, RI.11-12.6 and SL.11-12.3 as "~" (grade 11 begins a band standard and grade 12 owns it; frame.md line 9). days.csv drops the "~", so the skeleton shows them as fully owned, with no "begun here" and no grade 11 limit, and end days 93 and 94 are asked to assess the full standard.
   - Script fix: read the "~" from the progression row, not days.csv.
2. `s05.md:1`: the title keeps "**...** (weeks 17 to 19)" markup. The question itself parsed correctly (`:14`).
3. `s05.md:85-91`: seven "not named by id" rows come from continuous course use.
4. `s05.md:40-42`: rights are "not stated" for 1845, 1851 and 1852 texts.

### math-grade-1 s03 (days 40 to 68): ready with fixes

1. `s03.md:1`: the compelling question is lost ("*What makes a sum easy to find?*", italic form).
2. `s03.md:30` lists the K retrieval ids mk-decompose-to-10, mk-fluency-within-5, mk-make-ten and mk-teen-ten-ones as owned. They are missing from the field 4 table, and `:46` "Builds on" lists their assumes instead.
3. `s03.md:66-71`: six K rows are marked "this course, last day 15/38, retrieval, not named by id", each with a TODO. These come from continuous use in units 1 and 2.
4. Junk retrieval rows:
   - `:79` is a 27-day span, "retrieval of within-10 addition/subtraction ...".
   - `:81` "retrieved on day 40." is a fragment.
   - `:82` "Retrieval openings never count as assessment evidence." is a rule, not a task.
5. `s03.md:103`: field 5 gives 1.OA.C.6 a full item row on day 57, while the day 57 note (`:93`) says that day is contributing evidence only and reuses earlier fluency observations.
6. `s03.md:156`: the Note (K.OA.A.3, K.OA.A.5, K.OA.A.4, K.NBT.A.1) is a false alarm caused by the retrieval ids.
7. Field 10 source-map rows match source-map.csv. The IM L8 standard K.NBT.A.1 is the base text's tag, not an error. The rows repeat "Keep base order; adapt language ... (harms learning: no ...)" 29 times.

### math-grade-5 s04 (days 42 to 54): ready with fixes

1. `s04.md:28` lists m4-fraction-times-whole and m4-mixed-numbers (retrieval ids) as owned.
2. `s04.md:45-46`: "Builds on" and "Leads to" are wrong, because they come from the retrieval ids.
   - "Builds on" lists the grade 3 rows m3-unit-fractions, m3-fractions-number-line and m3-equivalent-fractions. The unit's own rows assume m4-fraction-times-whole (progression).
   - "Leads to" lists m5-fraction-times-whole, which is unit 3 (already taught), along with m5-add-sub-unlike and m5-fraction-add-sub-problems. The real hands-on rows are m6-divide-fractions and m6-ratio-parts-problems.
3. `s04.md:62` "retrieval and unit 3 multiplication." lost "m4-mixed-numbers"; the day 49 note reads "m4-mixed-numbers retrieval and unit 3 multiplication".
4. `s04.md:66-77`: the day 53 note says "Reuse day 51 independent contextual division for 7c and fraction/mixed-number multiplication for 6; no repeated collection". Field 5 still gives 7c and 6 fresh day 53 rows, owned by "section 4.3", with no pointer to day 51 (assess blank). A writer will likely write new items and collect twice.
5. `s04.md:21-23`: 5.NF.B.7a and 7b show "Parts, by verb: whole standard", although each has interpret, compute, story context, visual model and inverse-check parts. The day 53 note lists them. "Each part of each code is asked" depends on the writer finding them.
6. `s04.md:15` "Hook for day 1" should be day 42.

### math-grade-8 s02 (days 21 to 36): ready with fixes

1. `s02.md:28` lists m7-scale-drawings, m6-four-quadrants and m7-proportional-graphs as owned.
2. `s02.md:44-45`:
   - "Builds on" gives grade 4 to 6 rows (m6-equivalent-ratios, m6-polygon-area, m4-protractor, m5-coordinate-system, m5-graph-points). It omits m7-scale-drawings and m7-proportional-graphs, which are the true assumes of m8-dilations-similarity, m8-transformations-coordinates and m8-slope-similar-triangles.
   - "Leads to" includes m8-rigid-motions, which is unit 1, already taught.
3. `s02.md:64, :77`: m7-angle-relationships gets a "not named by id" retrieval TODO. It is assumed by m8-angle-facts, which was taught in unit 1 and cited again here, so it is continuous use.
4. Retrieval rows:
   - `:71-72` duplicate one task (day 21).
   - `:74` "retrieval" (day 30) is lifted from a shortened-year note ("replacing its ordinary mixed retrieval").
   - `:75` is a fragment.
5. `s02.md:24`: 8.EE.B.6 is shown as a whole owned standard. Days 31 to 33 say "Begin slope through similar triangles; unit 3 completes the derivations and assesses the full code". The skeleton does not mark it begun, so the Limits TODO depends on the writer reading the day list. Field 5 correctly leaves it out.
6. `s02.md:84`: "Time: 50 minutes a day" for the day 28 mid, which the note gives as 10 minutes.
7. `s02.md:92-102`: day 34 retains "the similarity-and-measurement product as end-of-unit evidence" (assess blank). Field 5 does not name day 34 as a reused source for day 35.

### geometry s03 (days 49 to 67): ready with fixes

1. `s03.md:1`: the compelling question is lost. The title is "Similarity: How can a photo, a map and a shadow tell us true lengths?" (question after a colon, no quotes), and `split_title` misses it, so the hook TODO at `:14` has no question to tie to.
2. `s03.md:73`: the readiness table lists only m8-dilations-similarity. The day 48 note quoted at `:60` checks four rows: m8-dilations-similarity, m8-pythagorean-theorem, m7-scale-drawings and m6-equivalent-ratios. The other three are dropped because they sit in the skills column (`earlier_rows`). The TODO at `:66` asks for items "for each earlier-grade row the table below marks readiness", so a writer following it writes one item, not four.
3. `s03.md:32` lists m8-angle-facts, m6-equivalent-ratios, m7-scale-drawings and m8-pythagorean-theorem as owned.
   - `:47` "Builds on" lists grade 4 to 7 rows that are assumes of those ids.
   - `:48` "Leads to" lists m7-proportional-tables, m7-proportional-graphs, m7-circles, m8-rigid-motions and m8-transformations-coordinates. These are earlier grades, all from the hands_on of the retrieval ids.
4. `s03.md:23, :102`: the progression marks ~G-CO.C.10 on geo-similar-triangle-proofs, and days 53 and 66 teach only the midsegment theorem. The skeleton shows G-CO.C.10 whole, and field 5 asks for an item on the full standard (angle sum, isosceles base angles, medians). This is the same "~" loss as ELA 11.
5. `s03.md:103-104`: G-MG.A.2 and G-MG.A.3 get fresh day 66 rows. The day 66 note says "Reuse day 65 playground model ... unit 5 completes both, with no new model here." The skeleton has no "begun" mark and no reuse pointer.
6. Neither the frame unit row (`frame.md:102`) nor its standard list includes G-CO.C.10, G-MG.A.2 or G-MG.A.3, which days 53, 65 and 66 cite. This is a frame/days mismatch (data). The skeleton does not flag it.
7. Retrieval rows:
   - `:81` "retrieval." (day 62) is junk.
   - `:82` (day 67) "retrieve unit 3 Pythagorean and dilation work for unit 4" is next-unit retrieval credited to unit 3.
8. `s03.md:34`: ratio-table is labelled "introduced or first used here", while the frame (`frame.md:87`) says it was introduced in grade 6 and is being reactivated.
9. `s03.md:94-96`: the parent G-SRT.A.1 is listed with 1a and 1b, and the parent's "Part" cell is a stem ending in a colon.
10. `s03.md:8`: Weight shows "prerequisite (G-SRT.B)". In `ccss-math-focus.csv` G-SRT.B is marked "wap" (widely applicable prerequisite), not a course weight. A writer may read it as "not this course's content".

## Across the sample

### Script changes (scripts/unit_skeleton.py)

1. **`build()` / `earlier_rows`: own-grade and earlier-grade skills are mixed** (chemistry, ELA 7, math 1, 5 and 8, geometry; 6 of 12). Earlier-grade ids in the days.csv skills column (math lead call 4 and the same practice in science and ELA) cause four problems:
   - They are printed as "Progression skills owned".
   - Their assumes fill "Builds on", and their hands_on fill "Leads to", which then names already-taught rows (math 5, math 8, geometry).
   - They drop out of the field 4 table. In geometry this loses three of the four rows the readiness check covers.
   - They trigger the false field 10 "progression lists X but days.csv does not cite them" Note.

   Fix: split `skills` by the row's grade against the course grade, at the start of `build()`. Earlier-grade ids go to field 4 as retrieval or readiness rows, and only own-grade rows feed "owned", "Builds on" and "Leads to".
2. **`earlier_rows`: continuous use becomes a retrieval TODO** (ELA 3, 7, 11, math 1, 8). This produced 18 rows in ELA 3. Take assumes only from skills first cited in this unit, or skip a row whose last use is the previous unit of the same course.
3. **`retrieval_clauses`: junk rows** (chemistry, ELA 3, ELA 7, math 1, 5, 8, geometry; 7 of 12). It produces four kinds:
   - mid-clause fragments (`c[m.start():]` drops the subject)
   - rules ("never count as assessment evidence")
   - minute budgets
   - next-unit retrieval on a Respond day

   Fix: take the whole clause. Drop clauses with no row id, unit or day reference. Credit "for unit N" clauses to unit N.
4. **`split_unit_cell` / `split_title`: the compelling question is lost** (ELA K, ELA 7, math 1, geometry). Handle the italic, the quoted-with-"?" and the "Title: Question?" forms, and strip `**` and "(weeks ...)". Reusing the `split_science_cell` logic would cover most cases.
5. **The "~" (begun here) mark is not carried** (ELA 11, geometry), and neither is a "begun, unit N completes" note (math 8, geometry G-MG). Read "~" from the progression row's standard column when filling field 2 and field 5.
6. **Field 5 (in `build()`) ignores retained evidence and coverage.**
   - Rows come only from days with assess end, mid or observe. Owned codes collected on a blank-assess day vanish (science 7). A reuse-from-day-N note gets fresh rows (math 5, 8, geometry, math 1).
   - Add a "reused from day N" owner when the note says so.
   - Add a coverage line listing owned codes that are on no assessment day.
   - Drop the parent code from `full` when parts are listed.
   - Take the time from the note's minutes when it gives them (science K, math 8).
7. **Bulk: `field10_extras`, plus field 5 and the day list repeating notes.** Print one line per source-map row (id, our days, decision) and drop repeated boilerplate. Field 5 should not reprint the note shown in the day list. This is the main lever for ELA K to 2.
8. **Small wording fixes.**
   - The science field 10 TODO always asks for a base unit. Make it grade-banded: only grades 6 to 8 have OpenSciEd.
   - The K-2-ETS1-1 crosscutting cell should say "NGSS lists none".
   - "Hook for day 1" should name the unit's first day.
   - The hook and question-board TODOs overlap the Storyline and Carried TODOs.
   - `frame_models` says "introduced here" for reactivated models.
   - `group_column` needs near-duplicate merging.
   - `SAFEWORDS` needs tightening (drop "chemical", "harms").
   - `used_on` should not count a Respond or course-check day as a one-hop use.
   - The Weight line should spell out "wap".

### Data fixes (one course each)

- **science-kindergarten:** add the missing full stop before "Anchor:" at `frame.md:134`.
- **science-grade-7:** days 93 and 94 should carry assess=end, or day 95 should list MS-LS2-3 and MS-PS1-3.
- **science-grade-4:**
  - The day 36 note asks for 4-PS3-3 evidence that is not in its codes.
  - The frame check-set cell is still "Candidate", while day 34 says it was kept.
- **english-language-arts-kindergarten:** unit 4 is one 39-day section. Split it into sections.
- **english-language-arts-grade-11:** days.csv dropped the "~" on RI.11-12.3, RI.11-12.6 and SL.11-12.3.
- **geometry:** the frame unit 3 row omits G-CO.C.10, G-MG.A.2 and G-MG.A.3, which days.csv cites.
- **ELA texts (all ELA courses):** `ela-texts.csv` leaves edition and rights empty, including for public-domain and Curio Class-written texts. This is not one course, but it is a data fix, not a script fix.

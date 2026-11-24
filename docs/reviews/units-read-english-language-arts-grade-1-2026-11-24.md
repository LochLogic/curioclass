# Units read: english-language-arts-grade-1 (2026-11-24)

COURSE-RUN stage 4, Reads. Full pass across the four unit plans read together.

## What was read

- Unit plans s01.md to s04.md in docs/courses/english-language-arts-grade-1/, all fields and the day lists. I read them with the skel blocks stripped out (helper view.py) and then read the field 5 and field 10 tables in full.
- data/plans/english-language-arts-grade-1/days.csv (kinds, codes, observe and mid/end rows) and items.csv (s04-A7, s04-A8).
- data/progressions/ela.csv, the grade 1 rows and the kindergarten rows that grade 1 assumes.
- The kindergarten last unit (docs/courses/english-language-arts-kindergarten/s04.md) and grade 2 unit 1 (docs/courses/english-language-arts-grade-2/s01.md), checked for continuity.
- Written days I sampled to test plan claims: u02-1/d038, u04-1/d124 (the exit), u04-4/d139 and its cycle-22 sample words. I also read the goalmap audit dump, which lists the goal verb and exit ask for each day.
- The lead list (docs/reviews/lead-list-lens-pass-2026-11-17.md) has no items for this course.

## Verdict

The four units form a sound arc, and they hand off cleanly from kindergarten and into grade 2. Unit 1 covers tools and topics, unit 2 stories and foundations, unit 3 birds and research, and unit 4 comparison, opinion and informative writing. The serious problems were mechanical. Three plans failed the unitplan gate, because field 5 had no rows for observation and assessment codes and s04's field 2 left out an owned code. Two plans also misdescribed the course checks they hand off to. All of these are fixed. What is left is days.csv noise on cycle-sample days and frame-level spacing of three skill families. Neither can be fixed from a plan.

## Findings

1. **Serious, fixed.** Gate failures came from missing field 5 coverage.
   - s02: observe codes on 61 and 76 had no field 5 row. I added SL.1.1a to c to the day 61 row, added the L.1.2 parent-record row (72), and added the course-check row for the RF.1.1, RF.1.2, RF.1.3g and RF.1.4 parts (76).
   - s03: the RF.1.3 parent record had no row. I added a day 118 row that cites a and b from the course check and the other parts from this unit, and keeps the record open until vowel teams arrive on 155.
   - s04: field 2 did not name RL.1.3, so I added it (taught in unit 1, returning on 120 to 124). The day 139 mid/end codes RF.1.3e and L.1.2d had no rows, so I added rows from items s04-A7 (elbow) and s04-A8 (spray). These match written d139, so there is no day fault.
2. **Moderate, fixed.** s02 field 3 said day 77 rechecks unit 2. It actually rechecks unit 1's topic codes on new tool and bicycle content, while day 78 responds to this unit's RI.1.3 and RL.1.2. Unit 2's W.1.3 is rechecked on 159. The unit 4 paragraph line now names the peer feedback on 151. I rewrote field 3 to match days.csv.
3. **Moderate, fixed.** s04 field 3 said 158 to 159 reuse this unit's records. Day 158 collects the cumulative reading record with cycles 19 to 25. Day 159 rechecks RI.1.2, RI.1.5 and W.1.3 from units 2 and 3. Day 160 retries this unit's RI.1.8, RI.1.4, L.1.4 and W.1.1 gaps. I rewrote field 3 to match.
4. **Moderate, for the structure pass.** days.csv observe rows on the cycle-sample days list the whole foundations block of codes, plus SL.1.1a to c on 38 and 88. The real evidence for those codes is the course checks on 76 to 77 and 158 to 159, along with the discussion records on 61 and 88. The plans now carry rows that say so, but the ledger overstates what each sample scores (see the structure pass list below).
5. **Minor, for the structure pass.** sequence.py notes that day 45 is a Fluency day whose note says "teach".
6. **Minor, for Cory.** Some skill families are spaced unevenly across the year. e1-word-relationships (L.1.5, L.1.6) is taught in unit 1 only and never returns. e1-sentences (L.1.1j, L.1.2a to c) appears in unit 2 only, although unit 4 uses L.1.1j on 152. e1-grammar appears in unit 4 only. This is set at the frame level, so I made no plan edit.
7. **Minor, no change.** The field 5 Owner column holds the skel default "section N.1" in all four plans. The section plans name the real owners, and this column sits inside the uncounted skeleton, so the default does no harm.
8. **Minor, fixed.** UK spellings outside skel blocks (practise, practised, labelled, catalogue, licence) are now in US spelling, following AGENTS.md's fix-when-edited rule: 62 replacements across s01 to s04. Spellings inside skel blocks are left for the skeleton scripts. "recognise" is kept because it is a locked Goal map word.
9. **No change.** Exit and goal verbs: the audit dump shows only the first ask on picture-choice exits. The written days back the produce-level goals with spoken stems, for example d124 asks "What is one thing the same?" and "What is one thing different?". I found no drift.
10. **No change.** s01's statement "unit 4 returns to informative writing on 141" is correct, s03's field 3 hand-backs hold, and every review entry I traced points at taught rows. Loads match days.csv, and all four plans are under the 2300 cap (1794, 1815, 1772, 1854).
11. **No change.** Continuity holds from kindergarten into grade 1 and from grade 1 into grade 2. Kindergarten's last unit ends on the skills that grade 1 unit 1 retrieves on 6 to 9, and grade 2 unit 1 assumes skills that grade 1 units 3 and 4 close.

## Day faults

None. Every plan fix agrees with the written days.

## For the structure pass

- data/plans/english-language-arts-grade-1/days.csv, observe rows on the cycle-sample days (38 to 68 and the unit 4 cycles): trim the codes to the pattern codes the sample actually scores. Otherwise, add to each note "foundations parts scored on the course checks 76 to 77 and 158 to 159". Also drop SL.1.1a to c from the cycle-sample observe codes on 38 and 88, or note that they are scored from the discussion records on 61 and 88.
- days.csv day 45: change the note's "teach" to "practice", or change the day's kind to Understanding if teaching is intended.

## For Cory

- Skill-family spacing (finding 6): should word relationships (L.1.5, L.1.6) return after unit 1, and sentence conventions after unit 2? It would be a frame change, about two practice touches in units 3 and 4.

## Lead-list items worked

0. The lead list has no items for this course.

## Gates

- `unitplan.py check english-language-arts-grade-1`: 39 PASS, 0 FAIL. Before the fixes, s02, s03 and s04 failed.
- `sequence.py check english-language-arts-grade-1`: 0 failures, with 1 note (day 45).
- `goalmap.py audit english-language-arts-grade-1`: a reading dump of 619 lines. I read it for exit and goal drift and found none.

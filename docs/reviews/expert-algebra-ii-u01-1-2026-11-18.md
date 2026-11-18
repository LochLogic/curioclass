# Expert read: Algebra II, unit 1, section 1.1, days 1 to 5 (math probe, 2026-11-18)

One reader, the whole section, day by day in order, so cross-day faults show. Acting as docs/agents/EXPERT.md says; each day
judged as docs/pipeline/briefs/expert-day.md says (its reading list and its "Judge:" list; no cheap read this probe, so no
CATCH or CHEAP tags). Findings carry the origin and repeat tags that docs/pipeline/PROBE-GUARD.md asks for.

## What I read

- Rules: AGENTS.md, docs/agents/EXPERT.md, docs/pipeline/briefs/expert-day.md, docs/pipeline/PROBE-GUARD.md,
  docs/agents/lenses/math.md, docs/courses/LESSON-DAY.md (in full).
- Plans: unit plan docs/courses/algebra-ii/s01.md (fields 2, 4 and the day table), section plans u01-1.md (in full) and
  u01-2.md (days 6 to 7 and the exits E6 to E10, to test the hand-off from 1.1 into 1.2).
- Data, every row for the unit that touches days 1 to 5: items.csv (R1 to R3, X1 to X5, K, P, F, W5 rows), wrongs.csv,
  errors.csv, days.csv, handbacks.csv, materials.csv, parts.csv, words.csv.
- Days: d001 to d005 in full, and the nine pieces in courses/algebra-ii/u01-1/ (opener, readiness, record, family note,
  disk puzzle sheet, folding table, sort cards, rule cards, situation cards).
- Built pages after `python -X utf8 scripts/lesson.py build --pdf`: key, exit, student, home pages for days 1 and 5; key,
  exit and student for day 2; teacher and student for day 3; teacher and display for day 4. Two-side counts read from the
  gate output.
- Earlier probe reports for the REPEAT tag: the "Back to the builders" tables of probe-social-studies-2026-11-15.md,
  probe-social-studies-2-2026-11-15.md and probe-social-studies-3-2026-11-18.md, and the earlier answer-key read
  docs/reviews/answer-key-algebra-ii-u01-2026-11-18.md (its seven fixes are in the files I read, so I did not repeat them).
- Keys reworked by hand, not from the key page: R1 to R3, X1 to X5, K1-1, K2-1, K3-1, K4-1, K5-1 to K5-3, P1-1, P2-1 to
  P2-7, P3-1 to P3-8, P4-1 to P4-7, P5-1 to P5-6, F1-1, F3-1, F4-1, W5 (cards A to D, including the domain end of card A,
  p(12) = 0). Every computed key is right. Every wrong answer on these rows recomputes as shown. The problems below are in
  what the items ask, what the days promise and how the days fit together.
- Gates: `plan.py check` for algebra-ii shows 14 failures, none in days 1 to 5: the three known units.csv lines, days 6 to
  14 with no exit row or minutes, and two source-map rows outside this read. `lesson.py check` shows days 1 to 5 and the
  nine pieces at 0 failures; teacher prose 625 to 732 words (cap 750 at 50 minutes), student pages 2 sides, at home 35 to
  40 minutes. Notes: d002 student page order, d005 hand-backs to the unwritten day 6.
- Outside sources: none read. The judgments on teaching are from memory of how a grade 11 class meets sequences and from the
  lens page.

Not opened: anything on the never-open list.

## Verdict per day

- **Day 1.** Sound. The disk puzzle, the 1, 3, 7 table and the "twice the one before, plus one" rule are right, the 50
  minutes add up, and the exit asks the day's goal. Fault: the 5-minute Talk holds an Ask, a class sentence, a fix and a
  neighbor check (finding 10).
- **Day 2.** Needs fixes before it is taught. The opening 10 minutes carry more repair than they can hold (3), the retry for
  readiness item 3 does not retry the skill missed (4), the day never models a rule with a start other than 1 although the
  pairs and the exit need it (8), and the folding task is under-specified (9).
- **Day 3.** Sound and the best-built day. The six cards check out (29, 162, 4, 40, 16, 13), the plot has a real purpose and
  the exit measures difference against ratio with fractions and a negative step. Minor: the dot graphs name every dot, so no
  day has students read a graph (16).
- **Day 4.** Weakest day. The exit asks students to read recurrence notation that day 5 teaches (1), the fix-it item marks a
  legitimate table wrong (2), and the demand is low for grade 11 (13).
- **Day 5.** Right mathematics, dense day. Start, rule, domain and the two-seed function idea in 35 minutes is the most the
  period holds. The exit's look-fors say more than the sheet (7), and what the day hands to day 6 cannot fit day 6 (5).

## Findings, most serious first

1. [d004 exit X4; E4 in u01-1.md] The exit gives "b(0) = 100 and b(n) = 0.8 b(n-1) for integers n at least 1". Recurrence notation and the domain phrase "integers n at least 1" are first met on day 5 (K5-1); day 4 is a fluency day whose cards and worked example are all in words, and says "no new idea is taught today". | The exit measures whether students can read notation they have not been shown, so a wrong answer cannot be told from a misread symbol, and error B and C counts on the record sheet are polluted. The day's goal is applying a rule repeatedly. | Write X4 in words: "b(0) = 100 and each next term is 0.8 times the term before. (a) Find b(1), b(2), b(3). (b) A classmate plotted (1, 80), (2, 64), (3, 48) ..." with the same answers and wrong rows; change E4 in u01-1.md the same way. Day 5 then introduces the notation as new. | origin=section | repeat=new

2. [d004 F4-1, Words and supports, Ask "Where does the start belong"] The fix-it says "start at 6 and multiply by 3", a student table 6, 18, 54, 162 plotted at n = 1 to 4, and the key calls that wrong because the start "belongs at n = 0". The stem never says n begins at 0. Days 1, 5, 7 and 8 start sequences at index 1 (chain 1, m(1) = 4), the Words line says "Start: the term at n = 0", and day 5 needs "the starting value with its index". | A student who reads the stem as written has a correct sequence and is told it is wrong; the day teaches a convention as if it were mathematics, one day before day 5 says the start can be at any stated index. | Stem: "A student builds a table for n = 0, 1, 2, 3 for 'start at 6 and multiply by 3 each time' and gets 6, 18, 54, 162. They plot (1, 6), (2, 18), (3, 54) and (4, 162)." Keep the key. Words: "Start: the first term, here the term at n = 0." Ask: "The table was set up for n = 0, so where does 6 go?" | origin=unit | repeat=yes

3. [d002 10 min Warm-up and repair] Five minutes of retrieval, then "five minutes of repair" that must cover readiness items 1 to 3 (errors G, B, C), the day 1 exit (errors C and D, both needing a board example worked twice), a whole-class or small-group split, and a fresh independent retry for every student who missed anything (P2-3 and P2-4, each two parts with justification). s01 field 4 gives the same five minutes. | The repair either runs over into the folding (the day's 15-minute pairs part is already full) or is a pretence; the day 2 exit then measures students who were never repaired. A teacher with 30 papers cannot mark, group and retry in 5 minutes. | Cut the retries to the items missed by more than a third of the class, one board example per error (not two), and move the independent retries for the rest into the first 6 minutes of the pairs part while they fold (the strip needs no thought for the first two folds). Say so in the day, and change field 4's "finish within the ten minutes" in s01.md to match. | origin=unit | repeat=yes

4. [d002 retry for readiness item 3; items P2-2, P2-3, P2-4] The day says "the warm-up above is the retry for items 1 and 3". For item 3 it is not: R3 asks students to write p(n) from a start of 40 and a factor of 0.25 (errors B and C), and P2-2 only evaluates a rule already written, v(n) = 6(2)^n. The ids skip P2-5, so a retry row seems to have been dropped. | Students who missed the one Algebra I skill the whole unit leans on (writing a start-times-power rule) are marked "retried" without being asked to do it. | Add s01-P2-5 as the item 3 retry with new numbers: "A quantity starts at q(0) = 90 and is multiplied by 0.2 at each step. Write q(n) and find q(2)." (q(n) = 90(0.2)^n, q(2) = 3.6; wrongs: 90 + 0.2n, error B; 90(0.2)^(n-1), error C.) Print it on Side 2 under "Retry" and change the sentence to name it. | origin=day | repeat=new

5. [d005 Tomorrow; u01-1 error table "opening day 6"; u01-2 day 6] Day 5 sends day 6 the repair for error A (5 minutes), D (8) or I (10), "the most common first", and the written task back for a revision note. Day 6 in the section plan opens with a 5-minute retrieval warm-up, then the 8-minute example, 25 minutes of pairs, a 7-minute talk and the exit. The day 6 file is not written; its writer is handed 5 to 23 minutes of repair and a handback with no slot. | The hand-off is promised on one side and has no room on the other, which is how earlier probes ended with repairs squeezed out. | In u01-2.md day 6, turn the warm-up into "10 min. Return and repair": the revision note on W5 (3 minutes), then one repair, the most common of A, D or I (7 minutes), with retrieval folded into the worked example; take the 3 minutes from the 7-minute talk. In u01-1.md the error table's minutes for A, D and I become 7 each. | origin=section | repeat=yes

6. [hand-off 1.1 to 1.2: days 2 to 5 against u01-2 day 7] Section 1.1 teaches the explicit form for a geometric sequence only (day 2) and the recursive form for an arithmetic one (day 5). No day teaches the explicit arithmetic rule; day 8 "derives" it. Day 7 is an application day ("nothing is taught as new") whose worked example has students write "the recurrence and the explicit rule" for loaves that rise by 5, and E7(b) shows r(n) = 6 + 3(n-1) with error C on 6 + 3n. | A class arrives on day 7 asked to write an arithmetic explicit rule that is first taught the next day, so day 7 either teaches it (and day 8 repeats) or fails. Section 1.1 also leaves F-BF.A.2 half started with no day that says so. | Choose one: (a) day 7 asks for the recurrence only and E7 accepts the recurrence, the explicit form moving to day 8; or (b) add to day 5 or day 7 a 5-minute "a + d(n - first index)" step. Recommend (a), since day 8 is already built to derive it and the section plan says so. Record the choice in u01-1.md section 1 under F-BF.A.2. | origin=section | repeat=new

7. [d005 exit X5, its look-for 2; E5 in u01-1.md] Look-for 2 asks for the recurrence, "the integer domain, ending at stop 8 because v(8) = 6". The sheet never says the bus has a last stop and asks only for "start, rule, domain". A student who writes the domain exactly as K5-1 and P5-4 modelled ("integers n at least 1") fails the tick though the idea is shown. The wrong rows for the domain are not in the register (the P5-6 rows are filed x), so Tomorrow for day 5 cannot name the likeliest miss. | A look-for that says more than the sheet marks a correct reading wrong, and the day 6 repair then guesses between A, D and I when the likeliest error has no letter. | Stem (a): "... start, rule and domain (the stops where the rule still makes sense)". Split look-for 2 into two: the recurrence with integer inputs, and the end of the domain with its reason. Add a wrong row "(a) v(0) = 70 and v(n) = v(n-1) - 8 for integers n at least 1: the domain runs past stop 8" filed x, and name it in Tomorrow. Update E5 and `exitlooks` on the record sheet. | origin=section | repeat=yes

8. [d002 12 min Worked example; 15 min Pairs; exit X2] The worked example ends at L(n) = 2^n (start 1, factor 2). The pairs then write P(n) = 3(2)^n and the exit asks S(n) = 12(5)^n, but nothing on the teacher page models how a start other than 1 enters the rule. The only support is readiness item 3, which the previous finding shows is not retried. | The day's goal is "track repeated multiplication"; most of the class writes 5^n or 12 x 5 x n on the exit, errors the register does not name, and the day 3 repair list (B, C, G) misses them. | Add a third worked step after L(3): "Start with 3 squares and double: 3, 6, 12, 24; the table is 3 x 2^n; the first number is the start, the second is the factor" and a frame "term = start x factor^position" on the folding table and in Words and supports. Add a line to Tomorrow for a rule that drops the start. | origin=day | repeat=new

9. [d002 materials, 12 min and 15 min parts; folding-table.md "Area of one layer"] (a) "A long strip of scrap paper" folded in half five times: the length is not stated, and a strip under about 30 cm cannot be folded five times by hand. (b) The students "open it to count layers": unfolded, they count sections, not layers, and the keyed word is "layers". (c) The area column has no whole to measure from and no key; the section's items never use it. | Pairs spend the 15 minutes on a folding task that jams at fold 4 or 5, and an unkeyed column invites fractions that nobody marks. | Say "a full sheet of paper cut lengthwise, at least 25 cm by 4 cm; four folds are enough, the fifth is on paper only"; say "after each fold, count the sections that show when you open it; each section was one layer". Either delete the area column or write "call the strip's area 1" and add its values 1, 1/2, 1/4, 1/8, 1/16, 1/32 to the folding table's teacher line. | origin=day | repeat=new

10. [d001 5 min Talk; d004 7 min Check and fix; d005 5 min Pairs write] Three parts hold more than their minutes. Day 1: an Ask, a sentence written from the class, then F1-1 "alone, in one minute" (replay a 5-disk case, name the missing move, give 31) and a neighbor check. Day 4: a swap of six tables and plots with a partner, one question each, then F4-1 alone. Day 5: pairs read a situation card, write start or starts, recurrence and domain, and a reasoned sentence in 5 minutes (card D has two seeds). | Students are rushed in the parts where the day's idea is said aloud, and the teacher drops the check or the talk first. | Day 1: make F1-1 the pairs' last step in the 10-minute part and keep Talk to the Ask and the class sentence. Day 4: the partner check covers cards 3 and 6 only. Day 5: take 2 minutes from Two seeds (the pairs list is written by the teacher) and give pairs 7 minutes. | origin=day | repeat=yes

11. [d002 Warm-up and repair; d003 Worked example; d004 Worked example; others] The teacher prose puts an item id in the middle of a sentence and the build expands the whole stem and answer there. The built d003 page reads "Put both tables from Table X gives 6, 10, 14, 18 ... [X adds 4 each step ...] side by side on the board", and d002 reads "the retry is Retry, for day 1's ticket. Chain 1 has 5 beads ... [Chain 4 has 17 ...]". | A teacher who reads the page the night before cannot follow the sentence; the plain-words and "reads fast" tests fail on the page that was built, though the source reads well. | Add a `lesson.py check` note when an `[[id]]` is followed or preceded by words on the same line, and have the build print a short label ("the day 1 retry") in prose instead of the stem; until then writers put an id on a line of its own. Reword these three days' sentences so each id stands alone. | origin=template | repeat=new

12. [wrongs for s01-X2 (36), s01-P2-6 (12), s01-K2-1 (L(3) = 4)] Error G is assigned to S(3) = 36 ("S times 3, with S = 12") and P(4) = 12 ("P multiplied by 4, with P = 3"). S and P are function names with no value; the real student error behind 36 and 12 is "start times position", a linear rule for a doubling or quintupling pattern. The G repair (trace the input through a labeled table) does not fix it, and Tomorrow for day 2 names it G. | A teacher who sees 36 is sent to the wrong repair; the other G rows (h(2) = 8n - 6, q(3) = 6n + 15, g(5) = 15n - 20, u(6) = 42n + 6) are real and correct. | Refile both numeric rows as error B (a linear rule where the pattern multiplies: 12 x 3, 3 x 4) or x, and delete "error G: 36" from day 2's Tomorrow; add a line for the start-times-position answer (finding 8). | origin=unit | repeat=new

13. [d004 25 min practice; P4-1 to P4-6, rule-cards.md] Day 4 is six table-building cards (add 7, times 5, subtract 6, times 1/3, add 4, times 3), three of them near copies of the day 3 cards. For grade 11 the arithmetic is below the course (grade 5 to 6) and the day's only demanding step, the plot, has no scale: cards 2 and 6 reach 250 and 567 on graph paper and the class is not told how to choose the axes. | The period is long on easy work and short on the part a student could get wrong, so day 4 produces little evidence beyond the exit and its fluency label is not earned. | Keep four cards (1, 2, 4, 6), give a scale on the two that need one ("one square is 50 for card 2"), and add two harder cards: a decimal ratio (start 200, times 0.9) and a negative change (start 15, subtract 4 until below 0, how many terms are positive). Day 4 then carries the 'reading a rule in words' that finding 1 moves out of the exit. | origin=section | repeat=new

14. [teacher page header, days 1 to 5] The header prints "Standard parts: see the section opener", but the opener names no standard (it holds no F-IF, F-BF or F-LE code). It also prints "Tool: None" on days 3 and 4 while days.csv names a coordinate graph and a graphing calculator and the day text says "the tool is a coordinate graph, light". | A teacher looking for the standard follows a pointer to nothing; the header contradicts the body. | In `lesson.py` the fallback for parts that are `whole` should list the codes from days.csv for the day; the tool field should read the days.csv `tools` column when no tool rows exist, as "coordinate graph (light, optional)". | origin=template | repeat=new

15. [answer key, opening line, all five days] Each key opens with "Any equal form of an equation is right: ... (n x 9 = 36, 9 x n = 36 ...)". The note is for multiplication fact equations; here the answers are rules such as S(n) = 12(5)^n and recurrences, for which "factors in either order" is not the rule a teacher needs (12(5)^n and 5^n x 12 are equal; 5 x 12^n is not). | A teacher marking 30 exits reads advice that does not apply, and nothing says which forms of a rule or recurrence are accepted. | For high school the key should open with the line for rules: "Any equal rule is right (12(5)^n = 5^n x 12); a recurrence needs its starting value and its domain." Change the trigger so the grade 4 sentence prints only in a course whose standards are 4.OA. | origin=template | repeat=new

16. [sort-cards.md cards C and F; X3 stem; P3-8] The two "dot graph" cards print every dot's coordinates beside it, and the exit gives graph Q as the points (0, 47), (1, 41), (2, 35) in words. Students never read a value off a graph in this section, though F-LE.A.2 says "given a graph" and day 6 opens with graphs. Card F's n-axis sits at y = -4, not at zero, with ticks only at -4 and 10. | The graph part of the standard is practised as a table, and day 6 meets the first real graph reading with no earlier step. | Print cards C and F with a grid and axis ticks and no coordinates beside the dots, and keep the coordinates in the key; draw card F's axis at zero. Leave X3 as it is. | origin=day | repeat=new

17. [errors.csv row A; wrongs for s01-P5-4 "m(0) = -2"] Error A is defined as "allows noninteger inputs", but P5-4's second A row is an integer outside the domain (m(0) with the domain starting at 1). | A teacher recording by letter counts a different misconception under A, and the day 6 repair (an input line) is right but the register and the Tomorrow line say something else. | Widen A to "allows an input outside the domain: a noninteger, or an integer before the start" in errors.csv, the opener's table and u01-1.md. | origin=unit | repeat=new

18. [handbacks.csv; u01-1.md days 2 and 4 text; section 11] Handbacks list only the readiness items for day 1 to 2, but d002 also returns the judged day 1 exit s01-X1 with a retry (P2-3), and X5 is judged and handed back to day 6 with no row. The section plan still says day 2 sorts six statements (the item has four) and "still to make" the exit sheets and record sheet, which now exist. | Rows the gate cannot see go stale, and the day 6 writer will not find X5 in handbacks.csv. | Add `1,2,s01-X1,retry,...` and `5,6,s01-X5,warm-up,...` rows; change "six statements" to "four" in u01-1.md day 2 and cut the made pieces from section 11. | origin=unit | repeat=new

19. [d005 print line, situation-cards.md; record sheet W5] The print line says "Per pair: the situation cards (cut into four cards)" while Before class says "one card for each pair", so 15 pairs would print 15 sheets to use one card each. W5 is written by a pair and the record sheet ticks W5 per student, so one pair's work is recorded as two students' evidence. | A teacher prints 60 cards for 15; W5 shows as individual evidence when X5 is the only individual item. | Print line: "Per class: four situation card sheets, cut into 16 cards; each pair takes one." In the day and the record sheet note that W5 is recorded for both partners and X5 is the individual measure. | origin=day | repeat=new

## Does 1.1 hand off to 1.2

Mostly. Day 5 ends on recurrence, starting value and domain and day 6 opens by connecting a recurrence to its table and graph, which is what 1.1 supplies. Three things do not travel: the explicit arithmetic rule that day 7 needs (6), the repair and hand-back time day 6 has no slot for (5), and a first graph reading (16). Section 1.2's day 6 mismatch routine repeats day 4's F4-1 error (a start plotted at n = 1), so finding 2 matters for that day too.

## What is right and should not be touched

- The readiness design (three Algebra I items after the hook, results recorded, repair at the head of day 2) is the correct
  order, and its wrong answers (h(2) = 8n - 6, B is linear so 36 or 33, 40(0.25)^(n-1)) are real student errors.
- The day 1 hook and worked example: pairs find 1, 3, 7, the rule is said in words, no formula is handed over.
- Day 3: equal steps only, fractional and negative ratios in the cards, the plot as dots with "what would a line claim at 1.5".
- Day 5's two-seed example answers the false idea (error I) with an index and term table, not an assertion.
- Every key is exact (10/3, 51.2, 40.5) and worked.

## Could not judge

No class has used any day, so timings are my reading, not data. Prose caps are by the gate. I did not read days 6 to 14
beyond the section plan lines I cite.

## Counts

Findings: 19. By origin: day 6, section 5, unit 5, scope 0, frame 0, template 3. By repeat: yes 5, new 14.

Plan share as PROBE-GUARD measure 1 defines it (unit, scope, frame, template): 8 of 19, 42 percent, over the 35 percent line;
with section origin counted as plan, 13 of 19, 68 percent. No finding has origin frame.

## Fix

1. FIXED: X4 and E4 now give the rule in words (same answers, same wrong rows); day 5 introduces the notation.
2. FIXED: F4-1 stem says the table is set up for n = 0; Ask, key, steps, at-home Say and Words line agree.
3. FIXED: day 2 repair limited to items missed by over a third, one board example per error, retries done in the first six minutes of the pairs part; s01 gap response, u01-1 day 2 and handbacks match. To stay under the 750 cap and two sides, some prose was cut and the pairs item moved to Side 1.
4. FIXED: added s01-P2-5 (q(0) = 120, times 0.2; wrongs B 120.4, C 24) as the check item 3 retry, item 8 on Side 2. The id gap was K2-1 taking n = 5, not a dropped row.
5. FIXED: u01-2 day 6 opens with 10 minutes (3 revision note, 7 repair), retrieval folded into the worked example; 3 minutes from the talk and 2 from the pairs (so the day stays 50); errors A, D, I repairs are 7 minutes in errors.csv, u01-1 and day 5 Tomorrow.
6. FIXED: option (a). Day 7 and E7 ask for the recurrence only; the explicit arithmetic form is first taught on day 8; recorded in u01-1 section 1.
7. FIXED: X5 stem asks for the domain, look-for 2 split into recurrence and domain end (four look-fors), new x wrong row for a domain past stop 8, named in Tomorrow; E5 and record note updated. Stem kept short so the exit slip still fits.
8. FIXED: worked step 4, 8, 16, 32 gives 4(2)^n with the frame "term = start x factor^position" in the day, folding table and Words; Tomorrow names the dropped start (125, new x row).
9. FIXED: strip is a lengthwise cut at least 25 cm by 4 cm, four folds, fifth row by doubling, sections counted after each fold; area column deleted (day, folding table, u01-1, materials.csv).
10. FIXED: F1-1 moved into day 1 pairs; day 4 partner check is cards 3 and 6; day 5 Two seeds 7 minutes and Pairs write 7.
11. LEAD: lesson.py should note an item id sharing a line with words and print a short label, not the stem, in prose. The named sentences in days 2 and 3 were reworded meanwhile.
12. FIXED: S(3) = 36 and P(4) = 12 refiled as x; day 2 Tomorrow and day 3 warm-up repair updated.
13. FIXED: cards 3 and 5 replaced by 200 times 0.9 and 15 minus 4 (count positive terms); scales on cards 2, 3 and 6; items, cards and plans agree. Plan said keep four of the old cards; the two replaced were the near copies.
14. LEAD: lesson.py should list the days.csv codes for whole parts and read the days.csv tools column when no tool rows exist.
15. LEAD: choose the key's opening line by standard (grade 4 equation sentence only for 4.OA; a rule and recurrence line for high school).
16. FIXED: cards C and F print a grid and ticks with no coordinates, card F axis at zero; P3-3 and P3-6 stems say to read the dots from the card.
17. FIXED: error A widened in errors.csv, opener and u01-1.
18. FIXED: handbacks rows for X1 and X5 added, W5 minutes set to 3; u01-1 says four statements and "still to make" is cleared.
19. FIXED: day 5 print line is four sheets cut into 16 cards; day and record sheet say W5 is recorded for both partners and X5 is the individual measure.

Count: 19 findings. FIXED 16, REJECTED 0, LEAD 3 (11, 14, 15, all origin template).

# Fix: social-studies-grade-3 unit 7 (2026-11-17)

Findings: 31 raw (assessment 13, sources 10, sequence 8), 29 after merging. Fixed in s07.md: 20. LEAD: 9 items below. Rejected: 0. Held up: assessment 13 of 13, sequence 8 of 8 (4 in part), sources 10 of 10 (6 need research and are LEAD).

Word cap: fields outside 4 to 6 were at 1,244 of 1,250, so every fix there was made word-neutral by rewriting field 7 and trimming only text I added. Gate: `unitplan.py check` PASS for s07.md (the two "(A, D)" and "(A, B)" notes are gone).

What changed:
- Field 7: self-marking and "hands up" sentences removed; day 159 is thirty unaided plus ten unscored reflection; marking time stated; component-to-move folded into four groups (people and sources; maps; explanation and questions; action), the rest in pairs.
- Field 5: P0a scores only the day 146 and 147 records; P0b is practice only, MA.3.T6.1 scored from Q2 alone; day 142, 144, 145 and 153 records are practice only; P3 defined with look-fors and anchors; Q4 sample has a result for each action; Q1 and P0a wrong answers split to one letter each; J added to Q1 (item reworded to name a worker group); day 149 exit letter E changed to P; B no longer holds the Massachusett account or Wheatley (both taught); Q1 C-part sample marked provisional, Q5 sample made a template; minutes recounted Q1 9, Q2 6, Q3 3, Q4 4, Q5 8; Q3 asks about a person (group and continuity judged from the day 150 notes only, since 149 is first-day work); P2 has one fallback rule (school adult hears it by 158 and initials); day 158 revises only the two flagged components, does not fold; day 145 gains the two-column local work record (the Labor History Card); day 152 summary covers the biography and the interim answer; a five-minute overlap model opens day 147, with a fold rule; E rights line fixed before 141.
- Fields 2, 3, 8, 10: sources tied to days (Local Nation Account 142, Local Interview 146, Labor History Card 145); carried models corrected to units 2, 4, 5 and the unit 6 handoff; map-key retrieval on 143 is now the title and scale reading; supplies extended and the interview is a transcript; the "pending" P2 sentence deleted; day 156 limits marked "ours, untested"; Bisceglia interview is transfer card C only; market photograph and Boston origin chart dropped; Tennessee row deleted; the three new items added to "Still to make".

Decisions on partial fixes: assessment 2 and 11 use the day 146 and 147 and the day 150 records only, because 142 and 149 are first-day work (UNIT-PLAN field 5). Sources 7 is fixed only for the Boston figure choice.

REJECTED: none

LEAD:
- days.csv, items data: if item minutes are held in data, set Q1 9, Q2 6, Q3 3, Q4 4, Q5 8 (assessment 10).
- days.csv: day 147 note should add the five-minute overlap model at its opening (sequence 3).
- scope-and-sequence and days.csv: day 158 is typed Fluency and holds a fresh observed performance; scope-and-sequence lists 158 as compressible but days.csv does not (sequence 4).
- Research needed, sources 1: name a rights-clear interview (NPS or Library of Congress oral history) to replace transfer source C and record where its words were checked.
- Research needed, sources 2: name the free source and edition for William Cooper Nell, the New England Freedom Association and the Wheatley letter (recipient, date, printing), or swap the day 153 case.
- Research needed, sources 3: give the New York K-8 comparison a URL and edition.
- Research needed, sources 4: inspect the Long Wharf engraving and record what was seen.
- Research needed, sources 6: name pages and mark reached or not reached for the Cheyenne and Arapaho Tribes, Northern Arapaho Tribe, Northern Cheyenne Tribe, two scholarship and two immigrant-voice sources.
- Research needed, sources 7 and 9: dated "As of November 2026" lines for the local nation and Boston figures, the news and legal check made, LOC item URLs for the Carleton and Buell maps, and a stated quotation limit for the nation pages.
- Research needed, sources 8: cite the state or district student-project and visitor guidance for day 156 (marked "ours, untested" meanwhile).

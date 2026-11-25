# Skel census by cause (consolidation 4.E2 step 1)

Read with groups.md (the 1841 hand lines in 34 groups, each with a suggested outcome, for Cory to mark: 4.E2 step 2) and hand-list.csv (every hand line, with its group, the closest line of today's render and the words only the plan has). Stale lines (data wins, nothing to do) are in census.csv with the reason.

Command: `python -X utf8 scripts/skel_census.py --pickaxe` (report only).

- 916 written plans with skel blocks, 63244 block lines; 6250 distinct lines per plan are not in today's fresh render.
- By cause: stale 4384, unit-prose 12, pickaxe 13, hand 1841.
- Hand lines by suggested outcome (after `--regroup`): discard 818, check 613, back-port 298, move 112.
- Hand lines in plans with no generated baseline in git (social studies unit plans and others): 212.

| Course | stale | unit-prose | pickaxe | hand |
|---|---|---|---|---|
| algebra-i | 11 | 0 | 0 | 16 |
| algebra-ii | 9 | 0 | 0 | 15 |
| biology | 9 | 0 | 0 | 12 |
| chemistry | 10 | 0 | 0 | 15 |
| civics-government-and-civic-life | 40 | 0 | 0 | 4 |
| economics | 36 | 0 | 0 | 0 |
| english-language-arts-grade-1 | 168 | 0 | 0 | 6 |
| english-language-arts-grade-10 | 4 | 0 | 0 | 6 |
| english-language-arts-grade-11 | 16 | 0 | 0 | 13 |
| english-language-arts-grade-12 | 3 | 0 | 0 | 3 |
| english-language-arts-grade-2 | 221 | 0 | 0 | 252 |
| english-language-arts-grade-3 | 335 | 7 | 0 | 9 |
| english-language-arts-grade-4 | 221 | 0 | 0 | 4 |
| english-language-arts-grade-5 | 10 | 0 | 0 | 34 |
| english-language-arts-grade-6 | 18 | 0 | 0 | 4 |
| english-language-arts-grade-7 | 15 | 0 | 0 | 3 |
| english-language-arts-grade-8 | 5 | 0 | 0 | 11 |
| english-language-arts-grade-9 | 21 | 0 | 0 | 7 |
| english-language-arts-kindergarten | 395 | 0 | 0 | 88 |
| geometry | 33 | 0 | 0 | 35 |
| math-grade-1 | 6 | 0 | 0 | 165 |
| math-grade-2 | 5 | 0 | 0 | 193 |
| math-grade-3 | 1 | 0 | 0 | 191 |
| math-grade-4 | 21 | 0 | 0 | 2 |
| math-grade-5 | 0 | 0 | 0 | 21 |
| math-grade-6 | 34 | 0 | 0 | 162 |
| math-grade-7 | 3 | 0 | 0 | 16 |
| math-grade-8 | 0 | 0 | 0 | 16 |
| math-kindergarten | 884 | 4 | 0 | 69 |
| physics | 5 | 0 | 0 | 16 |
| science-grade-1 | 69 | 0 | 0 | 7 |
| science-grade-2 | 51 | 1 | 0 | 9 |
| science-grade-3 | 111 | 0 | 0 | 20 |
| science-grade-4 | 219 | 0 | 0 | 17 |
| science-grade-5 | 220 | 0 | 0 | 7 |
| science-grade-6 | 4 | 0 | 0 | 99 |
| science-grade-7 | 119 | 0 | 0 | 17 |
| science-grade-8 | 125 | 0 | 0 | 5 |
| science-kindergarten | 75 | 0 | 0 | 10 |
| social-studies-grade-1 | 67 | 0 | 0 | 3 |
| social-studies-grade-2 | 101 | 0 | 1 | 10 |
| social-studies-grade-3 | 86 | 0 | 0 | 90 |
| social-studies-grade-4 | 212 | 0 | 2 | 42 |
| social-studies-grade-5 | 139 | 0 | 8 | 50 |
| social-studies-kindergarten | 37 | 0 | 0 | 12 |
| us-government-and-politics | 24 | 0 | 2 | 3 |
| us-history-i | 37 | 0 | 0 | 10 |
| us-history-ii | 13 | 0 | 0 | 8 |
| world-geography-and-ancient-civilizations-i | 35 | 0 | 0 | 22 |
| world-geography-and-ancient-civilizations-ii | 23 | 0 | 0 | 2 |
| world-history-i | 33 | 0 | 0 | 3 |
| world-history-ii | 45 | 0 | 0 | 7 |

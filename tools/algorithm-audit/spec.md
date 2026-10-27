# Algorithm Audit

## One idea
A school district picks who gets the 40 summer robotics camp seats with a point formula that never mentions where anyone lives, yet Riverbend gets 8 seats to Hillside's 32 from equally strong applicants: you find out why with twin tests (the same student, one answer changed), rewrite the rules, and then defend your new formula at a board hearing where every fix costs someone something.

## Not like
- model-mechanic (6-8, ml-lab): repairs a model that learned from photos. Here nothing learns; the algorithm is six written rules, and the bias comes from rules that look neutral but stand in for a neighborhood.
- ai-evaluator (9-12, ml-lab): measures a trained model's errors by slice and decides whether to ship it. Here you change the rules yourself and argue the tradeoffs with people who lose or gain.
- biased-bot (4, ml-lab): missing training examples. Here no data is missing; every applicant is counted, and the unfairness is in what earns points.
- misleading-charts (6-8, this group): a picture of data lies. Here the numbers are shown honestly; the decision rule is what is unfair.
- data-policy-council (9-12): writes a privacy policy. Here the subject is fairness of an automated decision, with a twin test as the evidence.
- conflict-coach (6-8) and decision-tree (6-8): personal choices. This is a public rule that decides for 120 students at once.

## Who and how
- Grades 6 to 8, computer science. Module: Algorithms and Fairness (Computing and Society), "Bias and ethics in everyday algorithms". Topic line: "testing an algorithm for fairness".
- Driver: students in pairs on laptops; the Hearing works well with a teacher on a projector and the class taking the board members' parts. 25 to 40 minutes.
- Standards (CSTA 2026 ids from the module): MS-ALG-IM-10, MS-ALG-IM-11, MS-SOC-CE-45. 2017 crosswalk: 2-IC-20 (compare tradeoffs of computing technologies that affect people's everyday activities), 2-IC-21 (discuss issues of bias and accessibility in the design of existing technologies), 2-AP-17 (systematically test and refine programs using a range of test cases). References: paired testing ("audit studies"), as described in Sandvig et al., "Auditing Algorithms" (2014); proxies and disparate impact, as in Barocas and Selbst, "Big Data's Disparate Impact" (2016).
- tool.json: driver "students or teacher", minutes "25-40", modes ["Audit", "Hearing"], grades_label "Grades 6-8".

## Screens and modes
Kit frame, own `:root` (a manila audit file). Header: title "Algorithm Audit", small line "Cedar Valley Summer Robotics Camp"; mode buttons "Audit" (magnifier on a page icon) and "Hearing" (gavel icon); Motion, Sound, Read.

### Mode 1: Audit (opens first)
Stage, top: the "Seat map": 40 seats as a grid of chairs, each filled with its student's neighborhood badge (Hillside green circle, Riverbend orange triangle) and a readout row: "Hillside 32 seats of 60 applicants. Riverbend 8 of 60." Stage, below: one of three audit views, chosen by tabs:
- "Rule check": a table, one row per rule, with the district's reason, its points, and how many applicants in each neighborhood earn it (count and a small bar each). Grades show each neighborhood's average.
- "Twin test": a pair of applicant cards side by side. Left: any applicant, picked from a searchable list (number, neighborhood, score, seat or no seat) or with "Show me a close call" (picks applicant 108). Right: the twin, identical, with each answer as a switch. Flipping one switch recomputes the twin's score, rank and seat; a line reads "Same student. One answer changed. Rank 42 becomes rank 10." Only one switch may differ at a time (flipping a second one resets the first, with the hint "A twin test changes one thing").
- "All applicants": the 120 applicants as a sortable `table` (number, neighborhood, grades, each rule's yes or no, score, rank, seat).
Panel:
- `#hint`.
- "The formula" section: the six rules as code-like lines (`points += 15 if applied_first_week`), each with a points picker and, where offered, a "Change rule" picker (below). A line "Ties go to the lower applicant number (numbers were given out in alphabetical order)." A "Lottery" switch replaces the formula with "Lottery among applicants with grades 2.5 or higher".
- "Results" readouts, live: Riverbend seats, Hillside seats, average grades of the 40, returning campers among the 40, students admitted who live over 2 miles away (and whether there is a bus), added cost.
- "Pin to my report" (pin icon): pins the current view (Rule check row, twin pair, or Results) as an evidence card for the Hearing. Up to 6 pins; each pin can be removed.
- "Reset formula" (circular arrow).

### Mode 2: Hearing
Stage: the board room drawn in code: a long table with three name plates and one public comment podium. Your formula's Results card on an easel. Board members speak in turn (speech bubbles, portraits from Art):
1. Dr. Rivera, board chair: "The formula never mentions neighborhoods. How can it be unfair?"
2. Mr. Bell, budget officer: "What does your change cost, and where does the money come from?"
3. Ms. Ortiz, camp teacher: "Will my campers still be ready for hard robotics work?"
For each question the panel shows your pinned evidence cards; tap one to present it. The member answers it (below): a relevant card gets a "That answers my question" response and the card is stamped "Presented"; an unrelated card gets "That doesn't answer what I asked" and you can present another. Then "Call the vote": each member votes yes or no by their rule (below), with their reason. Then public comment from Mrs. Park, a Hillside parent, whose words depend on how many Hillside seats changed. Result: "Passes 3 to 0", "Passes 2 to 1" or "Fails". No points; "Back to Audit" keeps everything for another try.

## Content
District, camp, people and applicants are made up. 120 applicants, 40 seats.
Rules and the district's reasons (start points; change options):
1. Grades (1.5 to 4.0) times 10: "Camp work is hard; strong students keep up." Options: times 10, times 5.
2. Teacher recommendation, 15: "Teachers know who's excited." Options: 15, 5, 0.
3. Applied online in the first week, 15: "Early sign-ups show they really want it." Options: 15, 5, 0 ("Any time before the deadline counts the same").
4. Came to last year's camp, 10: "Returning campers help new ones." Options: 10, 5, 0.
5. Lives within 2 miles of school, 10: "Camp has no bus, so nearby students can get there." Options: 10, 0 ("Remove, no bus"), "Remove and add a camp bus from Riverbend" (adds $2,500).
6. Attendance 95 percent or more, 10: "Students who come every day keep their team going." Options: 10, 0.
Score = sum, rounded to one decimal (`Math.round(x * 10) / 10`). Top 40 get seats; ties to the lower number. Budget for changes (Mr. Bell's limit): $3,000. Bus: $2,500. All amounts are the tool's own.

Applicants (exact, so every number reproduces): mulberry32 (`a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296`), seed 707. For i = 0 to 119: number i + 1; Hillside when i is even, Riverbend when odd; then, drawing in this order: grades = Math.round((1.5 + 2.5 R()) * 10) / 10; recommendation R() < 0.40; attendance R() < 0.60; first week R() < (Hillside 0.80, Riverbend 0.40); within 2 miles R() < (Hillside 0.70, Riverbend 0.20); last year's camp R() < (Hillside 0.30, Riverbend 0.08).
Checked: Hillside applicants average grades 2.66, Riverbend 2.77. Rule check counts (Hillside, Riverbend, of 60 each): recommendation 23, 25; attendance 38, 40; first week 51, 21; within 2 miles 47, 11; last year's camp 17, 5.
Why Riverbend differs (the on-screen "Background" card in Rule check): "Riverbend is across the river, more than 2 miles from school. Fewer Riverbend homes have home internet, so families often apply later, at the library. Last year's camp used the same formula." Home internet fact source below.
Results (Riverbend seats of 40; average grades of the 40; returning campers; lowest score admitted):
| Formula | Riverbend | Avg grades | Returning | Cutoff |
|---|---|---|---|---|
| Start | 8 | 3.01 | 12 | 63 |
| First week 0 | 13 | 3.04 | 9 | 53 |
| First week 5, last year 5 | 12 | 3.05 | 7 | 54 |
| Within 2 miles 0 (or bus) | 12 | 3.07 | 11 | 57 |
| Last year 0 | 10 | 3.09 | 7 | 60 |
| First week 0, last year 0 | 16 | 3.05 | 4 | 51 |
| First week 0, within 2 miles 0 (or bus) | 20 | 3.19 | 8 | 47 |
| First week 0, within 2 miles 0, last year 0 | 19 | 3.19 | 4 | 45 |
| Grades times 5 | 9 | 2.92 | 12 | 48.5 |
| Recommendation 0 | 7 | 3.12 | 12 | 56 |
| Lottery (grades 2.5 or higher, 71 in the pool) | 21 | 3.20 | 7 | - |
Lottery order: Fisher-Yates over the pool in number order with mulberry32 seed 708 (for i from the last index down to 1, j = floor(R() * (i + 1)), swap); the first 40 get seats; first ten: 58, 59, 28, 27, 24, 60, 3, 21, 55, 36.
Students admitted living over 2 miles away: Start 10; First week 0 and last year 0: 11; First week 0 and within 2 miles 0: 19; Lottery 23.
Close call: applicant 108, Riverbend, grades 3.8, recommendation yes, attendance yes, applied in week two, lives over 2 miles away, no camp last year: score 63, rank 42 (63 is the cutoff; applicants 5, 9 and 83, Hillside, and 86, Riverbend, also have 63). Twin "applied in the first week": 78, rank 10. Twin "lives within 2 miles": 73, seat.
Votes: Dr. Rivera yes when Riverbend has at least 16 seats ("within 4 seats of an even split, since each neighborhood sent 60"); Mr. Bell yes when added cost is $3,000 or less; Ms. Ortiz yes when the 40 average grades of 3.0 or higher. All three thresholds are the tool's own. A change passes with 2 or more yes votes. The board only votes on a change: "Call the vote" is disabled, with "The board is here to vote on a change", while the formula equals Start.
Evidence relevance: Rivera accepts a Rule check pin (first week, within 2 miles or last year's camp) or a Twin test pin; Bell accepts a Results pin (shows cost); Ortiz accepts a Results pin (shows average grades) or a Rule check pin for grades.
Board answers: Rivera, relevant: "So a rule about sign-up timing works like a rule about neighborhood. I see." Bell, relevant: "[Cost] it is. [Within budget / Over budget]." Ortiz, relevant: "Average grades of [x]. [I can work with that / That worries me]." Any member, not relevant: "That doesn't answer what I asked."
Mrs. Park (public comment): Hillside seats down 8 or more: "My son applied on the first day. Now he might not get in. I understand why, but I want the board to know it costs us something." Down 1 to 7: "Fewer Hillside seats, but I can see it's fairer." Unchanged or up: "This works for our family."
Ride note (Ortiz adds it when no bus and over 10 admitted live far away): "Some of these students will need a ride. Who's driving them?"

## Interactions in detail
- Every formula change recomputes all 120 scores, the seat map and the Results in under 50 ms; seats re-fill with a 300 ms shuffle (instant with Motion off). The seat map always shows the neighborhood by shape and color.
- The Lottery switch greys out rules 1 to 4 and 6 (rule 5's bus option stays, since rides still matter); turning it off restores the last formula.
- Twin test works with any formula; ranks use the current formula. The twin is never added to the 120.
- Pins store a snapshot (the numbers at the time), labeled with the formula they came from; a pin from an older formula shows "From an earlier formula".
- Hearing with no pins: each question shows "You have no evidence pinned. Go back to Audit and pin what you found." The vote still happens after all three questions are answered or skipped ("Skip" per question; a skipped question gets "We'll vote without it.").
- Votes use the current formula's numbers, not the pins.
- Nothing is saved. "Reset formula" restores Start and keeps pins.
- Keyboard: panel before stage; seat grid is one focusable image with a text summary; applicant table rows focusable. Visible focus.
- Sizes: the seat map, the formula section and the Results readouts visible without scrolling at 1280x720, 1366x768 and 680x425 (the formula rows compact to 40 px; audit views become a tab below the seat map); at 760 wide and below the panel stacks under the stage with the formula first.

## Look
- Accent `--brand #1e3a8a` (civic navy; header strip, formula code keywords, pressed pickers). `--head-ink #ffffff`.
- Own `:root` (manila file): `--paper #f6efdc`, `--panel #fffaf0`, `--ink #1e2421`, `--muted #59615c`, `--line #e2d6b8`, `--btn #1e3a8a`, `--focus #b4235a`. Formula lines on #fffaf0 in the readout font. Hillside badge: white circle glyph on #15803d; Riverbend badge: white triangle glyph on #c2410c. Votes: "Yes" with a check, "No" with a cross, in ink.
- Neighbors: model-mechanic lime, packet-race red, phishing-spotter lime, flowchart-factory cyan, code-kitchen rust, ai-evaluator pink. Navy on manila is apart from them and from its group siblings (chalk yellow, hot spring orange, fuchsia, deep sky).
- Contrast: white on brand 10.36:1; brand on paper 9.03:1; ink on paper 13.76:1; muted on paper 5.56:1; muted on panel 6.14:1; focus on paper 5.50:1; white on Hillside green 5.02:1; white on Riverbend orange 5.18:1. All pass AA.

## Art
- `board-rivera`: "portrait of a calm woman in her fifties with short gray hair and a navy blazer, seated at a meeting table, flat illustration, plain warm background, chest up"; 1:1; cutout yes; people: true; Codex (`scripts/gptart.py`), Cory reviews.
- `board-bell`: "portrait of a friendly man in his forties with glasses and a cardigan holding a calculator, flat illustration, plain warm background, chest up"; 1:1; cutout yes; people: true; Codex, Cory reviews.
- `board-ortiz`: "portrait of an energetic teacher in her thirties in a robotics club t-shirt with a small robot kit on the table, flat illustration, plain warm background, chest up"; 1:1; cutout yes; people: true; Codex, Cory reviews.
- `parent-park`: "portrait of a parent in their forties in a rain jacket standing at a podium, flat illustration, plain warm background, chest up"; 1:1; cutout yes; people: true; Codex, Cory reviews.
Everything else (seat map, badges, tables, board room, preview.svg: the seat map with 32 green circles and 8 orange triangles beside a formula card) is drawn in code. Applicants are never pictured; they are numbers and badges.

## Voice
Bank voice `calm-professor` (Schedar), "Say evenly and clearly, like a calm, friendly college professor": the outside auditor the board hired, coaching you. Not used by a 6-8 CS neighbor (model-mechanic science-narrator, packet-race firm-captain, phishing-spotter lively-host, flowchart-factory friendly-dad, code-kitchen easy-coach) or a group sibling; ai-evaluator, its closest topic, uses wise-mentor. Board members' and Mrs. Park's words are read on screen.
1. how, welcome Audit: "The district's formula gave Riverbend 8 seats out of 40. Nothing in it says Riverbend. Your job is to find out why."
2. how, first Rule check view: "Compare the two neighborhoods on each rule. Look for a rule one side earns much more often."
3. how, first Twin test view: "Flip one switch on the twin. If one answer moves a student in or out, that rule matters."
4. event, a twin flip moves the twin across the cutoff: "One answer changed, and the seat changed with it." Stale on the next flip.
5. how, first formula change: "Watch the seat map. Every fix moves some students in and others out."
6. how, first pin: "Pinned. You'll use it as evidence at the hearing."
7. how, welcome Hearing: "The board will ask three questions. Answer each one with evidence you pinned."
8. event, the vote: "The board votes. [Passes three to zero / Passes two to one / Fails]." (three fixed lines)
9. event, Mrs. Park speaks: "Before the vote counts, a parent asked to speak." Stale when the hearing resets.

## Family engine
none.

## Sources
- Paired (twin) testing to find discrimination in automated systems: Sandvig, Hamilton, Karahalios and Langbort, "Auditing Algorithms: Research Methods for Detecting Discrimination on Internet Platforms", ICA preconference paper, 2014: http://www-personal.umich.edu/~csandvig/research/Auditing%20Algorithms%20--%20Sandvig%20--%20ICA%202014%20Data%20and%20Discrimination%20Preconference.pdf
- A rule that looks neutral can stand in for a group (a proxy) and have an unfair effect on it (disparate impact): Barocas and Selbst, "Big Data's Disparate Impact", California Law Review 104 (2016), 671-732: https://papers.ssrn.com/abstract=2477899
- Lower-income households are less likely to have home broadband (on-screen background line): Pew Research Center, "Digital divide persists even as Americans with lower incomes make gains in tech adoption", June 22, 2021: https://www.pewresearch.org/short-reads/2021/06/22/digital-divide-persists-even-as-americans-with-lower-incomes-make-gains-in-tech-adoption/
- CSTA K-12 Computer Science Standards (2017), 2-IC-20, 2-IC-21, 2-AP-17: https://csteachers.org/k12standards/
- Cedar Valley, its camp, the board, the parent and all 120 applicants are made up; every result above was computed from the stated generator and rules.

## Done when
1. Audit opens with Riverbend 8 and Hillside 32 seats, average grades 3.01, cutoff 63.
2. Rule check shows first week 51 and 21, within 2 miles 47 and 11, last year's camp 17 and 5, recommendation 23 and 25.
3. "Show me a close call" opens applicant 108 at rank 42; flipping "applied in the first week" on the twin shows 78 and rank 10, and line 4 plays.
4. Setting First week to 0 and Last year to 0 gives Riverbend 16, average 3.05, cost $0; the Hearing vote passes 3 to 0.
5. Removing the distance rule with the bus and First week 0 gives Riverbend 20 and cost $2,500, and passes 3 to 0; Grades times 5 alone gets no from Rivera (9 seats) and Ortiz (2.92) and fails 1 to 2.
6. Lottery gives Riverbend 21, average 3.20, 23 admitted living far away, and Ms. Ortiz's ride note when there is no bus.
7. Presenting a Results pin to Dr. Rivera gets "That doesn't answer what I asked"; a Twin test pin gets her relevant answer.
8. Lines 2, 3, 5 and 6 are each spoken once in a run of five actions; line 4 on every crossing flip.
9. Seat map, formula and Results visible without scrolling at 1366x768 and 680x425; neighborhoods told apart in grayscale by circle and triangle.

## Open questions
- The unfairness is framed by neighborhood (across the river, less home internet), never by race or family income by name, to keep a 6-8 class discussion calm. Keep it that gentle, or name income directly in the background card?
- Four board and parent portraits (people: true) for Cory to review. Drop them for name plates only, if fewer people images are preferred.

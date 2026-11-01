# 1. Linear Search Trace
minutes: 35
materials: pencil
ican: I can trace a linear search and count its comparisons in the best and worst cases.
directions: Use the linear search below. Indexes start at 0. For each list, write every value the search compares with the target, in order, then the number of comparisons and what the search returns.
mistakes: Students often start counting indexes at 1, so every return value is off by one. Others keep going after a match: the search returns at the first match (list 4). When the target is missing, students sometimes stop early; the search must check every item before it can return -1.
notes: Linear search checks items one at a time from the front. Best case: 1 comparison (the target is first). Worst case: n comparisons (the target is last or not there at all). If the target is in the list and every position is equally likely, the average is (n + 1) / 2 comparisons, so 50.5 for n = 100. Stretch answer: sorting lets an unsuccessful search stop once it passes a value bigger than the target, but sorting costs more than one linear search, so it only pays off when you will search the same list many times (and then binary search is the better tool).

## The algorithm
table: linear_search(list, target)
  - FOR i FROM 0 TO length(list) - 1
  - IF list[i] = target THEN RETURN i
  - END FOR
  - RETURN -1

## Warm up: Trace list 1 step by step
text: List 1: [12, 7, 31, 4, 19, 25]. Target: 4.
table: Comparison | i | list[i] | Equal to 4?
  - 1 | {0} | {12} | {no }
  - 2 | {1} | {7 } | {no }
  - 3 | {2} | {31} | {no }
  - 4 | {3} | {4 } | {yes}
fill:
  - List 1: {4} comparisons. The search returns {3}.

## Main: Three more lists
fill:
  - List 2: [5, 18, 2, 40, 11, 9, 27]. Target 27. Values compared: {5, 18, 2, 40, 11, 9, 27}
  - List 2: {7} comparisons. Returns {6}.
  - List 3: ["cat", "dog", "emu", "fox", "owl"]. Target "ant". Values compared: {cat, dog, emu, fox, owl}
  - List 3: {5} comparisons. Returns {-1}.
  - List 4: [8, 3, 8, 6, 1]. Target 8. Values compared: {8}
  - List 4: {1} comparison. Returns {0}.
table: List length n | Best case comparisons | Worst case comparisons
  - 6 | {1} | {6}
  - 100 | {1} | {100}
  - 1,000,000 | {1} | {1,000,000}
fill:
  - For a list of n items, the worst case takes {n} comparisons.
  - If the target is in a list of 100 and every spot is equally likely, the average is {50.5} comparisons.
write: List 4 holds 8 twice. Why does the search return 0 and not 2?
  lines: 2
  key: It returns as soon as it finds a match. list[0] is already 8, so it returns 0 and never looks at index 2.

## Stretch
write: Would sorting the list first make linear search faster? Explain when it would and would not help.
  lines: 4
  key: For a missing target, a sorted list lets the search stop as soon as it passes a value bigger than the target, so it can save comparisons. For a target that is present, sorting does not change the worst case. Sorting itself costs more work than one linear search, so it only pays off if you search the same list many times, and then binary search on the sorted list is much faster.

# 23. Ethics Decision Frame
minutes: 45
materials: pencil, highlighter
ican: I can use a decision frame to reason through an ethical problem about data.
directions: Read the case. Work through the four steps: facts, stakeholders, options, choice. Fill each step before moving to the next, then write and defend your decision.
mistakes: Students jump to the choice in step 1 and use the rest of the frame to justify it. Hold them to facts first, including what they do not know yet. Others list only the school and the company as stakeholders and forget the students and families whose data it is. "De-identified" does not mean risk-free: watch for students who treat it as the end of the discussion.
notes: The case is made up for Curio Class. Useful background: in the United States, FERPA protects student education records, and schools may share them with contractors only for school purposes under the school's control; many states also have student privacy laws that limit vendors' use of student data, for example for advertising. Data that has had names removed can sometimes be re-identified by combining it with other data, especially for small groups. There is no single right choice; a strong answer weighs every stakeholder and names a condition that would change the decision.

## Read the case
passage: The Free Upgrade
  Lakeview School District uses a reading app in grades 3 to 8. The app records each student's reading level, the books they open, how long they read, and their quiz scores. Teachers use these reports every week.
  This spring, the company that makes the app sent the district an offer. If the district agrees to new terms, every school gets the premium version free next year, which would save the district about $40,000. In return, the company may use student data, with names removed, to "improve our products and develop new ones," and may share it with "trusted partners."
  The superintendent must answer in two weeks. The technology director says the premium version has tools teachers have asked for. A parent group has heard about the offer and wants to know who the partners are. The contract does not name them, and it does not say how long the data will be kept. Families were never asked about the change. Some teachers point out that in a few small classes, a student's reading level, grade and school could be enough to guess who they are, even with names removed.

## Step 1: Facts
chart: What we know | What we do not know yet
  rows: 3
  key: Know: the app collects reading level, books opened, reading time and quiz scores; the offer saves about $40,000; the data would be de-identified; it may be shared with unnamed partners; families were not asked; the answer is due in two weeks. Do not know: who the partners are, what they will do with the data, how long it will be kept, whether it can be re-identified, and whether state law allows it.

## Step 2: Stakeholders
chart: Stakeholder | What they care about | How they could be helped or harmed
  rows: 5
  key: Students (privacy, a good reading tool; could be profiled or identified); families (a say over their children's data; trust); teachers (better tools; trust of families); the district and taxpayers (saving $40,000; legal risk and loss of trust if data is misused); the company and its partners (data to build products; reputation).

## Step 3: Options
chart: Option | Benefit | Risk
  rows: 3
  key: Accept as written (saves money, new tools; data shared with unknown partners for unknown uses). Reject (protects data; lose the free upgrade and the teacher tools). Negotiate: accept only if the contract names partners, bans selling and advertising use, sets a deletion date, and lets families opt out (balances both; the company may say no or the deadline may pass).

## Step 4: Choice
write: What should the superintendent decide? Defend your choice using at least two stakeholders and one fact from the case.
  lines: 6
  starter: The superintendent should ... because ...
  key: Model: The superintendent should not sign the terms as written but should negotiate. The contract lets the company share student data with partners it does not name and keep it for no set time, and teachers warn that small classes could make students identifiable. Students and families carry the risk but were never asked, while the $40,000 benefit goes to the district. If the company names its partners, bans advertising use, deletes the data on a set date and lets families opt out, the district can accept; if not, it should say no.

## Stretch
write: What new fact would change your decision? Explain why.
  lines: 2
  key: Answers vary. For example: if the contract were limited to improving this app only, with no partners and deletion after one year, many students would accept; if the partners turned out to be advertisers, many who said yes would change to no.

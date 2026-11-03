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

# 6. Parameters and Returns Trace
minutes: 35
materials: pencil
ican: I can trace a procedure call by matching each argument to its parameter and following the value it returns.
directions: The programs are in Python. For each call, write the value each parameter gets, then the value the call returns. Arguments go into parameters in order, left to right. When a procedure reaches return, it stops right there and hands back that value.
mistakes: The most common slip is swapping arguments: price_after(5, 20) puts 5 into cost and 20 into discount, so it returns -15, not 15. In Program 4, students often skip the inner calls; square(3) and square(4) must finish before add can start. In Program 5, students keep looping after the return; return ends the whole procedure, so first_even never looks at the 4. Some write "nothing" for a list with no even numbers; the loop ends and the last line returns -1.
notes: Answers: Program 1: 14, then 28. Program 2: 15, then -15. Program 3: 9, 12, 6 (when a equals b, a > b is false, so it returns b, which is the same value). Program 4: square(3) = 9, square(4) = 16, add(9, 16) = 25; add(3, 4) = 7, square(7) = 49. Program 5: 10 and -1. Stretch: the program prints 10 12, because price inside add_fee is a new local variable: changing it does not change p outside. If your class uses another language, rewrite the programs in its syntax; the traces stay the same.

## Warm up: Program 1
program:
  | def double(n):
  |     return n * 2
  | x = double(7)
  | y = double(x)
table: Call | n gets | Returns
  - double(7) | {7} | {14}
  - double(x) | {14} | {28}

## Main: Programs 2 to 5
program: Program 2
  | def price_after(cost, discount):
  |     return cost - discount
  | p = price_after(20, 5)
  | q = price_after(5, 20)
table: Call | cost gets | discount gets | Returns
  - price_after(20, 5) | {20} | {5} | {15}
  - price_after(5, 20) | {5} | {20} | {-15}
program: Program 3
  | def bigger(a, b):
  |     if a > b:
  |         return a
  |     return b
  | r1 = bigger(4, 9)
  | r2 = bigger(12, 3)
  | r3 = bigger(6, 6)
table: Call | a gets | b gets | Which return runs? | Returns
  - bigger(4, 9) | {4} | {9} | {return b} | {9}
  - bigger(12, 3) | {12} | {3} | {return a} | {12}
  - bigger(6, 6) | {6} | {6} | {return b} | {6}
program: Program 4
  | def square(n):
  |     return n * n
  | def add(a, b):
  |     return a + b
  | r = add(square(3), square(4))
  | s = square(add(3, 4))
table: Call, in the order it runs | Parameters get | Returns
  - square(3) | {n = 3} | {9}
  - square(4) | {n = 4} | {16}
  - {add(9, 16)} | {a = 9, b = 16} | {25}
  - add(3, 4) | {a = 3, b = 4} | {7}
  - {square(7)} | {n = 7} | {49}
program: Program 5 (% gives the remainder, so n % 2 == 0 means n is even.)
  | def first_even(nums):
  |     for n in nums:
  |         if n % 2 == 0:
  |             return n
  |     return -1
  | a = first_even([3, 7, 10, 4])
  | b = first_even([1, 5, 9])
fill:
  - first_even([3, 7, 10, 4]) checks 3, 7, then {10} and returns {10}.
  - first_even([1, 5, 9]) checks every number, finds no even one, and returns {-1}.
## Stretch: Inside and outside
write: Suppose add_fee(price) sets price = price + 2 and returns price. After p = 10 and q = add_fee(p), what are p and q? Explain why p does not change.
  lines: 3
  key: p is 10 and q is 12. The parameter price is a new local variable that starts with a copy of p's value; changing price does not change p, and only the returned value goes into q.

# 17. AI, Simulation and Networks Check
minutes: 35
materials: pencil
ican: I can choose an AI approach for a problem, read a simulation graph, and label the parts of a network.
directions: Three short parts. In Part 1, name the best AI approach for each problem and give a reason. In Part 2, read the graph from a computer simulation. In Part 3, label the network diagram with the words in the box.
mistakes: Students call anything "smart" machine learning. A fixed school rule with no data to learn from (problem 3) is best as hand-written rules, and finding a best route on a known map (problem 2) is a search. On the graph, students read the percent after 100 rolls as the final answer; the point of the simulation is that the result settles toward the expected value as the number of rolls grows. In Part 3, students mix up the modem and the router: the router makes the home network (and the Wi-Fi), the modem connects the home to the internet provider's line.
notes: Part 1: 1 machine learning (patterns learned from 50,000 labeled examples; nobody could write rules for every trick), 2 search (try routes through a known map and keep the fastest), 3 hand-written rules (the rule is already known and must be exact). Part 2: the chance of a sum of 7 with two dice is 6 / 36 = 1 / 6, about 16.7%; the made-up run starts at 22% after 100 rolls and settles near 16.7%, which is the law of large numbers. Part 3: 1 wireless router, 2 modem, 3 the internet (many routers run by internet providers), 4 DNS server, 5 web server. Many homes have one box that does both the router's and the modem's jobs; the diagram shows them apart so students can name each job.

## Part 1: Rules, search or learning?
table: Problem | Best approach | Reason
  height: 0.75
  - 1. Flag spam email, learning from 50,000 emails that people already marked spam or not spam. | {machine learning} | {there are many labeled examples, and spam changes too much to write every rule by hand}
  - 2. Find the fastest way across the city on a subway map with travel times between stations. | {search} | {the map is known, so the program can try routes and keep the fastest one}
  - 3. Mark a student tardy if they sign in after 8:05 a.m. | {hand-written rules} | {the rule is known and exact; there is nothing to learn or search}

## Part 2: Read a simulation graph
text: A computer simulated rolling two dice 1,000 times. After every 100 rolls, it plotted the percent of rolls so far whose sum was 7.
graph: Number of rolls | 0 1000 100 | Percent of sums equal to 7 | 0 30 5
  line: 100,22 200,19 300,18 400,17.5 500,16 600,16.5 700,17 800,16.5 900,16.8 1000,16.6
  minor: off
fill:
  - After 100 rolls, about {22} percent of the sums were 7.
  - With two dice there are 36 equally likely outcomes, and {6} of them sum to 7, so the expected percent is about {16.7} percent.
choice: What happens to the line as the number of rolls grows?
  - It keeps rising.
  - It jumps around more and more.
  * It settles closer to the expected percent.
  - It drops to zero.
write: A classmate ran only 100 rolls and concluded that 7 comes up 22% of the time. What would you tell them?
  lines: 2
  key: One short run can be far from the true chance by luck. Run many more trials; the simulation shows the percent settling near 16.7% (1 in 6) after 1,000 rolls.

## Part 3: Label the network
text: **Word bank:** modem, wireless router, DNS server, web server, the internet
program: A phone loads a school web page.
  | [ Phone ] ))) Wi-Fi ))) [ 1 ] ---- [ 2 ] ---- ( 3 ) ---- [ 5 ]
  |                                                 |
  |                                               [ 4 ]
fill:
  - Box 1 gives the phone Wi-Fi and passes its packets toward the internet: {wireless router}
  - Box 2 connects the home to the internet provider's line: {modem}
  - Cloud 3 is a huge web of networks and routers: {the internet}
  - Box 4 answers the question "What is the IP address of this website's name?": {DNS server}
  - Box 5 stores the school web page and sends it back: {web server}
choice: Before the phone can ask Box 5 for the page, which box must answer one of its questions?
  - Box 5
  - Box 2
  - Box 1
  * Box 4, which looks up the IP address

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

# 28. The People Behind the Network
minutes: 40
materials: pencil, highlighter
ican: I can describe the work and the risks of the people who built early telephone networks.
directions: Read the passage. Highlight details about the work and its dangers. Then answer the questions, citing paragraph numbers.
mistakes: Students often treat the network as something that "spread" on its own; push them to name who did the work in each paragraph. On question 3, students sometimes say telephone wires themselves were deadly; the passage says the danger came when a phone wire touched an electric power line. Watch for students who see the union only as about pay: the passage also names safety and help for families.
notes: The passage is original to Curio Class. Facts to know: Bell's telephone patent is from 1876. Linemen climbed wooden poles with steel spikes strapped to their boots and a safety belt. In the 1880s and 1890s, electric light and streetcar lines went up on the same city streets, and contact between a phone or telegraph wire and a power line could electrocute a worker. Electrical workers and linemen founded a union in St. Louis in 1891, today the International Brotherhood of Electrical Workers (IBEW); the union's published history states that the death rate for linemen at the time was about twice the national average for other industries (check the IBEW history page before quoting a number to students). Emma Nutt became the first woman telephone operator in Boston in 1878; within a few years most operators were women. Telephone operators in New England went on strike in April 1919 and won higher pay. Today, line workers who install and repair cables still work at heights and near power lines, and storm repair is among the riskiest parts of the job.

## Read
passage: Climbing the Poles | numbered
  When Alexander Graham Bell patented the telephone in 1876, a phone was useless without wires. Over the next few decades, crews strung wire along city streets, railroads and country roads so that one telephone could reach another. The network that made this possible was not built by inventors. It was built by thousands of workers whose names rarely appear in history books.
  The work started on the ground. Crews cut and hauled heavy wooden poles, dug deep holes with shovels and iron bars, and raised each pole with ropes and long poles called pike poles. Then a lineman climbed. He strapped steel spikes to his boots, wrapped a leather safety belt around the pole, and worked high above the street, stringing and joining wires in wind, rain, summer heat and ice.
  The dangers were real. A spike could slip out of the wood and send a worker sliding down the pole. A rotten pole could snap. Heavy wire could whip loose. But the worst danger came from a new kind of line. In the 1880s and 1890s, cities were adding wires for electric lights and streetcars, often on the same streets and sometimes on the same poles. A telephone wire carried only a small current, but if it touched a power line, it could carry a deadly shock to the lineman holding it. Rubber gloves and safety rules for working near power lines came slowly.
  Workers organized. In 1891, a group of linemen and electrical workers met in St. Louis and formed a union, known today as the International Brotherhood of Electrical Workers. Its own history reports that linemen at the time died on the job at about twice the rate of workers in other industries. The union pushed for training, safer rules, fair pay, and help for the families of workers who were killed.
  Not all of the network's workers were on poles. Inside each telephone exchange, switchboard operators connected every call by hand, plugging cords into the right holes. Beginning with Emma Nutt in Boston in 1878, most operators were young women. They worked long shifts under strict rules about how to speak and how fast to answer. In 1919, thousands of operators across New England went on strike and won higher pay.
  The network still depends on workers. Today's crews bury fiber optic cable, climb poles and towers, and repair lines after storms, often while the power is still dangerous. Every message you send travels over work that someone did with their hands.

## Questions
choice: According to paragraph 3, what made power lines the biggest danger for telephone linemen?
  - Telephone wires carried more electricity than power lines.
  * A telephone wire that touched a power line could carry a deadly shock.
  - Power lines made the poles rot faster.
  - Power companies did not allow linemen to climb.
write: Name two jobs that had to be done before a single telephone call could go through. Which paragraph tells you?
  lines: 2
  key: Any two: cutting and hauling poles, digging holes, raising poles, climbing and stringing wire (paragraph 2), or connecting the call at the switchboard (paragraph 5).
write: Why did linemen form a union in 1891, and what did it push for? Use evidence from paragraph 4.
  lines: 3
  key: The work was very dangerous: linemen died on the job at about twice the rate of workers in other industries. The union pushed for training, safer rules, fair pay and help for the families of workers who were killed (paragraph 4).
write: Compare the work of linemen and switchboard operators. How were their jobs and risks different? How were they alike?
  lines: 4
  key: Linemen worked outdoors at heights, in all weather, with the risks of falls, broken poles and electric shock (paragraphs 2 and 3). Operators worked indoors, connecting every call by hand, with long shifts, strict rules and low pay (paragraph 5). Both did hard, necessary work that made the network run, and both groups organized to improve their pay and conditions (paragraphs 4 and 5).
write: Paragraph 6 says the network "still depends on workers." Who builds and repairs the internet today, and what risks do they face?
  lines: 3
  key: Crews who bury fiber optic cable, climb poles and towers, and repair lines after storms. They still work at heights and near power lines, and storm repair can be dangerous because downed lines may still carry power.

# 39. Spot the Invalid Rows
minutes: 35
materials: pencil, highlighter
ican: I can use a data dictionary to find rows that break its rules and name the rule each one breaks.
directions: Read the data dictionary for the Club Sign-Up dataset. Check every row of the dataset against every rule. Exactly 8 rows break a rule (each breaks just one). Record each invalid row, the field, and the rule it breaks.
mistakes: Students check only the columns that look odd and miss quiet errors: row 6 looks fine until you compare its student_id with row 1. Others flag row 12's 20.00 as too high; the range includes 20.00. Row 10's date has the right shape, YYYY-MM-DD, but month 13 does not exist. Remind students that a blank in a required field is its own rule.
notes: The dataset is made up for Curio Class. Invalid rows: 3 student_id has 5 digits (rule: exactly 6 digits); 4 grade 13 (rule: 9 to 12); 6 student_id 104233 repeats row 1 (rule: unique); 7 email has no @ (rule: format); 8 club Soccer (rule: one of the four clubs); 10 join_date 2026-13-01 has no month 13 (rule: a real date); 11 dues 25.00 (rule: 0.00 to 20.00); 13 email blank (rule: required). Every other row passes every rule. Stretch: a fix you can make yourself is one where the right value is certain from other data; most of these need the student or the club adviser, because guessing would put a made-up value into the data.

## The data dictionary
table: Field | Type | Rule
  - student_id | text | Required. Exactly 6 digits. Unique: no two rows share one.
  - grade | whole number | Required. 9, 10, 11 or 12.
  - email | text | Required. Has exactly one @ and ends with @school.example
  - club | text | Required. One of: Robotics, Chess, Art, Drama.
  - join_date | date | Required. A real date written YYYY-MM-DD, from 2026-08-20 to 2026-10-30.
  - dues | money | Required. From 0.00 to 20.00, with two decimal places.

## Warm up: Use the rules
fill:
  - Is grade 9.5 allowed? {no}, because grade must be {9, 10, 11 or 12}
  - Is a join_date of 2026-08-19 allowed? {no}, because it is {before 2026-08-20}
  - Is dues of 20.00 allowed? {yes}, because the range includes {20.00}

## The dataset
table: Row | student_id | grade | email | club | join_date | dues
  - 1 | 104233 | 9 | mlee@school.example | Chess | 2026-09-02 | 10.00
  - 2 | 104871 | 11 | ajones@school.example | Robotics | 2026-08-28 | 20.00
  - 3 | 10592 | 10 | kpatel@school.example | Art | 2026-09-10 | 5.00
  - 4 | 105330 | 13 | tnguyen@school.example | Drama | 2026-09-11 | 0.00
  - 5 | 105412 | 12 | rsilva@school.example | Chess | 2026-09-15 | 15.00
  - 6 | 104233 | 10 | bcho@school.example | Art | 2026-09-16 | 10.00
  - 7 | 106001 | 9 | dkim.school.example | Robotics | 2026-09-18 | 10.00
  - 8 | 106045 | 10 | jbrown@school.example | Soccer | 2026-09-20 | 5.00
  - 9 | 106112 | 11 | lgarcia@school.example | Drama | 2026-09-22 | 12.50
  - 10 | 106187 | 9 | owu@school.example | Art | 2026-13-01 | 5.00
  - 11 | 106230 | 12 | pmorris@school.example | Chess | 2026-10-01 | 25.00
  - 12 | 106301 | 10 | sahmed@school.example | Robotics | 2026-10-03 | 20.00
  - 13 | 106355 | 11 |  | Art | 2026-10-06 | 10.00
  - 14 | 106402 | 9 | vrossi@school.example | Drama | 2026-10-07 | 0.00
  - 15 | 106470 | 12 | ecole@school.example | Chess | 2026-10-12 | 7.50
  - 16 | 106533 | 11 | hali@school.example | Robotics | 2026-10-15 | 10.00

## Main: The 8 invalid rows
table: Row | Field | Rule it breaks
  - {3} | {student_id} | {exactly 6 digits (it has 5)}
  - {4} | {grade} | {must be 9 to 12 (it is 13)}
  - {6} | {student_id} | {unique (same as row 1)}
  - {7} | {email} | {must have one @ (it has none)}
  - {8} | {club} | {must be Robotics, Chess, Art or Drama}
  - {10} | {join_date} | {must be a real date (no month 13)}
  - {11} | {dues} | {must be 0.00 to 20.00}
  - {13} | {email} | {required (it is blank)}

## Stretch
write: Pick two invalid rows. For each, say whether you could safely fix it yourself or would need to ask someone, and why.
  lines: 3
  key: Answers vary. Example: Row 8 (Soccer) needs the student or the adviser, because we cannot guess which of the four clubs they meant. Row 7 is almost surely dkim@school.example, but we should still confirm it with the student before changing it, because a wrong email means messages go to someone else.

# 1. Nested Loops on Grid Paper
minutes: 35
materials: pencil, a dark pencil or crayon for shading
ican: I can trace a nested loop and predict what it draws.
directions: Each program shades squares on a grid with 4 rows and 6 columns. Trace each program one step at a time: for every value of row, the inner loop runs all the way through. Shade every square the program shades, then answer the questions.
mistakes: The classic slip is running the outer loop all the way first, then the inner loop, which shades only one row or one column. Have students write the pairs in order as they trace: (1,1), (1,2), (1,3) ... In Program B the inner loop's end depends on row, so it changes each time; students who use a fixed 4 shade a rectangle. STEP 2 means 1, 3, 5, not 2, 4, 6.
notes: Squares are named (row, col), with row 1 at the top and col 1 at the left. Program D makes a checkerboard: a square is shaded when row and col are both odd or both even. When the inner loop always runs the same number of times, SHADE runs (outer count) x (inner count) times: 3 x 4 = 12 for A, 2 x 3 = 6 for C. In B the inner count grows, so it is 1 + 2 + 3 + 4 = 10. Border program for the stretch: shade when row = 1 or row = 4 or col = 1 or col = 6 (16 squares).

## Warm up: One loop
example: FOR col FROM 1 TO 5: SHADE square (1, col). This shades row 1, columns 1, 2, 3, 4 and 5: five squares in a line.
fill:
  - FOR row FROM 2 TO 4: SHADE square (row, 6) shades {3} squares, all in column {6}.

## Main: Trace and shade
text: **Program A.** Outer loop: FOR row FROM 1 TO 3. Inner loop: FOR col FROM 1 TO 4. Inside both loops: SHADE square (row, col).
table: Grid A | col 1 | col 2 | col 3 | col 4 | col 5 | col 6
  - row 1 | {■} | {■} | {■} | {■} | {} | {}
  - row 2 | {■} | {■} | {■} | {■} | {} | {}
  - row 3 | {■} | {■} | {■} | {■} | {} | {}
  - row 4 | {} | {} | {} | {} | {} | {}
fill:
  - The inner loop runs {4} times each time the outer loop runs once.
  - SHADE runs {12} times in all.
text: **Program B.** Outer loop: FOR row FROM 1 TO 4. Inner loop: FOR col FROM 1 TO row. Inside both loops: SHADE square (row, col).
table: Grid B | col 1 | col 2 | col 3 | col 4 | col 5 | col 6
  - row 1 | {■} | {} | {} | {} | {} | {}
  - row 2 | {■} | {■} | {} | {} | {} | {}
  - row 3 | {■} | {■} | {■} | {} | {} | {}
  - row 4 | {■} | {■} | {■} | {■} | {} | {}
fill:
  - When row is 3, the inner loop runs {3} times.
  - SHADE runs {10} times in all.
text: **Program C.** Outer loop: FOR row FROM 1 TO 4 STEP 2. Inner loop: FOR col FROM 1 TO 6 STEP 2. Inside both loops: SHADE square (row, col).
table: Grid C | col 1 | col 2 | col 3 | col 4 | col 5 | col 6
  - row 1 | {■} | {} | {■} | {} | {■} | {}
  - row 2 | {} | {} | {} | {} | {} | {}
  - row 3 | {■} | {} | {■} | {} | {■} | {}
  - row 4 | {} | {} | {} | {} | {} | {}
fill:
  - The outer loop uses rows {1 and 3}.
  - SHADE runs {6} times in all.
text: **Program D.** Outer loop: FOR row FROM 1 TO 4. Inner loop: FOR col FROM 1 TO 6. Inside both loops: IF row + col is even THEN SHADE square (row, col).
table: Grid D | col 1 | col 2 | col 3 | col 4 | col 5 | col 6
  - row 1 | {■} | {} | {■} | {} | {■} | {}
  - row 2 | {} | {■} | {} | {■} | {} | {■}
  - row 3 | {■} | {} | {■} | {} | {■} | {}
  - row 4 | {} | {■} | {} | {■} | {} | {■}
fill:
  - The IF is checked {24} times.
  - SHADE runs {12} times in all.

## Stretch
write: Write a nested loop that shades only the border of the 4 by 6 grid. How many squares does it shade?
  lines: 5
  key: FOR row FROM 1 TO 4, FOR col FROM 1 TO 6, IF row = 1 OR row = 4 OR col = 1 OR col = 6 THEN SHADE square (row, col), END FOR col, END FOR row. It shades 16 squares (6 + 6 + 2 + 2).

# 6. Procedures That Return Values
minutes: 35
materials: pencil
ican: I can trace a procedure with parameters and say what each call returns.
directions: Each procedure takes values in (its parameters) and sends one value back (its return value). For each call, put the values into the parameters, trace the procedure, and write what it returns. When a call is inside another call, work from the inside out.
mistakes: Students mix up the order of parameters: in bigger(12, 3), a is 12 and b is 3. In shipping, students forget that elif is only checked when the first test is false, and that a return ends the procedure right away, so later lines never run. For nested calls, the inner call must be finished first: area(bigger(2, 4), 3) becomes area(4, 3).
notes: In bigger, when a > b is false (including a tie), the procedure skips to return b, so bigger(5, 5) returns 5. count_vowels counts only a, e, i, o and u, so "rhythm" returns 0 even though y can act as a vowel. shipping(6) is 5 + (6 - 2) x 2 = 13; shipping(10) is 5 + 8 x 2 = 21; anything over 10 pounds is a flat 25. Inside out: shipping(area(2, 3)) is shipping(6) = 13; bigger(count_vowels("queue"), 3) is bigger(4, 3) = 4; area(bigger(2, 4), 3) is area(4, 3) = 12.

## Warm up: Print or return?
example: def double(n): return n * 2. The call double(7) returns 14. Returning hands the value back to the code that called it, so y = double(7) + 1 makes y equal 15. Printing only shows a value on the screen; nothing is handed back.
fill:
  - double(9) returns {18}, and double(double(3)) returns {12}.

## Main: Four procedures
program: The procedures
  | def area(width, height):
  |     return width * height
  |
  | def bigger(a, b):
  |     if a > b:
  |         return a
  |     return b
  |
  | def count_vowels(word):
  |     total = 0
  |     for letter in word:
  |         if letter in "aeiou":
  |             total = total + 1
  |     return total
  |
  | def shipping(pounds):
  |     if pounds <= 2:
  |         return 5
  |     elif pounds <= 10:
  |         return 5 + (pounds - 2) * 2
  |     else:
  |         return 25
table: Call | Returns | Call | Returns
  - area(3, 5) | {15} | count_vowels("banana") | {3}
  - area(7, 2) | {14} | count_vowels("rhythm") | {0}
  - bigger(4, 9) | {9} | count_vowels("idea") | {3}
  - bigger(12, 3) | {12} | shipping(1) | {5}
  - bigger(5, 5) | {5} | shipping(6) | {13}
  - shipping(10) | {21} | shipping(15) | {25}

## Calls inside calls
fill:
  - area(bigger(2, 4), 3) returns {12}.
  - shipping(area(2, 3)) returns {13}.
  - bigger(count_vowels("queue"), 3) returns {4}.
  - total = shipping(1) + shipping(12) makes total equal {30}.

## Stretch
write: A 10-pound box costs 21 and an 11-pound box costs 25. Is that jump fair? Write a new last line for shipping that keeps adding 2 for each pound over 2, but never charges more than 25.
  lines: 3
  key: The jump of 4 for one more pound is uneven. One fix: else: return min(5 + (pounds - 2) * 2, 25). Then 11 pounds costs min(23, 25) = 23, and 12 pounds costs 25, the cap.

# 17. When Past Decisions Train the Model
minutes: 35
materials: pencil, highlighter
ican: I can explain how a model trained on past decisions can carry old bias forward.
directions: Read the case about a made-up company. Highlight the sentence that explains what the model learned from. Then answer the questions, using evidence from the paragraphs.
mistakes: Students say "the computer was sexist" as if the model chose to be unfair. The model has no opinions; it copied a pattern from past human decisions. Others think removing the word "gender" from the data fixes it; paragraph 4 shows the model found stand-in clues instead. Push for evidence from a numbered paragraph.
notes: The company and people are made up. A real case had the same shape: in 2018 news reports described a large technology company that stopped using an experimental resume-scoring tool after finding it rated resumes lower when they mentioned women's activities, such as a women's club. Engineers could not be sure they had removed every stand-in clue. Words to use: training data (the examples a model learns from), proxy (a clue that stands in for something the model was not given), audit (a check of who a system helps or harms).

## Read
passage: The Model That Learned the Past | numbered
  Company Q builds video games. Every year, thousands of people apply for its programming jobs, and reading every application takes weeks. So the company built a computer model to score applications from 1 to 5 stars. Managers would interview the five-star people first.
  To learn what a good application looks like, the model studied ten years of the company's own hiring records: every application, and whether that person was hired. For most of those years, almost all of the programmers Company Q hired were men. The model was never told anyone's gender. It was only told to find what the hired people's applications had in common.
  After a year, a manager noticed something strange. Applications that mentioned a girls' coding club or a women's college got lower scores. Two applicants with the same skills and the same projects got different stars when only one of them listed a women's soccer team.
  The engineers removed words like "women's" from what the model could see. The scores were still uneven. The model had found other clues that matched the old pattern, such as certain hobbies and certain schools. These clues stood in for the information that had been removed.
  The model was doing exactly what it was built to do: copying past decisions. But the past decisions were not fair. By learning from them, the model turned yesterday's habits into today's rules, and it did so quickly, quietly and thousands of times a day.
  Company Q stopped using the model to rank people. Its team now checks every hiring tool by comparing results for different groups of applicants before and after it is used.

## Questions
choice: What did the model learn from? (paragraph 2)
  - A list of the skills every programmer needs
  * Ten years of the company's past hiring decisions
  - Advice from expert programmers at other companies
  - The applicants' test scores
choice: The model was never told anyone's gender. How did its scores still end up unfair? (paragraphs 3 and 4)
  - It guessed gender from each applicant's photo.
  - The engineers told it to prefer men.
  * It found clues, like clubs, hobbies and schools, that matched the old pattern of who was hired.
  - It made random mistakes.
write: Explain in your own words how bias "carried forward" from the past into the model.
  lines: 3
  key: The company mostly hired men in the past. The model learned that the applications of people who were hired looked like men's applications, so it gave those higher scores. The old unfair pattern became the model's rule for new applicants.
write: Paragraph 5 says the model worked "quickly, quietly and thousands of times a day." Why does that make the problem worse than one unfair manager?
  lines: 3
  key: One manager makes a limited number of decisions, and people might notice and question them. The model repeats the same unfair pattern on every application, so it affects many more people, and because it looks like a neutral computer, the unfairness is harder to spot.
write: You are on Company Q's team. Name two checks you would run before using a new hiring model.
  lines: 3
  key: Compare the scores for different groups of applicants with the same skills; test pairs of applications that differ only in one detail, like a club name; look for proxy clues; check whether the training data itself was fair; have people review the model's top and bottom picks.

## Stretch
write: Could a model trained on past decisions ever be fair? What would its training data need?
  lines: 3
  key: Possibly, if its training data came from fair decisions that included all groups, and if it is audited often. If the past data is biased, the model will be too, so the data must be checked before training, not just the model afterward.

# 24. Choose the Granularity
minutes: 30
materials: pencil
ican: I can choose the level of detail data needs for a purpose, without collecting more than it needs.
directions: Granularity is how detailed data is: every second, every hour, every day, or one total for the year. For each use, choose the level of detail that answers the question without collecting extra. Then explain your thinking.
mistakes: Students often pick the most detailed option because "more data is better." Push back: extra detail costs storage and time, and detail about people can become a privacy risk. Others pick the coarsest option and lose the answer (a yearly total cannot tell you whether to bring an umbrella this afternoon).
notes: The right choice depends on the question being asked, so there are two tests for each option: can it answer the question, and does it collect more than the question needs? In the stretch, publishing numbers for very small groups can reveal facts about individuals; agencies often combine small groups or hide counts under a minimum size (for example, fewer than 10).

## Warm up
example: Temperature, finest to coarsest: every second, every hour, every day, the average for the month.
fill:
  - Daily rainfall totals are {coarser} than hourly rainfall totals.
  - One student's arrival time to the second is {finer} than the number of students present each day.

## Main: Choose the level of detail
choice: A weather app tells you whether to bring an umbrella this afternoon.
  * Hourly rain chances for your town today
  - The average rainfall for the whole state this year
  - Rain at your house measured every second for a year
  - Monthly rainfall for the country
choice: The district's yearly attendance report compares its schools.
  - Each student's exact arrival time, to the second, with their name
  * The percent of students present each month at each school
  - One attendance number for the whole district for the year
  - A list of every absent student and where they live
choice: A city is deciding which streets need bike lanes.
  - Every rider's name and exact path, recorded every second
  - The total number of bike trips in the city last year
  * The number of bike trips on each street each day, with no names
  - A list of the most popular bike colors
choice: A runner and coach plan training for a race.
  - The runner's total distance for the whole year
  - The runner's heart rate every thousandth of a second, all day, every day
  - The weather on race day last year
  * The time for each kilometer of each run
choice: The cafeteria orders milk for next week.
  * How many cartons of each kind were taken each day for the last few weeks
  - Which student took which carton, by name, every day
  - The total milk ordered by the school in the past ten years
  - The temperature of every carton every minute

## Explain
write: Pick one of the five uses. Explain what goes wrong with an option that is too coarse.
  lines: 3
  key: Example: For the umbrella question, a state yearly average cannot tell whether it will rain in your town this afternoon, so it cannot answer the question at all.
write: Pick one of the five uses. Explain what goes wrong with an option that is too fine.
  lines: 3
  key: Example: Recording every bike rider's name and path every second answers the bike-lane question no better than daily street counts, but it costs far more to store and could reveal where each person lives, works and goes.

## Stretch
write: The district wants to post attendance by grade for each school. One small school has only 2 students in grade 6. Why could that be a privacy problem, and what could the district do instead?
  lines: 4
  key: With only 2 students, a low attendance rate could show exactly who was absent, so the data reveals private facts about real people. The district could combine small groups (grades 6 to 8 together), or not report any group smaller than a minimum size, such as 10.

# 29. Duplicate Detective
minutes: 30
materials: pencil, highlighter
ican: I can find duplicate and near-duplicate records and decide which one to keep.
directions: The Robotics Club roster was typed by three different people, so some members were entered more than once. Find the 7 records that repeat an earlier member. Watch out: a matching name is not always the same person. For each duplicate, decide which record to keep, or how to merge them.
mistakes: Students match names only and flag the two Alex Chens, who are in different grades and homerooms: two real people. Others miss near-duplicates that do not look exactly alike (Jordon Lee, Kim, Ava). Deleting the newer record is not always right: record 17 has Leo's new homeroom, so the best fix merges the two.
notes: The roster is made up. Duplicates: 7 is 1 (capital letters), 11 is 2 (spelling), 12 is 3 (last name first), 14 is 5 (nickname), 15 is 6 (exact copy), 17 is 8 (homeroom changed), 19 is 10 (accent mark). Records 4 and 9 are different people. The club has 14 members, not 21. When two spellings differ (Jordan or Jordon, Diaz or Díaz), the honest fix is to ask the student, not to guess; the key shows a likely choice and flags it. Real data tools often flag possible duplicates for a person to review rather than deleting them automatically.

## The roster
table: # | Name | Grade | Homeroom | Joined | # | Name | Grade | Homeroom | Joined
  - 1 | Maya Patel | 7 | 112 | Sep 6 | 12 | Kim, Ava | 6 | 104 | Sep 14
  - 2 | Jordan Lee | 7 | 108 | Sep 6 | 13 | Ben Okafor | 8 | 114 | Sep 10
  - 3 | Ava Kim | 6 | 104 | Sep 7 | 14 | Sam Ortiz | 8 | 115 | Sep 15
  - 4 | Alex Chen | 6 | 101 | Sep 7 | 15 | Priya Shah | 8 | 117 | Sep 8
  - 5 | Samuel Ortiz | 8 | 115 | Sep 7 | 16 | Tess Moreno | 6 | 102 | Sep 12
  - 6 | Priya Shah | 8 | 117 | Sep 8 | 17 | Leo Grant | 6 | 105 | Oct 3
  - 7 | maya patel | 7 | 112 | Sep 12 | 18 | Ruby Hall | 7 | 109 | Sep 16
  - 8 | Leo Grant | 6 | 103 | Sep 8 | 19 | Nora Díaz | 7 | 110 | Sep 9
  - 9 | Alex Chen | 8 | 116 | Sep 9 | 20 | Omar Haddad | 6 | 101 | Sep 18
  - 10 | Nora Diaz | 7 | 110 | Sep 9 | 21 | Lily Tran | 8 | 116 | Sep 18
  - 11 | Jordon Lee | 7 | 108 | Sep 13 | | | | |

## Warm up
choice: Records 4 and 9 are both Alex Chen. Are they duplicates?
  - Yes, the names match exactly.
  * No, they are in different grades and homerooms, so they are two people.
  - Yes, delete record 9.
  - No, because record 9 joined later.

## Main: Find the 7 duplicates
table: Duplicate record | Same member as record | What is different | Keep or merge
  - {7} | {1} | {lowercase letters} | {keep 1}
  - {11} | {2} | {Jordon or Jordan spelling} | {keep 2; ask which spelling is right}
  - {12} | {3} | {last name first} | {keep 3}
  - {14} | {5} | {nickname Sam for Samuel} | {keep 5}
  - {15} | {6} | {nothing: exact copy} | {keep 6}
  - {17} | {8} | {new homeroom} | {merge: homeroom 105 from 17, Sep 8 join date from 8}
  - {19} | {10} | {accent mark in Díaz} | {keep one; ask Nora how she spells it}
fill:
  - The roster has {21} records but only {14} real members.

## Stretch
write: Write a rule a computer could use to flag possible duplicates. Why should it flag them for a person to check instead of deleting them?
  lines: 3
  key: Example: flag two records with the same grade and homeroom whose names match after ignoring capital letters, accent marks and word order, or differ by one letter. A person should check because some matches are different people (like two Alex Chens) and some differences need a decision, like which spelling is right.

# 40. Screen Reader Order
minutes: 30
materials: pencil
ican: I can predict the order a screen reader reads a page and fix problems that confuse it.
directions: A screen reader reads a web page aloud in the order the parts appear in the page's code, not the order your eyes see them. Read the code, then number each part of the page mockup in the order a screen reader reaches it. Then find and fix 2 problems.
mistakes: Students number the mockup the way they would read it with their eyes (top to bottom), which puts the email sign-up box second. The code order decides: the sign-up form comes near the end of the code, so it is read 8th. Some students say the photo is fine because it has alt text; "IMG_0042.jpg" is a file name, not a description.
notes: Reading order is code order (WCAG 1.3.2, Meaningful Sequence): A 1, B 2, C 3, D 4, E 5, F 6, G 7, I 8, H 9. Problems a student can fix: the sign-up box is shown near the top but read 8th, so move the form in the code to right after the heading (or move it on screen to match); the link text "Click here" makes no sense out of context (WCAG 2.4.4, Link Purpose), so use "Sign up for Summer Reading"; the photo's alt text is a file name (WCAG 1.1.1), so describe it ("Kids reading on beanbags in the library"). The library is made up.

## The page code
program: Simplified code for the page (read from top to bottom)
  | <header>
  |   <img src="logo.png" alt="Lakeside Library home">
  |   <nav> Home, Events, Books, Contact </nav>
  | </header>
  | <h1> Summer Reading Kickoff </h1>
  | <img src="IMG_0042.jpg" alt="IMG_0042.jpg">
  | <p> Join us June 10 at 2 p.m. for games, prizes and a reading log. </p>
  | <a href="/signup"> Click here </a>
  | <aside> Hours: Monday to Saturday, 9 to 6 </aside>
  | <form> Get reading news by email: [email box] [Join] </form>
  | <footer> 12 Lake Street. Contact us. </footer>

## Main: Number the reading order
text: The page as it looks on screen. Write the reading order number in each box.
table: Left side of the screen | Right side of the screen
  height: 0.7
  - **A** Logo: Lakeside Library. Order: {1} | **B** Menu: Home, Events, Books, Contact. Order: {2}
  - **C** Big heading: Summer Reading Kickoff. Order: {3} | **I** Box: Get reading news by email [ ] Join. Order: {8}
  - **D** Photo of kids reading on beanbags. Order: {4} | **E** Join us June 10 at 2 p.m. for games, prizes and a reading log. Order: {5}
  - **F** Link: Click here. Order: {6} | **G** Hours: Monday to Saturday, 9 to 6. Order: {7}
  - **H** Footer: 12 Lake Street. Contact us. Order: {9} |
fill:
  - A sighted visitor sees box I right after the heading, but a screen reader reads it {8th} out of 9.

## Find and fix 2 problems
chart: The problem | Who it confuses and why | Your fix
  labels: Problem 1; Problem 2
  height: 0.9
  key: Any two: (1) Box I is near the top on screen but read 8th, so a screen reader user may never know it is there or hear it out of place; move the form in the code to just after the h1. (2) The link says "Click here," which means nothing when a screen reader lists links; change it to "Sign up for Summer Reading." (3) The photo's alt text is a file name, so the user hears "IMG underscore 0042 dot jpg"; change it to "Kids reading on beanbags in the library."

## Stretch
write: Why is it a problem when the order on screen and the order in the code do not match? Who else, besides screen reader users, could it affect?
  lines: 3
  key: Screen reader users hear the parts in a different order than they appear, so the page makes less sense and important parts seem missing. People who move through a page with the Tab key instead of a mouse also follow code order, so their focus jumps around the screen.

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

# 1. Pseudocode a Quiz Game
minutes: 35
materials: pencil
ican: I can plan a program in pseudocode with a variable, a loop and an if-else.
directions: Finish the quiz game pseudocode, then trace it. Last, write pseudocode for your own 5-question quiz with a score variable, a loop and if-else feedback.
mistakes: The most common bug is setting the score to 0 inside the loop, which wipes out the points after every question. Ask students to trace it with three right answers and watch the score. Others forget the ELSE, so a wrong answer gets no feedback at all.
notes: Pseudocode is a plan written in plain words that look like code; there is no one right spelling, but every line should be one clear action. Line 4 accepts "right" or "correct"; line 7 must be ELSE. Traces: three right answers end with score 3; starting at 1 by mistake gives 4; the loop asks 5 times. Students who finish early can type the plan into a block or text language later.

## Warm up: Words in pseudocode
example: SET score TO 0 makes a variable called score that starts at 0. REPEAT 5 TIMES runs the lines inside it 5 times. IF ... THEN ... ELSE picks one of two paths.
choice: Where must SET score TO 0 go?
  * Before the loop starts
  - Inside the loop, before each question
  - After the loop ends
  - It is not needed

## Main: Finish the quiz
table: Line | Pseudocode
  - 1 | SET score TO {0}
  - 2 | REPEAT {5} TIMES
  - 3 | ASK the next question
  - 4 | IF the answer is {right} THEN
  - 5 | SAY "Correct!"
  - 6 | SET score TO score + {1}
  - 7 | {ELSE}
  - 8 | SAY "Not quite. The answer is ..."
  - 9 | END IF
  - 10 | END REPEAT
  - 11 | SAY "Your score is " and then {score}
fill:
  - Ana gets questions 1, 2 and 4 right. At the end, score is {3}.
  - How many times does the program run line 3? {5}
  - Ana's line 8 runs {2} times.
  - Bug: line 1 says SET score TO 1. With the same answers, Ana's score is {4}.

## Your quiz
write: Write pseudocode for your own 5-question quiz on a topic you like. Use a score variable, a REPEAT loop and IF ... ELSE feedback. Number your lines.
  lines: 10
  key: Model (any topic): 1 SET score TO 0. 2 REPEAT 5 TIMES. 3 ASK the next animal question. 4 IF the answer is right THEN. 5 SAY "Yes!" 6 SET score TO score + 1. 7 ELSE. 8 SAY "Good try. The answer is ..." 9 END IF. 10 END REPEAT. 11 SAY "You got " score " out of 5." Check: score is set before the loop, the loop runs 5 times, and both paths of the IF give feedback.

## Stretch
write: Add lines so a perfect score gets a special message. Where do they go?
  lines: 3
  key: After END REPEAT: IF score = 5 THEN SAY "Perfect score!" END IF. It must come after the loop, when all 5 questions are done.

# 6. Five-Step Debugging Routine
minutes: 35
materials: pencil
ican: I can find and fix a bug step by step instead of guessing.
directions: Each program has a bug. Use the five steps for each one and write a short note in its box. Reproduce: run it and write what really happens. Isolate: find the line or lines where it goes wrong. Guess: say why. Fix: write the new code. Test: run it again and write what happens now.
mistakes: Students jump straight to Fix and change lines at random. Make them write the Reproduce box first, with the actual output, and compare it to what the program should do. In Program 1, students often "fix" it by changing count = 5 to count = 6; that works, but say why moving the say line is the clearer fix. In Program 3, the computer divides before it adds, so only c is divided by 3.
notes: Program 1 prints 4, 3, 2, 1, 0 because it subtracts before it speaks; moving "say count" above the subtract line (or starting at 6) prints 5, 4, 3, 2, 1. Program 2 needs 11 coins because score > 10 is false when score is 10; use score >= 10 (or score = 10). Program 3 gives 6 + 9 + 1 = 16 because division happens before addition; (a + b + c) / 3 = 18 / 3 = 6. Testing means running it again with the same input and checking the output, and for Program 2 also checking that 9 coins does not win.

## Warm up: The five steps
example: Reproduce (make the bug happen and write what you see), Isolate (find where it goes wrong), Guess (why it goes wrong), Fix (change the code), Test (run it again to be sure).
fill:
  - You change score > 10 to score >= 10. That step is {Fix}.
  - You run the program and write, "It said 4, 3, 2, 1, 0." That step is {Reproduce}.
  - You cover lines until you find the one that causes the problem. That step is {Isolate}.

## Main: Three buggy programs
program: Program 1: Countdown. It should say 5, 4, 3, 2, 1, then "Blast off!"
  | count = 5
  | repeat 5 times:
  |     count = count - 1
  |     say count
  | say "Blast off!"
program: Program 2: Coin game. A player should win when they collect 10 coins.
  | score = 0
  | when a coin is collected:
  |     score = score + 1
  |     if score > 10:
  |         say "You win!"
program: Program 3: Average. It should say the average of 6, 9 and 3, which is 6.
  | a = 6
  | b = 9
  | c = 3
  | average = a + b + c / 3
  | say average
chart: Program 1 | Program 2 | Program 3
  labels: Reproduce; Isolate; Guess; Fix; Test
  height: 0.8
  key: Program 1: Reproduce: it says 4, 3, 2, 1, 0. Isolate: lines 3 and 4. Guess: it subtracts before it says the number. Fix: put "say count" above "count = count - 1". Test: it says 5, 4, 3, 2, 1, Blast off! Program 2: Reproduce: 10 coins, no win; it says "You win!" at 11. Isolate: line 4. Guess: 10 > 10 is false. Fix: if score >= 10. Test: wins at 10 coins, not at 9. Program 3: Reproduce: it says 16. Isolate: line 4. Guess: it divides only c by 3 (3 / 3 = 1), then adds 6 + 9 + 1. Fix: average = (a + b + c) / 3. Test: it says 6.

## Stretch
write: Why is it better to follow the five steps than to change lines until the program seems to work?
  lines: 3
  key: Random changes can hide the bug or add new ones, and you will not know why it works. Reproducing and isolating shows exactly where and why it fails, and testing proves the fix really worked.

# 18. Which Lock Broke?
minutes: 30
materials: pencil, scissors, glue
ican: I can tell whether confidentiality, integrity or availability failed in a security problem.
directions: Every system has three locks. Confidentiality: only the right people can see the information. Integrity: the information stays correct and is not changed by the wrong people. Availability: people can use the system when they need it. Cut out the 9 cards. Glue each under the lock that broke.
mistakes: Students often put every attack under confidentiality because an attacker was involved. Ask the question: did the wrong person SEE it (confidentiality), was it CHANGED (integrity), or could people not USE it (availability)? A power outage has no attacker, but availability still broke.
notes: Three cards go under each lock. Some real events break more than one lock; on this sheet each card has one clear main failure. Protections in the stretch: confidentiality, strong passwords, locking screens and sharing settings; integrity, edit permissions, backups and checking changes; availability, backup power, extra servers and blocking floods of fake traffic.

## Warm up
choice: A hacker reads a list of students' home addresses. Which lock broke?
  * Confidentiality
  - Integrity
  - Availability
choice: Someone changes the score in a game's high score list to 999,999. Which lock broke?
  - Confidentiality
  * Integrity
  - Availability
choice: The school's homework site is down all night. Which lock broke?
  - Confidentiality
  - Integrity
  * Availability

## Main: Sort the 9 scenarios
sort: Which lock broke?
  - Confidentiality: A stranger reads a class's private grade list left open on a library computer; Someone guesses a weak password and reads a student's private messages; A list of students' allergies is posted on the public school web page by mistake
  - Integrity: A prankster changes the lunch menu file to say "pizza every day"; A virus changes numbers in the class spreadsheet of test scores; Someone edits the online sports schedule so the game time is wrong
  - Availability: The school website crashes on a snow day when too many people visit at once; A power outage shuts down the library checkout computers for a day; An attacker floods a game server with fake requests so no one can log in

## Stretch
chart: Lock | One way to protect it
  labels: Confidentiality; Integrity; Availability
  key: Confidentiality: strong passwords, log out or lock the screen, share private files only with the right people. Integrity: let only some people edit, keep backups, check changes. Availability: backup power, more than one server, block floods of fake traffic.

# 22. Binary Mystery Picture
minutes: 25
materials: pencil, a dark crayon or marker
ican: I can write numbers in binary using place values 16, 8, 4, 2 and 1.
directions: Write each number in 5-bit binary under the place values 16, 8, 4, 2 and 1. Shade every square that holds a 1. A picture will appear.
mistakes: Students who start from the right with 1 often run out of places. Start at 16 and ask "does 16 fit?" each time. A row that does not add back up to its number has a mistake.
notes: Computers store pictures exactly like this: each row is a number, each 1 is a lit pixel. The mystery picture is a rocket. Students can make their own 5-wide picture and turn it into numbers for a partner.

## Warm up: Place values
example: 13 = 8 + 4 + 1, so 13 in binary is 01101.
fill:
  - 5 = 4 + {1}, so 5 is 00{101}
  - 18 = 16 + {2}, so 18 is {10010}

## Main: Decode the picture
binary: Fill in 0 or 1, then shade each 1.
  bits: 5
  numbers: 4 14 10 14 14 14 31 21 4 10

## Stretch: Your turn
write: Plan your own 5-wide picture on scrap paper. Write the numbers a partner would need to draw it.
  lines: 2
  key: Answers vary. Check that each number adds up to the shaded places in its row.

# 29. Scatter Plot Story
minutes: 30
materials: pencil, ruler
ican: I can plot data on a scatter plot and tell whether two things have a positive, negative or no relationship.
directions: A class grew 12 bean plants with different amounts of sunlight each day. After 3 weeks they measured each plant's height. Plot one dot for each plant. Then decide what story the dots tell.
mistakes: Students connect the dots like a line graph; a scatter plot keeps the dots separate. Others plot (height, hours) instead of (hours, height): sunlight goes across, height goes up. Students may call the relationship "none" because two plants with 4 hours have different heights; the overall upward drift is what makes it positive.
notes: The data is made up for practice. The relationship is positive: more sunlight goes with taller plants, but not perfectly, because plants vary (seeds, water, soil). A fair prediction for 5 hours is about 10 to 12 cm. Science caution for the stretch: in very low light, seedlings can grow tall and thin while they search for light, so real data at the dark end can surprise you; that is one reason scientists repeat trials and look at more than height.

## The data
table: Plant | A | B | C | D | E | F | G | H | I | J | K | L
  - Sunlight (hours per day) | 2 | 3 | 4 | 4 | 5 | 6 | 6 | 7 | 8 | 9 | 10 | 11
  - Height (cm) | 5 | 7 | 8 | 10 | 11 | 12 | 14 | 15 | 15 | 18 | 19 | 21

## Warm up
example: Plant A got 2 hours of sunlight and grew 5 cm. Its dot goes across to 2, then up to 5.
fill:
  - Plant J's dot goes across to {9} and up to {18}.
  - The tallest plant is Plant {L}, at {21} cm.

## Main: Plot and decide
graph: Sunlight (hours per day) | 0 12 1 | Plant height (cm) | 0 24 2
  key: 2,5 3,7 4,8 4,10 5,11 6,12 6,14 7,15 8,15 9,18 10,19 11,21
  dots: yes
choice: What relationship do the dots show?
  * Positive: as sunlight goes up, height tends to go up.
  - Negative: as sunlight goes up, height tends to go down.
  - None: the dots are scattered with no pattern.
fill:
  - Plants C and D both got 4 hours, but their heights differ by {2} cm.
  - A new plant gets 5 hours of sunlight. A good prediction for its height is about {11} cm.
choice: A snack stand records each day of the year. How would "outdoor temperature" and "mugs of hot cocoa sold" most likely look on a scatter plot?
  - Positive
  * Negative
  - None
choice: How would "a student's shoe size" and "the number of letters in the student's first name" most likely look?
  - Positive
  - Negative
  * None

## Stretch
write: Plants C and D got the same sunlight but grew different heights. Give two reasons data like this varies, and say why the class grew 12 plants instead of 2.
  lines: 3
  key: Each seed is a little different, and plants may get different water, soil or warmth; measuring can also be a little off. With 12 plants, the overall pattern shows through the variation; with 2, one unusual plant could fool you.

# 41. Computing Career Web
minutes: 30
materials: pencil
ican: I can connect computing skills to jobs in many fields.
directions: Computing skills are used in almost every job. First match each skill to what it means. Then, for each skill, name a job in health, art, sports or science that uses it and tell how. Use each field at least once. Last, draw your career web.
mistakes: Students name only "computer programmer" or "game maker." Push for jobs outside tech: a nurse, an animator, a coach, a scientist. Others name a job without the how; the how is the connection on the web.
notes: Jobs in the key are real examples; many answers work. Sports teams employ data analysts who study game statistics; animators and illustrators draw with digital tools; hospitals rely on security staff to protect patient records; fitness trackers and medical monitors are built around sensors; 3D printing is used for science models and for custom prosthetic hands.

## Warm up: What does each skill mean?
match: Match each skill to its meaning.
  - Coding = Writing step-by-step instructions a computer follows
  - Working with data = Collecting numbers and finding patterns in charts and tables
  - Digital art and design = Drawing, animating or laying out pictures on a computer
  - Building with sensors = Making devices that measure things like heat, light or motion
  - Keeping data safe = Protecting information from people who should not see or change it
  - 3D modeling = Designing shapes on a computer that can be printed as real objects

## Main: Connect skills to jobs
chart: Field | A job in that field | How the job uses this skill
  labels: Coding; Working with data; Digital art and design; Building with sensors; Keeping data safe; 3D modeling
  key: Examples: Coding: sports, app developer, writes the code for an app that shows live game scores. Working with data: sports, team data analyst, studies players' shot numbers to plan the next game. Digital art and design: art, animator, draws and moves characters for cartoons on a computer. Building with sensors: health, medical device engineer, builds monitors that measure a patient's heartbeat. Keeping data safe: health, hospital security specialist, protects patient records from people who should not see them. 3D modeling: science, museum scientist, prints a model of a fossil bone to study and share.
draw: My career web: write Computing Skills in a circle in the middle, the 4 fields around it, then draw lines from each field to its skills and jobs | 2.6
note: A complete web has a center, all 4 fields, all 6 skills, and at least one job on each line.

## Stretch
write: Which computing skill would you most like to learn? Name a job in any field where you could use it.
  lines: 2
  key: Answers vary. Example: Working with data. I could be a scientist who tracks bird counts and finds out which birds are disappearing.

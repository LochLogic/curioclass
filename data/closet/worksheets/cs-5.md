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

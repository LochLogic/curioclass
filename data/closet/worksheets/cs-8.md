# 1. Which Algorithm Is Better?
minutes: 40
materials: pencil
ican: I can compare two algorithms that solve the same problem by counting their steps.
directions: Two students wrote algorithms to find the largest number in a list. Trace both on the same list, count the comparisons each one makes, and fill the table for longer lists. Then judge which algorithm is better and why.
mistakes: Students often count lines of code instead of comparisons, or count Algorithm B's comparisons for only one candidate. B checks every number against every number until it finds the winner, so its worst case is when the largest number is last. Some say the algorithms are "the same" because both give the right answer: correctness is the first test, but not the only one.
notes: A comparison is one "is this bigger than that?" check. Algorithm A makes n - 1 comparisons on any list of n numbers. Algorithm B, as written, compares each candidate to all n numbers (itself included) and stops at the first candidate never beaten, so its best case is n (largest first) and its worst case is n x n (largest last). On 3, 8, 2, 9, 5, the 9 is the 4th candidate: 4 x 5 = 20 comparisons. For n = 1,000, A makes 999 and B up to 1,000,000.

## The two algorithms
table: Algorithm A (one pass)
  - SET biggest TO the first number
  - FOR each other number in the list
  - IF number > biggest THEN SET biggest TO number
  - END FOR
  - RETURN biggest
table: Algorithm B (check every candidate)
  - FOR each number x in the list
  - SET beaten TO false
  - FOR each number y in the list: IF y > x THEN SET beaten TO true. END FOR y
  - IF beaten is false THEN RETURN x
  - END FOR x

## Warm up: Trace A on 3, 8, 2, 9, 5
table: Number checked | Is it > biggest? | biggest after
  - (start) | (none) | 3
  - 8 | {yes} | {8}
  - 2 | {no } | {8}
  - 9 | {yes} | {9}
  - 5 | {no } | {9}
fill:
  - Algorithm A makes {4} comparisons and returns {9}.

## Main: Trace B and count
fill:
  - For x = 3, B compares 3 to all {5} numbers. Is 3 beaten? {yes}
  - B finds a winner when x = {9}, the {4th} candidate it tries.
  - In all, B makes {20} comparisons on this list.
table: List length (n) | A comparisons | B comparisons, worst case (largest last)
  - 5 | {4} | {25}
  - 10 | {9} | {100}
  - 20 | {19} | {400}
  - 1,000 | {999} | {1,000,000}
fill:
  - B's best case (largest number first) for a list of 20 takes {20} comparisons.

## Critique
write: Which algorithm is better? Give two reasons, using numbers from your table.
  lines: 4
  key: Algorithm A. Both are correct, but A makes n - 1 comparisons while B can make n x n: for 20 numbers, 19 versus 400, and for 1,000 numbers, 999 versus 1,000,000. A's work grows in step with the list; B's grows much faster. A also reads the list only once.
write: Is there any list where B does about as well as A? Explain.
  lines: 2
  key: Yes, when the largest number is first: B finds it with n comparisons (20 for 20 numbers), close to A's n - 1. But we cannot count on that, so we judge by the worst case.

## Stretch
write: Suggest one change that would make B faster without changing its answer.
  lines: 3
  key: Stop the inner loop as soon as x is beaten (no need to keep comparing), or skip comparing x with itself. Either cuts comparisons, but B is still about n x n in the worst case; only a one-pass idea like A gets to n - 1.

# 6. Document a Procedure
minutes: 35
materials: pencil
ican: I can write documentation that lets someone use a procedure without reading its code.
directions: Good documentation tells another programmer what a procedure does, what to give it, what it gives back, how to call it, and what happens in unusual cases. Trace the procedure first, then write its documentation using the frame.
mistakes: Students explain how the code works line by line instead of what it does for the caller; documentation should let someone use the procedure without reading its body. Others list parameter names without types or defaults. For edge cases, push past "it works": what does it return for 0 days, a negative number, or a very late book?
notes: Traces: late_fee(8) = 8 x 0.25 = 2.0. late_fee(30) is 7.5 before the cap, so it returns 5.0. late_fee(20) is exactly 5.0. late_fee(0) and any negative number return 0. late_fee(3, 0.5) = 1.5. late_fee(12, 0.5, 4.0) is 6.0 before the cap, so 4.0. In the stretch, initials("Kiri") returns "KK" because the first and last word are the same word, and initials("") crashes with an IndexError because split() returns an empty list. In Python, documentation like this usually goes in a docstring, the string on the first line inside the def.

## The procedure
program: A library late fee
  | def late_fee(days_late, daily_rate=0.25, max_fee=5.00):
  |     if days_late <= 0:
  |         return 0
  |     fee = days_late * daily_rate
  |     return min(fee, max_fee)

## Warm up: Trace it
table: Call | Returns | Call | Returns
  - late_fee(8) | {2.0} | late_fee(0) | {0}
  - late_fee(30) | {5.0} | late_fee(3, 0.5) | {1.5}
  - late_fee(20) | {5.0} | late_fee(12, 0.5, 4.0) | {4.0}

## Main: Write the documentation
write: **Purpose.** In one sentence, what does late_fee do?
  starter: late_fee figures out ...
  lines: 2
  key: late_fee figures out how much a library patron owes for a book returned late, charging a daily rate up to a maximum.
write: **Parameters.** For each one, give its name, its type, what it means and its default if it has one.
  lines: 4
  key: days_late (number): how many days late the book is. daily_rate (number, default 0.25): the charge for each late day, in dollars. max_fee (number, default 5.00): the most the fee can ever be, in dollars.
write: **Return value.** What does it give back, and in what unit?
  lines: 2
  key: The fee in dollars, a number from 0 up to max_fee: 0 if the book is not late, otherwise days_late x daily_rate, but never more than max_fee.
write: **Example call.** Write one call and what it returns.
  starter: late_fee( ... ) returns ...
  lines: 2
  key: late_fee(8) returns 2.0 (8 days at 0.25 a day). Or: late_fee(30) returns 5.0, because 7.50 is over the cap.
write: **Edge case.** Describe one unusual input and what happens.
  lines: 3
  key: If days_late is 0 or negative (returned early or on time), it returns 0 instead of a negative fee. Also: a very late book never costs more than max_fee, so 30 days and 300 days both return 5.0.

## Stretch
program: Another procedure
  | def initials(full_name):
  |     parts = full_name.split()
  |     return parts[0][0] + parts[-1][0]
fill:
  - initials("Ada Lovelace") returns {"AL"}, and initials("Kiri") returns {"KK"}.
write: initials("") crashes. Write the edge-case line of its documentation, and suggest a fix.
  lines: 3
  key: Edge case: full_name must contain at least one word; an empty string crashes (IndexError), and a one-word name repeats its letter ("Kiri" gives "KK"). Fix: if parts is empty, return an empty string; if there is one word, return just its first letter.

# 17. Algorithmic Grading Debate
minutes: 40
materials: pencil
ican: I can argue a position about an algorithm's use with reasons, evidence and a response to the other side.
directions: Should a computer program grade students' essays? Read the fact cards. Sort each statement as a reason for or against. Then choose a side and write your argument using the frame.
mistakes: Students pick a side but use reasons with no evidence ("it's just bad"). Each reason should point to a fact card. The counterargument part is often a straw man; push students to state the other side's best point fairly before answering it. Some argue for a middle position (a program as a first reader with a teacher deciding); that is a real side if they defend it.
notes: The fact cards are general and accurate: programs that score essays learn from essays people already scored; they measure features like length, vocabulary and grammar more easily than the quality of ideas; researchers have shown some can be fooled by long essays full of fancy words that make little sense; and some large exams have paired a computer score with a human reader. Either side can earn full credit with two supported reasons and a fair, answered counterargument.

## Fact cards
table: Card | Fact
  - 1 | A program can score thousands of essays in minutes and give feedback right away.
  - 2 | A program gives the same essay the same score every time. Human graders can get tired or disagree with each other.
  - 3 | Programs learn by studying essays that people already graded, so they copy those graders' patterns, including any unfairness.
  - 4 | Researchers have shown that some scoring programs give high scores to long essays full of fancy words that make little sense.
  - 5 | Programs measure length, vocabulary and grammar more easily than whether an idea is creative, true or well argued.
  - 6 | Some large exams have used a computer score alongside a human reader, with another person checking when the two disagree.

## Warm up: For or against?
table: Statement | Reason for or against computer grading? | Fact card
  - Students get feedback the same day and can revise sooner. | {for} | {1}
  - A student could learn to write long, fancy nonsense to get a high score. | {against} | {4}
  - Scores are consistent, even at the end of a long day. | {for} | {2}
  - A creative essay that breaks the usual pattern might be scored low. | {against} | {5}
  - If past graders were unfair to some students, the program learns it. | {against} | {3}

## Main: Your argument
write: **Claim.** Should a program grade essays at our school?
  starter: I believe a program should / should not grade essays because ...
  lines: 2
  key: Model (against): I believe a program should not be the final grader of our essays because it can be fooled and it cannot judge ideas.
write: **Reason 1** with evidence from a fact card.
  starter: First, ... For example, fact card __ shows ...
  lines: 3
  key: First, a program can be tricked. Fact card 4 shows that researchers got high scores for long essays full of fancy words that made little sense, so students might learn to write for the machine instead of the reader.
write: **Reason 2** with evidence from a fact card.
  starter: Second, ...
  lines: 3
  key: Second, programs measure what is easy to count, such as length and vocabulary, more than whether an argument is strong or creative (card 5). The skills we most want to grow would count least.
write: **The other side** and your response.
  starter: People who disagree say ... However, ...
  lines: 4
  key: People who disagree say a program is fast and consistent (cards 1 and 2), so students get feedback sooner. However, fast feedback is only useful if it is accurate. A program could give quick hints on grammar while a teacher gives the grade, as some exams pair a computer with a human reader (card 6).
write: **Conclusion.**
  lines: 2
  key: A program can help as a first reader, but a teacher should decide the grade, because essays are about ideas, and only people can fairly judge them.

## Stretch
write: Fact card 3 says programs copy the patterns of past graders. Suggest one way a school could check that a grading program is fair before using it.
  lines: 3
  key: Have teachers grade a sample of essays from many different groups of students, then compare the program's scores; if it scores one group lower for essays of the same quality, it is not fair. Also test it with tricky essays, like long nonsense.

# 24. Data Minimization Form
minutes: 35
materials: pencil
ican: I can design a form that collects only the data it truly needs.
directions: The Chess Club's old sign-up form asks for far too much. For each field, decide whether the club truly needs it: keep it or cut it, and give a short reason. Then design the new form.
mistakes: Students cut fields they find boring and keep fields that "might be useful someday." The test is the club's purpose right now: running meetings and reaching a family if plans change. Watch for students who keep date of birth "for safety"; grade already tells the club what it needs. Some cut the guardian contact, which the club does need.
notes: Data minimization means collecting only what you need for a stated purpose and keeping it only as long as you need it. It is a core idea in privacy laws such as the European GDPR. Every field the club does not collect is a field that cannot leak. Allergy information is a judgment call worth discussing: if the club serves snacks it is needed for safety, so ask a narrow question and use it only for snacks. Fair answers for the "why" column vary; the key gives one short reason each.

## Warm up
example: Purpose: a reading club that meets after school on Mondays. Needed: name, grade, a guardian contact. Not needed: home address, because nothing is mailed.
choice: Which question decides whether a field stays on a form?
  - Could this ever be useful?
  * Does the club need it for what it does right now?
  - Do other forms ask for it?
  - Is it easy to fill in?

## Main: Keep or cut?
table: Field on the old form | Keep or cut? | Why?
  - Full name | {keep} | {to know who signed up}
  - Grade | {keep} | {to plan groups and rooms}
  - Home address | {cut } | {nothing is mailed}
  - Date of birth | {cut } | {grade is enough}
  - Guardian phone or email | {keep} | {to reach a family}
  - Social Security number | {cut } | {never needed; high risk}
  - Photo of the student | {cut } | {not needed to play}
  - Parents' jobs | {cut } | {nothing to do with chess}
  - Days you can come (Tue, Thu) | {keep} | {to plan meetings}
  - Chess level: new, some, or expert | {keep} | {to pair players fairly}
  - Password for your school account | {cut } | {never share a password}
  - Religion | {cut } | {unrelated and sensitive}

## Design the new form
write: Write the new sign-up form: list each field you kept and the exact question it asks.
  lines: 6
  key: Chess Club Sign-Up. 1. Your name. 2. Your grade. 3. A parent or guardian's phone number or email, so we can reach your family if a meeting changes. 4. Which days can you come? (Tuesday, Thursday). 5. Your chess level: new, some experience, or expert.
write: The club wants to serve snacks at meetings. What one question could it add, and why is that OK to ask?
  lines: 3
  key: "Do you have any food allergies we need to know about for club snacks?" It is OK because the club needs it for safety, it asks only about food, and it is used only for snacks.
write: How long should the club keep the forms, and what should happen to them after that?
  lines: 2
  key: Only while the student is in the club, usually until the end of the school year; then the paper forms are shredded and any digital copies are deleted.

# 29. Critique a Data Report
minutes: 35
materials: pencil, highlighter
ican: I can judge whether a report cleaned its data honestly and suggest better choices.
directions: The Student Data Team wrote a report on a cafeteria survey. Read how they cleaned the data. Use the 5-point checklist to judge their choices, citing the numbered step for each. Then suggest 2 better choices.
mistakes: Students judge the conclusion ("students love the cafeteria") instead of the cleaning steps. Others call every step bad; steps 4 and 5 are reasonable, and saying so is part of a fair critique. Watch for "remove the outliers" being treated as always correct: a rating of 1 on a 1 to 5 scale is a real opinion, not an error.
notes: The team and survey are made up. Count: 30 grade 6 forms removed, 8 blanks filled in, 3 ratings of 1 removed and 2 impossible ratings of 7 removed: 43 of 120 responses were removed or changed (35 removed, 8 changed). Checklist: 1 partly (counts given but not the number left, and weak reasons); 2 no (the 1s are real answers; removing the 7s is fine); 3 no (blanks filled with 4.5); 4 no (grade 6 dropped); 5 no (no limits; a sweeping conclusion). The reported average is pushed up by removing low ratings and filling blanks with a high number.

## The report
passage: Cafeteria Survey: Final Report | numbered
  We asked 120 students in grades 6, 7 and 8 to rate school lunch from 1 (poor) to 5 (great) and to name their favorite food. Our goal was to find out how students feel about school lunch so the cafeteria staff could plan next year's menu. Three team members typed the answers into a spreadsheet over two days. Before finding the results, we cleaned the data in five steps.
  Step 1: The 30 grade 6 forms were filled out on paper and were hard to read, so we removed all grade 6 forms.
  Step 2: Eight students left the rating blank. We filled in each blank with 4.5, the average of the other ratings, so we would not lose any students.
  Step 3: Three students rated lunch a 1. These ratings were much lower than everyone else's, so we removed them as outliers.
  Step 4: Students wrote favorite foods in different ways, such as "Pizza," "pizza" and "PIZZA." We combined spellings of the same food.
  Step 5: Two forms rated lunch a 7, which is not possible on a 1 to 5 scale. We removed these two ratings.
  Results: The average rating is 4.5 out of 5, and the favorite food is pizza. Students love the cafeteria, and no changes are needed. We will share these results with the principal and the cafeteria staff.

## Warm up
fill:
  - Responses removed: 30 + 3 + 2 = {35}. Responses changed (filled in): {8}.
  - In all, {43} of the 120 responses were removed or changed.

## Main: The 5-point checklist
chart: Met? (yes, partly or no) | Evidence: which step, and why
  labels: 1. Says what was changed, with counts and reasons; 2. Removes only impossible values or proven errors; 3. Does not make up data; 4. Keeps every group, or explains a missing one; 5. States the limits of the results
  height: 0.75
  key: 1. Partly: counts are given, but not how many responses were left, and "hard to read" is a weak reason to drop 30 forms (step 1). 2. No: step 3 removed real answers just because they were low; step 5 was correct, since 7 is impossible. 3. No: step 2 made up eight ratings of 4.5. 4. No: step 1 removed every grade 6 student. 5. No: the results claim all students love the cafeteria, with no mention of who was left out or what was changed.
write: Which steps did the team handle well? Explain.
  lines: 2
  key: Steps 4 and 5. Combining spellings of the same food fixes a typing difference without changing anyone's answer, and a 7 is impossible on a 1 to 5 scale, so removing it fixes a real error.

## Suggest 2 better choices
write: Better choice 1:
  lines: 3
  key: Instead of dropping grade 6, type in the paper forms carefully (asking a second person to check hard ones), or report grade 6 separately and say why if some cannot be read.
write: Better choice 2:
  lines: 3
  key: Keep the three ratings of 1, because they are real opinions, and leave blanks out of the average instead of filling them in, reporting "8 students did not give a rating." Then state the final number of ratings used and that the average is for those students only.

## Stretch
write: Rewrite the report's last sentence so it is honest about the data.
  lines: 3
  key: Example: Among the 77 real ratings we kept, all from grades 7 and 8, the average was about 4.5 out of 5, but we removed or changed 43 of 120 responses, including all of grade 6, so this does not show how all students feel.

# 40. Accessibility Bug Report
minutes: 40
materials: pencil
ican: I can write a clear bug report for an accessibility problem, with steps, impact and a fix.
directions: Your team is testing a school lunch-ordering app before it launches. Read the description of its order screen. Choose 3 accessibility problems and write a bug report for each one, like the example.
mistakes: Students write vague titles ("it's bad") and skip the steps, so a developer cannot see the bug. A good report lets someone who has never seen the bug make it happen. The impact line should name who is affected and how, not just "people can't use it." Fixes should be specific (add a text label, raise the contrast), not "make it accessible."
notes: The app is made up. Bugs on the screen: low-contrast instructions (light gray #AAAAAA on white is about 2.3 to 1; WCAG asks at least 4.5 to 1 for normal text); meal pictures with no names or alt text; a Student ID box with only placeholder text and no label; an error shown only by a red border; and an Order button that a keyboard cannot reach. The timeout is used in the example. The key models three; any three well-written reports are correct.

## The order screen
table: Part of the screen | What it looks like and does
  - Heading | "Order Lunch" in large black letters.
  - Instructions | "Pick your meal by 9:30 a.m." in light gray (#AAAAAA) on a white background.
  - Meal choices | Three pictures: a taco, a salad and a sandwich. No words. The pictures have no alt text.
  - Student ID box | An empty box with pale "Student ID" text inside that disappears when you start typing. No label outside the box.
  - Error message | If you forget to pick a meal and press Order, the meal area's border turns red. No words appear.
  - Order button | A small green check mark with no text. It works with a mouse click, but pressing Tab never reaches it.
  - Time limit | The screen logs you out after 60 seconds with no warning.

## Warm up: A model bug report
example: **Title:** Order screen logs users out after 60 seconds with no warning.
  **Steps to reproduce:** 1. Open the Order Lunch screen. 2. Wait 60 seconds without finishing the order.
  **What happens:** The app logs out and the order is lost. No warning or option to get more time appears.
  **Who it affects and how:** Users who read slowly, use a screen reader, type with a switch or need extra time cannot finish an order.
  **Suggested fix:** Warn the user before time runs out and let them ask for more time, or remove the limit.

## Main: Your 3 bug reports
chart: Bug report 1
  labels: Title; Steps to reproduce; What happens; Who it affects and how; Suggested fix
  key: Title: Instruction text is too low in contrast to read. Steps: 1. Open the order screen. 2. Read the line under the heading. What happens: light gray text on white is hard or impossible to read (about 2.3 to 1). Who: users with low vision, color blindness, or a screen in sunlight miss the 9:30 deadline. Fix: use dark text, at least 4.5 to 1 contrast.
chart: Bug report 2
  labels: Title; Steps to reproduce; What happens; Who it affects and how; Suggested fix
  key: Title: Order button cannot be reached with the keyboard. Steps: 1. Open the order screen. 2. Pick a meal and enter an ID. 3. Press Tab repeatedly. What happens: focus never lands on the check mark, so the order cannot be sent. Who: keyboard and screen reader users cannot order lunch at all. Fix: make it a real button that Tab reaches and Enter presses, with the visible text "Order."
chart: Bug report 3
  labels: Title; Steps to reproduce; What happens; Who it affects and how; Suggested fix
  key: Title: Error shown only by a red border. Steps: 1. Open the order screen. 2. Enter an ID but pick no meal. 3. Press Order. What happens: only the border turns red; no message appears. Who: color-blind users and screen reader users do not know what went wrong. Fix: show and announce a text message, "Please pick a meal," next to the meal choices. (Other good reports: meal pictures with no names or alt text; Student ID box with no label.)

## Stretch
write: Which of your 3 bugs should the team fix first? Explain using impact.
  lines: 3
  key: The keyboard bug, because it completely blocks some users from ordering lunch; the other bugs make ordering harder, but this one makes it impossible. Bugs that block a task usually come first.

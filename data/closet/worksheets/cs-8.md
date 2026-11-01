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

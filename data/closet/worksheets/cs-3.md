# 1. Paper Airplane Algorithm
minutes: 35
materials: pencil, two sheets of plain paper per student
ican: I can write clear, numbered steps that someone else can follow exactly.
directions: Write a 6-step algorithm for folding a paper airplane. Each step should be one clear action. Swap with a partner. Your partner folds a plane using only your steps and marks any step that is unclear.
mistakes: Students write steps that pack several actions together ("fold it into a plane") or skip a step they do without thinking (creasing, turning the paper over). The partner test finds these fast. Watch for partners who "help" by folding what they know instead of what the words say: they should follow the steps exactly, like a computer.
notes: Fold a plane yourself first so you can model one clear step aloud. The key shows one good 6-step algorithm (the classic dart); students' steps will differ, and any set a partner can follow exactly is correct. Words that make steps clearer: in half, the long way, corner, center line, crease, turn over, the same on the other side.

## Warm up: Clear or unclear?
example: Unclear: "Fold it." Clear: "Fold the paper in half the long way, crease it hard, then open it flat."
choice: Which step is the clearest?
  - Make the wings.
  - Fold the corners.
  * Fold the top two corners down so they meet at the center line.
  - Do the next part like before.
choice: Why does an algorithm need steps in the right order?
  - So it looks neat.
  * Because each step depends on what the steps before it did.
  - Because computers like numbers.

## Main: Write your algorithm
chart: Step | One clear action | Partner mark: clear or unclear?
  rows: 6
  key: A model: 1. Fold the paper in half the long way, crease it, and open it flat. 2. Fold the two top corners down so their edges meet at the center line. 3. Fold the new slanted edges in to the center line again, making a sharper point. 4. Fold the plane in half along the center line, with the folds on the outside. 5. Fold one side down to make a wing, lining its top edge up with the bottom of the body. 6. Turn the plane over and fold the other wing the same way so the wings match.

## Swap and test
write: Which of your steps did your partner mark unclear? What went wrong when they followed it?
  lines: 2
  key: Answers vary. A good answer names the step number and what the partner did differently, like "Step 2: they folded the corners the wrong way because I did not say down."
write: Rewrite that step so it is clear.
  lines: 2
  key: Answers vary. The new step names exactly which part of the paper moves, which way, and where it lines up.
write: Did your partner's plane fly? What does that tell you about your algorithm?
  lines: 2
  key: Answers vary. If the plane looks like the plan, the steps were clear enough to follow exactly; if not, a step was missing or could be read two ways.

## Stretch
write: A robot will fold your plane. Why does a robot need even clearer steps than a person?
  lines: 3
  key: A robot does exactly what the steps say and cannot guess what you meant or fill in a missing step, so every action, direction and place must be written down.

# 6. If-Else Fruit Sorter
minutes: 25
materials: pencil
ican: I can follow an if-else program to decide what happens.
directions: A sorting robot uses the program in the box to put fruit in baskets. Read each fruit card. Run the program in your head, one question at a time, and write the basket the fruit lands in. Then count each basket.
mistakes: Students skip the first question and sort by size alone, which sends the lemon to the Small basket. Remind them the robot always asks the yellow question first, and once a fruit is sorted it stops: it never reaches the second IF. Others answer from what they know about a fruit instead of what the card says (a card is the robot's only data).
notes: The program checks color first, so a yellow fruit goes to the Sun basket no matter its size. Baskets: Sun has the banana, lemon and yellow pear (3); Small has the strawberry, grape, blueberry, cherry and kiwi (5); Big has the watermelon, pineapple, apple and orange (4). In the stretch, asking about size first sends the lemon to Small; it is the only fruit that is both yellow and small, so it is the only one that moves.

## Warm up: One if-else
example: IF the fruit is red THEN put it in Basket A ELSE put it in Basket B. A red strawberry goes to Basket A. A green grape goes to Basket B.
fill:
  - A red cherry goes to Basket {A}.
  - A yellow banana goes to Basket {B}.
  - An orange orange goes to Basket {B}.

## Main: Run the sorting program
program: The robot's program
  | IF the fruit is yellow THEN
  |     put it in the Sun basket
  | ELSE
  |     IF the fruit is small THEN
  |         put it in the Small basket
  |     ELSE
  |         put it in the Big basket
table: Card | Fruit | Color | Size | Basket it lands in
  - 1 | banana | yellow | big | {Sun}
  - 2 | strawberry | red | small | {Small}
  - 3 | watermelon | green | big | {Big}
  - 4 | lemon | yellow | small | {Sun}
  - 5 | grape | green | small | {Small}
  - 6 | blueberry | blue | small | {Small}
  - 7 | pineapple | brown | big | {Big}
  - 8 | cherry | red | small | {Small}
  - 9 | apple | red | big | {Big}
  - 10 | orange | orange | big | {Big}
  - 11 | yellow pear | yellow | big | {Sun}
  - 12 | kiwi | brown | small | {Small}
fill:
  - The Sun basket has {3} fruits.
  - The Small basket has {5} fruits.
  - The Big basket has {4} fruits.
choice: Card 4 is a lemon. It is small. Why does it NOT land in the Small basket?
  - The robot forgot about it.
  * The robot asks "Is it yellow?" first, and the answer is yes, so it goes to Sun and stops.
  - Lemons are always big.
  - The ELSE part runs for every fruit.
choice: How many questions does the robot ask about the banana?
  * 1
  - 2
  - 3
  - 12
choice: How many questions does the robot ask about the grape?
  - 1
  * 2
  - 3
  - 0

## Stretch
text: A new robot asks about size first: IF the fruit is small THEN Small basket ELSE (IF the fruit is yellow THEN Sun basket ELSE Big basket).
fill:
  - The one fruit that changes baskets is the {lemon}. It moves to the {Small} basket.
write: Why did only one fruit move?
  lines: 2
  key: The lemon is the only fruit that is both yellow and small. Every other fruit gets the same answer either way, so the order of the questions only matters for the lemon.

# 17. Comment Cards
minutes: 30
materials: pencil
ican: I can write comments that tell a teammate what each part of a program does.
directions: A comment is a note for people, not for the computer. The computer skips it. Each program has numbered spots for comments. Read the code under each spot, then write a comment for it. Use the frame: This part ... so that ...
mistakes: Students copy the code into the comment ("set score to 0") instead of saying what it is for ("start the score at zero for a new game"). Ask: if your teammate could not read code, would your comment still help? Others write one comment for a whole program; each numbered spot needs its own.
notes: Comments in many languages start with a mark, like # in Python; here the numbered spots stand in for it. Model comments are in the key; any comment that says what the part does and why, in plain words, is right. A good test: cover the code and read only the comments; a teammate should still know what the program does.

## Warm up: A good comment
example: Code: "set score to 0". Weak comment: Set score to 0. Helpful comment: This part starts the score at zero so that every new game is fair.

## Main: Comment four programs
program: Program 1: Good morning robot
  | # Comment 1
  | set lights to on
  | say "Good morning!"
  | # Comment 2
  | repeat 3 times
  |     clap
chart: This part ... so that ...
  labels: Comment 1; Comment 2
  key: 1. This part turns on the lights and says good morning so that the day starts with a greeting. 2. This part claps 3 times so that the class knows it is time to begin.
program: Program 2: Draw a square
  | # Comment 1
  | pen down
  | # Comment 2
  | repeat 4 times
  |     move 10 steps
  |     turn right 90 degrees
  | # Comment 3
  | pen up
chart: This part ... so that ...
  labels: Comment 1; Comment 2; Comment 3
  key: 1. This part puts the pen down so that the robot draws when it moves. 2. This part draws 4 equal sides with square corners so that it makes a square. 3. This part lifts the pen so that the robot stops drawing.
program: Program 3: Rain helper
  | # Comment 1
  | ask "Is it raining?"
  | # Comment 2
  | if answer = "yes" then
  |     say "Take an umbrella."
  | else
  |     say "Have fun outside!"
chart: This part ... so that ...
  labels: Comment 1; Comment 2
  key: 1. This part asks about the weather so that the program knows if it is raining. 2. This part picks a message so that a person gets the right advice for rain or no rain.
program: Program 4: Cat game
  | # Comment 1
  | when green flag clicked
  |     set score to 0
  | # Comment 2
  | when the cat is clicked
  |     change score by 1
  |     play sound "meow"
chart: This part ... so that ...
  labels: Comment 1; Comment 2
  key: 1. This part starts the score at 0 when the game begins so that every game starts fair. 2. This part adds a point and plays a meow each time the cat is clicked so that the player sees and hears that they scored.

## Stretch
write: Your teammate says, "Comments are a waste of time. The code already works." Write what you would say back.
  lines: 2
  key: Comments help people, not the computer. A teammate (or you, later) can understand and change the code faster, find the right part to fix, and not break something by mistake.

# 23. Kid-Safe Search Words
minutes: 25
materials: pencil
ican: I can choose good search words and pick results that will help.
directions: For each question, circle the best search words. Then read the result titles and circle the one most likely to help. Skip any result that asks for personal information.
mistakes: Students often type the whole question with extra words ("my friend says spiders are scary"), or one word that is too broad ("spiders"). Good search words are the 2 to 5 key words. In the results part, students sometimes pick the most exciting title (a game or a contest) instead of the one that answers the question.
notes: The results are made up for practice; there are no real sites here. A useful rule for the stretch: never type your name, address, school or password to get something free, and tell a trusted adult when a page asks. Facts behind the questions: spiders have 8 legs; giant pandas eat mostly bamboo; the capital of Canada is Ottawa.

## Warm up
example: Question: How fast can a cheetah run? Best search words: **cheetah top speed**. Too broad: "cats". Too much: "I want to know how fast a cheetah can go when it runs."

## Main: Pick the search words
choice: How many legs does a spider have?
  - spiders
  * how many legs spider
  - my friend says spiders are scary
  - legs
choice: What do pandas eat?
  - animals
  - black and white bear cute
  * panda food diet
  - eat
choice: How tall is the tallest tree in the world?
  - trees
  - big
  - tree pictures
  * tallest tree in the world height
choice: How do I take care of a pet goldfish?
  * goldfish care for kids
  - fish
  - pets
  - goldfish funny videos
choice: What is the capital of Canada?
  - Canada
  * capital of Canada
  - cities
  - maple leaf
choice: Why do leaves change color in fall?
  - leaves
  - fall
  * why leaves change color in fall
  - pretty orange tree

## Main: Pick the result
choice: You searched **panda food diet**. Which result will help most?
  - Panda Plush Toys: Shop Now
  * Giant Pandas: What They Eat in the Wild (City Zoo Kids Page)
  - Pandas: Movie Times Near You
  - Win a Panda Prize! Type Your Name and Address
choice: You searched **goldfish care for kids**. Which result will help most?
  - Win a Free Goldfish! Enter Your Name and School
  - Funniest Fish Videos Ever
  * Goldfish Care Guide for Kids: Tank, Food and Cleaning
  - Fish Shaped Cookie Recipe
choice: You searched **how many legs spider**. Which result will help most?
  - Spider Costume Ideas
  - Download the Spider Game Free! Click Here
  - Scary Spider Movies
  * How Many Legs Do Spiders Have? Science for Kids

## Stretch
write: One result said "Win a Free Goldfish! Enter Your Name and School." Why should you skip it?
  lines: 2
  key: It asks for personal information (your name and school) that strangers should not get, and it does not answer the question. Skip it and tell a trusted adult.

# 28. Check the Tally Sheet
minutes: 30
materials: pencil
ican: I can check survey answers for problems and fix the totals.
directions: Mr. Ruiz's class asked, "What is your favorite recess game: tag, soccer, four square or jump rope?" 25 students answered. A helper made the tally sheet below. Check every answer on the list. Find 5 problems, then fix the totals.
mistakes: Students often find the blank and the double vote but miss the tally miscount, because they trust the tally instead of recounting from the list. Others count Sam's "soccer and tag" in both columns, which makes the totals add up to more than the number of students.
notes: Recounting from the list: tag 6 (Ana, Mia, Fay, Kim, Nia, Sue), soccer 5 (Ben, Eli, Jon, Oz, Tom), four square 5 (Cal, Gus, Lu, Pia, Vic), jump rope 5 (Dev, Ivy, Max, Rex, Uma). That is 21 answers that count; the 4 that do not count are Leo's blank, Sam's two answers, Kai's "swimming" and Mia's second vote. The helper's sheet counted Mia twice (tag 7), counted Sam as soccer (6) and made one extra jump rope mark (6). Students may reasonably say the class should ask Leo, Sam and Kai again; the key counts only answers that follow the survey's rules. Names are made up.

## Warm up
example: A tally mark is one line for each answer. Every fifth mark crosses the first four: ~~||||~~ is 5.
fill:
  - ~~||||~~ ||| is {8}.
  - ~~||||~~ ~~||||~~ | is {11}.

## The answers
table: # | Student | Answer | # | Student | Answer
  - 1 | Ana | tag | 14 | Lu | four square
  - 2 | Ben | soccer | 15 | Max | jump rope
  - 3 | Cal | four square | 16 | Nia | tag
  - 4 | Mia | tag | 17 | Oz | soccer
  - 5 | Dev | jump rope | 18 | Pia | four square
  - 6 | Eli | soccer | 19 | Mia | tag
  - 7 | Fay | tag | 20 | Rex | jump rope
  - 8 | Gus | four square | 21 | Sue | tag
  - 9 | Leo | (blank) | 22 | Kai | swimming
  - 10 | Ivy | jump rope | 23 | Tom | soccer
  - 11 | Jon | soccer | 24 | Uma | jump rope
  - 12 | Kim | tag | 25 | Vic | four square
  - 13 | Sam | soccer and tag | | |
table: Game (the helper's tally sheet) | Tally | Total
  - tag | ~~\|\|\|\|~~ \|\| | 7
  - soccer | ~~\|\|\|\|~~ \| | 6
  - four square | ~~\|\|\|\|~~ | 5
  - jump rope | ~~\|\|\|\|~~ \| | 6

## Main: Find 5 problems
chart: Answer number(s) | What is wrong
  labels: Problem 1; Problem 2; Problem 3; Problem 4; Problem 5
  key: 1. Answers 4 and 19: Mia voted twice; count her once. 2. Answer 9: Leo's answer is blank. 3. Answer 13: Sam picked two games. 4. Answer 22: Kai picked swimming, which is not a choice. 5. Jump rope: the tally has 6 marks but only 5 students (5, 10, 15, 20, 24) picked it.

## Fix the totals
table: Game | Helper's total | Correct total
  - tag | 7 | {6}
  - soccer | 6 | {5}
  - four square | 5 | {5}
  - jump rope | 6 | {5}
  - All answers that count | 24 | {21}
fill:
  - Answers that do not count: {4}. Check: 21 + 4 = {25} students.
  - The favorite recess game in this class is {tag}.

## Stretch
write: How could the class change the survey so these problems do not happen next time?
  lines: 3
  key: Let each student vote only once (check off names), give a checkbox for each game and say "pick one," make sure no one leaves it blank, and recount from the list instead of trusting one helper's tally.

# 39. Who Uses Computing? Job Cards
minutes: 25
materials: pencil
ican: I can tell how people in different jobs use computing tools.
directions: Read the four job cards. For each job, write the computing tool the worker uses and why it helps. Then answer the questions.
mistakes: Students list a tool that is not computing (a shovel, a wrench) or name the tool without the "why." Point them to the job card: each tool collects data, stores it, or does something a person would find slow or hard.
notes: The workers are made-up characters, but each tool is real and common. Tractors can steer along straight rows with GPS, and soil sensors measure how wet the ground is. Hospitals keep health records on computers, and heart monitors measure and show a heartbeat. Cars from the late 1990s on have a computer port a mechanic can plug a code reader into. Many artists draw on a tablet with a stylus in a drawing app.

## Read
passage: Four Job Cards
  **Farmer:** Rosa grows corn. Her tractor uses GPS to steer itself in straight rows, so no seeds are wasted. Small sensors in her fields measure how wet the soil is. When the soil is dry, the sensors send a message to her phone, so she waters only when the corn needs it.
  **Nurse:** Mr. Okafor is a nurse. He types each patient's medicine and temperature into the hospital computer. Then every doctor and nurse can see the same, up-to-date record. A heart monitor beside the bed counts the patient's heartbeats and beeps if something changes.
  **Mechanic:** Dee fixes cars. A car has small computers inside it. Dee plugs a code reader into a port under the dashboard. The reader shows a code that tells her which part is having trouble, so she knows where to look first.
  **Artist:** Sam draws pictures for children's books. He draws on a tablet with a special pen. The drawing app lets him undo a mistake, try new colors, and send the finished picture to the book maker the same day.

## Main: Tool and why
table: Job | Computing tool | Why it helps
  - Farmer | {GPS steering or soil sensors} | {straight rows with no wasted seed; water only when the soil is dry}
  - Nurse | {hospital computer records or heart monitor} | {everyone sees the same up-to-date record; the monitor counts heartbeats and warns}
  - Mechanic | {code reader} | {shows which part has trouble so she knows where to look first}
  - Artist | {drawing tablet and app} | {undo mistakes, try colors, send the picture the same day}
choice: Which worker uses a tool that sends a message to a phone?
  * Rosa, the farmer
  - Mr. Okafor, the nurse
  - Dee, the mechanic
  - Sam, the artist
choice: Why is it helpful that every nurse and doctor sees the same record?
  - The computer can give the medicine.
  - It makes the hospital quieter.
  * Everyone knows what medicine and care the patient already had.
  - Nurses do not need to learn anything.
choice: What does Dee plug her code reader into?
  - The car's radio
  * A port under the dashboard
  - The gas tank
  - Her phone

## Stretch
write: Pick a job that is not on a card, like a bus driver or a librarian. What computing tool might that worker use, and why?
  lines: 3
  key: Example: A librarian uses a computer catalog and a scanner to check books in and out, so they can tell right away which books are on the shelf and who has the others.

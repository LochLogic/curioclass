# 1. Flowchart a Snack Machine
minutes: 35
materials: pencil, ruler
ican: I can use a flowchart with a loop and a decision to plan a program.
directions: A snack costs 75 cents. Fill in the missing parts of the flowchart table. Then trace three customers through it, and draw the whole flowchart with shapes and arrows.
mistakes: Students often send the "No" arrow from the money check to the end instead of back to "Put in a coin," so the machine gives up after one coin. Ask: "What should the machine do if you have not paid enough yet?" When tracing, some count the coins but forget to check the total after each one.
notes: Shapes used here: oval for start and end, rectangle for a step, diamond for a yes or no question. Box 3 to box 5 and back is the loop. Accept any clear wording for the missing step text (box 3 could be "Insert a coin"; box 6 could be "Give the snack"). Leo's change: 100 - 75 = 25 cents. Ana: 10, 35, 60, 85 cents after each coin, so 4 coins and 10 cents change.

## Warm up: Shapes
example: Oval = start or end. Rectangle = a step to do. Diamond = a yes or no question, with a Yes arrow and a No arrow.
fill:
  - Shape for "Is the total 75 cents or more?": {diamond  }
  - Shape for "Drop the snack": {rectangle}
  - Shape for "Start": {oval     }

## Main: Finish the flowchart
table: Box | Shape | Words inside | Arrow goes to
  - 1 | oval | Start | box {2}
  - 2 | rectangle | Choose a snack (75 cents) | box 3
  - 3 | rectangle | {Put in a coin} | box 4
  - 4 | rectangle | Add the coin to the total | box {5}
  - 5 | {diamond  } | Is the total 75 cents or more? | Yes: box {6}. No: box {3}
  - 6 | rectangle | {Drop the snack} | box 7
  - 7 | diamond | Is the total more than 75 cents? | Yes: box 8. No: box {9}
  - 8 | rectangle | Give back the change | box 9
  - 9 | {oval     } | {End} | (none)
fill:
  - Maya pays with quarters (25 cents each). She puts in {3} coins, and the No arrow sends her back {2} times.
  - Leo puts in one dollar coin (100 cents). After box 5 he goes to box {6}, and he gets {25} cents in change.
  - Ana puts in a dime (10 cents), then quarters. She puts in {4} coins in all and gets {10} cents in change.
draw: Draw the whole flowchart. Use the right shapes and label every arrow from a diamond Yes or No. | 4

## Stretch
write: The machine runs out of a snack. Where would you add a new diamond, and what would it ask? Where do its Yes and No arrows go?
  lines: 3
  key: After box 2 (choose a snack), before any coins go in: "Is this snack in stock?" Yes goes on to box 3. No shows "Sold out" and goes back to box 2 to choose again.

# 6. Trace-and-Decode Riddle
minutes: 30
materials: pencil
ican: I can trace a program and keep track of how its variables change.
directions: Trace each program one line at a time and keep track of every variable. Write the number the program prints. Find that number in the decoder and write its letter in the box with the same number. The letters answer the riddle.
mistakes: Students read a variable's first value and forget it changed: in Program 3, b uses the new value of a (6), not 10. In loops, students often add or double one time too few or too many; have them write the value after each time through the loop. In Program 5, only one branch of the if-else runs.
notes: Traces: Program 1: x is 5, then 8, then 16. Program 2: total is 5, 10, 15, 20. Program 3: a becomes 10 - 4 = 6, then b becomes 6 + 4 = 10. Program 4: n is 2, 4, 8. Program 5: 7 > 5 is true, so score becomes 17 and the else line never runs. Program 6: count is 26, 22, 18. The decoys catch common slips: 15 (one time too few through Program 2's loop), 6 (printing a in Program 3), 4 (one doubling too few in Program 4), 5 (running Program 5's else line) and 22 (one subtraction too few in Program 6). The riddle answer is A SHIRT.

## Warm up: Trace one together
example: x = 2, then x = x + 3, then print(x). After line 1, x is 2. Line 2 uses the old x: 2 + 3 = 5, so x is now 5. The program prints 5.
fill:
  - y = 4, then y = y * 3, then y = y - 2, then print(y). The program prints {10}.

## Main: Six programs
text: **Riddle: What has a neck but no head, and two arms but no hands?**
program: Program 1
  | x = 5
  | x = x + 3
  | x = x * 2
  | print(x)
program: Program 2
  | total = 0
  | repeat 4 times:
  |     total = total + 5
  | print(total)
program: Program 3
  | a = 10
  | b = 4
  | a = a - b
  | b = a + b
  | print(b)
program: Program 4
  | n = 1
  | repeat 3 times:
  |     n = n * 2
  | print(n)
program: Program 5
  | score = 7
  | if score > 5:
  |     score = score + 10
  | else:
  |     score = score - 2
  | print(score)
program: Program 6
  | count = 30
  | repeat 3 times:
  |     count = count - 4
  | print(count)
code: Write what each program prints, then decode.
  - Program 1 output | 16 | A
  - Program 2 output | 20 | S
  - Program 3 output | 10 | H
  - Program 4 output | 8 | I
  - Program 5 output | 17 | R
  - Program 6 output | 18 | T
  decoys: 4 5 6 15 22

## Stretch
write: Write a short program of your own that prints 24. Use a variable that changes at least twice.
  lines: 4
  key: Example: n = 3, then n = n * 2 (6), then n = n * 4 (24), then print(n). Any program works if tracing it ends at 24 and the variable changes at least twice.

# 18. Sort the Book Table
minutes: 35
materials: pencil
ican: I can sort a table of data and choose the sort that answers a question.
directions: The class library has 15 books. Sort the table two ways: by pages, from fewest to most, and by title, from A to Z. Cross off each book as you place it so you do not skip one. Then decide which sort helps answer each question.
mistakes: When two titles start with the same letter (Farm Year and Fossil Hunters), students stop at the first letter; look at the second letter to break the tie. When sorting by pages, students sometimes compare only the first digit, so 120 lands before 24. Cross-checking: both sorted lists must have all 15 books.
notes: The titles are made up. Sorted by pages: Messy Max 24, Zebra Stripes 32, Kites and Clouds 40, Lost Kite 48, Night Owls 56, Baking with Grandpa 64, Volcano Day 72, Jungle Map 80, Farm Year 88, Rocket to Mars 96, Under the Ice 104, Desert Rain 112, Ocean Giants 120, Penny's Garden 136, Fossil Hunters 144. Sorting by pages answers "how long" questions (shortest, longest, under 50 pages); sorting by title answers "find a book" questions (is it here, what comes next on the shelf). In the stretch, a tie needs a second rule, such as by title.

## The books
table: Title | Pages | Title | Pages
  - Rocket to Mars | 96 | Volcano Day | 72
  - Lost Kite | 48 | Kites and Clouds | 40
  - Ocean Giants | 120 | Messy Max | 24
  - Baking with Grandpa | 64 | Under the Ice | 104
  - Zebra Stripes | 32 | Jungle Map | 80
  - Fossil Hunters | 144 | Penny's Garden | 136
  - Night Owls | 56 | Desert Rain | 112
  - Farm Year | 88 | |

## Warm up
fill:
  - Which comes first, A to Z: Farm Year or Fossil Hunters? {Farm Year}
  - Which comes first, fewest pages to most: 120 or 24? {24}

## Main: Sort two ways
table: Order | Sorted by pages (fewest first) | Pages | Sorted by title (A to Z) | Pages
  - 1 | {Messy Max} | {24} | {Baking with Grandpa} | {64}
  - 2 | {Zebra Stripes} | {32} | {Desert Rain} | {112}
  - 3 | {Kites and Clouds} | {40} | {Farm Year} | {88}
  - 4 | {Lost Kite} | {48} | {Fossil Hunters} | {144}
  - 5 | {Night Owls} | {56} | {Jungle Map} | {80}
  - 6 | {Baking with Grandpa} | {64} | {Kites and Clouds} | {40}
  - 7 | {Volcano Day} | {72} | {Lost Kite} | {48}
  - 8 | {Jungle Map} | {80} | {Messy Max} | {24}
  - 9 | {Farm Year} | {88} | {Night Owls} | {56}
  - 10 | {Rocket to Mars} | {96} | {Ocean Giants} | {120}
  - 11 | {Under the Ice} | {104} | {Penny's Garden} | {136}
  - 12 | {Desert Rain} | {112} | {Rocket to Mars} | {96}
  - 13 | {Ocean Giants} | {120} | {Under the Ice} | {104}
  - 14 | {Penny's Garden} | {136} | {Volcano Day} | {72}
  - 15 | {Fossil Hunters} | {144} | {Zebra Stripes} | {32}

## Which sort answers the question?
table: Question | Best sort: pages or title? | Answer
  - What is the shortest book? | {pages} | {Messy Max}
  - Is Night Owls in the library? | {title} | {yes}
  - Which books have fewer than 50 pages? | {pages} | {Messy Max, Zebra Stripes, Kites and Clouds, Lost Kite}
  - Which book comes right after Jungle Map on the shelf? | {title} | {Kites and Clouds}
  - What is the longest book? | {pages} | {Fossil Hunters}

## Stretch
write: A new book, Moon Garden, also has 64 pages, the same as Baking with Grandpa. In the pages sort, which goes first? Write a rule that settles every tie.
  lines: 3
  key: Use a second rule: when two books have the same number of pages, put them in title order. Baking with Grandpa (B) comes before Moon Garden (M).

# 24. Outlier Hunt: Plant Growth
minutes: 30
materials: pencil
ican: I can find outliers in data and decide whether to keep them or measure again.
directions: A class grew 11 bean plants and measured them after two weeks. Find the values that are far from the rest. Use the notes to decide: keep the value, or redo the measurement?
mistakes: Students often want to throw out every outlier. Plant 8 is the one to talk about: it was measured carefully twice, so it is real data, and it tells us something (more sunlight). Others miss that plant 4 is a units mistake: 85 millimeters is 8.5 centimeters.
notes: The rule of thumb: if the measurement was done wrong, redo it; if the measurement is right and the plant really grew that way, keep it and explain why. Heights as written, in order: 3, 7, 8, 8, 8, 9, 9, 9, 10, 15, 85; the middle (6th) value is 9. After the redo (plant 4 is 8 cm, plant 10 is 9 cm): 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 15; the middle value is still 9, but the range drops from 82 to 8. That shows the middle value is not pulled by outliers, but the range is.

## Read the data
table: Plant | Height (cm) | Notes from the measurer
  - 1 | 8 |
  - 2 | 9 |
  - 3 | 7 |
  - 4 | 85 | I read the millimeter side of the ruler.
  - 5 | 8 |
  - 6 | 10 |
  - 7 | 9 |
  - 8 | 15 | Measured twice by two people: 15 cm both times. This pot sat closest to the sunny window.
  - 9 | 8 |
  - 10 | 3 | The stem was bent over when I measured it.
  - 11 | 9 |

## Find the outliers
fill:
  - Most plants grew between {7} and {10} cm.
  - The three outliers are plants {4}, {8} and {10}.
  - With the heights as written, the range (biggest minus smallest) is {82} cm.
  - Put the 11 heights in order. The middle value is {9} cm.

## Decide
table: Plant | Keep or redo? | Why?
  - 4 | {redo} | {mm, not cm: about 8.5 cm}
  - 8 | {keep} | {checked twice; real, more sun}
  - 10 | {redo} | {bent stem: straighten it}
fill:
  - The redo finds plant 4 is 8 cm and plant 10 is 9 cm. Now the range is {8} cm.
  - After the redo, the middle value is {9} cm.

## Stretch
write: Why is it a bad idea to erase every outlier? Use plant 8 in your answer.
  lines: 3
  key: Some outliers are real. Plant 8 was measured carefully twice and grew more because it got more sunlight; erasing it would hide a real result and a clue about what helps beans grow.

# 29. Fix the Lemon and Lime Model
minutes: 30
materials: pencil
ican: I can plan training data that helps a model learn the difference between two things.
directions: A class trained a model to tell lemons from limes. It keeps getting them mixed up. Study the training photos it learned from and the mistakes it made. Then plan 10 new training photos that would fix it.
mistakes: Students add 10 more photos just like the old ones (bright yellow lemons, green limes), which teaches the model nothing new. The fix is variety: green lemons, yellow limes, cut fruit, other lighting and backgrounds. Others plan photos with no label; every training photo needs the right label.
notes: Real facts behind the sheet: lemons are green before they ripen, and limes turn yellow when they get very ripe, so color alone cannot tell them apart. Lemons are usually larger and oval with a small bump at one end; limes are usually smaller and rounder. The model learned "yellow = lemon, green = lime" (and "white plate = lemon") because every training photo fit that pattern. The set starts lopsided (16 lemons, 4 limes), so a good plan adds more limes than lemons; removing a few of the look-alike lemon photos would also help. Keeping some new photos out of training lets the class test the model fairly.

## The model's training photos
table: Training photos | How many | What they all look like
  - Labeled lemon | 16 | Bright yellow, whole, on a white plate, in sunlight
  - Labeled lime | 4 | Dark green, whole, on a wooden board
table: Test photo | What the model said | Right answer
  - A green lemon that is not ripe yet | lime | lemon
  - A very ripe lime that has turned yellow | lemon | lime
  - A green lime on a white plate | lemon | lime
  - A lemon cut in half on a wooden board | lime | lemon

## Warm up: What went wrong?
choice: What did the model most likely learn?
  - Lemons are bigger than limes.
  * Yellow or a white plate means lemon; green or a wooden board means lime.
  - Lemons have seeds and limes do not.
  - Cut fruit is always a lime.
choice: What else is wrong with the training set?
  - It has too many limes.
  - Every photo is labeled wrong.
  * It has 16 lemons but only 4 limes, so it is lopsided.
  - The photos are too clear.

## Main: Plan 10 new training photos
chart: Describe the photo (color, whole or cut, background, light) | Label | What it teaches the model
  labels: 1; 2; 3; 4; 5; 6; 7; 8; 9; 10
  key: A strong plan (3 lemons, 7 limes): 1. Green unripe lemon, whole, white plate (lemon): green can be a lemon. 2. Lemon on a wooden board, indoor light (lemon): the board does not decide. 3. Lemon cut in half, shade (lemon). 4. Yellow ripe lime, whole, white plate (lime): yellow can be a lime. 5. Yellow-green lime on a wooden board (lime). 6. Green lime on a white plate in sunlight (lime). 7. Lime cut in half on a white plate (lime). 8. Lime in a bowl with other fruit (lime). 9. Lime held in a hand, close-up of its round shape (lime). 10. Small dark green lime in a shady kitchen (lime). Every photo is labeled, and color, background, light and whole or cut are mixed for both fruits.
fill:
  - If all 10 new photos were limes, the set would have {16} lemons and {14} limes.
  - If I plan 3 lemons and 7 limes, the set has {19} lemons and {11} limes.

## Stretch
write: Your teacher says, "Keep 4 of the new photos out of training and use them only for testing." Why is that a good idea?
  lines: 3
  key: If the model is tested on photos it trained on, it can look right just by remembering them. New photos it has never seen show whether it really learned to tell lemons from limes.

# 41. Computing on the Farm and in the Kitchen
minutes: 25
materials: pencil, highlighter
ican: I can explain how workers use sensors and spreadsheets to do their jobs.
directions: Read about a chef and a farmer. Highlight each computing tool. Then list each tool, the task it helps with, and who uses it.
mistakes: Students list the food or the crop instead of the tool, or the tool without the task. A sensor measures something (temperature, wetness) by itself; a spreadsheet is a table on a computer that can add and sort. Some students say the sensor "decides" what to do; here the people still decide, using the data.
notes: The chef and farmer are made-up characters, but the tools are common. US food safety guidance says to keep a refrigerator at 40 degrees Fahrenheit or colder. Soil moisture sensors and weather stations are widely used on farms, and both small restaurants and farms use spreadsheets for orders, costs and harvest records. Tool and task pairs in the key are the clearest ones; accept any tool and task that matches the passage.

## Read
passage: Two Workers, Lots of Data
  Chef Lina runs a small restaurant. A sensor inside her big refrigerator checks the temperature all night. If it gets warmer than 40 degrees Fahrenheit, the sensor sends an alert to her phone, so food does not spoil. Each Friday she opens a spreadsheet that lists every ingredient and how much she used. The spreadsheet adds up each column, so she knows how many onions and eggs to order. A probe thermometer tells her when the chicken is cooked all the way through.
  Lina buys vegetables from Farmer Joe. Joe has moisture sensors buried in his fields. Each morning he checks a map on his computer that shows which rows are dry, and he waters only those rows. A small weather station on his barn records rain and wind. Joe types every harvest into a spreadsheet: the date, the crop and the number of pounds. When he sorts it by crop, he can see which vegetables grew best this year and plan what to plant next spring.

## Main: Tools and tasks
table: Who uses it | Computing tool | Task it helps with
  - Chef Lina | {temperature sensor in the refrigerator} | {sends an alert if the fridge gets too warm, so food does not spoil}
  - Chef Lina | {spreadsheet of ingredients} | {adds up what she used so she knows what to order}
  - Chef Lina | {probe thermometer} | {tells her when the chicken is cooked through}
  - Farmer Joe | {soil moisture sensors and a map on his computer} | {shows which rows are dry so he waters only those}
  - Farmer Joe | {weather station} | {records rain and wind}
  - Farmer Joe | {harvest spreadsheet} | {sorts harvests by crop to plan next spring}
choice: Why does the refrigerator sensor send an alert to Lina's phone?
  - So she can count the eggs
  * So she can act before food spoils, even at night
  - So the fridge can order more food
  - So Joe knows what to plant
choice: What does Joe do with his harvest spreadsheet to see which vegetables grew best?
  - He adds a column of rain.
  - He deletes the dates.
  - He sends it to the weather station.
  * He sorts it by crop.

## Stretch
write: Lina and Joe both use a spreadsheet. How are their spreadsheets alike, and how are they different?
  lines: 3
  key: Alike: both keep data in rows and columns and help plan ahead (what to order, what to plant). Different: Lina's tracks ingredients she used each week and adds them up; Joe's tracks harvests by date and crop, and he sorts it.

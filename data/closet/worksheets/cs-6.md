# 1. Flowchart Symbols Field Guide
minutes: 35
materials: pencil, ruler
ican: I can use standard flowchart symbols to plan an algorithm.
directions: Match each flowchart symbol to its job, then name and sketch each shape. Use the symbols to chart how a crosswalk signal works, and check your chart by tracing it.
mistakes: Students often put a question in a rectangle, or give a diamond only one arrow out. Every decision needs at least two labeled exits (Yes and No). Others draw the parallelogram for every step; it is only for data coming in or going out (reading the button, showing a message).
notes: The five symbols here are the ones most courses teach: terminal (oval or rounded rectangle), process (rectangle), decision (diamond), input/output (parallelogram), and the flowline (arrow). Some guides add a small circle connector. For the crosswalk, showing WALK on the sign can be drawn as output (parallelogram) or as a process (rectangle); accept either if the student can explain it. Real signals vary; the key shows one sensible version.

## Warm up: Match the symbol to its job
match: Write the letter of each job next to its symbol.
  - Oval (terminal) = Marks where the algorithm starts or stops
  - Rectangle (process) = One action or calculation, like "add 1 to count"
  - Diamond (decision) = A yes or no question with a branch for each answer
  - Parallelogram (input/output) = Data comes in or goes out, like reading a button
  - Arrow (flowline) = Shows which step comes next

## Main: Your field guide
table: Symbol | Shape name | Sketch it
  - Terminal | {oval         } |
  - Process | {rectangle    } |
  - Decision | {diamond      } |
  - Input/output | {parallelogram} |
  - Flowline | {arrow        } |

## Main: Chart a crosswalk signal
text: **How the signal works.** The signal shows DON'T WALK. It keeps checking whether someone has pressed the button. When the button is pressed, it waits until the traffic light turns red. Then it shows WALK for 20 seconds, flashes DON'T WALK with a countdown for 15 seconds, and goes back to showing DON'T WALK and checking the button.
fill:
  - "Is the button pressed?" uses the {decision} symbol.
  - "Read the button" uses the {input/output} symbol.
  - "Wait 20 seconds" uses the {process} symbol.
  - The flowchart begins with a {terminal} symbol.
draw: Draw the crosswalk flowchart. Label both arrows out of each decision. | 3.6
write: Trace your flowchart for a day when no one presses the button. What happens?
  lines: 2
  key: The No arrow from "Is the button pressed?" loops back to reading the button, so the signal keeps showing DON'T WALK and checking forever; it never shows WALK.
write: Write your flowchart as numbered pseudocode steps.
  lines: 5
  key: 1 START. 2 SHOW DON'T WALK. 3 READ the button. 4 IF the button is not pressed, go back to step 3. 5 WAIT until the traffic light is red (a decision loop: Is the light red? No: wait and check again). 6 SHOW WALK. 7 WAIT 20 seconds. 8 FLASH DON'T WALK with a countdown for 15 seconds. 9 Go back to step 2. (The signal runs all day, so it may never reach an END.)

## Stretch
write: Why does a diamond always need at least two arrows leaving it, but a rectangle needs only one?
  lines: 3
  key: A decision asks a question with more than one possible answer, and each answer leads somewhere different, so each needs its own labeled arrow. A process just does one thing and then always goes to the same next step.

# 6. Name It Well
minutes: 30
materials: pencil
ican: I can give variables clear names that say what they hold.
directions: This program plans a class field trip, but its variable names hide what each one means. Trace it first to see what each variable holds. Then give each of the 8 variables a better name and explain your choice. ceil() rounds a number up to the next whole number.
mistakes: Students trade one vague name for another (x becomes number, data becomes info). A good name says what the value is and, when it matters, its unit or kind: ticket_price, not price2. Names that are very long or hard to type (the_total_amount_of_money_for_all_the_tickets) are also a problem. Watch for students who give two variables the same name.
notes: Traces: x = 28 students, thing2 = 4 adults, p = 12 dollars per ticket, a = 32 people, data = 32 x 12 = 384 dollars, n = 30 seats per bus, temp = ceil(32 / 30) = 2 buses, flag = 384 > 400, which is False. The program prints 384 2 False. Names in the key use the Python style (lowercase with underscores); camelCase like ticketPrice is also fine if students use one style throughout. A true or false variable reads best as a yes or no question (over_budget, is_full).

## Warm up
choice: A variable holds how many pets a student has. Which name is best?
  - n
  - thing
  * pet_count
  - the_number_of_pets_that_this_student_has_at_home
choice: What is the main problem with the name temp?
  - It is too long.
  * It could mean temperature or temporary, so it does not say what it holds.
  - It has a number in it.
  - Computers cannot read it.

## Main: Trace, then rename
program: Field trip planner
  | x = 28
  | thing2 = 4
  | p = 12
  | a = x + thing2
  | data = a * p
  | n = 30
  | temp = ceil(a / n)
  | flag = data > 400
  | print(data, temp, flag)
fill:
  - a is {32}, data is {384} and temp is {2}.
  - flag is {False}, so the program prints {384 2 False}.
table: Old name | What it holds | Better name | Why the new name is better
  - x | {the number of students (28)} | {num_students} | {says what is being counted}
  - thing2 | {the number of adult helpers (4)} | {num_chaperones} | {thing2 says nothing; this names who it counts}
  - p | {the price of one ticket, in dollars} | {ticket_price} | {p could be people or points}
  - a | {everyone going: students plus adults} | {total_people} | {shows it is the sum of everyone}
  - data | {the cost of all the tickets} | {total_cost} | {every variable holds data; this says which}
  - n | {how many seats one bus has} | {seats_per_bus} | {says what the 30 means}
  - temp | {how many buses to rent} | {buses_needed} | {temp sounds like temperature}
  - flag | {whether the cost is more than 400 dollars} | {over_budget} | {reads like a yes or no question}

## Stretch
write: Rewrite lines 5 and 7 using your new names. Does the program run any differently? Why do names still matter?
  lines: 3
  key: total_cost = total_people * ticket_price and buses_needed = ceil(total_people / seats_per_bus). It runs exactly the same, because the computer does not care about names; people do. Clear names make the code easier to read, check and fix.

# 18. Two Ranking Rules
minutes: 35
materials: pencil, calculator (optional)
ican: I can show how the weights in a scoring rule change who wins.
directions: Judges gave 8 science fair projects two scores out of 10: Science (a careful method and good data) and Creativity (a new idea). Score every project with both rules. Then rank the projects and explain why the winner changes.
mistakes: Students multiply the wrong score by 2, or rank from lowest to highest. Have them check one row aloud: Rule A doubles Science, Rule B doubles Creativity. Some say one rule is "right." Both are reasonable; the point is that the people who choose the weights shape the result, so the weights should be chosen and shared before judging.
notes: Rule A totals: Plant Music 22, Bridge Strength 23, Fruit Battery 21, Paper Towel Test 20, Bird Feeder Camera 19, Water Filter 26, Mold on Bread 18, Solar Oven 24. Rule B totals: 26, 19, 21, 16, 23, 22, 15, 24. Rule A ranks Water Filter, Solar Oven, Bridge Strength, Plant Music, Fruit Battery, Paper Towel Test, Bird Feeder Camera, Mold on Bread. Rule B ranks Plant Music, Solar Oven, Bird Feeder Camera, Water Filter, Fruit Battery, Bridge Strength, Paper Towel Test, Mold on Bread. Solar Oven is second under both rules because its scores are balanced (8 and 8). With equal weights, Plant Music, Water Filter and Solar Oven tie at 16.

## Warm up
example: Rule A = 2 x Science + Creativity. A project with Science 5 and Creativity 9 scores 2 x 5 + 9 = 19.
fill:
  - Under Rule B = Science + 2 x Creativity, the same project scores {23}.

## Main: Score and rank
table: Project | Science | Creativity | Rule A: 2 x Science + Creativity | Rule B: Science + 2 x Creativity
  - Plant Music | 6 | 10 | {22} | {26}
  - Bridge Strength | 9 | 5 | {23} | {19}
  - Fruit Battery | 7 | 7 | {21} | {21}
  - Paper Towel Test | 8 | 4 | {20} | {16}
  - Bird Feeder Camera | 5 | 9 | {19} | {23}
  - Water Filter | 10 | 6 | {26} | {22}
  - Mold on Bread | 7 | 4 | {18} | {15}
  - Solar Oven | 8 | 8 | {24} | {24}
table: Place | Rule A ranking | Rule B ranking
  - 1st | {Water Filter} | {Plant Music}
  - 2nd | {Solar Oven} | {Solar Oven}
  - 3rd | {Bridge Strength} | {Bird Feeder Camera}
  - 4th | {Plant Music} | {Water Filter}
  - 5th | {Fruit Battery} | {Fruit Battery}
  - 6th | {Paper Towel Test} | {Bridge Strength}
  - 7th | {Bird Feeder Camera} | {Paper Towel Test}
  - 8th | {Mold on Bread} | {Mold on Bread}

## Explain
write: Why does the winner change from Rule A to Rule B?
  lines: 3
  key: Water Filter has the top Science score (10) but lower Creativity (6), so it wins when Science counts double. Plant Music has the top Creativity score (10) but lower Science (6), so it wins when Creativity counts double. The weights decide which strength matters most.
write: Why does Solar Oven come in 2nd under both rules?
  lines: 2
  key: Its two scores are equal (8 and 8), so doubling either one gives the same total, 24. A balanced project is not helped or hurt by the choice of weights.
write: Which rule would you choose for a science fair, and why? When should the judges choose the rule?
  lines: 3
  key: Answers vary. Example: Rule A, because a science fair should reward a careful method and real data most. The judges should choose and share the rule before they see the projects, so they cannot pick weights to help a favorite.

## Stretch
fill:
  - With equal weights (Science + Creativity), {3} projects tie for first, each with {16} points.
write: Name the tied projects. Suggest a fair way to break the tie that is decided before judging.
  lines: 2
  key: Plant Music, Water Filter and Solar Oven. Example: a tie goes to the higher Science score (Water Filter), or the judges give a third score set ahead of time, such as how clearly the project is explained.

# 24. Photo Metadata Detective
minutes: 30
materials: pencil, highlighter
ican: I can explain what the metadata in a file reveals about a person.
directions: Jordan, a made-up student, posted three photos online. Read the metadata stored inside each photo file and the caption Jordan posted with it. List what each one reveals about Jordan, then decide what Jordan should change before sharing.
mistakes: Students focus on what is in the picture and skip the metadata rows. The point is that the file tells more than the picture does: a photo of a sunrise can still reveal a name, a place and a routine. Watch for students who think deleting a post deletes every copy; others may already have saved it.
notes: Jordan and Riverton are made up; no real person or address. Metadata is data about data; photo files often store EXIF data such as the date and time, camera or phone model and settings, and GPS coordinates when location is on. Many sites strip some of it on upload, but not all do, and files sent directly (by message or email) often keep it. The pattern question is the heart of the sheet: one photo reveals a little, three together reveal a routine. The dates are real 2026 calendar days (May 9 is a Saturday; June 3 a Wednesday; June 9 a Tuesday).

## Read the metadata
table: Photo A: sunrise.jpg | Metadata
  - Date taken | Saturday, May 9, 2026, 6:10 AM
  - Device name | Jordan's Phone
  - Location (GPS) | On. Map pin: Maple Street Dog Park, Riverton
  - Caption Jordan posted | Sunrise walk with Biscuit, like every Saturday!
table: Photo B: cake.jpg | Metadata
  - Date taken | Wednesday, June 3, 2026, 4:30 PM
  - Device name | Lee Family Tablet
  - Location (GPS) | On. Map pin: 18 Willow Lane, Riverton
  - Caption Jordan posted | Turning 12 today!
table: Photo C: team.jpg | Metadata
  - Date taken | Tuesday, June 9, 2026, 3:45 PM
  - Device name | Jordan's Phone
  - Location (GPS) | On. Map pin: Riverton Middle School, back field
  - Caption Jordan posted | Practice every Tuesday and Thursday after school

## What does each photo reveal?
write: Photo A reveals:
  lines: 2
  key: Jordan's first name (from the device name), that Jordan has a dog named Biscuit, and that Jordan is at Maple Street Dog Park early every Saturday morning.
write: Photo B reveals:
  lines: 2
  key: A home address (18 Willow Lane, Riverton), a family name (Lee), and Jordan's birthday (June 3) and age (12).
write: Photo C reveals:
  lines: 2
  key: Jordan's school and that Jordan is on its back field every Tuesday and Thursday after school.
fill:
  - The photo that gives away a home address is Photo {B}.
  - Two photos were taken on the same device: Photos {A} and {C}.
  - Photo C was taken on a {Tuesday}.
choice: Which piece of metadata is the most risky to share publicly?
  - The time of day
  * The GPS location
  - The file name
  - The size of the photo

## Put it together
write: A stranger sees all three posts. What could the stranger figure out by putting them together?
  lines: 3
  key: Jordan's full name (Jordan Lee), age and birthday, home address, school, and a schedule: where Jordan will be on Saturday mornings and on Tuesday and Thursday afternoons. Together that is enough to find Jordan in person.
write: Name two things Jordan could do before posting photos.
  lines: 2
  key: Turn off location tagging in the camera settings; remove metadata before sharing; change the device name; leave out captions that give routines or birthdays; post later instead of in real time; share only with people Jordan knows.

# 29. Before and After Cleaning
minutes: 35
materials: pencil, ruler
ican: I can show how cleaning data changes what a graph shows, and explain each change honestly.
directions: A sensor on the school roof recorded the temperature at lunchtime for 10 school days. The raw data has problems. Graph the raw data, clean it using the notes, graph the cleaned data, and describe how the picture changed.
mistakes: Students fill the missing day with a guess (like 20) without saying so; on this sheet it stays blank and is reported as missing. Others "fix" 73 by deleting it, but the note says it is a real reading in Fahrenheit, so it should be converted, not thrown away. On the cleaned graph, students should skip day 3, not plot it at 0.
notes: Raw: 18, 19, 0, 20, 22, 73, 22, 24, 2.5, 24. Cleaning: day 3 was offline and stored as 0, so it becomes missing; day 6 was recorded in Fahrenheit, and (73 - 32) x 5 / 9 is about 22.8, which rounds to 23 degrees Celsius; day 9 was a typing slip, and the paper log says 25. Cleaned: 18, 19, (missing), 20, 22, 23, 22, 24, 25, 24. Raw range 73 - 0 = 73; cleaned range 25 - 18 = 7. The cleaned graph shows a gentle warming trend that the raw graph hid. Honest cleaning keeps a log of every change and why, so readers can check it.

## The data
table: School day | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10
  - Raw reading | 18 | 19 | 0 | 20 | 22 | 73 | 22 | 24 | 2.5 | 24
  - Note | | | sensor offline; stored 0 | | | recorded in °F by mistake; °C = (°F - 32) x 5 ÷ 9 | | | paper log says 25 | 
  - Cleaned (°C) | {18} | {19} | {missing} | {20} | {22} | {23} | {22} | {24} | {25} | {24}

## Graph 1: Raw data
graph: School day | 0 10 1 | Raw reading | 0 80 10
  key: 1,18 2,19 3,0 4,20 5,22 6,73 7,22 8,24 9,2.5 10,24
  dots: yes
  minor: off

## Graph 2: Cleaned data
graph: School day | 0 10 1 | Temperature (°C) | 0 30 5
  key: 1,18 2,19 4,20 5,22 6,23 7,22 8,24 9,25 10,24
  dots: yes

## Compare
fill:
  - Raw data: highest {73}, lowest {0}, range {73}.
  - Cleaned data: highest {25}, lowest {18}, range {7}.
write: How did the picture change after cleaning?
  lines: 3
  key: The raw graph has one huge spike (day 6) and two big drops (days 3 and 9), so it looks wild and the real pattern is squashed flat near the bottom. The cleaned graph shows temperatures staying between 18 and 25 and slowly warming over the two weeks.
write: Why is day 3 left blank instead of filled in with a number?
  lines: 2
  key: There is no real reading for day 3. Filling it with 0 or a guess would add made-up data; leaving it blank and reporting it as missing is honest.

## Stretch
write: A classmate wants to fill day 3 with 20, "because it was probably about that." Is that ever OK? If so, what must the report say?
  lines: 3
  key: It can be OK only if it is clearly labeled as an estimate and the method is explained (for example, "day 3 estimated as the average of days 2 and 4"). Hiding a guess among real readings is dishonest because readers would trust it as measured data.

# 41. Alt Text Workshop
minutes: 30
materials: pencil
ican: I can write short alt text that gives a screen reader user what an image means on the page.
directions: Alt text is a short description that a screen reader reads aloud in place of an image. Each box describes an image on a school website and where it sits. Write alt text for each one in 20 words or fewer. Write "empty" if the image is only decoration.
mistakes: Students start with "Image of" or "Picture of" (the screen reader already says it is an image) or describe every detail of the photo. Ask: what does this image add to this page? For a button or link, the alt text is what it does (Search), not what it looks like (magnifying glass). For a chart, give the takeaway or the numbers, not "a bar chart."
notes: Rules of thumb: say what matters for the page, skip "image of," keep it short, give the function for buttons and links, give the data or main point for charts, and use empty alt text (alt="") for pure decoration so screen readers skip it. Word counts for the key answers: 1, 12 words; 2, 1 word; 3, empty; 4, 15 words (counting numbers as words); 5, 3 words; 6, 14 words. Other wordings are right if they carry the same meaning in 20 words or fewer.

## Warm up
example: On the Art Club page, a photo shows four students painting a mural of a whale on the gym wall. Weak: "Image of kids." Too long: every color, shirt and brush. Good: "Art Club students painting a whale mural on the gym wall."
choice: The school logo at the top of every page links to the home page. Which alt text is best?
  - Picture of a blue owl logo with a pencil
  - Logo
  * Maple Street School home page
  - Owl

## Main: Write the alt text
table: Image and where it is | Alt text (20 words or fewer) | Word count
  height: 0.75
  - 1. Garden Club page, at the top: a photo of three students planting tomato seedlings in a raised bed, with watering cans. | {Garden Club students planting tomato seedlings in the school's raised garden bed.} | {12}
  - 2. Every page, top right: a small magnifying glass picture. Clicking it opens the search box. It has no words. | {Search} | {1}
  - 3. Between two news stories: a thin wavy line, just for looks. | {empty (alt="")} | {0}
  - 4. Reading Challenge page: a bar chart of books read. Grade 4 read 310, grade 5 read 420 and grade 6 read 280. | {Books read: grade 4, 310; grade 5, 420; grade 6, 280. Grade 5 read the most.} | {15}
  - 5. Contact page: a small envelope picture that is a link for emailing the office. | {Email the office} | {3}
  - 6. Band News page, next to "Spring concert a hit!": a photo of the band on stage, playing to a full gym. | {The school band performing on stage at the spring concert for a packed gym.} | {14}

## Stretch
write: Image 3 gets empty alt text. Why is that better for a screen reader user than writing "wavy line"?
  lines: 2
  key: The line adds no meaning. Empty alt text tells the screen reader to skip it, so the user does not have to listen to useless words between the stories.

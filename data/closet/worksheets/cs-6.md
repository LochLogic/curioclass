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

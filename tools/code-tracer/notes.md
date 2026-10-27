## A 5-minute start

1. Open **Trace** at level 1, "Apples". The code card on the left is a tiny program. The orange arrow shows the line about to run: `apples = 3`.
2. Ask the class: "After this line, what is in apples?" Type the guess with the number keys (or the keyboard), then press **Run line**. The real value slides from the code into the trace table. A green check and "matched" means the guess was right. A wrong guess stays in the table, crossed out, under the real value.
3. Keep going line by line. Line 3 is the one to talk about: `apples = apples + 2` uses the 3 already in apples and stores 5 back in the same box. When the program ends, the "Traced!" stamp lands and the level dot fills.

## The two modes

- **Trace:** 12 short programs in four sets. Before every line runs, predict what it does, then press **Run line** to check. The table keeps a row for every step, so it is a record of the whole run. Nothing can be undone in Trace: that is the point, the computer does not go back either.
  - **One box** (levels 1 to 3): one variable changing. A new value throws the old one away.
  - **Two boxes** (levels 4 to 6): copying a value from one variable to another. Level 6 tries to swap two variables and does not manage it.
  - **Repeat** (levels 7 to 9): the repeat line runs the lines tucked under it again and again. Repeat rows fill in by themselves and write "round 2 of 4" in the Check column; you predict the lines inside.
  - **If** (levels 10 to 12): an if line asks a yes or no question. Choose **Yes** or **No**, then **Run line**. When the answer is no, the lines under the if are skipped: they fade and get a "skipped" tag on the code card.
  - Levels 6, 9 and 12 end with a **Note check**: the first line of every program is a note for people (it starts with #). Does the note tell the truth about what the code did?
  - **Just show me** runs the line without a guess. It counts as not matched.
- **Workbench:** any of the 12 programs, plus program 13, "Swap with a spare", the fix for level 6. **Step** runs one line, **Back** takes it back, **Play** runs on its own (Slow or Quick). Tap a number in the code to change it with the + and − buttons: the trace starts over with the new numbers, and the note gets a yellow "?" because notes don't change by themselves. **Reset numbers** puts the numbers back. Turn **Predict** on to guess each line before Step runs it.

## Talk about it

- In level 2, where did the 2 go when steps became 7?
- In level 4, a changed to 9. Why did b stay 4?
- Level 6 says "swap left and right". What went wrong? How does program 13 fix it?
- In level 9, which column tells you how many rounds are left? What would total be with repeat 4?
- In level 12, why does lives stop at 0? What would happen without the if?
- On the Workbench, change level 8's repeat to 6 and the 2 to 5. Is the note still true?

## Good to know

- Works for pairs on laptops, or on a projector with the class holding up whiteboard guesses before someone presses **Run line**.
- Keyboard: Tab moves through the controls, the number keys and minus type a guess, Backspace deletes, Y and N answer an if line or the note check, Enter runs the line. On the Workbench, Tab reaches the numbers in the code: Enter opens the + and − buttons, the arrow keys change the number, Escape closes them.
- **Read** speaks the line at the top of the panel again. **Sound** off stops the narrator and the sounds. **Motion** off keeps the same timing, but values appear in place with an orange outline instead of sliding, and the stamp does not drop.
- When all 12 levels have been traced in one visit (in any order), the narrator says so and the **Workbench** button glows once.
- **Print trace** prints the program and the full table for the level you are on.
- Nothing is saved: closing the page starts fresh. Nothing goes over the network.
- The code is a tiny made-up language, close to Python and Scratch: `=` means "store in", `say` shows a value, `repeat 3 times:` and `if temp > 80:` work on the lines indented under them. The tool runs it with its own small interpreter.
- Standards: CSTA K-12 Computer Science Standards E4-PRO-VD-06, E4-PRO-RD-07, E4-PRO-TR-08 (2017: 1B-AP-09, 1B-AP-17, 1B-AP-15).
- Sources: Code.org CS Fundamentals glossary (variable, loop, conditional); Scratch Wiki, "Variable"; The Python Tutorial 3.1 and 3.2 (assignment, comments); trace tables as taught by Isaac Computer Science and BBC Bitesize. The programs are original to Curio Class.

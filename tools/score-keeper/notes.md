## A 5-minute start

1. Open **Play** and press **Play** (or Space). Steer with the arrow buttons or the arrow keys. Every time a star lands in the ship, the game freezes for a moment, the line `when you catch a star:` lights up, then `score = score + 1`, and a new number flies into the **score** box. Its counter under the box ticks: "changed 1 time".
2. Press **Pause**, then **Step** (or S) a few times. Each press runs exactly one line. Ask: which box will change on the next line?
3. Let a rock hit the ship. `lives = lives - 1` runs and the **lives** box goes down. Watch the **goal** box the whole game: it says 20 and its counter stays at 0.
4. Switch to **Lab**, turn **lives start** down to 1 and press **Run**. Autopilot flies the same sky every time, so the game ends after only 3 drops. That one number made the difference.

## The three modes

- **Play:** Star Catch with five labeled boxes (score, lives, speed, best, goal) under the game and the whole program beside it. Stars add to score, rocks take from lives, every 10 seconds of game time speed goes up by 1 (up to 5), and the game ends when lives is 0 or less or score reaches the goal (20). At the end, `if score > best:` saves the score in best. **Code speed: Watch** freezes the game while each line runs, 0.7 s for each line and 0.5 s for each event or check line, so the class can follow it; **Quick** shows each line for a fifth of a second while the game keeps going. **Autopilot** and **Same sky** are off in Play.
- **Lab:** the same game with Autopilot and Same sky on, so every run is the same until a student turns a dial. The dials sit in the program itself: score start (0 to 15), lives start (1 to 9), speed start (1 to 5), how much a star adds (1, 2, 5, 10) and how much a rock takes (0 to 3). Seven questions step through one change each, and each one names the dial to turn and says to press **Run**. At the end a result card shows the final values, why the game ended and how many drops (and seconds) the game lasted; **Save to notebook** keeps the run (until the first save, the hint and voice say to press it). **Reset lab** puts every dial back (3 lives, 0 score, speed 1, star 1, rock 1). **Next ▶** and **◀ Prev** do the same, so each question starts from the defaults.
- **Notebook:** saved runs in a table (**Copy table** pastes into a spreadsheet as columns) and a bar chart of the final score with a dashed goal line. **Stored or changing?** asks students to sort each variable into Stayed the same or Changed (drag a card, use its buttons, or press 1, 2 or 0 on a focused card); **Check with my runs** answers from the counts in their own runs. Three What I found boxes take sentences. **Save notebook** keeps everything on this device only, and **Clear notebook** asks first. Nothing is sent anywhere.

## Talk about it

- Which box never changed in any run? Why might a program keep a number that never changes? (goal is stored once and only read.)
- What made score change? What made speed change? (A catch is something you did; speed changed because time passed, and nobody pressed anything.)
- Start speed at 5. The `if speed < 5:` line still lights up every 10 seconds. Did the line run? Did the box change?
- Make a rock take 2. Lives ends at minus 1. Can a variable go below zero? What would you change in the program to stop that?
- Run it twice without changing anything. Which boxes start over, and which one keeps its value from last time? (best keeps 8, and its counter says it changed 0 times on the second run.)
- A box holds one value at a time. When score goes from 3 to 4, where did the 3 go?

## Lab answers (teacher key)

Same sky and Autopilot on, after Reset lab, one change at a time:

| Change | Game ends at drop | Because | score | lives | speed | best |
|---|---|---|---|---|---|---|
| none | 13 (20.8 s) | lives is 0 or less | 8 | 0 | 3 | 8 |
| lives start 1 | 3 | lives | 2 | 0 | 1 | 2 |
| lives start 9 | 32 (41.4 s) | goal | 20 | 3 | 5 | 20 |
| star adds 5 | 5 | goal | 20 | 2 | 1 | 20 |
| rock takes 0 | 32 | goal | 20 | 3 | 5 | 20 |
| rock takes 2 | 9 | lives | 5 | minus 1 | 2 | 5 |
| speed start 5 | 13 (11.0 s) | lives | 8 | 0 | 5 | 8 |
| score start 10 | 13 | lives | 18 | 0 | 3 | 18 |

Question 5 (score start 10): Autopilot caught the same 8 stars; score just started higher. Question 7: running twice gives the same row, but best stays 8 and changes 0 times.

## Good to know

- The program is fixed and is data run by a small interpreter in the tool; nothing a student types or arranges is ever run as code. The dials only change numbers inside the program's lines.
- The score, lives and speed boxes show "empty" until the program's start lines put a value in them; best gets 0 when the page opens and goal gets 20.
- The game clock counts game time only: pause and the Watch freezes stop it, and so does the 10-second speed clock. Step while paused with no line waiting lets the game run on to the next line, then stops again. A Step pressed while a line is still showing is kept and runs the next line.
- In Watch mode the ship cannot be steered while a line runs (the game is frozen). Arrow keys and A and D move the ship; Space plays and pauses; S steps.
- With Motion off, values appear in the boxes without the flying number, the stars stop twinkling, and the voice is unchanged.
- On small screens the Lab log is hidden and the program card scrolls to the running line.
- Every waiting moment names what to press: before the first game the hint says to press Play and how to steer; after each game it says to press Play again; the Lab hint names Run; the result card's hint names Save to notebook; the Notebook says how to sort and to press Check with my runs, or, with no saved runs yet, sends students to the Lab.
- After Check, "Nice work" plays only when every card is right. If a card says Look again, the voice says to move it to the other bin and press Check again.
- Each mode keeps its own log: switching modes clears it.
- Read speaks the hint for the moment (and the current question in Lab).

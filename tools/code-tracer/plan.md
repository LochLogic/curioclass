arc: teach-then-practice
minutes: 45
focus: E4-PRO-VD-06; E4-PRO-RD-07
goal: I can trace a short program one line at a time to show how its variables change, and check whether its note tells the truth.
materials: The tool on the projector, and one laptop per pair. Whiteboards. Three clear cups: two with different colored water, one empty. An exit slip per student (or the exit program on the board).
grouping: Whole class, then pairs on laptops (one types, both agree), then whole class.
---
## Before class

- Open the tool on the projector in **Trace** at level 1, **Apples**. Laptops open to it too.
- Draw an empty trace table on the board: Step, Line, apples, Says.
- Nothing undoes in Trace; **Restart** clears the level. Nothing is saved. The teacher notes explain every button.

## Hook (5 min)

1. Write "line leader = Maya" on the board, then under it "line leader = Leo".
2. "Who is line leader now?" (Leo.) "Where did Maya go?" (Out of the job. It holds one name at a time.)
3. "A computer reads lines like these one at a time, top to bottom. Can you keep up with it?"

## Teach (8 min)

1. "The orange ▶ shows the line about to run. Line 1 starts with #: a note for people, so the computer skips it."
2. "After line 2, what will apples be?" Everyone holds up a whiteboard guess. A student types the class guess and presses **Run line**. Fill the board table too.
3. Stop on line 3, `apples = apples + 2`: "Which side is worked out first?" (The right side: the 3 in apples plus 2 is 5. Then 5 is stored back in apples.)
4. Point to the small grey numbers: every row carries the newest value of each variable.
5. Make one wrong guess on purpose. The guess stays, crossed out, under the real value. "That shows exactly where our thinking split from the computer's."
6. At "Traced!", point to the first-try tally. Show **Just show me** for a pair that is truly stuck (it counts as not matched).

## Practice (17 min)

1. Pairs open level 2 from the level dots. Both agree before **Run line**; switch typists each level.
2. Every pair does levels 2, 4, 6, 7 and 10. Fast pairs do all of them, ending with 12.
3. Level 4, to pairs who missed step 4: "a changed to 9. Why did b stay 4?" (b got a copy of the 4, not a link to a.)
4. Pairs wait at the note card on level 6, **The swap**. Then stop the class: "Does the note tell the truth?" (No. Both end at 8. The 3 was thrown away when left got the 8.) Pairs tap **No**, then **Next**.
5. Repeat levels: "The round rows fill in by themselves. You predict the lines inside."
6. If levels: tap **Yes** or **No**, then **Run line**. "On level 10, why is line 5 skipped?" (75 is not more than 80.)
7. Level 12: "Why does lives stop at 0?" (In round 4: is 0 more than 0? No, so the subtract line is skipped.)

## Apply (10 min)

1. "Swap the drinks so each cup holds the other color. You can only pour." A student tries with two cups. (They mix, like level 6.) "What would help?" (The empty cup.) Swap using the third cup.
2. On the projector, open **Workbench** and pick **Swap with a spare**. Press **Step** row by row. "Which line pours into the empty cup?" (`spare = left`.) "Did both values survive?" (Yes: it says 8, then 3.)
3. Pick **Doubling tower**. Tap the 3 in `repeat 3 times` and press + once. A yellow ? appears on the note. **Step** to the end. "Is the note still true?" (No. It doubles 4 times and ends at 16.)
4. Pairs write a new true note on whiteboards. Read two aloud, then press **Reset numbers**.

## Exit check (5 min)

Students trace this in a table (Step, Line, score, Says):

```
# the score never goes above 10
score = 4
repeat 3 times:
  score = score + 3
say score
```

"Does the note tell the truth?" (4, 7, 10, 13; it says 13. No.) Note who loses track of rounds.

## Support and stretch

- **Support:** start on levels 1 to 3 (**One box**). Before each guess, point to the row above: "What is in the box right now?"
- **Support:** **Read** speaks the hint again; a partner reads the line aloud, right side first.
- **Stretch:** in **Workbench**, turn **Predict** on for **Doubling tower**, change the repeat to 6 and the 2 to 5, and predict the end. (15625.)
- **Stretch:** "Without the if on level 12, where would lives end?" (-1.) Write a program whose note lies and trade with another pair.

## Short on time

- Hook (3 min), then teach on **Apples** (5 min).
- Pairs do levels 4 and 6, with the note card (8 min).
- Ask out loud: "a = 5, b = a, a = 2, say b. What does it say?" (5.) (3 min)

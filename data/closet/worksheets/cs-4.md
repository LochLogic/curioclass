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

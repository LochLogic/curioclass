# 1. Variables and Displays
minutes: 30
materials: pencil
ican: I can classify a variable as categorical or quantitative and choose a display that fits it.
directions: For each variable, write C if it is categorical or Q if it is quantitative. Then name a good graph to display it. Some variables have more than one good choice; be ready to defend yours.
mistakes: Numbers are not always quantitative: ZIP codes and jersey numbers are labels, so they are categorical (averaging them means nothing). A yes/no variable is categorical. Students often pick a line graph for any quantitative variable; a line graph (time plot) fits only data collected in time order.
notes: Accept any reasonable display: categorical takes a bar chart or pie chart; one quantitative variable takes a dotplot, histogram, stemplot or boxplot; a quantitative variable measured over time takes a time plot; two quantitative variables on the same individuals take a scatterplot. Quick test: "Does it make sense to average it?" If yes, it is quantitative.

## Warm up: Individuals and variables
text: A store surveys 50 shoppers. It records each shopper's number of items bought and which entrance they used.
fill:
  - The individuals are {the 50 shoppers}.
  - "Number of items bought" is a {quantitative} variable.
  - "Entrance used" is a {categorical} variable.

## Main: Classify and display
table: Variable | C or Q | A good display
  - Eye color of 30 people | {C} | {bar chart or pie chart}
  - Price of 40 used bikes | {Q} | {histogram, dotplot or boxplot}
  - Number of texts 25 teens sent yesterday | {Q} | {dotplot or histogram}
  - ZIP code of each customer of a shop | {C} | {bar chart}
  - Favorite music genre of 60 students | {C} | {bar chart or pie chart}
  - Finish time of each runner in a 5K race | {Q} | {histogram or boxplot}
  - Type of phone plan: prepaid or monthly | {C} | {bar chart or pie chart}
  - Daily high temperature for one month | {Q} | {time plot (line graph)}
  - Jersey numbers on a soccer team | {C} | {bar chart}
  - Grams of sugar in 50 breakfast cereals | {Q} | {histogram, stemplot or boxplot}
  - Whether each cereal box meets its label weight (yes or no) | {C} | {bar chart or pie chart}
  - Outdoor temperature and ice cream sales on each of 30 days | {Q} | {scatterplot}

## Stretch
write: A classmate says ZIP code is quantitative because it is a number. Explain why they are wrong.
  lines: 3
  key: ZIP codes are labels for places. Arithmetic on them has no meaning: the average of two ZIP codes is not a place in between, and a bigger ZIP code is not "more" of anything. So ZIP code is categorical.
choice: A survey records each student's grade level and whether they bike to school. Which display shows the relationship between these two variables best?
  - A scatterplot
  - A histogram of grade level
  * A segmented (stacked) bar chart
  - A boxplot for each answer

# 21. Probability Checkpoint
minutes: 45
materials: pencil, calculator
ican: I can use probability rules, find expected values, and compute binomial and geometric probabilities.
directions: Show the rule or formula you use for each item. Round decimals to four places unless the item says otherwise.
mistakes: Students add P(A) + P(B) without subtracting the overlap. In conditional probability, the "given" group goes in the denominator: P(instrument | sport) uses the 100 sport players, not all 200. For binomial "at least" questions, students often forget either P(9) or P(10). In the geometric items, "first success on the third try" means two failures then a success: (0.8)²(0.2).
notes: Independence check: P(A)P(B) = 0.4 × 0.5 = 0.2 = P(A and B), so A and B are independent. In the two-way table, P(instrument) = 70/200 = 0.35 but P(instrument | sport) = 0.30, so the events are not independent. Binomial: 45 × 0.7⁸ × 0.3² = 0.2335; P(X ≥ 9) = 0.1211 + 0.0282 = 0.1493. The game loses 20 cents per play on average.

## Part A: Probability rules
fill: P(A) = 0.4, P(B) = 0.5 and P(A and B) = 0.2. P(A or B) = {0.7}
fill: For the same events, are A and B independent? {yes}, because P(A) × P(B) = {0.2} = P(A and B).
fill: A fair die is rolled 4 times. P(at least one six) = 1 - (5/6)⁴ ≈ {0.5177}
text: A school surveys 200 students.
table: | Plays an instrument | No instrument | Total
  - Plays a sport | 30 | 70 | 100
  - No sport | 40 | 60 | 100
  - Total | 70 | 130 | 200
fill: P(plays an instrument | plays a sport) = {0.30}
fill: P(plays a sport | plays an instrument) = {30/70 ≈ 0.4286}
choice: Are "plays a sport" and "plays an instrument" independent?
  - Yes, because 30 students do both
  * No, because P(instrument | sport) = 0.30 but P(instrument) = 0.35
  - Yes, because each row adds to 100
  - No, because the events are mutually exclusive

## Part B: Random variables and expected value
fill: X takes the values 0, 1, 2 and 3 with probabilities 0.1, 0.3, 0.4 and p. p = {0.2}, and E(X) = {1.7}
fill: A game costs $1. You win $5 with probability 0.1, win $1 with probability 0.3, and win nothing otherwise. The expected net gain per play is {-$0.20}

## Part C: Binomial and geometric
text: A player makes 70% of free throws, and shots are independent. She shoots 10 free throws.
fill: P(exactly 8 made) = {0.2335}
fill: P(at least 9 made) = {0.1493}
fill: Mean number made = {7}, standard deviation ≈ {1.449}
text: Each scratch card has a 0.2 chance of a prize, independently.
fill: P(the first prize is on the 3rd card) = {0.128}
fill: P(it takes more than 4 cards to get a prize) = {0.4096}
fill: Expected number of cards to get the first prize = {5}
choice: Which situation is binomial?
  - Drawing cards from a deck without replacement until you get an ace
  * Flipping a fair coin 20 times and counting heads
  - Rolling a die until you roll a six
  - Measuring the heights of 10 plants

## Stretch
write: Explain the difference between "mutually exclusive" and "independent". Can two events with positive probability be both? Use an example.
  lines: 4
  key: Mutually exclusive means the events cannot happen together: P(A and B) = 0. Independent means one happening does not change the chance of the other: P(A and B) = P(A)P(B). If both have positive probability, P(A)P(B) > 0, so they cannot have P(A and B) = 0: they cannot be both. Example: rolling a 1 and rolling a 6 on one die are mutually exclusive but not independent, since knowing you rolled a 1 makes a 6 impossible.

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

# 5. Normal Model Calculations
minutes: 40
materials: pencil, calculator
ican: I can use z-scores and a standard Normal table to find Normal probabilities and percentiles.
directions: Use the z table: each entry is the area to the LEFT of z. The row gives z to one decimal and the column gives the second decimal (row -1.3, column .03 is z = -1.33). Round each z-score to two decimals. Sketch a Normal curve and shade the area for each problem.
mistakes: Students forget that the table gives the area to the left, so for "more than" they must subtract from 1. For "between," subtract the two left areas; do not add them. For percentiles they look up z in the table's margin instead of finding the area inside the table: the 90th percentile needs the area closest to 0.9000, which is 0.8997 at z = 1.28. With negative z, the column is still added to the row: row -0.6 and column .07 is z = -0.67, not -0.53.
notes: The table is an excerpt of the standard Normal table with only the rows these problems need; its values were computed and match standard printed tables. Answers by calculator (normalcdf) can differ in the fourth decimal because the table rounds z to two places: the first bulb problem by calculator is 0.0912 with the unrounded z. The 25th percentile uses z = -0.67 (area 0.2514, the closest to 0.2500).

## The z table (area to the left of z)
table: z | .00 | .01 | .02 | .03 | .04 | .05 | .06 | .07 | .08 | .09
  - -1.3 | .0968 | .0951 | .0934 | .0918 | .0901 | .0885 | .0869 | .0853 | .0838 | .0823
  - -1.2 | .1151 | .1131 | .1112 | .1093 | .1075 | .1056 | .1038 | .1020 | .1003 | .0985
  - -0.6 | .2743 | .2709 | .2676 | .2643 | .2611 | .2578 | .2546 | .2514 | .2483 | .2451
  - -0.5 | .3085 | .3050 | .3015 | .2981 | .2946 | .2912 | .2877 | .2843 | .2810 | .2776
  - 0.5 | .6915 | .6950 | .6985 | .7019 | .7054 | .7088 | .7123 | .7157 | .7190 | .7224
  - 1.2 | .8849 | .8869 | .8888 | .8907 | .8925 | .8944 | .8962 | .8980 | .8997 | .9015
  - 1.3 | .9032 | .9049 | .9066 | .9082 | .9099 | .9115 | .9131 | .9147 | .9162 | .9177
  - 1.5 | .9332 | .9345 | .9357 | .9370 | .9382 | .9394 | .9406 | .9418 | .9429 | .9441
  - 2.0 | .9772 | .9778 | .9783 | .9788 | .9793 | .9798 | .9803 | .9808 | .9812 | .9817

## Warm up: z-scores and the table
example: Light bulbs of one type last a mean of 1,200 hours with a standard deviation of 150 hours. A bulb that lasts 1,350 hours has z = (1,350 - 1,200)/150 = 1.00: one standard deviation above the mean.
fill:
  - A bulb that lasts 975 hours has z = {-1.50}
  - The area to the left of z = 1.25 is {0.8944}
  - The area to the right of z = 0.53 is {0.2981}

## Main: Eight Normal problems
text: **Light bulbs.** Lifetimes are approximately Normal with mean 1,200 hours and standard deviation 150 hours.
fill: What proportion of bulbs last less than 1,000 hours? z = {-1.33}, proportion = {0.0918}
fill: What proportion last more than 1,500 hours? z = {2.00}, proportion = {0.0228}
fill: What proportion last between 1,100 and 1,400 hours? {0.9082 - 0.2514 = 0.6568}
fill: How long does a bulb at the 90th percentile last? z = {1.28}, lifetime = {1,392} hours
text: **Reading test.** Scores are approximately Normal with mean 70 points and standard deviation 8 points.
fill: What percent of students score 82 or more? z = {1.50}, percent = {6.68%}
fill: What percent score below 60? z = {-1.25}, percent = {10.56%}
fill: What score is the 25th percentile (the first quartile)? z = {-0.67}, score = {64.64}
fill: What percent score between 66 and 74? {0.6915 - 0.3085 = 0.3830, or 38.30%}

## Stretch: Work backward
write: A machine fills cups with a mean of 250 mL, and fill amounts are Normal. Only 2.28% of cups get more than 260 mL. What is the standard deviation? Show how you used the table.
  lines: 3
  key: The area to the left of 260 is 1 - 0.0228 = 0.9772, which is z = 2.00 in the table. So 260 is 2 standard deviations above 250: 2σ = 10, and σ = 5 mL.

# 15. Probability Rules
minutes: 35
materials: pencil, calculator
ican: I can use the addition rule, the multiplication rule and conditional probability to find probabilities.
directions: Name the rule you use for each problem, then show the numbers you put into it. Give answers as fractions or as decimals rounded to four places.
mistakes: Students add without subtracting the overlap: hearts and face cards share the 3 heart face cards. They multiply probabilities for events that are not independent without changing the second one: after one red marble is drawn, only 4 of 7 are red. In conditional problems, the "given" group is the denominator: P(grade 10 | dog) uses the 54 dog owners, not the 60 tenth graders.
notes: Rules: P(A or B) = P(A) + P(B) - P(A and B); P(A and B) = P(A) × P(B | A), which is P(A) × P(B) when A and B are independent; P(B | A) = P(A and B)/P(A). The machine problem is a tree: 0.60 × 0.02 + 0.40 × 0.05 = 0.012 + 0.020 = 0.032. Stretch: P(Y | defective) = 0.020/0.032 = 0.625, so machine Y makes 40% of the parts but 62.5% of the defective ones.

## Warm up: Which rule?
match: Match each rule to its formula.
  - Addition rule = P(A or B) = P(A) + P(B) - P(A and B)
  - Multiplication rule = P(A and B) = P(A) × P(B | A)
  - Conditional probability = P(B | A) = P(A and B) ÷ P(A)
  - Independent events = P(A and B) = P(A) × P(B)

## Part A: Addition rule
fill: P(A) = 0.35, P(B) = 0.45 and P(A and B) = 0.15. P(A or B) = {0.65}
fill: Roll a fair die. P(a 1 or an even number) = {4/6 = 2/3}
fill: Draw one card from a standard 52-card deck. P(a heart or a face card) = {22/52 = 11/26 ≈ 0.4231}

## Part B: Multiplication rule
text: The chance of rain is 0.3 on Saturday and 0.4 on Sunday. Assume the two days are independent.
fill: P(rain on both days) = {0.12}
fill: P(no rain either day) = {0.42}, so P(rain on at least one day) = {0.58}
fill: A bag has 5 red and 3 blue marbles. Draw two without replacement. P(both red) = {5/8 × 4/7 = 5/14 ≈ 0.3571}

## Part C: Conditional probability
text: A survey of 120 students asked whether they have a dog.
table: | Has a dog | No dog | Total
  - Grade 9 | 30 | 30 | 60
  - Grade 10 | 24 | 36 | 60
  - Total | 54 | 66 | 120
fill: P(has a dog | grade 9) = {30/60 = 0.5}
fill: P(grade 10 | has a dog) = {24/54 = 4/9 ≈ 0.4444}
fill: P(A) = 0.6 and P(A and B) = 0.24. P(B | A) = {0.4}
fill: Machine X makes 60% of a factory's parts, and 2% of its parts are defective. Machine Y makes the other 40%, and 5% of its parts are defective. P(a random part is defective) = {0.032}

## Stretch
fill: A part is defective. P(it came from machine Y) = {0.625}
write: Are "has a dog" and "grade 9" independent in the survey? Show the numbers that decide it.
  lines: 3
  key: No. P(has a dog) = 54/120 = 0.45, but P(has a dog | grade 9) = 0.5. Knowing the grade changes the probability, so the events are not independent.

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

# 26. Sample Mean Probabilities
minutes: 40
materials: pencil, calculator
ican: I can use the sampling distribution of a sample mean to find probabilities about averages.
directions: For each problem, find the mean and standard deviation of the sample mean x̄ first: the mean is μ and the standard deviation is σ/√n. Check that a Normal model fits, then find the z-score and the probability. Round z to two decimals and probabilities to four.
mistakes: Students use σ instead of σ/√n, which answers a question about one item, not an average. In the luggage problem, they compare the total to the mean of one bag; convert the total limit to an average (1,500 ÷ 36) first. Students also use a Normal model for small samples from skewed populations: the commute problem works only because n = 50 is large.
notes: Keys show the z table answer with the rounded z, and the calculator answer (normalcdf with the unrounded z) where the two differ; accept either. In the first problem, σ/√n = 0.5/√20 ≈ 0.1118, z = -0.2/0.1118 ≈ -1.79. In the commute problem, 10/√50 ≈ 1.414, z = 2/1.414 ≈ 1.41. The battery problem uses z = -1.645 for the bottom 5%: 10 - 1.645(0.3) ≈ 9.51. For the sample size, 0.5/√n = 0.1 gives √n = 5.

## Warm up: Shrinking spread
text: Cereal bags have weights with mean μ = 16.2 ounces and standard deviation σ = 0.5 ounces, and the weights are approximately Normal.
table: Sample size n | Mean of x̄ | Standard deviation of x̄
  - 1 | {16.2} | {0.5}
  - 25 | {16.2} | {0.1}
  - 100 | {16.2} | {0.05}

## Main: Six problems
fill: A store checks a random sample of 20 bags. P(the mean weight is below 16 ounces): SD of x̄ = {0.1118}, z = {-1.79}, P = {0.0367 (0.0368 by calculator)}
fill: For comparison, P(one random bag weighs less than 16 ounces) = {0.3446}
fill: Commute times in a city are skewed right, with mean 24 minutes and standard deviation 10 minutes. For a random sample of 50 commuters, P(x̄ > 26 minutes): z = {1.41}, P = {0.0793 (0.0786 by calculator)}
fill: Checked bags on a flight weigh a mean of 40 pounds with standard deviation 8 pounds. A cart holds 36 bags and is rated for 1,500 pounds. The cart is over its limit when x̄ is more than {41.67} pounds, and P(over the limit) = {0.1056}
fill: A battery's life is Normal with mean 10 hours and standard deviation 1.2 hours. In samples of 16 batteries, only 5% of sample means fall below {9.51} hours.
fill: How large a sample of cereal bags makes the standard deviation of x̄ equal to 0.1 ounce? n = {25}
choice: Why can we use a Normal model for the commute problem even though commute times are skewed?
  - Because the population is Normal
  - Because the standard deviation is small
  * Because the sample is large (n = 50), so the central limit theorem applies
  - Because commute times cannot be negative

## Stretch
write: Explain why P(x̄ < 16) is so much smaller than P(one bag < 16) in the first two problems.
  lines: 3
  key: An average of 20 bags varies much less than a single bag: its standard deviation is 0.1118 ounces instead of 0.5. A light bag is common, but for the average to be below 16, many bags must be light at once, which is rare.
write: Could you find P(one commute is longer than 26 minutes) the same way? Why or why not?
  lines: 2
  key: No. One commute comes from the skewed population, not from a Normal distribution, so a Normal calculation would be wrong. The central limit theorem is about averages of large samples.

# 36. Homogeneity or Independence?
minutes: 40
materials: pencil, calculator
ican: I can tell a chi-square test for homogeneity from a test for independence and compute expected counts.
directions: For each setting, decide which chi-square test fits: **homogeneity** (separate samples or groups, one categorical variable compared across them) or **independence** (one sample, two categorical variables measured on each individual). Then compute expected counts: expected = (row total)(column total) ÷ (table total).
mistakes: Students decide from the table instead of from how the data were collected: both tests use the same two-way table and the same arithmetic. Ask, "Was there one sample or several?" Students also round expected counts to whole numbers; expected counts can be decimals. An experiment with groups assigned at random (setting 3) is compared with a homogeneity test.
notes: Settings 2, 3 and 5 are homogeneity; 1, 4 and 6 are independence. Lunch table: column totals 135, 66 and 99 out of 300, so each school's expected counts are 45, 22 and 33; χ² ≈ 7.09 with df = 4, P-value ≈ 0.13, so there is not convincing evidence that preferences differ. Bike lane table: expected 120 and 120, 50 and 50, 30 and 30; χ² ≈ 45.67 with df = 2, P-value far below 0.001. All expected counts are at least 5, so the large-counts condition holds.

## Warm up: The key question
fill:
  - Several samples or groups, one variable: a test for {homogeneity}
  - One sample, two variables: a test for {independence}
  - Degrees of freedom for an r × c table: df = {(r - 1)(c - 1)}

## Main: Classify six settings
table: Setting | Homogeneity or independence? | One sample or several?
  - 1. A random sample of 300 adults in a city is asked their age group and their main news source. | {independence} | {one}
  - 2. Separate random samples of 100 students from each of three high schools are asked their favorite lunch. | {homogeneity} | {three}
  - 3. 150 plants are randomly assigned to three fertilizers, and each is recorded as flowering or not. | {homogeneity} | {three groups}
  - 4. A random sample of 400 adults is asked how they get to work and whether they support a new bike lane. | {independence} | {one}
  - 5. Random samples of 200 people from each of four age groups are asked how they usually watch movies. | {homogeneity} | {four}
  - 6. One random sample of 250 cars in a lot is classified by color and by size. | {independence} | {one}

## Main: Expected counts
text: **Setting 2: favorite lunch.** Observed counts:
table: School | Pizza | Salad | Sandwich | Total
  - A | 45 | 20 | 35 | 100
  - B | 38 | 30 | 32 | 100
  - C | 52 | 16 | 32 | 100
  - Total | 135 | 66 | 99 | 300
table: Expected | Pizza | Salad | Sandwich
  - A | {45} | {22} | {33}
  - B | {45} | {22} | {33}
  - C | {45} | {22} | {33}
fill: H₀: The distribution of {favorite lunch} is the same at all three schools. df = {4}
text: **Setting 4: bike lane.** Observed counts:
table: How they get to work | Support | Do not support | Total
  - Car | 90 | 150 | 240
  - Transit | 60 | 40 | 100
  - Bike or walk | 50 | 10 | 60
  - Total | 200 | 200 | 400
table: Expected | Support | Do not support
  - Car | {120} | {120}
  - Transit | {50} | {50}
  - Bike or walk | {30} | {30}
fill: H₀: How adults get to work and support for the bike lane are {independent}. df = {2}

## Stretch
fill: For the bike lane table, χ² = Σ(observed - expected)²/expected = {45.67}
write: For the lunch table, χ² ≈ 7.09 with df = 4, and the P-value is about 0.13. What do you conclude at α = 0.05?
  lines: 3
  key: Since 0.13 > 0.05, fail to reject H₀. There is not convincing evidence that the distribution of favorite lunch differs among the three schools.

# Catalog extract packet: math-x-11

## game-show-strategist
- title: Game Show Strategist | format: simulator | family: probability | stage: spec
- module: math-12-probability-and-random-variables (math 12, Statistics): Probability and Random Variables. Probability models, expected value, binomial and geometric
- module standards: AP-STAT.U4;S-CP.A;S-MD.A;S-MD.B
- standard texts (filed wording; a bare cluster is spelled out):
  - S-CP.A.1: Describe events as subsets of a sample space (the set of outcomes) using characteristics (or categories) of the outcomes, or as unions, intersections, or complements of other events (“or,” “and,” “not”).
  - S-CP.A.2: Understand that two events A and B are independent if the probability of A and B occurring together is the product of their probabilities, and use this characterization to determine if they are independent.
  - S-CP.A.3: Understand the conditional probability of A given B as P(A and B)/P(B), and interpret independence of A and B as saying that the conditional probability of A given B is the same as the probability of A, and the conditional probability of B given A is the same as the probability of B.
  - S-CP.A.4: Construct and interpret two-way frequency tables of data when two categories are associated with each object being classified. Use the two-way table as a sample space to decide if events are independent and to approximate conditional probabilities. For example, collect data from a random sample of students in your school on their favorite subject among math, science, and English. Estimate the probability that a randomly selected student from your school will favor science given that the student is in tenth grade. Do the same for other subjects and compare the results.
  - S-CP.A.5: Recognize and explain the concepts of conditional probability and independence in everyday language and everyday situations. For example, compare the chance of having lung cancer if you are a smoker with the chance of being a smoker if you have lung cancer.
  - S-MD.A.1: (+) Define a random variable for a quantity of interest by assigning a numerical value to each event in a sample space; graph the corresponding probability distribution using the same graphical displays as for data distributions.
  - S-MD.A.2: (+) Calculate the expected value of a random variable; interpret it as the mean of the probability distribution.
  - S-MD.A.3: (+) Develop a probability distribution for a random variable defined for a sample space in which theoretical probabilities can be calculated; find the expected value. For example, find the theoretical probability distribution for the number of correct answers obtained by guessing on all five questions of a multiple-choice test where each question has four choices, and find the expected grade under various grading schemes.
  - S-MD.A.4: (+) Develop a probability distribution for a random variable defined for a sample space in which probabilities are assigned empirically; find the expected value. For example, find a current data distribution on the number of TV sets per household in the United States, and calculate the expected number of sets per household. How many TV sets would you expect to find in 100 randomly selected households?
  - S-MD.B.5: (+) Weigh the possible outcomes of a decision by assigning probabilities to payoff values and finding expected values.
  - S-MD.B.5a: Find the expected payoff for a game of chance. For example, find the expected winnings from a state lottery ticket or a game at a fast-food restaurant.
  - S-MD.B.5b: Evaluate and compare strategies on the basis of expected values. For example, compare a high-deductible versus a low-deductible automobile insurance policy using various, but reasonable, chances of having a minor or a major accident.
  - S-MD.B.6: (+) Use probabilities to make fair decisions (e.g., drawing by lots, using a random number generator).
  - S-MD.B.7: (+) Analyze decisions and strategies using probability concepts (e.g., product testing, medical testing, pulling a hockey goalie at the end of a game).
- concept line: Simulate game show choices (Monty Hall and friends); expected value says when to switch.
- old tags: skill_key=expected-value | action=simulate-tune | setting_group=game-show
- read: tools/game-show-strategist/spec.md

## sample-machine
- title: Sample Machine | format: simulator | family: sampling | stage: spec
- module: math-12-sampling-distributions (math 12, Statistics): Sampling Distributions. Variation in statistics from sample to sample
- module standards: S-IC.A;AP-STAT.U5
- standard texts (filed wording; a bare cluster is spelled out):
  - S-IC.A.1: Understand statistics as a process for making inferences about population parameters based on a random sample from that population.
  - S-IC.A.2: Decide if a specified model is consistent with results from a given data-generating process, e.g., using simulation. For example, a model says a spinning coin falls heads up with probability 0.5. Would a result of 5 tails in a row cause you to question the model?
- concept line: Draw thousands of samples and watch a sampling distribution form; the Central Limit Theorem appears on its own.
- old tags: skill_key=sampling-distributions | action=simulate-tune | setting_group=robot-machine
- read: tools/sample-machine/spec.md

## courtroom-statistics
- title: Courtroom Statistics | format: roleplay | family: none | stage: built
- module: math-12-confidence-intervals-and-significance-tests (math 12, Statistics): Confidence Intervals and Significance Tests. Inference for proportions and means
- module standards: S-IC.B;AP-STAT.U6;AP-STAT.U7
- standard texts (filed wording; a bare cluster is spelled out):
  - S-IC.B.3: Recognize the purposes of and differences among sample surveys, experiments, and observational studies; explain how randomization relates to each.
  - S-IC.B.4: Use data from a sample survey to estimate a population mean or proportion; develop a margin of error through the use of simulation models for random sampling.
  - S-IC.B.5: Use data from a randomized experiment to compare two treatments; use simulations to decide if differences between parameters are significant.
  - S-IC.B.6: Evaluate reports based on data.
- concept line: Put a claim on trial: the null is innocent until data proves otherwise. P-values become evidence.
- old tags: skill_key=significance-tests | action=debate | setting_group=courtroom
- read: tools/courtroom-statistics/spec.md, tools/courtroom-statistics/notes.md

## fair-dice-investigation
- title: Fair Dice Investigation | format: mystery | family: none | stage: built
- module: math-12-chi-square-and-regression-inference (math 12, Statistics): Chi-Square and Regression Inference. Inference for categorical data and slopes
- module standards: AP-STAT.U8;AP-STAT.U9
- concept line: Is the casino's die loaded? Collect counts and run chi-square to decide; then test whether a slope is real.
- old tags: skill_key=chi-square | action=investigate | setting_group=game-show
- read: tools/fair-dice-investigation/spec.md, tools/fair-dice-investigation/notes.md

## hole-hunter
- title: Hole Hunter | format: puzzle | family: none | stage: spec
- module: math-12-limits-and-continuity (math 12, Calculus): Limits and Continuity. Limits, continuity and asymptotic behavior
- module standards: AP-CALC.U1
- concept line: Find the holes, jumps and asymptotes hidden in graphs; repair them to make the function continuous.
- old tags: skill_key=continuity | action=fix | setting_group=generic
- read: tools/hole-hunter/spec.md

## speedometer
- title: Speedometer | format: simulator | family: none | stage: spec
- module: math-12-the-derivative (math 12, Calculus): The Derivative. Derivative as rate of change; rules of differentiation
- module standards: AP-CALC.U2;AP-CALC.U3
- concept line: Drive a car along a position graph; the speedometer is the derivative, drawn live.
- old tags: skill_key=derivative | action=simulate-tune | setting_group=vehicle
- read: tools/speedometer/spec.md

## optimization-workshop
- title: Optimization Workshop | format: builder | family: none | stage: spec
- module: math-12-applications-of-derivatives (math 12, Calculus): Applications of Derivatives. Related rates, optimization and curve sketching
- module standards: AP-CALC.U4;AP-CALC.U5
- concept line: Fence the biggest field, design the cheapest can; derivatives find the best design, and a slider proves it.
- old tags: skill_key=optimization | action=build | setting_group=garden-farm
- read: tools/optimization-workshop/spec.md

## rain-gauge
- title: Rain Gauge | format: simulator | family: none | stage: spec
- module: math-12-the-integral (math 12, Calculus): The Integral. Riemann sums, accumulation and the Fundamental Theorem
- module standards: AP-CALC.U6
- concept line: Rainfall rate over a day fills a tank; Riemann rectangles approximate the total as they get thinner.
- old tags: skill_key=integral | action=simulate-tune | setting_group=weather
- read: tools/rain-gauge/spec.md

## solid-spinner
- title: Solid Spinner | format: explorer | family: none | stage: spec
- module: math-12-applications-of-integrals (math 12, Calculus): Applications of Integrals. Area, volume and motion
- module standards: AP-CALC.U8
- concept line: Spin regions around an axis to make solids; stack disks and washers to find volume.
- old tags: skill_key=volumes-of-revolution | action=explore | setting_group=generic
- read: tools/solid-spinner/spec.md

## slope-field-garden
- title: Slope Field Garden | format: sandbox | family: none | stage: spec
- module: math-12-differential-equations (math 12, Calculus): Differential Equations. Slope fields and exponential models
- module standards: AP-CALC.U7
- concept line: Plant seeds in a slope field and watch solution curves grow; model population and cooling.
- old tags: skill_key=differential-equations | action=explore | setting_group=garden-farm
- read: tools/slope-field-garden/spec.md

## fire-lookout-triangles
- title: Fire Lookout Triangles | format: map | family: none | stage: built
- module: math-12-solving-any-triangle (math 12, Trigonometry): Solving Any Triangle. Law of sines, law of cosines and the area of any triangle
- module standards: G-SRT.D
- standard texts (filed wording; a bare cluster is spelled out):
  - G-SRT.D.9: (+) Derive the formula A = 1/2 ab sin(C) for the area of a triangle by drawing an auxiliary line from a vertex perpendicular to the opposite side.
  - G-SRT.D.10: (+) Prove the Laws of Sines and Cosines and use them to solve problems.
  - G-SRT.D.11: (+) Understand and apply the Law of Sines and the Law of Cosines to find unknown measurements in right and non-right triangles (e.g., surveying problems, resultant forces).
- concept line: Two fire lookouts spot the same smoke; use their bearings and the distance between towers to find the fire with the law of sines, then a third tower checks the answer with the law of cosines.
- old tags: skill_key=law-of-sines-cosines | action=locate | setting_group=nature
- read: tools/fire-lookout-triangles/spec.md, tools/fire-lookout-triangles/notes.md

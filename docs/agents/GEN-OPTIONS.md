# Worksheet Generators: every setting and its values

Generated from site/assets/gen/*.js. A generator-backed concept row (data/closet/worksheets/generated.csv) uses these ids and values in its query string.

## number-ops: Number Operations (grades K-5)

Addition, subtraction, multiplication and division, from facts within 10 to long division, with or without regrouping.

- **grade** (Grade; default "2"): k (Kindergarten), 1 (Grade 1), 2 (Grade 2), 3 (Grade 3), 4 (Grade 4), 5 (Grade 5)
- **skill** (Skill; default "add"): add (Addition), sub (Subtraction), addsub (Addition and subtraction)
  - when grade=3: add (Addition), sub (Subtraction), mul (Multiplication facts), div (Division facts), muldiv (Multiplication and division), mix (All four)
  - when grade=4: add (Addition), sub (Subtraction), mul (Multiplication), div (Division with remainders), mix (All four)
  - when grade=5: mul (Multiplication), div (Long division), dec (Adding and subtracting decimals), mix (All four)
- **regroup** (Regrouping, only in some modes; default "any"): any (Some with, some without), with (Every problem regroups), without (No regrouping)
- **count** (Problems; default "20"): 12 (12), 20 (20), 24 (24)

## fractions: Fractions (grades 3-7)

Equivalent fractions, comparing, adding, subtracting, multiplying and dividing, with fraction pictures for the younger grades.

- **grade** (Grade; default "4"): 3 (Grade 3), 4 (Grade 4), 5 (Grade 5), 6 (Grade 6), 7 (Grade 7)
- **skill** (Skill; default "equiv"): equiv (Equivalent fractions), compare (Compare fractions), addlike (Add and subtract, like denominators), mixed (Add and subtract mixed numbers), mulwhole (Multiply a fraction by a whole number)
  - when grade=3: line (Fractions on a number line), pic (Name the shaded fraction), equiv (Equivalent fractions with pictures), compare (Compare fractions with pictures)
  - when grade=5: addunlike (Add and subtract, unlike denominators), mul (Multiply fractions), divunit (Divide unit fractions and whole numbers), mix5 (Mixed review)
  - when grade=6: div (Divide fractions by fractions), all6 (All four operations)
  - when grade=7: negas (Add and subtract with negatives), negmd (Multiply and divide with negatives), negall (All four operations with negatives)
- **count** (Problems; default "m"): s (Fewer (12)), m (Standard (16)), l (More (20))
  - when grade=3: s (Fewer (4)), m (Standard (6)), l (More (8))
  - when grade=5: s (Fewer (8)), m (Standard (12)), l (More (16))
  - when grade=6: s (Fewer (8)), m (Standard (12)), l (More (16))
  - when grade=7: s (Fewer (8)), m (Standard (12)), l (More (16))

## equations: Expressions and Equations (grades 6-9)

Evaluate expressions, then solve one-step, two-step and both-sides equations and inequalities. The key shows each step.

- **grade** (Grade; default "7"): 6 (Grade 6), 7 (Grade 7), 8 (Grade 8), 9 (Grade 9 (Algebra 1))
- **skill** (Skill; default "two"): eval (Evaluate expressions with integers), two (Two-step equations), dist (Distributive property equations), ineq2 (Two-step inequalities), mix (Mixed review)
  - when grade=6: eval (Evaluate expressions), one (One-step equations), ineq1 (One-step inequalities), mix (Mixed review)
  - when grade=8: two (Two-step equations), both (Variables on both sides), dist (Distributive property equations), ineq2 (Two-step inequalities), mix (Mixed review)
  - when grade=9: both (Variables on both sides), multi (Multi-step equations), ineq (Multi-step inequalities), mix (Mixed review)
- **count** (Problems; default "m"): s (Fewer (6)), m (Standard (8)), l (More (12))
  - when grade=6: s (Fewer (8)), m (Standard (12)), l (More (16))

## measure-shapes: Area, Perimeter and Volume (grades 2-8)

Drawn shapes with their measurements: rectangles, triangles, circles, composite shapes, boxes and cylinders.

- **grade** (Grade; default "4"): 2 (Grade 2), 3 (Grade 3), 4 (Grade 4), 5 (Grade 5), 6 (Grade 6), 7 (Grade 7), 8 (Grade 8)
- **skill** (Skill; default "ap"): ap (Area and perimeter of rectangles), compo (Composite shapes), missing (Find the missing side), mix4 (Mixed review)
  - when grade=2: perim (Perimeter of shapes)
  - when grade=3: perim (Perimeter of polygons), area (Area of rectangles), compo (Area of L-shapes), mix3 (Area and perimeter)
  - when grade=5: vol (Volume of rectangular prisms), volc (Volume of two joined boxes)
  - when grade=6: tri (Area of triangles), para (Area of parallelograms), trap (Area of trapezoids), poly (Triangles, parallelograms and trapezoids), sa (Surface area of rectangular prisms)
  - when grade=7: circ (Circumference of circles), carea (Area of circles), circles (Circumference and area)
  - when grade=8: cyl (Volume of cylinders), vol8 (Prisms and cylinders)
- **units** (Units; default "both"): metric (Metric (cm, m)), customary (Customary (in, ft)), both (Some of each)
- **pi** (Pi, only in some modes; default "3.14"): 3.14 (Use 3.14), pi (Answer in terms of π)
- **count** (Problems; default "9"): 6 (6), 9 (9), 12 (12)

## word-problems: Word Problems (grades 1-6)

Everyday stories about money, time, measurement and sharing, plus fractions, rates and percents for older grades, with room to show the work.

- **grade** (Grade; default "3"): 1 (Grade 1), 2 (Grade 2), 3 (Grade 3), 4 (Grade 4), 5 (Grade 5), 6 (Grade 6)
- **topic** (Topic; default "mix"): mix (A mix of topics), money (Money), time (Time), measure (Measurement), groups (Equal groups and sharing), multi (Multi-step)
  - when grade=1: mix (A mix of topics), join (Adding and subtracting), time (Time), measure (Measurement)
  - when grade=2: mix (A mix of topics), join (Adding and subtracting), money (Money), time (Time), measure (Measurement), groups (Equal groups and sharing)
  - when grade=5: mix (A mix of topics), money (Money), time (Time), measure (Measurement), groups (Equal groups and sharing), multi (Multi-step), frac (Fractions of amounts)
  - when grade=6: mix (A mix of topics), money (Money), time (Time), measure (Measurement), multi (Multi-step), frac (Fractions of amounts), rates (Rates and percents)
- **count** (Problems; default "6"): 4 (4), 6 (6), 8 (8)

## science-calc: Science Calculations (grades 6-12)

Density, speed, acceleration, weight, work and power, then force from grade 8 and Ohm's law, momentum and kinetic energy in high school, with the formula, units and the worked answer.

- **grade** (Grade; default "8"): 6 (Grade 6), 7 (Grade 7), 8 (Grade 8), 9 (Grade 9), 10 (Grade 10), 11 (Grade 11), 12 (Grade 12)
- **topic** (Topic; default "density"): density (Density), speed (Speed), accel (Acceleration), force (Force), weight (Weight), work (Work), power (Power), mix (Mixed review)
  - when grade=6: density (Density), speed (Speed), accel (Acceleration), weight (Weight), work (Work), power (Power), mix (Mixed review)
  - when grade=7: density (Density), speed (Speed), accel (Acceleration), weight (Weight), work (Work), power (Power), mix (Mixed review)
  - when grade=9: density (Density), speed (Speed), accel (Acceleration), force (Force), weight (Weight), work (Work), power (Power), ohm (Ohm's law), momentum (Momentum), ke (Kinetic energy), mix (Mixed review)
  - when grade=10: density (Density), speed (Speed), accel (Acceleration), force (Force), weight (Weight), work (Work), power (Power), ohm (Ohm's law), momentum (Momentum), ke (Kinetic energy), mix (Mixed review)
  - when grade=11: density (Density), speed (Speed), accel (Acceleration), force (Force), weight (Weight), work (Work), power (Power), ohm (Ohm's law), momentum (Momentum), ke (Kinetic energy), mix (Mixed review)
  - when grade=12: density (Density), speed (Speed), accel (Acceleration), force (Force), weight (Weight), work (Work), power (Power), ohm (Ohm's law), momentum (Momentum), ke (Kinetic energy), mix (Mixed review)
- **count** (Problems; default "6"): 4 (4), 6 (6), 8 (8)

## punnett: Punnett Squares (grades 7-12)

One-trait and two-trait crosses with real traits: fill the square, then give the genotype and phenotype ratios.

- **grade** (Grade; default "7"): 7 (Grade 7), 8 (Grade 8), 9 (Grade 9), 10 (Grade 10), 11 (Grade 11), 12 (Grade 12)
- **cross** (Kind of cross; default "mono"): mono (One trait (complete dominance))
  - when grade=9: mono (One trait (complete dominance)), incomplete (Incomplete dominance), codom (Codominance), sex (Sex-linked (X-linked) traits), di (Two traits (dihybrid, 4 × 4)), mix (Mixed review)
  - when grade=10: mono (One trait (complete dominance)), incomplete (Incomplete dominance), codom (Codominance), sex (Sex-linked (X-linked) traits), di (Two traits (dihybrid, 4 × 4)), mix (Mixed review)
  - when grade=11: mono (One trait (complete dominance)), incomplete (Incomplete dominance), codom (Codominance), sex (Sex-linked (X-linked) traits), di (Two traits (dihybrid, 4 × 4)), mix (Mixed review)
  - when grade=12: mono (One trait (complete dominance)), incomplete (Incomplete dominance), codom (Codominance), sex (Sex-linked (X-linked) traits), di (Two traits (dihybrid, 4 × 4)), mix (Mixed review)
- **count** (Crosses; default "3"): 3 (3), 4 (4)
- **edges** (Print the parent alleles on each square (easier); default false): 0 or 1

## graph-reading: Reading Graphs (grades 1-8)

A picture graph, bar graph, line graph or table with questions that go from reading a value to comparing and finding the mean.

- **grade** (Grade; default "3"): 1 (Grade 1), 2 (Grade 2), 3 (Grade 3), 4 (Grade 4), 5 (Grade 5), 6 (Grade 6), 7 (Grade 7), 8 (Grade 8)
- **graph** (Graph; default "bar"): picture (Picture graph), bar (Bar graph)
  - when grade=4: bar (Bar graph), line (Line graph)
  - when grade=5: bar (Bar graph), line (Line graph)
  - when grade=6: line (Line graph), dot (Table and dot plot)
  - when grade=7: line (Line graph), dot (Table and dot plot)
  - when grade=8: line (Line graph), dot (Table and dot plot)

## vocabulary: Vocabulary Practice (grades K-12)

Pick any module on the Word Wall: match words to meanings, then fill in the missing word.

- **subject** (Subject; default "science"): arts (Arts and Music), cte (Career and Technical Education), computer-science (Computer Science), ela (English Language Arts), eld (English Language Development), health-pe (Health and PE), library (Library and Research Skills), math (Math), science (Science), sel (Social and Emotional Learning), social-studies (Social Studies), world-languages (World Languages)
- **band** (Grades; default "35"): k2 (Grades K-2), 35 (Grades 3-5), 68 (Grades 6-8), 912 (Grades 9-12)
- **mod** (Word Wall module; default ""): science-3-balanced-and-unbalanced-forces (Balanced and Unbalanced Forces (grade 3)), science-3-fossils-and-changing-environments (Fossils and Changing Environments (grade 3)), science-3-life-cycles (Life Cycles (grade 3)), science-3-living-in-groups (Living in Groups (grade 3)), science-3-magnets-and-static-electricity (Magnets and Static Electricity (grade 3)), science-3-traits-and-variation (Traits and Variation (grade 3)) ... 21 options
- **mod2** (Add a second module (optional); default ""):  (None), science-3-fossils-and-changing-environments (Fossils and Changing Environments (grade 3)), science-3-life-cycles (Life Cycles (grade 3)), science-3-living-in-groups (Living in Groups (grade 3)), science-3-magnets-and-static-electricity (Magnets and Static Electricity (grade 3)), science-3-traits-and-variation (Traits and Variation (grade 3)) ... 21 options
- **count** (Words; default "6"): 6 (6 words), 8 (8 words), 10 (10 words)

## word-puzzles: Word Puzzles (grades 1-12)

A word search or crossword made from any module's Word Wall words, with the meanings as clues.

- **subject** (Subject; default "science"): arts (Arts and Music), cte (Career and Technical Education), computer-science (Computer Science), ela (English Language Arts), eld (English Language Development), health-pe (Health and PE), library (Library and Research Skills), math (Math), science (Science), sel (Social and Emotional Learning), social-studies (Social Studies), world-languages (World Languages)
- **band** (Grades; default "35"): k2 (Grades 1-2), 35 (Grades 3-5), 68 (Grades 6-8), 912 (Grades 9-12)
- **mod** (Word Wall module; default ""): science-3-balanced-and-unbalanced-forces (Balanced and Unbalanced Forces (grade 3)), science-3-fossils-and-changing-environments (Fossils and Changing Environments (grade 3)), science-3-life-cycles (Life Cycles (grade 3)), science-3-living-in-groups (Living in Groups (grade 3)), science-3-magnets-and-static-electricity (Magnets and Static Electricity (grade 3)), science-3-traits-and-variation (Traits and Variation (grade 3)) ... 21 options
- **mod2** (Add a second module (optional); default ""):  (None), science-3-fossils-and-changing-environments (Fossils and Changing Environments (grade 3)), science-3-life-cycles (Life Cycles (grade 3)), science-3-living-in-groups (Living in Groups (grade 3)), science-3-magnets-and-static-electricity (Magnets and Static Electricity (grade 3)), science-3-traits-and-variation (Traits and Variation (grade 3)) ... 21 options
- **kind** (Puzzle; default "search"): search (Word search), cross (Crossword)
- **list** (Word search list, only in some modes; default "words"): words (Words with their meanings), clues (Meanings only (students work out each word))
- **count** (Words; default "8"): 6 (6 words), 8 (8 words), 10 (10 words)

## map-skills: Map Skills (grades 1-6)

A made-up town on a grid with a compass rose, a key and a scale: find places, give directions and measure distances.

- **grade** (Grade; default "3"): 1 (Grade 1), 2 (Grade 2), 3 (Grade 3), 4 (Grade 4), 5 (Grade 5), 6 (Grade 6)

## timeline: Timelines (grades 2-12)

Put real events in order on a timeline, from inventions to U.S. and world history, then count the years between them.

- **grade** (Grade; default "5"): 2 (Grade 2), 3 (Grade 3), 4 (Grade 4), 5 (Grade 5), 6 (Grade 6), 7 (Grade 7), 8 (Grade 8), 9 (Grade 9), 10 (Grade 10), 11 (Grade 11), 12 (Grade 12)
- **set** (Events; default "inv"): inv (Inventions and technology), space (Space exploration), sci (Science discoveries), us1 (U.S. history: to 1800), us2 (U.S. history: 1800 to 1877), us3 (U.S. history: 1877 to today), usall (U.S. history: all eras), w2 (World history: 500 to 1750), w3 (World history: 1750 to today), wall (World history: all eras), life (My own life (a blank timeline))
  - when grade=6: inv (Inventions and technology), space (Space exploration), sci (Science discoveries), us1 (U.S. history: to 1800), us2 (U.S. history: 1800 to 1877), us3 (U.S. history: 1877 to today), usall (U.S. history: all eras), w1 (World history: ancient world, to 500 CE), w2 (World history: 500 to 1750), w3 (World history: 1750 to today), wall (World history: all eras), life (My own life (a blank timeline))
  - when grade=7: inv (Inventions and technology), space (Space exploration), sci (Science discoveries), us1 (U.S. history: to 1800), us2 (U.S. history: 1800 to 1877), us3 (U.S. history: 1877 to today), usall (U.S. history: all eras), w1 (World history: ancient world, to 500 CE), w2 (World history: 500 to 1750), w3 (World history: 1750 to today), wall (World history: all eras), life (My own life (a blank timeline))
  - when grade=8: inv (Inventions and technology), space (Space exploration), sci (Science discoveries), us1 (U.S. history: to 1800), us2 (U.S. history: 1800 to 1877), us3 (U.S. history: 1877 to today), usall (U.S. history: all eras), w1 (World history: ancient world, to 500 CE), w2 (World history: 500 to 1750), w3 (World history: 1750 to today), wall (World history: all eras), life (My own life (a blank timeline))
  - when grade=9: inv (Inventions and technology), space (Space exploration), sci (Science discoveries), us1 (U.S. history: to 1800), us2 (U.S. history: 1800 to 1877), us3 (U.S. history: 1877 to today), usall (U.S. history: all eras), w1 (World history: ancient world, to 500 CE), w2 (World history: 500 to 1750), w3 (World history: 1750 to today), wall (World history: all eras), life (My own life (a blank timeline))
  - when grade=10: inv (Inventions and technology), space (Space exploration), sci (Science discoveries), us1 (U.S. history: to 1800), us2 (U.S. history: 1800 to 1877), us3 (U.S. history: 1877 to today), usall (U.S. history: all eras), w1 (World history: ancient world, to 500 CE), w2 (World history: 500 to 1750), w3 (World history: 1750 to today), wall (World history: all eras), life (My own life (a blank timeline))
  - when grade=11: inv (Inventions and technology), space (Space exploration), sci (Science discoveries), us1 (U.S. history: to 1800), us2 (U.S. history: 1800 to 1877), us3 (U.S. history: 1877 to today), usall (U.S. history: all eras), w1 (World history: ancient world, to 500 CE), w2 (World history: 500 to 1750), w3 (World history: 1750 to today), wall (World history: all eras), life (My own life (a blank timeline))
  - when grade=12: inv (Inventions and technology), space (Space exploration), sci (Science discoveries), us1 (U.S. history: to 1800), us2 (U.S. history: 1800 to 1877), us3 (U.S. history: 1877 to today), usall (U.S. history: all eras), w1 (World history: ancient world, to 500 CE), w2 (World history: 500 to 1750), w3 (World history: 1750 to today), wall (World history: all eras), life (My own life (a blank timeline))

## organizer: Graphic Organizer Maker (grades K-12)

Type your topic and pick a layout: compare, cause and effect, main idea, sequence, claim and evidence, and more.

- **layout** (Layout; default "venn2"): venn2 (Venn diagram, 2 circles), venn3 (Venn diagram, 3 circles), compare (Compare and contrast chart), cause (Cause and effect), chain (Cause chain), main (Main idea and details), sequence (Sequence / flow chart), cer (Claim, evidence, reasoning), kwl (KWL chart), problem (Problem and solution), web (Concept web), story (Story map), frayer (Frayer model)
- **band** (Grade band; default "35"): k2 (Grades K-2), 35 (Grades 3-5), 68 (Grades 6-8), 912 (Grades 9-12)
- **topic** (Topic or title (optional); default ""): free text (120 chars)
- **starters** (Add sentence starters; default false): 0 or 1

## writing-frame: Writing Frames (grades 1-12)

Opinion, informative, narrative, science claim-evidence-reasoning, compare and summary frames, built for the grade, with fresh starters and a standards checklist.

- **grade** (Grade; default "4"): 1 (Grade 1), 2 (Grade 2), 3 (Grade 3), 4 (Grade 4), 5 (Grade 5), 6 (Grade 6), 7 (Grade 7), 8 (Grade 8), 9 (Grade 9), 10 (Grade 10), 11 (Grade 11), 12 (Grade 12)
- **genre** (Kind of writing; default "opinion"): opinion (Opinion / argument), informative (Informative / explanatory), narrative (Narrative), cer (Claim, evidence, reasoning (science)), compare (Compare and contrast), summary (Summary)
- **topic** (Topic or prompt (optional); default ""): free text (120 chars)
- **space** (Writing space; default "plan"): plan (Planning frame (1 page)), draft (Drafting frame (2 pages))

## planner-log: Planners, Logs and Reflections (grades K-12)

Project planners, reading, practice and science logs, weekly and exit reflections, and goal setting (SMART from grade 6), sized for the grade.

- **kind** (Kind; default "reading"): project (Project planner), reading (Reading log), practice (Practice log), science (Science observation log), weekly (Weekly reflection), exit (Exit reflection (2 slips)), goal (Goal setting)
- **band** (Grade band; default "35"): k2 (Grades K-2), 35 (Grades 3-5), 68 (Grades 6-8), 912 (Grades 9-12)
- **topic** (Title, skill or topic (optional); default ""): free text (120 chars)


# Poll Workshop

## One idea
Poll an invented town whose true answer is hidden, then reveal it: a bigger sample shrinks the plus or minus, but only
a fair method puts the headline near the truth, and a biased poll of 2,000 people can be confidently wrong.

## Not like
- jellybean-jar (grade 7, same family): there, bigger samples get closer to the truth. Here the point is the case
  where they do not: bias does not shrink with sample size, and the printed margin of error does not cover it.
- sample-machine (grade 12, same family): there, thousands of fair samples build a sampling distribution and the
  Central Limit Theorem. Here repeats are only a check on one poll design; the subject is how people get chosen and
  asked, and what the headline says.
- design-the-study (grade 12): a story about experiments, with an editor reviewing choices. Here it is surveys, a
  live town you can sample over and over, and no narrative judge.
- medical-test-paradox (grade 10): conditional probability on one population. No sampling or survey design there.

## Who and how
Grade 11 math (Statistics and Probability: Statistical Inference). Students drive on their own laptops; also works on
a projector for whole-class discussion. 20 to 40 minutes. Standards: S-IC.A.1, S-IC.B.3, S-IC.B.4, S-ID.A.4.
Band 9-12 look: link `kit:curio` then `kit:theme-912`; tool accent `--brand` is a newsprint amber. No confetti, no
mascot, no score.

## Screens and modes
Header: title "Poll Workshop", mode buttons (`.seg`) **Workshop**, **Case file**, **Budget desk**, then the kit icon
buttons **Motion**, **Sound**, **Read**.

Layout (all modes): stage on the left with the **Millbrook map** on top and the **Headline wall** below it; panel on
the right.

### Workshop (default, pure explore)
- Map: Millbrook drawn in code, four labeled neighborhoods, block grid lines, a river; 20,000 residents as tiny grey
  dots (opinions hidden). After a poll, the people asked are ringed: supporters as filled dots with a check mark,
  opposers as hollow dots with an x (shape, not only color).
- Panel, "Design your poll":
  - **Who you ask**: eight method buttons, each with its one-line description from Content (Simple random,
    Stratified, Cluster, Systematic, Mall on Saturday, Online poll, Daytime phone calls, Mail to car and phone owners).
  - **How you ask**: three wording buttons (Neutral, Leans yes, Leans no); the full question text shows under them.
  - **How many**: slider with stops 20, 50, 100, 200, 400, 600, 1000, 1500, 2000; readout "n = 400".
  - Buttons: **Run poll**, **Run 50 more like this**, **Reveal the truth** (toggle; label becomes **Hide the truth**),
    **Clear wall**, **New town**.
- Panel, "Results" (after a run): "212 of 400 said yes", the percent to one decimal, "plus or minus 4.9 points",
  and a newspaper headline card. A **Who answered** table: age bands and neighborhoods, sample percent next to town
  percent, with a small paired bar for each row.
- Headline wall: a horizontal 0 to 100 percent axis with a dashed 50 percent line. Each poll run adds one dot,
  stacked in its 1-point bin; the newest dot shows its plus-or-minus bar (any dot's bar on hover or focus). A **Show**
  dropdown: "All methods" or any one method. A **Normal curve** toggle fits a normal curve (mean and sd of the dots
  shown) and shades its middle 95 percent.
- When the truth is revealed: a solid vertical truth line labeled "True support: 44.6 percent (neutral question)",
  plus readouts "Newest poll off by 3.1 points", "Inside its plus or minus: yes" (or no), and for the dots shown
  "Plus or minus caught the truth: 47 of 51 polls".

### Case file
- Panel shows the 1936 Literary Digest case card (text in Content) and two buttons: **Run the Digest's method in
  Millbrook** (loads Mail to car and phone owners, Neutral, n = 2000, runs 20 times) and **Run a fair method in
  Millbrook** (loads Stratified, Neutral, n = 2000, runs 20 times). The truth is revealed automatically once both
  have run. Show dropdown is set to "All methods".
- Three discussion prompts under the card (Content). Map and wall behave as in Workshop. Nothing to answer, no score.

### Budget desk (optional challenge)
- Brief: "The Millbrook Courier gives you $10,000. Publish one headline you can stand behind."
- Same design panel plus a **Cost** readout (cost per response times n, from Content). Over budget, the readout
  says "Over budget by $2,000" and **Publish** is disabled. **Run poll** and **Run 50 more** are replaced by
  **Publish**: one publish per round, no repeats, truth hidden until then.
- After Publish: the truth is revealed with two plain checks: "Truth inside your plus or minus: yes/no" and
  "Headline verdict right: yes/no". The verdict is right when the headline's word matches the truth: "backs" if the
  truth is above 52 percent, "says no" if below 48, "split" if 48 to 52.
  Then **Next round** (new hidden town).
- Three rounds (Content). A round log lists each round's design, result, truth and the two checks. **Start over**
  clears the log and returns to round 1. No points, no stars.

## Content

### Millbrook (invented; the tool says so on screen)
On-screen note: "Millbrook is invented, so its true answer can be known. Its numbers are made up to show how polls
behave; real bias sizes vary."

The question (neutral): "Do you support or oppose building a skate park at Riverside Park?"

Neighborhoods (residents; blocks of 100; age shares 18-29 / 30-49 / 50-64 / 65+ in percent; opinion shift):
- Downtown: 6,000; 60 blocks; 35 / 35 / 18 / 12; +6 points
- Riverside: 5,000; 50 blocks; 20 / 40 / 25 / 15; +4 points
- Hillside: 4,000; 40 blocks; 10 / 30 / 30 / 30; -10 points
- Eastfield Farms: 5,000; 50 blocks; 15 / 30 / 30 / 25; -8 points

Base support by age: 18-29: 72 percent; 30-49: 52; 50-64: 36; 65+: 24.
Block effect: each block gets a shift drawn from a normal distribution with sd 10 points.
Each resident's chance of support = base(age) + shift(neighborhood) + shift(block) + town offset, clamped to 2 to 98
percent. Their opinion is drawn once at town creation and stays fixed. The shown truth is always computed from the
actual residents. (A test simulation of this model gave a truth of 44.6 percent with offset 0.)

Other resident traits, drawn at creation:
- On the car and phone list: Downtown 30 percent, Riverside 50, Hillside 90, Eastfield 75; halved for age 18-29.
- Shops at the mall on Saturday: 18-29: 45 percent; 30-49: 30; 50-64: 15; 65+: 10.

### Methods (button description; sampling rule; what a test simulation showed at n = 2000 with truth 44.6)
1. Simple random: "The computer picks names at random from the full town list." n residents without replacement.
2. Stratified: "Random picks inside each neighborhood, in proportion to its size." 30 / 25 / 20 / 25 percent of n.
3. Cluster: "Pick random blocks, then ask people on those blocks." m = max(2, ceil(n / 40)) blocks, capped at 200;
   n split evenly across them (remainder one each to the first blocks). Centered on the truth but about twice as
   spread out as simple random; its intervals caught the truth only about 63 percent of the time.
4. Systematic: "Every k-th house on the street list, from a random start." List ordered by neighborhood, block,
   house; k = floor(20000 / n); start uniform in 0 to k minus 1.
5. Mall on Saturday: "Stop shoppers at the Downtown mall." Weighted draw: weight = 1 if shops on Saturday else 0.05,
   times 1.5 if Downtown. About 54 percent.
6. Online poll: "Post it on the town page; whoever answers counts." Weighted draw: supporters 8, opposers 3, times
   age factor 18-29: 1.5, 30-49: 1.0, 50-64: 0.6, 65+: 0.3. About 75 percent.
7. Daytime phone calls: "Call homes on a weekday afternoon." Weighted draw by age: 18-29: 5, 30-49: 8, 50-64: 15,
   65+: 35. About 33 percent.
8. Mail to car and phone owners: "Mail ballots to people on car and phone lists, count what comes back." Only
   residents on the list (about 10,500); weight 1.5 for opposers, 1 for supporters. About 30 percent.

Weighted draws without replacement use the key method: key = u to the power 1/w with u uniform, take the n largest.

### Wording (the full question shown)
- Neutral: "Do you support or oppose building a skate park at Riverside Park?" No change.
- Leans yes: "Would you support a skate park that gives local teens a safe place to go?" Each opposer answers yes
  with chance 15 percent (about +8 points).
- Leans no: "Should the town spend $1.2 million of taxpayer money on a skate park?" Each supporter answers no with
  chance 20 percent (about -9 points).
Flips are drawn fresh on every run. The truth line always uses the neutral question.

### Numbers shown
- p-hat = yes / n. Margin of error (95 percent) = 1.96 times the square root of (p-hat times (1 minus p-hat) / n), in
  points, one decimal; if p-hat is 0 or 1, use 0.5 in the formula. Every method gets this simple random formula,
  because that is what published polls print. The tool's info line says so.
- n under 30: add "Too few people to trust a plus or minus."

### Headlines (newspaper card)
- p-hat minus MOE above 50: "Poll: Millbrook backs skate park, 58 to 42"
- p-hat plus MOE below 50: "Poll: Millbrook says no to skate park, 41 to 59"
- otherwise: "Poll: Millbrook split on skate park"
- Dateline under it: "Millbrook Courier. Survey of 400 residents, plus or minus 4.9 points."
Numbers are rounded whole percents and always add to 100.

### Cost per response (Budget desk)
Simple random $25, Stratified $25, Systematic $25, Cluster $8, Daytime phone calls $6, Mall on Saturday $3, Mail to
car and phone owners $2, Online poll $0.

### Budget desk rounds
- Round 1: new seed, town offset uniform from -12 to +12 points.
- Round 2: same rule, new seed.
- Round 3, "Close race": redraw until the truth is between 48 and 52 percent.

### Case file text (1936)
"In 1936 the Literary Digest mailed about 10 million straw ballots, with names drawn largely from telephone
directories and car registration lists, plus its own subscribers. About 2.4 million came back. The Digest predicted
Alf Landon would beat Franklin Roosevelt, 57 percent to 43 percent. Roosevelt won with 60.8 percent of the popular
vote to Landon's 36.5 percent, and 523 electoral votes to 8. George Gallup, with a much smaller sample chosen to
match the voting public, called a Roosevelt win. In 1936, people with phones and cars were better off than most
voters, and the people who mailed ballots back were not a random slice either."
Prompts:
1. "Two million answers and still wrong: what did the Digest's sample miss?"
2. "Which Millbrook method copies the Digest, and what does its plus or minus claim?"
3. "Why can a few thousand well-chosen people beat millions?"

### Town seeds
Default town: seed 1936, offset 0. **New town** in Workshop picks a new seed and an offset from -12 to +12, clears
the wall and hides the truth.

## Interactions in detail
- Changing method, wording or n runs nothing; the next run uses the new design.
- Run poll: picks the sample, rings those dots on the map (rings fade in over about 0.6 s; Motion off: at once),
  fills Results and adds one wall dot.
- Run 50 more: 50 runs of the current design; dots drop onto the wall in sequence over about 2 s (Motion off: all
  at once). Results show the last run. The wall keeps at most 500 dots; the oldest are dropped.
- Wall dots are focusable (Tab to the wall, arrow keys move between dots): tooltip with method, wording, n, percent,
  plus or minus, and that dot's bar.
- Reveal only shows or hides; it never changes data. New town and Clear wall hide the truth again.
- Normal curve needs 10 or more dots shown; fewer shows "Run at least 10 polls of this design."
- Extremes: Systematic at n = 2000 gives k = 10, at n = 20 gives k = 1000. Cluster at n = 20 uses 2 blocks of 10;
  at n = 2000, 50 blocks of 40. Online poll at n = 2000 still pulls 2,000 distinct people. The mail frame (about
  10,500) is larger than any n.
- Who answered: sample vs town percents by age band and neighborhood; the row with the biggest gap is outlined.
- Mode switch calls Curio.stop(). The Workshop wall survives switching to Case file and back; Budget desk has its
  own wall, one dot per round.
- Hint line (`#hint`) follows the step: at start "Pick who you ask, then press Run poll."; after 3 runs "Try Run 50
  more like this, then Reveal the truth."; after a reveal while a biased method (5 to 8) is selected "More people
  will not fix this. Try n = 2000 and see."
- All buttons at least 44 px, everything works by keyboard, and the wall has a text alternative listing its values.
- The town and sampling logic live in one clearly marked block `/* SAMPLING ENGINE (family: sampling) */` so it can
  later become `kit/sampling.js`. Use a seeded PRNG (for example mulberry32) so the default town is identical on
  every load. One Run 50 at n = 2000 must finish in well under a second on a school laptop.

## Art
- newsprint: "aged newsprint paper texture, faint fibers, soft off-white, flat even lighting, no text, no letters";
  4:1; cutout no; people no. Used behind the headline card.
Everything else (map, dots, wall, bars, curve) is drawn in code.

## Voice
Bank "hs-narrator", voice "Kore", style "Read clearly and naturally, at a moderate pace".
1. welcome-workshop: "Welcome to Millbrook. Every one of these dots knows how they feel about a new skate park. You only get to ask some of them."
2. how-to: "Pick who you ask, how you ask, and how many. Then run the poll and read your headline."
3. run-more: "One poll can be lucky. Run the same design fifty more times and see where the results land."
4. reveal: "Here is the truth. A fair method scatters around it. A biased one lands off to the side, and more people will not move it back."
5. moe: "The plus or minus only covers the luck of the draw. It says nothing about who you left out."
6. welcome-case: "In nineteen thirty six, a magazine polled more than two million people and still called the election wrong. Let's see why."
7. case-after: "Same town, same number of people. The only difference is who got asked."
8. welcome-budget: "The Millbrook Courier has ten thousand dollars for a poll. Spend it on the design you trust most."
9. close-race: "This one is close. Think about how small your plus or minus needs to be."
10. publish: "Published. Let's see how it held up."
Line 1 plays on first entering Workshop, 2 after it, 3 after the first Run poll, 4 and 5 on the first reveal, 6 on
entering Case file, 7 after both case runs, 8 on entering Budget desk, 9 at round 3, 10 on each Publish.

## Family engine
Family sampling has no engine or doc yet. Keep it self-contained in the marked SAMPLING ENGINE block: seeded town
builder, simple random, stratified, cluster, systematic and weighted draws, p-hat and margin of error. Charts are the
tool's own (this tool is not in the data-desk family). Uses kit `curio.js`, `curio.css` and `theme-912`.

## Sources
- Literary Digest 1936: about 10 million mailed, about 2.4 million returned, phone and car lists, 57 to 43 Landon
  forecast, and the frame plus nonresponse explanation: Squire, Peverill (1988), "Why the 1936 Literary Digest Poll
  Failed," Public Opinion Quarterly 52(1): 125-133, https://doi.org/10.1086/269085
- 1936 popular vote, Roosevelt 60.8 percent, Landon 36.5 percent: Office of the Clerk, US House, "Statistics of the
  Presidential and Congressional Election of November 3, 1936," https://history.house.gov/Institution/Election-Statistics/
- 1936 electoral vote 523 to 8: National Archives, https://www.archives.gov/electoral-college/1936
- Gallup's smaller, representative sample calling a Roosevelt win: Squire (1988) above.
- Margin of error formula and that it covers sampling error only: Pew Research Center (2016), "5 key things to know
  about the margin of error in election polls,"
  https://www.pewresearch.org/short-reads/2016/09/08/understanding-the-margin-of-error-in-election-polls/
- Question wording effects: Pew Research Center, "Writing Survey Questions,"
  https://www.pewresearch.org/our-methods/u-s-surveys/writing-survey-questions/
- Sampling methods, convenience and voluntary response bias, nonresponse: Diez, Cetinkaya-Rundel, Barr, OpenIntro
  Statistics, 4th ed. (CC BY-SA), sections 1.3 and 1.4, https://www.openintro.org/book/os/
- Millbrook and all its numbers: invented for this tool (stated on screen).

## Done when
1. The default town shows the same truth on every reload, between 43 and 47 percent.
2. Simple random, n = 1000, Run 50 more: dots center within 1.5 points of the truth, and "caught the truth" reads
   about 44 to 51 of 51.
3. Mail to car and phone owners, n = 2000, 50 runs: dots sit at least 10 points below the truth and almost none of
   the intervals catch it, while the printed plus or minus is about 2 points.
4. Moving n from 100 to 2000 on a biased method narrows the spread but does not move its center toward the truth.
5. With Simple random, Leans yes and Leans no move results about 8 points up and 9 points down from the truth.
6. Cluster's dots spread visibly wider than Simple random at the same n, and its catch rate is clearly below 95
   percent (about 30 to 40 of 51).
7. Case file buttons each run 20 polls, the truth appears after both, and the case text matches Sources.
8. Budget desk disables Publish over $10,000, reveals the truth only after Publish, round 3's truth is between 48 and
   52, and there is no score or celebration.
9. Supporter and opposer marks differ in shape, the whole tool works by keyboard, and Motion off shows results at
   once.
10. Headlines follow the three rules exactly, and no em dashes appear anywhere in the tool's text.

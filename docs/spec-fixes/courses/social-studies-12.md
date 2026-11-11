# Spec fixes: social-studies, grade 12

22 tools: 4 rework, 14 small addition, 4 fine. How to use this file: ../README.md. When a spec is fixed, add a line to ../done.txt.

Kinds of fix in this course: Write the spec (1), Hand the key step to the student (5), Close the guessable check (14), Add the missing part (18), Add a check (3), Reach five items that differ (10), Put it on the main path (1), Sensitivity read (10), Source the facts (1).

Shape for this course: ../../agents/catalog/shape/social-studies-12.md.

## Jury Room

- Spec: `tools/jury-room/spec.md` . Module: social-studies-12-jury-room. Stage: spec only. Sort: **rework**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Reach five items that differ.
- Checks a student can pass by guessing:
  - Deliberation meter names unheard jurors and unused exhibits, so asking each in turn and citing each exhibit fills it mechanically
- **AASL.Collaborate** (practiced, in Deliberation (solo with computer jurors; Twelve seats real)): Draws out quiet jurors and builds on points before the vote
  - Parts of the standard the student never does (must add):
    - contribute to a real group discussion (solo play uses computer jurors)
    - involve diverse perspectives in own inquiry (jurors are given)
- **D2.Civ.9.9-12** (shown, in Other processes): Watches town hall and consensus circle run; fills a fit comparison
  - To do: the tool does the "use" step: the student must do it
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - use the town hall and circle themselves (scenes are played)
- The read was unsure about (check these against the spec; the read may be wrong):
  - AASL.Collaborate wording taken from the spec's paraphrase of III.A.3, III.C.2, III.D.1 and not checked against the standard
  - Civ.9 set shown because scenes are played; if the child takes part in the town hall it would be practiced
  - Twelve seats mode is the real collaboration but is off the solo main path

## One More Hour

- Spec: `tools/one-more-hour/spec.md` . Module: social-studies-12-scarcity-and-choice. Stage: spec only. Sort: **rework**.
- Fixes: Hand the key step to the student, Add the missing part, Reach five items that differ.
- **D2.Eco.2.9-12** (taught, in Saturday; the argument): Place Dani's hours, mark where extra benefit drops below extra cost, write a checked argument
  - Parts of the standard the student never does (small, add if cheap):
    - marginal figures for the town policies are not given, so the argument's margin is asserted
- **D2.Eco.1.9-12** (shown, in Surprises; Millbrook council): React to three surprises; read four groups' gains and losses for three town policies
  - To do: the tool does the "analyze" step: the student must do it
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - work out which groups gain or lose (the town board shows them)
    - explain why a group changes its choice
- The read was unsure about (check these against the spec; the read may be wrong):
  - D2.Eco.1 depth shown because the town board does the group analysis; surprises are practiced without a check but the day total shows lost value
  - Can it be beaten? hours row relies on the stop mark but stop mark has no stated key

## Go Along?

- Spec: `tools/go-along/spec.md` . Module: social-studies-12-social-psychology-and-mental-health. Stage: spec only. Sort: **rework**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Sensitivity read.
- Checks a student can pass by guessing:
  - Ethics ratings: rate everything fine; spec says each rating shows today's rule and asks a reason, but no check on the reason
- **APA.Sociocultural** (shown, in Line task; Conditions; Bystander and Obedience rooms; Ethics): Take line task, change conditions, rate each study's ethics
  - To do: the tool does the "investigate" step: the student must do it
  - Parts of the standard the student never does (must add):
    - culture and group identity
    - attitudes and prejudice
    - student predicting each result before reveal
    - explaining conformity in own words
- The read was unsure about (check these against the spec; the read may be wrong):
  - standard wording taken only from what the spec quotes, not filed text
  - shown chosen because the tool presents the published findings; the ethics rating (practiced) is only one part
  - the line task is skippable so it may not be on the path
  - ethics rating check is self-guide because the reason is a free typed field

## Concert Ticket Market

- Spec: `tools/concert-ticket-market/(no spec.md yet)` . Module: social-studies-12-supply-and-demand. Stage: LIVE (the code changes after the spec). Sort: **rework**.
- Fixes: Write the spec, Hand the key step to the student, Close the guessable check, Add the missing part, Add a check, Reach five items that differ.
- Checks a student can pass by guessing:
  - Tour: three nights per city with free tries and a line-or-empty-seats message that says which way to move, so halving the price range reaches a high revenue score without the model
- **D2.Eco.3.9-12** (practiced, in Explore): Drag the price and try four scenarios; read where the price line crosses demand
  - To do: no check: add one where thinking is cheaper than guessing
  - Parts of the standard the student never does (must add):
    - explain (nothing is written or said in the tool; the exit card is on paper)
- **D2.Eco.4.9-12** (practiced, in Tour): Set a price each night on tour and find each city's demand from sales
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - explain (the student adjusts price but does not explain the change)
- **D2.Eco.8.9-12** (shown, in Explore scenarios): Press Price cap $75 and watch the line and the empty seats
  - To do: the tool does the "describe" step: the student must do it
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - the student predicts nothing before the cap plays
    - evaluate or describe the cap's effect in the tool
- The read was unsure about (check these against the spec; the read may be wrong):
  - no spec exists; read notes.md, plan.md and tool.json only
  - wording of D2.Eco.3, D2.Eco.4 and D2.Eco.8 not given in the files; Eco.4 here is supply-demand per plan.md but the-buyout spec quotes D2.Eco.4 as competition
  - D2.Eco.8 is not in plan.md focus; assumed to be the price cap scenario
  - no src read; depth of Explore not checked against code beyond a grep for tour and score
  - words for texts not applicable

## Brain Explorer

- Spec: `tools/brain-explorer/spec.md` . Module: social-studies-12-brain-and-behavior. Stage: spec only. Sort: **small addition**.
- Fixes: Add the missing part, Sensitivity read.
- **APA.Biological** (taught, in Cases; neuron zoom; body map; case quiz): Predict what each case's damage changes, fire a neuron, add a substance, trace the near miss, name region and system
  - Parts of the standard the student never does (must add):
    - methods used to study the brain (a how-we-know tag is read, not done)
    - endocrine system beyond adrenaline and cortisol in one stress scene
    - brain structures beyond six regions
- The read was unsure about (check these against the spec; the read may be wrong):
  - APA.Biological wording is only the spec's one-line paraphrase; verb guessed as explain
  - predictions are not scored, so only the six-moment quiz carries a check; quiz answer format not stated
  - words for case cards not stated

## Who Decides?

- Spec: `tools/who-decides/spec.md` . Module: social-studies-12-civic-action. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part, Reach five items that differ, Put it on the main path, Source the facts.
- Checks a student can pass by guessing:
  - Intended or unintended on each result is a two-way mark, and a mark that 'checks against the case' lets trial reach the key
- **D2.Civ.13.9-12** (practiced, in Past policies): Mark each result of a past policy intended or unintended, and good or bad for whom
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - evaluate the whole policy (results are marked, no verdict)
    - write or explain why
- **D2.Civ.14.9-12** (practiced, in Action options): Compare six action options by cost, reach and effect; choose a plan of two or three
  - Parts of the standard the student never does (must add):
    - historical and emerging means of change (all six options are present-day local)
    - promoting the common good and protecting rights are not addressed
- **D4.7.9-12** (practiced, in Action options; the plan card): Pick two or three actions, write why and one reflection
  - Parts of the standard the student never does (must add):
    - complex causal reasoning
    - regional and global problems (local only)
- **D4.3.9-12** (taught, in Drafts): Write a testimony, a petition and a letter, each fitted to its audience
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - digital venue (no digital form among the three drafts)
    - oral delivery is an optional recorder with no check
- **D4.8.9-12** (touched, in Mock hearing (extra mode)): Run the mock hearing with chair, sign-up, time limit and class vote
  - To do: off the main path or can be skipped: put it on the path
  - Parts of the standard the student never does (must add):
    - the decision path on the main route is tool-lit, not a deliberation by the student
    - deliberative strategies in a classroom or school (hearing mode only, run by a teacher)
- The read was unsure about (check these against the spec; the read may be wrong):
  - library branch merger case has no entry in Sources ('a real city's audit, checked at build')
  - D4.8.9-12 marked touched because the matching part is the optional mock hearing; the path board could be read as shown
  - D2.Civ.13 check is tool-key per 'Each result checks against the case'; how wrong marks respond is not stated
  - spec says the tool is a lesson that can split across periods; minutes taken as 50 within 45-60

## Supreme Court Simulator

- Spec: `tools/supreme-court-simulator/spec.md` . Module: social-studies-12-civil-rights-and-liberties. Stage: spec only. Sort: **small addition**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Add a check, Sensitivity read.
- Checks a student can pass by guessing:
  - Mark 'no tilt' every time on the panel: asking for one interest per party first does not stop it
- **D2.Civ.12.9-12** (shown, in Step 1 person card; what-changed card): Read how each person used or challenged the law, then what changed
  - To do: the tool does the "analyze" step: the student must do it
  - Parts of the standard the student never does (must add):
    - analyze (the student reads; the tool tells how people used the law)
    - local, state and international laws (all five cases are U.S. Supreme Court cases)
- **D2.Civ.10.9-12** (practiced, in Whose interest panel): Fill the whose-interest panel; mark where own view tilted the ruling
  - To do: no check: add one where thinking is cheaper than guessing
  - Parts of the standard the student never does (small, add if cheap):
    - civic virtues and human rights (only constitutional rights cases)
    - judging whether a tilt was appropriate has no check
- **D3.4.9-12** (taught, in Steps 4 and 5; argument builder; refine step): Build claim, precedent and counterclaim for both sides; refine after justices' questions; name strength and limit
  - Parts of the standard the student never does (small, add if cheap):
    - precision and significance of the claim are not checked (only that a strength and a limit are named)
- The read was unsure about (check these against the spec; the read may be wrong):
  - words for the case folders not stated in the spec
  - whether the justices' questions are written per case or reacted to the student's typed claim is not stated
  - D2.Civ.10 and D2.Civ.12 wording taken from the spec's quotes

## Checks and Balances

- Spec: `tools/checks-and-balances/spec.md` . Module: social-studies-12-congress-the-president-and-the-courts. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part.
- Checks a student can pass by guessing:
  - Play any legal card: only the branch's real powers are playable, but every legal card passes and no card is wrong
  - The route note (which route fits which purpose) has no check on its content in the spec
- **D2.Civ.4.9-12** (practiced, in Play; the balance note): Play one branch's real power cards; mark one power that grew, one that shrank
  - Parts of the standard the student never does (must add):
    - explain how the Constitution sets powers and limits (no explanation is written or spoken)
    - responsibilities of each branch beyond the cards played
    - why the powers are still contested (student only names who contests)
- **D2.Civ.11.9-12** (practiced, in Replays; the scoreboard): Replay one policy by four other routes; write which route fits which purpose
  - Parts of the standard the student never does (must add):
    - evaluate by the student's own judgment (the tool scores speed, durability, voices and rights)
    - local level (routes are federal, state and international)
- The read was unsure about (check these against the spec; the read may be wrong):
  - wording of D2.Civ.4 and D2.Civ.11 taken from the spec's quotes
  - depth of D2.Civ.11 could be taught if the written route note were checked; the spec only tests that routes were replayed
  - kept action plan; compare or manipulate would also fit

## Campaign Manager

- Spec: `tools/campaign-manager/spec.md` . Module: social-studies-12-elections-parties-and-media. Stage: spec only. Sort: **small addition**.
- Fixes: Add the missing part, Reach five items that differ, Sensitivity read.
- **D2.Civ.2.9-12** (practiced, in Rules switch; turnout panel; the theory note): Replay the race under four rule systems; read turnout panel; pick a theory and write which system fits
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - analyze the role of citizens (the student runs a campaign, not a citizen)
    - changes in participation are read on a chart, not analyzed
    - theories of democracy are picked from three names with no teaching of them
- **D2.Civ.10.9-12** (taught, in Campaign weeks; message cards): Match a message to each voter group by its interest; watch polls move
  - Parts of the standard the student never does (must add):
    - appropriate roles of personal interests
    - civic virtues, democratic principles and rights (messages are about voter interests only)
- The read was unsure about (check these against the spec; the read may be wrong):
  - items for D2.Civ.10 is six groups times ten weeks, an estimate
  - D2.Civ.10 marked taught on the definition (match to stated interests, polls as key) though the standard's analysis of civic principles is not done
  - setting_group council-debate kept from the old tag though the picture is a campaign office
  - only one of the four rule systems is the default play; the other three are replays

## Build a Government

- Spec: `tools/build-a-government/spec.md` . Module: social-studies-12-foundations-of-government. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part, Reach five items that differ, Sensitivity read.
- Checks a student can pass by guessing:
  - Deciding-article question: eight options, trial works
  - Note: needs only one article and a reason
- **D2.Civ.3.9-12** (practiced, in Crisis stepper): Draft eight articles, run five crises, name the deciding article
  - Parts of the standard the student never does (small, add if cheap):
    - laws as such
    - international agreements beyond one river treaty
- **D2.Civ.8.9-12** (practiced, in Scorecard and note): Read scorecard and country match; write what to change
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - civic virtues
    - evaluating other systems in other times and places
- The read was unsure about (check these against the spec; the read may be wrong):
  - Haudenosaunee influence card could count as Native content
  - Scorecard checks the design by stated rules, not the student

## Train Your Dog

- Spec: `tools/train-your-dog/spec.md` . Module: social-studies-12-learning-and-development. Stage: spec only. Sort: **small addition**.
- Fixes: Add the missing part.
- **APA.Development and Learning** (taught, in Lessons 1-5; The report): Choose consequence and schedule, predict curve, run, write report
  - Parts of the standard the student never does (must add):
    - negative reinforcement and positive punishment as choices
    - generalization and discrimination
    - cognitive learning such as insight and latent learning
    - student classifying a new human example unaided
    - development half taught elsewhere
- The read was unsure about (check these against the spec; the read may be wrong):
  - standard wording taken only from what the spec quotes, not filed text
  - depth taught rests on the report rule of four terms used correctly, which the spec does not describe how the tool checks
  - predictions are not scored
  - beatable left empty because spec closes both listed routes
  - spec covers only the learning half of the standard (lifespan half is in one-life-many-stages)

## One Life, Many Stages

- Spec: `tools/one-life-many-stages/spec.md` . Module: social-studies-12-lifespan-development. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part.
- Checks a student can pass by guessing:
  - Method tags: four choices per stop with free tries, so trial is cheaper than recalling the study
- **APA.Development and Learning** (practiced, in Eight stops; method tags; The summary): Predict each stop, tag the research method, write summary
  - Parts of the standard the student never does (must add):
    - prenatal development
    - language development
    - moral development
    - explaining why changes happen
    - student applying a stage idea to a new case (Second life is optional)
- The read was unsure about (check these against the spec; the read may be wrong):
  - standard wording taken only from what the spec quotes, not filed text
  - practiced not taught because the method tag check is guessable and predictions are unscored
  - explored not used because the student does not set up cases
  - Second life (Theo) treated as not on the main path
  - depth might read taught if the summary rule counts as a check

## Economy Dashboard

- Spec: `tools/economy-dashboard/spec.md` . Module: social-studies-12-macroeconomics. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part.
- Checks a student can pass by guessing:
  - Investigation cards: three choices (spending, production, money) checked against the real first mover, free tries
- **D2.Eco.10.9-12** (practiced, in Investigation cards): Mark which force moved first (spending, production, money) on six investigation cards
  - Parts of the standard the student never does (must add):
    - explain (the student marks, writes nothing)
    - current data (cards use 1973 to 2022; only the brief uses the latest quarter)
- The read was unsure about (check these against the spec; the read may be wrong):
  - words for recession stories not stated
  - forecast is checked only on a later data refresh, not in the sitting, so D2.Eco.11 has no in-sitting check on its future part
  - does a wrong investigation answer show right away is not stated

## The Buyout

- Spec: `tools/the-buyout/spec.md` . Module: social-studies-12-market-structures-and-business. Stage: built (the code changes after the spec). Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part, Add a check, Reach five items that differ.
- Checks a student can pass by guessing:
  - Competition ratings: three buttons per rating with feedback that says 'Not quite', free tries, no score
  - Memo reason fit: four reason chips against five remedies with a 'Fix:' message, so trial finds the fitting pair
  - Memo sentence: twelve words and eight different words pass without economic content
- **D2.Eco.4.9-12** (practiced, in Compare; Switch test): Rate each run's sellers on the HHI ladder, rate buyers, run the Switch test
  - To do: only 3 items: reach five or more that differ
- **D2.Eco.5.9-12** (practiced, in Rivals; Buyout; Compare): Play both runs, then mark the 3 Compare rows that changed most for buyers
  - To do: no check: add one where thinking is cheaper than guessing
  - Parts of the standard the student never does (must add):
    - describe in words (rows are marked, nothing is written about them)
- **D2.Eco.6.9-12** (practiced, in Regulator; Memo): Pick one or two reasons the government might step in; write a sentence
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - generate own reasons (four reason chips are supplied; the sentence is checked for length and distinct words only)
- The read was unsure about (check these against the spec; the read may be wrong):
  - case card words estimated at 40 per card
  - spec gives ledger rank lists computed by the tool, so student 'ranking' in D2.Eco.7 follows the tool's list
  - no stated worked model for D2.Eco.5; guided is the gauge and table
  - family listed as market but spec says no kit engine, so new-engine

## Trait Lab

- Spec: `tools/trait-lab/spec.md` . Module: social-studies-12-personality-intelligence-and-motivation. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part.
- Checks a student can pass by guessing:
  - Goal sorting: three theories, per-goal check, free retries
- **APA.Individual Variations** (practiced, in Three benches; sorting board; Can and can't): Take sample items, sort goals by theory, fill can-and-can't cards
  - Parts of the standard the student never does (must add):
    - assessment of other traits or abilities
    - norms and test construction
    - theories beyond those shown (e.g. humanistic, psychodynamic personality)
    - student judging a new measure unaided
- The read was unsure about (check these against the spec; the read may be wrong):
  - standard wording taken only from what the spec quotes, not filed text
  - items counts ten personality items, four reasoning items and eight goals loosely
  - depth practiced because sorting is guessable and the can-and-can't check depends on the spec rule 'named limit and reason'

## Case Conference

- Spec: `tools/case-conference/spec.md` . Module: social-studies-12-psychological-disorders-and-treatment. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part, Reach five items that differ, Sensitivity read.
- Checks a student can pass by guessing:
  - Lens sorting: three lenses, per-fact check with reason, free retries
- **APA.Mental and Physical Health** (practiced, in Three lenses; Classification; Treatment evidence; Stress and health; Summary): Sort case facts under three lenses, pick plan, write summary
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - disorder categories beyond anxiety, depression, OCD and ADHD
    - psychotherapy approaches such as psychodynamic and humanistic
    - student applying criteria unaided (criteria card is read)
    - stigma and help-seeking
- The read was unsure about (check these against the spec; the read may be wrong):
  - standard wording taken only from what the spec quotes, not filed text
  - depth practiced because lens sort is guessable; summary check is the only non-guessable one
  - action kept as discuss though the student mostly sorts and writes

## Illusion Lab

- Spec: `tools/illusion-lab/spec.md` . Module: social-studies-12-sensation-perception-and-memory. Stage: built (the code changes after the spec). Sort: **small addition**.
- Fixes: Add the missing part, Sensitivity read.
- **APA.Biological** (explored, in Inside the Eye; Line Lengths; Shadow Squares): Set lines and grays by eye, predict edge or middle, slide inhibition
  - To do: see-why code, fine here; the unit must add: Add student-written explanations of why perception differs from sensation, other senses, and the brain structures involved.
  - Parts of the standard the student never does (must add):
    - senses other than vision
    - brain structures beyond the visual path
    - explaining in own words
    - genes and nervous system basics
- **APA.Cognition** (explored, in Spot the Change; Count Backward; Word Lists; Eyewitness): Run change, counting-backward and word-list trials, compare to research
  - To do: see-why code, fine here; the unit must add: Add student explanations of each result, and the cognition topics beyond attention and memory (language, problem solving, decisions).
  - Parts of the standard the student never does (must add):
    - thinking, language, problem solving and decision making
    - memory types and models beyond three steps
    - retrieval cues and improving memory
    - explaining in own words
- The read was unsure about (check these against the spec; the read may be wrong):
  - standard wording taken only from what the spec quotes, not filed text (APA wording not printed; spec paraphrases it)
  - explored chosen because the standard verb is unclear; both codes are broad and the spec covers a slice
  - minutes from 30 to 45 for all six stations

## Who Has the Power?

- Spec: `tools/who-has-the-power/spec.md` . Module: social-studies-12-the-constitution-and-federalism. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part, Sensitivity read.
- Checks a student can pass by guessing:
  - Sort: six bins, wrong placement opens the source, free retries
  - Defense sentence: needs a bin and a reason, not a good one
- **D2.Civ.1.9-12** (practiced, in The sort): Sort 24 powers into six bins and read each source
  - Parts of the standard the student never does (small, add if cheap):
    - responsibilities
- **D2.Civ.4.9-12** (practiced, in Moving line; contested cards): Replay six moved cards; place three contested cards and defend one
  - Parts of the standard the student never does (must add):
    - limits on power
    - explaining how the Constitution established the system
- The read was unsure about (check these against the spec; the read may be wrong):
  - Civ.4 combines a slider replay (shown) with a defense (practiced)
  - Moving-line replay is viewing

## Causes Web

- Spec: `tools/causes-web/spec.md` . Module: social-studies-12-causes-web. Stage: spec only. Sort: **fine**.
- Fixes: Reach five items that differ.
- **D4.2.9-12** (taught, in Three layouts; The explanation): Links cards, fixes gap flags across three layouts, writes explanation
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - gathers own data or examples (cards are supplied)
- **D4.6.9-12** (taught, in Building; The challenge step): Draws cards from four lenses for local and global case; marks challenges
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - regional scale (only local and global twin)
    - challenges across more than one place (one case chosen)
- The read was unsure about (check these against the spec; the read may be wrong):
  - items set to 1 because the child picks one of three cases
  - layout gate requires six linked cards from three lenses but the because label content is not checked beyond presence
  - challenge marking (one challenge, one opportunity) has no stated check

## Trade Island

- Spec: `tools/trade-island/spec.md` . Module: social-studies-12-global-trade. Stage: built (the code changes after the spec). Sort: **fine**.
- Fixes: Close the guessable check, Reach five items that differ, Sensitivity read.
- Checks a student can pass by guessing:
  - Cost card: nine possible values per island with a wrong value showing the working at once, so cycling reaches the answer (not scored)
- **D2.Eco.14.9-12** (taught, in Islands, four seasons): Fill the Cost card, move Pell's workers, offer deals until both islands fill more baskets
  - To do: only 4 items: reach five or more that differ
- **D2.Eco.15.9-12** (taught, in Policy; Case): Set tariff, currency and factory levers, pin evidence from both islands, write a case
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - real national economies (all effects come from a fictional model with case cards beside it)
- The read was unsure about (check these against the spec; the read may be wrong):
  - words for case cards not stated
  - D2.Eco.15 taught on the definition; the Case check tests structure, not argument (the spec says so)
  - spec items for D2.Eco.14 counted as four seasons

## Fed Chair

- Spec: `tools/fed-chair/spec.md` . Module: social-studies-12-money-and-the-federal-reserve. Stage: spec only. Sort: **fine**.
- Fixes: none found; confirm at final review.
- **D2.Eco.12.9-12** (taught, in Meetings; fiscal panel; comparison and evaluation): Set the rate and bond buying, recommend a fiscal choice, compare with the real path, write a mix per era
  - Parts of the standard the student never does (small, add if cheap):
    - fiscal policy is recommended from a fixed menu, not set
- The read was unsure about (check these against the spec; the read may be wrong):
  - taught on the definition; the evaluation check is a template needing a mix and reason per era, structure only
  - items counted as about 24 meetings

## Two Villages

- Spec: `tools/two-villages/spec.md` . Module: social-studies-12-property-rights-and-the-rule-of-law. Stage: spec only. Sort: **fine**.
- Fixes: Sensitivity read.
- The read was unsure about (check these against the spec; the read may be wrong):
  - words for evidence cards not stated
  - sensitive flag set because the spec guards against showing a culture as backward
  - the paragraph check is keyword-style (property rights, rule of law, one real case)


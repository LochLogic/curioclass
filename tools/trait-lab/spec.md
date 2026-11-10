# Trait Lab

## One idea
Three benches, personality, intelligence and motivation, each set out a theory, the real measure behind it, and sample items the student can try: on the personality bench the student answers ten public-domain items for the Big Five traits and sees a plain profile, then compares it with a horoscope-style "reading" that fits everyone and learns why reliable measures repeat (test-retest), predict real things (validity) and resist flattering vagueness (the Forer effect); on the intelligence bench the student tries sample reasoning and vocabulary items, sees how IQ scores are scaled to a mean of 100, compares Spearman's general factor with Gardner's and Sternberg's broader ideas and what the evidence says about each, and sees that average scores rose about 3 points a decade (the Flynn effect), which says something about tests and times; on the motivation bench the student sorts everyday goals by drive, need and self-determination theory (autonomy, competence, relatedness) and checks Maslow's pyramid against what research found; at the end the student fills a "can and can't" card for each measure, so a twelfth grader learns theories and measures of personality, intelligence and motivation and what each measure can and cannot tell you.

## Not like
- go-along (12, concept): social pressure. Here individual differences.
- case-conference (12, concept): disorders and treatment. Here typical variation.
- brain-explorer (12, spec): brain structures. Here traits and abilities.
- one-life-many-stages (12, spec): change across a life. Here differences between people.

## Who and how
- Grade 12, Psychology, module "Personality, Intelligence and Motivation". Standards: APA.Individual Variations (APA National Standards for High School Psychology Curricula: theories and assessment of personality, intelligence and motivation, and the reliability, validity and limits of measures).
- Format: lab. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Three benches with theories, real measures and sample items; the "can and can't" cards. Answers stay on the device and the screen says so (localStorage `trait-lab-v1`, try/catch). Extra: Measure check (the class compares how stable their own sample-item scores were from one day to the next, anonymously). tool.json `modes: ["Lab", "Measure check"]`, `minutes: "30-40"`, `grades_label: "Grade 12"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| APA.Individual Variations (personality) | Take ten Big Five sample items, compare with a vague reading, and name reliability and validity | the profile; the vague reading; the measure card | 2 |
| APA.Individual Variations (intelligence) | Try sample items, read the score scale, compare three theories with their evidence | the bell curve at mean 100; the theory cards; the Flynn chart | 3 |
| APA.Individual Variations (motivation) | Sort goals by theory and check Maslow against the research | the sorting board; the evidence card | 4 |
| APA.Individual Variations (limits) | Fill a can and can't card for each measure | the three cards | 5 |

## Screens and modes
Header (kit): title "Trait Lab"; `Lab`, `Measure check`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A lab with three benches: Personality, Intelligence, Motivation. A line under them: "Your answers stay on this device." The welcome is queued (`welcomeAfter: true`): "Every test claims to measure something about you. Here you'll check what each one really measures. Tap a bench." First hint: "Tap a bench to begin."

**Personality bench (focus: the measure).** At 1366x768 the bench fills the left with the card panel right; at 680x425 the panel is a sheet. Ten sample items from the public-domain International Personality Item Pool (two per trait: openness, conscientiousness, extraversion, agreeableness, neuroticism, shown as "emotional stability"), on a five-point scale. A plain profile follows, with no labels like good or bad and no diagnosis. Then a "reading" card that fits almost anyone; the student rates how well it fits and learns the Forer effect (1949). Measure card: test-retest reliability (Big Five scores are fairly stable in adults), validity (conscientiousness predicts school and job performance modestly), and the limits of self-report. A note: popular type tests that sort people into boxes often give a different type on retest.

**Intelligence bench.** Four sample items (a matrix pattern, a number series, a vocabulary item, a verbal analogy), never scored as an IQ. The scale card: IQ tests set the average at 100 with a standard deviation of 15, so about 68 percent of people score between 85 and 115. Theory cards with evidence: Spearman's general factor (1904), Gardner's multiple intelligences (1983, popular in schools but with weak test evidence), Sternberg's triarchic theory (1985). The Flynn chart: average raw scores rose about 3 points a decade across the 20th century, which suggests environment matters and tests must be re-normed.

**Motivation bench.** Eight everyday goals (finishing a puzzle, eating when hungry, practicing for a team, earning a paycheck, helping a friend) to sort by drive reduction, Maslow's needs, and self-determination theory (autonomy, competence, relatedness; Deci and Ryan). Evidence card: Maslow's needs are recognized across cultures, but people pursue higher needs before lower ones are met (Tay and Diener, 2011); rewards can lower interest in a task people already enjoy (the overjustification effect).

**Can and can't (the aha).** One card per measure: "This measure can tell you ___. It can't tell you ___, because ___." Narrator: "A score is a snapshot taken with a particular camera. It's never the whole person."

**The end.** The three cards, with the student's profile only if they choose to print it. `Print` prints the cards.

**Measure check (extra).** Students retake the ten items the next day on their own device and compare how much their profile moved, sharing only the change, never the answers.

## Content
- Ten IPIP items (public domain), four sample reasoning items written for this tool, theory and evidence cards, eight goals, three can and can't templates.
- Sample items only; never a full test, an IQ score or a diagnosis; answers stay on the device.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Benches open in any order; the can and can't cards open after all three benches.
- Answers save to the device with try/catch and a clear button; nothing is sent.
- Keyboard: Tab to benches, items, scales, cards and the sorting board; arrow keys choose a scale point; Enter places.
- With Motion off the bell curve and profile draw at once.

## Look
- Accent `--brand` #4b3f8f trait indigo (header, benches, the profile); gold #f4c542 (the item in focus, the placed goal); paper #f3f1fa; ink #130f2e; muted #56536a.
- Contrast (WCAG 2.1, computed): white on brand 8.73:1; brand on paper 7.80:1; ink on paper 16.53:1; muted on paper 6.61:1; ink on gold 11.37:1.
- Never color alone: profile bars carry numbers and trait names; theories carry labels.
- Different from this batch (biscuit brown, lifespan rose, chart navy, Fed green).

## Art
- Drawn in code: benches, item cards, the profile, the bell curve, the Flynn chart, the sorting board.
- Local FLUX (`scripts/localart.py`): the lab (1, 16:9).
About 1 image.

## Voice
Two bank voices, each unique in this batch: `curious-librarian` as the lab guide and hints; `clear-teacher` as the explainer of theories and measures. `Curio.voice` with `scope: () => state.mode + ':' + state.bench + ':' + state.item + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `item`: "Pick how well this describes you."
- event, whole, each measure card.
- event, whole, each theory card.
- how `sort`: "Sort this goal by theory."
- how `cancant`: "Write what this measure can and can't tell you."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: three benches, the item scale, the profile, the bell curve, the sorting board, the cards.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Items | Answer all middle | The profile still shows; the measure card asks what a flat profile can and can't mean. |
| Sorting | Put every goal under Maslow | Each placement checks against the theory that fits best. |
| Can and can't | Write "it can't tell everything" | Each card needs a named limit and a reason. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `item`; measure card (whole).
2. Theory cards (whole), waits.
3. `sort`.
4. `cancant`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| APA.Individual Variations wording | APA, "National Standards for High School Psychology Curricula" (2022) | data/modules/social-studies.txt | yes |
| IPIP Big Five items are public domain | Goldberg, International Personality Item Pool (ipip.ori.org) | Goldberg and colleagues, Journal of Research in Personality (2006) | yes |
| Big Five stability and conscientiousness predicting performance | Roberts and DelVecchio, Psychological Bulletin (2000) | Barrick and Mount, Personnel Psychology (1991) | yes |
| The Forer effect (1949) | Forer, Journal of Abnormal and Social Psychology (1949) | APA Dictionary of Psychology | yes |
| IQ scaled to mean 100, SD 15; about 68 percent within one SD | Wechsler Adult Intelligence Scale technical manual | APA, "Intelligence: Knowns and Unknowns" (Neisser and colleagues, 1996) | yes |
| Spearman (1904), Gardner (1983), Sternberg (1985) and the evidence on each | Neisser and colleagues (1996) | Waterhouse, Educational Psychologist (2006) | yes |
| The Flynn effect, about 3 points a decade | Flynn, Psychological Bulletin (1987) | Pietschnig and Voracek, Perspectives on Psychological Science (2015) | yes |
| Self-determination theory; overjustification | Deci and Ryan, "Intrinsic Motivation and Self-Determination" (Plenum, 1985) | Deci, Koestner and Ryan, Psychological Bulletin (1999) | yes |
| Maslow's needs across cultures, not in strict order | Tay and Diener, Journal of Personality and Social Psychology (2011) | Maslow, Psychological Review (1943) | yes |
| Type tests often change on retest | Pittenger, Review of Educational Research (1993) | National Research Council, "In the Mind's Eye" (1991) | yes |
Backed twice: 10. Cut: 0.

Checks run (Python, scratchpad r23, 2026-11-09): ten items, two per trait; 85 to 115 holds about 68 percent of a normal curve; 3 points a decade over 70 years is 21 points; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 bench and panel; at 680x425 sheet.
2. The personality bench shows the profile, the vague reading and the measure card. (APA.Individual Variations)
3. The intelligence bench shows sample items, the scale and three theories with evidence. (APA.Individual Variations)
4. The motivation bench sorts goals and checks Maslow against research. (APA.Individual Variations)
5. A can and can't card is filled for each measure. (APA.Individual Variations)
6. No IQ score, full test or diagnosis; answers stay on the device, stated on screen.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: charts draw at once; no network requests.

## Open questions
- The idea card flags a privacy line if answers are stored (default used: answers stay on the device under `trait-lab-v1` with a clear button, the screen says so, and the class mode shares only the change, never the answers).

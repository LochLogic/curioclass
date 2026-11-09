# Logic Gym

## One idea
Every claim is a barbell and every piece of evidence is a weight plate: in quick reps the student loads only plates that fit the bar (relevant) and decides when there are enough to lift the claim (sufficient), and a plate that doesn't fit slides off while a big claim on one light plate won't budge, then in a full workout they trace a whole letter to the editor, load each of its claims with the evidence it gives, and judge whether the reasoning connects, so they learn to judge whether an argument's evidence fits and is enough.

## Not like
- argument-x-ray (6, spec): tagging an op-ed's claim, reasons and evidence. Here judging relevance and sufficiency, grade 7.
- claim-court (5, spec): judging an author's support for points, grade 5. Here quick reps plus a sound-reasoning check.
- counterclaim-rally (7, spec): answering an opponent's points. Here weighing someone else's evidence.
- podcast-listening-club (6-8, spec): judging claims by ear. Here on the page, in fast reps.
- fallacy-field-guide (10, concept): named fallacies. Here relevance, sufficiency and sound reasoning without fallacy names.

## Who and how
- Grade 7, ELA, module "Evaluating Arguments" (Reading Informational Text). Standard: RI.7.8 (trace and evaluate the argument and specific claims in a text, assessing whether the reasoning is sound and the evidence is relevant and sufficient).
- Driver: one student; class mode is "Spot" where the room calls Lift or Drop (tool.json `driver: "student"`). Every plate and claim is read on tap.
- Reps (24 claims in three weight classes), a full workout on one letter to the editor, and a fix-it round. tool.json `modes: ["Reps", "Full workout", "Fix it", "Spot"]`, `minutes: "15-30"`, `grades_label: "Grade 7"`.
- Nothing is saved; the training log lasts while the page is open. `Print` prints the log and the workout.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RI.7.8 (relevant) | Load plates that bear on the claim; reject plates that don't | plates seating or sliding off | 2 |
| RI.7.8 (sufficient) | Decide when there is enough evidence to lift; light plates (one story, a tiny survey) can't lift a big claim alone | the bar lifting or staying down, plate weights | 2 |
| RI.7.8 (name the problem) | End each rep by naming it: irrelevant, not enough, or sound | the rep card and the training log | 3 |
| RI.7.8 (trace the argument; sound reasoning) | Full workout: trace the letter's claims, load each with its evidence, and judge whether the reasoning connects (timing, cause, comparison) | the letter with bars for each claim and a reasoning check | 4 |
| RI.7.8 | Fix it: choose the plates a weak argument needs | the repaired bar lifting | 5 |

## Screens and modes
Header (kit): title "Logic Gym"; `Reps`, `Full workout`, `Fix it`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A bright school gym with a barbell on a rack, a claim printed on the bar ("Our town's new skate park made the streets safer") and a rack of evidence plates beside it; Coach Dana Okoye, a strength coach with a clipboard, stands as spotter. First hint: "Tap the bar to hear the claim." The first tap reads the claim; the welcome is queued after it (`welcomeAfter: true`).

**Reps.** Each rep: a claim on the bar and five or six plates. The student drags plates onto the bar or into the reject bin. A plate keyed off topic won't seat ("Skateboarding is in the Olympics" slides off). Each plate has a keyed weight: light (one person's story, a survey of ten people), medium (one city's numbers), heavy (data from many places over years). Claims have keyed weights too: small ("Some kids like the park"), medium, big ("The park made the streets safer"). The student taps `Lift`: the bar lifts if loaded plates are relevant and their total meets the claim's weight; otherwise it stays down. Then the student names the problem on a rep card: Irrelevant, Not enough or Sound. Streaks unlock heavier claim classes.

**Full workout.** A letter to the editor (about 300 words, written for Curio Class and labeled practice) arguing for the skate park. It has three claims; the student traces each by tapping its sentence and the evidence the letter gives for it, which loads onto that claim's bar. Then a reasoning check per claim asks one question from the key: "Is the before number from before the park opened?" (the letter compares a 2019 crash count with a 2024 one, but a new crosswalk also opened in 2021), "Does the same group get compared?", "Could something else explain it?" The student marks each claim Sound, Weak reasoning, Irrelevant evidence or Not enough.

**Fix it.** A weak argument and a rack of extra plates; the student picks the fewest plates that make it lift and explains in one line.

**Training log.** Counts per problem type (spotted and missed), and which kind the student is fastest at.

**Spot (class).** The projector shows a loaded bar; the room calls Lift or Drop and the teacher taps the class answer.

At 1366x768 the bar and rack fit side by side; at 680x425 the rack is below.

## Content
Written for Curio Class: 24 rep claims with plates keyed for relevance and weight; the practice letter with keyed claims, evidence spans and reasoning questions; four fix-it arguments. All data is practice data, labeled made up on screen.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Plates can be pulled off before `Lift`.
- With Motion off the bar shows "Lifted" or "Didn't budge" without moving.

## Look
- Accent `--brand` #9c2a1f gym brick red (header, plates, bar ends); gold #f4c542 (the lifted bar, streaks); paper #fcf3f2; ink #2c0b07; muted #6a524f. Scene: a school gym with mats.
- Contrast (WCAG 2.1, computed): white on brand 7.60:1; brand on paper 6.96:1; ink on paper 16.62:1; muted on paper 6.56:1; ink on gold 11.15:1.
- Never color alone: plates show their weight in words; rep cards are labeled.
- Different from this batch (field olive, studio violet, chat teal, plum).

## Art
- People art goes to Gemini: Coach Dana Okoye (a Nigerian American woman in her thirties in a track jacket), 4 poses; "illustrated friendly gym coach <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): school gym (1); a small-town skate park (1).
About 6 images. Drawn in code: bar, plates, rack, log.

## Voice
Bank voice `hero-coach` as Coach Okoye (unique in this batch); the letter is read by `casual-peer` (unique in this batch). `Curio.voice` with `scope: () => state.view + ':' + state.rep`, `welcomeAfter: true`.
- how `welcome`: "Every claim is a bar. Load only the plates that fit, and decide if there's enough to lift it."
- event `claim`: the claim on the bar.
- event `slide`: "That plate doesn't fit this bar."
- event `stuck`: "Didn't budge. Is it enough?"
- event `lift`: "Lifted!"
- event `reasonCheck`: the keyed reasoning question.
- event, whole, `letter`: the letter.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: plates with keyed relevance and weight, claim weights, lift rule, rep cards, letter tracing with reasoning questions, log.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Reps | Load every plate | Off-topic plates slide off and the rep card must still name the problem. |
| Rep card | Always pick Sound | Each rep's problem is keyed; the log shows misses. |
| Full workout | Mark every claim Sound | The keyed timing problem shows in the print beside the mark. |
| Fix it | Load the whole rack | Fix it asks for the fewest plates; extra plates are counted. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the bar: `claim`, `welcome` (queued, first time).
2. Reps: `slide` as plates fail; `stuck` or `lift` on Lift.
3. Full workout: `letter` (whole) on Play; `reasonCheck` per claim.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RI.7.8 wording | thecorestandards.org, Reading Informational Text Grade 7 | CCSS ELA 2010 PDF | yes |
| Evidence must be relevant to the claim and sufficient to support it; anecdotes and small samples are weak support for broad claims | Purdue OWL, using evidence | ReadWriteThink, evaluating arguments | yes |
| Correlation over time does not show cause when other changes happened in the same period | Khan Academy, correlation and causation | National Library of Medicine or Census Bureau statistics primer on correlation and causation | yes |
Backed twice: 3. Cut: 0.

Design choices (not claims): the letter, claims and plate data are practice, labeled made up on screen.

Checks run (Python, scratchpad b22, 2026-11-09): every weight class has reps keyed to each of the three problems; no rep lifts with only light plates on a big claim; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 bar and rack fit; at 680x425 the rack is below.
2. Plates seat or slide by relevance; the bar lifts by weight. (RI.7.8)
3. Each rep is named and logged. (RI.7.8)
4. The full workout traces three claims and asks keyed reasoning questions. (RI.7.8)
5. Fix it counts plates and takes a line. (RI.7.8)
6. The training log shows spotted and missed per type.
7. Spot mode and Print work.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: the bar shows its result without moving; no network requests.

## Open questions
- None for Cory.

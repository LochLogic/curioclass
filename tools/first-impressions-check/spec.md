# First Impressions Check

## One idea
The student rides a city bus at dawn with six other riders, glances at each one for two seconds and writes a quick guess about them with a confidence level, then over the ride gets small clues (what each rider does, says on the phone, carries, or helps with), revises or keeps each guess with a reason, and finally hears each rider in their own words, while a "what was my guess based on?" board sorts every first guess into looks, clothes, a single moment or real evidence, so they learn to notice how fast first impressions form, what they rest on, and how to hold them loosely until they know more.

## Not like
- perspective-frames (6-8, spec): many views of one history. Here checking your own quick read of a person.
- friend-moves-practice (K-2, spec): what to do and say at play. Here what you assume before you speak.
- conflict-coach (6-8, live): handling a conflict with words. Here the guesses that come before any words.
- consejero (9-12, spec, this batch): advice for friends in Spanish. Here strangers on a bus.
- debate-en-español (9-12, spec, this batch): weighing reasons on a public question. Here weighing evidence about a person.

## Who and how
- Grades 9 to 12, Social and Emotional Learning, module "Seeing Others Clearly". Standards: CASEL Self-Awareness (examining prejudices and biases; linking feelings, values and thoughts) and Social Awareness (taking others' perspectives; recognizing strengths in others).
- Driver: one student; class mode is "Same bus", where the projector shows one rider and the class sees how spread out their guesses were, counted on this device only from hands raised (tool.json `driver: "student"`). Every card, clue and line is read on tap.
- Six riders, one ride, three stops of clues. tool.json `modes: ["Ride", "My board", "Same bus"]`, `minutes: "20-25"`, `grades_label: "Grades 9-12"`.
- Guesses are kept on this device only for the ride (localStorage), and the screen says so: "Your guesses stay on this device. Nothing is uploaded." `Clear my guesses` clears them. `Print` prints the board without the guesses unless the student ticks "Include my guesses".

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| CASEL Self-Awareness (noticing fast judgments) | Make a two-second guess with a confidence level for each rider | the guess card and the confidence dial | 2 |
| CASEL Self-Awareness (examining biases) | Sort each first guess by what it rested on (looks, clothes, one moment, evidence) | the "based on" board | 3 |
| CASEL Social Awareness (perspective-taking) | Revise or keep each guess as clues arrive, with a reason | the guess history per rider | 4 |
| CASEL Social Awareness (recognizing strengths in others) | Hear each rider in their own words and note one thing the first glance missed | the rider's card and the student's note | 5 |

## Screens and modes
Header (kit): title "First Impressions Check"; `Ride`, `My board`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** The inside of a city bus at dawn, windows blue with early light, six seats lit. A line at the top: "Everyone on this bus is made up." First hint: "Tap Start to get on the bus." The first tap plays the doors and the narrator's line; the welcome is queued after it (`welcomeAfter: true`).

**The glance.** Each rider is shown for two seconds (a still picture with no caption), then hidden. The student picks one or two words from a neutral card set (friendly, tired, busy, shy, bossy, kind, rude, worried, cheerful, serious, careless, careful) or types their own, and sets a confidence dial from "just a guess" to "very sure". The card sets never include words about a group, a background or a job.

**Three stops of clues.** At each stop, one small clue per rider, shown and read: an action (gives up a seat, picks up a dropped glove), a half-heard phone line, something carried (a nursing badge, a library book, a toolbox), or a moment out of context (a sigh, a frown at a phone). Some clues fit the first guess and some don't; one clue per ride is itself misleading out of context, and the next stop explains it. After each clue the student keeps or changes the guess and taps a reason chip ("what they did", "what they said", "one moment only", "still just looks").

**Their own words.** At the last stop each rider gets off and says two or three sentences about their morning in their own voice. The student writes one thing the first glance missed.

**My board.** Every first guess sorts into four columns by the reason chips: looks, clothes or things, one moment, real evidence. Beside it the confidence dial readings: how sure the student felt at the glance compared with at the end. The board ends with a short note for the student: "Fast guesses are normal. Holding them loosely is a skill."

**Same bus.** On the projector, one rider at a time; the class raises hands for each word and the teacher taps counts, so the class sees how differently they read the same two seconds.

At 1366x768 the bus and the guess card fit; at 680x425 the card is below the bus.

## Content
- Six riders, written for Curio Class, each with a two-second picture, three clues and their own words:
  1. Dolores, a woman in her sixties in a heavy coat who frowns at her phone; she is reading a text from her grandson who just got into college and can't find her glasses.
  2. Kai, a teen in a hoodie with headphones who doesn't look up; he gives up his seat at the second stop and is studying for his driving test while his mom quizzes him on the phone.
  3. Marcus, a man in his thirties in a work vest who looks tired; he just finished a night shift at a hospital lab.
  4. Priya, a woman in her twenties in a suit who seems rushed and short with the driver; she is late to her first day at a new job and apologizes at the last stop.
  5. Tomás, a man in his fifties with a toolbox who laughs loudly on the phone; he is a choir director carrying sheet-music stands.
  6. Hana, a girl about fourteen who looks bored; she is quietly teaching her little brother to read on the ride.
- Riders are varied in age, look and background, and no rider's story turns on their race, religion, disability or language; every rider has a strength the glance missed and an ordinary flaw (a short temper, a loud laugh, a bad morning), so no one is a saint or a villain.
- Teacher notes explain the research in plain words, give discussion prompts, and say that the point is noticing, not shame.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Guesses can be changed at any stop; there is no score and no right first guess.
- With Motion off the bus doesn't sway, the glance is a picture that hides on a tap instead of a timer, and stops change without the street scrolling past.

## Look
- Accent `--brand` #34406b dawn indigo (header, bus frame, the guess card); gold #f4c542 (seat lights, the confidence dial needle); paper #f2f3f8; ink #121729; muted #545a6c. Scene: a city bus at dawn.
- Contrast (WCAG 2.1, computed): white on brand 10.04:1; brand on paper 9.06:1; ink on paper 16.06:1; muted on paper 6.20:1; ink on gold 10.94:1.
- Never color alone: board columns have titles and icons; the dial shows words at each end.
- Different from this batch (chat teal, council maroon).

## Art
- People art goes to Gemini: six riders, each with a glance picture (seated, neutral), two clue poses and a speaking pose, 4 images each; "illustrated bus rider at dawn <pose>, soft gouache, plain white background, realistic proportions"; 1:1; cutout yes. The art brief asks for ordinary, respectful looks with no exaggerated features, and a fresh agent checks the set.
- Local FLUX (`scripts/localart.py`): the bus interior at dawn (1); the street outside at three stops, no faces (3).
About 28 images. Drawn in code: guess cards, the dial, the board.

## Voice
Bank voice `hs-narrator` as the hint voice and the narrator (unique in this batch); Dolores is read by `wise-mentor`, Kai by `soft-breath`, Marcus by `gravel-ranger`, Priya by `big-sister`, Tomás by `calm-professor` and Hana by `knowing-guide` styled as a young teen (each unique in this batch). `Curio.voice` with `scope: () => state.stop + ':' + state.rider`, `welcomeAfter: true`.
- how `welcome`: "You get two seconds with each rider. Make a guess and say how sure you are. Then watch what happens."
- event `stop`: the stop name.
- event `clue`: the clue for the tapped rider.
- event `phone`: a half-heard phone line.
- event, whole, `words`: a rider's own words.
- event `board`: "Fast guesses are normal. Holding them loosely is a skill."
- event `privacy`: "Your guesses stay on this device. Nothing is uploaded."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: the timed glance, guess cards and confidence dial, clue stops, reason chips, the board, Same bus counts and localStorage (wrapped in try and catch).

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Glance | Skip guessing | The ride waits on a guess for each rider; "no idea" is a choice and goes on the board as its own column. |
| Clues | Keep every guess | Allowed, but each keep needs a reason chip, and "still just looks" shows on the board. |
| Board | Tick "real evidence" every time | The board shows which stop each piece of evidence came from; a first guess at the glance has none. |
| Their own words | Leave the note blank | The board asks once more for each rider with a blank note before it prints. |
There is no score to beat, by design.

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap Start: the narrator's line, `welcome` (queued, first time).
2. Each stop: `stop` (waits); `clue` or `phone` on tap.
3. Last stop: `words` (whole) per rider. First save: `privacy`.
4. My board: `board`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CASEL Self-Awareness includes examining prejudices and biases; Social Awareness includes taking others' perspectives and recognizing strengths in others | CASEL, "What Is the CASEL Framework?" (casel.org) | CASEL, SEL competencies wheel (2020 update) | yes |
| People form trait judgments from a face within about a tenth of a second, and more time mostly raises confidence rather than changing the judgment | Willis and Todorov, "First impressions: making up your mind after a 100-ms exposure to a face" (Psychological Science, 2006) | Todorov, Olivola, Dotsch and Mende-Siedlecki, "Social attributions from faces" (Annual Review of Psychology, 2015) | yes |
| Judgments from faces are often inaccurate, and relying on them can do worse than chance or than using other information | Olivola and Todorov, "Fooled by first impressions? Reexamining the diagnostic value of appearance-based inferences" (Journal of Experimental Social Psychology, 2010) | Todorov, Face Value: The Irresistible Influence of First Impressions (Princeton University Press, 2017) | yes |
| Brief "thin slices" of behavior can carry some information, which is why first impressions feel reliable | Ambady and Rosenthal, "Thin slices of expressive behavior as predictors of interpersonal consequences: a meta-analysis" (Psychological Bulletin, 1992) | Todorov, Face Value (2017), discussion of thin slices | yes |
Backed twice: 4. Cut: 0.

Sensitivity note: a heavy stereotype risk; guess cards hold only mood and trait words, no rider's story turns on a group identity, every rider has a strength and an ordinary flaw, and a fresh agent reviews the riders, art brief and clues for stereotypes before build.

Checks run (Python, scratchpad b29, 2026-11-09): every rider has three clues, at least one that fits a likely first guess and one that doesn't; exactly one clue per ride is misleading and is explained at the next stop; no guess card word names a group, background or job; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 bus and guess card fit; at 680x425 the card is below.
2. Each glance lasts two seconds and takes a guess and a confidence. (CASEL Self-Awareness)
3. The board sorts first guesses by what they rested on. (CASEL Self-Awareness)
4. Guesses can be kept or changed at each stop with a reason. (CASEL Social Awareness)
5. Every rider speaks in their own words and the student notes what the glance missed. (CASEL Social Awareness)
6. Same bus counts and Print work; Print leaves guesses out unless ticked.
7. The privacy line shows; Clear my guesses clears them.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: the glance hides on a tap, not a timer; no network requests.
10. Storage blocked: the tool still works and says guesses won't be kept.

## Open questions
- Fresh stereotype review of riders, clues and art brief (default used: a fresh agent reviews before build, and changes go back to Cory).

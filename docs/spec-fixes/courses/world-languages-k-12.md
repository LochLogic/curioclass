# Spec fixes: world-languages, grade k-12

10 tools: 1 rework, 8 small addition, 1 fine. How to use this file: ../README.md. When a spec is fixed, add a line to ../done.txt.

Kinds of fix in this course: Write the spec (5), Hand the key step to the student (1), Close the guessable check (10), Add the missing part (8), Add a model or a guide (2), Add a check (2), Reach five items that differ (2), Put it on the main path (1), Sensitivity read (8).

## Mi Día

- Spec: `tools/mi-día/spec.md` . Module: world-languages-k-12-school-and-daily-routine. Stage: spec only. Sort: **rework**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Add a check.
- Checks a student can pass by guessing:
  - Time: leave cards at default times; the only guard is a prompt asking if everything is at eight, nothing blocks it
- **ACTFL Novice Mid (telling time)** (practiced, in Mi día): Set each card's time on the clock and hear it
  - To do: the tool does the "tell time" step: the student must do it
  - To do: no check: add one where thinking is cheaper than guessing
  - Parts of the standard the student never does (must add):
    - say or write the time phrase themselves
    - y cuarto and menos cuarto are only heard
- **ACTFL Novice Mid (daily activities, reflexive verbs)** (shown, in Mi día): Place routine cards and watch the little me light
  - To do: the tool does the "talk about" step: the student must do it
  - Parts of the standard the student never does (must add):
    - say or write any routine sentence
    - choose me, te or se for a person
    - use reflexive verbs in a sentence
- **ACTFL Novice Mid (classes)** (shown, in Mi día): Place class cards on the strip and hear the phrase
  - To do: the tool does the "talk about" step: the student must do it
  - Parts of the standard the student never does (must add):
    - say or write Tengo ___ a las ___ themselves
- **ACTFL Novice Mid (simple comparisons)** (taught, in Comparar): Fill about six comparison frames against Martina's day
  - Parts of the standard the student never does (small, add if cheap):
    - compare without frames
    - ask or answer questions about a day
- The read was unsure about (check these against the spec; the read may be wrong):
  - code spelled with facet in parentheses as the spec spells it; module line spells ACTFL.Novice Mid
  - no filed wording printed, so telling time and comparisons judged from the spec only
  - Time and routine cards have no right-wrong check; only reflexive me is keyed in the Comparar frames, so the me check is placed off the main step
  - Martina's day is read-only content, not counted as an item

## Mi Casa

- Spec: `tools/mi-casa/spec.md` . Module: world-languages-k-12-family-and-home. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part, Sensitivity read.
- Checks a student can pass by guessing:
  - Tap every room for a where question: one tap per question, wrong room plays the answer and asks again
  - Phrase tiles for who and where answers at Some and Lots help: few options, free tries
- **ACTFL.Novice Mid** (taught, in Ayudar and Describir modes; Standards map rows 2 to 4): Answer where and who questions by tapping and choosing a phrase; build descriptions with agreement
  - Parts of the standard the student never does (must add):
    - say the phrases aloud with any check
    - ask the questions yourself
    - describe beyond the listed adjectives
- The read was unsure about (check these against the spec; the read may be wrong):
  - ACTFL Novice Mid wording judged from the spec's own table
  - Explorar is free play and ends nowhere; Ayudar and Describir are on the main path
  - Describe mode is the only place the student produces agreement; it has three descriptions
  - minutes 15 taken as the middle of 10-20
  - cost_class sibling because the spanish engine is described in calendario-vivo's spec

## ASL Family Tree

- Spec: `tools/asl-family-tree/(no spec.md yet)` . Module: world-languages-k-12-family-home-and-school. Stage: idea only. Sort: **small addition**.
- Fixes: Write the spec, Close the guessable check, Add the missing part, Sensitivity read.
- Checks a student can pass by guessing:
  - Picking matching picture details after each signed sentence: few options, free tries
- **ACTFL.Novice High** (taught, in Core loop, second family step): Read signed sentences, place tiles, build sentences from sign tiles
  - Parts of the standard the student never does (must add):
    - sign the sentence with own hands
    - describe a person with new vocabulary not in the tiles
- The read was unsure about (check these against the spec; the read may be wrong):
  - Idea card only
  - Student builds sentences from tiles, so it is a build from given parts, not free signing
  - Check is the student comparing with the teen's version, so self-guide
  - K-12 span check (gf-04) open

## Fingerspell Flash

- Spec: `tools/fingerspell-flash/(no spec.md yet)` . Module: world-languages-k-12-fingerspelling-and-the-manual-alphabet. Stage: LIVE (the code changes after the spec). Sort: **small addition**.
- Fixes: Write the spec, Close the guessable check, Add the missing part, Add a model or a guide, Put it on the main path, Sensitivity read.
- Checks a student can pass by guessing:
  - Read it One letter mode: pick the letter from four look-alikes, free tries, a miss only slows the next word
- **ACTFL.Novice Low** (taught, in Read it, Spell it, Alphabet modes): Read hidden fingerspelled words and type them; watch typed words spelled
  - Parts of the standard the student never does (must add):
    - form the handshapes yourself with any check
    - produce a memorized phrase or greeting
- **WRS.Communication** (practiced, in plan.md Practice and Exit check (teacher led, not in the tool)): Pairs fingerspell names to each other and read them
  - To do: off the main path or can be skipped: put it on the path
  - To do: no model or guide: add one
  - Parts of the standard the student never does (must add):
    - exchange of information beyond letters
    - presentational use
    - reading anything but single words and names
- The read was unsure about (check these against the spec; the read may be wrong):
  - Common Core-free tool, so no filed wording; ACTFL Novice Low and WRS.Communication judged from tool.json outcome and plan.md
  - Forming handshapes is claimed in the outcome but the tool never checks the student's own hands
  - cost_class simple guessed; the tool uses line drawings, no shared engine named
  - sensitive set because it is Deaf language content with a practice-only note
  - items not stated

## El Restaurante

- Spec: `tools/el-restaurante/spec.md` . Module: world-languages-k-12-food-and-ordering. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add a model or a guide, Add a check, Reach five items that differ, Sensitivity read.
- Checks a student can pass by guessing:
  - Agreement: two forms (gusta or gustan), free retries, and the lit noun plus the hint says which to pick
  - Politeness: adding quisiera or por favor clears the blunt reaction, and the hint names it
- **ACTFL Novice High (state likes and dislikes)** (taught, in Turns): Build like and dislike sentences from tiles; noun lights
  - Parts of the standard the student never does (small, add if cheap):
    - say aloud (tiles and typing only)
    - states likes outside the menu foods
- **ACTFL Novice High (ask politely)** (taught, in Turns): Order with quisiera or me trae; blunt order gets a pause
  - Parts of the standard the student never does (small, add if cheap):
    - say aloud
    - only a few polite forms are accepted
- **ACTFL Novice High (ask questions)** (practiced, in Turns): Ask Lleva carne? or Qué recomienda? and act on the answer
  - To do: no model or guide: add one
  - To do: no check: add one where thinking is cheaper than guessing
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - no check that the question is well formed
    - only a few questions offered
- **ACTFL Novice High (answer questions)** (taught, in Turns and Diálogo): Answer the server's turns from drinks to the check
  - Parts of the standard the student never does (small, add if cheap):
    - say aloud (recording is optional and unchecked)
- The read was unsure about (check these against the spec; the read may be wrong):
  - items per code are guesses from about 12 turns; ask questions has no stated count
  - asking Lleva carne? is not shown to be checked, so rated practiced
  - code spelled with facet in parentheses as the spec spells it
  - no filed wording printed

## Hola Hallway

- Spec: `tools/hola-hallway/spec.md` . Module: world-languages-k-12-greetings-and-introductions. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part, Sensitivity read.
- Checks a student can pass by guessing:
  - Say hola every time: the time greeting is asked only once per part
  - Use usted or tú for everyone: the chart's final sort of six people is keyed, but in the hallway the reaction tells which way to move
  - Listening picture choices: few options, a miss replays slower with free tries
- **ACTFL.Novice Low** (taught, in Hallway; Standards map rows 1 and 2): Pick time greeting, exchange names, feelings and courtesy phrases
  - Parts of the standard the student never does (must add):
    - say the phrases aloud with any check (recording optional, no recognition)
    - produce phrases from memory without tiles or pictures at Lots and Some
- **WRS.Communication** (taught, in Hallway register; My chart; listening check): Choose tú or usted by person; pick what each reply meant
  - Parts of the standard the student never does (small, add if cheap):
    - presentational use
    - open exchange beyond set phrases
- The read was unsure about (check these against the spec; the read may be wrong):
  - ACTFL and WRS wording judged from the spec's own table, no filed text
  - Spec says the chart accepts usted anywhere, so a usted-for-all strategy passes the chart; I listed it as beatable
  - minutes 15 taken as the middle of 10-20
  - cost_class sibling because the spanish engine is described in calendario-vivo's spec and reused
  - items 16 characters; replies to the name and feeling exchanges are a subset

## ASL Hello Booth

- Spec: `tools/asl-hello-booth/(no spec.md yet)` . Module: world-languages-k-12-greetings-and-introductions-in-asl. Stage: idea only. Sort: **small addition**.
- Fixes: Write the spec, Close the guessable check, Add the missing part, Reach five items that differ, Sensitivity read.
- Checks a student can pass by guessing:
  - Picture choice for the greeting meaning: few options, free tries
  - Attention comic picks: two or three choices with a stated bad outcome
- **ACTFL.Novice Low** (taught, in Core loop, visitor exchanges (HELLO, NAME YOU WHAT?, HOW YOU?)): Pick meaning of each greeting, then copy the answer from panels
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - produce signs from memory without the panels
    - fingerspell own name with a check
- **WRS.Communication** (taught, in Core loop and attention comic strips): Answer each visitor in turn; pick polite ways to get attention
  - Parts of the standard the student never does (small, add if cheap):
    - presentational signing
    - open exchange beyond set phrases
- The read was unsure about (check these against the spec; the read may be wrong):
  - Idea card only: no screens, done-when, beatable or sources sections
  - Copy step is checked only by the student comparing with panels; camera mirror optional
  - K-12 span: card itself says a K child and a teen likely need two framings
  - cost_class new-engine because the Sign Strip engine does not exist yet
  - items guessed from four listed exchanges

## ASL Bingo Night

- Spec: `tools/asl-bingo-night/(no spec.md yet)` . Module: world-languages-k-12-numbers-colors-and-time. Stage: idea only. Sort: **small addition**.
- Fixes: Write the spec, Close the guessable check, Add the missing part, Sensitivity read.
- Checks a student can pass by guessing:
  - Bingo card with several squares: a student can mark by watching rivals
  - Wrong daub costs only a turn, so trial and error is cheap in early rounds
- **ACTFL.Novice Mid** (taught, in Core loop, themed bingo rounds): Read each signed number, color, day or time and mark the card
  - Parts of the standard the student never does (must add):
    - produce the signs with any check (copy step only, mirror optional)
    - build short phrases such as AGE 7 from memory
- The read was unsure about (check these against the spec; the read may be wrong):
  - Idea card only; no beatable, screens or done-when sections
  - Rival marking could let a student copy rivals; card does not close that
  - Producing step is copy from panels, unchecked
  - K-12 span check (gf-04) open

## Sign Parameters Lab

- Spec: `tools/sign-parameters-lab/(no spec.md yet)` . Module: world-languages-k-12-the-five-parameters-of-a-sign. Stage: idea only. Sort: **small addition**.
- Fixes: Write the spec, Close the guessable check, Add the missing part, Sensitivity read.
- Checks a student can pass by guessing:
  - Three-way predict (new sign, same sign, not a sign) with free tries and instant reveal
- **ACTFL.Novice Mid** (practiced, in Core loop, lab notebook): Change one dial, predict new sign, same sign or no sign
  - Parts of the standard the student never does (must add):
    - produce the signs with any check
    - use the signs in phrases
- **WRS.Comparisons** (taught, in Notebook conclusion frame and comparison card): Log trials, write a conclusion, compare ASL pairs with pat/bat
  - Parts of the standard the student never does (small, add if cheap):
    - comparing other features of the two languages
- The read was unsure about (check these against the spec; the read may be wrong):
  - Idea card only
  - ACTFL depth set to practiced: the standard asks to recognize and produce, the lab only predicts and logs; the reverse round (name the differing parameter) is tool-key but recognition only
  - Predict-then-reveal is the design but the verb is not understand-only, so not explored
  - K-12 span check (gf-04) open

## Calendario Vivo

- Spec: `tools/calendario-vivo/spec.md` . Module: world-languages-k-12-numbers-colors-and-calendar. Stage: spec only. Sort: **fine**.
- Fixes: Close the guessable check.
- Checks a student can pass by guessing:
  - Tap everything on a request: one tap per request, wrong tap speaks the right word then asks again, so trial is cheap
  - Copy home's weather in Dos ciudades: keyed by month but the sticker set is small
- **ACTFL.Novice Low** (taught, in Calendario free play, Lucía requests, date sentence, Dos ciudades): Tap numbers, days, months and colors; answer Lucía's requests; build the date
  - Parts of the standard the student never does (small, add if cheap):
    - say the words aloud with any check
    - use words outside the listed numbers 0 to 31, days, months, colors and weather
- The read was unsure about (check these against the spec; the read may be wrong):
  - Only one code in the module so the five rows in the Standards map are folded into one entry
  - Free play has no goals, so items 30 counts only the requests
  - Three levels (Tap and hear, Pen pal, Full date) give different tasks by grade
  - minutes 15 taken as the middle of 10-20
  - cost_class new-engine: the spanish engine is described in full in this spec


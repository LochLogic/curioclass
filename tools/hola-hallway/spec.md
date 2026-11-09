# Hola Hallway

## One idea
People walk down a school hallway through one day, from the 8:00 bell to the evening concert, and the student greets each one in Spanish, choosing by the clock (buenos días, buenas tardes, buenas noches) and by who they are (a friend gets "¿Qué tal?", the principal gets "¿Cómo está usted?"), trades names and feelings and uses courtesy words, hears each person answer and react, and fills in their own "who gets which" chart, so they learn that a greeting depends on the time and on the person.

## Not like
- asl-hello-booth (K-12, idea, on hold): ASL greetings and attention. Here spoken Spanish.
- el-restaurante (K-12, spec, this batch): ordering in sentences, Novice High. Here memorized greetings, Novice Low.
- calendario-vivo (K-12, spec): dates and weather. Here greetings by time and person.
- talk-moves-trainer (3-5, spec later): discussion moves in English. Here first-contact phrases in Spanish.
- i-choose-because (K-2, spec, this batch): giving reasons in English. Here choosing a greeting.

## Who and how
- Grades K to 12, World Languages (Spanish), module "Greetings and Introductions". Standards: ACTFL Novice Low; World-Readiness Standards, Communication (interpersonal and interpretive).
- Driver: one student; class mode is a projector vote on each greeting before the reveal (tool.json `driver: "student"`). Every phrase and reply is spoken in Spanish on tap; the hint voice speaks English.
- One day of about 16 passers-by in three parts (morning, afternoon, evening concert). Help levels: Lots (picture choices), Some (phrase tiles), Little (tiles with no English). tool.json `modes: ["Hallway", "My chart", "Class vote"]`, `minutes: "10-20"`, `grades_label: "Grades K-12"`.
- Optional: record your greeting and play it beside the model; the privacy line shows: "Your recording stays on this device. Nothing is uploaded." No speech recognition. Nothing else is saved; `Print` prints the chart.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| ACTFL Novice Low (greetings) | Pick buenos días, buenas tardes or buenas noches by the hallway clock | the clock and the greeting | 2 |
| ACTFL Novice Low (names, feelings, courtesy) | Exchange names (Me llamo..., ¿Cómo te llamas?), answer "¿Cómo estás?", use por favor, gracias, de nada, con permiso | the exchange strip | 3 |
| WRS Communication, interpersonal (register) | Choose tú or usted by who the person is; the person reacts | the person's reaction and the chart | 4 |
| WRS Communication, interpretive | Listen to each reply and pick what it meant (a feeling, a name, a request) | the reply and the student's pick | 3 |

## Screens and modes
Header (kit): title "Hola Hallway"; `Hallway`, `My chart`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A sunny school hallway with lockers, a wall clock at 8:00 and a bulletin board; a classmate, Valeria, walks in and waves. First hint: "Tap Valeria to hear her." She says "¡Hola!"; the welcome is queued after it (`welcomeAfter: true`).

**Hallway.** Each passer-by carries clues: the clock, their role badge (student, teacher, principal, custodian, a parent, a grandparent at the concert), their face. The student picks:
1. A greeting by time: buenos días (morning), buenas tardes (afternoon), buenas noches (evening and night). Hola fits any time.
2. A follow-up by person: ¿Qué tal? and ¿Cómo estás? for friends (tú); ¿Cómo está usted? for adults they don't know well or who hold a school role.
3. Sometimes a name exchange, a feelings answer (bien, muy bien, más o menos, cansado or cansada) or a courtesy phrase (con permiso to pass, perdón after bumping a backpack, gracias for a held door, de nada).
The person answers in recorded Spanish and reacts. A "¡Hola! ¿Qué tal?" to the principal, Sra. Delgado, gets a friendly raised eyebrow and "Buenos días. ¿Cómo está usted, mejor dicho?" (never a buzzer). After each reply, a listening check asks what the person said, with picture choices.

**The day.** Morning (8:00 to 11:30), afternoon (12:30 to 3:00) and the evening concert (7:00). The clock moves between parts; the light through the windows changes.

**My chart.** A "who gets which" chart the student fills as they go: rows of people, columns tú or usted and the greetings they used, with a reason chip (friend, adult, someone I don't know, older family member). At the end the student sorts six new people into the chart without help.

**Class vote.** The projector shows a passer-by; the class votes a greeting before the reveal.

At 1366x768 the hallway and choices fit; at 680x425 the choices are below.

## Content
- Sixteen characters from many Spanish-speaking backgrounds (Mexico, Puerto Rico, Colombia, Spain, Guatemala, Dominican Republic, Argentina), each with recorded replies in their regional accent and a one-line note on where they're from.
- A note on regional difference: in some places, including much of Colombia, people use usted even with friends and family; the chart accepts usted anywhere and says so.
- Phrases and replies written for Curio Class with the spanish engine's word records.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A greeting can be changed and tried again; there is no score.
- With Motion off people appear in place instead of walking, and the clock jumps.

## Look
- Accent `--brand` #1d5c8c hallway blue (header, lockers, choice tiles); gold #f4c542 (the clock face, a good match); paper #f0f5fa; ink #0a1f30; muted #4b5a68. Scene: a bright school hallway.
- Contrast (WCAG 2.1, computed): white on brand 7.09:1; brand on paper 6.46:1; ink on paper 15.30:1; muted on paper 6.47:1; ink on gold 10.32:1.
- Never color alone: tú and usted columns are labeled; reactions are faces with words.
- Different from this batch (terracotta, town green, night indigo, rewind amber).

## Art
- People art goes to Gemini: 16 characters, 2 poses each (walking and reacting), each a different age, role and background as in Content; "illustrated person walking in a school hallway <pose>, soft gouache, plain white background"; 1:1; cutout yes. People art is reviewed for respectful, varied looks with no stereotypes.
- Local FLUX (`scripts/localart.py`): the hallway in morning, afternoon and evening light (3); the school auditorium door at night (1).
About 36 images. Drawn in code: clock, choices, chart.

## Voice
Bank voice `clear-teacher` as the hint voice in English (unique in this batch); students and young characters are read by `playful-friend`, adults by `knowing-guide`, both in Spanish with each character's regional accent (unique in this batch). `Curio.voice` with `scope: () => state.part + ':' + state.person`, `welcomeAfter: true`.
- how `welcome`: "Greet everyone who walks by in Spanish. Check the clock, and check who they are."
- event `reply`: the person's reply in Spanish.
- event `react`: the reaction line ("¿Cómo está usted, mejor dicho?").
- event `listen`: "What did they say? Tap the picture."
- event `clock`: "It's {afternoon} now."
- event `privacy`: the privacy line.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
spanish (`kit/spanish.js`, `__tool.es`), described in full in tools/calendario-vivo/spec.md. This tool uses: word records with audio, `es.say`, `es.tiles` and `es.check`. The passers-by, reactions, clock and chart are tool-only code.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Time | Say hola every time | Hola is accepted but the time greeting is asked for once per part, by the clock. |
| Register | Use tú for everyone | Adults in school roles react and ask again; the chart's final sort is keyed. |
| Listening | Tap any picture | Each reply's meaning is keyed; a miss replays it slower. |
| Chart | Copy the first row | The six new people differ in age and role. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap Valeria: `reply`, `welcome` (queued, first time).
2. Each person: `reply` after the greeting (waits), `react` if register is off, then `listen`.
3. Between parts: `clock`. First recording: `privacy`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| ACTFL Novice Low and World-Readiness Standards, Communication (interpersonal, interpretive, presentational) | ACTFL Proficiency Guidelines 2012 | ACTFL, World-Readiness Standards for Learning Languages (2015) | yes |
| Buenos días is used in the morning, buenas tardes from about midday until dark, buenas noches in the evening and at night, as a greeting or a goodbye | Real Academia Española, Diccionario panhispánico de dudas, "bueno" (saludos) | Instituto Cervantes, Plan curricular, A1 greetings | yes |
| Usted is the formal "you"; use varies by region, and in parts of Colombia usted is used even among family and friends | Real Academia Española, Diccionario panhispánico de dudas, "usted" | Britannica, Spanish language: regional variation in address forms | yes |
Backed twice: 3. Cut: 0.

Sensitivity note: characters from many countries are drawn and voiced with care; the tool goes to the fresh-agent review.

Checks run (Python, scratchpad b25, 2026-11-09): every passer-by has a keyed time greeting that matches their clock time and a keyed register; each part has at least two tú and two usted people; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 hallway and choices fit; at 680x425 choices are below.
2. Greetings check against the clock. (ACTFL Novice Low)
3. Name, feeling and courtesy exchanges work with listening checks. (ACTFL Novice Low; WRS interpretive)
4. Register choices get reactions, and the chart's final sort is keyed. (WRS interpersonal)
5. The day runs through three parts.
6. Help levels behave as in Who and how; recording shows the privacy line.
7. Class vote and Print work.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: people appear without walking; no network requests.

## Open questions
- Spanish audio review: see calendario-vivo (default used: a fresh agent checks the text, and Sara or Cory listens to a sample of 20 lines).

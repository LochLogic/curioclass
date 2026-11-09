# Mi Día

## One idea
The student builds their own school day in Spanish on a clock-face timeline, dragging routine cards (me despierto, me cepillo los dientes, desayuno) and class cards (matemáticas, ciencias, arte) onto the day and setting each one's time on the clock (a las siete, a las nueve y media), then lays it beside the day of Martina, a pen pal at a school in Santiago, Chile, who stays at school all day and eats lunch there, and says what is the same and what is different, so they learn to tell time and talk about their daily routine with the little "me" of reflexive verbs.

## Not like
- calendario-vivo (K-12, spec): days, dates and weather. Here clock time and a routine.
- mi-casa (K-12, spec, this batch): people and places at home. Here a day's events.
- time-machine-talk (3-5, spec, this batch): English past tense in history. Here Spanish present-tense routine.
- hola-hallway (K-12, spec): greetings by time of day. Here what happens at each time.
- math-explainer (3-5, spec, this batch): steps of a solution. Here steps of a day.

## Who and how
- Grades K to 12, World Languages (Spanish), module "School and Daily Routine". Standard: ACTFL Novice Mid (lists and memorized phrases).
- Driver: one student; class mode is "Nuestro horario", a class schedule built on the projector (tool.json `driver: "student"`). Every card and time is spoken in Spanish on tap; the hint voice speaks English.
- Help levels: Lots (pictures, full phrases, clock set by tapping), Some (phrase tiles, clock hands), Little (word tiles). tool.json `modes: ["Mi día", "El día de Martina", "Comparar", "Nuestro horario"]`, `minutes: "15-25"`, `grades_label: "Grades K-12"`.
- Nothing is saved; `Print` prints both days and the comparison.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| ACTFL Novice Mid (telling time) | Set each card's time on the clock and hear "Son las nueve y media." | the clock and the time phrase | 2 |
| ACTFL Novice Mid (daily activities, reflexive verbs) | Place routine cards; the little "me" lights with a "who does it to whom" picture | the routine card and picture | 3 |
| ACTFL Novice Mid (classes) | Place class cards and say "Tengo matemáticas a las nueve." | the class card with time | 3 |
| ACTFL Novice Mid (simple comparisons) | Fill frames comparing two days ("Yo almuerzo a las doce. Martina almuerza a la una.") | the comparison with both days | 4 |

## Screens and modes
Header (kit): title "Mi Día"; `Mi día`, `El día de Martina`, `Comparar`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A long day strip from sunrise to night with a big clock above it and a deck of picture cards; a message from Martina pops up: "¡Hola! ¿Cómo es tu día?" First hint: "Tap Martina's message to hear it." The first tap plays it; the welcome is queued after it (`welcomeAfter: true`).

**Mi día.** The student drags cards onto the strip. Routine: me despierto, me levanto, me ducho, me visto, me cepillo los dientes, desayuno, voy a la escuela, almuerzo, vuelvo a casa, hago la tarea, ceno, me acuesto. Classes: matemáticas, ciencias, inglés, arte, música, educación física, historia, recreo. Each card asks for a time: the student sets the clock (tap hours and minutes at Lots help; drag hands at Some and Little), and hears "Es la una." or "Son las dos y media." Routine cards with "me" show the little word lighting and a tiny picture: a girl washing herself (me ducho) beside a girl washing a dog (baño al perro), so "me" means doing it to yourself.

**El día de Martina.** Martina, twelve, goes to a school in Santiago with the full school day (jornada escolar completa): about 8:00 to 15:30, two recreos, almuerzo at school about 13:00, then afternoon classes. Her strip is laid out for the student to explore and hear.

**Comparar.** The two strips line up. The student fills about six frames: "Yo almuerzo a las ___. Martina almuerza a las ___." "Yo tengo ___ a las ___. Ella tiene ___ a las ___." "Los dos ___." Then the finished day plays back as a short spoken paragraph in Spanish.

**Nuestro horario.** On the projector, the class builds its real schedule and says each time.

At 1366x768 the clock and strip fit; at 680x425 the strip scrolls sideways inside its own frame (the page itself never scrolls sideways).

## Content
- Cards, times and Martina's day written for Curio Class with the spanish engine's word records and audio.
- Time phrases: es la una, son las dos; y cuarto, y media, menos cuarto. A note says many Spanish-speaking schools and timetables also use the 24-hour clock (las 15:30).
- Martina's schedule is a typical full school day in Chile, labeled "a typical day, schools differ".

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Cards can be moved and times changed any time; cards keep the strip in time order.
- With Motion off the clock hands jump to the time and cards drop into place without sliding.

## Look
- Accent `--brand` #1f5d7a clock blue (header, clock rim, strip); gold #f4c542 (the clock hands, the lit "me"); paper #eff6f9; ink #0a1f29; muted #4a5c66. Scene: a sunrise-to-night strip under a big wall clock.
- Contrast (WCAG 2.1, computed): white on brand 7.23:1; brand on paper 6.62:1; ink on paper 15.49:1; muted on paper 6.38:1; ink on gold 10.41:1.
- Never color alone: times are written as words and numerals; "me" is underlined.
- Different from this batch (party magenta, blocks green, library brown, museum violet).

## Art
- People art goes to Gemini: Martina (a Chilean girl of about twelve in a school uniform with a backpack), 4 poses; routine card pictures with a child (about 14, a mix of children); "illustrated child <routine action>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): a school courtyard in Santiago with the Andes behind (1); class card icons (8).
About 27 images. Drawn in code: clock, strip, frames.

## Voice
Bank voice `bright-teacher` as the English hint voice and the card voice in Spanish (unique in this batch); Martina is read by `big-sister` in Spanish with a Chilean accent (unique in this batch). `Curio.voice` with `scope: () => state.view + ':' + state.card`, `welcomeAfter: true`.
- how `welcome`: "Build your day in Spanish. Put each thing on the strip and set its time."
- event `card`: the card in Spanish.
- event `time`: the time phrase.
- event `me`: "Me ducho. I wash myself."
- event `martina`: Martina's lines.
- event, whole, `day`: the day as a paragraph.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
spanish (`kit/spanish.js`, `__tool.es`), described in full in tools/calendario-vivo/spec.md. This tool uses: word records with audio, `es.say`, `es.num` for the hours and minutes, `es.tiles` and `es.check` for the frames. The clock, the strip and the reflexive pictures are tool-only code.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Time | Leave every card at the default time | Each card asks for a time; the paragraph reads the times back, and a day with all cards at one time asks "¿Todo a las ocho?" |
| Reflexives | Drop "me" | `es.check` keys "me" on reflexive routine verbs. |
| Compare | Copy Martina's times | The "yo" frames read the student's own strip. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the message: `martina`, `welcome` (queued, first time).
2. Mi día: `card` on drop, then `time` (waits) once set; `me` the first time a reflexive card is placed.
3. Comparar: `day` (whole) at the end.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| ACTFL Novice Mid: lists and memorized phrases on familiar topics | ACTFL Proficiency Guidelines 2012, Speaking, Novice Mid | NCSSFL-ACTFL Can-Do Statements (2017), Novice Mid | yes |
| Spanish tells time with "es la una" and "son las" plus y cuarto, y media, menos cuarto | Real Academia Española, Diccionario panhispánico de dudas, "hora" | Instituto Cervantes, Plan curricular, A1 notions (time) | yes |
| Reflexive routine verbs use me, te, se (me levanto, me ducho) | Real Academia Española, Nueva gramática, reflexive pronouns | Instituto Cervantes, Plan curricular, A1 grammar | yes |
| Chile's Law 19.532 (1997) created the full school day (Jornada Escolar Completa), with classes morning and afternoon | Wikipedia (es), Jornada Escolar Completa (checked 2026-11-09) | Biblioteca del Congreso Nacional de Chile, Ley 19.532 | yes |
Backed twice: 4. Cut: 0.

Design choices (not claims): Martina's exact class times are a typical day, labeled "schools differ".

Checks run (Python, scratchpad b26, 2026-11-09): the saved JEC page names Law 19532 published November 17, 1997; the time phrase function returns "Es la una", "Son las nueve y media" and "Son las tres menos cuarto" for 1:00, 9:30 and 2:45; every reflexive card carries "me"; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 clock and strip fit; at 680x425 the strip scrolls inside its frame and the page never scrolls sideways.
2. Times set on the clock and speak. (ACTFL Novice Mid)
3. Routine cards light "me" with the picture. (ACTFL Novice Mid)
4. Class cards and Martina's day speak. (ACTFL Novice Mid)
5. Comparison frames check and the day plays back. (ACTFL Novice Mid)
6. Help levels behave as in Who and how.
7. Nuestro horario and Print work.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: clock and cards jump into place; no network requests.

## Open questions
- Spanish audio review: see calendario-vivo (default used: a fresh agent checks the text, and Sara or Cory listens to a sample of 20 lines).

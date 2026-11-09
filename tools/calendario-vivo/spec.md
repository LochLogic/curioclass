# Calendario Vivo

## One idea
The student keeps a living wall calendar in Spanish with Lucía, a pen pal in Buenos Aires: every day, number, month, color and weather sticker is spoken when tapped, the student sets the date and the weather, colors in plans and answers Lucía's small requests ("Mi cumpleaños es el doce de agosto. ¿Qué día de la semana es?"), and then the two calendars sit side by side, where July is summer at home and winter in Buenos Aires, so numbers, colors, days, months, the date and the weather become one daily habit in Spanish.

## Not like
- mi-día (K-12, spec later): daily routine and clock time. Here the calendar, the date and the weather.
- hola-hallway (K-12, spec later): greetings by time of day. Here numbers, colors, days and months.
- asl-bingo-night (K-12, idea, on hold): ASL numbers and time. Here spoken Spanish.
- bike-lane-briefing (8, spec, this batch): data in a news case. Here a calendar sandbox with a pen pal.
- tough-text-club (9-12, spec, this batch): reading hard English texts. Here first words in a new language.

## Who and how
- Grades K to 12, World Languages (Spanish), module "Numbers, Colors and Calendar". Standard: ACTFL Novice Low (memorized words and phrases).
- Driver: one student; class mode is "Calendario de la mañana", a morning calendar routine on the projector (tool.json `driver: "student"`). Every word on the screen is spoken in Spanish on tap; the hint voice speaks English.
- Three levels pick themselves from a first choice and can be changed any time: Tap and hear (K to 2: tap, hear, color; no reading needed), Pen pal (3 to 8: requests and short answers), Full date (9 to 12: date sentences, weather reports for both cities, a week plan). tool.json `modes: ["Tap and hear", "Pen pal", "Full date", "Calendario de la mañana"]`, `minutes: "10-20"`, `grades_label: "Grades K-12"`.
- The calendar's colors and stickers are saved on this device only (localStorage), so the habit can continue day to day; the screen says "Your calendar stays on this device. Nothing is uploaded." `Clear my calendar` erases it. If the student records themselves saying the date (optional), the privacy line shows: "Your recording stays on this device. Nothing is uploaded." No speech recognition. `Print` prints the month.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| ACTFL Novice Low (numbers to 31) | Tap any day number to hear it; count down days to a plan | the number spoken and shown in Spanish words | 2 |
| ACTFL Novice Low (colors) | Color in plans by named color from Lucía's requests ("marca el cumpleaños en rojo") | the colored day and the color word | 3 |
| ACTFL Novice Low (days and months) | Answer "¿Qué día de la semana es?" by tapping a day name; set the month | the lowercase day and month names | 3 |
| ACTFL Novice Low (the date) | Build "Hoy es lunes 14 de octubre" from tiles | the date sentence | 4 |
| ACTFL Novice Low (weather) | Set today's weather for both cities with stickers and phrases (hace calor, hace frío, llueve) | the two weather windows | 5 |

## Screens and modes
Header (kit): title "Calendario Vivo"; `Calendario`, `Lucía`, `Dos ciudades`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word. Labels show Spanish first with English underneath in smaller text; Tap and hear shows pictures with the Spanish word.

**On load and first tap.** A big wall calendar in Spanish (weeks start on lunes; day and month names in lowercase) beside a window with today's sky, a box of weather stickers and a jar of colored pencils; a postcard from Lucía is clipped to the corner: "¡Hola! ¿Qué día es hoy?" First hint: "Tap the postcard to hear Lucía." The first tap plays her line; the welcome is queued after it (`welcomeAfter: true`).

**Calendario (free play).** Tap anything to hear it: a day number ("catorce"), a day name ("lunes"), the month ("octubre"), a sticker ("hace sol"), a pencil ("azul"). Drag weather stickers onto days; color days by picking a pencil; set today with a big pin. A countdown chip says how many days are left to a colored plan ("Faltan cinco días").

**Lucía (requests).** About 30 short requests in order of difficulty, three or four per sitting:
- "¿Qué día es hoy?" (tap today's day name)
- "Mi cumpleaños es el doce de agosto. ¿Qué día de la semana es?" (go to August, find 12, tap the day name)
- "Marca mi cumpleaños en rojo." (pick rojo, tap the 12th)
- "¿Qué tiempo hace hoy?" (pick a sticker; the phrase is spoken)
- "¿Cuántos días faltan para el sábado?" (count and tap the number)
Each answer is by tapping; in Full date the student also builds a short written answer from tiles. A wrong tap hears the right word and tries again; there is no score.

**Dos ciudades.** Two windows side by side, the student's town and Buenos Aires, on the same date. In July, home shows hace calor and Buenos Aires shows hace frío; in January the reverse. The student sets both and builds two weather reports: "En mi ciudad hace calor. En Buenos Aires hace frío." A short note in English says why: the seasons are opposite in the Southern Hemisphere. Full date adds the average temperature on Lucía's side (about 11 °C in July and about 25 °C in January) with a °C label and a °F conversion.

**Calendario de la mañana.** On the projector: today's date, a weather pick by the class, and a count of days to a class event, all spoken in Spanish.

At 1366x768 the calendar and window fit; at 680x425 the window is above the calendar.

## Content
- Words (each with recorded audio): numbers 0 to 31; days lunes to domingo; months enero to diciembre; colors rojo, azul, verde, amarillo, anaranjado, morado, rosado, negro, blanco, gris, marrón; weather hace sol, hace calor, hace frío, hace viento, llueve, está nublado; phrases for the date and Lucía's requests.
- Variants named on word cards: the first of the month is "el primero" in Argentina and much of Latin America and "el uno" in Spain, and both are accepted; anaranjado and naranja, morado and violeta, rosado and rosa are both shown. A culture note says that in Buenos Aires friends usually say "vos" instead of "tú"; Lucía uses "tú" in this tool to match most beginner classes.
- Lucía, her postcards and requests written for Curio Class.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Nothing is ever locked in free play; requests wait until the student opens them.
- With Motion off stickers drop in place without falling and pages change without flipping.

## Look
- Accent `--brand` #0f6b70 calendar teal (header, calendar frame, request cards); gold #f4c542 (today's pin, the countdown chip); paper #eef7f7; ink #042224; muted #47605f. Scene: a bright kitchen wall with a window.
- Contrast (WCAG 2.1, computed): white on brand 6.25:1; brand on paper 5.74:1; ink on paper 15.31:1; muted on paper 6.21:1; ink on gold 10.25:1.
- Pencil colors are the color words themselves and always carry the word on the pencil.
- Never color alone: every colored day shows its color word on focus and in print; stickers have words.
- Different from this batch (newsroom navy, lane green, rust, club purple).

## Art
- People art goes to Gemini: Lucía (an Argentine girl of about twelve with a scarf), 4 poses including waving and holding a postcard; "illustrated friendly pen pal <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): a Buenos Aires street with jacaranda trees in bloom (spring) (1), the same street in winter rain (1), a sunny American suburb street (1), the same street in snow (1), a kitchen wall (1).
About 9 images. Drawn in code: calendar, stickers, pencils, countdown chip.

## Voice
Bank voice `bright-teacher` as the hint voice in English and the word voice in Spanish (unique in this batch); Lucía's lines are read by `playful-friend` in Spanish with a Buenos Aires accent (unique in this batch). Spanish lines are generated with the bank voices and a Spanish style ("Say in clear, friendly Spanish, ..."), one file per word or phrase. `Curio.voice` with `scope: () => state.view + ':' + state.item`, `welcomeAfter: true`.
- how `welcome`: "This is your Spanish calendar. Tap anything to hear it, and help Lucía with her questions."
- event `word`: the tapped word in Spanish.
- event `lucia`: Lucía's request in Spanish, then the English hint.
- event `right`: "¡Sí!" then the word again.
- event `again`: the right word in Spanish, then "Try again."
- event `seasons`: "Same day, opposite seasons."
- event `privacy`: the privacy line.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
spanish (`kit/spanish.js`, `__tool.es`), described here in full; the other Spanish tools say what they use.
- **Words**: a tool passes word records `{id, es, en, audio, pic?, variants?: [{es, where}], gender?: 'm'|'f'}`. `es.say(id)` plays the word's audio through `Curio.voice` so it follows the newer-line-wins rule; `es.card(id)` returns a word card element (Spanish large, English small, picture if given, variant note).
- **Numbers**: `es.num(n, {gender})` returns the Spanish words for 0 to 100 ("veintiuno", "veintiún", "veintiuna"; "treinta y uno"); audio ids follow `num-<n>`.
- **Dates**: `es.date(d, {weekday: true, first: 'primero'|'uno'})` returns "lunes 14 de octubre" with lowercase names and "primero" or "uno" for day 1; `es.weekStart` is Monday; `es.days` and `es.months` hold the names.
- **Tiles**: `es.tiles(el, words, {target})` lays out word tiles to build a phrase; `es.check(built, keys)` compares after folding case, spacing and missing accents, and returns `{ok, accentNote}` so a missing accent is accepted with a gentle note.
- **Speech**: no speech recognition anywhere in the family; recording uses the kit recorder with the on-device privacy line.
Tool-only code here: the calendar, stickers, pencils, Lucía's request queue, the two-city view, localStorage save.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Requests | Tap everything | Requests take one tap; a wrong tap plays the right word and asks again, and the request stays until answered. |
| Date sentence | Drag tiles at random | `es.check` needs the keyed order and today's real weekday. |
| Two cities | Copy home's weather | The Buenos Aires window is keyed by month; a summer sticker in July asks "¿Hace calor en julio en Buenos Aires?" |
This is a sandbox first: free play has no goals to beat, by design.

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the postcard: `lucia`, `welcome` (queued, first time).
2. Free play: `word` on every tap.
3. Requests: `lucia`; then `right` or `again` on the answer.
4. Dos ciudades: `seasons` when both windows are set.
5. First save: `privacy`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| ACTFL Novice Low: communicates with memorized words and phrases | ACTFL Proficiency Guidelines 2012, Speaking, Novice Low | NCSSFL-ACTFL Can-Do Statements (2017), Novice Low benchmarks | yes |
| In Spanish, day and month names are written in lowercase | Real Academia Española, Ortografía de la lengua española (2010) | Instituto Cervantes / FundéuRAE writing guidance | yes |
| Buenos Aires averages about 11 °C in July and about 25 °C in January | Servicio Meteorológico Nacional (Argentina), climate normals, as tabled in Wikipedia's Climate of Buenos Aires (checked 2026-11-09) | Britannica, Buenos Aires: climate | yes |
| Seasons in the Southern Hemisphere are opposite to the Northern Hemisphere | NASA Space Place, what causes the seasons | National Weather Service, seasons | yes |
| "El primero" is used for the first of the month in much of Latin America and "el uno" in Spain | Real Academia Española, Diccionario panhispánico de dudas, "primero" | FundéuRAE, "el uno de enero / el primero de enero" | yes |
Backed twice: 5. Cut: 0.

Design choices (not claims): Lucía and her requests are made up; temperatures are rounded and labeled "average".

Checks run (Python, scratchpad b24, 2026-11-09): the saved climate table has July means of 11.0 and 11.3 °C and January means of 24.9 and 24.5 °C from two stations; `es.num` sample outputs for 1, 21, 31 and 100 match the word list; August 12, 2026 falls on a Wednesday (miércoles), as the sample request's key says; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 calendar and window fit; at 680x425 the window is above.
2. Every number, day, month, color and sticker speaks in Spanish on tap. (ACTFL Novice Low)
3. Lucía's requests take taps and color picks, with variants accepted. (ACTFL Novice Low)
4. The date sentence builds and checks with today's real weekday. (ACTFL Novice Low)
5. Dos ciudades keys opposite seasons and builds two reports. (ACTFL Novice Low)
6. The three levels behave as in Who and how; Tap and hear needs no reading.
7. The calendar persists on this device, the privacy lines show, and Clear my calendar erases; with storage blocked it still works for the session.
8. Calendario de la mañana and Print work.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: stickers and pages change without moving; no network requests.

## Open questions
- Spanish audio is made with the bank voices told to speak Spanish; who listens to it before release? (default used: a fresh agent checks every Spanish word and phrase in text, and Sara or Cory listens to a sample of 20 lines before release)

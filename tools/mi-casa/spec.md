# Mi Casa

## One idea
The student explores a busy house on the morning of Abuela's birthday party, taps people and rooms to hear them in Spanish (la cocina, el tío, la abuela es simpática), then helps cousin Diego by answering the family's questions (¿Dónde está el gato? ¿Quién es alta?) with short phrases, while describing words light up as their endings change with the person (el tío es alto, la tía es alta, los primos son altos), so they learn family, home and describing words and that adjectives agree with the people they describe.

## Not like
- asl-family-tree (K-12, idea, on hold): ASL sentences about people and places. Here spoken Spanish.
- mi-día (K-12, spec, this batch): a daily routine on a clock. Here people and places in a house.
- calendario-vivo (K-12, spec): dates and weather. Here family and home.
- el-restaurante (K-12, spec): ordering food. Here describing people and finding them.
- opinion-builder (3-5, spec, this batch): English opinion letters. Here Spanish descriptions.

## Who and how
- Grades K to 12, World Languages (Spanish), module "Family and Home". Standard: ACTFL Novice Mid (lists and memorized phrases to answer simple questions).
- Driver: one student; class mode is "¿Dónde está?", where the projector shows the house and the class answers each question together (tool.json `driver: "student"`). Every person, room and object speaks in Spanish on tap; the hint voice speaks English.
- Explore mode, Help mode (about 24 family questions) and Describe mode. Help levels: Lots (pictures and full phrases), Some (phrase tiles), Little (word tiles). tool.json `modes: ["Explorar", "Ayudar", "Describir", "¿Dónde está?"]`, `minutes: "10-20"`, `grades_label: "Grades K-12"`.
- Nothing is saved; `Print` prints the student's three family descriptions.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| ACTFL Novice Mid (family and rooms) | Tap people and rooms to hear and see their names | the word card with picture | 2 |
| ACTFL Novice Mid (answer simple questions: where) | Answer ¿Dónde está...? by tapping the room and choosing "Está en la cocina." | the answer phrase and the found person | 3 |
| ACTFL Novice Mid (answer simple questions: who) | Answer ¿Quién es...? by tapping the person and choosing "Es mi prima." | the answer phrase | 3 |
| ACTFL Novice Mid (descriptions with agreement) | Build descriptions where the adjective matches gender and number | the adjective ending lit as it changes | 4 |

## Screens and modes
Header (kit): title "Mi Casa"; `Explorar`, `Ayudar`, `Describir`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A cutaway two-story house, every room busy on party morning: balloons going up in la sala, a cake in la cocina, a cat asleep on a bed. Cousin Diego, about ten, waves at the front door: "¡Hola! Soy Diego. ¿Me ayudas?" First hint: "Tap Diego to hear him." The first tap plays his line; the welcome is queued after it (`welcomeAfter: true`).

**Explorar.** Tap anyone or anything: rooms (la sala, la cocina, el comedor, el baño, el dormitorio, el patio), people (la abuela, el abuelo, la mamá, el papá, la tía, el tío, la prima, el primo, el hermano, la hermana, el bebé), pets and objects (el gato, el perro, el pastel, los globos). Each person has a short description card ("La tía Rosa es alta y divertida."). People move between rooms as the morning goes on.

**Ayudar.** Family members ask short questions; the student answers by tapping the right person or room and choosing a phrase: "¿Dónde está el gato?" "Está en el dormitorio." "¿Quién es alta?" "La tía Rosa es alta." "¿Dónde están los globos?" "Están en la sala." Wrong taps hear the right answer and try again. Descriptions come in pairs so the ending change is heard and seen: "El tío Luis es alto." "La tía Rosa es alta." The ending lights and a small "o/a" or "s" badge shows on the word.

**Describir.** The student describes three family members from word tiles (person, es or son, adjective). `es.check` tests agreement: "Los primos son altos." "La abuela es simpática." The party starts when everyone is in the right room and three descriptions are built.

**¿Dónde está?** On the projector, the class answers the family's questions together.

At 1366x768 the house and panel fit; at 680x425 the panel is below.

## Content
- A Dominican American family in New York City getting ready for Abuela Carmen's seventieth birthday: written for Curio Class, with Caribbean Spanish voices and a few family words (abuela, tía, primo) everyone in the Spanish-speaking world shares.
- Adjectives: alto, bajo, simpático, divertido, cansado, contento, joven, mayor (mayor and joven don't change for gender, which the badge shows).
- Ser for describing and estar for location are shown by example only, without grammar terms at Lots help.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Explore never ends; questions wait until opened.
- With Motion off people appear in their new room without walking and balloons don't float.

## Look
- Accent `--brand` #a8285f party magenta (header, balloons, panel); gold #f4c542 (the changing ending, the cake candles); paper #fcf2f6; ink #2e0a1a; muted #6b5160. Scene: a bright family apartment on party morning.
- Contrast (WCAG 2.1, computed): white on brand 6.70:1; brand on paper 6.12:1; ink on paper 16.32:1; muted on paper 6.45:1; ink on gold 10.99:1.
- Never color alone: endings are underlined and shown with a badge.
- Different from this batch (clock blue, blocks green, library brown, museum violet).

## Art
- People art goes to Gemini: eleven family members (a Dominican American family of mixed skin tones, Abuela Carmen in her seventies, a tía who uses a wheelchair), 2 poses each, plus Diego with 4; "illustrated <family member> getting ready for a party <pose>, soft gouache, plain white background"; 1:1; cutout yes. The family's depiction goes to the fresh-agent review.
- Local FLUX (`scripts/localart.py`): the cutaway apartment as a base (1); objects (cake, balloons, cat, dog, gifts) (5).
About 33 images. Drawn in code: room labels, question cards, tiles.

## Voice
Bank voice `upbeat-guide` as the English hint voice (unique in this batch); Diego and the children are read by `casual-peer` and the adults by `gentle-storyteller`, both in Spanish with a Dominican accent (unique in this batch). `Curio.voice` with `scope: () => state.view + ':' + state.item`, `welcomeAfter: true`.
- how `welcome`: "It's Abuela's birthday. Explore the house, then help the family find everyone."
- event `word`: the tapped word or description in Spanish.
- event `ask`: the family member's question.
- event `right`: "¡Gracias!" then the answer again.
- event `again`: the right answer, then "Try again."
- event `ending`: "Alto, alta. The ending changes with the person."
- event `party`: "¡Feliz cumpleaños, Abuela!"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
spanish (`kit/spanish.js`, `__tool.es`), described in full in tools/calendario-vivo/spec.md. This tool uses: word records with `gender` and audio, `es.say`, `es.card`, `es.tiles` and `es.check`. The house, moving people, questions and agreement badges are tool-only code.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Where | Tap every room | Each question takes one tap; a wrong room plays the answer and asks again. |
| Agreement | Use the -o ending always | `es.check` keys the ending to the person's gender and number. |
| Describe | Copy one description three times | The three descriptions must be about three different people. |
Explore is free play with no goals to beat, by design.

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap Diego: his line, `welcome` (queued, first time).
2. Explore: `word` on every tap.
3. Help: `ask`; then `right` or `again`; `ending` the first time a pair appears.
4. Party: `party` when everyone is placed.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| ACTFL Novice Mid: lists and memorized phrases; answers simple questions | ACTFL Proficiency Guidelines 2012, Speaking, Novice Mid | NCSSFL-ACTFL Can-Do Statements (2017), Novice Mid | yes |
| Spanish adjectives agree with the noun in gender and number; adjectives like joven and mayor have one form for both genders | Real Academia Española, Nueva gramática, adjective agreement | Instituto Cervantes, Plan curricular, A1 grammar | yes |
| Ser is used to describe people; estar to say where someone or something is | Real Academia Española, Diccionario panhispánico de dudas, "estar" | Instituto Cervantes, Plan curricular, A1 grammar | yes |
Backed twice: 3. Cut: 0.

Sensitivity note: a Dominican American family shown with care and variety; the tool goes to the fresh-agent review.

Checks run (Python, scratchpad b26, 2026-11-09): every keyed description's adjective form matches its person's gender and number, with joven and mayor unchanged; every Help question has one keyed answer; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 house and panel fit; at 680x425 panel below.
2. Everything in Explore speaks in Spanish on tap. (ACTFL Novice Mid)
3. Where and who questions take taps and phrases. (ACTFL Novice Mid)
4. Descriptions check agreement with lit endings. (ACTFL Novice Mid)
5. The party starts when all are placed and three descriptions are built.
6. Help levels behave as in Who and how.
7. ¿Dónde está? and Print work.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: people appear without walking; no network requests.

## Open questions
- Spanish audio review: see calendario-vivo (default used: a fresh agent checks the text, and Sara or Cory listens to a sample of 20 lines).

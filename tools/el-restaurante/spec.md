# El Restaurante

## One idea
The student eats out with two friends at a small family restaurant in Mexico City and orders for the table in Spanish, turn by turn: reading a picture menu, saying what each friend likes and doesn't like (me gusta la sopa, me gustan los tacos, where the noun decides the ending), asking politely (quisiera, ¿me trae...?), asking the server "¿Lleva carne?" to work around a vegetarian friend, and asking for the check, so they learn to hold a real ordering conversation in simple Spanish sentences.

## Not like
- hola-hallway (K-12, spec, this batch): greetings and names in set phrases. Here sentences that state likes and make requests, Novice High.
- consejero (9-12, spec later): opinions with the subjunctive. Here likes, dislikes and polite requests.
- mi-casa (K-12, spec later): family and home words. Here food and ordering.
- calendario-vivo (K-12, spec): a calendar sandbox. Here a conversation with turns.
- i-choose-because (K-2, spec, this batch): choosing with reasons in English. Here ordering in Spanish.

## Who and how
- Grades K to 12, World Languages (Spanish), module "Food and Ordering". Standard: ACTFL Novice High (simple sentences on familiar topics; asks and answers questions).
- Driver: one student; class mode is a printable menu for pair role play plus a projector version where the class answers the server together (tool.json `driver: "student"`). Every menu item and line is spoken in Spanish on tap; the hint voice speaks English.
- Two restaurants: Fonda Doña Lupe in Mexico City and, once the first meal is done, Picantería Rosa in Lima, Peru. Three help levels: Lots (picture tiles, full frames), Some (word tiles, frames), Little (tiles without frames, then typing with `es.check`). tool.json `modes: ["Ciudad de México", "Lima", "Menú para imprimir"]`, `minutes: "15-25"`, `grades_label: "Grades K-12"`.
- Optional: record your own order and play it next to the model; the privacy line shows: "Your recording stays on this device. Nothing is uploaded." No speech recognition. Nothing else is saved; `Print` prints the menu and the student's dialogue.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| ACTFL Novice High (state likes and dislikes) | Build "A Sofía le gusta la sopa" and "No me gustan los frijoles" from tiles; the noun lights to show singular or plural | the sentence with the deciding noun lit | 2 |
| ACTFL Novice High (ask politely) | Order with quisiera or ¿me trae...?; a blunt "¡Dame tacos!" gets a pause, not a buzzer | the server's reaction | 3 |
| ACTFL Novice High (ask questions) | Ask "¿Lleva carne?" or "¿Qué recomienda?" and act on the answer | the server's answer and the vegetarian friend's plate | 4 |
| ACTFL Novice High (answer questions) | Answer the server's turns from drinks to the check | the dialogue strip | 5 |

## Screens and modes
Header (kit): title "El Restaurante"; `Mesa`, `Menú`, `Diálogo`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word. Spanish first, English small beneath at Lots and Some help.

**On load and first tap.** A small fonda with papel picado over the door, a table for three by the window, a handwritten menu with pictures, and the server, Don Ramón, with an order pad: "¡Buenas tardes! ¿Qué van a tomar?" First hint: "Tap Don Ramón to hear him." The first tap plays his line; the welcome is queued after it (`welcomeAfter: true`).

**The menu (Ciudad de México).** Drinks: agua de jamaica, horchata, limonada. Food: sopa de tortilla, chilaquiles verdes, tacos al pastor, quesadillas de flor de calabaza, enchiladas de pollo, frijoles de olla. Dessert: flan, arroz con leche. Tap any item to hear it; each has a picture drawn true to the dish.

**The friends.** Sofía (likes spicy food, doesn't like beans) and Mateo (vegetarian, likes cheese). Each turn a friend speaks ("No me gusta la carne") or the server asks ("¿Y para el joven?").

**Turns.** About 12 turns from drinks to the check. The student builds each answer from tiles. Agreement: "me gusta" before a singular noun, "me gustan" before a plural; the deciding noun glows and a wrong ending gets "¿Los tacos? ¿Cuántos?" with the noun lit. Politeness: a "quisiera" or "por favor" earns a smile; a blunt order earns a pause and "¿Perdón?", and the student can try again. Vegetarian: the student checks dishes by asking "¿Lleva carne?" (the server says the chilaquiles can come without chicken, the enchiladas have chicken, the sopa de tortilla is made with chicken broth here); ordering meat for Mateo makes him say "Ay, no como carne." End: "La cuenta, por favor."

**Diálogo.** The whole meal plays back as a dialogue the student built, with both voices; the student can record their part.

**Lima.** A second restaurant after the first meal: chicha morada, papa a la huancaína, ceviche, lomo saltado, ají de gallina, picarones. A new friend avoids fish. Same turns, new words.

At 1366x768 the table and tiles fit; at 680x425 the menu is a tab.

## Content
- Turns, menus, friends and reactions written for Curio Class, using the spanish engine's word records with audio. Each dish has a one-line culture note in English (where it is eaten, what is in it).
- Agreement and politeness keys with accepted alternates (quisiera, me gustaría, ¿me trae...?, ¿nos trae...?).
- Food is shown with respect: no jokes about any dish, no "weird food" framing.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Tiles can be moved and turns retried at any time; there is no score.
- With Motion off the server doesn't walk to the table and plates appear in place.

## Look
- Accent `--brand` #a23b1c terracotta (header, menu frame, tiles); gold #f4c542 (the deciding noun, the server's smile); paper #fcf3ef; ink #2d0f06; muted #6d5248. Scene: a family fonda with tiled walls.
- Contrast (WCAG 2.1, computed): white on brand 6.61:1; brand on paper 6.04:1; ink on paper 16.24:1; muted on paper 6.51:1; ink on gold 10.92:1.
- Never color alone: the deciding noun is also underlined; reactions are faces with words.
- Different from this batch (hallway blue, town green, night indigo, rewind amber).

## Art
- People art goes to Gemini: Don Ramón (a Mexican man in his sixties with a mustache and apron), 4 poses; Sofía (a Mexican American girl about twelve) and Mateo (a Black Mexican boy about twelve), 3 poses each; Peruvian server Rosa (a Quechua Peruvian woman in her fifties), 3 poses; "illustrated friendly restaurant server <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): the fonda interior (1); the Lima picantería (1); each dish on a plate, top view (14, checked against the culture notes).
About 29 images. Drawn in code: menu, tiles, dialogue strip.

## Voice
Bank voice `upbeat-guide` as the hint voice in English (unique in this batch); Don Ramón and Rosa are read by `friendly-dad` and Sofía, Mateo and the menu by `big-sister`, both in Spanish (unique in this batch), with a Mexico City accent for the fonda and a Lima accent for the picantería. `Curio.voice` with `scope: () => state.place + ':' + state.turn`, `welcomeAfter: true`.
- how `welcome`: "You're ordering for the table. Read the menu, listen to your friends, and ask nicely."
- event `line`: the server's or friend's line in Spanish.
- event `item`: the tapped menu item.
- event `agree`: "¿Los tacos? ¿Cuántos?" then the hint "Gusta or gustan? Look at the noun."
- event `blunt`: "¿Perdón?" then the hint "Try asking more politely."
- event, whole, `dialogue`: the built dialogue.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
spanish (`kit/spanish.js`, `__tool.es`), described in full in tools/calendario-vivo/spec.md. This tool uses: word records with audio and `es.say`, `es.card` for menu items, `es.tiles` and `es.check` for answers. The turn script, reactions, menus and the vegetarian logic are tool-only code.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Agreement | Always use "gusta" | Plural nouns are keyed to "gustan"; the noun lights and the turn waits. |
| Politeness | Be blunt every time | The server pauses each time; the meal can't move on until a polite version. |
| Vegetarian | Order at random | Meat dishes for Mateo are refused and he says why. |
| Little help | Copy the model | Little help hides the model until the student's version is checked. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap Don Ramón: `line`, `welcome` (queued, first time).
2. Each turn: `line` (waits), then the student's answer; `agree` or `blunt` as they fire.
3. The end: `dialogue` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| ACTFL Novice High: simple sentences, asks and answers questions on familiar topics | ACTFL Proficiency Guidelines 2012, Speaking, Novice High | NCSSFL-ACTFL Can-Do Statements (2017), Novice High | yes |
| "Gustar" agrees with the thing liked: "me gusta" with a singular noun, "me gustan" with a plural | Real Academia Española, Diccionario panhispánico de dudas, "gustar" | Instituto Cervantes, Plan curricular, A1-A2 functions (likes and dislikes) | yes |
| "Quisiera" is a polite way to ask for something | Real Academia Española, Nueva gramática (courtesy uses of the subjunctive imperfect) | Instituto Cervantes, Plan curricular, requests | yes |
| The Mexico City and Lima dishes are typical of each place, with the ingredients in their notes | Britannica, Mexican cuisine and Peruvian cuisine | Wikipedia, each dish's article | yes |
Backed twice: 4. Cut: 0.

Sensitivity note: food culture from two countries, shown with respect and with accents from each place; the tool goes to the fresh-agent review.

Checks run (Python, scratchpad b25, 2026-11-09): the agreement key gives "gustan" for every plural menu noun and "gusta" for every singular one; each friend can be served a full meal from the menu; Mateo has at least three meat-free dishes in Mexico City and the Lima friend at least three fish-free dishes; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 table and tiles fit; at 680x425 the menu is a tab.
2. Like and dislike sentences check gusta and gustan with the noun lit. (ACTFL Novice High)
3. Polite and blunt orders get different reactions, never a buzzer. (ACTFL Novice High)
4. "¿Lleva carne?" answers steer the vegetarian order. (ACTFL Novice High)
5. The meal runs drinks to check, and the dialogue plays back. (ACTFL Novice High)
6. Lima opens after the first meal; the printable menu prints.
7. Help levels behave as in Who and how; recording shows the privacy line.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: no walking or sliding; no network requests.

## Open questions
- Spanish audio review: see calendario-vivo (default used: a fresh agent checks the text, and Sara or Cory listens to a sample of 20 lines).

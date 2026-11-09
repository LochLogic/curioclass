# ¿Por Dónde?

## One idea
On their first day in San Lorenzo, a made-up city laid out like many Latin American cities on a grid around a central plaza, the student asks locals the way politely and follows their spoken directions (sigue derecho dos cuadras, dobla a la izquierda, cruza la plaza) on foot, by bus and by metro, then lost tourists ask the student and walk exactly what the student tells them, so a "derecha" that should be "izquierda" sends them the wrong way, and the student learns to ask for, understand and give directions in Spanish.

## Not like
- mundo-hispano (6-12, spec): a culture map of real countries. Here directions in one made-up city.
- mi-casa (K-12, spec): finding people in a house. Here finding places in a city.
- verb-conjugation-race (6-12, spec, this batch): verb forms at speed. Here commands with a place and a purpose.
- detective-del-pasado (6-12, spec): placing past events on a timeline. Here placing a route on a map.
- math-explainer (3-5, spec): a classmate replays your math words. Here a tourist walks your Spanish directions.

## Who and how
- Grades 6 to 12, World Languages (Spanish), module "Travel and Directions". Standard: ACTFL Intermediate Low (asks and answers simple questions, simple sentences).
- Driver: one student; class mode is "Mapa en parejas", a printable map for pairs where one gives directions and the other traces (tool.json `driver: "student"`). Every place name and line is spoken in Spanish on tap; the hint voice speaks English.
- Help levels: Lots (direction tiles with arrows, the route drawn as the local speaks), Some (tiles without arrows), Little (no tiles while listening; typing with `es.check` when giving). tool.json `modes: ["Pregunta", "Ayuda al turista", "Mapa en parejas"]`, `minutes: "20-30"`, `grades_label: "Grades 6-12"`.
- Nothing is saved; `Print` prints the map with the student's routes and the pairs map.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| ACTFL Intermediate Low (ask questions politely) | Choose "Disculpe, ¿dónde está...?" or "¿Cómo llego a...?" | the local's reaction | 2 |
| ACTFL Intermediate Low (understand simple directions, listening) | Trace the route a local speaks | the traced line against the spoken route | 3 |
| ACTFL Intermediate Low (give directions with commands and place words) | Build directions for a tourist from tiles | the tourist walking each step | 4 |
| ACTFL Intermediate Low (transport) | Choose bus, metro or on foot and say the stop | the route with transport legs | 3 |

## Screens and modes
Header (kit): title "¿Por Dónde?"; `Pregunta`, `Ayuda al turista`, `Mapa`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word. Spanish first.

**On load and first tap.** A bird's-eye map of San Lorenzo: a plaza with a church and a fountain in the middle, straight streets in a grid, a park, a market, a metro line and two bus routes. The student's dot stands outside the bus station with a phone list: la farmacia, el museo, la estación de metro, el mercado, la biblioteca. "Pregunta a alguien." First hint: "Tap a person on the street to ask them." The first tap starts the asking; the welcome is queued after it (`welcomeAfter: true`).

**Pregunta (listening).** The student picks a polite opener ("Disculpe, ¿dónde está la farmacia?" or "Perdón, ¿cómo llego al museo?"); a blunt "¿Farmacia?" gets a puzzled look and the polite version. The local answers aloud in two to four steps: "Sigue derecho dos cuadras. En la esquina, dobla a la izquierda. La farmacia está al lado del banco." The student traces the route on the map with a finger or the arrow keys; each step lights as it is traced. A wrong turn makes the dot stop with "¿A la izquierda o a la derecha?" and the line replays. Longer trips add transport: "Toma el metro, línea 2, hasta la estación Plaza. Bájate allí."

**Ayuda al turista (speaking).** Three lost tourists in turn, each with a place to reach. The student builds directions from tiles: sigue derecho, dobla a la derecha, dobla a la izquierda, cruza la plaza, toma el autobús, bájate en, una cuadra, dos cuadras, está al lado de, enfrente de, entre, en la esquina. The tourist walks exactly what is said, step by step. A wrong word sends them the wrong way, and they stop and say where they are ("Estoy enfrente del cine. ¿Y ahora?"). A tourist who arrives thanks the student and the place name is added to the map.

**Regional words.** A small card shows that the same thing has different names in different places: el autobús (also el camión in Mexico, la guagua in the Caribbean, el colectivo in Argentina); la cuadra (Latin America) and la manzana (Spain).

**Mapa en parejas.** A printable map and direction cards for pairs.

At 1366x768 the map and tiles fit; at 680x425 the tiles are a drawer.

## Content
- San Lorenzo, its places, locals' directions (about 20 routes) and tourists' goals written for Curio Class. Locals use usted with the student only when the student uses it; commands are in the tú form, as many locals use with a young person, with the usted form shown in a note.
- The city is made up and not modeled on any one real city.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Routes can be traced again and directions rebuilt any time.
- With Motion off the tourist jumps from corner to corner with a numbered step instead of walking, and traced lines appear whole.

## Look
- Accent `--brand` #0e6655 plaza green (header, parks, the student's dot); gold #f4c542 (the traced route, the tourist's path); paper #eff7f5; ink #06231d; muted #4a5e59. Scene: a sunny city grid around a plaza.
- Contrast (WCAG 2.1, computed): white on brand 6.88:1; brand on paper 6.32:1; ink on paper 15.24:1; muted on paper 6.35:1; ink on gold 10.20:1.
- Never color alone: streets and places are labeled with names and icons; routes are numbered steps.
- Different from this batch (rally red, lab blue, plum, playroom orange).

## Art
- People art goes to Gemini: six locals (a newspaper seller, a police officer, a grandmother with a market bag, a teen on a bike, a bus driver, a shopkeeper) and three tourists (a family from Brazil, a backpacker from Japan, an older couple from Canada), 2 poses each; "illustrated friendly <person> on a city street <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Drawn in code: the whole map (streets, plaza, metro, bus routes, place icons) for clarity.
About 18 images.

## Voice
Bank voice `upbeat-guide` as the English hint voice (unique in this batch); locals are read by `friendly-dad` and `knowing-guide`, and tourists by `smooth-narrator` speaking Spanish as learners do, clear and a little slow (each unique in this batch). Locals use a neutral Latin American accent. `Curio.voice` with `scope: () => state.mode + ':' + state.route + ':' + state.step`, `welcomeAfter: true`.
- how `welcome`: "You're new in town. Ask someone the way, then follow what they say on the map."
- event, whole, `directions`: the local's directions.
- event `wrongturn`: "¿A la izquierda o a la derecha?"
- event `tourist`: the tourist's question or "¿Y ahora?"
- event `arrived`: "¡Llegué! ¡Muchas gracias!"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
spanish (`kit/spanish.js`, `__tool.es`), described in full in tools/calendario-vivo/spec.md. This tool uses: word records with audio and `es.say`, `es.num` for blocks and line numbers, `es.tiles` and `es.check` for directions. The map, routes, tracing and the literal tourist walker are tool-only code.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Listening | Trace any path to the place | Tracing follows the spoken steps; a shortcut off the route stops at the first step that differs. |
| Directions | Pile up "sigue derecho" | The tourist walks it literally and stops at the city edge. |
| Directions | Copy a local's directions | Tourists start from different corners, so copied routes go wrong. |
| Polite | Ask bluntly | Locals answer only the polite form. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a person: the opener choice, `welcome` (queued, first time).
2. Pregunta: `directions` (whole); `wrongturn` as it fires.
3. Ayuda al turista: `tourist`; the student's directions read back (whole); `arrived`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| ACTFL Intermediate Low: asks and answers simple questions, creates with language in simple sentences | ACTFL Proficiency Guidelines 2012, Speaking, Intermediate Low | NCSSFL-ACTFL Can-Do Statements (2017), Intermediate Low | yes |
| Spanish colonial town planning (Laws of the Indies, 1573) set a central Plaza Mayor with a grid of straight streets, seen in many Latin American cities | Wikipedia, Laws of the Indies (checked 2026-11-09) | Britannica, Laws of the Indies | yes |
| Regional words: camión (Mexico), guagua (Caribbean), colectivo (Argentina) for bus; cuadra for a city block in Latin America | Real Academia Española, Diccionario de la lengua española, entries camión, guagua, colectivo, cuadra | Asociación de Academias de la Lengua Española, Diccionario de americanismos | yes |
| Informal commands for directions (sigue, dobla, cruza, toma, bájate) | Real Academia Española, Nueva gramática, imperative | Instituto Cervantes, Plan curricular, A2 functions (giving directions) | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad b28, 2026-11-09): the saved Laws of the Indies page names the Plaza Mayor and the rectilinear grid; every local's route, walked literally on the map grid, ends at its place; each tourist start corner differs from every local's; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 map and tiles fit; at 680x425 tiles are a drawer.
2. Polite openers get answers; blunt ones get the polite version. (ACTFL Intermediate Low)
3. Traced routes follow the spoken steps, with transport legs. (ACTFL Intermediate Low)
4. Tourists walk the student's directions literally and arrive or stop. (ACTFL Intermediate Low)
5. The map fills with learned place names; the regional words card opens.
6. Help levels behave as in Who and how.
7. Mapa en parejas and Print work.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: corner-to-corner jumps with step numbers; no network requests.

## Open questions
- Spanish audio review: same as calendario-vivo (default used: a fresh agent checks the Spanish text, and Sara or Cory listens to a sample of 20 lines).

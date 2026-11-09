# Detective del Pasado

## One idea
The student solves the case of the missing cake at a town festival in Colombia by listening to four witnesses whose verb tenses are the clues: "Cuando llegué, Marta salía" (she was on her way out as I arrived) and "Cuando llegué, Marta salió" (she left after I arrived) put people in different places, so the student lays imperfect clauses as background bands and preterite clauses as points on a timeline, finds the statement that cannot fit, and writes the report that names what happened, learning to choose preterite or imperfect by meaning when telling a story in the past.

## Not like
- verb-conjugation-race (6-12, spec later): present tense forms at speed. Here two past tenses chosen by meaning, slowly.
- then-what-happened (6-12, spec): English narration in comics. Here Spanish past tenses as evidence.
- consejero (9-12, spec later): advice with the subjunctive. Here the indicative past.
- mundo-hispano (6-12, spec, this batch): reading about traditions on a map. Here listening to witnesses for a timeline.
- time-machine-talk (3-5, spec): English past tense for grades 3 to 5. Here Spanish preterite and imperfect for grades 6 to 12.

## Who and how
- Grades 6 to 12, World Languages (Spanish), module "Past Tenses". Standard: ACTFL Intermediate Mid (strings of sentences on familiar topics), reaching toward Advanced Low (narrating and describing in the past).
- Driver: one student; class mode is "Cambia el verbo", where the projector shows one statement and the class votes which tense clears or catches a suspect (tool.json `driver: "student"`). Every statement plays in Spanish with its text; the hint voice speaks English.
- Two cases: "El pastel perdido" (main) and "El mapa del museo" (second). Help levels: Lots (English gloss under each clause, verbs pre-marked), Some (verbs marked, no gloss), Little (nothing marked). tool.json `modes: ["Caso 1", "Caso 2", "Cambia el verbo"]`, `minutes: "25-35"`, `grades_label: "Grades 6-12"`.
- Nothing is saved; `Print` prints the timeline and the student's report.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| ACTFL Intermediate Mid (understand strings of sentences, listening) | Listen to each statement and pull out its clauses | the statement with clauses split | 2 |
| ACTFL Intermediate Mid toward Advanced Low (imperfect for background, ongoing actions, time and weather) | Place imperfect clauses as bands on the timeline | the background bands | 3 |
| ACTFL Intermediate Mid toward Advanced Low (preterite for completed events) | Place preterite clauses as points | the event points | 3 |
| ACTFL Intermediate Mid toward Advanced Low (meaning decides the tense) | Find the contradiction and see that one verb's tense moves a person | the clash marker; the "Cambia el verbo" flip | 4 |
| ACTFL Intermediate Mid (write strings of sentences in the past) | Write the report with background in the imperfect and events in the preterite | the report checked clause by clause | 5 |

## Screens and modes
Header (kit): title "Detective del Pasado"; `Escuchar`, `Línea de tiempo`, `Informe`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word. Spanish first; English gloss only at Lots help.

**On load and first tap.** The community hall in San Benito, a made-up town in Colombia's coffee country, after the festival: paper flags, a stage with a band's instruments, an empty cake stand with crumbs, rain on the windows. Inspectora Valeria Ortega stands by the stand with a notebook: "Escucha bien. El tiempo del verbo importa." First hint: "Tap the inspector to hear her." The first tap plays her line; the welcome is queued after it (`welcomeAfter: true`).

**Escuchar.** Four witnesses, each with a statement of five to seven clauses: Doña Marta (the baker), Julián (the DJ), Camila (twelve, a dancer in the show) and Don Hernán (the hall keeper). Each statement plays aloud with its text. Example from Camila: "Eran las ocho y llovía mucho. La banda tocaba una cumbia. Cuando llegué a la cocina, Julián salía con una caja grande." From Don Hernán: "Cuando Camila llegó, Julián salió de la cocina."

**Línea de tiempo.** A clock line from 7:30 to 9:00 with a lane per person. The student drags each clause onto it: imperfect clauses stretch into bands (llovía, la banda tocaba, Julián salía) and preterite clauses drop as points (llegué, salió, se fue la luz). The tense decides the shape: dropping "salía" as a point, or "salió" as a band, is refused with a hint. A band and a point that cannot both be true light a clash: Camila's "Julián salía" (already on his way out when she arrived) against Don Hernán's "Julián salió" (left after she arrived) is the first clash, and only one can be true given the lights going out at 8:10.

**Preguntas.** For each clash the student asks one follow-up from a list ("¿Qué hacía Julián cuando llegaste?" "¿Qué pasó después?") and the witness answers, which settles it.

**Informe.** The student writes the report in six to eight clauses from verb tiles in both tenses: background first ("Era de noche y llovía. Todos bailaban."), then events ("A las ocho y diez se fue la luz. Julián llevó el pastel a la oficina."), then the conclusion. `es.check` tests each clause's tense against the timeline. The truth: when the roof began to leak over the cake table, Julián carried the cake to the office to keep it dry and forgot to tell anyone; no one stole it. The cake comes back on stage.

**Cambia el verbo.** One statement with one verb flipped (salía to salió); the timeline redraws and a different person could have done it. On the projector, the class votes before the flip.

At 1366x768 the timeline and statements fit; at 680x425 statements are a tab.

## Content
- Both cases, all statements and reports written for Curio Class, about 50 clauses per case, each tagged with tense, person, time and band or point. Colombian Spanish, with "usted" between adults and the inspector.
- Tense cues are taught by meaning (what was going on, what happened), never by keyword lists alone; "cuando" appears with both tenses on purpose.
- Case 2: a map goes missing from a small museum during a school visit; same tools, new verbs (estaba, había, abrió, cerró, se cayó).

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Clauses can be moved any time; clashes update as soon as a clause lands.
- With Motion off clauses drop into place without sliding and the clash marker appears without a flash.

## Look
- Accent `--brand` #1c4e5c detective teal (header, timeline, notebook); gold #f4c542 (event points, the clash marker); paper #eef5f7; ink #0a1d22; muted #4b5d63. Scene: a rainy community hall after a party.
- Contrast (WCAG 2.1, computed): white on brand 9.16:1; brand on paper 8.30:1; ink on paper 15.71:1; muted on paper 6.25:1; ink on gold 10.66:1.
- Never color alone: bands are striped and labeled "fondo", points are diamonds labeled "evento"; clashes show a symbol and words.
- Different from this batch (earth red, book-group purple, town slate, highlighter olive).

## Art
- People art goes to Gemini: Inspectora Valeria Ortega (a Colombian woman in her forties with a raincoat and notebook), 3 poses; Doña Marta (a baker in her sixties, Afro-Colombian), Julián (a young man with headphones), Camila (a girl of twelve in a dance costume), Don Hernán (an older man with keys), 3 poses each (talking, thinking, surprised); "illustrated <witness> at a town festival <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): the community hall after the festival (1); the hall's kitchen and office (2); the small museum for case 2 (1).
About 19 images. Drawn in code: timeline, bands, points, clash markers, tiles.

## Voice
Bank voice `news-reader` as the English hint voice (unique in this batch); Inspectora Ortega is read by `firm-captain`, Marta and Camila by `big-sister`, and Julián and Don Hernán by `gravel-ranger`, all in Spanish with a Colombian accent (each unique in this batch). `Curio.voice` with `scope: () => state.case + ':' + state.view + ':' + state.clause`, `welcomeAfter: true`.
- how `welcome`: "Listen to each witness. The tense of each verb tells you when things happened. Put them on the timeline."
- event, whole, `statement`: the witness's statement.
- event `shape`: "Salía was going on. Make it a band, not a point."
- event `clash`: "These two can't both be true. Ask a question."
- event `answer`: the witness's answer.
- event `solved`: "¡Caso cerrado!"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
spanish (`kit/spanish.js`, `__tool.es`), described in full in tools/calendario-vivo/spec.md. This tool uses: word records with audio and `es.say`, `es.tiles` and `es.check` (with tense tags in the keys) for the report. The timeline, bands, points, clash finder and cases are tool-only code.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Shapes | Drop every clause as a point | Imperfect clauses are refused as points with the hint. |
| Clash | Guess the culprit | The report's conclusion opens only after both clashes are settled with a question. |
| Report | Use one tense for every clause | `es.check` keys each clause's tense to the timeline. |
| Report | Copy a witness | The report needs clauses from at least three witnesses in time order. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the inspector: her line, `welcome` (queued, first time).
2. Escuchar: `statement` (whole) per witness.
3. Timeline: `shape` and `clash` as they fire; `answer` after each question.
4. Report: `solved` when it checks.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| ACTFL: Intermediate Mid speakers create with language in strings of sentences; narrating and describing in the past is an Advanced-level function | ACTFL Proficiency Guidelines 2012, Speaking, Intermediate Mid and Advanced Low | NCSSFL-ACTFL Can-Do Statements (2017), Intermediate Mid and Advanced Low | yes |
| The imperfect presents a past situation as ongoing or as background (time, weather, what was going on); the preterite presents a completed event | Real Academia Española, Nueva gramática, pretérito imperfecto and pretérito perfecto simple | Instituto Cervantes, Plan curricular, B1 grammar (contrast of past tenses) | yes |
| "Cuando llegué, salía" means the leaving was already under way; "Cuando llegué, salió" means the leaving followed the arriving | Real Academia Española, Nueva gramática, imperfect as a frame for a preterite event | Instituto Cervantes, Plan curricular, B1 grammar | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad b27, 2026-11-09): in case 1, every clause tagged imperfect is a band and every preterite clause a point; the timeline has exactly two clashes, and each is settled by one keyed answer; flipping Camila's "salía" to "salió" removes the first clash; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 timeline and statements fit; at 680x425 statements are a tab.
2. Statements play in Spanish with text, split into clauses. (ACTFL Intermediate Mid)
3. Imperfect clauses make bands and preterite clauses make points; wrong shapes are refused with a hint. (ACTFL Intermediate Mid toward Advanced Low)
4. Clashes light and questions settle them; Cambia el verbo redraws the timeline. (ACTFL Intermediate Mid toward Advanced Low)
5. The report checks each clause's tense, and the cake comes back. (ACTFL Intermediate Mid)
6. Help levels behave as in Who and how; case 2 plays the same way.
7. Cambia el verbo class mode and Print work.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: no sliding or flashing; no network requests.

## Open questions
- Spanish audio review: same as calendario-vivo (default used: a fresh agent checks the Spanish text, and Sara or Cory listens to a sample of 20 lines).

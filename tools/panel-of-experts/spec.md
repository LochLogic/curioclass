# Panel of Experts

## One idea
The child produces a radio show where one big question, "Was the Black Death a turning point?", goes to four experts (a historian, an economist, a geographer and a political scientist, all made for this game and labeled so); while each short segment plays, the child drags key words to that expert's column on the producer's board, pins to an Agree lane the points where two experts say the same thing in their own words (fewer workers, so higher wages), and before the next segment writes the smaller question that expert would ask, then sees the expert's own; at the end the big question has become four smaller ones, and the board shows where all four fields agree (fewer people changed work, wages and power) and what each would study next, so a seventh grader learns how a question carries each field's key ideas and where experts agree on compelling and supporting questions.

## Not like
- historians-disagree (7, spec): two historians compared. Here four fields on one question.
- manor-life (7, spec): daily life before the plague. Here what changed after it.
- house-of-wisdom (7, spec): one book's journey. Here one event through four lenses.
- unlabeled-archive (7, concept): sorting primary sources. Here hearing experts reason.

## Who and how
- Grade 7, Social Studies (Inquiry), module "Panel of Experts". Standards: D1.1.6-8 (explain how a question represents key ideas in the field), D1.2.6-8 (explain points of agreement experts have about interpretations and applications of disciplinary concepts and ideas associated with a compelling question), D1.3.6-8 (explain points of agreement experts have about interpretations and applications of disciplinary concepts and ideas associated with a supporting question).
- Format: explorer. Driver: one child alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Four segments, the producer's board, the closing wrap. Extra: A second show ("Did the printing press change everything?" with the same four fields). tool.json `modes: ["The Black Death", "The printing press"]`, `minutes: "25-35"`, `grades_label: "Grade 7"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D1.1.6-8 | Drag key words from each segment to that expert's column, and match each field to its kind of question | the four columns filling; the field-and-question match card | 2 |
| D1.2.6-8 | Pin points of agreement on the big question to the Agree lane | the Agree lane with linked quotes from two or more experts | 3 |
| D1.3.6-8 | Write each expert's smaller question, compare with theirs, and pin where they agree on it | the smaller-questions row; the expert's question beside the child's | 4 |

## Screens and modes
Header (kit): title "Panel of Experts"; `The Black Death`, `The printing press`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A radio studio: a host's desk, four labeled microphones (History, Economics, Geography, Political science), an ON AIR light, and the producer's board on the wall with three lanes: Key ideas, Agree, Smaller questions. The welcome is queued (`welcomeAfter: true`): "You're producing today's show. The big question: was the Black Death a turning point? Four experts will answer. Your job is to catch what each one cares about. Tap ON AIR to start." First hint: "Tap ON AIR."

**The segments (focus: the transcript and the board).** At 1366x768 the transcript sits left and the board right; at 680x425 tabs. Each segment is about 150 words of text, read aloud by its voice.
1. The historian: plague reached Europe in 1347 through Mediterranean ports and killed perhaps a third to a half of Europe's people by 1351 (estimates vary); old ways like serfdom weakened over the next century, but it's hard to say the plague alone caused that. Key words: change over time, causes, sources, before and after.
2. The economist: with fewer workers, land was plentiful and labor scarce, so wages rose; in England, records show real wages rising in the century after the plague. Key words: supply, demand, wages, prices, scarcity.
3. The geographer: the plague spread along trade routes, ship by ship and town by town, reaching ports first; crowded towns suffered; some villages emptied and were never resettled. Key words: routes, spread, location, settlement, distance.
4. The political scientist: governments tried to hold wages down (England's Ordinance of Labourers of 1349 and Statute of Labourers of 1351); workers resisted, and anger over wages and taxes fed the Peasants' Revolt of 1381. Key words: laws, power, rulers, revolts, rights.
- The child drags key words from the transcript to the expert's column. A wrong-column drop plays "Which expert would use that word most?"

**Agree (D1.2.6-8).** When two experts say the same thing in their own terms (the economist: "labor was scarce, wages rose"; the political scientist: "laws tried to stop wages rising"), the child pins both quotes together in the Agree lane. Three agreements to find on the big question.

**Smaller questions (D1.3.6-8).** Before each next segment, the child writes the smaller question that expert would ask (tiles plus a free line): history "What changed and what stayed the same after 1350?"; economics "What happened to wages and prices?"; geography "How did the plague spread, and where?"; political science "How did rulers and workers struggle over power?". The expert's own question appears beside the child's. Then the child pins where experts agree on one smaller question (the historian and economist both answer "What happened to wages?" with rising pay).

**The wrap (the aha).** The host: "So the big question was really four questions." The board shows where all four fields agree: fewer people changed work, wages and power. The child writes one sentence: "The Black Death was / was not a turning point because ___." Narrator: "Each field asks its own question. Where they meet is where the answer is strongest."

**The end.** The full board and the sentence. `Print` prints them as a producer's sheet.

**The printing press (extra).** A second show with the same four fields and a new big question.

## Content
- Four segments (about 150 words each, made for this game from real scholarship and labeled), key word sets, three Agree pairs on the big question, four smaller questions with the experts' versions, one Agree on a smaller question, the printing-press show.
- The experts and host are made up and labeled; the dates, death-toll ranges, laws and revolt are real.
- Death is named plainly in numbers and ranges, with no images of the sick or dead.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Each segment can be replayed; text and audio stay in step.
- Agree pins need quotes from two different experts.
- Keyboard: Tab to the transcript's words, the board lanes and pins; Enter to pick up and drop.
- With Motion off the ON AIR light doesn't pulse.

## Look
- Accent `--brand` #116466 studio teal (header, the board, microphones); gold #f4c542 (ON AIR, an Agree pin); paper #eef6f6; ink #042122; muted #4a5a5a.
- Contrast (WCAG 2.1, computed): white on brand 6.91:1; brand on paper 6.30:1; ink on paper 15.37:1; muted on paper 6.60:1; ink on gold 10.36:1.
- Never color alone: each field's column carries its name and an icon (scroll, coin, map pin, gavel); Agree pins carry a link symbol.
- Different from this batch (lapis blue, desert sienna, steppe olive, heraldic red).

## Art
- Public domain: a map of the plague's spread is drawn in code from published routes; one late medieval manuscript image of town life (not of the dying), rights checked at build, with credit.
- Local FLUX (`scripts/localart.py`): the radio studio (1, 16:9).
- People art goes to Gemini with `people: true`: the host and four experts (5; cutout yes), varied in age and background.
- Drawn in code: the board, lanes, pins, the spread map, the wage line.
About 7 images.

## Voice
Five bank voices, each unique in this batch: `lively-host` as the host and narrator; `calm-professor` as the historian; `clear-teacher` as the economist; `big-sister` as the geographer; `casual-peer` as the political scientist. `Curio.voice` with `scope: () => state.mode + ':' + state.segment + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each segment.
- how `words`: "Drag key words to this expert's column."
- how `agree`: "Pin two quotes that say the same thing."
- how `smaller`: "Write the smaller question this expert would ask."
- event, whole, each expert's own question.
- how `wrap`: "Finish the sentence: was it a turning point?"
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the transcript with draggable words, the producer's board with three lanes, Agree pins, the smaller-questions row, the wrap sentence.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Key words | Drag every word to one column | Each word checks its field; the miss names the better field. |
| Agree | Pin two quotes from the same expert | Pins need two different experts saying the same idea. |
| Smaller questions | Leave blanks | The next segment waits for a question. |
| Wrap | Leave the because blank | Print waits for it. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Segment (whole), waits.
2. `words`; `agree`.
3. `smaller`; the expert's question (whole).
4. `wrap`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D1.1.6-8, D1.2.6-8 and D1.3.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Plague reached Europe through Mediterranean ports in 1347 and killed perhaps a third to a half by 1351; estimates vary | Encyclopaedia Britannica, "Black Death" | Benedictow, "The Black Death 1346-1353" (Boydell, 2004) | yes, as a range |
| Wages rose after the plague as labor grew scarce | Clark, "The long march of history: farm wages, population, and economic growth, England 1209-1869," Economic History Review (2007) | Herlihy, "The Black Death and the Transformation of the West" (Harvard, 1997) | yes |
| The Ordinance of Labourers (1349) and Statute of Labourers (1351) tried to hold wages down | The National Archives (UK), "Statute of Labourers" | Britannica, "Statute of Labourers" | yes |
| Anger over wages and taxes fed the Peasants' Revolt of 1381 | Britannica, "Peasants' Revolt" | The National Archives (UK), "The Peasants' Revolt" | yes |
| The plague spread along trade routes and some villages were deserted | Britannica, "Black Death" | Historic England, "Deserted medieval villages" | yes |
| Historians debate how far the plague alone caused later changes | Herlihy (1997) | Britannica, "Black Death: effects" | yes |
Backed twice: 7. Cut: 0.

Checks run (Python, scratchpad r13, 2026-11-09): dates in order (1347, 1349, 1351, 1381); each segment draft is about 150 words; each Agree pair has two different experts; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 transcript and board; at 680x425 tabs.
2. Key words land in the right expert's column. (D1.1.6-8)
3. Three Agree pins on the big question link two experts each. (D1.2.6-8)
4. Four smaller questions are written and an Agree on one is pinned. (D1.3.6-8)
5. The wrap sentence prints with the board.
6. The printing press show loads.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no pulsing light; no network requests.

## Open questions
None.

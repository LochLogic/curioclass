# Tense Time Line

## One idea
A toy train runs along a story track drawn as a time line (long ago, earlier, now, later), and each sentence is a station the student must build so the train arrives at the right time: they pick verb forms (had walked, has walked, will have walked), fix sentences where the tense slips by accident, join ideas with the right connecting word and fit either/or and neither/nor pairs, and the train runs to the station the verb points to, so they learn that verb tense is how a sentence says when.

## Not like
- grammar-garage (4, spec): grade 4 progressive tenses and modals. Here grade 5 perfect tenses and tense shifts.
- comma-chameleon (4, spec): punctuation. Here verbs and connecting words.
- sentence-remixer (concept): sentence variety. Here tense and conjunctions.
- sentence-tree-builder (concept): sentence parts. Here time.
- pause-and-break (concept): pauses. Here time and joining words.

## Who and how
- Grade 5, ELA, module "Verb Tense and Conjunctions" (Language). Standards: L.5.1 (a, b, c, d, e).
- Driver: one student, or the class with the track on the projector (tool.json `driver: "student"`). Every sentence is read on tap.
- Four lines (each a short track): Perfect Line, Sequence Line, Fix-It Line, Joining Line. tool.json `modes: []`, `minutes: "20-30"`, `grades_label: "Grade 5"`.
- Nothing is saved; `Print` prints a ticket of each line's sentences.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| L.5.1b | Perfect Line: pick the past, present or future perfect form so the train stops at the right station | the train at the station the verb points to | 2 |
| L.5.1c | Sequence Line: order two events with tense ("By the time we got there, the show had started") | two trains, one stopping earlier | 3 |
| L.5.1d | Fix-It Line: find the verb that shifts tense by accident and fix it | the train jumping track at the slip | 4 |
| L.5.1a | Joining Line: pick the conjunction, preposition or interjection that fits (because, although, during, wow) | the word on a coupling between two cars | 5 |
| L.5.1e | Joining Line: correlative pairs (either/or, neither/nor, not only/but also, both/and) | paired couplings | 5 |

## Screens and modes
Header (kit): title "Tense Time Line"; `Lines`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A model railroad table with a track running left to right through four stations labeled Long Ago, Earlier, Now and Later, and Conductor Pip, a mouse in a conductor's cap. First hint: "Tap a line to lay its track." The first tap reads the line's name; the welcome is queued after it (`welcomeAfter: true`).

**Perfect Line.** A sentence with a time clue and a verb gap ("By next June, Ana ___ (finish) fifth grade."). Three verb cars: has finished, had finished, will have finished. The student hooks one to the train; the train runs to the station the verb names, and only the one that fits the time clue stops at the lit station. Each verb car's station is set in data (had + past participle = before another past time; has + past participle = from the past up to now; will have = before a future time).

**Sequence Line.** Two events, two trains. The student picks forms so the earlier event's train stops at the earlier station ("When Mom got home, we ___ (clean) the kitchen"). The track shows both stops.

**Fix-It Line.** A short paragraph (5 to 6 sentences) in the past with one or two accidental shifts ("He opens the door"). The train runs and derails at the slip; the student taps the verb and picks the fix. One paragraph has a correct shift (dialogue in the present inside a past story) to show not every shift is wrong; tapping it gets "This one is inside quotation marks. People talk in the present."

**Joining Line.** Cars to couple: two clauses and a coupling slot. Couplings: because, although, unless, so, while; prepositions during, despite, until; interjections Wow!, Oops!, Phew! for a sentence's start. Correlative pairs come as linked couplings that must both be placed (neither ... nor). The coupling's fit is set in data; a misfit makes the cars bump with a reason ("Although shows a surprise. Is there a surprise here?").

At 1366x768 the whole track fits; at 680x425 the track scrolls in its own box.

## Content
Written for Curio Class:
- Perfect Line: 12 sentences (4 of each perfect tense) with time clues.
- Sequence Line: 8 sentence pairs.
- Fix-It Line: 4 short paragraphs (a lost dog found, a science fair, a snow day, a garden), each with 1 or 2 slips and one has a correct shift in dialogue.
- Joining Line: 12 joins (6 conjunctions, 3 prepositions, 3 interjections) and 6 correlative pairs.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- With Motion off the train jumps to its station.
- Wrong cars stay on the track until changed; the train reruns on each change.
- Class mode: the track is large; the sentence sits above it in big type.

## Look
- Accent `--brand` #0b6e6e track teal (header, rails, station signs); gold #f4c542 (the lit station, couplings); paper #f0f8f8; ink #082626; muted #495e5e. Scene: a model railroad table with little trees.
- Contrast (WCAG 2.1, computed): white on brand 6.05:1; brand on paper 5.62:1; ink on paper 14.81:1; muted on paper 6.40:1; ink on gold 9.81:1.
- Never color alone: stations have words; derails show a mark and a word.
- Different from this batch (detective navy, stage pink, film sepia, courtroom mahogany).

## Art
Local FLUX (`scripts/localart.py`), no people.
- railroad table (1); Conductor Pip (4 poses: wave, point, whistle, think), "A friendly mouse train conductor in a blue cap holding a pocket watch <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- station signs are drawn in code.
About 5 images. Drawn in code: track, train, cars, couplings, stations.

## Voice
Bank voice `clear-teacher` as Conductor Pip (unique in this batch). `Curio.voice` with `scope: () => state.line + ':' + state.item`, `welcomeAfter: true`.
- event `line`: "{The Perfect Line}. All aboard!"
- how `welcome`: "Every verb tells the train when to stop. Pick the one that matches the time."
- event, whole, `sentence`: the built sentence.
- event `arrive`: "Arriving at {Earlier}."
- event `wrongStop`: "This verb stops at {Now}. The clue says {by last summer}."
- event `derail`: "Off the track! This verb jumps to {the present}."
- event `bump`: "{Although} shows a surprise. Is there a surprise here?"
- how `pairHow`: "This coupling comes in pairs. Place both."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: verb cars with station data, sequence pair, slip detection from the key, couplings with fit data.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Perfect | Try all three cars | Each car is read in the sentence with where it stops, so trying teaches; the line ends with a recap round of 4 new sentences scored on the first try. |
| Sequence | Same form for both | The two trains stop at the same station and the line asks "Which happened first?" |
| Fix-It | Change every verb | Changing a correct verb makes the train derail there; the dialogue shift is protected. |
| Joining | Use "and" | "And" isn't in the tray; each coupling has fit data. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a line: `line`, `welcome` (queued, first time).
2. Each car: `sentence` (whole), then `arrive` or `wrongStop`.
3. Fix-It: `derail` at each slip.
4. Joining: `bump` as it fires; first pair: `pairHow`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| L.5.1 (a to e) wording | thecorestandards.org, Language Grade 5 | CCSS ELA 2010 PDF | yes |
| Past perfect (had + past participle) shows an action finished before another past time; present perfect (has or have + past participle) connects past to now; future perfect (will have + past participle) is finished before a future time | Purdue OWL, verb tenses | Cambridge Dictionary, English Grammar Today (perfect aspect) | yes |
| Correlative conjunctions are paired (either/or, neither/nor, not only/but also, both/and) | Merriam-Webster, correlative conjunction | Purdue OWL, conjunctions | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad b15, 2026-11-09): every Perfect Line sentence has exactly one car that matches its time clue in the sample key; the Fix-It paragraphs' slips are verbs in the present inside past narration, outside quotation marks; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the track fits; at 680x425 it scrolls in its own box.
2. Perfect Line runs trains to the station each verb names. (L.5.1b)
3. Sequence Line shows two stops in order. (L.5.1c)
4. Fix-It derails at slips and protects dialogue shifts. (L.5.1d)
5. Joining Line checks couplings and correlative pairs. (L.5.1a, L.5.1e)
6. The recap round scores first tries.
7. Print shows each line's sentences as a ticket.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: the train jumps; no network requests.

## Open questions
- None for Cory.

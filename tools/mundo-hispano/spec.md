# Mundo Hispano

## One idea
The student travels a map of the 20 countries where Spanish is an official language, plus Puerto Rico and Spanish-speaking communities in the mainland United States, and at each stop reads and hears a short Spanish text about one living tradition (what people do, what they use, and why it matters to the people who keep it), filling a practice, product and perspective triangle, while a language layer shows the other languages spoken alongside Spanish there (Guaraní in Paraguay, Catalan in Spain, Garifuna in Honduras), so they learn how traditions connect to the beliefs behind them and how varied the Spanish-speaking world is.

## Not like
- el-restaurante (K-12, spec): ordering food in a conversation. Here reading and listening about traditions.
- deaf-culture-explorer (on hold): Deaf culture. Here the cultures of the Spanish-speaking world.
- calendario-vivo (K-12, spec): dates and weather in one city. Here a map of many places.
- detective-del-pasado (6-12, spec, this batch): past tense for a mystery. Here present-tense descriptions of real traditions.
- perspective-frames (6-8, spec, this batch): why people see a town decision differently. Here why a tradition matters to the people who keep it.

## Who and how
- Grades 6 to 12, World Languages (Spanish), module "Cultures of the Spanish-Speaking World". Standards: World-Readiness Standards, Cultures (Relating Cultural Practices to Perspectives; Relating Cultural Products to Perspectives); ACTFL Intermediate Mid.
- Driver: one student; class mode is "Presenta tu lugar", where each student presents one place from the projector with its triangle (tool.json `driver: "student"`). Every text is read aloud in Spanish; the hint voice speaks English.
- Help levels: Lots (English glossary on tap, picture questions), Some (Spanish glossary on tap), Little (no glossary, written answers). tool.json `modes: ["Mapa", "Pasaporte", "Comparar", "Presenta tu lugar"]`, `minutes: "10-15 per place"`, `grades_label: "Grades 6-12"`.
- The passport (places visited and triangles) is saved on this device only (localStorage), and the screen says so: "Your passport stays on this device. Nothing is uploaded." `Borrar mi pasaporte` clears it. `Print` prints the passport and the comparison.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| WRS Cultures, practices to perspectives | Fill the "why" corner of the triangle from the text | the triangle with the practice and the why | 3 |
| WRS Cultures, products to perspectives | Name what the tradition uses and why it matters | the product corner with a photo | 3 |
| ACTFL Intermediate Mid (interpretive reading and listening) | Read and hear each text and answer questions in Spanish | the question cards | 2 |
| ACTFL Intermediate Mid (written strings of sentences) | Compare two places and one tradition of their own with frames | the comparison page | 4 |
| WRS Cultures (language layer) | Open the language layer at each stop | the list of languages spoken there | 5 |

## Screens and modes
Header (kit): title "Mundo Hispano"; `Mapa`, `Pasaporte`, `Comparar`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word. Spanish first.

**On load and first tap.** A world map with the Spanish-speaking places lit and a blank passport on the desk; "Elige un lugar." First hint: "Tap a lit place to visit it." The first tap opens that place; the welcome is queued after it (`welcomeAfter: true`).

**A place.** A card with a photo of the tradition, a short text in Spanish (90 to 140 words, present tense, Intermediate Mid), audio, and four questions in Spanish (two about facts, one about the product, one about the why). Then the triangle: the student fills Práctica (what people do), Producto (what they use or make) and Perspectiva (why it matters, from the text, in the words of the people who keep it). The passport gets a stamp.

**Language layer.** A toggle on each card lists the languages spoken there alongside Spanish, with a short greeting in each where one is recorded, for example "Mba'éichapa" in Guaraní.

**Comparar.** The student picks two places and one tradition of their own and fills frames in Spanish: "En ___, la gente ___. En mi familia, nosotros ___. Las dos tradiciones ___ porque ___."

**Presenta tu lugar.** On the projector, one place full size for a student's short presentation.

At 1366x768 the map and card fit side by side; at 680x425 the card covers the map with a Back control.

## Content
One living tradition per place, each on UNESCO's Representative List of the Intangible Cultural Heritage of Humanity where one fits:

| Place | Tradition | Language layer |
|---|---|---|
| México | Pirekua, the traditional song of the P'urhépecha | P'urhépecha, Nahuatl, Maya and many more |
| Guatemala | Holy Week processions and carpets | K'iche', Kaqchikel and other Mayan languages, Garifuna, Xinka |
| Honduras | Language, dance and music of the Garifuna | Garifuna, Miskito |
| El Salvador | The Confraternity of flowers and palms, Panchimalco | Nawat |
| Nicaragua | El Güegüense, street theater | Miskito, Mayangna, Creole English |
| Costa Rica | Oxherding and painted oxcarts | Bribri, Cabécar, Limón Creole |
| Panamá | Weaving the sombrero pintao | Ngäbere, Guna |
| Cuba | Rumba | Spanish |
| República Dominicana | Music and dance of the merengue | Spanish, Haitian Creole |
| Puerto Rico | Plena, the "sung newspaper" | Spanish and English |
| Colombia | Carnival of Barranquilla | Wayuunaiki, Palenquero and others |
| Venezuela | Dancing Devils of Corpus Christi | Wayuu, Warao and others |
| Ecuador | Weaving the toquilla straw hat | Kichwa, Shuar |
| Perú | The scissors dance | Quechua, Aymara |
| Bolivia | Carnival of Oruro | Quechua, Aymara, Guaraní and 30 more |
| Chile | Baile chino | Mapudungun, Rapa Nui, Aymara |
| Argentina | Tango | Spanish, Guaraní, Quechua |
| Uruguay | Candombe | Spanish, Portuguese near Brazil |
| Paraguay | Tereré with pohã ñana herbs | Guaraní (official alongside Spanish) |
| España | Human towers (castells) | Catalan, Galician, Basque |
| Guinea Ecuatorial | The balélé dance on Bioko | Fang, Bubi, French, Portuguese |
| Estados Unidos | Mariachi in the Southwest | English and Spanish |

- Texts, questions and triangles written for Curio Class from the UNESCO element descriptions (which communities help write) and a second source each, with the "why" in the community's terms. No place is reduced to food, costumes or a stereotype; each card names that the tradition is living and changing.
- Sensitive cards (Indigenous traditions, religious processions) are written with care and go to the fresh-agent review.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Places can be visited in any order; triangles can be edited until the passport is cleared.
- With Motion off the map doesn't pan or zoom; cards open in place and stamps appear without the thump.

## Look
- Accent `--brand` #9a3412 earth red (header, passport cover, lit places); gold #f4c542 (stamps, the place you're on); paper #fcf3ee; ink #2b0f05; muted #6b5348. Scene: a travel desk with a map and a passport.
- Contrast (WCAG 2.1, computed): white on brand 7.31:1; brand on paper 6.68:1; ink on paper 16.36:1; muted on paper 6.49:1; ink on gold 11.01:1.
- Never color alone: lit places also carry a dot and their name; visited ones a stamp mark.
- Different from this batch (detective teal, book-group purple, town slate, highlighter olive).

## Art
- Real photos: one per place, from Wikimedia Commons or the Library of Congress, each with a free license or public domain status checked and a credit line on the card; where no suitable free photo exists, a local FLUX scene of the objects (no people, no faces) stands in and is labeled "illustration".
- Local FLUX (`scripts/localart.py`): the travel desk and map (1); passport and stamps drawn in code.
About 24 images. Drawn in code: map, triangle, stamps.

## Voice
Bank voice `hs-narrator` as the English hint voice (unique in this batch); the Spanish texts are read by `smooth-narrator` and `wise-mentor`, alternating by place, each told the regional accent of that place (each unique in this batch). `Curio.voice` with `scope: () => state.place + ':' + state.part`, `welcomeAfter: true`.
- how `welcome`: "Pick a place. Read about one tradition there, then fill in what people do, what they use, and why it matters."
- event, whole, `text`: the place's text in Spanish.
- event `question`: the question in Spanish.
- event `why`: "Find the why in the text. What do the people say it means?"
- event `stamp`: "¡Sello!"
- event `privacy`: "Your passport stays on this device. Nothing is uploaded."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
spanish (`kit/spanish.js`, `__tool.es`), described in full in tools/calendario-vivo/spec.md. This tool uses: word records with audio and `es.say` for glossary words, and `es.check` for written answers at Little help. The map, cards, triangle, language layer and passport (localStorage wrapped in try and catch) are tool-only code.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Triangle | Put the product in the why corner | The why corner is keyed to perspective words in the text (porque, significa, para recordar, para honrar); a product word gets the "why" hint. |
| Questions | Guess | Each question asks for the line in the text that answers it. |
| Compare | Fill frames with one place twice | The two places must differ. |
Exploring the map is free, by design.

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a place: `text` (whole), `welcome` (queued, first time).
2. Questions: `question` per card. Triangle: `why` as it fires; `stamp` when done.
3. First save: `privacy`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| Spanish is an official language in these 20 countries and in Puerto Rico | Wikipedia, Hispanophone (checked 2026-11-09) | Instituto Cervantes, El español en el mundo (yearbook) | yes |
| Each named tradition (except Puerto Rico's plena, the US mariachi card and Equatorial Guinea's balélé) is on UNESCO's Representative List | Wikipedia, Lists of Intangible Cultural Heritage elements (checked 2026-11-09) | ich.unesco.org element pages, linked from that list | yes |
| Mariachi is on the UNESCO list for Mexico and is played across Spanish-speaking communities of the US Southwest | ich.unesco.org, "Mariachi, string music, song and trumpet" | Smithsonian Folkways, mariachi collection notes | yes |
| Plena is a Puerto Rican music and dance with African roots, from Barrio San Antón in Ponce | Wikipedia, Plena (checked 2026-11-09) | Smithsonian Folkways, plena collection notes | yes |
| Equatorial Guinea: the balélé dance is performed on Bioko around Christmas; Spanish, French and Portuguese are official | Wikipedia, Culture of Equatorial Guinea (checked 2026-11-09) | Britannica, Equatorial Guinea, cultural life | yes |
| Paraguay's official languages are Spanish and Guaraní; UNESCO inscribed tereré with pohã ñana in 2020 | Wikipedia, Languages of Paraguay and Tereré (checked 2026-11-09) | Constitution of Paraguay (1992), article 140; ich.unesco.org tereré page | yes |
| WRS Cultures standards and ACTFL Intermediate Mid | ACTFL, World-Readiness Standards for Learning Languages (2015) | ACTFL Proficiency Guidelines 2012; NCSSFL-ACTFL Can-Do Statements (2017) | yes |
Backed twice: 7. Cut: 0.

Sensitivity note: many cards describe Indigenous and religious traditions; each is written from the community's own description and goes to the fresh-agent review, which also checks every card for stereotypes.

Checks run (Python, scratchpad b27, 2026-11-09): the saved UNESCO list page names each tradition marked as on the list; the Hispanophone page names Equatorial Guinea and Puerto Rico; the Paraguay page lists Guaraní as official; the place table has 22 rows with no place twice; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 map and card fit; at 680x425 the card covers the map with Back.
2. Each place's text plays in Spanish with four questions. (ACTFL Intermediate Mid)
3. Triangles fill, and the why corner checks perspective words. (WRS Cultures)
4. Comparar builds a comparison with the student's own tradition. (ACTFL Intermediate Mid)
5. The language layer opens on every card. (WRS Cultures)
6. Every photo has a checked license and a credit line, or is labeled "illustration".
7. The passport persists on this device; the privacy line shows; Borrar clears it.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: no panning or zooming; no network requests.
10. Storage blocked: the tool still works and says the passport won't be kept.

## Open questions
- Spanish audio review: same as calendario-vivo (default used: a fresh agent checks the Spanish text, and Sara or Cory listens to a sample of 20 lines).
- Should each place's text be recorded later by a speaker from that place instead of a bank voice with a regional accent? (default used: bank voices with regional accents)

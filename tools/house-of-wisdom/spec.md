# House of Wisdom

## One idea
The child follows one book backward and forward through time: a Latin copy of Ptolemy's astronomy on a desk in Toledo in 1175 has a thread leading back across a map to Greek scrolls in Alexandria (about 150 CE), to a paper mill in Baghdad using skills that came from China, to translators turning Greek into Arabic under the Abbasid caliphs in the 800s, to an observatory where astronomers checked and corrected Ptolemy, to a hospital, to al-Khwarizmi's lesson whose title gave us the word "algebra," and back to Toledo, where Gerard of Cremona put the Arabic into Latin; in each room the child inspects objects and picks up a "carried forward" card (an idea, a tool, a word), then lays the cards on a route map and writes how paper, roads and trade let knowledge travel and how Baghdad joined older Greek, Persian and Indian learning to later Europe, so a seventh grader learns to connect one place's scholars to the wider story before and after them, and how communication technology spreads ideas.

## Not like
- printing-press (7, concept): a later leap in copying. Here copying by hand and translating.
- silk-road-traders (6, spec): goods and beliefs moving by trade. Here one book moving by translation.
- panel-of-experts (7, spec): four fields question one event. Here one book's journey.
- historians-disagree (7, spec): judging two historians. Here following a text through time.

## Who and how
- Grade 7, Social Studies (History and Geography), module "Islamic Civilizations". Standards: D2.His.1.6-8 (analyze connections among events and developments in broader historical contexts), D2.Geo.7.6-8 (explain how changes in transportation and communication technology influence the spatial connections among human settlements and affect the diffusion of ideas and cultural practices).
- Format: explorer. Driver: one child alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Seven rooms, the route map, the closing paragraph. Extra: The medical book (the same journey for Galen's medicine, translated by Hunayn ibn Ishaq in Baghdad, then Ibn Sina's Canon of Medicine into Latin at Toledo). tool.json `modes: ["The astronomy book", "The medical book"]`, `minutes: "25-35"`, `grades_label: "Grade 7"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.His.1.6-8 | Explore seven rooms and collect a "carried forward" card from each, naming where it came from and where it went | the cards with "came from" and "went to" lines; the timeline under the map | 2 |
| D2.Geo.7.6-8 | Lay the cards on the route map and pick what carried each one (paper, roads, trade, translators) | the route map with lines and carrier icons | 3 |
| D2.His.1.6-8 (paragraph) | Write how Baghdad joined older learning to later Europe | the paragraph card beside the map | 4 |

## Screens and modes
Header (kit): title "House of Wisdom"; `The astronomy book`, `The medical book`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A desk in Toledo by candlelight; a thick Latin book open to a star diagram. A gold thread runs off the page onto a small map of the Mediterranean and the Middle East. The welcome is queued (`welcomeAfter: true`): "This Latin book holds a Greek astronomer's ideas. But it came here through Arabic. Follow the thread to see how. Tap the thread." First hint: "Tap the gold thread."

**The rooms (focus: the room scene and its objects).** At 1366x768 the room fills the screen with the card tray at the bottom and the mini map in the corner; at 680x425 the tray is a sheet.
1. Alexandria, about 150 CE: Ptolemy writes his great book of astronomy in Greek, a model of the sky with Earth at the center. Card: Ptolemy's star tables.
2. A paper mill in Baghdad, late 700s: papermaking, first developed in China, spread west; Baghdad had paper mills by the late 700s, and paper was far cheaper than parchment. Card: paper. A note says the old story that papermakers came as prisoners after a battle in 751 is told often but debated.
3. The translators' workroom, 800s: under the caliph al-Ma'mun and others, scholars translated Greek, Persian and Indian works into Arabic; Ptolemy's book became known by an Arabic name, "al-Majisti," which later became "Almagest." Translators like Hunayn ibn Ishaq, a Christian physician, worked for Muslim patrons. Card: the word Almagest.
4. An observatory, 820s and 830s: astronomers in Baghdad and Damascus measured the sky again and corrected some of Ptolemy's numbers. Card: checking old books against new measurements.
5. A hospital (bimaristan) in Baghdad: physicians trained, kept records and wrote books. Card: the hospital as a place to learn.
6. Al-Khwarizmi's lesson, about 820: his book on solving equations used the word "al-jabr," which became "algebra," and his name became "algorithm"; another of his books explained the Indian numerals we now call Hindu-Arabic numbers. Card: algebra, algorithm, and the digits 0 to 9.
7. Toledo, 1175: after the city came under Christian rule, scholars like Gerard of Cremona translated Arabic books into Latin, often working with Arabic-speaking Jewish and Christian helpers. Card: the Latin Almagest.
- In each room the child taps two or three objects (each with a short card and a source line), then picks up the "carried forward" card.

**The honest note.** On the translators' room: "Historians debate what the House of Wisdom itself was. Some think it was a great academy; others think it was mainly the caliph's library. Either way, the translating was real, and it happened across Baghdad."

**The route map (the aha).** The child drags each card onto the map at its place and draws its line to the next stop, then picks what carried it: paper, roads and trade, translators, a ruler's support. The timeline under the map runs from 150 to 1175. Then the paragraph card: "Baghdad's scholars joined ___ and ___ learning to ___, and ___ helped the ideas travel." (tiles plus a free line). Narrator: "The book survived because it kept moving, from language to language and city to city."

**The end.** The route map, the seven cards, the timeline and the paragraph. `Print` prints them.

**The medical book (extra).** Galen's Greek medicine translated by Hunayn ibn Ishaq; Ibn Sina's Canon of Medicine, written in Persia about 1025; Gerard of Cremona's Latin translation; the Canon taught in European universities for centuries.

## Content
- Seven rooms with two or three objects each, seven carried-forward cards, the honest note, the route map with carriers, paragraph tiles, the medical-book set.
- Every person, date and fact is real; dates are given as "about" where uncertain.
- Islam and the Abbasid caliphate are shown accurately and respectfully; the scholars' many faiths are named.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Rooms open in order along the thread; the child can return to any opened room.
- Cards must be placed at the right city; a wrong drop plays "Where was this made?"
- Keyboard: Tab to the thread, objects, cards and map cities; Enter to open, pick up and drop.
- With Motion off the thread doesn't draw itself and candlelight doesn't flicker.

## Look
- Accent `--brand` #1f4e86 lapis blue (header, the tray, the route lines); gold #f4c542 (the thread, the card in hand); paper #f0f4f9; ink #071a30; muted #4f5866.
- Contrast (WCAG 2.1, computed): white on brand 8.43:1; brand on paper 7.63:1; ink on paper 15.85:1; muted on paper 6.51:1; ink on gold 10.76:1.
- Never color alone: route lines carry carrier icons and labels; each city has a name tag.
- Different from this batch (desert sienna, steppe olive, heraldic red, studio teal).

## Art
- Public domain (Met Open Access, ids checked at build): a brass astrolabe (Islamic, medieval); a page from an Arabic translation of a Greek text (Walters Art Museum or Library of Congress World Digital Library, checked at build); a Latin Almagest page (public domain scan). Each with credit.
- Local FLUX (`scripts/localart.py`): seven room scenes (7, 16:9): Toledo desk, Alexandria scrolls, Baghdad paper mill, translators' workroom, observatory, hospital, al-Khwarizmi's lesson.
- People art goes to Gemini with `people: true`: Ptolemy, a papermaker, Hunayn ibn Ishaq, an astronomer, a physician, al-Khwarizmi, Gerard of Cremona (7; cutout yes), dress checked by a fresh agent against period sources. No images of the Prophet.
About 17 images.

## Voice
Two bank voices, each unique in this batch: `curious-librarian` as the thread's guide; `smooth-narrator` as the room cards' reader. `Curio.voice` with `scope: () => state.mode + ':' + state.room + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each room's opening line.
- how `inspect`: "Tap an object in the room."
- event, whole, each object card.
- how `carry`: "Pick up the carried forward card."
- how `map`: "Drag each card to its city, then pick what carried it."
- how `paragraph`: "Finish the paragraph about how ideas traveled."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the thread with seven rooms, object cards, the card tray, the route map with carriers, the timeline, the paragraph card.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Rooms | Skip objects | The carried-forward card appears only after two objects are opened. |
| Route map | Drop cards anywhere | Each card checks its city; the carrier must fit (paper can't carry a ruler's support). |
| Paragraph | Leave blanks | Print waits for them. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Room opening (whole), waits.
2. `inspect`; object cards (whole); `carry`.
3. `map`; `paragraph`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.1.6-8 and D2.Geo.7.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Ptolemy wrote his astronomy in Alexandria about 150 CE; its Arabic name became "Almagest" | Encyclopaedia Britannica, "Almagest" | Britannica, "Ptolemy" | yes |
| Greek, Persian and Indian works translated into Arabic in Abbasid Baghdad, including under al-Ma'mun | Gutas, "Greek Thought, Arabic Culture" (Routledge, 1998) | Britannica, "House of Wisdom" | yes |
| Historians debate whether the House of Wisdom was an academy or mainly a library | Gutas (1998) | Britannica, "House of Wisdom" | yes, the debate is named |
| Paper spread from China; Baghdad had paper mills by the late 700s; the 751 prisoner story is debated | Bloom, "Paper Before Print" (Yale, 2001) | Britannica, "Paper: history" | yes |
| Hunayn ibn Ishaq, a Christian physician, translated Greek medicine | Britannica, "Hunayn ibn Ishaq" | Gutas (1998) | yes |
| Astronomers in Baghdad and Damascus under al-Ma'mun measured the sky and corrected Ptolemy | Britannica, "Astronomy: Islamic world" | Saliba, "Islamic Science and the Making of the European Renaissance" (MIT, 2007) | yes |
| Al-Khwarizmi's al-jabr gave "algebra," his name "algorithm"; he explained Indian numerals | Britannica, "al-Khwarizmi" | MacTutor History of Mathematics, "al-Khwarizmi" | yes |
| Gerard of Cremona translated the Almagest from Arabic to Latin in Toledo, 1175 | Britannica, "Gerard of Cremona" | Britannica, "Almagest" | yes |
| Ibn Sina's Canon of Medicine, translated by Gerard, taught in Europe for centuries | Britannica, "Avicenna" | US National Library of Medicine, "Islamic Medical Manuscripts" | yes |
Backed twice: 10. Cut: 0.

Sensitivity note: Islam and the Abbasid caliphate are shown accurately and respectfully; the scholars' many faiths (Muslim, Christian, Jewish, Sabian) are named; no scripture pages and no images of the Prophet are used. A fresh-agent read is needed before build.

Checks run (Python, scratchpad r13, 2026-11-09): rooms in date order (about 150, late 700s, 800s, 820s to 830s, about 820 placed by theme, 1175) with the timeline sorting by date, not room order; 1175 minus 150 is 1,025 years; seven cards for seven rooms; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 room with tray and mini map; at 680x425 tray sheet.
2. Seven rooms each give a carried-forward card with came-from and went-to lines. (D2.His.1.6-8)
3. Cards place on the route map with carriers. (D2.Geo.7.6-8)
4. The paragraph prints with the map. (D2.His.1.6-8)
5. The honest note about the House of Wisdom shows.
6. The medical book loads its rooms.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no drawing thread or flicker; no network requests.

## Open questions
- Sensitivity flag: Islam and the Abbasid caliphate (default used: accurate and respectful, scholars' many faiths named, no scripture pages and no images of the Prophet, fresh-agent read before build).

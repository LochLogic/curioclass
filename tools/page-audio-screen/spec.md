# Page Audio Screen

## One idea
A book club needs one recommendation for each request card ("for a listener on a long car ride", "to build suspense", "for someone who has never seen a lighthouse"), so the student compares three versions of a story scene (four men in a small boat sighting a lighthouse, from Stephen Crane's "The Open Boat") and of an explainer (how a lighthouse lens works): the page, two audio readings with different delivery, and a film storyboard or diagram animation, pinning what each version adds, cuts, changes and what only that medium can do (a pause, a close-up, a sound), and writes a recommendation that cites their pins, so they learn that each medium makes its audience notice different things.

## Not like
- page-to-screen (10, concept): shooting a story shot by shot. Here comparing versions, grades 6-8.
- docent-tour-talk (6-8, spec): presenting a talk. Here judging versions made by others.
- podcast-listening-club (6-8, concept): a speaker's claims. Here delivery and medium.
- linked-feature (6-8, spec): publishing online. Here comparing media.
- script-read-through (spec): performing a script. Here listening to two readings.

## Who and how
- Grades 6-8, ELA, module "Text, Audio and Film Versions" (Reading Literature and Informational Text). Standards: RL.6.7, RI.6.7, RL.7.7, RI.7.7, RL.8.7, RI.8.7.
- Driver: one student; class mode tallies recommendations (tool.json `driver: "student"`). Every sentence is read on tap.
- Two pieces: the story scene and the lighthouse explainer; six request cards. Grade picker adds grade 7 technique pins and grade 8 faithful-or-departs judgments. tool.json `modes: ["Grade 6", "Grade 7", "Grade 8", "Class tally"]`, `minutes: "30-40"`, `grades_label: "Grades 6-8"`.
- Nothing is saved; `Print` prints the pins and recommendations.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.6.7 | Read, listen to and view the scene; pin what each lets the audience see or hear | pins on the page, the audio timeline and the storyboard | 2 |
| RI.6.7 | Build one picture of how the lens works from the article, the narrated audio and the diagram; answer three questions using all three | the answers with a medium tag each | 3 |
| RL.7.7 | Pin techniques unique to a medium (a pause, music, lighting, a close-up, a cut) and say their effect | technique pins with an effect line | 2 |
| RI.7.7 | Compare the two readings of the same words: which line lands harder and why | the two waveforms and the student's line | 4 |
| RL.8.7 | Judge where the storyboard stays faithful or departs, and whether the change was worth it | faithful and departs marks with a because | 5 |
| RI.8.7 | Weigh each medium's advantages and limits for explaining the lens | a three-column pros and limits card | 5 |
| all | Write the recommendation for a request card, citing two pins | the recommendation card | 6 |

## Screens and modes
Header (kit): title "Page Audio Screen"; `Story`, `Explainer`, `Recommend`; tabs inside each: `Page`, `Audio`, `Screen`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A book club's corner with a corkboard of request cards, an old radio and a small screen, and Ines, the club's organizer, holding a stack of cards. First hint: "Tap a request card to start." The first tap reads the card; the welcome is queued after it (`welcomeAfter: true`).

**Story: Page.** Section III of "The Open Boat" (1897), adapted for grades 6-8 to about 600 words with cuts marked: the cook says he has seen the lighthouse at Mosquito Inlet; the correspondent can't see it at first; it grows slowly larger; the men row in turns and talk about the station. Tap to hear any sentence; pins can go on any span.

**Story: Audio.** Two readings of the same adapted text: Reading 1 slow and hushed with long pauses and soft sea sound; Reading 2 brisk and plain with no sound under it. Each shows a waveform timeline; pins go on a moment.

**Story: Screen.** A storyboard of 12 frames (drawn and generated), each with a shot type (wide, close-up, over the shoulder), a lighting note and a sound note. The storyboard shows the cook's face as he spots the light (the text only gives his words), cuts a paragraph of the correspondent's thoughts, and adds a frame of the lighthouse beam at dusk (in the text it's daytime).

**Pins.** Added, Cut, Changed, Only here (grade 7 adds the technique list: pause, music, sound effect, close-up, wide shot, lighting, cut). Each pin needs a short effect line ("The pause makes me wait for the light too.").

**Explainer.** How a lighthouse lens works, in three versions: an article (about 400 words, written for Curio Class from sourced facts), a narrated audio version, and a diagram animation drawn in code (a lamp, rings of glass prisms bending light into one beam; Motion off shows steps). Three questions ("Why does the lens have rings?"), each answered and tagged with the medium that helped most.

**Recommend.** The student picks a request card and writes a recommendation: which version, and two pins that support it. At grade 8 the storyboard's departures get faithful or departs marks and a "worth it?" because.

**Class tally.** Counts per request card for each version.

At 1366x768 the version and pins fit side by side; at 680x425 pins are a drawer.

## Content
- Stephen Crane, "The Open Boat" (1897), section III, from "The Open Boat and Other Stories", Project Gutenberg eBook #45524, adapted with cuts marked. The story follows real events: Crane's ship, the Commodore, sank off Florida in January 1897.
- Explainer facts: Augustin Fresnel's lens (1822) uses rings of glass prisms to bend and focus a lamp's light into a beam that can be seen many miles out; lenses come in orders by size, first order the largest; the light at Mosquito Inlet (today Ponce de Leon Inlet Light, Florida) was first lit in 1887.
- Storyboard data: 12 frames with shot, lighting and sound notes; a key of what each frame adds, cuts or changes.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Audio readings can be scrubbed; pins snap to the nearest second.
- With Motion off the diagram steps through stills and the storyboard has no pans.
- The two readings are produced with two bank voices and sea sound from the kit's sound set.

## Look
- Accent `--brand` #7d5400 lamp amber (header, the lighthouse beam frame, pins); gold #f4c542 (the beam, Only here pins); paper #fbf7ee; ink #271a02; muted #625846. Scene: a cozy club corner with a sea painting.
- Contrast (WCAG 2.1, computed): white on brand 6.69:1; brand on paper 6.25:1; ink on paper 15.90:1; muted on paper 6.54:1; ink on gold 10.46:1.
- Never color alone: pins carry their type in words; waveforms have time labels.
- Different from this batch (editor's red, blueprint blue, web green, lilac).

## Art
- People art goes to Gemini: Ines (a Filipina American woman in her twenties with a cardigan and a stack of cards), 4 poses; storyboard frames with the four men in the boat (the captain, the cook, the oiler, the correspondent; 1890s clothing; 8 frames); "illustrated film storyboard frame <description>, ink and wash, no text"; 16:9.
- Local FLUX (`scripts/localart.py`): club corner (1); storyboard frames without people (4: the lighthouse far off in daylight, the lighthouse closer, the beam at dusk, the sea from the boat); 16:9.
About 17 images. Drawn in code: waveforms, lens diagram and animation, pins.

## Voice
Bank voice `curious-librarian` as Ines (unique in this batch); Reading 1 is `soft-breath`, Reading 2 is `lively-host`, and the narrated explainer is `smooth-narrator` (each unique in this batch). `Curio.voice` with `scope: () => state.piece + ':' + state.version + ':' + state.pin`, `welcomeAfter: true`.
- how `welcome`: "Same scene, three versions. Which one fits this request? Pin what each version does."
- event, whole, `sentence`: the tapped sentence.
- how `pinHow`: "Pin a moment: added, cut, changed or only here. Then say what it does."
- event `twoReadings`: "Same words. Which reading made the light feel closer?"
- event `depart`: "The storyboard shows {the beam at dusk}. In the text it's {daytime}. Worth it?"
- how `recommendHow`: "Pick a version for this request, and give two pins as reasons."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: three-medium viewer, pins on text, audio and frames, lens diagram, recommendation card.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Pins | Pin without an effect line | Each pin needs an effect line. |
| Explainer questions | Tag every answer "page" | Answers are checked against key facts; the medium tag is the student's call, shown back in the print. |
| Recommendation | Pick a version with no reasons | It needs two pins. |
| Faithful or departs | Mark everything faithful | Three key departures are marked in data and named when missed. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a request card: the card, `welcome` (queued, first time).
2. Page: `sentence` (whole). First pin: `pinHow`.
3. Audio: after both readings, `twoReadings`.
4. Screen (grade 8): `depart` per key departure. Recommend: `recommendHow`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.6.7 to RL.8.7 and RI.6.7 to RI.8.7 wording | thecorestandards.org, Grades 6-8 | CCSS ELA 2010 PDF | yes |
| "The Open Boat" (1897), section III: the lighthouse at Mosquito Inlet sighted and growing larger | Project Gutenberg eBook #45524 (checked 2026-11-09) | Library of Congress, catalog record for "The Open Boat and Other Tales of Adventure" (1898) | yes |
| The story follows Crane's own shipwreck when the Commodore sank off Florida in January 1897 | Stephen Crane Society, biography and chronology | Florida Memory (State Library and Archives of Florida), the Commodore and Stephen Crane | yes |
| Augustin Fresnel's lens (1822) uses rings of prisms to bend light into a strong beam; lenses come in orders, first order largest | National Park Service, lighthouse lenses | US Lighthouse Society, Fresnel lens | yes |
| Mosquito Inlet Light, now Ponce de Leon Inlet Light, was first lit in 1887 | US Coast Guard History Office, Ponce de Leon Inlet Light | Ponce de Leon Inlet Lighthouse and Museum, history | yes |
Backed twice: 5. Cut: 1 (how many miles out the 1887 light could be seen; numbers differ by source, so the article says "many miles").

Checks run (Python, scratchpad b17, 2026-11-09): the Gutenberg text has the cook's sighting of the lighthouse at Mosquito Inlet and the line about it growing slowly larger; the storyboard key has three departures; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the version and pins fit; at 680x425 pins are a drawer.
2. Pins with effect lines work on page, audio and storyboard. (RL.6.7, RL.7.7)
3. The explainer's three questions take answers and medium tags. (RI.6.7)
4. The two readings play and the comparison line is taken. (RI.7.7)
5. Grade 8 faithful or departs marks and the pros and limits card work. (RL.8.7, RI.8.7)
6. Recommendations need two pins; the class tally counts.
7. Print shows pins and recommendations.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: the diagram steps through stills; no network requests.

## Open questions
- None for Cory.

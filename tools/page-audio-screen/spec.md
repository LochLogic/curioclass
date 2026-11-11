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
- Driver: one student; class mode tallies recommendations (tool.json `driver: "student"`). Role: lesson. Every sentence is read on tap.
- Three grade paths. Each has a literature half and an information half with that grade's texts and that grade's wording on the goal card, five or more items in each half, and the last two of each done on your own. No path needs another. One half a sitting.
  - Grade 6. RL.6.7: compare the experience of reading a story or poem with listening to or viewing it, contrasting what you "see" and "hear" when reading with what you perceive when you listen or watch. RI.6.7: integrate information presented in words, visually and in numbers into one understanding of a topic.
  - Grade 7. RL.7.7: compare a written story or poem with its audio, filmed or staged version, analyzing the effects of techniques unique to each medium (lighting, sound, color, camera focus and angles). RI.7.7: compare a text with an audio or multimedia version, analyzing each medium's portrayal of the subject (how the delivery of a speech affects the impact of the words).
  - Grade 8. RL.8.7: analyze how far a filmed or live production stays faithful to or departs from the text, evaluating the choices of the director or actors. RI.8.7: evaluate the advantages and disadvantages of different mediums (print or digital text, video, multimedia) for presenting a topic or idea.
- Change note (spec fix, 2026-11-11): the book club, Ines, the request cards, the pins and the lighthouse explainer stay. Before, the three grades shared one scene and most checks only asked that a line be filled in. Now each grade has its own texts and five keyed moments or questions in each half; Ines works one first as the model; a pin's effect line is checked for what it names; grade 6 adds a poem, a short clip and a table of numbers; grade 7's delivery comparison is on a speech, with keyed techniques; grade 8 judges a real filmed production and marks cost something; grade 8 weighs print, digital, video and multimedia on five topics. Added the three hooks.
- English learners: every spoken line is also on screen in short sentences, and every audio and film has its words on screen. The words medium, version, technique, faithful, departs, advantage and limit each show with an example from Ines's model the first time they are used. Every written line offers a frame the student may take or leave ("In the audio I heard __, which made __."). Instructions use no idioms.
- tool.json `modes: ["Grade 6", "Grade 7", "Grade 8", "Class tally"]`, `minutes: "30-40"` for each half, `grades_label: "Grades 6-8"`.
- Nothing is saved; `Print` prints the pins, answers and recommendations.

## Standards map
| Code | The standard's verb and its parts | Who does the verb | Student action that teaches it | Items that differ | What they see | Done when check |
|---|---|---|---|---|---|---|
| RL.6.7 | compare and contrast reading a story or poem with listening to or viewing it; contrast what is "seen" and "heard" when reading with what is perceived when listening or watching | the student | At five moments, write what you pictured from the page before the audio or clip opens, then pin what the other version gave you or took away and what that did | 5 moments (3 in the story scene, 2 in the poem) | the student's own "what I pictured" line beside the moment | 2 |
| RI.6.7 | integrate information presented in different media or formats (visually, quantitatively) as well as in words | the student | Answer five lens questions, each needing two of article, diagram, audio and table, and tag where each part of the answer came from | 5 questions | the answer with its source tags | 3 |
| RL.7.7 | compare a written work with its audio, filmed or staged version, analyzing the effects of techniques unique to each medium | the student | At five moments, name the technique the medium used (keyed) and write its effect on the scene | 5 moments (2 audio, 2 film clip, 1 staged reading) | technique pins with effect lines | 2 |
| RI.7.7 | compare a text with its audio or multimedia version, analyzing each medium's portrayal of the subject | the student | For five lines of a speech, say how each delivery handles the line (keyed: pace, pause, stress, volume), which lands harder and why | 5 lines, 2 deliveries and a words-with-pictures version | the line, two waveforms and the student's line | 4 |
| RL.8.7 | analyze how far a filmed production stays faithful to or departs from the text, evaluating the director's or actors' choices | the student | For five moments of a film, mark faithful or departs, tap the text lines that prove it, name whose choice it was and say whether it was worth it | 5 moments (3 depart, 2 faithful) | the film frame beside the text | 5 |
| RI.8.7 | evaluate the advantages and disadvantages of using different mediums to present a topic or idea | the student | For five topics, try the topic in each medium, choose the best, and give one advantage and one limit | 5 topics, 4 mediums (print, digital text, video, multimedia) | a pros and limits card for each topic | 5 |
| all | use the comparison | the student | Write the recommendation for a request card, citing two pins or answers | 1 a path | the recommendation card | 6 |

## Screens and modes
Header (kit): title "Page Audio Screen"; `Story`, `Information`, `Recommend`; tabs inside each for its versions; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word. The goal card gives the grade's two standards in their own words.

**On load and first tap.** A book club's corner with a corkboard of request cards, an old radio and a small screen, and Ines, the club's organizer, holding a stack of cards. First hint: "Tap a request card to start." The first tap reads the card; the welcome is queued after it (`welcomeAfter: true`).

**Ines goes first (the model).** On a four-line nursery rhyme with a spoken version, Ines does one whole item aloud for the grade: says what she pictured, plays the version, pins what changed, and says what it did, pointing at the exact second. In the information half she answers one question and shows which part came from which source. It cannot be skipped the first time and `Ines's example` reopens it.

**Pins (all grades).** A pin has three parts: its kind (Added, Cut, Changed, Only here), what it is (grade 6: something seen, heard or left to imagine; grade 7: a technique from the list), and an effect line. Each of the five moments has a key: the kind, the thing, and a few word families an effect line about it would use (pause, wait, quiet; face, eyes, fear). A pin whose kind or thing is off is turned back once with "Look at that moment again"; an effect line that names nothing from the moment is turned back once with "What did it do to the scene?" After a second miss Ines shows hers and the pin prints as "shown".

**Grade 6, Story.** `Page`: Section III of "The Open Boat" (1897), adapted to about 600 words with cuts marked. `Audio`: a slow, hushed reading with sea sound. `Clip`: a 60-second animated clip of the lighthouse sighting. `Poem`: Longfellow's "The Tide Rises, the Tide Falls" on the page and read aloud. At each of five moments the page stops and asks "What do you see and hear in your head here?" The student writes a line. Only then does the audio or clip of that moment open, and the student pins the difference.

**Grade 6, Information.** How a lighthouse lens works, in four sources: an article (about 400 words), a narrated audio version, a diagram animation drawn in code (a lamp, rings of glass prisms bending light into one beam; Motion off shows steps), and a table of the six lens orders with each one's size. Five questions. Each needs two sources ("Which order of lens would a small harbor light use, and why are the rings shaped that way?"). The student writes the answer and tags each part with its source. The facts are keyed, and so are the sources that hold them: a part tagged to a source that does not hold it is turned back once.

**Grade 7, Story.** The same scene, with two audio readings (slow and hushed with sea sound; brisk and plain), the film clip with its shot, lighting and color notes, and a staged reading (three voices, a script page with stage directions). Five moments, each keyed to one technique from the list: pause, music, sound effect, close-up, wide shot, lighting, color, an actor's voice. The student pins the technique and its effect.

**Grade 7, Information.** Lincoln's Gettysburg Address: the text, two deliveries (measured and grave; fast and bright) and a words-with-pictures version (the words over period photographs). For each of five marked lines the student sets, for each delivery, what the speaker did (slows, pauses before it, leans on a word, drops the voice; keyed), picks which delivery makes the line land harder, and writes why. On the fifth line the pictures version is added: what does the picture add or take from the words?

**Grade 8, Story.** Dickens, "A Christmas Carol", Stave One, Marley's visit (about 700 words, with cuts marked), beside the same scene in the 1910 Edison film (silent, with title cards; about two minutes). Five moments. For each the student marks `faithful` or `departs`, taps the lines of the text that show it (the line kept, or the line changed or left out), picks whose choice it was (the director's: what is shown, cut or moved; the actor's: face, gesture, movement), and writes whether it was worth it. The mark and the lines are keyed and judged together; a miss says only "Check it against the page", and a second miss is printed as "shown". Three of the five depart.

**Grade 8, Information.** Five topics about lighthouses, each a card ("how the rings bend light"; "how the six orders compare in size"; "what a keeper's night was like"; "where the lights stood on one coast"; "why Fresnel's lens replaced mirrors"). For each, the same content is offered four ways: a printed page, a digital page with links and a search box, a short video, and a multimedia diagram the reader can step through. The student tries each, chooses the best medium for that topic, and gives one advantage and one limit from a keyed list plus a line in their own words. No medium is best for more than two topics.

**Recommend.** The student picks a request card and writes a recommendation: which version, and two pins or answers that support it.

**On your own.** In each half the last two items (moments, questions, lines or topics) run with Ines quiet: her example is closed, nothing is turned back, each part is answered once, and nothing is marked until both are in.

**The end.** A results strip for the teacher under the grade's two codes: for each, how many of the two items on your own were right in their keyed parts (kind and thing; sources; techniques; mark and lines; medium, advantage and limit), with the student's own lines printed beside them; then the counts for the three items before and anything printed as "shown".

**Class tally.** Counts per request card for each version.

At 1366x768 the version and pins fit side by side; at 680x425 pins are a drawer.

## Content
- Stephen Crane, "The Open Boat" (1897), section III, from "The Open Boat and Other Stories", Project Gutenberg eBook #45524, adapted with cuts marked. The story follows real events: Crane's ship, the Commodore, sank off Florida in January 1897. Used in grades 6 and 7 with different moments and different jobs.
- Grade 6 poem: Henry Wadsworth Longfellow, "The Tide Rises, the Tide Falls" (1880).
- Grade 7 speech: Abraham Lincoln, the Gettysburg Address (1863), Bliss copy.
- Grade 8 text and film: Charles Dickens, "A Christmas Carol" (1843), Stave One; "A Christmas Carol" (Edison Studios, 1910).
- Explainer facts: Augustin Fresnel's lens (1822) uses rings of glass prisms to bend and focus a lamp's light into a beam that can be seen many miles out; lenses come in orders by size, first order the largest; the light at Mosquito Inlet (today Ponce de Leon Inlet Light, Florida) was first lit in 1887. The table of orders gives each order's focal distance: first 920 mm, second 700 mm, third 500 mm, fourth 250 mm, fifth 187.5 mm, sixth 150 mm.
- Made for Curio Class: the audio readings, the 60-second clip, the staged reading, the two deliveries and the pictures version of the speech, the four-medium topic cards, the model rhyme.
- Data for each path: five moments, questions, lines or topics in each half with their keys (kind, thing and word families; facts and the sources that hold them; technique for each delivery; faithful or departs with the proving lines and whose choice; best medium with keyed advantages and limits).
- What a wrong answer on your own means. RL.6.7: a "what I pictured" line that only retells the sentence means the student is not yet noticing their own picture, so there is nothing to compare. RI.6.7: every part tagged to the article means the diagram and table are being looked at and not read. RL.7.7: naming "music" where the key is a pause means the student hears a mood and not the technique that made it. RI.7.7: picking the louder delivery every time means impact is being taken for volume. RL.8.7: marking a moment `departs` because it looks old or silent means the film is being judged and not checked against the page; calling a gesture the director's choice means the two roles are not yet apart. RI.8.7: choosing video for every topic means the medium is being picked for liking and not for what the topic needs.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Audio and film can be scrubbed; pins snap to the nearest second. A moment's audio or clip stays closed until the student's "what I pictured" line is in (grade 6).
- Access: every action works by tap and by keyboard. A pin is placed with a tap or Enter; scrubbing works with arrow keys. Every audio has its words on screen in time with it, sound effects and music are named in a caption ("soft sea sound", "long pause"), and the film's title cards are also given as text, so each item can be done with Sound off. Pin kinds and marks are words, never color alone. Motion can be paused.
- On your own: one answer for each part, no feedback until both items are in.
- With Motion off the diagram steps through stills and clips show as stills with captions.
- The readings are produced with bank voices and sea sound from the kit's sound set.

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
- how `picture`: "What do you see and hear in your head here? Write one line."
- how `tagHow`: "Tag each part of your answer with where you found it."
- how `lineHow`: "For each delivery, choose what the speaker did. Then say which lands harder."
- how `proof`: "Faithful or departs? Tap the lines on the page that show it."
- how `own`: "The last two are on your own. Answer each part once."
- event, whole, Ines's example.
Every `how` line is also shown as text beside its control. Instructions use no idioms.

## Family engine
None. Tool-only code: three-medium viewer, pins on text, audio and frames, lens diagram, recommendation card.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Pins | Type anything in the effect line | Kind, thing and effect line are keyed for each moment; a line that names nothing from the moment is turned back, and a second miss prints as shown. |
| What I pictured | Play the audio first | The moment's audio or clip is closed until the line is written. |
| Lens questions | Tag every part "article" | The sources that hold each fact are keyed, and each question needs two. |
| Deliveries | Pick the same delivery each time | Techniques are keyed for each line and delivery, and the harder-landing reading changes from line to line. |
| Faithful or departs | Mark everything departs, or everything faithful | Three depart and two do not; the mark needs the proving lines tapped, judged together, and a second miss prints. |
| Mediums | Pick one medium for all | No medium is best for more than two of the five topics; advantage and limit are keyed. |
| Recommendation | Pick a version with no reasons | It needs two pins or answers. |
| On your own | Lean on the turn-backs | Nothing is turned back and each part is answered once. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a request card: the card, `welcome` (queued, first time), then Ines's example (whole), waits.
2. Story: `sentence` (whole) on tap. Grade 6: `picture` at each moment, then `pinHow`. Grade 7: `pinHow`. Grade 8: `proof`, then `depart` for a keyed departure.
3. Information: grade 6 `tagHow`; grade 7 `lineHow`, and `twoReadings` after both deliveries.
4. Last two items of each half: `own`. Recommend: `recommendHow`.

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
Spec fix notes (2026-11-11): the six focal distances, the Longfellow poem and its date, the Dickens scene and the 1910 Edison film were written from memory and not opened in this pass. Build must confirm each, and that the film is in the public domain and can be shipped with the tool, before the grade 8 path is built.

## Done when
1. Focus and fold: at 1366x768 the version and pins fit; at 680x425 pins are a drawer.
2. Each grade path has its own texts, goal card and five items in each half, and none needs another. In grade 6 the student writes what they pictured before each audio or clip opens; pins are checked for kind, thing and effect. (RL.6.7, RL.7.7)
3. Grade 6's five lens questions each need two sources, with keyed source tags and a table of numbers. (RI.6.7)
4. Grade 7's five speech lines take a keyed technique for each delivery, a choice and a reason. (RI.7.7)
5. Grade 8's five film moments take a mark with proving lines, whose choice it was and a worth-it line; five topics take a best medium with an advantage and a limit. (RL.8.7, RI.8.7)
6. Recommendations need two pins or answers; the class tally counts.
7. Ines's example plays first and can be reopened; a second miss prints as shown.
8. The last two items of each half run with no example or turn-backs and one answer a part; the end screen shows the result under the grade's two codes.
9. Print shows pins, answers, recommendations and results.
10. Every spoken instruction is also on screen; every audio and film has its words and sounds as text; each key word shows with an example at first use; the frames can be left.
11. Every action works by keyboard as well as tap, nothing is shown by color alone, every item can be done with Sound off, and motion can be paused.
12. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
13. Motion off: the diagram and clips show as stills; no network requests.

## Open questions
- For Cory: RL.8.7 asks for a filmed or live production with actors and a director, which a storyboard cannot be. Default used: the grade 8 story half moves to "A Christmas Carol" with the 1910 Edison film, on the belief that it is public domain. If that film cannot be shipped, the fallback is a teacher-supplied production with the same five-moment sheet. This changes what must be made for the tool, so it needs a yes.
- For Cory: the paths now call for more made media (a 60-second clip, a staged reading, two speech deliveries, a pictures version, four-medium topic cards). Default used: all are specified; cut list if the cost is too high is the staged reading first, then the pictures version.

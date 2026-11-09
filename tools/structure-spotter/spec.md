# Structure Spotter

## One idea
The student hunts through "Fact Finder", a small kids' fact site with a search box, a sidebar and links, to find the paragraph that answers each question, then sorts that paragraph by how it is built (steps in order, this makes that happen, alike and different) by tapping the words that link its sentences, and a finding timer shows that key words and links beat scrolling, so they learn that how a text is built tells you where an answer is and how to find it fast.

## Not like
- how-it-works-diagrams (3-5, spec): sentences placed on an animated diagram. Here finding paragraphs on a site and naming their build.
- text-feature-makeover (1-2, spec): adding features to a page. Here using a site's search tools.
- blueprint-builder (4, spec): building facts to four structures. Here spotting three structures in found text, grade 3.
- note-card-shuffle (3, spec): notes from three pages. Here finding one answer fast.
- main-idea-pinboard (3-5, spec): proving a main idea. Here the shape of a paragraph.

## Who and how
- Grade 3, ELA, module "Text Structure and Search Tools" (Reading Informational). Standards: RI.3.3, RI.3.5, RI.3.8.
- Driver: one student (tool.json `driver: "student"`). Every paragraph is read on tap.
- Three topics (Volcanoes, Frogs, Bridges), four questions each. tool.json `modes: ["Solo", "Race"]`, `minutes: "15-25"`, `grades_label: "Grade 3"`.
- Nothing is saved; the site is a made-up site inside the tool and never goes online.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RI.3.5 | Find each answer with the search box, a sidebar box or a link; the finding timer and the tool used are logged | the site and a trail of tools used | 2, 3 |
| RI.3.8 | Sort the found paragraph into a bin, proved by tapping the linking words (first, then, because, so, both, but) | three bins and lit link words | 4 |
| RI.3.3 | The tapped time, sequence and cause words show how steps, events and science ideas connect | link words joined by small arrows between sentences | 4, 5 |
| RI.3.8 (same facts, three builds) | One frog fact written three ways; match each to the question it answers best | three paragraph cards and three questions | 6 |

## Screens and modes
Header (kit): title "Structure Spotter"; `Topics`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A kid's desk with a laptop showing "Fact Finder" and Scout, a meerkat with a magnifying glass on a lanyard. First hint: "Tap a question card to start a hunt." The first tap reads the question; the welcome is queued after it (`welcomeAfter: true`).

**Fact Finder.** A made-up kids' site in a browser frame drawn in code: a search box (matches whole words in paragraph key-word lists and headings, with simple word forms), a sidebar with boxes ("Did you know?", "Parts of a bridge"), headings, and links inside paragraphs. Each topic has 3 pages of 4 to 6 paragraphs. A question card sits on top: "Why does a volcano erupt? Find the answer."

**Hunt.** The student searches, opens a sidebar box or follows a link, and taps `This answers it` on a paragraph. Right paragraph: the trail shows the tools used and the time. Wrong paragraph: "Close! This one is about where volcanoes are. Try a key word from the question."

**Sort.** The found paragraph drops onto the sorting table with three bins: Steps in order, This makes that happen, Alike and different. The student taps the words that link the sentences; each tapped word lights and draws an arrow to the next sentence. The sort sticks only when at least two linking words of the bin's kind are tapped (data lists them per paragraph); otherwise "Which words link these sentences?"

**Timer race.** The first question of each topic is timed while scrolling only (search and sidebar locked); later questions unlock the tools. A chart after the topic shows the times with and without tools.

**Same facts, three builds.** One frog fact (frogs grow from eggs to tadpoles to adults) written as steps, as cause (warm water makes tadpoles grow faster), and as a comparison (tadpoles and frogs). Three questions: "What happens first?", "What makes it happen?", "How are they different?" The student matches each to the paragraph that answers it best.

**Race mode (class).** Two teams on one screen hunt for the same answer, one with search only, one with sidebar and links only; the times are compared.

At 1366x768 the site and sorting table fit side by side; at 680x425 the table is a tab.

## Content
Paragraphs written for Curio Class; every fact sourced. Twelve questions, each with one answering paragraph and its build:
- Volcanoes: Why does a volcano erupt? (cause: magma, gas and pressure); How does a volcano grow? (steps: layers of lava and ash pile up over eruptions); How are shield and cone volcanoes different? (alike and different); What happens after an eruption? (steps).
- Frogs: How does a frog grow? (steps: egg, tadpole, tadpole with legs, froglet, frog); Why do frogs need water? (cause: eggs and tadpoles live in water, skin must stay moist); How are frogs and toads different? (alike and different: toads usually have drier, bumpier skin and shorter legs); What do tadpoles eat? (a plain fact paragraph, no bin; "Not every paragraph has one of these three builds", with a fourth bin "Just facts").
- Bridges: How is a suspension bridge built? (steps: towers, main cables, hangers, deck); Why do bridges have trusses? (cause: triangles spread the load); How are beam and arch bridges different? (alike and different); Why do some bridges have expansion joints? (cause: metal grows in heat).

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Search is local and forgiving: lowercase, plural and -ing forms match.
- A tapped linking word can be untapped; arrows redraw.
- The timer counts seconds only while the hunt is open; it pauses when Read speaks.

## Look
- Accent `--brand` #0f6b7a lagoon teal (header, site frame, bins); gold #f4c542 (found paragraphs, lit link words); paper #f1f8f9; ink #0a2328; muted #495d61. Scene: a bright desk with a laptop.
- Contrast (WCAG 2.1, computed): white on brand 6.17:1; brand on paper 5.74:1; ink on paper 15.21:1; muted on paper 6.47:1; ink on gold 10.06:1.
- Never color alone: bins have words and icons (numbered steps, an arrow, two overlapping circles); lit words are underlined.
- Different from this batch (word violet, brick orange, storm slate, kite magenta).

## Art
Local FLUX (`scripts/localart.py`), no people.
- desk (1); Scout (4 poses: search, point, think, cheer), "A friendly meerkat with a magnifying glass on a lanyard <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- site photos (9): "<an erupting shield volcano / frog life stages / a suspension bridge at dusk>, realistic photo style, no people, no text"; 4:3; cutout no.
About 14 images. Drawn in code: site frame, search box, sidebar, bins, arrows, timer chart.

## Voice
Bank voice `upbeat-guide` as Scout and the paragraph reader (unique in this batch). `Curio.voice` with `scope: () => state.topic + ':' + state.question + ':' + state.step`, `welcomeAfter: true`.
- event `question`: "{Why does a volcano erupt?}"
- how `welcome`: "Fact Finder has the answer somewhere. Use the search box, the sidebar or a link to find it, then figure out how the paragraph is built."
- event, whole, `para`: the tapped paragraph.
- event `close`: "Close! This one is about {where volcanoes are}. Try a key word from the question."
- how `sortHow`: "Tap the words that link these sentences, then pick a bin."
- event `sorted`: "{Because} and {so}: this makes that happen!"
- event `faster`: "With the search box: {12} seconds. Scrolling: {41}."
- how `buildsHow`: "Same facts, three builds. Which one answers each question best?"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
text-features (`kit/text-features.js`), described in full in tools/windblown-pages/spec.md, exposed as `__tool.tf`. This tool uses: Page (the site pages with headings, sidebar boxes and links as feature pieces), Feature pieces (search box, sidebar, link, heading), Answer source (`tf.answerFrom` logs which feature found the answer). Not Reveal or Diagram. The search box, the timer and the structure bins are this tool's own additions.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Hunt | Tap This answers it on every paragraph | Wrong picks say what the paragraph is about; the trail logs each try, and the time keeps running. |
| Sort | Try bins until one sticks | A bin sticks only after two matching link words are tapped. |
| Link words | Tap every word | Untapped words don't block, but taps on non-linking words don't count, and 2 of the bin's kind are needed. |
| Three builds | Guess | 3 cards to 3 questions, 6 orders (checked); a wrong match reads the question again. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a question: `question`, `welcome` (queued, first time).
2. Hunt: `para` (whole) on taps; wrong: `close`.
3. Found: `sortHow` (first time); sorted: `sorted`.
4. After a topic: `faster`.
5. Builds page: `buildsHow`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RI.3.3, RI.3.5, RI.3.8 wording | thecorestandards.org, Reading Informational Grade 3 | CCSS ELA 2010 PDF | yes |
| Eruptions are driven by magma, dissolved gas and pressure; volcanoes grow from layers of lava and ash; shield and cone (stratovolcano) shapes differ | USGS Volcano Hazards Program, volcano types | Smithsonian Global Volcanism Program | yes |
| Frog life cycle: egg, tadpole, tadpole with legs, froglet, adult; toads usually have drier, bumpier skin and shorter legs | National Wildlife Federation, frogs and toads | Smithsonian's National Zoo, amphibians | yes |
| Suspension bridges hang the deck from cables over towers; trusses use triangles; arch and beam bridges carry loads differently; expansion joints let the deck grow and shrink with heat | PBS, Building Big: bridge basics | Federal Highway Administration, bridge basics | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad b12, 2026-11-09): all 11 answering paragraphs with a build hold at least two linking words of its bin's kind; 3 cards to 3 questions gives 6 orders; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the site and table fit; at 680x425 the table is a tab.
2. Search, sidebar and links reach every answer. (RI.3.5)
3. The trail logs the tools used and the time; the first question per topic is scroll-only. (RI.3.5)
4. A sort sticks only with two matching link words tapped. (RI.3.8, RI.3.3)
5. Arrows join linked sentences. (RI.3.3)
6. Same facts, three builds matches each version to its question. (RI.3.8)
7. Race mode compares two teams' times.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: arrows appear without drawing; no network requests.

## Open questions
- None for Cory.

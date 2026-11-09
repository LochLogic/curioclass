# How It Works Diagrams

## One idea
A short text explains how something happens (a seed sprouting, a canal lock lifting a boat, a bill becoming a law), and the student drags each sentence onto the part of a diagram, map or timeline where it happens and drags "because" links between causes and effects, and pressing Run plays the animation only up to the first gap, where the machine stops with the water halfway, so they learn that words and pictures explain a process together and that a missing "because" stops the machine; then a picture-only question and a words-only question show what each one adds.

## Not like
- structure-spotter (3, concept): sorting paragraphs by structure. Here placing sentences on a diagram of a process.
- text-feature-makeover (1-2, spec): adding features to a page. Here reading a diagram with a text at grades 3-5.
- bill-to-law-board-game (civics, concept): playing the process itself. Here reading about it.
- windblown-pages (K-2, spec): pictures back on their pages. Here steps and causes on a moving diagram.
- main-idea-pinboard (3-5, spec): main idea and support. Here sequence and cause.

## Who and how
- Grades 3-5, ELA, module "Diagrams and How Things Happen" (Reading Informational). Standards: RI.3.3, RI.3.7, RI.4.3, RI.4.7, RI.5.3.
- Driver: one student or a pair (tool.json `driver: "student"`). Every sentence is read on tap.
- Six levels by grade: grade 3 (How a Seed Sprouts, How a Volcano Erupts), grade 4 (The Canal Lock, The Dam Spillway), grade 5 (How a Bill Becomes a Law, How a Vaccine Is Tested). tool.json `modes: []`, `minutes: "10-15 per level"`, `grades_label: "Grades 3-5"`.
- Nothing is saved; `Print` prints a level's diagram with the placed sentences.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RI.3.3 | Place each step sentence on its hotspot in order; time words (first, next, then, finally) and cause words matter | sentences on the diagram, numbered | 2, 3 |
| RI.3.7 | Picture-only question answered from the diagram or map (where the magma collects; how deep the seed is) | the question and a tap on the diagram | 5 |
| RI.4.3 | Grade 4: drag "because" links between steps; Run needs every cause link | the link arrows | 3, 4 |
| RI.4.7 | Grade 4: a chart or timeline beside the text; say what it adds (a number the text doesn't give) | the chart and a pick | 5 |
| RI.5.3 | Grade 5: link people, groups and events (a senator, a committee, both houses, the president); explain the relationship in a sentence frame | role cards linked to steps | 6 |

## Screens and modes
Header (kit): title "How It Works Diagrams"; `Levels`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** An engineer's workshop with blueprints on the wall and Engineer Otto, an otter in overalls with a wrench. Six level blueprints. First hint: "Tap a blueprint to open a level." The first tap opens it with its line; the welcome is queued after it (`welcomeAfter: true`).

**Level.** The text on the left (5 to 8 sentences, tap to hear), the diagram on the right (drawn in code, 640 x 480) with numbered hotspots (one per step). Drag a sentence onto a hotspot; it snaps and shows a short form. At grade 4 and up, a link tool draws a "because" arrow from a cause step to its effect step (data lists required links).

**Run.** The animation plays step by step (each step is a small code animation: the gate opens, the water rises). It stops at the first hotspot with no sentence, a wrong sentence, or a missing required link, and Otto says what's missing ("The water can't rise. Which step lets it in?"). A wrong sentence glows on its hotspot and returns to the text.

**What each adds.** After a full run: a picture-only question (answered by tapping the diagram) and a words-only question (answered by tapping the sentence). Grade 4 levels add a chart or timeline (a small bar chart of lock heights; a timeline of a dam's year) with a "What does the chart add?" pick.

**Grade 5 roles.** Role cards (a senator, a committee, the House, the Senate, the president; or scientists, volunteers, a review board, doctors) are dragged onto the steps they act in. A frame completes the relationship: "The ___ can't ___ until the ___ ___."

At 1366x768 the text and diagram fit side by side; at 680x425 the text is a drawer.

## Content
Texts written for Curio Class; all facts sourced.
- **How a Seed Sprouts** (grade 3): the seed soaks up water; the seed coat splits; a root pushes out; a shoot reaches for light; leaves open and start making food. Picture-only: which way the root grows (the text never says; the diagram shows it going down).
- **How a Volcano Erupts** (grade 3): magma collects deep underground; gas and pressure build; magma rises through a vent; it erupts as lava, ash and gas; lava cools into rock. Picture-only: what the space where magma collects is called (the diagram labels it "magma chamber"; the text does not).
- **The Canal Lock** (grade 4): the boat enters the lower chamber; the lower gates close; valves let water in from the higher level; the water rises and lifts the boat; the upper gates open; the boat moves on. Because links: valves open, so water flows in; water rises, so the boat rises; levels match, so the gates can open. Chart: lifts of the Erie Canal's locks are given as a range, no single number claimed beyond the source.
- **The Dam Spillway** (grade 4): rain fills the reservoir; when water reaches the spillway, it flows over or through gates so the dam isn't overtopped. Timeline: a year of reservoir levels (illustrative, labeled as an example).
- **How a Bill Becomes a Law** (grade 5, US federal): a member of Congress introduces a bill; a committee studies it and may change it; the House votes; the Senate votes; both must pass the same text; the president signs it, or vetoes it; Congress can override a veto with a two-thirds vote in both houses.
- **How a Vaccine Is Tested** (grade 5): lab and animal studies; Phase 1 (a small group, safety); Phase 2 (hundreds, dose and safety); Phase 3 (thousands, does it work); review by the FDA; monitoring continues after approval.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Sentences snap to the nearest hotspot within 60 px; a keyboard alternative: pick a sentence, then a hotspot number.
- Run can be pressed any time; it always plays from the start to the first gap.
- Link arrows are drawn by tapping the cause step then the effect step; tapping an arrow removes it.

## Look
- Accent `--brand` #2b5c8a blueprint blue (header, blueprints, arrows); gold #f4c542 (hotspots, the run light); paper #f3f7fb; ink #0e1f30; muted #4b5a68. Scene: a tidy engineer's workshop.
- Contrast (WCAG 2.1, computed): white on brand 7.00:1; brand on paper 6.50:1; ink on paper 15.52:1; muted on paper 6.59:1; ink on gold 10.27:1.
- Never color alone: hotspots are numbered; arrows carry the word "because".
- Different from this batch (film-set red, cork brown, curtain plum, notecard green).

## Art
Diagrams are drawn in code so they animate. Local FLUX (`scripts/localart.py`): workshop (1); Otto (4 poses: point, wrench, think, cheer), "A friendly otter engineer in overalls with a wrench <pose>, soft gouache, plain white background"; 1:1; cutout yes; level backdrops (6, setting scenes like a canal with hills, a capitol building exterior with no people, a lab bench); 16:9.
About 11 images.

## Voice
Bank voice `science-narrator` as Otto and the text reader (unique in this batch). `Curio.voice` with `scope: () => state.level + ':' + state.step`, `welcomeAfter: true`.
- event `level`: "{The Canal Lock}. Let's get it running."
- how `welcome`: "The words and the picture explain this together. Put each sentence where it happens on the diagram, then press Run."
- event, whole, `sentence`: the tapped sentence.
- how `placeHow`: "Drag a sentence onto the step where it happens."
- how `linkHow`: "Some steps cause others. Tap the cause, then the step it causes."
- event `stuck`: the level's stuck line ("The water can't rise. Which step lets it in?").
- event `runs`: "It works! Every step and every because."
- how `addsHow`: "This question is answered by the picture only. Tap the diagram."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
text-features (`kit/text-features.js`), described in full in tools/windblown-pages/spec.md, exposed as `__tool.tf`. This tool uses: Page (text plus picture with hotspots), Answer source (`where: 'words'|'picture'` for the picture-only and words-only questions), Diagram (label spots with `tf.labelCheck`, and the step animation that runs only when every label and sentence is placed). Because links and role cards are this tool's own additions on the Diagram part.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Placement | Try sentences on hotspots until they stick | Wrong sentences glow and bounce back; trying is reading the step. 5 to 8 sentences give 120 to 40,320 orders (checked). |
| Links | Draw every arrow | Extra arrows that aren't causes stop Run with "Does this step cause that one?" |
| Picture-only | Answer from the text | The text doesn't contain the answer (checked per level). |
| Roles | Drag all roles to one step | Each role has its own steps; Run stops at the first wrong role. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a level: `level`, `welcome` (queued, first time), `placeHow`.
2. Sentences: `sentence` (whole). Grade 4 and up: `linkHow`.
3. Run: `stuck` at a gap, or `runs`.
4. After a full run: `addsHow`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RI.3.3, RI.3.7, RI.4.3, RI.4.7, RI.5.3 wording | thecorestandards.org, Reading Informational Grades 3 to 5 | CCSS ELA 2010 PDF | yes |
| Seed germination: water uptake, seed coat splits, root grows down, shoot up toward light | University of Minnesota Extension, starting seeds | RHS, how seeds germinate | yes |
| Eruption: magma in a chamber, gas pressure, rise through a vent, lava, ash and gas | USGS Volcano Hazards Program | Smithsonian Global Volcanism Program | yes |
| Lock operation: valves fill or empty the chamber to match levels, then gates open | US Army Corps of Engineers, how a lock works | New York State Canal Corporation, locks | yes |
| Spillways pass extra water so a dam is not overtopped | US Bureau of Reclamation, dams and spillways | US Army Corps of Engineers, dam safety | yes |
| Bill to law: committee, both houses pass the same text, president signs or vetoes, two-thirds override | Congress.gov, the legislative process | US House of Representatives, How Our Laws Are Made | yes |
| Vaccine testing in Phases 1 to 3, FDA review, ongoing monitoring | CDC, how vaccines are developed and approved | US FDA, vaccine development 101 | yes |
Backed twice: 7. Cut: 0.

Checks run (Python, scratchpad b11, 2026-11-09): orders 5! = 120 to 8! = 40,320; every level's picture-only answer word is absent from its text; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the text and diagram fit; at 680x425 the text is a drawer.
2. Sentences snap to hotspots, with a keyboard path. (RI.3.3)
3. Run stops at the first gap or wrong sentence. (RI.3.3, RI.4.3)
4. Grade 4 and up need every required because link; extra arrows stop Run. (RI.4.3)
5. Picture-only and words-only questions work; grade 4 chart picks work. (RI.3.7, RI.4.7)
6. Grade 5 roles link to steps and the frame completes. (RI.5.3)
7. Print shows the diagram with placed sentences.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: Run shows each step's end state instead of animating; no network requests.

## Open questions
- None for Cory.

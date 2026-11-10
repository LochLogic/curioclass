# Nature Inventor

## One idea
In an inventor's shed a problem board holds three people's problems (Sami's mitten keeps falling off, a crossing guard's cold walk to school, Grandpa's hard nuts), and the student opens a nature book of plant and animal parts (burr hooks, a polar bear's thick fur, a bird's strong beak, a turtle shell, duck feet, cactus spines, hedgehog quills), zooms in to see how each part helps the plant or animal survive, picks the part that solves the same kind of problem, builds a gadget from that idea (hooks and loops for the mitten, a fluffy layered coat, a beak-shaped nutcracker), and tests it on the problem, changing the design if it fails; real inventors cards tell true stories plainly (a hook-and-loop fastener came from burrs stuck to a dog's fur; bumps on humpback whale flippers inspired fan blades; a kingfisher's beak shaped a quieter bullet train nose); at the end a gallery shows each invention beside the part that inspired it, so a first grader learns to design a solution to a human problem by copying how plants and animals use their outside parts to survive.

## Not like
- who-s-my-baby (1, spec): parents and young. Here parts and what they do.
- shade-builder (K, spec): designing from parts in a box. Here designing from nature.
- shadow-puppet-studio (1, spec): materials and light. Here shapes from nature.
- beaver-builders (K, spec): an animal building. Here people copying animals.

## Who and how
- Grade 1, Science, module "Plant and Animal Parts". Standards: 1-LS1-1 (use materials to design a solution to a human problem by mimicking how plants and/or animals use their external parts to help them survive, grow, and meet their needs).
- Format: builder. Driver: one child alone or with a grown-up nearby (tool.json `driver: "student"`). Every card is spoken. Controls 56 px or more.
- Three problems, a nature book of seven parts, a build bench, a test for each, three real inventors cards, the gallery. Extra: Free invent (a new problem card each visit). tool.json `modes: ["Shed", "Free invent"]`, `minutes: "15-25"`, `grades_label: "Grade 1"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 1-LS1-1 (parts) | Zoom into each part and hear how it helps the plant or animal | the close-up; the "how it helps" card | 2 |
| 1-LS1-1 (mimic) | Pick the part that solves the same kind of problem and build from it | the build bench with nature-shaped pieces | 3 |
| 1-LS1-1 (test) | Test the gadget, change it if it fails, test again | the test scene; the fix | 4 |

## Screens and modes
Header (kit): title "Nature Inventor"; `Shed`, `Free invent`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more.

**On load and first tap.** A cozy inventor's shed with a problem board and a big nature book on the bench. Sami (made up, labeled "illustration") holds a mitten: "It keeps falling off at recess!" The welcome is queued (`welcomeAfter: true`): "Nature has solved lots of problems already. Look in the book for an idea. Tap the book." First hint: "Tap the nature book."

**The nature book (focus: the close-up).** At 1366x768 the book fills the left with the problem board right; at 680x425 the board is a sheet. Seven parts, each with a close-up and a spoken "how it helps": burr hooks grab fur so seeds travel; a polar bear's thick fur and fat keep it warm; a bird's strong beak cracks seeds; a turtle shell protects it; duck feet push water; cactus spines keep animals from eating it; hedgehog quills protect it.

**Build and test (focus: the bench).** For each problem the student picks a part, then builds from pieces shaped by it:
1. Sami's mitten: hooks and loops (from burrs) to strap it to the sleeve. Test: a windy, snowy recess; the mitten stays on.
2. The crossing guard's cold walk: a coat with thick layers (from polar bear fur). Test: a cold morning; a warmth meter with faces.
3. Grandpa's hard nuts: a beak-shaped nutcracker (from a bird's beak). Test: crack three nuts.
- A wrong pick (duck feet for the mitten) fails the test with a kind hint; the student changes one piece and tests again.

**Real inventors.** Three true stories, read aloud plainly:
1. In 1941 a Swiss engineer, George de Mestral, saw burrs stuck to his dog's fur; their tiny hooks led to the hook-and-loop fastener.
2. Bumps on the front edge of humpback whale flippers help them turn; engineers copied the bumps on fan and turbine blades.
3. A Japanese bullet train made a loud boom leaving tunnels; its nose was reshaped like a kingfisher's beak, which dives into water with little splash, and the train got quieter.

**The gallery (the aha).** Each invention beside its nature part, with the student's name on the plaque. Narrator: "You looked at how a plant or animal solves a problem, and you used the same idea. That's what real inventors do."

**The end.** The gallery. `Print` prints it as a picture page.

**Free invent (extra).** A new problem card each visit (a slippery shoe, a hot head in the sun).

## Content
- Three problems, seven parts with close-ups, about 12 build pieces, three tests, three real inventors cards, the gallery.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Pieces snap to the gadget frame; any piece can be swapped before a test.
- Keyboard: Tab to the book, parts, pieces and the test button; Enter places.
- With Motion off the tests show before and after pictures.

## Look
- Accent `--brand` #3b6e1e gadget green (header, the book, the bench); gold #f4c542 (the piece in hand, the passed test); paper #f3f8ef; ink #13240a; muted #555d4f.
- Contrast (WCAG 2.1, computed): white on brand 6.11:1; brand on paper 5.67:1; ink on paper 15.17:1; muted on paper 6.36:1; ink on gold 10.05:1.
- Never color alone: test results carry faces and words; parts carry spoken names.
- Different from this batch (berry, dusk blue, canyon rust, lagoon).

## Art
- Local FLUX (`scripts/localart.py`): the shed (1, 16:9); close-ups of seven parts (7, 1:1); three test scenes (3, 16:9); a kingfisher, a humpback flipper and a bullet train (3, 4:3).
- People (illustrated) for Sami, the crossing guard and Grandpa, labeled "illustration" (Gemini, `people: true`, 3; cutout yes).
- Drawn in code: build pieces, the gadget frame, the warmth meter.
About 17 images.

## Voice
Two bank voices, each unique in this batch: `hero-coach` as the inventor guide and hints; `curious-librarian` as the nature book and real inventors stories. `Curio.voice` with `scope: () => state.mode + ':' + state.problem + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `book`: "Tap a part to see how it helps."
- how `pick`: "Pick the part that solves this kind of problem."
- how `build`: "Drag pieces onto the gadget."
- how `test`: "Tap Test."
- event, whole, each test result.
- event, whole, each real inventors card.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the book, the bench, tests, the gallery.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Pick | Pick any part | A part that doesn't fit fails the test and the hint names the problem. |
| Build | Use every piece | Only pieces shaped by the chosen part fit the frame. |
| Gallery | Skip a problem | The gallery fills only with tested inventions. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `book`; `pick`.
2. `build`; `test`; result (whole), waits.
3. Real inventors (whole).
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for 1-LS1-1 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| De Mestral, burrs and the hook-and-loop fastener (1941) | Lemelson-MIT Program, "George de Mestral" | Smithsonian Magazine, "How Velcro was invented" | yes |
| Humpback flipper bumps and blade design | Fish and Battle, Journal of Morphology (1995) | NOAA Fisheries, "Humpback Whale" | yes |
| The kingfisher-shaped bullet train nose | Biomimicry Institute, AskNature, "Kingfisher beak and the Shinkansen" | Smithsonian Magazine, "Biomimicry" | yes |
| Polar bear fur and fat keep it warm; bird beaks crack seeds; burrs hitch on fur | Polar Bears International, "Polar bear adaptations" | Cornell Lab of Ornithology, "Bird beaks" | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad r26, 2026-11-09): three problems with one right part each among seven parts; three real inventors stories; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 book and board; at 680x425 sheet.
2. Seven parts each show how they help the plant or animal. (1-LS1-1)
3. Each problem's gadget is built from the matching nature part. (1-LS1-1)
4. Each gadget is tested, and a failed test can be fixed and retested. (1-LS1-1)
5. Three real inventors cards are true and plainly told.
6. Every card is spoken; controls are 56 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: before and after pictures; no network requests.

## Open questions
None.

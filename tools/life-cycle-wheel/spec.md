# Life Cycle Wheel

## One idea
An empty wheel waits beside a shuffled pile of real-looking stage pictures for a frog (eggs, tadpole, tadpole with legs, froglet, adult), and the student drags the cards into order around the wheel and spins it to check; wrong spots wobble with a hint ("Legs come before the tail is gone"); four more organisms each add a twist: a monarch butterfly's chrysalis, a bean's seed, flower and pod, a chicken's chick hatching after about three weeks with no tadpole-like stage, and a person who grows with no big change in body shape; then the five wheels stack on a board and the student tags each stage as birth, growth, reproduction or death, and the tags line up across all five; at the end the student builds a wheel for a new organism (a salmon, a sunflower or a sea turtle) from cards, showing the model works for any life, so a third grader learns to model life cycles that differ from one organism to the next but all share birth, growth, reproduction and death.

## Not like
- who-s-my-baby (1, spec): parents and young. Here the whole circle of a life.
- puppy-traits (3, concept): inherited traits. Here stages.
- fossil-clues (3, spec): lives long ago. Here lives going on now.
- plant-experiment-shelf (2, spec): what helps a plant grow. Here every stage of its life.

## Who and how
- Grade 3, Science, module "Life Cycles". Standards: 3-LS1-1 (develop models to describe that organisms have unique and diverse life cycles but all have in common birth, growth, reproduction, and death).
- Format: sort. Driver: one student alone, or the class on the projector (tool.json `driver: "either"`). `Read` reads every card. Controls 48 px or more.
- Five wheels, the compare board with four tags, a sixth wheel from a choice of three. Extra: Class wheel (the class orders cards together). tool.json `modes: ["Wheels", "Class wheel"]`, `minutes: "20-30"`, `grades_label: "Grade 3"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 3-LS1-1 (unique and diverse) | Order stage cards into wheels for five organisms | five different wheels with their twists | 2 |
| 3-LS1-1 (in common) | Tag every stage as birth, growth, reproduction or death | the tags lining up on the board | 3 |
| 3-LS1-1 (model) | Build a sixth wheel from cards without hints | the new wheel, tagged | 4 |

## Screens and modes
Header (kit): title "Life Cycle Wheel"; `Wheels`, `Class wheel`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** An empty wheel with five slots and a pile of frog stage pictures. The welcome is queued (`welcomeAfter: true`): "Every living thing has a life cycle. Put the frog's stages in order around the wheel. Drag a card to a slot." First hint: "Drag the eggs to the top slot."

**Building wheels (focus: the wheel).** At 1366x768 the wheel fills the left with the pile right; at 680x425 the pile is a sheet. After the slots fill, `Spin` checks: right cards glow; wrong spots wobble with a hint. Five organisms:
1. Frog: eggs, tadpole, tadpole with legs, froglet, adult.
2. Monarch butterfly: egg, caterpillar, chrysalis, adult; the twist is the chrysalis, when the body is rebuilt.
3. Bean plant: seed, seedling, flowering plant, pod with seeds; the twist is that the seeds start the next cycle.
4. Chicken: egg (about 21 days to hatch), chick, adult; no tadpole-like stage.
5. Human: baby, child, teen, adult, older adult; the body grows but keeps its shape.

**The compare board.** The five wheels unroll into rows. Four tags: Birth, Growth, Reproduction, Death. The student tags each stage; matching tags line up in columns across all five rows. Death is shown plainly and gently: an old frog resting, a fallen bean plant, a fading butterfly on a leaf, a grandparent with family. No gore.

**A new wheel (the aha).** The student picks a salmon, a sunflower or a sea turtle and builds its wheel from cards without hints, then tags it. Narrator: "Every life cycle is different. But every one has a start, growing, making new life, and an end. That's the pattern."

**The end.** Six wheels and the board. `Print` prints them as a wheel cut-out page.

**Class wheel (extra).** The class orders cards together.

## Content
- Six organisms' stage cards (about 30), the hints, the compare board, four tags.
- Death is shown gently and matter-of-factly.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Cards snap to slots; any card can be moved before `Spin`.
- Keyboard: Tab to cards, slots, `Spin` and tags; Enter places.
- With Motion off the wheel checks without spinning.

## Look
- Accent `--brand` #6b2f8f wheel violet (header, the wheel rim, tags); gold #f4c542 (the card in hand, a matched column); paper #f7f1fa; ink #210d2c; muted #5c5263.
- Contrast (WCAG 2.1, computed): white on brand 8.65:1; brand on paper 7.79:1; ink on paper 16.33:1; muted on paper 6.66:1; ink on gold 11.14:1.
- Never color alone: tags carry words and icons; checks show a mark and a sound.
- Different from this batch (clay pot, team blue, sandstone, winter teal).

## Art
- Local FLUX (`scripts/localart.py`): real-looking stage pictures for six organisms (about 30, 1:1).
- People (illustrated) for the human stages, labeled "illustration" (Gemini, `people: true`, 5; one person across ages).
- Drawn in code: the wheel, slots, the board, tags.
About 35 images.

## Voice
Two bank voices, each unique in this batch: `gentle-storyteller` as the narrator of each life; `bright-teacher` as the wheel guide and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.organism + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `place`: "Drag a card to a slot."
- how `spin`: "Tap Spin to check."
- event, whole, each organism's twist.
- how `tag`: "Drag a tag to each stage."
- how `new`: "Pick a new living thing and build its wheel."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the wheel, slots, spin check, the board, tags.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Wheels | Spin until it's right | Each spin shows a hint, but the new wheel has no hints. |
| Tags | Tag everything Growth | Each tag checks against the stage. |
| New wheel | Copy the frog's order | The new organism's cards don't fit the frog's stages. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `place`; `spin`.
2. Twist (whole), waits.
3. `tag`; `new`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for 3-LS1-1 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Frog life cycle stages | U.S. Geological Survey, Amphibian Research and Monitoring Initiative | Smithsonian's National Zoo, "Frogs" | yes |
| Monarch life cycle and the chrysalis | U.S. Forest Service, "Monarch Butterfly Life Cycle" | U.S. Fish and Wildlife Service, "Monarch" | yes |
| Chicken eggs hatch in about 21 days | University of Illinois Extension, "Embryology: incubation" | Penn State Extension, "Incubating eggs" | yes |
| Salmon and sea turtle life cycles | NOAA Fisheries, "Salmon life cycle" and "Sea turtles" | U.S. Fish and Wildlife Service, "Pacific salmon" | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad r27, 2026-11-09): five wheels plus one new wheel; frog 5 stages, monarch 4, bean 4, chicken 3, human 5 is 21 stages to tag; four tags; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 wheel and pile; at 680x425 sheet.
2. Five wheels are built in order with each twist named. (3-LS1-1)
3. Every stage is tagged and tags line up across organisms. (3-LS1-1)
4. A sixth wheel is built and tagged without hints. (3-LS1-1)
5. Death is shown plainly and gently.
6. Stage pictures are true to each organism.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no spin; no network requests.

## Open questions
None.

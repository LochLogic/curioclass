# Flower Lure

## One idea
In a summer meadow a hummingbird, a bumblebee and a night-flying hawk moth each need a meal, and the student designs a flower to win visits from one chosen pollinator by picking four traits (color, scent, shape and nectar, three options each, 81 designs in all), then runs a day (or a night for the moth) and watches visits tally and pollen move to a second flower of the same kind, so seeds set; a red tube with lots of nectar and no scent wins the hummingbird, a blue or yellow flower with a sweet smell and a landing lip wins the bee, a pale flower with a strong night scent and a long tube wins the moth, and each design card explains why (hummingbirds see red well and smell little; bees see blue and yellow and need a place to land; moths find flowers by smell in the dark); then a behavior gallery compares three animals whose behaviors raise their chances of raising young (a bowerbird building and decorating a bower, a male songbird singing to hold a territory and attract a mate, an emperor penguin father keeping an egg warm on his feet through winter), and the student matches each behavior to how it helps; at the end a claim card holds one plant and one animal example, so an eighth grader learns to use argument based on evidence for how characteristic animal behaviors and specialized plant structures affect the probability of successful reproduction.

## Not like
- gene-pool (8, concept): how traits are inherited. Here how traits win the next generation a chance.
- puppy-traits (3, spec): variation in one species. Here traits shaped for a partner.
- life-cycle-wheel (3, spec): stages of a life. Here the step where new life starts.
- plant-experiment-shelf (2, spec): what plants need to grow. Here how plants get pollinated.

## Who and how
- Grade 8, Science, module "Behaviors and Structures for Reproduction". Standard: MS-LS1-4 (use argument based on empirical evidence and scientific reasoning to support an explanation for how characteristic animal behaviors and specialized plant structures affect the probability of successful reproduction of animals and plants respectively).
- Format: builder. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Three pollinators, four traits with three options each, a day run with visit tally and seed count, three animal behaviors, the claim card. Extra: Real flowers (match six real flowers to their pollinators). tool.json `modes: ["Meadow", "Real flowers"]`, `minutes: "20-30"`, `grades_label: "Grade 8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-LS1-4 (plant structures) | Design a flower for each pollinator and run its day | the flower; the visit tally; seeds set | 2 |
| MS-LS1-4 (animal behaviors) | Match three behaviors to how they raise the chance of young | the behavior gallery | 3 |
| MS-LS1-4 (argument) | Write a claim with one plant and one animal example | the claim card with tallies | 4 |

## Screens and modes
Header (kit): title "Flower Lure"; `Meadow`, `Real flowers`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A sunny meadow with a bare green stem in the middle. A hummingbird hovers nearby. The welcome is queued (`welcomeAfter: true`): "This hummingbird is hungry. Design a flower it will visit. Tap a color." First hint: "Tap a color for the flower."

**Design (focus: the flower).** At 1366x768 the meadow is left with the trait picker right; at 680x425 the picker is a sheet. Four rows: color (red, blue, white), scent (none, sweet, strong at night), shape (long tube, open with a landing lip, wide bowl), nectar (a little, some, a lot). The flower redraws with each pick.

**The day (focus: the tally).** `Run day` plays a short time-lapse. Visits tally by pollinator; pollen dots travel to a second flower and seeds count up. A low count shows a card: "Few visits. What does a hummingbird notice?" After a strong design, the next pollinator unlocks. The moth's run is a night run.

**Design cards.** Each pollinator ends with a card: why these traits work, with a real flower example (hummingbird: cardinal flower; bee: a blue salvia; moth: evening primrose).

**Behavior gallery.** Three short scenes, drawn calm, no harm shown: a bowerbird arranging blue objects, a songbird singing from a post, an emperor penguin father with an egg on his feet in a storm. The student drags a card onto each: attracts a mate, holds a territory, keeps young safe.

**The claim card (the aha).** "Plants and animals have traits that raise the chance of young. A ___ flower works because ___ (tally: ___). A ___ does ___, which helps because ___." Narrator: "Flowers can't walk to each other. So they lure helpers. Animals do the work themselves."

**The end.** Three flowers, tallies, the gallery and the claim. `Print` prints them.

**Real flowers (extra).** Six real flower photos to match to pollinators.

## Content
- Three pollinators with stated preferences (a visit score per trait), the trait picker, a simple visit and seed model, three design cards, three behaviors, six real flowers.
- A note: "Visit scores are a model built from field studies."

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Traits can change between runs; the last three runs stay on a small chart.
- Keyboard: Tab to trait options, `Run day`, gallery cards and the claim; Enter picks.
- With Motion off visits and pollen show as counts only.

## Look
- Accent `--brand` #8e2f6b orchid (header, the trait picker, tallies); gold #f4c542 (the trait in focus, pollen); paper #fbf1f6; ink #2a0b1e; muted #5f4f58.
- Contrast (WCAG 2.1, computed): white on brand 7.58:1; brand on paper 6.87:1; ink on paper 16.32:1; muted on paper 6.92:1; ink on gold 11.08:1.
- Never color alone: the color trait always shows its name; tallies carry pollinator icons.
- Different from this batch (radio navy, bone tan, safety orange, town green).

## Art
- Local FLUX (`scripts/localart.py`): the meadow by day (1, 16:9), the meadow at night (1, 16:9), three pollinators (3, 1:1), three behavior scenes (3, 16:9).
- Real flowers: public domain or openly licensed photos, checked (6, 1:1).
- Drawn in code: the flower parts, the picker, tallies, pollen.
About 14 images.

## Voice
Two bank voices, each unique in this batch: `playful-friend` as the hummingbird; `warm-teacher` as the field biologist and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.pollinator + ':' + state.run + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `trait`: "Tap an option in each row."
- how `run`: "Tap Run day."
- event, whole, each design card.
- how `gallery`: "Drag a card onto each behavior."
- how `claim`: "Fill in the claim card."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the flower drawing, the visit model, the gallery. Preferences and examples sit in a marked block `/* FLOWER-LURE DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Designs | Try all 81 | Allowed, but the card asks why the winner works. |
| Gallery | Drag cards at random | Each scene accepts only its match, with a reason on a miss. |
| Claim | Skip tallies | The card needs a tally number. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `trait`; `run`.
2. Design card (whole), waits. Repeat for three pollinators.
3. `gallery`.
4. `claim`.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for MS-LS1-4 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Pollination syndromes: hummingbirds red tubes no scent; bees blue or yellow with landing platforms; moths pale with night scent | U.S. Forest Service, "Pollinator syndromes" | Pollinator Partnership, "Pollinator syndromes" | yes |
| Male bowerbirds build and decorate bowers to attract females | Australian Museum, "Satin bowerbird" | Smithsonian National Zoo, bowerbirds | yes |
| Songbirds sing to defend territory and attract mates | Cornell Lab of Ornithology, "Why birds sing" | Audubon, "Why do birds sing?" | yes |
| Emperor penguin fathers keep the egg on their feet through the winter | British Antarctic Survey, "Emperor penguin" | Australian Antarctic Division, "Emperor penguins" | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad r4, 2026-11-10): four traits with three options each give 81 designs; three pollinators times four traits is 12 choices; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 meadow and picker; at 680x425 sheet.
2. A flower is designed and run for each of three pollinators. (MS-LS1-4)
3. Three behaviors are matched to how they help. (MS-LS1-4)
4. The claim uses one plant and one animal example with a tally. (MS-LS1-4)
5. Preferences match the cited pollinator sources.
6. Behavior scenes show no harm.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: counts only; no network requests.

## Open questions
None.

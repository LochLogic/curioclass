# Leaf Factory

## One idea
Run one milkweed plant's leaf factory through an Iowa summer, week by week: open the stomata doors to let carbon
dioxide in (and water out), turn light into sugar, then spend every crate (new leaves, roots, starch for spring, seed
pods) while the plant burns sugar day and night, and a monarch caterpillar eats your leaves; then follow one carbon atom
as you break and rebuild its molecules with your own taps, from the air into sugar, a leaf, a caterpillar and back out.

## Not like
- energy-accountant (gr 9 data, spec): balances C, H, O, N and kilojoules in a ledger and follows a carbon through four
  Earth spheres with a passport of stamps. Here there are no kilojoules and no spheres: one plant's choices over a
  season, and the carbon trail stays inside a plant and a caterpillar, where the student rebuilds each molecule by hand.
  No "where did the wood come from" slider card.
- energy-pyramid (gr 7 builder, concept): energy and matter between feeding levels of a grassland. Here inside one
  organism, then one eater; no pyramid, no tenth rule.
- living-pond (gr 5 simulator, concept): populations and matter loops in a pond. Here one plant, no populations.
- lake-commons (gr 9 tycoon, spec): a town's century of five-year turns on a dark theme. Here a light theme, one summer
  of weekly turns, and the "company" is a living thing whose rules are photosynthesis and respiration.
- molecule-forge (gr 7 sandbox, draft): snaps atoms by bonding rules to grow a collection. Here no bonding rules: the
  same atoms are taken apart and put back together as different molecules, and the counter shows none appear or vanish.
- paper-plane-assembly-line (gr 3 social studies tycoon, this batch): a factory of workers and stations. Here the
  factory is a leaf; no workers, money or profit.

## Who and how
- Grade 7, science, module Photosynthesis and Respiration (science-7-photosynthesis-and-respiration). Standards:
  MS-LS1-6, MS-LS1-7. Driver: students (solo by default, pairs fine); a teacher can project Follow a carbon. 35 to 50
  minutes: Season 20 to 25, Follow a carbon 10, Explain 8.
- tool.json: driver "students or teacher", minutes "35-50", modes ["Season", "Follow a carbon", "Explain"],
  grades_label "Grade 7".
- No personal prompts. The season and the explanations are kept on this device (localStorage `curio-leaf-factory`,
  try/catch); the panel foot says "Your season stays on this device." (BASELINE 7).
- Teacher notes: all crate counts, rates and the weather are a model (labeled so); the photosynthesis and respiration
  ratios (6 to 1) are real. The model does not track which oxygen atoms come from water (in real leaves the O2 given
  off comes from water); MS-LS1-6 and 7 leave out the chemistry steps on purpose.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-LS1-6 (explanation, from evidence, of photosynthesis's role in cycling matter and energy into and out of organisms) | Season: set stomata and spending each week, read the week strip (in: CO2, water, light; out: sugar, O2; burned: sugar plus O2 to CO2 and water). Explain: build three claim, evidence, reasoning explanations from their own ledger (where the carbon came from, where the energy came from, what happened to burned sugar) | the factory running by day and the burner by night, the 6 to 1 strip, the season report's carbon summary, their own sentences with their own numbers | Done 2, 3, 7 |
| MS-LS1-7 (model of food rearranged into new molecules for growth or energy as it moves through an organism) | Follow a carbon: break 6 CO2 and 6 water apart and rebuild sugar and O2; link sugars into cellulose or starch; the caterpillar digests starch back into sugar, then links it into glycogen or burns it; predict the count first each time. Season: sugar spent on growth versus burned | atoms as lettered balls, the tagged gold-ringed carbon, the counter "Atoms in 36, atoms out 36", the energy bar moving from light into sugar and out as work and heat, the carbon trail | Done 4, 5, 6 |

## Screens and modes
Kit frame, light theme with the tool's own `:root` (Look). Header: "Leaf Factory", small line "Make sugar from air and
light, then spend it." Mode buttons `Season`, `Follow a carbon`, `Explain`; kit Motion, Sound, Read.
On load: Season, week 1 (June 1), plant of 3 leaves, 4 root units, 10 starch, 0 pods; Stomata Half; plan Leaves 40,
Roots 30, Starch 20, Pods 10. While Pods is locked its row reads "10, goes to Starch: flowers open in week 5" (its
`+` and `-` still set the share for later). Nothing
plays before the first tap. Hint: "You run this leaf's factory. Check the forecast, set the stomata and the plan, then
tap Next week." First tap on `Next week` runs week 1 (main path); any other first tap does its own job. The welcome may
be cut (BASELINE 16); the premise lives in the hint and Read.
Layout at 1366x768, all modes: header 52 px; stage left 64 percent, panel right 36 percent, everything above the fold.
At 1000x625 and 800x500 side by side with a compact panel (buttons first). At 680x425: the factory and plant views
share the stage with a `Plant` / `Factory` toggle (factory first while a week plays), the ledger strip folds into the
`Ledger` button, forecast shrinks to one line. At 760 and 375 wide the stage stacks on top at 16:10.

### Season (opens first)
Focus: the factory while a week plays; the plant and the week strip after it. Stage top 470 px: left 52 percent the
plant view (lf-field backdrop, a soil band lf-soil below the ground line with lf-roots scaled by root units 0.5 to 1.6
and the lf-rhizome with a starch meter drawn on it "Starch 30"); the stem (lf-stem, taller with leaves) carries leaf
cutouts in opposite pairs, flowers and pods, and the caterpillar beats. Right 48 percent the factory cutaway (lf-factory)
with code overlays: two stoma doors (lf-stoma-closed / half / open), a light beam, a water pipe from below, CO2 balls
drifting in, sugar crates rolling down a belt to four chutes labeled Leaves, Roots, Starch, Pods, and a burner (glows
while burning). Under the stage: the week strip (2 lines, 64 px) and a mini ledger (last 3 weeks, 120 px).
Panel top to bottom: hint; forecast card ("Week 9, July 27: Sunny, Hot and dry, Daylight 14.5 h", sky icon); `Stomata`
`.seg` with three stoma pictures `Closed`, `Half`, `Open`; Spending plan: four rows Leaves, Roots, Starch, Pods, each
with its share, a bar and `-` / `+` (10 percent steps); `Next week` (big, brand); `Ledger`, `Restart season`; foot line.
A week (Next week): 3 s. Day 1.6 s (sun arc, doors at the chosen opening, CO2 in, crates out, O2 bubbles out), night 1.0
s (moon, belt stops, burner eats crates, CO2 out), chutes 0.4 s (crates drop to the four chutes; new leaves, root growth,
starch meter, pods appear on the plant). Motion off: the end state at once. Then the strip, ledger and any beat line.
Week strip (real 6 to 1 ratios): "Made: 84 CO2 + 84 water + sunlight -> 14 sugar + 84 O2." / "Burned (day and night):
2 sugar + 12 O2 -> 12 CO2 + 12 water + energy for work and heat." Then "Kept 12: Leaves 6, Roots 3, Starch 3, Pods 0.
Water: Enough." Arrows are drawn in code, not typed.
`Ledger` opens the full table over the stage (Week, Weather, Stomata, Leaves at start, Sugar made, CO2 in, O2 out,
Burned, CO2 out, Net, To leaves, To roots, To starch, To pods, Water), 18 rows at 22 px; `Close`.
Season report (after week 18): frost (leaves turn lf-leaf-brown and fall, 1.5 s), then a card over the stage: left the
spring picture (lf-spring with 0 to 8 lf-shoot cutouts, one per 25 starch) and the open pods (lf-pod-open, one per
pod); right the carbon summary: "CO2 taken in", "CO2 given back by burning", "Carbon kept" split into leaves, roots,
starch, pods (a stacked bar), "Leaves eaten by the caterpillar", "Your plant burned [n] percent of what it made. Real
plants burn about a third to two thirds." Challenge line: "Challenge: 6 spring shoots and 5 pods" met or not. Buttons
`Explain this season` (to Explain), `Restart season`.
Outcomes (different at a glance):
1. Ran out (no leaves left, starch 0): bare brown stem, empty rhizome, spring picture is bare soil: "No leaves and no
   starch left in week [n]." Report opens at once.
2. Lived, starch under 25: green plant to frost, empty spring soil, "Nothing banked for spring."
3. Shoots but no pods: shoots in spring, no pods.
4. Pods but 0 or 1 shoot: open pods, almost bare spring soil.
5. Both: shoots and pods; with the Challenge met, the monarch butterfly (lf-butterfly) visits the spring shoots.

### Follow a carbon
Focus: the molecule bench. Stage: a top strip (90 px) with the carbon trail (station icons added as visited) and
"Paths found 0 of 4"; the bench (520 px) drawn in code over a soft painted backdrop that changes by station (lf-field
sky for Air, lf-factory for the leaf, lf-caterpillar close-up for the caterpillar, lf-frass for the soil); atoms are
balls with letters (C dark, O red, H white with outline), the tagged carbon has a gold ring; under the bench the energy
bar (Light, Stored in sugar, Released as work and heat) and the counter "Atoms loose [n] / Atoms in [n] / Atoms out
[n]" (hidden until the predict of that step is answered). Panel: hint; the predict card when one is due; step buttons
(`Break apart`, `Fill the rest`, `Next`), fork buttons when at a fork; `Start over` (new tag, trail kept).
Steps: Air: 8 CO2 drift; tap one to tag its carbon. Leaf: it drifts in through a stoma (`Next`). Build sugar: predict
P1, `Break apart` (6 CO2 and 6 water split into 6 C, 18 O, 12 H; light fills the energy bar), then tap an atom and a
matching empty spot in the sugar outline or an O2 outline (or drag); the tagged carbon must be placed by the student
(only the sugar has C spots); after the first O2 and the tagged carbon are placed, `Fill the rest` finishes. Fork in
the leaf: `Build a new leaf`, `Store as starch`, `Burn it`. Link (leaf: cellulose, straight chain; starch: coiled):
predict P2 the first time, then tap the 3 gaps between 4 sugars; each link pops one water. Burn: predict P3 the first
time, `Break apart` sugar and 6 O2, rebuild 6 CO2 and 6 water (tagged carbon into a CO2), energy bar empties to "work
and heat", carbon back to Air. Caterpillar: lf-caterpillar-eat chews the leaf. Cellulose path: "Much of the tough cell
wall passes through", to Frass, then Soil ("Fungi and bacteria break it down and breathe the carbon out."), back to
Air. Starch path: Digest (tap the 3 links to break them; each takes a water back), then fork `Build caterpillar body`
(link into glycogen, "It grows: about 2,000 times its hatching mass in about two weeks.") then `Burn it later`, or
`Burn it` (caterpillar respiration, carbon breathed out). Paths: A leaf burn; B cellulose to soil; C starch to
caterpillar glycogen then burned; D starch to caterpillar burned. Each completed loop marks its path.

### Explain
Focus: the explanation paper. Stage: left 55 percent the student's ledger (compact, all weeks played; rows a chosen
evidence names are lit with a left bar), right 45 percent a paper card (drawn in code) where the paragraph builds:
Claim, Evidence, Reasoning, with the student's numbers. Panel: hint; question chips Q1, Q2, Q3 (state: open,
explained, explained fixed); the step label (Claim, Evidence, Reasoning); option buttons (4, 4, 3); after a wrong pick
the reason and the options again; `Next question`. If the season has not reached week 12, the ledger card shows
`Use my season so far` (disabled until week 12) and `Use a sample season` (the default plan, Half all season), with
"Sample season: the plan the tool starts with." over the ledger.

## Content
Model (whole crates; L leaves and R root units at the start of the week; S starch; P pods):
- made = round(5 x 24 x (1 - e^(-L/24)) x sky x daylight/15 x stomataCO2 x water). sky: Sunny 1, Mixed 0.7, Cloudy
  0.4. stomataCO2: Closed 0, Half 0.6, Open 1.
- water = min(1, 2 x R x soil / (L x stomataWater x heat)); 1 when the demand is 0. soil: Wet 1, Normal 0.6, Dry 0.3.
  stomataWater: Closed 0, Half 0.5, Open 1. heat: Hot 1.6, else 1. Status: Enough 0.8 or more, Short 0.5 to 0.8,
  Wilting under 0.5 (then the plant loses max(1, round(0.3 x L)) leaves, never the last one).
- burned = round(0.35 x (L + R)). net = made - burned. CO2 in and O2 out = 6 x made; O2 used, CO2 out and water out = 6
  x burned.
- net 0 or more: split by the plan, whole crates by largest remainder (ties in order Leaves, Roots, Starch, Pods). Each
  4 crates to Leaves = 1 leaf, 4 to Roots = 1 root unit, 6 to Pods = 1 pod (carry-over kept); Starch adds 1 to 1.
  Pods take crates only in weeks 5 to 13; outside them the Pods share goes to Starch and the row says "goes to Starch:
  flowers open in week 5" or "goes to Starch: too late to ripen before frost".
- net below 0: taken from starch; if starch runs out, 1 leaf lost per 2 crates short (rounded up).
- Caterpillar: end of week 7 eggs (lf-eggs) on a leaf; weeks 8 and 9 it eats 1 leaf each (if 2 or more); week 10
  chrysalis (lf-chrysalis) on the stem; week 12 butterfly flies off. Ends: no leaves (outcome 1); after week 18, spring
  shoots = min(8, floor(S / 25)), pods = P.
- Plan buttons: `+` on Leaves, Roots or Pods takes 10 from Starch, or from the largest other row if Starch is 0; `-`
  gives 10 to Starch; Starch's own `+` takes 10 from the largest other row, its `-` gives 10 to Leaves. Total always
  100; a row at 0 has `-` disabled, a full 100 has `+` disabled.
Weeks (date, sky, soil, heat, daylight h at 41.6 N): 1 Jun 1 Sunny Wet 15.0; 2 Jun 8 Mixed Wet 15.1; 3 Jun 15 Sunny Normal
15.2; 4 Jun 22 Cloudy Wet 15.2; 5 Jun 29 Sunny Normal 15.1; 6 Jul 6 Sunny Normal 15.0; 7 Jul 13 Mixed Normal 14.9; 8 Jul 20
Sunny Normal Hot 14.7; 9 Jul 27 Sunny Dry Hot 14.5; 10 Aug 3 Sunny Dry Hot 14.2; 11 Aug 10 Sunny Dry Hot 13.9; 12 Aug 17
Cloudy Wet 13.6; 13 Aug 24 Mixed Normal 13.3; 14 Aug 31 Sunny Normal 13.0; 15 Sep 7 Cloudy Wet 12.6; 16 Sep 14 Mixed Normal
12.3; 17 Sep 21 Sunny Normal 12.0; 18 Sep 28 Mixed Normal 11.6. Then "First frost" (central Iowa: usually early October).
Worked seasons (computed): default plan, Half all season: 260 made, 108 burned (42 percent), 16 leaves, 44 starch, 1
pod: 1 shoot, 1 pod; carbon kept 152 = leaves 62 + roots 48 + starch 34 + pods 8. A strong plan (Open except Half in
weeks 9 to 11; weeks 1 to 9 Leaves 50 Roots 30 Starch 10 Pods 10; weeks 10 to 13 Starch 40 Pods 60; then Starch 100):
586 made, 191 burned (33 percent), 208 starch, 8 pods: 8 shoots, 8 pods.
Factory facts (tap the factory's `?` for a card; also in Read when open): "Stomata are tiny doors in the leaf. Open, CO2
comes in and water vapor escapes: several hundred water molecules for each CO2." "The plant burns sugar all day and all
night. At night it is the only line running." "Starch and cellulose are both chains of sugar." "Milkweed is a
perennial: frost kills the stems, and starch in the underground rhizome grows next spring's shoots." "Monarch
caterpillars eat only milkweed." Beat captions: eggs "Monarch eggs on your leaves."; eat "A monarch caterpillar is
eating your leaves. It eats only milkweed."; chrysalis "It hung up and made a chrysalis."; butterfly "A monarch, built
partly from your plant's carbon, flies off."; dry "Hot, dry weeks ahead."; wilt "Your leaves wilted: [n] lost."; starve
"Out of starch: the plant broke down [n] leaves to keep running."
Predicts (one try, shuffled; after the pick, the right answer marked and the build shows it):
- P1 "6 CO2 and 6 water hold 18 oxygen atoms. The sugar keeps 6. How many O2 molecules go out?" 6 (right); 12 ("12 is
  the atoms. Each O2 is a pair, so 12 atoms make 6 O2."); 3; 18.
- P2 "Link 4 sugars into a chain. Each link gives off one water. How many waters?" 3 (right); 4 ("4 sugars have only
  3 gaps between them."); 2; 8.
- P3 "1 sugar and 6 O2 hold 36 atoms. After burning, how many atoms come out in the CO2 and water?" "36, the same atoms"
  (right); "30: some atoms became energy"; "0: it all became energy"; "42: burning adds atoms". Wrong reason: "Atoms
  are never used up. Only the energy in the bonds is released."
Explain (week numbers and counts are filled from the ledger; w = the week with the most sugar made, b = the most
burned, ties earliest; pair = a cloudy week c (4, 12 or 15, made above 0) and the nearest sunny, not dry week s with
the same stomata and no more leaves at start than c; no pair: the evidence keeps only its first sentence). Options
shuffled; wrong pick: a reason, then pick again (marked "fixed").
- Q1 "Where did the carbon in your plant's sugar come from?" Claims: "From carbon dioxide in the air." (right); "From
  the soil, through the roots."; "From the water the roots took up."; "From the sunlight the leaves caught." Evidence:
  "Every week CO2 in was 6 times the sugar made: week [w] took in [6M] and made [M]." (right); "At night in week [b] the
  plant gave off [6B] CO2."; "The roots grew from 4 to [R] units and took up water all season."; "Cloudy week [c] made
  [Mc] sugar; sunny week [s] made [Ms]." Reasoning: "Sugar's carbon must come from an input that holds carbon. Of light,
  water and CO2, only CO2 has carbon, and sugar rose with CO2 in." (right); "Roots take food from the soil, and the
  plant builds its sugar from that food."; "Sunlight turns into carbon atoms inside the leaf, and those become sugar."
- Q2 "Where did the energy stored in your plant's sugar come from?" Claims: "From sunlight." (right); "From the soil."; "From
  the water."; "From the carbon dioxide." Evidence: "No sugar was made at night. Sunny week [s] ([Ls] leaves) made
  [Ms]; cloudy week [c] ([Lc] leaves) made [Mc]." (right); "Dry week 10 made [M10] sugar."; "Week [w] took in [6M] CO2
  and made [M] sugar."; "The roots grew from 4 to [R] units." Reasoning: "Sugar was made only while light reached the
  leaves, and less in dim light, so its energy came from light." (right); "Water carries energy up from the soil and
  packs it into the sugar."; "CO2 is full of energy, so more CO2 in means more energy stored."
- Q3 "What happened to the sugar your plant burned?" Claims: "Broken down with oxygen into CO2 and water, releasing its
  energy." (right); "Turned into pure energy, so its atoms were gone."; "Stored away as starch in the rhizome."; "Sent
  back out of the leaf as sunlight." Evidence: "Week [b]: [B] sugar burned, using [6B] O2 and giving off [6B] CO2 and [6B]
  water." (right); "Week [b]: [Sb] crates went into starch."; "Week [w]: the leaves made [M] sugar and gave off [6M]
  O2."; "In weeks 8 and 9 the caterpillar ate [e] leaves." Reasoning: "The atoms in the sugar and O2 came out as CO2
  and water; only the energy left, used for growth and given off as heat." (right); "Atoms get used up when a plant
  needs energy, so fewer come out."; "Burning makes new carbon atoms, so more CO2 comes out."
Wrong-pick reasons: claim "Look at the week strip: what goes in that holds carbon (or brings energy, or comes out)?";
evidence "That is true, but does it show [the claim]? Find the row that does."; reasoning "Which sentence keeps every
atom and links your evidence to your claim?" Finished paragraph: claim, evidence and reasoning as one paragraph.

## Interactions in detail
- Any tap during a week's animation finishes it at once (results shown), then does its own job; `Next week` during a
  week finishes it and starts the next. Settings changed after a week apply to the next one; the forecast names it.
- Mode switch during a week finishes it. Season state survives mode switches and reloads (saved each week).
- `Restart season` asks "Start the summer over?" `Restart` / `Keep`. Explanations stay marked until a restart.
- Stomata Closed in a wet week: no water lost, no sugar; the strip says "Doors closed: no CO2 in, no sugar made."
- Follow a carbon: a wrong element on a spot bounces back ("That spot holds an O."); no penalty. Keyboard: Tab to an
  atom, Enter, Tab to a spot, Enter; `Fill the rest` also by key F. `Start over` keeps paths found.
- Explain: the paragraph is kept on this device; `Next question` is live after any pick; chips let the student go back.
- `window.__tool = {state, setMode, season: {stomata(s), plan(obj), next(), restart(), ledger()}, carbon: {tag(i),
  predict(i), breakApart(), place(atom, spot), fill(), fork(name), link(i), next()}, explain: {use(kind), pick(i)},
  allLines, vlog}`.

## Look
Light field palette: paper `#f3f5ec`, panel `#ffffff`, tint `#e4efd9`, ink `#1b241c`, muted `#56625a`, button line
`#7b867d`, focus `#1f5fd1`, warn `#a8321d`. Accent `--brand #2e6a1e` (chlorophyll green: Next week, plan bars, the trail).
Sugar `#8a5800` (crate labels, starch meter), night `#2b3a67` (night tint 35 percent on the stage), O atoms `#c0392b`, C
atoms `#3a3a3a`, H white with a `#56625a` outline, tagged carbon ring `#a87200`. Neighbors: lake-commons reed green
`#7cac64` on dark, energy-accountant gilt on dark, electromagnet-lab teal, cooler-challenge red, bug-hunt mauve,
molecule-forge per its spec. Contrast (computed): ink 14.50 paper / 15.96 panel; muted 5.80 / 6.38; brand 5.97 / 6.57,
on tint 5.52, white on brand 6.57; sugar 5.49 / 6.04; night text 10.02; O red 4.94 / 5.44, white on O 5.44; white on C
11.37; warn 6.08; focus 5.28; ring 3.76 (non-text); button line 3.44 (non-text). Atoms carry letters, wilting carries a
word, so color is never the only signal.

## Art
Local FLUX, one style: soft painted realism, summer light. No people (`people: false` on all).
- lf-field: "A sunny Iowa field edge in summer, tall grasses, blue sky, distant row of trees"; 16:9; no; plant view.
- lf-soil: "A band of dark brown soil in cross section with small pebbles"; 4:1; no; under the ground line.
- lf-stem: "A tall bare green common milkweed stalk"; 9:16; yes; scaled taller with leaves.
- lf-leaf, lf-leaf-wilt, lf-leaf-brown: "A broad oval common milkweed leaf with a pale midrib" / "the same leaf drooping
  and curled" / "the same leaf dry and brown"; 9:16; yes; placed in pairs, rotated by code.
- lf-roots, lf-rhizome: "A spray of fine pale roots" / "A thick pale underground milkweed rhizome"; 4:1; yes.
- lf-flower: "A round cluster of pink-purple milkweed flowers"; 1:1; yes. lf-pod, lf-pod-open: "A green warty milkweed
  seed pod" / "A split milkweed pod with brown seeds and white silk"; 3:4; yes.
- lf-shoot: "A young milkweed shoot pushing out of spring soil"; 3:4; yes. lf-spring: "Bare spring soil at a field edge,
  morning light"; 16:9; no; the report.
- lf-eggs: "One tiny cream-colored monarch egg on a green leaf"; 1:1; yes. lf-caterpillar, lf-caterpillar-eat: "A
  monarch caterpillar with yellow, black and white bands, side view" / "the same caterpillar chewing a leaf edge"; 4:1;
  yes. lf-chrysalis: "A jade green monarch chrysalis with gold dots"; 3:4; yes. lf-butterfly: "A monarch butterfly with
  open orange and black wings"; 4:3; yes.
- lf-factory: "Inside a leaf drawn as a bright green factory hall, rows of rounded green chloroplast workbenches, blank
  wall panels, soft light from above"; 16:9; no; factory cutaway and the Follow leaf backdrop.
- lf-stoma-closed, lf-stoma-half, lf-stoma-open: "A leaf pore between two bean-shaped guard cells, shut" / "slightly
  open" / "wide open"; 1:1; yes; factory doors and the Stomata buttons.
- lf-frass: "Small dark round caterpillar droppings on brown soil"; 1:1; no; Follow soil backdrop.
Code: belt, crates, chutes, burner glow, sky arc, CO2 and O2 balls, every molecule and atom, bars, ledger, all labels.

## Voice
Bank voice `science-narrator`, style "Say in a clear, informative way, like a nature documentary narrator, with quiet
wonder." Neighbors use casual-peer (pocket-universe, bug-hunt), friendly-dad (cooler-challenge, warming-evidence-desk),
knowing-guide (molecule-forge), gravel-ranger (electromagnet-lab), firm-captain (span-and-spire, grid-operator),
easy-coach (lake-commons), playful-friend (mole-bakery), calm-professor (energy-accountant). `Curio.voice`, `scope: () =>
state.mode`. Grade 7: numbers stay on screen; no line reads data.
| Key | Kind | When | Stale when | Whole | Text |
|---|---|---|---|---|---|
| wSeason | how | Season welcome | week 1 played | no | You run this leaf's factory. Check the forecast, set the stomata and the plan, then tap Next week. |
| night | how | first night of week 1 | week ends | no | Night. The light is gone, but the plant still burns sugar to stay alive. |
| plan | how | after week 1 | a plan button tapped | no | Every crate you keep gets spent. Use the plus and minus buttons to change the plan. |
| eggs | event | end of week 7 | week 8 starts | yes | Monarch eggs on your leaves. A caterpillar is coming. |
| eat | event | weeks 8 and 9 | next week | yes | The caterpillar is eating your leaves. It eats only milkweed. |
| dry | event | after week 8 | week 9 played | yes | Hot, dry weeks ahead. Open doors lose a lot of water. |
| wilt | event | a wilting week, once per dry spell | next week | yes | Your leaves wilted. The plant lost some of them. |
| starve | event | a starving week | next week | yes | Out of starch. The plant is breaking down its own leaves. |
| pods | how | week 5 starts | Pods share set | no | The flowers are open. You can spend on seed pods now. |
| late | how | week 14 starts | week 15 | no | Too late for new pods to ripen. Bank starch for spring. |
| butterfly | event | week 12 | next week | yes | A monarch flies off, built partly from your plant's carbon. |
| frost | event | after week 18 | report closed | yes | Frost. The leaves are gone. What you banked decides next spring. |
| out | event | outcome 1 | report closed | yes | No leaves and no starch left. The factory has stopped. |
| wCarbon | how | Follow welcome | a CO2 tagged | no | Tap one carbon dioxide molecule to tag its carbon atom. |
| into | how | tagged | Next | no | It drifts in through a stoma. Tap Next. |
| predict | how | first predict card | picked | no | Predict first. Tap your answer. |
| right | event | right predict | build starts | yes | Right. Now build it and check. |
| wrongP | event | wrong predict | build starts | yes | Not quite. Read why, then build it and see. |
| breakApart | how | first build step | atoms loose | no | Tap Break apart. |
| place | how | atoms loose, first time | tagged carbon placed | no | Tap an atom, then an empty spot of the same letter. Place your gold carbon yourself. |
| fillRest | how | first O2 and tagged carbon placed | filled | no | Tap Fill the rest to finish the same way. |
| same | event | a build ends | next step | yes | Same atoms in, same atoms out. New molecules. |
| fork | how | first fork | fork picked | no | Where does your sugar go? Tap a path. |
| link | how | first link step | linked | no | Tap each gap between the sugars to link them. |
| eaten | event | caterpillar eats the leaf | next step | yes | A caterpillar eats the leaf, and your carbon goes with it. |
| path | event | a path completed | next tag | yes | Path found. Your carbon is back in the air. |
| wExplain | how | Explain welcome | a claim picked | no | Use your own season to explain. Tap the claim you can back up. |
| evidence | how | first evidence step | picked | no | Now tap the row from your ledger that shows it. |
| reason | how | first reasoning step | picked | no | Last, tap the reason that links your evidence to your claim. |
| explained | event | a paragraph completes | next question | yes | Explained, with your own numbers. |
How lines once per page load, then hint only. Events every time, at most once per action; wilt once per dry spell.
Read speaks the hint; in Season it adds the forecast.

## Family engine
none: no family covers organisms or molecules; the tool draws its own factory overlays, molecules, bars and ledger.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Season challenge (6 shoots, 5 pods) | do nothing; mash Next week on defaults; random weekly settings; one lever only; the common wrongs (doors always open, close them when worried, store from day one, grow leaves all summer); read the answer off a preview | nothing moves without Next week, no timer; defaults give 1 shoot, 1 pod; random week-by-week mashing 0 of 30,000; starch only 4 shoots 0 pods, pods only 2 and 9, leaves only 0 and 0, roots only and always Closed die; always Open (default plan) 3 and 3, wilts; strong plan but Closed in the drought 5 and 5 (starves), Open in the drought 5 and 6 (wilts); growing leaves to week 15 gives 5 and 2; no roots 2 and 3; even 25s 4 and 5; there is no preview of a week, only the weather forecast |
| Season challenge | copy a classmate's plan | the weather is the same for all, so a copied plan works; the challenge is optional and never recorded as a grade; Explain then asks the student to explain their own ledger |
| Predicts P1 to P3 | guess; position; longest; elimination across predicts; count atoms vs molecules; the common wrongs | one try, shuffled; answers differ (6, 3, 36) and options differ; 12 (atoms not molecules), 4 (sugars not gaps) and "some atoms became energy" are options and fail; the atoms counter is hidden until the pick |
| Answer on screen | the counter, the outlines or the trail show it | the counter appears only after the predict; outlines show one sugar and the O2 spots only after the pick; the trail shows stations, never counts |
| Build steps | mash atoms onto spots | not scored: a wrong element bounces; the model only completes with every atom used, which is the point shown |
| Paths found | tap Next through | each path needs its fork chosen and its build done; nothing marks by waiting |
| Explain claim | guess; keyword match; longest; elimination; common wrong (soil for carbon; atoms used up) | four claims of similar length, shuffled; the common wrongs are options and fail; a wrong pick shows a reason and marks "fixed" |
| Explain evidence | pick any row with the claim's word; pick a big number | all four are true and from the student's own ledger; a wrong one shares the key word (CO2 out at night in Q1, CO2 in in Q2, O2 out in Q3); only the right one bears on the claim |
| Explain reasoning | guess; longest | three of similar length; the wrongs state the misconceptions (food from soil, atoms used up, water carries energy) |
| Doing nothing | wait | nothing marks without an action |

## Heard in order
Grade 7: most text is read; beat lines and results land before the next prompt.
- Season week: Next week; the day (night line the first time, at the night phase); the week ends; one beat line in the
  order eggs, eat, dry, wilt, starve, pods, late, butterfly, whole; then plan (first time). A tap drops queued how lines,
  never a beat. After week 18: frost, whole, then the report.
- Follow: wCarbon; tag, into; predict, the pick, right or wrongP whole before breakApart; place; fillRest; same whole
  before fork; eaten whole; path whole before the next tag line.
- Explain: wExplain; claim pick (a wrong pick's reason shows; no line); evidence; reason; explained whole before the next
  question's claim.
- The welcome may be cut by the first tap (BASELINE 16); its content stays in the hint and Read.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| 6 CO2 + 6 H2O + light -> sugar (C6H12O6) + 6 O2 | OpenStax Biology 2e 8.1 | OpenStax Concepts of Biology 5.1 | yes |
| Sugar's carbon comes from CO2 entering through stomata | OpenStax Biology 2e 8.1, 8.3 | Khan Academy "Intro to photosynthesis" | yes |
| The light energy is stored in sugar's bonds | OpenStax Biology 2e 8.1 | OpenStax Concepts of Biology 5.1 | yes |
| Sugar + 6 O2 -> 6 CO2 + 6 H2O + energy (respiration) | OpenStax Biology 2e 7.1 | OpenStax Concepts of Biology 4.2 | yes |
| Plants respire day and night; at night only respiration runs | OpenStax Biology 2e 8.3 | Taiz and Zeiger, Plant Physiology 6e ch. 12 | yes |
| Plants burn about a third to two thirds of the sugar they make | Amthor, Annals of Botany 86 (2000) 1 | Gifford, Functional Plant Biology 30 (2003) 171 | yes |
| Stomata let CO2 in and water vapor out; plants close them when water is short | OpenStax Biology 2e 30.6 | Taiz and Zeiger ch. 4 | yes |
| Several hundred water molecules are lost per CO2 taken in | Morris et al., Biology: How Life Works 2e 29.5 | Raven (1984) as cited in Taiz and Zeiger ch. 4 (200 to 400; varies) | yes |
| Starch and cellulose are chains of glucose | OpenStax Biology 2e 3.2 | OpenStax Concepts of Biology 2.3 | yes |
| Linking sugars gives off one water per link; breaking a link takes one | OpenStax Biology 2e 3.1 | Khan Academy "Dehydration synthesis and hydrolysis" | yes |
| Atoms are conserved in chemical reactions | OpenStax Chemistry 2e 4.1 | NGSS MS-PS1-5 | yes |
| Common milkweed is a perennial; stems die at frost and it regrows from rhizomes | USDA NRCS Plant Guide, Asclepias syriaca | Penn State Extension, "Common Milkweed" | yes |
| Perennials store starch underground for spring regrowth | Taiz and Zeiger ch. 11 | USDA NRCS Plant Guide (rhizome reserves) | yes |
| Common milkweed blooms about June to August; pods ripen late summer to fall | USDA NRCS Plant Guide | Monarch Joint Venture, "Milkweed" | yes |
| Monarch caterpillars eat only milkweed | Monarch Joint Venture, "Life Cycle" | Journey North, "Larva Facts" | yes |
| Caterpillar stage about two weeks; mass grows about 2,000 times | Journey North, "Larva Facts" | UC Riverside Botanic Gardens newsletter (2,000-fold) | yes |
| Eggs hatch in 3 to 5 days; chrysalis 8 to 15 days | Monarch Joint Venture, "Life Cycle" | Monarch Watch, "Biology" | yes |
| Caterpillars digest leaf cell contents; much cell wall passes in frass | Barbehenn, Oecologia 89 (1992) 229 | Chapman, The Insects 5e ch. 3 | yes |
| Insects store energy as glycogen and fat | Arrese and Soulages, Annu Rev Entomol 55 (2010) 207 | Chapman, The Insects 5e ch. 6 | yes |
| Decomposers break down droppings and dead leaves and release CO2 | OpenStax Biology 2e 46.3 | OpenStax Concepts of Biology 20.2 | yes |
| Daylight hours at 41.6 N (central Iowa) | NOAA Solar Calculator | US Naval Observatory sun tables | yes |
| First fall frost in central Iowa usually early October | Iowa Environmental Mesonet frost climatology | NOAA NCEI 1991 to 2020 normals (Des Moines) | yes |
| MS-LS1-6 and MS-LS1-7 wording and boundaries | nextgenscience.org | NSTA NGSS hub | yes |
Backed twice: 23. Cut: a seeds-per-pod count; a percent of cellulose a caterpillar digests (no direct measure found;
kept as "much ... passes through"); "about 400 water per CO2" (sources range 200 to 600, so "several hundred").
Number checks (Python 3, 2026-11-07): daylight from the solar formula with refraction at 41.6 N; the whole model run in
whole crates. Seasons (shoots, pods): defaults 1, 1 (42 percent burned); default plan Open 3, 3 (9 leaves wilted);
always Closed dies week 8; starch only Open 4, 0; starch only Half 2, 0; leaves only 0, 0 (30 leaves wilted); pods only 2,
9; roots only dies week 13; even 25s Open 4, 5; strong plan 8, 8; strong but Open in drought 5, 6; strong but Closed in
drought 5, 5 (5 leaves starved); strong with no roots 2, 3; leaves to week 15 5, 2. Random week-by-week settings: 0 of
30,000 meet the challenge. 315 sensible two-phase plans each: challenge met with Half in the drought 243, Open 57 (only
with big roots), Closed 24. Burned share 27 to 44 percent in surviving plans. Carbon books: made minus burned equals
crates into leaves, roots, starch and pods in every run (152 = 62 + 48 + 34 + 8 for defaults). Explain pairs: a fair
sunny and cloudy pair exists in both worked seasons (weeks 3 and 4) and in 87 percent of 4,900 random seasons; the rest
use the night sentence alone. Predicts: 18 O minus 6 = 12 atoms = 6 O2; 4 sugars, 3 links; 24 + 12 = 36 atoms in, 18 +
18 out. Contrast ratios computed with the WCAG formula.

## Done when
1. Focus and one idea: Next week plays day, night and chutes on the factory; the strip shows CO2 in and O2 out equal to
   6 times sugar made and the burned line 6 times burned; the plant view changes with the crates spent.
2. Defaults run to frost give 1 shoot and 1 pod; the strong plan gives 8 and 8; always Closed ends in week 8 with
   outcome 1; each of the five outcomes looks different.
3. Season report: carbon kept equals leaves + roots + starch + pods; burned percent matches the ledger.
4. Follow: P1, P2, P3 mark only 6, 3 and "36, the same atoms"; the counter appears after the pick; atoms in equal atoms
   out in every build; the tagged carbon can only enter the sugar in Build sugar.
5. All four paths complete and mark; the cellulose path goes through frass and soil; the starch path digests then
   builds glycogen or burns.
6. Wrong elements bounce; `Fill the rest` appears only after the first O2 and the tagged carbon are placed by hand.
7. Explain: each question's right claim, evidence and reasoning fill from the student's own ledger numbers; a wrong
   pick shows its reason and marks "fixed"; the sample season works before week 12.
8. A tap on any control during a week's animation finishes it at once; mode switches keep the season.
9. At 1366x768 the stage, forecast, Stomata, the plan rows and Next week sit above the fold; at 680x425 stage and
   panel stay side by side with the Plant / Factory toggle and the Ledger button.
10. Voice: how lines once each; beat and result lines whole before the next prompt; no line names a disabled control.
11. No people in any art; no network requests; no console errors; "Your season stays on this device." shows.

## Open questions
None.

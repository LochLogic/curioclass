# Tree of Life

## One idea
Common ancestry is a claim you can check four independent ways, and they agree: walk a real dated tree of sixteen
living things, switch the lens between Time (when the branches split), Molecules (how many cytochrome c amino
acids differ from ours), Anatomy (the same forelimb bones in an arm, a flipper and a wing) and Fossils (dated
in-between forms), crack the case of the whale's closest living relative, then make a new fork yourself by letting
selection pull two finch islands apart.

## Not like
- bug-hunt (sci 8): an arcade where you are the predator and color shifts in one population. Here selection is a
  model you set up and measure (survival curve, beak share over 10 mm), and the main work is reading evidence for
  ancestry across a whole tree.
- gene-pool (sci 8, genetics family): breeding fantasy creatures. Here only real species and real data.
- biome-atlas (sci 12): where living things are on Earth. Here how they are related through time.
- star-life-story (sci 9, timeline): a timeline of one star. Here a branching tree, not a line.
- punnett-predictor and protein-factory (same group): how traits pass on and how DNA codes proteins. Here what
  millions of generations of that leave behind.
- which-model-wins and sample-machine (math): statistics on fixed data. Here statistics on a living population
  that changes because of the statistic.

## Who and how
Grade 9, science (Life Science module Evolution: "Natural selection and evidence for evolution"). Driver: students
on laptops, or the teacher on a projector for the whale case. 20 to 40 minutes. Standards: HS-LS4-1 (multiple lines
of evidence for common ancestry), HS-LS4-2 (four factors: potential to increase, heritable variation, competition
for limited resources, better fit survives and reproduces), HS-LS4-3 (an advantageous trait rises in proportion),
HS-LS4-4 (selection leads to adaptation), HS-LS4-5 (environmental change can lead to new species or extinction).
Topic line: evidence for evolution and natural selection.
9-12 dark theme. Header: title, `.seg` modes **Tree**, **Whale case**, **Make a fork**, kit buttons `motion`,
`sound`, `read`.

## Screens and modes
**Tree** (opens first). Stage: a dated tree drawn in code, time axis along the bottom in millions of years (Ma) on a
log-like scale with ticks 1, 10, 100, 1,000, 1,500 (labeled; real ages printed on every node, so the squeeze never
hides a number). Sixteen tips on the right, each with a painted round portrait and a common name. Panel: **Lens**
`.seg` **Time**, **Molecules**, **Anatomy**, **Fossils**, a detail card, `hint`, `tip`.
Focus: the tree, the biggest, central thing in every lens (at least 60 percent of the stage); the Molecules scatter
and the Anatomy limbs open in the detail area under or beside it, never covering it.
- Time: click any node to see "Last common ancestor of human and dog: about 89 million years ago" (node ages
  below). Click two tips to have their meeting node light up.
- Molecules: each tip shows a bar and number: cytochrome c amino acids that differ from human (out of 104).
  **Sort by difference** reorders the tips list in the panel (the tree itself never redraws). A scatter (graphing.js)
  plots split time from humans (x) against differences (y): the points climb together, not exactly in a line.
- Anatomy: five forelimbs (human arm, horse leg, gray whale flipper, chicken wing, bullfrog front leg) drawn in
  code side by side (a bone diagram, kept in code because every bone is a clickable, recolored shape), each under the
  small painted portrait of its animal, bones colored by name with a key (upper arm, forearm pair, wrist, hand); click a bone to highlight it
  in all five. Text: "same bones, different jobs".
- Fossils: fossils pinned to the branches where they sit (a small painted fossil thumbnail on the branch), each
  opening a card with its painted fossil, age and what it shows (list in Content).
**Which lens agrees?** button (any lens): asks "Is a whale closer to a hippo or to a dog?" and makes the student check
each lens in turn; each lens adds a tick to a small four-row table (lens, says). No score.

**Whale case** (a guided case, five clue cards in order, Next and Back; each card has a painted picture: 1
tol-whale-hip, 2 the whale and hippo portraits, 3 the three whale fossils, 4 tol-ankle, 5 the whale and hippo
portraits joined by the tree's branch). Focus: the clue card, large, with the tree's whale branches lit beside it;
on the last card the tree takes the center for the drop. 1 Anatomy: whales have a flipper with arm bones and a tiny
hip bone. 2 Time: the tree says whale and hippo split about 53 Ma. 3 Fossils: Pakicetus (about 50
Ma, land animal with a whale ear bone), Ambulocetus (about 49 Ma), Dorudon (about 40 Ma, fully at sea with small hind
legs) placed on the branch. 4 The ankle: early whale fossils have the double-pulley ankle bone found only in the
group with hippos, pigs and deer (Gingerich 2001, Thewissen 2001). 5 DNA studies agree. Last card: the student
drags the whale tip to the branch it belongs on (hippo, dog or horse); a wrong drop shows which clue disagrees.

**Make a fork** (the selection model). Two islands side by side, each headed by its painted island (tol-island-a,
tol-island-b, a band across the top of its panel) and its painted finch cutout (tol-finch-deep on A, tol-finch-slim
on B), then a dot strip of 200 finches by beak depth (mm, code) with a histogram, a seed bar showing the island's best beak depth (θ), and a survivors count. Controls:
**Next generation**, **Run 10**, **Reset**; **Gene flow** slider 0 to 20 percent of birds swapping islands each
generation (step 1, default 0); **Drought** buttons, one per island (moves that island's best beak 2 mm deeper);
**Seed** field (number, default 1) so a class can share a run. A chart under the islands: mean beak depth for
each island by generation, with a band where they differ by more than 2 mm. When they first differ by more than 2
mm a fork appears on a small tree drawing: "Model rule: we call it a fork when the island means differ by more than
2 mm." Readouts per island: mean, survivors last generation, share of beaks over 10 mm.
Focus: the two dot strips and their histograms, side by side and central; the painted island bands are headers, and
the means chart sits under them.

## Content
Tips, NCBI taxon id, cytochrome c difference from human: human 9606 (0, the reference), chimpanzee 9598 (0), rhesus
macaque 9544 (1), house mouse 10090 (9), dog 9615 (11), horse 9796 (12), gray whale 9764 (10), hippopotamus 9833
(no sequence: shown as "not sequenced in UniProt", a teaching point about real data gaps), red kangaroo 9317 (10),
chicken 9031 (13), eastern diamondback rattlesnake 8729 (15), American bullfrog 8400 (18), skipjack tuna 8226 (20),
fruit fly 7227 (23), baker's yeast 4932 (37), bread wheat 4565 (35).
Node ages (Ma, TimeTree adjusted): human and chimp 6.45; plus rhesus 28.90; primates and mouse 83.51; dog and horse
73.20; whale and hippo 53.01; (dog, horse) and (whale, hippo) 75.95; those two big groups 89.48; placentals and
kangaroo 159.16; mammals and reptiles (chicken, rattlesnake) 318.82; chicken and rattlesnake 280.68; amniotes and
bullfrog 352.08; four-limbed animals and tuna 435.13; vertebrates and fruit fly 692.17; animals and yeast 1,164.30;
fungi and animals with wheat 1,515.83.
Molecules pattern lines: "chimp 0, rhesus 1: close relatives, nearly the same protein" / "kangaroo 10 and dog 11:
kangaroo split from us earlier but differs less. Molecules change at a rough, not exact, rate." / "yeast 37 of 104:
we still share 67 amino acids with a fungus."
Fossils: Tiktaalik about 375 Ma (fish with wrist bones and a neck, on the tetrapod branch); Archaeopteryx about 150
Ma (feathers, teeth and a bony tail, on the chicken branch); Pakicetus about 50 Ma, Ambulocetus about 49 Ma, Dorudon
about 40 Ma (whale branch); Sahelanthropus about 7 Ma (near the human and chimp split); Jebel Irhoud Homo sapiens
about 315,000 years (tip of the human branch).
Finch model (Make a fork, labeled "model" on screen; numbers from Python, Curio Class 2026-10-27):
- Start: each island 200 birds, beak depth Normal(mean 9.0, sd 0.7). Island A best beak θA = 11 (big hard seeds),
  island B θB = 8 (small soft seeds).
- Survival chance exp(-(z - θ)^2 / (2 x 1.5^2)). Survivors pair at random; 200 chicks each with beak = average of
  its parents + Normal(0, 0.5). (Potential to increase: survivors always refill to 200; variation: the spread;
  competition: only some survive; better fit: survival curve. The four HS-LS4-2 factors are named on screen.)
- Gene flow: that percent of chicks swap islands before the next selection.
- Extinction: an island with under 10 survivors has no chicks; it shows "Extinct on this island".
- Expected behavior (the model itself, simulated bird by bird, 100 to 400 seeded runs each): island A survivors
  about 87 of 200 in generation 1, rising to about 170 by generation 8; island B about 155 at once. Means first differ
  by more than 2 mm at generation 6 or 7 in 4 runs of 5 (5 to 9 in nearly all); final means near 11.0 and 8.0. Gene
  flow (steady gap after 40 generations, fork generation): 2 percent 2.8 mm, about 7 to 8; 4 percent 2.6 mm, about
  9; 6 percent 2.4 mm, about 11; 8 percent 2.2 mm, about 14; 10 percent 2.0 mm, usually 15 to 30 (the gap hovers at
  the line); 12 percent 1.8 mm, about half the runs never fork in 60 generations; 15 percent 1.5 mm and 20 percent
  1.1 mm, never. Migrants land on the wrong island's seeds and mostly die before breeding, so it takes far more gene
  flow to stop a fork than an averaged formula suggests. Drought on an adapted island: about 76 survivors, the island
  recovers. Two drought presses before the next generation (a 4 mm shift at once): about 7 survivors, extinct in
  about 4 runs of 5. One drought per generation for two generations: extinct in about 1 run in 4; for three
  generations: always extinct.
Hints: Tree "<b>Tree.</b> Pick a lens, then click a node or two tips. Do the lenses tell the same story?" / Whale
"<b>Whale case.</b> Read each clue, then place the whale on its branch." / Fork "<b>Make a fork.</b> Press Next
generation and watch the beak means. Then add gene flow and try again."
Tips: "A tree shows relatives, not a ladder: no living species is the ancestor of another." / "Evolution acts on
populations, not on one bird." / "A drought does not make beaks grow. It changes which birds leave chicks."
Model limits line (Fork): "Real finches have many genes for beak size, mate choice and changing seed crops; this
model has one number and one best beak per island."

## Interactions in detail
- Tree nodes and tips are buttons in tab order (tips top to bottom, then nodes from the root); arrow keys walk the
  tree. Selected node: accent ring plus bold age label.
- Log time axis: positions use log10(age + 1); the axis note says "squeezed scale: older is farther left, with
  more squeezing" and every node prints its age.
- Whale drop: drag or keyboard (pick the whale, then pick a branch button). Wrong drop: "The ankle clue says
  otherwise" (or the clue that disagrees); never a fail sound.
- Fork: Next generation animates selection (unfit dots fade, 600 ms) then breeding (new strip, 600 ms); Motion off:
  instant. Run 10 runs ten generations at 4 per second (2.5 s). While it runs every control stays live: Reset stops
  it at once; Gene flow and Drought apply from the next generation; a second Run 10 or Next generation adds its
  generations at once after the current one. The dot strip shows each generation's result as soon as it is computed;
  the fade only decorates it. The seeded generator is probability.js `Rand(seed)`, so the
  same seed gives the same run on every computer.
- Gene flow and drought change the next generation only. Reset keeps the slider and seed.
- Mode change: `V.hush()`; Tree selection and Fork run kept per mode.

## Look
Accent `--brand #b8ead3` (celadon, a pale museum green), `--brand-ink #10161f`. Stage `#0f1517`, branches
`#8fa3a8` (6.88:1 on `#10171a`), time axis ink. Island A dots warm `#ffb36b`, island B cool `#7cc4ff`, also told
apart by shape (circles and squares) and labels; the painted island bands echo them (A dry and golden, B green and
blue). Bone colors with a text key (never color alone).
Contrast (computed): brand on --panel 12.98:1, on --sec-bg 12.30:1; brand-ink on brand 13.62:1. Nearest 9-12
accent #efe6d2 (dE 21); in this group punnett-predictor's #a3ffaf is the closest (dE 33).

## Art
Local FLUX (`scripts/localart.py`), no people. 29 images. House style for all: a natural history museum painting,
soft studio light, true colors, no lettering.
- Tip portraits (one shared prompt: "a natural history portrait, one living thing centered on a plain dark slate
  background, soft studio light"; 1:1; cutout no; people no; round tip portraits at 44 px, 96 px in the detail card,
  and the Anatomy limb headers): tol-chimp (an adult chimpanzee, head and shoulders, calm, facing slightly left),
  tol-rhesus (a rhesus macaque sitting, face toward the viewer), tol-mouse (a brown house mouse on all fours, side
  view), tol-dog (a mixed breed dog sitting, three-quarter view), tol-horse (a bay horse, head and neck, side view),
  tol-whale (a gray whale surfacing, mottled gray skin, side view), tol-hippo (a hippopotamus standing in shallow
  water, three-quarter view), tol-kangaroo (a red kangaroo standing upright, side view), tol-chicken (a brown hen
  standing, side view), tol-rattlesnake (an eastern diamondback rattlesnake coiled and resting, pattern clear),
  tol-bullfrog (an American bullfrog sitting, three-quarter view), tol-tuna (a skipjack tuna, side view, striped
  belly), tol-fly (a fruit fly, red eyes, macro side view), tol-yeast (budding yeast cells under a microscope, round
  cells, some with small buds), tol-wheat (a single ripe bread wheat ear on its stem), tol-human-footprint (a single
  bare human footprint pressed into smooth wet sand, top view; stands for the human tip, so no person is shown).
- Fossil kit (one shared prompt: "a museum fossil specimen in pale gray-brown rock, top lit, on a plain dark slate
  background"; 4:3; cutout no; people no; Fossils lens cards at 240 px and branch thumbnails at 40 px; the three
  whales also on clue card 3): tol-tiktaalik (a flat-headed fossil fish with a neck and sturdy front fins with wrist
  bones), tol-archaeopteryx (a crow-sized fossil bird with clear feather impressions on its wings, a long bony tail and
  small teeth), tol-pakicetus (a long-snouted fossil skull of a wolf-sized four-legged early whale relative),
  tol-ambulocetus (a fossil skeleton of a crocodile-shaped early whale with four strong legs and big hind feet),
  tol-dorudon (a long fossil skeleton of an early whale with a sleek body, flippers and tiny hind legs),
  tol-sahelanthropus (a dark brown fossil skull with a small braincase and a heavy brow ridge, lying on rock),
  tol-jebel-irhoud (pale fossil skull pieces with a flat face and a long low braincase, lying on rock).
- tol-whale-hip: a small curved whale hip bone lying on a dark museum cloth beside a long whale rib for scale,
  top view; 4:3; cutout no; people no; clue card 1.
- tol-ankle: a single fossil ankle bone with a pulley-shaped groove at each end, three-quarter view, on a dark museum
  cloth; 4:3; cutout no; people no; clue card 4.
- tol-island-a: a dry rocky volcanic island under hard sun, black lava rock, low cactus and thorny scrub with hard
  dark seed pods on the ground, wide view; 4:1; cutout no; people no; the band across the top of island A's panel.
- tol-island-b: a green damp volcanic island, soft grasses and leafy shrubs heavy with tiny pale seeds, misty hills,
  wide view; 4:1; cutout no; people no; the band across the top of island B's panel.
- Finch kit (one shared prompt: "a single dark brown ground finch perched on a twig, side view, on a plain green
  background"; 1:1; cutout yes; people no; 64 px beside each island's name, same size): tol-finch-deep (a thick deep
  crushing beak), tol-finch-slim (a small slender pointed beak).
Drawn in code: the tree, time axis, node ages, bars, scatter, the five forelimb bone diagrams, the lens table, dot
strips, histograms, seed bars, means chart, the small fork tree, preview.svg.

## Voice
Bank `clear-teacher` (Iapetus), restyled: "Say clearly and kindly, like a patient museum educator at a fossil hall."
Changed from `knowing-guide`, which spectrum-explorer (a `neighbors.py` explorer neighbor) also uses; clear-teacher
is used nearby only by hot-meets-cold, which is not on this tool's list. Uses `Curio.voice`, scope = mode.
- welcomeTree (how; Tree entered; stale once a node or tip is clicked): "Welcome to Tree of Life. Pick a lens at the
  top of the panel, then click a branch point or two living things."
- welcomeWhale (how; Whale case entered; stale once Next is pressed): "Whale case. Read the clue, then press Next.
  On the last card, drag the whale to its branch."
- dropHow (how; last clue card reached; stale once the whale is dropped): "Drag the whale onto the hippo, dog or
  horse branch. Or press the whale, then a branch button."
- welcomeFork (how; Make a fork entered; stale once a generation runs): "Make a fork. Press Next generation and watch
  the two islands' beaks."
- lensMolecules (how; first Molecules lens; stale on a lens change): "Each number counts the cytochrome c amino acids
  that differ from ours."
- lensAnatomy (how; first Anatomy lens; stale once a bone is clicked): "Click a bone to find it in every limb."
- whalePlaced (event; correct drop; stale on Back): "The whale goes beside the hippo. Every clue agrees."
- whaleWrong (event; each wrong drop; stale on the next drop): "One clue disagrees. Look at the highlighted card,
  then drag the whale again."
- fork (event; the first time the means split by 2 mm in a run; stale on Reset): "The islands have forked. The beak
  means now differ by more than two millimeters."
- extinct (event; each extinction; stale on Reset): "Too few birds survived on this island to raise chicks."
- flowHint (how; first gene flow of 15 percent or more; stale on the next slider move): "With this much gene flow,
  the islands keep mixing back together."

## Family engine
none. Uses `kit/probability.js` (from medical-test-paradox: `Rand(seed)` for all finch randomness, `Tally` for the
histograms) and `kit/graphing.js` (scatter in Molecules, beak means chart).

## Sources
- Divergence times: Kumar, S. et al. (2022), "TimeTree 5", Molecular Biology and Evolution 39(8) msac174;
  pairwise adjusted times from https://timetree.org (queried 2026-10-27 by NCBI taxon id).
- Cytochrome c sequences: UniProt (accessed 2026-10-27): human P99999, chimp P99998, rhesus P00002, mouse P62897,
  gray whale P68100, red kangaroo P00014, dog P00011, horse P00004, chicken P67881, rattlesnake P68517, bullfrog
  P00024, skipjack tuna P00025, fruit fly P84029, wheat P00068, yeast P00044. Differences counted in Python
  (initiator methionine removed, global alignment, mismatches at aligned positions; tuna also has one gap).
- Tiktaalik: Daeschler, Shubin and Jenkins (2006), Nature 440:757-763. Jebel Irhoud: Hublin et al. (2017), Nature
  546:289-292. Sahelanthropus: Brunet et al. (2002), Nature 418:145-151.
- Whale origins and the ankle bone: Gingerich et al. (2001), Science 293:2239-2242; Thewissen et al. (2001), Nature
  413:277-281. Pakicetus, Ambulocetus, Dorudon ages: Smithsonian National Museum of Natural History, "Whale
  evolution" (verify checks the page).
- Archaeopteryx about 150 Ma, homologous limbs, evidence for evolution: OpenStax Biology 2e, ch. 18 (CC BY 4.0),
  https://openstax.org/books/biology-2e/pages/18-1-understanding-evolution
- Finch beak depth and drought selection (qualitative only): Grant, P. R. and Grant, B. R. (2002), Science
  296:707-711. All finch numbers are model values.
- NGSS HS-LS4 evidence statements: https://www.nextgenscience.org (four factors in HS-LS4-2).
- Checks run in Python (Curio Class, 2026-10-29): node ages nest correctly (6.45 < 28.90 < 83.51 < 89.48; 73.20 and
  53.01 < 75.95 < 89.48; 280.68 < 318.82; each older node larger); 104 - 37 = 67 shared with yeast; kangaroo 10 and
  dog 11 against splits of 159.16 and 89.48 Ma. The finch model run bird by bird with numpy (200 seeds no gene flow,
  100 seeds per gene flow level, 400 per drought case): fork generation 6 (79 runs), 7 (79), 8 (26), 5 (9), other
  (7); gen 1 survivors 87.4, gen 8 171.2; steady gaps 2.78, 2.58, 2.37, 2.17, 1.97, 1.79, 1.51, 1.08 mm at 2, 4,
  6, 8, 10, 12, 15, 20 percent; one drought 76 survivors, double press 7.4 survivors and 78 percent extinct. These
  replaced the old averaged-model numbers (fork never at 4 percent, gap 1.95 mm; drought 87 and 9 survivors), which
  the bird-by-bird model the tool runs does not reproduce.

## Done when
1. Tree, Time lens: clicking whale then hippo lights the 53.01 Ma node; human and dog lights 89.48.
2. Molecules lens shows the sixteen numbers above, hippo as "not sequenced"; the scatter has fifteen points.
3. Anatomy lens: clicking the forearm in one limb highlights it in all five.
4. Whale case: dropping the whale on the dog branch names a disagreeing clue; on the hippo branch it completes.
5. Make a fork, seed 1, no gene flow: the fork appears between generations 5 and 9 and island A survivors climb from
   about 87 toward 170.
6. Gene flow 20 percent: after 40 generations the means stay about 1.1 mm apart and no fork shows; at 2 percent the
   fork still comes, a little later.
7. Pressing Drought twice on one island before Next generation usually ends in "Extinct on this island"; one press
   leaves about 76 survivors and the island recovers.
8. Focus: at 1366x768 and 680x425 the tree is the largest thing in Tree, the clue card in Whale case, and the two
   dot strips in Make a fork.
9. A tap while anything plays: during Run 10, Reset stops it in the same frame and a Drought press shows on the seed
   bar at once.
10. Everything works by keyboard; the main controls are visible at 1366x768 and 680x425; tree readable at 375 wide
    (scrolls inside its frame).
11. Each how-to line speaks once in five repeated actions and never names a control that is not on screen; the
    fork line speaks once per run.
12. All 29 images load and none shows a person (the human tip is a footprint); no network, no em dashes.

## Open questions
- [tree-of-life] HS-LS4-2 and LS4-3 are carried by the finch model only (the tree carries LS4-1). Enough, or should
  Make a fork add a second trait (for example, wing length) to show variation in more than one trait?
- [tree-of-life] Hippo cytochrome c is not in UniProt, so its Molecules bar reads "not sequenced". Keep the gap as
  a real-data lesson, or swap the hippo for a species with a sequence (then the whale case loses its partner)?
- [tree-of-life] The human tip is now a painted footprint, and the Fossils lens shows two painted fossil skulls
  (Sahelanthropus, Jebel Irhoud) from local FLUX as objects, not people. OK, or send the skulls to Cory's review too?
- [tree-of-life] Voice moved from knowing-guide to clear-teacher (restyled as a museum educator) because
  spectrum-explorer uses knowing-guide. OK?

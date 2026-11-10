# Shrink Ray

## One idea
In Dr. Ines's workshop (Dr. Ines is made up, labeled "illustration") a ray on a stand multiplies whatever it hits by the number on its dial, and before each shot the child calls the result bigger, smaller or the same without multiplying (a dial of 5/6 on a 7-unit picture: smaller; 1 1/2: bigger; 7/7: the same), then fires and sees it, while a tally collects the rule the child is forming; area rounds scale a 1-unit-square photo, width by 2/3 and height by 3/4, and the child tiles the new rectangle with 1/3 by 1/4 tiles, finds 6 tiles that each cover 1/12 of the square, and writes 2/3 x 3/4 = 6/12; larger cases use mixed numbers; job rounds come from the neighborhood (a mural plan scaled by 1 1/2, a garden bed made 3/4 of its old size, a recipe card cut to 2/3) and each is a product of fractions or mixed numbers in context; at the end the child's tally reads: times less than 1 shrinks, times more than 1 grows, times 1 stays, so a fifth grader learns to multiply a fraction or whole number by a fraction, to find areas of rectangles with fractional sides by tiling, to see multiplication as scaling, and to solve real-world problems with products of fractions and mixed numbers.

## Not like
- how-many-fit (6, concept): dividing fractions. Here multiplying them.
- recipe-scaler (4, spec): a whole number times a fraction. Here fraction times fraction, as scaling.
- blueprint-studio (7, concept): scale drawings. Here the meaning of multiplying by a fraction.
- camp-cook-share-out (5, spec): fractions as division. Here fractions as scaling.

## Who and how
- Grade 5, Math, module "Multiplying Fractions". Standards: 5.NF.4 (apply and extend previous understandings of multiplication to multiply a fraction or whole number by a fraction: a. interpret the product (a/b) x q as a parts of a partition of q into b equal parts; b. find the area of a rectangle with fractional side lengths by tiling it with unit squares of the appropriate unit fraction side lengths, and show that the area is the same as would be found by multiplying the side lengths), 5.NF.5 (interpret multiplication as scaling (resizing): a. comparing the size of a product to the size of one factor on the basis of the size of the other factor, without performing the indicated multiplication; b. explaining why multiplying a given number by a fraction greater than 1 results in a product greater than the given number, why multiplying by a fraction less than 1 results in a smaller product, and relating the principle of fraction equivalence a/b = (n x a)/(n x b) to the effect of multiplying a/b by 1), 5.NF.6 (solve real world problems involving multiplication of fractions and mixed numbers).
- Format: simulator. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Ten predict rounds, six area rounds (two with mixed numbers), six neighborhood jobs, the rule tally. Extra: Beat the ray (the class predicts sizes on the projector). tool.json `modes: ["Workshop", "Beat the ray"]`, `minutes: "20-30"`, `grades_label: "Grade 5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 5.NF.4 | Tile the scaled rectangle; find a parts of q split into b | 6 tiles of 1/12; 2/3 x 3/4 = 6/12 | 2 |
| 5.NF.5 | Call bigger, smaller or same before firing | the picture resizing; the tally | 3 |
| 5.NF.6 | Solve neighborhood jobs | the mural, garden bed and recipe card | 4 |

## Screens and modes
Header (kit): title "Shrink Ray"; `Workshop`, `Beat the ray`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A bright workshop, a ray on a stand, a photo 1 unit square on the wall, a dial set to 3/4, and Dr. Ines in goggles. The welcome is queued (`welcomeAfter: true`): "Before you fire: will the photo come out bigger, smaller or the same? Tap your call." First hint: "Tap Bigger, Smaller or Same."

**Predict (focus: the target).** At 1366x768 the ray and target fill the left with the dial and tally right; at 680x425 the tally is a tab. Dials: 5/6, 1, 1 1/2, 7/7, 9/10, 4/3, 1/2, 3/3, 2 1/4, 99/100, each on a 7-unit picture. The child calls, fires, and the tally fills: "less than 1: smaller", "more than 1: bigger", "equal to 1: same".

**Area (5.NF.4).** The ray scales width by 2/3 and height by 3/4. The child drags 1/3 by 1/4 tiles onto the new rectangle: 6 fit, and 12 would cover the whole square, so the area is 6/12. The strip writes 2/3 x 3/4 = (2 x 3)/(3 x 4) = 6/12. Mixed rounds: 1 1/2 by 2/3 (1 whole).

**Parts of q.** "3/4 of 8 photos": the child splits 8 into 4 equal groups and takes 3 (6).

**Jobs.** Six requests: a mural plan 4 by 6 feet scaled by 1 1/2 (6 by 9); a garden bed 3/4 the old 8-foot length (6 feet); a recipe card cut to 2/3; and three more.

**The rule (the aha).** Dr. Ines: "Times a number less than one shrinks it. More than one grows it. And 7/7 is just 1 in a costume."

**The end.** The tally and job log. `Print` prints them.

**Beat the ray (extra).** The class predicts before each shot.

## Content
- Ten dials, six area rounds, six jobs with made-up neighbors (labeled "illustration" where pictured), all readable with `Read`.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The dial can be turned to any fraction from the set; the call must come before firing.
- Keyboard: Tab to the call buttons, the dial, Fire, tiles and the job box; Enter fires or places.
- With Motion off the ray's beam is skipped and the picture changes at once.

## Look
- Accent `--brand` #0e6670 lab teal (header, the ray, buttons); gold #f4c542 (the beam, the tile in hand); paper #ebf6f7; ink #04202a; muted #495a5d.
- Contrast (WCAG 2.1, computed): white on brand 6.66:1; brand on paper 6.04:1; ink on paper 15.31:1; muted on paper 6.56:1; ink on gold 10.37:1.
- Never color alone: calls show words; tally rows carry symbols and words.
- Different from this batch (clockmaker brass, campfire red, cart blue, garden moss).

## Art
- People (illustrated): Dr. Ines and three neighbors, labeled "illustration" (Gemini, `people: true`, 4; cutout yes).
- Local FLUX (`scripts/localart.py`): the workshop (1, 16:9), the ray (1, 1:1), three job pictures (3, 4:3).
- Drawn in code: the target picture at exact sizes, tiles, the dial and tally.
About 9 images.

## Voice
Two bank voices, each unique in this batch: `calm-professor` as Dr. Ines; `playful-friend` as the ray's voice and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.dial + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `call`: "Tap Bigger, Smaller or Same."
- how `fire`: "Tap Fire."
- how `tile`: "Drag tiles onto the new rectangle."
- how `job`: "Type the new size."
- event, whole, the rule.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: exact fraction scaling (with `Frac` as described in equation-golf's spec), the tiler, the tally, jobs.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Calls | Fire first | Fire stays off until a call is made. |
| Area | Type 6/12 | The tiles must cover the rectangle exactly first. |
| Jobs | Multiply whole numbers only | Each job checks the exact product. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `call`; `fire`.
2. `tile`.
3. `job`.
4. The rule (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 5.NF.4, 5.NF.5, 5.NF.6 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Multiplication as scaling, and "multiplying makes bigger" as a common belief | Common Core Standards Writing Team (2013), "Progressions for the CCSS, 3-5 Number and Operations, Fractions" | Greer (1992), "Multiplication and division as models of situations", Handbook of Research on Mathematics Teaching and Learning | yes |
| Tiling a rectangle with unit-fraction tiles shows fraction products | Common Core Standards Writing Team (2013), "Progressions for the CCSS, 3-5 Number and Operations, Fractions" | Siegler and others (2010), "Developing effective fractions instruction for kindergarten through 8th grade", IES Practice Guide | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s15, 2026-11-10): 2/3 x 3/4 = 6/12; 5/6 x 7 < 7, 1 1/2 x 7 = 10 1/2, 7/7 x 7 = 7, 9/10 x 7 = 6.3; 1 1/2 x 2/3 = 1; 3/4 of 8 is 6; 4 by 6 scaled by 1 1/2 is 6 by 9; 3/4 of 8 feet is 6 feet; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 ray, dial and tally; at 680x425 tally as a tab.
2. Six areas are tiled with unit-fraction tiles and match the product. (5.NF.4)
3. Ten calls are made before firing, and the tally states the scaling rule. (5.NF.5)
4. Six jobs are solved with fraction and mixed-number products. (5.NF.6)
5. `Read` reads every card; every control is 48 px or more.
6. Dr. Ines and the neighbors are labeled illustration.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: pictures change at once; no network requests.

## Open questions
- The idea card moves 5.NF.3 and 5.NF.7 out of this tool (default used: they are taught in camp-cook-share-out; this tool keeps 5.NF.4, 5.NF.5 and 5.NF.6).

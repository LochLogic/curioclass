# Fraction Trail

## One idea
On a hiking map a trail runs from the trailhead (0) to the lake (1), and a ranger, Ms. Kai (made up, labeled "illustration"), asks the child to split it into equal legs by dragging trail markers, so each leg is 1/b of the way, and then to place campsites at fractions like 3/4, with the label growing leg by leg (1/4, 2/4, 3/4, and 4/4 = 1 at the lake); the trail keeps going past the lake for 5/4 and 3/1; in equal-camp rounds two hikers camp at 1/2 and 2/4 and meet at the same spot, and the child finds more pairs (3/6, 4/8); in compare rounds the child places two campsites (3/8 and 3/4, 2/6 and 5/6) and picks >, = or <; in the different-trail round half of a long trail is farther than half of a short trail, and the ranger explains we can only compare fractions of the same whole; at the end a trail guide lists every campsite, so a third grader learns that a unit fraction 1/b is one of b equal parts, that a/b is a such parts, to place fractions on a number line, to see and make equivalent fractions, to write whole numbers as fractions, and to compare two fractions with the same numerator or the same denominator, knowing comparisons only work for the same whole.

## Not like
- pizza-party (1, spec): equal shares of food. Here fractions as places on a line.
- garden-grid (2, spec): shares of shapes. Here numbers.
- fraction-wall-duel (4, concept): comparing on a fraction wall. Here a trail.
- jump-line (2, spec): whole-number jumps, same family. Here fractional legs.

## Who and how
- Grade 3, Math, module "Fractions as Numbers". Standards: 3.NF.1 (understand a fraction 1/b as the quantity formed by 1 part when a whole is partitioned into b equal parts; understand a fraction a/b as the quantity formed by a parts of size 1/b), 3.NF.2 (understand a fraction as a number on the number line; represent fractions on a number line diagram), 3.NF.3 (explain equivalence of fractions in special cases, and compare fractions by reasoning about their size: equivalent fractions are the same point on a number line; generate simple equivalent fractions; express whole numbers as fractions; compare two fractions with the same numerator or the same denominator, recognizing that comparisons are valid only when the two fractions refer to the same whole, and record with >, =, or <).
- Format: map. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Denominators 2, 3, 4, 6 and 8, eight placing rounds, four past-the-lake rounds, four equal-camp rounds, six compare rounds, the different-trail round, the trail guide. Extra: Ranger list (a teacher list of campsite challenges). tool.json `modes: ["Trail", "Ranger list"]`, `minutes: "20-30"`, `grades_label: "Grade 3"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 3.NF.1, 3.NF.2 | Split the trail and place campsites | equal legs; labels growing | 2 |
| 3.NF.3 (equivalence, wholes) | Meet at 1/2 and 2/4; place 3/1 | hikers at one spot; 4/4 = 1 | 3 |
| 3.NF.3 (compare) | Place two camps and pick the sign; the different-trail round | two flags; the ranger's warning | 4 |

## Screens and modes
Header (kit): title "Fraction Trail"; `Trail`, `Ranger list`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A hiking map with a trail from the trailhead sign (0) to a blue lake (1), pine trees along the way, and Ms. Kai in a ranger hat. The welcome is queued (`welcomeAfter: true`): "Welcome to the trail! Split it into 4 equal legs. Drag a marker onto the trail." First hint: "Drag a marker onto the trail."

**Splitting (focus: the trail).** At 1366x768 the trail runs across the map with the campsite card below; at 680x425 the map zooms to the trail. Markers snap only at equal spacing for the chosen number of legs; a helper shows each leg's length matching. Each leg is labeled 1/4.

**Campsites.** "Put a campsite at 3/4." The child drags a tent; legs count aloud: one fourth, two fourths, three fourths. Past the lake: the trail continues around the shore for 5/4; a long day hike lands at 3/1 = 3.

**Equal camps (the aha).** Two hikers: one splits into halves and camps at 1/2; the other into fourths and camps at 2/4. They walk and meet at the same tent. "Same spot, two names!" The child finds 3/6 and 4/8 too.

**Compare.** Two flags: 3/8 and 3/4. The child places both and picks >, = or <. Same numerator: bigger legs go farther. Same denominator: more legs go farther.

**Different trails.** Half of the long ridge trail and half of the short pond trail. "Which is farther? The long one, but that's not fair to compare. Fractions compare only on the same trail."

**The end.** The trail guide with every campsite. `Print` prints it and a blank trail.

**Ranger list (extra).** A list of challenges for the class.

## Content
- One main trail and two side trails, denominators 2, 3, 4, 6 and 8, campsites to 3, all readable with `Read`. Hikers are safe and cheerful; no one gets lost.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Markers and tents can be moved until `Check`.
- Keyboard: Tab to markers, tents, flags and sign buttons; arrows move by one leg; Enter places.
- With Motion off hikers appear at their camps instead of walking.

## Look
- Accent `--brand` #1e6070 lake teal (header, the trail, buttons); gold #f4c542 (the marker in hand, a matched camp); paper #edf6f7; ink #07202a; muted #465a5f.
- Contrast (WCAG 2.1, computed): white on brand 7.09:1; brand on paper 6.46:1; ink on paper 15.31:1; muted on paper 6.62:1; ink on gold 10.34:1.
- Never color alone: tents carry their fraction labels.
- Different from this batch (cafeteria brick, garden green, mystery violet, terracotta brown).

## Art
- People (illustrated): Ms. Kai and two hikers, labeled "illustration" (Gemini, `people: true`, 3; cutout yes).
- Local FLUX (`scripts/localart.py`): the trail map (1, 16:9), the ridge and pond side trails (2, 16:9).
- Drawn in code: the number line along the trail, markers, tents, flags.
About 6 images.

## Voice
Two bank voices, each unique in this batch: `calm-professor` as Ms. Kai; `knowing-guide` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.denom + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `split`: "Drag a marker onto the trail."
- how `camp`: "Drag the tent to the campsite."
- how `compare`: "Place both flags, then tap the sign."
- event, whole, equal camps.
- event, whole, different trails.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
number-line (`kit/number-line.js`, as described in roller-coaster-rounding's spec and docs/families/number-line.md). Uses: `NumberLine` (0 to 1 and 0 to 3 windows) with `format` for fraction labels and `snap` set to 1/b, `nl.x` to place tents and hikers, `nl.mark` for campsites and flags, `nl.span` for legs, `nl.draggable` for markers and tents, `nl.zoom` past the lake. The map, tents and hikers are this tool's own SVG.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Split | Drop markers anywhere | Markers snap only at equal spacing. |
| Camp | Drag the tent until it sticks | The legs count aloud and the label must match. |
| Compare | Pick a sign at random | Both flags must be placed first; the line shows which is farther. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `split`.
2. `camp`.
3. Equal camps (whole), waits.
4. `compare`. Different trails (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 3.NF.1, 3.NF.2, 3.NF.3 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| The number line builds the idea of fractions as numbers | Common Core Standards Writing Team (2013), "Progressions for the CCSS, 3-5 Number and Operations, Fractions" | Siegler and others (2010), "Developing effective fractions instruction for kindergarten through 8th grade", IES Practice Guide | yes |
| Fractions compare only when they refer to the same whole | Common Core Standards Writing Team (2013), "Progressions for the CCSS, 3-5 Number and Operations, Fractions" | Siegler and others (2010), "Developing effective fractions instruction for kindergarten through 8th grade", IES Practice Guide | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad r10, 2026-11-10): 1/2 = 2/4 = 3/6 = 4/8; 3/8 < 3/4 and 2/6 < 5/6; 4/4 = 1, 5/4 > 1 and 3/1 = 3; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 map and card; at 680x425 zoomed trail.
2. Eight placing rounds split the trail and place a/b. (3.NF.1, 3.NF.2)
3. Equal camps and whole numbers as fractions are shown. (3.NF.3)
4. Six compares and the different-trail round are done. (3.NF.3)
5. `Read` reads every card; every control is 48 px or more.
6. Ms. Kai and the hikers are labeled illustration.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: hikers appear in place; no network requests.

## Open questions
None.

# Safety read: science-kindergarten (course finish), 2026-11-22

Kind: safety. Target: science-kindergarten. Scope: 64 day files (days 1 to 64; the lister also matched two student-page strip files, dot-strip and design-cycle-chart, which have no materials or Safety section) plus data/plans/science-kindergarten/materials.csv (149 rows). Read: each day's materials line, its Safety and set-up section, its Before class set-up, and the steps children do with their hands (days 11, 12, 33, 40, 44 to 49, 55, 59 in full; the rest by materials and Safety). Read only; nothing but this report was edited.

## What I studied

- docs/FOUNDATION.md section 5 (room assumptions): kindergarten has one shared device, hands-on work and its materials are part of the unit, and a teacher with nothing gets a path. Every fallback in this course (photographs, drawings, "you alone") fits that.
- NSTA, "Safety in Elementary Science" (https://static.nsta.org/pdfs/SafetyInElementaryScience.pdf, opened 2026-11-22): ages 4 to 6 need more safety instruction; every student task is supervised by an adult; elementary students should not handle heat sources or heated materials; projectile risks (rolling balls, rubber bands) call for impact-rated eye protection worn by everyone in the room; shared eyewear is cleaned and sanitized after each use; household materials (sand, salt, water) count as chemicals and need a Safety Data Sheet on file; wash hands with soap and water after chemical work; do and document a hazard assessment; check for allergies; choking hazards and sharps are named hazards.
- NSTA safety topic page (https://www.nsta.org/topics/safety, opened): points to the elementary safety paper, an eye protection FAQ, personal protective equipment and a family acknowledgment form.
- U.S. Consumer Product Safety Commission, small parts page (https://www.cpsc.gov/Business--Manufacturing/Business-Education/Business-Guidance/Small-Parts-for-Toys-and-Childrens-Products, opened): the small-parts rule is a cylinder test for products for children under 3; the page says nothing about ages 3 to 6, so "too big to mouth" here is a sound extra margin, not a legal line.
- Could not open: an ACS school safety page (empty on fetch), a D.C. health science-lab PDF (404), two NSTA safety URLs (404). No safety data sheet was opened for sand or potting soil; see "Could not settle". No sources.csv row is needed: the report states no fact about a real place, person or event.

## Verdict

Pass with fixes. The days are unusually careful (soft balls only, floor only, "you alone" for plants, lamp, water filling and litter bags, held-back fallbacks that never fake a trial), but the course has no course safety page (S5 is a door, so S5 is not met yet) and the sun-warmed-surface days have no stop rule for a surface that is too hot.

## Course safety page (RUBRIC-SCIENCE row S5)

S5 says a course safety page covers the room rules, and it is a door row. Answer: **no, the course does not have one.** docs/courses/science-kindergarten/frame.md (Safety bullet) promises "a one-page course safety sheet for the year (no tasting, no sniffing unknowns, hands washed after soil, sun and hot-surface rules, gloves for any pick-up)". No such file exists in courses/science-kindergarten/ (only the 13 section folders) and none is listed in data/plans/science-kindergarten.

Every day's own Safety and set-up section is present (all 64 days), and materials lists are per child, per group and per class on every day.

## Findings

Severity: H = fix before the course is called finished; M = fix in this pass; L = tidy when next edited.

| # | Sev | Day | Hazard | What the day says | The exact fix |
|---|---|---|---|---|---|
| 1 | H | course | No course safety page (S5 door) | Nothing; frame.md promises it | Add a one-page "Our science safety rules" sheet (teacher and family copy) at courses/science-kindergarten/ and list it in the plan. Content: "We do not taste or sniff anything in science. We touch only what the teacher has checked. We wash hands with soap and water after soil, sand, gloves or litter. We never look at the sun. Eye protection stays on for every roll and pull, and the teacher wears it too." Add the too-warm rule (finding 2) and the litter rule (finding 6). |
| 2 | H | 44 | Hot surface: a playground slide, possibly metal, in direct sun | Before class: "Touch both slides (or benches) yourself with the back of your hand and clear them." Safety: "You touch first. Children touch briefly with the back of a hand, for a count of three." | Add to Safety and Before class: "A metal slide in sun is not touched by children: use a plastic slide, a wooden bench or a painted wall. If a surface is too warm for the back of your hand at a count of three, no child touches it: move to a cooler pair or use the dated photographs." Day 12 already says "no touch on metal in sun" and "If unsafe, no child touches"; reuse that wording. |
| 3 | H | 45, 46, 48 | Contact time longer than the rule, and no too-warm stop rule | Body (45, 46): "Each child touches the four samples, about 8 seconds each." Safety: "briefly, back of the hand" (no count). Before class: you "touch every sample first and clear it", but nothing says what stops a sample being cleared | Change "about 8 seconds" to "a count of three" to match day 44, or state why 8 is safe. Add to Safety: "A sample too warm for your hand at a count of three is not cleared: shade it for five minutes or use the dated photograph. Dark rock in full sun is the likeliest." |
| 4 | H | 50, 51, 53, 54 | Same stop rule missing | "Children touch only cleared rocks, briefly, back of the hand." | Add the sentence from finding 3. On 53 and 54, which clear about 30 patches ahead, add: "Touch a patch again just before the children arrive if it has been in sun more than 10 minutes since you cleared it." |
| 5 | M | 45, 48 | Hand cleaning after sand and soil is weaker than elsewhere | 45: "Wipes after sand and soil." 48: "Wipes after soil." But 40, 53 and 54 say "wash hands after soil", and the materials row for soil says the same | NSTA asks for soap-and-water handwashing after handling chemicals, and a wipe does not remove soil. Change 45 and 48 to "Wash hands with soap and water after sand and soil (a wipe only if there is no sink); no hands to faces first." |
| 6 | M | 55, 59 (56) | Litter pick-up: needles, pet waste, wet items, glove removal | 55: "Collectors touch only dry paper or intact plastic you cleared; glass, sharp things, food and unknown containers stay put." Safety omits washing; the body has "Collectors wash at the two sinks, three at a time, 45 seconds each." | Add to the Safety line of 55 and 59: "Anything sharp, any needle or syringe, any pet waste, anything wet or sticky: nobody touches it or goes near it; tell the teacher, who reports it to the school office." Add "Collectors take gloves off by turning them inside out into the adult bag, then wash." Add "Wash hands after" to day 55's Safety line (day 59 has it). Add "grabbers point down, never swung" beside "Grabbers low". |
| 7 | M | 11, 12, 44, 45, 46, 48, 51, 55, 59 (outdoor days) | Stinging insects, plant and pollen allergies, sun and water | 11: "stay in sight, touch nothing unknown, never look at the sun". Only 44, 48 and 51 have a water break; no day mentions stings, hats or the nurse's allergy list | Add one line to each outdoor day's Safety: "The day before, check the spot for wasp or bee nests and ask the nurse for stinging-insect and plant allergies. Hats in strong sun. Water break after." Days 45, 46, 55 and 59 have no water break line. |
| 8 | M | 44 to 48, 53, 54 | Sand and soil source and Safety Data Sheet | materials.csv: sand "about $3 for the unit"; soil "no tasting or sniffing; wash hands after soil". Neither says where from | NSTA treats household materials as chemicals that need a Safety Data Sheet on file. Add to the sand row: "washed play sand sold for children, labeled low dust; keep it damp; keep its Safety Data Sheet and the purchase date". Add to the soil row: "bagged potting soil, never dug from the schoolyard; keep its Safety Data Sheet". Add to day 45 Before class: "Wet the sand lightly so it makes no dust." |
| 9 | M | 1 to 9, 20 to 30 (every rolling day) | Eye protection: no standard named, no sharing rule, no path for a child who cannot wear it, glasses wearers | "Everyone present wears fitted eye protection for every roll and the clean-up." Materials row: stock "unconfirmed" | Define it once in the safety sheet and in the materials row: "child-sized safety glasses or goggles marked Z87.1, wiped with a disinfectant wipe and dried between children, worn by you too". Add: "A child who wears glasses uses fit-over goggles; a child who cannot wear eye protection is the recorder and stays behind the line for the rolls." The room with none is already handled (photographs). |
| 10 | M | 47, 49, 50 | Lamp when there is no sun | 47: "No sun: you show one lamp shadow, labeled a demonstration." Safety: "Only you handle a lamp." | Name it: "an LED lamp that stays cool to touch, cord taped flat and out of the lane, plugged in and unplugged by you, put out of reach after." A bulb that heats would add a warm surface to a unit about warm surfaces and invite a touch. |
| 11 | L | 46 to 54, 27, 28 | "Too big to mouth" is not a measure | "Rocks too big to mouth", "ball too big to mouth" | Say how a teacher checks: "larger than a child's fist, with no part that fits in a toilet paper tube". |
| 12 | L | 49, 50, 51, 53, 54 | Scissors | "One cutter at a time in a group." Materials: "two blunt child-safe scissors" per group of five | Add "cut paper only; tips down; carry closed; a left-handed child gets a left-handed pair". The cardboard hard cuts are already made by you the day before, which is right. |
| 13 | L | 29, 30 | Wheeled toys | "a large toy car", "a large toy van"; "nothing small enough to mouth" | Add to the materials row: "no battery or lights, no loose wheels, checked the day before". |

## Controls that work (no change)

- Rolling days: soft ball or taped paper ball only, floor only, no throwing, one child at a time, retrieve only a stopped ball, ramps lowered after a bounce, string straight and never around a body, nobody walks backward, stop-the-lane rule on days 8 and 9, and a fallback that never pretends to be a trial.
- Plants (32, 33, 40, 41, 42): "You alone handle the pots", allergies checked first, no tasting or sniffing, wash after soil, spills wiped.
- Paper-only days (13 to 19, 31, 34 to 39, 42, 43, 52, 56, 58, 60 to 64) say so and keep the room clear.
- Day 25's door swing is teacher-only with hands clear of the edge.
- Day 57's bottle samples: clean, labels off, edges and small parts checked the day before.
- Nothing hot is handled: all warmth is sun-warmed, which is why findings 2 to 4 matter most.

## Could not settle

- No Safety Data Sheet was opened for play sand or bagged potting soil, so finding 8 says "keep its Safety Data Sheet" without quoting one. The lead can open the maker's sheet once the products are chosen.
- Whether every 5-year-old can be fitted with Z87.1-marked child-size eye protection is a supply question (unit plan field 8 already says stock is unconfirmed); it does not change the fix.

## Browser check

None. No page I opened refused automated reads.

## Fixes applied (2026-11-22)

- 1. H, no course safety page: applied. courses/science-kindergarten/safety.md written (about 870 words); DEFAULTS.md names it; sources.csv row SAF1 (this NSTA paper, checked 2026-11-22).
- 2. H, day 44 metal slide: applied. No metal in sun; the too-warm stop rule added.
- 3. H, days 45, 46, 48: applied. A count of three replaces 8 seconds; the too-warm stop rule added.
- 4. H, days 50, 51, 53, 54: applied. Stop rule added; days 53 and 54 retouch after 10 minutes.
- 5. M, hand washing on 45 and 48: applied. Soap and water, wipe only with no sink.
- 6. M, litter on 55 and 59: applied. Needles, pet waste, wet items, gloves off inside out, grabbers down, wash after.
- 7. M, outdoor days: applied. Each outdoor day points to the outdoor check on the safety page (nests, nurse list, hats, water break); water breaks added on 45, 46, 55, 59.
- 8. M, sand and soil: applied. materials.csv rows say washed play sand, bagged potting soil, keep the Safety Data Sheet; day 45 wets the sand.
- 9. M, eye protection: applied. Rating, cleaning, fit-over goggles and the recorder path on the safety page and materials row; eye protection added to days 45, 46, 48, 50, 53, 54 (materials and safety) and the unit 5 cost.
- 10. M, lamp: applied. Cool LED lamp, cord taped flat, run by the teacher (days 47, 49).
- 11. L, too big to mouth: applied. Defined on the safety page and in the toy rows.
- 12. L, scissors: applied. materials.csv row and safety page.
- 13. L, wheeled toys: applied. materials.csv rows.

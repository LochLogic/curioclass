# Safety read: science-grade-2 (course finish, stage 7)

Kind: safety. Target: science-grade-2, all 76 days. Date: 2026-11-22. Read-only except this report.

## Verdict

Pass with fixes. Every hands-on day has a Safety and set-up section with hazards and controls, goggles or eye protection are used consistently, and every day has a paper or picture path; but the course has no course safety page (rubric S5 is a door, so it fails until one is written), the outdoor surveys lack an adult-ratio and site-sweep line, and several household stand-ins and set-up steps are looser than the school guidance read below.

Counts: 0 stop-ship hazards; 6 high, 11 medium, 8 low findings.

## What I studied

Pages opened on 2026-11-22 (each fetched and read, not a search summary):

- https://www.nsta.org/blog/preschool-grade-2-scienceengineering-hands-activity-safety-protocols : a national science teachers' association page for preschool to grade 2. Taught me: hand washing before and after hands-on work, adequate adult supervision at a low ratio, nothing in mouths, no eating, a safety talk before each activity, wipe spills, check equipment, adapt for allergies, splash goggles for liquids and side-shield glasses for flying objects.
- https://www.nsta.org/eye-protection-and-safer-practices-faq : the same association's eye protection page. Taught me: everyone present wears it, including the teacher and visitors, at elementary level too; Z87 impact marking for solids and collisions, indirectly vented splash goggles (D3) for liquids, heat and dust; clean goggles after each use.
- https://www.cde.ca.gov/ci/pl/animalsplantsinclassrm.asp : a state education department page on plants and animals in class. Taught me: use sterilized potting soil, not outdoor soil; grocery seeds, not coated garden seeds; never eat unknown plants or seeds; check allergies to the plants studied; wash hands and clean surfaces after plant work; teach children to avoid wild hazards (poison ivy, stinging nettle, fungi) on outdoor looks.
- docs/FOUNDATION.md sections 5 and 7.3: the room assumptions (shared device, hands-on work always has a path for a teacher with nothing) and the safety agent's job.
- docs/RUBRIC-SCIENCE.md row S5 and docs/courses/science-grade-2/frame.md lines 75 to 84: S5 is a door; the frame promised a one-page course safety sheet for the year and the safety agent's read of unit 4's heating above all.
- data/plans/science-grade-2/materials.csv (243 rows) and every day's Safety and set-up section, materials line and hands-on steps (listed below), plus the five unit safety sheets and each day's "At home" swap lines.

Chemicals: the course names none (play sand, soil, tap water, ice, chocolate and egg displays sealed). No safety data sheet applies except sand dust (see Could not settle).

## Scope

Days listed with a script: 74 day files (d001 to d076) carry a Safety heading, plus two unit side files (dated-table-days-50-55.md, desert-and-shore-cards-day69.md) that are not days. Safety and set-up read in full for all 76 days. Materials and every hands-on step read in full for the 34 days with real objects, heat, sand, soil, plants, fan, blocks or the schoolyard: 2, 4, 7, 16, 17, 18, 20, 21, 27, 28, 29, 30, 32, 33, 34, 36, 39, 40, 41, 42, 43, 47, 49, 50, 52, 54, 55, 60, 61, 62, 63, 66, 70, 75. The rest are paper-only or paper-and-card days whose Safety line says so.

## Rubric S5: course safety page

No. There is no course safety page. Five unit sheets exist (units 3.1, 4.1, 5.1, 6.1, 7.1); units 1.1 to 2.3 (sand, soil, water, the fan, the schoolyard look) have no sheet, and nothing covers the year. S5 names "a course safety page covers the rules for the room" and the frame promised one. S5 fails until it is written.

## Findings

Severity: H = fix before the course is called finished; M = fix in the next edit of the day; L = small wording.

| # | Sev | Day | Hazard | What the day says | The exact fix |
|---|---|---|---|---|---|
| 1 | H | Course | No course safety page (S5 door) | Frame: "A one-page course safety sheet for the year"; none exists. Unit sheets only for 3.1, 4.1, 5.1, 6.1, 7.1 | Write courses/science-grade-2/safety-page.md, one page, with: eye protection on for sand, soil, water and fan days and for everyone in the room including the teacher; spills wiped at once; hands washed after sand, soil, plants and outdoor looks; nothing tasted; sealed things stay sealed; all heating, freezing and fan by an adult; allergy list checked with the nurse before day 7, 29, 39, 42, 43, 66, 70, 75; outdoor rules; a first-aid and spill reminder. Add it to the course page list and link it from each unit sheet |
| 2 | H | 4, 66, 70 | Outdoor look: supervision and site hazards | d66: "Four rules: stay on the path, stay in sight... an adult counts heads." Six groups of five in two spots with one teacher | Add to the Safety and set-up of d4, d66 and d70: "A second adult comes outdoors (an aide, a volunteer or a teacher from the next room); one adult at each spot. The day before, an adult walks both spots and clears or avoids broken glass, sharp objects, animal waste, standing water, wasp or ant nests and poison ivy or nettle. If any is found, use the photograph path." Also: "Sun, heat or cold: water bottles, hats, and move indoors if the ground is icy" |
| 3 | H | 16, 17, 18, 20 (materials.csv) | Soil source | materials.csv: "untreated soil (household stand-ins)", d20 "damp soil", d2 home swap "damp sand or soil"; unit 5 says "damp sterilized potting soil" | Make the course agree with unit 5 and the school guidance read: write "sterilized bagged potting soil or play sand, never soil dug from the yard" in materials.csv and in the Safety line of d16, d18, d20; the d2 home swap: "damp sand, or bagged potting soil, not soil from outside" |
| 4 | H | 43 | Cooked egg display kept in the room | d43 materials: "sealed cooked-egg display" passed by 30 children; cleanup: "The adult collects the sealed displays and discards them". Safety: "Nothing is eaten." No storage, no allergy line | Add to d43 Safety and set-up: "The egg display is a cooked egg double-sealed in a bag, kept cold until class, in the room no more than the lesson and discarded the same day unopened. Egg allergy: the teacher checks the nurse's list before the day; a child with an egg or milk allergy looks at the photographs only and handles no display." Same lines for d39 (chocolate and egg displays) and d42 (chocolate); d42 and d43 currently have no allergy line (only d39 materials.csv and unit sheet line 6) |
| 5 | H | 21 | Wind trial: dust, asthma, sweeping | Fan on low "for a slow count of sixty" over damp sand; "You sweep the sand into the lined bin" | Add to Safety and set-up: "A child with asthma or a dust allergy sits at the back or watches the fallback cards; the sand stays damp; if dust lifts, stop the fan and wipe. At clean-up wipe with a damp cloth and scoop the sand; never dry-sweep it." The fan's cord taped flat on the room wall side |
| 6 | H | 7, d29 home | Glass or cracked containers, cold contact | d7 home swap: "two closed jars, one with ice and one with water, held briefly". d7 children hold the ice cup 20 seconds with no mitt option (d29 has one) | d7 home swap: "two closed plastic containers, never glass". d7 Safety add: "A child who dislikes cold, or a child whose hands are sensitive, holds the cup with a mitt or cloth or looks at the pictures" |
| 7 | M | 18 | Stakes for the mat | d18: "fabric mat... staked across one tray"; no stake is named in materials | Materials and Safety: "Stakes are blunt craft sticks pushed in by the adult, or the mat is held with tape; no pins, no skewers; sticks counted back" |
| 8 | M | 27 (and 28 no-kit) | Household samples | d27: "passes six household pieces round"; d28: "a lamp on a stack of books" | d27 no-kit: "six household pieces that are new, blunt and not glass, not sharp metal, not latex; a wooden spoon, a metal spoon, a plastic lid, a cloth, a paper towel, a nonlatex band (never stretched)". d28 no-kit: "a flashlight or an LED lamp, never a bulb that gets hot; cord taped flat; never aimed at eyes" |
| 9 | M | 29 | Lukewarm water temperature | "sealed lukewarm cups... prepared and checked by an adult"; the at-home line says "never hot" | In the d29 Safety and materials: "Lukewarm means tap water that feels barely warm on the adult's wrist, never from a kettle or a hot tap" |
| 10 | M | 42 | Adult warm-water bath | "adult warm-water bath and splash goggles (cleared before children enter)"; unit 4 sheet line 3: "Only a grown-up does the warm water. We stay behind the line" | Name the control in the day: "warm tap water, not hot, in a sealed tub on a table out of reach, emptied and cleared before children enter; no kettle, no heater in the room." Fix the sheet so line 3 matches: "The grown-up does the warm water before class, away from us." Say where the adult heats chocolate and paper (d43 "heated paper": photographs only, and "no flame in the room" is already there; add that heating happens elsewhere and the items are cooled to room temperature before they enter) |
| 11 | M | 50, 52, 54, 55 | Hand washing after soil | d49: "Hands are washed straight after". d50 to d55: "hands are washed at the next washing, said aloud"; unit 5 sheet line 8 repeats it | The guidance read says wash after plant and soil work. For days when children touch soil or plant cups (d50, d52, d54, d55), wash in two waves as d17 does, or wipe with a damp cloth and wash before the next food or at the next break, said aloud, and name the time. Do not leave it open |
| 12 | M | 56, d49 no-kit | Mold | d56: "discards any mouldy cup" (UK spelling). Unit 5 sheet line 7 | Change to "moldy". Add: "The adult removes a moldy cup without opening it, in a sealed bag, wearing gloves, and washes hands; a child with a mold allergy or asthma leaves the area. Covers and cups from home are washed food tubs, so rinse them of any food residue first" |
| 13 | M | 60 | Hand lens | "Look aloud at the sock through a lens"; "Plastic lenses only" | Add: "Never aim the lens at the sun or a window light; look only at the sock on the table" |
| 14 | M | 18, 49, 75 | Plant allergies | d18, d75 "not eaten"; no allergy check for the plants named (radish, bean, grass, seedlings) | Add to d18, d49, d52, d54, d55 and d75 Safety: "The teacher checks the nurse's list for plant and pollen allergies before day 18; a child who reacts watches the pictures." This follows the plant allergy guidance read |
| 15 | M | 16, 18 (home swap) | Sunglasses in place of goggles | "No goggles: use sunglasses" (d16, d18); d17 correctly says "a grown-up pours while the child steps back" | Use the d17 wording in d16 and d18: "No goggles: a grown-up pours while the child steps back." Sunglasses are not rated eye protection |
| 16 | M | 66, 70 | Weather, tick and sting checks | "check clothing for insects in pairs"; d66 Safety: allergy path | Add: "An adult checks the nurse's list for stinging-insect allergies (and where an epinephrine pen is kept) before the walk; the adult carries the pen and the nurse's phone number; any child may use the photographs without saying why" |
| 17 | M | 33 | Block placed on a strip | "The adult then places each group's block in turn"; "equal large wooden blocks"; Safety: "Low supports sit over the tray; the adult places every block; fingers and feet stay clear" | Adequate. Add "children sit, feet back from the tray, no standing" so the placing step is the only moment a block is above the table, and name the block weight ("under 250 grams") |
| 18 | L | 2, 16, 17, 18 | Stacks of books holding trays | d16: "trays on the same two books"; "stack of two books and a stack of four books" | Say: "trays sit on the table, not the floor, books taped together so the stack cannot slide, and a spill cloth under the tray" |
| 19 | L | 30 | Foil edge | "dull-edged foil" | Say "foil with the edges folded over by an adult" |
| 20 | L | 36 | Pine, plastic, cotton samples | "sanded pine... rounded edges" | Fine; add "the adult checks each piece for a splinter or crack before class" |
| 21 | L | 39 | Allergy check wording | Safety: "Ask no child what is eaten at home." Unit 4 sheet line 6: "Tell a grown-up if you cannot be near an egg or milk" | Good that no child is asked. Change the sheet line to: "The grown-up already knows who uses the picture. Any child may use the picture." So no child has to say a medical fact in front of the class |
| 22 | L | 61, 62, 63 | Floor mat and string | d61 mat and walking model; d63 pipe cleaners | Tape the mat edge; name the pipe cleaner ends folded back and covered (already there); the d47 string safe line ("short, away from necks") should also appear on d40 and d61 where string appears |
| 23 | L | 7, 29 | Sealed cups leaking | "The adult checks the seals"; "wipe the condensation" | Add: "A child never carries a tray alone; the adult hands out and collects the trays" |
| 24 | L | 75 | Radish seedlings "untreated" | d75: "five matched pre-grown untreated... never eaten" | State the source: "grown from grocery or school-garden seed, not coated garden seed" |
| 25 | L | course | Eye protection names | The course uses "splash goggles", "fitted goggles", "impact eye protection" and "eye protection" | Add a line in the new safety page: "Splash goggles (indirectly vented, marked Z87 and D3) for sand, soil, water and the fan; impact glasses or goggles (marked Z87) for sticks, blocks and pieces; one pair per child, wiped with a damp cloth after each use" |

## Days where the Safety and set-up passed with no change

1, 3, 5, 6, 8 to 15, 19, 22 to 26, 31, 35, 37, 38, 40, 41, 44 to 46, 48, 51, 53, 57 to 59, 64, 65, 67 to 69, 71 to 74, 76 (paper, cards or indoor pencil work; or controls named and matched to the hazard; goggles, count-back, adult-only steps and a no-kit path present).

## Course-wide checks

- Eye protection: present and rated sensibly on every sand, soil, water, fan, press and block day. Mixed names (finding 25).
- Heat: none by children; all adult-only and before class (d42, d43); no flame anywhere. Needs the temperature limit (finding 10).
- Glass and sharp edges: ruled out in the six-sample trays and unfamiliar samples (d27, d28, d34, d36); a glass picture card replaces real glass (d28). Home swap glass jars fixed in finding 6.
- Allergies: handled in unit 4 materials and unit 3 (nonlatex); not stated on d42, d43 or the plant days (findings 4, 14).
- Electricity: the fan runs on d21 only, adult-only, guarded, low; cord and dust points in finding 5.
- Choking: stones and counters named "out of mouths" (d2, d17, d20); card seeds "large" (d61 to d63).
- Substitution: each hands-on day has a paper, picture or invented-record path; the stand-ins are mostly as safe or safer (see findings 3, 6, 8, 15 for the exceptions).
- Time for clean-up and hand washing: shown in minutes on most days; deferred without a time on d50 to d55, d60, d75 (finding 11).

## Could not settle

- Whether a safety data sheet applies to play sand: I did not open one. Damp sand is the control the course uses, and the guidance read names dust under splash goggles; the lead may want one SDS for the sand brand a school buys.
- Whether the school will have a second adult outdoors (finding 2) is a staffing question for the teacher, not a content one; the day should say what to do if there is no second adult (use the photographs).
- The unit 2.1 and 2.3 days that discuss floods, volcanoes or earthquakes: not a safety matter; the sensitivity read covers them.

No source needs a "browser check": no page refused an automated read.

## Fixes applied (2026-11-22)

- 1. Course page: applied as courses/science-grade-2/safety.md (889 words, the brief's name); DEFAULTS.md names it. Links from the child unit sheets left.
- 2. Outdoor supervision: applied on d4, d66, d70 (second adult, site check the day before, photographs otherwise).
- 3. Soil source: applied in materials.csv, d2, d16, d18, d20.
- 4. Egg and chocolate displays: applied on d39, d42, d43.
- 5. Wind trial dust: applied on d21 (asthma, damp sand, scoop never dry-sweep, cord taped).
- 6. Glass and cold: applied on d7.
- 7. Mat stakes: applied on d18.
- 8. Household samples and lamp: applied on d27, d28.
- 9. Lukewarm: applied on d29.
- 10. Warm-water bath: applied on d42, d43 and unit 4 sheet line 3.
- 11. Hand washing after soil: applied on d42, d50, d52, d54, d55 and unit 5 sheet line 8.
- 12. Mold: applied on d50, d52, d54, d55, d56, d75 and unit 5 sheet line 7; home tubs on the safety page.
- 13. Hand lens: applied on d60.
- 14. Plant allergies: applied on d18, d49, d52, d54, d55, d75.
- 15. Sunglasses: applied on d16, d18.
- 16. Stings and weather: applied on d66, d70.
- 17. Blocks: applied on d33.
- 18. Book stacks: applied on d16, d17, d18 (d2 uses none).
- 19. Foil: applied on d30.
- 20. Splinters: applied on d36.
- 21. Allergy wording: applied, unit 4 sheet line 6.
- 22. Mat and string: applied; d61 mat taped, d40 string short and away from necks (d61 uses no string).
- 23. Trays carried: applied on d7, d29.
- 24. Seed source: applied on d75.
- 25. Eye protection names: applied on the safety page.
- Could not settle: the sand data sheet left for the lead; staffing is answered in the days (photographs without a second adult).

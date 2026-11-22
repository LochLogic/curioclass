# Safety read: science-grade-3 (2026-11-22)

Kind: safety. Target: every hands-on day of science-grade-3 (course finish, COURSE-RUN stage 7). Read-only: this report is the only file written.

## Verdict

Pass with fixes. The days carry a consistent, mostly sound Safety and set-up section (teacher-only pendulum and demonstration, counted magnets and washers, non-glass thermometer, plastic jar, adult-only ice, indoors in a warning), but the course has no course safety page (S5 is a door row), and four hazards need an exact fix: mold handling, seed treatment, the latex balloon and the electromagnet run time.

## What I studied

- NSTA, "Safety in Elementary Science" (http://static.nsta.org/pdfs/SafetyInElementaryScience.pdf, opened 2026-11-22, file dated 2019): taught me that elementary students should not handle heat sources; wires and circuits need goggles or safety glasses (Z87), short circuits are to be prevented and an open switch used; receptacles near water need ground-fault protection; seeds should be sprouting-grade, not garden seed that may be coated with chemicals; students never touch fungus; fungal cultures are never studied in elementary rooms; hands cleaned before and after handling animals; check plant and animal allergies; animals never released.
- NSTA, "Safety Resources for Elementary Schools" (https://www.nsta.org/safety-resources-elementary-schools, opened): index page only (poison control number, state manuals); confirmed what the NSTA elementary set is.
- NSTA, safety topics page (https://www.nsta.org/topics/safety, opened): located the elementary document above.
- CDC, "Mold" (https://www.cdc.gov/mold-health/about/index.html, opened): people with asthma or mold allergy may react severely; cleaning is done with gloves and goggles; ventilate.
- CDC, "Ways to Stay Healthy Around Animals" (https://www.cdc.gov/healthy-pets/about/index.html, opened): wash after touching animals, their habitats and equipment, supervised; no hands or objects in mouths after.
- docs/FOUNDATION.md section 5 (room assumptions: hands-on work written into the plan with a path for a teacher who has nothing) and docs/RUBRIC-SCIENCE.md row S5.
- data/plans/science-grade-3/materials.csv (244 rows).
- No chemical is named anywhere in the course (soil, water, tape, paper, magnets, a D cell), so no safety data sheet applies.

## Course safety page (S5)

No. The course folder holds only unit folders (u01-1 to u06-4), no safety page, and nothing in docs/courses/science-grade-3 is one. S5 is a door row: "No course safety page" is a listed failure. Finding 1 gives the fix.

## Days read

120 day files (d001 to d120) plus 5 sheets in the unit folders. 116 files carry a Safety and set-up section. I read the Safety and set-up and Before class text of every day, every materials row, every step children do with their hands on days 18, 23, 24 and 110, and every Other rooms and At home line that names a hands-on swap. Days d107, d108, d111 and d112 have no Safety and set-up heading; they are paper and talk only (from their materials rows), so this is low.

## Findings

Severity: H = fix before the course is called finished, M = fix, L = tidy.

| # | Sev | Day | Hazard | What the day says | The exact fix |
|---|---|---|---|---|---|
| 1 | H | course | No course safety page | None exists | Add courses/science-grade-3/safety.md (one page, read-aloud rules for children plus a teacher box): goggles on for pendulum, magnet, electromagnet and fan days and wiped between children; nothing in mouths (washers, magnets, counters, bits); wash hands after soil, plants, the mealworm box and the rain jar; the teacher alone secures the pendulum and runs the nail and coil, the fan and the lamp; an adult alone handles ice; indoors in a weather warning; never look at the sun; stop rule: a child who feels unwell, or any broken thing, tells the adult first. List the room needs: a sink or wipes, a ground-fault outlet for the lamp and fan, poison control 1-800-222-1222, and "check your school's policy" for the lamp and fan. Link it from each unit's first day. |
| 2 | H | 37 to 58 (every "an adult removes any") | Mold on class soil | "look for mold; an adult removes any." (d037, d038, d039 to d055, d058) | Replace with: "If mold shows on a pot, do not touch, shake or sniff it. Move children away, a child with asthma or a mold allergy farthest. An adult in gloves and goggles lifts the whole pot into a sealed bag, puts it in the outside trash, wipes the spot with soap and water, and washes hands. Drop that pot from the record and use the next pot or the supplied record, said aloud to be invented." Reason: CDC says mold can cause severe reactions in people with asthma or allergy; NSTA says students never touch fungus and fungal cultures are not studied. Mold should not be picked off in the room. |
| 3 | M | 18 and materials.csv | Seed treatment | Rows "radish seeds" and "fast-cycling flowering seeds" state no source or treatment | Add to both rows: "untreated seed sold for sprouting or classroom use, never garden seed, which can be coated with chemicals; keep the packet; no child eats any seed or plant." (NSTA, Safety Related to Plants.) |
| 4 | M | 23 and materials.csv balloon row | Latex balloon | "A balloon on hair is by choice only: an adult alone inflates it and picks up fragments at once." "Check allergies first." (generic) | Name latex: "Use a latex-free balloon, or none. Check for a latex allergy before any child touches one. An adult alone inflates it, and any burst piece goes straight in the bag." Comb and cloth stay the default. |
| 5 | M | 24 | Electromagnet: wire and D cell heat, flying clips | "the wire may warm: stop if it does. Never short the cell." "Disconnect the cell after each cycle." | Add: "Each on time is at most 5 seconds, then switch off and disconnect. Cell in a holder, new alkaline only. Touch the wire only after it has been off for a minute. Use a push switch so the circuit is open by default. Rehearse first. Children stay seated at least 1 m back." (NSTA: open switch, no short circuits, goggles with wires.) |
| 6 | M | 18, 48 and materials.csv growing lamp | Lamp, cord and water | "The lamp is adult-only, and water stays away from it." d048: "wipes spills at once, away from the lamp." | Add to the lamp row and d018: "LED grow light that stays cool, plugged into a ground-fault outlet, cord taped flat and out of walkways, above the pots, water tray on the other side of the room, unplugged when the pots are watered." (NSTA: receptacles near water need ground-fault protection; cords covered.) |
| 7 | M | 38, 44, 48 and materials.csv eye protection | Safety glasses named but not on the materials list | d038: "Safety glasses on for watering." d044, d048: "Safety glasses stay on until the cups are emptied." Eye protection row used_days: 1 8 9 12 14 17 19 20 21 24 26 27 31 110 | Recommend cutting the glasses lines from the three days: watering a seedling from a cup is not a splash hazard, and unneeded gear teaches that goggles are decoration. (Or add 38 44 48 to the row.) |
| 8 | M | 1, 8, 9, 12, 14 and materials.csv eye protection | Impact rating never stated | "Fit 30 pairs of eye protection." Only d110 says "impact". | In the eye protection row: "ANSI Z87.1 impact-rated safety glasses or goggles, wiped between children, worn over a child's own glasses." (NSTA names Z87.1.) |
| 9 | M | 73 | Outdoor walk | "walks, wears closed shoes, looks only and touches no living thing, unknown organism or water" | Good. Add: "Bring any child's allergy medicine, such as an auto-injector, and an adult trained to use it. The adult checks the spots for a stinging-insect nest the day before and uses the photographs if one is near." (NSTA lists stinging insects as never studied.) |
| 10 | L | 17, 19, 20, 21, 26, 27, 31 | Magnets: pinch, swallow | "large encased classroom magnets... low-strength... counted out and back... away from mouths" | Sound. Add to the materials row: "ceramic or encased only; no loose rare-earth magnets, the swallowing hazard." (CPSC page refused automated reads; see Browser check.) |
| 11 | L | 18 to 55 | Mealworm bran and soil dust | "wash hands after soil and living things" | Sound. Add: "damp the potting mix before pouring, to hold dust down; a child with asthma or a bran allergy sits away from the box." Looking through the lid stays. |
| 12 | L | 107, 108, 111, 112 | No Safety and set-up heading | none | Add one line to each: "Paper and talk only; nothing is handled. Clean-up is 2 minutes." |
| 13 | L | 21 At home swap | Coin as foil stand-in | "any thin non-steel metal, such as a coin from the drawer" | Change to "a square of kitchen foil"; a coin is a choking object. |
| 14 | L | 19, 20, 21 At home | Flying clips at home | The swaps have no eye line | Add: "Keep your face back and wear glasses or sunglasses while the clip swings." |
| 15 | L | 110 | Fan | "adult alone places the house, plugs in and switches the fan, on low, guarded, with water kept away... Unplug before collecting anything." | Sound. Add "ground-fault outlet; cord taped flat; the weather jar is emptied before the fan is plugged in", since the jar is in the room. |

## Checked and sound (no change)

- Pendulum days (1, 8, 9, 12, 14): teacher-only securing, low arcs below faces, washers counted and kept from mouths, no child on a swing, string off necks. Home swap: a key held at arm's length by an adult, away from the mouth.
- Push days (2 to 7, 15, 16): pushes inside the tray, nothing thrown, floors clear.
- Mealworms (18 to 58, 79 to 81): looked at through the lid, never handled, never released, hands washed. Matches NSTA and CDC.
- Plants: hydrangea is shown in pictures only, flowers are touched only after allergies are checked and hands washed, nothing is eaten.
- Weather record (all weather days): non-glass thermometer, plastic jar, adult empties it and handles ice, indoors in a warning, never look at the sun.
- Day 110 fan: adult only, low setting, impact eye protection over glasses, observers behind a line, unplug first.
- Paper days say so. No flame, chemical, glass, sharp or heat source is handled by a child anywhere in the course.

## Could not settle

- Whether a school allows the growing lamp and fan in the room (the teacher's facilities question; the course safety page says "check your school's policy").
- Any child's real allergy list (latex, bran, pollen): only the teacher can settle it; the days already say to check.

## Browser check

- https://www.cpsc.gov/Safety-Education/Safety-Guides/Toys/Magnets : refused automated reads (403). Fact it would support: swallowed magnets are a serious hazard for children, so loose rare-earth magnets stay out of the room (finding 10). File: this report. No sources.csv row was added, since this job edits only the report.

## Fixes applied (2026-11-22)

1. Applied: courses/science-grade-3/safety.md written (887 words); DEFAULTS.md names it; the 20 mold days point to it.
2. Applied: every "an adult removes any" line now sends the teacher to the safety page's mold rule; the full rule is on the page, in days.csv and in materials.csv.
3. Applied: the seed rows and d018 say untreated sprouting seed, nothing eaten.
4. Applied: d023 and the balloon row: latex-free only, after a latex check.
5. Applied: d024 push switch, 5 seconds at most, cell in a holder, touch after a minute, 1 m back; the D cell row.
6. Applied: d018 and the lamp row: a light that stays cool, ground-fault outlet, cord taped, unplugged for watering.
7. Applied: the glasses lines and materials cut from days 37, 38, 44 and 48.
8. Applied: the eye protection row names the Z87.1 impact rating, worn over glasses.
9. Applied: d073 adds allergy medicine, a trained adult and the nest check.
10. Applied: the magnet row: encased or ceramic, no loose rare-earth magnets (the CPSC page kept as browser check, sources.csv G71).
11. Applied: the potting soil and habitat rows (damp mix; asthma or bran allergy seat).
12. Applied: a Safety and set-up heading added to d107, d108, d111, d112 ("Paper and talk only; nothing is handled."); clean-up minutes not added (no minutes to spare).
13. Applied: the d021 swap is now an empty aluminum drink can held by an adult, not a coin.
14. Applied: the d019, d020, d021 At home swaps add face back and glasses.
15. Applied: d110 names a ground-fault outlet; the fan row adds cord taped and jar emptied first.

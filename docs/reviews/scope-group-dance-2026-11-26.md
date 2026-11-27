# Scope group read: dance, 2026-11-26

Group read of the four dance band courses side by side (build/scope-writes/GROUP-READ.md): dance-grades-k-to-2,
dance-grades-3-to-5, dance-grades-6-to-8, dance-grades-9-to-12. Findings already made and fixed in each course's own
read are not repeated.

## What I read

- AGENTS.md; docs/agents/EXPERT.md; docs/pipeline/briefs/sequence-read.md; build/scope-writes/ARTS-BRIEF.md.
- docs/agents/lenses/arts.md; docs/ADOPTION-BAR-SUBJECTS.md section 2; docs/courses/arts/STANDARD.md (3, 3.4, 5, 6)
  and docs/courses/arts/APPROACH.md in full.
- For each course: scope-and-sequence.md in full; frame.md Seams, Leave-out bullet and Units table; days.csv read by
  script (works named, safety wording, retrieval notes, leave-out fallbacks, cross-subject notes, skills and codes
  against data/progressions/arts.csv); the -fixes-2026-11-26 report.
- docs/courses/CALENDAR.md (how a course meets, the stagger rules, the dance rows); data/plans/calendar.csv for the
  physical education, health, science, ELA rows the dance days cite; data/plans/physical-education-grades-6-to-8/
  days.csv days 275 and 276 and its scope's unit 22 lines; data/progressions/physical-education.csv dance rows.
- docs/agents/decisions/DESK-ANSWERS.md, the 2026-11-26 entries naming the arts or dance.

Checks run by script: every one of the 100 dance progression rows is on some day's `skills`, and every id it lists is
on some day's `codes` (no gap, no `~` row left unfinished outside Level 4, whose four `~` rows are reassessment by
design).

## Findings

### 1. Safety wording on the days thins out outside grades 3 to 5 (scope)

- **K to 2.** The hazards and footwear block ("floor cleared and checked ... never socks on a smooth floor; spots an
  arm's length apart; freeze cue every session") sits only on days 1, 65 and 129, not on the first day of units 2 to
  4, 6 to 8 and 10 to 12. The scope's first page and the frame (frame.md line 186) say jumps, landings and soft
  stamping use a resilient floor the school confirms, and are marked met only in a suitable space, but no K to 2 day
  carries that rule: not the strong-beat landing days 137, 138 and 140, not the showing on day 145 and not the year 2
  mid-year check on day 161, which mark "strong-beat landings" met.
- **6 to 8.** The first days of units 8 and 11 (days 113 and 163) have no "Hazards and controls" line, though the
  scope says "each unit's day 1 note carries its hazards and controls in the frame's words"; and no 6 to 8 day names
  the footwear rule (bare feet or soft shoes, never socks on a smooth floor), which every other course's days do.
- **The stop cue's name.** K to 2 calls it the freeze cue and the stop cue on the same day (day 1: "The stop cue is
  taught first today ... freeze cue every session"); 3 to 5, 6 to 8 and 9 to 12 call it the stop cue. A grade 3
  student meets a renamed routine on day 1.
- **Against.** Dance 3 to 5 puts the full block on all 12 unit openers and the floor rule on its landing days (70,
  134). 9 to 12 states it on its landing and leap days (169, 171, 175, 189).
- **Why it matters.** A teacher plans from the day row. The check days 145 and 161 score landings with no line saying
  a hard floor means a low, no-impact version marked met only later; that is a safety and a scoring gap in the same
  cell.
- **Fix.** K to 2: copy the year's day 1 hazards block, shortened to its three rules, into each unit's first day
  (21, 37, 53, 83, 99, 115, 147, 163, 179), and the floor rule ("landings only on a level, resilient floor the school
  confirms; otherwise low and without impact, marked met only in a suitable space") into days 137, 138, 140, 145 and
  161. Name the cue once as "the stop cue (freeze on the drum)" on day 1 and use "stop cue" after. 6 to 8: add the
  hazards line to days 113 and 163 and the footwear rule to each year's day 1 (1, 65, 129).

### 2. The 9 to 12 leave-out list misses two units that draw on worship or ceremony (frame)

- **Where.** dance-grades-9-to-12 frame.md Leave-out bullet names units 5 (Kykunkor) and 9 (The Rite of Spring) only.
  Unit 12 day 331 studies Grace, "set partly to spiritual music, watched and not danced to as worship"; unit 14 day
  406 studies Birds with Skymirrors, which "draws on Pacific ceremony; watched, never danced or imitated".
- **Against.** K to 2 names unit 6 for Revelations, set to spirituals; K to 2 and 6 to 8 name each unit whose work is
  tied to ceremony (the hoop dance, khon, the fancy shawl dance, Kaha:wi); 3 to 5 names legong's and the Guinean
  piece's units. STANDARD.md 5 asks for one line on each course page for a unit that studies a sacred or ceremonial
  tradition (Cory, Desk q-prework-open-1).
- **Why it matters.** The same kind of work gets a named leave-out in grade 1 and none in Level 3, so the course page
  and family note would not offer it.
- **Fix.** Add to the bullet: unit 12 (Grace is set partly to spiritual music; Moon Water keeps every id met) and unit
  14 (Birds with Skymirrors draws on Pacific ceremony and is watched only; Creole Giselle and Admiring La Argentina
  keep every response id met). The unit plans confirm the swap covers each part.

### 3. Butoh: 6 to 8 asks for something its company does not offer, and the two courses say it two ways (scope)

- **Where.** 6 to 8 day 5: "a described butoh piece by Sankai Juku ... Sensitivity: butoh, the unit plan picks a piece
  without postwar themes; no body paint." 9 to 12 day 555 (Sankai Juku's Hibiki): "butoh may show bodies painted
  white ...; the teacher previews the linked material."
- **Why it matters.** Shaved heads and bodies covered in white powder are the company's usual look (Sources). Read as
  "a piece with no body paint", the 6 to 8 note sends the unit plan looking for a piece that may not exist; read as
  "students wear none", it says nothing about what the class will see, which the 9 to 12 note handles.
- **Fix.** 6 to 8 day 5 note: "Sensitivity: butoh; the unit plan picks a piece without postwar themes. The dancers'
  white-powdered bodies are named as the form's look, and the teacher previews the linked material; students wear no
  paint." Day 69 (butoh revisited) points back to it.

### 4. The choreographic tools card changes its members from band to band with no bridge (scope)

- **Where.** 3 to 5 day 36: "repeat a move, reverse it, add one move at a time" (repetition, reversal, accumulation).
  6 to 8 day 23: "repetition, canon, retrograde and accumulation". 9 to 12 bridge day 5: "repetition, canon,
  retrograde, change of level".
- **Why it matters.** The 6 to 8 retrieval on day 20 retrieves grade 5's "several choreographic tools altered
  together", then day 23 names the reversal "retrograde" without saying it is the tool the student knows. A student
  from 6 to 8 meets a Level 1 card that drops accumulation and adds change of level. Discipline words should grow, not
  swap.
- **Fix.** 6 to 8 day 23 goal: "... retrograde (the reverse of the grade 3 to 5 tools card) ...". 9 to 12 day 5: keep
  the four, and add to the note "a student from dance 6 to 8 also knows accumulation; it stays a choice on the card".

### 5. 6 to 8 says Trisha Brown is "met again", which only dance 3 to 5 made true (scope)

- **Where.** 6 to 8 day 147: "Grand Union ... Trisha Brown met again, now for group improvisation." Brown is met in 3
  to 5 (Accumulation, day 35; Roof Piece, day 181) and nowhere earlier in 6 to 8. The 6 to 8 frame says dance 3 to 5
  is not required and gives every year 6 retrieval a reteach for that reason.
- **Fix.** Day 147: "Trisha Brown, one of its members (a class that took dance 3 to 5 met her Accumulation and Roof
  Piece), now for group improvisation."

### 6. The reteach the first pages promise is written on the seam days but not inside the band in K to 2 and 3 to 5 (scope)

- **Where.** K to 2 first page: in a mixed class "each day 2 retrieval task becomes a ten-minute reteach"; 3 to 5
  first page: "each day-2 retrieval task then carries its ten-minute reteach as written". The year 1 and 2 retrieval
  days of K to 2 (66, 84, 100, 116, 130, 148, 164, 180) and the year 4 and 5 days of 3 to 5 (66, 82, 100, 118, 130,
  147, 166, 182) name the earlier row but no reteach. Only the 3 to 5 year 3 seam days (2, 18, 36, 54) write it.
- **Against.** 6 to 8 writes it on every inner retrieval day ("the reteach is used by any student new to the band",
  day 66 and on).
- **Fix.** Add one sentence to each of those 16 notes, in 6 to 8's words: "For a student new to the band or meeting
  this year first, the ten minutes are the reteach of the earlier step."

### 7. A stale physical education lean in 6 to 8 (scope)

- **Where.** 6 to 8 day 140 and the scope's lean table: "Physical education's grade 8 dance routine unit (its unit
  18, weeks 14 to 16)". In data/plans/calendar.csv grade 8 unit 18 is "My planned week, and leading a warm-up",
  school days 58 to 69, weeks 12 to 14 (its skill g8-fitness-dance-apply carries the dance routine).
- **Fix.** Day 140 and the lean table: "physical education grade 8 unit 18 (a planned week of routines, dance among
  them; weeks 12 to 14) comes later". Nothing else moves; the order still holds.

### 8. Physical education grade 8 retrieves a dance elective every student is assumed to have taken (scope, in the physical education course)

- **Where.** physical-education-grades-6-to-8 day 276: "Retrieval of dance 6 to 8 unit 8's study of capoeira's
  history (grade 7); where a school has no dance course, the case card gives the history." Dance 6 to 8 is one of four
  arts electives (CALENDAR.md rule 3: a student takes one at a time), so most students in a school that has dance
  still never met unit 8. Dance 6 to 8 day 113 and its lean table name the return and need nothing.
- **Fix (lead, physical education's file).** Day 276 note: "A student who took dance 6 to 8 retrieves its unit 8
  study of capoeira's history; every other student, and every student where the school has no dance course, gets
  the history from the case card first." No dance file changes.

### 9. Two K to 8 school_day patterns (scope)

- **Where.** K to 2 and 3 to 5 put each week's two sessions on its second and fourth school days (school days 2, 4,
  7, 9 ...); 6 to 8 uses ceil(2.5 x n) (3, 5, 8, 10 ...). Both are band-wide counts under lead call 5 and both put
  every day in the right week, so nothing breaks.
- **Why it matters.** Only for one dance teacher scheduling K to 8 from calendar.csv, who sees two weekday patterns.
- **Fix.** No CSV change. One line in CALENDAR.md (the lead's band-wide school_day note, already queued from the
  fix passes): the weekday inside a week is a placeholder and a school sets its own two days.

## What holds

- **Seams.** Every cross-band retrieval names what the earlier band taught, on the day it taught it: 3 to 5 days 2,
  18, 36 and 54 against K to 2 units 9 to 12 (days 129 to 138, 147 to 151, 165 to 170, 179 to 184); 6 to 8 days 2,
  20, 36 and 50 against 3 to 5 days 130 to 136, 147, 166, 168, 182 and 153; 9 to 12's bridge teaches each grade 8 row's
  steps (days 1 to 12) and units 2 to 5 retrieve the bridge. Inner-band retrievals all match their earlier days.
- **No gaps.** All 100 dance rows are taught; each id is on a day.
- **Repeats are reasoned or are different works.** Kpanlogo returns in K to 2 unit 12 as the leave-out cover for the
  hoop dance; Sinfonietta (units 4, 6) and Café Müller (units 13, 18) return by name in 9 to 12. Across bands the
  makers who recur bring a different work (Nikolais, Tharp, Cloud Gate, Akram Khan, Sankai Juku, Swan Lake and The
  Rite of Spring in new versions), and 9 to 12 Level 1 assumes no earlier dance.
- **Load and calendar.** Check weeks match CALENDAR.md in every year; the year-end check sits before the performance
  unit in K to 5 and after it in 6 to 8 (finals week), as the frames set; written work ramps from talk items (K to 2)
  to read-aloud short answers (3 to 5) to a paragraph and a page (6 to 8, 9 to 12).
- **Shared routines.** The critique is "describe, ask, suggest" word for word on every critique day of all four
  courses; showing days run six groups of five and the same 40-minute budget K to 8; the invented dancer carries
  every food and body item in each band (APPROACH "Sensitive ground"); Native, sacred and hard-history works are
  watched only, from the community's own words, with the sensitivity read named before the unit plan, in every band.
- **Cross-subject leans** checked against calendar.csv are right except finding 7: physical education K to 2, 3 to 5
  and 9 to 12 weeks, health grade 8 unit 26, science grade 4 units 1 to 3, science grade 5 unit 1, ELA grades 3, 5, 6
  and 8.
- **Named facts** spot-checked from memory hold (dates and makers in the four Units tables). Vincent Mantsoe's solo is
  listed as "Gula" (1993) on the page opened below; 9 to 12 day 18 already has the unit plan confirm the title and year.

## Sources

- https://en.wikipedia.org/wiki/Sankai_Juku, opened 2026-11-26: the company's dancers typically appear with shaved
  heads and white-powdered bodies (finding 3).
- https://en.wikipedia.org/wiki/Vincent_Mantsoe, opened 2026-11-26: solo "Gula" (1993) listed; living (What holds).
- data/plans/calendar.csv and data/plans/physical-education-grades-6-to-8/days.csv, read 2026-11-26 (findings 7, 8).

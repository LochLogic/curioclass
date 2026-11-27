# Scope group read: media arts, K to 12 (2026-11-26)

Group read per build/scope-writes/GROUP-READ.md for media-arts-grades-k-to-2, media-arts-grades-3-to-5,
media-arts-grades-6-to-8 and media-arts-grades-9-to-12. This read looks only across the four courses; findings
already raised and settled in each course's own read and fix report are not repeated.

## What I read

- AGENTS.md; docs/agents/EXPERT.md; docs/pipeline/briefs/sequence-read.md; build/scope-writes/ARTS-BRIEF.md.
- data/progressions/arts.csv, the 100 `ma` rows (grades K to 12), read by script.
- For each of the four courses: scope-and-sequence.md in full; days.csv by script (codes against owned rows, every
  code taught and assessed, card names, works, safety and consent wording, retrieval notes); the frame where a
  finding rests on it (check weeks, the 3 to 5 talk-and-written day form, the 9 to 12 consent lines, screen-break
  limits); the sequence read and the -fixes report of 2026-11-26.
- docs/courses/CALENDAR.md (rules 1, 3 and 4 and the arts rows of the target-week table); docs/courses/arts/APPROACH.md
  "How a day opens"; docs/agents/decisions/DESK-ANSWERS.md entries of 2026-11-25 and 2026-11-26 naming arts or media
  arts (connecting ids swapped back, arts scope lead calls, the unit 5 showing call, the after-core frame calls).
- Gates: `sequence.py check` on K to 2 and 9 to 12 (0 failures; 9 to 12 keeps its expected Level 4 notes). A script
  check found every `ma` row's codes, K to 12, on a teaching day and an assessed day of its own course and year.

## Findings

### 1. The year-end check sits before the screening unit in K to 5 and after it in 6 to 12

- **Where.** K to 2: year-end checks days 53/54, 117/118, 181/182 in week 27, before the screening units (days 55 to
  64, 119 to 128, 183 to 192). 3 to 5: days 51/52 (week 26), 113/114 (week 25), 177/178 (week 25), before units 4, 8,
  12. 6 to 8: days 63/64, 127/128, 191/192 in week 32, after the screening units, drawing from units 2 and 3 (6 and 7,
  10 and 11). 9 to 12: every level's year-end check in week 32 after its showing unit.
- **Why it matters.** The reason K to 5 placed the check early (staying off the core year-end weeks) no longer holds
  under CALENDAR.md rule 1 (specials do not count against the stagger). The cost is real and the same in both K to 5
  courses: the make and judge rows (units 3, 7, 11) and the present and sources rows (units 4, 8, 12) are never sampled
  at course level, 42 of 54 ids in K to 2 and 31 in 3 to 5, and both once-a-week paths have to pause the screening unit
  around the check. 6 to 8 shows the other shape works in this group: its year-end check samples the third unit's
  judge row (MA:Re8.1.6, 7, 8) and carries the screening unit's record.
- **Fix.** For K to 2 and 3 to 5 together: move each year-end check and its respond day to week 32, after the
  screening unit, sampling the second unit's ideas row and the third unit's judge row (as 6 to 8 does) and carrying
  the screening unit's record; change the frames' check tables and once-a-week bullets, the units-table phrases
  "after the year-end check", and CALENDAR.md's target weeks for both courses (K to 2 "21, 27" to "21, 32"; 3 to 5
  "17, 26 / 17, 25 / 18, 25" to "17, 32 / 17, 32 / 18, 32"); the course fixers then re-lay days.csv. The K to 2 fix
  report (structure item 1) and the 3 to 5 fix report (structure item 5) each asked for this alone; it should be one
  call for the K to 5 pair, so the two scopes do not split. My pick: move. If the lead keeps the early weeks, finding
  2 still applies.
- **Tag: structure.**

### 2. 3 to 5 still gives the stale stagger reason that K to 2 struck

- **Where.** 3 to 5 scope-and-sequence.md, "Codes not sampled on a course-level check": "the screening unit comes
  after the year-end check, which sits before the core year-end weeks 28 to 32". K to 2's matching paragraph struck
  the same reason in its fix pass and names CALENDAR.md rule 1 instead.
- **Why it matters.** Two scopes from one subject now give different reasons for the same design. A unit-plan writer
  reading 3 to 5 would think the weeks are fixed by the stagger rule.
- **Fix.** 3 to 5 .md: replace that clause with K to 2's wording ("because the frame keeps the year-end check before
  the screening unit; the older reason, staying off the core checks of weeks 28 to 32, no longer holds under
  CALENDAR.md rule 1; see finding 1 of the media arts group read"). The frame's "CALENDAR.md stagger tool c" reason
  goes with finding 1.
- **Tag: scope** (the frame's sentence: frame).

### 3. Three different rules for a 30-minute period, and 3 to 5's asks for an APPROACH exception it does not need

- **Where.** K to 2 Shorter path: the talk check day moves its self-check to the end of the day before, so the six talk
  groups still fit (5 + 21 + 4). 3 to 5 Shorter path: the end-of-unit talk items move onto the last three making days,
  and its fix report (structure item 2) asks for an exception to APPROACH "Kinds of day". 6 to 8: the opener drill
  drops first, check days keep their 25 minutes.
- **Why it matters.** The 3 to 5 rule moves assessment onto making days that already hold the critique and ten
  rotating marks, and would bend an arts-wide approach rule for one course. 3 to 5's own course-level check form
  already runs the talk groups while the class does the paper task and the written item at the tables (scope,
  "Course-level checks"), which is the K to 2 pattern. Run the same way, a 30-minute end-of-unit talk-and-written day
  is set-up 4, written item and self-check at the tables (15) while the six groups are heard (18), clean-up 3: 25
  minutes, 5 slack.
- **Fix.** 3 to 5 .md "A shorter period (30 minutes)": the end-of-unit talk-and-written day stays a check day; on the
  30-minute period the six talk groups run at the teacher's table while the class writes the item and the self-check
  (as on the course-level check days), and if a class needs longer, the self-check moves to the end of the day before
  (the K to 2 rule). Drop the 3 to 5 structure item 2 (the APPROACH exception).
- **Tag: scope.**

### 4. Shared cards and words are named differently from band to band

- **Where.**
  - Shot sizes: K to 2 day 67 "far, middle and close"; 3 to 5 days 3 and 5 "wide, medium, close-up"; 6 to 8 day 2
    "long, medium, close"; 9 to 12 day 2 "wide, medium, close".
  - The showing plan: K to 2 and 3 to 5 "screening-plan card" (K to 2 days 58, 122, 186; 3 to 5 days 59, 121, 185);
    6 to 8 "showing plan" (days 56, 120, 184, with "screening-plan" left on the same days); 9 to 12 "screening plan" in
    Level 1 (days 11, 74, 111, 161) and "showing plan" from unit 5 (days 133, 150 on).
  - 6 to 8 day 2's retrieval names grade 5's card "the class ethics checklist"; 3 to 5 calls it the media-literacy
    checklist (days 130, 186).
  - 9 to 12 days 2 and 3 "Look-describe-interpret retaught", but no K to 8 day teaches a routine by that name (it
    appears only in 9 to 12, days 2, 3, 14).
- **Why it matters.** A student meets these cards in every band, and a retrieval opener that names a card by a word
  the earlier course never used fails for exactly the students who did take the earlier course.
- **Fix.** One word set, kept in each scope's words: shot sizes "wide, medium, close" from grade 3 on (K to 2 keeps
  "far, middle, close" and 3 to 5 day 3's note adds "the far, middle and close shots of grades K to 2"); 6 to 8 day 2
  "wide (long), medium, close". The plan card is the "screening-plan card" through grade 5 and the "showing plan"
  from grade 6 on; 6 to 8 days 56, 120, 184 and 9 to 12 days 11, 74, 111, 118, 161, 164, 271, 431 say "showing plan",
  and 6 to 8 day 50's note adds "grade 5's screening-plan card grows into the showing plan". 6 to 8 day 2: "the
  media-literacy checklist". 9 to 12 days 2 and 3: "look-describe-interpret taught (the reading steps of grades 6 to 8,
  given one name here)".
- **Tag: scope.**

### 5. Techniques taught again as new in a later band, with no step up named

- **Where.**
  - Paper-cutout stop-motion: K to 2 day 153 ("move a little, capture, move again") and 3 to 5 day 80 (the same three
    steps, plus replacement parts).
  - Shot sizes and angles: 3 to 5 days 3 and 4 (sizes; high, low, eye level and how they steer) and 6 to 8 days 2 and
    36 (sizes; high, low, eye level and the point-of-view shot).
  - The 12-drawing flip book and stop-motion: 3 to 5 day 16 (the 12-frame loop and flip book) and days 80 and 146
    (stop-motion), then 6 to 8 day 18 (the 12-drawing flip book and stop-motion, "move a little, capture, move
    again") as the unit 2 Understanding day.
- **Why it matters.** Each later band is optional-entry, so a reteach is fair, but none of these days says it is a
  return or what is new, unlike the works that return (6 to 8 day 1; 9 to 12 days 1, 199, 279, 437). A student who took
  the earlier band redoes the same task, and 6 to 8 day 18 adds nothing for MA:Pr5.1.6c's "ordinary" use beyond
  grade 3's.
- **Fix.** In each later day's note: "returns from grade N (day D); new today: ...". 3 to 5 day 80: new are replacement
  parts and the even move. 6 to 8 day 2: new is what each size steers in a sequence; day 36: new is the point-of-view
  shot. 6 to 8 day 18: keep the ordinary use, but teach a step grade 3 to 5 did not: timing (holds, frames per second,
  and drawings spaced for ease in and ease out), with the 12-drawing flip book run as the retrieval warm-up rather
  than the day's technique. No day moves.
- **Tag: scope.**

### 6. 9 to 12 teaches the "what if" list as "idea method one" after 6 to 8 taught it

- **Where.** 6 to 8 day 16 teaches a mind map, a "what if" list and a constraint game; day 144 teaches thinking in many
  directions. 9 to 12 day 44 teaches "Idea method one, the 'what if' list" as new, and its retrieval (`retrieves`
  ma-g8-ideas) recalls the bridge's storyboard and workflow sheet, not grade 8's idea method; day 45 adds the forced
  pairing.
- **Why it matters.** The seam runs one way: the grade 8 row the Level 1 row builds on (methods to produce ideas) is
  named in `retrieves` and never retrieved, and a student who took 6 to 8 is taught its first method again.
- **Fix.** 9 to 12 day 44: the retrieval recalls grade 8's thinking in many directions and grade 6's methods card
  (with the reteach for a student new to media arts); the day's new method is the forced pairing (now day 45), and day
  45 takes a second new method (for one, a random-word link, or reversing the brief). The level's two-method look-for
  on days 44 to 46 is unchanged.
- **Tag: scope.**

### 7. Hopinka returns in 9 to 12 without the return named

- **Where.** 6 to 8 day 84 studies Sky Hopinka's Jáaji Approx. (grade 7); 9 to 12 day 321 opens Level 3 on his Kicking
  the Clouds and does not name the earlier study. Every other cross-band return in the group is named (6 to 8 day 1
  Lumière; 9 to 12 day 1 Méliès, 199 Te Wei, 279 Skawennati, 437 Isuma).
- **Why it matters.** The repeat is a fair one (a different film, a harder question), but a reader cannot tell it is
  chosen; the sensitivity read for Ho-Chunk and Pechanga language is also worth carrying over.
- **Fix.** 9 to 12 day 321 note: "Hopinka returns from the 6 to 8 frame's Jáaji Approx. with a different film and a
  harder question."
- **Tag: scope.**

### 8. 9 to 12 day notes drop the family's consent for a student under 18

- **Where.** 9 to 12 days 2, 6, 7, 8, 30, 31, 32, 33, 34: "no filming of anyone without their yes". The 9 to 12 frame
  (line 211: "their yes (and the family's under 18)") and its showing days (148, 566, 630) carry the full rule; K to 2,
  3 to 5 and 6 to 8 say "the family's yes" on every recording day (6 to 8: days 10, 25, 55, 60 and on).
- **Why it matters.** Most Level 1 students are 14 or 15. A teacher building those capture days from the note would
  film a classmate on the classmate's own say-so, which no other course in the group allows and the frame does not.
- **Fix.** Those nine notes: "no filming of anyone without their yes, and the family's for a student under 18 (a
  student 18 or over decides alone; the school's own rules apply)".
- **Tag: scope.**

### 9. Minutes that drift: same-year retrieval and fold-in savings

- **Where.** Same-year retrieval is a ten-minute task in K to 2 (days 86, 109, 156, 173) but a five-minute warm-up in
  3 to 5 (days 41, 58, 105, 120, 170, 186) and 6 to 8 (day 168); APPROACH "How a day opens" gives the opener five
  minutes. Fold-in days: K to 2 moves 10 minutes and saves 30, 3 to 5 moves 5 and saves 35, 9 to 12 moves 5 and saves
  40 of 45, but 6 to 8 moves the drill into the next opener and still says each fold-in "saves 40 minutes" of a
  40-minute session.
- **Why it matters.** Small, but these are the same routine in the same subject, and 6 to 8's sum (160 minutes a year)
  is off by the warm-up.
- **Fix.** K to 2: same-year retrievals become five-minute warm-ups in the opener (the cross-year ones stay ten, rule
  2), and the four notes say so. 6 to 8 Shorter path: "its drill moves into the next day's opener as a 5-minute warm-up;
  each saves 35 minutes, 140 a year".
- **Tag: scope.**

## What holds

- Every `ma` progression row, K to 12, is owned by its own course and year, taught before it is assessed, and
  assessed; no `~` row is left begun (the Level 4 rows deepen finished Level 3 ids). No gap.
- The seams hold by grade: each band's first-year retrievals name the right earlier unit (3 to 5 days 2, 16, 36, 54 on
  K to 2 units 9 to 12; 6 to 8 days 2, 16, 36, 50 on 3 to 5 units 9 to 12; 9 to 12 days 14 to 118 on grade 8 rows),
  each with its reteach, since every earlier band is optional; the 9 to 12 bridge and day-1 readiness check cover a
  student new to media arts.
- The unit order (read and society; ideas and craft; make and judge; present and sources) is the same in every K to 8
  year, and the critique routine is "describe, ask, suggest" on the critique card in all four courses.
- The demand ramps: talk and table tasks in K to 2; a first written item in grade 3 after chart practice (3 to 5 days
  1, 5, 6); two silent written items in 6 to 8; 30-minute sittings and the paragraph frame in 9 to 12. Screen-break
  limits rise on purpose (10 minutes K to 5, 15 in 6 to 8, 20 in 9 to 12).
- Sensitivity handling is the same across the group: flagged works name the flag and the read before use, Native
  works are studied by looking with no imitation, own-life tasks carry an invented or public option marked the same,
  and blades stay with an adult.
- Calendar: every check sits on CALENDAR.md's weeks for its course; K to 8 `school_day` counts across the band (6 to 8
  by frame.py's even spread, K to 5 by the second and fourth school day; both land in the frame's weeks, as lead call 8
  allows).
- Named facts checked: Alassane's 1965 film is listed under both "La Mort du Gandji" and "La Mort de Gandji", so the
  3 to 5 title stands; Hopinka's Kicking the Clouds (2021) on his grandmother learning Pechanga, and the 9 to 12 Te Wei,
  Skawennati and Isuma returns, match the earlier courses' days.

## Sources

- Web search, 2026-11-26, "Moustapha Alassane La Mort de Gandji 1965": results included
  https://iffr.com/en/2010/films/la-mort-de-gandji,
  https://blog.animationstudies.org/frogs-as-counterclaim-in-the-death-of-gandji-la-mort-du-gandji-1965/ and
  https://en.wikipedia.org/wiki/Moustapha_Alassane (both title spellings in use, 1965, Niger). Result listings only;
  the pages were not opened.
- Hopinka's Kicking the Clouds (2021) and the other work dates: from memory and the four frames; the frames' own
  "facts to confirm at the unit plan" items still stand.

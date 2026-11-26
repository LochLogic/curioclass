# Frame read: Dance, grades K to 12 (2026-11-25)

Expert cold read of the four Curio Class dance frames, read together as one combined read under
docs/pipeline/briefs/frame-read.md with the after-core changes:

- docs/courses/dance-grades-k-to-2/frame.md
- docs/courses/dance-grades-3-to-5/frame.md
- docs/courses/dance-grades-6-to-8/frame.md
- docs/courses/dance-grades-9-to-12/frame.md

I did not write the frames. Nothing else was edited and git was not run.

## What I read

- The four frames in full, and their rows in data/plans/frames.csv (K to 2, 3 to 5 and 6 to 8: 12 units, 192 days,
  40 minutes, 2 a week; 9 to 12: 19 units, 640 days, 45 minutes).
- All 100 da-* rows in data/progressions/arts.csv, parsed with Python's csv module, and today's commit 1a6b4e314 that
  changed them (read from the file, not through git).
- docs/courses/arts/STANDARD.md (band-year rule 3.1 and 3.2, the PE split in section 6) and APPROACH.md;
  docs/agents/lenses/arts.md; docs/agents/EXPERT.md.
- The four physical education frames (physical-education-grades-k-to-2, 3-to-5, 6-to-8, 9-to-12), at their Units
  tables, cross-subject tables and For the lead lists.
- The core frames the dance frames lean on, at their Units tables only (science grades 3 to 5, social studies grade 6
  and 7 seams named in the dance 3 to 5 and 6 to 8 frames).
- docs/courses/CALENDAR.md and data/plans/calendar.csv for the check weeks.
- The visual arts K to 2 expert read and fix pass of today (docs/reviews/frame-visual-arts-grades-k-to-2-2026-11-25.md
  and its fix file), for REPEAT tags.
- Gates: `python -X utf8 scripts/plan.py check` on each dance frame: 0 failures in all four. Unit days: K to 2, 3 to 5
  and 6 to 8 are 60 a year in units (192 days with checks and respond days); 9 to 12 is 156 a level in units, 640 in
  all. `python -X utf8 scripts/stale.py check`: 0 failures.
- My own scripted check across the four frames: each frame owns exactly 63 ids, no id is owned twice in a frame or
  across frames, each unit's ids equal its skill rows' standards, and every owned id appears in its unit's learning
  cell and its end-of-unit evidence cell.

## Verdict

| Frame | Verdict | Biggest issue |
|---|---|---|
| K to 2 | Sound; ready after a light fix pass | Stale For the lead notes; the unit 12 hoop dance move task |
| 3 to 5 | Sound; ready after a light fix pass | Check-day minutes run over the session; a stale PE pick list |
| 6 to 8 | Sound; ready after a light fix pass | Capoeira is in both dance and PE but the frame says it is not; stale notes |
| 9 to 12 | Sound; ready after a light fix pass | The 1895 serpentine film repeats from K to 2; PE 9 to 12 unit 5 teaches choreography |

All four frames place every owned id once, test each id by id, add up on the full, once-a-week and short paths, and
meet arts.csv at both ends of every seam. The models, the safety rules and the sensitivity handling are strong and
consistent. No finding is serious. The one change that matters most is the boundary with physical education at
9 to 12 (finding 4); second, the repeated serpentine film and the capoeira naming, which break the frames' own
"no repeat" claims.

## Findings, most serious first

### 1. Stale For the lead notes in all four frames (moderate)

LAYER process. REPEAT yes (stale notes, as in the visual arts K to 2 read, finding 5). Confidence: firm (checked
against arts.csv and the PE frames as they stand).

**What is wrong.** Several notes describe work that has since landed:

- K to 2 item 3, 3 to 5 item 3 and 6 to 8 item 3 say the row changes "are in the writer's final message". All of
  them are in arts.csv now (commit 1a6b4e314): da-k-technique, da-g2-elements, da-g2-technique, da-g1-connect,
  da-g2-connect; da-g3-elements, da-g3-connect, da-g4-elements, da-g4-technique, da-g4-connect, da-g4-revise,
  da-g5-elements and the "labeled" fix in da-g3-stage; da-g6-elements, da-g6-technique, da-g8-respond and the
  Assessed-by notes of da-g6, g7 and g8 technique and connect.
- K to 2, the brief text near lines 52 to 55 and the unit 1 and unit 9 cells, still carry "(For the lead)" notes
  about narrower rows. Those rows are now full.
- K to 2 item 2, 3 to 5 item 2, 6 to 8 item 2 and 9 to 12 item 6 ask PE to fill pending cross-subject cells. The PE
  frames have already replaced those cells.
- K to 2 near line 229: "The grade 3 to 5 frame is not written yet." 6 to 8 near line 262: the grade 9 to 12 frame
  "is being written beside this one." Both are written.
- 9 to 12 seam table, da-g8-respond: "time-stamped evidence". The row now says time-stamped or moment-named.

**Fix.** Rewrite each as done, in one line, or drop it; change the 9 to 12 seam cell to "time-stamped or
moment-named". For the lead, outside these frames: PE K to 2 near line 287 still says the dance K to 2 frame is not
written, and PE 9 to 12 near line 377 says the dance and SEL 9 to 12 frames are not written.

### 2. The same 1895 film is used in two bands, under two names (moderate)

LAYER frame. REPEAT no. Confidence: firm (same title, year and source).

**What is wrong.** K to 2 unit 1 shows "Annabelle Moore, Annabelle Serpentine Dance (1895, LoC)". The 9 to 12 Level 1
bridge (unit 1) uses "Annabelle Whitford, Annabelle Serpentine Dance (1895)". This is one performer (Annabelle
Whitford Moore) and one film. The 9 to 12 frame states that none of its works repeats a dance named in Dance K to 2,
and 9 to 12 unit 10 also shows a public domain serpentine dance film from the LoC, so the high school course meets
the same dance twice and K to 2 a third time.

**Fix.** Swap the 9 to 12 bridge work for another early film not used in K to 2 (a Fuller-school or other
public domain dance film), or keep it and name it as a deliberate review in 9 to 12 For the lead item 9 ("seen in
K to 2 as a picture of movement, now read as a staging problem"). Either way, use one name for the dancer across
the bands: "Annabelle Whitford Moore" once, then "Annabelle".

### 3. Capoeira is taught in both dance 6 to 8 and PE 6 to 8, but the dance frame says it is not (moderate)

LAYER frame. REPEAT no. Confidence: firm.

**What is wrong.** Dance 6 to 8 unit 8 (grade 7) studies capoeira. PE 6 to 8 unit 22 (grade 8) moves the ginga and
retrieves the dance study, and PE For the lead item 3 says it is "named both ways". The dance frame says none of its
picks repeats a PE 6 to 8 dance and lists PE's picks as "tinikling, kolo, a line dance" (near lines 67 and 363). The
PE fix pass replaced tinikling with cumbia, and the dance frame never names PE's capoeira.

**Fix.** In the dance 6 to 8 Cross-subject table add a row: PE 6 to 8 unit 22 moves the ginga as a motor pattern in
grade 8 and retrieves this unit's study; dance owns the cultural setting, the roda and the response. Correct the PE
pick list to "cumbia, kolo and a line dance", and drop "none repeats" for capoeira.

### 4. The PE and dance boundary is crossed at 9 to 12, and partly at 6 to 8 (moderate)

LAYER frame (dance cross-subject lines) and process (PE wording, for the lead). REPEAT no. Confidence: likely (the
SHAPE high school outcomes do ask for composed dance, so part of this is a standard choice, see the judgment call).

**What is wrong.** STANDARD 6 says PE teaches dance sequences as motor skill and "does not teach choreography,
performing for an audience or response", and the arts lens names "a dance unit that double-teaches what PE teaches"
as an error. PE 9 to 12 unit 5 "Dance by design" asks "can I design a phrase that says something?", and students
design an original phrase with a stated idea, a motif and a transition, then join a canon and a call and response.
That is choreography with intent. Dance 9 to 12 names PE only in unit 2, but the overlap is with Level 1 unit 3
(making: structure serves purpose). Smaller, at 6 to 8: PE unit 13 uses canon and contrast to change a dance, while
dance 6 to 8 unit 2 teaches canon as a choreographic tool in grade 6.

**Fix.** In dance 9 to 12 unit 3's connections line, name PE 9 to 12 unit 5 and state the line: PE designs a sequence
as a movement problem (counts, transitions, form as structure, done for fitness and skill); dance teaches intent,
motif and choreographic tools, and the response. Add the same line to dance 6 to 8 unit 2 for PE unit 13. For the
lead: PE 9 to 12 unit 5's question "says something" and its "stated idea" step belong to dance; PE can keep the
phrase design with a movement goal.

### 5. K to 2 unit 12: DA:Cn10.1.2b asks children to move from the hoop dance, which the frame says no child imitates (moderate)

LAYER frame. REPEAT no. Confidence: likely (sensitivity read not yet run).

**What is wrong.** Unit 12 shows a hoop dance "watched only ... no child imitates it", a sound rule for a
ceremonial-rooted Indigenous form. But the unit's id DA:Cn10.1.2b asks students to pose questions about a dance and
then "move from the answers", and the evidence line pins that task to the hoop dance.

**Fix.** Use Kpanlogo (already in the unit) or another open social dance for the question-and-move task, and keep
the hoop dance for the Cn11 talk only (where and why it is danced, who teaches it). Second choice: limit the move to
drawing the hoop's shapes in the air with arms, no hoop steps, and have the sensitivity read confirm it.

### 6. "travelling" in the da-g2-technique row (minor)

LAYER progression. REPEAT yes (US spelling sweep). Confidence: firm.

**What is wrong.** The row says "Perform travelling". **Fix.** "traveling". The row changes of today all landed;
this is the one leftover.

### 7. 3 to 5 course-level check days run past 40 minutes (minor)

LAYER frame. REPEAT no. Confidence: likely (my arithmetic from the frame's own minutes).

**What is wrong.** The check-day plan: set-up 3, warm-up 5, written part 10, showing 6 groups of 3 minutes (18),
cool-down 4 and room reset 3, about 43 minutes in a 40-minute session. Grades 4 and 5 mid-year showings also put four
look-fors into a group turn of about 3 minutes, which is hard to score.

**Fix.** On check days cut the warm-up to 2 minutes and the room reset into the cool-down, or keep 4-minute turns
with two look-fors each and score the other two from the written part.

### 8. Range claims that are not exact (minor)

LAYER frame. REPEAT no. Confidence: firm.

**What is wrong.** 6 to 8 says the 3 to 5 makers "come back only through other makers", but Trisha Brown (3 to 5
units 3 and 12) returns in Grand Union (6 to 8 unit 10). 9 to 12 For the lead item 9 lists the works that repeat from
earlier bands but omits Swan Lake (K to 2 uses Ivanov's Little Swans; 9 to 12 uses Dada Masilo's Swan Lake) and
Germaine Acogny and the Ecole des Sables (3 to 5 unit 1; 9 to 12 unit 9).

**Fix.** Add the three to the repeat lists, each named as a deliberate return (the pairs are good teaching).

### 9. 3 to 5 PE pick list is out of date (minor)

LAYER frame. REPEAT no (same kind as finding 3). Confidence: firm.

**What is wrong.** Near line 81 the frame lists tinikling among PE 3 to 5's dances. PE 3 to 5 never used it in its
current frame and now has Pilolo, which is a game. **Fix.** Correct the list to what PE 3 to 5 names now.

### 10. Agent read labels differ across the four frames (minor)

LAYER frame. REPEAT no. Confidence: firm.

**What is wrong.** "safety (moving)" in K to 2 and 3 to 5, "safety (hands-on)" in 6 to 8, "safety (moving unit)" in
9 to 12. **Fix.** Use the label from the sensitivity and safety read brief in all four.

### 11. PE picks that repeat across PE bands (minor, for the lead)

LAYER frame (PE). REPEAT no. Confidence: firm.

**What is wrong.** The Virginia reel is in PE 3 to 5 and PE 9 to 12 unit 5; PE 6 to 8 dropped it for that reason.
**Fix.** PE's to change; listed here because the brief asks for picks repeated across dance and PE bands.

### 12. Two Mexican folk dances in grade 1, in two subjects (judgment call)

LAYER frame. REPEAT no. Confidence: speculative.

PE K to 2 grade 1 unit 13 dances La Raspa; dance K to 2 grade 1 unit 5 studies Ballet Folklorico. They are not the
same work and the angles differ (motor pattern against regional style and costume). Choice: leave both and have each
frame name the other in one cross-subject line, or swap one. I would name both ways.

### Other judgment calls (keep as written)

- 3 to 5 pairs connecting with ideas and revising with staging, which differs from K to 2's pairing. It is reasoned
  in the frame; keep it.
- Kpanlogo twice in K to 2 (units 7 and 12) is deliberate and named; keep.
- Sankai Juku in 6 to 8 units 1 and 5 and again in 9 to 12 is acknowledged; keep.
- Level 4 seniors' checkpoints in week 28 (before senior exits); keep.

## Course-level check clashes (listed, not counted)

For the lead's calendar pass. These are not findings.

| Frame | Clashes |
|---|---|
| K to 2 | Year K week 18 (ELD, PE, visual arts); year K week 26 (SEL, visual arts); grade 1 weeks 17 and 25 (music); grade 2 week 17 (ELD, music, PE, theater, visual arts) and week 25 (music) |
| 3 to 5 | PE checks in weeks 18 and 26 in all three grades meet dance's year 5 week 18 and week 26 in every year; grade 4 week 27 respond day meets the social studies year-end check on the once-a-week path |
| 6 to 8 | Week 17 mid-year with health and PE (their day 84 sits between dance's 83 and 85); year-end week 32 is a core check week in the frame's own avoid list but is placed there under finals stagger rule 3; once-a-week respond week 18 meets science (grade 6) and ELA (grade 8) |
| 9 to 12 | Weeks 17 and 32 (finals); Level 4 weeks 15 and 28 |

## Settled by the expert

| Item | Settled as |
|---|---|
| The serpentine dancer's name | "Annabelle Whitford Moore" on first use in every band, then "Annabelle" |
| The 9 to 12 bridge work | Replace with an early film not used in K to 2; if the writer keeps it, it is named as review |
| K to 2 unit 12 move source | Kpanlogo carries the Cn10.1.2b question-and-move task; the hoop dance stays watch-and-talk |
| The PE and dance line | PE designs sequences as a movement problem; dance owns intent, motif, choreographic tools and response |
| 3 to 5 check-day minutes | Warm-up 2 minutes on check days; room reset folded into the cool-down |
| Repeat lists | Swan Lake, Acogny and the Ecole des Sables, and Trisha Brown named as deliberate returns |

## For Cory

Scope, money and people only.

- **The filmed set of unseen phrases.** All four frames assume a library of short filmed phrases the class has not
  seen, for respond checks. Someone has to dance and film them (people), or they are licensed (money).
- **Supplies ceilings.** $50 a class a year for the K to 8 bands; $75 a level for 9 to 12. Stated in the frames;
  worth a yes.
- **Level 4 has no short path.** Schools on a semester or 80-day schedule can take Levels 1 to 3 short but not
  Level 4. A scope choice; I would leave it.

## What is right and should not be touched

- Every one of the 63 ids in each frame is owned once and tested id by id in its unit's evidence.
- The days add up on every path: 64 a year (60 in units) and the 32-session once-a-week path for K to 8; 160 a
  level, the 80-day short path, the Level 1 bridge (12 days at most) and the Level 2 and 3 reviews (6 days at most)
  for 9 to 12.
- The seams meet arts.csv at both ends, with day-2 retrieval and ten-minute reteaches at grade 3 and Level 1.
- The models carried through the bands (body, action, space, time, energy; the choreographic tools; the respond
  frame) are consistent.
- Safety (floor, footwear, spacing, consent for touch and lifts) and sensitivity (watch-only for sacred or
  ceremonial forms, makers named in their own words) are strong.
- The science lean in 3 to 5 is timed after science teaches the topic (energy and waves in grade 4 units 1 to 3,
  matter in grade 5).

## Sources

All repository files listed under "What I read". No web pages were opened. I would want these opened in a browser at
the fix pass:

- The national dance standards text for 3 to 5 and 9 to 12 at nationalartsstandards.org (wording of Cn10.1.2b and the
  high school levels).
- The dance association's high school opportunity-to-learn lines (download approved by Cory 2026-11-21, Desk
  q-fix-downloads-1; not run in this read).
- UNESCO's kolo and capoeira pages (bot wall: browser check).
- The Library of Congress item afcreed000072 (403: browser check).

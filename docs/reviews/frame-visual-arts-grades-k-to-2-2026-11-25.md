# Frame read: Visual Arts, grades K to 2 (2026-11-25)

Expert cold read of docs/courses/visual-arts-grades-k-to-2/frame.md, the arts pilot frame, under
docs/pipeline/briefs/frame-read.md with the after-core changes. I did not write the frame.

## What I read

- The frame in full; its row in data/plans/frames.csv (line 63: 12 units, 192 days, 40 minutes, 2 a week, 96 weeks over
  three years); its rows in data/plans/calendar.csv (lines 870 to 893); its catalogue row in data/plans/course-list.csv
  (`grade:K|1|2&strand:va`).
- The 24 progression rows for va-k, va-g1 and va-g2 in data/progressions/arts.csv, and the va-g3 rows they hand to.
- The 45 owned ids' lines in data/standards/ncas-performance-standards-words.txt.
- The bar: docs/ADOPTION-BAR-SUBJECTS.md (shared core C1 to C16, arts part 2, the arts row of "Before a scope and
  sequence"); docs/courses/arts/STANDARD.md and APPROACH.md in full; docs/agents/lenses/arts.md; docs/agents/EXPERT.md.
- docs/pipeline/briefs/frame-write.md, its lessons and its last section "After-core courses (added 2026-11-25)".
- Every DESK-ANSWERS.md entry naming arts (2026-11-16, 11-20, 11-21 three entries, 11-25 band frames).
- docs/courses/CALENDAR.md; the core frames leaned on, at their Units tables only (math-kindergarten,
  social-studies-kindergarten, social-studies-grade-2).
- Earlier arts reads (prework-arts-*, the two progression reads) and earlier frame reads, for REPEAT tags.
- The gates: `python -X utf8 scripts/frame.py check visual-arts-grades-k-to-2` passes (0 failures; unit days by year K
  60, 1 60, 2 60; 192 days, 180 in units, 12 for checks and respond days). `scripts/stale.py check` passes (70 files,
  0 failures). `scripts/frame.py calendar` reports this course in six stagger clashes (finding 2). The scripts/frame.py
  calendar and stagger code (lines 385 to 440) was read to see how band years are mapped.

There is no course before (kindergarten opens the subject) and no base text. The course after,
visual-arts-grades-3-to-5, has no frame yet, so the hand-on was read against the va-g3 progression rows.

## Verdict

The frame is sound in shape and is a good pilot: all 45 ids are placed once in their own year (15 a year), every
unit makes, studies another artist's work with its setting and shows, technique climbs year on year, the days add up
on both paths, and safety, rights and sensitive ground are handled with care. The biggest risk is in what the other 19
arts frames would copy: each unit's end-of-unit evidence names two items that follow the progression rows' "Assessed
by" lines, which leaves 9 of the 45 ids with no item and 3 more with an item that does not test them, so as written
the course fails the C1 door. The one change that matters most is an id-by-id evidence line in every unit; second,
the check weeks clash with ELD, PE and SEL in every grade, and the stagger the frame proposes for the arts ignores the
other after-core courses.

## Findings, most serious first

### 1. Twelve owned ids have no end-of-unit item that tests them (serious)

LAYER frame. REPEAT yes (taught or checked only in part, as in earlier frame reads such as
docs/reviews/frame-social-studies-grade-3-2026-11-13.md). Confidence: firm (C1 and APPROACH say the same).

**What is wrong.** Each unit's "End-of-unit evidence" names two items, one per progression row, copied from the rows'
"Assessed by" notes. A row owns two to four ids, so the other ids get no item, and the course-level checks do not
fill the gap (they sample, by lesson 20, and never sample the exhibit units). Traced against the words file:

| Unit | Id with no item | Id with an item that does not test it |
|---|---|---|
| 1 | | VA:Re7.1.Ka (name where art appears around you): the unit's talk and the mid-year check use an unseen picture, which tests Re7.2.Ka only. VA:Cr2.2.Ka: see finding 4 |
| 2 | VA:Cr1.2.Ka (work with others on an art problem: the partner bridge is shown, never scored) | |
| 4 | VA:Pr5.1.Ka (why people keep a collection); VA:Pr6.1.Ka (museum against an ordinary building) | |
| 5 | | VA:Re7.1.1a (pick and describe works of everyday life): the talk and the mid-year check compare two pictures, which is Re7.2.1a |
| 6 | VA:Cr1.1.1a (explore materials with classmates) | |
| 7 | VA:Cn10.1.1a (times, places and reasons for art beyond school) | |
| 8 | VA:Pr5.1.1a (when, where, how to ready a work); VA:Pr6.1.1a (museum jobs) | |
| 9 | | VA:Re7.1.2a (look and feel of surroundings): the talk and the mid-year check sort pictures, which is Re7.2.2a |
| 10 | VA:Cr1.2.2a (follow your own question into a made work) | |
| 12 | VA:Pr5.1.2a (tell apart mounting, labels and frames) | |

**Why it matters.** C1 is a door: "any standard lacks ... a check item" fails the course unread. APPROACH "What the arts
carry" says every part has an end-of-unit item. The scope writer copies this cell, and the other arts frames will copy
its two-item form, so the gap would spread to all 20 arts courses (and is worst in the presenting ids, which every
discipline has).

**Fix.** In every unit, write the end-of-unit evidence id by id: each id names the item or the guide line that
carries it. Most need no new day, only a named look-for or a one-question talk item, for example: unit 1 adds a talk
item "name two places in our school where you saw art" from the looking-walk photo cards (Re7.1.Ka); unit 2's showing
guide gets a look-for "worked with the partner on the bridge" (Cr1.2.Ka); unit 4's talk adds "why do people keep a
collection?" and a museum, store or house picture sort (Pr5.1.Ka, Pr6.1.Ka); unit 5's talk adds "pick a picture of
everyday life and tell your partner about it" (Re7.1.1a); unit 6's sketchbook check adds a shared-table look-for
(Cr1.1.1a); unit 7's talk adds one reason people make art outside school (Cn10.1.1a); unit 8 scores the exhibit-plan
card (Pr5.1.1a) and the job-card sort (Pr6.1.1a); unit 9's talk adds the walk ("tell how the playground looks and
feels", Re7.1.2a); unit 10's sketchbook check adds "your own question on the page" (Cr1.2.2a); unit 12's guide adds
"named the mount, the label and the frame" (Pr5.1.2a). Then fix the mid-year checks' id lists so a check names only
the ids its task tests (Re7.1 out of the three unseen-picture talks, or a walk-photo item added). Add one sentence to
the brief bullet "Scored evidence": "Every owned id has an end-of-unit item or a look-for on the unit's guide, named
in the unit's evidence line." Other arts frames copy that sentence, not the two-item form.

### 2. The check weeks clash with other after-core courses in every grade, and the proposed arts stagger ignores them (serious)

LAYER frame and process. REPEAT new (the first after-core stagger read). Confidence: firm for the clashes (the gate
prints them), a judgment call for the rule.

**What is wrong.** The frame places its checks clear of the core check weeks, as frame-write's after-core section asks,
and the stated core weeks are right for every grade (checked against calendar.csv). But `frame.py calendar` now reads
the band years under their grades and prints six clashes with this course in them: grade K and grade 1 week 18 (arts,
ELD, PE), grade 2 week 17 (arts, ELD, PE), and week 26 in all three grades (arts, SEL). CALENDAR.md's stagger rule 1
("K to 5, one teacher: no school week holds the course-level check days of two subjects") is broken. For the lead item
3 then proposes staggering only the five K to 2 arts (music 12 and 25, theater 13 and 24, dance 21 and 23, media arts
11 and 27), and several of those weeks are already taken by after-core checks: media arts 11 with SEL K, music 12
with health K and computer science K, theater 13 with library K, media arts 27 with health, computer science and
library K. The gate's stagger check groups by subject, and all five disciplines are subject `arts`, so clashes between
two arts courses would never be flagged (scripts/frame.py `clashes`, keyed on `r['subject']`). Dance's 21 and 23 would
also put a "year-end" check nine weeks before the year ends.

**Why it matters.** The frame's own premise is that "the teacher needs no art training", that is, a classroom teacher
may teach it, the same adult who runs ELD and SEL checks. This is the pilot: the next four arts K to 2 frames will copy
item 3's weeks and add more clashes.

**Fix.** The lead rules once, for all after-core courses, whether stagger rule 1 binds between after-core subjects in
K to 5 (my pick: yes in K to 2, where one classroom teacher is the common case; frame-write's after-core section then
says so). If it binds, write one K to 2 after-core stagger table covering the five arts, PE, ELD, SEL, health,
computer science and library, not an arts-only one. Today the weeks free of every check in all three grades are 1 to 8
and 21 to 25. For this course: pin the year-end check to week 25 with CALENDAR.md tool (a) (course days 49 and 50 of
each year, the exhibit unit then starts a week earlier), and either move the mid-year check by a pin to week 21 or
move ELD or PE off weeks 17 and 18. Ask the frame.py worker to key the stagger check on course for the arts
disciplines (or on discipline), so two arts courses in one week are flagged. Replace For the lead item 3 with the
table's outcome.

### 3. The unit check day does not fit 40 minutes and holds two jobs one adult cannot do at once (moderate)

LAYER frame. REPEAT new. Confidence: likely (arithmetic from the frame's own minutes; lesson 19).

**What is wrong.** The brief bullet "Scored evidence" puts on one check day: the showing scored on the guide with each
child's self-check first, plus talk items heard in groups of five for about five minutes each. Six groups take 30
minutes; with 5 minutes of set-up and 4 to 7 of clean-up that is 39 to 42 minutes before any showing is scored. In units
1, 5 and 9 the check is a performance check (each child handles a tool safely, "watched in rotating groups") while the
teacher sits at the talk table. Frame-write lesson 19 says an end day holds at most one full performance. The
course-level check days (six groups of four minutes, 24 minutes) fit; the unit days do not.

**Why it matters.** A busy teacher will either skip children's talk items or mark safe handling without watching it,
and the second is a safety mark.

**Fix.** Units 1, 5 and 9: observe the safe-handling performance on the rotating list during the last two making days
(the APPROACH "performing day" form) and record it on the record sheet; the check day keeps the talk items and the
self-check. Every unit: say that the showing is scored from the kept work after the session, so the check day's 40
minutes hold only set-up, the self-check, the six talk groups and clean-up. State those minutes in the bullet.

### 4. VA:Cr2.2.Ka is assessed as handling a tool, which is grade 1's id (moderate)

LAYER frame and progression. REPEAT new. Confidence: firm (the words file lines differ).

**What is wrong.** The words file has VA:Cr2.2.Ka as picking out safe, non-toxic supplies, tools and equipment, and
VA:Cr2.2.1a as showing the safe way to handle them. Unit 1 teaches the pick (the label check on the box), but its
evidence is "each child handles one tool safely", and the K mid-year check scores "a tool picked and handled safely".
The va-k-craft row's "Assessed by" note says the same, which is where the frame took it from.

**Why it matters.** Year K then claims an id it never tests and tests grade 1's id a year early (the band-year rule,
STANDARD.md 3.1; the lens's first scope error).

**Fix.** Unit 1's item for VA:Cr2.2.Ka is a safe-supply sort: each child picks the safe items from a tray or picture
cards (labeled non-toxic against unlabeled, a blunt against a sharp tool) and says why. Handling stays as practice. The
mid-year check's making task says "picks the safe supplies for the task". The progression fixer changes va-k-craft's
"Assessed by" note to the same (both ends).

### 5. Stale notes the gate does not catch (moderate)

LAYER process. REPEAT yes (earlier frame reads logged stale notes). Confidence: firm.

- The frame's "Standard" bullet: "Until the standards gate exists (data/plans/later.csv L83), each year's scope and
  sequence states its id count (15) against STANDARD.md 3.2 and a reader spot-checks ten." L83 is done (2026-11-21):
  scripts/standards.py checks every NCAS id against the id file. Fix: "scripts/standards.py checks every id against
  the id file (L83, done 2026-11-21); each year's scope and sequence still states its id count (15)."
- For the lead item 4 says `frame.py calendar` and the stagger check do not see these checks against the core grades.
  They do now (scripts/frame.py lines 393 to 399; calendar.csv rows carry grades K, 1 and 2, and the clashes print).
  Fix: drop item 4, or replace it with the subject-key point in finding 2.
- Outside this frame, same kind: docs/courses/arts/STANDARD.md section 1 still says scripts/standards.py "does not
  check that an id exists" and that the gate is "owed"; the arts row of "Before a scope and sequence" in
  docs/ADOPTION-BAR-SUBJECTS.md still lists "Owed: the standards gate (later.csv L83)" and "load the 63 strand ids
  when the high school music frame is written" (loaded 2026-11-21, STANDARD.md 3.3). Fix: rewrite both notes as done.

### 6. The once-a-week path's claim about check weeks is only half true (minor)

LAYER frame. REPEAT new. Confidence: firm (arithmetic).

On the 32-session path, session n is week n. Year 1: units 5 and 6 take 9 and 8 sessions, so the check is session 18
(week 18) and its respond session 19 falls in week 19, grade 1 math's mid-year check week. Year 2: 8 and 8 sessions,
check in week 17, respond in week 18, inside grade 2 math's check weeks 18 to 19. The year-end checks land in week 26
with respond in week 27. Respond days are not checks, so no rule breaks, but "the checks then fall in the same weeks"
reads as covering the respond day. Fix: "the check sessions fall in the same weeks as on the full path; the respond
sessions fall one week later (weeks 19, 18 and 27)". Re-check once finding 2 moves the weeks.

### 7. "The four kindergarten threads" names eight (minor)

LAYER frame. REPEAT new. Confidence: firm. Seams, "Picked up from the course before": "The four kindergarten threads
that start here ... are" followed by eight rows. Fix: "The eight kindergarten threads".

### 8. Two works need a precise title or a teacher note (minor)

LAYER frame. REPEAT new. Confidence: firm (read at source).

- The Guggenheim's record titles the quilt "Woman on a Bridge #1 of 5: Tar Beach" (1988, accession 88.3620); "Tar
  Beach" alone is also the 1991 picture book and the 1990 Tar Beach 2 at the Pennsylvania Academy. Fix: use the
  museum's title in unit 3, so the unit plan links the right object.
- The Met's page on El Anatsui's Between Earth and Heaven (2006, accession 2007.96) says the caps are from liquor
  bottles from Nigerian distilleries and ties them to the alcohol trade between Africa and Europe. For grade 2 this is
  a teacher note, not a reason to drop the work. Fix: add to unit 11's sensitivity cell "the caps are liquor bottle caps;
  the unit says 'bottle caps' and tells the reuse, the sensitivity agent reads the Met's page first".

### 9. The works lean on one print tradition and skip Indigenous American art (minor, a judgment call)

LAYER frame. REPEAT new. Confidence: judgment call.

Each year meets the bar's range rule (more than one region and period, living makers each year), and the frame flags
the open-access lean itself. Still, a Japanese woodblock print anchors every year (Hokusai, Utamaro, Hiroshige), year K
has nothing from Africa or Latin America, and the band has no Native American work. Fix: make year K's "Candidate"
(a plain-subject work from Africa or the Americas) a pick in the frame, and add one Native American work in the band
(a made-to-use object fits unit 7's useful-things slot), read by the sensitivity agent under the sacred or ceremonial
rule. Other arts frames should range-check across the band, not only within each year.

## The data the brief asks for

- **Owned skills.** All 24 va rows for K, 1 and 2 are placed once, in the unit of their own year (frame.py checks
  this). No unit teaches another grade's skill except as named retrieval. Met.
- **Standards in full.** All 45 ids are taught in their own year (15 a year, STANDARD.md 3.2), each with a line of
  action in the unit's cell. Taught in full: met. Checked in full: not met (findings 1 and 4).
- **Units and reasons.** Each "Why this unit, here" holds: the studio and looking routine first, ideas next, making and
  judging next, the exhibit last because it draws on the year's kept work. No model is used before it is introduced
  (exhibit-plan and work-card begin in unit 8; the teacher's simpler work card from unit 1 is named as such). Met.
- **Days.** 64 a year: 60 in units (18, 16, 14, 12 in years K and 1; 16, 16, 16, 12 in year 2), 2 check days, 2
  respond days. Two 40-minute sessions over 32 weeks, as STANDARD.md 3.4 sets. Unit shares follow the ids and the
  set-up load; none is far over or under. The calendar rows match the stated weeks exactly (course day n in week
  ceil(n / 2): days 35 and 36 in week 18, 33 and 34 in week 17, 51 and 52 in week 26). Met.
- **Source map.** No base text. Not applicable.
- **Seams.** The year to year table matches every row's `assumes` and the day spans in calendar.csv. The hand-on to
  grade 3 matches all eight va-g3 rows' `assumes` and model_in, and the va-g3 descriptions in the table are faithful.
  Met (wording slip in finding 7).
- **Cross-subject.** No va K to 2 row has a cross_subject lean. The practiced contacts hold: kindergarten math's flat
  shapes are its unit 3 (weeks 9 to 13 on calendar.csv), after art unit 1, and the frame gives the "if later" line;
  sorting is in kindergarten math unit 2 (mk-sort-count); social studies kindergarten unit 3 is "Where things are" and
  grade 2 unit 6 is "Family stories and culture", as named. Met.
- **Stale notes.** stale.py passes; three unmarked stale notes found (finding 5).

## Lens checklist (course frame layer)

| Lens line | Result |
|---|---|
| A grade's ids in the wrong year of the band | Met: each year claims only its grade (finding 4 is about the item, not the claim) |
| A year with one artistic process missing | Met: every year has all four, every unit at least two |
| Works all from one tradition or one century | Met, with the lean in finding 9 |
| Technique does not get harder across units or years | Met: the "Techniques that get harder" bullet climbs in all four strands |
| A plan that needs a daily period in K to 8 | Met: two sessions a week, and a once-a-week path that keeps every unit |
| No showing in a unit | Met: every unit names its showing and audience |
| A making task with no technique taught first | Met at frame level: each unit names its technique and step cards |
| Response work with no discipline words | Met: three to six words a unit, art words from year 1 |
| A work studied with no setting | Met: maker, place, date, holder and purpose for each work; the teacher's work card from unit 1 |
| Critique with no protocol; no revision | Met: describe, ask, suggest on the second making day, revision the next day |
| End-of-unit assessment that is a vocabulary quiz | Met: showings, products, performance checks and talks |
| Copies the coalition's enduring understandings or cornerstone tasks | Met: own questions and checks |
| Set-up and clean-up that do not fit the session | Missed on the unit check day (finding 3); met elsewhere |
| Equipment the room may not have | Met: free path per unit, costs stated |
| Unsafe use of space (blades, heat, fumes) | Met: adult-only blades, no heat, no powders, the two guides named |
| "Respond" used for the artistic process on a respond day | Met: the frame says so twice |
| A tool asked to judge a finished work | Met: tools only show and give practice |
| The five disciplines planned as one | Met for this frame; For the lead items 1, 2 and 7 to 10 ask others to copy form, not content |

## Facts spot-checked at source

| Fact in the frame | Holds? | Source |
|---|---|---|
| Kandinsky, Improvisation 27 (Garden of Love II), 1912, the Met, open access | Holds (accession 49.70.1, Open Access image) | metmuseum.org/art/collection/search/488319 |
| Faience hippopotamus "William", Middle Kingdom, about 1961 to 1878 BCE, the Met, made for a tomb | Holds (17.9.1, from a shaft of the steward Senbi's tomb at Meir) | metmuseum.org/art/collection/search/544227 |
| Hiroshige, Sudden Shower over Shin-Ohashi Bridge and Atake, 1857, Brooklyn Museum, open | Holds (two impressions; the museum allows download and use with credit) | brooklynmuseum.org/opencollection/objects/121666 |
| Ringgold, Tar Beach, 1988, Guggenheim | Holds, with the full title in finding 8 | guggenheim.org (press kit, 2025) |
| El Anatsui, Between Earth and Heaven, 2006, the Met, flattened bottle tops; born 1944 in Ghana | Holds, with the note in finding 8 | metmuseum.org/art/collection/search/319872 |
| The federal consumer product safety agency's "Art and Craft Safety Guide" | Holds (publication 5015, written with the art materials institute and the national art education association) | cpsc.gov/s3fs-public/5015.pdf |
| California's environmental health hazard office's list of art materials not to buy for K to 6 | Holds (Education Code 32064 and 32066; the list is updated, 2025 edition) | oehha.ca.gov/risk-assessment/art-hazards |

From memory, not opened: Cassatt's The Child's Bath at the Art Institute of Chicago (CC0), Dürer's Young Hare at the
Albertina, Monet's bridge and Bruegel's The Harvesters at the Met, Chinese paper-cut on the UNESCO list since 2009,
Cloud Gate completed 2006, Asawa's wartime camp years, alebrijes' Mexico City start. None looked wrong; the unit plans
check each rights line as the frame says.

## The pilot pattern: what the other arts frames should and should not copy

**Copy:**
- The four-unit year with two threads a unit in the same slot each year, where the discipline's rows pair that way,
  and the Year column with units numbered through the band.
- The "Inside the band: year to year" seams table with each row's last use and course days.
- The exhibit or performance unit last, assessed by its own showing, after the year-end check (CALENDAR.md tool c).
- The once-a-week path stated per unit with its session counts, and the four things it keeps.
- Works named with maker, place, date, holder and purpose, rights checked by the unit plan, living status recorded
  "as of its date"; sensitive works named with the communities and the sources the agent reads first.
- The safety bullet naming the two guides and the per-unit hazards and controls cell; the leave-out bullet naming
  units; the supplies cost per unit with a free path; the four-line logic model; the "Processes, anchors and works"
  heading for the C3 column.

**Do not copy:**
- The two-item end-of-unit evidence line (finding 1). Copy an id-by-id line instead.
- Check weeks 18 or 17 and 26, or For the lead item 3's arts-only stagger (finding 2). Wait for the K to 2 after-core
  stagger table.
- A unit check day that holds a performance check and six talk groups (finding 3).
- The "Until the standards gate exists" line and For the lead item 4 (finding 5).
- The progression rows' "Assessed by" notes taken as the unit's whole evidence: they name one form per row, not one
  item per id.

## What is right and should not be touched

The band-year claim (15 ids a year, no pre-kindergarten id), the clean day 1 with retrieval in day 2's opener, the
mixed-class note with the reteach when a child meets year 2 first, the invented or public option on every own-life
task, the burial and ceremonial objects studied by looking only, the family's yes and chosen name for any showing
outside class, and the paper path with no student device. The days and weeks are right as arithmetic.

## What I could not judge

Whether Yayoi Kusama is living as of today (past my sources; the frame rightly leaves it to the unit plan). Whether the
supply costs are realistic: they are planning figures and were not priced. Whether the K critique routine (describe,
ask, suggest) works with five-year-olds in every unit: plausible with the picture frames given, untested.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| VA:Cr2.2.Ka's item is a safe-supply pick (tray or picture cards, labeled against unlabeled, blunt against sharp), handling stays practice | The id's action is picking; handling is grade 1's id | frame.md unit 1 and year K mid-year check; data/progressions/arts.csv va-k-craft notes |
| The per-id items listed under finding 1 (a talk question, a guide look-for or a scored card for each missing id) | Item-level choices inside each id's words line; no new days | frame.md units 1, 2, 4 to 10, 12 and the three mid-year checks |
| Safe handling in units 1, 5 and 9 observed on the rotating list in the last two making days; the showing scored from kept work after the session | Fits the 40 minutes and lesson 19 with no day added | frame.md brief "Scored evidence" and units 1, 5, 9 |
| "four" becomes "eight" in the Seams sentence | Plain count | frame.md Seams |
| Unit 3 uses the museum's title "Woman on a Bridge #1 of 5: Tar Beach"; unit 11 adds the liquor-cap teacher note | Read at source | frame.md units 3 and 11 |

The check weeks (finding 2) are the lead's call under CALENDAR.md, not an item-level choice.

## For Cory

- Money: the frame's provisional supply costs ($70, $50 and $40 a class of 30 a year, all optional beside a free path)
  and its pick of a $75 ceiling a class a year for K to 2 visual arts. I agree with the pick; it is yours to set.

## For the source list

- The Guggenheim's 2025 Faith Ringgold press kit (guggenheim.org/wp-content/uploads/2025/05/Faith-Ringgold-Press-Kit-Full.pdf):
  the quilt's full title and accession.
- California's environmental health hazard office art hazards page (oehha.ca.gov/risk-assessment/art-hazards) and its
  2025 list: the K to 6 do-not-buy list the safety read opens.
- The federal consumer product safety agency's Art and Craft Safety Guide, publication 5015 (cpsc.gov/s3fs-public/5015.pdf).

## Sources

- https://www.metmuseum.org/art/collection/search/488319 : Kandinsky's date, holder and open access line.
- https://www.metmuseum.org/art/collection/search/544227 : William's date, findspot and burial use.
- https://www.brooklynmuseum.org/opencollection/objects/121666 : Hiroshige's print, date and use terms.
- https://www.guggenheim.org/wp-content/uploads/2025/05/Faith-Ringgold-Press-Kit-Full.pdf : Tar Beach's title and accession.
- https://www.metmuseum.org/art/collection/search/319872 : El Anatsui's work, date and material.
- https://www.cpsc.gov/s3fs-public/5015.pdf : the safety guide named in the frame.
- https://oehha.ca.gov/risk-assessment/art-hazards : the K to 6 art materials list named in the frame.

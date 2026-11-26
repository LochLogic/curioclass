# Frame read: Health, grades K to 2 (2026-11-25)

Fresh expert read of docs/courses/health-grades-k-to-2/frame.md, the subject's pilot after-core band frame. Reader:
Curio Class curriculum expert agent (docs/agents/EXPERT.md), with the health lens. I did not write the frame.

## What I read

- The job: docs/pipeline/briefs/frame-read.md, with the after-core changes in the task, and
  docs/pipeline/briefs/frame-write.md, "After-core courses (added 2026-11-25)".
- The bar: docs/ADOPTION-BAR-SUBJECTS.md part 3 (health) and its row in "Before a scope and sequence";
  docs/courses/health/STANDARD.md and APPROACH.md in full; docs/agents/lenses/health.md; every DESK-ANSWERS.md entry
  naming health (2026-11-16, 2026-11-20, 2026-11-21 x3, 2026-11-25 spelling); earlier health reviews
  (progression-health-2026-11-19, prework-health-read-2026-11-19, prework-health-fixes-2026-11-20).
- The frame in full and its row in data/plans/frames.csv; the 57 rows selected by `file:health&grade:K|1|2`
  (data/plans/course-list.csv over data/progressions/health.csv); data/standards/nhes-2024.txt (the 33 PreK-2 ids).
- The neighbors: docs/courses/physical-education-grades-k-to-2/frame.md and
  docs/courses/social-and-emotional-learning-grades-k-to-2/frame.md (Cross-subject parts and Units tables), both
  written today beside this one. There is no health 3 to 5 frame yet; the hand-on table was checked against the
  grade 3 rows in health.csv.
- The calendar: data/plans/calendar.csv (the 29 rows for this course and every K, 1 and 2 check row) and
  docs/courses/CALENDAR.md, including the stagger rule and its generated list of breaks.
- Gates: `python -X utf8 scripts/frame.py check health-grades-k-to-2`: 0 failures (unit days by year K 24, 1 24,
  2 24; 84 days, 72 in units, 12 for checks and respond days). `python -X utf8 scripts/stale.py check`: 70 files,
  0 failures.

## Verdict

The frame is sound and is a good pilot: every one of the 33 PreK-2 indicators is owned once (10 in kindergarten, 14
in grade 1, 9 in grade 2), each year is whole, the sensitive units are truly removable, getting help sits in a
non-sensitive unit every year, and the calendar rows match the weeks the frame states. The biggest risk is in what
other frames will copy: the checks were placed off the core weeks only, so the health checks share weeks 12 and 27
with other after-core subjects' checks (three stagger rule breaks the calendar already prints), and four "For the
lead" and Cross-subject notes are already stale. The one change that matters most: the lead settles whether the
stagger rule binds after-core pairs in K to 5, and this frame's checks and notes are fixed before 3 to 5, 6 to 8 and
9 to 12 copy them.

## Calendar check

| Item | Frame says | calendar.csv | Holds |
|---|---|---|---|
| Weeks a year | 28 (weeks 1 to 28) | course-list `weeks` = 28; each year runs weeks 1 to 28 | Yes |
| Unit weeks named in Cross-subject (K unit 2 weeks 6 to 11, unit 3 14 to 18, unit 4 19 to 24; grade 1 unit 7 5 to 10, unit 9 18 to 22; grade 2 unit 12 1 to 5, unit 14 13 to 18, unit 15 19 to 22) | as listed | identical | Yes |
| Body names day 3 in week 3; family note week 1 | course day 3 | unit 1 weeks 1 to 5, day 3 = week 3 | Yes |
| Checks: K mid-year week 12, grades 1 and 2 week 11, every year-end week 27; respond the week after | as listed | identical | Yes |
| Off the core check weeks | K core 14 to 17, 29 to 32; grade 1 14 to 16, 19, 29 to 32; grade 2 14 to 16, 18 to 20, 28, 29, 31, 32 | K core checks 14 to 17 (math respond 18), 29 to 32; grade 1 as stated; grade 2 as stated (math respond 30) | Yes: no health check day falls in a core check week. The grade 2 respond day (week 28) shares a week with science grade 2's year-end check; respond days are not counted by the rule |
| Stagger rule against other after-core checks | not addressed | CALENDAR.md breaks: K week 12 (computer science, health), K week 27 (computer science, health, library), grade 2 week 27 (ELD, health, PE) | No (finding 1) |

## Findings, most serious first

### 1. Checks collide with other after-core checks (moderate; LAYER process; REPEAT yes)

**Wrong.** The frame places its checks off the core check weeks, as the after-core brief asks, but says nothing of
the stagger rule (CALENDAR.md, "K to 5, one teacher. No school week holds the course-level check days of two
subjects"). `frame.py calendar` lists three breaks that include health: K week 12 (with computer science K), K week
27 (with computer science K and library K) and grade 2 week 27 (with ELD and PE). The brief's after-core bullet
names only the core checks, so the frame obeyed its brief; the brief and the CALENDAR rule disagree.

**Why it matters.** This is the pilot: if 3 to 5 copies "year-end check in week 27", a grade 3 homeroom teacher
gets four or five check sittings in one week, and the calendar's break list grows with every after-core frame.

**Fix.** The lead decides once, in frame-write.md's after-core section and CALENDAR.md: either (a) the stagger rule
binds after-core pairs in K to 5, and each after-core frame reads `frame.py calendar` and takes a free week (for
health K the free weeks are 9, 10 and 19 to 25 today; grades 1 and 2 have only the week 27 clash in grade 2), or
(b) after-core checks may share a week with each other but never with a core check, and CALENDAR.md says so and
stops listing those pairs as breaks. Then this frame's Course-level checks bullet names the weeks against that rule.
I lean to (b) with one cap (no more than two after-core checks in a week for a grade), since a 28- or 32-week
after-core year has few free weeks once the core checks are out; this is the lead's call, not Cory's.

### 2. Stale notes in For the lead and Cross-subject (moderate; LAYER process; REPEAT yes)

**Wrong.**
- For the lead 1, "Data:" sentences: "set `weeks` to 28 ... or frame.py spreads each year's 28 lessons over 32
  weeks" and "frame.py also numbers band weeks straight through the three years ... the lead decides". Both are
  done: course-list.csv already has `weeks` 28 for this course, and calendar.csv shows weeks per year (grade 1 unit
  6 is weeks 1 to 4).
- For the lead 3: "frame.py reads 'None' as a code and fails it. Pick: let frame.py accept 'None'". frame.py line
  560 already drops `none` and `none owned` from the Owned standards cell, and the empty cells pass.
- For the lead 7 and the Cross-subject headings ("frame written separately; no PE unit number is guessed here", "No
  SEL unit number is guessed here", "When the SEL K to 2 and PE K to 2 frames are written"): both frames now exist.
  PE: k-fitness-activities in PE unit 6 (K weeks 24 to 27), g1-heart-muscle in unit 12 (grade 1 weeks 19 to 22),
  g2-foods-energy in unit 18 (grade 2 weeks 13 to 16). SEL: k-sa-name-feelings and k-sm-calm-down in SEL unit 2 (K
  weeks 5 to 10), k-rel-say-no unit 5 (K weeks 20 to 25), g1-rel-say-no and g1-rel-ask-offer-help unit 9 (grade 1
  weeks 10 to 15), g1-sm-set-goal unit 12 (grade 1 weeks 27 to 32), g2-rel-say-no unit 16 (grade 2 weeks 17 to 20).
- The SEL row for k-sa-name-feelings is written as a condition ("If SEL teaches feeling words first"); it is now a
  fact: SEL teaches them in weeks 5 to 10, before health unit 3 (week 14).

**Why it matters.** A later writer will spend a pass on a decision already made, and the 3 to 5 frame will copy a
"Data:" instruction that no longer applies.

**Fix.** Rewrite For the lead 1 to the dose call only (drop both "Data:" sentences); delete For the lead 3, or turn
it into "the other health bands may write None or leave the cell empty; both pass"; fill the PE and SEL unit numbers
and weeks above into the two Cross-subject tables and drop "no unit number is guessed"; change For the lead 7 to the
one open item (finding 6); turn the k-sa-name-feelings note into "SEL teaches feeling words in weeks 5 to 10, so
unit 3 opens them as retrieval and spends its first day on the I-statement frame".

### 3. Standard 3 is practiced in one topic once the sensitive units go (moderate; LAYER progression and frame; REPEAT new)

**Wrong.** The frame states "every skill standard (2 to 8) is practiced in at least two topics in the band
(STANDARD.md section 4)". By the rows, NHES standard 3 (accessing help) is owned and practiced only in Safety rows
(k-s-trusted-helpers, g1-s-ask-for-help, g2-s-find-school-helpers, g2-s-hurt-or-sick-get-help) plus the three body
safety rows in Violence prevention, which are sensitive and removable. A school that leaves out units 5, 10 and 16
has standard 3 in one topic. The mental health route to help, g1-meh-tell-a-helper, is coded to NHES.S8.2.1 only.
The 2026-11-19 progression read marked the two-topic rule "met" from the strand spread; that count included the
sensitive rows, so this read disagrees with it on standard 3. (Its "acceptable" on standard 6 in PHW and PA stands;
I do not reopen it.)

**Why it matters.** STANDARD.md section 5 says a sensitive unit only practices skills taught elsewhere; the
two-topic claim should survive the same removal, or the course page overstates what a school keeps.

**Fix.** Add `~NHES.S3.2.2` to g1-meh-tell-a-helper's standard cell (asking a trusted adult for help with a worry is
the help step in mental health) and say in unit 7's text that the worry scene practices the help steps (S3) as well
as advocacy (S8). This adds a practice tag and moves no ownership. The 3 to 5 frame should run the same count with
the sensitive rows taken out.

### 4. Four indicators taught or checked in part (minor; LAYER frame; REPEAT yes)

**Wrong.**
- NHES.S3.2.1 (what makes a person a trustworthy helper): unit 4 teaches naming helpers on a hand drawing, and the
  K year-end item is "point to a helper". The row's note has the criteria (helps keep you safe, listens); the unit
  text and the check item do not, so the "what makes" half is not taught or checked as written.
- NHES.S7.2.1 (habits that help self and others): unit 1's hand washing day names the moments but not that washing
  also protects other people.
- NHES.S4.2.2 (listening in different places): unit 3 practices listening with a partner only.
- Kindergarten and standard 8: the frame says every year touches all eight standards. Kindergarten touches standard
  8 only as "this prepares asking others for help" in unit 4; no kindergarten day practices asking.

**Why it matters.** A unit planner builds from the frame's "What students learn" cell; these halves will be missed.

**Fix.** Unit 4: "a trusted adult helps keep you safe and listens; children sort pictured adults by those two
signs", with the year-end item "point to the helper and say one sign" (scored by pointing to a sign card). Unit 1
day 2: add "washing keeps me and the people I touch from getting sick". Unit 3: listening practiced in two settings
(the circle and the lunch table or the playground). Unit 4: one scripted ask to a helper ("Can you help me?") so
kindergarten practices `~NHES.S8.2.1`.

### 5. Bar criterion 4 (norms and pressure) has no named place (minor; LAYER frame; REPEAT new)

**Wrong.** Criterion 4 asks that lessons work on beliefs, on what peers really do and on social pressure; APPROACH.md
says that below grade 6 a unit states the norm in plain words. The frame has pressure in places (the snack ad in
unit 8, the offered vape in unit 13, the rough game in unit 9) but names no unit where a plain-word norm is stated
("most children your age wash before they eat", "most kids say no thanks").

**Why it matters.** An adoption reviewer looks for criterion 4 at the frame and scope layer; nothing here tells a
planner to write it.

**Fix.** One line in the health unit shape bullet: each year's non-sensitive units state one plain-word norm in an
Understanding day, named in the unit row (K unit 1 or 4, grade 1 unit 6 or 7, grade 2 unit 13), with no figure
below grade 6.

### 6. Calm-down tools and step words differ from SEL's (minor; LAYER frame, cross-subject; REPEAT new)

**Wrong.** The SEL K to 2 frame says its calm-down tools (units 2, 8 and 14: "stop, breathe", the balloon breath,
count to five or a stretch) and step card pictures are the ones health should use, so a child meets one card. Health
unit 3 lists slow breaths, counting, squeezing hands and asking for a break. SEL's For the lead also asks that the
I-statement words match health's kindergarten frame.

**Why it matters.** Two cards for one routine in the same year is what the shared-skill rule (STANDARD.md section
8, SEL) is there to stop.

**Fix.** Unit 3 names SEL's kindergarten calm-down card as the one used, adds "asking for a break" only if SEL agrees
to add it, and states that health's "I feel ___ when ___. I need ___." is the frame SEL grade 1 adopts.

### 7. Two unit reasons do not hold on the calendar (minor; LAYER frame; REPEAT new)

**Wrong.** Unit 9's reason says the goal "ends the grade 1 non-sensitive year so the plan can go home over the
summer", but unit 9 ends in week 22 and the year runs to week 28. Unit 15's reason says "Spring, so active play can
be outside", but it runs in weeks 19 to 22 of 32, late winter on most school calendars.

**Fix.** Unit 9: "so the plan goes home with ten weeks of the year left to try it". Unit 15: drop the season clause
(its other reason, closing the goal thread before the year-end check, stands).

### 8. Year-end checks promise carried items they do not name (minor; LAYER frame; REPEAT new)

**Wrong.** The kindergarten and grade 1 year-end checks say "with one item each drawn from units 1 and 2" (and
"from units 6 and 7"), and grade 2 "from units 12 and 13", but the code lists name only the later units.

**Fix.** Name the items: K, order the washing steps (NHES.S7.2.1) and helps or hurts (NHES.S2.2.1); grade 1, a
germ-stopping action (NHES.S1.2.3) and who to ask (NHES.S3.2.2); grade 2, pick and give a reason (NHES.S5.2.4) and
the right school helper (NHES.S3.2.3).

### 9. The emergency call wording could teach the wrong rule (minor; LAYER frame; REPEAT new; judgment call)

**Wrong.** Unit 13 teaches "a first look at calling for emergency help with an adult". From memory (not opened for
this read): common child safety teaching gives young children the emergency number and when to call it themselves,
when no adult can. "With an adult" read by a busy writer becomes "only with an adult".

**Fix.** "Get an adult first; if no adult can help, call 911 on a phone (practiced on a paper phone)". The HECAT
Safety module PreK-2 read, owed before the unit plan, confirms the line.

## Lens checklist (course frame layer)

| Line | State |
|---|---|
| Band reaches all eight standards | Met for the band; each year met, with K's standard 8 thin (finding 4) |
| A skill standard practiced in only one topic | Missed for standard 3 once sensitive units are out (finding 3) |
| No coverage map, or cells naming no units | Not applicable at the frame (owed by the scope and sequence); the unit rows name HBOs that match the STANDARD.md K to 2 column exactly (PHW 1 to 5, 11; FN 1, 2, 3, 6, 7; MEH 1 to 5, 7; PA 1, 4, 6; S 1, 3 to 8; V 1, 3, 7 and 8 sensitive; T 1, 2; AOD 1; SH 1 to 3 sensitive) |
| A topic taught once with nothing after | Met: every topic returns in alternate years or more (T in K and 2, SH in 1 and 2) |
| Sensitive unit not removable | Met: each owns no indicator, no non-sensitive unit assumes one, each has a leave-out note and an extension unit |
| Getting help only in a sensitive unit | Met: units 4, 7, 13 |
| Indicators in the wrong span | Met: all 33 are PreK-2 |
| Behavior outcome named per unit | Met |
| Fact-recall end-of-unit test | Met: unseen pictured scenarios scored on steps |
| Skill with no steps, model or practice | Met in design (step cards, model day, pair practice) |
| Scare tactics, shock images | Met: pictures only, calm scenes |
| Figures with no source or year | Not applicable yet; the one figure (40 hours) is sourced and holds |
| Content above or below the age | Met as far as the frame shows; module reads owed per unit |
| Link home | Met: home task each unit, family notes in English and Spanish |
| Wording copied from SHAPE America | Met: ids and own words only |
| Day-level lines (disclosure, blame, weight focus) | Met in the teacher notes; no task asks about home, food, body or family |
| Health reteaching a science model | Met: no K to 2 science lean; germs and names stated by health |
| Health and PE both or neither planning the activity | Met: health teaches why and the habit, PE the moving, both name each other |

## Days

84 days, 28 a year, 24 in units and 4 course-level days each year: room is there. Unit shares follow load as the
frame says. The two outliers are unit 6 (4 days for 4 rows and 3 owned indicators, no Fluency day for its
cough-and-wash card) and unit 13 (5 days for 1 owned indicator across 4 rows); both are defensible, since unit 13's
rows carry three practices of earlier indicators. I would not move a day now; the unit 6 planner should say where
the card's model and pair practice fit in day 2.

The dose of 28 against APPROACH.md's "about 30" is within "about" and the reason holds. 14 hours a year against the
2007 figure of 40 is named openly, as Cory decided.

## Seams

Kindergarten to grade 1 and grade 1 to grade 2 tables match every `assumes` cell in health.csv; the hand-on table
to grade 3 matches every grade 3 row that assumes a grade 2 row. The sensitive chains (5 to 10 to 16, 11 to 17) open
with the one idea needed if the earlier unit was left out. No model is used before its introducing unit.

## What is right and should not be touched

- The Year column with units numbered through the band, and each year whole with its own two checks and respond days.
- Sensitive units last in each year, two days, owning no indicator, never sampled by a check; the leave-out note
  names the unit its days extend.
- Body names on day 3 with the family note in week 1, the person read marked (L89), and no later item asking a child
  to say the names.
- The said-aloud record across the last two days of communication units, and pointing, drawing or an adult scribe
  for every item.
- The C3 column used for the skill standard and its step card.

## What the other health frames should and should not copy

**Copy:** the band shape above; a getting-help unit in a non-sensitive place every year; sensitive units placed and
counted as here; the check shape (unseen scenario sitting plus a said-aloud record); the Seams tables per year pair;
the PE row table with "If PE teaches it later"; health stating its own plain facts with source.

**Do not copy:** the check-week reasoning until finding 1 is settled (read `frame.py calendar`, not just the core
weeks); the stale For the lead items 1, 3 and 7; the two-topic claim without recounting with sensitive rows removed
(finding 3); season words in unit reasons; "28 because the core year-end checks start in week 29" without checking
that band's own core weeks (grades 3 to 5 core year-end checks run weeks 28 to 32, so 3 to 5 may end at 27). Grades 6
to 8 and 9 to 12 must set their own doses (45 and 80 sessions) and are not homeroom grades, so the stagger rule reads
by school day there.

## Facts named from memory: spot checks at source

| Fact | Checked at | Holds |
|---|---|---|
| NHES 2007, second edition, page 76: at least 40 hours a year in pre-K to grade 2 (80 in grades 3 to 12) | NHES second edition PDF (copy hosted by ETR), PDF page 76; also Connecticut State Department of Education summary | Holds (PDF page 76; printed page not checked) |
| CDC "Clean Hands" pages; hand washing in five steps; the moments before eating, after the toilet, after coughing | https://www.cdc.gov/clean-hands/ (About Handwashing, 2024-02-16) | Holds. CDC says scrub at least 20 seconds, humming a song twice; "scrub for a song" should say twice (Settled below) |
| A national pediatrics association's family pages on correct body names | AAP, "10 Tips for Parents to Teach Children about Body Safety and Boundaries" | Holds: AAP advises correct names for all parts, including genitals, and teaching which areas are private |
| Child Welfare Information Gateway pages on preventing child sexual abuse | https://www.childwelfare.gov/topics/preventing/ | Partly: the prevention pages exist; a page on sexual abuse prevention was not found from that page. The sensitivity brief should name the exact page |
| NHTSA car seat pages; federal Poison Help pages | the two addresses in the frame | Not checked: both returned 403 to the fetcher. Browser check (lead opens them in Claude in Chrome at grade close, standing rule 2026-11-22) |

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Hand washing step card: "scrub while you sing the song twice (20 seconds)" | matches CDC's current page | frame.md unit 1 C3 and day 2 |
| Unit 9 reason: "so the plan goes home with ten weeks of the year left" | unit ends week 22, not at summer | frame.md unit 9 |
| Unit 15 reason: drop "Spring, so active play can be outside" | weeks 19 to 22 are not spring | frame.md unit 15 |
| Year-end checks name their carried items (finding 8 list) | the check promises items it does not name | frame.md Course-level checks |
| Unit 4 teaches and checks the two signs of a trusted helper | NHES.S3.2.1 in full | frame.md unit 4; K year-end check |
| Unit 1 day 2 adds that washing protects others; unit 3 listening in two settings | NHES.S7.2.1 and S4.2.2 in full | frame.md units 1 and 3 |
| Unit 4 adds one scripted ask to a helper (`~NHES.S8.2.1` practice) | kindergarten touches standard 8 | frame.md unit 4 |
| Unit 3 uses SEL kindergarten's calm-down card | one card a year | frame.md unit 3 and Cross-subject |
| Unit 13 emergency line: "get an adult; if no adult can help, call 911 on a paper phone" | the likely reading teaches the wrong rule | frame.md unit 13 |

The lead's calls (not settled here): the stagger rule for after-core pairs (finding 1) and the `~NHES.S3.2.2` tag
on g1-meh-tell-a-helper (finding 3, a progression edit).

## For Cory

- Supplies ceiling for health (frame For the lead 6): the frame asks for $30 a year for a class of 30; this frame
  costs $16 to $29. Money, so it is Cory's.

## What I could not judge

- The HECAT topic modules' PreK-2 span tables (other than Sexual Health in part) are unread; each unit's "Check set
  adds" cell rests on that read.
- The NHTSA and Poison Help pages (blocked to the fetcher).

## Sources

- NHES, second edition (2007), PDF copy: https://www.etr.org/sites/healthsmart/assets/File/standards/NHES_2dEd.pdf
  (the 40 and 80 hours figure, PDF page 76).
- Connecticut State Department of Education summary: https://test-cd.ct.gov/-/media/sde/health-education/mtchealthed.pdf
  (same figure, cited to the second edition).
- CDC, About Handwashing: https://www.cdc.gov/clean-hands/ (steps, 20 seconds, key times).
- AAP, 10 tips on body safety: https://aap.org/en/news-room/news-releases/health--safety-tips/10-tips-for-parents-to-teach-children-about-body-safety-and-boundaries
  (correct names, private areas).
- Child Welfare Information Gateway, Prevention: https://www.childwelfare.gov/topics/preventing/ (prevention pages).

## Confidence

Findings 1, 2 and 8: firm (read from the repository). Finding 3: likely (row count; disagrees with the 2026-11-19
read). Findings 4, 5, 6 and 7: likely. Finding 9: a judgment call, from memory.

## For the source list

- The NHES second edition PDF at the ETR address above opens with curl and extracts with pypdf (page 76 holds the
  hours figure).
- AAP's body safety tips release, for the body-names and body safety sensitivity reads.

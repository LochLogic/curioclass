# Expert read: scope and sequence of Media Arts, grades K to 2 (2026-11-26)

Course `media-arts-grades-k-to-2`. Cold read by the curriculum expert (PRODUCTION-PATH step 3), done as
docs/pipeline/briefs/sequence-read.md says, with build/scope-writes/ARTS-READ.md's extra checks. I did not write the
scope; a fresh Claude agent did.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/arts.md, docs/ADOPTION-BAR-SUBJECTS.md section 2 (items 1 to 9, "Fails
  if", "Scope and sequence states"), build/scope-writes/ARTS-BRIEF.md and ARTS-READ.md.
- Under review, in full: docs/courses/media-arts-grades-k-to-2/scope-and-sequence.md and
  data/plans/media-arts-grades-k-to-2/days.csv (192 rows).
- Beside them: the frame (docs/courses/media-arts-grades-k-to-2/frame.md, in full), the 24 ma-k, ma-g1 and ma-g2
  rows of data/progressions/arts.csv, docs/courses/CALENDAR.md (words, stagger rules 1 to 5, target weeks; the
  course's rows say weeks 21 and 27 in all three grades), the 54 kindergarten to grade 2 media arts lines of
  data/standards/ncas-performance-standards-words.txt, and the DESK-ANSWERS entries on media arts.
- Gates, run first: `scripts/plan.py check` (sequence media-arts-grades-k-to-2: 0 failures; the failures it prints
  belong to algebra-ii and others, not this course), `scripts/sequence.py check media-arts-grades-k-to-2` (0
  failures), `scripts/frame.py calendar` (arts weeks 21 and 27 in grades K, 1 and 2; no break), `scripts/stale.py
  check` (0 failures). The gates settle day totals, unit counts, kinds, an assessment per unit, respond days and
  owned skills placed; I spent the read on the rest.
- My own scripted checks on days.csv: every one of the 54 owned ids sits on a teaching day of its own year before
  its first assessed day (all 54 pass); kinds per unit; the per-unit "Processes" lists in the .md against each day's
  note.
- No earlier sequence read exists for any arts course; the frame reads (docs/reviews/frame-media-arts-*-2026-11-25.md
  and the fix pass docs/reviews/frame-music-theater-media-arts-fixes-2026-11-26.md) were checked so nothing settled
  there is reopened. No outside source was opened for this read; the two points that rest on memory are marked.

## Verdict

The scope is sound and close to ready: every owned id is taught in its own year before it is assessed, each year
names its grade's ids, every unit makes, critiques, revises and shows, the four processes are in every unit, and the
checks sit on CALENDAR.md's weeks. The biggest risk is the once-a-week path's screening units, whose first session
carries four days of first teaching in about 30 working minutes, so a teacher will cut the very parts the screening
scores. The one change that matters most is to spread those days across the six sessions (settled below). Six
assessment items or check tasks also miss a lettered part of the code they list, each fixed by an item-level change.

## Findings, most serious first

### 1. The once-a-week screening units put four days of first teaching into one session

LAYER sequence. REPEAT new. Confidence: firm (arithmetic on the frame's own session minutes).

**What is wrong.** Shorter path, "10-day screening unit (units 4, 8, 12)": S1 merges positions 1 to 4. In unit 4
that is Ruttmann with a remembered media moment (day 55), the film-strip technique with a ten-minute retrieval (day
56), Pas de deux with the class movement made (day 57) and the screening-plan card with how a showing felt (day 58).
Units 8 and 12 are the same shape (two works, a technique with its retrieval, the conditions card). After set-up and
clean-up a session has about 30 minutes. The frame's own keep list for that path asks S1 for "the demonstration with
a step card, opened by the look or listen at a work", one work and one technique, not four days.

**Why it matters.** A teacher who cannot fit S1 drops what looks optional: the plan card and the showing conditions
(MA:Pr6.1.Ka, 1a, 2a are scored on that card and at the screening) or the second work (unit 4's dance-with-film,
which carries MA:Pr4.1.K). ARTS-READ asks that the once-a-week path hold "with no assessed or owned part cut"; on
paper it does, in the room it will not.

**Fix (settled, see table).** Screening units: S1 = positions 1 and 2 (the hook study and the technique); S2 =
positions 3, 5 and 6 (the second study as the opener, making, the critique); S3 = positions 4 and 7 (the plan card
or conditions taught at the start of the revision session, then filled). The card is still scored after the
screening (S4), never in S3. For unit 8 this needs finding 1b's swap so its rotation talk item is taught in S1.

**1b.** Unit 8 teaches the meaningful media experience (MA:Cn10.1.1b) on day 121, position 3, while units 4 and 12
teach their experience share on the hook day. With the merge above, unit 8's rotation would hear MA:Cn10.1.1b in the
same session it is first taught. Fix (settled): move the experience share to day 119 (Viva Frida, the hook) and give
day 121 (Dear Primo) what Tonatiuh drew on (MA:Cn10.1.1a: an interest and an example). Day 119 codes MA:Pr4.1.1;
MA:Cn10.1.1a; MA:Cn10.1.1b. Day 121 codes MA:Cn10.1.1a. This also makes the three screening units match.

### 2. Six items or check tasks miss a lettered part of a code they list

LAYER sequence (and frame, for the evidence lines the days copy). REPEAT yes (part coverage was found in earlier
sequence reads). Confidence: firm (read against the words-file lines).

| Day(s) | Code | Part missed | Fix (settled) |
|---|---|---|---|
| 163 to 165 (rotation), unit 10 | MA:Pr5.1.2c, "named tool methods for recording **and shaping** media" | The look-for checks one recording method (move, capture, move) only; shaping (the sound made louder, softer or given a longer pause, days 159 to 161) is never marked | The rotation look-for adds one shaping move, shown on the device or the sound score and named. Day 163 note and the .md's unit 10 Assessments line |
| 99 to 101 (rotation), unit 6 | MA:Pr5.1.1c, "try varied tool uses, and **show classmates** what you found" | At the tray the child shows the teacher, not a classmate | At the tray the child shows a tablemate while the teacher watches and marks. Day 99 note |
| 187 to 190, unit 12 | MA:Cn10.1.2a, "what you know, like, **and have read**, plus examples" | The look-for reads "what the child knew, liked **or** read", so a child meets it without the reading part | The source card has three picture boxes (I know, I like, I read) and an example line; met = the "I read" box (the class tale or another book), one of the other two, and an example |
| 117, year 1 year-end check | MA:Cr1.1.1, "sketching **and making models**" | The table task is three sketches only | Add: fold one sketch into a stand-up paper model, kept with the sketches. Day 117 goal and the .md checks table |
| 181, year 2 year-end check | MA:Cr1.1.2 ("brainstorming **and improvising**") and MA:Cr2.1.2 ("sketches **and mockups**") | A paper table task cannot show improvising, and it has no mockup | MA:Cr1.1.2 leaves day 181's codes (the three ideas stay as the input to choosing) and joins the .md's "Codes not sampled" list with that reason; the task adds folding the chosen storyboard into a stand-up mockup, so MA:Cr2.1.2 is asked in full |
| 41, 105, 169, mid-year checks | MA:Cn11.1.Kb, 1b, 2b ("**use** media tools and spaces") | A picture sort shows the child knows the safe way, not that the child uses it | See finding 7; the S&S line should say the sort samples knowing the rule and the use stays assessed in the unit |

The frame's unit 6, 10 and 12 evidence lines and its year 1 and year 2 year-end rows say the old thing; their
wording is the lead's (For the lead below).

### 3. Two fold-in days on the 10-days-short path carry the unit's baseline look, and one lands on a full day

LAYER sequence. REPEAT new. Confidence: firm.

**What is wrong.** Day 68 (unit 5) and day 132 (unit 9) are fold-ins, and each holds its unit's baseline look at the
main look-for. Folding them drops the first of the two marks a unit that the logic model's output ("two marks a unit
per child") and the growth claim rest on. Day 94's practice folds into day 95, which already holds the technique
change and the ten-minute candidate work by a living maker from Asia.

**Fix (settled).** Fold-in 68 becomes 71 (into day 72's opener); fold-in 132 becomes 135 (into day 136's opener); day
94 stays a fold-in but its ten minutes go into day 97's opener (team making), not day 95's. Days 71 and 135 are plain
practice days with nothing assessed. The Shorter path table and the four day notes change.

### 4. The year-end check's placement rests on a calendar reason that no longer holds, and five threads are never sampled

LAYER frame. REPEAT new. Confidence: likely (the calendar fact is firm; the better placement is a judgment call).

**What is wrong.** The .md ("Codes not sampled") and the frame put each year-end check in week 27, before the
screening unit, "to stay off the core checks of weeks 29 to 32 (CALENDAR.md tool c)". CALENDAR.md rule 1, as
changed in the lead calendar pass of 2026-11-26, says specials (arts among them) do not count against the classroom
teacher's stagger. The .md itself says so two paragraphs later. So the reason is stale. Its cost: across the whole
band the course-level checks sample only the read, society and ideas threads. Craft, make, judge, present and sources
are never sampled. Units 3, 7 and 11 always end two days before the year-end check, and units 4, 8 and 12 come after
it. The frame's For the lead item 3 (week 27 shared with theater, health, library and others) is moot for the same
reason.

**Fix (for the lead, frame).** Pick: move each year-end check to week 32, after the screening unit (days 63 and 64 of
each year; the screening unit takes weeks 28 to 31). It may then sample unit 3 (make, judge) as well as units 1 and 2,
and the once-a-week screening unit no longer pauses for a check. CALENDAR.md's target weeks for this course become
21 and 32. Otherwise keep week 27 and strike the stale reason from both files. This bears on later.csv L107 (the
writer's lead item 1).

### 5. Years 1 and 2 have no same-year retrievals, though the frame names the same-year rows they build on

LAYER sequence. REPEAT new. Confidence: likely.

**What is wrong.** Year K opens three same-year retrievals (days 20, 44, 56), as rule 2 asks for a row used earlier
in the same year. Years 1 and 2 have none, yet the frame's "Why this unit, here" says unit 7 needs unit 6's pages in
order, unit 10 needs unit 9's fair roles and credit, and unit 11 combines the content recorded and shaped in unit 10.
Day 86 already practices unit 5's shots without marking it a retrieval.

**Fix (settled).** Add to `retrieves`, each a ten-minute task in the day's opener: day 86 `ma-g1-read` (far, middle,
close); day 109 `ma-g1-ideas` (pages in order); day 156 `ma-g2-society` (turns and the credit line before the first
team try); day 173 `ma-g2-craft` (the recorded or shaped sound that goes into the whole). The .md's same-year
paragraph lists them.

### 6. Year K's works are thin on living makers, and the unit 3 candidate was dropped for a reason the other units contradict

LAYER sequence. REPEAT new. Confidence: judgment call (whether Westerkamp is living rests on memory).

**What is wrong.** Year K studies nine works. Seven are by makers from Europe or North America, all but one are from
before 1970, and the only maker likely living is Westerkamp (born 1946; "the unit plan records whether living").
APPROACH asks for living makers each year (bar item 7). The .md drops unit 3's candidate (a second picture-sequence
form from Africa or the Americas) because "a third work in a ten-day unit would take the time of a making day". Yet
units 6 and 9 keep their candidates as ten minutes inside an existing day.

**Fix (settled).** Keep the unit 3 candidate as the practice piece on day 47. The critique card is practiced there
"on a Curio Class card"; it becomes a picture sequence by a living maker from Africa or the Americas, described and
linked. The unit plan picks it, records its rights line and checks every arts frame for a repeat. No day is added.
The .md's candidate line changes from dropped to kept.

### 7. Rotation items sampled on course-level checks: the writer's lead item 2

LAYER frame. REPEAT new. Confidence: judgment call.

The frame says the safe-use ids are "never a check day item", yet its checks table samples each by a picture sort.
The writer followed the table and proposed new frame wording. I agree, with one change. A sort shows that the child
knows the safe, polite way; the code asks for use. The frame sentence should read "never an end-of-unit check day
item; a course-level check may sample knowing the rule by a fresh paper task, and the use stays assessed in the
unit", and the .md's "Codes not sampled" paragraph should say the same.

### 8. Day 184 is overloaded, and the screening units' first making day carries the baseline and the first rotation

LAYER sequence. REPEAT new. Confidence: likely.

Day 184 holds the ten-minute retrieval, the patua scroll study (a flagged work that needs care) and the scroll
technique's step card, in about 30 working minutes. Days 59, 123 and 187 each hold the first making of the piece,
the baseline look for every child and rotation 1 (ten children at the tray). Fix, for the unit plan, not settled
here: time day 184 to the minute; if it runs over, the step card moves to the first half of day 186 and the
conditions take the second half (the once-a-week S1 then takes the technique half of position 4). On days 59, 123
and 187 the baseline is a glance mark made while walking the tables, and the tray rotation starts after it.

### 9. Two small order points in unit 2

LAYER sequence. REPEAT new. Confidence: likely.

(a) Day 21 asks kindergartners to play with "paper cutouts" two days before the silhouette cutout's step card (day
23). Fix (settled): day 21's note says the cutouts for play are shapes pre-cut by an adult; children cut their own
from day 23. (b) MA:Pr5.1.Kc ("tell what you learn about how a tool works") is taught once (day 22) and next met at
its talk item on day 39, seventeen days later. Fix (settled): day 26 adds "and tell one thing the crayon strip taught
you", and day 26's codes add MA:Pr5.1.Kc.

### 10. The per-unit "Processes" lists drift from the day notes

LAYER sequence. REPEAT new. Confidence: firm (scripted).

About eight days carry a process in their note that the .md's list leaves out: day 6 (respond), day 11 (connect),
days 13, 77, 92, 100, 140 and 141 (create, mostly critique and revision days). Every unit still has all four
processes, so nothing fails. Fix: regenerate the lists from the notes, or drop the day numbers and keep one line per
unit naming the days of the process that is thinnest.

## Settled by the expert

| Choice | Reason in one line | Files |
|---|---|---|
| Screening-unit once-a-week merge: S1 = positions 1, 2; S2 = 3, 5, 6; S3 = 4, 7 | S1 held four days of first teaching; this follows the frame's keep list | scope-and-sequence.md, Shorter path table |
| Unit 8: experience share moves from day 121 to day 119; day 121 carries MA:Cn10.1.1a | Matches units 4 and 12, and lets the merged path teach the rotation item before it is heard | days.csv days 119, 121; .md unit 8 paragraph |
| Unit 10 rotation look-for adds one shaping move, shown and named | MA:Pr5.1.2c's "shaping" part had no item | days.csv day 163 note; .md unit 10 Assessments |
| Unit 6 rotation: the varied use is shown to a tablemate while the teacher watches | MA:Pr5.1.1c's "show classmates" part | days.csv day 99 note |
| Unit 12 source card: I know, I like, I read boxes and an example; met needs "I read" plus one more plus the example | MA:Cn10.1.2a's "and have read" part | days.csv days 185, 187, 190 notes |
| Day 117 adds a stand-up paper model of one sketch | MA:Cr1.1.1's "making models" part | days.csv day 117; .md checks table |
| Day 181: MA:Cr1.1.2 leaves the codes (listed as not sampled, with the reason); the storyboard is folded into a mockup | A table task cannot show improvising; MA:Cr2.1.2 needs its mockup | days.csv days 181, 182; .md checks table and "Codes not sampled" |
| Fold-ins 68 to 71 (into 72) and 132 to 135 (into 136); day 94's ten minutes go to day 97, not 95 | Keeps each unit's baseline; day 95 was already full | .md Shorter path table; days.csv notes on days 68, 71, 94, 132, 135 |
| Same-year retrievals: day 86 ma-g1-read, 109 ma-g1-ideas, 156 ma-g2-society, 173 ma-g2-craft | Rule 2 for rows used earlier the same year, as year K already does | days.csv `retrieves` and notes; .md same-year paragraph |
| Unit 3 candidate kept: a living maker's picture sequence from Africa or the Americas as day 47's critique practice piece | Year K's range of living and non-Western makers is thin; no day added | days.csv day 47; .md unit 3 candidate line |
| Day 21 play uses pre-cut shapes; day 26 adds MA:Pr5.1.Kc | Cutting waits for its step card; the tool lesson gets one practice before its item | days.csv days 21, 26 |

The caller copies these to docs/reviews/DIGEST.md. I edited nothing but this report. I logged no
`scripts/plan.py defect` rows, since ARTS-READ allows only this file; the caller may log them.

## For the lead (frame and shared files)

1. Finding 4: the year-end check's week (my pick: week 32, after the screening unit) and the stale reason in the frame
   and the .md; the frame's For the lead item 3 is moot under CALENDAR.md rule 1.
2. Finding 7: the frame's "never a check day item" sentence, worded as above.
3. Finding 2: the frame's unit 6, 10 and 12 evidence lines and its year 1 and year 2 year-end rows, to match the
   settled items.
4. The writer's lead item 3 (unit 10 "talk record" should read "stop-motion and role record"): agreed. days.csv day
   169 already says it; the frame's checks table row does not.
5. The writer's lead item 1 (rule 3 coverage, L107): keep the frame's one table task and one talk item per check.
   Finding 4's move closes the worst of the gap (make and judge sampled each year) at no day cost.

## What is right and should not be touched

- The band-year rule is kept exactly: each year heading names its grade's 18 ids, all 54 are taught and assessed in
  their own year, and none from the year before is claimed.
- Readiness and retrieval by grade number are right: every year 1 and year 2 row assumes only the row one grade back,
  so each opens with a retrieval inside day 2, and no readiness check is owed. Day 1 of every unit stays clean.
- The four processes, technique before making, a critique day with a protocol, a revision and a showing are in every
  unit; every critique note keeps "talks about the work, never the maker".
- The talk check day, screening check day and rotation arithmetic (35 of 40 minutes planned, one talk item a child a
  day) and the `school_day` formula match CALENDAR.md, and the checks sit on the course's target weeks.
- Sensitivity flags travel into every day that studies a flagged work, with the story-character or class-shared
  option marked the same, and the leave-out lines for units 4, 9 and 10 are on the right days.
- The paper path is on every day, and no day needs a device or a student account.

## What I could not judge

- Whether Westerkamp, Rao, Villareal, Morales, Tonatiuh and Red Star are living as of today: from memory only; the unit
  plans record it.
- The rights lines of the works: the unit plans check each item's own page.
- Real session timing with 30 kindergartners and a cart: findings 1 and 8 rest on the frame's minute budget, not on a
  tried lesson.

## Sources

No outside source was opened for this read. The standards' wording is from data/standards/ncas-performance-standards-words.txt;
the calendar rule from docs/courses/CALENDAR.md (rule 1, lead calendar pass 2026-11-26). Living-maker status rests on
memory.

## For Cory

Nothing new on scope, money, people or audience. The frame's open supplies ceiling (its For the lead item 6) still
waits on him.

## For the source list

None.

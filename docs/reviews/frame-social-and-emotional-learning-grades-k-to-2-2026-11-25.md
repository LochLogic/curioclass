# Frame read: Social and Emotional Learning, Grades K to 2 (2026-11-25)

Expert cold read of docs/courses/social-and-emotional-learning-grades-k-to-2/frame.md, the pilot frame for SEL, by
docs/pipeline/briefs/frame-read.md with the after-core changes. I did not write the frame.

## What I read

- docs/agents/EXPERT.md; docs/agents/lenses/sel.md; docs/courses/sel/STANDARD.md and APPROACH.md in full;
  docs/ADOPTION-BAR-SUBJECTS.md (pass rule for small courses, part 9, the SEL owed row); data/standards/casel-5.txt.
- DESK-ANSWERS entries naming SEL: 2026-11-15 (L43), 2026-11-16 (q-later-sel-eld), 2026-11-21 (ownership, q-fix-sel-1),
  2026-11-22 (q-prog-sel-1), 2026-11-25 (after-core band frames).
- docs/pipeline/briefs/frame-write.md including "After-core courses (added 2026-11-25)".
- The frame in full; its row in data/plans/frames.csv (18 units, 192 days, 20 minutes, 2 a week, 96 weeks); its rows
  cell in data/plans/course-list.csv (`grade:K|1|2`) over data/progressions/sel.csv (120 rows, models and leans
  checked by script); data/progressions/sel-edges.md ("For the kindergarten frame").
- Its 24 rows in data/plans/calendar.csv, and every K, 1 and 2 check row of every other course there.
- The Units tables of the core frames it cites (ELA K, 1, 2; social studies K, 1, 2; math K, 1, 2) and their calendar
  weeks; the health K to 2 frame (units, Cross-subject, For the lead); the PE K to 2 frame (cultural picks).
- Gates: `python -X utf8 scripts/frame.py check social-and-emotional-learning-grades-k-to-2`: 0 failures, notes
  "unit days by year: K 60, 1 60, 2 60" and "18 units, 192 days (180 in units, 12 for checks and respond days)".
  `python -X utf8 scripts/stale.py check`: 70 files, 0 failures.
- Web spot checks (2026-11-25): Ampe, jan-ken, the CPSC Public Playground Safety Handbook.

## Verdict

The frame is sound in shape and faithful to the progression: every one of the 120 rows sits in one unit, each year is
whole with six units and two checks, the calendar rows match every week the frame states, no SEL check falls in a
core check week of its grade, and the models, carry-out cues, family activities and leave-out wording are what the
lens asks for. It is not yet a pattern to copy. The biggest risk is the health seam: the frame says the health frame
is still being written when it was finished minutes before, and in grades 1 and 2 health teaches refusal and
asking-for-help steps weeks before the SEL units that are meant to own them, with different step words. The one change
that matters most for the other three SEL bands is to get a Desk answer on the unit sizes (11 and 8 with course-level
checks, against q-fix-sel-1's 11 and 10) and to state the 20-minute session budget, before any band copies this one.

## Findings, most serious first

Severity: High (a writer would build wrong days or a settled call is changed), Medium (a gap the scope writer
would have to guess at), Low (wording, a count, a pick).

### 1. High. The health seam is stale and runs backwards in grades 1 and 2

LAYER frame (and process). REPEAT yes (cross-subject order, as in earlier frame reads).

- **What is wrong.** Cross-subject, "Health (same year)", says "The health frames are being written now, so no health
  unit number is cited here". docs/courses/health-grades-k-to-2/frame.md was saved at 21:29 on 2026-11-25, five minutes
  before this frame, with units and weeks for every SEL lean, and its For the lead 7 asks the SEL frame to name them.
  Read against those weeks:
  - Grade 1: health unit 7 (weeks 5 to 10) teaches g1-s-choose-and-ask and g1-s-ask-for-help before SEL unit 9
    (weeks 10 to 15) teaches g1-rel-say-no and g1-rel-ask-offer-help.
  - Grade 2: health unit 14 (weeks 13 to 18) teaches four boundary steps ("say it, say stop again, move away, tell")
    and its own conflict steps before SEL unit 16 (weeks 17 to 20) teaches two refusal steps ("say no with a reason,
    then offer something else"). Unit 16's "Health grade 2 applies the same refusal ... and builds on this unit" is
    false on these weeks.
  - Kindergarten: health unit 3 (weeks 14 to 18) teaches a four-step listening card, four calm-down tools (slow
    breaths, counting, squeezing hands, asking for a break) and "I feel ___ when ___. I need ___", while SEL
    kindergarten teaches a two-step talk turn card, two calm-down steps and no I-statement until grade 1. The
    frame's last line ("the ones health should use, so a child meets one card") is a wish the health frame does not
    meet.
- **Why it matters.** STANDARD section 7 says SEL teaches the skill and health applies it and does not reteach the
  steps. As written, a grade 2 child meets two refusal routines a month apart and a kindergartner two listening
  cards. The lens fails "a skill's name or steps changed" across the child's day, and the scope writers of both
  courses will write cards that do not match.
- **Fix.** Replace the "being written now" sentence and table with one that cites health units 3, 4, 7, 9 and 14 with
  their weeks as the health frame states them. For each lean say which course comes first and what the second does:
  kindergarten (SEL first): health unit 3 opens with SEL's feelings faces and "stop, breathe" as retrieval and adds
  tools; grade 1 and grade 2 (health first): either health units 7 and 14 move after SEL units 9 and 16 (the lead
  moves them in the health fix pass), or SEL units 9 and 16 open with health's steps as retrieval and build the
  refusal on them. Pick: one shared step set written once in STANDARD section 7 (talk turn card, calm-down tools,
  I-statement, refusal steps), both frames citing it. Move the three wording questions from For the lead 5 into that
  one pick. Confidence: firm (both frames and calendar.csv agree).

### 2. High. The 20-minute session has no budget, and the openings stack

LAYER frame. REPEAT yes (lesson 21, minutes inside the period, named in earlier frame reads).

- **What is wrong.** The Days bullet says "20 minutes a session" and nothing about what the 20 minutes hold (lesson 21:
  set-up, clean-up, collecting work). Meanwhile the frame and APPROACH ask each session for: the calm-down routine "at
  the start of every session from here on" (unit 2), a five-minute retrieval opening (Days bullet, every unit), three
  minutes of an earlier skill with its card (APPROACH section field 8), and two or three sub-skills a group, so an
  Understanding session names and models up to three skills for five-year-olds (unit 2 group 3 has four). Puppets,
  floor games and the class sheet add set-up.
- **Why it matters.** Summed, the fixed parts take about 10 of 20 minutes before the new skill. The sel-edges.md read
  already warned that about three new sub-skills in 20 minutes is too much for kindergarten. A scope writer will
  either overfill every session or drop the rehearsal, which is the bar's "Fails if".
- **Fix.** Add to the Days bullet: "A 20-minute session holds one opening of about 4 minutes (the calm-down routine
  and the retrieval item together, the returning skill folded into it), about 13 minutes of teaching and rehearsal,
  and about 3 minutes to mark the class sheet and put away puppets or cards. A first-teaching session names at most
  two sub-skills; a group of three or four spreads its first teaching over its Understanding and first Fluency
  sessions." Then check units 2 (group 3), 6, 10, 12, 17 and 18 against that line. Confidence: likely (arithmetic and
  the earlier expert note; no source sets K session content).

### 3. High. The unit sizes change a settled Desk call, and the pilot must not be copied before an answer

LAYER process. REPEAT new.

- **What is wrong.** Desk q-fix-sel-1 (Cory, 2026-11-21) set 64 = four units of 11 and two of 10, short path five and
  six. The frame keeps 64 but spends 4 sessions on course-level checks, so two-group units lose their second Fluency
  (10 to 8), the two-group short path becomes 5 (STANDARD says 6), and kindergarten runs 12, 8, 8, 8, 12, 12. This is
  flagged in For the lead 1, which is right, but the frame is built on it and asks the other three bands to copy it.
  The kindergarten short path ("4, 6, 4, 4, 6, 6 and 2") is given with no derivation, and it differs from grades 1 and
  2 (a K two-group unit has one Application, a grade 1 two-group unit two), so a writer cannot tell what its sessions
  hold.
- **Why it matters.** It changes how much rehearsal (the course's core, bar item 5) the units with six sub-skills get:
  units 8 and 13 put six sub-skills in 8 sessions. The frame-write brief's demand for course-level checks and the
  Desk's arithmetic conflict, and only the Desk can choose which gives.
- **Fix.** Keep the frame as written while the Desk decides; do not start grades 3 to 5, 6 to 8 or 9 to 12 frames on
  this shape until it does. In the Days bullet, derive the kindergarten short path in one line (settled below). My
  view for the Desk: the frame's trade is acceptable for K to 2 only if finding 2's budget is applied, because a
  two-group unit still gives each group Understanding, Fluency and Application. Confidence: judgment call.

### 4. Medium. No year-end check, and kindergarten's decision-making is never in a course-level check

LAYER frame. REPEAT new.

- **What is wrong.** frame-write's after-core section asks each year for "its own mid-year and year-end course-level
  checks". Check 2 sits after unit 5 (weeks 26 to 27), so unit 6 of each year follows it and is never sampled. Check 1
  takes only the calm-down steps from unit 2, and check 2 carries unit 5's record unchanged. In kindergarten that
  leaves units 5 and 6, all nine relationship skills taught there and all seven responsible decision-making
  sub-skills, outside every course-level check. Grades 1 and 2 sample RD3 and RD4 only (units 9 and 16).
- **Why it matters.** C8 and C9 (cumulative checks) are read on one cumulative check per course; a reviewer finds one
  of the five competencies missing from kindergarten's.
- **Fix (the lead's call, not the writer's).** The cause is real: K, 1 and 2 have core checks in weeks 28 or 29 to 32,
  and 64 sessions fill 32 weeks. Options: (a) the lead allows the SEL year-end check, a watched rehearsal and a pictured
  page with no sitting, in week 32 for K to 2, which the after-core rule was not written to stop; (b) keep after unit 5
  and say plainly in Course-level checks that unit 6's sub-skills are checked only in their unit and sampled again in
  the next year's check 1 retrieval. Pick (a), so each year ends whole. Either way, the check rows and the Course-level
  checks intro must name what is left unsampled. Confidence: firm on the gap, judgment call on the option.

### 5. Medium. RS3 at the owner year is a planning style, not people whose cultures differ

LAYER frame. REPEAT yes (a standard narrowed to less than it says, lesson 4).

- **What is wrong.** CASEL.Relationship Skills.3 (our words): "Work and get along well with people whose cultures
  differ from yours". Grade 2 owns it for the band. Unit 18's teacher note makes "the different way ... a planning
  style" (a picture list against a word list). The row (g2-rel-different-ways) says only "a story partner's different
  way of doing a task", and grade 3's row, which the Seams table hands on to, assumes "a story partner from another
  place" and adds only "the respectful question".
- **Why it matters.** The owner year drops the culture the standard is about, and the seam to grade 3 breaks.
- **Fix.** In unit 18, make the story partner an invented child from another place who brings one way of doing the
  task from a game or chore at home (settled below), shown as one child's way and never as a whole culture's; keep "no
  child is asked to explain their own culture". Confidence: firm.

### 6. Medium. Two more owner codes are met only in part: SA2 and SO7

LAYER progression and frame. REPEAT yes (lesson 4).

- **What is wrong.** SA2 (our words) includes strengths "that come from your culture and the languages you speak";
  unit 17 (g2-sa-my-strengths) teaches a strength toward a goal and a teammate's, with culture and language only
  "welcome when offered". SO7 includes "the chances it offers"; the frame's own Handed-on row says "Beyond grade 2: the
  chance a situation offers", so grade 2 owns a code it teaches half of.
- **Why it matters.** Each band's owner row is the code met "at the band's full depth" (STANDARD section 3); a half
  taught at the owner year is the lesson 4 fault.
- **Fix.** Unit 17: the invented teammate's strength comes from speaking two languages (settled below), so the clause is
  taught on a character with no child asked. Unit 13: one SO7 case names a chance, not only a demand (settled below).
  For the lead: g2-sa-my-strengths and g2-soc-read-situation notes gain those words; the "Beyond grade 2" cell is
  rewritten. Confidence: firm.

### 7. Medium. A left-out unit breaks later units that have no earlier year to fall back on

LAYER frame. REPEAT new.

- **What is wrong.** The lens asks that a school can leave out a unit without breaking later ones, and STANDARD 5.6
  falls back to the previous year's row. That fails where a model is first made in the band: leaving out kindergarten
  unit 2 removes the feelings faces and calm-down steps that units 4 and 5 use the same year; leaving out grade 1
  unit 9 removes the problem size meter and I-statement frame that grade 2 units 15, 16 and 18 need, and no earlier year
  taught them.
- **Fix.** Add to "Carry it out and families" (or a Leave-out bullet): for kindergarten units 4 and 5 and grade 2
  units 15, 16 and 18, if the unit that makes the card was left out, the unit's first Understanding session teaches the
  card's one-step form itself before its own skills. Name the cards: feelings faces, calm-down steps (unit 2); problem
  size meter, I-statement frame (unit 9); stop-think-choose and goal steps (unit 6, used by units 8, 9, 11 and 12).
  Confidence: firm.

### 8. Medium. The Check session cannot hold what each unit asks of it in 20 minutes

LAYER frame. REPEAT new.

- **What is wrong.** Every unit's end evidence is a pictured page read aloud plus a watched rehearsal "per pair" from an
  unseen card, in one 20-minute Check session (and one shared Check and Respond session on the short path). With 30
  children that is 15 pairs for one adult to watch against look-fors after the page.
- **Fix.** Say in the Evidence bullet that the watched rehearsal is marked across the unit's last Application session
  and the Check session (pairs not yet seen go first in the Check), with the pictured page taken by the whole class in
  the Check session; on the short path, the page in the shared session and the rehearsal marked in the Application
  session. Lesson 19's "no score on the day a topic is first taught" still holds. Confidence: likely.

### 9. Medium. The Safety bullet names no guide

LAYER frame. REPEAT yes (lesson 22).

- **What is wrong.** Movement games, scissors, a school walk and litter pick-up are named with controls, but no guide by
  title with a free link, which lesson 22 asks of the Safety read bullet.
- **Fix.** Name a guide per hazard: for outdoor play and the walk, the U.S. Consumer Product Safety Commission's Public
  Playground Safety Handbook (https://www.cpsc.gov/s3fs-public/325.pdf, title checked 2026-11-25); for the school walk
  and clean-up, the school's own grounds and field-trip policy plus one state education department's school-grounds or
  field-trip guidance, found and linked by the safety agent. Confidence: firm on the gap.

### 10. Low. The I-statement has three wordings

LAYER frame. REPEAT new.

- APPROACH section field 9 gives "When you ___, I feel ___. I would like ___."; the frame gives "I feel ___ when ___"
  (grade 1) and "I feel ___ when ___. I would like ___" (grade 2); health kindergarten gives "I feel ___ when ___. I
  need ___." **Fix:** one wording in STANDARD section 7 (finding 1), and APPROACH field 9's example changed to it.
  Since health kindergarten teaches three parts a year before SEL grade 1 teaches two, the grade 1 step should start
  from health's three parts as retrieval rather than step down. Confidence: firm.

### 11. Low. Cultural picks: Ampe repeats PE, jan-ken is the game the class already plays, sources unnamed

LAYER frame. REPEAT yes (lesson 11 and lesson 23).

- Spot checks at source: **Ampe** holds: a Ghanaian schoolyard game for two or more, no equipment, clapping, jumping and
  a leg thrust, often described as mainly a girls' game (Wikipedia and Ghanaian press below; no single rulebook, so the
  sensitivity agent should take the rules from a Ghanaian education source). **Jan-ken** holds as the Japanese name for
  rock paper scissors, descended from Chinese hand games. The claim "no ritual meaning" holds for both.
- **Problems.** PE K to 2 unit 14 (grade 1, weeks 29 to 32) also picks Ampe, so a child meets it twice. Jan-ken is the
  same game most US classes already play under another name, so "beside the version the class knows" teaches a name,
  not something learned from the other friend, which is the grade 1 step for RS3. Neither source is named (lesson 23).
- **Fix.** Unit 11: a game whose rule the class does not know (settled below). Unit 5: keep Ampe in SEL kindergarten and
  ask PE to pick another clapping and jumping game for grade 1, or the reverse; the lead decides once. Name each source
  in the unit cell, or "Pending(sensitivity read)" in the gate's form. Confidence: firm.

### 12. Low. Kindergarten units 2, 3, 5 and 6 name no retrieval

LAYER frame. REPEAT yes (lesson 16 and 18).

- Unit 4 opens with the feelings faces; units 5 and 6 use the talk turn card and calm-down steps from units 1 and 2 but
  have no "Retrieval only:" line with the unit of last use, as grades 1 and 2 do. **Fix:** unit 2: none (nothing
  earlier is used); unit 3: calm-down steps (unit 2); unit 5: talk turn card (unit 1), calm-down steps (unit 2),
  feelings faces (units 2 and 4); unit 6: calm-down steps (unit 2), "everyone can join" (unit 5).

### 13. Low. No "no study stands behind this course" line and no logic model pointer

LAYER frame. REPEAT new.

- Bar part 9 item 8 and APPROACH ("Where the evidence is thin") put this on every course page, and C16's logic model sits
  there. The frame's course-wide rules are what the course page is written from. **Fix:** add a bullet: "Evidence. No
  study has tried this course; it is never called evidence-based or rated. The course page carries the logic model
  (C16)."

### 14. Low. Stale or missing wording

LAYER process. REPEAT yes (stale notes).

- For the lead 3 asks for a decision already taken: DESK-ANSWERS 2026-11-25 says one band file with a Year column meets
  "one frame per grade year" for SEL. **Fix:** rewrite it as a stale-line note with the replacement text for STANDARD
  section 2 ("Each grade year's part of the band frame is that year's frame; plan.py takes one course id per band
  (Cory, 2026-11-25)"), as For the lead 8 does.
- The Days bullet lacks the brief's sentence "Each unit's days include its end-of-unit assessment"; the Check session
  is described, but add the sentence.
- For the lead 5(c) "Health K to 2 rows have no cross_subject to SEL yet": state it as a row change, "health.csv rows
  k-meh-feeling-words, k-meh-calm-body ... gain sel: leans", without "yet".

### 15. Low. After-core checks crowd the same weeks

LAYER process. REPEAT new.

- Not a rule breach (the rule guards core weeks only), but in calendar.csv SEL check 2 shares week 26 with visual arts'
  check in all three grades; in grades 1 and 2 SEL's respond (week 27) meets health's check; in grade 2 week 11 holds
  SEL's respond and health's check. **Fix (lead):** decide whether after-core checks also avoid each other in K to 5;
  if so, SEL check 2 moves to week 25 or arts moves.

## Calendar check

All 24 calendar.csv rows for this course match the weeks the frame states (units 1 to 18, six checks, six respond
sessions); first and last school days fall inside those weeks. Against the core check weeks of the same grade
(kindergarten 14 to 18 and 29 to 32; grade 1 14 to 16, 19 and 29 to 32; grade 2 14 to 20 and 28 to 32), no SEL check or
respond session collides. Unit 15 (grade 2, weeks 11 to 16) runs through core check weeks 14 to 16, which is allowed.
frame.py numbers band days straight through (grade 1 starts at day 65); the frame's per-year session numbers agree with
that once the offset is taken.

## Lens checklist (course frame layer)

| Lens line | Result |
|---|---|
| A grade year repeating another with the same cases and depth | Met: each year's angle and every row's step differ (Seams table) |
| A sub-skill missing from a grade, or met once with no return | Met for placement; returns are retrieval lines (finding 12 for K) |
| Minutes a week stated; short path drops sessions, not units | Met (40 minutes a week; short path keeps units), with finding 3 on the counts |
| "Carry it out" cue and family activity per unit | Met, all 18 |
| A unit a school could not leave out without breaking later units | Missed for units 2, 6 and 9 (finding 7) |
| Self-management and relationship skills rehearsed, not discussed | Met in every unit's plan; at risk from the session budget (finding 2) |
| Health topics pointed to, not taught | Met in wording; the seam itself fails (finding 1) |
| Systems and unfair norms held to playground fairness in K to 2 | Met (units 5, 11, 13) |
| End-of-unit assessment of the skill, never a feeling | Met; feasibility finding 8 |
| Teacher note and reporting route on sensitive units | Met in every unit |
| Growth taught as practice and help | Met (units 3, 12, 17) |
| No spiritual framing of calming | Met |

## What is right and should not be touched

- The Year column, units numbered through the band, and the "Inside the band" seams table with what each year adds: the
  clearest band shape yet, and the one the other SEL bands should copy.
- Retrieval only, never a Given item, inside the band, with the leave-out exception named.
- Every row placed in the unit its progression note names; models introduced before use in every case checked (talk
  turn card, feelings faces, calm-down steps, stop-think-choose, goal steps, problem size meter, I-statement frame).
- Check placement off the core weeks of each grade, stated in the frame and matching calendar.csv.
- The SA4, SA7, SA9 rules (invented case or private page, never recorded), the role-play rule, neutral traits for SA6,
  families of every kind, costs per unit, the paper path.
- Core links: every cited core unit exists and the "taught before" and bridge cells hold against calendar.csv.

## What the other SEL frames should copy, and should not

- **Copy:** the band shape (Year column, through-numbering, inside-band seams table, models table with "after the
  band"); a C3 cell holding the one core link; checks after the second and fifth unit placed off that grade's core
  check weeks, named by week; per-unit carry-out, family activity, tools, Curio Class writes, cost; the evidence
  bullet's "step, not a rating"; the disclosure and sensitivity lines.
- **Do not copy:** the 11/8 sizes until the Desk answers (finding 3); a Days bullet without a session budget (finding
  2; grades 3 to 8 at 30 minutes and 9 to 12 at 40 need their own); a health or other after-core seam written without
  reading that frame's weeks (finding 1); a check plan that leaves the last unit unsampled without saying so (finding
  4); owner rows narrowed below the CASEL wording (findings 5 and 6); cultural picks not checked against PE's and arts'
  lists (finding 11).

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Kindergarten short path: a 12-session three-group unit is 6 (3 shared Understanding and Fluency, 2 Application, 1 Check and Respond); an 8-session two-group unit is 4 (2 shared, 1 Application, 1 Check and Respond) | States the counts the frame gives, keeping the extra session where the heavy units need it | frame.md, Days bullet |
| One opening per session: the calm-down routine and the retrieval item share the first 4 minutes | Two openings cannot fit a 20-minute session | frame.md, Days bullet |
| Unit 13 SO7 case: a new classmate's first day also offers a chance, being the first to say hello | Teaches the "chances it offers" half at owner depth with an invented case | frame.md, unit 13 |
| Unit 17 SA2: the invented teammate's strength is speaking two languages (helps a new classmate with a word) | Teaches the culture and language clause on a character; no child asked | frame.md, unit 17 |
| Unit 18 RS3: the story partner is an invented child from another place who brings one way of sharing the work from a game or chore at home, shown as that child's way | Restores culture to the owner row and matches grade 3's assumes | frame.md, unit 18 |
| Unit 11 game: a hand or clapping game whose rule the class does not know, not on PE K to 2's or arts K to 2's pick lists, source named | Jan-ken is rock paper scissors under another name | frame.md, unit 11 |

## For Cory

- **Unit sizes (Desk q-fix-sel-1).** The frame uses 4 of the 64 sessions for course-level checks (units of 11 and 8,
  short path 5 and 5) instead of your 11 and 10 (short path 5 and 6). Pick: accept for K to 2 with the session budget
  in finding 2, and have each other band decide its own sizes against its minutes. The other three SEL frames wait on
  this.
- **Supply ceiling.** About $55 to $60 printing a year plus about $21 once and small task supplies, for 30 children; no
  ceiling is set for SEL (money).

## What I could not judge

- Whether 20 minutes, twice a week, is enough for this load in kindergarten: no source sets session content at this
  age; finding 2 rests on arithmetic.
- The health frame's own order (its units 7 and 14): read only for this seam, not as a frame read.
- The library seam (For the lead 4): the library frames were not read.

## For the source list

- U.S. Consumer Product Safety Commission, Public Playground Safety Handbook: https://www.cpsc.gov/s3fs-public/325.pdf
  (61 pages, title page read 2026-11-25; free). For SEL and PE outdoor play safety lines.
- Ampe: https://en.wikipedia.org/wiki/Ampe_(game) and Ghanaian press (https://www.myjoyonline.com/ghana-month-the-game-that-requires-you-to-make-quick-decisions-with-your-legs/);
  consistent on the core pattern, no single rulebook; a Ghanaian education source is still to find.
- Jan-ken: https://en.wikipedia.org/wiki/Rock_paper_scissors and https://en.wikipedia.org/wiki/Sansukumi-ken (origin in
  Chinese hand games, dates disputed).

## Sources

- docs/courses/sel/STANDARD.md, APPROACH.md; docs/agents/lenses/sel.md; docs/ADOPTION-BAR-SUBJECTS.md part 9: the bar.
- docs/courses/health-grades-k-to-2/frame.md: the health seam (finding 1, 10).
- docs/courses/physical-education-grades-k-to-2/frame.md unit 14 and For the lead 8: the Ampe repeat.
- data/plans/calendar.csv: every week checked.
- The web sources above: spot checks of the cultural and safety facts.

# Expert read: scope and sequence of Media Arts, grades 3 to 5 (2026-11-26)

Course `media-arts-grades-3-to-5`. A cold read by the curriculum expert (PRODUCTION-PATH step 3), done as
docs/pipeline/briefs/sequence-read.md says, with build/scope-writes/ARTS-READ.md and ARTS-BRIEF.md. I did not write
the scope; this file is the only file I changed.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/arts.md, docs/ADOPTION-BAR-SUBJECTS.md section "2. Arts" (items 1 to 9
  and "Fails if"), docs/courses/arts/STANDARD.md and docs/courses/arts/APPROACH.md in full.
- docs/courses/media-arts-grades-3-to-5/scope-and-sequence.md and data/plans/media-arts-grades-3-to-5/days.csv (all
  192 rows), read cold.
- Beside them: the frame (docs/courses/media-arts-grades-3-to-5/frame.md, all of it), the 24 ma-g3 to ma-g5 rows of
  data/progressions/arts.csv, docs/courses/CALENDAR.md (grades 3 to 5 rows) and the course's rows in
  data/plans/calendar.csv, the ELA grade 3 days that carry SL.3.1, the media arts lines of
  data/standards/ncas-performance-standards-words.txt (all 54 grade 3 to 5 ids), the frame reads
  (docs/reviews/frame-media-arts-grades-3-to-5-codex-2026-11-25.md, frame-media-arts-grades-k-to-12-2026-11-25.md,
  frame-music-theater-media-arts-fixes-2026-11-26.md) and the arts DESK-ANSWERS entries.
- Gates: `scripts/plan.py check` (0 failures for this course), `scripts/sequence.py check media-arts-grades-3-to-5`
  (0 failures), `scripts/frame.py calendar` (media arts weeks 17 and 26, 17 and 25, 18 and 25, as the frame sets),
  `scripts/stale.py check` (nothing for this course). I also ran a short script over days.csv: every one of the 54
  ids sits in its own year, and every id has an end-of-unit row, but three ids have no teaching day (finding 1).
- No new outside source was opened for this read. The standards' wording rests on our own-words file (checked at
  source by the earlier arts reads); the timing and room judgments rest on the arts approach page and on memory of
  elementary specials schedules, marked so.

## Verdict

Sound in shape: the band-year rule, the four-unit year, the four processes in every unit, technique before making,
one critique and a revision before every end-of-unit assessment, and a wide range of works with their settings all
hold, and the gates pass. The biggest risk is two things a writer would build wrong days from: the three "how did
the showing go and what would we improve" ids (MA:Pr6.1.3b, 4b, 5b) are never taught before they are scored, and
year 5's second showing format is never shown, so its results cannot be compared; and the once-a-week path packs
four to seven course days (two works, a technique and a ten-minute retrieval) into one 40-minute session in six
units. The one change that matters most is to teach the Pr6 "b" ids on the rehearsal days and show both newscast
formats (finding 1, settled below); the once-a-week rebalance (finding 2) is the lead's frame change.

## Findings, most serious first

### 1. The Pr6 "b" ids are scored but never taught, and year 5 compares results of a format nobody shows

LAYER sequence. REPEAT yes (an owned part carried by no day, as in earlier reads). Confidence: firm (days.csv and
the words file agree).

- **What is wrong.** MA:Pr6.1.3b (describe the experience, share results, suggest ways to present better),
  MA:Pr6.1.4b (explain how a presentation went and what to improve) and MA:Pr6.1.5b (compare results of
  presentations and ways to improve) appear only on check day 2 and the respond day of units 4, 8 and 12 (days 63,
  127, 191). No Understanding, Fluency or Application day carries them; day 63's note teaches "sharing results" in
  the check day's own opener. Unit 12 is worse: the talk item on day 191 asks the student to compare "the two
  formats' results", but only the live newscast is shown (day 190); the printed news sheet is "laid out" on day 189
  and never put before an audience, so there is no second result to compare.
- **Why it matters.** A student is scored on a routine met for the first time on the day of the score, which the
  frame forbids ("No score comes from the day a technique is first taught"), and the unit 12 item cannot be answered
  as written. A writer following days.csv would build no teaching for these ids.
- **The fix (settled below).**
  - Day 61 (unit 4, revision and rehearsal): after the run in roles, the watching crew says what it noticed; the
    crew describes the run's experience, shares that result and names one way to present better on the
    screening-plan card. Add MA:Pr6.1.3b to codes.
  - Day 124 (unit 8, run-through): after each run, the crew explains how the run went and one thing to improve,
    on the screening-plan card. Add MA:Pr6.1.4b.
  - Day 185 (unit 12, two formats weighed): the teacher models comparing two presentations' results on a Curio
    Class example (audience notes from a live run and from a printed sheet). Add MA:Pr6.1.5b.
  - Day 189 (unit 12, rehearsal in both formats): each crew presents its printed news sheet to a partner crew and
    logs one audience result on the screening-plan card; day 190's live showing gives the second result. Add
    MA:Pr6.1.5b. Day 191's talk item then compares the two logged results.
  - Day 63's note drops "sharing results" from the opener (it is now taught on day 61); the opener gathers what
    the screening audience noticed as material for the talk item only.

### 2. The once-a-week path does not hold in the demonstration sessions of units 3, 4, 7, 8, 11 and 12

LAYER frame and sequence. REPEAT new (the first arts scope read). Confidence: likely (strong reasoning from the
session's minutes; the counts are the frame's, settled at the frame read).

- **What is wrong.** The session counts are the frame's (year 3: 7, 9, 6, 6; year 4: 7, 9, 6, 6; year 5: 8, 9, 5,
  6), and the scope merges days to fit them. In the ideas-and-crew units (2, 6, 10, nine sessions each) a session
  merges two or three days, and two check sessions hold little but a self-check and a kept card. In the
  making-and-judging and screening units one opening session carries far more:

  | Unit | Opening session | What it holds in one 40-minute session (31 teaching minutes) |
  |---|---|---|
  | 3 | 35-40 | hook (Marey), 10-minute retrieval, order technique, Luminaris with its setting, stress technique, named criteria |
  | 4 | 53-57 | hook (Méliès), 10-minute retrieval, blending technique, Sigwan, the source log, the retelling study |
  | 7 | 99-104 | hook (Adams), 10-minute retrieval, balance and contrast, Iturbide, refining technique, criteria on production steps |
  | 8 | 115-118 | hook (Painlevé), 10-minute retrieval, coordinating forms, research with two sources, CyberPowWow |
  | 11 | 165-169 | hook (Keaton), 10-minute retrieval, the cut, Bread and Alley, setting criteria |
  | 12 | 179-185 | hook (Dianshizhai), 10-minute retrieval, newscast parts and voice-over, Posada and a newsreel, gathering sources, interview technique, hand-offs, two formats weighed |

  After the retrieval, about 21 minutes remain for two techniques and two or three works with their settings.
  MA:Cn10.1.5a (gather sources, including an interview with a consenting adult) and MA:Pr6.1.5a (weigh two
  formats) in unit 12, and MA:Cn10.1.3a (the source log) in unit 4, are owned parts that cannot be taught in their
  share of that session; on a busy teacher's reading they are cut.
- **Why it matters.** The brief asks that the once-a-week path hold with no owned part cut, and the lens names
  "technique taught, not hoped for". Here, on that path, a technique and a work's setting get a few minutes each.
- **The fix.** Two parts.
  - **Inside the frame's counts (settled below), units 3, 7 and 11.** The class viewing is not scored, so it joins
    the revision session as its last ten minutes, which frees a session for a second demonstration:
    unit 3: 35-37 (hook, retrieval, order, the drill as opener); 38-40 (Luminaris, stress, criteria); 41-44
    (making with critique); 45-46 and 50 (revision, criteria practice, the viewing); 47-48 (check); 49 (respond).
    Unit 7: 99-101; 102-104; 105-106; 107-108 and 112; 109-110; 111. Unit 11: 165-167; 168-171 (drill as opener,
    criteria set, making with critique); 172-173 (revision and viewing, as now); 174-175; 176. Unit 11 stays at
    five sessions and gains no second demonstration; its 12 days are the lightest, so it holds.
  - **For the lead (a frame change).** Units 4, 8 and 12 have no unscored day to fold. Move one session in each
    year from the ideas-and-crew unit to the screening unit (year 3: 7, 8, 6, 7; year 4: 7, 8, 6, 7; year 5: 8, 8,
    5, 7). The ideas-and-crew unit merges its two check sessions (30-31, 94-95, 160-161) into one, which they can
    take since both are kept-card and self-check days with no talk item. The screening unit gets two demonstration
    sessions: unit 4: 53-55 and 56-57; unit 8: 115-116 and 117-118; unit 12: 179-181 and 182-185 (after finding
    3's swap: interview, then gathering sources, then hand-offs and formats). The weeks still work with every check
    on its week: for example year 5 runs unit 9 in weeks 1 to 8, unit 10 in 9 to 16, unit 11's first session in
    17, the check in 18, respond in 19, unit 11's last four in 20 to 23, unit 12's first session in 24, the check in
    25, respond in 26 and unit 12's last six in 27 to 32 (32 sessions). Years 3 and 4 run the same way (the
    making-and-judging unit's first session falls before the mid-year check). If the lead keeps the counts, the
    scope must at least move day 182 (gathering) into the making session 186-187 and day 185 (formats) into the
    rehearsal session 188-189, and say that the opening session there is two works and one technique only.

### 3. Unit 12 uses the interview a day before it teaches it

LAYER sequence. REPEAT yes (used before taught). Confidence: firm.

- **What is wrong.** Day 182 gathers sources including "an interview with a consenting adult at school"; day 183
  teaches "Interview and voice-over in steps: questions planned, listening".
- **Why it matters.** Students conduct an interview, an owned part of MA:Cn10.1.5a, before planning questions or
  practicing listening; the interview evidence on the source log comes from an untaught step.
- **The fix (settled below).** Swap the content of days 182 and 183: day 182 teaches interview and voice-over in
  steps (MA:Pr4.1.5), day 183 gathers the sources with the interview (MA:Cn10.1.5a, with its health-steps note
  moved with it), day 184's hand-off drill stays and its note reads "practice of days 180 and 182". The Arc
  paragraph of unit 12 changes to match.

### 4. Several items list a code but ask only some of its parts

LAYER sequence. REPEAT yes (part coverage, as in earlier reads). Confidence: firm against the words file.

| Day or item | Code | Part not asked | Change |
|---|---|---|---|
| Day 51, year 3 year-end, fresh plan | MA:Cr1.1.3 | "several ideas using different tools or materials" (the task asks two ideas) | three ideas, at least two tools or materials, as the unit 2 look-for |
| Day 51, talk item | MA:Cn11.1.3a | online behavior, cultural life | add one invented online case sorted fair or unfair with a reason, or list the code as sampling its daily-life and values parts only and keep online behavior on the unit 1 kept card |
| Day 113, year 4 year-end | MA:Cr2.1.4 | test; presentation in mind | "two quick plans combined, with one test named and the showing in mind" |
| Day 177, year 5 year-end, talk item | MA:Cn11.1.5a | history, community | add one way the ad's form differs from a trade card of the 1880s (history), for a named community (public or invented) |
| Day 177, fresh proposal | MA:Cr2.1.5 | goals | "a proposal with its goal and audience, and one test named" |
| Unit 2 and unit 6 look-fors (days 30, 94) | MA:Cr2.1.4 | test; presentation | the unit 6 storyboard look-for: "two plans combined after a test, with the goal and the showing kept" |
| Unit 4 screening look-for (day 62) | MA:Pr4.1.3 | content "from subjects" | the look-for names the school-subject fact in the blended piece |
| Unit 4 talk item (day 63) | MA:Pr6.1.3b | "describe the experience" | one sentence describing the screening's experience, one result shared, one improvement |
| Unit 9 look-for (day 143) | MA:Cn11.1.5a | history | the investigation card's conclusion names one fact of the form's history from the trade-card work card |
| Unit 10 look-for (day 160) | MA:Cr2.1.5 | goals | "a proposal naming the goal and the audience, and a model tested with its result" |

All are item wording inside the standards' own limits (settled below); none moves a code.

### 5. Rows used earlier the same year are leaned on with no retrieval

LAYER sequence. REPEAT yes (same-year retrieval missing, as in earlier sequence reads). Confidence: firm against
sequence-write rule 2 as quoted in the brief.

- **What is wrong.** The retrieval table names only each unit's progression `assumes` row (the year before's pair).
  Several units lean on a row taught earlier the same year with no retrieval: unit 3 (24-frame flip book and
  spacing, ma-g3-craft, unit 2) on day 41; unit 4 (crew roles, ma-g3-craft, last used day 32, eleven weeks and a
  unit earlier; kept frames from units 2 and 3) on day 58; unit 7 (capture skills, ma-g4-craft, unit 6) on day 105;
  unit 8 (stop-motion and roles, ma-g4-craft) on day 120; unit 11 (capture in roles, ma-g5-craft) on day 170;
  unit 12 (emphasis, ma-g5-make, and the media-literacy checklist, ma-g5-society) on day 186.
- **Why it matters.** The frame itself says unit 4's screening "uses the year's crew roles" and unit 8's "the year's
  stop-motion"; a crew that has not used its roles since week 16 starts its making day cold.
- **The fix (settled below).** A five-minute retrieval warm-up in the opener of each named making day (APPROACH "How
  a day opens": a warm-up from earlier technique), named in the note and in `retrieves`: day 41 ma-g3-craft;
  day 58 ma-g3-craft and ma-g3-make; day 105 ma-g4-craft; day 120 ma-g4-craft; day 170 ma-g5-craft; day 186
  ma-g5-make and ma-g5-society. Add a line to the .md's Readiness and retrieval section: "Same-year retrieval" with
  these six rows. No readiness check is needed (no row is two grades idle), and no unit's first day changes.

### 6. Unit 11 applies the kept criteria card to a sequence that is still being revised, and leaves day 175 nearly empty

LAYER sequence. REPEAT new. Confidence: likely.

- **What is wrong.** Day 172 holds the revision and, in the same session, the kept criteria card for MA:Re9.1.5
  "applied to a classmate's sequence", while that classmate is revising it; the frame's evidence line asks for "a
  classmate's finished sequence". Day 175, check 2, then holds only scoring that card after the session and a
  self-check.
- **Why it matters.** The scored card judges an unfinished piece, and a 40-minute check day has no student task.
- **The fix (settled below).** Move the kept criteria card from day 172 to day 175: on day 175 each student applies
  their own criteria (set on day 169) to a classmate's finished sequence and one of its production steps, with aim
  and setting named and feedback that names a look-for, then self-checks. Day 172 keeps the revision and the logged
  change only (codes MA:Cr3.1.5b). On the once-a-week path the card goes in the 174-175 check session, which then
  holds the written item (10) and the card (about 15) with set-up and clean-up: it fits.

### 7. Two flagged works have no sensitivity line in their day's note

LAYER sequence. REPEAT new. Confidence: firm (the frame's Sensitivity reads bullet lists both).

- **What is wrong.** The frame flags unit 10 (Chinese ink-wash animation) and unit 11 (an Iranian filmmaker). Day
  147 (Where Is Mama) and day 167 (Bread and Alley) name neither flag; day 167 names only the dog.
- **The fix (settled below).** Day 147: "Sensitivity: Chinese ink-wash animation from a Shanghai studio; the
  sensitivity agent reads the studio's or a museum's page first; the style is studied, not imitated as a tradition
  students claim." Day 167: "Sensitivity: an Iranian filmmaker; the sensitivity agent reads a film archive's page
  and the maker's published words first."

### 8. Note text that a writer would copy wrong

LAYER sequence. REPEAT new. Confidence: firm.

- Days 48 and 110 are talk-only check days (the written item was on days 47 and 109), but their notes copy the
  talk-and-written form ("written item 10 ... slack 5"). Change to: "Talk check day: set-up 4, six groups of five at
  the teacher's table about 3 minutes each (18) while the others self-check and finish work, self-check 5, clean-up
  3, slack 10."
- "How this file is read" says the tool, space, ethics and role items "are never check-day items", but the
  mid-year checks (days 33, 97, 163) sample MA:Cn11.1.3b, 4b and 5b by a paper sort or case. Change to: "are never
  end-of-unit check-day items; a mid-year check samples their 'examine' part by a fresh sort or case on paper."

### 9. Folding the drill days of the short year also cuts the baseline look

LAYER sequence. REPEAT new. Confidence: likely.

- **What is wrong.** Seven of the twelve fold days (5, 37, 68, 82, 102, 134, 149) are where the baseline look at the
  unit's main look-for ends. Folding them leaves the last rotating group unobserved, so those students have one
  mark in the unit, not two (APPROACH "Growth").
- **The fix (settled below).** Add to the fold table's lead line: "Where the fold day ends the baseline look, its
  last rotating group is observed in the next day's opener." Nothing else changes.

### 10. The 30-minute period moves end-of-unit talk items onto making days

LAYER frame. REPEAT new. Confidence: judgment call.

- **What is wrong.** "A shorter period (30 minutes)" moves the talk items to the unit's last three making days.
  APPROACH "Kinds of day" says the end-of-unit assessment is always a check day, and those making days already hold
  the critique and ten rotating marks a day; the teacher would watch the table and the room at once, which the
  frame rules out.
- **The fix (for the lead).** The talk items cannot go to the respond day (a respond day never assesses), and a
  30-minute check day cannot hold both items. So name this as the one stated exception to APPROACH for the
  30-minute period, and put the talk groups only on the revision day, where no critique runs and the rotating marks
  can move to the two earlier making days. The lead decides, since it bends an approach-page rule.

### 11. `school_day` and data/plans/calendar.csv count the same weeks a day apart

LAYER process. REPEAT new. Confidence: firm.

- days.csv puts course day 1 on school day 2 and day 33 on 82; calendar.csv (from the frame) puts unit 1's start on
  school day 3 and the mid-year check on 83. Years 4 and 5 also differ in base (days.csv 161 and 321 on, calendar.csv
  counts each year from 1, as frame.py reads it). Every check lands in the same week either way, so no student or
  teacher is affected. For the lead: say once which count a later tool should read, or regenerate one from the
  other, so a future gate comparing the two does not fail on this course.

## What is right and should not be touched

- The band-year rule is stated once and kept: each year claims only its grade's 18 ids, 54 in all; the mixed-class
  line is on the first page; each year's heading names its grade.
- Every unit has all four processes by day, a work studied with its setting on a work card, technique taught in
  steps and drilled before the making that needs it, one critique by the describe, ask, suggest routine, a revision
  before the end-of-unit assessment, a showing, and a portfolio piece with a reflection.
- Unit 1 models the critique before its first use (day 10 before day 11); the readiness table is right that no row
  is two grades idle, and every unit's first day stays clean.
- The works range widely in each year (three continents or more, twelfth century to 2016, living makers each
  year), with the frame's sensitivity notes carried on the days for all but two (finding 7).
- The course-level checks sit on CALENDAR.md's weeks, sample the units before the one just finished and say so,
  and arts as specials need no stagger.
- The rotating look-for design for the tool, role and ethics ids keeps check days light and is applied the same in
  every unit.
- The candidate cells are all settled, with reasons, and the two kept second works sit in ten minutes of a study day.
- The ten-days-short path folds only unassessed drill days, four a year, and the arithmetic is right for two
  meetings a week.

## What I could not judge

- Whether 24 minutes of screening in six groups of five fits a real elementary room with a partner class as
  audience; a classroom trial would tell.
- The rights lines of the works the frame leaves to the unit plans (Sigwan, La Mort du Gandji, the Ōfuji film, the
  Ghana posters); not this layer's job.

## Settled by the expert

| Choice | Reason in one line | File |
|---|---|---|
| Teach MA:Pr6.1.3b on day 61, MA:Pr6.1.4b on day 124, MA:Pr6.1.5b on days 185 and 189; the printed news sheet shown to a partner crew on day 189 | scored ids need a teaching day, and year 5's comparison needs two showings | days.csv; scope-and-sequence.md units 4, 8, 12 |
| Once-a-week merges for units 3, 7, 11 as in finding 2 (viewing joins the revision session; a second demonstration session) | keeps the frame's counts and halves the opening session's load | scope-and-sequence.md, Shorter path table |
| Swap the content of days 182 and 183 | the interview is taught before it is used | days.csv; scope-and-sequence.md unit 12 |
| Item wording in finding 4's table | each listed code asks each of its parts | days.csv notes and goals of days 51, 62, 63, 113, 177; scope-and-sequence.md assessment lines and Course-level checks table |
| Same-year retrieval warm-ups on days 41, 58, 105, 120, 170, 186, with `retrieves` filled | rule 2 for rows used earlier the same year | days.csv; scope-and-sequence.md Readiness and retrieval |
| Kept criteria card moved from day 172 to day 175 | it must judge a finished sequence; the check day gets its task | days.csv; scope-and-sequence.md unit 11 |
| Sensitivity lines on days 147 and 167 | the frame flags both works | days.csv |
| Notes of days 48 and 110; the "never check-day items" sentence | copy errors a writer would build from | days.csv; scope-and-sequence.md "How this file is read" |
| Baseline look finishes in the next day's opener when a fold day ends it | keeps two marks a unit on the short year | scope-and-sequence.md, Shorter path |

## For the lead (not Cory)

- Finding 2's session rebalance (one session from each ideas-and-crew unit to the screening unit) is a frame change.
- Finding 10's 30-minute exception to APPROACH.
- Finding 11's two school-day counts.

## For Cory

Nothing new on scope, money, people or audience. The supplies ceiling stays where the frame puts it (frame "For
the lead" item 6).

## For the source list

None: no outside source was opened for this read.

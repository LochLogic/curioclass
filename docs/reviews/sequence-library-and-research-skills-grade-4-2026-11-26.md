# Expert read: scope and sequence, Library and Research Skills, grade 4 (2026-11-26)

Course `library-and-research-skills-grade-4`. Read cold as a grade 4 teacher and school librarian, a district
curriculum lead and a researcher, per docs/pipeline/briefs/sequence-read.md and build/scope-writes/AFTERCORE-READ.md.

## What I read

- docs/agents/EXPERT.md; docs/agents/lenses/library.md; docs/ADOPTION-BAR-SUBJECTS.md (the shared core and part 11);
  docs/courses/library/STANDARD.md and APPROACH.md (by their use in the frame); build/scope-writes/AFTERCORE-BRIEF.md;
  docs/pipeline/briefs/sequence-write.md rules 2 and 3.
- Under review: docs/courses/library-and-research-skills-grade-4/scope-and-sequence.md and
  data/plans/library-and-research-skills-grade-4/days.csv (30 rows).
- Beside them: the course frame.md; the nine grade 4 rows of data/progressions/library.csv; data/standards/aasl-words.txt
  for the nine owned ids; docs/courses/CALENDAR.md (rule 1 and the grade 4 table); data/plans/calendar.csv for grade 4
  (ELA, math, science, social studies, SEL units and checks); docs/reviews/frame-library-and-research-skills-grade-4-codex-2026-11-25.md;
  DESK-ANSWERS entries on library and the 2026-11-26 sources answer; later.csv L107 and L149.
- Source opened: the continuum's 3 to 5 band file, on disk at
  S:\CurioClass-sources\library\aasl-2026-11-21\esifc-3-5\esifc-priority-3-5.docx (read as text with `python -I`,
  nothing copied), grade 4 column. The NetSmartz resources listing (https://www.missingkids.org/netsmartz/resources),
  opened 2026-11-26.
- Earlier reads for the REPEAT tag: sequence-library-and-research-skills-kindergarten-2026-11-26.md and
  sequence-library-and-research-skills-grade-1-2026-11-26.md.

Gates: `scripts/plan.py check` (no library failure; the only failures are algebra-ii items), `scripts/frame.py
calendar` (grade 4 library weeks 14, 29), `scripts/sequence.py check` (0 failures), `scripts/frame.py check` (0
failures, 4 units, 30 days), `scripts/stale.py check` (121 files, 0 failures).

## Verdict

The scope and sequence is sound: every owned id sits on a teaching day, a practiced day and an assessment, the four
inquiry cycles run in a defensible order on neutral, closed source sets, the calendar weeks match CALENDAR.md, and the
leans that come later carry their bridges. The biggest risk is small but would be built wrong: in units 1 and 2 each
grade 3 retrieval sits one day after the move that needs it. The one change that matters most is the retrieval swap
settled below; the shorter path also needs two repairs before it holds. Nine findings, none serious.

## Findings, most serious first

### 1. Retrieval comes the day after the move it supports, in units 1 and 2 (moderate)

LAYER sequence (the day mapping is copied from the frame's seam table). REPEAT new.

**What is wrong.** Unit 1: day 2 models the three-way search with key words and the stop rule, but key words and safe
searching (g3-key-words, g3-safe-searching) are retrieved on day 3; day 2 instead retrieves g3-research-questions,
whose move day 1 already used. Unit 2: day 8 teaches primary and secondary sources but g3-source-kinds-and-makers is
retrieved on day 9; day 9 teaches honest use and the source list but g3-source-list is retrieved on day 10; day 8's
retrieval is g3-notes-in-boxes, which day 7 already built on. Every retrieval lands one day late.

**Why it matters.** Retrieval exists to wake the grade 3 move before the grade 4 move is built on it (C4, rule 2). A
student who has forgotten key words meets the three-way search cold, and the ten-minute reteach where many miss it
comes after the show-me it should have supported.

**Fix (settled below).** Day 2 opens with key words and a synonym plus one scenario card (g3-key-words,
g3-safe-searching); day 3 opens with three questions on a picture, one thick (g3-research-questions), before the
narrowing practice. Day 8 opens with labeling two sources and naming each maker (g3-source-kinds-and-makers); day 9
with a source list line for one cover (g3-source-list); day 10 with two key-word notes from a short paragraph
(g3-notes-in-boxes), before the own-box notes round. Day 7 stays clean for the hook; its model may start from a grade 3
key-word box as the "before" picture, inside the show-me, not as a task. Update the `retrieves` column, the unit
bullets and the "How the year sits" line to match; the frame's seam table then differs, a line for the lead.

**Confidence.** Firm (the days' own goals against their retrieves column).

### 2. The shorter path does not hold on two counts (moderate)

LAYER sequence. REPEAT yes (grade 1 read, finding 1: fold-ins and the short session overfill their days).

**What is wrong.** (a) The 30-minute session gives about 26 working minutes with setup cut to 2 minutes at each end,
but days 12 and 29 are 27-minute sittings, so neither fits. (b) Fold-in 2 removes day 10, the only practice day for
unit 2: purpose sorting, the ad, own-box notes and the honest-use fixes would then be scored on day 12 after only
show-me days and an exit ticket, against the frame's "scored on a day after the move was practiced". (c) Two lost
weekly sessions need two fold-ins, and the page names three.

**Why it matters.** C2 asks for a short path that holds with nothing assessed cut; a teacher on 30-minute periods
would run out of time in the two longest sittings.

**Fix (settled below).** (a) On the 30-minute path, sitting days have the papers on the desks before the class
arrives, so the opening setup is about 1 minute and 27 minutes fit; say so in the short-session bullet. (b, c) Drop
fold-in 2. Folding day 3 and day 13 saves two sessions (about 10 school days), leaving 28 days; day 10 stays. If a
school loses a third session, fold day 6 (unit 1 respond) into day 15's regrouped reteach, which already works from
unit 1's mid-year results.

**Confidence.** Firm (the page's own minute budgets).

### 3. Three assessment rows ask only part of the id they claim (moderate)

LAYER sequence. REPEAT yes (grade 1 read, finding 3).

**What is wrong.** AASL.I.B.2 is "Plan the steps and sources that will fill what you still do not know". Days 5, 14
and 29 score the narrowed part, the questions and "a plan whose sources fit its questions", but no rubric line scores
the "what you still do not know" part, though day 1 models it as the plan sheet's line. AASL.VI.A.2 is "Explain what
fair and honest use ... means": day 29 asks for "one not-yet-honest case fixed" with no reason, so it samples the fix,
not the explaining.

**Why it matters.** The unit plan writer copies the check rows; a plan with no gaps line, or a silent fix, would
score as meeting the id.

**Fix (settled below).** Days 5, 14 and 29: add the rubric line "the plan names what I still do not know, and each
step fills one of those" (no minutes added: the plan sheet already holds the line). Day 29: "one not-yet-honest case
fixed with a reason", as day 12 has it (about 1 minute inside the 27).

**Confidence.** Firm (aasl-words.txt against the day rows).

### 4. Unit 3's observation depends on rain in mid-winter (moderate)

LAYER sequence (and progression: the row note differs). REPEAT new.

**What is wrong.** Day 18 starts a week-long observation of how schoolyard soil changes after rain; it runs in weeks
18 and 19, which in a late-August start is about mid-January. In much of the country the ground is frozen, snow
covered or dry that week, and no teacher can schedule rain. The page offers no fallback for the observation group
(the survey branch and the home picture sequence exist, but are not named as the in-class fallback). The progression
row note says "birds at a feeder for a week", the frame and scope say soil after rain; a writer will not know which
holds.

**Why it matters.** A group with nothing to observe cannot tally on day 19 or explain its plan on day 20, the unit's
owned evidence for AASL.V.C.2.

**Fix (settled below).** Day 18's note: "If no rain falls or the ground is frozen, the observation group records what
the week offers at three set spots (where frost, puddles or snow last longest), or works from the printed schoolyard
picture sequence in class; the steps and the tally are the same." Keep soil after rain as the scope's case; the lead
may align the g4-class-survey row note in data/progressions/library.csv (a progression line, not the expert's).

**Confidence.** Likely (reasoning from the calendar; weather varies by region).

### 5. Two hosts are not in step in the weeks the scope says (minor)

LAYER sequence. REPEAT new.

**What is wrong.** Unit 2: the scope calls science grade 4 unit 2 (energy resources) a host "in the same weeks", but
calendar.csv puts it in weeks 4 to 10 and the inquiry day 11 is week 11, after that unit ends. Unit 1: social studies
grade 4 unit 2 opens in week 4 (day 17), the same week as the day 4 inquiry; a research project usually sits later in
that unit (weeks 5 to 8). Energy resources can also drift to climate policy, which the K to 5 neutral rule keeps out.

**Why it matters.** A teacher scheduling against the named host will find it finished or not yet started.

**Fix (settled below).** Unit 2's host line and day 11's note: "ELA grade 4 unit 2's animal defenses research is the
in-step host; science unit 2's energy resources question ended in week 10 and may be reused as a finished question,
kept to how a resource is made and used, not to policy." Unit 1's host line and day 4's note: "day 4 most often runs
on the stand-alone Arctic question; the plan carries into social studies' project in weeks 5 to 8."

**Confidence.** Firm (calendar.csv).

### 6. Day 4, day 11 and day 12's items are tight for 29 minutes (minor)

LAYER sequence. REPEAT yes (grade 1 read, finding 5: a day that holds more than its minutes).

**What is wrong.** Day 4 holds a plan, searches in two kinds, reading the answering part, judging its maker, a
one-line answer with its source line, a partner share and the self-check, with no minutes named. Day 11 holds notes
from two sources, two candidate lines, a source list, a pair share and the self-check. Day 12's items part (about 7
minutes) now carries what each kind can tell, a three-page purpose sort, the ad and an accuracy check that needs a
second source read.

**Fix.** Name minutes in day 4's note (plan about 6, search two kinds about 10, judge and answer about 5, partner
about 3, self-check about 4) and day 11's (notes about 13, the two lines about 4, source list about 3, share about
3, self-check about 4). Day 12: the accuracy item gives the second source as two printed sentences beside the
statement, so the 7 minutes hold.

**Confidence.** Likely.

### 7. AASL.V.C.2's check can be met by describing a plan the student watched (minor)

LAYER progression (the check form is the row's "checked alone" line), sequence. REPEAT yes (the lens's "recall"
error; kindergarten read, finding 2).

**What is wrong.** Day 20's written part asks each student to explain the group's plan from days 18 and 19. A student
who rode along in a group can describe it without ever working out a way to find something out; no scored task asks
for a new way on a new question, though day 17 practices exactly that.

**Fix (judgment call, for the lead).** Add one line to day 20's written part: "for a new neutral question no source
holds, which kind of plan would you use and what is its first step?" (about 2 minutes; the day goes to about 28 of
29). Day 29's "why a survey or an observation answers" line then samples it again.

**Confidence.** A judgment call (the row sets the check form; reasonable reviewers differ).

### 8. Source notes are stale or overstated, and the projector page has no swap note (minor)

LAYER sequence. REPEAT new.

**What is wrong.** (a) "How the year sits" says the continuum's 3 to 5 band file is not loaded, so the candidate days
rest on the frame's reading. The file is on disk (downloaded 2026-11-25, README in its folder); I checked the grade 4
cells the scope uses: gaps in prior knowledge, predicted answers, accuracy and relevance within a source, restating
others' ideas, group research to a shared product, plagiarism strategies including quoting, media accuracy and
purpose, and assessing own work to teacher criteria. All match. L149 is its entry into the source store, not its
first reading. (b) Days 2 to 4 and 23 are said to "lean on" the free grades 3 to 5 digital-citizenship presentation,
but the frame names it for the sensitivity read only and no day uses it. The listing shows the title "Being a Good
Digital Citizen: Grades 3-5"; downloading needs a sign-in, so the kit itself stays a browser check. (c) Day 2's
projector option shows a live results page with no dated capture or swap note (lens, Day errors).

**Fix (settled below).** (a) Reword: "the band file is on disk and was read by the frame and checked by the expert
2026-11-26; its store entry waits on L149." (b) "No day leans on the digital-citizenship presentation; it is a
sensitivity-read source only (browser check: download needs a sign-in)." (c) Day 2's note: "the teacher checks the
page the same day; the printed results page is the swap."

**Confidence.** Firm (files and listing opened).

### 9. Unit 4's owned codes reach no course-level check (minor)

LAYER frame. REPEAT yes (L107 family of findings).

**What is wrong.** AASL.V.A.3 and AASL.I.C.3 are sampled only in unit 4. The scope names them and says why (rule 3
allows that), and its For the lead item 2 offers a 3-minute year-end item. The year-end sitting is already 27 of 29
minutes, so the item cannot be added without trimming another part.

**Fix.** Keep as written this pass; at the frame pass the lead may trade day 29's three-page purpose sort for two
pages (about 2 minutes) and add one change-log line for one piece of advice on a sample unit 2 note sheet (earlier
content, as rule 3 asks).

**Confidence.** Firm on the fact; a judgment call on the trade.

## Checked and right (do not touch)

- Every owned id (I.B.2, IV.B.1, I.B.1, IV.B.4, VI.A.2, V.C.2, II.D.2, V.A.3, I.C.3) sits on a show-me, a practiced
  or inquiry day, and its unit's end; none is claimed outside the frame's owned rows; `~` codes match the rows.
- school_day = 5 x course day puts units in weeks 1 to 6, 7 to 13, 16 to 21 and 22 to 28, and the checks in weeks 14
  and 29, as the frame and CALENDAR.md's grade 4 row give; library is a special and does not count in the stagger.
- No readiness check is needed: every assumed row is a library grade 3 row; V.C.1 and VI.B.2 are revisited codes,
  not assumed rows, and g4-own-question's g3-research-questions comes back through g4-narrow-and-plan on day 23.
- Course-level checks draw from earlier units and say so; no task form repeats within two weeks; II.D.2's exchange
  is collected once (day 20).
- Day 20's observed exchanges (70 seconds a pair for 15 pairs, three results recorded apart) fit the class of 30.
- Leans that come later (ss4-primary-source, e4-firsthand-secondhand) carry the bridge on day 8 and borrow no voyages
  content; neutral case sets throughout; honest use without shaming; survey and interview rules on days 16 to 20;
  the shared skill cards are this course's own, and no SEL shared card is used, so none needs quoting.
- Every candidate cell is settled with minutes inside its day.
- Unit 4's product, feedback round, revision and gallery give the year a made and shared product (bar item 6).

## Lens checklist (scope and sequence layer)

| Line | Status |
|---|---|
| Host task from another course named | Met (finding 5 fixes two week claims) |
| Source judging not a website checklist | Met at grade 4 depth: purpose and the ad on the page, plus one statement checked against a second source; lateral reading starts in grade 5 (g5-first-lateral-check) |
| Citation unit has research to cite | Met (day 11, unit 4) |
| End-of-unit assessment does the skill, not recall | Met, with finding 7 as a judgment call |
| No AASL text copied, no alignment claim | Met (own words only) |
| Live web page with dated capture or swap | Missed on day 2's projector option (finding 8) |
| No paid database or library visit | Met |
| No product or company on a student page | Met (the presentation's maker is named only in the frame's sensitivity line) |
| No claim the method raises scores | Met |

## Stale notes

stale.py: 0 failures. By hand: the "not loaded" line on the band file (finding 8a); the frame's seam table will
disagree with the scope once finding 1 is applied.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Retrieval swap: day 2 g3-key-words and g3-safe-searching; day 3 g3-research-questions; day 8 g3-source-kinds-and-makers; day 9 g3-source-list; day 10 g3-notes-in-boxes | Each grade 3 move is woken before the day that builds on it | days.csv (notes, retrieves), scope-and-sequence.md |
| 30-minute path: sitting papers on desks, 1-minute opening on sitting days | Days 12 and 29 fit 27 minutes | scope-and-sequence.md, Shorter path |
| Drop fold-in 2 (day 10); fold days 3 and 13; day 6 into day 15 only if a third session is lost | Unit 2 keeps its practice before scoring; two sessions for 10 school days | scope-and-sequence.md, Shorter path |
| Rubric line "the plan names what I still do not know, and each step fills one" on days 5, 14, 29 | Asks the whole of AASL.I.B.2 | days.csv, scope-and-sequence.md |
| Day 29: the honest-use case fixed "with a reason" | Asks the explaining in AASL.VI.A.2 | days.csv |
| Day 18 weather fallback (frost, puddles or snow at three set spots, or the printed picture sequence) | Week 18 is mid-winter | days.csv |
| Host lines: ELA unit 2 the in-step host for unit 2; science energy resources as a finished question kept off policy; day 4 most often on the stand-alone | calendar.csv weeks | days.csv, scope-and-sequence.md |
| Minutes named on days 4 and 11; day 12's second source as two printed sentences | Fit 29 minutes | days.csv |
| Source-note rewording (band file on disk, presentation a sensitivity source only, day 2 swap note) | Accurate and current | scope-and-sequence.md, days.csv |

## What I could not judge

The NetSmartz presentation's contents (download needs a sign-in: browser check). The library APPROACH and STANDARD
pages were read only through the frame's citations this run. Whether the sample sheets and invented pages land at
grade 4 reading level waits for the days.

## Sources

- Empire State Information Fluency Continuum, 3 to 5 band file (local copy, source
  https://libguides.monroe.edu/ld.php?content_id=49990827): grade 4 cells behind the candidates and the frame's check
  set read.
- NetSmartz resources listing, https://www.missingkids.org/netsmartz/resources: the presentation's title and the
  sign-in on download.
- data/plans/calendar.csv and docs/courses/CALENDAR.md: host and check weeks.

## For the source list

The NetSmartz listing confirmed 2026-11-26: "Being a Good Digital Citizen: Grades 3-5" is listed as free, and the
download asks for a sign-in or registration.

## For Cory

Nothing: every finding is inside the frame's scope, audience and cost.

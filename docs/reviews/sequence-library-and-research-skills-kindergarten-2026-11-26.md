# Expert read: scope and sequence, Library and Research Skills, kindergarten, 2026-11-26

Cold read (PRODUCTION-PATH step 3, docs/pipeline/briefs/sequence-read.md, with build/scope-writes/AFTERCORE-READ.md
and AFTERCORE-BRIEF.md). I did not write the scope.

## What I read

- docs/courses/library-and-research-skills-kindergarten/scope-and-sequence.md and
  data/plans/library-and-research-skills-kindergarten/days.csv (all 30 rows).
- The frame (docs/courses/library-and-research-skills-kindergarten/frame.md), its expert, second-model and fixes
  reviews (docs/reviews/frame-library-and-research-skills-kindergarten-*2026-11-25.md).
- data/progressions/library.csv, the seven K rows and the grade 1 rows that assume them; data/standards/aasl-words.txt
  for the ten ids the days carry.
- docs/agents/EXPERT.md, docs/agents/lenses/library.md, docs/ADOPTION-BAR-SUBJECTS.md part 11,
  docs/courses/library/STANDARD.md and APPROACH.md, docs/pipeline/briefs/sequence-write.md.
- docs/courses/CALENDAR.md (rule 1 and the generated table) and data/plans/calendar.csv for grade K; the days.csv of
  ELA, science and social studies kindergarten for the leaned rows (ek-shared-research, ek-books-and-authors,
  ek-discussion, sk-push-pull, sk-weather-watch, sk-needs-places, ssk-asking-questions, ssk-talk-together).
- docs/courses/sel/STANDARD.md section 7 (Shared steps) and the SEL K to 2 frame's talk turn card.
- DESK-ANSWERS 2026-11-26 entries (after-core frame fix-pass rules, after-core frame calls, arts and computer
  science scope calls); docs/reviews/sequence-computer-science-kindergarten-2026-11-26.md for repeat tags.
- Outside: the free online-safety listing the frame names, https://www.missingkids.org/netsmartz/resources (opened
  2026-11-26).

Gates: `scripts/sequence.py check` 0 failures; `scripts/frame.py check` 0 failures (4 units, 30 days);
`scripts/frame.py calendar` shows library K at weeks 13, 27 and 28; library is a special and does not count in the
K to 5 stagger (CALENDAR.md rule 1), and CALENDAR.md reports no stagger break. `scripts/stale.py check` 0 failures.
`plan.py check` failures are all in other courses (algebra-ii and others), none in this one.

## Verdict

The scope is sound: it keeps the frame's units, days and weeks, places the one owned id (AASL.V.C.1) on teaching
days, the end-of-unit assessment and both course-level checks, costs every assessment against 19 working minutes
for 30, and keeps every sensitivity guard on the day it applies. The most serious fault is in the arc of two units:
the show-me or hook day answers the stand-alone question the later inquiry day is meant to find (unit 3's rabbit
question on day 15, unit 1's seed cut open on day 1), so a writer following the days would build an inquiry with
nothing left to find. Seven findings, two moderate and five minor; none needs Cory.

## Findings

### 1. Two units answer their inquiry question before the inquiry (moderate)

LAYER sequence. REPEAT new.

- **What is wrong.** Unit 3: day 15's show-me opens on "What does a rabbit eat?" and the teacher reads the fact book
  and stops at the sentence that answers it; day 17's inquiry then asks the same question of the same read-aloud on
  the stand-alone path. Unit 1: day 1's hook is "a seed the teacher cuts open", and day 4's find step on the
  stand-alone path is "What is inside a seed?" from the seed read-aloud. In both, the find has already happened.
- **Why it matters.** The frame defines the show-me day as thinking aloud "on an invented or read-aloud case"; the
  inquiry day is where the class runs the cycle and finds. If the answer is out on day 1, the inquiry day is a
  repeat, children learn that the find step means remembering what the teacher said, and the end-of-unit
  assessment's unseen-case design has no practiced find behind it. On the host path (sk-needs-places) the fault
  hides; on the stand-alone path, which every school without a core task in step will use, it is plain.
- **Fix.** Unit 3: day 15 models the held-question move on a parallel case (a tortoise passage with its own held
  question, "What does a tortoise eat?"), still opening with the rabbit question as the unit's hook; the rabbit
  read-aloud is first read on day 17. Day 16's three passages and the unseen passages on days 18 and 27 are other
  plant eaters (the sensitivity line stands). Unit 1: on day 1 the seeds stay whole (children look at the outside
  and wonder); the teacher cuts one open on day 4 as a find source beside the read-aloud. Update the day 1, 4, 15,
  16 and 17 goals and notes and the unit 1 and 3 paragraphs.
- **Confidence.** Firm (the frame's own day-kind definitions, and the scope's days read as a writer would).

### 2. Unit 1's check on the cycle is recall of the step words (moderate)

LAYER sequence (the item comes from the frame). REPEAT yes (the lens's "end-of-unit assessment is recall of terms";
the computer science K read's finding 1 is of the same family: an item asks less than the skill it scores).

- **What is wrong.** Day 5 scores k-class-inquiry by "each child points at the four cycle pictures in order saying
  each step's word". The row's skill is running the cycle (ask, find, share a drawn fact, reflect). In unit 1 the
  share and reflect steps happen only on day 6, after the assessment; so the only evidence of the cycle is naming it.
- **Why it matters.** The lens names "the end-of-unit assessment is recall of terms, with no search, judgment or
  citation actually done" as an error reviewers catch. The same item returns on day 13, so the year's only scored
  evidence of k-class-inquiry is word recall.
- **Fix.** Keep the picture-order item, and name the day 4 drawing (one found fact, labeled or dictated) as the
  observed performance for the find and use steps of k-class-inquiry, marked on the class checklist on day 4 (an
  inquiry day, not a show-me day, so the frame's scoring rule holds). Day 5's note says the checklist for
  k-class-inquiry is the day 4 product plus the day 5 item. Sequence-write rule 2 allows "a product or an observed
  performance may stand for a code where the day says so". No day added.
- **Confidence.** Likely (lens and rule; the frame set the item, so a reviewer could accept it at K depth).

### 3. Unit 4's turn card does not start from SEL's talk turn card (minor)

LAYER sequence. REPEAT yes (the shared-card findings of the SEL and health K to 2 frame reads, 2026-11-25).

- **What is wrong.** Day 20 teaches a group turn with a talking object on a new skill card, "my turn, your turn, what
  did Sam add, who made it". SEL kindergarten unit 1 already teaches the talk turn card, "eyes look, wait my turn",
  with a talking object in a circle (SEL K to 2 frame; SEL STANDARD section 7 keeps one wording so "a child meets one
  card in every course"). Library is not bound by the shared-card rule, but a kindergartner here meets two turn cards
  for one move.
- **Fix.** Day 20's card opens with SEL's two pictures in SEL's words ("eyes look, wait my turn") and adds library's
  steps ("what did Sam add, who made it"). Day 20's note: where the school runs SEL, the class already knows the first
  two pictures; where it does not, this day teaches them. No day added.
- **Confidence.** Likely.

### 4. Day 7 carries no hook or compelling question, and the retrieval crowds it (minor)

LAYER sequence. REPEAT new.

- **What is wrong.** The frame says "every unit's day 1 is a show-me day with the hook and the compelling question".
  Day 7, unit 2's first day, names neither "How do we find a book that answers our question, and look after it?" nor a
  hook, and opens with a five-minute k-wonder retrieval before book care, borrowing, returning and the stop rule: 14
  minutes for four new routines.
- **Fix.** Day 7's goal opens with the hook and the compelling question; drop its k-wonder retrieval (day 9 already
  retrieves k-wonder, and days 22 and 27 return it, so spacing holds). Update the retrieval list in the .md.
- **Confidence.** Firm.

### 5. Retrieval column and the "every teaching day opens with retrieval" line disagree with the days (minor)

LAYER sequence. REPEAT yes (computer science K read, finding 3: a unit retrieves itself).

- **What is wrong.** Days 10, 17 and 23 list k-class-inquiry in `retrieves` while it is also in their `skills`; their
  notes describe the cycle card held up for the unit's own run of the cycle, not a retrieval task. The .md counts them
  as retrievals and says "from unit 2 on, a teaching day opens with the five-minute retrieval task", but days 10, 17,
  23 and 24 open with none. The spacing report would read three retrievals that are the day's own work.
- **Fix.** Clear `retrieves` on days 10, 17 and 23 (the cycle run is the day's skill); the .md line becomes "From unit
  2 on, show-me and practice days open with the five-minute retrieval task; inquiry days open with the cycle card".
  The k-class-inquiry retrievals that remain (days 8, 30) are real.
- **Confidence.** Firm.

### 6. Smaller item and wording fixes (minor)

LAYER sequence. REPEAT new.

- **Day 11 and day 28 claim ~AASL.IV.A.2** ("list the kinds of sources likely to hold the answer you need") but ask
  only "story book or fact book". Add one prompt: "Which one would help us find out about ___?" (a named question),
  so the item asks the row's slice of the id. No time added beyond a few seconds a child.
- **Day 23's ELA host timing is wrong.** The day 23 note, the unit 4 paragraph and the Unsure line say ELA's trees
  research "ends on school day 118, the week before day 23". Day 23 is school day 115 (week 23) and ek-shared-research
  runs school days 80 to 118 (weeks 16 to 24), so days 20 to 24 are in step. Rewrite as "in step (ELA days 80 to
  118, weeks 16 to 24)" and drop the Unsure line. Social studies' ssk-talk-together also returns on its school day
  115 (week 23); day 20's note can say "weeks 3 to 4 and again in week 23".
- **Day 10 and day 12 disagree on the partner share.** Day 10's goal ends with the partner share and its note moves it
  to day 12 "if time runs out"; day 12's goal holds it every time. Pick one: the share and self-check open day 12, as
  units 1 and 3 do, and day 10 ends at the drawing.
- **Day 2's cover guess** is a new move on a Fluency day. Its note says "the teacher shows one cover guess first";
  it stays about 3 minutes.
- **Unit 3's passage list** needs to be named for the unit plan: the rabbit read-aloud, the day 15 model passage,
  three practice passages (day 16), a fresh-try passage (day 19) and unseen passages for days 18 and 27 (all plant
  eaters), plus day 20's two-sentence retrieval passage. The frame's "two short animal passages" is short of this; it
  is a Tools line, not a day change.
- **Confidence.** Firm.

### 7. Shorter path: one fold-in loses the year's audience (minor)

LAYER sequence. REPEAT new.

- **What is wrong.** The second fold-in moves day 24, the year's last product shared with the class circle, into day
  23 as a share inside each group of three, and claims it saves the whole 19 minutes. Day 23 is already a full find
  and draw day, and the share to the whole class is the bar's "make a product and share it" (part 11 item 6; the
  lens's "a product for a real audience").
- **Fix.** Fold day 24's circle share into the opening 10 minutes of day 26 (the pattern units 1 and 3 already use:
  the respond day opens with the share), with the self-check and reteach after it; the feedback candidate's 3 minutes
  go with it. Day 30 into day 29 stays. That is two fold-ins, about 38 working minutes, 28 of 30 days, nothing
  assessed or owned cut. Keep day 22 into days 21 and 23 as the third.
- **Confidence.** Judgment call.

## Checked and met (no finding)

- **Owned ids and frame rows.** AASL.V.C.1 sits on days 1 to 5 and on both checks (13, 27); every carried id has a `~`
  and its later owner in the frame; no id outside the frame's rows is claimed. Every owned skill is on a day.
- **school_day and weeks.** school_day = 5n puts every unit and check in the frame's and CALENDAR.md's weeks (units
  1 to 6, 7 to 12, 15 to 19, 20 to 26; checks 13, 27 and 28; respond 14, 29, 30).
- **Readiness.** None owed: kindergarten has no course before it and no K row has an `assumes` cell.
- **Course-level checks.** Each samples earlier units on new cases and reuses the just-ended unit's class count,
  stated in the .md and the day goals; no form repeats within two weeks; minute totals fit 19 minutes for 30.
- **Candidate cells.** All six settled with their cost inside the unit (the main-idea cell dropped with a reason).
- **Leans.** Every same-year lean checked against the other course's days: sk-push-pull (weeks 1 to 5) and ELA unit 2
  (weeks 7 to 16) in step; sk-weather-watch before; ek-books-and-authors (weeks 1 to 7) before; ek-shared-research is
  later than unit 1 and day 3 carries the bridge.
- **Sensitivity.** Neutral case sets; the visiting staff member's guards on day 4; the stop rule on pretend cards with
  the adult's steps and the health pointer on day 7; a mild pretend picture on day 11; borrowing from the class corner
  with no home question; honest use without shaming on day 21; class-level note to grade 1, never a per-child record.
  No shared SEL card is quoted wrongly (finding 3 is about one not used).
- **Source.** The free K to 2 online-safety presentation the frame names is listed on the page opened 2026-11-26,
  free, by its title. The listing does not show the presentation's rule; the frame's statement that its K to 2 rule
  matches the stop rule rests on the presentation itself: **browser check** at grade close (the kit is a download and
  was not opened). The scope rightly names no organization.
- **Facts.** Rabbits and tortoises as plant eaters, seeds, rain and trees: accurate at K depth.

## Lens checklist (scope and sequence layer)

| Lens line | Result |
|---|---|
| Host task from another course named | Met, every unit, with a stand-alone question |
| Source judging as a website checklist | Not applicable in K (judge is the fact-book pick) |
| A citation unit with no research to cite | Met: unit 4 cites the book its facts came from |
| End-of-unit assessment is recall of terms | Partly missed: unit 1's cycle item (finding 2) |
| AASL text copied or alignment claimed | Met: own words only |
| Live web page with no dated capture | Not applicable (no web day) |
| Paid database or a library visit | Met: none |
| A company or product named | Met |
| A claim that the method raises scores | Met: none |

## Stale notes

- The frame's Placement paragraph and For the lead item 4 still treat the week 27 and 28 after-core clash as open;
  CALENDAR.md rule 1 settles it (the scope's For the lead says so). The lead's.
- The lens (docs/agents/lenses/library.md) still has "catalogues", "licences" and "judgement"; the frame fix pass
  left it for the lead.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Day 15 models on a tortoise passage; the rabbit read-aloud is first read on day 17 | The inquiry keeps something to find | days.csv days 15 to 17; scope unit 3 |
| The seed stays whole on day 1 and is cut on day 4 | Same | days.csv days 1, 4; scope unit 1 |
| The day 4 drawing is k-class-inquiry's observed performance beside the day 5 item | The cycle is done, not only named | days.csv days 4, 5; scope unit 1 |
| Day 20's card opens with "eyes look, wait my turn" | One turn card across courses | days.csv day 20 |
| Day 7 opens with the hook and the compelling question; its retrieval is dropped | First-day rule; load | days.csv day 7; scope retrieval list |
| `retrieves` cleared on days 10, 17, 23; the .md line reworded | Not retrieval tasks | days.csv; scope one-page section |
| "Which one would help us find out about ___?" on days 11 and 28 | Asks the IV.A.2 slice | days.csv days 11, 28 |
| ELA trees research is in step on days 20 to 24 | Calendar fact | days.csv day 23; scope unit 4, Unsure |
| The unit 2 partner share sits on day 12 | One place for it | days.csv days 10, 12 |
| Shorter path: day 24's share folds into day 26's opening | Keeps the class audience | scope Shorter path |

## For Cory

None. Every finding is an item-level or day-level choice inside the frame.

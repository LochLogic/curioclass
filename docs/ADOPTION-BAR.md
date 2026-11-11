# The adoption bar

**Decision (Cory, 2026-11-10; BASELINE rule 20):** state adoption is the bar we build to. Full-course materials are
built to meet the substance of what state and national curriculum reviews ask for. We do not pursue formal adoption
now. If later data says formal adoption is a good path, we pivot and are already well placed.

This file is the record of that decision: what the bar asks, what we took into the plan, what we left out and why.
docs/VISION.md states the decision, docs/ROADMAP.md holds the order of the work, and each track's plan holds the detail.

Source: "US Curriculum Design Blueprint" (docs/US Curriculum Design Blueprint.pdf, compiled by Cory, 2026-11-10),
assessed by Claude the same day. The Blueprint is input, not a rule book; see "Cautions about the source".

## What the bar asks

The reviews judge a whole course, not single tools. So this bar applies to Track 7 (units, Tracks, the Binder) and to
the shelves that feed it. Single tools keep their own rules (BASELINE, docs/TOOL-CONTRACT.md).

**Any course**

- **A year that hangs together.** Each unit and day has a place in a year's order, and the plan says why it sits there.
- **Ready to teach.** Daily plans, student pages, checks and keys are all there. A teacher writes nothing from scratch.
- **Every standard really taught** (BASELINE rule 2), and coverage shown per standard, never claimed as a slogan.
- **No errors.** Wrong facts, wrong sums, misquoted standards and mislabeled pictures are what reviews fail first.
- **Support for every learner.** More than one way in, more than one way to show learning, English learner supports.
- **Open to families.** Anyone can see every page with no login. Curio Class already works this way.

**Math**

- Most of the year's time goes to the major work of the grade.
- A balance of understanding, fluency and real-world use. No year leans on one alone.

**ELA**

- Texts worth reading, at the right difficulty for the grade, each with a short record of why it sits there.
- Reading builds knowledge: texts are grouped by topic so words and ideas pile up across a unit.
- Questions and writing send students back to the text for evidence.
- K-2 reading follows a plain, ordered phonics path. Students decode words; they are never told to guess a word from
  the picture or the sentence (the "three-cueing" approach, which several states now forbid).

**Science**

- Units start from a real thing to explain and have students work it out with evidence, with plain content summaries
  beside the investigation.

**Teacher support**

- The teacher pages teach the teacher: why this model or picture was chosen, what students tend to get wrong and
  how to spot it, and how to shorten or stretch a lesson without making it easier.

## What we took into the plan

| What | Where it lives | When |
|---|---|---|
| Year spine before units: a year's order with reasons, for each pilot course | ROADMAP Track 7, step 1 | Before the unit pilot |
| Teacher pages that teach the teacher (why this model, watch for, adapt it) | ROADMAP Track 7, step 2 (unit pilot) | Tried on the two pilot units; tool lesson plans stay as they are until the pilot is judged |
| Pilot units judged against this bar | ROADMAP Track 7, step 2 | With Cory's review of the pilot |
| K-2 reading scan for guess-the-word prompts | ROADMAP Now, item 8a (tools: the catalog review) | Now |
| Math focus and balance report, per grade | ROADMAP Now, item 8b (tools: the catalog review) | Now |
| Reading Room: a text record and topic sets | docs/LIBRARY-PLAN.md ("Reading level", "Topic sets"); ROADMAP Now 8c and Track 3 | Before the ten-story pilot |
| Hands-on work uses things a classroom or home already has, or names a cheap stand-in | docs/agents/STANDARDS.md (Scope), docs/agents/PLAN.md | Standing, from 2026-11-10 |
| The teaching test, tool roles, modules that name standards, depth on major work (from the catalog review) | BASELINE rules 21 and 22; ROADMAP "The path from here" | Locked 2026-11-10; tool building paused until the rules are in |
| State crosswalk: one state outside the Common Core first; CASE as a file format in and out | ROADMAP Track 7 ("Later"), docs/PHASE1-SCOPE.md | When the crosswalk starts |

On the crosswalk: the Blueprint's shape (our own spine of small pieces, with each state's standards mapped onto it)
is what modules plus data/sequence.csv already are. A state view is a mapping layer on top: which modules a state
teaches in which grade. Nothing is rebuilt. CASE is the open, machine-readable format many states publish their
standards in; we read it in and can write our map out in it.

## Gaps a cold review found (2026-11-11), and where each now sits

| What a review looks at | Where it was | Where it sits now |
|---|---|---|
| Assessment beyond one short check per unit | Not in the six steps | Every spec ends each code with an unaided check the teacher can see (SPEC.md, three hooks); the pilot unit carries its own assessment (ROADMAP step 4). A readiness check per unit and a cumulative check each quarter and at year end are now part of a finished course (ROADMAP, "What a finished course holds", item 4) |
| English learner supports | Named above, in no step | SPEC.md, three hooks; FINAL-REVIEW.md |
| Access: keyboard, color, sound with text | A font and contrast bar, later | SPEC.md, three hooks; FINAL-REVIEW.md |
| What ships, not what the spec says | The measure read specs only | The measure now also counts live and verified tools and unit days (catalog/tables/measure.md) |
| A reader outside the project | Open in PHASE1-SCOPE | A working teacher reads the pilot unit (ROADMAP step 4) |
| A real rubric | This file, compiled from one Blueprint and Claude's knowledge | A published rubric is filed and used in step 4 |
| Coherence across grades | One line in the spine | Each spine row names the standards it builds on and where they are taught; a progression table per subject is built by script before step 6 (ROADMAP gap table) |
| Evidence that it works | Left out | Not claimed. A one-page logic model is written with the pilot unit; a study waits for a partner (ROADMAP gap table) |

The full list of gaps, each with the step that closes it and the test for closed, is in docs/ROADMAP.md, "Gaps found, and how each closes".

A published rubric is now on file: docs/RUBRIC-MATH-K8.md (EdReports K-8 math criteria v2.0, summarised, not copied). Where it and this file differ, the rubric wins. Its evidence guide confirms the 65 percent line for grades 3 to 8 (75 percent for K to 2), checked 2026-11-11.

## What we left out, and why

| The Blueprint says | Why not |
|---|---|
| Rostering, single sign-on, grade passback, live telemetry, dosage dashboards | VISION: no accounts, tracking or student analytics, ever. The Binder's course cartridge export stays; nothing that carries student data does |
| Load all 50 states' standards before writing any content | Quality first, shared parts grown from finished work (rules 13 and 14). One state first, when its time comes |
| An engine that picks each student's next lesson | Needs stored student data. Score codes and The Map are our answer |
| Teacher guides that change as the teacher gains skill | Needs a teacher account. A short and a full view of the same page does the useful part |
| Every lesson teacher-led and built on student inquiry | Rule 4: every tool stands alone. The inquiry shape fits units, where a teacher is present. Several states also ask for fluency and direct teaching, so units keep both |
| Formal reviews, state funding, controlled trials | Not pursued now (the decision above) |

## Cautions about the source

Checked from Claude's own knowledge on 2026-11-10, not against the sources. Verify before any of it is relied on in
public copy or a funding ask.

- The technical section rests on one vendor case study of one private school. Its "2.1X growth" figure is not
  evidence that data standards cause learning.
- The Texas per-student printing money is for state-developed materials, not any open curriculum. The larger Texas
  fund needs a formal publisher submission and state board approval.
- California's state adoption covers K-8 only, and districts may choose materials off the list.
- The Virginia comparison uses a crosswalk of the 2010 English standards, which Virginia has since revised.
- The "three-year fraction gap" is overstated: the Common Core has halves and fourths in grade 1.
- It quotes the 2017 CSTA codes; the repo already uses the 2026 set (data/standards/csta-2026-ids.txt).
- Sound as far as Claude knows: the outline of Texas HB 1605, the three-gateway shape of the national review, and
  the research on teacher-facing curriculum materials (Davis and Krajcik).

## If we pivot to formal adoption later

It would need, at least: a legal publisher, a full-year program for each grade of a subject, a formal submission in
each review cycle, and state-specific pieces (for Texas, a standard-by-standard coverage document and the state's
book and word lists). Building to the bar now means the content would not need rework, only packaging and paperwork.

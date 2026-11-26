# Fixes: scope and sequence of computer-science-grade-1, 2026-11-26

Fix pass on the Claude expert read (docs/reviews/sequence-computer-science-grade-1-2026-11-26.md), per
build/scope-writes/CS-FIX.md and docs/pipeline/briefs/sequence-fix.md. The Codex read waits for its own pass after
2026-11-30.

Counts: applied 9 of 9 expert findings and all 12 rows of "Settled by the expert"; lead calls 1, 3, 4, 5 and 7
applied, 2 answered, 6, 8, 9, 10, 11 and 12 checked (nothing to do here); 1 own fix. Not applied: 0. Neighbor reads
(kindergarten, grade 2): no item touches this course. Defect rows logged: 11.

## Applied

- **Expert 1** (days.csv days 25 and 27; .md unit 4 Arc; frame unit 4 cell, year-end check row, Seams k-ask-and-count
  row): day 25's sort is now "questions we answer by collecting data, counting, measuring, looking or asking everyone"
  against "questions answered another way" (one person's own idea or feeling, imagination, asking someone who knows),
  with the "most of us / I" pair. Day 27's sort labels match ("collect data to find out", "answered another way").
- **Expert 2** (days.csv days 13, 21 and 31; .md units 2, 3 and 5 Assessments; frame unit 3 and 5 cells, mid-year
  check row): day 13 ML-02 is four pictured machines, circle the two pattern-finders (one decides, one makes something
  new), then the card guess; day 21 VD-05 uses worded picture cards read aloud, the word circled on one changing card;
  day 31 CE-16 is a three-scene strip (home, school room, town place) with a line from each scene to its device, plus
  the spoken use.
- **Expert 3** (days.csv days 11 and 12; .md unit 2 Arc; frame unit 2 cell): day 12 reads "repeat a step the same way
  every time without getting tired"; day 11 plants one wrong guess with "a pattern-finder can guess wrong too, so
  people check it" and says "people call these systems AI" once, not tested.
- **Expert 4** (days.csv days 13 and 27 notes; .md "A session"; frame Evidence): each check note has the minute plan
  (0 to 3 settle, 3 to 8 read-aloud items together with each card read twice, 8 to 26 picture-only items alone while
  groups are heard, last four minutes collect and cubes away). The fallback drop (day 13's rule-scene sample) is in
  the .md For the lead 5.
- **Expert 5** (.md Shorter path, day 9 row): day 10 keeps its opening as a new pretend login card with a rule scene;
  the five-minute change comes out of the make.
- **Expert 6 / lead call 1** (days.csv day 24; .md): `assess` blanked; note now "the teacher notes by exception which
  groups chose a way to collect each piece; it shapes the day 28 groups"; old For the lead 1 and the second Unsure
  bullet deleted. Days 11 and 12 keep `observe`.
- **Expert 7** (days.csv days 10, 18, 23; frame unit 3 cell): day 23 opens on k-ask-and-count only (it carries the
  math lean), the attribute retrieval moved inside the description step, `retrieves` now
  `k-ask-and-count; m1-data-three-categories`; day 18's bug is "moves forward before it turns, so it ends on the wrong
  square"; day 10's carrying-out pair has reader and doer roles switching at the halfway signal (IC5).
- **Expert 8** (.md For the lead 4): the scope keeps check sittings without an opening; the APPROACH.md wording goes
  under For the structure pass.
- **Expert 9 / lead call 3** (frame.md For the lead 5): "until it is loaded" replaced by
  Pending(docs/sources/BASE-TEXTS.md#teach-computing-curriculum). frame.py check is clean.
- **Lead call 2**: the .md's source-map item now reads "waits on L149"; no source-map.csv written.
- **Lead call 4**: frame wording brought in line in the same pass (all items listed above). No unit, day count or
  owned row moved.
- **Lead call 5** (frame Day kinds bullet): reworded to GLOSSARY: Understanding is the first teaching of a row,
  construct or method; Fluency is practice of what earlier days taught and teaches nothing new. The scope already
  followed GLOSSARY.
- **Own**: the .md spaced-retrieval day list dropped day 23 (it no longer retrieves a course row); the .md For the lead
  list was renumbered.

## Not applied

None.

Checked, nothing to do: lead call 6 (no Specialty id or day here; both fold-ins are standard days), 8 (all frame items
were wording and are applied), 9 (no begun ids), 10 (grade 9 only), 11 (no read here differs from an earlier frame
read), 12 (the one UK spelling lint hit in the gate baseline is the frame's "Open Government Licence", the known
exception).

## Settled (for DIGEST)

| Judgment | Reason |
|---|---|
| A class survey of feelings ("which do most of us like best") is data; one person's own feeling is answered another way | K, day 23 and day 26 collect preferences as data; E1-DAT-DI-09's "other means" |
| A check sitting with early readers runs read-aloud items together first, picture-only items while groups are heard | The teacher cannot read aloud and interview at once |
| Computers repeat a step "the same way every time without getting tired", never "without mistakes" | The row's wording; the year teaches bugs; lens misconception |
| "AI" is said and shown once beside the pattern-finder, never tested | E1-ALG-ML-02 names AI systems |
| Day 23's math lean rides on the k-ask-and-count picture-graph opening, one retrieval | Three minutes, one retrieval, hook day |

## For the structure pass

1. **data/progressions/computer-science.csv, row g1-data-questions, `notes`.** Old: "Children sort questions into those
   that counting or looking can answer (how many windows does our room have) and those of feeling, guess or
   imagination (which window has the best view)." New: "Children sort questions into those we answer by collecting
   data, counting, measuring, looking or asking everyone (how many windows does our room have; which window do most of
   us like best), and those answered another way: one person's own idea or feeling (which window do I like best),
   imagination (what would a dragon see from our window) or asking someone who knows (what is our school's name)."
   The rest of the notes cell is unchanged.
2. **docs/courses/computer-science/APPROACH.md, Pacing** (expert finding 8, the lead's wording), line 151. Old: "every session opens with the three-minute retrieval trace and every unit ends with a respond day".
   New: "every teaching and respond session opens with a three-minute retrieval task, a trace where the earlier row
   is a program or algorithm, and every unit ends with a respond day".
3. **Probe follow-up, not yet a change.** If the probe shows day 13 over 30 minutes after the minute plan, drop the
   unit 1 rule-scene sample from the frame's mid-year check row and days.csv day 13 (E1-SYS-IM-13 stays scored on days
   3 to 5); a frame change.

## For Cory

None.

## Gates

- `python -X utf8 scripts/sequence.py check computer-science-grade-1`: 0 failures.
- `python -X utf8 scripts/frame.py check computer-science-grade-1`: 0 failures (was 1, frame.md:286). Unfiltered
  `frame.py check`: no failures listed.
- `python -X utf8 scripts/frame.py calendar`: grade 1 computer science weeks 13 and 27, unchanged; a K to 5 special
  (CALENDAR.md rule 1), so no stagger break.
- `python -X utf8 scripts/gate.py --course computer-science-grade-1`: 0 failing findings against the baseline, exit 0.
  One failing line stays as before (lint UK spelling, the "Open Government Licence" exception, lead call 12); the
  index-reports gate exited non-zero before and after this pass.

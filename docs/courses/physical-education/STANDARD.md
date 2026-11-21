# Physical education: the standard, made usable

**DRAFT, 2026-11-16, fixed 2026-11-19 after a cold read (docs/reviews/prework-physical-education-read-2026-11-19.md)
and 2026-11-20 after the second-model read (docs/reviews/prework-physical-education-fixes-2026-11-20.md).**

Written 2026-11-16 as pre-work for physical education (four courses, one per band). It answers the PE row of
"Before a scope and sequence in this subject" in docs/ADOPTION-BAR-SUBJECTS.md. The bar is the PE part of that
page. The lens is docs/agents/lenses/physical-education.md. The approach page is
docs/courses/physical-education/APPROACH.md (approved 2026-11-21, Desk q-prework-open-1).

| Owed | State | Where |
|---|---|---|
| Keep the 2024 standards | Done (decided 2026-11-11) | Section 1 |
| Write the map from the tool's five standards to the loaded four | Done 2026-11-11 | docs/standards-notes/pe-2014-to-2024.md |
| Find and read the appropriate practice guidelines | Done in part 2026-11-16 | Section 4 |
| (Also) Outcome for each standard by grade, the bar's scope and sequence line | Rule written | Section 3 |
| (Also) later.csv L46, read the review tool's grade tables | Done 2026-11-19: all grade tables read | Section 3 |
| (Also) Each indicator in our own words | Done 2026-11-19 | data/standards/shape-pe-2024.txt, second column |

## 1. The standard and the review tool

- **Standard:** SHAPE America National Physical Education Standards, 2024. Loaded in
  data/standards/shape-pe-2024.txt: 210 grade-span learning indicators, each id with one line in our own words, `SHAPE.S<standard>.<span
  end>.<n>`, spans ending at grade 2, 5, 8 and 12. Four standards: motor skills; knowledge of movement and
  fitness; social skills through movement; personal skills, the benefits of movement and choosing to be active.
- **Review tool:** CDC's Physical Education Curriculum Analysis Tool (PECAT), 2019. It is keyed to SHAPE America's
  earlier five standards (2013, with grade-level outcomes in the 2014 book). Our mapping from five to four is
  docs/standards-notes/pe-2014-to-2024.md. Both editions are named wherever the tool is used.
- scripts/standards.py checks the standard (1 to 4), the span (2, 5, 8 or 12) and a one or two digit number; it
  does not check that the number exists. scripts/progression.py checks ids against the file.
- Indicator wording is never copied. Our one-line paraphrases are the file's second column; a plan cites the id
  and states its action in our words.
- data/standards/nspfe-2021.txt (personal finance) is not a PE file. It belongs to the personal finance course
  and is left untouched here.

## 2. Reuse terms (read at source, 2026-11-16)

- **SHAPE America, 2024:** the free standards page shows the standards and indicators in full, with no reuse terms
  and a footer of "All Rights Reserved". So: ids and our own words only. No indicator sentence is copied.
- **PECAT 2019:** a CDC publication, a US government work. Its method is used; its tables are not copied into
  pages.
- **Appropriate practice guidelines (2009):** copyright of the professional body (now SHAPE America), all rights
  reserved; SHAPE's current page allows free download for personal or classroom use, not redistribution (search
  only). Read into our own words; never quoted on a page.

## 3. Outcome for each standard by grade

The bar asks the scope and sequence to state the outcome for each standard by grade. The 2024 indicators are
written per span, and SHAPE says they are not meant to line up across spans. So the grade outcomes are ours.

**The rule.**

1. **In the progression** (data/progressions/physical-education.csv, layer 4), a row owns an indicator in the
   grade where the student first meets it as a pattern and can show it in a stated setting: any grade of the span.
   Grades after it in the span carry it as `~CODE` (used in new settings); grades before it that prepare it carry
   `~CODE` (toward). Every indicator has exactly one owner grade and is met no later than the span's last grade.
   scripts/progression.py checks this.
2. Every standard (SHAPE.S1 to S4) has a stated outcome in every grade, in our own words, each naming at least one
   owned or `~` indicator. The scope and sequence copies these grade outcomes and lists the indicators each year
   works on.
3. Motor skills are ordered by how they develop (bar criterion 2): a skill is first met as a pattern with its key
   parts, then used in changing settings, then combined and used in games and dance. Locomotor patterns and
   balance come first in K and 1, before manipulatives that need them; weight transfer follows locomotor control.
   By default, a skill the PECAT tables first expect in a grade is owned there, and the grade before carries it as
   `~CODE`. Overhand throwing is worked toward in K and 1 and owned in grade 2. Two settled exceptions: continuous
   hand dribbling and a self-turned rope are attempted in K (`~CODE`, with growth marked) and owned in grades 1 and 2
   (Cory, 2026-11-20, Desk q-prework-health-pe-2). Each placement is marked "from the tool", "from memory" or "ours,
   untested". For the order within K to 5, the PECAT tables are a guide. They show, for example, that underhand throwing, catching, hand and foot
   dribbling, kicking, striking with a short implement and jumping rope start in kindergarten, while weight
   transfer starts in grade 1, and overhand throwing, jogging and striking with a long implement start in grade
   2. We use that order as a reference, not as wording.
4. Each grade outcome names how it is assessed (bar criterion 7, PECAT's "outcome, content, assessment" for every
   standard in every grade).
5. High school (9 to 12): two required years and two elective years (Cory, 2026-11-20, Desk
   q-prework-health-pe-2; most schools require one or two years). Grades 9 and 10 own every indicator of the span,
   in a range of activities; grade 10 owns the choice and personal plan indicators (S4) in short form, teaching every
   part of each, so every student meets them. Grades 11 and 12 are electives that deepen the plan and carry the rest as `~CODE`. Grade
   outcomes are stated per year as for K to 8.

**PECAT tables (L46), read 2026-11-16 and 2026-11-19.** The tables score a curriculum per grade, per outcome, on
three marks: the outcome is stated, content teaches it, and an assessment checks it. Outcomes are coded by the 2014
book (S1.E1 and so on) and keyed to the 2013 five standards throughout; split older outcomes by the rule in
docs/standards-notes/pe-2014-to-2024.md. What the tables expect, read in a browser (nothing saved):

- **K to 5, standard 1:** see rule 3 above; in grade 3 passing with hands, dribbling in combination, overhead
  volleying and manipulatives combined with locomotor are not yet expected (they start in grade 4).
- **K to 5, standards 2 to 5:** every outcome is expected in every grade, except these, which start in grade 3:
  alignment and muscular tension, and strategies and tactics (older S2); warming up and cooling down, and
  assessment and program planning (older S3); social interaction (older S5). In K to 2 these ideas are met only
  at the depth the K to 2 indicators ask: SHAPE.S2.2.2, S2.2.7 and S4.2.2 (naming a chasing tactic, saying why we
  stretch, pointing out activities with others) are owned in grade 1 or 2; tactics in play, warm-up routines,
  program planning and social interaction as the tables mean them start in grade 3.
- **6 to 8:** every outcome of all five standards is expected in every grade (24, 13, 18, 7 and 6 outcomes).
- **9 to 12:** two levels, not grades; every outcome of all five standards is expected at both levels (3, 4, 14, 5
  and 4 outcomes). Our grades 9 and 10 stand for level 1 and 11 and 12 for level 2 (rule 5).

The tables give placement only, never wording.

## 4. Appropriate practice guidelines (read in part)

Read: "Appropriate Instructional Practice Guidelines, K-12: A Side-by-Side Comparison" (the professional body,
2009), pages 1 to 12 and 22 to 25, from a state education agency's copy. Not read: SHAPE's newer "essential
components" document (2026) and its position statements. In our words, the points that bind our plans:

- **Learning environment.** Safe and supportive; students may fail and try again. Motivation through success and
  choice, not rewards and punishments. Exercise is never a punishment, and activity is never withheld as one.
- **Equity and inclusion.** No captains choosing teams in public. No activities split by gender, and
  gender-neutral language. Activities fit every ability and are adapted for fitness levels, disabilities and
  short-term injury, so nobody simply sits out. Activities come from many cultures.
- **Competition.** No elimination games and no games with people as targets. Small-sided games. No public lists of
  winners and losers. Where it fits, students choose a more or less competitive setting.
- **Instruction.** Clear objectives tied to outcomes. A lesson shape of instant activity, warm-up, focus, cool-down
  and closure. Stretching after a warm-up, not before. Skills are taught before they are used in game play, and
  they come back across the year.
- **Activity time.** Most of the class moving most of the time: no long lines, enough equipment for small groups,
  and at least half of the lesson in moderate to vigorous activity.
- **Fitness testing.** Used to set and track personal goals, prepared for, done privately, results shared
  privately. Never a grade.
- **Grading.** On defined outcomes aligned to the standards. Never on effort alone, dress, attendance, or a single
  fitness test.

How these points meet PE's sensitive ground (bodies, food, injury and medical conditions, water, cultural dance
and games, emotions) is on the approach page, "Sensitive ground".

## 5. Left out, and why

- Pre-kindergarten: no pre-kindergarten course.
- State PE standards and state fitness-test requirements: a school adds them; the course page says so.
- Adapted physical education plans for individual students: the school's specialists. Our lessons carry
  adaptations for a range of needs (bar criterion 6), not individual plans.

## 6. Leans on the core progressions and other subjects

- **Health:** the physical activity topic is shared (HECAT PA outcomes). PE teaches the moving and in-class fitness
  knowledge; health teaches planning, goals and influences. In grades 6 to 8, HECAT PA 3, 4 and 6 (warm-up and
  cool-down, water during activity, staying safe while active) are taught in PE (Cory, 2026-11-20, Desk
  q-prework-health-pe-2); the health map names them so. Units name each other.
- **Arts, dance:** PE dance units (rhythm, locomotor patterns, simple sequences) and the dance course name each
  other so the same thing is not taught twice in a year.
- **Science:** heart rate, muscles, energy and force lean on science (body structures in grade 4, body systems and
  food for energy in grade 7, force and motion in grade 8); PE uses the idea, science teaches the model.
- **Math:** personal data and heart-rate counts lean on graphing in grade 5 and on ratio and data in grade 6.
- **Social studies:** why a game, sport or dance matters to a culture leans on regional cultures (grade 4) and
  complex societies (grade 6); the course pages name each other.
- **SEL:** PE's social standard (SHAPE.S3) overlaps with SEL's relationship skills; the two course pages name each
  other.
- Each lean's code is in the progression's cross_subject column (data/progressions/physical-education.csv); a
  same-year lean carries the frame's "if later" line (docs/pipeline/briefs/frame-write.md).

# Physical education: the standard, made usable

**DRAFT, 2026-11-16.**

Written 2026-11-16 as pre-work for physical education (four courses, one per band). It answers the PE row of
"Before a scope and sequence in this subject" in docs/ADOPTION-BAR-SUBJECTS.md. The bar is the PE part of that
page. The lens is docs/agents/lenses/physical-education.md. The approach page is
docs/courses/physical-education/APPROACH.md (draft).

| Owed | State | Where |
|---|---|---|
| Keep the 2024 standards | Done (decided 2026-11-11) | Section 1 |
| Write the map from the tool's five standards to the loaded four | Done 2026-11-11 | docs/standards-notes/pe-2014-to-2024.md |
| Find and read the appropriate practice guidelines | Done in part 2026-11-16 | Section 4 |
| (Also) Outcome for each standard by grade, the bar's scope and sequence line | Rule written | Section 3 |
| (Also) later.csv L46, read the review tool's grade tables | Done in part: K to 5 overview and standard 1 tables | Section 3 |

## 1. The standard and the review tool

- **Standard:** SHAPE America National Physical Education Standards, 2024. Loaded in
  data/standards/shape-pe-2024.txt: 210 grade-span learning indicators, ids only, `SHAPE.S<standard>.<span
  end>.<n>`, spans ending at grade 2, 5, 8 and 12. Four standards: motor skills; knowledge of movement and
  fitness; social skills through movement; personal skills, the benefits of movement and choosing to be active.
- **Review tool:** CDC's Physical Education Curriculum Analysis Tool (PECAT), 2019. It is keyed to SHAPE America's
  earlier five standards (2013, with grade-level outcomes in the 2014 book). Our mapping from five to four is
  docs/standards-notes/pe-2014-to-2024.md. Both editions are named wherever the tool is used.
- scripts/standards.py checks `SHAPE.S[1-4]` by pattern; it does not check span or number.
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

1. For each band year (K, 1, 2 in K to 2, and so on), the scope and sequence states one outcome per standard
   (SHAPE.S1 to S4) for that grade, in our own words, and lists the span indicators that the year works on.
2. Every span indicator is placed in at least one year of the band and is fully met by the band's last year.
   A year that only works toward an indicator says "toward".
3. Motor skills are ordered by how they develop (bar criterion 2): a skill is first met as a pattern with its key
   parts, then used in changing settings, then combined and used in games and dance. For the order within K to
   5, the PECAT tables are a guide. They show, for example, that underhand throwing, catching, hand and foot
   dribbling, kicking, striking with a short implement and jumping rope start in kindergarten, while weight
   transfer starts in grade 1, and overhand throwing, jogging and striking with a long implement start in grade
   2. We use that order as a reference, not as wording.
4. Each grade outcome names how it is assessed (bar criterion 7, PECAT's "outcome, content, assessment" for every
   standard in every grade).
5. High school (9 to 12): a four-year band. Years 1 and 2 meet the span's indicators in a range of activities;
   years 3 and 4 add choice and a personal fitness and activity plan. Grade outcomes are stated per year as for
   K to 8.

**PECAT tables (L46), read in part.** The K to 5 overview and the standard 1 tables (pages 30 to 33 of the tool)
were read on 2026-11-16. The tables score a curriculum per grade, per outcome, on three marks: the outcome is
stated, content teaches it, and an assessment checks it. Outcomes are coded by the 2014 book (S1.E1 and so on), and
some are not expected in some grades. The rest of the K to 5 tables and the 6 to 8 and 9 to 12 tables are read by
the band's planner before that band's scope and sequence; the keying is the 2013 five throughout.

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

## 5. Left out, and why

- Pre-kindergarten: no pre-kindergarten course.
- State PE standards and state fitness-test requirements: a school adds them; the course page says so.
- Adapted physical education plans for individual students: the school's specialists. Our lessons carry
  adaptations for a range of needs (bar criterion 6), not individual plans.

## 6. Leans on the core progressions and other subjects

- **Health:** the physical activity topic is shared (HECAT PA outcomes). PE teaches the moving and in-class fitness
  knowledge; health teaches planning, goals and influences. Units name each other.
- **Arts, dance:** PE dance units (rhythm, locomotor patterns, simple sequences) and the dance course name each
  other so the same thing is not taught twice in a year.
- **Science:** heart rate, muscles and energy lean on the life science progression (body systems, grades 4 to
  7); PE uses the idea, science teaches the model.
- **Math:** heart-rate zones, pacing and personal data (graphs of one's own progress) lean on ratio and data
  (grades 6 to 7).
- **SEL:** PE's social standard (SHAPE.S3) overlaps with SEL's relationship skills; the two course pages name each
  other.

# Scope group read: library and research skills, kindergarten to grade 12 (2026-11-26)

Group read of the eight library scopes side by side (build/scope-writes/GROUP-READ.md, {group} = library). It looks
only at what a single-course read could not see. The per-course findings in
docs/reviews/sequence-library-and-research-skills-*-2026-11-26.md and their -fixes files are not repeated.

## What I read

- AGENTS.md, docs/agents/EXPERT.md, docs/pipeline/briefs/sequence-read.md, build/scope-writes/AFTERCORE-BRIEF.md.
- docs/agents/lenses/library.md; docs/ADOPTION-BAR-SUBJECTS.md part 11; docs/courses/library/STANDARD.md and
  APPROACH.md; data/progressions/library.csv (98 rows), library-edges.md, library-excluded.csv.
- For all eight courses (kindergarten, grades 1 to 5, grades 6 to 8, grades 9 to 12): scope-and-sequence.md in full,
  frame.md where a seam, card or case needed it (Seams tables, inquiry arc, cycle card lines), and days.csv through
  short Python scripts (every day's skills, codes, assess, school_day and retrieves; goals and notes searched for
  cards, cases, stop rule, talk turn, self-check, hand-off notes, sensitivity lines).
- The eight -fixes reports (skimmed for what was settled).
- docs/courses/CALENDAR.md (rule 1 and the end table rows for library); DESK-ANSWERS.md entries naming library and the
  2026-11-26 entries (after-core frame fix-pass rules, after-core frame calls, after-core scope lead calls).
- SEL STANDARD section 7 ("Shared steps") and the SEL K to 2, 3 to 5 and 6 to 8 talk turn card wording, for the
  library days that open with SEL's card.

Scripted checks across the group: every progression row is taught in its course and sits on at least one Check day;
every owned id is plain on its row's days and on an end or course-level check; every one of the 63 kept AASL ids has
exactly one owner; every `retrieves` entry was checked for its grade gap.

## Findings

1. **Readiness checks on year-before rows in both band courses, against the 2026-11-26 lead call.** The lead call
   "Readiness on a band year's first day" says a row last used the year before is a retrieval, never a readiness
   check, and that a read showing it wins over an earlier frame read. Grades 6 to 8 give all nine grade 5 rows as
   readiness checks only (days 1, 5 and 12, assess `readiness`) and retrieve none of them: g5-first-lateral-check,
   taught on grade 5 days 8 to 11, is never retrieved before lateral reading is taught on 6 to 8 day 6, and
   g5-group-inquiry and g5-share-real-audience (grade 5 days 21 to 27) are not retrieved before day 13. Grades 9 to 12
   give the grade 8 rows both a readiness check (days 1 and 9) and a retrieval (days 2, 3, 4, 10, 11, 13). Both keep
   the frame's reason (the earlier course is optional). The K to 5 courses meet the same risk the way the rule asks:
   grade 5 day 8 retrieves g4-primary-secondary and says "a class that did not take grade 4 library gets it for every
   student". Why it matters: the two band courses, and the band courses against K to 5, treat the same seam three
   ways, and grade 6 loses its opening retrieval of the very move (the first lateral check) its unit 2 builds on.
   Fix: in grades 6 to 8, turn the three readiness checks into five-minute retrieval openers on the days that build on
   each row, never a unit's first day: g5-search-revise and g5-research-or-guess on day 2, g5-bibliography on day 3,
   g5-search-log-look-back on day 4, g5-first-lateral-check and g5-evidence-notes on day 7, g5-choose-sources on day 8,
   g5-group-inquiry and g5-share-real-audience on day 14 (beside s5-design-test, or on day 15), each with the K to 5
   line "a class that did not take library grade 5 gets the ten-minute reteach for every student"; days 1, 5 and 12
   lose `readiness` and get their exit ticket or respond time back. In grades 9 to 12, drop the readiness check on
   days 1 and 9 and keep the retrievals already placed; g8-test-assumptions and g8-research-product move to day 2's
   opening. The two frames' Seams tables ("How it opens", "Where it opens here") and For the lead items then read
   retrieval. Tag: **scope** (days.csv assess and retrieves columns, the .md Readiness lines), with the matching
   Seams wording in both frames (**frame**). If the lead wants the optional-course reason kept, that is a Cory call;
   my pick is the rule as logged, since K to 5 shows the reteach-for-all line covers a class that skipped a year.

2. **The same sunflower question in grades 1 and 2.** Grade 1 unit 1's show-me and stand-alone case is "How tall do
   sunflowers grow?" (grade 1 days 1, 3 and 4). Grade 2 unit 3's stand-alone is "How tall does a sunflower grow?"
   (grade 2 day 18, scope unit 3), the next year, with no reason named. A class that runs both stand-alones answers
   the same question twice, and grade 2's "two sources differ" lesson loses its surprise because the children already
   hold one answer. A smaller echo: grade 1 unit 3's stand-alone "How do birds build their nests?" (grade 1 days 18
   to 20) returns as grade 3's unit 1 end-of-unit "new topic" on how birds build nests (grade 3 day 4), which the day
   calls not seen before. Fix: give grade 2 unit 3 another plant case whose figures differ by kind (for example how
   big pumpkins grow, with two kinds of pumpkin), keeping the "check, and see why" third source; give grade 3 day 4
   another neutral topic (for example how bees build a hive). Tag: **scope**.

3. **The tallest-tree case three years apart.** Grade 5 unit 3 is built on "How tall do redwood trees grow, and how
   old can they get?" (grade 5 days 15 to 19). Grades 6 to 8 unit 8 (grade 8) uses "How tall is the tallest tree,
   and who measured it?" (6 to 8 day 41, three invented entries that differ). The world's tallest measured tree is a
   coast redwood (Hyperion, checked 2026-11-26), so grade 8's case answers grade 5's question again. Fix: swap grade
   8's stand-alone for another single number that group-written entries often give differently (a waterfall's
   height, a river's length), so the "trace each difference to its references" move gets a fresh case. Tag:
   **scope**.

4. **"Should school start later?" in grade 8 and grade 9.** Grades 6 to 8 unit 7's stand-alone (day 37 to 40) is
   "Should our school start later in the morning?", with six invented sources. Grades 9 to 12 unit 2 names ELA grade 9
   unit 6, "Should school start later?", as its optional in-step host (scope unit 2; days 11 to 13), the next year. A
   student who took library 6 to 8 meets the same decision two years running, and the grade 9 memo's "fair to every
   side" work is then rehearsed rather than new. Fix: change the 6 to 8 stand-alone, since ELA's unit is a core course
   the library cannot move (a neutral school decision with even sides, for example whether the school should add a
   second recess or a later bus run); keep the grade 9 host line. Tag: **scope**.

5. **Three wordings of one lateral reading card.** Grade 5 day 8 teaches the first lateral check with a "what others
   say" card: leave the page, look up the maker, who is behind it and why, check one statement in a second source,
   marked supported, contradicted or not settled. Grades 6 to 8 day 6's skill card is "leave the page, ask who is
   behind it, go upstream, then judge" (accurate, fair in context, fit for the task). Grades 9 to 12 day 3's lateral
   routine card is "stop, investigate the source, look for better coverage, trace the claim to its original", and day
   3's retrieval (g8-news-lateral) does not tie the new words to the old ones. The moves line up, but no day says so,
   so a student meets three cards for one method, the thing the shared-card rule avoids in SEL, health and PE. Fix:
   6 to 8 day 6's note says the card grows grade 5's "what others say" card by "go upstream"; 9 to 12 day 3's note
   names the mapping (stop is new; investigate the source is "ask who is behind it"; better coverage is "what others
   say"; trace the claim is "go upstream"), or the 9 to 12 card keeps the 6 to 8 words and adds "stop" first. My pick
   is the mapping line, since the 9 to 12 card follows the web-literacy book the band will adapt (later.csv L149).
   Tag: **scope**.

6. **The cycle card's "check" step becomes "judge" without a word.** Kindergarten to grade 1 use four pictures (ask,
   find, share, reflect; kindergarten day 3). Grade 2 day 16 adds a fifth picture, "check" (the grade 2 frame calls it
   the lens's judge step). Grade 3 day 1 opens the cycle card "with its six named steps" (ask, find, judge, use, share,
   reflect, grade 3 frame), so "check" is renamed and "use" added, and neither grade 3's day nor frame says so.
   Grades 4 and 5 day 1 then hold the six-step card. Why it matters: the card is the one model every year carries;
   a grade 3 child who learned "check" a few months earlier is handed a new word for the same picture. Fix: grade 3
   day 1's note adds one line, "the check picture from grade 2 is now called judge; use is new: what we do with the
   notes", and the grade 3 frame's inquiry arc says the same. Tag: **scope** (the frame line is **frame**).

7. **The class-level hand-off note is written at four seams of seven, and read at none.** Kindergarten day 30,
   grade 1 day 30, grade 2 day 29 and grades 6 to 8 day 54 each have the teacher pass the next teacher a class-level
   note of the moves to retrieve. Grade 3 day 30, grade 4 day 30 and grade 5 day 30 have none (grade 5's scope calls
   day 30 "the handoff to grade 6", but its note only sends the student's open question on, and 6 to 8 day 4's
   follow-up is picked inside the host study, so that question is not picked up either). On the receiving side, no
   course's first retrieval day (grade 1 day 2, grade 2 day 2, grade 3 day 2, grade 4 day 2, grade 5 day 2, grades 6
   to 8 day 1, grades 9 to 12 day 1) says the teacher reads the note to choose who gets the reteach. Why it matters:
   for a once-a-week special, that note is the only record of last year that survives the thrown-away checklist; as
   written it is work with no reader. Fix: add the same one-line note to grade 3, 4 and 5's last day, and to each
   receiving course's first retrieval day "the teacher reads last year's class-level note, where there is one, to
   plan the reteach"; 6 to 8 day 4 lets a student pick their grade 5 question as the follow-up where it fits the host
   study. Tag: **scope**.

8. **SEL's talk turn card is named on some library talk days and not others.** Kindergarten day 20, grade 1 day 16,
   grade 2 day 22, grade 3 day 21 and grades 6 to 8 day 47 open group talk with SEL's band card in SEL's words (SEL
   STANDARD section 7), "so students meet one set of words". The other talk days in the group do not: grade 4 day 17
   (restating an interview answer), grade 5 day 23 (say-back before pooling), grades 6 to 8 days 25 and 27 (the
   sourced discussion) and grades 9 to 12 days 13, 22 and 24, where day 13 tells a class to "set its own talk rules"
   and day 22 builds seminar ground rules of its own. Why it matters: the library course's own argument for the card
   holds on these days too, and in 9 to 12 a class is told to invent rules SEL's 9 to 12 card already gives. Fix: each
   of those days opens its talk with the band's card (3 to 5: listen, say back, ask a question, add your idea; 6 to 8:
   with choose how to talk first; 9 to 12: with check what landed and plan the next talk last), and library adds only
   its source rule ("where did that come from?"). Tag: **scope**.

9. **A program brand name on the grade 2 scope page.** Grade 2's "Sources not loaded" line names the K to 2
   online-safety presentation by its program brand; kindergarten and grade 1 describe the same listing without the
   name ("a free K to 2 online-safety presentation"). AGENTS.md keeps company and product names off anything a teacher
   reads, and the scope page is teacher-facing. Fix: reword grade 2's line as grade 1 has it. Tag: **scope**.

10. **Grade 1 has no record of whose voices a source set shows.** Kindergarten and grades 2 to 12 each carry the C12
    line ("whose voices: the unit records the makers of its read-alouds and pictures") on unit days or in the scope;
    the grade 1 frame states it, but grade 1's scope and days.csv never do (0 hits). Fix: add the line to each grade 1
    unit's inquiry day note (days 4, 10, 18, 22). Tag: **scope**.

11. **Grades 9 to 12 misdate the last use of the citation style.** Its readiness table says g7-citation-style was
    last used in library grade 7, "three grades back". Grades 6 to 8 retrieve it in grade 8 (day 42, unit 8) and use
    it in unit 9's cited product (days 49 to 53). The treatment holds (grade 10 is two years after grade 8, so a
    readiness check on day 27 is right), but the stated last use is wrong. Fix: "last used in library grade 8 (6 to 8
    days 42 and 53), two grades back". Tag: **scope**.

## What holds

- **No gaps.** Every one of the 98 progression rows is taught in its course and sits on a Check day; every owned id is
  plain on its row's days and on an end or course-level check; each of the 63 kept AASL ids has one owner, and the
  five excluded ids are not owned by any library row.
- **Seams by row.** Every assumed row is the year before, and every course's retrieval table names the day; the 6 to 8
  and 9 to 12 Seams tables match the rows of the course before, row for row (apart from finding 1's treatment). The
  only two-grades-back retrieval (grade 5 day 9, g3-safe-searching) is correct: grade 4 day 2 used it.
- **The stop rule** reads "close, tell, no blame" (K to 2) and "close the page, tell the adult, no blame" (3 to 12) on
  every device day of every course, and grade 12 day 57 teaches it back in its K to 2 words.
- **Load and calendar.** Doses follow APPROACH.md (25, 35, then 45 minutes every two weeks); every check sits in the
  week CALENDAR.md's end table gives; grade 2's 29 days carry their reason; the written sitting ramps from read-aloud
  sheets (grade 2, 15 to 18 minutes) to 20 to 27 minutes in grades 3 to 5 and 30 to 35 in 6 to 12. Grade 1's
  school_day of 5n - 2 (mid-week) against 5n elsewhere changes no week.
- **Unit 4 codes off the year-end check** in grades 2 to 5 follow lead call 10 the same way; mid-year checks sample
  only the unit before the one just assessed in every K to 5 course.
- **Sensitive ground** is handled the same way across the group: K to 5 neutral cases, honest use without shaming,
  interview rules (staff by role, consent), invented hoax and machine-made pages, the `rights` read on 6 to 12 fair
  use and license days, health's source-check card bridged on grade 5 day 8.
- **Named facts checked:** the four fair use questions (grade 8 day 42) match the federal copyright office's four
  factors; grade 3's password cards (length first, no symbol-swap) match current federal digital identity guidance;
  grade 3's storm rule "When Thunder Roars, Go Indoors" is the weather service's slogan (the grade 3 browser check can
  close); grade 5's "most bats" line is right to hedge.

## Sources

- https://www.copyright.gov/fair-use/ (opened 2026-11-26): the four fair use factors, for grades 6 to 8 day 42.
- https://www.weather.gov/safety/lightning-safety (opened 2026-11-26): the slogan "When Thunder Roars, Go Indoors",
  for grade 3 unit 3.
- https://pages.nist.gov/800-63-4/sp800-63b.html (opened 2026-11-26, first part of the page read): length over
  composition rules, for grade 3's password cards.
- https://en.wikipedia.org/wiki/Hyperion_(tree) (opened 2026-11-26): the tallest measured tree is a coast redwood,
  for finding 3.
- The 2022 high school lateral reading field study's size and lesson count (APPROACH.md's figure, used by 9 to 12):
  the news page address tried returned a search page, so browser check.

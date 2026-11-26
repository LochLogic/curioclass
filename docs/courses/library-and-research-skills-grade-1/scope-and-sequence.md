# Scope and sequence: Library and Research Skills, grade 1

Course `library-and-research-skills-grade-1` (catalog id `library-1`), grade 1, draft 2026-11-26, from the frame
(docs/courses/library-and-research-skills-grade-1/frame.md); the days live in
data/plans/library-and-research-skills-grade-1/days.csv.

## The year on the calendar

- **30 course days**, one session of about 25 minutes a week for 30 weeks (a specials slot), so course day n sits in
  week n. `school_day` = 5n - 2 (the middle school day of week n), so week = (school_day - 1) // 5 + 1 = n for every
  day. Units 1 to 4 hold 6, 6, 6 and 7 days (25), as the frame sets; days 13 and 14 are the mid-year check and its
  respond day, days 28 to 30 the year-end check and its two respond days. Weeks 31 and 32 hold no library session.
- **A session.** About 3 minutes at each end go to getting to the carpet or book corner and putting books back, so
  about 19 working minutes. Most teaching days after a unit's day 1 open with a retrieval task of five minutes at
  most; the `retrieves` column names its rows, and a day with that column empty has none. Check days have no
  retrieval opening.
- **Topic first.** Every know and wonder sheet starts from the topic named by word and a plain icon (no detail): the
  class fills the "know" box, and only then is the picture or book opened, in the owned id's own order ("before you
  start looking"). On check days the marking rule is "a fact the icon does not show, true of the topic", so a child
  cannot pass by drawing what a picture shows.
- **Kinds.** Understanding is the show-me day, Fluency the practice day, Application the inquiry day (APPROACH.md).
  Every unit's day 1 is a show-me day with the hook and the compelling question and nothing else. Fluency is small in
  grade 1: days 2, 8 and 17. Day 25 (stars and wishes, then each maker revises a page) is Application: a day that
  revises a piece of work is Application (GLOSSARY, teaching day), and the frame now says so.
- **No base text.** Every day is Curio Class's own; no source map. Paper path throughout: printed read-alouds,
  mini-books, sheets, cover cards, pretend screen cards, sticky notes and crayons. The one device day is day 9 (and
  day 10's teacher page), on the teacher's shared device or the printed card frame.
- **Standards.** Grade 1 owns one id, AASL.I.A.2 (g1-what-i-know). The other ids in `codes` are carried with help,
  written `~ID` as in data/progressions/library.csv, each owned in a later grade (AASL.V.C.1 comes back from
  kindergarten). Ids and our own words only (data/standards/aasl-words.txt).
- **Retrieval and readiness (rule 2).** Every earlier-grade row this course assumes is a kindergarten row, used the
  year before, so each opens as a retrieval task inside a day; no unit has a readiness check. Rows taught earlier
  this year come back as retrieval in later units.

| Earlier row | Last used | Treatment | Day |
|---|---|---|---|
| k-class-inquiry | Kindergarten | Retrieval | 2 (unit 1), 24 (unit 4, whose rows build on it) |
| k-wonder | Kindergarten | Retrieval | 2 |
| k-picture-book-labels | Kindergarten | Retrieval | 3 |
| k-listen-and-retell | Kindergarten | Retrieval | 8 |
| k-library-visit | Kindergarten | Retrieval | 9 |
| k-talk-in-group | Kindergarten | Retrieval | 16 (opening with the kindergarten turn card, "eyes look, wait my turn", in SEL's words) |
| k-who-made-book | Kindergarten | Retrieval | 17 (and named on day 16's model) |
| g1-what-i-know | Grade 1 unit 1 | Retrieval | 10, 22 |
| g1-find-in-a-book | Grade 1 unit 2 | Retrieval | 18, 22 |
| g1-author-and-title | Grade 1 unit 3 | Retrieval | 23 |

The frame placed the k-talk-in-group and k-who-made-book retrievals on unit 3's days 2 and 3, and that is where they
are here (days 16 and 17).

- **Evidence.** Daily: the teacher's class checklist of one named skill per child, thrown away at the end of each
  unit, plus the child's drawing, sheet or spoken answer. End-of-unit and check forms as the frame costs them (sheet
  item, scanned pointing item, whisper walk, station of three), each inside 19 minutes for a class of 30. Response
  time is the unit's respond day, counted once.

## Unit 1. What we know, and which book (days 1 to 6, weeks 1 to 6)

*What do we already know about a topic, and which book could tell us more?*

Arc: the know and wonder sheet modeled on a sunflower (day 1), practiced on two new pictures (day 2), then the
story-or-information choice modeled (day 3), then both run together on the class's question (day 4). The sheet comes
first because the connect step is the cycle's first and the unit's owned id; choosing the book needs a question
already held. Host: science:s1-sky-patterns (science grade 1 unit 1, weeks 1 to 4) or science:s1-parts-mimic (unit 2,
weeks 4 to 9), both in step with day 4 in week 4; stand-alone: "How tall do sunflowers grow?" Skill card withdrawn on
day 4. Day 4 also starts the unnamed class know and wonder chart kept for the year-end reflect step (day 30).

- **Readiness:** none (every assumed row was used in kindergarten; retrieval on days 2 and 3).
- **Mid-unit:** none (6 days).
- **End-of-unit, day 5:** a know and wonder sheet on snails, the topic named by word and a plain snail outline, the
  full picture shown only after the sheet is done (AASL.I.A.2: a real prior fact, unprompted, marked as a fact the
  icon does not show, true of the topic; the wonder box carries AASL.V.C.1), a story-or-information pointing strip
  and a whisper walk on why
  (g1-story-or-fact-book, ~AASL.IV.A.2). About 17 minutes. Response on day 6 (the self-check and a new wonder first).
- **Leans:** ELA's books that tell stories and books that inform (e1-stories-and-information) and shared research
  (e1-shared-research) come in ELA unit 2, weeks 7 to 15, later than this unit; day 3 teaches the choice itself and
  day 1 the sheet itself (the frame's "if later" lines).
- **Candidates:** telling easy from harder questions (a sort of the board's wonders on day 2): dropped, because
  day 2's 19 minutes already hold the five-minute retrieval and two sheets, and grade 2's g2-question-to-research
  sorts which wonders a book could answer, its natural home. Saying the "big picture" idea of a read-aloud orally:
  kept, zero days, one sentence at day 4's share circle.

## Unit 2. Finding the page (days 7 to 12, weeks 7 to 12)

*Where in a book, or on the page our teacher opened, is the answer to our question?*

Arc: finding the answering page by contents, headings, pictures and labels, modeled (day 7) and practiced in three
mini-books (day 8); then the second place grade 1 looks, the page the teacher opened, with the stop rule and never
typing a name or school (day 9); then both on the class question (day 10). The book move comes first because the
child already has the right book from unit 1; the stop rule is in place before the only device inquiry day. Host:
science:s1-parts-mimic (science grade 1 unit 2, weeks 4 to 9, just ended, so the class brings its tree questions
back on day 10); stand-alone: "What do tree roots do?" Skill card withdrawn on day 10; the stop pictures stay up.

- **Readiness:** none (retrieval of k-listen-and-retell on day 8 and k-library-visit on day 9).
- **Mid-unit:** none.
- **End-of-unit, day 11:** a contents page and spread not seen before, circle the heading and the page number
  (g1-find-in-a-book), then the labeled picture circled on a printed card-frame teacher's page on the same question,
  so the item asks for both kinds of place unit 2 teaches (~AASL.IV.B.1, about 2 minutes); the stop steps pointed
  in order for two pretend cases and a whisper walk on what we never type (g1-device-stop-rule, ~AASL.VI.A.1).
  About 18 minutes. Response on day 12. The class count of who met
  each move goes on the mid-year check sheet before the checklist is thrown away.
- **Lean:** ELA's text features (e1-text-features) come in ELA unit 3, weeks 16 to 24, later; day 7 teaches the
  contents page and headings itself, as finding tools only.
- **Sensitivity:** days 9 to 11 (Sensitive ground items 2 and 3): the teacher page says what the adult does if an
  upsetting picture appears (close it, the child tells, no blame) and points to health's steps; no child types
  anything; the pretend pop-up asks for a name so the class can practice not giving it.
- **The teacher's page** (days 9 to 11) is the unit's tree-roots read-aloud page on the Curio Class site, the same
  page printed in the card frame on the paper path; any other page the teacher picks gets the teacher page's swap
  note (what was checked, and when).
- **Candidates:** reading information in pictures and simple charts with help: kept, zero days, one of day 8's three
  mini-books has a labeled picture or simple chart as its answering page. Knowing what the internet is: kept, about
  2 minutes, one sentence on day 9.

## Course-level check 1, mid-year (days 13 and 14, weeks 13 and 14)

Day 13, week 13: new cases from unit 1 only (a know and wonder sheet on a new topic named by word and plain icon,
the picture held back until the sheet is done, a story-or-information
pointing strip, a whisper walk on why), about 17 minutes. Unit 2 ended on day 11, so the check draws on the earlier
unit, and unit 2's result is carried as the unscored class count. None of day 11's tasks (contents sheet, stop steps,
never-type walk) is given again. Day 14 (week 14) reteaches the missed step in small groups and ends with one fresh
try. Codes sampled: AASL.I.A.2, ~AASL.V.C.1, ~AASL.IV.A.2.

## Unit 3. Finding it together (days 15 to 20, weeks 15 to 20)

*How can a team find a fact, and say which book it came from?*

Arc: the three pictured jobs (day 15), then the source line "I found this in the book (title) by (author)" and
copying title and author onto a sticky note (day 16), both practiced with swapped jobs (day 17), then the cycle with
the group's drawing carrying its sticky note and each helper named (day 18). Jobs come before the source line because
the teller is the one who passes on a fact not their own. Host: ela:e1-shared-research (review), the shared research
on a bird's body parts in ELA grade 1 unit 3 (weeks 16 to 24, in step with day 18); stand-alone: "How do birds build
their nests?" Skill card withdrawn on day 18.

- **Readiness:** none (retrieval of k-talk-in-group on day 16 and k-who-made-book on day 17).
- **Mid-unit:** none.
- **End-of-unit, day 19:** stations of three on a new picture set: each child, holding one card of the set, says one
  finding of their own (~AASL.III.D.1, about 15 seconds) and names what one helper added (~AASL.II.A.1, about 10
  seconds); the jobs stay for handing and holding the cards. About 1.7 minutes a group, about 17 minutes for ten
  groups. The seated task during the stations is the sticky-note copy of a new cover's title and author
  (g1-author-and-title, ~AASL.VI.B.2), marked from the note afterwards, after one minute of whole-class
  instructions. About 18 minutes. Response on day 20.
- **Lean:** ELA's discussion (e1-discussion) came in ELA unit 1, weeks 1 to 7, before this unit; day 15 uses the
  class's talk rules.
- **Sensitivity:** honest use without shaming (item 4), days 16 to 19: a child who calls a found fact "mine" is
  helped to say "I found it in...". Groups mixed by the teacher, never by background.
- **Candidates:** drawing a conclusion in discussion: kept, zero days, the group says what its facts add up to at
  day 18's share. Knowing it is wrong to copy from an author or peer: kept, about 2 minutes on day 16, said as the
  habit of naming a fact's maker, never as a warning.

## Unit 4. Our class information book (days 21 to 27, weeks 21 to 27)

*What can our class find out together, and how do we make each page better?*

Arc: a finished pretend class book and the page template (day 21); each child picks a wonder from a picture menu of
6 to 8 wonders the source set answers (their own where it is on the menu) and finds the answering page (day 22; the
source set is written so each menu wonder has one answering page, so every child has a found fact by day 23); drafts a page with a sticky-note source line (day 23); star and wish modeled (day 24); stars and
wishes in pairs and each maker revises (day 25); the book shared on day 27 after the end-of-unit assessment. The
page is drafted before feedback is shown so the star and wish have real work to land on. Seven days by load: the
product needs draft, advice and revision (the frame's reason). Host: science:s1-parent-offspring (science grade 1
unit 7, weeks 24 to 26) or caring for birds in ELA grade 1 unit 4 (weeks 24 to 32); stand-alone: "How do animal
parents keep their babies fed and warm?" Skill card in hand on day 23, withdrawn on day 25.

- **Readiness:** none (retrieval of g1-what-i-know and g1-find-in-a-book on day 22, g1-author-and-title on day 23,
  k-class-inquiry on day 24).
- **Mid-unit:** none.
- **End-of-unit, day 26:** a short passage read twice with a held question, each child draws and labels an answering
  fact and writes or dictates a sentence (g1-class-book, the product standing for ~AASL.I.B.3, about 9 minutes); a
  star drawn on a pretend classmate's page, then a whisper walk on two things, "This page taught me ___"
  (~AASL.I.C.1, what the work says) and a wish (g1-star-and-wish, ~AASL.I.C.2), about 15 seconds a child. About 18
  minutes. Response on day 27: the teacher reads each page's sentence (about 6 minutes), each child tells a partner
  one thing a friend's page taught them (2), the self-check by pointing (2), the reteach and fresh try (9).
- **Leans:** the science host (s1-parent-offspring) comes in weeks 24 to 26, after days 22 and 23; the bridge from the
  frame's "if later" line: the class asks and finds from Curio Class's animal-parents read-aloud, and science's unit
  then meets pages already drafted. ELA's shared research and writing (e1-shared-research) came in ELA unit 2, before.
- **Sensitivity:** kind feedback (the star first; wishes about the page, never the child; the maker may say no).
  Animal parents keep to feeding and warmth, never a hunt or a lost young one. No family photo or fact in the book.
- **Candidates:** beginning to respond to feedback to revise: kept, zero days, day 25. A group product for classmates
  and families: kept, zero class days, the book may go home in turn by the school's rules (day 27, family note).

## Course-level check 2, year-end (days 28 to 30, weeks 28 to 30)

Day 28, week 28: all sheet and pointing items on new cases from units 1 to 3 (contents page, sticky-note copy, know
and wonder sheet on a topic named by word and plain icon, stop steps), about 18 minutes. The contents page item is
g1-find-in-a-book alone, one source, so ~AASL.IV.B.1 is not claimed on this check; day 11 holds it. Unit 4 was assessed on day 26, so the check draws on earlier units
and carries unit 4 as the class count; day 26's passage page and star-and-wish forms are not given again. Day 29
(week 29) reteaches the gaps; day 30 (week 30) is the year's reflect step on the unnamed class chart from day 4, and
the class-level note for the grade 2 teacher (the class book is reread there, not made, so day 30 claims
g1-what-i-know only). Codes sampled: AASL.I.A.2, ~AASL.V.C.1, ~AASL.VI.B.2, ~AASL.VI.A.1.

**Owned code on a course-level check:** AASL.I.A.2 is sampled on both (days 13 and 28). The carried ids not sampled
on a check (~AASL.IV.A.2 and ~AASL.IV.B.1 at year-end, ~AASL.III.D.1, ~AASL.II.A.1, ~AASL.I.B.3, ~AASL.I.C.1, ~AASL.I.C.2) are owned
in later grades, assessed on their unit's end day here, and not claimed by this course.

**Weeks.** 13 and 28, as the frame and CALENDAR.md give. Library is a special, so the K to 5 stagger rule (CALENDAR.md
rule 1) does not count it; neither week is a grade 1 core check week (14, 15, 16, 19, 29 to 32). Any after-core
check sharing week 13 or 28 is settled by the same rule.

## Shorter path

- **A shorter session** (about 20 minutes, not 25, so about 14 working minutes): teaching days hold by cutting the
  five-minute retrieval openings to three minutes and the share circles to two or three children. Each check day
  names what runs alongside its seated sheet item:
  - Days 5, 11, 13 and 26: the whisper walk runs while the children work on the sheet, the teacher walking the room
    as they draw (about 11 to 12 minutes in all).
  - Day 19: the sticky-note copy is already the seated task while the stations run (about 14 minutes with the
    stations at about 1.3 minutes a group, each child's finding and helper turn kept).
  - Day 28: the four items read once each on one sheet (contents 4 minutes, sticky note 3, know and wonder 5, stop
    steps 2: about 14 minutes).
- **A year about 10 school days short** counts as lost sessions wherever they fall (the arts scope lead call): for a
  once-a-week course that is about 2 sessions. Fold-ins 1 and 2 below cover them, and fold-in 3 covers a third, with
  nothing assessed and no owned or carried part cut. Each receiving day still holds 19 working minutes:
  - Fold-in 1, day 3 into day 4: day 4 has no retrieval opening (k-wonder was retrieved on day 2), opens with the
    story-or-information model in 5 minutes on the two sunflower covers, does the bin fetch (k-picture-book-labels)
    as the act of choosing the book, and takes the share circle to three children.
  - Fold-in 2, day 24 into day 25: the star and wish modeled on the pretend page in 5 minutes, one star and one wish
    in pairs (6 minutes), revision (8 minutes); k-class-inquiry is pointed at in day 27's self-check.
  - Fold-in 3, day 29 into day 30: the reteach in small groups (10 minutes) and the reflect step on the class chart
    (9 minutes), without rereading the class book (it was read on day 27).
  Every end-of-unit day (5, 11, 19, 26), both check days (13, 28) and the respond days 6, 12, 14, 20 and 27 stay.
- **Leave-out.** A school may leave out a unit by the SEL, PE and arts rule (STANDARD.md section 4); a left-out
  unit's ids are named as not claimed that year. Where unit 4 uses a left-out unit's card (unit 1's sheet, unit 2's
  contents move, unit 3's source line), the leave-out bridge rule holds: unit 4 teaches that card's one-step form in
  its first ten minutes and claims none of the left-out unit's skills. Leaving out unit 1 leaves AASL.I.A.2 unclaimed
  that year, and two more days change: day 10 opens with the know and wonder sheet's one-step form (say one thing you
  know, one thing you wonder) in place of its retrieval, claiming nothing; and day 13, with no unit 1 to sample,
  samples unit 2 on new cases in forms not given on day 11 (a contents page item and the stop steps for a pretend
  case, about 11 minutes).

## Sources not loaded

No day leans on the online-reasoning lessons, the web-literacy book or the AASL 3 to 5 band file (later.csv L149);
grade 1 plans from the frame and the PK to 2 band file read for it. The frame's Sensitivity reads list a K to 2
online-safety presentation; its listing (opened 2026-11-26) names it as a free download but does not state its rule,
and the file was not read, so day 9's stop rule rests on nothing in it. All read-alouds,
mini-books, cards and sheets are Curio Class's own and not yet written.

## For the lead

1. **Unit 4's science host runs later** (weeks 24 to 26) than days 22 and 23; the bridge stands, and where a school
   runs science's parents-and-young unit earlier, the class uses it.

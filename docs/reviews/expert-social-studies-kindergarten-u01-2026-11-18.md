# Expert read: kindergarten social studies, unit 1, days 1 to 10 (probe, 2026-11-18)

One reader, the whole unit, day by day in order. Acting as docs/agents/EXPERT.md says; each day judged as
docs/pipeline/briefs/expert-day.md says (no cheap read this probe). Findings are tagged for docs/pipeline/PROBE-GUARD.md.

## What I read

- Rules and lens: AGENTS.md, docs/agents/EXPERT.md, docs/pipeline/briefs/expert-day.md, docs/pipeline/PROBE-GUARD.md,
  docs/agents/lenses/social-studies.md, docs/courses/LESSON-DAY.md, docs/GLOSSARY.md (the rows on assessment, readiness,
  exit ticket, record sheet), docs/courses/social-studies-kindergarten/DEFAULTS.md.
- Plans: s01.md in full (unit plan), u01-1.md (section 1.1, days 1 to 2) and the day lines of u01-2.md, plus the
  grep of u01-3.md for the rotation and bridge rules; frames.csv row for the course.
- Unit data: all unit 1 rows of items.csv (R1 to R3, X1 to X8, X10, E1 to E8), wrongs.csv, errors.csv, days.csv,
  handbacks.csv, materials.csv, parts.csv.
- Days: d001 to d010 in full; every piece in u01-1, u01-2, u01-3 (openers, read-alouds, all cards files, readiness,
  record, family note).
- Built pages (after `python -X utf8 scripts/lesson.py build --pdf`): teacher, student, key, exit, display and home
  pages for days 1 and 7 to 10 in full, the other days by sampling, and record.html.
- Gates: `plan.py check` and `lesson.py check`. Unit 1 days 1 to 10 show 0 failures. The seven "not in data/units.csv"
  failures are the known ones. One note on d009 (end items can show errors that "the respond part names no group
  for", which is right: day 10 is the respond day). The day 12 failure and day 11 failure belong to the other agent's
  work and are not judged here.
- Earlier probe reports: docs/reviews/probe-social-studies-2026-11-15.md and probe-social-studies-2-2026-11-15.md
  ("Back to the builders"), and the kinds in data/plans/defects.csv for us-history-i and world-history-i.

Not opened: anything on the never-open list.

**The handoff into day 1.** There is no earlier day: kindergarten social studies unit 1 opens the course (s01.md
section 3, "none precedes"). The handoff therefore holds trivially, and the unit plan's stated assumption (no preschool,
no discussion routines) is carried: day 1 asks for nothing the children have not been shown. One caution: day 1 lands
on school day 3, and a rug, partner turns, an easel, a sink and cubbies are assumed to exist and be known by name.
Nothing here is a finding; it is a point for the teacher's opener.

## Verdict per day

- **Day 1.** Content is right and gentle, but the day is overloaded (a 10-page read-aloud, a Q and A, the bear, the
  bird, the wall and a check in 20 minutes), the built teacher page garbles the three readiness items into the middle of
  its sentences, and the check reaches six children, not thirty. Not teachable as written.
- **Day 2.** The read-aloud and exit hold together, but the supported work (many at once or one at a time) does not
  teach "each person is different, the class shares one room and one set of rules", and the day promises readiness
  coverage it does not carry.
- **Day 3.** The best-built day in the unit: a made-up consequence on the glue, a modelled why-question, and an exit
  that fits. Weak spots are the "wipe the table" pairing and the missing practice note.
- **Day 4.** Sorting "to a maker and to a reason" has nothing to sort to, and the crosswalk, sign and gate make the
  maker the person who paints or latches, not the body that decides the rule.
- **Day 5.** The unit's anchor day (Our Class Charter) is asked to do a pick of two rules, two dictated reasons, a
  what-if talk and a drawing in 10 minutes, with art the teacher must draw first; and one candidate rule is reused as
  day 8's "invented" teaching card.
- **Day 6.** Sound idea and good cards (the answering reply always attends to the same thing). The day returns an exit it
  does nothing with, and "choose six not yet heard" has no children left to choose.
- **Day 7.** The two-view cards are fair and unranked. The exit changes puppets (Moss and Wren to Pia and Tov) and asks
  "alike" in an adult way, and the practice note is the only one in the unit.
- **Day 8.** Good modelled claim, why-question and answer. The exit as written cannot show error F because the puppet
  asks, and the "shared rule choice" observed for item 5 is only two children speaking.
- **Day 9.** Cannot be done in its minutes. The tasks, the fresh pictures and the look-fors are sound; the
  administration is not.
- **Day 10.** The respond logic (group by the letter whose move repairs it) is right. Four tables and a fresh try per
  child in 10 minutes is too much for one adult, it prints a student page and an exit for children who never use them,
  and its input (day 9's marks) is in a different vocabulary than day 9 writes.

## Findings, most serious first

Each line: `N. [dNNN part] what is wrong | why it matters | exact fix | origin=<layer> | repeat=<yes|new>`

1. [d009 The day, 15 min groups and 3 min look back] Five groups of six get "three minutes each", so six children share
   half a minute for item 1 (about 5 seconds a child), one minute for items 3 and 4 together (10 seconds a child for two
   settings, a function and a proposed change), and half a minute each for items 6, 7 and 8; the look back asks for each
   child's dictated line on their drawing in 3 minutes; 24 five-year-olds draw alone for 15 minutes; then the sheet is
   marked for ten minutes after class | the unit's only end-of-unit evidence cannot be gathered, so most cells will be
   "not yet observed" and day 10 will have groups made from gaps in the clock, not in the children | Make day 9 the
   30-minute route (frames.csv allows it) with groups of six at 5 minutes: each child answers item 1 and item 7 in
   turn (one sentence each, 15 seconds), items 6 and 8 as one pair exchange (the partner asks, the speaker answers);
   hear School Doorway (item 3 and 4) on day 9 and Garden Path on day 10's 8 fresh-try minutes; take the dictated line
   from the six being heard, not from all; change s01 section 5 "Administration for thirty children" and days.csv
   `check_min` to match | origin=unit | repeat=yes

2. [d003, d004, d005, d006 The day, supported work] s01 section 5 says each child gets a practice note "from the one day
   among days 3 to 7" the child is in the rotating six, read privately that day or the next; only day 7 writes one
   ("write one thing done and one next step"), and day 8 notes item 5. Days 3, 4, 5 and 6 never say it (day 6 says only
   "Notes today are practice") | 24 of 30 children reach day 9 with no practice note, so by the plan's own rule items 2
   and 5 are "not yet observed" for them and are not scored | In each of days 3, 4, 5 and 6 add to supported work: "Write
   the six's one thing done and one next step on the record sheet; read it to each child privately by tomorrow" (about
   40 words each; the cap has room only if the day is lengthened, see 9) | origin=day | repeat=yes

3. [d001 to d008 Before class, "Choose today's six"] Days 1 to 5 each take "six not yet heard on a spoken exit", which
   uses up all 30 children by day 5; days 6, 7 and 8 then say the same and have no one to choose. The unit plan also
   wants days 3 to 7 to be five groups covering all 30 (the practice-note rotation), so days 1 and 2's sixes, chosen by
   "not yet heard", overlap days 3 to 7 or break them | The teacher cannot tell who is in today's six on days 6 to 8,
   and the practice note, the exit "heard once a week" and the readiness catch-up cannot all be true at once | Put one
   rotation on the record sheet: a "group day" column assigning each child to one of days 3 to 7 (six each); say on each
   day "today's six are the day-N group on the sheet"; days 1 and 2 take the first two groups' children early for the
   readiness items only; day 8 repeats the day 3 group | origin=unit | repeat=new

4. [d001 The day (start-of-year check), d002 Before class and supported work, d003 Before class] The check reaches six
   children on day 1 (R2 for the six, R3 in three pairs, R1 whoever speaks). s01 and u01-1 say "the rest are noted on
   days 2 and 3 and recorded by the end of day 3"; days 2 and 3 only say "Note the support for the six" for R3 and "Meet
   the s01-R2 group", with no step that runs R1, R2 or R3 for the other 24 | The day 2, 3 and 4 bridges are aimed at
   "children who needed support", a list that exists for six children, so most children who need a bridge never get one
   and the "access observations" that shape cues and partners are mostly blank | Give day 2 supported work and day 3
   supported work a line that runs R3 (day 2) and R2 (day 3) for that day's six and the day 1 children still unseen, and
   name on day 4 how R1 is taken for the rest; or cut the promise from s01 and the openers and say only six are looked
   at | origin=day | repeat=yes

5. [d001 to d010 print line and the built dNNN-exit.html] DEFAULTS says exit items are `path spoken`, "no paper ticket
   prints", yet the build writes dNNN-exit.html: four tickets to a sheet, each with "Name ______ Day N", the whole adult
   stem ("Invented for practice: ... Mark: circle ... Spoken: ...") and two writing lines, for five-year-olds who do not
   read or write; and every day's print line also asks for a per-child exit card from cards-exits-N. The mark everyone
   makes cannot show the errors the next day repairs (A, B, K, H come only from the six spoken whys) | A teacher who
   prints the sheet hands children a page they cannot use; the paper mark costs a hand-out and a collection every day
   for no evidence the hand-offs read | In lesson.py, build no exit.html for an exit whose `path` is spoken; either drop
   the per-child exit card (the six answer aloud with the picture card held up, the class list marked) or make the card
   the only printed exit and say so in DEFAULTS; delete "Name ... Date" lines from the kindergarten student page | origin=template | repeat=new

6. [d008 exit X8 and items.csv X8 wrongs] The teacher page has the puppet ask "Why do you think that?" in the exit, but
   the item and look-fors say "the partner's question aims at the claim", and the F wrong answer is "the partner asks
   what color the bucket is" (the teacher page also lists it) | A puppet's question cannot be about the color, so error F
   cannot be shown, the look-for cannot be ticked, and day 10's picture table (E, F, L) is built from a mark the exit
   cannot give | Either the six ask each other (a child partner asks, as E8 does) or drop F and the "partner's question"
   look-for from X8 and the wrongs row, and take F only from the day 8 partner practice; make items, wrongs and
   the day say the same | origin=unit | repeat=yes

7. [d009 Before class, "independent, content-prompted or not yet observed"; d010 Before class, "0 and 1 cells"; record.md]
   Three recording languages for the same cells: day 9 marks each part independent, content-prompted or not yet
   observed; the unit plan and day 10 read "0 and 1 cells"; record.md says "one tick for each look-for met" across 36
   columns. The sheet has 28 rows for a class the plan sizes at 30, no place for the dated attempts E2 and E5 need, no
   group-day column (see 3), and the E2 and E5 columns have three look-fors but no column for the two occasions | The
   teacher cannot move from day 9's marks to day 10's groups without inventing a mapping | State once, in record.md and
   both days: independent = 2, content-prompted = 1, not yet observed = blank (0 is never written for an unheard part);
   rows: 32; add a date and a group-day column | origin=unit | repeat=yes

8. [d005 The day, supported work (10 min)] The class picks two of three teacher-drawn rules, gives a "because" for each
   (written beside a quick picture, symbols "finished after class"), discusses a what-if picture and agrees how to
   change a rule, then every child draws a charter rule, in 10 minutes. No method for "the class picks two" (voting is
   taught on days 13 and 14), and the teacher must draw three two-panel candidate pictures and a what-if card before
   class | Our Class Charter is the evidence for days 8 and 9 and the unit's only real source; if it is rushed or thin
   it is teacher-made, and the picks are decided by the loudest | Make day 5 the 30-minute route; pick by pointing (each
   child puts a counter on one of three pictures, two highest stay) and say so; cut the what-if talk to the picture and
   one sentence, and move the drawing to a three-minute exit; ship the three candidate pictures and the what-if card as
   a cards piece instead of asking the teacher to draw them | origin=section | repeat=yes

9. [All days, days.csv and u01-N.md minutes] Every day in unit 1 is pinned to 20 minutes (2 + 6 + 10 + 2, day 9 as
   2 + 15 + 3), the frame's lowest, though DEFAULTS says "most days 25"; the other agent's days 11 and 12 run 25. No time
   is budgeted for moving 30 five-year-olds from rug to tables and back, handing out cards, or collecting them | These
   are the first weeks of school: the transitions alone are 3 to 5 minutes, so the 2-minute exits and the 6-minute
   read-alouds are cut first and the spoken why, the thing being measured, is dropped | Set days 3 to 8 and 10 to 25
   minutes and days 1, 5 and 9 to 30 in days.csv, with the extra 5 minutes named as transition and the six-child
   talk; re-run plan.py tables; keep the frame's 20 to 30 | origin=unit | repeat=yes

10. [d001 The day, 8 min Hook and wonder wall; Exit ticket] In 8 minutes: ten pictures read page by page, an Ask,
    posting the big question, the bear model, a reason model, the sink-and-bird wonder, and writing each wonder with a
    picture; the exit is "circle on the room card", then two spoken questions to six children in 2 minutes; the last
    sentence "Bring home answers back to our room" is cryptic | The first day of school is where five-year-olds learn
    that this is a place where they may wonder; rushed, the teacher reads and the children do not wonder | Use the day's
    own "shorter" read (pages 1, 2, 3, 5, 6, 7, 10) as the day, move the bear and the bird to the first two minutes of
    the check, and replace the last sentence with "If a child names home, thank them and bring the answer back to our
    room" | origin=day | repeat=yes

11. [d005 Before class and d008 The day, teaching card] Day 5's candidate rules are "the scissors tub, the book bin, the
    door line", and day 8's "invented" teaching card (kept apart "from every exit and assessment picture") is the
    scissors tub, claim "everyone can find them" | If the class picks the scissors tub on day 5 (or the card is
    remembered), day 8's model is the child's own charter rule and the claim is copied, not made; item 7 and 8 evidence
    is then a repeat | Change day 8's card and its Ask and model sentences to a thing day 5 never lists (the paper
    tray, a low hook for bags); keep scissors off the candidate list's overlap | origin=day | repeat=new

12. [d004 The day, supported work; cards-rule-makers; day 3 words] Pairs "sort each card to its maker and to a reason
    (safe, fair, or helps everyone)". Each card already has its maker drawn in its corner and the three reasons exist
    nowhere as cards, only as spoken words; day 3 named the third reason "helps us learn", day 4 "helps everyone" | A pair
    has nothing to sort to, so "sorting" is the teacher telling; the changed word breaks the reason chain from day 3 |
    Add to cards-rule-makers three reason cards (shield, two hands taking turns, open book) and three maker cards to
    sort to, and use one set of words (safe, fair, helps everyone learn) on days 3 and 4 | origin=day | repeat=yes

13. [d004 The day, Rule-maker cards; X4 exit card] The cards show the people who paint the stripes, put up the sign and
    latch the gate, and the teacher says "road workers made it". The rule (cars stop at the crosswalk) is made by the
    town, not by those who paint it, and a gate is a barrier, not a rule; the exit asks "circle the person who made the
    rule" with a school helper latching the gate | Five-year-olds will learn that whoever puts up the sign made the
    rule, which a later unit (rules, government) has to undo; the plan itself marks "roles from memory" | Change the
    makers to the deciding body in words a child can hold ("the town", "the library people", "the park office") with
    the worker shown putting it up second; change the day 4 exit card to a sign being put up and ask "who decided" only
    if a decider is pictured, otherwise key the reason alone and drop the mark | origin=section | repeat=new

14. [d005 to d006, d007 to d008 Tomorrow and Reopen] Day 5's exit shows errors B, E and J; day 6 "returns day 5's exit"
    and asks which rule helps if two people want the same thing, and repairs none; no handbacks.csv row for 5 to 6 or
    7 to 8 (E), and day 8 repairs only D. "Return the exit" is a math habit: a spoken mark returns nothing a child can
    read | The next-day branch the plan relies on (field 6) is silent for three of the unit's exits, and the reopen
    spends two minutes on a ritual | Drop "return day N's exit" in days 6 to 8; add to day 6's reopen and day 8's reopen
    one line each acting on B, E and J (day 6) and E (day 8); add the handbacks.csv rows | origin=day | repeat=yes

15. [d001 The day, 10 min and 2 min, and d002 Reopen and Exit ticket; d001 Tomorrow] The `[[s01-R1]]`, `[[s01-R2]]`,
    `[[s01-R3]]` and `[[s01-X1]]` marks expand in the built teacher page to the whole item stem and its bracketed key,
    inside the sentence ("ask Show a toy bird on the edge ... [Any relevant question ...]: 'What do you wonder?'",
    "pairs do Say, choose a block ... [Record access ...]"); the same on the Tomorrow line; days 3 to 10 write the id as
    plain text and read fine | The teacher reads doubled, bracketed text on the first day of school and the page runs
    about 950 words | Write the ids plain, as day 3 does ("(s01-R1)"), in days 1 and 2 | origin=day | repeat=new

16. [d008 The day, 11 min partner practice and Exit; s01 E5] Item 5's third look-for is "takes part in the shared rule
    choice of day eight", but the reopen has two children say which rule to look at and "this is two turns, not a vote",
    and the day sits with the six for the "reopen choice" | Four of the six cannot show what the look-for asks, and the
    other 24 never could | Make the shared choice a whole-class one: each child points to one of the two charter pictures
    and says "I want ___ because ___" in pairs; then the six's turn and response are observed in the partner practice | origin=day | repeat=new

17. [d002 The day, supported work (and u01-1.md day 2)] The goal is "each person is different, and the class still shares
    one room and one set of rules"; supported work sorts four room cards by "many of us at once, one at a time", which is
    about how a place is used, not about differing people or rules; the student page repeats it ("We are different. We
    share one room.") over those two boxes; the exit asks "what both need" | The goal's second half (shared rules)
    is untaught and the pair work is off the point | Replace the sort with: each pair is given two of the eight
    pictured things from Everyone Has a Place (a book, a cup, a cloth, a turn card) and points to the room card where
    each is used, then to the card that both use; or cut "one set of rules" from the goal in days.csv and say day 3 owns it | origin=section | repeat=new

18. [s01 section 5 item 2; d003 error G, d009 item 2] The unit scores whether a five-year-old follows a class rule "with
    at most one neutral reminder" on two dated occasions, records reminders, and day 3 teaches error G by drilling "cap
    a marker; then cap another without the picture"; day 10 groups children for G | It records a young child's
    compliance as a score, which the unit's own limit ("no child labelled a rule-breaker") and the opener's "stillness
    is not a look-for" push against, and it takes the most teacher time for the least reliable evidence | Keep the
    standard (MA.K.T1.1 asks it) but take E2's "follows a rule" as a teacher's yes/no note across days 7 to 9 with no
    reminder count and no group; score only asking and answering why; remove G from day 10's wonder table | origin=unit | repeat=new

19. [wrongs.csv s01-X5, errors.csv J] The wrong answer "I would just change it so I go first" is filed under J ("I can
    change a shared rule without telling anyone"); it is a self-serving fix, not a skipped consultation, and its repair
    ("model asking the class and the teacher first") does not address it | The fix taught for J does nothing for the child
    who made the answer | Re-file under E-style "no reason for others" or add a letter for taking the turn, and give X5 a
    J wrong that is about telling no one ("I would change the rule myself and not say") | origin=unit | repeat=yes

20. [d003 The day, supported work; cards-rules-day3] "Wipe the table" is keyed "helps us learn", while its protects card
    shows "a clean table for the next person" and teaches nothing about learning | A child who says "fair, so the next
    person can use it" (correct, and the day 5 charter reasoning) is marked wrong against the teacher's key | Key the pair
    as fair or helps us learn ("another pictured reason is right" is already said for the other two; say it for this one
    and write it on the card) | origin=day | repeat=yes

21. [d007 Before class, The day, exit; cards-exits-6-10] The day uses puppets Moss and Wren; the exit changes to Pia
    (round head) and Tov (star), and Moss is round-headed like Pia; the spoken question "How are their ideas alike or
    different?" has a key of "both choose a first thing", which is an adult abstraction | Children map Pia to Moss, and a
    child who says "they both want to start" is right but outside the key's words | Use Moss and Wren on the exit card
    (swap their heads' marks to keep them distinct from the day), key "both want to start with something" and
    accept it | origin=day | repeat=new

22. [d010 materials and print; student page; cards-exits-6-10; items.csv X10] The student page "A rule helps / Who it
    helps" is printed for each child but the class day never uses it (only the home view does); the built d010-exit.html
    prints a museum exit for every child but only the sorting table does it; the look-for says "circles the objects or
    the people looking" and the card has no people to circle | The teacher prints and files two sheets nobody uses and
    the look-for cannot be met | Take the student page and exit sheet off the day's print line (home keeps them); add a
    "people looking" circle to the museum card or cut that phrase from the look-for | origin=day | repeat=yes

23. [DEFAULTS and lesson.py teacher-prose cap] The cap is a flat 450 words from the longest day's 30 minutes; the unit's
    20-minute days sit at 439 to 450 words, so about 22 words a minute, half again over the 15 a minute LESSON-DAY sets,
    and all nine teaching days are at the cap | Every day is written to the ceiling and then has no room for the missing
    lines (finding 2, 14, 16) | Make the cap per day (15 a minute: 300 at 20 minutes, 375 at 25, 450 at 30), which forces
    finding 9's minutes up, and say it in DEFAULTS | origin=template | repeat=new

24. [d001 to d010 display and home views] The built display page for every unit 1 day is a blank page with only the foot
    line (28 words); the home view prints the internal id as "S01-X1" in the parent's list | A teacher with one screen
    gets nothing; a parent reads jargon | For `path` spoken days, build the display as the read-aloud pages list
    (page numbers and captions) or do not build it; print the exit's question in words, not its id, in the home view | origin=template | repeat=new

25. [d008 Tomorrow; d009 title] "Day 9 is the unit check" (and the day title "Our check"); GLOSSARY lists "end check" and
    "check day" as words not to use and gives "end-of-unit assessment" | A small drift from the locked words in a day a
    parent also reads | Write "the unit assessment" in d008 Tomorrow and d009 | origin=day | repeat=yes

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Reason words for rules are "safe, fair, helps everyone learn" on days 3 to 5 | One chain from the glue story to the charter | d003.md, d004.md, cards-rule-makers.md |
| Day 7's exit uses Moss and Wren | Same puppets as the teaching | d007.md, cards-exits-6-10.md, items.csv X7 |

## For Cory

None. Findings 9 and 23 touch the frame's 20 to 30 minute range but not scope or audience.

## Count line

25 findings: by origin day 12, section 3, unit 7, scope 0, frame 0, template 3; by repeat yes 14, new 11. Plan share (unit, section, template, scope, frame) 13 of 25 (52%).

## Fix

1. FIXED: day 9 now 30 minutes (5 a group, items 1 and 7 together, items 3 and 4 on School Doorway, items 6 and 8 as one pair exchange); Garden Path moved to day 10 (15 fresh-try minutes); dictated line from the six heard last; s01, u01-3, days.csv check_min and handbacks agree.
2. FIXED: days 3 to 6 each add the practice-note line for the day's six.
3. FIXED: record.md gains a group-day assignment (3 to 7, day 8 repeats day 3), each day names its group, days 1 and 2 look early at the day 4 and 5 groups.
4. FIXED: days 2, 3, 4 run R3, R2, R1 for the six and any child still unseen; s01 section 4 says recorded by the end of day 4.
5. LEAD: confirmed after a rebuild (not stale): lesson.py should build no dNNN-exit.html for a `path` spoken exit, and DEFAULTS must settle whether the per-child mark card is the one printed exit (s01 section 5 and the exit-card pieces say every child marks a card).
6. FIXED: day 8 exit has the six ask each other in pairs; X8, wrongs and the day agree.
7. FIXED: one language (2, 1, 0, blank) in record.md, d009, s01; rows 32; group day and date written into the sheet text (the printed grid has no such columns: template).
8. FIXED: day 5 at 30 minutes, counters to pick, what-if cut to a picture and one sentence, candidate and what-if pictures shipped in cards-claim-frame; drawing kept in supported work because the day has the time.
9. FIXED: all ten days run 30 minutes (content did not fit 20), prose kept under the per-day cap.
10. FIXED: day 1 reads the shorter page set, bear and bird move into the check, last sentence rewritten.
11. FIXED: day 8 card is the paper tray, not the scissors tub.
12. FIXED: maker and reason cards added to cards-rule-makers; one reason vocabulary on days 3 and 4.
13. FIXED: makers are the deciding body (the town, the library people, the park office), worker second; day 4 exit asks what the gate keeps children away from.
14. FIXED: no "return the exit" on days 6 to 8; day 6 reopen repairs B, E, J, day 8 reopen repairs D and E; handbacks rows added.
15. FIXED: plain ids in days 1 and 2 teacher prose.
16. FIXED: day 8 shared choice is whole class (point, then tell a partner).
17. FIXED: day 2 supported work and student page now teach different people and one shared room.
18. FIXED: E2 is a teacher yes or no note with no reminder count and no group; G removed from day 3, day 10 and the s01 grouping table.
19. FIXED: the go-first wrong answer is filed x; a new J wrong answer added.
20. FIXED: wipe the table keyed fair or helps everyone learn.
21. FIXED: day 7 exit uses Moss and Wren and accepts "both want to start with something" (puppet marks kept as the day's, not swapped).
22. FIXED: student page and exit sheet off day 10's print line; X10 look-for no longer asks for people; the template-built d010-exit.html stays with finding 5.
23. FIXED (by the lead): per-day cap in lesson.py and DEFAULTS.
24. LEAD: for `path` spoken days build the display from the read-aloud pages list (or skip it), and print the exit question in words, not its id, in the home view.
25. FIXED: "unit assessment" in day 8 Tomorrow, day 9 title and day 10 at-home.

Count: 25 findings: 23 fixed (22 by this pass, 23 by the lead), 0 rejected, 2 LEAD (5, 24; origin template).

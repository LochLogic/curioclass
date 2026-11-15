# Lead calls for the science, ELA and math scope fix pass, 2026-11-15

The lead's answers to the "For the lead" and "Across the band" items of the 37 expert reads
(docs/reviews/sequence-<course>-2026-11-1[45].md), plus Cory's calls. The fix pass applies them as settled; it does not
re-decide them. Rules that are now in docs/pipeline/briefs/sequence-write.md are named, not repeated.

## Every subject

1. **Readiness is counted by grade number** (sequence-write.md rule 2, "Count by grade number"): a row last used in
   grade g gets retrieval in grade g+1 and a readiness check in grade g+2 or later. Every frame's gloss that says
   "two or more grades between" (or otherwise reads differently) is corrected to the brief's wording, and each course
   re-checks every earlier-grade row against it: list each row with its last-use grade and its treatment in the scope
   and sequence, once, by one method.
2. **Collect once, checks claim only what they sample, each part of each code, end days, our words, class size 30**:
   as in sequence-write.md rule 2. A course-level check never re-scores unit work and never repeats a task form given
   in the last two weeks; it draws new cases. A check reuses any one-to-one or small-group record taken in the last
   ten days and says so.
3. **One source-map layout** (sequence-write.md rule 8, gated by sequence.py): convert every source-map.csv to
   `source,title,goals,standards,unit,days,decision,why,order_conflict,harms_learning[,url]`, decisions keep, split,
   merge, cut, ours only. Keep every row's content; nothing is lost in the move (an old column with no home, such as a
   licence or a minutes note, goes into `why` or `url`). Days that adapt no base lesson drop "Base" from their goal and
   note.
4. **Shorter path**: each fold-in day names the minutes it saves, and the section states its total against the
   frame's day count (rule 10).
5. **Copied base wording**: check every goal, note and source-map cell against the base text (OpenSciEd, EL Education,
   Illustrative Mathematics); rewrite any copied or lightly edited lesson purpose, goal, title sentence or teacher note
   in Curio Class words.
6. **Religious texts** (Cory, 2026-11-15, DESK-ANSWERS): where a standard calls for one, a religious text is read as
   literature or history, never as scripture; no religious text is an anchor; no student states or performs a belief.
7. **Timers** (Cory, 2026-11-14): a timer is fine where it has a grounded purpose (a pace cue, a movement game,
   classroom management); none without one.

## Science

1. **K to 2 meet three times a week** (Cory, 2026-11-14): kindergarten, grade 1 and grade 2 frames move to three
   meetings a week, days kept. Edit the frame's Days bullet; put the frames.csv change (per_week 3, and weeks if it
   follows) under "For the structure pass".
2. **Grade 2's mid-year check moves from week 17 to week 20** (Cory, 2026-11-14): frame calendar pin and days.csv.
3. **Grade 8 unit 2 reteach** (expert finding 1): the response runs inside days 28 and 32, as grade 7's day 70 does,
   logged as an exception to the one-lesson reteach. No base day is condensed.
4. **Grade 8 frame lines 140 and 143 are stale** (physics read, item 6): fix them in the grade 8 frame.
5. **Math leans in science** (sequence-write.md rule 2, "Math leans in other subjects"): retrieval by default;
   chemistry's two math readiness checks (days 41 and 130) stay. Physics: an Algebra I row is retrieval where Algebra
   II (same year) has already checked or used it, and a readiness check where physics uses it first; the calendar
   (data/plans/calendar.csv, math's days in data/plans/algebra-ii/days.csv) decides.
6. One readiness method across the band, course-level checks draw new cases, one source-map layout (above).

## ELA

1. **Frames**: grade 1, 2, 3, 4 and 5 readiness wording follows the counted rule. Kindergarten's frame gets one line:
   a foundations row owned in one unit and finished in a later one is continued, not re-checked for readiness.
2. **Grade 1** pourquoi tales cite Module 2, unit 1.
3. **Grade 3** makes g3-u1-06 and g3-u4-02 anchors (evens the literary to informational split).
4. **One root and affix list**, grades 3 to 8, then one word-family list for 9 to 12 (academic and discipline Greek and
   Latin roots, new each year): grade 3 affixes, grade 4 roots, grade 5 on new roots only, earlier ones retrieved (no
   reteach weeks), 6 to 8 new roots only (graph is not taught a third time), word parts spread over a unit, never one
   day. Fit your course's days to it; the list itself goes into data/progressions/ela.csv in the structure pass, so
   put your course's roots and affixes, exact, under "For the structure pass".
5. **Course-level checks**: grades 4 and 5 check 2 takes a form the unit just before did not (grade 4 informational,
   grade 5 narrative or research). Grades 6 to 8: every course-level check rewritten to Collect once (a new topic and a
   form the last two weeks did not give). Grade 9 day 158 reuses day 150's W.9-10.1 record. Where a frame drives a
   repeated check (grade 10 check 2, grade 11 check 3's narrative), edit the frame too. Grade 12 check 2 uses a form
   already taught (argument or analysis); the informative essay moves to check 3, after unit 6 teaches W.11-12.2.
6. **Anchor balance** counts anchors only (not paired or short reads), per year, one method for the band; a poem
   cluster or a paired set read as one anchor counts once; each year stays at 45 to 65 percent informational. Grade 12
   (76.5) swaps anchors toward literary.
7. **Grade 6 novella**: the frame's "climbs" claim is about demand, not length. Check its measured demand against grade
   5's novel; pick a longer or harder one only if demand does not climb.
8. **Grade 8 unit 5** talk audience: another class in the school, families invited where the school allows.
   **Grade 12 unit 8** panels: student panels in rotation plus the teacher as lead judge, another class or staff as
   audience where the school allows.
9. **One sustained literary-analysis piece per grade**, 6 to 8.
10. **Grade 8 RL.8.9**: unit 4 stays with myths and folk tales; replace the frame's "open with Cory (progression
    stitch, item 11)" lines (unit 4 row and For the lead item 6) with the ruling (Every subject, 6). Grade 10 day 86
    (Paradise Lost) and grade 11's Winthrop sermon stand, read as literature and as a seminal US document.
11. **The course text record** (one per course, the frame's "Candidate: the text record" cells): file it in the fix pass
    as a section of the scope and sequence.

## Math

1. **Frames**: grades 1, 2 and 3 "readiness" wording becomes retrieval where the counted rule says so. Review units
   drop "no assessment": a review unit may hold one embedded observation that reuses no record from the last ten days.
   Grade 1 frame unit 8 is 10 days (match days.csv and the frame). No tilde codes in frames.
2. **Full performance and fluency** (sequence-write.md End days): an end day holds at most one extended task plus short
   items; every year-end check samples each fluency standard directly, as a short independent station with no supplied
   work. Grade 2's year-end check asks 2.NBT.B.5 directly. Algebra I's day 158 gets a direct fluency station.
3. **Focus** is counted one way and stated once in each scope: minutes on major-cluster codes over instructional
   minutes, assessment and respond days excluded. Grade 8's 65.25 is recounted. Grade 4 states its minutes on major
   work (at the 65 percent line).
4. **Earlier-grade retrievals** carry the row id in the skills column.
5. **High school**: checks reuse any record from the last ten days. End-of-unit assessments name the part of each begun
   code they sample; begun codes owned later are checked by their owner, and Algebra I's year-end check samples the
   main ones it starts (F-IF.B.4, F-BF.A.1a, F-LE.A.2). Algebra II drops its completing-the-square readiness check
   (Geometry teaches and assesses it).
6. **Science leans on math**: where a science course's scope leans on a row your course owns, nothing changes in your
   course; the science fixers decide their treatment from your days.
7. **Copy rates** from the reads: grade 1 copied most base purposes (rewrite them all); grade 3 5.5 percent; grade 4
   under 1; others near 0. Every course checks its own.

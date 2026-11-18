# Expert read: social-studies-kindergarten unit 2, days 11 to 19 (kindergarten probe, 2026-11-18)

Unit 2, "Doing our part. How can each of us help our class?" One reader, whole unit, in order, no cheap read. Judged as docs/pipeline/briefs/expert-day.md says, against docs/courses/social-studies-kindergarten/DEFAULTS.md (20 to 30 minute days, prose cap 15 words a minute, student page pictures and boxes at 60 words or fewer and 18pt, spoken exits with picture cards, a rotating six heard each day, at home 15 to 30 minutes).

## What I read

- Rules and measures: docs/agents/EXPERT.md, docs/pipeline/briefs/expert-day.md, docs/pipeline/PROBE-GUARD.md, docs/courses/LESSON-DAY.md, docs/GLOSSARY.md, docs/agents/lenses/social-studies.md, the course DEFAULTS.md.
- Plans: unit plan s02.md and section plans u02-1 to u02-4 (docs/courses/social-studies-kindergarten).
- Days: courses/social-studies-kindergarten/u02-1/d011, d012; u02-2/d013, d014; u02-3/d015, d016; u02-4/d017, d018, d019; and u01-3/d010 for the handoff.
- Shared pieces the days call: Job Left Unfinished, job cards, paintbrush helper card, sorting cards, paper-box and cushion puppets, class problem-spot cards, count-plan-step cards, The Paper Workshop, spare apron card, class book pictures, The Lion and the Mouse, The Puppet Basket, rhythm sticks, record sheet, family note, the 2.1 and 2.4 openers, and the u01-2 charter pieces.
- Data: data/plans/social-studies-kindergarten (days, items, wrongs, errors, handbacks, materials).
- Built pages in build/lessons/social-studies-kindergarten/u02-N: teacher, student, student-large, key, display and home HTML for the days, and student PDFs for d011, d015, d017, d019.
- Prior probe reads, for the repeat tag only: docs/reviews/probe-social-studies-2026-11-15.md, probe-social-studies-2-2026-11-15.md, and defects.csv.

## Day 10 handoff

Holds. Day 10's Tomorrow line names day 11 and the charter, and d011 retrieves the charter on the wall with the plant and jug set out. Weak points, all small: d011 has no branch for "many missed day 10's exit"; the talk rules day 10 mentions are not retrieved on day 11; s02.md still says day 10 has no Tomorrow line (stale, finding 26).

## Verdict per day

- Day 11: sound content and a good unfinished-job story, but 429 teacher words against a 375 cap.
- Day 12: sound idea (real jobs, finished means done), but 447 words against 375, and the exit and picture-page chain cannot work as written.
- Day 13: right ideas about agreeing before voting, but overloaded at 448 of 450 words, and day 14 contradicts it on voting.
- Day 14: works as a lesson, but hard-codes the outcome of the class's own choice and sits at the cap.
- Day 15: strong read-aloud on making versus following; the exit's "six" is ambiguous and has no whole-class mark.
- Day 16: good handling of the fable; the exit asks four circles in three minutes and repeats the same story shape day 19 uses.
- Day 17: the judging idea is good, but the time per child and the reserved sketch are off.
- Day 18: the assessment instrument does not exist as built, the scenes cannot show which actor a child means, captions leak answers, and the home view cannot be answered.
- Day 19: sensible plan, but ten error letters feed two groups with bare letters and the student page prints a teacher note.

## Findings (most serious first)

1. [d013 to d017 section 2.1 to 2.4, Tomorrow and repair lines] Repair slots promised ("up to 2 or 5 more minutes") sit on days already planned at 30 minutes, so any repair breaks the 30 minute limit; handbacks.csv says 5 where the day says 2, and d017 says "stays under 30" while holding 3 spare | a teacher who repairs runs over, or skips the repair and the next day builds on a gap | give each repair a fixed slot inside the day (name the minutes it replaces) or route it to that day's group of six, and make handbacks.csv match the day text | origin=unit | repeat=yes
2. [d018 Teaching and Exit] The response-row instrument (seven rows of scene thumbnails, materials.csv "response rows") does not exist; the fallback has the teacher hand-draw 42 scenes per child, and "record each mark before resetting" conflicts with "collect the rows"; seven prompts in 8 minutes invites copying | the day's assessment cannot be run, so items 1 to 7 are unscored in practice | build the response-row sheet (7 rows, printed thumbnails, one token per row, a name line) and state one rule: collect, then record | origin=unit | repeat=new
3. [d018 Puppet Basket scene 1] Scene 1 holds two actors (Lena in charge, Rae caring), so a thumbnail cannot show which actor the child means | a correct child and a wrong child can mark the same picture | split scene 1 into two thumbnails, or tell the child to point at the character, and key it that way | origin=unit | repeat=new
4. [d018 captions] Captions leak answers ("Now the turns are equal", "They agree") | the exit measures reading the caption, not judging | caption with what happens only; keep the judgement words out of the picture text | origin=day | repeat=yes
5. [d018 home page] The home view asks about Lena, who is never in the summary told to the parent, and teacher-addressed stems print for the parent | the parent cannot answer and sees instructions meant for the teacher | tell Lena's part in the home summary and rewrite the stems to speak to the parent | origin=unit | repeat=yes
6. [d011, d012, d013, d017, d018, d019 display pages] Kindergarten display pages show answers, wrong answers and teacher notes: d011 "Tuli watered it, so it is done"; d012 the answer text; d013 "I'm picking" and "Tell the child the vote only named a plant"; d017 a bare "it did not help"; d018 "Answers. Mark your own in pen... 1. Read by your teacher." and the item 6 model answer; d019 "She is biggest" | a wall display shows the children the answer or the teacher's script | display pages for K carry pictures and the prompt only; move answers and notes to the key | origin=template | repeat=yes
7. [d011 to d019 student pages] Body prints at 14pt (18pt only in student-large), answer boxes 0.9in and 0.5in, pages mostly empty, and word labels have no picture cue | five-year-olds cannot find or fill the boxes, and the default page is not the large one | make 18pt the K default, boxes 1.5in or more with a picture cue on every label | origin=template | repeat=new
8. [d019 student page] The page prints "Scored from the work you handed in. Write nothing here." under a draw box | a draw box with an instruction not to write, in words a five-year-old cannot read, is a trap | remove the box and the line, or draw the box and say aloud what it is for | origin=template | repeat=new
9. [d011 and d012 teacher page, whole] d011 is 429 words and d012 is 447, both against the 375 cap for a 25-minute day (15 words a minute) | the days fail the prose gate and cannot be built | cut the duplicate phrases without changing any step. d011 to about 373: Before class "Keep Our Class Charter and the talk rules on the wall. Set the plant and jug out. Choose today's six, children not yet heard."; Retrieval "Ask: ... Listen at five pairs; note the words (s02-R11, no score). Count thumbs up for 'I can say why'. A child may pass. If many have no reason, two puppets act one rule kept, then not."; Hook "Read Job Left Unfinished, pages 1 to 7."; Teaching first "Teach job and responsible with the pictures." (drop "Anyone may have any job."); Pairs "draws the finished look."; Exit "Show the paintbrush card: ... Ask the six: 'Who counts on this job?' Mark s02-X11."; Tomorrow "If many gave error A (s02-X11), set the two side by side first."; Words and supports drop the "Frame: ___ counts on it." sentence; Shorter or longer "Longer: a second person who counts." d012 to about 375 (373 if "(the six)" is dropped in the exit): Warm-up "Draw day 11's corner finished."; Before class drop "Choose today's six."; Worked example drop the "if many gave error A" sentence; Take a job "Model the door holder with a puppet on a stool" and drop "No job belongs to a boy or a girl."; Do the job "Watch the six for the finishing step and for asking before taking; note it on their picture pages. Early finishers draw their job and who counts on it; write their words." and drop "It shows how our charter rule looks and sounds."; Exit "one partner holding two cards ... Watch three pairs (the six)" and drop the "For H, practise" sentence; Our Jobs Chart and Tomorrow trimmed as in the scratch edit lists. Both counts were checked with lesson.words on the teacher page without At home. A tall order at 25 minutes remains for d012; if the cut feels thin the clean fix is a 30 minute day with a 450 cap | origin=day | repeat=yes
10. [d012 Do the job and picture page] Only early finishers draw on the picture page, but the scoring chain needs a page per child, and the "evening next step on each child's page" cannot come from watching only the six | most children have no page and no next step, so days 13 to 15 private readings fail | every child draws one picture; the teacher writes next steps only for the six heard, and the other children's steps are written on the day they are heard | origin=unit | repeat=new
11. [d012 Exit] The exit has partners show how to finish and then three exit pictures, but the cards start in the envelope so nothing needs putting away, and the whole exit cannot fit 2 minutes | the mark rests on a thing that never happens | start with cards out on the table and keep one action: put away, ask first, then point | origin=day | repeat=new
12. [d012 Take a job] Only 3 job cards exist but 6 job kinds are needed, with no finishing pictures for the extra three | children have no card to hold up for "finished" | add the three cards and one finished picture for each, or cut to three jobs and rotate | origin=unit | repeat=new
13. [d013 and d014 voting] Day 13 teaches that when children agree no vote is needed, but day 14 votes even after agreement; "two towers" versus "a choice tower" is unclear after the revision | children are taught a rule and then watch it ignored | settle one rule across both days: vote only when the class does not agree, and say so in d014's opening line | origin=unit | repeat=new
14. [d014, d017, the J example] "bag" or "basket" and "the basket moved" are hard-coded though the class may pick the block corner | if the class picks another place, every later line is wrong | write the place as a slot ("the place the class chose") and name the bag case as one example | origin=section | repeat=new
15. [d014 to d018] The constants "fifteen" and "six" assume a class of 30; d018's "fifteen not heard on day 17" leaves only 10 in a class of 25 | the rotation breaks in a smaller or larger class | state the rule (a sixth of the class a day; those not heard on 17) not the number | origin=unit | repeat=new
16. [d013 to d017, item 1 evidence] Item 1 needs two dated job observations per child on days 13 to 17, but only d015 says whom to watch, and the record sheet has no dated-attempt columns | the teacher cannot see which child has which attempt | add two dated cells per child to the sheet and name the watch group on each of the five days | origin=unit | repeat=yes
17. [record sheet End 5] The End 5 look-fors are procedure, not child behaviour, and cover five qualities with three cells | the sheet cannot hold what it is meant to record | rewrite as three child behaviours (waits, asks, finishes) and give each a cell | origin=unit | repeat=yes
18. [d015 Exit] Who "the six" are is ambiguous (twelve?), and there is no whole-class mark, unlike days 11, 13 and 14 | the exit is heard by an unclear group and the class gets no response | say "today's six" and have all children point to the scene card as on day 14 | origin=day | repeat=new
19. [d016 Exit and d019] The d016 exit asks four circles in 3 minutes, and the Class Book story is the same shape as Rhythm Sticks on d019 | the second use is recognisable and the exit is a rush | ask two circles on d016, and give d019 a story with a different shape | origin=unit | repeat=yes
20. [d019 Teaching and groups] Ten error letters feed two groups, the group list uses bare letters (which trips the gate note), and pairs have no work on their own gap | the teacher cannot tell which child gets which help | name each group by the picture in plain words, put a letter-free label on each, and give pairs one task from their own gap | origin=section | repeat=yes
21. [d017 and d018 timing] Four questions per child in 40 seconds on d017, and 25 next steps read in 3 minutes on d018 | the pace is faster than a five-year-old can answer | ask two questions a child, or read next steps to the group of six only | origin=section | repeat=new
22. [d017 reserved sketch] The reserved sketch needs a different viewpoint before unit 3 teaches position words, is teacher-drawn, and has no fixed key | the teacher's own drawing becomes the answer and the viewpoint is unteachable | fix a drawing from a named spot (the door) with a key that says what shows | origin=unit | repeat=new
23. [d014 Exit] Exit card rows are told apart by colour (green and blue), which fails in black and white; the puppet-theatre and curtain setting recurs on day 18 | children who cannot tell the colours, or a black and white print, cannot answer; the same setting twice cheapens day 18 | mark rows with a shape as well as colour; change day 18's setting | origin=day | repeat=new
24. [d011 home, d011 student page, several days] d011 at home says the jug is "in the doorway" while the story says the walkway; most days lack the "read the student page aloud" line (only d015 and d016 have it); the d011 page asks "Who counts on it" but the day only draws the finished look | a parent reads wrong words, and a child cannot read the page | fix the doorway line; add the read-aloud line to every K day; drop the question or teach it | origin=day | repeat=new
25. [d013 whole day] d013 is overloaded (two votes, a story and an exit in 30 minutes at 448 of 450 words), and the exit mark is given away by the story | the day has no slack and the exit measures hearing the story | move the second vote to d014 (see 13), and make the exit about a new problem | origin=day | repeat=yes
26. [s02.md, opener 2.4, d010 and d011, s02-X11] s02.md says no Tomorrow line exists for day 10 (stale); opener 2.4 says a child "has read written feedback"; d010's Tomorrow says "charter and talk rules" but d011 retrieves only the charter; s02-X11 "The teacher will do it" is filed as error A | the plan text and the day text disagree | correct each line in place (stale sentence out, "has heard written feedback", retrieve the talk rules or drop them from d010, move X11 to its own letter) | origin=unit | repeat=new

## Gate check against five-year-olds

No day obeys a gate in a way that is wrong for five-year-olds beyond what findings 6, 7, 8 and 20 already name (display pages carrying answers, 14pt default pages, a "write nothing" line, bare letters). Those four are origin=template and are counted above.

## Counts

26 findings. By origin: day 7, section 3, unit 13, scope 0, frame 0, template 3. By repeat: yes 10, new 16.

## Fix (all 26 findings, 2026-11-18)

1. FIXED: each repair runs inside the opening part's own minutes (d013 3, d014 2, d015 3, d016 3, d017 3); handbacks.csv and section plans agree.
2. FIXED: new cards-response-rows (seven rows, seven thumbnails, a token a row); rule is collect the sheets, then record.
3. FIXED: Puppet Basket scene 1 split into Lena and Rae scenes; seven scenes, key renumbered.
4. FIXED: captions say only what happens.
5. FIXED: Lena added to the d018 home summary; item stems E1 to E5 now read as questions to ask aloud.
6. LEAD: K display view carries pictures and the prompt only; answers and notes go to the key (ledger row corrected to kind classroom).
7. LEAD: 18pt default for K student pages, boxes 1.5in or more, a picture cue on every label.
8. LEAD: template must not print the write-nothing line on K pages; removed from d019 (its exit is spoken).
9. FIXED: d011 375 words, d012 373.
10. FIXED: every child draws on d012; next steps for the six that evening, the rest on the day each is heard.
11. FIXED: d012 exit starts with cards on the table, one action.
12. FIXED: d012 and u02-1.md use the three taught job cards with copies.
13. FIXED: d014 opens with "we vote only when we still do not agree", counts hands if all accept the change, votes only if not; u02-2.md agrees.
14. FIXED: error J now "We picked it, so we are done"; d017 names the class's own first step, not the basket.
15. FIXED for fifteen (half the class on d017, those not heard on d018). The rotating six stays: it is the course's daily group.
16. FIXED: record.md adds dated job cells J1 and J2 and names the six as the watch group on days 13 to 17.
17. FIXED: s02-E4 steps are three child marks, one cell each in record.md.
18. FIXED: d015 exit says today's six and all children point to the scene card.
19. FIXED: d016 asks two circles each. Same-shape story on d019 REJECTED: it is a transfer try in a new setting and cast.
20. FIXED: d019 groups carry plain labels; pairs take the picture card for their own gap.
21. FIXED: d017 two questions a child; d018 next steps read to the six only.
22. FIXED: reserved sketch drawn from the door with a stated clue and obstacle; u02-4.md agrees.
23. FIXED: count card rows differ by shape as well as shade; setting changed to a reading corner.
24. FIXED: doorway changed to walkway on d011. LEAD: template should print the read-aloud line on K student pages (no room under the cap).
25. REJECTED: the exit already uses a new problem (Cushions); the load was words, relieved by 1.
26. FIXED: stale s02.md sentence corrected, opener 2.4 "heard", d010 Tomorrow retrieves the charter only; X11 stays error A.

Count: 26 findings: 22 FIXED (15 and 19 each with a rejected part, 24 with a LEAD note), 3 LEAD (6, 7, 8), 1 REJECTED (25).

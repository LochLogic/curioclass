# Scope and sequence: Social and Emotional Learning, Grades 3 to 5

Course `social-and-emotional-learning-grades-3-to-5`, one band course over three school years, 192 sessions of 30
minutes, two a week, 64 a year. Written 2026-11-26 from docs/courses/social-and-emotional-learning-grades-3-to-5/frame.md
(every frame "For the lead" item settled or done). The days are data/plans/social-and-emotional-learning-grades-3-to-5/days.csv,
written by build/scope-writes/scratch/social-and-emotional-learning-grades-3-to-5/make_days.py.

## Calendar and school days

- Year 1 (course days 1 to 64) teaches the grade 3 rows (g3-*), year 2 (days 65 to 128) the grade 4 rows (g4-*), year
  3 (days 129 to 192) the grade 5 rows (g5-*). Grades 3 and 4 list the begun form of each code (`~CASEL...`); grade 5
  is the owner year and lists the plain codes, with the three AASL ids library places in SEL (V.D.1 on
  g5-sm-stay-on-task, V.D.2 on g5-sa-skills-grow, III.D.2 on g5-rel-teamwork).
- `school_day` counts across the whole band (lead rule 2026-11-26). For session s of year y (s = 1 to 64, y = 1 to 3):
  school_day = (y - 1) * 160 + 5 * ((s - 1) // 2) + (2 if s is odd else 4), a Tuesday and Thursday pattern. Week within
  the year = ((school_day - 1) mod 160) // 5 + 1. The last session of each year falls in week 32.
- SEL is a classroom teacher's course in K to 5 and counts in the stagger (CALENDAR.md rule 1). Its check weeks are the
  frame's: grade 3 weeks 10 and 26, grade 4 weeks 15 and 26, grade 5 weeks 15 and 26, each with its Respond day in the
  same or the next week. Health 3 to 5's check weeks (15 and 29, 14 and 29, 14 and 28) do not meet them.

## How every unit runs

- **Openings.** Every session opens with the calm-down routine. Each group's Understanding day then gives one retrieval
  item per sub-skill on its prior-grade form (g2, g3 or g4, listed in `retrieves`), a scenario item at the earlier
  depth; a miss gets the earlier step modeled again. Fluency and Application days give a three-minute return to an
  earlier same-year skill with its card. There is no readiness day: every row assumes the prior-year row, so every
  unit opens with retrieval (rule 2).
- **Kinds.** Understanding holds the hook (each unit's first day, on its compelling question), the cards and the
  group's two or three sub-skills; Fluency is partner rehearsal with the card held; Application uses an unseen card
  with the card withdrawn. Products (plan cards, webs, weighed choices, planners) get a written note on their
  Application day and are revised before the Check; nothing is scored the day it is first made. No Fluency goal
  drafts, edits or introduces anything.
- **End-of-unit evidence.** The last Application holds the first half of the watched rehearsal (about half the pairs,
  two minutes each). On the Check, page and rehearsal run side by side: the unseen page (read aloud on request,
  answered in a sentence or by circling, about 15 minutes) while the teacher watches the pairs not yet seen; any left
  go first in the Respond opening. Every Check note maps each code to a page item, the rehearsal, or a revised product
  seen earlier in the unit. Feelings in every item are a character's. Class sheet "seen" or "not yet" by step; the
  sheet is thrown away after the Respond day (collect once; class size 30).
- **Respond.** At most four groups from the sheet's "not yet" cells, reteach then rehearse with the step card; the rest
  rehearse in pairs. Each Respond day sends the unit's family note. Each unit's first Understanding day names the
  disclosure line and its carry-out cue; the core link sits on the day that leans on it.
- **Safety and care.** A partner never plays an unkind, pushing or abusive part: the teacher or a card plays the push,
  the tease, the exclusion and the hurt friend's words, and a partner coaches with the step card. No real friends,
  families or cultures are asked about by name; webs, logs and SA7 plans of a student's own stay private. Disclosure
  follows health's steps (the school's reporting route and the counselor). No clinical words. Body tools are done
  beside desks with room to reach, with no spiritual framing. Supplies and safe use of space are named in each day's
  note.
- **Settled cases** do not repeat within the band: the three cultural cases (units 3, 9, 17) come from three different
  places, and the one settled history case (Brown v. Board, unit 15) appears once.

## The shared cards (SEL STANDARD section 7, the grades 3 to 5 form)

Quoted as the frame grows STANDARD section 7's cards for grades 3 to 5 (section 7 itself gives a grades 3 to 5 form only for the I-statement), so a child meets one card in SEL, health and PE:
- **Talk turn card:** "listen, say back, ask a question, add your idea" (day 33; health uses the first three steps as
  its listening steps).
- **Calm-down steps:** "stop, breathe, name it, choose", with three body tools (slow breaths, a stretch, counting back
  from ten) (day 4).
- **I-statement:** "I feel ___ when ___ because ___. I need ___." (day 33).
- **Goal steps card:** "goal, steps, block and plan, check" (day 54).
- **Refusal steps:** "stop and think, say no clearly, give a reason or none, offer something else or walk away; if it
  comes again: say it, say it again, move away, tell" (day 43), health's words; the second push is rehearsed against
  the teacher's or card's repeat on days 43, 51, 112, 114, 165 and 167.
- Stop-think-choose (day 7) and the problem size meter (tiny, small, medium, big; day 37) are SEL's own and grow the
  same way.

## Year 1: grade 3 (course days 1 to 64)

### Unit 1. Think, feel, do

Course days 1 to 11, weeks 1 to 6. Three groups: spot it and name it (days 1 to 3), calm it (days 4 to 6), choose with
care (days 7 to 9). The arc runs from naming a feeling and its thought, to calming before acting, to choosing with the
four-step stop-think-choose, because each card is used by the next; the three cards serve units 2, 3 and 5. Retrieval
from the grade 2 rows opens each group; the leave-out bridge teaches the grade 2 card forms in the first ten minutes
where the class had no SEL K to 2. End-of-unit check day 10 (unseen scene page plus the four calm-down steps rehearsed),
Respond day 11. Candidate cells settled, no day cost: "test it" only on characters (day 1); one plan card shared with
health 3 to 5's calm tools (day 4).

### Unit 2. Who I am and what I bring

Course days 12 to 19, weeks 6 to 9, then the mid-year check. Two groups with two Fluency days each: who I am (days 12
to 15), what I stand for and bring (days 16 to 19). Identity and strengths come before honesty and praise because the
shout-out names a strength. The private interest log runs days 12 to 19. End-of-unit evidence is the grade 3 mid-year
check on day 20 (week 10), Respond day 21 (week 11). Candidate cells settled, no day cost: model webs checked for range
(day 12); the log's look-for is "steps followed" only (day 16).

### Unit 3. Walking in their shoes

Course days 22 to 32, weeks 11 to 16. Three groups: reading others (22 to 24), checking my guess (25 to 27), thanks and
systems (28 to 30). Reading clues comes first because the snap-judgment check and the shoes switch use them; systems
come last as the widest view. Check day 31, Respond day 32. Candidate cells settled, no day cost: the teacher-acted
scenes scripted in the unit plan (day 22); the partner's game way from a cited source the sensitivity agent reads, not
one of PE's, the arts' or K to 2's picks (day 25).

### Unit 4. When friends disagree

Course days 33 to 42, weeks 17 to 21. Two groups with two Fluency days each: talk it out and repair (33 to 36), help,
places and leading (37 to 40). Talk turn, then I-statement, then repair, because each uses the one before; it follows
unit 3 because talking it out uses reading the other side. Health grade 3 unit 4 teaches its I-statement in the same
weeks with the same words. Check day 41, Respond day 42. Candidate settled by the 2026-11-25 fix pass: one I-statement
and listening wording with health (day 33).

### Unit 5. Saying no, choosing well

Course days 43 to 51, weeks 22 to 26, then the year-end check. Three groups: think ahead and hold my ground (43 to 45),
questions, facts and fair rules (46 to 48), solve it and see who it touches (49 to 51). Refusal and upstanding use the
I-statement and meter from unit 4; the scaled graph leans on math grade 3 unit 1, taught before. End-of-unit evidence is
the grade 3 year-end check on day 52 (week 26), Respond day 53 (week 27). Candidate cells settled, no day cost: refusal
cases checked against health's refusal card (day 43); the coat-hook test runs one week and is checked on day 51.

### Unit 6. Goals that stretch me

Course days 54 to 64, weeks 27 to 32. Three groups: plan the stretch (54 to 56), our class plan (57 to 59), step up
together (60 to 62). Last in the year because it uses every earlier card (goal steps, talk turn, stop-think-choose) and
hands the grade 3 rows on to grade 4. The three-week goal and practice record run days 54 to 63. Check day 63, Respond
day 64. Candidate cells settled, no day cost: the class vote is group 2's Application so its two weeks end before the
Check (day 59); the welcome kit from paper the class has (day 60).

## Year 2: grade 4 (course days 65 to 128)

### Unit 7. Team rules we make

Course days 65 to 74, weeks 1 to 5. Two groups with two Fluency days each: our working agreement (65 to 68), fair and
honest teams (69 to 72). First in the year because every later team task runs on the agreement, and PE 3 to 5 unit 11
opens with it. Check day 73, Respond day 74. Candidate settled, no day cost: one building session only, so the agreement
is the point (day 68).

### Unit 8. Plans and steps

Course days 75 to 84, weeks 6 to 10. Two groups with two Fluency days each: a shared plan (75 to 78), two paths and
focus (79 to 82). Day 79's opening carries the grade 3 if-then plan item (moved from the mid-year check by the frame).
The two-week team project, a class guide to our routines for a substitute teacher day (reusing unit 7's substitute-day case, so it does not repeat grade 3's welcome kit), runs days 75 to 82. Check day 83, Respond day 84. Candidate cells settled, no day cost: the
project ends before the Check (day 75); the try-again step worded as in units 6 and 14 (day 79).

### Unit 9. Many ways to be

Course days 85 to 92, weeks 11 to 14, then the mid-year check. Two groups with two Fluency days each: webs and strengths
(85 to 88), two views (89 to 92). End-of-unit evidence is the grade 4 mid-year check on day 93 (week 15), Respond day 94
(week 15). Candidate settled, no day cost: the shared-work custom from a cited source, a different place from units 3
and 17 (day 89).

### Unit 10. Feelings at work

Course days 95 to 105, weeks 16 to 21. Three groups: one event, two people (95 to 97), calm and care for a teammate (98
to 100), thanks and systems (101 to 103). Health grade 4 unit 11 shows one thing affecting people differently in the
same weeks. Check day 104 (week 20), Respond day 105. Candidate settled, no day cost: the crossing-guard case written
for rural and city schools (day 101).

### Unit 11. Leading and following

Course days 106 to 114, weeks 21 to 25, then the year-end check. Three groups: leading the team (106 to 108), repair
and settle (109 to 111), hold the no and speak up (112 to 114). Health grade 4 unit 12 runs refusal and speak-up on
health topics in the same weeks and opens with this card. End-of-unit evidence is the grade 4 year-end check on day 115
(week 26), Respond day 116. Candidate settled, no day cost: the class improvement chosen so the election and first step
fit day 108.

### Unit 12. Thinking it through

Course days 117 to 128, weeks 27 to 32. Three groups, the second with two Application sessions: questions and claims
(117 to 119), solve and map (120 to 123, day 122 the moved session that gathers two groups' views), interests and growth
(124 to 126). The chosen solution's one-week test starts on day 123 and is checked on day 126. Check day 127, Respond day 128, handing the grade 4 rows on. Candidate settled, no day cost: the
classroom-only version of the visit uses written questions (day 122).

## Year 3: grade 5 (course days 129 to 192)

### Unit 13. Changes ahead

Course days 129 to 138, weeks 1 to 5. Two groups with two Fluency days each: naming the change (129 to 132), steady
through change (133 to 136). Grade 5 adds the pressure of change to each row. Health grade 5 unit 15 runs in the same
weeks and names these calm tools without teaching them. Check day 137, Respond day 138. Candidate settled, no day cost:
the timed practice is two tools, two minutes each on a sand timer, a pace cue (day 133).

### Unit 14. What drives me

Course days 139 to 148, weeks 6 to 10. Two groups with two Fluency days each: goals and plans (139 to 142), purpose and
setbacks (143 to 146). Teaches AASL.V.D.1 (day 139) and V.D.2 (day 143). Check day 147, Respond day 148. Candidate
settled, no day cost: the backward plan sized so its slip and recovery fall inside the unit (day 139).

### Unit 15. Who shapes what we do

Course days 149 to 156, weeks 11 to 14, then the mid-year check. Two groups with two Fluency days each: systems and
crowds (149 to 152), checking against the crowd and the past (153 to 156). Day 149's opening carries the grade 4 source
check item (moved from the mid-year check by the frame). Counts only, no percents. End-of-unit evidence is the grade 5
mid-year check on day 157 (week 15), Respond day 158. Candidate settled, no day cost: the Brown v. Board page read
against the National Archives page, the National Park Service's five-cases and Briggs v. Elliott pages (the families' cost: job loss and refused loans only) and social studies grade 5 unit 9's sources, the Brown Foundation page a secondary link only (day 153).

### Unit 16. Friends through change

Course days 159 to 169, weeks 16 to 21. Three groups: a friend's side (159 to 161), talking it through (162 to 164),
help and hold (165 to 167). Health grade 5 unit 18 runs care and conflict in the same weeks; each stands alone. Check
day 168 (week 20), Respond day 169. Candidate settled, no day cost: the step-back case worded about leaving someone out
(day 162).

### Unit 17. My voice, our group

Course days 170 to 179, weeks 21 to 26, then the year-end check. Three groups, the second with two Application
sessions: propose and start (170 to 172), keep everyone in (173 to 176, day 175 the moved session of improvement work),
speak up and thank (177 to 179). Teaches AASL.III.D.2 (day 173). End-of-unit evidence is the grade 5 year-end check on
day 180 (week 26), Respond day 181 (week 27). Candidate cells settled, no day cost: the classroom-only version where the
principal or council cannot host the proposal (day 170); the habits case from a cited source, a third place (day 173).

### Unit 18. Choices with reach

Course days 182 to 192, weeks 27 to 32. Three groups: ask and predict (182 to 184), solve and map (185 to 187, day 187
the school-grounds pick-up), who I take with me (188 to 190). Last because it looks ahead to grade 6. Check day 191,
Respond day 192. Candidate settled, no day cost: the class acts only on school grounds the teacher has checked; the park
part is planned on paper unless the school runs a trip under its field-trip policy (day 185).

## Course-level checks

Each check is the end-of-unit assessment of the unit it follows (sequence.py accepts a C Check on the day after a
unit's last day) and adds two written samples from earlier units on new cases, five page items at most, plus the
unit's watched rehearsal. Each is followed by a C Respond day.

| Day | Week | Check | Stands for | Samples on new cases |
|---|---|---|---|---|
| 20 | grade 3, 10 (Respond 11) | Grade 3 mid-year | Unit 2 | g3-sa-name-feelings (feeling and clue), g3-sm-big-feelings (the skipped step) |
| 52 | grade 3, 26 (Respond 27) | Grade 3 year-end | Unit 5 | g3-sa-snap-judgments, g3-rel-settle-disagreements |
| 93 | grade 4, 15 | Grade 4 mid-year | Unit 9 | g4-soc-fair-rules, g4-sa-i-can-try |
| 115 | grade 4, 26 | Grade 4 year-end | Unit 11 | g4-sa-feel-think-link, g4-soc-read-feelings |
| 157 | grade 5, 15 | Grade 5 mid-year | Unit 15 | g5-sa-feel-think-link, g5-sa-i-can-try |
| 180 | grade 5, 26 (Respond 27) | Grade 5 year-end | Unit 17 | g5-soc-read-feelings, g5-rel-settle-disagreements |

**Owned codes on the course-level checks (rule 3).** Grade 5 owns 43 codes. The two grade 5 checks sample 11:
Responsible Decision-Making.2, Social Awareness.6, Self-Awareness.6, Self-Awareness.5, Self-Awareness.7 (mid-year) and
Relationship Skills.9, Social Awareness.2, Relationship Skills.4, AASL.III.D.2, Social Awareness.4, Relationship Skills.5
(year-end). The other 32 are not sampled on a course-level check, for these reasons:
- The frame caps each check at its unit plus two samples and five page items, so a check cannot reach every unit.
- Units 13, 14 and 16 are checked at their own unit ends (days 137, 147, 168), every code mapped there: Self-Awareness.3,
  Self-Management.1, Self-Management.2, Social Awareness.7 (unit 13); Self-Management.3, Self-Management.4,
  Self-Management.5, Self-Awareness.8, Self-Awareness.9, AASL.V.D.1, AASL.V.D.2 (unit 14); Social Awareness.1, Social
  Awareness.3, Relationship Skills.1, Relationship Skills.2, Relationship Skills.6, Relationship Skills.8 (unit 16).
- Unit 18 falls after the year-end check and is checked on day 191: Responsible Decision-Making.1, .3, .4, .6, .7,
  Self-Awareness.1, .2, .4.
- Unit 15 and 17 rows evidenced through Application products and observation, mapped on their check notes: Social
  Awareness.8, Responsible Decision-Making.5 (unit 15); Self-Management.6, Self-Management.7, Relationship Skills.3,
  Relationship Skills.7, Social Awareness.5 (unit 17).

## Shorter path

**Short year (about 10 school days short).** Two sessions a week makes that about 4 sessions a year (lead rule
2026-11-26). Each year names four fold-in days, each a second Fluency or a Fluency whose rehearsal folds into the
Understanding day before it, saving 30 minutes. No Check, Respond, Application or owned part is cut, and the check
weeks hold.
- Grade 3: day 14 (unit 2), day 18 (unit 2), day 34 (unit 4), day 38 (unit 4): 120 minutes.
- Grade 4: day 67 (unit 7), day 77 (unit 8), day 102 (unit 10), day 125 (unit 12): 120 minutes.
- Grade 5: day 131 (unit 13), day 135 (unit 13), day 141 (unit 14), day 155 (unit 15): 120 minutes.
- Each folded task is repeated on the next Application (days 15, 19, 36, 40, 132, 136, 142, 156), so no assessed skill loses its only rehearsal.
- Total 12 sessions, 360 minutes, 192 sessions to 180.

**Once-a-week path (the frame's).** 32 sessions a year. Grade 3 units run 5, 6, 5, 6, 5, 5; grade 4 run 5, 5, 5, 6, 5,
6; grade 5 run 5, 5, 5, 6, 6, 5 sessions. A three-group unit in five sessions: Understanding and Fluency together for
each group (three sessions), one Application, then Check and Respond in one session. A two-group unit in six:
Understanding with the first rehearsal and the second rehearsal for each group (four sessions), one Application, Check
and Respond together; in five, one second rehearsal is dropped. A six-session three-group unit keeps one Fluency
session of its own. Every Check keeps its page and its watched rehearsal, so no assessed part is cut. Check weeks on
this path: grade 3 weeks 11 and 27, grade 4 weeks 15 and 26, grade 5 weeks 15 and 27.

**Leave-out units and the bridge.** Where a unit is left out, a later unit that uses its card models the card's
one-step form in its first ten minutes (the card named, its first step modeled once) and claims none of the left-out
unit's rows; day 1's bridge for a class without SEL K to 2 keeps the grade 2 forms, already one or two steps. Named on the days: day 1 (no SEL K to 2: the grade 2
card forms), day 12 (unit 1 left out: stop-think-choose), day 22 (unit 1: the strength scale and stop-think-choose),
day 33 (unit 1 left out: the calm-down steps), day 43 (unit 4 left out: the I-statement and meter; unit 1: stop-think-choose), day
60 (unit 4 left out: the talk turn card), day 65 (the grade 3 talk turn card), day 75 (unit 7 left out: a minimal
agreement; grade 3 unit 6 left out: the goal steps card), day 79 (grade 3 unit 6: the focus plan and its try-again step), day 95 (unit 1: the calm-down steps), day 98 (unit 3: the care steps), day 109 (unit 4: the I-statement and
talk turn card), day 112 (unit 5: refusal and upstander cards), day 188 (unit 2 or 9: the web item moved to the nearest
earlier year taught).

## Sources not loaded

These days lean on sources the unit plan reads first; none is loaded in the repository yet, and no source-map.csv is
written this run:
- The cited cultural sources for the partner's game way (day 25), the shared-work custom (day 89) and the teammates'
  habits (day 173), chosen at the unit plan and read by the sensitivity agent.
- The National Archives Brown v. Board page, and the National Park Service's Brown v. Board pages for the families' cost
  (https://www.nps.gov/brvb/learn/historyculture/fivecases.htm and
  https://www.nps.gov/brvb/learn/historyculture/socarolina.htm, opened by the expert read 2026-11-26); the Brown Foundation
  page is the foundation's own history, kept as a secondary link (day 153).
- An education association's guidance on families and cultures (days 12, 85, 188).
- The CPSC public playground safety handbook (December 29, 2015 edition, about playground equipment) for the grounds check,
  the school's own grounds policy as the pick-up guide, and one state's field-trip guidance (days 185, 187).

## For the lead

1. **Owned codes not on a course-level check (settled by the scope group read, 2026-11-26, finding 11).** The unit's own
   end-of-unit assessment is rule 3's named reason, and the cap stays (frame, Course-level checks); the line for
   STANDARD section 2 is the lead's. Kept as a record: 32 grade 5 codes are checked only at their own unit ends or through
   products and observation (listed under Course-level checks), because the frame caps each check at two samples. If
   rule 3 needs more, the fix is a frame change (a third sample on the year-end check, or a sixth page item), not a
   sequence change.
2. **Rule 2 counting tools skip SEL.** scripts/unit_skeleton.py's SUBJECTS list holds only social studies, math, ELA
   and science, so sequence.py prints no rule 2 notes for this course; retrieval was checked by hand (every
   Understanding day lists its prior-grade rows in `retrieves`).
3. **Once-a-week form for units 12 and 17.** The frame's six-session three-group form adds one Fluency session, but
   units 12 and 17 carry an extra Application (the moved sessions, days 122 and 175). This sequence follows the frame;
   the lead may prefer the six-session form keep the moved Application instead.

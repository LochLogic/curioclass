# Scope group read: social and emotional learning, K to 12 (2026-11-26)

The four SEL band scopes read side by side, under build/scope-writes/GROUP-READ.md. This read looks only at what no
single-course read could see; the four expert reads and their fix passes are not repeated.

## What I read

- AGENTS.md; docs/agents/EXPERT.md; docs/pipeline/briefs/sequence-read.md; build/scope-writes/AFTERCORE-BRIEF.md.
- docs/courses/sel/STANDARD.md in full (sections 2, 3, 5 and 7 above all); the four frames by section (Seams, Models
  carried, Days, Leave-out, Cross-subject, the Picked up and Handed on tables).
- The four scopes and days.csv files: social-and-emotional-learning-grades-k-to-2, -3-to-5, -6-to-8, -9-to-12. The
  CSVs were read with short Python scripts (scratchpad only): every progression row against the days that teach it,
  every row's `assumes` against the `retrieves` of the day that first models it, the frames' Picked up tables against
  the earlier band's unit numbers, the shared card wordings, case and project words by grade, and the per-unit
  carriers (disclosure route, carry-out cue, family note, core link).
- The four -fixes-2026-11-26 reports; docs/courses/CALENDAR.md (rules 1 to 4 and the check-week table);
  docs/agents/decisions/DESK-ANSWERS.md, the three 2026-11-26 entries (after-core frame fix-pass rules, after-core
  frame calls, after-core scope lead calls).
- Health and PE at the same bands, for the shared cards and leans: the card wordings in health K to 2, 3 to 5, 6 to 8,
  9 to 12 and PE 3 to 5 and 6 to 8 days.csv, and the health unit weeks behind SEL's lean claims.

## Findings

1. **The first day of a band handles the band before in three different ways, and 6 to 8's breaks the Desk rule.**
   SEL 6 to 8 day 1 carries `assess = readiness` on g5-rds-careful-thinking, g5-rel-ask-offer-help and g5-sm-set-goal,
   rows last used the year before (SEL 3 to 5 days 182 to 190, 165 to 167, 139 to 142). The 2026-11-26 after-core scope
   lead calls say a row last used the year before is a retrieval, never a readiness check, and that a read showing it
   wins over the frame. SEL 3 to 5 day 1 and SEL 9 to 12 day 1 follow that rule (retrieval of the grade 2 and grade 8
   rows). The 6 to 8 fix pass (expert 6) also made day 1 model all three grade 6 rows of group 1.1 while the grade 5 rows
   those three assume (g5-sm-plan-and-tidy, g5-sm-stay-on-task, g5-sa-i-can-try) are retrieved only on days 2, 3 and 4,
   after the new depth is taught. It is the only day in the 832 band days where a row is modeled before its assumed
   row is warmed. A fix made this worse. For a class that did not take the band before, the three scopes use three
   tools: 3 to 5 the leave-out bridge on day 1 (grade 2 card forms in the first ten minutes), 6 to 8 the readiness check
   plus a bridge on days 2 and 5, 9 to 12 a "Given:" item on day 1 (STANDARD 5.6 keeps "Given:" for a left-out unit).
   Why it matters: a grade 6 teacher marks a check the rule says is not owed, and the first new depth of the band lands
   cold. Fix: 6 to 8 day 1 `assess` blank, its opening (after the hook) one retrieval item in three parts on the three
   assumed grade 5 rows, `retrieves` filled, the readiness wording dropped from the note; days 2 to 4 keep their
   same-year spacing items. A class new to the band, in 6 to 8 and 9 to 12 alike, gets the 3 to 5 day 1 form: the
   earlier band's card forms in the first ten minutes as the bridge, claiming nothing. 6 to 8 frame Days bullet and
   Seams paragraph, and the 9 to 12 Readiness bullet and unit 1 candidate, reworded to match. **scope** (with frame
   wording in two frames).

2. **The bar part 9 carriers sit on the days in some bands and only in the frame in others.** Counted per unit from
   days.csv:
   - Carry-out cue and family activity: K to 2, 3 to 5 and 9 to 12 name them on the days (K to 2 cue on the unit's
     first day, family activity on its Respond day; 3 to 5 "each Respond day sends the unit's family note"). SEL 6 to 8
     names neither on any of its 192 days, and its scope never mentions the family note except the eighteen Spanish
     notes waiting on a translation read; the frame's unit cells have both.
   - Disclosure route (STANDARD 5.4, "each unit's teacher notes"): every unit in K to 2 (added by its fix pass) and 6
     to 8; in 3 to 5 no day of units 2, 6, 7, 8, 9, 12, 14, 15, 17, 18 names it (the scope says it once in "Safety and
     care"); in 9 to 12 no day of units 3, 5, 6, 7, 9, 10, 12, 15, 16, 18, 19, 21, 22.
   - Health unit named for a 6 to 12 unit that first teaches SM2 or RS6 (STANDARD section 3): named in every such unit
     but 6 to 8 unit 10 (day 99 says "health owns mental health", no unit) and 9 to 12 unit 8 (day 75).
   - Core link (bar item 9): K to 2 units 3, 6, 12, 16, 18 and 3 to 5 unit 5 name none on a day (the frames have one).
   - The 18-or-over rule (AGENTS.md): the 9 to 12 frame states it; the 9 to 12 scope does not, though grade 12 sends
     family notes (health 9 to 12's scope states it).
   Why it matters: a unit plan writer works from the days, so in 6 to 8 the family note and the cue are the easiest
   part of bar items 7 and 10 to lose, and a 3 to 5 or 9 to 12 unit can reach its sensitivity read with no disclosure
   line. Fix: the K to 2 pattern in every band: the cue on the unit's first day, the family activity on its Respond day
   (for units 3 and 6 of a year, the course-level Respond day), the disclosure line on the unit's first Understanding
   day, the health unit and the core link on the day that leans on them; one line in the 9 to 12 scope for students 18
   or over. Notes only. **scope**

3. **The refusal card loses its second push for six years, and SEL and health word the card differently.** STANDARD
   section 7 makes "say it again, move away, tell" the shared second push, and K to 2 teaches it (days 89, 161 to
   166). No day in SEL 3 to 5 or 6 to 8 uses it (3 to 5 refusal days 43, 51, 112, 114, 165, 167; 6 to 8 days 38, 40,
   76, 79, 145, 147 rehearse a card that ends at "walk away" or "a way out"), and 9 to 12 day 35 then teaches it as new,
   as section 7's 9 to 12 line says ("add ... the second push"). The 3 to 5 frame's Models carried row calls the K to 2
   card "two refusal steps". Beside SEL, health uses another wording: "a reason is optional" from grade 4 and "give a
   reason or none" on health 3 to 5 days 51 and 70, health 6 to 8 days 19 and 55 and health 9 to 12 day 46, while SEL 3
   to 5 says "give a reason" and SEL 6 to 8 and 9 to 12 use the options form (a plain no, a no with a reason, a way out).
   The Desk's "one set of card words" rule (2026-11-26 frame fix-pass rules) is not met. Why it matters: a pressure
   that comes back after the first no is the case the skill most needs, and a grade 4 child hears "give a reason" in
   SEL and "a reason is optional" in health in the same year. Fix: section 7 gives the refusal card in full per band:
   3 to 5 "stop and think, say no clearly, give a reason or none, offer something else or walk away; if it comes
   again: say it again, move away, tell"; 6 to 8 the three options with the same second push; 9 to 12 the options, the
   plan made ahead, the ally, with the second push carried (not added). Then the 3 to 5 and 6 to 8 refusal days above
   rehearse the second push against the teacher's or card's repeat, and 9 to 12 day 35 retrieves it. My pick on the
   reason: "a reason or none", health's wording, since a no needs no reason. **frame** (STANDARD section 7 and the
   frames' card cells; the day notes follow as scope work).

4. **SEL 3 to 5's leave-out bridges teach whole cards, not the one-step form.** STANDARD 5.6, the Desk leave-out
   rule (2026-11-26) and the K to 2, 6 to 8 and 9 to 12 days all say the bridge teaches the card's one-step form in ten
   minutes. The 3 to 5 frame's Leave-out bullet says "the card's grades 3 to 5 form", and its days do so: day 33 the
   four calm-down steps, day 43 the four-part I-statement, the meter and four-step stop-think-choose, day 60 the
   four-step talk turn card, day 75 a minimal agreement and the goal steps card (no 3 to 5 day uses the words "one-step
   form"). Why it matters: three four-step cards in ten minutes is a lesson, not a bridge, and it eats the session it
   sits in. Fix: frame Leave-out bullet and the bridge notes on days 12, 22, 33, 43, 60, 65, 75, 79, 95, 98, 109 and 112
   say "the one-step form" (the card named, its first step modeled once); day 1's no-K to 2 bridge keeps the grade 2
   forms, which are already one or two steps. **scope** (the frame bullet as frame wording).

5. **STANDARD section 7 has no grades 3 to 5 cards, so the band forms drift at the edges.** Section 7 gives K to 2, 6 to
   8 and 9 to 12 forms and only the I-statement for 3 to 5; the 3 to 5 frame grew the rest. Results: the goal steps
   card reads "goal, steps, block and plan, check" from grade 3 week 27 (SEL 3 to 5 day 54, PE 3 to 5, health 3 to 5),
   while section 7 lists those four steps as the 6 to 8 change and 6 to 8 day 1 calls the same words both "the grade 5
   form" and something "a class new to the card meets here". K to 2 grade 2 puts "I hear ___; I think ___ because ___"
   on the talk turn card (days 131, 134, 135), a line section 7 does not hold. Fix: the lead writes the 3 to 5 row of
   each card into section 7 (talk turn four steps, calm-down four steps with its three body tools, goal steps four
   steps, refusal as in finding 3), states that the goal steps card keeps its four steps through 6 to 8 and grows only
   in 9 to 12, and either adds the grade 2 talk line to section 7 or names it in K to 2 as a separate disagree frame,
   not the card. **frame**

6. **6 to 8's unit titles left STANDARD behind, and the 9 to 12 frame cites the old ones.** SEL 6 to 8 retitled 17 of
   its 18 units (for example grade 8 unit 14 "Values that cost", 15 "Heavy weeks", 17 "Hard talks and fair deals"). The
   9 to 12 frame's Picked up table names every grade 8 unit by STANDARD's title ("Values and integrity", "Stress, focus
   and rest", "Communication and conflict", "How I decide", "Understanding others", "Making a difference"; 40 rows), and
   STANDARD section 3's health-adjacent list names "Stress and strong feelings" and "Under pressure", which no course
   uses now. Every unit number in the 3 to 5, 6 to 8 and 9 to 12 Picked up tables matches the earlier band's days (120
   rows checked). Fix: the 9 to 12 frame table uses the 6 to 8 titles; STANDARD section 3 says once that frame titles
   win over the table's draft titles, or takes the 6 to 8 titles. **frame**

7. **Repeated projects and task forms.**
   - Grade 12 runs a book drive twice: unit 21's service project (days 215 to 217) and unit 23's community fix, "a book
     drive by default" (days 241 to 243). K to 2 grade 2 also ran a book swap shelf (day 175).
   - A real class improvement project closes the year in grades 2 (unit 18), 4 (unit 11), 5 (unit 17), 6 (unit 6), 7
     (unit 12), 8 (unit 18), 9 (unit 6), 11 (unit 18) and 12 (units 21 and 23). Grade 5 day 170 and grade 6 day 56 both
     take a proposal to the student council in consecutive years, across a band seam, and no scope names what the
     later proposal adds; inside 6 to 8 the three proposals (days 54, 118, 182) are told apart only by the depth
     ladder's words. STANDARD gap D asks for student voice in school life, so the form is right; the sameness is not.
   - Grade 11 day 152 rehearses "an offer sheet with a hidden fee, found only by the planned questions"; grade 12's
     owner-year Check (day 244) puts "an offer sheet with a hidden term found only by the planned questions" on the
     unseen page, so the end-of-band item is a form students met the year before.
   Fix: unit 23's default community fix becomes something other than a book drive (my pick: a printed guide for new
   ninth graders, inside school); the grade 6 unit 6 note on day 54 names the step up from grade 5 (the presentation
   chosen among options and weighed against the term, not the reasons-and-evidence sheet), and its audience is a grade
   team or the principal where grade 5 used the council; day 244's hidden term moves to a different document (a lease
   or a job offer letter) or the note names it as grade 11's form met at owner depth. **scope**

8. **9 to 12's four settled cases are all segregation rulings, two of them school segregation in back-to-back years.**
   Mendez v. Westminster (grade 9 day 43), Brown v. Board (grade 10 day 85, a settled return from grade 5 day 153,
   DESK 2026-11-26), Morgan v. Virginia (grade 11 day 182) and Heart of Atlanta (grade 12 day 224). Each is a different
   community or setting (Mexican American families, schools nationwide, interstate buses, public accommodations), and
   the U.S. Courts page says the Mendez arguments were later used in Brown, which is a reason, but no day names it.
   Day 43 says "a federal court found ... (1947)"; the page gives 1947 as the year the Ninth Circuit upheld the
   trial court's ruling. The facts on days 90, 164 and 182 match their pages (opened today). Fix: day 43 reads "a
   federal appeals court upheld in 1947"; day 85's note names Mendez as the year-before case Brown's lawyers drew on;
   the 9 to 12 scope's Settled cases bullet names the arc (schools, then travel, then public places). No case changes.
   **scope**

9. **The cultural picks have no register across the bands.** 3 to 5 says its three cultural sources come from three
   places and not from PE's, the arts' or K to 2's picks (day 25); 6 to 8 only keeps day 71's pick apart from unit 6's
   (day 57); 9 to 12 days 26, 85 and 230 name a source at the unit plan with no rule against an earlier band's place.
   K to 2 uses Ghana (Ampe, day 47) and Japan (acchi muite hoi, day 112). Why it matters: unit plans are written band
   by band, so the same place can come back as "one person's way" three times. Fix: one line in STANDARD section 5 and
   each frame's Sensitivity bullet: a place already used for a game or custom in any SEL band (and in that grade's PE
   and arts) is not used again; the unit plan lists the places used so far. **frame**

10. **Begun AASL ids are coded in 9 to 12 only.** 9 to 12 writes `~AASL.V.D.1`, `~AASL.V.D.2` and `~AASL.III.D.2` in the
    codes column on begun-year days (days 1 to 4, 9, 10 and on); K to 2, 3 to 5 and 6 to 8 name the AASL ids only in
    notes on begun years and code them only in the owner year. No progression row's `standard` carries them (the 9 to
    12 scope's For the lead 4). Fix: drop the `~AASL` codes from 9 to 12's begun years and keep the notes, as the other
    three do; that closes For the lead 4. **scope**

11. **All four scopes leave most owned codes off the course-level checks, and each asks the lead on its own.** The
    owner-year checks sample 8 owned codes in K to 2, 11 in 3 to 5, 12 in 6 to 8 and 12 in 9 to 12 (of 43 each); the
    rest are assessed at their own units' ends, and 3 to 5 For the lead 1 and 9 to 12 For the lead 2 ask whether to
    widen the frame's two-sample cap. The reason is the same everywhere: six units a year each with its own end-of-unit
    assessment (STANDARD section 2) and a check of one session. Fix: one call for the group, recorded once in STANDARD
    section 2: the unit's own end-of-unit assessment is rule 3's named reason for an owned SEL code not on a course
    check, and the cap stays; the two For the lead items are then closed. **frame**

12. **K to 2's once-a-week path puts grade 1 and grade 2 checks in health's week.** On the scope's short path a grade
    1 or 2 unit runs 5 sessions, so units 7 and 8 (13 and 14) fill sessions 1 to 10 and the mid-year check falls in
    session 11, week 11, the week of health grade 1's and grade 2's mid-year checks (CALENDAR.md table; rule 1 counts
    both). Kindergarten's short path runs its 8-session units in 4, grades 1 and 2 run theirs in 5. The K to 2 and 6 to
    8 scopes do not state their short-path check weeks; 3 to 5 (grade 3 weeks 11 and 27, grade 4 15 and 26, grade 5 15
    and 27, all clear) and 9 to 12 do. Fix: on the once-a-week path, grade 1 unit 7 and grade 2 unit 13 run in 4 as
    kindergarten's 8-session units do (2 shared, 1 Application, 1 Check and Respond), the mid-year check moves to
    session 10 (week 10, clear of health's 11 and every core week), and units 12 and 18 take the freed session (6); K to
    2 and 6 to 8 add their short-path check weeks. **scope**

13. **The rule 2 counting tool does not see SEL.** scripts/unit_skeleton.py's SUBJECTS list holds the four core
    subjects only, so sequence.py prints no retrieval or readiness notes for any SEL course (3 to 5 For the lead 2 says
    so; the other three checked by hand). Finding 1 is the kind of miss the tool would print. Fix: add SEL (and the
    other after-core subjects) to SUBJECTS so `sequence.py check` reports rule 2 for them. **structure**

## What holds

- Every one of the 520 progression rows is taught on a day, each has an Understanding day, and every owner row sits in
  grade 2, 5, 8 or 12. No begun `~` row is left without its owner year.
- Every row's `assumes` is in the `retrieves` of the day that first models it, in all four bands, except 6 to 8 day 1
  (finding 1). All 120 Picked up rows in the 3 to 5, 6 to 8 and 9 to 12 frames name the right unit on both sides.
- The I-statement and the calm-down card grow cleanly through the bands and match health and PE word for word
  ("I feel ___ when ___. I need ___." to the five-part 9 to 12 form; "stop, breathe" to "stop, breathe, name it,
  choose, go on"); the talk turn card grows the same way, with health's listening card its first steps.
- The health lean claims checked against health's own days (on health's 140 and 150-day year spans) all hold: each
  "comes first" or "same weeks" is true.
- Check weeks across all 13 grades sit where CALENDAR.md puts them, with no stagger break on the full path; dose is
  40, 60, 60 and 80 minutes a week as STANDARD section 2 sets, and every year is 64 sessions with a 4-a-year short year.
- No settled court or history case repeats inside a band; Brown's return in grade 10 is the settled exception and
  names its new depth. A partner never plays the push in any band.

## Sources

- U.S. Courts, "Mendez v. Westminster: how a young girl's courage transformed schools",
  https://www.uscourts.gov/data-news/judiciary-news/2024/09/26/mendez-v-westminster-how-a-young-girls-courage-transformed-schools,
  opened 2026-11-26 (Ninth Circuit upheld in 1947; arguments later used in Brown).
- Library of Virginia, Irene Morgan, https://www.lva.virginia.gov/collections/educator-resources/changemakers/items/show/44,
  opened 2026-11-26 (Supreme Court, June 3, 1946, Virginia's law on interstate passengers).
- National Park Service, "Who was excluded?", https://www.nps.gov/articles/who-was-excluded-women-s-suffrage.htm,
  opened 2026-11-26 (supports 6 to 8 day 90).
- ADA.gov, introduction to the ADA, https://www.ada.gov/topics/intro-to-ada/, opened 2026-11-26 (what the law covers;
  the page gives no signing date, which 6 to 8 day 164 takes from the National Archives page, as its fix report says).
- Oyez pages for Morgan and Heart of Atlanta (https://www.oyez.org/cases/1940-1955/328us373,
  https://www.oyez.org/cases/1964/515): browser check, as the 9 to 12 scope already lists.

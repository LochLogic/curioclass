# Frame read: Health, grades 3 to 5, 6 to 8 and 9 to 12 (2026-11-25)

Expert cold read, one combined read of three band frames, written 2026-11-25 on the pattern of the fixed K to 2 pilot.
Reader: Curio Class curriculum expert agent (fresh run). Brief: docs/pipeline/briefs/frame-read.md with the lead's
after-core changes (subject health; seams between bands; shared ground with the SEL and PE frames of each band;
sensitive topics; sources for health facts; the 6 to 8 dose question; stagger clashes listed, not counted).

## What I read

- AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/health.md; docs/courses/health/STANDARD.md and APPROACH.md.
- In full: docs/courses/health-grades-3-to-5/frame.md, health-grades-6-to-8/frame.md, health-grades-9-to-12/frame.md.
- The pilot: docs/reviews/frame-health-grades-k-to-2-fixes-2026-11-25.md (findings and pattern notes) and the card
  words and grade 2 units of docs/courses/health-grades-k-to-2/frame.md.
- Neighbor seams: the health sections of the SEL frames 3 to 5, 6 to 8 and 9 to 12, their units tables, and SEL
  STANDARD.md section 7 ("Shared steps"); the health sections and For the lead notes of the PE frames 3 to 5, 6 to 8
  and 9 to 12.
- Data: data/plans/frames.csv rows, data/plans/course-list.csv (health-grades-9-to-12), data/plans/calendar.csv,
  the cited rows of data/progressions/health.csv and physical-education.csv, data/standards/hecat-topics.txt.
- Scripts: `plan.py check` (0 failures for the three frames), `frame.py check` for each (0 failures; unit days
  3-5: 26, 26, 25; 6-8: 44 a year; 9-12: 76 of 80), `progression.py check health` (207 rows, 0 failures),
  `stale.py check` (1 failure, in the PE 9 to 12 frame, not health), `frame.py calendar` (clashes below).
- Outside sources opened: CDC, "Physical Activity Guidelines for Children" page
  (https://www.cdc.gov/physical-activity-basics/guidelines/children.html, page dated 2025-12-04). The CDC YRBS 2023
  fact sheet address I tried returned 404; survey figures below are from memory and marked so.

## Verdict

All three frames are sound in their bones: the day arithmetic holds, every owned indicator sits in one unit (the
gate agrees), every HECAT outcome in each band's column of the STANDARD.md section 4 map is served by a unit I could
trace, the two-topic rule is counted with sensitive rows out, and the sensitive units follow every line of
STANDARD.md section 5 (own units, a non-sensitive owner for every skill practiced, getting help taught twice, leave-out
and family notes two weeks ahead, scripts only, 988 and the abuse hotline by purpose, the 18-or-over rule in 9 to 12).
The biggest risk is the shared ground: the frames were written before or beside the SEL and PE frames and did not
pick up what those frames now say, so the I-statement words, the refusal and listening cards and every SEL unit
number in grades 4, 5, 7 and 8 disagree with the neighbor frames, and one physical activity fact (the "three kinds"
of activity) is wrong in a progression row and grade 3 unit 1. The one change that matters most: rewrite the SEL and
PE Cross-subject tables and the step-card words in all three frames from the landed SEL and PE frames and SEL
STANDARD.md section 7.

Per frame: **3 to 5** sound, fix the I-statement, the activity fact and the SEL and PE seams. **6 to 8** sound, the
strongest of the three on sensitive design; fix the card words, the SEL unit numbers and the shared-project
contradiction, the stale clash note and the unit 7 harassment line. **9 to 12** sound and fits its semester; fix the
stale term and neighbor notes and the unit 2 norm framing.

## Findings

Counts: serious 3, moderate 6, minor 5, judgment calls 4 (18). Clashes are listed in their own section and not
counted.

### Serious

**S1. The I-statement words break the one-card rule.** LAYER frame. REPEAT yes (K to 2 expert finding 6).
- What is wrong: the 3 to 5 frame sets the grade 3 form "I feel ___ when ___ because ___. Please ___." (Course in
  brief, Reading level; Models carried; unit 4 day 1; the SEL paragraph of Cross-subject, which calls it "health's
  words"), and the 6 to 8 frame copies it (Reading level; Models carried). Health K to 2 teaches "I feel ___ when
  ___. I need ___." (its unit on feelings), and SEL STANDARD.md section 7, "Shared steps" (2026-11-25), fixes the
  grades 3 to 5 form as I feel, when, because, I need. SEL 3 to 5's For the lead 4(a) already asks health to take
  "I need ___".
- Why it matters: every grade 3 to 8 communication day, sentence frame and check item would be written on a card
  that changes its last slot between K to 2 health, SEL and 3 to 8 health, so a child meets two cards in one week.
  A writer builds wrong days from it.
- Fix: in both frames replace "Please ___." with "I need ___." everywhere the I-statement is quoted, and in 3 to 5
  Models carried write "grade 3 form: 'I feel ___ when ___ because ___. I need ___.' (because added to the K to 2
  card)". The polite request ("please") may stay as a sentence frame for the ask-for-help step in unit 10, not as
  the I-statement.

**S2. "The three kinds" of activity are wrong.** LAYER progression and frame. REPEAT new.
- What is wrong: 3 to 5 unit 1 day 3 and row g3-pa-active-and-invite say "an hour of activity a day and the three
  kinds that build the heart, muscles and flexibility". The federal guidelines name aerobic, muscle-strengthening and
  bone-strengthening activity (muscle and bone at least 3 days a week inside the daily 60 minutes); flexibility is
  not one of them (CDC children's guidelines page, dated 2025-12-04; HHS Physical Activity Guidelines for Americans,
  2nd edition, 2018). PE 3 to 5 unit 4 teaches flexibility as a health-related fitness part, which is a different
  model, so the health line blurs the two.
- Why it matters: a factual error in the health course's one physical activity fact for grade 3, taught beside a PE
  chart that uses other words. Firm (two sources agree).
- Fix: row and unit 1 day 3 read "an hour of activity a day, most of it heart-pumping (aerobic), with muscle-strengthening
  and bone-strengthening activity at least three days a week (CDC, Physical Activity Guidelines for Children, page
  dated 2025-12-04)". The row's words column drops "stretch" or keeps it only under warm-up. The Cross-subject PE
  line already says health does not teach the fitness parts chart; add "flexibility is PE's fitness part, not one
  of the guideline's three kinds".

**S3. The SEL and PE seams are not written from the landed frames.** LAYER frame. REPEAT yes (K to 2 expert
finding 2 and pattern note "write the PE and SEL seams from their frames' unit numbers and calendar.csv weeks").
- What is wrong, by frame:
  - SEL unit numbers. The SEL frames number units across the band (1 to 18). Health uses per-grade numbers from the
    SEL row notes, so grade 3 and grade 6 match by luck and the rest are wrong. 3 to 5: SEL "grade 4 unit 2" is SEL
    unit 8 (weeks 6 to 10), "grade 4 unit 4" is unit 10 (weeks 16 to 21), "unit 5" is 11 (21 to 25), "unit 6" is 12
    (27 to 32); "grade 5 unit 1" is 13 (1 to 5), "unit 2" is 14 (6 to 10), "unit 4" is 16 (16 to 21), "unit 5" is 17
    (21 to 26), "unit 6" is 18 (27 to 32). The same wrong numbers sit in the Why column of units 8, 10, 11, 12, 15,
    17, 18 and 19. 6 to 8: grade 7 "SEL unit 2" is unit 8, "unit 5" is 11, "unit 6" is 12; grade 8 "unit 1" is 13,
    "unit 2" is 14, "unit 4" is 16, "unit 5" is 17, "unit 6" is 18, also in the Why column of units 11, 12, 17, 24
    and 25. 9 to 12 gives no SEL or PE unit numbers at all (its For the lead 4 defers them).
  - "If SEL comes first / later" hedges that the SEL frames now settle with weeks (3 to 5 rows g3-sa-name-feelings,
    g3-rel-stand-up, g4-sa-feel-think-link, the grade 4 and 5 rows; 6 to 8 g6-rel-ask-offer-help, g7-rel-stand-up,
    g8-rds-check-facts).
  - A contradiction: 6 to 8 says health's unit 26 team habit and SEL's term project "may be the same project if both
    teachers agree"; SEL 6 to 8 says they cannot be, since SEL unit 18 runs weeks 27 to 31 and health unit 26 weeks
    18 to 22.
  - PE stale and incomplete. 3 to 5 says "The PE grades 3 to 5 frame is not written" and gives no PE unit numbers;
    PE 3 to 5 is written and cites health units 1, 2, 3, 5, 8, 15 and 18 against PE units 1, 4, 5, 7, 9, 17, 18, 20
    and 23. PE 3 to 5 For the lead 6 asks that grade 5 keep one log, not two (health unit 15's habit log tracks the
    PE unit 17 goal); health's unit 15 does not say so. 6 to 8 records 4 PE rows by row only; PE 6 to 8 names more
    shared rows (g7-rest with g7-phw-sleep-habits-community, g7-settle-disagreements with health unit 11,
    g7-manage-feelings with health unit 3, g8-fitness-test-track and g8-goals-obstacles with the health goal rows)
    and gives its units and weeks (units 7, 13, 14, 15, 18). 9 to 12 names PE rows with no units; PE 9 to 12 places
    them in units 6, 8, 10 and 12.
- Why it matters: unit planners would write retrievals from the wrong SEL unit, keep teaching steps "in case SEL is
  later" when the order is known, and plan two logs or one shared project against what the neighbor frame says.
- Fix: rebuild each frame's SEL and PE tables from those frames' units tables and data/plans/calendar.csv (unit
  number and weeks in both columns), delete every hedge the weeks settle, and correct the Why column references
  above. 6 to 8 unit 26: "SEL unit 18 runs after it (weeks 27 to 31) and opens with the team habit as retrieval; they
  are not one project". 3 to 5 unit 15: "where PE runs, the student's activity habit is the PE unit 17 goal; one
  log". 9 to 12: drop For the lead 4 and write the numbers in.

### Moderate

**M1. Refusal and listening cards ignore what K to 2 and SEL already taught.** LAYER frame. REPEAT yes (K to 2
finding 6).
- Wrong: 3 to 5 Models carried calls refusal-steps "New in grade 4" though K to 2 grade 2 unit 13 teaches a "no
  thanks" line (g2-t-no-thanks-smoke) and SEL 3 to 5 unit 5 (grade 3, weeks 22 to 26) teaches a four-step refusal
  card. The listening card changes words each band (K to 2 "look, quiet body, wait, say back"; 3 to 5 "look, wait,
  ask one question, say back"), and SEL STANDARD.md section 7 says the talk turn card's two steps open health's
  listening card.
- Fix: refusal-steps row: "From K to 2 grade 2 unit 13 (no thanks) and SEL unit 5 (grade 3); health grade 4 unit 12
  opens with that card as retrieval and adds 'a reason is optional' and leaving". Listening: take SEL 3 to 5's pick
  (the talk turn card's words) or state in one line why health keeps its own; the 6 to 8 and 9 to 12 Models carried
  rows copy the result. This is SEL 3 to 5 For the lead 4(b) and 4(c).

**M2. Stale lead notes and stale Cross-subject lines.** LAYER process. REPEAT yes (K to 2 expert finding 2).
- Wrong: 9 to 12 For the lead 1 asks the lead to set `term` to `fall`; course-list.csv already says `fall` and
  calendar.csv already places the course in weeks 1 to 16. 9 to 12 For the lead 4 and its Cross-subject lines ("set
  by the PE frame", "set by its frame") and 3 to 5's "The PE grades 3 to 5 frame is not written" and For the lead 5
  and 6 ("when its frame is written") are stale: those frames have landed. 6 to 8 For the lead 2 says `frame.py
  calendar` shows no clash with the after-core frames; it now shows PE 6 to 8 on school day 84 in grades 6, 7 and 8.
  stale.py does not catch these (no Pending markers).
- Fix: rewrite each as what is now true: 9 to 12 item 1 deleted (term is fall); item 4 replaced by the numbers of
  S3; 3 to 5 items 5 and 6 become "SEL and PE cite health units ..." with any open choice only; 6 to 8 item 2 names
  the day 84 clash (Clashes section) for the calendar pass.

**M3. The two grade 5 dead ends are treated differently at each end.** LAYER progression. REPEAT new.
- Wrong: 3 to 5 lists g5-fn-claims-that-hurt and g5-s-online-safety under "Threads that end inside the band"; 6 to 8
  (Seams and For the lead 4) says both should hand on, to g7-fn-judge-claims and g7-s-online-boundaries. STANDARD.md
  section 4's key backs 6 to 8: fads (PHW 12) are first met in grade 5 and judged in grade 7.
- Fix (settled below): take 6 to 8's pick. In health.csv, g5-fn-claims-that-hurt hands_on `g7-fn-judge-claims` and
  g5-s-online-safety hands_on `g7-s-online-boundaries`, each grade 7 row's assumes adds it; 6 to 8 adds the two
  readiness checks it names (last ten minutes of unit 12 and unit 13); 3 to 5 drops both rows from its "threads that
  end" line and adds them to Handed on. The grade 5 cells are the lead's to apply.

**M4. The 9 to 12 unit 2 norm states a minority as the norm.** LAYER frame. REPEAT new. Confidence: likely.
- Wrong: unit 2 day 1 uses the YRBS share of high school students active 60 minutes every day as its norm figure.
  From memory (the CDC fact sheet I tried returned 404), that share is about one in four (2023 YRBS), so the
  "what most peers really do" day would tell students most peers do not do the healthy behavior. APPROACH.md and bar
  criterion 4 use the norm to correct overestimates of risk behavior; a figure showing the healthy behavior is rare
  works against it.
- Fix: keep the figure, but as the gap the unit explains (its question is "why does a teen who wants to be more
  active often not do it"), not as the course's norm; the Course in brief names units 11 and 12 as the two norm days
  (both "most do not"), plus, if a third is wanted, a YRBS item where most do the safe thing (for example, not riding
  with a driver who had been drinking), picked and dated at the unit plan.

**M5. 6 to 8 unit 7 does not fence off sexual harassment.** LAYER frame. REPEAT new.
- Wrong: unit 7 (non-sensitive) teaches "bullying and harassment in person and online"; its Out line names only
  dating violence. Sexual harassment is sensitive content (STANDARD.md section 5 rule 1; units 9 and 20 here).
- Fix: unit 7 Out: "sexual harassment and unwanted touch (sensitive units 9 and 20); harassment here means
  non-sexual harassment (name-calling, threats, exclusion, rumors)". Same note in the row g6-v-bullying-harassment-help.

**M6. Health facts are named but none was checked at source.** LAYER frame. REPEAT new.
- Wrong: all three frames name sources by agency ("a national pediatrics association's puberty pages", "a national
  eating disorders association's guidance", "the national survey of grade 8 students"), with "year at the expert
  read" and links "named from memory". That is allowed at the frame layer, but it left one fact wrong (S2) and gave
  no exact page for the sensitivity reads of the puberty, eating disorders and dating violence units. NHTSA pages
  stay browser check (6 to 8 For the lead 7).
- Fix: each frame's Sensitivity reads bullet gets one line: "the unit planner names the exact page and its date for
  each named source before the unit plan's expert read; a page that refuses an automated read is browser check".
  My spot checks are in "Settled" and Sources.

### Minor

**m1.** 6 to 8 unit 12 day 3 "buckle up and ride in the back seat": NHTSA's rule is the back seat for children under
13 (from memory). Fix: "ride in the back seat until age 13 (NHTSA, year at the expert read)", since grade 7 students
turn 13. LAYER frame. New.

**m2.** 9 to 12 unit 12 day 1 "naloxone ... rules on carrying it vary by state": nasal naloxone has been sold over
the counter since 2023 (FDA, from memory); what varies is state and school rules for students carrying it. Fix the
wording. LAYER frame. New.

**m3.** 9 to 12 unit 21 names SAMHSA, "Preventing Suicide: A Toolkit for High Schools" with no year (2012, from
memory). Fix: name the year and have the expert read confirm it is the latest edition or name its successor. LAYER
frame. New.

**m4.** 9 to 12 day 36 (mid-course respond day, the first lesson of week 8) carries the respond work, the week 8
goal slot (ten minutes) and the g7-s-online-boundaries readiness check (ten minutes), leaving 25 minutes to respond.
Fix (settled): the week 8 goal slot moves to day 37. LAYER frame. New.

**m5.** 3 to 5 unit 4 and 6 to 8/9 to 12 spoken-record days hear a third or half of the class "while others write"
inside one lesson (30 minutes in 3 to 5). Fix: the unit plan sets the record as two or three short pair stations,
not one-at-a-time to the teacher; no frame change beyond one line in End-of-unit evidence. LAYER frame. New.

### Judgment calls

**J1. The 6 to 8 dose (already with Cory).** 48 lessons a year of 45 minutes (36 hours) against APPROACH.md's "about
45" (34). The reason holds: three lessons every two weeks is a timetable a middle school can run, the arithmetic is
right (24 unit days before the day 25 mid-year check, 20 after, checks on days 25 and 47, respond on 48), and both
checks land off every core check week. The cost is one stagger clash with PE on day 84 (below), which the lead's
pass can move either course out of. My view: keep 48. Cutting to 45 would take three days from units that already
run four to seven days with a model and a pair day each.

**J2. Two-day sensitive units.** In all three frames a sensitive unit's second day holds the scripted practice and
the end-of-unit check (in 3 to 5, inside 30 minutes). It keeps the optional days small, which helps a school that
leaves them out; it is thin for a school that keeps them. My view: keep two days, and let each sensitive unit's
leave-in note say a school may add one day of practice before the check.

**J3. Puberty in two grade 4 lessons (3 to 5 For the lead 7).** Agree with the frame's pick (keep two; it returns in
unit 21), provided the HECAT Sexual Health 3 to 5 read at the unit plan does not list more expectations than two
lessons hold; if it does, add the day from unit 11's slack, not a new unit.

**J4. The 9 to 12 goal thread.** Unit 16 owns three indicators in two days and relies on ten ten-minute slots in
units 2 to 15. Cory accepted this shape; it holds as long as each unit plan of units 2 to 15 shows its slot day and
plans 35 minutes on it. No change.

## The lens checklist (course frame layer)

| Line | 3 to 5 | 6 to 8 | 9 to 12 |
|---|---|---|---|
| All eight standards in the band | Met | Met | Met |
| Each skill standard in two topics (sensitive out) | Met | Met | Met |
| Coverage map with unit names | Met (cells traceable to units; the scope and sequence writes the table) | Met | Met |
| No topic taught once with nothing after | Met | Met | Met (last course; returns inside the semester) |
| Sensitive units removable (no skill only there, no later unit needs one, leave-out note) | Met | Met | Met |
| Getting help outside sensitive units every year | Met (3, 10, 16, 17) | Met (2, 11, 24) | Met (4, 8) |
| Indicators in the right span | Met | Met | Met |
| Norms worked on directly | Met (plain words below grade 6) | Met (figures, latest edition) | Missed in part (M4) |
| No body or weight focus, no calories, no good or bad foods | Met | Met | Met |
| Suicide and self-harm: no method, help line, adult plan | Not applicable | Met | Met |
| Families in the loop, opt-out path, 18-or-over rule | Met | Met | Met |
| Health and PE neither both nor neither on activity | Met in substance, seams stale (S3) | Met in substance, seams incomplete (S3) | Met in substance, no unit numbers (S3) |
| Science model used, not retaught | Met | Met | Met |
| Facts few, accurate, dated | Missed once (S2) | Met at frame level | Met at frame level |

## Stagger clashes (listed, not counted; the lead's calendar pass)

From `frame.py calendar` on 2026-11-25:
- Grade 3: week 15 health and music; week 29 health and library.
- Grade 4: week 14 health and library; week 29 health, ELD and library. SEL 3 to 5 also notes its week 15 check
  beside health's grade 4 respond day (respond days are not counted by the script).
- Grade 5: week 15 health, music and SEL; week 28 health, ELD and library (health moved to week 28 to dodge the grade
  5 social studies check in week 29).
- Grades 6, 7 and 8: school day 84 (week 17) health and PE in each grade. PE 6 to 8 For the lead 6 offers weeks 19 to
  21 (grades 6, 7) and 19, 21 to 23 (grade 8) for PE; health's mid-year check could instead move to day 85 or 86 only
  if its own unit boundaries shift, so PE moving is the cheaper pick.
- 9 to 12: no stagger rule except finals week (week 16); none found.

## What is right and should not be touched

- The sensitive design: own units at the end of each year, a named non-sensitive owner for every skill they practice,
  no course-level check samples them, the fallbacks when an earlier sensitive unit was left out, the 6 to 8 and 9 to
  12 safe-messaging lines and counselor notice, the 18-or-over rule.
- Doing records for "do" indicators (units 9, 15, 19 in 3 to 5; 26, 27 in 6 to 8; 7, 14 to 18 in 9 to 12), scored on
  steps, never on health or whether a goal worked, with a character's log never standing alone.
- The plain-word norm below grade 6 and the survey figure from grade 6, per the pilot.
- Step-card handling (model, pairs, withdrawn, check without) and the one-day return of a carried card.
- Every handoff pair 3 to 5 to 6 to 8 and 6 to 8 to 9 to 12 agrees at both ends except M3.

## What I could not judge

- Whether the HECAT 2021 module span tables add expectations the units cannot hold (owed at the unit plans).
- Current survey figures (YRBS 2023, NYTS 2024, Monitoring the Future 2024): not opened; M4 and the norm days rest on
  memory until the expert read.

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| I-statement grade 3 form "I feel ___ when ___ because ___. I need ___." | One card across K to 2, SEL and health (SEL STANDARD section 7) | health 3-5 and 6-8 frame.md |
| Grade 3 activity line: aerobic most of the hour, muscle and bone at least three days a week | CDC children's guidelines page, 2025-12-04 | health.csv g3-pa-active-and-invite; health 3-5 frame.md unit 1 |
| The two grade 5 dead ends hand on to g7-fn-judge-claims and g7-s-online-boundaries, with 6 to 8's two readiness checks | STANDARD section 4 key places fads in grades 5 and 7 | health.csv; health 3-5 and 6-8 frame.md |
| 9 to 12 unit 2's activity figure is the gap the unit explains, not a norm day | Norm days state what most peers do (bar criterion 4) | health 9-12 frame.md |
| 9 to 12 week 8 goal slot on day 37, not day 36 | The respond day already holds a readiness check | health 9-12 frame.md |

## For Cory

- Supplies ceilings (money): 3 to 5 printing $18, $19, $20 a year (pick $30 a year for a class of 30, as K to 2);
  6 to 8 $32, $31 ($46 with a bought helmet), $39 (pick $40 a year, helmet outside); 9 to 12 $68 a semester, $113
  with the optional no-cook demonstration (pick $70, the demonstration outside).
- The 6 to 8 dose (already put to you): my read supports keeping 48 lessons a year (J1).

## Sources

- CDC, Physical Activity Guidelines for Children, https://www.cdc.gov/physical-activity-basics/guidelines/children.html
  (page dated 2025-12-04): the three kinds of activity (S2).
- CDC YRBS 2023 fact sheet, https://www.cdc.gov/healthy-youth/data/yrbs/2023/factsheet.html: returned 404; M4 rests
  on memory.
- From memory, not opened: HHS Physical Activity Guidelines for Americans, 2nd edition (2018); NHTSA back-seat rule
  (m1); FDA over-the-counter naloxone approval, 2023 (m2); SAMHSA high school suicide prevention toolkit, 2012 (m3).

## For the source list

- The CDC children's physical activity guidelines page above opened to an automated read on 2026-11-25.
- The YRBS 2023 fact sheet address above is dead (404); the expert read needs the current YRBS results page.
